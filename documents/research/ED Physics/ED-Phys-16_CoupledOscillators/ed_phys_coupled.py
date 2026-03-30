"""
ED-Phys-16: Coupled Oscillators & Mode Interactions
====================================================

Explores nonlinear interactions between oscillatory participation modes
in the fully symmetric, conservative oscillator layer (P_SY2 + hyperbolic time).

Builds on:
  - ED-Phys-15: P_SY2 canonical oscillator penalty
  - ED-Phys-14: oscillator layer
  - ED-Phys-13: hyperbolic participation

Canonical sources: ED-5, ED-12, ED-12.5
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from pathlib import Path

import numpy as np


# ---------------------------------------------------------------------------
# Configuration (from ED-Phys-15)
# ---------------------------------------------------------------------------
@dataclass
class EDParams:
    alpha: float = 0.1
    gamma_exp: float = 0.5
    M_0: float = 1.0
    rho_max: float = 100.0
    n_mob: int = 2
    dx: float = 1.0
    n_steps: int = 50000
    dimensions: int = 1
    grid_size: int = 512
    boundary: str = "periodic"
    eps: float = 1e-10
    cfl_safety: float = 0.4
    seed: int = 42


@dataclass
class OscParams:
    tau: float = 100.0
    zeta: float = 0.5
    rho_star: float = 50.0
    rho_0: float = 0.5


# ---------------------------------------------------------------------------
# Operators (identical to ED-Phys-15)
# ---------------------------------------------------------------------------
def _pad(rho, boundary):
    if rho.ndim == 1:
        if boundary == "periodic":
            return np.concatenate(([rho[-1]], rho, [rho[0]]))
        return np.concatenate(([rho[0]], rho, [rho[-1]]))
    else:
        if boundary == "periodic":
            return np.pad(rho, 1, mode="wrap")
        return np.pad(rho, 1, mode="edge")


def discrete_laplacian(rho, dx, boundary):
    dx2 = dx * dx
    p = _pad(rho, boundary)
    if rho.ndim == 1:
        return (p[2:] - 2.0 * p[1:-1] + p[:-2]) / dx2
    return (p[2:, 1:-1] + p[:-2, 1:-1] + p[1:-1, 2:] + p[1:-1, :-2]
            - 4.0 * p[1:-1, 1:-1]) / dx2


def discrete_grad_squared(rho, dx, boundary):
    p = _pad(rho, boundary)
    two_dx = 2.0 * dx
    if rho.ndim == 1:
        gx = (p[2:] - p[:-2]) / two_dx
        return gx * gx
    gx = (p[2:, 1:-1] - p[:-2, 1:-1]) / two_dx
    gy = (p[1:-1, 2:] - p[1:-1, :-2]) / two_dx
    return gx * gx + gy * gy


def mobility(rho, M_0, rho_max, n_mob):
    ratio = np.clip(1.0 - rho / rho_max, 0.0, None)
    M = M_0 * ratio ** n_mob
    M_prime = -M_0 * (n_mob / rho_max) * ratio ** max(n_mob - 1, 0)
    return M, M_prime


# ---------------------------------------------------------------------------
# Penalty (P_SY2 from ED-Phys-15)
# ---------------------------------------------------------------------------
def penalty_sy2(rho, alpha, gamma, rho_star, rho_0, eps=1e-10):
    rho_safe = np.maximum(rho, eps)
    delta = rho_safe - rho_star
    return alpha * gamma * delta / np.sqrt(delta * delta + rho_0 * rho_0)


def potential_sy2(rho, alpha, gamma, rho_star, rho_0):
    delta = rho - rho_star
    return alpha * gamma * np.sqrt(delta * delta + rho_0 * rho_0)


# ---------------------------------------------------------------------------
# Linear theory
# ---------------------------------------------------------------------------
def omega_0(k, params: EDParams, osc: OscParams):
    P_prime = params.alpha * params.gamma_exp / osc.rho_0
    M_star = params.M_0 * (1.0 - osc.rho_star / params.rho_max) ** params.n_mob
    K_eff = M_star * k ** 2 + P_prime
    return np.sqrt(K_eff / osc.tau)


def K_eff_func(k, params: EDParams, osc: OscParams):
    P_prime = params.alpha * params.gamma_exp / osc.rho_0
    M_star = params.M_0 * (1.0 - osc.rho_star / params.rho_max) ** params.n_mob
    return M_star * k ** 2 + P_prime


# ---------------------------------------------------------------------------
# Timestep
# ---------------------------------------------------------------------------
def compute_timestep(params: EDParams, osc: OscParams):
    d = params.dimensions
    dx = params.dx
    eta_diff = params.cfl_safety * dx ** 2 / (2.0 * d * params.M_0)
    P_prime = params.alpha * params.gamma_exp / osc.rho_0
    k_max = np.pi / dx
    K_eff_max = params.M_0 * k_max ** 2 + P_prime
    c_max = np.sqrt(K_eff_max / osc.tau)
    eta_wave = params.cfl_safety * dx / max(c_max, 1e-10)
    eta_damp = 2.0 * osc.tau / max(osc.zeta, 1e-10)
    return min(eta_diff, eta_wave, eta_damp, 0.5)


# ---------------------------------------------------------------------------
# FFT-based mode diagnostics
# ---------------------------------------------------------------------------
def mode_amplitudes_1d(rho, rho_star):
    """Compute mode amplitudes from FFT of (rho - rho_star)."""
    delta = rho - rho_star
    N = len(delta)
    fft_coeffs = np.fft.rfft(delta) / N
    amps = 2.0 * np.abs(fft_coeffs)
    amps[0] /= 2.0  # DC component
    if N % 2 == 0:
        amps[-1] /= 2.0  # Nyquist
    return amps  # shape: (N//2 + 1,)


def mode_phases_1d(rho, rho_star):
    """Compute mode phases from FFT."""
    delta = rho - rho_star
    N = len(delta)
    fft_coeffs = np.fft.rfft(delta) / N
    return np.angle(fft_coeffs)


def mode_energies_1d(rho, v, params: EDParams, osc: OscParams):
    """Compute per-mode energy: E_k = (tau/2)|v_k|^2 + (1/2)*K_eff(k)*|delta_rho_k|^2."""
    N = params.grid_size
    delta = rho - osc.rho_star
    fft_rho = np.fft.rfft(delta) / N
    fft_v = np.fft.rfft(v) / N

    n_modes = len(fft_rho)
    k_vals = 2.0 * np.pi * np.arange(n_modes) / N
    K_eff = K_eff_func(k_vals, params, osc)

    E_pot = 0.5 * K_eff * np.abs(fft_rho) ** 2
    E_kin = 0.5 * osc.tau * np.abs(fft_v) ** 2

    # Scale: each mode except DC and Nyquist contributes twice (positive + negative k)
    scale = np.full(n_modes, 2.0)
    scale[0] = 1.0
    if N % 2 == 0:
        scale[-1] = 1.0

    return (E_pot + E_kin) * scale * N  # energy per unit length * N


def total_energy(rho, v, params: EDParams, osc: OscParams):
    """Total oscillator energy (real-space)."""
    rho_safe = np.maximum(rho, params.eps)
    grad_sq = discrete_grad_squared(rho_safe, params.dx, params.boundary)
    M_star = params.M_0 * (1.0 - osc.rho_star / params.rho_max) ** params.n_mob
    E_kin = 0.5 * osc.tau * float(np.mean(v ** 2))
    E_grad = 0.5 * M_star * float(np.mean(grad_sq))
    V = potential_sy2(rho, params.alpha, params.gamma_exp, osc.rho_star, osc.rho_0)
    E_pot = float(np.mean(V))
    return {"E_kin": E_kin, "E_grad": E_grad, "E_pot": E_pot,
            "E_total": E_kin + E_grad + E_pot}


def mode_amplitudes_2d(rho, rho_star):
    """Radially averaged power spectrum for 2D."""
    delta = rho - rho_star
    Nx = delta.shape[0]
    fft2 = np.fft.fft2(delta) / (Nx * Nx)
    power = np.abs(fft2) ** 2

    # Radial binning
    kx = np.fft.fftfreq(Nx) * Nx
    ky = np.fft.fftfreq(Nx) * Nx
    KX, KY = np.meshgrid(kx, ky)
    kr = np.sqrt(KX ** 2 + KY ** 2)

    max_k = Nx // 2
    bins = np.arange(0.5, max_k + 1.5, 1.0)
    radial_power = np.zeros(max_k + 1)
    for i in range(max_k + 1):
        mask = (kr >= bins[i] - 0.5) & (kr < bins[i] + 0.5)
        if np.any(mask):
            radial_power[i] = float(np.mean(power[mask]))
    return radial_power


# ---------------------------------------------------------------------------
# Simulator (from ED-Phys-15, extended with mode tracking)
# ---------------------------------------------------------------------------
def simulate(
    params: EDParams,
    osc: OscParams,
    initial_rho: np.ndarray,
    label: str = "",
    track_modes: list[int] | None = None,
    mode_diag_interval: int | None = None,
    snapshot_interval: int = 2000,
    initial_v: np.ndarray | None = None,
) -> dict:
    rho = initial_rho.astype(np.float64).copy()
    eta = compute_timestep(params, osc)
    v = initial_v.copy() if initial_v is not None else np.zeros_like(rho)

    diag_interval = max(1, params.n_steps // 4000)
    if mode_diag_interval is None:
        mode_diag_interval = max(1, params.n_steps // 2000)

    diagnostics = {
        "rho_mean": [], "rho_std": [], "rho_min": [], "rho_max": [],
        "v_rms": [], "E_total": [],
    }

    # Mode tracking
    mode_data = {}
    if track_modes and rho.ndim == 1:
        for n in track_modes:
            mode_data[n] = {"amplitude": [], "phase": [], "energy": []}
        mode_data["_total_energy"] = []
        mode_data["_steps"] = []

    snapshots = []
    snapshot_times = []
    t_start = time.time()
    blew_up = False
    positivity_clips = 0

    for t in range(params.n_steps):
        if t % 100 == 0:
            if np.any(np.isnan(rho)) or np.any(np.isinf(rho)):
                blew_up = True
                break
            if np.max(np.abs(rho)) > 1e12:
                blew_up = True
                break
            if np.any(np.isnan(v)) or np.any(np.isinf(v)):
                blew_up = True
                break

        # RHS
        rho_safe = np.maximum(rho, params.eps)
        lap = discrete_laplacian(rho_safe, params.dx, params.boundary)
        grad_sq = discrete_grad_squared(rho_safe, params.dx, params.boundary)
        M, M_prime = mobility(rho_safe, params.M_0, params.rho_max, params.n_mob)
        pen = penalty_sy2(rho_safe, params.alpha, params.gamma_exp,
                          osc.rho_star, osc.rho_0, params.eps)
        rhs = M * lap + M_prime * grad_sq - pen

        # Hyperbolic time step
        dv = (1.0 / osc.tau) * (rhs - osc.zeta * v)
        v_new = v + eta * dv
        rho_new = rho + eta * v_new

        below = rho_new < 0.0
        if np.any(below):
            positivity_clips += int(np.sum(below))
            rho_new = np.maximum(rho_new, 0.0)

        # Scalar diagnostics
        if t % diag_interval == 0 or t == params.n_steps - 1:
            diagnostics["rho_mean"].append(float(np.mean(rho_new)))
            diagnostics["rho_std"].append(float(np.std(rho_new)))
            diagnostics["rho_min"].append(float(np.min(rho_new)))
            diagnostics["rho_max"].append(float(np.max(rho_new)))
            diagnostics["v_rms"].append(float(np.sqrt(np.mean(v_new ** 2))))
            en = total_energy(rho_new, v_new, params, osc)
            diagnostics["E_total"].append(en["E_total"])

        # Mode diagnostics (1D only)
        if track_modes and rho.ndim == 1 and (
            t % mode_diag_interval == 0 or t == params.n_steps - 1
        ):
            amps = mode_amplitudes_1d(rho_new, osc.rho_star)
            phases = mode_phases_1d(rho_new, osc.rho_star)
            m_energies = mode_energies_1d(rho_new, v_new, params, osc)
            for n in track_modes:
                if n < len(amps):
                    mode_data[n]["amplitude"].append(float(amps[n]))
                    mode_data[n]["phase"].append(float(phases[n]))
                    mode_data[n]["energy"].append(float(m_energies[n]))
            mode_data["_total_energy"].append(float(np.sum(m_energies)))
            mode_data["_steps"].append(t)

        # Snapshots
        if t % snapshot_interval == 0 or t == params.n_steps - 1:
            snapshots.append(rho_new.copy())
            snapshot_times.append(t)

        rho = rho_new
        v = v_new

    elapsed = time.time() - t_start

    return {
        "label": label,
        "eta": eta,
        "n_steps": params.n_steps,
        "blew_up": blew_up,
        "steps_completed": t + 1 if blew_up else params.n_steps,
        "elapsed_s": round(elapsed, 3),
        "positivity_clips": positivity_clips,
        "diagnostics": diagnostics,
        "mode_data": mode_data,
        "snapshots": snapshots,
        "snapshot_times": snapshot_times,
        "final_rho": rho,
        "final_v": v,
    }


# ---------------------------------------------------------------------------
# Simulator for 2D (lighter diagnostics)
# ---------------------------------------------------------------------------
def simulate_2d(
    params: EDParams,
    osc: OscParams,
    initial_rho: np.ndarray,
    label: str = "",
    snapshot_interval: int = 2000,
    radial_spectrum_interval: int | None = None,
) -> dict:
    rho = initial_rho.astype(np.float64).copy()
    eta = compute_timestep(params, osc)
    v = np.zeros_like(rho)

    diag_interval = max(1, params.n_steps // 2000)
    if radial_spectrum_interval is None:
        radial_spectrum_interval = max(1, params.n_steps // 200)

    diagnostics = {
        "rho_mean": [], "rho_std": [], "E_total": [],
    }
    spectra = []
    spectra_steps = []

    snapshots = []
    snapshot_times = []
    t_start = time.time()
    blew_up = False
    positivity_clips = 0

    for t in range(params.n_steps):
        if t % 200 == 0:
            if np.any(np.isnan(rho)) or np.any(np.isinf(rho)):
                blew_up = True
                break
            if np.max(np.abs(rho)) > 1e12:
                blew_up = True
                break

        rho_safe = np.maximum(rho, params.eps)
        lap = discrete_laplacian(rho_safe, params.dx, params.boundary)
        grad_sq = discrete_grad_squared(rho_safe, params.dx, params.boundary)
        M, M_prime = mobility(rho_safe, params.M_0, params.rho_max, params.n_mob)
        pen = penalty_sy2(rho_safe, params.alpha, params.gamma_exp,
                          osc.rho_star, osc.rho_0, params.eps)
        rhs = M * lap + M_prime * grad_sq - pen

        dv = (1.0 / osc.tau) * (rhs - osc.zeta * v)
        v_new = v + eta * dv
        rho_new = rho + eta * v_new

        below = rho_new < 0.0
        if np.any(below):
            positivity_clips += int(np.sum(below))
            rho_new = np.maximum(rho_new, 0.0)

        if t % diag_interval == 0 or t == params.n_steps - 1:
            diagnostics["rho_mean"].append(float(np.mean(rho_new)))
            diagnostics["rho_std"].append(float(np.std(rho_new)))
            en = total_energy(rho_new, v_new, params, osc)
            diagnostics["E_total"].append(en["E_total"])

        if t % radial_spectrum_interval == 0 or t == params.n_steps - 1:
            spectra.append(mode_amplitudes_2d(rho_new, osc.rho_star).tolist())
            spectra_steps.append(t)

        if t % snapshot_interval == 0 or t == params.n_steps - 1:
            snapshots.append(rho_new.copy())
            snapshot_times.append(t)

        rho = rho_new
        v = v_new

    elapsed = time.time() - t_start

    return {
        "label": label,
        "eta": eta,
        "blew_up": blew_up,
        "steps_completed": t + 1 if blew_up else params.n_steps,
        "elapsed_s": round(elapsed, 3),
        "positivity_clips": positivity_clips,
        "diagnostics": diagnostics,
        "spectra": spectra,
        "spectra_steps": spectra_steps,
        "snapshots": snapshots,
        "snapshot_times": snapshot_times,
        "final_rho": rho,
        "final_v": v,
    }


# ---------------------------------------------------------------------------
# Analysis helpers
# ---------------------------------------------------------------------------
def measure_beating(amp_series, diag_steps, eta):
    """Detect beating envelope from amplitude time series."""
    arr = np.array(amp_series)
    if len(arr) < 30:
        return {"detected": False}

    # Find peaks of the amplitude envelope
    peaks = []
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            peaks.append(i)

    if len(peaks) < 3:
        return {"detected": False, "n_peaks": len(peaks)}

    # Find envelope peaks (peaks of peaks — beat maxima)
    peak_vals = arr[np.array(peaks)]
    beat_peaks = []
    for i in range(1, len(peak_vals) - 1):
        if peak_vals[i] > peak_vals[i - 1] and peak_vals[i] > peak_vals[i + 1]:
            beat_peaks.append(peaks[i])

    if len(beat_peaks) < 2:
        return {"detected": False, "n_peaks": len(peaks), "n_beat_peaks": len(beat_peaks)}

    # Beat period in diagnostic steps
    beat_spacings = np.diff(beat_peaks)
    T_beat_diag = float(np.mean(beat_spacings))
    # Convert to simulation steps
    mode_diag_interval_est = diag_steps[1] - diag_steps[0] if len(diag_steps) > 1 else 1
    T_beat_steps = T_beat_diag * mode_diag_interval_est

    return {
        "detected": True,
        "n_beat_peaks": len(beat_peaks),
        "T_beat_diag": T_beat_diag,
        "T_beat_steps": T_beat_steps,
        "T_beat_time": T_beat_steps * eta,
        "envelope_max": float(np.max(peak_vals)),
        "envelope_min": float(np.min(peak_vals)),
        "modulation_depth": float(
            (np.max(peak_vals) - np.min(peak_vals)) / max(np.max(peak_vals), 1e-15)
        ),
    }


def measure_energy_transfer(E_k1, E_k2):
    """Characterize energy exchange between two modes."""
    E1 = np.array(E_k1)
    E2 = np.array(E_k2)
    if len(E1) < 10 or len(E2) < 10:
        return {"detected": False}

    E_total = E1 + E2
    # Fractional energy in mode 1
    frac1 = E1 / np.maximum(E_total, 1e-30)

    # Check if fraction varies significantly
    frac1_std = float(np.std(frac1))
    frac1_range = float(np.max(frac1) - np.min(frac1))

    # Correlation between modes
    corr = float(np.corrcoef(E1, E2)[0, 1]) if len(E1) > 2 else 0.0

    return {
        "frac1_mean": float(np.mean(frac1)),
        "frac1_std": frac1_std,
        "frac1_range": frac1_range,
        "correlation": corr,
        "energy_exchange": frac1_range > 0.05,  # >5% exchange = significant
        "E1_initial": float(E1[0]),
        "E1_final": float(E1[-1]),
        "E2_initial": float(E2[0]),
        "E2_final": float(E2[-1]),
    }


def measure_spectral_evolution(mode_data, track_modes):
    """Characterize how the spectrum evolves."""
    # Check modes that weren't initially excited
    excited = set(track_modes)
    n_modes_in_data = set(int(k) for k in mode_data.keys() if isinstance(k, int) or (isinstance(k, str) and k.isdigit()))

    # Amplitude growth in non-excited modes
    growth = {}
    for n_key, mdata in mode_data.items():
        if isinstance(n_key, str) and n_key.startswith("_"):
            continue
        n = int(n_key)
        amps = np.array(mdata["amplitude"])
        if len(amps) < 2:
            continue
        growth[n] = {
            "initial": float(amps[0]),
            "final": float(amps[-1]),
            "max": float(np.max(amps)),
            "mean": float(np.mean(amps)),
            "initially_excited": n in excited,
        }

    return growth


# ---------------------------------------------------------------------------
# Initial condition constructors
# ---------------------------------------------------------------------------
def ic_two_mode(N, rho_star, eps1, n1, eps2, n2, phi1=0, phi2=0):
    x = np.arange(N, dtype=np.float64)
    return rho_star + eps1 * np.sin(2 * np.pi * n1 * x / N + phi1) + \
                      eps2 * np.sin(2 * np.pi * n2 * x / N + phi2)


def ic_three_mode(N, rho_star, epsilons, modes, phases=None):
    x = np.arange(N, dtype=np.float64)
    rho = np.full(N, rho_star, dtype=np.float64)
    if phases is None:
        phases = [0.0] * len(modes)
    for eps, n, phi in zip(epsilons, modes, phases):
        rho += eps * np.sin(2 * np.pi * n * x / N + phi)
    return rho


def ic_multi_mode_packet(N, rho_star, modes, eps, seed=42):
    rng = np.random.default_rng(seed)
    x = np.arange(N, dtype=np.float64)
    rho = np.full(N, rho_star, dtype=np.float64)
    phases = rng.uniform(0, 2 * np.pi, len(modes))
    for n, phi in zip(modes, phases):
        rho += eps * np.sin(2 * np.pi * n * x / N + phi)
    return rho, phases


def ic_2d_two_mode(Nx, rho_star, eps, nx, ny):
    """Two orthogonal modes: sin(kx*x) + sin(ky*y)."""
    x = np.arange(Nx, dtype=np.float64)
    y = np.arange(Nx, dtype=np.float64)
    X, Y = np.meshgrid(x, y)
    return rho_star + eps * np.sin(2 * np.pi * nx * X / Nx) + \
                      eps * np.sin(2 * np.pi * ny * Y / Nx)


def ic_2d_radial_two_mode(Nx, rho_star, eps, sigma1, sigma2):
    """Two radial modes with different length scales."""
    cx, cy = Nx // 2, Nx // 2
    y, x = np.mgrid[0:Nx, 0:Nx]
    r2 = (x - cx) ** 2 + (y - cy) ** 2
    return rho_star + eps * np.exp(-r2 / (2 * sigma1 ** 2)) + \
                      0.5 * eps * np.exp(-r2 / (2 * sigma2 ** 2))


# ---------------------------------------------------------------------------
# JSON helper
# ---------------------------------------------------------------------------
def _json_safe(obj):
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.floating,)):
        return float(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, (np.bool_,)):
        return bool(obj)
    return str(obj)


def _compact_summary(res):
    d = res["diagnostics"]
    return {
        "label": res["label"],
        "blew_up": res["blew_up"],
        "elapsed_s": res["elapsed_s"],
        "positivity_clips": res["positivity_clips"],
        "rho_mean_final": d["rho_mean"][-1] if d["rho_mean"] else None,
        "rho_std_final": d["rho_std"][-1] if d["rho_std"] else None,
        "E_total_initial": d["E_total"][0] if d["E_total"] else None,
        "E_total_final": d["E_total"][-1] if d["E_total"] else None,
    }


# ===================================================================
# EXPERIMENTS
# ===================================================================
def run_all_experiments(results_dir: str) -> dict:
    os.makedirs(results_dir, exist_ok=True)
    all_results = {}

    N = 512
    params = EDParams(grid_size=N, n_steps=50000, dimensions=1)
    osc = OscParams(tau=100, zeta=0.5, rho_star=50, rho_0=0.5)
    eta = compute_timestep(params, osc)

    # Precompute frequencies for reference
    print("=" * 70)
    print("ED-Phys-16: Coupled Oscillators & Mode Interactions")
    print(f"eta = {eta:.4f}, tau={osc.tau}, zeta={osc.zeta}")
    print("=" * 70)
    print("\nMode frequencies (linear theory):")
    ref_modes = [4, 8, 16, 24, 32, 48, 64]
    for n in ref_modes:
        k = 2 * np.pi * n / N
        w = omega_0(k, params, osc)
        K = K_eff_func(k, params, osc)
        Q = np.sqrt(osc.tau * K) / osc.zeta
        T_steps = 2 * np.pi / w / eta
        print(f"  n={n:3d}: k={k:.4f}, omega={w:.5f}, K_eff={K:.4f}, "
              f"Q={Q:.2f}, T={T_steps:.0f} steps")
    print()

    # ===================================================================
    # EXP 1: TWO-MODE BEATING TEST
    # ===================================================================
    print("=" * 70)
    print("EXP 1: Two-Mode Beating")
    print("=" * 70)
    exp1 = {}

    beating_pairs = [
        ("close_32_48", 32, 48, 5.0, 5.0),
        ("close_24_40", 24, 40, 5.0, 5.0),
        ("very_close_30_34", 30, 34, 5.0, 5.0),
    ]

    for pair_name, n1, n2, e1, e2 in beating_pairs:
        k1, k2 = 2 * np.pi * n1 / N, 2 * np.pi * n2 / N
        w1, w2 = omega_0(k1, params, osc), omega_0(k2, params, osc)
        dw = abs(w1 - w2)
        T_beat_pred = 2 * np.pi / dw / eta if dw > 0 else float("inf")

        rho0 = ic_two_mode(N, 50.0, e1, n1, e2, n2)
        # Track the two excited modes plus their sum/difference and neighbors
        track = sorted(set([n1, n2, abs(n1 - n2), n1 + n2,
                            n1 - 1, n1 + 1, n2 - 1, n2 + 1, 0]))
        track = [m for m in track if 0 <= m <= N // 2]

        res = simulate(params, osc, rho0, label=pair_name, track_modes=track,
                       mode_diag_interval=25)

        # Analyze beating at a point
        beat_info = {}
        for m in [n1, n2]:
            if m in res["mode_data"] and res["mode_data"][m]["amplitude"]:
                bi = measure_beating(
                    res["mode_data"][m]["amplitude"],
                    res["mode_data"]["_steps"],
                    eta,
                )
                beat_info[m] = bi

        # Energy transfer between modes
        if n1 in res["mode_data"] and n2 in res["mode_data"]:
            et = measure_energy_transfer(
                res["mode_data"][n1]["energy"],
                res["mode_data"][n2]["energy"],
            )
        else:
            et = {}

        # Spectral growth in non-excited modes
        spec_ev = measure_spectral_evolution(res["mode_data"], [n1, n2])

        exp1[pair_name] = {
            **_compact_summary(res),
            "n1": n1, "n2": n2,
            "omega1": w1, "omega2": w2,
            "delta_omega": dw,
            "T_beat_predicted_steps": T_beat_pred,
            "beating": beat_info,
            "energy_transfer": et,
            "spectral_evolution": spec_ev,
            "mode_data": {k: v for k, v in res["mode_data"].items()
                          if not isinstance(k, str) or not k.startswith("_")},
        }
        beat_n1 = beat_info.get(n1, {})
        print(f"  {pair_name}: T_beat_pred={T_beat_pred:.0f}, "
              f"beat_detected={beat_n1.get('detected', '-')}, "
              f"T_beat_meas={beat_n1.get('T_beat_steps', '-')}, "
              f"energy_exchange={et.get('energy_exchange', '-')}, "
              f"clips={res['positivity_clips']}")

    all_results["exp1_beating"] = exp1

    # ===================================================================
    # EXP 2: ENERGY TRANSFER TEST (widely separated modes)
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXP 2: Energy Transfer (Widely Separated Modes)")
    print("=" * 70)
    exp2 = {}

    transfer_pairs = [
        ("n4_n64", 4, 64),
        ("n8_n48", 8, 48),
        ("n16_n64", 16, 64),
    ]

    for pair_name, n1, n2 in transfer_pairs:
        # Case A: all energy in mode 1
        rho_a = ic_two_mode(N, 50.0, 5.0, n1, 0.0, n2)
        track = sorted(set([n1, n2, abs(n1 - n2), n1 + n2, 2 * n1, 2 * n2, 0]))
        track = [m for m in track if 0 < m <= N // 2]

        res_a = simulate(params, osc, rho_a, label=f"{pair_name}_only_n{n1}",
                         track_modes=track, mode_diag_interval=25)

        # Case B: energy split equally
        rho_b = ic_two_mode(N, 50.0, 5.0, n1, 5.0, n2)
        res_b = simulate(params, osc, rho_b, label=f"{pair_name}_both",
                         track_modes=track, mode_diag_interval=25)

        for case_label, res in [("only_n1", res_a), ("both", res_b)]:
            key = f"{pair_name}_{case_label}"
            et = measure_energy_transfer(
                res["mode_data"][n1]["energy"] if n1 in res["mode_data"] else [],
                res["mode_data"][n2]["energy"] if n2 in res["mode_data"] else [],
            )
            spec_ev = measure_spectral_evolution(res["mode_data"], [n1, n2])

            # Check sum/difference mode growth (nonlinear signature)
            sum_mode = n1 + n2
            diff_mode = abs(n1 - n2)
            sum_growth = spec_ev.get(sum_mode, {}).get("max", 0)
            diff_growth = spec_ev.get(diff_mode, {}).get("max", 0)

            exp2[key] = {
                **_compact_summary(res),
                "n1": n1, "n2": n2, "case": case_label,
                "energy_transfer": et,
                "sum_mode_growth": sum_growth,
                "diff_mode_growth": diff_growth,
                "spectral_evolution": spec_ev,
            }
            print(f"  {key}: E_exchange={et.get('energy_exchange', '-')}, "
                  f"sum_mode({sum_mode})={sum_growth:.6f}, "
                  f"diff_mode({diff_mode})={diff_growth:.6f}, "
                  f"clips={res['positivity_clips']}")

    all_results["exp2_transfer"] = exp2

    # ===================================================================
    # EXP 3: PHASE INTERACTION TEST
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXP 3: Phase Interaction")
    print("=" * 70)
    exp3 = {}

    # Same modes, different phase offsets
    phase_configs = [
        ("in_phase", 32, 48, 0.0, 0.0),
        ("quarter_phase", 32, 48, 0.0, np.pi / 2),
        ("anti_phase", 32, 48, 0.0, np.pi),
    ]

    for cfg_name, n1, n2, phi1, phi2 in phase_configs:
        rho0 = ic_two_mode(N, 50.0, 5.0, n1, 5.0, n2, phi1, phi2)
        track = sorted(set([n1, n2, abs(n1 - n2), n1 + n2, 0]))
        track = [m for m in track if 0 <= m <= N // 2]

        res = simulate(params, osc, rho0, label=cfg_name,
                       track_modes=track, mode_diag_interval=25)

        # Track phase difference evolution
        if n1 in res["mode_data"] and n2 in res["mode_data"]:
            ph1 = np.array(res["mode_data"][n1]["phase"])
            ph2 = np.array(res["mode_data"][n2]["phase"])
            delta_phase = np.mod(ph1 - ph2 + np.pi, 2 * np.pi) - np.pi
            phase_drift = float(np.std(delta_phase))
            phase_mean = float(np.mean(delta_phase))
        else:
            delta_phase = []
            phase_drift = 0
            phase_mean = 0

        exp3[cfg_name] = {
            **_compact_summary(res),
            "phi1": phi1, "phi2": phi2,
            "phase_drift_std": phase_drift,
            "phase_mean": phase_mean,
            "initial_phase_diff": phi2 - phi1,
        }
        print(f"  {cfg_name}: phase_drift_std={phase_drift:.4f}, "
              f"phase_mean={phase_mean:.4f}, clips={res['positivity_clips']}")

    all_results["exp3_phase"] = exp3

    # ===================================================================
    # EXP 4: TRIAD INTERACTION (k1 + k2 = k3)
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXP 4: Triad Resonance")
    print("=" * 70)
    exp4 = {}

    triads = [
        ("triad_8_24_32", [8, 24, 32]),      # 8 + 24 = 32
        ("triad_16_32_48", [16, 32, 48]),     # 16 + 32 = 48
        ("triad_4_12_16", [4, 12, 16]),       # 4 + 12 = 16
    ]

    for triad_name, modes in triads:
        rho0 = ic_three_mode(N, 50.0, [5.0] * len(modes), modes)
        # Track excited modes plus their interactions
        extra = []
        for i in range(len(modes)):
            for j in range(i + 1, len(modes)):
                extra.append(abs(modes[i] - modes[j]))
                extra.append(modes[i] + modes[j])
            extra.append(2 * modes[i])
        track = sorted(set(modes + extra + [0]))
        track = [m for m in track if 0 < m <= N // 2]

        res = simulate(params, osc, rho0, label=triad_name,
                       track_modes=track, mode_diag_interval=25)

        spec_ev = measure_spectral_evolution(res["mode_data"], modes)

        # Measure growth of non-excited combination modes
        combo_growth = {}
        for m in track:
            if m not in modes and m in spec_ev:
                combo_growth[m] = spec_ev[m]

        exp4[triad_name] = {
            **_compact_summary(res),
            "modes": modes,
            "spectral_evolution": spec_ev,
            "combination_mode_growth": combo_growth,
        }
        # Print growth of key combination modes
        for m in sorted(combo_growth.keys())[:5]:
            cg = combo_growth[m]
            print(f"  {triad_name} combo n={m}: "
                  f"initial={cg.get('initial', 0):.6f}, "
                  f"max={cg.get('max', 0):.6f}")

    all_results["exp4_triad"] = exp4

    # ===================================================================
    # EXP 5: MULTI-MODE PACKET
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXP 5: Multi-Mode Packet (20 modes)")
    print("=" * 70)
    exp5 = {}

    # 20 modes spanning n=4 to n=80
    packet_modes = list(range(4, 84, 4))  # [4, 8, 12, ..., 80]
    rho0, phases = ic_multi_mode_packet(N, 50.0, packet_modes, 1.0, seed=42)

    # Track all excited modes plus some intermediates
    track = sorted(set(packet_modes + [2, 6, 10, 14, 82, 84, 88, 0]))
    track = [m for m in track if 0 < m <= N // 2]

    params_long = EDParams(grid_size=N, n_steps=100000, dimensions=1)
    res = simulate(params_long, osc, rho0, label="packet_20modes",
                   track_modes=track, mode_diag_interval=50)

    spec_ev = measure_spectral_evolution(res["mode_data"], packet_modes)

    # Check for spectral broadening: amplitude growth in non-excited modes
    non_excited_growth = {}
    for m in track:
        if m not in packet_modes and m in spec_ev:
            non_excited_growth[m] = spec_ev[m]

    # Equipartition check: compare initial and final energy distribution
    excited_energies_initial = []
    excited_energies_final = []
    for m in packet_modes:
        if m in res["mode_data"] and res["mode_data"][m]["energy"]:
            excited_energies_initial.append(res["mode_data"][m]["energy"][0])
            excited_energies_final.append(res["mode_data"][m]["energy"][-1])

    ei = np.array(excited_energies_initial) if excited_energies_initial else np.array([0])
    ef = np.array(excited_energies_final) if excited_energies_final else np.array([0])
    equipartition_initial = float(np.std(ei) / max(np.mean(ei), 1e-15))
    equipartition_final = float(np.std(ef) / max(np.mean(ef), 1e-15))

    exp5["packet"] = {
        **_compact_summary(res),
        "n_modes": len(packet_modes),
        "modes": packet_modes,
        "non_excited_growth": non_excited_growth,
        "equipartition_cv_initial": equipartition_initial,
        "equipartition_cv_final": equipartition_final,
        "spectral_broadening": any(
            g.get("max", 0) > 0.01 for g in non_excited_growth.values()
        ),
    }
    print(f"  Packet: equipartition CV initial={equipartition_initial:.4f}, "
          f"final={equipartition_final:.4f}, "
          f"spectral_broadening={exp5['packet']['spectral_broadening']}, "
          f"clips={res['positivity_clips']}")
    for m in sorted(non_excited_growth.keys())[:5]:
        ng = non_excited_growth[m]
        print(f"    non-excited n={m}: max_amp={ng.get('max', 0):.6f}")

    all_results["exp5_packet"] = exp5

    # ===================================================================
    # EXP 6: STANDING WAVE STABILITY
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXP 6: Standing Wave Stability")
    print("=" * 70)
    exp6 = {}

    for n_mode, n_steps in [(16, 100000), (32, 100000)]:
        rho0 = ic_two_mode(N, 50.0, 5.0, n_mode, 0.0, 1)
        track = [n_mode, 2 * n_mode, 3 * n_mode, 0]
        track = [m for m in track if 0 < m <= N // 2]

        params_sw = EDParams(grid_size=N, n_steps=n_steps, dimensions=1)
        res = simulate(params_sw, osc, rho0, label=f"standing_n{n_mode}",
                       track_modes=track, mode_diag_interval=50)

        # Check node stability: nodes should be at fixed x positions
        # For sin(kx) mode, nodes are at x = j*N/(2*n_mode)
        # Check if the mode amplitude decays smoothly without node drift
        spec_ev = measure_spectral_evolution(res["mode_data"], [n_mode])
        harmonic_growth = {}
        for m in [2 * n_mode, 3 * n_mode]:
            if m in spec_ev and m <= N // 2:
                harmonic_growth[m] = spec_ev[m]

        key = f"standing_n{n_mode}"
        exp6[key] = {
            **_compact_summary(res),
            "n_mode": n_mode,
            "harmonic_growth": harmonic_growth,
            "mode_amp_initial": spec_ev.get(n_mode, {}).get("initial", None),
            "mode_amp_final": spec_ev.get(n_mode, {}).get("final", None),
            "spectral_evolution": spec_ev,
        }
        print(f"  {key}: amp {spec_ev.get(n_mode, {}).get('initial', '-'):.6f} -> "
              f"{spec_ev.get(n_mode, {}).get('final', '-'):.6f}, "
              f"2nd harmonic max={harmonic_growth.get(2*n_mode, {}).get('max', 0):.6f}, "
              f"clips={res['positivity_clips']}")

    all_results["exp6_standing"] = exp6

    # ===================================================================
    # EXP 7: 2D MODE INTERACTIONS
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXP 7: 2D Mode Interactions")
    print("=" * 70)
    exp7 = {}
    Nx_2d = 128
    params_2d = EDParams(grid_size=Nx_2d, n_steps=20000, dimensions=2)

    # 7a: Orthogonal modes sin(kx*x) + sin(ky*y)
    rho0_2d = ic_2d_two_mode(Nx_2d, 50.0, 5.0, 8, 8)
    res = simulate_2d(params_2d, osc, rho0_2d, label="2d_orthogonal_n8",
                      snapshot_interval=2000, radial_spectrum_interval=100)
    exp7["orthogonal_n8"] = {
        **_compact_summary(res),
        "initial_spectrum": res["spectra"][0] if res["spectra"] else [],
        "final_spectrum": res["spectra"][-1] if res["spectra"] else [],
    }
    np.save(os.path.join(results_dir, "2d_orthogonal_rho.npy"), res["final_rho"])
    drift = abs(res["diagnostics"]["rho_mean"][-1] - 50.0)
    print(f"  Orthogonal n=8: drift={drift:.4f}, clips={res['positivity_clips']}")

    # 7b: Different orthogonal modes sin(kx*x) + sin(ky*y) with different k
    rho0_2d = ic_2d_two_mode(Nx_2d, 50.0, 5.0, 4, 16)
    res = simulate_2d(params_2d, osc, rho0_2d, label="2d_mixed_n4_n16",
                      snapshot_interval=2000, radial_spectrum_interval=100)
    exp7["mixed_n4_n16"] = {
        **_compact_summary(res),
        "initial_spectrum": res["spectra"][0] if res["spectra"] else [],
        "final_spectrum": res["spectra"][-1] if res["spectra"] else [],
    }
    np.save(os.path.join(results_dir, "2d_mixed_rho.npy"), res["final_rho"])
    drift = abs(res["diagnostics"]["rho_mean"][-1] - 50.0)
    print(f"  Mixed n=4,16: drift={drift:.4f}, clips={res['positivity_clips']}")

    # 7c: Radial two-mode
    rho0_2d = ic_2d_radial_two_mode(Nx_2d, 50.0, 5.0, 5.0, 20.0)
    res = simulate_2d(params_2d, osc, rho0_2d, label="2d_radial_two_mode",
                      snapshot_interval=2000, radial_spectrum_interval=100)
    exp7["radial_two_mode"] = {
        **_compact_summary(res),
        "initial_spectrum": res["spectra"][0] if res["spectra"] else [],
        "final_spectrum": res["spectra"][-1] if res["spectra"] else [],
    }
    np.save(os.path.join(results_dir, "2d_radial_rho.npy"), res["final_rho"])
    drift = abs(res["diagnostics"]["rho_mean"][-1] - 50.0)
    print(f"  Radial two-mode: drift={drift:.4f}, clips={res['positivity_clips']}")

    # 7d: 2D Energy conservation (100K steps)
    params_2d_long = EDParams(grid_size=Nx_2d, n_steps=50000, dimensions=2)
    rho0_2d = ic_2d_two_mode(Nx_2d, 50.0, 3.0, 8, 8)
    res = simulate_2d(params_2d_long, osc, rho0_2d, label="2d_energy_test",
                      snapshot_interval=5000, radial_spectrum_interval=250)
    d = res["diagnostics"]
    E_arr = np.array(d["E_total"])
    dE = np.diff(E_arr)
    n_increases = int(np.sum(dE > 1e-10))
    E_drift_pct = abs(E_arr[-1] - E_arr[0]) / max(E_arr[0], 1e-15) * 100

    exp7["energy_conservation"] = {
        **_compact_summary(res),
        "E_initial": float(E_arr[0]),
        "E_final": float(E_arr[-1]),
        "E_monotonic": n_increases == 0,
        "n_energy_increases": n_increases,
        "E_drift_pct": E_drift_pct,
    }
    print(f"  2D Energy: {E_arr[0]:.6f} -> {E_arr[-1]:.6f}, "
          f"monotonic={n_increases==0}, drift={E_drift_pct:.4f}%")

    all_results["exp7_2d"] = exp7

    # ===================================================================
    # EXP 8: LONG-TERM TWO-MODE STABILITY
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXP 8: Long-Term Two-Mode Stability (100K steps)")
    print("=" * 70)
    exp8 = {}

    params_lt = EDParams(grid_size=N, n_steps=100000, dimensions=1)

    rho0 = ic_two_mode(N, 50.0, 5.0, 32, 5.0, 48)
    track = [32, 48, 16, 80, 0]
    res = simulate(params_lt, osc, rho0, label="stability_32_48",
                   track_modes=track, mode_diag_interval=50)

    spec_ev = measure_spectral_evolution(res["mode_data"], [32, 48])
    d = res["diagnostics"]
    E_arr = np.array(d["E_total"])
    dE = np.diff(E_arr)
    n_increases = int(np.sum(dE > 1e-10))

    exp8["stability_32_48"] = {
        **_compact_summary(res),
        "E_monotonic": n_increases == 0,
        "n_energy_increases": n_increases,
        "rho_mean_drift": abs(d["rho_mean"][-1] - d["rho_mean"][0]),
        "spectral_evolution": spec_ev,
    }
    print(f"  32+48 stability: E_mono={n_increases==0}, "
          f"mean_drift={abs(d['rho_mean'][-1]-d['rho_mean'][0]):.6f}, "
          f"clips={res['positivity_clips']}")

    all_results["exp8_stability"] = exp8

    # ===================================================================
    # Save
    # ===================================================================
    results_path = os.path.join(results_dir, "coupled_results.json")
    with open(results_path, "w") as f:
        json.dump(all_results, f, indent=2, default=_json_safe)
    print(f"\nResults saved to {results_path}")

    return all_results


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    script_dir = Path(__file__).parent
    results_dir = str(script_dir / "results")
    results = run_all_experiments(results_dir)

    print("\n" + "=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)
    for exp_name, exp_data in results.items():
        print(f"\n--- {exp_name} ---")
        for cfg, data in exp_data.items():
            if isinstance(data, dict):
                stable = "OK" if not data.get("blew_up", True) else "FAIL"
                clips = data.get("positivity_clips", "?")
                print(f"  {cfg:35s}: {stable}  clips={clips}")
