"""Validation tests for invariants_3d.py"""
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from edsim_solver_3d import *
from invariants_3d import *
from invariants_3d import _trap_3d

print("=" * 70)
print("  INVARIANTS_3D VALIDATION TESTS")
print("=" * 70)

N = 16
Lx = Ly = Lz = 1.0
hx = hy = hz = Lx / (N - 1)
x = np.linspace(0, Lx, N); y = np.linspace(0, Ly, N); z = np.linspace(0, Lz, N)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
rho_star = 0.5

rho_iso = rho_star + 0.05 * np.cos(np.pi*X) * np.cos(np.pi*Y) * np.cos(np.pi*Z)
rho_xonly = rho_star + 0.05 * np.cos(np.pi*X)
rho_gauss = rho_star + 0.1 * np.exp(-((X-0.5)**2 + (Y-0.5)**2 + (Z-0.5)**2) / 0.02)
rho_gauss = np.clip(rho_gauss, 1e-12, 0.999999)
rho_uniform = np.full((N, N, N), rho_star)
params = EDParameters3D(Nx=N, Ny=N, Nz=N, Lx=Lx, Ly=Ly, Lz=Lz, dt=1e-3)

n_pass = 0
n_fail = 0

def check(name, cond, detail=""):
    global n_pass, n_fail
    if cond:
        n_pass += 1; print(f"  PASS  {name}  {detail}")
    else:
        n_fail += 1; print(f"  FAIL  {name}  {detail}")

# --- T1: Parseval ---
print("\n--- T1: Modal amplitudes & Parseval ---")
a = modal_amplitudes_3d(rho_iso, rho_star, Lx, Ly, Lz, Kx_max=N, Ky_max=N, Kz_max=N)
E_spec = np.sum(a**2)
u = rho_iso - rho_star
E_phys = _trap_3d(u**2, hx, hy, hz)
ratio = E_spec / E_phys
check("Parseval", abs(ratio - 1.0) < 0.02, f"ratio={ratio:.4f}")
check("Dominant (1,1,1)", a[1,1,1]**2 / E_spec > 0.95, f"frac={a[1,1,1]**2/E_spec:.4f}")

# --- T2: Entropy ---
print("\n--- T2: Spectral entropy ---")
H_iso = spectral_entropy_3d(modal_amplitudes_3d(rho_iso, rho_star, Lx, Ly, Lz))
H_gauss = spectral_entropy_3d(modal_amplitudes_3d(rho_gauss, rho_star, Lx, Ly, Lz))
check("Cosine H < Gauss H", H_iso < H_gauss, f"H_cos={H_iso:.4f}, H_gauss={H_gauss:.4f}")

# --- T3: Renyi ordering ---
print("\n--- T3: Renyi entropy ---")
ag = modal_amplitudes_3d(rho_gauss, rho_star, Lx, Ly, Lz)
H1 = spectral_entropy_3d(ag)
H2 = renyi_entropy_3d(ag, 2.0)
H05 = renyi_entropy_3d(ag, 0.5)
check("H_0.5 >= H_1 >= H_2", H05 >= H1 >= H2, f"H05={H05:.3f}, H1={H1:.3f}, H2={H2:.3f}")

# --- T4: Spectral anisotropy ---
print("\n--- T4: Spectral anisotropy ---")
# Multi-mode field for true spectral isotropy
rho_multi = rho_star + 0.02 * (np.cos(np.pi*X) + np.cos(np.pi*Y) + np.cos(np.pi*Z))
sa_multi = spectral_anisotropy_3d(modal_amplitudes_3d(rho_multi, rho_star, Lx, Ly, Lz), Lx, Ly, Lz)
sa_x = spectral_anisotropy_3d(modal_amplitudes_3d(rho_xonly, rho_star, Lx, Ly, Lz), Lx, Ly, Lz)
check("Multi-mode: isotropy ~ 1", sa_multi['isotropy'] > 0.9, f"iso={sa_multi['isotropy']:.4f}")
check("x-only: linearity ~ 1", sa_x['linearity'] > 0.9, f"lin={sa_x['linearity']:.4f}")

# --- T5: Morphology ---
print("\n--- T5: Morphology ---")
morph_iso = morphology_3d(rho_iso, hx, hy, hz)
morph_x = morphology_3d(rho_xonly, hx, hy, hz)
check("x-only high sheetness", morph_x['sheetness_mean'] > morph_iso['sheetness_mean'],
      f"S_x={morph_x['sheetness_mean']:.3f}")
check("Fractions sum to ~1",
      abs(morph_iso['filament_fraction'] + morph_iso['sheet_fraction'] + morph_iso['blob_fraction'] - 1) < 0.02,
      f"sum={morph_iso['filament_fraction']+morph_iso['sheet_fraction']+morph_iso['blob_fraction']:.4f}")

# --- T6: Curvature ---
print("\n--- T6: Curvature invariants ---")
curv = curvature_invariants_3d(rho_gauss, hx, hy, hz)
check("Gauss has nonzero mean curvature", curv['mean_curvature_rms'] > 0,
      f"H_rms={curv['mean_curvature_rms']:.4f}")
check("Gauss has nonzero Gaussian curvature", curv['gaussian_curvature_rms'] > 0,
      f"K_rms={curv['gaussian_curvature_rms']:.4f}")

# --- T7: Twist ---
print("\n--- T7: Twist tensor ---")
tw_x = twist_tensor_3d(rho_xonly, hx, hy, hz)
tw_iso = twist_tensor_3d(rho_iso, hx, hy, hz)
check("x-only twist ~ 0", tw_x['twist_rms'] < 1e-10, f"twist={tw_x['twist_rms']:.4e}")
check("Isotropic has twist", tw_iso['twist_rms'] > tw_x['twist_rms'],
      f"twist_iso={tw_iso['twist_rms']:.4e}")

# --- T8: Geometric anisotropy ---
print("\n--- T8: Geometric anisotropy ---")
ag_iso = anisotropy_geometric_3d(rho_iso, hx, hy, hz)
ag_x = anisotropy_geometric_3d(rho_xonly, hx, hy, hz)
check("Isotropic: isotropy ~ 1", ag_iso['isotropy'] > 0.9, f"iso={ag_iso['isotropy']:.4f}")
check("x-only: linearity ~ 1", ag_x['linearity'] > 0.9, f"lin={ag_x['linearity']:.4f}")

# --- T9: Dissipation ---
print("\n--- T9: Dissipation ---")
D_u = dissipation_channels_3d(rho_uniform, 0.0, params)
check("Uniform D_grad=0", D_u['gradient'] < 1e-20, f"D_grad={D_u['gradient']:.2e}")
D_iso = dissipation_channels_3d(rho_iso, 0.0, params)
check("Iso D_grad>0", D_iso['gradient'] > 0, f"D_grad={D_iso['gradient']:.4e}")
dr = dissipation_ratios_3d(rho_iso, 0.0, params)
check("Ratios sum ~ 1", abs(dr['R_grad'] + dr['R_pen'] + dr['R_part'] - 1) < 0.01,
      f"sum={dr['R_grad']+dr['R_pen']+dr['R_part']:.6f}")

# --- T10: Correlation lengths ---
print("\n--- T10: Correlation lengths ---")
cl_iso = correlation_lengths_3d(rho_iso, hx, hy, hz)
cl_x = correlation_lengths_3d(rho_xonly, hx, hy, hz)
check("Isotropic xi_x ~ xi_y ~ xi_z",
      abs(cl_iso['xi_x'] - cl_iso['xi_y']) < 0.05 and abs(cl_iso['xi_y'] - cl_iso['xi_z']) < 0.05,
      f"xi=({cl_iso['xi_x']:.3f},{cl_iso['xi_y']:.3f},{cl_iso['xi_z']:.3f})")
check("x-only xi_y,xi_z >> xi_x",
      cl_x['xi_y'] > 2 * cl_x['xi_x'] and cl_x['xi_z'] > 2 * cl_x['xi_x'],
      f"xi=({cl_x['xi_x']:.3f},{cl_x['xi_y']:.3f},{cl_x['xi_z']:.3f})")

# --- T11: Minkowski functionals ---
print("\n--- T11: Minkowski functionals ---")
mf = minkowski_functionals_3d(rho_gauss, hx, hy, hz, threshold=0.55)
check("V > 0", mf['V'] > 0, f"V={mf['V']:.4e}")
check("S > 0", mf['S'] > 0, f"S={mf['S']:.4e}")
check("chi is integer", isinstance(mf['chi'], (int, np.integer)), f"chi={mf['chi']}")

# --- T12: Structure functions ---
print("\n--- T12: Structure functions ---")
sf = structure_functions_3d(rho_gauss, hx, hy, hz, orders=[2])
check("S_2 increases", sf[2][-1] > sf[2][0], f"S_2[0]={sf[2][0]:.4e}, S_2[-1]={sf[2][-1]:.4e}")

# --- T13: Horizon ---
print("\n--- T13: Horizon detector ---")
rho_near = rho_star + 0.48 * np.exp(-((X-0.5)**2 + (Y-0.5)**2 + (Z-0.5)**2) / 0.02)
rho_near = np.clip(rho_near, 1e-12, 0.999999)
hz_det = horizon_detector_3d(rho_near, params)
check("Near-max high proximity", hz_det['max_proximity'] > 0.9,
      f"prox={hz_det['max_proximity']:.4f}")
hz_norm = horizon_detector_3d(rho_iso, params)
check("Normal low proximity", hz_norm['max_proximity'] < 0.5,
      f"prox={hz_norm['max_proximity']:.4f}")

# --- T14: Full dispatcher ---
print("\n--- T14: Full compute_invariants_3d ---")
from edsim_solver_3d import operator_F_fd_3d, spatial_avg_3d
F_rho = operator_F_fd_3d(rho_iso, params)
F_bar = spatial_avg_3d(F_rho, hx, hy, hz)
inv = compute_invariants_3d(rho_iso, 0.0, F_bar, params)
check("Has spectral", 'spectral' in inv)
check("Has geometric", 'geometric' in inv)
check("Has dynamical", 'dynamical' in inv)
check("Has structure_functions", 'structure_functions' in inv)

# --- T15: Evolved field ---
print("\n--- T15: Evolved field ---")
p15 = EDParameters3D(Nx=12, Ny=12, Nz=12, dt=1e-3, T=0.05, method='etdrk4', k_out=50)
state = initialize_state_3d(p15, perturbation='cosine', amplitude=0.03)
for _ in range(50):
    state = step_3d(state, p15)
F_r = operator_F_fd_3d(state['rho'], p15)
F_b = spatial_avg_3d(F_r, p15.hx, p15.hy, p15.hz)
inv_f = compute_invariants_3d(state['rho'], state['v'], F_b, p15)
H_f = inv_f['spectral']['spectral_entropy']
C_f = inv_f['dynamical']['ed_complexity']
dr_f = inv_f['dynamical']['dissipation_ratios']
check("Evolved entropy finite", 0 <= H_f < 30, f"H={H_f:.4f}")
check("Evolved complexity > 0", C_f > 0, f"C={C_f:.6e}")
check("Ratios sum ~1", abs(dr_f['R_grad']+dr_f['R_pen']+dr_f['R_part']-1)<0.01,
      f"sum={dr_f['R_grad']+dr_f['R_pen']+dr_f['R_part']:.6f}")

print("\n" + "=" * 70)
print(f"  RESULTS: {n_pass} PASS, {n_fail} FAIL out of {n_pass + n_fail}")
print("=" * 70)
