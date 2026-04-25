# ED-SC 3.5 FFT-Based Field Autocorrelation — Driver Specification

**Pass:** seventeenth (post-F4 checkpoint; ED-SC 3.5 arc driver memo)
**Date:** 2026-04-23
**Parent scoping memo:** `theory/ED_SC_3_5_FFT_XiField_Scoping.md`
**Parent driver templates:** `analysis/scripts/ed_sc_3_4_twopoint_correlation_relaxed.py` (for calibration + evolution + motif extraction), `analysis/scripts/ed_sc_3_1_xi_canonical.py` (for FFT autocorrelation machinery — `xi_halfdecay` pattern)
**This driver memo specifies:** `analysis/scripts/ed_sc_3_5_fft_xi_field.py` (forthcoming)

---

## 1. Purpose

Provide a complete, executable specification for the FFT-based
field-autocorrelation driver that implements the ED-SC 3.5 scoping
memo §3 measurement architecture. The output is a primary four-way
verdict on the GR-SC 1.7 half-rise compression prediction
`r_½^filt / r_½^unfilt = 0.80 ± 0.05`, operating on the bulk
continuous p-field rather than the motif-ratio pair pool.

**This memo is one-pass-implementation-sufficient:** any future
session should be able to write the driver script from this memo
alone without re-reading parent scoping or F4 drivers, given the
named simulator of record.

---

## 2. Inputs

### 2.1 Ensemble

```python
SEEDS = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]   # 10 seeds
N_SNAPSHOTS_PER_SEED = 40
XI_TARGET = 1.7575                                    # canonical ξ (lu)
XI_CANONICAL = 1.7575325729470939                     # full precision from outputs/ed_sc_3_1/xi_canonical.json
```

Inherited verbatim from F4-alt (same 10-seed ensemble so the FFT
output can be cross-referenced against F4-alt artefacts realisation-
for-realisation).

### 2.2 Evolution and calibration

```python
XI_BURN_IN = 100                      # snapshots begin at step 100
XI_SNAP_EVERY = 10                    # 40 snapshots × 10 steps = 400 steps post-burn-in

CALIBRATION_W_GRID = [0.05, 0.08, 0.10, 0.13, 0.16, 0.20, 0.25, 0.30, 0.35]
CALIBRATION_TOL = 0.01                # |miss| tolerance for one-pass refinement
```

Inherited verbatim from F4-alt. Each seed runs a 9-point IC-amplitude
calibration pre-pass, interpolates w → ξ_target, and applies one
refinement step if |ξ_measured − ξ_target| / ξ_target > 1 %.

### 2.3 Simulator of record

```python
import r2_grf_falsifier_tests as fr
from ED_Update_Rule import ed_step_mobility

# Canonical constants from fr:
#   fr.SIZE, fr.STEPS, fr.DT, fr.ALPHA0, fr.GAMMA,
#   fr.NOISE0, fr.MOBILITY_EXP, fr.BOUNDARY, fr.P_MIN, fr.P_MAX
```

Canonical parameters must be read from the simulator's module
globals; no module constants are mutated by this driver.

### 2.4 Motif-mask filter (for channel B)

```python
ALPHA_FILT = 0.25                     # canonical
N_REQ = 4                             # canonical (NOT relaxed)
DIMLESS_HINGE = 1.08                  # L_ray = 1.08 · ξ_measured
DIAG_COS = 0.707

WINDOW_A = (2.50, 2.80)               # L_ray resonance window 1
WINDOW_B = (3.50, 3.90)               # L_ray resonance window 2
```

**Important:** this driver uses the **canonical filter** for the
motif mask (not the F4-alt relaxed N_req = 2). The scoping memo §2
pins the primary channel to the canonical operating point's
motif-indicator field; the relaxed-filter masked channel is not
part of the primary verdict and is not computed by this driver.

### 2.5 FFT / radial-averaging parameters

```python
# Computed from fr.SIZE at runtime:
N_LATTICE = fr.SIZE                   # 64 on canonical
R_SHELL_MAX = N_LATTICE // 2          # 32 integer shells
```

### 2.6 Bootstrap / verdict parameters

```python
BOOTSTRAP_B = 4000
BOOTSTRAP_RNG_SEED = 199              # distinct from F4/F4-alt (99) for reproducibility audit

# Tenth-pass GR-SC 1.7 band
VERDICT_CONFIRMED_LO = 0.75
VERDICT_CONFIRMED_HI = 0.85
VERDICT_REFUTED_LO = 0.70
VERDICT_REFUTED_HI = 0.90

# Self-calibration guardrail (scoping §4):
SELF_CAL_TOL = 0.10                   # ±10% ensemble band on r_½^unfilt vs ξ_canonical
```

---

## 3. Driver architecture

### 3.1 Per-seed execution

For each seed s ∈ SEEDS:

1. **Calibration pre-pass.** Run the 9-point w-grid calibration
   (function `run_calibration_for_seed` verbatim from F4-alt).
2. **Interpolate w → ξ_target** (function `interpolate_w` from F4-alt).
3. **Evolve 40 snapshots** (function `evolve_40snap` from F4-alt).
   Apply one refinement step if |miss| > CALIBRATION_TOL.
4. **Record ξ_measured (per-seed).** Verify L_ray = DIMLESS_HINGE ·
   ξ_measured is not in WINDOW_A or WINDOW_B; raise if so.
5. **For each of the 40 snapshots `p(x)`:**
   - Extract motif positions with the canonical filter
     (function `extract_motifs_with_positions` from F4-alt, with
     `ALPHA_FILT = 0.25`, `N_REQ = 4`, `L_ray = 1.08 · ξ_measured`).
   - Build the 0/1 motif mask `M(x)` on the 64² lattice; `M[i,j] = 1`
     if a motif was admitted at site `(i, j)` in this snapshot,
     else 0.
   - Record per-snapshot mask density `ρ_M = M.mean()`.
6. **Compute per-snapshot FFT autocorrelations** (see §3.2) for:
   - **Channel A:** bulk `p(x)` (mean-subtracted).
   - **Channel B:** masked `p(x) · M(x)` (mean-subtracted *after
     masking*).
7. **Accumulate per-seed ensemble curves** by averaging across the
   40 snapshots: `ξ_φ_A_seed(r)`, `ξ_φ_B_seed(r)` on Z² shell
   radii.

### 3.2 FFT autocorrelation core

For any 64² field `φ`:

```python
def fft_autocorr(field):
    """Return (shells, xi_of_shell) where xi is the radially-averaged
    autocorrelation on Z² integer-squared-radius shells."""
    N = field.shape[0]
    f = field - np.mean(field)
    F = fft2(f)
    P = np.abs(F) ** 2
    C = np.real(ifft2(P)) / (N * N)      # real-space autocorr, centred at (0,0)
    C = fftshift(C)                       # centre r=0 at (N//2, N//2)

    # Radial average over integer-squared-radius shells:
    cy, cx = N // 2, N // 2
    y_idx, x_idx = np.indices(C.shape)
    r_squared = (y_idx - cy) ** 2 + (x_idx - cx) ** 2

    # Unique sorted shell radii (in lattice units):
    unique_r2 = np.unique(r_squared)
    shells = np.sqrt(unique_r2.astype(float))
    xi_shells = np.array([
        C[r_squared == r2].mean() for r2 in unique_r2
    ])
    # Keep r ∈ [0, N//2] to avoid edge-wrap artefacts at large r:
    keep = shells <= (N // 2)
    return shells[keep], xi_shells[keep]
```

This yields `ξ_φ(0)` (= variance σ_0²), `ξ_φ(1)`, `ξ_φ(√2)`,
`ξ_φ(2)`, `ξ_φ(√5)`, … on every achievable Z² shell up to r =
N/2. The shell structure is dense at small r (no gap-induced
empty bins), which is the key advantage over the F4 pair-binning
channel.

### 3.3 Ensemble averaging

Per-seed curves `ξ_φ_A_seed(r)` and `ξ_φ_B_seed(r)` are averaged
across SEEDS to form the ensemble central curves:

```python
xi_phi_A_central(r) = mean_over_seeds(xi_phi_A_seed(r))
xi_phi_B_central(r) = mean_over_seeds(xi_phi_B_seed(r))
```

Each curve is **normalised by its own σ_0²**:

```python
C_A(r) = 2 * (1 - xi_phi_A_central(r) / xi_phi_A_central(0))
C_B(r) = 2 * (1 - xi_phi_B_central(r) / xi_phi_B_central(0))
```

so that `C(0) = 0` and `C(∞) → 2` (by construction).

### 3.4 Bootstrap across seeds

```python
rng = np.random.default_rng(BOOTSTRAP_RNG_SEED)
bootstrap_C_A = np.empty((BOOTSTRAP_B, len(shells)))   # per-resample C_A(r) curve
bootstrap_C_B = np.empty((BOOTSTRAP_B, len(shells)))
for b in range(BOOTSTRAP_B):
    idx = rng.integers(0, len(SEEDS), size=len(SEEDS))   # bootstrap over seeds
    A_b = np.mean(per_seed_xi_A_matrix[idx], axis=0)
    B_b = np.mean(per_seed_xi_B_matrix[idx], axis=0)
    bootstrap_C_A[b] = 2 * (1 - A_b / A_b[0])
    bootstrap_C_B[b] = 2 * (1 - B_b / B_b[0])
```

16 / 84 quantiles across b give per-r band; the half-rise
bootstrap uses per-resample half-rise interpolation (same
pattern as `bootstrap_half_rise` from F4-alt, adapted to the
new grid).

### 3.5 Half-rise extraction and ratio

```python
def half_rise_interp(shells, C_values, target=1.0):
    """Smallest r where C(r) = target, via linear interpolation between
    consecutive shell radii. Returns None if no crossing, or flags
    'multi-crossing' if more than one crossing (diagnostic only — uses
    the smallest crossing as canonical)."""
    crossings = []
    for k in range(len(shells) - 1):
        if (C_values[k] < target) != (C_values[k+1] < target):
            denom = C_values[k+1] - C_values[k]
            if abs(denom) < 1e-12:
                continue
            r_cross = shells[k] + (shells[k+1] - shells[k]) * \
                      (target - C_values[k]) / denom
            crossings.append(r_cross)
    return crossings  # caller picks [0] if non-empty

r_half_unfilt = smallest_crossing(shells, C_A(r), target=1.0)
r_half_filt   = smallest_crossing(shells, C_B(r), target=1.0)

ratio = r_half_filt / r_half_unfilt
```

Bootstrap band on ratio: apply the same extraction to each
bootstrap-resample pair `(C_A_b, C_B_b)`; report 16 / 84
quantiles of the ratio distribution.

### 3.6 Self-calibration guardrail (scoping §4)

Before verdict adjudication:

```python
miss_self_cal = abs(r_half_unfilt - XI_CANONICAL) / XI_CANONICAL
if miss_self_cal > SELF_CAL_TOL:
    verdict = "Inconclusive"
    reason = ("Self-calibration check failed: "
              f"r_half_unfilt = {r_half_unfilt:.4f} lu "
              f"deviates from ξ_canonical = {XI_CANONICAL:.4f} "
              f"by {miss_self_cal*100:.1f}% > {SELF_CAL_TOL*100:.0f}%")
    # skip primary verdict branch
```

This catches cases where the FFT-derived r_½^unfilt does not
match the canonical ξ (measured by `xi_halfdecay` on the same
channel) — which would indicate either an FFT-pipeline bug or
a discrepancy between the full-shell FFT radial average and
the integer-shell `xi_halfdecay` extraction.

### 3.7 Verdict taxonomy (four-way)

```python
def compute_verdict(ratio_central, ratio_bootstrap_band, self_cal_ok):
    if not self_cal_ok:
        return ("Inconclusive", "Self-calibration failed — see §3.6")
    if ratio_central is None:
        return ("Inconclusive", "No C_B(r) = 1 crossing in measured range")
    if VERDICT_CONFIRMED_LO <= ratio_central <= VERDICT_CONFIRMED_HI:
        if ratio_bootstrap_band is not None:
            lo, hi = ratio_bootstrap_band
            if lo < VERDICT_CONFIRMED_LO or hi > VERDICT_CONFIRMED_HI:
                return ("Confirmed-marginal",
                        f"ratio = {ratio_central:.3f} ∈ [0.75, 0.85] "
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
```

---

## 4. Outputs

All under

```
OUT_DIR = outputs/ed_sc_3_5_fft_xi_field/
```

### 4.1 `xi_field_profile.csv` (ensemble central table)

One row per shell radius; columns:

| column | meaning |
|---|---|
| `r_shell` | shell radius (lu); first row is r = 0 (σ_0²) |
| `xi_phi_A` | ensemble-mean bulk-field ξ_φ(r) |
| `xi_phi_A_CI_lo` | 16%-quantile across seed bootstrap |
| `xi_phi_A_CI_hi` | 84%-quantile across seed bootstrap |
| `C_A` | C_redshift(r) on bulk channel |
| `C_A_CI_lo`, `C_A_CI_hi` | bootstrap bands on C |
| `xi_phi_B` | ensemble-mean masked-field ξ_φ(r) |
| `xi_phi_B_CI_lo`, `xi_phi_B_CI_hi` | bootstrap bands |
| `C_B`, `C_B_CI_lo`, `C_B_CI_hi` | C_redshift on masked channel |
| `n_lattice_sites_in_shell` | count of (i, j) sites with r²_exact = shell² |

### 4.2 `xi_field_per_seed.csv` (per-seed decomposition)

One row per (seed × shell_radius); columns:

| column | meaning |
|---|---|
| `seed` | int |
| `r_shell` | shell radius (lu) |
| `xi_phi_A_seed` | per-seed bulk ξ_φ(r) |
| `xi_phi_B_seed` | per-seed masked ξ_φ(r) |
| `xi_seed` | per-seed ξ_measured (40-snap mean) |
| `L_ray_seed` | per-seed L_ray = 1.08 · ξ_seed |
| `mean_mask_density_seed` | per-seed mean of M(x).mean() across 40 snaps |

### 4.3 `xi_field_summary.json` (summary with verdict)

Top-level keys:

```python
{
  "method": "ED-SC 3.5 FFT-based bulk-field autocorrelation; "
            "measures ξ_φ(r) on (A) bulk p-field and (B) motif-mask-"
            "weighted p-field; primary verdict against GR-SC 1.7 "
            "half-rise compression prediction",
  "simulator_of_record": "r2_grf_falsifier_tests.py + ED_Update_Rule.ed_step_mobility",
  "xi_canonical_lattice_units": 1.7575325729470939,
  "xi_target": 1.7575,
  "alpha_filt": 0.25,
  "N_req": 4,
  "seeds": [11, ..., 111],
  "canonical_params": {...},                       # from fr module
  "resonance_windows_excluded": {"A": [2.50, 2.80], "B": [3.50, 3.90]},

  "per_seed": [{"seed": ..., "xi_measured": ..., "L_ray": ...,
                "mean_mask_density": ..., "wall_seconds": ...}, ...],
  "shells": [0.0, 1.0, 1.4142..., 2.0, 2.2360..., ...],

  "bulk_field_channel_A": {
    "xi_phi_central": [...],                       # per shell
    "C_central": [...],
    "C_CI_lo": [...],
    "C_CI_hi": [...],
    "r_half_central": float,
    "r_half_bootstrap_16_84": [lo, hi],
    "n_bootstrap_samples_valid": int,
    "multi_crossing_flag": bool,
    "non_monotone_flag": bool,
  },
  "masked_field_channel_B": {
    # Same schema as Channel A
    "...": ...,
    "mean_mask_density_ensemble": float,
  },

  "half_rise_comparison": {
    "r_half_unfilt": float,                        # from Channel A
    "r_half_filt": float,                          # from Channel B
    "ratio_central": float,
    "ratio_bootstrap_16_84": [lo, hi],
  },

  "self_calibration_check": {
    "r_half_unfilt": float,
    "xi_canonical_reference": 1.7575325729470939,
    "miss_fraction": float,
    "tolerance": 0.10,
    "passed": bool,
  },

  "verdict": {
    "verdict": "Confirmed | Confirmed-marginal | Refuted | Inconclusive",
    "reason": "...",
    "tenth_pass_prediction": "0.80 ± 0.05 (GR-SC 1.7)",
    "confirmed_threshold": [0.75, 0.85],
    "refuted_threshold_low": 0.70,
    "refuted_threshold_high": 0.90,
    "taxonomy": "four-way (inherited from F4)",
  },

  "diagnostics": {
    "non_monotone_A": bool,
    "non_monotone_B": bool,
    "multi_crossing_A": bool,
    "multi_crossing_B": bool,
    "mean_mask_density_ensemble": float,
    "resonance_window_intrusions": [],
    "r_diag_excursions": [],                        # per scoping §3
  },

  "cross_channel_reconciliation": {
    "parent_F4_sub_arc_verdict": "Refuted-by-extension structural (relaxed filter, N_req=2)",
    "parent_F4_canonical_verdict": "Inconclusive (pair-count sparsity)",
    "interpretation_matrix_case": "A/B/C/D per scoping §5",
    # Filled post-hoc by integration memo, left as placeholder string
    # in the driver output: "pending_integration_memo".
  },

  "wall_seconds_total": float,
}
```

---

## 5. Summary JSON fields — canonical list

For quick driver-writer reference, the mandatory fields (every
implementation must produce these; cosmetic fields like nested
ordering may vary):

1. `shells` — list of shell radii (lu), starting at 0.0.
2. `bulk_field_channel_A.xi_phi_central`, `.C_central`,
   `.C_CI_lo`, `.C_CI_hi`, `.r_half_central`,
   `.r_half_bootstrap_16_84`.
3. `masked_field_channel_B.xi_phi_central`, `.C_central`,
   `.C_CI_lo`, `.C_CI_hi`, `.r_half_central`,
   `.r_half_bootstrap_16_84`, `.mean_mask_density_ensemble`.
4. `half_rise_comparison.ratio_central`,
   `.ratio_bootstrap_16_84`.
5. `self_calibration_check.passed`, `.miss_fraction`.
6. `verdict.verdict`, `.reason`.
7. `diagnostics.non_monotone_A/B`, `.multi_crossing_A/B`,
   `.mean_mask_density_ensemble`.

---

## 6. Deliverables

- [x] Complete driver specification (this memo).
- [x] Pre-registered four-way verdict taxonomy (Confirmed /
  Confirmed-marginal / Refuted / Inconclusive; includes
  self-calibration-guardrail-triggered Inconclusive).
- [ ] Next step: implement
  `analysis/scripts/ed_sc_3_5_fft_xi_field.py` as a
  one-pass translation of this memo. Implementation-time
  guidance:
  - Inherit all F4-alt driver scaffolding (calibration,
    `evolve_40snap`, `extract_motifs_with_positions`,
    resonance-window guards, half-rise interpolation pattern).
  - Add the FFT autocorrelation core (§3.2) and the radial
    shell averaging as the only new machinery.
  - Bootstrap is over *seeds*, not pairs — a simpler
    structure than F4-alt's pair-bootstrap.
  - Wall budget: ≈ 30–90 s on 64² (FFT is cheap; the motif
    extraction is the rate-limiting step, same as F4-alt).
- [ ] Next step after implementation: execute and record
  artefacts; write
  `theory/ED_SC_3_5_FFT_XiField_Integration.md` to synthesise
  against the F4 sub-arc per scoping §5.

**Changelog.**

- 2026-04-23 (seventeenth pass) — Initial draft. One-pass-
  implementation-sufficient driver specification for the FFT
  field-autocorrelation primary channel. Inherits F4-alt
  scaffolding verbatim; adds only the FFT radial-shell
  autocorrelation core (§3.2), per-seed bootstrap scheme
  (§3.4), self-calibration guardrail (§3.6), and four-way
  verdict (§3.7). Output schema (§4-5) specified completely
  to prevent downstream schema-drift.
