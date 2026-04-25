# ED-SC 3.4 Two-Point — F4-alt Δr = 0.25 Small-r Refinement

**Status:** Scope amendment. Defines the Δr = 0.25 refinement of
the F4-alt relaxed-filter measurement restricted to the small-r
region r ∈ [0.25, 2.0] lu. Purpose: locate (or rule out) the
half-rise `r_½^{filt}` below r = 1.0 lu and resolve the
interpretive gap between the strict pre-registered
`Inconclusive` verdict and the structural-reading `Refuted-by-
extension` of the F4-alt execution.
**Parents:**
- `theory/ED_SC_3_4_twopoint_FilterRelaxation.md` (F4-alt
  amendment; relaxed-filter scope restriction to the
  Correlation-class channel).
- `theory/ED_SC_3_4_twopoint_FilterRelaxation_Driver.md`
  (F4-alt canonical driver spec; inherited wholesale with the
  single change of the r-grid).
- F4-alt execution (2026-04-23;
  `outputs/ed_sc_3_4_twopoint_relaxed/correlation_twopoint_summary.json`):
  **Verdict Inconclusive** at the 10-point Δr = 0.5 grid; 8 of
  10 bins admissible; `C_ensemble(r) ≈ 2.0` across all
  admissible bins from r = 1.0 to r = 5.0 lu.
- `theory/GR_SC_1_7_Redshift_MotifStatistics.md` (tenth-pass
  pooled-R2 prediction `r_½^{filt}/r_½^{unfilt} = 0.80 ± 0.05`).
- `theory/ED_SC_3_4_twopoint_Driver.md` §3 (canonical F4 driver
  architecture — reused verbatim).
- `theory/GR_SC_2_0_Consolidation_Amendment.md` §4 (ensemble-
  vs-single-seed guardrail).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post F4-alt execution).

---

## 1. Motivation

### 1.1 F4-alt execution outcome (recap)

The F4-alt relaxed-filter execution
(`analysis/scripts/ed_sc_3_4_twopoint_correlation_relaxed.py`,
2026-04-23) produced abundant pair density and 8 of 10 admissible
bins, but `C_ensemble(r)` saturates at ≈ 2.0 across the entire
admissible r range:

| r (lu) | N_pairs | C_ensemble | CI |
|---:|---:|---:|---|
| 1.0 | 1,473 | **2.044** | [1.997, 2.095] |
| 1.5 | 1,126 | **2.042** | [1.985, 2.101] |
| 2.0 | 3,154 | **2.024** | [1.990, 2.060] |
| 3.0 | 4,614 | **1.963** | [1.933, 1.994] |
| 3.5 | 2,153 | **2.022** | [1.979, 2.065] |
| 4.0 | 4,412 | **1.980** | [1.950, 2.009] |
| 4.5 | 2,105 | **2.043** | [2.003, 2.084] |
| 5.0 | 5,427 | **2.042** | [2.017, 2.068] |

Every admissible bin has `C_ensemble ∈ [1.96, 2.05]` — already
at the uncorrelated asymptote `C(∞) = 2`. No C(r) = 1 crossing
exists in the pre-registered r-grid.

### 1.2 The interpretive gap

Two readings of this result are both defensible:

- **Strict verdict:** `Inconclusive` — the driver's pre-
  registered verdict logic returns this when no C(r) = 1 crossing
  is found in the r-grid range. The literal state of the
  measurement.
- **Structural reading:** `Refuted-by-extension` — if the
  half-rise `r_½^{filt}` must lie below r = 1.0 lu (the smallest
  admissible bin where C = 2.04 already), then:
  - `r_½^{filt} < 1.0` → ratio `< 1.0 / 1.7575 = 0.569`.
  - The tenth-pass prediction 0.80 ± 0.05 (i.e. [0.75, 0.85]) is
    rejected: 0.569 < 0.70 falls outside the `Refuted` double
    envelope [0.70, 0.90].

### 1.3 The refinement closes the gap

The strict and structural readings diverge because the F4-alt
grid's smallest bin is r = 1.0 lu. A Δr = 0.25 refinement in
r ∈ [0.25, 2.0] gives 8 additional small-r sample points at
{0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00}, resolving:

- **If `C_ensemble(r) = 1` crossing is found** at some
  `r_½^{filt} ∈ [0.25, 2.0]`: compute the ratio and apply the
  four-way verdict taxonomy (Confirmed / Confirmed-marginal /
  Inconclusive / Refuted) per F4-driver §3.7.
- **If `C_ensemble(r) ≥ 2` everywhere** in the refined grid:
  the structural `Refuted` reading is empirically confirmed.
  The tenth-pass prediction cannot be reproduced at the F4-alt
  operating point.

This is the cleanest path to a definitive verdict.

---

## 2. Amendment

**Single parameter change** vs
`theory/ED_SC_3_4_twopoint_FilterRelaxation_Driver.md`:

### 2.1 `R_GRID` constant

```python
# F4-alt driver (relaxed):
R_GRID = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
DR_BIN = 0.5

# F4-alt-refine driver (this memo):
R_GRID = [0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00]
DR_BIN = 0.25
```

**8 points at Δr = 0.25 spanning r ∈ [0.25, 2.0] lu.**

All other parameters unchanged:

| parameter | F4-alt | F4-alt-refine |
|---|:---:|:---:|
| α_filt | 0.25 | 0.25 (unchanged) |
| N_req | 2 | 2 (unchanged) |
| ξ target | 1.7575 | 1.7575 (unchanged) |
| Snapshots per seed | 40 | 40 (unchanged) |
| Seeds | `{11, ..., 111}` | same 10-seed set |
| **R_GRID** | **Δr = 0.5, 10 points** | **Δr = 0.25, 8 points** |
| r_diag guard | 1 | 1 (unchanged) |
| Resonance windows | excluded | unchanged |
| Bootstrap resamples | 4000 | 4000 (unchanged) |
| MIN_PAIRS_ENSEMBLE | 20 | 20 (unchanged) |
| MIN_PAIRS_PER_SEED | 10 | 10 (unchanged) |
| Verdict thresholds | [0.75, 0.85] / [0.70, 0.90] | unchanged |

### 2.2 Bin-edge computation

The `r_bin_assign` function in the canonical F4 driver uses
symmetric `[r_k − Δr/2, r_k + Δr/2)` half-open intervals.
At Δr = 0.25:

- r = 0.25 bin covers `[0.125, 0.375)`.
- r = 0.50 bin covers `[0.375, 0.625)`.
- …
- r = 2.00 bin covers `[1.875, 2.125)`.

Pairs with `r < 0.125` or `r ≥ 2.125` are dropped. This means
F4-alt-refine **only measures the small-r region**; the large-r
saturation regime (r > 2.0) is already characterised by F4-alt
and is not re-measured here.

### 2.3 Expected pair-count scaling

At F4-alt, total pairs binned = 24,464 in r ∈ [0.25, 5.25);
of these, the bins at r = 1.0, 1.5, 2.0 contributed 1473 + 1126
+ 3154 = 5,753 pairs, i.e. ~24 % of total binned count landed
in the r ≤ 2.0 region. The refined Δr = 0.25 grid captures
roughly the same set of small-r pairs plus whatever sits in
r ∈ [0.125, 0.875) lu which F4-alt dropped (no 0.5-bin → 0
pairs artefact):

- **Expected per-bin counts:** ~300–1500, based on interpolating
  F4-alt's adjacent bin densities.
- **Expected 6–8 bins admissible** at the 20-pair threshold.

---

## 3. Success criteria

F4-alt-refine success is pre-registered with **two independent
verdicts** that together resolve the interpretive gap:

### 3.1 Admissibility success (primary gate)

    n_bins_admissible >= 6 (out of 8)

If fewer than 6 bins admissible, the refinement failed to
produce usable statistics; the overall verdict is
`Inconclusive-thin` and a deeper intervention (e.g. 100-seed
ensemble, or a different correlation estimator) would be
required. This mirrors the F4-alt primary success criterion
but scaled to the 8-point grid.

### 3.2 Half-rise verdict (secondary gate)

Given admissibility ≥ 6, apply the F4-driver §3.7 four-way
taxonomy:

- **Case A — C(r) = 1 crossing exists in [0.25, 2.0]:**
  compute `r_½^{filt}` via linear interpolation; compute
  ratio = `r_½^{filt} / 1.7575`; apply thresholds
  `[0.75, 0.85]` → Confirmed, `[0.70, 0.90]` → Confirmed-marginal
  or Inconclusive, outside → Refuted.
- **Case B — No crossing; all admissible bins have C ≥ 2:**
  the structural `Refuted-by-extension` reading of F4-alt is
  empirically confirmed. Verdict = **`Refuted`**. Implies the
  tenth-pass prediction 0.80 ± 0.05 does not reproduce at the
  relaxed-filter operating point; half-rise is below the
  measurement floor (r = 0.25 lu) or does not exist as a
  well-defined quantity at this filter density.
- **Case C — No crossing; some admissible bins have C < 2:**
  the correlation function is non-monotone or has structure not
  anticipated by the tenth-pass Rayleigh-based derivation.
  Verdict = **`Inconclusive-nonmonotone`**. Triggers a fresh
  scoping memo on the Correlation-class functional form.

### 3.3 Strong-cushion verdict

If Case A yields Confirmed with a bootstrap 16–84 band that does
not straddle any threshold (similar to F4-alt verdict logic), the
verdict is the unqualified `Confirmed`. Otherwise
`Confirmed-marginal` applies.

---

## 4. Outputs

All three files under the new directory
**`outputs/ed_sc_3_4_twopoint_relaxed_refine/`** to keep the
refinement artefacts separate from the canonical F4-alt outputs:

- `correlation_twopoint_table.csv` — 8 rows, one per r-bin;
  same 14 columns as F4-alt.
- `correlation_twopoint_per_seed.csv` — 80 rows (= 8 r-bins ×
  10 seeds); same 7 columns.
- `correlation_twopoint_summary.json` — same master payload
  structure as F4-alt; includes the `filter_relaxation_amendment`
  top-level key inherited from F4-alt (noting the canonical
  N_req = 4 vs F4-alt N_req = 2 vs F4-alt-refine N_req = 2),
  plus a new top-level key:

```json
"filter_relaxation_refinement": {
  "parent_f4_alt_r_grid": [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0],
  "refined_r_grid": [0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00],
  "dr_bin_refined": 0.25,
  "motivation": "F4-alt C_ensemble saturates at ~2.0 across r ∈ [1.0, 5.0]; half-rise (if exists) must lie below 1.0 lu; see theory/ED_SC_3_4_twopoint_FilterRelaxation_Refine.md",
  "parent_f4_alt_artefact": "outputs/ed_sc_3_4_twopoint_relaxed/correlation_twopoint_summary.json",
  "parent_f4_alt_verdict": "Inconclusive (no C(r)=1 crossing in Δr=0.5 grid)"
}
```

---

## 5. Deliverables

### 5.1 Complete refinement spec

`analysis/scripts/ed_sc_3_4_twopoint_correlation_relaxed_refine.py`
(to be written in a subsequent turn) is the F4-alt driver
copied verbatim with:

- `R_GRID = [0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00]`.
- `DR_BIN = 0.25`.
- `R_GRID_MIN_EDGE = 0.125, R_GRID_MAX_EDGE = 2.125`.
- `OUT_DIR = outputs/ed_sc_3_4_twopoint_relaxed_refine/`.
- Summary JSON adds `filter_relaxation_refinement` top-level
  key per §4.

No other code changes. All pipeline logic — calibration pre-
pass, evolution, motif extraction with positions, pair
enumeration, r-binning, Pearson + Spearman estimators,
bootstrap, per-seed CoV, half-rise linear interpolation,
bootstrap-propagated half-rise, verdict taxonomy — inherited
verbatim from F4-alt (and via F4-alt from F4 canonical).

### 5.2 Pre-registered falsifier logic

Inherited F4-driver §3.7 taxonomy with **one new case (Case C
`Inconclusive-nonmonotone`)** per §3.2:

- **Confirmed:** ratio ∈ [0.75, 0.85] with bootstrap band
  respecting thresholds.
- **Confirmed-marginal:** ratio ∈ [0.75, 0.85] but bootstrap
  band straddles a threshold.
- **Inconclusive:** ratio ∈ [0.70, 0.75) ∪ (0.85, 0.90].
- **Refuted:** ratio ∉ [0.70, 0.90] (explicit crossing found
  outside double envelope) **OR** Case B (no crossing, C ≥ 2
  throughout admissible bins).
- **Inconclusive-nonmonotone:** no crossing, but C < 2
  somewhere in admissible bins.
- **Inconclusive-thin:** `n_bins_admissible < 6` (primary gate
  fails).

### 5.3 Changelog

- **Rev. 1 (2026-04-23, this memo):** opens F4-alt-refine as the
  Δr = 0.25 small-r refinement of the F4-alt relaxed-filter
  measurement. Motivated by F4-alt's `C_ensemble(r) ≈ 2.0`
  saturation across r ∈ [1.0, 5.0] which renders the strict
  `Inconclusive` verdict interpretively ambiguous (structural
  reading is `Refuted-by-extension`). Refined r-grid `{0.25,
  0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00}` at Δr = 0.25
  samples the region where the half-rise (if any) must live per
  tenth-pass 0.80 ratio. Two-gate verdict structure: (1)
  admissibility ≥ 6 of 8, (2) half-rise interpolation with
  three resolution cases (A crossing exists → four-way verdict;
  B no crossing with C ≥ 2 → Refuted; C non-monotone →
  Inconclusive-nonmonotone). Scope-restricted to
  C_redshift(r) measurement channel (inherited from F4-alt
  scope restriction); canonical operating point unchanged. No
  driver written in this memo; driver
  `analysis/scripts/ed_sc_3_4_twopoint_correlation_relaxed_refine.py`
  and F4-alt-refine-execution are flagged as downstream work.
