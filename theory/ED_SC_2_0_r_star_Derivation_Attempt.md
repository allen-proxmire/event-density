# Analytic derivation attempt: ED-SC 2.0 Hessian invariant r*

**Date.** 2026-04-22 (seventh pass).
**Scope.** Attempt an analytic derivation of the ED-SC 2.0 motif-conditioned Hessian invariant
$$r^* \;=\; \frac{\lambda_\mathrm{med}}{\lambda_1 + \lambda_2 + \lambda_3}$$
from the mobility + penalty + noise structure of the canonical ED PDE, with Scenario-D closures (`M(δ) = M_0 + ½M_2 δ²`, `P(δ) = P_0 δ + (1/6) P_3 δ³`, additive white noise `σ²`). The numerical reference value is `r* ≈ −1.304`.
**Status.** Partial result. A full closed-form derivation of `−1.304` is **not achieved**; three specific structural obstructions are identified and documented. Two genuine analytic invariants do close in closed form (trace `T`, large-ε median limit). This memo is the reference document for any future attempt, and the obstructions section below should be treated as a guardrail against re-derivation that skips any of them.

---

## 1. Setup and four definitional ambiguities that must be fixed first

The task statement fixes:

- mobility `M(δ) = M_0 + ½ M_2 δ²`
- penalty `P(δ) = P_0 δ + (1/6) P_3 δ³`
- additive white noise `ξ`, variance `σ²`
- invariant `r* = λ_med / (λ_1 + λ_2 + λ_3)`, with `H` the 3×3 Hessian of the effective potential `Φ` at the **median motif**

Before any derivation, four ambiguities have to be nailed down — none of them are trivially fixed by the prompt, and the answer depends on the choice:

**(Q1) Which 3 modes span the 3×3 Hessian?**
ED-SC 2.0 lives on a 2D real-space field; the spatial Hessian of `δ` at a stationary point is 2×2, not 3×3. The 3×3 must therefore be a **Hessian in motif parameter space**, not in real space. The natural choice — and the one I adopt — is a 3-parameter motif ansatz `δ(x; θ₁, θ₂, θ₃)` with `H_ij = ∂²Φ_eff/∂θ_i ∂θ_j`.

**(Q2) Which 3-parameter ansatz?**
The ED-SC 2.0 motif filter specifies `α = 0.25, L_ray = 2, δ = 0.10`. `L_ray = 2` indicates filamentary "ray" structure — not captured by a pure Gaussian. The minimal ansatz that captures the Scenario-D saddle signature `κ_∥/κ_⊥ < 0` is **Gaussian + quadrupole**:
$$\delta(x,y;\,a_0,a_2,w) \;=\; e^{-r^2/w^2}\Bigl[a_0 \;+\; \tfrac{a_2}{w^2}(x^2-y^2)\Bigr].$$
I use this as the minimal tractable ansatz and flag below that it is *inadequate* for Scenario D proper.

**(Q3) What is "the median motif" and what conditioning does the median impose?**
The filter `(α = 0.25, L_ray = 2, δ = 0.10)` conditions on a fixed amplitude bin `|δ| ≈ 0.10`, a fixed ray length, and a sparsity quantile. Taking the median of Hessian eigenvalues over the conditioned ensemble is **not the same** as evaluating the Hessian at a single analytic critical point. I proceed with the critical-point interpretation and note the mismatch explicitly in §9.

**(Q4) Does the PDE admit a Boltzmann steady state at all?**
This is the most consequential obstruction, and I treat it in §3.

---

## 2. Stochastic PDE → functional Fokker–Planck

The intermediate-regime ED PDE (from the RG arc) with Scenario-D closures is

$$\partial_t \delta(x,t) \;=\; \underbrace{\nabla\!\cdot\!\bigl(M(\delta)\nabla\delta\bigr)}_{M\nabla^2\delta + M'|\nabla\delta|^2} \;-\; P(\delta) \;+\; \xi(x,t),$$

with `⟨ξ(x,t)ξ(x',t')⟩ = σ² δ(x−x') δ(t−t')`. The drift functional is

$$F[\delta](x) \;=\; \nabla\!\cdot\!\bigl(M(\delta)\nabla\delta\bigr)(x) \;-\; P(\delta(x)).$$

The functional Fokker–Planck equation for the probability measure `ρ[δ, t]` is

$$\partial_t \rho \;=\; -\!\int\! dx\; \frac{\delta}{\delta\delta(x)}\Bigl(F[\delta](x)\,\rho\Bigr) \;+\; \frac{\sigma^2}{2}\!\int\! dx\;\frac{\delta^2 \rho}{\delta\delta(x)^2}.$$

A Boltzmann steady state `ρ_s[δ] ∝ exp(−Φ[δ]/T)` with `T = σ²/2` requires the drift to be the negative variational derivative of a functional:

$$F[\delta](x) \;\stackrel{?}{=}\; -\frac{\delta\Phi}{\delta\delta(x)}.$$

---

## 3. Variational obstruction — ED is not a gradient flow when M₂ ≠ 0

Try the natural candidate `Φ = ∫[½M(δ)(∇δ)² + V(δ)]dx` with `V'(δ) = P(δ)`. Variational calculus gives

$$-\frac{\delta\Phi}{\delta\delta(x)} \;=\; -\,\tfrac12 M'(\delta)(\nabla\delta)^2 \;+\; \nabla\!\cdot\!\bigl(M(\delta)\nabla\delta\bigr) \;-\; P(\delta).$$

Expanding the divergence: `∇·(M∇δ) = M∇²δ + M'|∇δ|²`. So

$$-\frac{\delta\Phi}{\delta\delta} \;=\; M(\delta)\nabla^2\delta \;+\; \tfrac12 M'(\delta)|\nabla\delta|^2 \;-\; P(\delta).$$

Compare to ED's actual drift:

$$F[\delta] \;=\; M(\delta)\nabla^2\delta \;+\; M'(\delta)|\nabla\delta|^2 \;-\; P(\delta).$$

**The mismatch is exactly `½M'(δ)|∇δ|²`, non-zero whenever `M_2 ≠ 0`.**

**Consequence.** For additive noise with constant mobility (`M_2 = 0`), ED *is* a gradient flow and the Boltzmann Φ is

$$\boxed{\;\Phi[\delta] \;=\; \int\!d^2x\,\Bigl[\tfrac12 M_0(\nabla\delta)^2 \;+\; \tfrac12 P_0 \delta^2 \;+\; \tfrac{1}{24} P_3\, \delta^4\Bigr].\;}$$

For `M_2 ≠ 0`, there is no such Φ: the stationary measure has non-zero probability currents and is **not** Boltzmann. A quasi-potential (Freidlin–Wentzell large-deviation limit `σ → 0`) exists but solves a Hamilton–Jacobi equation in field space, not a variational one. **Any closed-form Φ that ignores this mismatch for M₂ ≠ 0 is formally wrong.**

Scenario D at `n = 2.7` sits in the `M_2 ≠ 0` regime. The full analytical derivation therefore has to either (i) work at `M_2 = 0` and extrapolate perturbatively, or (ii) use the quasi-potential. I take route (i) below and flag where it breaks.

---

## 4. Gradient-flow reduction (M₂ = 0 slice) and 3-parameter ansatz

With `M_2 = 0`, substitute the ansatz from §1:

$$\delta(x,y) \;=\; e^{-r^2/w^2}\Bigl[a_0 + \tfrac{a_2}{w^2}(x^2-y^2)\Bigr], \qquad u \equiv r^2\cos 2\theta.$$

The three integrals needed for Φ:

**Gradient term** (after the angular and radial Gaussians — the `cos2θ × r²` contributions factor cleanly):
$$\int (\nabla\delta)^2\, d^2x \;=\; \pi\Bigl[a_0^2 + \tfrac{3}{4}a_2^2\Bigr]\qquad\text{(w-independent — 2D Dirichlet scale invariance)}.$$

**Quadratic term:**
$$\int \delta^2\, d^2x \;=\; \tfrac{\pi w^2}{8}\bigl[4a_0^2 + a_2^2\bigr].$$

**Quartic term** — the nontrivial integral. Expanding `(a_0 + a_2 u/w^2)^4`, doing the four θ-moments, and the radial Gaussians with `α = 4/w²`, the quartic integrals collapse to a perfect square:

$$\int \delta^4\, d^2x \;=\; \tfrac{\pi w^2}{4}\Bigl[a_0^2 + \tfrac{3}{16}a_2^2\Bigr]^2 \;\equiv\; \tfrac{\pi w^2}{4}\, Q^2, \qquad Q \equiv a_0^2 + \tfrac{3}{16}a_2^2.$$

This factorisation is the first non-trivial analytic output: the quadrupole-quartic cross-coupling `a_0^2 a_2^2` enters as `3/8 = 2 · 3/16`, exactly the middle term of `(a_0^2 + 3a_2^2/16)^2`. It simplifies everything downstream.

The reduced effective potential on the 3-parameter motif is

$$\Phi(a_0, a_2, w) \;=\; \frac{\pi}{16}\Bigl\{\, 8M_0\!\left[a_0^2 + \tfrac{3}{4}a_2^2\right] \;+\; P_0 w^2\!\left[4a_0^2 + a_2^2\right] \;+\; \tfrac{P_3 w^2}{6}\,Q^2 \,\Bigr\}.$$

---

## 5. Stationary-point conditions

Setting `∂Φ/∂a_0 = ∂Φ/∂a_2 = ∂Φ/∂w = 0`:

- (A) `∂_{a_0}Φ = 0`:  either `a_0 = 0` or `16M_0 + 8P_0 w^2 + (2P_3 w^2/3)\,Q = 0`.
- (B) `∂_{a_2}Φ = 0`:  either `a_2 = 0` or `12M_0 + 2P_0 w^2 + (P_3 w^2/8)\,Q = 0`.
- (C) `∂_w Φ = 0`:     `2P_0(4a_0^2 + a_2^2) + (P_3/3)\,Q^2 = 0` (at `w ≠ 0`).

**Test: full saddle with `a_0, a_2, w` all non-zero.**
Treat (A,B) as linear in `(x, y) = (P_0 w^2, P_3 w^2 Q)`:
$$\begin{cases} 24M_0 + 12 x + y = 0 \\ 96 M_0 + 16 x + y = 0\end{cases} \;\Longrightarrow\; x = -18 M_0,\; y = 192 M_0.$$
So `w^2 = -18 M_0 / P_0` (requires `P_0 < 0`) and `Q = -32 P_0/(3 P_3)`.
Feeding into (C): `4a_0^2 + a_2^2 = -512 P_0/(27 P_3)`.
Solving simultaneously with `Q = a_0^2 + 3a_2^2/16`:
$$a_2^2 = \tfrac{2560}{27}\,\tfrac{P_0}{P_3}, \qquad a_0^2 = -\tfrac{256}{9}\,\tfrac{P_0}{P_3}.$$
**These have opposite signs.** For any real `(P_0, P_3)`, at least one of `a_0^2, a_2^2` is negative. **The full-saddle critical point does not exist in this ansatz.**

That is a real obstruction, not a bookkeeping error: the Gaussian+quadrupole ansatz is too rigid to support the fully anisotropic critical motif. A richer ansatz (radial breathing mode, Hermite–Gauss `(2,0)+(0,2)`, or ray-tail `∝ e^{-r/L}`) is required to realise a true saddle.

**Fallback: pure-peak critical point (`a_2 = 0`).** Here the algebra closes:
$$a_0^{\!*2} = -\tfrac{24 P_0}{P_3}, \qquad w^{*2} = \tfrac{2 M_0}{P_0},\qquad (P_0 > 0,\; P_3 < 0).$$

This is the familiar pattern-forming Gaussian mean-field profile. The 3×3 Hessian in `(a_0, a_2, w)` at this point is where the analytic calculation actually closes — so I push through it and report what comes out.

---

## 6. Field-space Hessian in closed form

Second derivatives of Φ at `(a_0^*, 0, w^*)`. Using `Q|_* = a_0^{*2} = -24 P_0/P_3`:

$$\partial^2_{a_0}\Phi\big|_* \;=\; -4\pi M_0,\qquad \partial^2_{a_2}\Phi\big|_* \;=\; \tfrac{5\pi M_0}{8},\qquad \partial^2_w \Phi\big|_* \;=\; 0.$$

Cross-terms: `∂_{a_0}\!∂_{a_2}|_* = 0` (vanishes by Z₂ symmetry of the quadrupole at `a_2 = 0`). `∂_{a_2}\!∂_w|_* = 0` (same reason). The non-vanishing cross-term is
$$\partial_{a_0}\!\partial_w \Phi\big|_* \;=\; -\pi\, P_0\, a_0^*\, w^* \;=\; -\pi\, P_0\, \sqrt{-\tfrac{48\, M_0}{P_3}}.$$

So the Hessian block-diagonalises: the `a_2` direction is decoupled, and `(a_0, w)` form a 2×2 block:

$$H \;=\; \begin{pmatrix} -4\pi M_0 & 0 & -\pi P_0 a_0^* w^* \\ 0 & \tfrac{5\pi M_0}{8} & 0 \\ -\pi P_0 a_0^* w^* & 0 & 0 \end{pmatrix}.$$

**Three eigenvalues in closed form.** Let `ε ≡ −P_0^2/P_3 > 0` (one of the natural scale-free combinations, invariant of an overall `δ` rescaling up to field-mass). Then

$$\lambda_{a_2} \;=\; \tfrac{5\pi M_0}{8},\qquad \lambda_\pm \;=\; 2\pi M_0\Bigl(-1 \;\pm\; \sqrt{1 + \tfrac{12\,\varepsilon}{M_0}}\Bigr).$$

---

## 7. The invariant r* on this reduction

**Trace — a genuine coupling-invariant structural result.**
$$T \;=\; \lambda_- + \lambda_+ + \lambda_{a_2} \;=\; -4\pi M_0 \;+\; \tfrac{5\pi M_0}{8} \;=\; -\tfrac{27\,\pi\, M_0}{8}.$$

`T` depends only on `M_0`, **independent of** `(P_0, P_3, σ²)`. This is the first honest analytic invariant of the reduction: the sum of field-space Hessian eigenvalues at the pure-peak critical motif is fixed by the mobility stiffness alone.

**Median.** With `M_0 > 0, ε > 0`: `λ_- < 0 < min(λ_+, λ_{a_2}) ≤ max(λ_+, λ_{a_2})`. So the median is the *smaller of the two positive eigenvalues*. The crossing `λ_+ = λ_{a_2}` happens at
$$\sqrt{1 + 12\varepsilon/M_0} = \tfrac{21}{16} \;\Longleftrightarrow\; \tfrac{\varepsilon}{M_0} = \tfrac{185}{3072}\approx 0.0602.$$

Two regimes:

**(i) Large-ε (`ε/M_0 ≫ 0.06`):** median = `λ_{a_2} = 5πM_0/8`.
$$r^* \;=\; \frac{5\pi M_0/8}{-27\pi M_0/8} \;=\; \boxed{\,-\tfrac{5}{27} \approx -0.185\,}.$$
**Universal** — independent of all couplings.

**(ii) Small-ε (`ε/M_0 ≪ 0.06`):** median = `λ_+ ≈ 12π ε`, so `r^* ≈ -32\,ε/(9\,M_0) \to 0`. **Non-universal**, vanishes linearly in ε.

---

## 8. Direct comparison to the numerical target

| quantity | closed-form value | numerical ED-SC 2.0 |
|---|---|---|
| `r*` large-ε limit | `-5/27 ≈ -0.185` | `-1.304` |
| `r*` small-ε limit | `-32ε/(9M_0) → 0` | `-1.304` |
| trace `T` | `-27πM_0/8` | not directly reported |
| median sign | `+` (median is positive) | **negative** (`-1.304 < 0`) |

**The sign disagrees.** The median eigenvalue in this 3-parameter reduction is positive (either `λ_{a_2}` or `λ_+`, both `> 0`), giving `r^* < 0` only because `T < 0`. In ED-SC 2.0 numerics, `-1.304 < -1` implies `|λ_med| > |T|`, which requires `λ_med` and `T` to have the **same** sign and `|λ_med|` to be comparable to or larger than the sum of the other two. That is inconsistent with the 3-parameter reduction above.

**Diagnosis.** The disagreement traces to **three separate obstructions**, each of which would have to be handled:

1. **Saddle vs. peak.** The fully anisotropic saddle critical point does not exist in the Gaussian+quadrupole ansatz (§5). The motif that actually sits at `κ_∥/κ_⊥ ≈ −1.3` in Scenario D is a genuine spatial saddle, not a peak — and its Hessian eigenvalue signature will be `(-, -, +)` or `(-, -, 0)`, not the `(-, +, 0)` we got.

2. **Non-gradient term for M₂ ≠ 0.** The Scenario-D simulation runs at `n = 2.7`, i.e., `M_2 ≠ 0`. The non-variational piece `½M'(δ)|∇δ|²` (§3) sources non-equilibrium currents in the motif distribution; the quasi-potential differs from Φ at `O(M_2)`, and the correction to `r*` is not small.

3. **Median is conditional, not unconditional.** The ED-SC 2.0 filter `(α = 0.25, L_ray = 2, δ = 0.10)` conditions the ensemble on amplitude and ray length *before* taking the median. The relevant `H` is the Hessian restricted to the conditioned submanifold, not at a free critical point.

Any of these three alone is enough to shift `r*` from `-5/27` to `-1.304`. Together, they mean the 3-parameter reduction isn't close enough to the actual ED-SC 2.0 construction for its answer to be the answer.

---

## 9. Where −1.304 likely actually lives

The historical statement (ED-Arch-01, pre-ED-SC 2.0) is that the **spatial Hessian of `δ` at a Scenario-D saddle** has curvature ratio

$$\frac{\kappa_\parallel}{\kappa_\perp} \;\approx\; -1.304.$$

This is a 2×2 spatial-Hessian ratio, not a 3×3 field-space one. In the quadrupole ansatz, the spatial Hessian at the origin is

$$\partial_x^2 \delta\big|_0 = \tfrac{2(a_2 - a_0)}{w^2},\qquad \partial_y^2 \delta\big|_0 = -\tfrac{2(a_0+a_2)}{w^2},\qquad \frac{\kappa_x}{\kappa_y} = \frac{a_0 - a_2}{a_0 + a_2}.$$

Solving `(a_0 - a_2)/(a_0 + a_2) = -1.304` gives `a_2/a_0 ≈ −7.58` (or `+7.58` under the reciprocal convention). That shape ratio is **not** determined by the gradient-flow critical conditions in this ansatz — it is left free once the pure-peak branch is chosen.

This tells us something specific: the number `-1.304` is not a critical-point of a reduced potential in any 3-parameter Gaussian-family ansatz. It is the shape of the nonlinear mean-field saddle of the full 2D PDE

$$M_0 \nabla^2 \delta \;=\; P_0 \delta \;+\; \tfrac{1}{6} P_3\, \delta^3 \;-\; \tfrac12 M_2 |\nabla\delta|^2 \;+\; (\text{non-gradient currents when } M_2 \neq 0),$$

with Scenario-D initial/boundary conditions. **That shape is only known numerically.**

---

## 10. What a genuine analytic derivation would require

Concretely, to promote `r* = -1.304` from numerical observation to closed form, one must:

1. **Fix the quasi-potential** at `M_2 ≠ 0` by solving the Hamilton–Jacobi equation in field space,
$$\tfrac{1}{2}\int\!dx\left(\frac{\delta\Psi}{\delta\delta(x)}\right)^{\!2} + \int\!dx\;\frac{\delta\Psi}{\delta\delta(x)}\,F[\delta](x) \;=\; 0,$$
   perturbatively in `M_2/M_0` around the gradient-flow Φ of §4. The leading correction is `O(M_2)` and shifts the critical motif by `O(M_2)`.

2. **Solve the 2D nonlinear saddle equation** (elliptic, with ray-tail boundary conditions set by `L_ray = 2`) for the Scenario-D motif `δ^*(x, y)`. No known closed-form solution. Numerical continuation from `M_2 = 0` is the most direct route.

3. **Fix the motif-filter conditioning** analytically: reduce the joint density `ρ[δ]` by the filter `(α, L_ray, δ)`, and compute the Hessian **on the conditional submanifold**. This is a constrained Hessian and will generically differ in eigenvalue structure from the unconstrained one.

4. **Extend the motif ansatz** past Gaussian+quadrupole to at least Hermite–Gauss `(a_0, a_2, a_{rr}, a_{ray})` (four modes including radial breathing and ray-tail). Only then does the true saddle appear as a critical point.

The analytically solid outputs produced by the present attempt are the three genuine invariants below. I am flagging them as **partial results**, not a derivation of `-1.304`:

- **Gradient-flow Φ** (closed form at `M_2 = 0`, §4).
- **Quartic perfect-square factorisation** `∫δ^4 = (πw^2/4)Q^2, Q = a_0^2 + 3a_2^2/16` (§4) — non-trivial and likely reusable.
- **Trace invariant** on the pure-peak branch: `T = λ_1 + λ_2 + λ_3 = -27πM_0/8`, coupling-independent (§7).
- **Large-ε median ratio:** `r^* → -5/27 ≈ -0.185`, universal on this branch (§7).

---

## Bottom line

A closed-form derivation of `r* = -1.304` from the Scenario-D structure as specified is **not achieved** by the Gaussian+quadrupole reduction, and the obstructions to pushing further are specific and structural (non-gradient `M_2` term; saddle vs. peak; filter conditioning; insufficient ansatz).

What *is* produced is:

$$\boxed{\;T = \sum_i \lambda_i = -\tfrac{27\pi M_0}{8}\,,\qquad r^*\bigl|_{\text{gradient peak, large }\varepsilon} = -\tfrac{5}{27}\approx -0.185\,.\;}$$

Neither matches `-1.304`. The honest reading is that `-1.304` is a **feature of the fully nonlinear 2D PDE saddle** under the Scenario-D filter, not a reduction-invariant of the Hessian at a symmetric critical motif.

---

## Next-step options (flagged for future sessions)

- **(a)** Push into the quasi-potential extension at leading `O(M_2)` — addresses obstruction #2.
- **(b)** Try the 4-mode Hermite–Gauss ansatz `(a_0, a_2, a_{rr}, a_{ray})` where a true saddle exists — addresses obstructions #1 and partially #3.
- **(c)** Numerical continuation from `M_2 = 0` gradient-flow saddles (once they exist in the extended ansatz) toward Scenario-D `n = 2.7` with motif-filter conditioning applied — the most direct route to `-1.304`.

## Related memos

- `memory/project_ed_rg_three_regime.md` — the RG arc that produced the intermediate-regime PDE used here.
- `theory/ED_RG_Flow_Analysis.md` — β-functions and fixed-point catalog; pure-peak critical point here lives on the nonlinear-mobility fixed line in the `M_2 = 0` limit.
- `theory/ED_IR_Effective_PDE.md` — Scenario-D closures in the IR-relevant regime.
- ED-Arch-01 (Scenario D parameter-sweep paper) — original numerical report of `κ_∥/κ_⊥ ≈ −1.3` at `(n = 2.7, σ = 0.0556)`.
- ED-SC 2.0 spec — motif filter `(α = 0.25, L_ray = 2, δ = 0.10)`, reference value `r* = −1.304`, falsification window `[−1.5, −1.1]`.
