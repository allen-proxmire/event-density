# ED-SC 3.6 L-Larger Follow-up — Driver Specification

**Pass:** seventeenth (L-larger driver memo)
**Date:** 2026-04-23
**Parent scoping memo:** `theory/ED_SC_3_6_L_Larger_Scoping.md`
**Parent driver templates:**
- `analysis/scripts/ed_sc_3_4_twopoint_correlation.py` (F4 canonical, Channel A scaffolding)
- `analysis/scripts/ed_sc_3_5_fft_xi_field.py` (ED-SC 3.5 FFT driver, Channels B and C scaffolding)
**This driver memo specifies:** `analysis/scripts/ed_sc_3_6_l_larger.py` (forthcoming)

---

## 1. Purpose

Provide a one-pass-implementation-sufficient executable
specification for the ED-SC 3.6 L-larger three-channel driver.
The driver combines the F4-canonical pair-binning channel and
the ED-SC 3.5 full-shell FFT autocorrelation channels (masked +
bulk-reference) into a single run per lattice size L, producing
a three-channel combined verdict against the GR-SC 1.7 half-rise
compression prediction `r_½^filt / r_½^unfilt = 0.80 ± 0.05`.

**Objective.** Test GR-SC 1.7 at the canonical filter
`(α_filt, N_req) = (0.25, 4)` on a lattice size where motif-mask
sparsity no longer blocks correlation measurement. L = 128
primary; L = 256 optional secondary per scoping §2.

**One-pass guarantee.** Any future session should be able to
write the driver script from this memo alone, given the named
simulator of record and the parent driver templates, without
re-reading the scoping memo or the F4 / ED-SC 3.5 driver specs.

---

## 2. Inputs

### 2.1 Lattice size

```python
L_PRIMARY = 128
L_SECONDARY = 256                     # run only if L=128 Inconclusive
L_ACTIVE = L_PRIMARY                  # the driver's active size; override via CLI
```

The driver overrides `fr.SIZE` at entry:

```python
fr.SIZE = L_ACTIVE                    # BEFORE any calibration call
```

All downstream scaffolding (calibration, evolution, motif-pass)
reads `fr.SIZE` dynamically, so the override propagates without
code changes.

### 2.2 Ensemble

```python
SEEDS = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]
N_SNAPSHOTS_PER_SEED = 40
XI_TARGET = 1.7575
XI_CANONICAL = 1.7575325729470939

XI_BURN_IN = 100
XI_SNAP_EVERY = 10
CALIBRATION_W_GRID = [0.05, 0.08, 0.10, 0.13, 0.16, 0.20, 0.25, 0.30, 0.35]
CALIBRATION_TOL = 0.01
```

Inherited verbatim from ED-SC 3.5 / F4-alt.

### 2.3 Canonical motif filter

```python
ALPHA_FILT = 0.25
N_REQ = 4                             # CANONICAL (not relaxed)
DIMLESS_HINGE = 1.08
DIAG_COS = 0.707
WINDOW_A = (2.50, 2.80)
WINDOW_B = (3.50, 3.90)
```

Canonical operating point preserved. No scope amendment at this
arc; the whole point is to test whether L-larger alone (without
relaxing the filter) suffices.

### 2.4 Measurement parameters

```python
# Channel A (pair-binned F4, same grid as F4 canonical)
R_GRID = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
DR_BIN = 0.5
R_GRID_MIN_EDGE = 0.25
R_GRID_MAX_EDGE = 5.25

MIN_PAIRS_ENSEMBLE = 20
MIN_PAIRS_PER_SEED = 10
PRIMARY_GATE_CHANNEL_A = 8            # ≥ 8 of 10 bins admissible

# Channel B (FFT masked) primary gate (absolute motif count)
PRIMARY_GATE_CHANNEL_B_MIN_MOTIFS = 3200   # L=128; scales with L² target
# Computed at runtime as: max(3200, int(L_ACTIVE**2 * 5e-4 * N_SNAPSHOTS * N_SEEDS / 2))
# — a floor of 3200 ensemble-total motifs, raised if L>128 expects more.

# Channel C (FFT bulk, self-calibration)
SELF_CAL_TOL = 0.10

# Bootstrap (both channels)
BOOTSTRAP_B = 4000
BOOTSTRAP_RNG_SEED = 299              # distinct from F4/ED-SC 3.5
```

### 2.5 Verdict thresholds

```python
VERDICT_CONFIRMED_LO = 0.75
VERDICT_CONFIRMED_HI = 0.85
VERDICT_REFUTED_LO = 0.70
VERDICT_REFUTED_HI = 0.90
```

### 2.6 Output directory

```python
OUT_DIR = os.path.join(HERE, "..", "..", "outputs",
                       f"ed_sc_3_6_l_larger_L{L_ACTIVE}")
```

If L = 128 and L = 256 are both run in a single session, they
write to two distinct subdirectories (`ed_sc_3_6_l_larger_L128/`
and `ed_sc_3_6_l_larger_L256/`).

---

## 3. Channel A — pair-binned F4 (L-generalised)

Verbatim port of `ed_sc_3_4_twopoint_correlation.py` with the
`fr.SIZE` override. Every estimator, bootstrap scheme, and
admissibility test is unchanged.

### 3.1 Per-seed execution (shared with Channels B and C)

For each seed s ∈ SEEDS:

1. Calibration pre-pass (function `run_calibration_for_seed`
   from F4/ED-SC 3.5 templates, verbatim).
2. IC-amplitude interpolation (`interpolate_w`, verbatim).
3. 40-snapshot evolution (`evolve_40snap`, verbatim; reads
   `fr.SIZE = L_ACTIVE` implicitly).
4. Record ξ_measured (per-seed mean across 40 snaps via
   `xi_halfdecay`). Check L_ray = 1.08 · ξ_measured not in
   WINDOW_A or WINDOW_B; raise if so.
5. Per-snapshot: extract motifs with positions (for Channel A
   pair enumeration) *and* build the 0/1 mask M(x) (for
   Channel B). Both derive from the same `fr.find_morse_saddles`
   + `fr.motif_pass` pipeline, so a single extraction step
   produces both; do not repeat the saddle-finding work.

### 3.2 Channel A pair enumeration + r-binning

```python
def accumulate_pairs_per_seed(motifs_per_snap, L):
    pair_pool = {k: [] for k in range(len(R_GRID))}
    for snap_motifs in motifs_per_snap:
        n = len(snap_motifs)
        for a in range(n):
            m_a = snap_motifs[a]
            for b in range(a + 1, n):
                m_b = snap_motifs[b]
                r = min_image_distance(
                    (m_a["i"], m_a["j"]),
                    (m_b["i"], m_b["j"]),
                    L=L)
                k = r_bin_assign(r)
                if k is None:
                    continue
                pair_pool[k].append((m_a["rho"], m_b["rho"]))
    return pair_pool
```

Note: `min_image_distance` takes the explicit `L` argument (it
no longer defaults to `fr.SIZE`); the explicit argument is the
one change from the F4-alt canonical `min_image_distance`
signature.

### 3.3 Channel A estimators + bootstrap

Verbatim:
- `pearson_C(pair_pool, rho_bar, var_rho)`
- `spearman_C(pair_pool)`
- `bootstrap_ensemble_C(pair_pool, rho_bar, var_rho, B=4000)`

Ensemble pool statistics (ρ̄, σ²_ρ) computed across all admitted
motifs from all seeds × snapshots, identical to F4-alt
`main()` steps 2–4.

### 3.4 Channel A half-rise and verdict

```python
r_half_A_filt   = linear_interp_halfrise(R_GRID, C_A_central)
r_half_A_unfilt = XI_CANONICAL                  # GR-SC 1.7 reference
ratio_A         = r_half_A_filt / r_half_A_unfilt
```

Bootstrap band via `bootstrap_half_rise` from F4-alt, verbatim.
Four-way verdict via `compute_verdict(ratio_A,
ratio_A_bootstrap_band)`, verbatim from F4-alt.

**Channel A primary gate (§5.1 of scoping):**
`n_admissible_A = sum(1 for bin in r_bins_data if not
bin["low_N_ensemble"])` ≥ 8.

---

## 4. Channel B — FFT masked-field (L-generalised)

Verbatim port of `ed_sc_3_5_fft_xi_field.py` Channel B scaffolding,
with `fr.SIZE = L_ACTIVE` override and the absolute-motif-count
gate.

### 4.1 Shell index (recomputed for L_ACTIVE)

```python
_SHELLS, _SHELL_MASKS, _N_SITES_SHELL = _build_shell_index(fr.SIZE)
N_SHELLS = len(_SHELLS)
```

At L = 128 the shell count rises from 338 (on 64²) to
≈ 1,349 shells (≈ 4× 64² count, since shell density grows as
L²/(4πr) at large r but is linear in L²). All shells with
r ≤ L/2 are kept.

### 4.2 Per-snapshot FFT autocorrelation

```python
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
```

Applied to `φ_B = p · M` (mean-subtracted inside the function).

### 4.3 Channel B bootstrap (over seeds)

```python
rng = np.random.default_rng(BOOTSTRAP_RNG_SEED)
n_seeds = len(SEEDS)
xi_B_boot = np.empty((BOOTSTRAP_B, N_SHELLS))
for b in range(BOOTSTRAP_B):
    idx = rng.integers(0, n_seeds, size=n_seeds)
    xi_B_boot[b] = per_seed_xi_B[idx].mean(axis=0)
C_B_boot = 2 * (1 - xi_B_boot / xi_B_boot[:, 0:1])
```

16 / 84 quantiles per shell give Channel B bands; per-resample
half-rise extraction → `bootstrap_r_half_B` list → 16 / 84
quantiles give `r_half_B_bootstrap_16_84`.

### 4.4 Channel B primary gate (§5.2 of scoping)

```python
ensemble_total_motifs = sum(
    sum(len(m) for m in r["motifs_per_snap"])
    for r in per_seed_results
)
channel_B_gate_passed = ensemble_total_motifs >= PRIMARY_GATE_CHANNEL_B_MIN_MOTIFS
```

At L = 128 the expected `ensemble_total_motifs` ≈ 3,360, giving
pair-coincidence statistics at the threshold. L = 256 raises this
to ≈ 13,440.

---

## 5. Channel C — FFT bulk-field (self-calibration reference)

Verbatim port of ED-SC 3.5 Channel A:

- Applied to `φ_A = p` (not masked).
- Same shell index as Channel B.
- Same bootstrap scheme as Channel B (independent resamples
  using the same bootstrap RNG stream).

### 5.1 Self-calibration guardrail (§5.3 of scoping)

```python
# Ensemble-mean xi_halfdecay from the per-seed ξ_measured values
xi_halfdecay_ensemble = np.mean([r["xi_measured"] for r in per_seed_results])
self_cal_miss = abs(xi_halfdecay_ensemble - XI_TARGET) / XI_TARGET
self_cal_ok = self_cal_miss <= SELF_CAL_TOL
```

**Note.** The ED-SC 3.5 driver applied the guardrail to the
*full-shell FFT* r_half; here we apply it to the
**`xi_halfdecay` ensemble mean** against ξ_target (the standard
ED-SC 3.x calibration gate). The FFT full-shell r_half (Channel C
output) is reported but does not drive the guardrail — this
avoids the ED-SC 3.5 §2.4 estimator-bias artefact, consistent
with the scoping memo §4.2 within-arc-one-estimator rule.

Report *both* `xi_halfdecay_ensemble` and `r_half_C_FFT` in the
summary JSON; the guardrail uses the former.

---

## 6. Ratio extraction

### 6.1 Primary ratio (Channel B vs Channel C)

Both numerator and denominator from the same FFT full-shell
estimator:

```python
ratio_primary = r_half_B_FFT / r_half_C_FFT
ratio_primary_bootstrap = bootstrap_quantile_of(
    [r_half_B_b / r_half_C_b
     for (r_half_B_b, r_half_C_b) in zip(
         bootstrap_r_half_B, bootstrap_r_half_C)
     if r_half_B_b is not None and r_half_C_b is not None
        and r_half_C_b > 0],
    [0.16, 0.84])
```

This ratio is the **primary GR-SC 1.7 test** for this arc: both
quantities from the same coarse-graining rule, no cross-estimator
bias.

### 6.2 Diagnostic ratio (Channel A pair-binned)

```python
ratio_A = r_half_A_filt / XI_CANONICAL
```

This ratio uses pair-binned half-rise (F4-canonical) as
numerator and `xi_halfdecay`-defined ξ_canonical as
denominator. Both quantities are computed on the canonical
ED-SC 3.3 estimator chain (no FFT shift). Reported alongside
the primary ratio; used for cross-channel reconciliation per
scoping §6.

### 6.3 Channel-independence gate

If `|ratio_primary − ratio_A| > 0.15`, flag the result as
**channel-dependent** in the verdict reason string (not as a
separate verdict category — the taxonomy stays four-way per
channel, but the combined interpretation escalates per the
scoping §6 reconciliation matrix).

---

## 7. Outputs

All under `OUT_DIR = outputs/ed_sc_3_6_l_larger_L{L}/`
(where `{L}` is the active lattice size). Mandatory files:

### 7.1 `correlation_twopoint_table.csv` (Channel A ensemble)

Columns identical to F4-canonical table:
`r_target, N_pairs_ensemble, C_ensemble, C_CI_lo, C_CI_hi,
C_ensemble_rank, model_band_rel, CoV_across_seeds,
N_seeds_in_CoV, N_pairs_per_seed_mean, low_N_ensemble,
low_N_any_seed, Spearman_undefined, bootstrap_iterations`.

### 7.2 `correlation_twopoint_per_seed.csv` (Channel A per-seed)

Columns: `seed, r_target, N_pairs_seed, C_seed, C_seed_low_N,
xi_seed, L_ray_seed`.

### 7.3 `xi_field_profile.csv` (Channels B + C ensemble)

Columns (identical schema to ED-SC 3.5 profile): `r_shell,
n_lattice_sites_in_shell, xi_phi_A, xi_phi_A_CI_lo,
xi_phi_A_CI_hi, C_A, C_A_CI_lo, C_A_CI_hi, xi_phi_B,
xi_phi_B_CI_lo, xi_phi_B_CI_hi, C_B, C_B_CI_lo, C_B_CI_hi`.

Note: the "A" labels in this CSV are the FFT channels, consistent
with ED-SC 3.5's naming — **Channel A (pair-binned) of this memo
≠ A column of this CSV**. Document the naming reconciliation in
the CSV header comment and in the summary JSON method string.

### 7.4 `xi_field_per_seed.csv` (Channels B + C per-seed)

Columns: `seed, r_shell, xi_phi_A_seed, xi_phi_B_seed, xi_seed,
L_ray_seed, mean_mask_density_seed`.

### 7.5 `summary.json` (the integration artefact)

```python
{
  "method": "ED-SC 3.6 L-larger three-channel driver; L_active = {L}; "
            "Channel A pair-binned F4 (canonical filter), "
            "Channel B FFT mask-weighted, "
            "Channel C FFT bulk-reference",
  "simulator_of_record": "r2_grf_falsifier_tests.py + ED_Update_Rule.ed_step_mobility",
  "L_active": L_ACTIVE,
  "L_primary": 128,
  "L_secondary_planned": 256,
  "xi_canonical_lattice_units": XI_CANONICAL,
  "xi_target": XI_TARGET,
  "alpha_filt": 0.25,
  "N_req": 4,
  "seeds": SEEDS,
  "r_grid_pair_binned": R_GRID,
  "dr_bin_pair_binned": DR_BIN,
  "n_shells_fft": N_SHELLS,
  "canonical_params": {...},                       # from fr module
  "resonance_windows_excluded": {"A": [2.50, 2.80], "B": [3.50, 3.90]},

  "per_seed": [...],                                # xi_measured, L_ray, wall, calibration

  "channel_A_pair_binned": {
    "r_bins": [...],                                # F4-canonical schema
    "n_admissible_bins": int,
    "primary_gate_passed": bool,
    "r_half_filt_central": float or None,
    "r_half_filt_bootstrap_16_84": [lo, hi] or None,
    "r_half_unfilt_reference": XI_CANONICAL,
    "ratio_A_central": float or None,
    "ratio_A_bootstrap_16_84": [lo, hi] or None,
    "verdict_A": "...",
    "verdict_A_reason": "...",
  },

  "channel_B_fft_masked": {
    "shells": [...],
    "xi_phi_central": [...],
    "C_central": [...],
    "C_CI_lo": [...], "C_CI_hi": [...],
    "r_half_central": float or None,
    "r_half_bootstrap_16_84": [lo, hi] or None,
    "ensemble_total_motifs": int,
    "mean_mask_density_ensemble": float,
    "primary_gate_passed": bool,
    "multi_crossing_flag": bool,
    "non_monotone_flag": bool,
  },

  "channel_C_fft_bulk_reference": {
    "shells": [...],
    "xi_phi_central": [...],
    "C_central": [...],
    "C_CI_lo": [...], "C_CI_hi": [...],
    "r_half_FFT_central": float,
    "r_half_FFT_bootstrap_16_84": [lo, hi],
    "xi_halfdecay_ensemble_mean": float,
    "xi_halfdecay_ensemble_CI": [lo, hi],
    "multi_crossing_flag": bool,
    "non_monotone_flag": bool,
  },

  "self_calibration_check": {
    "xi_halfdecay_ensemble": float,
    "xi_target_reference": XI_TARGET,
    "miss_fraction": float,
    "tolerance": SELF_CAL_TOL,
    "passed": bool,
  },

  "primary_ratio": {
    "ratio_central": float or None,                 # Channel B / Channel C FFT
    "ratio_bootstrap_16_84": [lo, hi] or None,
    "ratio_A_for_comparison": float or None,        # pair-binned diagnostic
    "channel_independence_flag": bool,              # |primary − A| > 0.15
  },

  "combined_verdict": {
    "verdict": "Confirmed | Confirmed-marginal | Refuted | Inconclusive",
    "reason": "...",
    "channel_A_verdict": "...",
    "channel_B_verdict": "...",
    "reconciliation_case": "row_A+row_B per scoping §6 matrix",
    "promote_to_L256": bool,
    "taxonomy": "four-way per channel; combined via scoping §6 matrix",
  },

  "diagnostics": {
    "n_admissible_bins_channel_A": int,
    "ensemble_total_motifs_channel_B": int,
    "mean_mask_density_channel_B": float,
    "multi_crossing_flags": {"A": bool, "B": bool, "C": bool},
    "non_monotone_flags": {"A": bool, "B": bool, "C": bool},
    "empty_masks_per_seed": {...},
    "r_diag_excursions": [...],
    "resonance_window_intrusions": [],
    "n_valid_bootstrap": int,
  },

  "wall_seconds_total": float,
}
```

### 7.6 `stdout.json`

Abbreviated summary printed to stdout at end of run (for
CLI consumption):

```python
{
  "L_active": L_ACTIVE,
  "N_seeds": 10,
  "n_admissible_bins_A": int,
  "ensemble_total_motifs_B": int,
  "r_half_A_pair_binned": float or None,
  "r_half_B_FFT": float or None,
  "r_half_C_FFT": float,
  "xi_halfdecay_ensemble": float,
  "ratio_primary": float or None,
  "ratio_primary_bootstrap_16_84": [...] or None,
  "ratio_A_diagnostic": float or None,
  "self_cal_passed": bool,
  "channel_A_gate_passed": bool,
  "channel_B_gate_passed": bool,
  "channel_independence_flag": bool,
  "combined_verdict": "...",
  "combined_verdict_reason": "...",
  "promote_to_L256": bool,
  "wall_seconds_total": float,
}
```

---

## 8. Verdict logic

### 8.1 Per-channel verdicts

Both Channel A and Channel B produce their own four-way verdict
using the same `compute_verdict(ratio, bootstrap_band)` function
(inherited from F4 / ED-SC 3.5 verbatim). Channel C is a
reference — it does not produce a verdict, only the self-
calibration check.

### 8.2 Combined verdict (via scoping §6 matrix)

```python
def combine_verdicts(verdict_A, verdict_B,
                      channel_A_gate_ok, channel_B_gate_ok,
                      self_cal_ok):
    if not self_cal_ok:
        return ("Inconclusive",
                "Self-calibration guardrail failed — Channel C check "
                f"miss = {self_cal_miss*100:.1f}% > {SELF_CAL_TOL*100}%")
    if not channel_A_gate_ok and not channel_B_gate_ok:
        return ("Inconclusive",
                "Both Channel A and Channel B primary gates failed")
    # If only one channel passes its gate, its verdict is the combined:
    if channel_A_gate_ok and not channel_B_gate_ok:
        return (verdict_A,
                f"Channel B gate failed; Channel A verdict reported. {...}")
    if channel_B_gate_ok and not channel_A_gate_ok:
        return (verdict_B,
                f"Channel A gate failed; Channel B verdict reported. {...}")
    # Both gates passed — apply scoping §6 matrix:
    if verdict_A == "Confirmed" and verdict_B == "Confirmed":
        return ("Confirmed",
                "Two-channel Confirmed: pair-binned and FFT-masked both "
                "report ratio ∈ [0.75, 0.85]")
    if verdict_A == "Refuted" and verdict_B == "Refuted":
        return ("Refuted",
                "Two-channel Refuted: pair-binned and FFT-masked both "
                "report ratio outside [0.70, 0.90]")
    if verdict_A in {"Confirmed", "Confirmed-marginal"} and \
       verdict_B in {"Confirmed", "Confirmed-marginal"}:
        return ("Confirmed-marginal",
                "Two-channel Confirmed or marginal")
    if verdict_A == "Refuted" and verdict_B in {"Confirmed",
                                                 "Confirmed-marginal"}:
        return ("Inconclusive",
                "Channel-dependent: Channel A Refuted but Channel B "
                "Confirmed (or marginal). Escalates to eighteenth-pass "
                "scoping per scoping §6 row 2.")
    if verdict_B == "Refuted" and verdict_A in {"Confirmed",
                                                 "Confirmed-marginal"}:
        return ("Inconclusive",
                "Channel-dependent: Channel B Refuted but Channel A "
                "Confirmed (or marginal). Escalates per scoping §6.")
    # Any channel Inconclusive → report the other's verdict or Inconclusive:
    if verdict_A == "Inconclusive":
        return (verdict_B, f"Channel A Inconclusive; Channel B = {verdict_B}")
    if verdict_B == "Inconclusive":
        return (verdict_A, f"Channel B Inconclusive; Channel A = {verdict_A}")
    return ("Inconclusive", f"Unhandled case: A={verdict_A}, B={verdict_B}")
```

### 8.3 Promotion rule to L = 256

```python
promote_to_L256 = (
    L_ACTIVE == L_PRIMARY
    and combined_verdict == "Inconclusive"
    and (verdict_A == "Inconclusive" or verdict_B == "Inconclusive")
    and not self_cal_ok_failure
)
```

Stated in prose per scoping §6: if L = 128 passed the self-cal
guardrail but one or both channels reported Inconclusive due
to insufficient statistics (not due to a genuine no-crossing),
promote to L = 256.

---

## 9. Deliverables

- [x] Driver specification (this memo).
- [ ] Next step: implement `analysis/scripts/ed_sc_3_6_l_larger.py`
  as a one-pass translation of this memo. Implementation-time
  guidance:
  - Import F4-canonical scaffolding (`pair-binning`, `pearson_C`,
    `spearman_C`, `bootstrap_ensemble_C`, `bootstrap_half_rise`,
    `compute_verdict`) from `analysis/scripts/ed_sc_3_4_twopoint_correlation.py`
    via `sys.path` adjustment, OR duplicate verbatim (the
    inheritance pattern used by F4-alt + ED-SC 3.5 drivers).
  - Import ED-SC 3.5 FFT scaffolding (`_build_shell_index`,
    `fft_autocorr`, `C_from_xi`, `all_crossings`,
    `smallest_crossing`, `is_non_monotone`) from
    `analysis/scripts/ed_sc_3_5_fft_xi_field.py` similarly.
  - The only new code is the three-channel combiner in §8.2
    and the primary ratio extraction in §6.
  - **Order of operations in `main()`:** (1) override
    `fr.SIZE`; (2) rebuild `_SHELLS, _SHELL_MASKS, _N_SITES_SHELL`
    for the new size; (3) per-seed run (shared motif extraction);
    (4) ensemble statistics across seeds (pool motifs for
    Pearson, accumulate xi_A/xi_B arrays for FFT); (5) Channel A
    + bootstrap; (6) Channel B + bootstrap; (7) Channel C +
    self-cal check; (8) primary ratio + diagnostic ratio;
    (9) combined verdict; (10) write outputs.
  - **Wall budget.** On L = 128: expect 400–900 s (motif
    extraction on 16,384-site snapshots at 10 seeds × 40 snaps
    × 9 calibration w + 40 measurement = 490 evolved snapshots
    per seed). On L = 256: 2,000–4,000 s expected.
- [ ] Execution artefacts under `outputs/ed_sc_3_6_l_larger_L128/`
  (primary run); `outputs/ed_sc_3_6_l_larger_L256/` (promoted
  secondary run if triggered).
- [ ] Integration memo
  `theory/ED_SC_3_6_L_Larger_Integration.md`
  (post-execution synthesis; combined-verdict reporting;
  GR-SC 1.0 §5 canonical-filter row pointer update;
  recommendation on whether the arc closes or continues to
  L = 256; cross-channel reconciliation per scoping §6).

**Changelog.**

- 2026-04-23 (seventeenth pass) — Initial draft. One-pass-
  implementation-sufficient driver specification for ED-SC 3.6
  L-larger three-channel test. Channels A (pair-binned F4), B
  (FFT masked), C (FFT bulk reference). Channel A and Channel B
  inherit F4-canonical and ED-SC 3.5 scaffolding respectively
  with only the `fr.SIZE` override as the lattice generalisation.
  Self-calibration guardrail is on `xi_halfdecay` ensemble
  (not FFT full-shell r_half) per scoping §4.2 within-arc-one-
  estimator rule. Primary ratio uses Channel B / Channel C
  (both FFT); diagnostic ratio uses Channel A / ξ_canonical
  (both canonical ED-SC 3.3 chain). Combined-verdict
  reconciliation via scoping §6 matrix, implemented as
  `combine_verdicts` in §8.2. Promotion rule to L = 256
  in §8.3. Output schema in §7 pins a superset of F4-canonical
  and ED-SC 3.5 output-CSV columns plus new combined-verdict
  and self-cal blocks in summary.json.
