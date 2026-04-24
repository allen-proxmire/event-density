"""ED-SC 3.3.8a ξ-Crossing Selection Scan.

Pre-registered in theory/ED_SC_3_3_8a_XiCrossing_Scan.md.

Executes the 11-point ξ scan across ξ ∈ [1.85, 2.10] at Δξ = 0.025,
bracketing the predicted diagonal-ray shell-crossing
ξ_crossing ≈ 1.964 lu. For each ξ_target, an initial-condition
amplitude half-width w is chosen (from a calibration interpolant)
so that the measured 40-snapshot ξ matches the target within ±1%
(one bisection refinement permitted). At each scan point the driver
collects 40-snapshot-pooled motifs at L_ray = 1.08·ξ_measured and
records (N, S1, S2, S3), endpoint shell histogram, JS divergence
vs the ξ = 1.900 reference, and boolean √8 shell admission.

After the scan, the ED-SC 3.3.8a §5 pass/fail logic selects one of
remediations A, B, D, or Inconsistent.

Simulator of record:
  r2_grf_falsifier_tests.py  +  ED_Update_Rule.ed_step_mobility

Seed: 77 (fixed; ED-SC 3.3.8a §2 specifies single-seed reproducibility).

Writes:
  outputs/ed_sc_3_3_8a/xi_scan_summary.json
  outputs/ed_sc_3_3_8a/xi_scan_table.csv

No simulator constants are mutated. Deterministic given seed + w.
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
FIXED_SEED = 77

WINDOW_A = (2.50, 2.80)
WINDOW_B = (3.50, 3.90)

# Predicted crossing (from ED-SC 3.3.8 §3)
XI_CROSSING_PREDICTED = 1.964

# Scan grid
XI_TARGETS = [round(1.850 + 0.025 * k, 4) for k in range(11)]
# -> [1.850, 1.875, 1.900, 1.925, 1.950, 1.975, 2.000, 2.025, 2.050, 2.075, 2.100]
REF_INDEX = 2  # ξ = 1.900 is the reference histogram

# IC-amplitude calibration grid (w = half-width around 0.5)
CALIBRATION_W_GRID = [0.05, 0.08, 0.10, 0.13, 0.16, 0.20, 0.25, 0.30, 0.35]

# Verdict thresholds (per ED-SC 3.3.8a §5)
S1_FLAT_THRESH = 0.20
S2_JUMP_THRESH = 0.20            # of mean(S2)
CROSSING_PROXIMITY = 0.05         # of ξ_crossing for "at-crossing"
CALIBRATION_TOL = 0.01            # ±1% target matching

OUT_DIR = os.path.join(HERE, "..", "..", "outputs", "ed_sc_3_3_8a")


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
# Resonance-window guard
# ---------------------------------------------------------------------------
def in_window(L, win):
    return win[0] <= L <= win[1]


def assert_no_resonance_any(l_list):
    bad = [L for L in l_list
           if in_window(L, WINDOW_A) or in_window(L, WINDOW_B)]
    if bad:
        raise RuntimeError(
            f"Scan L_ray values intersect forbidden windows: {bad}")


# ---------------------------------------------------------------------------
# Evolution with controllable IC half-width; 40 snapshots
# ---------------------------------------------------------------------------
def evolve_40snap(seed, w):
    """Return (final_field, snapshots[], xi_snapshots[]) under fixed seed
    with IC = uniform(0.5 - w, 0.5 + w). 40 snapshots (burn-in 100, snap
    every 10)."""
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
    return p, snaps, xis


# ---------------------------------------------------------------------------
# Calibration pre-pass
# ---------------------------------------------------------------------------
def run_calibration(seed):
    """Sweep CALIBRATION_W_GRID, measure 40-snapshot ξ at each w. Return
    sorted list of (w, xi_mean) for monotone interpolation."""
    results = []
    for w in CALIBRATION_W_GRID:
        ts = time.time()
        _, _, xis = evolve_40snap(seed, w)
        xi_mean = float(np.mean([x for x in xis if np.isfinite(x)]))
        results.append({"w": w, "xi": xi_mean,
                        "wall_seconds": time.time() - ts})
        print(f"  cal w={w:.3f}  ξ={xi_mean:.4f}  "
              f"t={time.time()-ts:.1f}s", file=sys.stderr)
    # Sort by ξ (IC half-width and coherence length are typically
    # monotone but we don't assume direction — sort on ξ for interpolation)
    results.sort(key=lambda r: r["xi"])
    return results


def interpolate_w(calibration, xi_target):
    """Linear interpolation of w(ξ) using the (sorted by ξ) calibration
    table. Clamps at table extremes."""
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
# Motif extraction (canonical filter, per-scan L_ray)
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
    for snap_idx, p in enumerate(snapshots):
        for m in collect_motifs_snapshot(p, L_ray):
            m["snap_index"] = snap_idx
            motifs.append(m)
    return motifs


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
# Shell histogram + Jensen–Shannon divergence
# ---------------------------------------------------------------------------
def shell_histogram(motifs):
    h = {}
    for m in motifs:
        for r in m["r_k"]:
            key = f"{r:.4f}"
            h[key] = h.get(key, 0) + 1
    return h


def has_shell_root8(hist, tol=1e-3):
    for k in hist:
        if abs(float(k) - math.sqrt(8.0)) < tol:
            return True, hist[k]
    return False, 0


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
# Per-scan-point execution
# ---------------------------------------------------------------------------
def run_scan_point(xi_target, calibration):
    """Run one scan point. Returns a dict of measurements."""
    t0 = time.time()
    w = interpolate_w(calibration, xi_target)

    _, snapshots, xis = evolve_40snap(FIXED_SEED, w)
    xi_finite = [x for x in xis if np.isfinite(x)]
    xi_measured = float(np.mean(xi_finite)) if xi_finite else float('nan')

    miss = (abs(xi_measured - xi_target) / xi_target
            if xi_target != 0 else float('inf'))

    # One bisection refinement if miss > tolerance
    refinement_used = False
    if miss > CALIBRATION_TOL and xi_finite:
        # Adjust w to reduce error: assume monotone (smaller w → larger ξ)
        xs = [r["xi"] for r in calibration]
        ws = [r["w"] for r in calibration]
        # Find current position and nudge toward target
        if xi_measured < xi_target:
            # need smaller w → larger ξ
            w_new = max(min(ws), w * 0.85)
        else:
            # need larger w → smaller ξ
            w_new = min(max(ws), w * 1.15)
        _, snapshots, xis = evolve_40snap(FIXED_SEED, w_new)
        xi_finite = [x for x in xis if np.isfinite(x)]
        xi_new = float(np.mean(xi_finite)) if xi_finite else xi_measured
        miss_new = (abs(xi_new - xi_target) / xi_target
                    if xi_target != 0 else float('inf'))
        if miss_new < miss:
            w = w_new
            xi_measured = xi_new
            miss = miss_new
            refinement_used = True

    L_ray = DIMLESS_HINGE * xi_measured
    # Hard-fail if L_ray intersects a resonance window
    if in_window(L_ray, WINDOW_A) or in_window(L_ray, WINDOW_B):
        raise RuntimeError(
            f"ξ_target={xi_target}: L_ray={L_ray} intersects a "
            f"resonance window. Aborting scan.")

    motifs = collect_motifs_40snap(snapshots, L_ray)
    ratios = [m["ratio"] for m in motifs]
    bs = bootstrap_median_iqr(ratios)
    s3 = tail_log_slope(ratios)
    hist = shell_histogram(motifs)
    has_r8, r8_count = has_shell_root8(hist)
    total_endpoints = 4 * len(motifs)
    r8_fraction = (r8_count / total_endpoints
                   if total_endpoints > 0 else 0.0)

    return {
        "xi_target": xi_target,
        "xi_measured": xi_measured,
        "xi_miss_fraction": miss,
        "w_used": w,
        "refinement_used": refinement_used,
        "L_ray": L_ray,
        "N_motifs": int(bs["n"]),
        "N_endpoints": total_endpoints,
        "S1": bs["median"],
        "S1_CI": bs["median_ci"],
        "S2": bs["iqr"],
        "S2_CI": bs["iqr_ci"],
        "S3": s3,
        "shell_histogram": hist,
        "has_root8": has_r8,
        "root8_count": r8_count,
        "root8_fraction": r8_fraction,
        "wall_seconds": time.time() - t0,
    }


# ---------------------------------------------------------------------------
# Verdict logic (per ED-SC 3.3.8a §5)
# ---------------------------------------------------------------------------
def apply_verdict(scan_points):
    xis = [p["xi_target"] for p in scan_points]
    s1s = [p["S1"] for p in scan_points]
    s2s = [p["S2"] for p in scan_points]
    has_r8 = [p["has_root8"] for p in scan_points]

    # S1 stability (relative to S1_ref)
    s1_ref = s1s[REF_INDEX]
    s1_deviations = []
    for s1 in s1s:
        if s1 is None or s1_ref is None or s1_ref == 0:
            s1_deviations.append(None)
        else:
            s1_deviations.append(abs(s1 - s1_ref) / abs(s1_ref))
    s1_max_dev = max((d for d in s1_deviations if d is not None), default=None)
    s1_stable = (s1_max_dev is not None
                 and s1_max_dev < S1_FLAT_THRESH)

    # √8 shell monotonicity: does has_r8 transition from False → True
    # exactly once, monotonically?
    transitions = []
    for i in range(len(has_r8) - 1):
        if has_r8[i] != has_r8[i + 1]:
            transitions.append((i, has_r8[i], has_r8[i + 1]))
    # crossing_index: first i where has_r8 is True
    crossing_index = next(
        (i for i, v in enumerate(has_r8) if v), None)
    monotone_shell = (
        len(transitions) <= 1 and
        (crossing_index is None or
         all(not has_r8[i] for i in range(crossing_index))
         and all(has_r8[i] for i in range(crossing_index, len(has_r8))))
    )

    # S2 discontinuity
    s2_finite = [s for s in s2s if s is not None]
    s2_mean = float(np.mean(s2_finite)) if s2_finite else 0.0
    jump_thresh_abs = S2_JUMP_THRESH * s2_mean
    s2_jumps = []
    for i in range(len(s2s) - 1):
        if s2s[i] is None or s2s[i + 1] is None:
            s2_jumps.append(None)
            continue
        s2_jumps.append(abs(s2s[i + 1] - s2s[i]))
    s2_disc_idx = None
    s2_disc_amp = 0.0
    for i, j in enumerate(s2_jumps):
        if j is None:
            continue
        if j > s2_disc_amp:
            s2_disc_amp = j
            s2_disc_idx = i
    s2_has_jump = (s2_disc_amp > jump_thresh_abs)
    # is the jump at the crossing?
    jump_at_crossing = False
    if s2_disc_idx is not None:
        xi_at_jump = xis[s2_disc_idx]
        jump_at_crossing = (
            abs(xi_at_jump - XI_CROSSING_PREDICTED) <= CROSSING_PROXIMITY)

    # S2 range test
    s2_range_frac = ((max(s2_finite) - min(s2_finite)) / s2_mean
                     if s2_finite and s2_mean > 0 else 0.0)
    s2_range_exceeds = (s2_range_frac > S2_JUMP_THRESH)

    # Remediation selection
    if not s1_stable:
        verdict = "Inconsistent"
        reason = (f"S1 varies across scan: max_dev={s1_max_dev} "
                  f">= threshold {S1_FLAT_THRESH}; S1 invariance "
                  "from ED-SC 3.3.6 fails on this scan; diagnostic "
                  "memo required before remediation selection")
    elif monotone_shell and s2_has_jump and jump_at_crossing and s2_range_exceeds:
        verdict = "B"
        reason = (f"monotone √8 shell admission at crossing_index={crossing_index} "
                  f"(ξ={xis[crossing_index] if crossing_index is not None else None}); "
                  f"S1 stable (max_dev={s1_max_dev}); "
                  f"S2 range {s2_range_frac:.3f} > {S2_JUMP_THRESH} "
                  f"with discrete jump at ξ={xis[s2_disc_idx]} "
                  f"(amplitude {s2_disc_amp:.3f} > {jump_thresh_abs:.3f}, "
                  f"within ±{CROSSING_PROXIMITY} of predicted {XI_CROSSING_PREDICTED})")
    elif (not monotone_shell) or (s2_has_jump and not jump_at_crossing):
        verdict = "A"
        reason = (f"√8 shell admission non-monotone (transitions={transitions}), "
                  f"OR S2 jump at ξ={xis[s2_disc_idx] if s2_disc_idx is not None else None} "
                  f"not at predicted crossing; multiple shell-index classes present; "
                  f"shell-binned coordinate required")
    elif monotone_shell and not s2_has_jump:
        verdict = "D"
        reason = (f"monotone √8 shell admission at ξ={xis[crossing_index] if crossing_index is not None else None} "
                  f"but S2 varies smoothly (max ΔS2={s2_disc_amp:.3f} <= {jump_thresh_abs:.3f}); "
                  "shell-aware effective coordinate selected")
    else:
        verdict = "Inconsistent"
        reason = ("verdict logic did not match any remediation "
                  "pattern; inspect scan data manually")

    return {
        "s1_deviations": s1_deviations,
        "s1_max_dev": s1_max_dev,
        "s1_stable": s1_stable,
        "has_root8": has_r8,
        "shell_transitions": transitions,
        "monotone_shell": monotone_shell,
        "crossing_index": crossing_index,
        "crossing_xi": (xis[crossing_index]
                        if crossing_index is not None else None),
        "s2_mean": s2_mean,
        "s2_jumps": s2_jumps,
        "s2_discontinuity_index": s2_disc_idx,
        "s2_discontinuity_amplitude": s2_disc_amp,
        "s2_range_frac": s2_range_frac,
        "s2_has_discrete_jump": s2_has_jump,
        "jump_at_crossing": jump_at_crossing,
        "remediation_verdict": verdict,
        "reason": reason,
    }


# ---------------------------------------------------------------------------
# Master driver
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    t_master = time.time()

    # Defensive: none of the scanned L_ray values can fall in Windows A/B
    predicted_L = [DIMLESS_HINGE * xi for xi in XI_TARGETS]
    assert_no_resonance_any(predicted_L)

    # 1. Calibration pre-pass
    print("Calibration pre-pass: sweeping IC half-width w...",
          file=sys.stderr)
    calibration = run_calibration(FIXED_SEED)

    # 2. Scan
    print(f"\nξ-crossing scan: {len(XI_TARGETS)} points at seed={FIXED_SEED}",
          file=sys.stderr)
    scan_points = []
    for xi_target in XI_TARGETS:
        print(f"  ξ_target={xi_target} ...", file=sys.stderr)
        pt = run_scan_point(xi_target, calibration)
        scan_points.append(pt)
        dom_shells = sorted(pt["shell_histogram"].items(),
                            key=lambda kv: -kv[1])[:3]
        print(f"    ξ_measured={pt['xi_measured']:.4f} "
              f"(miss {pt['xi_miss_fraction']*100:.2f}%, "
              f"ref={pt['refinement_used']})  "
              f"L={pt['L_ray']:.4f}  N={pt['N_motifs']}  "
              f"S1={pt['S1']}  S2={pt['S2']}  "
              f"√8={pt['has_root8']}({pt['root8_count']})  "
              f"top_shells={dom_shells}",
              file=sys.stderr)

    # 3. JS divergences vs ref (ξ = 1.900, index 2)
    ref_hist = scan_points[REF_INDEX]["shell_histogram"]
    for pt in scan_points:
        pt["JS_vs_ref"] = jensen_shannon(pt["shell_histogram"], ref_hist)

    # 4. Verdict
    diagnostics = apply_verdict(scan_points)

    # 5. Write outputs
    out = {
        "method": ("ED-SC 3.3.8a ξ-crossing selection scan: "
                   "11-point Δξ=0.025 scan across ξ ∈ [1.85, 2.10] "
                   "bracketing predicted ξ_crossing ≈ 1.964, with "
                   "IC-amplitude ξ-control on fixed seed 77"),
        "simulator_of_record":
            "r2_grf_falsifier_tests.py + ED_Update_Rule.ed_step_mobility",
        "xi_canonical_lattice_units": XI_CANONICAL,
        "xi_crossing_predicted": XI_CROSSING_PREDICTED,
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
        "calibration": calibration,
        "scan_points": scan_points,
        "diagnostics": diagnostics,
        "remediation_verdict": diagnostics["remediation_verdict"],
        "wall_seconds_total": time.time() - t_master,
    }

    summary_path = os.path.join(OUT_DIR, "xi_scan_summary.json")
    with open(summary_path, "w") as f:
        json.dump(out, f, indent=2)

    csv_path = os.path.join(OUT_DIR, "xi_scan_table.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["xi_target", "xi_measured", "miss_frac", "w_used",
                    "L_ray", "N_motifs", "N_endpoints",
                    "S1", "S2", "S3",
                    "has_root8", "root8_count", "root8_fraction",
                    "JS_vs_ref"])
        for pt in scan_points:
            w.writerow([
                pt["xi_target"], pt["xi_measured"], pt["xi_miss_fraction"],
                pt["w_used"], pt["L_ray"], pt["N_motifs"],
                pt["N_endpoints"], pt["S1"], pt["S2"], pt["S3"],
                pt["has_root8"], pt["root8_count"], pt["root8_fraction"],
                pt["JS_vs_ref"],
            ])

    print(f"\nWrote master summary → {summary_path}", file=sys.stderr)
    print(f"Wrote table → {csv_path}", file=sys.stderr)
    print(json.dumps({
        "remediation_verdict": diagnostics["remediation_verdict"],
        "reason": diagnostics["reason"],
        "s1_stable": diagnostics["s1_stable"],
        "s1_max_dev": diagnostics["s1_max_dev"],
        "monotone_shell": diagnostics["monotone_shell"],
        "crossing_index": diagnostics["crossing_index"],
        "crossing_xi": diagnostics["crossing_xi"],
        "s2_has_discrete_jump": diagnostics["s2_has_discrete_jump"],
        "jump_at_crossing": diagnostics["jump_at_crossing"],
        "wall_seconds_total": out["wall_seconds_total"],
    }, indent=2))


if __name__ == "__main__":
    main()
