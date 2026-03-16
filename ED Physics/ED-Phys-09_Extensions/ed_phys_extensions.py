"""
ED-Phys-09: Extension Simulator
=================================
Implements two ED-consistent extensions to the canonical PDE:

Extension A — Inertial (Wave) Extension:
    tau * d²ρ/dt² + dρ/dt = M(ρ)·∇²ρ + M'(ρ)·|∇ρ|² − α·γ·ρ^(γ−1)

    Introduces a second time derivative with inertial timescale τ.
    At τ=0, recovers the canonical parabolic PDE.
    At τ>0, the PDE becomes hyperbolic-parabolic (damped wave equation).

Extension B — Nonlocal Kernel Extension:
    dρ/dt = ∇·[M(ρ)∇ρ] − α·γ·ρ^(γ−1) + σ·(K*ρ − ρ)

    Adds a nonlocal smoothing/coupling term where K is a Gaussian kernel
    with characteristic range R. The term σ·(K*ρ − ρ) computes the
    difference between the kernel-averaged density and local density,
    providing long-range coupling.

Both extensions preserve:
  - Non-negativity (positivity enforcement)
  - Compositionality (extensions modify how penalty terms combine)
  - Concave relational penalty (f(ρ)=ρ^γ unchanged)
  - Mobility function M(ρ) (horizon formation preserved)

Canonical sources: ED-5, ED-12, ED-12.5, ED-Phys-01 through ED-Phys-07.
"""

import sys
import os
import time
import json
import numpy as np

# Add simulator to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ED-Phys-02_Simulator'))

from ed_phys_config import EDParams
from ed_phys_operators import (
    discrete_laplacian,
    discrete_grad_squared,
    discrete_grad_magnitude,
    mobility,
    mobility_derivative,
)
from ed_phys_diagnostics import extract_time_series


# ============================================================
# Extension A: Inertial (Wave) Extension
# ============================================================

def simulate_inertial(
    params: EDParams,
    initial_rho: np.ndarray,
    tau: float = 1.0,
    snapshot_interval: int = 500,
    damping_ratio: float = 1.0,
) -> dict:
    """Simulate the inertial extension of the ED PDE.

    The modified PDE is:
        tau * d²ρ/dt² + damping_ratio * dρ/dt
            = M(ρ)·∇²ρ + M'(ρ)·|∇ρ|² − α·γ·ρ^(γ−1)

    We rewrite as a first-order system:
        dρ/dt = v
        dv/dt = (1/tau) * [RHS - damping_ratio * v]

    where RHS = M(ρ)·∇²ρ + M'(ρ)·|∇ρ|² − α·γ·ρ^(γ−1)

    Parameters
    ----------
    params : EDParams
    initial_rho : np.ndarray
    tau : float
        Inertial timescale. tau=0 gives canonical PDE. Higher tau = more wave-like.
    snapshot_interval : int
    damping_ratio : float
        Coefficient of first-order damping. At 1.0, recovers canonical damping.
        Lower values give more persistent oscillations.

    Returns
    -------
    dict with keys: rho_final, v_final, snapshots, diagnostics
    """
    rho = initial_rho.astype(np.float64).copy()
    v = np.zeros_like(rho)  # velocity field starts at zero

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

    # For the inertial system, we need a smaller timestep
    # CFL for wave equation: eta < dx / c_wave where c_wave ~ sqrt(M_0/tau)
    if tau > 0:
        c_wave = np.sqrt(M_0 / tau) if tau > 0 else M_0
        eta_wave = 0.1 * dx / c_wave
        eta = min(eta, eta_wave)

    snapshots = []
    diagnostics = []

    for t in range(params.n_steps):
        # Compute spatial operators
        lap = discrete_laplacian(rho, dx, boundary, rho_min_abs)
        grad_sq = discrete_grad_squared(rho, dx, boundary, rho_min_abs)
        M = mobility(rho, M_0, rho_max_param, n_mob)
        M_prime = mobility_derivative(rho, M_0, rho_max_param, n_mob)
        rho_safe = np.maximum(rho, eps)
        rel_penalty = alpha * gamma_exp * rho_safe ** (gamma_exp - 1.0)

        # RHS of the canonical PDE
        RHS = M * lap + M_prime * grad_sq - rel_penalty

        if tau > 0:
            # Inertial system: dv/dt = (1/tau) * (RHS - damping_ratio * v)
            dv = (1.0 / tau) * (RHS - damping_ratio * v)
            v = v + eta * dv
            rho = rho + eta * v
        else:
            # Canonical parabolic limit
            rho = rho + eta * RHS

        # Positivity enforcement
        np.clip(rho, 0.0, None, out=rho)

        # Record diagnostics
        if t % params.record_interval == 0:
            grad_mag = np.sqrt(discrete_grad_squared(rho, dx, boundary, rho_min_abs))
            diag = {
                'step': t,
                'rho_mean': float(np.mean(rho)),
                'rho_max': float(np.max(rho)),
                'rho_min': float(np.min(rho)),
                'rho_std': float(np.std(rho)),
                'grad_mean': float(np.mean(grad_mag)),
                'grad_max': float(np.max(grad_mag)),
                'grad_energy': float(np.sum(grad_mag ** 2)),
                'v_rms': float(np.sqrt(np.mean(v ** 2))) if tau > 0 else 0.0,
                'v_max': float(np.max(np.abs(v))) if tau > 0 else 0.0,
                'kinetic_energy': float(0.5 * tau * np.sum(v ** 2)) if tau > 0 else 0.0,
            }

            # Detect oscillatory behavior: sign changes in v
            if tau > 0 and rho.ndim == 1:
                v_sign_changes = int(np.sum(np.diff(np.sign(v)) != 0))
                diag['v_sign_changes'] = v_sign_changes

            # Peak detection
            if rho.ndim == 1:
                n_peaks = _count_peaks_1d(rho)
            else:
                n_peaks = _count_peaks_2d(rho)
            diag['n_peaks'] = n_peaks

            # Basin count
            if rho.ndim == 1:
                n_basins = _count_basins_1d(rho)
            else:
                n_basins = _count_basins_2d(rho)
            diag['n_basins'] = n_basins

            # Horizon fraction
            horizon_mask = rho > 0.9 * rho_max_param
            diag['horizon_frac'] = float(np.sum(horizon_mask) / rho.size)
            diag['M_min'] = float(np.min(mobility(rho, M_0, rho_max_param, n_mob)))

            diagnostics.append(diag)

        # Store snapshot
        if snapshot_interval and t % snapshot_interval == 0:
            snapshots.append(rho.copy())

        # Stability check
        if np.any(np.isnan(rho)) or np.any(np.isinf(rho)):
            print(f"  WARNING: NaN/Inf detected at step {t}, aborting")
            break
        if float(np.max(rho)) > 10 * rho_max_param:
            print(f"  WARNING: Blowup detected at step {t} (max_rho={np.max(rho):.1f}), aborting")
            break

    return {
        'rho_final': rho,
        'v_final': v if tau > 0 else None,
        'snapshots': snapshots,
        'diagnostics': diagnostics,
        'eta_used': eta,
        'tau': tau,
        'damping_ratio': damping_ratio,
        'final_step': t + 1 if t < params.n_steps else params.n_steps,
    }


# ============================================================
# Extension B: Nonlocal Kernel Extension
# ============================================================

def _build_gaussian_kernel_1d(N, R, dx=1.0):
    """Build a normalized Gaussian kernel for 1D periodic convolution.

    K(x) = (1/Z) * exp(-x²/(2R²))

    Returns kernel as 1D array of length N, centered at index 0 (for FFT use).
    """
    x = np.arange(N, dtype=np.float64)
    # Periodic distance
    x = np.minimum(x, N - x) * dx
    kernel = np.exp(-0.5 * (x / R) ** 2)
    kernel /= np.sum(kernel)  # normalize
    return kernel


def _build_gaussian_kernel_2d(N, R, dx=1.0):
    """Build a normalized Gaussian kernel for 2D periodic convolution."""
    x = np.arange(N, dtype=np.float64)
    x = np.minimum(x, N - x) * dx
    xx, yy = np.meshgrid(x, x, indexing='ij')
    r2 = xx ** 2 + yy ** 2
    kernel = np.exp(-0.5 * r2 / R ** 2)
    kernel /= np.sum(kernel)
    return kernel


def simulate_nonlocal(
    params: EDParams,
    initial_rho: np.ndarray,
    sigma_nl: float = 0.01,
    R_kernel: float = 50.0,
    snapshot_interval: int = 500,
) -> dict:
    """Simulate the nonlocal kernel extension of the ED PDE.

    The modified PDE is:
        dρ/dt = M(ρ)·∇²ρ + M'(ρ)·|∇ρ|² − α·γ·ρ^(γ−1) + σ·(K*ρ − ρ)

    where K is a Gaussian kernel with range R, and σ controls coupling strength.

    The term σ·(K*ρ − ρ) produces:
      - Attraction: overdense regions pull density from underdense regions
      - Long-range: coupling extends to distance ~R
      - Smoothing: at small R, approaches additional diffusion
      - Structure coupling: two peaks within range R interact

    Parameters
    ----------
    params : EDParams
    initial_rho : np.ndarray
    sigma_nl : float
        Nonlocal coupling strength.
    R_kernel : float
        Kernel range (in lattice units).
    snapshot_interval : int

    Returns
    -------
    dict with keys: rho_final, snapshots, diagnostics
    """
    rho = initial_rho.astype(np.float64).copy()

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

    # Build kernel in Fourier space for fast convolution
    N = params.N
    if rho.ndim == 1:
        kernel = _build_gaussian_kernel_1d(N, R_kernel, dx)
        kernel_fft = np.fft.rfft(kernel)
    else:
        kernel = _build_gaussian_kernel_2d(N, R_kernel, dx)
        kernel_fft = np.fft.rfft2(kernel)

    # Adjust timestep for nonlocal term stability
    eta_nl = 0.1 / max(sigma_nl, 1e-10)
    eta = min(eta, eta_nl)

    snapshots = []
    diagnostics = []

    for t in range(params.n_steps):
        # Compute local operators (canonical PDE)
        lap = discrete_laplacian(rho, dx, boundary, rho_min_abs)
        grad_sq = discrete_grad_squared(rho, dx, boundary, rho_min_abs)
        M = mobility(rho, M_0, rho_max_param, n_mob)
        M_prime = mobility_derivative(rho, M_0, rho_max_param, n_mob)
        rho_safe = np.maximum(rho, eps)
        rel_penalty = alpha * gamma_exp * rho_safe ** (gamma_exp - 1.0)

        # Canonical RHS
        RHS_local = M * lap + M_prime * grad_sq - rel_penalty

        # Nonlocal term: sigma * (K * rho - rho)
        if rho.ndim == 1:
            rho_fft = np.fft.rfft(rho)
            K_rho = np.fft.irfft(kernel_fft * rho_fft, n=N)
        else:
            rho_fft = np.fft.rfft2(rho)
            K_rho = np.fft.irfft2(kernel_fft * rho_fft, s=(N, N))

        nonlocal_term = sigma_nl * (K_rho - rho)

        # Combined update
        drho = RHS_local + nonlocal_term
        rho = rho + eta * drho

        # Positivity enforcement
        np.clip(rho, 0.0, None, out=rho)

        # Record diagnostics
        if t % params.record_interval == 0:
            grad_mag = np.sqrt(discrete_grad_squared(rho, dx, boundary, rho_min_abs))
            diag = {
                'step': t,
                'rho_mean': float(np.mean(rho)),
                'rho_max': float(np.max(rho)),
                'rho_min': float(np.min(rho)),
                'rho_std': float(np.std(rho)),
                'grad_mean': float(np.mean(grad_mag)),
                'grad_max': float(np.max(grad_mag)),
                'grad_energy': float(np.sum(grad_mag ** 2)),
                'nonlocal_rms': float(np.sqrt(np.mean(nonlocal_term ** 2))),
                'nonlocal_max': float(np.max(np.abs(nonlocal_term))),
            }

            # Peak detection
            if rho.ndim == 1:
                n_peaks = _count_peaks_1d(rho)
            else:
                n_peaks = _count_peaks_2d(rho)
            diag['n_peaks'] = n_peaks

            # Basin count
            if rho.ndim == 1:
                n_basins = _count_basins_1d(rho)
            else:
                n_basins = _count_basins_2d(rho)
            diag['n_basins'] = n_basins

            # Horizon fraction
            horizon_mask = rho > 0.9 * rho_max_param
            diag['horizon_frac'] = float(np.sum(horizon_mask) / rho.size)
            diag['M_min'] = float(np.min(mobility(rho, M_0, rho_max_param, n_mob)))

            diagnostics.append(diag)

        # Store snapshot
        if snapshot_interval and t % snapshot_interval == 0:
            snapshots.append(rho.copy())

        # Stability check
        if np.any(np.isnan(rho)) or np.any(np.isinf(rho)):
            print(f"  WARNING: NaN/Inf detected at step {t}, aborting")
            break
        if float(np.max(rho)) > 10 * rho_max_param:
            print(f"  WARNING: Blowup detected at step {t} (max_rho={np.max(rho):.1f}), aborting")
            break

    return {
        'rho_final': rho,
        'snapshots': snapshots,
        'diagnostics': diagnostics,
        'eta_used': eta,
        'sigma_nl': sigma_nl,
        'R_kernel': R_kernel,
        'final_step': t + 1 if t < params.n_steps else params.n_steps,
    }


# ============================================================
# Helper functions
# ============================================================

def _count_peaks_1d(rho):
    N = len(rho)
    count = 0
    for i in range(N):
        if rho[i] > rho[(i - 1) % N] and rho[i] > rho[(i + 1) % N]:
            count += 1
    return count


def _count_peaks_2d(rho):
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
        if rho[i] < rho[(i - 1) % N] and rho[i] < rho[(i + 1) % N]:
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
    """Find local maxima with positions and heights."""
    N = len(rho)
    peaks = []
    for i in range(N):
        if rho[i] > rho[(i - 1) % N] and rho[i] > rho[(i + 1) % N]:
            peaks.append((i, float(rho[i])))
    positions = [p[0] for p in peaks]
    heights = [p[1] for p in peaks]
    return len(peaks), heights, positions


# ============================================================
# IC generators (reused from ED-Phys-06 with additions)
# ============================================================

def ic_two_bumps(params, rho_mean=50.0, bump_height=25.0, separation=0.3, seed=42):
    """Two Gaussian bumps at configurable separation."""
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
        rho += bump_height * np.exp(-0.5 * (((x - c1x) ** 2 + (y - cy) ** 2) / sigma ** 2))
        rho += bump_height * np.exp(-0.5 * (((x - c2x) ** 2 + (y - cy) ** 2) / sigma ** 2))
    np.clip(rho, 0.0, None, out=rho)
    return rho


def ic_gaussian_pulse(params, rho_mean=50.0, pulse_height=15.0, pulse_sigma=20.0, seed=42):
    """Single narrow Gaussian pulse — good for wave propagation tests."""
    N = params.N
    if params.dimensions == 1:
        rho = np.full(N, rho_mean, dtype=np.float64)
        x = np.arange(N)
        rho += pulse_height * np.exp(-0.5 * ((x - N // 2) / pulse_sigma) ** 2)
    else:
        rho = np.full((N, N), rho_mean, dtype=np.float64)
        x, y = np.meshgrid(np.arange(N), np.arange(N), indexing='ij')
        r2 = (x - N // 2) ** 2 + (y - N // 2) ** 2
        rho += pulse_height * np.exp(-0.5 * r2 / pulse_sigma ** 2)
    np.clip(rho, 0.0, None, out=rho)
    return rho


def ic_sinusoidal(params, rho_mean=50.0, amplitude=5.0, n_modes=3):
    """Sinusoidal perturbation."""
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
# Experiment Suite
# ============================================================

def run_extension_experiments(output_dir="results"):
    """Run all ED-Phys-09 extension experiments."""

    os.makedirs(output_dir, exist_ok=True)
    all_results = {}

    print("=" * 70)
    print("  ED-Phys-09: Extensions — Full Experiment Suite")
    print("=" * 70)
    t_total = time.time()

    # ========================================================
    # EXTENSION A: Inertial (Wave) Extension
    # ========================================================
    print("\n" + "=" * 70)
    print("  EXTENSION A: Inertial (Wave) Extension")
    print("=" * 70)

    # --------------------------------------------------------
    # A1: Wave propagation from Gaussian pulse (1D, N=512)
    # --------------------------------------------------------
    print("\n>>> A1: Wave propagation from Gaussian pulse (1D)")
    a1_results = []
    for tau in [0.0, 0.1, 1.0, 10.0, 100.0]:
        for damping in [0.1, 0.5, 1.0]:
            p = EDParams(
                alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
                dimensions=1, N=512, dx=1.0, cfl_safety=0.4,
                n_steps=20000, record_interval=200, boundary="periodic",
            )
            rho_0 = ic_gaussian_pulse(p, rho_mean=50.0, pulse_height=15.0,
                                       pulse_sigma=15.0)

            label = f"A1_tau{tau}_damp{damping}"
            print(f"  {label}...", end="", flush=True)
            t0 = time.time()

            result = simulate_inertial(p, rho_0, tau=tau,
                                        damping_ratio=damping,
                                        snapshot_interval=500)

            elapsed = time.time() - t0
            d = result['diagnostics']

            info = {
                'tau': tau,
                'damping': damping,
                'eta_used': result['eta_used'],
                'final_step': result['final_step'],
                'elapsed_s': elapsed,
            }

            if d:
                info['initial_rho_max'] = d[0]['rho_max']
                info['final_rho_max'] = d[-1]['rho_max']
                info['initial_rho_std'] = d[0]['rho_std']
                info['final_rho_std'] = d[-1]['rho_std']
                info['initial_grad_mean'] = d[0]['grad_mean']
                info['final_grad_mean'] = d[-1]['grad_mean']
                info['final_v_rms'] = d[-1].get('v_rms', 0)
                info['final_v_max'] = d[-1].get('v_max', 0)
                info['final_KE'] = d[-1].get('kinetic_energy', 0)
                info['final_n_peaks'] = d[-1].get('n_peaks', 0)
                info['initial_n_peaks'] = d[0].get('n_peaks', 0)

                # Check for wave propagation: did the pulse spread or stay?
                # Compare peak positions at start vs end from snapshots
                if result['snapshots'] and len(result['snapshots']) >= 2:
                    snap_0 = result['snapshots'][0]
                    snap_mid = result['snapshots'][len(result['snapshots']) // 2]
                    snap_f = result['snapshots'][-1]

                    # Check if peak moved
                    peak_0 = int(np.argmax(snap_0))
                    peak_f = int(np.argmax(snap_f))
                    info['peak_moved'] = abs(peak_f - peak_0)

                    # Check for secondary peaks (wave fronts)
                    n_p0, _, _ = _detect_peaks_1d(snap_0)
                    n_pf, _, _ = _detect_peaks_1d(snap_f)
                    info['new_peaks_generated'] = max(0, n_pf - n_p0)

                    # Oscillation check: does the v field show traveling pattern?
                    if 'v_sign_changes' in d[-1]:
                        info['v_sign_changes'] = d[-1]['v_sign_changes']

            a1_results.append(info)
            print(f" done ({elapsed:.1f}s) "
                  f"v_rms={info.get('final_v_rms', 0):.4f} "
                  f"peaks={info.get('initial_n_peaks', 0)}->{info.get('final_n_peaks', 0)}")

    all_results['A1_wave_propagation'] = a1_results

    # --------------------------------------------------------
    # A2: Oscillatory mode check (1D, N=512)
    # --------------------------------------------------------
    print("\n>>> A2: Oscillatory mode check — sinusoidal IC (1D)")
    a2_results = []
    for tau in [1.0, 10.0, 100.0]:
        for damping in [0.1, 0.5, 1.0]:
            p = EDParams(
                alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
                dimensions=1, N=512, dx=1.0, cfl_safety=0.4,
                n_steps=20000, record_interval=200, boundary="periodic",
            )
            rho_0 = ic_sinusoidal(p, rho_mean=50.0, amplitude=5.0, n_modes=3)

            label = f"A2_tau{tau}_damp{damping}"
            print(f"  {label}...", end="", flush=True)
            t0 = time.time()

            result = simulate_inertial(p, rho_0, tau=tau,
                                        damping_ratio=damping,
                                        snapshot_interval=500)

            elapsed = time.time() - t0
            d = result['diagnostics']

            info = {
                'tau': tau,
                'damping': damping,
                'eta_used': result['eta_used'],
                'final_step': result['final_step'],
                'elapsed_s': elapsed,
            }

            if d:
                info['initial_grad_energy'] = d[0]['grad_energy']
                info['final_grad_energy'] = d[-1]['grad_energy']
                info['grad_energy_ratio'] = (d[-1]['grad_energy'] / d[0]['grad_energy']
                                              if d[0]['grad_energy'] > 0 else 0)
                info['final_v_rms'] = d[-1].get('v_rms', 0)
                info['final_KE'] = d[-1].get('kinetic_energy', 0)

                # Track v_rms over time for oscillation detection
                v_rms_series = [dd.get('v_rms', 0) for dd in d]
                info['v_rms_max'] = max(v_rms_series)
                info['v_rms_final'] = v_rms_series[-1]
                # Oscillation: does v_rms go up and down?
                if len(v_rms_series) > 10:
                    v_arr = np.array(v_rms_series)
                    # Count local maxima in v_rms time series
                    oscillations = 0
                    for i in range(1, len(v_arr) - 1):
                        if v_arr[i] > v_arr[i - 1] and v_arr[i] > v_arr[i + 1]:
                            oscillations += 1
                    info['v_rms_oscillations'] = oscillations

            a2_results.append(info)
            print(f" done ({elapsed:.1f}s) "
                  f"GE_ratio={info.get('grad_energy_ratio', 0):.4f} "
                  f"v_osc={info.get('v_rms_oscillations', 0)}")

    all_results['A2_oscillatory_modes'] = a2_results

    # --------------------------------------------------------
    # A3: Inertial extension — 2D test (128x128)
    # --------------------------------------------------------
    print("\n>>> A3: Inertial extension — 2D Gaussian pulse (128x128)")
    a3_results = []
    for tau in [0.0, 1.0, 10.0]:
        for damping in [0.5, 1.0]:
            p = EDParams(
                alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
                dimensions=2, N=128, dx=1.0, cfl_safety=0.4,
                n_steps=10000, record_interval=200, boundary="periodic",
            )
            rho_0 = ic_gaussian_pulse(p, rho_mean=50.0, pulse_height=15.0,
                                       pulse_sigma=10.0)

            label = f"A3_2d_tau{tau}_damp{damping}"
            print(f"  {label}...", end="", flush=True)
            t0 = time.time()

            result = simulate_inertial(p, rho_0, tau=tau,
                                        damping_ratio=damping,
                                        snapshot_interval=1000)

            elapsed = time.time() - t0
            d = result['diagnostics']

            info = {
                'tau': tau,
                'damping': damping,
                'eta_used': result['eta_used'],
                'final_step': result['final_step'],
                'elapsed_s': elapsed,
            }
            if d:
                info['initial_rho_max'] = d[0]['rho_max']
                info['final_rho_max'] = d[-1]['rho_max']
                info['initial_n_peaks'] = d[0]['n_peaks']
                info['final_n_peaks'] = d[-1]['n_peaks']
                info['final_v_rms'] = d[-1].get('v_rms', 0)
                info['final_KE'] = d[-1].get('kinetic_energy', 0)
                info['final_rho_std'] = d[-1]['rho_std']

            a3_results.append(info)
            print(f" done ({elapsed:.1f}s) "
                  f"peaks={info.get('initial_n_peaks', 0)}->{info.get('final_n_peaks', 0)} "
                  f"v_rms={info.get('final_v_rms', 0):.4f}")

    all_results['A3_2d_inertial'] = a3_results

    # --------------------------------------------------------
    # A4: Horizon behavior with inertial term
    # --------------------------------------------------------
    print("\n>>> A4: Horizon behavior with inertial term (1D)")
    a4_results = []
    for tau in [0.0, 1.0, 10.0]:
        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=1, N=512, dx=1.0, cfl_safety=0.4,
            n_steps=20000, record_interval=200, boundary="periodic",
        )
        rho_0 = np.full(512, 50.0, dtype=np.float64)
        x = np.arange(512)
        rho_0 += 45.0 * np.exp(-0.5 * ((x - 256) / 30.0) ** 2)  # peak at 95

        label = f"A4_horizon_tau{tau}"
        print(f"  {label}...", end="", flush=True)
        t0 = time.time()

        result = simulate_inertial(p, rho_0, tau=tau, damping_ratio=1.0,
                                    snapshot_interval=500)

        elapsed = time.time() - t0
        d = result['diagnostics']

        info = {'tau': tau, 'elapsed_s': elapsed, 'final_step': result['final_step']}
        if d:
            info['initial_horizon_frac'] = d[0]['horizon_frac']
            info['final_horizon_frac'] = d[-1]['horizon_frac']
            info['initial_M_min'] = d[0]['M_min']
            info['final_M_min'] = d[-1]['M_min']
            info['initial_rho_max'] = d[0]['rho_max']
            info['final_rho_max'] = d[-1]['rho_max']

        a4_results.append(info)
        print(f" done ({elapsed:.1f}s) "
              f"rho_max={info.get('final_rho_max', 0):.1f} "
              f"horizon={info.get('final_horizon_frac', 0):.4f}")

    all_results['A4_horizon_inertial'] = a4_results

    # ========================================================
    # EXTENSION B: Nonlocal Kernel Extension
    # ========================================================
    print("\n" + "=" * 70)
    print("  EXTENSION B: Nonlocal Kernel Extension")
    print("=" * 70)

    # --------------------------------------------------------
    # B1: Two-peak interaction with nonlocal coupling (1D)
    # --------------------------------------------------------
    print("\n>>> B1: Two-peak interaction with nonlocal coupling (1D)")
    b1_results = []
    for sigma_nl in [0.0, 0.001, 0.005, 0.01, 0.05]:
        for R in [30.0, 100.0]:
            p = EDParams(
                alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
                dimensions=1, N=512, dx=1.0, cfl_safety=0.4,
                n_steps=20000, record_interval=200, boundary="periodic",
            )
            rho_0 = ic_two_bumps(p, rho_mean=50.0, bump_height=25.0,
                                  separation=0.3)

            label = f"B1_sigma{sigma_nl}_R{R}"
            print(f"  {label}...", end="", flush=True)
            t0 = time.time()

            if sigma_nl == 0.0:
                # Canonical PDE for comparison
                result = simulate_inertial(p, rho_0, tau=0.0,
                                            snapshot_interval=500)
            else:
                result = simulate_nonlocal(p, rho_0, sigma_nl=sigma_nl,
                                            R_kernel=R,
                                            snapshot_interval=500)

            elapsed = time.time() - t0
            d = result['diagnostics']

            info = {
                'sigma_nl': sigma_nl,
                'R_kernel': R,
                'elapsed_s': elapsed,
                'eta_used': result['eta_used'],
                'final_step': result['final_step'],
            }

            if d:
                info['initial_n_peaks'] = d[0]['n_peaks']
                info['final_n_peaks'] = d[-1]['n_peaks']
                info['initial_rho_max'] = d[0]['rho_max']
                info['final_rho_max'] = d[-1]['rho_max']
                info['initial_rho_std'] = d[0]['rho_std']
                info['final_rho_std'] = d[-1]['rho_std']

                # Track peak positions for interaction detection
                if result['snapshots'] and len(result['snapshots']) >= 2:
                    snap_0 = result['snapshots'][0]
                    snap_f = result['snapshots'][-1]
                    _, _, pos_0 = _detect_peaks_1d(snap_0)
                    _, _, pos_f = _detect_peaks_1d(snap_f)

                    if len(pos_0) >= 2 and len(pos_f) >= 2:
                        # Sort positions
                        pos_0_s = sorted(pos_0)
                        pos_f_s = sorted(pos_f)
                        # Find the two tallest peaks
                        init_sep = abs(pos_0_s[-1] - pos_0_s[-2]) if len(pos_0_s) >= 2 else 0
                        final_sep = abs(pos_f_s[-1] - pos_f_s[-2]) if len(pos_f_s) >= 2 else 0
                        info['initial_peak_sep'] = init_sep
                        info['final_peak_sep'] = final_sep
                        info['sep_change'] = final_sep - init_sep
                    elif len(pos_f) < 2 and len(pos_0) >= 2:
                        info['peaks_merged'] = True
                        info['sep_change'] = -999  # merged

            b1_results.append(info)
            sep_str = f"sep_change={info.get('sep_change', 'N/A')}"
            print(f" done ({elapsed:.1f}s) "
                  f"peaks={info.get('initial_n_peaks', 0)}->{info.get('final_n_peaks', 0)} "
                  f"{sep_str}")

    all_results['B1_peak_interaction'] = b1_results

    # --------------------------------------------------------
    # B2: Cosmological timeline with nonlocal term (1D)
    # --------------------------------------------------------
    print("\n>>> B2: Cosmological timeline with nonlocal term (1D)")
    b2_results = []
    for sigma_nl in [0.0, 0.001, 0.01, 0.05]:
        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=1, N=512, dx=1.0, cfl_safety=0.4,
            n_steps=20000, record_interval=200, boundary="periodic",
        )
        rng = np.random.default_rng(42)
        rho_0 = 50.0 + 0.5 * rng.standard_normal(512)
        np.clip(rho_0, 0.0, None, out=rho_0)

        label = f"B2_cosmo_sigma{sigma_nl}"
        print(f"  {label}...", end="", flush=True)
        t0 = time.time()

        if sigma_nl == 0.0:
            result = simulate_inertial(p, rho_0, tau=0.0, snapshot_interval=500)
        else:
            result = simulate_nonlocal(p, rho_0, sigma_nl=sigma_nl,
                                        R_kernel=50.0, snapshot_interval=500)

        elapsed = time.time() - t0
        d = result['diagnostics']

        info = {
            'sigma_nl': sigma_nl,
            'elapsed_s': elapsed,
            'final_step': result['final_step'],
        }

        if d:
            # Measure inflation rate
            steps = np.array([dd['step'] for dd in d])
            grad_mean = np.array([dd['grad_mean'] for dd in d])
            info['initial_grad_mean'] = d[0]['grad_mean']
            info['final_grad_mean'] = d[-1]['grad_mean']
            info['initial_n_basins'] = d[0]['n_basins']
            info['final_n_basins'] = d[-1]['n_basins']
            info['initial_rho_mean'] = d[0]['rho_mean']
            info['final_rho_mean'] = d[-1]['rho_mean']

            # Fit exponential decay to grad_mean
            eta_used = result['eta_used']
            phys_t = steps * eta_used
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

        b2_results.append(info)
        print(f" done ({elapsed:.1f}s) "
              f"lambda_1={info.get('lambda_1', 'N/A'):.4f} "
              f"R2={info.get('r_squared', 'N/A'):.3f}")

    all_results['B2_cosmological_nonlocal'] = b2_results

    # --------------------------------------------------------
    # B3: Nonlocal extension — 2D test (128x128)
    # --------------------------------------------------------
    print("\n>>> B3: Nonlocal extension — 2D (128x128)")
    b3_results = []
    for sigma_nl in [0.0, 0.005, 0.01]:
        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=2, N=128, dx=1.0, cfl_safety=0.4,
            n_steps=10000, record_interval=200, boundary="periodic",
        )
        rng = np.random.default_rng(42)
        rho_0 = 50.0 + 5.0 * rng.standard_normal((128, 128))
        np.clip(rho_0, 0.0, None, out=rho_0)

        label = f"B3_2d_sigma{sigma_nl}"
        print(f"  {label}...", end="", flush=True)
        t0 = time.time()

        if sigma_nl == 0.0:
            result = simulate_inertial(p, rho_0, tau=0.0, snapshot_interval=1000)
        else:
            result = simulate_nonlocal(p, rho_0, sigma_nl=sigma_nl,
                                        R_kernel=20.0, snapshot_interval=1000)

        elapsed = time.time() - t0
        d = result['diagnostics']

        info = {
            'sigma_nl': sigma_nl,
            'elapsed_s': elapsed,
            'final_step': result['final_step'],
        }
        if d:
            info['initial_n_peaks'] = d[0]['n_peaks']
            info['final_n_peaks'] = d[-1]['n_peaks']
            info['initial_n_basins'] = d[0]['n_basins']
            info['final_n_basins'] = d[-1]['n_basins']
            info['initial_rho_std'] = d[0]['rho_std']
            info['final_rho_std'] = d[-1]['rho_std']

        b3_results.append(info)
        print(f" done ({elapsed:.1f}s) "
              f"peaks={info.get('initial_n_peaks', 0)}->{info.get('final_n_peaks', 0)} "
              f"basins={info.get('initial_n_basins', 0)}->{info.get('final_n_basins', 0)}")

        # Save final snapshot
        if sigma_nl > 0:
            np.save(os.path.join(output_dir, f"2d_nonlocal_sigma{sigma_nl}_final.npy"),
                    result['rho_final'])

    all_results['B3_2d_nonlocal'] = b3_results

    # --------------------------------------------------------
    # B4: Horizon behavior with nonlocal coupling
    # --------------------------------------------------------
    print("\n>>> B4: Horizon behavior with nonlocal coupling (1D)")
    b4_results = []
    for sigma_nl in [0.0, 0.005, 0.01]:
        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=1, N=512, dx=1.0, cfl_safety=0.4,
            n_steps=20000, record_interval=200, boundary="periodic",
        )
        rho_0 = np.full(512, 50.0, dtype=np.float64)
        x = np.arange(512)
        rho_0 += 45.0 * np.exp(-0.5 * ((x - 256) / 30.0) ** 2)

        label = f"B4_horizon_sigma{sigma_nl}"
        print(f"  {label}...", end="", flush=True)
        t0 = time.time()

        if sigma_nl == 0.0:
            result = simulate_inertial(p, rho_0, tau=0.0, snapshot_interval=500)
        else:
            result = simulate_nonlocal(p, rho_0, sigma_nl=sigma_nl,
                                        R_kernel=50.0, snapshot_interval=500)

        elapsed = time.time() - t0
        d = result['diagnostics']

        info = {'sigma_nl': sigma_nl, 'elapsed_s': elapsed}
        if d:
            info['initial_horizon_frac'] = d[0]['horizon_frac']
            info['final_horizon_frac'] = d[-1]['horizon_frac']
            info['initial_rho_max'] = d[0]['rho_max']
            info['final_rho_max'] = d[-1]['rho_max']

        b4_results.append(info)
        print(f" done ({elapsed:.1f}s) "
              f"rho_max={info.get('final_rho_max', 0):.1f} "
              f"horizon={info.get('final_horizon_frac', 0):.4f}")

    all_results['B4_horizon_nonlocal'] = b4_results

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

    results_path = os.path.join(output_dir, "extension_results.json")
    with open(results_path, 'w') as f:
        json.dump(make_serializable(all_results), f, indent=2, default=str)

    elapsed_total = time.time() - t_total
    print(f"\n{'=' * 70}")
    print(f"  All extension experiments complete in {elapsed_total:.1f}s")
    print(f"  Results saved to {results_path}")
    print(f"{'=' * 70}")

    return all_results


if __name__ == "__main__":
    output_dir = os.path.join(os.path.dirname(__file__), "results")
    run_extension_experiments(output_dir=output_dir)
