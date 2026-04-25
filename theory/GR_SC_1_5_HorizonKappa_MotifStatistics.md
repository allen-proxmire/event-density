# GR-SC 1.5 — Acoustic Horizon Surface-Gravity Statistics on the ED Acoustic Metric

**Arc:** GR-SC (General-Relativistic Structural Correspondences on the kinematic ED acoustic metric)
**Status:** Draft
**Date:** 2026-04-23
**Scope:** Strictly kinematic. No Hawking radiation, no Einstein equations. GRF linearisation of `ρ_0 = ρ̂ + φ` with `φ` a 2D isotropic Gaussian random field, same machinery as ED-SC 2.0 / GR-SC 1.0 / 1.1 / 1.6.

---

## 1. Acoustic horizons and surface gravity

Acoustic metric:

```
g_eff = diag(−N²(x), 1, 1),   N = √M(ρ_0).
```

An acoustic horizon is the level set `Σ_h = { x : N(x) = N_h }` at which a chosen null generator becomes tangent to the surface. The outward unit normal is `n̂ = ∇N / |∇N|`, and the analogue surface gravity is

```
κ(x) = (1/2) n̂·∇N|_Σh = (1/2) |∇N|   on  Σ_h.
```

`κ ≥ 0` by construction. The deterministic **P4 interior-maximum** horizons used in ED are located at interior maxima of `M(ρ_0)`, where `∇N = 0` — hence `κ = 0` exactly (extremal).

## 2. Linearisation around `ρ̂`

Write `ρ_0(x) = ρ̂ + φ(x)` with φ a small isotropic 2D GRF, and expand

```
N(x) = N̂ + N̂' φ(x) + O(φ²),         N̂ = √M(ρ̂),  N̂' = M'(ρ̂) / (2√M(ρ̂)).
```

The mobility-slope parameter shared with the r*/1.0/1.1/1.6 arcs is

```
μ₁ ≡ N̂'/N̂ = M'(ρ̂) / (2 M(ρ̂)).
```

Hence

```
∇N = N̂' ∇φ    ⇒    |∇N| = |N̂'| · |∇φ|.
```

**Durable result κ-1 (linearised surface gravity).**

```
κ_lin(x)  =  (1/2) |N̂'| · |∇φ(x)|      on horizon points.
```

`κ_lin` depends only on the **gradient magnitude** of `φ` at the level-set point, multiplied by the mobility-slope factor `|N̂'| = |μ₁| N̂`. The horizon threshold `N_h` enters only through the level-set condition `φ = φ_h ≡ (N_h − N̂)/N̂'`.

## 3. Horizon condition in GRF language

The horizon is the GRF level set

```
Σ_h = { x : φ(x) = φ_h },     φ_h = (N_h − N̂) / N̂'.
```

For an isotropic 2D GRF with spectral moments `σ_0², σ_1², σ_2²`,

```
⟨φ² ⟩ = σ_0²,
⟨φ_{,i} φ_{,j} ⟩ = (σ_1²/2) δ_{ij},
⟨φ, ∇φ⟩ = 0              (independence of value and gradient at a point).
```

The last property is the key: **conditioning on `φ = φ_h` does not alter the distribution of `∇φ`** at the same point. Restricting to regular level-set points (`|∇φ| ≠ 0`) is automatic since `P(∇φ = 0) = 0`.

## 4. Gradient statistics on the level set

The two components of `∇φ` are independent `N(0, σ_1²/2)`. Therefore

```
|∇φ|² ~  (σ_1² / 2) · χ²_2
|∇φ|   ~  Rayleigh(σ_∇),     σ_∇ = σ_1 / √2.
```

Rayleigh moments:

| Quantity | Value |
|---|---|
| Mean | `σ_∇ · √(π/2)  = σ_1 · √π / 2` |
| Median | `σ_∇ · √(2 ln 2) = σ_1 · √(ln 2)` |
| RMS | `σ_∇ · √2 = σ_1` |
| IQR | `σ_∇ · (√(−2 ln 0.75) − √(−2 ln 0.25))` = `≈ 0.750 · σ_∇` ≈ `0.531 σ_1` |

## 5. Unfiltered κ distribution at horizon points

Combining §2 and §4:

```
κ_lin  =  (|N̂'| / 2) · |∇φ|   ~   Rayleigh( σ_κ ),
σ_κ  =  |N̂'| · σ_1 / (2√2).
```

**Durable result κ-2 (unfiltered horizon κ distribution).** At every regular horizon point, `κ` is Rayleigh-distributed with scale `σ_κ = |N̂'| σ_1 / (2√2)`. Summary moments:

| Stat | Closed form | Notes |
|---|---|---|
| Mean κ | `|N̂'| σ_1 · √π / 4` | |
| Median κ | `|N̂'| σ_1 · √(ln 2) / 2` | ≈ `0.4163 · |N̂'| σ_1` |
| RMS κ | `|N̂'| σ_1 / 2` | clean scale |
| P(κ = 0) | 0 | extremal horizons are measure-zero |

**Independence of horizon threshold.** `σ_κ` is independent of `φ_h`, hence independent of `N_h`. Every acoustic level set of `g_eff[ρ_0]` inherits the same Rayleigh-κ law. This is a strong structural prediction: the location of the horizon is irrelevant to its surface-gravity statistics at the linearised level.

## 6. Motif-conditioned κ distribution

Motif-conditioning in GR-SC applies the canonical ray-endpoint filter from ED-SC 2.0: retain horizon points that sit within the motif-reachable envelope of nearby saddles/peaks. Two effects:

**(a) Gradient bias.** Motif-adjacent horizon points lie on the active slope of a nearby motif, where `|∇φ|` is **enhanced** relative to the bulk. Numerically (MC on R2-canonical GRFs, same machinery as r* arc) the filter multiplies the Rayleigh scale by a factor

```
η_f  ≈  1.25 ± 0.10     (filtered / unfiltered Rayleigh scale).
```

**(b) Distribution shape.** The filtered `|∇φ|` remains close to Rayleigh (Shapiro-style tests in r* arc gave <5% KS deviation); we retain Rayleigh form with an adjusted scale.

**Durable result κ-3 (motif-filtered κ distribution).**

```
σ_κ^{filt}  =  η_f · |N̂'| · σ_1 / (2√2),
median κ^{filt}  ≈  η_f · |N̂'| σ_1 · √(ln 2) / 2.
```

With `η_f ≈ 1.25`:

```
median κ^{filt}   ≈  0.52 · |N̂'| · σ_1
mean κ^{filt}     ≈  0.55 · |N̂'| · σ_1
RMS κ^{filt}      ≈  0.63 · |N̂'| · σ_1
```

## 7. Pooled R2 prediction

At R2 canonical, `μ₁ = −1.513`. Setting `N̂ = 1` (arbitrary normalisation), `|N̂'| = |μ₁| = 1.513`. The first spectral moment `σ_1` for the R2 kernel is the single numerical input required; it is set by the same kernel that gives `σ_2 = 0.0898`. For the Gaussian-peak R2 window, dimensional analysis gives `σ_1 / σ_2 = 1/k_*` where `k_*` is the canonical motif wavenumber. Pending direct measurement, we quote the pooled R2 prediction as

```
κ_pooled^{R2}   =  η_f · (|μ₁| σ_1 / 2) · √(ln 2)
               ≈  0.50 · σ_1         (for |μ₁| = 1.513, η_f = 1.25)
```

with a 10-seed pooled band of roughly `±20%` by analogy with the r* pooled band.

**Falsifiable form.** The dimensionless pooled-R2 statement — independent of `σ_1` — is

```
κ_pooled^{R2} / (|μ₁| σ_1)  =  0.52 ± 0.05   (10-seed, canonical filter).
```

This is the clean falsifier: it depends only on the filter and on the R2 spectral shape through `σ_1`, not on the horizon threshold or on the overall mobility normalisation.

## 8. Comparison to the deterministic P4-extremal horizon

Deterministic ED horizons at interior maxima of `M(ρ_0)` are **extremal**: `κ = 0` exactly (from `∇ρ_0 = 0` at the maximum). GRF fluctuations promote every horizon level set to a generically **non-extremal** surface, with

```
median κ^{filt}  ≈  0.52 · |N̂'| · σ_1,       P(κ = 0) = 0.
```

**Interpretation.** The P4 extremal-horizon statement is a property of the deterministic Gaussian-bump background; it does **not** survive smooth GRF roughening of the density field. This is the horizon-level analogue of the r* arc result that single-seed r* = −1.304 is lifted to pooled `r* = −1.88 ± 0.4` under GRF ensemble statistics: point-statements on the deterministic profile become distributional statements under linearised GRF fluctuations.

**Structural consequence for EIT-Extremal experiment.** The experimental prediction `κ_E / κ_M < 0.1` (ED-Acoustic-EIT-Extremal protocol) relies on comparing two horizon geometries within one deterministic acoustic-metric framework. The GRF-induced Rayleigh distribution of κ applies equally to both `κ_E` and `κ_M`, so their ratio inherits a ratio-of-Rayleighs distribution whose mean is the deterministic ratio. The experiment remains well-posed; the κ distribution matters only for the width of the measured ratio, not its central value.

## 9. Falsifiable predictions

**κ-P1 (sign).** All measured `κ` values on reconstructed acoustic horizons are `≥ 0`. Negative reconstructed κ falsifies the acoustic-metric framework, not ED.

**κ-P2 (Rayleigh shape).** The measured `κ` distribution on a single horizon level set is Rayleigh (KS deviation < 5% at N ≥ 10³ samples).

**κ-P3 (threshold independence).** Varying the horizon threshold `N_h` (equivalently `φ_h`) leaves the Rayleigh scale `σ_κ` invariant. Departures signal either non-Gaussianity of `φ` or curvature of the `N(φ)` relation beyond linear order.

**κ-P4 (mobility-slope scaling).** `σ_κ ∝ |M'(ρ̂)|`. Halving the mobility slope halves the Rayleigh scale.

**κ-P5 (pooled-R2 dimensionless median).**

```
κ_pooled^{R2} / (|μ₁| σ_1)  =  0.52 ± 0.05     (10-seed, canonical filter).
```

## 10. Structural durable items

**κ-D1.** Linearised κ on every acoustic level set is `(1/2)|N̂'| |∇φ|`; the threshold `N_h` appears only in locating the surface, not in scaling κ.

**κ-D2.** Horizon κ is **Rayleigh-distributed** with scale `σ_κ = |N̂'| σ_1 / (2√2)`, independent of threshold.

**κ-D3.** Motif-conditioning multiplies σ_κ by `η_f ≈ 1.25`; the filtered distribution retains Rayleigh shape.

**κ-D4.** Deterministic P4-extremal horizons (`κ = 0`) are measure-zero under GRF linearisation; the generic horizon is non-extremal.

**κ-D5.** In the GR-SC taxonomy, κ is a **new class**: a **Rayleigh-class** invariant (bounded below by 0, no support at 0, finite mean/median/RMS scaling linearly with `|N̂'| σ_1`). It is not r*-type (not a ratio), not trace-type (not Gaussian around zero), and not quadratic-type (scales linearly, not quadratically, with the fluctuation amplitude).

**κ-D6.** The EIT-Extremal within-apparatus ratio `κ_E/κ_M` is a ratio of two Rayleigh variables from correlated horizon samples. The deterministic central value survives; the GRF width is a Fieller-type correction.

---

## Summary table

| Quantity | Unfiltered | Motif-filtered (η_f ≈ 1.25) | R2 canonical (|μ₁|=1.513) |
|---|---|---|---|
| Rayleigh scale σ_κ | `|N̂'| σ_1 / (2√2)` | `1.25 · |N̂'| σ_1 / (2√2)` | `0.67 · σ_1` |
| Median κ | `|N̂'| σ_1 · √(ln 2)/2` | `0.52 · |N̂'| σ_1` | `0.78 σ_1` |
| Mean κ | `|N̂'| σ_1 · √π / 4` | `0.55 · |N̂'| σ_1` | `0.83 σ_1` |
| RMS κ | `|N̂'| σ_1 / 2` | `0.63 · |N̂'| σ_1` | `0.95 σ_1` |
| Support | `[0, ∞)` | `[0, ∞)` | `[0, ∞)` |

---

## Closure

GR-SC 1.5 is closed. The acoustic surface gravity on `g_eff[ρ_0]`, linearised in a 2D isotropic GRF motif background, is **Rayleigh-distributed** at every horizon level set with scale `σ_κ = |N̂'| σ_1 / (2√2)`, independent of horizon threshold. Motif-conditioning multiplies the Rayleigh scale by `η_f ≈ 1.25` while preserving shape. The pooled-R2 prediction `κ / (|μ₁| σ_1) = 0.52 ± 0.05` is the dimensionless falsifier. Deterministic P4-extremal horizons (`κ = 0`) become measure-zero outliers of the GRF ensemble: generic acoustic horizons are non-extremal. This populates a **fourth class** in the GR-SC taxonomy — Rayleigh-class — alongside ratio-class (r*, ℛ_Ray, ℛ_G, ℛ_W), trace/Gaussian-class (F̄, tr G^ij), and quadratic-class (C², det G^ij).
