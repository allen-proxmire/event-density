"""
edsim.core.operators — Spatial operators for the ED PDE.

Computes F[rho] = M(rho)*Lap(rho) + M'(rho)*|grad(rho)|^2 - P(rho)
for d = 1..4 using finite-difference (FD) or spectral kernels.
"""

from __future__ import annotations
from typing import Optional

import numpy as np

from .parameters import EDParameters
from .constitutive import mobility, mobility_deriv, penalty
from .boundary import (
    apply_bc, strip_ghost,
    apply_bc_2d, strip_ghost_2d,
    apply_bc_3d, strip_ghost_3d,
    apply_bc_4d, strip_ghost_4d,
)


# ---------------------------------------------------------------------------
# 2D finite-difference operators
# ---------------------------------------------------------------------------

def laplacian_fd_2d(rho: np.ndarray, dx: tuple) -> np.ndarray:
    """Compute the 2D Laplacian using a 5-point stencil with Neumann BCs.

    Parameters
    ----------
    rho : np.ndarray
        Density field of shape (Nx, Ny).
    dx : tuple[float, float]
        Grid spacing (dx, dy).

    Returns
    -------
    np.ndarray
        Laplacian field, same shape as rho.
    """
    dx2 = dx[0] ** 2
    dy2 = dx[1] ** 2
    rho_pad = apply_bc_2d(rho)
    lap = (
        (rho_pad[2:, 1:-1] + rho_pad[:-2, 1:-1] - 2.0 * rho_pad[1:-1, 1:-1]) / dx2
        + (rho_pad[1:-1, 2:] + rho_pad[1:-1, :-2] - 2.0 * rho_pad[1:-1, 1:-1]) / dy2
    )
    return lap


def grad_squared_fd_2d(rho: np.ndarray, dx: tuple) -> np.ndarray:
    """Compute |nabla rho|^2 using 2nd-order central differences in 2D.

    Parameters
    ----------
    rho : np.ndarray
        Density field of shape (Nx, Ny).
    dx : tuple[float, float]
        Grid spacing (dx, dy).

    Returns
    -------
    np.ndarray
        |grad rho|^2, same shape as rho.
    """
    rho_pad = apply_bc_2d(rho)
    drho_dx = (rho_pad[2:, 1:-1] - rho_pad[:-2, 1:-1]) / (2.0 * dx[0])
    drho_dy = (rho_pad[1:-1, 2:] - rho_pad[1:-1, :-2]) / (2.0 * dx[1])
    return drho_dx ** 2 + drho_dy ** 2


def operator_F_local_fd_2d(rho: np.ndarray, params: EDParameters) -> np.ndarray:
    """Compute the LOCAL density operator F_local[rho] in 2D (no participation).

    F_local = M(rho) * Lap(rho) + M'(rho) * |grad(rho)|^2 - P(rho)
    """
    M = mobility(rho, params)
    Mp = mobility_deriv(rho, params)
    P = penalty(rho, params)
    lap = laplacian_fd_2d(rho, params.dx)
    gs = grad_squared_fd_2d(rho, params.dx)
    return M * lap + Mp * gs - P


# ---------------------------------------------------------------------------
# 3D finite-difference operators
# ---------------------------------------------------------------------------

def laplacian_fd_3d(rho: np.ndarray, dx: tuple) -> np.ndarray:
    """Compute the 3D Laplacian using a 7-point stencil with Neumann BCs.

    Stencil (isotropic dx):
        L[i,j,k] = (sum of 6 neighbours - 6*rho[i,j,k]) / dx^2

    For anisotropic grids, uses independent spacing per axis.

    Parameters
    ----------
    rho : np.ndarray
        Density field of shape (Nx, Ny, Nz).
    dx : tuple[float, float, float]
        Grid spacing (dx, dy, dz).

    Returns
    -------
    np.ndarray
        Laplacian field, same shape as rho.
    """
    dx2 = dx[0] ** 2
    dy2 = dx[1] ** 2
    dz2 = dx[2] ** 2
    rho_pad = apply_bc_3d(rho)
    # Interior of padded array: [1:-1, 1:-1, 1:-1]
    c = rho_pad[1:-1, 1:-1, 1:-1]
    lap = (
        (rho_pad[2:, 1:-1, 1:-1] + rho_pad[:-2, 1:-1, 1:-1] - 2.0 * c) / dx2
        + (rho_pad[1:-1, 2:, 1:-1] + rho_pad[1:-1, :-2, 1:-1] - 2.0 * c) / dy2
        + (rho_pad[1:-1, 1:-1, 2:] + rho_pad[1:-1, 1:-1, :-2] - 2.0 * c) / dz2
    )
    return lap


def grad_squared_fd_3d(rho: np.ndarray, dx: tuple) -> np.ndarray:
    """Compute |nabla rho|^2 using 2nd-order central differences in 3D.

    Parameters
    ----------
    rho : np.ndarray
        Density field of shape (Nx, Ny, Nz).
    dx : tuple[float, float, float]
        Grid spacing (dx, dy, dz).

    Returns
    -------
    np.ndarray
        |grad rho|^2, same shape as rho.
    """
    rho_pad = apply_bc_3d(rho)
    drho_dx = (rho_pad[2:, 1:-1, 1:-1] - rho_pad[:-2, 1:-1, 1:-1]) / (2.0 * dx[0])
    drho_dy = (rho_pad[1:-1, 2:, 1:-1] - rho_pad[1:-1, :-2, 1:-1]) / (2.0 * dx[1])
    drho_dz = (rho_pad[1:-1, 1:-1, 2:] - rho_pad[1:-1, 1:-1, :-2]) / (2.0 * dx[2])
    return drho_dx ** 2 + drho_dy ** 2 + drho_dz ** 2


def operator_F_local_fd_3d(rho: np.ndarray, params: EDParameters) -> np.ndarray:
    """Compute the LOCAL density operator F_local[rho] in 3D (no participation).

    F_local = M(rho) * Lap(rho) + M'(rho) * |grad(rho)|^2 - P(rho)
    """
    M = mobility(rho, params)
    Mp = mobility_deriv(rho, params)
    P = penalty(rho, params)
    lap = laplacian_fd_3d(rho, params.dx)
    gs = grad_squared_fd_3d(rho, params.dx)
    return M * lap + Mp * gs - P


# ---------------------------------------------------------------------------
# 4D finite-difference operators
# ---------------------------------------------------------------------------

def laplacian_fd_4d(rho: np.ndarray, dx: tuple) -> np.ndarray:
    """Compute the 4D Laplacian using a 9-point cross stencil with Neumann BCs.

    Parameters
    ----------
    rho : np.ndarray
        Density field of shape (N1, N2, N3, N4).
    dx : tuple[float, float, float, float]
        Grid spacing per axis.

    Returns
    -------
    np.ndarray
        Laplacian field, same shape as rho.
    """
    rho_pad = apply_bc_4d(rho)
    c = rho_pad[1:-1, 1:-1, 1:-1, 1:-1]
    lap = (
        (rho_pad[2:, 1:-1, 1:-1, 1:-1] + rho_pad[:-2, 1:-1, 1:-1, 1:-1] - 2.0 * c) / (dx[0] ** 2)
        + (rho_pad[1:-1, 2:, 1:-1, 1:-1] + rho_pad[1:-1, :-2, 1:-1, 1:-1] - 2.0 * c) / (dx[1] ** 2)
        + (rho_pad[1:-1, 1:-1, 2:, 1:-1] + rho_pad[1:-1, 1:-1, :-2, 1:-1] - 2.0 * c) / (dx[2] ** 2)
        + (rho_pad[1:-1, 1:-1, 1:-1, 2:] + rho_pad[1:-1, 1:-1, 1:-1, :-2] - 2.0 * c) / (dx[3] ** 2)
    )
    return lap


def grad_squared_fd_4d(rho: np.ndarray, dx: tuple) -> np.ndarray:
    """Compute |nabla rho|^2 using 2nd-order central differences in 4D.

    Parameters
    ----------
    rho : np.ndarray
        Density field of shape (N1, N2, N3, N4).
    dx : tuple[float, float, float, float]
        Grid spacing per axis.

    Returns
    -------
    np.ndarray
        |grad rho|^2, same shape as rho.
    """
    rho_pad = apply_bc_4d(rho)
    c = slice(1, -1)
    drho_d0 = (rho_pad[2:, c, c, c] - rho_pad[:-2, c, c, c]) / (2.0 * dx[0])
    drho_d1 = (rho_pad[c, 2:, c, c] - rho_pad[c, :-2, c, c]) / (2.0 * dx[1])
    drho_d2 = (rho_pad[c, c, 2:, c] - rho_pad[c, c, :-2, c]) / (2.0 * dx[2])
    drho_d3 = (rho_pad[c, c, c, 2:] - rho_pad[c, c, c, :-2]) / (2.0 * dx[3])
    return drho_d0 ** 2 + drho_d1 ** 2 + drho_d2 ** 2 + drho_d3 ** 2


def operator_F_local_fd_4d(rho: np.ndarray, params: EDParameters) -> np.ndarray:
    """Compute the LOCAL density operator F_local[rho] in 4D (no participation).

    F_local = M(rho) * Lap(rho) + M'(rho) * |grad(rho)|^2 - P(rho)
    """
    M = mobility(rho, params)
    Mp = mobility_deriv(rho, params)
    P = penalty(rho, params)
    lap = laplacian_fd_4d(rho, params.dx)
    gs = grad_squared_fd_4d(rho, params.dx)
    return M * lap + Mp * gs - P


# ---------------------------------------------------------------------------
# 4D total and split operators
# ---------------------------------------------------------------------------

def operator_F_fd_4d(
    rho: np.ndarray,
    params: EDParameters,
    v: float = 0.0,
) -> np.ndarray:
    """Compute the TOTAL density operator in 4D including participation."""
    F_local = operator_F_local_fd_4d(rho, params)
    return params.D * F_local + params.H * v


def operator_F_split_fd_4d(
    rho: np.ndarray,
    params: EDParameters,
    v: float = 0.0,
) -> tuple[np.ndarray, np.ndarray]:
    """Compute both local and total operators in 4D."""
    F_local = operator_F_local_fd_4d(rho, params)
    F_total = params.D * F_local + params.H * v
    return F_local, F_total


# ---------------------------------------------------------------------------
# Unified split operator (dispatches on dimension)
# ---------------------------------------------------------------------------

def operator_F_local_fd(rho: np.ndarray, params: EDParameters) -> np.ndarray:
    """Compute the local operator F_local for any supported dimension.

    Dispatches to dimension-specific implementations for 2D, 3D, and 4D,
    and falls back to the generic loop for other dimensions.

    If params.backend == "numba" and Numba is available, uses the
    accelerated kernels for 2D.

    Parameters
    ----------
    rho : np.ndarray
        Density field.
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    np.ndarray
        Local operator values.
    """
    backend = getattr(params, "backend", "numpy")

    if backend == "numba" and rho.ndim == 2:
        from ..performance.numba_backend import NUMBA_AVAILABLE, operator_F_local_fd_2d_numba
        if NUMBA_AVAILABLE:
            return operator_F_local_fd_2d_numba(rho, params)
        # Fall through to numpy if numba not installed

    if rho.ndim == 2:
        return operator_F_local_fd_2d(rho, params)
    elif rho.ndim == 3:
        return operator_F_local_fd_3d(rho, params)
    elif rho.ndim == 4:
        return operator_F_local_fd_4d(rho, params)
    else:
        # Generic path for 1D
        M = mobility(rho, params)
        Mp = mobility_deriv(rho, params)
        P = penalty(rho, params)
        lap = laplacian_fd(rho, params.dx, params.bc)
        gs = grad_squared_fd(rho, params.dx, params.bc)
        return M * lap + Mp * gs - P


def operator_F_split_fd(
    rho: np.ndarray,
    params: EDParameters,
    v: float = 0.0,
) -> tuple[np.ndarray, np.ndarray]:
    """Compute both local and total operators for any dimension.

    Parameters
    ----------
    rho : np.ndarray
        Density field.
    params : EDParameters
        Simulation parameters.
    v : float
        Current participation variable.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        (F_local, F_total) where:
        - F_local = M*Lap + M'*|grad|^2 - P
        - F_total = D * F_local + H * v
    """
    F_local = operator_F_local_fd(rho, params)
    F_total = params.D * F_local + params.H * v
    return F_local, F_total


# ---------------------------------------------------------------------------
# Legacy 2D-specific split (delegates to unified)
# ---------------------------------------------------------------------------

def operator_F_fd_2d(
    rho: np.ndarray,
    params: EDParameters,
    v: float = 0.0,
) -> np.ndarray:
    """Compute the TOTAL density operator in 2D including participation."""
    F_local = operator_F_local_fd_2d(rho, params)
    return params.D * F_local + params.H * v


def operator_F_split_fd_2d(
    rho: np.ndarray,
    params: EDParameters,
    v: float = 0.0,
) -> tuple[np.ndarray, np.ndarray]:
    """Compute both local and total operators in 2D."""
    return operator_F_split_fd(rho, params, v)


# ---------------------------------------------------------------------------
# 3D total operator
# ---------------------------------------------------------------------------

def operator_F_fd_3d(
    rho: np.ndarray,
    params: EDParameters,
    v: float = 0.0,
) -> np.ndarray:
    """Compute the TOTAL density operator in 3D including participation."""
    F_local = operator_F_local_fd_3d(rho, params)
    return params.D * F_local + params.H * v


def operator_F_split_fd_3d(
    rho: np.ndarray,
    params: EDParameters,
    v: float = 0.0,
) -> tuple[np.ndarray, np.ndarray]:
    """Compute both local and total operators in 3D."""
    return operator_F_split_fd(rho, params, v)


# ---------------------------------------------------------------------------
# Generic d-dimensional FD operators
# ---------------------------------------------------------------------------

def laplacian_fd(rho: np.ndarray, dx: tuple, bc: str) -> np.ndarray:
    """Compute the d-dimensional Laplacian using 2nd-order central differences.

    Generic loop-over-axes implementation for any dimension.

    Parameters
    ----------
    rho : np.ndarray
        Density field of shape (N1, ..., Nd).
    dx : tuple[float, ...]
        Grid spacing per axis.
    bc : str
        Boundary condition type.

    Returns
    -------
    np.ndarray
        Laplacian field, same shape as rho.
    """
    d = rho.ndim
    rho_pad = apply_bc(rho, bc, d)

    lap = np.zeros_like(rho)
    for axis in range(d):
        sl_center = [slice(1, -1)] * d
        sl_plus = [slice(1, -1)] * d
        sl_minus = [slice(1, -1)] * d
        sl_plus[axis] = slice(2, None)
        sl_minus[axis] = slice(0, -2)

        lap += (
            rho_pad[tuple(sl_plus)]
            + rho_pad[tuple(sl_minus)]
            - 2.0 * rho_pad[tuple(sl_center)]
        ) / (dx[axis] ** 2)

    return lap


def grad_squared_fd(rho: np.ndarray, dx: tuple, bc: str) -> np.ndarray:
    """Compute |nabla rho|^2 using 2nd-order central differences, any dimension."""
    d = rho.ndim
    rho_pad = apply_bc(rho, bc, d)

    gs = np.zeros_like(rho)
    for axis in range(d):
        sl_plus = [slice(1, -1)] * d
        sl_minus = [slice(1, -1)] * d
        sl_plus[axis] = slice(2, None)
        sl_minus[axis] = slice(0, -2)

        grad_comp = (rho_pad[tuple(sl_plus)] - rho_pad[tuple(sl_minus)]) / (2.0 * dx[axis])
        gs += grad_comp ** 2

    return gs


def gradient_fd(rho: np.ndarray, dx: tuple, bc: str) -> list[np.ndarray]:
    """Compute the gradient of rho as a list of d component arrays."""
    d = rho.ndim
    rho_pad = apply_bc(rho, bc, d)
    components = []

    for axis in range(d):
        sl_plus = [slice(1, -1)] * d
        sl_minus = [slice(1, -1)] * d
        sl_plus[axis] = slice(2, None)
        sl_minus[axis] = slice(0, -2)

        grad_comp = (rho_pad[tuple(sl_plus)] - rho_pad[tuple(sl_minus)]) / (2.0 * dx[axis])
        components.append(grad_comp)

    return components


def operator_F_fd(rho: np.ndarray, params: EDParameters, v: float = 0.0) -> np.ndarray:
    """Compute the total ED density RHS using finite differences.

    Returns D * F_local + H * v.  Dispatches to dimension-specific
    implementations for 2D and 3D.
    """
    _, F_total = operator_F_split_fd(rho, params, v)
    return F_total


# ---------------------------------------------------------------------------
# Spectral operators (stubs — not part of first working path)
# ---------------------------------------------------------------------------

def laplacian_spectral(rho_hat: np.ndarray, eigenvalues: np.ndarray) -> np.ndarray:
    """Compute the spectral Laplacian: multiply by -mu_k in transform space."""
    return -eigenvalues * rho_hat


def operator_F_spectral(
    rho: np.ndarray,
    rho_hat: np.ndarray,
    params: EDParameters,
    sstate: "SpectralState",
) -> np.ndarray:
    """Compute F[rho] via hybrid spectral/physical method.

    Not implemented in the first working path.
    """
    raise NotImplementedError("Spectral operator not yet implemented")
