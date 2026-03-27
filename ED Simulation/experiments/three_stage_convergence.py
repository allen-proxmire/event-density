"""
three_stage_convergence.py
===========================
Experiment: Three-Stage Convergence (Atlas §7, Suite §8.5)

Validates Theorem C.76: every solution of the canonical ED system
converges to (rho*, 0) through three stages:
    Stage I:   Global bounds (energy bounded and decreasing)
    Stage II:  Algebraic decay (polynomial decrease of E(t))
    Stage III: Exponential decay (E(t) ~ C * exp(-2*sigma*t))

The transition time t* from Stage II to Stage III depends on
the initial ED-complexity C_ED(0).

Runs all five parameter sets with IC-C (Gaussian, high complexity)
at three complexity levels (low, medium, high).
"""

import os
import sys
import numpy as np

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from edsim_parameters import load_parameter_set
from edsim_runner import RunConfig, run_simulation
from edsim_diagnostics import detect_three_stages, extract_decay_rate


def run_three_stage_experiment(param_set: str = "I",
                               complexity_levels: dict = None,
                               T: float = 100.0,
                               verbose: bool = True) -> dict:
    """
    Run the three-stage convergence experiment.

    Parameters
    ----------
    param_set : canonical parameter set ('I'-'V')
    complexity_levels : dict mapping label -> IC amplitude A
    T : integration time (long enough for Stage III)
    verbose : print progress

    Returns
    -------
    dict with results for each complexity level
    """
    if complexity_levels is None:
        complexity_levels = {
            "low": 0.01,
            "medium": 0.1,
            "high": 0.3,
        }

    results = {}

    for label, A in complexity_levels.items():
        if verbose:
            print(f"\n{'=' * 60}")
            print(f"  Three-Stage Convergence: Set {param_set}, {label} complexity (A={A})")
            print(f"{'=' * 60}")

        params = load_parameter_set(param_set, T=T, method="crank_nicolson")
        config = RunConfig(
            params,
            ic_name="C",
            ic_kwargs={"A": A, "sigma": 0.05},
            run_id=f"three_stage_{param_set}_{label}",
        )
        result = run_simulation(config, verbose=verbose)

        # Detect three stages
        ts = result["time_series"]
        stages = detect_three_stages(ts["t"], ts["E_total"], params)

        # Extract Stage III decay rate
        if stages["has_three_stages"]:
            t_star = stages["t_star"]
            mask = ts["t"] >= t_star
            t_III = ts["t"][mask]
            E_III = ts["E_total"][mask]
            if len(t_III) > 5:
                log_E = np.log(np.maximum(np.abs(E_III), 1e-30))
                A_mat = np.column_stack([t_III, np.ones_like(t_III)])
                coeffs = np.linalg.lstsq(A_mat, log_E, rcond=None)[0]
                sigma_measured = -coeffs[0] / 2.0
            else:
                sigma_measured = np.nan
        else:
            sigma_measured = np.nan

        # Analytic prediction: sigma = D * alpha_0 = D * P*'
        sigma_predicted = params.D * params.P_star_prime

        results[label] = {
            "A": A,
            "C_ED_initial": ts["C_ED"][0],
            "has_three_stages": stages["has_three_stages"],
            "t_star": stages["t_star"],
            "sigma_measured": sigma_measured,
            "sigma_predicted": sigma_predicted,
            "E_final": ts["E_total"][-1],
            "time_series": ts,
        }

        if verbose and stages["has_three_stages"]:
            print(f"\n  Results for {label} complexity:")
            print(f"    C_ED(0) = {ts['C_ED'][0]:.6e}")
            print(f"    t*      = {stages['t_star']:.4f}")
            print(f"    sigma_measured  = {sigma_measured:.6f}")
            print(f"    sigma_predicted = {sigma_predicted:.6f}")
            ratio = sigma_measured / sigma_predicted if sigma_predicted > 0 else np.nan
            print(f"    ratio   = {ratio:.4f}")

    return results


def run_transition_time_sweep(param_set: str = "I",
                               A_values: np.ndarray = None,
                               T: float = 150.0,
                               verbose: bool = True) -> dict:
    """
    Sweep initial amplitude to measure t*(C_ED).

    Tests the prediction from Theorem C.76 that t* increases
    with initial complexity.

    Returns dict with arrays: A, C_ED_0, t_star.
    """
    if A_values is None:
        A_values = np.array([0.005, 0.01, 0.02, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3])

    A_list = []
    C_list = []
    t_star_list = []

    for A in A_values:
        if verbose:
            print(f"\n  A = {A:.3f} ...")

        params = load_parameter_set(param_set, T=T, method="crank_nicolson")
        config = RunConfig(
            params,
            ic_name="C",
            ic_kwargs={"A": A, "sigma": 0.05},
            run_id=f"tstar_sweep_{param_set}_A{A:.4f}",
        )
        result = run_simulation(config, verbose=False)
        ts = result["time_series"]
        stages = detect_three_stages(ts["t"], ts["E_total"], params)

        A_list.append(A)
        C_list.append(ts["C_ED"][0])
        t_star_list.append(stages["t_star"])

        if verbose:
            print(f"    C_ED(0) = {ts['C_ED'][0]:.4e}, t* = {stages['t_star']:.2f}")

    return {
        "A": np.array(A_list),
        "C_ED_0": np.array(C_list),
        "t_star": np.array(t_star_list),
    }


# ===================================================================
#  ENTRY POINT
# ===================================================================

if __name__ == "__main__":
    param_set = sys.argv[1] if len(sys.argv) > 1 else "I"

    print("=" * 60)
    print("  ED Three-Stage Convergence Experiment")
    print(f"  Parameter Set: {param_set}")
    print("=" * 60)

    results = run_three_stage_experiment(param_set=param_set, T=100.0)

    print("\n\nSummary:")
    print("-" * 60)
    print(f"{'Level':<10} {'C_ED(0)':<12} {'t*':<10} {'sigma_meas':<12} {'sigma_pred':<12} {'Pass'}")
    print("-" * 60)
    for label, r in results.items():
        if r["has_three_stages"]:
            ratio = r["sigma_measured"] / r["sigma_predicted"]
            passed = "YES" if abs(ratio - 1.0) < 0.05 else "NO"
        else:
            ratio = np.nan
            passed = "N/A"
        print(f"{label:<10} {r['C_ED_initial']:<12.4e} {r['t_star']:<10.2f} "
              f"{r['sigma_measured']:<12.6f} {r['sigma_predicted']:<12.6f} {passed}")
