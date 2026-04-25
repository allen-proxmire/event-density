# GR-SC 1.3 — Rayleigh-Class Predictions at the Canonical Point

**Status:** Scope memo. Third quantitative GR-SC prediction layer.
Evaluates the Rayleigh-class invariant `κ` at the canonical
operating point using the ED-SC 3.4-σ₁ calibration curve under
the provisional rules of GR-SC 1.3-Scoping (revised post-F1).
Four uncertainty components carried separately. No new kinematic
formulas. No execution required (pure algebraic substitution and
linear error propagation).
**Parents:**
- `theory/GR_SC_1_3_RayleighClass_Scoping.md` (scoping layer;
  Rules R1–R5; revised Rule R3 after F1 execution).
- `theory/ED_SC_3_4_sigma1_Calibration.md` + execution
  `outputs/ed_sc_3_4_sigma1/sigma1_calibration_summary.json`
  (σ₁ calibration).
- `theory/GR_SC_1_5_HorizonKappa_MotifStatistics.md` (tenth-pass
  arc; Rayleigh derivation and pooled-R2 anchor
  `κ/(|μ₁|σ₁) = 0.52 ± 0.05`).
- `theory/GR_SC_1_8_EIT_Extremal_ErrorBudget.md` (integration
  memo; clearance target `σ₁/κ_M^det < 0.036`).
- `theory/GR_SC_1_0_MotifCurvatureInvariants.md` (mapping layer;
  §5 authoritative table row for `κ` now evaluated here).
- `theory/GR_SC_1_1_RaychaudhuriClass_Predictions.md` and
  `theory/GR_SC_1_2_QuadraticClass_Predictions.md` (structural
  precedents for the three-then-four-component uncertainty
  pattern).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post GR-SC 1.3-Scoping + F1 execution).

---

## 1. Purpose

GR-SC 1.3-Scoping established Rules R1–R5 governing κ evaluation.
After the F1 execution, Rule R3 was revised: both bulk and
filtered Hessian-trace populations exhibit small positive median
bias, with the filter amplifying the bulk bias by ~9×. The
Rayleigh derivation's structural input is `Var(T_motif) = σ₁²`
(variance, second moment), which is **not directly broken by the
rigid-zero failure**. Rule R2's Gaussianity-model band
absorbs the combined heavy-tail and residual-bias approximation
error.

**Under Rules R1–R5 (with revised R3), this memo emits:**

- Central scale-free `κ(ξ_canonical) / |N̂'|`.
- Scale-free calibration curve `κ(ξ) / |N̂'|` across the canonical
  r_diag = 1 window.
- Four uncertainty components propagated separately (calibration
  CI, ensemble CI, per-realisation ±25 %, model-approximation
  ±10.9 %).
- Cross-check against the tenth-pass pooled-R2 anchor
  `κ/(|μ₁|σ₁) = 0.52 ± 0.05`.
- GR-SC 1.8 EIT-Extremal clearance ratio `σ₁/κ_M^det` at
  canonical ξ vs the engineering target `< 0.036`.

The kinematic constant `|N̂'|` is left symbolic throughout —
scale-free results are reported. A downstream memo (not GR-SC
1.3) will fix `|N̂'|` from the acoustic-metric calculation of
GR-SC 1.5 to convert scale-free numbers to dimensional values.

---

## 2. Inputs

| Quantity | Value | Source |
|---|---:|---|
| `σ₁_std(ξ)` fit | `0.000114 + 0.002876·ξ` | ED-SC 3.4-σ₁ OLS |
| `R²` of fit | 0.880 | ED-SC 3.4-σ₁ |
| RMS residual | 0.000126 | ED-SC 3.4-σ₁ |
| `σ₁_std` at canonical ξ = 1.7575 (fit) | **0.005169** | derived |
| `σ₁_std(ξ = 1.75)` grid central | 0.005135 | ED-SC 3.4-σ₁ |
| `σ₁_std(ξ = 1.75)` grid CI | [0.004664, 0.005509] | bootstrap 16–84 |
| `σ₁_std / σ₁_IQR_proxy` at canonical | 1.109 (10.9 % excess) | ED-SC 3.4-σ₁ |
| per-realisation spread (inherited) | ±25 % of σ₁_std | ED-SC 3.3.9 |
| Rayleigh scaling | `κ = |N̂'| · σ₁ / (2√2)` | GR-SC 1.5 |
| pooled-R2 anchor | `κ/(|μ₁|·σ₁) = 0.52 ± 0.05` | GR-SC 1.5 |
| EIT-Extremal target | `σ₁/κ_M^det < 0.036` (2σ) | GR-SC 1.8 |

**Provisional rules in force:**

- **R1:** `σ₁_std` primary; `σ₁_IQR_proxy` cross-check only.
- **R2:** Rayleigh scaling as leading-order approximation with
  ±10.9 % model band.
- **R3 (revised):** reading (a) — bulk and filter both slightly
  biased, filter amplifies. Does not affect variance-based
  Rayleigh scaling.
- **R4:** κ is ξ-dependent linearly with slope `|N̂'| · 0.001017`
  per unit ξ.
- **R5:** four uncertainty components, quoted separately.

---

## 3. Central values

**Scale-free Rayleigh scaling:** from GR-SC 1.5,

    κ(ξ) / |N̂'| = σ₁_std(ξ) / (2√2).

With `2√2 = 2.828427`, the σ₁_std OLS fit maps to:

    κ(ξ) / |N̂'| = (0.000114 + 0.002876·ξ) / 2.828427
                = 0.0000403 + 0.001017·ξ.

**At canonical `ξ_canonical = 1.7575`** (Gaussian Rayleigh
leading order):

    κ_Gauss(ξ_canonical) / |N̂'|
      = 0.0000403 + 0.001017 · 1.7575
      = 0.0000403 + 0.001787
      = 0.001828.

Equivalently, from the fitted `σ₁_std(1.7575) = 0.005169`:

    κ_Gauss / |N̂'| = 0.005169 / 2.828427 = 0.001828.

**F3 correction** (GR-SC 1.3-ModelCorrection, Student-t ν ≈ 30
fit from multi-seed Gaussianity ratio 1.023): multiplicative
factor `√((ν−2)/ν) = √(28/30) = 0.9661`. Applied:

    κ_central(ξ_canonical) / |N̂'| = 0.001828 × 0.9661
                                   = **0.001766**.

This is the **canonical scale-free κ value post-F3**. The
pre-F3 Gaussian Rayleigh value 0.001828 is retained in the
calibration curve (§4) as the intermediate Gaussian anchor but
is not quoted as the prediction; all downstream bands re-anchor
on 0.001766.

---

## 4. Calibration curve

Scale-free `κ(ξ) / |N̂'|` across the canonical r_diag = 1 window.
**Post-F3 values** incorporate the Student-t correction factor
0.9661 applied uniformly; pre-F3 Gaussian column is preserved as
the intermediate anchor:

| ξ | σ₁_std (fit) | κ/|N̂'| Gaussian | κ/|N̂'| post-F3 |
|---:|---:|---:|---:|
| 1.60 | 0.004716 | 0.001667 | **0.001610** |
| 1.65 | 0.004860 | 0.001718 | **0.001660** |
| 1.70 | 0.005004 | 0.001769 | **0.001709** |
| 1.75 | 0.005147 | 0.001820 | **0.001758** |
| **1.7575** | **0.005169** | 0.001828 | **0.001766** |
| 1.80 | 0.005291 | 0.001870 | **0.001807** |
| 1.85 | 0.005435 | 0.001921 | **0.001856** |
| 1.90 | 0.005579 | 0.001972 | **0.001905** |
| 1.93 | 0.005665 | 0.002003 | **0.001935** |
| 1.95 | 0.005722 | 0.002023 | **0.001954** |

Across the canonical window, post-F3 `κ/|N̂'|` grows from
**0.001610 to 0.001954** — a factor of **1.21×** monotonically,
unchanged from Gaussian (the correction is a constant
multiplicative factor). Much gentler ξ-dependence than `C²` in
GR-SC 1.2 (1.58× across the same window) because `κ` is linear
in σ₁ while `C²` is quadratic in S2.

---

## 5. Uncertainty components

All four components are mapped through the linear relation
`κ = |N̂'|·σ₁_std/(2√2)`; scale-free values are reported.

### 5.1 Calibration CI (from RMS residual)

Between grid points, the OLS-fit RMS residual serves as the
interpolation uncertainty on σ₁_std:

    δσ₁_std_calib = ±0.000126.
    δκ_calib / |N̂'| = ±0.000126 / 2.828 × 0.9661 = ±0.0000431.
    κ_calib band: [0.001723, 0.001809] around **0.001766** (post-F3).
    Relative: ±2.44 % (unchanged; correction factor is
    multiplicative and cancels in the relative).

### 5.2 Ensemble CI (bootstrap at nearest grid point)

The canonical ξ = 1.7575 sits 0.0075 from the ξ = 1.75 grid point
(0.43 % relative), within the OLS fit's residual distance, so
the nearest-grid bootstrap band applies:

    σ₁_std(ξ = 1.75) ∈ [0.004664, 0.005509].
    κ_ensemble (Gaussian) / |N̂'| ∈ [0.001649, 0.001948].
    **Post-F3 (×0.9661):** κ_ensemble / |N̂'| ∈ [0.001593, 0.001883].
    Relative about post-F3 central 0.001766: [−9.8 %, +6.6 %]
    (unchanged; the correction factor is multiplicative).

### 5.3 Per-realisation ±9.9 % on σ₁_std (F2 measured)

**Replaced 2026-04-23 by F2 execution.** The pessimistic ±25 %
transfer from ED-SC 3.3.9's S2 measurement has been superseded
by a direct σ₁_std measurement across 10 seeds at canonical ξ
(ED-SC 3.4-σ₁ Multi-Seed; artefact
`outputs/ed_sc_3_4_sigma1/sigma1_multiseed_summary.json`).
Measured coefficient of variation:

    σ₁_std_CoV = std(σ₁_std_seed) / mean(σ₁_std_seed)
               = 0.000554 / 0.005597
               = **0.0991**  (±9.9 %).

Applied linearly through `κ = |N̂'| · σ₁_std / (2√2)`:

    σ₁_std_per_real ∈ [0.005169 · (1 − 0.0991),
                       0.005169 · (1 + 0.0991)]
                    = [0.004657, 0.005681].
    κ_per_real (Gaussian) / |N̂'| ∈ [0.001647, 0.002009].
    **Post-F3 (×0.9661):** κ_per_real / |N̂'| ∈ [**0.001591**, **0.001941**].
    Relative about post-F3 central 0.001766: ±9.9 %
    (unchanged; measured; replaces ±25 % transfer).

**Tightening factor: 2.52×** (band shrinks to ~40 % of former
width). F2 also confirmed cross-seed rigid-zero
(`contains_zero = true` at the 10-seed aggregate level) and
found the cross-seed Gaussianity ratio 1.023 — much tighter
than the single-seed single-ξ value of 1.109. See §8 for the
uncertainty-hierarchy reordering consequence.

### 5.4 Model-approximation band (±10.78 % post-F3-verify, Student-t ν = 28)

**Revised 2026-04-23 by F3-verify MLE execution.** F3's
summary-statistic envelope `ν ∈ [20, 50]` (10-seed sampling of
the Gaussianity ratio) produced a ±1.61 % model band; F3-verify
(MLE Student-t fit on the raw pooled `T_motif` sample, N = 849
motifs) reveals that the **likelihood Hessian is shallow in the
ν direction** — the Fisher-information-based σ_ν = 23.05 at
ν_fit = 28.01, producing a much wider envelope than the sampling-
based F3 estimate.

**MLE fit diagnostics** (from
`outputs/ed_sc_3_4_sigma1/sigma1_model_verify_summary.json`):

- `ν_fit = 28.013` — 7 % below F3's summary-statistic ν = 30;
  well within F3's envelope [20, 50]; Student-t family validated
  by **KS p = 0.987** (K-S statistic 0.0153 on N = 849).
- `σ_ν = 23.05` (Hessian-based). The ν-marginal uncertainty is
  comparable in magnitude to ν itself — structural property of
  Student-t likelihood surfaces at moderate-to-large ν where
  the distribution approaches Gaussian and Fisher information
  on ν becomes small.
- `μ_fit = 2.18 × 10⁻⁴`, `σ_fit = 5.446 × 10⁻³`: both well-
  constrained; σ_μ = 1.94e−4, σ_σ = 2.08e−4.

**Honest-Hessian model band** (ν ∈ [ν_fit − σ_ν, ν_fit + σ_ν] =
[4.96, 51.07]):

    scale_factor band = [0.7724, 0.9802]
    κ_model / |N̂'| ∈ [0.001412, 0.001792]  around 0.001762
                                            (MLE central, 0.25 %
                                            below F3's 0.001766
                                            — negligible shift).
    Relative (half-width / central): **±10.78 %**.

**Rayleigh-preservation-restricted model band** (optional
secondary envelope; truncates the lower tail at `ν ≥ 15` where
F3 §3.4's Rayleigh-shape-preservation assumption remains valid):

    ν ∈ [15, 51.07]  →  scale_factor ∈ [0.9309, 0.9802]
    κ_model / |N̂'| ∈ [0.001702, 0.001792]  around 0.001762.
    Relative: **±3.4 %** (optional, assumption-dependent).

The ±3.4 % restricted band is the tighter envelope available
**if** one is willing to truncate the ν distribution at the
Rayleigh-shape-preservation boundary (ν ≥ 15); the ±10.78 %
honest-Hessian band is the one quoted as canonical because it
makes no additional assumption beyond the Student-t fit
itself.

**Summary of model-band evolution across the arc:**

| pass | method | band | notes |
|---|---|---|---|
| Pre-F3 (Gaussian) | conservative envelope from Gaussian-vs-empirical mismatch | ±10.9 % | Rule R2 |
| F3 (summary-statistic) | Student-t ν = 30, ν envelope [20, 50] | ±1.61 % | 10-seed sampling of Gaussianity ratio |
| **F3-verify (Hessian MLE)** | **Student-t ν = 28.01, σ_ν = 23.05 (Fisher)** | **±10.78 %** | **honest; canonical** |
| F3-verify (restricted) | Student-t, truncate ν ≥ 15 | ±3.4 % | optional, assumption-dependent |

The honest-Hessian band matches the pre-F3 Gaussian envelope in
magnitude (±10.78 % vs ±10.9 %) but for a different structural
reason: not Gaussian-vs-empirical mismatch but Fisher-information
shallowness in the ν direction. The F3 tightening claim
(±10.9 % → ±1.61 %) was an artefact of the summary-statistic
envelope being narrower than the likelihood actually supports;
F3-verify reverts the model band to post-F2 magnitude.

---

## 6. Prediction table

Scale-free `κ/|N̂'|` central value and four independent
uncertainty bands at canonical ξ = 1.7575:

**Post-F3-verify prediction table** (central unchanged at
0.001766 — MLE shift is only −0.25 %, well within calibration
band; model band revised to honest-Hessian ±10.78 %):

| Quantity | Central | Calib CI (RMS) | Ensemble CI | Per-real ±9.9 % (F2) | Model ±10.78 % (F3-verify) |
|---|---:|---:|---:|---:|---:|
| `κ / |N̂'|` | **0.001766** | [0.001723, 0.001809] | [0.001593, 0.001883] | [0.001591, 0.001941] | [**0.001412**, **0.001792**] |
| relative | — | ±2.44 % | [−9.8 %, +6.6 %] | ±9.9 % | **±10.78 %** |

**Uncertainty ranking (smallest to largest) post-F3-verify:**
**Calibration (2.4 %) < Ensemble (~8 % avg) < Per-realisation
(9.9 %) < Model (10.78 %, dominant).**

This **reverts to the post-F2 ordering** (model > per-real >
ensemble > calibration) with similar magnitudes: the F3
summary-statistic tightening of the model band to ±1.61 % was
an artefact of the 10-seed Gaussianity-ratio sampling envelope
being narrower than the Fisher-information Hessian supports.
The Rayleigh-preservation-restricted band ±3.4 % (see §5.4) is
the optional tighter alternative, but it requires an additional
assumption (ν ≥ 15) beyond the Student-t fit itself and is not
the canonical quote. **A single-realisation κ measurement is
expected to lie anywhere in `[0.001412, 0.001792] · |N̂'|`** —
a factor-of-1.27 range around the central. The ensemble average
remains tight (calib band ±2.4 %).

### 6.1 ξ-curve with combined envelope

If a single conservative envelope is needed (e.g. for external
citation), use the **model band** (now the largest component
post-F3-verify) and quote (with Student-t-corrected central):

    κ(ξ) / |N̂'| = 0.9661 · (0.0000403 + 0.001017·ξ) ± 10.78 %
               at each ξ in the canonical window [1.60, 1.95].

Equivalently, writing out the post-F3 central coefficients:

    κ(ξ) / |N̂'| = (0.0000389 + 0.000982·ξ) ± 10.78 %.

Per-realisation (±9.9 %) is nearly as large; quoting ±11 %
covers both the model and per-realisation bands with a small
conservative cushion.

Ensemble-level external citations (e.g. averaged experimental
observables over many repeats) should use the calibration band:

    κ(ξ) / |N̂'| = (0.0000389 + 0.000982·ξ) ± 2.4 %.

Ensemble-level external citations (e.g. averaged experimental
observables over many repeats) should use the calibration band:

    κ(ξ) / |N̂'| = (0.0000403 + 0.001017·ξ) ± 2.4 %.

---

## 7. Cross-check against tenth-pass pooled-R2 anchor

Tenth-pass GR-SC 1.5 reports

    κ / (|μ₁| · σ₁) = 0.52 ± 0.05

as the pooled-R2 empirical anchor. The Rayleigh scaling from the
same memo gives

    κ / σ₁ = |N̂'| / (2√2) = 0.35355 · |N̂'|.

Combining:

    0.35355 · 0.9661 · |N̂'| = 0.52 · |μ₁|  ±  0.05 · |μ₁|
    0.3416 · |N̂'|           = 0.52 · |μ₁|  ±  0.05 · |μ₁|
    |N̂'| / |μ₁|             = 0.52 / 0.3416
                             = **1.522**  ± 0.147 (9.6 % relative).

(Post-F3 Student-t correction factor 0.9661 absorbed into the
scaling. Pre-F3 Gaussian value was 1.471; the 3.4 % upward
shift mirrors the central-value correction.)

This is a **symbolic consistency relation** between the
kinematic constants `|N̂'|` and `|μ₁|`: the pooled-R2 anchor and
the Rayleigh scaling are mutually consistent iff the constants
satisfy `|N̂'| = (1.47 ± 0.14) · |μ₁|`. Neither constant is
computed here; the ratio is a testable prediction that the
forthcoming acoustic-metric-calculation memo can verify.

**If** the kinematic ratio turns out to differ from 1.47 ± 0.14,
one of three things is happening:

- The pooled-R2 anchor is measuring a different (filtered vs
  bulk) ensemble than the Rayleigh derivation assumes — possibly
  related to the F1 filter-amplification mechanism; the factor
  ~9× amplification of median_T maps to a different correction
  on the variance σ₁² than on the median, and the sign + size
  of that correction would show up in the pooled-R2 anchor's
  deviation from 0.52.
- The Rayleigh scaling's Gaussianity assumption is dominating
  the discrepancy (Rule R2's ±10.9 % band).
- The tenth-pass derivation of one of the two has an
  undocumented factor (unlikely; both are derived from the same
  GRF-saddle machinery).

Quantitatively: if the kinematic calculation gives
`|N̂'| / |μ₁| ∈ [1.33, 1.61]`, the anchor agreement is
confirmed within its stated ±9.6 % uncertainty. Deviations
outside that range flag a load-bearing inconsistency that must
be resolved before GR-SC 1.8 can be quoted quantitatively.

---

## 8. GR-SC 1.8 EIT-Extremal clearance ratio

GR-SC 1.8 §6 specifies the engineering falsification-clearance
target

    σ₁ / κ_M^det < 0.036   (2σ).

At canonical ξ, `σ₁_std = 0.005169` (scale-free). For the
clearance target to be met:

    κ_M^det > 0.005169 / 0.036
             = **0.1436** (scale-free, same units as σ₁).

**Interpretation.** The engineering design target for the
EIT-Extremal protocol requires that the measured motif-
conditioned surface gravity `κ_M^det` exceed ~0.144 in units of
σ₁_std. Stated differently:

    κ_M^det / σ₁_std > 1/0.036 = **27.78**.

Using the **post-F3 central `κ / σ₁`** prediction from §7
(`0.3416 · |N̂'|`), the clearance condition becomes:

    0.3416 · |N̂'| > 27.78    (for the central prediction to
                                clear the 0.036 target)
    |N̂'|          > **81.4**.

So the design target translates into a kinematic lower bound on
`|N̂'|`: the acoustic-metric calculation must deliver
`|N̂'| ≳ 81.4` for the EIT-Extremal experiment to clear
falsification at 2σ using the Student-t-corrected central σ₁
prediction. (Pre-F3 Gaussian value was 78.6; the upward shift
is the Student-t correction factor 1/0.9661 = 1.035.)

**Uncertainty bands propagate (after F2 + F3 + F3-verify,
re-anchored on |N̂'| ≳ 81.4 central):**

- Using **calibration band** (±2.4 %): `|N̂'|` threshold shifts
  by ±2.4 % → `≥ 79.4` to `≥ 83.4`.
- Using **per-realisation band** (±9.9 %, measured F2):
  `|N̂'|` threshold shifts by ±9.9 % → `≥ 73.4` to `≥ 89.5`.
- Using **model band** (**±10.78 %, F3-verify honest-Hessian,
  now dominant**): `|N̂'|` threshold shifts by ±10.78 % → `≥
  72.6` to `≥ 90.2`.
- Optional **Rayleigh-preservation-restricted model band**
  (±3.4 %): `|N̂'|` threshold shifts by ±3.4 % → `≥ 78.6` to
  `≥ 84.2` (assumption-dependent).

**Post-F3-verify, the model band dominates the clearance
envelope** (range 17.6 scale-free-units from low to high),
followed closely by per-realisation (range 16.1 units). The
former (pre-F2) ±25 % transfer band gave `|N̂'| ∈ [58.9, 98.1]`
(range 39.2 units); post-F3-verify model envelope
`[72.6, 90.2]` (range 17.6 units) is **2.2× tighter overall**.
The model and per-realisation envelopes are now comparable in
magnitude (ratios within 10 %), so a single conservative
envelope at ±11 % covers both.

Ensemble measurements (many repeats) use the calibration band
and the threshold remains tight (±2 %; range 4.0 scale-free
units). This is the first quantitative handle on the GR-SC 1.8
clearance target in absolute terms. The remaining blocker for
an absolute clearance-vs-design evaluation is the kinematic
computation of `|N̂'|` from the acoustic metric.

### 8.1 F2 tightening note

The per-realisation band was the dominant uncertainty
component in the pre-F2 prediction layer (±25 %, 2.3× over the
next component). F2 replaced the ED-SC 3.3.9 S2-derived
transfer band with a direct σ₁ measurement and produced
**CoV = 9.9 %**, a **2.52× tightening factor**. Immediately
after F2, the model-approximation band (±10.9 %) and
per-realisation (±9.9 %) sat at near-parity; F3 then tightened
the model band further (see §8.2).

### 8.2 F3 tightening note (central-value shift + model band)

**F3** (GR-SC 1.3-ModelCorrection, 2026-04-23) replaced the
conservative Gaussianity envelope with a distribution-correct
Student-t derivation. Key results:

- **Best-fit family:** Student-t with `ν ≈ 30` (pinned by the
  F2 multi-seed Gaussianity ratio 1.023 via the analytical
  `R(ν)` table in the F3 memo §3.1).
- **Central-value shift:** κ correction factor `√((ν−2)/ν) =
  0.9661` applied uniformly. Post-F3 central
  `κ(ξ_canonical)/|N̂'| = 0.001766`, down from the Gaussian
  Rayleigh value **0.001828** (a 3.4 % structural correction,
  not an uncertainty).
- **Model band tightening:** `ν ∈ [20, 50]` envelope maps to
  κ/|N̂'| ∈ `[0.001734, 0.001791]`, half-width ±1.61 %. This
  is a **6.8× tightening** of the pre-F3 ±10.9 % band.
- **Hierarchy reorder:** the model band is now the **smallest**
  of the four uncertainty components. Post-F3 ordering:
  model (±1.61 %) < calibration (±2.4 %) < ensemble (~±8 %) <
  per-realisation (±9.9 %, new dominant again).

**Pooled-R2 consistency** tightens accordingly:
`|N̂'|/|μ₁| = 1.522 ± 0.147` (pre-F3 was 1.471 ± 0.141; the
3.4 % shift mirrors the central-value correction).

**GR-SC 1.8 clearance threshold** shifts to `|N̂'| ≳ 81.4`
(pre-F3: 78.6). Model-band clearance envelope narrows to
`[80.1, 82.7]`, a 6.6× tightening of the pre-F3 `[70.1, 87.2]`.
Per-realisation remains the dominant clearance-envelope
component at `[73.4, 89.5]`.

**F3-verify update (2026-04-23).** The caveat above was addressed
by executing the MLE fit on the raw pooled `T_motif` sample; see
§8.3 for the verdict. **Summary:** Student-t family validated
(KS p = 0.987), ν_fit = 28.01 (within F3 envelope [20, 50]),
central essentially unchanged (−0.25 % shift, within calibration
band), **but σ_ν from the likelihood Hessian is 23.05 — much
wider than F3's summary-statistic envelope of ±10**, revising
the honest model band to ±10.78 %. F3's tightening claim is
retracted; post-F3-verify hierarchy reverts to post-F2
ordering.

### 8.3 F3-verify note (hierarchy reverts)

**F3-verify** (GR-SC 1.3-ModelCorrection-Verify; executed
2026-04-23 via `analysis/scripts/ed_sc_3_4_sigma1_model_verify.py`)
MLE-fit the Student-t family to the raw pooled `T_motif`
sample (N = 849 motifs, regenerated deterministically from F2
evolution). Key outcomes:

- **ν_fit = 28.013**; σ_ν = 23.05 (from the Fisher-information
  Hessian at the MLE optimum). The ν central is within 7 % of
  F3's summary-statistic ν = 30, well inside F3's envelope
  [20, 50] — **F3's ν central is confirmed**.
- **KS p = 0.987** (K-S statistic 0.0153) — Student-t family
  validated as the correct parametric choice at the N = 849
  sample size. No need to explore generalized Gaussian or
  stretched exponential alternatives.
- **Model band widens to ±10.78 %** (honest Hessian) — F3's
  ±1.61 % tightening was an artefact of the summary-statistic
  sampling envelope being narrower than the likelihood
  actually supports at ν ≈ 28. The Rayleigh-preservation-
  restricted band ±3.4 % is an optional tighter alternative
  that assumes ν ≥ 15 (§5.4).
- **κ central shift is −0.25 %** (MLE 0.001762 vs F3 summary
  0.001766) — well within the calibration band ±2.4 %; the F3
  central **stands unchanged**.
- **Uncertainty hierarchy reverts to post-F2 ordering:**
  **model (±10.78 %, dominant) > per-real (±9.9 %) > ensemble
  (~±8 %) > calibration (±2.4 %).** F3's rearrangement (model
  becoming smallest) was a consequence of the artificially
  tight ±1.61 % band; with the honest Hessian, model is
  dominant again.

**Structural interpretation.** The Student-t log-likelihood
surface is asymptotically flat in ν for large ν (because
Student-t → Gaussian as ν → ∞). At ν ≈ 28 with N = 849, the
Fisher information on ν is shallow — much more so than on
μ or σ. This is a generic property of the family, not a
deficiency of F3-verify. The honest band is correspondingly
wide.

**Consequence for GR-SC 1.8.** Clearance envelopes must use
the ±10.78 % model band rather than F3's ±1.61 %:

- **Model band** `|N̂'|` threshold range ±10.78 % →
  `≥ 72.6` to `≥ 90.2` (honest-Hessian envelope).
- Per-realisation remains `[73.4, 89.5]` — model and per-real
  envelopes are now comparable again in magnitude.

The F3-verify outcome confirms F3's **structural** claim
(Student-t ν ≈ 28–30 is the correct family; central at
0.001766 is correct) while revising F3's **quantitative band
tightening** (the model band was not actually tightenable by
the F3 method; it matches the pre-F3 conservative envelope
under honest Hessian analysis).

---

## 9. Notable tensions and agreements with the tenth-pass scaling

**Agreement:**

- The Rayleigh scaling `κ = |N̂'|·σ₁/(2√2)` from GR-SC 1.5
  reproduces cleanly from the σ₁_std calibration under Rule R1.
- The pooled-R2 anchor `κ/(|μ₁|σ₁) = 0.52 ± 0.05` is
  structurally consistent with the Rayleigh scaling iff
  `|N̂'|/|μ₁| = 1.47 ± 0.14`; this becomes a testable prediction
  rather than a tension.
- The ξ-dependence of `κ` (slope `|N̂'| · 0.001017` per unit ξ)
  is the Rayleigh-scaling linear response to the ED-SC 3.4-σ₁
  linear σ₁_std(ξ) trend; no new mechanism required.

**Tensions (documented, not resolved here):**

- **Rigid-zero failure** (F1 reading (a)) does not break the
  Rayleigh scaling directly but does indicate the tenth-pass
  Trace-Gaussian derivation is incomplete; a correction-term
  note in GR-SC 2.0 Consolidation is owed. This memo marks the
  amendment as pending, not blocking.
- **Gaussianity failure** (σ₁_std > σ₁_IQR_proxy by 10.9 % at
  canonical ξ) means the Rayleigh-distribution shape is only
  approximate; the ±10.9 % model band reflects this. A
  dedicated non-Gaussian Rayleigh-equivalent derivation (F3) is
  optional and would tighten this band.
- **Per-realisation band transfer from ED-SC 3.3.9** is
  provisional; a multi-seed σ₁ measurement (F2) is required to
  replace the pessimistic ±25 % with a measured value. F2 is
  flagged as the next follow-up priority.

**No prediction is retracted.** The central κ value and its four
uncertainty bands stand; the two structural tensions (rigid-zero,
Gaussianity) are already absorbed by Rule R2's model band and
the flagged amendment to GR-SC 2.0.

---

## 10. Changelog

- **Rev. 1 (2026-04-23, this memo):** opens GR-SC 1.3 as the
  third quantitative GR-SC prediction layer. Under GR-SC 1.3-
  Scoping Rules R1–R5 (with revised R3 post-F1) evaluates the
  Rayleigh-class `κ` at canonical ξ. Scale-free central value
  `κ(ξ_canonical)/|N̂'| = 0.001828` (Gaussian Rayleigh). Linear
  calibration curve `κ(ξ)/|N̂'| = 0.0000403 + 0.001017·ξ`,
  growing 1.21× across the canonical window. Four independent
  uncertainty bands (calib ±2.4 %, ensemble ≈ ±8 % asymmetric,
  per-real ±25 %, model ±10.9 %) quoted separately per Rule R5.
  Cross-check with the tenth-pass pooled-R2 anchor reframes as a
  testable symbolic prediction `|N̂'|/|μ₁| = 1.47 ± 0.14`.
  GR-SC 1.8 clearance target `σ₁/κ_M^det < 0.036` translates to
  `|N̂'| ≳ 78.6` for central-prediction clearance at 2σ; four
  bands propagate through. No new kinematic formulas; no
  execution. Pure algebraic substitution and linear error
  propagation.
- **Rev. 1 F2 patch (2026-04-23):** per-realisation band replaced
  by direct σ₁ measurement (CoV = 9.9 %, down from inherited
  ±25 %); uncertainty hierarchy briefly had model (±10.9 %) as
  dominant; new §8.1 F2 tightening note.
- **Rev. 1 F3 patch (2026-04-23):** central value shifted from
  0.001828 → **0.001766** (Student-t ν ≈ 30 correction factor
  0.9661 applied); model band tightened from ±10.9 % to
  **±1.61 %** (6.8× tightening); pooled-R2 ratio updated to
  **1.522 ± 0.147**; GR-SC 1.8 clearance threshold updated to
  **|N̂'| ≳ 81.4**; uncertainty hierarchy reordered to
  **per-real (±9.9 %, dominant) > ensemble (~±8 %) > calibration
  (±2.4 %) > model (±1.61 %, smallest)**; new §8.2 F3 tightening
  note. All bands re-anchored on 0.001766; the pre-F3 Gaussian
  values are retained as intermediate anchors in §3–§5 but are
  not the canonical quotes.
- **Rev. 1 F3-verify patch (2026-04-23):** MLE fit on the raw
  pooled `T_motif` sample (N = 849) **confirms Student-t family
  via KS p = 0.987** and **confirms ν_fit = 28.013** (within F3
  envelope [20, 50]). However, the likelihood Hessian at the
  MLE optimum is **shallow in ν** (σ_ν = 23.05 from Fisher
  information), revealing that F3's ±1.61 % envelope was a
  summary-statistic artefact. Model band revised to the
  honest-Hessian **±10.78 %** (matches pre-F3 ±10.9 % in
  magnitude). Central shifts by only −0.25 % (0.001766 →
  0.001762); **canonical central remains 0.001766** (F3 value,
  within calibration band of F3-verify MLE). **Uncertainty
  hierarchy reverts to post-F2 ordering: model (±10.78 %,
  dominant) > per-real (±9.9 %) > ensemble (~±8 %) > calibration
  (±2.4 %).** Rayleigh-preservation-restricted ±3.4 % band
  noted in §5.4 as optional assumption-dependent alternative.
  New §8.3 F3-verify note. GR-SC 1.8 clearance envelopes under
  model band widen to `[72.6, 90.2]`. F3's structural claims
  (Student-t family, ν ≈ 28–30, κ central 0.001766) stand;
  F3's tightening claim (±10.9 % → ±1.61 %) is retracted.
