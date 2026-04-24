# ED-SC 3.4 Two-Point — Filter Relaxation Amendment (F4-alt)

**Status:** Scope amendment. Proposes a relaxed motif filter
(`N_req = 2` at canonical `α_filt = 0.25`) for the F4 two-point
correlation measurement **only**. The canonical filter
(`N_req = 4, α_filt = 0.25`) remains the authoritative operating
point for all other ED-SC / GR-SC claims; this amendment scope
is restricted to the C_redshift(r) measurement channel.
**Parents:**
- `theory/ED_SC_3_4_twopoint_Scoping.md` (F4 pre-registration).
- `theory/ED_SC_3_4_twopoint_Driver.md` (F4 driver spec).
- F4 canonical-filter execution (2026-04-23; `Inconclusive`
  verdict via pair-count sparsity):
  `outputs/ed_sc_3_4_twopoint/correlation_twopoint_summary.json`.
- `theory/GR_SC_1_7_Redshift_MotifStatistics.md` (tenth-pass
  pooled-R2 half-rise compression prediction
  `r_½^{filt}/r_½^{unfilt} = 0.80 ± 0.05`).
- `theory/GR_SC_2_0_Consolidation_Amendment.md` (sixteenth-pass
  ensemble-vs-single-seed guardrail, inherited).
- `theory/ED_SC_3_3_rev2_FilterGeometry.md` (ED-SC 3.3 full-sweep
  pair-count statistics; evidence base for the 5–6× motif
  density at `N_req = 2`).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post F4 canonical-filter execution).

---

## 1. Motivation

The F4 driver
(`analysis/scripts/ed_sc_3_4_twopoint_correlation.py`) executed
2026-04-23 at the canonical filter `(α_filt = 0.25, N_req = 4)`
with 10-seed × 40-snapshot ensemble. Result: **Verdict =
Inconclusive, reason = "No C(r) = 1 crossing found in r_grid
range."** The underlying mechanism is pair-count sparsity:

| quantity | canonical-filter F4 value |
|---|---:|
| N_motifs total (10 seeds × 40 snaps) | 849 |
| motifs per snapshot (avg) | **2.12** |
| pair candidates generated | 958 |
| pair candidates binned (r ∈ [0.25, 5.25) lu) | **51** (5.3 %) |
| pair candidates unbinned (r > 5.25 lu) | 907 (94.7 %) |
| r-bins with N_pairs ≥ 20 (ensemble admission) | **0 of 10** |
| r-bins with Spearman-defined (N_pairs ≥ 3) | 6 of 10 |

**Every r-bin failed the ensemble 20-pair minimum**, so all
`C_ensemble(r)` values are `None`; the half-rise cannot be
interpolated; no verdict on the 0.80 ± 0.05 pooled-R2 prediction
is possible.

### Why the canonical filter is too sparse for C(r)

Two compounding facts:

1. **Canonical filter admits ~2 motifs per snapshot** under the
   `N_req = 4` quorum — the strictest of the ED-SC 3.3 settings.
   Per-snapshot pair count averages `(2 · 1) / 2 = 1`.
2. **Pair separations on a 64² torus with sparse uniform motifs
   land dominantly at large r** — mean min-image distance is
   ~25 lu; only ~5 % of pairs fall below 5.25 lu.

Product: ~50–60 pairs in the pre-registered r ∈ [0.5, 5.0] range
across the entire 10-seed × 40-snap ensemble. Insufficient for
bootstrap; insufficient for bin-level estimators.

**This is not a measurement failure.** The F4 driver and
methodology are correct; the measurement substrate (canonical
filter density) simply cannot support the half-rise resolution
that GR-SC 1.7's pooled-R2 prediction targets. A relaxed-filter
amendment is required to recover statistical power.

### Why GR-SC 1.7's prediction cannot be retracted

The tenth-pass `r_½^{filt}/r_½^{unfilt} = 0.80 ± 0.05` prediction
was derived from the kinematic acoustic-metric analysis under the
assumption of dense motif sampling (GR-SC 1.7 §3). It targets a
scale `r_½^{filt} ≈ 0.80 · ξ_canonical = 1.406 lu` — precisely
the regime where canonical filter admits few pairs. The
prediction is not wrong at the tenth-pass level; it simply cannot
be tested at the canonical filter's motif density.

---

## 2. Amendment

**Single change:** replace `N_req = 4` with `N_req = 2`.

All other parameters remain canonical:

| parameter | canonical F4 | F4-alt (this memo) |
|---|:---:|:---:|
| α_filt | 0.25 | 0.25 (unchanged) |
| **N_req** | **4** | **2** |
| ξ target | 1.7575 | 1.7575 (unchanged) |
| L_ray | 1.08 · ξ | 1.08 · ξ (unchanged) |
| Snapshots per seed | 40 | 40 (unchanged) |
| Seeds | `{11, 22, ..., 111}` | same 10-seed set |
| r-grid | {0.5 … 5.0} Δr=0.5 | unchanged |
| r_diag guard | `r_diag = 1` | unchanged |
| Resonance windows | A, B excluded | unchanged |
| Bootstrap resamples | 4000 | unchanged |
| Verdict thresholds | 0.80 ± 0.05 | unchanged |

**Expected motif-density increase.** From ED-SC 3.3 rev. 2
filter-geometry sweep (executed 2026-04-23,
`outputs/ed_sc_3_3/filter_geometry_summary.json`) at canonical
L_ray:

| cell | N_pool (5-point hinge sub-sweep) | per-snap avg (approx) |
|---|---:|---:|
| α_filt = 0.25, **N_req = 4** (canonical) | 164 | ~33 per hinge point |
| α_filt = 0.25, **N_req = 3** | 1189 | ~238 per hinge point |
| α_filt = 0.25, **N_req = 2** | **3985** | ~797 per hinge point |

**Motif density at N_req = 2 is ~24× canonical per hinge point**
(5 hinge points × 33 motifs = 165 vs 3985). Converting to the
F4 operational context (40 snapshots per seed, 10 seeds): the
per-snap motif count scales from ~2 to **~50–60**, giving
per-snap pair count from ~1 to **~1200–1800**. Across 400
snapshots: ~500,000 pair candidates vs the canonical ~1000.

Even accounting for the 5–6 % of pairs that fall in r ≤ 5.25 lu
(canonical geometry distribution), this gives **~25,000–30,000
pairs in the r-grid range** — three orders of magnitude above
the 20-pair-per-bin admission threshold, and sufficient for
tight bootstrap CIs on `C_ensemble(r)`.

### Scope restriction

**F4-alt is restricted to the C_redshift(r) measurement
channel.** The canonical operating point
`(α_filt = 0.25, N_req = 4)` remains the authoritative ED-SC /
GR-SC reference for:

- ED-SC 3.1 rev. 3 canonical pool statistics.
- ED-SC 3.3.x / 3.4 invariance claims.
- GR-SC 1.1 Ratio-class predictions.
- GR-SC 1.2 Quadratic-class predictions.
- GR-SC 1.3 Rayleigh-class predictions.
- Pooled-R2 anchors for `r*`, `ℛ_W`, `κ/(|μ₁|σ₁)`.

Only the Correlation-class `C_redshift(r)` row in GR-SC 1.0 §5
uses the F4-alt relaxed filter, and that row **must carry an
explicit note** that the measurement is not at the canonical
operating point.

---

## 3. Measurement architecture

Architecture is otherwise identical to
`theory/ED_SC_3_4_twopoint_Driver.md` §3. All data structures,
guards, estimators, bootstrap, and verdict logic carry over
verbatim. The only code change required in the driver is
**replacing `N_REQ = 4` with `N_REQ = 2`** in the constants
block.

Diagnostic additions for F4-alt:

- **Motif-density comparison diagnostic:** report per-seed motif
  count at F4-alt vs the F4 canonical-filter value. Expected:
  5–6× more motifs per seed under N_req = 2 at 40-snapshot
  pooling.
- **Pair-density success metric:** the number of r-bins meeting
  the 20-pair ensemble threshold must be ≥ 8 of 10 for F4-alt
  to be considered a successful amendment (primary criterion).
- **Half-rise location verdict** applies per the F4-driver
  §3.7 taxonomy (Confirmed / Confirmed-marginal / Inconclusive /
  Refuted) using the same 0.80 ± 0.05 tenth-pass prediction.

---

## 4. Outputs

All F4-alt outputs live under the new directory
**`outputs/ed_sc_3_4_twopoint_relaxed/`** to avoid collision with
the canonical F4 output files. The three-file structure mirrors
F4 exactly:

- `correlation_twopoint_table.csv` — ensemble per-r-bin (10 rows).
- `correlation_twopoint_per_seed.csv` — per-seed per-r-bin
  (100 rows).
- `correlation_twopoint_summary.json` — master aggregate with
  verdict.

Summary JSON contents are identical to the F4-driver §5 spec
plus one additional top-level key:

    "filter_relaxation_amendment": {
      "canonical_N_req": 4,
      "F4_alt_N_req": 2,
      "motivation": "canonical filter pair-count sparsity;
        see theory/ED_SC_3_4_twopoint_FilterRelaxation.md",
      "scope_restriction": "C_redshift(r) measurement only;
        does not affect canonical operating point"
    }

---

## 5. Deliverables

### 5.1 Complete scope amendment

This memo is itself the complete scope amendment. The F4-alt
driver **`analysis/scripts/ed_sc_3_4_twopoint_correlation_relaxed.py`**
(to be written in a subsequent turn) implements the amendment
by copying the F4 canonical driver verbatim with two changes:

- `N_REQ = 2` (constants block).
- `OUT_DIR = ".../outputs/ed_sc_3_4_twopoint_relaxed/"`.
- `summary JSON` adds the `filter_relaxation_amendment` field.

All other code identical — same seed set, same calibration,
same evolution, same pair enumeration, same bootstrap, same
verdict logic.

### 5.2 Documentation of the canonical-filter inconclusive verdict

The canonical-filter F4 execution outcome (Verdict:
`Inconclusive` via pair-count sparsity) is documented as the
**canonical-filter result** in:

- `outputs/ed_sc_3_4_twopoint/correlation_twopoint_summary.json`
  (raw artefact; unchanged).
- The `C_redshift(r)` row of GR-SC 1.0 §5 must be annotated
  with: "**Inconclusive at canonical operating point**
  (α_filt = 0.25, N_req = 4) per F4 execution 2026-04-23
  — pair-count sparsity. F4-alt relaxed-filter measurement
  pending per
  `theory/ED_SC_3_4_twopoint_FilterRelaxation.md`."
- GR-SC 2.0 Consolidation Amendment §6 taxonomy table row for
  Correlation class must similarly note the canonical-filter
  inconclusive + F4-alt pending status.

These pointer updates are **flagged but not applied in this
memo**; they are deferred to the F4-alt-integration consolidation
pass that will follow the F4-alt execution.

### 5.3 Follow-up memos

Three downstream memos pre-registered:

- **F4-alt-driver** (next turn): builds
  `analysis/scripts/ed_sc_3_4_twopoint_correlation_relaxed.py`
  per §5.1.
- **F4-alt-execution:** report summary after driver run;
  verdict against the 0.80 ± 0.05 pooled-R2 prediction.
- **F4-alt-integration:** update GR-SC 1.0 §5 `C_redshift(r)`
  row + GR-SC 2.0 Consolidation Amendment §6 + project memory
  / orientation docs with the F4-alt verdict. If Confirmed:
  close the Correlation-class row as quantitatively evaluated
  at the relaxed filter. If Refuted: open a re-scoping memo
  for the pooled-R2 prediction or the F4 methodology itself.

---

## 6. Changelog

- **Rev. 1 (2026-04-23, this memo):** opens F4-alt as a filter-
  relaxation amendment to the F4 methodology for the sole
  purpose of C_redshift(r) measurement. Replaces `N_req = 4`
  with `N_req = 2` at otherwise-canonical parameters; expected
  motif-density increase ~24× per hinge point (5–6× per-snap);
  expected pair-density increase ~500× in the r-grid range.
  Scope restriction: F4-alt applies **only** to the
  Correlation-class measurement channel; does not affect the
  canonical operating point, ED-SC 3.x invariance claims, or
  GR-SC 1.1 / 1.2 / 1.3 prediction layers. Documents the
  canonical-filter `Inconclusive` verdict as the authoritative
  result at canonical density; F4-alt provides the quantitative
  test at relaxed density. Three follow-up memos flagged:
  F4-alt-driver, F4-alt-execution, F4-alt-integration. No
  driver written in this memo; amendment is scope-only.
