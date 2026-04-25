# ED-SC 2.0 r*: Numerical 2D Saddle Solve and Closure Diagnostics

**Status.** Derivation memo. Numerical. Closes the last computational gap in
the `r_star_*` arc: extract `(δ*_max, κ∥, κ⊥, ε)` from the full deterministic
Scenario-D saddle PDE and insert into the closed-form r* formula of
`ED_SC_2_0_r_star_Anisotropy.md`. Results are unambiguous and carry a
structural lesson: the pure-PDE radial bounce sits in the *stiff-curvature*
limit (r* → −1); the ED-SC 2.0 reference −1.304 requires the motif filter to
select shallower stationary points in the noisy field, not the deterministic
instanton.

**Scope marker.** What is *derived/computed*: the 2D radial localised
deterministic saddle, its amplitude, principal curvature, nullcline shift,
and the r* it predicts via the Anisotropy-memo asymptotic. What remains *out
of scope*: the full fluctuation-noisy-field motif-filter-selected saddle —
this requires sampling stationary points of a Gaussian random field whose
power spectrum is set by the linearised ED dispersion, a distinct
computation logged as a next-step target.

Companion script: [`analysis/scripts/r_star_saddle_solve.py`](../analysis/scripts/r_star_saddle_solve.py).

---

## 1. PDE and parameters

Deterministic Scenario-D saddle PDE (leading order, M₂ = 0):

    (M₀ + ½ M₂ δ²) ∇²δ + M₂ δ |∇δ|² − P₀ δ − (1/6) P₃ δ³ = 0.          (1.1)

Parameters:

    M₀ = 1,   M₂ = 0   (leading order),
    P₀ = 1,   P₃ = −1.

At these settings, (1.1) reduces to

    ∇²δ  =  δ − δ³/6.                                                 (1.2)

---

## 2. Boundary conditions

Imposed on the radial problem:

- **Localisation:** δ(r) → 0 as r → ∞.
- **Regularity at origin:** δ′(0) = 0 and δ(0) = δ*_max (shooting parameter).
- **SO(2) symmetry reduction:** in the absence of explicit anisotropic
  boundary data, solutions of (1.2) that decay to 0 are radial, i.e.
  δ*(x, y) = δ(r) with r = √(x² + y²). D₂ symmetry + ray-axis selection and
  motif-filter constraints (α = 0.25, L_ray = 2, δ_thr = 0.10) are **not
  realisable in the pure PDE** — they require noise-selected fluctuations
  whose spectrum is set by (1.2) linearised. This is the structural finding
  in §6.

---

## 3. Radial ODE and numerical method

Under radial reduction, (1.2) becomes

    δ″(r) + δ′(r)/r  =  δ(r) − δ(r)³/6,                               (3.1)

with δ(0) = δ*_max, δ′(0) = 0. Near r = 0, L'Hôpital gives
δ″(0) = ½(δ*_max − δ*_max³/6).

**Shooting.** Integrate (3.1) outward from r = 0 with RK45 (rtol 1e−11,
atol 1e−13, max_step 0.02), using two termination events:
(i) δ(r) crosses 0 (overshoot → bounce); (ii) |δ(r)| > 50 (blow-up).
Bisect δ*_max until the critical value separating "does not cross 0" from
"crosses 0" is isolated to 1e−8.

---

## 4. Numerical results

### 4.1 Critical amplitude (pure 2D radial bounce)

Bisection converges to

    ┌────────────────────────────────────────────────────┐
    │   δ*_max  =  5.40406639   (critical bounce)        │
    └────────────────────────────────────────────────────┘

i.e. the smallest amplitude at which the radial profile overshoots to
δ = 0. This is the natural "2D Coleman-like" soliton of (3.1).

### 4.2 Derived invariants

From δ″(0) = ½(δ*_max − δ*_max³/6) and the radial-symmetry identity
κ∥ = κ⊥ = δ″(0):

| Quantity           | Symbol          | Value       |
|--------------------|-----------------|-------------|
| Saddle amplitude   | δ*_max          | 5.40407     |
| Amplitude squared  | δ*_max²         | 29.204      |
| Nullcline shift    | ε = (δ_max²−6)/6 | 3.867      |
| Radial curvature   | κ_rad = κ∥ = κ⊥ | −10.4496    |
| Curvature squared  | κ⊥²             | 109.195     |
| Mobility at peak   | μ = M(δ_max)    | 1.000       |
| Penalty slope peak | π = P′(δ_max)   | −13.602     |
| χ = 2 μ κ⊥² / P₀   | χ               | 218.39      |

### 4.3 r* prediction from (4.4) of the Anisotropy memo

Inserting χ = 218.39 into

    r*  =  − 2 χ / (2 χ − 1)                                          (4.1)

gives

    ┌────────────────────────────────────────────────────┐
    │   r*  (radial, pure-PDE bounce)  =  − 1.00229      │
    └────────────────────────────────────────────────────┘

against Scenario-D reference **r* = −1.304**.

### 4.4 Target inversion

For r* = −1.304 exactly, the asymptotic inverts to

    χ_target   =  −1.304 / (2 − 2·1.304)  =  2.1447
    κ⊥²_target =  χ_target · P₀ / (2 μ)    =  1.0724
    κ⊥_target  =  1.0356                                              (4.2)

i.e. the ED-SC 2.0 reference requires a motif with **κ⊥ ≈ 1.04**, about a
factor of ten shallower than the deterministic 2D bounce's curvature
|κ_rad| ≈ 10.45.

---

## 5. Comparison to target −1.304

| Source                                     | δ*_max   | κ⊥²      | χ       | r*       |
|--------------------------------------------|----------|----------|---------|----------|
| Pure-PDE 2D radial bounce (§4.1)           | 5.404    | 109.2    | 218.4   | −1.002   |
| Anisotropy-memo nullcline closure (ε = 0)  | √6 ≈ 2.449 | 0     | 0       | 0        |
| ED-SC 2.0 reference (filter-selected)      | ≲ √6     | 1.072    | 2.145   | −1.304   |

Three points characterising the landscape:

1. At δ_max² = 6 (cubic nullcline): κ ≡ 0, r* → 0. Homogeneous solution
   δ ≡ √6; not a localised motif. Anisotropy memo's leading-order `s = −1`
   closure is a limit of measure zero in pure radial PDE — it is recovered
   only when the motif is both localised (κ ≠ 0) and balanced (κ∥+κ⊥ = 0),
   which requires broken radial symmetry.

2. At the deterministic 2D bounce (δ_max ≈ 5.40): κ is very stiff
   (|κ| ≈ 10.5), χ ≈ 218, r* → −1 from below. The pure-PDE soliton is
   in the stiff-curvature asymptote, not at the ED-SC 2.0 reference.

3. At the ED-SC 2.0 target (χ = 2.145): κ⊥ ≈ 1.04 is an order of magnitude
   *shallower* than the deterministic bounce, and δ_max must sit between
   √6 and 5.40. This is the band of **filter-selected stationary points
   in the noisy field** — shallower than the deterministic soliton,
   localised unlike the homogeneous nullcline state.

---

## 6. Structural lesson: filter vs. deterministic bounce

The ED-SC 2.0 invariant is not the 2D Coleman-like radial bounce of the
deterministic Scenario-D PDE. The pure-PDE bounce gives r* ≈ −1, not
−1.304. The ED-SC 2.0 reference lives in a different regime:

**The noisy ED field `δ(x, t)` has stationary points scattered through
space with a distribution of curvatures set by the linearised PDE's
dispersion and the noise amplitude σ.** The motif filter (α, L_ray, δ_thr)
picks out a sub-population of these — *ray-like, D₂-symmetric, amplitude
≥ δ_thr* — and `r* = −1.304` is the conditional median over this
sub-population.

This population of stationary points is shallower than the deterministic
soliton (by about 10× in curvature) because the noisy field's typical
stationary points live near the homogeneous state, not at the deep
deterministic attractor. The Anisotropy memo's closed-form asymptotic
r* = −2χ/(2χ−1) with χ = 2.145 is the *first analytic result* that
connects the ED-SC 2.0 target to a single scalar motif scale: the
⊥-direction curvature is κ⊥ ≈ 1.04.

### 6.1 What this changes in the derivation chain

- **Anisotropy memo §3** (natural-amplitude closure `δ_max² = −6P₀/P₃`,
  `s = −1`) is the degenerate-limit closure. It is the *formal* leading
  order for the transcendental equation, but corresponds to a non-
  localised state (κ = 0). The finite-κ motif (the actually-observed
  one) lies close to this limit but with ε > 0 and κ⊥ = O(1).
- **The "empirical scalar" κ⊥** needed to close the chain is **not
  extractable from the deterministic 2D bounce** — it is a statistical
  property of a noisy field. Estimating it requires sampling stationary
  points of a realisation of the Scenario-D SPDE and applying the motif
  filter.

### 6.2 Why this is still progress

The chain is *analytically closed* up to a single computable number κ⊥.
The leading-order structural form r* = −2χ/(2χ−1) is derived; the target
match χ = 2.145 is derived; the failure of the pure-PDE bounce to match
is a clean diagnostic (not an approximation error) and tells us **which
calculation to do next** — sample stationary points of the noisy field.

---

## 7. Closed result

    ┌──────────────────────────────────────────────────────────────────┐
    │                                                                  │
    │   Leading-order analytic chain (closed):                         │
    │                                                                  │
    │      r*  =  −2 χ / (2 χ − 1),    χ  =  2 μ κ⊥² / P₀              │
    │                                                                  │
    │   Target value:                                                  │
    │                                                                  │
    │      r* = −1.304   ⟺   χ = 2.145   ⟺   κ⊥ ≈ 1.04                 │
    │                                                                  │
    │   Pure-PDE 2D radial bounce (diagnostic):                        │
    │                                                                  │
    │      δ*_max = 5.404,  κ∥ = κ⊥ = −10.45,  r* = −1.00              │
    │                                                                  │
    │   The deterministic soliton is in the stiff-curvature asymptote; │
    │   the ED-SC 2.0 reference sits in the shallow, filter-selected   │
    │   band. The single remaining empirical scalar is κ⊥ ≈ 1.04,      │
    │   obtainable from stationary-point statistics of the noisy       │
    │   Scenario-D SPDE under the canonical motif filter.              │
    │                                                                  │
    └──────────────────────────────────────────────────────────────────┘

---

## 8. Next-step targets

1. **Monte-Carlo SPDE stationary-point statistics.** Simulate (1.1) as an
   SPDE at canonical Scenario-D parameters (M₀ = 1, P₀ = 1, P₃ = −1,
   σ = 0.0556), identify 2D spatial stationary points in the noisy field,
   apply the motif filter, and compute the median of κ⊥. Expected value
   ≈ 1.04; falsification if it lands outside [0.97, 1.10].

2. **M₂-regularisation of the deterministic bounce.** Re-run §4 with
   M₂ ≠ 0 to see whether the bounce amplitude δ_max shifts toward √6 and
   whether κ softens toward O(1). This diagnoses the relative roles of
   noise and nonlinear-mobility regularisation in shallow-motif selection.

3. **Anisotropic bounce with broken SO(2).** Solve (1.1) on a domain with
   explicit ray-like boundary data (e.g. a rectangular domain with
   different aspect ratios) to see whether an anisotropic deterministic
   saddle exists and what κ∥/κ⊥ it produces.

4. **Close the 𝒦_NL kernel** (Local Geometry memo eq. 4.8) along the
   instanton from δ = 0 to δ* to produce the full-order r* at O(M₂).

---

## 9. Related memos

- `theory/ED_SC_2_0_r_star_Derivation_Attempt.md` — 3-mode predecessor.
- `theory/ED_SC_2_0_r_star_Derivation_Extended.md` — 4-mode Hermite–Gauss
  (β* ≈ 1.09, η* ≈ 0.48, s ≈ 0.13, κ∥/κ⊥ ≈ −1.3).
- `theory/ED_SC_2_0_r_star_Local_Geometry.md` — symbolic r* formula.
- `theory/ED_SC_2_0_r_star_Anisotropy.md` — closed-form asymptotic
  r* = −2χ/(2χ−1), χ = 2.145 target.
- `memory/project_ed_r_star_analytic_arc.md` — durable arc memory.
- `docs/ED-SC-2.0.md` — canonical invariance statement.
