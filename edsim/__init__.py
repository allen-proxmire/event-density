"""
edsim — Event Density Simulation Platform v2 (ED-SIM-02)

A modular, extensible simulation platform for the Event Density PDE
across dimensions d = 1 through d = 4. Implements the canonical ED
architecture from ED-Phys-40.

Modules
-------
core
    PDE operators, constitutive functions, time integrators, boundary
    conditions, and spectral utilities.
invariants
    Full invariant atlas: energy, spectral, dissipation, morphology,
    topology, and correlation invariants.
experiments
    Run configurations, scenarios, parameter sweeps, and atlas generation.
reproducibility
    Nine-phase validation pipeline and consistency certificates.
"""

from .version import VERSION, get_version

__version__ = VERSION
__author__ = "Allen Proxmire"

from .core.parameters import EDParameters
from .experiments.runner import run_simulation, RunConfig, TimeSeries
from .invariants.atlas import compute_atlas

__all__ = [
    "EDParameters",
    "RunConfig",
    "TimeSeries",
    "run_simulation",
    "compute_atlas",
    "get_version",
    "__version__",
]
