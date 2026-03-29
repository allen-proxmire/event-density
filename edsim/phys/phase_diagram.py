"""
edsim.phys.phase_diagram — Global phase diagram for the ED PDE.

The ED PDE has three primary control parameters that determine its
qualitative behaviour:

    M0  — mobility prefactor (diffusion strength)
    P0  — penalty slope (reaction strength)
    H   — participation coupling (telegraph strength)

These span a 3D parameter space partitioned into five phases:

    DIFFUSION       M_star * pi^2 >> P0 and H small
    REACTION        P0 >> M_star * pi^2 and H small
    TELEGRAPH       H large enough for underdamped oscillation (Q > 1)
    TRANSIENT       moderate M0, P0; rich morphological structure
    QUANTUM-LIKE    high M0, low P0, high H; nonlinear + oscillatory
"""

from __future__ import annotations

import math
import itertools
from dataclasses import dataclass, field
from typing import Optional

import numpy as np

from ..core.parameters import EDParameters


# ---------------------------------------------------------------
# Phase grid point
# ---------------------------------------------------------------

@dataclass
class PhaseMetrics:
    """Diagnostic metrics for a single (M0, P0, H) point.

    Attributes
    ----------
    D_eff : float
        D * M_star.
    lambda_eff : float
        D * P0.
    diffusion_reaction_ratio : float
        D_eff * pi^2 / lambda_eff.
    gamma : float
        Telegraph damping rate.
    omega_osc : float
        Telegraph oscillation frequency (0 if overdamped).
    Q : float
        Quality factor.
    sigma_k1 : float
        Decay rate of k=1 mode.
    complexity_lifetime : float
        1 / sigma_k1.
    mobility_variation : float
        Fractional mobility reduction at A=0.05.
    """

    D_eff: float
    lambda_eff: float
    diffusion_reaction_ratio: float
    gamma: float
    omega_osc: float
    Q: float
    sigma_k1: float
    complexity_lifetime: float
    mobility_variation: float


@dataclass
class PhasePoint:
    """A single point in the phase diagram.

    Attributes
    ----------
    M0 : float
    P0 : float
    H : float
    metrics : PhaseMetrics
    classification : str
        One of: "diffusion", "reaction", "telegraph",
        "transient", "quantum_like".
    """

    M0: float
    P0: float
    H: float
    metrics: PhaseMetrics
    classification: str


@dataclass
class PhaseDiagram:
    """Complete phase diagram over a grid.

    Attributes
    ----------
    points : list[PhasePoint]
    M0_values : list[float]
    P0_values : list[float]
    H_values : list[float]
    phase_counts : dict[str, int]
    """

    points: list
    M0_values: list
    P0_values: list
    H_values: list
    phase_counts: dict


# ---------------------------------------------------------------
# Grid construction
# ---------------------------------------------------------------

def build_phase_grid(
    M0_values: Optional[list] = None,
    P0_values: Optional[list] = None,
    H_values: Optional[list] = None,
) -> list[tuple[float, float, float]]:
    """Return a list of (M0, P0, H) grid points.

    Default grid: 4 x 4 x 4 = 64 points spanning the interesting region.

    Parameters
    ----------
    M0_values, P0_values, H_values : list[float], optional

    Returns
    -------
    list[tuple[float, float, float]]
    """
    if M0_values is None:
        M0_values = [0.5, 1.0, 2.0, 4.0]
    if P0_values is None:
        P0_values = [0.05, 0.2, 1.0, 3.0]
    if H_values is None:
        H_values = [0.0, 0.5, 2.0, 5.0]

    return list(itertools.product(M0_values, P0_values, H_values))


# ---------------------------------------------------------------
# Metric computation (analytical — no simulation needed)
# ---------------------------------------------------------------

def compute_phase_metrics(
    M0: float,
    P0: float,
    H: float,
    D: float = 0.3,
    beta: float = 2.0,
    rho_star: float = 0.5,
    rho_max: float = 1.0,
    zeta: float = 0.1,
    tau: float = 1.0,
    A_test: float = 0.05,
) -> PhaseMetrics:
    """Compute all diagnostic metrics analytically.

    Parameters
    ----------
    M0, P0, H : float
        Control parameters.
    D, beta, rho_star, rho_max, zeta, tau : float
        Fixed constitutive parameters.
    A_test : float
        Amplitude for mobility variation estimate.

    Returns
    -------
    PhaseMetrics
    """
    M_star = M0 * (rho_max - rho_star) ** beta
    D_eff = D * M_star
    lam_eff = D * P0

    # Diffusion / reaction ratio at k=1
    mu_1 = (math.pi) ** 2  # on [0, 1]
    dr_ratio = D_eff * mu_1 / (lam_eff + 1e-30)

    # Telegraph
    gamma = (D * P0 + zeta / tau) / 2.0
    omega0_sq = (D * P0 * zeta + H * P0) / tau
    disc = gamma ** 2 - omega0_sq
    omega_osc = math.sqrt(max(0.0, -disc))
    Q = omega_osc / (2.0 * gamma) if gamma > 0 and omega_osc > 0 else 0.0

    # Modal decay
    sigma_k1 = D * (M_star * mu_1 + P0)
    c_life = 1.0 / sigma_k1 if sigma_k1 > 0 else float("inf")

    # Mobility variation
    M_peak = M0 * max(0.0, rho_max - (rho_star + A_test)) ** beta
    mob_var = 1.0 - M_peak / (M_star + 1e-30)

    return PhaseMetrics(
        D_eff=D_eff,
        lambda_eff=lam_eff,
        diffusion_reaction_ratio=dr_ratio,
        gamma=gamma,
        omega_osc=omega_osc,
        Q=Q,
        sigma_k1=sigma_k1,
        complexity_lifetime=c_life,
        mobility_variation=mob_var,
    )


# ---------------------------------------------------------------
# Classification
# ---------------------------------------------------------------

def classify_phase(M0: float, P0: float, H: float, m: PhaseMetrics) -> str:
    """Classify a phase point.

    Rules (applied in priority order):

    1. quantum_like: M0 >= 2.0 AND P0 <= 0.1 AND H >= 1.0
    2. telegraph: Q >= 1.0 (underdamped with good oscillation)
    3. reaction: diffusion_reaction_ratio < 1.0 (penalty dominates k=1 diffusion)
    4. diffusion: diffusion_reaction_ratio >= 5.0 (diffusion dominates)
    5. transient: everything else (moderate competition)

    Parameters
    ----------
    M0, P0, H : float
    m : PhaseMetrics

    Returns
    -------
    str
    """
    if M0 >= 2.0 and P0 <= 0.1 and H >= 1.0:
        return "quantum_like"
    if m.Q >= 1.0:
        return "telegraph"
    if m.diffusion_reaction_ratio < 1.0:
        return "reaction"
    if m.diffusion_reaction_ratio >= 5.0:
        return "diffusion"
    return "transient"


# ---------------------------------------------------------------
# Full diagram builder
# ---------------------------------------------------------------

def build_phase_diagram(
    M0_values: Optional[list] = None,
    P0_values: Optional[list] = None,
    H_values: Optional[list] = None,
) -> PhaseDiagram:
    """Build the complete phase diagram.

    This is purely analytical: no simulations are run.  All metrics
    are computed from the closed-form linearised expressions.

    Parameters
    ----------
    M0_values, P0_values, H_values : list[float], optional

    Returns
    -------
    PhaseDiagram
    """
    if M0_values is None:
        M0_values = [0.5, 1.0, 2.0, 4.0]
    if P0_values is None:
        P0_values = [0.05, 0.2, 1.0, 3.0]
    if H_values is None:
        H_values = [0.0, 0.5, 2.0, 5.0]

    grid = build_phase_grid(M0_values, P0_values, H_values)

    points = []
    for M0, P0, H in grid:
        m = compute_phase_metrics(M0, P0, H)
        phase = classify_phase(M0, P0, H, m)
        points.append(PhasePoint(M0=M0, P0=P0, H=H, metrics=m, classification=phase))

    counts = {}
    for p in points:
        counts[p.classification] = counts.get(p.classification, 0) + 1

    return PhaseDiagram(
        points=points,
        M0_values=M0_values,
        P0_values=P0_values,
        H_values=H_values,
        phase_counts=counts,
    )
