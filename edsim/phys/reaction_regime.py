"""
edsim.phys.reaction_regime — Reaction/source-like ED parameter regime.

In the reaction limit the ED PDE is dominated by the penalty term.
For a spatially uniform field (Laplacian = 0, |grad|^2 = 0):

    d rho / dt = -D P0 (rho - rho_star) + H v

With H = 0 (no participation), this reduces to

    d delta / dt = -lambda_eff * delta,   lambda_eff = D * P0

which is a simple exponential decay toward rho_star.

With H > 0, the coupled (delta, v) system produces overdamped or
underdamped relaxation (see ED-PHYS-02 for the telegraph regime).

For spatially varying fields, the ED operator combines:
    - diffusion: D * M_star * mu_k  (k^2 scaling, always stabilising)
    - reaction:  D * P0             (constant, always stabilising)

The crossover wavenumber k_c = sqrt(P0 / M_star) / pi separates
reaction-dominated (k < k_c) from diffusion-dominated (k > k_c) modes.

The reaction regime is defined by:
    - strong P0 relative to M_star mu_1  (penalty dominates diffusion)
    - H = 0 or small  (clean exponential decay)
    - spatially uniform or slowly varying initial conditions
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from ..core.parameters import EDParameters


@dataclass(frozen=True)
class ReactionRegime:
    """Specification of an ED regime that approximates a reaction equation.

    Attributes
    ----------
    name : str
    parameters : EDParameters
    description : str
    expected_behavior : str
    lambda_eff : float
        Predicted effective reaction rate D * P0.
    e_folding_time : float
        1 / lambda_eff.
    crossover_k : float
        Wavenumber above which diffusion dominates reaction.
    """

    name: str
    parameters: EDParameters
    description: str
    expected_behavior: str
    lambda_eff: float
    e_folding_time: float
    crossover_k: float


def build_reaction_regime(
    d: int = 2,
    N_per_axis: int = 64,
    P0: float = 2.0,
    H: float = 0.0,
    T: float = 8.0,
    dt: float = 1e-3,
) -> ReactionRegime:
    """Construct a reaction-dominated ED regime.

    Uses strong penalty P0 and zero (or weak) participation coupling
    so that the penalty term dominates the dynamics for low-k modes.

    Parameters
    ----------
    d : int
        Spatial dimension (default 2).
    N_per_axis : int
        Grid points per axis (default 64).
    P0 : float
        Penalty slope (default 2.0 — stronger than canonical 1.0).
    H : float
        Participation coupling (default 0.0 — pure reaction).
    T : float
        Final time (default 8.0 — several e-folding times).
    dt : float
        Time step (default 1e-3).

    Returns
    -------
    ReactionRegime
    """
    D = 0.3
    L_tuple = tuple(1.0 for _ in range(d))
    N_tuple = tuple(N_per_axis for _ in range(d))

    params = EDParameters(
        d=d,
        L=L_tuple,
        N=N_tuple,
        D=D,
        H=H,
        zeta=0.1,
        tau=1.0,
        rho_star=0.5,
        rho_max=1.0,
        M0=1.0,
        beta=2.0,
        P0=P0,
        dt=dt,
        T=T,
        method="implicit_euler",
        bc="neumann",
        k_out=max(1, int(T / dt) // 40),
        seed=42,
    )

    M_star = params.M_star
    lam_eff = D * P0
    e_fold = 1.0 / lam_eff
    k_c = math.sqrt(P0 / M_star) / math.pi if M_star > 0 else float("inf")

    description = (
        f"Reaction regime in {d}D: P0={P0}, H={H}, D={D}, "
        f"M_star={M_star:.4f}.  "
        f"lambda_eff = D*P0 = {lam_eff:.4f}, "
        f"e-folding time = {e_fold:.2f}.  "
        f"Crossover k_c = {k_c:.2f}."
    )

    expected = (
        f"Spatially uniform perturbations decay exponentially "
        f"at rate lambda_eff = {lam_eff:.4f}.  "
        f"Modes with k < {k_c:.1f} are reaction-dominated; "
        f"modes with k > {k_c:.1f} are diffusion-dominated."
    )

    return ReactionRegime(
        name=f"reaction_{d}d",
        parameters=params,
        description=description,
        expected_behavior=expected,
        lambda_eff=lam_eff,
        e_folding_time=e_fold,
        crossover_k=k_c,
    )
