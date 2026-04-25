# ED-SC 3.4 Two-Point — Filter Relaxation Driver Specification (F4-alt)

**Status:** Driver specification memo. Translates the F4-alt
filter-relaxation amendment (`theory/ED_SC_3_4_twopoint_FilterRelaxation.md`)
into a concrete, executable driver specification. Pairs with
`analysis/scripts/ed_sc_3_4_twopoint_correlation_relaxed.py` (to
be written in the same turn). No execution; scope-only for the
driver itself.
**Parents:**
- `theory/ED_SC_3_4_twopoint_FilterRelaxation.md` (F4-alt scope
  amendment; motivation, parameter table, scope restriction).
- `theory/ED_SC_3_4_twopoint_Driver.md` (F4 canonical driver
  spec; architecture inherited wholesale).
- `theory/ED_SC_3_4_twopoint_Scoping.md` (F4 scoping; r-grid,
  estimator definitions, uncertainty structure).
- `analysis/scripts/ed_sc_3_4_twopoint_correlation.py` (F4
  canonical driver; copied verbatim with three changes).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post F4-alt amendment).

---

## 1. Purpose

Execute the filter-relaxation amendment from
`theory/ED_SC_3_4_twopoint_FilterRelaxation.md` as a concrete
driver. The F4 canonical-filter execution (2026-04-23,
verdict **Inconclusive via pair-count sparsity**) demonstrated
that at the canonical motif filter `(α_filt = 0.25, N_req = 4)`
the two-point pair density in the r ≤ 5.25 lu range is
insufficient (51 pairs across 10 r-bins) to test the tenth-pass
GR-SC 1.7 prediction `r_½^{filt}/r_½^{unfilt} = 0.80 ± 0.05`.

This driver restores statistical power by **relaxing the
filter to N_req = 2** — expected ~24× motif-density increase
per hinge point (from ED-SC 3.3 rev. 2 sweep data), yielding
~25,000–30,000 pairs in the r-grid range (>500× the canonical
count). All other canonical parameters and all F4 driver logic
are preserved verbatim.

**The canonical operating point (N_req = 4) is not changed.**
F4-alt is scope-restricted to the C_redshift(r) measurement
channel per the amendment §2. The canonical filter remains the
authoritative ED-SC / GR-SC reference for every other claim.

---

## 2. Changes relative to canonical F4 driver

Three changes from `analysis/scripts/ed_sc_3_4_twopoint_correlation.py`:

### 2.1 `N_REQ` constant

```python
# Canonical F4 driver:
N_REQ = 4

# F4-alt driver (this memo):
N_REQ = 2
```

### 2.2 `OUT_DIR` constant

```python
# Canonical F4 driver:
OUT_DIR = os.path.join(HERE, "..", "..", "outputs", "ed_sc_3_4_twopoint")

# F4-alt driver (this memo):
OUT_DIR = os.path.join(HERE, "..", "..", "outputs",
                       "ed_sc_3_4_twopoint_relaxed")
```

### 2.3 Summary JSON: add `filter_relaxation_amendment` block

Append one top-level key to the emitted summary JSON:

```python
out["filter_relaxation_amendment"] = {
    "canonical_N_req": 4,
    "F4_alt_N_req": 2,
    "motivation": ("canonical filter pair-count sparsity "
                   "(51 pairs across 10 r-bins at canonical "
                   "N_req=4); see "
                   "theory/ED_SC_3_4_twopoint_FilterRelaxation.md"),
    "scope_restriction": ("C_redshift(r) measurement only; "
                          "does not affect canonical operating "
                          "point or any other ED-SC / GR-SC claim"),
    "canonical_F4_artefact": (
        "outputs/ed_sc_3_4_twopoint/correlation_twopoint_summary.json"),
    "canonical_F4_verdict": "Inconclusive (pair-count sparsity)",
}
```

**No other code changes.** All pipeline logic — calibration
pre-pass, 40-snapshot evolution, motif extraction with
positions, minimum-image pair distance, r-bin assignment,
Pearson and Spearman estimators, bootstrap, per-seed CoV,
half-rise linear interpolation, bootstrap-propagated half-rise,
verdict taxonomy — is inherited verbatim from the canonical F4
driver.

---

## 3. Driver architecture

Identical to `theory/ED_SC_3_4_twopoint_Driver.md` §3:

1. **Pre-flight guards** — `assert_no_resonance(XI_TARGET)`;
   create `OUT_DIR` if absent.
2. **Per-seed evolution + motif extraction** — loop over
   `SEEDS = {11, 22, 33, 44, 55, 66, 77, 88, 99, 111}`; per
   seed: 9-point IC-amplitude calibration pre-pass + monotone
   interpolation + 1-step bisection refinement; 40-snapshot
   evolution at ξ target 1.7575; extract motifs with
   `(i, j, ρ)` triples at each snapshot.
3. **Global pool statistics** — compute `ρ̄` and `σ²_ρ` across
   all admitted motifs (all seeds × all snapshots).
4. **Per-seed pair enumeration + r-binning** — within each
   snapshot, enumerate all motif pairs; compute min-image
   distance on 64² torus; assign to r-bin in
   `R_GRID = {0.5, 1.0, ..., 5.0}` at Δr = 0.5; accumulate
   `(ρ_i, ρ_j)` tuples per bin per seed.
5. **Ensemble pair pools** — concatenate per-seed pair pools
   per r-bin.
6. **Per-r-bin ensemble estimators** — Pearson `C_ensemble(r)`
   and bootstrap 16–84 CI (4000 pair-resample iterations);
   Spearman `C_rank(r)`; model-band relative
   `|C − C_rank|/|C|`. Low-N gate: `N_pairs < 20` → flagged,
   C = None.
7. **Per-seed per-r-bin estimators** — Pearson `C_seed(r)` if
   `N_pairs_seed ≥ 10`, else flagged; cross-seed CoV per r-bin.
8. **Half-rise interpolation** — linear interpolation of
   `C_ensemble(r) = 1` between bracketing r-bins; bootstrap
   over the 4000 resampled arrays; ratio = `r_half_filt /
   r_half_unfilt` where `r_half_unfilt = XI_CANONICAL = 1.7575`.
9. **Verdict taxonomy** — `{Confirmed, Confirmed-marginal,
   Inconclusive, Refuted}` per F4-driver §3.7 thresholds
   `[0.75, 0.85]` / `[0.70, 0.90]`.
10. **Emit outputs** per §5.

---

## 4. Diagnostics

F4-alt adds three pre-registered diagnostic reports to the
summary JSON (beyond those already in the F4 canonical driver):

### 4.1 Motif-density comparison

Per seed, report:

- `N_motifs_total_F4_alt`: count emitted by F4-alt (expected
  ~400–600 per seed at N_req = 2, vs ~70–96 canonical).
- `N_motifs_density_ratio`: `N_F4_alt / N_canonical_F4`.
  Expected: 5–6× per-seed.

Aggregate comparison:

- `ensemble_N_motifs_F4_alt` vs canonical F4 value (849 total).
- `ensemble_N_pairs_F4_alt` vs canonical F4 value (958 total
  pair candidates; 51 binned).

### 4.2 Pair-density success criterion

**Primary F4-alt success metric** (pre-registered):

    n_bins_admissible = count(r_bins where N_pairs_ensemble >= 20)
    F4_alt_success = (n_bins_admissible >= 8)

If `F4_alt_success = False`, the relaxation is insufficient; a
deeper amendment (e.g., N_req = 1 or wider r-grid) would be
required. This is the primary gate before interpreting the
half-rise verdict.

### 4.3 Ensemble-vs-single-seed guardrail preservation

Per sixteenth-pass GR-SC 2.0 Amendment §4, taxonomy-level
claims on C_redshift(r) must derive from ensemble measurements.
F4-alt preserves this:

- Canonical ensemble estimator uses cross-seed pooled pairs.
- Per-seed local estimators are emitted as diagnostic only.
- The verdict against the pooled-R2 prediction is made on the
  ensemble estimator, never on a single-seed estimate.

---

## 5. Outputs

All three files under the new directory
`outputs/ed_sc_3_4_twopoint_relaxed/`:

- `correlation_twopoint_table.csv` — 10 rows, one per r-bin;
  same 14 columns as canonical F4 (r_target, N_pairs_ensemble,
  C_ensemble, C_CI_lo, C_CI_hi, C_ensemble_rank,
  model_band_rel, CoV_across_seeds, N_seeds_in_CoV,
  N_pairs_per_seed_mean, low_N_ensemble, low_N_any_seed,
  Spearman_undefined, bootstrap_iterations).
- `correlation_twopoint_per_seed.csv` — 100 rows, one per
  (seed, r-bin); same 7 columns (seed, r_target, N_pairs_seed,
  C_seed, C_seed_low_N, xi_seed, L_ray_seed).
- `correlation_twopoint_summary.json` — same master payload as
  canonical F4 plus the `filter_relaxation_amendment` top-level
  key per §2.3.

---

## 6. Deliverables

### 6.1 Complete driver specification

`analysis/scripts/ed_sc_3_4_twopoint_correlation_relaxed.py`
implements §2–§5 verbatim. Structural precedent: copy the
canonical F4 driver `ed_sc_3_4_twopoint_correlation.py` with
exactly the three changes enumerated in §2.

Expected wall time: **~50–60 s** (evolution cost dominates;
pair enumeration grows from O(2² × 40 × 10) = ~1.6 K ops to
O(50² × 40 × 10) = ~1 M ops, still sub-second with numpy;
bootstrap of 10 bins × 4000 resamples × larger-N arrays is the
next-largest cost at ~5 s).

### 6.2 Pre-registered falsifier logic

Verdict taxonomy inherited verbatim from F4-driver §3.7:

- **Confirmed:** ratio ∈ [0.75, 0.85] (tenth-pass 0.80 ± 0.05 band).
- **Confirmed-marginal:** ratio ∈ [0.75, 0.85] but bootstrap 16–84
  straddles a threshold.
- **Inconclusive:** ratio ∈ [0.70, 0.75) ∪ (0.85, 0.90]
  (marginal band) OR no C(r) = 1 crossing found OR primary
  success criterion `n_bins_admissible < 8` fails.
- **Refuted:** ratio ∉ [0.70, 0.90] (outside double envelope).

The primary success criterion from §4.2 is pre-registered to
block verdict interpretation: if F4-alt does not itself clear
the 8-of-10 admissibility threshold, the verdict is
`Inconclusive` regardless of the half-rise interpolation.

### 6.3 Changelog

- **Rev. 1 (2026-04-23, this memo):** provides the full F4-alt
  driver specification. Three localised changes vs canonical
  F4 driver: `N_REQ = 2`, `OUT_DIR = outputs/ed_sc_3_4_twopoint_relaxed/`,
  `filter_relaxation_amendment` JSON block. All other pipeline
  logic (calibration pre-pass, evolution, motif extraction,
  pair enumeration, r-binning, estimators, bootstrap, CoV,
  half-rise, verdict) inherited verbatim. Primary success
  criterion (≥ 8 of 10 r-bins admissible) pre-registered as
  the verdict gate. Driver
  `analysis/scripts/ed_sc_3_4_twopoint_correlation_relaxed.py`
  to be written in the same turn as this memo per the
  pre-registered scoping-then-driver chain.
