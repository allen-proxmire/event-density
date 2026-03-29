"""Validation tests for visualization_2d.py — verify all plots render without error."""
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from edsim_solver_2d import *
from invariants_2d import *
from visualization_2d import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_output_viz")
os.makedirs(OUT, exist_ok=True)

print("=" * 70)
print("  VISUALIZATION_2D VALIDATION")
print("=" * 70)

# --- Setup ---
params = EDParameters2D(Nx=48, Ny=48, Lx=1.0, Ly=1.0, dt=5e-4, T=0.5,
                        method='etdrk4', k_out=100)
x = np.linspace(0, 1, 48)
y = np.linspace(0, 1, 48)
X, Y = np.meshgrid(x, y, indexing='ij')
rho_test = 0.5 + 0.05 * np.cos(np.pi * X) * np.cos(np.pi * Y)
rho_gauss = 0.5 + 0.1 * np.exp(-((X-0.5)**2 + (Y-0.5)**2) / 0.02)
rho_gauss = np.clip(rho_gauss, 1e-12, 0.999999)

n_pass = 0
n_fail = 0

def try_plot(name, func, *args, savepath=None, **kwargs):
    global n_pass, n_fail
    try:
        result = func(*args, **kwargs)
        if savepath and hasattr(result, 'savefig'):
            result.savefig(savepath, dpi=150, bbox_inches='tight')
        plt.close('all')
        n_pass += 1
        print(f"  PASS  {name}")
    except Exception as e:
        n_fail += 1
        print(f"  FAIL  {name}: {e}")

# --- A. Field visualizations ---
print("\n--- A. Field Visualizations ---")
try_plot("density_heatmap", plot_density_heatmap, rho_test, params,
         savepath=os.path.join(OUT, "density_heatmap.png"))
try_plot("density_contour", plot_density_contour, rho_test, params,
         savepath=os.path.join(OUT, "density_contour.png"))
try_plot("gradient_quiver", plot_gradient_quiver, rho_test, params,
         savepath=os.path.join(OUT, "gradient_quiver.png"))
try_plot("level_sets", plot_level_sets, rho_test, params,
         savepath=os.path.join(OUT, "level_sets.png"))
try_plot("level_sets+gradient", plot_level_sets, rho_test, params,
         show_gradient=True,
         savepath=os.path.join(OUT, "level_sets_grad.png"))
try_plot("field_quad", plot_field_quad, rho_test, params,
         savepath=os.path.join(OUT, "field_quad.png"))

# --- B. Spectral visualizations ---
print("\n--- B. Spectral Visualizations ---")
a = modal_amplitudes_2d(rho_test, 0.5, 1.0, 1.0)
sa = spectral_anisotropy(a, 1.0, 1.0)
try_plot("spectrum_2d", plot_spectrum_2d, a, 1.0, 1.0,
         savepath=os.path.join(OUT, "spectrum_2d.png"))
try_plot("radial_spectrum", plot_radial_spectrum, a, 1.0, 1.0,
         savepath=os.path.join(OUT, "radial_spectrum.png"))
try_plot("anisotropy_ellipse", plot_anisotropy_ellipse, sa,
         savepath=os.path.join(OUT, "anisotropy_ellipse.png"))
try_plot("spectral_overview", plot_spectral_overview, a, 1.0, 1.0, sa,
         savepath=os.path.join(OUT, "spectral_overview.png"))

# --- C. Geometric visualizations ---
print("\n--- C. Geometric Visualizations ---")
try_plot("hessian_max", plot_hessian_eigenvalues, rho_gauss, params,
         which='max', savepath=os.path.join(OUT, "hessian_max.png"))
try_plot("hessian_det", plot_hessian_eigenvalues, rho_gauss, params,
         which='det', savepath=os.path.join(OUT, "hessian_det.png"))
try_plot("filamentarity", plot_filamentarity_field, rho_gauss, params,
         savepath=os.path.join(OUT, "filamentarity.png"))
try_plot("curvature", plot_curvature_field, rho_gauss, params,
         savepath=os.path.join(OUT, "curvature.png"))
try_plot("geometry_quad", plot_geometry_2d, rho_gauss, params,
         savepath=os.path.join(OUT, "geometry_quad.png"))

# --- D. Horizon visualizations ---
print("\n--- D. Horizon Visualizations ---")
rho_nearmax = 0.5 + 0.45 * np.exp(-((X-0.5)**2 + (Y-0.5)**2) / 0.005)
rho_nearmax = np.clip(rho_nearmax, 1e-12, 0.999999)
try_plot("horizon_proximity", plot_horizon_proximity, rho_nearmax, params,
         savepath=os.path.join(OUT, "horizon_proximity.png"))
try_plot("horizon_mask", plot_horizon_mask, rho_nearmax, params,
         savepath=os.path.join(OUT, "horizon_mask.png"))
try_plot("horizon_overview", plot_horizon_2d, rho_nearmax, params,
         savepath=os.path.join(OUT, "horizon_overview.png"))

# --- E. Diagnostics ---
print("\n--- E. Diagnostic Plots ---")
print("  Running short simulation for time-series data...")
results = run_simulation_2d(params, perturbation='gaussian', amplitude=0.05,
                           verbose=False)
try_plot("time_series", plot_time_series, results,
         savepath=os.path.join(OUT, "time_series.png"))

try_plot("snapshot_evolution", plot_snapshot_evolution,
         results['rho_snapshots'], results['times'], params,
         savepath=os.path.join(OUT, "snapshot_evolution.png"))

# Invariant dashboard
rho_final = results['rho_snapshots'][-1]
F_rho = operator_F_fd_2d(rho_final, params)
F_bar = spatial_avg_2d(F_rho, params.hx, params.hy)
inv = compute_invariants_2d(rho_final, results['v_history'][-1], F_bar, params)
try_plot("invariant_dashboard", plot_invariants_2d, inv, params,
         savepath=os.path.join(OUT, "invariant_dashboard.png"))

# --- Summary ---
print("\n" + "=" * 70)
print(f"  RESULTS: {n_pass} PASS, {n_fail} FAIL out of {n_pass + n_fail}")
print(f"  Output saved to: {OUT}")
print("=" * 70)
