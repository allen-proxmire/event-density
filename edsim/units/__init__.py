"""
edsim.units -- Physical units and dimensional mapping for ED-SIM-02.

This package provides an OPTIONAL layer that converts between
nondimensional ED solver variables and physical (SI) quantities.
The solver operates entirely in nondimensional form; physical units
are applied at the interface only.

Submodules
----------
constants
    Fundamental physical constants (SI, CODATA 2018).
scales
    Characteristic scales (L0, T0, R0, V0, E0) and scale factories
    for various physical regimes (Planck, quantum, galactic, etc.).
mapping
    Point-wise conversion functions and the ED -> physics dictionary.
wrapper
    High-level runner that accepts physical parameters and returns
    physical-units output.
"""

from .constants import hbar, G, c, k_B, m_p, m_e
from .scales import (
    Scales,
    compute_scales,
    planck_scales,
    quantum_scales,
    condensed_matter_scales,
    galactic_scales,
    cosmological_scales,
    custom_scales,
)
from .mapping import (
    ed_to_physical_rho,
    physical_to_ed_rho,
    ed_to_physical_time,
    physical_to_ed_time,
    ed_to_physical_length,
    physical_to_ed_length,
    ed_to_physical_velocity,
    physical_to_ed_velocity,
    ed_to_physical_energy,
    ed_to_physical_complexity,
    ed_to_physical_mass,
    ed_to_physical_correlation_length,
    parameter_dictionary,
    print_dictionary,
    classify_regime,
)
from .wrapper import (
    PhysicalParameters,
    PhysicalTimeSeries,
    convert_time_series,
    run_physical_simulation,
    run_physical_atlas,
)

__all__ = [
    # Constants
    "hbar", "G", "c", "k_B", "m_p", "m_e",
    # Scales
    "Scales", "compute_scales",
    "planck_scales", "quantum_scales",
    "condensed_matter_scales", "galactic_scales",
    "cosmological_scales", "custom_scales",
    # Mapping
    "ed_to_physical_rho", "physical_to_ed_rho",
    "ed_to_physical_time", "physical_to_ed_time",
    "ed_to_physical_length", "physical_to_ed_length",
    "ed_to_physical_velocity", "physical_to_ed_velocity",
    "ed_to_physical_energy", "ed_to_physical_complexity",
    "ed_to_physical_mass", "ed_to_physical_correlation_length",
    "parameter_dictionary", "print_dictionary", "classify_regime",
    # Wrapper
    "PhysicalParameters", "PhysicalTimeSeries",
    "convert_time_series",
    "run_physical_simulation", "run_physical_atlas",
]
