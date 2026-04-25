# GR-SC 1.8 — EIT-Extremal Error-Budget Integration

**Arc:** GR-SC (General-Relativistic Structural Correspondences on the kinematic ED acoustic metric)
**Status:** Draft, integration memo (no new curvature derivations)
**Date:** 2026-04-23
**Sources:** GR-SC 1.5 (horizon κ Rayleigh statistics), GR-SC 1.7 (redshift two-point correlation), ED-SC 2.0 (motif filter), `experiements/ED-Acoustic-EIT-Extremal_InProcess/` (experimental protocol)
**Role:** Translates the five-class GR-SC taxonomy into a quantitative error budget for the live EIT-Extremal `κ_E/κ_M < 0.1` test.

---

## 1. Deterministic EIT-Extremal prediction

The EIT-Extremal protocol compares two within-apparatus configurations of the EIT control-field spatial profile:

- **E-configuration:** control field shaped so the group-index profile `N_E(x)` has an interior maximum (P4 extremal horizon).
- **M-configuration:** control field shaped so `N_M(x)` has a standard smooth-max horizon (non-extremal baseline).

Deterministic kinematic-acoustic prediction:

```
κ_E / κ_M  <  0.1       (within-apparatus, single realisation, no noise).
```

At a deterministic interior maximum of `M(ρ_0)`, `∇N = 0` exactly, so `κ_E = 0` and the ratio vanishes. The `<0.1` bound is the engineering tolerance for how close the experimental E-profile can be made to true extremality.

**GRF upgrade.** GR-SC 1.5 shows the deterministic `κ = 0` is measure-zero under GRF roughening: generic horizons are non-extremal, with `κ` Rayleigh-distributed. The E-configuration picks up a non-zero GRF-induced κ floor. The M-configuration also acquires GRF corrections but on top of a non-zero deterministic baseline. **Question for this memo:** what is the GRF-induced width of the measured ratio `κ_E/κ_M`, and does it still clear the `<0.1` falsification threshold?

## 2. Inserting GRF corrections

### 2.1 From GR-SC 1.5

At any horizon level set, the linearised surface gravity is

```
κ  =  (1/2) |N̂'| · |∇φ|       ~  Rayleigh(σ_κ),
σ_κ  =  |N̂'| σ₁ / (2√2),       motif-filtered σ_κ^{filt} = η_f · σ_κ,  η_f ≈ 1.25.
```

Decomposition:

```
κ_E  =  κ_E^{det}  +  ΔκE,       ΔκE ~ Rayleigh-type GRF fluctuation at E-horizon,
κ_M  =  κ_M^{det}  +  ΔκM,       ΔκM ~ Rayleigh-type GRF fluctuation at M-horizon.
```

For the E-configuration, `κ_E^{det} ≈ 0` by design, so `κ_E ≈ ΔκE` and is **pure Rayleigh**. For the M-configuration, `κ_M^{det} > 0` and `ΔκM` is a Gaussian-like correction around it (the Rayleigh becomes approximately Gaussian-normal centred at `κ_M^{det}` when the deterministic magnitude dominates the fluctuation scale).

### 2.2 From GR-SC 1.7

Redshift-variance profile:

```
Var(Δν/ν)(r)  =  2 μ₁² [ σ_0² − ξ_φ(r) ],
C_redshift(r) =  2 [ 1 − ξ_φ(r)/σ_0² ],      rigid envelope C(0)=0, C(∞)=2.
```

This enters the error budget through the **inferred `N(x)` profile**: the EIT reconstruction of `N(x)` uses frequency-shift measurements between probe points. The variance of `Δν/ν` at separation `r` sets the noise floor on reconstructed `ΔN(x)`:

```
σ_N(r)^2 / N̂^2  =  Var(Δν/ν)(r)  =  2 μ₁² [ σ_0² − ξ_φ(r) ].
```

Propagating to gradient reconstruction, with pixel spacing `Δx`:

```
σ_{∇N}^2  ≈  (2 N̂² μ₁² / Δx²) · [ σ_0² − ξ_φ(Δx) ]
         ≈  (2 N̂² μ₁² / Δx²) · σ_0² · (1/2) · (Δx/ℓ_R2)²   for small Δx
         =  N̂² μ₁² σ_0² / ℓ_R2²        (leading-order small-Δx).
```

The zero-lag rigidity `ξ_φ(0) = σ_0²` makes the near-field reconstruction noise **finite** even in the `Δx → 0` limit, set by the R2 correlation length `ℓ_R2`. This is the structural statement: redshift correlation **caps** the reconstruction gradient-noise floor.

### 2.3 How fluctuations enter `κ_E` and `κ_M`

Two channels:

- **Channel A — intrinsic Rayleigh** (from 1.5): the horizon-point `|∇φ|` is Rayleigh-distributed under the GRF ensemble. Scales with `σ₁`.
- **Channel B — reconstruction (from 1.7):** the inferred `N(x)` is noisy at the level set `σ_0 · μ₁`, translated to `∇N` at level `|μ₁| σ_0 / ℓ_R2`. Scales with `σ_0 / ℓ_R2`.

Channel A is the physical fluctuation of the geometry; Channel B is measurement noise in the EIT reconstruction. Both enter additively in quadrature at the reconstructed-κ level:

```
σ_{κ,tot}²  =  σ_{κ,A}²  +  σ_{κ,B}²
           =  (|N̂'| σ₁ / (2√2))² · η_f²  +  (|N̂'| σ_0 / (2 ℓ_R2))²  · (geom factor).
```

## 3. Ratio-of-Rayleighs distribution

When both `κ_E` and `κ_M` are drawn from the same φ realisation (within-apparatus toggle), their fluctuations are **correlated**, since they share the underlying motif field on overlapping spatial regions.

Let

```
κ_E  =  r_E,         r_E ~ Rayleigh(σ_κ),
κ_M  =  κ_M^{det} + r_M',   r_M' partially correlated with r_E.
```

Two regimes:

**Regime (i) — E and M horizons spatially disjoint** (typical design):
Correlation coefficient `ρ_EM ≈ 0`. Then `κ_E/κ_M` is a ratio of a Rayleigh variable (small mean) and an approximately Gaussian variable (large mean). This is a Fieller-type ratio.

Fieller approximation for `κ_E ~ Rayleigh(σ_κ)` and `κ_M ~ N(κ_M^{det}, σ_κ^2)`:

```
median(κ_E/κ_M)  ≈  σ_κ · √(ln 2) / κ_M^{det}
                  =  σ_κ · 0.833 / κ_M^{det}.
```

With `σ_κ = |N̂'| σ₁ η_f / (2√2)` and introducing the **dimensionless GRF smoothness**

```
ε  ≡  σ_κ / κ_M^{det}  =  (η_f / (2√2)) · |N̂'| σ₁ / κ_M^{det},
```

we get

```
median(κ_E / κ_M)  ≈  0.833 · ε,
IQR ≈ 0.55 · ε,       (propagating Rayleigh quartiles through the ratio)
95% upper tail   ≈  1.80 · ε.
```

**Regime (ii) — E and M horizons spatially close / sharing motifs:**
Correlation coefficient `ρ_EM` up to ≈ 0.5. The ratio narrows: `σ_{ratio} → σ_{ratio} · √(1 − ρ_EM²)`. Median shifts only weakly (via second-order cross-moments). For the protocol's typical geometry, `ρ_EM ≈ 0.2–0.4`, giving a 10–20% tightening of the ratio width.

**Durable result E1.** The GRF-induced ratio `κ_E/κ_M` has median `≈ 0.83 · ε` with `ε = (η_f/(2√2)) · |N̂'| σ₁ / κ_M^{det}`, to be compared against the deterministic `<0.1` threshold.

## 4. Redshift-induced calibration uncertainty

The EIT reconstruction of `N(x)` proceeds by measuring probe-field detunings at a grid of spatial points. Each measurement carries irreducible noise set by the two-point redshift statistics:

```
Var(Δν/ν)(r=Δx)  =  2 μ₁² [σ_0² − ξ_φ(Δx)]  ≈  μ₁² σ_0² · (Δx/ℓ_R2)²   (small Δx).
```

Propagated to `∇N`:

```
σ_{∇N} / N̂  ≈  |μ₁| σ_0 / ℓ_R2.
```

Propagated to κ via `κ = (1/2)|∇N|`:

```
σ_{κ,B}  ≈  (N̂/2) · |μ₁| σ_0 / ℓ_R2  =  (1/2) |N̂'| σ_0 / ℓ_R2.
```

Comparing to Channel A:

```
σ_{κ,A}  =  |N̂'| σ₁ η_f / (2√2)     ≈  0.35 · |N̂'| σ₁.
σ_{κ,B}  ≈  (1/2) · |N̂'| σ_0 / ℓ_R2.
```

**Ratio of reconstruction-to-intrinsic noise.** Using the spectral-moment scaling `σ₁ ≈ σ_0 / ℓ_R2` (dimensional, holds to O(1) for any reasonable kernel):

```
σ_{κ,B} / σ_{κ,A}  ≈  (σ_0 / (2 ℓ_R2)) / (0.35 · σ_0 / ℓ_R2)  ≈  1.4.
```

**Durable result E2.** In the R2-canonical regime, **reconstruction noise (Channel B) is of the same order as intrinsic GRF noise (Channel A)**, with `σ_B/σ_A ≈ 1.4`. Both must be accounted for; neither dominates. Combined noise in quadrature:

```
σ_{κ,tot}  ≈  √(1 + 1.4²) · σ_{κ,A}  ≈  1.72 · σ_{κ,A}.
```

## 5. Combined error budget (pooled R2)

Putting everything together at R2 canonical (`|μ₁| = 1.513`, `N̂ = 1`, `η_f = 1.25`, `σ_B/σ_A ≈ 1.4`):

```
σ_κ^{tot}  ≈  1.72 · (η_f · |N̂'| σ₁ / (2√2))
          ≈  0.77 · |N̂'| σ₁
          ≈  1.17 · σ₁     (using |N̂'| = |μ₁| = 1.513).
```

Pooled-R2 **prediction for the ratio**, under the assumption that the M-configuration gives `κ_M^{det} ≈ 0.1 · N̂/ℓ_{horizon}` (standard EIT-horizon estimate):

```
ε_{tot}  =  σ_κ^{tot} / κ_M^{det}  ≈  1.17 σ₁ / κ_M^{det}.
```

The absolute numerical value depends on `σ₁` and on `κ_M^{det}`, both of which are apparatus-specific and are **independently measurable** in the EIT protocol. The dimensionless pooled-R2 prediction of the ratio's median is

```
median(κ_E/κ_M)  ≈  0.83 · ε_{tot}  ≈  0.98 · σ₁ / κ_M^{det}.
```

**Dominance analysis.** In R2 canonical, Channel B (redshift reconstruction noise) slightly dominates Channel A (intrinsic Rayleigh) — by factor ≈ 1.4. Reducing Channel B requires shorter probe spacing `Δx < ℓ_R2` (already saturated at `Δx = 0`) or denser averaging over independent cells. Reducing Channel A requires physically smoother ρ_0 preparation (smaller σ₁).

**Durable result E3.** The EIT-Extremal ratio width in R2-canonical conditions is

```
width(κ_E/κ_M)  ≈  σ_{ratio}  ≈  ε_{tot}  ≈  0.98 · σ₁ / κ_M^{det}     (10-seed pooled R2).
```

**Interpretation against the `<0.1` threshold.** The experiment succeeds (ratio clears the threshold) when

```
median(κ_E/κ_M) + 2σ  <  0.1
⇔  0.83 · ε_{tot} + 2 · ε_{tot}  <  0.1
⇔  ε_{tot}  <  0.035.
```

This sets the **experimental design requirement**:

```
σ₁ / κ_M^{det}  <  0.036        (pooled-R2, 2σ falsification clearance).
```

This is the cleanest engineering target the error budget produces.

## 6. Falsifiable predictions

**E-P1 (zero-lag rigidity).** EIT-measured `C_exp(0) = 0` to measurement resolution. Non-zero → falsifies the linearised acoustic-metric kinematic assumption.

**E-P2 (plateau).** `Var(Δν/ν)(∞) / (μ₁² σ_0²) = 2`. Independent check of kinematic assumption + GRF isotropy.

**E-P3 (κ pooled).** `κ_pooled / (|μ₁| σ₁) = 0.52 ± 0.05` (from GR-SC 1.5). Per-realisation measurement of κ at generic horizon level sets must satisfy this dimensionless law.

**E-P4 (spectral inequality).** `σ_0 · σ_2 ≥ σ_1²` must hold in measurements. Isoperimetric on GRF moments; violation → non-Gaussian motif field.

**E-P5 (ratio width).** `width(κ_E/κ_M) ≈ 0.98 · σ₁ / κ_M^{det}` (pooled R2). Empirical width inconsistent with this prediction falsifies either the Rayleigh-class model (1.5) or the correlation-class model (1.7).

**E-P6 (central value).** `median(κ_E/κ_M) ≈ 0.83 · σ_κ^{tot} / κ_M^{det}`, not zero. Any claim of `κ_E/κ_M = 0` within GRF noise regime contradicts the Rayleigh-class prediction.

**E-P7 (falsification clearance).** If `σ₁/κ_M^{det} < 0.036`, the experiment can falsify `κ_E/κ_M ≥ 0.1` at 2σ. If `σ₁/κ_M^{det} > 0.1`, the experiment cannot discriminate even under perfect kinematic-acoustic assumption.

## 7. Experimental protocol mapping

### 7.1 Independent measurement of `σ_0, σ_1, σ_2`

- **σ_0** (value variance of φ): measure `N(x)` at many points, take empirical variance of `(N − N̂)/N̂` divided by `μ₁²`.
- **σ_1** (gradient variance): measure `|∇N|²` at many points via finite-difference on the reconstructed `N(x)`; extract `σ₁² = ⟨|∇N|²⟩ / (2 N̂² μ₁²)`.
- **σ_2** (Hessian variance): measure second spatial differences of `N(x)` at a fine grid; extract `σ_2² = ⟨|H_N|²⟩ / (something analogous)`.

The three measurements give three numbers that must satisfy `σ_0 σ_2 ≥ σ_1²` (E-P4).

### 7.2 Extraction of `κ_E, κ_M`

For each configuration:

1. Reconstruct `N(x)` from probe-field detuning grid.
2. Locate the horizon level set `{x : N(x) = N_h}`.
3. Compute `|∇N|` on the level set.
4. Take `κ = (1/2)|∇N|` averaged over the level set (or at the horizon's saddle-like point).

Repeat over ≥ 10 independent control-field realisations (different motif seeds) to build a pooled-R2 κ ensemble.

### 7.3 Comparison to predicted distribution

1. Compute measured median and IQR of `κ_E/κ_M` over the ensemble.
2. Compare median to `0.83 · ε_{tot}` with `ε_{tot}` computed from measured σ_1 and κ_M^{det}.
3. Compare IQR to `0.55 · ε_{tot}`.
4. Test zero-lag redshift rigidity and plateau (E-P1, E-P2) as independent kinematic-assumption checks.
5. If measured `κ_E/κ_M` distribution falls below 0.1 with ≥ 2σ clearance, the deterministic prediction is confirmed *within* the kinematic acoustic-metric framework adopted by ED.

**Honesty caveat (unchanged).** The `κ_E/κ_M < 0.1` prediction is shared with standard analogue gravity; this memo does not claim ED-uniqueness of the central prediction. What this memo adds is a **calibrated noise model** and **clearance criterion** that translates the GR-SC arc's statistical machinery into an actionable experimental design target.

---

## Summary table

| Source | Contribution | Scale | R2 canonical |
|---|---|---|---|
| 1.5 intrinsic Rayleigh (A) | `σ_{κ,A} = η_f·|N̂'|σ₁/(2√2)` | σ_1 | 0.53 σ_1 |
| 1.7 reconstruction (B) | `σ_{κ,B} ≈ (1/2)|N̂'|σ_0/ℓ_R2` | σ_0/ℓ_R2 ≈ σ_1 | 0.76 σ_1 |
| Combined (quadrature) | `σ_{κ,tot}` | σ_1 | 0.93 σ_1 |
| Median(κ_E/κ_M) | `0.83 · σ_κ^{tot}/κ_M^{det}` | dimensionless | 0.77·σ₁/κ_M^{det} |
| Falsification clearance | `σ₁/κ_M^{det} < 0.036` | — | engineering target |

---

## Closure

GR-SC 1.8 integrates 1.5 and 1.7 into a quantitative error budget for the EIT-Extremal `κ_E/κ_M < 0.1` protocol. The ratio of surface gravities under GRF linearisation is a Fieller-type statistic whose median scales as `0.83·σ_κ^{tot}/κ_M^{det}`, with `σ_κ^{tot}` receiving **comparable** contributions from intrinsic Rayleigh fluctuations (Channel A, σ_1) and from redshift-induced reconstruction noise (Channel B, σ_0/ℓ_R2). In R2 canonical conditions Channel B slightly dominates (×1.4). The engineering design target `σ₁/κ_M^{det} < 0.036` is the cleanest deliverable: any EIT-Extremal apparatus meeting this target can falsify the `<0.1` prediction at 2σ within the kinematic acoustic-metric framework. Seven falsifiable predictions (E-P1 through E-P7) span zero-lag redshift rigidity, plateau, κ pooled law, spectral inequality, ratio width, ratio median, and clearance condition. The memo produces no new curvature derivations; it consolidates the five-class GR-SC taxonomy into a single experimental budget ready to hand to an EIT collaboration.
