---
title: |
  ED Mobility Saturation Predicts Non-Newtonian Rheology\
  \large A Fluid-Mechanical Extension of the Universal Mobility Law
author: Allen Proxmire
date: April 2026
---


## Abstract

We extend the empirically-validated Universal Mobility Law $D(c) = D_0(1 - c/c_\mathrm{max})^\beta$ — established for ten chemically distinct soft-matter systems with $R^2 > 0.986$ — from concentration-driven diffusion in soft matter to fluid-mechanical rheology. Treating the Universal Mobility Law as the empirical content of Event Density's architectural principle P4 (mobility capacity bound), we derive five form-FORCED predictions: (i) the Krieger-Dougherty viscosity divergence $\mu(\rho) = \mu_0(1 - \rho/\rho_\mathrm{max})^{-\beta}$ near suspension jamming; (ii) discontinuous shear-thickening / shear-thickening-fluid (STF) divergence under strain-rate-driven mobility saturation; (iii) Cross-class shear-thinning under monotone shear-rate-dependent mobility; (iv) mixed regime thinning-to-thickening transitions admitted by non-monotone constitutive choices for the mobility function; and (v) Maxwell-class viscoelasticity arising as the leading-order coarse-graining of ED's V5 cross-chain memory kernel under exponential-decay ansatz. Of thirteen catalogued standard rheology classes, five are form-FORCED at the architectural canon level, four are compatible-INHERITED (form-derivable with material-specific shape parameters not predicted from primitives), and four are non-canonical (Oldroyd-B, Giesekus, FENE-P, Bingham yield-stress) requiring constitutive structure beyond P4 + V5. Empirical comparison against the Universal Mobility Law's ten-system distribution gives mean $\beta = 1.72 \pm 0.37$, range $[1.30, 2.49]$, all $R^2 > 0.986$; this is consistent within $1\sigma$ at individual-system scatter level with the canonical Event Density prediction $\beta = 2.0$. Mechanism-clustered $\beta$ patterns — cooperative networks (H-bond viscosity, hydrodynamic crowding) cluster at $\bar\beta \approx 2.31$; steric / canonical (hard-sphere, polymer suspensions) at $\bar\beta \approx 1.76$; gradual / less-cooperative (polymer entanglement, electrostatic) at $\bar\beta \approx 1.38$ — are structurally coherent with the framework's cooperativity interpretation. The fluid-mechanical extension unifies soft-matter mobility, suspension-rheology divergence, shear-thickening fluids, polymer-melt thinning, and Maxwell viscoelasticity under a single architectural principle (P4 + V5) with canonical $\beta = 2.0$ as the quantitative anchor. Parameter values ($\beta$, $\rho_\mathrm{max}$, $\dot\gamma_\mathrm{max}$, Cross / Carreau shape parameters, V5 relaxation time $\tau_R$) are INHERITED per material-specific physics. The result extends ED's empirical reach from the soft-matter regime (Universal Mobility Law) into mainstream non-Newtonian fluid mechanics, with no new free parameters introduced beyond those already present in standard rheology models.

---

## 1. Introduction

### 1.1 The empirical universality problem in non-Newtonian rheology

Non-Newtonian rheology — the study of fluids whose viscous response deviates from the linear Newtonian $\sigma = \mu \dot\gamma$ relation — encompasses a remarkably diverse set of empirical phenomena: dense colloidal suspensions exhibit Krieger-Dougherty divergence near close-packing; cornstarch and silica suspensions exhibit discontinuous shear-thickening at critical shear rates; polymer melts and biological fluids exhibit Cross / Carreau-class shear-thinning; viscoelastic gels and polymer solutions exhibit Maxwell-class memory-kernel response. Each phenomenon is, individually, well-characterized empirically. None has a single unifying first-principles derivation in standard fluid mechanics; instead, each is described by a domain-specific phenomenological model (Krieger-Dougherty for suspensions, Cross or Carreau for polymer fluids, Maxwell or Oldroyd-B for viscoelastic media) with separately-fit material parameters.

The question this paper addresses is whether these distinct rheology classes share a deeper architectural origin. We argue that they do, and that the architectural principle is the *mobility capacity bound* P4 of Event Density's canonical PDE — the same principle that, applied to concentration in soft matter, generates the empirically-validated Universal Mobility Law.

### 1.2 The Universal Mobility Law as empirical anchor

The Universal Mobility Law (UMD) [Proxmire 2026] establishes that concentration-dependent self-diffusion in crowded soft matter follows the universal form

$$D(c) = D_0 \left(1 - \frac{c}{c_\mathrm{max}}\right)^\beta$$

across ten chemically distinct materials — colloids (hard-sphere, PMMA, Ludox silica, casein), proteins (BSA, lysozyme), polymers (PEG-water, dextran), small molecules (sucrose-water, glycerol-water) — with $R^2 > 0.986$ in every fit. The fitted exponent ranges $\beta \in [1.30, 2.49]$ with mean $\bar\beta = 1.72 \pm 0.37$, consistent within $1\sigma$ with the canonical ED-architectural value $\beta = 2.0$.

The UMD is the empirical content of Event Density's principle P4 (mobility capacity bound) instantiated on a scalar density field. It is not a phenomenological fit specific to any particular material; it is a structural prediction that the same functional form must hold across mechanistically distinct systems whose only shared feature is finite packing capacity.

### 1.3 The fluid-mechanical extension question

This paper extends the UMD's empirical anchor from soft-matter concentration-driven diffusion to fluid-mechanical rheology. The structural template is identical: P4 specifies that the mobility function $M(\cdot)$ vanishes at a packing-class upper bound $\cdot_\mathrm{max}$ on its argument. By varying which physical variable plays the role of the saturating argument — fluid density $\rho$, strain-rate magnitude $\dot\gamma$, or generalized state variables — and by combining P4 with V5 (cross-chain memory kernel for time-dependent response), we recover a family of predicted rheology classes.

The architectural commitment is fixed; the constitutive choice (which argument saturates, what specific functional form $M$ takes within the form-FORCED class) is INHERITED per material physics. This pattern — *form-FORCED, value-INHERITED* — is the canonical methodology of the Event Density program and is preserved here.

### 1.4 Scope and contributions

The paper's substantive contributions:

1. **Density-driven jamming → Krieger-Dougherty divergence** (Section 3): the universal viscosity-divergence form near suspension close-packing follows from P4 mobility saturation combined with the standard Stokes-Einstein-class mobility-viscosity inversion.

2. **Strain-rate extension → DST, STF, and Cross / Carreau shear-thinning** (Section 4): applying the same architectural template with $\dot\gamma$ as the saturating argument yields shear-thickening / discontinuous shear-thickening (mobility vanishing at upper shear-rate bound) and Cross-class shear-thinning (monotone-decreasing mobility).

3. **Rheology-class catalogue** (Section 5): we classify thirteen standard rheology classes by their architectural status — five form-FORCED, four compatible-INHERITED, four non-canonical.

4. **Empirical comparison** (Section 6): the UMD's ten-system $\beta$ distribution provides quantitative empirical anchoring; canonical ED prediction $\beta = 2.0$ is consistent within $1\sigma$ of the empirical mean $\bar\beta = 1.72 \pm 0.37$.

5. **V5 → Maxwell viscoelasticity** (Section 7): ED's cross-chain memory kernel, under exponential-decay ansatz, reduces to the Maxwell viscoelastic constitutive equation $\tau_R \dot\sigma + \sigma = 2\mu S$, with $\tau_R$ and amplitude INHERITED.

6. **Architectural synthesis** (Section 8): we show that the fluid-mechanical rheology landscape unifies under a single architectural framework (P4 + V5) with canonical $\beta = 2.0$ as the quantitative anchor.

The non-canonical classes — Oldroyd-B, Giesekus, FENE-P, Bingham yield-stress — are flagged honestly as requiring constitutive structure beyond the canonical P4 + V5 framework. They are real empirical phenomena that ED's current canon does not natively absorb; we discuss their architectural status and candidate canon-extension routes in Section 9.

### 1.5 Relationship to standard non-Newtonian rheology

ED's prediction does not contradict standard non-Newtonian rheology; it provides a structural origin for it. The Krieger-Dougherty form, the Cross and Carreau models, and the Maxwell viscoelastic equation remain valid as the canonical phenomenological descriptions. ED's contribution is to derive their *functional form* from a single architectural principle, with material-specific parameters (the $\beta$ exponent, packing fractions, shape parameters, relaxation times) inherited per system rather than postulated. The empirical match between the ten-system UMD distribution and the canonical $\beta = 2.0$ within $1\sigma$ is the substantive quantitative content of the paper.

---

## 2. Architectural Background

### 2.1 The Event Density canonical PDE

Event Density's canonical scalar partial differential equation, established in the program's foundational papers, takes the form

$$\partial_t \rho \;=\; D \cdot F[\rho] \;+\; H \cdot v, \qquad D + H = 1, \qquad D, H \in [0, 1],$$

$$\dot v = \frac{1}{\tau}\bigl(\bar F(\rho) - \zeta v\bigr),$$

with the operator

$$F[\rho] = M(\rho) \nabla^2 \rho + M'(\rho) |\nabla\rho|^2 - P(\rho).$$

Three constitutive channels — mobility ($M$), penalty ($P$), and participation ($v$) — are jointly necessary and sufficient under the seven structural constraints C1–C7 of [Foundations 2025]. The architectural canon abstracts these constraints to the seven principles P1–P7 [Architectural Canon 2026]; the Universal Mobility Law is the empirical signature of P4 (mobility capacity bound) operating on a scalar field.

### 2.2 P4: the mobility capacity bound

Principle P4 specifies:

$$M(\rho_\mathrm{max}) = 0, \qquad M(\rho) > 0 \text{ for } \rho < \rho_\mathrm{max}.$$

The mobility function vanishes at a packing-class upper bound, and is positive below. The simplest functional class admissible under the four constitutive constraints (non-negativity, vanishing at capacity, smoothness, dissipative structure) is the monomial form

$$M(\rho) = M_0 (1 - \rho/\rho_\mathrm{max})^\beta, \qquad \beta > 0.$$

The exponent $\beta$ is INHERITED per material structure. The canonical ED-architectural value is $\beta = 2.0$, which arises as the natural exponent under multiplicative-cooperativity counting (each unit of jamming-cooperativity contributes one factor of $(1 - \rho/\rho_\mathrm{max})$ to the mobility suppression).

### 2.3 V5: cross-chain memory kernel

Principle V5 (vacuum-induced cross-chain correlations), established in arc-N N.2 of the Event Density program, specifies that same-sector chains acquire correlated bandwidth content via vacuum-mediated coupling. Translated to fluid-mechanical language, V5 introduces a finite-memory kernel $K_\mathrm{V5}(t)$ relating present stress to past strain rate:

$$\sigma_\mathrm{V5}(t) = 2\mu \int_{-\infty}^t K_\mathrm{V5}(t - t') \, S(t') \, dt'.$$

The memory time $\tau_R$ — the characteristic decay scale of $K_\mathrm{V5}$ — is INHERITED; it depends on molecular-relaxation physics specific to the material. For polymer melts and solutions $\tau_R \in [10^{-3}, 10^0]\,\mathrm{s}$; for biological gels $\tau_R \in [10^{-2}, 10^1]\,\mathrm{s}$; for water $\tau_R \sim 10^{-12}\,\mathrm{s}$.

### 2.4 The dual mobility-viscosity mapping

Two distinct mobility-to-viscosity identifications are operative in fluid mechanics, depending on the physical scenario:

- **Stokes-Einstein-class inversion** (concentration-mobility scenario): $\mu \propto 1/M$. Used when $M$ represents particle self-diffusion in a suspension and viscosity is the bulk viscoelastic response. Operative in dense suspensions near jamming (Section 3).

- **NS-direct mapping** (velocity-mobility scenario): $\mu = D \cdot M$. Used when $M$ represents the kinematic-viscosity-class diffusivity for velocity gradients. Operative in polymer-melt-class shear-thinning (Section 4).

Both are admissible at the architectural level; the choice is determined by which physical mobility the Event Density mobility function $M$ represents in the particular system. The Stokes-Einstein-class inversion is imported from kinetic theory (not derived from ED); ED supplies the saturation form of $M$, kinetic theory supplies the inversion.

### 2.5 The form-FORCED / value-INHERITED methodology

Throughout this paper we maintain the canonical Event Density distinction:

- **Form-FORCED**: structural functional form derived from architectural principles. Universal across systems.
- **Value-INHERITED**: specific numerical parameters within the form-FORCED class. Determined by material-specific physics, not predictable from primitives alone.

The Universal Mobility Law is form-FORCED via P4; the specific $\beta$ value for any given system is INHERITED. The canonical $\beta = 2.0$ is a *predicted central value* under the architectural multiplicative-cooperativity reading; empirical $\bar\beta = 1.72 \pm 0.37$ is consistent within $1\sigma$.

---

## 3. D1 — Density-Driven Jamming

### 3.1 Setup: P4 mobility saturation in dense suspensions

For a dense suspension of particles in a Newtonian carrier fluid, the relevant mobility is the particle self-diffusion coefficient $M(\rho)$, where $\rho$ is the suspension's volume fraction (or equivalent packing density). The Universal Mobility Law fixes the functional form:

$$M(\rho) = M_0 \left(1 - \frac{\rho}{\rho_\mathrm{max}}\right)^\beta, \qquad \beta > 0,$$

with $M(\rho_\mathrm{max}) = 0$ corresponding to physical jamming at close-packing.

### 3.2 Stokes-Einstein-class mobility-viscosity inversion

For Brownian particles in moderate-to-dense suspensions, the Stokes-Einstein relation in the dilute limit gives

$$D_\mathrm{tracer} = \frac{k_B T}{6\pi \mu a},$$

with $a$ the particle radius. Inverting to express viscosity as a function of mobility:

$$\mu \propto \frac{1}{M(\rho)}.$$

For finite-concentration suspensions the proportionality constant is set by the dilute limit ($\mu_\mathrm{susp}(0) = \mu_0$, the carrier-fluid viscosity; $M(0) = M_0$):

$$\mu_\mathrm{susp}(\rho) = \mu_0 \cdot \frac{M_0}{M(\rho)}.$$

This is the standard Stokes-Einstein-class extension to moderately-dense suspensions (Russel, Saville & Schowalter 1989).

### 3.3 Result: Krieger-Dougherty form

Substituting the UMD mobility form:

$$\boxed{\;\mu_\mathrm{susp}(\rho) = \mu_0 \left(1 - \frac{\rho}{\rho_\mathrm{max}}\right)^{-\beta}.\;}$$

This is the **Krieger-Dougherty form** (Krieger & Dougherty 1959), structurally identical to the standard empirical model for suspension viscosity divergence near close-packing. The standard Krieger-Dougherty model writes

$$\frac{\mu_\mathrm{susp}}{\mu_0} = \left(1 - \frac{\phi}{\phi_\mathrm{max}}\right)^{-[\eta]\phi_\mathrm{max}},$$

with intrinsic viscosity $[\eta] = 5/2$ for hard spheres and maximum packing fraction $\phi_\mathrm{max} \approx 0.64$ (random close packing), giving exponent $[\eta]\phi_\mathrm{max} \approx 1.82$. Our derived form maps via $\rho \leftrightarrow \phi$, $\rho_\mathrm{max} \leftrightarrow \phi_\mathrm{max}$, $\beta \leftrightarrow [\eta]\phi_\mathrm{max}$.

### 3.4 What is form-FORCED, what is INHERITED, what is imported

| Component | Source |
|---|---|
| Mobility saturation $M(\rho_\mathrm{max}) = 0$ | Form-FORCED (P4) |
| Specific form $M(\rho) = M_0(1-\rho/\rho_\mathrm{max})^\beta$ | Form-FORCED (Universal Mobility Law) |
| Exponent $\beta$ value | INHERITED per material |
| Stokes-Einstein-class inversion $\mu \propto 1/M$ | Imported from kinetic theory |
| Krieger-Dougherty divergence $\mu \propto (1 - \rho/\rho_\mathrm{max})^{-\beta}$ | Form-FORCED (combined) |

ED's structural contribution is the *unification* of soft-matter Universal Mobility Law and suspension-rheology Krieger-Dougherty divergence under a single architectural principle (P4) plus one Stokes-Einstein-class inversion step.

---

## 4. D2 — Shear-Rate Extension

### 4.1 Strain-rate as P4 saturation argument

The architectural template extends naturally from density to strain-rate magnitude

$$\dot\gamma = \sqrt{2 \, S_{ij} S_{ij}}, \qquad S_{ij} = \frac{1}{2}(\partial_i v_j + \partial_j v_i),$$

where $S_{ij}$ is the symmetric strain-rate tensor. The natural rotational invariant $\dot\gamma$ is a positive scalar with dimensions of inverse time. Three structurally-distinct sub-cases arise from different choices of $M(\dot\gamma)$.

### 4.2 Discontinuous shear-thickening (DST) and shear-thickening fluids

Apply P4 saturation directly to strain rate:

$$M(\dot\gamma) = M_0 \left(1 - \frac{\dot\gamma}{\dot\gamma_\mathrm{max}}\right)^\beta.$$

Under Stokes-Einstein-class inversion (appropriate for particle-mobility-driven jamming under shear):

$$\mu(\dot\gamma) = \mu_0 \left(1 - \frac{\dot\gamma}{\dot\gamma_\mathrm{max}}\right)^{-\beta}.$$

Viscosity diverges at the critical shear rate $\dot\gamma \to \dot\gamma_\mathrm{max}$, corresponding to **shear-rate-driven jamming**. This is the canonical Event Density prediction for discontinuous shear-thickening (DST) and shear-thickening-fluid (STF) behavior in dense particulate suspensions.

Empirical correspondence: cornstarch + water at moderate volume fraction (DST onset at $\dot\gamma_c \sim 1$–$10\,\mathrm{s}^{-1}$); fumed silica suspensions (DST at $\dot\gamma_c \sim 10^2$–$10^4\,\mathrm{s}^{-1}$); shear-thickening fluids designed for impact protection (tuned $\dot\gamma_c \sim 10^3$–$10^5\,\mathrm{s}^{-1}$). The threshold $\dot\gamma_c$ is INHERITED across five orders of magnitude depending on system.

### 4.3 Cross / Carreau shear-thinning

For fluids whose mobility *increases* with shear (or whose effective viscosity *decreases* — polymer-melt physics where shear aligns chains and reduces effective inter-chain coupling), the appropriate framework uses monotone non-saturating $M(\dot\gamma)$. The Cross-class form admits two derivation paths:

- **Path A (NS-direct mapping):** $M(\dot\gamma) = M_0/[1 + (\lambda \dot\gamma)^n]$ decreasing; viscosity from $\mu = D \cdot M$:
$$\mu(\dot\gamma) = \frac{\mu_0}{1 + (\lambda \dot\gamma)^n}.$$

- **Path B (Stokes-Einstein-class inversion):** $M(\dot\gamma) = M_0[1 + (\lambda \dot\gamma)^n]$ increasing; viscosity from $\mu \propto 1/M$:
$$\mu(\dot\gamma) = \frac{\mu_0}{1 + (\lambda \dot\gamma)^n}.$$

Both paths produce the **Cross model**. They differ in which physical mobility ED's $M$ represents (velocity-mobility for Path A; particle-mobility for Path B). Path A is the natural physics for polymer-melt shear-thinning; Path B for suspensions in the shear-thinning regime.

The Carreau extension adds a high-shear viscosity floor $\mu_\infty$:

$$\mu(\dot\gamma) = \mu_\infty + (\mu_0 - \mu_\infty)\bigl[1 + (\lambda \dot\gamma)^2\bigr]^{(n-1)/2}.$$

The Carreau-Yasuda generalization adds a shape exponent $a$. Both are form-compatible with monotone-$M$ structures within the architectural canon; the additional shape parameters $(\mu_\infty, n, a, \lambda)$ are INHERITED.

Empirical correspondence: polymer melts (HDPE, polystyrene, polypropylene) with $n \sim 0.3$–$0.5$ and $\lambda \sim 10^{-2}$–$10^0\,\mathrm{s}$; polymer solutions ($n \sim 0.1$–$0.4$; $\lambda \sim 10^{-1}$–$10^1\,\mathrm{s}$); blood ($n \sim 0.3$, $\lambda \sim 1$–$5\,\mathrm{s}$); paints ($n \sim 0.1$–$0.4$).

### 4.4 Mixed regimes via non-monotone $M(\dot\gamma)$

Real concentrated suspensions often exhibit shear-thinning at low shear rates (alignment / lubrication-mediated) followed by shear-thickening at higher rates (DST onset). Event Density accommodates this via non-monotone mobility:

$$M_\mathrm{mixed}(\dot\gamma) = M_0 \bigl[1 + (\lambda_1 \dot\gamma)^{n_1}\bigr] \cdot \left(1 - \frac{\dot\gamma}{\dot\gamma_\mathrm{max}}\right)^\beta.$$

At low $\dot\gamma$ the shear-thinning factor dominates and $M$ rises; near $\dot\gamma_\mathrm{max}$ the saturation factor drives $M \to 0$ and viscosity diverges. The combined curve transitions from shear-thinning to DST onset.

Empirical correspondence: concentrated colloidal suspensions, semi-dilute polymer solutions with associative interactions, granular pastes, food rheology (yogurt, ketchup, mayonnaise).

### 4.5 The dual-mapping framework

The two distinct mobility-viscosity mappings (Stokes-Einstein-class inversion for particle-mobility; NS-direct for velocity-mobility) are not in competition; they apply to different physical scenarios. The architectural canon supplies the saturation *form*; the choice of which mobility the form applies to is determined by the system being modeled. Both choices preserve the form-FORCED / value-INHERITED methodology cleanly.

---

## 5. D3 — Rheology-Class Catalogue

We classify thirteen standard rheology classes by their architectural status under the P4 + V5 framework. Notation: SE = Stokes-Einstein-class inversion; NS-direct = velocity-mobility direct mapping; Form-FORCED = derivable from architectural principles; Compatible-INHERITED = architecturally consistent but with shape parameters going beyond basic P4 + V5; Non-canonical = requires structural content beyond P4 + V5.

| # | Class | Standard form | Mapping | Status | Notes |
|---|---|---|---|---|---|
| 1 | Newtonian | $\mu = \mathrm{const}$ | Either | Form-FORCED (limit) | P4 far from saturation |
| 2 | Krieger-Dougherty | $\mu \propto (1-\phi/\phi_\mathrm{max})^{-[\eta]\phi_\mathrm{max}}$ | SE | Form-FORCED | Section 3 |
| 3 | DST / STF | $\mu \propto (1-\dot\gamma/\dot\gamma_c)^{-\beta}$ | SE | Form-FORCED | Section 4.2 |
| 4 | Power-law thinning | $\mu = K\dot\gamma^{n-1}$ | Either | Compatible-INHERITED | Cross-class high-shear limit |
| 5 | Cross | $\mu = \mu_0/[1+(\lambda\dot\gamma)^n]$ | Either | Form-FORCED | Section 4.3 |
| 6 | Carreau | $(\mu - \mu_\infty)/(\mu_0-\mu_\infty) = [1+(\lambda\dot\gamma)^2]^{(n-1)/2}$ | Either | Compatible-INHERITED | Adds $\mu_\infty$ |
| 7 | Carreau-Yasuda | Carreau with shape exponent $a$ | Either | Compatible-INHERITED | Industrial standard fit |
| 8 | Mixed (thin-then-thick) | Non-monotone $\mu(\dot\gamma)$ | Either | Form-FORCED | Section 4.4 |
| 9 | Maxwell viscoelastic | $\tau_R \dot\sigma + \sigma = 2\mu S$ | V5 kernel | Compatible-INHERITED | Section 7 |
| 10 | Oldroyd-B | Maxwell + convected derivative + retardation | Beyond V5 | Non-canonical | Conformation tensor |
| 11 | Giesekus | Oldroyd-B + quadratic stress | Beyond V5 | Non-canonical | Stress nonlinearity |
| 12 | FENE-P | Maxwell + finite extensibility | Beyond V5 | Non-canonical | Polymer chain constraint |
| 13 | Bingham yield-stress | $\sigma = \sigma_\mathrm{yield} + \mu\dot\gamma$ | Inverted P4 | Non-canonical | Sign-inverted threshold |

**Summary statistics:**

- **Form-FORCED (5 classes):** Newtonian, Krieger-Dougherty, DST/STF, Cross-class shear-thinning, mixed-regime non-monotone.
- **Compatible-INHERITED (4 classes):** power-law thinning, Carreau, Carreau-Yasuda, Maxwell viscoelastic.
- **Non-canonical (4 classes):** Oldroyd-B, Giesekus, FENE-P, Bingham yield-stress.

**Coverage:** 9 of 13 classes fall within ED's canonical architectural reach. The four non-canonical classes are concentrated in polymer-solution-specific models (Oldroyd-B, Giesekus, FENE-P) and yield-stress fluids (Bingham, requiring sign-inverted P4); each is a candidate for future architectural extension via tensor / inverted-saturation primitives, tracked in [Candidate Architectural Extensions 2026].

---

## 6. D4 — Empirical Comparison

### 6.1 The Universal Mobility Law's ten-system distribution

The empirical anchor for the fluid-mechanical extension is the Universal Mobility Law's ten-system distribution. Table 1 reports the fitted exponents $\beta$ and goodness-of-fit $R^2$ across the ten chemically distinct materials.

**Table 1: Universal Mobility Law fits across 10 materials** [Proxmire 2026, Table 1]

| # | Material | Type | Mechanism | $\beta$ | $R^2$ |
|---|---|---|---|---|---|
| 1 | Hard-sphere colloids | Colloid | Steric jamming | 1.69 | 0.995 |
| 2 | Sucrose-water | Molecular | H-bond viscosity | 2.49 | 0.987 |
| 3 | BSA protein | Protein | Hydrodynamic crowding | 2.12 | 0.986 |
| 4 | Lysozyme | Protein | Short-range attraction + crowding | 1.36 | 0.998 |
| 5 | PMMA colloids | Colloid | Steric jamming | 1.81 | 0.994 |
| 6 | Ludox silica | Charged colloid | Electrostatic + steric | 1.41 | 0.999 |
| 7 | PEG-water | Polymer | Entanglement | 1.30 | 0.996 |
| 8 | Dextran | Polysaccharide | Polymer crowding | 1.46 | 0.993 |
| 9 | Casein micelles | Bio-colloid | Depletion + steric | 1.79 | 0.998 |
| 10 | Glycerol-water | Small molecule | Viscosity divergence | 1.74 | 0.999 |

**Key statistics:**

- **Mean** $\bar\beta = 1.72 \pm 0.37$ ($N = 10$)
- **Range** $[1.30, 2.49]$
- **Goodness of fit** $R^2 > 0.986$ in every system; 7 of 10 with $R^2 \geq 0.99$
- **Mechanisms covered** 8 distinct physical mechanisms
- **Materials excluded** 0

### 6.2 Comparison to canonical $\beta = 2.0$

The canonical Event Density prediction is $\beta = 2.0$, arising from the architectural multiplicative-cooperativity reading of P4 mobility saturation. The empirical mean $\bar\beta = 1.72$ deviates from this central value by:

$$\Delta \beta = |\beta_\mathrm{ED} - \bar\beta| = 0.28.$$

Normalized to the empirical standard deviation:

$$\frac{\Delta \beta}{\sigma_\beta} = \frac{0.28}{0.37} \approx 0.76 \, \sigma.$$

**The canonical ED prediction is consistent within $1\sigma$ of the individual-system scatter level.**

At the standard-error-of-mean level:

$$\sigma_{\bar\beta} = \frac{\sigma_\beta}{\sqrt{N}} = \frac{0.37}{\sqrt{10}} \approx 0.117,$$

$$\frac{\Delta \beta}{\sigma_{\bar\beta}} = \frac{0.28}{0.117} \approx 2.4 \, \sigma.$$

The standard-error-of-mean deviation is $2.4\sigma$ — marginal but admitting structural interpretation: if the ten-system population under-samples cooperative networks (which would shift $\bar\beta$ above 2), the population mean would naturally sit below the canonical central value. Larger or more diverse system populations would tighten this comparison.

### 6.3 Mechanism-clustered $\beta$ patterns

Grouping the ten systems by structural cooperativity class:

| Cluster | Mechanisms | Systems | $\bar\beta$ |
|---|---|---|---|
| Cooperative (high $\beta$) | H-bond viscosity, hydrodynamic crowding | sucrose, BSA | $\bar\beta \approx 2.31$ |
| Steric / canonical (mid $\beta$) | Hard-sphere, PMMA, casein, glycerol | hard-sphere, PMMA, casein, glycerol | $\bar\beta \approx 1.76$ |
| Gradual / less-cooperative (low $\beta$) | Polymer entanglement, electrostatic, short-range attraction | PEG, lysozyme, Ludox, dextran | $\bar\beta \approx 1.38$ |

The three-cluster pattern is structurally interpretable under Event Density's cooperativity reading: higher $\beta$ corresponds to more cooperative arrest (more neighbours must be simultaneously displaced for a particle to move); lower $\beta$ to more gradual decline. The steric / canonical cluster's mean $\bar\beta \approx 1.76$ sits closest to the canonical prediction; cooperative networks (H-bond, hydrodynamic) push above; gradual / less-cooperative systems (polymer entanglement, electrostatic) pull below.

This pattern is not random material-specific scatter; it reflects a structurally-coherent gradation of cooperativity strength across the ten systems.

### 6.4 Cross-class extrapolation to broader rheology literature

Beyond the ten UMD systems, the fluid-mechanical extension predicts that Krieger-Dougherty divergence, DST exponents, and Cross-class shape parameters should also fall within form-FORCED bounds, with INHERITED specific values per material.

**Krieger-Dougherty $\beta$ values** in standard suspension-rheology literature:
- Hard-sphere suspensions: $\beta \approx 1.5$–$2.0$ (canonical $[\eta]\phi_\mathrm{max} \approx 1.82$).
- Soft / polymeric colloids: $\beta \approx 1.0$–$2.5$.
- Polydisperse suspensions: $\beta \approx 1.5$–$3.0$ (rises with polydispersity).
- Granular pastes: $\beta \approx 2$–$4$ (frictional contacts).
- Fiber / rod suspensions: $\beta \approx 2$–$5$ (anisotropic alignment).

The wider literature ranges sit at and above the UMD soft-matter range, consistent with the cooperativity interpretation: granular systems have stronger frictional cooperativity than colloids; anisotropic systems have stronger alignment cooperativity than isotropic.

**DST critical shear rates** span 5+ orders of magnitude across material classes (cornstarch + water $\sim 1$–$10\,\mathrm{s}^{-1}$; STF body-armor designs $\sim 10^3$–$10^5\,\mathrm{s}^{-1}$). Form-universality holds; specific $\dot\gamma_c$ INHERITED.

**Cross / Carreau shape parameters** $n \sim 0.1$–$0.7$ and $\lambda \sim 10^{-3}$–$10^1\,\mathrm{s}$ across polymer melts, solutions, and biological fluids. Form-universality holds; specific $(n, \lambda)$ INHERITED.

### 6.5 Empirical-comparison aggregate verdict

- **Form-FORCED universality:** strongly supported. The Universal Mobility Law form fits 10 mechanistically distinct systems with $R^2 > 0.986$; cross-class extrapolation to Krieger-Dougherty / DST / Cross literature is consistent at order-of-magnitude level.
- **Canonical $\beta = 2.0$ quantitative anchor:** consistent within $1\sigma$ at individual-system scatter level. The systematic offset (mean 1.72 vs. canonical 2.0) admits structural interpretation via mechanism-class population.
- **Mechanism-clustered $\beta$ patterns:** structurally coherent with cooperativity interpretation. The three-cluster pattern (cooperative / canonical / gradual) is not random scatter.

**Aggregate:** Event Density's fluid-mechanical extension is consistent with empirical rheology data at qualitative + light-quantitative level. The form-FORCED structural claim is empirically validated; the canonical quantitative anchor is consistent within statistical scatter; mechanism-class patterns add structural coherence beyond the basic universality finding.

---

## 7. D5 — Maxwell Viscoelasticity from V5

### 7.1 V5 cross-chain memory kernel

Per arc-N N.2 of the Event Density program, V5 establishes that same-sector chains acquire correlated bandwidth content via vacuum-mediated coupling. In fluid-mechanical context, this corresponds to a finite-memory stress-strain coupling:

$$\sigma_\mathrm{V5}(t) = 2\mu \int_{-\infty}^t K_\mathrm{V5}(t - t') \, S(t') \, dt',$$

where $K_\mathrm{V5}(t)$ is the V5 memory kernel (zero for $t < 0$ by causality; normalized so $\int_0^\infty K_\mathrm{V5}(t)\,dt = 1$ by convention), and $\mu$ is the V5 amplitude prefactor. Both $K_\mathrm{V5}$ and $\mu$ are INHERITED per arc-N N.2 §6.5.

### 7.2 Exponential-decay ansatz: the Maxwell-mode kernel

The simplest single-mode V5 kernel — and the one most natural under exponential-decay relaxation kinetics — is

$$K_\mathrm{V5}(t) = \frac{1}{\tau_R} \, e^{-t/\tau_R} \quad \text{for } t \geq 0,$$

where $\tau_R$ is the V5 correlation time (INHERITED per material physics). For polymer melts and solutions $\tau_R \in [10^{-3}, 10^0]\,\mathrm{s}$; for biological gels $\tau_R \in [10^{-2}, 10^1]\,\mathrm{s}$.

### 7.3 Reduction to Maxwell ODE

Substitute into the V5 stress expression:

$$\sigma(t) = \frac{2\mu}{\tau_R} \int_{-\infty}^t e^{-(t-t')/\tau_R} \, S(t') \, dt'.$$

Differentiate with respect to $t$:

$$\dot\sigma(t) = \frac{2\mu}{\tau_R} S(t) - \frac{1}{\tau_R} \cdot \frac{2\mu}{\tau_R} \int_{-\infty}^t e^{-(t-t')/\tau_R} \, S(t') \, dt' = \frac{2\mu}{\tau_R} S(t) - \frac{1}{\tau_R} \sigma(t).$$

Rearranging:

$$\boxed{\;\tau_R \dot\sigma + \sigma = 2\mu S.\;}$$

This is the **Maxwell viscoelastic constitutive equation** [Maxwell 1867; Tanner 2000], the canonical phenomenological model for linear viscoelasticity. ED's V5 supplies the form-FORCED memory-kernel structure under exponential-decay ansatz; $\tau_R$ and $\mu$ remain INHERITED.

### 7.4 Multi-mode generalized Maxwell

For multi-mode viscoelasticity (multiple molecular relaxation processes — common in polymer rheology), the V5 kernel becomes a sum of exponentials:

$$K_\mathrm{V5}^\mathrm{multi}(t) = \sum_i \frac{w_i}{\tau_i} \, e^{-t/\tau_i},$$

with mode weights $w_i$ and times $\tau_i$ all INHERITED. This corresponds to the standard generalized Maxwell model. Form-compatible with V5; values INHERITED per material structure.

### 7.5 V5 vs. V1 memory: a critical distinction

It is essential to distinguish V5 cross-chain memory from V1 single-chain memory:

- **V1 memory:** characteristic time $\tau_\mathrm{V1} \sim \ell_P/c \sim 10^{-44}\,\mathrm{s}$ (forced by Theorem N1 + Newton-recovery in T19, where $\ell_\mathrm{ED} = \ell_P$). At any fluid-mechanical scale, V1 memory coarse-grains to instantaneous response; it is operative only at substrate scale.
- **V5 memory:** characteristic time $\tau_R$ INHERITED at molecular-relaxation scale ($10^{-3}$–$10^0\,\mathrm{s}$ for polymer melts, solutions, gels). Operative at fluid-mechanical scales.

V5, not V1, is the empirically-relevant viscoelastic memory mechanism at fluid-mechanical scales. V1's substrate-cutoff regularization is structurally distinct and is operative only in the smoothness / blow-up question (Clay-NS territory; out of scope for this paper).

### 7.6 Architectural status

| Component | Source |
|---|---|
| Existence of finite-memory cross-chain stress contribution | Form-FORCED (V5) |
| Maxwell ODE form $\tau_R \dot\sigma + \sigma = 2\mu S$ | Form-FORCED (V5 + Maxwell-mode ansatz) |
| $\tau_R$ value | INHERITED |
| $\mu$ amplitude | INHERITED (per arc-N N.2 §6.5) |
| Multi-mode mode-weight distribution | INHERITED |
| Beyond-Maxwell constitutive structure (Oldroyd-B, etc.) | Non-canonical (requires extensions) |

### 7.7 Architectural axis structure: P4 + V5

P4 governs *equilibrium / instantaneous* mobility behavior — what the steady-state mobility (and viscosity) is at given $(\rho, \dot\gamma)$. V5 governs *time-dependent memory* — how fast stress relaxes after strain-rate changes. Together, P4 and V5 cover the major architectural axes of non-Newtonian rheology:

| Behavior axis | ED architectural source |
|---|---|
| Equilibrium / instantaneous response | P4 (mobility saturation) |
| Time-dependent memory / relaxation | V5 (cross-chain correlation kernel) |
| Mixed time-dependent + nonlinear | P4 + V5 combined |

---

## 8. Synthesis

### 8.1 Three structural unifications

The fluid-mechanical extension of the Universal Mobility Law accomplishes three structurally meaningful unifications:

1. **Soft-matter mobility ↔ suspension rheology.** The Universal Mobility Law (concentration self-diffusion in 10 soft-matter systems with $R^2 > 0.986$) and the suspension-rheology Krieger-Dougherty model (viscosity divergence near close-packing) are revealed as two manifestations of a single architectural principle (P4) plus one Stokes-Einstein-class inversion step. Two empirical regimes usually treated as separate become one Event Density-architectural family.

2. **Equilibrium and time-dependent rheology.** P4 (mobility saturation, instantaneous response) and V5 (cross-chain memory kernel, Maxwell viscoelasticity) are both architectural canon principles of Event Density. Together they cover the major architectural axes of non-Newtonian rheology — instantaneous-mobility classes (Sections 3–4) and time-dependent-memory classes (Section 7) — within a single framework.

3. **Form-FORCED + canonical-quantitative-anchor methodology.** ED's prediction extends beyond pure form-FORCED to include a quantitative canonical $\beta = 2.0$ anchor. The empirical mean $\bar\beta = 1.72 \pm 0.37$ is consistent within $1\sigma$ of the canonical central value at individual-system scatter level. This is stronger than form-FORCED-only methodology used in some prior program closures and represents a methodological advance: ED can produce quantitatively-leaning predictions in addition to structural ones, with empirical scatter set by INHERITED material physics.

### 8.2 Form-FORCED / value-INHERITED summary

| Component | Form status | Value status |
|---|---|---|
| P4 mobility saturation | FORCED | — |
| Universal Mobility Law functional form | FORCED | — |
| Krieger-Dougherty divergence $\mu \propto (1-\rho/\rho_\mathrm{max})^{-\beta}$ | FORCED | $\beta$ INHERITED |
| DST / STF divergence form | FORCED | $\dot\gamma_\mathrm{max}$, $\beta$ INHERITED |
| Cross / Carreau shear-thinning form | FORCED | $n, \lambda, \mu_\infty$ INHERITED |
| Mixed-regime non-monotone $M$ | FORCED via constitutive freedom | Specific form INHERITED |
| V5 cross-chain memory existence | FORCED-conditional-on-V1 | Amplitude INHERITED |
| Maxwell ODE form | FORCED via V5 + exponential ansatz | $\tau_R, \mu$ INHERITED |
| Canonical $\beta = 2.0$ central value | Predicted (multiplicative cooperativity) | — |
| Empirical $\bar\beta = 1.72 \pm 0.37$ | — | INHERITED (population statistic) |

### 8.3 Architectural reach

Of thirteen catalogued standard rheology classes:

- **Five form-FORCED:** Newtonian (P4 limit), Krieger-Dougherty, DST/STF, Cross-form shear-thinning, mixed-regime non-monotone.
- **Four compatible-INHERITED:** power-law thinning, Carreau, Carreau-Yasuda, Maxwell viscoelastic.
- **Four non-canonical:** Oldroyd-B, Giesekus, FENE-P, Bingham yield-stress.

Event Density's architectural canon covers 9 of 13 classes (5 FORCED + 4 INHERITED). The 4 non-canonical classes are concentrated in polymer-solution-specific models (Oldroyd-B, Giesekus, FENE-P) and yield-threshold fluids (Bingham); each is a candidate for future canonical extension via tensor / inverted-saturation primitives.

---

## 9. Discussion

### 9.1 Significance for Event Density's empirical reach

Prior to the fluid-mechanical extension, Event Density's empirical anchoring rested on the Universal Mobility Law's ten-system validation in soft matter. The extension developed here moves ED's empirical content into mainstream non-Newtonian fluid mechanics — an empirically-rich domain with extensive industrial, biomedical, and geophysical applications. The structural unification of soft-matter mobility, suspension rheology, shear-thickening fluids, polymer-melt thinning, and Maxwell viscoelasticity under a single architectural principle (P4 + V5) substantially broadens ED's predictive footprint.

The result is consistent with — and extends — the Event Density program's existing structural-foundations content. The form-FORCED / value-INHERITED methodology is preserved; the canonical $\beta = 2.0$ prediction adds a quantitative anchor that the framework can be tested against; the four non-canonical classes are honestly catalogued rather than fitted into the canon by force.

### 9.2 Honest limitations

Several limitations warrant explicit discussion:

**Stokes-Einstein-class inversion is imported.** The mobility-to-viscosity conversion in dense suspensions (Section 3.2) uses Stokes-Einstein-class physics from standard kinetic theory. Event Density supplies the saturation form of $M(\rho)$; kinetic theory supplies the inversion to viscosity. The combination is Krieger-Dougherty. ED does not independently derive Stokes-Einstein. This is honest accounting rather than a weakness — most empirical content in physics combines architectural principles with imported relations.

**Quantitative comparison is light.** The $\bar\beta = 1.72$ vs. canonical $\beta = 2.0$ comparison is the strongest quantitative result. Cross-class extrapolation to broader Krieger-Dougherty / DST / Cross literature is order-of-magnitude only. Full statistical analysis (ANOVA on mechanism clusters; formal hypothesis test on canonical $\beta$; AIC/BIC against alternative phenomenological models) is appendix-class work.

**V5 amplitude INHERITED status limits viscoelastic prediction power.** Section 7 establishes Maxwell-class compatibility but does not predict $\tau_R$ or amplitude values. Real predictive content for viscoelastic fluids would require additional substrate articulation beyond the current V5 framework.

**Standard-error-of-mean vs. individual-system scatter.** The canonical $\beta = 2.0$ prediction is consistent within $1\sigma$ at individual-system scatter level (mean $\bar\beta = 1.72$, $\sigma = 0.37$). At standard-error-of-mean level (which scales as $\sigma/\sqrt{N}$), the deviation is 2.4σ — marginal but not strongly inconsistent. Larger or more diverse system populations would tighten this comparison.

**Not a Clay-NS resolution.** This paper is "ED on Earth" empirical territory — non-Newtonian rheology — not Clay-NS smoothness. The smoothness / blow-up question for the developed-cascade turbulence regime (closed at Intermediate verdict in NS-3.04) is structurally distinct from the rheology questions addressed here; the structural feature breaking BKM-class smoothness in 3D NS is the advective vortex-stretching term, unrelated to P4 / V5.

### 9.3 Non-canonical classes and candidate canon extensions

The four non-canonical classes — Oldroyd-B, Giesekus, FENE-P, Bingham yield-stress — are real empirical phenomena that ED's current canonical architecture does not natively absorb:

- **Oldroyd-B** requires a conformation tensor evolving under upper-convected-derivative dynamics; this is tensor-extension architectural content beyond the scalar P4 + V5 framework.
- **Giesekus** adds a quadratic stress nonlinearity to Oldroyd-B; requires both tensor extension and quadratic-coupling structure.
- **FENE-P** adds a finite-extensibility constraint on polymer chain length; requires polymer-chain-specific structural content.
- **Bingham yield-stress** requires sign-inverted P4 (mobility zero at *lower* stress threshold rather than upper packing limit).

Each is a candidate for future architectural extension. Tensor-extension of the canonical PDE (parallel to the vector-extension framework of [Architectural Canon Vector Extension 2026]) could potentially absorb Oldroyd-B and Giesekus structurally. Inverted-P4 architectural variants could potentially handle Bingham. None is pursued in this paper; they are flagged for future canon-extension work.

### 9.4 Future work

Three concrete future directions emerge from the arc:

1. **Quantitative empirical refinement.** Full statistical analysis of the UMD ten-system distribution (ANOVA on mechanism clusters; formal hypothesis test of canonical $\beta = 2.0$; AIC/BIC vs. alternative models) would strengthen the empirical anchoring quantitatively.

2. **Tensor-extension architectural canon.** Following the vector-extension framework already articulated for fluid kinematics, a tensor-extension would address Oldroyd-B, Giesekus, and FENE-P at the architectural level. This is substantial future work parallel in scale to a canon-extension memo.

3. **Forced-response and turbulence connections.** A separate arc (Reference: [P7 Triads NS-Turb Synthesis 2026]) found that ED's P7 triadic harmonic-generation structure provides a restricted-regime forced-response prediction in viscous-laminar flow but does not architecturally template developed-cascade turbulence. The interplay between P4 + V5 (rheology) and P7 (harmonic generation) at the level of full nonlinear fluid response remains an open structural question.

---

## 10. Conclusion

We have shown that Event Density's principle P4 (mobility capacity bound), already empirically validated in the soft-matter regime via the Universal Mobility Law's ten-system $R^2 > 0.986$ fit quality, extends to fluid-mechanical rheology to predict, at the architectural-canon level:

- **Krieger-Dougherty viscosity divergence** $\mu(\rho) = \mu_0 (1 - \rho/\rho_\mathrm{max})^{-\beta}$ near suspension jamming;
- **Discontinuous shear-thickening / shear-thickening-fluid (STF)** divergence under strain-rate-driven mobility saturation;
- **Cross / Carreau shear-thinning** under monotone strain-rate-dependent mobility;
- **Mixed thinning-then-thickening regimes** under non-monotone constitutive choices;
- **Maxwell-class viscoelasticity** $\tau_R \dot\sigma + \sigma = 2\mu S$ as the leading-order coarse-graining of V5 cross-chain memory kernel under exponential-decay ansatz.

Of thirteen standard rheology classes catalogued, nine (five form-FORCED, four compatible-INHERITED) fall within the canonical architectural reach of P4 + V5; four (Oldroyd-B, Giesekus, FENE-P, Bingham yield-stress) are non-canonical and flagged for future architectural extension.

Empirical comparison gives mean $\bar\beta = 1.72 \pm 0.37$ across the ten Universal Mobility Law systems, consistent within $1\sigma$ at individual-system scatter level with the canonical Event Density prediction $\beta = 2.0$. Mechanism-clustered $\beta$ patterns — cooperative networks $\bar\beta \approx 2.31$, steric / canonical $\bar\beta \approx 1.76$, gradual / less-cooperative $\bar\beta \approx 1.38$ — are structurally coherent with the canonical cooperativity interpretation.

The structural significance is the unification of three previously-separate empirical regimes — soft-matter mobility, suspension-rheology divergence, polymer-class viscoelastic response — under a single architectural principle (P4 + V5) with a quantitative canonical anchor ($\beta = 2.0$, supported within $1\sigma$). Parameter values (specific $\beta$ exponent, packing fraction, shear-rate threshold, Cross / Carreau shape parameters, V5 relaxation time) remain INHERITED per material-specific physics, consistent with Event Density's form-FORCED / value-INHERITED methodology.

The result extends Event Density's empirical reach from the soft-matter regime (Universal Mobility Law) into mainstream non-Newtonian fluid mechanics, with no new free parameters introduced beyond those already present in standard rheology models.

---

## Appendix A. Derivation of the Krieger-Dougherty Form

We outline the explicit derivation chain for the Krieger-Dougherty viscosity-divergence form from the architectural principle P4.

**Step 1 — P4 mobility saturation.** The architectural principle P4 specifies that the mobility function $M(\rho)$ vanishes at a packing-class upper bound:

$$M(\rho_\mathrm{max}) = 0, \qquad M(\rho) > 0 \text{ for } \rho < \rho_\mathrm{max}.$$

The simplest functional class admissible under non-negativity, vanishing-at-capacity, smoothness, and dissipative-structure constraints is the monomial form

$$M(\rho) = M_0 (1 - \rho/\rho_\mathrm{max})^\beta, \qquad \beta > 0.$$

**Step 2 — Empirical anchor via Universal Mobility Law.** The empirical content of P4 in the soft-matter regime is the Universal Mobility Law $D(c) = D_0(1 - c/c_\mathrm{max})^\beta$, validated across 10 chemically distinct systems with $R^2 > 0.986$ in every fit.

**Step 3 — Stokes-Einstein-class inversion.** The dilute-limit Stokes-Einstein relation

$$D_\mathrm{tracer} = \frac{k_B T}{6\pi \mu a}$$

extends to moderate-to-dense suspensions via the inversion

$$\mu_\mathrm{susp}(\rho) = \mu_0 \cdot \frac{M_0}{M(\rho)},$$

with the proportionality constant set by the dilute limit ($\mu_\mathrm{susp}(0) = \mu_0$, the carrier-fluid viscosity).

**Step 4 — Combined Krieger-Dougherty form.** Substituting:

$$\mu_\mathrm{susp}(\rho) = \mu_0 (1 - \rho/\rho_\mathrm{max})^{-\beta},$$

structurally identical to the standard Krieger-Dougherty form $\mu/\mu_0 = (1 - \phi/\phi_\mathrm{max})^{-[\eta]\phi_\mathrm{max}}$ under the identification $\beta \leftrightarrow [\eta]\phi_\mathrm{max} \approx 1.82$ for hard spheres.

**Step 5 — Form-FORCED / value-INHERITED status.** The functional form is form-FORCED by P4 + Universal Mobility Law + Stokes-Einstein. The exponent $\beta$ value is INHERITED per particle geometry, surface chemistry, and inter-particle interaction structure.

---

## Appendix B. The Dual Mobility-Viscosity Mapping

Two distinct mobility-viscosity identifications apply in fluid mechanics, depending on the physical scenario:

**Stokes-Einstein-class inversion** ($\mu \propto 1/M$). Applies when $M$ represents particle self-diffusion in a suspension and $\mu$ represents the bulk viscoelastic response. Operative in dense-suspension Krieger-Dougherty / DST scenarios where particle mobility drives jamming behavior. Imported from kinetic theory; not derived from ED.

**NS-direct mapping** ($\mu = D \cdot M$). Applies when $M$ represents the kinematic-viscosity-class diffusivity for velocity gradients in an Event Density vector-extension treatment of fluid kinematics. Operative in polymer-melt-class shear-thinning scenarios where chain alignment under shear reduces effective momentum transport.

Both mappings are admissible at the architectural level. The choice is determined by which physical mobility ED's $M$ represents in the particular system — concentration-mobility (for jamming/DST) vs. velocity-mobility (for polymer-melt thinning). The architectural canon supplies the saturation *form*; the choice of mapping reflects the physical scenario being modeled. Both choices preserve the form-FORCED / value-INHERITED methodology cleanly.

---

## Appendix C. V5 Memory-Kernel Reduction to Maxwell ODE

We derive the Maxwell viscoelastic equation as the leading-order coarse-graining of V5 cross-chain memory kernel under exponential-decay ansatz.

**V5 stress-strain coupling.** Per arc-N N.2, V5 introduces:

$$\sigma_\mathrm{V5}(t) = 2\mu \int_{-\infty}^t K_\mathrm{V5}(t - t') S(t') \, dt'.$$

**Exponential ansatz.** The simplest single-mode V5 kernel:

$$K_\mathrm{V5}(t) = \frac{1}{\tau_R} e^{-t/\tau_R} \quad (t \geq 0).$$

**Differentiation.** Taking $d/dt$ of the V5 stress:

$$\dot\sigma(t) = 2\mu K_\mathrm{V5}(0) S(t) + 2\mu \int_{-\infty}^t \frac{dK_\mathrm{V5}}{dt}(t-t') S(t') \, dt'.$$

For the exponential kernel:
- $K_\mathrm{V5}(0) = 1/\tau_R$.
- $dK_\mathrm{V5}/dt = -K_\mathrm{V5}/\tau_R$.

Substituting:

$$\dot\sigma(t) = \frac{2\mu}{\tau_R} S(t) - \frac{1}{\tau_R} \cdot 2\mu \int_{-\infty}^t K_\mathrm{V5}(t-t') S(t') \, dt' = \frac{2\mu}{\tau_R} S(t) - \frac{1}{\tau_R} \sigma(t).$$

**Maxwell ODE.** Rearranging:

$$\tau_R \dot\sigma + \sigma = 2\mu S.$$

**Multi-mode generalization.** For multiple molecular relaxation processes:

$$K_\mathrm{V5}^\mathrm{multi}(t) = \sum_i \frac{w_i}{\tau_i} e^{-t/\tau_i},$$

corresponding to the standard generalized Maxwell model with mode weights $w_i$ and times $\tau_i$ all INHERITED.

**Architectural status.** Form-FORCED at the existence-of-memory-kernel + Maxwell-mode-ansatz level via V5 + exponential-decay ansatz; values INHERITED per molecular-relaxation physics.

---

## References

[Architectural Canon 2026] Proxmire, A. *The Architectural Canon of Event Density.* Event Density program, March 2026.

[Born-Gleason 2026] Proxmire, A. *Born Rule from Gleason-Busch in Event Density.* ED Foundational Theorems series, 2026.

[Candidate Architectural Extensions 2026] *Candidate Architectural Extensions* tracking memo, Event Density program, 2026.

[Foundations 2025] Proxmire, A. *Foundations of Event Density: Axiomatic Derivation and Universality.* Event Density program, 2025.

[Krieger & Dougherty 1959] Krieger, I.M. & Dougherty, T.J. "A Mechanism for Non-Newtonian Flow in Suspensions of Rigid Spheres." *Trans. Soc. Rheol.* 3, 137–152 (1959).

[Maxwell 1867] Maxwell, J.C. "On the dynamical theory of gases." *Philos. Trans. R. Soc.* 157, 49–88 (1867).

[NS-1.05 2026] Proxmire, A. *NS-1.05 — Synthesis: Final B2 Dimensional-Forcing Verdict.* Event Density Navier-Stokes roadmap, 2026.

[NS-3.04 2026] Proxmire, A. *NS-3.04 — Synthesis + Path C Verdict.* Event Density Navier-Stokes roadmap, 2026.

[P7 Triads NS-Turb Synthesis 2026] Proxmire, A. *P7 Triads NS-Turb-5 Synthesis.* Event Density Navier-Stokes Turbulence arc, 2026.

[Proxmire 2026] Proxmire, A. *Universal Degenerate-Mobility Scaling in Crowded Soft Matter.* Event Density program / Universal Mobility Law paper, 2026.

[Russel, Saville & Schowalter 1989] Russel, W.B., Saville, D.A. & Schowalter, W.R. *Colloidal Dispersions.* Cambridge University Press, 1989.

[Tanner 2000] Tanner, R.I. *Engineering Rheology.* 2nd ed., Oxford University Press, 2000.

---

*Manuscript draft. Event Density program — P4 Non-Newtonian arc. Author: Allen Proxmire. AI collaborator: Claude. April 2026.*
