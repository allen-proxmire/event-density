"""
edsim.math.modal -- Modal decomposition and hierarchy extraction.

Extracts the full modal structure A_k(t) from a TimeSeries, identifies
the dominant mode cascade, and characterises the spectral subranges
(inertial, dissipative).

This module extends the invariants.spectral layer with *time-resolved*
modal tracking, enabling transient classification and architectural
law verification.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from scipy.fft import dctn

from ..core.parameters import EDParameters
from ..experiments.runner import TimeSeries


@dataclass
class ModalSpectrum:
    """Time-resolved spectral decomposition of the density field.

    Attributes
    ----------
    times : np.ndarray
        Time values, shape (n_t,).
    k_values : np.ndarray
        Flattened wavenumber indices (excluding DC), shape (n_k,).
    amplitudes : np.ndarray
        Modal amplitudes |rho_hat_k(t)|, shape (n_t, n_k), DC excluded.
    k_magnitudes : np.ndarray
        Wavenumber magnitudes |k|, shape (n_k,).
    dominant_mode_idx : np.ndarray
        Index of the dominant mode at each time, shape (n_t,).
    dc_amplitude : np.ndarray
        DC mode amplitude (mean density) at each time, shape (n_t,).
    """

    times: np.ndarray
    k_values: np.ndarray
    amplitudes: np.ndarray
    k_magnitudes: np.ndarray
    dominant_mode_idx: np.ndarray
    dc_amplitude: np.ndarray


@dataclass
class ModalHierarchy:
    """Characterisation of the modal cascade structure.

    Attributes
    ----------
    primary_k : int
        Flattened index of the primary (most energetic) mode.
    primary_amplitude : float
        Amplitude of the primary mode at t=0.
    secondary_k : np.ndarray
        Indices of the secondary cascade modes (next 3-5 by energy).
    inertial_range : tuple[float, float]
        (k_min, k_max) of the inertial subrange where A_k ~ k^{-alpha}.
    inertial_exponent : float
        Power-law exponent alpha in the inertial range.
    dissipative_cutoff : float
        Wavenumber k_d above which modes decay faster than the inertial law.
    energy_concentration : float
        Fraction of total spectral energy in the top 10% of modes.
    hierarchy_ratio : float
        A_1 / A_2 (ratio of leading to second mode amplitude).
    """

    primary_k: int = 0
    primary_amplitude: float = 0.0
    secondary_k: np.ndarray = field(default_factory=lambda: np.array([], dtype=int))
    inertial_range: tuple = (0.0, 0.0)
    inertial_exponent: float = 0.0
    dissipative_cutoff: float = 0.0
    energy_concentration: float = 0.0
    hierarchy_ratio: float = 0.0


def compute_modal_spectrum(ts: TimeSeries, params: EDParameters) -> ModalSpectrum:
    """Compute the full time-resolved modal spectrum from a TimeSeries.

    Uses DCT-II (Neumann) or FFT (periodic) consistent with the solver.

    Parameters
    ----------
    ts : TimeSeries
        Completed simulation output.
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    ModalSpectrum
        Full time-resolved spectral decomposition.
    """
    n_t = len(ts.fields)
    if n_t == 0:
        return ModalSpectrum(
            times=np.array([]),
            k_values=np.array([]),
            amplitudes=np.zeros((0, 0)),
            k_magnitudes=np.array([]),
            dominant_mode_idx=np.array([], dtype=int),
            dc_amplitude=np.array([]),
        )

    # Build wavenumber grid from first field
    rho0 = ts.fields[0]
    d = rho0.ndim
    shape = rho0.shape

    # Wavenumber index arrays
    k_arrays = [np.arange(s) for s in shape]
    K = np.meshgrid(*k_arrays, indexing="ij")
    k_mag = np.sqrt(sum(ki.astype(float) ** 2 for ki in K)).ravel()

    n_modes = k_mag.size

    # Indices of non-DC modes
    non_dc = np.arange(n_modes)
    non_dc = non_dc[1:]  # exclude flattened index 0 (the DC mode)
    k_mag_non_dc = k_mag[non_dc]

    n_k = non_dc.size
    times = np.array(ts.times, dtype=float)
    amplitudes = np.zeros((n_t, n_k))
    dc_amp = np.zeros(n_t)

    for i, rho in enumerate(ts.fields):
        if params.bc == "neumann":
            rho_hat = dctn(rho, type=2, norm="ortho")
        else:
            rho_hat = np.fft.fftn(rho)
        amp_flat = np.abs(rho_hat).ravel()
        dc_amp[i] = amp_flat[0]
        amplitudes[i, :] = amp_flat[non_dc]

    dominant = np.argmax(amplitudes, axis=1)

    return ModalSpectrum(
        times=times,
        k_values=non_dc,
        amplitudes=amplitudes,
        k_magnitudes=k_mag_non_dc,
        dominant_mode_idx=dominant,
        dc_amplitude=dc_amp,
    )


def extract_modal_hierarchy(
    modal_spectrum: ModalSpectrum,
    n_secondary: int = 5,
) -> ModalHierarchy:
    """Identify the modal hierarchy from a ModalSpectrum.

    Uses the initial-time amplitudes to define the primary mode,
    secondary cascade, inertial subrange, and dissipative tail.

    Parameters
    ----------
    modal_spectrum : ModalSpectrum
        From compute_modal_spectrum().
    n_secondary : int
        Number of secondary cascade modes to identify.

    Returns
    -------
    ModalHierarchy
    """
    if modal_spectrum.amplitudes.size == 0:
        return ModalHierarchy()

    # Use t=0 amplitudes for hierarchy
    A0 = modal_spectrum.amplitudes[0, :]
    k_mag = modal_spectrum.k_magnitudes

    # Sort by amplitude
    order = np.argsort(A0)[::-1]
    primary_idx = order[0]
    secondary_idx = order[1: 1 + n_secondary]

    A_sorted = A0[order]
    hierarchy_ratio = A_sorted[0] / (A_sorted[1] + 1e-30)

    # Energy concentration: top 10% of modes
    n_top = max(1, len(A0) // 10)
    total_energy = np.sum(A0 ** 2)
    top_energy = np.sum(A_sorted[:n_top] ** 2)
    concentration = top_energy / (total_energy + 1e-30)

    # Inertial range: fit log(A) vs log(k) in a middle range
    # Exclude the top 3 modes and the bottom 10% by amplitude
    k_sorted = k_mag[order]
    valid = (k_sorted > 0) & (A_sorted > 1e-15)
    n_valid = valid.sum()

    inertial_exp = 0.0
    inertial_lo = 0.0
    inertial_hi = 0.0
    diss_cutoff = float(k_mag.max()) if k_mag.size > 0 else 0.0

    if n_valid > 5:
        log_k = np.log(k_sorted[valid])
        log_A = np.log(A_sorted[valid])
        # Use modes 3..N-2 for the fit
        fit_slice = slice(3, max(4, n_valid - 2))
        if log_k[fit_slice].size >= 2:
            coeffs = np.polyfit(log_k[fit_slice], log_A[fit_slice], 1)
            inertial_exp = -coeffs[0]  # A ~ k^{-alpha}
            inertial_lo = float(np.exp(log_k[fit_slice][0]))
            inertial_hi = float(np.exp(log_k[fit_slice][-1]))

        # Dissipative cutoff: where amplitude drops below 1% of primary
        threshold = A_sorted[0] * 0.01
        below = np.where(A_sorted < threshold)[0]
        if below.size > 0:
            diss_cutoff = float(k_sorted[below[0]])

    return ModalHierarchy(
        primary_k=int(modal_spectrum.k_values[primary_idx]),
        primary_amplitude=float(A0[primary_idx]),
        secondary_k=modal_spectrum.k_values[secondary_idx],
        inertial_range=(inertial_lo, inertial_hi),
        inertial_exponent=float(inertial_exp),
        dissipative_cutoff=diss_cutoff,
        energy_concentration=float(concentration),
        hierarchy_ratio=float(hierarchy_ratio),
    )


def modal_decay_rates(modal_spectrum: ModalSpectrum) -> np.ndarray:
    """Compute exponential decay rates for each mode.

    Fits log(A_k(t)) vs t for each mode to estimate sigma_k.

    Parameters
    ----------
    modal_spectrum : ModalSpectrum

    Returns
    -------
    np.ndarray
        Decay rates sigma_k, shape (n_k,).  Positive = decaying.
    """
    n_t, n_k = modal_spectrum.amplitudes.shape
    if n_t < 3:
        return np.zeros(n_k)

    rates = np.zeros(n_k)
    t = modal_spectrum.times

    for j in range(n_k):
        A_j = modal_spectrum.amplitudes[:, j]
        valid = A_j > 1e-30
        if valid.sum() < 3:
            continue
        log_A = np.log(A_j[valid])
        t_valid = t[valid]
        if t_valid[-1] - t_valid[0] < 1e-30:
            continue
        coeffs = np.polyfit(t_valid, log_A, 1)
        rates[j] = -coeffs[0]  # positive = decaying

    return rates
