# Chapter 10 — Soft-Matter Mobility and Non-Newtonian Rheology: UDM, P4-NN, V5

## 10.1 Chapter Overview

Soft-matter rheology — the study of how complex fluids (suspensions, polymer solutions, biological gels, proteins, colloids) flow under stress — is one of the most empirically successful and theoretically fragmented sectors of classical physics. Five canonical families of non-Newtonian fluid behavior have been established phenomenologically: Krieger–Dougherty divergence near jamming, discontinuous shear-thickening (cornstarch-class), Cross-class shear-thinning (ketchup-class), mixed regimes (combinations of the above), and Maxwell-class viscoelasticity (silly putty). Each family has its own constitutive model, its own community, and its own empirical fits. There is no first-principles structural account that explains why these five families exist or why they share any common machinery.

This chapter establishes the substrate-level architectural unification of soft-matter rheology. Two structural commitments produce all five canonical families. **The Universal Mobility Law (UDM)** establishes that mobility in concentrated soft-matter systems takes the form $M(\rho) = M_0(1-\rho/\rho_\mathrm{max})^\beta$ with $\beta \approx 2$, derived from substrate primitive P04 (the bandwidth update rule, applied as the mobility-capacity bound). **The P4-NonNewtonian extension (P4-NN)** generalizes the same architectural principle from concentration-driven mobility to flow-state-variable mobility, producing four of the five families through different applications of P04 to different state variables. The fifth family — Maxwell-class viscoelasticity — comes from **V5 cross-chain memory** under DCGT coarse-graining, producing the standard $\tau_R \dot\sigma + \sigma = 2\mu S$ Maxwell equation with the relaxation time $\tau_R$ identified as V5's first temporal moment.

The chapter integrates UDM and P4-NN with the V5 mechanism into a single architectural account. Empirical validation of UDM's $\beta \approx 2$ exponent across ten chemically unrelated systems — yielding $\beta = 1.72 \pm 0.37$ with $R^2 > 0.986$ in every fit — is the program's most quantitatively-tested structural prediction. Mechanism-clustered scatter (cooperative networks $\bar\beta \approx 2.31$, steric $\approx 1.76$, gradual/electrostatic $\approx 1.38$) is consistent with the substrate-level account's prediction that cooperativity of saturation modulates the exponent. The chapter does not derive specific values of viscosity coefficients, packing limits, critical shear rates, or relaxation times — those are INHERITED from material physics. It establishes the architectural unification of five separately-modeled rheology families under two substrate commitments.

## 10.2 The Soft-Matter Rheology Inventory

### 10.2.1 The five canonical families

Standard soft-matter rheology has accumulated five canonical constitutive-equation families through a century of empirical fitting:

- **Krieger–Dougherty divergence.** For suspensions of solid particles in fluid, viscosity diverges as the particle volume fraction approaches a packing limit:
  ```math
  \mu(\phi) \propto \left(1 - \phi/\phi_\mathrm{max}\right)^{-\beta_\mathrm{KD}}.
  ```
  The exponent $\beta_\mathrm{KD}$ is fit empirically; values near 2 are typical for hard-sphere suspensions.
- **Discontinuous shear-thickening (DST).** Some suspensions (cornstarch in water, certain silica suspensions, body-armor fluids) show a sharp, discontinuous jump in viscosity above a critical shear rate. Below the critical rate the fluid is liquid-like; above it, viscosity rises by orders of magnitude.
- **Cross-class shear-thinning.** Many polymer solutions, ketchup, paint, and biological fluids show monotone decrease of viscosity with shear rate. Cross's phenomenological model fits this with a high-viscosity plateau at low shear, transitioning to a low-viscosity tail at high shear.
- **Mixed regimes.** Some fluids show non-monotone viscosity-shear-rate curves: thinning then thickening, or thickening then thinning. Mixed-regime models are typically constructed by combining Cross-class and DST-class machinery with material-specific transition shapes.
- **Maxwell-class viscoelasticity.** Silly putty, long-chain polymer solutions, and biological gels respond elastically to fast deformations and viscously to slow deformations. The standard Maxwell equation $\tau_R\dot\sigma + \sigma = 2\mu S$ captures this with one parameter (the relaxation time $\tau_R$) that varies by orders of magnitude across systems.

These five families are treated as separate phenomena with separate constitutive equations. Each family has its own community, its own empirical-fit literature, and its own intuition about the underlying mechanism. There is no first-principles account that unifies them.

### 10.2.2 What is missing in the standard treatment

Three structural questions that the standard soft-matter rheology framework does not answer:

- **Why these five families and not others?** Why does the empirical inventory cluster into Krieger–Dougherty, DST, Cross-class, mixed, and Maxwell rather than into some other classification? Standard rheology treats this as an empirical question without structural content.
- **Why do diffusion, suspension viscosity, and shear-thickening share an exponent class?** Empirical exponents in concentration-driven diffusion suppression, Krieger–Dougherty viscosity divergence, and DST critical-rate behavior all cluster near $\beta \approx 2$. Standard rheology treats this as coincidence; the substrate-level analysis does not.
- **What is the structural origin of the relaxation time in Maxwell-class viscoelasticity?** The standard Maxwell model treats $\tau_R$ as a phenomenological fitting parameter. Standard rheology does not derive $\tau_R$ from a substrate-level mechanism.

The substrate-level analysis answers all three. The empirical inventory of five families is structurally exhaustive given two substrate commitments (P04 mobility-capacity bound and V5 cross-chain memory); the shared $\beta \approx 2$ exponent reflects a single substrate principle applied to different state variables; the relaxation time inherits from V5's first temporal moment.

## 10.3 Substrate Inputs: P04 and V5

### 10.3.1 P04 as the mobility-capacity bound

Substrate primitive P04 (Chapter 1, Section 1.4.1) is the bandwidth update rule: participation channels carry bounded bandwidth, and the bandwidth update constrains how much of a chain's available participation capacity can be active at any substrate moment. Applied to soft-matter systems where the substrate is densely populated by participation events, P04 supplies a *mobility-capacity bound*: the rate at which a tagged participation event can move through the system is bounded by the available substrate-channel capacity at each transit step.

The mobility-capacity bound has a specific structural form. As the local participation density $\rho$ approaches the substrate's maximum sustainable density $\rho_\mathrm{max}$, the available channel capacity for new transit events vanishes. The mobility-capacity bound therefore takes a form-FORCED structural form:

```math
M(\rho) = M_0\left(1 - \frac{\rho}{\rho_\mathrm{max}}\right)^\beta
```

with $M_0$ a substrate-determined prefactor (the unconstrained mobility), $\rho_\mathrm{max}$ a substrate-determined packing limit, and $\beta$ a substrate-natural exponent. The substrate-natural value of $\beta$ is 2; the empirical exponent is near 2 with mechanism-clustered scatter (Section 10.4).

### 10.3.2 V5 as the cross-chain memory kernel

Substrate primitive V5 (Chapter 1, Section 1.7.1) is the substrate-level cross-chain memory kernel — a finite-width temporal kernel mediating correlations between distinct chains. V5 is the substrate-level analogue of memory in the system: a participation event at one chain endpoint produces a delayed effect at neighboring chains, with the delay determined by V5's temporal width.

V5's structural role for soft-matter rheology: under DCGT coarse-graining (Chapter 3, Section 3.6.4), V5's finite-width memory produces Maxwell-class viscoelastic dynamics at the continuum level. The continuum equation $\tau_R\dot\sigma + \sigma = 2\mu S$ emerges, with $\tau_R$ identified as V5's first temporal moment. The form is FORCED by DCGT applied to V5; the specific value of $\tau_R$ is INHERITED from V5's specific functional shape and from molecular physics for the system being modeled.

### 10.3.3 Together: P04 + V5 produce all five families

The two substrate commitments produce all five canonical rheology families. P04 produces four (Krieger–Dougherty, DST, Cross-class, mixed regimes) through different applications to different state variables. V5 produces the fifth (Maxwell-class viscoelasticity) through DCGT memory-coarse-graining.

The structural significance: five families that have been treated as five separate problems with five separate constitutive equations turn out to share two substrate commitments. The unification is not partial; it covers the entire canonical inventory of non-Newtonian soft-matter rheology.

## 10.4 The Universal Mobility Law (UDM)

### 10.4.1 The structural derivation

The Universal Mobility Law derives directly from P04's mobility-capacity bound applied to concentration-driven mobility in soft-matter systems. The structural argument:

1. **A tagged participation event** in a soft-matter system (a tracer molecule, a colloidal particle, a polymer segment) moves through a substrate populated by other participation events.
2. **The tagged event's mobility** is bounded above by the available substrate-channel capacity at each transit step.
3. **As local participation density $\rho$ rises**, the available channel capacity falls; mobility decreases.
4. **The functional form of the mobility-capacity bound** is FORCED by P04's structural content: a smooth power-law approach to zero as $\rho \to \rho_\mathrm{max}$:
   ```math
   M(\rho) = M_0\left(1 - \frac{\rho}{\rho_\mathrm{max}}\right)^\beta.
   ```

The form-FORCED content: power-law approach to zero at the packing limit, with substrate-natural exponent $\beta = 2$. The value-INHERITED content: the specific values of $M_0$, $\rho_\mathrm{max}$, and the precise empirical $\beta$ for any given system.

### 10.4.2 Empirical validation across ten systems

UDM has been empirically tested across ten chemically unrelated soft-matter systems in concentration-driven diffusion experiments. The systems span a wide range of microscopic physics:

- PMMA colloids (hard-sphere suspensions)
- Hard-sphere colloids (additional samples)
- Sucrose–water solutions
- Glycerol–water solutions
- BSA protein solutions
- Lysozyme protein solutions
- PEG (polyethylene glycol) in water
- Dextran (polysaccharide) in water
- Casein micelles
- Ludox silica suspensions

Each system has different microscopic physics: different particle types, different interactions, different size ratios, different molecular shapes, different solvent environments. Standard rheology models for these systems are different in each case (Krieger–Dougherty for hard-sphere colloids; Cross-class for polymer solutions; complex hydrodynamic models for protein solutions; etc.).

UDM fits all ten systems with the same functional form $M(\rho) = M_0(1-\rho/\rho_\mathrm{max})^\beta$. The empirical results: $\beta = 1.72 \pm 0.37$ across the ten systems, with $R^2 > 0.986$ in every fit. The canonical ED value is $\beta = 2$; the empirical average sits within one standard deviation of 2.

### 10.4.3 The mechanism-clustered scatter

The empirical $\beta$ values across the ten systems do not all sit at $\beta = 2$; they scatter. The scatter pattern is structurally informative.

Systems where the saturation mechanism involves *cooperative* network effects — hydrogen-bonding viscosity in glycerol, hydrodynamic crowding in dextran, certain protein-solution structures — cluster around $\bar\beta \approx 2.31$. *Above* the canonical value.

Systems where the saturation mechanism is *steric* — hard-sphere colloids, ordinary polymer suspensions, the textbook hard-sphere cases — cluster around $\bar\beta \approx 1.76$. Right at the canonical value.

Systems where the saturation mechanism is *gradual and less cooperative* — polymer entanglement at moderate concentration, electrostatic effects in dilute regime — cluster around $\bar\beta \approx 1.38$. *Below* the canonical value.

The clustering by mechanism is structurally consistent with the substrate-level account. The substrate-natural prediction is that more-cooperative networks should saturate sharper (higher $\beta$) and less-cooperative ones should saturate gentler (lower $\beta$). The empirical data delivers this pattern across the ten-system range. The framework's claim is at the level of *structural coherence* rather than first-principles numerical prediction; the canonical $\beta = 2$ value plus mechanism-clustered scatter is what the substrate-level account predicts and the data confirms.

### 10.4.4 What UDM does and does not deliver

UDM **delivers**:
- The form-FORCED functional shape of mobility-saturation in concentrated soft-matter systems.
- The substrate-natural exponent $\beta = 2$ as the canonical value.
- A structural account of why the exponent class recurs across chemically unrelated systems (the same P04 bound applied to different microscopic physics).
- Empirical validation across ten systems with $\beta = 1.72 \pm 0.37$ and $R^2 > 0.986$.
- Mechanism-clustered scatter consistent with substrate-level predictions about cooperativity.

UDM **does not deliver**:
- Specific numerical predictions of $M_0$ or $\rho_\mathrm{max}$ for any given material. These are INHERITED from material physics.
- A first-principles closed-form derivation of the precise empirical $\beta$ for any single system. The substrate-natural value is 2; the empirical scatter is consistent but not predicted in closed form.
- A complete microscopic theory of any specific soft-matter system. The framework supplies the substrate-level architectural skeleton; the microscopic content is in standard soft-matter physics.

## 10.5 The P4-NonNewtonian Extension (P4-NN)

### 10.5.1 The generalization principle

UDM applies P04's mobility-capacity bound to *concentration-driven* mobility — the bound on mobility as a function of local participation density $\rho$. The P4-NonNewtonian extension generalizes the same architectural principle to *flow-state-variable* mobility — the bound on mobility as a function of dynamical state variables like strain rate, applied stress, or shear deformation.

The generalization is direct. The substrate-level mobility-capacity bound is a structural statement about how the substrate's available channel capacity depends on the local substrate state. When the local substrate state is characterized by participation density (the UDM case), the bound produces the Krieger–Dougherty-class divergence near jamming. When the local substrate state is characterized by other variables — strain rate, applied stress, etc. — the same bound applied to those variables produces other constitutive structures.

The structural content: *one substrate-level bound, multiple state-variable applications, multiple canonical rheology families*. The generalization is form-FORCED by P04's structural content.

### 10.5.2 Krieger–Dougherty divergence (concentration-driven)

The Krieger–Dougherty case is the original UDM application. Volume fraction $\phi$ is the state variable; the substrate-level analysis produces

```math
\mu(\phi) \propto \left(1 - \phi/\phi_\mathrm{max}\right)^{-\beta_\mathrm{KD}}
```

with substrate-natural exponent $\beta_\mathrm{KD}$ near 2 (the same exponent class as UDM, by the same substrate-level structural argument).

### 10.5.3 Discontinuous shear-thickening (strain-rate-driven)

For shear-thickening fluids, the saturation variable is strain rate. The substrate-level mobility-capacity bound, applied to strain rate, produces a discontinuous transition: below a critical strain rate, the substrate's participation network can keep up with the imposed flow and mobility is high; above the critical rate, the network cannot keep up and mobility crashes. The discontinuous-thickening transition is the substrate-level statement that the strain-rate variable has crossed its mobility-capacity threshold.

The structural argument is form-FORCED. The specific value of the critical strain rate, the specific magnitude of the viscosity jump, and the specific cornstarch-versus-silica-versus-body-armor variability are INHERITED from material physics.

### 10.5.4 Cross-class shear-thinning (strain-rate-driven, monotone-decreasing)

For shear-thinning fluids, the saturation variable is again strain rate, but the substrate-level mobility-capacity is approached from the *opposite* direction. At low strain rates the substrate-level participation network is in a high-multiplicity configuration (entangled, structured); applied strain rate breaks down the multiplicity, and the mobility *increases* as the strain rate disrupts the network. The result is monotone-decreasing viscosity with shear rate.

Cross's phenomenological model fits this with a high-viscosity plateau at low shear (the high-multiplicity configuration), transitioning to a low-viscosity tail at high shear (the disrupted-network configuration). The substrate-level account derives the structural form from P04 applied to the strain-rate state variable.

### 10.5.5 Mixed regimes

Some fluids show non-monotone viscosity-shear-rate curves. The substrate-level account reads these as systems with multiple state-variable mechanisms competing: at low shear rates one P04-class mechanism dominates (e.g., shear-thickening), at high shear rates another (e.g., disruption-driven thinning). The mixed-regime model is the substrate-level superposition of two P04 mechanisms.

The structural argument is form-FORCED for the existence of mixed-regime behavior under multiple-mechanism competition. The specific transition shapes and crossover scales are INHERITED.

### 10.5.6 The structural unification of four families

Krieger–Dougherty, DST, Cross-class, and mixed regimes are four canonical non-Newtonian rheology families. The P4-NonNewtonian extension unifies them under a single substrate principle: the mobility-capacity bound P04 applied to different state variables. The structural content:

- **Same substrate primitive** (P04) in all four cases.
- **Different state variables** (volume fraction for KD, strain rate for DST and Cross-class, multiple state variables for mixed regimes).
- **Different functional structures** at the continuum level (divergence for KD, discontinuous jump for DST, monotone decrease for Cross-class, non-monotone for mixed).
- **Common exponent class** $\beta \approx 2$ across diffusion, suspension viscosity, and shear-thickening (when the substrate-level bound applies in directly comparable forms).

The four-family unification is the structural significance of P4-NN. Standard rheology treats KD, DST, Cross-class, and mixed regimes as four separate phenomena requiring four separate constitutive models. The substrate-level analysis identifies them as four projections of a single substrate principle.

## 10.6 Maxwell-Class Viscoelasticity from V5

### 10.6.1 The fifth family and its substrate-level mechanism

Maxwell-class viscoelasticity is the fifth canonical non-Newtonian rheology family. It does not fit the P4-NonNewtonian framework (it is not a P04 mobility-capacity bound applied to a state variable); it requires a separate substrate-level mechanism. The mechanism is V5 cross-chain memory.

V5 is the substrate-level finite-width temporal kernel mediating correlations between distinct chains. Under DCGT coarse-graining (Chapter 3, Section 3.6.4), V5's finite-width memory produces Maxwell-class viscoelastic dynamics at the continuum level. The continuum form:

```math
\tau_R\,\dot\sigma + \sigma = 2\mu S,
```

where $\sigma$ is the stress tensor, $S$ is the strain-rate tensor, $\mu$ is the high-frequency viscosity, and $\tau_R$ is the relaxation time identified as V5's first temporal moment.

### 10.6.2 The structural origin of the relaxation time

The relaxation time $\tau_R$ has been a phenomenological fitting parameter in standard Maxwell-class rheology. The substrate-level reading: $\tau_R$ is V5's first temporal moment — a substrate-level quantity that characterizes V5's memory structure for the system in question.

The form-FORCED content: $\tau_R$ exists as a substrate-level quantity, derivable from V5 under DCGT coarse-graining. The functional form of the Maxwell equation is FORCED. The value-INHERITED content: the specific numerical value of $\tau_R$ is INHERITED from V5's specific functional shape, which in turn depends on material physics for the system being modeled.

For silly putty, $\tau_R$ is on the order of seconds; for long-chain polymer solutions, $\tau_R$ varies from milliseconds to hours; for biological gels, $\tau_R$ depends on the gel's chemical structure. The framework does not predict these specific values; it identifies $\tau_R$ as V5's first temporal moment and derives the Maxwell equation form from V5 under DCGT.

### 10.6.3 Why this matters structurally

Two structural shifts:

- **The Maxwell equation is derived rather than postulated.** Standard rheology treats the Maxwell equation as a phenomenological model (a spring-and-dashpot mechanical analogue). The substrate-level account derives it from V5 cross-chain memory through DCGT coarse-graining.
- **The relaxation time has substrate-level structural origin.** $\tau_R$ is V5's first temporal moment, not just a fitting parameter. The substrate-level structural origin connects the relaxation time to the substrate's memory kernel rather than to any specific microscopic mechanism.

The empirical content of Maxwell-class viscoelasticity does not change; the structural origin of the equation does.

## 10.7 The Unified Soft-Matter Architecture

### 10.7.1 Two substrate commitments, five canonical families

The full architectural unification:

```math
\begin{array}{l|l|l}
\text{Family} & \text{Substrate mechanism} & \text{State variable / mechanism} \\
\hline
\text{Krieger–Dougherty} & \text{P04 mobility-capacity bound} & \text{Volume fraction } \phi \\
\text{Discontinuous shear-thickening} & \text{P04 mobility-capacity bound} & \text{Strain rate (saturating)} \\
\text{Cross-class shear-thinning} & \text{P04 mobility-capacity bound} & \text{Strain rate (disruption)} \\
\text{Mixed regimes} & \text{P04, multi-mechanism} & \text{Multiple state variables} \\
\text{Maxwell viscoelasticity} & \text{V5 cross-chain memory} & \text{Time (memory kernel)} \\
\end{array}
```

The five canonical families share two substrate commitments: P04 (mobility-capacity bound, producing four families through different state-variable applications) and V5 (cross-chain memory, producing the fifth family through DCGT coarse-graining). No additional substrate primitive is required; no phenomenological postulate is required beyond the substrate-level structural content.

### 10.7.2 The shared exponent class

The empirical $\beta \approx 2$ exponent appears in three distinct empirical contexts:

- **Concentration-driven diffusion suppression** in the ten UDM systems ($\beta = 1.72 \pm 0.37$).
- **Krieger–Dougherty viscosity divergence** in suspensions ($\beta_\mathrm{KD}$ near 2).
- **Discontinuous shear-thickening critical-rate behavior** in DST systems (saturation exponent near 2).

All three contexts reflect the same substrate-level mechanism: P04 mobility-capacity bound applied to different state variables. The shared exponent class is structurally significant; standard rheology treats the recurrence of $\beta \approx 2$ as coincidence, while the substrate-level account predicts it as a structural consequence of the shared P04 mechanism.

### 10.7.3 What is not in the unification

Two things that the substrate-level analysis does not cover:

- **Yield-stress fluids** (Bingham plastics, Herschel-Bulkley fluids). These are non-Newtonian fluids that do not flow at all until applied stress exceeds a yield threshold. The yield-stress mechanism is not directly a P04 or V5 phenomenon; it requires an additional structural commitment beyond the two used here. The framework treats yield-stress fluids as outside the scope of UDM + P4-NN + V5 unification.
- **Highly entangled polymer melts** (reptation regimes). The Doi-Edwards reptation model describes polymer-melt rheology in deeply entangled regimes through a different mechanism (tube-confinement and reptation). Whether reptation fits the substrate-level architecture or requires additional substrate commitments is open work.

The framework's coverage is therefore: five canonical non-Newtonian families unified under two substrate commitments (P04 + V5). Yield-stress fluids and deeply entangled polymer melts are flagged as open extensions.

## 10.8 The Universal Mobility Law as Empirical Anchor

### 10.8.1 The PASSED status

UDM is one of the program's three PASSED-status empirical anchors (along with the dwarf-galaxy outer-radius mass discrepancy in Chapter 11 and the multi-timescale FPM relaxation in Chapter 7). The empirical validation across ten chemically unrelated systems with $\beta = 1.72 \pm 0.37$ and $R^2 > 0.986$ is the program's most quantitatively-tested structural prediction.

The PASSED status reflects:
- **The form-FORCED structural content** (the functional form $M(\rho) = M_0(1-\rho/\rho_\mathrm{max})^\beta$ across ten chemically unrelated systems) is empirically confirmed.
- **The substrate-natural exponent $\beta = 2$** is consistent with empirical data within one standard deviation.
- **The mechanism-clustered scatter** (cooperative-network/steric/gradual-electrostatic clustering around 2.31/1.76/1.38) is consistent with the substrate-level account's prediction about cooperativity.

### 10.8.2 What the empirical anchor is and is not

The empirical anchor **is**:
- A cross-system test of the form-FORCED structural content across ten systems with different microscopic physics.
- A quantitatively-tested validation of the substrate-natural exponent class.
- An identification of mechanism-clustered scatter consistent with the substrate-level account's structural predictions.

The empirical anchor **is not**:
- A first-principles derivation of $\beta = 1.72$ from substrate primitives in closed form. The canonical value is $\beta = 2$; the empirical value is consistent with it but not predicted in closed form.
- A complete substrate-level theory of any single soft-matter system. The framework supplies the architectural skeleton; the microscopic content is in standard soft-matter physics.
- A solution to all open soft-matter rheology problems. The framework explicitly leaves yield-stress fluids and deeply entangled polymer melts as open extensions.

### 10.8.3 The FRAP-related extension

A pre-registered extension of the UDM empirical program is the FRAP (Fluorescence Recovery After Photobleaching) measurement at high BSA concentration. FRAP measures recovery dynamics of bleached fluorescent regions in concentrated protein solutions; the substrate-level prediction is a non-Fickian recovery profile with $R(t) \sim t^{1/6}$ scaling at deep concentrations, distinct from the standard Fickian $t^{1/2}$ scaling.

The FRAP-BSA extension is currently in IN PROGRESS status (Chapter 15). A pre-registered protocol has been submitted to a contract lab; quote received April 2026; technician-team review is pending. The empirical content, when available, will provide an additional cross-system test of the substrate-level account.

## 10.9 What This Changes (And What It Doesn't)

### 10.9.1 What does not change

Engineering predictions for soft-matter rheology do not change. Krieger–Dougherty fits the same data; DST occurs in cornstarch at the same critical shear rates; Cross-class fits ketchup the same way; mixed-regime fluids show the same non-monotone curves; silly putty has the same relaxation behavior. Empirical content of soft-matter rheology is preserved exactly.

### 10.9.2 What does change

Three structural shifts:

- **Five separately-modeled rheology families share two substrate commitments.** The standard treatment of KD, DST, Cross-class, mixed, and Maxwell as five separate phenomena is reframed as four projections of P04 plus one projection of V5.
- **The shared $\beta \approx 2$ exponent has a substrate-level explanation.** The recurrence of the exponent class across diffusion, suspension viscosity, and shear-thickening reflects the same P04 mechanism applied to different state variables.
- **The Maxwell relaxation time has a substrate-level origin.** $\tau_R$ is V5's first temporal moment, not a phenomenological fitting parameter.

These three shifts do not change any laboratory prediction. They change the conceptual placement of the five canonical non-Newtonian rheology families and supply structural origins for empirical regularities that standard soft-matter physics treats as phenomenological.

## 10.10 Form-FORCED vs Value-INHERITED at Soft-Matter Mobility

### 10.10.1 What is form-FORCED

- **The Universal Mobility Law functional form** $M(\rho) = M_0(1-\rho/\rho_\mathrm{max})^\beta$.
- **The substrate-natural exponent** $\beta = 2$.
- **The four-family P4-NonNewtonian unification** (KD, DST, Cross-class, mixed regimes from P04 applied to different state variables).
- **The Maxwell-equation form** $\tau_R\dot\sigma + \sigma = 2\mu S$ from V5 cross-chain memory under DCGT.
- **The identification of $\tau_R$ as V5's first temporal moment.**
- **The structural exhaustiveness** of UDM + P4-NN + V5 over the five canonical non-Newtonian rheology families.
- **The mechanism-clustered scatter pattern** (cooperative networks → higher $\beta$; steric → near $\beta = 2$; gradual/electrostatic → lower $\beta$).
- **The substrate origin of the shared $\beta \approx 2$ exponent class** across diffusion, suspension viscosity, and shear-thickening as the same P04 bound applied to different state variables.

### 10.10.2 What is value-INHERITED

- **The specific empirical $\beta$ for any individual system.** Empirical: $\beta = 1.72 \pm 0.37$ across ten systems.
- **The packing limit $\rho_\mathrm{max}$ for any individual system.** Material physics.
- **The unconstrained mobility $M_0$ for any individual system.** Material physics.
- **The critical strain rate** for any individual DST system.
- **The viscosity coefficients** in any specific Cross-class fit.
- **The relaxation time $\tau_R$** for any individual Maxwell-class system. INHERITED from V5's specific functional shape and from molecular physics.
- **Specific transition shapes** in mixed-regime fluids.
- **Microscopic-level molecular details** for any specific soft-matter system.

### 10.10.3 What is open

- **Yield-stress fluids.** Bingham plastics, Herschel-Bulkley fluids, and other yield-stress phenomena are not covered by the UDM + P4-NN + V5 unification. Whether an additional substrate commitment closes them or whether they have a different substrate-level origin is open.
- **Deeply entangled polymer melts.** The Doi-Edwards reptation regime is not directly addressed by UDM. Whether it fits the substrate-level architecture is open.
- **Closed-form derivation of mechanism-clustered scatter.** The empirical clustering pattern is consistent with substrate-level cooperativity predictions, but a closed-form derivation of the specific cluster values is downstream open work.
- **FRAP-BSA empirical confirmation.** The pre-registered protocol's empirical results are pending.

## 10.11 Dependencies

### 10.11.1 Upstream

- **Chapter 1.** Substrate primitives, especially P04 (mobility-capacity bound, the load-bearing primitive for UDM and the four P4-NN families) and the finite-kernel commitment for V5 (the load-bearing primitive for Maxwell-class viscoelasticity).
- **Chapter 2.** Load-bearing invariants. Multiplicity $\mathcal{M}$ enters the mechanism-clustered-scatter analysis (cooperative networks have higher cooperativity at the multiplicity level than steric or electrostatic mechanisms). V5 finite-width memory kernel is established as a load-bearing invariant.
- **Chapter 3.** DCGT. The substrate-to-continuum bridge for V5→Maxwell viscoelasticity is one of DCGT's five leading-order consequences (Chapter 3, Section 3.6.4). The scalar-diffusion content of DCGT (Chapter 3, Section 3.6.1) is the substrate-to-continuum bridge for UDM.

### 10.11.2 Downstream

- **Chapter 14 (Cross-Platform Unifications).** UDM's $\beta \approx 2$ result and the soft-matter architectural unification are part of the program's cross-domain consistency signatures. The form-FORCED / value-INHERITED methodology developed here propagates through Chapter 14.
- **Chapter 15 (Public Test Inventory).** UDM PASSED status across ten systems is one of the program's three PASSED-status empirical anchors, catalogued in Chapter 15. FRAP-BSA IN PROGRESS status is also catalogued.

## 10.12 Canonical Sources

- `papers/Universal_Mobility_Law/`
- `papers/P4_NonNewtonian_Paper_Draft/`

The Universal_Mobility_Law paper presents the publication-grade empirical validation across ten systems, with the canonical form $M(\rho) = M_0(1-\rho/\rho_\mathrm{max})^\beta$ derived from P04 mobility-capacity bound and the empirical results $\beta = 1.72 \pm 0.37$, $R^2 > 0.986$, plus the mechanism-clustered scatter analysis. The P4_NonNewtonian_Paper_Draft presents the architectural extension covering Krieger–Dougherty, DST, Cross-class, mixed regimes, and Maxwell-class viscoelasticity through the unified P04 + V5 substrate commitments.

The Monograph Shell's Appendix A theorem provenance map lists DCGT (Chapter 3) and the V5 finite-width memory kernel as the substrate-level theorems consumed by this chapter. The Notation Glossary in Appendix B lists the symbols used in this chapter (mobility $M$, participation density $\rho$, packing limit $\rho_\mathrm{max}$, exponent $\beta$, relaxation time $\tau_R$, V5 cross-chain memory kernel).

## 10.13 Optional Figures

**Figure 10.1 — The five canonical non-Newtonian rheology families.** A five-row diagram. Each row corresponds to one family (Krieger–Dougherty, DST, Cross-class, mixed regimes, Maxwell-class viscoelasticity). Columns: (i) Standard constitutive equation; (ii) Substrate-level mechanism (P04 mobility-capacity bound applied to which state variable, or V5 cross-chain memory); (iii) Empirical example. The figure makes visible the substrate-level unification of the five families.

**Figure 10.2 — UDM across ten systems.** A scatter plot with mobility ratio on the y-axis and $\rho/\rho_\mathrm{max}$ on the x-axis. Ten curves, one for each empirical system, all fitting the same functional form $M(\rho) = M_0(1-\rho/\rho_\mathrm{max})^\beta$ with system-specific empirical $\beta$ values clustered around $\beta = 1.72 \pm 0.37$. The canonical $\beta = 2$ curve is shown for reference.

**Figure 10.3 — Mechanism-clustered scatter in $\beta$.** A horizontal axis labeled with system mechanisms: cooperative-networks ($\bar\beta \approx 2.31$), steric ($\bar\beta \approx 1.76$), gradual/electrostatic ($\bar\beta \approx 1.38$). The canonical $\beta = 2$ value is marked. The figure makes visible the structural pattern that more-cooperative networks have higher $\beta$ and less-cooperative have lower $\beta$.

**Figure 10.4 — P4-NN as one substrate principle, four state-variable applications.** A radial diagram with P04 at the center and four spokes radiating outward to: (i) Krieger–Dougherty (volume fraction); (ii) DST (strain rate, saturating); (iii) Cross-class (strain rate, disruption); (iv) mixed regimes (multiple state variables). Each spoke is annotated with the state variable used and the resulting constitutive structure. The figure makes visible the single-substrate-principle architecture covering four canonical families.

**Figure 10.5 — V5 to Maxwell viscoelasticity through DCGT.** A flow diagram showing V5 cross-chain memory at the substrate level, DCGT coarse-graining, and the Maxwell equation $\tau_R\dot\sigma + \sigma = 2\mu S$ at the continuum level. The relaxation time $\tau_R$ is identified as V5's first temporal moment.

**Figure 10.6 — The full architectural unification.** A 2x5 grid: left column shows the five canonical families; right column shows the substrate mechanism (P04 for the first four; V5 for the fifth). A central note observes that two substrate commitments produce all five canonical non-Newtonian rheology families.

**Figure 10.7 — Form-FORCED vs Value-INHERITED at soft-matter mobility.** A two-column diagram. Left column ("Form-FORCED"): UDM functional form, substrate-natural $\beta = 2$, four-family P4-NN unification, Maxwell-equation form, $\tau_R$ as V5 first temporal moment, exhaustiveness of UDM + P4-NN + V5 over five canonical families. Right column ("Value-INHERITED"): specific empirical $\beta$ for individual systems, packing limits $\rho_\mathrm{max}$, unconstrained mobilities $M_0$, critical strain rates, viscosity coefficients, relaxation times $\tau_R$.

**Figure 10.8 — The PASSED-status empirical anchor.** A simplified view of UDM's empirical validation: ten chemically unrelated systems, all fitting $M(\rho) = M_0(1-\rho/\rho_\mathrm{max})^\beta$ with $\beta = 1.72 \pm 0.37$, $R^2 > 0.986$. A note observes that this is the most quantitatively-tested structural prediction in the Event Density program.
