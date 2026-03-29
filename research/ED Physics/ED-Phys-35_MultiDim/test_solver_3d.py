"""Validation tests for edsim_solver_3d.py"""
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edsim_solver_3d import *

print("=" * 70)
print("  EDSIM_SOLVER_3D VALIDATION TESTS")
print("=" * 70)

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

# --- T1: DCT roundtrip ---
print("\n--- T1: DCT-I roundtrip (3D) ---")
p = EDParameters3D(Nx=16, Ny=16, Nz=16, dt=1e-3)
spec = SpectralState3D(p)
x = np.linspace(0, 1, spec.Npx)
y = np.linspace(0, 1, spec.Npy)
z = np.linspace(0, 1, spec.Npz)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
u = 0.05 * np.cos(np.pi*X) * np.cos(np.pi*Y) * np.cos(np.pi*Z)
u_hat = spec.to_spectral(u)
u_back = spec.to_physical(u_hat, spec.Npx, spec.Npy, spec.Npz)
err = np.max(np.abs(u_back - u))
check("DCT roundtrip", err < 1e-12, f"err={err:.2e}")

# Constant roundtrip
u_const = 0.03 * np.ones((spec.Npx, spec.Npy, spec.Npz))
err_c = np.max(np.abs(spec.to_physical(spec.to_spectral(u_const),
                                        spec.Npx, spec.Npy, spec.Npz) - u_const))
check("Constant roundtrip", err_c < 1e-12, f"err={err_c:.2e}")

# --- T2: FD operators on constant ---
print("\n--- T2: FD operators on constant field ---")
rho_c = np.full((16, 16, 16), 0.5)
lap_c = laplacian_fd_3d(rho_c, p.hx, p.hy, p.hz, 'neumann')
gs_c = grad_squared_fd_3d(rho_c, p.hx, p.hy, p.hz, 'neumann')
check("Lap(const)=0", np.max(np.abs(lap_c)) < 1e-14, f"max={np.max(np.abs(lap_c)):.2e}")
check("|grad(const)|^2=0", np.max(np.abs(gs_c)) < 1e-14, f"max={np.max(np.abs(gs_c)):.2e}")

# --- T3: FD Laplacian accuracy ---
print("\n--- T3: FD Laplacian accuracy ---")
N = 32
p3 = EDParameters3D(Nx=N, Ny=N, Nz=N)
x = np.linspace(0, 1, N); y = np.linspace(0, 1, N); z = np.linspace(0, 1, N)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
f = np.cos(np.pi*X) * np.cos(np.pi*Y) * np.cos(np.pi*Z)
lap_f = laplacian_fd_3d(f, p3.hx, p3.hy, p3.hz, 'neumann')
exact = -3 * np.pi**2 * f
# Interior only (avoid boundary)
err_lap = np.max(np.abs(lap_f[3:-3, 3:-3, 3:-3] - exact[3:-3, 3:-3, 3:-3]))
h = 1.0 / (N - 1)
check("Lap O(h^2)", err_lap < 2.0, f"err={err_lap:.4e}, h^2={h**2:.4e}")

# --- T4: Uniform IC stays uniform (ETD) ---
print("\n--- T4: Uniform stays uniform ---")
p4 = EDParameters3D(Nx=12, Ny=12, Nz=12, dt=1e-3, T=0.01, method='etdrk4', k_out=10)
state = initialize_state_3d(p4, perturbation='uniform')
for _ in range(10):
    state = step_3d(state, p4)
dev = np.max(np.abs(state['rho'] - 0.5))
check("Uniform ETD", dev < 1e-13, f"dev={dev:.2e}")

p4c = EDParameters3D(Nx=12, Ny=12, Nz=12, dt=1e-3, T=0.01, method='crank_nicolson', k_out=10)
state_c = initialize_state_3d(p4c, perturbation='uniform')
for _ in range(10):
    state_c = step_3d(state_c, p4c)
dev_c = np.max(np.abs(state_c['rho'] - 0.5))
check("Uniform CN", dev_c < 1e-13, f"dev={dev_c:.2e}")

# --- T5: z-invariant IC preserves symmetry ---
print("\n--- T5: z-invariant IC ---")
N5 = 16
p5 = EDParameters3D(Nx=N5, Ny=N5, Nz=N5, dt=5e-4, T=0.01, method='crank_nicolson', k_out=20)
x5 = np.linspace(0, 1, N5); y5 = np.linspace(0, 1, N5); z5 = np.linspace(0, 1, N5)
X5, Y5, Z5 = np.meshgrid(x5, y5, z5, indexing='ij')
rho5 = 0.5 + 0.02 * np.cos(np.pi * X5) * np.cos(np.pi * Y5)
state5 = initialize_state_3d(p5, rho_init=rho5)
for _ in range(20):
    state5 = step_3d(state5, p5)
z_std = np.max(np.std(state5['rho'], axis=2))
check("z-uniformity", z_std < 1e-14, f"max_z_std={z_std:.2e}")

# --- T6: Energy monotonicity ---
print("\n--- T6: Energy monotonicity ---")
p6 = EDParameters3D(Nx=16, Ny=16, Nz=16, dt=1e-3, T=0.1, method='etdrk4', k_out=10)
state6 = initialize_state_3d(p6, perturbation='gaussian', amplitude=0.05)
Es = [energy_3d(state6['rho'], state6['v'], p6)['total']]
for n in range(100):
    state6 = step_3d(state6, p6)
    if (n + 1) % 10 == 0:
        Es.append(energy_3d(state6['rho'], state6['v'], p6)['total'])
dE = np.diff(Es)
n_inc = int(np.sum(dE > 1e-15))
check("Energy monotone ETD", n_inc == 0, f"increases={n_inc}/{len(dE)}")

p6c = EDParameters3D(Nx=16, Ny=16, Nz=16, dt=1e-3, T=0.1, method='crank_nicolson', k_out=10)
state6c = initialize_state_3d(p6c, perturbation='gaussian', amplitude=0.05)
Es_c = [energy_3d(state6c['rho'], state6c['v'], p6c)['total']]
for n in range(100):
    state6c = step_3d(state6c, p6c)
    if (n + 1) % 10 == 0:
        Es_c.append(energy_3d(state6c['rho'], state6c['v'], p6c)['total'])
dE_c = np.diff(Es_c)
n_inc_c = int(np.sum(dE_c > 1e-15))
check("Energy monotone CN", n_inc_c == 0, f"increases={n_inc_c}/{len(dE_c)}")

# --- T7: Cross-method agreement ---
print("\n--- T7: ETD vs CN cross-validation ---")
p7e = EDParameters3D(Nx=16, Ny=16, Nz=16, dt=5e-4, T=0.01, method='etdrk4', k_out=20)
p7c = EDParameters3D(Nx=16, Ny=16, Nz=16, dt=5e-4, T=0.01, method='crank_nicolson', k_out=20)
rho7 = 0.5 + 0.01 * np.cos(np.pi * X5) * np.cos(np.pi * Y5) * np.cos(np.pi * Z5)
se = initialize_state_3d(p7e, rho_init=rho7.copy())
sc = initialize_state_3d(p7c, rho_init=rho7.copy())
for _ in range(20):
    se = step_3d(se, p7e)
    sc = step_3d(sc, p7c)
diff = np.max(np.abs(se['rho'] - sc['rho']))
pert = np.max(np.abs(se['rho'] - 0.5))
rel = diff / max(pert, 1e-15)
check("ETD vs CN agreement", rel < 0.1, f"rel_diff={rel:.4e}")

# --- T8: Memory estimate ---
print("\n--- T8: Memory and performance ---")
p8 = EDParameters3D(Nx=64, Ny=64, Nz=64)
check("Memory estimate", p8.memory_estimate_mb() > 10, f"~{p8.memory_estimate_mb():.0f} MB")
print(f"  Grid points: {p8.n_points():,}")

# --- T9: run_simulation_3d ---
print("\n--- T9: Full run_simulation_3d ---")
t0 = time.time()
p9 = EDParameters3D(Nx=12, Ny=12, Nz=12, dt=1e-3, T=0.05, method='etdrk4', k_out=50)
res = run_simulation_3d(p9, perturbation='cosine', amplitude=0.03, verbose=False)
elapsed = time.time() - t0
check("run_simulation_3d completes", res['final_state']['t'] > 0.04,
      f"t_final={res['final_state']['t']:.4f}, {elapsed:.1f}s")
E0 = res['energy_history'][0]['total']
Ef = res['energy_history'][-1]['total']
check("Energy decays", Ef < E0, f"E_ratio={Ef/E0:.4f}")

# --- Summary ---
print("\n" + "=" * 70)
print(f"  RESULTS: {n_pass} PASS, {n_fail} FAIL out of {n_pass + n_fail}")
print("=" * 70)
