"""
edsim2d — 2D Event Density simulation package.

Submodules:
  solver       — core PDE solver (edsim_solver_2d)
  invariants   — 2D invariant atlas (invariants_2d)
  visualization— 2D visualization suite (visualization_2d)
  runner       — experiment orchestration (RunConfig2D, run_simulation)
  experiments  — predefined 2D scenarios (A2D–D2D)
"""

import os as _os
import sys as _sys

# Add the parent directory so the original flat modules are importable
_PARENT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
if _PARENT not in _sys.path:
    _sys.path.insert(0, _PARENT)

from edsim_solver_2d import (
    EDParameters2D,
    make_grid_2d,
    laplacian_fd_2d,
    grad_squared_fd_2d,
    compute_operators_2d,
    operator_F_fd_2d,
    spatial_avg_2d,
    advance_v,
    enforce_bounds_2d,
    energy_2d,
    total_mass_2d,
    SpectralState2D,
    step_etdrk4_2d,
    step_cn_fd_2d,
    initialize_state_2d,
    step_2d,
    run_simulation_2d,
)

from invariants_2d import (
    compute_invariants_2d,
    compute_spectral_invariants_2d,
    compute_geometric_invariants_2d,
    compute_dynamical_invariants_2d,
)

__all__ = [
    "EDParameters2D",
    "make_grid_2d",
    "initialize_state_2d",
    "step_2d",
    "run_simulation_2d",
    "compute_invariants_2d",
    "compute_spectral_invariants_2d",
    "compute_geometric_invariants_2d",
    "compute_dynamical_invariants_2d",
    "energy_2d",
    "total_mass_2d",
    "enforce_bounds_2d",
    "spatial_avg_2d",
    "SpectralState2D",
]
