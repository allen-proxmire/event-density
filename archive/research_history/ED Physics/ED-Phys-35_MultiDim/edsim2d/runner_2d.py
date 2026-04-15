"""
runner_2d.py
============
Experiment orchestration for 2D ED simulations.

Mirrors the 1D edsim_runner.py architecture: RunConfig -> TimeSeries -> run_simulation.
Output format: metadata.json + time_series.npz + final_state.npz per run.
"""

import os
import json
import time
import hashlib
import numpy as np
from datetime import datetime, timezone
from typing import Dict, List, Optional

import sys
_PARENT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PARENT not in sys.path:
    sys.path.insert(0, _PARENT)

from edsim_solver_2d import (
    EDParameters2D, make_grid_2d, initialize_state_2d, step_2d,
    energy_2d, total_mass_2d, spatial_avg_2d, operator_F_fd_2d,
    enforce_bounds_2d,
)
from invariants_2d import (
    compute_invariants_2d, modal_amplitudes_2d, spectral_entropy_2d,
    ed_complexity_2d, dissipation_channels_2d,
)


# ===================================================================
#  OUTPUT DIRECTORY MANAGEMENT
# ===================================================================

_MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(_MODULE_DIR, "output")
RUNS_DIR = os.path.join(OUTPUT_DIR, "runs")
FIGURES_DIR = os.path.join(OUTPUT_DIR, "figures")
ATLAS_DIR = os.path.join(OUTPUT_DIR, "atlas")


def ensure_dirs():
    for d in [RUNS_DIR, FIGURES_DIR, ATLAS_DIR]:
        os.makedirs(d, exist_ok=True)


# ===================================================================
#  RUN CONFIGURATION (mirrors edsim_runner.RunConfig)
# ===================================================================

class RunConfig2D:
    """
    Complete specification of a single 2D simulation run.

    Parameters
    ----------
    params : EDParameters2D
    ic_name : initial condition identifier ("cosine", "gaussian", "random", etc.)
    ic_kwargs : extra keyword arguments for IC generation
    run_id : unique string identifier (auto-generated if None)
    N_obs : number of spectral modes to observe per axis
    """

    def __init__(self, params: EDParameters2D,
                 ic_name: str = "gaussian",
                 ic_kwargs: Optional[dict] = None,
                 run_id: Optional[str] = None,
                 N_obs: int = 16):
        self.params = params
        self.ic_name = ic_name
        self.ic_kwargs = ic_kwargs or {}
        self.run_id = run_id or self._generate_run_id()
        self.N_obs = N_obs

    def _generate_run_id(self) -> str:
        ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        param_str = f"2d_{self.params.D}_{self.params.Nx}_{self.ic_name}"
        h = hashlib.md5(param_str.encode()).hexdigest()[:6]
        return f"run2d_{ts}_{h}"


# ===================================================================
#  TIME SERIES STORAGE (mirrors edsim_runner.TimeSeries)
# ===================================================================

class TimeSeries2D:
    """
    In-memory storage for 2D time-series diagnostics.

    Stores scalar fields at each output step. Modal amplitudes
    are stored as flattened 2D arrays.
    """

    def __init__(self, N_obs: int = 16):
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
        self.mass = []
        self.spectral_entropy = []
        self.rho_max_local = []
        self.rho_min_local = []
        self.horizon_margin = []
        self.modal_amplitudes = []  # list of (N_obs, N_obs) arrays

    def append(self, snap: dict):
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
        self.mass.append(snap["mass"])
        self.spectral_entropy.append(snap["spectral_entropy"])
        self.rho_max_local.append(snap["rho_max_local"])
        self.rho_min_local.append(snap["rho_min_local"])
        self.horizon_margin.append(snap["horizon_margin"])
        self.modal_amplitudes.append(snap["modal_amplitudes"])

    def to_arrays(self) -> dict:
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
            "mass": np.array(self.mass),
            "spectral_entropy": np.array(self.spectral_entropy),
            "rho_max_local": np.array(self.rho_max_local),
            "rho_min_local": np.array(self.rho_min_local),
            "horizon_margin": np.array(self.horizon_margin),
            "modal_amplitudes": np.array(self.modal_amplitudes),
        }

    def save(self, filepath: str):
        np.savez_compressed(filepath, **self.to_arrays())

    @staticmethod
    def load(filepath: str) -> dict:
        return dict(np.load(filepath, allow_pickle=True))


# ===================================================================
#  DIAGNOSTIC SNAPSHOT
# ===================================================================

def diagnostic_snapshot_2d(rho: np.ndarray, v: float, t: float,
                           params: EDParameters2D,
                           N_obs: int = 16) -> dict:
    """Compute a complete diagnostic snapshot at one time step."""
    E = energy_2d(rho, v, params)
    D = dissipation_channels_2d(rho, v, params)
    C = ed_complexity_2d(rho, params.hx, params.hy)
    m = total_mass_2d(rho, params.hx, params.hy)
    a = modal_amplitudes_2d(rho, params.rho_star, params.Lx, params.Ly,
                            Kx_max=N_obs, Ky_max=N_obs)
    H = spectral_entropy_2d(a)

    return {
        "t": float(t),
        "v": float(v),
        "E_total": E["total"],
        "E_potential": E["potential"],
        "E_kinetic": E["kinetic"],
        "D_gradient": D["gradient"],
        "D_penalty": D["penalty"],
        "D_participation": D["participation"],
        "D_total": D["total"],
        "C_ED": C,
        "mass": m,
        "spectral_entropy": H,
        "rho_max_local": float(np.max(rho)),
        "rho_min_local": float(np.min(rho)),
        "horizon_margin": float(np.min(params.rho_max - rho)),
        "modal_amplitudes": a,
    }


# ===================================================================
#  MAIN INTEGRATION LOOP
# ===================================================================

def run_experiment_2d(config: RunConfig2D, verbose: bool = True,
                      save: bool = True) -> dict:
    """
    Execute a complete 2D simulation experiment.

    Mirrors edsim_runner.run_simulation with 2D diagnostics.

    Parameters
    ----------
    config : RunConfig2D
    verbose : print progress
    save : write output to disk (metadata.json, time_series.npz, final_state.npz)

    Returns
    -------
    dict with: 'time_series', 'final_rho', 'final_v', 'metadata', 'status',
               'rho_snapshots' (list of arrays at output steps)
    """
    ensure_dirs()
    params = config.params

    # --- Output directory ---
    run_dir = os.path.join(RUNS_DIR, config.run_id)
    if save:
        os.makedirs(run_dir, exist_ok=True)

    # --- Initialize ---
    ic_kwargs = dict(config.ic_kwargs)
    perturbation = config.ic_name
    amplitude = ic_kwargs.pop("amplitude", 0.05)
    seed = ic_kwargs.pop("seed", None)
    rho_init = ic_kwargs.pop("rho_init", None)

    state = initialize_state_2d(params, rho_init=rho_init,
                                perturbation=perturbation,
                                amplitude=amplitude, seed=seed)

    n_steps = int(np.ceil(params.T / params.dt))
    ts = TimeSeries2D(N_obs=config.N_obs)

    # Initial snapshot
    snap0 = diagnostic_snapshot_2d(state['rho'], state['v'], 0.0,
                                   params, config.N_obs)
    ts.append(snap0)

    rho_snapshots = [state['rho'].copy()]
    snapshot_times = [0.0]

    wall_start = time.time()
    n_pos_total = 0
    n_cap_total = 0
    termination = "FinalTime"

    if verbose:
        print(params.summary())
        print(f"Run ID: {config.run_id}")
        print(f"Running {n_steps} steps...")

    # --- Main loop ---
    for n in range(1, n_steps + 1):
        state = step_2d(state, params)
        n_pos_total += state.get('n_pos', 0)
        n_cap_total += state.get('n_cap', 0)

        # Check for NaN/Inf
        if np.any(np.isnan(state['rho'])) or np.any(np.isinf(state['rho'])):
            termination = "NaN_detected"
            if verbose:
                print(f"  WARNING: NaN/Inf at step {n}")
            break

        # Diagnostic output
        if n % params.k_out == 0 or n == n_steps:
            snap = diagnostic_snapshot_2d(state['rho'], state['v'],
                                          state['t'], params, config.N_obs)
            ts.append(snap)
            rho_snapshots.append(state['rho'].copy())
            snapshot_times.append(state['t'])

            if verbose and n % (10 * params.k_out) == 0:
                E = snap["E_total"]
                m = snap["mass"]
                H = snap["spectral_entropy"]
                print(f"  step {n:>8d}/{n_steps}, t={state['t']:.4f}, "
                      f"E={E:.4e}, H={H:.4f}, mass={m:.6e}")

    wall_time = time.time() - wall_start

    # --- Metadata ---
    metadata = {
        "run_id": config.run_id,
        "dimension": 2,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "termination_reason": termination,
        "n_steps": n_steps,
        "final_t": state['t'],
        "wall_time_s": wall_time,
        "n_positivity_violations": n_pos_total,
        "n_capacity_violations": n_cap_total,
        "ic_name": config.ic_name,
        "ic_kwargs": {k: v for k, v in config.ic_kwargs.items()
                      if not isinstance(v, np.ndarray)},
        "method": params.method,
        "boundary": params.boundary,
        "D": params.D,
        "H": params.H,
        "zeta": params.zeta,
        "tau": params.tau,
        "rho_star": params.rho_star,
        "rho_max": params.rho_max,
        "M0": params.M0,
        "beta": params.beta,
        "P0": params.P0,
        "Nx": params.Nx,
        "Ny": params.Ny,
        "Lx": params.Lx,
        "Ly": params.Ly,
        "dt": params.dt,
        "T": params.T,
        "k_out": params.k_out,
        "N_obs": config.N_obs,
    }

    # --- Save ---
    if save:
        ts.save(os.path.join(run_dir, "time_series.npz"))
        np.savez_compressed(os.path.join(run_dir, "final_state.npz"),
                            rho=state['rho'], v=state['v'], t=state['t'])
        with open(os.path.join(run_dir, "metadata.json"), "w") as f:
            json.dump(metadata, f, indent=2)
        if verbose:
            print(f"  Output saved to: {run_dir}")

    if verbose:
        print(f"Done in {wall_time:.1f}s. Status: {termination}")

    return {
        'time_series': ts.to_arrays(),
        'final_rho': state['rho'],
        'final_v': state['v'],
        'metadata': metadata,
        'status': termination,
        'rho_snapshots': rho_snapshots,
        'snapshot_times': snapshot_times,
    }


def run_batch_2d(configs: List[RunConfig2D],
                 verbose: bool = True) -> List[dict]:
    """Run a batch of 2D simulations sequentially."""
    results = []
    for i, config in enumerate(configs):
        if verbose:
            print(f"\n{'='*60}")
            print(f"  Batch run {i+1}/{len(configs)}: {config.run_id}")
            print(f"{'='*60}")
        result = run_experiment_2d(config, verbose=verbose)
        results.append(result)
    return results


def export_results_2d(result: dict, out_dir: str):
    """
    Export a completed experiment result to a specific directory.

    Writes metadata.json, time_series.npz, and final_state.npz.
    """
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "metadata.json"), "w") as f:
        json.dump(result['metadata'], f, indent=2)
    ts_arrays = result['time_series']
    np.savez_compressed(os.path.join(out_dir, "time_series.npz"), **ts_arrays)
    np.savez_compressed(os.path.join(out_dir, "final_state.npz"),
                        rho=result['final_rho'],
                        v=result['final_v'],
                        t=result['metadata']['final_t'])
