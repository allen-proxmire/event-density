"""
edsim_runner.py
================
Main integration loop and experiment orchestration for the ED simulation engine.

Implements the time loop structure from Simulation Suite §2.3,
output logging from §2.4, checkpointing from §2.5, and error handling from §2.6.

All notation follows Appendix C of the Rigour Paper.
"""

import os
import json
import time
import hashlib
import numpy as np
from datetime import datetime, timezone
from dataclasses import asdict

from edsim_parameters import EDParameters
from edsim_core import (
    make_grid, step, energy, total_mass, enforce_bounds,
    SpectralState, operator_F_fd, spatial_avg_fd,
)
from edsim_diagnostics import diagnostic_snapshot, modal_amplitudes
from edsim_initial_conditions import load_ic


# ===================================================================
#  OUTPUT DIRECTORY MANAGEMENT
# ===================================================================

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
RUNS_DIR = os.path.join(OUTPUT_DIR, "runs")
LOGS_DIR = os.path.join(OUTPUT_DIR, "logs")
FIGURES_DIR = os.path.join(OUTPUT_DIR, "figures")
MANIFESTS_DIR = os.path.join(os.path.dirname(__file__), "manifests")


def ensure_dirs():
    """Create output directories if they don't exist."""
    for d in [RUNS_DIR, LOGS_DIR, FIGURES_DIR, MANIFESTS_DIR]:
        os.makedirs(d, exist_ok=True)


# ===================================================================
#  RUN CONFIGURATION
# ===================================================================

class RunConfig:
    """
    Complete specification of a single simulation run.

    Bundles parameters, initial condition, and output settings.
    """

    def __init__(self, params: EDParameters, ic_name: str = "A",
                 ic_kwargs: dict = None, run_id: str = None,
                 checkpoint_interval: int = 1000,
                 N_obs: int = 32):
        self.params = params
        self.ic_name = ic_name
        self.ic_kwargs = ic_kwargs or {}
        self.run_id = run_id or self._generate_run_id()
        self.checkpoint_interval = checkpoint_interval
        self.N_obs = N_obs

    def _generate_run_id(self) -> str:
        """Generate a unique run ID from timestamp and parameter hash."""
        ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        param_str = f"{self.params.D}_{self.params.zeta}_{self.params.tau}_{self.ic_name}"
        h = hashlib.md5(param_str.encode()).hexdigest()[:6]
        return f"run_{ts}_{h}"


# ===================================================================
#  TIME SERIES STORAGE
# ===================================================================

class TimeSeries:
    """
    In-memory storage for time-series diagnostics.

    Fields follow the time-series format specification (Suite §6.1).
    """

    def __init__(self, N_obs: int = 32):
        self.N_obs = N_obs
        self.t = []
        self.v = []
        self.E_total = []
        self.E_potential = []
        self.E_kinetic = []
        self.D_gradient = []
        self.D_penalty = []
        self.D_participation = []
        self.D_total = []
        self.C_ED = []
        self.C_ED_eff = []
        self.mass = []
        self.margin = []
        self.M_min = []
        self.rho_max_local = []
        self.modal_amplitudes = []  # list of arrays

    def append(self, snap: dict):
        """Append a diagnostic snapshot."""
        self.t.append(snap["t"])
        self.v.append(snap["v"])
        self.E_total.append(snap["E_total"])
        self.E_potential.append(snap["E_potential"])
        self.E_kinetic.append(snap["E_kinetic"])
        self.D_gradient.append(snap["D_gradient"])
        self.D_penalty.append(snap["D_penalty"])
        self.D_participation.append(snap["D_participation"])
        self.D_total.append(snap["D_total"])
        self.C_ED.append(snap["C_ED"])
        self.C_ED_eff.append(snap["C_ED_eff"])
        self.mass.append(snap["mass"])
        self.margin.append(snap["margin"])
        self.M_min.append(snap["M_min"])
        self.rho_max_local.append(snap["rho_max_local"])
        self.modal_amplitudes.append(snap["a"])

    def to_arrays(self) -> dict:
        """Convert all lists to numpy arrays."""
        return {
            "t": np.array(self.t),
            "v": np.array(self.v),
            "E_total": np.array(self.E_total),
            "E_potential": np.array(self.E_potential),
            "E_kinetic": np.array(self.E_kinetic),
            "D_gradient": np.array(self.D_gradient),
            "D_penalty": np.array(self.D_penalty),
            "D_participation": np.array(self.D_participation),
            "D_total": np.array(self.D_total),
            "C_ED": np.array(self.C_ED),
            "C_ED_eff": np.array(self.C_ED_eff),
            "mass": np.array(self.mass),
            "margin": np.array(self.margin),
            "M_min": np.array(self.M_min),
            "rho_max_local": np.array(self.rho_max_local),
            "modal_amplitudes": np.array(self.modal_amplitudes),
        }

    def save(self, filepath: str):
        """Save time series to .npz file."""
        arrays = self.to_arrays()
        np.savez_compressed(filepath, **arrays)

    @staticmethod
    def load(filepath: str) -> dict:
        """Load time series from .npz file."""
        return dict(np.load(filepath, allow_pickle=True))


# ===================================================================
#  MAIN INTEGRATION LOOP (Suite §2.3)
# ===================================================================

def run_simulation(config: RunConfig, verbose: bool = True) -> dict:
    """
    Execute a complete simulation run.

    Implements the time loop from Suite §2.3:
    1. Initialize grid, IC, parameters
    2. Main loop: step rho, step v, check diagnostics, log
    3. Stopping criteria: final time, energy convergence, or error

    Parameters
    ----------
    config : RunConfig
    verbose : print progress

    Returns
    -------
    dict with:
        'time_series' : TimeSeries arrays
        'final_rho' : final density profile
        'final_v' : final participation
        'metadata' : run metadata
        'status' : termination reason
    """
    ensure_dirs()
    params = config.params
    x = make_grid(params)

    # --- Initialize ---
    rho, v = load_ic(config.ic_name, x, params, **config.ic_kwargs)
    t = 0.0
    n_step = 0
    N_steps = int(np.ceil(params.T / params.dt))

    # Spectral state for ETD-RK4
    spectral = None
    u_hat = None
    if params.method == "etdrk4":
        spectral = SpectralState(params)
        u = rho - params.rho_star
        u_hat = spectral.to_spectral(u)

    # Time series storage
    ts = TimeSeries(N_obs=config.N_obs)

    # Initial snapshot
    snap0 = diagnostic_snapshot(rho, v, t, params, config.N_obs)
    ts.append(snap0)

    # Tracking
    E_prev = snap0["E_total"]
    wall_start = time.time()
    n_pos_total = 0
    n_cap_total = 0
    energy_warning_count = 0
    energy_warning_max = 20
    termination = "FinalTime"

    if verbose:
        print(params.summary())
        print(f"\nStarting integration: {N_steps} steps, T = {params.T}")
        print(f"IC = {config.ic_name}, method = {params.method}")
        print("-" * 60)

    # --- Main loop ---
    for n_step in range(1, N_steps + 1):
        t = n_step * params.dt

        # Step
        if params.method == "etdrk4":
            result = step(rho, v, params, spectral=spectral, u_hat=u_hat)
            rho = result["rho"]
            v = result["v"]
            u_hat = result["u_hat"]
        else:
            result = step(rho, v, params)
            rho = result["rho"]
            v = result["v"]
            n_pos_total += result.get("n_pos_violations", 0)
            n_cap_total += result.get("n_cap_violations", 0)

        # Enforce bounds (safety net)
        rho, n_p, n_c = enforce_bounds(rho, params)
        n_pos_total += n_p
        n_cap_total += n_c

        # --- Error detection (Suite §2.6) ---
        if np.any(np.isnan(rho)) or np.isnan(v):
            termination = "NaN_detected"
            if verbose:
                print(f"\n  ERROR: NaN at step {n_step}, t = {t:.4f}")
            break

        if np.any(np.isinf(rho)) or np.isinf(v):
            termination = "Inf_detected"
            if verbose:
                print(f"\n  ERROR: Inf at step {n_step}, t = {t:.4f}")
            break

        # --- Diagnostics at output steps ---
        if n_step % params.k_out == 0 or n_step == N_steps:
            snap = diagnostic_snapshot(rho, v, t, params, config.N_obs)
            ts.append(snap)

            # Energy monotonicity check
            E_cur = snap["E_total"]

            # Energy is theoretically non-increasing, but we ignore tiny drifts
            # below abs 1e-8 and rel 1e-6, and cap warnings at 20.
            dE = E_cur - E_prev
            abs_thresh = 1e-8
            rel_thresh = 1e-6  # relative to |E_prev|
            rel = dE / max(abs(E_prev), 1e-12)

            if dE > abs_thresh and rel > rel_thresh and energy_warning_count < energy_warning_max:
                if verbose:
                    print(f"  WARNING: energy increase at t={t:.4f}: "
                          f"dE = {dE:.6e} (rel = {rel:.3e})")
                energy_warning_count += 1
                if energy_warning_count == energy_warning_max:
                    print("  NOTE: further energy warnings suppressed (reached cap).")

            E_prev = E_cur

            # Convergence check: energy deviation < epsilon
            E_eq = 0.0  # E[rho*, 0]
            if abs(E_cur - E_eq) < 1e-14:
                termination = "Converged"
                if verbose:
                    print(f"\n  Converged at t = {t:.4f} (step {n_step})")
                break

        # --- Progress ---
        if verbose and n_step % (N_steps // 10 + 1) == 0:
            pct = 100.0 * n_step / N_steps
            wall = time.time() - wall_start
            print(f"  [{pct:5.1f}%] step {n_step}/{N_steps}, "
                  f"t = {t:.3f}, E = {E_prev:.6e}, "
                  f"wall = {wall:.1f}s")

        # --- Checkpointing ---
        if (config.checkpoint_interval > 0
                and n_step % config.checkpoint_interval == 0):
            _save_checkpoint(config, rho, v, t, n_step, ts)

    wall_total = time.time() - wall_start

    if verbose:
        print("-" * 60)
        print(f"Finished: {termination}")
        print(f"  Steps: {n_step}, Final t: {t:.4f}")
        print(f"  Wall time: {wall_total:.2f}s")
        print(f"  Positivity violations: {n_pos_total}")
        print(f"  Capacity violations: {n_cap_total}")

    # --- Metadata ---
    metadata = {
        "run_id": config.run_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "termination_reason": termination,
        "n_steps": n_step,
        "final_t": t,
        "wall_time_s": wall_total,
        "n_positivity_violations": n_pos_total,
        "n_capacity_violations": n_cap_total,
        "ic_name": config.ic_name,
        "ic_kwargs": config.ic_kwargs,
        "method": params.method,
        "D": params.D,
        "zeta": params.zeta,
        "tau": params.tau,
        "rho_star": params.rho_star,
        "rho_max": params.rho_max,
        "N": params.N,
        "L": params.L,
        "dt": params.dt,
        "T": params.T,
        "k_out": params.k_out,
        "M0": params.M0,
        "beta": params.beta,
        "P0": params.P0,
    }

    # --- Save outputs ---
    run_dir = os.path.join(RUNS_DIR, config.run_id)
    os.makedirs(run_dir, exist_ok=True)

    # Time series
    ts_path = os.path.join(run_dir, "time_series.npz")
    ts.save(ts_path)

    # Final state
    state_path = os.path.join(run_dir, "final_state.npz")
    np.savez_compressed(state_path, rho=rho, v=np.array([v]), t=np.array([t]))

    # Metadata
    meta_path = os.path.join(run_dir, "metadata.json")
    with open(meta_path, "w") as f:
        json.dump(metadata, f, indent=2, default=str)

    if verbose:
        print(f"\nOutputs saved to: {run_dir}")

    return {
        "time_series": ts.to_arrays(),
        "final_rho": rho,
        "final_v": v,
        "metadata": metadata,
        "status": termination,
    }


# ===================================================================
#  CHECKPOINTING (Suite §2.5)
# ===================================================================

def _save_checkpoint(config, rho, v, t, n_step, ts):
    """Save a checkpoint file for restart."""
    run_dir = os.path.join(RUNS_DIR, config.run_id)
    os.makedirs(run_dir, exist_ok=True)
    ckpt_path = os.path.join(run_dir, f"checkpoint_{n_step:08d}.npz")
    np.savez_compressed(ckpt_path,
                        rho=rho, v=np.array([v]),
                        t=np.array([t]), n_step=np.array([n_step]))


def load_checkpoint(filepath: str) -> dict:
    """Load a checkpoint file."""
    data = np.load(filepath, allow_pickle=True)
    return {
        "rho": data["rho"],
        "v": float(data["v"][0]),
        "t": float(data["t"][0]),
        "n_step": int(data["n_step"][0]),
    }


# ===================================================================
#  BATCH RUNNER
# ===================================================================

def run_batch(configs: list, verbose: bool = True) -> list:
    """
    Run a batch of simulations sequentially.

    Parameters
    ----------
    configs : list of RunConfig
    verbose : print progress

    Returns
    -------
    list of result dicts
    """
    results = []
    for i, config in enumerate(configs):
        if verbose:
            print(f"\n{'=' * 60}")
            print(f"  Batch run {i + 1}/{len(configs)}: {config.run_id}")
            print(f"{'=' * 60}")
        result = run_simulation(config, verbose=verbose)
        results.append(result)
    return results


# ===================================================================
#  QUICK RUN CONVENIENCE
# ===================================================================

def quick_run(param_set: str = "I", ic: str = "A", T: float = 50.0,
              method: str = "crank_nicolson", verbose: bool = True,
              **kwargs) -> dict:
    """
    Convenience function: run a simulation with a canonical parameter set.

    Parameters
    ----------
    param_set : 'I', 'II', 'III', 'IV', or 'V'
    ic : 'A', 'B', 'C', or 'D'
    T : final time
    method : time-stepping method
    verbose : print progress
    **kwargs : additional IC parameters

    Returns
    -------
    result dict
    """
    from edsim_parameters import load_parameter_set
    params = load_parameter_set(param_set, T=T, method=method)
    config = RunConfig(params, ic_name=ic, ic_kwargs=kwargs)
    return run_simulation(config, verbose=verbose)


# ===================================================================
#  ENTRY POINT
# ===================================================================

if __name__ == "__main__":
    import sys

    param_set = sys.argv[1] if len(sys.argv) > 1 else "I"
    ic = sys.argv[2] if len(sys.argv) > 2 else "A"

    print(f"Running ED simulation: Parameter Set {param_set}, IC-{ic}")
    result = quick_run(param_set=param_set, ic=ic)
    print(f"\nTermination: {result['status']}")
    print(f"Final energy: {result['time_series']['E_total'][-1]:.6e}")
    print(f"Final complexity: {result['time_series']['C_ED'][-1]:.6e}")
