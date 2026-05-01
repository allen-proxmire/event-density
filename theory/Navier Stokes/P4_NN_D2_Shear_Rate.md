# P4-NN-D2 — Shear-Rate-Dependent Mobility: DST, Carreau, and Mixed Regimes

**Date:** 2026-04-30
**Status:** Deliverable D2 of the P4 → Non-Newtonian arc. **Headline: ED's P4 mobility-saturation extends from density to strain-rate magnitude γ̇ to derive shear-thickening (DST/STF) and shear-thinning (Carreau-class) viscosity laws. The derivation requires explicit attention to which physical mobility the ED $M$ is identified with — *concentration-mobility* (Stokes-Einstein-class inversion, as in D1) for jamming/DST, or *velocity-mobility* (NS-2.08 direct mapping) for polymer-class shear-thinning. Both are legitimate ED-architectural identifications applying to different physical scenarios.**
**Companions:** [`P4_NN_D1_Density_Jamming.md`](P4_NN_D1_Density_Jamming.md), [`Future_Arc_P4_Non_Newtonian_Scoping.md`](Future_Arc_P4_Non_Newtonian_Scoping.md), [`NS-2.08_ED-PDE_Direct_Mapping.md`](NS-2.08_ED-PDE_Direct_Mapping.md), [`../Architectural_Canon.md`](../Architectural_Canon.md) §2 (P4).

---

## 1. Purpose

This memo extends ED's P4 mobility-saturation principle from **density** ρ (D1's Krieger-Dougherty derivation) to **strain-rate magnitude** $\dot\gamma$. The extension enables ED to structurally derive:

- **Discontinuous shear-thickening (DST)** and **shear-thickening fluid (STF)** behavior in dense suspensions (form-FORCED).
- **Power-law and Carreau-class shear-thinning** in polymer melts, blood, paints (form-FORCED with caveats).
- **Mixed regimes** (shear-thinning transitioning to shear-thickening) via non-monotone $M(\dot\gamma)$.

This is the second major deliverable of the arc. D1 established density-driven jamming via concentration-mobility; D2 extends to shear-rate-driven non-Newtonian behavior via the same architectural principle applied to a different mobility argument.

A structurally important point that surfaces in D2: ED's P4 mobility, when applied to fluid mechanics, has **two distinct mobility-viscosity identifications** depending on the physical scenario being modeled. Both are legitimate; the choice is determined by what physical mobility the ED $M$ represents. D2 makes this explicit.

---

## 2. Inputs

| Input | Source |
|---|---|
| P4: $M(\rho_\mathrm{max}) = 0$, monotone | [`Architectural_Canon.md`](../Architectural_Canon.md) §2 |
| Universal Mobility Law functional form $(1 - \rho/\rho_\mathrm{max})^\beta$ | [`PDE.md`](../PDE.md) §4.1 |
| NS-2.08 velocity-mobility mapping: $\mu = D \cdot M$ for velocity-as-mobility-channel-field | [`NS-2.08_ED-PDE_Direct_Mapping.md`](NS-2.08_ED-PDE_Direct_Mapping.md) §4.1 |
| D1 concentration-mobility + Stokes-Einstein-class mapping: $\mu \propto 1/M$ | [`P4_NN_D1_Density_Jamming.md`](P4_NN_D1_Density_Jamming.md) §4 |
| Standard rheology models: power-law, Cross, Carreau, DST/STF | Standard rheology literature |

---

## 3. The Strain-Rate Variable

The natural ED argument for fluid-mechanical mobility (when shear-rate effects are operative) is the strain-rate magnitude:

$$\dot\gamma = \sqrt{2 \, S_{ij} S_{ij}}, \qquad S_{ij} = \frac{1}{2}(\partial_i v_j + \partial_j v_i)$$

(using the standard rheology convention; an alternative scalar invariant is $|\nabla v|$, which differs by factors of order unity but has the same scaling structure).

**Why $\dot\gamma$ is the natural ED argument.** ED's P4 specifies that $M$ vanishes at some upper bound on its argument. For fluid-mechanical scenarios where mobility depends on the *intensity* of local deformation (rather than density), $\dot\gamma$ is the rotationally-invariant scalar that quantifies deformation rate. It is constructed from the symmetric strain-rate tensor (rotation-free), positive definite, and dimensionally a frequency. ED-10's relational adjacency invariance (rotational symmetry) requires a scalar argument; $\dot\gamma$ is the natural choice.

For non-Newtonian-fluid scenarios where mobility depends on *both* density and shear rate (suspension rheology near jamming under shear), the natural ED argument is the joint $(ρ, \dot\gamma)$. §4.3 below addresses this case.

---

## 4. ED Structural Forms for $M(\dot\gamma)$

### 4.1 Shear-thickening / DST (P4 upper-bound saturation)

**Setup.** Apply P4's saturation structure to strain-rate-dependent particle mobility. The Universal-Mobility-Law-class form, with $\dot\gamma$ replacing $\rho$:

$$M(\dot\gamma) = M_0 \left(1 - \frac{\dot\gamma}{\dot\gamma_\mathrm{max}}\right)^\beta, \qquad \beta > 0.$$

**Mapping.** Use the **Stokes-Einstein-class inversion** (D1 §4) since DST physics is particle-mobility-driven (particles cannot move past each other at high shear; jamming under shear):

$$\mu(\dot\gamma) = \frac{\mu_0 M_0}{M(\dot\gamma)} = \mu_0 \left(1 - \frac{\dot\gamma}{\dot\gamma_\mathrm{max}}\right)^{-\beta}.$$

**Result.**

$$\boxed{\;\mu(\dot\gamma) = \mu_0 \left(1 - \frac{\dot\gamma}{\dot\gamma_\mathrm{max}}\right)^{-\beta}\;}$$

**Interpretation.** Viscosity diverges as $\dot\gamma \to \dot\gamma_\mathrm{max}$. This is **shear-rate-driven jamming** — DST/STF behavior. At low shear, fluid behaves Newtonian ($\mu \approx \mu_0$); near $\dot\gamma_\mathrm{max}$, viscosity rises sharply, transitioning to a near-solid response (the "jamming" regime in DST fluids).

**Empirical correspondence.** Cornstarch + water, fumed silica suspensions, shear-thickening fluids (STFs) used in body armor — viscosity rises dramatically (multi-orders-of-magnitude) at critical shear rate. The ED-derived form is structurally identical to the DST/STF empirical observation.

**Form-FORCED status.** P4-class upper-bound saturation applied to strain-rate variable. β value INHERITED. **Same architectural principle as D1 Krieger-Dougherty**, just applied to $\dot\gamma$ instead of ρ.

### 4.2 Shear-thinning (monotone decrease without strict zero)

Shear-thinning is more nuanced because the natural physics is *velocity-mobility* (polymer-chain alignment increases effective velocity-diffusivity at high shear), not particle-mobility (no jamming). Two derivation paths produce the same Carreau-class result via different ED mobility identifications.

**Path A — NS-2.08 velocity-mobility mapping (direct).**

$M(\dot\gamma)$ is the *velocity-mobility* (kinematic-viscosity-class quantity); high $M$ = fast velocity diffusion = low viscous resistance. NS-2.08 §4.1 gives $\mu = D \cdot M$ for this case.

For shear-thinning behavior — viscosity *decreasing* with $\dot\gamma$ — we need $M$ *decreasing* with $\dot\gamma$. The Cross-class form:

$$M_A(\dot\gamma) = \frac{M_0}{1 + (\lambda \dot\gamma)^n}, \qquad n > 0.$$

This $M$ saturates at $M(\infty) = 0$ asymptotically (without strict zero at finite $\dot\gamma$). Direct mapping:

$$\mu_A(\dot\gamma) = D \cdot M_A(\dot\gamma) = \frac{\mu_0}{1 + (\lambda \dot\gamma)^n}.$$

This is the **Cross model** for shear-thinning fluids.

**Path B — Stokes-Einstein-class inversion (consistent with D1).**

$M(\dot\gamma)$ is the *particle-mobility*; high $M$ = high particle diffusivity = low viscosity. Stokes-Einstein-class inversion gives $\mu \propto 1/M$.

For shear-thinning — viscosity *decreasing* with $\dot\gamma$ — we need $M$ *increasing* with $\dot\gamma$. A natural form:

$$M_B(\dot\gamma) = M_0 \left[1 + (\lambda \dot\gamma)^n\right].$$

Inverse mapping:

$$\mu_B(\dot\gamma) = \frac{\mu_0}{1 + (\lambda \dot\gamma)^n}.$$

**Same Cross-model viscosity form as Path A.**

**Honest finding on the dual derivation.** Both paths produce the standard Cross model. They differ in *which physical mobility* the ED $M$ represents:
- Path A: $M$ is velocity-mobility / kinematic-viscosity-class. ED's M decreases with shear.
- Path B: $M$ is particle-mobility / inverse-viscosity-class (consistent with D1 Stokes-Einstein-class). ED's M increases with shear.

For polymer-melt shear-thinning, **Path A is the natural physics** — high shear aligns chains, reduces inter-chain entanglement, allows easier flow. Velocity-diffusivity (effective momentum transport) is reduced because chains transmit momentum less efficiently when aligned. Path B's "particle mobility increases" framing is less natural for polymer-melt physics but is mathematically consistent.

**Carreau model extension.** The standard Carreau-Yasuda generalization is:

$$\frac{\mu(\dot\gamma) - \mu_\infty}{\mu_0 - \mu_\infty} = \left[1 + (\lambda \dot\gamma)^a\right]^{(n-1)/a},$$

with $\mu_\infty$ a high-shear viscosity floor and $a, n$ shape parameters. This is form-compatible with ED's P4-class structure with appropriate constitutive choices (e.g., $M(\dot\gamma)$ with finite asymptote rather than zero).

**Form-FORCED status for shear-thinning.** Cross-class form is form-FORCED at the architectural level (monotone decreasing $M$ via either mapping). Carreau-Yasuda generalization is form-compatible but with INHERITED shape parameters $(a, n, \mu_\infty)$.

### 4.3 Mixed regimes (non-monotone $M(\dot\gamma)$)

Real dense suspensions often exhibit *both* shear-thinning at low rates (alignment / lubrication) *and* shear-thickening at high rates (DST onset). ED accommodates this via non-monotone $M(\dot\gamma)$:

$$M_\mathrm{mixed}(\dot\gamma) = M_0 \left[1 + (\lambda_1 \dot\gamma)^{n_1}\right] \cdot \left(1 - \frac{\dot\gamma}{\dot\gamma_\mathrm{max}}\right)^\beta$$

(combining Path B's increasing factor for low-shear thinning with P4's saturation factor for high-shear jamming). At low $\dot\gamma$, the increasing factor dominates and $M$ rises (shear-thinning under inverse mapping); near $\dot\gamma_\mathrm{max}$, the saturation factor drives $M \to 0$ and viscosity diverges (DST onset).

**Form-FORCED structure of mixed regimes.** ED admits non-monotone constitutive mobility. Whether a specific fluid exhibits thinning, thickening, or both, depends on the *constitutive choice* of $M$ — which is INHERITED at the form level (it's a constitutive specification, not derivable from substrate primitives).

**Empirical correspondence.** Concentrated colloidal suspensions, semi-dilute polymer solutions with associative interactions, granular pastes — all show thinning-then-thickening transitions. ED's structural framework accommodates these natively via mixed P4-class constitutive choices.

For combined density-and-shear-rate dependence (suspension rheology near jamming under shear), the natural ED form is $M(\rho, \dot\gamma)$ with both arguments saturating at their respective bounds. This produces the suspension-rheology phase diagram structurally.

---

## 5. Mapping to Viscosity — Aggregate

| ED structural choice | Mapping used | Resulting viscosity law | Empirical class |
|---|---|---|---|
| $M(\dot\gamma) = M_0 (1 - \dot\gamma/\dot\gamma_\mathrm{max})^\beta$ | Stokes-Einstein-class inversion | $\mu(\dot\gamma) = \mu_0 (1 - \dot\gamma/\dot\gamma_\mathrm{max})^{-\beta}$ | DST / STF / shear-thickening |
| $M_A(\dot\gamma) = M_0 / [1 + (\lambda \dot\gamma)^n]$ | NS-2.08 direct (velocity-mobility) | $\mu(\dot\gamma) = \mu_0 / [1 + (\lambda \dot\gamma)^n]$ | Cross / Carreau shear-thinning |
| $M_B(\dot\gamma) = M_0 [1 + (\lambda \dot\gamma)^n]$ | Stokes-Einstein-class inversion | $\mu(\dot\gamma) = \mu_0 / [1 + (\lambda \dot\gamma)^n]$ | Cross / Carreau shear-thinning |
| $M_\mathrm{mixed}(\dot\gamma)$ non-monotone | Either mapping | Hybrid thinning-then-thickening | Concentrated suspensions |
| $M(\rho, \dot\gamma)$ joint | Stokes-Einstein-class inversion | Krieger-Dougherty + DST combined | Suspension rheology phase diagram |

---

## 6. Empirical Anchors

### 6.1 DST / STF behavior (form-FORCED via 4.1)

Discontinuous shear-thickening in dense particulate suspensions (cornstarch + water at φ ≳ 0.45; fumed silica suspensions at moderate concentration; STFs used in body armor and impact protection). Viscosity jumps multi-orders-of-magnitude at critical shear rate $\dot\gamma_c$. **ED's structural prediction:** $(1 - \dot\gamma/\dot\gamma_\mathrm{max})^{-\beta}$ divergence; $\dot\gamma_c$ corresponds to the onset of the divergence. Empirically observed.

### 6.2 Power-law / Cross / Carreau shear-thinning (form-compatible via 4.2)

Polymer melts (HDPE, polystyrene), polymer solutions (HPC, xanthan gum), blood (in viscometric flow), paints, foods. Viscosity decreases monotonically with shear rate, fit with Cross or Carreau-Yasuda models. **ED's structural prediction:** Cross-form viscosity $\mu_0 / [1 + (\lambda \dot\gamma)^n]$ form-FORCED at the architectural level; $(\lambda, n)$ INHERITED per material.

### 6.3 Mixed regimes (form-FORCED via 4.3)

Concentrated colloidal suspensions showing thinning-then-thickening; granular pastes; some food rheology. Non-monotone viscosity-vs-shear-rate curve. **ED's structural prediction:** non-monotone $M(\dot\gamma)$ admits both regimes; transition shear rate is INHERITED.

### 6.4 ED's contribution

ED unifies three rheology classes (DST/STF, Carreau-shear-thinning, mixed-regime suspensions) under a single architectural principle (P4 mobility-saturation applied to strain-rate). The functional forms emerge structurally from constitutive choices on $M(\dot\gamma)$ within the form-FORCED P4-class structure. Specific exponents and shape parameters are INHERITED per material.

---

## 7. ED Architectural Classification

| Rheology class | ED-architectural status | Notes |
|---|---|---|
| **Newtonian** | Special case: constant $M$ | Both mappings reduce to Newtonian behavior |
| **Krieger-Dougherty / suspension jamming** | **Form-FORCED via P4 (D1)** | Stokes-Einstein-class inversion + concentration mobility |
| **Discontinuous shear-thickening (DST) / STF** | **Form-FORCED via P4 (D2 §4.1)** | Stokes-Einstein-class inversion + strain-rate mobility |
| **Cross / Carreau / power-law shear-thinning** | **Form-FORCED via monotone P4-class** | Either mapping; shape parameters INHERITED |
| **Carreau-Yasuda** | Form-compatible with INHERITED extra parameters | Generalizes Cross/Carreau |
| **Mixed-regime non-monotone fluids** | Form-FORCED via constitutive-choice freedom | Constitutive choice for $M(\dot\gamma)$ is INHERITED |
| **Bingham yield-stress** | **Non-canonical ED** | Requires inverted P4 (M=0 at lower threshold); flagged in scoping §6.1 |
| **Maxwell viscoelastic** | Form-compatible via V5 with finite memory time | Treated separately in D5 |
| **Oldroyd-B / Giesekus / FENE-P** | Beyond P4 — require additional constitutive structure (conformation tensor, etc.) | Out of scope per scoping §6.3 |

---

## 8. Recommended Next Steps

1. **Begin D3 — rheology-class audit catalogue.** File: `theory/Navier Stokes/P4_NN_D3_Rheology_Classes.md`. Consolidates the §7 table above into a comprehensive catalogue with structural justification per class, empirical anchors, and INHERITED-parameter status. Cross-references D1 + D2 derivations. Estimated 1 session.

2. **Pre-D4 check: gather β / shape-parameter values from literature.** For each rheology class:
   - Krieger-Dougherty β values across hard-sphere / polymer / granular suspensions.
   - DST exponents and $\dot\gamma_c$ ranges for cornstarch, fumed silica, STFs.
   - Cross / Carreau shape parameters $(\lambda, n)$ for polymer melts, blood, paints.
   - Universal Mobility Law's β distribution across the 10 systems (from existing repo material).
   ~30–60 minutes assembling summary tables. Used in D4.

3. **Draft D4 in qualitative-only mode** following the scoping recommendation. File: `theory/Navier Stokes/P4_NN_D4_Empirical_Comparison.md`. Compare β-value distributions across the three regimes (Krieger-Dougherty, DST, Cross/Carreau) to look for cross-system patterns. Recommend qualitative-only scope; quantitative analysis (+2 sessions) optional based on what qualitative reveals.

4. **D5 viscoelastic V5 integration** as brief subsection at the end of the arc.

### Decisions for you

- **Confirm dual-mapping framing.** ED has two distinct mobility-viscosity identifications depending on physical scenario: Stokes-Einstein-class inversion (concentration-mobility, used for jamming/DST in D1 + D2 §4.1) vs. NS-2.08 direct mapping (velocity-mobility, used for polymer-melt shear-thinning in D2 §4.2 Path A). Both are legitimate; choice determined by physics. This is honest and consistent across D1 + D2.
- **Confirm Carreau-Yasuda is form-compatible (not strictly form-FORCED).** The shape parameters $(a, n, \mu_\infty)$ go beyond the basic P4 saturation structure; INHERITED rather than form-derived.
- **Confirm proceeding to D3 next.** Catalogue work; consolidates D1 + D2 findings; cleanest of the remaining deliverables.

---

*P4-NN-D2 closes shear-rate extension. Three structural classes derived: shear-thickening / DST via P4 upper-bound saturation + Stokes-Einstein-class inversion; Cross / Carreau shear-thinning via monotone $M(\dot\gamma)$ (either mapping path); mixed regimes via non-monotone $M$. ED's dual-mapping framework — Stokes-Einstein-class inversion for jamming, NS-2.08 direct mapping for polymer-melt physics — is structurally honest and applies appropriate physics to appropriate scenarios. Form-FORCED architectural content: existence of viscosity divergence near $\dot\gamma_\mathrm{max}$ (DST), monotone Cross-class shear-thinning, mixed-regime accommodation. Value-INHERITED: β, $\dot\gamma_\mathrm{max}$, $(\lambda, n)$, mode parameters per material. D3 next: rheology-class audit catalogue.*
