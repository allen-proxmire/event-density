"""
ED-Phys-15: Symmetric-Denominator Restoring Penalty
====================================================

Replaces the ED-Phys-12/14 symmetric penalty
    P_SY(rho) = alpha*gamma*(rho - rho_star) / (rho + rho_0)
with the fully symmetric form
    P_SY2(rho) = alpha*gamma*(rho - rho_star) / sqrt((rho - rho_star)^2 + rho_0^2)

Key properties of P_SY2:
  - Zero at rho = rho_star
  - EXACTLY anti-symmetric: P(rho* + d) = -P(rho* - d) for all d
  - Bounded: |P| <= alpha*gamma
  - C-infinity smooth
  - Restoring force P'(rho*) = alpha*gamma/rho_0

This eliminates the nonlinear density drift observed in ED-Phys-14 2D tests
(rho_mean: 50 -> 122) caused by the asymmetric denominator (rho + rho_0).

Effective potential: V(rho) = alpha*gamma*sqrt((rho - rho_star)^2 + rho_0^2)
Energy: E = (tau/2)*int(v^2) + (M/2)*int(|grad rho|^2) + int(V(rho))
Dissipation: dE/dt = -zeta*int(v^2) <= 0

Canonical sources: ED-5, ED-12, ED-12.5
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass, field
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
    tau: float = 100.0
    zeta: float = 1.0
    rho_star: float = 50.0
    rho_0: float = 0.5


# ---------------------------------------------------------------------------
# Operators
# ---------------------------------------------------------------------------
def _pad(rho: np.ndarray, boundary: str) -> np.ndarray:
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
    M = M_0 * ratio ** n_mob
    M_prime = -M_0 * (n_mob / rho_max) * ratio ** max(n_mob - 1, 0)
    return M, M_prime


# ---------------------------------------------------------------------------
# Penalty functions (all three forms for comparison)
# ---------------------------------------------------------------------------
def penalty_sy2(
    rho: np.ndarray,
    alpha: float,
    gamma: float,
    rho_star: float,
    rho_0: float = 0.5,
    eps: float = 1e-10,
) -> np.ndarray:
    """Symmetric-denominator penalty (NEW):
    P_SY2(rho) = alpha*gamma*(rho - rho_star) / sqrt((rho - rho_star)^2 + rho_0^2)

    Exactly anti-symmetric around rho_star. No nonlinear drift.
    """
    rho_safe = np.maximum(rho, eps)
    delta = rho_safe - rho_star
    return alpha * gamma * delta / np.sqrt(delta * delta + rho_0 * rho_0)


def penalty_sy(
    rho: np.ndarray,
    alpha: float,
    gamma: float,
    rho_star: float,
    rho_0: float = 0.5,
    eps: float = 1e-10,
) -> np.ndarray:
    """Original symmetric penalty (ED-Phys-12/14):
    P_SY(rho) = alpha*gamma*(rho - rho_star) / (rho + rho_0)

    Asymmetric denominator causes nonlinear density drift.
    """
    rho_safe = np.maximum(rho, eps)
    return alpha * gamma * (rho_safe - rho_star) / (rho_safe + rho_0)


def penalty_soft_floor(
    rho: np.ndarray,
    alpha: float,
    gamma: float,
    rho_0: float = 0.5,
    eps: float = 1e-10,
) -> np.ndarray:
    """Soft-floor penalty (ED-Phys-12/13):
    P_SF(rho) = alpha*gamma*(rho + rho_0)^(gamma-1)

    Always positive. No equilibrium. Drains to zero.
    """
    rho_safe = np.maximum(rho, eps)
    return alpha * gamma * (rho_safe + rho_0) ** (gamma - 1.0)


# ---------------------------------------------------------------------------
# Effective potential for energy computation
# ---------------------------------------------------------------------------
def potential_sy2(
    rho: np.ndarray,
    alpha: float,
    gamma: float,
    rho_star: float,
    rho_0: float = 0.5,
) -> np.ndarray:
    """Effective potential V(rho) = alpha*gamma*sqrt((rho - rho_star)^2 + rho_0^2).

    V'(rho) = P_SY2(rho).  V(rho_star) = alpha*gamma*rho_0.
    """
    delta = rho - rho_star
    return alpha * gamma * np.sqrt(delta * delta + rho_0 * rho_0)


# ---------------------------------------------------------------------------
# RHS computation
# ---------------------------------------------------------------------------
def compute_rhs(
    rho: np.ndarray,
    params: EDParams,
    osc: OscillatorParams,
    penalty_mode: str,
) -> np.ndarray:
    rho_safe = np.maximum(rho, params.eps)
    lap = discrete_laplacian(rho_safe, params.dx, params.boundary)
    grad_sq = discrete_grad_squared(rho_safe, params.dx, params.boundary)
    M, M_prime = mobility(rho_safe, params.M_0, params.rho_max, params.n_mob)

    if penalty_mode == "sy2":
        pen = penalty_sy2(
            rho_safe, params.alpha, params.gamma_exp,
            osc.rho_star, osc.rho_0, params.eps,
        )
    elif penalty_mode == "sy":
        pen = penalty_sy(
            rho_safe, params.alpha, params.gamma_exp,
            osc.rho_star, osc.rho_0, params.eps,
        )
    elif penalty_mode == "soft_floor":
        pen = penalty_soft_floor(
            rho_safe, params.alpha, params.gamma_exp, osc.rho_0, params.eps,
        )
    else:
        raise ValueError(f"Unknown penalty_mode: {penalty_mode}")

    return M * lap + M_prime * grad_sq - pen


# ---------------------------------------------------------------------------
# Timestep
# ---------------------------------------------------------------------------
def compute_timestep(params: EDParams, osc: OscillatorParams, time_mode: str) -> float:
    d = params.dimensions
    dx = params.dx
    eta_diff = params.cfl_safety * dx ** 2 / (2.0 * d * params.M_0)
    if time_mode == "parabolic":
        P_max = params.alpha * params.gamma_exp  # bounded penalty
        eta_pen = 0.1 / max(P_max, 1e-10)
        return min(eta_diff, eta_pen, 0.5)
    else:
        # Wave CFL: c_max^2 = max(K_eff/tau)
        # K_eff_max at highest k ~ pi/dx: M_0*(pi/dx)^2 + P'(rho_star)
        P_prime = params.alpha * params.gamma_exp / osc.rho_0
        k_max = np.pi / dx
        K_eff_max = params.M_0 * k_max ** 2 + P_prime
        c_max = np.sqrt(K_eff_max / osc.tau)
        eta_wave = params.cfl_safety * dx / max(c_max, 1e-10)
        eta_damp = 2.0 * osc.tau / max(osc.zeta, 1e-10)
        return min(eta_diff, eta_wave, eta_damp, 0.5)


# ---------------------------------------------------------------------------
# Energy computation
# ---------------------------------------------------------------------------
def compute_energy(
    rho: np.ndarray,
    v: np.ndarray,
    params: EDParams,
    osc: OscillatorParams,
    penalty_mode: str,
) -> dict:
    """Compute oscillator energy components.

    E_kinetic  = (tau/2) * mean(v^2)
    E_gradient = (M(rho_star)/2) * mean(|grad rho|^2)
    E_potential = mean(V(rho))
    E_total    = E_kinetic + E_gradient + E_potential
    dissipation_rate = zeta * mean(v^2)
    """
    dx = params.dx
    # Kinetic energy (velocity field)
    E_kin = 0.5 * osc.tau * float(np.mean(v ** 2))

    # Gradient energy (linearized around rho_star)
    rho_safe = np.maximum(rho, params.eps)
    grad_sq = discrete_grad_squared(rho_safe, dx, params.boundary)
    M_star = params.M_0 * (1.0 - osc.rho_star / params.rho_max) ** params.n_mob
    E_grad = 0.5 * M_star * float(np.mean(grad_sq))

    # Potential energy
    if penalty_mode == "sy2":
        V = potential_sy2(rho, params.alpha, params.gamma_exp, osc.rho_star, osc.rho_0)
        E_pot = float(np.mean(V))
    else:
        # No clean potential for P_SY or soft_floor; use numerical proxy
        delta = rho - osc.rho_star
        E_pot = 0.5 * float(np.mean(delta ** 2))  # harmonic approximation

    # Dissipation rate
    diss = osc.zeta * float(np.mean(v ** 2))

    return {
        "E_kinetic": E_kin,
        "E_gradient": E_grad,
        "E_potential": E_pot,
        "E_total": E_kin + E_grad + E_pot,
        "dissipation_rate": diss,
    }


# ---------------------------------------------------------------------------
# Main simulator
# ---------------------------------------------------------------------------
def simulate(
    params: EDParams,
    osc: OscillatorParams,
    initial_rho: np.ndarray,
    time_mode: str = "hyperbolic",
    penalty_mode: str = "sy2",
    snapshot_interval: int = 500,
    label: str = "",
    point_traces: list[int] | None = None,
    track_energy: bool = False,
) -> dict:
    """
    Combined hyperbolic + penalty simulator.

    Parameters
    ----------
    time_mode : "parabolic" or "hyperbolic"
    penalty_mode : "sy2", "sy", or "soft_floor"
    track_energy : if True, record energy components at each diagnostic step
    """
    rho = initial_rho.astype(np.float64).copy()
    eta = compute_timestep(params, osc, time_mode)
    v = np.zeros_like(rho)

    diag_interval = max(1, params.n_steps // 4000)

    diagnostics = {
        "rho_mean": [], "rho_max": [], "rho_min": [], "rho_std": [],
        "grad_mean": [], "v_rms": [], "v_max": [],
        "penalty_mean": [], "penalty_max": [], "penalty_min": [],
        "rho_deviation": [],
    }
    if track_energy:
        diagnostics["E_kinetic"] = []
        diagnostics["E_gradient"] = []
        diagnostics["E_potential"] = []
        diagnostics["E_total"] = []
        diagnostics["dissipation_rate"] = []

    snapshots = []
    snapshot_times = []

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
        rhs = compute_rhs(rho, params, osc, penalty_mode)

        # Time integration
        if time_mode == "parabolic":
            rho_new = rho + eta * rhs
            v_new = v
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
            if penalty_mode == "sy2":
                pen = penalty_sy2(
                    rho_safe, params.alpha, params.gamma_exp,
                    osc.rho_star, osc.rho_0, params.eps,
                )
            elif penalty_mode == "sy":
                pen = penalty_sy(
                    rho_safe, params.alpha, params.gamma_exp,
                    osc.rho_star, osc.rho_0, params.eps,
                )
            else:
                pen = penalty_soft_floor(
                    rho_safe, params.alpha, params.gamma_exp, osc.rho_0, params.eps,
                )

            p = _pad(rho_safe, params.boundary)
            if rho.ndim == 1:
                gx = (p[2:] - p[:-2]) / (2.0 * params.dx)
                grad_mag = np.abs(gx)
            else:
                gx = (p[2:, 1:-1] - p[:-2, 1:-1]) / (2.0 * params.dx)
                gy = (p[1:-1, 2:] - p[1:-1, :-2]) / (2.0 * params.dx)
                grad_mag = np.sqrt(gx ** 2 + gy ** 2)

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
                diagnostics["v_rms"].append(float(np.sqrt(np.mean(v_new ** 2))))
                diagnostics["v_max"].append(float(np.max(np.abs(v_new))))
            else:
                diagnostics["v_rms"].append(0.0)
                diagnostics["v_max"].append(0.0)

            if track_energy and time_mode == "hyperbolic":
                en = compute_energy(rho_new, v_new, params, osc, penalty_mode)
                diagnostics["E_kinetic"].append(en["E_kinetic"])
                diagnostics["E_gradient"].append(en["E_gradient"])
                diagnostics["E_potential"].append(en["E_potential"])
                diagnostics["E_total"].append(en["E_total"])
                diagnostics["dissipation_rate"].append(en["dissipation_rate"])

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
# Analysis helpers
# ---------------------------------------------------------------------------
def measure_oscillation(series: list[float], skip_fraction: float = 0.05) -> dict:
    arr = np.array(series)
    if len(arr) < 20:
        return {"oscillations": 0, "damping_ratio": None, "period": None,
                "amplitude_initial": None, "amplitude_final": None}

    start = max(1, int(len(arr) * skip_fraction))
    arr = arr[start:]

    peaks_idx = []
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            peaks_idx.append(i)

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
    arr = np.array(trace_rho)
    if len(arr) < 20:
        return {"oscillations": 0, "period": None, "damping_ratio": None}

    delta = arr - rho_star
    signs = np.sign(delta)
    crossings = np.where(np.abs(np.diff(signs)) > 0)[0]
    n_crossings = len(crossings)
    n_oscillations = n_crossings // 2

    period = None
    if len(crossings) >= 4:
        half_periods = np.diff(crossings)
        period = float(2.0 * np.mean(half_periods))

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
    x = np.arange(N, dtype=np.float64)
    return rho_star + epsilon * np.sin(2.0 * np.pi * n_mode * x / N)


def ic_far_from_star(N: int, rho_init: float) -> np.ndarray:
    return np.full(N, rho_init, dtype=np.float64)


def ic_2d_perturbed(Nx: int, rho_star: float, epsilon: float, seed: int = 42):
    rng = np.random.default_rng(seed)
    return rho_star + epsilon * rng.standard_normal((Nx, Nx))


def ic_2d_radial(Nx: int, rho_star: float, amplitude: float, sigma: float):
    cx, cy = Nx // 2, Nx // 2
    y, x = np.mgrid[0:Nx, 0:Nx]
    r2 = (x - cx) ** 2 + (y - cy) ** 2
    return rho_star + amplitude * np.exp(-r2 / (2.0 * sigma ** 2))


def ic_2d_directional(Nx: int, rho_star: float, amplitude: float, n_mode: int):
    x = np.arange(Nx, dtype=np.float64)
    row = rho_star + amplitude * np.sin(2.0 * np.pi * n_mode * x / Nx)
    return np.tile(row, (Nx, 1))


def ic_2d_mixed(Nx: int, rho_star: float, amplitude: float, seed: int = 42):
    """Mixed-mode: radial + directional + random."""
    rho = np.full((Nx, Nx), rho_star, dtype=np.float64)
    # Radial component
    cx, cy = Nx // 2, Nx // 2
    y, x = np.mgrid[0:Nx, 0:Nx]
    r2 = (x - cx) ** 2 + (y - cy) ** 2
    rho += 0.5 * amplitude * np.exp(-r2 / (2.0 * 15.0 ** 2))
    # Directional component
    rho += 0.3 * amplitude * np.sin(2.0 * np.pi * 8 * x / Nx)
    # Random component
    rng = np.random.default_rng(seed)
    rho += 0.2 * amplitude * rng.standard_normal((Nx, Nx))
    return rho


# ---------------------------------------------------------------------------
# Summary helper
# ---------------------------------------------------------------------------
def _summarize(res: dict) -> dict:
    d = res["diagnostics"]
    summary = {
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
    if "E_total" in d:
        summary["E_total_initial"] = d["E_total"][0] if d["E_total"] else None
        summary["E_total_final"] = d["E_total"][-1] if d["E_total"] else None
        summary["E_total_series"] = d["E_total"]
        summary["E_kinetic_series"] = d["E_kinetic"]
        summary["E_gradient_series"] = d["E_gradient"]
        summary["E_potential_series"] = d["E_potential"]
        summary["dissipation_series"] = d["dissipation_rate"]
    return summary


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
# Linear theory predictions
# ---------------------------------------------------------------------------
def predict_linear(params: EDParams, osc: OscillatorParams, n_mode: int, N: int) -> dict:
    """Predict oscillation properties from linear theory."""
    k = 2.0 * np.pi * n_mode / N if n_mode > 0 else 0.0
    lam = N / n_mode if n_mode > 0 else float("inf")
    P_prime = params.alpha * params.gamma_exp / osc.rho_0
    M_star = params.M_0 * (1.0 - osc.rho_star / params.rho_max) ** params.n_mob
    K_eff = M_star * k ** 2 + P_prime
    omega_0 = np.sqrt(K_eff / osc.tau)
    Q = np.sqrt(osc.tau * K_eff) / osc.zeta
    T_time = 2.0 * np.pi / omega_0 if omega_0 > 0 else float("inf")
    eta = compute_timestep(params, osc, "hyperbolic")
    T_steps = T_time / eta

    # Damping ratio (standard form)
    zeta_ratio = osc.zeta / (2.0 * np.sqrt(osc.tau * K_eff))

    return {
        "n_mode": n_mode,
        "wavelength": lam,
        "k": k,
        "P_prime": P_prime,
        "M_star": M_star,
        "K_eff": K_eff,
        "omega_0": omega_0,
        "Q": Q,
        "zeta_ratio": zeta_ratio,
        "T_time_units": T_time,
        "T_steps": T_steps,
    }


# ===================================================================
# EXPERIMENT SUITE
# ===================================================================
def run_all_experiments(results_dir: str) -> dict:
    os.makedirs(results_dir, exist_ok=True)
    all_results = {}

    # ----- Parameter regimes -----
    # P_SY2'(rho*) = alpha*gamma/rho_0 (independent of rho_star!)
    # With rho_0=0.5: P_prime = 0.1. With rho_0=5.0: P_prime = 0.01
    # With rho_0=50.5: P_prime = 9.90e-4 (matches ED-Phys-14 linearization)
    regimes = [
        # name,             tau,  zeta, rho_star, rho_0
        ("R1_baseline",     100,  1.0,  50,       0.5),   # Q(k=0)=3.16
        ("R2_moderate",     100,  1.0,  50,       5.0),   # Q(k=0)=1.0
        ("R3_light_damp",   100,  0.5,  50,       0.5),   # Q(k=0)=6.32
        ("R4_matched_14",   500,  1.0,  50,       50.5),  # Q(k=0)=0.70 (same as ED-14 R1)
        ("R5_alt_equil",    100,  1.0,  20,       0.5),   # Q(k=0)=3.16, different rho_star
    ]

    print("=" * 70)
    print("ED-Phys-15: Symmetric-Denominator Restoring Penalty")
    print("=" * 70)
    print("\nParameter Regimes:")
    print("-" * 80)
    for name, tau, zeta, rstar, rho0 in regimes:
        P_prime = 0.1 * 0.5 / rho0
        M_star = (1.0 - rstar / 100.0) ** 2
        Q_k0 = np.sqrt(tau * P_prime) / zeta
        k16 = 2.0 * np.pi * 16 / 512
        K_eff_16 = M_star * k16 ** 2 + P_prime
        Q_k16 = np.sqrt(tau * K_eff_16) / zeta
        T_k0 = 2.0 * np.pi * np.sqrt(tau / P_prime)
        eta_est = compute_timestep(
            EDParams(grid_size=512), OscillatorParams(tau=tau, zeta=zeta, rho_star=rstar, rho_0=rho0),
            "hyperbolic",
        )
        print(f"  {name}: tau={tau}, zeta={zeta}, rho*={rstar}, rho_0={rho0}, "
              f"P'={P_prime:.4f}, Q(k=0)={Q_k0:.2f}, Q(k16)={Q_k16:.2f}, "
              f"T(k=0)={T_k0/eta_est:.0f} steps, eta={eta_est:.4f}")
    print()

    # ===================================================================
    # EXPERIMENT 1: Homogeneous Equilibrium + Validation (TASK 3)
    # ===================================================================
    print("=" * 70)
    print("EXPERIMENT 1: Homogeneous Equilibrium Validation")
    print("=" * 70)
    exp1 = {}
    params = EDParams(grid_size=256, n_steps=20000, dimensions=1)

    for name, tau, zeta, rstar, rho0 in regimes:
        osc = OscillatorParams(tau=tau, zeta=zeta, rho_star=rstar, rho_0=rho0)
        rho0_ic = ic_uniform(256, rstar)
        res = simulate(
            params, osc, rho0_ic.copy(),
            time_mode="hyperbolic", penalty_mode="sy2",
            label=f"sy2_{name}_homog",
        )
        exp1[name] = _summarize(res)
        print(f"  {name}: rho_mean {res['diagnostics']['rho_mean'][0]:.6f} -> "
              f"{res['diagnostics']['rho_mean'][-1]:.6f}, "
              f"deviation={res['diagnostics']['rho_deviation'][-1]:.8f}, "
              f"stable={not res['blew_up']}")

    # Small perturbation validation
    osc_v = OscillatorParams(tau=100, zeta=1.0, rho_star=50, rho_0=0.5)
    rho0_ic = ic_perturbed(256, 50.0, 1.0, 4)
    res = simulate(
        params, osc_v, rho0_ic.copy(),
        time_mode="hyperbolic", penalty_mode="sy2",
        label="sy2_R1_small_perturb",
        point_traces=[64, 128],
    )
    exp1["small_perturb"] = _summarize(res)
    print(f"  Small perturb: rho_mean {res['diagnostics']['rho_mean'][-1]:.6f}, "
          f"rho_std {res['diagnostics']['rho_std'][0]:.4f} -> "
          f"{res['diagnostics']['rho_std'][-1]:.4f}")

    # Large perturbation validation (0.5x and 1.5x)
    for factor, label_tag in [(0.5, "below"), (1.5, "above")]:
        rho0_ic = ic_far_from_star(256, factor * 50.0)
        res = simulate(
            params, osc_v, rho0_ic.copy(),
            time_mode="hyperbolic", penalty_mode="sy2",
            label=f"sy2_R1_{label_tag}",
            point_traces=[128],
        )
        exp1[f"large_perturb_{label_tag}"] = {
            **_summarize(res),
            "start_rho": factor * 50.0,
            "point_oscillation": measure_point_oscillation(
                res["traces"][128]["rho"], 50.0
            ) if 128 in res["traces"] else {},
        }
        print(f"  Large perturb ({label_tag}, rho={factor*50:.0f}): "
              f"rho_final={res['diagnostics']['rho_mean'][-1]:.4f}, "
              f"clips={res['positivity_clips']}")

    all_results["exp1_validation"] = exp1

    # ===================================================================
    # EXPERIMENT 2: Period + Damping Test (TASK 3, 4.1)
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXPERIMENT 2: Period and Damping Test")
    print("=" * 70)
    exp2 = {}
    params = EDParams(grid_size=512, n_steps=50000, dimensions=1)

    test_modes = [1, 4, 16, 32, 64]

    for name, tau, zeta, rstar, rho0 in regimes[:3]:  # R1, R2, R3
        osc = OscillatorParams(tau=tau, zeta=zeta, rho_star=rstar, rho_0=rho0)

        for n_mode in test_modes:
            epsilon = 5.0
            rho0_ic = ic_perturbed(512, rstar, epsilon, n_mode)
            trace_pts = [128, 256]

            res = simulate(
                params, osc, rho0_ic.copy(),
                time_mode="hyperbolic", penalty_mode="sy2",
                label=f"sy2_{name}_mode{n_mode}",
                point_traces=trace_pts,
            )

            osc_rho = measure_oscillation(res["diagnostics"]["rho_std"])
            pt_osc = {}
            for idx in trace_pts:
                if idx in res["traces"] and res["traces"][idx]["rho"]:
                    pt_osc[idx] = measure_point_oscillation(
                        res["traces"][idx]["rho"], rstar,
                    )

            pred = predict_linear(params, osc, n_mode, 512)
            key = f"{name}_mode{n_mode}"
            exp2[key] = {
                **_summarize(res),
                "osc_rho_std": osc_rho,
                "point_oscillations": pt_osc,
                "predicted": pred,
            }
            print(f"  {key}: osc={osc_rho['oscillations']}, "
                  f"period={osc_rho.get('period', '-')}, "
                  f"Q_pred={pred['Q']:.2f}, T_pred={pred['T_steps']:.0f}, "
                  f"damp={osc_rho.get('damping_ratio', '-')}, "
                  f"clips={res['positivity_clips']}")

    all_results["exp2_period_damping"] = exp2

    # ===================================================================
    # EXPERIMENT 3: Long-Term Stability (TASK 3.3, TASK 4.2)
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXPERIMENT 3: Long-Term Stability (100K steps)")
    print("=" * 70)
    exp3 = {}
    params = EDParams(grid_size=512, n_steps=100000, dimensions=1)

    for name, tau, zeta, rstar, rho0 in regimes[:3]:
        osc = OscillatorParams(tau=tau, zeta=zeta, rho_star=rstar, rho_0=rho0)
        rho0_ic = ic_perturbed(512, rstar, 5.0, 32)
        trace_pts = [128, 256]

        res = simulate(
            params, osc, rho0_ic.copy(),
            time_mode="hyperbolic", penalty_mode="sy2",
            label=f"sy2_{name}_sustained",
            point_traces=trace_pts,
            track_energy=True,
        )

        osc_rho = measure_oscillation(res["diagnostics"]["rho_std"])
        pt_osc = {}
        for idx in trace_pts:
            if idx in res["traces"] and res["traces"][idx]["rho"]:
                pt_osc[idx] = measure_point_oscillation(
                    res["traces"][idx]["rho"], rstar,
                )

        # Mean drift check
        rho_means = res["diagnostics"]["rho_mean"]
        mean_drift = abs(rho_means[-1] - rho_means[0]) if rho_means else 0

        exp3[name] = {
            **_summarize(res),
            "osc_rho_std": osc_rho,
            "point_oscillations": pt_osc,
            "mean_drift": mean_drift,
        }
        print(f"  {name}: osc={osc_rho['oscillations']}, "
              f"damp={osc_rho.get('damping_ratio', '-')}, "
              f"amp_i={osc_rho.get('amplitude_initial', '-')}, "
              f"amp_f={osc_rho.get('amplitude_final', '-')}, "
              f"mean_drift={mean_drift:.6f}, clips={res['positivity_clips']}")

    all_results["exp3_sustained"] = exp3

    # ===================================================================
    # EXPERIMENT 4: k=0 Global Oscillation Test (TASK 3.4)
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXPERIMENT 4: k=0 Global Oscillation Test")
    print("=" * 70)
    exp4 = {}
    params = EDParams(grid_size=256, n_steps=50000, dimensions=1)

    for name, tau, zeta, rstar, rho0 in regimes[:3]:
        osc = OscillatorParams(tau=tau, zeta=zeta, rho_star=rstar, rho_0=rho0)

        # Start uniformly above rho_star (pure k=0 excitation)
        rho0_ic = ic_far_from_star(256, rstar + 10.0)
        res = simulate(
            params, osc, rho0_ic.copy(),
            time_mode="hyperbolic", penalty_mode="sy2",
            label=f"sy2_{name}_k0_above",
            point_traces=[128],
        )
        pt_osc = measure_point_oscillation(
            res["traces"][128]["rho"], rstar,
        ) if 128 in res["traces"] else {}

        pred = predict_linear(params, osc, 0, 256)

        # Check symmetry: mean should return to rho_star, no drift
        rho_means = res["diagnostics"]["rho_mean"]
        overshoot = min(rho_means) if rho_means else rstar  # minimum density during oscillation

        exp4[f"{name}_above"] = {
            **_summarize(res),
            "start_rho": rstar + 10.0,
            "point_oscillation": pt_osc,
            "predicted_k0": pred,
            "mean_overshoot": float(overshoot),
        }
        print(f"  {name} k=0 (start={rstar+10:.0f}): "
              f"final={rho_means[-1]:.4f}, overshoot_min={overshoot:.4f}, "
              f"osc={pt_osc.get('oscillations', '-')}, Q_pred={pred['Q']:.2f}")

        # Also from below for symmetry check
        rho0_ic = ic_far_from_star(256, max(rstar - 10.0, 1.0))
        res = simulate(
            params, osc, rho0_ic.copy(),
            time_mode="hyperbolic", penalty_mode="sy2",
            label=f"sy2_{name}_k0_below",
            point_traces=[128],
        )
        pt_osc_b = measure_point_oscillation(
            res["traces"][128]["rho"], rstar,
        ) if 128 in res["traces"] else {}
        rho_means_b = res["diagnostics"]["rho_mean"]
        overshoot_b = max(rho_means_b) if rho_means_b else rstar

        exp4[f"{name}_below"] = {
            **_summarize(res),
            "start_rho": max(rstar - 10.0, 1.0),
            "point_oscillation": pt_osc_b,
            "mean_overshoot": float(overshoot_b),
        }
        print(f"  {name} k=0 (start={max(rstar-10,1):.0f}): "
              f"final={rho_means_b[-1]:.4f}, overshoot_max={overshoot_b:.4f}, "
              f"osc={pt_osc_b.get('oscillations', '-')}")

    all_results["exp4_k0_test"] = exp4

    # ===================================================================
    # EXPERIMENT 5: Structural Scale Test (TASK 5)
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXPERIMENT 5: Structural Scale Test")
    print("=" * 70)
    exp5 = {}
    params = EDParams(grid_size=512, n_steps=50000, dimensions=1)

    scale_modes = {
        "short_n64": 64,
        "short_n32": 32,
        "mid_n8": 8,
        "mid_n4": 4,
        "long_n2": 2,
        "long_n1": 1,
    }

    osc = OscillatorParams(tau=100, zeta=0.5, rho_star=50, rho_0=0.5)  # R3
    for scale_name, n_mode in scale_modes.items():
        rho0_ic = ic_perturbed(512, 50.0, 5.0, n_mode)
        res = simulate(
            params, osc, rho0_ic.copy(),
            time_mode="hyperbolic", penalty_mode="sy2",
            label=f"sy2_R3_{scale_name}",
            point_traces=[256],
        )
        osc_rho = measure_oscillation(res["diagnostics"]["rho_std"])
        pt_osc = measure_point_oscillation(
            res["traces"][256]["rho"], 50.0,
        ) if 256 in res["traces"] else {}
        pred = predict_linear(params, osc, n_mode, 512)

        exp5[scale_name] = {
            **_summarize(res),
            "n_mode": n_mode,
            "wavelength": 512.0 / n_mode,
            "osc_rho_std": osc_rho,
            "point_oscillation": pt_osc,
            "predicted": pred,
        }
        print(f"  {scale_name} (lam={512/n_mode:.0f}): Q_pred={pred['Q']:.2f}, "
              f"T_pred={pred['T_steps']:.0f}, osc={osc_rho['oscillations']}, "
              f"period={osc_rho.get('period', '-')}, "
              f"drift={abs(res['diagnostics']['rho_mean'][-1] - 50.0):.6f}")

    all_results["exp5_scale"] = exp5

    # ===================================================================
    # EXPERIMENT 6: 2D Oscillation Tests (TASK 6)
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXPERIMENT 6: 2D Oscillation Tests")
    print("=" * 70)
    exp6 = {}
    params_2d = EDParams(grid_size=128, n_steps=20000, dimensions=2)
    osc_2d = OscillatorParams(tau=100, zeta=0.5, rho_star=50, rho_0=0.5)

    # 6a: Random perturbations (the critical 2D test)
    rho0_2d = ic_2d_perturbed(128, 50.0, 3.0, seed=42)
    res = simulate(
        params_2d, osc_2d, rho0_2d.copy(),
        time_mode="hyperbolic", penalty_mode="sy2",
        label="sy2_2d_random",
        snapshot_interval=2000,
        track_energy=True,
    )
    osc_rho = measure_oscillation(res["diagnostics"]["rho_std"])
    exp6["random_perturb"] = {**_summarize(res), "osc_rho_std": osc_rho}
    np.save(os.path.join(results_dir, "2d_sy2_random_rho.npy"), res["final_rho"])
    rho_drift_rand = abs(res["diagnostics"]["rho_mean"][-1] - 50.0)
    print(f"  SY2 Random: rho_mean {res['diagnostics']['rho_mean'][0]:.4f} -> "
          f"{res['diagnostics']['rho_mean'][-1]:.4f} (drift={rho_drift_rand:.4f}), "
          f"osc={osc_rho['oscillations']}, clips={res['positivity_clips']}")

    # 6b: Radial perturbation
    rho0_2d = ic_2d_radial(128, 50.0, 10.0, 10.0)
    res = simulate(
        params_2d, osc_2d, rho0_2d.copy(),
        time_mode="hyperbolic", penalty_mode="sy2",
        label="sy2_2d_radial",
        snapshot_interval=2000,
    )
    osc_rho = measure_oscillation(res["diagnostics"]["rho_std"])
    exp6["radial_perturb"] = {**_summarize(res), "osc_rho_std": osc_rho}
    np.save(os.path.join(results_dir, "2d_sy2_radial_rho.npy"), res["final_rho"])
    print(f"  SY2 Radial: rho_mean {res['diagnostics']['rho_mean'][0]:.4f} -> "
          f"{res['diagnostics']['rho_mean'][-1]:.4f}, "
          f"osc={osc_rho['oscillations']}, clips={res['positivity_clips']}")

    # 6c: Directional perturbation
    rho0_2d = ic_2d_directional(128, 50.0, 5.0, 16)
    res = simulate(
        params_2d, osc_2d, rho0_2d.copy(),
        time_mode="hyperbolic", penalty_mode="sy2",
        label="sy2_2d_directional",
        snapshot_interval=2000,
    )
    osc_rho = measure_oscillation(res["diagnostics"]["rho_std"])
    exp6["directional_perturb"] = {**_summarize(res), "osc_rho_std": osc_rho}
    np.save(os.path.join(results_dir, "2d_sy2_directional_rho.npy"), res["final_rho"])
    print(f"  SY2 Directional: rho_mean {res['diagnostics']['rho_mean'][0]:.4f} -> "
          f"{res['diagnostics']['rho_mean'][-1]:.4f}, "
          f"osc={osc_rho['oscillations']}, clips={res['positivity_clips']}")

    # 6d: Mixed-mode perturbation
    rho0_2d = ic_2d_mixed(128, 50.0, 5.0, seed=42)
    res = simulate(
        params_2d, osc_2d, rho0_2d.copy(),
        time_mode="hyperbolic", penalty_mode="sy2",
        label="sy2_2d_mixed",
        snapshot_interval=2000,
    )
    osc_rho = measure_oscillation(res["diagnostics"]["rho_std"])
    exp6["mixed_perturb"] = {**_summarize(res), "osc_rho_std": osc_rho}
    np.save(os.path.join(results_dir, "2d_sy2_mixed_rho.npy"), res["final_rho"])
    print(f"  SY2 Mixed: rho_mean {res['diagnostics']['rho_mean'][0]:.4f} -> "
          f"{res['diagnostics']['rho_mean'][-1]:.4f}, "
          f"osc={osc_rho['oscillations']}, clips={res['positivity_clips']}")

    # 6e: COMPARISON — original P_SY with same IC
    rho0_2d_cmp = ic_2d_perturbed(128, 50.0, 3.0, seed=42)
    osc_sy = OscillatorParams(tau=500, zeta=0.5, rho_star=50, rho_0=0.5)  # ED-14 R3 params
    res_sy = simulate(
        params_2d, osc_sy, rho0_2d_cmp.copy(),
        time_mode="hyperbolic", penalty_mode="sy",
        label="sy_2d_random_comparison",
        snapshot_interval=2000,
    )
    osc_rho_sy = measure_oscillation(res_sy["diagnostics"]["rho_std"])
    exp6["sy_comparison"] = {**_summarize(res_sy), "osc_rho_std": osc_rho_sy}
    print(f"  P_SY Random (comparison): rho_mean {res_sy['diagnostics']['rho_mean'][0]:.4f} -> "
          f"{res_sy['diagnostics']['rho_mean'][-1]:.4f}, "
          f"osc={osc_rho_sy['oscillations']}, clips={res_sy['positivity_clips']}")

    all_results["exp6_2d"] = exp6

    # ===================================================================
    # EXPERIMENT 7: Conservation and Energy Tests (TASK 5)
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXPERIMENT 7: Conservation and Energy Tests")
    print("=" * 70)
    exp7 = {}
    params = EDParams(grid_size=512, n_steps=100000, dimensions=1)

    # Test with R1 and R3 (different damping)
    for name, tau, zeta, rstar, rho0 in [
        ("R1_baseline", 100, 1.0, 50, 0.5),
        ("R3_light_damp", 100, 0.5, 50, 0.5),
    ]:
        osc = OscillatorParams(tau=tau, zeta=zeta, rho_star=rstar, rho_0=rho0)
        rho0_ic = ic_perturbed(512, rstar, 5.0, 16)

        res = simulate(
            params, osc, rho0_ic.copy(),
            time_mode="hyperbolic", penalty_mode="sy2",
            label=f"sy2_{name}_energy",
            track_energy=True,
        )

        d = res["diagnostics"]
        E_init = d["E_total"][0] if d["E_total"] else 0
        E_final = d["E_total"][-1] if d["E_total"] else 0
        E_min = min(d["E_total"]) if d["E_total"] else 0

        # Check monotonic decrease of energy
        E_arr = np.array(d["E_total"])
        dE = np.diff(E_arr)
        n_increases = int(np.sum(dE > 1e-12))
        max_increase = float(np.max(dE)) if len(dE) > 0 else 0

        exp7[name] = {
            **_summarize(res),
            "E_initial": E_init,
            "E_final": E_final,
            "E_min": E_min,
            "energy_monotonic": n_increases == 0,
            "n_energy_increases": n_increases,
            "max_energy_increase": max_increase,
            "energy_decay_fraction": (E_init - E_final) / max(E_init, 1e-15),
        }
        print(f"  {name}: E {E_init:.6f} -> {E_final:.6f} "
              f"(decay {100*(E_init-E_final)/max(E_init,1e-15):.1f}%), "
              f"monotonic={n_increases==0} ({n_increases} increases, "
              f"max_increase={max_increase:.2e})")

    # Mode-coupling test: two modes superposed
    osc = OscillatorParams(tau=100, zeta=0.5, rho_star=50, rho_0=0.5)
    x = np.arange(512, dtype=np.float64)
    rho0_ic = 50.0 + 3.0 * np.sin(2 * np.pi * 8 * x / 512) + 3.0 * np.sin(2 * np.pi * 32 * x / 512)
    res = simulate(
        params, osc, rho0_ic.copy(),
        time_mode="hyperbolic", penalty_mode="sy2",
        label="sy2_mode_coupling",
        track_energy=True,
    )
    d = res["diagnostics"]
    exp7["mode_coupling"] = {
        **_summarize(res),
        "E_initial": d["E_total"][0] if d["E_total"] else 0,
        "E_final": d["E_total"][-1] if d["E_total"] else 0,
    }
    print(f"  Mode coupling (n=8+32): E {d['E_total'][0]:.6f} -> {d['E_total'][-1]:.6f}")

    all_results["exp7_energy"] = exp7

    # ===================================================================
    # EXPERIMENT 8: Penalty Comparison (TASK 6)
    # ===================================================================
    print("\n" + "=" * 70)
    print("EXPERIMENT 8: P_SY2 vs P_SY vs Soft-Floor Comparison")
    print("=" * 70)
    exp8 = {}

    # 8a: 1D sinusoidal perturbation
    params = EDParams(grid_size=512, n_steps=50000, dimensions=1)
    penalties_1d = [
        ("sy2", OscillatorParams(tau=100, zeta=0.5, rho_star=50, rho_0=0.5)),
        ("sy",  OscillatorParams(tau=500, zeta=0.5, rho_star=50, rho_0=0.5)),
        ("soft_floor", OscillatorParams(tau=100, zeta=0.5, rho_star=50, rho_0=0.5)),
    ]

    for pen_mode, osc_p in penalties_1d:
        rho0_ic = ic_perturbed(512, 50.0, 5.0, 16)
        res = simulate(
            params, osc_p, rho0_ic.copy(),
            time_mode="hyperbolic", penalty_mode=pen_mode,
            label=f"compare_1d_{pen_mode}",
            point_traces=[256],
        )
        osc_rho = measure_oscillation(res["diagnostics"]["rho_std"])
        pt_osc = measure_point_oscillation(
            res["traces"][256]["rho"], 50.0,
        ) if 256 in res["traces"] else {}

        key = f"1d_{pen_mode}"
        exp8[key] = {
            **_summarize(res),
            "osc_rho_std": osc_rho,
            "point_oscillation": pt_osc,
        }
        print(f"  1D {pen_mode}: rho_mean {res['diagnostics']['rho_mean'][-1]:.4f}, "
              f"osc={osc_rho['oscillations']}, damp={osc_rho.get('damping_ratio', '-')}, "
              f"clips={res['positivity_clips']}")

    # 8b: 2D random perturbation (the critical comparison)
    params_2d = EDParams(grid_size=128, n_steps=20000, dimensions=2)
    penalties_2d = [
        ("sy2", OscillatorParams(tau=100, zeta=0.5, rho_star=50, rho_0=0.5)),
        ("sy",  OscillatorParams(tau=500, zeta=0.5, rho_star=50, rho_0=0.5)),
        ("soft_floor", OscillatorParams(tau=100, zeta=0.5, rho_star=50, rho_0=0.5)),
    ]

    for pen_mode, osc_p in penalties_2d:
        rho0_2d = ic_2d_perturbed(128, 50.0, 3.0, seed=42)
        res = simulate(
            params_2d, osc_p, rho0_2d.copy(),
            time_mode="hyperbolic", penalty_mode=pen_mode,
            label=f"compare_2d_{pen_mode}",
            snapshot_interval=2000,
        )
        osc_rho = measure_oscillation(res["diagnostics"]["rho_std"])
        key = f"2d_{pen_mode}"
        exp8[key] = {
            **_summarize(res),
            "osc_rho_std": osc_rho,
        }
        drift = abs(res["diagnostics"]["rho_mean"][-1] - 50.0)
        print(f"  2D {pen_mode}: rho_mean {res['diagnostics']['rho_mean'][-1]:.4f} "
              f"(drift={drift:.4f}), osc={osc_rho['oscillations']}, "
              f"clips={res['positivity_clips']}")

    all_results["exp8_comparison"] = exp8

    # ===================================================================
    # Save all results
    # ===================================================================
    results_path = os.path.join(results_dir, "symden_results.json")
    with open(results_path, "w") as f:
        json.dump(all_results, f, indent=2, default=_json_safe)
    print(f"\nResults saved to {results_path}")

    return all_results


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
                osc_n = config_data.get("osc_rho_std", {}).get("oscillations", "-")
                if isinstance(rho_f, (int, float)):
                    rho_f = f"{rho_f:.4f}"
                print(f"  {config_name:35s}: {stable:8s}  rho_mean={rho_f}  "
                      f"osc={osc_n}  clips={clips}")
