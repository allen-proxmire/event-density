"""
low_mode_attractor.py
=====================
Experiment: Low-Mode Attractor Convergence (Atlas §7, Appendix C.7)

Investigates the long-time behavior of the canonical ED system by running
diverse initial conditions to long final times. All solutions should converge
to the unique equilibrium (rho*, 0) regardless of the initial condition,
confirming Theorem C.76 (three-stage convergence) and the uniqueness of the
omega-limit set (Proposition C.72).

The experiment probes the attractor from five qualitatively different
directions in state space:

  IC1: Dense broadband block 1-30  (widest triad network, 435 triads)
  IC2: Dense broadband block 1-20  (moderate network, 190 triads)
  IC3: Triad cluster [1,2,3,5]     (sparse seeding, targeted overlap)
  IC4: Random-phase broadband 1-30 (random signs break constructive piling)
  IC5: High-mode-only 20-40        (tests inverse cascade to low k)

The key observable is universality: all five ICs must converge to the same
equilibrium, with the same late-time exponential rate sigma = D*alpha_1 + P*',
despite vastly different transient dynamics. The convergence path exhibits
the three stages (global bounds -> algebraic -> exponential), with the
transition time t* depending on the initial ED-complexity.

Uses Parameter Set I (deep oscillatory, same as all other experiments).

Output directories:
  output/runs/attractor_IC1
  output/runs/attractor_IC2
  output/runs/attractor_IC3
  output/runs/attractor_IC4
  output/runs/attractor_IC5

Usage:
    python experiments/low_mode_attractor.py

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
A = 0.02                 # Per-mode amplitude
T = 100.0                # Long final time for attractor convergence
METHOD = "crank_nicolson"
K_OUT = 20               # Output every K_OUT steps (long runs produce many steps)

# N_OBS covers forward cascade from widest IC (modes up to 80)
N_OBS = 80

# Random seed for IC4 (deterministic reproducibility)
RANDOM_SEED = 20260326


# ---------------------------------------------------------------------------
#  Initial condition specifications
# ---------------------------------------------------------------------------

IC_SPECS = {
    "IC1": {
        "modes": list(range(1, 31)),
        "signs": None,          # all positive
        "description": "Dense broadband 1-30 (435 triads, stress test)",
    },
    "IC2": {
        "modes": list(range(1, 21)),
        "signs": None,
        "description": "Dense broadband 1-20 (190 triads, moderate network)",
    },
    "IC3": {
        "modes": [1, 2, 3, 5],
        "signs": None,
        "description": "Triad cluster [1,2,3,5] (sparse, overlapping triads)",
    },
    "IC4": {
        "modes": list(range(1, 31)),
        "signs": "random",      # random +/- per mode
        "description": "Random-phase broadband 1-30 (random signs, 435 triads)",
    },
    "IC5": {
        "modes": list(range(20, 41)),
        "signs": None,
        "description": "High-mode-only 20-40 (tests inverse cascade to low k)",
    },
}


# ---------------------------------------------------------------------------
#  Helpers
# ---------------------------------------------------------------------------

def build_attractor_ic(
    x: np.ndarray,
    params,
    modes: list,
    A_per_mode: float,
    signs: np.ndarray | None = None,
) -> tuple:
    """Construct initial density from a sum of Neumann eigenmodes.

    rho(x, 0) = rho* + sum_{n in modes} s_n * A * cos(n * pi * x / L)
    v(0) = 0

    Parameters
    ----------
    x : grid points
    params : canonical parameter object
    modes : list of mode indices
    A_per_mode : amplitude per mode
    signs : array of +1/-1 per mode (None = all +1)

    Returns
    -------
    rho0, v0
    """
    rho0 = np.full_like(x, params.rho_star)

    if signs is None:
        signs = np.ones(len(modes))

    for i, n in enumerate(modes):
        rho0 += signs[i] * A_per_mode * np.cos(n * np.pi * x / params.L)

    # Safety clamp
    rho0 = np.clip(rho0, 1e-12, params.rho_max - 1e-12)
    v0 = 0.0
    return rho0, v0


def generate_random_signs(n_modes: int, seed: int) -> np.ndarray:
    """Generate deterministic random +1/-1 signs."""
    rng = np.random.RandomState(seed)
    return rng.choice([-1.0, 1.0], size=n_modes)


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

    fwd_max = max(m + n for i, m in enumerate(modes)
                  for j, n in enumerate(modes) if j > i) if n_triads > 0 else 0
    inv_min = min(abs(m - n) for i, m in enumerate(modes)
                  for j, n in enumerate(modes) if j > i) if n_triads > 0 else 0

    return {
        "n_triads": n_triads,
        "forward_max": fwd_max,
        "inverse_min": inv_min,
        "all_targets": sorted(all_tgt),
        "novel_targets": novel,
        "feedback_count": len(feedback),
        "feedback_targets": feedback,
    }


def run_single_ic(label: str, spec: dict, verbose: bool = True) -> dict:
    """Run a single attractor-convergence experiment."""
    modes = spec["modes"]
    description = spec["description"]
    run_id = f"attractor_{label}"
    n_modes = len(modes)

    if verbose:
        print(f"\n{'='*65}")
        print(f"  {run_id}")
        print(f"  {description}")
        print(f"  Modes: {n_modes}, A = {A}, T = {T}")
        print(f"{'='*65}")

    # Generate signs
    if spec["signs"] == "random":
        signs = generate_random_signs(n_modes, RANDOM_SEED)
        if verbose:
            n_pos = int(np.sum(signs > 0))
            n_neg = n_modes - n_pos
            print(f"  Random signs: {n_pos} positive, {n_neg} negative (seed={RANDOM_SEED})")
    else:
        signs = None

    # Triad network analysis
    stats = triad_statistics(modes)
    if verbose:
        print(f"  Triad network:")
        print(f"    Active pairs:   {stats['n_triads']}")
        print(f"    Forward max:    mode {stats['forward_max']}")
        print(f"    Inverse min:    mode {stats['inverse_min']}")
        print(f"    Novel targets:  {len(stats['novel_targets'])} modes")

    # Safety check
    total_amp = A * n_modes
    params_check = load_parameter_set(PARAM_SET)
    headroom = min(params_check.rho_star, params_check.rho_max - params_check.rho_star)
    if total_amp > 0.8 * headroom:
        print(f"  WARNING: total perturbation A*N_m = {total_amp:.3f} is "
              f"{total_amp/headroom:.0%} of headroom {headroom:.3f}.")

    # Load parameters
    params = load_parameter_set(PARAM_SET, T=T, method=METHOD, k_out=K_OUT)

    # Build initial condition
    x = make_grid(params)
    rho0, v0 = build_attractor_ic(x, params, modes, A, signs)

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

    # Report at 10 equally spaced intervals
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
            eta = elapsed / (step_n / N_steps) - elapsed
            print(f"    t = {t_val:7.2f}  ({pct:5.1f}%)  "
                  f"[{elapsed:.1f}s elapsed, ~{eta:.0f}s remaining]")

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
    signs_list = signs.tolist() if signs is not None else [1.0] * n_modes
    metadata = {
        "run_id": run_id,
        "experiment": "low_mode_attractor",
        "ic_label": label,
        "description": description,
        "seeded_modes": modes,
        "seeded_range": [modes[0], modes[-1]],
        "n_seeded": n_modes,
        "A_per_mode": A,
        "total_amplitude": A * n_modes,
        "signs": signs_list,
        "random_seed": RANDOM_SEED if spec["signs"] == "random" else None,
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
        "ic_name": "custom_attractor",
        "ic_kwargs": {"modes": modes, "A": A, "signs": signs_list},
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
        margin_final = ts_arrays["margin"][-1]
        print(f"\n  Summary:")
        print(f"    Wall time:             {wall_time:.2f} s")
        print(f"    Steps:                 {N_steps}")
        print(f"    E(0)    = {E_init:.6e},  E(T)    = {E_final:.6e}")
        print(f"    C_ED(0) = {C_init:.6e},  C_ED(T) = {C_final:.6e}")
        print(f"    Final margin:          {margin_final:.6e}")
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
    print("=" * 65)
    print("  Low-Mode Attractor Experiment")
    print(f"  Parameter Set {PARAM_SET}, A = {A}, T = {T}")
    print(f"  Five ICs probing the attractor from different directions")
    print("=" * 65)

    results = {}
    for label in sorted(IC_SPECS.keys()):
        spec = IC_SPECS[label]
        results[label] = run_single_ic(label, spec, verbose=True)

    # --- Cross-IC summary ---
    print("\n" + "=" * 85)
    print("  Attractor Convergence Summary")
    print("=" * 85)
    print(f"  {'IC':<6} {'Description':<42} {'E(T)':<14} {'C_ED(T)':<14} "
          f"{'Wall(s)':<10}")
    print("  " + "-" * 85)

    for label in sorted(results.keys()):
        ts = results[label]["time_series"]
        meta = results[label]["metadata"]

        print(f"  {label:<6} {meta['description'][:40]:<42} "
              f"{ts['E_total'][-1]:<14.6e} "
              f"{ts['C_ED'][-1]:<14.6e} "
              f"{meta['wall_time_s']:<10.1f}")

    # Check attractor universality: all E(T) should be approximately equal
    final_energies = [results[l]["time_series"]["E_total"][-1]
                      for l in sorted(results.keys())]
    E_mean = np.mean(final_energies)
    E_spread = np.max(final_energies) - np.min(final_energies)

    print(f"\n  Attractor universality check:")
    print(f"    Mean E(T):   {E_mean:.6e}")
    print(f"    Spread:      {E_spread:.6e}")
    if E_mean > 0:
        rel_spread = E_spread / E_mean
        print(f"    Rel spread:  {rel_spread:.3e}")
        if rel_spread < 1e-4:
            print(f"    PASS: all ICs converge to the same equilibrium energy.")
        elif rel_spread < 1e-2:
            print(f"    MARGINAL: ICs are converging but may need longer integration time.")
        else:
            print(f"    FAIL: significant spread -- investigate convergence.")
    else:
        print(f"    NOTE: E(T) ~ 0, attractor reached to machine precision.")

    print(f"\nAll runs saved to: output/runs/attractor_IC{{1,2,3,4,5}}")
    print("Done.")


if __name__ == "__main__":
    main()
