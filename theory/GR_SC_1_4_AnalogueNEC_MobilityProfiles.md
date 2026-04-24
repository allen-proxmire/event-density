# GR-SC 1.4 — Analogue Null Energy Condition on the ED Acoustic Metric

**Arc:** GR-SC (General-Relativistic Structural Correspondences on the kinematic ED acoustic metric)
**Status:** Draft
**Date:** 2026-04-23
**Scope:** Strictly kinematic. Treats `ρ_0(x)` as a smooth deterministic background, not a GRF. Derives the condition on the mobility law `M(ρ)` under which the acoustic metric `g_eff[ρ_0]` satisfies the analogue null energy condition, `R_{μν} k^μ k^ν ≥ 0` on all `g_eff`-null vectors.

---

## 1. Acoustic metric and null vectors

Working in 2+1D with the canonical ED reversible slice:

```
g_eff = diag(−N²(x), 1, 1),   N(x) = √M(ρ_0(x)).
```

Null vectors `k^μ = (k^0, k^i)` satisfy `−N² (k^0)² + |k|² = 0`, i.e.

```
k^μ = (1/N, n̂),   |n̂| = 1.
```

## 2. The NEC scalar

From GR-SC 1.1, the non-zero Ricci components of a static ultrastatic metric are

```
R_{00} = N ∇²N,        R_{ij} = −N_{,ij} / N.
```

Hence

```
R_{μν} k^μ k^ν = R_{00} (k^0)²  +  R_{ij} n̂^i n̂^j
              = (∇²N)/N  −  (n̂·H_N·n̂)/N
              = (1/N) · [ tr(H_N) − n̂·H_N·n̂ ]
```

where `H_N` is the spatial Hessian of `N`. In 2D, for `n̂` aligned at angle `θ` to the `λ_1`-eigenaxis of `H_N`:

```
tr(H_N) − n̂·H_N·n̂ = λ_1 sin²θ + λ_2 cos²θ.
```

The minimum over `n̂` equals `min(λ_1, λ_2) = λ_min(H_N)`. Since `N > 0`:

**Durable result NEC-1.**

```
NEC holds for all null k^μ   ⇔   H_N(x) ⪰ 0   at every x.
```

The analogue NEC is equivalent to pointwise **convexity of N(x) = √M(ρ_0(x))**.

## 3. Reduction to mobility derivatives

Using `N = √M`:

```
N_{,i}  = M'(ρ) · ρ_{,i} / (2√M)
N_{,ij} = (1/(2√M)) · [ M' · ρ_{,ij}  +  ( M'' − (M')²/(2M) ) · ρ_{,i} ρ_{,j} ].
```

Therefore

```
H_N  = (1/(2√M)) · [ M' · H_ρ  +  Q(ρ) · ∇ρ ⊗ ∇ρ ],
Q(ρ) ≡ M''(ρ) − M'(ρ)² / (2 M(ρ)).
```

The NEC condition `H_N ⪰ 0` becomes

```
M'(ρ) · n̂·H_ρ·n̂   +   Q(ρ) · (n̂·∇ρ)²   ≥   0     for all unit n̂.    (★)
```

`(★)` is the **closed-form NEC inequality** for a general mobility law `M(ρ)` on a smooth background `ρ_0(x)`. It decomposes into:

- a **Hessian term** `M' · H_ρ`, sensitive to local curvature of the density;
- a **rank-1 gradient term** `Q(ρ) · ∇ρ⊗∇ρ`, sensitive to the density slope.

Two structural limits:

- **At a motif extremum** (`∇ρ = 0`): (★) reduces to `M'(ρ) · H_ρ ⪰ 0`.
  - At a maximum of ρ (`H_ρ ⪯ 0`) this needs `M'(ρ) ≤ 0` (mobility must be non-increasing in ρ, which all ED mobility laws satisfy).
- **On a steep slope** (`|∇ρ|` large): (★) is dominated by the sign of `Q(ρ)`. `Q ≥ 0` is the **sufficient** condition for NEC to survive the slope contribution when the Hessian term is friendly.

## 4. The canonical ED mobility families

### 4.1 Power-law (β-family) `M(ρ) = (1−ρ)^β`, `β > 0`

```
M'  = −β (1−ρ)^{β−1}
M'' = β(β−1)(1−ρ)^{β−2}
Q   = M'' − (M')²/(2M) = (1−ρ)^{β−2} · β(β−2)/2.
```

Sign of `Q` over `ρ ∈ [0,1)`:

| β | sign(Q) | Slope contribution |
|---|---|---|
| β > 2 | + | helps NEC |
| β = 2 | 0 | neutral |
| 0 < β < 2 | − | fights NEC |

At a motif maximum (`H_ρ ⪯ 0`, `∇ρ = 0`), `M' < 0` gives `M' H_ρ ⪰ 0` — NEC holds. Off the maximum, the rank-1 term with `Q < 0` can drive the directional eigenvalue of `H_N` negative when `∇ρ` is aligned with a weakly-convex direction of `−M' H_ρ`. So:

- **β ≥ 2:** NEC holds globally on any smooth background with `H_ρ ⪯ 0` in a neighbourhood of each motif peak (sufficient condition: Q ≥ 0 + Hessian term non-negative).
- **β < 2 (includes canonical linear `β = 1`):** NEC holds at motif extrema, but **generically fails on the slopes** wherever `|∇ρ|²` is large enough to overcome the Hessian term. Explicit threshold (slope-direction eigenvalue):

```
NEC fails along slope direction ŝ = ∇ρ/|∇ρ|  when
  |M'| · (−ŝ·H_ρ·ŝ)  <  |Q| · |∇ρ|²
i.e. when    (ŝ·H_ρ·ŝ) · (1−ρ)  <  −(2−β)/2 · |∇ρ|².
```

### 4.2 Saturating mobility `M(ρ) = M_0 / (1 + α ρ)`, `α > 0`

```
M'  = −M_0 α / (1+αρ)²
M'' =  2 M_0 α² / (1+αρ)³
(M')²/(2M) = M_0 α² / (2(1+αρ)³)
Q   = M'' − (M')²/(2M) = (3/2) · M_0 α² / (1+αρ)³  >  0.
```

Slope term is always helpful; Hessian term at motif max is non-negative. **NEC holds globally** on any smooth density background with concave-down motif peaks.

### 4.3 Exponential mobility `M(ρ) = M_0 e^{−αρ}`, `α > 0`

```
M'  = −α M,   M'' = α² M
(M')²/(2M) = α² M / 2
Q   = α² M / 2  >  0.
```

Slope term helpful, `M' < 0` at maxima. **NEC holds globally.**

### 4.4 Linear mobility `M(ρ) = 1 − ρ` (β-family with β=1, the common ED default)

```
M' = −1,  M'' = 0,  Q = −1/(2(1−ρ))  <  0.
```

Slope term is **strictly destructive**. NEC holds at motif maxima but fails on sufficiently steep slopes wherever

```
(ŝ·H_ρ·ŝ) · (1−ρ)  <  −(1/2) |∇ρ|².
```

## 5. Classification table

| Mobility `M(ρ)` | `M'` at peak | `Q(ρ)` | NEC at extremum | NEC on slopes | Verdict |
|---|---|---|---|---|---|
| `(1−ρ)^β`, β ≥ 2 | ≤ 0 | ≥ 0 | ✅ | ✅ (sufficient) | **NEC-safe** |
| `(1−ρ)^2` | ≤ 0 | 0 | ✅ | marginal | **NEC-marginal** |
| `(1−ρ)^β`, 0 < β < 2 | ≤ 0 | < 0 | ✅ | ❌ on steep slopes | **NEC-violating** |
| `(1−ρ)` (linear, β=1) | −1 | < 0 | ✅ | ❌ on steep slopes | **NEC-violating** |
| `M_0/(1+αρ)` | < 0 | > 0 | ✅ | ✅ | **NEC-safe** |
| `M_0 e^{−αρ}` | < 0 | > 0 | ✅ | ✅ | **NEC-safe** |

**Durable result NEC-2.** The **sign of the combination**

```
Q(ρ) = M''(ρ) − M'(ρ)²/(2 M(ρ))
```

is the single diagnostic that sorts ED mobility laws into NEC-safe (`Q ≥ 0`) and NEC-violating (`Q < 0`) families on generic smooth backgrounds.

**Durable result NEC-3.** The canonical-ED linear mobility `M = 1−ρ` is **NEC-violating**: the analogue acoustic geometry admits defocusing on steep density slopes. Raychaudhuri focusing is therefore **not guaranteed** under the default ED mobility; null congruences can expand.

**Durable result NEC-4.** Saturating and exponential mobility laws are NEC-safe on any smooth background. If ED wishes to import standard GR focusing intuition as an effective theorem, it must adopt a mobility law with `Q ≥ 0`.

## 6. Interpretation

(a) **Q is a quasi-convexity discriminant.** `Q ≥ 0` is equivalent to `√M` being concave-up as a function of `ρ` (easy to check: `(√M)'' = (M''/2√M) − (M'²/4 M^{3/2}) = (1/2√M)·Q`, so `(√M)''` and `Q` share a sign). NEC-safe mobility ⟺ `√M` convex in ρ.

(b) **ED's canonical `M = 1−ρ` is NEC-violating** not because the mobility is pathological, but because `√(1−ρ)` is concave (not convex) in ρ. The geometry inherited from this mobility is an acoustic analogue with negative effective null energy in regions of steep ρ-gradient.

(c) **For the reversible slice used in ED-SC 2.0 (linear mobility),** Raychaudhuri-type focusing of null congruences is not universal. Focusing is restored locally at motif peaks (∇ρ = 0) where the NEC reduces to `M' H_ρ ⪰ 0` and is automatically satisfied. This aligns with the GR-SC 1.1 result that the *motif-conditioned* Raychaudhuri ratio `ℛ_Ray` is well-defined at saddles — the saddle condition is precisely the small-∇ρ regime where NEC survives.

(d) **Focusing vs. defocusing as a mobility-law selector.** If future ED work wishes to exploit null-focusing theorems (horizon area, topological censorship analogues), the mobility must be promoted to an NEC-safe family. The β=2 power-law is the **minimal** such promotion from within the `(1−ρ)^β` family; saturating `M_0/(1+αρ)` is the minimal analytic non-power-law promotion.

## 7. Deliverables

- **Closed-form NEC inequality (★):** `M'(ρ) · n̂·H_ρ·n̂ + Q(ρ) · (n̂·∇ρ)² ≥ 0` for all unit n̂, with `Q = M'' − (M')²/(2M)`.
- **Equivalent geometric form:** `H_N(x) ⪰ 0` pointwise; equivalently, `√M(ρ_0(x))` must be a convex function of position.
- **Mobility-law sorting diagnostic:** `sign(Q(ρ))` over the operating range of ρ.
- **Classification table** (§5) for canonical ED mobility families.
- **Main physical statement:** the default ED mobility `M = 1−ρ` does not enforce NEC; only `M(ρ)` with `(√M)''(ρ) ≥ 0` does.

---

## Closure

GR-SC 1.4 is closed. The analogue NEC for `g_eff[ρ_0]` reduces to pointwise convexity of `N = √M(ρ_0)`, which further reduces to the scalar condition `Q(ρ) = M'' − (M')²/(2M) ≥ 0` plus the (generically satisfied) extremum condition `M'(ρ) ≤ 0`. Under canonical ED mobility `M = 1−ρ`, `Q < 0` strictly — NEC fails on steep-gradient regions and Raychaudhuri focusing is not universal. Saturating and exponential mobility laws restore NEC globally. This provides the first **mobility-law-level** structural constraint in the GR-SC arc: the choice of `M(ρ)` directly determines whether the acoustic geometry admits focusing or defocusing of null congruences.
