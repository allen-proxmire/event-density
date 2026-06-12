"""Reach-stratum detection — Build Step 5.

A reach stratum is a maximal set of nodes mutually reachable WITHOUT crossing a
decoupling surface — i.e. a connected component of the RECIPROCAL subgraph
G_recip = (V, { e : not decoupled(e) }). One-sided influence does NOT merge
strata (Phase E §6): only non-decoupled (reciprocal) edges are traversed.

Stratum numbering is deterministic: components are labelled in ascending order
of their smallest node id, so the same graph always yields the same ids.
"""
from __future__ import annotations

from .graph import ParticipationGraph
from .state import StateVector


def compute_strata(graph: ParticipationGraph) -> dict[int, int]:
    """Return node_id -> stratum_id over the reciprocal (non-decoupled) subgraph.

    BFS flood over non-decoupled edges only. Deterministic: seed nodes are taken
    in ascending id order and each new component gets the next id, so stratum ids
    are ordered by smallest member.
    """
    labels: dict[int, int] = {}
    next_id = 0
    for seed in sorted(graph.nodes()):          # ascending ⇒ deterministic labelling
        if seed in labels:
            continue
        sid = next_id
        next_id += 1
        # BFS over reciprocal edges from this seed.
        stack = [seed]
        labels[seed] = sid
        while stack:
            u = stack.pop()
            for v in graph.admissible_neighbors(u):   # non-decoupled only
                if v not in labels:
                    labels[v] = sid
                    stack.append(v)
    return labels


def assign_stratum_ids(state: StateVector, graph: ParticipationGraph) -> dict[int, int]:
    """Compute strata and write stratum_id onto every NodeState. Returns the
    mapping. Call at init for constructed surfaces (static); re-call after any
    decoupling-flag change (emergent mode, Build Step 6+)."""
    labels = compute_strata(graph)
    for node_id, sid in labels.items():
        if node_id in state:
            state[node_id].stratum_id = sid
    return labels
