---
title: |
  Event Density — Public Test Inventory
  \large{A living catalog of falsifiable predictions and experimental status}
author: Allen Proxmire
date: May 2026 (v2 — supersedes February 2026 *Open Note for Experiments*)
---

## Foreword

This is a stand-alone catalog of falsifiable predictions of the **Event Density (ED) framework** and their current empirical status. Each entry is a short, self-contained experimental claim designed to confirm or refute a specific ED prediction.

The framework's results to date span nine sectors of substrate-level architectural closure: quantum-mechanical foundations, form-level quantum field theory, classical fluid dynamics (Navier–Stokes), non-Abelian gauge theory (Yang–Mills), substrate gravity, curvature emergence, soft-matter mobility, black-hole architecture, and quantum computation. Each closed sector produced sharp predictions; this document collects them into a single inventory readable without the technical machinery.

The methodology is consistent across the program: **the structural form of each prediction is derived from substrate primitives; specific numerical thresholds are calibrated empirically rather than computed in closed form**. Where calibration anchors are already in place, they are noted. Where calibration is the next step, the experimental path is named.

This document supersedes the February 2026 *Open Note for Experiments*. It will continue to expand as new predictions are derived and new experimental anchors are calibrated.

**Repository:** `https://github.com/allen-proxmire/event-density`

---

## Status legend

- **[PASSED]** — empirical confirmation in published data
- **[ANCHORED]** — prediction calibrated to existing empirical observation
- **[IN PROGRESS]** — active experimental program awaiting result
- **[ACTIVE]** — test fully specified, awaiting execution
- **[OPEN]** — prediction stated, technique requires development
- **[REFRAMED]** — earlier prediction sharpened under a closed arc

---

## How to read this document

Each test is presented in the same compact structure:

> **Test name** — *status*
>
> **Prediction.** What ED says. How it differs from the standard expectation.
>
> **Test.** The experimental setup, briefly.
>
> **Decisive observation.** What confirms; what refutes.
>
> *Derived in:* arc or paper reference.

Across sections, the underlying invariants are shared: substrate participation density $\rho$, gradient sparsity $\sigma = |\nabla\rho|\ell_P^2/\rho_\mathrm{local}$, cross-bandwidth $\Gamma_\mathrm{cross}$, multiplicity $\mathcal{M}$ (the ED analogue of entropy), commitment-injection rate $\Lambda$, and the V1 finite-width vacuum kernel. Every prediction below is a consequence of one or more of these substrate quantities crossing a threshold.

\newpage

# Section 1 — Quantum Mechanics and Quantum Computing

The unifying result for this section: **all quantum-computing platforms — including matter-wave interferometers — operate by holding a low-multiplicity unresolved state and fall to the same three substrate-level failure modes**. Three architectural classes (A: engineered-low-multiplicity; B: global-geometric-rigidity; C: high-multiplicity-redundancy) exhaust the protection strategies. The matter-wave quantum-classical boundary at 140–250 kDa and the qubit-system multiplicity walls are the same substrate-determined boundary projected onto two platforms.

## 1.1 Matter-wave quantum-classical boundary at 140–250 kDa — *[ANCHORED]*

**Prediction.** A neutral molecule's coherence in a matter-wave interferometer fails when its internal multiplicity (rotational + vibrational + electronic activated modes) crosses a substrate-determined critical value $\mathcal{M}_\mathrm{crit}$. The boundary is set by *internal molecular structure*, not by mass alone. Below the threshold, fringes are stable; above it, no environmental engineering recovers them.

**Test.** Matter-wave interferometry across mass-matched isomers with different internal-DOF structure — e.g., highly symmetric vs floppy molecules at fixed mass. Coherence should track internal-DOF multiplicity, not mass.

**Decisive observation.** A pair of mass-matched isomers showing the *same* fringe behavior would refute the multiplicity-driven reading. A pair showing systematically different boundaries at fixed mass confirms it.

*Derived in:* Arc Q-COMPUTE, Memo 6 § 7.4; QC Foundations Paper § 7.

## 1.2 Cross-platform identity: matter-wave boundary ↔ qubit-system multiplicity wall — *[ACTIVE]*

**Prediction.** The matter-wave Q-C boundary mass and the qubit-system effective-multiplicity wall are evaluations of *the same* substrate constant $\mathcal{M}_\mathrm{crit}$, projected onto two different platforms. Sharper measurement of one directly constrains the location of the other.

**Test.** Cross-platform calibration program: parallel sharpening of the matter-wave boundary (mass-matched isomers, ultra-cold vacuum extension) and direct multiplicity tomography in scaled SC qubit arrays (cross-talk, leakage, system-level coherence vs $N_\mathrm{qubits}$).

**Decisive observation.** A consistent value of $\mathcal{M}_\mathrm{crit}$ extracted from both platforms confirms the cross-platform identity — the framework's strongest unification claim. Inconsistent values refute it.

*Derived in:* Arc Q-COMPUTE Memo 5; QC Foundations Paper § 7.1.

## 1.3 Class A system-multiplicity wall in superconducting qubit arrays — *[IN PROGRESS]*

**Prediction.** Pure-Class-A superconducting qubit platforms hit a hard scaling ceiling at a substrate-determined system size, regardless of T₁ or T₂ improvements, regardless of dynamical decoupling overhead. Continued unbounded improvement of system-level effective coherence with qubit count, *without composition with logical-qubit encoding*, is structurally impossible past the wall.

**Test.** Measure $\tau_\mathrm{QC}^\mathrm{logical}$ in scaled SC qubit systems vs $N_\mathrm{qubits}$ at fixed code distance, while continuing physical-qubit T₁/T₂ engineering.

**Decisive observation.** A plateau at the predicted multiplicity-determined size confirms the wall. Continued monotonic improvement past the projected wall, with no plateau in the explored range, refutes the framework.

*Derived in:* Arc Q-COMPUTE Memo 5; QC Foundations Paper § 7.4.

## 1.4 Class B exponential coherence advantage — *[OPEN]*

**Prediction.** Topological-qubit platforms (Majorana, anyonic, Chern-band photonic) can outrun the Class A wall by an exponential factor $\sim \exp(\Delta_\mathrm{top}/T_\mathrm{eff})$, where $\Delta_\mathrm{top}$ is the topological gap and $T_\mathrm{eff}$ is the substrate-equivalent perturbation temperature. The binding constraint shifts from environmental coupling rate to *topology stability*.

**Test.** Coherence measurements in topological-qubit platforms as a function of gap and temperature, with explicit decomposition of binding mechanism into environmental rate vs gap-perturbation rate.

**Decisive observation.** Polynomial dependence on $\Delta_\mathrm{top}/T_\mathrm{eff}$ (instead of exponential) refutes the gap-suppression structure. A topological platform with stable topology but no exponential coherence advantage over Class A also refutes.

*Derived in:* Arc Q-COMPUTE Memo 5–6; QC Foundations Paper § 6.3, § 7.2.

## 1.5 Class C correlation-budget saturation — *[ACTIVE]*

**Prediction.** Redundancy-based architectures (multi-axis photonic, bosonic codes) exhibit a substrate-determined correlation-budget plateau. Past a critical pathway count $N_\mathrm{corr}$, additional redundancy stops paying because correlated noise channels become dominant. Class C cannot exceed single-pathway coherence by more than an O(1) factor at saturation.

**Test.** Extend Hafezi-class multi-timescale photonic lattices to higher axis counts (3, 4, 5+); scale bosonic-code distance and measure logical-qubit lifetime.

**Decisive observation.** A clean plateau at the predicted $N_\mathrm{corr}$ confirms the bounded-redundancy structure. Continued exponential scaling past saturation refutes.

*Derived in:* Arc Q-COMPUTE Memo 5; QC Foundations Paper § 6.4.

## 1.6 Multi-timescale FPM relaxation in nonlinear photonic lattices — *[PASSED]*

**Prediction.** Adding a second timescale to a single-ring resonator dramatically relaxes the strict frequency-phase-matching (FPM) constraint, broadens harmonic generation, and produces near-100% device yield with disorder tolerance.

**Empirical status.** Confirmed by the Hafezi group at the University of Maryland (multi-timescale resonator-lattice work, arXiv:2506.15016, 2025). 100% yield, two-octave harmonic generation, edge-localized harmonic propagation. The framework identifies this as Class C empirical demonstration in the photonic platform.

*Derived in:* ED-I-18 (Multi-Timescale Photonics, Feb 2026); Arc Q-COMPUTE Memo 4–5.

## 1.7 Hyper-coherence in ultra-symmetric engineered systems — *[ANCHORED]*

**Prediction.** Systems whose substrate gradients are extremely simple (lattice-symmetry-collapsed superconductors, BECs, symmetric optical lattices, deeply trapped cold atoms) show coherence consistent with substrate-level low-multiplicity engineering. Coherence times beyond what coupling-rate models predict appear when the architectural mechanism suppresses local multiplicity rather than only suppressing environmental coupling.

**Empirical status.** Anchored. Bulk superconductors below $T_c$ exhibit zero resistance, Meissner effect, and flux quantization — all reproduced under Class A substrate-level reading (lattice symmetry collapses $\mathcal{M}$; thermal injection above $T_c$ crosses condition (iii) threshold). Macroscopic quantum coherence in superconducting circuits (Devoret–Martinis–Clarke) reproduced as preservation of low-multiplicity geometry.

*Derived in:* ED-I-01 (Superconductivity, Feb 2026); ED-I-23 (Josephson Junctions, Mar 2026); Arc Q-COMPUTE Memo 2.

## 1.8 Josephson-junction macroscopic quantum tunneling: WKB structure from DCGT — *[ANCHORED]*

**Prediction.** The exponential MQT-rate dependence on barrier parameters is recovered directly from DCGT (Diffusion Coarse-Graining Theorem) cross-bandwidth structure: $\tau_\mathrm{MQT}^{-1} \sim \omega_0\,\exp[-\alpha\!\int_\mathrm{barrier}\sigma\,d\ell]$. Standard physics has this as WKB; ED derives it.

**Empirical status.** Anchored. Devoret–Martinis–Clarke 1985 measurements of MQT-rate exponential dependence on barrier height and width are reproduced as DCGT $\kappa$-function evaluation at the engineered $\sigma$-profile.

*Derived in:* ED-I-23 (Josephson Junctions); ED-I-29 (Tunneling); Arc Q-COMPUTE Memo 2 § 3.3.

## 1.9 Quantum error correction as Class A + Class C composition — *[IN PROGRESS]*

**Prediction.** Surface-code-based fault-tolerant quantum computers are *meta-architectural compositions* of Class A (physical-qubit level: low-multiplicity engineering) with Class C (logical encoding: redundancy across many physical qubits). Their scaling is bounded by the substrate-level identities of both layers — physical-layer Class A walls + logical-layer Class C correlation budget.

**Test.** Track logical-qubit lifetime $\tau_\mathrm{QC}^\mathrm{logical}$ against code distance + physical T₁/T₂ across major fault-tolerant programs (IBM, Google, IonQ, etc.).

**Decisive observation.** Logical lifetime that exceeds the framework-predicted Class A wall + Class C plateau composition without invoking Class B (topological) subsystems would refute the framework's exhaustiveness claim.

*Derived in:* Arc Q-COMPUTE Memo 4 § 5.5; QC Foundations Paper § 6.5.

## 1.10 Bell correlation degradation with ED-multiplicity — *[OPEN]*

**Prediction.** Entanglement-based correlations (Bell, CHSH-class measurements) degrade with the ED-multiplicity load of the entangled system, even when environmental coupling is held constant. The mechanism is multiplicity-driven individuation, not coupling-driven decoherence.

**Test.** Send entangled photons or trapped-ion pairs through structured media of varying ED-complexity; measure correlation strength at fixed environmental conditions.

**Decisive observation.** A complexity-dependent degradation — at fixed coupling — confirms the multiplicity-driven mechanism. A coupling-only correlation supports the standard reading.

*Derived in:* Arc Q-COMPUTE Memo 3.

\newpage

# Section 2 — Galactic Gravity and Cosmology

The unifying result for this section: **Newton's gravitational constant, the MOND transition acceleration $a_0$, the deep-MOND geometric-mean combination rule, and the slope-4 Tully–Fisher relation all derive from substrate primitives without free parameters.** Galactic-scale phenomenology becomes substrate-grounded; cluster-scale and full-cosmological work is downstream.

## 2.1 Newton's gravitational constant from substrate — *[ANCHORED]*

**Prediction.** $G = c^3\ell_P^2/\hbar$ — the gravitational constant derived as a relationship among the speed of light, the Planck length, and Planck's constant. The substrate length scale is identified with $\ell_P$ as a derived consequence of Newton-recovery, not a postulate.

**Empirical status.** Anchored. Plug in measured $\ell_P$ and $\hbar$, recover $G$ with no fit parameters.

*Derived in:* Arc SG (Substrate Gravity, Apr 2026), Theorem T19; SG-Foundations Paper.

## 2.2 MOND transition acceleration $a_0 = c\,H_0/(2\pi)$ — *[ANCHORED] within ~10%*

**Prediction.** $a_0 \approx 1.08 \times 10^{-10}$ m/s² as $a_0 = c\,H_0/(2\pi)$ — derived from the cosmic horizon's dipole-projection contribution to a local accelerating object's substrate environment. The factor of $2\pi$ is structural (azimuthal period of the leading anisotropic projection mode), not phenomenological.

**Empirical status.** Anchored. Empirical MOND constant is ~$1.2 \times 10^{-10}$ m/s². Match within ~10%, parameter-free. Hubble-tension band ($H_0$ between 67–73 km/s/Mpc) translates to a ~15% prediction band on $a_0$.

*Derived in:* Arc SG, Theorem T20; SG-Foundations Paper § 5.

## 2.3 Slope-4 baryonic Tully–Fisher relation $v^4 = G\,M\,a_0$ — *[ANCHORED]*

**Prediction.** The flat-rotation-curve speed at galactic outskirts scales with baryonic mass to the fourth power, with proportionality constant $G \cdot a_0$ expressed entirely in fundamental substrate quantities. Zero intrinsic scatter predicted in the deep-MOND asymptotic regime; observed scatter dominated by mass-measurement uncertainty.

**Empirical status.** Anchored against SPARC galaxy-rotation-curve catalog (~150 galaxies, sub-0.1-dex scatter dominated by baryonic-mass uncertainty).

*Derived in:* Arc SG, Theorem T21 + ED Combination Rule; SG-Foundations Paper § 7.

## 2.4 Dwarf galaxy outer-radius mass discrepancy: Active > Quiet — *[PASSED]*

**Prediction.** Dynamically active dwarf galaxies (recent star formation, mergers, AGN feedback) should exhibit larger outer-radius mass discrepancies than quiescent dwarfs at fixed baryonic mass. Sustained internal activity generates ED gradients that diffuse into smooth temporal halos.

**Empirical status.** Passed. SPARC-dataset analysis of 46 dwarf galaxies yields ⟨D⟩ ≈ 6.01 for Active dwarfs vs 3.94 for Quiet — a 53% higher outer-radius mass discrepancy. Two clean visual bands at D ≈ 3–4 (Quiet) and D ≈ 5–6 (Active). First completed astrophysical test of the framework.

*Derived in:* ED-04.5 (Temporal Tension in Dwarf Galaxies, SPARC-Based Test).

## 2.5 Halo lag in cluster collisions — *[ACTIVE]*

**Prediction.** In Bullet-Cluster-class high-speed cluster collisions, ED's temporal-tension halo cannot follow the baryonic mass instantaneously. Predicted: halo lags behind baryonic mass, shears and stretches, produces smeared lensing peaks and vortex-like trailing wakes. CDM predicts collisionless passage with lensing peaks aligned to dark matter.

**Test.** Compare lensing maps to X-ray gas distributions in cluster collisions. Look for elongated, asymmetric, or dragged halo contours; identify temporal wakes.

**Decisive observation.** Clean collisionless passage refutes ED. Lagging, sheared halo supports it.

*Derived in:* ED-XX (Environment Sourcing of Temporal Tension).

## 2.6 Activity-dependent halo strength — *[ACTIVE]*

**Prediction.** Galaxy halos depend on dynamical activity (rotation, turbulence, star formation, feedback, bar dynamics, merger history), not on mass alone. Galaxies with identical baryonic mass but different dynamical states should exhibit different halo strengths.

**Test.** Compare rotation curves of galaxies matched in mass but differing in star-formation rate, bar dynamics, or merger history.

**Decisive observation.** Mass-only correlation supports CDM. Activity-dependent correlation supports ED.

*Derived in:* ED-XX; Arc SG follow-on work.

## 2.7 Hysteresis in post-starburst halos — *[ACTIVE]*

**Prediction.** Temporal tension relaxes slowly. A galaxy that recently experienced a starburst, merger, AGN feedback, or bar-driven inflow should retain an enhanced halo even after the activity subsides. CDM predicts no such memory effect.

**Test.** Identify post-starburst galaxies; measure halo strength; compare to galaxies with similar present-day activity but different recent histories.

**Decisive observation.** Memory effect supports ED. Instantaneous response supports CDM.

## 2.8 Reduced small-scale substructure — *[ACTIVE]*

**Prediction.** Temporal tension is diffusive — predicts smoother halo profiles, suppressed substructure, fewer dwarf satellites, weaker strong-lensing flux anomalies, smoother low-mass rotation curves. CDM predicts abundant subhalos and clumpy small-scale structure.

**Test.** Count dwarf satellites around Milky-Way analogues; analyze strong-lensing flux anomalies; compare high-resolution rotation curves to CDM substructure predictions.

**Decisive observation.** A smooth, low-clump halo profile supports ED. A highly clumpy halo supports CDM.

\newpage

# Section 3 — Soft-Matter Mobility and Non-Newtonian Rheology

The unifying result: **a single architectural principle (P4 mobility-capacity bound) plus a memory primitive (V5 cross-chain memory) reproduces five canonical non-Newtonian families** — Krieger–Dougherty divergence, discontinuous shear-thickening, Cross-class shear-thinning, mixed regimes, and Maxwell viscoelasticity. The exponent $\beta \approx 2$ is shared across ten chemically unrelated diffusion experiments.

## 3.1 Universal Mobility Law $\beta \approx 2$ — *[PASSED] across 10 systems*

**Prediction.** The mobility-vs-saturation curve in crowded systems takes the form $M(\rho) = M_0(1 - \rho/\rho_\mathrm{max})^\beta$ with $\beta$ near 2, regardless of the system's microscopic physics, provided the saturation mechanism is geometrically generic.

**Empirical status.** Passed. Ten chemically unrelated systems — PMMA colloids, hard-sphere colloids, sucrose-water, glycerol-water, BSA, lysozyme, PEG-water, dextran, casein micelles, Ludox silica — all fit the form with $\beta = 1.72 \pm 0.37$, $R^2 > 0.986$. Canonical ED value is $\beta = 2$; data scatter clusters by saturation mechanism (cooperative networks at $\beta \approx 2.31$, steric at $\approx 1.76$, gradual/electrostatic at $\approx 1.38$).

*Derived in:* Universal Mobility Law paper (Apr 2026); P4-NonNewtonian extension.

## 3.2 FRAP $t^{1/6}$ scaling at high BSA concentration — *[IN PROGRESS]*

**Prediction.** Fluorescence recovery after photobleaching at deep BSA concentration follows non-Fickian recovery profile with $R(t) \sim t^{1/6}$ front propagation, distinct from standard $t^{1/2}$ Fickian diffusion.

**Empirical status.** In progress. Pre-registered protocol submitted to Creative Proteomics; quote received April 2026; technician-team review pending. Engineering frontier of mobility-channel testing.

*Derived in:* P4-NonNewtonian; Universal Mobility Law experimental program.

## 3.3 Krieger–Dougherty divergence and discontinuous shear-thickening — *[ANCHORED]*

**Prediction.** Both divergence-near-jamming (paint, blood, slurries) and discontinuous shear-thickening (cornstarch in water, body-armor fluids) follow from the same architectural principle (P4) applied to two different state variables: particle volume fraction (Krieger-Dougherty) vs strain rate (DST). Same exponent class, derived rather than fit.

**Empirical status.** Anchored. Both phenomenologies have a century of empirical support; ED reframes them as shared-architecture consequences.

*Derived in:* P4-NonNewtonian Foundations.

\newpage

# Section 4 — Black Holes and Strong-Field Gravity

The unifying result: **black-hole architecture is structurally complete at the substrate level** without invoking the standard paradoxes. Horizons are coarse-grained statistical features of $\Gamma_\mathrm{cross}$ collapse; singularities don't exist as physical objects (replaced by saturated participation zones); information cannot cross horizons but entanglement can; evaporation is participation re-routing. The standard paradoxes (information loss, firewalls, complementarity, singularity) don't arise because the four assumptions that generate them are not imposed at substrate level.

## 4.1 Hawking spectrum from substrate cross-chain correlations — *[OPEN] (next natural arc)*

**Prediction.** The thermal spectrum of Hawking radiation should match $T_H = \kappa/(2\pi)$ as a structural recovery from substrate-level asymmetric participation flow at the saturated decoupling surface. The mechanism is in hand from BH-4 (participation re-routing through pair-creation events at the surface); the explicit V5 cross-chain correlation calculation is the load-bearing remaining work.

**Test.** Black-hole evaporation observations; Hawking-temperature measurements (e.g., analog-gravity laboratory analogues — BEC sonic horizons).

**Decisive observation.** Match to $T_H = \kappa/(2\pi)$ confirms the substrate-level mechanism. Deviation is a falsifier.

*Derived in:* Arc BH Memo 4; BH-Foundations Paper § 5.4.

## 4.2 Bekenstein–Hawking area-law form — *[ANCHORED]*

**Prediction.** $S \propto A/\ell_P^2$ — entropy scales with horizon area in Planck units. Form derived structurally from two-dimensional decoupling-surface support + gradient saturation + per-patch finite alphabet. The 1/4 coefficient inherits from substrate motif counting; closed-form derivation is downstream work analogous to closed-form derivation of the substrate constants in QC.

**Empirical status.** Form anchored. Coefficient inherited.

*Derived in:* Arc BH Memo 5; BH-Foundations Paper § 6.

## 4.3 BHPT phase shift as a global path-integrated invariant — *[ANCHORED]*

**Prediction.** Black-hole-perturbation-theory phase shifts $\delta_{\ell m}$ are global path-integrated invariants of minimal ED-channels traversing the saturated-gradient exterior. Helicity preservation under axisymmetric backgrounds (Schwarzschild) and helicity flip under frame-dragging (Kerr) follow from anisotropy-basis transport; Kerr twist scales with integrated background vorticity.

**Empirical status.** Form anchored. Numerical values match GR-class predictions to the extent that the acoustic-metric scalar-tensor framework (Arc ED-10) reproduces Schwarzschild and Kerr metrics. LIGO/Virgo quasinormal-mode catalog provides empirical anchors.

*Derived in:* Arc BH Memo 6; BH-Foundations Paper § 7.

## 4.4 No-singularity prediction: finite-thickness saturated zone — *[OPEN]*

**Prediction.** Black-hole interiors do not contain singularities. The acoustic-metric scalar-tensor reading breaks down at the substrate-saturation regime ($\sigma \gtrsim \beta_\mathrm{crit}$); substrate dynamics remain finite throughout. The interior is a finite-thickness saturated participation zone, not a singular point.

**Test.** Indirect — interior observations are not directly accessible. Tests via implications: cluster-scale gravitational-wave observations, late-time evaporation tail behavior, analog-gravity simulations.

**Decisive observation.** Any observational signature inconsistent with substrate-level interior finiteness would refute.

*Derived in:* Arc BH Memo 3; BH-Foundations Paper § 4.

## 4.5 Universal horizon mechanism across BH/Rindler/cosmic/acoustic — *[ANCHORED]*

**Prediction.** Black-hole event horizons, Rindler horizons (accelerated frames), cosmological horizons, and acoustic horizons (analog gravity) all share a single substrate-level mechanism: cross-bandwidth $\Gamma_\mathrm{cross}$ collapse at the surface where $\sigma$ exceeds the threshold $\log(R_\mathrm{cg}/\ell_P)$.

**Empirical status.** Anchored. The thermodynamic-style features shared across these four horizon classes (temperature, entropy, evaporation analogues) — long known empirically — are reproduced as one substrate phenomenon.

*Derived in:* Arc BH Memo 2; BH-Foundations Paper § 3.

\newpage

# Section 5 — Condensed Matter and Superconductivity

## 5.1 Mesoscopic transport threshold $L_\mathrm{crit}$ — *[ACTIVE]*

**Prediction.** The transition between ballistic and diffusive transport in mesoscopic conductors is governed by a structural threshold in event-density gradient saturation, not by scattering amplitudes. Conductance $G(L)$ exhibits a non-analytic kink at a critical channel length $L_\mathrm{crit}$ where the ED-gradient saturates.

**Test.** Fabricate quasi-1D channels with tunable length (graphene nanoribbons, carbon nanotubes, GaAs/AlGaAs heterostructures, metallic nanowires); measure conductance across length sweep; identify predicted kink.

**Decisive observation.** A clean non-analytic kink at a reproducible ED-complexity-dependent threshold confirms ED. A smooth crossover with no structural transition refutes.

*Derived in:* ED Open Note (Feb 2026); under review for sharpening under Arc Q-COMPUTE Class A reading.

## 5.2 Superconducting phase-stiffness saturation plateau — *[ACTIVE]*

**Prediction.** Superfluid phase stiffness $J(T)$ in thin-film superconductors exhibits a characteristic flattening before the superconducting transition. Standard BCS and KT models predict smooth monotonic softening. ED predicts an early saturation plateau driven by event-density constraints.

**Test.** Use thin-film superconductors with tunable geometry (NbN, MoGe, YBCO, amorphous InOx). Measure $J(T)$ via THz spectroscopy or two-coil mutual inductance; identify plateau onset.

**Decisive observation.** A clear stiffness plateau at an ED-complexity-dependent temperature is a decisive ED signature. Smooth monotonic softening with no plateau falsifies.

*Derived in:* ED Open Note; consistent with ED-I-01 superconductivity reading.

## 5.3 Casimir-gradient saturation at sub-100 nm separation — *[ACTIVE]*

**Prediction.** Near-field Casimir-class forces saturate at sub-100 nm separations as the ED-field gradient between approaching surfaces reaches its maximum sustainable value. Standard Casimir–Lifshitz theory predicts smooth $F \propto 1/d^4$ divergence.

**Test.** MEMS/NEMS or microcantilever platforms with tunable separation (gold-gold in salt water, gold-silica in dielectric fluids, graphene-substrate cavities). Measure $F(d)$ down to ~10 nm.

**Decisive observation.** A clear force plateau at an ED-complexity-dependent distance is a decisive ED signature. A smooth divergence with no plateau refutes.

*Derived in:* ED Open Note; ED-I-16 (Casimir Self-Assembly).

## 5.4 High-Tc superconductors as intrinsically low-multiplicity materials — *[ANCHORED]*

**Prediction.** High-temperature superconductors (cuprates, pnictides, nickelates) share a common ED-geometry signature: their lattice structure is *intrinsically* low-multiplicity even before cooling. Cooling completes a coherence already partially formed by lattice symmetry. This unifies cuprates, pnictides, and nickelates under a single ED principle.

**Empirical status.** Anchored. Three predicted features — short coherence lengths, unconventional pairing symmetries, complex phase diagrams — match observed properties of high-Tc materials.

*Derived in:* ED-I-01 § 8.

\newpage

# Section 6 — Photonics, Microresonators, and Phononics

## 6.1 Microresonator linewidth asymmetry — *[ACTIVE]*

**Prediction.** Optical linewidths in high-Q microresonators split into asymmetric branches when the ED-gradient becomes uneven across the cavity. Standard cavity theory predicts symmetric Lorentzian broadening.

**Test.** SiN microrings, AlN/LiNbO₃ resonators, silica microtoroids, chalcogenide micro-racetracks. Sweep detuning and pump power; measure transmission spectrum; identify asymmetric splitting.

**Decisive observation.** Reproducible asymmetric splitting at an ED-complexity-dependent threshold confirms. A symmetric Lorentzian with no structural splitting refutes.

## 6.2 Photonic crystal ED-gradient confinement limit — *[ACTIVE]*

**Prediction.** Nanophotonic cavities exhibit a saturation of field confinement when the ED-gradient inside the cavity reaches its structural maximum. Beyond this point, further geometric confinement does not increase local field intensity. Standard photonic-crystal theory predicts continuous enhancement as mode volume shrinks.

**Test.** Si/SiN photonic-crystal nanobeams, L3/H0 defect cavities, high-contrast 2D slabs, inverse-designed nanocavities. Vary defect geometry; measure local field via nonlinear emission, SHG, or photoluminescence.

**Decisive observation.** A reproducible confinement plateau at an ED-complexity-dependent mode volume confirms. Smooth, unbounded enhancement with no plateau refutes.

## 6.3 Multi-timescale comb formation threshold — *[ACTIVE]*

**Prediction.** Optical frequency-comb formation in microresonators is governed by multi-timescale event-density locking, not by smooth nonlinear dispersion alone. Comb formation exhibits a sharp threshold transition when ED locking activates. Standard Lugiato–Lefever theory predicts continuous transition from modulation instability to soliton formation.

**Test.** SiN microrings, AlN/LiNbO₃ resonators, silica microtoroids, chalcogenide platforms. Sweep pump power and detuning; monitor comb spectra; identify sharp onset.

**Decisive observation.** A reproducible ED-complexity-dependent threshold for stable comb formation confirms. A smooth, continuous transition refutes.

## 6.4 ED-limited soliton step height — *[ACTIVE]*

**Prediction.** Discrete soliton steps observed in pumped microresonators saturate at a maximum height set by the substrate's gradient ceiling. Standard LLE theory predicts smooth scaling of step height with pump power.

**Test.** Use microcomb-capable resonators with tunable pump power and detuning. Measure soliton-step height; identify saturation plateau.

**Decisive observation.** Reproducible ED-complexity-dependent saturation height confirms. Smooth, unbounded increase refutes.

## 6.5 Chiral-phonon ED-vorticity entrainment — *[ACTIVE]*

**Prediction.** Chiral phonon modes in nonmagnetic crystals (α-quartz, transition-metal dichalcogenides, polar/piezoelectric lattices) generate orbital angular-momentum currents via rotating ED-flow. The orbital-current magnitude scales with ED-vorticity, local ED-tension, and lattice-electron participation bandwidth — *not* with phonon population alone, magnetic susceptibility, or band-structure symmetry.

**Test.** Apply controlled thermal gradient to bias phonon chirality; measure orbital current via XMCD, Kerr rotation, or orbital Hall probes; compare scaling to phonon-population vs ED-tension predictions.

**Decisive observation.** Orbital current scaling with ED-tension and phonon vorticity, not phonon number, confirms. Absence of entrainment refutes.

*Derived in:* ED-I-21 (Chiral Phonons).

## 6.6 Orbital Seebeck ED-tension test — *[ACTIVE]*

**Prediction.** A thermal gradient in nonmagnetic crystals with chiral phonon modes generates orbital angular-momentum current proportional to ED-tension, not to charge-carrier density or magnetic ordering. The effect persists when phonon coherence is degraded, scales with ED-tension at fixed phonon population, and appears in any lattice supporting circular ED-flow.

**Test.** Quartz, h-BN, strained graphene, polar oxides. Hold phonon population constant via controlled illumination or fixed heating power; vary thermal gradient; measure orbital current.

**Decisive observation.** Current scaling with ED-tension rather than phonon number confirms. Current collapse with phonon-coherence loss refutes.

## 6.7 ED-entrainment universality across rotating fields — *[OPEN]*

**Prediction.** Any rotating ED-flow structure — phononic, photonic, excitonic, polaritonic, acoustic — must entrain overlapping ED-flow loops and produce orbital angular-momentum currents. This universality is structurally specific to ED and not present in standard phonon or spin-transport models.

**Test.** Optical vortex beams, exciton vortices, polariton vortices, acoustic vortices, mechanical micro-rotors. Overlap with nonmagnetic crystals; measure induced orbital magnetization or current.

**Decisive observation.** Observation of orbital currents from any rotating field confirms ED-entrainment universality. Failure of non-phononic entrainment refutes.

*Derived in:* ED-I-21; structurally consistent with Arc ED-10 acoustic-metric framework.

\newpage

# Section 7 — Cross-Cutting Predictions

A small set of predictions cut across multiple domains, reflecting the framework's substrate-level identity.

## 7.1 Cross-domain $\Gamma_\mathrm{cross}$ collapse mechanism — *[ANCHORED]*

**Prediction.** The same substrate-level mechanism — cross-bandwidth $\Gamma_\mathrm{cross}$ collapse at substrate gradient threshold — produces black-hole horizon formation, qubit-system condition (ii) failure, photonic-cavity decoupling, Rindler-horizon formation in accelerated frames, and acoustic-horizon formation in analog-gravity systems. Five empirical phenomena, one substrate-level mechanism, scales separated by ~50 orders of magnitude in physical length.

**Empirical status.** Anchored. The cross-domain consistency is the program's strongest cross-domain identity prediction.

*Derived in:* Arc D (DCGT, Apr 2026); cross-arc work in Arc BH Memo 2 + Arc Q-COMPUTE Memo 5.

## 7.2 Form-FORCED / value-INHERITED methodology as testable signature — *[ANCHORED]*

**Prediction.** Across every closed sector (QM emergence, NS, MHD, Yang-Mills, substrate gravity, curvature emergence, soft-matter mobility, black-hole architecture, quantum computation), the framework derives the *form* of empirical regularities and inherits *specific numerical values* from substrate constants. This methodological consistency itself is a cross-domain pattern: any closed-form derivation of any inherited substrate constant in one sector should produce consistent values when projected to another sector.

**Empirical status.** Anchored across nine closed sectors. Future closed-form derivations of $\mathcal{M}_\mathrm{crit}$ (QC), $\log g$ (BH entropy), $\kappa/|\hat N'|$ (ED-SC) should yield mutually consistent values.

*Derived in:* Cross-program methodology; visible in every Foundations paper.

\newpage

# Status summary at a glance

**[PASSED]:** dwarf galaxy outer-radius mass discrepancy (Active > Quiet); multi-timescale FPM relaxation (Hafezi 2025); Universal Mobility Law $\beta \approx 1.72$ across 10 systems.

**[ANCHORED]:** matter-wave Q-C boundary as multiplicity wall; Newton's $G$ from substrate; MOND $a_0$ within 10%; slope-4 Tully–Fisher; hyper-coherence in ultra-symmetric SC; JJ MQT WKB from DCGT; Krieger–Dougherty + DST + viscoelasticity; BH area-law form; BHPT phase-shift structure; universal horizon mechanism; high-Tc as intrinsically low-multiplicity; cross-domain $\Gamma_\mathrm{cross}$ collapse; form-FORCED / value-INHERITED methodology.

**[IN PROGRESS]:** SC-qubit system-multiplicity wall; FRAP $t^{1/6}$ scaling at high BSA; quantum error correction as Class A + Class C composition.

**[ACTIVE]:** mass-matched isomer matter-wave test; cross-platform calibration of $\mathcal{M}_\mathrm{crit}$; Class C correlation-budget plateau; Bell correlation degradation with multiplicity; halo lag in cluster collisions; activity-dependent halo strength; post-starburst hysteresis; reduced small-scale substructure; mesoscopic transport threshold; SC phase-stiffness saturation; Casimir-gradient saturation; microresonator linewidth asymmetry; photonic-crystal ED-gradient limit; multi-timescale comb formation; ED-limited soliton step; chiral-phonon vorticity; orbital Seebeck.

**[OPEN]:** Class B exponential coherence advantage (topological qubits); Hawking spectrum; no-singularity interior observation; ED-entrainment universality across rotating fields.

---

## Closing notes

The framework's empirical posture is mixed by design. The form-derivations are sharp and falsifiable; specific numerical thresholds inherit from substrate constants whose closed-form derivation is downstream work — analogous to how Bekenstein–Hawking's $1/4$ entropy coefficient or Planck's specific value of $\hbar$ are anchored empirically in standard physics. The list above maps the empirical frontier where each anchor sits.

This document will continue to expand as new predictions are derived and new experimental anchors are calibrated. Repository at `https://github.com/allen-proxmire/event-density`. Open-access papers (architectural-level Foundations papers for Substrate Gravity, Black Holes, and Quantum Computing; Universal Mobility Law; Theorem 17 / 18; NS Synthesis; ED-QFT Unified Overview; *Event Density: One Substrate, Three Domains*; *Event Density Foundations*) archived through Zenodo.

— Allen Proxmire, May 2026
