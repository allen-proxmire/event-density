"""
ED-Phys-05: Parameter Sweep Engine
====================================
Runs systematic parameter sweeps using the ED-Phys-02 simulator,
extracts diagnostics, computes derived quantities (lambda_1, w_eff),
and saves results as CSV.

Canonical sources: ED-Phys-01 (update rule), ED-Phys-03 (epoch rates),
ED-Phys-04 (physical analogues).
"""

import sys
import os
import time
import json
import csv
import numpy as np

# Add simulator to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ED-Phys-02_Simulator'))

from ed_phys_config import EDParams
from ed_phys_lattice import create_initial_condition
from ed_phys_engine import simulate
from ed_phys_diagnostics import extract_time_series, identify_phases


def run_single(
    alpha: float,
    gamma_exp: float,
    M_0: float,
    rho_max: float,
    n_mob: int,
    ic_mode: str = "uniform_noise",
    rho_mean: float = 50.0,
    noise_amplitude: float = 0.5,
    N: int = 256,
    n_steps: int = 20000,
    cfl_safety: float = 0.4,
    seed: int = 42,
) -> dict:
    """Run a single simulation and extract summary diagnostics.

    Returns a dict with all measured quantities for one parameter point.
    """
    try:
        params = EDParams(
            alpha=alpha,
            gamma_exp=gamma_exp,
            M_0=M_0,
            rho_max=rho_max,
            n_mob=n_mob,
            gamma_b=0.0,
            dimensions=1,
            N=N,
            dx=1.0,
            cfl_safety=cfl_safety,
            n_steps=n_steps,
            record_interval=max(1, n_steps // 40),  # ~40 diagnostic points
            boundary="periodic",
        )
    except (AssertionError, ValueError) as e:
        return {"error": str(e)}

    rho_0 = create_initial_condition(
        params, mode=ic_mode, rho_mean=rho_mean,
        noise_amplitude=noise_amplitude, seed=seed,
    )

    result = simulate(params, rho_0)
    ts = extract_time_series(result)

    if not ts or len(ts["steps"]) < 4:
        return {"error": "insufficient_data"}

    steps = ts["steps"]
    grad_mean = ts["grad_mean"]
    rho_mean_ts = ts["rho_mean"]
    n_basins = ts["n_basins"]
    rho_total = ts["rho_total"]
    eta = params.eta

    # --- Compute lambda_1 (inflation rate) ---
    physical_time = steps * eta
    valid = grad_mean > 0
    if np.sum(valid) > 3:
        log_G = np.log(grad_mean[valid])
        t_valid = physical_time[valid]
        coeffs = np.polyfit(t_valid, log_G, 1)
        lambda_1 = -coeffs[0]
        G0_fit = np.exp(coeffs[1])
        residuals = log_G - (coeffs[1] + coeffs[0] * t_valid)
        ss_res = np.sum(residuals**2)
        ss_tot = np.sum((log_G - np.mean(log_G))**2)
        r_squared = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    else:
        lambda_1 = 0.0
        r_squared = 0.0
        G0_fit = 0.0

    # --- Compute lambda_2 (thinning coefficient) ---
    drho_dt = np.diff(rho_mean_ts) / np.diff(physical_time)
    G_mid = 0.5 * (grad_mean[:-1] + grad_mean[1:])
    G2_mid = G_mid**2
    valid_thin = G2_mid > 1e-20
    if np.sum(valid_thin) > 2:
        lambda_2 = float(-np.mean(drho_dt[valid_thin] / G2_mid[valid_thin]))
    else:
        lambda_2 = 0.0

    # --- Thinning rate ---
    total_rho_change = float(rho_total[-1] - rho_total[0])
    pct_rho_change = 100.0 * total_rho_change / rho_total[0] if rho_total[0] > 0 else 0.0

    # --- Basin trajectory ---
    basins_initial = int(n_basins[0])
    basins_final = int(n_basins[-1])
    basins_max = int(np.max(n_basins))
    basins_grew = bool(np.any(np.diff(n_basins) > 0))

    # --- Scale factor ---
    a_initial = 1.0 / grad_mean[0] if grad_mean[0] > 0 else float('inf')
    a_final = 1.0 / grad_mean[-1] if grad_mean[-1] > 0 else float('inf')
    scale_factor_ratio = a_final / a_initial if a_initial > 0 and np.isfinite(a_initial) else float('inf')

    # --- Horizon candidates ---
    rho_f = result.rho_final
    horizon_frac = float(np.sum(rho_f > 0.9 * rho_max) / rho_f.size)
    rho_final_max = float(np.max(rho_f))
    rho_final_min = float(np.min(rho_f))
    rho_final_std = float(np.std(rho_f))

    # --- Curvature statistics ---
    from ed_phys_operators import discrete_laplacian
    lap_final = discrete_laplacian(rho_f, 1.0, "periodic")
    lap_pos_frac = float(np.sum(lap_final > 0) / lap_final.size)
    lap_mean = float(np.mean(lap_final))
    lap_std = float(np.std(lap_final))

    # --- Equation of state proxy (ED-Phys-04 Section 13.2) ---
    if lambda_1 > 0 and rho_mean_ts[0] > 0:
        w_eff = (lambda_2 * grad_mean[0]**2) / (3.0 * lambda_1 * rho_mean_ts[0]) - 1.0
    else:
        w_eff = float('nan')

    # --- Phase identification ---
    phases = identify_phases(result)
    phase_names = [p["name"] for p in phases]
    has_inflation = "inflation" in phase_names
    has_structure = "structure_formation" in phase_names
    has_residual = "residual_gradient" in phase_names
    has_thinning = "thinning" in phase_names
    has_heat_death = "heat_death" in phase_names

    return {
        # Input parameters
        "alpha": alpha,
        "gamma_exp": gamma_exp,
        "M_0": M_0,
        "rho_max": rho_max,
        "n_mob": n_mob,
        "ic_mode": ic_mode,
        "rho_mean_ic": rho_mean,
        "noise_amplitude": noise_amplitude,
        "eta": eta,
        "n_steps": n_steps,
        # Inflation
        "lambda_1": lambda_1,
        "lambda_1_r2": r_squared,
        "G0_fit": G0_fit,
        # Thinning
        "lambda_2": lambda_2,
        "total_rho_change_pct": pct_rho_change,
        # Scale factor
        "scale_factor_ratio": scale_factor_ratio,
        # Basins
        "basins_initial": basins_initial,
        "basins_final": basins_final,
        "basins_max": basins_max,
        "basins_grew": basins_grew,
        # Horizons
        "horizon_frac": horizon_frac,
        "rho_final_max": rho_final_max,
        "rho_final_min": rho_final_min,
        "rho_final_std": rho_final_std,
        # Curvature
        "lap_pos_frac": lap_pos_frac,
        "lap_mean": lap_mean,
        "lap_std": lap_std,
        # Equation of state
        "w_eff": w_eff,
        # Phases
        "has_inflation": has_inflation,
        "has_structure_formation": has_structure,
        "has_residual_gradient": has_residual,
        "has_thinning": has_thinning,
        "has_heat_death": has_heat_death,
        "phase_sequence": " -> ".join(phase_names),
        # Metadata
        "error": "",
    }


def save_sweep_csv(results: list[dict], filepath: str):
    """Save sweep results as CSV."""
    if not results:
        return
    keys = results[0].keys()
    with open(filepath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)


def run_sweep(
    param_grid: list[dict],
    label: str = "sweep",
    output_dir: str = "results",
) -> list[dict]:
    """Run a sweep over a list of parameter dicts."""
    results = []
    n_total = len(param_grid)
    t0 = time.time()

    for i, params in enumerate(param_grid):
        r = run_single(**params)
        # Merge input params into result for traceability
        for k, v in params.items():
            if k not in r:
                r[k] = v
        results.append(r)

        if (i + 1) % 10 == 0 or (i + 1) == n_total:
            elapsed = time.time() - t0
            rate = (i + 1) / elapsed
            remaining = (n_total - i - 1) / rate if rate > 0 else 0
            print(f"  [{i+1}/{n_total}] {elapsed:.1f}s elapsed, "
                  f"~{remaining:.0f}s remaining")

    filepath = os.path.join(output_dir, f"{label}.csv")
    save_sweep_csv(results, filepath)
    print(f"  Saved {len(results)} results to {filepath}")
    return results


if __name__ == "__main__":
    # Quick test
    r = run_single(alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
                   n_steps=5000)
    for k, v in r.items():
        print(f"  {k}: {v}")
