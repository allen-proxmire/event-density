"""
edsim.invariants.morphology — Hessian-based morphological classification.

Classifies spatial structure into blobs, sheets, filaments, and pancakes
based on the eigenvalue structure of the density Hessian.
Supports d = 2, 3, and 4.

Classification scheme (sign-based, following ED-Phys-35/39/40):

    2D: blob / sheet
    3D: blob / filament / sheet
    4D: blob / filament / sheet / pancake
"""

from __future__ import annotations

import numpy as np

from ..core.parameters import EDParameters


def hessian_eigenvalues(rho: np.ndarray, params: EDParameters) -> np.ndarray:
    """Compute Hessian eigenvalues at each grid point, sorted descending.

    Uses np.gradient for first derivatives (handles boundaries with
    one-sided differences), then applies central differences to the
    first derivatives to obtain second derivatives.

    Parameters
    ----------
    rho : np.ndarray
        Density field of shape (N1, ..., Nd) with d = 2 or 3.
    params : EDParameters
        Simulation parameters (for grid spacing).

    Returns
    -------
    np.ndarray
        Eigenvalues of shape (*grid_shape, d), sorted descending
        (lambda_1 >= lambda_2 >= ... >= lambda_d) at each point.
    """
    d = rho.ndim
    dx = params.dx
    grid_shape = rho.shape

    # Step 1: compute first derivatives using np.gradient
    # grad[i] = d(rho)/d(x_i), shape = grid_shape
    grad = [np.gradient(rho, dx[i], axis=i) for i in range(d)]

    # Step 2: compute second derivatives d(grad[i])/d(x_j)
    # H_ij = d^2(rho)/(dx_i dx_j)
    # Only need upper triangle (symmetric): i <= j
    hessian_components = {}
    for i in range(d):
        for j in range(i, d):
            hessian_components[(i, j)] = np.gradient(grad[i], dx[j], axis=j)

    # Step 3: assemble Hessian matrix at each point and compute eigenvalues
    # Build array of shape (*grid_shape, d, d)
    H_matrix = np.zeros(grid_shape + (d, d))
    for i in range(d):
        for j in range(i, d):
            H_matrix[..., i, j] = hessian_components[(i, j)]
            if i != j:
                H_matrix[..., j, i] = hessian_components[(i, j)]

    # Step 4: eigenvalues at each point
    # eigvalsh returns eigenvalues in ascending order
    eigvals = np.linalg.eigvalsh(H_matrix)

    # Reverse to descending order: lambda_1 >= lambda_2 >= ...
    eigvals = eigvals[..., ::-1]

    return eigvals


def morphology_fractions(eigenvalues: np.ndarray, params: EDParameters) -> dict:
    """Classify each grid point and return volume fractions.

    Classification uses eigenvalue signs with a tolerance threshold
    to handle near-zero values.

    For 2D (lambda_1 >= lambda_2):
        blob:  lambda_1 < -tol AND lambda_2 < -tol
        sheet: everything else

    For 3D (lambda_1 >= lambda_2 >= lambda_3):
        blob:     all three negative
        filament: two negative, one near-zero or positive
        sheet:    everything else

    For 4D (lambda_1 >= lambda_2 >= lambda_3 >= lambda_4):
        blob:     all four negative
        filament: three negative, one near-zero or positive
        sheet:    two negative, rest near-zero or positive
        pancake:  one negative, rest near-zero or positive (or all non-negative)

    Parameters
    ----------
    eigenvalues : np.ndarray
        Hessian eigenvalues of shape (*grid_shape, d).
    params : EDParameters
        Simulation parameters (for dimension).

    Returns
    -------
    dict
        {"blob": float, "sheet": float, "filament": float, "pancake": float}
        Volume fractions summing to 1.0.
        Unused classes are 0.0 for lower dimensions.
    """
    d = params.d
    total_points = eigenvalues[..., 0].size

    # Adaptive threshold: fraction of the maximum absolute eigenvalue
    max_abs = np.max(np.abs(eigenvalues))
    tol = 1e-6 * max_abs if max_abs > 1e-30 else 1e-30

    if d == 2:
        lam1 = eigenvalues[..., 0]
        lam2 = eigenvalues[..., 1]

        blob_mask = (lam1 < -tol) & (lam2 < -tol)

        f_blob = float(np.sum(blob_mask)) / total_points
        f_sheet = 1.0 - f_blob

        return {
            "blob": f_blob,
            "sheet": f_sheet,
            "filament": 0.0,
            "pancake": 0.0,
        }

    elif d == 3:
        lam1 = eigenvalues[..., 0]
        lam2 = eigenvalues[..., 1]
        lam3 = eigenvalues[..., 2]

        blob_mask = (lam1 < -tol) & (lam2 < -tol) & (lam3 < -tol)
        filament_mask = (lam1 < -tol) & (lam2 < -tol) & (lam3 >= -tol)
        sheet_mask = ~blob_mask & ~filament_mask

        f_blob = float(np.sum(blob_mask)) / total_points
        f_filament = float(np.sum(filament_mask)) / total_points
        f_sheet = float(np.sum(sheet_mask)) / total_points

        return {
            "blob": f_blob,
            "sheet": f_sheet,
            "filament": f_filament,
            "pancake": 0.0,
        }

    elif d == 4:
        lam1 = eigenvalues[..., 0]
        lam2 = eigenvalues[..., 1]
        lam3 = eigenvalues[..., 2]
        lam4 = eigenvalues[..., 3]

        # Count how many eigenvalues are negative at each point
        neg_count = (
            (lam1 < -tol).astype(int)
            + (lam2 < -tol).astype(int)
            + (lam3 < -tol).astype(int)
            + (lam4 < -tol).astype(int)
        )

        blob_mask = neg_count == 4       # all 4 negative
        filament_mask = neg_count == 3   # 3 negative, 1 not
        sheet_mask = neg_count == 2      # 2 negative, 2 not
        pancake_mask = neg_count <= 1    # 0 or 1 negative

        f_blob = float(np.sum(blob_mask)) / total_points
        f_filament = float(np.sum(filament_mask)) / total_points
        f_sheet = float(np.sum(sheet_mask)) / total_points
        f_pancake = float(np.sum(pancake_mask)) / total_points

        return {
            "blob": f_blob,
            "sheet": f_sheet,
            "filament": f_filament,
            "pancake": f_pancake,
        }

    else:
        # Fallback for d=1
        return {
            "blob": 1.0,
            "sheet": 0.0,
            "filament": 0.0,
            "pancake": 0.0,
        }


def filamentarity_field(eigenvalues: np.ndarray) -> np.ndarray:
    """Compute the filamentarity indicator at each grid point.

    filamentarity = (|lambda_{d-1}| - |lambda_d|) / |lambda_1|

    High values indicate filament-like structure (one small eigenvalue).

    Parameters
    ----------
    eigenvalues : np.ndarray
        Hessian eigenvalues of shape (*N, d), sorted descending.

    Returns
    -------
    np.ndarray
        Filamentarity values in [0, 1], shape (*N,).
    """
    d = eigenvalues.shape[-1]
    abs_eig = np.abs(eigenvalues)
    denom = abs_eig[..., 0]
    denom = np.where(denom > 1e-30, denom, 1e-30)
    return (abs_eig[..., d - 2] - abs_eig[..., d - 1]) / denom


def sheetness_field(eigenvalues: np.ndarray) -> np.ndarray:
    """Compute the sheetness indicator at each grid point.

    For d >= 3:
        sheetness = (|lambda_{d-2}| - |lambda_{d-1}|) / |lambda_1|

    Parameters
    ----------
    eigenvalues : np.ndarray
        Hessian eigenvalues of shape (*N, d) with d >= 3.

    Returns
    -------
    np.ndarray
        Sheetness values in [0, 1], shape (*N,).
    """
    d = eigenvalues.shape[-1]
    if d < 3:
        return np.zeros(eigenvalues.shape[:-1])
    abs_eig = np.abs(eigenvalues)
    denom = abs_eig[..., 0]
    denom = np.where(denom > 1e-30, denom, 1e-30)
    return (abs_eig[..., d - 3] - abs_eig[..., d - 2]) / denom


def blobness_field(eigenvalues: np.ndarray) -> np.ndarray:
    """Compute the blobness indicator at each grid point.

    blobness = |lambda_d| / |lambda_1|

    High values indicate isotropic (blob-like) structure.

    Parameters
    ----------
    eigenvalues : np.ndarray
        Hessian eigenvalues of shape (*N, d).

    Returns
    -------
    np.ndarray
        Blobness values in [0, 1], shape (*N,).
    """
    abs_eig = np.abs(eigenvalues)
    denom = abs_eig[..., 0]
    denom = np.where(denom > 1e-30, denom, 1e-30)
    return abs_eig[..., -1] / denom
