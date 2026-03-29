"""
edsim.phys.diffusion_regime — Diffusion-like ED parameter regime.

In the diffusion limit the canonical ED PDE simplifies toward the linear
heat equation.  The simplification requires:

    1. Small penalty (P0 << D * M_star * pi^2 / L^2) so that the reaction
       term is negligible compared to diffusion.
    2. Density perturbations well below rho_max so that the mobility is
       approximately constant: M(rho) ~ M_star.
    3. Participation coupling weak or absent (H ~ 0) so that the global
       mode does not inject energy.

Under these conditions the ED operator reduces to

    F[rho] ~ M_star * Laplacian(rho)

and the PDE becomes

    d rho / dt ~ D * M_star * Laplacian(rho) = D_eff * Laplacian(rho)

with effective diffusion coefficient D_eff = D * M_star.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..core.parameters import EDParameters


@dataclass(frozen=True)
class DiffusionRegime:
    """Specification of an ED regime that approximates diffusion.

    Attributes
    ----------
    name : str
        Human-readable regime label.
    parameters : EDParameters
        ED parameters tuned for the diffusion limit.
    description : str
        Narrative description of why this regime is diffusion-like.
    expected_D_eff : float
        Predicted effective diffusion coefficient D * M_star.
    expected_behavior : str
        Summary of expected dynamical behaviour.
    """

    name: str
    parameters: EDParameters
    description: str
    expected_D_eff: float
    expected_behavior: str


def build_diffusion_regime(
    d: int = 2,
    N_per_axis: int = 64,
    T: float = 0.5,
    dt: float = 5e-5,
) -> DiffusionRegime:
    """Construct a diffusion-like ED regime.

    The regime uses:
        - very small penalty slope  P0 = 0.01  (almost no reaction)
        - zero participation         H = 0      (no global feedback)
        - moderate diffusion         D = 0.3
        - equilibrium far from       rho_star = 0.5, rho_max = 1.0
          capacity bound             so M(rho_star) = M0 * 0.5^beta

    Parameters
    ----------
    d : int
        Spatial dimension (default 2).
    N_per_axis : int
        Grid points per axis (default 64).
    T : float
        Final time (default 0.5).
    dt : float
        Time step (default 5e-5).

    Returns
    -------
    DiffusionRegime
        Complete regime specification.
    """
    L_tuple = tuple(1.0 for _ in range(d))
    N_tuple = tuple(N_per_axis for _ in range(d))

    params = EDParameters(
        d=d,
        L=L_tuple,
        N=N_tuple,
        D=0.3,
        H=0.0,           # no participation coupling
        zeta=0.1,
        tau=1.0,
        rho_star=0.5,
        rho_max=1.0,
        M0=1.0,
        beta=2.0,
        P0=0.01,         # very weak penalty
        dt=dt,
        T=T,
        method="implicit_euler",
        bc="neumann",
        k_out=max(1, int(T / dt) // 20),  # ~20 snapshots
        seed=42,
    )

    M_star = params.M_star  # M0 * (rho_max - rho_star)^beta = 1.0 * 0.5^2 = 0.25
    D_eff = params.D * M_star  # 0.3 * 0.25 = 0.075

    description = (
        f"Diffusion regime in {d}D: P0={params.P0} (weak penalty), "
        f"H={params.H} (no participation), D={params.D}, "
        f"M_star={M_star:.4f}, D_eff={D_eff:.4f}.  "
        f"The ED PDE approximates the heat equation "
        f"d rho/dt = {D_eff:.4f} * Laplacian(rho)."
    )

    expected = (
        "A localised bump spreads diffusively with variance growing as "
        f"<x^2>(t) ~ 2*d*D_eff*t = {2*d*D_eff:.4f}*t.  "
        "A step-function profile relaxes toward the complementary error "
        "function profile of the linear heat equation."
    )

    return DiffusionRegime(
        name=f"diffusion_{d}d",
        parameters=params,
        description=description,
        expected_D_eff=D_eff,
        expected_behavior=expected,
    )
