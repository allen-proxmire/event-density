# GR-SC 1.2 — Quadratic-Class Predictions at the Canonical Point

**Status:** Scope memo. Second quantitative GR-SC prediction layer.
Evaluates the Quadratic-class invariants (`C²`, `det G`) at the
canonical operating point using the ED-SC 3.4 S2(ξ) calibration
curve. Three uncertainty components carried separately per the
ensemble-only qualification of S2. No new kinematic formulas
introduced. No execution required (pure algebraic substitution with
propagated uncertainty).
**Parents:**
- `theory/GR_SC_1_0_MotifCurvatureInvariants.md` (mapping layer +
  §4 three-component uncertainty rule).
- `theory/GR_SC_1_1_RaychaudhuriClass_Predictions.md` (first
  quantitative prediction layer; S1-derived).
- `theory/GR_SC_1_6_WeylTensor_MotifStatistics.md` (tenth-pass arc
  Weyl-squared analysis on the acoustic metric).
- `theory/GR_SC_2_0_Consolidation.md` (Quadratic-class taxonomy).
- `theory/ED_SC_3_4_XiCalibration.md` + execution
  `outputs/ed_sc_3_4/xi_calibration_summary.json` (S2 calibration).
- `theory/ED_SC_3_3_9_EnsembleVsRealisation.md` (ensemble-only
  qualification + per-realisation ~25 % spread).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post GR-SC 1.1).

---

## 1. Purpose

GR-SC 1.1 evaluated every S1-derived Ratio-class invariant at the
canonical operating point with per-realisation certainty. **GR-SC
1.2 now evaluates the S2-derived Quadratic-class invariants** —
the second and final quantitatively-evaluable class of the GR-SC
1.0 §5 authoritative map:

- **`C²`** — the Weyl-squared / quadratic curvature analogue
  (`⟨C²⟩ ≈ 2.44·μ₁²·σ_2²` in the tenth-pass arc's clean-saddle
  scaling; this memo evaluates only the `S2²` part, leaving `μ₁²`
  as a kinematic-calibration constant).
- **`det G`** — the determinant-like quadratic invariant scaling
  as `S2² / N̂²`, with `N̂` the motif-centre normal-field mean.

Both quantities depend on `S2(ξ) = −0.322 + 1.396·ξ`, the
linear-in-ξ calibration curve from ED-SC 3.4. **Both inherit
ensemble-only certainty** per ED-SC 3.3.9: per-realisation S2
spread is ~25 % and is not suppressed by higher N. Consequently,
every Quadratic-class prediction must carry three distinct
uncertainty components, enumerated in GR-SC 1.0 §4 and
instantiated here.

---

## 2. Inputs

| quantity | value | source |
|---|---:|---|
| `S2(ξ)` | `−0.322 + 1.396·ξ` | ED-SC 3.4 OLS fit |
| `ξ_canonical` | **1.7575 lu** | ED-SC 3.1 rev. 3 |
| `S2_fit(ξ_canonical)` | **2.132** | from fit |
| `S2(ξ = 1.75)` grid value | 2.320 | ED-SC 3.4 table row (closest grid to canonical) |
| `S2(ξ = 1.75)` grid CI | [1.971, 2.821] | bootstrap 16–84 |
| `RMS_residual` | **0.124** | ED-SC 3.4 S2 OLS fit |
| per-realisation spread | **±25 %** of S2 | ED-SC 3.3.9 |

The canonical ξ = 1.7575 lu sits 0.0075 from the ξ = 1.75 grid
point (0.43 % relative) and 0.0425 from ξ = 1.80 (2.43 %). The
nearest-grid bootstrap CI is therefore the ξ = 1.75 row: S2 =
2.320, CI [1.971, 2.821]. Half-widths: lower 0.349, upper 0.501;
symmetric approximation ±0.425.

**Out-of-scope inputs** (cited for traceability):

- `μ₁²` — kinematic prefactor for `C²`; not re-derived here.
- `N̂²` — normal-field normalisation for `det G`; not re-derived
  here.
- `σ₁` — Rayleigh-class; awaits ED-SC 3.4-σ₁ scan.

---

## 3. Invariants to evaluate

### 3.1 `C²` — Weyl-squared / quadratic curvature analogue

    C²(ξ) ∝ S2(ξ)²                  (tenth-pass Quadratic-class scaling)

The proportionality constant is `2.44·μ₁²` in the clean-saddle
limit; GR-SC 1.2 reports the scale-free quantity

    C²(ξ) / (2.44·μ₁²) = S2(ξ)²

and leaves `μ₁²` as a kinematic output from
`GR_SC_1_6_WeylTensor_MotifStatistics.md`, not re-derived here.

### 3.2 `det G` — determinant-class invariant

    det G(ξ) ∝ S2(ξ)² / N̂²         (Quadratic-class scaling with
                                     normal-field normalisation)

Central value at canonical ξ:

    det G(ξ_canonical) ∝ S2_fit² / N̂² = 2.132² / N̂²
                     = 4.545 / N̂².

---

## 4. Evaluation rules

**Rule 1. Central values.** Compute at `ξ = ξ_canonical = 1.7575`.

- `S2_fit(ξ_canonical) = −0.322 + 1.396 · 1.7575 = 2.132`.
- `C²/(2.44·μ₁²) = S2_fit² = 2.132² = 4.545`.
- `det G · N̂² / (unknown kinematic constant b) = 2.132² = 4.545`.

**Rule 2. Three uncertainty components propagated separately.**
Each component is applied to S2 at its raw magnitude, then mapped
through the quadratic `f(S2) = S2²` by **endpoint evaluation**
(honest, asymmetric) rather than linearised `±|2·S2|·δS2`
(symmetric, underestimates positive excursion). Linearised
values are reported alongside the endpoints as a sanity check.

**Component (i): Calibration CI (OLS-residual-band).** Between
grid points, the fit's RMS residual serves as the interpolation
uncertainty on S2:

    δS2_calib = ±0.124.
    S2 ∈ [2.008, 2.256]     → S2² ∈ [4.032, 5.090].
    Central C² band: [4.032, 5.090] around 4.545.
    Linearised equivalent: ±|2 · 2.132| · 0.124 = ±0.529 (symmetric).

**Component (ii): Ensemble-pool CI at nearest grid point.** The
canonical ξ sits 0.43 % from ξ = 1.75; the nearest grid bootstrap
band applies directly:

    S2_grid(1.75) ∈ [1.971, 2.821]  (16–84 bootstrap)
    S2² grid band: [1.971², 2.821²] = [3.884, 7.958].
    Central C² band: [3.884, 7.958] around 4.545.
    Linearised equivalent: ±|2 · 2.132| · 0.425 = ±1.812 (symmetric).

(Note: the grid-band central value S2_grid(1.75) = 2.320 differs
from the fit value S2_fit(1.7575) = 2.132 by about 9 %, within
the RMS residual 0.124. The ensemble CI should therefore be
interpreted as "what the ensemble-pool S2 could plausibly be
given a single 40-snapshot realisation on seed 77," not as a
confidence interval on `S2_fit`.)

**Component (iii): Per-realisation ±25 % on S2 (ED-SC 3.3.9).**

    δS2_per_real = ±0.25 · 2.132 = ±0.533.
    S2 ∈ [1.599, 2.665]   → S2² ∈ [2.557, 7.102].
    Central C² band: [2.557, 7.102] around 4.545.
    Linearised equivalent: ±|2 · 2.132| · 0.533 = ±2.273 (symmetric).

**Rule 3. No quadrature combination.** The three components
express different operational claims and are not independent
samples from a single noise distribution. Per GR-SC 1.0 §4, all
three are quoted separately on any downstream citation of
Quadratic-class predictions.

**Rule 4. det G inherits the same bands.** The `N̂²` factor is
kinematic and ξ-independent at fixed operating point; all three
bands apply to `det G · N̂²` in the same form as to `C²/(2.44·μ₁²)`.

---

## 5. Deliverable: Quadratic-class prediction table

Scale-free central values and the three independent uncertainty
bands, in endpoint-mapped (honest asymmetric) form.

| Invariant | Formula | Central at ξ_canonical | Calib CI band | Ensemble CI band | Per-real ±25 % band |
|---|---|---:|---:|---:|---:|
| `C² / (2.44·μ₁²)` | `S2²` | **4.545** | **[4.032, 5.090]** | **[3.884, 7.958]** | **[2.557, 7.102]** |
| `det G · N̂² / b` | `S2²` | **4.545** | [4.032, 5.090] | [3.884, 7.958] | [2.557, 7.102] |

(Both invariants share the scale-free value because their
kinematic normalisations `2.44·μ₁²` and `b/N̂²` factor out
uniformly across the three uncertainty components.)

**Linearised (symmetric) bands for comparison:**

| Invariant | Central | Calib ±δ | Ensemble ±δ | Per-real ±δ |
|---|---:|---:|---:|---:|
| `C² / (2.44·μ₁²)` | 4.545 | ±0.529 | ±1.812 | ±2.273 |
| `det G · N̂² / b` | 4.545 | ±0.529 | ±1.812 | ±2.273 |

Linearised bands **underestimate the upper excursion** in all
three columns because the map `S2 → S2²` is convex and the
central S2 is the positive-definite minimum of the quadratic. The
endpoint-mapped bands in the first table are the citable
quantities.

**ξ-dependence of C² across the scan range** (for downstream
non-canonical-ξ evaluations):

| ξ | S2_fit | S2_fit² |
|---:|---:|---:|
| 1.60 | 1.912 | 3.656 |
| 1.70 | 2.052 | 4.211 |
| 1.75 | 2.121 | 4.499 |
| 1.7575 | 2.132 | 4.545 |
| 1.80 | 2.191 | 4.800 |
| 1.90 | 2.331 | 5.432 |
| 1.95 | 2.400 | 5.762 |

Across the ξ scan `[1.60, 1.95]`, scale-free `C²` rises from
**3.66 to 5.76** — a factor of **1.58×** — monotonically and
smoothly.

---

## 6. Interpretive reading (qualitative)

**Monotonic ξ-dependence.** Unlike the Ratio-class invariants
(GR-SC 1.1), which are ξ-independent inside the r_diag = 1
window, the Quadratic-class invariants vary systematically with
ξ. `C²` grows by ~58 % across the canonical calibration window,
and `det G` scales identically. Any GR-SC 1.0+ prediction citing
`C²` or `det G` must declare `ξ_pred` explicitly — the canonical
ξ is the default but is not unique.

**Uncertainty component hierarchy.** Ordered by magnitude at the
canonical operating point:

- **Calibration CI** (±0.53 linearised, ±12 %): smallest; reflects
  only the fit's RMS residual around a smooth curve.
- **Ensemble-pool CI** (±1.81 linearised, ±40 %): moderate;
  reflects how the ensemble pool's S2 might differ from the fit
  value at the specific canonical ξ.
- **Per-realisation ±25 %** (±2.27 linearised, ±50 % on `C²`):
  largest; reflects the irreducible realisation-wise scatter
  characterised by ED-SC 3.3.9.

The per-realisation band dominates. A single-realisation
measurement of `C²` at the canonical operating point is expected
to lie anywhere in **[2.56, 7.10] · (2.44·μ₁²)**, roughly a
factor-of-3 range. The ensemble average is much tighter
(calibration band ±12 %), but a single observation should not be
compared against the ensemble band for falsification purposes —
it should be compared against the per-realisation band.

**How these feed into GR-SC 1.0+ predictions.** Three operational
rules:

1. **Ensemble predictions** (e.g., averaged over a large seed
   set) use the calibration CI band. `C²/(2.44·μ₁²) = 4.545 ±
   0.53` (linearised) or `[4.03, 5.09]` (endpoint-mapped).
2. **Single-realisation predictions** must use the per-realisation
   ±25 % band on S2 mapped through the quadratic. `C²/(2.44·μ₁²)`
   ranges over `[2.56, 7.10]` at the canonical operating point.
3. **Intermediate-ensemble predictions** (small-N seed sets, e.g.
   10 seeds as in ED-SC 3.3.6): use the ensemble-pool CI band.
   `C²/(2.44·μ₁²)` ranges over `[3.88, 7.96]`.

**No prediction is retracted.** Quadratic-class predictions from
the tenth-pass arc that were quoted at fixed ξ and without
explicit ensemble-vs-realisation qualification carry forward
structurally; their numerical values simply acquire the three-
component uncertainty structure recorded here.

---

## 7. Changelog

- **Rev. 1 (2026-04-23, this memo):** opens GR-SC 1.2 as the
  second quantitative GR-SC prediction layer. Evaluates
  Quadratic-class invariants `C²` and `det G` at the canonical
  operating point `ξ_canonical = 1.7575 lu` with scale-free
  value `S2_fit² = 4.545` at central S2 = 2.132. Propagates three
  independent uncertainty components (calibration CI ±0.53,
  ensemble CI ±1.81, per-realisation ±2.27 linearised) via
  endpoint-mapped quadratic propagation; quotes them separately
  per GR-SC 1.0 §4 rule. Provides ξ-dependence table across the
  calibration range (C² grows 1.58× from ξ = 1.60 to ξ = 1.95)
  and a three-tier guidance for downstream prediction forms
  (ensemble / intermediate / single-realisation). No new kinematic
  formulas; no execution; scope-level only.
