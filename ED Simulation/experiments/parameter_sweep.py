"""
parameter_sweep.py
==================
Experiment: Diffusion-Coefficient Sweep (Atlas §8.3, Suite §4.1)

Varies the diffusion coefficient D across five values while holding all other
canonical parameters (zeta, tau, rho_star, rho_max, constitutive functions)
fixed at Parameter Set I. Each run uses the same broadband initial condition
(modes 1–20, equal amplitude A = 0.02), identical to broadband_cascade IC2.

This isolates the effect of D on:
  - energy decay rate
  - modal hierarchy (the eigenvalues alpha_k scale as D * (k*pi/L)^2)
  - regime geometry (the discriminant Delta depends on D)
  - triad coupling strength
  - convergence stage durations

The sweep directly validates Atlas Figures 8.5–8.8 and the regime-map
predictions of Appendix C.3.

Sweep values:
  D = 0.1, 0.2, 0.5, 1.0, 2.0

Output directories:
  output/runs/param_D0p1
  output/runs/param_D0p2
  output/runs/param_D0p5
  output/runs/param_D1p0
  output/runs/param_D2p0

Usage:
    python experiments/parameter_sweep.py

All notation follows Appendix C of the Rigour Paper.
"""

import os
import sys
import json
import time as _time
import numpy as np

# Allow imports from the parent ED Simulation directory
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from edsim_parameters import load_parameter_set
from edsim_runner import (
    RunConfig, TimeSeries, ensure_dirs,
    diagnostic_snapshot, enforce_bounds,
)
from edsim_core import make_grid, step


# ---------------------------------------------------------------------------
#  Configuration
# ---------------------------------------------------------------------------

PARAM_SET = "I"               # Baseline parameter set
A = 0.02                      # Per-mode amplitude
T = 20.0                      # Final time
METHOD = "crank_nicolson"
K_OUT = 10                    # Output every K_OUT steps
N_OBS = 64                    # Observable modes (covers forward cascade)

# Broadband IC: modes 1–20 (same as broadband_cascade IC2)
SEEDED_MODES = list(range(1, 21))

# Sweep parameter
D_VALUES = [0.1, 0.2, 0.5, 1.0, 2.0]

# Mapping from D value to output folder name
def d_to_folder(D: float) -> str:
    """Convert D value to a safe folder name: 0.1 -> 'param_D0p1'."""
    s = f"{D:.1f}".replace(".", "p")
    return f"param_D{s}"


# ---------------------------------------------------------------------------
#  Helpers (reused from broadband_cascade)
# ---------------------------------------------------------------------------

def build_broadband_ic(x: np.ndarray, params, modes: list, A_per_mode: float):
    """Construct initial density by summing Neumann eigenmodes.

    rho(x, 0) = rho* + A_per_mode * sum_{n in modes} cos(n * pi * x / L)
    v(0) = 0
    """
    rho0 = np.full_like(x, params.rho_star)
    for n in modes:
        rho0 += A_per_mode * np.cos(n * np.pi * x / params.L)

    # Safety clamp
    rho0 = np.clip(rho0, 1e-12, params.rho_max - 1e-12)
    v0 = 0.0
    return rho0, v0


def triad_statistics(modes: list) -> dict:
    """Compute summary statistics of the triad network."""
    seeded_set = set(modes)
    all_tgt = set()
    n_triads = 0

    for i, m in enumerate(modes):
        for j, n in enumerate(modes):
            if j <= i:
                continue
            n_triads += 1
            all_tgt.add(m + n)
            all_tgt.add(abs(m - n))

    novel = sorted(all_tgt - seeded_set)
    feedback = sorted(all_tgt & seeded_set)

    return {
        "n_triads": n_triads,
        "forward_max": max(m + n for i, m in enumerate(modes)
                          for j, n in enumerate(modes) if j > i),
        "inverse_min": min(abs(m - n) for i, m in enumerate(modes)
                          for j, n in enumerate(modes) if j > i),
        "all_targets": sorted(all_tgt),
        "novel_targets": novel,
        "feedback_count": len(feedback),
        "feedback_targets": feedback,
    }


def compute_discriminant(D: float, zeta: float, tau: float, P_prime: float) -> float:
    """Compute the damping discriminant Delta (Appendix C.3).

    Delta = (D*P_prime + zeta/tau)^2 / (4 * D * P_prime * zeta / tau)

    The regime is oscillatory (Spiral Sheet) if Delta < 1,
    overdamped (Monotonic Cone) if Delta > 1.
    """
    numer = (D * P_prime + zeta / tau) ** 2
    denom = 4.0 * D * P_prime * zeta / tau
    if denom < 1e-30:
        return float("inf")
    return numer / denom


def _json_default(obj):
    """JSON serializer for numpy types."""
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.floating,)):
        return float(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, set):
        return sorted(obj)
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


# ---------------------------------------------------------------------------
#  Single-D runner
# ---------------------------------------------------------------------------

def run_single_D(D_val: float, verbose: bool = True) -> dict:
    """Run the broadband IC at a single D value."""
    folder = d_to_folder(D_val)
    run_id = folder

    if verbose:
        print(f"\n{'='*60}")
        print(f"  {run_id}  (D = {D_val})")
        print(f"  Modes: {SEEDED_MODES[0]}–{SEEDED_MODES[-1]} "
              f"({len(SEEDED_MODES)} modes), A = {A}")
        print(f"{'='*60}")

    # Load Parameter Set I with D overridden
    params = load_parameter_set(
        PARAM_SET,
        T=T,
        method=METHOD,
        k_out=K_OUT,
        D=D_val,
    )

    # Compute the discriminant at this D
    # P'(rho*) is available from the constitutive functions
    # For Parameter Set I: P(rho) = P0 * (rho - rho*)^2 / 2
    # => P'(rho*) = 0, but the linearized operator uses P''(rho*) * (rho - rho*)
    # The effective penalty derivative at equilibrium:
    P_star_prime = params.P0  # P'_eff at rho* (from the canonical form)
    Delta = compute_discriminant(D_val, params.zeta, params.tau, P_star_prime)

    regime = "oscillatory (Spiral Sheet)" if Delta < 1.0 else (
        "critical" if abs(Delta - 1.0) < 0.01 else "overdamped (Monotonic Cone)")

    if verbose:
        print(f"  Discriminant Delta = {Delta:.4f} => {regime}")

    # Triad statistics (same for all D)
    stats = triad_statistics(SEEDED_MODES)

    # Build initial condition
    x = make_grid(params)
    rho0, v0 = build_broadband_ic(x, params, SEEDED_MODES, A)

    if verbose:
        print(f"  IC range: rho in [{rho0.min():.6f}, {rho0.max():.6f}]")

    # Prepare output directory
    out_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "output", "runs", run_id,
    )
    ensure_dirs()
    os.makedirs(out_dir, exist_ok=True)

    # --- Integration loop ---
    t_val = 0.0
    rho = rho0.copy()
    v = v0
    N_steps = int(np.ceil(params.T / params.dt))

    ts = TimeSeries(N_obs=N_OBS)
    snap0 = diagnostic_snapshot(rho, v, t_val, params, N_OBS)
    ts.append(snap0)

    wall_start = _time.perf_counter()
    n_pos_violations = 0
    n_cap_violations = 0
    report_interval = max(N_steps // 10, 1)

    for step_n in range(1, N_steps + 1):
        t_val = step_n * params.dt
        res = step(rho, v, params)
        rho = res["rho"]
        v = res["v"]

        rho, pos_flag, cap_flag = enforce_bounds(rho, params)
        if pos_flag:
            n_pos_violations += 1
        if cap_flag:
            n_cap_violations += 1

        if step_n % params.k_out == 0 or step_n == N_steps:
            snap = diagnostic_snapshot(rho, v, t_val, params, N_OBS)
            ts.append(snap)

        if verbose and step_n % report_interval == 0:
            pct = 100.0 * step_n / N_steps
            elapsed = _time.perf_counter() - wall_start
            print(f"    t = {t_val:.4f}  ({pct:.0f}%)  [{elapsed:.1f}s]")

    wall_time = _time.perf_counter() - wall_start
    ts_arrays = ts.to_arrays()

    # --- Save time_series.npz ---
    ts_path = os.path.join(out_dir, "time_series.npz")
    np.savez_compressed(ts_path, **ts_arrays)
    if verbose:
        print(f"  Saved: {ts_path}")

    # --- Save final_state.npz ---
    final_path = os.path.join(out_dir, "final_state.npz")
    np.savez_compressed(
        final_path,
        rho=rho,
        v=np.array([v]),
        t=np.array([t_val]),
    )

    # --- Save metadata.json ---
    metadata = {
        "run_id": run_id,
        "experiment": "parameter_sweep_D",
        "sweep_parameter": "D",
        "D_sweep_value": D_val,
        "description": f"D-sweep at D={D_val}, broadband IC modes 1-20",
        "seeded_modes": SEEDED_MODES,
        "seeded_range": [SEEDED_MODES[0], SEEDED_MODES[-1]],
        "n_seeded": len(SEEDED_MODES),
        "A_per_mode": A,
        "total_amplitude": A * len(SEEDED_MODES),
        "param_set": PARAM_SET,
        "D": params.D,
        "zeta": params.zeta,
        "tau": params.tau,
        "rho_star": params.rho_star,
        "rho_max": params.rho_max,
        "M0": params.M0,
        "beta": params.beta,
        "P0": params.P0,
        "N": params.N,
        "L": params.L,
        "dt": params.dt,
        "T": params.T,
        "method": params.method,
        "k_out": params.k_out,
        "N_obs": N_OBS,
        "n_steps": N_steps,
        "final_t": t_val,
        "wall_time_s": wall_time,
        "n_positivity_violations": n_pos_violations,
        "n_capacity_violations": n_cap_violations,
        "termination_reason": "FinalTime",
        "discriminant_Delta": Delta,
        "regime": regime,
        "ic_name": "custom_broadband",
        "ic_kwargs": {"modes": SEEDED_MODES, "A": A},
        "triad_statistics": {
            "n_triads": stats["n_triads"],
            "forward_max": stats["forward_max"],
            "inverse_min": stats["inverse_min"],
            "n_novel_targets": len(stats["novel_targets"]),
            "n_feedback_targets": stats["feedback_count"],
        },
        "timestamp": _time.strftime("%Y-%m-%dT%H:%M:%SZ", _time.gmtime()),
    }

    meta_path = os.path.join(out_dir, "metadata.json")
    with open(meta_path, "w") as f:
        json.dump(metadata, f, indent=2, default=_json_default)
    if verbose:
        print(f"  Saved: {meta_path}")

    # --- Summary ---
    if verbose:
        E_init = ts_arrays["E_total"][0]
        E_final = ts_arrays["E_total"][-1]
        C_init = ts_arrays["C_ED"][0]
        C_final = ts_arrays["C_ED"][-1]
        print(f"\n  Summary:")
        print(f"    D = {D_val},  Delta = {Delta:.4f},  regime = {regime}")
        print(f"    Wall time:          {wall_time:.2f} s")
        print(f"    Steps:              {N_steps}")
        print(f"    E(0) = {E_init:.6e},  E(T) = {E_final:.6e}")
        print(f"    C_ED(0) = {C_init:.6e},  C_ED(T) = {C_final:.6e}")
        print(f"    Positivity violations: {n_pos_violations}")
        print(f"    Capacity violations:   {n_cap_violations}")

    return {
        "time_series": ts_arrays,
        "metadata": metadata,
    }


# ---------------------------------------------------------------------------
#  Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("  Parameter Sweep: Diffusion Coefficient D")
    print(f"  Baseline: Parameter Set {PARAM_SET}")
    print(f"  IC: modes {SEEDED_MODES[0]}–{SEEDED_MODES[-1]}, A = {A}")
    print(f"  D values: {D_VALUES}")
    print(f"  T = {T}, method = {METHOD}")
    print("=" * 60)

    results = {}
    for D_val in D_VALUES:
        results[D_val] = run_single_D(D_val, verbose=True)

    # --- Cross-D summary ---
    print("\n" + "=" * 90)
    print("  Parameter Sweep Summary: D")
    print("=" * 90)
    print(f"  {'D':<8} {'Delta':<10} {'Regime':<22} "
          f"{'E(0)':<14} {'E(T)':<14} {'E(T)/E(0)':<12} {'Wall(s)':<10}")
    print("  " + "-" * 92)

    for D_val in D_VALUES:
        meta = results[D_val]["metadata"]
        ts = results[D_val]["time_series"]
        E0 = ts["E_total"][0]
        ET = ts["E_total"][-1]
        ratio = ET / max(E0, 1e-30)
        regime_short = meta["regime"].split("(")[0].strip()

        print(f"  {D_val:<8.1f} {meta['discriminant_Delta']:<10.4f} "
              f"{regime_short:<22} {E0:<14.6e} {ET:<14.6e} "
              f"{ratio:<12.4e} {meta['wall_time_s']:<10.1f}")

    # --- Regime transitions ---
    print("\n  Regime transitions:")
    prev_regime = None
    for D_val in D_VALUES:
        regime = results[D_val]["metadata"]["regime"]
        if prev_regime is not None and regime != prev_regime:
            print(f"    Transition between D = {D_VALUES[D_VALUES.index(D_val)-1]} "
                  f"and D = {D_val}: {prev_regime} -> {regime}")
        prev_regime = regime

    folders = [d_to_folder(D) for D in D_VALUES]
    print(f"\nAll runs saved to: output/runs/{{{','.join(folders)}}}")
    print("Done.")


if __name__ == "__main__":
    main()
