"""ED-SC 3.6 L-Larger three-channel driver.

Pre-registered in:
  theory/ED_SC_3_6_L_Larger_Scoping.md       (scope)
  theory/ED_SC_3_6_L_Larger_Driver.md        (driver spec)

Tests GR-SC 1.7 half-rise compression prediction
`r_½^filt / r_½^unfilt = 0.80 ± 0.05` at the **canonical filter**
`(α_filt, N_req) = (0.25, 4)` on a larger lattice where motif-mask
sparsity no longer blocks correlation measurement.

Primary: L = 128 (4× 64² area; motif count ≈ 8.4/snap × 400 snaps = 3,360).
Secondary: L = 256 (16× 64² area; promoted only if L=128 Inconclusive
            per scoping §6).

Three channels:
  A — pair-binned F4 (canonical r-grid Δr=0.5, Pearson + Spearman,
      4000-pair bootstrap).
  B — FFT motif-mask-weighted field autocorrelation (φ_B = p · M),
      full-shell radial average, 4000-seed bootstrap.
  C — FFT bulk-field autocorrelation (φ_C = p), full-shell radial
      average, 4000-seed bootstrap, self-calibration reference.

Primary ratio (same estimator numerator + denominator):
  ratio_primary = r_half_B_FFT / r_half_C_FFT
Diagnostic ratio (Channel A, canonical ED-SC 3.3 chain):
  ratio_A = r_half_A_pair_binned / ξ_canonical

Simulator of record:
  r2_grf_falsifier_tests.py + ED_Update_Rule.ed_step_mobility

Seeds: {11, 22, 33, 44, 55, 66, 77, 88, 99, 111}
Canonical filter: α_filt = 0.25, N_req = 4
Canonical hinge: L_ray = 1.08 · ξ_measured per seed

CLI:
  python ed_sc_3_6_l_larger.py          # L = 128 (default)
  python ed_sc_3_6_l_larger.py --L 256  # L = 256

Writes:
  outputs/ed_sc_3_6_l_larger_L{L}/correlation_twopoint_table.csv
  outputs/ed_sc_3_6_l_larger_L{L}/correlation_twopoint_per_seed.csv
  outputs/ed_sc_3_6_l_larger_L{L}/xi_field_profile.csv
  outputs/ed_sc_3_6_l_larger_L{L}/xi_field_per_seed.csv
  outputs/ed_sc_3_6_l_larger_L{L}/summary.json
  outputs/ed_sc_3_6_l_larger_L{L}/stdout.json (printed to stdout)

No simulator constants are mutated except `fr.SIZE` (by design).
Deterministic given seeds.
"""
import argparse
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
# CLI: lattice size selection
# ---------------------------------------------------------------------------
_parser = argparse.ArgumentParser(description="ED-SC 3.6 L-larger driver")
_parser.add_argument("--L", type=int, default=128,
                     help="Lattice size (128 primary, 256 secondary)")
_args = _parser.parse_args()
L_ACTIVE = int(_args.L)

# Critical override: set fr.SIZE BEFORE any function reads it
fr.SIZE = L_ACTIVE

# ---------------------------------------------------------------------------
# Canonical constants (inherited from F4 canonical + ED-SC 3.5)
# ---------------------------------------------------------------------------
XI_CANONICAL = 1.7575325729470939
XI_BURN_IN = 100
XI_SNAP_EVERY = 10

ALPHA_FILT = 0.25
N_REQ = 4  # CANONICAL filter (not relaxed)
DIMLESS_HINGE = 1.08
DIAG_COS = 0.707

WINDOW_A = (2.50, 2.80)
WINDOW_B = (3.50, 3.90)

XI_TARGET = 1.7575
SEEDS = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]

CALIBRATION_W_GRID = [0.05, 0.08, 0.10, 0.13, 0.16, 0.20, 0.25, 0.30, 0.35]
CALIBRATION_TOL = 0.01

# Channel A (pair-binned F4) — canonical r-grid
R_GRID = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
DR_BIN = 0.5
R_GRID_MIN_EDGE = R_GRID[0] - DR_BIN / 2   # 0.25
R_GRID_MAX_EDGE = R_GRID[-1] + DR_BIN / 2  # 5.25

# Admissibility thresholds
MIN_PAIRS_ENSEMBLE = 20
MIN_PAIRS_PER_SEED = 10
PRIMARY_GATE_CHANNEL_A = 8  # ≥ 8 of 10 bins admissible

# Channel B primary gate (absolute motif count; scales as L²)
PRIMARY_GATE_CHANNEL_B_MIN_MOTIFS = int(800 * (L_ACTIVE / 64) ** 2)
#   L=128 → 3200; L=256 → 12800 (matches scoping §5.2)

# Channel C self-calibration guardrail (on xi_halfdecay ensemble, per
# driver §5.1 — within-arc-one-estimator rule from ED-SC 3.5 §2.4)
SELF_CAL_TOL = 0.10

# Bootstrap config
BOOTSTRAP_B = 4000
BOOTSTRAP_RNG_SEED = 299  # distinct from F4 (99) and ED-SC 3.5 (199)

# Verdict thresholds (tenth-pass GR-SC 1.7 prediction: 0.80 ± 0.05)
VERDICT_CONFIRMED_LO = 0.75
VERDICT_CONFIRMED_HI = 0.85
VERDICT_REFUTED_LO = 0.70
VERDICT_REFUTED_HI = 0.90

OUT_DIR = os.path.join(HERE, "..", "..", "outputs",
                       f"ed_sc_3_6_l_larger_L{L_ACTIVE}")


# ---------------------------------------------------------------------------
# ξ half-decay (integer-binned; canonical ED-SC 3.3 definition)
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
# Evolution + calibration (inherited verbatim)
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
# Motif extraction (both positions for Channel A AND 0/1 mask for Channel B)
# ---------------------------------------------------------------------------
def extract_motifs_and_mask(snapshot, L_ray):
    """Single-pass: returns (positions_list, mask_2d). Shares the
    saddle-finding + motif-pass work between Channel A and Channel B."""
    E = fr.smooth_field(snapshot)
    p_hat = float(snapshot.mean())
    p_std = float(snapshot.std())
    sads = fr.find_morse_saddles(E)
    positions = []
    mask = np.zeros_like(snapshot, dtype=float)
    for s in sads:
        if not fr.motif_pass(s, E, p_hat, p_std,
                             ALPHA_FILT, L_ray, N_REQ):
            continue
        positions.append({
            "i": int(s["i"]),
            "j": int(s["j"]),
            "rho": float(s["ratio"]),
        })
        mask[int(s["i"]), int(s["j"])] = 1.0
    return positions, mask


# ---------------------------------------------------------------------------
# Minimum-image distance with explicit L argument
# ---------------------------------------------------------------------------
def min_image_distance(p1, p2, L):
    di = abs(p1[0] - p2[0])
    dj = abs(p1[1] - p2[1])
    di = min(di, L - di)
    dj = min(dj, L - dj)
    return math.sqrt(di * di + dj * dj)


def r_bin_assign(r):
    if r < R_GRID_MIN_EDGE or r >= R_GRID_MAX_EDGE:
        return None
    k = int(round((r - R_GRID[0]) / DR_BIN))
    if 0 <= k < len(R_GRID):
        r_k = R_GRID[k]
        if r_k - DR_BIN / 2 <= r < r_k + DR_BIN / 2:
            return k
    return None


# ---------------------------------------------------------------------------
# FFT radial-shell autocorrelation core (built for L_ACTIVE)
# ---------------------------------------------------------------------------
def _build_shell_index(N):
    cy, cx = N // 2, N // 2
    y_idx, x_idx = np.indices((N, N))
    r_squared = (y_idx - cy) ** 2 + (x_idx - cx) ** 2
    unique_r2 = np.unique(r_squared)
    shells = np.sqrt(unique_r2.astype(float))
    keep = shells <= (N // 2)
    unique_r2 = unique_r2[keep]
    shells = shells[keep]
    shell_masks = [(r_squared == r2) for r2 in unique_r2]
    n_sites_shell = np.array([int(m.sum()) for m in shell_masks])
    return shells, shell_masks, n_sites_shell


_SHELLS, _SHELL_MASKS, _N_SITES_SHELL = _build_shell_index(fr.SIZE)
N_SHELLS = len(_SHELLS)


def fft_autocorr(field):
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
# Per-seed execution (shared motif extraction + FFT per snapshot)
# ---------------------------------------------------------------------------
def run_seed(seed):
    t_seed = time.time()
    print(f"Seed {seed} — calibration + evolution (L={L_ACTIVE})...",
          file=sys.stderr)
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
    xi_A_snaps = np.empty((len(snapshots), N_SHELLS), dtype=float)
    xi_B_snaps = np.empty((len(snapshots), N_SHELLS), dtype=float)
    mask_densities = np.empty(len(snapshots), dtype=float)
    empty_masks = 0
    total_motifs = 0
    for s_idx, p in enumerate(snapshots):
        positions, mask = extract_motifs_and_mask(p, L_ray)
        motifs_per_snap.append(positions)
        total_motifs += len(positions)
        mask_densities[s_idx] = float(mask.mean())
        if mask.sum() == 0:
            empty_masks += 1
        xi_A_snaps[s_idx] = fft_autocorr(p)        # Channel C (bulk)
        xi_B_snaps[s_idx] = fft_autocorr(p * mask)  # Channel B (masked)

    xi_A_seed = xi_A_snaps.mean(axis=0)
    xi_B_seed = xi_B_snaps.mean(axis=0)
    mean_mask_density = float(mask_densities.mean())

    print(f"  seed={seed}  ξ_meas={xi_measured:.4f} "
          f"(miss {miss*100:.2f}%, refined={refinement_used})  "
          f"L_ray={L_ray:.4f}  r_diag={r_diag}  "
          f"N_motifs={total_motifs}  ⟨ρ_M⟩={mean_mask_density:.5f}  "
          f"empty={empty_masks}/40  "
          f"σ_0²_C={xi_A_seed[0]:.6f}  σ_0²_B={xi_B_seed[0]:.4g}  "
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
        "N_motifs_total": total_motifs,
        "motifs_per_snap": motifs_per_snap,
        "xi_A_seed": xi_A_seed,  # bulk (Channel C)
        "xi_B_seed": xi_B_seed,  # masked (Channel B)
        "mean_mask_density": mean_mask_density,
        "empty_masks_count": empty_masks,
        "calibration_prepass": calibration,
        "wall_seconds": time.time() - t_seed,
    }


# ---------------------------------------------------------------------------
# Channel A — pair enumeration + estimators + bootstrap
# ---------------------------------------------------------------------------
def accumulate_pairs_per_seed(motifs_per_snap, L):
    pair_pool = {k: [] for k in range(len(R_GRID))}
    for snap_motifs in motifs_per_snap:
        n = len(snap_motifs)
        for a in range(n):
            m_a = snap_motifs[a]
            for b in range(a + 1, n):
                m_b = snap_motifs[b]
                r = min_image_distance(
                    (m_a["i"], m_a["j"]), (m_b["i"], m_b["j"]), L=L)
                k = r_bin_assign(r)
                if k is None:
                    continue
                pair_pool[k].append((m_a["rho"], m_b["rho"]))
    return pair_pool


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
        return {"C": None, "C_CI_lo": None, "C_CI_hi": None,
                "low_N": True, "bootstrap_values": []}
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
# Half-rise interpolation (shared across channels)
# ---------------------------------------------------------------------------
def linear_interp_halfrise(r_grid, C_values, target=1.0):
    for k in range(len(r_grid) - 1):
        C_k = C_values[k]
        C_k1 = C_values[k + 1]
        if C_k is None or C_k1 is None:
            continue
        if not np.isfinite(C_k) or not np.isfinite(C_k1):
            continue
        if (C_k < target) == (C_k1 < target):
            continue
        denom = C_k1 - C_k
        if abs(denom) < 1e-12:
            continue
        return r_grid[k] + (r_grid[k + 1] - r_grid[k]) * (
            target - C_k) / denom
    return None


def all_crossings(r_grid, C_values, target=1.0):
    crossings = []
    for k in range(len(r_grid) - 1):
        c_k, c_k1 = C_values[k], C_values[k + 1]
        if not (np.isfinite(c_k) and np.isfinite(c_k1)):
            continue
        if (c_k < target) == (c_k1 < target):
            continue
        denom = c_k1 - c_k
        if abs(denom) < 1e-12:
            continue
        crossings.append(
            r_grid[k] + (r_grid[k + 1] - r_grid[k]) * (target - c_k) / denom)
    return crossings


def is_non_monotone(C_values, noise_tol=0.05):
    if C_values is None:
        return False
    finite = np.array([c for c in C_values
                       if c is not None and np.isfinite(c)])
    if len(finite) < 3:
        return False
    diffs = np.diff(finite)
    return bool(np.any(diffs < -noise_tol))


def C_from_xi(xi_curve):
    if xi_curve[0] <= 0 or not np.isfinite(xi_curve[0]):
        return None
    return 2.0 * (1.0 - xi_curve / xi_curve[0])


def bootstrap_half_rise_pairs(bootstrap_C_arrays, r_grid):
    """Channel A pair-level bootstrap half-rise. Returns
    (16, 84, samples) or None."""
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
# Per-channel verdict (four-way, inherited from F4)
# ---------------------------------------------------------------------------
def compute_verdict(ratio_central, ratio_bootstrap_band, label="channel"):
    if ratio_central is None:
        return ("Inconclusive",
                f"{label}: no C=1 crossing in measured range")
    if VERDICT_CONFIRMED_LO <= ratio_central <= VERDICT_CONFIRMED_HI:
        if ratio_bootstrap_band is not None:
            lo, hi = ratio_bootstrap_band[:2]
            if (lo is not None and hi is not None
                    and (lo < VERDICT_CONFIRMED_LO
                         or hi > VERDICT_CONFIRMED_HI)):
                return ("Confirmed-marginal",
                        f"{label}: ratio={ratio_central:.3f} in [0.75, "
                        f"0.85] but bootstrap 16-84=[{lo:.3f}, {hi:.3f}] "
                        "straddles a threshold")
        return ("Confirmed",
                f"{label}: ratio={ratio_central:.3f} ∈ [0.75, 0.85] "
                "(tenth-pass 0.80 ± 0.05 band)")
    if ratio_central < VERDICT_REFUTED_LO or ratio_central > VERDICT_REFUTED_HI:
        return ("Refuted",
                f"{label}: ratio={ratio_central:.3f} ∉ [0.70, 0.90] "
                "(outside double envelope of tenth-pass prediction)")
    return ("Confirmed-marginal",
            f"{label}: ratio={ratio_central:.3f} in marginal band "
            "[0.70, 0.75) ∪ (0.85, 0.90]")


# ---------------------------------------------------------------------------
# Combined verdict (scoping §6 reconciliation matrix)
# ---------------------------------------------------------------------------
def combine_verdicts(verdict_A, reason_A, verdict_B, reason_B,
                     channel_A_gate_ok, channel_B_gate_ok,
                     self_cal_ok, self_cal_miss,
                     ratio_A, ratio_B, L_active):
    if not self_cal_ok:
        return ("Inconclusive",
                f"Self-calibration guardrail failed: "
                f"xi_halfdecay_ensemble miss = {self_cal_miss*100:.1f}% "
                f"> {SELF_CAL_TOL*100:.0f}% tolerance",
                {}, False)
    if not channel_A_gate_ok and not channel_B_gate_ok:
        promote = (L_active == 128)
        return ("Inconclusive",
                "Both Channel A and Channel B primary gates failed",
                {"channel_A_gate_ok": channel_A_gate_ok,
                 "channel_B_gate_ok": channel_B_gate_ok},
                promote)
    if channel_A_gate_ok and not channel_B_gate_ok:
        return (verdict_A,
                f"Channel B gate failed (motif-count < {PRIMARY_GATE_CHANNEL_B_MIN_MOTIFS}); "
                f"Channel A (pair-binned) verdict reported. {reason_A}",
                {"single_channel": "A"},
                False)
    if channel_B_gate_ok and not channel_A_gate_ok:
        return (verdict_B,
                f"Channel A gate failed (admissible bins < "
                f"{PRIMARY_GATE_CHANNEL_A}); Channel B (FFT) verdict "
                f"reported. {reason_B}",
                {"single_channel": "B"},
                False)
    # Both gates passed — apply reconciliation matrix
    both_confirmed = (verdict_A == "Confirmed" and verdict_B == "Confirmed")
    both_refuted = (verdict_A == "Refuted" and verdict_B == "Refuted")
    if both_confirmed:
        return ("Confirmed",
                f"Two-channel Confirmed: Channel A ratio={ratio_A:.3f}, "
                f"Channel B ratio={ratio_B:.3f}; both in [0.75, 0.85]",
                {"reconciliation_case": "row_1_both_confirmed"},
                False)
    if both_refuted:
        return ("Refuted",
                f"Two-channel Refuted: Channel A ratio={ratio_A:.3f}, "
                f"Channel B ratio={ratio_B:.3f}; both outside [0.70, 0.90]",
                {"reconciliation_case": "row_4_both_refuted"},
                False)
    # Mixed Confirmed / Refuted — channel-dependent
    if ((verdict_A == "Refuted" and verdict_B in
         {"Confirmed", "Confirmed-marginal"})
            or (verdict_B == "Refuted" and verdict_A in
                {"Confirmed", "Confirmed-marginal"})):
        return ("Inconclusive",
                f"Channel-dependent result: Channel A ({verdict_A}, "
                f"ratio={ratio_A:.3f}) vs Channel B ({verdict_B}, "
                f"ratio={ratio_B:.3f}). Escalates to 18th-pass scoping "
                "per scoping §6 matrix.",
                {"reconciliation_case": "channel_dependent",
                 "escalation_required": True},
                False)
    if verdict_A == "Inconclusive" and verdict_B != "Inconclusive":
        return (verdict_B,
                f"Channel A Inconclusive; Channel B verdict reported. "
                f"{reason_B}",
                {"single_channel": "B_with_A_inconclusive"},
                False)
    if verdict_B == "Inconclusive" and verdict_A != "Inconclusive":
        return (verdict_A,
                f"Channel B Inconclusive; Channel A verdict reported. "
                f"{reason_A}",
                {"single_channel": "A_with_B_inconclusive"},
                False)
    if verdict_A == "Inconclusive" and verdict_B == "Inconclusive":
        promote = (L_active == 128)
        return ("Inconclusive",
                "Both channels Inconclusive (no C=1 crossing in either)",
                {"reconciliation_case": "row_6_both_inconclusive"},
                promote)
    # Mixed Confirmed / Confirmed-marginal or similar non-contradictory
    if (verdict_A in {"Confirmed", "Confirmed-marginal"}
            and verdict_B in {"Confirmed", "Confirmed-marginal"}):
        return ("Confirmed-marginal",
                f"Channel A ({verdict_A}, ratio={ratio_A:.3f}) and "
                f"Channel B ({verdict_B}, ratio={ratio_B:.3f}) both "
                "Confirmed or marginal",
                {"reconciliation_case": "both_confirmed_or_marginal"},
                False)
    return ("Inconclusive",
            f"Unhandled: A={verdict_A}, B={verdict_B}",
            {"reconciliation_case": "unhandled"},
            False)


# ---------------------------------------------------------------------------
# Master driver
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    t_master = time.time()
    assert_no_resonance_plan()

    print(f"ED-SC 3.6 L-larger three-channel driver: L={L_ACTIVE}, "
          f"ξ_target={XI_TARGET}, {len(SEEDS)} seeds × 40 snaps, "
          f"N_SHELLS={N_SHELLS}, Channel B min motifs = "
          f"{PRIMARY_GATE_CHANNEL_B_MIN_MOTIFS}", file=sys.stderr)

    # 1. Per-seed execution (shared motif extraction + FFT)
    per_seed_results = []
    for seed in SEEDS:
        per_seed_results.append(run_seed(seed))

    # 2. Ensemble pool statistics (for Channel A Pearson estimator)
    all_rho = []
    for r in per_seed_results:
        for snap in r["motifs_per_snap"]:
            for m in snap:
                all_rho.append(m["rho"])
    ensemble_total_motifs = len(all_rho)
    rho_bar = float(np.mean(all_rho)) if all_rho else 0.0
    var_rho = float(np.var(all_rho, ddof=1)) if len(all_rho) >= 2 else 0.0
    print(f"\nEnsemble pool: N_motifs = {ensemble_total_motifs}, "
          f"ρ̄ = {rho_bar:.6f}, σ²_ρ = {var_rho:.6f}",
          file=sys.stderr)

    # 3. Channel A — per-seed pair pools, ensemble pool, bootstrap
    pair_pool_per_seed = {}
    for r in per_seed_results:
        pair_pool_per_seed[r["seed"]] = accumulate_pairs_per_seed(
            r["motifs_per_snap"], L=L_ACTIVE)
    ensemble_pool_A = {k: [] for k in range(len(R_GRID))}
    for seed_pool in pair_pool_per_seed.values():
        for k, pairs in seed_pool.items():
            ensemble_pool_A[k].extend(pairs)
    N_pairs_total_A = sum(len(v) for v in ensemble_pool_A.values())
    print(f"Channel A: total pairs binned = {N_pairs_total_A} across "
          f"{len(R_GRID)} r-bins", file=sys.stderr)

    r_bins_data = []
    bootstrap_arrays_A = []
    C_A_central = []
    for k in range(len(R_GRID)):
        pool = ensemble_pool_A[k]
        bs = bootstrap_ensemble_C(pool, rho_bar, var_rho)
        C_rank = spearman_C(pool)
        if bs["C"] is not None and C_rank is not None:
            model_band_rel = abs(bs["C"] - C_rank) / max(abs(bs["C"]), 1e-12)
        else:
            model_band_rel = None
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
        bootstrap_arrays_A.append(bs["bootstrap_values"])
        C_A_central.append(bs["C"])

    n_admissible_A = sum(1 for b in r_bins_data
                         if not b["low_N_ensemble"])
    channel_A_gate_ok = n_admissible_A >= PRIMARY_GATE_CHANNEL_A

    # Channel A half-rise + ratio_A
    r_half_A_filt = linear_interp_halfrise(R_GRID, C_A_central)
    r_half_A_unfilt = XI_CANONICAL
    ratio_A = (r_half_A_filt / r_half_A_unfilt
               if r_half_A_filt is not None else None)
    bs_half_A = bootstrap_half_rise_pairs(bootstrap_arrays_A, R_GRID)
    if bs_half_A is not None:
        r_half_A_lo, r_half_A_hi, r_half_A_samples = bs_half_A
        ratio_A_lo = (r_half_A_lo / r_half_A_unfilt
                      if r_half_A_lo is not None else None)
        ratio_A_hi = (r_half_A_hi / r_half_A_unfilt
                      if r_half_A_hi is not None else None)
    else:
        r_half_A_lo = r_half_A_hi = None
        ratio_A_lo = ratio_A_hi = None
        r_half_A_samples = []
    ratio_A_band = ((ratio_A_lo, ratio_A_hi)
                    if ratio_A_lo is not None else None)
    verdict_A, reason_A = compute_verdict(ratio_A, ratio_A_band, "Channel A")

    print(f"\nChannel A: n_admissible = {n_admissible_A}/10 "
          f"(gate ≥ {PRIMARY_GATE_CHANNEL_A}: {channel_A_gate_ok}) | "
          f"r_half_filt = {r_half_A_filt} | ratio_A = {ratio_A} | "
          f"verdict = {verdict_A}", file=sys.stderr)

    # 4. Channels B + C — ensemble FFT curves
    per_seed_xi_A = np.array([r["xi_A_seed"] for r in per_seed_results])
    per_seed_xi_B = np.array([r["xi_B_seed"] for r in per_seed_results])
    xi_A_central = per_seed_xi_A.mean(axis=0)  # Channel C (bulk)
    xi_B_central = per_seed_xi_B.mean(axis=0)  # Channel B (masked)

    C_A_fft_central = C_from_xi(xi_A_central)  # Channel C
    C_B_fft_central = C_from_xi(xi_B_central)  # Channel B

    r_half_C_FFT = (linear_interp_halfrise(_SHELLS, C_A_fft_central)
                    if C_A_fft_central is not None else None)
    r_half_B_FFT = (linear_interp_halfrise(_SHELLS, C_B_fft_central)
                    if C_B_fft_central is not None else None)
    all_cross_C = (all_crossings(_SHELLS, C_A_fft_central)
                   if C_A_fft_central is not None else [])
    all_cross_B = (all_crossings(_SHELLS, C_B_fft_central)
                   if C_B_fft_central is not None else [])
    multi_crossing_C = len(all_cross_C) > 1
    multi_crossing_B = len(all_cross_B) > 1
    non_monotone_C = is_non_monotone(C_A_fft_central)
    non_monotone_B = is_non_monotone(C_B_fft_central)

    # 5. Paired bootstrap over seeds (Channels B and C simultaneously)
    n_seeds = len(SEEDS)
    rng = np.random.default_rng(BOOTSTRAP_RNG_SEED)
    xi_A_boot = np.empty((BOOTSTRAP_B, N_SHELLS), dtype=float)
    xi_B_boot = np.empty((BOOTSTRAP_B, N_SHELLS), dtype=float)
    bootstrap_r_half_C = []
    bootstrap_r_half_B = []
    bootstrap_ratios_primary = []
    for b in range(BOOTSTRAP_B):
        idx = rng.integers(0, n_seeds, size=n_seeds)
        A_b = per_seed_xi_A[idx].mean(axis=0)
        B_b = per_seed_xi_B[idx].mean(axis=0)
        xi_A_boot[b] = A_b
        xi_B_boot[b] = B_b
        C_A_b = C_from_xi(A_b)
        C_B_b = C_from_xi(B_b)
        if C_A_b is None or C_B_b is None:
            continue
        r_C_b = linear_interp_halfrise(_SHELLS, C_A_b)
        r_B_b = linear_interp_halfrise(_SHELLS, C_B_b)
        if r_C_b is not None:
            bootstrap_r_half_C.append(r_C_b)
        if r_B_b is not None:
            bootstrap_r_half_B.append(r_B_b)
        if (r_C_b is not None and r_B_b is not None and r_C_b > 0):
            bootstrap_ratios_primary.append(r_B_b / r_C_b)

    # Per-shell bootstrap bands for ξ and C
    xi_A_lo_shell = np.quantile(xi_A_boot, 0.16, axis=0)
    xi_A_hi_shell = np.quantile(xi_A_boot, 0.84, axis=0)
    xi_B_lo_shell = np.quantile(xi_B_boot, 0.16, axis=0)
    xi_B_hi_shell = np.quantile(xi_B_boot, 0.84, axis=0)
    C_A_fft_lo = np.quantile(2.0 * (1.0 - xi_A_boot
                                    / xi_A_boot[:, 0:1]), 0.16, axis=0)
    C_A_fft_hi = np.quantile(2.0 * (1.0 - xi_A_boot
                                    / xi_A_boot[:, 0:1]), 0.84, axis=0)
    # For Channel B, guard against σ_0²_B=0 in any resample:
    safe_denom = np.where(xi_B_boot[:, 0:1] > 0,
                           xi_B_boot[:, 0:1], np.nan)
    C_B_fft_all = 2.0 * (1.0 - xi_B_boot / safe_denom)
    C_B_fft_lo = np.nanquantile(C_B_fft_all, 0.16, axis=0)
    C_B_fft_hi = np.nanquantile(C_B_fft_all, 0.84, axis=0)

    if bootstrap_r_half_C:
        r_half_C_lo = float(np.quantile(bootstrap_r_half_C, 0.16))
        r_half_C_hi = float(np.quantile(bootstrap_r_half_C, 0.84))
    else:
        r_half_C_lo = r_half_C_hi = None
    if bootstrap_r_half_B:
        r_half_B_lo = float(np.quantile(bootstrap_r_half_B, 0.16))
        r_half_B_hi = float(np.quantile(bootstrap_r_half_B, 0.84))
    else:
        r_half_B_lo = r_half_B_hi = None
    if bootstrap_ratios_primary:
        ratio_primary_lo = float(np.quantile(bootstrap_ratios_primary, 0.16))
        ratio_primary_hi = float(np.quantile(bootstrap_ratios_primary, 0.84))
    else:
        ratio_primary_lo = ratio_primary_hi = None

    ratio_primary = (r_half_B_FFT / r_half_C_FFT
                     if (r_half_B_FFT is not None
                         and r_half_C_FFT is not None
                         and r_half_C_FFT > 0)
                     else None)
    ratio_primary_band = ((ratio_primary_lo, ratio_primary_hi)
                          if ratio_primary_lo is not None else None)
    verdict_B, reason_B = compute_verdict(ratio_primary, ratio_primary_band,
                                          "Channel B (primary)")

    print(f"Channel C (bulk FFT): r_half = {r_half_C_FFT}", file=sys.stderr)
    print(f"Channel B (masked FFT): r_half = {r_half_B_FFT}, "
          f"ratio_primary = {ratio_primary} | verdict = {verdict_B}",
          file=sys.stderr)

    # 6. Channel B primary gate (absolute motif count)
    channel_B_gate_ok = (ensemble_total_motifs
                         >= PRIMARY_GATE_CHANNEL_B_MIN_MOTIFS)
    print(f"Channel B gate: {ensemble_total_motifs} motifs vs "
          f"{PRIMARY_GATE_CHANNEL_B_MIN_MOTIFS} threshold → "
          f"{channel_B_gate_ok}", file=sys.stderr)

    # 7. Channel C self-calibration guardrail (on xi_halfdecay ensemble)
    xi_halfdecay_ensemble = float(np.mean(
        [r["xi_measured"] for r in per_seed_results]))
    xi_halfdecay_ensemble_std = float(np.std(
        [r["xi_measured"] for r in per_seed_results], ddof=1))
    self_cal_miss = abs(xi_halfdecay_ensemble - XI_TARGET) / XI_TARGET
    self_cal_ok = self_cal_miss <= SELF_CAL_TOL
    print(f"Self-cal: xi_halfdecay ensemble = {xi_halfdecay_ensemble:.4f} "
          f"vs ξ_target = {XI_TARGET} → miss = {self_cal_miss*100:.2f}%, "
          f"passed = {self_cal_ok}", file=sys.stderr)

    # 8. Channel independence flag
    channel_independence_flag = False
    if ratio_primary is not None and ratio_A is not None:
        channel_independence_flag = abs(ratio_primary - ratio_A) > 0.15

    # 9. Combined verdict
    combined_verdict, combined_reason, reconciliation, promote_L256 = \
        combine_verdicts(verdict_A, reason_A, verdict_B, reason_B,
                         channel_A_gate_ok, channel_B_gate_ok,
                         self_cal_ok, self_cal_miss,
                         ratio_A, ratio_primary, L_ACTIVE)
    print(f"\nCombined verdict: {combined_verdict} — {combined_reason}",
          file=sys.stderr)
    if promote_L256:
        print("→ PROMOTE TO L = 256 recommended", file=sys.stderr)

    # 10. Diagnostics
    mean_mask_density_ensemble = float(np.mean(
        [r["mean_mask_density"] for r in per_seed_results]))
    C_A_fft_at_r_min = (float(C_A_fft_central[1])
                        if (C_A_fft_central is not None
                            and len(C_A_fft_central) > 1) else None)
    C_A_fft_at_r_max = (float(C_A_fft_central[-1])
                        if C_A_fft_central is not None else None)

    # 11. Write Channel A CSV (pair-binned table)
    csv_path_A = os.path.join(OUT_DIR, "correlation_twopoint_table.csv")
    with open(csv_path_A, "w", newline="") as f:
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

    # 12. Write Channel A per-seed CSV
    per_seed_csv_A = os.path.join(OUT_DIR,
                                  "correlation_twopoint_per_seed.csv")
    with open(per_seed_csv_A, "w", newline="") as f:
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

    # 13. Write FFT profile CSV (Channels C + B)
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
                float(xi_A_central[k]),
                float(xi_A_lo_shell[k]), float(xi_A_hi_shell[k]),
                (None if C_A_fft_central is None
                 else float(C_A_fft_central[k])),
                float(C_A_fft_lo[k]), float(C_A_fft_hi[k]),
                float(xi_B_central[k]),
                float(xi_B_lo_shell[k]), float(xi_B_hi_shell[k]),
                (None if C_B_fft_central is None
                 else float(C_B_fft_central[k])),
                float(C_B_fft_lo[k]), float(C_B_fft_hi[k]),
            ])

    # 14. Write FFT per-seed CSV
    per_seed_csv_fft = os.path.join(OUT_DIR, "xi_field_per_seed.csv")
    with open(per_seed_csv_fft, "w", newline="") as f:
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
                    r["xi_measured"], r["L_ray"],
                    r["mean_mask_density"],
                ])

    # 15. Write summary JSON
    out = {
        "method": ("ED-SC 3.6 L-larger three-channel driver: "
                   "Channel A pair-binned F4 (canonical filter); "
                   "Channel B FFT mask-weighted; "
                   "Channel C FFT bulk reference. "
                   "Primary ratio = r_half_B_FFT / r_half_C_FFT."),
        "simulator_of_record":
            "r2_grf_falsifier_tests.py + ED_Update_Rule.ed_step_mobility",
        "L_active": L_ACTIVE,
        "L_primary": 128,
        "L_secondary_planned": 256,
        "xi_canonical_lattice_units": XI_CANONICAL,
        "xi_target": XI_TARGET,
        "alpha_filt": ALPHA_FILT,
        "N_req": N_REQ,
        "dimensionless_hinge": DIMLESS_HINGE,
        "seeds": SEEDS,
        "r_grid_pair_binned": R_GRID,
        "dr_bin_pair_binned": DR_BIN,
        "n_shells_fft": N_SHELLS,
        "canonical_params": {
            "alpha": fr.ALPHA0, "gamma": fr.GAMMA,
            "noise_sigma": fr.NOISE0,
            "mobility_exp": fr.MOBILITY_EXP,
            "steps": fr.STEPS, "size": fr.SIZE, "dt": fr.DT,
        },
        "resonance_windows_excluded": {
            "A": list(WINDOW_A), "B": list(WINDOW_B)},
        "per_seed": [
            {k: (v if k not in ("xi_A_seed", "xi_B_seed",
                                "motifs_per_snap", "calibration_prepass")
                 else ([float(x) for x in v]
                       if k in ("xi_A_seed", "xi_B_seed") else None))
             for k, v in r.items()
             if k not in ("motifs_per_snap", "calibration_prepass")}
            for r in per_seed_results
        ],
        "ensemble_pool": {
            "rho_bar": rho_bar,
            "sigma2_rho": var_rho,
            "N_motifs_total": ensemble_total_motifs,
        },
        "channel_A_pair_binned": {
            "r_bins": [
                {k: v for k, v in b.items()
                 if k not in ("per_seed_C", "per_seed_N")}
                | {"per_seed_C": b["per_seed_C"],
                   "per_seed_N": b["per_seed_N"]}
                for b in r_bins_data
            ],
            "n_admissible_bins": n_admissible_A,
            "primary_gate_threshold": PRIMARY_GATE_CHANNEL_A,
            "primary_gate_passed": channel_A_gate_ok,
            "r_half_filt_central": r_half_A_filt,
            "r_half_filt_bootstrap_16_84": (
                [r_half_A_lo, r_half_A_hi]
                if r_half_A_lo is not None else None),
            "r_half_unfilt_reference": XI_CANONICAL,
            "ratio_A_central": ratio_A,
            "ratio_A_bootstrap_16_84": (
                [ratio_A_lo, ratio_A_hi]
                if ratio_A_lo is not None else None),
            "verdict_A": verdict_A,
            "verdict_A_reason": reason_A,
        },
        "channel_B_fft_masked": {
            "shells": [float(x) for x in _SHELLS],
            "xi_phi_central": [float(x) for x in xi_B_central],
            "C_central": (None if C_B_fft_central is None
                          else [float(x) for x in C_B_fft_central]),
            "C_CI_lo": [float(x) for x in C_B_fft_lo],
            "C_CI_hi": [float(x) for x in C_B_fft_hi],
            "r_half_central": r_half_B_FFT,
            "r_half_bootstrap_16_84": (
                [r_half_B_lo, r_half_B_hi]
                if r_half_B_lo is not None else None),
            "ensemble_total_motifs": ensemble_total_motifs,
            "primary_gate_threshold": PRIMARY_GATE_CHANNEL_B_MIN_MOTIFS,
            "primary_gate_passed": channel_B_gate_ok,
            "mean_mask_density_ensemble": mean_mask_density_ensemble,
            "multi_crossing_flag": multi_crossing_B,
            "non_monotone_flag": non_monotone_B,
            "all_crossings": all_cross_B,
        },
        "channel_C_fft_bulk_reference": {
            "shells": [float(x) for x in _SHELLS],
            "xi_phi_central": [float(x) for x in xi_A_central],
            "C_central": (None if C_A_fft_central is None
                          else [float(x) for x in C_A_fft_central]),
            "C_CI_lo": [float(x) for x in C_A_fft_lo],
            "C_CI_hi": [float(x) for x in C_A_fft_hi],
            "r_half_FFT_central": r_half_C_FFT,
            "r_half_FFT_bootstrap_16_84": (
                [r_half_C_lo, r_half_C_hi]
                if r_half_C_lo is not None else None),
            "xi_halfdecay_ensemble_mean": xi_halfdecay_ensemble,
            "xi_halfdecay_ensemble_std": xi_halfdecay_ensemble_std,
            "multi_crossing_flag": multi_crossing_C,
            "non_monotone_flag": non_monotone_C,
            "all_crossings": all_cross_C,
        },
        "self_calibration_check": {
            "xi_halfdecay_ensemble": xi_halfdecay_ensemble,
            "xi_target_reference": XI_TARGET,
            "miss_fraction": self_cal_miss,
            "tolerance": SELF_CAL_TOL,
            "passed": bool(self_cal_ok),
        },
        "primary_ratio": {
            "ratio_central": ratio_primary,
            "ratio_bootstrap_16_84": (
                [ratio_primary_lo, ratio_primary_hi]
                if ratio_primary_lo is not None else None),
            "ratio_A_for_comparison": ratio_A,
            "channel_independence_flag": channel_independence_flag,
        },
        "combined_verdict": {
            "verdict": combined_verdict,
            "reason": combined_reason,
            "channel_A_verdict": verdict_A,
            "channel_B_verdict": verdict_B,
            "reconciliation": reconciliation,
            "promote_to_L256": promote_L256,
            "taxonomy": ("four-way per channel; combined via scoping §6 "
                         "reconciliation matrix"),
            "tenth_pass_prediction": "0.80 ± 0.05 (GR-SC 1.7)",
            "confirmed_threshold": [VERDICT_CONFIRMED_LO,
                                    VERDICT_CONFIRMED_HI],
            "refuted_threshold_low": VERDICT_REFUTED_LO,
            "refuted_threshold_high": VERDICT_REFUTED_HI,
        },
        "diagnostics": {
            "n_admissible_bins_channel_A": n_admissible_A,
            "ensemble_total_motifs_channel_B": ensemble_total_motifs,
            "mean_mask_density_channel_B": mean_mask_density_ensemble,
            "multi_crossing_flags": {
                "A": False, "B": multi_crossing_B, "C": multi_crossing_C,
            },
            "non_monotone_flags": {
                "A": False, "B": non_monotone_B, "C": non_monotone_C,
            },
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
            "n_valid_bootstrap": BOOTSTRAP_B,
            "bootstrap_valid_r_half_C": len(bootstrap_r_half_C),
            "bootstrap_valid_r_half_B": len(bootstrap_r_half_B),
            "bootstrap_valid_ratio_primary":
                len(bootstrap_ratios_primary),
            "channel_A_endpoint_C_at_r_min":
                (float(C_A_central[0])
                 if C_A_central and C_A_central[0] is not None
                 else None),
            "channel_A_endpoint_C_at_r_max":
                (float(C_A_central[-1])
                 if C_A_central and C_A_central[-1] is not None
                 else None),
            "channel_C_fft_at_r_1": C_A_fft_at_r_min,
            "channel_C_fft_at_r_max": C_A_fft_at_r_max,
        },
        "wall_seconds_total": time.time() - t_master,
    }

    json_path = os.path.join(OUT_DIR, "summary.json")
    with open(json_path, "w") as f:
        json.dump(out, f, indent=2)

    print(f"\nWrote Channel A table → {csv_path_A}", file=sys.stderr)
    print(f"Wrote Channel A per-seed → {per_seed_csv_A}", file=sys.stderr)
    print(f"Wrote FFT profile → {profile_path}", file=sys.stderr)
    print(f"Wrote FFT per-seed → {per_seed_csv_fft}", file=sys.stderr)
    print(f"Wrote summary → {json_path}", file=sys.stderr)

    # 16. Print stdout summary (to stdout; redirect to stdout.json)
    print(json.dumps({
        "L_active": L_ACTIVE,
        "N_seeds": len(SEEDS),
        "n_admissible_bins_A": n_admissible_A,
        "ensemble_total_motifs_B": ensemble_total_motifs,
        "channel_B_motif_threshold": PRIMARY_GATE_CHANNEL_B_MIN_MOTIFS,
        "r_half_A_pair_binned": r_half_A_filt,
        "r_half_B_FFT": r_half_B_FFT,
        "r_half_C_FFT": r_half_C_FFT,
        "xi_halfdecay_ensemble": xi_halfdecay_ensemble,
        "ratio_primary": ratio_primary,
        "ratio_primary_bootstrap_16_84": (
            [ratio_primary_lo, ratio_primary_hi]
            if ratio_primary_lo is not None else None),
        "ratio_A_diagnostic": ratio_A,
        "self_cal_passed": bool(self_cal_ok),
        "self_cal_miss_fraction": self_cal_miss,
        "channel_A_gate_passed": bool(channel_A_gate_ok),
        "channel_B_gate_passed": bool(channel_B_gate_ok),
        "channel_independence_flag": bool(channel_independence_flag),
        "verdict_A": verdict_A,
        "verdict_B_primary": verdict_B,
        "combined_verdict": combined_verdict,
        "combined_verdict_reason": combined_reason,
        "promote_to_L256": bool(promote_L256),
        "mean_mask_density_ensemble": mean_mask_density_ensemble,
        "multi_crossing": {
            "A": False, "B": multi_crossing_B, "C": multi_crossing_C,
        },
        "non_monotone": {
            "A": False, "B": non_monotone_B, "C": non_monotone_C,
        },
        "wall_seconds_total": out["wall_seconds_total"],
    }, indent=2))


if __name__ == "__main__":
    main()
