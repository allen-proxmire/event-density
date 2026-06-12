"""ParticipationGraph — B2 bandwidth-weighted participation graph.

Node ids are the B1 distinct identities; they also serve as the tie-break
final key (sigma) when bandwidths tie. Edges are reciprocal (undirected) by
default; a `decoupled` flag marks a decoupling surface (B6).
"""
from __future__ import annotations

from typing import Iterable


class ParticipationGraph:
    """Sparse adjacency-list participation graph (B2).

    Internal store: node -> {neighbor -> {"bw": float, "decoupled": bool}}.
    The same edge-data dict is shared by both directions so a flag flip is
    seen reciprocally.
    """

    def __init__(self) -> None:
        self._adj: dict[int, dict[int, dict]] = {}

    def add_node(self, node_id: int) -> None:
        """Register a node (no-op if it already exists)."""
        self._adj.setdefault(node_id, {})

    def add_edge(self, u: int, v: int, bandwidth: float,
                 decoupled: bool = False) -> None:
        """Add a reciprocal channel u<->v with the given bandwidth (B2 weight)."""
        self.add_node(u)
        self.add_node(v)
        data = {"bw": float(bandwidth), "decoupled": bool(decoupled)}
        self._adj[u][v] = data
        self._adj[v][u] = data  # shared dict ⇒ reciprocal

    def neighbors(self, u: int) -> list[int]:
        """All nodes adjacent to u (reciprocal and decoupled alike)."""
        return list(self._adj.get(u, {}).keys())

    def admissible_neighbors(self, u: int) -> list[int]:
        """Candidate set N(u): neighbors reachable via a NON-decoupled edge.
        Reach-bounded; respects decoupling surfaces (B6)."""
        return [v for v, d in self._adj.get(u, {}).items() if not d["decoupled"]]

    def bw(self, u: int, v: int) -> float:
        """Channel bandwidth on edge (u, v)."""
        return self._adj[u][v]["bw"]

    def is_decoupled(self, u: int, v: int) -> bool:
        """Whether edge (u, v) is a decoupling surface."""
        return self._adj[u][v]["decoupled"]

    def set_decoupled(self, u: int, v: int, flag: bool) -> None:
        """Set/clear the decoupling flag on edge (u, v) (reciprocal)."""
        self._adj[u][v]["decoupled"] = bool(flag)

    def nodes(self) -> Iterable[int]:
        """All registered node ids."""
        return self._adj.keys()
