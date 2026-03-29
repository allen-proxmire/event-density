"""
edsim.phys.cosmology_regime — Cosmological analogue regime for ED.

This module defines parameter regimes that produce STRUCTURAL ANALOGUES
of cosmological phenomena.  These are NOT claims of cosmological physics.

Three analogues:

1. **Expansion:** Starting from an overdense state (rho > rho_star), the
   penalty drives global density decay — analogous to matter dilution in
   an expanding universe.  An effective scale factor a(t) is defined as
   a(t) = (rho_star / <rho>(t))^(1/d).

2. **Horizons:** Regions where rho -> rho_max have M(rho) -> 0 and
   become dynamically isolated — analogous to causal horizons where
   communication ceases.

3. **Structure:** Multi-modal initial conditions produce transient
   filaments and sheets — analogous to the cosmic web.  The analogy is
   INVERTED: cosmological structure grows; ED structure decays.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from ..core.parameters import EDParameters


@dataclass(frozen=True)
class CosmologyRegime:
    """Specification of a cosmological-analogue ED regime.

    Attributes
    ----------
    name : str
    parameters : EDParameters
    description : str
    expected_analogues : str
    expansion_rate : float
        Predicted global density decay rate D * P0.
    horizon_threshold : float
        Density above which M < 1% of M_star.
    structure_lifetime : float
        Estimated filament lifetime 1/sigma_k1.
    ic_amplitude : float
    ic_modes : int
    """

    name: str
    parameters: EDParameters
    description: str
    expected_analogues: str
    expansion_rate: float
    horizon_threshold: float
    structure_lifetime: float
    ic_amplitude: float
    ic_modes: int


def build_cosmology_regime(
    d: int = 2,
    N: int = 64,
    A: float = 0.35,
    Nm: int = 3,
    P0: float = 0.3,
    H: float = 0.5,
    T: float = 8.0,
    dt: float = 5e-4,
) -> CosmologyRegime:
    """Build a cosmological-analogue regime.

    Uses:
    - Large amplitude A to push rho near rho_max (horizons)
    - Multiple modes Nm for structure
    - Moderate P0 for expansion-like decay
    - Nonzero H for telegraph epochs

    Parameters
    ----------
    d, N, A, Nm, P0, H, T, dt : various

    Returns
    -------
    CosmologyRegime
    """
    D = 0.3
    M0, beta = 1.0, 2.0
    rho_star, rho_max = 0.5, 1.0

    L_tuple = tuple(1.0 for _ in range(d))
    N_tuple = tuple(N for _ in range(d))

    params = EDParameters(
        d=d, L=L_tuple, N=N_tuple,
        D=D, H=H, zeta=0.1, tau=1.0,
        rho_star=rho_star, rho_max=rho_max,
        M0=M0, beta=beta, P0=P0,
        dt=dt, T=T, method="implicit_euler", bc="neumann",
        k_out=max(1, int(T / dt) // 60),
        seed=42,
    )

    M_star = M0 * (rho_max - rho_star) ** beta
    exp_rate = D * P0

    # Horizon threshold: M(rho) < 0.01 * M_star
    M_crit = 0.01 * M_star
    rho_h = rho_max - (M_crit / M0) ** (1.0 / beta)

    mu_1 = (math.pi / params.L[0]) ** 2
    sigma_k1 = D * (M_star * mu_1 + P0)
    struct_life = 1.0 / sigma_k1

    description = (
        f"Cosmology-analogue regime in {d}D: A={A}, Nm={Nm}, P0={P0}, H={H}.  "
        f"Expansion rate={exp_rate:.4f}, horizon threshold rho>{rho_h:.4f}, "
        f"structure lifetime={struct_life:.3f}."
    )

    expected = (
        "1. Global density decays exponentially (expansion analogue).  "
        "2. High-density regions have M->0 (horizon analogue).  "
        "3. Multi-modal IC produces transient filaments (structure analogue)."
    )

    return CosmologyRegime(
        name=f"cosmology_{d}d",
        parameters=params,
        description=description,
        expected_analogues=expected,
        expansion_rate=exp_rate,
        horizon_threshold=rho_h,
        structure_lifetime=struct_life,
        ic_amplitude=A,
        ic_modes=Nm,
    )
