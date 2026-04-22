"""
C7 Triad-Coupling — Collinearity Check on AFM Pilot Frame.

Builds on c7_triad_scan_pilot.py. The ring-peak scan found:
  k_s peak at (-0.106, 0.134)  |k|=0.1848
  3 k_s peak at (-0.141, 0.538)  |k|=0.5555
but 3 * (-0.106, 0.134) = (-0.318, 0.402), which is NOT the direction
of the 3 k_s ring peak. A genuine triad should source 3 k_s along the
3 * k_s_vec direction.

This script extracts A and phi at the EXACT collinear direction 3*k_s_vec
(and likewise 2*k_s_vec for A2), using bilinear-interpolated FFT values.
"""

from __future__ import annotations

import json
import os
import numpy as np


def planar_detrend(h):
    Nx, Ny = h.shape
    x = np.arange(Nx)[:, None] * np.ones((1, Ny))
    y = np.ones((Nx, 1)) * np.arange(Ny)[None, :]
    A = np.column_stack([x.ravel(), y.ravel(), np.ones(Nx * Ny)])
    coeffs, *_ = np.linalg.lstsq(A, h.ravel(), rcond=None)
    plane = (A @ coeffs).reshape(Nx, Ny)
    return h - plane


def hann_2d(Nx, Ny):
    wx = 0.5 - 0.5 * np.cos(2 * np.pi * np.arange(Nx) / (Nx - 1))
    wy = 0.5 - 0.5 * np.cos(2 * np.pi * np.arange(Ny) / (Ny - 1))
    return np.outer(wx, wy)


def fft_value_at(Hhat, kx, ky, k_target_x, k_target_y):
    """Return complex FFT value at the nearest bin to (k_target_x, k_target_y)."""
    i = int(np.argmin(np.abs(kx - k_target_x)))
    j = int(np.argmin(np.abs(ky - k_target_y)))
    return Hhat[i, j], kx[i], ky[j]


def wrap_to_pi(x):
    return (x + np.pi) % (2 * np.pi) - np.pi


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    h = np.load(os.path.join(here, "thinfilm_pilot_h.npy"))
    Nx, Ny = h.shape

    h_dt = planar_detrend(h)
    h_dt -= h_dt.mean()
    W = hann_2d(Nx, Ny)
    h_w = h_dt * W

    Hhat = np.fft.fftshift(np.fft.fft2(h_w)) / (Nx * Ny)
    kx = 2 * np.pi * np.fft.fftshift(np.fft.fftfreq(Nx, d=1.0))
    ky = 2 * np.pi * np.fft.fftshift(np.fft.fftfreq(Ny, d=1.0))

    # Dominant k_s from the ring scan
    # Re-find it here: magnitude of peak outside low-k region
    K = np.sqrt(kx[:, None] ** 2 + ky[None, :] ** 2)
    amp = np.abs(Hhat)
    # Mask out low-k region (DC + immediate neighbors)
    low_k_mask = K < 0.05
    amp_search = amp.copy()
    amp_search[low_k_mask] = 0.0
    peak_flat = int(np.argmax(amp_search))
    pi, pj = np.unravel_index(peak_flat, amp.shape)
    ks_x, ks_y = float(kx[pi]), float(ky[pj])
    ks_mag = float(np.hypot(ks_x, ks_y))

    print(f"Dominant k_s direction:  kx={ks_x:+.4f}  ky={ks_y:+.4f}  |k|={ks_mag:.4f}")
    print(f"Target 2 k_s direction:  kx={2*ks_x:+.4f}  ky={2*ks_y:+.4f}  |k|={2*ks_mag:.4f}")
    print(f"Target 3 k_s direction:  kx={3*ks_x:+.4f}  ky={3*ks_y:+.4f}  |k|={3*ks_mag:.4f}")
    print()

    # Extract at collinear 2 k_s and 3 k_s
    H1, k1x, k1y = fft_value_at(Hhat, kx, ky, ks_x, ks_y)
    H2, k2x, k2y = fft_value_at(Hhat, kx, ky, 2 * ks_x, 2 * ks_y)
    H3, k3x, k3y = fft_value_at(Hhat, kx, ky, 3 * ks_x, 3 * ks_y)

    A1 = 2 * np.abs(H1)
    A2_col = 2 * np.abs(H2)
    A3_col = 2 * np.abs(H3)
    phi1 = float(np.angle(H1))
    phi2_col = float(np.angle(H2))
    phi3_col = float(np.angle(H3))

    Dphi13 = wrap_to_pi(phi3_col - 3 * phi1)
    Dphi12 = wrap_to_pi(phi2_col - 2 * phi1)

    # Compare to the ring peaks
    # Ring peak at 3 k_s (ignoring direction):
    dk = 2 * np.pi / max(Nx, Ny)
    ring_mask = (K >= 3 * ks_mag - dk) & (K < 3 * ks_mag + dk)
    if ring_mask.any():
        ring_vals = Hhat[ring_mask]
        ring_amps = np.abs(ring_vals)
        ring_peak_amp = 2 * float(np.max(ring_amps))
        ring_mean = 2 * float(np.mean(ring_amps))
        ring_median = 2 * float(np.median(ring_amps))
    else:
        ring_peak_amp = ring_mean = ring_median = 0.0

    # Background / noise at 3 k_s: mean of ring excluding the max
    if ring_mask.any() and len(ring_vals) > 1:
        sorted_amps = np.sort(ring_amps)
        noise_floor = 2 * float(np.median(sorted_amps[: max(1, len(sorted_amps) // 2)]))
    else:
        noise_floor = 0.0

    snr3_col = A3_col / noise_floor if noise_floor > 0 else float("inf")

    print("--- COLLINEAR EXTRACTION (exact 3*k_s_vec direction) ---")
    print(f"A1                    = {A1:.4e}   phi1 = {phi1:+.4f}")
    print(f"A2 (collinear)        = {A2_col:.4e}   phi2 = {phi2_col:+.4f}")
    print(f"A3 (collinear)        = {A3_col:.4e}   phi3 = {phi3_col:+.4f}")
    print(f"Delta phi (2:1 triad) = {Dphi12:+.4f}  (ED expects 0 mod 2pi)")
    print(f"Delta phi (3:1 triad) = {Dphi13:+.4f}  (ED expects +/- pi)")
    print(f"                        distance from +/- pi: {min(abs(Dphi13-np.pi), abs(Dphi13+np.pi)):.4f}")
    print()
    print("--- RING (azimuth-agnostic) vs COLLINEAR ---")
    print(f"3 k_s ring-peak |A|   = {ring_peak_amp:.4e}")
    print(f"3 k_s ring-mean |A|   = {ring_mean:.4e}")
    print(f"3 k_s ring-median |A| = {ring_median:.4e}  (noise floor proxy)")
    print(f"3 k_s collinear |A|   = {A3_col:.4e}   SNR_col = {snr3_col:.2f}")
    print(f"ratio collinear/ring_peak  = {A3_col/ring_peak_amp if ring_peak_amp>0 else 0:.4f}")
    print(f"ratio collinear/noise      = {snr3_col:.4f}")
    print()

    collinear_is_peak = A3_col >= 0.7 * ring_peak_amp
    collinear_above_noise = snr3_col >= 3.0

    print("--- TRIAD-GENUINENESS DIAGNOSIS ---")
    if collinear_is_peak:
        print("The 3 k_s ring peak IS the collinear 3*k_s direction.")
        print("  -> consistent with triad sourcing from k_s")
    else:
        print("The 3 k_s ring peak is NOT at the collinear 3*k_s direction.")
        print("  -> the ring peak is an INDEPENDENT mode in that ring, not a k_s triad.")

    if collinear_above_noise:
        print(f"Collinear A3 is above 3x noise (SNR = {snr3_col:.2f}).")
    else:
        print(f"Collinear A3 is NOT above 3x noise (SNR = {snr3_col:.2f}).")
        print("  -> no detectable triad response at 3*k_s direction in this frame.")

    print()
    # Corrected verdict
    if collinear_above_noise and collinear_is_peak \
            and min(abs(Dphi13-np.pi), abs(Dphi13+np.pi)) < np.pi/8:
        verdict = "WEAK POSITIVE (collinear, phase-locked, above noise)"
    elif collinear_above_noise and min(abs(Dphi13-np.pi), abs(Dphi13+np.pi)) < np.pi/8:
        verdict = "PARTIAL (phase-lock at collinear bin but ring has stronger off-axis mode)"
    elif not collinear_above_noise:
        verdict = "NEGATIVE (no collinear A3 above noise; earlier ring-peak SNR was picking up an independent mode)"
    else:
        verdict = "AMBIGUOUS (collinear present but phase not locked)"

    print(f"CORRECTED ONE-FRAME VERDICT: {verdict}")

    out = {
        "dataset": "thinfilm_pilot_h.npy",
        "k_s_vec": [ks_x, ks_y],
        "k_s_mag": ks_mag,
        "collinear_A1": float(A1),
        "collinear_A2": float(A2_col),
        "collinear_A3": float(A3_col),
        "collinear_phi1": phi1,
        "collinear_phi2": phi2_col,
        "collinear_phi3": phi3_col,
        "Delta_phi_3_1": float(Dphi13),
        "Delta_phi_2_1": float(Dphi12),
        "distance_Dphi13_from_pi": float(min(abs(Dphi13-np.pi), abs(Dphi13+np.pi))),
        "3k_ring_peak_amp": ring_peak_amp,
        "3k_ring_mean_amp": ring_mean,
        "3k_ring_median_amp": ring_median,
        "collinear_over_ring_peak": float(A3_col/ring_peak_amp) if ring_peak_amp > 0 else 0.0,
        "collinear_SNR3": float(snr3_col),
        "collinear_is_ring_peak": bool(collinear_is_peak),
        "collinear_above_3x_noise": bool(collinear_above_noise),
        "corrected_verdict": verdict,
    }
    with open(os.path.join(here, "c7_triad_collinear_results.json"), "w") as f:
        json.dump(out, f, indent=2)
    print()
    print("Wrote c7_triad_collinear_results.json")


if __name__ == "__main__":
    main()
