"""
ED-Phys-14: Oscillatory Participation with Restoring Penalty
=============================================================

Combines:
  - Hyperbolic time evolution (ED-Phys-13): tau*d²rho/dt² + zeta*drho/dt = RHS
  - Symmetric restoring penalty (ED-Phys-12): P_SY = alpha*gamma*(rho-rho_star)/(rho+rho_0)

The symmetric penalty provides:
  - Zero drain at rho = rho_star (true equilibrium)
  - Positive restoring force (P_SY' > 0 at rho_star)
  - K_eff > 0 at ALL k, including k=0

This enables oscillatory dynamics at ALL scales if Q > 0.5.

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
    """Standard ED parameters."""

    alpha: float = 0.1
    gamma_exp: float = 0.5
    M_0: float = 1.0
    rho_max: float = 100.0
    n_mob: int = 2
    dx: float = 1.0
    n_steps: int = 20000
    dimensions: int = 1
    grid_size: int = 512
    boundary: str = "periodic"
    eps: float = 1e-10
    cfl_safety: float = 0.4
    seed: int = 42


@dataclass
class OscillatorParams:
    """Parameters for hyperbolic + symmetric mode."""

    tau: float = 500.0        # inertial timescale
    zeta: float = 1.0         # damping coefficient
    rho_star: float = 50.0    # restoring equilibrium density
    rho_0: float = 0.5        # soft-floor shift (in denominator)


# ---------------------------------------------------------------------------
# Operators
# ---------------------------------------------------------------------------
def _pad(rho: np.ndarray, boundary: str) -> np.ndarray:
    """Pad array for boundary conditions."""
    if rho.ndim == 1:
        if boundary == "periodic":
            return np.concatenate(([rho[-1]], rho, [rho[0]]))
        elif boundary == "reflecting":
            return np.concatenate(([rho[0]], rho, [rho[-1]]))
        else:
            return np.concatenate(([0.0], rho, [0.0]))
    else:
        if boundary == "periodic":
            return np.pad(rho, 1, mode="wrap")
        elif boundary == "reflecting":
            return np.pad(rho, 1, mode="edge")
        else:
            return np.pad(rho, 1, mode="constant", constant_values=0.0)


def discrete_laplacian(rho: np.ndarray, dx: float, boundary: str) -> np.ndarray:
    dx2 = dx * dx
    p = _pad(rho, boundary)
    if rho.ndim == 1:
        return (p[2:] - 2.0 * p[1:-1] + p[:-2]) / dx2
    else:
        return (
            p[2:, 1:-1] + p[:-2, 1:-1] + p[1:-1, 2:] + p[1:-1, :-2]
            - 4.0 * p[1:-1, 1:-1]
        ) / dx2


def discrete_grad_squared(rho: np.ndarray, dx: float, boundary: str) -> np.ndarray:
    p = _pad(rho, boundary)
    two_dx = 2.0 * dx
    if rho.ndim == 1:
        gx = (p[2:] - p[:-2]) / two_dx
        return gx * gx
    else:
        gx = (p[2:, 1:-1] - p[:-2, 1:-1]) / two_dx
        gy = (p[1:-1, 2:] - p[1:-1, :-2]) / two_dx
        return gx * gx + gy * gy


def mobility(rho: np.ndarray, M_0: float, rho_max: float, n_mob: int):
    ratio = np.clip(1.0 - rho / rho_max, 0.0, None)
    M = M_0 * ratio**n_mob
    M_prime = -M_0 * (n_mob / rho_max) * ratio ** max(n_mob - 1, 0)
    return M, M_prime


# ---------------------------------------------------------------------------
# Penalty functions
# ---------------------------------------------------------------------------
def penalty_symmetric(
    rho: np.ndarray,
    alpha: float,
    gamma: float,
    rho_star: float,
    rho_0: float = 0.5,
    eps: float = 1e-10,
) -> np.ndarray:
    """Symmetric restoring penalty: P(rho) = alpha*gamma*(rho-rho_star)/(rho+rho_0).

    - Zero at rho = rho_star (no drain at equilibrium)
    - Positive above rho_star (drains)
    - Negative below rho_star (restores)
    - Bounded as rho->0: P(0) = -alpha*gamma*rho_star/rho_0
    """
    rho_safe = np.maximum(rho, eps)
    return alpha * gamma * (rho_safe - rho_star) / (rho_safe + rho_0)


def penalty_symmetric_derivative(
    rho_star: float, rho_0: float, alpha: float, gamma: float
) -> float:
    """Analytical penalty derivative at rho_star: P'(rho_star) = alpha*gamma/(rho_star+rho_0)."""
    return alpha * gamma / (rho_star + rho_0)


def penalty_soft_floor(
    rho: np.ndarray, alpha: float, gamma: float, rho_0: float = 0.5, eps: float = 1e-10
) -> np.ndarray:
    """Soft-floor penalty (for parabolic baseline comparison)."""
    rho_safe = np.maximum(rho, eps)
    return alpha * gamma * (rho_safe + rho_0) ** (gamma - 1.0)


# ---------------------------------------------------------------------------
# RHS computation
# ---------------------------------------------------------------------------
def compute_rhs_symmetric(
    rho: np.ndarray, params: EDParams, osc: OscillatorParams
) -> np.ndarray:
    """RHS with symmetric restoring penalty."""
    rho_safe = np.maximum(rho, params.eps)
    lap = discrete_laplacian(rho_safe, params.dx, params.boundary)
    grad_sq = discrete_grad_squared(rho_safe, params.dx, params.boundary)
    M, M_prime = mobility(rho_safe, params.M_0, params.rho_max, params.n_mob)
    pen = penalty_symmetric(
        rho_safe, params.alpha, params.gamma_exp, osc.rho_star, osc.rho_0, params.eps
    )
    return M * lap + M_prime * grad_sq - pen


def compute_rhs_softfloor(
    rho: np.ndarray, params: EDParams, rho_0: float = 0.5
) -> np.ndarray:
    """RHS with soft-floor penalty (for baseline comparison)."""
    rho_safe = np.maximum(rho, params.eps)
    lap = discrete_laplacian(rho_safe, params.dx, params.boundary)
    grad_sq = discrete_grad_squared(rho_safe, params.dx, params.boundary)
    M, M_prime = mobility(rho_safe, params.M_0, params.rho_max, params.n_mob)
    pen = penalty_soft_floor(rho_safe, params.alpha, params.gamma_exp, rho_0, params.eps)
    return M * lap + M_prime * grad_sq - pen


# ---------------------------------------------------------------------------
# Timestep
# ---------------------------------------------------------------------------
def compute_timestep(params: EDParams, osc: OscillatorParams, time_mode: str) -> float:
    d = params.dimensions
    dx = params.dx
    # Diffusion CFL
    eta_diff = params.cfl_safety * dx**2 / (2.0 * d * params.M_0)
    if time_mode == "parabolic":
        # Penalty bound for symmetric
        P_max = params.alpha * params.gamma_exp * max(
            abs(osc.rho_star / osc.rho_0), 1.0
        )
        eta_pen = 0.1 / max(P_max, 1e-10)
        return min(eta_diff, eta_pen)
    else:
        # Wave CFL
        c_max = np.sqrt(params.M_0 / osc.tau)
        eta_wave = params.cfl_safety * dx / c_max
        # Damping stability
        eta_damp = 2.0 * osc.tau / max(osc.zeta, 1e-10)
        return min(eta_diff, eta_wave, eta_damp, 0.5)


# ---------------------------------------------------------------------------
# Main simulator
# ---------------------------------------------------------------------------
def simulate_oscillator(
    params: EDParams,
    osc: OscillatorParams,
    initial_rho: np.ndarray,
    time_mode: str = "hyperbolic",
    penalty_mode: str = "symmetric",
    snapshot_interval: int = 500,
    label: str = "",
    point_traces: list[int] | None = None,
) -> dict:
    """
    Simulator for combined hyperbolic + symmetric penalty dynamics.

    Parameters
    ----------
    time_mode : "parabolic" or "hyperbolic"
    penalty_mode : "symmetric" or "soft_floor"
    point_traces : list of grid indices to track rho(t) at specific points
    """
    rho = initial_rho.astype(np.float64).copy()
    eta = compute_timestep(params, osc, time_mode)
    v = np.zeros_like(rho)

    diag_interval = max(1, params.n_steps // 4000)

    diagnostics = {
        "rho_mean": [], "rho_max": [], "rho_min": [], "rho_std": [],
        "grad_mean": [], "v_rms": [], "v_max": [],
        "penalty_mean": [], "penalty_max": [], "penalty_min": [],
        "rho_deviation": [],  # mean |rho - rho_star|
    }
    snapshots = []
    snapshot_times = []

    # Point traces for tracking individual grid points
    traces = {}
    if point_traces:
        for idx in point_traces:
            traces[idx] = {"rho": [], "v": []}

    t_start = time.time()
    blew_up = False
    positivity_clips = 0

    for t in range(params.n_steps):
        # Safety check
        if t % 100 == 0:
            if np.any(np.isnan(rho)) or np.any(np.isinf(rho)):
                blew_up = True
                break
            if np.max(np.abs(rho)) > 1e12:
                blew_up = True
                break
            if time_mode == "hyperbolic":
                if np.any(np.isnan(v)) or np.any(np.isinf(v)):
                    blew_up = True
                    break
                if np.max(np.abs(v)) > 1e12:
                    blew_up = True
                    break

        # Compute RHS
        if penalty_mode == "symmetric":
            rhs = compute_rhs_symmetric(rho, params, osc)
        else:
            rhs = compute_rhs_softfloor(rho, params, osc.rho_0)

        # Time integration
        if time_mode == "parabolic":
            rho_new = rho + eta * rhs
            v_new = v  # unused
        else:
            dv = (1.0 / osc.tau) * (rhs - osc.zeta * v)
            v_new = v + eta * dv
            rho_new = rho + eta * v_new

        # Positivity enforcement
        below_zero = rho_new < 0.0
        if np.any(below_zero):
            positivity_clips += int(np.sum(below_zero))
            rho_new = np.maximum(rho_new, 0.0)

        # Diagnostics
        if t % diag_interval == 0 or t == params.n_steps - 1:
            rho_safe = np.maximum(rho_new, params.eps)
            pen = penalty_symmetric(
                rho_safe, params.alpha, params.gamma_exp,
                osc.rho_star, osc.rho_0, params.eps
            )
            p = _pad(rho_safe, params.boundary)
            if rho.ndim == 1:
                gx = (p[2:] - p[:-2]) / (2.0 * params.dx)
                grad_mag = np.abs(gx)
            else:
                gx = (p[2:, 1:-1] - p[:-2, 1:-1]) / (2.0 * params.dx)
                gy = (p[1:-1, 2:] - p[1:-1, :-2]) / (2.0 * params.dx)
                grad_mag = np.sqrt(gx**2 + gy**2)

            diagnostics["rho_mean"].append(float(np.mean(rho_new)))
            diagnostics["rho_max"].append(float(np.max(rho_new)))
            diagnostics["rho_min"].append(float(np.min(rho_new)))
            diagnostics["rho_std"].append(float(np.std(rho_new)))
            diagnostics["grad_mean"].append(float(np.mean(grad_mag)))
            diagnostics["penalty_mean"].append(float(np.mean(pen)))
            diagnostics["penalty_max"].append(float(np.max(pen)))
            diagnostics["penalty_min"].append(float(np.min(pen)))
            diagnostics["rho_deviation"].append(
                float(np.mean(np.abs(rho_new - osc.rho_star)))
            )
            if time_mode == "hyperbolic":
                diagnostics["v_rms"].append(float(np.sqrt(np.mean(v_new**2))))
                diagnostics["v_max"].append(float(np.max(np.abs(v_new))))
            else:
                diagnostics["v_rms"].append(0.0)
                diagnostics["v_max"].append(0.0)

        # Point traces
        if point_traces and (t % diag_interval == 0 or t == params.n_steps - 1):
            for idx in point_traces:
                if rho.ndim == 1 and idx < len(rho_new):
                    traces[idx]["rho"].append(float(rho_new[idx]))
                    traces[idx]["v"].append(
                        float(v_new[idx]) if time_mode == "hyperbolic" else 0.0
                    )

        # Snapshots
        if t % snapshot_interval == 0 or t == params.n_steps - 1:
            snapshots.append(rho_new.copy())
            snapshot_times.append(t)

        rho = rho_new
        if time_mode == "hyperbolic":
            v = v_new

    elapsed = time.time() - t_start

    return {
        "label": label,
        "time_mode": time_mode,
        "penalty_mode": penalty_mode,
        "tau": osc.tau,
        "zeta": osc.zeta,
        "rho_star": osc.rho_star,
        "rho_0": osc.rho_0,
        "eta": eta,
        "n_steps": params.n_steps,
        "blew_up": blew_up,
        "steps_completed": t + 1 if blew_up else params.n_steps,
        "elapsed_s": round(elapsed, 3),
        "positivity_clips": positivity_clips,
        "diagnostics": diagnostics,
        "traces": traces,
        "snapshots": snapshots,
        "snapshot_times": snapshot_times,
        "final_rho": rho,
        "final_v": v if time_mode == "hyperbolic" else None,
    }


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------
def measure_oscillation(series: list[float], skip_fraction: float = 0.05) -> dict:
    """Measure oscillatory character of a time series."""
    arr = np.array(series)
    if len(arr) < 20:
        return {"oscillations": 0, "damping_ratio": None, "period": None,
                "amplitude_initial": None, "amplitude_final": None}

    # Skip initial transient
    start = max(1, int(len(arr) * skip_fraction))
    arr = arr[start:]

    # Find peaks (local maxima)
    peaks_idx = []
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            peaks_idx.append(i)

    # Find troughs (local minima)
    troughs_idx = []
    for i in range(1, len(arr) - 1):
        if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
            troughs_idx.append(i)

    n_oscillations = min(len(peaks_idx), len(troughs_idx))

    period = None
    damping_ratio = None
    amplitude_initial = None
    amplitude_final = None

    if len(peaks_idx) >= 2:
        spacings = np.diff(peaks_idx)
        period = float(np.mean(spacings))

    if len(peaks_idx) >= 3:
        peak_vals = arr[peaks_idx]
        # Damping from successive peak amplitudes (relative to mean)
        mean_val = np.mean(arr)
        amps = np.abs(peak_vals - mean_val)
        if len(amps) >= 2 and amps[0] > 1e-15:
            ratios = amps[1:] / np.maximum(amps[:-1], 1e-15)
            valid_ratios = ratios[(ratios > 0) & (ratios < 2.0)]
            if len(valid_ratios) > 0:
                mean_ratio = float(np.mean(valid_ratios))
                if 0 < mean_ratio < 1:
                    damping_ratio = -np.log(mean_ratio)

        amplitude_initial = float(amps[0]) if len(amps) > 0 else None
        amplitude_final = float(amps[-1]) if len(amps) > 0 else None

    return {
        "oscillations": n_oscillations,
        "damping_ratio": damping_ratio,
        "period": period,
        "amplitude_initial": amplitude_initial,
        "amplitude_final": amplitude_final,
        "n_peaks": len(peaks_idx),
        "n_troughs": len(troughs_idx),
    }


def measure_point_oscillation(trace_rho: list[float], rho_star: float) -> dict:
    """Measure oscillation at a single grid point."""
    arr = np.array(trace_rho)
    if len(arr) < 20:
        return {"oscillations": 0, "period": None, "damping_ratio": None}

    # Deviation from rho_star
    delta = arr - rho_star

    # Zero crossings
    signs = np.sign(delta)
    crossings = np.where(np.abs(np.diff(signs)) > 0)[0]
    n_crossings = len(crossings)

    # Oscillation count
    n_oscillations = n_crossings // 2

    # Period from zero crossings (half-period between successive crossings)
    period = None
    if len(crossings) >= 4:
        # Full period = 2 * half-period
        half_periods = np.diff(crossings)
        period = float(2.0 * np.mean(half_periods))

    # Damping from peak envelope
    peaks_idx = []
    for i in range(1, len(delta) - 1):
        if abs(delta[i]) > abs(delta[i - 1]) and abs(delta[i]) > abs(delta[i + 1]):
            peaks_idx.append(i)

    damping_ratio = None
    if len(peaks_idx) >= 3:
        peak_amps = np.abs(delta[peaks_idx])
        ratios = peak_amps[1:] / np.maximum(peak_amps[:-1], 1e-15)
        valid = ratios[(ratios > 0) & (ratios < 2.0)]
        if len(valid) > 0:
            mr = float(np.mean(valid))
            if 0 < mr < 1:
                damping_ratio = -np.log(mr)

    return {
        "oscillations": n_oscillations,
        "zero_crossings": n_crossings,
        "period": period,
        "damping_ratio": damping_ratio,
    }


# ---------------------------------------------------------------------------
# Initial conditions
# ---------------------------------------------------------------------------
def ic_uniform(N: int, rho_star: float) -> np.ndarray:
    return np.full(N, rho_star, dtype=np.float64)


def ic_perturbed(N: int, rho_star: float, epsilon: float, n_mode: int) -> np.ndarray:
    """rho = rho_star + epsilon * sin(2*pi*n*x/N)."""
    x = np.arange(N, dtype=np.float64)
    return rho_star + epsilon * np.sin(2.0 * np.pi * n_mode * x / N)


def ic_gaussian_perturb(
    N: int, rho_star: float, amplitude: float, sigma: float
) -> np.ndarray:
    """Gaussian perturbation around rho_star."""
    x = np.arange(N, dtype=np.float64)
    return rho_star + amplitude * np.exp(-((x - N // 2) ** 2) / (2.0 * sigma**2))


def ic_step_perturb(N: int, rho_star: float, delta: float) -> np.ndarray:
    """Half above, half below rho_star."""
    rho = np.full(N, rho_star, dtype=np.float64)
    rho[: N // 2] += delta
    rho[N // 2 :] -= delta
    return rho


def ic_far_from_star(N: int, rho_init: float) -> np.ndarray:
    """Uniform density far from rho_star."""
    return np.full(N, rho_init, dtype=np.float64)


def ic_2d_perturbed(Nx: int, rho_star: float, epsilon: float, seed: int = 42) -> np.ndarray:
    """Small random perturbations around rho_star in 2D."""
    rng = np.random.default_rng(seed)
    return rho_star + epsilon * rng.standard_normal((Nx, Nx))


def ic_2d_radial(Nx: int, rho_star: float, amplitude: float, sigma: float) -> np.ndarray:
    """Radial Gaussian perturbation in 2D."""
    cx, cy = Nx // 2, Nx // 2
    y, x = np.mgrid[0:Nx, 0:Nx]
    r2 = (x - cx) ** 2 + (y - cy) ** 2
    return rho_star + amplitude * np.exp(-r2 / (2.0 * sigma**2))


def ic_2d_directional(Nx: int, rho_star: float, amplitude: float, n_mode: int) -> np.ndarray:
    """Directional sinusoidal perturbation in 2D (x-direction only)."""
    x = np.arange(Nx, dtype=np.float64)
    row = rho_star + amplitude * np.sin(2.0 * np.pi * n_mode * x / Nx)
    return np.tile(row, (Nx, 1))


# ---------------------------------------------------------------------------
# Experiments
# ---------------------------------------------------------------------------
def run_all_experiments(results_dir: str) -> dict:
    """Run the complete ED-Phys-14 experiment suite."""
    os.makedirs(results_dir, exist_ok=True)
    all_results = {}

    # Parameter regimes
    regimes = [
        ("R1_baseline",        500,  1.0, 50),
        ("R2_strong_restoring", 500, 1.0, 20),
        ("R3_light_damping",   500,  0.5, 50),
        ("R4_max_Q",          1000,  0.5, 20),
    ]

    # Predicted Q at k=0 for reference
    print("Parameter Regimes:")
    print("-" * 70)
    for name, tau, zeta, rstar in regimes:
        P_prime = 0.1 * 0.5 / (rstar + 0.5)
        M_star = (1.0 - rstar / 100.0) ** 2
        Q_k0 = np.sqrt(tau * P_prime) / zeta
        k_test = 2.0 * np.pi * 16 / 512
        K_eff = M_star * k_test**2 + P_prime
        Q_k16 = np.sqrt(tau * K_eff) / zeta
        T_k0 = 2.0 * np.pi * np.sqrt(tau / P_prime) if P_prime > 0 else float("inf")
        print(f"  {name}: tau={tau}, zeta={zeta}, rho*={rstar}, "
              f"Q(k=0)={Q_k0:.3f}, Q(k16)={Q_k16:.3f}, "
              f"T(k=0)={T_k0:.0f} t.u. = {T_k0/0.2:.0f} steps")
    print()

    # ===================================================================
    # EXPERIMENT 1: Homogeneous Equilibrium Validation
    # ===================================================================
    print("=" * 70)
    print("EXPERIMENT 1: Homogeneous Equilibrium Validation")
    print("=" * 70)
    exp1 = {}
    params = EDParams(grid_size=256, n_steps=20000, dimensions=1)

    for name, tau, zeta, rstar in regimes:
        osc = OscillatorParams(tau=tau, zeta=zeta, rho_star=rstar)
        rho0 = ic_uniform(256, rstar)

        # Hyperbolic + symmetric
        res = simulate_oscillator(
            params, osc, rho0.copy(),
            time_mode="hyperbolic", penalty_mode="symmetric",
            label=f"hyp_sym_{name}_homogeneous"
        )
        exp1[name] = _summarize(res)
        print(f"  {name}: rho_mean {res['diagnostics']['rho_mean'][0]:.4f} -> "
              f"{res['diagnostics']['rho_mean'][-1]:.4f}, "
              f"deviation={res['diagnostics']['rho_deviation'][-1]:.6f}, "
              f"stable={not res['blew_up']}")

    # Parabolic + soft-floor baseline (rho drains)
    osc_base = OscillatorParams(rho_star=50)
    rho0 = ic_uniform(256, 50.0)
    res = simulate_oscillator(
        params, osc_base, rho0.copy(),
        time_mode="parabolic", penalty_mode="soft_floor",
        label="parabolic_sf_homogeneous"
    )
    exp1["parabolic_softfloor"] = _summarize(res)
    print(f"  Parabolic+SF: rho_mean {res['diagnostics']['rho_mean'][0]:.4f} -> "
          f"{res['diagnostics']['rho_mean'][-1]:.4f} (drains)")

    all_results["exp1_homogeneous"] = exp1

    # ===================================================================
    # EXPERIMENT 2: Local Oscillation Test (sinusoidal perturbation)
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXPERIMENT 2: Local Oscillation Test")
    print("=" * 70)
    exp2 = {}
    params = EDParams(grid_size=512, n_steps=50000, dimensions=1)

    # Test modes at different wavelengths
    test_modes = [1, 4, 16, 32, 64]  # n_mode values

    for name, tau, zeta, rstar in regimes:
        osc = OscillatorParams(tau=tau, zeta=zeta, rho_star=rstar)

        for n_mode in test_modes:
            epsilon = 5.0  # perturbation amplitude
            rho0 = ic_perturbed(512, rstar, epsilon, n_mode)
            trace_pts = [128, 256]  # track two grid points

            res = simulate_oscillator(
                params, osc, rho0.copy(),
                time_mode="hyperbolic", penalty_mode="symmetric",
                label=f"hyp_sym_{name}_mode{n_mode}",
                point_traces=trace_pts,
            )

            # Measure oscillation in rho_std
            osc_rho = measure_oscillation(res["diagnostics"]["rho_std"])
            osc_v = measure_oscillation(res["diagnostics"]["v_rms"])

            # Measure point oscillation
            pt_osc = {}
            for idx in trace_pts:
                if idx in res["traces"] and res["traces"][idx]["rho"]:
                    pt_osc[idx] = measure_point_oscillation(
                        res["traces"][idx]["rho"], rstar
                    )

            key = f"{name}_mode{n_mode}"
            exp2[key] = {
                **_summarize(res),
                "osc_rho_std": osc_rho,
                "osc_v_rms": osc_v,
                "point_oscillations": pt_osc,
            }
            print(f"  {key}: rho_osc={osc_rho['oscillations']}, "
                  f"v_osc={osc_v['oscillations']}, "
                  f"period={osc_rho.get('period', '-')}, "
                  f"pt256_osc={pt_osc.get(256, {}).get('oscillations', '-')}, "
                  f"blew_up={res['blew_up']}")

    all_results["exp2_local_oscillation"] = exp2

    # ===================================================================
    # EXPERIMENT 3: Sustained Oscillation Test
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXPERIMENT 3: Sustained Oscillation Test (100K steps)")
    print("=" * 70)
    exp3 = {}
    params = EDParams(grid_size=512, n_steps=100000, dimensions=1)

    # Use short-wavelength mode (n=32) where Q is highest
    for name, tau, zeta, rstar in regimes:
        osc = OscillatorParams(tau=tau, zeta=zeta, rho_star=rstar)
        rho0 = ic_perturbed(512, rstar, 5.0, 32)
        trace_pts = [128, 256]

        res = simulate_oscillator(
            params, osc, rho0.copy(),
            time_mode="hyperbolic", penalty_mode="symmetric",
            label=f"hyp_sym_{name}_sustained",
            point_traces=trace_pts,
        )

        osc_rho = measure_oscillation(res["diagnostics"]["rho_std"])
        pt_osc = {}
        for idx in trace_pts:
            if idx in res["traces"] and res["traces"][idx]["rho"]:
                pt_osc[idx] = measure_point_oscillation(
                    res["traces"][idx]["rho"], rstar
                )

        exp3[name] = {
            **_summarize(res),
            "osc_rho_std": osc_rho,
            "point_oscillations": pt_osc,
        }
        print(f"  {name}: rho_osc={osc_rho['oscillations']}, "
              f"damping={osc_rho.get('damping_ratio', '-')}, "
              f"amp_i={osc_rho.get('amplitude_initial', '-')}, "
              f"amp_f={osc_rho.get('amplitude_final', '-')}, "
              f"pt256_osc={pt_osc.get(256, {}).get('oscillations', '-')}, "
              f"clips={res['positivity_clips']}")

    all_results["exp3_sustained"] = exp3

    # ===================================================================
    # EXPERIMENT 4: Restoring Force Test
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXPERIMENT 4: Restoring Force Test")
    print("=" * 70)
    exp4 = {}
    params = EDParams(grid_size=256, n_steps=50000, dimensions=1)

    # Start far from rho_star: test recovery
    for name, tau, zeta, rstar in regimes:
        osc = OscillatorParams(tau=tau, zeta=zeta, rho_star=rstar)

        # Test: start at rho = 0.5*rho_star (far below)
        rho0 = ic_far_from_star(256, 0.5 * rstar)
        res_below = simulate_oscillator(
            params, osc, rho0.copy(),
            time_mode="hyperbolic", penalty_mode="symmetric",
            label=f"hyp_sym_{name}_below",
            point_traces=[128],
        )

        # Test: start at rho = 1.5*rho_star (far above)
        rho0 = ic_far_from_star(256, 1.5 * rstar)
        res_above = simulate_oscillator(
            params, osc, rho0.copy(),
            time_mode="hyperbolic", penalty_mode="symmetric",
            label=f"hyp_sym_{name}_above",
            point_traces=[128],
        )

        pt_below = measure_point_oscillation(
            res_below["traces"][128]["rho"], rstar
        ) if 128 in res_below["traces"] else {}
        pt_above = measure_point_oscillation(
            res_above["traces"][128]["rho"], rstar
        ) if 128 in res_above["traces"] else {}

        exp4[f"{name}_below"] = {
            **_summarize(res_below),
            "start_rho": 0.5 * rstar,
            "point_oscillation": pt_below,
        }
        exp4[f"{name}_above"] = {
            **_summarize(res_above),
            "start_rho": 1.5 * rstar,
            "point_oscillation": pt_above,
        }
        print(f"  {name} below (rho={0.5*rstar:.0f}): "
              f"rho_final={res_below['diagnostics']['rho_mean'][-1]:.4f}, "
              f"osc={pt_below.get('oscillations', '-')}, "
              f"clips={res_below['positivity_clips']}")
        print(f"  {name} above (rho={1.5*rstar:.0f}): "
              f"rho_final={res_above['diagnostics']['rho_mean'][-1]:.4f}, "
              f"osc={pt_above.get('oscillations', '-')}, "
              f"clips={res_above['positivity_clips']}")

    all_results["exp4_restoring"] = exp4

    # ===================================================================
    # EXPERIMENT 5: Structural Scale Test
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXPERIMENT 5: Structural Scale Test")
    print("=" * 70)
    exp5 = {}
    params = EDParams(grid_size=512, n_steps=50000, dimensions=1)

    # Lambda categories:
    # short: n=64 (lambda=8), n=32 (lambda=16)
    # mid: n=8 (lambda=64), n=4 (lambda=128)
    # long: n=1 (lambda=512), n=2 (lambda=256)
    scale_modes = {
        "short_n64": 64,
        "short_n32": 32,
        "mid_n8": 8,
        "mid_n4": 4,
        "long_n2": 2,
        "long_n1": 1,
    }

    # Use R3 (light damping, rho_star=50) for best chance of oscillation
    osc = OscillatorParams(tau=500, zeta=0.5, rho_star=50)
    for scale_name, n_mode in scale_modes.items():
        rho0 = ic_perturbed(512, 50.0, 5.0, n_mode)
        res = simulate_oscillator(
            params, osc, rho0.copy(),
            time_mode="hyperbolic", penalty_mode="symmetric",
            label=f"hyp_sym_R3_{scale_name}",
            point_traces=[256],
        )
        osc_rho = measure_oscillation(res["diagnostics"]["rho_std"])
        pt_osc = measure_point_oscillation(
            res["traces"][256]["rho"], 50.0
        ) if 256 in res["traces"] else {}

        k = 2.0 * np.pi * n_mode / 512
        lam = 512.0 / n_mode
        M_star = (1.0 - 50.0 / 100.0) ** 2
        P_prime = 0.05 / 50.5
        K_eff = M_star * k**2 + P_prime
        Q_pred = np.sqrt(500 * K_eff) / 0.5
        T_pred = 2.0 * np.pi * np.sqrt(500 / K_eff) / 0.2  # in steps

        exp5[scale_name] = {
            **_summarize(res),
            "n_mode": n_mode,
            "wavelength": lam,
            "k": k,
            "K_eff": K_eff,
            "Q_predicted": Q_pred,
            "T_predicted_steps": T_pred,
            "osc_rho_std": osc_rho,
            "point_oscillation": pt_osc,
        }
        print(f"  {scale_name} (lambda={lam:.0f}): "
              f"Q_pred={Q_pred:.2f}, T_pred={T_pred:.0f} steps, "
              f"rho_osc={osc_rho['oscillations']}, "
              f"pt_osc={pt_osc.get('oscillations', '-')}, "
              f"period_meas={osc_rho.get('period', '-')}")

    all_results["exp5_scale_test"] = exp5

    # ===================================================================
    # EXPERIMENT 6: 2D Oscillation Tests
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXPERIMENT 6: 2D Oscillation Tests")
    print("=" * 70)
    exp6 = {}
    params_2d = EDParams(grid_size=128, n_steps=20000, dimensions=2)

    # 6a: Small random perturbations
    osc = OscillatorParams(tau=500, zeta=0.5, rho_star=50)
    rho0_2d = ic_2d_perturbed(128, 50.0, 3.0, seed=42)
    res = simulate_oscillator(
        params_2d, osc, rho0_2d.copy(),
        time_mode="hyperbolic", penalty_mode="symmetric",
        label="hyp_sym_2d_random",
        snapshot_interval=2000,
    )
    osc_rho = measure_oscillation(res["diagnostics"]["rho_std"])
    exp6["random_perturb"] = {
        **_summarize(res), "osc_rho_std": osc_rho,
    }
    np.save(os.path.join(results_dir, "2d_random_rho.npy"), res["final_rho"])
    print(f"  Random perturb: rho_osc={osc_rho['oscillations']}, "
          f"rho_std {res['diagnostics']['rho_std'][0]:.4f} -> "
          f"{res['diagnostics']['rho_std'][-1]:.4f}, "
          f"clips={res['positivity_clips']}")

    # 6b: Radial perturbation
    rho0_2d = ic_2d_radial(128, 50.0, 10.0, 10.0)
    res = simulate_oscillator(
        params_2d, osc, rho0_2d.copy(),
        time_mode="hyperbolic", penalty_mode="symmetric",
        label="hyp_sym_2d_radial",
        snapshot_interval=2000,
    )
    osc_rho = measure_oscillation(res["diagnostics"]["rho_std"])
    exp6["radial_perturb"] = {
        **_summarize(res), "osc_rho_std": osc_rho,
    }
    np.save(os.path.join(results_dir, "2d_radial_rho.npy"), res["final_rho"])
    print(f"  Radial perturb: rho_osc={osc_rho['oscillations']}, "
          f"rho_std {res['diagnostics']['rho_std'][0]:.4f} -> "
          f"{res['diagnostics']['rho_std'][-1]:.4f}, "
          f"clips={res['positivity_clips']}")

    # 6c: Directional perturbation (x-direction sinusoid)
    rho0_2d = ic_2d_directional(128, 50.0, 5.0, 16)
    res = simulate_oscillator(
        params_2d, osc, rho0_2d.copy(),
        time_mode="hyperbolic", penalty_mode="symmetric",
        label="hyp_sym_2d_directional",
        snapshot_interval=2000,
    )
    osc_rho = measure_oscillation(res["diagnostics"]["rho_std"])
    exp6["directional_perturb"] = {
        **_summarize(res), "osc_rho_std": osc_rho,
    }
    np.save(os.path.join(results_dir, "2d_directional_rho.npy"), res["final_rho"])
    print(f"  Directional perturb: rho_osc={osc_rho['oscillations']}, "
          f"rho_std {res['diagnostics']['rho_std'][0]:.4f} -> "
          f"{res['diagnostics']['rho_std'][-1]:.4f}, "
          f"clips={res['positivity_clips']}")

    # 6d: Parabolic 2D baseline for comparison
    rho0_2d = ic_2d_perturbed(128, 50.0, 3.0, seed=42)
    res = simulate_oscillator(
        params_2d, OscillatorParams(rho_star=50), rho0_2d.copy(),
        time_mode="parabolic", penalty_mode="soft_floor",
        label="parabolic_sf_2d_random",
        snapshot_interval=2000,
    )
    osc_rho = measure_oscillation(res["diagnostics"]["rho_std"])
    exp6["parabolic_baseline"] = {
        **_summarize(res), "osc_rho_std": osc_rho,
    }
    print(f"  Parabolic baseline: rho_osc={osc_rho['oscillations']}, "
          f"rho_std {res['diagnostics']['rho_std'][0]:.4f} -> "
          f"{res['diagnostics']['rho_std'][-1]:.4f}")

    all_results["exp6_2d"] = exp6

    # ===================================================================
    # Save
    # ===================================================================
    results_path = os.path.join(results_dir, "oscillator_results.json")
    with open(results_path, "w") as f:
        json.dump(all_results, f, indent=2, default=_json_safe)
    print(f"\nResults saved to {results_path}")

    return all_results


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _summarize(res: dict) -> dict:
    d = res["diagnostics"]
    return {
        "label": res["label"],
        "time_mode": res["time_mode"],
        "penalty_mode": res["penalty_mode"],
        "tau": res["tau"],
        "zeta": res["zeta"],
        "rho_star": res["rho_star"],
        "rho_0": res["rho_0"],
        "eta": res["eta"],
        "blew_up": res["blew_up"],
        "steps_completed": res["steps_completed"],
        "elapsed_s": res["elapsed_s"],
        "positivity_clips": res["positivity_clips"],
        "rho_mean_initial": d["rho_mean"][0] if d["rho_mean"] else None,
        "rho_mean_final": d["rho_mean"][-1] if d["rho_mean"] else None,
        "rho_std_initial": d["rho_std"][0] if d["rho_std"] else None,
        "rho_std_final": d["rho_std"][-1] if d["rho_std"] else None,
        "rho_min_final": d["rho_min"][-1] if d["rho_min"] else None,
        "rho_max_final": d["rho_max"][-1] if d["rho_max"] else None,
        "rho_deviation_final": d["rho_deviation"][-1] if d["rho_deviation"] else None,
        "v_rms_final": d["v_rms"][-1] if d["v_rms"] else None,
        "v_max_final": d["v_max"][-1] if d["v_max"] else None,
        "rho_mean_series": d["rho_mean"],
        "rho_std_series": d["rho_std"],
        "v_rms_series": d["v_rms"],
        "rho_deviation_series": d["rho_deviation"],
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
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    script_dir = Path(__file__).parent
    results_dir = str(script_dir / "results")
    results = run_all_experiments(results_dir)

    print("\n" + "=" * 70)
    print("COMPLETE SUMMARY")
    print("=" * 70)
    for exp_name, exp_data in results.items():
        print(f"\n--- {exp_name} ---")
        for config_name, config_data in exp_data.items():
            if isinstance(config_data, dict):
                stable = "STABLE" if not config_data.get("blew_up", True) else "BLEW UP"
                rho_f = config_data.get("rho_mean_final", "?")
                clips = config_data.get("positivity_clips", "?")
                osc = config_data.get("osc_rho_std", {}).get("oscillations", "-")
                if isinstance(rho_f, (int, float)):
                    rho_f = f"{rho_f:.4f}"
                print(f"  {config_name:30s}: {stable:8s}  rho_mean={rho_f}  "
                      f"osc={osc}  clips={clips}")
