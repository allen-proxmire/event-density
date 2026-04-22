"""
v1.4 diagnostic script: reproduces the FPv2 §8.4 54% renormalization from
`edsim/phys/analogues/telegraph_pme.py`, identifies the specific bug (line 162
passes `params.D * F_local` to the participation ODE instead of F_local),
and demonstrates that patching the bug restores ω_measured = ω_linear.

The three sections below correspond to the three verification tests in the
v1.4 memo:

  1. Original code: ω-measurement at H ∈ {10, 20, 50} (reproduces FPv2 54%)
  2. Amplitude independence (A_ic ∈ [0.01, 0.4] all give same ω)
  3. Patched code: ω-measurement at H ∈ {10, 20, 50} (matches linear theory)

Run directly: `python3 diagnostic_runs.py`
"""

import numpy as np

from edsim.phys.analogues.telegraph_pme import (
    _make_params, _make_ic, _extract_oscillation,
    predict_telegraph_pme, run_telegraph_pme,
)
from edsim.core.constitutive import mobility, mobility_deriv, penalty, enforce_bounds
from edsim.core.operators import laplacian_fd_2d, grad_squared_fd_2d
from edsim.core.participation import advance_v, spatial_average


def _run_solver_patched(params, rho0, T, snap_interval):
    """Solver with the v1.4 patch: F_avg uses <F_local> without the spurious D factor."""
    rho = rho0.copy()
    v = 0.0
    t = 0.0
    dt = params.dt
    dx = (params.L[0] / params.N[0], params.L[1] / params.N[1])
    times, fields, v_hist = [0.0], [rho.copy()], [0.0]
    n_steps = int(np.ceil(T / dt))
    next_snap = snap_interval

    for _ in range(n_steps):
        rho_old = rho.copy()
        for _fp in range(12):
            lap = laplacian_fd_2d(rho, dx)
            gsq = grad_squared_fd_2d(rho, dx)
            M = mobility(rho, params)
            Mp = mobility_deriv(rho, params)
            P = penalty(rho, params)
            F_local = M * lap + Mp * gsq - P
            F_total = params.D * F_local + params.H * v
            rho_new = rho_old + dt * F_total
            rho_new = enforce_bounds(rho_new, params)
            if np.max(np.abs(rho_new - rho)) < 1e-8:
                rho = rho_new
                break
            rho = rho_new

        # PATCH: <F_local> without the D factor, matching FPv2 §2.1 spec
        F_avg = spatial_average(F_local, dx)
        v = advance_v(v, F_avg, params)
        t += dt
        if t >= next_snap - dt / 2:
            times.append(t)
            fields.append(rho.copy())
            v_hist.append(v)
            next_snap += snap_interval
    return dict(times=np.array(times), fields=fields, v=np.array(v_hist))


def measure_omega_patched(H, A_ic=0.05, sigma=0.25, T=100.0):
    params = _make_params(N=64, L=8.0, beta=1.0, P0=0.01, H=H, dt=0.005)
    ic = _make_ic(params, A=A_ic, sigma=sigma)
    result = _run_solver_patched(params, ic, T=T, snap_interval=T/200)
    cx_ix = params.N[0] // 2
    cd = np.array([params.rho_max - f[cx_ix, cx_ix] for f in result["fields"]])
    omega_d, _ = _extract_oscillation(result["times"], cd, t_min=T * 0.1)
    return omega_d


def test1_reproduce_54_percent():
    """Test 1: Original code reproduces FPv2 table values."""
    print("=" * 80)
    print("Test 1: Original code at H ∈ {10, 20, 50} (reproduces FPv2 54%)")
    print("=" * 80)
    print(f'{"H":>6} {"ω_linear":>10} {"ω_coded":>10} {"ω_meas":>10} {"ratio":>8} {"paper":>10}')
    print("-" * 80)
    paper_values = {10: 0.1662, 20: 0.2400, 50: 0.3842}
    for H in [10.0, 20.0, 50.0]:
        pred = predict_telegraph_pme(H=H, P0=0.01, beta=1.0)
        # Derived eigenmode from the buggy code
        gamma = (0.3 * 0.01 + 0.1) / 2
        omega_coded_sq = 0.3 * 0.01 * (0.1 + H) / 1.0 - gamma ** 2
        omega_coded = np.sqrt(max(omega_coded_sq, 0.0))
        # Measurement from original code
        res = run_telegraph_pme(H=H, P0=0.01, beta=1.0, N=64,
                                 T=100.0, n_snaps=200, dt=0.005, A_ic=0.05)
        print(f'{H:>6.1f} {pred.omega:>10.4f} {omega_coded:>10.4f} '
              f'{res.omega_density_fitted:>10.4f} '
              f'{res.omega_density_fitted/pred.omega:>8.3f} '
              f'{paper_values[H]:>10.4f}')
    print()


def test2_amplitude_independence():
    """Test 2: ω is independent of A_ic — confirms it's structural, not amplitude-driven."""
    print("=" * 80)
    print("Test 2: Amplitude independence at H=50 (original code)")
    print("=" * 80)
    print(f'{"A_ic":>8} {"ω_meas":>10} {"ratio":>8}')
    print("-" * 80)
    omega_linear = 0.7054
    for A_ic in [0.01, 0.05, 0.1, 0.2, 0.3, 0.4]:
        res = run_telegraph_pme(H=50.0, P0=0.01, beta=1.0, N=64,
                                 T=100.0, n_snaps=200, dt=0.005,
                                 A_ic=A_ic, sigma=0.25)
        print(f'{A_ic:>8.2f} {res.omega_density_fitted:>10.4f} '
              f'{res.omega_density_fitted/omega_linear:>8.3f}')
    print()


def test3_patch_restores_linear():
    """Test 3: Patched code (remove D factor) gives ω_measured = ω_linear."""
    print("=" * 80)
    print("Test 3: Patched code at H ∈ {10, 20, 50} (should give ω ≈ ω_linear)")
    print("=" * 80)
    print(f'{"H":>6} {"ω_linear":>10} {"ω_meas_patched":>16} {"ratio":>8}')
    print("-" * 80)
    for H in [10.0, 20.0, 50.0]:
        pred = predict_telegraph_pme(H=H, P0=0.01, beta=1.0)
        omega_patched = measure_omega_patched(H, A_ic=0.05)
        print(f'{H:>6.1f} {pred.omega:>10.4f} {omega_patched:>16.4f} '
              f'{omega_patched/pred.omega:>8.3f}')
    print()


if __name__ == "__main__":
    test1_reproduce_54_percent()
    test2_amplitude_independence()
    test3_patch_restores_linear()
    print("=" * 80)
    print("v1.4 CONCLUSION:")
    print("  The 54% renormalization in FPv2 §8.4 is caused by line 162 of")
    print("  `edsim/phys/analogues/telegraph_pme.py`:")
    print('      F_avg = spatial_average(params.D * F_local, dx)  ← BUG')
    print("  The extra D factor shifts the off-diagonal coupling in the 2D")
    print("  uniform-mode matrix from P_0/τ (paper convention) to D·P_0/τ,")
    print("  producing the observed ratio √D ≈ 0.548 in the large-H limit.")
    print("  Patch: remove `params.D *` — makes ω_measured ≈ ω_linear.")
    print("=" * 80)
