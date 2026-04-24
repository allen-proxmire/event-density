"""ED-SC 3.2 L_ray/xi scan driver.

Sweeps L_RAY over the six grid points G1-G6 defined in
theory/ED_SC_3_2_LrayXi_Scan.md, computes spectral triad (sigma0,
sigma1, sigma2) and correlation length xi per realisation, extracts
motif-conditioned s = kappa_par/kappa_perp (== ED-SC 3.x rho variable),
and reports S1 (median), S2 (IQR), S3 (upper-tail log-slope) with
bootstrap uncertainties.

Emits JSON summary to stdout; per-grid record CSVs to outputs/.
"""
import json
import os
import sys
import time
import numpy as np
from numpy.fft import fft2, ifft2, fftshift

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r_star_montecarlo as mc


def spectral_triad(delta, dx=1.0):
    """Return (sigma0, sigma1, sigma2) from a 2D snapshot.

    sigma0 = std of delta
    sigma1 = RMS gradient magnitude
    sigma2 = RMS Laplacian magnitude
    """
    gx = (np.roll(delta, -1, axis=0) - np.roll(delta, 1, axis=0)) / (2 * dx)
    gy = (np.roll(delta, -1, axis=1) - np.roll(delta, 1, axis=1)) / (2 * dx)
    grad2 = gx * gx + gy * gy
    lap = (np.roll(delta, -1, axis=0) + np.roll(delta, 1, axis=0)
           + np.roll(delta, -1, axis=1) + np.roll(delta, 1, axis=1)
           - 4 * delta) / (dx * dx)
    s0 = float(np.std(delta))
    s1 = float(np.sqrt(np.mean(grad2)))
    s2 = float(np.sqrt(np.mean(lap * lap)))
    return s0, s1, s2


def correlation_length(delta, dx=1.0):
    """Return xi = r at which radial 2-pt correlation decays to 0.5."""
    N = delta.shape[0]
    f = delta - np.mean(delta)
    F = fft2(f)
    C = np.real(ifft2(F * np.conj(F))) / (N * N)
    C = fftshift(C)
    c0 = C[N // 2, N // 2]
    if c0 <= 0:
        return np.nan
    # Radial profile
    y, x = np.indices(C.shape)
    r = np.sqrt((x - N // 2) ** 2 + (y - N // 2) ** 2)
    r_int = r.astype(int)
    rmax = N // 2
    prof = np.array([C[r_int == k].mean() if np.any(r_int == k) else 0.0
                     for k in range(rmax)])
    prof /= c0
    # Find first crossing of 0.5
    for k in range(1, rmax):
        if prof[k] <= 0.5:
            # Linear interpolation
            if prof[k - 1] == prof[k]:
                return float(k) * dx
            frac = (prof[k - 1] - 0.5) / (prof[k - 1] - prof[k])
            return float((k - 1 + frac)) * dx
    return float(rmax) * dx  # never crosses -> clip


def run_one_seed_with_spectra(seed, l_ray):
    """Override globals, run realisation, collect motifs AND spectral triad."""
    mc.L_RAY = l_ray
    rng = np.random.default_rng(seed)
    delta = 0.3 + 0.4 * rng.random((mc.L, mc.L))
    lap_sym = mc.fft_laplacian_symbol(mc.L, mc.DX)
    all_records = []
    spectra = []  # list of (s0, s1, s2, xi)
    for step in range(mc.N_STEPS):
        delta = mc.imex_step(delta, mc.DT, lap_sym, rng)
        if step >= mc.BURN_IN and (step - mc.BURN_IN) % mc.SNAPSHOT_EVERY == 0:
            recs = mc.process_snapshot(delta)
            for r in recs:
                r['step'] = step
                r['seed'] = seed
                r['l_ray'] = l_ray
            all_records.extend(recs)
            s0, s1, s2 = spectral_triad(delta, mc.DX)
            xi = correlation_length(delta, mc.DX)
            spectra.append((s0, s1, s2, xi))
    return all_records, spectra


def bootstrap_median_iqr(values, B=2000, rng=None):
    if rng is None:
        rng = np.random.default_rng(99)
    v = np.asarray([x for x in values if np.isfinite(x)])
    if len(v) < 3:
        return dict(n=len(v), median=np.nan, iqr=np.nan,
                    median_ci=(np.nan, np.nan), iqr_ci=(np.nan, np.nan))
    meds, iqrs = [], []
    for _ in range(B):
        smp = rng.choice(v, size=len(v), replace=True)
        meds.append(np.median(smp))
        iqrs.append(np.quantile(smp, 0.75) - np.quantile(smp, 0.25))
    return dict(
        n=int(len(v)),
        median=float(np.median(v)),
        iqr=float(np.quantile(v, 0.75) - np.quantile(v, 0.25)),
        median_ci=(float(np.quantile(meds, 0.16)), float(np.quantile(meds, 0.84))),
        iqr_ci=(float(np.quantile(iqrs, 0.16)), float(np.quantile(iqrs, 0.84))),
    )


def tail_log_slope(values):
    """S3: log-slope of 1 - F(rho) on the upper tail (least-negative rho)."""
    v = np.asarray([x for x in values if np.isfinite(x)])
    if len(v) < 8:
        return np.nan
    vs = np.sort(v)          # ascending (most negative first)
    n = len(vs)
    # Upper tail = rho closest to 0 (= least negative). Use top 40% of ordered values.
    k = max(4, int(0.4 * n))
    tail = vs[-k:]
    ranks = np.arange(1, k + 1)
    pexc = (k - ranks + 0.5) / n   # empirical 1 - F
    # Fit log(pexc) vs tail
    mask = pexc > 0
    if mask.sum() < 4:
        return np.nan
    slope, _ = np.polyfit(tail[mask], np.log(pexc[mask]), 1)
    return float(slope)


def main():
    grid = [
        ('G1', 0.30),
        ('G2', 0.50),
        ('G3', 1.08),
        ('G4', 2.00),
        ('G5', 3.00),
        ('G6', 5.00),
    ]
    seeds = [77, 123, 456, 789, 1011, 1213, 1415, 1617, 1819, 2021]
    # Pilot budget: use all 10 seeds, default N_STEPS; total ~25 min.

    mc.N_STEPS = 2000
    mc.BURN_IN = 500
    mc.SNAPSHOT_EVERY = 20

    # Step 1: measure xi and sigma_i at L_ray = 2 (canonical) with one seed
    # to set the L_ray values for each grid point.
    print("Calibrating xi at canonical settings...", file=sys.stderr)
    t0 = time.time()
    _, calib_spec = run_one_seed_with_spectra(seed=77, l_ray=2.0)
    s0_c = np.mean([s[0] for s in calib_spec])
    s1_c = np.mean([s[1] for s in calib_spec])
    s2_c = np.mean([s[2] for s in calib_spec])
    xi_c = np.nanmean([s[3] for s in calib_spec])
    print(f"  xi={xi_c:.3f}  sigma0={s0_c:.3f}  sigma1={s1_c:.3f}  sigma2={s2_c:.3f}  "
          f"(elapsed {time.time()-t0:.1f}s)", file=sys.stderr)

    grid_results = {}
    for label, ratio in grid:
        l_ray_val = float(ratio * xi_c)
        print(f"\n[{label}] L_ray/xi={ratio}  L_ray={l_ray_val:.3f}", file=sys.stderr)
        t1 = time.time()
        pool_recs = []
        per_seed_counts = []
        per_seed_spectra = []
        for s in seeds:
            recs, spectra = run_one_seed_with_spectra(s, l_ray_val)
            pool_recs.extend(recs)
            per_seed_counts.append(len(recs))
            per_seed_spectra.extend(spectra)
            print(f"  seed={s} n={len(recs)}  (cum {len(pool_recs)})", file=sys.stderr)
        dt = time.time() - t1
        s_vals = [r['s'] for r in pool_recs]
        bs_s = bootstrap_median_iqr(s_vals)
        s3 = tail_log_slope(s_vals)
        s0_arr = np.array([sp[0] for sp in per_seed_spectra])
        s1_arr = np.array([sp[1] for sp in per_seed_spectra])
        s2_arr = np.array([sp[2] for sp in per_seed_spectra])
        xi_arr = np.array([sp[3] for sp in per_seed_spectra])

        grid_results[label] = {
            'L_ray_over_xi': ratio,
            'L_ray': l_ray_val,
            'xi_mean': float(np.nanmean(xi_arr)),
            'xi_std': float(np.nanstd(xi_arr)),
            'sigma0_mean': float(np.mean(s0_arr)),
            'sigma1_mean': float(np.mean(s1_arr)),
            'sigma2_mean': float(np.mean(s2_arr)),
            'N_motifs': int(bs_s['n']),
            'per_seed_counts': per_seed_counts,
            'S1_median': bs_s['median'],
            'S1_ci': bs_s['median_ci'],
            'S2_iqr': bs_s['iqr'],
            'S2_ci': bs_s['iqr_ci'],
            'S3_tail_slope': s3,
            'wall_seconds': dt,
        }

    # Spectral isoperimetric check (pooled)
    s0p = np.mean([grid_results[g[0]]['sigma0_mean'] for g in grid])
    s1p = np.mean([grid_results[g[0]]['sigma1_mean'] for g in grid])
    s2p = np.mean([grid_results[g[0]]['sigma2_mean'] for g in grid])

    summary = {
        'calibration': {
            'seed': 77, 'L_ray_used_for_calib': 2.0,
            'xi': float(xi_c),
            'sigma0': float(s0_c), 'sigma1': float(s1_c), 'sigma2': float(s2_c),
        },
        'grid': grid_results,
        'pooled_spectra': {
            'sigma0': float(s0p), 'sigma1': float(s1p), 'sigma2': float(s2p),
            'isoperimetric_s0s2_over_s1sq': float(s0p * s2p / (s1p * s1p)) if s1p > 0 else None,
        },
        'sf2_weak_reading': _sf2_weak(grid_results),
    }
    print(json.dumps(summary, indent=2))


def _sf2_weak(gr):
    """S-F2 weak reading: |S2_k - S2_G3| / S2_G3 for k in G2..G4."""
    out = {}
    s2_g3 = gr['G3']['S2_iqr']
    if not np.isfinite(s2_g3) or s2_g3 <= 0:
        return {'triggered': None, 'note': 'G3 S2 invalid'}
    for k in ['G2', 'G3', 'G4']:
        s2k = gr[k]['S2_iqr']
        out[k] = float(abs(s2k - s2_g3) / s2_g3) if np.isfinite(s2k) else None
    triggered = any((v is not None and v > 0.20) for v in out.values())
    return {'drifts': out, 'triggered': bool(triggered),
            'tolerance': 0.20}


if __name__ == '__main__':
    main()
