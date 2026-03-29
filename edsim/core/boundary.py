"""
edsim.core.boundary — Boundary condition enforcement via ghost cells.

Supports Neumann (mirror), periodic (wrap), and Dirichlet (fixed-value)
boundary conditions for d = 1..4.
"""

from __future__ import annotations

import numpy as np


# ---------------------------------------------------------------------------
# Generic d-dimensional interface
# ---------------------------------------------------------------------------

def apply_bc(rho: np.ndarray, bc: str, d: int) -> np.ndarray:
    """Pad the density array with one ghost cell per side per axis.

    Parameters
    ----------
    rho : np.ndarray
        Density field of shape (N1, ..., Nd).
    bc : str
        Boundary condition type: "neumann", "periodic", "dirichlet".
    d : int
        Spatial dimension.

    Returns
    -------
    np.ndarray
        Padded density field of shape (N1+2, ..., Nd+2).
    """
    if bc == "neumann":
        return np.pad(rho, pad_width=1, mode="reflect")
    elif bc == "periodic":
        return np.pad(rho, pad_width=1, mode="wrap")
    elif bc == "dirichlet":
        return np.pad(rho, pad_width=1, mode="constant", constant_values=0.0)
    else:
        raise ValueError(f"Unknown BC type: {bc}")


def strip_ghost(rho: np.ndarray, d: int) -> np.ndarray:
    """Remove ghost cells from a padded array.

    Parameters
    ----------
    rho : np.ndarray
        Padded density field.
    d : int
        Spatial dimension.

    Returns
    -------
    np.ndarray
        Interior density field with ghost cells removed.
    """
    slices = tuple(slice(1, -1) for _ in range(d))
    return rho[slices]


# ---------------------------------------------------------------------------
# Convenience wrappers for 2D
# ---------------------------------------------------------------------------

def apply_bc_2d(rho: np.ndarray) -> np.ndarray:
    """Pad a 2D density array with Neumann (mirror) ghost cells.

    Parameters
    ----------
    rho : np.ndarray
        Density field of shape (Nx, Ny).

    Returns
    -------
    np.ndarray
        Padded field of shape (Nx+2, Ny+2).
    """
    return np.pad(rho, pad_width=1, mode="reflect")


def strip_ghost_2d(rho: np.ndarray) -> np.ndarray:
    """Remove ghost cells from a 2D padded array.

    Parameters
    ----------
    rho : np.ndarray
        Padded field of shape (Nx+2, Ny+2).

    Returns
    -------
    np.ndarray
        Interior field of shape (Nx, Ny).
    """
    return rho[1:-1, 1:-1]


# ---------------------------------------------------------------------------
# Convenience wrappers for 3D
# ---------------------------------------------------------------------------

def apply_bc_3d(rho: np.ndarray) -> np.ndarray:
    """Pad a 3D density array with Neumann (mirror) ghost cells.

    Parameters
    ----------
    rho : np.ndarray
        Density field of shape (Nx, Ny, Nz).

    Returns
    -------
    np.ndarray
        Padded field of shape (Nx+2, Ny+2, Nz+2).
    """
    return np.pad(rho, pad_width=1, mode="reflect")


def strip_ghost_3d(rho: np.ndarray) -> np.ndarray:
    """Remove ghost cells from a 3D padded array.

    Parameters
    ----------
    rho : np.ndarray
        Padded field of shape (Nx+2, Ny+2, Nz+2).

    Returns
    -------
    np.ndarray
        Interior field of shape (Nx, Ny, Nz).
    """
    return rho[1:-1, 1:-1, 1:-1]


# ---------------------------------------------------------------------------
# Convenience wrappers for 4D
# ---------------------------------------------------------------------------

def apply_bc_4d(rho: np.ndarray) -> np.ndarray:
    """Pad a 4D density array with Neumann (mirror) ghost cells.

    Parameters
    ----------
    rho : np.ndarray
        Density field of shape (N1, N2, N3, N4).

    Returns
    -------
    np.ndarray
        Padded field of shape (N1+2, N2+2, N3+2, N4+2).
    """
    return np.pad(rho, pad_width=1, mode="reflect")


def strip_ghost_4d(rho: np.ndarray) -> np.ndarray:
    """Remove ghost cells from a 4D padded array.

    Parameters
    ----------
    rho : np.ndarray
        Padded field of shape (N1+2, N2+2, N3+2, N4+2).

    Returns
    -------
    np.ndarray
        Interior field of shape (N1, N2, N3, N4).
    """
    return rho[1:-1, 1:-1, 1:-1, 1:-1]


# ---------------------------------------------------------------------------
# Spectral BC compatibility
# ---------------------------------------------------------------------------

def apply_bc_spectral(rho: np.ndarray, bc: str) -> np.ndarray:
    """Apply boundary conditions compatible with spectral transforms.

    For Neumann BCs the field already has the correct symmetry for DCT-I.
    For periodic BCs no modification is needed.

    Parameters
    ----------
    rho : np.ndarray
        Density field.
    bc : str
        Boundary condition type.

    Returns
    -------
    np.ndarray
        BC-compatible density field (unchanged for well-posed inputs).
    """
    return rho.copy()
