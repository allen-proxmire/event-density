"""ED-SC 3.3.5 Per-Seed Distributional-Collapse Test.

Pre-registered in theory/ED_SC_3_3_5_PerSeedCollapse.md.

Tests whether the motif-conditioned distribution f(ρ | ξ, filter)
collapses across the 10 canonical seeds when the dimensionless
hinge L_ray/ξ = 1.08 is held fixed but absolute ξ varies (35 %
natural variation in the canonical field cache: ξ ∈ [1.62, 2.19] lu).

Per seed i:
  ξ_i        = xi_per_seed[i] from outputs/ed_sc_3_1/xi_canonical.json
  L_ray_i    = 1.08 · ξ_i   (seed-specific dimensionless hinge at 1.08)
  α_filt     = 0.25         (canonical, fixed)
  N_req      = 4            (canonical, fixed)

Simulator of record:
  r2_grf_falsifier_tests.py  +  ED_Update_Rule.ed_step_mobility

The field cache is deterministically reconstructed from the canonical
seeds; ξ values are loaded (not recomputed) from xi_canonical.json to
preserve the canonical 40-snapshot ξ anchor.

Resonance windows (ED-SC 3.2.6 rev. 2) hard-fail the driver at launch:
  Window A: L_ray ∈ [2.50, 2.80]
  Window B: L_ray ∈ [3.50, 3.90]

Writes:
  outputs/ed_sc_3_3_5/per_seed_pools.csv
  outputs/ed_sc_3_3_5/per_seed_summary.json

No simulator constants are mutated. Deterministic given seeds.
"""
import csv
import json
import math
import os
import sys
import time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "ed_arch_r2"))
import r2_grf_falsifier_tests as fr  # noqa: E402

from ED_Update_Rule import ed_step_mobility  # noqa: E402

# ---------------------------------------------------------------------------
# Canonical constants (inherited, NOT mutated)
# ---------------------------------------------------------------------------
XI_CANONICAL = 1.7575325729470939
XI_GUARDRAIL_TOL = 0.20
XI_GUARDRAIL_MIN_PASS = 8

ALPHA_FILT = 0.25
N_REQ = 4
DIMLESS_HINGE = 1.08  # canonical L_ray/ξ per ED-SC 3.1 rev. 3

WINDOW_A = (2.50, 2.80)
WINDOW_B = (3.50, 3.90)

XI_JSON_PATH = os.path.join(
    HERE, "..", "..", "outputs", "ed_sc_3_1", "xi_canonical.json")
OUT_DIR = os.path.join(HERE, "..", "..", "outputs", "ed_sc_3_3_5")


# ---------------------------------------------------------------------------
# Field evolution (deterministic; bit-equivalent to the ED-SC 3.3 drivers)
# ---------------------------------------------------------------------------
def evolve_seed_to_final_field(seed):
    """Evolve the canonical ED-SIM mobility engine for the canonical seed;
    return the final p field after fr.STEPS updates (matches the field used
    for motif extraction in the ED-SC 3.3 family of drivers)."""
    rng = np.random.default_rng(seed)
    p = rng.uniform(0.3, 0.7, size=(fr.SIZE, fr.SIZE))
    for _ in range(fr.STEPS):
        p = ed_step_mobility(
            p, alpha=fr.ALPHA0, gamma=fr.GAMMA, dt=fr.DT,
            p_min=fr.P_MIN, p_max=fr.P_MAX, boundary=fr.BOUNDARY,
            mobility_exp=fr.MOBILITY_EXP, noise_scale=fr.NOISE0, rng=rng,
        )
    return p


# ---------------------------------------------------------------------------
# Resonance-window guard
# ---------------------------------------------------------------------------
def in_window(L, win):
    return win[0] <= L <= win[1]


def assert_no_resonance(seed_L_table):
    bad = []
    for seed, L in seed_L_table:
        if in_window(L, WINDOW_A) or in_window(L, WINDOW_B):
            bad.append((seed, L))
    if bad:
        raise RuntimeError(
            f"Per-seed L_ray values intersect forbidden resonance "
            f"window(s): {bad}. Refusing to launch.")


# ---------------------------------------------------------------------------
# Motif collection (canonical filter, per-seed L_ray)
# ---------------------------------------------------------------------------
def endpoints_of(saddle, L_ray):
    e_neg = saddle["e_neg"]
    e_pos = saddle["e_pos"]
    out = []
    for e, sign in ((e_neg, +1), (e_neg, -1), (e_pos, +1), (e_pos, -1)):
        di = int(round(sign * e[0] * L_ray))
        dj = int(round(sign * e[1] * L_ray))
        r = float(np.sqrt(di * di + dj * dj))
        out.append([di, dj, r])
    return out


def collect_motifs_for_seed(seed, p_final, L_ray):
    E = fr.smooth_field(p_final)
    p_hat = float(p_final.mean())
    p_std = float(p_final.std())
    sads = fr.find_morse_saddles(E)
    ratios = []
    per_motif = []
    for s in sads:
        if not fr.motif_pass(s, E, p_hat, p_std,
                             ALPHA_FILT, L_ray, N_REQ):
            continue
        ep = endpoints_of(s, L_ray)
        ratios.append(s["ratio"])
        per_motif.append({
            "seed": int(seed), "i": int(s["i"]), "j": int(s["j"]),
            "lam_neg": float(s["lam_neg"]),
            "lam_pos": float(s["lam_pos"]),
            "ratio": float(s["ratio"]),
            "L_ray": L_ray,
            "endpoints": ep,
        })
    return ratios, per_motif


# ---------------------------------------------------------------------------
# Summary statistics
# ---------------------------------------------------------------------------
def bootstrap_median_iqr(values, B=4000, rng_seed=99):
    v = np.asarray([x for x in values if np.isfinite(x)])
    if len(v) < 3:
        return dict(n=int(len(v)), median=None, iqr=None,
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


# ---------------------------------------------------------------------------
# Master driver
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    t_master = time.time()

    # -- 1. Load canonical per-seed ξ (ED-SC 3.1 rev. 2 artefact) ----------
    with open(XI_JSON_PATH) as f:
        xi_doc = json.load(f)
    xi_per_seed = {int(k): float(v) for k, v in xi_doc["xi_per_seed"].items()}
    canonical_seeds = [int(s) for s in xi_doc["seeds"]]
    print(f"Loaded canonical ξ for {len(canonical_seeds)} seeds "
          f"from {XI_JSON_PATH}", file=sys.stderr)

    # Sanity: the seed list must match r2_grf_falsifier_tests.SEEDS
    assert set(canonical_seeds) == set(int(s) for s in fr.SEEDS), (
        "canonical seeds in xi_canonical.json do not match "
        "r2_grf_falsifier_tests.SEEDS")

    # -- 2. Build per-seed L_ray table and check resonance windows ---------
    seed_L_table = []
    for seed in canonical_seeds:
        xi_i = xi_per_seed[seed]
        L_i = DIMLESS_HINGE * xi_i
        seed_L_table.append((seed, L_i))
    assert_no_resonance(seed_L_table)

    # -- 3. ξ guardrail (inherited; no re-measurement) ---------------------
    xi_vals = list(xi_per_seed.values())
    n_pass = sum(1 for x in xi_vals
                 if math.isfinite(x)
                 and abs(x - XI_CANONICAL) / XI_CANONICAL < XI_GUARDRAIL_TOL)
    xi_guardrail = {
        "method": ("inherited from outputs/ed_sc_3_1/xi_canonical.json "
                   "(canonical 40-snapshot half-decay, GR-SC 1.7)"),
        "tolerance": XI_GUARDRAIL_TOL,
        "xi_canonical": XI_CANONICAL,
        "per_seed": xi_per_seed,
        "n_pass": n_pass,
        "min_pass": XI_GUARDRAIL_MIN_PASS,
        "pass": n_pass >= XI_GUARDRAIL_MIN_PASS,
    }

    # -- 4. Per-seed motif collection --------------------------------------
    per_seed_rows = []
    pool_rows = []
    all_per_motif = []
    for seed, L_i in seed_L_table:
        ts = time.time()
        p_final = evolve_seed_to_final_field(seed)
        ratios, per_motif = collect_motifs_for_seed(seed, p_final, L_i)
        bs = bootstrap_median_iqr(ratios)
        s3 = tail_log_slope(ratios)
        row = {
            "seed": seed,
            "xi_i": xi_per_seed[seed],
            "L_ray_i": L_i,
            "N_i": int(bs["n"]),
            "S1_i": bs["median"],
            "S1_i_CI": bs["median_ci"],
            "S2_i": bs["iqr"],
            "S2_i_CI": bs["iqr_ci"],
            "S3_i": s3,
            "wall_seconds": time.time() - ts,
        }
        per_seed_rows.append(row)
        for r in ratios:
            pool_rows.append({"seed": seed, "L_ray": L_i, "ratio": r})
        all_per_motif.extend(per_motif)
        print(f"  seed={seed:>4}  ξ={xi_per_seed[seed]:.4f}  "
              f"L_ray={L_i:.4f}  N={bs['n']:>3}  "
              f"S1={bs['median']}  S2={bs['iqr']}  "
              f"t={time.time()-ts:.1f}s", file=sys.stderr)

    # -- 5. Pooled statistics ---------------------------------------------
    pooled_ratios = [r["ratio"] for r in pool_rows]
    bs_pool = bootstrap_median_iqr(pooled_ratios)
    s3_pool = tail_log_slope(pooled_ratios)
    S1_pool = bs_pool["median"]
    S2_pool = bs_pool["iqr"]

    # -- 6. Per-seed deviations + cross-seed flatness threshold ------------
    dS1 = []
    dS2 = []
    for r in per_seed_rows:
        s1 = r["S1_i"]; s2 = r["S2_i"]
        d1 = (abs(s1 - S1_pool) / abs(S1_pool)
              if (s1 is not None and S1_pool not in (None, 0)) else None)
        d2 = (abs(s2 - S2_pool) / abs(S2_pool)
              if (s2 is not None and S2_pool not in (None, 0)) else None)
        r["dS1_i"] = d1
        r["dS2_i"] = d2
        if d1 is not None: dS1.append(d1)
        if d2 is not None: dS2.append(d2)

    s2_vals = [r["S2_i"] for r in per_seed_rows if r["S2_i"] is not None]
    if len(s2_vals) >= 2 and S2_pool not in (None, 0):
        s2_std = float(np.std(s2_vals, ddof=1))
        s2_rel_sem_across_seeds = s2_std / (abs(S2_pool) * math.sqrt(len(s2_vals)))
    else:
        s2_rel_sem_across_seeds = None

    flat_thresh = (max(0.20, 2 * s2_rel_sem_across_seeds)
                   if s2_rel_sem_across_seeds is not None else 0.20)

    max_dS1 = max(dS1) if dS1 else None
    max_dS2 = max(dS2) if dS2 else None

    # -- 7. Verdict --------------------------------------------------------
    if not xi_guardrail["pass"]:
        verdict = "GuardrailFailure"
        verdict_reason = "xi guardrail < min_pass"
    elif (max_dS1 is None or max_dS2 is None):
        verdict = "GuardrailFailure"
        verdict_reason = "insufficient statistics to compute deviations"
    elif max_dS1 < flat_thresh and max_dS2 < flat_thresh:
        verdict = "Collapsed"
        verdict_reason = (f"max ΔS1 = {max_dS1:.4f}, "
                          f"max ΔS2 = {max_dS2:.4f}, "
                          f"both below flat_thresh = {flat_thresh:.4f}")
    else:
        verdict = "Broken-collapse"
        failing = []
        for r in per_seed_rows:
            if (r["dS1_i"] is not None and r["dS1_i"] >= flat_thresh) or \
               (r["dS2_i"] is not None and r["dS2_i"] >= flat_thresh):
                failing.append({
                    "seed": r["seed"], "xi_i": r["xi_i"],
                    "dS1_i": r["dS1_i"], "dS2_i": r["dS2_i"]})
        verdict_reason = {
            "flat_thresh": flat_thresh,
            "max_dS1": max_dS1, "max_dS2": max_dS2,
            "failing_seeds": failing,
        }

    # -- 8. Write per-seed pool CSV ----------------------------------------
    csv_path = os.path.join(OUT_DIR, "per_seed_pools.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["seed", "L_ray", "ratio"])
        for row in pool_rows:
            w.writerow([row["seed"], row["L_ray"], row["ratio"]])

    # -- 9. Write master summary JSON --------------------------------------
    out = {
        "method": ("ED-SC 3.3.5 per-seed distributional-collapse test "
                   "at canonical filter geometry; per-seed L_ray = 1.08·ξ_i; "
                   "no new field evolution beyond deterministic regeneration"),
        "simulator_of_record":
            "r2_grf_falsifier_tests.py + ED_Update_Rule.ed_step_mobility",
        "xi_canonical_lattice_units": XI_CANONICAL,
        "dimensionless_hinge": DIMLESS_HINGE,
        "alpha_filt": ALPHA_FILT,
        "N_req": N_REQ,
        "canonical_params": {
            "alpha": fr.ALPHA0, "gamma": fr.GAMMA,
            "noise_sigma": fr.NOISE0,
            "mobility_exp": fr.MOBILITY_EXP,
            "steps": fr.STEPS, "size": fr.SIZE, "dt": fr.DT,
        },
        "seeds": canonical_seeds,
        "xi_json_source": XI_JSON_PATH,
        "resonance_windows_excluded": {
            "A": list(WINDOW_A), "B": list(WINDOW_B)},
        "per_seed_L_ray_table": [
            {"seed": s, "L_ray": L} for s, L in seed_L_table],
        "xi_guardrail": xi_guardrail,
        "per_seed_stats": per_seed_rows,
        "pooled": {
            "N_pool": int(bs_pool["n"]),
            "S1_pool": S1_pool,
            "S1_pool_CI": bs_pool["median_ci"],
            "S2_pool": S2_pool,
            "S2_pool_CI": bs_pool["iqr_ci"],
            "S3_pool": s3_pool,
        },
        "cross_seed_flatness": {
            "S2_rel_SEM_across_seeds": s2_rel_sem_across_seeds,
            "flat_thresh": flat_thresh,
            "max_dS1": max_dS1,
            "max_dS2": max_dS2,
        },
        "verdict": verdict,
        "verdict_reason": verdict_reason,
        "wall_seconds_total": time.time() - t_master,
    }

    json_path = os.path.join(OUT_DIR, "per_seed_summary.json")
    with open(json_path, "w") as f:
        json.dump(out, f, indent=2)

    print(f"\nWrote master summary → {json_path}", file=sys.stderr)
    print(json.dumps({
        "verdict": verdict,
        "xi_guardrail_pass": xi_guardrail["pass"],
        "N_pool": int(bs_pool["n"]),
        "S1_pool": S1_pool,
        "S2_pool": S2_pool,
        "max_dS1": max_dS1,
        "max_dS2": max_dS2,
        "flat_thresh": flat_thresh,
        "wall_seconds_total": out["wall_seconds_total"],
    }, indent=2))


if __name__ == "__main__":
    main()
