"""
overlap_cascade.py
===================
Experiment: Overlapping Triad Cascade Dynamics (Atlas §4, Suite §3)

Investigates the spectral cascade when multiple triads share common modes,
creating coupled energy-transfer pathways. Seeds clusters of modes whose
pairwise triads overlap, producing richer cascade dynamics than the
isolated-triad experiments of triad_cascade.py.

Initial conditions:
  IC1: modes {1, 2, 3}      -- triads sharing mode 2
       Active triads: (1,2)→{3,1}, (1,3)→{4,2}, (2,3)→{5,1}
       Mode 1 is both seeded and a triad target: energy fed back into source.

  IC2: modes {1, 2, 3, 5}   -- triads sharing mode 3
       Active triads: (1,2)→{3,1}, (1,3)→{4,2}, (2,3)→{5,1},
                      (1,5)→{6,4}, (2,5)→{7,3}, (3,5)→{8,2}
       Modes 1, 2, 3 appear as both sources and targets: strongly coupled.

  IC3: modes {2, 3, 5}      -- extended overlap with gap
       Active triads: (2,3)→{5,1}, (2,5)→{7,3}, (3,5)→{8,2}
       Mode 5 is both seeded and a triad target of (2,3): resonant overlap.
       Mode 3 is both seeded and a target of (2,5): double overlap.

Uses Parameter Set I (deep oscillatory, same as modal_hierarchy.py and
three_stage_convergence.py).

Output directories:
  output/runs/overlap_cascade_IC1
  output/runs/overlap_cascade_IC2
  output/runs/overlap_cascade_IC3

Usage:
    python experiments/overlap_cascade.py

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
A = 0.05                 # Per-mode amplitude (weakly nonlinear regime)
T = 15.0                 # Final time
METHOD = "crank_nicolson"
K_OUT = 10               # Output every K_OUT steps
N_OBS = 32               # Track 32 modal amplitudes

# Initial conditions: overlapping-triad clusters
IC_SPECS = {
    "IC1": {
        "modes": [1, 2, 3],
        "description": "Triads sharing mode 2: (1,2)->{3,1}, (1,3)->{4,2}, (2,3)->{5,1}",
    },
    "IC2": {
        "modes": [1, 2, 3, 5],
        "description": "Triads sharing mode 3: six active triads, strongly coupled",
    },
    "IC3": {
        "modes": [2, 3, 5],
        "description": "Extended overlap with gap: mode 5 seeded and target of (2,3)",
    },
}


# ---------------------------------------------------------------------------
#  Helpers
# ---------------------------------------------------------------------------

def build_multimode_ic(x: np.ndarray, params, modes: list, A_per_mode: float):
    """Construct initial density by summing Neumann eigenmodes.

    rho(x, 0) = rho* + A_per_mode * sum_{n in modes} cos(n * pi * x / L)
    v(0) = 0
    """
    rho0 = np.full_like(x, params.rho_star)
    for n in modes:
        rho0 += A_per_mode * np.cos(n * np.pi * x / params.L)
    rho0 = np.clip(rho0, 1e-12, params.rho_max - 1e-12)
    v0 = 0.0
    return rho0, v0


def triad_targets(modes: list) -> dict:
    """Compute all pairwise triad-predicted target modes.

    Returns {(m,n): [target1, target2]} for each unordered pair.
    """
    targets = {}
    for i, m in enumerate(modes):
        for j, n in enumerate(modes):
            if j <= i:
                continue
            targets[(m, n)] = sorted({m + n, abs(m - n)})
    return targets


def overlap_analysis(modes: list) -> dict:
    """Analyze the overlap structure of the seeded mode set.

    Returns dict with:
      - all_targets: set of all triad-generated modes
      - novel_targets: targets not in the seeded set
      - feedback_targets: targets that are also seeded (energy feedback)
      - triad_map: {(m,n): [targets]}
    """
    seeded_set = set(modes)
    tmap = triad_targets(modes)

    all_tgt = set()
    for tlist in tmap.values():
        all_tgt.update(tlist)

    novel = all_tgt - seeded_set
    feedback = all_tgt & seeded_set

    return {
        "all_targets": sorted(all_tgt),
        "novel_targets": sorted(novel),
        "feedback_targets": sorted(feedback),
        "triad_map": {f"({m},{n})": t for (m, n), t in sorted(tmap.items())},
    }


def run_single_ic(label: str, spec: dict, verbose: bool = True) -> dict:
    """Run a single overlap-cascade experiment.

    Parameters
    ----------
    label : IC label string ("IC1", "IC2", etc.)
    spec : dict with keys "modes", "description"
    verbose : print progress

    Returns
    -------
    dict with keys: time_series (dict of arrays), metadata (dict)
    """
    modes = spec["modes"]
    description = spec["description"]
    run_id = f"overlap_cascade_{label}"

    if verbose:
        print(f"\n{'='*60}")
        print(f"  {run_id}")
        print(f"  Seeded modes: {modes},  A = {A}")
        print(f"  {description}")
        print(f"{'='*60}")

    # Overlap analysis
    overlap = overlap_analysis(modes)
    if verbose:
        print(f"  Triad map:")
        for pair, tgt in sorted(overlap["triad_map"].items()):
            print(f"    {pair} -> {tgt}")
        print(f"  Novel targets:    {overlap['novel_targets']}")
        print(f"  Feedback targets: {overlap['feedback_targets']}")

    # Load parameters
    params = load_parameter_set(PARAM_SET, T=T, method=METHOD, k_out=K_OUT)

    # Build initial condition
    x = make_grid(params)
    rho0, v0 = build_multimode_ic(x, params, modes, A)

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

        if verbose and step_n % (N_steps // 10 or 1) == 0:
            pct = 100.0 * step_n / N_steps
            print(f"    t = {t_val:.4f}  ({pct:.0f}%)")

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
        "experiment": "overlap_cascade",
        "ic_label": label,
        "description": description,
        "seeded_modes": modes,
        "A_per_mode": A,
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
        "ic_name": "custom_multimode",
        "ic_kwargs": {"modes": modes, "A": A},
        "overlap_analysis": {
            "triad_map": overlap["triad_map"],
            "novel_targets": overlap["novel_targets"],
            "feedback_targets": overlap["feedback_targets"],
            "all_targets": overlap["all_targets"],
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
        print(f"    Novel targets:      {overlap['novel_targets']}")
        print(f"    Feedback targets:   {overlap['feedback_targets']}")

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
    print("  Overlapping Triad Cascade Experiment")
    print(f"  Parameter Set {PARAM_SET}, A = {A}, T = {T}")
    print("=" * 60)

    results = {}
    for label in sorted(IC_SPECS.keys()):
        spec = IC_SPECS[label]
        results[label] = run_single_ic(label, spec, verbose=True)

    # --- Cross-IC summary ---
    print("\n" + "=" * 70)
    print("  Cross-IC Summary")
    print("=" * 70)
    print(f"  {'IC':<6} {'Seeded':<16} {'Novel':<16} {'Feedback':<12} "
          f"{'E(0)':<14} {'E(T)':<14}")
    print("  " + "-" * 78)

    for label in sorted(results.keys()):
        ts = results[label]["time_series"]
        meta = results[label]["metadata"]
        modes = meta["seeded_modes"]
        overlap = meta["overlap_analysis"]

        print(f"  {label:<6} {str(modes):<16} "
              f"{str(overlap['novel_targets']):<16} "
              f"{str(overlap['feedback_targets']):<12} "
              f"{ts['E_total'][0]:<14.6e} {ts['E_total'][-1]:<14.6e}")

    print(f"\nAll runs saved to: output/runs/overlap_cascade_IC{{1,2,3}}")
    print("Done.")


if __name__ == "__main__":
    main()
