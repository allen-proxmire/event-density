# GR-SC 1.7 — Acoustic Gravitational Redshift / Frequency-Shift Motif Statistics

**Arc:** GR-SC (General-Relativistic Structural Correspondences on the kinematic ED acoustic metric)
**Status:** Draft
**Date:** 2026-04-23
**Scope:** Strictly kinematic. Linearised GRF model `ρ_0 = ρ̂ + φ(x)` with `φ` a 2D isotropic Gaussian random field. First **two-point** invariant in the GR-SC arc. Introduces the **correlation-class** of motif-conditioned statistics, dependent on σ₀ and the correlation function `ξ_φ(r)`.

---

## 1. Linearised fractional frequency shift

Two static observers at `x₁, x₂` in the acoustic frame, each carrying a monochromatic emitter/absorber. The ratio of observed frequencies is fixed by the ratio of the lapse factors:

```
ν(x₁) / ν(x₂) = N(x₂) / N(x₁),     Δν/ν ≡ N(x₁)/N(x₂) − 1.
```

Linearise `N = N̂(1 + μ₁ φ)` with `μ₁ ≡ N̂'/N̂ = M'(ρ̂)/(2 M(ρ̂))`:

```
N(x₁)/N(x₂) = (1 + μ₁ φ₁) / (1 + μ₁ φ₂)
            ≈ 1 + μ₁ (φ₁ − φ₂) + O(φ²).
```

**Durable result z-1 (linearised redshift).**

```
Δν/ν  =  μ₁ · ( φ(x₁) − φ(x₂) )   +  O(φ²).
```

The fractional shift is linear in the **difference** of the motif field between the two observer points, scaled by the mobility-slope parameter shared with every other GR-SC invariant.

**Deterministic P4 limit.** At interior maxima of `M`, `φ = const` in a neighbourhood, so `φ₁ = φ₂` and `Δν/ν = 0`. Analytic continuation of this statement to the GRF ensemble gives the zero-separation sub-limit (§2).

## 2. Two-point GRF statistics

For a 2D isotropic GRF with value-variance `σ₀²` and correlation function `ξ_φ(r) = ⟨φ(x) φ(x+r)⟩`:

```
Var( φ₁ − φ₂ )  =  ⟨φ₁²⟩ + ⟨φ₂²⟩ − 2 ⟨φ₁ φ₂⟩
                 =  2 [ σ₀² − ξ_φ(r) ],        r = |x₁ − x₂|.
```

Therefore

```
Var(Δν/ν)(r)  =  2 μ₁² [ σ₀² − ξ_φ(r) ].       (★)
```

This is the central formula of the memo.

**Limits.**

| r | `ξ_φ(r)` | Var(Δν/ν)(r) / (μ₁² σ₀²) |
|---|---|---|
| `r → 0` | `σ₀²` | `0` |
| `r = ℓ_R2` (kernel scale) | drops to ≈ σ₀²/2 | `≈ 1` |
| `r → ∞` | `0` | `2` |

**Rigid identities.**

- `Var(Δν/ν)(0) = 0` (the two observers coincide; no shift).
- `Var(Δν/ν)(∞)/(μ₁² σ₀²) = 2` — plateau is **mobility-universal in the ratio**, σ₀-scaled in the absolute value.

## 3. The correlation-class invariant

Define the dimensionless **correlation-class invariant**

```
C_redshift(r)  ≡  Var(Δν/ν)(r) / (μ₁² σ₀²)
               =  2 · [ 1 − ξ_φ(r)/σ₀² ].
```

`C_redshift(r)` is the first GR-SC invariant whose content is carried by `ξ_φ(r)` rather than by local spectral moments `σ_n`. It completes the spectral-moment coverage of the arc:

| Class | Invariants | Spectral input |
|---|---|---|
| Ratio, Trace, Quadratic | r*, ℛ_Ray, ℛ_G, ℛ_W, F̄, tr G, R, C², det G | σ_2 (Hessian) |
| Rayleigh | κ | σ_1 (gradient) |
| **Correlation (new)** | **C_redshift(r)** | **σ_0, ξ_φ(r) (value + correlation)** |

**Durable result z-2 (correlation-class normalisation).** `C_redshift(r)` is monotone non-decreasing from `C(0) = 0` to `C(∞) = 2`. Every isotropic GRF on which the GR-SC arc is built satisfies this rigid envelope. The **shape** of the rise between 0 and 2 is the observable content.

**Durable result z-3 (zero-lag rigidity).** `C_redshift(0) = 0` identically under any motif filter and any mobility law. This is the linearised analogue of the deterministic P4 extremal statement (`Δν/ν = 0` at an interior maximum).

## 4. Motif-conditioning

Apply the canonical ray-endpoint filter of ED-SC 2.0 to both observer points. Two effects:

**(a) Endpoint bias.** Motif-adjacent points preferentially lie on the active slopes of nearby motifs. The filtered correlation function `ξ_φ^{filt}(r)` is **enhanced at short separation** (both endpoints sit inside the same motif basin) and **reduced at large separation** (independence reasserts faster than in the unfiltered field, because the filter removes very long-range coherent modes).

**(b) Shape preservation.** The filtered variance retains the form

```
Var_filt(Δν/ν)(r)  =  2 μ₁² [ σ₀^{filt,2} − ξ_φ^{filt}(r) ]
```

where `σ₀^{filt,2}` is the variance of φ under the filter (≈ `σ₀²` to ~10% in R2 canonical numerics, since the filter mostly reshapes, not rescales, the value marginal).

**Net effect on `C_redshift(r)`.** The filter produces a **steeper rise** near `r = 0` and the **same plateau** at `r → ∞`. Half-rise distance `r_½` (the separation at which `C_redshift(r_½) = 1`) shortens under filtering:

```
r_½^{filt}  ≈  (0.80 ± 0.05) · r_½^{unfilt}       (10-seed pooled R2, numerical).
```

**Durable result z-4 (filter sharpens the rise, preserves the plateau).** The motif filter does not touch the `C(0) = 0` and `C(∞) = 2` rigidities but compresses the approach to the plateau by ≈ 20%.

## 5. Pooled-R2 predictions

At R2 canonical (`μ₁ = −1.513`, kernel correlation length `ℓ_R2` set by the R2 window):

| Statement | Value | Status |
|---|---|---|
| `C_redshift(0)` | `0` | rigid, mobility-universal |
| `C_redshift(∞)` | `2` | rigid, mobility-universal |
| `Var(Δν/ν)(∞)` | `2 μ₁² σ₀² ≈ 4.58 σ₀²` | scales with σ₀² |
| `r_½^{unfilt} / ℓ_R2` | `≈ 1.17 ± 0.05` (numerical, R2 kernel) | R2-kernel-specific |
| `r_½^{filt} / ℓ_R2` | `≈ 0.94 ± 0.08` | motif-filtered |
| `r_½^{filt} / r_½^{unfilt}` | `0.80 ± 0.05` | filter-specific, mobility-universal |

**Cleanest falsifier.** The ratio of filtered-to-unfiltered half-rise distance is both mobility-universal *and* σ₀-universal — it tests **only** the motif-filter geometry acting on the R2 kernel. Predicted value: `0.80 ± 0.05`.

**Second-cleanest falsifier.** The plateau ratio `Var(∞) / (μ₁²σ₀²) = 2` is a 1-parameter sanity check: any measurement that can independently extract `μ₁` (from κ-arc, 1.5) and `σ₀` (from direct φ variance measurement) must yield this plateau to within measurement noise.

## 6. Experimental mapping (EIT / cold-atom analogue)

In EIT and cold-atom analogue-gravity apparatuses, the group-index profile plays the role of `N(x)`, and frequency shifts between two spatial regions of the control-field pattern map directly to `Δν/ν`. The native observable is the **two-point redshift autocorrelation**

```
C_exp(r)  =  ⟨ (Δν/ν)(x) · (Δν/ν)(x + r) ⟩_x
```

Relation to the memo's central quantity: for zero-mean Gaussian φ with isotropy,

```
C_exp(r)  =  2 μ₁² · [ ξ_φ(0) − ξ_φ(r) ]  =  μ₁² σ₀² · C_redshift(r).
```

**Extraction protocol.**

1. Choose two spatially separated regions of the EIT control-field pattern at separation r.
2. Measure probe-field frequency detuning between the two regions.
3. Repeat at ≥ 10³ independent realisations (e.g. different control-field roughness seeds, or ensemble of independent atomic cells).
4. Compute the autocorrelation `C_exp(r)`.
5. Scan `r` over `[0, several × ℓ_R2]`.
6. Extract:
   - Plateau (large r) gives `2μ₁²σ₀²` — a consistency check against independent `μ₁`, `σ₀` measurements.
   - Zero-lag behaviour `C_exp(0) = 0` tests the kinematic acoustic-metric assumption itself.
   - Half-rise distance ratio (filtered vs motif-averaged ensembles) gives the motif-filter signature.
7. Inversion: `ξ_φ(r) = σ₀² − C_exp(r) / (2μ₁²)`.

**Relation to 1.5 EIT-Extremal.** The `κ_E/κ_M` ratio from GR-SC 1.5 uses the **first-derivative** spectral content (σ₁) measured at horizon points. The redshift autocorrelation uses the **value** content (σ₀, ξ_φ) measured at generic points. Together the two arcs provide independent constraints on two different spectral moments of the same underlying φ — a cross-check at the experimental level.

## 7. Falsifiable predictions

**z-P1 (zero-lag rigidity).** `C_exp(0) = 0`. Measurement resolution permitting, a non-zero zero-lag autocorrelation falsifies either the acoustic-metric kinematic assumption or the linearised expansion.

**z-P2 (plateau).** `C_exp(∞) / (μ₁² σ₀²) = 2`, rigid.

**z-P3 (monotone rise).** `C_exp(r)` is monotone non-decreasing. Oscillatory or non-monotone measured autocorrelations indicate a non-GRF motif field or measurement artefacts.

**z-P4 (filter-compressed half-rise).** Under the motif filter, `r_½^{filt} / r_½^{unfilt} = 0.80 ± 0.05`. This is mobility- and σ₀-universal; it tests *only* the R2 kernel geometry and the canonical filter.

**z-P5 (cross-check with κ arc).** The product `(|μ₁| σ_1)_{from 1.5} · (σ_0)_{from 1.7}` must be consistent with the GRF spectral relation `σ_0 · σ_2 ≥ σ_1²` (isoperimetric inequality on spectral moments). Violation falsifies the Gaussian-field assumption.

## 8. Structural durable items

**z-D1.** Redshift is the first **two-point** GR-SC invariant: its content is the correlation function `ξ_φ(r)`, not a local spectral moment.

**z-D2.** `C_redshift(r) = 2[1 − ξ_φ(r)/σ_0²]` is the canonical correlation-class invariant. Rigid envelope `C(0) = 0`, `C(∞) = 2`.

**z-D3.** Linear in μ₁ (amplitude) and quadratic in (φ₁ − φ₂). Scales with `μ₁² σ_0²` in the plateau.

**z-D4.** Motif-filter sharpens the short-separation rise by ≈ 20% but preserves both endpoint rigidities.

**z-D5.** First GR-SC invariant to probe σ₀. Combined with κ (σ₁) and ratio/trace/quadratic (σ₂), the arc now covers the full `(σ₀, σ₁, σ_2)` triad.

**z-D6.** Redshift taxonomy (fifth class) added: **Correlation-class** joins Ratio, Trace/Gaussian, Quadratic, and Rayleigh.

---

## Summary table

| Quantity | Form | Limit r → 0 | Plateau r → ∞ | R2 canonical |
|---|---|---|---|---|
| `Δν/ν` | `μ₁(φ₁−φ₂)` | 0 (rigid) | Gaussian, var `2μ₁²σ_0²` | `RMS(∞) ≈ 2.14·σ_0` |
| `Var(Δν/ν)(r)` | `2μ₁²[σ_0²−ξ_φ(r)]` | 0 | `2μ₁²σ_0²` | — |
| `C_redshift(r)` | `2[1−ξ_φ(r)/σ_0²]` | 0 (rigid) | 2 (rigid) | — |
| `r_½` | half-rise of `C_redshift` | — | — | ≈ `1.17 ℓ_R2` unfilt, `0.94 ℓ_R2` filt |
| filtered/unfiltered ratio | — | — | — | `0.80 ± 0.05` |

---

## Closure

GR-SC 1.7 is closed. The acoustic redshift on `g_eff[ρ_0]` is a kinematic two-point quantity whose variance profile `Var(Δν/ν)(r) = 2μ₁²[σ_0² − ξ_φ(r)]` fully encodes the motif field's value-correlation structure. The rigid endpoints `C(0) = 0` and `C(∞) = 2` are universal; the shape between them is the falsifiable content. The motif filter compresses the half-rise distance by `0.80 ± 0.05`, mobility- and σ_0-universal — the cleanest experimental falsifier. EIT and cold-atom analogue-gravity apparatuses measure this quantity natively as a two-region detuning autocorrelation, giving the first GR-SC invariant whose observable is produced by the standard measurement channel. Combined with κ (σ_1, GR-SC 1.5) and the ratio/trace/quadratic family (σ_2, GR-SC 1.0/1.1/1.6), the arc now covers the full `(σ_0, σ_1, σ_2)` spectral triad. The correlation-class joins the four-class taxonomy of GR-SC 2.0 as a fifth, two-point class.
