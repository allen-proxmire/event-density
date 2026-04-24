"""ED-SC 3.4-σ₁ Calibration driver.

Pre-registered in theory/ED_SC_3_4_sigma1_Calibration.md.

9-point σ₁ calibration inside the canonical invariance domain
(r_diag = 1, ξ ∈ [1.60, 1.95] lu) on fixed seed 77 with IC-amplitude
ξ-control (inherited from ED-SC 3.4 and 3.3.8a). At each ξ point the
driver pools the Hessian-trace distribution T_motif = λ_neg + λ_pos
across all admitted motifs in 40 snapshots, computes bootstrap
median_T, std-based σ₁ and IQR-proxy σ₁, and records per-snapshot
stationarity diagnostics, endpoint shell histogram, and JS divergence
vs ξ = 1.80 reference.

After the scan, OLS σ₁(ξ) = a + b·ξ fit + RMS residual + R², plus
four diagnostic checks:
  - flat_check (total variation fraction)
  - trend_direction (sign of slope)
  - rigid_zero_check (all median_T CIs contain 0 → tenth-pass
    Trace-Gaussian-class rigid identity confirmed empirically at the
    motif-filter level)
  - gaussianity_check (σ₁_std vs σ₁_IQR_proxy agreement within 10 %)
  - r_diag_excursions (should be empty)

Simulator of record:
  r2_grf_falsifier_tests.py  +  ED_Update_Rule.ed_step_mobility

Fixed seed: 77. Canonical filter (α_filt = 0.25, N_req = 4). Canonical
hinge: L_ray = 1.08·ξ_measured.

Guards (hard-fail):
  - Resonance windows A [2.50, 2.80] and B [3.50, 3.90] on L_ray.
  - r_diag window: any point whose r_diag_measured ≠ 1 is flagged
    out-of-scope and excluded from the σ₁(ξ) fit.

Writes:
  outputs/ed_sc_3_4_sigma1/sigma1_calibration_table.csv
  outputs/ed_sc_3_4_sigma1/sigma1_calibration_summary.json

No simulator constants are mutated. Deterministic given (seed, w).
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
# Canonical constants (inherited, NOT mutated)
# ---------------------------------------------------------------------------
XI_CANONICAL = 1.7575325729470939
XI_BURN_IN = 100
XI_SNAP_EVERY = 10

ALPHA_FILT = 0.25
N_REQ = 4
DIMLESS_HINGE = 1.08
DIAG_COS = 0.707
FIXED_SEED = 77

WINDOW_A = (2.50, 2.80)
WINDOW_B = (3.50, 3.90)

XI_TARGETS = [1.60, 1.65, 1.70, 1.75, 1.80, 1.85, 1.90, 1.93, 1.95]
REF_INDEX = 4  # ξ = 1.80 is the reference histogram

CALIBRATION_W_GRID = [0.05, 0.08, 0.10, 0.13, 0.16, 0.20, 0.25, 0.30, 0.35]
CALIBRATION_TOL = 0.01

# Gaussian IQR → std conversion factor
IQR_TO_STD = 1.349

OUT_DIR = os.path.join(HERE, "..", "..", "outputs", "ed_sc_3_4_sigma1")


# ---------------------------------------------------------------------------
# ξ measurement (verbatim)
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
# Evolution with controllable IC half-width; 40 snapshots
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


# ---------------------------------------------------------------------------
# Calibration pre-pass + interpolation
# ---------------------------------------------------------------------------
def run_calibration(seed):
    results = []
    for w in CALIBRATION_W_GRID:
        ts = time.time()
        _, xis = evolve_40snap(seed, w)
        xi_mean = float(np.mean([x for x in xis if np.isfinite(x)]))
        results.append({"w": w, "xi": xi_mean,
                        "wall_seconds": time.time() - ts})
        print(f"  cal w={w:.3f}  ξ={xi_mean:.4f}  "
              f"t={time.time()-ts:.1f}s", file=sys.stderr)
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


def assert_no_resonance_plan(xi_targets):
    for xi in xi_targets:
        L = DIMLESS_HINGE * xi
        if in_window(L, WINDOW_A) or in_window(L, WINDOW_B):
            raise RuntimeError(
                f"Planned ξ_target={xi} yields L_ray={L:.4f} in a "
                f"resonance window. Refusing to launch.")


def r_diag_of(L):
    return int(round(DIAG_COS * L))


# ---------------------------------------------------------------------------
# Motif extraction — record trace T_motif and endpoint shells
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
    """Returns list of (T_motif, shell_radii[4]) for each admitted motif."""
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
    """Returns (all_T, all_shells, per_snap_stats).

    all_T: list of T_motif values pooled across snapshots
    all_shells: list of shell radii across all endpoints (4·N_motifs)
    per_snap_stats: list of {snap, N, median_T, iqr_T}
    """
    all_T = []
    all_shells = []
    per_snap_stats = []
    for snap_idx, p in enumerate(snapshots):
        ms = collect_motifs_snapshot(p, L_ray)
        T_snap = [m["T"] for m in ms]
        for m in ms:
            all_T.append(m["T"])
            all_shells.extend(m["r_k"])
        # Per-snapshot diagnostic
        if len(T_snap) >= 4:
            per_snap_stats.append({
                "snap": snap_idx, "N": len(T_snap),
                "median": float(np.median(T_snap)),
                "iqr": float(np.quantile(T_snap, 0.75)
                              - np.quantile(T_snap, 0.25)),
                "std": float(np.std(T_snap, ddof=1)),
            })
        else:
            per_snap_stats.append({
                "snap": snap_idx, "N": len(T_snap),
                "median": (float(np.median(T_snap))
                           if T_snap else None),
                "iqr": None, "std": None,
            })
    return all_T, all_shells, per_snap_stats


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------
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


def jensen_shannon(hist_a, hist_b):
    keys = sorted(set(hist_a.keys()) | set(hist_b.keys()),
                  key=lambda k: float(k))
    ta = sum(hist_a.values()) or 1
    tb = sum(hist_b.values()) or 1
    pa = np.array([hist_a.get(k, 0) / ta for k in keys])
    pb = np.array([hist_b.get(k, 0) / tb for k in keys])
    m = 0.5 * (pa + pb)
    def kl(p, q):
        s = 0.0
        for pi, qi in zip(p, q):
            if pi > 0 and qi > 0:
                s += pi * math.log(pi / qi)
        return s
    return 0.5 * kl(pa, m) + 0.5 * kl(pb, m)


def ols_slope_residuals(xs, ys):
    pts = [(x, y) for x, y in zip(xs, ys) if x is not None and y is not None]
    if len(pts) < 2:
        return None
    xa = np.array([p[0] for p in pts])
    ya = np.array([p[1] for p in pts])
    b, a = np.polyfit(xa, ya, 1)
    fit = a + b * xa
    resid = ya - fit
    ss_res = float(np.sum(resid ** 2))
    ss_tot = float(np.sum((ya - ya.mean()) ** 2))
    r2 = 1.0 - (ss_res / ss_tot if ss_tot > 0 else 0.0)
    return {
        "slope": float(b),
        "intercept": float(a),
        "residuals": [float(r) for r in resid],
        "rms_residual": float(np.sqrt(ss_res / len(resid))),
        "R_squared": float(r2),
    }


# ---------------------------------------------------------------------------
# Per-point execution
# ---------------------------------------------------------------------------
def run_scan_point(xi_target, calibration):
    t0 = time.time()
    w = interpolate_w(calibration, xi_target)

    snapshots, xis = evolve_40snap(FIXED_SEED, w)
    xi_finite = [x for x in xis if np.isfinite(x)]
    xi_measured = float(np.mean(xi_finite)) if xi_finite else float('nan')
    miss = (abs(xi_measured - xi_target) / xi_target
            if xi_target != 0 else float('inf'))

    refinement_used = False
    if miss > CALIBRATION_TOL and xi_finite:
        if xi_measured < xi_target:
            w_new = max(min(CALIBRATION_W_GRID), w * 0.85)
        else:
            w_new = min(max(CALIBRATION_W_GRID), w * 1.15)
        snapshots_new, xis_new = evolve_40snap(FIXED_SEED, w_new)
        xi_finite_new = [x for x in xis_new if np.isfinite(x)]
        xi_new = (float(np.mean(xi_finite_new))
                  if xi_finite_new else xi_measured)
        miss_new = (abs(xi_new - xi_target) / xi_target
                    if xi_target != 0 else float('inf'))
        if miss_new < miss:
            w = w_new
            xi_measured = xi_new
            snapshots = snapshots_new
            miss = miss_new
            refinement_used = True

    L_ray = DIMLESS_HINGE * xi_measured

    if in_window(L_ray, WINDOW_A) or in_window(L_ray, WINDOW_B):
        raise RuntimeError(
            f"ξ_target={xi_target}: L_ray={L_ray:.4f} intersects a "
            f"resonance window. Aborting scan.")
    r_diag = r_diag_of(L_ray)
    out_of_scope = (r_diag != 1)

    all_T, all_shells, per_snap = collect_motifs_40snap(snapshots, L_ray)
    bs = bootstrap_median_std(all_T)

    sigma1_std = bs["std"]
    sigma1_IQR_proxy = ((bs["iqr"] / IQR_TO_STD)
                        if bs["iqr"] is not None else None)

    hist = shell_histogram(all_shells)

    N_per_snap = [ps["N"] for ps in per_snap]
    N_per_snap_mean = (float(np.mean(N_per_snap))
                       if N_per_snap else None)

    return {
        "xi_target": xi_target,
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
        "shell_histogram": hist,
        "N_per_snap": N_per_snap,
        "N_per_snap_mean": N_per_snap_mean,
        "per_snapshot_stats": per_snap,
        "wall_seconds": time.time() - t0,
    }


# ---------------------------------------------------------------------------
# Master driver
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    t_master = time.time()

    assert_no_resonance_plan(XI_TARGETS)

    # 1. Calibration pre-pass
    print(f"Calibration pre-pass: sweeping IC half-width w on seed "
          f"{FIXED_SEED}...", file=sys.stderr)
    calibration = run_calibration(FIXED_SEED)

    # 2. Scan
    print(f"\nσ₁-calibration scan: {len(XI_TARGETS)} points "
          f"at seed={FIXED_SEED}", file=sys.stderr)
    scan_points = []
    for xi_target in XI_TARGETS:
        print(f"  ξ_target={xi_target} ...", file=sys.stderr)
        pt = run_scan_point(xi_target, calibration)
        scan_points.append(pt)
        print(f"    ξ_meas={pt['xi_measured']:.4f} "
              f"(miss {pt['xi_miss_fraction']*100:.2f}%, "
              f"refined={pt['refinement_used']})  "
              f"L={pt['L_ray']:.4f}  r_diag={pt['r_diag']}  "
              f"N={pt['N_pool']}  "
              f"med_T={pt['median_T']}  σ₁_std={pt['sigma1_std']}  "
              f"σ₁_IQR={pt['sigma1_IQR_proxy']}  "
              f"OOS={pt['out_of_scope']}",
              file=sys.stderr)

    # 3. JS divergences vs ξ = 1.80 reference
    ref_hist = scan_points[REF_INDEX]["shell_histogram"]
    for pt in scan_points:
        pt["JS_vs_ref"] = jensen_shannon(pt["shell_histogram"], ref_hist)

    # 4. r_diag excursions
    r_diag_excursions = [
        {"xi_target": pt["xi_target"],
         "xi_measured": pt["xi_measured"],
         "L_ray": pt["L_ray"],
         "r_diag": pt["r_diag"]}
        for pt in scan_points if pt["out_of_scope"]
    ]

    # 5. OLS fits on in-scope points
    in_scope = [pt for pt in scan_points if not pt["out_of_scope"]]
    xi_vals = [pt["xi_measured"] for pt in in_scope]
    sigma1_vals = [pt["sigma1_std"] for pt in in_scope]
    sigma1_IQR_vals = [pt["sigma1_IQR_proxy"] for pt in in_scope]
    medT_vals = [pt["median_T"] for pt in in_scope]

    sigma1_fit = ols_slope_residuals(xi_vals, sigma1_vals)
    sigma1_IQR_fit = ols_slope_residuals(xi_vals, sigma1_IQR_vals)

    # Derived diagnostic quantities
    if sigma1_fit is not None:
        dxi = max(xi_vals) - min(xi_vals)
        s1_total_variation = abs(sigma1_fit["slope"]) * dxi
        s1_ref = float(np.mean(sigma1_vals)) if sigma1_vals else 0.0
        flat_check = {
            "total_variation": float(s1_total_variation),
            "fraction_of_ref": float(s1_total_variation / abs(s1_ref)
                                     if s1_ref != 0 else 0.0),
            "near_flat_prior_020": bool(
                s1_total_variation / abs(s1_ref) < 0.20
                if s1_ref != 0 else False),
        }
        trend_direction = (
            "positive" if sigma1_fit["slope"] > 0
            else "negative" if sigma1_fit["slope"] < 0 else "zero")
    else:
        flat_check = None
        trend_direction = None

    # rigid_zero_check: all median_T CIs must contain 0
    rigid_zero_rows = []
    rigid_zero_all_pass = True
    for pt in scan_points:
        ci = pt["median_T_CI"]
        if ci is None or ci[0] is None or ci[1] is None:
            rigid_zero_rows.append({
                "xi_target": pt["xi_target"],
                "median_T": pt["median_T"],
                "median_T_CI": ci,
                "contains_zero": None,
            })
            rigid_zero_all_pass = False
        else:
            contains_zero = (ci[0] <= 0 <= ci[1])
            rigid_zero_rows.append({
                "xi_target": pt["xi_target"],
                "median_T": pt["median_T"],
                "median_T_CI": ci,
                "contains_zero": bool(contains_zero),
            })
            if not contains_zero:
                rigid_zero_all_pass = False
    rigid_zero_check = {
        "pass": bool(rigid_zero_all_pass),
        "per_point": rigid_zero_rows,
    }

    # gaussianity_check: |σ₁_std - σ₁_IQR_proxy| / σ₁_std < 0.10 at each point
    gaussianity_rows = []
    gaussianity_all_pass = True
    for pt in scan_points:
        s = pt["sigma1_std"]
        i = pt["sigma1_IQR_proxy"]
        if s is None or i is None or s == 0:
            row = {
                "xi_target": pt["xi_target"],
                "sigma1_std": s,
                "sigma1_IQR_proxy": i,
                "rel_diff": None,
                "pass": None,
            }
            gaussianity_rows.append(row)
            gaussianity_all_pass = False
            continue
        rel_diff = abs(s - i) / abs(s)
        p = rel_diff < 0.10
        gaussianity_rows.append({
            "xi_target": pt["xi_target"],
            "sigma1_std": s,
            "sigma1_IQR_proxy": i,
            "rel_diff": float(rel_diff),
            "pass": bool(p),
        })
        if not p:
            gaussianity_all_pass = False
    gaussianity_check = {
        "pass": bool(gaussianity_all_pass),
        "per_point": gaussianity_rows,
    }

    # 6. Write CSV
    csv_path = os.path.join(OUT_DIR, "sigma1_calibration_table.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["xi_target", "xi_measured", "miss_frac", "w_used",
                    "refined", "L_ray", "r_diag", "out_of_scope",
                    "N_pool",
                    "median_T", "median_T_lo", "median_T_hi",
                    "sigma1_std", "sigma1_std_lo", "sigma1_std_hi",
                    "sigma1_IQR_proxy",
                    "JS_vs_ref", "N_per_snap_mean"])
        for pt in scan_points:
            mci = pt["median_T_CI"] or [None, None]
            sci = pt["sigma1_std_CI"] or [None, None]
            w.writerow([
                pt["xi_target"], pt["xi_measured"], pt["xi_miss_fraction"],
                pt["w_used"], pt["refinement_used"],
                pt["L_ray"], pt["r_diag"], pt["out_of_scope"],
                pt["N_pool"],
                pt["median_T"], mci[0], mci[1],
                pt["sigma1_std"], sci[0], sci[1],
                pt["sigma1_IQR_proxy"],
                pt["JS_vs_ref"], pt["N_per_snap_mean"],
            ])

    # 7. Write master summary JSON
    out = {
        "method": ("ED-SC 3.4-σ₁ calibration inside r_diag=1 window "
                   "(ξ ∈ [1.60, 1.95]) on fixed seed 77 with 40-snapshot "
                   "pooling of Hessian-trace T_motif = λ_neg + λ_pos"),
        "simulator_of_record":
            "r2_grf_falsifier_tests.py + ED_Update_Rule.ed_step_mobility",
        "xi_canonical_lattice_units": XI_CANONICAL,
        "dimensionless_hinge": DIMLESS_HINGE,
        "alpha_filt": ALPHA_FILT,
        "N_req": N_REQ,
        "fixed_seed": FIXED_SEED,
        "snapshot_schedule": {
            "burn_in": XI_BURN_IN, "snap_every": XI_SNAP_EVERY,
            "snapshots_per_xi": 40,
        },
        "canonical_params": {
            "alpha": fr.ALPHA0, "gamma": fr.GAMMA,
            "noise_sigma": fr.NOISE0,
            "mobility_exp": fr.MOBILITY_EXP,
            "steps": fr.STEPS, "size": fr.SIZE, "dt": fr.DT,
        },
        "xi_targets": XI_TARGETS,
        "ref_xi_index": REF_INDEX,
        "resonance_windows_excluded": {
            "A": list(WINDOW_A), "B": list(WINDOW_B)},
        "calibration_prepass": calibration,
        "scan_points": scan_points,
        "r_diag_excursions": r_diag_excursions,
        "derived_summary": {
            "sigma1_vs_xi_fit": sigma1_fit,
            "sigma1_IQR_vs_xi_fit": sigma1_IQR_fit,
            "flat_check": flat_check,
            "trend_direction": trend_direction,
            "rigid_zero_check": rigid_zero_check,
            "gaussianity_check": gaussianity_check,
            "n_in_scope_points": len(in_scope),
            "n_out_of_scope_points": len(r_diag_excursions),
        },
        "wall_seconds_total": time.time() - t_master,
    }

    summary_path = os.path.join(OUT_DIR, "sigma1_calibration_summary.json")
    with open(summary_path, "w") as f:
        json.dump(out, f, indent=2)

    print(f"\nWrote table → {csv_path}", file=sys.stderr)
    print(f"Wrote master summary → {summary_path}", file=sys.stderr)
    print(json.dumps({
        "n_points": len(scan_points),
        "n_in_scope": len(in_scope),
        "n_out_of_scope": len(r_diag_excursions),
        "sigma1_vs_xi_slope": sigma1_fit["slope"] if sigma1_fit else None,
        "sigma1_vs_xi_R2": sigma1_fit["R_squared"] if sigma1_fit else None,
        "trend_direction": trend_direction,
        "flat_check_near_flat_020": (flat_check["near_flat_prior_020"]
                                      if flat_check else None),
        "rigid_zero_all_pass": rigid_zero_check["pass"],
        "gaussianity_all_pass": gaussianity_check["pass"],
        "wall_seconds_total": out["wall_seconds_total"],
    }, indent=2))


if __name__ == "__main__":
    main()
