# P4-NN-D5 — V5 Viscoelastic Integration: Maxwell from Cross-Chain Memory

**Date:** 2026-04-30
**Status:** Deliverable D5 of the P4 → Non-Newtonian arc. **Headline: Maxwell-class viscoelastic constitutive equation $\tau_R \dot\sigma + \sigma = 2\mu S$ emerges as the leading-order coarse-graining of ED's V5 cross-chain correlation kernel under exponential-decay-form. Form-FORCED: existence of memory-kernel structure + Maxwell limit. Value-INHERITED: $\tau_R$ (V5 correlation time) and $\mu$ (V5 amplitude prefactor) per arc-N N.2 §6.5. Non-canonical: Oldroyd-B, Giesekus, FENE-P require additional constitutive structure (conformation tensor, finite extensibility) beyond V5.**
**Companions:** [`P4_NN_D1_Density_Jamming.md`](P4_NN_D1_Density_Jamming.md) through [`P4_NN_D4_Empirical_Comparison.md`](P4_NN_D4_Empirical_Comparison.md), [`../Architectural_Canon.md`](../Architectural_Canon.md), [`arcs/arc-N/non_markov_forced.md`](../../arcs/arc-N/non_markov_forced.md) §6.5.

---

## 1. Purpose

This memo closes the P4 → Non-Newtonian arc by incorporating V5 (cross-chain correlations) to show how Maxwell-class viscoelasticity emerges as a natural extension of the P4 mobility-saturation framework. While P4 governs *equilibrium* mobility behavior (Krieger-Dougherty divergence, DST, Cross-class shear-thinning per D1–D2), V5 governs *time-dependent memory* — the ability of stress to relax over a finite correlation time rather than respond instantaneously to strain.

Together, P4 and V5 span the major non-Newtonian rheology classes:
- **P4 alone** → instantaneous-response non-Newtonian (jamming, DST, shear-thinning).
- **V5 alone** → linear viscoelasticity (Maxwell class).
- **P4 + V5** → broader nonlinear viscoelastic regimes (more complex, partially canonical).

The memo is brief — D5 was scoped at 0.5 sessions per [`Future_Arc_P4_Non_Newtonian_Scoping.md`](Future_Arc_P4_Non_Newtonian_Scoping.md) §5 — but closes the arc's coverage of the rheology catalogue with the viscoelastic class.

---

## 2. Inputs

| Input | Source |
|---|---|
| V5 cross-chain correlations: existence FORCED-conditional-on-V1; **amplitude INHERITED** | [`arcs/arc-N/non_markov_forced.md`](../../arcs/arc-N/non_markov_forced.md) §6.5 |
| V1 finite-width retarded vacuum kernel | Theorem N1 + T19 |
| D1–D4 P4 derivation chain (mobility, viscosity, empirical anchoring) | This arc |
| Standard Maxwell viscoelastic model: $\tau_R \dot\sigma + \sigma = 2\mu S$ | Standard rheology |
| NS-2.05 §3.1: $\tau_{ij} = \tau_{ij}^\mathrm{kin} + \tau_{ij}^\mathrm{V5} + \tau_{ij}^\mathrm{V1-mem}$ | Stress-tensor decomposition |

---

## 3. V5 Structural Content

Per arc-N N.2 §6.5, V5 establishes that same-sector chains acquire correlated bandwidth content via V1-mediated vacuum coupling. The structural content for the rheology context:

### 3.1 Memory kernel form

V5 introduces a finite-memory kernel $K_\mathrm{V5}(t)$ relating present stress to past strain rate. The cross-chain stress contribution at time $t$ takes the form:

$$\sigma_\mathrm{V5}(t) = 2\mu \int_{-\infty}^{t} K_\mathrm{V5}(t - t') \, S(t') \, dt',$$

where $S(t)$ is the symmetric strain rate at past time $t'$, and $\mu$ is the V5 amplitude prefactor (INHERITED).

### 3.2 Correlation time

The V5 correlation time $\tau_R$ is the characteristic decay scale of the kernel:

$$\tau_R = \int_0^\infty K_\mathrm{V5}(t) \, dt \cdot \tau_R^\mathrm{normalization}.$$

For a normalized kernel ($\int K_\mathrm{V5}(t) \, dt = 1$ by convention), $\tau_R$ is the kernel's decay time scale. **INHERITED** per arc-N N.2 §6.5 — V5 amplitudes (and hence correlation-time scales) depend on multi-chain couplings to the vacuum sector and are not derivable from primitive-level structure.

### 3.3 V5 vs. V1-memory distinction

Important to keep these distinct:

- **V1-memory** (single-chain): time scale $\tau_\mathrm{V1} \sim \ell_P/c \sim 10^{-44}$ s (forced by Theorem N1 + T19's ℓ_ED = ℓ_P). Coarse-grains to instantaneous at any NS scale per NS-2.05 §5. **Empirically negligible at fluid-mechanical scales.**
- **V5-memory** (cross-chain): time scale $\tau_R$ INHERITED per molecular relaxation physics. For polymer melts / solutions / biological fluids, $\tau_R$ ranges ms–s — *operative at NS scales for these systems.*

V5 supplies the empirically-relevant viscoelastic memory; V1 supplies the substrate-cutoff regularization that's only operative at substrate scales (NS-3.01 territory). The two mechanisms are structurally distinct and operate at different scales.

---

## 4. Maxwell Limit

### 4.1 Exponential-decay kernel ansatz

For the simplest V5 kernel form consistent with exponential-decay dynamics:

$$K_\mathrm{V5}(t) = \frac{1}{\tau_R} \, e^{-t/\tau_R} \quad \text{for } t \ge 0,$$

(zero for $t < 0$ by causality; normalized so $\int_0^\infty K_\mathrm{V5}(t) \, dt = 1$). This is the Maxwell-mode kernel — the simplest single-mode viscoelastic memory.

### 4.2 Convolution → Maxwell ODE

Substituting into the V5 stress expression:

$$\sigma(t) = \frac{2\mu}{\tau_R} \int_{-\infty}^t e^{-(t-t')/\tau_R} \, S(t') \, dt'.$$

Differentiate with respect to $t$ (Leibniz):

$$\dot\sigma(t) = \frac{2\mu}{\tau_R} S(t) - \frac{1}{\tau_R} \cdot \frac{2\mu}{\tau_R} \int_{-\infty}^t e^{-(t-t')/\tau_R} \, S(t') \, dt' = \frac{2\mu}{\tau_R} S(t) - \frac{1}{\tau_R} \sigma(t).$$

Rearranging:

$$\boxed{\;\tau_R \dot\sigma + \sigma = 2\mu S.\;}$$

**This is the Maxwell viscoelastic constitutive equation.** The ED-derivation gives:
- $\tau_R$ = V5 correlation time (INHERITED).
- $\mu$ = V5 amplitude prefactor (INHERITED).
- The functional form (exponential-decay memory + linear viscous response) is form-FORCED via V5's structural kernel + the leading-order Maxwell-mode ansatz.

### 4.3 Why exponential decay is natural

The exponential decay form $K_\mathrm{V5}(t) \propto e^{-t/\tau_R}$ is the simplest single-time-scale Markovian decay. It corresponds to a relaxation process in which stress decays at a rate proportional to its current value — analogous to first-order chemical kinetics or RC-circuit discharge. Physically, this matches the "single-mode" assumption in viscoelasticity: one molecular relaxation process dominates, with characteristic time $\tau_R$.

For multi-mode viscoelasticity (multiple relaxation times — common in polymer rheology), the kernel becomes a sum of exponentials:

$$K_\mathrm{V5}^\mathrm{multi}(t) = \sum_i \frac{w_i}{\tau_i} e^{-t/\tau_i},$$

corresponding to a generalized Maxwell model. Multi-mode relaxation is form-compatible with V5's cross-chain correlation structure (each mode corresponds to a different cross-chain correlation channel) but requires additional constitutive specification (mode weights $w_i$ and times $\tau_i$, all INHERITED).

---

## 5. ED Architectural Classification

### 5.1 Form-FORCED: existence of memory kernel + Maxwell limit

ED's V5 + V1 architecture forces:

- **Existence of finite-memory cross-chain stress contribution** at fluid-mechanical scales (V5 with $\tau_R$ INHERITED). V1-memory is structurally separate and operates only at substrate scales.
- **Maxwell ODE form $\tau_R \dot\sigma + \sigma = 2\mu S$** as the leading-order coarse-graining under exponential-decay V5 kernel ansatz. The functional form (linear ODE in stress, sourced by strain rate, exponential relaxation) is form-FORCED via the V5 kernel + Maxwell-mode-ansatz pair.

This places Maxwell viscoelasticity in the same architectural family as the P4-derived rheology classes (D1–D4): the *form* is universal across systems; the parameter values are INHERITED.

### 5.2 Value-INHERITED: τ_R, amplitude, non-Maxwell corrections

ED's V5 framework does *not* predict:
- Specific value of $\tau_R$ (depends on molecular relaxation physics; varies from ~ms for water-near-glass-transition to ~s for polymer melts).
- Specific value of $\mu$ amplitude (per arc-N N.2 §6.5 V5 amplitude is INHERITED).
- Multi-mode mode-weight distribution $w_i, \tau_i$ for generalized Maxwell.
- Any non-Maxwell non-linearity coupling between stress and strain rate.

These are all INHERITED from material-specific physics. The pattern matches D1–D4's form-FORCED / value-INHERITED methodology.

### 5.3 Non-canonical: Oldroyd-B, Giesekus, FENE-P

These polymer-class viscoelastic models go beyond Maxwell + V5 and require constitutive structure ED does not natively supply:

- **Oldroyd-B:** Maxwell + upper-convected derivative + retardation time. Requires conformation tensor evolution; **non-canonical ED**.
- **Giesekus:** Oldroyd-B + quadratic stress nonlinearity. Adds quadratic-in-stress coupling; **non-canonical ED**.
- **FENE-P:** Maxwell + finite-extensibility constraint on polymer chain length. Requires polymer-chain-specific finite-extensibility primitive; **non-canonical ED**.

Each is flagged for `theory/Candidate_Architectural_Extensions.md` per Architectural_Canon_Vector_Extension §8 and D3 §4.3 recommendations. Architectural extensions to absorb conformation tensors / finite extensibility are candidate future canon work, not pursued in this arc.

---

## 6. Integration With the P4 Arc

The P4 → Non-Newtonian arc spans four major non-Newtonian rheology categories via the P4 + V5 architecture:

| Category | ED architectural source | Class |
|---|---|---|
| **Equilibrium jamming** (no time-dependence) | P4 + Stokes-Einstein-class inversion | Krieger-Dougherty (D1) |
| **Shear-rate thickening** (instantaneous response) | P4 + Stokes-Einstein-class inversion applied to $\dot\gamma$ | DST / STF (D2 §4.1) |
| **Shear-rate thinning** (instantaneous response) | P4-class monotone $M(\dot\gamma)$ + either mapping | Cross / Carreau (D2 §4.2) |
| **Time-dependent memory** (finite relaxation) | V5 cross-chain correlation kernel + Maxwell-mode ansatz | Maxwell viscoelastic (D5) |

**P4 governs equilibrium / instantaneous mobility behavior** — *what* the steady-state mobility is at given (ρ, $\dot\gamma$). **V5 governs time-dependent memory** — *how fast* stress relaxes after strain-rate changes. Together they cover the major architectural axes of non-Newtonian rheology.

**Mixed regimes** (e.g., a fluid that is both shear-thickening AND viscoelastic — some dense colloidal systems) are accommodated by combining P4-class $M(\rho, \dot\gamma)$ with V5-mediated time-dependence. The combined framework is form-compatible with the major mixed-regime models in literature, with INHERITED parameter sets per system.

---

## 7. Recommended Next Steps

1. **Draft arc-level synthesis memo.** File: `theory/Navier Stokes/P4_NN_Synthesis.md`. Aggregate D1 + D2 + D3 + D4 + D5 into the arc closure. Recommended structure:
   - §1 Arc purpose and scope.
   - §2 D1 Krieger-Dougherty / density-driven jamming.
   - §3 D2 Shear-rate extension (DST + Cross).
   - §4 D3 Rheology-class catalogue (form-FORCED / compatible-INHERITED / non-canonical).
   - §5 D4 Empirical comparison (UDM β = 1.72 ± 0.37 vs. canonical ED β = 2.0 within 1σ; mechanism clusters).
   - §6 D5 Maxwell viscoelastic integration via V5.
   - §7 Aggregate arc verdict + standalone-paper recommendation.
   - §8 Identification gaps + candidate architectural extensions.
   Estimated 1 session; closes the arc.

2. **Decide on standalone-paper structure.** With D1–D5 closed, the arc has publication-grade content. Recommended path: standalone paper *"ED Mobility Saturation Predicts Non-Newtonian Rheology — Fluid-Mechanical Extension of the Universal Mobility Law,"* sequel to UDM paper. Possible structure outlined in D4 §10. Decision needed on whether to include the V5 viscoelastic integration as a chapter or as a separate paper. Recommend single-paper inclusion (V5 viscoelastic as §5 or §6 of the paper) since both P4 and V5 are integral to the rheology coverage and producing two papers risks artificial fragmentation.

3. **Optional: quantitative viscoelastic comparison.** Would require:
   - Empirical $\tau_R$ values across polymer melts, polymer solutions, biological fluids.
   - Comparison of multi-mode generalized Maxwell fits to V5-multi-correlation framework.
   - Estimated +1 session for qualitative; +2 for quantitative.
   
   Recommend deferring until standalone-paper decision is firm; can be added as appendix-class work for the paper.

### Decisions for you

- **Confirm V5 → Maxwell derivation.** Form-FORCED Maxwell ODE $\tau_R \dot\sigma + \sigma = 2\mu S$ via exponential-decay V5 kernel ansatz; $\tau_R$ and $\mu$ INHERITED per arc-N N.2 §6.5.
- **Confirm P4 + V5 architectural-axis framing** (P4 = equilibrium / instantaneous mobility; V5 = time-dependent memory).
- **Confirm proceeding to arc-level synthesis memo as next deliverable.**

---

*P4-NN-D5 V5 viscoelastic integration. Maxwell ODE $\tau_R \dot\sigma + \sigma = 2\mu S$ derived as leading-order coarse-graining of V5 cross-chain correlation kernel under exponential-decay ansatz; form-FORCED Maxwell limit, $\tau_R$ and $\mu$ INHERITED per arc-N N.2 §6.5. Multi-mode generalized Maxwell form-compatible with summed-exponential V5 kernel. Oldroyd-B / Giesekus / FENE-P non-canonical (require conformation tensor / finite extensibility beyond V5). Together with P4 (equilibrium mobility behavior — D1–D4), V5 (time-dependent memory) covers the major architectural axes of non-Newtonian rheology. Arc closes after synthesis memo (next deliverable).*
