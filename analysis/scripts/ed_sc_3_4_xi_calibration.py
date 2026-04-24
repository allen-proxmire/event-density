"""ED-SC 3.4 ξ Calibration driver.

Pre-registered in theory/ED_SC_3_4_XiCalibration.md.

9-point ξ calibration inside the canonical invariance domain
(r_diag = 1, ξ ∈ [1.60, 1.95] lu) on fixed seed 77 with IC-amplitude
ξ-control (inherited from ED-SC 3.3.8a). At each ξ point the driver
pools motifs across 40 snapshots, computes bootstrap S1/S2/S3,
endpoint shell histogram, JS divergence vs the ξ = 1.80 reference,
and per-snapshot stationarity diagnostic. After the scan, OLS slopes
and residuals are fit to S1(ξ) and S2(ξ) as the primary calibration-
curve output.

Simulator of record:
  r2_grf_falsifier_tests.py  +  ED_Update_Rule.ed_step_mobility

Fixed seed: 77. Canonical filter (α_filt = 0.25, N_req = 4).
Canonical hinge: L_ray = 1.08 · ξ_measured.

Guards (hard-fail):
  - Resonance windows A [2.50, 2.80] and B [3.50, 3.90] on L_ray.
  - r_diag window: any ξ point whose r_diag_measured != 1 is flagged
    out-of-scope and excluded from the fit (per ED-SC 3.4 §3).

Writes:
  outputs/ed_sc_3_4/xi_calibration_table.csv
  outputs/ed_sc_3_4/xi_calibration_summary.json

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
DIAG_COS = 0.707  # 1/√2 for r_diag computation
FIXED_SEED = 77

WINDOW_A = (2.50, 2.80)
WINDOW_B = (3.50, 3.90)

# Scan grid (ED-SC 3.4 §3)
XI_TARGETS = [1.60, 1.65, 1.70, 1.75, 1.80, 1.85, 1.90, 1.93, 1.95]
REF_INDEX = 4  # ξ = 1.80 is the reference histogram

# IC-amplitude calibration grid (inherited from ED-SC 3.3.8a)
CALIBRATION_W_GRID = [0.05, 0.08, 0.10, 0.13, 0.16, 0.20, 0.25, 0.30, 0.35]

CALIBRATION_TOL = 0.01  # ±1% ξ target tolerance

OUT_DIR = os.path.join(HERE, "..", "..", "outputs", "ed_sc_3_4")


# ---------------------------------------------------------------------------
# ξ measurement (verbatim from canonical method)
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
# Calibration pre-pass
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
    """Pre-flight: verify no nominal L_ray intersects resonance windows."""
    for xi in xi_targets:
        L = DIMLESS_HINGE * xi
        if in_window(L, WINDOW_A) or in_window(L, WINDOW_B):
            raise RuntimeError(
                f"Planned ξ_target={xi} yields L_ray={L:.4f} in a "
                f"resonance window. Refusing to launch.")


def r_diag_of(L):
    return int(round(DIAG_COS * L))


# ---------------------------------------------------------------------------
# Motif extraction (canonical filter, per-point L_ray)
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
    motifs = []
    for s in sads:
        if not fr.motif_pass(s, E, p_hat, p_std,
                             ALPHA_FILT, L_ray, N_REQ):
            continue
        eps = endpoints_of(s, L_ray)
        motifs.append({
            "ratio": float(s["ratio"]),
            "r_k": [float(e[2]) for e in eps],
        })
    return motifs


def collect_motifs_40snap(snapshots, L_ray):
    motifs = []
    per_snap_stats = []
    for snap_idx, p in enumerate(snapshots):
        ms = collect_motifs_snapshot(p, L_ray)
        for m in ms:
            m["snap_index"] = snap_idx
            motifs.append(m)
        rs = [m["ratio"] for m in ms]
        per_snap_stats.append({
            "snap": snap_idx, "N": len(rs),
            "median": float(np.median(rs)) if len(rs) >= 1 else None,
            "iqr": (float(np.quantile(rs, 0.75) - np.quantile(rs, 0.25))
                    if len(rs) >= 2 else None),
        })
    return motifs, per_snap_stats


# ---------------------------------------------------------------------------
# Bootstrap + tail slope + shell histogram + JS
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


def shell_histogram(motifs):
    h = {}
    for m in motifs:
        for r in m["r_k"]:
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


# ---------------------------------------------------------------------------
# OLS fit for calibration curve summaries
# ---------------------------------------------------------------------------
def ols_slope_residuals(xs, ys):
    """Ordinary-least-squares fit y = a + b·x. Returns dict with slope b,
    intercept a, residuals list, RMS residual, R²."""
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

    # Guards
    if in_window(L_ray, WINDOW_A) or in_window(L_ray, WINDOW_B):
        raise RuntimeError(
            f"ξ_target={xi_target}: L_ray={L_ray:.4f} intersects a "
            f"resonance window. Aborting scan.")
    r_diag = r_diag_of(L_ray)
    out_of_scope = (r_diag != 1)

    motifs, per_snap = collect_motifs_40snap(snapshots, L_ray)
    ratios = [m["ratio"] for m in motifs]
    bs = bootstrap_median_iqr(ratios)
    s3 = tail_log_slope(ratios)
    hist = shell_histogram(motifs)

    # Per-snapshot N and median arrays
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
        "N_motifs": int(bs["n"]),
        "N_endpoints": 4 * int(bs["n"]),
        "S1": bs["median"],
        "S1_CI": bs["median_ci"],
        "S2": bs["iqr"],
        "S2_CI": bs["iqr_ci"],
        "S3": s3,
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

    # Pre-flight: check nominal L_ray values for resonance windows
    assert_no_resonance_plan(XI_TARGETS)

    # 1. Calibration pre-pass on fixed seed
    print(f"Calibration pre-pass: sweeping IC half-width w on seed "
          f"{FIXED_SEED}...", file=sys.stderr)
    calibration = run_calibration(FIXED_SEED)

    # 2. Scan
    print(f"\nξ-calibration scan: {len(XI_TARGETS)} points "
          f"at seed={FIXED_SEED}", file=sys.stderr)
    scan_points = []
    for xi_target in XI_TARGETS:
        print(f"  ξ_target={xi_target} ...", file=sys.stderr)
        pt = run_scan_point(xi_target, calibration)
        scan_points.append(pt)
        print(f"    ξ_measured={pt['xi_measured']:.4f} "
              f"(miss {pt['xi_miss_fraction']*100:.2f}%, "
              f"refined={pt['refinement_used']})  "
              f"L={pt['L_ray']:.4f}  r_diag={pt['r_diag']}  "
              f"N={pt['N_motifs']}  "
              f"S1={pt['S1']}  S2={pt['S2']}  S3={pt['S3']}  "
              f"OOS={pt['out_of_scope']}",
              file=sys.stderr)

    # 3. JS divergences vs reference (ξ = 1.80, index 4)
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

    # 5. OLS fits for S1(ξ) and S2(ξ), restricted to in-scope points
    in_scope = [pt for pt in scan_points if not pt["out_of_scope"]]
    xi_vals = [pt["xi_measured"] for pt in in_scope]
    s1_vals = [pt["S1"] for pt in in_scope]
    s2_vals = [pt["S2"] for pt in in_scope]
    s3_vals = [pt["S3"] for pt in in_scope]

    s1_fit = ols_slope_residuals(xi_vals, s1_vals)
    s2_fit = ols_slope_residuals(xi_vals, s2_vals)
    s3_fit = ols_slope_residuals(xi_vals, s3_vals)

    # Derived interpretations
    if s1_fit is not None:
        dxi = max(xi_vals) - min(xi_vals)
        s1_total_variation = abs(s1_fit["slope"]) * dxi
        s1_ref = abs(np.mean(s1_vals))
        s1_flat_check = {
            "total_variation": float(s1_total_variation),
            "fraction_of_ref": float(s1_total_variation / s1_ref
                                     if s1_ref > 0 else 0.0),
            "near_flat_prior_020": bool(
                s1_total_variation / s1_ref < 0.20 if s1_ref > 0 else False),
        }
    else:
        s1_flat_check = None

    if s2_fit is not None:
        s2_trend_direction = (
            "positive" if s2_fit["slope"] > 0
            else "negative" if s2_fit["slope"] < 0 else "zero")
    else:
        s2_trend_direction = None

    # 6. Write CSV
    csv_path = os.path.join(OUT_DIR, "xi_calibration_table.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["xi_target", "xi_measured", "miss_frac", "w_used",
                    "refined", "L_ray", "r_diag", "out_of_scope",
                    "N", "S1", "S1_lo", "S1_hi", "S2", "S2_lo", "S2_hi",
                    "S3", "JS_vs_ref", "N_per_snap_mean"])
        for pt in scan_points:
            s1ci = pt["S1_CI"] or [None, None]
            s2ci = pt["S2_CI"] or [None, None]
            w.writerow([
                pt["xi_target"], pt["xi_measured"], pt["xi_miss_fraction"],
                pt["w_used"], pt["refinement_used"], pt["L_ray"],
                pt["r_diag"], pt["out_of_scope"], pt["N_motifs"],
                pt["S1"], s1ci[0], s1ci[1],
                pt["S2"], s2ci[0], s2ci[1],
                pt["S3"], pt["JS_vs_ref"], pt["N_per_snap_mean"],
            ])

    # 7. Write master summary JSON
    out = {
        "method": ("ED-SC 3.4 ξ calibration inside r_diag=1 window "
                   "(ξ ∈ [1.60, 1.95]) on fixed seed 77 with 40-snapshot "
                   "pooling and IC-amplitude ξ-control"),
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
            "S1_vs_xi_fit": s1_fit,
            "S1_flat_check": s1_flat_check,
            "S2_vs_xi_fit": s2_fit,
            "S2_trend_direction": s2_trend_direction,
            "S3_vs_xi_fit": s3_fit,
            "n_in_scope_points": len(in_scope),
            "n_out_of_scope_points": len(r_diag_excursions),
        },
        "wall_seconds_total": time.time() - t_master,
    }

    summary_path = os.path.join(OUT_DIR, "xi_calibration_summary.json")
    with open(summary_path, "w") as f:
        json.dump(out, f, indent=2)

    print(f"\nWrote table → {csv_path}", file=sys.stderr)
    print(f"Wrote master summary → {summary_path}", file=sys.stderr)
    print(json.dumps({
        "n_points": len(scan_points),
        "n_in_scope": len(in_scope),
        "n_out_of_scope": len(r_diag_excursions),
        "S1_vs_xi_slope": s1_fit["slope"] if s1_fit else None,
        "S1_total_variation_frac": (s1_flat_check["fraction_of_ref"]
                                    if s1_flat_check else None),
        "S1_near_flat_prior_020": (s1_flat_check["near_flat_prior_020"]
                                   if s1_flat_check else None),
        "S2_vs_xi_slope": s2_fit["slope"] if s2_fit else None,
        "S2_trend_direction": s2_trend_direction,
        "wall_seconds_total": out["wall_seconds_total"],
    }, indent=2))


if __name__ == "__main__":
    main()
