"""
regime_map_2d.py
================
Experiment: Two-Dimensional Regime Map in the (D, A) Plane (Atlas §8.5,
Suite §4.1)

Sweeps the diffusion coefficient D and the perturbation amplitude A on a
2D grid while holding all other canonical parameters fixed at Parameter Set I.
Each point uses a broadband initial condition (modes 1-20, equal amplitude A),
identical in structure to broadband_cascade IC2.

The purpose is to map the regime geometry -- oscillatory, critical, overdamped,
and inadmissible -- as a function of the two most experimentally accessible
control parameters:

  D: controls the diffusion timescale and, through the discriminant Delta,
     the regime classification (Appendix C.3).
  A: controls the initial perturbation amplitude and, through the nonlinear
     coupling, the effective regime experienced during transients.

The discriminant Delta is computed from the linearised eigenvalues at
equilibrium and depends only on D (not A); however, the *effective* regime
during the transient depends on both D and A because large amplitudes
activate the nonlinear terms and can produce transient oscillations even
in the overdamped regime (Atlas §8.3, Figure 8.3).

Grid:
  D_values = [0.05, 0.1, 0.15, 0.2, 0.3, 0.5, 0.8]
  A_values = [0.005, 0.01, 0.02, 0.05, 0.10]
  Total: 35 points

Regime classification (per run):
  - Linear: Delta < 1 => underdamped (oscillatory)
            Delta = 1 => critical
            Delta > 1 => overdamped
  - Nonlinear: detected from the time series (sign changes in a_0(t))
  - Admissibility: if positivity or capacity violations exceed a threshold,
    the point is flagged as inadmissible.

Output directories:
  output/runs/regime_D{D}_A{A}
  e.g., output/runs/regime_D0p05_A0p005

Usage:
    python experiments/regime_map_2d.py

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

SEEDED_MODES = list(range(1, 21))   # modes 1-20

D_VALUES = [0.05, 0.1, 0.15, 0.2, 0.3, 0.5, 0.8]
A_VALUES = [0.005, 0.01, 0.02, 0.05, 0.10]

# Admissibility thresholds
MAX_POS_VIOLATIONS = 50     # More than this => inadmissible
MAX_CAP_VIOLATIONS = 50

# Oscillation detection: count sign changes in the homogeneous perturbation
OSCILLATION_SIGN_CHANGES_MIN = 4   # At least this many => "observed oscillation"


# ---------------------------------------------------------------------------
#  Helpers
# ---------------------------------------------------------------------------

def val_to_str(v: float) -> str:
    """Convert a float to a filesystem-safe string: 0.05 -> '0p05'."""
    # Format with enough decimals to distinguish all grid values,
    # stripping trailing zeros but keeping at least one decimal.
    s = f"{v:.4g}"
    # Remove scientific notation for small numbers
    if "e" in s:
        s = f"{v:.6f}".rstrip("0").rstrip(".")
    return s.replace(".", "p")


def folder_name(D: float, A: float) -> str:
    return f"regime_D{val_to_str(D)}_A{val_to_str(A)}"


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
    """Classify the regime from the linearised discriminant."""
    if abs(Delta - 1.0) < 0.01:
        return "critical"
    elif Delta < 1.0:
        return "underdamped"
    else:
        return "overdamped"


def detect_oscillation(modal_a0: np.ndarray) -> int:
    """Count sign changes in the homogeneous perturbation a_0(t) - a_0(T).

    Returns the number of zero-crossings, which distinguishes oscillatory
    transients from monotonic ones.
    """
    # Deviation from the final value
    deviation = modal_a0 - modal_a0[-1]
    # Count sign changes
    signs = np.sign(deviation)
    # Remove exact zeros (keep nonzero entries)
    signs_nz = signs[signs != 0]
    if len(signs_nz) < 2:
        return 0
    changes = np.sum(np.abs(np.diff(signs_nz)) > 0)
    return int(changes)


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
    return {
        "n_triads": n_triads,
        "forward_max": max(m + n for i, m in enumerate(modes)
                          for j, n in enumerate(modes) if j > i),
        "inverse_min": min(abs(m - n) for i, m in enumerate(modes)
                          for j, n in enumerate(modes) if j > i),
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

def run_single_point(D_val: float, A_val: float, verbose: bool = True) -> dict:
    """Run one (D, A) grid point."""
    run_id = folder_name(D_val, A_val)
    n_modes = len(SEEDED_MODES)

    if verbose:
        print(f"\n  {run_id}  (D={D_val}, A={A_val})")

    # Load parameters with D override
    params = load_parameter_set(
        PARAM_SET,
        T=T,
        method=METHOD,
        k_out=K_OUT,
        D=D_val,
    )

    # Discriminant
    P_star_prime = params.P0
    Delta = compute_discriminant(D_val, params.zeta, params.tau, P_star_prime)
    linear_regime = classify_linear_regime(Delta)

    # Check amplitude safety
    total_amp = A_val * n_modes
    headroom = min(params.rho_star, params.rho_max - params.rho_star)
    amplitude_safe = total_amp < 0.95 * headroom

    if verbose:
        print(f"    Delta={Delta:.4f}  linear_regime={linear_regime}  "
              f"total_amp={total_amp:.4f}  safe={amplitude_safe}")

    # Build IC
    x = make_grid(params)
    rho0, v0 = build_broadband_ic(x, params, SEEDED_MODES, A_val)

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

        # NaN/Inf check
        if not np.all(np.isfinite(rho)) or not np.isfinite(v):
            nan_detected = True
            if verbose:
                print(f"    NaN/Inf at step {step_n}, t={t_val:.4f}. Aborting.")
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

    # --- Post-processing: regime classification ---
    # Admissibility
    inadmissible = (
        nan_detected
        or n_pos > MAX_POS_VIOLATIONS
        or n_cap > MAX_CAP_VIOLATIONS
    )

    # Oscillation detection from the homogeneous mode
    n_sign_changes = 0
    observed_oscillation = False
    modal = ts_arrays.get("modal_amplitudes")
    if modal is not None and modal.ndim == 2 and modal.shape[1] > 0:
        a0 = modal[:, 0]
        n_sign_changes = detect_oscillation(a0)
        observed_oscillation = n_sign_changes >= OSCILLATION_SIGN_CHANGES_MIN

    # Effective regime (combining linear + nonlinear information)
    if inadmissible:
        effective_regime = "inadmissible"
    elif observed_oscillation:
        effective_regime = "oscillatory"
    elif linear_regime == "underdamped" and not observed_oscillation:
        # Linear says underdamped but no oscillation observed --
        # possible if amplitude is so small the oscillation is below noise
        effective_regime = "underdamped_weak"
    elif linear_regime == "overdamped" and observed_oscillation:
        # Nonlinear transient oscillation in the overdamped regime
        effective_regime = "transient_oscillatory"
    else:
        effective_regime = linear_regime

    termination = "NaN_detected" if nan_detected else "FinalTime"

    if verbose:
        print(f"    regime: {effective_regime}  "
              f"sign_changes={n_sign_changes}  "
              f"pos_viol={n_pos}  cap_viol={n_cap}  "
              f"wall={wall_time:.1f}s")

    # --- Save ---
    np.savez_compressed(os.path.join(out_dir, "time_series.npz"), **ts_arrays)
    np.savez_compressed(
        os.path.join(out_dir, "final_state.npz"),
        rho=rho, v=np.array([v]), t=np.array([t_val]),
    )

    metadata = {
        "run_id": run_id,
        "experiment": "regime_map_2d",
        "D": D_val,
        "A_per_mode": A_val,
        "total_amplitude": total_amp,
        "amplitude_safe": amplitude_safe,
        "seeded_modes": SEEDED_MODES,
        "seeded_range": [SEEDED_MODES[0], SEEDED_MODES[-1]],
        "n_seeded": n_modes,
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
        "triad_statistics": triad_statistics(SEEDED_MODES),
        "timestamp": _time.strftime("%Y-%m-%dT%H:%M:%SZ", _time.gmtime()),
    }

    with open(os.path.join(out_dir, "metadata.json"), "w") as f:
        json.dump(metadata, f, indent=2, default=_json_default)

    return metadata


# ---------------------------------------------------------------------------
#  Main
# ---------------------------------------------------------------------------

def main():
    total = len(D_VALUES) * len(A_VALUES)
    print("=" * 65)
    print("  2D Regime Map: (D, A) Plane")
    print(f"  Baseline: Parameter Set {PARAM_SET}")
    print(f"  D grid: {D_VALUES}")
    print(f"  A grid: {A_VALUES}")
    print(f"  Total points: {total}")
    print(f"  IC: modes {SEEDED_MODES[0]}-{SEEDED_MODES[-1]}")
    print(f"  T = {T},  method = {METHOD}")
    print("=" * 65)

    ensure_dirs()
    results = {}
    count = 0
    wall_total_start = _time.perf_counter()

    for D_val in D_VALUES:
        for A_val in A_VALUES:
            count += 1
            print(f"\n--- Point {count}/{total} ---")
            meta = run_single_point(D_val, A_val, verbose=True)
            results[(D_val, A_val)] = meta

    wall_total = _time.perf_counter() - wall_total_start

    # --- Summary table ---
    print("\n" + "=" * 105)
    print("  2D Regime Map Summary")
    print("=" * 105)

    # Header
    header = f"  {'D':<8}"
    for A_val in A_VALUES:
        header += f"  A={A_val:<7}"
    print(header)
    print("  " + "-" * (8 + 9 * len(A_VALUES)))

    # Rows
    for D_val in D_VALUES:
        row = f"  {D_val:<8.3f}"
        for A_val in A_VALUES:
            meta = results.get((D_val, A_val), {})
            regime = meta.get("effective_regime", "?")

            # Abbreviate for table
            abbrev = {
                "underdamped": "UD",
                "overdamped": "OD",
                "critical": "CR",
                "oscillatory": "OSC",
                "underdamped_weak": "UDw",
                "transient_oscillatory": "tOSC",
                "inadmissible": "INAD",
            }
            short = abbrev.get(regime, regime[:4])
            row += f"  {short:<9}"
        print(row)

    # Delta column (same for all A at a given D)
    print(f"\n  Discriminant Delta (independent of A):")
    for D_val in D_VALUES:
        meta = results.get((D_val, A_VALUES[0]), {})
        Delta = meta.get("discriminant_Delta", 0)
        lin = meta.get("linear_regime", "?")
        print(f"    D={D_val:<6.3f}  Delta={Delta:<8.4f}  linear={lin}")

    # Admissibility summary
    n_inad = sum(1 for m in results.values() if m.get("inadmissible", False))
    n_nan = sum(1 for m in results.values() if m.get("nan_detected", False))
    print(f"\n  Admissibility:")
    print(f"    Total points:     {total}")
    print(f"    Admissible:       {total - n_inad}")
    print(f"    Inadmissible:     {n_inad}")
    print(f"    NaN detected:     {n_nan}")

    # Regime counts
    regime_counts = {}
    for m in results.values():
        r = m.get("effective_regime", "unknown")
        regime_counts[r] = regime_counts.get(r, 0) + 1
    print(f"\n  Regime distribution:")
    for r, c in sorted(regime_counts.items()):
        print(f"    {r:<24}: {c}")

    print(f"\n  Total wall time: {wall_total:.1f} s ({wall_total/60:.1f} min)")

    folders = [folder_name(D, A) for D in D_VALUES for A in A_VALUES]
    print(f"\n  Runs saved to: output/runs/regime_D*_A*")
    print(f"  ({len(folders)} directories)")
    print("Done.")


if __name__ == "__main__":
    main()
