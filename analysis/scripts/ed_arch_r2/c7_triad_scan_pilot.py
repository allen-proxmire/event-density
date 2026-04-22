"""
C7 Triad-Coupling Scan — AFM Thin-Film Pilot Frame
==================================================

Scope: one frame only. No amplitude-scaling fit.
Target observables:
  - A1, A2, A3 at k_s, 2k_s, 3k_s
  - phases phi1, phi3, and Dphi = phi3 - 3*phi1 (wrapped)
  - ratios A2/A1^2, A3/A1^3
  - noise floor estimate at each ring

Caveats:
  - 178 x 187 pseudo-heightmap from image brightness; no physical scale.
  - k_s is in pixel-inverse units.
  - Single frame -> no scaling law fit possible.
"""

from __future__ import annotations

import json
import os
import numpy as np


# ------------------------------------------------------------------ #
#  Utilities                                                          #
# ------------------------------------------------------------------ #

def planar_detrend(h):
    """Subtract a best-fit plane from h(x, y)."""
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


def radial_power_spectrum(Hhat, kx, ky, k_bins):
    """Average |Hhat|^2 in radial bins."""
    K = np.sqrt(kx[:, None] ** 2 + ky[None, :] ** 2)
    P = np.abs(Hhat) ** 2
    rps = np.zeros(len(k_bins) - 1)
    rps_counts = np.zeros(len(k_bins) - 1)
    for i in range(len(k_bins) - 1):
        mask = (K >= k_bins[i]) & (K < k_bins[i + 1])
        if mask.any():
            rps[i] = P[mask].mean()
            rps_counts[i] = mask.sum()
    centers = 0.5 * (k_bins[:-1] + k_bins[1:])
    return centers, rps, rps_counts


def ring_amplitude_and_phase(Hhat, kx, ky, k_target, dk):
    """
    At radius k_target with half-width dk, find the bin with the
    largest |Hhat|. Return the complex value at that bin (peak amplitude
    and phase in that direction), plus the ring-mean |Hhat| as an
    isotropic alternative, and the ring noise floor.
    """
    K = np.sqrt(kx[:, None] ** 2 + ky[None, :] ** 2)
    mask = (K >= k_target - dk) & (K < k_target + dk)
    if not mask.any():
        return {
            "n_bins_in_ring": 0,
            "peak_amp": 0.0,
            "peak_phase": 0.0,
            "peak_kx": 0.0,
            "peak_ky": 0.0,
            "ring_mean_amp": 0.0,
            "ring_noise_floor": 0.0,
        }
    amps = np.abs(Hhat[mask])
    phases = np.angle(Hhat[mask])
    peak_idx_in_ring = np.argmax(amps)

    # Recover the (i, j) of the peak in the full array
    idx_flat = np.flatnonzero(mask.ravel())
    peak_flat = idx_flat[peak_idx_in_ring]
    peak_i, peak_j = np.unravel_index(peak_flat, Hhat.shape)

    ring_mean = amps.mean()
    # Noise floor: median of the lower half of the ring, robust to the peak
    lower_half = np.sort(amps)[: max(1, len(amps) // 2)]
    ring_noise = np.median(lower_half)

    return {
        "n_bins_in_ring": int(mask.sum()),
        "peak_amp": float(amps[peak_idx_in_ring]),
        "peak_phase": float(phases[peak_idx_in_ring]),
        "peak_kx": float(kx[peak_i]),
        "peak_ky": float(ky[peak_j]),
        "ring_mean_amp": float(ring_mean),
        "ring_noise_floor": float(ring_noise),
    }


def wrap_to_pi(x):
    return (x + np.pi) % (2 * np.pi) - np.pi


# ------------------------------------------------------------------ #
#  Main                                                               #
# ------------------------------------------------------------------ #

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "thinfilm_pilot_h.npy")
    h = np.load(path)
    Nx, Ny = h.shape
    print(f"Loaded {path}")
    print(f"  shape = {h.shape}, range = [{h.min():.4f}, {h.max():.4f}], "
          f"mean = {h.mean():.4f}, std = {h.std():.4f}")

    # 1. Detrend (already pre-processed but redo to be sure of zero mean + no tilt)
    h_dt = planar_detrend(h)
    h_dt -= h_dt.mean()
    print(f"  after planar detrend: mean = {h_dt.mean():.2e}, std = {h_dt.std():.4f}")

    # 2. 2D Hann window
    W = hann_2d(Nx, Ny)
    h_w = h_dt * W

    # 3. 2D FFT; use fftshift for clean radial indexing around zero
    Hhat = np.fft.fftshift(np.fft.fft2(h_w))
    # normalise so amplitudes are in h-units
    Hhat_norm = Hhat / (Nx * Ny)

    # Wavenumber grids (pixel^-1, cycles-per-pixel * 2*pi convention)
    kx = 2 * np.pi * np.fft.fftshift(np.fft.fftfreq(Nx, d=1.0))
    ky = 2 * np.pi * np.fft.fftshift(np.fft.fftfreq(Ny, d=1.0))

    # 4. Radial power spectrum
    k_nyq = min(np.pi, np.pi)
    dk_bin = 2 * np.pi / max(Nx, Ny)   # one bin per FFT resolution
    k_bins = np.arange(0.0, k_nyq, dk_bin)
    centers, rps, counts = radial_power_spectrum(Hhat_norm, kx, ky, k_bins)

    # Identify dominant spinodal mode: peak of rps excluding low-k (first 2 bins)
    search_start = 2
    peak_bin = search_start + int(np.argmax(rps[search_start:]))
    k_s = float(centers[peak_bin])
    print(f"  radial power peak at bin {peak_bin} -> k_s = {k_s:.4f} rad/px  "
          f"(lambda_s = {2*np.pi/k_s:.2f} px)")

    # 5. Sampling check: require dx <= lambda_s / 6 (here dx = 1 px)
    oversampling_ratio = (2 * np.pi / k_s) / 1.0
    print(f"  oversampling lambda_s / dx = {oversampling_ratio:.2f}  (need >= 6 for 3k_s clean)")

    # 6. Extract at k_s, 2 k_s, 3 k_s with half-width dk = dk_bin
    dk = dk_bin
    r1 = ring_amplitude_and_phase(Hhat_norm, kx, ky, k_s, dk)
    r2 = ring_amplitude_and_phase(Hhat_norm, kx, ky, 2 * k_s, dk)
    r3 = ring_amplitude_and_phase(Hhat_norm, kx, ky, 3 * k_s, dk)

    # Factor of 2 accounts for cos-mode amplitude from one-sided FFT bin.
    A1 = 2 * r1["peak_amp"]
    A2 = 2 * r2["peak_amp"]
    A3 = 2 * r3["peak_amp"]
    phi1 = r1["peak_phase"]
    phi3 = r3["peak_phase"]

    # Noise floors (ring median, doubled consistently with A_k convention)
    N1 = 2 * r1["ring_noise_floor"]
    N2 = 2 * r2["ring_noise_floor"]
    N3 = 2 * r3["ring_noise_floor"]

    Dphi = wrap_to_pi(phi3 - 3 * phi1)
    K_sim = A3 / A1 ** 3 if A1 > 0 else 0.0
    K2_sim = A2 / A1 ** 2 if A1 > 0 else 0.0
    A2_over_A3 = A2 / A3 if A3 > 0 else float("inf")

    # SNR
    snr1 = A1 / N1 if N1 > 0 else float("inf")
    snr2 = A2 / N2 if N2 > 0 else float("inf")
    snr3 = A3 / N3 if N3 > 0 else float("inf")

    # 7. Output
    print()
    print("=" * 72)
    print("C7 TRIAD-COUPLING SCAN — AFM PILOT FRAME")
    print("=" * 72)
    print()
    print(f"{'quantity':<28} {'value':>12}  {'notes':<28}")
    print(f"{'-'*28} {'-'*12}  {'-'*28}")
    print(f"{'k_s (rad/px)':<28} {k_s:>12.4f}  lambda_s = {2*np.pi/k_s:.2f} px")
    print(f"{'2 k_s':<28} {2*k_s:>12.4f}  lambda = {2*np.pi/(2*k_s):.2f} px")
    print(f"{'3 k_s':<28} {3*k_s:>12.4f}  lambda = {2*np.pi/(3*k_s):.2f} px")
    print()
    print(f"{'A1':<28} {A1:>12.4e}  (k_s peak)")
    print(f"{'A2':<28} {A2:>12.4e}  (2 k_s peak)")
    print(f"{'A3':<28} {A3:>12.4e}  (3 k_s peak)")
    print()
    print(f"{'ring noise floor N1':<28} {N1:>12.4e}  SNR1 = {snr1:.2f}")
    print(f"{'ring noise floor N2':<28} {N2:>12.4e}  SNR2 = {snr2:.2f}")
    print(f"{'ring noise floor N3':<28} {N3:>12.4e}  SNR3 = {snr3:.2f}")
    print()
    print(f"{'phi1 (rad)':<28} {phi1:>12.4f}")
    print(f"{'phi3 (rad)':<28} {phi3:>12.4f}")
    print(f"{'Delta phi (wrapped)':<28} {Dphi:>12.4f}  "
          f"(pi = {np.pi:.4f}, 0 = 0.0000)")
    print(f"{'|Delta phi|':<28} {abs(Dphi):>12.4f}  "
          f"distance from +/-pi: {min(abs(Dphi-np.pi), abs(Dphi+np.pi)):.4f}")
    print()
    print(f"{'K_sim = A3 / A1^3':<28} {K_sim:>12.4e}  sim reference K = 1.48e-2")
    print(f"{'K2_sim = A2 / A1^2':<28} {K2_sim:>12.4e}  sim reference K2 = 2.79e-1")
    print(f"{'A2 / A3':<28} {A2_over_A3:>12.4f}  "
          f"(ED sim has A2 ~ 200 * A3 at A1=0.1)")
    print()
    print(f"{'peak direction k_s':<28} ({r1['peak_kx']:.3f}, {r1['peak_ky']:.3f})")
    print(f"{'peak direction 3 k_s':<28} ({r3['peak_kx']:.3f}, {r3['peak_ky']:.3f})")
    print()
    print("=" * 72)
    print("INTERPRETATION")
    print("=" * 72)

    # a) is A3 above noise?
    a3_above_noise = snr3 >= 3.0
    print(f"A3 above 3x noise floor? {a3_above_noise}  (SNR3 = {snr3:.2f})")

    # b) phase lock check
    phase_lock_pi = min(abs(Dphi - np.pi), abs(Dphi + np.pi)) < np.pi / 8
    phase_lock_zero = abs(Dphi) < np.pi / 8
    if phase_lock_pi:
        phase_status = "PHASE-LOCKED AT +/- pi (canonical ED triad signature)"
    elif phase_lock_zero:
        phase_status = "PHASE-LOCKED AT 0 (non-canonical — suggests non-ED nonlinearity)"
    else:
        phase_status = "NOT phase-locked (|Dphi - pi| > pi/8 and |Dphi| > pi/8)"
    print(f"Phase lock status: {phase_status}")

    # c) A2/A3 ordering
    if A2 > A3:
        ordering = f"A2 > A3 (clean-regime ED signature; ratio {A2_over_A3:.2f})"
    else:
        ordering = f"A2 < A3 (non-canonical ordering)"
    print(f"Mode ordering: {ordering}")

    # d) Sampling check for k=3 validity
    sampling_ok = oversampling_ratio >= 6.0
    if not sampling_ok:
        print(f"WARNING: lambda_s / dx = {oversampling_ratio:.2f} < 6; "
              f"3 k_s is at lambda = {2*np.pi/(3*k_s):.2f} px, marginal for clean resolution.")
    else:
        print(f"Sampling OK: lambda_s / dx = {oversampling_ratio:.2f} >= 6.")

    # Overall verdict
    print()
    if not a3_above_noise:
        verdict = "UNDECIDABLE (A3 below noise)"
    elif phase_lock_pi and A2 > A3 and sampling_ok:
        verdict = "WEAK POSITIVE (phase-lock + ordering + SNR; one frame only, no scaling fit)"
    elif phase_lock_pi:
        verdict = "SUGGESTIVE (phase-lock at +/- pi but other criteria partial)"
    elif a3_above_noise and abs(Dphi) > np.pi / 2:
        verdict = "AMBIGUOUS (A3 present but phase not near +/- pi)"
    else:
        verdict = "NEGATIVE (no clean triad signature)"
    print(f"One-frame verdict: {verdict}")
    print()
    print("(Single-frame scan; no A1^2 scaling possible. Multi-frame acquisition")
    print(" per experiements/AFM-Dewetting-ED-SC_InProcess/ required for a PASS.)")

    # JSON output
    out = {
        "dataset": "thinfilm_pilot_h.npy",
        "shape": [int(Nx), int(Ny)],
        "k_s_rad_per_px": k_s,
        "lambda_s_px": float(2 * np.pi / k_s),
        "oversampling_ratio": float(oversampling_ratio),
        "A1": float(A1), "A2": float(A2), "A3": float(A3),
        "N1": float(N1), "N2": float(N2), "N3": float(N3),
        "SNR1": float(snr1), "SNR2": float(snr2), "SNR3": float(snr3),
        "phi1": float(phi1), "phi3": float(phi3),
        "Delta_phi_wrapped": float(Dphi),
        "distance_from_pi": float(min(abs(Dphi-np.pi), abs(Dphi+np.pi))),
        "K_sim_single_frame": float(K_sim),
        "K2_sim_single_frame": float(K2_sim),
        "A2_over_A3": float(A2_over_A3),
        "phase_lock_at_pi": bool(phase_lock_pi),
        "phase_lock_at_zero": bool(phase_lock_zero),
        "A3_above_3x_noise": bool(a3_above_noise),
        "sampling_ok_for_3k": bool(sampling_ok),
        "verdict": verdict,
        "sim_reference_K": 0.0148,
        "sim_reference_K2": 0.279,
        "sim_reference_Dphi": float(np.pi),
    }

    out_path = os.path.join(here, "c7_triad_scan_pilot_results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
