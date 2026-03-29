"""
edsim.core — Core computation tier for ED-SIM-02.

Provides the canonical ED PDE operator, constitutive functions,
time integrators, boundary conditions, and spectral utilities
for dimensions d = 1 through d = 4.
"""

from .parameters import EDParameters
from .constitutive import mobility, mobility_deriv, penalty, density_potential
from .operators import operator_F_fd, operator_F_spectral, laplacian_fd, grad_squared_fd
from .participation import advance_v, spatial_average
from .boundary import apply_bc, strip_ghost
from .spectral import SpectralState, forward_transform, inverse_transform

__all__ = [
    "EDParameters",
    "mobility", "mobility_deriv", "penalty", "density_potential",
    "operator_F_fd", "operator_F_spectral", "laplacian_fd", "grad_squared_fd",
    "advance_v", "spatial_average",
    "apply_bc", "strip_ghost",
    "SpectralState", "forward_transform", "inverse_transform",
]
