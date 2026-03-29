"""
edsim.core.integrators — Time integration schemes for the ED PDE.

Provides three integrators behind a common protocol:
- ETD-RK4 (spectral, primary)
- Crank-Nicolson / ADI (FD, secondary)
- Implicit Euler (FD, fallback)
"""

from .base import Integrator, get_integrator
from .etdrk4 import ETDRK4Integrator
from .crank_nicolson import CrankNicolsonIntegrator
from .implicit_euler import ImplicitEulerIntegrator

__all__ = [
    "Integrator",
    "get_integrator",
    "ETDRK4Integrator",
    "CrankNicolsonIntegrator",
    "ImplicitEulerIntegrator",
]
