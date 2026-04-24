"""Diagnostic MC: saddle statistics with NO motif filter (pure stationary-point
population), and with amplitude-only filter. Quantifies the gap between
pre-registered-filter-selected saddles and the underlying noisy-field saddle
population.
"""
import json
import sys
import numpy as np
import r_star_montecarlo as mc


def process_snapshot_nofilter(delta, amp_thr=None):
    """Extract saddle records without D2/aspect/orientation gates."""
    records = []
    sp = mc.detect_stationary_points(delta)
    for x0, y0, i, j in sp:
        K = mc.compute_hessian(delta, i, j)
        evals, evecs = np.linalg.eigh(K)
        order = np.argsort(-np.abs(evals))
        kappa_par = evals[order[0]]
        kappa_perp = evals[order[1]]
        if kappa_par * kappa_perp >= 0:
            continue
        d_pt = mc.interpolate_delta(delta, x0, y0)
        if amp_thr is not None and abs(d_pt) < amp_thr:
            continue
        chi = 2 * mc.M0 * kappa_perp**2 / mc.P0
        denom = 2*chi - 1
        r_star_pt = -2*chi/denom if abs(denom) > 1e-3 else float('nan')
        records.append({
            'd_pt': float(d_pt),
            'kappa_par': float(kappa_par),
            'kappa_perp': float(kappa_perp),
            's': float(kappa_par/kappa_perp),
            'chi': float(chi),
            'r_star_pt': float(r_star_pt),
        })
    return records


def run_real(seed, sigma, n_steps=1200, burn_in=300, snap_every=25, amp_thr=None):
    mc.SIGMA = sigma
    rng = np.random.default_rng(seed)
    delta = 0.3 + 0.4 * rng.random((mc.L, mc.L))
    lap_sym = mc.fft_laplacian_symbol(mc.L, mc.DX)
    all_recs = []
    for step in range(n_steps):
        delta = mc.imex_step(delta, mc.DT, lap_sym, rng)
        if step >= burn_in and (step - burn_in) % snap_every == 0:
            all_recs.extend(process_snapshot_nofilter(delta, amp_thr=amp_thr))
    return all_recs, float(np.std(delta))


def aggregate(name, seeds, sigma, amp_thr):
    per_real = []
    all_recs = []
    last_std = None
    for s in seeds:
        recs, fstd = run_real(s, sigma, amp_thr=amp_thr)
        last_std = fstd
        all_recs.extend(recs)
        if recs:
            per_real.append({
                'seed': s, 'n': len(recs),
                'kperp_med': float(np.median([abs(r['kappa_perp']) for r in recs])),
                's_med': float(np.median([r['s'] for r in recs])),
                'rstar_med': float(np.nanmedian([r['r_star_pt'] for r in recs])),
                'd_med': float(np.median([abs(r['d_pt']) for r in recs])),
            })
        else:
            per_real.append({'seed': s, 'n': 0})
        print(f"    [{name}] seed={s} n_saddles={len(recs)} field_std={fstd:.3f}", file=sys.stderr)

    out = {
        'name': name, 'sigma': sigma, 'amp_thr': amp_thr,
        'n_real': len(seeds), 'n_total': len(all_recs),
        'field_std_last': last_std,
        'per_realisation': per_real,
    }
    if all_recs:
        kperp = [abs(r['kappa_perp']) for r in all_recs]
        svals = [r['s'] for r in all_recs]
        rstar = [r['r_star_pt'] for r in all_recs]
        d = [abs(r['d_pt']) for r in all_recs]
        out['pooled'] = {
            'kappa_perp_median': float(np.median(kperp)),
            'kappa_perp_iqr': [float(np.quantile(kperp, .25)), float(np.quantile(kperp, .75))],
            's_median': float(np.median(svals)),
            's_iqr': [float(np.quantile(svals, .25)), float(np.quantile(svals, .75))],
            'r_star_median': float(np.nanmedian(rstar)),
            'r_star_iqr': [float(np.nanquantile(rstar, .25)), float(np.nanquantile(rstar, .75))],
            'd_pt_median': float(np.median(d)),
        }
        reals_with = [p for p in per_real if p['n'] > 0]
        if len(reals_with) >= 3:
            rng = np.random.default_rng(99)
            B = 2000
            def bs(key):
                vals = np.array([p[key] for p in reals_with])
                meds = [np.median(rng.choice(vals, size=len(vals), replace=True)) for _ in range(B)]
                return [float(np.quantile(meds, .025)), float(np.median(vals)), float(np.quantile(meds, .975))]
            out['bootstrap95'] = {
                'kappa_perp': bs('kperp_med'),
                's': bs('s_med'),
                'r_star': bs('rstar_med'),
            }
    return out


def main():
    seeds = [77, 123, 456, 789, 1011, 1213, 1415, 1617, 1819, 2021]
    configs = [
        # (name, sigma, amp_thr)
        ('sig0.0556_ampNone',   0.0556, None),
        ('sig0.0556_amp0.01',   0.0556, 0.01),
        ('sig1.0_ampNone',      1.0,    None),
        ('sig1.0_amp0.10',      1.0,    0.10),
    ]
    results = []
    for name, sig, amp in configs:
        print(f"[nofilter] {name}", file=sys.stderr)
        r = aggregate(name, seeds[:5], sig, amp)
        results.append(r)
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
