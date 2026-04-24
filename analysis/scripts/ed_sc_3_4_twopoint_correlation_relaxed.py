"""ED-SC 3.4 F4-alt Two-Point Correlation driver (relaxed filter).

Pre-registered in theory/ED_SC_3_4_twopoint_FilterRelaxation.md +
theory/ED_SC_3_4_twopoint_FilterRelaxation_Driver.md.

Identical to analysis/scripts/ed_sc_3_4_twopoint_correlation.py
(the F4 canonical driver) except:

  1. N_REQ = 2 (instead of 4) — filter relaxation per F4-alt
     amendment §2.
  2. OUT_DIR = outputs/ed_sc_3_4_twopoint_relaxed/ (instead of
     outputs/ed_sc_3_4_twopoint/) — separate artefacts to avoid
     collision with canonical-filter F4 outputs.
  3. Summary JSON adds top-level `filter_relaxation_amendment`
     key documenting the scope restriction to C_redshift(r)
     measurement only.

The canonical operating point (N_req = 4) remains authoritative
for every other ED-SC / GR-SC claim. F4-alt is scope-restricted
to the Correlation-class measurement channel.

Measures the two-point motif-ratio correlation function
`C_redshift(r) = 2[1 − ξ_φ(r)/σ_0²]` at canonical ξ = 1.7575
across the pre-registered 10-point r-grid {0.5, 1.0, ..., 5.0}
lu with Δr = 0.5. Expected ~24× motif-density increase per
hinge point vs canonical F4 (per ED-SC 3.3 rev. 2 data at
α_filt=0.25: N_pool=3985 at N_req=2 vs 164 at N_req=4).

Simulator of record:
  r2_grf_falsifier_tests.py  +  ED_Update_Rule.ed_step_mobility

Seeds: {11, 22, 33, 44, 55, 66, 77, 88, 99, 111} (matches F2
and canonical F4). Filter: α_filt = 0.25, **N_req = 2**.
Canonical hinge: L_ray = 1.08·ξ_measured. 40-snapshot per seed,
burn-in 100, snap every 10.

Writes:
  outputs/ed_sc_3_4_twopoint_relaxed/correlation_twopoint_table.csv
  outputs/ed_sc_3_4_twopoint_relaxed/correlation_twopoint_per_seed.csv
  outputs/ed_sc_3_4_twopoint_relaxed/correlation_twopoint_summary.json

No simulator constants are mutated. Deterministic given seeds.
"""
import csv
import json
import math
import os
import sys
import time
import numpy as np
from numpy.fft import fft2, ifft2, fftshift
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "ed_arch_r2"))
import r2_grf_falsifier_tests as fr  # noqa: E402

from ED_Update_Rule import ed_step_mobility  # noqa: E402

# ---------------------------------------------------------------------------
# Canonical constants (inherited verbatim)
# ---------------------------------------------------------------------------
XI_CANONICAL = 1.7575325729470939
XI_BURN_IN = 100
XI_SNAP_EVERY = 10

ALPHA_FILT = 0.25
N_REQ = 2  # F4-alt filter relaxation (canonical F4 uses 4)
DIMLESS_HINGE = 1.08
DIAG_COS = 0.707

WINDOW_A = (2.50, 2.80)
WINDOW_B = (3.50, 3.90)

XI_TARGET = 1.7575
SEEDS = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]

CALIBRATION_W_GRID = [0.05, 0.08, 0.10, 0.13, 0.16, 0.20, 0.25, 0.30, 0.35]
CALIBRATION_TOL = 0.01

# r-grid for two-point correlation
R_GRID = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
DR_BIN = 0.5
R_GRID_MIN_EDGE = R_GRID[0] - DR_BIN / 2   # 0.25
R_GRID_MAX_EDGE = R_GRID[-1] + DR_BIN / 2  # 5.25

# Pair-count admissibility thresholds
MIN_PAIRS_ENSEMBLE = 20
MIN_PAIRS_PER_SEED = 10

# Bootstrap config
BOOTSTRAP_B = 4000
BOOTSTRAP_RNG_SEED = 99

# Verdict thresholds (tenth-pass GR-SC 1.7 prediction: 0.80 ± 0.05)
VERDICT_CONFIRMED_LO = 0.75
VERDICT_CONFIRMED_HI = 0.85
VERDICT_REFUTED_LO = 0.70
VERDICT_REFUTED_HI = 0.90

OUT_DIR = os.path.join(HERE, "..", "..", "outputs",
                       "ed_sc_3_4_twopoint_relaxed")


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
        _, xis = evolve_40snap(seed, w)
        xi_mean = float(np.mean([x for x in xis if np.isfinite(x)]))
        results.append({"w": w, "xi": xi_mean})
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
            f"Planned ξ_target={XI_TARGET} yields L_ray={L} in a "
            f"resonance window.")


# ---------------------------------------------------------------------------
# Motif extraction with positions
# ---------------------------------------------------------------------------
def extract_motifs_with_positions(snapshot, L_ray):
    E = fr.smooth_field(snapshot)
    p_hat = float(snapshot.mean())
    p_std = float(snapshot.std())
    sads = fr.find_morse_saddles(E)
    out = []
    for s in sads:
        if not fr.motif_pass(s, E, p_hat, p_std,
                             ALPHA_FILT, L_ray, N_REQ):
            continue
        out.append({
            "i": int(s["i"]),
            "j": int(s["j"]),
            "rho": float(s["ratio"]),
        })
    return out


# ---------------------------------------------------------------------------
# Periodic-boundary minimum-image distance
# ---------------------------------------------------------------------------
def min_image_distance(p1, p2, L=None):
    if L is None:
        L = fr.SIZE
    di = abs(p1[0] - p2[0])
    dj = abs(p1[1] - p2[1])
    di = min(di, L - di)
    dj = min(dj, L - dj)
    return math.sqrt(di * di + dj * dj)


def r_bin_assign(r):
    """Return bin index k in R_GRID, or None if outside all bins."""
    if r < R_GRID_MIN_EDGE or r >= R_GRID_MAX_EDGE:
        return None
    # R_GRID is uniform at DR_BIN starting at R_GRID[0]
    k = int(round((r - R_GRID[0]) / DR_BIN))
    if 0 <= k < len(R_GRID):
        r_k = R_GRID[k]
        if r_k - DR_BIN / 2 <= r < r_k + DR_BIN / 2:
            return k
    return None


# ---------------------------------------------------------------------------
# Per-seed execution: evolve, extract motifs per snapshot
# ---------------------------------------------------------------------------
def run_seed(seed):
    t_seed = time.time()
    print(f"Seed {seed} — calibration + evolution...", file=sys.stderr)
    calibration = run_calibration_for_seed(seed)
    w = interpolate_w(calibration, XI_TARGET)
    snapshots, xis = evolve_40snap(seed, w)
    xi_finite = [x for x in xis if np.isfinite(x)]
    xi_measured = float(np.mean(xi_finite)) if xi_finite else float('nan')
    miss = abs(xi_measured - XI_TARGET) / XI_TARGET

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
        miss_new = abs(xi_new - XI_TARGET) / XI_TARGET
        if miss_new < miss:
            w = w_new
            xi_measured = xi_new
            snapshots = snapshots_new
            miss = miss_new
            refinement_used = True

    L_ray = DIMLESS_HINGE * xi_measured
    if in_window(L_ray, WINDOW_A) or in_window(L_ray, WINDOW_B):
        raise RuntimeError(
            f"seed {seed}: L_ray={L_ray} in a resonance window.")
    r_diag = r_diag_of(L_ray)
    out_of_scope = (r_diag != 1)

    motifs_per_snap = []
    for p in snapshots:
        m = extract_motifs_with_positions(p, L_ray)
        motifs_per_snap.append(m)

    total_motifs = sum(len(m) for m in motifs_per_snap)
    print(f"  seed={seed}  ξ_meas={xi_measured:.4f} (miss {miss*100:.2f}%, "
          f"refined={refinement_used})  L={L_ray:.4f}  r_diag={r_diag}  "
          f"N_motifs_total={total_motifs}  t={time.time()-t_seed:.1f}s",
          file=sys.stderr)

    return {
        "seed": seed,
        "xi_measured": xi_measured,
        "xi_miss_fraction": miss,
        "w_used": w,
        "refinement_used": refinement_used,
        "L_ray": L_ray,
        "r_diag": r_diag,
        "out_of_scope": out_of_scope,
        "N_motifs_total": total_motifs,
        "motifs_per_snap": motifs_per_snap,
        "calibration_prepass": calibration,
        "wall_seconds": time.time() - t_seed,
    }


# ---------------------------------------------------------------------------
# Pair enumeration + r-binning per seed
# ---------------------------------------------------------------------------
def accumulate_pairs_per_seed(motifs_per_snap):
    """Return pair_pool[r_bin] = [(ρ_i, ρ_j), ...] accumulated across
    all 40 snapshots."""
    pair_pool = {k: [] for k in range(len(R_GRID))}
    for snap_motifs in motifs_per_snap:
        n = len(snap_motifs)
        for a in range(n):
            m_a = snap_motifs[a]
            for b in range(a + 1, n):
                m_b = snap_motifs[b]
                r = min_image_distance((m_a["i"], m_a["j"]),
                                        (m_b["i"], m_b["j"]))
                k = r_bin_assign(r)
                if k is None:
                    continue
                pair_pool[k].append((m_a["rho"], m_b["rho"]))
    return pair_pool


# ---------------------------------------------------------------------------
# Correlation estimators
# ---------------------------------------------------------------------------
def pearson_C(pair_pool, rho_bar, var_rho):
    if len(pair_pool) < 2 or var_rho <= 0:
        return None
    xs = np.array([p[0] for p in pair_pool])
    ys = np.array([p[1] for p in pair_pool])
    corr = float(np.mean((xs - rho_bar) * (ys - rho_bar)) / var_rho)
    return 2.0 * (1.0 - corr)


def spearman_C(pair_pool):
    if len(pair_pool) < 3:
        return None
    xs = np.array([p[0] for p in pair_pool])
    ys = np.array([p[1] for p in pair_pool])
    if np.std(xs) == 0 or np.std(ys) == 0:
        return None
    rho_s, _ = stats.spearmanr(xs, ys)
    if not np.isfinite(rho_s):
        return None
    return 2.0 * (1.0 - float(rho_s))


def bootstrap_ensemble_C(pair_pool, rho_bar, var_rho,
                          B=BOOTSTRAP_B, rng_seed=BOOTSTRAP_RNG_SEED):
    N = len(pair_pool)
    if N < MIN_PAIRS_ENSEMBLE or var_rho <= 0:
        return {
            "C": None, "C_CI_lo": None, "C_CI_hi": None,
            "low_N": True, "bootstrap_values": [],
        }
    rng = np.random.default_rng(rng_seed)
    xs = np.array([p[0] for p in pair_pool])
    ys = np.array([p[1] for p in pair_pool])
    C_vals = np.empty(B, dtype=float)
    for b in range(B):
        idx = rng.integers(0, N, size=N)
        corr = np.mean((xs[idx] - rho_bar) * (ys[idx] - rho_bar)) / var_rho
        C_vals[b] = 2.0 * (1.0 - corr)
    C_central = pearson_C(pair_pool, rho_bar, var_rho)
    return {
        "C": C_central,
        "C_CI_lo": float(np.quantile(C_vals, 0.16)),
        "C_CI_hi": float(np.quantile(C_vals, 0.84)),
        "low_N": False,
        "bootstrap_values": C_vals.tolist(),
    }


# ---------------------------------------------------------------------------
# Half-rise interpolation and bootstrap ratio
# ---------------------------------------------------------------------------
def linear_interp_halfrise(r_grid, C_values):
    """Return r such that C(r) = 1 via linear interpolation between
    bracketing grid points. Returns None if no crossing found."""
    for k in range(len(r_grid) - 1):
        C_k = C_values[k]
        C_k1 = C_values[k + 1]
        if C_k is None or C_k1 is None:
            continue
        if not np.isfinite(C_k) or not np.isfinite(C_k1):
            continue
        if (C_k < 1) == (C_k1 < 1):
            continue
        r_k = r_grid[k]
        r_k1 = r_grid[k + 1]
        denom = (C_k1 - C_k)
        if abs(denom) < 1e-12:
            continue
        return r_k + (r_k1 - r_k) * (1.0 - C_k) / denom
    return None


def bootstrap_half_rise(bootstrap_C_arrays, r_grid):
    """Given per-r-bin bootstrap arrays, compute re-interpolated
    half-rise values. Returns (16%-quantile, 84%-quantile, samples)
    3-tuple, or None if insufficient data."""
    non_empty_lengths = [len(a) for a in bootstrap_C_arrays if len(a) > 0]
    if not non_empty_lengths:
        return None
    B = min(non_empty_lengths)
    if B == 0:
        return None
    r_half_samples = []
    for b in range(B):
        C_vals = [(a[b] if len(a) > b else None)
                  for a in bootstrap_C_arrays]
        rh = linear_interp_halfrise(r_grid, C_vals)
        if rh is not None:
            r_half_samples.append(rh)
    if len(r_half_samples) < 10:
        return None
    return (float(np.quantile(r_half_samples, 0.16)),
            float(np.quantile(r_half_samples, 0.84)),
            r_half_samples)


# ---------------------------------------------------------------------------
# Verdict logic
# ---------------------------------------------------------------------------
def compute_verdict(ratio_central, ratio_bootstrap_band):
    if ratio_central is None:
        return ("Inconclusive",
                "No C(r) = 1 crossing found in r_grid range")
    if VERDICT_CONFIRMED_LO <= ratio_central <= VERDICT_CONFIRMED_HI:
        # Check whether bootstrap band straddles a threshold
        if ratio_bootstrap_band is not None:
            lo, hi = ratio_bootstrap_band[:2]
            if lo < VERDICT_CONFIRMED_LO or hi > VERDICT_CONFIRMED_HI:
                return ("Confirmed-marginal",
                        f"ratio = {ratio_central:.3f} in [0.75, 0.85] "
                        f"but bootstrap 16–84 = [{lo:.3f}, {hi:.3f}] "
                        "straddles a threshold")
        return ("Confirmed",
                f"ratio = {ratio_central:.3f} ∈ [0.75, 0.85] "
                "(tenth-pass 0.80 ± 0.05 band)")
    if ratio_central < VERDICT_REFUTED_LO or ratio_central > VERDICT_REFUTED_HI:
        return ("Refuted",
                f"ratio = {ratio_central:.3f} ∉ [0.70, 0.90] "
                "(outside double envelope of tenth-pass prediction)")
    return ("Inconclusive",
            f"ratio = {ratio_central:.3f} in marginal band "
            "[0.70, 0.75) ∪ (0.85, 0.90]; "
            "Δr = 0.25 refinement recommended")


# ---------------------------------------------------------------------------
# Master driver
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    t_master = time.time()
    assert_no_resonance_plan()

    print(f"F4 two-point correlation scan at ξ_target = {XI_TARGET} lu, "
          f"{len(SEEDS)} seeds, {len(R_GRID)} r-bins",
          file=sys.stderr)

    # 1. Per-seed evolution + motif extraction
    per_seed_results = []
    for seed in SEEDS:
        per_seed_results.append(run_seed(seed))

    # 2. Global pool statistics for Pearson estimator
    all_rho = []
    for r in per_seed_results:
        for snap in r["motifs_per_snap"]:
            for m in snap:
                all_rho.append(m["rho"])
    rho_bar = float(np.mean(all_rho)) if all_rho else 0.0
    var_rho = float(np.var(all_rho, ddof=1)) if len(all_rho) >= 2 else 0.0
    print(f"\nGlobal pool: N_motifs = {len(all_rho)}, "
          f"ρ̄ = {rho_bar:.6f}, σ²_ρ = {var_rho:.6f}",
          file=sys.stderr)

    # 3. Per-seed pair pools
    pair_pool_per_seed = {}
    for r in per_seed_results:
        pair_pool_per_seed[r["seed"]] = accumulate_pairs_per_seed(
            r["motifs_per_snap"])

    # 4. Ensemble pair pools (concatenate across seeds)
    ensemble_pool = {k: [] for k in range(len(R_GRID))}
    for seed_pool in pair_pool_per_seed.values():
        for k, pairs in seed_pool.items():
            ensemble_pool[k].extend(pairs)

    # Count totals
    N_pairs_total = sum(len(v) for v in ensemble_pool.values())
    N_pairs_unbinned = 0  # r-bin_assign returned None
    # Count unbinned for diagnostic
    for r in per_seed_results:
        for snap in r["motifs_per_snap"]:
            n = len(snap)
            for a in range(n):
                m_a = snap[a]
                for b in range(a + 1, n):
                    m_b = snap[b]
                    d = min_image_distance(
                        (m_a["i"], m_a["j"]), (m_b["i"], m_b["j"]))
                    if r_bin_assign(d) is None:
                        N_pairs_unbinned += 1
    print(f"Pair counts: total binned = {N_pairs_total}, "
          f"unbinned (outside r-grid) = {N_pairs_unbinned}",
          file=sys.stderr)

    # 5. Per-r-bin ensemble estimators + bootstrap
    r_bins_data = []
    bootstrap_arrays = []
    C_ensemble_central = []
    for k in range(len(R_GRID)):
        pool = ensemble_pool[k]
        bs = bootstrap_ensemble_C(pool, rho_bar, var_rho)
        C_rank = spearman_C(pool)
        if bs["C"] is not None and C_rank is not None:
            model_band_rel = abs(bs["C"] - C_rank) / max(abs(bs["C"]), 1e-12)
        else:
            model_band_rel = None
        # Per-seed C_seed per bin
        per_seed_C = {}
        per_seed_N = {}
        for seed in SEEDS:
            sp = pair_pool_per_seed[seed][k]
            per_seed_N[seed] = len(sp)
            if len(sp) >= MIN_PAIRS_PER_SEED:
                per_seed_C[seed] = pearson_C(sp, rho_bar, var_rho)
            else:
                per_seed_C[seed] = None
        per_seed_C_valid = [v for v in per_seed_C.values()
                            if v is not None and np.isfinite(v)]
        if len(per_seed_C_valid) >= 2 and np.mean(per_seed_C_valid) != 0:
            CoV = (float(np.std(per_seed_C_valid, ddof=1))
                   / abs(float(np.mean(per_seed_C_valid))))
            N_seeds_in_CoV = len(per_seed_C_valid)
        else:
            CoV = None
            N_seeds_in_CoV = len(per_seed_C_valid)
        N_per_seed_mean = (float(np.mean(list(per_seed_N.values())))
                           if per_seed_N else 0.0)
        low_N_any_seed = any(per_seed_N[s] < MIN_PAIRS_PER_SEED
                             for s in SEEDS)
        r_bins_data.append({
            "r": R_GRID[k],
            "N_pairs_ensemble": len(pool),
            "C_ensemble": bs["C"],
            "C_CI_lo": bs["C_CI_lo"],
            "C_CI_hi": bs["C_CI_hi"],
            "C_ensemble_rank": C_rank,
            "model_band_rel": model_band_rel,
            "per_seed_C": per_seed_C,
            "per_seed_N": per_seed_N,
            "CoV_across_seeds": CoV,
            "N_seeds_in_CoV": N_seeds_in_CoV,
            "N_pairs_per_seed_mean": N_per_seed_mean,
            "low_N_ensemble": bs["low_N"],
            "low_N_any_seed": low_N_any_seed,
            "spearman_undefined": (C_rank is None),
        })
        bootstrap_arrays.append(bs["bootstrap_values"])
        C_ensemble_central.append(bs["C"])
        print(f"  r={R_GRID[k]:.2f}  N_pairs={len(pool)}  "
              f"C={bs['C']}  rank={C_rank}  CoV={CoV}  "
              f"low_N={bs['low_N']}",
              file=sys.stderr)

    # 6. Half-rise interpolation + bootstrap
    r_half_filt = linear_interp_halfrise(R_GRID, C_ensemble_central)
    r_half_unfilt = XI_CANONICAL
    ratio_central = (r_half_filt / r_half_unfilt
                     if r_half_filt is not None else None)
    bs_half = bootstrap_half_rise(bootstrap_arrays, R_GRID)
    if bs_half is not None:
        r_half_lo, r_half_hi, r_half_samples = bs_half
        if r_half_lo is not None and r_half_hi is not None:
            ratio_lo = r_half_lo / r_half_unfilt
            ratio_hi = r_half_hi / r_half_unfilt
        else:
            ratio_lo = ratio_hi = None
    else:
        r_half_lo = r_half_hi = None
        ratio_lo = ratio_hi = None
        r_half_samples = []

    print(f"\nHalf-rise: r_half_filt = {r_half_filt}, "
          f"r_half_unfilt = {r_half_unfilt}, ratio = {ratio_central}",
          file=sys.stderr)

    # 7. Verdict
    ratio_bootstrap_band = ((ratio_lo, ratio_hi)
                            if ratio_lo is not None else None)
    verdict, reason = compute_verdict(ratio_central, ratio_bootstrap_band)
    print(f"Verdict: {verdict} — {reason}", file=sys.stderr)

    # 8. Rigid-endpoint check
    C_at_rmin = C_ensemble_central[0] if C_ensemble_central else None
    C_at_rmax = C_ensemble_central[-1] if C_ensemble_central else None

    # 9. Write CSV (ensemble table)
    csv_path = os.path.join(OUT_DIR, "correlation_twopoint_table.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "r_target", "N_pairs_ensemble",
            "C_ensemble", "C_CI_lo", "C_CI_hi",
            "C_ensemble_rank", "model_band_rel",
            "CoV_across_seeds", "N_seeds_in_CoV",
            "N_pairs_per_seed_mean",
            "low_N_ensemble", "low_N_any_seed",
            "Spearman_undefined", "bootstrap_iterations",
        ])
        for b in r_bins_data:
            w.writerow([
                b["r"], b["N_pairs_ensemble"],
                b["C_ensemble"], b["C_CI_lo"], b["C_CI_hi"],
                b["C_ensemble_rank"], b["model_band_rel"],
                b["CoV_across_seeds"], b["N_seeds_in_CoV"],
                b["N_pairs_per_seed_mean"],
                b["low_N_ensemble"], b["low_N_any_seed"],
                b["spearman_undefined"], BOOTSTRAP_B,
            ])

    # 10. Write per-seed CSV
    per_seed_csv = os.path.join(OUT_DIR, "correlation_twopoint_per_seed.csv")
    with open(per_seed_csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "seed", "r_target", "N_pairs_seed", "C_seed", "C_seed_low_N",
            "xi_seed", "L_ray_seed",
        ])
        seed_xi_L = {r["seed"]: (r["xi_measured"], r["L_ray"])
                     for r in per_seed_results}
        for b in r_bins_data:
            for seed in SEEDS:
                N = b["per_seed_N"][seed]
                C_s = b["per_seed_C"][seed]
                xi_s, L_s = seed_xi_L[seed]
                w.writerow([
                    seed, b["r"], N, C_s,
                    (N < MIN_PAIRS_PER_SEED),
                    xi_s, L_s,
                ])

    # 11. Write summary JSON
    out = {
        "method": ("ED-SC 3.4 F4 two-point correlation at canonical ξ; "
                   "measures C_redshift(r) = 2[1 − ξ_φ(r)/σ_0²] on the "
                   "motif-ratio pool with Pearson + Spearman estimators"),
        "simulator_of_record":
            "r2_grf_falsifier_tests.py + ED_Update_Rule.ed_step_mobility",
        "xi_canonical_lattice_units": XI_CANONICAL,
        "xi_target": XI_TARGET,
        "alpha_filt": ALPHA_FILT,
        "N_req": N_REQ,
        "dimensionless_hinge": DIMLESS_HINGE,
        "r_grid": R_GRID,
        "dr_bin": DR_BIN,
        "seeds": SEEDS,
        "canonical_params": {
            "alpha": fr.ALPHA0, "gamma": fr.GAMMA,
            "noise_sigma": fr.NOISE0,
            "mobility_exp": fr.MOBILITY_EXP,
            "steps": fr.STEPS, "size": fr.SIZE, "dt": fr.DT,
        },
        "resonance_windows_excluded": {
            "A": list(WINDOW_A), "B": list(WINDOW_B)},
        "calibration_prepass_per_seed": {
            r["seed"]: r["calibration_prepass"]
            for r in per_seed_results
        },
        "per_seed": [
            {k: v for k, v in r.items() if k != "motifs_per_snap"}
            for r in per_seed_results
        ],
        "global_pool": {
            "rho_bar": rho_bar,
            "sigma2_rho": var_rho,
            "N_motifs_total": len(all_rho),
        },
        "r_bins": [
            {k: v for k, v in b.items()
             if k not in ("per_seed_C", "per_seed_N")}
            | {"per_seed_C": b["per_seed_C"],
               "per_seed_N": b["per_seed_N"]}
            for b in r_bins_data
        ],
        "half_rise": {
            "r_half_filt_central": r_half_filt,
            "r_half_filt_bootstrap_16_84": (
                [r_half_lo, r_half_hi]
                if r_half_lo is not None else None),
            "r_half_unfilt": r_half_unfilt,
            "ratio_central": ratio_central,
            "ratio_bootstrap_16_84": (
                [ratio_lo, ratio_hi]
                if ratio_lo is not None else None),
            "n_bootstrap_samples_valid": len(r_half_samples),
        },
        "verdict": {
            "verdict": verdict,
            "reason": reason,
            "tenth_pass_prediction": "0.80 ± 0.05 (GR-SC 1.7)",
            "confirmed_threshold": [VERDICT_CONFIRMED_LO,
                                     VERDICT_CONFIRMED_HI],
            "refuted_threshold_low": VERDICT_REFUTED_LO,
            "refuted_threshold_high": VERDICT_REFUTED_HI,
        },
        "diagnostics": {
            "r_diag_excursions": [
                {"seed": r["seed"], "xi": r["xi_measured"],
                 "L_ray": r["L_ray"], "r_diag": r["r_diag"]}
                for r in per_seed_results if r["out_of_scope"]
            ],
            "resonance_window_intrusions": [],
            "rigid_endpoint_check_C_at_r_min": C_at_rmin,
            "rigid_endpoint_check_C_at_r_max": C_at_rmax,
            "N_pairs_total_across_all_bins": N_pairs_total,
            "N_pairs_unbinned": N_pairs_unbinned,
            "calibration_component_status": (
                "N/A (Δr=0.25 refinement not run)"),
        },
        "filter_relaxation_amendment": {
            "canonical_N_req": 4,
            "F4_alt_N_req": 2,
            "motivation": (
                "canonical filter pair-count sparsity "
                "(51 pairs across 10 r-bins at canonical "
                "N_req=4); see "
                "theory/ED_SC_3_4_twopoint_FilterRelaxation.md"),
            "scope_restriction": (
                "C_redshift(r) measurement only; does not "
                "affect canonical operating point or any other "
                "ED-SC / GR-SC claim"),
            "canonical_F4_artefact": (
                "outputs/ed_sc_3_4_twopoint/"
                "correlation_twopoint_summary.json"),
            "canonical_F4_verdict": (
                "Inconclusive (pair-count sparsity)"),
        },
        "wall_seconds_total": time.time() - t_master,
    }

    json_path = os.path.join(OUT_DIR, "correlation_twopoint_summary.json")
    with open(json_path, "w") as f:
        json.dump(out, f, indent=2)

    print(f"\nWrote table → {csv_path}", file=sys.stderr)
    print(f"Wrote per-seed → {per_seed_csv}", file=sys.stderr)
    print(f"Wrote summary → {json_path}", file=sys.stderr)
    print(json.dumps({
        "N_seeds": len(SEEDS),
        "N_r_bins": len(R_GRID),
        "N_motifs_total": len(all_rho),
        "N_pairs_total": N_pairs_total,
        "rho_bar": rho_bar,
        "sigma2_rho": var_rho,
        "r_half_filt_central": r_half_filt,
        "r_half_unfilt": r_half_unfilt,
        "ratio_central": ratio_central,
        "ratio_bootstrap_16_84": (
            [ratio_lo, ratio_hi]
            if ratio_lo is not None else None),
        "verdict": verdict,
        "verdict_reason": reason,
        "rigid_C_at_r_min": C_at_rmin,
        "rigid_C_at_r_max": C_at_rmax,
        "wall_seconds_total": out["wall_seconds_total"],
    }, indent=2))


if __name__ == "__main__":
    main()
