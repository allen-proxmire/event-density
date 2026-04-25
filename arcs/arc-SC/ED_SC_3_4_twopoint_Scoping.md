# ED-SC 3.4 Two-Point — Correlation-Class Scoping (F4)

**Status:** Pre-registration. Scope-only memo. Opens the F4
program — the last remaining sub-arc of the fifteenth-pass GR-SC
prediction layer. Establishes the measurement architecture,
r-grid, bootstrap strategy, and uncertainty structure for
extracting the two-point motif-ratio correlation function
`C_redshift(r)` from ED motif evolution. Driver and execution
are deferred to follow-up memos.
**Parents:**
- `theory/GR_SC_1_7_Redshift_MotifStatistics.md` (tenth-pass
  arc; defines `C_redshift(r) = 2[1 − ξ_φ(r)/σ_0²]` with rigid
  endpoints `C(0) = 0` and `C(∞) = 2`; pooled-R2 half-rise
  compression `r_½^{filt} / r_½^{unfilt} = 0.80 ± 0.05`).
- `theory/GR_SC_1_0_MotifCurvatureInvariants.md` §5 (`C_redshift`
  row is the last deferred row; F4 unlocks it).
- `theory/GR_SC_2_0_Consolidation.md` +
  `theory/GR_SC_2_0_Consolidation_Amendment.md` (five-class
  taxonomy; Correlation class as the one remaining class
  awaiting quantitative characterisation).
- `theory/ED_SC_3_4_XiCalibration.md` + execution (S2
  calibration; structural precedent for the ED-SC 3.4.x scan
  pattern).
- `theory/ED_SC_3_4_sigma1_Calibration.md` +
  `theory/ED_SC_3_4_sigma1_MultiSeed.md` (σ₁ calibration;
  methodological precedent for multi-seed uncertainty and the
  ensemble-vs-single-seed guardrail).
- `theory/ED_SC_3_3_10_ArcClosure.md` §3 (four-clause invariance
  statement; r_diag = 1 canonical window).
- `theory/ED_SC_3_0_rev3_ScopePatch.md` (size-dependent S-F2,
  verdict taxonomy, shell-class validity window, geometric
  quorum).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post-sixteenth-pass; final open sub-arc
of the fifteenth-pass GR-SC layer).

---

## 1. Purpose

The GR-SC 1.0 §5 authoritative invariant table has one remaining
deferred row: **`C_redshift(r)` in the Correlation class**.
F4 opens the scoping work to compute it.

F4's specific goals:

- **Measure the two-point motif-ratio correlation function**
  `C(r)` at the certified canonical operating point, across a
  pre-registered r-grid spanning the sub-Regime-I, Regime-I,
  and super-Regime-I separations.
- **Compare against the tenth-pass GR-SC 1.7 prediction** of
  half-rise compression `r_½^{filt}/r_½^{unfilt} = 0.80 ± 0.05`
  — the cleanest falsifier in the GR-SC arc (mobility- and
  σ_0-universal).
- **Establish the uncertainty structure** for correlation-
  function observables, which is substantively different from
  single-point observables (ensemble / per-realisation /
  calibration / model bands all acquire different meanings at
  the two-point level).
- **Inherit the ensemble-vs-single-seed guardrail** from the
  sixteenth-pass (GR-SC 2.0 Amendment §4): taxonomy-level
  claims about `C_redshift(r)` must derive from ensemble
  measurements; single-seed or single-ξ single-r diagnostics
  are acceptable for flagging but not for promotion.

This memo is scope-only. Driver (F4-driver) and execution
(F4-execution) are separate follow-up memos.

---

## 2. Background

### 2.1 GR-SC 1.7 definition

From `theory/GR_SC_1_7_Redshift_MotifStatistics.md`:

    C_redshift(r) = 2 [1 − ξ_φ(r) / σ_0²]

where `ξ_φ(r) = ⟨φ(x)·φ(x+r)⟩` is the two-point autocorrelation
of the field `φ` (equivalently the motif-ratio ρ at two
separated motif centres), `σ_0² = ξ_φ(0) = Var(φ)` is the
variance at zero separation.

Rigid endpoints:

- `C(0) = 2[1 − 1] = 0`.
- `C(∞) = 2[1 − 0] = 2` (assuming `ξ_φ(r) → 0` at large r).

**Half-rise scale** `r_½^{filt}`: the separation at which
`C_redshift(r) = 1`, equivalently where `ξ_φ(r) = σ_0² / 2`.
This is the filtered-motif equivalent of the bulk-field
autocorrelation half-decay (which GR-SC 1.7 calls
`r_½^{unfilt}`).

**Tenth-pass pooled-R2 prediction:**

    r_½^{filt} / r_½^{unfilt} = 0.80 ± 0.05

— mobility- and σ_0-universal per GR-SC 1.7. This is the
cleanest single-number GR-SC falsifier.

### 2.2 ED-SC 3.x motif geometry for two-point sampling

Each admitted motif at the canonical filter has:

- A **spatial position** `(i, j)` on the 64² periodic lattice
  (the saddle centre from `fr.find_morse_saddles`).
- A **ρ value** = `λ_neg / λ_pos` (the Hessian eigenvalue ratio,
  i.e. S1 at per-motif level).
- A **T value** = `λ_neg + λ_pos` (the Hessian trace, per F2 /
  F3-verify).

For a two-point correlation measurement:

- Pairs `(m_1, m_2)` of admitted motifs are considered.
- Separation `r_{m_1, m_2} = ||pos_{m_1} − pos_{m_2}||` with
  periodic-boundary distance (minimum image convention on the
  64² torus).
- The correlation statistic at separation r is accumulated over
  all pairs binned into the r-bin.

### 2.3 Sixteenth-pass guardrail inherited

From GR-SC 2.0 Amendment §4: **taxonomy-level claims about
`C_redshift(r)` must derive from ensemble measurements where
possible.** F4 uses:

- **Multi-seed ensemble** (10 seeds, mirroring the F2 seed set
  `{11, 22, 33, 44, 55, 66, 77, 88, 99, 111}` or equivalent
  fresh 10 seeds at canonical ξ).
- **40-snapshot per seed** at canonical ξ = 1.7575 (matches
  the ED-SC 3.4.x snapshot cadence).
- **Cross-seed pairs pooled** for the canonical `C(r)` curve;
  per-seed pair pools emit the per-realisation spread band.

---

## 3. Measurement architecture

### 3.1 r-grid

Pre-registered 10-point grid spanning the key physical scales:

    r ∈ {0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0} lu.

Rationale:

- **r = 0.5 lu:** sub-motif scale; expected `C(r) ≈ 0` (motifs
  do not overlap at half the nearest-neighbour distance).
- **r = 1.0–2.0 lu:** characteristic motif-geometry scale; the
  filter's `L_ray = 1.898 lu` at canonical ξ lives here.
  Expected rising `C(r)`; half-rise `r_½^{filt}` likely in this
  band.
- **r = 2.5–3.5 lu:** post-filter-geometry scale; `C(r)` should
  be approaching plateau.
- **r = 4.0–5.0 lu:** multiple motif-separations scale; `C(r)
  ≈ 2` expected (uncorrelated regime, equivalent to C(∞)).

The grid is uniform at Δr = 0.5 lu. An optional refinement to
Δr = 0.25 lu in the 0.5–3.0 range (13 points total) is flagged
as a post-execution diagnostic if the half-rise location is
poorly resolved at Δr = 0.5.

### 3.2 Sampling strategy

**Per snapshot per seed:**

1. **Motif extraction:** inherited from the ED-SC 3.4.x
   pipeline — `fr.find_morse_saddles` followed by `fr.motif_pass`
   at canonical `(α_filt = 0.25, N_req = 4, L_ray = 1.08 · ξ)`.
2. **Position and ρ recording:** for each admitted motif,
   record `(i, j, ρ)` where `(i, j)` are lattice indices and ρ
   = `λ_neg / λ_pos`.
3. **Pair enumeration:** for each pair of distinct admitted
   motifs `(m_1, m_2)`, compute the **periodic-boundary
   separation**:

        Δi = min(|i_1 − i_2|, 64 − |i_1 − i_2|)
        Δj = min(|j_1 − j_2|, 64 − |j_1 − j_2|)
        r_{m_1, m_2} = √(Δi² + Δj²).

4. **r-bin assignment:** pair `(m_1, m_2)` contributes to bin
   `k` if `r_k − Δr/2 ≤ r_{m_1, m_2} < r_k + Δr/2` where
   `Δr = 0.5 lu`.
5. **Correlation statistic:** for each pair, compute the
   **centred ρ-product**:

        x_{m_1, m_2} = (ρ_{m_1} − ρ̄) · (ρ_{m_2} − ρ̄)

   where `ρ̄` is the global pool mean (across all admitted
   motifs across all snapshots and seeds — the canonical
   S1-equivalent baseline).

**Cross-snapshot pooling:**

- Per seed, accumulate pair statistics across the 40 snapshots.
- Per r-bin, maintain the raw list of `x_{m_1, m_2}` values
  (not just the mean, for bootstrap).

**Cross-seed pooling:**

- Per r-bin, pool pair statistics across the 10 seeds for the
  **canonical ensemble estimator** `C_ensemble(r)`.
- Per seed per r-bin, compute seed-local estimator
  `C_seed(r)` for the per-realisation spread.

### 3.3 Estimator definitions

Per r-bin `k`, let `N_k` = total pair count across all seeds
and snapshots. The ensemble correlation estimator is:

    ξ̂_φ(r_k) / σ̂_0² = ⟨x_{m_1, m_2}⟩ / σ̂_ρ²

where the numerator is the mean centred-product across the r-bin
and `σ̂_ρ²` is the pooled ρ variance. Then:

    Ĉ_redshift(r_k) = 2 [1 − ξ̂_φ(r_k) / σ̂_0²].

**Per-seed seed-local estimator** `Ĉ_seed(r_k)` uses only that
seed's pair pool with the same formula.

**Half-rise determination:** `r̂_½^{filt}` = linearly
interpolated separation at which `Ĉ_redshift(r) = 1`, using
the two r-bins bracketing C(r) = 1.

### 3.4 Admissibility filters and guards

Pre-registered per GR-SC 2.0 Amendment §4 ensemble guardrail:

- **r_diag = 1 guard** (ED-SC 3.0 rev. 3): all evaluations use
  canonical ξ = 1.7575; no cross-coordinate-class data.
- **Minimum pairs per r-bin for admissibility:** N_k ≥ 20 at
  ensemble level; below this threshold, the bin is flagged
  `low-N` and its bootstrap CI is treated as wide-open
  (uninformative). Per-seed-local bins with N < 10 are not
  included in per-realisation spread computation.
- **Resonance-window guard:** all per-seed L_ray values must
  have `r_diag = 1`; canonical ξ = 1.7575 satisfies this
  structurally.
- **Ensemble-vs-single-seed rule:** `C(r)` canonical-value
  citations use the cross-seed pooled estimator; single-seed
  estimates are emitted as diagnostic only.

### 3.5 Bootstrap strategy

**Ensemble band** (calibration CI analogue):

- At each r-bin `k`, resample the pool of `N_k`
  centred-products with replacement 4000 times; compute
  `Ĉ_redshift(r_k)` for each resample; report the 16–84
  percentile band.

**Per-realisation spread** (F2 analogue):

- Compute `C_seed_i(r_k)` for each of the 10 seeds; compute
  `std(C_seed) / mean(C_seed)` across seeds at each r-bin.
  Report as CoV(r_k), analogous to the F2 σ₁_std CoV = 9.9 %.

**Shape model band** (F3-verify analogue):

- Correlation functions do not admit a Student-t family fit in
  the same way single-point distributions do. Instead, the
  model band captures the **estimator choice**: emit both the
  product-moment estimator (§3.3) and a **rank-correlation
  estimator** (Spearman ρ at each r-bin); the relative difference
  `|Ĉ_PM − Ĉ_rank| / Ĉ_PM` is the model-approximation band at
  each r-bin. Large discrepancies flag non-Gaussian pair
  distributions requiring a dedicated scoping-memo amendment.

**Calibration interpolation** (OLS-residual analogue): not
applicable to correlation functions in the same sense as the
ED-SC 3.4 S2 RMS residual. Replace with **r-grid-refinement
uncertainty** from the post-execution Δr = 0.25 refinement
diagnostic (if performed). Absent this diagnostic, the
calibration component is recorded as `N/A` rather than
computed.

---

## 4. Outputs

Per r-bin (10 or 13 rows depending on refinement):

- `r`, `N_pairs`, `C_ensemble(r)`, `C_ensemble_CI_lo`,
  `C_ensemble_CI_hi` (bootstrap 16–84),
  `CoV_across_seeds`, `C_rank(r)`, `model_band_rel`.
- Per-seed: `C_seed_i(r)` for i ∈ {1..10}.

Emit:

- `outputs/ed_sc_3_4_twopoint/correlation_twopoint_table.csv`
  — flat rows, one per r-bin, all ensemble columns.
- `outputs/ed_sc_3_4_twopoint/correlation_twopoint_per_seed.csv`
  — flat rows, one per (r, seed) combination.
- `outputs/ed_sc_3_4_twopoint/correlation_twopoint_summary.json`
  — master aggregate:
  - Calibration parameters, seed set, ξ canonical.
  - Per-r-bin ensemble/per-seed statistics and bootstrap arrays.
  - `r_half_filt_estimated` and its CI from bootstrap.
  - `r_half_filt_over_r_half_unfilt_ratio` vs tenth-pass
    pooled-R2 prediction 0.80 ± 0.05.
  - Pre-registered diagnostic verdict `{Confirmed, Refuted,
    Inconclusive}` on the half-rise compression prediction.
  - Low-N bin flags.
  - `C(0)` and `C(∞)` rigid-endpoint check (expected C(0) ≈ 0
    at r = 0.5 if 0.5 lu is below the filter's two-point
    resolution; C(∞) ≈ 2 at r = 5 lu if the uncorrelated
    regime has been reached).

---

## 5. Deliverables

### 5.1 Complete F4-driver specification

The driver **`analysis/scripts/ed_sc_3_4_twopoint_correlation.py`**
(to be written in F4-driver memo) will implement:

- ED-SC 3.4 canonical evolution pipeline (fixed seed per
  run, but looped over 10 canonical seeds).
- 40-snapshot motif extraction per seed with position and ρ
  recording.
- Pair enumeration with periodic-boundary distances.
- r-bin assignment at Δr = 0.5 (canonical 10-bin grid).
- Ensemble, per-seed, and bootstrap estimators per §3.5.
- CSV + JSON emission per §4.

No lattice-side innovation; the driver is a post-processing
extension of the ED-SC 3.4.x evolution pipeline.

### 5.2 Decision tree for uncertainty propagation

For any downstream citation of `C_redshift(r)` or the derived
`r_½^{filt}`:

    ┌─ ensemble-level citation? ────────────────────┐
    │                                                │
    │ yes → use ensemble bootstrap CI (§3.5)         │
    │                                                │
    │ single-realisation → use CoV band (§3.5)       │
    │                                                │
    │ half-rise compression r_½_filt / r_½_unfilt: ──┤
    │                                                │
    │   compare to 0.80 ± 0.05 from tenth-pass       │
    │   via bootstrap r_½_filt distribution          │
    │                                                │
    └───────────────────────────────────────────────┘

Uncertainty components quoted **separately**, never combined in
quadrature, in line with the κ-prediction convention from the
GR-SC 1.3 layer:

- Ensemble bootstrap CI (within-r-bin pair-resample spread).
- Per-realisation CoV (across-seed spread).
- Estimator-choice model band (PM vs rank).
- Low-N flag (binary, per r-bin).

### 5.3 Follow-up memo list

Three downstream memos pre-registered:

- **F4-driver** (`ED_SC_3_4_twopoint_Driver.md`) — explicit
  driver implementation notes; the §5.1 pipeline is made
  concrete. Written by the turn that creates
  `ed_sc_3_4_twopoint_correlation.py`.
- **F4-execution** (`ED_SC_3_4_twopoint_Execution.md`) —
  execution summary: raw numerical outputs, verdict on the
  0.80 ± 0.05 half-rise compression prediction, per-r-bin
  statistics.
- **F4-integration** (`ED_SC_3_4_twopoint_Integration.md`) —
  integrates F4 findings into `GR_SC_1_0_MotifCurvatureInvariants.md`
  §5 (`C_redshift` row update), `GR_SC_1_7_Redshift_MotifStatistics.md`
  (pooled-R2 prediction test outcome), and `GR_SC_2_0_Consolidation_Amendment.md`
  (Correlation-class amendment).

If the half-rise compression falsifier is **Refuted**, a
fourth memo `F4-alt` opens to scope an alternative two-point
observable.

---

## 6. Changelog

- **Rev. 1 (2026-04-23, this memo):** opens F4 as the
  Correlation-class scoping for the last-deferred row of
  GR-SC 1.0 §5. Pre-registers the 10-point r-grid (0.5 to
  5.0 lu at Δr = 0.5), the centred-ρ-product correlation
  estimator, the ensemble/per-seed/bootstrap uncertainty
  structure, the product-moment-vs-rank model band, the
  r_diag = 1 guard and low-N admissibility threshold, and
  the ensemble-vs-single-seed guardrail inherited from GR-SC
  2.0 Amendment §4. Tenth-pass half-rise compression
  prediction `r_½^{filt}/r_½^{unfilt} = 0.80 ± 0.05` is the
  pre-registered falsifier target. No driver, no execution;
  pure scope memo. Three follow-up memos (F4-driver,
  F4-execution, F4-integration) flagged as downstream work.
