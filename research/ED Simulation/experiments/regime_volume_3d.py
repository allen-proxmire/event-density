"""
regime_volume_3d.py
===================
Experiment: Three-Dimensional Regime Volume in the (D, A, N_m) Space
(Atlas §8.5, Suite §4.1)

Sweeps the diffusion coefficient D, perturbation amplitude A, and the number
of seeded modes N_m on a 3D grid while holding all other canonical parameters
fixed at Parameter Set I. Each point uses a broadband initial condition
(modes 1..N_m, equal amplitude A).

The three control parameters span the experimentally accessible design space:

  D:   diffusion timescale -- controls the discriminant Delta and thereby the
       linear regime classification (oscillatory vs overdamped).
  A:   perturbation amplitude -- controls the nonlinear regime experienced
       during transients (triad activation, mobility-collapse proximity).
  N_m: number of seeded modes -- controls the triad-network density
       (N_m*(N_m-1)/2 active triads) and the initial ED-complexity.

The 3D sweep reveals:
  - how the regime boundary (Delta = 1 surface) depends on D alone
  - how the effective (nonlinear) regime depends on A and N_m
  - how the cascade breadth and decay rate scale with all three parameters
  - which regions of parameter space are inadmissible (positivity/capacity)

Grid:
  D_values  = [0.05, 0.1, 0.2, 0.5]            (4 values)
  A_values  = [0.005, 0.01, 0.02, 0.05]         (4 values)
  Nm_values = [5, 10, 20, 30]                    (4 values)
  Total: 64 points

Output directories:
  output/runs/regime_D{D}_A{A}_Nm{Nm}
  e.g., output/runs/regime_D0p05_A0p005_Nm5

Usage:
    python experiments/regime_volume_3d.py

Runtime: approximately 2-4 hours on a single core for the full 64-point
sweep. Each run integrates to T=20 with Crank-Nicolson at N=768,
dt=3.125e-5 (~640,000 time steps per run).

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
T = 20.0
METHOD = "crank_nicolson"
K_OUT = 10
N_OBS = 64

D_VALUES  = [0.05, 0.1, 0.2, 0.5]
A_VALUES  = [0.005, 0.01, 0.02, 0.05]
NM_VALUES = [5, 10, 20, 30]

# Admissibility thresholds
MAX_POS_VIOLATIONS = 50
MAX_CAP_VIOLATIONS = 50

# Oscillation detection threshold
OSCILLATION_SIGN_CHANGES_MIN = 4


# ---------------------------------------------------------------------------
#  Helpers
# ---------------------------------------------------------------------------

def val_to_str(v) -> str:
    """Convert a number to a filesystem-safe string."""
    if isinstance(v, int) or (isinstance(v, float) and v == int(v)):
        return str(int(v))
    s = f"{v:.4g}"
    if "e" in s:
        s = f"{v:.6f}".rstrip("0").rstrip(".")
    return s.replace(".", "p")


def folder_name(D: float, A: float, Nm: int) -> str:
    return f"regime_D{val_to_str(D)}_A{val_to_str(A)}_Nm{Nm}"


def build_broadband_ic(x: np.ndarray, params, modes: list, A_per_mode: float):
    """Construct initial density by summing Neumann eigenmodes."""
    rho0 = np.full_like(x, params.rho_star)
    for n in modes:
        rho0 += A_per_mode * np.cos(n * np.pi * x / params.L)
    rho0 = np.clip(rho0, 1e-12, params.rho_max - 1e-12)
    v0 = 0.0
    return rho0, v0


def compute_discriminant(D: float, zeta: float, tau: float, P_prime: float) -> float:
    """Compute the damping discriminant Delta (Appendix C.3)."""
    numer = (D * P_prime + zeta / tau) ** 2
    denom = 4.0 * D * P_prime * zeta / tau
    if denom < 1e-30:
        return float("inf")
    return numer / denom


def classify_linear_regime(Delta: float) -> str:
    if abs(Delta - 1.0) < 0.01:
        return "critical"
    elif Delta < 1.0:
        return "underdamped"
    else:
        return "overdamped"


def detect_oscillation(modal_a0: np.ndarray) -> int:
    """Count sign changes in the homogeneous perturbation a_0(t) - a_0(T)."""
    deviation = modal_a0 - modal_a0[-1]
    signs = np.sign(deviation)
    signs_nz = signs[signs != 0]
    if len(signs_nz) < 2:
        return 0
    return int(np.sum(np.abs(np.diff(signs_nz)) > 0))


def triad_statistics(modes: list) -> dict:
    """Compute triad network summary."""
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
    fwd_max = max((m + n for i, m in enumerate(modes)
                   for j, n in enumerate(modes) if j > i), default=0)
    inv_min = min((abs(m - n) for i, m in enumerate(modes)
                   for j, n in enumerate(modes) if j > i), default=0)
    return {
        "n_triads": n_triads,
        "forward_max": fwd_max,
        "inverse_min": inv_min,
        "n_novel_targets": len(novel),
    }


def _json_default(obj):
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
#  Single-point runner
# ---------------------------------------------------------------------------

def run_single_point(D_val: float, A_val: float, Nm: int,
                     verbose: bool = True) -> dict:
    """Run one (D, A, N_m) grid point."""
    modes = list(range(1, Nm + 1))
    run_id = folder_name(D_val, A_val, Nm)

    if verbose:
        print(f"  {run_id}  (D={D_val}, A={A_val}, Nm={Nm})", end="", flush=True)

    # Load parameters with D override
    params = load_parameter_set(
        PARAM_SET, T=T, method=METHOD, k_out=K_OUT, D=D_val,
    )

    # Discriminant
    P_star_prime = params.P0
    Delta = compute_discriminant(D_val, params.zeta, params.tau, P_star_prime)
    linear_regime = classify_linear_regime(Delta)

    # Amplitude safety check
    total_amp = A_val * Nm
    headroom = min(params.rho_star, params.rho_max - params.rho_star)
    amplitude_safe = total_amp < 0.95 * headroom

    # Triad statistics
    stats = triad_statistics(modes)

    # Build IC
    x = make_grid(params)
    rho0, v0 = build_broadband_ic(x, params, modes, A_val)

    # Output directory
    out_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "output", "runs", run_id,
    )
    ensure_dirs()
    os.makedirs(out_dir, exist_ok=True)

    # --- Integration ---
    t_val = 0.0
    rho = rho0.copy()
    v = v0
    N_steps = int(np.ceil(params.T / params.dt))

    ts = TimeSeries(N_obs=N_OBS)
    snap0 = diagnostic_snapshot(rho, v, t_val, params, N_OBS)
    ts.append(snap0)

    wall_start = _time.perf_counter()
    n_pos = 0
    n_cap = 0
    nan_detected = False

    for step_n in range(1, N_steps + 1):
        t_val = step_n * params.dt
        res = step(rho, v, params)
        rho = res["rho"]
        v = res["v"]

        if not np.all(np.isfinite(rho)) or not np.isfinite(v):
            nan_detected = True
            break

        rho, pos_flag, cap_flag = enforce_bounds(rho, params)
        if pos_flag:
            n_pos += 1
        if cap_flag:
            n_cap += 1

        if step_n % params.k_out == 0 or step_n == N_steps:
            snap = diagnostic_snapshot(rho, v, t_val, params, N_OBS)
            ts.append(snap)

    wall_time = _time.perf_counter() - wall_start
    ts_arrays = ts.to_arrays()

    # --- Regime classification ---
    inadmissible = (
        nan_detected
        or n_pos > MAX_POS_VIOLATIONS
        or n_cap > MAX_CAP_VIOLATIONS
    )

    n_sign_changes = 0
    observed_oscillation = False
    modal = ts_arrays.get("modal_amplitudes")
    if modal is not None and modal.ndim == 2 and modal.shape[1] > 0:
        a0 = modal[:, 0]
        n_sign_changes = detect_oscillation(a0)
        observed_oscillation = n_sign_changes >= OSCILLATION_SIGN_CHANGES_MIN

    if inadmissible:
        effective_regime = "inadmissible"
    elif observed_oscillation:
        effective_regime = "oscillatory"
    elif linear_regime == "underdamped" and not observed_oscillation:
        effective_regime = "underdamped_weak"
    elif linear_regime == "overdamped" and observed_oscillation:
        effective_regime = "transient_oscillatory"
    else:
        effective_regime = linear_regime

    termination = "NaN_detected" if nan_detected else "FinalTime"

    if verbose:
        E_final = ts_arrays["E_total"][-1] if len(ts_arrays["E_total"]) > 0 else 0
        print(f"  => {effective_regime:<16} Delta={Delta:.3f}  "
              f"E(T)={E_final:.2e}  [{wall_time:.1f}s]")

    # --- Save ---
    np.savez_compressed(os.path.join(out_dir, "time_series.npz"), **ts_arrays)
    np.savez_compressed(
        os.path.join(out_dir, "final_state.npz"),
        rho=rho, v=np.array([v]), t=np.array([t_val]),
    )

    metadata = {
        "run_id": run_id,
        "experiment": "regime_volume_3d",
        "D": D_val,
        "A_per_mode": A_val,
        "Nm": Nm,
        "seeded_modes": modes,
        "seeded_range": [1, Nm],
        "n_seeded": Nm,
        "total_amplitude": total_amp,
        "amplitude_safe": amplitude_safe,
        "param_set": PARAM_SET,
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
        "n_steps": int(np.ceil(params.T / params.dt)),
        "final_t": t_val,
        "wall_time_s": wall_time,
        "n_positivity_violations": n_pos,
        "n_capacity_violations": n_cap,
        "nan_detected": nan_detected,
        "termination_reason": termination,
        "discriminant_Delta": Delta,
        "linear_regime": linear_regime,
        "n_sign_changes": n_sign_changes,
        "observed_oscillation": observed_oscillation,
        "effective_regime": effective_regime,
        "inadmissible": inadmissible,
        "triad_statistics": stats,
        "timestamp": _time.strftime("%Y-%m-%dT%H:%M:%SZ", _time.gmtime()),
    }

    with open(os.path.join(out_dir, "metadata.json"), "w") as f:
        json.dump(metadata, f, indent=2, default=_json_default)

    return metadata


# ---------------------------------------------------------------------------
#  Main
# ---------------------------------------------------------------------------

def main():
    total = len(D_VALUES) * len(A_VALUES) * len(NM_VALUES)
    print("=" * 70)
    print("  3D Regime Volume: (D, A, N_m) Space")
    print(f"  Baseline: Parameter Set {PARAM_SET}")
    print(f"  D  grid: {D_VALUES}  ({len(D_VALUES)} values)")
    print(f"  A  grid: {A_VALUES}  ({len(A_VALUES)} values)")
    print(f"  Nm grid: {NM_VALUES}  ({len(NM_VALUES)} values)")
    print(f"  Total points: {total}")
    print(f"  T = {T},  method = {METHOD}")
    print("=" * 70)

    ensure_dirs()
    results = {}
    count = 0
    wall_total_start = _time.perf_counter()

    for D_val in D_VALUES:
        for A_val in A_VALUES:
            for Nm in NM_VALUES:
                count += 1
                # Check amplitude safety before running
                headroom_est = 0.5  # conservative; actual check in runner
                if A_val * Nm > 0.95 * headroom_est:
                    print(f"\n  [{count}/{total}] SKIP {folder_name(D_val, A_val, Nm)}: "
                          f"A*Nm = {A_val * Nm:.3f} > 0.95 * headroom")
                    results[(D_val, A_val, Nm)] = {
                        "run_id": folder_name(D_val, A_val, Nm),
                        "effective_regime": "inadmissible",
                        "inadmissible": True,
                        "reason": "amplitude_exceeds_headroom",
                        "D": D_val, "A_per_mode": A_val, "Nm": Nm,
                    }
                    continue

                print(f"\n  [{count}/{total}]", end=" ")
                meta = run_single_point(D_val, A_val, Nm, verbose=True)
                results[(D_val, A_val, Nm)] = meta

    wall_total = _time.perf_counter() - wall_total_start

    # --- Summary: 2D slices ---
    print("\n" + "=" * 80)
    print("  3D Regime Volume -- Summary")
    print("=" * 80)

    # Print one 2D slice per Nm value
    abbrev = {
        "underdamped": "UD", "underdamped_weak": "UDw",
        "oscillatory": "OSC", "critical": "CR",
        "overdamped": "OD", "transient_oscillatory": "tOSC",
        "inadmissible": "INAD", "unknown": "?",
    }

    for Nm in NM_VALUES:
        print(f"\n  --- Nm = {Nm} (modes 1-{Nm}, "
              f"{Nm*(Nm-1)//2} triads) ---")
        header = f"  {'D \\ A':<10}"
        for A_val in A_VALUES:
            header += f" {A_val:<8}"
        print(header)
        print("  " + "-" * (10 + 9 * len(A_VALUES)))

        for D_val in D_VALUES:
            row = f"  {D_val:<10.3f}"
            for A_val in A_VALUES:
                meta = results.get((D_val, A_val, Nm), {})
                regime = meta.get("effective_regime", "?")
                short = abbrev.get(regime, regime[:4])
                row += f" {short:<8}"
            print(row)

    # --- Global statistics ---
    print(f"\n  Global Statistics:")
    print(f"    Total grid points:  {total}")

    regime_counts = {}
    n_inad = 0
    n_nan = 0
    n_skipped = 0
    for m in results.values():
        r = m.get("effective_regime", "unknown")
        regime_counts[r] = regime_counts.get(r, 0) + 1
        if m.get("inadmissible", False):
            n_inad += 1
        if m.get("nan_detected", False):
            n_nan += 1
        if m.get("reason") == "amplitude_exceeds_headroom":
            n_skipped += 1

    print(f"    Computed:           {total - n_skipped}")
    print(f"    Pre-skipped:        {n_skipped} (amplitude > headroom)")
    print(f"    Admissible:         {total - n_inad}")
    print(f"    Inadmissible:       {n_inad}")
    print(f"    NaN detected:       {n_nan}")

    print(f"\n  Regime distribution:")
    for r in ["underdamped", "underdamped_weak", "oscillatory",
              "critical", "overdamped", "transient_oscillatory",
              "inadmissible"]:
        if r in regime_counts:
            print(f"    {r:<24}: {regime_counts[r]}")

    # Discriminant (depends only on D)
    print(f"\n  Discriminant Delta (independent of A, Nm):")
    for D_val in D_VALUES:
        meta = None
        for A_val in A_VALUES:
            for Nm in NM_VALUES:
                m = results.get((D_val, A_val, Nm), {})
                if "discriminant_Delta" in m:
                    meta = m
                    break
            if meta:
                break
        if meta:
            Delta = meta["discriminant_Delta"]
            lin = meta.get("linear_regime", "?")
            print(f"    D={D_val:<6.3f}  Delta={Delta:<8.4f}  linear={lin}")

    print(f"\n  Total wall time: {wall_total:.1f} s ({wall_total / 60:.1f} min)")
    print(f"  Runs saved to: output/runs/regime_D*_A*_Nm*")
    print("Done.")


if __name__ == "__main__":
    main()
