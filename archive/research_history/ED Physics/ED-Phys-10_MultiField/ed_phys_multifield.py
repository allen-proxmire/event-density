"""
ED-Phys-10: Multi-Field ED Simulator
=======================================
Introduces a second scalar field φ(x,t) coupled to ρ(x,t).

Selected coupling: Gradient-Mediated Force (GMF)

The coupled PDE system:

    dρ/dt = M(ρ)·∇²ρ + M'(ρ)·|∇ρ|² − α·γ·ρ^(γ−1) − λ·∇·(ρ·∇φ)
    dφ/dt = D_φ·∇²φ − μ·φ + κ·(ρ − ρ̄)

Physics:
  - φ is sourced by density perturbations (κ·(ρ−ρ̄))
  - φ decays with rate μ (finite range)
  - φ diffuses with coefficient D_φ (propagation)
  - φ exerts a force on ρ via −λ·∇·(ρ·∇φ) (density-weighted gradient coupling)
  - The force term moves ρ along gradients of φ: overdense regions create
    a φ potential well, and other density flows toward it = ATTRACTION

Key design:
  - φ has its OWN mobility (D_φ), independent of M(ρ)
  - φ is NOT frozen at horizons (D_φ does not vanish at ρ_max)
  - φ can therefore mediate forces across horizon boundaries
  - The coupling −λ·∇·(ρ·∇φ) is a conservative force (divergence form)

Canonical sources: ED-5, ED-12, ED-12.5, ED-Phys-01 through ED-Phys-09.
"""

import sys
import os
import io
import time
import json
import numpy as np

# Force UTF-8 output on Windows to handle Greek letters in print statements
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
if sys.stderr.encoding != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ED-Phys-02_Simulator'))

from ed_phys_config import EDParams
from ed_phys_operators import (
    discrete_laplacian,
    discrete_grad_squared,
    discrete_grad_magnitude,
    mobility,
    mobility_derivative,
)


# ============================================================
# Multi-field simulator
# ============================================================

def simulate_multifield(
    params: EDParams,
    initial_rho: np.ndarray,
    initial_phi: np.ndarray = None,
    D_phi: float = 1.0,
    mu: float = 0.1,
    kappa: float = 0.01,
    lam: float = 0.01,
    snapshot_interval: int = 500,
) -> dict:
    """Simulate the coupled (ρ, φ) multi-field system.

    Parameters
    ----------
    params : EDParams
        Parameters for the ρ field (canonical).
    initial_rho : np.ndarray
        Initial density field.
    initial_phi : np.ndarray or None
        Initial mediator field. If None, starts at zero.
    D_phi : float
        Diffusion coefficient for φ.
    mu : float
        Decay rate for φ (sets effective range: L_φ ~ sqrt(D_φ/μ)).
    kappa : float
        Source coupling: φ is sourced by density perturbations.
    lam : float
        Force coupling: ρ is pushed by gradients of φ.
    snapshot_interval : int

    Returns
    -------
    dict with rho_final, phi_final, snapshots, diagnostics
    """
    rho = initial_rho.astype(np.float64).copy()
    if initial_phi is not None:
        phi = initial_phi.astype(np.float64).copy()
    else:
        phi = np.zeros_like(rho)

    alpha = params.alpha
    gamma_exp = params.gamma_exp
    M_0 = params.M_0
    rho_max_param = params.rho_max
    n_mob = params.n_mob
    eta = params.eta
    dx = params.dx
    eps = params.eps
    boundary = params.boundary
    rho_min_abs = params.rho_min_absorbing

    # Compute mean rho for source term
    rho_bar = float(np.mean(rho))

    # Stability: additional CFL from phi diffusion and coupling
    eta_phi = 0.1 * dx ** 2 / (2 * max(params.dimensions, 1) * max(D_phi, 1e-10))
    eta_coupling = 0.05 * dx / max(lam * float(np.max(rho)) * 0.1, 1e-10)
    eta = min(eta, eta_phi, eta_coupling)

    snapshots_rho = []
    snapshots_phi = []
    diagnostics = []

    for t in range(params.n_steps):
        # --- ρ field: canonical terms ---
        lap_rho = discrete_laplacian(rho, dx, boundary, rho_min_abs)
        grad_sq_rho = discrete_grad_squared(rho, dx, boundary, rho_min_abs)
        M = mobility(rho, M_0, rho_max_param, n_mob)
        M_prime = mobility_derivative(rho, M_0, rho_max_param, n_mob)
        rho_safe = np.maximum(rho, eps)
        rel_penalty = alpha * gamma_exp * rho_safe ** (gamma_exp - 1.0)

        RHS_rho_canonical = M * lap_rho + M_prime * grad_sq_rho - rel_penalty

        # --- φ field operators ---
        lap_phi = discrete_laplacian(phi, dx, boundary, rho_min_abs)

        # Source term: κ·(ρ − ρ̄)
        phi_source = kappa * (rho - rho_bar)

        # φ update: dφ/dt = D_φ·∇²φ − μ·φ + κ·(ρ − ρ̄)
        RHS_phi = D_phi * lap_phi - mu * phi + phi_source

        # --- Force term: −λ·∇·(ρ·∇φ) on ρ ---
        # ∇·(ρ·∇φ) = ρ·∇²φ + ∇ρ·∇φ
        # We compute ∇ρ·∇φ via central differences
        force_term = _compute_force_term(rho, phi, dx, boundary, rho_min_abs, lap_phi)

        RHS_rho = RHS_rho_canonical - lam * force_term

        # --- Update both fields ---
        rho = rho + eta * RHS_rho
        phi = phi + eta * RHS_phi

        # Positivity for rho
        np.clip(rho, 0.0, None, out=rho)

        # Update running mean (slowly tracks)
        if t % 1000 == 0:
            rho_bar = float(np.mean(rho))

        # Record diagnostics
        if t % params.record_interval == 0:
            grad_mag_rho = np.sqrt(discrete_grad_squared(rho, dx, boundary, rho_min_abs))
            diag = {
                'step': t,
                'rho_mean': float(np.mean(rho)),
                'rho_max': float(np.max(rho)),
                'rho_min': float(np.min(rho)),
                'rho_std': float(np.std(rho)),
                'grad_mean': float(np.mean(grad_mag_rho)),
                'grad_max': float(np.max(grad_mag_rho)),
                'grad_energy': float(np.sum(grad_mag_rho ** 2)),
                'phi_mean': float(np.mean(phi)),
                'phi_max': float(np.max(phi)),
                'phi_min': float(np.min(phi)),
                'phi_std': float(np.std(phi)),
                'phi_rms': float(np.sqrt(np.mean(phi ** 2))),
                'force_rms': float(np.sqrt(np.mean(force_term ** 2))) * lam,
                'force_max': float(np.max(np.abs(force_term))) * lam,
                'n_peaks': _count_peaks(rho),
                'n_basins': _count_basins(rho),
                'horizon_frac': float(np.sum(rho > 0.9 * rho_max_param) / rho.size),
                'M_min': float(np.min(M)),
            }

            # Peak positions for interaction tracking
            if rho.ndim == 1:
                _, heights, positions = _detect_peaks_1d(rho)
                diag['peak_positions'] = positions
                diag['peak_heights'] = heights

            diagnostics.append(diag)

        # Store snapshots
        if snapshot_interval and t % snapshot_interval == 0:
            snapshots_rho.append(rho.copy())
            snapshots_phi.append(phi.copy())

        # Stability check
        if np.any(np.isnan(rho)) or np.any(np.isnan(phi)):
            print(f"  WARNING: NaN at step {t}, aborting")
            break
        if float(np.max(np.abs(rho))) > 10 * rho_max_param:
            print(f"  WARNING: ρ blowup at step {t}, aborting")
            break
        if float(np.max(np.abs(phi))) > 1e6:
            print(f"  WARNING: φ blowup at step {t}, aborting")
            break

    return {
        'rho_final': rho,
        'phi_final': phi,
        'snapshots_rho': snapshots_rho,
        'snapshots_phi': snapshots_phi,
        'diagnostics': diagnostics,
        'eta_used': eta,
        'params_multi': {'D_phi': D_phi, 'mu': mu, 'kappa': kappa, 'lam': lam},
        'final_step': min(t + 1, params.n_steps),
    }


def _compute_force_term(rho, phi, dx, boundary, rho_min_abs, lap_phi):
    """Compute ∇·(ρ·∇φ) = ρ·∇²φ + ∇ρ·∇φ."""
    # First term: ρ·∇²φ
    term1 = rho * lap_phi

    # Second term: ∇ρ·∇φ (dot product of gradients)
    if rho.ndim == 1:
        p_rho = np.pad(rho, 1, mode='wrap')
        p_phi = np.pad(phi, 1, mode='wrap')
        grad_rho_x = (p_rho[2:] - p_rho[:-2]) / (2.0 * dx)
        grad_phi_x = (p_phi[2:] - p_phi[:-2]) / (2.0 * dx)
        term2 = grad_rho_x * grad_phi_x
    else:
        p_rho = np.pad(rho, 1, mode='wrap')
        p_phi = np.pad(phi, 1, mode='wrap')
        # x-gradients
        grad_rho_x = (p_rho[2:, 1:-1] - p_rho[:-2, 1:-1]) / (2.0 * dx)
        grad_phi_x = (p_phi[2:, 1:-1] - p_phi[:-2, 1:-1]) / (2.0 * dx)
        # y-gradients
        grad_rho_y = (p_rho[1:-1, 2:] - p_rho[1:-1, :-2]) / (2.0 * dx)
        grad_phi_y = (p_phi[1:-1, 2:] - p_phi[1:-1, :-2]) / (2.0 * dx)
        term2 = grad_rho_x * grad_phi_x + grad_rho_y * grad_phi_y

    return term1 + term2


# ============================================================
# Helpers
# ============================================================

def _count_peaks(rho):
    if rho.ndim == 1:
        return _count_peaks_1d_count(rho)
    return _count_peaks_2d_count(rho)

def _count_basins(rho):
    if rho.ndim == 1:
        return _count_basins_1d(rho)
    return _count_basins_2d(rho)

def _count_peaks_1d_count(rho):
    N = len(rho)
    count = 0
    for i in range(N):
        if rho[i] > rho[(i-1)%N] and rho[i] > rho[(i+1)%N]:
            count += 1
    return count

def _count_peaks_2d_count(rho):
    padded = np.pad(rho, 1, mode='wrap')
    center = padded[1:-1, 1:-1]
    is_max = (
        (center > padded[:-2, 1:-1]) &
        (center > padded[2:, 1:-1]) &
        (center > padded[1:-1, :-2]) &
        (center > padded[1:-1, 2:])
    )
    return int(np.sum(is_max))

def _count_basins_1d(rho):
    N = len(rho)
    count = 0
    for i in range(N):
        if rho[i] < rho[(i-1)%N] and rho[i] < rho[(i+1)%N]:
            count += 1
    return count

def _count_basins_2d(rho):
    padded = np.pad(rho, 1, mode='wrap')
    center = padded[1:-1, 1:-1]
    is_min = (
        (center < padded[:-2, 1:-1]) &
        (center < padded[2:, 1:-1]) &
        (center < padded[1:-1, :-2]) &
        (center < padded[1:-1, 2:])
    )
    return int(np.sum(is_min))

def _detect_peaks_1d(rho):
    N = len(rho)
    peaks = []
    for i in range(N):
        if rho[i] > rho[(i-1)%N] and rho[i] > rho[(i+1)%N]:
            peaks.append((i, float(rho[i])))
    positions = [p[0] for p in peaks]
    heights = [p[1] for p in peaks]
    return len(peaks), heights, positions


# ============================================================
# IC generators
# ============================================================

def ic_two_bumps(params, rho_mean=50.0, bump_height=25.0, separation=0.3, seed=42):
    N = params.N
    if params.dimensions == 1:
        rho = np.full(N, rho_mean, dtype=np.float64)
        sigma = N * 0.03
        c1 = int(N * (0.5 - separation / 2))
        c2 = int(N * (0.5 + separation / 2))
        x = np.arange(N)
        rho += bump_height * np.exp(-0.5 * ((x - c1) / sigma) ** 2)
        rho += bump_height * np.exp(-0.5 * ((x - c2) / sigma) ** 2)
    else:
        rho = np.full((N, N), rho_mean, dtype=np.float64)
        sigma = N * 0.03
        c1x = int(N * (0.5 - separation / 2))
        c2x = int(N * (0.5 + separation / 2))
        cy = N // 2
        x, y = np.meshgrid(np.arange(N), np.arange(N), indexing='ij')
        rho += bump_height * np.exp(-0.5 * (((x-c1x)**2 + (y-cy)**2) / sigma**2))
        rho += bump_height * np.exp(-0.5 * (((x-c2x)**2 + (y-cy)**2) / sigma**2))
    np.clip(rho, 0.0, None, out=rho)
    return rho


def ic_gaussian_pulse(params, rho_mean=50.0, pulse_height=15.0, pulse_sigma=20.0):
    N = params.N
    if params.dimensions == 1:
        rho = np.full(N, rho_mean, dtype=np.float64)
        x = np.arange(N)
        rho += pulse_height * np.exp(-0.5 * ((x - N//2) / pulse_sigma) ** 2)
    else:
        rho = np.full((N, N), rho_mean, dtype=np.float64)
        x, y = np.meshgrid(np.arange(N), np.arange(N), indexing='ij')
        r2 = (x - N//2)**2 + (y - N//2)**2
        rho += pulse_height * np.exp(-0.5 * r2 / pulse_sigma**2)
    np.clip(rho, 0.0, None, out=rho)
    return rho


def ic_sinusoidal(params, rho_mean=50.0, amplitude=5.0, n_modes=3):
    N = params.N
    if params.dimensions == 1:
        x = np.arange(N, dtype=np.float64)
        rho = np.full(N, rho_mean, dtype=np.float64)
        for k in range(1, n_modes + 1):
            rho += amplitude / k * np.sin(2 * np.pi * k * x / N)
    else:
        x, y = np.meshgrid(np.arange(N), np.arange(N), indexing='ij')
        rho = np.full((N, N), rho_mean, dtype=np.float64)
        for k in range(1, n_modes + 1):
            rho += amplitude / k * np.sin(2 * np.pi * k * x / N)
            rho += amplitude / k * np.sin(2 * np.pi * k * y / N)
    np.clip(rho, 0.0, None, out=rho)
    return rho


# ============================================================
# Experiment suite
# ============================================================

def run_multifield_experiments(output_dir="results"):
    """Run all ED-Phys-10 multi-field experiments."""

    os.makedirs(output_dir, exist_ok=True)
    all_results = {}

    print("=" * 70)
    print("  ED-Phys-10: Multi-Field ED — Full Experiment Suite")
    print("=" * 70)
    t_total = time.time()

    # ========================================================
    # EXP 1: Wave Test — φ bump → wave propagation?
    # ========================================================
    print("\n>>> EXP 1: Wave Test — localized φ bump (1D, N=512)")
    exp1_results = []
    for kappa in [0.01, 0.05, 0.1]:
        for lam in [0.01, 0.05, 0.1]:
            for D_phi in [1.0, 5.0]:
                p = EDParams(
                    alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
                    dimensions=1, N=512, dx=1.0, cfl_safety=0.4,
                    n_steps=20000, record_interval=200, boundary="periodic",
                )
                rho_0 = np.full(512, 50.0, dtype=np.float64)
                # Initialize φ with a Gaussian bump
                x = np.arange(512)
                phi_0 = 10.0 * np.exp(-0.5 * ((x - 256) / 20.0) ** 2)

                label = f"wave_k{kappa}_l{lam}_D{D_phi}"
                print(f"  {label}...", end="", flush=True)
                t0 = time.time()

                result = simulate_multifield(
                    p, rho_0, initial_phi=phi_0,
                    D_phi=D_phi, mu=0.1, kappa=kappa, lam=lam,
                    snapshot_interval=500,
                )

                elapsed = time.time() - t0
                d = result['diagnostics']
                info = {
                    'kappa': kappa, 'lam': lam, 'D_phi': D_phi,
                    'eta_used': result['eta_used'],
                    'elapsed_s': elapsed,
                    'final_step': result['final_step'],
                }

                if d:
                    info['phi_rms_initial'] = d[0]['phi_rms']
                    info['phi_rms_final'] = d[-1]['phi_rms']
                    info['rho_std_initial'] = d[0]['rho_std']
                    info['rho_std_final'] = d[-1]['rho_std']
                    info['force_rms_final'] = d[-1]['force_rms']
                    info['n_peaks_initial'] = d[0]['n_peaks']
                    info['n_peaks_final'] = d[-1]['n_peaks']
                    info['rho_max_initial'] = d[0]['rho_max']
                    info['rho_max_final'] = d[-1]['rho_max']

                    # Check if φ spread or traveled
                    if result['snapshots_phi'] and len(result['snapshots_phi']) >= 3:
                        phi_0_snap = result['snapshots_phi'][0]
                        phi_mid = result['snapshots_phi'][len(result['snapshots_phi'])//2]
                        phi_f = result['snapshots_phi'][-1]
                        # Peak of phi: did it move?
                        phi_peak_0 = int(np.argmax(np.abs(phi_0_snap)))
                        phi_peak_f = int(np.argmax(np.abs(phi_f)))
                        info['phi_peak_moved'] = abs(phi_peak_f - phi_peak_0)
                        # Width of phi: did it spread?
                        info['phi_width_initial'] = float(np.sum(np.abs(phi_0_snap) > 0.1 * np.max(np.abs(phi_0_snap))))
                        info['phi_width_final'] = float(np.sum(np.abs(phi_f) > 0.1 * np.max(np.abs(phi_f)))) if np.max(np.abs(phi_f)) > 1e-10 else 0

                    # Check if ρ developed new structure
                    if result['snapshots_rho'] and len(result['snapshots_rho']) >= 2:
                        rho_f = result['snapshots_rho'][-1]
                        rho_perturbation = rho_f - 50.0  # deviation from background
                        info['rho_perturbation_max'] = float(np.max(np.abs(rho_perturbation)))

                exp1_results.append(info)
                print(f" done ({elapsed:.1f}s) "
                      f"φ_rms={info.get('phi_rms_final', 0):.4f} "
                      f"ρ_peaks={info.get('n_peaks_initial', 0)}->{info.get('n_peaks_final', 0)} "
                      f"F_rms={info.get('force_rms_final', 0):.6f}")

    all_results['exp1_wave'] = exp1_results

    # ========================================================
    # EXP 2: Force Test — two ρ peaks, φ mediates interaction
    # ========================================================
    print("\n>>> EXP 2: Force Test — two ρ peaks + φ mediator (1D, N=512)")
    exp2_results = []
    for kappa in [0.01, 0.05, 0.1]:
        for lam in [0.01, 0.05, 0.1]:
            p = EDParams(
                alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
                dimensions=1, N=512, dx=1.0, cfl_safety=0.4,
                n_steps=20000, record_interval=200, boundary="periodic",
            )
            rho_0 = ic_two_bumps(p, rho_mean=50.0, bump_height=25.0, separation=0.3)
            # φ starts at zero — will be sourced by ρ peaks

            label = f"force_k{kappa}_l{lam}"
            print(f"  {label}...", end="", flush=True)
            t0 = time.time()

            result = simulate_multifield(
                p, rho_0, initial_phi=None,
                D_phi=2.0, mu=0.05, kappa=kappa, lam=lam,
                snapshot_interval=500,
            )

            elapsed = time.time() - t0
            d = result['diagnostics']
            info = {
                'kappa': kappa, 'lam': lam,
                'eta_used': result['eta_used'],
                'elapsed_s': elapsed,
                'final_step': result['final_step'],
            }

            if d:
                info['n_peaks_initial'] = d[0]['n_peaks']
                info['n_peaks_final'] = d[-1]['n_peaks']
                info['phi_rms_final'] = d[-1]['phi_rms']
                info['phi_max_final'] = d[-1]['phi_max']
                info['force_rms_final'] = d[-1]['force_rms']
                info['rho_std_initial'] = d[0]['rho_std']
                info['rho_std_final'] = d[-1]['rho_std']

                # Track peak positions
                pos_0 = d[0].get('peak_positions', [])
                pos_f = d[-1].get('peak_positions', [])
                if len(pos_0) >= 2 and len(pos_f) >= 2:
                    pos_0_s = sorted(pos_0)
                    pos_f_s = sorted(pos_f)
                    # Use two tallest
                    h_0 = d[0].get('peak_heights', [])
                    h_f = d[-1].get('peak_heights', [])
                    if len(h_0) >= 2:
                        idx_sorted = np.argsort(h_0)[-2:]
                        init_sep = abs(pos_0[idx_sorted[1]] - pos_0[idx_sorted[0]])
                    else:
                        init_sep = abs(pos_0_s[1] - pos_0_s[0])
                    if len(h_f) >= 2:
                        idx_sorted = np.argsort(h_f)[-2:]
                        final_sep = abs(pos_f[idx_sorted[1]] - pos_f[idx_sorted[0]])
                    else:
                        final_sep = abs(pos_f_s[1] - pos_f_s[0])
                    info['initial_peak_sep'] = int(init_sep)
                    info['final_peak_sep'] = int(final_sep)
                    info['sep_change'] = int(final_sep - init_sep)
                elif len(pos_f) < 2 and len(pos_0) >= 2:
                    info['peaks_merged'] = True
                    info['sep_change'] = -999

                # Track separation over time for dynamics
                sep_series = []
                for dd in d:
                    pp = dd.get('peak_positions', [])
                    hh = dd.get('peak_heights', [])
                    if len(pp) >= 2 and len(hh) >= 2:
                        idx_s = np.argsort(hh)[-2:]
                        sep_series.append(abs(pp[idx_s[1]] - pp[idx_s[0]]))
                    else:
                        sep_series.append(None)
                info['sep_series'] = sep_series

            exp2_results.append(info)
            sep_str = f"sep={info.get('initial_peak_sep', '?')}->{info.get('final_peak_sep', '?')}"
            print(f" done ({elapsed:.1f}s) "
                  f"peaks={info.get('n_peaks_initial', 0)}->{info.get('n_peaks_final', 0)} "
                  f"{sep_str} "
                  f"F_rms={info.get('force_rms_final', 0):.6f}")

    all_results['exp2_force'] = exp2_results

    # ========================================================
    # EXP 3: Anisotropy Test — directional gradients (2D)
    # ========================================================
    print("\n>>> EXP 3: Anisotropy Test — directional initial φ (2D, 128x128)")
    exp3_results = []
    for lam in [0.01, 0.05]:
        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=2, N=128, dx=1.0, cfl_safety=0.4,
            n_steps=10000, record_interval=200, boundary="periodic",
        )
        rng = np.random.default_rng(42)
        rho_0 = 50.0 + 5.0 * rng.standard_normal((128, 128))
        np.clip(rho_0, 0.0, None, out=rho_0)

        # Directional φ: gradient in x-direction
        x_grid = np.arange(128, dtype=np.float64)
        phi_0 = np.zeros((128, 128))
        phi_0[:, :] = 5.0 * np.sin(2 * np.pi * x_grid / 128)[np.newaxis, :]

        label = f"aniso_lam{lam}"
        print(f"  {label}...", end="", flush=True)
        t0 = time.time()

        result = simulate_multifield(
            p, rho_0, initial_phi=phi_0,
            D_phi=1.0, mu=0.05, kappa=0.05, lam=lam,
            snapshot_interval=1000,
        )

        elapsed = time.time() - t0
        d = result['diagnostics']
        info = {
            'lam': lam,
            'elapsed_s': elapsed,
            'final_step': result['final_step'],
        }

        if d:
            info['n_peaks_initial'] = d[0]['n_peaks']
            info['n_peaks_final'] = d[-1]['n_peaks']
            info['rho_std_initial'] = d[0]['rho_std']
            info['rho_std_final'] = d[-1]['rho_std']
            info['phi_rms_final'] = d[-1]['phi_rms']

            # Measure anisotropy: compare x-variance to y-variance of rho
            rho_f = result['rho_final']
            x_var = float(np.mean(np.var(rho_f, axis=0)))  # variance along x
            y_var = float(np.mean(np.var(rho_f, axis=1)))  # variance along y
            info['x_variance'] = x_var
            info['y_variance'] = y_var
            info['anisotropy_ratio'] = x_var / y_var if y_var > 0 else float('inf')

        exp3_results.append(info)
        print(f" done ({elapsed:.1f}s) "
              f"aniso_ratio={info.get('anisotropy_ratio', 0):.3f} "
              f"φ_rms={info.get('phi_rms_final', 0):.4f}")

        np.save(os.path.join(output_dir, f"2d_aniso_lam{lam}_rho.npy"), result['rho_final'])
        np.save(os.path.join(output_dir, f"2d_aniso_lam{lam}_phi.npy"), result['phi_final'])

    # Also run a control without φ coupling
    p = EDParams(
        alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
        dimensions=2, N=128, dx=1.0, cfl_safety=0.4,
        n_steps=10000, record_interval=200, boundary="periodic",
    )
    rng = np.random.default_rng(42)
    rho_0 = 50.0 + 5.0 * rng.standard_normal((128, 128))
    np.clip(rho_0, 0.0, None, out=rho_0)

    print(f"  aniso_control...", end="", flush=True)
    t0 = time.time()
    result = simulate_multifield(
        p, rho_0, initial_phi=None,
        D_phi=1.0, mu=0.05, kappa=0.0, lam=0.0,
        snapshot_interval=1000,
    )
    elapsed = time.time() - t0
    d = result['diagnostics']
    info_ctrl = {'lam': 0.0, 'elapsed_s': elapsed, 'final_step': result['final_step']}
    if d:
        rho_f = result['rho_final']
        x_var = float(np.mean(np.var(rho_f, axis=0)))
        y_var = float(np.mean(np.var(rho_f, axis=1)))
        info_ctrl['x_variance'] = x_var
        info_ctrl['y_variance'] = y_var
        info_ctrl['anisotropy_ratio'] = x_var / y_var if y_var > 0 else float('inf')
        info_ctrl['n_peaks_final'] = d[-1]['n_peaks']
        info_ctrl['rho_std_final'] = d[-1]['rho_std']
    exp3_results.append(info_ctrl)
    print(f" done ({elapsed:.1f}s) "
          f"aniso_ratio={info_ctrl.get('anisotropy_ratio', 0):.3f} (control)")

    all_results['exp3_anisotropy'] = exp3_results

    # ========================================================
    # EXP 4: Horizon Test — can φ cross M(ρ)=0 regions?
    # ========================================================
    print("\n>>> EXP 4: Horizon Test — φ crossing M(ρ)=0 regions (1D, N=512)")
    exp4_results = []
    for lam in [0.0, 0.01, 0.05]:
        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=1, N=512, dx=1.0, cfl_safety=0.4,
            n_steps=20000, record_interval=200, boundary="periodic",
        )
        # ρ with near-horizon bump
        rho_0 = np.full(512, 50.0, dtype=np.float64)
        x = np.arange(512)
        rho_0 += 45.0 * np.exp(-0.5 * ((x - 256) / 30.0) ** 2)  # peak at 95

        # φ bump on one side of the horizon
        phi_0 = 5.0 * np.exp(-0.5 * ((x - 180) / 15.0) ** 2)

        label = f"horizon_lam{lam}"
        print(f"  {label}...", end="", flush=True)
        t0 = time.time()

        result = simulate_multifield(
            p, rho_0, initial_phi=phi_0,
            D_phi=2.0, mu=0.05, kappa=0.01, lam=lam,
            snapshot_interval=500,
        )

        elapsed = time.time() - t0
        d = result['diagnostics']
        info = {'lam': lam, 'elapsed_s': elapsed, 'final_step': result['final_step']}

        if d:
            info['horizon_frac_initial'] = d[0]['horizon_frac']
            info['horizon_frac_final'] = d[-1]['horizon_frac']
            info['rho_max_initial'] = d[0]['rho_max']
            info['rho_max_final'] = d[-1]['rho_max']
            info['phi_rms_final'] = d[-1]['phi_rms']

            # Did φ penetrate past the horizon?
            phi_f = result['phi_final']
            # Horizon is centered at x=256; phi started at x=180 (left of horizon)
            # Check phi amplitude on the right side of horizon (x > 300)
            phi_right = float(np.mean(np.abs(phi_f[300:])))
            phi_left = float(np.mean(np.abs(phi_f[:200])))
            info['phi_left_of_horizon'] = phi_left
            info['phi_right_of_horizon'] = phi_right
            info['phi_crossed_horizon'] = phi_right > 0.01 * phi_left if phi_left > 1e-10 else False

        exp4_results.append(info)
        print(f" done ({elapsed:.1f}s) "
              f"φ_crossed={info.get('phi_crossed_horizon', False)} "
              f"φ_right={info.get('phi_right_of_horizon', 0):.4f}")

    all_results['exp4_horizon'] = exp4_results

    # ========================================================
    # EXP 5: Cosmology Test — full ρ+φ cosmological run
    # ========================================================
    print("\n>>> EXP 5: Cosmology Test — ρ+φ cosmological run (1D, N=512)")
    exp5_results = []
    for kappa in [0.0, 0.01, 0.05]:
        for lam in [0.0, 0.01, 0.05]:
            if kappa == 0 and lam == 0:
                pass  # include canonical baseline
            elif kappa == 0 or lam == 0:
                continue  # skip half-coupled runs (not interesting)

            p = EDParams(
                alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
                dimensions=1, N=512, dx=1.0, cfl_safety=0.4,
                n_steps=20000, record_interval=200, boundary="periodic",
            )
            rng = np.random.default_rng(42)
            rho_0 = 50.0 + 0.5 * rng.standard_normal(512)
            np.clip(rho_0, 0.0, None, out=rho_0)

            label = f"cosmo_k{kappa}_l{lam}"
            print(f"  {label}...", end="", flush=True)
            t0 = time.time()

            result = simulate_multifield(
                p, rho_0, initial_phi=None,
                D_phi=2.0, mu=0.1, kappa=kappa, lam=lam,
                snapshot_interval=500,
            )

            elapsed = time.time() - t0
            d = result['diagnostics']
            info = {
                'kappa': kappa, 'lam': lam,
                'eta_used': result['eta_used'],
                'elapsed_s': elapsed,
                'final_step': result['final_step'],
            }

            if d:
                info['rho_mean_initial'] = d[0]['rho_mean']
                info['rho_mean_final'] = d[-1]['rho_mean']
                info['grad_mean_initial'] = d[0]['grad_mean']
                info['grad_mean_final'] = d[-1]['grad_mean']
                info['n_basins_initial'] = d[0]['n_basins']
                info['n_basins_final'] = d[-1]['n_basins']
                info['phi_rms_final'] = d[-1]['phi_rms']
                info['rho_std_final'] = d[-1]['rho_std']

                # Fit inflation rate
                steps = np.array([dd['step'] for dd in d])
                grad_mean = np.array([dd['grad_mean'] for dd in d])
                phys_t = steps * result['eta_used']
                valid = grad_mean > 0
                if np.sum(valid) > 3:
                    log_G = np.log(grad_mean[valid])
                    t_v = phys_t[valid]
                    coeffs = np.polyfit(t_v, log_G, 1)
                    l1 = -coeffs[0]
                    resid = log_G - (coeffs[1] + coeffs[0] * t_v)
                    ss_r = np.sum(resid ** 2)
                    ss_t = np.sum((log_G - np.mean(log_G)) ** 2)
                    r2 = 1 - ss_r / ss_t if ss_t > 0 else 0
                    info['lambda_1'] = float(l1)
                    info['r_squared'] = float(r2)

            exp5_results.append(info)
            print(f" done ({elapsed:.1f}s) "
                  f"λ₁={info.get('lambda_1', 'N/A'):.4f} "
                  f"R²={info.get('r_squared', 'N/A'):.3f} "
                  f"basins={info.get('n_basins_initial', 0)}->{info.get('n_basins_final', 0)}")

    all_results['exp5_cosmology'] = exp5_results

    # ========================================================
    # EXP 6: 2D Cosmology with multi-field (128x128)
    # ========================================================
    print("\n>>> EXP 6: 2D Cosmology with multi-field (128x128)")
    exp6_results = []
    for lam in [0.0, 0.05]:
        kappa_val = 0.05 if lam > 0 else 0.0
        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=2, N=128, dx=1.0, cfl_safety=0.4,
            n_steps=10000, record_interval=200, boundary="periodic",
        )
        rng = np.random.default_rng(42)
        rho_0 = 50.0 + 5.0 * rng.standard_normal((128, 128))
        np.clip(rho_0, 0.0, None, out=rho_0)

        label = f"2d_cosmo_k{kappa_val}_l{lam}"
        print(f"  {label}...", end="", flush=True)
        t0 = time.time()

        result = simulate_multifield(
            p, rho_0, initial_phi=None,
            D_phi=2.0, mu=0.1, kappa=kappa_val, lam=lam,
            snapshot_interval=1000,
        )

        elapsed = time.time() - t0
        d = result['diagnostics']
        info = {'kappa': kappa_val, 'lam': lam, 'elapsed_s': elapsed,
                'final_step': result['final_step']}
        if d:
            info['n_peaks_initial'] = d[0]['n_peaks']
            info['n_peaks_final'] = d[-1]['n_peaks']
            info['n_basins_initial'] = d[0]['n_basins']
            info['n_basins_final'] = d[-1]['n_basins']
            info['rho_std_initial'] = d[0]['rho_std']
            info['rho_std_final'] = d[-1]['rho_std']
            info['phi_rms_final'] = d[-1]['phi_rms']

        exp6_results.append(info)
        print(f" done ({elapsed:.1f}s) "
              f"peaks={info.get('n_peaks_initial', 0)}->{info.get('n_peaks_final', 0)} "
              f"basins={info.get('n_basins_initial', 0)}->{info.get('n_basins_final', 0)}")

        np.save(os.path.join(output_dir, f"2d_cosmo_lam{lam}_rho.npy"), result['rho_final'])

    all_results['exp6_2d_cosmology'] = exp6_results

    # ========================================================
    # Save all results
    # ========================================================
    def make_serializable(obj):
        if isinstance(obj, dict):
            return {k: make_serializable(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [make_serializable(v) for v in obj]
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, (np.floating,)):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, tuple):
            return list(obj)
        if isinstance(obj, bool):
            return obj
        return obj

    results_path = os.path.join(output_dir, "multifield_results.json")
    with open(results_path, 'w') as f:
        json.dump(make_serializable(all_results), f, indent=2, default=str)

    elapsed_total = time.time() - t_total
    print(f"\n{'=' * 70}")
    print(f"  All multi-field experiments complete in {elapsed_total:.1f}s")
    print(f"  Results saved to {results_path}")
    print(f"{'=' * 70}")

    return all_results


if __name__ == "__main__":
    output_dir = os.path.join(os.path.dirname(__file__), "results")
    run_multifield_experiments(output_dir=output_dir)
