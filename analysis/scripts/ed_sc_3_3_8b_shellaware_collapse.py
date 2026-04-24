"""ED-SC 3.3.8b Shell-Aware Per-Seed Collapse Test.

Pre-registered in theory/ED_SC_3_3_8b_ShellAwareCoordinate.md.

Re-runs the ED-SC 3.3.6 40-snapshot per-seed collapse test under the
shell-aware effective coordinate L_eff selected by ED-SC 3.3.8a:

    r_diag(L)   = round(0.707 * L)             # diagonal endpoint index
    L_eff(L)    = L * ( s / (0.707 * L) )       # snaps to shell class s
                = s / 0.707 = sqrt(2) * s        # equivalent form

Per seed:
    ξ_i      = xi_per_seed[i] from xi_canonical.json
    L_ray_i  = 1.08 * ξ_i
    s_i      = round(0.707 * L_ray_i)
    L_eff_i  = sqrt(2) * s_i

Motifs extracted at L_eff_i instead of L_ray_i for each seed; all
other canonical parameters unchanged.

Simulator of record:
  r2_grf_falsifier_tests.py  +  ED_Update_Rule.ed_step_mobility

Resonance-window guard hard-fails if any L_eff_i ∈ [2.50, 2.80]
(Window A) or [3.50, 3.90] (Window B). Under the current canonical ξ
table, seed 456's L_eff = √8 ≈ 2.828 sits 0.028 above Window A's
upper edge — narrow but outside.

Writes:
  outputs/ed_sc_3_3_8b/per_seed_shellaware_pools.csv
  outputs/ed_sc_3_3_8b/per_seed_shellaware_summary.json

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
XI_BURN_IN = 100
XI_SNAP_EVERY = 10

ALPHA_FILT = 0.25
N_REQ = 4
DIMLESS_HINGE = 1.08
DIAG_COS = 0.707  # 1/√2

WINDOW_A = (2.50, 2.80)
WINDOW_B = (3.50, 3.90)

XI_JSON_PATH = os.path.join(
    HERE, "..", "..", "outputs", "ed_sc_3_1", "xi_canonical.json")
ED_SC_3_3_6_JSON = os.path.join(
    HERE, "..", "..", "outputs", "ed_sc_3_3_6",
    "per_seed_40snap_summary.json")
OUT_DIR = os.path.join(HERE, "..", "..", "outputs", "ed_sc_3_3_8b")


# ---------------------------------------------------------------------------
# Shell-aware coordinate
# ---------------------------------------------------------------------------
def shell_index(L):
    """Diagonal endpoint shell index s = round(0.707·L)."""
    return int(round(DIAG_COS * L))


def L_eff_of(L):
    """Shell-aware effective ray length. Piecewise constant in L."""
    s = shell_index(L)
    return math.sqrt(2) * s, s


# ---------------------------------------------------------------------------
# Resonance-window guard
# ---------------------------------------------------------------------------
def in_window(L, win):
    return win[0] <= L <= win[1]


def assert_no_resonance(seed_L_table):
    bad = [(s, L) for s, L in seed_L_table
           if in_window(L, WINDOW_A) or in_window(L, WINDOW_B)]
    if bad:
        raise RuntimeError(
            f"Per-seed L_eff values intersect forbidden resonance "
            f"window(s): {bad}. Refusing to launch.")


# ---------------------------------------------------------------------------
# Motif extraction on a single snapshot (at per-seed L_eff)
# ---------------------------------------------------------------------------
def endpoints_of(saddle, L_ray):
    e_neg = saddle["e_neg"]
    e_pos = saddle["e_pos"]
    out = []
    for e, sign in ((e_neg, +1), (e_neg, -1), (e_pos, +1), (e_pos, -1)):
        di = int(round(sign * e[0] * L_ray))
        dj = int(round(sign * e[1] * L_ray))
        r = float(np.sqrt(di * di + dj * dj))
        out.append((di, dj, r))
    return out


def collect_motifs_snapshot(p_snapshot, L_ray):
    E = fr.smooth_field(p_snapshot)
    p_hat = float(p_snapshot.mean())
    p_std = float(p_snapshot.std())
    sads = fr.find_morse_saddles(E)
    per_motif = []
    for s in sads:
        if not fr.motif_pass(s, E, p_hat, p_std,
                             ALPHA_FILT, L_ray, N_REQ):
            continue
        eps = endpoints_of(s, L_ray)
        per_motif.append({
            "i": int(s["i"]), "j": int(s["j"]),
            "lam_neg": float(s["lam_neg"]),
            "lam_pos": float(s["lam_pos"]),
            "ratio": float(s["ratio"]),
            "r_k": [e[2] for e in eps],
        })
    return per_motif


def evolve_and_collect_40snap(seed, L_eff):
    rng = np.random.default_rng(seed)
    p = rng.uniform(0.3, 0.7, size=(fr.SIZE, fr.SIZE))
    per_motif_all = []
    snap_index = 0
    for step in range(fr.STEPS):
        p = ed_step_mobility(
            p, alpha=fr.ALPHA0, gamma=fr.GAMMA, dt=fr.DT,
            p_min=fr.P_MIN, p_max=fr.P_MAX, boundary=fr.BOUNDARY,
            mobility_exp=fr.MOBILITY_EXP, noise_scale=fr.NOISE0, rng=rng,
        )
        if step >= XI_BURN_IN and (step - XI_BURN_IN) % XI_SNAP_EVERY == 0:
            for m in collect_motifs_snapshot(p, L_eff):
                m["snap_index"] = snap_index
                per_motif_all.append(m)
            snap_index += 1
    return per_motif_all


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

    # -- 1. Load canonical per-seed ξ --------------------------------------
    with open(XI_JSON_PATH) as f:
        xi_doc = json.load(f)
    xi_per_seed = {int(k): float(v) for k, v in xi_doc["xi_per_seed"].items()}
    canonical_seeds = [int(s) for s in xi_doc["seeds"]]
    assert set(canonical_seeds) == set(int(s) for s in fr.SEEDS), (
        "canonical seeds in xi_canonical.json do not match "
        "r2_grf_falsifier_tests.SEEDS")
    print(f"Loaded canonical ξ for {len(canonical_seeds)} seeds "
          f"from {XI_JSON_PATH}", file=sys.stderr)

    # -- 2. Load ED-SC 3.3.6 per-seed verdicts for annotation -------------
    try:
        with open(ED_SC_3_3_6_JSON) as f:
            doc_336 = json.load(f)
        stats_336 = {int(r["seed"]): r for r in doc_336["per_seed_stats"]}
        flat_336 = doc_336["cross_seed_flatness"]["flat_thresh"]
    except FileNotFoundError:
        stats_336 = {}
        flat_336 = 0.20
        print("WARNING: ED-SC 3.3.6 summary not found; will skip "
              "pre-remediation annotations.", file=sys.stderr)

    # -- 3. Build per-seed (L_ray, s, L_eff) table ------------------------
    seed_Leff_table = []
    for seed in canonical_seeds:
        xi_i = xi_per_seed[seed]
        L_ray_i = DIMLESS_HINGE * xi_i
        L_eff_i, s_i = L_eff_of(L_ray_i)
        seed_Leff_table.append((seed, xi_i, L_ray_i, s_i, L_eff_i))

    # Resonance-window guard on L_eff values
    assert_no_resonance([(s, Le) for s, _, _, _, Le in seed_Leff_table])

    # -- 4. ξ guardrail (inherited; no re-measurement) --------------------
    xi_vals = list(xi_per_seed.values())
    n_pass = sum(1 for x in xi_vals
                 if math.isfinite(x)
                 and abs(x - XI_CANONICAL) / XI_CANONICAL < XI_GUARDRAIL_TOL)
    xi_guardrail = {
        "method": ("inherited from outputs/ed_sc_3_1/xi_canonical.json "
                   "(canonical 40-snapshot half-decay)"),
        "tolerance": XI_GUARDRAIL_TOL,
        "xi_canonical": XI_CANONICAL,
        "per_seed": xi_per_seed,
        "n_pass": n_pass,
        "min_pass": XI_GUARDRAIL_MIN_PASS,
        "pass": n_pass >= XI_GUARDRAIL_MIN_PASS,
    }

    # -- 5. Per-seed motif collection at L_eff ----------------------------
    per_seed_rows = []
    pool_rows = []
    for seed, xi_i, L_ray_i, s_i, L_eff_i in seed_Leff_table:
        ts = time.time()
        per_motif = evolve_and_collect_40snap(seed, L_eff_i)
        ratios = [m["ratio"] for m in per_motif]
        bs = bootstrap_median_iqr(ratios)
        s3 = tail_log_slope(ratios)
        row = {
            "seed": seed,
            "xi_i": xi_i,
            "L_ray_i": L_ray_i,
            "s_index": s_i,
            "L_eff_i": L_eff_i,
            "N_i": int(bs["n"]),
            "S1_i": bs["median"],
            "S1_i_CI": bs["median_ci"],
            "S2_i": bs["iqr"],
            "S2_i_CI": bs["iqr_ci"],
            "S3_i": s3,
            "wall_seconds": time.time() - ts,
        }
        per_seed_rows.append(row)
        for m in per_motif:
            pool_rows.append({
                "seed": seed, "xi_i": xi_i, "L_eff_i": L_eff_i,
                "s_index": s_i, "snap_index": m["snap_index"],
                "i": m["i"], "j": m["j"],
                "lam_neg": m["lam_neg"], "lam_pos": m["lam_pos"],
                "ratio": m["ratio"],
            })
        print(f"  seed={seed:>4}  ξ={xi_i:.4f}  L_ray={L_ray_i:.4f}  "
              f"s={s_i}  L_eff={L_eff_i:.4f}  N={bs['n']:>4}  "
              f"S1={bs['median']}  S2={bs['iqr']}  "
              f"t={time.time()-ts:.1f}s", file=sys.stderr)

    # -- 6. Pooled + deviations -------------------------------------------
    pooled_ratios = [r["ratio"] for r in pool_rows]
    bs_pool = bootstrap_median_iqr(pooled_ratios)
    s3_pool = tail_log_slope(pooled_ratios)
    S1_pool = bs_pool["median"]
    S2_pool = bs_pool["iqr"]

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
        s2_rel_sem = s2_std / (abs(S2_pool) * math.sqrt(len(s2_vals)))
    else:
        s2_rel_sem = None

    flat_thresh = (max(0.20, 2 * s2_rel_sem)
                   if s2_rel_sem is not None else 0.20)
    max_dS1 = max(dS1) if dS1 else None
    max_dS2 = max(dS2) if dS2 else None

    # -- 7. Per-seed pre/post annotation ----------------------------------
    for r in per_seed_rows:
        prev = stats_336.get(r["seed"], {})
        prev_d1 = prev.get("dS1_i")
        prev_d2 = prev.get("dS2_i")
        prev_fail = ((prev_d1 is not None and prev_d1 >= flat_336) or
                     (prev_d2 is not None and prev_d2 >= flat_336))
        curr_fail = ((r["dS1_i"] is not None and r["dS1_i"] >= flat_thresh)
                     or (r["dS2_i"] is not None
                         and r["dS2_i"] >= flat_thresh))
        r["pre_remediation_336"] = {
            "S1_prev": prev.get("S1_i"),
            "S2_prev": prev.get("S2_i"),
            "dS1_prev": prev_d1,
            "dS2_prev": prev_d2,
            "was_failing": prev_fail,
        }
        r["is_failing"] = curr_fail

    # -- 8. Verdict --------------------------------------------------------
    # Collapsed-seed456-only: seed 456 (previously H-coord) now passes;
    # seeds 789, 1213 (H-shallow) still fail as expected; S1 collapses.
    # Collapsed: everyone passes.
    # Broken-collapse: seed 456 still fails OR S1 broke OR new failure.
    # GuardrailFailure: ξ guardrail or window intrusion.

    if not xi_guardrail["pass"]:
        verdict = "GuardrailFailure"
        verdict_reason = "xi guardrail < min_pass"
    else:
        s1_ok = all(r["dS1_i"] is not None and r["dS1_i"] < flat_thresh
                    for r in per_seed_rows)
        failing_now = [r["seed"] for r in per_seed_rows if r["is_failing"]]
        seed_456 = next(r for r in per_seed_rows if r["seed"] == 456)
        seed_456_passes = not seed_456["is_failing"]

        if not s1_ok:
            verdict = "Broken-collapse"
            verdict_reason = ("S1 invariance broke under L_eff "
                              f"(max dS1={max_dS1} >= flat_thresh "
                              f"{flat_thresh:.4f})")
        elif len(failing_now) == 0:
            verdict = "Collapsed"
            verdict_reason = ("All 10 seeds within size-corrected "
                              f"flat_thresh {flat_thresh:.4f} under "
                              "shell-aware coordinate")
        elif seed_456_passes and set(failing_now).issubset({789, 1213}):
            verdict = "Collapsed-seed456-only"
            verdict_reason = ("Seed 456 (H-coord) now within flat_thresh "
                              f"{flat_thresh:.4f}; H-shallow seeds "
                              f"{failing_now} remain failing as "
                              "expected per ED-SC 3.3.9 "
                              "(ensemble-only S2 invariance)")
        else:
            verdict = "Broken-collapse"
            verdict_reason = (f"Unexpected failure pattern: "
                              f"failing_now={failing_now}, "
                              f"seed_456_passes={seed_456_passes}")

    # -- 9. Write per-seed pool CSV ---------------------------------------
    csv_path = os.path.join(OUT_DIR, "per_seed_shellaware_pools.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["seed", "xi_i", "L_eff_i", "s_index", "snap_index",
                    "i", "j", "lam_neg", "lam_pos", "ratio"])
        for row in pool_rows:
            w.writerow([row["seed"], row["xi_i"], row["L_eff_i"],
                        row["s_index"], row["snap_index"],
                        row["i"], row["j"],
                        row["lam_neg"], row["lam_pos"], row["ratio"]])

    # -- 10. Write master summary JSON ------------------------------------
    out = {
        "method": ("ED-SC 3.3.8b shell-aware per-seed collapse test: "
                   "per-seed L_eff = √2 · round(0.707 · 1.08 · ξ_i) "
                   "replaces L_ray = 1.08·ξ_i; 40-snapshot pool per seed"),
        "simulator_of_record":
            "r2_grf_falsifier_tests.py + ED_Update_Rule.ed_step_mobility",
        "xi_canonical_lattice_units": XI_CANONICAL,
        "dimensionless_hinge": DIMLESS_HINGE,
        "alpha_filt": ALPHA_FILT,
        "N_req": N_REQ,
        "snapshot_schedule": {
            "burn_in": XI_BURN_IN, "snap_every": XI_SNAP_EVERY,
            "snapshots_per_seed": 40,
        },
        "canonical_params": {
            "alpha": fr.ALPHA0, "gamma": fr.GAMMA,
            "noise_sigma": fr.NOISE0,
            "mobility_exp": fr.MOBILITY_EXP,
            "steps": fr.STEPS, "size": fr.SIZE, "dt": fr.DT,
        },
        "seeds": canonical_seeds,
        "xi_json_source": XI_JSON_PATH,
        "ed_sc_3_3_6_source": ED_SC_3_3_6_JSON,
        "resonance_windows_excluded": {
            "A": list(WINDOW_A), "B": list(WINDOW_B)},
        "per_seed_L_table": [
            {"seed": s, "xi_i": x, "L_ray_i": Lr,
             "s_index": si, "L_eff_i": Le}
            for s, x, Lr, si, Le in seed_Leff_table],
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
            "S2_rel_SEM_across_seeds": s2_rel_sem,
            "flat_thresh": flat_thresh,
            "max_dS1": max_dS1,
            "max_dS2": max_dS2,
        },
        "verdict": verdict,
        "verdict_reason": verdict_reason,
        "wall_seconds_total": time.time() - t_master,
    }

    json_path = os.path.join(OUT_DIR, "per_seed_shellaware_summary.json")
    with open(json_path, "w") as f:
        json.dump(out, f, indent=2)

    print(f"\nWrote master summary → {json_path}", file=sys.stderr)
    print(json.dumps({
        "verdict": verdict,
        "verdict_reason": verdict_reason,
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
