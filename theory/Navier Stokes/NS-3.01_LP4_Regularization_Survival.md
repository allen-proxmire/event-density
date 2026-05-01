# NS-3.01 — ℓ_P² ∇⁴ v Regularization Survival Analysis (Route R1)

**Date:** 2026-04-30
**Status:** R1 audit complete. **Headline: structurally promising but conditional. ED's V1 finite-width vacuum kernel produces a stabilizing $-\kappa \mu \ell_P^2 \nabla^4 \mathbf{v}$ contribution to the momentum equation with κ > 0 form-FORCED by V1 being a positive smoothing kernel; magnitude INHERITED via Theorem N1's G-function specific form. However, the standard kinetic-theory Chapman-Enskog expansion *also* produces ∇⁴ v terms (Burnett-class) with notoriously destabilizing signs (Bobylev instability). Whether ED's stabilizing contribution dominates the standard destabilizing Burnett contributions is INHERITED on both sides and not derivable from primitives alone. R1 partially closes form-FORCED but value-conditional.**
**Sources:** [`NS-2.05_Stress_Tensor.md`](NS-2.05_Stress_Tensor.md), [`NS-2.07_Synthesis.md`](NS-2.07_Synthesis.md), [`Future_Arc_Diffusion_Coarse_Graining_Scoping.md`](Future_Arc_Diffusion_Coarse_Graining_Scoping.md), [`arcs/arc-N/non_markov_forced.md`](../../arcs/arc-N/non_markov_forced.md) (V1 form-class), T18 + T19 (V1 retardation + ℓ_ED = ℓ_P).

---

## 1. Purpose

NS-3.01 evaluates whether ED's substrate cutoff at ℓ_P produces a higher-derivative regularization term in the continuum NS momentum equation:

$$\rho \frac{D\mathbf{v}}{Dt} = -\nabla p + \mu \nabla^2 \mathbf{v} \;-\; \kappa \, \mu \, \ell_P^2 \, \nabla^4 \mathbf{v} \;+\; \rho \mathbf{f}^\mathrm{ext} \;+\; (\mathrm{other\ corrections}),$$

with κ > 0 (stabilizing).

This is the most promising of the three NS-3 routes for achieving Path C+. The mechanism is direct: V1's finite-width retarded kernel on ℓ_ED = ℓ_P acts as a low-pass filter at substrate scale; expanded in gradients, it produces a stabilizing ℓ_P² correction to the standard Navier-Stokes viscous term. If non-trivial, this is the structural mechanism by which ED's substrate cutoff prevents finite-time blow-up at substrate scale.

---

## 2. Inputs from NS-2

| Input | Source |
|---|---|
| ℓ_P² ∇⁴ v candidate term identified (flagged but not derived) | NS-2.05 §7.3, NS-2.07 §4.2 |
| Coarse-graining cell geometry (spherical, R_cg in (C1)∩(C2)∩(C3) window) | NS-2.01 §2 |
| Flux expansion structure (advective + non-advective decomposition) | NS-2.02 §3 |
| Stress-tensor decomposition $\tau_{ij} = p_\mathrm{eff}\delta_{ij} + \sigma_{ij}^\mathrm{visc} + \tau_{ij}^\mathrm{ED-spec}$ | NS-2.05 §7 |
| V1 retarded kernel form: $K_\mathrm{vac}^\mathrm{ret} = \theta(t-t') \cdot G(\sigma/\ell_\mathrm{ED}^2)$, finite-width Lorentz-scalar, sub-power-law-2 decaying | T18 derivation + Theorem N1 (arc-N N.2) |
| ℓ_ED = ℓ_P forced by Newton-recovery | T19 |
| V1 G-function specific form INHERITED | arc-N N.4 |
| Form-FORCED / value-INHERITED hierarchy | NS-2.07 §5 |

---

## 3. Multi-Scale Expansion Setup

### 3.1 Expansion parameter

Define the small parameter:

$$\varepsilon = \frac{\ell_P}{L_\mathrm{flow}},$$

where $L_\mathrm{flow}$ is the smallest characteristic gradient length scale of the flow at any given time.

In the standard NS regime, $\varepsilon \le 10^{-30}$ (laboratory NS) — vanishingly small. Higher-derivative corrections at order ε² are numerically negligible.

In a putative finite-time blow-up scenario, gradients diverge: $L_\mathrm{flow}(t) \to 0$ as $t \to t_*$. At the moment when $L_\mathrm{flow}(t)$ approaches ℓ_P, ε approaches order unity, and higher-derivative corrections become dominant. **This is the regime where R1's regularization activates**, if the term exists.

### 3.2 Multi-scale stress-tensor expansion

Expand the stress tensor in powers of ε:

$$\tau_{ij}(x, t) = \tau_{ij}^{(0)}(x, t) + \varepsilon^2 \, \tau_{ij}^{(2)}(x, t) + \varepsilon^4 \, \tau_{ij}^{(4)}(x, t) + \cdots.$$

Identifications by order:

- $\tau_{ij}^{(0)}$: pressure + standard Newtonian viscous (the leading NS form derived in NS-2.05). Contains $p_\mathrm{eff} \delta_{ij}$ and $\sigma_{ij}^\mathrm{visc}$ at $\nabla v$ order.
- $\tau_{ij}^{(2)}$: contains terms at $\nabla^2 v$ order multiplied by ε² ~ ℓ_P². When inserted into $\partial_j \tau_{ij}$ in the momentum equation, generates terms at $\nabla^3 v$ — the **Burnett-class corrections**.
- $\tau_{ij}^{(4)}$: contains terms at $\nabla^3 v$ order multiplied by ε⁴ ~ ℓ_P⁴. When inserted, generates $\nabla^5 v$ — super-super-Burnett.

The ∇⁴ v term in the momentum equation comes from $\partial_j \tau_{ij}^{(2)}$ when $\tau_{ij}^{(2)}$ contains $\nabla^3 v$ structure. Specifically: any term $\ell_P^2 \nabla^2 (\partial_i v_j + \partial_j v_i)$ in $\tau_{ij}^{(2)}$ produces $\ell_P^2 \nabla^4 v_i$ in the momentum equation under incompressibility.

### 3.3 Order tracking

Standard kinetic-theory Chapman-Enskog expansion produces *all* even-order Burnett-class terms ($\tau_{ij}^{(2)}$, $\tau_{ij}^{(4)}$, ...). ED's contribution is whether V1's substrate-cutoff structure modifies these terms (or adds new ones) with a sign and magnitude distinct from standard kinetic theory.

---

## 4. Derivation of Higher-Derivative Terms

### 4.1 V1 finite-width as a low-pass filter

Theorem N1 (arc-N N.2) establishes V1 as a finite-width Lorentz-scalar function $G(\sigma/\ell_\mathrm{ED}^2)$ with sub-power-law-2 decay. The Fourier transform of any such positive finite-width kernel has the structure:

$$\hat{K}(k) = K_0 \left[1 - \alpha (k \ell_P)^2 + \beta (k \ell_P)^4 - \cdots\right] \quad \text{for}\ k \ell_P \ll 1,$$

with $\alpha > 0$, $\beta > 0$ for any *positive* smoothing kernel (general fact about positive monotonically-decreasing-in-|k| kernels). Specific values of α, β are INHERITED via G's specific functional form (per arc-N N.4: G's form is INHERITED).

### 4.2 V1-mediated stress tensor at higher order

The V1-mediated cross-chain participation-overlap stress contribution is V1's kernel acting on the cell-level chain-pair velocity-gradient structure:

$$\tau_{ij}^\mathrm{V1-mediated}(x, t) = K_\mathrm{V1} * S_{ij}(x, t),$$

where $S_{ij} = (\partial_i v_j + \partial_j v_i)/2$ is the symmetric strain rate and $*$ is convolution in space. Expanding the kernel in Fourier space using §4.1:

$$\widehat{\tau_{ij}^\mathrm{V1-mediated}}(k) = \hat{K}_\mathrm{V1}(k) \, \hat{S}_{ij}(k) \;=\; K_0 \left[1 - \alpha (k\ell_P)^2 + \cdots\right] \, \hat{S}_{ij}(k).$$

In real space:

$$\tau_{ij}^\mathrm{V1-mediated}(x, t) \;=\; K_0 \, S_{ij}(x, t) \;+\; \alpha \, K_0 \, \ell_P^2 \, \nabla^2 S_{ij}(x, t) \;+\; O(\ell_P^4).$$

The leading $K_0 S_{ij}$ term contributes (with appropriate sign) to the standard Newtonian deviatoric form already in NS-2.05's $\sigma_{ij}^\mathrm{visc}$ at order ε⁰.

The subleading $\alpha K_0 \ell_P^2 \nabla^2 S_{ij}$ term is the **higher-derivative correction at order ε²**. This is $\tau_{ij}^{(2)}$ from §3.2.

### 4.3 The ∇⁴ v term in the momentum equation

Insert $\tau_{ij}^{(2)} = \alpha K_0 \ell_P^2 \nabla^2 S_{ij}$ into $-\partial_j \tau_{ij}$ in the momentum equation:

$$-\partial_j \tau_{ij}^{(2)} = -\alpha K_0 \ell_P^2 \, \partial_j \nabla^2 S_{ij} = -\alpha K_0 \ell_P^2 \, \nabla^2 \partial_j S_{ij}.$$

Using incompressibility $\partial_j v_j = 0$ and the strain definition $\partial_j S_{ij} = (1/2)(\nabla^2 v_i + \partial_i \partial_j v_j) = (1/2) \nabla^2 v_i$:

$$-\partial_j \tau_{ij}^{(2)} = -\frac{\alpha K_0 \ell_P^2}{2} \, \nabla^2 (\nabla^2 v_i) = -\frac{\alpha K_0 \ell_P^2}{2} \, \nabla^4 v_i.$$

Identifying $K_0 = 2\mu_\mathrm{V1}$ (the V1 contribution to total viscosity, per the standard relation between strain-rate kernel coefficient and viscosity), and writing $\kappa \equiv \alpha$ for clarity:

$$\boxed{-\partial_j \tau_{ij}^{(2)} = -\kappa \, \mu_\mathrm{V1} \, \ell_P^2 \, \nabla^4 v_i.}$$

The momentum equation acquires:

$$\rho \frac{D v_i}{Dt} = -\partial_i p_\mathrm{eff} + \mu_\mathrm{total} \nabla^2 v_i - \kappa \, \mu_\mathrm{V1} \, \ell_P^2 \, \nabla^4 v_i + \rho f_i^\mathrm{ext} + (\mathrm{other\ corrections}),$$

with κ > 0 (per §4.1's positivity for smoothing kernels).

### 4.4 What is form-FORCED, what is INHERITED

| Step | Status |
|---|---|
| V1 kernel finite-width on ℓ_P | **FORCED** (Theorem N1 + T19 ℓ_ED = ℓ_P) |
| V1 kernel positivity → α > 0 sign of leading higher-derivative correction | **FORCED** (positive smoothing kernels have positive Fourier-space curvature in k) |
| Existence of $-\kappa \mu_\mathrm{V1} \ell_P^2 \nabla^4 v$ term in momentum equation | **FORCED** (appears at order ε² of the V1-mediated stress expansion) |
| $\kappa = \alpha$ specific value | **INHERITED** (depends on G's specific functional form per arc-N N.4) |
| $\mu_\mathrm{V1}$ coefficient | INHERITED (V1 contribution to viscosity per NS-2.05 §7.2) |

**Net form-FORCED finding:** ED's substrate produces a $-\kappa \mu_\mathrm{V1} \ell_P^2 \nabla^4 v_i$ term in the continuum NS momentum equation with κ > 0 (stabilizing). This is the structural existence of a regularization mechanism.

**Inherited content:** the coefficient $\kappa \mu_\mathrm{V1}$ has INHERITED magnitude. The qualitative existence is FORCED; the quantitative magnitude is INHERITED.

---

## 5. Continuum-Limit Survival Test

### 5.1 ℓ_P does not vanish in the continuum limit

ℓ_P is a *fixed substrate constant* per Q.8 / T19. The substrate→continuum coarse-graining limit is $R_\mathrm{cg} / L_\mathrm{flow} \to 0$ with ℓ_P held fixed. The ℓ_P² coefficient of the ∇⁴ v term is therefore *fixed* in the continuum limit; it does not vanish.

What *does* happen in the limit: at scales $L_\mathrm{flow} \gg \ell_P$, the term is suppressed by ratio $\ell_P^2 / L_\mathrm{flow}^2 \le 10^{-60}$ (for laboratory NS). The term *exists* at the form level but is *numerically negligible* at NS scales.

This is exactly the desired behavior for a regularization term: it is structurally present at the form level, ignorable at standard NS scales, and dominant at scales approaching ℓ_P.

### 5.2 Activation regime

The term becomes dominant when:

$$\kappa \mu_\mathrm{V1} \ell_P^2 \, k^4 \;\gtrsim\; \mu_\mathrm{total} \, k^2,$$

equivalently:

$$k \;\gtrsim\; \sqrt{\frac{\mu_\mathrm{total}}{\kappa \mu_\mathrm{V1}}} \, \frac{1}{\ell_P} \;\sim\; \frac{1}{\ell_P}$$

(with the kinematic prefactor of order unity since $\mu_\mathrm{total} \approx \mu_\mathrm{kin} + \mu_\mathrm{V5}$ with $\mu_\mathrm{V1}$ a small contribution per NS-2.05 §7.2 + Arc D scoping §4.2; the prefactor magnitude is INHERITED).

The activation scale is essentially $1/\ell_P$ — the substrate scale. In a finite-time blow-up scenario, gradients reach this scale, the regularization activates, and high-frequency modes are suppressed.

### 5.3 Survival verdict

**The term survives the continuum limit.** Coefficient is fixed at $\kappa \mu_\mathrm{V1} \ell_P^2$; sign is FORCED positive (stabilizing); existence is FORCED via V1 finite-width form.

**Caveat: not the only ∇⁴ v term in the equation.** See §6.2 below.

---

## 6. Magnitude and Physical Interpretation

### 6.1 Order-of-magnitude estimate

$\kappa \mu_\mathrm{V1} \ell_P^2 \nabla^4 v_i$ at NS scales:

- $\kappa \sim O(1)$ (specific value INHERITED).
- $\mu_\mathrm{V1}$ small contribution to total viscosity per NS-2.05 §7.2 + Arc D scoping §4.2; estimated $\mu_\mathrm{V1} \sim \rho c \ell_P$ from substrate constants. For water at standard density, $\mu_\mathrm{V1} \sim 10^3 \cdot 3 \times 10^8 \cdot 10^{-35} \approx 3 \times 10^{-24}$ Pa·s. Compare to actual water viscosity $\mu_\mathrm{water} \approx 10^{-3}$ Pa·s. **Ratio $\mu_\mathrm{V1}/\mu_\mathrm{water} \sim 10^{-21}$.**
- $\ell_P^2 \nabla^4 v$: at laboratory scale $L_\mathrm{flow} \sim 10^{-3}$ m, the ratio $\ell_P^2 / L^2 \sim 10^{-64}$.

Total magnitude relative to leading viscous term: $\sim 10^{-21} \cdot 10^{-64} = 10^{-85}$. **Vanishingly negligible at NS scales.**

In activation regime ($L_\mathrm{flow} \to \ell_P$): the term dominates, and the regularization is decisive.

### 6.2 Honest concern: standard Burnett-class ∇⁴ v terms

Standard kinetic-theory Chapman-Enskog expansion *also* produces ∇⁴ v terms in the momentum equation, at the **super-Burnett** (third-order) level. These come from the binary-collision integral expansion at higher order; they appear independently of any substrate cutoff. The notable fact: standard super-Burnett ∇⁴ v terms are well-known to have **destabilizing signs** that lead to short-wavelength instability (Bobylev's instability, originally for the BGK kinetic equation; generalizes to standard Boltzmann-derived hydrodynamics).

Schematically:

$$\mathrm{standard\ super\text{-}Burnett:}\quad +\kappa_\mathrm{Burnett} \, \mu \, \lambda_\mathrm{mfp}^2 \, \nabla^4 v_i,$$

with $\kappa_\mathrm{Burnett}$ of order unity, sign positive (destabilizing). The relevant length scale is $\lambda_\mathrm{mfp}$ (mean free path), not ℓ_P. For typical fluids, $\lambda_\mathrm{mfp}$ is enormously larger than ℓ_P:

- STP gas: $\lambda_\mathrm{mfp} \sim 10^{-7}$ m → $\lambda_\mathrm{mfp}^2 / \ell_P^2 \sim 10^{56}$.
- Water: $\lambda_\mathrm{mfp} \sim 10^{-10}$ m → $\lambda_\mathrm{mfp}^2 / \ell_P^2 \sim 10^{50}$.

**The standard Burnett ∇⁴ v term is overwhelmingly larger than ED's V1 contribution by ratio ~ $\lambda_\mathrm{mfp}^2 / \ell_P^2 \sim 10^{50}$ or more.** ED's stabilizing contribution at substrate scale is structurally present but quantitatively dominated by the standard destabilizing Burnett contribution at mean-free-path scale.

### 6.3 Sign and magnitude verdict

- **ED's V1 contribution: stabilizing (sign FORCED), tiny (magnitude INHERITED, scale ℓ_P²).**
- **Standard kinetic-theory Burnett contribution: destabilizing (sign known from kinetic theory), much larger (scale $\lambda_\mathrm{mfp}^2$).**

Naive sum: the standard destabilizing Burnett dominates at any standard fluid regime. ED's stabilizing contribution is irrelevant at any scale where Burnett is operative.

**Resolution at substrate scale:** at gradient scales approaching ℓ_P, the standard Burnett analysis breaks down (it assumes $\lambda_\mathrm{mfp} \ll L$, i.e., Knudsen number small; near substrate scale this assumption fails). ED's analysis takes over: the V1 finite-width kernel directly governs the substrate-scale physics, and its stabilizing contribution is what physical NS would actually exhibit at substrate scale, regardless of what an extrapolation of Burnett-class analysis suggests.

This is a structural argument: standard kinetic theory's destabilizing Burnett term is a *long-wavelength expansion* artifact extrapolated to short wavelengths where the expansion fails. ED's V1 stabilizing term is a *substrate-scale* result derived directly from the substrate kernel structure, valid where Burnett-class analysis breaks down.

**Honest verdict on the competition:**

- For standard NS scales ($L_\mathrm{flow} \gg \lambda_\mathrm{mfp}$), Burnett expansion converges and the destabilizing Burnett term is suppressed by Knudsen smallness. Both standard Burnett and ED V1 are negligible at NS scales.
- For intermediate scales ($\ell_P \ll L \lesssim \lambda_\mathrm{mfp}$), Burnett expansion may not converge cleanly; both contributions are formally relevant, with the standard destabilizing Burnett term *as currently formulated in continuum-fluid theory* dominating in magnitude.
- For scales approaching $\ell_P$, Burnett expansion fails, ED's V1 substrate-derived term is the physically correct description, and it is stabilizing.

**Implication for blow-up prevention:** in a putative finite-time blow-up, gradients pass through all three regimes en route to divergence. The destabilizing Burnett regime might *accelerate* blow-up at intermediate scales, while ED's V1 stabilizing regime would prevent blow-up at substrate scale. Whether the trajectory through scales is dominated by one or the other depends on the specific blow-up scenario.

This is a legitimate Path C+ candidate — ED's V1 *does* produce a stabilizing mechanism at substrate scale — but it is not as clean a Path C+ as the simple "ED has a stabilizing ∇⁴ v term and Clay is solved" framing would suggest.

---

## 7. Preliminary Verdict for R1

**R1 partially closes form-FORCED, value-conditional.**

### 7.1 What is delivered

- ED's substrate produces a $-\kappa \mu_\mathrm{V1} \ell_P^2 \nabla^4 v_i$ term in the continuum NS momentum equation. Existence is FORCED via V1 finite-width form (Theorem N1) + Newton-recovery (T19) + multi-scale expansion (this memo §4).
- The sign is FORCED positive (stabilizing) by V1 being a positive smoothing kernel.
- The magnitude is INHERITED via Theorem N1's G-function specific form (per arc-N N.4) and via $\mu_\mathrm{V1}$'s INHERITED status.
- The term survives the substrate→continuum limit as a fixed-coefficient term; it is numerically negligible at NS scales but dominant at substrate scales.

### 7.2 What is not delivered

- A clean Path C+ resolution of the Clay smoothness question. The standard kinetic-theory Burnett-class ∇⁴ v term is *destabilizing* and quantitatively dominates ED's stabilizing V1 contribution at all scales where Burnett expansion applies.
- A rigorous statement that ED's regularization, taken in isolation, prevents finite-time blow-up. The trajectory through scales (NS regime → intermediate → substrate) involves multiple kinetic regimes; whether ED's substrate-scale stabilization wins out over intermediate-scale destabilization depends on blow-up scenario specifics not derivable from primitives.

### 7.3 R1 verdict character

**Form-FORCED-conditional Path C+ candidate.** ED produces a structurally identifiable stabilizing mechanism at substrate scale that is *not present in standard kinetic-theory NS*. This is structurally significant. It does not, however, deliver a rigorous Path C+ resolution of Clay-NS in the strong sense ("ED's substrate cutoff prevents blow-up"). It delivers the weaker statement: **ED's substrate framework contains a stabilizing higher-derivative regularization at substrate scale; whether this regularization is sufficient to prevent finite-time blow-up depends on quantitative competition with standard destabilizing Burnett-class terms whose magnitudes are INHERITED on both sides.**

This is the honest verdict. It is structurally valuable (a real ED-specific Clay-relevant mechanism is identified) but it is weaker than a clean Path C+ closure.

### 7.4 Implication for the NS-3 program

R1 is the most likely productive route, and it has produced a partial result. R2 (holographic global bound) and R3 (V5/V1 transport bound) remain to be audited. If either of those produces a *cleaner* Path C+ candidate (e.g., a global bound that constrains gradient distribution unconditionally), the aggregate NS-3 verdict could be Path C+. If both R2 and R3 fail or partial-close, the aggregate is **partial-Path-C+** — ED structurally identifies a regularization mechanism that is conditional rather than rigorous.

The honest a-priori from NS-3 scoping (30% C+ / 50% C− / 20% intermediate) is updated by R1's outcome: R1 partial-closing pushes the aggregate toward intermediate. Updated rough prior: **20% Path C+ (R2 or R3 closes cleanly) / 30% Path C− (R2 and R3 fail, R1's partial closure is empirically vacuous) / 50% intermediate (partial-Path-C+ with conditional regularization)**.

---

## 8. Recommended Next Steps

In priority order. R1 partial closure shifts the NS-3 outcome distribution toward intermediate; R2 and R3 are now the load-bearing audits for whether NS-3 lands at clean Path C+ or at intermediate.

1. **Draft NS-3.02 — Holographic Global-Bound Audit.** File: `theory/Navier Stokes/NS-3.02_Holographic_Global_Bound.md`. Audit T19's holographic participation-count bound for translation to continuum gradient distribution bound. Three sub-tasks: (a) explicit chain of identifications from substrate area-scaling to continuum gradient bound; (b) compare the resulting bound to standard Leray energy bound — is it stronger, weaker, or equivalent; (c) verdict on whether the bound is sufficient to rule out blow-up via Beale-Kato-Majda-class criteria. **Stall risk high** — the chain may produce only the standard energy bound, which is insufficient. But if R2 closes cleanly, the aggregate NS-3 is clean Path C+.

2. **Draft NS-3.03 — V5/V1 Transport-Bound Audit.** File: `theory/Navier Stokes/NS-3.03_V5_V1_Transport_Bound.md`. Audit V5/V1 substrate-level rate bounds for translation to continuum strain-rate bound. Two sub-tasks: (a) propagate substrate-level maximum rate to continuum (likely vacuous at NS scales since c/ℓ_P ~ 10⁴³ s⁻¹); (b) audit whether V5's INHERITED amplitude can be bounded above by *any* substrate-level argument (form-derivable bound rather than value-pinned bound). **Stall risk high** — likely produces formal bound that is empirically vacuous, but worth running honestly.

3. **Carry forward NS-3.01's R1 partial-closure into NS-3.04 synthesis.** The honest framing for NS-3.04: ED's substrate produces a stabilizing higher-derivative regularization at substrate scale (form-FORCED, value-INHERITED), conditional on dominance over standard destabilizing Burnett-class terms (INHERITED on both sides). NS-3.04's aggregate verdict will combine this with R2 and R3 outcomes.

4. **Mark Arc D dependencies in NS-3.01.** R1's analysis used standard multi-scale expansion machinery; no explicit Arc D dependency surfaced. Arc D's diffusion-coarse-graining could refine $\mu_\mathrm{V1}$'s value-INHERITED status to substrate-derivable, which would tighten NS-3.01's quantitative competition analysis (§6.3) but would not change the form-FORCED structural conclusion. Arc D opening remains a Path-A-promotion + program-strengthening decision; not critical for NS-3.

### Decisions for you

- **Confirm R1 verdict framing.** Form-FORCED-conditional Path C+ candidate is the honest framing — ED produces a real substrate-scale stabilizing mechanism, but its dominance over standard destabilizing Burnett-class terms is INHERITED on both sides. Not a clean Clay resolution; not a fail either; structurally significant but conditional.
- **Confirm proceeding to NS-3.02 directly**, vs. pausing at one-of-three NS-3 audits closed for status summary. Given NS-3's elevated stall risk overall and R1's partial closure being the most likely productive of the three audits, reasonable to either (a) push through to NS-3.02 / NS-3.03 / NS-3.04 to close the audit cycle, or (b) pause now since the most informative audit is in hand.
- **Confirm honest a-priori update.** Updated rough prior (20% C+ / 30% C− / 50% intermediate) is recorded for tracking. The shift from initial 30/50/20 toward intermediate is driven by R1's partial closure being more structurally substantial than initially expected.

---

*NS-3.01 closes R1 with partial closure: form-FORCED stabilizing $-\kappa \mu_\mathrm{V1} \ell_P^2 \nabla^4 v_i$ term derived; sign FORCED positive; magnitude INHERITED. Honest concern flagged: standard kinetic-theory Burnett-class ∇⁴ v term is destabilizing and quantitatively dominates ED's stabilizing contribution at $\lambda_\mathrm{mfp}$ scale. ED's substrate-scale stabilization is structurally significant but conditional on competition with standard destabilizing Burnett at intermediate scales. Aggregate: NS-3 trending toward intermediate (partial Path C+) rather than clean Path C+. R2 and R3 audits remain; NS-3.04 synthesis after.*
