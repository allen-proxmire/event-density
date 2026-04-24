"""Supplementary: quadrupolar forcing + NO motif filter — just saddle detection.

Rationale: the pre-registered ED-SC 2.0 filter rejects quadrupolar-seeded
saddles because they have delta ~ 0 at the centre (fails delta_thr=0.10 gate)
and/or the alpha-contour connected component around the saddle is empty
(fails cc_too_small gate). These failures are intrinsic to the filter's
implicit assumption that motifs are PEAK-LIKE (field high at centre), not
saddle-like. To recover quantitative measurements of (kappa_par, kappa_perp,
s, r*_pt) at quadrupole-seeded saddles, we must bypass the filter.

This script reuses the forcing + integrator from r_star_mc_rayforce but drops
the filter, accepting all kappa_par*kappa_perp<0 spatial saddles within
radius R_primary of the seed centre.
"""
import json
import sys
import numpy as np
import r_star_montecarlo as mc
import r_star_mc_rayforce as rf


def run_realisation_nofilter(seed, sigma, A, sigma_x, sigma_y,
                              T_seed=300, T_relax=800, T_burn=100,
                              snap_every=20, R_primary=4.0):
    rng = np.random.default_rng(seed)
    L = mc.L
    lap_sym = mc.fft_laplacian_symbol(L, mc.DX)
    x0, y0 = L // 2, L // 2
    F = rf.make_forcing(L, x0, y0, A, sigma_x, sigma_y)
    Fzero = np.zeros_like(F)

    delta = 0.01 * rng.standard_normal((L, L))

    for _ in range(T_seed):
        delta = rf.imex_step_forced(delta, mc.DT, lap_sym, rng, F, sigma)

    d_peak_end_seed = float(np.max(np.abs(delta)))

    primary_records = []
    all_records = []
    for step in range(T_relax):
        delta = rf.imex_step_forced(delta, mc.DT, lap_sym, rng, Fzero, sigma)
        if step >= T_burn and (step - T_burn) % snap_every == 0:
            sp = mc.detect_stationary_points(delta)
            for (xsp, ysp, i, j) in sp:
                K = mc.compute_hessian(delta, i, j)
                evals, evecs = np.linalg.eigh(K)
                order = np.argsort(-np.abs(evals))
                kpar = float(evals[order[0]])
                kperp = float(evals[order[1]])
                if kpar * kperp >= 0:
                    continue
                d_pt = float(mc.interpolate_delta(delta, xsp, ysp))
                chi = 2 * mc.M0 * kperp**2 / mc.P0
                denom = 2 * chi - 1
                rstar = -2 * chi / denom if abs(denom) > 1e-3 else float('nan')
                dx = (xsp - x0) % L; dx = dx if dx <= L/2 else dx - L
                dy = (ysp - y0) % L; dy = dy if dy <= L/2 else dy - L
                r_from_seed = float(np.sqrt(dx**2 + dy**2))
                rec = {
                    'step': step, 'seed': seed,
                    'x0': float(xsp), 'y0': float(ysp),
                    'd_pt': d_pt, 'kappa_par': kpar, 'kappa_perp': kperp,
                    's': kpar/kperp, 'chi': float(chi),
                    'r_star_pt': float(rstar), 'r_from_seed': r_from_seed,
                    'is_primary': bool(r_from_seed <= R_primary),
                }
                all_records.append(rec)
                if rec['is_primary']:
                    primary_records.append(rec)
    return all_records, primary_records, d_peak_end_seed


def summarise(records, label):
    out = {'label': label, 'n_total': len(records)}
    if not records:
        return out
    kperp = [abs(r['kappa_perp']) for r in records]
    svals = [r['s'] for r in records]
    rstar = [r['r_star_pt'] for r in records if np.isfinite(r['r_star_pt'])]
    d = [r['d_pt'] for r in records]
    chi = [r['chi'] for r in records]
    out['pooled'] = {
        'kappa_perp_abs_median': float(np.median(kperp)),
        'kappa_perp_abs_iqr': [float(np.quantile(kperp, .25)), float(np.quantile(kperp, .75))],
        's_median': float(np.median(svals)),
        's_iqr': [float(np.quantile(svals, .25)), float(np.quantile(svals, .75))],
        'r_star_median': float(np.median(rstar)) if rstar else None,
        'r_star_iqr': [float(np.quantile(rstar, .25)), float(np.quantile(rstar, .75))] if rstar else None,
        'd_pt_median': float(np.median(d)),
        'd_pt_iqr': [float(np.quantile(d, .25)), float(np.quantile(d, .75))],
        'chi_median': float(np.median(chi)),
    }
    by_seed = {}
    for r in records:
        by_seed.setdefault(r['seed'], []).append(r)
    per_real = []
    for s, recs in by_seed.items():
        per_real.append({
            'seed': s, 'n': len(recs),
            'kperp_med': float(np.median([abs(r['kappa_perp']) for r in recs])),
            's_med': float(np.median([r['s'] for r in recs])),
            'rstar_med': float(np.nanmedian([r['r_star_pt'] for r in recs])),
            'd_med': float(np.median([r['d_pt'] for r in recs])),
        })
    out['per_realisation'] = per_real
    if len(per_real) >= 3:
        rng = np.random.default_rng(99)
        B = 2000
        def bs(key):
            vals = np.array([p[key] for p in per_real if np.isfinite(p[key])])
            if len(vals) < 3: return None
            meds = [np.median(rng.choice(vals, size=len(vals), replace=True)) for _ in range(B)]
            return [float(np.quantile(meds, .025)), float(np.median(vals)), float(np.quantile(meds, .975))]
        out['bootstrap95'] = {
            'kappa_perp': bs('kperp_med'),
            's': bs('s_med'),
            'r_star': bs('rstar_med'),
        }
    return out


def main():
    sigma_x, sigma_y = 3.0, 3.0
    A = 2.0
    seeds = [77, 123, 456, 789, 1011, 1213, 1415, 1617, 1819, 2021]
    configs = [
        ('sig0.05_A2', 0.05, A),
        ('sig0.20_A2', 0.20, A),
        ('sig0.40_A2', 0.40, A),
    ]
    results = []
    for name, sigma, Aloc in configs:
        print(f"[nofilter] {name}", file=sys.stderr)
        all_recs, prim_recs = [], []
        per_seed_diag = []
        for s in seeds[:5]:
            allr, primr, d_end = run_realisation_nofilter(
                s, sigma, Aloc, sigma_x, sigma_y,
                T_seed=300, T_relax=800, T_burn=100, snap_every=20, R_primary=4.0)
            all_recs.extend(allr)
            prim_recs.extend(primr)
            per_seed_diag.append({'seed': s, 'n_total': len(allr),
                                  'n_primary': len(primr), 'd_peak_end_seed': d_end})
            print(f"    {name} seed={s} n_total={len(allr)} "
                  f"n_primary={len(primr)} d_peak={d_end:.3f}", file=sys.stderr)
        results.append({
            'config': name, 'sigma': sigma, 'A': Aloc,
            'seed_diag': per_seed_diag,
            'all_saddles': summarise(all_recs, f'{name}_all'),
            'primary_saddles': summarise(prim_recs, f'{name}_primary'),
        })
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
