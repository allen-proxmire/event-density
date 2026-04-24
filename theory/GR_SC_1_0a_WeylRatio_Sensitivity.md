# GR-SC 1.0a — Weyl-Ratio Sensitivity Sweep

**Status:** Pre-registration + execution-ready (pure arithmetic; no
simulator call). Resolves the stability / citation-trustworthiness
question flagged by GR-SC 1.0 §3.1 on `ℛ_W` at the canonical
empirical operating point.
**Parents:**
- `theory/GR_SC_1_0_MotifCurvatureInvariants.md` §3.1 (defines
  `ℛ_W = −(2·S1+1)/(S1+2)`; flags near-pole behaviour at
  S1_eff = −1.95).
- `theory/ED_SC_3_4_XiCalibration.md` +
  `outputs/ed_sc_3_4/xi_calibration_summary.json` (provides
  S1_eff ≈ −1.95 with empirical 16–84 % range ≈ [−2.209, −1.733]
  across the scan's CIs).
- `theory/GR_SC_2_0_Consolidation.md` (tenth-pass arc five-class
  taxonomy; `ℛ_W` as bounded Ratio-class subclass in
  `(−2, −1/2)`).
**Simulator of record:** none required — the computation is
algebraic. Citation preserved for traceability: the S1 input values
come from `r2_grf_falsifier_tests.py` +
`ED_Update_Rule.ed_step_mobility` via the ED-SC 3.4 execution.
**Date:** 2026-04-23 (post GR-SC 1.0).

---

## 1. Purpose

GR-SC 1.0 §3.1 introduced

    ℛ_W(S1) ≡ −(2·S1 + 1) / (S1 + 2)

as the Weyl-like bounded-Ratio-class invariant, following the
tenth-pass arc's algebraic map from `r*` to the bounded Weyl
invariant in `(−2, −1/2)`. ED-SC 3.4's ξ-calibration inside the
canonical `r_diag = 1` window produced

    S1_eff = −1.95  (effectively constant, ±0.15 single-realisation
    scatter; OLS slope across ξ ∈ [1.60, 1.95] = 0.058, R² = 0.011).

At this value, `ℛ_W = −((−3.90) + 1) / (0.05) = +58.0` — an
**order-of-magnitude spike** caused by `S1 + 2 = 0.05` sitting at
the boundary of the `r* = −2` pole. GR-SC 1.0 flagged the
observable as "near-singular" and recommended a dedicated
sensitivity sweep before quoting the number in any external claim.

This memo executes that sweep analytically and classifies
`ℛ_W(S1_eff)` as either:

- **Quantitative prediction** — if the sensitivity is bounded, the
  derivative is finite on the entire 16–84 % S1 interval, and the
  condition number κ is `O(10)` or smaller across the central
  range.
- **Near-singular artefact** — if the sensitivity diverges within
  the 16–84 % S1 interval, the derivative is `O(10³)` or larger
  near S1_eff, and the condition number κ exceeds `O(100)`,
  indicating that any per-realisation S1 fluctuation of size
  ±0.05 produces `ℛ_W` fluctuations of order unity or larger.

This memo is pre-registration only. The deliverables §5 specify
the exact CSV and JSON the computation will emit; no numerical
values are preempted in §3 beyond the explicit definitions.

---

## 2. Input range

**Primary sweep.** `S1 ∈ [−2.00, −1.75] step 0.01` — 26 points,
denser than the ED-SC 3.4 bootstrap resolution and covering the
full 16–84 % S1 spread from the calibration.

**Excluded endpoint.** `S1 = −2.00` is the pole; `ℛ_W(−2)` is
undefined (division by zero). The driver reports `ℛ_W = None`
and derivative `= +inf` at this row, rather than failing.

**Marked annotations on the output:**

- **Empirical 16–84 % band.** From `xi_calibration_summary.json`,
  the full bootstrap 16–84 range across all 9 scan points is
  roughly `S1 ∈ [−2.30, −1.73]`. Take the most restrictive
  bracket inside the sweep: `S1_lo = −2.00` (pole-adjacent) and
  `S1_hi = −1.73`. Used to annotate the sensitivity table with a
  `within_empirical_band` boolean per row.
- **Canonical `S1_eff = −1.95`** (ED-SC 3.4 average): dedicated
  row flag.
- **Approximate S1_mean from ED-SC 3.4 scan table.** Mean of
  per-point S1 values `[−1.998, −1.969, −1.973, −1.967, −1.913,
  −1.783, −1.976, −1.997, −2.000]` = **−1.953**. This is the
  arithmetic-mean anchor; flag the closest row.

---

## 3. Computation

For each S1_k on the sweep:

1. **Weyl ratio:**

        ℛ_W(S1_k) = −(2·S1_k + 1) / (S1_k + 2)

2. **Derivative** (closed-form):

        dℛ_W / dS1 = d/dS1 [ −(2S1 + 1) / (S1 + 2) ]
                   = −[ 2·(S1 + 2) − (2S1 + 1)·1 ] / (S1 + 2)²
                   = −[ 2S1 + 4 − 2S1 − 1 ] / (S1 + 2)²
                   = −3 / (S1 + 2)².

   Always **negative** and **monotonically increasing in
   magnitude** as S1 approaches −2. At S1 = −1.95 the derivative
   is `−3 / 0.0025 = −1200`.

3. **Condition number** (relative sensitivity):

        κ(S1_k) = | (S1_k / ℛ_W(S1_k)) · (dℛ_W/dS1)(S1_k) |.

   Interpreted as: a 1 % change in S1 produces a κ·1 % change in
   ℛ_W. κ ~ 1 means well-conditioned; κ » 1 means ill-conditioned
   (sensitive).

**Analytic context (not in deliverables).** In the algebraic
limit S1 → −2, `S1 + 2 → 0` and `|dℛ_W/dS1| → ∞`; `ℛ_W → ∞`
with same sign as −(2·(−2)+1) = +3, i.e. `ℛ_W → +∞`. The pole
is one-sided: approaching from S1 = −2 + ε (ε > 0), ℛ_W takes
large positive values; from S1 = −2 − ε, ℛ_W takes large
negative values. ED-SC 3.4's empirical S1 values `[−2.00, −1.78]`
all lie on the `S1 > −2` side, so ℛ_W takes large positive
values throughout.

**Analytic context, continued.** Within the bounded Ratio-class
subclass `r* ∈ (−2, −1/2)`, the algebraic map `ℛ_W(r*)` takes
values in `(−2, −1/2)` as well — this is the tenth-pass arc's
boundedness claim. But **S1_eff = −1.95 sits at the edge of the
subclass domain**, not inside its interior. The 58.0 value
corresponds to a point where the bounded interpretation has
broken down. The sensitivity sweep will document where the
algebraic map remains in the bounded interpretation and where it
transitions to the unbounded near-pole regime.

---

## 4. Outputs

**Sensitivity table** (26 rows + the 16–84 % band annotations):

    S1_k,  ℛ_W_k,  dℛ_W/dS1_k,  κ_k,  within_empirical_band,  is_S1_eff,  is_S1_mean

**Interpretive block** in the summary JSON:

- `r_W_at_S1_eff`, `r_W_at_S1_mean` — values at the two empirical
  anchors.
- `derivative_at_S1_eff`, `derivative_at_S1_mean` — the
  `|dℛ_W/dS1|` at anchors.
- `condition_number_at_S1_eff`, `condition_number_at_S1_mean`.
- `kappa_max_within_band`, `kappa_min_within_band`,
  `kappa_median_within_band` across rows with
  `within_empirical_band = True`.
- **Stability classification**:
  - `quantitative_prediction` iff `κ_max_within_band < 10` AND
    `|dℛ_W/dS1|_max_within_band < O(10²)` (rule-of-thumb; the
    exact threshold is a modelling choice flagged in the memo).
  - `near_singular_artifact` iff `κ_max_within_band ≥ 100` OR
    the empirical band contains S1 values where
    `|dℛ_W/dS1| > 10³`.
  - `borderline` for intermediate cases, with an explicit
    narrative classification.
- **Recommended citation form for `ℛ_W`**:
  - If `quantitative_prediction`: report `ℛ_W(S1_eff) ± κ ·
    δS1_per_realisation`, with δS1 taken as the ED-SC 3.3.9
    ~0.15 per-realisation envelope.
  - If `near_singular_artifact`: **do not cite a numerical
    value**. Instead cite the bounded-Ratio-class structural
    claim (`ℛ_W ∈ (−2, −1/2)`) and flag that the empirical S1
    lies outside the bounded-subclass interior, so the
    algebraic map's bounded-interval prediction is not empirically
    validated at the current operating point.
  - If `borderline`: cite `ℛ_W` as a **range**, not a point,
    bracketed by the `ℛ_W(S1_lo)` and `ℛ_W(S1_hi)` values from
    the empirical band; propagate the full range forward as a
    conservative prediction.

---

## 5. Deliverables

- `outputs/gr_sc_1_0a/wy_sensitivity_table.csv` — flat rows per
  sweep point; columns match §4.
- `outputs/gr_sc_1_0a/wy_sensitivity_summary.json` — header
  metadata + interpretive block + stability classification +
  recommended citation form.

Driver (next turn): `analysis/scripts/gr_sc_1_0a_weyl_sensitivity.py`.
Expected wall time < 1 s (pure arithmetic on 26 points).

---

## 6. Changelog

- **Rev. 1 (2026-04-23, this memo):** opens GR-SC 1.0a as the
  Weyl-ratio sensitivity sweep. Pre-registers the 26-point S1
  sweep (−2.00 to −1.75 at Δ = 0.01), the closed-form derivative
  `dℛ_W/dS1 = −3/(S1+2)²`, the condition-number `κ = |S1 · (dℛ_W
  /dS1) / ℛ_W|`, and the three-way stability classification
  (`quantitative_prediction` / `near_singular_artifact` /
  `borderline`) with corresponding citation-form prescriptions.
  No numerics computed here; driver + execution are the next
  turn's work. Inputs are the GR-SC 1.0 algebraic map and the
  ED-SC 3.4 S1 calibration; no simulator re-run required.
