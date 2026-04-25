# GR-SC 2.0 Consolidation Amendment — Fifteenth-Pass Integration

**Status:** Amendment memo. Folds the fifteenth-pass findings
(F1, F2, F3, F3-verify) into the tenth-pass GR-SC 2.0
Consolidation taxonomy. Documentation pass only — no new
derivations, no new execution, no new tensor calculations.
The parent `theory/GR_SC_2_0_Consolidation.md` memo remains the
authoritative taxonomy record; this amendment is the canonical
way to cite the fifteenth-pass corrections alongside it.
**Parent (tenth-pass consolidation):**
- `theory/GR_SC_2_0_Consolidation.md` — five-class invariant
  taxonomy, rigid-zero Trace-Gaussian identity, Gaussian-based
  Rayleigh scaling, pooled-R2 anchor block.
**Fifteenth-pass parents (inputs to this amendment):**
- `theory/ED_SC_3_4_sigma1_Calibration.md` + single-seed
  execution (σ₁ ξ-calibration; single-seed Gaussianity ratio
  1.109 and rigid-zero failure diagnostics).
- `theory/ED_SC_3_4_sigma1_filtered_vs_unfiltered_T.py`
  execution (F1 diagnostic; reading (a) adopted).
- `theory/ED_SC_3_4_sigma1_MultiSeed.md` + F2 execution
  (multi-seed σ₁; CoV = 9.9 %; cross-seed Gaussianity ratio
  1.023; cross-seed rigid-zero passes).
- `theory/GR_SC_1_3_RayleighClass_ModelCorrection.md` (F3
  analytic Student-t ν = 30 derivation; central shift to
  0.001766).
- `theory/GR_SC_1_3_RayleighClass_ModelCorrection_Verify.md` +
  F3-verify MLE execution (ν_fit = 28.013; KS p = 0.987;
  σ_ν = 23.05; model band revised to honest ±10.78 %).
- `theory/GR_SC_1_3_RayleighClass_Scoping.md` and
  `theory/GR_SC_1_3_RayleighClass_Predictions.md` (current
  Rayleigh-class prediction layer containing all four
  fifteenth-pass patches).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`. Cited for traceability;
this amendment performs no simulator calls.
**Date:** 2026-04-23 (fifteenth-pass consolidation close).

---

## 1. Purpose

`GR_SC_2_0_Consolidation.md` (tenth pass, 2026-04-23) encodes
the consolidated GR-SC curvature-invariant taxonomy derived
from the kinematic acoustic metric under GRF motif-conditioning.
Its durable claims include:

- **Five-class invariant taxonomy**: Ratio (unbounded / bounded),
  Trace-Gaussian, Quadratic, Rayleigh, Correlation.
- **Two rigid identities**: `G_00 ≡ 0`, `B_ab ≡ 0`.
- **Trace-Gaussian-class rigid-zero median claim** for `F̄`,
  `tr(G^ij)`, `R`.
- **Rayleigh-class surface-gravity scaling** `κ ∝ |N̂'|·σ₁/(2√2)`
  derived under Gaussian-trace assumption.
- **Pooled-R2 anchor block** including `κ/(|μ₁|σ₁) = 0.52 ± 0.05`.

The fifteenth-pass GR-SC 1.3 layer (Rayleigh-class predictions
+ F1/F2/F3/F3-verify follow-ups) produced **four corrections**
that amend — but do not retract — the tenth-pass taxonomy:

1. **Trace-Gaussian rigid-zero is approximate, not exact**, at
   single-seed resolution (F1). Ensemble resolution recovers
   rigid-zero to within statistical uncertainty (F2).
2. **Rayleigh-class central shifts −3.4 %** under a Student-t
   correction factor (F3) empirically validated by MLE (F3-verify).
3. **Rayleigh-class model band magnitude is ±10.78 %** (F3-verify
   honest Hessian), matching the pre-F3 Gaussian conservative
   envelope ±10.9 % for a different structural reason (Fisher
   shallowness in ν vs Gaussian-vs-empirical mismatch).
4. **Ensemble-vs-single-seed phenomenon** — ensemble statistics
   systematically milder than single-seed estimates — documented
   at two independent measurements (F1 rigid-zero, F3 Gaussianity
   ratio) and worth promoting to a taxonomy-level guardrail.

This memo is the canonical amendment that folds all four into
the GR-SC 2.0 record. Citations in future GR-SC work should
cite `GR_SC_2_0_Consolidation.md + this amendment` rather than
the parent alone.

---

## 2. Amendments to Trace-Gaussian class

**Tenth-pass claim** (GR-SC 2.0 §2 and five-class taxonomy
table):

> Trace-Gaussian class (σ_2 input; distribution `N(0, μ₁²σ_2²·k)`;
> members `F̄`, `tr(G^{ij})`, `R`): median rigidly 0.

**Fifteenth-pass amendment.** Replace "median rigidly 0" with:

> **Median approximately zero at ensemble resolution; small
> ξ-dependent bulk bias (~0.02 % σ_T at canonical ξ, growing
> monotonically with ξ) and a filter-amplified bias (~0.2 % σ_T,
> ~9× the bulk bias) at single-seed resolution.** The rigid-zero
> identity derived from symmetry in the tenth-pass kinematic
> calculation holds as the leading-order claim but is **not
> exact** at the ED-SC motif-filter population level. F2 cross-
> seed rigid-zero check passes (`contains_zero = true` within 2σ
> envelope at N = 10 seeds); single-seed single-ξ rigid-zero
> check fails at 7 of 9 ξ points.

**Provenance** for this amendment:

- ED-SC 3.4-σ₁ (single-seed single-ξ execution): 7 of 9 ξ
  points' bootstrap CI on `median(T_motif)` excludes zero
  (`median_T ≈ +0.0008` at canonical ξ); `median_T / σ₁_std
  ≈ 0.21`.
- F1 filtered-vs-unfiltered T diagnostic (reading (a) adopted):
  bulk `median_T ≈ 7.7e−5 → 2.0e−4` monotonically in ξ (~0.02 %
  σ_T); filter amplifies ~9× to ~0.2 % σ_T.
- F2 multi-seed cross-seed aggregate: `median_T_mean = 2.3e−4`,
  `std = 8.2e−4`, |mean|/std = 0.28 — within 2σ of zero;
  `contains_zero = true`.

**Consequence for downstream citations:** any tenth-pass
Trace-Gaussian-class prediction quoting "rigidly zero median"
should instead cite `median ≈ 0 at ensemble resolution` and add
the single-seed bias note. The **functional form** of the
taxonomy (Gaussian distribution with scale `μ₁²σ_2²·k`) is
unchanged; only the median claim acquires the amendment. The
trace itself remains a Gaussian-distributed quantity at
ensemble level.

**Scope of amendment:** `F̄`, `tr(G^{ij})`, `R`. Rigid
identities `G_00 ≡ 0` and `B_ab ≡ 0` are **unaffected** — they
derive from spatial-metric structure and Weyl duality, not from
the Gaussian-trace assumption, and the F1/F2 findings do not
touch them.

---

## 3. Amendments to Rayleigh class

### 3.1 Central value

**Tenth-pass claim** (GR-SC 2.0 pooled-R2 block + GR-SC 1.5):

    κ ∝ |N̂'|·σ₁/(2√2).

Gaussian-trace assumption baked in; no explicit scale-free
central value quoted in GR-SC 2.0 (the central was implicitly
the pooled-R2 anchor `κ/(|μ₁|σ₁) = 0.52 ± 0.05`).

**Fifteenth-pass amendment.** The Rayleigh scaling acquires a
Student-t correction factor:

    κ = |N̂'| · σ₁_std · √((ν−2)/ν) / (2√2),
    with ν = 28.013 (F3-verify MLE, KS p = 0.987),
    correction factor = 0.9661.

**Scale-free central value at the canonical operating point
ξ = 1.7575 lu:**

    κ(ξ_canonical) / |N̂'| = **0.001766**
                          (was 0.001828 under Gaussian Rayleigh;
                           −3.4 % structural correction).

The pooled-R2 symbolic consistency relation updates to:

    |N̂'| / |μ₁| = 1.522 ± 0.147
                  (was 1.471 ± 0.141 under Gaussian;
                   +3.4 % shift mirrors the central correction).

### 3.2 Model band and uncertainty hierarchy

**Tenth-pass claim:** no explicit model-approximation band; κ
uncertainty was bundled with the pooled-R2 anchor at ±9.6 %.

**Fifteenth-pass amendment.** Four independent uncertainty
components with explicit bands:

| component | source | band | notes |
|---|---|---|---|
| Calibration CI | ED-SC 3.4-σ₁ OLS fit RMS residual | **±2.44 %** | tightest |
| Ensemble CI | nearest-grid bootstrap of σ₁_std | **~±8 %** (asymmetric) | |
| Per-realisation | F2 multi-seed σ₁_std CoV | **±9.9 %** | measured, replaces pre-F2 ±25 % transfer |
| Model (honest Hessian) | F3-verify MLE Hessian σ_ν = 23.05 | **±10.78 %** | dominant |
| Model (restricted, optional) | F3-verify with ν ≥ 15 assumption | ±3.4 % | assumption-dependent alternative |

**Uncertainty hierarchy post-F3-verify:**

    model (±10.78 %, dominant)
    > per-real (±9.9 %)
    > ensemble (~±8 %)
    > calibration (±2.4 %).

The model-dominant ordering reverts to the post-F2 configuration
after F3-verify retracted F3's summary-statistic tightening
claim. These four bands must be quoted **separately, not
combined in quadrature** — they express different operational
claims (ensemble vs single-realisation vs noise-floor vs
model-family) and are not independent draws from a single
noise distribution.

**Rayleigh-shape preservation.** The Rayleigh functional form
is preserved under the Student-t correction at ν = 28; only
the scale parameter acquires the `√((ν−2)/ν)` correction
factor. The Rayleigh-preservation-restricted ±3.4 % band
assumes ν ≥ 15, below which the functional-form preservation
itself breaks down (GR-SC 1.3-ModelCorrection §3.4 caveat).

---

## 4. Ensemble-vs-single-seed phenomenon (new guardrail)

The fifteenth-pass arc has documented the **same structural
pattern at two independent measurements**:

- **F1 rigid-zero.** Single-seed single-ξ `median(T_motif)` CI
  excludes zero at 7 of 9 ξ points (ED-SC 3.4-σ₁). F2 multi-seed
  cross-seed `median_T_mean` has 2σ envelope containing zero
  (F2 cross-seed rigid-zero check passes). **Ensemble reveals
  rigid-zero holds approximately; single-seed overstates the
  bias by an order of magnitude in statistical significance.**

- **F3 Gaussianity ratio.** Single-seed single-ξ `σ₁_std /
  σ₁_IQR_proxy = 1.109` at canonical ξ (ED-SC 3.4-σ₁). F2
  multi-seed cross-seed `⟨σ₁_std⟩ / ⟨σ₁_IQR_proxy⟩ = 1.023`.
  Mapped through the Student-t R(ν) table: single-seed → ν ≈ 7
  (strongly heavy-tailed); ensemble → ν ≈ 28–30 (mildly heavy-
  tailed, validated by F3-verify KS p = 0.987). **Ensemble
  reveals the distribution is close to Gaussian; single-seed
  overstates tail weight by a factor of ~4 in ν.**

In both cases, the **ensemble measurement is the reliable one**;
single-seed estimates are systematically biased toward
stronger-than-reality signals. This is a structural consequence
of the finite-N statistical fluctuations combining with
distribution-shape nonlinearities.

**Fifteenth-pass guardrail (proposed; adopted by this
amendment):**

> **Taxonomy-level claims in the GR-SC arc must be derived from
> ensemble measurements where possible. Single-seed or single-ξ
> diagnostic findings may be used for flagging but not for
> taxonomy-level claims.** Ensemble aggregates (≥ 10 seeds, or
> cross-ξ pooling) are the preferred source for rigid-zero,
> Gaussianity, or distributional-shape statements.

This guardrail does not retract any prior finding. It
prescribes future methodological practice: single-seed
diagnostic results are fine for sub-arc triage but must be
confirmed at ensemble resolution before being promoted to the
five-class taxonomy.

---

## 5. Updated GR-SC 1.8 clearance implications

**Tenth-pass claim** (GR-SC 1.8):

    σ₁ / κ_M^det < 0.036     (2σ clearance target)

translates under Gaussian Rayleigh scaling to a kinematic lower
bound on `|N̂'|`; the tenth-pass memo did not compute this bound
explicitly because σ₁ was not yet calibrated at the canonical
operating point.

**Fifteenth-pass amendment.** With σ₁_std(ξ_canonical) = 0.005169
from ED-SC 3.4-σ₁ and the Student-t-corrected Rayleigh scaling:

- **Central:** `|N̂'| ≳ 81.4` for the EIT-Extremal experiment to
  clear the 2σ target using the central σ₁ prediction.
- **Model-band envelope** (±10.78 %, honest Hessian): `|N̂'|
  ∈ [72.6, 90.2]`.
- **Per-realisation envelope** (±9.9 %): `|N̂'| ∈ [73.4, 89.5]`.
- **Calibration envelope** (±2.4 %, for ensemble-averaged
  measurements): `|N̂'| ∈ [79.4, 83.4]`.
- **Rayleigh-preservation-restricted envelope** (±3.4 %,
  optional assumption-dependent): `|N̂'| ∈ [78.6, 84.2]`.

Conservative single envelope: ±11 % covers both the dominant
components (model ±10.78 % and per-real ±9.9 %) with small
cushion, giving `|N̂'| ∈ [72.4, 90.4]`.

The remaining blocker for an absolute clearance-vs-design
evaluation is the kinematic computation of `|N̂'|` from the
acoustic metric, which is outside the fifteenth-pass scope and
belongs to a future GR-SC kinematic-calibration memo.

---

## 6. Summary of amendments to the five-class taxonomy

| class | tenth-pass claim | fifteenth-pass amendment |
|---|---|---|
| Ratio (unbounded) | `r*`, `ℛ_Ray`, `ℛ_G^{spatial} = r*`; pooled R2 `−1.88 ± 0.40` | unchanged |
| Ratio (bounded) | `ℛ_W ∈ (−2, −1/2)`; algebraic map from r* | **ℛ_W near-singular at empirical S1_eff ≈ −1.95** (GR-SC 1.0a `no_numerical_citation`); structural Ratio-class membership preserved but no quantitative citation |
| Trace-Gaussian | median rigidly 0; Gaussian shape | **median ≈ 0 at ensemble; single-seed bias ~0.02–0.2 % σ_T** (this memo §2); Gaussian shape unchanged |
| Quadratic | sign-definite; `⟨C²⟩ ≈ 2.44·μ₁²σ_2²` | unchanged at the tenth-pass level; GR-SC 1.2 provides quantitative predictions with three-component uncertainty |
| Rayleigh | `κ ∝ |N̂'|·σ₁/(2√2)`; pooled R2 `κ/(|μ₁|σ₁) = 0.52 ± 0.05` | **Student-t correction factor 0.9661; central `κ/|N̂'| = 0.001766`; model band ±10.78 %** (this memo §3); pooled-R2 ratio refactored to symbolic `|N̂'|/|μ₁| = 1.522 ± 0.147` |
| Correlation | `C_redshift(r)`; half-rise compression `0.80 ± 0.05` | unchanged; awaits F4 two-point calibration scan |

**Rigid identities** `G_00 ≡ 0` and `B_ab ≡ 0` remain valid;
they derive from geometric structure (static ultrastatic
metric; Weyl duality) and are unaffected by the fifteenth-pass
findings.

**Pooled-R2 anchor block updates:**

| quantity | tenth-pass | fifteenth-pass |
|---|---:|---:|
| `r*` | `−1.88 ± 0.40` | unchanged (S1 projection); per-realisation ±0.15 per GR-SC 1.1 |
| `ℛ_W` | `−1.23 ± 0.05` | **quantitative citation forbidden** (GR-SC 1.0a); structural membership only |
| `κ/(|μ₁|σ₁)` | `0.52 ± 0.05` | structurally stands; maps to `|N̂'|/|μ₁| = 1.522 ± 0.147` under Student-t correction |
| `r_½^{filt}/r_½^{unfilt}` | `0.80 ± 0.05` | unchanged; awaits F4 confirmation |

---

## 7. Guidance for future GR-SC memos

When citing the GR-SC taxonomy post-fifteenth-pass:

- **Use `GR_SC_2_0_Consolidation.md + this amendment`** as the
  paired authoritative reference.
- **For Trace-Gaussian-class claims:** cite
  `median ≈ 0 at ensemble` (not "rigidly zero"); add single-
  seed bias note if the claim depends on single-realisation
  behaviour.
- **For Rayleigh-class κ predictions:** use the post-F3-verify
  central `κ/|N̂'| = 0.001766`; quote all four uncertainty
  bands separately; note the Rayleigh-preservation-restricted
  ±3.4 % optional band as a tighter alternative requiring an
  extra assumption.
- **For any new taxonomy-level claim:** ensure it derives from
  ensemble measurements (≥ 10 seeds or cross-ξ pooling). Single-
  seed diagnostic results are acceptable for flagging but not
  for taxonomy-level promotion.
- **Rigid identities** `G_00 ≡ 0` and `B_ab ≡ 0` remain
  unqualified.

Pre-F3-verify quotes of F3's ±1.61 % model-approximation band
are **retracted**; downstream citations should use ±10.78 %
(honest Hessian) or ±3.4 % (Rayleigh-preservation-restricted,
optional).

---

## 8. Changelog (amendments relative to GR-SC 2.0 tenth pass)

- **Trace-Gaussian class** (§2): "rigidly zero median" replaced
  with "approximately zero at ensemble resolution; single-seed
  bias ~0.02–0.2 % σ_T per F1/F2 diagnostics."
- **Rayleigh class central** (§3.1): scale-free central
  established as `κ/|N̂'| = 0.001766` via Student-t correction
  factor `√((ν−2)/ν) = 0.9661` at F3-verify-confirmed
  ν = 28.013; pooled-R2 symbolic relation updates to
  `|N̂'|/|μ₁| = 1.522 ± 0.147`.
- **Rayleigh class uncertainty structure** (§3.2): four-band
  structure (calibration ±2.4 %, ensemble ~±8 %, per-real ±9.9 %,
  model ±10.78 %) adopted as canonical; model-band's post-F3
  ±1.61 % tightening claim retracted by F3-verify honest-
  Hessian treatment. Hierarchy is **model-dominant**.
- **New guardrail** (§4): ensemble-vs-single-seed phenomenon
  documented at two independent measurements; taxonomy-level
  claims must derive from ensemble measurements.
- **GR-SC 1.8 clearance translation** (§5): first explicit
  quantitative translation of the `σ₁/κ_M^det < 0.036` target
  into a kinematic constraint on `|N̂'|`; central 81.4 with
  four-band propagation envelopes.
- **Taxonomy table updates** (§6): `ℛ_W` marked
  `no_numerical_citation` per GR-SC 1.0a; Trace-Gaussian class
  amended; Rayleigh class gains quantitative scale-free central
  + Student-t correction factor.
- **Guidance for future memos** (§7): use `GR_SC_2_0 +
  amendment` as paired reference; ensemble vs single-seed
  preference; retract pre-F3-verify F3 tightening quotes.
- **No changes** to Ratio-class unbounded, Quadratic class,
  Correlation class (at tenth-pass level), rigid identities
  `G_00`, `B_ab`, or the five-class taxonomy structure itself.

---

## 9. Changelog (this memo)

- **Rev. 1 (2026-04-23, this memo):** opens the GR-SC 2.0
  Consolidation Amendment as the fifteenth-pass integration
  layer. Folds F1 (Trace-Gaussian rigid-zero → approximate),
  F2 (σ₁ per-realisation band = ±9.9 %), F3 (Student-t ν ≈ 30
  correction factor shifts κ central −3.4 %), F3-verify (MLE
  ν = 28.013 confirms family + central; Hessian σ_ν = 23
  revises model band to ±10.78 %) into the tenth-pass GR-SC 2.0
  taxonomy. Introduces the ensemble-vs-single-seed guardrail as
  a new taxonomy-level practice (§4). Provides the first
  explicit quantitative translation of the GR-SC 1.8 clearance
  target (§5). No tenth-pass structural claims retracted; all
  amendments are qualifications or quantitative refinements of
  the existing taxonomy. No execution; pure documentation
  consolidation. Future GR-SC memo citations should reference
  `GR_SC_2_0_Consolidation.md + this amendment` as the paired
  authoritative record.
