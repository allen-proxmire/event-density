"""
ED-Phys-12: Redesigning the Relational Penalty
================================================
Tests alternative relational penalty forms that:
 - preserve ED ontology (event density + participation channels),
 - remain concave / stabilizing at high density,
 - avoid the rho^(gamma-1) singularity at low density,
 - may support stronger participation flows.

Three penalty modes:
 - canonical: P(rho) = alpha * gamma * rho^(gamma-1)           [original]
 - soft_floor: P(rho) = alpha * gamma * (rho + rho_0)^(gamma-1)  [tamed singularity]
 - symmetric: P(rho) = alpha * gamma * (rho - rho_star) / (rho + rho_0)  [swing around rho*]

Canonical sources: ED-5, ED-12, ED-12.5, ED-Phys-01 through ED-Phys-11.
"""

import sys
import os
import io
import time
import json
import numpy as np

# Force UTF-8 output on Windows
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
# Penalty functions
# ============================================================

def penalty_canonical(rho, alpha, gamma, eps=1e-10):
    """Canonical penalty: alpha * gamma * rho^(gamma-1).

    Derived from f(rho) = rho^gamma => f'(rho) = gamma * rho^(gamma-1).
    The PDE term is -alpha * f'(rho) = -alpha * gamma * rho^(gamma-1).

    Singularity: as rho -> 0, rho^(gamma-1) -> infinity for gamma < 1.
    """
    rho_safe = np.maximum(rho, eps)
    return alpha * gamma * rho_safe ** (gamma - 1.0)


def penalty_soft_floor(rho, alpha, gamma, rho_0=0.5, eps=1e-10):
    """Soft-floor penalty: alpha * gamma * (rho + rho_0)^(gamma-1).

    Derived from f(rho) = (rho + rho_0)^gamma.
    The shifted argument removes the singularity at rho=0:
      at rho=0: P = alpha * gamma * rho_0^(gamma-1) = finite.

    Properties:
    - Concave for all rho >= 0 (same gamma < 1 concavity)
    - Monotonically decreasing (same qualitative behavior as canonical)
    - At high rho: (rho + rho_0)^(gamma-1) ~ rho^(gamma-1) [recovers canonical]
    - At low rho: saturates to rho_0^(gamma-1) [finite floor]

    The soft-floor density rho_0 controls the transition:
    - rho >> rho_0: canonical behavior
    - rho << rho_0: saturated penalty (no runaway depletion)
    """
    rho_safe = np.maximum(rho, eps)
    return alpha * gamma * (rho_safe + rho_0) ** (gamma - 1.0)


def penalty_symmetric(rho, alpha, gamma, rho_star=5.0, rho_0=0.5, eps=1e-10):
    """Symmetric participation penalty:
    P(rho) = alpha * gamma * (rho - rho_star) / (rho + rho_0).

    This penalty:
    - Is ZERO at rho = rho_star (equilibrium density)
    - Is NEGATIVE for rho < rho_star (drives rho UP toward rho_star)
    - Is POSITIVE for rho > rho_star (drives rho DOWN toward rho_star)
    - Saturates as rho -> infinity: P -> alpha * gamma
    - Is bounded at rho=0: P(0) = -alpha * gamma * rho_star / rho_0

    Properties:
    - No singularity at rho=0
    - Creates a restoring force toward rho_star
    - Participation channels can "swing" above and below rho_star
    - Still sublinear growth at high rho (bounded penalty)
    - The factor alpha*gamma scales the overall strength

    Physical interpretation:
    - rho_star is the "natural participation density"
    - Channels below rho_star are under-participating and get boosted
    - Channels above rho_star are over-participating and get drained
    - The (rho + rho_0) denominator prevents runaway at low rho
    """
    rho_safe = np.maximum(rho, eps)
    return alpha * gamma * (rho_safe - rho_star) / (rho_safe + rho_0)


# ============================================================
# Unified simulator with penalty mode
# ============================================================

def simulate_penalty(
    params: EDParams,
    initial_rho: np.ndarray,
    penalty_mode: str = "canonical",
    rho_0: float = 0.5,
    rho_star: float = 5.0,
    snapshot_interval: int = 500,
    label: str = "",
) -> dict:
    """Simulate ED cosmology with configurable penalty.

    Parameters
    ----------
    penalty_mode : str
        One of "canonical", "soft_floor", "symmetric".
    rho_0 : float
        Soft-floor / denominator scale (for soft_floor and symmetric).
    rho_star : float
        Reference density (for symmetric only).
    """
    rho = initial_rho.copy().astype(np.float64)
    d = rho.ndim
    dx = params.dx
    eps = 1e-10
    alpha = params.alpha
    gamma = params.gamma_exp

    # CFL timestep
    M_max = params.M_0
    eta = params.cfl_safety * dx**2 / (2 * d * M_max) if M_max > 0 else 1.0

    # For symmetric mode, the penalty can be negative (boosting rho),
    # which may require a smaller timestep
    if penalty_mode == "symmetric":
        max_penalty = alpha * gamma * max(abs(rho_star / rho_0), 1.0)
        eta = min(eta, 0.1 / max(max_penalty, 1e-12))

    diagnostics = []
    blowup_step = None
    blowup_msg = ""

    for step in range(params.n_steps):
        # Safety check
        if step % 100 == 0:
            if np.any(np.isnan(rho)) or np.any(np.isinf(rho)):
                blowup_step = step
                blowup_msg = f"NaN/Inf in rho at step {step}"
                break
            if np.max(np.abs(rho)) > 1e8:
                blowup_step = step
                blowup_msg = f"rho blowup at step {step}: max={np.max(np.abs(rho)):.2e}"
                break

        # Record diagnostics
        if step % snapshot_interval == 0:
            rho_safe = np.maximum(rho, eps)
            grad_mag = discrete_grad_magnitude(rho_safe, dx, params.boundary, eps)

            # Compute penalty value for diagnostics
            if penalty_mode == "canonical":
                pen_val = penalty_canonical(rho, alpha, gamma, eps)
            elif penalty_mode == "soft_floor":
                pen_val = penalty_soft_floor(rho, alpha, gamma, rho_0, eps)
            elif penalty_mode == "symmetric":
                pen_val = penalty_symmetric(rho, alpha, gamma, rho_star, rho_0, eps)
            else:
                pen_val = np.zeros_like(rho)

            diag = {
                'step': step,
                'rho_mean': float(np.mean(rho)),
                'rho_max': float(np.max(rho)),
                'rho_min': float(np.min(rho)),
                'rho_std': float(np.std(rho)),
                'grad_mean': float(np.mean(grad_mag)),
                'penalty_mean': float(np.mean(pen_val)),
                'penalty_max': float(np.max(pen_val)),
                'penalty_min': float(np.min(pen_val)),
            }

            # Count peaks and basins (1D)
            if rho.ndim == 1:
                n_peaks = 0
                peak_positions = []
                rho_mean_val = np.mean(rho)
                for i in range(1, len(rho)-1):
                    if rho[i] > rho[i-1] and rho[i] > rho[i+1] and rho[i] > rho_mean_val + 0.5*np.std(rho):
                        n_peaks += 1
                        peak_positions.append(i)
                diag['n_peaks'] = n_peaks
                diag['peak_positions'] = peak_positions[:10]

                # Count basins
                n_basins = 0
                for i in range(1, len(rho)-1):
                    if rho[i] < rho[i-1] and rho[i] < rho[i+1]:
                        n_basins += 1
                diag['n_basins'] = n_basins

                # Horizon fraction (rho > 0.95 * rho_max)
                diag['horizon_frac'] = float(np.mean(rho > 0.95 * params.rho_max))

            diagnostics.append(diag)

        # Compute RHS
        rho_safe = np.maximum(rho, eps)
        lap = discrete_laplacian(rho_safe, dx, params.boundary, eps)
        grad_sq = discrete_grad_squared(rho_safe, dx, params.boundary, eps)
        M = mobility(rho_safe, params.M_0, params.rho_max, params.n_mob)
        Mprime = mobility_derivative(rho_safe, params.M_0, params.rho_max, params.n_mob)

        diffusion = M * lap + Mprime * grad_sq

        if penalty_mode == "canonical":
            pen = penalty_canonical(rho_safe, alpha, gamma, eps)
        elif penalty_mode == "soft_floor":
            pen = penalty_soft_floor(rho_safe, alpha, gamma, rho_0, eps)
        elif penalty_mode == "symmetric":
            pen = penalty_symmetric(rho_safe, alpha, gamma, rho_star, rho_0, eps)
        else:
            raise ValueError(f"Unknown penalty mode: {penalty_mode}")

        drho = diffusion - pen
        rho_new = rho + eta * drho

        # Positivity enforcement
        rho_new = np.maximum(rho_new, 0.0)

        rho = rho_new

    # Final snapshot
    rho_safe = np.maximum(rho, eps)
    grad_mag = discrete_grad_magnitude(rho_safe, dx, params.boundary, eps)
    if penalty_mode == "canonical":
        pen_val = penalty_canonical(rho, alpha, gamma, eps)
    elif penalty_mode == "soft_floor":
        pen_val = penalty_soft_floor(rho, alpha, gamma, rho_0, eps)
    else:
        pen_val = penalty_symmetric(rho, alpha, gamma, rho_star, rho_0, eps)

    final = {
        'step': step if blowup_step is None else blowup_step,
        'rho_mean': float(np.mean(rho)),
        'rho_max': float(np.max(rho)),
        'rho_min': float(np.min(rho)),
        'rho_std': float(np.std(rho)),
        'grad_mean': float(np.mean(grad_mag)),
        'penalty_mean': float(np.mean(pen_val)),
        'penalty_max': float(np.max(pen_val)),
        'penalty_min': float(np.min(pen_val)),
    }
    if rho.ndim == 1:
        n_peaks = 0
        peak_positions = []
        rho_mean_val = np.mean(rho)
        for i in range(1, len(rho)-1):
            if rho[i] > rho[i-1] and rho[i] > rho[i+1] and rho[i] > rho_mean_val + 0.5*np.std(rho):
                n_peaks += 1
                peak_positions.append(i)
        final['n_peaks'] = n_peaks
        final['peak_positions'] = peak_positions[:10]
        n_basins = 0
        for i in range(1, len(rho)-1):
            if rho[i] < rho[i-1] and rho[i] < rho[i+1]:
                n_basins += 1
        final['n_basins'] = n_basins
        final['horizon_frac'] = float(np.mean(rho > 0.95 * params.rho_max))

    return {
        'eta_used': eta,
        'blowup_step': blowup_step,
        'blowup_msg': blowup_msg,
        'diagnostics': diagnostics,
        'final': final,
        'rho_final': rho,
    }


# ============================================================
# Experiment runner
# ============================================================
# IMPORTANT: Use rho_mean ~ 50 for ICs (matching the canonical pipeline).
# At rho~50, the penalty is 0.1*0.5*50^(-0.5) = 0.0071 per time unit.
# With eta~0.2, drho/step ~ -0.0014. Over 20K steps: drain ~ 28.
# This keeps density alive throughout the simulation.
# For symmetric penalty, rho_star should be comparable to rho_mean.

def run_penalty_experiments(output_dir="results"):
    os.makedirs(output_dir, exist_ok=True)
    all_results = {}
    t_total = time.time()

    # Build configuration list
    configs = []
    configs.append(("canonical", {}))
    for r0 in [0.1, 0.5, 2.0, 5.0]:
        configs.append(("soft_floor", {'rho_0': r0}))
    for rs in [20.0, 40.0, 50.0]:
        configs.append(("symmetric", {'rho_0': 1.0, 'rho_star': rs}))

    # ========================================================
    # EXP 1: Homogeneous Validation (rho=50)
    # ========================================================
    print("\n>>> EXP 1: Homogeneous Validation (1D, N=256, 5K steps)")
    exp1 = []
    for mode in ["canonical", "soft_floor", "symmetric"]:
        if mode == "soft_floor":
            extras = {'rho_0': 0.5}
        elif mode == "symmetric":
            extras = {'rho_0': 1.0, 'rho_star': 50.0}
        else:
            extras = {}

        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=1, N=256, dx=1.0, cfl_safety=0.4,
            n_steps=5000, record_interval=100, boundary="periodic",
        )
        rho0 = np.full(256, 50.0)
        t0 = time.time()
        result = simulate_penalty(p, rho0, penalty_mode=mode,
                                   snapshot_interval=100, label=f"homo_{mode}", **extras)
        elapsed = time.time() - t0

        entry = {
            'mode': mode, **extras,
            'elapsed_s': round(elapsed, 1),
            'rho_mean_initial': 50.0,
            'rho_mean_final': result['final']['rho_mean'],
            'rho_std_final': result['final']['rho_std'],
            'penalty_mean_final': result['final']['penalty_mean'],
        }
        exp1.append(entry)
        print(f"  {mode}: rho {50.0:.1f}->{result['final']['rho_mean']:.4f} "
              f"P_mean={result['final']['penalty_mean']:.4f}")

    all_results['exp1_homogeneous'] = exp1

    # ========================================================
    # EXP 2: Peak Test (1D, N=512, 20K steps)
    # ========================================================
    print("\n>>> EXP 2: Peak Test -- Gaussian on rho=50 background (1D)")
    exp2 = []
    x = np.arange(512, dtype=np.float64)

    for mode, extras in configs:
        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=1, N=512, dx=1.0, cfl_safety=0.4,
            n_steps=20000, record_interval=200, boundary="periodic",
        )
        rho0 = 50.0 + 25.0 * np.exp(-(x - 256)**2 / (2 * 20**2))

        t0 = time.time()
        result = simulate_penalty(p, rho0, penalty_mode=mode,
                                   snapshot_interval=200, label=f"peak_{mode}", **extras)
        elapsed = time.time() - t0

        diags = result['diagnostics']
        heights = [d['rho_max'] for d in diags]
        backgrounds = [d['rho_min'] for d in diags]

        # Height above background over time
        contrast_series = [h - b for h, b in zip(heights, backgrounds)]
        n_osc = 0
        for i in range(1, len(contrast_series)-1):
            if contrast_series[i] > contrast_series[i-1] and contrast_series[i] > contrast_series[i+1]:
                n_osc += 1

        entry = {
            'mode': mode, **extras,
            'elapsed_s': round(elapsed, 1),
            'blowup': result['blowup_step'],
            'peak_height_initial': heights[0] if heights else 0,
            'peak_height_final': result['final']['rho_max'],
            'background_initial': backgrounds[0] if backgrounds else 0,
            'background_final': result['final']['rho_min'],
            'contrast_initial': contrast_series[0] if contrast_series else 0,
            'contrast_final': contrast_series[-1] if contrast_series else 0,
            'n_peaks_final': result['final'].get('n_peaks', 0),
            'contrast_oscillations': n_osc,
        }
        exp2.append(entry)
        status = "BLOWUP" if result['blowup_step'] else "ok"
        print(f"  {mode}({extras}): {status} ({elapsed:.1f}s) "
              f"peak={heights[0]:.1f}->{result['final']['rho_max']:.2f} "
              f"bg={backgrounds[0]:.2f}->{result['final']['rho_min']:.4f} "
              f"contrast={contrast_series[0]:.1f}->{contrast_series[-1]:.2f} osc={n_osc}")

    all_results['exp2_peak'] = exp2

    # ========================================================
    # EXP 3: Horizon Test (1D, N=512, 20K steps)
    # ========================================================
    print("\n>>> EXP 3: Horizon Test -- near-rho_max region (1D)")
    exp3 = []
    for mode, extras in configs:
        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=1, N=512, dx=1.0, cfl_safety=0.4,
            n_steps=20000, record_interval=200, boundary="periodic",
        )
        rho0 = 50.0 * np.ones(512)
        rho0[200:312] = 95.0

        t0 = time.time()
        result = simulate_penalty(p, rho0, penalty_mode=mode,
                                   snapshot_interval=200, label=f"horiz_{mode}", **extras)
        elapsed = time.time() - t0

        diags = result['diagnostics']
        horizon_series = [d.get('horizon_frac', 0) for d in diags]

        entry = {
            'mode': mode, **extras,
            'elapsed_s': round(elapsed, 1),
            'blowup': result['blowup_step'],
            'rho_max_initial': 95.0,
            'rho_max_final': result['final']['rho_max'],
            'horizon_frac_initial': horizon_series[0] if horizon_series else 0,
            'horizon_frac_final': result['final'].get('horizon_frac', 0),
            'background_final': result['final']['rho_min'],
        }
        exp3.append(entry)
        status = "BLOWUP" if result['blowup_step'] else "ok"
        print(f"  {mode}({extras}): {status} ({elapsed:.1f}s) "
              f"rho_max=95->{result['final']['rho_max']:.2f} "
              f"H_frac={horizon_series[0]:.3f}->{result['final'].get('horizon_frac',0):.4f} "
              f"bg={result['final']['rho_min']:.4f}")

    all_results['exp3_horizon'] = exp3

    # ========================================================
    # EXP 4: Flow Test -- two peaks (1D, N=512, 20K steps)
    # ========================================================
    print("\n>>> EXP 4: Flow Test -- two peaks on rho=50 background (1D)")
    exp4 = []
    for mode, extras in configs:
        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=1, N=512, dx=1.0, cfl_safety=0.4,
            n_steps=20000, record_interval=200, boundary="periodic",
        )
        rho0 = 50.0 + 20.0*np.exp(-(x-179)**2/(2*15**2)) + 20.0*np.exp(-(x-332)**2/(2*15**2))

        t0 = time.time()
        result = simulate_penalty(p, rho0, penalty_mode=mode,
                                   snapshot_interval=200, label=f"flow_{mode}", **extras)
        elapsed = time.time() - t0

        diags = result['diagnostics']
        init_pp = diags[0].get('peak_positions', []) if diags else []
        final_pp = result['final'].get('peak_positions', [])
        init_sep = abs(init_pp[1] - init_pp[0]) if len(init_pp) >= 2 else 0
        final_sep = abs(final_pp[1] - final_pp[0]) if len(final_pp) >= 2 else 0

        # Valley density
        mid = 256
        valley_init = float(rho0[mid])
        valley_final = float(result['rho_final'][mid])

        entry = {
            'mode': mode, **extras,
            'elapsed_s': round(elapsed, 1),
            'blowup': result['blowup_step'],
            'peaks_initial': diags[0].get('n_peaks', 0) if diags else 0,
            'peaks_final': result['final'].get('n_peaks', 0),
            'sep_initial': init_sep,
            'sep_final': final_sep,
            'sep_change': final_sep - init_sep if init_sep > 0 and final_sep > 0 else None,
            'valley_initial': round(valley_init, 2),
            'valley_final': round(valley_final, 4),
        }
        exp4.append(entry)
        status = "BLOWUP" if result['blowup_step'] else "ok"
        sc = f"sep={init_sep}->{final_sep}" if init_sep > 0 else "peaks lost"
        print(f"  {mode}({extras}): {status} ({elapsed:.1f}s) {sc} "
              f"valley={valley_init:.1f}->{valley_final:.4f}")

    all_results['exp4_flow'] = exp4

    # ========================================================
    # EXP 5: Cosmology Test (1D, N=512, 20K steps)
    # ========================================================
    print("\n>>> EXP 5: Cosmology Test -- random IC rho in [20,80] (1D)")
    exp5 = []
    np.random.seed(42)
    rho0_cosmo = np.random.uniform(20.0, 80.0, 512).astype(np.float64)

    for mode, extras in configs:
        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=1, N=512, dx=1.0, cfl_safety=0.4,
            n_steps=20000, record_interval=200, boundary="periodic",
        )
        t0 = time.time()
        result = simulate_penalty(p, rho0_cosmo.copy(), penalty_mode=mode,
                                   snapshot_interval=200, label=f"cosmo_{mode}", **extras)
        elapsed = time.time() - t0

        diags = result['diagnostics']
        grad_series = [(d['step'], d['grad_mean']) for d in diags if d['grad_mean'] > 1e-6]
        lambda_1 = 0.0
        r_squared = 0.0
        if len(grad_series) > 5:
            steps_arr = np.array([g[0] for g in grad_series])
            grads_arr = np.array([g[1] for g in grad_series])
            log_grads = np.log(grads_arr + 1e-20)
            if len(steps_arr) > 2:
                coeffs = np.polyfit(steps_arr, log_grads, 1)
                lambda_1 = -coeffs[0]
                predicted = np.polyval(coeffs, steps_arr)
                ss_res = np.sum((log_grads - predicted)**2)
                ss_tot = np.sum((log_grads - np.mean(log_grads))**2)
                r_squared = 1 - ss_res / max(ss_tot, 1e-20)

        basins_i = diags[0].get('n_basins', 0) if diags else 0
        basins_f = result['final'].get('n_basins', 0)

        entry = {
            'mode': mode, **extras,
            'elapsed_s': round(elapsed, 1),
            'blowup': result['blowup_step'],
            'lambda_1': round(lambda_1, 6),
            'r_squared': round(r_squared, 4),
            'basins_initial': basins_i,
            'basins_final': basins_f,
            'rho_mean_final': result['final']['rho_mean'],
            'rho_std_final': result['final']['rho_std'],
            'rho_min_final': result['final']['rho_min'],
            'rho_max_final': result['final']['rho_max'],
            'peaks_final': result['final'].get('n_peaks', 0),
        }
        exp5.append(entry)
        status = "BLOWUP" if result['blowup_step'] else "ok"
        print(f"  {mode}({extras}): {status} ({elapsed:.1f}s) lam1={lambda_1:.6f} R2={r_squared:.4f} "
              f"basins={basins_i}->{basins_f} rho=[{result['final']['rho_min']:.2f},{result['final']['rho_max']:.2f}]")

    all_results['exp5_cosmology'] = exp5

    # ========================================================
    # EXP 6: Low-density Depletion Test
    # ========================================================
    print("\n>>> EXP 6: Low-density Depletion Test (1D, N=256, 2K steps)")
    exp6 = []
    for mode in ["canonical", "soft_floor", "symmetric"]:
        if mode == "soft_floor":
            extras_list = [{'rho_0': r0} for r0 in [0.1, 0.5, 2.0]]
        elif mode == "symmetric":
            extras_list = [{'rho_0': 1.0, 'rho_star': 5.0}]
        else:
            extras_list = [{}]

        for extras in extras_list:
            p = EDParams(
                alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
                dimensions=1, N=256, dx=1.0, cfl_safety=0.4,
                n_steps=2000, record_interval=50, boundary="periodic",
            )
            rho0 = np.full(256, 1.0)

            t0 = time.time()
            result = simulate_penalty(p, rho0, penalty_mode=mode,
                                       snapshot_interval=50, label=f"depl_{mode}", **extras)
            elapsed = time.time() - t0

            # Track rho_mean over time
            rho_mean_series = [d['rho_mean'] for d in result['diagnostics']]

            entry = {
                'mode': mode, **extras,
                'elapsed_s': round(elapsed, 1),
                'rho_mean_initial': 1.0,
                'rho_mean_final': result['final']['rho_mean'],
                'penalty_mean_final': result['final']['penalty_mean'],
                'rho_mean_at_500': rho_mean_series[10] if len(rho_mean_series) > 10 else None,
                'rho_mean_at_1000': rho_mean_series[20] if len(rho_mean_series) > 20 else None,
            }
            exp6.append(entry)
            print(f"  {mode}({extras}): rho={1.0:.1f}->{result['final']['rho_mean']:.6f} "
                  f"P_mean={result['final']['penalty_mean']:.4f}")

    all_results['exp6_depletion'] = exp6

    # ========================================================
    # EXP 7: 2D Cosmology Test (128x128, 5K steps)
    # ========================================================
    print("\n>>> EXP 7: 2D Cosmology Test (128x128, 5K steps)")
    exp7 = []
    np.random.seed(77)
    rho0_2d = np.random.uniform(20.0, 80.0, (128, 128)).astype(np.float64)

    for mode in ["canonical", "soft_floor", "symmetric"]:
        if mode == "soft_floor":
            extras = {'rho_0': 0.5}
        elif mode == "symmetric":
            extras = {'rho_0': 1.0, 'rho_star': 50.0}
        else:
            extras = {}

        p = EDParams(
            alpha=0.1, gamma_exp=0.5, M_0=1.0, rho_max=100.0, n_mob=2,
            dimensions=2, N=128, dx=1.0, cfl_safety=0.4,
            n_steps=5000, record_interval=500, boundary="periodic",
        )
        t0 = time.time()
        result = simulate_penalty(p, rho0_2d.copy(), penalty_mode=mode,
                                   snapshot_interval=500, label=f"2d_{mode}", **extras)
        elapsed = time.time() - t0

        entry = {
            'mode': mode, **extras,
            'elapsed_s': round(elapsed, 1),
            'rho_mean_final': result['final']['rho_mean'],
            'rho_max_final': result['final']['rho_max'],
            'rho_min_final': result['final']['rho_min'],
            'rho_std_final': result['final']['rho_std'],
        }
        exp7.append(entry)
        print(f"  {mode}: rho=[{result['final']['rho_min']:.2f},{result['final']['rho_max']:.2f}] "
              f"std={result['final']['rho_std']:.4f} mean={result['final']['rho_mean']:.2f}")

        if result['blowup_step'] is None:
            np.save(os.path.join(output_dir, f"2d_{mode}_rho.npy"), result['rho_final'])

    all_results['exp7_2d_cosmology'] = exp7

    # ========================================================
    # Save results
    # ========================================================
    elapsed_total = time.time() - t_total
    results_path = os.path.join(output_dir, "penalty_results.json")
    with open(results_path, 'w') as f:
        json.dump(all_results, f, indent=2, default=str)

    print(f"\n{'='*70}")
    print(f"  All ED-Phys-12 experiments complete in {elapsed_total:.1f}s")
    print(f"  Results saved to {os.path.abspath(results_path)}")
    print(f"{'='*70}")


if __name__ == "__main__":
    print("=" * 70)
    print("  ED-Phys-12: Redesigning the Relational Penalty")
    print("=" * 70)
    output_dir = os.path.join(os.path.dirname(__file__), "results")
    run_penalty_experiments(output_dir=output_dir)
