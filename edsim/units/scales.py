"""
edsim.units.scales -- Characteristic scales for nondimensionalization.

The canonical ED PDE is solved in nondimensional form.  This module
defines the mapping between nondimensional variables and physical
quantities through a set of *characteristic scales*:

    L0  -- length [m]
    T0  -- time   [s]
    R0  -- density [kg m^-3]  (or probability density, curvature, ...)
    V0  -- velocity [m s^-1]  (derived: L0 / T0)
    E0  -- energy [J]         (derived: R0 * L0^d)

All solver variables are related to physical variables by:

    x_phys = x_nd * L0
    t_phys = t_nd * T0
    rho_phys = rho_nd * R0
    v_phys = v_nd * V0

The nondimensional PDE parameters (D, P0, M0, H, ...) are obtained
from the physical parameters by absorbing the scales.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional

from ..core.parameters import EDParameters
from . import constants as C


@dataclass(frozen=True)
class Scales:
    """Characteristic scales linking nondimensional ED to physical units.

    Attributes
    ----------
    L0 : float
        Characteristic length [m].
    T0 : float
        Characteristic time [s].
    R0 : float
        Characteristic density [kg m^-3] (or other appropriate density unit).
    V0 : float
        Characteristic velocity [m s^-1] (derived: L0 / T0).
    E0 : float
        Characteristic energy density [J m^-d] (derived: R0 * V0^2 or
        from the Lyapunov functional).
    d : int
        Spatial dimension.
    regime : str
        Label describing the physical regime.
    """

    L0: float
    T0: float
    R0: float
    V0: float
    E0: float
    d: int = 2
    regime: str = "generic"

    def __post_init__(self) -> None:
        if self.L0 <= 0 or self.T0 <= 0 or self.R0 <= 0:
            raise ValueError("All characteristic scales must be positive.")

    @property
    def K0(self) -> float:
        """Characteristic curvature [m^-2]."""
        return 1.0 / (self.L0 ** 2)

    @property
    def D0(self) -> float:
        """Characteristic diffusivity [m^2 s^-1]."""
        return self.L0 ** 2 / self.T0


def compute_scales(
    params: EDParameters,
    L0: float = 1.0,
    R0: float = 1.0,
    regime: str = "generic",
    D_phys: Optional[float] = None,
) -> Scales:
    """Compute characteristic scales from ED parameters and one physical anchor.

    The nondimensionalization is defined by:

        rho = rho_phys / R0
        x   = x_phys   / L0
        t   = t_phys   / T0

    The diffusion coefficient D in nondimensional form satisfies:

        D_nd = D_phys * T0 / L0^2

    Given (L0, R0) and either D_phys or params.D, the time scale T0
    is determined.

    Parameters
    ----------
    params : EDParameters
        Nondimensional simulation parameters.
    L0 : float
        Physical domain length [m].
    R0 : float
        Physical density scale [kg m^-3].
    regime : str
        Label for the physical regime.
    D_phys : float, optional
        Physical diffusivity [m^2 s^-1].  If provided, T0 = D_phys / (params.D * L0^2).
        If None, T0 = L0^2 / params.D (unit diffusivity assumption).

    Returns
    -------
    Scales
        Complete set of characteristic scales.
    """
    if D_phys is not None and D_phys > 0:
        T0 = L0 ** 2 / D_phys * params.D
    else:
        # Default: T0 such that D_nd * L0^2 / T0 = D_nd (T0 = L0^2)
        T0 = L0 ** 2 / params.D

    V0 = L0 / T0
    E0 = R0 * L0 ** params.d  # total-mass scale, energy ~ integral(rho dV)

    return Scales(
        L0=L0, T0=T0, R0=R0, V0=V0, E0=E0,
        d=params.d, regime=regime,
    )


# ── Pre-built scale factories ────────────────────────────────────────


def planck_scales(params: EDParameters) -> Scales:
    """Planck-scale ED: length ~ l_Pl, density ~ rho_Pl.

    Appropriate for quantum-gravity analogues.
    """
    return compute_scales(
        params,
        L0=C.l_Pl,
        R0=C.rho_Pl,
        regime="planck",
    )


def quantum_scales(params: EDParameters, mass: float = C.m_e) -> Scales:
    """Quantum-scale ED: length ~ Bohr radius, density ~ |psi|^2.

    Appropriate for Schrodinger-like or probability-density analogues.

    Parameters
    ----------
    mass : float
        Particle mass [kg] setting the Compton/Bohr scale.
    """
    L0 = C.hbar / (mass * C.c)  # reduced Compton wavelength
    R0 = 1.0 / L0 ** params.d   # probability density normalised to 1
    return compute_scales(
        params,
        L0=L0,
        R0=R0,
        regime="quantum",
    )


def condensed_matter_scales(
    params: EDParameters,
    L0: float = 1e-6,
    R0: float = 1e3,
) -> Scales:
    """Condensed-matter scale ED: micron lengths, moderate densities.

    Parameters
    ----------
    L0 : float
        Characteristic length [m], default 1 micron.
    R0 : float
        Characteristic density [kg m^-3], default 1000 (water).
    """
    return compute_scales(
        params,
        L0=L0,
        R0=R0,
        regime="condensed_matter",
    )


def galactic_scales(params: EDParameters) -> Scales:
    """Galactic-scale ED: kpc lengths, critical-density normalisation.

    Appropriate for cosmological-density or dark-matter analogues.
    """
    return compute_scales(
        params,
        L0=C.kpc,
        R0=C.rho_crit,
        regime="galactic",
    )


def cosmological_scales(params: EDParameters) -> Scales:
    """Cosmological-scale ED: Hubble length, critical density.

    Appropriate for large-scale structure analogues.
    """
    L0 = C.c / C.H_0  # Hubble length ~ 4.4 Gpc
    return compute_scales(
        params,
        L0=L0,
        R0=C.rho_crit,
        regime="cosmological",
    )


def custom_scales(
    params: EDParameters,
    L0: float = 1.0,
    T0: Optional[float] = None,
    R0: float = 1.0,
    regime: str = "custom",
) -> Scales:
    """Build scales from explicit (L0, T0, R0).

    If T0 is omitted, it is derived from params.D and L0.
    """
    if T0 is not None:
        V0 = L0 / T0
        E0 = R0 * L0 ** params.d
        return Scales(L0=L0, T0=T0, R0=R0, V0=V0, E0=E0,
                       d=params.d, regime=regime)
    return compute_scales(params, L0=L0, R0=R0, regime=regime)
