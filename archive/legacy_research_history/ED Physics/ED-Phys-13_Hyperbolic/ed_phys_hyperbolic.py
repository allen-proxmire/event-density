"""
ED-Phys-13: Hyperbolic Participation with Regularized Penalty
=============================================================

Tests whether oscillatory participation channels are possible when:
  1. The low-density singularity is removed (soft-floor penalty)
  2. The time sector is promoted to a hyperbolic (second-order) form

PDE:
  tau * d^2 rho/dt^2 + zeta * drho/dt
      = M(rho)*Lap(rho) + M'(rho)*|grad(rho)|^2 - alpha*gamma*(rho+rho_0)^(gamma-1)

First-order system:
  drho/dt = v
  dv/dt   = (1/tau) * [RHS_softfloor(rho) - zeta*v]

Canonical source: ED-5, ED-12, ED-12.5
"""

from __future__ import annotations

import json
import os
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
@dataclass
class EDParams:
    """Standard ED parameters shared across all modes."""

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
class HyperbolicParams:
    """Parameters specific to the hyperbolic extension."""

    tau: float = 1.0          # inertial timescale
    zeta: float = 0.01        # damping coefficient
    rho_0: float = 0.5        # soft-floor shift


# ---------------------------------------------------------------------------
# Operators (self-contained, matching ED-Phys-02 conventions)
# ---------------------------------------------------------------------------
def _pad(rho: np.ndarray, boundary: str) -> np.ndarray:
    """Pad array for boundary conditions."""
    if rho.ndim == 1:
        if boundary == "periodic":
            return np.concatenate(([rho[-1]], rho, [rho[0]]))
        elif boundary == "reflecting":
            return np.concatenate(([rho[0]], rho, [rho[-1]]))
        else:  # absorbing
            return np.concatenate(([0.0], rho, [0.0]))
    else:
        if boundary == "periodic":
            p = np.pad(rho, 1, mode="wrap")
        elif boundary == "reflecting":
            p = np.pad(rho, 1, mode="edge")
        else:
            p = np.pad(rho, 1, mode="constant", constant_values=0.0)
        return p


def discrete_laplacian(
    rho: np.ndarray, dx: float, boundary: str, eps: float = 1e-10
) -> np.ndarray:
    """Standard discrete Laplacian (5-point in 2D)."""
    dx2 = dx * dx
    p = _pad(rho, boundary)
    if rho.ndim == 1:
        return (p[2:] - 2.0 * p[1:-1] + p[:-2]) / dx2
    else:
        return (
            p[2:, 1:-1] + p[:-2, 1:-1] + p[1:-1, 2:] + p[1:-1, :-2]
            - 4.0 * p[1:-1, 1:-1]
        ) / dx2


def discrete_grad_squared(
    rho: np.ndarray, dx: float, boundary: str, eps: float = 1e-10
) -> np.ndarray:
    """Squared gradient magnitude (central differences)."""
    p = _pad(rho, boundary)
    two_dx = 2.0 * dx
    if rho.ndim == 1:
        gx = (p[2:] - p[:-2]) / two_dx
        return gx * gx
    else:
        gx = (p[2:, 1:-1] - p[:-2, 1:-1]) / two_dx
        gy = (p[1:-1, 2:] - p[1:-1, :-2]) / two_dx
        return gx * gx + gy * gy


def mobility(
    rho: np.ndarray,
    M_0: float,
    rho_max: float,
    n_mob: int,
) -> tuple[np.ndarray, np.ndarray]:
    """Compute M(rho) and M'(rho)."""
    ratio = np.clip(1.0 - rho / rho_max, 0.0, None)
    M = M_0 * ratio**n_mob
    if n_mob >= 1:
        M_prime = -M_0 * (n_mob / rho_max) * ratio ** (n_mob - 1)
    else:
        M_prime = np.zeros_like(rho)
    return M, M_prime


# ---------------------------------------------------------------------------
# Penalty functions
# ---------------------------------------------------------------------------
def penalty_soft_floor(
    rho: np.ndarray,
    alpha: float,
    gamma: float,
    rho_0: float = 0.5,
    eps: float = 1e-10,
) -> np.ndarray:
    """Soft-floor penalty: P(rho) = alpha*gamma*(rho + rho_0)^(gamma-1).

    Removes the low-density singularity while recovering canonical at rho >> rho_0.
    """
    rho_safe = np.maximum(rho, eps)
    return alpha * gamma * (rho_safe + rho_0) ** (gamma - 1.0)


def penalty_canonical(
    rho: np.ndarray,
    alpha: float,
    gamma: float,
    eps: float = 1e-10,
) -> np.ndarray:
    """Canonical penalty (for parabolic baseline comparison)."""
    rho_safe = np.maximum(rho, eps)
    return alpha * gamma * rho_safe ** (gamma - 1.0)


# ---------------------------------------------------------------------------
# RHS computation (shared by both modes)
# ---------------------------------------------------------------------------
def compute_rhs(
    rho: np.ndarray,
    params: EDParams,
    rho_0: float = 0.5,
    use_soft_floor: bool = True,
) -> np.ndarray:
    """Compute the spatial RHS: M*Lap + M'*|grad|^2 - P(rho)."""
    rho_safe = np.maximum(rho, params.eps)

    lap = discrete_laplacian(rho_safe, params.dx, params.boundary, params.eps)
    grad_sq = discrete_grad_squared(rho_safe, params.dx, params.boundary, params.eps)
    M, M_prime = mobility(rho_safe, params.M_0, params.rho_max, params.n_mob)

    diffusion = M * lap + M_prime * grad_sq

    if use_soft_floor:
        pen = penalty_soft_floor(rho_safe, params.alpha, params.gamma_exp, rho_0, params.eps)
    else:
        pen = penalty_canonical(rho_safe, params.alpha, params.gamma_exp, params.eps)

    return diffusion - pen


# ---------------------------------------------------------------------------
# CFL / timestep
# ---------------------------------------------------------------------------
def compute_timestep(
    params: EDParams, hyp: HyperbolicParams | None, time_mode: str
) -> float:
    """Compute stable timestep for parabolic or hyperbolic mode."""
    d = params.dimensions
    dx = params.dx

    # Diffusion CFL
    eta_diff = params.cfl_safety * dx**2 / (2.0 * d * params.M_0)

    if time_mode == "parabolic":
        # Penalty bound (soft-floor at rho=0)
        P_max = params.alpha * params.gamma_exp * hyp.rho_0 ** (params.gamma_exp - 1.0)
        eta_pen = 0.1 / max(P_max, 1e-10)
        return min(eta_diff, eta_pen)

    else:  # hyperbolic
        # Wave CFL: eta < CFL_safety * dx / c_max, where c_max = sqrt(M_max / tau)
        c_max = np.sqrt(params.M_0 / hyp.tau)
        eta_wave = params.cfl_safety * dx / c_max

        # Damping stability: eta < 2*tau/zeta (velocity damping stability)
        eta_damp = 2.0 * hyp.tau / max(hyp.zeta, 1e-10)

        return min(eta_diff, eta_wave, eta_damp, 0.5)


# ---------------------------------------------------------------------------
# Main simulator
# ---------------------------------------------------------------------------
def simulate_hyperbolic(
    params: EDParams,
    hyp: HyperbolicParams,
    initial_rho: np.ndarray,
    time_mode: str = "hyperbolic",
    snapshot_interval: int = 500,
    label: str = "",
) -> dict:
    """
    Unified simulator supporting both parabolic and hyperbolic time modes.

    Parameters
    ----------
    time_mode : str
        "parabolic" -> first-order: drho/dt = RHS(rho)
        "hyperbolic" -> second-order: tau*d^2rho/dt^2 + zeta*drho/dt = RHS(rho)
    """
    rho = initial_rho.astype(np.float64).copy()
    N = rho.shape[0]

    eta = compute_timestep(params, hyp, time_mode)

    # Velocity field (only used in hyperbolic mode)
    v = np.zeros_like(rho)

    # Storage
    diagnostics = {
        "rho_mean": [],
        "rho_max": [],
        "rho_min": [],
        "rho_std": [],
        "grad_mean": [],
        "v_rms": [],
        "v_max": [],
        "penalty_mean": [],
        "penalty_max": [],
    }
    snapshots = []
    snapshot_times = []

    t_start = time.time()
    blew_up = False

    for t in range(params.n_steps):
        # --- Safety check every 100 steps ---
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

        # --- Compute RHS ---
        rhs = compute_rhs(rho, params, hyp.rho_0, use_soft_floor=True)

        # --- Time integration ---
        if time_mode == "parabolic":
            rho_new = rho + eta * rhs
        else:
            # Leapfrog-like: update v, then rho
            dv = (1.0 / hyp.tau) * (rhs - hyp.zeta * v)
            v_new = v + eta * dv
            rho_new = rho + eta * v_new

        # Enforce positivity
        rho_new = np.maximum(rho_new, 0.0)

        # --- Diagnostics ---
        if t % max(1, params.n_steps // 2000) == 0 or t == params.n_steps - 1:
            rho_safe = np.maximum(rho_new, params.eps)
            pen = penalty_soft_floor(
                rho_safe, params.alpha, params.gamma_exp, hyp.rho_0, params.eps
            )

            # Gradient magnitude
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

            if time_mode == "hyperbolic":
                diagnostics["v_rms"].append(float(np.sqrt(np.mean(v_new**2))))
                diagnostics["v_max"].append(float(np.max(np.abs(v_new))))
            else:
                diagnostics["v_rms"].append(0.0)
                diagnostics["v_max"].append(0.0)

        # --- Snapshots ---
        if t % snapshot_interval == 0 or t == params.n_steps - 1:
            snapshots.append(rho_new.copy())
            snapshot_times.append(t)

        # --- Update state ---
        rho = rho_new
        if time_mode == "hyperbolic":
            v = v_new

    elapsed = time.time() - t_start

    return {
        "label": label,
        "time_mode": time_mode,
        "tau": hyp.tau,
        "zeta": hyp.zeta,
        "rho_0": hyp.rho_0,
        "eta": eta,
        "n_steps": params.n_steps,
        "blew_up": blew_up,
        "steps_completed": t + 1 if blew_up else params.n_steps,
        "elapsed_s": round(elapsed, 3),
        "diagnostics": diagnostics,
        "snapshots": snapshots,
        "snapshot_times": snapshot_times,
        "final_rho": rho,
        "final_v": v if time_mode == "hyperbolic" else None,
    }


# ---------------------------------------------------------------------------
# Analysis utilities
# ---------------------------------------------------------------------------
def count_zero_crossings(series: list[float]) -> int:
    """Count zero crossings in a time series (after removing mean)."""
    arr = np.array(series)
    arr = arr - np.mean(arr)
    signs = np.sign(arr)
    crossings = np.sum(np.abs(np.diff(signs)) > 0)
    return int(crossings)


def count_oscillations_v(series: list[float]) -> int:
    """Count oscillation peaks in v_rms time series."""
    arr = np.array(series)
    if len(arr) < 3:
        return 0
    # Find local maxima
    peaks = 0
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            peaks += 1
    return peaks


def measure_ringing(diagnostics: dict, key: str = "rho_std") -> dict:
    """Measure oscillatory character of a diagnostic time series."""
    series = diagnostics[key]
    arr = np.array(series)

    if len(arr) < 10:
        return {"oscillations": 0, "damping_ratio": None, "period_steps": None}

    # Zero crossings of derivative (turning points)
    d_arr = np.diff(arr)
    signs = np.sign(d_arr)
    turning_points = np.where(np.abs(np.diff(signs)) > 0)[0]
    n_oscillations = len(turning_points) // 2

    # Estimate damping from envelope of peaks
    peaks_idx = []
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            peaks_idx.append(i)

    damping_ratio = None
    period_steps = None
    if len(peaks_idx) >= 2:
        # Mean period in diagnostic indices
        peak_spacings = np.diff(peaks_idx)
        period_steps = float(np.mean(peak_spacings))

        # Damping: ratio of successive peak heights
        peak_vals = arr[peaks_idx]
        if len(peak_vals) >= 2 and peak_vals[0] > 1e-15:
            ratios = peak_vals[1:] / np.maximum(peak_vals[:-1], 1e-15)
            mean_ratio = float(np.mean(ratios))
            if 0 < mean_ratio < 1:
                damping_ratio = -np.log(mean_ratio)

    return {
        "oscillations": n_oscillations,
        "damping_ratio": damping_ratio,
        "period_steps": period_steps,
        "turning_points": len(turning_points),
    }


def measure_propagation(snapshots: list, snapshot_times: list, bg_level: float) -> dict:
    """Measure wave propagation speed from snapshot series."""
    if len(snapshots) < 3 or snapshots[0].ndim != 1:
        return {"speed": None, "spread": None}

    # Track the position of maximum perturbation
    positions = []
    widths = []
    for snap in snapshots:
        delta = snap - bg_level
        above = delta > 0.1 * np.max(np.abs(delta))
        if np.any(above):
            idx = np.where(above)[0]
            positions.append(float(np.mean(idx)))
            widths.append(float(len(idx)))
        else:
            positions.append(None)
            widths.append(None)

    # Estimate speed from position shift
    valid = [(t, p, w) for t, p, w in zip(snapshot_times, positions, widths) if p is not None]
    if len(valid) < 2:
        return {"speed": None, "spread": None}

    t0, p0, w0 = valid[0]
    t1, p1, w1 = valid[-1]
    dt = t1 - t0
    if dt > 0:
        speed = abs(p1 - p0) / dt
        spread = (w1 - w0) / dt if w0 is not None and w1 is not None else None
    else:
        speed = None
        spread = None

    return {"speed": speed, "spread": spread}


# ---------------------------------------------------------------------------
# Initial conditions
# ---------------------------------------------------------------------------
def ic_gaussian_pulse(N: int, rho_bg: float, amplitude: float, sigma: float, center: int | None = None) -> np.ndarray:
    """Single Gaussian peak on uniform background."""
    if center is None:
        center = N // 2
    x = np.arange(N, dtype=np.float64)
    return rho_bg + amplitude * np.exp(-((x - center) ** 2) / (2.0 * sigma**2))


def ic_sinusoidal(N: int, rho_bg: float, amp1: float, amp2: float) -> np.ndarray:
    """Sinusoidal superposition on uniform background."""
    x = np.arange(N, dtype=np.float64)
    return rho_bg + amp1 * np.sin(2.0 * np.pi * x / N) + amp2 * np.sin(4.0 * np.pi * x / N)


def ic_sinusoidal_single(N: int, rho_bg: float, amplitude: float, n_mode: int) -> np.ndarray:
    """Single sinusoidal mode for targeted wavelength test."""
    x = np.arange(N, dtype=np.float64)
    return rho_bg + amplitude * np.sin(2.0 * np.pi * n_mode * x / N)


def ic_two_peaks(N: int, rho_bg: float, amplitude: float, sigma: float, sep: int) -> np.ndarray:
    """Two Gaussian peaks for flow/interaction test."""
    c1 = N // 2 - sep // 2
    c2 = N // 2 + sep // 2
    x = np.arange(N, dtype=np.float64)
    return (
        rho_bg
        + amplitude * np.exp(-((x - c1) ** 2) / (2.0 * sigma**2))
        + amplitude * np.exp(-((x - c2) ** 2) / (2.0 * sigma**2))
    )


def ic_step(N: int, rho_low: float, rho_high: float) -> np.ndarray:
    """Step function for sharp-front propagation test."""
    rho = np.full(N, rho_low, dtype=np.float64)
    rho[N // 4 : N // 2] = rho_high
    return rho


# ---------------------------------------------------------------------------
# Experiments
# ---------------------------------------------------------------------------
def run_all_experiments(results_dir: str) -> dict:
    """Run the complete ED-Phys-13 experiment suite.

    Parameter design rationale:
    --------------------------
    The hyperbolic formulation converts the penalty drain P(rho) into a
    velocity field with steady-state v_ss = P(rho)/zeta.  For zeta << 1,
    this is far larger than the parabolic drain rate P, causing instant
    depletion.  The fix: zeta ~ 1 so v_ss ~ P (matching parabolic drain).
    Then Q > 1 requires tau > zeta^2 / K_eff(k).

    Regime table (at rho=50, M=0.25, K_eff(k=0.126)=0.00388):
      R1: tau=100, zeta=1.0   -> Q=0.62 (overdamped at k=0.126, oscillatory at k>0.16)
      R2: tau=500, zeta=1.0   -> Q=1.39 (oscillatory at k=0.126)
      R3: tau=50,  zeta=0.5   -> Q=0.88 (borderline, oscillatory at short wavelengths)
      R4: tau=1000, zeta=1.0  -> Q=1.97 (clear oscillation)
    """
    os.makedirs(results_dir, exist_ok=True)
    all_results = {}

    # -----------------------------------------------------------------------
    # EXPERIMENT 1: Homogeneous validation (both modes)
    # Verify hyperbolic mode doesn't blow up on uniform background
    # -----------------------------------------------------------------------
    print("=" * 70)
    print("EXPERIMENT 1: Homogeneous Validation")
    print("=" * 70)
    exp1 = {}
    params = EDParams(grid_size=256, n_steps=10000, dimensions=1)

    # Parabolic baseline
    rho0 = np.full(256, 50.0)
    res = simulate_hyperbolic(
        params, HyperbolicParams(rho_0=0.5), rho0,
        time_mode="parabolic", label="parabolic_homogeneous"
    )
    exp1["parabolic"] = _summarize(res)
    print(f"  Parabolic: rho_mean {res['diagnostics']['rho_mean'][0]:.4f} -> "
          f"{res['diagnostics']['rho_mean'][-1]:.4f}, stable={not res['blew_up']}")

    # Hyperbolic at each regime (corrected: zeta ~ 1 to match parabolic drain)
    regimes = [
        ("R1_short_wave",   100,  1.0),
        ("R2_medium_wave",  500,  1.0),
        ("R3_fast_response", 50,  0.5),
        ("R4_high_Q",      1000,  1.0),
    ]
    for name, tau, zeta in regimes:
        hyp = HyperbolicParams(tau=tau, zeta=zeta, rho_0=0.5)
        res = simulate_hyperbolic(
            params, hyp, rho0.copy(),
            time_mode="hyperbolic", label=f"hyp_{name}_homogeneous"
        )
        exp1[name] = _summarize(res)
        print(f"  {name} (tau={tau}, zeta={zeta}): rho_mean {res['diagnostics']['rho_mean'][0]:.4f} -> "
              f"{res['diagnostics']['rho_mean'][-1]:.4f}, stable={not res['blew_up']}, "
              f"v_rms_final={res['diagnostics']['v_rms'][-1]:.6f}")

    all_results["exp1_homogeneous"] = exp1

    # -----------------------------------------------------------------------
    # EXPERIMENT 2: Local Oscillation Test (Gaussian pulse)
    # Does rho_std ring rather than decay monotonically?
    # -----------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("EXPERIMENT 2: Local Oscillation Test")
    print("=" * 70)
    exp2 = {}
    params = EDParams(grid_size=512, n_steps=20000, dimensions=1)

    rho0 = ic_gaussian_pulse(512, rho_bg=50.0, amplitude=25.0, sigma=20.0)

    # Parabolic baseline
    res = simulate_hyperbolic(
        params, HyperbolicParams(rho_0=0.5), rho0.copy(),
        time_mode="parabolic", label="parabolic_pulse"
    )
    ring = measure_ringing(res["diagnostics"], "rho_std")
    exp2["parabolic"] = {**_summarize(res), "ringing": ring}
    print(f"  Parabolic: oscillations={ring['oscillations']}, "
          f"damping={ring['damping_ratio']}")

    for name, tau, zeta in regimes:
        hyp = HyperbolicParams(tau=tau, zeta=zeta, rho_0=0.5)
        res = simulate_hyperbolic(
            params, hyp, rho0.copy(),
            time_mode="hyperbolic", label=f"hyp_{name}_pulse"
        )
        ring = measure_ringing(res["diagnostics"], "rho_std")
        exp2[name] = {**_summarize(res), "ringing": ring}
        print(f"  {name}: oscillations={ring['oscillations']}, "
              f"damping={ring['damping_ratio']}, blew_up={res['blew_up']}")

    all_results["exp2_oscillation"] = exp2

    # -----------------------------------------------------------------------
    # EXPERIMENT 3: Sinusoidal Mode Test
    # Does a sinusoidal IC produce standing waves?
    # -----------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("EXPERIMENT 3: Sinusoidal Mode Test")
    print("=" * 70)
    exp3 = {}
    params = EDParams(grid_size=512, n_steps=20000, dimensions=1)

    rho0 = ic_sinusoidal(512, rho_bg=50.0, amp1=10.0, amp2=5.0)

    # Parabolic baseline
    res = simulate_hyperbolic(
        params, HyperbolicParams(rho_0=0.5), rho0.copy(),
        time_mode="parabolic", label="parabolic_sine"
    )
    ring = measure_ringing(res["diagnostics"], "rho_std")
    v_crossings = count_zero_crossings(res["diagnostics"]["rho_std"])
    exp3["parabolic"] = {**_summarize(res), "ringing": ring, "std_crossings": v_crossings}
    print(f"  Parabolic: oscillations={ring['oscillations']}, crossings={v_crossings}")

    for name, tau, zeta in regimes:
        hyp = HyperbolicParams(tau=tau, zeta=zeta, rho_0=0.5)
        res = simulate_hyperbolic(
            params, hyp, rho0.copy(),
            time_mode="hyperbolic", label=f"hyp_{name}_sine"
        )
        ring = measure_ringing(res["diagnostics"], "rho_std")
        v_ring = measure_ringing(res["diagnostics"], "v_rms")
        v_crossings = count_zero_crossings(res["diagnostics"]["rho_std"])
        exp3[name] = {
            **_summarize(res),
            "ringing": ring,
            "v_ringing": v_ring,
            "std_crossings": v_crossings,
        }
        print(f"  {name}: rho oscillations={ring['oscillations']}, "
              f"v oscillations={v_ring['oscillations']}, "
              f"crossings={v_crossings}, blew_up={res['blew_up']}")

    all_results["exp3_sinusoidal"] = exp3

    # -----------------------------------------------------------------------
    # EXPERIMENT 4: Wave Propagation Test (step function)
    # Does a sharp front propagate as a wave?
    # -----------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("EXPERIMENT 4: Wave Propagation Test")
    print("=" * 70)
    exp4 = {}
    params = EDParams(grid_size=512, n_steps=20000, dimensions=1)

    rho0 = ic_step(512, rho_low=40.0, rho_high=70.0)

    # Parabolic baseline
    res = simulate_hyperbolic(
        params, HyperbolicParams(rho_0=0.5), rho0.copy(),
        time_mode="parabolic", label="parabolic_step",
        snapshot_interval=1000,
    )
    prop = measure_propagation(res["snapshots"], res["snapshot_times"], 50.0)
    exp4["parabolic"] = {**_summarize(res), "propagation": prop}
    print(f"  Parabolic: speed={prop['speed']}, spread={prop['spread']}")

    for name, tau, zeta in regimes:
        hyp = HyperbolicParams(tau=tau, zeta=zeta, rho_0=0.5)
        res = simulate_hyperbolic(
            params, hyp, rho0.copy(),
            time_mode="hyperbolic", label=f"hyp_{name}_step",
            snapshot_interval=1000,
        )
        prop = measure_propagation(res["snapshots"], res["snapshot_times"], 50.0)
        exp4[name] = {**_summarize(res), "propagation": prop}
        print(f"  {name}: speed={prop['speed']}, spread={prop['spread']}, "
              f"blew_up={res['blew_up']}")

    all_results["exp4_propagation"] = exp4

    # -----------------------------------------------------------------------
    # EXPERIMENT 5: Long-term Stability (50K steps)
    # -----------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("EXPERIMENT 5: Long-term Stability (50K steps)")
    print("=" * 70)
    exp5 = {}
    params = EDParams(grid_size=512, n_steps=50000, dimensions=1)

    rho0 = ic_gaussian_pulse(512, rho_bg=50.0, amplitude=25.0, sigma=20.0)

    for name, tau, zeta in regimes:
        hyp = HyperbolicParams(tau=tau, zeta=zeta, rho_0=0.5)
        res = simulate_hyperbolic(
            params, hyp, rho0.copy(),
            time_mode="hyperbolic", label=f"hyp_{name}_stability",
            snapshot_interval=5000,
        )
        exp5[name] = _summarize(res)
        print(f"  {name}: steps={res['steps_completed']}, blew_up={res['blew_up']}, "
              f"rho_mean_final={res['diagnostics']['rho_mean'][-1]:.4f}, "
              f"v_rms_final={res['diagnostics']['v_rms'][-1]:.6f}")

    all_results["exp5_stability"] = exp5

    # -----------------------------------------------------------------------
    # EXPERIMENT 6: Parabolic vs Hyperbolic Comparison (peak dynamics)
    # -----------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("EXPERIMENT 6: Parabolic vs Hyperbolic Comparison")
    print("=" * 70)
    exp6 = {}
    params = EDParams(grid_size=512, n_steps=20000, dimensions=1)

    rho0 = ic_two_peaks(512, rho_bg=50.0, amplitude=25.0, sigma=20.0, sep=150)

    # Parabolic + soft-floor
    res_para = simulate_hyperbolic(
        params, HyperbolicParams(rho_0=0.5), rho0.copy(),
        time_mode="parabolic", label="parabolic_two_peaks"
    )
    exp6["parabolic_softfloor"] = _summarize(res_para)

    # Hyperbolic + soft-floor (R1 and R2)
    for name, tau, zeta in regimes[:2]:
        hyp = HyperbolicParams(tau=tau, zeta=zeta, rho_0=0.5)
        res = simulate_hyperbolic(
            params, hyp, rho0.copy(),
            time_mode="hyperbolic", label=f"hyp_{name}_two_peaks"
        )
        exp6[name] = _summarize(res)

    print(f"  Parabolic: rho_std_final={res_para['diagnostics']['rho_std'][-1]:.4f}")
    for name in ["R1_short_wave", "R2_medium_wave"]:
        if name in exp6:
            print(f"  {name}: blew_up={exp6[name].get('blew_up', '?')}, "
                  f"rho_mean_final={exp6[name].get('rho_mean_final', '?')}")

    all_results["exp6_comparison"] = exp6

    # -----------------------------------------------------------------------
    # EXPERIMENT 7: 2D Hyperbolic Cosmology
    # -----------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("EXPERIMENT 7: 2D Hyperbolic Cosmology")
    print("=" * 70)
    exp7 = {}
    params = EDParams(grid_size=128, n_steps=5000, dimensions=2)

    rng = np.random.default_rng(42)
    rho0_2d = rng.uniform(20.0, 80.0, size=(128, 128))

    # Parabolic baseline
    res = simulate_hyperbolic(
        params, HyperbolicParams(rho_0=0.5), rho0_2d.copy(),
        time_mode="parabolic", label="parabolic_2d_cosmo",
        snapshot_interval=1000,
    )
    exp7["parabolic"] = _summarize(res)
    np.save(os.path.join(results_dir, "2d_parabolic_rho.npy"), res["final_rho"])
    print(f"  Parabolic 2D: rho_std {res['diagnostics']['rho_std'][0]:.4f} -> "
          f"{res['diagnostics']['rho_std'][-1]:.4f}")

    # Hyperbolic R1 (short_wave, tau=100, zeta=1.0)
    hyp = HyperbolicParams(tau=100, zeta=1.0, rho_0=0.5)
    res = simulate_hyperbolic(
        params, hyp, rho0_2d.copy(),
        time_mode="hyperbolic", label="hyp_R1_2d_cosmo",
        snapshot_interval=1000,
    )
    exp7["R1_short_wave"] = _summarize(res)
    if not res["blew_up"]:
        np.save(os.path.join(results_dir, "2d_hyperbolic_R1_rho.npy"), res["final_rho"])
    print(f"  Hyperbolic R1 2D: blew_up={res['blew_up']}, "
          f"rho_std_final={res['diagnostics']['rho_std'][-1]:.4f}")

    # Hyperbolic R3 (fast_response, tau=50, zeta=0.5)
    hyp = HyperbolicParams(tau=50, zeta=0.5, rho_0=0.5)
    res = simulate_hyperbolic(
        params, hyp, rho0_2d.copy(),
        time_mode="hyperbolic", label="hyp_R3_2d_cosmo",
        snapshot_interval=1000,
    )
    exp7["R3_fast_response"] = _summarize(res)
    if not res["blew_up"]:
        np.save(os.path.join(results_dir, "2d_hyperbolic_R3_rho.npy"), res["final_rho"])
    print(f"  Hyperbolic R3 2D: blew_up={res['blew_up']}, "
          f"rho_std_final={res['diagnostics']['rho_std'][-1]:.4f}")

    all_results["exp7_2d_cosmology"] = exp7

    # -----------------------------------------------------------------------
    # EXPERIMENT 8: Short-Wavelength Oscillation Test (TARGETED)
    # Use modes where Q > 1 to look for genuine oscillatory behavior
    # -----------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("EXPERIMENT 8: Short-Wavelength Oscillation Test")
    print("=" * 70)
    exp8 = {}
    params = EDParams(grid_size=512, n_steps=30000, dimensions=1)

    # At rho=50, M=0.25:
    # mode n=16: k=2*pi*16/512=0.196, K_eff=0.25*0.0384-7e-5=0.00953, Q(tau=100)=0.98
    # mode n=32: k=2*pi*32/512=0.393, K_eff=0.25*0.154-7e-5=0.0386,  Q(tau=100)=1.96
    # mode n=48: k=2*pi*48/512=0.589, K_eff=0.25*0.347-7e-5=0.0867,  Q(tau=100)=2.94
    # Narrower Gaussian (sigma=5): most power at k~0.2, should show oscillation

    short_wave_ics = [
        ("mode_n16", ic_sinusoidal_single(512, 50.0, 5.0, 16)),
        ("mode_n32", ic_sinusoidal_single(512, 50.0, 5.0, 32)),
        ("narrow_pulse", ic_gaussian_pulse(512, 50.0, 15.0, 5.0)),
    ]

    for ic_name, rho0 in short_wave_ics:
        # Parabolic baseline
        res = simulate_hyperbolic(
            params, HyperbolicParams(rho_0=0.5), rho0.copy(),
            time_mode="parabolic", label=f"parabolic_{ic_name}"
        )
        ring = measure_ringing(res["diagnostics"], "rho_std")
        exp8[f"parabolic_{ic_name}"] = {**_summarize(res), "ringing": ring}
        print(f"  Parabolic {ic_name}: osc={ring['oscillations']}, "
              f"rho_std_final={res['diagnostics']['rho_std'][-1]:.6f}")

        # Hyperbolic R1 (tau=100, zeta=1) and R4 (tau=1000, zeta=1)
        for rname, tau, zeta in [("R1", 100, 1.0), ("R4", 1000, 1.0)]:
            hyp = HyperbolicParams(tau=tau, zeta=zeta, rho_0=0.5)
            res = simulate_hyperbolic(
                params, hyp, rho0.copy(),
                time_mode="hyperbolic", label=f"hyp_{rname}_{ic_name}"
            )
            ring_rho = measure_ringing(res["diagnostics"], "rho_std")
            ring_v = measure_ringing(res["diagnostics"], "v_rms")
            exp8[f"{rname}_{ic_name}"] = {
                **_summarize(res),
                "ringing_rho": ring_rho,
                "ringing_v": ring_v,
            }
            print(f"  {rname} {ic_name}: rho_osc={ring_rho['oscillations']}, "
                  f"v_osc={ring_v['oscillations']}, "
                  f"rho_std_final={res['diagnostics']['rho_std'][-1]:.6f}, "
                  f"period={ring_rho.get('period_steps', '-')}")

    all_results["exp8_short_wavelength"] = exp8

    # -----------------------------------------------------------------------
    # Save results
    # -----------------------------------------------------------------------
    results_path = os.path.join(results_dir, "hyperbolic_results.json")
    with open(results_path, "w") as f:
        json.dump(all_results, f, indent=2, default=_json_safe)
    print(f"\nResults saved to {results_path}")

    return all_results


def _summarize(res: dict) -> dict:
    """Extract JSON-safe summary from simulation result."""
    d = res["diagnostics"]
    summary = {
        "label": res["label"],
        "time_mode": res["time_mode"],
        "tau": res["tau"],
        "zeta": res["zeta"],
        "rho_0": res["rho_0"],
        "eta": res["eta"],
        "blew_up": res["blew_up"],
        "steps_completed": res["steps_completed"],
        "elapsed_s": res["elapsed_s"],
        "rho_mean_initial": d["rho_mean"][0] if d["rho_mean"] else None,
        "rho_mean_final": d["rho_mean"][-1] if d["rho_mean"] else None,
        "rho_std_initial": d["rho_std"][0] if d["rho_std"] else None,
        "rho_std_final": d["rho_std"][-1] if d["rho_std"] else None,
        "rho_min_final": d["rho_min"][-1] if d["rho_min"] else None,
        "rho_max_final": d["rho_max"][-1] if d["rho_max"] else None,
        "grad_mean_final": d["grad_mean"][-1] if d["grad_mean"] else None,
        "v_rms_final": d["v_rms"][-1] if d["v_rms"] else None,
        "v_max_final": d["v_max"][-1] if d["v_max"] else None,
        "penalty_mean_final": d["penalty_mean"][-1] if d["penalty_mean"] else None,
        # Full time series for analysis
        "rho_mean_series": d["rho_mean"],
        "rho_std_series": d["rho_std"],
        "v_rms_series": d["v_rms"],
    }
    return summary


def _json_safe(obj):
    """Handle numpy types for JSON serialization."""
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

    # Print summary table
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    for exp_name, exp_data in results.items():
        print(f"\n--- {exp_name} ---")
        for config_name, config_data in exp_data.items():
            if isinstance(config_data, dict):
                stable = "STABLE" if not config_data.get("blew_up", True) else "BLEW UP"
                rho_f = config_data.get("rho_mean_final", "?")
                v_f = config_data.get("v_rms_final", "?")
                ring = config_data.get("ringing", {})
                osc = ring.get("oscillations", "-")
                if isinstance(rho_f, (int, float)):
                    rho_f = f"{rho_f:.4f}"
                if isinstance(v_f, (int, float)):
                    v_f = f"{v_f:.6f}"
                print(f"  {config_name:20s}: {stable:8s}  rho_mean={rho_f}  "
                      f"v_rms={v_f}  osc={osc}")
