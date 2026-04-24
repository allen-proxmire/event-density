"""ED-SC 3.4-σ₁ Filtered-vs-Unfiltered T Diagnostic (F1 follow-up).

Pre-registered in theory/GR_SC_1_3_RayleighClass_Scoping.md §7 F1.

Discriminates the three T-bias readings (a/b/c) for the rigid-zero
failure observed in ED-SC 3.4-σ₁:
  (a) tenth-pass derivation incomplete; motif-filter-level correction
  (b) motif filter selects a biased sub-ensemble; bulk GRF still obeys
      rigid-zero; tenth-pass taxonomy stands with footnote
  (c) tenth-pass derivation contains an error; bulk GRF also biased

Method: re-run the ED-SC 3.4-σ₁ evolution pipeline and, at every
admitted Morse saddle per snapshot, record two statistics:
  - T_motif_filt : T = λ_neg + λ_pos ONLY for saddles passing the
                    canonical motif filter (same as ED-SC 3.4-σ₁).
  - T_bulk       : T = λ_neg + λ_pos for ALL Morse saddles found
                    by fr.find_morse_saddles() regardless of filter.

Bulk is therefore a superset of filtered (every filtered motif is
first a Morse saddle). Comparing median and std between the two at
each ξ reveals whether the filter introduces the observed rigid-zero
bias.

Verdict logic:
  - count_bulk_bias = ξ points where bulk median CI does NOT contain 0
  - count_filt_bias = ξ points where filtered median CI does NOT contain 0
  - Reading (b) supported iff   count_bulk_bias ≤ 2   AND   count_filt_bias ≥ 6
  - Reading (c) supported iff   count_bulk_bias ≥ 6   AND   count_filt_bias ≥ 6
  - Reading (a) supported iff   count_bulk_bias ≥ 6   AND   count_filt_bias ≥ 6
                                AND   filt_bias ≫ bulk_bias in magnitude
    (i.e. both biased, but filter amplifies — tenth-pass incomplete)
  - Otherwise: Inconclusive

Simulator of record:
  r2_grf_falsifier_tests.py  +  ED_Update_Rule.ed_step_mobility

Fixed seed: 77. Canonical filter for filtered population:
α_filt = 0.25, N_req = 4. Canonical hinge: L_ray = 1.08·ξ_measured.

Writes:
  outputs/ed_sc_3_4_sigma1/sigma1_filtered_vs_unfiltered_T_table.csv
  outputs/ed_sc_3_4_sigma1/sigma1_filtered_vs_unfiltered_T_summary.json

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
CALIBRATION_W_GRID = [0.05, 0.08, 0.10, 0.13, 0.16, 0.20, 0.25, 0.30, 0.35]
CALIBRATION_TOL = 0.01

# Verdict thresholds (per memo §7 F1)
VERDICT_BIAS_COUNT_HIGH = 6     # "≥ 6 of 9 points biased" threshold
VERDICT_BIAS_COUNT_LOW = 2      # "≤ 2 of 9 points biased" threshold
VERDICT_AMPLIFICATION_FACTOR = 2.0  # for reading (a) filt ≫ bulk

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
# Bulk-vs-filtered saddle extraction per snapshot
# ---------------------------------------------------------------------------
def collect_bulk_and_filtered_T(snapshot, L_ray):
    """For one snapshot, return (T_bulk_list, T_filt_list).

    T_bulk_list = all Morse saddles from fr.find_morse_saddles (no filter)
    T_filt_list = subset passing fr.motif_pass at canonical filter geometry
    Both lists record T = λ_neg + λ_pos per saddle.
    """
    E = fr.smooth_field(snapshot)
    p_hat = float(snapshot.mean())
    p_std = float(snapshot.std())
    sads = fr.find_morse_saddles(E)
    T_bulk = []
    T_filt = []
    for s in sads:
        T = float(s["lam_neg"]) + float(s["lam_pos"])
        T_bulk.append(T)
        if fr.motif_pass(s, E, p_hat, p_std, ALPHA_FILT, L_ray, N_REQ):
            T_filt.append(T)
    return T_bulk, T_filt


def collect_40snap(snapshots, L_ray):
    all_T_bulk = []
    all_T_filt = []
    per_snap = []
    for snap_idx, p in enumerate(snapshots):
        T_b, T_f = collect_bulk_and_filtered_T(p, L_ray)
        all_T_bulk.extend(T_b)
        all_T_filt.extend(T_f)
        per_snap.append({"snap": snap_idx,
                         "N_bulk": len(T_b),
                         "N_filt": len(T_f)})
    return all_T_bulk, all_T_filt, per_snap


# ---------------------------------------------------------------------------
# Bootstrap statistics
# ---------------------------------------------------------------------------
def bootstrap_median_std(values, B=4000, rng_seed=99):
    v = np.asarray([x for x in values if np.isfinite(x)])
    if len(v) < 3:
        return dict(n=int(len(v)),
                    median=None, median_ci=[None, None],
                    std=None, std_ci=[None, None])
    rng = np.random.default_rng(rng_seed)
    meds, stds = [], []
    for _ in range(B):
        smp = rng.choice(v, size=len(v), replace=True)
        meds.append(np.median(smp))
        stds.append(np.std(smp, ddof=1))
    return dict(
        n=int(len(v)),
        median=float(np.median(v)),
        median_ci=[float(np.quantile(meds, 0.16)),
                   float(np.quantile(meds, 0.84))],
        std=float(np.std(v, ddof=1)),
        std_ci=[float(np.quantile(stds, 0.16)),
                float(np.quantile(stds, 0.84))],
    )


def ci_contains_zero(ci):
    if ci is None or ci[0] is None or ci[1] is None:
        return None
    return ci[0] <= 0 <= ci[1]


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

    T_bulk, T_filt, per_snap = collect_40snap(snapshots, L_ray)
    bs_bulk = bootstrap_median_std(T_bulk)
    bs_filt = bootstrap_median_std(T_filt)

    # Differences
    med_diff = (bs_filt["median"] - bs_bulk["median"]
                if (bs_filt["median"] is not None
                    and bs_bulk["median"] is not None) else None)
    std_ratio = (bs_filt["std"] / bs_bulk["std"]
                 if (bs_filt["std"] is not None
                     and bs_bulk["std"] is not None and bs_bulk["std"] > 0)
                 else None)

    return {
        "xi_target": xi_target,
        "xi_measured": xi_measured,
        "xi_miss_fraction": miss,
        "w_used": w,
        "refinement_used": refinement_used,
        "L_ray": L_ray,
        "r_diag": r_diag,
        "out_of_scope": out_of_scope,
        "N_bulk": bs_bulk["n"],
        "median_T_bulk": bs_bulk["median"],
        "median_T_bulk_CI": bs_bulk["median_ci"],
        "sigma1_std_bulk": bs_bulk["std"],
        "sigma1_std_bulk_CI": bs_bulk["std_ci"],
        "bulk_CI_contains_zero": ci_contains_zero(bs_bulk["median_ci"]),
        "N_filt": bs_filt["n"],
        "median_T_filt": bs_filt["median"],
        "median_T_filt_CI": bs_filt["median_ci"],
        "sigma1_std_filt": bs_filt["std"],
        "sigma1_std_filt_CI": bs_filt["std_ci"],
        "filt_CI_contains_zero": ci_contains_zero(bs_filt["median_ci"]),
        "median_diff": med_diff,
        "sigma1_std_ratio_filt_over_bulk": std_ratio,
        "per_snapshot_N": per_snap,
        "wall_seconds": time.time() - t0,
    }


# ---------------------------------------------------------------------------
# Verdict logic
# ---------------------------------------------------------------------------
def render_verdict(scan_points):
    n_bulk_bias = sum(1 for pt in scan_points
                      if pt["bulk_CI_contains_zero"] is False)
    n_filt_bias = sum(1 for pt in scan_points
                      if pt["filt_CI_contains_zero"] is False)

    # Amplification factor: compare median magnitudes where both defined
    amp_ratios = []
    for pt in scan_points:
        mf = pt["median_T_filt"]
        mb = pt["median_T_bulk"]
        if mf is None or mb is None or abs(mb) < 1e-10:
            continue
        amp_ratios.append(abs(mf) / max(abs(mb), 1e-10))
    amp_median = float(np.median(amp_ratios)) if amp_ratios else None

    # Decision
    if n_bulk_bias <= VERDICT_BIAS_COUNT_LOW \
            and n_filt_bias >= VERDICT_BIAS_COUNT_HIGH:
        verdict = "reading_b_filter_introduces_bias"
        reason = (f"n_bulk_bias={n_bulk_bias} ≤ {VERDICT_BIAS_COUNT_LOW} "
                  f"(bulk is consistent with rigid-zero) AND "
                  f"n_filt_bias={n_filt_bias} ≥ {VERDICT_BIAS_COUNT_HIGH} "
                  f"(filter shows bias); tenth-pass Trace-Gaussian "
                  f"taxonomy stands with motif-filter-population "
                  f"footnote.")
    elif n_bulk_bias >= VERDICT_BIAS_COUNT_HIGH \
            and n_filt_bias >= VERDICT_BIAS_COUNT_HIGH:
        # Both biased - distinguish (a) from (c) by amplification
        if amp_median is not None \
                and amp_median >= VERDICT_AMPLIFICATION_FACTOR:
            verdict = "reading_a_tenth_pass_incomplete_filter_amplifies"
            reason = (f"Both populations biased "
                      f"(n_bulk={n_bulk_bias}, n_filt={n_filt_bias}) "
                      f"AND filter median is {amp_median:.2f}× bulk "
                      f"median (≥ {VERDICT_AMPLIFICATION_FACTOR} "
                      f"amplification threshold); tenth-pass derivation "
                      f"is incomplete and filter adds correction.")
        else:
            verdict = "reading_c_tenth_pass_wrong"
            reason = (f"Both populations biased "
                      f"(n_bulk={n_bulk_bias}, n_filt={n_filt_bias}) "
                      f"with filt/bulk median ratio "
                      f"{amp_median:.2f}× (< {VERDICT_AMPLIFICATION_FACTOR} "
                      f"amplification threshold); bulk GRF itself has "
                      f"non-zero median; tenth-pass rigid-zero claim "
                      f"was never true.")
    else:
        verdict = "Inconclusive"
        reason = (f"Mixed pattern: n_bulk_bias={n_bulk_bias}, "
                  f"n_filt_bias={n_filt_bias}; neither reading cleanly "
                  f"supported. Additional statistics or method refinement "
                  f"required.")

    return {
        "verdict": verdict,
        "reason": reason,
        "n_bulk_bias": n_bulk_bias,
        "n_filt_bias": n_filt_bias,
        "amp_ratio_median": amp_median,
        "bias_count_thresholds": {
            "high": VERDICT_BIAS_COUNT_HIGH,
            "low": VERDICT_BIAS_COUNT_LOW,
        },
        "amplification_threshold": VERDICT_AMPLIFICATION_FACTOR,
    }


# ---------------------------------------------------------------------------
# Master driver
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    t_master = time.time()

    assert_no_resonance_plan(XI_TARGETS)

    print(f"Calibration pre-pass: sweeping IC half-width w on seed "
          f"{FIXED_SEED}...", file=sys.stderr)
    calibration = run_calibration(FIXED_SEED)

    print(f"\nFiltered-vs-unfiltered T scan: {len(XI_TARGETS)} points "
          f"at seed={FIXED_SEED}", file=sys.stderr)
    scan_points = []
    for xi_target in XI_TARGETS:
        print(f"  ξ_target={xi_target} ...", file=sys.stderr)
        pt = run_scan_point(xi_target, calibration)
        scan_points.append(pt)
        print(f"    ξ_meas={pt['xi_measured']:.4f}  "
              f"N_bulk={pt['N_bulk']}  N_filt={pt['N_filt']}  "
              f"med_T_bulk={pt['median_T_bulk']}  "
              f"med_T_filt={pt['median_T_filt']}  "
              f"bulk_CI_zero={pt['bulk_CI_contains_zero']}  "
              f"filt_CI_zero={pt['filt_CI_contains_zero']}",
              file=sys.stderr)

    verdict = render_verdict(scan_points)

    r_diag_excursions = [
        {"xi_target": pt["xi_target"], "xi_measured": pt["xi_measured"],
         "L_ray": pt["L_ray"], "r_diag": pt["r_diag"]}
        for pt in scan_points if pt["out_of_scope"]
    ]

    # Write CSV
    csv_path = os.path.join(
        OUT_DIR, "sigma1_filtered_vs_unfiltered_T_table.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "xi_target", "xi_measured", "miss_frac", "w_used", "refined",
            "L_ray", "r_diag", "out_of_scope",
            "N_bulk",
            "median_T_bulk", "median_T_bulk_lo", "median_T_bulk_hi",
            "sigma1_std_bulk", "sigma1_std_bulk_lo", "sigma1_std_bulk_hi",
            "bulk_CI_contains_zero",
            "N_filt",
            "median_T_filt", "median_T_filt_lo", "median_T_filt_hi",
            "sigma1_std_filt", "sigma1_std_filt_lo", "sigma1_std_filt_hi",
            "filt_CI_contains_zero",
            "median_diff", "sigma1_std_ratio_filt_over_bulk",
        ])
        for pt in scan_points:
            mb_ci = pt["median_T_bulk_CI"] or [None, None]
            sb_ci = pt["sigma1_std_bulk_CI"] or [None, None]
            mf_ci = pt["median_T_filt_CI"] or [None, None]
            sf_ci = pt["sigma1_std_filt_CI"] or [None, None]
            w.writerow([
                pt["xi_target"], pt["xi_measured"], pt["xi_miss_fraction"],
                pt["w_used"], pt["refinement_used"],
                pt["L_ray"], pt["r_diag"], pt["out_of_scope"],
                pt["N_bulk"],
                pt["median_T_bulk"], mb_ci[0], mb_ci[1],
                pt["sigma1_std_bulk"], sb_ci[0], sb_ci[1],
                pt["bulk_CI_contains_zero"],
                pt["N_filt"],
                pt["median_T_filt"], mf_ci[0], mf_ci[1],
                pt["sigma1_std_filt"], sf_ci[0], sf_ci[1],
                pt["filt_CI_contains_zero"],
                pt["median_diff"], pt["sigma1_std_ratio_filt_over_bulk"],
            ])

    # Write summary JSON
    out = {
        "method": ("ED-SC 3.4-σ₁ F1 follow-up: filtered-vs-unfiltered "
                   "T_motif = λ_neg + λ_pos comparison at 9-point ξ grid; "
                   "discriminates T-bias readings (a/b/c) for the "
                   "rigid-zero failure of ED-SC 3.4-σ₁"),
        "simulator_of_record":
            "r2_grf_falsifier_tests.py + ED_Update_Rule.ed_step_mobility",
        "xi_canonical_lattice_units": XI_CANONICAL,
        "dimensionless_hinge": DIMLESS_HINGE,
        "alpha_filt_for_filter": ALPHA_FILT,
        "N_req_for_filter": N_REQ,
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
        "resonance_windows_excluded": {
            "A": list(WINDOW_A), "B": list(WINDOW_B)},
        "calibration_prepass": calibration,
        "scan_points": scan_points,
        "r_diag_excursions": r_diag_excursions,
        "verdict": verdict,
        "wall_seconds_total": time.time() - t_master,
    }

    json_path = os.path.join(
        OUT_DIR, "sigma1_filtered_vs_unfiltered_T_summary.json")
    with open(json_path, "w") as f:
        json.dump(out, f, indent=2)

    print(f"\nWrote table → {csv_path}", file=sys.stderr)
    print(f"Wrote master summary → {json_path}", file=sys.stderr)
    print(json.dumps({
        "n_points": len(scan_points),
        "n_bulk_bias": verdict["n_bulk_bias"],
        "n_filt_bias": verdict["n_filt_bias"],
        "amp_ratio_median": verdict["amp_ratio_median"],
        "verdict": verdict["verdict"],
        "reason": verdict["reason"],
        "wall_seconds_total": out["wall_seconds_total"],
    }, indent=2))


if __name__ == "__main__":
    main()
