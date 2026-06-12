"""HistoryRecorder — Build Step 7.

Append-only instrumentation for ED substrate runs. Records per-step snapshots of
the commitment field (rho) and orientation, plus the committed-event log, and
exports the trajectory as a NumPy .npz (arrays) + a JSON sidecar (topology,
strata, decoupling surfaces, parameters). The recorder NEVER mutates the
simulation state — it only reads it. History is itself irreversible: snapshots
are appended, never edited.

Downstream consumers: the informational half of Gate 3 (across-boundary MI ≈ 0)
and the Δ computation both read these exports. The recorder computes no entropy,
MI, or Δ — it produces raw histories; analysis is external (Phase_SimulatorDesign
§8).
"""
from __future__ import annotations

import json
from typing import Optional

import numpy as np

from .boundary import boundary_map, detect_boundary_nodes, detect_decoupled_edges
from .graph import ParticipationGraph
from .state import StateVector


class HistoryRecorder:
    """Append-only recorder of an ED substrate trajectory.

    Build with the run's graph (for static topology/strata/boundary metadata) and
    the ordered node list. Call snapshot(t, state) once per step; call
    log_commit(t, u, v) per commitment; call export(prefix) to write files.
    """

    def __init__(self, graph: ParticipationGraph, nodes: Optional[list[int]] = None,
                 strata: Optional[dict[int, int]] = None,
                 params: Optional[dict] = None,
                 seed: Optional[int] = None) -> None:
        self.graph = graph
        self.nodes: list[int] = sorted(nodes if nodes is not None else graph.nodes())
        self._index = {n: i for i, n in enumerate(self.nodes)}
        self.strata = strata  # may be None at construction; can be set later
        self.params = dict(params) if params else {}
        self.seed = seed

        # Append-only buffers.
        self._steps: list[int] = []
        self._rho: list[list[float]] = []
        self._orient: list[list[list[float]]] = []
        self._commits: list[tuple[int, int, int]] = []  # (t, u, v)

    # ----- recording (append-only) -----

    def snapshot(self, t: int, state: StateVector) -> None:
        """Append a per-step snapshot of rho and orientation. Read-only on state."""
        rho_row = [float(state[n].rho) for n in self.nodes]
        orient_row = [[float(x) for x in np.asarray(state[n].orientation)]
                      for n in self.nodes]
        self._steps.append(int(t))
        self._rho.append(rho_row)
        self._orient.append(orient_row)

    def log_commit(self, t: int, u: int, v: int) -> None:
        """Append a committed-event record (t, source u, target v)."""
        self._commits.append((int(t), int(u), int(v)))

    # ----- views -----

    def rho_history(self) -> np.ndarray:
        """[T, |V|] commitment-density history (rows = steps, cols = self.nodes)."""
        return np.asarray(self._rho, dtype=float)

    def orientation_history(self) -> np.ndarray:
        """[T, |V|, k] orientation history."""
        return np.asarray(self._orient, dtype=float)

    def committed_edges(self) -> np.ndarray:
        """[C, 3] array of (t, u, v) commitment events (empty -> shape [0, 3])."""
        if not self._commits:
            return np.zeros((0, 3), dtype=int)
        return np.asarray(self._commits, dtype=int)

    # ----- metadata -----

    def metadata(self) -> dict:
        """Topology / strata / boundary / params metadata for the JSON sidecar."""
        edges = [
            {"u": int(u), "v": int(v),
             "bw": float(self.graph.bw(u, v)),
             "decoupled": bool(self.graph.is_decoupled(u, v))}
            for u, v in _undirected_edge_list(self.graph)
        ]
        strata = self.strata
        return {
            "nodes": [int(n) for n in self.nodes],
            "edges": edges,
            "decoupled_edges": [[int(u), int(v)]
                                for u, v in detect_decoupled_edges(self.graph)],
            "boundary_nodes": sorted(int(n) for n in detect_boundary_nodes(self.graph)),
            "boundary_map": {str(k): [int(x) for x in v]
                             for k, v in boundary_map(self.graph).items()},
            "strata": ({str(k): int(v) for k, v in strata.items()}
                       if strata is not None else None),
            "params": self.params,
            "seed": self.seed,
            "n_steps": len(self._steps),
            "n_commits": len(self._commits),
        }

    # ----- export -----

    def export(self, path_prefix: str) -> tuple[str, str]:
        """Write <prefix>.npz (arrays) and <prefix>.json (metadata). Returns the
        two paths. Does not touch simulation state."""
        npz_path = f"{path_prefix}.npz"
        json_path = f"{path_prefix}.json"
        np.savez(
            npz_path,
            nodes=np.asarray(self.nodes, dtype=int),
            steps=np.asarray(self._steps, dtype=int),
            rho_history=self.rho_history(),
            orientation_history=self.orientation_history(),
            committed_edges=self.committed_edges(),
        )
        with open(json_path, "w", encoding="utf-8") as fh:
            json.dump(self.metadata(), fh, indent=2, sort_keys=True)
        return npz_path, json_path


def _undirected_edge_list(graph: ParticipationGraph) -> list[tuple[int, int]]:
    """All edges as canonical (min, max) pairs, each once, sorted."""
    seen: set[tuple[int, int]] = set()
    for u in graph.nodes():
        for v in graph.neighbors(u):
            seen.add((min(u, v), max(u, v)))
    return sorted(seen)
