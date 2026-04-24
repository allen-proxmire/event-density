"""Sweep driver for r_star_montecarlo: varies SIGMA and filter strictness.

Reuses the module's functions but overrides module-level globals before each run.
Writes compact JSON summary to stdout.
"""
import json
import sys
import numpy as np
import importlib

import r_star_montecarlo as mc


def run_config(sigma, delta_thr, sym_thresh, aspect_min, orient_tol_deg,
               n_real=5, n_steps=1500, burn_in=400, snapshot_every=20,
               seeds=None, label=""):
    # Override module globals
    mc.SIGMA = sigma
    mc.DELTA_THR = delta_thr
    mc.SYM_THRESH = sym_thresh
    mc.ASPECT_MIN = aspect_min
    mc.ORIENT_TOL_DEG = orient_tol_deg
    mc.N_STEPS = n_steps
    mc.BURN_IN = burn_in
    mc.SNAPSHOT_EVERY = snapshot_every

    if seeds is None:
        seeds = [77, 123, 456, 789, 1011, 1213, 1415, 1617, 1819, 2021][:n_real]

    per_real = []
    all_recs = []
    for s in seeds:
        recs = mc.run_realisation(s)
        all_recs.extend(recs)
        if recs:
            per_real.append({
                'seed': s,
                'n_motifs': len(recs),
                'kappa_perp_med': float(np.median([abs(r['kappa_perp']) for r in recs])),
                's_med': float(np.median([r['s'] for r in recs])),
                'r_star_med': float(np.nanmedian([r['r_star_pt'] for r in recs])),
                'd_pt_med': float(np.median([abs(r['d_pt']) for r in recs])),
            })
        else:
            per_real.append({'seed': s, 'n_motifs': 0})
        print(f"    [{label}] seed={s} n_motifs={len(recs)}", file=sys.stderr)

    n_tot = len(all_recs)
    out = {
        'label': label,
        'sigma': sigma,
        'filter': {'delta_thr': delta_thr, 'sym_thresh': sym_thresh,
                   'aspect_min': aspect_min, 'orient_tol_deg': orient_tol_deg},
        'n_realisations': len(seeds),
        'n_motifs_total': n_tot,
        'per_realisation': per_real,
    }
    if n_tot >= 3:
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
        # Bootstrap CI over realisations
        reals_with = [p for p in per_real if p['n_motifs'] > 0]
        if len(reals_with) >= 3:
            rng = np.random.default_rng(99)
            B = 2000
            def bs(key):
                vals = np.array([p[key] for p in reals_with])
                meds = [np.median(rng.choice(vals, size=len(vals), replace=True)) for _ in range(B)]
                return [float(np.quantile(meds, .025)), float(np.median(vals)), float(np.quantile(meds, .975))]
            out['bootstrap95_over_reals'] = {
                'kappa_perp': bs('kappa_perp_med'),
                's': bs('s_med'),
                'r_star': bs('r_star_med'),
            }
    return out


def main():
    configs = [
        # (label, sigma, delta_thr, sym_thresh, aspect_min, orient_tol_deg)
        ('prereg_canonical',   0.0556, 0.10, 0.20, 1.5, 15.0),
        ('prereg_sig1',        1.0,    0.10, 0.20, 1.5, 15.0),
        ('relax_med_sig1',     1.0,    0.10, 0.40, 1.3, 30.0),
        ('relax_loose_sig1',   1.0,    0.10, 0.60, 1.2, 45.0),
        ('relax_loose_sig07',  0.7,    0.10, 0.60, 1.2, 45.0),
    ]
    results = []
    for cfg in configs:
        label, sigma, dthr, sym, asp, orient = cfg
        print(f"[sweep] {label}", file=sys.stderr)
        r = run_config(sigma, dthr, sym, asp, orient, n_real=5,
                       n_steps=1200, burn_in=300, snapshot_every=25,
                       label=label)
        results.append(r)
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
