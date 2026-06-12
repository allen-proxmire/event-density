"""Decoupling-surface detection — Build Step 6.

A decoupling surface is an edge across which reciprocal participation fails
(B6). It is the empirical determinability boundary: strata are the connected
components of the reciprocal subgraph (strata.py), and the surfaces are the
edges that separate them. This module exposes those surfaces explicitly for the
factorization gate (Gate 3) and for Δ pairing.

Directionality. An edge (u, v) counts as a decoupling surface if it is decoupled
in EITHER direction:  decoupled(u, v) OR decoupled(v, u). One-sided decoupling
does not restore comparability, so a single decoupled direction is enough to
make the edge a boundary. The current ParticipationGraph stores the flag
symmetrically (a shared edge record), so both directions agree — this models the
RECIPROCAL-decoupling ("true boundary") case the MWE and Gate 3 use. The OR is
written directionally so that, were per-direction storage added later for
one-sided surfaces, detection would already be correct.

All returned structures are deterministic and sorted.
"""
from __future__ import annotations

from .graph import ParticipationGraph


def _undirected_edges(graph: ParticipationGraph) -> list[tuple[int, int]]:
    """All edges as canonical (min, max) pairs, each once, sorted."""
    seen: set[tuple[int, int]] = set()
    for u in graph.nodes():
        for v in graph.neighbors(u):
            seen.add((min(u, v), max(u, v)))
    return sorted(seen)


def detect_decoupled_edges(graph: ParticipationGraph) -> list[tuple[int, int]]:
    """Return the decoupling surfaces as sorted canonical (u, v) pairs.

    An edge is a surface iff it is decoupled in either direction. Deterministic.
    """
    surfaces: list[tuple[int, int]] = []
    for u, v in _undirected_edges(graph):
        if graph.is_decoupled(u, v) or graph.is_decoupled(v, u):  # directional OR
            surfaces.append((u, v))
    return surfaces


def detect_boundary_nodes(graph: ParticipationGraph) -> set[int]:
    """Return the set of nodes incident to at least one decoupling surface."""
    nodes: set[int] = set()
    for u, v in detect_decoupled_edges(graph):
        nodes.add(u)
        nodes.add(v)
    return nodes


def boundary_map(graph: ParticipationGraph) -> dict[int, list[int]]:
    """node_id -> sorted list of neighbors reachable only across a decoupling
    surface. Deterministic and stable across runs; used to anchor Δ pairings
    (the across-boundary partner of each boundary node)."""
    m: dict[int, set[int]] = {}
    for u, v in detect_decoupled_edges(graph):
        m.setdefault(u, set()).add(v)
        m.setdefault(v, set()).add(u)
    return {k: sorted(vs) for k, vs in sorted(m.items())}
