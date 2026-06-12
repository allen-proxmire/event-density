"""ED substrate simulator (empirical arc) — Milestone 1 core.

Faithful executable transcription of the closed ED-substrate specification:
discrete Sigma-maximization with a deterministic tie-break, never averaging.
Milestone 1 ships graph / state / sigma / tie-break only; the update loop,
strata, boundaries, and recorder follow in build order.
"""
from .graph import ParticipationGraph
from .state import NodeState, StateVector
from .sigma import compute_sigma, compute_candidates, coherence, SigmaCoeffs
from .update import apply_tiebreak, apply_update, step, hash_state
from .strata import compute_strata, assign_stratum_ids
from .boundary import (
    detect_decoupled_edges,
    detect_boundary_nodes,
    boundary_map,
)
from .recorder import HistoryRecorder

__all__ = [
    "ParticipationGraph",
    "NodeState",
    "StateVector",
    "compute_sigma",
    "compute_candidates",
    "coherence",
    "SigmaCoeffs",
    "apply_tiebreak",
    "apply_update",
    "step",
    "hash_state",
    "compute_strata",
    "assign_stratum_ids",
    "detect_decoupled_edges",
    "detect_boundary_nodes",
    "boundary_map",
    "HistoryRecorder",
]
