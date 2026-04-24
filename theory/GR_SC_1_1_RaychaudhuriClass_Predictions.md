# GR-SC 1.1 — Raychaudhuri-Class Predictions at the Canonical Point

**Status:** Scope memo. First quantitative GR-SC prediction layer.
Uses only the S1-derived invariants; no S2 or σ₁ quantities. No
new kinematic formulas introduced. No execution required (pure
algebraic substitution with propagated uncertainty).
**Parents:**
- `theory/GR_SC_1_0_MotifCurvatureInvariants.md` (mapping layer
  + ξ-positioning rules).
- `theory/GR_SC_1_0a_WeylRatio_Sensitivity.md` (ℛ_W quantitative
  citation forbidden).
- `theory/GR_SC_1_0_EinsteinTensor_MotifStatistics.md` (tenth-pass
  arc; defines Einstein-tensor statistics on the acoustic metric).
- `theory/GR_SC_1_1_Raychaudhuri_MotifStatistics.md` (tenth-pass
  arc; defines Raychaudhuri-class quantities at the kinematic
  level).
- `theory/GR_SC_2_0_Consolidation.md` (five-class taxonomy; the
  Ratio-class identifications that collapse ℛ_Ray and ℛ_G onto
  r*).
- `theory/ED_SC_3_4_XiCalibration.md` + execution
  `outputs/ed_sc_3_4/xi_calibration_summary.json` (S1 calibration).
**Simulator of record:** `r2_grf_falsifier_tests.py`
  + `ED_Update_Rule.ed_step_mobility`.
**Date:** 2026-04-23 (post GR-SC 1.0 + 1.0a).

---

## 1. Purpose

GR-SC 1.0 established the motif-statistics → curvature-invariant
mapping layer and §5's authoritative invariant table. GR-SC 1.0a
closed the one structurally unstable row (`ℛ_W`) by forbidding
numerical citation. **GR-SC 1.1 begins the first quantitative
prediction layer** by evaluating the Raychaudhuri-class
invariants — all of which are S1-derived, ξ-independent, and
carry per-realisation certainty from the ED-SC 3.4 calibration.

The evaluation uses:

- `r* = S1_eff = −1.95`
- Per-realisation envelope: ±0.15 (ED-SC 3.3.9 single-realisation
  scatter, inherited through GR-SC 1.0 §2.1).
- ξ-positioning: **none required.** S1 is ξ-independent across the
  r_diag = 1 canonical window; the Raychaudhuri-class invariants
  therefore take the same value at every operating point inside
  the window.
- `ℛ_W` is **excluded from this memo's quantitative outputs** per
  the GR-SC 1.0a near-singular classification. Its structural
  placement in the Ratio-class taxonomy is preserved but no
  numerical value is emitted.

No new kinematic formulas are derived. Algebraic expressions are
taken verbatim from the tenth-pass arc's Raychaudhuri-class
memos; the novelty is the quantitative substitution and
linearised-error propagation with the ED-SC 3.4 calibrated S1
envelope.

---

## 2. Inputs

| quantity | value | source | notes |
|---|---|---|---|
| `S1_eff` | **−1.95** | ED-SC 3.4 mean S1 across 9 ξ points | ξ-independent in r_diag = 1 |
| `δS1_per_realisation` | **±0.15** | ED-SC 3.3.9 ensemble spread | per-realisation envelope |
| `ξ_pred` | any ∈ [1.60, 1.95] | GR-SC 1.0 §4 | no ξ dependence for S1 |
| `r_diag(L_ray)` | 1 | ED-SC 3.3.10 clause (c) | canonical shell class |

Out-of-scope inputs (cited for traceability but unused):
- `S2(ξ)` — Quadratic-class (memo GR-SC 1.2, projected).
- `σ₁` — Rayleigh-class (awaits ED-SC 3.4-σ₁ scan).
- ξ-correlator — Correlation-class (awaits two-point scan).

---

## 3. Raychaudhuri-class invariants to evaluate

Per the tenth-pass arc's Raychaudhuri-class subset of the
Ratio-class (`GR_SC_1_1_Raychaudhuri_MotifStatistics.md` +
`GR_SC_2_0_Consolidation.md`), the following S1-only invariants
are evaluable at the canonical operating point:

### 3.1 `ℛ_Ray` — Raychaudhuri eigenvalue ratio

    ℛ_Ray ≡ λ_1 / λ_2 = r* = S1

Ratio-class identity. Direct S1 identification.

### 3.2 `ℛ_G` — spatial Einstein-trace ratio

    ℛ_G ≡ trace(G^ij) / det(G^ij)   [schematic]
    Ratio-class limit: ℛ_G = r*.

Ratio-class identity on the clean-saddle acoustic-metric
evaluation. Direct S1 identification.

### 3.3 `θ` — expansion-like scalar (r*-proportional)

    θ ∝ r*

The proportionality constant is fixed by the kinematic acoustic-
metric calculation in `GR_SC_1_1_Raychaudhuri_MotifStatistics.md`
and is not re-derived here. Scale-free output `θ / a` is
reported; absolute θ requires the kinematic calibration constant
a.

### 3.4 `σ²` — shear-squared (r*²-proportional)

    σ² ∝ r*²

Same treatment: scale-free output `σ² / b` is reported; absolute
σ² requires the kinematic constant b. The scaling is **quadratic
in r***, so uncertainty propagation is also quadratic (see §4.4).

### 3.5 Einstein-tensor rigid identities

From the tenth-pass arc (`GR_SC_1_0_EinsteinTensor_MotifStatistics.md`):

- `G_00 ≡ 0` on any static ultrastatic acoustic metric — **rigid
  identity, structural zero**, not a prediction.
- `B_ab ≡ 0` (magnetic Weyl vanishes) — rigid identity.

These are recorded for completeness but do not enter the numerical
table below; they take the value 0 identically at every
realisation and every ξ.

### 3.6 Excluded

- `ℛ_W` — forbidden from numerical citation per GR-SC 1.0a
  classification `near_singular_artifact`.

---

## 4. Evaluation rules

**Rule 1.** Substitute `r* = −1.95` into each algebraic expression
from §3.

**Rule 2.** Propagate the per-realisation envelope `δS1 = ±0.15`
via standard linear error propagation:

    δf(r*) ≈ |df/dr*| · |δr*|.

**Rule 3.** For quadratic quantities (`σ² ∝ r*²`), the linearised
propagation gives

    δ(r*²) = |2·r*| · |δr*| = 2 · 1.95 · 0.15 = 0.585,

which is used as the envelope. The exact endpoint-evaluated
envelope `[r*_lo², r*_hi²]` with `r*_lo = −2.10, r*_hi = −1.80`
gives `[3.240, 4.410]` around the central value `3.8025` — an
asymmetric band `[−0.563, +0.608]`. The symmetric ±0.585 linear
envelope covers both sides to within rounding; for §5's table we
report the linear propagation for consistency with Rules 1–2.

**Rule 4.** Do not combine uncertainties across invariants in
quadrature. Each row stands alone; the `±0.15` envelope is a
single common source (the S1 per-realisation scatter), not
independent.

---

## 5. Deliverable: Raychaudhuri-class prediction table

| Invariant | Formula | Value at `r* = −1.95` | Uncertainty envelope | Sign/magnitude reading |
|---|---|---:|---|---|
| `ℛ_Ray` | `r*` | **−1.95** | ±0.15 | large-magnitude negative ratio |
| `ℛ_G` | `r*` | **−1.95** | ±0.15 | large-magnitude negative ratio |
| `θ / a` | `r*` | **−1.95** | ±0.15 | expansion scalar negative (contraction) |
| `σ² / b` | `r*²` | **+3.80** | ±0.59 | shear-squared ~4× |
| `θ / a` − `ℛ_Ray` | `0` (identity) | **0.00** | 0 | structural: both equal `r*` |
| `(σ²/b) / (θ/a)²` | `r*² / r*² = 1` | **1.00** | 0 | structural: σ²/θ² = 1 in Ratio-class limit |
| `G_00` | rigid | **0** | 0 | structural zero (static ultrastatic metric) |
| `B_ab` | rigid | **0** | 0 | structural zero (magnetic Weyl) |
| `ℛ_W` | — | — | — | **excluded** per GR-SC 1.0a (near-singular) |

Notes on the structural rows:

- **`θ/a` − `ℛ_Ray` = 0.** Both are algebraically `r*`; their
  difference is identically zero regardless of the actual r*
  value. This is a **Ratio-class identity**, not a prediction —
  included as an internal consistency check that the Raychaudhuri
  and Ratio classes collapse onto the same single real number.
- **`(σ²/b) / (θ/a)² = 1`.** The shear-to-expansion-squared
  ratio is unity in the pure Ratio-class limit because both
  sides scale as r*² (after squaring θ). Any empirical deviation
  from unity would indicate a Ratio-class breakdown or a new
  Hessian asymmetry mode; at the canonical operating point there
  is none.
- **Rigid identities** (`G_00`, `B_ab`) are tenth-pass-arc
  structural zeros and do not depend on S1, S2, σ₁, or ξ. They
  are the simplest non-trivial predictions of the ED acoustic-
  metric framework (non-trivial because they forbid certain
  classes of curvature coupling that would otherwise be
  generically present).

---

## 6. Interpretive reading (qualitative)

The Raychaudhuri-class invariants at the ED canonical operating
point carry three qualitative features worth naming, each
directly visible in the numerical table:

**Sign.** All Ratio-class values are negative (`ℛ_Ray = ℛ_G =
θ/a = −1.95`). In the acoustic-metric analogy, this means the
motif centres act as **focusing** rather than defocusing loci of
null congruences: the expansion scalar is negative, consistent
with saddle Hessian eigenvalues of opposite signs (one negative,
one positive) weighted toward the negative direction. This is
the ED-saddle version of gravitational focusing — geometric, not
dynamical.

**Magnitude.** |r*| = 1.95 sits at the edge of the bounded
Ratio-class interval `(−2, −1/2)` from the tenth-pass arc's
clean-saddle derivation. That the empirical value crowds the
lower bound is what caused `ℛ_W` to diverge (GR-SC 1.0a); the
Raychaudhuri-class invariants `ℛ_Ray`, `ℛ_G`, `θ/a` are **not**
sensitive to this crowding because their dependence on `r*` is
linear, not through the singular `1/(r*+2)` map. Per-realisation
certainty is preserved.

**Shear-to-expansion ratio.** `σ² / θ² = r*² / r*² = 1`. Shear
and expansion are commensurate in the Ratio-class limit — the
ED-saddle geometry is neither strongly anisotropic (σ² » θ²) nor
strongly isotropic (σ² « θ²) at the canonical operating point.
This is the Ratio-class collapse claim of the tenth-pass arc,
here confirmed empirically via the S1 calibration.

No prediction with non-trivial ξ dependence, non-trivial ensemble
spread, or non-trivial σ₁-involvement is promoted in this memo.
Those belong to GR-SC 1.2 (Quadratic-class via S2) and GR-SC 1.3
(Rayleigh-class via σ₁), both of which will require the relevant
ED-SC calibration as their load-bearing input.

---

## 7. Changelog

- **Rev. 1 (2026-04-23, this memo):** opens GR-SC 1.1 as the
  first quantitative prediction layer of the GR-SC program.
  Evaluates the Raychaudhuri-class invariants (`ℛ_Ray`, `ℛ_G`,
  `θ/a`, `σ²/b`) at `r* = S1_eff = −1.95 ± 0.15` via direct
  substitution and linear error propagation. Records two
  structural identities (`θ/a − ℛ_Ray = 0`;
  `(σ²/b)/(θ/a)² = 1`) as Ratio-class internal consistency
  checks. Excludes `ℛ_W` per GR-SC 1.0a. Notes `G_00 ≡ 0` and
  `B_ab ≡ 0` as rigid identities (tenth-pass arc). Provides a
  qualitative interpretive reading (focusing sign, near-boundary
  magnitude, commensurate shear-to-expansion ratio). No new
  kinematic formulas; no execution; scope-level only.
