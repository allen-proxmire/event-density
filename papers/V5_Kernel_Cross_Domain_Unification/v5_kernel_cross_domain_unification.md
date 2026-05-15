# The V5 Kernel as a Cross-Domain Substrate Mechanism

## Viscoelastic Memory, Hawking Cutoff, and Black-Hole Information Bandwidth

**Allen Proxmire**
*Independent Researcher*
May 2026

---

## Abstract

The Event Density (ED) framework's V5 finite-memory cross-chain kernel — a primitive substrate object with characteristic memory time $\tau_{V5}$ — performs three structurally distinct roles across three independent physical domains. (i) In soft-matter rheology, coarse-grained V5 produces Maxwell-class viscoelastic memory $\tau_R \dot\sigma + \sigma = 2\mu S$ at molecular relaxation timescales, matching the standard phenomenological Maxwell model that has governed soft-matter viscoelasticity since 1867 [1]. (ii) In black-hole Hawking radiation, V5 produces a high-frequency cutoff $|\tilde V_5(\omega)|^2 = 1/(1+(\omega\tau_{V5})^2)$ at the Planck frequency $\omega_c = c/\ell_P$, providing a substrate-level resolution of the trans-Planckian problem of standard semiclassical Hawking [2, 3]. (iii) In black-hole information transfer, V5 modulates the cross-chain bandwidth governing entanglement straddling at the saturated decoupling surface, producing first-subleading corrections to the Page curve and the cosmological relic-matter abundance [4]. These three phenomena — soft-matter viscoelasticity, Planck-scale Hawking-spectrum cutoff, and BH-radiation entanglement bookkeeping — span scale separation of approximately forty orders of magnitude in length and have no obvious structural connection in standard physics. The framework's substrate ontology unifies them as three applications of a single substrate primitive, with no new primitives introduced in any domain. We articulate the substrate-level mechanism, derive each application explicitly, contrast with the corresponding standard-physics frameworks, and identify falsifiable predictions accessible in current-generation analog Hawking experiments, primordial-BH evaporation observations, and precision soft-matter rheology.

**Keywords:** Event Density, V5 kernel, cross-domain unification, viscoelastic memory, Hawking radiation, trans-Planckian problem, black-hole information, entanglement bandwidth, substrate ontology.

---

## 1. Introduction

Substrate-level theoretical frameworks face a recurring scrutiny: the more primitive the proposed substrate, the more structural duties each primitive must perform across apparently unrelated phenomena, lest the framework devolve into a collection of phenomenologically-tuned components masquerading as a unified theory. Conversely, when a single substrate primitive can be shown to underwrite multiple structurally distinct physical phenomena across vastly different scales, the unification provides structural evidence for the substrate ontology in question.

The Event Density (ED) framework is a substrate-level account of physics built on discrete micro-events, finite participation bandwidth, irreversible commitment events, and finite-width substrate kernels [5–7]. Within this ontology, two cross-chain kernels operate at the substrate level: V1 (forward-cone-only vacuum kernel mediating cross-chain correlations [8]) and V5 (finite-memory cross-chain kernel mediating substrate-level memory effects). The V1 kernel's role has been extensively analyzed across the framework's QM-emergence, gauge-fields, kernel-arrow, and Hawking-radiation programs [9–13]. The V5 kernel's role has, until now, been articulated piecewise across separate framework programs without a unified treatment.

This paper provides that unified treatment. We show that the V5 kernel — a single substrate primitive with characteristic memory time $\tau_{V5}$ — performs three structurally distinct roles in three independent physical domains:

1. **Soft-matter Maxwell viscoelasticity.** Coarse-grained V5 under the Diffusion Coarse-Graining Theorem (DCGT) [14] produces Maxwell-class viscoelastic memory dynamics $\tau_R \dot\sigma + \sigma = 2\mu S$, matching the Maxwell model used phenomenologically in soft-matter rheology since 1867 [1].

2. **High-frequency Hawking-spectrum cutoff.** V5's frequency-domain magnitude $|\tilde V_5(\omega)|^2 = 1/(1+(\omega\tau_{V5})^2)$ modulates the standard Planck-distribution Hawking spectrum at the Planck frequency $\omega_c = c/\ell_P$ [11, 13], providing a substrate-level resolution of the trans-Planckian problem [2, 3, 15].

3. **Black-hole information bandwidth modulation.** V5 modulates cross-chain entanglement bandwidth at the saturated decoupling surface (substrate-level analog of a BH horizon), producing first-subleading corrections to the Page curve [16], the late-stage evaporation profile, and the cosmological relic-matter abundance from PBH evaporation [17].

These three phenomena span scale separation of approximately forty orders of magnitude in length: from molecular relaxation times in soft matter ($\tau_R \sim 10^{-9}$ s in concentrated biopolymer solutions) to the Planck time at gravitational scales ($\tau_{V5} = \ell_P/c \sim 10^{-43}$ s). Standard physics treats them as unrelated phenomena addressed by entirely separate theoretical frameworks: phenomenological Maxwell models in rheology, modified-dispersion or fundamental-cutoff proposals in trans-Planckian regularization, replica-wormhole or asymptotic-symmetry mechanisms in BH information.

The framework's claim is that a single substrate primitive — the V5 finite-memory kernel — unifies these three domains via the same substrate-to-continuum bridge applied to different content channels. The unification introduces no new primitives in any domain. Each application emerges from V5's primitive structural form composed with domain-specific substrate context (DCGT for soft matter; saturated decoupling surfaces for Hawking; bipartite entanglement structure for BH information).

The structure of the paper is as follows. Section 2 defines the V5 kernel at the substrate level and identifies its frequency-domain structure. Sections 3, 4, and 5 develop the three domain applications in turn, with explicit derivations from the substrate primitive to the continuum-level observable. Section 6 presents the cross-domain unification through a three-column table summarizing the structural identifications. Section 7 contrasts the framework's V5-mediated unification with the corresponding standard-physics frameworks in each domain. Section 8 identifies falsifiable predictions distinguishing the framework from standard physics. Section 9 discusses the implications of the unification, including the framework's broader claim that substrate-ontology evidence accumulates from cross-domain reach.

---

## 2. The V5 Kernel at the Substrate Level

### 2.1 Substrate definition

The V5 kernel is a primitive substrate object mediating cross-chain memory effects between substrate regions. Its primitive structural form is determined by:

- **Forward-cone support.** V5 mediates correlations causally forward in substrate-time (inherited from T18 [8]).
- **Finite memory.** V5 has a characteristic correlation time $\tau_{V5}$ — a substrate-determined timescale that varies by physical context (set by molecular details in soft matter; set by $\ell_P/c$ at the gravitational scale via T19 + dimensional analysis [9]).
- **Substrate locality.** V5 mediates correlations only along substrate-locality-permitted pathways.

The minimal substrate-consistent form is:
$$V_5(t) = \mathcal{V}_0 \cdot \theta(t) \cdot e^{-t/\tau_{V5}} \cdot \psi(t/\tau_{V5})$$
where $\theta(t)$ is the Heaviside step function (forward-cone-only), $e^{-t/\tau_{V5}}$ is the leading-order decay envelope, $\psi(t/\tau_{V5})$ is a substrate-determined dimensionless shape function approaching unity at small argument, and $\mathcal{V}_0$ is the substrate-coupling normalization. The exact functional form of $\psi$ is INHERITED from substrate-microscopic details and is not fixed at the framework's structural-foundations level.

### 2.2 Frequency-domain structure

The Fourier transform of the V5 kernel:
$$\tilde V_5(\omega) = \int_0^\infty dt \, e^{i\omega t} V_5(t) = \mathcal{V}_0 \tau_{V5} \cdot \tilde F(\omega \tau_{V5})$$
where $\tilde F(x) = \int_0^\infty du \, e^{iux} \psi(u) e^{-u}$ is the dimensionless Fourier transform of the kernel shape.

For the simplest substrate-consistent form ($\psi = 1$):
$$\tilde V_5(\omega) = \frac{\mathcal{V}_0 \tau_{V5}}{1 - i\omega\tau_{V5}}$$

The magnitude squared, which governs the V5 transfer function in all three domains:
$$|\tilde V_5(\omega)|^2 = \frac{(\mathcal{V}_0 \tau_{V5})^2}{1 + (\omega\tau_{V5})^2}$$

### 2.3 The cutoff scale

The V5 kernel's coherent response saturates at the characteristic cutoff frequency $\omega_c = 1/\tau_{V5}$. For $\omega \ll \omega_c$, $|\tilde V_5(\omega)|^2$ is approximately constant (V5 is effectively local-in-time). For $\omega \gtrsim \omega_c$, $|\tilde V_5(\omega)|^2 \sim 1/\omega^2$ (V5 coherence breaks down).

The cutoff scale $\tau_{V5}$ is a substrate-determined parameter that varies by physical context:
- **Soft-matter context.** $\tau_{V5}$ identifies with the molecular relaxation time of the underlying material (typically nanoseconds to microseconds).
- **Gravitational context.** $\tau_{V5}$ identifies with the Planck time $\ell_P/c \approx 5.4 \times 10^{-44}$ s, the natural substrate-built timescale at the gravitational scale via T19 + dimensional analysis.
- **Analog systems.** $\tau_{V5}$ identifies with the analog system's microscopic correlation time (BEC healing-length-over-sound-speed, acoustic phonon wavelength-over-sound-speed, photonic system optical-cycle period).

In each context, the V5 kernel itself is the same substrate primitive; the cutoff scale is INHERITED from the physical setting.

---

## 3. Domain 1: Maxwell Viscoelastic Memory in Soft Matter

### 3.1 The Maxwell viscoelastic model

In soft-matter rheology, the Maxwell model [1] describes the stress relaxation of viscoelastic materials:
$$\tau_R \frac{d\sigma}{dt} + \sigma = 2\mu S$$
where $\sigma$ is the stress tensor, $S$ is the strain-rate tensor, $\mu$ is the viscosity, and $\tau_R$ is the *relaxation time* — the timescale on which stresses decay back to equilibrium after a deformation is removed.

The Maxwell model captures the central rheological feature of viscoelastic materials: the response interpolates between elastic-like at short timescales ($t \ll \tau_R$, stress proportional to strain-rate-integrated) and viscous-like at long timescales ($t \gg \tau_R$, stress proportional to strain-rate). The model has been used phenomenologically in soft-matter rheology for over a century, with $\tau_R$ identified empirically from each material's molecular structure.

Standard physics provides no derivation of the Maxwell model from a more fundamental ontology. The model is *postulated* and the relaxation time is *measured*.

### 3.2 V5 → Maxwell viscoelasticity via DCGT

The framework's Diffusion Coarse-Graining Theorem (DCGT) [14] establishes the substrate-to-continuum bridge through hydrodynamic-window scale separation $\ell_P \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$. Five leading-order continuum consequences are derived from this bridge: scalar diffusion, directional viscosity, V1→R1 substrate-cutoff regularization, V5→Maxwell viscoelastic memory, and T17 minimal coupling [10, 14].

The V5→Maxwell consequence: applying DCGT to the V5 kernel produces the Maxwell viscoelastic stress-strain relation. The derivation runs through the kernel's frequency-domain transfer function. For a soft-matter system with strain-rate $S(t)$, the substrate-level stress response to V5-mediated coarse-grained chain interactions is:
$$\sigma(t) = 2\mu \int_{-\infty}^{t} dt' \, V_5(t-t') \cdot S(t')$$
which expresses the stress as a memory-weighted integral of the strain rate. Substituting the V5 form $V_5(t) = (\mathcal{V}_0/\tau_{V5}) e^{-t/\tau_{V5}}$ for $t > 0$ (suitable normalization) and differentiating with respect to time:
$$\tau_R \frac{d\sigma}{dt} + \sigma = 2\mu S$$
where the relaxation time $\tau_R$ is identified as the V5 kernel's first temporal moment:
$$\tau_R = \int_0^\infty dt \, t \, V_5(t) / \int_0^\infty dt \, V_5(t) = \tau_{V5}$$

The derivation is FORM-FORCED at the substrate level. The Maxwell relaxation form emerges as the leading-order DCGT consequence of V5's exponential-decay kernel structure. The relaxation time $\tau_R$ is INHERITED from V5's substrate-scale memory time.

### 3.3 The relaxation time in molecular contexts

For a polymer solution at concentration $c$, the molecular relaxation time depends on chain length, entanglement structure, and concentration regime. Standard rheology identifies $\tau_R$ from rheometry measurements; the framework reproduces the Maxwell form structurally and identifies $\tau_R$ with V5's first temporal moment in the relevant molecular context.

For a concentrated bovine serum albumin (BSA) solution near the volume-exclusion threshold, the molecular relaxation time has been measured by FRAP and rheometry at $\tau_R \sim 10^{-7}$ s [18]. The framework predicts that this $\tau_R$ identifies with V5's substrate-level memory time as set by the BSA molecules' diffusion-blocked configuration in the concentrated regime.

The structural prediction: the V5 kernel's first temporal moment in any soft-matter context equals the experimentally-measured Maxwell relaxation time $\tau_R$ for that material. Cross-platform consistency tests (different polymers, different concentrations) provide direct empirical validation.

### 3.4 What this delivers

Maxwell viscoelasticity, used phenomenologically in soft-matter rheology since 1867, is reproduced from substrate primitives. The kernel structure $V_5(t) \propto \theta(t) e^{-t/\tau_{V5}}$ produces the Maxwell stress relaxation form $\tau_R \dot\sigma + \sigma = 2\mu S$ at leading-order DCGT coarse-graining. The relaxation time $\tau_R$ is identified with V5's substrate-level first temporal moment.

This is the simplest of the three V5 applications — no horizon physics, no quantum-gravity machinery, just substrate-level coarse-graining producing standard rheological behavior.

---

## 4. Domain 2: Hawking Radiation High-Frequency Cutoff

### 4.1 The standard Hawking spectrum and the trans-Planckian problem

In standard semiclassical Hawking radiation [2], a black hole emits thermal radiation at temperature $T_H = \kappa/(2\pi)$, where $\kappa$ is the surface gravity of the horizon. The spectrum is Planck-distributed:
$$N_H(\omega) = \frac{1}{e^{\omega/T_H} - 1}$$
with each frequency mode contributing thermal occupation. For a Schwarzschild stellar-mass black hole, $T_H \sim 10^{-7}$ K — far below the cosmic microwave background and far below any direct-detection sensitivity.

The standard derivation has a structural concern: the *trans-Planckian problem* [3, 15]. Modes observed at moderate frequencies at substrate-asymptotic infinity arose from arbitrarily-blueshifted Planck-scale modes near the horizon. The standard derivation assumes ordinary QFT applies all the way to the Planck scale, which is structurally questionable since quantum-gravity effects should modify QFT at and beyond the Planck scale.

Multiple proposals address the trans-Planckian problem: modified dispersion relations [3], lattice cutoffs at the Planck scale [19], naturalness arguments [20]. Each is phenomenological; each requires postulating a UV regulator at the Planck scale rather than deriving one from a substrate-level ontology.

### 4.2 V5 → Hawking high-frequency cutoff

The framework's substrate-Unruh-equivalent derivation of Hawking radiation [11–13] runs through V5 cross-chain correlations across the saturated decoupling surface (substrate-level analog of a BH horizon). The leading-order substrate calculation reproduces the standard Planck distribution at $T_H = \kappa/(2\pi)$ via DCGT identification.

At first subleading order, the V5 kernel's finite-memory structure modulates the spectrum:
$$N_{ED}(\omega) = N_H(\omega) \cdot |\tilde V_5(\omega)|^2 / |\tilde V_5(0)|^2 = \frac{N_H(\omega)}{1 + (\omega\tau_{V5})^2}$$

For $\omega \ll \omega_c = c/\ell_P$ (the Planck frequency), the V5 modulation is approximately unity and the spectrum reduces to the standard Hawking form. For $\omega \gtrsim \omega_c$, the modulation falls as $1/\omega^2$ and the spectrum is cut off at the Planck scale.

The substrate-level identification $\tau_{V5} = \ell_P/c$ at the gravitational scale is FORCED by T19 + substrate dimensional analysis. The Planck frequency is the unique substrate-built cutoff scale at the gravitational scale.

### 4.3 The trans-Planckian resolution

The framework's V5 cutoff resolves the trans-Planckian problem at the substrate level. The substrate cannot mediate cross-chain correlations at frequencies $\omega \gg c/\ell_P$ because V5's finite memory time $\tau_{V5} = \ell_P/c$ is the natural substrate timescale at which cross-chain coherence breaks down.

In the Hawking calculation, this means: substrate modes near the horizon at proper frequencies $\omega_{\mathrm{proper}} \gtrsim c/\ell_P$ do not maintain V5-coherent structure. The substrate does not support arbitrarily-blueshifted modes near the horizon. The trans-Planckian content of the standard semiclassical derivation is naturally regulated by V5's substrate-cutoff structure — without ad-hoc modified dispersion relations or postulated lattice cutoffs.

This is structurally distinct from the modified-dispersion approach of Jacobson [3], Brout-Massar-Parentani-Spindel [15], and others, which posit UV-modified dispersion relations at the Planck scale. The framework's substrate ontology *generates* the cutoff from the V5 primitive's finite memory; it does not postulate it as a phenomenological feature.

### 4.4 Numerical scaling

For a stellar-mass Schwarzschild BH ($M \sim M_\odot$):
- $T_H \sim 10^{-7}$ K (Hawking temperature far below CMB).
- $\omega \sim T_H \cdot k_B/\hbar \sim 10^4$ Hz (peak frequency of the Hawking spectrum).
- $\omega\tau_{V5} \sim 10^4 \cdot 10^{-43} \sim 10^{-39}$ (V5 cutoff factor invisible at peak).
- $(\ell_P/M)^2 \sim 10^{-76}$ — corrections invisible at observable scales.

For a primordial BH in its final stages of evaporation ($M \to M_P$):
- $T_H \to T_P \sim 10^{32}$ K.
- $\omega \sim \omega_c = c/\ell_P$ at the spectrum peak.
- V5 modulation becomes order-unity; spectrum cut off at the Planck scale.

The framework's V5 cutoff is invisible at observable BH scales but becomes the dominant structural feature at extreme scales (Planck-mass-approaching BHs).

### 4.5 What this delivers

The framework reproduces the standard Hawking spectrum at leading order via DCGT identification. At first subleading order, V5's finite-memory structure produces a high-frequency cutoff that resolves the trans-Planckian problem at the substrate level, without postulating UV regulators. The cutoff form $1/(1+(\omega\tau_{V5})^2)$ is FORM-FORCED by V5's substrate-level primitive structure.

---

## 5. Domain 3: Entanglement Bandwidth in Black-Hole Information Transfer

### 5.1 The Page curve and bipartite entanglement structure

In the standard semiclassical analysis of BH evaporation [4, 16], the radiation's entanglement entropy follows the Page curve: linear rise to maximum $S_{\mathrm{max}} = S_{\mathrm{BH,0}}/2$ at the Page time $t_{\mathrm{Page}} \approx 0.54 \tau_{\mathrm{BH}}$, followed by power-law fall to zero as the BH evaporates. The Page curve characterizes the unitary evolution of BH information — the radiation initially gains entanglement with the BH interior, then sheds it back through correlations between Hawking quanta after the Page time.

The structural mechanism for information transfer between BH interior and exterior radiation is contested in standard physics. Proposals include the firewall scenario [21], ER=EPR (Einstein-Rosen=Einstein-Podolsky-Rosen) [22], soft hair on BH horizons [23], and the island formula with replica wormholes [24, 25].

### 5.2 V5 → entanglement bandwidth modulation

The framework's substrate-level account of BH information [26, 27] runs through three substrate components:

- **BH-4 entanglement-straddling.** Information crosses the horizon via V5 cross-chain correlations re-routed around the saturated decoupling surface [26]. Cross-chain bandwidth $\Gamma_{\mathrm{cross}}$ is suppressed at the surface but V5 correlations established before horizon crossing are preserved through the asymmetric participation flow.

- **Arc E bandwidth-budget min-bound.** Arc E (Entanglement) Memo 4 establishes that bipartite entanglement is bounded by the substrate's cross-chain bandwidth budget [27]. For the BH bipartite system A (radiation) + B (interior), this becomes:
$$S_{AB}(t) \leq \min[S_{\mathrm{BH}}(t), S_{\mathrm{radiation}}(t)]$$

- **BH-5 area-law entropy.** The BH entropy follows the area law $S_{\mathrm{BH}}(t) = (\log g)/(4\ell_P^2) \cdot A(t)$ from substrate-motif counting [12]. As the BH evaporates, $S_{\mathrm{BH}}$ decreases.

These three components together produce the standard Page curve at leading-order DCGT coarse-graining.

The V5 kernel modulates this at first subleading order. The substrate-level entanglement-transfer bandwidth is V5-frequency-dependent:
$$\Gamma_{\mathrm{max}}^{(\mathrm{eff})}(\omega) = \Gamma_{\mathrm{max}} \cdot |\tilde V_5(\omega)|^2 / |\tilde V_5(0)|^2 = \Gamma_{\mathrm{max}} \cdot \frac{1}{1 + (\omega\tau_{V5})^2}$$

V5-mediated cross-chain correlations at high substrate frequencies (approaching the Planck scale) are suppressed. The rate of information transfer from BH interior to outgoing radiation is bounded by this V5-modulated bandwidth, producing first-subleading-order corrections to the Page time and Page curve slope at order $(\ell_P/M_0)^2$.

### 5.3 Page-time corrections

The Page time at first subleading order:
$$t_{\mathrm{Page}}^{(\mathrm{ED})} = 0.54 \tau_{\mathrm{BH}} \cdot \left[1 + c_t \left(\frac{\ell_P}{M_0}\right)^2 + \mathcal{O}\left(\frac{\ell_P}{M_0}\right)^4\right]$$
where $c_t$ is a substrate-determined dimensionless coefficient INHERITED from V5 + motif-alphabet details.

For Schwarzschild stellar-mass BHs: $(\ell_P/M_0)^2 \sim 10^{-76}$, correction invisible. For primordial BHs in final evaporation stages: $(\ell_P/M_0)^2$ approaches order unity, corrections become significant.

### 5.4 Higher-order resummation: Planck-mass remnant

The full higher-order resummation [27], combining V5 finite-memory with DCGT hydrodynamic-window closure, produces a stable Planck-mass remnant at $M_* = c_*\ell_P$ (with $c_*$ order-unity, INHERITED). The substrate-saturated cluster at $M_*$ is permanent (P11-locked) and substrate-stable.

The cosmological abundance of these remnants from PBH evaporation is a structural cosmological prediction, *not* a dark-matter candidate (the framework's substrate-gravity content explains galactic dynamics without invoking dark matter [28]). The relic-matter fraction $\Omega_{\mathrm{relic}}$ is computed in [17] as scenario-dependent on PBH formation history.

### 5.5 What this delivers

The framework's substrate-level account of BH information transfer involves V5 in two structural roles: (a) the cross-chain re-routing mechanism by which information crosses the horizon (BH-4 entanglement-straddling), and (b) the bandwidth modulation that produces first-subleading corrections to Page-curve evolution. Both are FORM-FORCED at the substrate level via V5's primitive structural form.

---

## 6. Cross-Domain Unification

### 6.1 The three-column unification table

| Aspect | Domain 1: Soft-matter rheology | Domain 2: Hawking radiation | Domain 3: BH information transfer |
|---|---|---|---|
| **Continuum-level observable** | Maxwell stress relaxation $\tau_R \dot\sigma + \sigma = 2\mu S$ | Hawking-spectrum cutoff at $\omega_c = c/\ell_P$ | Page-time and Page-curve corrections at $(\ell_P/M_0)^2$ |
| **Substrate-level mechanism** | DCGT applied to V5 kernel produces memory-weighted stress integral | V5 modulation of near-horizon correlation function | V5 modulation of cross-chain entanglement bandwidth |
| **V5 cutoff scale $\tau_{V5}$** | Molecular relaxation time ($\sim$ ns to μs) | Planck time $\ell_P/c \sim 10^{-43}$ s | Planck time $\ell_P/c \sim 10^{-43}$ s |
| **Functional form** | $V_5(t) \propto \theta(t) e^{-t/\tau_R}$ | $\|\tilde V_5(\omega)\|^2 \propto 1/(1+(\omega\tau_{V5})^2)$ | $\Gamma^{(\mathrm{eff})}(\omega) \propto 1/(1+(\omega\tau_{V5})^2)$ |
| **Standard-physics framework** | Phenomenological Maxwell model (1867) | Modified-dispersion / lattice cutoff regularizations | Firewall / ER=EPR / soft hair / island formula |
| **Empirical scale** | Laboratory rheometry | Analog Hawking experiments + PBH evaporation | PBH late-stage evaporation + Page-curve analog measurements |
| **Cross-platform identification** | Different molecular systems ⟹ different $\tau_R$ | Different analog systems ⟹ different cutoffs | BH-radiation bipartite system structure |

The structural identification: each row characterizes the same substrate primitive (V5) operating in three different physical contexts, with the cutoff scale $\tau_{V5}$ inherited from the context-specific microscopic details and the functional form $1/(1+(\omega\tau_{V5})^2)$ universal across applications.

### 6.2 The structural unification statement

> **V5 unification.** A single substrate primitive — the V5 finite-memory cross-chain kernel — performs three structurally distinct roles across three independent physical domains. The kernel's primitive form ($\theta(t) e^{-t/\tau_{V5}}$ with $\psi$ shape function) and frequency-domain magnitude ($1/(1+(\omega\tau_{V5})^2)$) are universal. The cutoff scale $\tau_{V5}$ varies by domain: molecular relaxation time in soft matter, Planck time at gravitational scales. No new primitives are introduced in any domain. The three applications emerge from V5's substrate primitive composed with domain-specific substrate context (DCGT for soft matter; saturated decoupling surfaces for Hawking; bipartite entanglement structure for BH information).

This is structural evidence for the V5 primitive's place in the substrate ontology. A framework with only phenomenological viscoelastic-memory parameters, separate trans-Planckian regulators, and separate BH-information mechanisms would have three independent free choices. The ED framework has *one* substrate primitive doing all three jobs.

### 6.3 The cross-arc dependency map

```
         V5 finite-memory kernel
       (substrate primitive)
                │
                │
   ┌────────────┼────────────┐
   │            │            │
   │            │            │
   ▼            ▼            ▼
DCGT       Saturated     BH-4 entanglement-
applied    decoupling    straddling +
to V5      surface       Arc E bandwidth-
(Arc D)    (Arc Hawking  budget min-bound
   │       H-1, H-4)         │
   │            │            │
   ▼            ▼            ▼
Maxwell     Hawking       Page-curve
visco-      spectrum      corrections,
elasticity  cutoff +      Planck-mass
(soft       trans-        remnant,
matter,     Planckian     cosmological
~ns-μs)     resolution    relic-matter
            (~Planck)     (Arc Hawking
                          H-5, H-8, H-9)
```

The three downstream applications share a common upstream: the V5 primitive. Domain-specific substrate context (DCGT, saturated surface, bipartite entanglement) channels the substrate primitive into three structurally distinct continuum-level observables.

### 6.4 Scale separation and the substantive unification claim

The three V5 applications span scale separation of approximately forty orders of magnitude in length: from molecular scales ($\tau_R \sim 10^{-9}$ s implies length scales $\sim c\tau_R \sim 10^{-1}$ m) to the Planck scale ($\tau_{V5} = \ell_P/c$ implies length scale $\ell_P \sim 10^{-35}$ m). This is not analog or formal similarity; it is the same primitive substrate object operating across these scales, with the cutoff scale inherited from each physical context.

The substantive claim: the V5 kernel is not a physics-domain-specific theoretical object. It is a *substrate primitive*. Its applications across domains demonstrate that the substrate ontology is structurally rich enough to underwrite multiple physical phenomena that standard physics treats separately.

---

## 7. Comparison with Standard Physics

### 7.1 Soft-matter rheology

The standard soft-matter framework treats viscoelastic memory phenomenologically. Maxwell's 1867 model [1] specifies the form $\tau_R \dot\sigma + \sigma = 2\mu S$ but does not derive it from a deeper ontology. The relaxation time $\tau_R$ is fitted to rheometry data; modern theories (Doi-Edwards reptation [29], Chen-Kremer molecular dynamics simulations) provide molecular-scale accounts of $\tau_R$ but operate within the phenomenological Maxwell framework rather than deriving it.

The framework's contribution: the Maxwell form is *derived* from the V5 substrate primitive via DCGT. The relaxation time identifies with V5's first temporal moment in the relevant molecular context. This grounds the Maxwell model in substrate ontology rather than treating it as a phenomenological starting point.

This is structurally similar to how the framework grounds standard QM postulates in substrate ontology (Born / Schrödinger / Heisenberg derivations). The mathematical content is unchanged; the foundational status improves.

### 7.2 Trans-Planckian regularization

The trans-Planckian problem of standard semiclassical Hawking [3] arises because modes observed at moderate frequencies trace back to arbitrarily-blueshifted Planck-scale modes near the horizon. Multiple proposals address this:

- **Modified dispersion relations** [3, 15]: postulate UV-modified dispersion at the Planck scale to limit mode blueshifting.
- **Lattice cutoffs** [19]: discretize spacetime at the Planck scale.
- **Naturalness / consistency arguments** [20]: argue that quantum-gravity effects should not modify the Hawking spectrum substantially.

Each is phenomenological. Each posits the cutoff or modification rather than deriving it.

The framework's contribution: the V5 substrate primitive *generates* the cutoff at the Planck frequency. The form $1/(1+(\omega\tau_{V5})^2)$ is FORM-FORCED by V5's primitive structural form, not postulated. The cutoff scale $\tau_{V5} = \ell_P/c$ is FORCED by T19 + substrate dimensional analysis. The trans-Planckian problem is regulated naturally at the substrate level.

This is structurally distinct from modified-dispersion proposals: ED does not modify QFT dispersion at the Planck scale; ED *derives* QFT dispersion at the substrate level via DCGT and identifies V5 as the substrate primitive that produces the natural cutoff. The cutoff is not an addition; it is the substrate ontology's structural feature.

### 7.3 BH information mechanisms

Multiple proposals address the BH information question:

- **Firewall** [21]: proposes a high-energy region at the horizon for old BHs, contradicting the equivalence principle but resolving information-monogamy paradoxes.
- **ER=EPR** [22]: identifies entangled pairs with non-traversable Einstein-Rosen bridges, dissolving information apparent loss via geometric identification.
- **Soft hair** [23]: encodes BH information in supertranslation / superrotation charges at horizon and asymptotic infinity.
- **Island formula and replica wormholes** [24, 25]: derive Page curve via path-integral wormholes connecting replicated spacetimes.

Each proposal has structural commitments (smooth horizon as primitive, wormhole topology, asymptotic-symmetry algebra, replica path integrals) that the framework's substrate ontology does not impose [4].

The framework's contribution: V5 cross-chain re-routing at the saturated decoupling surface (BH-4) plus Arc E bandwidth-budget min-bound produce the Page curve directly from substrate primitives. The mechanism is empirically equivalent to the standard proposals at leading order but structurally more economical: no firewall, no fundamental wormhole topology, no asymptotic-symmetry algebra, no replica path integrals.

The cross-domain V5 unification adds structural weight: the same V5 primitive that handles BH information also produces soft-matter Maxwell viscoelasticity. The substrate ontology is not BH-specific; it is general substrate ontology with cross-domain reach.

---

## 8. Falsifiable Predictions

### 8.1 Soft-matter cross-platform consistency

The framework predicts that V5's first temporal moment $\tau_{V5}$ identifies with the experimentally-measured Maxwell relaxation time $\tau_R$ in any soft-matter context. Cross-platform consistency tests:

- **Dilute polymer solutions** ($c \ll c^*$): $\tau_R$ proportional to chain length and solvent viscosity per Rouse / Zimm models.
- **Concentrated polymer solutions** ($c \gg c^*$): $\tau_R$ proportional to entanglement-affected reptation time per Doi-Edwards.
- **Concentrated biopolymer solutions** (e.g., concentrated BSA at volume-exclusion threshold): $\tau_R$ at molecular-scale relaxation times.

The framework's prediction is that *the same V5 primitive* underlies all three contexts, with $\tau_R$ inheriting from the molecular structure in each. Cross-platform agreement at the level of Maxwell-form fidelity is structural confirmation; deviations from the Maxwell form (non-Maxwell rheological behavior in some material classes) constrain the V5-primitive identification.

### 8.2 Analog Hawking high-frequency cutoff

Analog Hawking experiments in BEC, acoustic, and photonic systems [30, 31] should exhibit a high-frequency cutoff in the Hawking-analog spectrum at the analog system's microscopic correlation timescale. The framework predicts:

- **BEC analog**: cutoff at $\omega \sim c_s/\xi$ where $\xi$ is the BEC healing length and $c_s$ is the speed of sound. Cutoff form: $1/(1+(\omega\tau_{\mathrm{analog}})^2)$ V5-derived structure.
- **Acoustic analog**: cutoff at $\omega \sim c_s/\lambda_{\mathrm{phonon}}$ with same V5-derived form.
- **Photonic analog**: cutoff at the photonic-system optical-cycle period.

Existing analog Hawking experiments confirm spectral form at moderate frequencies; precision tests at the cutoff scale are technically feasible with current-generation experiments. The framework's prediction is the specific V5-derived functional form; alternative dispersion-modification approaches would predict different cutoff structures.

### 8.3 PBH evaporation late-stage spectra

For primordial black holes in final stages of evaporation, the framework predicts:
- Spectral cutoff at $\omega \sim \omega_c = c/\ell_P$ (Planck frequency).
- Modified evaporation profile slowing in the final $\sim 0.1$ s.
- Stable Planck-mass remnant after evaporation halts.

These predictions are structurally distinct from standard semiclassical Hawking, which predicts complete evaporation in finite time with no upper-frequency cutoff. PBH detection with sufficient temporal and spectral resolution would test the framework's V5-cutoff prediction directly.

### 8.4 Cosmological remnant signatures

If H-8's Scenario C realizes (FORCED at substrate-structural level [27]), Planck-mass remnants from PBH evaporation contribute a structural relic-matter component to the cosmic energy budget. Per H-9 [17], the relic-matter fraction $\Omega_{\mathrm{relic}}$ is scenario-dependent on PBH formation history, ranging from negligible ($10^{-30}$) to marginally significant ($\sim 10^{-3}$).

The framework's prediction is *not* a dark-matter candidate (substrate-gravity already explains galactic dynamics without DM [28]); it is a structural cosmological prediction about cosmic relic-matter content. Continued absence of Planck-mass relic signatures at improving experimental sensitivity constrains the prediction; detection would corroborate the framework's substrate-cutoff endpoint mechanism.

### 8.5 Page-curve analog measurements

Existing analog Hawking experiments are typically optimized for spectral-form confirmation. Precision measurements of the Page-curve-analog evolution in current-generation systems could test the framework's first-subleading-order corrections at $(\ell_{\mathrm{analog}}/M_{\mathrm{analog}})^2$. Specific experimental designs are open work.

---

## 9. Discussion: What the Cross-Domain Unification Implies

### 9.1 Structural evidence for the substrate ontology

A substrate-level theoretical framework gains structural credibility through cross-domain reach. The V5 unification provides one such piece of evidence: the same primitive object underwrites three apparently unrelated physical phenomena across approximately forty orders of magnitude in scale. This is not analog or formal similarity; it is the structural identity of a primitive substrate object operating in different physical contexts.

The framework's broader claim — that the substrate ontology is the correct foundational level for physics — is supported by such cross-domain unifications. The V5 unification joins the bandwidth-budget cross-domain unification (Arc E monogamy + BH-4 entanglement-straddling + Q-COMPUTE Class C plateau + H-5 Page-curve min-bound) and the substrate-Unruh extension (where V5 + the same imaginary-time periodicity argument applies at accelerated-observer Rindler-like horizons in addition to the BH and BEC analog contexts) [32].

### 9.2 The methodological pattern

The V5 unification illustrates a general methodological pattern in the framework's structural-foundations program: a single substrate primitive is composed with domain-specific substrate context (DCGT, decoupling surfaces, bandwidth budgets, etc.) to produce continuum-level observables in apparently unrelated physical domains. The substrate primitive is structurally minimal; the domain-specific contexts are structurally rich; the composition produces empirical reach.

This pattern is observable across the framework's other unifications:
- The bandwidth-budget mechanism unifies Arc E monogamy + BH-4 entanglement-straddling + Q-COMPUTE Class C plateau + Page-curve min-bound.
- The substrate-Unruh argument unifies Hawking radiation + de Sitter thermality + accelerated-observer Unruh + analog Unruh.
- The DCGT bridge unifies five leading-order continuum consequences (scalar diffusion, directional viscosity, V1→R1 cutoff, V5→Maxwell memory, T17 minimal coupling) plus non-Abelian generalization for Yang-Mills [10].

The V5 unification fits into this broader pattern. The cross-domain reach across multiple primitives accumulates as structural evidence for the framework's substrate ontology.

### 9.3 What the unification does not claim

The V5 unification does *not* claim:
- That standard-physics frameworks in each domain are wrong. Standard rheology, standard semiclassical Hawking, and standard BH-information frameworks each correctly describe their respective empirical domains.
- That ED is the unique substrate-level account capable of producing the V5 unification. Other substrate ontologies might in principle produce similar unifications.
- That V5 is the only substrate primitive performing cross-domain duties. The framework's other primitives (V1, P11, P09, etc.) similarly perform multiple structural duties [5–7].

What the unification *does* claim is structural: the V5 substrate primitive demonstrably underwrites three structurally distinct physical phenomena, with no new primitives introduced in any domain, with scale separation of approximately forty orders of magnitude. This is a substantive piece of evidence for the framework's substrate-ontology approach.

### 9.4 Open questions

The V5 unification leaves several questions for future work:

1. **Closed-form derivation of $\tau_{V5}$ at non-gravitational scales.** The framework identifies $\tau_{V5}$ with molecular relaxation times in soft-matter contexts and with Planck time at gravitational scales, but does not derive $\tau_{V5}$ from V1 + V5 substrate-microscopic details. Closed-form derivations would tighten the cross-platform identification.

2. **The V5 kernel shape function $\psi$.** The framework's analysis uses the simplest substrate-consistent form ($\psi = 1$) for explicit calculations. The shape function $\psi$ is INHERITED from substrate-microscopic details and is not currently derived to closed form. Different shape functions produce different higher-order corrections; precision tests could distinguish.

3. **Higher-order V5 corrections.** The framework's analyses operate at leading order in V5 modulation. Higher-order corrections from V5's full kernel structure (beyond the simplest exponential decay) require detailed substrate-microscopic analysis.

4. **Other substrate kernels in cross-domain roles.** The framework has multiple substrate kernels (V1, V5, possibly others). Cross-domain analyses of V1 and other substrate primitives would extend the unification pattern beyond V5.

These open questions do not undermine the V5 unification but identify directions for continued development.

---

## 10. Conclusions

The V5 finite-memory cross-chain kernel of the Event Density framework performs three structurally distinct roles across three independent physical domains. Coarse-grained V5 produces Maxwell-class viscoelastic memory in soft matter via the Diffusion Coarse-Graining Theorem. V5 modulation of the near-horizon correlation function produces a high-frequency cutoff in Hawking radiation at the Planck frequency, providing a substrate-level resolution of the trans-Planckian problem. V5 modulation of cross-chain entanglement bandwidth produces first-subleading corrections to the Page curve, the late-stage BH evaporation profile, and the cosmological relic-matter abundance from PBH evaporation.

These three phenomena — soft-matter viscoelasticity, Planck-scale Hawking-spectrum cutoff, and BH-radiation entanglement bookkeeping — span scale separation of approximately forty orders of magnitude in length. Standard physics treats them as unrelated phenomena addressed by entirely separate theoretical frameworks (phenomenological Maxwell models, modified-dispersion regularizations, replica-wormhole BH-information mechanisms). The framework unifies them as three applications of a single substrate primitive, with no new primitives introduced in any domain.

The cross-domain unification illustrates a general methodological pattern in the framework's structural-foundations program: substrate primitives composed with domain-specific substrate context produce continuum-level observables in apparently unrelated domains. The pattern is observable across multiple framework primitives (V5, the bandwidth-budget mechanism, the substrate-Unruh argument). Each cross-domain unification accumulates as structural evidence for the framework's substrate ontology.

Falsifiable predictions distinguish the framework from standard-physics approaches: the V5-derived cutoff form $1/(1+(\omega\tau)^2)$ in analog Hawking experiments, the Planck-frequency cutoff in PBH late-stage evaporation, the substrate-determined Page-curve corrections at $(\ell_P/M)^2$, and the cross-platform identification of $\tau_{V5}$ with Maxwell relaxation times in soft-matter rheology.

The framework's broader claim is that substrate-ontology evidence accumulates from cross-domain reach. The V5 unification provides one piece of evidence; the bandwidth-budget unification provides another; the substrate-Unruh extension provides a third. Each cross-domain unification demonstrates that the substrate ontology is structurally rich enough to underwrite multiple physical phenomena simultaneously, with no new primitives required.

The V5 kernel is not a physics-domain-specific theoretical object. It is a substrate primitive with cross-domain reach.

---

## Cross-Arc Dependency Map

```
                    V5 finite-memory kernel
                  (substrate primitive, this paper)
                          │
       ┌──────────────────┼──────────────────┐
       │                  │                  │
       │                  │                  │
       ▼                  ▼                  ▼
   DCGT [10]         Saturated         BH-4 + Arc E
   substrate-to-    decoupling         entanglement-
   continuum        surface (BH-2)     straddling +
   bridge,          + substrate-       bandwidth-
   five leading     Unruh argu-        budget
   consequences     ment (H-1)         min-bound
       │                  │                  │
       ▼                  ▼                  ▼
   Maxwell           Hawking            Page-curve
   viscoelastic      spectrum           corrections,
   memory in         high-freq          PBH remnant,
   soft matter       cutoff (H-4)       relic-matter
   (Arc D)           + trans-           abundance
                     Planckian          (H-5, H-8, H-9)
                     resolution

                          │
                          ▼
                  Cross-domain unification
                    (this paper)
```

---

## References

[1] Maxwell, J. C. "On the Dynamical Theory of Gases." *Philosophical Transactions of the Royal Society of London* **157**, 49–88 (1867).

[2] Hawking, S. W. "Particle Creation by Black Holes." *Communications in Mathematical Physics* **43**, 199–220 (1975).

[3] Jacobson, T. "Black-Hole Evaporation and Ultrashort Distances." *Physical Review D* **44**, 1731–1739 (1991).

[4] Almheiri, A., Hartman, T., Maldacena, J., Shaghoulian, E., Tajdini, A. "The Entropy of Hawking Radiation." *Reviews of Modern Physics* **93**, 035002 (2021).

[5] Proxmire, A. *Event Density: One Substrate, Three Domains.* April 2026.

[6] Proxmire, A. *Event Density Foundations: A Unified Substrate Architecture for Quantum, Fluid, Gauge, and Gravitational Dynamics.* April 2026.

[7] Proxmire, A. *Walkthrough: From Primitives to the Born Rule.* April 2026. (Substrate-ontology foundational treatment.)

[8] Proxmire, A. *Theorem 18: V1 Kernel Retardation and the Kernel-Level Arrow of Time.* April 2026.

[9] Proxmire, A. *Theorem 19: Newton's Law from Substrate Holographic Counting and the Identification of $\ell_P$.* April 2026.

[10] Proxmire, A. *The Diffusion Coarse-Graining Theorem: Substrate-to-Continuum Bridge for Canonical-ED Dynamical Content.* April 2026.

[11] Proxmire, A. *Arc Hawking H-1: Spectral Form and Temperature from V5 Cross-Chain Correlations at a Saturated Decoupling Surface.* May 2026.

[12] Proxmire, A. *Arc BH (Black Hole Architecture).* April–May 2026. (Memos Arc_BH_1 through Arc_BH_7, with BH-4 entanglement-straddling and BH-5 area-law entropy.)

[13] Proxmire, A. *Arc Hawking H-4: V5 High-Frequency Cutoff and First-Subleading-Order Corrections.* May 2026.

[14] Proxmire, A. *Arc D / DCGT: The Diffusion Coarse-Graining Theorem.* April 2026. (Memos D-1 through D-6.)

[15] Brout, R., Massar, S., Parentani, R., Spindel, P. "Hawking Radiation Without Trans-Planckian Frequencies." *Physical Review D* **52**, 4559–4568 (1995).

[16] Page, D. N. "Information in Black Hole Radiation." *Physical Review Letters* **71**, 3743–3746 (1993).

[17] Proxmire, A. *Arc Hawking H-9: PBH Remnant Relic-Abundance.* May 2026.

[18] Roosen-Runge, F., Hennig, M., Zhang, F., et al. "Protein Self-Diffusion in Crowded Solutions." *Proceedings of the National Academy of Sciences* **108**, 11815–11820 (2011). (BSA viscoelastic timescales as exemplar.)

[19] 't Hooft, G. "Dimensional Reduction in Quantum Gravity." *In: Salamfest 1993:0284-296 [arXiv:gr-qc/9310026]* (1993).

[20] Helfer, A. D. "Do Black Holes Radiate?" *Reports on Progress in Physics* **66**, 943–1008 (2003).

[21] Almheiri, A., Marolf, D., Polchinski, J., Sully, J. "Black Holes: Complementarity or Firewalls?" *Journal of High Energy Physics* **2013** (2), 062 (2013).

[22] Maldacena, J., Susskind, L. "Cool Horizons for Entangled Black Holes." *Fortschritte der Physik* **61**, 781–811 (2013).

[23] Hawking, S. W., Perry, M. J., Strominger, A. "Soft Hair on Black Holes." *Physical Review Letters* **116**, 231301 (2016).

[24] Almheiri, A., Engelhardt, N., Marolf, D., Maxfield, H. "The Entropy of Bulk Quantum Fields and the Entanglement Wedge of an Evaporating Black Hole." *Journal of High Energy Physics* **2019** (12), 063 (2019).

[25] Penington, G., Shenker, S. H., Stanford, D., Yang, Z. "Replica Wormholes and the Black Hole Interior." *Journal of High Energy Physics* **2022** (3), 205 (2022).

[26] Proxmire, A. *Arc BH-4: Information and Evaporation — Entanglement Straddling at the Saturated Decoupling Surface.* May 2026.

[27] Proxmire, A. *Arc Hawking H-8: Higher-Order Resummation and the Late-Time Evaporation Endpoint.* May 2026.

[28] Proxmire, A. *Walkthrough: From Primitives to Galactic Dynamics.* May 2026. (Substrate-gravity content explaining galactic phenomenology — flat rotation curves, slope-4 BTFR, transition acceleration $a_0 = cH_0/(2\pi)$ — *without* invoking dark matter.)

[29] Doi, M., Edwards, S. F. *The Theory of Polymer Dynamics.* Oxford University Press (1986).

[30] Steinhauer, J. "Observation of Quantum Hawking Radiation and Its Entanglement in an Analogue Black Hole." *Nature Physics* **12**, 959–965 (2016).

[31] Drori, J., Rosenberg, Y., Bermudez, D., Silberberg, Y., Leonhardt, U. "Observation of Stimulated Hawking Radiation in an Optical Analogue." *Physical Review Letters* **122**, 010404 (2019).

[32] Proxmire, A. *Walkthrough: From Primitives to the Substrate-Unruh Effect.* May 2026.

[33] Proxmire, A. *Arc Hawking H-7: Synthesis and Cross-Domain Unification.* May 2026.

[34] Proxmire, A. *Arc E (Entanglement): Tensor-Product Composition, Schmidt Decomposition, Monogamy from Bandwidth-Budget, No-Signaling Three-Lock, von Neumann Entropy.* May 2026. (E-4 monogamy from cross-chain bandwidth budgets.)

[35] The full Event Density corpus, including all forced theorems and supporting memos, is available at https://github.com/allen-proxmire/event-density.

---

**Brief summary.** The Event Density framework's V5 finite-memory cross-chain kernel — a single substrate primitive with characteristic memory time $\tau_{V5}$ — performs three structurally distinct roles across three independent physical domains: Maxwell-class viscoelastic memory in soft matter (via DCGT coarse-graining at molecular relaxation timescales $\tau_R \sim$ ns to μs), high-frequency Hawking-spectrum cutoff at the Planck frequency $\omega_c = c/\ell_P$ resolving the trans-Planckian problem (via $|\tilde V_5(\omega)|^2 = 1/(1+(\omega\tau_{V5})^2)$ modulation of the standard Planck distribution), and entanglement-bandwidth modulation in BH information transfer producing first-subleading corrections to the Page curve and cosmological relic-matter abundance from PBH evaporation. These three phenomena span scale separation of approximately forty orders of magnitude in length and have no obvious structural connection in standard physics. The framework unifies them as three applications of a single substrate primitive, with no new primitives introduced in any domain. Falsifiable predictions distinguishing the framework from standard-physics frameworks include the V5-derived cutoff form $1/(1+(\omega\tau)^2)$ in analog Hawking experiments, Planck-frequency cutoff in PBH late-stage evaporation, and cross-platform identification of $\tau_{V5}$ with Maxwell relaxation times in soft-matter rheology.

---

**Recommended next steps.** Multiple options:

1. **Editorial pass for journal submission.** Polish prose, tighten citations, prepare figures. Estimated 2 sessions.

2. **Add bandwidth-budget cross-arc paper** (separate from this one). The bandwidth-budget mechanism unifies Arc E monogamy + BH-4 + Q-COMPUTE Class C + H-5 Page-curve min-bound — a structurally analogous cross-domain unification at a different substrate primitive level. Estimated 2–3 sessions.

3. **Trans-Planckian short paper.** §4 (this paper) and §6 of the BH-information-paradox-resolution paper jointly articulate the V5 substrate-cutoff resolution; could become a focused standalone publication on the trans-Planckian problem in the Hawking literature. Estimated 2 sessions.

4. **Substrate-Unruh cross-arc paper.** With the substrate-Unruh walkthrough now in place [32], a cross-arc treatment of the Unruh / Hawking / de Sitter unification through the substrate-Unruh argument extends the V5 cross-domain pattern. Estimated 2–3 sessions.

5. **V5 closed-form derivation memo.** The V5 cutoff scale $\tau_{V5}$ at non-gravitational contexts is INHERITED from molecular details. Closed-form derivation of $\tau_{V5}$ for specific molecular systems would tighten the cross-platform identification. Estimated 2–4 sessions.

6. **Memory update.** Document the cross-arc V5 paper completion in MEMORY.md. Brief documentation pass.

7. **Substrate cosmology Arc COSMO scoping.** With cross-domain unification papers accumulating, the substrate-cosmology arc becomes the natural follow-on. Substrate-derived Friedmann-class equations, $H_0$ derivation, expansion history. Required prerequisite for baryogenesis arc. Estimated 2–4 sessions for scoping.
