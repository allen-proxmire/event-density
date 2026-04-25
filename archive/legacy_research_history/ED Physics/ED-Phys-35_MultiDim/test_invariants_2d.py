"""Validation tests for invariants_2d.py"""
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from edsim_solver_2d import *
from invariants_2d import *

print('=' * 70)
print('  INVARIANTS_2D VALIDATION TESTS')
print('=' * 70)

Nx, Ny = 64, 64
Lx, Ly = 1.0, 1.0
hx = Lx / (Nx - 1)
hy = Ly / (Ny - 1)
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y, indexing='ij')
rho_star = 0.5
params = EDParameters2D(Nx=Nx, Ny=Ny, Lx=Lx, Ly=Ly, dt=1e-4)

rho_iso = rho_star + 0.05 * np.cos(np.pi * X) * np.cos(np.pi * Y)
rho_xonly = rho_star + 0.05 * np.cos(np.pi * X)
rho_gauss = rho_star + 0.1 * np.exp(-((X-0.5)**2 + (Y-0.5)**2) / 0.02)
rho_uniform = np.full((Nx, Ny), rho_star)

n_pass = 0
n_fail = 0

def check(name, condition, detail=""):
    global n_pass, n_fail
    if condition:
        n_pass += 1
        print(f"  PASS  {name}  {detail}")
    else:
        n_fail += 1
        print(f"  FAIL  {name}  {detail}")

# --- T1: Parseval ---
print("\n--- T1: Modal amplitudes & Parseval ---")
a = modal_amplitudes_2d(rho_iso, rho_star, Lx, Ly, Kx_max=Nx, Ky_max=Ny)
E_spec = np.sum(a**2)
u = rho_iso - rho_star
from invariants_2d import _trap_2d
E_phys = _trap_2d(u**2, hx, hy)
ratio = E_spec / E_phys
check("Parseval L2 norm", abs(ratio - 1.0) < 0.02, f"ratio={ratio:.4f}")
check("Dominant mode (1,1)", a[1,1]**2 / E_spec > 0.95, f"frac={a[1,1]**2/E_spec:.4f}")

# --- T2: Entropy ---
print("\n--- T2: Spectral entropy ---")
H_iso = spectral_entropy_2d(modal_amplitudes_2d(rho_iso, rho_star, Lx, Ly))
H_gauss = spectral_entropy_2d(modal_amplitudes_2d(rho_gauss, rho_star, Lx, Ly))
check("Cosine entropy < Gauss entropy", H_iso < H_gauss,
      f"H_cos={H_iso:.4f}, H_gauss={H_gauss:.4f}")
check("Single-mode entropy is low", H_iso < 1.0, f"H_cos={H_iso:.4f}")

# --- T3: Renyi entropy ---
print("\n--- T3: Renyi entropy ---")
H1 = spectral_entropy_2d(modal_amplitudes_2d(rho_gauss, rho_star, Lx, Ly))
H2 = renyi_entropy_2d(modal_amplitudes_2d(rho_gauss, rho_star, Lx, Ly), 2.0)
H05 = renyi_entropy_2d(modal_amplitudes_2d(rho_gauss, rho_star, Lx, Ly), 0.5)
check("H_0.5 >= H_1 >= H_2 (Renyi ordering)", H05 >= H1 >= H2,
      f"H05={H05:.4f}, H1={H1:.4f}, H2={H2:.4f}")

# --- T4: Spectral anisotropy ---
print("\n--- T4: Spectral anisotropy ---")
aiso = spectral_anisotropy(modal_amplitudes_2d(rho_iso, rho_star, Lx, Ly), Lx, Ly)
axonly = spectral_anisotropy(modal_amplitudes_2d(rho_xonly, rho_star, Lx, Ly), Lx, Ly)
check("Isotropic A_spec ~ 0", abs(aiso['anisotropy']) < 0.1,
      f"A={aiso['anisotropy']:.4f}")
check("x-only A_spec ~ +1", axonly['anisotropy'] > 0.9,
      f"A={axonly['anisotropy']:.4f}")

# --- T5: Filamentarity ---
print("\n--- T5: Filamentarity ---")
f_xonly = filamentarity_2d(rho_xonly, hx, hy)
f_iso = filamentarity_2d(rho_iso, hx, hy)
check("x-only high filamentarity", f_xonly['filamentarity_mean'] > 0.8,
      f"F={f_xonly['filamentarity_mean']:.4f}")
check("Isotropic lower filamentarity", f_iso['filamentarity_mean'] < f_xonly['filamentarity_mean'],
      f"F_iso={f_iso['filamentarity_mean']:.4f}")

# --- T6: Geometric anisotropy ---
print("\n--- T6: Geometric anisotropy ---")
ag_iso = anisotropy_geometric_2d(rho_iso, hx, hy)
ag_xonly = anisotropy_geometric_2d(rho_xonly, hx, hy)
check("Isotropic A_geom ~ 0", abs(ag_iso['anisotropy_geometric']) < 0.15,
      f"A={ag_iso['anisotropy_geometric']:.4f}")
check("x-only A_geom ~ 1", ag_xonly['anisotropy_geometric'] > 0.95,
      f"A={ag_xonly['anisotropy_geometric']:.4f}")

# --- T7: Level-set curvature ---
print("\n--- T7: Level-set curvature ---")
lsc = level_set_curvature_2d(rho_gauss, hx, hy)
check("Gaussian has nonzero curvature", lsc['curvature_rms'] > 0,
      f"kappa_rms={lsc['curvature_rms']:.4f}")
lsc_u = level_set_curvature_2d(rho_xonly, hx, hy)
check("x-only has zero mean curvature", abs(lsc_u['curvature_mean']) < 0.5,
      f"kappa_mean={lsc_u['curvature_mean']:.4f}")

# --- T8: Correlation lengths ---
print("\n--- T8: Correlation lengths ---")
cl_iso = correlation_lengths_2d(rho_iso, hx, hy)
cl_xonly = correlation_lengths_2d(rho_xonly, hx, hy)
check("Isotropic xi_x ~ xi_y", abs(cl_iso['xi_ratio'] - 1.0) < 0.3,
      f"ratio={cl_iso['xi_ratio']:.4f}")
check("x-only xi_y >> xi_x", cl_xonly['xi_y'] > 2 * cl_xonly['xi_x'],
      f"xi_x={cl_xonly['xi_x']:.4f}, xi_y={cl_xonly['xi_y']:.4f}")

# --- T9: Dissipation ---
print("\n--- T9: Dissipation channels ---")
D_iso = dissipation_channels_2d(rho_iso, 0.0, params)
D_uniform = dissipation_channels_2d(rho_uniform, 0.0, params)
check("Uniform D_grad = 0", D_uniform['gradient'] < 1e-20,
      f"D_grad={D_uniform['gradient']:.2e}")
check("Uniform D_pen = 0", D_uniform['penalty'] < 1e-20,
      f"D_pen={D_uniform['penalty']:.2e}")
check("Iso D_grad > 0", D_iso['gradient'] > 0,
      f"D_grad={D_iso['gradient']:.4e}")

# --- T10: Horizon detector ---
print("\n--- T10: Horizon detector ---")
rho_near_max = rho_star + 0.45 * np.exp(-((X-0.5)**2 + (Y-0.5)**2) / 0.01)
rho_near_max = np.clip(rho_near_max, 1e-12, params.rho_max - 1e-12)
hz = horizon_detector_2d(rho_near_max, params)
hz_norm = horizon_detector_2d(rho_iso, params)
check("Near-max high proximity", hz['max_proximity'] > 0.9,
      f"prox={hz['max_proximity']:.4f}")
check("Normal field low proximity", hz_norm['max_proximity'] < 0.5,
      f"prox={hz_norm['max_proximity']:.4f}")

# --- T11: Structure functions ---
print("\n--- T11: Structure functions ---")
sf = structure_functions_2d(rho_gauss, hx, hy, orders=[2])
check("S_2 increases with lag", sf[2][-1] > sf[2][0],
      f"S_2[0]={sf[2][0]:.4e}, S_2[-1]={sf[2][-1]:.4e}")

# --- T12: Geometric norms ---
print("\n--- T12: Geometric norms ---")
a_gauss = modal_amplitudes_2d(rho_gauss, rho_star, Lx, Ly)
gn = geometric_norms_2d(a_gauss, Lx, Ly)
check("G_0 > 0 (total L2 excl k=0)", gn[0] > 0, f"G_0={gn[0]:.4e}")
check("G_1 > G_0 (gradient weighting)", gn[1] > gn[0],
      f"G_0={gn[0]:.4e}, G_1={gn[1]:.4e}")

# --- T13: Vorticity/twist ---
print("\n--- T13: Vorticity structure ---")
vs_iso = vorticity_structure_2d(rho_iso, hx, hy)
vs_xonly = vorticity_structure_2d(rho_xonly, hx, hy)
check("x-only twist_rms ~ 0", vs_xonly['twist_rms'] < 0.01,
      f"twist={vs_xonly['twist_rms']:.4e}")
check("Isotropic has nonzero twist", vs_iso['twist_rms'] > vs_xonly['twist_rms'],
      f"twist_iso={vs_iso['twist_rms']:.4e}")

# --- T14: Full dispatcher ---
print("\n--- T14: Full compute_invariants_2d ---")
F_rho = operator_F_fd_2d(rho_iso, params)
F_bar = spatial_avg_2d(F_rho, hx, hy)
inv = compute_invariants_2d(rho_iso, 0.0, F_bar, params)
check("Has spectral key", 'spectral' in inv)
check("Has geometric key", 'geometric' in inv)
check("Has dynamical key", 'dynamical' in inv)
check("Has structure_functions key", 'structure_functions' in inv)
n_scalar = 0
for cat in inv.values():
    if isinstance(cat, dict):
        n_scalar += len(cat)
check("Produces many metrics", n_scalar > 15, f"n_fields={n_scalar}")

# --- T15: Evolved field invariants ---
print("\n--- T15: Evolved field ---")
p_run = EDParameters2D(Nx=48, Ny=48, dt=5e-4, T=0.5, method='etdrk4', k_out=100)
state = initialize_state_2d(p_run, perturbation='gaussian', amplitude=0.05)
for _ in range(1000):
    state = step_2d(state, p_run)
rho_f = state['rho']
F_f = operator_F_fd_2d(rho_f, p_run)
F_bar_f = spatial_avg_2d(F_f, p_run.hx, p_run.hy)
inv_f = compute_invariants_2d(rho_f, state['v'], F_bar_f, p_run)
H_f = inv_f['spectral']['spectral_entropy']
C_f = inv_f['dynamical']['ed_complexity']
check("Evolved entropy is finite", 0 < H_f < 20, f"H={H_f:.4f}")
check("Evolved complexity is small (relaxed)", C_f < 0.01, f"C={C_f:.6e}")
diss_r = inv_f['dynamical']['dissipation_ratios']
check("Diss ratios sum ~ 1", abs(diss_r['R_grad'] + diss_r['R_pen'] + diss_r['R_part'] - 1.0) < 0.01,
      f"sum={diss_r['R_grad']+diss_r['R_pen']+diss_r['R_part']:.6f}")

# --- Summary ---
print("\n" + "=" * 70)
print(f"  RESULTS: {n_pass} PASS, {n_fail} FAIL out of {n_pass + n_fail} tests")
print("=" * 70)
