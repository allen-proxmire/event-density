"""
modal_hierarchy.py
===================
Experiment: Modal Hierarchy Demonstrations (Atlas §3, Suite §3)

Validates the spectral theory of Appendix C:
  - Single-mode decay at rate D * alpha_k (Theorem C.17)
  - Multi-mode spectral gap behavior (Lemma C.31)
  - Decay-rate funnel: alpha_k increases with k

Runs all five parameter sets with IC-A (single mode) and IC-B (multi-mode).
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from edsim_parameters import load_parameter_set
from edsim_runner import RunConfig, run_simulation
from edsim_diagnostics import extract_decay_rate, modal_amplitudes


def run_single_mode_decay(param_set: str = "I",
                          modes: list = None,
                          A: float = 0.01,
                          T: float = 30.0,
                          verbose: bool = True) -> dict:
    """
    Single-mode initialization: verify exponential decay at rate D * alpha_k.

    For each mode n in `modes`, initializes with IC-A (single cosine)
    and extracts the decay rate from the modal amplitude time series.

    Parameters
    ----------
    param_set : canonical parameter set
    modes : list of mode numbers to test
    A : perturbation amplitude (small for linear regime)
    T : integration time
    verbose : print progress

    Returns
    -------
    dict with arrays: mode, sigma_measured, sigma_predicted, R2, ratio
    """
    if modes is None:
        modes = [1, 2, 3, 4, 5, 8, 12, 16]

    results = {
        "mode": [],
        "sigma_measured": [],
        "sigma_predicted": [],
        "R2": [],
        "ratio": [],
    }

    for n in modes:
        if verbose:
            print(f"\n  Mode n = {n} ...")

        params = load_parameter_set(param_set, T=T, method="crank_nicolson",
                                    k_out=10)
        config = RunConfig(
            params,
            ic_name="A",
            ic_kwargs={"A": A, "n": n},
            run_id=f"modal_single_{param_set}_n{n}",
            N_obs=max(32, 2 * n + 4),
        )
        result = run_simulation(config, verbose=False)
        ts = result["time_series"]

        # Extract decay rate for mode n
        a_n = ts["modal_amplitudes"][:, min(n, ts["modal_amplitudes"].shape[1] - 1)]
        rate = extract_decay_rate(ts["t"], a_n, t_start=0.5)

        # Predicted rate
        sigma_pred = params.modal_decay_rate(n)

        results["mode"].append(n)
        results["sigma_measured"].append(rate["sigma"])
        results["sigma_predicted"].append(sigma_pred)
        results["R2"].append(rate["R2"])

        ratio = rate["sigma"] / sigma_pred if sigma_pred > 0 else np.nan
        results["ratio"].append(ratio)

        if verbose:
            print(f"    sigma_meas = {rate['sigma']:.6f}, "
                  f"sigma_pred = {sigma_pred:.6f}, "
                  f"ratio = {ratio:.4f}, R^2 = {rate['R2']:.6f}")

    # Convert to arrays
    for key in results:
        results[key] = np.array(results[key])

    return results


def run_multi_mode_spectral_gap(param_set: str = "I",
                                 N_m: int = 8,
                                 A: float = 0.02,
                                 T: float = 50.0,
                                 verbose: bool = True) -> dict:
    """
    Multi-mode initialization: demonstrate spectral gap behavior.

    Initializes with IC-B (N_m modes) and tracks the decay of each mode.
    The spectral gap is verified by showing that modes k >= 1 decay faster
    than the homogeneous mode k = 0.

    Parameters
    ----------
    param_set : canonical parameter set
    N_m : number of initial modes
    A : total amplitude
    T : integration time
    verbose : print progress

    Returns
    -------
    dict with modal time series and extracted decay rates
    """
    if verbose:
        print(f"\n  Multi-mode spectral gap: Set {param_set}, N_m = {N_m}")

    params = load_parameter_set(param_set, T=T, method="crank_nicolson",
                                k_out=10)
    config = RunConfig(
        params,
        ic_name="B",
        ic_kwargs={"A": A, "N_m": N_m},
        run_id=f"modal_multi_{param_set}_Nm{N_m}",
        N_obs=2 * N_m + 4,
    )
    result = run_simulation(config, verbose=False)
    ts = result["time_series"]

    # Extract decay rate for each mode
    rates = {}
    for k in range(min(N_m + 4, ts["modal_amplitudes"].shape[1])):
        a_k = ts["modal_amplitudes"][:, k]
        rate = extract_decay_rate(ts["t"], a_k, t_start=1.0)
        rates[k] = {
            "sigma": rate["sigma"],
            "R2": rate["R2"],
            "sigma_predicted": params.modal_decay_rate(k),
        }

    # Spectral gap: D * M* * mu_1
    gap = params.spectral_gap()

    if verbose:
        print(f"\n  Spectral gap (predicted): {gap:.6f}")
        print(f"  {'Mode':<6} {'sigma_meas':<14} {'sigma_pred':<14} {'R^2':<10}")
        print("  " + "-" * 44)
        for k in sorted(rates.keys()):
            r = rates[k]
            print(f"  {k:<6} {r['sigma']:<14.6f} {r['sigma_predicted']:<14.6f} "
                  f"{r['R2']:<10.6f}")

    return {
        "rates": rates,
        "spectral_gap_predicted": gap,
        "time_series": ts,
    }


def run_decay_funnel(param_set: str = "I",
                     K_max: int = 20,
                     verbose: bool = True) -> dict:
    """
    Compute and display the decay-rate funnel: alpha_k vs k.

    This is a purely analytic computation (no simulation needed)
    that visualizes the modal hierarchy.

    Returns dict with arrays: k, mu_k, alpha_k, D_alpha_k
    """
    params = load_parameter_set(param_set)

    k = np.arange(K_max + 1)
    mu_k = np.array([params.mu(ki) for ki in k])
    alpha_k = np.array([params.alpha(ki) for ki in k])
    D_alpha_k = np.array([params.modal_decay_rate(ki) for ki in k])

    if verbose:
        print(f"\n  Decay-Rate Funnel: Set {param_set}")
        print(f"  {'k':<4} {'mu_k':<14} {'alpha_k':<14} {'D*alpha_k':<14}")
        print("  " + "-" * 46)
        for i in range(len(k)):
            print(f"  {k[i]:<4} {mu_k[i]:<14.4f} {alpha_k[i]:<14.4f} "
                  f"{D_alpha_k[i]:<14.4f}")

    return {
        "k": k,
        "mu_k": mu_k,
        "alpha_k": alpha_k,
        "D_alpha_k": D_alpha_k,
    }


# ===================================================================
#  ENTRY POINT
# ===================================================================

if __name__ == "__main__":
    param_set = sys.argv[1] if len(sys.argv) > 1 else "I"

    print("=" * 60)
    print("  ED Modal Hierarchy Experiment")
    print(f"  Parameter Set: {param_set}")
    print("=" * 60)

    # 1. Decay funnel
    funnel = run_decay_funnel(param_set=param_set)

    # 2. Single-mode decay
    single = run_single_mode_decay(param_set=param_set)

    # 3. Multi-mode spectral gap
    multi = run_multi_mode_spectral_gap(param_set=param_set)

    # Summary
    print("\n\n" + "=" * 60)
    print("  SUMMARY")
    print("=" * 60)
    print(f"\n  Single-mode decay rates (Set {param_set}):")
    print(f"  {'Mode':<6} {'Ratio (meas/pred)':<20} {'Pass (|r-1|<5%)'}")
    print("  " + "-" * 40)
    for i, n in enumerate(single["mode"]):
        r = single["ratio"][i]
        passed = "YES" if abs(r - 1.0) < 0.05 else "NO"
        print(f"  {int(n):<6} {r:<20.4f} {passed}")
