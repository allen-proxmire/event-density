# GR-SC 1.3 — Rayleigh-Class Scoping

**Status:** Scoping memo. Establishes admissibility criteria,
interpretive rules, and a decision tree for evaluating the
Rayleigh-class invariant `κ` given the ED-SC 3.4-σ₁ calibration
findings. **Does NOT compute κ.** A follow-up memo (GR-SC 1.3
rev. 2, or a dedicated 1.3-Predictions memo) will execute the
quantitative κ evaluation once the scoping questions below are
resolved.
**Parents:**
- `theory/ED_SC_3_4_sigma1_Calibration.md` + execution
  `outputs/ed_sc_3_4_sigma1/sigma1_calibration_summary.json`
  (σ₁ calibration; three diagnostic findings).
- `theory/GR_SC_1_0_MotifCurvatureInvariants.md` §5 (authoritative
  table row for `κ` marked "awaits ED-SC 3.4-σ₁ scan").
- `theory/GR_SC_1_5_HorizonKappa_MotifStatistics.md` (tenth-pass
  arc; defines `κ` as Rayleigh-distributed with scale
  `|N̂'|σ_1/(2√2)`; pooled-R2 anchor `κ/(|μ₁|σ_1) = 0.52 ± 0.05`).
- `theory/GR_SC_1_8_EIT_Extremal_ErrorBudget.md` (integration memo;
  `σ_1/κ_M^det < 0.036` clearance target — becomes numerically
  actionable once κ is evaluated).
- `theory/GR_SC_1_0_EinsteinTensor_MotifStatistics.md` and
  `theory/GR_SC_2_0_Consolidation.md` (tenth-pass Trace-Gaussian-
  class rigid-zero claim on `F̄`, `tr(G^ij)`, `R`; challenged by
  the ED-SC 3.4-σ₁ median_T finding).
- `theory/GR_SC_1_1_RaychaudhuriClass_Predictions.md` and
  `theory/GR_SC_1_2_QuadraticClass_Predictions.md` (prior
  quantitative layers; structural precedent for what this memo
  defers).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post ED-SC 3.4-σ₁ execution).

---

## 1. Purpose

ED-SC 3.4-σ₁ calibrated the Hessian-trace spread `σ₁(ξ)` across
the canonical r_diag = 1 window, producing the calibration curve
needed for Rayleigh-class predictions. **Two of the three
pre-registered diagnostic checks in ED-SC 3.4-σ₁ §7 failed**:

- **Rigid-zero check failed** at 7 of 9 ξ points: pool-level
  `median(T_motif)` is positive (≈ `+0.0008`) with 16–84 CI
  strictly above zero from ξ = 1.70 upward. The tenth-pass
  Trace-Gaussian-class claim of a **rigidly zero median** on
  `F̄`, `tr(G^ij)`, `R` does not reproduce at the ED-SC motif-
  filter level under canonical parameters.
- **Gaussianity check failed** at 6 of 9 ξ points: `σ₁_std`
  systematically exceeds `σ₁_IQR_proxy = IQR/1.349` by 10–19 %,
  with the deviation growing monotonically in ξ. The `T_motif`
  distribution is **heavy-tailed**, not Gaussian, at the upper
  6 ξ points.

The third diagnostic (r_diag excursions) passed cleanly (empty
list), confirming that the scan stayed inside the canonical
shell class.

**Consequence.** The tenth-pass GR-SC 1.5 derivation of
`κ = Rayleigh-distributed with scale |N̂'|σ_1/(2√2)` was made
**under a Gaussian-trace assumption** and invoked the
Trace-Gaussian-class rigid-zero identity as a symmetry input.
Both assumptions are now empirically violated at the motif-
filter resolution where ED-SC 3.x measures. Before κ can be
quoted as a quantitative prediction, four scoping questions must
be resolved. GR-SC 1.3 pre-registers those questions, provisional
rules, and a decision tree.

This memo is **scoping-level**: no κ value is emitted here.

---

## 2. Inputs from ED-SC 3.4-σ₁

Verbatim from `outputs/ed_sc_3_4_sigma1/sigma1_calibration_summary.json`:

### 2.1 σ₁ calibration curves

**Standard-deviation-based `σ₁_std(ξ)`:**

- Fit: `σ₁_std(ξ) = 0.000114 + 0.002876·ξ`
- R² = **0.880** (strong linear trend)
- RMS residual = 0.000126
- Value at `ξ_canonical = 1.7575`: **`σ₁_std ≈ 0.00517`**
  (fit) / **0.00514** (nearest grid, ξ = 1.75 or 1.80)
- Range across scan: `[0.00483, 0.00579]`, total variation
  19.1 % of mean (just under 20 % flat threshold; the trend is
  real but magnitude is small)
- Trend direction: `positive`

**IQR-proxy-based `σ₁_IQR_proxy(ξ) = IQR(T_motif) / 1.349`:**

- Fit: `σ₁_IQR(ξ) = 0.003853 + 0.000429·ξ`
- R² = **0.215** (much weaker trend)
- Value at `ξ_canonical = 1.7575`: `σ₁_IQR ≈ 0.00460`
- Range across scan: `[0.00445, 0.00482]`, nearly flat

### 2.2 Rigid-zero diagnostic (failed)

- 7 of 9 points fail: `median_T` 16–84 CI does not contain 0.
- Central value at ξ_canonical ≈ 1.80: `median_T ≈ +0.00110`,
  CI `[+0.000380, +0.001433]`.
- Magnitude: `median_T / σ₁_std ≈ 0.21` at canonical ξ
  (statistically small but bootstrap-resolved).
- Pattern: positive bias at all 9 points, monotone-ish in ξ,
  no zero crossing.

### 2.3 Gaussianity diagnostic (failed)

- 6 of 9 points fail `|σ₁_std − σ₁_IQR_proxy| / σ₁_std < 0.10`
  threshold.
- At ξ_canonical: rel_diff ≈ **0.109** (10.9 %).
- Pattern: `σ₁_std > σ₁_IQR_proxy` at all 9 points, rel_diff
  growing monotonically from 0.038 (ξ = 1.60) to 0.168 (ξ = 1.95).
- Structural reading: heavy tails in `T_motif` distribution,
  getting heavier at larger ξ.

### 2.4 r_diag excursions (passed)

Empty list; all 9 points held `r_diag = 1`.

---

## 3. Questions to resolve

Four scoping questions must each receive an explicit answer
before GR-SC 1.3-Predictions can be written. This memo
pre-registers the questions; §4 proposes provisional rules; §5
states what GR-SC 1.3-Predictions will compute under the
provisional rules (contingent on acceptance).

### Q1. Which σ₁ definition is admissible for κ?

Two candidate definitions:

- **`σ₁_std`** — standard deviation of `T_motif`. The natural
  "spread" statistic when the distribution is Gaussian; also the
  natural input to a Rayleigh-scaling derivation that begins
  from `Var(T_motif)`.
- **`σ₁_IQR_proxy = IQR(T_motif) / 1.349`** — the IQR scaled by
  the Gaussian-equivalent factor. Robust to heavy tails; matches
  `σ₁_std` only when the distribution is exactly Gaussian.

At the ED-SC canonical operating point the two differ by 10.9 %
and diverge systematically with ξ. They are not interchangeable.

### Q2. Does Rayleigh scaling remain valid under heavy-tailed distributions?

The tenth-pass `GR_SC_1_5_HorizonKappa_MotifStatistics.md`
derivation begins from two premises:

- **Premise A:** The Hessian-trace field is Gaussian with
  zero mean (Trace-Gaussian-class identity).
- **Premise B:** The surface gravity `κ` on a level set of a
  Gaussian field with spectral second moment σ_1² follows the
  Rayleigh distribution with scale `|N̂'|·σ_1/(2√2)`.

ED-SC 3.4-σ₁ breaks **both** premises empirically at the motif-
filter resolution. Premise A fails by the rigid-zero diagnostic;
Premise B's Gaussian input fails by the Gaussianity diagnostic.
The question is whether the Rayleigh scaling survives as an
approximation, and if so with what correction.

### Q3. How does the non-zero trace bias affect the Rayleigh-class taxonomy?

The tenth-pass GR-SC 2.0 consolidation lists `F̄`, `tr(G^ij)`,
`R` as Trace-Gaussian-class with **rigidly zero median**. The
empirical `median_T ≈ +0.0008` at canonical ξ is small in
absolute terms but bootstrap-resolved at 7 of 9 points.

Three mutually-exclusive readings:

- **T-bias reading (a):** The tenth-pass derivation is
  incomplete; a correction term of order `O(σ₁²/N̂)` or similar
  lives at the motif-filter-population level and was not
  captured by the clean-saddle GRF analysis. `F̄`, `tr(G^ij)`,
  `R` remain approximately zero in ensemble average but have
  small positive bias; the Trace-Gaussian-class taxonomy
  stands with a footnote.
- **T-bias reading (b):** The motif-filter population is not
  the same ensemble as the tenth-pass saddle GRF; the filter
  selects a biased subset that does not inherit the symmetry
  properties of the bulk GRF. The tenth-pass rigid-zero claim
  remains true for the un-filtered GRF but false for the
  filtered pool. Trace-Gaussian-class survives as a bulk
  statement; the motif-filter quantity is a different object.
- **T-bias reading (c):** The tenth-pass derivation contains
  an error. Rigid-zero was never a true prediction; the
  positive bias is the correct value.

These three readings point to different downstream actions.

### Q4. Should κ be ξ-dependent or evaluated only at ξ_canonical?

`σ₁_std(ξ)` has a positive monotone trend with R² = 0.88.
`σ₁_IQR_proxy(ξ)` is nearly flat (R² = 0.21). If `σ₁_std` is the
admissible input (§Q1), then κ inherits the ξ-dependence of
`σ₁_std` linearly through `κ ∝ σ₁`. If `σ₁_IQR_proxy` is
admissible, κ is approximately ξ-independent inside the
canonical window.

The decision whether κ is ξ-dependent depends on §Q1.

---

## 4. Provisional rules (subject to refinement)

These rules are **provisional**: GR-SC 1.3-Predictions may adopt
or modify them; other downstream memos may challenge them. They
represent the simplest internally-consistent position that
permits progress without overclaiming.

### Rule R1 (provisional) — σ₁ admissibility

Adopt **`σ₁_std`** as the primary κ input, with `σ₁_IQR_proxy`
as a cross-check. Rationale:

- The tenth-pass Rayleigh derivation invokes `Var(T_motif) =
  σ₁²` structurally; the variance-equivalent definition is
  `σ₁_std`.
- `σ₁_std` is the mathematically-appropriate second-moment
  input for the Rayleigh distribution even when the underlying
  distribution is heavy-tailed; the Rayleigh form then becomes
  an approximation whose accuracy is quantified by the
  `σ₁_std / σ₁_IQR_proxy` ratio.
- `σ₁_IQR_proxy` provides the Gaussian-equivalent comparator;
  a κ evaluation using both and quoting the difference as a
  model-uncertainty component is honest and operationally
  consistent with the three-component scheme of GR-SC 1.2.

### Rule R2 (provisional) — Rayleigh-scaling validity

Quote κ using the Rayleigh scaling `κ ∝ |N̂'|·σ₁/(2√2)` as a
**leading-order approximation**. Attach an additional uncertainty
component reflecting the Gaussianity breakdown:

- **Model-approximation band** = `|σ₁_std − σ₁_IQR_proxy| /
  σ₁_std` × central κ value.

At canonical ξ this band is ≈ **±10.9 %**, comparable to the
calibration CI but smaller than the per-realisation ±25 %
inherited from ED-SC 3.3.9.

If in the future a non-Gaussian analog of the Rayleigh
distribution is derived specifically for the heavy-tailed
`T_motif` case, this band collapses; until then it stands as
honest uncertainty.

### Rule R3 (revised post-F1) — trace bias interpretation

**Adopt T-bias reading (a):** the tenth-pass Trace-Gaussian-class
rigid-zero identity is **approximate**, not exact, at the ED-SC
motif-filter resolution. Both bulk and filtered populations
exhibit a small positive median_T bias; the filter **amplifies**
the bulk bias rather than creating it.

Quantitative findings from F1 (ED-SC 3.4-σ₁ filtered-vs-unfiltered
T scan; see §4.bis below):

- **Bulk median_T is ξ-dependent and small** (~0.02 % of σ_T at
  canonical ξ), rising monotonically from 7.7 × 10⁻⁵ at
  ξ = 1.60 to 2.0 × 10⁻⁴ at ξ = 1.93. Bulk CI excludes 0 at 5 of
  9 points (the upper 5, ξ ≥ 1.80).
- **Filtered median_T is roughly flat** (~0.0008 across ξ),
  corresponding to ~0.2 % of σ_T at canonical ξ.
- **Amplification ratio** `|median_T_filt| / |median_T_bulk|` is
  ~9× at most points (median across the scan = 8.94; range 3.7
  to 16.2 with higher ratios at lower ξ).
- **σ₁_std ratio** `σ₁_std_filt / σ₁_std_bulk` is systematically
  > 1, rising monotonically from 1.27 to 1.41; the filter also
  widens the distribution.

**Readings (b) and (c) are refuted:** (b) predicted bulk CI would
contain 0 at essentially all ξ (refuted at 5/9 points); (c)
predicted filtered and bulk medians would be comparable in
magnitude (refuted — filter medians are ~9× bulk medians, far
above the 2× amplification threshold).

**Consequences for downstream memos:**

- **Tenth-pass GR-SC 2.0 Consolidation** — the "Trace-Gaussian-
  class rigidly-zero median" characterisation needs a
  **correction-term note**: the rigid-zero identity holds only
  approximately at the bulk saddle-ensemble level, with a small
  ξ-dependent positive bias (~0.02 % of σ_T at ξ ≈ 1.8, growing
  with ξ). A dedicated tenth-pass amendment memo is required.
- **GR-SC 1.1 §3.5 (rigid identities `G_00 ≡ 0`, `B_ab ≡ 0`)** —
  these two identities derive from spatial-metric structure and
  Weyl duality, not from the trace-GRF assumption; they are
  **unaffected** by the F1 finding. The rigid-zero claim for
  `F̄`, `tr(G^ij)`, `R` (which **does** derive from the Gaussian-
  trace assumption) needs the same correction-term note.
- **GR-SC 1.5 Rayleigh derivation** uses `Var(T_motif) = σ₁²`
  (variance, a second-moment quantity), not `median(T_motif)`.
  **The Rayleigh scaling κ ∝ |N̂'|·σ₁/(2√2) is not directly
  broken by the rigid-zero failure.** Rule R2's ±10.9 %
  model-approximation band (from the Gaussianity failure)
  already absorbs the combined heavy-tail and residual-bias
  error.
- **GR-SC 1.3-Predictions may proceed without further delay.**
  The bulk bias is small in absolute magnitude (~5 % of σ₁_std
  at the largest ξ), non-Gaussian tails and rigid-zero bias are
  both contained within the ±10.9 % band, and the Rayleigh
  scaling's variance structure is unaffected.

F1 follow-up (§7 of this memo) is now **executed, not pending**.
Remaining pending follow-ups: F2 (multi-seed σ₁ spread), F3
(non-Gaussian Rayleigh-equivalent derivation, optional), F4
(Correlation-class scoping).

### Rule R4 (provisional) — ξ-dependence of κ

Under Rule R1 (σ₁_std is primary), κ is **ξ-dependent** inside
the canonical window with the same linear trend as σ₁_std:
slope in κ equal to `|N̂'| · 0.002876 / (2√2) ≈ |N̂'| ·
0.001017` per unit ξ.

Predictions at ξ ≠ ξ_canonical must quote the κ value at the
chosen ξ using the `σ₁_std(ξ)` fit; ξ_canonical is the default
but not unique. Mirror of GR-SC 1.2's treatment of `C²`.

### Rule R5 (provisional) — κ uncertainty structure

Under rules R1–R4, κ inherits **four** uncertainty components,
quoted separately and never combined in quadrature:

- **(i) Calibration CI** — from `σ₁_std` bootstrap CI at the
  nearest ξ grid point, or RMS residual 0.000126 between
  grid points, mapped linearly through `κ = |N̂'|·σ₁_std/(2√2)`.
- **(ii) Ensemble CI** — from the per-grid-point bootstrap CI of
  `σ₁_std` as recorded in `sigma1_calibration_table.csv`.
- **(iii) Per-realisation ±25 %** — inherited from ED-SC 3.3.9
  pending empirical verification at the σ₁ level (currently a
  pessimistic transfer from S2; a multi-seed σ₁ measurement
  would refine this band).
- **(iv) Model-approximation band ±10.9 %** — from the
  Gaussianity failure (per Rule R2).

---

## 4.bis F1 follow-up execution (filtered vs unfiltered T)

The filtered-vs-unfiltered T diagnostic pre-registered as §7 F1
was executed 2026-04-23; results in
`outputs/ed_sc_3_4_sigma1/sigma1_filtered_vs_unfiltered_T_summary.json`
and the companion CSV. Driver:
`analysis/scripts/ed_sc_3_4_sigma1_filtered_vs_unfiltered_T.py`.

**Reading (a) adopted; readings (b) and (c) rejected.**

The stock three-way verdict logic emitted "Inconclusive" because
`n_bulk_bias = 5` fell into the middle range of the pre-registered
bias-count thresholds (≤ 2 for (b); ≥ 6 for (a)/(c)). Inspection
of the per-ξ structure showed a cleaner story than the threshold
test captured:

- **Bulk bias is ξ-ordered**, present only at the upper 5 points
  (ξ ≥ 1.80) where the larger N_bulk ≈ 2900 resolves the small
  bias; at the lower 4 points the bulk pool is consistent with
  zero.
- **Filter amplification is dramatic**, with median amp = 8.94,
  well above the 2× threshold that distinguishes (a) from (c).
- **σ₁_std is also amplified by the filter** (ratio 1.27–1.41),
  confirming the filter changes distribution shape, not just
  location.

No reading other than (a) fits this pattern: the bulk GRF has a
small real bias, the filter amplifies it. The stock "Inconclusive"
tag reflects a limitation of the count-based threshold logic, not
ambiguity in the underlying signal. Rule R3 above is the amended
reading adopted on the strength of the per-ξ structure.

---

## 5. What GR-SC 1.3-Predictions will compute

Contingent on acceptance of the §4 provisional rules, the
follow-up memo `theory/GR_SC_1_3_RayleighClass_Predictions.md`
will emit:

- **Central κ value** at `ξ_canonical = 1.7575`:

      κ_central = |N̂'| · σ₁_std(ξ_canonical) / (2√2)
                = |N̂'| · 0.00517 / 2.828
                = |N̂'| · 0.001828       (scale-free: 0.001828)

  with `|N̂'|` the kinematic calibration constant from GR-SC 1.5
  (not re-derived).

- **κ(ξ) curve** across the canonical window, mirroring the
  GR-SC 1.2 §5 S2 table:

      κ(ξ) / |N̂'| = (0.000114 + 0.002876·ξ) / (2√2)
                  = 0.0000403 + 0.001017·ξ

- **Four uncertainty bands** per Rule R5, endpoint-mapped
  through the linear `κ ∝ σ₁_std` scaling.

- **Pool-R2 anchor cross-check.** Verify that the empirical
  `σ₁_std`, `|μ₁|`, and the tenth-pass-arc prediction
  `κ/(|μ₁|σ₁) = 0.52 ± 0.05` are mutually consistent at canonical
  ξ. Quote the discrepancy.

- **GR-SC 1.8 clearance evaluation.** Compute the ratio
  `σ₁_std(ξ_canonical) / κ_M^det` under the scale-free
  parameterisation; test against the engineering target `<
  0.036` (2σ). This makes the EIT-Extremal clearance memo
  numerically actionable for the first time.

GR-SC 1.3-Predictions will **not** attempt to resolve T-bias
reading (b) vs (a) vs (c), and will explicitly cite Rule R3 as
a provisional assumption inherited from this memo.

---

## 6. Decision tree for κ evaluation

```
                  ┌──────────────────────────────┐
                  │ ED-SC 3.4-σ₁ executed?       │
                  │ YES → proceed; NO → block    │
                  └──────────────┬───────────────┘
                                 │ YES
                  ┌──────────────▼───────────────┐
                  │ r_diag excursions = empty?    │
                  │ YES → proceed; NO → block    │
                  └──────────────┬───────────────┘
                                 │ YES
                  ┌──────────────▼───────────────┐
                  │ Apply Rule R1: σ₁_std primary │
                  │ (σ₁_IQR_proxy cross-check)    │
                  └──────────────┬───────────────┘
                                 │
                  ┌──────────────▼───────────────┐
                  │ Apply Rule R2: Rayleigh      │
                  │ scaling + ±10.9 % model band │
                  └──────────────┬───────────────┘
                                 │
                  ┌──────────────▼───────────────┐
                  │ Apply Rule R3: T-bias (b)    │
                  │ (filter-population bias;     │
                  │  tenth-pass taxonomy stands) │
                  └──────────────┬───────────────┘
                                 │
                  ┌──────────────▼───────────────┐
                  │ Apply Rule R4: κ(ξ) linear   │
                  │ in ξ with slope 0.001017     │
                  └──────────────┬───────────────┘
                                 │
                  ┌──────────────▼───────────────┐
                  │ Apply Rule R5: quote 4 bands │
                  │ (calib, ensemble, per-real,  │
                  │  model-approx) separately    │
                  └──────────────┬───────────────┘
                                 │
                  ┌──────────────▼───────────────┐
                  │ Emit GR-SC 1.3-Predictions:  │
                  │ κ_central, κ(ξ), 4 bands,    │
                  │ pooled-R2 cross-check,       │
                  │ GR-SC 1.8 clearance ratio    │
                  └──────────────────────────────┘
```

---

## 7. Required follow-up analyses

The following analyses are **not in scope for GR-SC 1.3-Predictions**
but are flagged as required before related downstream claims can be
finalised:

- **F1. Filtered-vs-unfiltered `T` statistics** on the same 40-
  snapshot field realisations. Discriminates T-bias reading (b)
  from (a)/(c). Scope: small follow-up driver that takes the
  existing σ₁ snapshots and additionally computes `T_field =
  trace(H)` over the full lattice (not just admitted motifs),
  comparing bulk `median(T_field)` against motif `median(T_motif)`.
  Decides whether the bias is a filter artefact (then Rule R3
  stands as written) or an intrinsic property of the bulk field
  (then Rule R3 and the tenth-pass taxonomy both need
  amendment).

- **F2. Multi-seed σ₁ spread characterisation.** Currently the
  ±25 % per-realisation band in Rule R5 (iii) is inherited from
  ED-SC 3.3.9's S2 measurement. A dedicated multi-seed σ₁ scan
  would replace that pessimistic transfer with a measured band.
  Scope: run ED-SC 3.4-σ₁ at canonical ξ only, on 10 canonical
  seeds, and measure the per-seed spread of σ₁_std. If tighter
  than 25 %, relax Rule R5 (iii).

- **F3. Non-Gaussian Rayleigh-equivalent derivation** (optional,
  theory-only). If the `T_motif` distribution turns out to be
  describable by a known heavy-tailed family (student-t,
  stretched exponential, etc.), deriving the surface-gravity
  distribution on that family would replace the `±10.9 %` model
  band with a sharper form. Scope: analytic work, no driver.

- **F4. Correlation-class scoping** for `C_redshift(r)`. The
  other remaining deferred row of GR-SC 1.0 §5. Two-point motif
  correlation scan along ξ, structurally analogous to ED-SC 3.4
  and 3.4-σ₁ but emitting the two-point autocorrelation rather
  than single-point statistics. Not a Rayleigh-class issue but
  the natural next calibration target.

---

## 8. Summary statement for GR-SC 1.3-Predictions

Once §4 rules are adopted, GR-SC 1.3-Predictions will compute:

- `κ(ξ_canonical) / |N̂'| = 0.001828` (scale-free central value)
- `κ(ξ) / |N̂'| = 0.0000403 + 0.001017·ξ` (scale-free linear
  calibration curve across the canonical window)
- Four separate uncertainty bands (calibration, ensemble,
  per-realisation, model-approximation)
- A cross-check against the tenth-pass-arc pooled-R2 anchor
  `κ/(|μ₁|σ₁) = 0.52 ± 0.05`
- The EIT-Extremal clearance ratio `σ₁_std/κ_M^det`

and will explicitly cite this memo (GR-SC 1.3-Scoping) as the
source of its interpretive rules. Rules R1–R5 are **provisional**
and subject to revision if any of the four follow-up analyses
(F1–F4) yield conflicting evidence.

---

## 9. Changelog

- **Rev. 1 (2026-04-23, this memo):** opens GR-SC 1.3 as the
  Rayleigh-class scoping layer. Incorporates ED-SC 3.4-σ₁
  execution results: σ₁_std(ξ) fit `0.000114 + 0.002876·ξ`, R² =
  0.880; rigid-zero failure at 7/9 points (`median_T ≈ +0.0008`);
  Gaussianity failure at 6/9 points (`σ₁_std/σ₁_IQR_proxy` rising
  from 1.04 to 1.17 monotonically in ξ). Pre-registers four
  scoping questions (Q1–Q4), five provisional rules (R1–R5),
  and a decision tree for κ evaluation. Provisionally adopts
  `σ₁_std` as primary κ input (Rule R1); Rayleigh scaling as
  leading-order approximation with ±10.9 % model band (Rule R2);
  T-bias reading (b) — filter-population bias (Rule R3);
  ξ-dependent κ with slope |N̂'|·0.001017 per unit ξ (Rule R4);
  four-component uncertainty structure (Rule R5). Flags four
  required follow-up analyses (F1–F4) before downstream claims
  are finalised. Scope-level only; no κ value emitted; GR-SC
  1.3-Predictions is the computation memo to be written after
  acceptance of Rules R1–R5.
