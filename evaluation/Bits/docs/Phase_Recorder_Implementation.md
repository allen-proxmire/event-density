# Phase Bits / Recorder — Build Step 7 Implementation

**Program:** Determinability-boundary bits-measurement (empirical arc)
**Document:** Build Step 7 — HistoryRecorder
**Status:** **Implemented, run, PASS** — append-only, read-only, faithful export; simulator package complete (7/7); no regression
**Date filed:** June 2026
**Author:** Allen Proxmire
**Related:** `Phase_SimulatorDesign.md` §7; `Phase_SimulatorImplementationPlan.md` §3; `BuildStep7_Results.md`

---

## 1. Purpose

This document implements **Build Step 7 — `HistoryRecorder`**, per `Phase_SimulatorDesign.md` §7. The recorder is the simulator's instrumentation layer: it captures per-step ED substrate states, attaches the run's topology / strata / boundary metadata, and exports the trajectory for external analysis (entropy, MI, Δ).

It is the **last simulator component**. With it filed, all seven modules exist; what remains (Steps 8–10) is assembly and certification, not new code.

Design constraints, all upheld and verified (§6):

- **Append-only** — snapshots and the commit log are appended, never edited; history is itself irreversible, consistent with the substrate it records.
- **Read-only on state** — the recorder never mutates `NodeState`; recording cannot change the dynamics.
- **Analysis-oriented** — it computes no entropy/MI/Δ; it emits raw histories in the exact schema the external `analysis/` layer consumes (design §8).

The code below was written, executed, and **passes** (output §6; record in `BuildStep7_Results.md`). Steps 4–6 and Milestone 1 were re-run and still pass.

---

## 2. Recorder Design (in-memory, append-only)

The recorder holds four append-only buffers and static run metadata:

- **`_steps`** — list of step indices.
- **`_rho`** — list of per-step ρ rows, each `[|V|]` over the fixed node order.
- **`_orient`** — list of per-step orientation rows, each `[|V|, k]`.
- **`_commits`** — list of `(t, u, v)` commitment events.

Plus, fixed at construction: the **graph** (for topology/strata/boundary metadata), the ordered **node list** (column order for all arrays), the **strata** mapping, run **params**, and the ensemble **seed**.

The node order is fixed once (sorted ids) so every ρ/orientation row and every reload uses the same columns — essential for the Δ pairing, which indexes regions by node. Buffers only grow: `snapshot` and `log_commit` append; nothing is ever rewritten. `export` reads the buffers and writes files; it does not touch state.

---

## 3. Code — `Bits/simulator/recorder.py`

```python
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
```

Note: JSON object keys must be strings, so `strata` and `boundary_map` are emitted with **string keys** (`{'0': 0, …}`). This is deliberate and correct; the analysis layer parses them back to ints.

---

## 4. Integration with Update Loop

`step()` gains an optional recording hook — **non-breaking**:

```python
def step(state, graph, coeffs=SigmaCoeffs(), strata=None, recorder=None, t=None) -> int:
    ...
    for u in order:
        ...
        v = apply_update(u, state, graph, coeffs)
        if v is not None:
            commits += 1
            newly_active.add(v)
            if recorder is not None and t is not None:
                recorder.log_commit(t, u, v)          # per-commit log
    if recorder is not None and t is not None:
        recorder.snapshot(t, state)                    # per-step snapshot
    return commits
```

When `recorder`/`t` are omitted, `step` behaves exactly as in Build Steps 4–6 — all four prior demos re-run unchanged. Recording is read-only (snapshot copies values out of `NodeState`), so it cannot affect the dynamics; the demo verifies this by running with and without a recorder and confirming the final state is identical.

`__init__.py` now exports `HistoryRecorder`.

---

## 5. Minimal Demo — `Bits/examples/recorder_demo.py`

Two-cluster graph, one front per stratum, five steps, full recording; exports `.npz` + JSON to a temp dir, reloads, and verifies round-trip + no-perturbation + metadata.

```python
"""Build Step 7 demo - HistoryRecorder.

Runs a few steps on the two-cluster graph with one front per stratum, records
per-step rho/orientation + commit log, exports .npz + JSON, and reloads to
verify the round-trip. Also checks that recording does not perturb the run
(identical final state with and without a recorder).
"""
import json
import os
import sys
import tempfile

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from simulator import (  # noqa: E402
    ParticipationGraph, NodeState, StateVector, SigmaCoeffs,
    compute_strata, assign_stratum_ids, step, HistoryRecorder,
)

STEPS = 5


def build_two_clusters():
    g = ParticipationGraph()
    g.add_edge(0, 1, bandwidth=0.5)
    g.add_edge(1, 2, bandwidth=0.5)
    g.add_edge(3, 4, bandwidth=0.5)
    g.add_edge(4, 5, bandwidth=0.5)
    g.add_edge(2, 3, bandwidth=0.5, decoupled=True)
    return g


def fresh_state(g, seeds):
    sv = StateVector()
    for n in sorted(g.nodes()):
        sv[n] = NodeState(rho=0.0, orientation=np.array([0.0, 0.0]))
    for s in seeds:
        sv[s].active = True
    return sv


def run(record=True, prefix=None):
    g = build_two_clusters()
    sv = fresh_state(g, seeds=[0, 3])
    strata = assign_stratum_ids(sv, g)
    coeffs = SigmaCoeffs()
    rec = None
    if record:
        rec = HistoryRecorder(g, strata=strata,
                              params={"kc": coeffs.kc, "ks": coeffs.ks,
                                      "kg": coeffs.kg, "rho_star": coeffs.rho_star},
                              seed=0)
        rec.snapshot(0, sv)  # initial state
    for t in range(1, STEPS + 1):
        step(sv, g, coeffs, strata=strata, recorder=rec, t=t)
    final_rho = [sv[n].rho for n in sorted(g.nodes())]
    paths = rec.export(prefix) if (record and prefix) else (None, None)
    return final_rho, rec, paths


def main():
    print("=" * 64)
    print("BUILD STEP 7 - HistoryRecorder")
    print("=" * 64)

    tmp = tempfile.mkdtemp(prefix="ed_rec_")
    prefix = os.path.join(tmp, "run")

    final_rho, rec, (npz_path, json_path) = run(record=True, prefix=prefix)

    rho_hist = rec.rho_history()
    orient_hist = rec.orientation_history()
    commits = rec.committed_edges()
    meta = rec.metadata()

    print(f"\n  rho_history shape         : {rho_hist.shape}   (T x |V|)")
    print(f"  orientation_history shape : {orient_hist.shape}   (T x |V| x k)")
    print(f"  committed_edges shape     : {commits.shape}   (C x 3: t,u,v)")
    print(f"  final rho                 : {final_rho}")
    print(f"  metadata.strata           : {meta['strata']}")
    print(f"  metadata.decoupled_edges  : {meta['decoupled_edges']}")
    print(f"  metadata.boundary_nodes   : {meta['boundary_nodes']}")
    print(f"  exported npz              : {os.path.basename(npz_path)}")
    print(f"  exported json             : {os.path.basename(json_path)}")

    loaded = np.load(npz_path)
    rho_roundtrip = np.allclose(loaded["rho_history"], rho_hist)
    with open(json_path, encoding="utf-8") as fh:
        meta_loaded = json.load(fh)
    meta_roundtrip = (meta_loaded["strata"] == {str(k): v for k, v in meta["strata"].items()}
                      and meta_loaded["decoupled_edges"] == meta["decoupled_edges"])

    final_rho_norec, _, _ = run(record=False, prefix=None)
    no_perturb = (final_rho == final_rho_norec)

    monotone = bool(np.all(np.diff(rho_hist, axis=0) >= -1e-12))

    # Metadata correctness. (strata uses string keys: JSON-compatible.)
    meta_ok = (meta["strata"] == {"0": 0, "1": 0, "2": 0, "3": 1, "4": 1, "5": 1}
               and meta["decoupled_edges"] == [[2, 3]]
               and meta["boundary_nodes"] == [2, 3])

    print("\nChecks")
    print(f"  npz round-trip (rho)         : {rho_roundtrip}")
    print(f"  json round-trip (metadata)   : {meta_roundtrip}")
    print(f"  recording does not perturb   : {no_perturb}")
    print(f"  recorded rho monotone        : {monotone}")
    print(f"  metadata correct             : {meta_ok}")

    passed = (rho_roundtrip and meta_roundtrip and no_perturb
              and monotone and meta_ok)
    print("\n" + "=" * 64)
    print(f"BUILD STEP 7: {'PASS' if passed else 'FAIL'}")
    print("=" * 64)
    return passed


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
```

---

## 6. Acceptance Criteria for Build Step 7 — Result

Executed; **PASS** (exit 0). Recorded output:

```
================================================================
BUILD STEP 7 - HistoryRecorder
================================================================

  rho_history shape         : (6, 6)   (T x |V|)
  orientation_history shape : (6, 6, 2)   (T x |V| x k)
  committed_edges shape     : (10, 3)   (C x 3: t,u,v)
  final rho                 : [0.0, 3.0, 2.0, 0.0, 3.0, 2.0]
  metadata.strata           : {'0': 0, '1': 0, '2': 0, '3': 1, '4': 1, '5': 1}
  metadata.decoupled_edges  : [[2, 3]]
  metadata.boundary_nodes   : [2, 3]
  exported npz              : run.npz
  exported json             : run.json

Checks
  npz round-trip (rho)         : True
  json round-trip (metadata)   : True
  recording does not perturb   : True
  recorded rho monotone        : True
  metadata correct             : True

================================================================
BUILD STEP 7: PASS
================================================================
```

Regressions: boundary, strata, update_loop, milestone1 — all exit 0.

| Criterion | Result |
|---|---|
| No mutation of state (read-only) | **PASS** (identical run with/without recorder) |
| Correct metadata (topology/strata/boundary) | **PASS** |
| Clean export + faithful reload | **PASS** (`.npz` ρ + JSON metadata round-trip) |
| Append-only / monotone snapshots | **PASS** (Δρ ≥ 0) |
| No regression (M1, Steps 4–6) | **PASS** (all exit 0) |

**Factorization preview.** Final ρ = `[0,3,2, 0,3,2]` — the two strata are mirror-identical: independent fronts on isomorphic, decoupled clusters produce byte-identical fills. The strata evolved without cross-talk. This is the behavior Gate 3 will formally certify (Step 9); it is already visible.

**A demo-only fix, recorded for honesty.** The first run reported `metadata correct: False` — a bug in the *demo's assertion* (it compared strata against int keys), not in the recorder (which correctly emits **string** keys for JSON validity). Fixed the comparison; re-ran → PASS. The code was right; the test's expectation was wrong.

---

## 7. Next Steps (Preview)

| Step | Build | Unlocks |
|---|---|---|
| **8** | MWE (`examples/mwe_16node.py`) — two 8-node clusters, decoupled bridge, independent seeds, full recording | first measurement-shaped run |
| **9** | Full test suite (5 files) | **Gate 3 (factorization) executable** |
| **10** | Run all four gates on the MWE | acceptance: simulator certified → Δ opens |

---

## 8. Deliverables

Produced and verified:

- **`Bits/simulator/recorder.py`** — `HistoryRecorder` (append-only, read-only, `.npz` + JSON export with full metadata).
- **`Bits/simulator/update.py`** — `step()` recording hook (non-breaking).
- **`Bits/examples/recorder_demo.py`** — runnable; verifies round-trip, no-perturbation, metadata.
- **`Bits/BuildStep7_Results.md`** — recorded run and acceptance table.

**The simulator package is complete (7/7 modules).** Per program discipline, **no Δ is measured until all four gates pass** (Build Step 10). The next deliverable is the MWE.

---

## 9. Next Actions

Proceed to **Build Step 8 — the MWE** (`examples/mwe_16node.py`): two 8-node clusters joined by a decoupled bridge, independent seeds and initial conditions per cluster, evolved to the fixed point with full recording and export. This is the first measurement-shaped run and the substrate for the Gate 3 factorization test (Step 9) — where the across-boundary independence previewed here is formally certified.

---

*End of Build Step 7 implementation. The HistoryRecorder is live, append-only, read-only, with faithful `.npz` + JSON export; the simulator package is complete; a factorization preview is already visible in the symmetric two-stratum fill. The next deliverable is the 16-node MWE.*
