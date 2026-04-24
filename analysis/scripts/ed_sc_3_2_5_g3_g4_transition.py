"""ED-SC 3.2.5 G3-G4 Transition fine-grid diagnostic.

Dense L_ray/xi scan across [1.0, 2.5] at step 0.1 to resolve whether the
G3 -> G4 jump (S2: 1.29 -> 2.99; S1: -1.92 -> -2.77) observed in
ed_sc_3_2_lrayxi_scan_v2 is a smooth drift, a shoulder, or a sharp
transition.

Simulator of record:
  r2_grf_falsifier_tests.py  +  ED_Update_Rule.ed_step_mobility
xi_canonical = 1.7575325729470939  (outputs/ed_sc_3_1/xi_canonical.json)

Writes:
  outputs/ed_sc_3_2/transition_g3_g4_summary.json
"""
import json
import os
import sys
import time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "ed_arch_r2"))
import r2_grf_falsifier_tests as fr

from ED_Update_Rule import ed_step_mobility

XI_CANONICAL = 1.7575325729470939

# Fine grid ΔL_ray/ξ = 0.1 across [1.0, 2.5]
GRID = [round(1.0 + 0.1 * k, 2) for k in range(16)]  # 1.0, 1.1, ..., 2.5

ALPHA_FILT = 0.25
N_REQ = 4


def run_scenario(seed):
    rng = np.random.default_rng(seed)
    p = rng.uniform(0.3, 0.7, size=(fr.SIZE, fr.SIZE))
    for _ in range(fr.STEPS):
        p = ed_step_mobility(
            p, alpha=fr.ALPHA0, gamma=fr.GAMMA, dt=fr.DT,
            p_min=fr.P_MIN, p_max=fr.P_MAX, boundary=fr.BOUNDARY,
            mobility_exp=fr.MOBILITY_EXP, noise_scale=fr.NOISE0, rng=rng,
        )
    return p


def collect_motifs(field_cache, l_ray_val):
    """Given cached (p, E, p_hat, p_std) per seed, run motif filter."""
    pooled = []
    per_seed = []
    for seed, (p, E, p_hat, p_std) in field_cache.items():
        sads = fr.find_morse_saddles(E)
        admitted = [s for s in sads
                    if fr.motif_pass(s, E, p_hat, p_std,
                                     ALPHA_FILT, l_ray_val, N_REQ)]
        r = [s["ratio"] for s in admitted]
        pooled.extend(r)
        per_seed.append({"seed": seed, "n_cand": len(sads), "n_motif": len(r)})
    return pooled, per_seed


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

    # Evolve each seed once; reuse for all L_ray values
    print("Evolving seeds (one field cache shared across grid)...",
          file=sys.stderr)
    field_cache = {}
    for seed in fr.SEEDS:
        ts = time.time()
        p = run_scenario(seed)
        E = fr.smooth_field(p)
        field_cache[seed] = (p, E, float(p.mean()), float(p.std()))
        print(f"  seed={seed}  t={time.time()-ts:.1f}s", file=sys.stderr)

    grid_out = {}
    for ratio in GRID:
        l_ray_val = ratio * XI_CANONICAL
        t1 = time.time()
        pooled, per_seed = collect_motifs(field_cache, l_ray_val)
        bs = bootstrap_median_iqr(pooled)
        s3 = tail_log_slope(pooled)
        key = f"r{ratio:.2f}"
        grid_out[key] = {
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
            "wall_seconds": time.time() - t1,
        }
        print(f"[{key}] L_ray/xi={ratio}  L={l_ray_val:.3f}  "
              f"N={bs['n']}  S1={bs['median']}  S2={bs['iqr']}  "
              f"S3={s3}  t={time.time()-t1:.2f}s", file=sys.stderr)

    out = {
        "method": ("Fine-grid L_ray/xi scan on simulator of record "
                   "(G3-G4 transition diagnostic)"),
        "simulator": ("r2_grf_falsifier_tests.py + "
                      "ED_Update_Rule.ed_step_mobility"),
        "xi_canonical_lattice_units": XI_CANONICAL,
        "alpha_filt": ALPHA_FILT,
        "N_req": N_REQ,
        "seeds": fr.SEEDS,
        "grid_ratios": GRID,
        "canonical_params": {
            "alpha": fr.ALPHA0, "gamma": fr.GAMMA,
            "noise_sigma": fr.NOISE0,
            "mobility_exp": fr.MOBILITY_EXP,
            "steps": fr.STEPS, "size": fr.SIZE,
        },
        "grid": grid_out,
        "wall_seconds_total": time.time() - t0,
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
