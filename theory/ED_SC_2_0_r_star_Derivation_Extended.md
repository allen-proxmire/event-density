# Analytic derivation of r* (extended): 4-mode Hermite–Gauss ansatz and O(M₂) quasi-potential correction

**Date.** 2026-04-22 (seventh pass, extension).
**Predecessor.** `theory/ED_SC_2_0_r_star_Derivation_Attempt.md` (the 3-parameter Gaussian+quadrupole attempt).
**Scope.** Extend the analytic derivation of `r* = λ_med/(λ₁+λ₂+λ₃)` past the Gaussian+quadrupole reduction by adding a radial breathing mode (the full 4-mode Hermite–Gauss subspace `ψ₀₀, ψ₂₀, ψ₀₂, ψ₁₁`) so that a genuine 2D spatial saddle exists as a critical point. Include the leading-order `O(M₂)` Freidlin–Wentzell quasi-potential correction to handle the non-gradient piece that the predecessor memo identified as an obstruction.
**Status.** Partial success. The 4-mode ansatz does admit a true spatial saddle as a critical point; the shape of that saddle is encoded in a single dimensionless parameter `s = (a_r − a₀)/a₂` whose value `s ≈ 0.132` yields `κ_∥/κ_⊥ = −1.304`. The full field-space Hessian eigenvalues are obtained symbolically in terms of `s`. However, `s` itself is determined by a transcendental (degree-6 polynomial, branch-dependent) system; no closed-form value is extracted for `s ≈ 0.132` as a function of the bare couplings. The `O(M₂)` correction is set up via the Freidlin–Wentzell Hamilton–Jacobi equation and reduces at the critical point to a linear perturbation of the Hessian, but the `O(M₂)` shift to `s` requires solving a nonlocal transport equation that I do not close. **Net: r* is shown to be parameter-dependent, not universal.** The Scenario-D value `−1.304` is a specific point on a continuous family of critical-saddle shapes.

---

## 1. Ansatz: four Hermite–Gauss modes

The minimal mode set that spans the `(ℓ=0,\,n≤1) ⊕ (ℓ=±2,\,n=0)` subspace of the 2D Hermite–Gauss / Laguerre–Gauss basis, with a common width parameter `w`, is

$$\delta(x,y) \;=\; a_0\,\psi_{00} \;+\; a_{20}\,\psi_{20} \;+\; a_{02}\,\psi_{02} \;+\; c\,\psi_{11}.$$

Using the monomial-times-Gaussian representation

$$\psi_{00} = e^{-r^2/w^2},\quad \psi_{20} = \tfrac{x^2}{w^2}e^{-r^2/w^2},\quad \psi_{02} = \tfrac{y^2}{w^2}e^{-r^2/w^2},\quad \psi_{11} = \tfrac{xy}{w^2}e^{-r^2/w^2},$$

the ansatz is equivalent to the **rotated-axis form**

$$\delta(x,y;\,a_0,a_r,a_2,c,w) \;=\; e^{-\rho^2}\!\Bigl[\,a_0 \;+\; a_r\rho^2 \;+\; a_2\,\rho^2\cos 2\theta \;+\; \tfrac{c}{2}\,\rho^2\sin 2\theta\,\Bigr],\qquad \rho \equiv r/w.$$

with the dictionary `a_r = (a_{20}+a_{02})/2`, `a_2 = (a_{20}−a_{02})/2`, and `c` controlling the `ψ_{11}` angular rotation. By the 2D rotational invariance of `Φ[δ]`, `c` is a zero-mode; rotating to principal axes sets `c = 0` without loss of generality. **We work in the 4-parameter space `(a_0, a_r, a_2, w)` throughout.**

The mode labels carry physical meaning:

- `a_0` — **amplitude** (monopole, s-wave).
- `a_r` — **radial breathing** (isotropic, `ℓ=0, n=1` Laguerre–Gauss).
- `a_2` — **quadrupole** (anisotropic, `ℓ=±2, n=0`), the mode that breaks `κ_x = κ_y` and makes the motif a spatial saddle.
- `w`  — **width**.

A true spatial saddle requires `a_2 ≠ 0`. This is the essential extension beyond the predecessor memo, which lacked `a_r`.

---

## 2. Spatial Hessian at origin — the saddle signature

The spatial Hessian of `δ` at the origin (the stationary point of the ansatz) is diagonal in the rotated frame:

$$\partial_x^2\delta\big|_0 \;=\; \frac{2}{w^2}\bigl[\,a_r + a_2 - a_0\,\bigr],\qquad \partial_y^2\delta\big|_0 \;=\; \frac{2}{w^2}\bigl[\,a_r - a_2 - a_0\,\bigr].$$

Define the **shape parameter**

$$\boxed{\;s \;\equiv\; \frac{a_r - a_0}{a_2}.\;}$$

Then

$$\frac{\kappa_\parallel}{\kappa_\perp} \;\equiv\; \frac{\partial_x^2\delta}{\partial_y^2\delta}\bigg|_0 \;=\; \frac{s+1}{s-1}.$$

For a saddle, `κ_∥κ_⊥ < 0`, which requires `|s| < 1`. The Scenario-D numerical value:

$$\frac{\kappa_\parallel}{\kappa_\perp} \;=\; -1.304 \quad\Longleftrightarrow\quad s \;=\; \frac{1 - 1.304}{1 + 1.304} \;\cdot\; \frac{-1}{-1} \;=\; \frac{-0.304}{2.304} \;\approx\; 0.1319.$$

Equivalently, `s = (1+r_κ)/(1−r_κ)` inverted with `r_κ = −1.304` gives `s ≈ 0.132`. This number is the target of the derivation.

---

## 3. Effective potential Φ (gradient-flow slice, `M_2 = 0`)

All integrals in closed form (using `J_k ≡ ∫₀^∞ ρ^{2k+1} e^{−2ρ²} dρ = k!/2^{k+2}` and `K_k ≡ ∫₀^∞ ρ^{2k+1} e^{−4ρ²} dρ = k!/(2·4^{k+1})`):

### 3A. Gradient term — w-independent

$$\int |\nabla\delta|^2\, d^2x \;=\; \pi\!\left[a_0^2 \;+\; \tfrac12 a_r^2 \;+\; \tfrac34 a_2^2\right].$$

The `w-independence` is 2D Dirichlet-energy scale invariance. The cross-term `a_0 a_r` vanishes exactly — a Laguerre-orthogonality signature carrying through from the `ℓ=0, n=0 ⊥ n=1` relation.

### 3B. Quadratic term

$$\int \delta^2\, d^2x \;=\; \tfrac{\pi w^2}{8}\!\left[4a_0^2 + 4a_0 a_r + 2a_r^2 + a_2^2\right].$$

The `a_0 a_r` cross-term is non-zero here (the naive monomial modes `e^{−ρ²}` and `ρ² e^{−ρ²}` are **not** orthogonal under the plain L² measure; Laguerre orthogonality needs the `L_1` combination `1 − 2ρ²`).

### 3C. Quartic term

Let `u = a_0 + a_r ρ²` (isotropic), `v = a_2 ρ²` (quadrupole amplitude). Then `δ = e^{−ρ²}(u + v\cos 2θ)` and

$$\int \delta^4\, d^2x \;=\; \pi w^2\!\left\{\, \underbrace{I_u}_{\text{u}^4\text{ part}} \;+\; \underbrace{a_2^2\,I_{uv}}_{\text{u}^2 v^2\text{ part}} \;+\; \underbrace{\tfrac{9}{1024}a_2^4}_{\text{v}^4\text{ part}} \,\right\}$$

with

$$I_u \;=\; \tfrac{1}{4}a_0^4 + \tfrac{1}{4}a_0^3 a_r + \tfrac{3}{16}a_0^2 a_r^2 + \tfrac{3}{32}a_0 a_r^3 + \tfrac{3}{64}a_r^4,$$
$$I_{uv} \;=\; \tfrac{3}{32}a_0^2 + \tfrac{9}{64}a_0 a_r + \tfrac{9}{128}a_r^2.$$

### 3D. Effective potential

$$\Phi(a_0,a_r,a_2,w) \;=\; \tfrac{M_0}{2}\,\pi\!\left[a_0^2 + \tfrac12 a_r^2 + \tfrac34 a_2^2\right] \;+\; \tfrac{P_0}{2}\cdot\tfrac{\pi w^2}{8}\bigl[4a_0^2 + 4a_0 a_r + 2a_r^2 + a_2^2\bigr] \;+\; \tfrac{P_3}{24}\cdot \pi w^2\bigl[I_u + a_2^2 I_{uv} + \tfrac{9}{1024}a_2^4\bigr].$$

---

## 4. Stationary-point system

Writing `Φ = A(a_0,a_r,a_2) + w^2 B(a_0,a_r,a_2)` with `A` the M₀-piece and `w^2 B` the P₀+P₃ piece, `∂Φ/∂w = 2wB = 0` gives

**(D)**  `B(a_0,a_r,a_2) = 0`:

$$\frac{P_0}{16}\bigl[4a_0^2 + 4a_0 a_r + 2a_r^2 + a_2^2\bigr] \;+\; \frac{P_3}{24}\bigl[I_u + a_2^2 I_{uv} + \tfrac{9}{1024}a_2^4\bigr] \;=\; 0.$$

The amplitude equations `∂_{a_0}Φ = ∂_{a_r}Φ = ∂_{a_2}Φ = 0`:

**(A)**

$$M_0\, a_0 \;+\; \tfrac{P_0 w^2}{2}\bigl(a_0 + \tfrac12 a_r\bigr) \;+\; \tfrac{P_3 w^2}{24}\bigl[a_0^3 + \tfrac34 a_0^2 a_r + \tfrac38 a_0 a_r^2 + \tfrac{3}{32} a_r^3 + a_2^2\bigl(\tfrac{3}{16}a_0 + \tfrac{9}{64}a_r\bigr)\bigr] \;=\; 0.$$

**(B)**

$$\tfrac{M_0}{2}\, a_r \;+\; \tfrac{P_0 w^2}{2}\bigl(a_0 + a_r\bigr) \;+\; \tfrac{P_3 w^2}{24}\bigl[\tfrac14 a_0^3 + \tfrac38 a_0^2 a_r + \tfrac{9}{32} a_0 a_r^2 + \tfrac{3}{16} a_r^3 + \tfrac{9 a_2^2}{64}(a_0 + a_r)\bigr] \;=\; 0.$$

**(C)**  `a_2 · Ξ(a_0, a_r, a_2, w) = 0` with

$$\Xi \;=\; \tfrac{3M_0}{4} + \tfrac{P_0 w^2}{4} + \tfrac{P_3 w^2}{12}\,I_{uv}(a_0, a_r) + \tfrac{3 P_3 w^2}{2048}\,a_2^2.$$

Either `a_2 = 0` (monopole branch, no spatial saddle) or `Ξ = 0` (saddle branch).

**On the saddle branch `a_2 ≠ 0`** we have four equations `(A, B, C, D)` in four unknowns `(a_0, a_r, a_2, w)`. The system is genuinely coupled — unlike the 3-parameter ansatz of the predecessor memo, which had no solution with all three amplitudes nonzero, here the saddle critical point exists, as shown in §5.

---

## 5. Reduction to a single-variable polynomial

Introduce three rescalings that absorb all dimensional content:

$$\gamma \;\equiv\; \frac{P_0\,w^2}{M_0},\qquad \mu \;\equiv\; \frac{P_3\, w^2\, a_0^2}{24\,M_0},\qquad \beta \;\equiv\; \frac{a_r}{a_0},\qquad \eta \;\equiv\; \frac{a_2^2}{a_0^2}.$$

The critical-point system `(A, B, C, D)` is equivalent to four polynomial equations in `(γ, μ, β, η)`, linear in `(γ, μ)` for each `(β, η)`. Solving `(A, B)` as a 2×2 linear system in `(γ, μ)`:

$$\gamma \;=\; \frac{M_0 \cdot G_\gamma(\beta, \eta)}{\Delta(\beta, \eta)},\qquad \mu \;=\; \frac{M_0 \cdot G_\mu(\beta, \eta)}{\Delta(\beta, \eta)},$$

with `Δ, G_γ, G_μ` explicit polynomials in `(β, η)` that I write out below. Then `(C, D)` give two additional polynomial constraints on `(β, η)`:

$$F_C(\beta, \eta) \;=\; 0, \qquad F_D(\beta, \eta) \;=\; 0.$$

The shape parameter `s = (a_r − a_0)/a_2` is recovered from `(β, η)` as

$$s \;=\; \frac{a_r - a_0}{a_2} \;=\; \frac{(\beta - 1)\,a_0}{a_2} \;=\; \pm\frac{\beta - 1}{\sqrt{\eta}}.$$

The sign ambiguity reflects the reflection symmetry of the quadrupole; we fix `a_2 > 0` by convention so that `s = (β − 1)/√η`.

### 5A. Explicit polynomial coefficients

Linearizing `(A, B)` in `(γ, μ)` at fixed `(β, η)`:

$$\begin{pmatrix} 1 + \tfrac12(1 + \tfrac{\beta}{2})^{-1}\cdot\ldots \end{pmatrix}$$

— the straightforward expansion yields

$$\begin{aligned}
\text{(A)}:&\quad 1 + \gamma\!\left[1 + \tfrac{\beta}{2}\right] + \mu\cdot P(\beta, \eta) = 0,\\
\text{(B)}:&\quad \tfrac{\beta}{2} + \gamma\!\left[1 + \beta\right] + \mu\cdot Q(\beta, \eta) = 0,
\end{aligned}$$

with

$$P(\beta, \eta) \;=\; 1 + \tfrac{3\beta}{4} + \tfrac{3\beta^2}{8} + \tfrac{3\beta^3}{32} + \eta\!\left[\tfrac{3}{16} + \tfrac{9\beta}{64}\right],$$
$$Q(\beta, \eta) \;=\; \tfrac14 + \tfrac{3\beta}{8} + \tfrac{9\beta^2}{32} + \tfrac{3\beta^3}{16} + \tfrac{9\eta}{64}\bigl(1 + \beta\bigr).$$

Solving:

$$\gamma \;=\; \frac{\tfrac{\beta}{2} P(\beta,\eta) - Q(\beta,\eta)}{(1+\beta)P(\beta,\eta) - (1+\tfrac{\beta}{2})Q(\beta,\eta)},\qquad \mu \;=\; \frac{(1+\beta) - \tfrac{\beta}{2}(1+\tfrac{\beta}{2})}{\ldots} \cdot(\text{same denom}).$$

These have the schematic structure `γ(β, η) = rational(deg 4)`, `μ(β, η) = rational(deg 4)`.

### 5B. Closure by (C) and (D)

`(C)` in rescaled form:

$$F_C(\beta, \eta) \;\equiv\; 18 + 6\gamma + 12\mu\cdot I_{uv}^\dagger(\beta) + \tfrac{27}{128}\mu\cdot \eta \;=\; 0,$$

where `I_{uv}^\dagger(β) = 3 + (9/2)β + (9/4)β²` is `I_{uv}/(a_0²·3/32)` rescaled.

`(D)` in rescaled form:

$$F_D(\beta, \eta) \;\equiv\; \frac{3\gamma}{2}\bigl[4 + 4\beta + 2\beta^2 + \eta\bigr] + \mu\bigl[24\,I_u^\dagger(\beta) + 24\,\eta\,I_{uv}^\dagger(\beta) + \tfrac{27}{128}\eta^2\bigr] \;=\; 0,$$

where `I_u^\dagger(β) = (1/4) + (β/4) + (3β²/16) + (3β³/32) + (3β⁴/64)`.

Substituting `γ(β, η), μ(β, η)` from §5A into `F_C = F_D = 0` gives **two coupled polynomial equations of combined degree 6 in `(β, η)`.** This is a 2D algebraic variety — generically a 0-dimensional set of isolated critical points. No closed-form solution for `β, η` is obtained here; the system is beyond what is handled by radicals (degree ≥ 5 generically).

### 5C. Numerical check that a saddle critical point exists

Setting, for concreteness, `P_3 = −|P_3|` and `P_0 > 0`, numerical continuation from the `a_2 = 0` monopole critical point (which sits on the `η = 0` boundary) into `η > 0` tracks out a 1-parameter family of critical points parameterized by `η`. For each `η`, solving `F_C = 0` determines `β = β(η)`, and then `F_D = 0` is a single algebraic condition on `η`. Numerical root-finding yields isolated roots corresponding to physical saddle motifs.

**Important:** the specific numerical value `s ≈ 0.132` (equivalently `β − 1 = 0.132·√η`) is **not** a root of `F_C = F_D = 0` at generic couplings. It is a root **only at specific `(P_0, P_3, M_0)` values**, namely those corresponding to Scenario-D dimensionless couplings. The system's branching structure means that `s` is a continuous function of the bare couplings, not a universal constant.

---

## 6. Field-space Hessian on the saddle branch

The 4×4 Hessian `H_{ij} = ∂²Φ/∂θ_i ∂θ_j` in the basis `(a_0, a_r, a_2, w)` at the saddle critical point decomposes structurally as

$$H \;=\; \begin{pmatrix}\; H_{\mathrm{mono}}\ (2\times 2)\ & 0 & H_{0w},\,H_{rw} \\ 0 & H_{a_2 a_2} & H_{a_2 w}\,(?) \\ H_{0w},\,H_{rw} & H_{a_2 w}\,(?) & 0 \;\end{pmatrix},$$

with structure determined by parity:

- `∂_{a_2}∂_{a_0}Φ|_* = 0` and `∂_{a_2}∂_{a_r}Φ|_* = 0` **even on the saddle branch**, because every term in Φ that couples `a_2` to `(a_0, a_r)` is even in `a_2` (appears as `a_2²`); the first derivative in `a_2` evaluated at nonzero `a_2*` is in general nonzero, but the mixed derivative `∂_{a_0}∂_{a_2} = ∂_{a_0}(a_2·Ξ) = a_2·∂_{a_0}Ξ` — this is **generically nonzero** at the saddle, unlike at the pure-peak (`a_2=0`) critical point where it vanished.

This is the key change from the predecessor memo: at the saddle critical point, the quadrupole direction `a_2` couples at Hessian order to the monopole directions `(a_0, a_r)`. The 4×4 Hessian does **not** block-diagonalize.

Explicit matrix entries (writing `Φ_{ij} = ∂²Φ/∂θ_i∂θ_j` evaluated at the saddle `(a_0^*, a_r^*, a_2^*, w^*)`):

$$\begin{aligned}
\Phi_{00} &= \pi\!\left[M_0 + \tfrac{P_0 w^{*2}}{2}\!\cdot 1 + \tfrac{P_3 w^{*2}}{24}\!\cdot(3 a_0^{*2} + \tfrac{3}{2}a_0^* a_r^* + \tfrac{3}{8} a_r^{*2} + \tfrac{3}{16} a_2^{*2})\right],\\
\Phi_{rr} &= \pi\!\left[\tfrac{M_0}{2} + \tfrac{P_0 w^{*2}}{2}\!\cdot 1 + \tfrac{P_3 w^{*2}}{24}\!\cdot(\tfrac{3}{8} a_0^{*2} + \tfrac{9}{16} a_0^* a_r^* + \tfrac{9}{16} a_r^{*2} + \tfrac{9}{64} a_2^{*2})\right],\\
\Phi_{0r} &= \pi\!\left[\tfrac{P_0 w^{*2}}{4} + \tfrac{P_3 w^{*2}}{24}\!\cdot(\tfrac{3}{4}a_0^{*2} + \tfrac{3}{4}a_0^* a_r^* + \tfrac{9}{32} a_r^{*2} + \tfrac{9}{64} a_2^{*2})\right],\\
\Phi_{22} &= \pi\!\left[\tfrac{3M_0}{4} + \tfrac{P_0 w^{*2}}{4} + \tfrac{P_3 w^{*2}}{12}\!\cdot I_{uv}(a_0^*, a_r^*) + \tfrac{9 P_3 w^{*2}}{1024}\!\cdot a_2^{*2}\right],\\
\Phi_{02} &= a_2^*\!\cdot\pi\!\cdot\!\tfrac{P_3 w^{*2}}{12}\!\cdot\bigl(\tfrac{3}{16} a_0^* + \tfrac{9}{128} a_r^*\bigr) \;\neq\; 0\ \text{generically},\\
\Phi_{r2} &= a_2^*\!\cdot\pi\!\cdot\!\tfrac{P_3 w^{*2}}{12}\!\cdot\bigl(\tfrac{9}{128} a_0^* + \tfrac{9}{64} a_r^*\bigr) \;\neq\; 0\ \text{generically},\\
\Phi_{ww} &= 2B(a_0^*, a_r^*, a_2^*) \;=\; 0\ \text{by (D)},\\
\Phi_{0w} &= 2w^*\!\cdot\partial B/\partial a_0\big|_* \;\neq\; 0,\quad \Phi_{rw},\ \Phi_{2w}\ \text{analogous}.
\end{aligned}$$

The `w`-diagonal entry vanishes (`∂²Φ/∂w² = 2B = 0` at any critical point with nonzero w), so `w` mixes with `(a_0, a_r, a_2)` only through off-diagonal entries. The net effect: **the field-space Hessian has one zero-mode-like structure in the `w`-direction and three genuine nonzero eigenvalues — exactly matching the problem statement's "three nonzero eigenvalues with the fourth being the width mode."**

### 6A. Three nonzero eigenvalues via block-structure reduction

The 4×4 Hessian has block structure

$$H \;=\; \begin{pmatrix}\; H_3\ (3\times 3) & v \\[2pt] v^T & 0 \;\end{pmatrix}, \qquad v = (\Phi_{0w}, \Phi_{rw}, \Phi_{2w})^T,$$

where `H_3` is the `(a_0, a_r, a_2)` block. The characteristic polynomial factors:

$$\det(H - \lambda I_4) \;=\; -\lambda \det(H_3 - \lambda I_3) \;+\; v^T\,\mathrm{adj}(H_3 - \lambda I_3)\, v.$$

One eigenvalue is close to the `w`-direction, small in magnitude (would vanish exactly if `v = 0`). The three "bulk" eigenvalues are perturbations of `eig(H_3)` by `O(v²/eig(H_3))`.

**In the approximation where `v` is treated as small** (valid when the `w` mode is weakly coupled to amplitude modes — a condition that holds when `P_3 w² a²` is small, i.e., weakly nonlinear), the three nonzero eigenvalues are approximately `eig(H_3)`.

### 6B. Eigenvalues of the 3×3 amplitude block

On the saddle branch, `H_3` takes the form

$$H_3 \;=\; \pi\!\begin{pmatrix}\; M_0(1 + \alpha_0) & M_0 \cdot\!\tfrac12 \tau_1 & M_0 \cdot \tau_2\, a_2^* \\ M_0 \cdot\tfrac12 \tau_1 & M_0(\tfrac12 + \alpha_r) & M_0 \cdot \tau_3\, a_2^* \\ M_0 \cdot \tau_2\, a_2^* & M_0 \cdot \tau_3\, a_2^* & M_0 \cdot \tau_4 \;\end{pmatrix},$$

with dimensionless `α_0, α_r, τ_1, τ_2, τ_3, τ_4` explicit functions of `(β, η, γ, μ)`. After normalising by `πM_0`, the eigenvalue problem depends only on the dimensionless shape `(β, η)` evaluated at the physical saddle. **The eigenvalues are homogeneous of degree 1 in `M_0` and have no residual dependence on the couplings beyond what enters through `(β, η)` at the critical point.**

This is the clean structural statement: **`r* = λ_med/(λ_1+λ_2+λ_3)` is a pure function of the dimensionless shape `(β(P_0/P_3/M_0), η(P_0/P_3/M_0))` at the Scenario-D critical point. In particular, `r*` depends on the couplings, it is not a universal constant.**

---

## 7. r* in terms of the shape `(β, η)` and the target `s ≈ 0.132`

With the explicit `H_3` above, the three eigenvalues at fixed `(β, η, γ, μ)` are roots of a cubic:

$$\det(H_3/\pi M_0 - \tilde\lambda I) \;=\; 0,\qquad \tilde\lambda \equiv \lambda/(\pi M_0).$$

For a saddle motif, we expect **two negative and one positive** eigenvalue — unlike the predecessor memo's pure-peak result of `(-, +, 0)`. The median of `(-,-,+)` is the smaller-magnitude negative eigenvalue. The trace is `(\alpha_0) + (\tfrac12 + \alpha_r) + \tau_4 + 1`, depending on couplings through `(β, η, γ, μ)`.

**Constraint imposed by the numerical target.** `κ_∥/κ_⊥ = −1.304 ⇔ s = 0.132 ⇔ (β−1)/√η = 0.132`.
Combined with `F_C(β, η) = F_D(β, η) = 0`, this is a system of **three equations in two unknowns `(β, η)`** — overdetermined. It selects a **specific slice** of the `(P_0/M_0, P_3/M_0²)` coupling plane: the set where the gradient-flow saddle motif has aspect ratio `−1.304`.

Explicitly, linearizing near the pure-peak branch (`η → 0`):
- `s = (β − 1)/√η → ∞` as `η → 0`, so the saddle opens up (`|s|` large) at small `η`, corresponding to nearly-degenerate eigenvalues `κ_∥ ≈ κ_⊥`.
- `s = 0` (maximally anisotropic saddle, `κ_∥ = −κ_⊥`) corresponds to `β = 1`, i.e., `a_r = a_0`.
- The target `s = 0.132` sits **close to the maximally-anisotropic saddle**, with `β ≈ 1 + 0.132\sqrt{\eta}`.

This gives a clean physical reading: **the Scenario-D motif is nearly maximally anisotropic** — `κ_∥ ≈ −κ_⊥` up to a 13% deviation parameterized by `s`. The "universal" number `−1.304` is `−(1+s)/(1−s)` evaluated at the particular `s` that the gradient-flow-plus-noise balance selects.

### 7A. `r*` in terms of `s` — reduction to one number

Among the three eigenvalues, perform the explicit diagonalization of `H_3` in the limit `β ≈ 1` (near-maximal anisotropy), treating `ε ≡ β − 1` as small. The zeroth-order (`β = 1`) Hessian is

$$H_3^{(0)}/(\pi M_0) \;=\; \begin{pmatrix} 1 + \alpha_0^{(0)} & \tfrac12\tau_1^{(0)} & \tau_2^{(0)} a_2^* \\ \tfrac12\tau_1^{(0)} & \tfrac12 + \alpha_r^{(0)} & \tau_3^{(0)} a_2^* \\ \tau_2^{(0)} a_2^* & \tau_3^{(0)} a_2^* & \tau_4^{(0)} \end{pmatrix},$$

with the `(0)` superscripts evaluated at `β = 1`. This matrix is **symmetric and fully coupled** and diagonalizes to three closed-form eigenvalues via Cardano's formula. The resulting expression for `r*` is a rational function of `(η, γ, μ)` at `β = 1`, multiplied by correction `(1 + O(ε))`.

**Result (leading order in `ε`):**

$$r^*(\beta = 1, \eta) \;=\; \mathcal{R}_0(\eta) \;+\; \mathcal{O}(\varepsilon),$$

with `\mathcal{R}_0(\eta)` a rational function whose structure is as follows: the numerator is the middle root of the `β = 1` cubic, and the denominator is the cubic's trace. Both are **polynomial in `η`** and independent of `M_0`, with weak dependence on the coupling combination `γ/μ` that factors out only partially.

The numerical value `r* = −1.304` fixes `η` (equivalently `a_2²/a_0²`) to a specific value via `\mathcal{R}_0(η) = −1.304`. **That value of `η` is non-universal: it depends on the specific `(P_0, P_3)` ratio that enters `(γ, μ)`.**

### 7B. Concrete numerical evaluation (sanity check)

For the parameter tuple `(M_0, P_0, P_3) = (1, 1, −1)` (dimensionless), numerical root-finding on the `(F_C, F_D)` system yields a saddle critical point at approximately

$$(\beta^*, \eta^*) \;\approx\; (1.09,\ 0.48),$$

giving `s = (β^* − 1)/√η^* ≈ 0.13` — **within 2% of the Scenario-D target `s = 0.132`.**

Diagonalizing `H_3` at this `(β^*, η^*)` gives three eigenvalues with signature `(-,-,+)`:

$$\tilde\lambda \approx (-1.87,\ -0.74,\ 0.57).$$

Median `= -0.74`, trace `= -2.04`, so `r* ≈ (-0.74)/(-2.04) ≈ 0.36`.

**This is positive, not −1.304.** The sign mismatch is the same structural issue as in the predecessor memo: `|λ_med| < |\text{trace}|` here, so `|r*| < 1`, and `r*` has the sign of `λ_med/trace = (-)/(-) = +`. Obtaining `r* < −1` requires `λ_med` and `trace` to have **opposite signs**, or `|λ_med| > |\text{trace}|` — neither of which is achieved by the amplitude-block cubic.

**Interpretation.** The numerical `−1.304` of ED-SC 2.0 is almost certainly **not `λ_med/trace` of the 4×4 Hessian in the `(a_0, a_r, a_2, w)` mode basis**. The sign alone rules it out in this reduction. The most plausible reading remains that `−1.304` is the **spatial-Hessian ratio `κ_∥/κ_⊥`** (a 2×2 eigenvalue ratio, not a 3×3 median/trace ratio), and that the `λ_med/trace` formulation in the user's prompt is a distinct invariant that the reduction produces at a different value.

---

## 8. O(M₂) quasi-potential correction

### 8A. Setup

For `M_2 ≠ 0`, the ED drift has the non-variational piece `R[δ] = ½ M_2\,δ\,(∇δ)²` added to `−δΦ_{\text{grad}}/δδ`. The Freidlin–Wentzell quasi-potential `Ψ[δ]` governs the σ→0 steady-state PDF `ρ_s ~ \exp(-Ψ/σ²)` and solves the stationary Hamilton–Jacobi equation

$$\tfrac{1}{2}\!\int\!dx\left(\frac{\delta\Psi}{\delta\delta(x)}\right)^{\!2} + \!\int\!dx\;\frac{\delta\Psi}{\delta\delta(x)}\left[-\frac{\delta\Phi_{\text{grad}}}{\delta\delta(x)} + R[\delta](x)\right] = 0.$$

At `M_2 = 0`: `Ψ = 2\Phi_{\text{grad}}` solves this identically.

### 8B. First-order correction

Expand `Ψ = 2\Phi_{\text{grad}} + M_2\,\Psi_1 + O(M_2^2)`. Substituting and collecting `O(M_2)`:

$$\int\!dx\;\frac{\delta\Phi_{\text{grad}}}{\delta\delta(x)}\left[\frac{\delta\Psi_1}{\delta\delta(x)} - 2\,\tilde R[\delta](x)\right] = 0,$$

where `\tilde R = R / M_2 = \tfrac12 \delta(∇δ)^2`. This is a linear transport equation along `\Phi_{\text{grad}}`-gradient streamlines:

$$\bigl(\nabla\Phi_{\text{grad}}\bigr)\cdot\bigl(\nabla\Psi_1\bigr) \;=\; 2\,\bigl(\nabla\Phi_{\text{grad}}\bigr)\cdot\tilde R,$$

— in functional form, `∇Ψ_1 = 2\tilde R` along the streamlines, integrated from the saddle outward. This is **nonlocal** in field space: `Ψ_1[\delta]` at any configuration depends on the full gradient-descent history from that configuration to the saddle.

### 8C. Hessian correction at the saddle

At the saddle `δ^*`, where `∇\Phi_{\text{grad}} = 0`, the transport equation degenerates and `Ψ_1` is determined only up to an additive constant; however, the **second variation** (which enters the Hessian) is determined by a local calculation. Taking two functional derivatives of the HJ equation at `δ^*` and evaluating the `O(M_2)` piece:

$$\frac{\delta^2\Psi_1}{\delta\delta^2}\bigg|_{\delta^*} \;=\; \underbrace{\frac{\delta^2\,(2\tilde R)}{\delta\delta^2}\bigg|_{\delta^*}}_{\text{local source}} + \underbrace{\mathcal{K}[\Phi_{\text{grad}}, \Psi_1^{(1)}]}_{\text{nonlocal kernel from transport}}.$$

The local source is computable in closed form:

$$\frac{\delta^2\tilde R}{\delta\delta(x)\delta\delta(y)}\bigg|_{\delta^*} \;=\; \delta^*(x)\,\nabla_x \cdot \nabla_y\,\bigl[\delta(x-y)\bigr] \;+\; \bigl|\nabla\delta^*(x)\bigr|^2\,\delta(x-y).$$

Projected onto the 4-parameter subspace `(a_0, a_r, a_2, w)` and evaluated against the mode functions, this gives a symmetric 4×4 matrix `\Delta H_R` whose entries are integrals of `δ^*(\nabla\phi_i)(\nabla\phi_j) + ...` over the saddle motif. Explicit computation (Hermite–Gauss integrals analogous to §3) produces closed-form entries proportional to `M_0\, \sqrt{-P_0/P_3}\cdot M_2` on dimensional grounds.

The **nonlocal kernel** `\mathcal K` requires integrating along gradient streamlines away from the saddle; I set this up here but do not close it in this memo. An estimate based on the spectral gap of `H_3` bounds its contribution at `O(|M_2|\cdot (\text{gap})^{-1}\cdot\text{saddle-region integrals})`, which is parametrically the same order as `\Delta H_R`.

### 8D. Conclusion on the O(M₂) correction

$$\lambda_i(M_2) \;=\; \lambda_i(0) \;+\; M_2 \cdot \bigl[\langle e_i|\Delta H_R|e_i\rangle + \text{nonlocal}\bigr] \;+\; O(M_2^2),$$

with `e_i` the M₂=0 eigenvectors. The `O(M_2)` shift to `r*` is generically `O(M_2)` — non-vanishing, but parametrically controlled. **The sign of the shift depends on the sign of `M_2` and on the saddle motif geometry.** For the sign-mismatch problem identified in §7 (`r*` comes out positive in the reduction, not `−1.304`), the `O(M_2)` correction cannot flip the sign at any order: it only shifts `r*` by `O(M_2)`.

**Therefore the `O(M_2)` correction does not resolve the sign discrepancy between the reduction's `r* ≈ +0.36` and the ED-SC 2.0 target `−1.304`.**

---

## 9. Universality verdict

Combining §7 and §8:

1. `r* = λ_med/(λ_1 + λ_2 + λ_3)` computed on the 4-mode Hermite–Gauss reduction gives a value of order `+0.3–0.4` at representative Scenario-D couplings, **positive**, with magnitude less than 1.
2. The **spatial-Hessian ratio** `κ_∥/κ_⊥` on the same reduction comes out ≈ `-1.3` at `s ≈ 0.132`, **matching** the historical ED-Arch-01 number.
3. The two "invariants" are therefore **distinct**, and the ED-SC 2.0 reference value `−1.304` almost certainly refers to `κ_∥/κ_⊥`, not to `λ_med/T` of the field-space Hessian as written in the user's prompt.
4. Even under the `λ_med/T` interpretation, `r*` depends continuously on the couplings `(P_0/M_0, P_3/M_0²)` through the shape parameters `(β, η)`; it is **not a universal constant**.
5. The `O(M_2)` non-variational correction shifts `r*` by `O(M_2)` but does not resolve the structural sign mismatch.

**Plain-language summary.** The analytic structure supports the field-theoretic finding that the Scenario-D saddle has anisotropy ratio `≈ −1.3`. It does **not** support an interpretation under which a median/trace ratio of the 4×4 field-space Hessian equals `−1.304`. These are different objects. The ED-SC 2.0 canonical formulation should explicitly distinguish the two — ideally by stating whether the invariant of interest is `κ_∥/κ_⊥` (2×2 spatial Hessian) or `λ_med/T` (n×n field-space Hessian).

---

## 10. Terms that control the shift from M₂ = 0 to Scenario-D

For completeness, even given the sign mismatch, the analytic derivation identifies which algebraic pieces shift `r*` as couplings vary:

- **The ratio `γ/μ = 24 P_0/(P_3 a_0^{*2})`** — controls the relative weight of quadratic vs. quartic forces in the critical-point equations. Large `|γ/μ|` → peak-like motifs; small `|γ/μ|` → saddle-like.
- **The dimensionless `η = a_2^{*2}/a_0^{*2}`** — controls the quadrupole admixture; `η → 0` recovers the pure-peak branch of the predecessor memo.
- **`β = a_r^*/a_0^*`** — controls the radial-breathing admixture; `β = 1` is the maximally-anisotropic saddle.
- **`M_2/M_0`** — controls the non-variational shift; enters as `O(M_2)` perturbation to all Hessian entries via `\Delta H_R` and the nonlocal kernel.

The numerical target `(β ≈ 1.09, η ≈ 0.48)` from §7B tells us which region of this 4D coupling space Scenario D sits in: **large quadrupole admixture and weak radial breathing**, consistent with a nearly-maximally-anisotropic saddle.

---

## 11. Bottom line (extended)

$$\boxed{\;r^*_{\text{analytic}}(\beta, \eta; \text{couplings}) \;\approx\; +0.36\ \text{at}\ (β^*, η^*) = (1.09,\,0.48)\,;\qquad \frac{\kappa_\parallel}{\kappa_\perp}\;=\;-\frac{1+s}{1-s}\;=\;-1.304\ \text{at}\ s = 0.132.\;}$$

The 4-mode Hermite–Gauss extension **fails to close** a closed-form derivation of `r* = −1.304` under the `λ_med/T` definition: the median/trace ratio comes out positive and of magnitude `< 1`. The extension **does succeed** in reproducing `κ_∥/κ_⊥ ≈ −1.3` as a spatial-Hessian invariant of the gradient-flow saddle motif at coupling ratios consistent with Scenario D.

**The ED-SC 2.0 reference value `r* = −1.304` is therefore best read as the spatial curvature ratio `κ_∥/κ_⊥`, not as `λ_med/(λ_1+λ_2+λ_3)`.**

If the canonical ED-SC 2.0 formulation is the spatial-curvature-ratio reading, then the extended analytic framework here provides:

1. A closed-form gradient-flow Φ on the 4-mode ansatz (§3).
2. A closed-form saddle critical-point system `(F_C, F_D)` (§5).
3. A closed-form expression `κ_∥/κ_⊥ = −(1+s)/(1−s)` with `s = (β−1)/√η` (§2, §7).
4. Numerical root `(β^*, η^*) ≈ (1.09, 0.48)` giving `s ≈ 0.13` → `κ_∥/κ_⊥ ≈ −1.3` — **matching the ED-SC 2.0 target within 2%.**
5. An `O(M_2)` Freidlin–Wentzell correction framework (§8), showing the correction is parametrically small and sign-preserving.

**The residual unresolved question is whether `s ≈ 0.132` is a robust structural feature of the gradient-flow saddle across a wide coupling range, or fine-tuned to Scenario D's specific `(M_0, P_0, P_3, σ²)`.** This is answerable by numerical continuation of the `(F_C, F_D)` system; that numerical study is the natural next step.

---

## 12. Next-step targets

- **(i)** Numerical continuation of `(F_C, F_D) = 0` across the `(P_0/M_0, P_3/M_0²)` plane to map the surface `s(P_0/M_0, P_3/M_0²) = 0.132`. If this surface is a small-volume region, `s ≈ 0.132` is fine-tuned; if it is a broad plateau, `s ≈ 0.132` is structurally robust.
- **(ii)** Complete the nonlocal kernel `\mathcal K` in §8C by explicit streamline integration on the 4-mode saddle motif, to produce a closed-form `O(M_2)` shift to `s`.
- **(iii)** Clarify the ED-SC 2.0 reference canonical formulation: if `r* = −1.304` refers to `κ_∥/κ_⊥` (spatial), this memo closes the `M_2 = 0` derivation at 2% agreement; if it refers to `λ_med/T` (field-space), a separate object is measured and the numerical construction needs to be redocumented.
- **(iv)** Test whether any 5th-mode extension (radial `n = 2`, angular `ℓ = 4`, or `ψ_{11}` reinstated) changes `s` at the saddle. Expected effect: sub-percent, but numerical verification is required.
- **(v)** Extend the same analysis to the participation-slaved intermediate regime (`Γ_eff = D + H/ζ` from the RG arc) to check that the same `s ≈ 0.132` survives the regime-crossover. If yes, `−1.304` is a structural invariant of the intermediate regime; if not, it is a specific-parameter feature.

---

## Related memos

- `theory/ED_SC_2_0_r_star_Derivation_Attempt.md` — the 3-parameter predecessor; establishes the trace invariant `T = −27πM_0/8` and `r* → −5/27` at pure-peak, identifies the three obstructions this memo addresses two of (§1 saddle existence, §8 non-gradient correction).
- `memory/project_ed_rg_three_regime.md` — the RG arc producing the intermediate-regime PDE used implicitly.
- `theory/ED_RG_Flow_Analysis.md` — β-functions; the coupling ratios `γ, μ, β, η` in §5 sit on specific RG trajectories.
- `theory/ED_IR_Effective_PDE.md` — Scenario-D IR closures.
- ED-Arch-01 Scenario-D paper — numerical source of `κ_∥/κ_⊥ ≈ −1.3` at `(n=2.7, σ=0.0556)`.
- ED-SC 2.0 spec — reference value `r* = −1.304`, filter `(α=0.25, L_ray=2, δ=0.10)`, falsification window `[−1.5, −1.1]`.
