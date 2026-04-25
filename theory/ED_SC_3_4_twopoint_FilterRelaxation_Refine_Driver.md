# ED-SC 3.4 F4-alt-refine Two-Point Correlation Driver

**Pass:** seventeenth (GR-SC F4 Correlation-class sub-arc refinement)
**Date:** 2026-04-23
**Parent scope memo:** `theory/ED_SC_3_4_twopoint_FilterRelaxation_Refine.md`
**Parent driver memo:** `theory/ED_SC_3_4_twopoint_FilterRelaxation_Driver.md`
**Parent driver script:** `analysis/scripts/ed_sc_3_4_twopoint_correlation_relaxed.py`
**This driver script:** `analysis/scripts/ed_sc_3_4_twopoint_correlation_relaxed_refine.py`

---

## 1. Purpose

- Implement the Δr = 0.25 refinement for r ∈ [0.25, 2.0] to locate the
  half-rise of `C_redshift(r) = 2[1 − ξ_φ(r)/σ_0²]` — or to confirm
  its absence below the first admissible F4-alt separation (r = 1.0 lu).
- Preserve *every* guard, estimator, bootstrap, and verdict threshold
  from the F4-alt driver. This is a small-r re-sampling, not a
  methodological excursion.

The refinement is the third tier of the F4 sub-arc:
canonical (Δr = 0.5, N_req = 4) → relaxed (Δr = 0.5, N_req = 2) →
**refined (Δr = 0.25, N_req = 2)**. Tiers 1 and 2 are Inconclusive
(pair sparsity) and Inconclusive-structural-Refuted-by-extension
(`C(r) ≈ 2` across r ∈ [1.0, 5.0] lu with no C = 1 crossing). Tier 3
pushes resolution into r < 1.0 lu to test whether the crossing lies
there or the field is genuinely uncorrelated throughout.

---

## 2. Changes relative to F4-alt driver

Exactly four localised changes; everything else is inherited verbatim.

1. **R_GRID** replaced with the refinement grid
   ```python
   R_GRID = [0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00]
   ```
2. **DR_BIN** replaced
   ```python
   DR_BIN = 0.25
   ```
   and the derived edges update automatically:
   `R_GRID_MIN_EDGE = 0.125`, `R_GRID_MAX_EDGE = 2.125`.
3. **OUT_DIR** redirected
   ```python
   OUT_DIR = os.path.join(HERE, "..", "..", "outputs",
                          "ed_sc_3_4_twopoint_relaxed_refine")
   ```
4. **Summary JSON** gains a new top-level block
   ```json
   "filter_relaxation_refinement": {
       "parent_driver": "ed_sc_3_4_twopoint_correlation_relaxed.py",
       "parent_summary": ".../twopoint_relaxed.stdout.json",
       "motivation": "F4-alt C(r) saturated at ~2; half-rise below 1.0 lu",
       "scope_restriction": "refinement of small-r region only"
   }
   ```

No other line of the F4-alt driver changes.

---

## 3. Driver architecture

Identical to F4-alt:

- **Calibration pre-pass** — 9-point w-grid per seed; IC amplitude
  interpolated to ξ_target = 1.7575 lu; one-pass refinement if
  miss > 1 %.
- **40-snapshot evolution** — simulator of record
  `r2_grf_falsifier_tests.py + ED_Update_Rule.ed_step_mobility`;
  burn-in 100, snap-every 10.
- **Motif extraction with positions** — canonical filter
  (`α_filt = 0.25`, `N_req = 2`) with (i, j, ρ) recorded per motif.
- **Pair enumeration + r-binning** — minimum-image distance on the
  64² periodic torus; `r_bin_assign` against the refined
  `[0.125, 2.125)` edge window at Δr = 0.25.
- **Pearson + Spearman estimators** — paired per ensemble r-bin;
  agreement reported as `model_band_rel`.
- **Bootstrap** — 4000 pair-level resamples per bin; RNG seed 99;
  16/84 percentiles for C_CI_lo / C_CI_hi.
- **Per-seed CoV** — per-seed Pearson C and CoV across ≥ 10-pair
  seeds per bin.
- **Half-rise extraction** — linear-interpolation crossing of
  C(r) = 1 on the ensemble table; bootstrapped 16/84 band from
  re-interpolation across bootstrap samples.
- **Verdict logic** — inherits F4-alt taxonomy (Confirmed /
  Confirmed-marginal / Inconclusive / Refuted). The **six-way
  refinement taxonomy** (adding Case B Refuted-by-extension /
  Case C Inconclusive-nonmonotone / Inconclusive-thin under the
  primary admissibility gate ≥ 6 of 8) lives in the integration
  memo and is applied **post-hoc** to the driver's standard
  output. No driver-level code change: the driver emits the raw
  r-binned C table, which the integration memo classifies.

---

## 4. Diagnostics

The driver's stdout and JSON summary report, without change from
F4-alt plus the new refinement block:

- **Per-seed motif counts** — `N_motifs_total` per seed (expect
  ~2700 at N_req = 2 on the refinement's 10-seed ensemble).
- **N_pairs per refined r-bin** — the bottleneck on square-Z² 64²:
  only bins whose interior contains a lattice-achievable radius
  ({1, √2, 2, √5, …}) receive pairs. Empty bins are flagged
  `low_N_ensemble = True`.
- **n_bins_admissible** — count of bins with `N_pairs ≥ 20`
  (MIN_PAIRS_ENSEMBLE). The integration memo's six-way verdict
  gates on `n_admissible ≥ 6` of 8; driver records the raw count
  in `diagnostics.N_pairs_ensemble` per bin.
- **C(r) < 2 detection** — per-bin `C_ensemble` values are emitted
  verbatim; the Case-C trigger (any admissible bin with C < 2) is
  applied post-hoc in the integration memo.

---

## 5. Outputs

All under `OUT_DIR = outputs/ed_sc_3_4_twopoint_relaxed_refine/`:

1. `correlation_twopoint_table.csv` — one row per refined r-bin.
   Columns inherit F4-alt: `r_target, N_pairs_ensemble, C_ensemble,
   C_CI_lo, C_CI_hi, C_ensemble_rank, model_band_rel,
   CoV_across_seeds, N_seeds_in_CoV, N_pairs_per_seed_mean,
   low_N_ensemble, low_N_any_seed, Spearman_undefined,
   bootstrap_iterations`.
2. `correlation_twopoint_per_seed.csv` — one row per (seed × r-bin);
   columns `seed, r_target, N_pairs_seed, C_seed, C_seed_low_N,
   xi_seed, L_ray_seed`.
3. `correlation_twopoint_summary.json` — full driver summary with
   `filter_relaxation_amendment` (inherited from F4-alt) plus the
   new `filter_relaxation_refinement` block per §2.

---

## 6. Deliverables

- [x] Complete refinement driver spec (this memo).
- [x] Pre-registered **six-way verdict taxonomy** (Confirmed /
      Confirmed-marginal / Inconclusive / Refuted /
      Inconclusive-nonmonotone / Inconclusive-thin), carried in the
      parent scope memo `theory/ED_SC_3_4_twopoint_FilterRelaxation_Refine.md`
      and applied post-hoc by the integration memo
      `theory/ED_SC_3_4_twopoint_FilterRelaxation_Integration.md`.
- [x] Driver script
      `analysis/scripts/ed_sc_3_4_twopoint_correlation_relaxed_refine.py`
      as F4-alt + four localised changes (no other changes).

**Changelog.**

- 2026-04-23 — Initial draft. Driver spec pinned to "F4-alt
  verbatim + 4 changes only"; verdict-logic augmentations moved
  to the post-hoc integration-memo classification layer to keep
  the driver diff minimal and auditable.
