"""
ED-Phys-17: Oscillator Cosmology
=================================

Structure formation, peak dynamics, basin evolution, and horizon behavior
in an ED universe whose background density oscillates around rho_star
under P_SY2 + hyperbolic time.

Builds on ED-Phys-15 (P_SY2), ED-Phys-16 (mode interactions),
ED-Phys-14 (oscillatory participation), ED-Phys-06 (emergent phenomena).

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
# Configuration
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
# Operators (from ED-Phys-15)
# ---------------------------------------------------------------------------
def _pad(rho, boundary):
    if rho.ndim == 1:
        if boundary == "periodic":
            return np.concatenate(([rho[-1]], rho, [rho[0]]))
        return np.concatenate(([rho[0]], rho, [rho[-1]]))
    else:
        return np.pad(rho, 1, mode="wrap" if boundary == "periodic" else "edge")


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


def penalty_sy2(rho, alpha, gamma, rho_star, rho_0, eps=1e-10):
    rho_safe = np.maximum(rho, eps)
    delta = rho_safe - rho_star
    return alpha * gamma * delta / np.sqrt(delta * delta + rho_0 * rho_0)


def potential_sy2(rho, alpha, gamma, rho_star, rho_0):
    delta = rho - rho_star
    return alpha * gamma * np.sqrt(delta * delta + rho_0 * rho_0)


def compute_timestep(params, osc):
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
# Peak / Basin / Horizon tracking
# ---------------------------------------------------------------------------
def find_peaks_1d(rho, min_prominence=0.01):
    """Find local maxima with minimum prominence."""
    peaks = []
    for i in range(1, len(rho) - 1):
        if rho[i] > rho[i - 1] and rho[i] > rho[i + 1]:
            # Prominence: height above lowest neighbor
            prom = rho[i] - min(rho[i - 1], rho[i + 1])
            if prom >= min_prominence:
                peaks.append({"pos": i, "height": float(rho[i]), "prominence": float(prom)})
    # Also check wrap-around for periodic
    if len(rho) > 2:
        if rho[0] > rho[-1] and rho[0] > rho[1]:
            prom = rho[0] - min(rho[-1], rho[1])
            if prom >= min_prominence:
                peaks.append({"pos": 0, "height": float(rho[0]), "prominence": float(prom)})
    return sorted(peaks, key=lambda p: p["pos"])


def find_basins_1d(rho, min_depth=0.01):
    """Find local minima."""
    basins = []
    for i in range(1, len(rho) - 1):
        if rho[i] < rho[i - 1] and rho[i] < rho[i + 1]:
            depth = max(rho[i - 1], rho[i + 1]) - rho[i]
            if depth >= min_depth:
                basins.append({"pos": i, "depth": float(rho[i]), "depth_contrast": float(depth)})
    return sorted(basins, key=lambda b: b["pos"])


def find_horizons_1d(rho, rho_max, threshold=0.9):
    """Find regions where rho > threshold * rho_max."""
    horizon_threshold = threshold * rho_max
    above = rho >= horizon_threshold
    n_horizon = int(np.sum(above))
    if n_horizon == 0:
        return {"n_sites": 0, "fraction": 0.0, "max_rho": float(np.max(rho))}
    return {
        "n_sites": n_horizon,
        "fraction": float(n_horizon / len(rho)),
        "max_rho": float(np.max(rho)),
        "mean_horizon_rho": float(np.mean(rho[above])),
    }


def measure_peak_width(rho, peak_pos, rho_star):
    """Measure FWHM of a peak relative to rho_star."""
    h = rho[peak_pos]
    half_height = rho_star + (h - rho_star) / 2.0
    N = len(rho)
    # Search left
    left = peak_pos
    for j in range(1, N // 2):
        idx = (peak_pos - j) % N
        if rho[idx] <= half_height:
            left = j
            break
    # Search right
    right = peak_pos
    for j in range(1, N // 2):
        idx = (peak_pos + j) % N
        if rho[idx] <= half_height:
            right = j
            break
    return left + right  # FWHM in grid sites


# ---------------------------------------------------------------------------
# Initial conditions
# ---------------------------------------------------------------------------
def ic_global_oscillation(N, rho_star, A):
    """Uniform offset: rho = rho_star + A. System will oscillate globally."""
    return np.full(N, rho_star + A, dtype=np.float64)


def ic_modulated_oscillation(N, rho_star, A, n_mode):
    """Standing wave: rho = rho_star + A*sin(kx)."""
    x = np.arange(N, dtype=np.float64)
    return rho_star + A * np.sin(2 * np.pi * n_mode * x / N)


def ic_multi_mode_background(N, rho_star, amplitudes, modes, seed=42):
    """Multi-mode oscillatory background."""
    rng = np.random.default_rng(seed)
    rho = np.full(N, rho_star, dtype=np.float64)
    for A, n in zip(amplitudes, modes):
        phi = rng.uniform(0, 2 * np.pi)
        rho += A * np.sin(2 * np.pi * n * np.arange(N, dtype=np.float64) / N + phi)
    return rho


def ic_peak_on_background(N, rho_star, bg_perturbation, peak_height, peak_pos, peak_sigma):
    """Gaussian peak on top of a background perturbation."""
    x = np.arange(N, dtype=np.float64)
    rho = rho_star + bg_perturbation
    rho += peak_height * np.exp(-((x - peak_pos) ** 2) / (2 * peak_sigma ** 2))
    return rho


def ic_two_peaks(N, rho_star, bg_perturbation, h1, p1, s1, h2, p2, s2):
    """Two Gaussian peaks on a background."""
    x = np.arange(N, dtype=np.float64)
    rho = rho_star + bg_perturbation
    rho += h1 * np.exp(-((x - p1) ** 2) / (2 * s1 ** 2))
    rho += h2 * np.exp(-((x - p2) ** 2) / (2 * s2 ** 2))
    return rho


def ic_multi_peak(N, rho_star, bg_perturbation, n_peaks, peak_height, peak_sigma, seed=42):
    """Multiple random peaks on a background."""
    rng = np.random.default_rng(seed)
    x = np.arange(N, dtype=np.float64)
    rho = rho_star + bg_perturbation
    positions = rng.choice(N, n_peaks, replace=False)
    for p in positions:
        h = peak_height * (0.5 + rng.random())
        rho += h * np.exp(-((x - p) ** 2) / (2 * peak_sigma ** 2))
    return rho, sorted(positions.tolist())


def ic_near_horizon(N, rho_star, rho_max, bg_perturbation, peak_height, peak_pos, peak_sigma):
    """Peak that approaches horizon (rho_max)."""
    x = np.arange(N, dtype=np.float64)
    rho = rho_star + bg_perturbation
    rho += peak_height * np.exp(-((x - peak_pos) ** 2) / (2 * peak_sigma ** 2))
    return np.clip(rho, 0, rho_max - 0.1)


def ic_2d_peaks_on_oscillation(Nx, rho_star, A, n_mode, peaks, peak_sigma):
    """2D: sinusoidal background + Gaussian peaks."""
    x = np.arange(Nx, dtype=np.float64)
    X, Y = np.meshgrid(x, x)
    rho = rho_star + A * np.sin(2 * np.pi * n_mode * X / Nx)
    for px, py, ph in peaks:
        rho += ph * np.exp(-((X - px) ** 2 + (Y - py) ** 2) / (2 * peak_sigma ** 2))
    return rho


def ic_2d_random_cosmo(Nx, rho_star, amplitude, n_modes, seed=42):
    """2D random cosmological field around rho_star."""
    rng = np.random.default_rng(seed)
    x = np.arange(Nx, dtype=np.float64)
    X, Y = np.meshgrid(x, x)
    rho = np.full((Nx, Nx), rho_star, dtype=np.float64)
    for _ in range(n_modes):
        nx = rng.integers(1, Nx // 4)
        ny = rng.integers(1, Nx // 4)
        phi = rng.uniform(0, 2 * np.pi)
        A = amplitude * (0.5 + rng.random())
        rho += A * np.sin(2 * np.pi * nx * X / Nx + phi) * np.cos(2 * np.pi * ny * Y / Nx)
    return rho


# ---------------------------------------------------------------------------
# Simulator
# ---------------------------------------------------------------------------
def simulate(
    params: EDParams,
    osc: OscParams,
    initial_rho: np.ndarray,
    label: str = "",
    snapshot_interval: int = 1000,
    track_peaks: bool = True,
    initial_v: np.ndarray | None = None,
) -> dict:
    rho = initial_rho.astype(np.float64).copy()
    eta = compute_timestep(params, osc)
    v = initial_v.copy() if initial_v is not None else np.zeros_like(rho)

    diag_interval = max(1, params.n_steps // 4000)
    peak_interval = max(1, params.n_steps // 500)

    diagnostics = {
        "rho_mean": [], "rho_std": [], "rho_min": [], "rho_max": [],
        "v_rms": [], "E_total": [],
    }
    peak_history = []
    basin_history = []
    horizon_history = []
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
            V = potential_sy2(rho_new, params.alpha, params.gamma_exp, osc.rho_star, osc.rho_0)
            M_star = params.M_0 * (1.0 - osc.rho_star / params.rho_max) ** params.n_mob
            gs = discrete_grad_squared(np.maximum(rho_new, params.eps), params.dx, params.boundary)
            E_t = 0.5 * osc.tau * float(np.mean(v_new ** 2)) + \
                  0.5 * M_star * float(np.mean(gs)) + float(np.mean(V))
            diagnostics["rho_mean"].append(float(np.mean(rho_new)))
            diagnostics["rho_std"].append(float(np.std(rho_new)))
            diagnostics["rho_min"].append(float(np.min(rho_new)))
            diagnostics["rho_max"].append(float(np.max(rho_new)))
            diagnostics["v_rms"].append(float(np.sqrt(np.mean(v_new ** 2))))
            diagnostics["E_total"].append(E_t)

        if track_peaks and rho.ndim == 1 and (
            t % peak_interval == 0 or t == params.n_steps - 1
        ):
            peaks = find_peaks_1d(rho_new, min_prominence=0.01)
            basins = find_basins_1d(rho_new, min_depth=0.01)
            horizons = find_horizons_1d(rho_new, params.rho_max)
            peak_history.append({"step": t, "n_peaks": len(peaks),
                                 "peaks": peaks[:10]})  # cap storage
            basin_history.append({"step": t, "n_basins": len(basins),
                                  "basins": basins[:10]})
            horizon_history.append({"step": t, **horizons})

        if t % snapshot_interval == 0 or t == params.n_steps - 1:
            snapshots.append(rho_new.copy())
            snapshot_times.append(t)

        rho = rho_new
        v = v_new

    elapsed = time.time() - t_start

    return {
        "label": label, "eta": eta,
        "blew_up": blew_up,
        "steps_completed": t + 1 if blew_up else params.n_steps,
        "elapsed_s": round(elapsed, 3),
        "positivity_clips": positivity_clips,
        "diagnostics": diagnostics,
        "peak_history": peak_history,
        "basin_history": basin_history,
        "horizon_history": horizon_history,
        "snapshots": snapshots,
        "snapshot_times": snapshot_times,
        "final_rho": rho,
        "final_v": v,
    }


# ---------------------------------------------------------------------------
# Analysis helpers
# ---------------------------------------------------------------------------
def analyze_peak_dynamics(peak_history, rho_star):
    """Analyze peak evolution over time."""
    if not peak_history or len(peak_history) < 5:
        return {"n_peaks_initial": 0, "n_peaks_final": 0}

    n_initial = peak_history[0]["n_peaks"]
    n_final = peak_history[-1]["n_peaks"]
    n_series = [ph["n_peaks"] for ph in peak_history]
    n_min = min(n_series)
    n_max = max(n_series)

    # Track tallest peak
    h_series = []
    pos_series = []
    for ph in peak_history:
        if ph["peaks"]:
            tallest = max(ph["peaks"], key=lambda p: p["height"])
            h_series.append(tallest["height"])
            pos_series.append(tallest["pos"])
        else:
            h_series.append(rho_star)
            pos_series.append(-1)

    h_arr = np.array(h_series)
    # Peak height oscillation
    h_osc = 0
    for i in range(1, len(h_arr) - 1):
        if (h_arr[i] > h_arr[i - 1] and h_arr[i] > h_arr[i + 1]) or \
           (h_arr[i] < h_arr[i - 1] and h_arr[i] < h_arr[i + 1]):
            h_osc += 1
    h_osc //= 2

    # Peak position drift
    pos_arr = np.array(pos_series)
    valid = pos_arr >= 0
    if np.sum(valid) > 2:
        pos_drift = float(np.std(pos_arr[valid]))
    else:
        pos_drift = 0.0

    # Merging events (n_peaks decreases)
    merges = 0
    for i in range(1, len(n_series)):
        if n_series[i] < n_series[i - 1]:
            merges += n_series[i - 1] - n_series[i]

    return {
        "n_peaks_initial": n_initial,
        "n_peaks_final": n_final,
        "n_peaks_min": n_min,
        "n_peaks_max": n_max,
        "peak_oscillations": h_osc,
        "tallest_initial": float(h_arr[0]) if len(h_arr) > 0 else None,
        "tallest_final": float(h_arr[-1]) if len(h_arr) > 0 else None,
        "tallest_max": float(np.max(h_arr)) if len(h_arr) > 0 else None,
        "tallest_min": float(np.min(h_arr)) if len(h_arr) > 0 else None,
        "peak_pos_drift": pos_drift,
        "merging_events": merges,
        "n_peaks_oscillates": n_max > n_min + 1,
    }


def analyze_basins(basin_history, rho_star):
    """Analyze basin depth evolution."""
    if not basin_history or len(basin_history) < 5:
        return {}
    n_series = [bh["n_basins"] for bh in basin_history]
    depth_series = []
    for bh in basin_history:
        if bh["basins"]:
            deepest = min(bh["basins"], key=lambda b: b["depth"])
            depth_series.append(deepest["depth"])
        else:
            depth_series.append(rho_star)

    d_arr = np.array(depth_series)
    return {
        "n_basins_initial": n_series[0],
        "n_basins_final": n_series[-1],
        "deepest_initial": float(d_arr[0]) if len(d_arr) > 0 else None,
        "deepest_final": float(d_arr[-1]) if len(d_arr) > 0 else None,
        "deepest_min": float(np.min(d_arr)) if len(d_arr) > 0 else None,
        "basin_oscillates": float(np.std(d_arr)) > 0.5 if len(d_arr) > 0 else False,
    }


def analyze_horizons(horizon_history):
    """Analyze horizon evolution."""
    if not horizon_history:
        return {}
    frac_series = [hh.get("fraction", 0) for hh in horizon_history]
    n_series = [hh.get("n_sites", 0) for hh in horizon_history]
    return {
        "horizon_initial": n_series[0],
        "horizon_final": n_series[-1],
        "horizon_max": max(n_series),
        "horizon_fraction_max": float(max(frac_series)),
        "horizon_ever_formed": max(n_series) > 0,
    }


def _compact(res):
    d = res["diagnostics"]
    pd = analyze_peak_dynamics(res["peak_history"], 50.0)
    bd = analyze_basins(res["basin_history"], 50.0)
    hd = analyze_horizons(res["horizon_history"])
    return {
        "label": res["label"],
        "blew_up": res["blew_up"],
        "elapsed_s": res["elapsed_s"],
        "positivity_clips": res["positivity_clips"],
        "rho_mean_initial": d["rho_mean"][0] if d["rho_mean"] else None,
        "rho_mean_final": d["rho_mean"][-1] if d["rho_mean"] else None,
        "rho_std_initial": d["rho_std"][0] if d["rho_std"] else None,
        "rho_std_final": d["rho_std"][-1] if d["rho_std"] else None,
        "rho_max_final": d["rho_max"][-1] if d["rho_max"] else None,
        "rho_min_final": d["rho_min"][-1] if d["rho_min"] else None,
        "E_initial": d["E_total"][0] if d["E_total"] else None,
        "E_final": d["E_total"][-1] if d["E_total"] else None,
        "rho_mean_series": d["rho_mean"],
        "rho_std_series": d["rho_std"],
        "E_total_series": d["E_total"],
        "peak_dynamics": pd,
        "basin_dynamics": bd,
        "horizon_dynamics": hd,
    }


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


# ===================================================================
# EXPERIMENTS
# ===================================================================
def run_all_experiments(results_dir):
    os.makedirs(results_dir, exist_ok=True)
    all_results = {}

    N = 512
    osc = OscParams(tau=100, zeta=0.5, rho_star=50, rho_0=0.5)

    print("=" * 70)
    print("ED-Phys-17: Oscillator Cosmology")
    print("=" * 70)

    # ===================================================================
    # EXP 1: PEAK DYNAMICS IN OSCILLATORY BACKGROUNDS (TASK 2)
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXP 1: Peak Dynamics in Oscillatory Backgrounds")
    print("=" * 70)
    exp1 = {}
    params = EDParams(grid_size=N, n_steps=50000, dimensions=1)

    # 1a: Single peak on flat background (baseline)
    bg_flat = np.zeros(N)
    rho0 = ic_peak_on_background(N, 50.0, bg_flat, 30.0, N // 2, 15.0)
    res = simulate(params, osc, rho0, label="single_peak_flat")
    exp1["single_peak_flat"] = _compact(res)
    pd = exp1["single_peak_flat"]["peak_dynamics"]
    print(f"  Flat bg: peak {pd['tallest_initial']:.1f}->{pd['tallest_final']:.1f}, "
          f"osc={pd['peak_oscillations']}, drift={pd['peak_pos_drift']:.1f}, "
          f"clips={res['positivity_clips']}")

    # 1b: Single peak on global oscillation background (A=10)
    bg_global = np.full(N, 10.0)  # rho starts at 60 = rho_star + 10
    rho0 = ic_peak_on_background(N, 50.0, bg_global, 20.0, N // 2, 15.0)
    res = simulate(params, osc, rho0, label="single_peak_global_osc")
    exp1["single_peak_global_osc"] = _compact(res)
    pd = exp1["single_peak_global_osc"]["peak_dynamics"]
    print(f"  Global osc bg: peak {pd['tallest_initial']:.1f}->{pd['tallest_final']:.1f}, "
          f"osc={pd['peak_oscillations']}, drift={pd['peak_pos_drift']:.1f}")

    # 1c: Single peak on standing wave background (n=4)
    x = np.arange(N, dtype=np.float64)
    bg_wave = 10.0 * np.sin(2 * np.pi * 4 * x / N)
    rho0 = ic_peak_on_background(N, 50.0, bg_wave, 20.0, N // 2, 15.0)
    res = simulate(params, osc, rho0, label="single_peak_wave_bg")
    exp1["single_peak_wave_bg"] = _compact(res)
    pd = exp1["single_peak_wave_bg"]["peak_dynamics"]
    print(f"  Wave bg: peak {pd['tallest_initial']:.1f}->{pd['tallest_final']:.1f}, "
          f"osc={pd['peak_oscillations']}, peaks_final={pd['n_peaks_final']}")

    # 1d: Two peaks on flat background (interaction test)
    bg_flat = np.zeros(N)
    rho0 = ic_two_peaks(N, 50.0, bg_flat, 25.0, 150, 15.0, 25.0, 350, 15.0)
    res = simulate(params, osc, rho0, label="two_peaks_flat")
    exp1["two_peaks_flat"] = _compact(res)
    pd = exp1["two_peaks_flat"]["peak_dynamics"]
    print(f"  Two peaks flat: peaks {pd['n_peaks_initial']}->{pd['n_peaks_final']}, "
          f"merges={pd['merging_events']}, drift={pd['peak_pos_drift']:.1f}")

    # 1e: Two peaks on oscillatory background
    bg_wave = 8.0 * np.sin(2 * np.pi * 2 * x / N)
    rho0 = ic_two_peaks(N, 50.0, bg_wave, 25.0, 150, 15.0, 25.0, 350, 15.0)
    res = simulate(params, osc, rho0, label="two_peaks_wave_bg")
    exp1["two_peaks_wave_bg"] = _compact(res)
    pd = exp1["two_peaks_wave_bg"]["peak_dynamics"]
    print(f"  Two peaks wave: peaks {pd['n_peaks_initial']}->{pd['n_peaks_final']}, "
          f"merges={pd['merging_events']}, osc={pd['peak_oscillations']}")

    all_results["exp1_peak_dynamics"] = exp1

    # ===================================================================
    # EXP 2: BASIN AND HORIZON BEHAVIOR (TASK 3)
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXP 2: Basin and Horizon Behavior")
    print("=" * 70)
    exp2 = {}

    # 2a: Deep basin (rho well below rho_star)
    bg = np.zeros(N)
    bg[200:300] = -30.0  # basin at rho=20
    rho0 = 50.0 + bg
    res = simulate(params, osc, rho0, label="deep_basin")
    exp2["deep_basin"] = _compact(res)
    bd = exp2["deep_basin"]["basin_dynamics"]
    print(f"  Deep basin: depth {bd.get('deepest_initial', '?'):.1f}"
          f"->{bd.get('deepest_final', '?'):.1f}, "
          f"oscillates={bd.get('basin_oscillates', '-')}")

    # 2b: Near-horizon peak
    rho0 = ic_near_horizon(N, 50.0, 100.0, np.zeros(N), 45.0, N // 2, 15.0)
    res = simulate(params, osc, rho0, label="near_horizon")
    exp2["near_horizon"] = _compact(res)
    hd = exp2["near_horizon"]["horizon_dynamics"]
    pd = exp2["near_horizon"]["peak_dynamics"]
    print(f"  Near horizon: peak {pd['tallest_initial']:.1f}->{pd['tallest_final']:.1f}, "
          f"horizon_formed={hd.get('horizon_ever_formed', '-')}, "
          f"horizon_max={hd.get('horizon_max', 0)}")

    # 2c: Near-horizon on oscillatory background
    bg_wave = 5.0 * np.sin(2 * np.pi * 4 * x / N)
    rho0 = ic_near_horizon(N, 50.0, 100.0, bg_wave, 40.0, N // 2, 15.0)
    res = simulate(params, osc, rho0, label="near_horizon_wave")
    exp2["near_horizon_wave"] = _compact(res)
    hd = exp2["near_horizon_wave"]["horizon_dynamics"]
    pd = exp2["near_horizon_wave"]["peak_dynamics"]
    print(f"  Near horizon + wave: peak {pd['tallest_initial']:.1f}"
          f"->{pd['tallest_final']:.1f}, "
          f"horizon_formed={hd.get('horizon_ever_formed', '-')}")

    # 2d: Basin surrounded by peaks (cosmological void)
    rho0 = np.full(N, 50.0)
    rho0[100:150] = 75.0  # left peak
    rho0[350:400] = 75.0  # right peak
    rho0[150:350] = 35.0  # void
    # Smooth
    from scipy.ndimage import gaussian_filter1d
    rho0 = gaussian_filter1d(rho0, sigma=10.0)
    res = simulate(params, osc, rho0, label="cosmological_void")
    exp2["cosmological_void"] = _compact(res)
    bd = exp2["cosmological_void"]["basin_dynamics"]
    pd = exp2["cosmological_void"]["peak_dynamics"]
    print(f"  Cosmological void: peaks {pd['n_peaks_initial']}->{pd['n_peaks_final']}, "
          f"basin depth {bd.get('deepest_initial', '?'):.1f}"
          f"->{bd.get('deepest_final', '?'):.1f}")

    all_results["exp2_basin_horizon"] = exp2

    # ===================================================================
    # EXP 3: OSCILLATORY THINNING AND INFLATION (TASK 4)
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXP 3: Oscillatory Thinning and Inflation")
    print("=" * 70)
    exp3 = {}

    # 3a: Peak at wave node (bg=rho_star there, bg oscillates elsewhere)
    bg_wave = 10.0 * np.sin(2 * np.pi * 2 * x / N)
    # Node of sin(2*pi*2*x/512) is at x=0,128,256,384
    rho0 = ic_peak_on_background(N, 50.0, bg_wave, 20.0, 128, 15.0)  # peak at node
    res = simulate(params, osc, rho0, label="peak_at_node")
    exp3["peak_at_node"] = _compact(res)
    pd = exp3["peak_at_node"]["peak_dynamics"]
    print(f"  Peak at node: {pd['tallest_initial']:.1f}->{pd['tallest_final']:.1f}, "
          f"osc={pd['peak_oscillations']}")

    # 3b: Peak at wave crest (bg is max there)
    rho0 = ic_peak_on_background(N, 50.0, bg_wave, 20.0, 64, 15.0)  # peak at crest
    res = simulate(params, osc, rho0, label="peak_at_crest")
    exp3["peak_at_crest"] = _compact(res)
    pd = exp3["peak_at_crest"]["peak_dynamics"]
    print(f"  Peak at crest: {pd['tallest_initial']:.1f}->{pd['tallest_final']:.1f}, "
          f"osc={pd['peak_oscillations']}")

    # 3c: Peak at wave trough (bg is min there)
    rho0 = ic_peak_on_background(N, 50.0, bg_wave, 20.0, 192, 15.0)  # peak at trough
    res = simulate(params, osc, rho0, label="peak_at_trough")
    exp3["peak_at_trough"] = _compact(res)
    pd = exp3["peak_at_trough"]["peak_dynamics"]
    print(f"  Peak at trough: {pd['tallest_initial']:.1f}->{pd['tallest_final']:.1f}, "
          f"osc={pd['peak_oscillations']}")

    # 3d: Phase-locking test — two peaks at different phases of background
    rho0 = ic_two_peaks(N, 50.0, bg_wave, 20.0, 64, 15.0, 20.0, 192, 15.0)
    res = simulate(params, osc, rho0, label="phase_locking")
    exp3["phase_locking"] = _compact(res)
    pd = exp3["phase_locking"]["peak_dynamics"]
    print(f"  Phase locking: peaks {pd['n_peaks_initial']}->{pd['n_peaks_final']}, "
          f"osc={pd['peak_oscillations']}, merges={pd['merging_events']}")

    all_results["exp3_thinning_inflation"] = exp3

    # ===================================================================
    # EXP 4: MULTI-PEAK INTERACTION TESTS (TASK 5)
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXP 4: Multi-Peak Interactions")
    print("=" * 70)
    exp4 = {}

    params_long = EDParams(grid_size=N, n_steps=100000, dimensions=1)

    # 4a: 5 peaks on flat background
    rho0, positions = ic_multi_peak(N, 50.0, np.zeros(N), 5, 20.0, 12.0, seed=42)
    res = simulate(params_long, osc, rho0, label="5_peaks_flat")
    exp4["5_peaks_flat"] = _compact(res)
    pd = exp4["5_peaks_flat"]["peak_dynamics"]
    print(f"  5 peaks flat: {pd['n_peaks_initial']}->{pd['n_peaks_final']}, "
          f"merges={pd['merging_events']}, osc={pd['peak_oscillations']}")

    # 4b: 5 peaks on oscillatory background
    bg_wave = 8.0 * np.sin(2 * np.pi * 4 * x / N)
    rho0, positions = ic_multi_peak(N, 50.0, bg_wave, 5, 20.0, 12.0, seed=42)
    res = simulate(params_long, osc, rho0, label="5_peaks_wave")
    exp4["5_peaks_wave"] = _compact(res)
    pd = exp4["5_peaks_wave"]["peak_dynamics"]
    print(f"  5 peaks wave: {pd['n_peaks_initial']}->{pd['n_peaks_final']}, "
          f"merges={pd['merging_events']}, osc={pd['peak_oscillations']}")

    # 4c: 10 peaks on flat background
    rho0, positions = ic_multi_peak(N, 50.0, np.zeros(N), 10, 15.0, 10.0, seed=123)
    res = simulate(params_long, osc, rho0, label="10_peaks_flat")
    exp4["10_peaks_flat"] = _compact(res)
    pd = exp4["10_peaks_flat"]["peak_dynamics"]
    print(f"  10 peaks flat: {pd['n_peaks_initial']}->{pd['n_peaks_final']}, "
          f"merges={pd['merging_events']}, osc={pd['peak_oscillations']}")

    # 4d: 10 peaks on multi-mode background
    bg_multi = ic_multi_mode_background(N, 0.0, [5.0, 3.0, 4.0], [2, 8, 16], seed=77)
    rho0, positions = ic_multi_peak(N, 50.0, bg_multi, 10, 15.0, 10.0, seed=123)
    res = simulate(params_long, osc, rho0, label="10_peaks_multi_bg")
    exp4["10_peaks_multi_bg"] = _compact(res)
    pd = exp4["10_peaks_multi_bg"]["peak_dynamics"]
    print(f"  10 peaks multi-bg: {pd['n_peaks_initial']}->{pd['n_peaks_final']}, "
          f"merges={pd['merging_events']}, osc={pd['peak_oscillations']}")

    # 4e: Close pair — test merging vs oscillatory repulsion
    rho0 = ic_two_peaks(N, 50.0, np.zeros(N), 25.0, 240, 12.0, 25.0, 280, 12.0)
    res = simulate(params, osc, rho0, label="close_pair_40sep")
    exp4["close_pair_40sep"] = _compact(res)
    pd = exp4["close_pair_40sep"]["peak_dynamics"]
    print(f"  Close pair (sep=40): {pd['n_peaks_initial']}->{pd['n_peaks_final']}, "
          f"merges={pd['merging_events']}")

    # 4f: Very close pair
    rho0 = ic_two_peaks(N, 50.0, np.zeros(N), 25.0, 246, 12.0, 25.0, 266, 12.0)
    res = simulate(params, osc, rho0, label="close_pair_20sep")
    exp4["close_pair_20sep"] = _compact(res)
    pd = exp4["close_pair_20sep"]["peak_dynamics"]
    print(f"  Close pair (sep=20): {pd['n_peaks_initial']}->{pd['n_peaks_final']}, "
          f"merges={pd['merging_events']}")

    all_results["exp4_multi_peak"] = exp4

    # ===================================================================
    # EXP 5: 2D OSCILLATOR COSMOLOGY (TASK 6)
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXP 5: 2D Oscillator Cosmology")
    print("=" * 70)
    exp5 = {}
    Nx = 128
    params_2d = EDParams(grid_size=Nx, n_steps=20000, dimensions=2)

    # 5a: Radial peak on oscillatory background
    rho0_2d = ic_2d_peaks_on_oscillation(
        Nx, 50.0, 8.0, 4, [(64, 64, 25.0)], 10.0
    )
    res = simulate(params_2d, osc, rho0_2d, label="2d_radial_osc",
                   snapshot_interval=2000, track_peaks=False)
    exp5["radial_osc"] = {
        "label": res["label"],
        "blew_up": res["blew_up"],
        "positivity_clips": res["positivity_clips"],
        "rho_mean_final": res["diagnostics"]["rho_mean"][-1],
        "rho_std_final": res["diagnostics"]["rho_std"][-1],
        "rho_mean_drift": abs(res["diagnostics"]["rho_mean"][-1] - 50.0),
    }
    np.save(os.path.join(results_dir, "2d_radial_osc.npy"), res["final_rho"])
    print(f"  2D radial+osc: drift={abs(res['diagnostics']['rho_mean'][-1]-50):.4f}, "
          f"clips={res['positivity_clips']}")

    # 5b: Directional oscillatory background with peaks
    rho0_2d = ic_2d_peaks_on_oscillation(
        Nx, 50.0, 8.0, 8,
        [(32, 64, 20.0), (96, 64, 20.0)], 8.0
    )
    res = simulate(params_2d, osc, rho0_2d, label="2d_dir_peaks",
                   snapshot_interval=2000, track_peaks=False)
    exp5["directional_peaks"] = {
        "label": res["label"],
        "blew_up": res["blew_up"],
        "positivity_clips": res["positivity_clips"],
        "rho_mean_final": res["diagnostics"]["rho_mean"][-1],
        "rho_std_final": res["diagnostics"]["rho_std"][-1],
        "rho_mean_drift": abs(res["diagnostics"]["rho_mean"][-1] - 50.0),
    }
    np.save(os.path.join(results_dir, "2d_dir_peaks.npy"), res["final_rho"])
    print(f"  2D directional+peaks: drift={abs(res['diagnostics']['rho_mean'][-1]-50):.4f}, "
          f"clips={res['positivity_clips']}")

    # 5c: Random cosmological field (multi-mode)
    rho0_2d = ic_2d_random_cosmo(Nx, 50.0, 3.0, 15, seed=42)
    res = simulate(params_2d, osc, rho0_2d, label="2d_random_cosmo",
                   snapshot_interval=2000, track_peaks=False)
    exp5["random_cosmo"] = {
        "label": res["label"],
        "blew_up": res["blew_up"],
        "positivity_clips": res["positivity_clips"],
        "rho_mean_final": res["diagnostics"]["rho_mean"][-1],
        "rho_std_final": res["diagnostics"]["rho_std"][-1],
        "rho_std_initial": res["diagnostics"]["rho_std"][0],
        "rho_mean_drift": abs(res["diagnostics"]["rho_mean"][-1] - 50.0),
        "E_initial": res["diagnostics"]["E_total"][0],
        "E_final": res["diagnostics"]["E_total"][-1],
    }
    np.save(os.path.join(results_dir, "2d_random_cosmo.npy"), res["final_rho"])
    print(f"  2D random cosmo: drift={abs(res['diagnostics']['rho_mean'][-1]-50):.4f}, "
          f"std {res['diagnostics']['rho_std'][0]:.3f}->"
          f"{res['diagnostics']['rho_std'][-1]:.3f}, "
          f"clips={res['positivity_clips']}")

    # 5d: Long 2D cosmology (50K steps)
    params_2d_long = EDParams(grid_size=Nx, n_steps=50000, dimensions=2)
    rho0_2d = ic_2d_random_cosmo(Nx, 50.0, 2.0, 15, seed=99)
    res = simulate(params_2d_long, osc, rho0_2d, label="2d_cosmo_long",
                   snapshot_interval=5000, track_peaks=False)
    exp5["cosmo_long"] = {
        "label": res["label"],
        "blew_up": res["blew_up"],
        "positivity_clips": res["positivity_clips"],
        "rho_mean_final": res["diagnostics"]["rho_mean"][-1],
        "rho_std_final": res["diagnostics"]["rho_std"][-1],
        "rho_std_initial": res["diagnostics"]["rho_std"][0],
        "rho_mean_drift": abs(res["diagnostics"]["rho_mean"][-1] - 50.0),
        "E_initial": res["diagnostics"]["E_total"][0],
        "E_final": res["diagnostics"]["E_total"][-1],
    }
    np.save(os.path.join(results_dir, "2d_cosmo_long.npy"), res["final_rho"])
    print(f"  2D cosmo long (50K): drift={abs(res['diagnostics']['rho_mean'][-1]-50):.4f}, "
          f"std {res['diagnostics']['rho_std'][0]:.3f}->"
          f"{res['diagnostics']['rho_std'][-1]:.3f}, "
          f"clips={res['positivity_clips']}")

    all_results["exp5_2d_cosmology"] = exp5

    # ===================================================================
    # EXP 6: COMPARISON — OSCILLATORY vs PARABOLIC COSMOLOGY
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXP 6: Oscillatory vs Parabolic Cosmology Comparison")
    print("=" * 70)
    exp6 = {}
    params_cmp = EDParams(grid_size=N, n_steps=50000, dimensions=1)

    # Same multi-peak IC for both
    rho0_cmp, _ = ic_multi_peak(N, 50.0, np.zeros(N), 5, 20.0, 12.0, seed=42)

    # Oscillatory (hyperbolic + P_SY2)
    res_osc = simulate(params_cmp, osc, rho0_cmp.copy(), label="osc_5peaks")
    exp6["oscillatory"] = _compact(res_osc)
    pd_osc = exp6["oscillatory"]["peak_dynamics"]

    # Parabolic (first-order + P_SY2 — use very large tau so v tracks RHS)
    # Actually, for true parabolic, set tau very small (instant velocity equilibration)
    # In practice, use the parabolic update: rho_new = rho + eta * RHS
    # Let me simulate parabolic directly
    rho_par = rho0_cmp.copy()
    eta_par = compute_timestep(params_cmp, osc)
    par_diag = {"rho_mean": [], "rho_std": []}
    par_peak_hist = []
    peak_int = max(1, params_cmp.n_steps // 500)
    diag_int = max(1, params_cmp.n_steps // 4000)
    for t in range(params_cmp.n_steps):
        rho_s = np.maximum(rho_par, params_cmp.eps)
        lap = discrete_laplacian(rho_s, params_cmp.dx, params_cmp.boundary)
        gs = discrete_grad_squared(rho_s, params_cmp.dx, params_cmp.boundary)
        M, Mp = mobility(rho_s, params_cmp.M_0, params_cmp.rho_max, params_cmp.n_mob)
        pen = penalty_sy2(rho_s, params_cmp.alpha, params_cmp.gamma_exp,
                          osc.rho_star, osc.rho_0, params_cmp.eps)
        rhs = M * lap + Mp * gs - pen
        rho_par = rho_par + eta_par * rhs
        rho_par = np.maximum(rho_par, 0.0)
        if t % diag_int == 0:
            par_diag["rho_mean"].append(float(np.mean(rho_par)))
            par_diag["rho_std"].append(float(np.std(rho_par)))
        if t % peak_int == 0:
            peaks = find_peaks_1d(rho_par, 0.01)
            par_peak_hist.append({"step": t, "n_peaks": len(peaks), "peaks": peaks[:10]})

    pd_par = analyze_peak_dynamics(par_peak_hist, 50.0)
    exp6["parabolic"] = {
        "label": "parabolic_5peaks",
        "rho_mean_final": par_diag["rho_mean"][-1] if par_diag["rho_mean"] else None,
        "rho_std_final": par_diag["rho_std"][-1] if par_diag["rho_std"] else None,
        "peak_dynamics": pd_par,
        "rho_mean_series": par_diag["rho_mean"],
        "rho_std_series": par_diag["rho_std"],
    }

    print(f"  Oscillatory: peaks {pd_osc['n_peaks_initial']}->{pd_osc['n_peaks_final']}, "
          f"merges={pd_osc['merging_events']}, osc={pd_osc['peak_oscillations']}")
    print(f"  Parabolic:   peaks {pd_par['n_peaks_initial']}->{pd_par['n_peaks_final']}, "
          f"merges={pd_par['merging_events']}, osc={pd_par['peak_oscillations']}")

    all_results["exp6_comparison"] = exp6

    # ===================================================================
    # Save
    # ===================================================================
    results_path = os.path.join(results_dir, "oscosmo_results.json")
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
                pd = data.get("peak_dynamics", {})
                clips = data.get("positivity_clips", "?")
                n_i = pd.get("n_peaks_initial", "-")
                n_f = pd.get("n_peaks_final", "-")
                merges = pd.get("merging_events", "-")
                osc_n = pd.get("peak_oscillations", "-")
                print(f"  {cfg:30s}: peaks {n_i}->{n_f}  merges={merges}  "
                      f"osc={osc_n}  clips={clips}")
