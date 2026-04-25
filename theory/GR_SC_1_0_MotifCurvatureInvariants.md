# GR-SC 1.0 — Motif-to-Curvature Invariant Mapping

**Status:** Scope memo. Opens the motif-statistics → curvature-
invariant program. Uses ED-SC 3.3.x closure + ED-SC 3.4
ξ-calibration as inputs. No new numerics beyond those quoted from
the ED-SC 3.4 execution.
**Relation to existing GR-SC arc:** this memo is a **mapping layer**
that connects the ED-SC motif statistics `(S1, S2, S3)` to the
curvature-invariant classes defined in the tenth-pass GR-SC arc
(`GR_SC_1_0_EinsteinTensor_MotifStatistics.md`,
`GR_SC_1_6_WeylTensor_MotifStatistics.md`,
`GR_SC_2_0_Consolidation.md`, and the five-class taxonomy
Ratio/Trace/Quadratic/Rayleigh/Correlation). It does not
reopen or re-derive the kinematic acoustic-metric results of that
arc; it catalogues how the motif-filter observables calibrated by
ED-SC 3.4 are to be **propagated into** those invariants' numerical
predictions.
**Parents:**
- `theory/ED_SC_3_3_10_ArcClosure.md` §3 (four-clause final
  invariance statement).
- `theory/ED_SC_3_4_XiCalibration.md` + execution
  `outputs/ed_sc_3_4/xi_calibration_summary.json`.
- `theory/GR_SC_2_0_Consolidation.md` (five-class taxonomy).
- `theory/ED_SC_3_1_rev3_CanonicalPointCertification.md` §4.1
  (canonical operating point + resolution qualification).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post ED-SC 3.4 execution).

---

## 1. Purpose

The ED-SC 3.3.x sub-arc closed with a four-clause distributional
invariance statement (ED-SC 3.3.10): S1 invariant per-realisation,
S2 invariant ensemble-only, canonical domain `r_diag(L_ray) = 1`,
`r_diag = 2` rescued by the shell-aware coordinate `L_eff`. ED-SC
3.4 has produced the ξ-calibration curves needed to evaluate
downstream quantities at any ξ inside the canonical domain:

- **S1(ξ) is near-flat** across `ξ ∈ [1.60, 1.95]` (OLS slope
  0.058, R² = 0.011, total variation 1.05 % of |S1_mean| — well
  below the 20 % size-corrected envelope).
- **S2(ξ) rises monotonically** with OLS slope **+1.396** per
  unit ξ and intercept −0.322 (R² = 0.640; RMS residual 0.124).
- **S3(ξ)** is exploratory; weakly positive trend (slope +1.25,
  R² = 0.463) but no cross-scale claim is promoted.

**GR-SC 1.0 opens the motif-statistics → curvature-invariant
program.** Its scope here is:

- **S1-derived invariants** — `r*`, `ℛ_W`, `ℛ_Ray`, `ℛ_G` — use
  the S1 calibration as a ξ-independent constant inside the
  canonical domain and inherit **per-realisation certainty**.
- **S2-derived invariants** — `C²`, `det G` — use the S2
  calibration curve via linear interpolation and inherit
  **ensemble-only certainty** with the ED-SC 3.3.9 ±25 %
  per-realisation spread attached.
- **S3-derived invariants** — exploratory only; no cross-scale
  claim promoted from S3.

No tensor redefinition or new kinematic calculation is performed
here. The five-class taxonomy of the tenth-pass GR-SC arc
(Ratio / Trace-Gaussian / Quadratic / Rayleigh / Correlation) is
preserved verbatim; this memo specifies how the ED-SC motif
observables populate their numerical values, with calibrated
uncertainty.

---

## 2. Inputs from ED-SC 3.4

Verbatim from `outputs/ed_sc_3_4/xi_calibration_summary.json`
(executed 2026-04-23 on fixed seed 77, 40-snapshot pooling per
point, 9 ξ points in [1.60, 1.95]):

### 2.1 S1 calibration

- **Fit:** `S1(ξ) = −2.057 + 0.058·ξ`, R² = 0.011, RMS residual
  0.065.
- **Range across scan:** `S1 ∈ [−2.00, −1.78]`, mean ≈ −1.95.
- **Total variation fraction:** 1.05 % of |S1_mean|.
- **Operational reading:** S1 is **effectively constant** across
  the r_diag = 1 window. For GR-SC purposes,

        S1_eff = −1.95  (± ~0.15 single-realisation scatter)

  is the recommended point value. The negligible slope (0.058
  per unit ξ across a 0.35 lu window) is not promoted as a
  trend; it is noise.

### 2.2 S2 calibration

- **Fit:** `S2(ξ) = −0.322 + 1.396·ξ`, R² = 0.640, RMS residual
  0.124.
- **Range across scan:** `S2 ∈ [1.78, 2.51]`, monotone positive
  trend.
- **At canonical `ξ_canonical = 1.7575 lu`:** `S2_fit =
  −0.322 + 1.396 · 1.7575 = 2.132`.
- **Operational reading:** S2 is a smooth monotone function of
  ξ. GR-SC evaluates S2 at any ξ in [1.60, 1.95] by **linear
  interpolation on the calibration grid** (or equivalently the
  OLS fit). Uncertainty has three components — discussed in §4.

### 2.3 S3 calibration (exploratory)

- **Fit:** `S3(ξ) = −6.387 + 1.249·ξ`, R² = 0.463, RMS residual
  0.160.
- **Range across scan:** `S3 ∈ [−4.47, −3.83]`.
- **Operational reading:** recorded for completeness. Not
  propagated into any GR-SC invariant promoted here.

### 2.4 Domain of validity

- `ξ ∈ [1.60, 1.95]` under the canonical hinge `L_ray/ξ = 1.08`
  (equivalently `r_diag(L_ray) = 1`). Predictions outside this
  range require either (i) the shell-aware coordinate `L_eff`
  for `r_diag = 2` per ED-SC 3.3.8b (with its own calibration to
  be executed in a follow-up ED-SC 3.4b if needed) or (ii) a
  fresh scoping memo for `r_diag ≥ 3`.

---

## 3. Definitions of GR-SC 1.0 invariants

All definitions are in terms of the ED-SC motif statistics.
Algebraic forms follow the tenth-pass GR-SC arc's five-class
taxonomy; the novelty here is the **explicit evaluation recipe**
via S1 / S2 with ED-SC 3.4 calibration.

### 3.1 S1-derived (Ratio-class; per-realisation certainty)

**`r*` — median-ray invariant.**

    r* ≡ S1 = median(λ_neg / λ_pos)

where the ratio is taken over admitted motifs. `S1` is the direct
ED-SC measurement; `r*` is its GR-SC name. The ninth-pass r*
analytic arc's closed-form `r* = −2χ/(2χ − 1)` (with
`χ = 2μκ⊥²/P_0`) applies to the cubic-bistable saddle premise;
on R2 motifs `r* = S1` empirically. Inside the r_diag = 1 window:

    r* = S1_eff = −1.95  (ξ-independent per §2.1).

**`ℛ_W` — Weyl ratio (near-singular at empirical operating point).**

ℛ_W (Weyl ratio) is defined algebraically as
ℛ_W(S1) = −(2 S1 + 1)/(S1 + 2), but at the empirical operating
point S1_eff ≈ −1.95 this map is near-singular. The dedicated
sensitivity scan GR_SC_1_0a_WeylRatio_Sensitivity classifies
ℛ_W as a near_singular_artifact: |dℛ_W/dS1| ≈ 1200 at S1_eff
and κ_max ≈ 200 across the empirical S1 band. Consequently,
GR-SC 1.0 does not promote any numerical ℛ_W prediction; only
the structural Ratio-class mapping is retained.

Citation rule: do not quote a numerical ℛ_W value. Cite only
that ℛ_W is a Ratio-class invariant defined by the algebraic
map above, and that at the current ED-SC operating point the
map is too ill-conditioned for quantitative use.

**`ℛ_Ray` — Raychaudhuri-like contraction.**

    ℛ_Ray ≡ λ_1 / λ_2 = r* = S1

(Ratio-class identification from the tenth-pass arc: `ℛ_Ray = r*`
as the `λ_neg / λ_pos` ratio on the saddle Hessian.) Numerically
identical to `r*`: `ℛ_Ray = −1.95` inside the canonical domain.

**`ℛ_G` — geometric mean curvature proxy.**

    ℛ_G ≡ trace(G^ij) / det(G^ij)    [schematic]

In the tenth-pass arc's Ratio-class limit, `ℛ_G = r*` as well
when the Einstein tensor trace is evaluated on the kinematic
acoustic metric at motif centres. Empirically `ℛ_G = S1 =
−1.95`.

### 3.2 S2-derived (Quadratic-class; ensemble-only with spread)

**`C²` — Weyl-squared / quadratic curvature analogue.**

The tenth-pass arc's quadratic-class scaling
`⟨C²⟩ ≈ 2.44·μ₁²·σ_2²` is evaluated with `σ_2` proxied by S2
(the IQR of the ratio distribution is the dominant observable
spread). Schematically,

    C²(ξ) ∝ S2(ξ)²

with the proportionality constant fixed by the acoustic-metric
calculation, not by this memo. Evaluated on the ED-SC 3.4
calibration curve:

    C²(ξ) ∝ (−0.322 + 1.396·ξ)²
    C²(ξ_canonical = 1.7575) ∝ 2.132² = 4.547.

**Uncertainty structure** (see §4): ensemble-pool band ± ED-SC
3.3.9 ~25 % per-realisation spread.

**`det G` — determinant-class invariant.**

Quadratic-class; scales similarly:

    det G(ξ) ∝ S2(ξ)² / N̂²

where `N̂` is the motif-centre normal-field mean (scale-factor
inherited from the kinematic calculation). Numerically:

    det G(ξ_canonical) ∝ 2.132² / N̂² = 4.547 / N̂².

Same uncertainty structure as `C²`.

### 3.3 S3-derived (exploratory)

No invariant is promoted from S3 here. Future memos may
characterise the upper-tail log-slope if it acquires a role in a
correlation-class (two-point) prediction; not in scope for
GR-SC 1.0.

---

## 4. ξ-positioning rules

For any GR-SC prediction:

1. **Declare `ξ_pred`** — the ξ value at which the prediction is
   to be evaluated.
2. **Verify** `ξ_pred ∈ [1.60, 1.95]` (canonical r_diag = 1
   domain). Outside this window the calibration is not valid;
   either use L_eff for `r_diag = 2` with a dedicated
   calibration, or declare the prediction out-of-scope.
3. **Evaluate S1, S2, S3 at ξ_pred**:
   - **S1** — use `S1_eff = −1.95` (ξ-independent); the fitted
     slope is not promoted and should not be used.
   - **S2** — linear interpolation on the calibration grid, or
     equivalently the OLS fit `S2(ξ) = −0.322 + 1.396·ξ`. At
     grid points, use the per-point bootstrap CI; between grid
     points, use the RMS residual 0.124 as an interpolation
     uncertainty.
   - **S3** — use the fit if at all, but do not promote to a
     cross-scale claim.
4. **Propagate uncertainty** per invariant class:
   - **S1-derived (Ratio-class):** per-realisation certainty;
     total S1 envelope ±0.15 covers single-realisation scatter.
     `ℛ_W` additionally requires a sensitivity check due to
     near-singular `r* + 2` map.
   - **S2-derived (Quadratic-class):** three uncertainty
     components, reported separately:
     - **(i) Calibration CI** — bootstrap 16–84 band at the
       grid point (or RMS residual 0.124 between points).
     - **(ii) Ensemble-pool uncertainty** — from the per-point
       CI reported in `xi_calibration_table.csv`.
     - **(iii) Per-realisation spread** — ED-SC 3.3.9 ±25 % of
       the central value.
     A GR-SC 1.0+ prediction citing `C²` or `det G` must quote
     all three separately; they are not combinable in quadrature
     without a physical rationale.

---

## 5. Deliverable: invariant → input → ξ-dependence → uncertainty map

| Invariant | Class | ED input | ξ-dependence | Uncertainty | Evaluated in |
|---|---|---|---|---|---|
| `r*` | Ratio | S1 | ξ-independent (1.05 % variation) | per-realisation ±0.15 | GR-SC 1.1 |
| `ℛ_Ray` | Ratio | S1 (identity) | ξ-independent | per-realisation ±0.15 | GR-SC 1.1 |
| `ℛ_G` | Ratio | S1 (identity) | ξ-independent | per-realisation ±0.15 | GR-SC 1.1 |
| `ℛ_W` | Ratio (bounded) | near_singular_artifact (no numerical citation; see GR_SC_1_0a) | Not quantitatively calibrated. Sensitivity scan shows \|dℛ_W/dS1\| and κ too large for predictive use at S1_eff. | Not quantitatively calibrated. | GR-SC 1.0a (excluded) |
| `C²` | Quadratic | S2² | linear in ξ (slope +1.396) | calib CI + ensemble CI + per-real ±25 % | GR-SC 1.2 |
| `det G` | Quadratic | S2² / N̂² | linear in ξ (slope +1.396) | calib CI + ensemble CI + per-real ±25 % | GR-SC 1.2 |
| `κ` | Rayleigh | σ₁ | linear in ξ (slope \|N̂'\|·0.001017 × 0.9661) | calibration ±2.4 %, ensemble ~±8 %, per-real ±9.9 % (F2 measured), model ±10.78 % ‡ (F3-verify Hessian; dominant) | GR-SC 1.3 (Rayleigh-class predictions) |
| `F̄`, `tr(G^ij)`, `R` | Trace-Gaussian | rigidly-zero-median **†** | none | none (structural zero; see †) | GR-SC 1.1 §3.5 (rigid zeros) |
| `C_redshift(r)` | Correlation | ξ-correlator | two-point, not calibrated | awaits separate two-point scan | awaits two-point scan |

The table is authoritative for GR-SC 1.0 predictions. Any
prediction that cites a row not listed here is out-of-scope for
GR-SC 1.0 and requires a dedicated opening memo.

**† Correction-term note on Trace-Gaussian-class rigid-zero.**
The ED-SC 3.4-σ₁ F1 follow-up (filtered-vs-unfiltered T scan,
executed 2026-04-23) demonstrated that the tenth-pass
Trace-Gaussian-class "rigidly-zero median" claim for `F̄`,
`tr(G^ij)`, `R` is **approximate** at the ED-SC motif-filter
resolution, not exact. Both bulk and filtered populations exhibit
a small positive `median_T` bias (~0.02 % σ_T at ξ ≈ 1.8 for
bulk, ~0.2 % σ_T for filtered, ~9× filter-amplification). The
bulk bias is ξ-dependent and only resolved at large sample size;
the filter amplifies it. This does **not** affect the
‡ **Rayleigh-class κ model-band note.** F3 (Student-t
ν ≈ 30 fit via multi-seed Gaussianity ratio) initially
claimed a ±1.61 % model band via a 10-seed summary-statistic
envelope. F3-verify (MLE fit on the raw pooled `T_motif`
sample of ~849 motifs) confirmed the Student-t family (KS
p = 0.987) and ν_fit = 28.013 within the F3 envelope, **but
revealed the Fisher-information Hessian is shallow in ν
(σ_ν = 23)**, producing an honest model band of ±10.78 %
— reverting to post-F2 hierarchy with model as dominant
component again. An optional **Rayleigh-preservation-
restricted band ±3.4 %** is available as an
assumption-dependent tighter alternative (truncates ν ≥ 15
where Rayleigh-shape preservation of GR-SC 1.3-ModelCorrection
§3.4 remains valid); ±3.4 % is not the canonical quote
because it requires an extra assumption beyond the Student-t
fit itself.

Rayleigh-class scaling in GR-SC 1.3 (which uses `σ₁²`, a variance,
not the median) but does require a forthcoming amendment to
GR-SC 2.0 Consolidation's five-class taxonomy. Rigid-zero
remains the correct leading-order claim; the correction term is
empirically small. See GR-SC 1.3-Scoping §4.bis for the full
discrimination against readings (b) and (c). `G_00 ≡ 0` and
`B_ab ≡ 0` from GR-SC 1.1 §3.5 derive from spatial-metric
structure and Weyl duality and are **not** affected by this
correction.

---

## 6. Changelog

- **Rev. 1 (2026-04-23, this memo):** opens GR-SC 1.0 as the
  motif-statistics → curvature-invariant mapping layer. Uses
  ED-SC 3.4 calibration (S1 near-flat inside r_diag = 1 window;
  S2(ξ) = −0.322 + 1.396·ξ; S3 exploratory) as the numerical
  substrate for S1-derived Ratio-class invariants (`r*`, `ℛ_W`,
  `ℛ_Ray`, `ℛ_G`) and S2-derived Quadratic-class invariants
  (`C²`, `det G`). Flags `ℛ_W` as **near-singular** at the
  canonical S1 = −1.95 (maps to 58.0 via `−(2S1+1)/(S1+2)`, very
  sensitive to S1 near the `r* = −2` pole). Defines explicit
  ξ-positioning rules and three-component uncertainty propagation
  for S2-derived predictions (calibration CI + ensemble CI +
  per-realisation ±25 % spread). Rayleigh-class `κ` and
  correlation-class `C_redshift` are explicitly out-of-scope
  pending dedicated σ₁ and two-point calibration scans. No tensor
  redefinition; the tenth-pass GR-SC arc's five-class taxonomy is
  preserved.
