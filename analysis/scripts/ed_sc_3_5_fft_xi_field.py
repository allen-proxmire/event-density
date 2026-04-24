"""ED-SC 3.5 FFT-based field-autocorrelation driver.

Pre-registered in:
  theory/ED_SC_3_5_FFT_XiField_Scoping.md  (scope)
  theory/ED_SC_3_5_FFT_XiField_Driver.md   (driver spec)

Measures the two-point field autocorrelation

    ξ_φ(r) = ⟨ φ(x) φ(x+r) ⟩ − ⟨φ⟩²

on 10 seeds × 40 snapshots at canonical ξ_target = 1.7575 lu, for
two channels:

    (A) bulk p-field                   — primary channel
    (B) motif-mask-weighted p-field    — filtered primary channel
        M(x) is the canonical (α_filt=0.25, N_req=4) motif indicator

Radial-averages on every Z² shell radius (no pair-binning obstruction).
Ensemble-averages across seeds; bootstraps over seeds (4000 resamples).
Extracts r_half on each channel as the smallest r where

    C_redshift(r) = 2 [1 − ξ_φ(r) / σ_0²] = 1,

equivalently ξ_φ(r)/σ_0² = 0.5. Computes ratio = r_half_B / r_half_A
and applies the tenth-pass GR-SC 1.7 four-way verdict taxonomy
(Confirmed / Confirmed-marginal / Refuted / Inconclusive), with a
self-calibration guardrail: r_half_A must match ξ_canonical within
±10 %.

Scaffolding (calibration, evolution, motif-pass, resonance guards)
inherits verbatim from the F4-alt driver
`ed_sc_3_4_twopoint_correlation_relaxed.py`; only the measurement
core (FFT radial-shell autocorrelation) and the bootstrap scheme
(over seeds, not over pairs) are new.

Simulator of record:
  r2_grf_falsifier_tests.py  +  ED_Update_Rule.ed_step_mobility

Writes:
  outputs/ed_sc_3_5_fft_xi_field/xi_field_profile.csv
  outputs/ed_sc_3_5_fft_xi_field/xi_field_per_seed.csv
  outputs/ed_sc_3_5_fft_xi_field/xi_field_summary.json

No simulator constants are mutated. Deterministic given seeds.
"""
import csv
import json
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
# Canonical constants (inherited from F4-alt; filter is CANONICAL N_req=4)
# ---------------------------------------------------------------------------
XI_CANONICAL = 1.7575325729470939
XI_BURN_IN = 100
XI_SNAP_EVERY = 10

ALPHA_FILT = 0.25
N_REQ = 4  # CANONICAL filter for motif mask (ED-SC 3.5 scoping §2)
DIMLESS_HINGE = 1.08
DIAG_COS = 0.707

WINDOW_A = (2.50, 2.80)
WINDOW_B = (3.50, 3.90)

XI_TARGET = 1.7575
SEEDS = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]

CALIBRATION_W_GRID = [0.05, 0.08, 0.10, 0.13, 0.16, 0.20, 0.25, 0.30, 0.35]
CALIBRATION_TOL = 0.01

# Bootstrap config (over seeds; distinct RNG seed from F4/F4-alt)
BOOTSTRAP_B = 4000
BOOTSTRAP_RNG_SEED = 199

# Verdict thresholds (tenth-pass GR-SC 1.7 prediction: 0.80 ± 0.05)
VERDICT_CONFIRMED_LO = 0.75
VERDICT_CONFIRMED_HI = 0.85
VERDICT_REFUTED_LO = 0.70
VERDICT_REFUTED_HI = 0.90

# Self-calibration guardrail (ED-SC 3.5 scoping §4)
SELF_CAL_TOL = 0.10

OUT_DIR = os.path.join(HERE, "..", "..", "outputs", "ed_sc_3_5_fft_xi_field")


# ---------------------------------------------------------------------------
# ξ half-decay (same as F4-alt; used for calibration check)
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
# Evolution + calibration (inherited verbatim from F4-alt)
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
# Resonance guards (inherited from F4-alt)
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
# Motif-mask extraction (new; canonical filter)
# ---------------------------------------------------------------------------
def extract_motif_mask(snapshot, L_ray):
    """Return a float 0/1 mask of sites admitted by the canonical motif
    filter at (α_filt, N_req) = (0.25, 4) and the per-seed L_ray."""
    E = fr.smooth_field(snapshot)
    p_hat = float(snapshot.mean())
    p_std = float(snapshot.std())
    sads = fr.find_morse_saddles(E)
    mask = np.zeros_like(snapshot, dtype=float)
    for s in sads:
        if fr.motif_pass(s, E, p_hat, p_std,
                         ALPHA_FILT, L_ray, N_REQ):
            mask[int(s["i"]), int(s["j"])] = 1.0
    return mask


# ---------------------------------------------------------------------------
# FFT radial-shell autocorrelation core (ED-SC 3.5 driver §3.2)
# ---------------------------------------------------------------------------
# Precompute the Z² shell structure once (fr.SIZE is fixed).
def _build_shell_index(N):
    cy, cx = N // 2, N // 2
    y_idx, x_idx = np.indices((N, N))
    r_squared = (y_idx - cy) ** 2 + (x_idx - cx) ** 2
    unique_r2 = np.unique(r_squared)
    shells = np.sqrt(unique_r2.astype(float))
    keep = shells <= (N // 2)
    unique_r2 = unique_r2[keep]
    shells = shells[keep]
    # Precompute the flat index lists per shell for fast averaging.
    shell_masks = [(r_squared == r2) for r2 in unique_r2]
    n_sites_shell = np.array([int(m.sum()) for m in shell_masks])
    return shells, shell_masks, n_sites_shell


_SHELLS, _SHELL_MASKS, _N_SITES_SHELL = _build_shell_index(fr.SIZE)
N_SHELLS = len(_SHELLS)


def fft_autocorr(field):
    """Return the radially-averaged autocorrelation on Z² shells.

    Output shape = (N_SHELLS,). Shell[0] is r = 0 (variance σ_0²).
    Mean-subtracts the field before transforming.
    """
    N = field.shape[0]
    f = field - np.mean(field)
    F = fft2(f)
    P = np.abs(F) ** 2
    C = np.real(ifft2(P)) / (N * N)
    C = fftshift(C)
    xi_shells = np.empty(N_SHELLS, dtype=float)
    for k, m in enumerate(_SHELL_MASKS):
        xi_shells[k] = C[m].mean()
    return xi_shells


# ---------------------------------------------------------------------------
# Per-seed execution
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

    # Per-snapshot FFT autocorrelations for channels A and B
    xi_A_snaps = np.empty((len(snapshots), N_SHELLS), dtype=float)
    xi_B_snaps = np.empty((len(snapshots), N_SHELLS), dtype=float)
    mask_densities = np.empty(len(snapshots), dtype=float)
    masks_all_zero = 0
    for s_idx, p in enumerate(snapshots):
        mask = extract_motif_mask(p, L_ray)
        mask_densities[s_idx] = float(mask.mean())
        if mask.sum() == 0:
            masks_all_zero += 1
        xi_A_snaps[s_idx] = fft_autocorr(p)
        xi_B_snaps[s_idx] = fft_autocorr(p * mask)

    xi_A_seed = xi_A_snaps.mean(axis=0)
    xi_B_seed = xi_B_snaps.mean(axis=0)
    mean_mask_density = float(mask_densities.mean())

    print(f"  seed={seed}  ξ_meas={xi_measured:.4f} (miss {miss*100:.2f}%, "
          f"refined={refinement_used})  L={L_ray:.4f}  r_diag={r_diag}  "
          f"⟨ρ_M⟩={mean_mask_density:.5f}  empty_masks={masks_all_zero}/40  "
          f"σ_0²_A={xi_A_seed[0]:.4f}  σ_0²_B={xi_B_seed[0]:.4g}  "
          f"t={time.time()-t_seed:.1f}s",
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
        "xi_A_seed": xi_A_seed,
        "xi_B_seed": xi_B_seed,
        "mean_mask_density": mean_mask_density,
        "empty_masks_count": masks_all_zero,
        "calibration_prepass": calibration,
        "wall_seconds": time.time() - t_seed,
    }


# ---------------------------------------------------------------------------
# C_redshift + half-rise extraction
# ---------------------------------------------------------------------------
def C_from_xi(xi_curve):
    """Return C_redshift(r) = 2 [1 − ξ(r)/ξ(0)]. Returns None if ξ(0) ≤ 0."""
    if xi_curve[0] <= 0 or not np.isfinite(xi_curve[0]):
        return None
    return 2.0 * (1.0 - xi_curve / xi_curve[0])


def all_crossings(shells, C_values, target=1.0):
    """All smallest-first linear-interpolation crossings of C = target."""
    crossings = []
    for k in range(len(shells) - 1):
        c_k, c_k1 = C_values[k], C_values[k + 1]
        if not (np.isfinite(c_k) and np.isfinite(c_k1)):
            continue
        if (c_k < target) == (c_k1 < target):
            continue
        denom = c_k1 - c_k
        if abs(denom) < 1e-12:
            continue
        r_cross = shells[k] + (shells[k + 1] - shells[k]) * \
                  (target - c_k) / denom
        crossings.append(r_cross)
    return crossings


def smallest_crossing(shells, C_values, target=1.0):
    cs = all_crossings(shells, C_values, target)
    return cs[0] if cs else None


def is_non_monotone(C_values, noise_tol=0.05):
    """Flag if C(r) decreases by more than noise_tol at any step after
    the first significant rise (heuristic for monotonicity diagnostics)."""
    finite = C_values[np.isfinite(C_values)]
    if len(finite) < 3:
        return False
    diffs = np.diff(finite)
    return bool(np.any(diffs < -noise_tol))


# ---------------------------------------------------------------------------
# Verdict logic (four-way; includes self-calibration guardrail)
# ---------------------------------------------------------------------------
def compute_verdict(ratio_central, ratio_bootstrap_band, self_cal_ok,
                    self_cal_miss_frac):
    if not self_cal_ok:
        return ("Inconclusive",
                f"Self-calibration guardrail failed: r_half_A deviates "
                f"from ξ_canonical by {self_cal_miss_frac*100:.1f}% "
                f"> {SELF_CAL_TOL*100:.0f}% tolerance")
    if ratio_central is None:
        return ("Inconclusive",
                "No C_B(r) = 1 crossing found in measured r-range")
    if VERDICT_CONFIRMED_LO <= ratio_central <= VERDICT_CONFIRMED_HI:
        if ratio_bootstrap_band is not None:
            lo, hi = ratio_bootstrap_band
            if (lo is not None and hi is not None
                    and (lo < VERDICT_CONFIRMED_LO
                         or hi > VERDICT_CONFIRMED_HI)):
                return ("Confirmed-marginal",
                        f"ratio = {ratio_central:.3f} in [0.75, 0.85] "
                        f"but bootstrap 16-84 = [{lo:.3f}, {hi:.3f}] "
                        "straddles a threshold")
        return ("Confirmed",
                f"ratio = {ratio_central:.3f} ∈ [0.75, 0.85] "
                "(tenth-pass 0.80 ± 0.05 band)")
    if ratio_central < VERDICT_REFUTED_LO or ratio_central > VERDICT_REFUTED_HI:
        return ("Refuted",
                f"ratio = {ratio_central:.3f} ∉ [0.70, 0.90] "
                "(outside double envelope of tenth-pass prediction)")
    return ("Confirmed-marginal",
            f"ratio = {ratio_central:.3f} in marginal band "
            "[0.70, 0.75) ∪ (0.85, 0.90]")


# ---------------------------------------------------------------------------
# Master driver
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    t_master = time.time()
    assert_no_resonance_plan()

    print(f"ED-SC 3.5 FFT field-autocorr driver: ξ_target = {XI_TARGET}, "
          f"{len(SEEDS)} seeds × 40 snaps, N_SHELLS = {N_SHELLS} on "
          f"{fr.SIZE}² lattice", file=sys.stderr)

    # 1. Per-seed execution
    per_seed_results = []
    for seed in SEEDS:
        per_seed_results.append(run_seed(seed))

    # 2. Stack per-seed curves and compute ensemble centrals
    per_seed_xi_A = np.array([r["xi_A_seed"] for r in per_seed_results])
    per_seed_xi_B = np.array([r["xi_B_seed"] for r in per_seed_results])
    xi_A_central = per_seed_xi_A.mean(axis=0)
    xi_B_central = per_seed_xi_B.mean(axis=0)

    C_A_central = C_from_xi(xi_A_central)
    C_B_central = C_from_xi(xi_B_central)

    print(f"\nEnsemble σ_0²_A = {xi_A_central[0]:.6f}, "
          f"σ_0²_B = {xi_B_central[0]:.6g}", file=sys.stderr)

    # 3. Ensemble half-rise extraction
    r_half_A = (smallest_crossing(_SHELLS, C_A_central)
                if C_A_central is not None else None)
    r_half_B = (smallest_crossing(_SHELLS, C_B_central)
                if C_B_central is not None else None)
    all_cross_A = (all_crossings(_SHELLS, C_A_central)
                   if C_A_central is not None else [])
    all_cross_B = (all_crossings(_SHELLS, C_B_central)
                   if C_B_central is not None else [])
    multi_crossing_A = len(all_cross_A) > 1
    multi_crossing_B = len(all_cross_B) > 1
    non_monotone_A = (is_non_monotone(C_A_central)
                      if C_A_central is not None else False)
    non_monotone_B = (is_non_monotone(C_B_central)
                      if C_B_central is not None else False)

    ratio_central = (r_half_B / r_half_A
                     if (r_half_A is not None and r_half_B is not None
                         and r_half_A > 0)
                     else None)

    print(f"Ensemble half-rise: r_half_A = {r_half_A}, "
          f"r_half_B = {r_half_B}, ratio = {ratio_central}",
          file=sys.stderr)

    # 4. Self-calibration check (ED-SC 3.5 scoping §4)
    if r_half_A is not None and r_half_A > 0:
        self_cal_miss = abs(r_half_A - XI_CANONICAL) / XI_CANONICAL
        self_cal_ok = self_cal_miss <= SELF_CAL_TOL
    else:
        self_cal_miss = float('nan')
        self_cal_ok = False
    print(f"Self-cal: r_half_A = {r_half_A} vs ξ_canonical = "
          f"{XI_CANONICAL:.4f} → miss = {self_cal_miss*100:.2f}%, "
          f"passed = {self_cal_ok}", file=sys.stderr)

    # 5. Bootstrap over seeds
    n_seeds = len(SEEDS)
    rng = np.random.default_rng(BOOTSTRAP_RNG_SEED)
    bootstrap_C_A = np.empty((BOOTSTRAP_B, N_SHELLS), dtype=float)
    bootstrap_C_B = np.empty((BOOTSTRAP_B, N_SHELLS), dtype=float)
    bootstrap_r_half_A = []
    bootstrap_r_half_B = []
    bootstrap_ratios = []
    n_valid_bootstrap = 0
    for b in range(BOOTSTRAP_B):
        idx = rng.integers(0, n_seeds, size=n_seeds)
        A_b = per_seed_xi_A[idx].mean(axis=0)
        B_b = per_seed_xi_B[idx].mean(axis=0)
        C_A_b = C_from_xi(A_b)
        C_B_b = C_from_xi(B_b)
        if C_A_b is None or C_B_b is None:
            bootstrap_C_A[b] = np.nan
            bootstrap_C_B[b] = np.nan
            continue
        bootstrap_C_A[b] = C_A_b
        bootstrap_C_B[b] = C_B_b
        r_A_b = smallest_crossing(_SHELLS, C_A_b)
        r_B_b = smallest_crossing(_SHELLS, C_B_b)
        if r_A_b is not None:
            bootstrap_r_half_A.append(r_A_b)
        if r_B_b is not None:
            bootstrap_r_half_B.append(r_B_b)
        if (r_A_b is not None and r_B_b is not None and r_A_b > 0):
            bootstrap_ratios.append(r_B_b / r_A_b)
        n_valid_bootstrap += 1

    # Per-shell bootstrap bands
    C_A_lo = np.nanquantile(bootstrap_C_A, 0.16, axis=0)
    C_A_hi = np.nanquantile(bootstrap_C_A, 0.84, axis=0)
    C_B_lo = np.nanquantile(bootstrap_C_B, 0.16, axis=0)
    C_B_hi = np.nanquantile(bootstrap_C_B, 0.84, axis=0)
    xi_A_lo = np.nanquantile(
        np.array([per_seed_xi_A[rng.integers(0, n_seeds, size=n_seeds)].mean(axis=0)
                  for _ in range(1)]), 0.16, axis=0)  # placeholder; we recompute below
    # Recompute ξ bands directly from bootstrap resamples for correctness
    xi_A_boot = np.empty((BOOTSTRAP_B, N_SHELLS), dtype=float)
    xi_B_boot = np.empty((BOOTSTRAP_B, N_SHELLS), dtype=float)
    rng2 = np.random.default_rng(BOOTSTRAP_RNG_SEED)  # reproduce same idx stream
    for b in range(BOOTSTRAP_B):
        idx = rng2.integers(0, n_seeds, size=n_seeds)
        xi_A_boot[b] = per_seed_xi_A[idx].mean(axis=0)
        xi_B_boot[b] = per_seed_xi_B[idx].mean(axis=0)
    xi_A_lo = np.quantile(xi_A_boot, 0.16, axis=0)
    xi_A_hi = np.quantile(xi_A_boot, 0.84, axis=0)
    xi_B_lo = np.quantile(xi_B_boot, 0.16, axis=0)
    xi_B_hi = np.quantile(xi_B_boot, 0.84, axis=0)

    if bootstrap_r_half_A:
        r_half_A_lo = float(np.quantile(bootstrap_r_half_A, 0.16))
        r_half_A_hi = float(np.quantile(bootstrap_r_half_A, 0.84))
    else:
        r_half_A_lo = r_half_A_hi = None
    if bootstrap_r_half_B:
        r_half_B_lo = float(np.quantile(bootstrap_r_half_B, 0.16))
        r_half_B_hi = float(np.quantile(bootstrap_r_half_B, 0.84))
    else:
        r_half_B_lo = r_half_B_hi = None
    if bootstrap_ratios:
        ratio_lo = float(np.quantile(bootstrap_ratios, 0.16))
        ratio_hi = float(np.quantile(bootstrap_ratios, 0.84))
    else:
        ratio_lo = ratio_hi = None

    # 6. Verdict
    ratio_bootstrap_band = ((ratio_lo, ratio_hi)
                            if ratio_lo is not None else None)
    verdict, reason = compute_verdict(ratio_central, ratio_bootstrap_band,
                                      self_cal_ok, self_cal_miss)
    print(f"Verdict: {verdict} — {reason}", file=sys.stderr)

    # 7. Ensemble diagnostics
    mean_mask_density_ensemble = float(np.mean(
        [r["mean_mask_density"] for r in per_seed_results]))

    # 8. Write profile CSV
    profile_path = os.path.join(OUT_DIR, "xi_field_profile.csv")
    with open(profile_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "r_shell", "n_lattice_sites_in_shell",
            "xi_phi_A", "xi_phi_A_CI_lo", "xi_phi_A_CI_hi",
            "C_A", "C_A_CI_lo", "C_A_CI_hi",
            "xi_phi_B", "xi_phi_B_CI_lo", "xi_phi_B_CI_hi",
            "C_B", "C_B_CI_lo", "C_B_CI_hi",
        ])
        for k in range(N_SHELLS):
            w.writerow([
                float(_SHELLS[k]), int(_N_SITES_SHELL[k]),
                float(xi_A_central[k]), float(xi_A_lo[k]), float(xi_A_hi[k]),
                (None if C_A_central is None else float(C_A_central[k])),
                float(C_A_lo[k]), float(C_A_hi[k]),
                float(xi_B_central[k]), float(xi_B_lo[k]), float(xi_B_hi[k]),
                (None if C_B_central is None else float(C_B_central[k])),
                float(C_B_lo[k]), float(C_B_hi[k]),
            ])

    # 9. Write per-seed CSV
    per_seed_csv = os.path.join(OUT_DIR, "xi_field_per_seed.csv")
    with open(per_seed_csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "seed", "r_shell",
            "xi_phi_A_seed", "xi_phi_B_seed",
            "xi_seed", "L_ray_seed", "mean_mask_density_seed",
        ])
        for r in per_seed_results:
            for k in range(N_SHELLS):
                w.writerow([
                    r["seed"], float(_SHELLS[k]),
                    float(r["xi_A_seed"][k]), float(r["xi_B_seed"][k]),
                    r["xi_measured"], r["L_ray"], r["mean_mask_density"],
                ])

    # 10. Write summary JSON
    out = {
        "method": ("ED-SC 3.5 FFT-based bulk-field autocorrelation; "
                   "measures ξ_φ(r) on (A) bulk p-field and (B) motif-mask-"
                   "weighted p-field; primary verdict against GR-SC 1.7 "
                   "half-rise compression prediction"),
        "simulator_of_record":
            "r2_grf_falsifier_tests.py + ED_Update_Rule.ed_step_mobility",
        "xi_canonical_lattice_units": XI_CANONICAL,
        "xi_target": XI_TARGET,
        "alpha_filt": ALPHA_FILT,
        "N_req": N_REQ,
        "dimensionless_hinge": DIMLESS_HINGE,
        "seeds": SEEDS,
        "canonical_params": {
            "alpha": fr.ALPHA0, "gamma": fr.GAMMA,
            "noise_sigma": fr.NOISE0,
            "mobility_exp": fr.MOBILITY_EXP,
            "steps": fr.STEPS, "size": fr.SIZE, "dt": fr.DT,
        },
        "resonance_windows_excluded": {
            "A": list(WINDOW_A), "B": list(WINDOW_B)},
        "shells": [float(x) for x in _SHELLS],
        "n_shells": N_SHELLS,
        "n_lattice_sites_per_shell": [int(x) for x in _N_SITES_SHELL],
        "calibration_prepass_per_seed": {
            r["seed"]: r["calibration_prepass"]
            for r in per_seed_results
        },
        "per_seed": [
            {k: (v if k not in ("xi_A_seed", "xi_B_seed")
                 else [float(x) for x in v])
             for k, v in r.items()
             if k not in ("calibration_prepass",)}
            for r in per_seed_results
        ],
        "bulk_field_channel_A": {
            "xi_phi_central": [float(x) for x in xi_A_central],
            "xi_phi_CI_lo": [float(x) for x in xi_A_lo],
            "xi_phi_CI_hi": [float(x) for x in xi_A_hi],
            "C_central": (None if C_A_central is None
                          else [float(x) for x in C_A_central]),
            "C_CI_lo": [float(x) for x in C_A_lo],
            "C_CI_hi": [float(x) for x in C_A_hi],
            "r_half_central": r_half_A,
            "r_half_bootstrap_16_84": (
                [r_half_A_lo, r_half_A_hi]
                if r_half_A_lo is not None else None),
            "n_bootstrap_samples_valid_for_r_half":
                len(bootstrap_r_half_A),
            "multi_crossing_flag": multi_crossing_A,
            "non_monotone_flag": non_monotone_A,
            "all_crossings": all_cross_A,
        },
        "masked_field_channel_B": {
            "xi_phi_central": [float(x) for x in xi_B_central],
            "xi_phi_CI_lo": [float(x) for x in xi_B_lo],
            "xi_phi_CI_hi": [float(x) for x in xi_B_hi],
            "C_central": (None if C_B_central is None
                          else [float(x) for x in C_B_central]),
            "C_CI_lo": [float(x) for x in C_B_lo],
            "C_CI_hi": [float(x) for x in C_B_hi],
            "r_half_central": r_half_B,
            "r_half_bootstrap_16_84": (
                [r_half_B_lo, r_half_B_hi]
                if r_half_B_lo is not None else None),
            "n_bootstrap_samples_valid_for_r_half":
                len(bootstrap_r_half_B),
            "multi_crossing_flag": multi_crossing_B,
            "non_monotone_flag": non_monotone_B,
            "all_crossings": all_cross_B,
            "mean_mask_density_ensemble": mean_mask_density_ensemble,
        },
        "half_rise_comparison": {
            "r_half_unfilt": r_half_A,
            "r_half_filt": r_half_B,
            "ratio_central": ratio_central,
            "ratio_bootstrap_16_84": (
                [ratio_lo, ratio_hi]
                if ratio_lo is not None else None),
            "n_bootstrap_samples_valid_for_ratio":
                len(bootstrap_ratios),
        },
        "self_calibration_check": {
            "r_half_unfilt": r_half_A,
            "xi_canonical_reference": XI_CANONICAL,
            "miss_fraction": (self_cal_miss
                              if np.isfinite(self_cal_miss) else None),
            "tolerance": SELF_CAL_TOL,
            "passed": bool(self_cal_ok),
        },
        "verdict": {
            "verdict": verdict,
            "reason": reason,
            "tenth_pass_prediction": "0.80 ± 0.05 (GR-SC 1.7)",
            "confirmed_threshold": [VERDICT_CONFIRMED_LO,
                                    VERDICT_CONFIRMED_HI],
            "refuted_threshold_low": VERDICT_REFUTED_LO,
            "refuted_threshold_high": VERDICT_REFUTED_HI,
            "taxonomy": "four-way (inherited from F4)",
        },
        "diagnostics": {
            "non_monotone_A": non_monotone_A,
            "non_monotone_B": non_monotone_B,
            "multi_crossing_A": multi_crossing_A,
            "multi_crossing_B": multi_crossing_B,
            "mean_mask_density_ensemble": mean_mask_density_ensemble,
            "empty_masks_per_seed": {
                r["seed"]: r["empty_masks_count"]
                for r in per_seed_results
            },
            "r_diag_excursions": [
                {"seed": r["seed"], "xi": r["xi_measured"],
                 "L_ray": r["L_ray"], "r_diag": r["r_diag"]}
                for r in per_seed_results if r["out_of_scope"]
            ],
            "resonance_window_intrusions": [],
            "n_valid_bootstrap": n_valid_bootstrap,
        },
        "cross_channel_reconciliation": {
            "parent_F4_sub_arc_verdict":
                "Refuted-by-extension structural (relaxed filter, N_req=2)",
            "parent_F4_canonical_verdict":
                "Inconclusive (pair-count sparsity)",
            "interpretation_matrix_case":
                "pending_integration_memo",
        },
        "wall_seconds_total": time.time() - t_master,
    }

    json_path = os.path.join(OUT_DIR, "xi_field_summary.json")
    with open(json_path, "w") as f:
        json.dump(out, f, indent=2)

    print(f"\nWrote profile → {profile_path}", file=sys.stderr)
    print(f"Wrote per-seed → {per_seed_csv}", file=sys.stderr)
    print(f"Wrote summary → {json_path}", file=sys.stderr)
    print(json.dumps({
        "N_seeds": len(SEEDS),
        "N_shells": N_SHELLS,
        "r_half_unfilt": r_half_A,
        "r_half_filt": r_half_B,
        "ratio_central": ratio_central,
        "ratio_bootstrap_16_84": (
            [ratio_lo, ratio_hi] if ratio_lo is not None else None),
        "self_cal_passed": bool(self_cal_ok),
        "self_cal_miss_fraction": (
            self_cal_miss if np.isfinite(self_cal_miss) else None),
        "verdict": verdict,
        "verdict_reason": reason,
        "mean_mask_density_ensemble": mean_mask_density_ensemble,
        "multi_crossing_A": multi_crossing_A,
        "multi_crossing_B": multi_crossing_B,
        "non_monotone_A": non_monotone_A,
        "non_monotone_B": non_monotone_B,
        "wall_seconds_total": out["wall_seconds_total"],
    }, indent=2))


if __name__ == "__main__":
    main()
