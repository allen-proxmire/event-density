"""Sigma functional — Σ = Coh − Str − Grad. ORIENTATION-BLIND (Phase D §5).

HARD INVARIANT: compute_sigma and coherence read rho (B4) and graph-local
structure ONLY. They MUST NOT read NodeState.orientation (B5). Sigma being
orientation-blind is the basis of the stratified-orientation result; violating
it would corrupt the whole evaluation. Verified by the orientation-blindness
acceptance check (Milestone 1).

Note on signature: Sigma is intrinsically a property of a *transition* u -> v
(the Grad term needs both endpoints), so compute_sigma takes (u, v). This is
the implementation-plan signature; it supersedes the shorthand in the kickoff.
"""
from __future__ import annotations

from dataclasses import dataclass

from .graph import ParticipationGraph
from .state import StateVector


@dataclass(frozen=True)
class SigmaCoeffs:
    """Channel weights and parameters for Sigma. Qualitative roles are fixed
    (Coh stabilizing +, Str/Grad destabilizing -); magnitudes are tunable."""
    kc: float = 1.0          # coherence weight
    ks: float = 1.0          # strain weight
    kg: float = 1.0          # gradient-strain weight
    rho_star: float = 0.5    # coherence target density
    increment: float = 1.0   # commitment increment per step
    # Extinction: when not None, a front stops once its maximal Sigma <= this
    # threshold (Phase D: "no positive-Sigma continuation"). When None, fronts
    # propagate as long as admissible candidates exist (used by bounded-step demos).
    extinction_threshold: float | None = None


def coherence(u: int, v: int, state: StateVector, coeffs: SigmaCoeffs) -> float:
    """Local consistency functional on the commitment field. ORIENTATION-FREE.

    Reference default: negative squared distance of rho(v) from the target
    rho_star, so maximizing Sigma favors candidates whose density is consistent
    with the chain's target. Reads rho only.
    """
    return -(state.rho_at(v) - coeffs.rho_star) ** 2


def compute_sigma(u: int, v: int, state: StateVector, graph: ParticipationGraph,
                  coeffs: SigmaCoeffs = SigmaCoeffs()) -> float:
    """Sigma for the transition u -> v:  Σ = kc*Coh - ks*Str - kg*Grad.

    Reads rho (B4) and graph-local structure ONLY; never orientation (B5).
    """
    rho_u = state.rho_at(u)
    rho_v = state.rho_at(v)
    coh = coherence(u, v, state, coeffs)   # stabilizing channel  (+)
    strain = rho_v                          # destabilizing: penalize dense targets (-)
    grad = abs(rho_v - rho_u)               # destabilizing: penalize fighting gradient (-)
    return coeffs.kc * coh - coeffs.ks * strain - coeffs.kg * grad


def compute_candidates(u: int, state: StateVector,
                       graph: ParticipationGraph) -> list[int]:
    """Admissible next-states from u: non-decoupled neighbors (reach-bounded)."""
    return graph.admissible_neighbors(u)
