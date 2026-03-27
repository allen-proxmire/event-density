"""
triad_coupling.py
==================
Experiment: Nonlinear Triad Simulations (Atlas §4, Suite §8.3)

Validates Theorem C.34 (triad selection rule) and Proposition C.35
(locked amplitude ratio):
  - Initialize with modes m and n
  - Verify generation of modes m+n and |m-n| (and no others)
  - Measure the amplitude ratio k3/k1 and compare to theory
  - Track the harmonic cascade over time

Runs with Parameter Set I (deep oscillatory) at moderate amplitude
to ensure the nonlinear term is active.
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from edsim_parameters import load_parameter_set
from edsim_runner import RunConfig, run_simulation
from edsim_diagnostics import (
    triad_coefficient, triad_compliance_matrix,
    extract_decay_rate, modal_amplitudes,
)


def run_triad_activation(param_set: str = "I",
                         source_pairs: list = None,
                         A: float = 0.05,
                         T: float = 20.0,
                         verbose: bool = True) -> dict:
    """
    Triad activation: initialize with two modes, verify selection rule.

    For each pair (m, n), initializes with:
        rho(x,0) = rho* + A/sqrt(2) * [cos(m*pi*x/L) + cos(n*pi*x/L)]

    and checks which modes are activated by the nonlinear term M'(rho)|grad rho|^2.

    Parameters
    ----------
    param_set : canonical parameter set
    source_pairs : list of (m, n) tuples
    A : perturbation amplitude
    T : integration time
    verbose : print progress

    Returns
    -------
    dict with compliance results for each pair
    """
    if source_pairs is None:
        source_pairs = [
            (1, 2), (1, 3), (2, 3), (1, 4), (2, 4),
            (3, 4), (1, 5), (2, 5),
        ]

    N_obs = 32  # Track enough modes
    results = {}

    for m, n in source_pairs:
        if verbose:
            print(f"\n  Pair ({m}, {n}) ...")

        params = load_parameter_set(param_set, T=T, method="crank_nicolson",
                                    k_out=10)

        # Custom two-mode initial condition
        def two_mode_ic(x, p):
            A_each = A / np.sqrt(2.0)
            return p.rho_star + A_each * (np.cos(m * np.pi * x / p.L)
                                           + np.cos(n * np.pi * x / p.L))

        from edsim_initial_conditions import ic_custom
        from edsim_core import make_grid

        x = make_grid(params)
        rho0, v0 = ic_custom(x, params, two_mode_ic)

        config = RunConfig(
            params,
            ic_name="A",  # placeholder; we override
            ic_kwargs={"A": A, "n": 1},
            run_id=f"triad_{param_set}_m{m}_n{n}",
            N_obs=N_obs,
        )

        # Override IC in runner — we run manually
        from edsim_runner import (
            TimeSeries, ensure_dirs, diagnostic_snapshot,
            enforce_bounds,
        )
        from edsim_core import step
        import time as _time

        ensure_dirs()
        t_val = 0.0
        rho = rho0.copy()
        v = v0
        N_steps = int(np.ceil(params.T / params.dt))

        ts = TimeSeries(N_obs=N_obs)
        snap0 = diagnostic_snapshot(rho, v, t_val, params, N_obs)
        ts.append(snap0)

        for step_n in range(1, N_steps + 1):
            t_val = step_n * params.dt
            res = step(rho, v, params)
            rho = res["rho"]
            v = res["v"]
            rho, _, _ = enforce_bounds(rho, params)

            if step_n % params.k_out == 0 or step_n == N_steps:
                snap = diagnostic_snapshot(rho, v, t_val, params, N_obs)
                ts.append(snap)

        ts_arrays = ts.to_arrays()

        # Analyze which modes were activated
        # A mode k is "activated" if max|a_k(t)| > threshold * A^2
        threshold = 1e-4  # relative to A^2
        a_max = np.max(np.abs(ts_arrays["modal_amplitudes"]), axis=0)

        activated = set()
        for k in range(N_obs):
            # Skip the source modes
            if k == m or k == n:
                continue
            if a_max[k] > threshold * A ** 2:
                activated.add(k)

        # Predicted targets
        predicted = set()
        if m == n:
            predicted.add(2 * m)
            predicted.add(0)
        else:
            predicted.add(m + n)
            predicted.add(abs(m - n))

        # Compliance check
        false_positives = activated - predicted
        false_negatives = predicted - activated

        results[(m, n)] = {
            "activated": activated,
            "predicted": predicted,
            "false_positives": false_positives,
            "false_negatives": false_negatives,
            "compliant": len(false_positives) == 0 and len(false_negatives) == 0,
            "a_max": a_max,
            "time_series": ts_arrays,
        }

        if verbose:
            status = "PASS" if results[(m, n)]["compliant"] else "FAIL"
            print(f"    Predicted: {sorted(predicted)}")
            print(f"    Activated: {sorted(activated)}")
            print(f"    Status: {status}")
            if false_positives:
                print(f"    False positives: {sorted(false_positives)}")
            if false_negatives:
                print(f"    False negatives: {sorted(false_negatives)}")

    return results


def run_locked_ratio(param_set: str = "I",
                     m: int = 1, n: int = 2,
                     A_values: np.ndarray = None,
                     T: float = 30.0,
                     verbose: bool = True) -> dict:
    """
    Locked amplitude ratio: measure k3/k1 for the triad (m, n, m+n).

    Initializes with mode m only, and measures the quasi-steady ratio
    of a_{m+n} / a_m after the triad locks.

    Parameters
    ----------
    param_set : canonical parameter set
    m, n : source mode pair
    A_values : array of initial amplitudes
    T : integration time
    verbose : print progress

    Returns
    -------
    dict with amplitude ratios vs A
    """
    if A_values is None:
        A_values = np.array([0.01, 0.02, 0.05, 0.1, 0.15, 0.2])

    k_target = m + n
    L = 1.0  # default domain

    # Predicted ratio from triad coefficient
    Gamma = triad_coefficient(m, n, k_target, L)

    ratios = []

    for A in A_values:
        if verbose:
            print(f"\n  A = {A:.3f} ...")

        params = load_parameter_set(param_set, T=T, method="crank_nicolson",
                                    k_out=10)

        # Single-mode IC (mode m)
        config = RunConfig(
            params,
            ic_name="A",
            ic_kwargs={"A": A, "n": m},
            run_id=f"locked_{param_set}_m{m}_n{n}_A{A:.4f}",
            N_obs=2 * k_target + 4,
        )
        result = run_simulation(config, verbose=False)
        ts = result["time_series"]

        # Measure quasi-steady ratio in the second half of the run
        N_half = len(ts["t"]) // 2
        a_m_late = ts["modal_amplitudes"][N_half:, m]
        a_target_late = ts["modal_amplitudes"][N_half:, k_target]

        # Average absolute ratio
        with np.errstate(divide='ignore', invalid='ignore'):
            ratio_vals = np.abs(a_target_late) / np.maximum(np.abs(a_m_late), 1e-30)
        mean_ratio = np.nanmean(ratio_vals)
        std_ratio = np.nanstd(ratio_vals)

        ratios.append({
            "A": A,
            "mean_ratio": mean_ratio,
            "std_ratio": std_ratio,
        })

        if verbose:
            print(f"    ratio = {mean_ratio:.6f} +/- {std_ratio:.6f}")

    return {
        "m": m,
        "n": n,
        "k_target": k_target,
        "Gamma": Gamma,
        "ratios": ratios,
    }


def run_cascade_depth(param_set: str = "I",
                      A: float = 0.1,
                      T: float = 40.0,
                      verbose: bool = True) -> dict:
    """
    Harmonic cascade: track spectral evolution from IC-B.

    Initializes with modes 1–4 and tracks how the nonlinear term
    cascades energy to higher modes through successive triad interactions.

    Returns dict with spectral snapshots at selected times.
    """
    if verbose:
        print(f"\n  Harmonic cascade: Set {param_set}, A = {A}")

    params = load_parameter_set(param_set, T=T, method="crank_nicolson",
                                k_out=5)
    config = RunConfig(
        params,
        ic_name="B",
        ic_kwargs={"A": A, "N_m": 4},
        run_id=f"cascade_{param_set}_A{A:.3f}",
        N_obs=32,
    )
    result = run_simulation(config, verbose=False)
    ts = result["time_series"]

    # Select snapshot times
    t_snaps = [0.0, 0.5, 1.0, 2.0, 5.0, 10.0, T]
    snapshots = {}

    for t_target in t_snaps:
        idx = np.argmin(np.abs(ts["t"] - t_target))
        t_actual = ts["t"][idx]
        spectrum = ts["modal_amplitudes"][idx, :]
        snapshots[t_actual] = spectrum

        if verbose:
            n_active = np.sum(np.abs(spectrum) > 1e-8)
            print(f"    t = {t_actual:.2f}: {n_active} active modes, "
                  f"max|a| = {np.max(np.abs(spectrum)):.4e}")

    # Measure cascade depth: highest mode with |a_k| > threshold
    final_spectrum = ts["modal_amplitudes"][-1, :]
    cascade_depth = 0
    for k in range(len(final_spectrum) - 1, -1, -1):
        if abs(final_spectrum[k]) > 1e-10:
            cascade_depth = k
            break

    if verbose:
        print(f"\n  Final cascade depth: mode {cascade_depth}")

    return {
        "snapshots": snapshots,
        "cascade_depth": cascade_depth,
        "time_series": ts,
    }


# ===================================================================
#  ENTRY POINT
# ===================================================================

if __name__ == "__main__":
    param_set = sys.argv[1] if len(sys.argv) > 1 else "I"

    print("=" * 60)
    print("  ED Triad Coupling Experiment")
    print(f"  Parameter Set: {param_set}")
    print("=" * 60)

    # 1. Selection rule compliance
    print("\n--- Selection Rule Compliance ---")
    activation = run_triad_activation(param_set=param_set)

    n_pass = sum(1 for r in activation.values() if r["compliant"])
    n_total = len(activation)
    print(f"\n  Compliance: {n_pass}/{n_total} pairs passed")

    # 2. Locked amplitude ratio
    print("\n--- Locked Amplitude Ratio ---")
    locked = run_locked_ratio(param_set=param_set)

    # 3. Harmonic cascade
    print("\n--- Harmonic Cascade ---")
    cascade = run_cascade_depth(param_set=param_set)

    print(f"\n  Cascade depth: mode {cascade['cascade_depth']}")
