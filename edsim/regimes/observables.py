"""
edsim.regimes.observables -- Physical observables from PhysicalTimeSeries.

Extracts scalar and time-dependent physical quantities from a completed
PhysicalTimeSeries.  All outputs are in SI units.

These observables are the "measurable predictions" of the ED framework
when anchored to a specific physical regime.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

import numpy as np

from ..units.wrapper import PhysicalTimeSeries
from ..units.scales import Scales


@dataclass
class PhysicalObservables:
    """Collection of physical observables extracted from a simulation.

    All quantities in SI unless noted.
    """

    # Scalar summaries
    regime_name: str = ""
    total_mass_kg: float = 0.0
    mass_change_fraction: float = 0.0
    initial_energy_J: float = 0.0
    final_energy_J: float = 0.0
    energy_ratio: float = 0.0
    correlation_length_initial_m: float = 0.0
    correlation_length_final_m: float = 0.0
    xi_growth_factor: float = 0.0
    characteristic_velocity_m_s: float = 0.0
    diffusion_timescale_s: float = 0.0
    simulation_duration_s: float = 0.0

    # Time series (physical)
    times_s: list[float] = field(default_factory=list)
    energy_J: list[float] = field(default_factory=list)
    mass_kg: list[float] = field(default_factory=list)
    correlation_length_m: list[float] = field(default_factory=list)

    # Dimensionless (passed through)
    R_grad_mean: float = 0.0
    R_pen_mean: float = 0.0
    R_part_mean: float = 0.0
    spectral_entropy_initial: float = 0.0
    spectral_entropy_final: float = 0.0
    morphology_initial: dict = field(default_factory=dict)
    morphology_final: dict = field(default_factory=dict)
    euler_chi_initial: int = 0
    euler_chi_final: int = 0
    chi_conserved: bool = True


def compute_observables(
    pts: PhysicalTimeSeries,
    regime_name: str = "",
) -> PhysicalObservables:
    """Extract physical observables from a PhysicalTimeSeries.

    Parameters
    ----------
    pts : PhysicalTimeSeries
        Completed simulation in physical units.
    regime_name : str
        Label for the regime (informational).

    Returns
    -------
    PhysicalObservables
        All observables in SI.
    """
    n = len(pts.times_s)
    if n == 0:
        return PhysicalObservables(regime_name=regime_name)

    M0 = pts.mass_kg[0]
    Mf = pts.mass_kg[-1]
    E0 = pts.energy_J[0]
    Ef = pts.energy_J[-1]
    xi0 = pts.correlation_length_m[0] if pts.correlation_length_m else 0.0
    xif = pts.correlation_length_m[-1] if pts.correlation_length_m else 0.0

    obs = PhysicalObservables(
        regime_name=regime_name,
        total_mass_kg=M0,
        mass_change_fraction=abs(Mf - M0) / abs(M0) if abs(M0) > 1e-300 else 0.0,
        initial_energy_J=E0,
        final_energy_J=Ef,
        energy_ratio=Ef / E0 if abs(E0) > 1e-300 else 0.0,
        correlation_length_initial_m=xi0,
        correlation_length_final_m=xif,
        xi_growth_factor=xif / xi0 if abs(xi0) > 1e-300 else 0.0,
        simulation_duration_s=pts.times_s[-1],
        # Time series
        times_s=list(pts.times_s),
        energy_J=list(pts.energy_J),
        mass_kg=list(pts.mass_kg),
        correlation_length_m=list(pts.correlation_length_m),
        # Dimensionless
        R_grad_mean=float(np.mean(pts.R_grad)) if pts.R_grad else 0.0,
        R_pen_mean=float(np.mean(pts.R_pen)) if pts.R_pen else 0.0,
        R_part_mean=float(np.mean(pts.R_part)) if pts.R_part else 0.0,
        spectral_entropy_initial=pts.spectral_entropy[0] if pts.spectral_entropy else 0.0,
        spectral_entropy_final=pts.spectral_entropy[-1] if pts.spectral_entropy else 0.0,
        morphology_initial=pts.morphology_fractions[0] if pts.morphology_fractions else {},
        morphology_final=pts.morphology_fractions[-1] if pts.morphology_fractions else {},
        euler_chi_initial=pts.euler_characteristic[0] if pts.euler_characteristic else 0,
        euler_chi_final=pts.euler_characteristic[-1] if pts.euler_characteristic else 0,
        chi_conserved=(
            len(set(pts.euler_characteristic)) <= 1
            if pts.euler_characteristic else True
        ),
    )

    if pts.scales is not None:
        obs.characteristic_velocity_m_s = pts.scales.V0
        obs.diffusion_timescale_s = pts.scales.T0

    return obs


def observables_table(obs_list: list[PhysicalObservables]) -> str:
    """Format a list of observables as a Markdown table.

    Parameters
    ----------
    obs_list : list[PhysicalObservables]

    Returns
    -------
    str
        Markdown table.
    """
    lines = [
        "| Regime | Mass [kg] | Energy ratio | xi growth | R_grad | chi conserved |",
        "|--------|-----------|-------------|-----------|--------|---------------|",
    ]
    for o in obs_list:
        lines.append(
            f"| {o.regime_name} "
            f"| {o.total_mass_kg:.4e} "
            f"| {o.energy_ratio:.4f} "
            f"| {o.xi_growth_factor:.2f} "
            f"| {o.R_grad_mean:.4f} "
            f"| {'Yes' if o.chi_conserved else 'No'} |"
        )
    return "\n".join(lines)


def compare_observables(
    obs_list: list[PhysicalObservables],
) -> dict[str, list]:
    """Compare observables across regimes.

    Returns a dictionary suitable for plotting or tabulation.

    Parameters
    ----------
    obs_list : list[PhysicalObservables]

    Returns
    -------
    dict[str, list]
        Keys are observable names; values are lists aligned with obs_list.
    """
    return {
        "regime": [o.regime_name for o in obs_list],
        "mass_kg": [o.total_mass_kg for o in obs_list],
        "energy_ratio": [o.energy_ratio for o in obs_list],
        "xi_growth": [o.xi_growth_factor for o in obs_list],
        "R_grad": [o.R_grad_mean for o in obs_list],
        "R_pen": [o.R_pen_mean for o in obs_list],
        "R_part": [o.R_part_mean for o in obs_list],
        "H_initial": [o.spectral_entropy_initial for o in obs_list],
        "H_final": [o.spectral_entropy_final for o in obs_list],
        "chi_conserved": [o.chi_conserved for o in obs_list],
    }
