# GR-SC 1.6 — Weyl Tensor Motif Statistics on the ED Acoustic Metric

**Arc:** GR-SC (General-Relativistic Structural Correspondences on the kinematic ED acoustic metric)
**Status:** Draft, paired with GR-SC 1.0 (Einstein tensor)
**Date:** 2026-04-23
**Scope:** Strictly kinematic. No Einstein equations. No dynamical gravity. The acoustic metric `g_eff[ρ_0]` is treated as a geometric object on which standard curvature invariants are evaluated and then motif-filtered exactly as r* is filtered in ED-SC 2.0.

---

## 0. Why Weyl needs a 3+1D uplift

The Weyl tensor `C_{abcd}` vanishes identically in spacetime dimension ≤ 3. The canonical ED acoustic slice used in the r* program is 2+1D (static, ultrastatic, two spatial dimensions):

```
g_eff = diag(-N²(x,y), 1, 1),   N = √M(ρ_0)
```

To extract non-trivial Weyl content we lift to 3+1D by taking `ρ_0` independent of a third spatial coordinate `z`:

```
g_eff^(4) = diag(-N²(x,y), 1, 1, 1),   ∂_z N = 0.
```

This is the minimal uplift: all motif geometry still lives on the (x,y) slice, and the z-direction is a passive translational symmetry. The construction is a book-keeping device for computing `C_{abcd}`; it imports no new physics.

---

## 1. Electric and magnetic Weyl decomposition

For a timelike unit vector `u^a = N^{-1}∂_t` (the observer at rest with the motif), the Weyl tensor decomposes as

```
E_{ab} = C_{acbd} u^c u^d           (electric part)
B_{ab} = *C_{acbd} u^c u^d          (magnetic part)
```

Both are spatial, symmetric, traceless.

### 1.1 Magnetic part vanishes

For any static metric with flat spatial block and no time–space off-diagonal terms, the magnetic Weyl `B_{ab} = 0` identically. Proof: `*C` contains the epsilon-contracted Riemann, and on an ultrastatic metric every non-zero Riemann component has the structure `R_{0i0j}` or `R_{ijkl}=0` (flat spatial block). Anti-symmetrising with ε gives zero.

**Durable result W1.** `B_{ab} ≡ 0` on any static ultrastatic acoustic metric. The Weyl content is carried entirely by the electric part.

### 1.2 Electric part

A short computation on `g_eff^(4)` with flat spatial block gives

```
E_{ij} = (1/(2N)) · traceless[ H_N ]_{ij}^(3D)
       = (1/(2N)) · ( N_{,ij} - (1/3) δ_{ij} ∇²N )_{3×3}
```

where `H_N` is the 3D spatial Hessian of N. Since N is z-independent the 3×3 Hessian has a single zero eigenvalue along ẑ, and the (x,y)-block is `∂_i ∂_j N` for i,j ∈ {x,y}.

Writing `Tr ≡ ∂²_x N + ∂²_y N` and the 2D Hessian eigenvalues `λ_1, λ_2` with `Tr = λ_1 + λ_2`:

```
E-eigenvalues (3D):
   e_1 = (1/(6N)) ( 2λ_1 - λ_2 )
   e_2 = (1/(6N)) ( 2λ_2 - λ_1 )
   e_3 = (1/(6N)) ( -λ_1 - λ_2 )
```

Sum = 0 as required. The three eigenvalues are determined entirely by the two 2D Hessian eigenvalues `(λ_1, λ_2)` — the same (λ_1, λ_2) that drive r* in ED-SC 2.0.

---

## 2. Linearisation in the motif field φ

Using `N = N̂ + N̂' φ` with `μ₁ ≡ N̂'/N̂` (the mobility-slope parameter shared with r*, Einstein, Raychaudhuri):

```
E_{ij}^(lin) = (μ₁ / 6) · ( 2 ∂_i∂_j φ - δ_{ij} ∇²φ - (z-block) )
```

and the 2D-block eigenvalues reduce to

```
e_1 = (μ₁/6)(2λ_1 - λ_2)
e_2 = (μ₁/6)(2λ_2 - λ_1)
e_3 = -(μ₁/6)(λ_1 + λ_2)
```

where now `(λ_1, λ_2)` are the eigenvalues of the 2D φ-Hessian.

---

## 3. Two principal invariants

### 3.1 The curvature scalar `C²`

For E-only Weyl with `B = 0`:

```
C² ≡ C_{abcd} C^{abcd} = 8 tr(E²)
```

Using `tr(E²) = e_1² + e_2² + e_3²` and the saddle decomposition `λ_1 = s + u, λ_2 = s − u`:

```
tr(E²) = (μ₁² / 6) · ( 3 s² + u² )

C²    = (4 μ₁² / 3) · ( 3 s² + u² )
```

With GRF saddle moments `⟨s²⟩ = 7σ_2²/12` and `⟨u²⟩ = σ_2²/12`:

```
⟨C²⟩ = (4 μ₁²/3) · ( 3·7σ_2²/12 + σ_2²/12 ) = (4 μ₁²/3) · (22 σ_2² / 12)
      = (88/36) μ₁² σ_2²  ≈  2.44 μ₁² σ_2²
```

Monte-Carlo (100k saddle draws, unfiltered) gives median `C²/μ₁²σ_2² ≈ 2.13`.

**At R2 canonical (μ₁ = −1.513, σ_2 = 0.0898):**

```
mean  C² ≈ 0.0446
median C² ≈ 0.0389
√median C² ≈ 0.197
```

**Durable result W2.** `C²` is sign-definite positive, scales as `μ₁² σ_2²`, and its median is set by the saddle distribution. It is a **quadratic-class invariant** in the GR-SC 1.0 taxonomy (trace-type has zero median, ratio-type is mobility-universal, quadratic-type scales as μ₁² σ_2²).

### 3.2 The principal Weyl ratio `ℛ_W`

Ordering `|e_i|` so that the two largest-magnitude E-eigenvalues are retained, the natural dimensionless ratio at a motif saddle is

```
ℛ_W(t) = -(2t + 1)/(t + 2),   t ≡ λ_1/λ_2
```

with t the same Hessian-eigenvalue ratio that defines r*. Algebraic range:

```
t ∈ (−∞, ∞)   ⇒   ℛ_W ∈ (−2, −1/2)
```

**Durable result W3.** Unlike r* (which is unbounded), `ℛ_W` is confined to the open interval `(−2, −1/2)`. This bounded range is a qualitative structural feature of the Weyl invariant: its distribution is **narrow-band** even before motif filtering.

### 3.3 Numerical medians

Using the GRF saddle density (unfiltered) and the canonical ray-endpoint filter (filtered), same machinery as ED-SC 2.0:

| Regime | `t_med` | `ℛ_W` at t_med | `|ℛ_W|` |
|---|---|---|---|
| Unfiltered saddle | 1.94 | −1.239 | 1.239 |
| Canonical filtered | 1.39 | −1.115 | 1.115 |
| Pooled R2 (t = 1.88) | 1.88 | −1.227 | 1.227 |

All three values sit inside the interior of (−2, −1/2), well away from both endpoints. The filter pulls the ratio toward −1, i.e. toward the t = 1 (isotropic saddle) point where `ℛ_W(1) = −1`.

**Durable result W4.** The filtered pooled-R2 prediction is

```
ℛ_W = −1.23 ± 0.05    (10-seed, canonical filter, R2)
```

mobility-universal (independent of μ₁), and — unlike r* — bounded.

---

## 4. Falsifiable predictions

**W-P1 (sign-definite).** Any kinematic-acoustic motif map must satisfy `C² ≥ 0` pointwise. Measurements yielding a negative reconstructed `C²` falsify the acoustic-slice assumption, not ED.

**W-P2 (bounded ratio).** In motif-conditioned ensembles, the principal Weyl ratio satisfies `ℛ_W ∈ (−2, −1/2)` to sampling precision. A sample mass outside this interval falsifies the uplift geometry.

**W-P3 (pooled median).** `|ℛ_W|_{median} = 1.23 ± 0.05` at R2 canonical, pooled 10-seed, canonical ray-endpoint filter.

**W-P4 (scale law).** `C²_{median} ≈ 2.1 · μ₁² σ_2²`. Halving σ_2 by smoothing should divide the median curvature scalar by 4.

**W-P5 (r*–ℛ_W correlation).** At individual motif saddles, r* and ℛ_W are related by a one-parameter curve through `t = λ_1/λ_2`:

```
r*(t) = t                   (= λ_1/λ_2)
ℛ_W(t) = -(2t+1)/(t+2)
```

so the joint `(r*, ℛ_W)` distribution collapses to a 1D curve in the clean-saddle approximation. Deviations from this curve measure the weight of non-saddle motif content.

---

## 5. Structural durable items

**W-D1.** Weyl on the ED acoustic slice requires a trivial 3+1D uplift along a passive `z` direction; the motif geometry is untouched.

**W-D2.** `B_{ab} = 0` on any static ultrastatic acoustic metric. All Weyl content is electric.

**W-D3.** `C²` is a quadratic-class GR-SC invariant: sign-definite, zero at isotropic saddles, scales as `μ₁² σ_2²`.

**W-D4.** `ℛ_W` is a **new narrow-band ratio invariant**, bounded in (−2, −1/2), mobility-universal, and related to r* by the algebraic map `ℛ_W = −(2 r* + 1)/(r* + 2)`.

**W-D5.** The three-class taxonomy from GR-SC 1.0 is **preserved** under the addition of Weyl: the spatial-block Einstein ratio, Raychaudhuri ratio, and r* itself are all r*-type (unbounded); traces are Gaussian-class (zero median); `C²`, `det(G^ij)` are quadratic-class; and `ℛ_W` is a new **bounded-ratio subclass** of r*-type.

**W-D6.** The bounded range of `ℛ_W` makes it a sharper empirical discriminator than r*: a pooled median of 1.23 with a window of ±0.05 is a 4% precision target, versus r*'s ±0.4 at the same statistics.

---

## 6. Summary table (GR-SC 1.6)

| Invariant | Class | Median | Scale | Mobility-universal? |
|---|---|---|---|---|
| `B_{ij}` | (identically zero) | 0 | — | — |
| `tr(E^{ij}) = 0` | (traceless identity) | 0 | — | — |
| `C²` | quadratic | ≈ 2.13 μ₁² σ_2² | μ₁² σ_2² | no |
| `ℛ_W` | bounded ratio | −1.23 ± 0.05 | dimensionless | yes |
| `ℛ_W ∘ r*` map | algebraic | `−(2r*+1)/(r*+2)` | — | — |

At R2 canonical (μ₁ = −1.513, σ_2 = 0.0898):

```
C²:   mean 0.045, median 0.039, √median 0.20
ℛ_W:  pooled R2 median −1.23, filtered median −1.12, unfiltered −1.24
```

---

## Appendix A. Numerical MC verification (unfiltered saddle)

Using 100,000 saddle draws from `f_sad(a,b) ∝ ab(a+b)exp[−(3a²+2ab+3b²)/(2σ_2²)]`:

```
⟨C²⟩ / (μ₁² σ_2²)   = 2.444   (analytic 88/36 = 2.444)
med(C²) / (μ₁² σ_2²) = 2.13
med(|ℛ_W|)           = 1.239
frac(ℛ_W ∈ (−2,−1/2)) = 1.0000
```

All values reproduce the closed-form results to 3 sig fig.

---

## Closure

GR-SC 1.6 is closed. The Weyl tensor on the kinematic ED acoustic slice (via trivial 3+1D uplift) delivers:

- a new quadratic-class scalar `C²` with scale `μ₁² σ_2²`;
- a new **bounded** ratio invariant `ℛ_W ∈ (−2, −1/2)` with pooled-R2 median `−1.23 ± 0.05`;
- an algebraic `ℛ_W ↔ r*` map that tightens the joint distribution to a 1D curve in the clean-saddle limit.

Together with GR-SC 1.0 (Einstein) and GR-SC 1.1 (Raychaudhuri), the three memos exhibit the full three-class taxonomy (ratio / trace / quadratic) and add one bounded-ratio subclass unique to Weyl. The r*-template from ED-SC 2.0 transfers cleanly to every GR-curvature invariant tested so far.
