"""
edsim.performance — Backend acceleration for ED-SIM-02.

Provides optional Numba and JAX backends for FD operators and integrators.
Falls back to NumPy if accelerators are not installed.

Usage:
    params = EDParameters(..., backend="numba")  # or "jax", "numpy"
"""

from .numba_backend import NUMBA_AVAILABLE
from .jax_backend import JAX_AVAILABLE

__all__ = ["NUMBA_AVAILABLE", "JAX_AVAILABLE"]
