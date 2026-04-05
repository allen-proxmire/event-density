"""Validation tests for visualization_3d.py — verify all plots render without error."""
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from edsim_solver_3d import *
from invariants_3d import *
from visualization_3d import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_output_viz3d")
os.makedirs(OUT, exist_ok=True)

print("=" * 70)
print("  VISUALIZATION_3D VALIDATION")
print("=" * 70)

N = 16
params = EDParameters3D(Nx=N, Ny=N, Nz=N, Lx=1.0, Ly=1.0, Lz=1.0, dt=1e-3)
x = np.linspace(0, 1, N); y = np.linspace(0, 1, N); z = np.linspace(0, 1, N)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
rho_test = 0.5 + 0.05 * np.cos(np.pi*X) * np.cos(np.pi*Y) * np.cos(np.pi*Z)
rho_gauss = 0.5 + 0.1 * np.exp(-((X-0.5)**2 + (Y-0.5)**2 + (Z-0.5)**2) / 0.02)
rho_gauss = np.clip(rho_gauss, 1e-12, 0.999999)
rho_near = 0.5 + 0.48 * np.exp(-((X-0.5)**2 + (Y-0.5)**2 + (Z-0.5)**2) / 0.02)
rho_near = np.clip(rho_near, 1e-12, 0.999999)

n_pass = 0
n_fail = 0

def try_plot(name, func, *args, savepath=None, **kwargs):
    global n_pass, n_fail
    try:
        result = func(*args, **kwargs)
        # Save if result is a figure or list of figures
        if savepath:
            if isinstance(result, list):
                for i, f in enumerate(result):
                    if hasattr(f, 'savefig'):
                        f.savefig(savepath.replace('.png', f'_{i}.png'),
                                  dpi=150, bbox_inches='tight')
            elif hasattr(result, 'savefig'):
                result.savefig(savepath, dpi=150, bbox_inches='tight')
        plt.close('all')
        n_pass += 1
        print(f"  PASS  {name}")
    except Exception as e:
        n_fail += 1
        print(f"  FAIL  {name}: {e}")

# --- A. Field visualizations ---
print("\n--- A. Field Visualizations ---")
try_plot("density_slices", plot_density_slices, rho_test, params,
         savepath=os.path.join(OUT, "density_slices.png"))
try_plot("gradient_slices", plot_gradient_magnitude_slices, rho_test, params,
         savepath=os.path.join(OUT, "grad_slices.png"))
try_plot("max_intensity_proj", plot_max_intensity_projection, rho_gauss, params,
         savepath=os.path.join(OUT, "mip.png"))
try_plot("isosurface_contours", plot_isosurface_contours, rho_gauss, params,
         savepath=os.path.join(OUT, "iso_contours.png"))
try_plot("field_overview", plot_field_overview_3d, rho_gauss, params,
         savepath=os.path.join(OUT, "field_overview.png"))

# --- B. Spectral visualizations ---
print("\n--- B. Spectral Visualizations ---")
a = modal_amplitudes_3d(rho_test, 0.5, 1.0, 1.0, 1.0)
sa = spectral_anisotropy_3d(a, 1.0, 1.0, 1.0)
try_plot("spectrum_slice", plot_spectrum_3d, a, 1.0, 1.0, 1.0,
         savepath=os.path.join(OUT, "spectrum.png"))
try_plot("radial_spectrum", plot_radial_spectrum_3d, a, 1.0, 1.0, 1.0,
         savepath=os.path.join(OUT, "radial_spectrum.png"))
try_plot("anisotropy_ellipsoid", plot_anisotropy_ellipsoid, sa,
         savepath=os.path.join(OUT, "ellipsoid.png"))
try_plot("spectral_overview", plot_spectral_overview_3d, a, 1.0, 1.0, 1.0, sa,
         savepath=os.path.join(OUT, "spectral_overview.png"))

# --- C. Geometric visualizations ---
print("\n--- C. Geometric Visualizations ---")
try_plot("morphology_slices", plot_morphology_slices, rho_gauss, params,
         savepath=os.path.join(OUT, "morphology.png"))
try_plot("curvature_slices", plot_curvature_slices, rho_gauss, params,
         savepath=os.path.join(OUT, "curvature.png"))
try_plot("hessian_slices", plot_hessian_eigenvalue_slices, rho_gauss, params,
         savepath=os.path.join(OUT, "hessian.png"))
try_plot("geometry_composite", plot_geometry_3d, rho_gauss, params,
         savepath=os.path.join(OUT, "geometry.png"))

# --- D. Horizon visualizations ---
print("\n--- D. Horizon Visualizations ---")
try_plot("horizon_slices", plot_horizon_slices, rho_near, params,
         savepath=os.path.join(OUT, "horizon_prox.png"))
try_plot("horizon_mask", plot_horizon_mask_slices, rho_near, params,
         savepath=os.path.join(OUT, "horizon_mask.png"))
try_plot("horizon_composite", plot_horizon_3d, rho_near, params,
         savepath=os.path.join(OUT, "horizon.png"))

# --- E. Diagnostic plots ---
print("\n--- E. Diagnostic Plots ---")
print("  Running short simulation...")
p_run = EDParameters3D(Nx=12, Ny=12, Nz=12, dt=1e-3, T=0.05, method='etdrk4', k_out=50)
results = run_simulation_3d(p_run, perturbation='cosine', amplitude=0.03, verbose=False)
try_plot("time_series", plot_time_series_3d, results,
         savepath=os.path.join(OUT, "time_series.png"))

rho_f = results['final_state']['rho']
F_rho = operator_F_fd_3d(rho_f, p_run)
F_bar = spatial_avg_3d(F_rho, p_run.hx, p_run.hy, p_run.hz)
inv = compute_invariants_3d(rho_f, results['v_history'][-1], F_bar, p_run)
try_plot("invariant_dashboard", plot_invariants_3d, inv, p_run,
         savepath=os.path.join(OUT, "invariants.png"))

# --- Summary ---
print("\n" + "=" * 70)
print(f"  RESULTS: {n_pass} PASS, {n_fail} FAIL out of {n_pass + n_fail}")
print(f"  Output saved to: {OUT}")
print("=" * 70)
