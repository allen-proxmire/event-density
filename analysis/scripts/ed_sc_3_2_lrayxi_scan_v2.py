"""ED-SC 3.2 L_ray/xi scan — v2 (simulator of record).

Rebuilt against the canonical ED-SIM mobility engine:
  r2_grf_falsifier_tests.py  +  ED_Update_Rule.ed_step_mobility

Supersedes ed_sc_3_2_lrayxi_scan.py (v1), which was wired to the wrong
simulator (r_star_montecarlo.py). Per the rectification memo
(theory/ED_SC_3_1_rev2_Rectification.md).

Protocol:
  - L_ray / xi grid: {0.30, 0.50, 1.08, 2.00, 3.00, 5.00}
  - xi_canonical = 1.758 lattice units (from outputs/ed_sc_3_1/xi_canonical.json)
  - alpha_filt = 0.25 (canonical), N_req = 4 (canonical)
  - 10 canonical seeds; 500 steps; 64x64 periodic
  - Mobility M(p) = (1-p)^{2.7}, alpha=0.03, gamma=0.5, sigma=0.0556
  - Read-only use of r2_grf_falsifier_tests module constants.

Outputs:
  outputs/ed_sc_3_2/v2_scan_summary.json
"""
import json
import os
import sys
import time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "ed_arch_r2"))
import r2_grf_falsifier_tests as fr  # simulator of record (read-only)

from ED_Update_Rule import ed_step_mobility


# ---------------------------------------------------------------------------
# Constants (read-only; do not mutate fr.*)
# ---------------------------------------------------------------------------

XI_CANONICAL = 1.7575325729470939   # from outputs/ed_sc_3_1/xi_canonical.json

GRID = [
    ("G1", 0.30),
    ("G2", 0.50),
    ("G3", 1.08),
    ("G4", 2.00),
    ("G5", 3.00),
    ("G6", 5.00),
]

ALPHA_FILT = 0.25  # canonical (matches T1a_baseline)
N_REQ = 4          # canonical (matches T1a_baseline)


def spectral_triad(field, dx=1.0):
    gx = (np.roll(field, -1, 0) - np.roll(field, 1, 0)) / (2 * dx)
    gy = (np.roll(field, -1, 1) - np.roll(field, 1, 1)) / (2 * dx)
    lap = (np.roll(field, -1, 0) + np.roll(field, 1, 0)
           + np.roll(field, -1, 1) + np.roll(field, 1, 1) - 4 * field) / (dx * dx)
    return (float(np.std(field)),
            float(np.sqrt(np.mean(gx * gx + gy * gy))),
            float(np.sqrt(np.mean(lap * lap))))


def run_scenario(seed):
    """Evolve canonical ED-SIM mobility engine to step STEPS. Returns final p."""
    rng = np.random.default_rng(seed)
    p = rng.uniform(0.3, 0.7, size=(fr.SIZE, fr.SIZE))
    for _ in range(fr.STEPS):
        p = ed_step_mobility(
            p, alpha=fr.ALPHA0, gamma=fr.GAMMA, dt=fr.DT,
            p_min=fr.P_MIN, p_max=fr.P_MAX, boundary=fr.BOUNDARY,
            mobility_exp=fr.MOBILITY_EXP, noise_scale=fr.NOISE0, rng=rng,
        )
    return p


def collect_motifs_at_l_ray(l_ray_val):
    """For each seed, evolve the field, detect saddles, run motif filter with
    the specified (non-canonical) L_ray. Return per-seed stats + pooled ratios
    + pooled field spectra."""
    pooled_ratios = []
    per_seed = []
    spectra = []
    for seed in fr.SEEDS:
        p = run_scenario(seed)
        E = fr.smooth_field(p)
        p_hat = float(p.mean())
        p_std = float(p.std())
        s0, s1, s2 = spectral_triad(p)
        spectra.append((s0, s1, s2))
        sads = fr.find_morse_saddles(E)
        admitted = [s for s in sads
                    if fr.motif_pass(s, E, p_hat, p_std,
                                     ALPHA_FILT, l_ray_val, N_REQ)]
        r = [s["ratio"] for s in admitted]
        pooled_ratios.extend(r)
        per_seed.append({
            "seed": seed, "n_cand": len(sads), "n_motif": len(r),
            "median": float(np.median(r)) if r else None,
            "p_hat": p_hat, "p_std": p_std,
        })
    return pooled_ratios, per_seed, spectra


def bootstrap_median_iqr(values, B=4000, rng_seed=99):
    v = np.asarray([x for x in values if np.isfinite(x)])
    if len(v) < 3:
        return dict(n=len(v), median=None, iqr=None,
                    median_ci=[None, None], iqr_ci=[None, None])
    rng = np.random.default_rng(rng_seed)
    meds, iqrs = [], []
    for _ in range(B):
        smp = rng.choice(v, size=len(v), replace=True)
        meds.append(np.median(smp))
        iqrs.append(np.quantile(smp, 0.75) - np.quantile(smp, 0.25))
    return dict(
        n=int(len(v)),
        median=float(np.median(v)),
        iqr=float(np.quantile(v, 0.75) - np.quantile(v, 0.25)),
        median_ci=[float(np.quantile(meds, 0.16)),
                   float(np.quantile(meds, 0.84))],
        iqr_ci=[float(np.quantile(iqrs, 0.16)),
                float(np.quantile(iqrs, 0.84))],
    )


def tail_log_slope(values):
    """Upper-tail (least-negative) log-slope of 1 - F(rho)."""
    v = np.asarray([x for x in values if np.isfinite(x)])
    if len(v) < 8:
        return None
    vs = np.sort(v)
    n = len(vs)
    k = max(4, int(0.4 * n))
    tail = vs[-k:]
    ranks = np.arange(1, k + 1)
    pexc = (k - ranks + 0.5) / n
    mask = pexc > 0
    if mask.sum() < 4:
        return None
    slope, _ = np.polyfit(tail[mask], np.log(pexc[mask]), 1)
    return float(slope)


def main():
    t0 = time.time()
    grid_out = {}
    for label, ratio in GRID:
        l_ray_val = ratio * XI_CANONICAL
        t1 = time.time()
        pooled, per_seed, spectra = collect_motifs_at_l_ray(l_ray_val)
        bs = bootstrap_median_iqr(pooled)
        s3 = tail_log_slope(pooled)
        s_arr = np.array(spectra)
        grid_out[label] = {
            "L_ray_over_xi": ratio,
            "L_ray_lattice_units": l_ray_val,
            "N_motifs": int(bs["n"]),
            "per_seed": per_seed,
            "pooled_ratios": pooled,
            "S1_median": bs["median"],
            "S1_ci16_84": bs["median_ci"],
            "S2_iqr": bs["iqr"],
            "S2_ci16_84": bs["iqr_ci"],
            "S3_tail_slope": s3,
            "sigma0_mean": float(s_arr[:, 0].mean()),
            "sigma1_mean": float(s_arr[:, 1].mean()),
            "sigma2_mean": float(s_arr[:, 2].mean()),
            "wall_seconds": time.time() - t1,
        }
        print(f"[{label}] L_ray/xi={ratio}  L_ray={l_ray_val:.3f}  "
              f"N={bs['n']}  S1={bs['median']}  S2={bs['iqr']}  "
              f"t={time.time()-t1:.1f}s", file=sys.stderr)

    # Cross-grid spectral stability
    s0s = [grid_out[lab]["sigma0_mean"] for lab, _ in GRID]
    s1s = [grid_out[lab]["sigma1_mean"] for lab, _ in GRID]
    s2s = [grid_out[lab]["sigma2_mean"] for lab, _ in GRID]

    # S-F2 weak reading: |S2_k - S2_G3| / S2_G3 for k in G2..G4
    s2_g3 = grid_out["G3"]["S2_iqr"]
    sf2 = {}
    if s2_g3 is not None and s2_g3 > 0:
        for k in ["G2", "G3", "G4"]:
            s2k = grid_out[k]["S2_iqr"]
            sf2[k] = (float(abs(s2k - s2_g3) / s2_g3)
                      if s2k is not None else None)
        triggered = any((v is not None and v > 0.20) for v in sf2.values())
    else:
        sf2 = {"G2": None, "G3": None, "G4": None}
        triggered = None

    out = {
        "method": "L_ray/xi sweep on simulator of record",
        "simulator": ("r2_grf_falsifier_tests.py + "
                      "ED_Update_Rule.ed_step_mobility"),
        "xi_canonical_lattice_units": XI_CANONICAL,
        "alpha_filt": ALPHA_FILT,
        "N_req": N_REQ,
        "seeds": fr.SEEDS,
        "canonical_params": {
            "alpha": fr.ALPHA0, "gamma": fr.GAMMA,
            "noise_sigma": fr.NOISE0,
            "mobility_exp": fr.MOBILITY_EXP,
            "steps": fr.STEPS, "size": fr.SIZE,
        },
        "grid": grid_out,
        "spectral_stability_across_grid": {
            "sigma0_minmax_rsd": float((max(s0s) - min(s0s)) / np.mean(s0s)),
            "sigma1_minmax_rsd": float((max(s1s) - min(s1s)) / np.mean(s1s)),
            "sigma2_minmax_rsd": float((max(s2s) - min(s2s)) / np.mean(s2s)),
        },
        "sf2_weak_reading": {
            "drifts_G2_G3_G4": sf2,
            "tolerance": 0.20,
            "triggered": triggered,
        },
        "wall_seconds_total": time.time() - t0,
    }
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
