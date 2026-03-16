"""
ED-Phys-02: Finite-Difference Gradient Operators
===================================================
Canonical source: ED-Phys-01 §7.2 – §7.4

Implements:
  - Discrete Laplacian (∇²ρ) for 1D and 2D
  - Discrete gradient magnitude squared (|∇ρ|²) for 1D and 2D
  - Mobility M(ρ) and M'(ρ)
  - Boundary condition wrapping

All operators match the finite-difference stencils specified in
ED-Phys-01 §7.2 exactly.
"""

import numpy as np
from typing import Literal


# ============================================================
# Boundary-condition helpers
# ============================================================

def _pad_periodic(rho: np.ndarray) -> np.ndarray:
    """Pad array with periodic boundary conditions (one ghost cell each side)."""
    if rho.ndim == 1:
        return np.pad(rho, 1, mode='wrap')
    return np.pad(rho, 1, mode='wrap')


def _pad_reflecting(rho: np.ndarray) -> np.ndarray:
    """Pad array with reflecting (Neumann) boundary conditions."""
    if rho.ndim == 1:
        return np.pad(rho, 1, mode='reflect')
    return np.pad(rho, 1, mode='reflect')


def _pad_absorbing(rho: np.ndarray, rho_min: float) -> np.ndarray:
    """Pad array with absorbing (Dirichlet) boundary conditions."""
    if rho.ndim == 1:
        padded = np.pad(rho, 1, mode='constant', constant_values=rho_min)
    else:
        padded = np.pad(rho, 1, mode='constant', constant_values=rho_min)
    return padded


def _pad(rho: np.ndarray, boundary: str, rho_min: float = 0.01) -> np.ndarray:
    """Pad rho with ghost cells according to boundary type."""
    if boundary == "periodic":
        return _pad_periodic(rho)
    elif boundary == "reflecting":
        return _pad_reflecting(rho)
    elif boundary == "absorbing":
        return _pad_absorbing(rho, rho_min)
    raise ValueError(f"Unknown boundary type: {boundary!r}")


# ============================================================
# Discrete Laplacian — ED-Phys-01 §7.2
# ============================================================

def discrete_laplacian(
    rho: np.ndarray,
    dx: float,
    boundary: str = "periodic",
    rho_min: float = 0.01,
) -> np.ndarray:
    """Compute the discrete Laplacian ∇²ρ.

    1D: ∇²ρ_i = (ρ_{i+1} − 2ρ_i + ρ_{i−1}) / Δx²
    2D: ∇²ρ_{i,j} = (ρ_{i+1,j} + ρ_{i−1,j} + ρ_{i,j+1} + ρ_{i,j−1} − 4ρ_{i,j}) / Δx²
    """
    p = _pad(rho, boundary, rho_min)
    dx2 = dx * dx

    if rho.ndim == 1:
        # p has shape (N+2,); interior is p[1:-1]
        lap = (p[2:] - 2.0 * p[1:-1] + p[:-2]) / dx2
    elif rho.ndim == 2:
        # p has shape (N+2, N+2); interior is p[1:-1, 1:-1]
        lap = (
            p[2:, 1:-1] + p[:-2, 1:-1] +
            p[1:-1, 2:] + p[1:-1, :-2] -
            4.0 * p[1:-1, 1:-1]
        ) / dx2
    else:
        raise ValueError(f"Only 1D and 2D supported, got ndim={rho.ndim}")

    return lap


# ============================================================
# Discrete Gradient Magnitude Squared — ED-Phys-01 §7.2
# ============================================================

def discrete_grad_squared(
    rho: np.ndarray,
    dx: float,
    boundary: str = "periodic",
    rho_min: float = 0.01,
) -> np.ndarray:
    """Compute |∇ρ|² using central differences.

    1D: |∇ρ|²_i = ((ρ_{i+1} − ρ_{i−1}) / (2Δx))²
    2D: |∇ρ|²_{i,j} = ((ρ_{i+1,j} − ρ_{i−1,j}) / (2Δx))²
                     + ((ρ_{i,j+1} − ρ_{i,j−1}) / (2Δx))²
    """
    p = _pad(rho, boundary, rho_min)
    two_dx = 2.0 * dx

    if rho.ndim == 1:
        grad_x = (p[2:] - p[:-2]) / two_dx
        grad_sq = grad_x ** 2
    elif rho.ndim == 2:
        grad_x = (p[2:, 1:-1] - p[:-2, 1:-1]) / two_dx
        grad_y = (p[1:-1, 2:] - p[1:-1, :-2]) / two_dx
        grad_sq = grad_x ** 2 + grad_y ** 2
    else:
        raise ValueError(f"Only 1D and 2D supported, got ndim={rho.ndim}")

    return grad_sq


def discrete_grad_magnitude(
    rho: np.ndarray,
    dx: float,
    boundary: str = "periodic",
    rho_min: float = 0.01,
) -> np.ndarray:
    """Compute |∇ρ| (the magnitude, not squared)."""
    return np.sqrt(discrete_grad_squared(rho, dx, boundary, rho_min))


# ============================================================
# Mobility — ED-Phys-01 §7.3, §7.4  (from ED-12.5)
# ============================================================

def mobility(
    rho: np.ndarray,
    M_0: float,
    rho_max: float,
    n_mob: int,
) -> np.ndarray:
    """Compute mobility M(ρ) = M_0 · max(0, 1 − ρ/ρ_max)^n_mob.

    ED-Phys-01 §7.3: The max(0,...) clamp prevents negative mobility
    if ρ overshoots ρ_max.
    """
    ratio = np.clip(1.0 - rho / rho_max, 0.0, None)
    return M_0 * ratio ** n_mob


def mobility_derivative(
    rho: np.ndarray,
    M_0: float,
    rho_max: float,
    n_mob: int,
) -> np.ndarray:
    """Compute M'(ρ) = −M_0 · (n_mob/ρ_max) · max(0, 1 − ρ/ρ_max)^{n_mob−1}.

    ED-Phys-01 §7.4.
    """
    ratio = np.clip(1.0 - rho / rho_max, 0.0, None)
    return -M_0 * (n_mob / rho_max) * ratio ** (n_mob - 1)
