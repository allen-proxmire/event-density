"""
edsim.invariants.correlation — Correlation lengths and structure functions.

Computes spatial correlation diagnostics from the density field:
    - correlation length xi via Wiener-Khinchin autocorrelation
    - second-order structure function S_2(r) via axis-aligned displacements

Supports d = 2, 3, 4.
"""

from __future__ import annotations

import numpy as np
from scipy.fft import dctn, idctn

from ..core.parameters import EDParameters


def autocorrelation(rho: np.ndarray, params: EDParameters) -> np.ndarray:
    """Compute the normalised autocorrelation field via Wiener-Khinchin.

    C(r) = IFFT(|FFT(delta_rho)|^2) / C(0)

    where delta_rho = rho - mean(rho). The result is normalised so C(0) = 1.

    Uses DCT for Neumann BCs (the power spectrum of a DCT is real and
    positive, and the inverse DCT of the power spectrum gives the
    autocorrelation).

    Parameters
    ----------
    rho : np.ndarray
        Density field, any dimension.
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    np.ndarray
        Normalised autocorrelation field, same shape as rho.
        C[0,...,0] = 1.0 (by construction).
    """
    # Subtract mean
    delta_rho = rho - np.mean(rho)

    # Power spectrum via DCT (Neumann-compatible)
    if params.bc == "neumann":
        rho_hat = dctn(delta_rho, type=2, norm="ortho")
    else:
        rho_hat = np.fft.fftn(delta_rho)

    power = np.abs(rho_hat) ** 2

    # Inverse transform of power spectrum = autocorrelation
    if params.bc == "neumann":
        C = idctn(power, type=2, norm="ortho")
    else:
        C = np.real(np.fft.ifftn(power))

    # Normalise so C(0) = 1
    C0 = C.ravel()[0]
    if abs(C0) > 1e-30:
        C = C / C0
    else:
        C = np.zeros_like(C)

    return C


def _radial_profile(field: np.ndarray, dx: tuple, n_bins: int) -> tuple[np.ndarray, np.ndarray]:
    """Compute a radially averaged profile of a d-dimensional field.

    Bins grid points by their distance from the origin (index [0,...,0])
    and averages the field values in each bin.

    Parameters
    ----------
    field : np.ndarray
        Field of shape (N1, ..., Nd).
    dx : tuple[float, ...]
        Grid spacing per axis.
    n_bins : int
        Number of radial bins.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        (r_centres, profile) — bin centres and averaged values.
    """
    d = field.ndim

    # Build distance-from-origin grid
    # For autocorrelation, index 0 = zero lag; index k = lag of k*dx
    idx_arrays = [np.arange(s) * dx[i] for i, s in enumerate(field.shape)]
    grids = np.meshgrid(*idx_arrays, indexing="ij")
    r = np.sqrt(sum(g ** 2 for g in grids))

    # Bin by distance
    r_max = r.max()
    if r_max < 1e-30:
        return np.zeros(1), np.zeros(1)

    bin_edges = np.linspace(0, r_max, n_bins + 1)
    r_centres = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    profile = np.zeros(n_bins)
    counts = np.zeros(n_bins)

    r_flat = r.ravel()
    f_flat = field.ravel()
    bin_idx = np.digitize(r_flat, bin_edges) - 1
    bin_idx = np.clip(bin_idx, 0, n_bins - 1)

    # Accumulate
    np.add.at(profile, bin_idx, f_flat)
    np.add.at(counts, bin_idx, 1.0)

    # Average
    mask = counts > 0
    profile[mask] /= counts[mask]

    return r_centres, profile


def correlation_length(rho: np.ndarray, params: EDParameters) -> float:
    """Compute the correlation length xi from the autocorrelation of rho.

    xi = sqrt(sum(r^2 * C(r)) / sum(C(r)))

    where C(r) is the radially averaged normalised autocorrelation.
    Only positive values of C(r) contribute (negative tails are excluded
    to keep xi well-defined).

    Parameters
    ----------
    rho : np.ndarray
        Density field (2D, 3D, or 4D).
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    float
        Correlation length in physical units. Returns 0.0 if the field
        is uniform (no spatial structure).
    """
    # Check for uniform field
    if np.std(rho) < 1e-30:
        return 0.0

    C = autocorrelation(rho, params)

    # Radially average the autocorrelation
    n_bins = min(32, max(rho.shape) // 2)
    r_centres, C_radial = _radial_profile(C, params.dx, n_bins)

    # Use only positive part of C(r) for xi computation
    # (autocorrelation can go negative at large r)
    positive = C_radial > 0
    if not np.any(positive):
        return 0.0

    r_pos = r_centres[positive]
    C_pos = C_radial[positive]

    # xi^2 = sum(r^2 * C(r)) / sum(C(r))
    numerator = np.sum(r_pos ** 2 * C_pos)
    denominator = np.sum(C_pos)

    if denominator < 1e-30:
        return 0.0

    xi_sq = numerator / denominator
    return float(np.sqrt(max(xi_sq, 0.0)))


def structure_function_2(
    rho: np.ndarray,
    params: EDParameters,
    n_bins: int = 16,
) -> tuple[np.ndarray, np.ndarray]:
    """Compute the second-order structure function S_2(r).

    S_2(r) = < |rho(x + r) - rho(x)|^2 >

    averaged over all points x and displacements with |r| in each bin.

    Uses axis-aligned displacements for efficiency: for each axis i and
    each shift s = 1, 2, ..., smax, computes the squared difference
    field and bins by physical distance |r| = s * dx_i.

    Parameters
    ----------
    rho : np.ndarray
        Density field (2D, 3D, or 4D).
    params : EDParameters
        Simulation parameters.
    n_bins : int
        Number of radial bins.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        (r_bins, S2) — bin centres and structure function values.
    """
    d = rho.ndim
    dx = params.dx

    # Maximum shift: half the smallest axis (Neumann: no wrap)
    smax = min(s // 2 for s in rho.shape)
    if smax < 1:
        return np.zeros(1), np.zeros(1)

    # Physical distance of the longest axis-aligned shift
    r_max = max(smax * dxi for dxi in dx) * 1.01  # slight margin
    bin_edges = np.linspace(0, r_max, n_bins + 1)
    r_centres = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    S2_accum = np.zeros(n_bins)
    count_accum = np.zeros(n_bins)

    for axis in range(d):
        for s in range(1, smax + 1):
            # Physical distance for this shift
            r_phys = s * dx[axis]

            # Find which bin this falls in
            b = int(np.searchsorted(bin_edges, r_phys)) - 1
            b = max(0, min(b, n_bins - 1))

            # Compute |rho(x + s*e_i) - rho(x)|^2 over the interior
            # For axis-aligned shift s along axis i:
            sl_left = [slice(None)] * d
            sl_right = [slice(None)] * d
            sl_left[axis] = slice(0, -s)
            sl_right[axis] = slice(s, None)

            diff_sq = (rho[tuple(sl_right)] - rho[tuple(sl_left)]) ** 2
            S2_accum[b] += np.sum(diff_sq)
            count_accum[b] += diff_sq.size

    # Average
    mask = count_accum > 0
    S2 = np.zeros(n_bins)
    S2[mask] = S2_accum[mask] / count_accum[mask]

    return r_centres, S2


# Legacy alias
def structure_function(
    rho: np.ndarray,
    p: int,
    dx: tuple,
    n_bins: int = 50,
) -> tuple[np.ndarray, np.ndarray]:
    """Compute the p-th order structure function S_p(r).

    For p=2, delegates to structure_function_2.
    Other orders use the same axis-aligned displacement approach.

    Parameters
    ----------
    rho : np.ndarray
        Density field.
    p : int
        Order of the structure function.
    dx : tuple[float, ...]
        Grid spacing per axis.
    n_bins : int
        Number of radial bins.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        (r_bins, S_p)
    """
    d = rho.ndim
    smax = min(s // 2 for s in rho.shape)
    if smax < 1:
        return np.zeros(1), np.zeros(1)

    r_max = max(smax * dxi for dxi in dx) * 1.01
    bin_edges = np.linspace(0, r_max, n_bins + 1)
    r_centres = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    Sp_accum = np.zeros(n_bins)
    count_accum = np.zeros(n_bins)

    for axis in range(d):
        for s in range(1, smax + 1):
            r_phys = s * dx[axis]
            b = max(0, min(int(np.searchsorted(bin_edges, r_phys)) - 1, n_bins - 1))

            sl_left = [slice(None)] * d
            sl_right = [slice(None)] * d
            sl_left[axis] = slice(0, -s)
            sl_right[axis] = slice(s, None)

            diff_p = np.abs(rho[tuple(sl_right)] - rho[tuple(sl_left)]) ** p
            Sp_accum[b] += np.sum(diff_p)
            count_accum[b] += diff_p.size

    mask = count_accum > 0
    Sp = np.zeros(n_bins)
    Sp[mask] = Sp_accum[mask] / count_accum[mask]

    return r_centres, Sp
