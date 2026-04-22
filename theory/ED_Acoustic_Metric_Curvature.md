# Curvature of the ED Acoustic Metric on a Gaussian Bump

**Date.** 2026-04-22.
**Scope.** Working memo. Concrete curvature calculation for the effective acoustic metric `g^{eff}_{μν} = diag(−M(ρ_0(x)), 1, 1, 1)` (from `theory/ED_Effective_Acoustic_Metric.md`) on a specific analytically-tractable background `ρ_0(x)`: a 1D Gaussian bump with tunable amplitude. Compute all Christoffel symbols, Riemann tensor, Ricci tensor, and Ricci scalar. Interpret the result and examine (i) whether curvature concentrates near mobility gradients, (ii) whether Schwarzschild-like features emerge, (iii) whether surface gravity `κ` is definable at the P4 horizon, (iv) whether a Hawking-like `T_H` can be read off.
**Status.** Concrete calculation. Two substantive structural findings: **(A) R[g^{eff}] is localised on the mobility-gradient scale and changes sign across the bump width `σ`**; **(B) generic P4 horizons formed at *interior* local maxima of `ρ_0` are acoustically *extremal* (`κ_acoustic = 0`)** — Hawking-like radiation in the Visser sense is absent for such horizons. Finite `κ` requires a monotonic profile with `ρ_0 → ρ_max` at a boundary, which is a restricted class.

---

## 1. Choice of Background `ρ_0(x)` and Justification

### 1A. Profile

1D Gaussian bump on a uniform equilibrium:

$$
\rho_0(x) \;=\; \rho^* + A\,\exp\!\bigl(-x^2/(2\sigma^2)\bigr),
\qquad
0 \le A \le \rho_{\max} - \rho^*.
$$

Parameters: `A` is bump amplitude, `σ` is width, `ρ*` is equilibrium background, `ρ_max` is the P4 mobility-capacity bound.

### 1B. Why this profile

- **Analytically tractable.** Single independent coordinate `x`; the static metric reduces to 2D non-trivial (`t, x`) with two flat spectator directions (`y, z`); curvature expressions close in elementary functions.
- **Tunable horizon.** At the critical amplitude `A = ρ_max − ρ*` (equivalently `a ≡ A/(ρ_max − ρ*) = 1`), the profile touches `ρ_0(0) = ρ_max` and the mobility `M(ρ_0(0)) = 0` — an acoustic horizon forms at `x = 0`.
- **Smooth.** `ρ_0 ∈ C^∞`. Any non-analyticity in the curvature is inherited from the metric, not from a hand-chosen kink.
- **Generic.** Gaussian is the leading-order approximation to any smooth unimodal bump. Findings should apply qualitatively to other smooth unimodal profiles.
- **Captures both regimes.** For `0 < a < 1`, no horizon (pure curvature analysis). For `a → 1`, horizon formation at an interior local maximum.

### 1C. Static background condition

`F[ρ_0] = 0` (from `ED_Effective_Acoustic_Metric.md` §1B) is required for a stationary background. The Gaussian bump does **not** satisfy `F[ρ_0] = 0` exactly; it is a test profile for *kinematic* curvature analysis. For the reversible sector, the implicit assumption is WKB / eikonal: `ρ_0(x)` varies slowly enough that fluctuations `δρ(x, t)` at frequency `ω` see a quasi-static background. The length scale is `σ`; the fluctuation timescale is `1/ω`. Validity: `σ·ω/c_s ≫ 1`, i.e., probe wavelengths small compared to `σ`. Keep this restriction in mind when interpreting.

---

## 2. Explicit Form of `M(ρ_0(x))` and `c_s(x)`

### 2A. Canonical mobility

Canon P4 with `β = 1` (the canonical choice in `theory/PDE.md` §1):

$$
M(\rho) \;=\; M_0\,(\rho_{\max} - \rho).
$$

Substituting the Gaussian:

$$
M(\rho_0(x)) \;=\; M_0\bigl(\rho_{\max} - \rho^*\bigr) - M_0 A\,\exp\!\bigl(-x^2/(2\sigma^2)\bigr).
$$

Define

$$
M_\infty \;\equiv\; M_0(\rho_{\max} - \rho^*),
\qquad
a \;\equiv\; \frac{A}{\rho_{\max} - \rho^*} \in [0, 1],
\qquad
u(x) \;\equiv\; a\,\exp\!\bigl(-x^2/(2\sigma^2)\bigr).
$$

Then

$$
\boxed{\;\; M(\rho_0(x)) \;=\; M_\infty\bigl(1 - u(x)\bigr),
\qquad
c_s(x) \;=\; \sqrt{M_\infty}\,\sqrt{1-u(x)}. \;\;}
$$

### 2B. Asymptotic behaviour

- `|x| → ∞`: `u → 0`, `M → M_∞`, `c_s → √M_∞ = c_∞`. Flat Minkowski acoustic metric with speed `c_∞`.
- `x = 0`, `a < 1`: `u = a`, `M = M_∞(1 − a) > 0`, `c_s = c_∞ √(1 − a)`. Finite, reduced signal speed at bump center.
- `x = 0`, `a = 1`: `u = 1`, `M = 0`, `c_s = 0`. Acoustic horizon at `x = 0`.

### 2C. Derivatives needed for curvature

Using `u' = −(x/σ²)u`, `u'' = [(x² − σ²)/σ⁴]u`:

$$
M' = -M_\infty\,u' = M_\infty\,\frac{x u}{\sigma^2},
\qquad
M'' = -M_\infty\,u'' = -M_\infty\,\frac{(x^2 - \sigma^2)u}{\sigma^4}.
$$

Letting `N(x) ≡ c_s(x) = √M(ρ_0(x))`:

$$
\frac{N'}{N} \;=\; \frac{M'}{2M} \;=\; \frac{-u'}{2(1-u)} \;=\; \frac{x u}{2\sigma^2(1-u)}.
$$

---

## 3. Full Curvature Calculation for `g^{eff}`

Metric `g^{eff}_{μν} = diag(−N²(x), 1, 1, 1)` with `N = √M`; inverse `g^{μν} = diag(−1/N², 1, 1, 1)`; `√(−g) = N`.

### 3A. Christoffel symbols

Non-zero components only (all others vanish because the spatial metric is flat and `N` depends on `x` only):

$$
\Gamma^0_{0x} \;=\; \Gamma^0_{x0} \;=\; \frac{N'}{N},
\qquad
\Gamma^x_{00} \;=\; N N'.
$$

All `Γ^y_{··}, Γ^z_{··} = 0`. All `Γ^0_{ij} = Γ^x_{ij} = 0` for spatial `i, j ∈ {y, z}` or for cross-terms.

### 3B. Riemann tensor components

Using the static-metric-with-flat-spatial-section formulas (derivation in Appendix A):

$$
R^0_{\ x0x} \;=\; -\frac{N''}{N},
\qquad
R^x_{\ 0x0} \;=\; N N''.
$$

Fully covariant (for downstream use):

$$
R_{0x0x} \;=\; g_{00}\,R^0_{\ x0x} \;=\; N N''.
$$

All other components of `R^ρ_{\ σμν}` involving the transverse directions `y, z` vanish, because the conformal factor depends only on `x`.

### 3C. Ricci tensor

$$
R_{00} \;=\; R^\rho_{\ 0\rho 0} \;=\; R^x_{\ 0x0} \;=\; N N''.
$$

$$
R_{xx} \;=\; R^\rho_{\ x\rho x} \;=\; R^0_{\ x0x} \;=\; -\frac{N''}{N}.
$$

$$
R_{yy} \;=\; R_{zz} \;=\; R_{0i} \;=\; 0 \quad (\text{for transverse } i = y, z).
$$

### 3D. Ricci scalar

$$
R \;=\; g^{\mu\nu}R_{\mu\nu} \;=\; g^{00}R_{00} + g^{xx}R_{xx} \;=\; -\frac{NN''}{N^2} + \left(-\frac{N''}{N}\right) \;=\; -\frac{2N''}{N}.
$$

$$
\boxed{\;\; R[g^{\rm eff}] \;=\; -\frac{2N''(x)}{N(x)} \;=\; -\frac{\nabla^2 M}{M} \;+\; \frac{(\nabla M)^2}{2 M^2} \;\;}
$$

(converting `N = √M` via `N''/N = M''/(2M) − (M')²/(4M²)` and simplifying). Structurally: curvature is a second-derivative functional of the background mobility, with the expected `∇²M/M + (∇M/M)²` form from the scoping memo (`ED_Geometry_Emergence_Scoping.md` §2C).

### 3E. Ricci scalar for the Gaussian bump — closed form

Substituting `u(x) = a e^{−x²/(2σ²)}`:

$$
\boxed{\;\; R(x) \;=\; \frac{u(x)}{\sigma^4\bigl(1 - u(x)\bigr)^2}\,\Bigl[\,x^2 - \sigma^2 \;+\; u(x)\!\left(\sigma^2 - \tfrac{x^2}{2}\right)\,\Bigr] \;\;}
$$

### 3F. Key values

At `x = 0` (bump center):

$$
R(0) \;=\; -\frac{a}{\sigma^2(1-a)}.
$$

- Negative scalar curvature. Deepens as `a → 1` (horizon-forming limit): `R(0) → −∞`.
- Magnitude-scales as `1/σ²` — inverse of the squared bump width.

At `x = σ` (characteristic width, `u = a/\sqrt{e} ≈ 0.607 a`):

$$
R(\sigma) \;=\; \frac{u(\sigma)^2}{2\sigma^2\bigl(1-u(\sigma)\bigr)^2} \;>\; 0.
$$

**Sign reversal.** `R < 0` inside `|x| ≲ σ`; `R > 0` outside. The zero-locus of `R` (from §3E's bracket: `x² − σ² + u(σ² − x²/2) = 0`) sits near `|x| ≈ σ` for small `a`, shifting slightly outward as `a` grows.

At `|x| → ∞`: `u → 0`, `R → 0`. Flat spacetime asymptotically.

---

## 4. Interpretation: Curvature as Non-Uniform Update Rate

### 4A. What `R` measures in ED

`c_s(x) = √M(ρ_0(x))` is the local rate at which a linearised ED update propagates. A region of high `ρ_0` (near a P4 bump) has low `M`, hence low `c_s` — updates propagate *slowly* through high-density regions.

`R[g^{eff}] = −2N''/N` is a second-derivative of `N = c_s`. It measures the **non-uniformity** of the update rate: regions where `c_s` varies rapidly across space have large `|R|`.

### 4B. Sign of `R` and its physical meaning

- **`R < 0` in the bump interior (`|x| ≲ σ`).** The update rate has a local *minimum* at the bump center. Null geodesics bend *toward* the bump center (a "gravitational well" for fluctuations). This is consistent with Fermat's principle: "path of easiest updating" — signals spend more time where `c_s` is low, accumulating phase and being deflected inward.
- **`R > 0` in the bump wings (`|x| ≳ σ`).** The update rate is recovering toward its asymptotic value `c_∞`. Null geodesics are defocused here.
- **Sign reversal at `|x| ≈ σ`.** The width `σ` is the natural Ricci-flat surface of the configuration; it is where the effective curvature crosses zero.

### 4C. Localisation on mobility-gradient scale

The curvature `R(x)` is supported on a region of extent `∼ σ` and falls off as `e^{−x²/(2σ²)}` at large `|x|`. **Curvature concentrates exactly where `M` has non-trivial gradients**, which is the affirmative answer to the question in the task spec.

More precisely: the integral `∫ R(x) dx` is dominated by the `|x| ≲ σ` region. As `a → 1`, the bump center's `R(0) ∼ −1/[σ²(1−a)]` diverges, and the curvature becomes increasingly concentrated at `x = 0` — the incipient horizon.

---

## 5. Whether Curvature Concentrates Near Mobility Gradients

**Yes.** Section 4C gives the direct answer: `R(x)` is supported on the mobility-gradient region, falls off exponentially far from the bump, and sharpens as `a → 1`. For the generic smooth unimodal profile, `|R|` peaks at the local extremum of `ρ_0` (bump center) and at the inflection points of `ρ_0`. This is the direct translation into ED of the acoustic-gravity folklore "curvature tracks sound-speed gradients" — now with the specific ED mobility dependence `c_s² = M(ρ_0)`.

---

## 6. Whether Any Profile Produces Schwarzschild-Like Features

### 6A. Schwarzschild structure

Schwarzschild: `ds² = −f(r) dt² + f(r)^{−1} dr² + r²dΩ²` with `f(r) = 1 − 2GM/r`. Crucially:

- `g_{tt} g_{rr} = −1` (non-flat spatial section, with `g_{rr} = 1/f`).
- Horizon at `r = 2GM` where `f(r) = 0` linearly.
- Surface gravity `κ_Sch = 1/(4GM)`, finite and non-zero.

### 6B. ED acoustic metric comparison

Our `g^{eff}_{μν} = diag(−N², 1, 1, 1)` has a **flat spatial section** (`g_{xx} = 1`), not `1/N²`. Therefore `g_{tt} g_{xx} = −N² ≠ −1`. **The ED acoustic metric is not Schwarzschild-like in its spatial sector.** It is closer to a **Rindler-like** metric with position-dependent lapse, without the compensating spatial warp that Schwarzschild has.

### 6C. Consequence: no GR-style black holes

GR-style black holes (finite `κ`, Hawking thermality) require the spatial-warp factor. Without it, the ED acoustic metric can produce horizons in the sense of `N → 0` surfaces, but their detailed structure differs from Schwarzschild's. In particular: § 7 shows that ED acoustic horizons at interior local maxima of `ρ_0` are generically *extremal* (`κ = 0`).

### 6D. Could a different `M(ρ)` form fix this?

Changing `M(ρ) = M_0(ρ_{\max} − ρ)^β` with different `β` rescales how `M` vanishes at the mobility ceiling. For `β = 2`, `M ∼ (ρ_{\max} − ρ_0)^2`, and if `ρ_0 → ρ_{\max}` linearly in `x`, then `M ∼ x^2` near the horizon — still extremal-type. For non-integer `β`, similar scaling analysis. **No choice of `β` alone recovers Schwarzschild's spatial-warp structure**, because the acoustic-metric construction always has flat `g_{ij}` (unless ED's underlying substrate itself has curvature, which it does not by Canon).

---

## 7. Surface Gravity at the P4 Horizon

### 7A. Visser acoustic surface gravity

For a static acoustic metric without background flow, the acoustic surface gravity (Visser 1998) is:

$$
\kappa_{\rm acoustic} \;=\; \frac{1}{2}\,\bigl|\partial_n\,c_s^2\bigr|_{\rm horizon} \;=\; \frac{1}{2}\,\bigl|\partial_n M(\rho_0)\bigr|_{\rm horizon},
$$

where `n` is the direction normal to the horizon, pointing outward.

### 7B. Gaussian bump at `a = 1`: extremal horizon

Horizon at `x = 0`. Normal direction is `±x̂`. Compute:

$$
\partial_x M(\rho_0) \;=\; -M_\infty\,u'(x) \;=\; M_\infty\,\frac{x u(x)}{\sigma^2}.
$$

At `x = 0`: `∂_x M(ρ_0)|_{x=0} = 0`. Therefore

$$
\kappa_{\rm acoustic}\bigr|_{\text{Gaussian},\, a=1} \;=\; 0.
$$

**Extremal / degenerate acoustic horizon.** The vanishing of `κ` at `x = 0` reflects the fact that `ρ_0(x)` has a smooth local maximum at `x = 0`, so `M(ρ_0(x))` has a quadratic minimum (vanishing first derivative).

### 7C. Extremality is generic for interior maxima

For *any* smooth `ρ_0(x)` with an interior local maximum reaching `ρ_{\max}`, the Taylor expansion forces `∂_x ρ_0 = 0` at the maximum, so `∂_x M(ρ_0) = 0` at the acoustic horizon. **All interior-maximum P4 horizons are acoustically extremal.**

This is a significant structural fact: the generic "horizon" formed by a ρ_0-maximum touching ρ_max is NOT a standard non-extremal Killing horizon. It has `κ = 0` by symmetry. No Hawking temperature in the Visser-formula sense.

### 7D. Non-extremal horizons require boundary/monotonic profiles

To get `κ ≠ 0`, need `∂_x M(ρ_0)|_{\rm horizon} ≠ 0`, which means `∂_x ρ_0|_{\rm horizon} ≠ 0`. This requires `ρ_0` to reach `ρ_{\max}` at a point where it is *still increasing* — i.e., `ρ_{\max}` is reached as a boundary value of the accessible region, not as an interior local maximum.

Example: monotonic ramp `ρ_0(x) = ρ^* + (ρ_{\max} − ρ^*)·(1 − x/L)` for `0 ≤ x ≤ L`, with `ρ_0(x = 0) = ρ_{\max}`. Then `M(ρ_0(x)) = M_\infty·(x/L)` and

$$
\kappa_{\rm acoustic}\bigr|_{\rm ramp} \;=\; \frac{M_\infty}{2L}.
$$

Finite. But this profile has `ρ_0(0) = ρ_{\max}` as a boundary value of the domain `[0, L]`, not an interior structure of ED.

### 7E. Structural interpretation

**ED horizons are generically cold.** In the reversible-sector acoustic metric, any horizon formed by `ρ_0` reaching `ρ_{\max}` at an interior point is acoustically extremal, with `κ = 0`. Finite `κ` requires either (i) a boundary horizon (`ρ_{\max}` at the edge of the accessible region) or (ii) a non-smooth profile (kinks, shocks).

This is consistent with ED-06 ("Horizons as Decoupling Surfaces"): the kinetic barrier at `M = 0` is a one-way information boundary, but its thermal properties are trivially cold in the standard acoustic-analogue framework. ED does not automatically produce Hawking-radiating horizons.

---

## 8. Hawking-Like Temperature

### 8A. Standard formula

For a non-extremal Killing horizon with surface gravity `κ`, the Hawking temperature is

$$
T_H \;=\; \frac{\hbar\,\kappa}{2\pi\,k_B}.
$$

In the acoustic-analogue literature (Unruh 1981, Visser 1998), this formula applies with `κ_{\rm acoustic}` in place of `κ_{\rm GR}`, giving a phonon-sector temperature for the analog horizon.

### 8B. Gaussian bump: `T_H = 0`

From §7B: `κ_{\rm acoustic} = 0` at the `a = 1` Gaussian horizon. Therefore

$$
\boxed{\;\; T_H\bigr|_{\text{Gaussian},\, a=1} \;=\; 0. \;\;}
$$

**The ED Gaussian-bump horizon is cold. No Hawking-like radiation.** Consistent with extremality.

### 8C. Monotonic ramp: finite `T_H`

For the §7D ramp:

$$
T_H\bigr|_{\rm ramp} \;=\; \frac{\hbar\,M_\infty}{4\pi\,L\,k_B}.
$$

Finite. In physical units with `M_\infty → c_\infty^2` (from the `c_s = c_0 = c/0.6` identification in `ED_Reversible_Sector_QFT.md` §7E):

$$
T_H \;=\; \frac{\hbar\,c_\infty^2}{4\pi\,L\,k_B} \;=\; \frac{\hbar\,(c/0.6)^2}{4\pi\,L\,k_B}.
$$

For `L` at the Compton length `L \sim \hbar/(m c)` of a particle species, this gives an `O(m c^2)`-scale temperature — enormous, and to be taken as a formal consequence of the acoustic-metric setup, not a physical prediction.

### 8D. Physical plausibility check

- The `T_H > 0` case (monotonic ramp) requires a boundary where `ρ_0 = ρ_{\max}` sharply — not a generic stationary ED configuration.
- Even when `T_H > 0` formally, identifying this with a measurable thermal spectrum requires (i) a quantised fluctuation field (the reversible-sector QFT from `ED_Reversible_Sector_QFT.md`), (ii) a well-defined positive-frequency notion on both sides of the horizon, (iii) a sensible ground state on the full spacetime.
- For ED, only (i) is in hand. (ii) and (iii) are non-trivial; they constitute the full Unruh-Wald calculation in this specific acoustic metric, which is a separate project.

**Bottom line on Hawking-like thermality in ED.** It is *formally definable* for profiles with finite `κ`, but (a) generic interior-maximum horizons are extremal (`κ = 0`, `T_H = 0`), and (b) even for non-extremal profiles, making the thermal identification precise requires the full QFT-on-curved-acoustic-metric construction, not just the metric itself.

---

## 9. Assessment

### 9A. Generic versus profile-dependent features

| Feature | Generic or profile-dependent |
|---|---|
| `R(x)` as a second-derivative functional of `M(ρ_0(x))` | **Generic** — holds for any smooth `ρ_0` |
| Sign reversal of `R` at the characteristic width `σ` | **Profile-dependent** but qualitatively generic for unimodal bumps |
| `R → −∞` at horizon formation (`a → 1`) | **Generic** — divergent curvature at the mobility-collapse surface |
| Curvature localisation on mobility-gradient scale | **Generic** |
| Extremal horizon (`κ = 0`) at interior local maximum | **Generic** — by symmetry, any smooth local max of `ρ_0` gives this |
| Non-extremal horizons (`κ ≠ 0`) require monotonic / boundary profile | **Generic** — follows from smoothness plus `∂_x ρ_0 ≠ 0` requirement |
| Absence of Schwarzschild spatial-warp structure | **Generic** — flat `g_{ij}` is a structural feature of all ED acoustic metrics |
| Specific numerical coefficients (e.g., `R(0) = −a/[σ²(1−a)]`) | **Profile-dependent** |

### 9B. What this supports for ED-10

The geometry-form ED-10 (from `ED_Effective_Acoustic_Metric.md` §5A) is further constrained:

> **Constraint from this memo.** The emergent ED acoustic metric has well-defined Ricci curvature concentrated on mobility gradients, with sign that reflects the bending of update-trajectories around ED density extrema. However, ED horizons formed at generic interior local maxima of `ρ_0` are acoustically *extremal*, with vanishing surface gravity and zero Hawking-like temperature. The kinetic barrier at `M = 0` (ED-06 / Canon P4) is a decoupling surface in the information-flow sense, but not a thermally-radiating surface in the standard acoustic-analogue sense. Finite Hawking-like thermality would require specific monotonic profiles not generated by stationary ED dynamics.

### 9C. What this rules out

- **Rules out** the casual claim "ED black holes radiate Hawking-style" without further qualification. They generically don't.
- **Rules out** Schwarzschild identification of ED's `g^{eff}`. The spatial sector is flat; Schwarzschild's spatial warp is absent.
- **Rules out** the pretension that ED-06 horizons are quantitative GR-horizon analogues beyond the "decoupling surface" kinematic statement.

### 9D. What this does support

- **Supports** the ED-06 claim that mobility-ceiling surfaces are one-way information barriers. They are, via acoustic-metric null-cone degeneration.
- **Supports** the identification of `R[g^{eff}]` with a second-derivative functional of the updating-rate field — "curvature = non-uniformity of updating" is a precise statement.
- **Supports** the kinematic (ii)-grade character of ED-10: emergent geometry in the kinematic sense, without dynamical Einstein equations and without GR-style black-hole thermodynamics.

### 9E. Suggested follow-ups (low priority)

- **Direct 3D spherical profile.** Repeat the calculation for `ρ_0(r) = ρ^* + A·sech²(r/L)` (or similar spherically-symmetric bump). Expect similar qualitative structure: interior-maximum horizon → extremal. Memo: 1 week.
- **Non-smooth/kink profiles.** Investigate whether shock-like transitions in `ρ_0` (e.g., traveling fronts in ED simulation data) produce finite-κ horizons. This would connect to ED-Phys-series work on cluster-merger lags and peak-merging behaviour. Memo: 2–3 weeks.
- **Curvature integrals.** Compute `∫ R d^dx` for the Gaussian bump as a function of `a`; check whether it is bounded or diverges in the horizon limit. Test a topological-charge-like interpretation (probably negative, but worth the explicit check). Memo: 1 week.
- **Generic-sector correction.** Extend the calculation into the weak-dissipation underdamped sector. The acoustic metric rescales `M_0 → (H + ζD)M_0/τ` at leading order; dissipation corrections break the pure metric structure. Memo: 1–2 weeks.

None are urgent; all are ordinary extensions of the concrete calculation here.

---

## Appendix A — Christoffel / Riemann for static metric with flat spatial section

For `g_{μν} = diag(−N²(x), 1, 1, 1)` with `N = N(x)` only, define `N'= ∂_x N, N'' = ∂_x^2 N`. Non-zero Christoffels:

$$
\Gamma^0_{0x} = \frac{N'}{N}, \qquad \Gamma^x_{00} = N N'.
$$

All other components vanish (direct calculation: the only derivatives of metric components are `∂_x g_{00} = −2NN'`, and all other partials of `g_{μν}` are zero).

Non-zero Riemann tensor component:

$$
R^0_{\ x0x} \;=\; \partial_0\Gamma^0_{xx} - \partial_x\Gamma^0_{0x} + \Gamma^0_{0\lambda}\Gamma^\lambda_{xx} - \Gamma^0_{x\lambda}\Gamma^\lambda_{0x}.
$$

Each term: `∂_0 Γ^0_{xx} = 0` (static, Γ^0_{xx} = 0); `∂_x Γ^0_{0x} = ∂_x(N'/N) = N''/N − (N')²/N²`; `Γ^0_{0λ}Γ^λ_{xx} = 0` (all `Γ^λ_{xx} = 0`); `Γ^0_{x\lambda}Γ^\lambda_{0x}`: only `λ = 0` term, giving `Γ^0_{x0}\Gamma^0_{0x} = (N'/N)^2`. Summing:

$$
R^0_{\ x0x} = -\bigl[N''/N - (N')^2/N^2\bigr] - (N')^2/N^2 = -N''/N.
$$

Similarly, `R^x_{\ 0x0} = N N''` by the analogous calculation. All spatial-spatial components `R^y_{···}, R^z_{···}` and cross-terms involving the `y, z` directions vanish. Ricci and scalar follow as in §3C–3D.

---

**Status.** Working memo. Explicit concrete curvature calculation with analytic closed-form result for the 1D Gaussian bump. Substantive findings: (A) curvature localised on mobility-gradient scale with sign reversal at width `σ`; (B) interior-maximum P4 horizons are acoustically extremal (`κ = 0`, `T_H = 0`). No new axioms, no new predictions. Reinforces the (ii)-grade kinematic character of ED-10's emergent-geometry claim.
