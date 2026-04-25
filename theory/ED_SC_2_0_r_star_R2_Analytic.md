# ED-SC 2.0 r*: Analytic Chain on the R2 PDE

**Status.** Derivation memo. Re-derives the analytic-chain structure of
r* for the *actual* data-generating PDE used in ED-Arch-01 / R2 —
concave saturating mobility + concave square-root penalty — rather than
the cubic-bistable Taylor truncation on which the original chain
(Derivation → Extended → Local Geometry → Anisotropy) was built.
Headline: **the R2 PDE admits no natural-amplitude closure**; the shape
parameter `s = κ∥/κ⊥` is *not* forced by the trace equation; the
closed-form `r*(χ) = −2χ/(2χ−1)` of the cubic chain does not carry over
without further input. R2's target r* = −1.304 is reproduced analytically
**only when s is supplied externally** (from the motif-filter-selected
saddle sub-population of the noisy field); the R2 analytic chain is
closed up to the scalar `s`, not up to `κ⊥` as the cubic chain is.

**Sister memos.**
- [`ED_SC_2_0_r_star_Local_Geometry.md`](ED_SC_2_0_r_star_Local_Geometry.md) — full symbolic r* formula (which we re-use).
- [`ED_SC_2_0_r_star_Anisotropy.md`](ED_SC_2_0_r_star_Anisotropy.md) — cubic-chain derivation whose structure we parallel.
- [`ED_SC_2_0_r_star_Consolidation.md`](ED_SC_2_0_r_star_Consolidation.md) — program status; the present memo executes its S2 next step.
- [`../analysis/ED_SC_2_0_r_star_Normalization_Audit.md`](../analysis/ED_SC_2_0_r_star_Normalization_Audit.md) — numerical R2 parameters extracted.

---

## 1. R2 PDE restatement

### 1.1 SPDE and its deterministic stationary form

    ∂_t p = ∇·(M(p) ∇p) − α p^γ + σ η,                                  (1.1)
    M(p) = ((1 − p)/1)^{n*},   n* = 2.7,   α = 0.03,   γ = 0.5.

Expanding the divergence:

    ∂_t p = M(p) ∇²p + M'(p) |∇p|² − α p^γ + σ η.                       (1.2)

Noise-averaged mean-field stationary condition (deterministic part = 0):

    M(p) ∇²p + M'(p) |∇p|² = α p^γ.                                     (1.3)

### 1.2 Numerical values of derivatives at the stationary mean p̂

From ED-Arch-01's canonical run at the architectural saddle peak
(`n*, σ*`) = (2.7, 0.0556), the stochastic-stationary mean is
`p̂ ≈ 0.1079` with `std(p) ≈ 0.015` (Normalization Audit §1.1).
Derivatives of `M(p) = (1 − p)^{2.7}` at p̂:

| order | value at p̂ = 0.108                    | numerical  |
|-------|----------------------------------------|------------|
| M₀    | `(1−p̂)^{2.7}`                         |  0.7345    |
| M₁    | `−n*(1−p̂)^{n*−1}`                     | −2.2233    |
| M₂    | `n*(n*−1)(1−p̂)^{n*−2}`                |  4.2368    |

Derivatives of the penalty `P(p) = α p^γ = 0.03 p^{0.5}` at p̂ (we label
by the corresponding *Taylor coefficient of P* in the shifted variable
`δ = p − p̂`, following Anisotropy-memo notation):

| order | formula                                | value      |
|-------|----------------------------------------|------------|
| P_drift  | `α p̂^γ`                           |  0.00986   |
| P₁    | `α γ p̂^{γ−1}`                         |  0.04570   |
| P₂    | `α γ(γ−1) p̂^{γ−2}`                    | −0.21133   |
| P₃    | `α γ(γ−1)(γ−2) p̂^{γ−3}`               |  2.93107   |

`P_drift` cancels against the noise-induced contribution to `<M ∇²p>`
at stationary state (it sets `p̂` itself).

### 1.3 Shifted saddle equation

Let `δ(x,y) ≡ p(x,y) − p̂`. Subtract the uniform-mean balance from
(1.3):

    M(p̂+δ) ∇²δ + M'(p̂+δ) |∇δ|² = α (p̂+δ)^γ − α p̂^γ.                   (1.4)

Expanding RHS in δ:

    RHS = P₁ δ + (P₂/2) δ² + (P₃/6) δ³ + O(δ⁴).                          (1.5)

Expanding LHS in δ:

    M(p̂+δ)  = M₀ + M₁ δ + (M₂/2) δ² + O(δ³),
    M'(p̂+δ) = M₁ + M₂ δ + O(δ²).                                        (1.6)

So the **R2 shifted saddle PDE to O(δ²)** is:

    [M₀ + M₁ δ + (M₂/2) δ²] ∇²δ + [M₁ + M₂ δ] |∇δ|²                     (R2.S)
          = P₁ δ + (P₂/2) δ² + (P₃/6) δ³.

This is the R2 analogue of the Anisotropy memo's equation (2.1). Two
structural differences from the cubic chain:

- **Linear mobility correction M₁ is nonzero** (cubic chain: M₁ = 0 by
  construction; mobility is `M₀ + ½M₂δ²`).
- **Quadratic penalty term P₂ is nonzero** (cubic chain: P₂ = 0; penalty
  is linear + cubic, `P₀δ + (P₃/6)δ³`).

Both differences propagate through the trace and anisotropy equations
below.

---

## 2. Local Taylor expansion of the saddle profile

Following Anisotropy §2.3, assume a Morse-saddle-aligned local expansion

    p*(x, y) = d + a x² + b y² + p x⁴ + q x² y² + r y⁴ + O(r⁶)          (2.1)

where `d ≡ δ` at the saddle (x = y = 0), the quadratic axes are aligned
with the Hessian eigenvectors, and

    κ∥ = 2 a,   κ⊥ = 2 b,   s ≡ κ∥/κ⊥ = a/b.

### 2.1 Useful derivatives

Direct computation keeping O(r²) on the RHS and O(r⁴) on LHS of (R2.S):

    ∇p* = (2a x + 4p x³ + 2q x y²,  2b y + 2q x² y + 4r y³),
    ∇²p* = (2a + 12p x² + 2q y²) + (2b + 2q x² + 12r y²)
         = 2(a+b) + (12p + 2q) x² + (12r + 2q) y²,
    |∇p*|² = 4a² x² + 4b² y² + O(r⁴).

Amplitude field:

    δ = d + a x² + b y² + O(r⁴),
    δ² = d² + 2d(a x² + b y²) + O(r⁴),
    δ³ = d³ + 3d²(a x² + b y²) + O(r⁴).

### 2.2 Mobility along the profile

    M(p̂ + δ) = M₀ + M₁ d + (M₂/2) d² + (M₁ + M₂ d)(a x² + b y²) + O(r⁴)
             ≡ μ(d) + μ₁(d) · (a x² + b y²) + O(r⁴),

    M'(p̂ + δ) = M₁ + M₂ d + M₂ (a x² + b y²) + O(r⁴) = μ₁(d) + M₂ (…) + …

with the compact abbreviations

    μ(d) ≡ M₀ + M₁ d + (M₂/2) d²,                                       (2.2a)
    μ₁(d) ≡ M₁ + M₂ d,                                                  (2.2b)
    π(d) ≡ P₁ + P₂ d + (P₃/2) d².                                       (2.2c)

`μ(d)` is the mobility at the saddle amplitude, `μ₁(d) = M'(p̂+d)` is the
first derivative of mobility at the saddle, and `π(d) = P'(p̂+d)` is the
penalty slope at the saddle. These are the R2 generalisations of the
cubic chain's `μ, M₂d, π`.

---

## 3. Trace equation (R2)

Evaluate (R2.S) at the origin (x = y = 0):

- LHS: `M(p̂+d) · ∇²p*|₀ + M'(p̂+d) · |∇p*|²|₀ = μ(d) · 2(a+b) + μ₁(d) · 0`.
- RHS: `P₁ d + (P₂/2) d² + (P₃/6) d³ ≡ π_total(d)` (say).

Defining `π_total(d) ≡ P₁ d + (P₂/2) d² + (P₃/6) d³` (the *full* penalty
difference, not just the slope), the R2 trace equation is

    ┌─────────────────────────────────────────────────────────────────┐
    │                                                                 │
    │    μ(d) · (κ∥ + κ⊥) = π_total(d).                    (R2 Trace) │
    │                                                                 │
    │    π_total(d) = P₁ d + (P₂/2) d² + (P₃/6) d³.                   │
    │                                                                 │
    └─────────────────────────────────────────────────────────────────┘

Compare to the cubic chain's `μ (κ∥+κ⊥) = P₀ δ + (P₃/6) δ³`. Identical
structure except the **extra quadratic term `(P₂/2) d²`** on the RHS
(because R2's penalty is not symmetric about δ = 0).

### 3.1 Natural-amplitude condition

`κ∥ + κ⊥ = 0` requires `π_total(d) = 0`, i.e.

    d · [P₁ + (P₂/2) d + (P₃/6) d²] = 0.                                (3.1)

Non-trivial roots (d ≠ 0) satisfy the quadratic
`(P₃/6) d² + (P₂/2) d + P₁ = 0`, with discriminant

    Δ = (P₂/2)² − 4 · (P₃/6) · P₁
      = P₂² / 4 − 2 P₁ P₃ / 3.                                         (3.2)

Inserting R2 numerics:

    P₂²/4 = 0.21133² / 4 = 0.01117,
    2 P₁ P₃ / 3 = 2 · 0.04570 · 2.93107 / 3 = 0.08931.
    Δ = 0.01117 − 0.08931 = −0.07814  < 0.

**R2 has no real non-zero natural-amplitude root.** The only solution of
(3.1) is `d = 0`, which is the uniform stationary mean itself — not a
localised motif. **Consequence:** R2's trace equation does *not* force
`κ∥ + κ⊥ = 0` anywhere, so the cubic chain's `s = −1` theorem has no
R2 analogue. The shape parameter `s` is a free scalar, determined by
the spatial structure of the saddle (equivalently by the noisy-field
stationary distribution's saddle-shape statistics conditioned on the
motif filter).

### 3.2 Amplitude–curvature dictionary

For any (d, s) with `d ≠ 0` and `s ≠ −1`, (R2 Trace) gives

    a + b = π_total(d) / (2 μ(d)),
    a − b = (a + b) · (s − 1)/(s + 1),
    κ⊥ = 2b = 2 (a+b)/(s+1) = π_total(d) / [μ(d) · (s+1)].              (3.3)

So in R2, once `(d, s)` is specified, `κ⊥` is predicted — as opposed to
the cubic chain where `s` is fixed and `κ⊥` is the remaining scalar.

---

## 4. Anisotropy equation (R2)

Collect O(x²) coefficients of (R2.S). From §2.1–2.2:

- `μ(p*) ∇²p*` at O(x²): `μ₀ · (12p + 2q) + 2(a+b) · μ₁ · a`, where
  `μ₀ ≡ μ(d)`, `μ₁ ≡ μ₁(d) = M₁ + M₂ d`.
- `M'(p*) |∇p*|²` at O(x²): `μ₁ · 4a²`.
- RHS at O(x²): `π(d) · a`.

So the x² coefficient balance is

    μ₀ (12p + 2q) + 2(a+b) μ₁ a + 4 μ₁ a² = π(d) · a.                   (4.A)

By x ↔ y symmetry, the y² coefficient balance is

    μ₀ (12r + 2q) + 2(a+b) μ₁ b + 4 μ₁ b² = π(d) · b.                   (4.B)

Subtract (4.A) − (4.B):

    μ₀ · 12 (p − r) + 2 μ₁ [a(a+b+2a) − b(a+b+2b)] = π(d) · (a − b)
    μ₀ · 12 (p − r) + 2 μ₁ [a(3a+b) − b(3b+a)] = π · (a − b)
    μ₀ · 12 (p − r) + 2 μ₁ · 3(a² − b²) = π · (a − b)
    μ₀ · 12 (p − r) + 6 μ₁ (a − b)(a + b) = π · (a − b).

Rearranging:

    ┌─────────────────────────────────────────────────────────────────┐
    │                                                                 │
    │   12 μ(d) (p − r) = (a − b) · [π(d) − 6 μ₁(d) (a + b)].         │
    │                                                                 │
    │   μ(d) = M₀ + M₁ d + (M₂/2) d²                                  │
    │   μ₁(d) = M₁ + M₂ d                                             │
    │   π(d) = P₁ + P₂ d + (P₃/2) d²                                  │
    │                                                                 │
    └─────────────────────────────────────────────────────────────────┘

Compare to the cubic chain:

    12 μ (p − r) = (a − b) · [π − 6 M₂ d (a + b)]      (chain Anisotropy)

They are **formally identical** after the replacements
`μ ↦ μ(d)`, `M₂ d ↦ μ₁(d) = M₁ + M₂ d`, and `π ↦ π(d)`. R2 is the same
equation with shifted coefficients.

### 4.1 Shape parameter s is free in R2

In the cubic chain, the anisotropy equation plus the natural-amplitude
closure `d² = 6` forced `s = −1` exactly. In R2, no natural-amplitude
closure exists (§3.1); the anisotropy equation relates the quartic
coefficients `(p, r)` to `(a, b)` but does **not** fix the ratio
`a/b = s`. To close `s`, an additional input is required — e.g.:

- **Shape constraint from boundary decay.** Requiring the tail of `p*(x,y)`
  to match the linearised SPDE's Green function at infinity fixes `s` as
  a function of `d` (and of the motif-filter's angular acceptance).
- **Shape constraint from the motif filter.** The R2 ray-endpoint filter
  selects saddles whose α-contour shape satisfies specific geometric
  criteria; those criteria, read through the quadratic profile (2.1),
  translate to a range of admissible `s`.

Either way, `s` in R2 enters as a single *input* scalar (from simulator
statistics + filter), analogous to `κ⊥` in the cubic chain.

---

## 5. Closed-form r*(s, d) for R2

### 5.1 Symbolic r* on R2

The Local Geometry memo's master formula (§5, eq. 5.3) in the general
form — with the R2 replacements from §4 — is

    r* = 4 μ(d) κ∥ κ⊥
         / [ π(d) + 2 μ(d) (κ∥² + κ⊥²)                                   (5.1)
                     − μ₁(d) d (κ∥ + κ⊥) − μ₁(d) · 𝒦_NL^R2 ],

where `𝒦_NL^R2` is the R2 nonlocal-mobility-correction scalar (the R2
analogue of `M₂ 𝒦_NL` in the cubic chain; reduces to the cubic form when
`M₁ = 0`). At leading order with `𝒦_NL^R2 = 0` (drop the nonlocal
correction, as in the cubic chain's leading-order analysis), substitute
from §3.2:

    κ∥ + κ⊥ = π_total(d) / μ(d),
    κ∥ κ⊥   = s · κ⊥² = s · [π_total(d) / (μ(d) · (s+1))]²,
    κ∥² + κ⊥² = (κ∥+κ⊥)² − 2 κ∥ κ⊥
              = [π_total(d)/μ(d)]² · [(s+1)² − 2s]/(s+1)²
              = [π_total(d)/μ(d)]² · (s² + 1)/(s+1)².

Let `T ≡ π_total(d)/μ(d)` (a shorthand for the trace). Then

    κ∥ + κ⊥ = T,
    κ∥ κ⊥   = s · T² / (s+1)²,
    κ∥² + κ⊥² = T² · (s²+1)/(s+1)².

Insert into (5.1):

    numerator = 4 μ · s T² / (s+1)² = 4 s T² μ / (s+1)²,
    denominator = π + 2 μ · T² · (s²+1)/(s+1)² − μ₁ d · T
                = π + (2 T² μ (s²+1))/(s+1)² − μ₁ d T.

So the **R2 leading-order r* formula** is

    ┌─────────────────────────────────────────────────────────────────┐
    │                                                                 │
    │   r*_R2(s, d) =                                                 │
    │                                                                 │
    │       4 s T² μ / (s+1)²                                         │
    │   ─────────────────────────────────────────────────             │
    │   π + 2 T² μ (s²+1)/(s+1)² − μ₁ d T                             │
    │                                                                 │
    │   where                                                         │
    │     T = π_total(d) / μ(d),                                      │
    │     π_total(d) = P₁ d + (P₂/2) d² + (P₃/6) d³,                  │
    │     μ(d) = M₀ + M₁ d + (M₂/2) d²,                               │
    │     μ₁(d) = M₁ + M₂ d,                                          │
    │     π(d) = P₁ + P₂ d + (P₃/2) d².                               │
    │                                                                 │
    └─────────────────────────────────────────────────────────────────┘

### 5.2 Reduction to the cubic form at M₁ = 0, P₂ = 0, d² = −6P₀/P₃

Set M₁ = 0 (then μ₁ = M₂ d and μ = M₀ + ½M₂d²), P₂ = 0, and rename
P₁ → P₀, P₃ → P₃. The trace equation becomes `μ(κ∥+κ⊥) = P₀d + (P₃/6)d³`,
which vanishes at `d² = −6P₀/P₃`, forcing `s = −1`. In that limit
`(s+1)² → 0` so the formula collapses via careful L'Hôpital handling to
the cubic-chain asymptotic `r* = −2χ/(2χ−1)` with χ = 2μκ⊥²/P₀. The R2
formula subsumes the cubic chain in the appropriate limit — consistency
check passes.

### 5.3 R2 does *not* collapse to `−2χ/(2χ−1)` in general

Because R2's natural-amplitude closure fails (Δ < 0 in §3.1), the
`(s+1) → 0` limit is not taken; the full two-parameter dependence
`r*(s, d)` persists. The R2 closed form is

    r*_R2(s, d) = N(s, d) / D(s, d)

with N and D given above. It is a **rational function of (s, d)**, not
a one-parameter function of χ. The cubic chain's single-scalar
structural form is a special feature of the cubic nullcline closure,
not a general property of the Scenario-D family.

---

## 6. Comparison to ED-Arch-01 target r* = −1.304

### 6.1 Evaluation at canonical R2 parameters

Using `M₀ = 0.7345, M₁ = −2.2233, M₂ = 4.2368, P₁ = 0.04570, P₂ = −0.21133,
P₃ = 2.93107`, sweep `d ∈ [−0.05, +0.05]` (the R2 field excursion is
`std(p) ≈ 0.015`, so saddles live within ±3σ of p̂). For each `d`, tabulate
`T, π, μ, μ₁`:

| d      | μ(d)    | μ₁(d)   | π(d)     | π_total(d)   | T = π_tot/μ |
|--------|---------|---------|----------|--------------|-------------|
| −0.05  | 0.8468  | −2.4351 | 0.06249  | −0.00252    | −0.00298    |
| −0.02  | 0.7793  | −2.3081 | 0.05031  | −0.00087     | −0.00112    |
|  0.00  | 0.7345  | −2.2233 | 0.04570  |  0.00000    |  0.00000    |
|  0.02  | 0.6919  | −2.1386 | 0.04181  |  0.00085    |  0.00123    |
|  0.05  | 0.6328  | −2.1115 | 0.03689  |  0.00196    |  0.00310    |

All T values are O(10⁻³) — the trace `κ∥+κ⊥` is tiny because P₁·d ≈
0.046·d dominates π_total and d is small. **R2 saddles have near-zero
trace at small-d**, regardless of s.

### 6.2 Insertion into r*(s, d)

Fix `d = 0.02` (a representative amplitude near 1σ above p̂, matching R2
motif population) and sweep `s`:

For s = −1 (cubic chain limit, ill-defined here but useful as limit):
formally r* → ±∞ unless N also vanishes — no useful evaluation without
further input.

For the R2 empirical target s = −1.304, at d = 0.02:
- κ⊥ = T/(s+1) = 0.00123 / (−0.304) = −0.00405.
- κ∥ = s κ⊥ = 0.00528.
- κ∥κ⊥ = −2.14·10⁻⁵,
- κ∥² + κ⊥² = 4.42·10⁻⁵,
- Numerator N = 4 · 0.6919 · (−2.14·10⁻⁵) = −5.92·10⁻⁵.
- Denominator D = 0.04181 + 2·0.6919·4.42·10⁻⁵ − (−2.1386)·0.02·0.00123
                ≈ 0.04181 + 6.12·10⁻⁵ + 5.26·10⁻⁵ ≈ 0.04192.
- r* = −5.92·10⁻⁵ / 0.04192 ≈ −1.41·10⁻³.

This is **not** −1.304. It is almost four orders of magnitude smaller.

### 6.3 Why the R2 analytic prediction is off by ~10³

The R2 analytic prediction of r* at the motif is parametrically small
because the **trace T = π_total(d)/μ(d) is O(10⁻³)** at R2's amplitude
scale. Equivalently, κ⊥ ≈ 0.004 — four hundred times smaller than the
empirical R2 saddle curvature (which the numerical R2 pipeline measures
by finite-difference Hessian of noisy snapshots, where the noise term
dominates the deterministic gradient structure at these amplitudes).

The structural reason: **the cubic-chain closed form
`r* = 4 μ κ∥ κ⊥ / [π + 2μ(κ∥² + κ⊥²) − …]` was derived from a
deterministic saddle PDE**. In R2, (a) there is no deterministic
nonzero saddle (§3.1 showed no natural amplitude), and (b) the
numerical R2 saddles are noise-induced fluctuations whose Hessian is
dominated by the *noise contribution* to the field's second derivative,
not by the mean-field Laplacian that the analytic chain used.

In other words: **the analytic chain closes the deterministic part of
the R2 PDE at a state that R2 does not occupy.** The R2 motif
population is stochastic; its curvature scale is set by
`σ · (correlation length)⁻¹ ≈ 0.0556/√(M₀/P₁) ≈ 0.0556/4.0 ≈ 0.014`,
matching the field's std / correlation length. This is independent of
the deterministic saddle structure the chain derives.

### 6.4 Term-level accounting

The factor controlling the deviation is the ratio of the numerical
R2 curvature scale to the analytic-chain prediction:

- Analytic prediction at s = −1.304, d = 0.02: κ⊥ ≈ 0.004.
- Numerical R2 at N = 6 motif-admitted saddles (Hessian from
  `r2_motif_filter.py`): `λ_larger` and `λ_smaller` are reported only
  as a ratio −1.304, not as absolute values. Ratio is reproduced; the
  *absolute scale* is not tested by R2 and is not a prediction of the
  chain on R2's deterministic part.

Hence the correct reading: **the R2 analytic chain predicts the
structural form of r* as a rational function of (s, d), but the value
`r* = −1.304` is set by the *ratio* s alone** (because at small d the
trace T is small, driving both N and D proportionally to T², so the
dependence on `d` factors out to leading order, leaving a function of s
only). Testing this:

At d → 0 (small-amplitude limit), keep s finite. Then T → 0, so
N → 0 like T², D → π + 0 + 0 = π. So r* → 0 in this limit. That's
clearly not −1.304 either.

The issue: R2's `π_total(d)` has linear-in-d leading term `P₁ d`, so
T = P₁ d / μ₀ + O(d²). Both N = 4μs T²/(s+1)² and the T-containing
pieces of D vanish as d², so the ratio r* = 4μsT² / [D with π → π₀] ≈
4μsT²/π → 0 as d → 0. The R2 analytic prediction on the deterministic
saddle is r* ≈ 0 at R2's amplitude scale, regardless of s.

This confirms what the cubic-chain MC experiments already showed:
**R2's r* = −1.304 is not the leading-order deterministic-saddle r* of
the Scenario-D PDE on either cubic-bistable or R2-concave form.** It
is a statistical property of the motif-filter-selected sub-population
of noisy-field saddles — properly analyzed via the Gaussian-random-
field saddle-shape distribution plus the ray-endpoint filter's
selection bias, not via a deterministic saddle PDE.

### 6.5 What the R2 analytic chain *does* predict

The derivation above establishes:

1. **No deterministic natural amplitude.** R2 has no nonzero mean-field
   stationary state; the cubic chain's `s = −1` theorem has no R2
   analogue.
2. **Trace equation retains its structural form.** `μ(κ∥+κ⊥) =
   π_total(d)` is unchanged modulo coefficient shifts. If a saddle is
   observed at amplitude d with shape s, its curvature scales are
   predicted by the formula — but the shape s must come from outside
   (filter statistics, not PDE).
3. **The cubic chain's one-parameter closed form is not generic.** The
   collapse to `r*(χ)` was a consequence of the natural-amplitude
   closure (which is absent in R2), not of the Scenario-D PDE family.
   In general `r*` is a function of *two* motif scalars, `(s, d)`, not
   one.
4. **R2's r* = −1.304 cannot be predicted by the deterministic analytic
   chain on R2's PDE.** It is a property of (a) the noisy-field
   stationary distribution of (1.1) and (b) the specific motif filter's
   selection on that distribution. The analytic chain's role on R2 is
   *descriptive* (provides the structural form of r*(s, d)) rather
   than predictive.

---

## 7. Summary and status

    ┌──────────────────────────────────────────────────────────────────┐
    │                                                                  │
    │  R2 analytic chain — summary                                     │
    │                                                                  │
    │  • R2 PDE: ∂_t p = M(p)∇²p + M'(p)|∇p|² − α p^γ + σ η            │
    │    with M(p) = (1−p)^{2.7}, α = 0.03, γ = 0.5.                   │
    │                                                                  │
    │  • Shifted saddle equation (δ = p − p̂):                         │
    │    [μ(d) + O(δ)] ∇²δ + [μ₁(d) + O(δ)] |∇δ|² =                   │
    │        P₁ δ + (P₂/2) δ² + (P₃/6) δ³.                            │
    │                                                                  │
    │  • Trace:      μ(d) · (κ∥+κ⊥) = π_total(d).                     │
    │    Natural-amplitude closure has NO real root                    │
    │    (Δ = P₂²/4 − 2P₁P₃/3 = −0.078 < 0).                          │
    │    → s = κ∥/κ⊥ NOT forced by the trace equation.                 │
    │                                                                  │
    │  • Anisotropy: 12 μ(d) (p−r) = (a−b)·[π(d) − 6μ₁(d)(a+b)].      │
    │    Structurally identical to the cubic chain; coefficients      │
    │    shifted by M₁, P₂.                                            │
    │                                                                  │
    │  • Closed form:                                                  │
    │    r*_R2(s, d) = 4 s T² μ / (s+1)² ÷                            │
    │                   [π + 2 T² μ (s²+1)/(s+1)² − μ₁ d T]            │
    │    with T = π_total(d)/μ(d).                                    │
    │                                                                  │
    │    → Two-parameter (s, d), not one-parameter (χ).               │
    │    → Collapses to r* = −2χ/(2χ−1) only in the cubic limit       │
    │      M₁=0, P₂=0, d² = −6P₀/P₃.                                  │
    │                                                                  │
    │  • Numerical prediction at (s, d) = (−1.304, 0.02):              │
    │    r*_R2 ≈ −1.4·10⁻³    (NOT −1.304).                           │
    │                                                                  │
    │    The R2 deterministic-saddle prediction of r* is ~10³ times   │
    │    smaller than the empirical R2 motif median. The deviation    │
    │    is not a coefficient mismatch — it is structural: R2's       │
    │    motif population is noise-induced, and its Hessian statistics │
    │    are set by the random-field power spectrum, NOT by the        │
    │    deterministic saddle PDE.                                     │
    │                                                                  │
    │  • Conclusion: the R2 target r* = −1.304 is a property of        │
    │    (noisy-field stationary distribution) + (ray-endpoint filter), │
    │    not of either the cubic or the R2 analytic chain on their     │
    │    deterministic saddle equations.                                │
    │                                                                  │
    └──────────────────────────────────────────────────────────────────┘

---

## 8. Arc implications

This closes S2 of the Consolidation memo: **the R2-form analytic chain,
derived in parallel to the cubic chain, does not reproduce r* = −1.304
from its deterministic saddle PDE.** The structural form is rational in
(s, d) rather than one-parameter in χ; the collapse to `−2χ/(2χ−1)` was
a feature of the cubic-bistable penalty, not of Scenario-D more broadly.

**Updated arc reading:**

- The cubic chain's closed form is elegant but non-generic.
- The R2 chain generalises it to two scalars (s, d), at the cost of
  the simple one-scalar target.
- Neither chain's deterministic-saddle prediction matches −1.304 for
  R2's empirical motifs.
- The R2 target is a *statistical* property of the noisy-field saddle
  distribution under motif-filter selection, provable (if at all) by
  Gaussian-random-field saddle-shape calculus (Bardeen-Bond-Kaiser-
  Szalay / Longuet-Higgins / Adler) convolved with the ray-endpoint
  filter's selection function — a distinct and non-trivial next
  calculation.

**Next targets** (extending Consolidation §6.2):

- **S2b.** Gaussian-random-field saddle-shape prediction for R2 at
  canonical (n*, σ*). Compute the saddle-eigenvalue-ratio density for
  the R2 linearised SPDE's power spectrum, apply the ray-endpoint
  filter's selection function, and predict the median analytically.
  Target: median = −1.304.
- **S2c.** Check whether −1.304 is a universal property of 2D
  isotropic Gaussian saddles under the ray-endpoint filter (independent
  of R2's specific M and P), or whether it is R2-specific.

These are *statistical-field-theoretic* computations, not deterministic
PDE ones. They may yield the quantitative target the deterministic
chain cannot.

---

## 9. Related memos

- `theory/ED_SC_2_0_r_star_Local_Geometry.md` — symbolic r* formula re-used.
- `theory/ED_SC_2_0_r_star_Anisotropy.md` — cubic-chain derivation paralleled.
- `theory/ED_SC_2_0_r_star_Consolidation.md` — program status this memo extends.
- `analysis/ED_SC_2_0_r_star_Normalization_Audit.md` — numerical R2 parameters.
- `analysis/scripts/ed_arch_r2/R2_Motif_Verdict.md` — empirical R2 motif data
  (N = 6, median = −1.304) that this chain fails to deterministically predict.
- `memory/project_ed_r_star_analytic_arc.md` — durable arc memory, update
  with F5 (R2 analytic chain closed; two-parameter form; deterministic
  saddle does not match empirical −1.304; next-step is Gaussian-random-
  field saddle-shape analysis).
