"""
experiments_2d.py
=================
Predefined 2D experiment scenarios for the canonical ED PDE.

Scenarios:
  A2D — Isotropic relaxation (cosine perturbation)
  B2D — Filament formation (x-only mode, anisotropic IC)
  C2D — Anisotropic collapse (multi-mode, asymmetric)
  D2D — Horizon emergence (large-amplitude Gaussian)

Each scenario function returns a RunConfig2D ready for execution.
The run_atlas_2d() function runs all four and produces a summary.
"""

import os
import json
import time
import numpy as np
import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning)

import sys
_PARENT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PARENT not in sys.path:
    sys.path.insert(0, _PARENT)

from edsim_solver_2d import (
    EDParameters2D, make_grid_2d, operator_F_fd_2d, spatial_avg_2d,
)
from invariants_2d import compute_invariants_2d
from edsim2d.runner_2d import (
    RunConfig2D, run_experiment_2d, run_batch_2d,
    export_results_2d, ensure_dirs, RUNS_DIR, FIGURES_DIR, ATLAS_DIR,
)

try:
    from visualization_2d import (
        plot_field_quad, plot_spectral_overview, plot_geometry_2d,
        plot_horizon_2d, plot_time_series, plot_invariants_2d,
        plot_snapshot_evolution,
    )
    from invariants_2d import (
        modal_amplitudes_2d, spectral_anisotropy,
    )
    HAS_VIZ = True
except ImportError:
    HAS_VIZ = False


# ===================================================================
#  SCENARIO DEFINITIONS
# ===================================================================

def scenario_A2D(N: int = 64, T: float = 1.0, dt: float = 5e-4,
                 method: str = "etdrk4", **overrides) -> RunConfig2D:
    """
    Scenario A2D: Isotropic Relaxation.

    IC: rho_star + 0.05 * cos(pi x) * cos(pi y)
    Physics: canonical Set I (D=0.3, zeta=0.1, tau=1.0)
    Expected: isotropic decay to equilibrium, energy monotone decrease,
              spectral entropy low (single mode).
    """
    params = EDParameters2D(
        D=0.3, zeta=0.1, tau=1.0, rho_star=0.5, rho_max=1.0,
        M0=1.0, beta=2.0, P0=1.0,
        Nx=N, Ny=N, Lx=1.0, Ly=1.0,
        dt=dt, T=T, method=method, boundary="neumann",
        k_out=max(1, int(T / dt / 50)),
        **overrides,
    )
    return RunConfig2D(params, ic_name="cosine",
                       ic_kwargs={"amplitude": 0.05},
                       run_id="A2D_relaxation")


def scenario_B2D(N: int = 64, T: float = 1.0, dt: float = 5e-4,
                 method: str = "etdrk4", **overrides) -> RunConfig2D:
    """
    Scenario B2D: Filament Formation.

    IC: rho_star + 0.08 * cos(pi x) (x-only mode; y-invariant)
    Physics: canonical Set I
    Expected: filamentary structure (F ~ 1), high geometric anisotropy,
              correlation length ratio xi_y >> xi_x.
    """
    Nx = N
    Ny = N
    Lx, Ly = 1.0, 1.0
    x = np.linspace(0, Lx, Nx)
    y = np.linspace(0, Ly, Ny)
    X, Y = np.meshgrid(x, y, indexing='ij')
    rho_init = 0.5 + 0.08 * np.cos(np.pi * X / Lx)

    params = EDParameters2D(
        D=0.3, zeta=0.1, tau=1.0, rho_star=0.5, rho_max=1.0,
        M0=1.0, beta=2.0, P0=1.0,
        Nx=Nx, Ny=Ny, Lx=Lx, Ly=Ly,
        dt=dt, T=T, method=method, boundary="neumann",
        k_out=max(1, int(T / dt / 50)),
        **overrides,
    )
    return RunConfig2D(params, ic_name="gaussian",
                       ic_kwargs={"amplitude": 0.0, "rho_init": rho_init},
                       run_id="B2D_filament")


def scenario_C2D(N: int = 64, T: float = 1.0, dt: float = 5e-4,
                 method: str = "etdrk4", **overrides) -> RunConfig2D:
    """
    Scenario C2D: Anisotropic Collapse.

    IC: Multi-mode with different amplitudes in x and y.
        rho = rho* + 0.04*cos(pi x) + 0.015*cos(pi y) + 0.01*cos(2pi x)*cos(pi y)
    Physics: Set II (D=0.6, zeta=0.5)
    Expected: anisotropic spectral structure, mode coupling,
              saddle formation in Hessian.
    """
    Nx = N
    Ny = N
    Lx, Ly = 1.0, 1.0
    x = np.linspace(0, Lx, Nx)
    y = np.linspace(0, Ly, Ny)
    X, Y = np.meshgrid(x, y, indexing='ij')
    rho_init = (0.5
                + 0.04 * np.cos(np.pi * X / Lx)
                + 0.015 * np.cos(np.pi * Y / Ly)
                + 0.01 * np.cos(2 * np.pi * X / Lx) * np.cos(np.pi * Y / Ly))

    params = EDParameters2D(
        D=0.6, zeta=0.5, tau=1.0, rho_star=0.5, rho_max=1.0,
        M0=1.0, beta=2.0, P0=1.0,
        Nx=Nx, Ny=Ny, Lx=Lx, Ly=Ly,
        dt=dt, T=T, method=method, boundary="neumann",
        k_out=max(1, int(T / dt / 50)),
        **overrides,
    )
    return RunConfig2D(params, ic_name="gaussian",
                       ic_kwargs={"amplitude": 0.0, "rho_init": rho_init},
                       run_id="C2D_anisotropic")


def scenario_D2D(N: int = 64, T: float = 0.5, dt: float = 2e-4,
                 method: str = "etdrk4", **overrides) -> RunConfig2D:
    """
    Scenario D2D: Horizon Emergence.

    IC: rho_star + 0.4 * exp(-(r^2)/(2*0.01)) (large-amplitude Gaussian)
    Physics: Set IV (D=0.9, zeta=5.0) — strong diffusion, heavy damping
    Expected: horizon proximity approaches 1 near the peak,
              mobility collapse, filamentary structure near the horizon edge.
    """
    Nx = N
    Ny = N
    Lx, Ly = 1.0, 1.0
    x = np.linspace(0, Lx, Nx)
    y = np.linspace(0, Ly, Ny)
    X, Y = np.meshgrid(x, y, indexing='ij')
    rho_init = 0.5 + 0.4 * np.exp(-((X - 0.5)**2 + (Y - 0.5)**2) / 0.02)
    rho_init = np.clip(rho_init, 1e-12, 0.999999)

    params = EDParameters2D(
        D=0.9, zeta=5.0, tau=1.0, rho_star=0.5, rho_max=1.0,
        M0=1.0, beta=2.0, P0=1.0,
        Nx=Nx, Ny=Ny, Lx=Lx, Ly=Ly,
        dt=dt, T=T, method=method, boundary="neumann",
        k_out=max(1, int(T / dt / 50)),
        **overrides,
    )
    return RunConfig2D(params, ic_name="gaussian",
                       ic_kwargs={"amplitude": 0.0, "rho_init": rho_init},
                       run_id="D2D_horizon")


ALL_SCENARIOS = {
    "A2D": scenario_A2D,
    "B2D": scenario_B2D,
    "C2D": scenario_C2D,
    "D2D": scenario_D2D,
}


# ===================================================================
#  ATLAS RUNNER
# ===================================================================

def run_atlas_2d(N: int = 64, T: float = 1.0, dt: float = 5e-4,
                 method: str = "etdrk4",
                 scenarios: list = None,
                 verbose: bool = True,
                 generate_figures: bool = True) -> dict:
    """
    Run the full 2D atlas: all four scenarios with diagnostics and figures.

    Returns
    -------
    atlas : dict with per-scenario results and summary.
    """
    ensure_dirs()
    if scenarios is None:
        scenarios = list(ALL_SCENARIOS.keys())

    atlas = {
        "dimension": 2,
        "N": N,
        "T": T,
        "dt": dt,
        "method": method,
        "scenarios": {},
    }

    for scenario_name in scenarios:
        if verbose:
            print(f"\n{'='*60}")
            print(f"  SCENARIO {scenario_name}")
            print(f"{'='*60}")

        config_fn = ALL_SCENARIOS[scenario_name]
        if scenario_name == "D2D":
            config = config_fn(N=N, T=min(T, 0.5), dt=dt, method=method)
        else:
            config = config_fn(N=N, T=T, dt=dt, method=method)

        result = run_experiment_2d(config, verbose=verbose, save=True)

        # Compute invariants on final state
        rho_f = result['final_rho']
        v_f = result['final_v']
        params = config.params
        F_rho = operator_F_fd_2d(rho_f, params)
        F_bar = spatial_avg_2d(F_rho, params.hx, params.hy)
        inv = compute_invariants_2d(rho_f, v_f, F_bar, params,
                                    Kx_max=config.N_obs, Ky_max=config.N_obs)

        # Generate figures
        if generate_figures and HAS_VIZ:
            fig_dir = os.path.join(FIGURES_DIR, scenario_name)
            os.makedirs(fig_dir, exist_ok=True)

            try:
                plot_field_quad(rho_f, params,
                               savepath=os.path.join(fig_dir, "field_quad.png"))
                plot_time_series(
                    {'times': result['snapshot_times'],
                     'energy_history': [{'total': e, 'potential': e, 'kinetic': 0}
                                        for e in result['time_series']['E_total']],
                     'mass_history': result['time_series']['mass'],
                     'v_history': result['time_series']['v'],
                     'F_bar_history': np.zeros(len(result['time_series']['t']))},
                    savepath=os.path.join(fig_dir, "time_series.png"))
                plot_snapshot_evolution(
                    result['rho_snapshots'], result['snapshot_times'], params,
                    savepath=os.path.join(fig_dir, "evolution.png"))
                plot_invariants_2d(inv, params,
                                   savepath=os.path.join(fig_dir, "invariants.png"))
                plot_geometry_2d(rho_f, params,
                                savepath=os.path.join(fig_dir, "geometry.png"))
                if scenario_name == "D2D":
                    plot_horizon_2d(rho_f, params,
                                   savepath=os.path.join(fig_dir, "horizon.png"))
                import matplotlib.pyplot as plt
                plt.close('all')
                if verbose:
                    print(f"  Figures saved to: {fig_dir}")
            except Exception as e:
                if verbose:
                    print(f"  WARNING: Figure generation failed: {e}")

        # Collect scalar summary
        spec = inv['spectral']
        dyn = inv['dynamical']
        geo = inv['geometric']
        scenario_summary = {
            "status": result['status'],
            "wall_time_s": result['metadata']['wall_time_s'],
            "final_t": result['metadata']['final_t'],
            "E_final": float(result['time_series']['E_total'][-1]),
            "E_ratio": float(result['time_series']['E_total'][-1]
                            / max(result['time_series']['E_total'][0], 1e-30)),
            "mass_relative_change": float(abs(
                result['time_series']['mass'][-1]
                / max(result['time_series']['mass'][0], 1e-30) - 1)),
            "spectral_entropy": float(spec['spectral_entropy']),
            "ed_complexity": float(dyn['ed_complexity']),
            "anisotropy_spectral": float(spec['spectral_anisotropy']['anisotropy']),
            "anisotropy_geometric": float(geo['anisotropy_geometric']['anisotropy_geometric']),
            "filamentarity": float(geo['filamentarity']['filamentarity_mean']),
            "horizon_max_proximity": float(geo['horizon']['max_proximity']),
            "R_grad": float(dyn['dissipation_ratios']['R_grad']),
            "R_pen": float(dyn['dissipation_ratios']['R_pen']),
            "R_part": float(dyn['dissipation_ratios']['R_part']),
            "n_pos_violations": result['metadata']['n_positivity_violations'],
            "n_cap_violations": result['metadata']['n_capacity_violations'],
        }
        atlas["scenarios"][scenario_name] = scenario_summary

        if verbose:
            print(f"  Summary: E_ratio={scenario_summary['E_ratio']:.4f}, "
                  f"H={scenario_summary['spectral_entropy']:.4f}, "
                  f"A_spec={scenario_summary['anisotropy_spectral']:.4f}, "
                  f"F={scenario_summary['filamentarity']:.4f}, "
                  f"H_prox={scenario_summary['horizon_max_proximity']:.4f}")

    # Save atlas report
    atlas_path = os.path.join(ATLAS_DIR, "atlas_2d_report.json")
    with open(atlas_path, "w") as f:
        json.dump(atlas, f, indent=2)
    if verbose:
        print(f"\nAtlas report saved to: {atlas_path}")

    return atlas


# ===================================================================
#  ENTRY POINT
# ===================================================================

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run 2D ED atlas experiments")
    parser.add_argument("-N", type=int, default=48, help="Grid size per axis")
    parser.add_argument("-T", type=float, default=0.5, help="Simulation time")
    parser.add_argument("--dt", type=float, default=5e-4, help="Time step")
    parser.add_argument("--method", default="etdrk4", help="Solver method")
    parser.add_argument("--no-figures", action="store_true")
    parser.add_argument("--scenario", type=str, default=None,
                        help="Run single scenario (A2D, B2D, C2D, D2D)")
    args = parser.parse_args()

    scenarios = [args.scenario] if args.scenario else None
    run_atlas_2d(N=args.N, T=args.T, dt=args.dt, method=args.method,
                 scenarios=scenarios, generate_figures=not args.no_figures)
