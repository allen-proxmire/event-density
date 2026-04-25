"""
phase3_validation.py
====================
Phase 3 validation suite for the 2D ED solver.

Runs all tests and prints structured results for the validation report.
"""

import numpy as np
import time
import sys
import os
import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edsim_solver_2d import *


def make_cosine_ic(Nx, Ny, Lx, Ly, rho_star, amplitude):
    """Smooth reproducible IC: rho_star + A * cos(pi x/Lx) * cos(pi y/Ly)."""
    x = np.linspace(0, Lx, Nx)
    y = np.linspace(0, Ly, Ny)
    X, Y = np.meshgrid(x, y, indexing='ij')
    return rho_star + amplitude * np.cos(np.pi * X / Lx) * np.cos(np.pi * Y / Ly)


def interpolate_to_grid(rho, Nx_src, Ny_src, Nx_dst, Ny_dst, Lx, Ly):
    """Interpolate rho from one grid to another."""
    from scipy.interpolate import RegularGridInterpolator
    x_src = np.linspace(0, Lx, Nx_src)
    y_src = np.linspace(0, Ly, Ny_src)
    interp = RegularGridInterpolator((x_src, y_src), rho, method='cubic')
    x_dst = np.linspace(0, Lx, Nx_dst)
    y_dst = np.linspace(0, Ly, Ny_dst)
    Xd, Yd = np.meshgrid(x_dst, y_dst, indexing='ij')
    pts = np.column_stack([Xd.ravel(), Yd.ravel()])
    return interp(pts).reshape(Nx_dst, Ny_dst)


def run_to_time(params, rho_init, T_target):
    """Run solver and return final rho."""
    state = initialize_state_2d(params, rho_init=rho_init)
    n_steps = int(round(T_target / params.dt))
    for _ in range(n_steps):
        state = step_2d(state, params)
    return state['rho'], state['v']


# ======================================================================
print("=" * 72)
print("  ED 2D SOLVER — PHASE 3 VALIDATION SUITE")
print("=" * 72)


# ======================================================================
# TEST 1: SPATIAL CONVERGENCE (CN-FD)
# ======================================================================
print("\n" + "=" * 72)
print("  TEST 1: SPATIAL CONVERGENCE (Crank-Nicolson FD)")
print("=" * 72)

T_conv = 0.05
dt_conv = 2.5e-5  # small dt to minimize temporal error
amp = 0.02
Lx, Ly = 1.0, 1.0
rho_star = 0.5

# Reference run at N=384
N_ref = 384
print(f"  Reference run: N={N_ref}, dt={dt_conv}")
t0 = time.time()
p_ref = EDParameters2D(Nx=N_ref, Ny=N_ref, Lx=Lx, Ly=Ly, dt=dt_conv, T=T_conv,
                       method='crank_nicolson', k_out=999999)
rho_ref_init = make_cosine_ic(N_ref, N_ref, Lx, Ly, rho_star, amp)
rho_ref, v_ref = run_to_time(p_ref, rho_ref_init, T_conv)
print(f"  Reference done in {time.time()-t0:.1f}s")

Ns_spatial = [32, 48, 64, 96, 128, 192]
spatial_results_cn = []

for N in Ns_spatial:
    p = EDParameters2D(Nx=N, Ny=N, Lx=Lx, Ly=Ly, dt=dt_conv, T=T_conv,
                       method='crank_nicolson', k_out=999999)
    rho_init = make_cosine_ic(N, N, Lx, Ly, rho_star, amp)
    t0 = time.time()
    rho_f, v_f = run_to_time(p, rho_init, T_conv)
    elapsed = time.time() - t0

    # Interpolate reference to this grid for comparison
    rho_ref_on_grid = interpolate_to_grid(rho_ref, N_ref, N_ref, N, N, Lx, Ly)
    diff = rho_f - rho_ref_on_grid
    L2 = np.sqrt(np.mean(diff**2))
    Linf = np.max(np.abs(diff))
    h = Lx / (N - 1)
    spatial_results_cn.append((N, h, L2, Linf, elapsed))
    print(f"  N={N:>4d}  h={h:.4e}  L2={L2:.4e}  Linf={Linf:.4e}  ({elapsed:.1f}s)")

print("\n  Convergence rates (CN):")
for i in range(1, len(spatial_results_cn)):
    N1, h1, L2_1, Li_1, _ = spatial_results_cn[i-1]
    N2, h2, L2_2, Li_2, _ = spatial_results_cn[i]
    if L2_2 > 0 and L2_1 > 0:
        rate_L2 = np.log(L2_1 / L2_2) / np.log(h1 / h2)
        rate_Li = np.log(Li_1 / Li_2) / np.log(h1 / h2)
        print(f"    N={N1:>3d}->{N2:>3d}  L2 rate={rate_L2:.2f}  Linf rate={rate_Li:.2f}")


# ======================================================================
# TEST 2: SPATIAL CONVERGENCE (ETD-RK4)
# ======================================================================
print("\n" + "=" * 72)
print("  TEST 2: SPATIAL CONVERGENCE (ETD-RK4)")
print("=" * 72)

# For ETD, reference is its own high-N run
N_ref_etd = 256
dt_etd = 1e-4
print(f"  Reference run: N={N_ref_etd}, dt={dt_etd}")
t0 = time.time()
p_ref_e = EDParameters2D(Nx=N_ref_etd, Ny=N_ref_etd, Lx=Lx, Ly=Ly, dt=dt_etd,
                         T=T_conv, method='etdrk4', k_out=999999)
rho_ref_e_init = make_cosine_ic(N_ref_etd, N_ref_etd, Lx, Ly, rho_star, amp)
rho_ref_e, _ = run_to_time(p_ref_e, rho_ref_e_init, T_conv)
print(f"  Reference done in {time.time()-t0:.1f}s")

Ns_etd = [32, 48, 64, 96, 128]
spatial_results_etd = []

for N in Ns_etd:
    p = EDParameters2D(Nx=N, Ny=N, Lx=Lx, Ly=Ly, dt=dt_etd, T=T_conv,
                       method='etdrk4', k_out=999999)
    rho_init = make_cosine_ic(N, N, Lx, Ly, rho_star, amp)
    t0 = time.time()
    rho_f, _ = run_to_time(p, rho_init, T_conv)
    elapsed = time.time() - t0

    rho_ref_on_grid = interpolate_to_grid(rho_ref_e, N_ref_etd, N_ref_etd, N, N, Lx, Ly)
    diff = rho_f - rho_ref_on_grid
    L2 = np.sqrt(np.mean(diff**2))
    Linf = np.max(np.abs(diff))
    h = Lx / (N - 1)
    spatial_results_etd.append((N, h, L2, Linf, elapsed))
    print(f"  N={N:>4d}  h={h:.4e}  L2={L2:.4e}  Linf={Linf:.4e}  ({elapsed:.1f}s)")

print("\n  Convergence rates (ETD):")
for i in range(1, len(spatial_results_etd)):
    N1, h1, L2_1, Li_1, _ = spatial_results_etd[i-1]
    N2, h2, L2_2, Li_2, _ = spatial_results_etd[i]
    if L2_2 > 0 and L2_1 > 0:
        rate_L2 = np.log(L2_1 / L2_2) / np.log(h1 / h2)
        rate_Li = np.log(Li_1 / Li_2) / np.log(h1 / h2)
        print(f"    N={N1:>3d}->{N2:>3d}  L2 rate={rate_L2:.2f}  Linf rate={rate_Li:.2f}")


# ======================================================================
# TEST 3: TEMPORAL CONVERGENCE
# ======================================================================
print("\n" + "=" * 72)
print("  TEST 3: TEMPORAL CONVERGENCE")
print("=" * 72)

N_time = 64
T_time = 0.02

# Reference: very small dt
dt_ref_t = 1e-6
print(f"  Reference run: N={N_time}, dt={dt_ref_t}")
t0 = time.time()
p_tr = EDParameters2D(Nx=N_time, Ny=N_time, dt=dt_ref_t, T=T_time,
                      method='crank_nicolson', k_out=999999)
rho_t_init = make_cosine_ic(N_time, N_time, Lx, Ly, rho_star, amp)
rho_t_ref, _ = run_to_time(p_tr, rho_t_init, T_time)
print(f"  Reference done in {time.time()-t0:.1f}s")

dts_cn = [2e-3, 1e-3, 5e-4, 2.5e-4, 1.25e-4]
dts_etd = [2e-3, 1e-3, 5e-4, 2.5e-4, 1.25e-4]

print("\n  CN temporal convergence:")
temporal_cn = []
for dt_test in dts_cn:
    p = EDParameters2D(Nx=N_time, Ny=N_time, dt=dt_test, T=T_time,
                       method='crank_nicolson', k_out=999999)
    t0 = time.time()
    rho_f, _ = run_to_time(p, rho_t_init.copy(), T_time)
    elapsed = time.time() - t0
    diff = rho_f - rho_t_ref
    L2 = np.sqrt(np.mean(diff**2))
    Linf = np.max(np.abs(diff))
    temporal_cn.append((dt_test, L2, Linf, elapsed))
    print(f"    dt={dt_test:.4e}  L2={L2:.4e}  Linf={Linf:.4e}  ({elapsed:.1f}s)")

print("  CN temporal rates:")
for i in range(1, len(temporal_cn)):
    dt1, L2_1, _, _ = temporal_cn[i-1]
    dt2, L2_2, _, _ = temporal_cn[i]
    if L2_2 > 0 and L2_1 > 0:
        rate = np.log(L2_1 / L2_2) / np.log(dt1 / dt2)
        print(f"    dt {dt1:.1e}->{dt2:.1e}: rate={rate:.2f}")

# ETD temporal reference
print(f"\n  ETD reference: N={N_time}, dt=5e-6")
t0 = time.time()
p_tr_e = EDParameters2D(Nx=N_time, Ny=N_time, dt=5e-6, T=T_time,
                        method='etdrk4', k_out=999999)
rho_t_ref_e, _ = run_to_time(p_tr_e, rho_t_init.copy(), T_time)
print(f"  ETD reference done in {time.time()-t0:.1f}s")

print("\n  ETD temporal convergence:")
temporal_etd = []
for dt_test in dts_etd:
    p = EDParameters2D(Nx=N_time, Ny=N_time, dt=dt_test, T=T_time,
                       method='etdrk4', k_out=999999)
    t0 = time.time()
    rho_f, _ = run_to_time(p, rho_t_init.copy(), T_time)
    elapsed = time.time() - t0
    diff = rho_f - rho_t_ref_e
    L2 = np.sqrt(np.mean(diff**2))
    Linf = np.max(np.abs(diff))
    temporal_etd.append((dt_test, L2, Linf, elapsed))
    print(f"    dt={dt_test:.4e}  L2={L2:.4e}  Linf={Linf:.4e}  ({elapsed:.1f}s)")

print("  ETD temporal rates:")
for i in range(1, len(temporal_etd)):
    dt1, L2_1, _, _ = temporal_etd[i-1]
    dt2, L2_2, _, _ = temporal_etd[i]
    if L2_2 > 0 and L2_1 > 0:
        rate = np.log(L2_1 / L2_2) / np.log(dt1 / dt2)
        print(f"    dt {dt1:.1e}->{dt2:.1e}: rate={rate:.2f}")


# ======================================================================
# TEST 4: STABILITY LIMITS
# ======================================================================
print("\n" + "=" * 72)
print("  TEST 4: STABILITY LIMITS")
print("=" * 72)

N_stab = 32
T_stab = 0.1

def check_stable(method, N, dt, D_val=0.3, amp_val=0.02):
    """Run a few steps and check for NaN/Inf or huge values."""
    try:
        p = EDParameters2D(Nx=N, Ny=N, dt=dt, T=T_stab, method=method, D=D_val)
        rho_init = make_cosine_ic(N, N, Lx, Ly, rho_star, amp_val)
        state = initialize_state_2d(p, rho_init=rho_init)
        n_steps = min(int(T_stab / dt), 2000)
        for _ in range(n_steps):
            state = step_2d(state, p)
        rho = state['rho']
        if np.any(np.isnan(rho)) or np.any(np.isinf(rho)):
            return False, "NaN/Inf"
        if np.max(np.abs(rho)) > 100:
            return False, "blowup"
        return True, f"max={np.max(np.abs(rho - rho_star)):.4e}"
    except Exception as e:
        return False, str(e)[:50]

print("\n  4a. CN stability vs dt (N=32, D=0.3):")
for dt_test in [1e-2, 5e-3, 2e-3, 1e-3, 5e-4, 1e-4]:
    ok, msg = check_stable('crank_nicolson', N_stab, dt_test)
    print(f"    dt={dt_test:.1e}: {'STABLE' if ok else 'UNSTABLE'} ({msg})")

print("\n  4b. ETD stability vs dt (N=32, D=0.3):")
for dt_test in [1e-1, 5e-2, 1e-2, 5e-3, 1e-3, 5e-4]:
    ok, msg = check_stable('etdrk4', N_stab, dt_test)
    print(f"    dt={dt_test:.1e}: {'STABLE' if ok else 'UNSTABLE'} ({msg})")

print("\n  4c. Stiff regime: D=0.9 (CN, N=32):")
for dt_test in [5e-3, 1e-3, 5e-4, 1e-4]:
    ok, msg = check_stable('crank_nicolson', N_stab, dt_test, D_val=0.9)
    print(f"    dt={dt_test:.1e}: {'STABLE' if ok else 'UNSTABLE'} ({msg})")

print("\n  4d. Stiff regime: D=0.9 (ETD, N=32):")
for dt_test in [5e-2, 1e-2, 5e-3, 1e-3]:
    ok, msg = check_stable('etdrk4', N_stab, dt_test, D_val=0.9)
    print(f"    dt={dt_test:.1e}: {'STABLE' if ok else 'UNSTABLE'} ({msg})")

print("\n  4e. Near-singular: large amplitude (rho near 0 and rho_max):")
for amp_val in [0.1, 0.2, 0.3, 0.4, 0.45]:
    ok_cn, msg_cn = check_stable('crank_nicolson', N_stab, 1e-4, amp_val=amp_val)
    ok_etd, msg_etd = check_stable('etdrk4', N_stab, 1e-4, amp_val=amp_val)
    print(f"    amp={amp_val:.2f}: CN={'STABLE' if ok_cn else 'UNSTAB'} ETD={'STABLE' if ok_etd else 'UNSTAB'}")


# ======================================================================
# TEST 5: ENERGY & MASS DIAGNOSTICS
# ======================================================================
print("\n" + "=" * 72)
print("  TEST 5: ENERGY & MASS DIAGNOSTICS")
print("=" * 72)

N_diag = 64
T_diag = 1.0
dt_diag = 5e-4
sample_every = 20

for method_name in ['etdrk4', 'crank_nicolson']:
    print(f"\n  Method: {method_name}")
    p = EDParameters2D(Nx=N_diag, Ny=N_diag, dt=dt_diag, T=T_diag,
                       method=method_name, k_out=sample_every)
    rho_init = make_cosine_ic(N_diag, N_diag, Lx, Ly, rho_star, 0.05)
    state = initialize_state_2d(p, rho_init=rho_init)

    energies = [energy_2d(state['rho'], state['v'], p)['total']]
    masses = [total_mass_2d(state['rho'], p.hx, p.hy)]
    n_pos_total = 0
    n_cap_total = 0
    n_steps = int(T_diag / dt_diag)

    for n in range(1, n_steps + 1):
        state = step_2d(state, p)
        n_pos_total += state.get('n_pos', 0)
        n_cap_total += state.get('n_cap', 0)
        if n % sample_every == 0:
            energies.append(energy_2d(state['rho'], state['v'], p)['total'])
            masses.append(total_mass_2d(state['rho'], p.hx, p.hy))

    E_arr = np.array(energies)
    M_arr = np.array(masses)
    dE = np.diff(E_arr)

    n_E_increase = int(np.sum(dE > 1e-15))
    max_dE_rel = np.max(dE / np.abs(E_arr[:-1])) if len(E_arr) > 1 else 0
    mass_rel_change = abs(M_arr[-1] / M_arr[0] - 1)

    print(f"    E_0 = {E_arr[0]:.6e},  E_f = {E_arr[-1]:.6e}")
    print(f"    Energy increases: {n_E_increase} / {len(dE)} intervals")
    print(f"    Max relative dE: {max_dE_rel:.4e}")
    print(f"    Energy ratio E_f/E_0: {E_arr[-1]/E_arr[0]:.6f}")
    print(f"    Mass_0 = {M_arr[0]:.8e},  Mass_f = {M_arr[-1]:.8e}")
    print(f"    Mass relative change: {mass_rel_change:.4e}")
    print(f"    Positivity violations (total): {n_pos_total}")
    print(f"    Capacity violations (total): {n_cap_total}")
    print(f"    rho range: [{state['rho'].min():.8f}, {state['rho'].max():.8f}]")


# ======================================================================
# TEST 6: 1D REGRESSION (y-invariant IC in 2D vs 1D solver)
# ======================================================================
print("\n" + "=" * 72)
print("  TEST 6: 1D REGRESSION (y-invariant IC)")
print("=" * 72)

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', 'ED Simulation'))
try:
    from edsim_parameters import EDParameters, parameter_set_I
    from edsim_core import (step_crank_nicolson as step_cn_1d,
                            make_grid, laplacian_fd, grad_squared_fd,
                            spatial_avg_fd, advance_v as advance_v_1d,
                            enforce_bounds, operator_F_fd)
    have_1d = True
except ImportError:
    have_1d = False
    print("  WARNING: Could not import 1D solver. Skipping 1D regression.")

if have_1d:
    N_1d = 64
    T_1d = 0.05
    dt_1d = 5e-5

    # 1D run
    p1 = EDParameters(D=0.3, zeta=0.1, tau=1.0, rho_star=0.5, rho_max=1.0,
                      M0=1.0, beta=2.0, P0=1.0, N=N_1d-2, L=1.0, dt=dt_1d,
                      T=T_1d, method='crank_nicolson', k_out=999999)
    x_1d = make_grid(p1)
    rho_1d = p1.rho_star + 0.02 * np.cos(np.pi * x_1d / p1.L)
    v_1d = 0.0
    n_steps_1d = int(T_1d / dt_1d)
    for _ in range(n_steps_1d):
        rho_1d, v_1d, _ = step_cn_1d(rho_1d, v_1d, p1)
        rho_1d, _, _ = enforce_bounds(rho_1d, p1)

    # 2D run with y-invariant IC
    p2 = EDParameters2D(Nx=N_1d, Ny=N_1d, Lx=1.0, Ly=1.0, dt=dt_1d, T=T_1d,
                        method='crank_nicolson')
    x2d = np.linspace(0, 1.0, N_1d)
    y2d = np.linspace(0, 1.0, N_1d)
    X2, Y2 = np.meshgrid(x2d, y2d, indexing='ij')
    rho_2d_init = 0.5 + 0.02 * np.cos(np.pi * X2 / 1.0)
    rho_2d, v_2d = run_to_time(p2, rho_2d_init, T_1d)

    # Compare: extract center row of 2D (should match 1D)
    rho_2d_center = rho_2d[:, N_1d // 2]
    # Note: 1D grid has N+2 = N_1d points, same as 2D x-axis
    diff_1d = rho_2d_center - rho_1d
    L2_1d = np.sqrt(np.mean(diff_1d**2))
    Linf_1d = np.max(np.abs(diff_1d))

    # Also check y-uniformity
    y_std = np.max(np.std(rho_2d, axis=1))

    print(f"  1D grid points: {len(rho_1d)}, 2D grid: {N_1d}x{N_1d}")
    print(f"  L2(2D_row - 1D)  = {L2_1d:.4e}")
    print(f"  Linf(2D_row - 1D)= {Linf_1d:.4e}")
    print(f"  y-uniformity (max std across rows): {y_std:.4e}")
    print(f"  v_1D = {v_1d:.6e},  v_2D = {v_2d:.6e}")
    print(f"  v agreement: {abs(v_1d - v_2d):.4e}")

    # ETD cross-check
    print("\n  ETD 2D y-invariant vs CN 2D y-invariant:")
    p2e = EDParameters2D(Nx=N_1d, Ny=N_1d, Lx=1.0, Ly=1.0, dt=dt_1d, T=T_1d,
                         method='etdrk4')
    rho_2d_etd, v_2d_etd = run_to_time(p2e, rho_2d_init.copy(), T_1d)
    diff_methods = rho_2d_etd - rho_2d
    print(f"  L2(ETD - CN) = {np.sqrt(np.mean(diff_methods**2)):.4e}")
    print(f"  Linf(ETD - CN) = {np.max(np.abs(diff_methods)):.4e}")
    print(f"  ETD y-uniformity: {np.max(np.std(rho_2d_etd, axis=1)):.4e}")


# ======================================================================
# TEST 7: CROSS-METHOD AGREEMENT ON LONGER RUN
# ======================================================================
print("\n" + "=" * 72)
print("  TEST 7: ETD vs CN CROSS-VALIDATION (longer run)")
print("=" * 72)

N_cross = 48
T_cross = 0.5
dt_cross = 2e-4
rho_cross_init = make_cosine_ic(N_cross, N_cross, Lx, Ly, rho_star, 0.05)

p_etd = EDParameters2D(Nx=N_cross, Ny=N_cross, dt=dt_cross, T=T_cross, method='etdrk4')
p_cn = EDParameters2D(Nx=N_cross, Ny=N_cross, dt=dt_cross, T=T_cross, method='crank_nicolson')

t0 = time.time()
rho_etd_f, v_etd_f = run_to_time(p_etd, rho_cross_init.copy(), T_cross)
t_etd = time.time() - t0

t0 = time.time()
rho_cn_f, v_cn_f = run_to_time(p_cn, rho_cross_init.copy(), T_cross)
t_cn = time.time() - t0

diff = rho_etd_f - rho_cn_f
pert = np.max(np.abs(rho_etd_f - rho_star))
L2_cross = np.sqrt(np.mean(diff**2))
Linf_cross = np.max(np.abs(diff))
print(f"  ETD time: {t_etd:.1f}s, CN time: {t_cn:.1f}s")
print(f"  L2(ETD - CN)  = {L2_cross:.4e}")
print(f"  Linf(ETD - CN) = {Linf_cross:.4e}")
print(f"  Relative to perturbation: {Linf_cross/pert:.4e}")
print(f"  v_ETD = {v_etd_f:.6e},  v_CN = {v_cn_f:.6e}")


# ======================================================================
print("\n" + "=" * 72)
print("  VALIDATION SUITE COMPLETE")
print("=" * 72)
