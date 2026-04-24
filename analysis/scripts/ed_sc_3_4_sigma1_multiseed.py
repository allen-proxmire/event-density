"""ED-SC 3.4-σ₁ Multi-Seed driver (F2 follow-up).

Pre-registered in theory/ED_SC_3_4_sigma1_MultiSeed.md.

Measures the per-realisation σ₁_std spread across 10 seeds at the
canonical operating point ξ = 1.7575 lu, replacing the inherited
±25 % transfer band (from ED-SC 3.3.9 S2) in GR-SC 1.3-Scoping
Rule R5 (iii) with a directly-measured σ₁ coefficient of
variation.

Pipeline is identical to ed_sc_3_4_sigma1_calibration.py except
(i) only one ξ target (canonical), (ii) loop over 10 seeds with
per-seed calibration pre-pass. All motif extraction, bootstrap,
and diagnostic logic inherited verbatim.

Simulator of record:
  r2_grf_falsifier_tests.py  +  ED_Update_Rule.ed_step_mobility

Seeds: {11, 22, 33, 44, 55, 66, 77, 88, 99, 111} (includes 77 for
continuity with the single-seed ED-SC 3.4-σ₁ calibration; set is
distinct from the ED-SC 3.x canonical 10-seed ensemble).

Writes:
  outputs/ed_sc_3_4_sigma1/sigma1_multiseed_table.csv
  outputs/ed_sc_3_4_sigma1/sigma1_multiseed_summary.json

No simulator constants are mutated. Deterministic given seed.
"""
import csv
import json
import math
import os
import sys
import time
import numpy as np
from numpy.fft import fft2, ifft2, fftshift

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "ed_arch_r2"))
import r2_grf_falsifier_tests as fr  # noqa: E402

from ED_Update_Rule import ed_step_mobility  # noqa: E402

# ---------------------------------------------------------------------------
# Canonical constants (inherited verbatim from ed_sc_3_4_sigma1_calibration.py)
# ---------------------------------------------------------------------------
XI_CANONICAL = 1.7575325729470939
XI_BURN_IN = 100
XI_SNAP_EVERY = 10

ALPHA_FILT = 0.25
N_REQ = 4
DIMLESS_HINGE = 1.08
DIAG_COS = 0.707

WINDOW_A = (2.50, 2.80)
WINDOW_B = (3.50, 3.90)

XI_TARGET = 1.7575  # canonical, single value
SEEDS = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]
ANCHOR_SEED = 77  # rel_dev reported against this seed

CALIBRATION_W_GRID = [0.05, 0.08, 0.10, 0.13, 0.16, 0.20, 0.25, 0.30, 0.35]
CALIBRATION_TOL = 0.01

IQR_TO_STD = 1.349

OUT_DIR = os.path.join(HERE, "..", "..", "outputs", "ed_sc_3_4_sigma1")


# ---------------------------------------------------------------------------
# ξ measurement
# ---------------------------------------------------------------------------
def xi_halfdecay(field, dx=1.0):
    N = field.shape[0]
    f = field - np.mean(field)
    F = fft2(f)
    C = fftshift(np.real(ifft2(F * np.conj(F)))) / (N * N)
    c0 = C[N // 2, N // 2]
    if c0 <= 0:
        return float('nan')
    y, x = np.indices(C.shape)
    r = np.sqrt((x - N // 2) ** 2 + (y - N // 2) ** 2).astype(int)
    rmax = N // 2
    prof = np.empty(rmax)
    for k in range(rmax):
        mask = (r == k)
        prof[k] = C[mask].mean() if mask.any() else 0.0
    prof /= c0
    for k in range(1, rmax):
        if prof[k] <= 0.5:
            if prof[k - 1] == prof[k]:
                return float(k) * dx
            return float(k - 1 + (prof[k - 1] - 0.5)
                         / (prof[k - 1] - prof[k])) * dx
    return float(rmax) * dx


# ---------------------------------------------------------------------------
# Evolution + per-seed calibration
# ---------------------------------------------------------------------------
def evolve_40snap(seed, w):
    rng = np.random.default_rng(seed)
    p = rng.uniform(0.5 - w, 0.5 + w, size=(fr.SIZE, fr.SIZE))
    snaps = []
    xis = []
    for step in range(fr.STEPS):
        p = ed_step_mobility(
            p, alpha=fr.ALPHA0, gamma=fr.GAMMA, dt=fr.DT,
            p_min=fr.P_MIN, p_max=fr.P_MAX, boundary=fr.BOUNDARY,
            mobility_exp=fr.MOBILITY_EXP, noise_scale=fr.NOISE0, rng=rng,
        )
        if step >= XI_BURN_IN and (step - XI_BURN_IN) % XI_SNAP_EVERY == 0:
            snaps.append(p.copy())
            xis.append(xi_halfdecay(p))
    return snaps, xis


def run_calibration_for_seed(seed):
    results = []
    for w in CALIBRATION_W_GRID:
        ts = time.time()
        _, xis = evolve_40snap(seed, w)
        xi_mean = float(np.mean([x for x in xis if np.isfinite(x)]))
        results.append({"w": w, "xi": xi_mean,
                        "wall_seconds": time.time() - ts})
    results.sort(key=lambda r: r["xi"])
    return results


def interpolate_w(calibration, xi_target):
    xs = [r["xi"] for r in calibration]
    ws = [r["w"] for r in calibration]
    if xi_target <= xs[0]:
        return ws[0]
    if xi_target >= xs[-1]:
        return ws[-1]
    for i in range(len(xs) - 1):
        if xs[i] <= xi_target <= xs[i + 1]:
            a = (xi_target - xs[i]) / (xs[i + 1] - xs[i])
            return ws[i] * (1 - a) + ws[i + 1] * a
    return ws[-1]


# ---------------------------------------------------------------------------
# Guards
# ---------------------------------------------------------------------------
def in_window(L, win):
    return win[0] <= L <= win[1]


def r_diag_of(L):
    return int(round(DIAG_COS * L))


def assert_no_resonance_plan():
    L = DIMLESS_HINGE * XI_TARGET
    if in_window(L, WINDOW_A) or in_window(L, WINDOW_B):
        raise RuntimeError(
            f"Planned ξ_target={XI_TARGET} yields L_ray={L:.4f} in a "
            f"resonance window. Refusing to launch.")


# ---------------------------------------------------------------------------
# Motif extraction + stats
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


def collect_motifs_snapshot(snapshot, L_ray):
    E = fr.smooth_field(snapshot)
    p_hat = float(snapshot.mean())
    p_std = float(snapshot.std())
    sads = fr.find_morse_saddles(E)
    out = []
    for s in sads:
        if not fr.motif_pass(s, E, p_hat, p_std,
                             ALPHA_FILT, L_ray, N_REQ):
            continue
        T = float(s["lam_neg"]) + float(s["lam_pos"])
        eps = endpoints_of(s, L_ray)
        out.append({"T": T, "r_k": [float(e[2]) for e in eps]})
    return out


def collect_motifs_40snap(snapshots, L_ray):
    all_T = []
    all_shells = []
    per_snap = []
    for snap_idx, p in enumerate(snapshots):
        ms = collect_motifs_snapshot(p, L_ray)
        T_snap = [m["T"] for m in ms]
        for m in ms:
            all_T.append(m["T"])
            all_shells.extend(m["r_k"])
        if len(T_snap) >= 4:
            per_snap.append({
                "snap": snap_idx, "N": len(T_snap),
                "median": float(np.median(T_snap)),
                "iqr": float(np.quantile(T_snap, 0.75)
                              - np.quantile(T_snap, 0.25)),
                "std": float(np.std(T_snap, ddof=1)),
            })
        else:
            per_snap.append({
                "snap": snap_idx, "N": len(T_snap),
                "median": (float(np.median(T_snap))
                           if T_snap else None),
                "iqr": None, "std": None,
            })
    return all_T, all_shells, per_snap


def bootstrap_median_std(values, B=4000, rng_seed=99):
    v = np.asarray([x for x in values if np.isfinite(x)])
    if len(v) < 3:
        return dict(n=int(len(v)),
                    median=None, median_ci=[None, None],
                    std=None, std_ci=[None, None],
                    iqr=None, iqr_ci=[None, None])
    rng = np.random.default_rng(rng_seed)
    meds, stds, iqrs = [], [], []
    for _ in range(B):
        smp = rng.choice(v, size=len(v), replace=True)
        meds.append(np.median(smp))
        stds.append(np.std(smp, ddof=1))
        iqrs.append(np.quantile(smp, 0.75) - np.quantile(smp, 0.25))
    return dict(
        n=int(len(v)),
        median=float(np.median(v)),
        median_ci=[float(np.quantile(meds, 0.16)),
                   float(np.quantile(meds, 0.84))],
        std=float(np.std(v, ddof=1)),
        std_ci=[float(np.quantile(stds, 0.16)),
                float(np.quantile(stds, 0.84))],
        iqr=float(np.quantile(v, 0.75) - np.quantile(v, 0.25)),
        iqr_ci=[float(np.quantile(iqrs, 0.16)),
                float(np.quantile(iqrs, 0.84))],
    )


def shell_histogram(shell_list):
    h = {}
    for r in shell_list:
        key = f"{r:.4f}"
        h[key] = h.get(key, 0) + 1
    return h


# ---------------------------------------------------------------------------
# Per-seed execution
# ---------------------------------------------------------------------------
def run_seed(seed):
    t_seed = time.time()
    print(f"Seed {seed} — calibration pre-pass...", file=sys.stderr)
    calibration = run_calibration_for_seed(seed)
    w = interpolate_w(calibration, XI_TARGET)

    snapshots, xis = evolve_40snap(seed, w)
    xi_finite = [x for x in xis if np.isfinite(x)]
    xi_measured = float(np.mean(xi_finite)) if xi_finite else float('nan')
    miss = (abs(xi_measured - XI_TARGET) / XI_TARGET
            if XI_TARGET != 0 else float('inf'))

    refinement_used = False
    if miss > CALIBRATION_TOL and xi_finite:
        if xi_measured < XI_TARGET:
            w_new = max(min(CALIBRATION_W_GRID), w * 0.85)
        else:
            w_new = min(max(CALIBRATION_W_GRID), w * 1.15)
        snapshots_new, xis_new = evolve_40snap(seed, w_new)
        xi_finite_new = [x for x in xis_new if np.isfinite(x)]
        xi_new = (float(np.mean(xi_finite_new))
                  if xi_finite_new else xi_measured)
        miss_new = (abs(xi_new - XI_TARGET) / XI_TARGET
                    if XI_TARGET != 0 else float('inf'))
        if miss_new < miss:
            w = w_new
            xi_measured = xi_new
            snapshots = snapshots_new
            miss = miss_new
            refinement_used = True

    L_ray = DIMLESS_HINGE * xi_measured
    if in_window(L_ray, WINDOW_A) or in_window(L_ray, WINDOW_B):
        raise RuntimeError(
            f"seed {seed}: L_ray={L_ray:.4f} intersects a resonance window.")
    r_diag = r_diag_of(L_ray)
    out_of_scope = (r_diag != 1)

    all_T, all_shells, per_snap = collect_motifs_40snap(snapshots, L_ray)
    bs = bootstrap_median_std(all_T)
    sigma1_std = bs["std"]
    sigma1_IQR_proxy = ((bs["iqr"] / IQR_TO_STD)
                        if bs["iqr"] is not None else None)

    N_per_snap = [ps["N"] for ps in per_snap]
    N_per_snap_mean = (float(np.mean(N_per_snap))
                       if N_per_snap else None)

    result = {
        "seed": seed,
        "xi_target": XI_TARGET,
        "xi_measured": xi_measured,
        "xi_miss_fraction": miss,
        "w_used": w,
        "refinement_used": refinement_used,
        "L_ray": L_ray,
        "r_diag": r_diag,
        "out_of_scope": out_of_scope,
        "N_pool": int(bs["n"]),
        "median_T": bs["median"],
        "median_T_CI": bs["median_ci"],
        "sigma1_std": sigma1_std,
        "sigma1_std_CI": bs["std_ci"],
        "sigma1_IQR_proxy": sigma1_IQR_proxy,
        "IQR_T": bs["iqr"],
        "IQR_T_CI": bs["iqr_ci"],
        "shell_histogram": shell_histogram(all_shells),
        "N_per_snap": N_per_snap,
        "N_per_snap_mean": N_per_snap_mean,
        "per_snapshot_stats": per_snap,
        "calibration_prepass": calibration,
        "wall_seconds": time.time() - t_seed,
    }
    print(f"  seed={seed}  ξ_meas={xi_measured:.4f} "
          f"(miss {miss*100:.2f}%, refined={refinement_used})  "
          f"N={bs['n']}  med_T={bs['median']}  σ₁_std={sigma1_std}  "
          f"σ₁_IQR={sigma1_IQR_proxy}  OOS={out_of_scope}  "
          f"t={time.time()-t_seed:.1f}s",
          file=sys.stderr)
    return result


# ---------------------------------------------------------------------------
# Cross-seed aggregate
# ---------------------------------------------------------------------------
def aggregate(per_seed_results):
    sigma1_std_values = [r["sigma1_std"] for r in per_seed_results
                         if r["sigma1_std"] is not None]
    sigma1_IQR_values = [r["sigma1_IQR_proxy"] for r in per_seed_results
                         if r["sigma1_IQR_proxy"] is not None]
    median_T_values = [r["median_T"] for r in per_seed_results
                       if r["median_T"] is not None]

    def stats(vals):
        if not vals:
            return {"mean": None, "std": None, "iqr": None, "CoV": None,
                    "min": None, "max": None, "n": 0}
        arr = np.asarray(vals)
        mean = float(arr.mean())
        std = float(arr.std(ddof=1)) if len(arr) >= 2 else 0.0
        iqr = float(np.quantile(arr, 0.75) - np.quantile(arr, 0.25))
        cov = float(std / mean) if mean != 0 else None
        return {
            "mean": mean, "std": std, "iqr": iqr, "CoV": cov,
            "min": float(arr.min()), "max": float(arr.max()),
            "n": int(len(arr)),
        }

    sigma1_std_agg = stats(sigma1_std_values)
    sigma1_IQR_agg = stats(sigma1_IQR_values)
    median_T_agg = stats(median_T_values)

    # Anchor: deviation vs seed 77
    anchor_val = None
    for r in per_seed_results:
        if r["seed"] == ANCHOR_SEED:
            anchor_val = r["sigma1_std"]
            break
    rel_dev_vs_anchor = []
    for r in per_seed_results:
        if anchor_val is None or r["sigma1_std"] is None or anchor_val == 0:
            rel_dev_vs_anchor.append({"seed": r["seed"], "rel_dev": None})
        else:
            rel_dev_vs_anchor.append({
                "seed": r["seed"],
                "rel_dev": float((r["sigma1_std"] - anchor_val) / anchor_val),
            })

    # Rigid-zero cross-seed check: does the median_T distribution contain 0?
    rigid_zero_cross = {
        "median_T_mean": median_T_agg["mean"],
        "median_T_std": median_T_agg["std"],
        "contains_zero": (median_T_agg["mean"] is not None
                          and abs(median_T_agg["mean"])
                          < 2 * (median_T_agg["std"] or 0)),
    }

    # Gaussianity cross-seed: ratio of means
    gauss_ratio = None
    if (sigma1_std_agg["mean"] is not None
            and sigma1_IQR_agg["mean"] is not None
            and sigma1_IQR_agg["mean"] != 0):
        gauss_ratio = sigma1_std_agg["mean"] / sigma1_IQR_agg["mean"]

    return {
        "sigma1_std_values": sigma1_std_values,
        "sigma1_std_aggregate": sigma1_std_agg,
        "sigma1_IQR_proxy_values": sigma1_IQR_values,
        "sigma1_IQR_proxy_aggregate": sigma1_IQR_agg,
        "median_T_values": median_T_values,
        "median_T_aggregate": median_T_agg,
        "anchor_seed": ANCHOR_SEED,
        "anchor_sigma1_std": anchor_val,
        "rel_dev_vs_anchor": rel_dev_vs_anchor,
        "rigid_zero_cross_seed": rigid_zero_cross,
        "gaussianity_ratio_mean_std_over_IQR_mean": gauss_ratio,
    }


# ---------------------------------------------------------------------------
# Master driver
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    t_master = time.time()

    assert_no_resonance_plan()
    print(f"Multi-seed σ₁ scan at ξ_target = {XI_TARGET} lu, "
          f"{len(SEEDS)} seeds", file=sys.stderr)

    per_seed_results = []
    for seed in SEEDS:
        per_seed_results.append(run_seed(seed))

    agg = aggregate(per_seed_results)

    r_diag_excursions = [
        {"seed": r["seed"], "xi_measured": r["xi_measured"],
         "L_ray": r["L_ray"], "r_diag": r["r_diag"]}
        for r in per_seed_results if r["out_of_scope"]
    ]

    # Write CSV
    csv_path = os.path.join(OUT_DIR, "sigma1_multiseed_table.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "seed", "xi_target", "xi_measured", "miss_frac", "w_used",
            "refined", "L_ray", "r_diag", "out_of_scope",
            "N_pool",
            "median_T", "median_T_lo", "median_T_hi",
            "sigma1_std", "sigma1_std_lo", "sigma1_std_hi",
            "sigma1_IQR_proxy",
            "N_per_snap_mean",
            "rel_dev_vs_seed77",
        ])
        rel_dev_map = {e["seed"]: e["rel_dev"]
                       for e in agg["rel_dev_vs_anchor"]}
        for r in per_seed_results:
            mci = r["median_T_CI"] or [None, None]
            sci = r["sigma1_std_CI"] or [None, None]
            w.writerow([
                r["seed"], r["xi_target"], r["xi_measured"],
                r["xi_miss_fraction"], r["w_used"], r["refinement_used"],
                r["L_ray"], r["r_diag"], r["out_of_scope"],
                r["N_pool"],
                r["median_T"], mci[0], mci[1],
                r["sigma1_std"], sci[0], sci[1],
                r["sigma1_IQR_proxy"],
                r["N_per_snap_mean"],
                rel_dev_map.get(r["seed"]),
            ])

    # Write JSON summary
    out = {
        "method": ("ED-SC 3.4-σ₁ F2 follow-up: multi-seed σ₁ measurement "
                   "at canonical ξ = 1.7575 lu across 10 seeds; "
                   "direct replacement for Rule R5 (iii) per-realisation "
                   "transfer band in GR-SC 1.3-Scoping"),
        "simulator_of_record":
            "r2_grf_falsifier_tests.py + ED_Update_Rule.ed_step_mobility",
        "xi_canonical_lattice_units": XI_CANONICAL,
        "xi_target": XI_TARGET,
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
        "seeds": SEEDS,
        "anchor_seed": ANCHOR_SEED,
        "resonance_windows_excluded": {
            "A": list(WINDOW_A), "B": list(WINDOW_B)},
        "per_seed": per_seed_results,
        "cross_seed_aggregate": agg,
        "r_diag_excursions": r_diag_excursions,
        "wall_seconds_total": time.time() - t_master,
    }

    json_path = os.path.join(OUT_DIR, "sigma1_multiseed_summary.json")
    with open(json_path, "w") as f:
        json.dump(out, f, indent=2)

    print(f"\nWrote table → {csv_path}", file=sys.stderr)
    print(f"Wrote master summary → {json_path}", file=sys.stderr)
    print(json.dumps({
        "n_seeds": len(SEEDS),
        "n_in_scope": len(SEEDS) - len(r_diag_excursions),
        "sigma1_std_mean": agg["sigma1_std_aggregate"]["mean"],
        "sigma1_std_std": agg["sigma1_std_aggregate"]["std"],
        "sigma1_std_CoV": agg["sigma1_std_aggregate"]["CoV"],
        "sigma1_std_min": agg["sigma1_std_aggregate"]["min"],
        "sigma1_std_max": agg["sigma1_std_aggregate"]["max"],
        "rigid_zero_contains_zero":
            agg["rigid_zero_cross_seed"]["contains_zero"],
        "gauss_ratio":
            agg["gaussianity_ratio_mean_std_over_IQR_mean"],
        "wall_seconds_total": out["wall_seconds_total"],
    }, indent=2))


if __name__ == "__main__":
    main()
