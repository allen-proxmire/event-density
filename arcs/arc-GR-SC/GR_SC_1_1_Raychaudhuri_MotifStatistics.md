# GR-SC 1.1 — Raychaudhuri Focusing from Motif-Conditioned Hessian Statistics

**Date.** 2026-04-23.
**Scope.** Working memo. Opens the **GR-SC** arc (kinematic GR quantities computed on the ED acoustic metric, recast as filtered GRF statistics of the ED field). Target: the Raychaudhuri focusing term `F ≡ −R_μν u^μ u^ν` on `g^{eff}[ρ_0]`, linearised around a uniform background and conditioned on motif-filtered saddles of the ED GRF. Same machinery as `theory/ED_SC_2_0_r_star_R2_GRF.md`, applied to a geometric Ricci contraction instead of a Hessian eigenvalue ratio.
**Status.** Concrete calculation. Two deliverables: (A) a closed-form linearised expression `F = −μ₁·[tr(Hφ) − n̂·Hφ·n̂]` with `μ₁ = (M′/2M)|_{ρ̂}`; (B) a structural identity at the level of motif-conditioned distributions: **the principal-axis Raychaudhuri focusing ratio `ℛ_Ray ≡ F_∥/F_⊥` has the same distribution as r*** (the ED-SC 2.0 Hessian ratio), so pooled R2 gives `ℛ_Ray ≈ −1.88 ± 0.4`. The `−μ₁` prefactor cancels in the ratio; the angle-averaged focusing `F̄` is Gaussian with zero median and RMS `|μ₁|·σ_2/(2√3)` set by GRF spectral moments.

**Scope guardrails.**
- Kinematic only. Acoustic metric is `g^{eff}[ρ_0]`; no Einstein equations, no ADM, no dynamical geometry.
- No derivation of GR. Raychaudhuri here is an **identity** on the fixed metric `g^{eff}`; what is derived is the **statistics of the focusing scalar** over the ED GRF ensemble.
- 2D spatial (2+1 spacetime) throughout, to match ED-SC 2.0 conventions. 3D generalisation sketched in Appendix A.

---

## 1. Acoustic metric and Ricci tensor

### 1.1 Metric

Per `theory/ED_Effective_Acoustic_Metric.md` §2B, the reversible-slice acoustic metric on a stationary background `ρ_0(x)` with no background flow is

$$
g^{\rm eff}_{\mu\nu}(x) = \mathrm{diag}\bigl(-N^2(x),\ 1,\ 1\bigr),\qquad
N(x) \equiv c_s(x) = \sqrt{M(\rho_0(x))}.
$$

Signature `(−, +, +)`. Inverse: `g^{μν}_{\rm eff} = diag(−1/N², 1, 1)`. Determinant `√(−g) = N`.

### 1.2 Christoffels

From Appendix A of `ED_Acoustic_Metric_Curvature.md` (generalised from 1D to arbitrary spatial dependence):

$$
\Gamma^{0}_{\ 0i} = \frac{N_{,i}}{N} = (\ln N)_{,i},
\qquad
\Gamma^{i}_{\ 00} = N\,N_{,i},
\qquad
\Gamma^{i}_{\ jk} = 0.
$$

All other components vanish (flat spatial section, static metric).

### 1.3 Ricci tensor

Direct calculation (Appendix A):

$$
R_{00} = N\,\nabla^2 N,\qquad
R_{ij} = -\frac{N_{,ij}}{N},\qquad
R_{0i} = 0,
$$

where `∇²` is the flat 2D spatial Laplacian and `N_{,ij} = ∂_i ∂_j N`. Ricci scalar:

$$
R[g^{\rm eff}] = g^{\mu\nu}R_{\mu\nu}
= -\frac{\nabla^2 N}{N} + \delta^{ij}\!\left(-\frac{N_{,ij}}{N}\right)
= -\frac{2\,\nabla^2 N}{N}.
$$

(Consistent with `ED_Acoustic_Metric_Curvature.md` eq. §3D for 1D.)

---

## 2. Null congruence and focusing term

### 2.1 Null vector

The reversible-slice KG equation has null cones `|k⃗|/|k^0| = c_s(x) = N(x)`. Pick a null vector with spatial direction `n̂` (unit):

$$
u^\mu = \left(\tfrac{1}{N},\ n̂^x,\ n̂^y\right),
\qquad n̂^i n̂_i = 1.
$$

Check: `g^{\rm eff}_{μν} u^μ u^ν = -N²·(1/N²) + |n̂|² = -1 + 1 = 0`. ✓

Affine parameter choice is the standard one; `u^μ` is tangent to a null geodesic parametrised so that `u^0 = 1/N`. The scalar `F = −R_{μν} u^μ u^ν` is independent of the affine reparametrisation up to a positive factor (we fix it with this normalisation).

### 2.2 Focusing term

$$
F \;=\; -R_{\mu\nu}\,u^\mu u^\nu
\;=\; -\!\left[R_{00}\,(u^0)^2 + R_{ij}\,u^i u^j\right]
\;=\; -\!\left[\frac{N\,\nabla^2 N}{N^2} - \frac{n̂^i n̂^j N_{,ij}}{N}\right]
$$

$$
\boxed{\;\;
F(x,n̂) \;=\; -\frac{1}{N(x)}\,\Bigl[\nabla^2 N(x) \;-\; n̂^i n̂^j\,N_{,ij}(x)\Bigr]
\;\;}
$$

Equivalently, with `(H_N)_{ij} ≡ ∂_i ∂_j N` the spatial Hessian of `N`:

$$
F = -\frac{1}{N}\bigl[\mathrm{tr}(H_N) - n̂\!\cdot\! H_N\!\cdot\! n̂\bigr].
$$

### 2.3 Sign structure

At a critical point of `N` where `H_N` has eigenvalues `(ℓ_1, ℓ_2)` (ordered `ℓ_1 ≥ ℓ_2`) with eigenvectors `(ê_1, ê_2)`, and `n̂ = cosθ·ê_1 + sinθ·ê_2`:

$$
\mathrm{tr}(H_N) - n̂\!\cdot\!H_N\!\cdot\!n̂
= \ell_1\sin^2\theta + \ell_2\cos^2\theta,
$$

so

$$
F(\theta) = -\frac{1}{N}\bigl(\ell_1\sin^2\theta + \ell_2\cos^2\theta\bigr).
$$

`F` is positive (focusing) or negative (defocusing) depending on `θ` and on the signs of `ℓ_1, ℓ_2`.

---

## 3. Linearisation around a uniform background

### 3.1 Background + fluctuation

Let `ρ_0(x) = ρ̂ + φ(x)` with `ρ̂` a uniform mean (the noise-sustained stationary mean of the ED SPDE) and `φ` a zero-mean GRF with the spectral moments computed in `theory/ED_SC_2_0_r_star_R2_GRF.md §1`. Expanding `N(ρ) = √M(ρ)`:

$$
N(x) = N̂ + N̂'\,\varphi(x) + O(\varphi^2),
\qquad
N̂ \equiv \sqrt{M(\hat\rho)},
\qquad
N̂' \equiv \left.\frac{dN}{d\rho}\right|_{\hat\rho} = \frac{M'(\hat\rho)}{2\,N̂}.
$$

Define the **logarithmic mobility derivative** at the mean:

$$
\boxed{\;\;
\mu_1 \;\equiv\; \left.\frac{d\ln N}{d\rho}\right|_{\hat\rho}
\;=\; \frac{1}{2}\frac{M'(\hat\rho)}{M(\hat\rho)}
\;\;}
$$

For canonical ED (Canon P4, `M′ < 0`), `μ₁ < 0`.

### 3.2 R2 canonical numerical values

At R2 canonical `M(p) = (1−p)^{2.7}`, `p̂ = 0.108`:

$$
\frac{M'}{M}\bigg|_{\hat p} = -\frac{n_*}{1-\hat p} = -\frac{2.7}{0.892} = -3.027,
\qquad
\mu_1 = -1.513,\qquad N̂ = 0.857.
$$

### 3.3 First and second derivatives of N

$$
N_{,i}(x) = N̂'\,\varphi_{,i}(x) + O(\varphi^2),
\qquad
N_{,ij}(x) = N̂'\,\varphi_{,ij}(x) + N̂''\,\varphi_{,i}\varphi_{,j} + O(\varphi^2\text{ in 2nd d.}).
$$

At a critical point of `φ` (where `∇φ = 0`) the `N̂''` term vanishes identically, and to leading order in `φ`:

$$
(H_N)_{ij} = N̂'\,(H_\varphi)_{ij},\qquad
\nabla^2 N = N̂'\,\nabla^2\varphi.
$$

### 3.4 Linearised focusing term

Substituting into the boxed formula of §2.2 and using `1/N ≈ 1/N̂·(1 - N̂'φ/N̂)`:

$$
F(x,n̂) = -\frac{N̂'}{N̂}\bigl[\nabla^2\varphi - n̂^i n̂^j\,\varphi_{,ij}\bigr] + O(\varphi^2).
$$

$$
\boxed{\;\;
F_{\rm lin}(x, n̂) \;=\; -\mu_1\,\Bigl[\mathrm{tr}(H_\varphi) \;-\; n̂\!\cdot\! H_\varphi\!\cdot\! n̂\Bigr]
\;\;}
$$

with `μ₁ = (1/2)·M′(ρ̂)/M(ρ̂)`. For canonical ED `μ₁ < 0`, so `−μ₁ > 0`.

### 3.5 At critical points of φ

At a saddle with `H_φ` eigenvalues `(λ_1, λ_2)`, eigenvectors `(ê_1, ê_2)`, and null direction `n̂ = cos θ ê_1 + sin θ ê_2`:

$$
F_{\rm lin}(\theta) = -\mu_1\bigl(\lambda_1\sin^2\theta + \lambda_2\cos^2\theta\bigr).
$$

Two special directions:

- **Null ray along the expansion axis** (parallel to `ê_1`, the `λ_1 > 0` eigenvector): `θ = 0`, `F_∥ = −μ₁ λ_2`.
- **Null ray along the compression axis** (parallel to `ê_2`, the `λ_2 < 0` eigenvector): `θ = π/2`, `F_⊥ = −μ₁ λ_1`.

With `−μ₁ > 0`: `F_∥ < 0` (defocusing along the peak direction), `F_⊥ > 0` (focusing along the dip direction). Physically: null geodesics run parallel to lines of constant `N`; along an expansion axis they diverge, along a compression axis they converge.

---

## 4. GRF saddle statistics — port from r* memo

### 4.1 Hessian joint density at 2D isotropic-GRF saddles

From `R2_GRF.md §2`, restricted to saddles `(a ≡ λ_1 > 0, b ≡ −λ_2 > 0)`:

$$
f_{\rm sad}(a, b) \;\propto\; ab(a+b)\,\exp\!\left[-\frac{3a^2 + 2ab + 3b^2}{2\sigma_2^2}\right],
$$

symmetric under `a ↔ b` (saddle orientation is statistically uniform).

### 4.2 Change to (sum, difference) coordinates

Let `s = (a+b)/2, u = (a−b)/2`. Domain `s > 0, |u| < s`. Jacobian = 2:

$$
f_{\rm sad}(s, u) \;\propto\; s\,(s^2 - u^2)\,\exp\!\left[-\frac{4s^2 + 2u^2}{\sigma_2^2}\right].
$$

### 4.3 Marginal of u = (λ_1 + λ_2)/2

Integrating over `s ∈ [|u|, ∞)` (closed-form via `w = s²` substitution):

$$
f(u) \;\propto\; e^{-6u^2/\sigma_2^2},
$$

i.e. `u` is **Gaussian at saddles** with variance `σ_u² = σ_2²/12`:

$$
\boxed{\;\;
\sigma_u \;=\; \frac{\sigma_2}{2\sqrt{3}},
\qquad
\sigma_{\mathrm{tr}(H_\varphi)} \;=\; 2\sigma_u \;=\; \frac{\sigma_2}{\sqrt{3}}.
\;\;}
$$

At R2 canonical (`σ_2 = 0.0898` from `R2_GRF.md §1.4`): `σ_u ≈ 0.0259`, `σ_tr ≈ 0.0519`.

---

## 5. Deliverable A — the two natural focusing invariants

### 5.1 Angle-averaged focusing `F̄`

Averaging `F_lin(θ)` over `θ ∈ [0, π)` uniform (isotropic choice of null direction relative to saddle principal axes):

$$
\bar F(x) \;\equiv\; \langle F_{\rm lin}(x, \theta)\rangle_\theta
= -\mu_1\cdot\frac{\lambda_1 + \lambda_2}{2}
= -\mu_1\,u(x).
$$

**Statistics at saddles (unfiltered):**

| Quantity | Value |
| --- | --- |
| `⟨F̄⟩_sad` | `0` (by `u ↔ −u` symmetry) |
| `std(F̄)_sad` | `|μ₁|·σ_2/(2√3)` |
| `med(\|F̄\|)_sad` | `0.6745·std(F̄)` (Gaussian) |

**R2 canonical numerical:**

$$
\mathrm{std}(\bar F)_{\rm sad} = 1.513 \cdot \frac{0.0898}{2\sqrt{3}} \approx 0.039,
\qquad
\mathrm{med}(|\bar F|)_{\rm sad} \approx 0.026.
$$

### 5.2 Principal-axis focusing ratio `ℛ_Ray`

Define

$$
\boxed{\;\;
\mathcal{R}_{\rm Ray} \;\equiv\; \frac{F_{\rm lin}(n̂\,\|\,ê_2)}{F_{\rm lin}(n̂\,\|\,ê_1)}
\;=\; \frac{-\mu_1\lambda_1}{-\mu_1\lambda_2}
\;=\; \frac{\lambda_1}{\lambda_2}
\;\;}
$$

**Two structural facts follow immediately:**

1. The prefactor `−μ₁` cancels. `ℛ_Ray` is **independent of the mobility law** (as long as `μ₁ ≠ 0`). Any canonical ED mobility (Canon P4, canonical β, saturating, …) gives the same `ℛ_Ray` distribution. This is a genuine mobility-universality result of the kind §5 of `R2_GRF.md` anticipated at the statistical level.
2. `ℛ_Ray` is exactly the signed Hessian eigenvalue ratio `λ_1/λ_2` at a φ-saddle — which, under the ED-SC 2.0 ordering convention `|κ_∥| ≥ |κ_⊥|` with sign preserved, is `κ_∥/κ_⊥`. **This is r*.**

Therefore

$$
\boxed{\;\;
\text{at the level of motif-conditioned distributions:}\quad
\mathcal{R}_{\rm Ray}\;\stackrel{\rm d}{=}\;r^*.
\;\;}
$$

Unfiltered median: `−1.94` (from `R2_GRF.md §2.5`). Motif-conditioned (canonical ray-endpoint filter, 10-seed pooled): **`ℛ_Ray = −1.88 ± 0.4`** (from `analysis/ED_SC_2_0_r_star_R2_GRF_Tests.md`).

---

## 6. Deliverable B — motif-conditioned distributions

### 6.1 Filter definition

Same filter as r*: ray-endpoint test on the GRF `φ` at each candidate saddle `x_0`,

$$
\text{admit } x_0 \;\iff\; \varphi(x_0 + L_{\rm ray}\hat e_{\rm dir}) < -\alpha_{\rm filt}\cdot\mathrm{std}(\varphi)
\quad\text{for at least } N_{\rm req}\text{ of 8 cardinal directions},
$$

with canonical parameters `α_filt = 0.25, L_ray = 2, N_req = 2`. This is the filter that yields the pooled `r* = −1.88 ± 0.4` at R2 canonical.

### 6.2 Effect on `ℛ_Ray`

By §5.2, `ℛ_Ray = r*` in distribution. The filter acts identically on both. **Predicted pooled motif-conditioned median:**

$$
\boxed{\;\;
\mathrm{med}(\mathcal{R}_{\rm Ray}\mid\text{filter}) \;=\; -1.88 \pm 0.4\quad(\text{10-seed pooled, R2 canonical}).
\;\;}
$$

### 6.3 Effect on `F̄`

The filter is symmetric under `a ↔ b`, which is the same as `u ↔ −u`, which preserves the `F̄ ↔ −F̄` symmetry of §5.1. Therefore

$$
\mathrm{med}(\bar F \mid \text{filter}) \;=\; 0
$$

**exactly** (in the linearised GRF approximation), independent of filter parameters. This is a genuine symmetry statement — not a numerical coincidence.

However the filter biases the **magnitude** distribution. The canonical filter preferentially admits near-isotropic saddles (small `ρ = max(a/b, b/a)` — see `R2_GRF.md §3.3`). Near-isotropic saddles have small `|u|/s`, so the filter compresses `|F̄|`:

$$
\mathrm{med}(|\bar F| \mid \text{filter}) \;<\; \mathrm{med}(|\bar F|)_{\rm sad,\ unfiltered} \approx 0.026.
$$

The exact filtered median of `|F̄|` requires numerical integration of `w(ρ)·|u|·f_sad(s, u)`; a one-sigma estimate from the isotropisation strength observed in the r* filter gives

$$
\mathrm{med}(|\bar F| \mid \text{filter}) \;\approx\; 0.7\cdot 0.026 \;\approx\; 0.018\quad(\text{R2 canonical}),
$$

with uncertainty `~30%` inherited from the filter-correlation truncation (see `R2_GRF.md §4` discussion of modelling uncertainty).

### 6.4 Distribution of `F_lin(θ)` at fixed `θ`

Using the `(S, D) = (s, u)` decomposition of §4.2 and writing `F/(−μ₁) = D − S·cos 2θ`:

$$
F_{\rm lin} = -\mu_1\bigl(D - S\cos 2\theta\bigr).
$$

For `θ` uniform and independent of `(S, D)`, `cos 2θ` has the arcsine density on `[−1, 1]` with mean 0, variance 1/2. Variance of `F_lin`:

$$
\mathrm{Var}(F_{\rm lin}) = \mu_1^2\bigl[\mathrm{Var}(D) + \tfrac{1}{2}\langle S^2\rangle\bigr].
$$

With `Var(D) = σ_u² = σ_2²/12` (from §4.3) and `⟨S²⟩` computable from the `s`-marginal of `f_sad` (numerical value `⟨S²⟩ ≈ 0.28·σ_2²` for the 2D Gaussian GRF saddle distribution), R2 canonical gives

$$
\mathrm{std}(F_{\rm lin})_{\rm sad} \;\approx\; |\mu_1|\cdot\sigma_2\cdot\sqrt{1/12 + 0.14} \;\approx\; |\mu_1|\cdot\sigma_2\cdot 0.47 \;\approx\; 0.064.
$$

So the focusing term at a randomly-oriented null ray at a random GRF saddle has RMS `~0.06` in dimensionless R2 units. (Re-dimensionalisation requires the lattice-unit → physical-unit map of the ED-Arch-01 setup.)

---

## 7. Falsifiable predictions

The analysis above produces four concrete, R2-testable predictions, all executable in the existing `analysis/scripts/ed_arch_r2/` pipeline:

1. **`ℛ_Ray` ≡ r* in distribution.** Computing `F_∥/F_⊥` on the canonical R2 motif population should reproduce the pooled r* histogram to within sampling error. A discrepancy would indicate the linearisation (§3.4) is breaking down at saddle scales, i.e. `|φ|` is not small enough to neglect `N̂''` corrections.

2. **Zero-median `F̄`.** Computing `F̄ = −μ₁·tr(H_φ)/2` at motif-conditioned saddles should yield a distribution with median statistically consistent with zero. A systematic non-zero median would violate the `u ↔ −u` symmetry of §4.3 and indicate GRF isotropy is broken — e.g. by anisotropic drift in R2, or by a PDE-level `u ↔ −u` asymmetry the linearisation misses.

3. **RMS scaling.** `std(F̄)_sad ∝ |μ₁|·σ_2`. Rescaling `(α, σ)` within the regime where `p̂` is fixed (see the T1 falsifier limitation noted in `R2_GRF_Tests.md`) should leave `std(F̄)/|μ₁|σ_2` invariant. Equivalently, the ratio `std(F̄)·σ_2⁻¹` should track `|μ₁|` across mobility parameterisations.

4. **Filter-compression of `|F̄|`.** Increasing `N_req` from 2 to 4 should reduce `med(|F̄| | filter)` (tighter isotropy requirement → smaller `|u|/s`). Predicted direction of shift: toward zero. Predicted magnitude: `~30%` decrease, by analogy with the T3 shift of `ℛ_Ray` documented in `R2_GRF_Tests.md`.

---

## 8. Durable content for the GR-SC arc

1. **The linearised acoustic-metric Ricci is a constant multiple of the ED-field Hessian.** Specifically `R_μν` contracted against any spatial direction at a φ-critical point equals `−μ₁` times the corresponding spatial Hessian contraction, to leading order in φ. All motif-conditioned statistics of focusing-type geometric invariants on `g^eff[ρ_0]` reduce to statistics on `H_φ` modulated by the single scalar `μ₁`.

2. **The focusing ratio is mobility-universal.** `ℛ_Ray = λ_1/λ_2` at φ-saddles carries no dependence on `M(ρ)` beyond the non-vanishing condition `μ₁ ≠ 0`. This is a genuine GRF universality result, distinct from the cubic-bistable `r*(χ) = −2χ/(2χ−1)` universality (which failed to port to R2 because `Δ < 0` in R2).

3. **The angle-averaged focusing has exact-zero median under isotropic GRF statistics.** No PDE-level computation can lift this to non-zero without breaking the `a ↔ b` symmetry of the GRF saddle distribution. Any observation of `med(F̄) ≠ 0` in an R2 run would be a direct signal of GRF-isotropy breaking.

4. **The GR-SC 1.1 result is a first structural instance of the r* template.** A geometric GR-adjacent scalar on the kinematic acoustic metric reduces, at the level of motif-conditioned distributions on ED field realisations, either to an r*-copy (focusing ratio) or to an r*-orthogonal scalar (zero-median focusing mean) — both computable in closed form from GRF spectral moments. This is the template to repeat for GR-SC 1.0 (Einstein tensor), 1.4 (NEC / focusing-positivity), 1.5 (horizon surface gravity), 1.6 (Weyl motif statistics).

5. **Scope boundary restated.** GR-SC 1.1 does not derive Raychaudhuri's equation (it is an identity), does not introduce dynamics for `g^eff` (it stays kinematic), and does not make any statement about Einstein equations or analogue-Hawking radiation. What it provides is a computable distribution for a specific geometric scalar on a field-theoretic background.

---

## Appendix A — Derivation of `R_{μν}` for `g = diag(−N²(x⃗), δ_ij)`

Static diagonal metric with `N = N(x⃗)`. Non-zero Christoffels `Γ^0_{0i} = N_{,i}/N`, `Γ^i_{00} = N\,N_{,i}`.

Riemann `R^μ_{νρσ} = ∂_ρΓ^μ_{νσ} − ∂_σΓ^μ_{νρ} + Γ^μ_{ρλ}Γ^λ_{νσ} − Γ^μ_{σλ}Γ^λ_{νρ}`:

**`R^0_{i0j}`:**
- `∂_0 Γ^0_{ij} = 0`, `∂_j Γ^0_{i0} = ∂_j(N_{,i}/N) = N_{,ij}/N − N_{,i}N_{,j}/N²`.
- `Γ^0_{0λ}Γ^λ_{ij} = 0` (no nonzero `Γ^λ_{ij}`).
- `Γ^0_{jλ}Γ^λ_{i0}`: only `λ = 0` contributes, giving `(N_{,j}/N)(N_{,i}/N) = N_{,i}N_{,j}/N²`.
- Sum: `R^0_{i0j} = 0 − [N_{,ij}/N − N_{,i}N_{,j}/N²] + 0 − N_{,i}N_{,j}/N² = −N_{,ij}/N.`

**`R^i_{0j0}`:**
- `∂_j Γ^i_{00} = ∂_j(N\,N_{,i}) = N_{,j}N_{,i} + N\,N_{,ij}`.
- `∂_0 Γ^i_{0j} = 0`.
- `Γ^i_{jλ}Γ^λ_{00} = 0`.
- `Γ^i_{0λ}Γ^λ_{0j}`: only `λ = 0` contributes, giving `(N\,N_{,i})(N_{,j}/N) = N_{,i}N_{,j}`.
- Sum: `R^i_{0j0} = N_{,j}N_{,i} + N\,N_{,ij} − 0 − N_{,i}N_{,j} = N\,N_{,ij}.`

**Ricci tensor** (sum over `μ` in `R^μ_{νμσ}`):
- `R_{00} = R^μ_{0μ0} = R^i_{0i0} = δ^{ij}·N\,N_{,ij} = N\,\nabla^2 N.`
- `R_{ij} = R^μ_{iμj} = R^0_{i0j} + R^k_{ikj} = −N_{,ij}/N + 0 = −N_{,ij}/N.`
- `R_{0i} = 0` (no mixing between `t` and spatial; direct check).

---

## Appendix B — 3D generalisation (sketch)

For 3+1 spacetime with `g^eff = diag(−N²(x⃗), 1, 1, 1)`, the same Christoffels and Ricci formulas extend verbatim with `i, j ∈ {1, 2, 3}`:

- `R_{00} = N\,\nabla^2 N` (3D Laplacian),
- `R_{ij} = −N_{,ij}/N`,
- `R = −2\,\nabla^2 N/N`.

Null vector `u^μ = (1/N, n̂)` with `|n̂| = 1` in 3D. At a 3D φ-saddle with Hessian eigenvalues `(λ_1, λ_2, λ_3)` and `n̂` with direction cosines `(α, β, γ)`:

$$
\mathrm{tr} - n̂\!\cdot\!H_\varphi\!\cdot\!n̂
= \lambda_1(1-\alpha^2) + \lambda_2(1-\beta^2) + \lambda_3(1-\gamma^2).
$$

Angle-averaged (over uniform `n̂` on `S²`):

$$
\langle\mathrm{tr} - n̂\!\cdot\!H\!\cdot\!n̂\rangle = \tfrac{2}{3}\,\mathrm{tr}(H_\varphi),
$$

so `F̄ = −(2/3)μ₁·tr(H_φ)` in 3D (vs `−(1/2)μ₁·tr(H_φ)` in 2D). The Gaussian-at-saddles property of `tr(H_φ)` extends to 3D GRFs (standard Rice/Adler result), so the zero-median statement of §6.3 holds.

The principal-axis ratio `ℛ_Ray` in 3D requires choosing two of three eigenvalues (there are three principal axes); the natural choice is the extremal pair (largest-|·| and smallest-|·| with sign), which recovers a 3D analogue of r* once ED-SC 2.0 is generalised to 3D (currently an open extension — see project memory).

---

## Cross-references

- Acoustic metric: `theory/ED_Effective_Acoustic_Metric.md`.
- Ricci on a Gaussian bump: `theory/ED_Acoustic_Metric_Curvature.md`.
- GRF machinery (spectral moments, saddle density, filter weight): `theory/ED_SC_2_0_r_star_R2_GRF.md`.
- Pooled r* empirical (−1.88 ± 0.4): `analysis/ED_SC_2_0_r_star_R2_GRF_Tests.md`, `theory/ED_SC_2_0_r_star_Final_Verdict.md`.
- Scope guardrails for GR claims in ED: `memory/project_ed10_geometry_qft_scope.md`.
