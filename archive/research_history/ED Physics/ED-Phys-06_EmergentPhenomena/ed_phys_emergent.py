"""
ED-Phys-06: Emergent Phenomena Scanner
========================================
Targeted high-resolution simulations to detect:
  1. Stable localized structures (peaks, oscillons, solitons, lumps)
  2. Wave-like modes (traveling curvature waves, dispersion)
  3. Horizon dynamics (M(rho)=0 surfaces, merging/splitting)
  4. Structure-formation motifs (basin merging, ridges, filaments)
  5. Critical phenomena (bifurcations, thresholds, universality)

Canonical sources: ED-Phys-01 through ED-Phys-05, ED-5, ED-12, ED-12.5.
"""

import sys
import os
import time
import json
import csv
import numpy as np

# Add simulator to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ED-Phys-02_Simulator'))

from ed_phys_config import EDParams
from ed_phys_lattice import create_initial_condition
from ed_phys_engine import simulate, SimulationResult, DiagnosticRecord
from ed_phys_diagnostics import extract_time_series, identify_phases
from ed_phys_operators import (
    discrete_laplacian, discrete_grad_squared, discrete_grad_magnitude,
    mobility, mobility_derivative,
)


# ============================================================
# Custom IC generators for emergent-phenomena experiments
# ============================================================

def ic_two_bumps(params, rho_mean=50.0, bump_height=25.0, separation=0.3, seed=42):
    """Two Gaussian bumps at configurable separation (fraction of domain).

    Used to test: peak interaction, merging, attraction.
    """
    rng = np.random.default_rng(seed)
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


def ic_step_function(params, rho_low=20.0, rho_high=80.0, seed=42):
    """Step function IC: half domain at rho_high, half at rho_low.

    Used to test: wave generation from sharp discontinuity, horizon dynamics.
    """
    N = params.N
    if params.dimensions == 1:
        rho = np.full(N, rho_low, dtype=np.float64)
        rho[N // 4: 3 * N // 4] = rho_high
    else:
        rho = np.full((N, N), rho_low, dtype=np.float64)
        rho[N // 4: 3 * N // 4, N // 4: 3 * N // 4] = rho_high
    return rho


def ic_near_horizon(params, rho_mean=90.0, noise_amplitude=5.0, seed=42):
    """IC near rho_max for horizon dynamics studies.

    Used to test: M(rho)=0 surface formation and evolution.
    """
    rng = np.random.default_rng(seed)
    shape = params.grid_shape
    rho = rho_mean + noise_amplitude * rng.standard_normal(shape)
    np.clip(rho, 0.0, params.rho_max, out=rho)
    return rho


def ic_multi_peak(params, rho_mean=50.0, n_peaks=5, peak_height=20.0, seed=42):
    """Multiple peaks at random positions.

    Used to test: structure merging patterns, filamentary connections.
    """
    rng = np.random.default_rng(seed)
    N = params.N

    if params.dimensions == 1:
        rho = np.full(N, rho_mean, dtype=np.float64)
        sigma = N * 0.02
        positions = rng.integers(0, N, size=n_peaks)
        x = np.arange(N)
        for pos in positions:
            rho += peak_height * np.exp(-0.5 * ((x - pos) / sigma) ** 2)
    else:
        rho = np.full((N, N), rho_mean, dtype=np.float64)
        sigma = N * 0.02
        positions = rng.integers(0, N, size=(n_peaks, 2))
        x, y = np.meshgrid(np.arange(N), np.arange(N), indexing='ij')
        for px, py in positions:
            r2 = (x - px) ** 2 + (y - py) ** 2
            rho += peak_height * np.exp(-0.5 * r2 / sigma ** 2)

    np.clip(rho, 0.0, None, out=rho)
    return rho


def ic_sinusoidal(params, rho_mean=50.0, amplitude=5.0, n_modes=3, seed=42):
    """Sinusoidal perturbation for wave/dispersion analysis.

    Used to test: dispersive vs non-dispersive propagation.
    """
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
# Enhanced diagnostics for emergent phenomena
# ============================================================

def compute_enhanced_diagnostics(rho, params, rho_prev=None, dt=None):
    """Compute extended diagnostics beyond standard DiagnosticRecord.

    Returns a dict with:
      - Standard: rho_mean, rho_max, rho_min, grad_mean, grad_max
      - Curvature: lap_mean, lap_std, lap_pos_frac, lap_zero_crossings
      - Horizon: horizon_frac, horizon_sites, M_min
      - Structure: n_peaks_1d (or n_peaks_2d), peak_heights, peak_widths
      - Wave: if rho_prev provided, velocity estimates
    """
    dx = params.dx
    boundary = params.boundary
    rho_min_abs = params.rho_min_absorbing

    grad_mag = discrete_grad_magnitude(rho, dx, boundary, rho_min_abs)
    lap = discrete_laplacian(rho, dx, boundary, rho_min_abs)
    M = mobility(rho, params.M_0, params.rho_max, params.n_mob)
    grad_sq = discrete_grad_squared(rho, dx, boundary, rho_min_abs)

    diag = {}

    # Standard
    diag['rho_mean'] = float(np.mean(rho))
    diag['rho_max'] = float(np.max(rho))
    diag['rho_min'] = float(np.min(rho))
    diag['rho_std'] = float(np.std(rho))
    diag['grad_mean'] = float(np.mean(grad_mag))
    diag['grad_max'] = float(np.max(grad_mag))
    diag['grad_energy'] = float(np.sum(grad_sq))

    # Curvature
    diag['lap_mean'] = float(np.mean(lap))
    diag['lap_std'] = float(np.std(lap))
    diag['lap_pos_frac'] = float(np.sum(lap > 0) / lap.size)

    # Laplacian zero-crossings (sign changes between neighbors)
    if rho.ndim == 1:
        sign_changes = np.sum(np.diff(np.sign(lap)) != 0)
    else:
        # Horizontal + vertical sign changes
        sign_changes = (
            np.sum(np.diff(np.sign(lap), axis=0) != 0) +
            np.sum(np.diff(np.sign(lap), axis=1) != 0)
        )
    diag['lap_zero_crossings'] = int(sign_changes)

    # Horizon dynamics
    horizon_threshold = 0.9 * params.rho_max
    horizon_mask = rho > horizon_threshold
    diag['horizon_frac'] = float(np.sum(horizon_mask) / rho.size)
    diag['horizon_sites'] = int(np.sum(horizon_mask))
    diag['M_min'] = float(np.min(M))
    diag['M_mean'] = float(np.mean(M))

    # Peak detection
    if rho.ndim == 1:
        n_peaks, peak_heights, peak_positions = _detect_peaks_1d(rho)
        diag['n_peaks'] = n_peaks
        diag['peak_heights'] = peak_heights
        diag['peak_positions'] = peak_positions
    else:
        n_peaks, peak_heights, peak_positions = _detect_peaks_2d(rho)
        diag['n_peaks'] = n_peaks
        diag['peak_heights'] = peak_heights
        diag['peak_positions'] = peak_positions

    # Flux
    flux = M * grad_mag
    diag['flux_mean'] = float(np.mean(flux))
    diag['flux_max'] = float(np.max(flux))

    # Wave detection (requires previous snapshot)
    if rho_prev is not None and dt is not None and dt > 0:
        drho = rho - rho_prev
        diag['drho_max'] = float(np.max(np.abs(drho)))
        diag['drho_rms'] = float(np.sqrt(np.mean(drho ** 2)))

        # Check for oscillatory behavior: does drho change sign spatially?
        if rho.ndim == 1:
            drho_sign_changes = int(np.sum(np.diff(np.sign(drho)) != 0))
        else:
            drho_sign_changes = int(
                np.sum(np.diff(np.sign(drho), axis=0) != 0) +
                np.sum(np.diff(np.sign(drho), axis=1) != 0)
            )
        diag['drho_sign_changes'] = drho_sign_changes

    return diag


def _detect_peaks_1d(rho):
    """Find local maxima in 1D field (periodic)."""
    N = len(rho)
    peaks = []
    for i in range(N):
        left = rho[(i - 1) % N]
        right = rho[(i + 1) % N]
        if rho[i] > left and rho[i] > right:
            peaks.append((i, float(rho[i])))
    n_peaks = len(peaks)
    positions = [p[0] for p in peaks]
    heights = [p[1] for p in peaks]
    return n_peaks, heights, positions


def _detect_peaks_2d(rho):
    """Find local maxima in 2D field (periodic)."""
    N = rho.shape[0]
    padded = np.pad(rho, 1, mode='wrap')
    center = padded[1:-1, 1:-1]
    is_max = (
        (center > padded[:-2, 1:-1]) &
        (center > padded[2:, 1:-1]) &
        (center > padded[1:-1, :-2]) &
        (center > padded[1:-1, 2:])
    )
    positions = list(zip(*np.where(is_max)))
    heights = [float(rho[i, j]) for i, j in positions]
    return len(positions), heights, positions


# ============================================================
# Experiment definitions
# ============================================================

def run_experiment(label, params, rho_0, snapshot_interval=500,
                   enhanced_interval=500, verbose=True):
    """Run a simulation with enhanced diagnostics at regular intervals.

    Returns:
      - SimulationResult (standard)
      - enhanced_history: list of (step, enhanced_diag_dict)
      - snapshots_enhanced: list of (step, rho_copy) at enhanced_interval
    """
    if verbose:
        print(f"\n{'='*60}")
        print(f"  Experiment: {label}")
        print(f"  {params.dimensions}D, N={params.N}, steps={params.n_steps}")
        print(f"  alpha={params.alpha}, gamma={params.gamma_exp}, "
              f"M_0={params.M_0}, n_mob={params.n_mob}")
        print(f"  eta={params.eta:.6e}")
        print(f"{'='*60}")

    t0 = time.time()
    result = simulate(params, rho_0, snapshot_interval=snapshot_interval)
    elapsed = time.time() - t0

    if verbose:
        print(f"  Completed in {elapsed:.1f}s, final step={result.final_step}")

    # Compute enhanced diagnostics from snapshots
    enhanced_history = []
    if result.rho_snapshots:
        prev_snap = None
        for idx, snap in enumerate(result.rho_snapshots):
            step = idx * snapshot_interval
            dt_phys = snapshot_interval * params.eta
            diag = compute_enhanced_diagnostics(
                snap, params,
                rho_prev=prev_snap,
                dt=dt_phys if prev_snap is not None else None,
            )
            diag['step'] = step
            enhanced_history.append(diag)
            prev_snap = snap

    return result, enhanced_history


def peak_persistence_experiment(params_base, rho_0, label, verbose=True):
    """Measure how long peaks persist by tracking their heights over time.

    Returns dict with per-peak persistence data.
    """
    result, enh = run_experiment(label, params_base, rho_0,
                                 snapshot_interval=max(1, params_base.n_steps // 100),
                                 verbose=verbose)

    if not enh:
        return {'label': label, 'n_snapshots': 0}

    # Track peak count and max height over time
    steps = [e['step'] for e in enh]
    n_peaks_over_time = [e['n_peaks'] for e in enh]
    max_height_over_time = [e['rho_max'] for e in enh]
    rho_std_over_time = [e['rho_std'] for e in enh]
    grad_mean_over_time = [e['grad_mean'] for e in enh]

    # Determine persistence: how many steps before peak count changes
    initial_peaks = n_peaks_over_time[0] if n_peaks_over_time else 0
    persistence_step = params_base.n_steps  # default: survived entire run
    for i, np_val in enumerate(n_peaks_over_time):
        if np_val != initial_peaks:
            persistence_step = steps[i]
            break

    # Height stability: std of max_height relative to initial
    heights_arr = np.array(max_height_over_time)
    if len(heights_arr) > 1 and heights_arr[0] > 0:
        height_stability = float(np.std(heights_arr) / heights_arr[0])
        height_drift = float((heights_arr[-1] - heights_arr[0]) / heights_arr[0])
    else:
        height_stability = 0.0
        height_drift = 0.0

    return {
        'label': label,
        'n_snapshots': len(enh),
        'initial_peaks': initial_peaks,
        'final_peaks': n_peaks_over_time[-1] if n_peaks_over_time else 0,
        'persistence_step': persistence_step,
        'height_stability': height_stability,
        'height_drift_pct': height_drift * 100,
        'initial_rho_max': max_height_over_time[0] if max_height_over_time else 0,
        'final_rho_max': max_height_over_time[-1] if max_height_over_time else 0,
        'initial_grad_mean': grad_mean_over_time[0] if grad_mean_over_time else 0,
        'final_grad_mean': grad_mean_over_time[-1] if grad_mean_over_time else 0,
        'steps_data': steps,
        'n_peaks_data': n_peaks_over_time,
        'rho_max_data': max_height_over_time,
        'rho_std_data': rho_std_over_time,
        'grad_mean_data': grad_mean_over_time,
        'total_steps': params_base.n_steps,
        'eta': params_base.eta,
    }


# ============================================================
# Main experiment runner
# ============================================================

def run_all_experiments(output_dir="results"):
    """Run all ED-Phys-06 emergent phenomena experiments."""

    os.makedirs(output_dir, exist_ok=True)
    all_results = {}

    print("=" * 70)
    print("  ED-Phys-06: Emergent Phenomena — Full Experiment Suite")
    print("=" * 70)
    t_total = time.time()

    # ========================================================
    # EXPERIMENT 1: Stable Localized Structures (1D, N=2048)
    # ========================================================
    print("\n>>> BLOCK 1: Stable Localized Structures (1D)")

    # 1a: Single bump persistence at various alpha
    print("  1a: Single bump persistence vs alpha")
    bump_results = []
    for alpha in [0.05, 0.1, 0.3, 0.5, 1.0, 2.0]:
        p = EDParams(
            alpha=alpha, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=1, N=2048, dx=1.0, cfl_safety=0.4,
            n_steps=50000, record_interval=500, boundary="periodic",
        )
        rho_0 = np.full(2048, 50.0)
        # Add single Gaussian bump
        x = np.arange(2048)
        rho_0 += 25.0 * np.exp(-0.5 * ((x - 1024) / 30.0) ** 2)

        res = peak_persistence_experiment(p, rho_0,
                                          f"bump_alpha_{alpha}", verbose=False)
        bump_results.append(res)
        print(f"    alpha={alpha}: peaks {res['initial_peaks']}->{res['final_peaks']}, "
              f"height drift={res['height_drift_pct']:.4f}%")

    all_results['1a_bump_persistence'] = bump_results

    # 1b: Two bumps at various separations — do they attract?
    print("  1b: Two-bump interaction vs separation", flush=True)
    two_bump_results = []
    for sep in [0.05, 0.10, 0.15, 0.20, 0.30, 0.40]:
        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=1, N=2048, dx=1.0, cfl_safety=0.4,
            n_steps=50000, record_interval=500, boundary="periodic",
        )
        rho_0 = ic_two_bumps(p, rho_mean=50.0, bump_height=25.0, separation=sep)

        # Single run — use run_experiment with snapshots for position tracking
        result_sim, enh = run_experiment(
            f"two_bump_sep_{sep}", p, rho_0,
            snapshot_interval=max(1, p.n_steps // 50), verbose=False,
        )

        # Track peak positions at start and end
        if enh:
            initial_pos = enh[0].get('peak_positions', [])
            final_pos = enh[-1].get('peak_positions', [])
            initial_peaks = enh[0]['n_peaks']
            final_peaks = enh[-1]['n_peaks']
            height_drift = ((enh[-1]['rho_max'] - enh[0]['rho_max']) / enh[0]['rho_max'] * 100
                            if enh[0]['rho_max'] > 0 else 0)
        else:
            initial_pos = []
            final_pos = []
            initial_peaks = 0
            final_peaks = 0
            height_drift = 0

        res = {
            'separation': sep,
            'initial_peaks': initial_peaks,
            'final_peaks': final_peaks,
            'height_drift_pct': height_drift,
            'initial_positions': initial_pos,
            'final_positions': final_pos,
        }
        two_bump_results.append(res)

        # Compute separation change
        if len(initial_pos) >= 2 and len(final_pos) >= 2:
            init_sep_val = abs(initial_pos[1] - initial_pos[0])
            final_sep_val = abs(final_pos[1] - final_pos[0])
            sep_change = final_sep_val - init_sep_val
            print(f"    sep={sep}: peaks {initial_peaks}->{final_peaks}, "
                  f"sep {init_sep_val:.0f}->{final_sep_val:.0f} (delta={sep_change:.1f})",
                  flush=True)
        else:
            print(f"    sep={sep}: peaks {initial_peaks}->{final_peaks}", flush=True)

    all_results['1b_two_bump_interaction'] = two_bump_results

    # 1c: Oscillon search — start with perturbation near penalty-dominated regime
    print("  1c: Oscillon search (high gamma_exp)")
    oscillon_results = []
    for gamma in [0.6, 0.7, 0.8]:
        for alpha in [0.5, 1.0]:
            p = EDParams(
                alpha=alpha, gamma_exp=gamma, M_0=1.0, rho_max=100.0, n_mob=2,
                dimensions=1, N=2048, dx=1.0, cfl_safety=0.4,
                n_steps=50000, record_interval=500, boundary="periodic",
            )
            rho_0 = ic_sinusoidal(p, rho_mean=50.0, amplitude=10.0, n_modes=5)
            res = peak_persistence_experiment(p, rho_0,
                                              f"oscillon_g{gamma}_a{alpha}",
                                              verbose=False)
            oscillon_results.append({
                'gamma_exp': gamma, 'alpha': alpha,
                **{k: v for k, v in res.items() if k not in ['steps_data', 'n_peaks_data',
                   'rho_max_data', 'rho_std_data', 'grad_mean_data',
                   'peak_positions', 'initial_positions', 'final_positions']}
            })
            print(f"    gamma={gamma}, alpha={alpha}: peaks {res['initial_peaks']}->"
                  f"{res['final_peaks']}, height_drift={res['height_drift_pct']:.2f}%")

    all_results['1c_oscillon_search'] = oscillon_results

    # ========================================================
    # EXPERIMENT 2: Wave-like Modes (1D, N=2048)
    # ========================================================
    print("\n>>> BLOCK 2: Wave-like Modes (1D)")

    # 2a: Sinusoidal modes — track dispersion
    print("  2a: Dispersion analysis (sinusoidal IC)")
    wave_results = []
    for n_modes in [1, 3, 5, 10]:
        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=1, N=2048, dx=1.0, cfl_safety=0.4,
            n_steps=50000, record_interval=500, boundary="periodic",
        )
        rho_0 = ic_sinusoidal(p, rho_mean=50.0, amplitude=5.0, n_modes=n_modes)

        result_sim, enh = run_experiment(
            f"wave_modes_{n_modes}", p, rho_0,
            snapshot_interval=max(1, p.n_steps // 50), verbose=False,
        )

        # Measure per-mode amplitude decay
        ts = extract_time_series(result_sim)
        if ts:
            wave_info = {
                'n_modes': n_modes,
                'initial_grad_energy': float(ts['grad_energy'][0]),
                'final_grad_energy': float(ts['grad_energy'][-1]),
                'grad_energy_ratio': float(ts['grad_energy'][-1] / ts['grad_energy'][0])
                    if ts['grad_energy'][0] > 0 else 0,
                'initial_rho_std': float(np.std(result_sim.rho_snapshots[0]))
                    if result_sim.rho_snapshots else 0,
                'final_rho_std': float(np.std(result_sim.rho_final)),
            }

            # Fourier analysis at start and end
            if result_sim.rho_snapshots:
                fft_initial = np.abs(np.fft.rfft(result_sim.rho_snapshots[0] - np.mean(result_sim.rho_snapshots[0])))
                fft_final = np.abs(np.fft.rfft(result_sim.rho_final - np.mean(result_sim.rho_final)))
                # Track first few mode amplitudes
                n_track = min(15, len(fft_initial))
                wave_info['fft_initial'] = fft_initial[:n_track].tolist()
                wave_info['fft_final'] = fft_final[:n_track].tolist()

                # Decay rates per mode
                decay_rates = []
                total_time = p.n_steps * p.eta
                for k in range(1, n_track):
                    if fft_initial[k] > 1e-10 and fft_final[k] > 1e-10:
                        rate = -np.log(fft_final[k] / fft_initial[k]) / total_time
                        decay_rates.append((k, float(rate)))
                wave_info['per_mode_decay_rates'] = decay_rates

            wave_results.append(wave_info)
            print(f"    modes={n_modes}: grad_energy ratio={wave_info['grad_energy_ratio']:.4f}")

    all_results['2a_dispersion'] = wave_results

    # 2b: Step function — sharp discontinuity evolution
    print("  2b: Step function evolution")
    step_results = []
    for rho_high in [60.0, 70.0, 80.0, 90.0]:
        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=1, N=2048, dx=1.0, cfl_safety=0.4,
            n_steps=50000, record_interval=500, boundary="periodic",
        )
        rho_0 = ic_step_function(p, rho_low=20.0, rho_high=rho_high)

        result_sim, enh = run_experiment(
            f"step_rho{rho_high}", p, rho_0,
            snapshot_interval=max(1, p.n_steps // 50), verbose=False,
        )

        ts = extract_time_series(result_sim)
        if ts:
            step_info = {
                'rho_high': rho_high,
                'initial_grad_max': float(ts['grad_max'][0]),
                'final_grad_max': float(ts['grad_max'][-1]),
                'initial_grad_mean': float(ts['grad_mean'][0]),
                'final_grad_mean': float(ts['grad_mean'][-1]),
                'rho_final_std': float(np.std(result_sim.rho_final)),
                'rho_final_range': float(np.max(result_sim.rho_final) - np.min(result_sim.rho_final)),
            }
            step_results.append(step_info)
            print(f"    rho_high={rho_high}: grad_max {step_info['initial_grad_max']:.4f} -> "
                  f"{step_info['final_grad_max']:.4f}")

    all_results['2b_step_function'] = step_results

    # ========================================================
    # EXPERIMENT 3: Horizon Dynamics (1D, N=2048)
    # ========================================================
    print("\n>>> BLOCK 3: Horizon Dynamics (1D)")

    # 3a: Near-horizon IC
    print("  3a: Near-horizon evolution")
    horizon_results = []
    for rho_mean in [80.0, 85.0, 90.0, 95.0]:
        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=1, N=2048, dx=1.0, cfl_safety=0.4,
            n_steps=50000, record_interval=500, boundary="periodic",
        )
        rho_0 = ic_near_horizon(p, rho_mean=rho_mean, noise_amplitude=3.0)

        result_sim, enh = run_experiment(
            f"horizon_rho{rho_mean}", p, rho_0,
            snapshot_interval=max(1, p.n_steps // 50), verbose=False,
        )

        if enh:
            h_info = {
                'rho_mean_ic': rho_mean,
                'initial_horizon_frac': enh[0]['horizon_frac'],
                'final_horizon_frac': enh[-1]['horizon_frac'],
                'initial_M_min': enh[0]['M_min'],
                'final_M_min': enh[-1]['M_min'],
                'initial_M_mean': enh[0]['M_mean'],
                'final_M_mean': enh[-1]['M_mean'],
                'initial_horizon_sites': enh[0]['horizon_sites'],
                'final_horizon_sites': enh[-1]['horizon_sites'],
                'rho_final_max': float(np.max(result_sim.rho_final)),
                'rho_final_min': float(np.min(result_sim.rho_final)),
                'rho_final_mean': float(np.mean(result_sim.rho_final)),
                'horizon_frac_data': [e['horizon_frac'] for e in enh],
                'M_min_data': [e['M_min'] for e in enh],
            }
            horizon_results.append(h_info)
            print(f"    rho_mean={rho_mean}: horizon {h_info['initial_horizon_frac']:.4f} -> "
                  f"{h_info['final_horizon_frac']:.4f}, M_min={h_info['final_M_min']:.6f}")

    all_results['3a_horizon_evolution'] = horizon_results

    # 3b: High-density bump — horizon formation from localized overdensity
    print("  3b: Localized horizon formation")
    loc_horizon_results = []
    for bump_h in [30.0, 40.0, 45.0, 48.0]:
        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=1, N=2048, dx=1.0, cfl_safety=0.4,
            n_steps=50000, record_interval=500, boundary="periodic",
        )
        rho_0 = np.full(2048, 50.0)
        x = np.arange(2048)
        rho_0 += bump_h * np.exp(-0.5 * ((x - 1024) / 30.0) ** 2)

        result_sim, enh = run_experiment(
            f"loc_horizon_bump{bump_h}", p, rho_0,
            snapshot_interval=max(1, p.n_steps // 50), verbose=False,
        )

        max_rho = float(np.max(rho_0))
        final_max = float(np.max(result_sim.rho_final))
        if enh:
            lh_info = {
                'bump_height': bump_h,
                'initial_max_rho': max_rho,
                'final_max_rho': final_max,
                'exceeds_horizon': max_rho > 0.9 * 100.0,
                'horizon_formed': any(e['horizon_sites'] > 0 for e in enh),
                'max_horizon_frac': max(e['horizon_frac'] for e in enh),
            }
            loc_horizon_results.append(lh_info)
            print(f"    bump={bump_h}: max_rho {max_rho:.1f} -> {final_max:.1f}, "
                  f"horizon={'YES' if lh_info['horizon_formed'] else 'no'}")

    all_results['3b_localized_horizons'] = loc_horizon_results

    # ========================================================
    # EXPERIMENT 4: Structure Formation Motifs (2D, 256x256)
    # ========================================================
    print("\n>>> BLOCK 4: Structure Formation Motifs (2D)")

    # 4a: Multi-peak interaction in 2D
    print("  4a: Multi-peak 2D interaction")
    mp_results_2d = []
    for n_peaks_ic in [3, 5, 10]:
        for alpha in [0.1, 0.5, 1.0]:
            p = EDParams(
                alpha=alpha, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
                dimensions=2, N=128, dx=1.0, cfl_safety=0.4,
                n_steps=20000, record_interval=500, boundary="periodic",
            )
            rho_0 = ic_multi_peak(p, rho_mean=50.0, n_peaks=n_peaks_ic,
                                  peak_height=20.0, seed=42)

            result_sim, enh = run_experiment(
                f"2d_peaks_{n_peaks_ic}_a{alpha}", p, rho_0,
                snapshot_interval=max(1, p.n_steps // 20), verbose=False,
            )

            if enh:
                mp_info = {
                    'n_peaks_ic': n_peaks_ic,
                    'alpha': alpha,
                    'initial_peaks': enh[0]['n_peaks'],
                    'final_peaks': enh[-1]['n_peaks'],
                    'initial_rho_max': enh[0]['rho_max'],
                    'final_rho_max': enh[-1]['rho_max'],
                    'initial_lap_zero_crossings': enh[0]['lap_zero_crossings'],
                    'final_lap_zero_crossings': enh[-1]['lap_zero_crossings'],
                }
                mp_results_2d.append(mp_info)
                print(f"    peaks={n_peaks_ic}, alpha={alpha}: "
                      f"peaks {mp_info['initial_peaks']}->{mp_info['final_peaks']}, "
                      f"Lap crossings {mp_info['initial_lap_zero_crossings']}->"
                      f"{mp_info['final_lap_zero_crossings']}")

    all_results['4a_2d_multi_peak'] = mp_results_2d

    # 4b: Large-noise 2D — look for filamentary structure
    print("  4b: Filamentary structure search (2D, large noise)")
    fil_results = []
    for gamma in [0.5, 0.6, 0.7]:
        p = EDParams(
            alpha=0.3, gamma_exp=gamma, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=2, N=128, dx=1.0, cfl_safety=0.4,
            n_steps=20000, record_interval=500, boundary="periodic",
        )
        rng = np.random.default_rng(42)
        rho_0 = 50.0 + 10.0 * rng.standard_normal((128, 128))
        np.clip(rho_0, 0.0, None, out=rho_0)

        result_sim, enh = run_experiment(
            f"2d_filament_g{gamma}", p, rho_0,
            snapshot_interval=max(1, p.n_steps // 20), verbose=False,
        )

        ts = extract_time_series(result_sim)
        if enh and ts:
            f_info = {
                'gamma_exp': gamma,
                'initial_peaks': enh[0]['n_peaks'],
                'final_peaks': enh[-1]['n_peaks'],
                'initial_rho_std': enh[0]['rho_std'],
                'final_rho_std': enh[-1]['rho_std'],
                'initial_lap_crossings': enh[0]['lap_zero_crossings'],
                'final_lap_crossings': enh[-1]['lap_zero_crossings'],
                'initial_basins': int(ts['n_basins'][0]),
                'final_basins': int(ts['n_basins'][-1]),
                'basin_loss': int(ts['n_basins'][0] - ts['n_basins'][-1]),
            }
            fil_results.append(f_info)
            print(f"    gamma={gamma}: peaks {f_info['initial_peaks']}->"
                  f"{f_info['final_peaks']}, basins {f_info['initial_basins']}->"
                  f"{f_info['final_basins']}")

            # Save final rho snapshot for analysis
            np.save(os.path.join(output_dir, f"2d_filament_g{gamma}_final.npy"),
                    result_sim.rho_final)

    all_results['4b_filamentary'] = fil_results

    # ========================================================
    # EXPERIMENT 5: Critical Phenomena (1D, N=2048)
    # ========================================================
    print("\n>>> BLOCK 5: Critical Phenomena (1D)")

    # 5a: Inflation cliff — fine scan around gamma_exp=0.6-0.7
    print("  5a: Inflation cliff fine scan")
    cliff_results = []
    for gamma in np.arange(0.55, 0.76, 0.01):
        gamma = round(gamma, 2)
        p = EDParams(
            alpha=0.1, gamma_exp=gamma, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=1, N=2048, dx=1.0, cfl_safety=0.4,
            n_steps=50000, record_interval=500, boundary="periodic",
        )
        rho_0 = 50.0 + 0.5 * np.random.default_rng(42).standard_normal(2048)
        np.clip(rho_0, 0.0, None, out=rho_0)

        result_sim = simulate(p, rho_0)
        ts = extract_time_series(result_sim)

        if ts and len(ts['steps']) > 3:
            phys_t = ts['steps'] * p.eta
            valid = ts['grad_mean'] > 0
            if np.sum(valid) > 3:
                log_G = np.log(ts['grad_mean'][valid])
                t_v = phys_t[valid]
                coeffs = np.polyfit(t_v, log_G, 1)
                l1 = -coeffs[0]
                resid = log_G - (coeffs[1] + coeffs[0] * t_v)
                ss_r = np.sum(resid ** 2)
                ss_t = np.sum((log_G - np.mean(log_G)) ** 2)
                r2 = 1 - ss_r / ss_t if ss_t > 0 else 0
            else:
                l1 = 0.0
                r2 = 0.0

            # Basin dynamics
            basin_loss = int(ts['n_basins'][0] - ts['n_basins'][-1])

            cliff_results.append({
                'gamma_exp': gamma,
                'lambda_1': float(l1),
                'r_squared': float(r2),
                'basins_initial': int(ts['n_basins'][0]),
                'basins_final': int(ts['n_basins'][-1]),
                'basin_loss': basin_loss,
            })
            print(f"    gamma={gamma:.2f}: lambda_1={l1:.4f}, R2={r2:.3f}, "
                  f"basin_loss={basin_loss}")

    all_results['5a_inflation_cliff'] = cliff_results

    # 5b: Bifurcation search — alpha threshold for structure survival
    print("  5b: Alpha bifurcation (structure survival threshold)")
    bifurc_results = []
    for alpha in np.arange(0.05, 0.55, 0.05):
        alpha = round(alpha, 2)
        p = EDParams(
            alpha=alpha, gamma_exp=0.6, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=1, N=2048, dx=1.0, cfl_safety=0.4,
            n_steps=50000, record_interval=500, boundary="periodic",
        )
        rho_0 = ic_multi_peak(p, rho_mean=50.0, n_peaks=10, peak_height=15.0, seed=42)

        result_sim, enh = run_experiment(
            f"bifurc_a{alpha}", p, rho_0,
            snapshot_interval=max(1, p.n_steps // 50), verbose=False,
        )

        ts = extract_time_series(result_sim)
        if enh and ts:
            bifurc_results.append({
                'alpha': alpha,
                'initial_peaks': enh[0]['n_peaks'],
                'final_peaks': enh[-1]['n_peaks'],
                'basins_initial': int(ts['n_basins'][0]),
                'basins_final': int(ts['n_basins'][-1]),
                'rho_std_initial': enh[0]['rho_std'],
                'rho_std_final': enh[-1]['rho_std'],
            })
            print(f"    alpha={alpha:.2f}: peaks {enh[0]['n_peaks']}->{enh[-1]['n_peaks']}, "
                  f"rho_std {enh[0]['rho_std']:.3f}->{enh[-1]['rho_std']:.3f}")

    all_results['5b_bifurcation'] = bifurc_results

    # ========================================================
    # Save all results
    # ========================================================
    # Save JSON-serializable version
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
        return obj

    results_path = os.path.join(output_dir, "emergent_phenomena_results.json")
    with open(results_path, 'w') as f:
        json.dump(make_serializable(all_results), f, indent=2, default=str)

    elapsed_total = time.time() - t_total
    print(f"\n{'='*70}")
    print(f"  All experiments complete in {elapsed_total:.1f}s")
    print(f"  Results saved to {results_path}")
    print(f"{'='*70}")

    return all_results


if __name__ == "__main__":
    output_dir = os.path.join(os.path.dirname(__file__), "results")
    run_all_experiments(output_dir=output_dir)
