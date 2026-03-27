"""
broadband_cascade.py
=====================
Experiment: Broadband Cascade Dynamics (Atlas §4, Suite §3)

Investigates the spectral cascade when a dense block of modes is seeded
simultaneously, activating a large triad network. This is the most
physically realistic initial condition — analogous to a broadband
perturbation or thermal fluctuation — and produces the richest cascade
structure in the modal hierarchy.

Initial conditions (equal amplitude per mode):
  IC1: modes 1–10     — moderate breadth, 45 active triads
  IC2: modes 1–20     — wide breadth, 190 active triads
  IC3: modes 5–25     — shifted window, 210 triads, novel low-k generation
  IC4: modes 1–30     — stress test, 435 triads, deep forward cascade

The number of active triads scales as N_m*(N_m-1)/2 where N_m is the
number of seeded modes. The forward cascade can generate modes up to
2*k_max; the inverse cascade can generate modes down to 1 (or 0 for
even-spaced seeds).

Uses Parameter Set I (deep oscillatory, same as modal_hierarchy.py and
three_stage_convergence.py).

Output directories:
  output/runs/broadband_IC1
  output/runs/broadband_IC2
  output/runs/broadband_IC3
  output/runs/broadband_IC4

Usage:
    python experiments/broadband_cascade.py

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

PARAM_SET = "I"
A = 0.02                 # Per-mode amplitude (small for dense seeding)
T = 20.0                 # Final time (longer than triad_cascade to let
                         # the deep cascade develop and begin decaying)
METHOD = "crank_nicolson"
K_OUT = 10               # Output every K_OUT steps

# N_OBS must cover the forward cascade: up to ~2*k_max of the widest IC
N_OBS = 64

# Initial conditions: dense blocks of modes
IC_SPECS = {
    "IC1": {
        "modes": list(range(1, 11)),    # 1–10
        "description": "Moderate breadth: modes 1-10, 45 triads",
    },
    "IC2": {
        "modes": list(range(1, 21)),    # 1–20
        "description": "Wide breadth: modes 1-20, 190 triads",
    },
    "IC3": {
        "modes": list(range(5, 26)),    # 5–25
        "description": "Shifted window: modes 5-25, 210 triads, inverse cascade to low-k",
    },
    "IC4": {
        "modes": list(range(1, 31)),    # 1–30
        "description": "Stress test: modes 1-30, 435 triads, deep forward cascade",
    },
}


# ---------------------------------------------------------------------------
#  Helpers
# ---------------------------------------------------------------------------

def build_broadband_ic(x: np.ndarray, params, modes: list, A_per_mode: float):
    """Construct initial density by summing Neumann eigenmodes.

    rho(x, 0) = rho* + A_per_mode * sum_{n in modes} cos(n * pi * x / L)
    v(0) = 0

    For dense seeding the total perturbation amplitude is A * N_m, so
    A must be small enough that rho stays in (0, rho_max).
    """
    rho0 = np.full_like(x, params.rho_star)
    for n in modes:
        rho0 += A_per_mode * np.cos(n * np.pi * x / params.L)

    # Safety clamp — should not trigger at A = 0.02 with N_m <= 30
    rho0 = np.clip(rho0, 1e-12, params.rho_max - 1e-12)
    v0 = 0.0
    return rho0, v0


def triad_statistics(modes: list) -> dict:
    """Compute summary statistics of the triad network.

    Returns dict with:
      n_triads:       number of active (m,n) pairs
      forward_max:    highest mode reachable by m+n
      inverse_min:    lowest mode reachable by |m-n|
      all_targets:    sorted list of all target modes
      novel_targets:  targets not in the seeded set
      feedback_count: number of targets that coincide with seeded modes
    """
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


def run_single_ic(label: str, spec: dict, verbose: bool = True) -> dict:
    """Run a single broadband-cascade experiment."""
    modes = spec["modes"]
    description = spec["description"]
    run_id = f"broadband_{label}"
    n_modes = len(modes)

    if verbose:
        print(f"\n{'='*60}")
        print(f"  {run_id}")
        print(f"  Modes: {modes[0]}–{modes[-1]} ({n_modes} modes), A = {A}")
        print(f"  {description}")
        print(f"{'='*60}")

    # Triad network analysis
    stats = triad_statistics(modes)
    if verbose:
        print(f"  Triad network:")
        print(f"    Active pairs:   {stats['n_triads']}")
        print(f"    Forward max:    mode {stats['forward_max']}")
        print(f"    Inverse min:    mode {stats['inverse_min']}")
        print(f"    Novel targets:  {len(stats['novel_targets'])} modes")
        print(f"    Feedback:       {stats['feedback_count']} modes overlap with seeds")

    # Check that the total perturbation amplitude is safe
    total_amp = A * n_modes
    params_check = load_parameter_set(PARAM_SET)
    headroom = min(params_check.rho_star, params_check.rho_max - params_check.rho_star)
    if total_amp > 0.8 * headroom:
        print(f"  WARNING: total perturbation A*N_m = {total_amp:.3f} is "
              f"{total_amp/headroom:.0%} of headroom {headroom:.3f}. "
              f"Consider reducing A.")

    # Load parameters
    params = load_parameter_set(PARAM_SET, T=T, method=METHOD, k_out=K_OUT)

    # Build initial condition
    x = make_grid(params)
    rho0, v0 = build_broadband_ic(x, params, modes, A)

    if verbose:
        print(f"  IC range: rho in [{rho0.min():.6f}, {rho0.max():.6f}]")
        print(f"  Admissible: (0, {params.rho_max}), rho* = {params.rho_star}")

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
        "experiment": "broadband_cascade",
        "ic_label": label,
        "description": description,
        "seeded_modes": modes,
        "seeded_range": [modes[0], modes[-1]],
        "n_seeded": n_modes,
        "A_per_mode": A,
        "total_amplitude": A * n_modes,
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
        "ic_name": "custom_broadband",
        "ic_kwargs": {"modes": modes, "A": A},
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
#  Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("  Broadband Cascade Experiment")
    print(f"  Parameter Set {PARAM_SET}, A = {A}, T = {T}")
    print("=" * 60)

    results = {}
    for label in sorted(IC_SPECS.keys()):
        spec = IC_SPECS[label]
        results[label] = run_single_ic(label, spec, verbose=True)

    # --- Cross-IC summary ---
    print("\n" + "=" * 78)
    print("  Cross-IC Summary")
    print("=" * 78)
    print(f"  {'IC':<6} {'Range':<10} {'#Modes':<8} {'#Triads':<10} "
          f"{'Fwd max':<10} {'E(0)':<14} {'E(T)':<14} {'Wall(s)':<10}")
    print("  " + "-" * 82)

    for label in sorted(results.keys()):
        ts = results[label]["time_series"]
        meta = results[label]["metadata"]
        modes = meta["seeded_modes"]
        tri = meta["triad_statistics"]

        print(f"  {label:<6} {modes[0]}-{modes[-1]:<7} {len(modes):<8} "
              f"{tri['n_triads']:<10} {tri['forward_max']:<10} "
              f"{ts['E_total'][0]:<14.6e} {ts['E_total'][-1]:<14.6e} "
              f"{meta['wall_time_s']:<10.1f}")

    print(f"\nAll runs saved to: output/runs/broadband_IC{{1,2,3,4}}")
    print("Done.")


if __name__ == "__main__":
    main()
