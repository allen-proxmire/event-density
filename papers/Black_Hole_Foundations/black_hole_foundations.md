---
title: |
  Black Holes in Event Density\
  \large A Substrate-Level Architecture
author: Allen Proxmire
date: May 2026
---

## Abstract

The Event Density (ED) program presents a substrate ontology under which black-hole physics emerges as a structural consequence of substrate participation-channel dynamics rather than as a property of a fundamental spacetime metric. This paper integrates the seven-memo Arc BH closure (2026-05-01) into a single architectural account of the black-hole sector. **Horizons are decoupling surfaces:** under the Diffusion Coarse-Graining Theorem (DCGT), a horizon is the surface where cross-participation bandwidth $\Gamma_\mathrm{cross}$ falls below hydrodynamic-window resolution, governed by the substrate condition $|\nabla\rho|\ell_P^2/\rho_\mathrm{local} \gtrsim \log(R_\mathrm{cg}/\ell_P)$. The mechanism universalizes across black-hole, Rindler, cosmological, and acoustic horizons. **Singularities do not exist:** three independent substrate constraints — finite participation (Theorem N1), discrete micro-events, gradient saturation — jointly forbid divergent curvature; the singularity is replaced by a finite-thickness saturated participation zone. **Information cannot cross the horizon** as a participation-bandwidth prohibition (not a causal one); entanglement amplitude can straddle the surface; **evaporation is participation re-routing** through pair-creation-class events, not information destruction. The four assumptions that generate the standard information paradox are not imposed at the substrate level, so no paradox arises. **Area-law entropy** $S = (A/\ell_P^2)\log g$ is FORCED in form by two-dimensional decoupling-surface support + gradient saturation; the Bekenstein-Hawking $1/4$ coefficient is INHERITED from substrate motif counting and is not closed-form derived at present. **Wave-black-hole scattering** produces a global phase shift $\delta_{\ell m} = \int_\mathrm{path}\Delta\mathcal{A}\,d\lambda$ as a substrate-derived invariant of minimal ED-channels, with helicity preservation/flip from anisotropy-basis transport and Kerr twist from integrated frame-dragging vorticity. The verdict is **conditional-positive structural closure** at the architectural level, parallel to the program's NS-Smoothness Intermediate Path C, Yang-Mills Clay-relevance, and Arc ED-10 verdicts. Form FORCED / value INHERITED / extensions OPEN — the standard methodology of the ED program — applied honestly to the black-hole sector.

---

## 1. Introduction

### 1.1 Motivation

Black-hole physics in standard treatments combines general-relativistic geometry (event horizons, singularities, Killing structure) with quantum-field-theoretic content (Hawking radiation, Bekenstein-Hawking entropy, information loss). The combination generates a well-known cluster of paradoxes: the information-loss paradox (apparent unitarity violation in evaporation), the firewall puzzle (monogamy-of-entanglement at the horizon), the complementarity contradiction (interior-vs-exterior descriptions), and the singularity problem (geodesic incompleteness + diverging curvature invariants). These puzzles have driven decades of work on holography, ER=EPR, soft-hair conjectures, fuzzballs, and other proposals — none of which has produced a consensus resolution.

The Event Density (ED) program approaches the black-hole sector from a different ontological starting point. ED's substrate primitives — local participation density $\rho$, participation gradients $\nabla\rho$, anisotropy structure, V1 finite-width kernel, P11 commitment irreversibility — generate spacetime geometry only as a coarse-grained kinematic reading via the acoustic metric (Arc ED-10), not as a fundamental object. The substrate ontology does not impose global unitarity, global Cauchy data, sharp geometric boundaries, or monogamy-at-boundaries as primitive features. The standard paradoxes are therefore **not generated in framework**; they arise only when continuum-level assumptions are imposed on a fundamentally local-and-irreversible substrate.

### 1.2 ED Ontology in Brief

ED treats the world as a substrate of participation events. Local participation density $\rho(\mathbf{x})$ is the density of viable participation-channel slots per coarse-graining cell. Participation events commit irreversibly (Primitive P11): once a substrate channel commits, the commitment is preserved as part of the local history. Cross-participation bandwidth $\Gamma_\mathrm{cross}$ between adjacent regions controls whether committed structure on one side can register as committed structure on the other. The hydrodynamic window $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$ separates substrate scales from continuum dynamics; the Diffusion Coarse-Graining Theorem (DCGT, Arc D, 2026-04-30) is the substrate-to-continuum bridge.

### 1.3 Why ED Does Not Generate the Standard Paradoxes

- **No global unitarity requirement.** Unitarity is a coarse-grained continuum property of closed sub-systems in the QM-emergence sector (Phase-1, T1–T16); it is not a global constraint at the substrate level.
- **No global Cauchy data.** ED commits events locally; there is no spacelike surface on which the entire universe's state must be specified.
- **No sharp geometric boundary.** A horizon in ED is a coarse-grained statistical feature of $\Gamma_\mathrm{cross}$, not a knife-edge geometric locus.
- **No monogamy-at-boundary requirement.** Without a sharp boundary, monogamy-of-entanglement enforcement at one is not a structural requirement.

Removing these four assumptions removes the four standard paradoxes. **The information paradox, firewall paradox, complementarity contradiction, and singularity problem are not solved in ED — they simply never arise in its ontology.** What remains is the constructive question: what does ED's substrate machinery actually deliver for black-hole architecture?

### 1.4 Arc BH as a Consolidation + Derivation Arc

Arc BH (2026-05-01) is a seven-memo arc that consolidates the interpretive content of ED-06 (information and horizons), ED-10 (curvature emergence), ED-I-06 (fields and forces), and ED-I-26 (wave-BH scattering channels) into a single substrate-derivation chain grounded in DCGT + Arc SG (substrate gravity) + Arc ED-10 (acoustic-metric scalar-tensor covariantization). The seven memos: BH-1 opening; BH-2 horizon-as-decoupling-surface; BH-3 singularity replacement + strong-curvature audit; BH-4 information vs entanglement + evaporation; BH-5 area-law entropy + 1/4 coefficient; BH-6 wave-BH scattering; BH-7 synthesis.

### 1.5 Summary of Results

A single substrate condition unifies the architecture:
$$
|\nabla\rho|\ell_P^2/\rho_\mathrm{local} \gtrsim \log(R_\mathrm{cg}/\ell_P).
$$
This condition governs horizon formation (BH-2), interior saturation (BH-3), information blocking (BH-4), participation-capacity saturation (BH-5), and the strong-curvature scattering region (BH-6). One condition supports six derivations. The architecture is internally consistent. The verdict is conditional-positive structural closure: form derived from substrate machinery; value-layer (entropy coefficient, BHPT spectral details, $\beta_\mathrm{crit}$, $\log g$) inherited; explicit open extensions (Hawking spectrum, superradiance amplitude, closed-form $\log g$, full Kerr interior) named.

---

## 2. Substrate Primitives and DCGT Machinery

### 2.1 Participation Density and Its Gradients

The substrate's load-bearing scalar field is the local participation density $\rho(\mathbf{x})$, defined as the density of viable participation-channel slots per coarse-graining cell of size $R_\mathrm{cg}$. Its gradient $\nabla\rho$ encodes the spatial variation of the substrate's participation-channel availability. The dimensionless ratio
$$
\sigma(\mathbf{x}) \equiv |\nabla\rho|\ell_P^2/\rho_\mathrm{local}
$$
measures the relative steepness of $\rho$ at the substrate Planck scale $\ell_P$. This is the load-bearing quantity for Arc BH: $\sigma$ controls horizon formation, interior saturation, and the strong-curvature scattering region.

### 2.2 Anisotropy and Polarization Structure

Substrate channels carry directional content: the local anisotropy tensor encodes the relative weight of participation along different axes. For minimal ED-channels (gravitational waves, BH-6), the anisotropy tensor is small and traces out a polarization frame whose transport along propagation trajectories carries the channel's helicity content.

### 2.3 V1 Finite-Width Kernel

The V1 vacuum kernel, established in Theorem N1 (2026 foundational theorem), is the finite-width temporal smearing kernel that mediates substrate participation events. Its width sets the temporal resolution of commitment events at a patch and is load-bearing for: (i) the kernel-arrow result (Theorem 18), (ii) the per-patch motif alphabet $g$ in BH-5, (iii) the cross-patch correlation structure that links adjacent decoupling-surface patches.

### 2.4 Multi-Scale Expansion and the Hydrodynamic Window

DCGT (Arc D, 2026-04-30) establishes a hydrodynamic-window scale separation
$$
\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}
$$
under which substrate dynamics admit a multi-scale expansion to coarse-grained continuum equations. In Arc BH, DCGT supplies: the cross-bandwidth $\Gamma_\mathrm{cross}$ structure, the per-patch independence assumption used in BH-5 (with corrections from V1 cross-patch correlations), and the channel-propagation kernels used in BH-6.

### 2.5 The Critical Gradient Condition

The substrate condition
$$
\sigma = |\nabla\rho|\ell_P^2/\rho_\mathrm{local} \gtrsim \log(R_\mathrm{cg}/\ell_P)
$$
is the single load-bearing inequality of Arc BH. Below the threshold, cross-bandwidth between adjacent regions remains finite and substrate dynamics admit ordinary hydrodynamic-window coarse-graining. At and above the threshold, $\Gamma_\mathrm{cross}$ falls below hydrodynamic-window resolution and the region exhibits decoupling-surface behavior (Section 3) or gradient-saturation behavior (Section 4) depending on whether the steep-gradient region is a surface or a bulk volume.

The threshold value $\log(R_\mathrm{cg}/\ell_P)$ is itself substrate-determined (depends on the choice of coarse-graining scale relative to Planck length); the precise prefactor enters as INHERITED data labelled $\beta_\mathrm{crit}$ in subsequent sections.

---

## 3. Horizons as Decoupling Surfaces (BH-2)

### 3.1 Bandwidth Collapse Mechanism

Cross-participation bandwidth between adjacent substrate regions takes the form (DCGT-derived)
$$
\Gamma_\mathrm{cross}(\mathbf{x}) \sim \exp\!\left[-\alpha\,\sigma(\mathbf{x})\right]
$$
with $\alpha$ a substrate-determined dimensionless prefactor. The exponential suppression is a generic consequence of the multi-scale expansion: large $|\nabla\rho|$ at the substrate scale creates steep barriers to participation-channel mediation between adjacent regions.

### 3.2 Decoupling Surface Definition

The decoupling surface is the locus
$$
\Sigma_H \equiv \{\mathbf{x}: \sigma(\mathbf{x}) \gtrsim \log(R_\mathrm{cg}/\ell_P)\},
$$
beyond which $\Gamma_\mathrm{cross}$ has dropped below hydrodynamic-window resolution. From a coarse-grained continuum perspective, the substrate channels carrying committed structure across $\Sigma_H$ have effectively zero bandwidth.

### 3.3 Universalization

The same mechanism applies to:

- **Black-hole event horizons:** steep $|\nabla\rho|$ from the SG-4 / Arc SG participation profile near a high-mass concentration.
- **Rindler horizons:** acceleration-induced steep $|\nabla\rho|$ in the accelerated frame.
- **Cosmological horizons:** $H_0$-scale gradient set by cosmic-horizon participation density.
- **Acoustic horizons (analog gravity):** flow-induced gradient in fluid analog systems.

In each case the horizon is a continuum shadow of the same substrate decoupling surface. This explains, at the substrate level, why these four classes share thermodynamic-style features (temperature, entropy, evaporation analogs) despite differing in their continuum-geometry origins.

### 3.4 Geometric Horizon as Continuum Shadow

The geometric horizon — defined in the acoustic-metric reading of Arc ED-10 as the locus of null-geodesic capture — is the coarse-grained continuum signature of $\Sigma_H$. The two coincide to leading order in the hydrodynamic expansion; corrections arise at the substrate scale.

### 3.5 Observer-Independence

$\Sigma_H$ is defined as a level set of the substrate scalar $\sigma$, which is built from $\rho$ and $\nabla\rho$. Both are coarse-grained substrate quantities; they do not depend on a choice of continuum-observer. The decoupling surface is therefore observer-independent in the same sense that $\rho$ is. (Continuum-observer-dependent statements about which side of $\Sigma_H$ a particular continuum trajectory is on do depend on the observer, as expected — but the surface itself does not.)

---

## 4. No Singularities: Interior Saturation (BH-3)

### 4.1 Three Substrate Constraints

Three independent substrate constraints jointly forbid divergent curvature/energy/tidal/incompleteness at the substrate level:

**(C1) Finite participation (P4 + Theorem N1).** The substrate has finite participation-channel density per coarse-graining cell. There is no substrate state in which infinitely many channels participate at a single point.

**(C2) Discrete micro-events (P01).** Substrate events are discrete: each commitment is a finite-amplitude occurrence at a finite-resolution patch. Continuum singularity statements that require unbounded micro-event multiplicity are inadmissible.

**(C3) Gradient saturation (P4 mobility-capacity bound).** $|\nabla\rho|$ has a substrate-imposed maximum: when $\sigma \to \beta_\mathrm{crit}$, the substrate's mobility-capacity bound caps further steepening. Gradients cannot run away to infinity.

Any one of (C1)–(C3) alone would suffice to forbid a continuum singularity; the three together overdetermine the result.

### 4.2 Acoustic Metric Breakdown

The acoustic-metric scalar-tensor reading of Arc ED-10 is a coarse-grained kinematic structure: $g_{\mu\nu}^\mathrm{ac}[\rho,\nabla\rho]$. Its validity requires the hydrodynamic-window expansion of DCGT to be controlled. When $\sigma \gtrsim \beta_\mathrm{crit}$, the multi-scale expansion's small parameter ceases to be small; the acoustic metric ceases to be a controlled approximation. **The acoustic metric breaks down before the substrate does.**

This is the substrate-level meaning of "singularity": the breakdown is a property of the kinematic continuum reading, not of the underlying substrate. Substrate dynamics remain finite throughout.

### 4.3 Replacement: Finite-Thickness Saturated Zone

The substrate replacement for the singular endpoint is a finite-thickness saturated participation zone characterized by:

- Gradients at the substrate-imposed maximum: $\sigma \to \beta_\mathrm{crit}$.
- Cross-participation bandwidth collapsed in all directions (not just the radial-equivalent of $\Sigma_H$).
- Only the commitment-order direction (P11) remaining structurally meaningful.
- Acoustic metric degenerate or undefined.
- Substrate dynamics finite, consisting of saturated commitment cycles.

### 4.4 No Geodesic Incompleteness at Substrate Level

Geodesic incompleteness is a property of the acoustic-metric reading. At the substrate level there are no geodesics — there are only commitment-event sequences. Commitment-event sequences inside the saturated zone proceed in finite-amplitude finite-resolution increments; there is no sequence that "ends" at a singular point. Substrate-level evolution is everywhere defined.

---

## 5. Information Architecture and Evaporation (BH-4)

### 5.1 Committed vs Uncommitted Structure

ED distinguishes two structurally different forms of correlation:

- **Committed structure (information):** P11-irreversible records of participation events. Transmission of committed structure between two regions requires nonzero $\Gamma_\mathrm{cross}$ between them.
- **Uncommitted structure (entanglement):** correlation potential between two regions, set up at pair-formation. Persistence of uncommitted structure does not require ongoing cross-bandwidth.

This is the substrate translation of the standard quantum-information no-signaling-but-correlations-persist behavior.

### 5.2 Why Information Cannot Cross a Horizon

At $\Sigma_H$, $\Gamma_\mathrm{cross}$ is below hydrodynamic-window resolution (Section 3). Therefore:
- Committed structure transmission across $\Sigma_H$ requires bandwidth that is structurally absent.
- Information, in the substrate sense, does not pass through a horizon.

This is **not a causal prohibition** (ED has no fundamental light-cone primitive); it is a **participation-bandwidth prohibition**.

### 5.3 Entanglement Straddling

Uncommitted structure does not require ongoing $\Gamma_\mathrm{cross}$; it is set by joint participation amplitude at pair-formation. Pair-amplitude structures can therefore exist with one leg inside and one leg outside $\Sigma_H$ without violating Section 5.2.

### 5.4 Evaporation as Participation Re-Routing

The evaporation mechanism follows from the architecture above:

1. Horizon blocks committed structure.
2. Uncommitted pair structures can straddle $\Sigma_H$.
3. Strong $|\nabla\rho|$ near $\Sigma_H$ supports pair-creation-class events (gradient-driven, substrate analog of strong-field vacuum pair production).
4. Commitment events on these pairs commit one leg inward (joining the BH-3 saturated zone) and the other outward (joining the radiation field).
5. Joint correlation is preserved globally across the inward + outward commitments.

This is **participation re-routing**, not information destruction. What an external observer reads as thermal Hawking radiation is the coarse-grained statistics of outward-committed legs of these pairs. (The thermal spectrum derivation itself is reserved for the next arc — priority item B4 — and is explicitly out of scope for the present paper.)

### 5.5 No Information Paradox

The four assumptions that generate the standard information paradox are:
(a) global unitarity, (b) global Cauchy data, (c) sharp geometric boundary, (d) monogamy-at-boundary.

None of these is imposed at the substrate level. The paradox does not arise. The same applies to firewalls and complementarity: both require a sharp geometric boundary, which the ED ontology does not provide.

The ED stance is structural: BH puzzles are **not solved in framework** but **not generated in framework**. The same pattern applies to the singularity (BH-3) and to the horizon (BH-2): standard puzzles dissolve when the continuum-level assumptions that generate them are not imposed.

---

## 6. Area-Law Entropy and the 1/4 Coefficient (BH-5)

### 6.1 Participation Capacity

Define the participation-capacity density $\chi(\rho,\nabla\rho)$ as the substrate-level density of viable commitment-channel slots per Planck-area patch on $\Sigma_H$. Total participation capacity:
$$
\mathcal{C}_H = \int_{\Sigma_H} \frac{dA}{\ell_P^2}\,\chi(\rho,\nabla\rho).
$$
Two structural points: (i) area-extensivity (the integrand is supported only on $\Sigma_H$, not on a bulk volume); (ii) saturation in the BH-relevant regime ($\chi \to 1$ where gradient saturation holds, per BH-3).

### 6.2 Area-Law Form

In the BH-relevant regime,
$$
\mathcal{C}_H \approx A/\ell_P^2,
$$
with $A$ the coarse-grained acoustic-metric area of $\Sigma_H$. The area-law form is **derived** from substrate machinery: two-dimensional surface support + gradient saturation.

### 6.3 Entropy as Log of Viable Commitment Histories

ED's substrate definition: $S = \log(\text{number of viable commitment histories compatible with the macroscopic constraint})$. With per-patch finite alphabet $g$ (the substrate's local count of distinct commitment motifs per Planck-area patch) and per-patch independence under DCGT:
$$
S = \mathcal{C}_H \log g \approx \frac{A}{\ell_P^2}\log g.
$$

### 6.4 The 1/4 Coefficient: Inherited

The Bekenstein-Hawking value $S_\mathrm{BH} = A/(4\ell_P^2)$ corresponds to $\log g = 1/4$, i.e. $g = e^{1/4} \approx 1.284$. This is **not an integer**. Naive per-patch-independent finite-alphabet counting cannot reproduce $1/4$: integer $g \geq 2$ all give $\log g \geq \ln 2 \approx 0.693$.

To recover $1/4$, the per-patch-independence assumption must be relaxed: adjacent patches share commitment-history correlations through V1-kernel cross-patch overlap. The effective per-patch contribution is reduced from $\log g$ (independent count) to a smaller correlated value. Recovering $1/4$ exactly requires substrate-level state counting that is not currently in hand — structurally similar in difficulty to closed-form derivation of $\kappa/|\hat{N}'| = 0.001766$ (priority item E4).

**Verdict on the 1/4 coefficient: INHERITED, not derived.** Form-FORCED + value-INHERITED methodology applied honestly. Same category as $a_0$, $G$, $\Lambda$, gauge couplings, and the other substrate-determined dimensionless numbers in the ED program.

### 6.5 Implications for Motif Counting and V1 Correlations

The closed-form $\log g$ derivation would require either: (a) an explicit V1-kernel-counting argument analogous to a substrate-level partition function; or (b) a derivation of the per-patch commitment alphabet from microscopic substrate dynamics. Either route is a candidate future arc. Currently flagged as **OPEN item O2**.

---

## 7. Wave-Black-Hole Scattering (BH-6)

### 7.1 Minimal ED-Channel

A minimal ED-channel (gravitational wave, in the continuum reading) is a substrate excitation characterized by:
- Low multiplicity (small number of participation degrees of freedom involved per coarse-graining cell).
- Low anisotropy (anisotropy tensor magnitude small compared to substrate-saturation).
- DCGT-coherent propagation (channel survives multi-scale expansion to a wave equation on the acoustic metric).

Channel global phase along propagation trajectory $\gamma(\lambda)$:
$$
\Phi[\gamma] = \int_\gamma \mathcal{A}(\rho,\nabla\rho,\text{anisotropy})\,d\lambda.
$$

### 7.2 Maximal ED-Structure

A maximal ED-structure (black hole) is high-multiplicity, saturated-gradient, decoupling-surface-bounded, with curvature-like participation structure given by SG-4 / Arc SG. In the BH-relevant regime, scattered channels propagate through a region where $\sigma \gg 1$ near $\Sigma_H$ and the acoustic metric is strongly curved.

### 7.3 Phase Shift as Global Invariant

The minimal channel's propagation kernel is distorted by the maximal structure's saturated gradients. The channel's phase accumulates a shift relative to its asymptotic free-wave value:
$$
\delta_{\ell m} = \int_\mathrm{path}\Delta\mathcal{A}\,d\lambda
$$
with $\Delta\mathcal{A} = \mathcal{A}_\mathrm{full} - \mathcal{A}_\mathrm{asymptotic}$ the curvature-induced excess action density along the trajectory. The shift is a single scalar per partial-wave mode $(\ell,m)$ because the channel is minimal; it is inevitable along any trajectory threading the strong-curvature region because the gradients are saturated.

### 7.4 S-Matrix Exponentiation

The S-matrix structure $S = e^{iN}$ from ED-I-26 is recovered: $N$ is the integrated channel action; $\delta_{\ell m}$ are its partial-wave components. Exterior-side unitarity follows from BH-4 (no committed structure leaks across $\Sigma_H$, so no probability is lost from the scattering channel; entanglement-amplitude correlations with the interior persist but do not enter exterior unitarity bookkeeping).

### 7.5 Helicity Preservation and Flip

For axisymmetric, non-rotating backgrounds (Schwarzschild-like): principal directions of the participation profile are aligned uniformly along the trajectory's symmetry plane. The channel's anisotropy tensor returns to itself up to an overall scalar phase under parallel transport. **Helicity is preserved**; phase shifts act identically on both helicity states.

For backgrounds with frame-dragging (Kerr-like): principal directions rotate along the trajectory. The channel's anisotropy tensor picks up a twist relative to a non-rotating reference frame:
$$
\Delta\phi_\mathrm{twist} = \int \omega_\mathrm{FD}\,d\lambda.
$$
**Helicity flip channels open**, with mixing strength tied to spin parameter via $\omega_\mathrm{FD}$.

### 7.6 Kerr Twist and Superradiance

The Kerr phase shift relative to Schwarzschild has a substrate origin: frame-dragging is a global rotation of the participation anisotropy basis, sourced by substrate-level vorticity in the participation flow of a spinning maximal structure. The channel acquires a twist proportional to integrated background vorticity along its trajectory. Trajectory-dependence of the integration produces the prograde/retrograde scattering asymmetry.

**Superradiance** (energy extraction by certain scattering channels) is structurally compatible with this picture: channels traversing the rotating-vorticity exterior can net positive energy transfer from background to channel via the participation-flow vorticity. No committed structure is extracted from the interior; the energy transfer is mediated by exterior participation flow. Full amplitude derivation is **OPEN item O1**.

---

## 8. Unified Black-Hole Architecture

The six derivations integrate into a single architectural picture supported by the single substrate condition $\sigma \gtrsim \log(R_\mathrm{cg}/\ell_P)$:

- **Formation.** Steep participation-density gradients drive $\sigma$ across threshold; cross-bandwidth collapses; decoupling surface $\Sigma_H$ emerges (Section 3 / BH-2).
- **Interior.** Gradients continue steepening but saturate at the substrate-imposed maximum (C3); finite-thickness saturated zone replaces the singular endpoint (Section 4 / BH-3).
- **Information flow.** Committed structure cannot cross $\Sigma_H$ (bandwidth-blocked); entanglement amplitude can straddle (Section 5 / BH-4).
- **Thermal behavior.** Asymmetric participation flow at the saturated decoupling surface produces, at the coarse-grained continuum level, the statistical features standardly read as thermal (mechanism: Section 5; spectrum derivation: deferred to B4).
- **Entropy.** Area-law form from participation capacity of $\Sigma_H$ (Section 6 / BH-5); coefficient INHERITED.
- **Scattering.** Minimal ED-channel acquires global phase shift through saturated-gradient exterior; helicity behavior + Kerr twist follow from anisotropy-basis transport (Section 7 / BH-6).
- **Evaporation.** Pair-creation-class events at $\Sigma_H$ route participation outward + inward; correlation structure preserved globally (Section 5 / BH-4).

The architecture is internally consistent: one substrate-level condition governs all six. **No singularity. No information paradox. No global unitarity requirement. No firewall. No complementarity contradiction. No geometric-boundary primitive.**

---

## 9. FORCED / INHERITED / OPEN Classification

### FORCED (substrate-level form)

- Horizon as decoupling surface (BH-2).
- No singularities (BH-3).
- Information blocking + entanglement straddling (BH-4).
- Evaporation as participation re-routing (BH-4).
- Area-law form (BH-5).
- BHPT phase shift structure (BH-6).
- Helicity behavior under axisymmetric vs frame-dragging backgrounds (BH-6).
- Kerr twist as integrated background vorticity (BH-6).

### INHERITED (value-level)

- 1/4 entropy coefficient (BH-5): corresponds to $\log g$ from substrate motif counting; closed-form value not currently extracted.
- BHPT spectral details (BH-6): match to specific $\delta_{\ell m}$ values conditional on Arc ED-10 + Arc SG acoustic-metric prerequisites.
- $\beta_\mathrm{crit}$ (BH-2 / BH-3): substrate-determined dimensionless threshold; precise value depends on coarse-graining choices.
- V1 kernel width + per-patch motif alphabet $g$ (BH-5): substrate constants whose closed-form values are not currently extracted.

### OPEN (future arcs)

- **B4 — Hawking spectrum derivation** (next natural arc). Mechanism in hand from BH-4; load-bearing work is the explicit V5 cross-chain correlation calculation that produces the spectrum. Match to $T_H = \kappa/(2\pi)$ would be structural recovery; deviation a falsifier.
- **O1 — Superradiance amplitude derivation.** Structurally compatible per BH-6; full derivation requires extending BH-6 + Arc SG.
- **O2 — Closed-form $\log g$ from V1 kernel + motif counting.** Substrate-level state-counting derivation, structurally similar in difficulty to E4.
- **O3 — Full Kerr interior audit.** Extension of BH-3 to rotating-BH interior architecture (ergosphere, Cauchy horizons, frame-dragging at saturation).

---

## 10. Discussion and Outlook

### 10.1 Implications for Quantum Gravity

The standard quantum-gravity program seeks to reconcile general-relativistic geometry with quantum-field-theoretic content within a single dynamical framework, treating the metric as a fundamental (or holographically dual) degree of freedom. ED takes a different starting point: the metric is a coarse-grained kinematic reading; the substrate is local participation events with irreversible commitment. From this starting point, the standard black-hole puzzles are not generated. Whether this dissolution is satisfying or merely re-locates the difficulty is a judgement call. The honest claim is that ED delivers a substrate-level architecture for the black-hole sector that is internally consistent, derives form from substrate machinery, and inherits value-layer details from substrate constants — the same form-FORCED + value-INHERITED pattern that holds across the rest of the program.

### 10.2 Relation to GR, QFT, and Analog Gravity

- **GR.** ED does not derive the Einstein equation. The acoustic-metric reading is kinematic, not full GR. Black-hole architecture in ED is **not** a derivation of GR black-hole solutions; it is a substrate-level account of how black-hole-like structure emerges from substrate participation dynamics, with continuum-geometry features matching GR-class predictions to leading order via the acoustic-metric scalar-tensor approximation (Arc ED-10).
- **QFT.** ED supplies QM emergence (Phase-1, T1–T16) and form-level QFT content (T17, T18) within the canonical-ED hydrodynamic window. Hawking-radiation derivation (priority B4) is the natural site to test how far the form-level QFT machinery extends into the strong-curvature regime.
- **Analog gravity.** The universalization of the decoupling-surface mechanism across BH / Rindler / cosmological / acoustic horizons (Section 3) is a substrate-level explanation for the empirical similarity of analog-gravity systems to gravitational ones. Acoustic horizons are not "weakly gravity-like"; they are decoupling surfaces of the same substrate type.

### 10.3 Why ED Avoids Paradoxes Rather Than Solving Them

**The information paradox, firewall paradox, complementarity contradiction, and singularity problem are not solved in ED — they simply never arise in its ontology.** The standard paradox-cluster (information loss, firewalls, complementarity) requires four assumptions: global unitarity, global Cauchy data, sharp geometric boundary, monogamy-at-boundary. None is imposed at the substrate level. The dissolution is structural, not constructive: ED does not propose a clever resolution within a paradox-generating framework; it identifies the assumptions whose joint imposition generates the paradox and shows that the substrate ontology does not impose them. The same pattern appears in BH-3 (singularity) and BH-2 (horizon). It is a recurring feature of the ED program: standard puzzles dissolve when continuum-level assumptions are not imposed on a fundamentally local-and-irreversible substrate.

### 10.4 Next Arc: Hawking Spectrum (B4)

The next natural arc is Hawking-spectrum derivation. The mechanism is in hand from BH-4 (asymmetric participation flow at saturated decoupling surface produces outward-radiation statistics). The load-bearing technical work is the explicit V5 cross-chain correlation calculation that produces the spectrum. A match to $T_H = \kappa/(2\pi)$ would be a structural recovery; a deviation would be a falsifier of the architecture. Estimated 6–8 memos. Couples naturally with O1 (superradiance) since both involve substrate-level cross-chain correlations at the decoupling surface.

### 10.5 Long-Term Program Trajectory

Arc BH closure brings the structurally-complete column to: QM emergence (Phase-1) + form-level QFT (T17, T18) + substrate gravity (Arc SG / T19 / T20 / ECR / T21) + curvature emergence (Arc ED-10) + fluid dynamics (NS / MHD) + non-Abelian gauge theory (Yang-Mills) + soft-matter mobility (UDM / P4-NN) + black-hole architecture (Arc BH). Eight sectors with form-derived content. The remaining major open structural fronts are: GR-4A (Einstein equation emergence, SPECULATIVE), Arc COSMO (cosmic expansion / $H_0$ derivation, SPECULATIVE), and B4 (Hawking spectrum, the next concrete arc). The program-level methodology — form-FORCED + value-INHERITED + explicit OPEN items — is consistent across every closed arc.

---

## 11. Appendices

### Appendix A — DCGT Derivation Details

DCGT (Diffusion Coarse-Graining Theorem, Arc D, 2026-04-30) supplies the substrate-to-continuum bridge for canonical-ED dynamical content. The hydrodynamic-window scale separation $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$ admits a multi-scale expansion. At leading order, scalar diffusion + directional viscosity + V1→R1 + V5→Maxwell memory + T17 minimal-coupling Lorentz are all derived from substrate primitives.

For Arc BH, DCGT supplies: (i) the cross-bandwidth structure $\Gamma_\mathrm{cross} \sim \exp[-\alpha\sigma]$ used in Section 3; (ii) the per-patch independence assumption used in Section 6 (with V1 cross-patch correction terms responsible for reducing naive integer-$g$ counts to the inherited $\log g \approx 1/4$); (iii) the channel-propagation kernels used in Section 7. The full derivation is in Arc D's six memos at `theory/Arc_D/`.

### Appendix B — Participation Capacity and Motif Counting

The participation-capacity density $\chi(\rho,\nabla\rho)$ measures viable commitment-channel slots per Planck-area patch. By construction $\chi \in [0,1]$, with $\chi \to 1$ in the gradient-saturated regime. The total participation capacity is the surface integral $\mathcal{C}_H = \int_{\Sigma_H}(dA/\ell_P^2)\chi$.

The per-patch motif alphabet $g$ counts distinct viable commitment motifs per Planck-area patch on a saturated decoupling surface. Constraints on $g$:

- P11 (each commitment slot is a one-way switch): bounds motif count by the count of distinguishable commitment-switch sequences.
- V1 finite kernel width: bounds the count of distinguishable temporal orderings within a patch.
- Gradient saturation (BH-3): suppresses motif bleeding between adjacent patches, justifying per-patch independence to leading order.
- DCGT hydrodynamic-window resolution: distinguishability requires motifs to survive coarse-graining over $R_\mathrm{cg}$.

These constraints determine $g$ as a finite substrate-determined integer ≥ 2. Closed-form extraction is OPEN item O2.

### Appendix C — Scattering Integrals and Anisotropy Transport

The phase-shift integral $\delta_{\ell m} = \int_\mathrm{path}\Delta\mathcal{A}\,d\lambda$ has the structure of a path-integrated curvature-coupling correction. The integrand $\Delta\mathcal{A} = \mathcal{A}_\mathrm{full} - \mathcal{A}_\mathrm{asymptotic}$ is built from the channel's substrate action density evaluated against the full SG-4 / Arc SG participation profile minus its asymptotic flat-space limit.

Anisotropy-basis transport along the trajectory is governed by parallel transport of the channel's polarization tensor through the local participation-frame. For axisymmetric backgrounds, parallel transport closes (helicity preserved). For frame-dragging backgrounds, parallel transport accumulates a twist $\Delta\phi_\mathrm{twist} = \int\omega_\mathrm{FD}\,d\lambda$ proportional to integrated substrate vorticity.

### Appendix D — Comparison with GR / QFT BH Structures

| Feature | GR/QFT | ED (this paper) |
|---|---|---|
| Horizon | Null hypersurface in metric | Decoupling surface in $\sigma$ |
| Singularity | Geodesic incompleteness + diverging curvature | Acoustic-metric breakdown; substrate finite |
| Information | Crosses horizon classically; paradox quantum | Cannot cross (bandwidth); paradox not generated |
| Entanglement | Monogamy-at-boundary forces firewall | Straddles surface; no firewall |
| Entropy | $A/(4\ell_P^2)$ derived (e.g. holography) | Form $A/\ell_P^2 \cdot \log g$ derived; coefficient inherited |
| Hawking $T$ | $\kappa/(2\pi)$ from QFT in curved background | Mechanism from re-routing; spectrum derivation OPEN (B4) |
| Helicity preservation | Schwarzschild diagonal | Anisotropy-basis aligned |
| Kerr twist | Frame-dragging in metric | Integrated substrate vorticity |
| Superradiance | Penrose process / wave amplification | Structurally compatible; OPEN (O1) |
| Universal across horizon types | Analog gravity heuristically related | Universal at substrate level (Section 3.3) |

---

## 12. Metadata

**Keywords.** Event Density; Black Holes; Substrate Physics; Decoupling Surface; DCGT; Acoustic Metric; Information Paradox; Bekenstein-Hawking Entropy; BHPT; Kerr Scattering; Form-FORCED / Value-INHERITED Methodology.

**Version.** 1.0 — May 2026.

**Arc BH References.** Seven memos in `theory/Black_Holes/`: Arc_BH_1_Opening; Arc_BH_2_Horizon_DCGT; Arc_BH_3_Singularity_And_Strong_Curvature_Audit; Arc_BH_4_Information_And_Evaporation; Arc_BH_5_Area_Law_Entropy; Arc_BH_6_Wave_BH_Scattering; Arc_BH_7_Synthesis.

**Related ED Papers.** *Foundations of Substrate Gravity* (April 2026, two complementary papers); *Event Density Foundations of Quantum Field Theory: A Unified Substrate-to-Continuum Overview* (April 2026); *Navier-Stokes Synthesis Paper* (April 2026, with Appendices C/D/E covering MHD + DCGT + Yang-Mills); *Event Density: One Substrate, Three Domains* (April 2026); *Theorem 17: Gauge-Field-as-Rule-Type*; *Theorem 18: V1 Kernel Retardation*.

**Citation Block (Zenodo-safe).**

> Proxmire, A. (2026). *Black Holes in Event Density: A Substrate-Level Architecture.* Event Density Program, Black Hole Foundations Paper, May 2026.

**Conditional-Positive Verdict Disclaimer.** This paper presents a substrate-level architectural account of black-hole physics. Form-derivations are FORCED from substrate machinery; value-layer details (entropy coefficient, BHPT spectral values, $\beta_\mathrm{crit}$, $\log g$) are INHERITED and not closed-form derived at present. No claim of GR derivation is made; the acoustic-metric reading is kinematic per ED-Phys-10 guardrails. Open extensions (Hawking spectrum derivation, superradiance amplitude, closed-form $\log g$, full Kerr interior audit) are explicitly named.
