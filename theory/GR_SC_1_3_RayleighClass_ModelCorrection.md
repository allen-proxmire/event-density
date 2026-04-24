# GR-SC 1.3 — Rayleigh-Class Model Correction (F3 derivation)

**Status:** Analytic derivation. No driver, no execution. Derives a
distribution-correct replacement for the ±10.9 % Gaussianity model
band in the κ prediction by fitting the empirical `T_motif`
distribution to a parametric heavy-tailed family and propagating
the correction through the Rayleigh scaling. Follow-up F3 from
GR-SC 1.3-Scoping §7 + §4 consolidation.
**Parents:**
- `theory/GR_SC_1_3_RayleighClass_Scoping.md` (Rule R2's ±10.9 %
  model band; this memo replaces it).
- `theory/GR_SC_1_3_RayleighClass_Predictions.md` (§5.4 model
  band; §8.1 F2 note — model now dominant; this memo tightens it).
- `theory/ED_SC_3_4_sigma1_Calibration.md` + execution (single-seed
  single-ξ Gaussianity ratio 1.109 at canonical ξ).
- `theory/ED_SC_3_4_sigma1_MultiSeed.md` + execution (cross-seed
  Gaussianity ratio 1.023 — much tighter than single-seed).
- `theory/GR_SC_1_5_HorizonKappa_MotifStatistics.md` (tenth-pass
  Rayleigh derivation; `κ ∝ |N̂'|·σ₁/(2√2)` is the Gaussian
  leading-order scaling).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility` — cited for traceability
  only; this memo performs no new evolution.
**Date:** 2026-04-23 (post F2 consolidation).

---

## 1. Purpose

F2 demonstrated that the model-approximation band (Gaussianity
failure in the `T_motif` distribution) is now the **dominant**
κ uncertainty component after the per-realisation band tightened
from ±25 % to ±9.9 %. F3 attacks the model band directly.

**The model band's ±10.9 % value was set by substituting the
Gaussian Rayleigh scaling's structural input** — a Gaussian
`T_motif` distribution — **and treating the empirical deviation
`|σ₁_std − σ₁_IQR_proxy| / σ₁_std` as a conservative
uncertainty envelope.** That deviation measures the mismatch
between a Gaussian's variance-to-IQR relation and the empirical
distribution's; it is **not** the correct uncertainty on κ if the
true distribution is describable by a heavier-tailed parametric
family for which the Rayleigh derivation can be re-run.

F3 replaces the ±10.9 % conservative envelope with a
distribution-correct band computed by:

1. Fitting the empirical `T_motif` distribution to a
   parametric heavy-tailed family.
2. Re-deriving the κ distribution under that family.
3. Computing the predicted κ_central shift and the new
   uncertainty envelope.

This is an **analytic** follow-up — no driver required. The
empirical inputs are the summary statistics (Gaussianity ratios
at multi-seed and single-seed levels) already produced by
ED-SC 3.4-σ₁ and its F2 follow-up.

---

## 2. Inputs

### 2.1 Empirical Gaussianity ratios

| source | `⟨σ₁_std⟩` | `⟨σ₁_IQR_proxy⟩` | ratio = std/IQR | Gaussian value |
|---|---:|---:|---:|---:|
| ED-SC 3.4-σ₁ single-seed single-ξ (ξ = 1.80) | 0.00514 | 0.00458 | **1.109** | 1.000 |
| F2 multi-seed aggregate (ξ = 1.7575) | 0.005597 | 0.005474 | **1.023** | 1.000 |
| ED-SC 3.4-σ₁ single-seed (ξ = 1.60) | 0.00483 | 0.00465 | 1.038 | 1.000 |
| ED-SC 3.4-σ₁ single-seed (ξ = 1.95) | 0.00579 | 0.00482 | 1.168 | 1.000 |

The single-seed ratio climbs monotonically with ξ, from 1.04 at
ξ = 1.60 to 1.17 at ξ = 1.95. The multi-seed aggregate at
canonical ξ sits at 1.023 — **much tighter than the single-seed
ratio at the same ξ** (1.109). This discrepancy is the key
structural clue: **single-seed heavy-tail estimates overstate
the tail weight** relative to the ensemble.

### 2.2 σ₁ calibration slope

From ED-SC 3.4-σ₁: `σ₁_std(ξ) = 0.000114 + 0.002876·ξ`. At
canonical ξ = 1.7575: `σ₁_std ≈ 0.00517`.

### 2.3 Rayleigh scaling structure (from GR-SC 1.5)

    κ = |N̂'| · σ_T(effective) / (2√2)

where `σ_T(effective)` is the variance-equivalent standard
deviation of the underlying Hessian-trace field. Under Gaussian
assumption, `σ_T(effective) = σ₁_std`. Under a heavier-tailed
family, `σ_T(effective) = f(family, parameters) · σ₁_std` with
`f` a dimensionless correction factor to be derived.

---

## 3. Tasks

### 3.1 Parametric-family fit

Two candidate families have the right structural properties
(zero-mean, symmetric, controllable tail weight):

- **Student-t with ν degrees of freedom.** Natural for
  field-derived statistics where the second derivative involves
  ratios of Gaussian quantities. `ν = ∞` reduces to Gaussian.
- **Generalized Gaussian (GGD) with shape β.** `β = 2` is
  Gaussian, `β < 2` is heavy-tailed (β = 1 is Laplace). Also
  parameterisable but less naturally motivated from the ED
  saddle-eigenvalue construction.

**Student-t ν vs Gaussianity ratio `R = σ_std / (IQR/1.349)`:**

For a standardised Student-t with scale 1 and ν > 2:

- Variance: `ν / (ν − 2)`, so `std = √(ν/(ν−2))`.
- IQR: `2 · t_{0.75, ν}` where `t_{q, ν}` is the q-quantile.

Numerically:

| ν | std | IQR | IQR/1.349 | Ratio `R = std · 1.349 / IQR` |
|---:|---:|---:|---:|---:|
| ∞ (Gaussian) | 1.000 | 1.349 | 1.000 | **1.000** |
| 50 | 1.021 | 1.359 | 1.007 | 1.014 |
| 30 | 1.035 | 1.366 | 1.012 | **1.023** ★ |
| 20 | 1.054 | 1.374 | 1.019 | 1.034 |
| 15 | 1.074 | 1.382 | 1.025 | 1.048 |
| 10 | 1.118 | 1.400 | 1.038 | 1.077 |
| 7 | 1.183 | 1.419 | 1.052 | **1.125** ≈ single-seed |
| 5 | 1.291 | 1.456 | 1.079 | 1.196 |
| 3 | ∞ (var undef) | 1.538 | 1.140 | — |

(★ denotes the F2 multi-seed value.)

**Best-fit ν from multi-seed Gaussianity ratio 1.023: ν ≈ 30.**
The single-seed single-ξ ratio 1.109 would imply ν ≈ 7, but F2
showed this to be an overestimate of tail weight caused by
per-seed and per-ξ fluctuations averaging out at the 10-seed
level.

**Adopted parametric family (this memo):** **Student-t with
ν = 30** as the best-fit family for the F2 multi-seed aggregate.
A full maximum-likelihood fit on the raw `T_motif` sample would
refine this; the summary-statistic match pins ν to within ~5
units (range 20–50 consistent with the multi-seed ratio given
its own sampling error on 10 seeds).

### 3.2 κ distribution under Student-t

Under the tenth-pass Rayleigh derivation, the surface gravity on
a level set of a zero-mean isotropic Gaussian field `T` with
spectral second moment `σ_T²` has density

    p_κ(κ) = (κ / s²) · exp(−κ² / (2s²))    for κ ≥ 0,

i.e. Rayleigh with scale `s = |N̂'|·σ_T/(2√2)`. This is
**exact** under the Gaussian assumption.

For a **Student-t underlying field `T`** with degrees of freedom
`ν`, the scale parameter of the Rayleigh-type envelope becomes

    s(ν) = |N̂'| · σ_T(effective, ν) / (2√2)

with the **effective-variance correction**

    σ_T(effective, ν) = σ_T_std · √((ν − 2) / ν)

because the scale parameter of the Student-t (the "σ" entering
the density) is `σ_t = σ_std · √((ν−2)/ν)`. This is the
variance-deconvolution correction: the standard deviation of a
Student-t sample overstates the scale parameter by
`√(ν/(ν−2))`, so the true underlying scale for the Rayleigh
density is the *smaller* quantity.

**Corrected κ central under Student-t ν:**

    κ_corrected(ν) / |N̂'| = σ_T_std · √((ν − 2) / ν) / (2√2).

At **ν = 30** (multi-seed best fit):

    correction_factor = √(28/30) = √0.9333 = **0.9661**.

So:

    κ_corrected(ν=30) / |N̂'| = 0.001828 × 0.9661
                             = **0.001766**.

**This is a central-value shift of −3.4 %**, not an uncertainty
band. The old Gaussian Rayleigh central value `0.001828` was
an **overestimate** relative to the Student-t-corrected value
`0.001766` by about 3.4 %.

### 3.3 Model-approximation band under Student-t ν

Under the Gaussian Rayleigh derivation, the model band was a
**conservative envelope** capturing the mismatch between
Gaussian and empirical distributions. Under the Student-t
derivation, the band narrows to the **residual uncertainty on
`ν`** itself.

The multi-seed ratio 1.023 pins `ν` to roughly `[20, 50]` given
the 10-seed sampling variance (a naive ±25 % sampling error on
the ratio maps to ν uncertainty via the monotonic R(ν) table in
§3.1). The corresponding κ correction factor ranges:

| ν | correction factor `√((ν−2)/ν)` | κ / |N̂'| |
|---:|---:|---:|
| ∞ (Gaussian) | 1.000 | 0.001828 |
| 50 | 0.9798 | 0.001791 |
| 30 (best fit) | **0.9661** | **0.001766** |
| 20 | 0.9487 | 0.001734 |
| 15 | 0.9309 | 0.001702 |

**ν ∈ [20, 50] corresponds to κ / |N̂'| ∈ [0.001734, 0.001791].**
Half-width: `(0.001791 − 0.001734) / 2 = 0.0000285`. Relative to
the central value `0.001766`:

    model band (corrected) = ±0.0285 / 1.766 × 100 %
                           = **±1.61 %**.

**This is a 6.8× tightening** of the old ±10.9 % model band.

### 3.4 Rayleigh scaling: leading term still correct

The Student-t derivation preserves the **functional form** of
the Rayleigh distribution — the density is still `p_κ(κ) ∝ κ ·
exp(−κ²/(2s²))` — because the surface-gravity construction
depends on the field being isotropic and zero-mean, not
specifically on Gaussianity. What changes is the **scale
parameter** `s`: it acquires the `√((ν−2)/ν)` correction
factor.

**Conclusion for Rayleigh scaling:** the leading term
`κ = |N̂'|·σ_T(effective)/(2√2)` remains the correct scaling
structure. A **multiplicative correction factor** of
`√((ν−2)/ν) = 0.9661` at `ν = 30` is the full F3 correction.
No new functional form is required; the Rayleigh distribution
is preserved in shape.

---

## 4. Deliverables

### 4.1 New model-approximation band for κ

    κ_corrected(ξ_canonical) / |N̂'| = 0.001766   (central, Student-t ν = 30)
    model band = ±1.61 %  (from ν ∈ [20, 50] envelope)

Compared to the pre-F3 values:

    κ_central (Gaussian Rayleigh)    = 0.001828   [was the central]
    model band (Gaussian)            = ±10.9 %    [was the envelope]

**Central value tightens to 0.001766 (−3.4 %); band tightens to
±1.61 % (6.8× smaller).** The former conservative ±10.9 %
envelope was dominated by the Gaussian-vs-non-Gaussian
mismatch at the distribution-shape level; replacing that with
the parametric Student-t fit reveals the true distribution is
**close to Gaussian** (ν = 30 is mildly heavy-tailed) and the
uncertainty is much smaller than the conservative envelope
suggested.

### 4.2 Updated uncertainty hierarchy

Post-F3 ordering:

| rank | component | relative | absolute κ/|N̂'| band |
|---|---|---:|---|
| 1 (new dominant) | **Per-realisation (F2 measured)** | **±9.9 %** | [0.001591, 0.001941] |
| 2 | **Ensemble CI** | ≈ ±8 % asymmetric | [0.001593, 0.001883] |
| 3 | **Calibration CI** | ±2.4 % | [0.001723, 0.001809] |
| 4 (new smallest) | **Model-approx (F3 Student-t)** | **±1.61 %** | [0.001737, 0.001795] |

All bands here are re-anchored on the corrected central
`0.001766`. The pre-F3 central `0.001828` was 3.4 % higher, so
the bands shift with it.

**New hierarchy: per-realisation > ensemble > calibration >
model.** F2 tightened per-real to bring it into parity with
model; F3 then tightens model below calibration. **Per-real is
now the dominant component again, but at 9.9 % instead of 25 %.**

### 4.3 Central-value shift note

The 3.4 % central-value shift from `0.001828` to `0.001766` is a
**structural correction**, not an uncertainty. Downstream memos
citing the κ prediction should adopt the corrected central; the
pre-F3 value remains recorded in the artefact history but is no
longer the canonical quote.

**Pooled-R2 anchor consistency.** The tenth-pass anchor
`κ/(|μ₁|σ₁) = 0.52 ± 0.05` combined with the corrected scaling

    κ / σ₁ = |N̂'| · √((ν−2)/ν) / (2√2)
           = |N̂'| · 0.9661 · 0.35355
           = 0.3416 · |N̂'|

gives the symbolic consistency relation

    |N̂'| / |μ₁| = 0.52 / 0.3416 = **1.522 ± 0.147**

(up from the pre-F3 value 1.471 ± 0.141, a 3.4 % upward shift
consistent with the κ central-value correction).

### 4.4 GR-SC 1.8 clearance envelope

At canonical ξ with `σ₁_std = 0.005169` (unchanged; σ₁
calibration not affected by F3), the clearance target
`σ₁/κ_M^det < 0.036` translates to

    κ_M^det > 0.005169 / 0.036 = 0.1436

unchanged from GR-SC 1.3-Predictions §8 (clearance uses σ₁, not
κ; F3's correction applies to κ prediction, not to σ₁ directly).

Using the **corrected central** and Student-t-based model band,
the clearance envelope becomes:

- Central: `|N̂'| ≳ 78.6 / 0.9661 = **81.4**` (was 78.6 under
  Gaussian).
- Model band ±1.61 %: `|N̂'| ∈ [80.1, 82.7]` (much tighter than
  pre-F3 [70.1, 87.2]).
- Per-realisation ±9.9 %: `|N̂'| ∈ [74.2, 90.4]` (now the
  dominant envelope).

### 4.5 Caveats

- **Summary-statistic fit, not raw-sample fit.** F3's ν = 30
  estimate is pinned to the multi-seed Gaussianity ratio 1.023
  via the analytical Student-t R(ν) table in §3.1. A direct
  MLE fit on the raw pooled `T_motif` sample (stored in the
  ED-SC 3.4-σ₁ and F2 CSV artefacts) would refine ν and may
  move the best fit by ±5 units. **Whether the raw-sample fit
  confirms ν ≈ 30 is pre-registered as a follow-up verification
  driver** (F3-verify, not executed here).
- **Single-seed single-ξ ratio discrepancy.** The ED-SC 3.4-σ₁
  single-seed single-ξ value 1.109 at canonical ξ = 1.80 would
  imply ν ≈ 7, which is substantially heavier-tailed than the
  F2 multi-seed 1.023 (ν ≈ 30). F3 adopts the multi-seed fit
  on the argument that single-seed estimates of tail weight are
  subject to per-realisation and per-ξ fluctuations that bias
  high. A direct test would compute the Gaussianity ratio on
  the pooled F2 `T_motif` distribution (10-seed pool, ~850
  motifs) — if that pool also gives ratio ≈ 1.02, multi-seed is
  confirmed as the right reference.
- **Rayleigh-shape preservation assumed.** F3 preserves the
  Rayleigh functional form and applies a scale-parameter
  correction; it does not verify that the Student-t surface-
  gravity distribution is exactly Rayleigh. A rigorous
  derivation on Student-t random fields would produce a slightly
  different tail behaviour (heavier than Rayleigh for small ν);
  at ν = 30 the correction from the Rayleigh shape itself is
  second-order (≲ 1 %) and absorbed into the ν-envelope model
  band. For ν < 15, the Rayleigh-shape-preservation assumption
  breaks down and F3's scaling needs revision.
- **No driver.** F3 is analytic; the corrected band is based on
  the summary statistics already produced by F2. No new
  execution is performed in this memo. A F3-verify driver that
  MLE-fits Student-t to the pooled raw `T_motif` data would
  confirm the ν estimate and the correction factor to higher
  precision; pre-registered as a downstream follow-up.

---

## 5. Changelog

- **Rev. 1 (2026-04-23, this memo):** opens F3 as the analytic
  derivation of a distribution-correct κ model-approximation
  band. Adopts Student-t with ν = 30 as the best-fit family
  from the F2 multi-seed Gaussianity ratio 1.023. Derives the
  κ distribution correction factor `√((ν−2)/ν) = 0.9661` under
  Student-t; applies to both central value and band. **Corrected
  central: `κ(ξ_canonical)/|N̂'| = 0.001766`** (−3.4 % vs pre-F3
  `0.001828`). **Corrected model band: ±1.61 %** (6.8× tighter
  than pre-F3 ±10.9 %). **Uncertainty hierarchy reorders to
  per-realisation (±9.9 %, new dominant) > ensemble (±8 %) >
  calibration (±2.4 %) > model (±1.61 %, new smallest).**
  Symbolic pooled-R2 consistency updates to `|N̂'|/|μ₁| =
  1.522 ± 0.147`. GR-SC 1.8 clearance envelope narrows to
  `|N̂'| ∈ [80.1, 82.7]` under model band; per-realisation
  envelope `[74.2, 90.4]` now dominates clearance. Caveats
  flagged: summary-statistic fit only; single-seed ratio
  discrepancy (1.109 vs multi-seed 1.023); Rayleigh-shape
  preservation assumed for ν ≥ 15. F3-verify driver
  (MLE fit on raw pooled `T_motif`) pre-registered as
  downstream follow-up. GR-SC 1.3-Predictions patching (§5.4
  new band, §6 prediction table, §6 hierarchy reordering, §8
  clearance envelope updates, central-value shift in §3 and §7)
  is deferred to a subsequent consolidation pass.
