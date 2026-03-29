"""
edsim.invariants.spectral — Spectral entropy, modal hierarchy, anisotropy.

Computes spectral invariants from the transform-space representation
of the density field. Uses DCT-II for Neumann BCs, FFT for periodic.
"""

from __future__ import annotations

from typing import Optional

import numpy as np

from ..core.parameters import EDParameters


def _forward_transform(rho: np.ndarray, bc: str) -> np.ndarray:
    """Compute the forward spectral transform of a density field.

    For Neumann BCs: uses the multidimensional DCT-II (scipy.fft.dctn),
    which is the natural eigenbasis for the Neumann Laplacian.

    For periodic BCs: uses numpy.fft.rfftn (real FFT), returning
    complex coefficients.

    Parameters
    ----------
    rho : np.ndarray
        Density field, any dimension.
    bc : str
        Boundary condition type: "neumann" or "periodic".

    Returns
    -------
    np.ndarray
        Transform coefficients (real for DCT, complex for FFT).
    """
    if bc == "neumann":
        from scipy.fft import dctn
        # DCT-II, orthonormalised so Parseval's theorem holds:
        # sum(rho^2) = sum(rho_hat^2)
        return dctn(rho, type=2, norm="ortho")
    else:
        # Periodic: real FFT
        return np.fft.rfftn(rho)


def _power_spectrum(rho_hat: np.ndarray, bc: str) -> np.ndarray:
    """Compute the power spectrum |rho_hat_k|^2 from transform coefficients.

    Parameters
    ----------
    rho_hat : np.ndarray
        Transform-space coefficients.
    bc : str
        Boundary condition type (determines whether coefficients are
        real or complex).

    Returns
    -------
    np.ndarray
        Power spectrum, same shape as rho_hat.
    """
    if bc == "neumann":
        # DCT coefficients are real
        return rho_hat ** 2
    else:
        # FFT coefficients are complex
        return np.abs(rho_hat) ** 2


def spectral_entropy(rho: np.ndarray, params: EDParameters) -> float:
    """Compute spectral entropy H = -sum(p_k * ln(p_k)).

    Steps:
    1. Transform rho to spectral space (DCT for Neumann, FFT for periodic).
    2. Compute power spectrum P_k = |rho_hat_k|^2.
    3. Exclude the DC mode (k=0): the mean density does not contribute
       to structural entropy.
    4. Normalise: p_k = P_k / sum(P_k).
    5. Compute H = -sum(p_k * log(p_k + eps)).

    Parameters
    ----------
    rho : np.ndarray
        Density field.
    params : EDParameters
        Simulation parameters (uses bc for transform selection).

    Returns
    -------
    float
        Spectral entropy (0 = single mode, log(N) = equipartition).
    """
    rho_hat = _forward_transform(rho, params.bc)
    P = _power_spectrum(rho_hat, params.bc)

    # Flatten to 1D
    P_flat = P.ravel().copy()

    # Zero out the DC component (index 0 in flattened DCT/FFT output)
    P_flat[0] = 0.0

    # Normalise
    total = P_flat.sum()
    if total < 1e-30:
        return 0.0

    p = P_flat / total

    # Entropy with epsilon guard against log(0)
    eps = 1e-30
    mask = p > eps
    H = -np.sum(p[mask] * np.log(p[mask]))

    return float(H)


def modal_hierarchy(
    rho: np.ndarray,
    params: EDParameters,
    max_modes: int = 64,
) -> np.ndarray:
    """Compute sorted modal amplitudes |rho_hat_k|, descending.

    Steps:
    1. Transform rho to spectral space.
    2. Compute |rho_hat_k| for all modes.
    3. Exclude the DC mode.
    4. Sort in descending order.
    5. Return the first max_modes entries.

    Parameters
    ----------
    rho : np.ndarray
        Density field.
    params : EDParameters
        Simulation parameters.
    max_modes : int
        Maximum number of modes to return.

    Returns
    -------
    np.ndarray
        1D array of sorted amplitudes, length min(max_modes, total_modes-1).
    """
    rho_hat = _forward_transform(rho, params.bc)
    amplitudes = np.abs(rho_hat).ravel().copy()

    # Zero out the DC component
    amplitudes[0] = 0.0

    # Sort descending
    amplitudes.sort()
    amplitudes = amplitudes[::-1]

    # Trim to max_modes (excluding any leading zeros from DC removal)
    n = min(max_modes, amplitudes.size)
    return amplitudes[:n].copy()


def spectral_anisotropy(rho: np.ndarray, params: EDParameters) -> dict:
    """Compute the spectral inertia tensor and its eigenstructure.

    The inertia tensor is:
        I_ij = sum_k (k_i * k_j * |rho_hat_k|^2) / sum_k |rho_hat_k|^2

    Its eigenvalues measure directional energy concentration:
    - Equal eigenvalues = isotropic.
    - Unequal eigenvalues = anisotropic.

    Parameters
    ----------
    rho : np.ndarray
        Density field.
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    dict
        {"eigenvalues": np.ndarray, "eigenvectors": np.ndarray,
         "anisotropy_ratio": float}
    """
    d = rho.ndim
    rho_hat = _forward_transform(rho, params.bc)
    P = _power_spectrum(rho_hat, params.bc)

    # Build wavenumber grids
    if params.bc == "neumann":
        k_arrays = [np.arange(s) for s in rho_hat.shape]
    else:
        # For rfftn the last axis has shape N//2+1
        k_arrays = []
        for axis in range(d):
            if axis < d - 1:
                k_arrays.append(np.fft.fftfreq(rho.shape[axis], d=1.0) * rho.shape[axis])
            else:
                k_arrays.append(np.arange(rho_hat.shape[axis]))

    K = np.meshgrid(*k_arrays, indexing="ij")

    # Compute inertia tensor
    total_power = P.sum()
    if total_power < 1e-30:
        return {
            "eigenvalues": np.zeros(d),
            "eigenvectors": np.eye(d),
            "anisotropy_ratio": 1.0,
        }

    I_tensor = np.zeros((d, d))
    for i in range(d):
        for j in range(i, d):
            val = np.sum(K[i] * K[j] * P) / total_power
            I_tensor[i, j] = val
            I_tensor[j, i] = val

    eigvals, eigvecs = np.linalg.eigh(I_tensor)
    eigvals = eigvals[::-1]  # Sort descending
    eigvecs = eigvecs[:, ::-1]

    ratio = eigvals[-1] / eigvals[0] if eigvals[0] > 1e-30 else 1.0

    return {
        "eigenvalues": eigvals,
        "eigenvectors": eigvecs,
        "anisotropy_ratio": float(ratio),
    }


def radial_spectrum(
    rho: np.ndarray,
    params: EDParameters,
    n_bins: int = 32,
) -> tuple[np.ndarray, np.ndarray]:
    """Compute radially averaged power spectrum P(k) vs k.

    Parameters
    ----------
    rho : np.ndarray
        Density field.
    params : EDParameters
        Simulation parameters.
    n_bins : int
        Number of radial bins.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        (k_bins, P_k) -- bin centres and averaged power.
    """
    d = rho.ndim
    rho_hat = _forward_transform(rho, params.bc)
    P = _power_spectrum(rho_hat, params.bc)

    # Build wavenumber magnitude grid
    if params.bc == "neumann":
        k_arrays = [np.arange(s) for s in rho_hat.shape]
    else:
        k_arrays = []
        for axis in range(d):
            if axis < d - 1:
                k_arrays.append(np.fft.fftfreq(rho.shape[axis], d=1.0) * rho.shape[axis])
            else:
                k_arrays.append(np.arange(rho_hat.shape[axis]))

    K = np.meshgrid(*k_arrays, indexing="ij")
    k_mag = np.sqrt(sum(ki ** 2 for ki in K))

    # Bin by |k|
    k_max = k_mag.max()
    if k_max < 1e-30:
        return np.zeros(1), np.zeros(1)

    bin_edges = np.linspace(0, k_max, n_bins + 1)
    bin_centres = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    P_binned = np.zeros(n_bins)

    k_flat = k_mag.ravel()
    P_flat = P.ravel()
    bin_idx = np.digitize(k_flat, bin_edges) - 1
    bin_idx = np.clip(bin_idx, 0, n_bins - 1)

    for b in range(n_bins):
        mask = bin_idx == b
        if mask.any():
            P_binned[b] = P_flat[mask].mean()

    return bin_centres, P_binned
