"""
edsim.phys.pattern_regime — Pattern-formation analysis for ED.

The canonical ED PDE is UNCONDITIONALLY STABLE: the uniform equilibrium
rho = rho_star is linearly stable to perturbations of ALL wavenumbers.

    sigma_k = -D (M_star mu_k + P0) < 0   for all k.

This means ED does NOT support:
    - Turing patterns
    - spinodal decomposition
    - stripe/spot instabilities
    - symmetry-breaking bifurcations

However, ED DOES produce rich TRANSIENT morphological structure:
    - Filaments, sheets, blobs (from multi-modal initial conditions)
    - Differential decay rates create transient complexity
    - Nonlinear mobility sharpens gradients transiently
    - The morphological taxonomy (ED-Phys-35) is entirely transient

This module defines the "pattern regime" as the parameter set that
MAXIMISES transient complexity before the system decays to equilibrium.
The experiments measure:
    - Transient amplification ratio (max complexity / initial complexity)
    - Morphological lifetime (time before structure is lost)
    - Nonlinear sharpening (gradient concentration by M'|grad rho|^2)
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from ..core.parameters import EDParameters


@dataclass(frozen=True)
class PatternRegime:
    """Specification of an ED regime for transient pattern analysis.

    Attributes
    ----------
    name : str
    parameters : EDParameters
    description : str
    expected_behavior : str
    sigma_k1 : float
        Linear decay rate of k=1 mode.
    decay_ratio_k1_k4 : float
        sigma_k4 / sigma_k1: how much faster high modes decay.
    morphological_lifetime_est : float
        Estimated time before structure is lost (1/sigma_k1).
    """

    name: str
    parameters: EDParameters
    description: str
    expected_behavior: str
    sigma_k1: float
    decay_ratio_k1_k4: float
    morphological_lifetime_est: float


def build_pattern_regime(
    d: int = 2,
    N_per_axis: int = 64,
    A: float = 0.1,
    Nm: int = 4,
    P0: float = 0.5,
    D: float = 0.3,
    T: float = 2.0,
    dt: float = 5e-4,
) -> PatternRegime:
    """Construct a regime that maximises transient morphological complexity.

    Strategy:
        - Weak penalty P0 (slow reaction, long-lived structure)
        - Moderate amplitude A (strong nonlinear terms)
        - Many modes Nm (rich initial structure)
        - Standard diffusion D

    Parameters
    ----------
    d : int
    N_per_axis : int
    A : float
        Initial perturbation amplitude (default 0.1 — larger than canonical 0.03).
    Nm : int
        Modes per axis (default 4 — richer than canonical 2).
    P0 : float
        Penalty slope (default 0.5 — weaker than canonical 1.0).
    D : float
        Diffusion weight (default 0.3).
    T : float
        Final time (default 2.0).
    dt : float
        Time step (default 5e-4).

    Returns
    -------
    PatternRegime
    """
    L_tuple = tuple(1.0 for _ in range(d))
    N_tuple = tuple(N_per_axis for _ in range(d))

    params = EDParameters(
        d=d,
        L=L_tuple,
        N=N_tuple,
        D=D,
        H=0.0,
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
        k_out=max(1, int(T / dt) // 50),
        seed=42,
    )

    M_star = params.M_star
    mu_1 = (math.pi / params.L[0]) ** 2
    mu_4 = (4 * math.pi / params.L[0]) ** 2
    sigma_k1 = D * (M_star * mu_1 + P0)
    sigma_k4 = D * (M_star * mu_4 + P0)

    description = (
        f"Pattern regime in {d}D: A={A}, Nm={Nm}, P0={P0}, D={D}.  "
        f"sigma_k1 = {sigma_k1:.4f}, morphological lifetime ~ {1/sigma_k1:.2f}.  "
        f"Decay ratio k4/k1 = {sigma_k4/sigma_k1:.2f} (differential decay "
        f"creates transient structure)."
    )

    expected = (
        f"ED does NOT form stable patterns (all sigma_k < 0).  "
        f"However, the multi-modal IC with {Nm}^{d} = {Nm**d} modes "
        f"produces rich transient morphology: filaments, sheets, blobs.  "
        f"The structure has lifetime ~ {1/sigma_k1:.2f} before decaying "
        f"to the uniform equilibrium."
    )

    return PatternRegime(
        name=f"pattern_{d}d",
        parameters=params,
        description=description,
        expected_behavior=expected,
        sigma_k1=sigma_k1,
        decay_ratio_k1_k4=sigma_k4 / sigma_k1,
        morphological_lifetime_est=1.0 / sigma_k1,
    )
