"""
edsim.units.mapping -- Conversion between ED nondimensional and physical units.

Provides:
    - Point-wise conversion functions (rho, v, x, t, energy, etc.)
    - Full-field conversion for arrays and time series
    - The ED -> physics dictionary describing parameter correspondences
"""

from __future__ import annotations

from typing import Any

import numpy as np

from ..core.parameters import EDParameters
from .scales import Scales
from . import constants as C


# ══════════════════════════════════════════════════════════════════════
#  Scalar / array converters: nondimensional <-> physical
# ══════════════════════════════════════════════════════════════════════

def ed_to_physical_rho(rho_nd: np.ndarray | float, scales: Scales) -> np.ndarray | float:
    """Convert nondimensional density to physical density.

    rho_phys = rho_nd * R0
    """
    return rho_nd * scales.R0


def physical_to_ed_rho(rho_phys: np.ndarray | float, scales: Scales) -> np.ndarray | float:
    """Convert physical density to nondimensional density.

    rho_nd = rho_phys / R0
    """
    return rho_phys / scales.R0


def ed_to_physical_time(t_nd: float | np.ndarray, scales: Scales) -> float | np.ndarray:
    """t_phys = t_nd * T0"""
    return t_nd * scales.T0


def physical_to_ed_time(t_phys: float | np.ndarray, scales: Scales) -> float | np.ndarray:
    """t_nd = t_phys / T0"""
    return t_phys / scales.T0


def ed_to_physical_length(x_nd: float | np.ndarray, scales: Scales) -> float | np.ndarray:
    """x_phys = x_nd * L0"""
    return x_nd * scales.L0


def physical_to_ed_length(x_phys: float | np.ndarray, scales: Scales) -> float | np.ndarray:
    """x_nd = x_phys / L0"""
    return x_phys / scales.L0


def ed_to_physical_velocity(v_nd: float | np.ndarray, scales: Scales) -> float | np.ndarray:
    """v_phys = v_nd * V0 = v_nd * L0 / T0"""
    return v_nd * scales.V0


def physical_to_ed_velocity(v_phys: float | np.ndarray, scales: Scales) -> float | np.ndarray:
    """v_nd = v_phys / V0"""
    return v_phys / scales.V0


def ed_to_physical_energy(E_nd: float, scales: Scales) -> float:
    """Convert nondimensional Lyapunov energy to physical energy.

    The Lyapunov functional E[rho] = int Phi(rho) dV has dimensions
    of [R0] * [L0]^d * [Phi/R0] where Phi ~ P/M * rho has the same
    dimension as the density potential.

    We use E_phys = E_nd * E0 where E0 = R0 * L0^d.
    """
    return E_nd * scales.E0


def ed_to_physical_complexity(C_nd: float, scales: Scales) -> float:
    """Convert nondimensional complexity int|grad rho|^2 dV to physical.

    C_phys = C_nd * R0^2 * L0^(d-2)
    """
    return C_nd * scales.R0 ** 2 * scales.L0 ** (scales.d - 2)


def ed_to_physical_mass(M_nd: float, scales: Scales) -> float:
    """Convert nondimensional mass int rho dV to physical.

    M_phys = M_nd * R0 * L0^d
    """
    return M_nd * scales.E0  # E0 = R0 * L0^d


def ed_to_physical_correlation_length(xi_nd: float, scales: Scales) -> float:
    """xi_phys = xi_nd * L0"""
    return xi_nd * scales.L0


# ══════════════════════════════════════════════════════════════════════
#  ED parameter <-> physical constant dictionary
# ══════════════════════════════════════════════════════════════════════

def parameter_dictionary(params: EDParameters, scales: Scales) -> dict[str, dict[str, Any]]:
    """Build the ED -> physics dictionary for a given parameter set and scale.

    Returns a dict keyed by ED parameter name.  Each entry contains:
        - "ed_value": nondimensional value
        - "physical_value": value in SI
        - "physical_unit": SI unit string
        - "physical_name": descriptive physical name
        - "analogue_candidates": list of possible physical interpretations
        - "notes": contextual information

    This is the *first edition* of the dictionary (ED-Phys-36 Section II.4).
    It is a mapping, not a commitment to a single ontology.
    """
    D0 = scales.D0  # L0^2 / T0

    return {
        "rho": {
            "ed_value": f"field in [0, {params.rho_max}]",
            "physical_value": f"field in [0, {params.rho_max * scales.R0:.4e}]",
            "physical_unit": "kg m^-3" if scales.regime != "quantum" else "m^-d",
            "physical_name": "density",
            "analogue_candidates": [
                "mass density (fluid/cosmological)",
                "probability density (quantum)",
                "curvature potential (geometric)",
                "concentration (reaction-diffusion)",
            ],
            "notes": "The primary dynamical field of the ED PDE.",
        },
        "v": {
            "ed_value": "scalar, nondimensional",
            "physical_value": f"scalar * {scales.V0:.4e}",
            "physical_unit": "m s^-1",
            "physical_name": "participation velocity",
            "analogue_candidates": [
                "bulk velocity (fluid)",
                "global mode amplitude (field theory)",
                "mean-field order parameter (statistical mechanics)",
            ],
            "notes": "Global coupling variable driven by domain-averaged F.",
        },
        "D": {
            "ed_value": params.D,
            "physical_value": params.D * D0,
            "physical_unit": "m^2 s^-1",
            "physical_name": "diffusivity",
            "analogue_candidates": [
                "thermal diffusivity (heat equation)",
                "kinematic viscosity (Navier-Stokes)",
                "quantum diffusivity hbar/2m (Schrodinger)",
            ],
            "notes": "Controls rate of gradient-driven smoothing.",
        },
        "M(rho)": {
            "ed_value": f"M0 * (rho_max - rho)^beta = {params.M0} * (... )^{params.beta}",
            "physical_value": f"{params.M0 * D0:.4e} * (...)^{params.beta}",
            "physical_unit": "m^2 s^-1",
            "physical_name": "mobility / conductivity",
            "analogue_candidates": [
                "porous-medium mobility u^m (PME)",
                "thin-film mobility h^n (TFE)",
                "degenerate diffusion coefficient",
                "electrical conductivity sigma(rho)",
            ],
            "notes": (
                "Degenerate: M -> 0 at rho_max, creating horizons.  "
                f"Equilibrium value M* = {params.M_star:.4f} (nd), "
                f"{params.M_star * D0:.4e} (phys)."
            ),
        },
        "P(rho)": {
            "ed_value": f"P0 * (rho - rho*) = {params.P0} * (rho - {params.rho_star})",
            "physical_value": f"{params.P0 / scales.T0:.4e} * (rho_phys - rho*_phys)",
            "physical_unit": "kg m^-3 s^-1",
            "physical_name": "penalty / restoring force",
            "analogue_candidates": [
                "pressure (fluid)",
                "entropic penalty (free energy)",
                "drift potential gradient (Fokker-Planck)",
                "chemical potential difference (Cahn-Hilliard)",
            ],
            "notes": "Drives rho toward rho_star.  Single equilibrium (monostable).",
        },
        "H": {
            "ed_value": params.H,
            "physical_value": params.H * scales.V0,
            "physical_unit": "m s^-1",
            "physical_name": "participation coupling strength",
            "analogue_candidates": [
                "forcing amplitude (driven systems)",
                "global feedback gain (control theory)",
                "mean-field coupling constant",
            ],
            "notes": "Strength of the global v(t) feedback into the local PDE.",
        },
        "tau": {
            "ed_value": params.tau,
            "physical_value": params.tau * scales.T0,
            "physical_unit": "s",
            "physical_name": "participation timescale",
            "analogue_candidates": [
                "relaxation time (kinetic theory)",
                "damping time (oscillator)",
                "mean free time (transport)",
            ],
            "notes": "Controls how fast v responds to changes in F_avg.",
        },
        "zeta": {
            "ed_value": params.zeta,
            "physical_value": params.zeta / scales.T0,
            "physical_unit": "s^-1",
            "physical_name": "participation damping rate",
            "analogue_candidates": [
                "friction coefficient (Langevin)",
                "drag coefficient (fluid)",
                "decay rate (particle physics)",
            ],
            "notes": "Dissipation rate for the global mode v(t).",
        },
        "rho_star": {
            "ed_value": params.rho_star,
            "physical_value": params.rho_star * scales.R0,
            "physical_unit": "kg m^-3",
            "physical_name": "equilibrium density",
            "analogue_candidates": [
                "background density (cosmology)",
                "mean density (statistical mechanics)",
                "target concentration (chemistry)",
            ],
            "notes": "Unique attractor of the penalty term.",
        },
        "rho_max": {
            "ed_value": params.rho_max,
            "physical_value": params.rho_max * scales.R0,
            "physical_unit": "kg m^-3",
            "physical_name": "capacity bound / horizon density",
            "analogue_candidates": [
                "close-packing density (granular)",
                "Pauli exclusion limit (fermion)",
                "Chandrasekhar limit analogue",
            ],
            "notes": "M(rho) -> 0 at this value; creates dynamical horizons.",
        },
    }


def print_dictionary(params: EDParameters, scales: Scales) -> None:
    """Pretty-print the ED -> physics dictionary."""
    d = parameter_dictionary(params, scales)
    for name, info in d.items():
        print(f"\n{'=' * 60}")
        print(f"  {name}")
        print(f"{'=' * 60}")
        print(f"  ED value:        {info['ed_value']}")
        print(f"  Physical value:  {info['physical_value']}")
        print(f"  Unit:            {info['physical_unit']}")
        print(f"  Physical name:   {info['physical_name']}")
        print(f"  Analogues:")
        for a in info['analogue_candidates']:
            print(f"    - {a}")
        print(f"  Notes: {info['notes']}")


# ══════════════════════════════════════════════════════════════════════
#  Regime classification
# ══════════════════════════════════════════════════════════════════════

def classify_regime(scales: Scales) -> dict[str, bool]:
    """Classify the physical regime based on characteristic scales.

    Returns flags indicating which physical domains are relevant.
    """
    return {
        "quantum": scales.L0 < 1e-9,            # sub-nanometre
        "atomic": 1e-11 < scales.L0 < 1e-8,     # Angstrom to nm
        "mesoscopic": 1e-8 < scales.L0 < 1e-4,  # nm to 100 micron
        "macroscopic": 1e-4 < scales.L0 < 1e3,  # 100 micron to 1 km
        "astrophysical": scales.L0 > 1e12,       # > 1 AU
        "cosmological": scales.L0 > 1e22,        # > Mpc
        "fast": scales.T0 < 1e-12,              # sub-picosecond
        "slow": scales.T0 > 1e6,                # > 10 days
    }
