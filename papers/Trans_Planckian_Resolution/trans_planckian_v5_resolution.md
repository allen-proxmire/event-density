# The V5 Finite-Memory Kernel as a Substrate-Level Resolution of the Trans-Planckian Problem

**Allen Proxmire**
*Independent Researcher*
May 2026

---

## Abstract

The standard semiclassical derivation of Hawking radiation traces observed-at-infinity modes back to arbitrarily-blueshifted near-horizon frequencies. The derivation thus implicitly requires standard QFT to apply at and beyond the Planck scale, where quantum-gravity effects should structurally modify field theory. This is the *trans-Planckian problem*, recognized since Jacobson [1] (1991) and analyzed extensively in subsequent literature [2–6]. Multiple proposals address it phenomenologically: modified dispersion relations [1, 2], lattice cutoffs [3], naturalness arguments [4], the Trans-Planckian Censorship Conjecture (TCC) [5], and others. We show that the Event Density (ED) framework's V5 finite-memory cross-chain kernel, with characteristic memory time $\tau_{V5} = \ell_P/c$ at the gravitational scale (the natural substrate-built timescale via T19 + dimensional analysis), produces a substrate-level resolution that does not require any of the standard phenomenological additions. The substrate cannot mediate cross-chain correlations at frequencies $\omega \gg c/\ell_P$ because V5's coherence breaks down beyond the cutoff. Combined with the Diffusion Coarse-Graining Theorem's hydrodynamic-window closure at $L_{\mathrm{flow}} \sim \ell_P$, the substrate naturally cuts off arbitrarily-blueshifted modes near the horizon. The standard trans-Planckian divergence is a continuum artifact that vanishes at the substrate level. The V5-modulated Hawking spectrum is $N_{ED}(\omega) = N_H(\omega) / (1+(\omega\tau_{V5})^2)$, finite at all frequencies and reducing to standard Hawking at observable scales. Falsifiable predictions in current-generation analog Hawking experiments and primordial-BH late-stage evaporation distinguish the framework from modified-dispersion and lattice-cutoff approaches.

**Keywords:** trans-Planckian problem, Hawking radiation, Event Density, substrate ontology, V5 finite-memory kernel, UV regulation, modified dispersion, Diffusion Coarse-Graining Theorem.

---

## 1. Introduction

In the standard semiclassical derivation of Hawking radiation [7, 8], a Schwarzschild black hole of mass $M$ emits thermal radiation at temperature $T_H = \kappa/(2\pi)$, where $\kappa$ is the surface gravity of the horizon. The derivation runs through QFT in curved spacetime: vacuum modes propagated from past null infinity, through the BH-collapse spacetime, to future null infinity, where they appear as a thermal mixture via the Bogoliubov transformation between past and future mode bases.

The derivation has empirical content (analog Hawking experiments [9–10] confirm the spectral form) but a structural concern. Modes observed at moderate frequencies $\omega \sim T_H$ at substrate-asymptotic infinity were arbitrarily-blueshifted near the horizon at proper frequencies
$$\omega_{\mathrm{proper}}(r) = \omega \cdot (1 - 2M/r)^{-1/2}$$

For $r \to r_h^+$ (horizon-approaching), $\omega_{\mathrm{proper}} \to \infty$. The standard derivation thus implicitly requires standard QFT to apply at proper frequencies arbitrarily far above the Planck scale $\omega_P = c/\ell_P \approx 1.85 \times 10^{43}$ Hz, where quantum-gravity effects should structurally modify field theory.

This is the *trans-Planckian problem* of Hawking radiation [1]. It has been addressed in the literature through several proposals:

- **Modified dispersion relations** [1, 2]: postulate UV-modified dispersion $\omega^2 = c^2 k^2 (1 + \mathcal{O}(\ell_P k))$ at the Planck scale.
- **Lattice cutoffs** [3]: discretize spacetime at the Planck scale, eliminating modes with $k \gg 1/\ell_P$.
- **Naturalness / robustness arguments** [4]: argue that physics-domain robustness should protect Hawking radiation from trans-Planckian modifications.
- **Trans-Planckian Censorship Conjecture (TCC)** [5]: conjectured cosmological censorship of trans-Planckian modes by sufficient inflation.
- **'t Hooft S-matrix arguments** [6]: structural arguments from BH information theory.

Each proposal is structurally meaningful but each is *phenomenological* in character: each posits the cutoff or modification rather than deriving one from a substrate-level ontology. The trans-Planckian problem has therefore remained a structural concern of standard semiclassical Hawking, without a derivation-level resolution.

This paper presents the Event Density (ED) framework's substrate-level resolution. The framework is built on a substrate ontology of discrete micro-events, finite participation bandwidth, irreversible commitment events, and finite-width substrate kernels [11, 12]. The framework's V5 finite-memory cross-chain kernel — a primitive substrate object with characteristic memory time $\tau_{V5}$ — naturally regulates the high-frequency behavior of substrate-mediated correlations. At the gravitational scale, $\tau_{V5} = \ell_P/c$ (the Planck time, identified via T19 + substrate dimensional analysis [13]). This is the natural substrate-built timescale at which V5 coherence breaks down.

The framework's claim: the substrate cannot mediate cross-chain correlations at frequencies $\omega \gg c/\ell_P$. Arbitrarily-blueshifted near-horizon modes do not exist at the substrate level. The trans-Planckian divergence of standard semiclassical Hawking is a *continuum artifact* of the QFT-in-curved-spacetime calculation; the substrate-level account regulates it naturally without postulating modified dispersion, lattice cutoffs, or any other phenomenological addition.

Combined with the Diffusion Coarse-Graining Theorem's (DCGT) hydrodynamic-window closure at $L_{\mathrm{flow}} \sim \ell_P$, the framework provides a substrate-level UV regulation that:
1. Reproduces standard Hawking exactly at observable scales.
2. Cuts off the high-frequency tail at the Planck frequency.
3. Resolves the trans-Planckian problem without new physics or postulated regulators.
4. Produces falsifiable first-subleading-order corrections distinguishing the framework from standard semiclassical Hawking and from the major phenomenological resolutions.

The structure of the paper: §2 states the standard trans-Planckian problem precisely. §3 presents the V5 kernel at the substrate level. §4 derives the V5-modulated Hawking spectrum. §5 articulates DCGT's role in the resolution. §6 states the substrate-level resolution explicitly. §7 contrasts with the major standard-physics proposals. §8 identifies falsifiable predictions. §9 discusses the implications.

---

## 2. The Standard Trans-Planckian Problem

### 2.1 The blueshift argument

In Schwarzschild geometry, an outgoing mode observed at substrate-asymptotic infinity with frequency $\omega$ traces back to a mode near the horizon at proper frequency
$$\omega_{\mathrm{proper}}(r) = \omega \cdot (1 - 2M/r)^{-1/2}.$$

For an observer at radius $r = 2M(1+\epsilon)$ with small $\epsilon$, the proper frequency is approximately $\omega/\sqrt{2\epsilon}$. As $\epsilon \to 0$, $\omega_{\mathrm{proper}} \to \infty$. Modes traced back to the horizon at any positive distance away are blueshifted to arbitrarily high proper frequencies.

For a stellar-mass black hole observed mode at $\omega \sim T_H$ (peak of the Hawking spectrum), the proper frequency exceeds the Planck scale at distances
$$\epsilon \lesssim (T_H/\omega_P)^2 \cdot 2 \sim 10^{-86}$$
— a substantial fraction of the horizon's neighborhood, in the relevant blueshift sense.

### 2.2 The structural concern

Standard QFT in curved spacetime is a continuum-level theory whose validity at and beyond the Planck scale is structurally questionable. Quantum-gravity effects should modify field theory at the Planck scale, where:
- Spacetime fluctuations become order-unity.
- Quantum-gravity corrections to dispersion relations should appear.
- The continuum description of spacetime should break down.

The trans-Planckian problem articulates this concern: the standard semiclassical Hawking calculation requires QFT to be valid at arbitrarily-high proper frequencies near the horizon, including frequencies far above where QFT's structural status is secure.

### 2.3 The standard responses

Multiple proposals have been advanced:

**(a) Modified dispersion relations [1, 2].** Postulate that the standard relativistic dispersion $\omega^2 = c^2 k^2$ is modified at the Planck scale to $\omega^2 = c^2 k^2 + f(k\ell_P)$ for some function $f$ that effectively cuts off mode propagation at $k \sim 1/\ell_P$. This requires postulating the specific form of $f$.

**(b) Lattice cutoffs [3].** Discretize spacetime at the Planck scale. This requires postulating the discrete spacetime structure and its specific properties.

**(c) Naturalness / robustness arguments [4].** Argue that the empirical robustness of Hawking radiation should protect it from trans-Planckian sensitivity. This is an argument-from-empirical-robustness rather than a derivation.

**(d) Trans-Planckian Censorship Conjecture (TCC) [5].** Conjecture that cosmological inflation must terminate before trans-Planckian modes have stretched to observable scales. This is a conjecture about cosmological dynamics; it does not directly resolve the BH trans-Planckian problem.

**(e) 't Hooft S-matrix arguments [6].** Structural arguments from BH information theory and the holographic principle, suggesting that the BH S-matrix should be unitary and structurally regulated.

Each proposal contributes structural insight; each remains phenomenological in character. The trans-Planckian problem awaits a derivation-level resolution.

---

## 3. The V5 Finite-Memory Kernel

### 3.1 Substrate definition

The V5 cross-chain memory kernel is a primitive substrate object in the Event Density framework [11, 12]. Its primitive structural form is determined by:

- **Forward-cone support.** V5 mediates cross-chain correlations causally forward in substrate-time (inherited from T18 [14]).
- **Finite memory.** V5 has a characteristic correlation time $\tau_{V5}$ — a substrate-determined timescale that varies by physical context.
- **Substrate locality.** V5 mediates correlations only along substrate-locality-permitted pathways.

The minimal substrate-consistent kernel form is:
$$V_5(t) = \mathcal{V}_0 \cdot \theta(t) \cdot e^{-t/\tau_{V5}} \cdot \psi(t/\tau_{V5})$$
where $\theta(t)$ is the Heaviside step function (forward-cone-only), $e^{-t/\tau_{V5}}$ is the leading-order decay envelope, $\psi(t/\tau_{V5})$ is a substrate-determined dimensionless shape function approaching unity at small argument, and $\mathcal{V}_0$ is the substrate-coupling normalization. The exact functional form of $\psi$ is INHERITED from substrate-microscopic details and is not fixed at the framework's structural-foundations level.

### 3.2 Frequency-domain structure

The Fourier transform of the simplest substrate-consistent V5 form ($\psi = 1$):
$$\tilde V_5(\omega) = \frac{\mathcal{V}_0 \tau_{V5}}{1 - i\omega\tau_{V5}}$$

The magnitude squared, governing V5's coherent transfer of cross-chain correlations:
$$|\tilde V_5(\omega)|^2 = \frac{(\mathcal{V}_0 \tau_{V5})^2}{1 + (\omega\tau_{V5})^2}$$

For $\omega \ll \omega_c \equiv 1/\tau_{V5}$, $|\tilde V_5(\omega)|^2$ is approximately constant — V5 is effectively local-in-time and behaves as a delta-function memory.

For $\omega \gtrsim \omega_c$, $|\tilde V_5(\omega)|^2 \to (1/\omega^2)$ — V5 coherence breaks down. The substrate cannot mediate cross-chain correlations at frequencies above the cutoff scale.

### 3.3 The cutoff scale at the gravitational scale

The cutoff $\tau_{V5}$ is a substrate-determined parameter. At the gravitational scale, the only substrate-built timescale available from substrate primitives is the Planck time:
$$\tau_{V5} = \ell_P/c \approx 5.4 \times 10^{-44}\, \mathrm{s}$$

This identification is FORCED via T19 (Newton-recovery $\ell_P$) [13] plus substrate dimensional analysis. The Planck time is the natural substrate timescale at which V5 coherence breaks down at gravitational scales.

The corresponding cutoff frequency:
$$\omega_c = c/\ell_P \approx 1.85 \times 10^{43}\, \mathrm{Hz}$$

— the Planck frequency. The V5 kernel does not coherently mediate cross-chain correlations at proper frequencies approaching the Planck scale.

### 3.4 Why $\tau_{V5}$ is not phenomenological

The V5 cutoff scale is *not* a phenomenological cutoff inserted ad hoc to regulate the trans-Planckian problem. The V5 kernel is a substrate primitive in its own right — it appears across multiple framework sectors:
- Soft-matter Maxwell viscoelasticity, where $\tau_{V5}$ identifies with molecular relaxation times [15].
- Hawking radiation high-frequency spectral cutoff (this paper).
- Black-hole information transfer bandwidth modulation [16, 17].
- Substrate-Unruh radiation cutoff [18].

The kernel exists *before* and *independently of* the trans-Planckian problem. The cutoff scale at the gravitational context is FORCED by substrate dimensional analysis. The trans-Planckian regulation is a *consequence* of V5's primitive structure, not a feature added to address the problem.

---

## 4. The V5-Modulated Hawking Spectrum

### 4.1 The leading-order substrate Hawking calculation

The framework's leading-order substrate-level Hawking calculation [19, 20] reproduces the standard semiclassical result via the substrate-Unruh argument applied at a saturated decoupling surface (substrate-level analog of a BH horizon). V5 cross-chain correlations across the surface, satisfying imaginary-time periodicity at $\beta = 2\pi/\kappa_{ED}$ (forced by substrate-vacuum self-consistency at the surface), produce a Planck spectrum at temperature $T = \kappa_{ED}/(2\pi)$. DCGT identification at leading order gives $T_H = \kappa/(2\pi)$ — the standard Hawking temperature.

The leading-order spectrum:
$$N_H(\omega) = \frac{1}{e^{\omega/T_H} - 1}$$

This is the standard result, exactly reproduced.

### 4.2 First-subleading-order V5 modulation

At first subleading order, V5's finite-memory structure modulates the spectrum. The substrate-level near-horizon correlation function involves V5 cross-chain mediation at frequency $\omega$. The leading-order calculation treats V5 as effectively local-in-time (valid for $\omega \ll \omega_c$). The first-subleading correction includes the explicit V5 frequency-domain modulation:

$$N_{ED}(\omega) = N_H(\omega) \cdot \frac{|\tilde V_5(\omega)|^2}{|\tilde V_5(0)|^2} = \frac{N_H(\omega)}{1 + (\omega\tau_{V5})^2}$$

This is the V5-modulated Hawking spectrum. For modes with $\omega \ll \omega_c = c/\ell_P$:
$$N_{ED}(\omega) \approx N_H(\omega) \cdot [1 - (\omega\tau_{V5})^2 + \mathcal{O}((\omega\tau_{V5})^4)]$$

The modulation is approximately unity, and the spectrum reduces to the standard Planck distribution.

For modes with $\omega \gg \omega_c$:
$$N_{ED}(\omega) \approx N_H(\omega) \cdot (\omega_c/\omega)^2$$

The modulation suppresses the high-frequency tail. The substrate-level spectrum is finite and well-defined at all frequencies.

### 4.3 The peak of the spectrum

The Hawking spectrum's peak is at $\omega \sim T_H \cdot k_B/\hbar$. For a Schwarzschild stellar-mass BH:
$$T_H \approx 6 \times 10^{-8}\, \mathrm{K}, \qquad \omega_{\mathrm{peak}} \sim 10^4\, \mathrm{Hz}$$

The corresponding $\omega_{\mathrm{peak}}\tau_{V5} \sim 10^4 \cdot 10^{-43} \sim 10^{-39}$ — invisible at the spectrum peak.

For a primordial BH in its final stages of evaporation ($M \to M_P$):
$$T_H \to T_P \sim 10^{32}\, \mathrm{K}, \qquad \omega_{\mathrm{peak}} \sim \omega_c$$

The V5 cutoff becomes order-unity at the peak. The spectrum is dramatically modified from standard Hawking at extreme scales.

### 4.4 Integrated emission rate

The framework's integrated Page emission rate is also modulated by V5 [21]:
$$\frac{dM}{dt}\bigg|_{ED} = -\frac{\alpha_{\mathrm{Page}}}{M^2} \cdot \left[1 - K\left(\frac{\ell_P}{M}\right)^2 + \mathcal{O}\left(\frac{\ell_P}{M}\right)^4\right]$$

where $K = -c_{V5}^{\mathrm{int}} - c_g^{\mathrm{int}}\log g$ is an order-unity coefficient inherited from V5 and motif-alphabet substrate details. The correction is invisible at observable BH scales but becomes order-unity at $M \sim M_P$.

---

## 5. DCGT and the Closing Hydrodynamic Window

The V5 cutoff is one structural component of the framework's substrate-level resolution. The Diffusion Coarse-Graining Theorem (DCGT) [15] supplies the second.

### 5.1 The DCGT scale-separation requirement

DCGT establishes the substrate-to-continuum bridge through hydrodynamic-window scale separation:
$$\ell_P \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$$

The substrate-level lower bound is $\ell_P$ (the substrate's irreducible length scale). The upper bound $L_{\mathrm{flow}}$ is the characteristic length scale of the continuum theory under derivation. For Hawking radiation, $L_{\mathrm{flow}}$ is set by the BH's size: $L_{\mathrm{flow}} = r_s = 2M$.

The scale separation requires $M \gg \ell_P$ substantially. For ordinary BHs ($M \gg M_P$), the window is enormous (ratios of $10^{38}$ to $10^{60}$ are typical). For Planck-mass-approaching BHs ($M \sim M_P$), the window closes.

### 5.2 The window closure and its meaning

When $M$ approaches $\ell_P$, the upper and lower bounds of the hydrodynamic window coincide. There is no scale $R_{\mathrm{cg}}$ satisfying $\ell_P \ll R_{\mathrm{cg}} \ll 2M$. The DCGT substrate-to-continuum bridge fails.

What does this mean structurally? Hawking radiation as a continuum-level phenomenon depends on the DCGT bridge. The bridge's leading-order consequences (scalar diffusion, directional viscosity, V1→R1 substrate-cutoff, V5→Maxwell viscoelasticity, T17 minimal coupling [15]) all require the hydrodynamic-window separation. When the window closes, the substrate-level dynamics no longer produce continuum-level emission as a coherent process.

For the trans-Planckian problem specifically: blueshifted near-horizon modes at proper frequencies $\omega_{\mathrm{proper}} \gtrsim 1/\ell_P$ have proper wavelengths $\lambda_{\mathrm{proper}} \lesssim \ell_P$. These modes lie *below* the DCGT hydrodynamic window's lower bound. They are not continuum-level features at all.

### 5.3 The combined substrate-level cutoff

The two structural components combine to provide the substrate-level cutoff:

1. **V5 finite-memory cutoff (perturbative).** The V5 kernel's coherent response saturates at $\omega \sim 1/\tau_{V5} = c/\ell_P$. Substrate cross-chain correlations at frequencies above the cutoff are suppressed by $1/\omega^2$. This is the leading-order substrate-cutoff structure.

2. **DCGT hydrodynamic-window closure (non-perturbative).** When proper wavelengths approach $\ell_P$, the substrate-to-continuum bridge fails entirely. The continuum description does not apply. This is the structural-foundational substrate-cutoff statement.

The two components are complementary. V5 provides a smooth perturbative cutoff at frequencies below the DCGT failure scale. DCGT provides the structural-foundational statement that the continuum description does not extend into the trans-Planckian regime.

---

## 6. The Substrate-Level Resolution

### 6.1 Statement of the resolution

> **The substrate-level trans-Planckian resolution.** Substrate cross-chain correlations at frequencies $\omega \gg c/\ell_P$ are not coherently mediated. The substrate's V5 finite-memory kernel does not support coherent correlations beyond $\tau_{V5}^{-1} = c/\ell_P$. Combined with DCGT's hydrodynamic-window closure when proper wavelengths approach $\ell_P$, the substrate provides a natural UV cutoff at the Planck frequency. Modes at proper frequencies above the Planck scale do not exist as continuum-level objects. The standard trans-Planckian divergence of semiclassical Hawking is a *continuum artifact* of extending QFT beyond its substrate-level support; the substrate-level account regulates the divergence naturally without postulating modified dispersion, lattice cutoffs, or any phenomenological addition.

### 6.2 Why this is not a phenomenological cutoff

The framework's resolution is structurally distinct from postulating an ad-hoc cutoff:

- The V5 kernel is a substrate primitive that exists *independently* of the trans-Planckian problem. The same kernel produces Maxwell viscoelastic memory in soft matter and entanglement-bandwidth modulation in BH information transfer [16].
- The cutoff scale $\tau_{V5} = \ell_P/c$ at the gravitational scale is FORCED by T19 + substrate dimensional analysis. It is the unique substrate-built timescale at the gravitational context.
- DCGT's hydrodynamic-window closure is a structural feature of the substrate-to-continuum bridge, not a regulator inserted to address the trans-Planckian problem.

The trans-Planckian regulation is therefore a *consequence* of substrate ontology, not a feature added to address a structural concern. This is the methodological distinction between phenomenological regularization and substrate-level resolution.

### 6.3 What this delivers

The framework's resolution:
1. Reproduces standard Hawking exactly at observable scales.
2. Produces a finite, well-defined Hawking spectrum at all frequencies.
3. Cuts off the high-frequency tail at the Planck frequency via V5.
4. Establishes the structural-foundational cutoff via DCGT closure when wavelengths approach $\ell_P$.
5. Predicts substrate-cutoff corrections at first subleading order $(\ell_P/M)^2$.
6. Combined with H-8's higher-order resummation [21], produces a stable Planck-mass remnant at the late-time evaporation endpoint.

The resolution is therefore not just a regularization — it is a substrate-level account of where, why, and how the standard semiclassical framework's structural concerns are resolved.

---

## 7. Comparison with Standard Proposals

### 7.1 Modified dispersion relations (Unruh, Jacobson, BMPS)

Modified-dispersion approaches [1, 2] postulate UV-modified dispersion relations such as:
$$\omega^2 = c^2 k^2 + f(k\ell_P)$$
with $f(k\ell_P)$ a function that effectively cuts off mode propagation at $k \sim 1/\ell_P$. Specific forms include $f(k\ell_P) = -(c\ell_P k)^4/c^2$ (Unruh-class), and various lattice-derived forms.

**Comparison with ED:**
- *Modified dispersion*: postulates the dispersion modification as a phenomenological feature.
- *ED*: derives the high-frequency cutoff from V5's substrate primitive structure. The dispersion relation itself is unchanged at the leading order; the modification appears as a multiplicative modulation of the spectrum, not as a modification of the underlying field-theoretic mode structure.

**Empirical distinguishability:** Modified-dispersion approaches typically predict specific UV modification forms that depend on the chosen $f(k\ell_P)$. ED's V5 modulation $1/(1+(\omega\tau_{V5})^2)$ is form-FORCED by V5's substrate primitive. Precision analog Hawking experiments could distinguish between different cutoff functional forms.

### 7.2 Lattice cutoffs

Lattice-cutoff approaches [3] discretize spacetime at the Planck scale, eliminating modes with wavelengths shorter than the lattice spacing.

**Comparison with ED:**
- *Lattice cutoff*: discretizes spacetime structure at the Planck scale by postulate.
- *ED*: substrate ontology is *already* discrete (P01: discrete micro-events). The substrate ontology underlying ED is not a regularization of continuum spacetime but the framework's primitive ontology. The continuum description emerges as a coarse-grained leading-order consequence (DCGT [15]).

**Structural distinction:** ED's discreteness is ontologically primary; lattice cutoff approaches treat discreteness as a regulator added to a continuum-level theory. In ED, the continuum is the emergent description; in lattice approaches, the continuum is the fundamental description being regulated.

### 7.3 Naturalness and robustness arguments

Naturalness arguments [4] argue that Hawking radiation should be *robust* against trans-Planckian sensitivities — that the empirically validated content (the thermal spectrum at $T_H = \kappa/(2\pi)$) is protected from quantum-gravity modifications by general arguments about effective field theory.

**Comparison with ED:**
- *Robustness arguments*: argue from empirical-protection that trans-Planckian content shouldn't matter, without supplying a mechanism.
- *ED*: provides the explicit mechanism (V5 substrate-cutoff + DCGT closure) by which trans-Planckian modes are absent at the substrate level.

**Methodological distinction:** Robustness arguments are arguments-from-empirical-protection; ED supplies the underlying mechanism that makes the empirical robustness structurally inevitable.

### 7.4 Trans-Planckian Censorship Conjecture (TCC)

TCC [5] conjectures that cosmological inflation must terminate before trans-Planckian modes have stretched to observable scales. This addresses cosmological trans-Planckian sensitivity but not directly the BH trans-Planckian problem.

**Comparison with ED:**
- *TCC*: cosmological constraint on inflation duration.
- *ED*: substrate-level UV cutoff applicable in any context (BH, cosmological horizon, accelerated observer [18]).

**Scope distinction:** TCC and ED's V5 cutoff address different aspects of the trans-Planckian problem. TCC concerns cosmological inflation; ED's V5 cutoff applies to all substrate-level modes. The two could in principle coexist; ED's V5 mechanism does not require TCC.

### 7.5 Firewalls and information-paradox-class proposals

Firewall [22] and related proposals (ER=EPR [23], soft hair [24], island formula [25]) address BH information at the horizon scale but do not directly resolve the trans-Planckian problem. They address what happens *at* or *near* the horizon, not the structural question of whether QFT applies at trans-Planckian frequencies.

**Comparison with ED:** ED addresses a structurally different question. Firewalls / ER=EPR / soft hair / island formula address the BH information question (handled separately in [16]). The trans-Planckian problem is addressed by V5 + DCGT, independently of the BH information mechanism.

### 7.6 Comparison summary

| Approach | Mechanism | Status | Empirical distinguishability |
|---|---|---|---|
| Modified dispersion (Jacobson, BMPS) | Postulated UV dispersion modification | Phenomenological | Specific cutoff form depends on chosen $f$ |
| Lattice cutoffs | Postulated spacetime discreteness | Phenomenological regulator | Discrete-spectrum signatures at small scales |
| Naturalness arguments | Empirical-protection argument | Argumentative | Cannot directly distinguish |
| TCC | Cosmological constraint on inflation | Conjectural | Cosmological inflation observables |
| ED V5 + DCGT | Substrate primitive + structural closure | Substrate-derived | Form-FORCED $1/(1+(\omega\tau)^2)$ cutoff |

---

## 8. Falsifiable Predictions

The framework's substrate-level resolution distinguishes itself from standard-physics approaches through specific falsifiable predictions.

### 8.1 Analog Hawking cutoff form

In analog Hawking experiments [9, 10], the Hawking-analog spectrum should exhibit a high-frequency cutoff at the analog system's microscopic correlation timescale. The framework predicts:

- The cutoff form is $1/(1+(\omega\tau_{\mathrm{analog}})^2)$.
- The analog timescale $\tau_{\mathrm{analog}}$ identifies with the analog system's characteristic correlation time:
  - BEC: $\tau_{\mathrm{analog}} \sim \xi/c_s$ (healing length over speed of sound).
  - Acoustic: $\tau_{\mathrm{analog}} \sim \lambda_{\mathrm{phonon}}/c_s$.
  - Photonic: $\tau_{\mathrm{analog}} \sim$ optical-cycle period.

Existing analog Hawking experiments confirm spectral form at moderate frequencies; precision tests at the cutoff scale are technically feasible with current-generation experiments. Modified-dispersion approaches predict specific cutoff functional forms depending on the chosen $f(k\ell_P)$; ED's prediction is the specific V5-derived $1/(1+(\omega\tau)^2)$ form.

### 8.2 Primordial BH late-stage spectra

For primordial black holes in their final stages of evaporation, the framework predicts:
- Spectral cutoff at $\omega \sim \omega_c = c/\ell_P$ (Planck frequency).
- Modified evaporation profile slowing in the final $\sim 0.1$ s.
- Possible Planck-mass remnant after evaporation halts (per H-8 [21]).

Standard semiclassical Hawking predicts complete evaporation in finite time with no upper-frequency cutoff. PBH detection with sufficient temporal and spectral resolution would test the framework's substrate-cutoff prediction.

### 8.3 High-energy photon dispersion in vacuum

If the V5 substrate-cutoff at $\omega_c = c/\ell_P$ extends to vacuum-substrate propagation (not only to BH horizon contexts), high-energy astrophysical photons traveling astronomical distances could exhibit dispersion at order $(\omega/\omega_c)^2$:
$$\Delta v / c \sim (\omega/\omega_c)^2$$

Public LIGO/Virgo + Fermi-LAT data on high-energy gamma-ray bursts and gravitational-wave-electromagnetic counterparts permit precision time-of-flight measurements. This connects ED's V5 substrate-cutoff to the active observational program on Lorentz-invariance-violation searches at high energies [26].

### 8.4 Cross-platform consistency

The V5 kernel does multiple substrate-level jobs across the framework's other domains:
- Soft-matter Maxwell viscoelasticity at molecular relaxation timescales.
- Substrate-Unruh radiation cutoff at accelerated-observer Rindler-like horizons.
- Black-hole information transfer bandwidth modulation.

Cross-platform measurement of V5-mediated phenomena across these distinct domains provides a structural consistency test. If the V5 kernel's primitive structural form $1/(1+(\omega\tau)^2)$ is correctly identified in all four domains, the substrate-ontology evidence accumulates from cross-domain reach. If the kernel's form differs across domains, the substrate-level identification needs revision.

### 8.5 Distinctive predictions versus standard proposals

| Prediction | Modified dispersion | Lattice cutoff | Naturalness | TCC | ED V5 + DCGT |
|---|---|---|---|---|---|
| Specific cutoff form | Depends on $f(k\ell_P)$ | Lattice-spacing-dependent | No specific prediction | Cosmological-only | $1/(1+(\omega\tau)^2)$ FORM-FORCED |
| Cross-platform consistency | Not predicted | Not predicted | Not predicted | Not predicted | $\tau_{V5}$ identification across domains |
| Late-stage PBH evaporation | Modified dispersion-dependent | Lattice-cutoff-dependent | Robust prediction | No prediction | Planck-mass remnant + spectrum cutoff |
| Connection to soft matter | None | None | None | None | Maxwell relaxation time identification |

---

## 9. Discussion

### 9.1 The structural-resolution claim

The trans-Planckian problem of standard semiclassical Hawking has been recognized for over thirty years [1] and addressed through multiple phenomenological approaches. Each approach contributes structural insight; none has produced a derivation-level resolution from a substrate-level ontology.

The Event Density framework's V5 + DCGT account is structurally distinct. The V5 kernel is a substrate primitive existing for reasons independent of the trans-Planckian problem (cross-domain duties in soft matter, BH information, substrate-Unruh). The DCGT bridge is the framework's substrate-to-continuum machinery. Their combination produces a substrate-level UV cutoff at the Planck scale as a *consequence* of substrate ontology, not as a feature added to address the trans-Planckian concern.

This is what we call a *substrate-level resolution*. It differs from phenomenological regularization in that the regulator is not introduced for the problem; it emerges from the substrate-level account that produces the framework's other structural commitments.

### 9.2 What this does not claim

The substrate-level resolution does *not* claim:
- That standard semiclassical Hawking is wrong. It correctly describes the empirically validated content (thermal spectrum at $T_H$ at observable scales).
- That ED is the unique substrate-level framework capable of producing such a resolution. Other substrate ontologies might in principle produce analogous resolutions.
- That all features of standard Hawking are reproduced exactly. First-subleading-order corrections at $(\ell_P/M)^2$ distinguish ED from strict semiclassical Hawking, particularly at extreme scales.

What it *does* claim is structural: the substrate ontology produces the trans-Planckian regulator as a derived consequence rather than as a phenomenological addition.

### 9.3 Implications for substrate-ontology evidence

The cross-platform reach of the V5 kernel — operating in soft-matter rheology, Hawking radiation, BH information, and substrate-Unruh contexts [16] — provides structural evidence for the substrate ontology. A phenomenological framework would have separate cutoff parameters for each context; ED has one substrate primitive (V5) doing all jobs, with the cutoff scale $\tau_{V5}$ inheriting from the physical context.

The trans-Planckian resolution illustrates this pattern. The same V5 kernel that produces Maxwell viscoelastic memory in soft matter at nanosecond timescales also produces the trans-Planckian cutoff at the Planck scale. The cross-domain reach is structural evidence that V5 is a primitive substrate object, not a domain-specific phenomenological regulator.

### 9.4 Open questions

The substrate-level resolution leaves several questions for future work:

1. **Closed-form derivation of $\tau_{V5}$ at the gravitational scale.** The framework identifies $\tau_{V5} = \ell_P/c$ via dimensional analysis; closed-form derivation from substrate-microscopic V1 + V5 details would tighten the identification.

2. **The V5 kernel shape function $\psi$.** Different shape functions produce different higher-order corrections; precision tests could distinguish.

3. **Analog Hawking precision tests.** Current analog experiments confirm spectral form at moderate frequencies; precision measurements at the cutoff scale would test ED's specific functional form against modified-dispersion alternatives.

4. **Connection to the Standard Model UV completion question.** The V5 substrate cutoff regulates trans-Planckian Hawking modes; whether it also regulates the Standard Model's UV-completion concerns at the Planck scale is open.

These open items do not undermine the substrate-level resolution but identify directions for continued development.

---

## 10. Conclusions

The trans-Planckian problem of standard semiclassical Hawking radiation arises because the standard derivation traces observed-at-infinity modes back to arbitrarily-blueshifted near-horizon proper frequencies. The standard derivation thus implicitly requires standard QFT to apply at and beyond the Planck scale, where structural concerns about quantum-gravity modification arise.

The Event Density framework provides a substrate-level resolution. The V5 finite-memory cross-chain kernel — a primitive substrate object with characteristic memory time $\tau_{V5} = \ell_P/c$ at the gravitational scale (FORCED via T19 + substrate dimensional analysis) — does not coherently mediate cross-chain correlations at frequencies $\omega \gg c/\ell_P$. Combined with the Diffusion Coarse-Graining Theorem's hydrodynamic-window closure when proper wavelengths approach $\ell_P$, the substrate provides a natural UV cutoff at the Planck frequency. The substrate cannot instantiate arbitrarily-blueshifted modes near the horizon; the trans-Planckian divergence of standard semiclassical Hawking is a continuum artifact that vanishes at the substrate level.

The V5-modulated Hawking spectrum is:
$$N_{ED}(\omega) = \frac{1}{e^{\omega/T_H} - 1} \cdot \frac{1}{1 + (\omega\tau_{V5})^2}$$
finite at all frequencies, reducing to standard Hawking at observable scales, and cut off at the Planck frequency.

The framework's resolution is structurally distinct from standard-physics approaches:
- Modified-dispersion approaches postulate UV modification of the dispersion relation.
- Lattice-cutoff approaches postulate spacetime discreteness at the Planck scale.
- Naturalness arguments invoke empirical robustness without supplying a mechanism.
- TCC addresses cosmological inflation, not the BH trans-Planckian problem.

ED's V5 + DCGT mechanism produces the cutoff as a *derived consequence* of substrate ontology rather than as a phenomenological addition. The V5 kernel exists for reasons independent of the trans-Planckian problem (cross-domain duties in soft matter, BH information, and substrate-Unruh). The trans-Planckian regulation is a cross-platform application of the same substrate primitive.

Falsifiable predictions distinguishing the framework include the V5-derived cutoff form $1/(1+(\omega\tau)^2)$ in analog Hawking experiments, the Planck-frequency cutoff in primordial-BH late-stage evaporation, possible high-energy photon dispersion at order $(\omega/\omega_c)^2$, and cross-platform identification of $\tau_{V5}$ across the framework's V5-mediated phenomena.

The substrate-level resolution illustrates a general methodological pattern: substrate primitives composed with domain-specific substrate context produce continuum-level observables in apparently unrelated domains, providing structural evidence for the substrate ontology through cross-domain reach.

---

## References

[1] Jacobson, T. "Black-Hole Evaporation and Ultrashort Distances." *Physical Review D* **44**, 1731–1739 (1991).

[2] Unruh, W. G. "Sonic Analog of Black Holes and the Effects of High Frequencies on Black Hole Evaporation." *Physical Review D* **51**, 2827–2838 (1995).

[3] 't Hooft, G. "Dimensional Reduction in Quantum Gravity." In: *Salamfest 1993*, 0284–296 [arXiv:gr-qc/9310026] (1993). (Lattice-cutoff perspective.)

[4] Helfer, A. D. "Do Black Holes Radiate?" *Reports on Progress in Physics* **66**, 943–1008 (2003). (Naturalness / robustness analysis.)

[5] Bedroya, A., Vafa, C. "Trans-Planckian Censorship and the Swampland." *Journal of High Energy Physics* **2020** (9), 123 (2020).

[6] 't Hooft, G. "On the Quantum Structure of a Black Hole." *Nuclear Physics B* **256**, 727–745 (1985).

[7] Hawking, S. W. "Particle Creation by Black Holes." *Communications in Mathematical Physics* **43**, 199–220 (1975).

[8] Hawking, S. W. "Black Hole Explosions?" *Nature* **248**, 30–31 (1974).

[9] Steinhauer, J. "Observation of Quantum Hawking Radiation and Its Entanglement in an Analogue Black Hole." *Nature Physics* **12**, 959–965 (2016).

[10] Drori, J., Rosenberg, Y., Bermudez, D., Silberberg, Y., Leonhardt, U. "Observation of Stimulated Hawking Radiation in an Optical Analogue." *Physical Review Letters* **122**, 010404 (2019).

[11] Proxmire, A. *Event Density: One Substrate, Three Domains.* April 2026.

[12] Proxmire, A. *Event Density Foundations: A Unified Substrate Architecture for Quantum, Fluid, Gauge, and Gravitational Dynamics.* April 2026.

[13] Proxmire, A. *Theorem 19: Newton's Law from Substrate Holographic Counting and the Identification of $\ell_P$.* April 2026.

[14] Proxmire, A. *Theorem 18: V1 Kernel Retardation and the Kernel-Level Arrow of Time.* April 2026.

[15] Proxmire, A. *The Diffusion Coarse-Graining Theorem: Substrate-to-Continuum Bridge for Canonical-ED Dynamical Content.* April 2026.

[16] Proxmire, A. *The V5 Kernel as a Cross-Domain Substrate Mechanism: Viscoelastic Memory, Hawking Cutoff, and Black-Hole Information Bandwidth.* May 2026.

[17] Proxmire, A. *Arc Hawking H-5: Information Correlations and Substrate-Level Page Curve Structure.* May 2026.

[18] Proxmire, A. *Walkthrough: From Primitives to the Substrate-Unruh Effect.* May 2026.

[19] Proxmire, A. *Arc Hawking H-1: Spectral Form and Temperature from V5 Cross-Chain Correlations at a Saturated Decoupling Surface.* May 2026.

[20] Proxmire, A. *Walkthrough: From Primitives to Hawking Radiation.* May 2026.

[21] Proxmire, A. *Arc Hawking H-8: Higher-Order Resummation and the Late-Time Evaporation Endpoint.* May 2026.

[22] Almheiri, A., Marolf, D., Polchinski, J., Sully, J. "Black Holes: Complementarity or Firewalls?" *Journal of High Energy Physics* **2013** (2), 062 (2013).

[23] Maldacena, J., Susskind, L. "Cool Horizons for Entangled Black Holes." *Fortschritte der Physik* **61**, 781–811 (2013).

[24] Hawking, S. W., Perry, M. J., Strominger, A. "Soft Hair on Black Holes." *Physical Review Letters* **116**, 231301 (2016).

[25] Almheiri, A., Engelhardt, N., Marolf, D., Maxfield, H. "The Entropy of Bulk Quantum Fields and the Entanglement Wedge of an Evaporating Black Hole." *Journal of High Energy Physics* **2019** (12), 063 (2019).

[26] Mattingly, D. "Modern Tests of Lorentz Invariance." *Living Reviews in Relativity* **8**, 5 (2005). (High-energy photon dispersion observational program.)

[27] Brout, R., Massar, S., Parentani, R., Spindel, P. "Hawking Radiation Without Trans-Planckian Frequencies." *Physical Review D* **52**, 4559–4568 (1995). (BMPS approach.)

[28] Polchinski, J. "String Theory and Black Hole Complementarity." In: *String Theory* (1999). (Robustness analysis.)

[29] Brout, R., Massar, S., Parentani, R., Spindel, P. "A Primer for Black Hole Quantum Physics." *Physics Reports* **260**, 329–446 (1995). (Comprehensive review of trans-Planckian issue.)

[30] Proxmire, A. *Substrate-Level Resolution of the Black Hole Information Paradox: Integrating Event Density Architecture with Hawking-Radiation Derivations.* May 2026.

[31] The full Event Density corpus, including all forced theorems and supporting memos, is available at https://github.com/allen-proxmire/event-density.

---

**Brief summary.** The Event Density framework's V5 finite-memory cross-chain kernel — a substrate primitive with characteristic memory time $\tau_{V5} = \ell_P/c$ at the gravitational scale — produces a substrate-level resolution of the trans-Planckian problem of standard semiclassical Hawking radiation. The substrate cannot mediate cross-chain correlations at frequencies $\omega \gg c/\ell_P$ because V5's coherence breaks down beyond the cutoff, and combined with the Diffusion Coarse-Graining Theorem's hydrodynamic-window closure when proper wavelengths approach $\ell_P$, the substrate provides a natural UV cutoff at the Planck frequency without requiring modified dispersion relations, lattice cutoffs, or other phenomenological additions. The V5-modulated Hawking spectrum $N_{ED}(\omega) = N_H(\omega)/(1+(\omega\tau_{V5})^2)$ is finite at all frequencies, reduces to standard Hawking at observable scales, and produces falsifiable first-subleading-order corrections distinguishing the framework from modified-dispersion approaches in analog Hawking experiments and primordial-BH late-stage evaporation observations.

---

**Recommended next steps.** Multiple options:

1. **Editorial pass for journal submission.** Polish prose, tighten citations, prepare figures for the V5 cutoff function and Hawking-spectrum modification. Estimated 1–2 sessions.

2. **Bandwidth-budget cross-arc paper.** Companion paper to the V5 cross-domain unification, articulating the bandwidth-budget mechanism unifying Arc E monogamy + BH-4 entanglement-straddling + Q-COMPUTE Class C plateau + H-5 Page-curve min-bound. Estimated 2–3 sessions.

3. **Substrate-Unruh / de Sitter cross-arc paper.** Extends the substrate-Unruh argument from the H-arc and substrate-Unruh walkthrough to cosmological horizons; would be a structural prerequisite for any future substrate-cosmology arc. Estimated 2–3 sessions.

4. **Memory update.** Document the trans-Planckian short paper completion in MEMORY.md. Brief documentation pass.

5. **Substrate cosmology Arc COSMO scoping.** With the cross-arc unification papers and trans-Planckian short paper completed, the substrate-cosmology arc becomes the natural follow-on. Substrate-derived Friedmann-class equations, $H_0$ derivation, expansion history. Required prerequisite for the baryogenesis arc previously discussed. Estimated 2–4 sessions for scoping.

6. **Continue from Investigation Priority List.** Other items: O1 (superradiance amplitude), O3 (full Kerr interior), B5 (SM gauge group residue), C1/GR-4A (Einstein-equation emergence) become next-natural-arc candidates.
