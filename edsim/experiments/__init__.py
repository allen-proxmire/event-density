"""
edsim.experiments — Experiment harness for ED-SIM-02.

Provides RunConfig, run_simulation, batch execution, parameter sweeps,
and predefined scenarios.
"""

from .runner import RunConfig, TimeSeries, run_simulation
from .scenarios import scenario_A, scenario_B, scenario_C, scenario_D
from .sweeps import run_sweep, run_batch
from .atlas import run_atlas

__all__ = [
    "RunConfig", "TimeSeries", "run_simulation",
    "scenario_A", "scenario_B", "scenario_C", "scenario_D",
    "run_sweep", "run_batch",
    "run_atlas",
]
