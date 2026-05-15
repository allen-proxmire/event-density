# From Primitives to Hawking Radiation

## A Walkthrough of the Event Density Substrate-Level Derivation

**Allen Proxmire** · May 2026

---

## 1. The Question

In 1974, Stephen Hawking published a calculation that nobody saw coming. Combine quantum field theory with the geometry of a black hole, and the black hole emits thermal radiation. The temperature is set by the surface gravity of the horizon: $T_H = \kappa/(2\pi)$. For a one-solar-mass black hole, $T_H \approx 6 \times 10^{-8}$ K — far below the cosmic microwave background, far below any direct detection threshold. But the calculation is mathematically clean, structurally compelling, and predicts a definite spectrum: Planck distribution per mode, modulated by greybody factors from spacetime-curvature backscattering, with the black hole losing mass at a rate $\dot M = -\alpha_{\mathrm{Page}}/M^2$.

The Hawking calculation is one of the most striking results in theoretical physics. It connects general relativity to quantum mechanics. It introduces black-hole thermodynamics as a structurally serious framework. It launches the black-hole information paradox: thermal radiation appears to discard information about the BH initial state, contradicting unitary quantum mechanics. It produces — through Page's 1993 analysis — a definite prediction for the entanglement entropy of the radiation as a function of time: linear rise to a maximum at the Page time, followed by power-law fall to zero as the BH evaporates and information is recovered through correlations between Hawking quanta.

The standard derivation has worked since 1974. Bogoliubov-transformation calculations on Schwarzschild spacetime produce the thermal spectrum; standard wave-equation methods on curved spacetime produce the greybody factors; integration over modes produces the Page rate; entanglement-entropy analysis produces the Page curve. Each step is mathematically clean within standard QFT-in-curved-spacetime.

But the standard derivation has structural questions left open. The *trans-Planckian problem*: modes observed at moderate frequencies at infinity arose from arbitrarily-blueshifted Planck-scale modes near the horizon, where standard QFT is structurally questionable. The *information paradox*: if Hawking radiation is purely thermal, information about the BH initial state seems to be lost — contradicting unitary quantum mechanics. The *vacuum-state-choice issue*: which QFT vacuum (Boulware, Hartle-Hawking, Unruh) is appropriate, and how do we know? The *pair-creation mechanism*: virtual particle-antiparticle pairs near the horizon, with one captured and one escaping, raises ontological questions about what's actually happening at the substrate level.

The Event Density framework provides a substrate-level account of Hawking radiation that addresses these structural questions. The derivation reproduces every ingredient of standard semiclassical Hawking exactly at leading order, while resolving the trans-Planckian problem at the substrate level, providing a structural account of the information paradox via entanglement-straddling, and producing FORM-FORCED first-subleading-order corrections that distinguish ED from strict semiclassical Hawking.

The honest framing: ED's contribution to Hawking radiation is what the framework calls a *regulated completion* of standard semiclassical Hawking. The framework reproduces the empirically validated content (Hawking spectrum, Page rate, Page curve) at leading order — exactly. The framework provides substrate-level UV regulation (V5 finite-memory cutoff at the Planck scale) that resolves the trans-Planckian problem. The framework provides an alternative substrate-level account of the information-recovery mechanism (entanglement-straddling at the saturated decoupling surface). And the framework produces conditional new content at extreme scales — possible Planck-mass remnants — that could be cosmologically significant if confirmed by higher-order analysis.

The chain has six structural moves:

1. The black-hole horizon is, in ED's substrate ontology, a *saturated decoupling surface* where cross-chain bandwidth $\Gamma_{\mathrm{cross}}$ falls below hydrodynamic-window resolution. Information cannot flow freely across it; the BH interior is a saturated participation zone.

2. Substrate observers accelerated near the saturated surface experience the substrate vacuum as thermal — the substrate analog of the Unruh effect. Cross-chain V5 correlations across the surface satisfy imaginary-time periodicity at $\beta= 2\pi/\kappa_{\mathrm{ED}}$, where $\kappa_{\mathrm{ED}}$ is the substrate-level surface gravity.

3. The KMS condition (mathematical equivalent of imaginary-time periodicity) produces a Planck distribution per substrate mode at temperature $T = \kappa_{\mathrm{ED}}/(2\pi)$.

4. The Diffusion Coarse-Graining Theorem (DCGT) identifies $\kappa_{\mathrm{ED}}$ with the standard surface gravity $\kappa$ at leading-order substrate-to-continuum coarse-graining. The substrate-level temperature becomes $T_H = \kappa/(2\pi)$ — the Hawking temperature.

5. Substrate scattering of emitted modes through the substrate-effective potential (which identifies with the Regge-Wheeler potential at leading order) produces greybody factors. Integration over modes produces the Page evaporation rate.

6. The bipartite entanglement structure between near-horizon and outgoing modes — governed by the BH-4 entanglement-straddling mechanism plus Arc E's bandwidth-budget min-bound — produces the Page curve. Information is recovered through correlations between Hawking quanta.

The structural payoff: Hawking radiation is what the substrate produces at a saturated decoupling surface. Every ingredient of the standard semiclassical calculation reproduces from substrate primitives via DCGT identification, with first-subleading-order corrections that distinguish ED from strict semiclassical and resolve historical structural questions in the bargain.

---

## 2. The Primitives That Matter

The framework rests on substrate-level ontological commitments. The Hawking-radiation walkthrough uses the working subset that the BH-arc and the QM-emergence walkthroughs use, plus one additional substrate kernel that does the heavy substrate-level work for Hawking specifically.

**Micro-events (P01).** Discrete acts of becoming, vertices in a graph spanning the event manifold.

**Chains (P02).** Stable subgraphs along which a chain repeatedly instantiates its update rule. The chains are what propagate; their dynamics is what we observe.

**Bandwidth (P04).** Non-negative real edge weight, with bandwidth-additivity for independent contributions.

**Polarity / U(1) phase (P09).** $U(1)$-valued phase relation between a chain's update rule and the local ED-flow direction.

**Commitment irreversibility (P11).** Once a chain selects one channel from those available, the commitment is irreversible.

**Continuous time (P13).** The substrate's temporal evolution is continuous between commitment events.

**V1 forward-cone-only kernel (T18).** The substrate's vacuum kernel mediating cross-chain correlations. Forward-cone-only by closed-arc inheritance from the kernel-arrow / arrow-of-time program. Establishes the causal structure of substrate cross-chain interactions.

**V5 finite-memory kernel.** The substrate's *cross-chain memory* kernel that mediates correlations across regions of substrate. Has finite memory time $\tau_{V5}$ — a primitive substrate parameter. V5 is the load-bearing kernel for Hawking radiation; this is the kernel that does the substrate analog of the Bogoliubov calculation.

**Substrate locality.** Cross-chain correlations propagate via mediating substrate structure (V1, V5, channels), not via instantaneous non-local action.

Three forced theorems load-bear here:

**T17 (Gauge-field-as-rule-type connection).** Charged particles emit Hawking radiation in standard physics; the gauge-coupling structure that determines the emission rates is FORCED by T17 from substrate rule-type taxonomy.

**T19 (Newton's $G = c^3 \ell_P^2/\hbar$).** Identifies the substrate's irreducible length scale $\ell_P$ as the Planck length. Load-bears for the V5 timescale identification at the gravitational scale: $\tau_{V5} = \ell_P/c$ (the Planck time).

**DCGT (Diffusion Coarse-Graining Theorem).** The substrate-to-continuum bridge that identifies substrate-level quantities with their continuum-level counterparts at leading order. Critical for the substrate calculation to match standard semiclassical Hawking at observable scales.

Two interpretation-level structures load-bear:

**BH-2 (Horizon as saturated decoupling surface).** The BH-arc's structural identification of black-hole horizons with substrate-level saturated decoupling surfaces. Cross-chain bandwidth $\Gamma_{\mathrm{cross}}$ across the horizon falls below hydrodynamic-window resolution.

**BH-4 (Entanglement-straddling at horizon).** Information crosses the horizon via V5 cross-chain correlations re-routed around the saturated surface. The substrate-level account of "what happens at the horizon" beyond the semiclassical pair-creation picture.

That's the structural setup. The Hawking-radiation argument runs on this.

---

## 3. The Substrate Reading of Black-Hole Horizons

Standard general relativity describes a black-hole horizon as a one-way membrane in spacetime: matter and light can fall in, but nothing can escape. The horizon is defined geometrically as the boundary of the trapped region; its area is the BH's "size" in the area-law-entropy sense. Beyond the horizon, the spacetime ends at a singularity (in classical GR) or at a region of unbounded curvature (in semiclassical analyses).

ED's substrate ontology produces a different account.

### 3.1 The horizon as saturated decoupling surface

In ED, what classical GR calls a "black-hole horizon" is, at the substrate level, a *saturated decoupling surface* — a region of substrate where the gradient sparsity $\sigma$ has reached its substrate-saturation value $\sigma_{\mathrm{sat}}$. At this saturation:

- Cross-chain bandwidth $\Gamma_{\mathrm{cross}}(r) \sim \exp[-\alpha\int_0^r \sigma(r')\, dr']$ across the surface falls exponentially as the path-integrated $\sigma$ rises sharply.
- At and beyond the saturation, $\Gamma_{\mathrm{cross}}$ falls below the hydrodynamic-window resolution.
- The substrate cannot support coherent cross-region correlations from the interior to the exterior (or vice versa) at the substrate level.

The "horizon" is thus a substrate-level boundary not in spacetime geometry but in the substrate's *correlational structure*. Substrate modes from the interior cannot reach the exterior via direct cross-chain coupling because the gradient barrier is too steep.

### 3.2 The interior as saturated participation zone

Beyond the saturated decoupling surface, the substrate enters a *saturated participation zone* — a region where substrate participation density is at its maximum sustainable value. In this regime:

- Standard substrate dynamics break down (the substrate is at the boundary of its operating range).
- Coarse-graining through DCGT fails (the hydrodynamic window closes).
- New chains cannot be created and existing chains' propagation is highly constrained.

This is the substrate-level analog of the BH interior. There is no singularity (BH-3 closure: the saturation zone has finite substrate-density, no divergent quantities). There is no spacetime endpoint. There is a substrate region where ordinary substrate dynamics no longer apply.

### 3.3 The substrate-level surface gravity $\kappa_{\mathrm{ED}}$

Define the substrate-level surface gravity:

$$
\kappa_ED = \alpha \cdot(\nabla \sigma)|_{\mathrm{surf}}
$$

where $(\nabla\sigma)|_{\mathrm{surf}}$ is the gradient of $\sigma$ evaluated at the saturation surface, and $\alpha$ is the substrate-level path-suppression coefficient appearing in $\Gamma_{\mathrm{cross}} \sim \exp[-\alpha\int\sigma\,d\ell]$.

This is the substrate analog of the standard surface gravity $\kappa$ at a Schwarzschild horizon. It measures how rapidly the gradient sparsity rises at the saturation surface — equivalently, how "steep" the substrate-level barrier is between interior and exterior.

DCGT identifies $\kappa_{\mathrm{ED}}$ with $\kappa$ at leading-order substrate-to-continuum coarse-graining. For Schwarzschild substrate-states, $\kappa= 1/(4M)$ (geometrized units), so $\kappa_{\mathrm{ED}} \to 1/(4M)$ in the standard BH-mass convention.

---

## 4. The Substrate-Unruh Argument

The standard semiclassical derivation of Hawking radiation runs through the *Bogoliubov transformation* between past and future modes of a quantum field on Schwarzschild spacetime. The result: vacuum modes that look empty in one frame look thermal in the other, with the thermal mixing parameter equal to $\kappa/(2\pi)$.

ED's substrate-level derivation runs through the *substrate-Unruh argument* — a structurally parallel calculation but performed on substrate primitives rather than QFT-in-curved-spacetime.

### 4.1 The Rindler-like substrate frame near the saturated surface

Near the saturated decoupling surface, introduce substrate coordinates $(\rho, t)$ with:

$$
r = \rho^{2} \cdot(\kappa_ED / 2)
$$

where $\rho$ is a substrate radial distance and $r = 0$ is at the saturation surface. The substrate's local geometry in $(\rho, t)$ has the structure of an accelerating frame — the substrate analog of the Rindler frame in flat spacetime. Substrate observers at fixed $\rho$ experience proper substrate-acceleration:

$$
a(\rho) = 1/\rho
$$

This is a substrate-level Rindler-like frame: the substrate has a distinguished accelerating direction (toward and away from the surface) plus a distinguished time direction (the Killing-like substrate time of the stationary saturated surface).

### 4.2 The substrate-Unruh effect

A substrate observer at fixed $\rho$ near the saturated surface — accelerating relative to the substrate's asymptotic frame at proper acceleration $a$ — sees the substrate's V5 vacuum as a thermal state at temperature:

$$
T_{\mathrm{local}} = a/(2\pi) = 1/(2\pi \rho)
$$

This is the substrate-level Unruh effect: an accelerated observer in the substrate sees thermal radiation at temperature proportional to the proper acceleration. The argument is structurally parallel to the standard Unruh effect in QFT, with the substrate's V5 vacuum playing the role of the standard Wightman vacuum.

### 4.3 Imaginary-time periodicity from substrate self-consistency

The substrate-Unruh argument's load-bearing step: under analytic continuation $t \to -i\tau$, the substrate's local geometry near the surface becomes:

$$
ds^{2}_{\mathrm{substrate}} \approx \rho^{2} \kappa_ED^{2} \cdot d\tau^{2} + d\rho^{2} + (transverse pieces)
$$

This is the substrate analog of flat 2D Euclidean space in polar coordinates, with $\rho$ as the radial coordinate and $\kappa_{\mathrm{ED}}\tau$ as the angular coordinate. To avoid a substrate-level *conical singularity* at $\rho= 0$ (the saturated surface itself), the angular coordinate $\kappa_{\mathrm{ED}}\tau$ must have period $2\pi$:

$$
\tau \in[0, 2\pi /\kappa_ED)
$$

The substrate-time, analytically continued to imaginary substrate-time, has period $\beta= 2\pi/\kappa_{\mathrm{ED}}$.

What does "no substrate-level conical singularity" mean? At the substrate level: V5 cross-chain correlations near the saturated surface must form a self-consistent substrate object. A conical singularity in the analytically continued substrate would correspond to a discontinuity in V5 correlations as the imaginary substrate-time circle is traversed. This would mean the substrate's vacuum state is not a single coherent substrate object but two separate substrate states glued together inconsistently. Substrate locality (P02) and continuity-under-DCGT-coarse-graining forbid such discontinuities.

The periodicity $\beta= 2\pi/\kappa_{\mathrm{ED}}$ is therefore FORCED by substrate-vacuum self-consistency at the saturated surface, in parallel with the standard no-conical-singularity argument in QFT-in-curved-spacetime.

### 4.4 The KMS condition and Planck distribution

A correlation function periodic in imaginary time with period $\beta$ satisfies the *KMS condition*:

$$
G(-i\beta + \Delta t, x_1, x_2) = G(\Delta t, x_2, x_1)
$$

The KMS condition is mathematically equivalent to thermal correlations at temperature $T = 1/\beta$ — a theorem of standard mathematical physics (Kubo, Martin, Schwinger 1957–1959). The substrate's V5 correlation function across the saturated surface, satisfying the imaginary-time periodicity from §4.3, therefore satisfies KMS at temperature:

$$
T = 1/\beta= \kappa_ED / (2\pi)
$$

The spectral content of a KMS-thermal correlation function is the Planck distribution:

$$
N(\omega) = 1 / (e^{\beta \omega} - 1) for \omega > 0 (bosonic substrate modes)
$$

This is the substrate-level Planck distribution at temperature $T = \kappa_{\mathrm{ED}}/(2\pi)$.

### 4.5 The Hawking temperature via DCGT identification

At leading-order DCGT coarse-graining:

$$
\kappa_ED \to \kappa(standard surface gravity at the horizon)
$$

For Schwarzschild: $\kappa= c^4/(4GM)$ in SI units, or $1/(4M)$ in geometrized units. The substrate-level Planck distribution becomes:

$$
N(\omega) = 1/(e^{\omega /T_H} - 1), T_H = \kappa /(2\pi)
$$

— the Hawking temperature. For Schwarzschild stellar mass:

$$
T_H = \hbar c^{3}/(8\pi G M k_B) \approx 6 \times 10^{-8} K \cdot(M_ \odot /M)
$$

The framework has reproduced the Hawking temperature exactly at leading order via the substrate-Unruh argument plus DCGT identification.

---

## 5. Greybody Factors and the Page Rate

The Planck spectrum at the saturated surface is *not* what observers at infinity see. Each substrate mode emitted from the surface has to propagate through the substrate exterior, where it encounters an effective potential barrier — the substrate analog of the spacetime-curvature backscattering in standard semiclassical Hawking.

### 5.1 The substrate scattering problem

For a substrate mode with frequency $\omega$ and angular labels $(\ell, m)$, the radial substrate amplitude $R_{\omega\ell}(r)$ satisfies a wave equation:

$$
d^{2}R_\omega \ell /dr*^{2} + [\omega^{2} - V_\ell^(ED)(r)] \cdot R_\omega \ell= 0
$$

where $r_*$ is a substrate-tortoise coordinate and the substrate-effective potential is:

$$
V_\ell^(ED)(r) = f_\sigma(r) \cdot[\ell(\ell +1)/r^{2} + (1/r) \cdot(df_\sigma /dr)]
$$

The substrate state-dependent factor $f_\sigma(r)$ goes to zero at the saturated surface (where $\sigma$ saturates) and to unity at substrate-asymptotic infinity. At leading-order DCGT coarse-graining:

$$
f_\sigma(r) \to 1 - 2M/r (Schwarzschild lapse function)
$$

The substrate-effective potential at leading order becomes the standard Regge-Wheeler effective potential. The substrate scattering problem identifies with the standard semiclassical scattering problem at leading order.

### 5.2 The greybody factor

The transmission coefficient through the substrate-effective potential gives the *greybody factor*:

$$
𝒯_\ell(\omega) = |T_\ell(\omega)|^{2}
$$

where $T_\ell(\omega)$ is the transmission amplitude. The greybody factor measures the fraction of radiation in mode $(\ell, \omega)$ that escapes to infinity; the rest is reflected back into the BH.

Limits:
- Low frequency $\omega M \ll 1$: $\mathcal{T}_\ell(\omega) \approx((\omega r_h)/2)^{2\ell+2}$ — high angular momentum modes are exponentially suppressed.
- High frequency $\omega M \gg 1$: $\mathcal{T}_\ell(\omega) \to 1$ — modes propagate semiclassically, with cross-section approaching the geometric absorption cross-section $27\pi M^2$ for s-wave.

At intermediate frequencies, $\mathcal{T}_\ell(\omega)$ takes substrate-derived values that identify with the standard Regge-Wheeler / Teukolsky greybody factors at leading-order DCGT.

### 5.3 The spectrum at infinity

The differential emission rate at infinity:

$$
dN/(dt d\omega) = (1/2\pi) \cdot \sum_\ell(2\ell +1) \cdot 𝒯_\ell(\omega) \cdot N_H(\omega)
$$

This is the standard semiclassical Hawking spectrum — Planck distribution filtered by greybody factors, with full angular-momentum sum. ED reproduces this at leading order.

### 5.4 The Page evaporation rate

Integrating the substrate emission rate over modes:

$$
dM/dt = -(1/2\pi) \sum_\ell(2\ell +1) \int_0^\infty d\omega \cdot \omega \cdot 𝒯_\ell(\omega) \cdot N_H(\omega)
= -\alpha_Page / M^{2}
$$

where $\alpha_{\mathrm{Page}}$ is the standard Page numerical coefficient (which depends on which species are emitted). For Schwarzschild stellar mass, integrating the standard species mix gives a BH lifetime of order $10^{67}$ years for $M \sim M_\odot$.

The substrate calculation reproduces this exactly at leading order. The framework's substrate-derived $\dot M$ matches the standard Page rate at observable BH scales.

---

## 6. The Page Curve and Information Recovery

Standard physics has been worried about the *information paradox* since Hawking's 1976 paper: if the BH evaporates and the radiation is purely thermal, then the BH initial state's information appears to be lost — contradicting unitary quantum mechanics.

Page (1993) proposed a resolution: the radiation is not purely thermal but contains correlations between emitted Hawking quanta. The *Page curve* tracks the entanglement entropy of the radiation as a function of time:

- Linear rise from 0 at $t = 0$ to a maximum at the *Page time* $t_{\mathrm{Page}} \approx 0.54 \tau_{\mathrm{BH}}$ (when half the BH has evaporated).
- Maximum entropy $S_{\mathrm{\max}} = S_{\mathrm{BH,0}}/2$.
- Power-law fall back to 0 at $\tau_{\mathrm{BH}}$ (full evaporation).
- Information recovered through correlations between Hawking quanta.

ED produces this Page-curve structure from substrate primitives.

### 6.1 The bipartite entanglement structure

The substrate-level bipartite system:
- **System A:** outgoing radiation modes that have escaped to substrate-asymptotic infinity.
- **System B:** BH-interior modes that fell across the saturated decoupling surface.

The two systems are entanglement-paired: each Hawking quantum (in A) is entangled with an interior-fallen mode (in B) via V5 cross-chain correlations re-routed around the saturated surface (BH-4 mechanism).

### 6.2 The bandwidth-budget min-bound

Arc E (entanglement) Memo 4 established that bipartite entanglement is bounded by the substrate's cross-chain bandwidth budget. For the Hawking system A + B:

$$
S_AB(t) \leq \min[S_BH(t), S_{\mathrm{radiation}}(t)]
$$

where $S_{\mathrm{BH}}(t)$ is the BH entropy from BH-5's area-law (which decreases as the BH evaporates) and $S_{\mathrm{radiation}}(t)$ is the cumulative entropy of the emitted radiation up to time $t$ (which increases as more is emitted).

The min-bound is what produces the Page-curve structure:

- **Pre-Page-time:** $S_{\mathrm{radiation}}$ is small, so the min is dominated by $S_{\mathrm{radiation}}$, which is rising. The radiation entropy $S_{\mathrm{rad}}(t)$ rises with the radiation's own thermodynamic entropy.
- **Page-time:** $S_{\mathrm{radiation}} = S_{\mathrm{BH}}$. Both are at intermediate values; the min-bound is saturated.
- **Post-Page-time:** $S_{\mathrm{BH}}$ has shrunk below $S_{\mathrm{radiation}}$, so the min is dominated by $S_{\mathrm{BH}}$, which is falling. The radiation entropy $S_{\mathrm{rad}}(t)$ falls with the BH entropy.

The cusp at $t_{\mathrm{Page}}$, where the min-bound switches between the two arguments, is the substrate-level origin of the Page curve's distinctive shape.

### 6.3 Numerical Page time

Using BH-5's area-law $S_{\mathrm{BH}}(t) = S_{\mathrm{BH,0}}(1 - t/\tau_{\mathrm{BH}})^{2/3}$ (since $A \propto M^2$ and $M^3 \propto(1 - t/\tau_{\mathrm{BH}})$) and $S_{\mathrm{radiation}}(t) \approx S_{\mathrm{BH,0}}(t/\tau_{\mathrm{BH}})$, equating gives:

$$
(1 - t_Page/\tau_BH)^(2/3) = t_Page/\tau_BH
$$

Numerical solution: $t_{\mathrm{Page}}/\tau_{\mathrm{BH}} \approx 0.54$ — the standard Page time.

### 6.4 Information recovery via entanglement-straddling

The substrate-level mechanism for information recovery in ED:

- Information crosses the horizon via V5 cross-chain re-routing around the saturated surface (BH-4).
- This routing is causally constrained by T18 (V1 forward-cone-only) and irreversibly tracked by P11 (commitment-irreversibility).
- Substrate-level unitarity is over-determined by T18 + P11 + ED-I-06 (no fundamental fields) — the same three substrate locks that produce E-5's no-signaling theorem.
- As the BH evaporates, $S_{\mathrm{BH}} \to 0$ and the bipartite entanglement structure collapses into purely-radiation correlations. Information that was previously stored in the bipartite entanglement is now in the radiation's self-correlations. An observer who collected and analyzed all Hawking quanta would, in principle, reconstruct the BH initial state.

There is no information loss at the substrate level. The Page curve's return to zero at $\tau_{\mathrm{BH}}$ reflects the substrate-level fact that information is fully recovered through correlations between Hawking quanta.

This is ED's substrate-level resolution of the information paradox: V5 cross-chain re-routing + bandwidth-budget min-bound + substrate-level unitarity from T18 + P11 + ED-I-06.

---

## 7. What ED Adds Beyond Semiclassical

The framework reproduces standard semiclassical Hawking exactly at leading order. ED's substantively new content lives at first subleading order $(\ell_P/M)^2$ and in structural improvements that resolve historical concerns.

### 7.1 The trans-Planckian resolution

Standard semiclassical Hawking has a *trans-Planckian problem*: modes observed at moderate frequencies at infinity arose from arbitrarily-blueshifted Planck-scale modes near the horizon. The standard derivation assumes ordinary QFT applies all the way to the Planck scale, which is structurally questionable.

ED resolves this at the substrate level. The V5 finite-memory kernel has characteristic time $\tau_{V5} = \ell_P/c$ (the Planck time). The kernel cannot mediate coherent cross-chain correlations at frequencies $\omega \gg c/\ell_P = \omega_c$ (the Planck frequency). At and beyond $\omega_c$, V5 coherence breaks down — substrate modes near the horizon at proper frequencies $\omega_{\mathrm{proper}} \gtrsim \omega_c$ do not maintain V5-coherent structure.

The trans-Planckian problem is *resolved at the substrate level* by V5's finite memory. The substrate does not support arbitrarily-blueshifted modes near the horizon, regulating the trans-Planckian content of the standard calculation without phenomenological ad-hoc cutoffs.

### 7.2 First-subleading-order spectrum corrections

The V5 finite-memory kernel modulates the Planck distribution at first subleading order:

$$
N_ED(\omega) = N_H(\omega) \cdot[1 - (\omega \tau_V5)^{2} + O((\omega \tau_V5)^4)]
$$

For ordinary Hawking frequencies $\omega \sim T_H \sim 1/M$ (geometrized units), the correction at the spectrum's peak is of order $(\ell_P/M)^2$ — far below observable threshold for stellar-mass BHs. For modes approaching the Planck scale, the correction grows toward order unity and the spectrum's high-frequency tail is cut off.

Combined with motif-alphabet corrections from BH-5 (which produce a temperature shift $\delta_g \sim(\ell_P/M)^2 \log g$), the first-subleading corrected spectrum is:

$$
N_ED(\omega) = N_H(\omega) \cdot[1 + \delta_V5(\omega) + \delta_g \cdot G(\omega /T_H) + O((\ell_P/M)^4)]
$$

with $\delta_{V5}(\omega) = -(\omega\ell_P/c)^2$ and $\delta_g = c_g(\ell_P/M)^2\log g$, both with FORM-FORCED structure and INHERITED coefficients.

### 7.3 Possible Planck-mass remnant

The first-subleading-order Page rate:

$$
dM/dt|_ED = -\alpha_Page/M^{2} \cdot[1 - K(\ell_P/M)^{2} + O((\ell_P/M)^4)]
$$

For stellar-mass BHs, the correction is $\sim 10^{-76}$ — invisible. For primordial BHs in their final stages of evaporation, $(\ell_P/M)^2$ approaches order unity and the correction becomes significant.

The correction *slows* the late-stage evaporation. Whether higher-order corrections produce a stable endpoint at $M \sim M_*$ (a *Planck-mass remnant*) or allow continued slow evaporation depends on the resummation of $(\ell_P/M)^2$ corrections at all orders. The leading-correction analysis cannot determine this; substrate-microscopic analysis or empirical evidence is required.

If higher-order analysis settles a stable Planck-mass remnant scenario, the framework predicts:
- Primordial-BH evaporation leaves remnants of mass $\sim 22\,\mu$g each.
- Each remnant carries $\sim O(\log g)$ bits of substrate-bound information about its parent BH.
- Aggregate remnants from primordial-BH evaporation contribute to a structural relic-matter component of the cosmic energy budget.

This is the framework's most cosmologically significant Hawking-arc prediction. It is *conditional* on higher-order analysis but structurally available.

### 7.4 Pair-creation vs. entanglement-straddling

Standard semiclassical Hawking interprets the radiation as continuous vacuum pair-production near the horizon, with one member captured (falling in) and one escaping (becoming a Hawking quantum). This requires QFT vacuum-state choices (Boulware, Hartle-Hawking, Unruh) and the ontologically heavy assumption of continuous vacuum pair-production.

ED's entanglement-straddling mechanism is structurally different. The "outgoing Hawking quantum" is one endpoint of a V5 cross-chain correlation; the "infalling partner" is the other endpoint. Both endpoints exist as substrate features; the saturated decoupling surface bifurcates them. There is no vacuum pair-production primitive; the substrate's entanglement structure is already in place pre-horizon-formation.

ED's mechanism is empirically equivalent to the pair-creation picture at leading order (both predict the same Planck spectrum), but structurally more economical. It also avoids the QFT vacuum-state-choice issue: ED's V5 vacuum is a substrate-level object with its own structural definition, not requiring a choice between standard QFT vacua.

---

## 8. What's Forced, What's Inherited, What's Open

It is worth being precise about what changes when ED's substrate-level Hawking machinery is in place versus when it isn't.

### 8.1 What's forced

The substrate-level Hawking temperature $T_H = \kappa/(2\pi)$ is FORCED at leading order via the substrate-Unruh argument plus DCGT identification.

The Planck distribution per mode is FORCED at leading order via the KMS condition derived from V5 imaginary-time periodicity at $\beta= 2\pi/\kappa_{\mathrm{ED}}$.

The greybody factors $\mathcal{T}_\ell(\omega)$ are FORM-FORCED via substrate scattering through the substrate-effective potential, with leading-order identification with the Regge-Wheeler / Teukolsky greybody factors via DCGT.

The Page evaporation rate $\dot M = -\alpha_{\mathrm{Page}}/M^2$ is FORCED at leading order via integration of the substrate spectrum.

The Page curve structure (linear rise + power-law fall, $t_{\mathrm{Page}} \approx 0.54\tau_{\mathrm{BH}}$, $S_{\mathrm{\max}} = S_{\mathrm{BH,0}}/2$) is FORCED at leading order via Arc E bandwidth-budget min-bound + BH-4 entanglement-straddling + BH-5 area-law entropy.

The first-subleading-order corrections from V5 cutoff and motif-alphabet are FORM-FORCED with COEFFICIENTS-INHERITED from substrate-microscopic details.

The substrate-level resolution of the trans-Planckian problem is FORCED via T19 ($\ell_P$ identification) + V5's finite memory.

The substrate-level information-recovery mechanism (entanglement-straddling + bandwidth-budget min-bound + substrate-unitarity) is FORCED via BH-4 + Arc E + T18 + P11 + ED-I-06.

### 8.2 What's inherited

The numerical value of $\alpha_{\mathrm{Page}}$ is INHERITED from standard physics. The species sum (which particles are emitted at the relevant Hawking temperature) is INHERITED from the Standard Model rule-type taxonomy.

The numerical values of the first-subleading-order coefficients ($K$, $c_g$, $c_t$, etc.) are INHERITED from substrate-microscopic details that the framework's structural-foundations program has not yet derived to closed numerical values.

The motif alphabet $g$ from BH-5 is INHERITED from substrate-microscopic motif-counting structure.

The specific Schwarzschild $\kappa= 1/(4M)$ is INHERITED from the substrate state's spherical-symmetry assumption (the framework's substrate calculation here applies to Schwarzschild-class BHs).

### 8.3 What's open

The closed-form derivation of $\alpha$ (the path-suppression coefficient in $\Gamma_{\mathrm{cross}}$) from substrate-microscopic V1 + V5 details is open. The framework establishes that $\alpha$ exists; its numerical value comes from substrate microscopic details.

The substrate-microscopic derivation of $\tau_{V5}$ in terms of more fundamental substrate parameters is open. The framework identifies $\tau_{V5} = \ell_P/c$ at the gravitational scale via dimensional analysis on T19 + V5 primitive structure; a closed-form derivation from more fundamental substrate timescales would tighten the identification.

The higher-order resummation of $(\ell_P/M)^2$ corrections that determines the late-time evaporation profile (Scenario A full-recovery / Scenario B modified-turnover / Scenario C Planck-mass-remnant) is open. The leading-correction analysis identifies the existence of qualitatively distinct late-time scenarios; settling which realizes requires substrate-microscopic analysis or empirical evidence.

The extension to charged BHs (Reissner-Nordström substrate analog) is open. The substrate calculation here applies to Schwarzschild-class BHs; charged-BH extensions involve T17 (gauge-field-as-rule-type) inheritance for the charged-particle Hawking emission and modified substrate-state-dependent factor.

The extension to rotating BHs (Kerr substrate analog) is open. The substrate calculation here uses spherical-symmetry assumption from BH-2; rotating-BH extensions require generalization of the saturated-surface substrate state.

---

## 9. What This Argument Establishes

The chain runs:

Substrate primitives (micro-events, chains, bandwidth, polarity, commitment, locality, V1/V5 kernels) → BH-2 (saturated decoupling surface) → BH-4 (entanglement-straddling) → substrate-Unruh argument (substrate observers near saturated surface see V5 vacuum as thermal) → imaginary-time periodicity at $\beta= 2\pi/\kappa_{\mathrm{ED}}$ from substrate-vacuum self-consistency → KMS condition → Planck distribution at $T = \kappa_{\mathrm{ED}}/(2\pi)$ → DCGT identification $\kappa_{\mathrm{ED}} \to \kappa$, $T_H = \kappa/(2\pi)$ at leading order → substrate scattering through $V_\ell^{(\mathrm{ED})}(r)$ → greybody factors identifying with Regge-Wheeler at leading order → integration over modes → Page rate $\dot M = -\alpha_{\mathrm{Page}}/M^2$ → Arc E bandwidth-budget min-bound + BH-5 area-law → Page curve with $t_{\mathrm{Page}} \approx 0.54\tau_{\mathrm{BH}}$, $S_{\mathrm{\max}} = S_{\mathrm{BH,0}}/2$ → information recovery via correlations between Hawking quanta.

Hawking radiation is now derived from substrate ontology rather than from postulated QFT-in-curved-spacetime. The mathematical content of the standard semiclassical calculation — Bogoliubov transformation, Regge-Wheeler scattering, Planck distribution, greybody factors, Page rate, Page curve — is unchanged. What changes is the foundational status: each ingredient is derived from substrate primitives via DCGT identification at leading order, with FORM-FORCED first-subleading-order corrections.

The framework reproduces standard semiclassical Hawking exactly where it has been tested. Analog Hawking experiments in BEC and acoustic systems, which match the standard spectral form within experimental precision, also match ED's leading-order prediction. Stellar-mass BH evaporation timescales (~$10^{67}$ years for $M \sim M_\odot$) match the standard semiclassical prediction. No deviation from standard semiclassical at leading order; corrections at first subleading order develop in regimes not currently tested.

What's new is the substrate-level account of the structural questions standard semiclassical leaves open:

- **The trans-Planckian problem** is resolved at the substrate level by V5 finite memory at $\tau_{V5} = \ell_P/c$. The substrate naturally provides a UV cutoff at the Planck frequency, regulating the standard derivation's reliance on arbitrarily-blueshifted modes near the horizon.
- **The information paradox** is resolved at the substrate level by entanglement-straddling (BH-4) + bandwidth-budget min-bound (Arc E) + substrate-unitarity from T18 + P11 + ED-I-06. Information is preserved at the substrate level and recovered through correlations between Hawking quanta.
- **The vacuum-state-choice issue** is bypassed: ED's V5 vacuum is a substrate-level object with its own definition, not requiring a choice between QFT vacua.
- **The pair-creation mechanism** is replaced by substrate-level entanglement-straddling, structurally more economical.

The first-subleading-order corrections at $(\ell_P/M)^2$ are the framework's substantive new substrate content. They produce:

- A high-frequency cutoff in the spectrum at $\omega \sim \omega_c = c/\ell_P$ (the Planck frequency), distinguishing ED from strict semiclassical Hawking in the trans-Planckian regime.
- A modified evaporation profile in the late stages of primordial-BH evaporation, possibly producing a stable Planck-mass remnant (cosmologically significant as a structural relic-matter component of the cosmic energy budget).
- Frequency-dependent modifications to greybody factors detectable in analog Hawking experiments at the substrate-cutoff scale.
- Modifications to the Page-curve shape at $(\ell_P/M_0)^2$ that affect the information-recovery profile.

A cross-domain feature: the V5 kernel that produces the high-frequency cutoff in Hawking radiation is the *same substrate primitive* that produces Maxwell viscoelastic memory in soft matter (via DCGT). One substrate primitive, two different physical applications across vastly different scales. This is the framework's typical cross-domain unification pattern: the same substrate machinery produces measurable phenomena in apparently unrelated domains.

For empirically tested aspects of Hawking radiation, ED predicts the same as standard semiclassical Hawking at observable precision. The framework's empirical exposure lives in regimes not currently tested: the Planck-scale cutoff in primordial-BH evaporation, the substrate-cutoff signature in analog Hawking spectra, the conditional Planck-mass remnant relic-matter scenario, and substrate-cutoff dispersion of high-energy photons over astronomical distances.

The structural case for ED's relationship to semiclassical Hawking is: **regulated completion**. The framework includes all of standard semiclassical at leading order while providing substrate-level UV regulation, structural information-paradox resolution, and conditional new content at extreme scales. ED is not a replacement; it is what the substrate produces when the standard semiclassical machinery is given a substrate-level account.

The factor that's worth emphasizing: the Hawking walkthrough introduces no new substrate primitive. Every primitive used — micro-events, chains, bandwidth, polarity, commitment, locality, V1, V5 — was already in the framework's inventory from the QM-emergence walkthroughs and the BH-arc work. The Hawking spectrum is what these primitives produce when applied to a saturated decoupling surface. The substrate inventory is unchanged; the structural-foundations theorem inventory does not grow — the Hawking calculation is a downstream consequence of BH-4 + DCGT + V5 + substrate-Unruh argument rather than a new theorem at the same structural level.

Whether the substrate primitives themselves are right is the load-bearing empirical question, as in every walkthrough. The framework stands or falls on whether participation, bandwidth, channels, polarity, commitment, V1, V5, locality, and the substrate-level structural commitments are the correct foundational concepts. The empirical exposure of the framework lives across closed sectors — soft-matter mobility, substrate-derived gravity transitions, quantum-computational ceilings, Clay-relevance results — not exclusively in Hawking radiation, where the framework reproduces empirically validated semiclassical predictions plus FORM-FORCED first-subleading-order content.

For Hawking radiation specifically, the substrate-level case is closed at leading + first-subleading order. The framework reproduces every standard semiclassical ingredient at leading order, provides substrate-level UV regulation that resolves the trans-Planckian problem, supplies a substrate-level account of information recovery via entanglement-straddling, and produces FORM-FORCED first-subleading-order corrections distinguishing ED from strict semiclassical at extreme scales. Standard semiclassical Hawking has been correct since 1974; ED supplies the substrate-level account of why.

---

## 10. References

- Hawking, S. W. "Black Hole Explosions?" *Nature* 248, 30–31 (1974).
- Hawking, S. W. "Particle Creation by Black Holes." *Communications in Mathematical Physics* 43, 199–220 (1975).
- Page, D. N. "Particle Emission Rates from a Black Hole: Massless Particles from an Uncharged, Nonrotating Hole." *Physical Review D* 13, 198–206 (1976).
- Page, D. N. "Information in Black Hole Radiation." *Physical Review Letters* 71, 3743–3746 (1993).
- Bekenstein, J. D. "Black Holes and Entropy." *Physical Review D* 7, 2333–2346 (1973).
- Unruh, W. G. "Notes on Black-Hole Evaporation." *Physical Review D* 14, 870–892 (1976).
- Kubo, R. "Statistical-Mechanical Theory of Irreversible Processes." *Journal of the Physical Society of Japan* 12, 570–586 (1957).
- Martin, P. C., Schwinger, J. "Theory of Many-Particle Systems. I." *Physical Review* 115, 1342–1373 (1959).
- Regge, T., Wheeler, J. A. "Stability of a Schwarzschild Singularity." *Physical Review* 108, 1063–1069 (1957).
- Teukolsky, S. A. "Perturbations of a Rotating Black Hole. I. Fundamental Equations for Gravitational, Electromagnetic, and Neutrino-Field Perturbations." *Astrophysical Journal* 185, 635–648 (1973).
- 't Hooft, G. "On the Quantum Structure of a Black Hole." *Nuclear Physics B* 256, 727–745 (1985).
- Maldacena, J., Susskind, L. "Cool Horizons for Entangled Black Holes." *Fortschritte der Physik* 61, 781–811 (2013).
- Steinhauer, J. "Observation of Quantum Hawking Radiation and Its Entanglement in an Analogue Black Hole." *Nature Physics* 12, 959–965 (2016).
- Proxmire, A. *Theorem 18: V1 Kernel Retardation and the Kernel-Level Arrow of Time.* April 2026.
- Proxmire, A. *Theorem 19: Newton's Law from Substrate Holographic Counting and the Identification of $\ell_P$.* April 2026.
- Proxmire, A. *The Diffusion Coarse-Graining Theorem: Substrate-to-Continuum Bridge for Canonical-ED Dynamical Content.* April 2026.
- Proxmire, A. *Black Hole Architecture: Horizon as Saturated Decoupling Surface, Information Architecture, and Area-Law Entropy.* May 2026.
- Proxmire, A. *Arc Hawking: V5-Mediated Hawking Spectrum, Greybody Factors, Page Rate, Page Curve, and Substrate-Level Resolution of the Information Paradox.* May 2026.
- Proxmire, A. *Arc E (Entanglement): Tensor-Product Composition, Schmidt Decomposition, Monogamy from Bandwidth-Budget, No-Signaling Three-Lock, von Neumann Entropy.* May 2026.
- Proxmire, A. *Event Density: One Substrate, Three Domains.* April 2026.
- The full Event Density corpus, including all forced theorems and supporting memos, is available at https://github.com/allen-proxmire/event-density.
