"""
edsim.experiments.scenarios — Predefined test scenarios.

Provides a catalog of canonical ED experiments as Scenario objects.
Each scenario encapsulates parameter construction and IC generation,
making experiments reproducible and self-documenting.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np

from ..core.parameters import EDParameters
from .runner import RunConfig, generate_ic


@dataclass(frozen=True)
class Scenario:
    """A named, reproducible ED experiment specification.

    Attributes
    ----------
    name : str
        Short identifier (e.g., "A_2d_cosine").
    description : str
        Human-readable description of the experiment.
    make_config : Callable[[], RunConfig]
        Factory that returns a fully specified RunConfig.
    """

    name: str
    description: str
    make_config: Callable[[], RunConfig]


# ---------------------------------------------------------------------------
# Helper: modify a frozen EDParameters by replacing selected fields
# ---------------------------------------------------------------------------

def _replace_params(params: EDParameters, **kwargs) -> EDParameters:
    """Create a new EDParameters with selected fields replaced.

    Parameters
    ----------
    params : EDParameters
        Base parameters.
    **kwargs
        Fields to override.

    Returns
    -------
    EDParameters
        New parameters with overrides applied.
    """
    d = params.to_dict()
    d.update(kwargs)
    # Ensure tuples
    if "L" in d and isinstance(d["L"], list):
        d["L"] = tuple(d["L"])
    if "N" in d and isinstance(d["N"], list):
        d["N"] = tuple(d["N"])
    return EDParameters.from_dict(d)


# ---------------------------------------------------------------------------
# Scenario A: Isotropic cosine relaxation (2D)
# ---------------------------------------------------------------------------

def _make_config_A_2d() -> RunConfig:
    params = EDParameters(
        d=2, N=(32, 32), L=(1.0, 1.0),
        D=0.3, H=0.15, zeta=0.1, tau=1.0,
        rho_star=0.5, rho_max=1.0, M0=1.0, beta=2.0, P0=1.0,
        dt=5e-4, T=0.5, k_out=100,
        method="implicit_euler", bc="neumann", seed=42,
    )
    return RunConfig(params=params, ic_type="cosine", ic_kwargs={"A": 0.03, "Nm": 2})


SCENARIO_A_2D = Scenario(
    name="A_2d_cosine",
    description="2D isotropic cosine relaxation. Moderate amplitude A=0.03, Nm=2. "
                "Tests Laws 1-2 (attractor, energy monotonicity).",
    make_config=_make_config_A_2d,
)


# ---------------------------------------------------------------------------
# Scenario B: Isotropic cosine relaxation (3D)
# ---------------------------------------------------------------------------

def _make_config_B_3d() -> RunConfig:
    params = EDParameters(
        d=3, N=(16, 16, 16), L=(1.0, 1.0, 1.0),
        D=0.3, H=0.15, zeta=0.1, tau=1.0,
        rho_star=0.5, rho_max=1.0, M0=1.0, beta=2.0, P0=1.0,
        dt=5e-4, T=0.25, k_out=50,
        method="implicit_euler", bc="neumann", seed=42,
    )
    return RunConfig(params=params, ic_type="cosine", ic_kwargs={"A": 0.03, "Nm": 2})


SCENARIO_B_3D = Scenario(
    name="B_3d_cosine",
    description="3D isotropic cosine relaxation. Tests morphology (filament/sheet/blob) "
                "and dimensional complexity scaling.",
    make_config=_make_config_B_3d,
)


# ---------------------------------------------------------------------------
# Scenario C: Isotropic cosine relaxation (4D)
# ---------------------------------------------------------------------------

def _make_config_C_4d() -> RunConfig:
    params = EDParameters(
        d=4, N=(8, 8, 8, 8), L=(1.0, 1.0, 1.0, 1.0),
        D=0.3, H=0.15, zeta=0.1, tau=1.0,
        rho_star=0.5, rho_max=1.0, M0=1.0, beta=2.0, P0=1.0,
        dt=5e-4, T=0.1, k_out=20,
        method="implicit_euler", bc="neumann", seed=42,
    )
    return RunConfig(params=params, ic_type="cosine", ic_kwargs={"A": 0.03, "Nm": 2})


SCENARIO_C_4D = Scenario(
    name="C_4d_cosine",
    description="4D isotropic cosine relaxation. Tests 4D morphology (pancake class), "
                "factorial complexity law, and horizon suppression.",
    make_config=_make_config_C_4d,
)


# ---------------------------------------------------------------------------
# Scenario D: Random IC (2D)
# ---------------------------------------------------------------------------

def _make_config_D_2d_random() -> RunConfig:
    params = EDParameters(
        d=2, N=(32, 32), L=(1.0, 1.0),
        D=0.3, H=0.15, zeta=0.1, tau=1.0,
        rho_star=0.5, rho_max=1.0, M0=1.0, beta=2.0, P0=1.0,
        dt=5e-4, T=0.5, k_out=100,
        method="implicit_euler", bc="neumann", seed=123,
    )
    return RunConfig(params=params, ic_type="random", ic_kwargs={"A": 0.02})


SCENARIO_D_2D_RANDOM = Scenario(
    name="D_2d_random",
    description="2D random-noise IC. Small amplitude A=0.02 around rho_star. "
                "Tests broadband relaxation and spectral entropy evolution.",
    make_config=_make_config_D_2d_random,
)


# ---------------------------------------------------------------------------
# Scenario E: High-amplitude cosine (2D, near-horizon)
# ---------------------------------------------------------------------------

def _make_config_E_2d_high_amp() -> RunConfig:
    params = EDParameters(
        d=2, N=(32, 32), L=(1.0, 1.0),
        D=0.3, H=0.15, zeta=0.1, tau=1.0,
        rho_star=0.5, rho_max=1.0, M0=1.0, beta=2.0, P0=1.0,
        dt=1e-4, T=0.2, k_out=200,
        method="implicit_euler", bc="neumann", seed=42,
    )
    return RunConfig(params=params, ic_type="cosine", ic_kwargs={"A": 0.10, "Nm": 2})


SCENARIO_E_2D_HIGH = Scenario(
    name="E_2d_high_amplitude",
    description="2D high-amplitude cosine A=0.10. Tests near-capacity dynamics, "
                "horizon approach, and stiff-regime stability.",
    make_config=_make_config_E_2d_high_amp,
)


# ---------------------------------------------------------------------------
# Scenario F: Gaussian bump (3D)
# ---------------------------------------------------------------------------

def _make_config_F_3d_gaussian() -> RunConfig:
    params = EDParameters(
        d=3, N=(16, 16, 16), L=(1.0, 1.0, 1.0),
        D=0.3, H=0.15, zeta=0.1, tau=1.0,
        rho_star=0.5, rho_max=1.0, M0=1.0, beta=2.0, P0=1.0,
        dt=5e-4, T=0.25, k_out=50,
        method="implicit_euler", bc="neumann", seed=42,
    )
    return RunConfig(params=params, ic_type="gaussian", ic_kwargs={"A": 0.05, "sigma": 0.15})


SCENARIO_F_3D_GAUSSIAN = Scenario(
    name="F_3d_gaussian",
    description="3D Gaussian bump IC. Tests localised perturbation decay, "
                "blob-dominated morphology, and correlation length evolution.",
    make_config=_make_config_F_3d_gaussian,
)


# ---------------------------------------------------------------------------
# Catalog
# ---------------------------------------------------------------------------

_SCENARIOS = {
    "A_2d_cosine": SCENARIO_A_2D,
    "B_3d_cosine": SCENARIO_B_3D,
    "C_4d_cosine": SCENARIO_C_4D,
    "D_2d_random": SCENARIO_D_2D_RANDOM,
    "E_2d_high_amplitude": SCENARIO_E_2D_HIGH,
    "F_3d_gaussian": SCENARIO_F_3D_GAUSSIAN,
}


def get_scenarios() -> dict[str, Scenario]:
    """Return the full catalog of predefined scenarios.

    Returns
    -------
    dict[str, Scenario]
        Mapping from scenario name to Scenario object.
    """
    return dict(_SCENARIOS)


def get_scenario(name: str) -> Scenario:
    """Look up a scenario by name.

    Parameters
    ----------
    name : str
        Scenario name (e.g., "A_2d_cosine").

    Returns
    -------
    Scenario

    Raises
    ------
    KeyError
        If name is not in the catalog.
    """
    if name not in _SCENARIOS:
        available = ", ".join(sorted(_SCENARIOS.keys()))
        raise KeyError(f"Unknown scenario '{name}'. Available: {available}")
    return _SCENARIOS[name]


# ---------------------------------------------------------------------------
# Legacy function-style API (delegates to Scenario objects)
# ---------------------------------------------------------------------------

def scenario_A(d: int = 2, N: int = 32, output_dir: str = "./output/A") -> RunConfig:
    """Scenario A: Isotropic cosine relaxation."""
    params = EDParameters(
        d=d, N=(N,) * d, L=(1.0,) * d,
        D=0.3, H=0.15, zeta=0.1, tau=1.0,
        dt=5e-4, T=0.5, k_out=100,
        method="implicit_euler", bc="neumann",
    )
    return RunConfig(params=params, ic_type="cosine", ic_kwargs={"A": 0.03, "Nm": 2},
                     output_dir=output_dir)


def scenario_B(d: int = 3, N: int = 16, output_dir: str = "./output/B") -> RunConfig:
    """Scenario B: 3D cosine relaxation."""
    return scenario_A(d=d, N=N, output_dir=output_dir)


def scenario_C(d: int = 4, N: int = 8, output_dir: str = "./output/C") -> RunConfig:
    """Scenario C: 4D cosine relaxation."""
    params = EDParameters(
        d=d, N=(N,) * d, L=(1.0,) * d,
        D=0.3, H=0.15, zeta=0.1, tau=1.0,
        dt=5e-4, T=0.1, k_out=20,
        method="implicit_euler", bc="neumann",
    )
    return RunConfig(params=params, ic_type="cosine", ic_kwargs={"A": 0.03, "Nm": 2},
                     output_dir=output_dir)


def scenario_D(d: int = 2, N: int = 32, output_dir: str = "./output/D") -> RunConfig:
    """Scenario D: Random IC relaxation."""
    params = EDParameters(
        d=d, N=(N,) * d, L=(1.0,) * d,
        D=0.3, H=0.15, zeta=0.1, tau=1.0,
        dt=5e-4, T=0.5, k_out=100,
        method="implicit_euler", bc="neumann", seed=123,
    )
    return RunConfig(params=params, ic_type="random", ic_kwargs={"A": 0.02},
                     output_dir=output_dir)
