"""Ray-forced Monte Carlo for the ED-SC 2.0 r* arc.

Adds a Gaussian-ridge forcing term F(x,y) to the Scenario-D SPDE to seed
a ray-like motif near delta_nat = sqrt(6), then turns F off and samples
stationary points during noisy relaxation. Full pre-registered motif
filter is imported unchanged from r_star_montecarlo.
"""
import json
import sys
import numpy as np
from numpy.fft import fft2, ifft2

import r_star_montecarlo as mc


# -------- Forcing -------------------------------------------------------

def make_forcing(L, x0, y0, A, sigma_x, sigma_y):
    """Quadrupolar forcing that seeds a clean saddle at (x0, y0).

    F(x,y) = A * (xt^2/sigma_x^2 - yt^2/sigma_y^2) * exp(-(xt^2+yt^2)/(2*sigma^2))
    with sigma = min(sigma_x, sigma_y). A single-ridge Gaussian creates a
    local MAXIMUM, not a saddle, so the pre-registered filter (which
    requires kappa_par * kappa_perp < 0) would reject it by construction.
    The quadrupolar form has F=0 at centre, positive-curvature lobes
    along x-axis and negative-curvature lobes along y-axis (or vice versa
    depending on sign of A), producing a Morse saddle at (x0, y0) in the
    steady-state response.
    """
    xs = np.arange(L).reshape(-1, 1)
    ys = np.arange(L).reshape(1, -1)
    xt = xs - x0
    yt = ys - y0
    sigma = min(sigma_x, sigma_y)
    env = np.exp(-(xt**2 + yt**2) / (2 * sigma**2))
    return A * (xt**2 / sigma_x**2 - yt**2 / sigma_y**2) * env


# -------- Forced IMEX step ---------------------------------------------

def imex_step_forced(delta, dt, lap_sym, rng, F, sigma):
    """One IMEX step with explicit forcing term F added to source."""
    explicit = -(mc.P3 / 6.0) * delta**3 + F
    noise_amp = np.sqrt(2 * sigma**2 * dt / mc.DX**2)
    xi = noise_amp * rng.standard_normal(delta.shape)
    src = delta + dt * explicit + xi
    src_hat = fft2(src)
    denom = 1.0 - dt * (mc.M0 * lap_sym - mc.P0)
    delta_new_hat = src_hat / denom
    return np.real(ifft2(delta_new_hat))


# -------- Amplitude pre-sweep -------------------------------------------

def calibrate_amplitude(A_candidates, sigma_x, sigma_y, L, x0, y0, dt, n_steps=200):
    """Deterministic (no noise) calibration: run forced SPDE and report
    delta(x0,y0) at the end. Return table."""
    lap_sym = mc.fft_laplacian_symbol(L, mc.DX)
    results = []
    for A in A_candidates:
        F = make_forcing(L, x0, y0, A, sigma_x, sigma_y)
        delta = 0.01 * np.random.default_rng(0).standard_normal((L, L))
        for _ in range(n_steps):
            explicit = -(mc.P3 / 6.0) * delta**3 + F
            src = delta + dt * explicit  # no noise
            src_hat = fft2(src)
            denom = 1.0 - dt * (mc.M0 * lap_sym - mc.P0)
            delta = np.real(ifft2(src_hat / denom))
        d_centre = float(delta[int(x0), int(y0)])
        d_max = float(np.max(delta))
        results.append({'A': A, 'd_centre': d_centre, 'd_max': d_max})
    return results


# -------- Run one realisation -------------------------------------------

def run_realisation(seed, sigma, A, sigma_x, sigma_y,
                    T_seed=300, T_relax=800, T_burn=100, snap_every=20,
                    record_primary_radius=4.0):
    rng = np.random.default_rng(seed)
    L = mc.L
    lap_sym = mc.fft_laplacian_symbol(L, mc.DX)
    x0, y0 = L // 2, L // 2
    F = make_forcing(L, x0, y0, A, sigma_x, sigma_y)
    Fzero = np.zeros_like(F)

    # IC: tiny isotropic noise
    delta = 0.01 * rng.standard_normal((L, L))

    # Phase 1: seed with forcing ON + noise
    for _ in range(T_seed):
        delta = imex_step_forced(delta, mc.DT, lap_sym, rng, F, sigma)

    d_at_end_of_seed = float(delta[x0, y0])
    d_max_after_seed = float(np.max(np.abs(delta)))

    # Phase 2: relax with forcing OFF + noise
    records = []
    for step in range(T_relax):
        delta = imex_step_forced(delta, mc.DT, lap_sym, rng, Fzero, sigma)
        if step >= T_burn and (step - T_burn) % snap_every == 0:
            # Detect stationary points + apply filter
            sp = mc.detect_stationary_points(delta)
            for (xsp, ysp, i, j) in sp:
                K = mc.compute_hessian(delta, i, j)
                evals, evecs = np.linalg.eigh(K)
                order = np.argsort(-np.abs(evals))
                kpar = float(evals[order[0]])
                kperp = float(evals[order[1]])
                kpar_vec = evecs[:, order[0]]
                if kpar * kperp >= 0:
                    continue
                accept, diag = mc.motif_filter_check(delta, xsp, ysp, i, j, K, kpar_vec)
                if not accept:
                    continue
                d_pt = float(diag['d_pt'])
                mu = mc.M0 + 0.5 * mc.M2 * d_pt**2
                chi = 2 * mu * kperp**2 / mc.P0
                denom = 2 * chi - 1
                rstar = -2 * chi / denom if abs(denom) > 1e-3 else float('nan')
                # distance to seed centre (with periodic wrap)
                dx = (xsp - x0) % L; dx = dx if dx <= L/2 else dx - L
                dy = (ysp - y0) % L; dy = dy if dy <= L/2 else dy - L
                r_from_seed = float(np.sqrt(dx**2 + dy**2))
                records.append({
                    'step': step, 'seed': seed,
                    'x0': float(xsp), 'y0': float(ysp),
                    'd_pt': d_pt,
                    'kappa_par': kpar, 'kappa_perp': kperp, 's': kpar/kperp,
                    'mu': float(mu), 'chi': float(chi), 'r_star_pt': float(rstar),
                    'L_maj': float(diag['L_maj']), 'aspect': float(diag['aspect']),
                    'r_from_seed': r_from_seed,
                    'is_primary': bool(r_from_seed <= record_primary_radius),
                })
    return records, d_at_end_of_seed, d_max_after_seed


# -------- Aggregation --------------------------------------------------

def summarise(records, label, n_real):
    out = {'label': label, 'n_realisations': n_real, 'n_motifs_total': len(records)}
    if not records:
        return out
    by_seed = {}
    for r in records:
        by_seed.setdefault(r['seed'], []).append(r)
    per_real = []
    for s, recs in by_seed.items():
        primary = [r for r in recs if r['is_primary']]
        per_real.append({
            'seed': s,
            'n_motifs': len(recs),
            'n_primary': len(primary),
            'kperp_med': float(np.median([abs(r['kappa_perp']) for r in recs])),
            's_med': float(np.median([r['s'] for r in recs])),
            'rstar_med': float(np.nanmedian([r['r_star_pt'] for r in recs])),
            'd_med': float(np.median([r['d_pt'] for r in recs])),
            'kperp_med_primary': float(np.median([abs(r['kappa_perp']) for r in primary])) if primary else None,
            's_med_primary': float(np.median([r['s'] for r in primary])) if primary else None,
            'rstar_med_primary': float(np.nanmedian([r['r_star_pt'] for r in primary])) if primary else None,
        })
    out['per_realisation'] = per_real

    def pool(key, filter_primary=False):
        if filter_primary:
            vals = [r[key] for r in records if r['is_primary']]
        else:
            vals = [r[key] for r in records]
        vals = [v for v in vals if np.isfinite(v)]
        if not vals: return None
        return {
            'n': len(vals),
            'median': float(np.median(vals)),
            'iqr': [float(np.quantile(vals, .25)), float(np.quantile(vals, .75))],
        }
    out['pooled_all'] = {
        'kappa_perp_abs': pool_abs(records, 'kappa_perp', False),
        's': pool(key='s'),
        'r_star_pt': pool(key='r_star_pt'),
        'd_pt': pool(key='d_pt'),
    }
    out['pooled_primary'] = {
        'kappa_perp_abs': pool_abs(records, 'kappa_perp', True),
        's': pool(key='s', filter_primary=True),
        'r_star_pt': pool(key='r_star_pt', filter_primary=True),
        'd_pt': pool(key='d_pt', filter_primary=True),
    }

    # Bootstrap over realisations — primary-saddle medians
    reals_primary = [p for p in per_real if p['n_primary'] > 0]
    if len(reals_primary) >= 3:
        rng = np.random.default_rng(99)
        B = 2000
        def bs(key):
            vals = np.array([p[key] for p in reals_primary])
            meds = [np.median(rng.choice(vals, size=len(vals), replace=True)) for _ in range(B)]
            return [float(np.quantile(meds, .025)), float(np.median(vals)), float(np.quantile(meds, .975))]
        out['bootstrap95_primary'] = {
            'kappa_perp': bs('kperp_med_primary'),
            's': bs('s_med_primary'),
            'r_star': bs('rstar_med_primary'),
        }
    return out


def pool_abs(records, key, filter_primary):
    if filter_primary:
        vals = [abs(r[key]) for r in records if r['is_primary']]
    else:
        vals = [abs(r[key]) for r in records]
    vals = [v for v in vals if np.isfinite(v)]
    if not vals: return None
    return {
        'n': len(vals),
        'median': float(np.median(vals)),
        'iqr': [float(np.quantile(vals, .25)), float(np.quantile(vals, .75))],
    }


# -------- Main ---------------------------------------------------------

def main():
    L = mc.L
    x0 = y0 = L // 2
    dt = mc.DT
    # Quadrupole widths: sigma_x and sigma_y control principal-curvature scales
    # at the saddle centre. Pick equal for s = -1 lead-order (matches Anisotropy
    # memo); unequal tunes s away from -1.
    sigma_x = 3.0
    sigma_y = 3.0

    # 0. Amplitude calibration pre-sweep (deterministic, no noise).
    # For quadrupole, d_centre = 0 by symmetry; report d_max and d_min instead
    # (which give signed curvature magnitudes of the induced saddle's lobes).
    print("[calibration] deterministic forced steady state:", file=sys.stderr)
    calib = calibrate_amplitude([0.25, 0.5, 1.0, 1.5, 2.0], sigma_x, sigma_y,
                                 L, x0, y0, dt, n_steps=200)
    for c in calib:
        print(f"    A={c['A']:.2f}  d_centre={c['d_centre']:.3f}  d_max={c['d_max']:.3f}",
              file=sys.stderr)

    # Pick largest stable A (d_max finite). Goal: d_max close to sqrt(6) = 2.449
    # but without blowup.
    stable = [c for c in calib if np.isfinite(c['d_max']) and c['d_max'] < 5.0]
    target = np.sqrt(6.0)
    Astar = min(stable, key=lambda c: abs(c['d_max'] - target))['A'] if stable else 0.5
    print(f"[calibration] selected A = {Astar} (target sqrt(6) = {target:.3f})", file=sys.stderr)

    # 1. Main ray-forced runs — primary sigma 0.20, 10 realisations
    primary_sigma = 0.20
    seeds = [77, 123, 456, 789, 1011, 1213, 1415, 1617, 1819, 2021]

    all_results = []
    # Primary config
    print(f"[main] sigma={primary_sigma}  A={Astar}", file=sys.stderr)
    records = []
    seed_diagnostics = []
    for s in seeds:
        recs, d_end_seed, d_max_after = run_realisation(
            s, primary_sigma, Astar, sigma_x, sigma_y,
            T_seed=300, T_relax=800, T_burn=100, snap_every=20)
        records.extend(recs)
        seed_diagnostics.append({
            'seed': s, 'd_centre_end_seed': d_end_seed,
            'd_max_after_seed': d_max_after, 'n_motifs': len(recs),
            'n_primary': sum(1 for r in recs if r['is_primary']),
        })
        print(f"    seed={s} d_seed_end={d_end_seed:.3f} d_max={d_max_after:.3f} "
              f"n={len(recs)} n_primary={sum(1 for r in recs if r['is_primary'])}",
              file=sys.stderr)
    summary = summarise(records, f'primary_sigma{primary_sigma}', len(seeds))
    summary['A'] = Astar
    summary['sigma_x'] = sigma_x
    summary['sigma_y'] = sigma_y
    summary['sigma'] = primary_sigma
    summary['seed_diagnostics'] = seed_diagnostics
    all_results.append(summary)

    # 2. Sigma sweep — 5 realisations each at {0.05, 0.10, 0.40}
    for sigma in [0.05, 0.10, 0.40]:
        print(f"[sweep] sigma={sigma}", file=sys.stderr)
        records = []
        seed_diag = []
        for s in seeds[:5]:
            recs, d_end_seed, d_max_after = run_realisation(
                s, sigma, Astar, sigma_x, sigma_y,
                T_seed=300, T_relax=800, T_burn=100, snap_every=20)
            records.extend(recs)
            seed_diag.append({'seed': s, 'd_centre_end_seed': d_end_seed,
                              'd_max_after_seed': d_max_after, 'n_motifs': len(recs)})
            print(f"    sigma={sigma} seed={s} n={len(recs)}", file=sys.stderr)
        summ = summarise(records, f'sweep_sigma{sigma}', 5)
        summ['sigma'] = sigma
        summ['A'] = Astar
        summ['seed_diagnostics'] = seed_diag
        all_results.append(summ)

    output = {
        'parameters': {
            'L': L, 'DX': mc.DX, 'DT': mc.DT,
            'M0': mc.M0, 'M2': mc.M2, 'P0': mc.P0, 'P3': mc.P3,
            'A': Astar, 'sigma_x': sigma_x, 'sigma_y': sigma_y,
            'T_seed': 300, 'T_relax': 800, 'T_burn': 100, 'snap_every': 20,
            'filter': {
                'delta_thr': mc.DELTA_THR, 'alpha': mc.ALPHA, 'L_ray': mc.L_RAY,
                'aspect_min': mc.ASPECT_MIN, 'sym_thresh': mc.SYM_THRESH,
                'orient_tol_deg': mc.ORIENT_TOL_DEG,
            },
        },
        'calibration_table': calib,
        'configs': all_results,
    }
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
