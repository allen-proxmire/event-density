"""
ED-Phys-18: Hybrid Cosmology (Oscillator + Parabolic)
=====================================================

Combines parabolic ED cosmology (diffusive, structure-forming, irreversible)
with oscillator ED cosmology (reversible, conservative, universally relaxing).

Hybrid update rule:
    drho/dt = D * RHS  +  H * v
    dv/dt   = (1/tau) * (RHS - zeta * v)

where RHS = M(rho)*Lap(rho) + M'(rho)*|grad rho|^2 - P_SY2(rho)
      D + H = 1 (normalized mixture)

When D=1, H=0: pure parabolic (v decouples)
When D=0, H=1: pure oscillatory
When 0<D<1, 0<H<1: hybrid

Builds on ED-Phys-17 (oscillator cosmology), ED-Phys-15 (P_SY2),
ED-Phys-13 (parabolic vs hyperbolic), ED-Phys-06 (emergent phenomena).

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


@dataclass
class HybridParams:
    """Hybrid mixing weights. D + H must equal 1."""
    D: float = 0.5   # parabolic weight
    H: float = 0.5   # oscillatory weight


# ---------------------------------------------------------------------------
# Operators (from ED-Phys-15/17)
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
# Peak / Basin / Horizon tracking (from ED-Phys-17, fixed thresholds)
# ---------------------------------------------------------------------------
def find_peaks_1d(rho, min_prominence=0.01):
    peaks = []
    for i in range(1, len(rho) - 1):
        if rho[i] > rho[i - 1] and rho[i] > rho[i + 1]:
            prom = rho[i] - min(rho[i - 1], rho[i + 1])
            if prom >= min_prominence:
                peaks.append({"pos": i, "height": float(rho[i]),
                              "prominence": float(prom)})
    if len(rho) > 2:
        if rho[0] > rho[-1] and rho[0] > rho[1]:
            prom = rho[0] - min(rho[-1], rho[1])
            if prom >= min_prominence:
                peaks.append({"pos": 0, "height": float(rho[0]),
                              "prominence": float(prom)})
    return sorted(peaks, key=lambda p: p["pos"])


def find_basins_1d(rho, min_depth=0.01):
    basins = []
    for i in range(1, len(rho) - 1):
        if rho[i] < rho[i - 1] and rho[i] < rho[i + 1]:
            depth = max(rho[i - 1], rho[i + 1]) - rho[i]
            if depth >= min_depth:
                basins.append({"pos": i, "depth": float(rho[i]),
                               "depth_contrast": float(depth)})
    return sorted(basins, key=lambda b: b["pos"])


def find_horizons_1d(rho, rho_max, threshold=0.9):
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


# ---------------------------------------------------------------------------
# Initial conditions
# ---------------------------------------------------------------------------
def ic_peak_on_flat(N, rho_star, peak_height, peak_pos, peak_sigma):
    x = np.arange(N, dtype=np.float64)
    rho = np.full(N, rho_star, dtype=np.float64)
    rho += peak_height * np.exp(-((x - peak_pos) ** 2) / (2 * peak_sigma ** 2))
    return rho


def ic_two_peaks(N, rho_star, h1, p1, s1, h2, p2, s2):
    x = np.arange(N, dtype=np.float64)
    rho = np.full(N, rho_star, dtype=np.float64)
    rho += h1 * np.exp(-((x - p1) ** 2) / (2 * s1 ** 2))
    rho += h2 * np.exp(-((x - p2) ** 2) / (2 * s2 ** 2))
    return rho


def ic_multi_peak(N, rho_star, n_peaks, peak_height, peak_sigma, seed=42):
    rng = np.random.default_rng(seed)
    x = np.arange(N, dtype=np.float64)
    rho = np.full(N, rho_star, dtype=np.float64)
    positions = rng.choice(N, n_peaks, replace=False)
    for p in positions:
        h = peak_height * (0.5 + rng.random())
        rho += h * np.exp(-((x - p) ** 2) / (2 * peak_sigma ** 2))
    return rho, sorted(positions.tolist())


def ic_near_horizon(N, rho_star, rho_max, peak_height, peak_pos, peak_sigma):
    x = np.arange(N, dtype=np.float64)
    rho = np.full(N, rho_star, dtype=np.float64)
    rho += peak_height * np.exp(-((x - peak_pos) ** 2) / (2 * peak_sigma ** 2))
    return np.clip(rho, 0, rho_max - 0.1)


def ic_peak_on_wave(N, rho_star, wave_A, wave_n, peak_height, peak_pos, peak_sigma):
    x = np.arange(N, dtype=np.float64)
    rho = rho_star + wave_A * np.sin(2 * np.pi * wave_n * x / N)
    rho += peak_height * np.exp(-((x - peak_pos) ** 2) / (2 * peak_sigma ** 2))
    return rho


def ic_2d_random(Nx, rho_star, amplitude, n_modes, seed=42):
    rng = np.random.default_rng(seed)
    x = np.arange(Nx, dtype=np.float64)
    X, Y = np.meshgrid(x, x)
    rho = np.full((Nx, Nx), rho_star, dtype=np.float64)
    for _ in range(n_modes):
        nx = rng.integers(1, Nx // 4)
        ny = rng.integers(1, Nx // 4)
        phi = rng.uniform(0, 2 * np.pi)
        A = amplitude * (0.5 + rng.random())
        rho += A * np.sin(2 * np.pi * nx * X / Nx + phi) * np.cos(
            2 * np.pi * ny * Y / Nx
        )
    return rho


def ic_2d_peaks(Nx, rho_star, wave_A, wave_n, peaks_list, peak_sigma):
    x = np.arange(Nx, dtype=np.float64)
    X, Y = np.meshgrid(x, x)
    rho = rho_star + wave_A * np.sin(2 * np.pi * wave_n * X / Nx)
    for px, py, ph in peaks_list:
        rho += ph * np.exp(-((X - px) ** 2 + (Y - py) ** 2) / (2 * peak_sigma ** 2))
    return rho


# ---------------------------------------------------------------------------
# Hybrid Simulator
# ---------------------------------------------------------------------------
def simulate_hybrid(
    params: EDParams,
    osc: OscParams,
    hybrid: HybridParams,
    initial_rho: np.ndarray,
    label: str = "",
    snapshot_interval: int = 1000,
    track_peaks: bool = True,
    initial_v: np.ndarray | None = None,
) -> dict:
    """
    Hybrid parabolic + oscillator simulator.

    Update rule:
        drho/dt = D * RHS + H * v
        dv/dt   = (1/tau) * (RHS - zeta * v)

    D=1,H=0 -> pure parabolic
    D=0,H=1 -> pure oscillatory
    """
    rho = initial_rho.astype(np.float64).copy()
    eta = compute_timestep(params, osc)
    v = initial_v.copy() if initial_v is not None else np.zeros_like(rho)

    D = hybrid.D
    H = hybrid.H

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

        # Hybrid update
        dv = (1.0 / osc.tau) * (rhs - osc.zeta * v)
        v_new = v + eta * dv
        drho = D * rhs + H * v_new
        rho_new = rho + eta * drho

        below = rho_new < 0.0
        if np.any(below):
            positivity_clips += int(np.sum(below))
            rho_new = np.maximum(rho_new, 0.0)

        if t % diag_interval == 0 or t == params.n_steps - 1:
            V = potential_sy2(rho_new, params.alpha, params.gamma_exp,
                              osc.rho_star, osc.rho_0)
            M_star = params.M_0 * (1.0 - osc.rho_star / params.rho_max) ** params.n_mob
            gs = discrete_grad_squared(np.maximum(rho_new, params.eps),
                                       params.dx, params.boundary)
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
                                 "peaks": peaks[:10]})
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
        "D": D, "H": H,
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
# Analysis helpers (from ED-Phys-17)
# ---------------------------------------------------------------------------
def analyze_peak_dynamics(peak_history, rho_star):
    if not peak_history or len(peak_history) < 5:
        return {"n_peaks_initial": 0, "n_peaks_final": 0, "peak_oscillations": 0,
                "merging_events": 0, "tallest_initial": rho_star,
                "tallest_final": rho_star, "tallest_max": rho_star,
                "tallest_min": rho_star, "peak_pos_drift": 0.0,
                "n_peaks_oscillates": False}

    n_initial = peak_history[0]["n_peaks"]
    n_final = peak_history[-1]["n_peaks"]
    n_series = [ph["n_peaks"] for ph in peak_history]
    n_min = min(n_series)
    n_max = max(n_series)

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
    h_osc = 0
    for i in range(1, len(h_arr) - 1):
        if (h_arr[i] > h_arr[i - 1] and h_arr[i] > h_arr[i + 1]) or \
           (h_arr[i] < h_arr[i - 1] and h_arr[i] < h_arr[i + 1]):
            h_osc += 1
    h_osc //= 2

    pos_arr = np.array(pos_series)
    valid = pos_arr >= 0
    pos_drift = float(np.std(pos_arr[valid])) if np.sum(valid) > 2 else 0.0

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
        "tallest_initial": float(h_arr[0]),
        "tallest_final": float(h_arr[-1]),
        "tallest_max": float(np.max(h_arr)),
        "tallest_min": float(np.min(h_arr)),
        "peak_pos_drift": pos_drift,
        "merging_events": merges,
        "n_peaks_oscillates": n_max > n_min + 1,
    }


def analyze_basins(basin_history, rho_star):
    if not basin_history or len(basin_history) < 5:
        return {"n_basins_initial": 0, "n_basins_final": 0}
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
        "deepest_initial": float(d_arr[0]),
        "deepest_final": float(d_arr[-1]),
        "deepest_min": float(np.min(d_arr)),
        "basin_oscillates": float(np.std(d_arr)) > 0.5,
    }


def analyze_horizons(horizon_history):
    if not horizon_history:
        return {"horizon_ever_formed": False, "horizon_max": 0}
    frac_series = [hh.get("fraction", 0) for hh in horizon_history]
    n_series = [hh.get("n_sites", 0) for hh in horizon_history]
    # Compute horizon lifetime: consecutive steps with horizon
    lifetime = 0
    max_run = 0
    for n in n_series:
        if n > 0:
            lifetime += 1
            max_run = max(max_run, lifetime)
        else:
            lifetime = 0
    return {
        "horizon_initial": n_series[0],
        "horizon_final": n_series[-1],
        "horizon_max": max(n_series),
        "horizon_fraction_max": float(max(frac_series)),
        "horizon_ever_formed": max(n_series) > 0,
        "horizon_lifetime_samples": max_run,
    }


def _compact(res, rho_star=50.0):
    d = res["diagnostics"]
    pd = analyze_peak_dynamics(res["peak_history"], rho_star)
    bd = analyze_basins(res["basin_history"], rho_star)
    hd = analyze_horizons(res["horizon_history"])
    return {
        "label": res["label"],
        "D": res["D"], "H": res["H"],
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
        "v_rms_final": d["v_rms"][-1] if d["v_rms"] else None,
        "peak_dynamics": pd,
        "basin_dynamics": bd,
        "horizon_dynamics": hd,
    }


def _compact_2d(res):
    d = res["diagnostics"]
    return {
        "label": res["label"],
        "D": res["D"], "H": res["H"],
        "blew_up": res["blew_up"],
        "positivity_clips": res["positivity_clips"],
        "rho_mean_initial": d["rho_mean"][0] if d["rho_mean"] else None,
        "rho_mean_final": d["rho_mean"][-1] if d["rho_mean"] else None,
        "rho_std_initial": d["rho_std"][0] if d["rho_std"] else None,
        "rho_std_final": d["rho_std"][-1] if d["rho_std"] else None,
        "rho_mean_drift": abs(d["rho_mean"][-1] - 50.0) if d["rho_mean"] else None,
        "E_initial": d["E_total"][0] if d["E_total"] else None,
        "E_final": d["E_total"][-1] if d["E_total"] else None,
        "elapsed_s": res["elapsed_s"],
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


# ---------------------------------------------------------------------------
# Hybrid regimes
# ---------------------------------------------------------------------------
REGIMES = {
    "osc_dom": HybridParams(D=0.2, H=0.8),
    "balanced": HybridParams(D=0.5, H=0.5),
    "par_dom": HybridParams(D=0.8, H=0.2),
    "pure_osc": HybridParams(D=0.0, H=1.0),
    "pure_par": HybridParams(D=1.0, H=0.0),
}


# ===================================================================
# EXPERIMENTS
# ===================================================================
def run_all_experiments(results_dir):
    os.makedirs(results_dir, exist_ok=True)
    all_results = {}

    N = 512
    osc = OscParams(tau=100, zeta=0.5, rho_star=50, rho_0=0.5)

    print("=" * 70)
    print("ED-Phys-18: Hybrid Cosmology (Oscillator + Parabolic)")
    print("=" * 70)

    # ===================================================================
    # EXP 1: SINGLE-PEAK HYBRID DYNAMICS (TASK 2)
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXP 1: Single-Peak Hybrid Dynamics")
    print("=" * 70)
    exp1 = {}
    params = EDParams(grid_size=N, n_steps=50000, dimensions=1)

    for regime_name, hybrid in REGIMES.items():
        rho0 = ic_peak_on_flat(N, 50.0, 30.0, N // 2, 15.0)
        res = simulate_hybrid(params, osc, hybrid, rho0,
                               label=f"single_peak_{regime_name}")
        exp1[regime_name] = _compact(res)
        pd = exp1[regime_name]["peak_dynamics"]
        hd = exp1[regime_name]["horizon_dynamics"]
        print(f"  {regime_name:10s} (D={hybrid.D:.1f},H={hybrid.H:.1f}): "
              f"peak {pd['tallest_initial']:.1f}->{pd['tallest_final']:.1f}, "
              f"osc={pd['peak_oscillations']}, merges={pd['merging_events']}, "
              f"clips={res['positivity_clips']}, "
              f"std_f={exp1[regime_name]['rho_std_final']:.6f}")

    all_results["exp1_single_peak"] = exp1

    # ===================================================================
    # EXP 2: MULTI-PEAK HYBRID COSMOLOGY (TASK 3)
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXP 2: Multi-Peak Hybrid Cosmology")
    print("=" * 70)
    exp2 = {}
    params_long = EDParams(grid_size=N, n_steps=80000, dimensions=1)

    for regime_name in ["osc_dom", "balanced", "par_dom"]:
        hybrid = REGIMES[regime_name]

        # 2 peaks
        rho0 = ic_two_peaks(N, 50.0, 25.0, 150, 15.0, 25.0, 350, 15.0)
        res = simulate_hybrid(params_long, osc, hybrid, rho0,
                               label=f"2peaks_{regime_name}")
        key = f"2peaks_{regime_name}"
        exp2[key] = _compact(res)
        pd = exp2[key]["peak_dynamics"]
        print(f"  2-peak {regime_name:10s}: peaks {pd['n_peaks_initial']}->"
              f"{pd['n_peaks_final']}, osc={pd['peak_oscillations']}, "
              f"merges={pd['merging_events']}")

        # 5 peaks
        rho0, _ = ic_multi_peak(N, 50.0, 5, 20.0, 12.0, seed=42)
        res = simulate_hybrid(params_long, osc, hybrid, rho0,
                               label=f"5peaks_{regime_name}")
        key = f"5peaks_{regime_name}"
        exp2[key] = _compact(res)
        pd = exp2[key]["peak_dynamics"]
        print(f"  5-peak {regime_name:10s}: peaks {pd['n_peaks_initial']}->"
              f"{pd['n_peaks_final']}, osc={pd['peak_oscillations']}, "
              f"merges={pd['merging_events']}")

        # 10 peaks
        rho0, _ = ic_multi_peak(N, 50.0, 10, 15.0, 10.0, seed=123)
        res = simulate_hybrid(params_long, osc, hybrid, rho0,
                               label=f"10peaks_{regime_name}")
        key = f"10peaks_{regime_name}"
        exp2[key] = _compact(res)
        pd = exp2[key]["peak_dynamics"]
        print(f"  10-peak {regime_name:10s}: peaks {pd['n_peaks_initial']}->"
              f"{pd['n_peaks_final']}, osc={pd['peak_oscillations']}, "
              f"merges={pd['merging_events']}")

    all_results["exp2_multi_peak"] = exp2

    # ===================================================================
    # EXP 3: HYBRID HORIZON BEHAVIOR (TASK 4)
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXP 3: Hybrid Horizon Behavior")
    print("=" * 70)
    exp3 = {}
    params_hor = EDParams(grid_size=N, n_steps=50000, dimensions=1)

    for regime_name in ["pure_osc", "osc_dom", "balanced", "par_dom", "pure_par"]:
        hybrid = REGIMES[regime_name]
        rho0 = ic_near_horizon(N, 50.0, 100.0, 45.0, N // 2, 15.0)
        res = simulate_hybrid(params_hor, osc, hybrid, rho0,
                               label=f"horizon_{regime_name}")
        exp3[regime_name] = _compact(res)
        hd = exp3[regime_name]["horizon_dynamics"]
        pd = exp3[regime_name]["peak_dynamics"]
        print(f"  {regime_name:10s}: peak {pd['tallest_initial']:.1f}->"
              f"{pd['tallest_final']:.1f}, "
              f"hor_max={hd['horizon_max']}, "
              f"hor_life={hd['horizon_lifetime_samples']}, "
              f"clips={res['positivity_clips']}")

    all_results["exp3_horizon"] = exp3

    # ===================================================================
    # EXP 4: HYBRID INFLATION AND THINNING (TASK 5)
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXP 4: Hybrid Inflation and Thinning")
    print("=" * 70)
    exp4 = {}
    params_inf = EDParams(grid_size=N, n_steps=50000, dimensions=1)

    # 4a: Peak at wave crest (upward curvature -> inflation)
    for regime_name in ["osc_dom", "balanced", "par_dom"]:
        hybrid = REGIMES[regime_name]
        rho0 = ic_peak_on_wave(N, 50.0, 10.0, 2, 20.0, 64, 15.0)
        res = simulate_hybrid(params_inf, osc, hybrid, rho0,
                               label=f"inflation_{regime_name}")
        key = f"inflation_{regime_name}"
        exp4[key] = _compact(res)
        pd = exp4[key]["peak_dynamics"]
        print(f"  Inflation {regime_name:10s}: peak {pd['tallest_initial']:.1f}->"
              f"{pd['tallest_final']:.1f}, osc={pd['peak_oscillations']}")

    # 4b: Peak at wave trough (downward curvature -> thinning)
    for regime_name in ["osc_dom", "balanced", "par_dom"]:
        hybrid = REGIMES[regime_name]
        rho0 = ic_peak_on_wave(N, 50.0, 10.0, 2, 20.0, 192, 15.0)
        res = simulate_hybrid(params_inf, osc, hybrid, rho0,
                               label=f"thinning_{regime_name}")
        key = f"thinning_{regime_name}"
        exp4[key] = _compact(res)
        pd = exp4[key]["peak_dynamics"]
        print(f"  Thinning  {regime_name:10s}: peak {pd['tallest_initial']:.1f}->"
              f"{pd['tallest_final']:.1f}, osc={pd['peak_oscillations']}")

    # 4c: Phase-dependent hybrid evolution — peak at node
    for regime_name in ["osc_dom", "balanced", "par_dom"]:
        hybrid = REGIMES[regime_name]
        rho0 = ic_peak_on_wave(N, 50.0, 10.0, 2, 20.0, 128, 15.0)
        res = simulate_hybrid(params_inf, osc, hybrid, rho0,
                               label=f"node_{regime_name}")
        key = f"node_{regime_name}"
        exp4[key] = _compact(res)
        pd = exp4[key]["peak_dynamics"]
        print(f"  Node      {regime_name:10s}: peak {pd['tallest_initial']:.1f}->"
              f"{pd['tallest_final']:.1f}, osc={pd['peak_oscillations']}")

    all_results["exp4_inflation_thinning"] = exp4

    # ===================================================================
    # EXP 5: 2D HYBRID COSMOLOGY (TASK 6)
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXP 5: 2D Hybrid Cosmology")
    print("=" * 70)
    exp5 = {}
    Nx = 128
    params_2d = EDParams(grid_size=Nx, n_steps=20000, dimensions=2)

    for regime_name in ["osc_dom", "balanced", "par_dom"]:
        hybrid = REGIMES[regime_name]

        # 5a: Random initial field
        rho0_2d = ic_2d_random(Nx, 50.0, 3.0, 15, seed=42)
        res = simulate_hybrid(params_2d, osc, hybrid, rho0_2d,
                               label=f"2d_random_{regime_name}",
                               snapshot_interval=2000, track_peaks=False)
        key = f"random_{regime_name}"
        exp5[key] = _compact_2d(res)
        np.save(os.path.join(results_dir, f"2d_random_{regime_name}.npy"),
                res["final_rho"])
        print(f"  2D random {regime_name:10s}: drift={exp5[key]['rho_mean_drift']:.6f}, "
              f"std {exp5[key]['rho_std_initial']:.3f}->"
              f"{exp5[key]['rho_std_final']:.3f}, "
              f"clips={res['positivity_clips']}")

        # 5b: Directional oscillatory background + peaks
        rho0_2d = ic_2d_peaks(Nx, 50.0, 8.0, 4, [(64, 64, 20.0)], 10.0)
        res = simulate_hybrid(params_2d, osc, hybrid, rho0_2d,
                               label=f"2d_dir_{regime_name}",
                               snapshot_interval=2000, track_peaks=False)
        key = f"directional_{regime_name}"
        exp5[key] = _compact_2d(res)
        print(f"  2D dir    {regime_name:10s}: drift={exp5[key]['rho_mean_drift']:.6f}, "
              f"std {exp5[key]['rho_std_initial']:.3f}->"
              f"{exp5[key]['rho_std_final']:.3f}, "
              f"clips={res['positivity_clips']}")

        # 5c: Radial peak only
        rho0_2d = ic_2d_peaks(Nx, 50.0, 0.0, 1, [(64, 64, 30.0)], 12.0)
        res = simulate_hybrid(params_2d, osc, hybrid, rho0_2d,
                               label=f"2d_radial_{regime_name}",
                               snapshot_interval=2000, track_peaks=False)
        key = f"radial_{regime_name}"
        exp5[key] = _compact_2d(res)
        print(f"  2D radial {regime_name:10s}: drift={exp5[key]['rho_mean_drift']:.6f}, "
              f"std {exp5[key]['rho_std_initial']:.3f}->"
              f"{exp5[key]['rho_std_final']:.3f}, "
              f"clips={res['positivity_clips']}")

    all_results["exp5_2d_hybrid"] = exp5

    # ===================================================================
    # EXP 6: HYBRID PHASE DIAGRAM (TASK 7)
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXP 6: Hybrid Phase Diagram")
    print("=" * 70)
    exp6 = {}
    params_phase = EDParams(grid_size=N, n_steps=50000, dimensions=1)

    # Sweep D from 0.0 to 1.0 in steps of 0.1
    D_values = np.arange(0.0, 1.01, 0.1)
    phase_data = []

    for D_val in D_values:
        H_val = 1.0 - D_val
        hybrid = HybridParams(D=float(D_val), H=float(H_val))

        # Use 5-peak IC as standard test
        rho0, _ = ic_multi_peak(N, 50.0, 5, 20.0, 12.0, seed=42)
        res = simulate_hybrid(params_phase, osc, hybrid, rho0,
                               label=f"phase_D{D_val:.1f}")
        c = _compact(res)
        pd = c["peak_dynamics"]
        hd = c["horizon_dynamics"]

        # Relaxation rate: how fast std drops
        stds = res["diagnostics"]["rho_std"]
        if len(stds) > 10:
            half_std = stds[0] / 2.0
            half_time = params_phase.n_steps
            for idx, s in enumerate(stds):
                if s <= half_std:
                    half_time = idx * max(1, params_phase.n_steps // 4000)
                    break
        else:
            half_time = params_phase.n_steps

        entry = {
            "D": float(D_val), "H": float(H_val),
            "peak_oscillations": pd["peak_oscillations"],
            "merging_events": pd["merging_events"],
            "n_peaks_final": pd["n_peaks_final"],
            "tallest_max": pd["tallest_max"],
            "rho_std_final": c["rho_std_final"],
            "E_final": c["E_final"],
            "positivity_clips": c["positivity_clips"],
            "half_life_steps": half_time,
            "horizon_max": hd["horizon_max"],
            "horizon_lifetime": hd["horizon_lifetime_samples"],
            "blew_up": c["blew_up"],
        }
        phase_data.append(entry)
        print(f"  D={D_val:.1f} H={H_val:.1f}: osc={pd['peak_oscillations']}, "
              f"merges={pd['merging_events']}, "
              f"half_life={half_time}, "
              f"clips={c['positivity_clips']}, "
              f"std_f={c['rho_std_final']:.6f}")

    exp6["phase_sweep"] = phase_data

    # Also run horizon sweep
    print("\n  --- Horizon Phase Sweep ---")
    horizon_sweep = []
    for D_val in D_values:
        H_val = 1.0 - D_val
        hybrid = HybridParams(D=float(D_val), H=float(H_val))
        rho0 = ic_near_horizon(N, 50.0, 100.0, 45.0, N // 2, 15.0)
        res = simulate_hybrid(params_phase, osc, hybrid, rho0,
                               label=f"hor_D{D_val:.1f}")
        c = _compact(res)
        hd = c["horizon_dynamics"]
        pd = c["peak_dynamics"]
        entry = {
            "D": float(D_val), "H": float(H_val),
            "horizon_max": hd["horizon_max"],
            "horizon_lifetime": hd["horizon_lifetime_samples"],
            "horizon_ever_formed": hd["horizon_ever_formed"],
            "peak_oscillations": pd["peak_oscillations"],
            "tallest_final": pd["tallest_final"],
            "positivity_clips": c["positivity_clips"],
        }
        horizon_sweep.append(entry)
        print(f"  D={D_val:.1f} H={H_val:.1f}: hor_max={hd['horizon_max']}, "
              f"hor_life={hd['horizon_lifetime_samples']}, "
              f"osc={pd['peak_oscillations']}, "
              f"clips={c['positivity_clips']}")

    exp6["horizon_sweep"] = horizon_sweep

    all_results["exp6_phase_diagram"] = exp6

    # ===================================================================
    # Save
    # ===================================================================
    results_path = os.path.join(results_dir, "hybrid_results.json")
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
        if isinstance(exp_data, dict):
            for cfg, data in exp_data.items():
                if isinstance(data, dict) and "peak_dynamics" in data:
                    pd = data["peak_dynamics"]
                    print(f"  {cfg:30s}: D={data.get('D','?')} H={data.get('H','?')} "
                          f"peaks {pd['n_peaks_initial']}->{pd['n_peaks_final']}  "
                          f"osc={pd['peak_oscillations']}  "
                          f"merges={pd['merging_events']}  "
                          f"clips={data.get('positivity_clips','?')}")
                elif isinstance(data, list):
                    for entry in data[:3]:
                        print(f"  D={entry.get('D','?'):.1f}: "
                              f"osc={entry.get('peak_oscillations','?')} "
                              f"merges={entry.get('merging_events','?')}")
                    if len(data) > 3:
                        print(f"  ... ({len(data)} entries total)")
