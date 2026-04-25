# Emergent U(1) in ED's Underdamped Sector — Scoping Memo

**Date.** 2026-04-22.
**Scope.** One-afternoon feasibility scope. Structural audit, not a derivation. Does ED's P6 underdamped sector support a genuine U(1)-like structure from the `(δρ, δv)` phase-space geometry? Is the complex field `ψ = δρ + i·(…)·δv` a bona fide symmetry object or a coordinate trick?
**Verdict.** **Partial.** The linearised underdamped sector admits a well-defined complex field `ψ` and a global U(1) *is* a symmetry of solutions (trivially, by complex diagonalisation), but the associated norm `|ψ|²` is **not conserved** — it decays at rate `2γ = D + ζ`. The U(1) becomes a genuine conservation law only in the measure-zero reversible slice `D = 0, ζ = 0`. There is no local gauge structure. See §4–§8.

---

## 1. Problem Statement

### 1A. The precise question

In the P6 underdamped sector of ED (parameter region `(D − ζ)² < 4(1 − D)` at canon-default `τ = 1, P₀ = 1`), do linearised fluctuations `(δρ, δv)` around the homogeneous equilibrium `(ρ*, 0)` admit a complex reformulation `ψ = δρ + a·δv` such that:

- **(Q1)** The equations of motion are invariant under a global phase rotation `ψ → e^{iθ}ψ`?
- **(Q2)** A conserved Noether-like charge `Q[ψ]` exists under that rotation?
- **(Q3)** A spatially-varying phase `θ(x,t)` has gauge-like dynamical significance — i.e., `∇θ` enters other ED equations as a connection?

(Q1) is "global symmetry"; (Q2) is "conservation law"; (Q3) is "gauge structure." They are strictly ordered: Q1 is weakest, Q3 is strongest.

### 1B. What would count as a real U(1)

A **genuine U(1)** in a field theory requires at minimum:
- **(R1)** A *complex* field (or pair of real fields packaged into a complex) on which phase rotation acts.
- **(R2)** Equations of motion invariant under that rotation — both global and (for gauge) local.
- **(R3)** A conserved current `J^μ` via Noether, satisfying `∂_μ J^μ = 0`, giving a time-independent charge `Q = ∫ J⁰ d³x`.
- **(R4)** (Optional, for gauge) A vector potential `A_μ` that transforms inhomogeneously under local phase, and a field-strength tensor `F_{μν}`.

Anything meeting (R1)+(R2)+(R3) is a genuine *global* U(1). (R1)+(R2) without (R3) is a symmetry of solutions but not a symmetry principle — it produces no conservation law and therefore no charge. (R4) is needed to talk about electromagnetic coupling or gauge fields.

### 1C. Prior from the fine-structure memo

The `α`-scoping memo (`theory/Fine_Structure_Constant_Scoping.md`) flagged as a live subquestion whether the `(ρ, v)` phase-space structure supports an emergent phase. This memo addresses exactly that subquestion without any commitment to deriving `α` from it.

---

## 2. Linearised ED in the Underdamped Regime

### 2A. Setup

Canon (P1–P5) with linear-penalty near-equilibrium form (`PDE.md` §1):

$$
\partial_t \rho = D\bigl[M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho)\bigr] + H v, \qquad
\tau \partial_t v = F[\rho] - \zeta v.
$$

Expand `ρ = ρ* + δρ`, `v = δv` with `δρ, δv` small. At linear order:
- `P(ρ) ≈ P'(ρ*)·δρ ≡ P₀·δρ`
- `M(ρ) ≈ M(ρ*) ≡ M₀`
- `M'(ρ)|∇ρ|² = O(δρ²)` — drops.

Fourier-decompose `δρ(x,t) = Σ_k δρ_k(t) e^{ik·x}`, similarly for `δv`. The linearised system per mode `k`:

$$
\partial_t \delta\rho_k = -D\,\Omega^2(k)\,\delta\rho_k + H\,\delta v_k,
$$

$$
\tau\,\partial_t \delta v_k = -\Omega^2(k)\,\delta\rho_k - \zeta\,\delta v_k,
$$

where

$$
\Omega^2(k) \equiv M_0 k^2 + P_0.
$$

`Ω²(k) > 0` always (P3: `P₀ > 0`; P4: `M₀ > 0`).

### 2B. Natural units

Set `τ = P₀ = 1` throughout §§3–6; this is the canon-default dimensionless form. Restoring dimensions at the end is trivial. Define `Ω² ≡ Ω²(k) = 1 + M₀ k²`.

### 2C. Matrix form

$$
\partial_t \begin{pmatrix}\delta\rho_k \\ \delta v_k\end{pmatrix}
= A(k)\,\begin{pmatrix}\delta\rho_k \\ \delta v_k\end{pmatrix},
\qquad
A(k) = \begin{pmatrix} -D\,\Omega^2 & H \\ -\Omega^2 & -\zeta \end{pmatrix}.
$$

### 2D. Eigenvalues

Characteristic polynomial:

$$
\lambda^2 + (D\Omega^2 + \zeta)\lambda + \Omega^2(D\zeta + H) = 0.
$$

Discriminant: `(DΩ² + ζ)² − 4Ω²(Dζ + H) = (DΩ² − ζ)² − 4Ω²·H + 4DΩ²ζ − 4DΩ²ζ`

Cleaner:

$$
\Delta(k) = (D\Omega^2 + \zeta)^2 - 4\Omega^2(D\zeta + H).
$$

Underdamped iff `Δ(k) < 0`. At `k = 0` (`Ω² = 1`) this reduces to `(D + ζ)² − 4(Dζ + H) = (D − ζ)² − 4H`, so underdamped iff `(D − ζ)² < 4H = 4(1 − D)` — **matches Canon P6 exactly** ✓. At `k > 0` the underdamping condition shifts, but the sector exists on a non-empty parameter region.

### 2E. Eigenvalues in the underdamped regime

Write

$$
\lambda_\pm(k) = -\gamma(k) \pm i\,\omega(k),
$$

$$
\gamma(k) = \frac{D\Omega^2(k) + \zeta}{2}, \qquad
\omega(k) = \sqrt{\Omega^2(k)(D\zeta + H) - \gamma(k)^2}.
$$

At `k = 0`: `γ_0 = (D + ζ)/2`, `ω_0 = √(H − (D − ζ)²/4)`. Both real and positive in the underdamped sector.

---

## 3. Complex Field Construction

### 3A. Defining ψ such that ∂_t ψ = λ_+ ψ

Seek `ψ_k = δρ_k + a(k)·δv_k` with scalar `a(k)` such that `∂_t ψ_k = λ_+(k)·ψ_k`.

Direct computation:

$$
\partial_t \psi_k = (-D\Omega^2 - a)\,\delta\rho_k + (H - a\zeta)\,\delta v_k
\stackrel{!}{=} \lambda_+(\delta\rho_k + a\,\delta v_k).
$$

Matching real and imaginary coefficients gives the two conditions `−DΩ² − a = λ_+` and `H − aζ = aλ_+`. Both are satisfied (consistent with the characteristic equation) by

$$
\boxed{\;\; a(k) = -D\Omega^2(k) - \lambda_+(k) = \frac{\zeta - D\Omega^2(k)}{2} - i\,\omega(k). \;\;}
$$

So

$$
\boxed{\;\; \psi_k \equiv \delta\rho_k + \left[\frac{\zeta - D\Omega^2(k)}{2} - i\,\omega(k)\right]\delta v_k \;\;}
$$

evolves by

$$
\partial_t \psi_k = \bigl(-\gamma(k) + i\,\omega(k)\bigr)\,\psi_k.
$$

**This is well-defined wherever the sector is underdamped** (so that `ω(k) ∈ ℝ` and `a(k) ∈ ℂ \ ℝ`). It fails on the sector boundary (`ω → 0`: critical damping) and outside (overdamped: both eigenvalues real, complex ψ reduces to a real linear combination).

### 3B. Properties of a(k)

- `Re(a) = (ζ − DΩ²)/2`, `Im(a) = −ω(k)`.
- At `k = 0`: `a = (ζ − D)/2 − iω_0`.
- At the canon defaults `ζ = 1/4`, `D = D_crit ≈ 0.896`: `Re(a) ≈ (0.25 − 0.896)/2 = −0.323`; `Im(a) ≈ 0` (approaching the sector boundary).
- `a` is `k`-dependent — different modes have different complex structure.

### 3C. User's proposed form ψ = δρ + i·√(τ/D)·δv

The user's proposal `ψ = δρ + i·√(τ/D)·δv` has `a = i·√(τ/D)` — purely imaginary, independent of `k`, and with dimensionful scaling `√(τ/D)` matching `[δρ]/[δv]`. It is a reasonable natural-unit guess but **does not diagonalise the full linearised system**: the diagonalising `a(k)` has a non-zero real part `(ζ − DΩ²)/2` whenever `ζ ≠ D·Ω²`, which is the generic case.

For `D = ζ` (a measure-zero parameter choice) and `k = 0`, `Re(a) = 0` and `Im(a) = −ω_0 = −√(H − 0) = −√(1 − D)`. Then `ψ = δρ − i·√(1 − D)·δv`, of the same form as the user's guess with `√(1 − D)` in place of `√(τ/D)`. So the user's guess is the *right shape*; the coefficient is different and the general case needs the real part.

### 3D. Position-space ψ

`ψ(x, t) = Σ_k ψ_k(t)·e^{ik·x}`. Because `a(k)` depends on `k`, the position-space `ψ` is **not** expressible as `δρ(x,t) + a·δv(x,t)` for any single `a`. It is a *non-local* functional of `δρ, δv`:

$$
\psi(x,t) = \int K(x - x')\bigl[\delta\rho(x',t) + \text{stuff}\cdot\delta v(x',t)\bigr] dx'
$$

with a kernel `K` reflecting the `k`-dependence of `a(k)`. **This non-locality is the first red flag for a genuine local U(1) structure** (§6C).

---

## 4. U(1) Structure: Phase, Amplitude, Invariants

### 4A. Is the linearised system invariant under ψ → e^{iθ} ψ?

Per mode `k`: `∂_t ψ_k = λ_+(k)·ψ_k` is a linear complex first-order ODE. Any solution multiplied by a constant complex phase `e^{iθ}` remains a solution. **Global U(1) invariance holds trivially** in each Fourier mode.

This is (Q1) ✓ — but only in the weakest sense: it is the tautological phase freedom of any complex-diagonalised linear ODE. It does not distinguish ED from an undamped harmonic oscillator, a damped harmonic oscillator, or any 2D linear system with complex-conjugate eigenvalues.

### 4B. Amplitude evolution

$$
\frac{d}{dt}|\psi_k|^2 = 2\,\text{Re}(\lambda_+)\,|\psi_k|^2 = -2\gamma(k)\,|\psi_k|^2.
$$

So

$$
|\psi_k(t)|^2 = |\psi_k(0)|^2 \cdot e^{-2\gamma(k)\,t}.
$$

**The norm is not conserved.** It decays exponentially at rate `2γ(k) = DΩ²(k) + ζ`.

### 4C. Phase evolution

$$
\arg\psi_k(t) = \arg\psi_k(0) + \omega(k)\,t.
$$

Phase winds at rate `ω(k)` — the natural oscillation frequency of the mode. **Phase dynamics is trivial (linear in time) and set entirely by `ω(k)`.**

### 4D. Is there an invariant?

Combine: `|ψ_k|² · e^{2γ(k)t}` is conserved by construction. But this is just the initial norm — a trivial integral of motion with explicit time dependence. It is not a function of the field configuration alone.

**No genuine Noether charge exists unless `γ = 0`.** (§4E.)

### 4E. The γ = 0 slice

`γ(k) = 0` requires `DΩ²(k) + ζ = 0`. Since `D, ζ, Ω²(k) ≥ 0`, this forces `D = 0` **and** `ζ = 0`.

In this sub-sector:
- `D = 0`: pure mediated channel; diffusion is off.
- `ζ = 0`: no participation damping.
- `H = 1`: all dynamics via the participation loop.

Linearised system reduces to:

$$
\partial_t \delta\rho = \delta v, \qquad
\partial_t \delta v = -\Omega^2(k)\,\delta\rho.
$$

This is exactly a simple harmonic oscillator per mode (the undamped limit of P5). Combined: `∂_t^2 δρ = −Ω²(k)·δρ` — a massive Klein-Gordon equation with `mass² = P₀` and sound speed² `= M₀`. In this slice:

$$
\psi_k = \delta\rho_k - i\,\Omega(k)^{-1}\,\delta v_k \quad \text{(with convenient normalisation)},
$$

$$
\partial_t \psi_k = i\,\Omega(k)\,\psi_k, \qquad
|\psi_k|^2 = \text{const}.
$$

**Here U(1) is genuine.** The conserved quantity is the oscillator energy (per mode): `E_k ∝ |δv_k|² + Ω²(k)|δρ_k|²`. Noether charge = oscillator number (in the quantum case) or the classical action variable.

**This is the reversible ED sector, and it is a measure-zero slice of the (D, ζ) parameter space.** It is the same regime where `ED = wave equation + harmonic oscillator`, and the U(1) is the standard harmonic-oscillator phase.

---

## 5. Conserved Quantities and Currents

### 5A. Candidate "charge"

The norm `|ψ_k|²` is not conserved in the generic underdamped regime (§4B). In position space:

$$
\int |\psi(x,t)|^2 d^dx = \sum_k |\psi_k(t)|^2 = \sum_k |\psi_k(0)|^2 e^{-2\gamma(k)t},
$$

which decays and is mode-weighted by its own decay rate — not a useful conserved charge.

### 5B. Is there a continuity equation?

A continuity equation `∂_t ρ_U1 + ∇·J_U1 = 0` for some `ρ_U1[ψ], J_U1[ψ]` would establish local conservation. Try `ρ_U1 = |ψ|²`:

$$
\partial_t |\psi|^2 = 2\,\text{Re}(\psi^*\,\partial_t\psi).
$$

In position space this is messy (because `a(k)` is `k`-dependent — §3D), but roughly:

$$
\partial_t |\psi|^2 = -2\gamma_{\rm eff}\,|\psi|^2 + \nabla\cdot J_{\rm drift},
$$

where `γ_eff` is a positive operator encoding the `k`-dependent decay rates and `J_drift` is a redistribution current. **The decay term is a genuine sink — not a divergence of a current — so no continuity equation exists for `|ψ|²` in the generic sector.**

### 5C. Bateman-style doubled fields

A standard mathematical trick for damped oscillators: introduce an auxiliary "mirror" field `ψ̃` with amplified dynamics, such that the composite system `(ψ, ψ̃)` is conservative and admits a Lagrangian. This gives a conserved quantity `Re(ψ·ψ̃*)` or similar.

**This works mathematically but is a coordinate trick, not physics.** The mirror field has no ED interpretation. If it did (e.g., coupling to an additional ED sector), it would be new physics, not derivation from current axioms.

### 5D. Summary

- **Reversible slice (`D = 0, ζ = 0`):** genuine conserved Noether charge = oscillator action/energy. This is the mode-by-mode oscillator conservation in the undamped limit.
- **Generic underdamped sector (`γ > 0`):** no conserved charge; `|ψ|²` decays; Bateman doubling is available but adds unphysical structure.

---

## 6. Coupling and Gauge-Like Behavior

### 6A. Spatially-varying phase θ(x, t)

Consider an ansatz `ψ(x, t) = R(x, t)·e^{iθ(x, t)}`. Substitute into `∂_t ψ = (−γ + iω)ψ`. Separate real and imaginary:

$$
\partial_t R = -\gamma\,R, \qquad
\partial_t\theta = \omega.
$$

Both are **purely temporal**. The phase `θ(x,t)` has no spatial dynamics at linear order — it just winds at `ω` everywhere. `∇θ` is set by the initial condition and is not dynamically coupled to anything else.

**At finite k**, different modes wind at different `ω(k)`. A coherent wave packet spreads in phase as the modes dephase — but this is ordinary linear dispersion, not gauge dynamics.

### 6B. Does ∇θ appear as a "connection" in other ED equations?

In a gauge theory, `∇θ` acts as a connection via **minimal coupling**: `∇ → ∇ − iA` in some covariant derivative. For ED: the other linearised equation is for `δv`, but `δv` is already packaged into `ψ` — there is no *second* field that could "see" `∇θ`. ED at linearised order has **two real DOFs** `(δρ, δv)`, packaged as **one complex DOF** `ψ`. There is no additional charged sector to minimally couple to.

At nonlinear order (P7 triad term, higher-order `P(ρ)`), different modes of `ψ` couple to each other via `M'(ρ)|∇ρ|²` and `P''(ρ*)·δρ²`. Do those coupling terms acquire a `∇θ`-dependence that could be interpreted as a connection?

Check: the leading nonlinear term is `M'(ρ*)|∇(δρ)|²`. In terms of `ψ`: `δρ = Re(ψ) − (Re(a)/ω)·Im(ψ) + …` (see §3). `∇(δρ)` contains both `∇|ψ|` and `|ψ|·∇θ` through `Im(ψ) = −ω·δv` giving `δv = −Im(ψ)/ω`. So `|∇δρ|²` contains cross-terms mixing `∇|ψ|` and `|ψ|∇θ`. This is a specific nonlinear coupling of amplitude and phase gradients.

**Is this gauge-like?** Not in the standard sense. In gauge theory, the connection `A_μ` is an *independent* field that transforms inhomogeneously under local phase rotation. Here `∇θ` is just the gradient of `ψ`'s own phase — it is not an independent DOF. There is no field strength `F = dA`, no Bianchi identity, no gauge redundancy.

**This is not a gauge symmetry.** It is a nonlinear-field-theory statement that amplitude and phase gradients mix at nonlinear order — which is true in any complex nonlinear scalar field theory (e.g., Gross-Pitaevskii).

### 6C. Local vs global

The global U(1) `ψ → e^{iθ_0}ψ` (constant `θ_0`) is a symmetry of the linearised equations (§4A).

The local U(1) `ψ(x,t) → e^{iθ(x,t)}ψ(x,t)` is **not** a symmetry. Under a local phase rotation, `∂_t ψ → e^{iθ}(∂_t ψ + i(∂_t θ)ψ)`, so `∂_t ψ = λψ` becomes `∂_t ψ = λψ − i(∂_t θ)ψ`, which is not of the same form unless `∂_t θ = 0`.

A gauge theory would compensate by introducing a gauge field `A_0` that transforms as `A_0 → A_0 + ∂_t θ`, making `(∂_t − iA_0)ψ` covariant. ED has no such field. **Local U(1) therefore fails by the most direct route: there is no gauge field to absorb the transformation, and none emerges from the existing axioms.**

### 6D. What would be needed for a genuine gauge structure

To promote (Q1) and approximate-(Q2) to genuine gauge (Q3):
- **Add a vector field `A_μ`** with dynamics `∂_μ F^{μν} ∝ J^ν`.
- **Gauge-transformation law.** `A_μ → A_μ + ∂_μ θ` under local U(1).
- **Field-strength tensor.** `F_{μν} = ∂_μ A_ν − ∂_ν A_μ`.
- **Gauge-invariant action.** Rewrite ED's linearised Lagrangian (if it has one — see §4 of `ED_Geometry_Emergence_Scoping.md`) using `(∂_μ − iA_μ)ψ`.

None of these is in ED. All are axiomatic additions, not consequences.

---

## 7. Structural Obstacles and Limitations

| # | Obstacle | Severity |
|---|---|---|
| O1 | `\|ψ\|²` is not conserved in the generic underdamped regime (decays at rate `2γ`). | **Fatal for (Q2)** — no Noether charge outside the reversible slice. |
| O2 | Diagonalising `a(k)` is `k`-dependent → position-space `ψ` is a non-local functional of `(δρ, δv)`. | **Fatal for (Q3) locality** — there is no local `ψ(x,t)` field in position space, only a non-local packaging. |
| O3 | The global U(1) invariance of (Q1) is the tautological complex diagonalisation of a linear ODE. It does not distinguish ED from any 2D damped oscillator. | **Informative** — (Q1) alone is not content. |
| O4 | No additional charged sector to minimally couple to `ψ`; the two real DOFs are exhausted by `ψ`. | **Fatal for (Q3)** — no matter field to gauge. |
| O5 | Local U(1) is broken by dissipation term (§6C); no compensating gauge field in Canon. | **Fatal for (Q3)** — would require new axioms (vector potential). |
| O6 | No field-strength tensor, no gauge-invariant action, no Bianchi identity. | **Fatal for (Q3)** — all absent. |
| O7 | Genuine U(1) with conservation holds only on the measure-zero slice `D = 0, ζ = 0` (reversible limit). | **Informative** — the "good" sector is a boundary of parameter space, not an open region. |
| O8 | Nonlinear coupling of amplitude and phase gradients (§6B) is *not* gauge-like; it is the ordinary mixing of nonlinear complex scalar theories. | **Clarifying** — don't confuse with gauge structure. |

**Summary.** (Q1) holds, as a tautology. (Q2) fails outside the reversible slice. (Q3) fails by multiple independent routes. The "emergent U(1)" is not a genuine gauge symmetry of ED; it is the complex diagonalisation of a 2D linear system, trivially dressed.

---

## 8. Assessment and Next Steps

### 8A. Verdict

**The ψ-phase is a useful parametrisation of the linearised underdamped sector but not a genuine U(1) symmetry of ED.** More precisely:

- **(Global, tautological).** `∂_t ψ_k = λ_+(k)·ψ_k` admits the trivial global phase rotation `ψ_k → e^{iθ}ψ_k`. Every linear ODE with complex eigenvalues has this. It is (Q1) ✓ but empty of content.
- **(Conservation, only in reversible slice).** `|ψ_k|²` is conserved only when `D = 0, ζ = 0` (measure zero). In the generic underdamped sector, `|ψ|²` decays. (Q2) ✗ except on a parameter boundary.
- **(Gauge, absent).** No local gauge symmetry, no connection, no field strength, no charged sector to couple. (Q3) ✗.

This is a **"useful packaging"** result, not a **"genuine symmetry"** result. The distinction matters because it determines whether ED has any native charge-like quantum number, and the answer is: **no**, outside the reversible sub-sector where the conservation is inherited from the harmonic-oscillator structure rather than from anything specifically ED.

### 8B. The honest version of the structural claim

> **ED-10 / ED-Quantum (honest form).** "In the linearised underdamped sector, ED admits a complex parametrisation `ψ_k(t)` per Fourier mode that diagonalises the 2×2 linear dynamics of `(δρ, δv)`. The dynamics are invariant under global phase rotation of `ψ_k`, but the associated norm is dissipated rather than conserved, so no global U(1) Noether charge exists in the generic sector. A genuine conserved U(1) emerges only in the measure-zero purely-reversible slice `D = 0, ζ = 0`, where it is the standard conservation law of an undamped harmonic oscillator. ED has no local gauge structure, no vector potential, no field strength, and no charged matter sector to couple to. Schrödinger-like evolution of ψ in the reversible slice is consistent with ED-10's 'Schrödinger = thin-regime participation' identification, but does not constitute a gauge theory."

### 8C. What this does and doesn't advance

**Advances:**
- Provides a **clean complex formulation** of the P6 linearised dynamics, which is useful for spectral analysis, signal propagation, and further theoretical work in the reversible sector.
- Clarifies that ED's **reversible-limit sector** (where `D + ζ → 0`) is exactly a collection of harmonic oscillators with conserved action per mode — the canonical starting point for quantisation.
- Rules out the "charge emerges from `(ρ, v)` phase space" route to `α` (already reached by `theory/Fine_Structure_Constant_Scoping.md` via a different path; reinforced here).

**Does not advance:**
- The `α` derivation question (the coupling that `ψ` has is not a gauge coupling, and its value is set by parameters not an axiom).
- Local gauge structure in ED.
- A mechanism for charge, spin, or any internal quantum number.

### 8D. Concrete follow-ups (if pursued)

**Follow-up 1 — Canonical quantisation of the reversible slice (small).** In the `D = 0, ζ = 0` sector, ED linearises to a massive Klein-Gordon field with mass² = `P₀` and sound speed² = `M₀`. Standard canonical quantisation gives a Fock space with particle-number conservation (the U(1) is exactly the `U(1)_{\rm number}` of a scalar QFT). Memo: 1–2 weeks. Outcome: explicit form of ED's reversible-sector QFT, which then connects to ED-10's Schrödinger identification.

**Follow-up 2 — Bateman doubling as physical ansatz (speculative).** Introduce a conjugate ED sector `ρ̃` with time-reversed dynamics so that the composite `(ρ, ρ̃)` has conserved norm. Check whether there is any ED interpretation (e.g., dual field, mirror sector, horizon-crossing mode). High risk of being just a formal trick.

**Follow-up 3 — Nonlinear coupling of amplitude and phase (small).** Compute the leading-order nonlinear coupling between `|ψ|` and `∇θ` from the P7 term `M'(ρ)|∇ρ|²` explicitly. Not gauge-like, but may reveal interesting mode-coupling structure. Memo: ~1 week. Outcome: spectral map of the P7 triad term in the complex-variable formulation.

**Not recommended:** Attempting to derive a "charge" or "gauge field" from the `ψ`-phase. The structural obstacles in §7 make this a non-starter without adding axioms.

### 8E. Language for public-facing materials

- **Say:** "In ED's reversible sector, linearised fluctuations form a conservative harmonic-oscillator dynamics with a natural complex parametrisation. This is where ED's connection to Schrödinger-like evolution (ED-10) lives."
- **Say:** "Outside the reversible limit, dissipation breaks the conservation; the complex variable remains a useful analytical tool but is not a symmetry principle."
- **Do not say:** "ED has an emergent U(1) gauge symmetry." It doesn't. The structure is global and non-gauge, and even the global symmetry is broken by dissipation.

---

## 9. Related Memos

- `theory/Architectural_Canon.md` — Canon P1–P7, especially P5 (participation feedback) and P6 (damping discriminant).
- `theory/PDE.md` — canonical PDE and primitives, §1–§3.
- `theory/Fine_Structure_Constant_Scoping.md` — prior scoping memo; this memo is the follow-up on the `(ρ, v)` phase-space subquestion.
- `theory/ED_Geometry_Emergence_Scoping.md` — prior scoping memo; flagged emergent-Lorentz and related structural issues relevant to any gauge-theory embedding.
- `theory/Species_Mass_Spectrum_Scoping.md` — related structural-audit format.

---

**Status.** Scoping only. No new axioms, no new predictions, no updates to Canon. Headline: ED's underdamped sector admits a convenient complex reformulation; the associated U(1) is a tautology of complex diagonalisation, not a symmetry principle. Genuine conservation exists only in the measure-zero reversible slice. Recommend preserving the complex-field formulation as an analytical tool while honestly flagging that it does not constitute a gauge structure.
