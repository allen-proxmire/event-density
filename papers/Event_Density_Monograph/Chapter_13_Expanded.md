# Chapter 13 — Black-Hole Architecture: Arc BH, Horizons, Area Law, Phase-Shift Structure

## 13.1 Chapter Overview

Black-hole physics in standard treatments combines general-relativistic geometry (event horizons, singularities, Killing structure) with quantum-field-theoretic content (Hawking radiation, Bekenstein–Hawking entropy, information loss). The combination generates a well-known cluster of paradoxes: the information-loss paradox, the firewall paradox, the complementarity contradiction, and the singularity problem. Forty years of work on holography, ER=EPR, soft-hair conjectures, fuzzballs, and other proposals has produced no consensus resolution. The Event Density framework approaches the black-hole sector from a different ontological starting point: substrate participation events with irreversible commitment, with spacetime geometry as a coarse-grained kinematic reading via the acoustic metric (Chapter 12) rather than as a fundamental object. Under the substrate ontology, the standard paradoxes are *not generated in framework* — the four assumptions whose joint imposition produces them are not imposed at substrate level.

This chapter establishes the substrate-level architecture of black-hole physics. **A single substrate condition** unifies six derivations:

```math
\sigma(\mathbf{x}) \;=\; \frac{|\nabla\rho|\,\ell_P^2}{\rho_\mathrm{local}} \;\gtrsim\; \log\!\left(\frac{R_\mathrm{cg}}{\ell_P}\right).
```

Six structural results follow from this single condition: **horizon as decoupling surface** (BH-2, universal across black-hole / Rindler / cosmic / acoustic horizons), **singularity replacement by finite-thickness saturated participation zone** (BH-3, three substrate constraints jointly forbid divergent curvature), **information architecture and evaporation as participation re-routing** (BH-4, paradoxes not generated rather than solved), **area-law entropy with form derived and 1/4 coefficient INHERITED** (BH-5), **wave-black-hole scattering as global path-integrated invariant of minimal ED-channels** (BH-6), and a **conditional-positive structural closure verdict** (BH-7) parallel in form to Clay-NS Intermediate Path C (Chapter 8), Yang–Mills Clay-relevance (Chapter 9), and Arc ED-10 curvature emergence (Chapter 12). Hawking-spectrum derivation is named as the next natural arc (B4); the mechanism is in hand from BH-4, with the explicit V5 cross-chain correlation calculation producing the spectrum as the remaining work.

The chapter does not change empirical predictions for black-hole observations. Engineering and astronomical computations using standard general-relativistic black-hole solutions proceed unchanged. What changes is the structural origin of black-hole architecture: from a combined GR+QFT framework that generates paradoxes to a substrate-level framework in which the same paradoxes do not arise because their generating assumptions are not imposed.

## 13.2 The Standard Paradox Cluster

### 13.2.1 The four canonical paradoxes

Standard black-hole physics has four canonical paradoxes that arise from combining general-relativistic geometry with quantum-field-theoretic content:

- **The information-loss paradox.** Stephen Hawking's 1974 result that black holes radiate thermally implies that information apparently disappears as the black hole evaporates: the radiation that emerges is featureless, regardless of what fell in. Standard quantum mechanics requires information preservation under unitary evolution; combining GR's classical evaporation with QM's information conservation produces the paradox.
- **The firewall paradox.** Pushing hard on the demand that information escape evaporating black holes plus the standard rules of quantum entanglement plus the standard demand that an infalling observer experiences nothing strange at the horizon produces a contradiction (AMPS 2012). Saving quantum mechanics appears to require the horizon to be a wall of high-energy radiation that vaporizes anything entering it — the firewall.
- **The complementarity contradiction.** The proposal that outside the horizon information returns in radiation and inside the horizon information falls toward the center, with both descriptions valid because no single observer can verify both at once. The proposal works as a partial fix until sharp questions are asked, at which point complementarity cracks. The firewall was, in part, the crack.
- **The singularity problem.** General relativity, applied to a collapsing massive object, drives toward a point at which curvature is infinite, density is infinite, and the equations stop working. Every physicist agrees the singularity is not a feature of nature; it is a notice from the formalism that the formalism has run out. What replaces it has been an open question for sixty years.

### 13.2.2 The four assumptions whose joint imposition generates the paradoxes

Each of the four paradoxes arises from imposing a combination of four assumptions about reality:

- **Global unitarity.** The universe's quantum state evolves perfectly invertibly across all space and time.
- **Global Cauchy data.** The entire state of the universe must be specifiable on a single connected spacelike slice.
- **A sharp geometric boundary.** The horizon is a knife-edge surface, not a fade or a coarse-grained statistical feature.
- **Monogamy at that boundary.** Entanglement between two regions cannot be shared with a third region, particularly enforced at the horizon.

Standard GR plus QFT imposes all four. Each individual assumption is plausible in its respective regime. Their joint imposition at black-hole horizons produces the paradox cluster.

### 13.2.3 The Event Density structural position

ED imposes none of the four assumptions at the substrate level:

- **No global unitarity requirement.** Unitarity is a coarse-grained continuum property of closed sub-systems in the QM-emergence sector (Phase-1, Chapter 5); it is not a global constraint on the substrate.
- **No global Cauchy data.** ED commits events locally; there is no spacelike surface on which the entire universe's state must be specified.
- **No sharp geometric boundary.** A horizon in ED is a coarse-grained statistical feature of cross-bandwidth $\Gamma_\mathrm{cross}$, not a knife-edge geometric locus.
- **No monogamy-at-boundary requirement.** Without a sharp boundary, monogamy-of-entanglement enforcement at one is not a structural requirement.

The four standard paradoxes therefore do not arise. They are not "solved by clever ED machinery" — they are *not generated in framework*. This is structurally distinct from any of the standard interpretive resolutions (Copenhagen, many-worlds, holography, ER=EPR, etc.); ED's substrate ontology does not impose the assumptions whose joint presence is what generates the paradox cluster, and so the cluster does not exist at substrate level.

## 13.3 The Single Substrate Condition

### 13.3.1 The threshold condition

The substrate-level analysis identifies a single condition that unifies six structural results across Arc BH:

```math
\sigma(\mathbf{x}) \;=\; \frac{|\nabla\rho(\mathbf{x})|\,\ell_P^2}{\rho_\mathrm{local}(\mathbf{x})} \;\gtrsim\; \log\!\left(\frac{R_\mathrm{cg}}{\ell_P}\right).
```

The left-hand side is the substrate-scale gradient sparsity $\sigma$ from Chapter 2 — the substrate-natural dimensionless steepness of participation density. The right-hand side is the threshold scale at which the cross-bandwidth $\Gamma_\mathrm{cross}$ falls below hydrodynamic-window resolution under DCGT (Chapter 3). The condition demarcates the regime in which substrate-level analysis transitions from coarse-grained continuum reading (where standard physics applies) to substrate-saturated regime (where the acoustic-metric reading breaks down).

### 13.3.2 What the condition controls

The single condition supports six derivations:

- **Horizon formation (BH-2).** Where the condition is met across a closed surface, $\Gamma_\mathrm{cross}$ collapses below hydrodynamic-window resolution and the surface becomes a substrate-level decoupling surface — the substrate reading of an event horizon.
- **Interior saturation (BH-3).** Where the condition is met in a bulk volume, substrate gradients are at the saturation regime; the acoustic-metric reading fails; substrate dynamics remain finite but the continuum-spacetime description does not.
- **Information blocking (BH-4).** Where the condition is met across the horizon surface, committed structure cannot cross the surface (participation-bandwidth prohibition); entanglement (uncommitted structure) can straddle.
- **Participation-capacity saturation (BH-5).** Where the condition is met, the substrate's participation channels at the surface are at their saturated capacity; the area-law entropy form follows from counting capacity.
- **Strong-curvature scattering (BH-6).** Near the surface, substrate gradients produce the strong-curvature region through which minimal ED-channels (gravitational waves) propagate; the BHPT phase shift is the path-integrated channel-action over this region.
- **Verdict status (BH-7).** All six derivations rest on the same substrate condition; the architectural-level closure is internally consistent.

The single substrate condition unifies the six derivations. This is structurally significant: rather than six separate substrate-level analyses for six separate phenomena, the framework supplies one substrate-level condition with six consequences.

### 13.3.3 Form-FORCED and value-INHERITED

The functional form $\sigma = |\nabla\rho|\ell_P^2/\rho_\mathrm{local}$ and the threshold scale $\log(R_\mathrm{cg}/\ell_P)$ are form-FORCED by Chapter 2's load-bearing invariants and Chapter 3's DCGT cross-bandwidth structure. The specific numerical coefficient $\beta_\mathrm{crit}$ that the condition's right-hand side approximates (with $\beta_\mathrm{crit} \sim \log(R_\mathrm{cg}/\ell_P)$) is INHERITED from substrate-determined dimensionless content; precise prefactor depends on coarse-graining choices.

## 13.4 Horizon as Decoupling Surface (BH-2)

### 13.4.1 The substrate-level horizon

A black-hole event horizon, in standard general relativity, is a sharp surface — a knife-edge null hypersurface separating the interior from the exterior. Across the surface, light cannot propagate outward; the surface is geometric and well-defined.

The substrate-level reading reframes this. A horizon is the surface where the cross-bandwidth $\Gamma_\mathrm{cross}$ between the two sides falls below hydrodynamic-window resolution under DCGT coarse-graining. The substrate-level condition for horizon formation is precisely the single substrate condition: $\sigma \gtrsim \log(R_\mathrm{cg}/\ell_P)$ across a closed surface.

Where this condition is met, $\Gamma_\mathrm{cross}$ collapses exponentially through the DCGT-derived structure $\Gamma_\mathrm{cross} \sim \exp[-\alpha\int_\mathrm{path}\sigma\,d\ell]$ (Chapter 3). At the threshold, the cross-bandwidth becomes effectively zero at the coarse-grained continuum scale — the two sides of the surface decouple. The "fade, not cliff" character of the substrate-level horizon is structurally significant: from coarse-grained continuum perspective the decoupling is sharp, but at the substrate level it is exponential rather than discontinuous.

### 13.4.2 Universal horizon mechanism

The substrate-level horizon mechanism is *universal* across four classes of horizons that standard physics treats as analogous but distinct:

- **Black-hole event horizons.** Strong gradients at high-mass concentrations produce the substrate condition.
- **Rindler horizons.** Acceleration-induced gradients in accelerated frames produce the substrate condition.
- **Cosmological horizons.** $H_0$-scale gradient set by cosmic-horizon participation density produces the substrate condition.
- **Acoustic horizons.** Flow-induced gradients in fluid analog systems (the acoustic metric of analog gravity) produce the substrate condition.

In each case, the horizon is a continuum shadow of the same substrate decoupling surface. The four classes share thermodynamic-style features (temperature, entropy, evaporation analogs) at the standard-physics level; the substrate-level analysis explains why: they are projections of one substrate phenomenon at four different scales.

This is one of the framework's strongest cross-domain unifications. Chapter 14's cross-platform analysis develops it as part of the program's $\Gamma_\mathrm{cross}$-collapse cross-domain echo.

### 13.4.3 The geometric horizon as continuum shadow

The acoustic-metric reading of Arc ED-10 (Chapter 12) supplies the continuum-level definition of an event horizon as the locus of null-geodesic capture in the acoustic metric. The substrate-level decoupling surface and the acoustic-metric event horizon coincide to leading order in the hydrodynamic-window expansion; corrections arise at the substrate scale.

The structural reading: the geometric horizon is the continuum-level reading of the substrate-level decoupling surface. It is not a separate object; it is what the decoupling surface looks like in the coarse-grained continuum. The framework's substrate-level analysis identifies the underlying object (the decoupling surface) and explains its standard-physics reading (the geometric horizon) as the coarse-grained continuum projection.

### 13.4.4 Observer-independence

The decoupling surface is defined as a level set of the substrate scalar $\sigma$. Both $\rho$ and $\nabla\rho$ are coarse-grained substrate quantities; they do not depend on the choice of continuum-observer. The decoupling surface is therefore observer-independent in the same sense that $\rho$ is.

Continuum-observer-dependent statements about which side of the surface a particular continuum trajectory is on do depend on the observer (as expected in the standard-physics horizon framing) — but the surface itself does not. This resolves the "different observers see different horizons" issue at substrate level: the surface is observer-independent; what changes is which trajectory the observer follows relative to the surface.

## 13.5 Singularity Replacement by Saturated Zone (BH-3)

### 13.5.1 The three substrate constraints

Standard general relativity produces curvature singularities at black-hole interiors. The acoustic-metric reading of Arc ED-10 (Chapter 12) is a coarse-grained continuum reading; the substrate ontology's three constraints jointly forbid the divergent quantities that the continuum reading produces.

The three substrate constraints:

- **(C1) Finite participation.** The substrate has a finite count of viable participation channels per coarse-graining cell. There is no substrate state in which infinitely many channels participate at one point. P04 (bandwidth update rule, Chapter 1) plus participation primitives (Chapter 2) supply the finite-participation commitment.
- **(C2) Discrete micro-events.** Substrate events are discrete (P01, Chapter 1). Each commitment is a finite-amplitude occurrence at a finite-resolution patch. Continuum singularity statements that require unboundedly many infinitely small events at a single point are inadmissible at the substrate level.
- **(C3) Gradient saturation.** $|\nabla\rho|$ has a substrate-imposed maximum: when $\sigma \to \beta_\mathrm{crit}$, the substrate's mobility-capacity bound caps further steepening. Gradients cannot run away to infinity. P04's mobility-capacity content (Chapter 2) supplies the saturation commitment.

Any one of (C1)–(C3) alone would suffice to forbid a continuum singularity; the three together overdetermine the result. The substrate ontology has *no singularities*.

### 13.5.2 Acoustic-metric breakdown before substrate

The acoustic metric (Chapter 12) is a coarse-grained kinematic reading of substrate participation density. Its validity requires the hydrodynamic-window expansion of DCGT to be controlled. When $\sigma \gtrsim \beta_\mathrm{crit}$, the multi-scale expansion's small parameter ceases to be small; the acoustic metric ceases to be a controlled approximation.

The acoustic metric breaks down before the substrate does. This is the substrate-level meaning of "singularity": the breakdown is a property of the kinematic continuum reading, not of the underlying substrate. Substrate dynamics remain finite throughout; the continuum-spacetime description fails because the continuum approximation fails, not because reality has run out.

### 13.5.3 The replacement: finite-thickness saturated zone

The substrate replacement for the singular endpoint is a *finite-thickness saturated participation zone* characterized by:

- **Gradients at the substrate-imposed maximum.** $\sigma \to \beta_\mathrm{crit}$ throughout the zone.
- **Cross-participation bandwidth collapsed in all directions.** Not just radial; the saturated zone is decoupled from all neighboring substrate regions in the cross-bandwidth sense.
- **Only the commitment-order direction (P11) remaining structurally meaningful.** Spatial directions become structurally interchangeable when $\sigma$ saturates; only the temporal commitment-order direction remains as a structural direction.
- **Acoustic metric degenerate or undefined.** The continuum kinematic-summary breaks down; no acoustic-metric reading is available within the saturated zone.
- **Substrate dynamics finite.** Substrate-level evolution proceeds as saturated commitment cycles. Nothing diverges.

The saturated zone is not a point; it is a region of finite thickness. Substrate dynamics inside the zone are finite, ordinary, and well-defined. They just do not admit a smooth-spacetime description.

### 13.5.4 No geodesic incompleteness at substrate level

Geodesic incompleteness — the property that null and timelike geodesics in Schwarzschild and Kerr black holes terminate at finite proper time at the central singularity — is a property of the acoustic-metric reading, not of the substrate. At the substrate level, there are no geodesics; there are only commitment-event sequences. Commitment-event sequences inside the saturated zone proceed in finite-amplitude finite-resolution increments; there is no sequence that "ends" at a singular point.

Substrate-level evolution is everywhere defined. The geodesic-incompleteness reading of the singular interior is a continuum-level artifact; at substrate level the evolution continues through saturated commitment cycles, and the standard-physics geodesic incompleteness corresponds to the regime where the continuum reading breaks down.

## 13.6 Information Architecture and Evaporation (BH-4)

### 13.6.1 Committed vs uncommitted structure

ED distinguishes two structurally different forms of correlation at the substrate level:

- **Committed structure (information).** P11-irreversible records of participation events. Transmission of committed structure between two regions requires nonzero $\Gamma_\mathrm{cross}$ between them. This is the substrate analog of "information" in the standard QC and QI literature.
- **Uncommitted structure (entanglement).** Correlation potential between two regions, set up at pair-formation. Persistence of uncommitted structure does not require ongoing cross-bandwidth — it is set by the joint participation amplitude when the pair was created.

This is the substrate translation of the standard quantum-information no-signaling-but-correlations-persist behavior. Two regions can be in a deeply correlated joint state without any ongoing exchange of information; the correlation persists because of how the joint state was prepared, not because of ongoing communication.

### 13.6.2 Information cannot cross a horizon

At the substrate-level decoupling surface (Section 13.4), $\Gamma_\mathrm{cross}$ is below hydrodynamic-window resolution. Therefore:

- **Committed structure transmission across the surface requires bandwidth that is structurally absent.** Information, in the substrate sense, does not pass through a horizon.
- **This is not a causal prohibition.** ED has no fundamental light-cone primitive; the prohibition is a *participation-bandwidth prohibition*. The substrate channels that would carry committed structure have their bandwidth suppressed below resolution.
- **The substrate-level horizon-blocking-information statement** is structurally distinct from the GR-level "information cannot exit a black hole because nothing can travel faster than light." The substrate-level reading is bandwidth-mediated, not lightcone-mediated.

### 13.6.3 Entanglement straddling

Uncommitted structure does not require ongoing $\Gamma_\mathrm{cross}$; it is set by joint participation amplitude at pair-formation. Pair-amplitude structures can therefore exist with one leg inside and one leg outside the decoupling surface without violating Section 13.6.2. Entanglement (uncommitted structure) straddles the horizon freely; only committed structure (information) is blocked.

### 13.6.4 Evaporation as participation re-routing

The substrate-level evaporation mechanism follows from the architecture above:

1. **Horizon blocks committed structure** (Section 13.6.2).
2. **Uncommitted pair structures can straddle the surface** (Section 13.6.3).
3. **Strong $|\nabla\rho|$ near the surface supports pair-creation-class events** (gradient-driven, substrate analog of strong-field vacuum pair production).
4. **Commitment events on these pairs commit one leg inward** (joining the BH-3 saturated zone) **and the other outward** (joining the radiation field).
5. **Joint correlation is preserved globally** across the inward + outward commitments.

This is *participation re-routing*, not information destruction. Hawking radiation, in the substrate-level reading, is the coarse-grained statistics of outward-committed legs of these pair-creation-class events. The thermal-spectrum derivation itself is the next natural arc (B4); the *mechanism* of evaporation as participation re-routing is established in BH-4.

### 13.6.5 No information paradox: not solved, not generated

The four standard assumptions that produce the information paradox (global unitarity, global Cauchy data, sharp geometric boundary, monogamy-at-boundary) are not imposed at substrate level (Section 13.2.3). The paradox does not arise.

The same applies to firewalls and complementarity: both require a sharp geometric boundary, which the ED ontology does not provide. Without the sharp boundary, monogamy-at-boundary and complementarity-versus-non-locality questions do not have well-defined formulations at substrate level.

The framework's stance is structural: BH puzzles are *not solved in framework* but *not generated in framework*. The same pattern applies to the singularity (BH-3) and to the horizon (BH-2). Standard puzzles dissolve when the continuum-level assumptions that generate them are not imposed on a fundamentally local-and-irreversible substrate.

This is the framework's central rhetorical move on black-hole physics, stated structurally: **the information paradox, firewall paradox, complementarity contradiction, and singularity problem are not solved in ED — they simply never arise in its ontology.**

## 13.7 Area-Law Entropy (BH-5)

### 13.7.1 Participation capacity at the decoupling surface

Define the participation-capacity density $\chi(\rho, \nabla\rho)$ as the substrate-level density of viable commitment-channel slots per Planck-area patch on the decoupling surface $\Sigma_H$. The total participation capacity of $\Sigma_H$:

```math
\mathcal{C}_H \;=\; \int_{\Sigma_H} \frac{dA}{\ell_P^2}\,\chi(\rho, \nabla\rho).
```

Two structural points:
- **Area-extensivity.** $\mathcal{C}_H$ scales with the integrated surface area, not with the enclosed volume, because the integrand is supported only on $\Sigma_H$.
- **Saturation in the BH-relevant regime.** $\chi \to 1$ where gradient saturation holds (BH-3); the capacity reduces to $\mathcal{C}_H \approx A/\ell_P^2$.

The area-law form is *derived* from substrate machinery: two-dimensional surface support + gradient saturation + per-patch finite alphabet.

### 13.7.2 Entropy as log of viable commitment histories

ED's substrate-level definition of entropy: $S = \log(\text{number of viable commitment histories compatible with the macroscopic constraint})$. At the decoupling surface, the macroscopic constraint is the participation capacity. With per-patch finite alphabet $g$ (the substrate's local count of distinct commitment motifs per Planck-area patch) and per-patch independence under DCGT:

```math
S \;=\; \mathcal{C}_H\,\log g \;\approx\; \frac{A}{\ell_P^2}\,\log g.
```

The area-law form is now derived. The proportionality constant $\log g$ remains to be determined.

### 13.7.3 The 1/4 coefficient: INHERITED, not derived

The Bekenstein–Hawking value $S_\mathrm{BH} = A/(4\ell_P^2)$ corresponds to $\log g = 1/4$, i.e., $g = e^{1/4} \approx 1.284$. This is *not an integer*. Naive per-patch-independent finite-alphabet counting cannot reproduce $1/4$: integer $g \geq 2$ all give $\log g \geq \ln 2 \approx 0.693$, well above $1/4$.

To recover $1/4$, the per-patch-independence assumption must be relaxed. Adjacent patches share commitment-history correlations through V1-kernel cross-patch overlap; the effective per-patch contribution is reduced from $\log g$ (independent count) to a smaller correlated value. Recovering $1/4$ exactly requires substrate-level state counting that is not currently in hand — structurally similar in difficulty to closed-form derivation of $\kappa/|\hat{N}'| = 0.001766$ (priority item E4) and to closed-form $\mathcal{M}_\mathrm{crit}$ in QC (Chapter 7's O-QC-1).

**Verdict on the 1/4 coefficient: INHERITED, not derived.** Form-FORCED + value-INHERITED methodology applied honestly. Same category as $a_0$ (Chapter 11), $G$ (Chapter 11), $\Lambda$, gauge couplings (Chapter 9), and the other substrate-determined dimensionless numbers in the program.

### 13.7.4 Implications for motif counting and V1 correlations

The closed-form $\log g$ derivation would require either:
- An explicit V1-kernel-counting argument analogous to a substrate-level partition function.
- A derivation of the per-patch commitment alphabet from microscopic substrate dynamics.

Either route is a candidate future arc. Currently flagged as **OPEN item O2** in the program's priority list. The closed-form-substrate-constants program (combining O-QC-1 for $\mathcal{M}_\mathrm{crit}$, O2 for $\log g$, and E4 for $\kappa/|\hat{N}'|$) is the program's structurally-similar collection of closed-form open work.

## 13.8 Wave–Black-Hole Scattering (BH-6)

### 13.8.1 Minimal ED-channel

A minimal ED-channel — a gravitational wave in the continuum reading — is a substrate excitation characterized by:
- Low multiplicity (small number of participation degrees of freedom involved per coarse-graining cell).
- Low anisotropy (anisotropy tensor magnitude small compared to substrate-saturation).
- DCGT-coherent propagation (channel survives multi-scale expansion to a wave equation on the acoustic metric).

The channel's global phase along propagation trajectory $\gamma(\lambda)$:

```math
\Phi[\gamma] \;=\; \int_\gamma \mathcal{A}(\rho, \nabla\rho, \mathrm{anisotropy})\,d\lambda.
```

### 13.8.2 Maximal ED-structure

A maximal ED-structure — a black hole in the continuum reading — is high-multiplicity, saturated-gradient, decoupling-surface-bounded, with curvature-like participation structure given by SG-4 / Arc ED-10 (Chapter 12). In the BH-relevant regime, scattered channels propagate through a region where $\sigma \gg 1$ near $\Sigma_H$ and the acoustic metric is strongly curved.

### 13.8.3 Phase shift as global path-integrated invariant

The minimal channel's propagation kernel is distorted by the maximal structure's saturated gradients. The channel's phase accumulates a shift relative to its asymptotic free-wave value:

```math
\delta_{\ell m} \;=\; \int_\mathrm{path} \Delta\mathcal{A}\,d\lambda
```

with $\Delta\mathcal{A} = \mathcal{A}_\mathrm{full} - \mathcal{A}_\mathrm{asymptotic}$ the curvature-induced excess action density along the trajectory. The shift is a single scalar per partial-wave mode $(\ell, m)$ because the channel is minimal; it is inevitable along any trajectory threading the strong-curvature region because the gradients are saturated.

### 13.8.4 S-matrix exponentiation

The S-matrix structure $S = e^{iN}$ (from ED-I-26) is recovered: $N$ is the integrated channel action; $\delta_{\ell m}$ are its partial-wave components. Exterior-side unitarity follows from BH-4 (no committed structure leaks across $\Sigma_H$, so no probability is lost from the scattering channel; entanglement-amplitude correlations with the interior persist but do not enter exterior unitarity bookkeeping).

### 13.8.5 Helicity preservation and flip

For axisymmetric, non-rotating backgrounds (Schwarzschild-like): principal directions of the participation profile are aligned uniformly along the trajectory's symmetry plane. The channel's anisotropy tensor returns to itself up to an overall scalar phase under parallel transport. **Helicity is preserved**; phase shifts act identically on both helicity states.

For backgrounds with frame-dragging (Kerr-like): principal directions rotate along the trajectory. The channel's anisotropy tensor picks up a twist relative to a non-rotating reference frame:

```math
\Delta\phi_\mathrm{twist} \;=\; \int \omega_\mathrm{FD}\,d\lambda.
```

**Helicity flip channels open**, with mixing strength tied to spin parameter via $\omega_\mathrm{FD}$.

### 13.8.6 Kerr twist and superradiance

The Kerr phase shift relative to Schwarzschild has a substrate origin: frame-dragging is a global rotation of the participation anisotropy basis, sourced by substrate-level vorticity in the participation flow of a spinning maximal structure. The channel acquires a twist proportional to integrated background vorticity along its trajectory. Trajectory-dependence of the integration produces the prograde/retrograde scattering asymmetry.

**Superradiance** (energy extraction by certain scattering channels) is structurally compatible with this picture: channels traversing the rotating-vorticity exterior can net positive energy transfer from background to channel via the participation-flow vorticity. No committed structure is extracted from the interior; the energy transfer is mediated by exterior participation flow. Full amplitude derivation is **OPEN item O1**.

## 13.9 The Conditional-Positive Verdict (BH-7)

### 13.9.1 Architectural-level structural closure

The seven memos of Arc BH (Opening + BH-2 + BH-3 + BH-4 + BH-5 + BH-6 + Synthesis) collectively close the substrate-level architecture of black-hole physics at the architectural level. The closure is conditional-positive: the architectural framework is internally consistent; the structural results are derived from substrate primitives plus closed-arc machinery; specific numerical thresholds (the 1/4 coefficient, the BHPT spectral details, $\beta_\mathrm{crit}$, V1 kernel width) are INHERITED rather than closed-form derived.

The verdict is structurally parallel to NS-Smoothness Intermediate Path C (Chapter 8), Yang–Mills Clay-relevance (Chapter 9), and Arc ED-10 curvature emergence (Chapter 12). Each delivers substrate-grounded structural-positive content with explicit demarcation of what is not closed at higher rigor.

### 13.9.2 What the closure delivers

- **The single substrate condition** unifying horizon formation, interior saturation, information blocking, participation-capacity saturation, and strong-curvature scattering region.
- **Universal horizon mechanism** across BH / Rindler / cosmic / acoustic horizons.
- **No singularities; finite-thickness saturated participation zone replacement.**
- **Information / firewall / complementarity / singularity paradoxes not generated in framework.**
- **Area-law entropy form derived; 1/4 coefficient INHERITED.**
- **BHPT phase-shift structure derived as global path-integrated invariant.**
- **Helicity preservation/flip and Kerr twist** from anisotropy-basis transport plus substrate-level vorticity.
- **Conditional-positive structural closure** at architectural level.

### 13.9.3 What the closure does not deliver

- **Hawking spectrum derivation** (the next natural arc, B4). The mechanism is in hand from BH-4 (asymmetric participation flow at saturated decoupling surface produces outward-radiation statistics); the explicit V5 cross-chain correlation calculation that produces the spectrum is the remaining work.
- **Closed-form 1/4 coefficient.** OPEN item O2; closed-form $\log g$ requires either explicit V1-kernel-counting argument or substrate-level partition function.
- **Superradiance amplitude derivation.** OPEN item O1; structurally compatible per BH-6, but full derivation requires extending BH-6 + Arc SG.
- **Full Kerr interior audit.** OPEN item O3; BH-3 establishes saturated-zone interior structure for Schwarzschild-class BHs; rotating-BH interior architecture (ergosphere, Cauchy horizons, frame-dragging at saturation) requires extension.
- **Constructive-rigor proofs** at any single component. The verdict is structural-positive at substrate-suggestive level, not constructive-rigor.

### 13.9.4 The Hawking-spectrum next arc

Hawking-spectrum derivation (B4) is the next natural concrete arc following Arc BH closure. The components in hand:
- **The mechanism** (BH-4, evaporation as participation re-routing through pair-creation events at the saturated decoupling surface).
- **The substrate-level structural framework** for the spectrum derivation (BH-2's universal horizon mechanism plus BH-4's information-architecture content).
- **The V5 cross-chain memory kernel** (Chapter 1, Chapter 2) as the substrate-level object whose cross-chain correlation calculation produces the spectrum.

The remaining work: the explicit V5 cross-chain correlation calculation. A clean match with $T_H = \kappa/(2\pi)$ would be a structural recovery; a deviation would be a falsifier of the substrate-level framework. Either result is informative.

## 13.10 What This Changes (And What It Doesn't)

### 13.10.1 What does not change

Engineering and astronomical predictions for black-hole physics do not change. Standard general-relativistic black-hole solutions (Schwarzschild, Kerr, Reissner–Nordström, Kerr–Newman) continue to govern strong-field gravity computations. LIGO/Virgo gravitational-wave detection continues to use standard BHPT quasinormal-mode catalogs. Black-hole astrophysics computations proceed unchanged.

### 13.10.2 What does change

Three structural shifts:

- **The standard paradox cluster does not arise.** Information-loss, firewall, complementarity, and singularity paradoxes are not solved in framework but not generated in framework. The four assumptions whose joint imposition produces them are not imposed at substrate level.
- **Horizons become coarse-grained statistical features** of $\Gamma_\mathrm{cross}$ collapse, not knife-edge geometric loci. The decoupling-surface mechanism is universal across BH / Rindler / cosmic / acoustic horizons.
- **Singularities do not exist** as physical objects. The acoustic-metric reading breaks down at $\sigma \gtrsim \beta_\mathrm{crit}$; substrate dynamics remain finite. The replacement is a finite-thickness saturated participation zone.

These three shifts do not change any astronomical observation. They change the structural origin of black-hole architecture — from a combined GR+QFT framework that generates paradoxes to a substrate-level framework in which the paradoxes do not arise.

## 13.11 Form-FORCED vs Value-INHERITED at Black-Hole Architecture

### 13.11.1 What is form-FORCED

- **The single substrate condition** $\sigma \gtrsim \log(R_\mathrm{cg}/\ell_P)$ unifying six derivations.
- **The horizon as decoupling surface** mechanism, universal across BH / Rindler / cosmic / acoustic horizons.
- **The three substrate constraints (C1)–(C3)** jointly forbidding divergent curvature (no singularities).
- **The finite-thickness saturated participation zone** as replacement for the singular interior.
- **The committed-vs-uncommitted structure distinction** producing information blocking + entanglement straddling.
- **The evaporation-as-participation-re-routing** mechanism through pair-creation events at the saturated surface.
- **The non-generation of standard paradoxes** (information, firewall, complementarity, singularity).
- **The area-law form** $S \propto A/\ell_P^2$ from two-dimensional surface support + gradient saturation + per-patch finite alphabet.
- **The BHPT phase-shift structure** as global path-integrated invariant of minimal ED-channels.
- **Helicity preservation/flip from anisotropy-basis transport.**
- **Kerr twist from integrated frame-dragging vorticity.**
- **The conditional-positive structural closure verdict.**

### 13.11.2 What is value-INHERITED

- **The 1/4 coefficient** in the area-law entropy. Corresponds to $\log g \approx 1/4$ from substrate motif counting; closed-form derivation is OPEN item O2.
- **BHPT spectral details.** Specific values of $\delta_{\ell m}$ for given backgrounds; INHERITED from acoustic-metric structure (Chapter 12) and from background-specific content.
- **$\beta_\mathrm{crit}$** in the substrate condition's right-hand side. Substrate-determined dimensionless number; precise prefactor depends on coarse-graining choices.
- **V1 kernel width.** Set the per-patch substrate temporal width entering the motif alphabet $g$.
- **Specific Hawking temperature for any given background.** Depends on V5 cross-chain correlation calculation; the next-arc B4 deliverable.
- **Specific superradiance amplitudes.** OPEN item O1.
- **Specific Kerr-interior architectural details** beyond Schwarzschild-class. OPEN item O3.

### 13.11.3 What is open

Three OPEN items carrying forward from Arc BH:

- **O1 — Superradiance amplitude derivation.** Structurally compatible; full amplitude derivation requires extending BH-6.
- **O2 — Closed-form $\log g$ from substrate motif counting.** Closed-form $1/4$ coefficient; structurally similar in difficulty to O-QC-1 ($\mathcal{M}_\mathrm{crit}$) and E4 ($\kappa/|\hat{N}'|$).
- **O3 — Full Kerr interior audit.** Rotating-BH interior architecture beyond Schwarzschild-class.

Plus the **B4 Hawking spectrum derivation** as the next natural concrete arc.

## 13.12 Dependencies

### 13.12.1 Upstream

- **Chapter 1.** Substrate primitives. Especially: P11 commitment-irreversibility (load-bearing for the committed-vs-uncommitted information architecture); P01 event discreteness (load-bearing for constraint C2 forbidding singularities); P04 bandwidth update rule (load-bearing for constraint C1 finite participation and constraint C3 gradient saturation); the finite-kernel commitment for V1 (load-bearing for the per-patch motif alphabet); substrate locality (load-bearing for the cross-bandwidth structure underlying horizon formation).
- **Chapter 2.** Load-bearing invariants. Gradient sparsity $\sigma$ enters the single substrate condition directly; cross-bandwidth $\Gamma_\mathrm{cross}$ enters horizon formation through DCGT; multiplicity $\mathcal{M}$ enters the saturated-zone interior structure; V1 finite-width vacuum kernel enters the motif alphabet.
- **Chapter 3.** DCGT. The substrate-to-continuum bridge for $\Gamma_\mathrm{cross}$ structure used in horizon formation; the multi-scale expansion underlying the threshold scale $\log(R_\mathrm{cg}/\ell_P)$.
- **Chapter 12.** Arc ED-10 acoustic-metric scalar-tensor framework. The acoustic metric is the kinematic-summary structure that breaks down at $\sigma \gtrsim \beta_\mathrm{crit}$ in BH-3; the curvature-emergence content underlies the strong-curvature scattering region in BH-6.

### 13.12.2 Downstream

- **Chapter 14 (Cross-Platform Unifications).** The cross-domain $\Gamma_\mathrm{cross}$-collapse mechanism shared with QC condition (ii) failure (Chapter 7) at scales separated by ~50 orders of magnitude is one of the program's strongest cross-platform substrate-mechanism identities. Chapter 14 develops it as part of the program's cross-domain unification analysis.
- **Chapter 15 (Public Test Inventory).** Hawking spectrum is the next natural arc (B4); BHPT phase-shift content is anchored against LIGO/Virgo quasinormal-mode catalogs; OPEN items O1, O2, O3 are catalogued.

## 13.13 Canonical Sources

- `papers/Black_Hole_Foundations/`
- Arc BH memos in `theory/Black_Holes/`

The Black_Hole_Foundations paper presents the publication-grade architectural account of the BH sector, including the single substrate condition, the universal horizon mechanism, the singularity replacement, the information non-paradox, the area-law form, the BHPT phase-shift structure, the conditional-positive verdict, and the explicit not-generated-in-framework framing for the four standard paradoxes. Arc BH memos in `theory/Black_Holes/` (seven memos: Opening, Horizon-DCGT, Singularity-And-Strong-Curvature-Audit, Information-And-Evaporation, Area-Law-Entropy, Wave-BH-Scattering, Synthesis) develop each component in detail.

The Monograph Shell's Appendix A theorem provenance map lists DCGT (Chapter 3) and the substrate-condition machinery as the upstream theorems consumed by this chapter. The Notation Glossary in Appendix B lists the symbols used in this chapter (gradient sparsity $\sigma$, cross-bandwidth $\Gamma_\mathrm{cross}$, decoupling surface $\Sigma_H$, area $A$, motif alphabet $g$, BHPT phase shift $\delta_{\ell m}$, channel action $\mathcal{A}$, frame-dragging vorticity $\omega_\mathrm{FD}$).

## 13.14 Optional Figures

**Figure 13.1 — The single substrate condition unifying six derivations.** A central diagram with the substrate condition $\sigma \gtrsim \log(R_\mathrm{cg}/\ell_P)$ at the center and six radial spokes labeled BH-2 horizon formation, BH-3 interior saturation, BH-4 information blocking, BH-5 participation-capacity, BH-6 strong-curvature scattering, BH-7 verdict. Each spoke is annotated with its substrate-level consequence.

**Figure 13.2 — Universal horizon mechanism across four classes.** A four-panel diagram showing four horizon classes (BH event horizons, Rindler horizons, cosmic horizons, acoustic horizons in analog gravity). Each panel shows the substrate-level decoupling surface produced by the same single substrate condition. A central note observes that the four classes share thermodynamic-style features at standard-physics level because they are projections of one substrate phenomenon at four different scales.

**Figure 13.3 — Singularity replacement.** A two-panel diagram. Left panel: standard GR singular interior (curvature divergence, geodesic incompleteness). Right panel: substrate-level finite-thickness saturated participation zone (gradient saturation, finite substrate dynamics, no singularity). A note observes that the acoustic-metric reading breaks down before the substrate does; substrate dynamics remain finite.

**Figure 13.4 — The four assumptions whose joint imposition generates the paradox cluster.** A diagram showing the four assumptions (global unitarity, global Cauchy data, sharp geometric boundary, monogamy-at-boundary) connected to the four paradoxes (information loss, firewall, complementarity, singularity). A central note observes that ED imposes none of the four at substrate level — the paradoxes do not arise.

**Figure 13.5 — Information vs entanglement at the horizon.** A schematic showing committed structure (information, P11-irreversible) blocked at the decoupling surface, and uncommitted structure (entanglement, joint amplitude) straddling the surface freely. A note observes that the blocking is participation-bandwidth, not causal.

**Figure 13.6 — Evaporation as participation re-routing.** A schematic showing pair-creation-class events at the saturated decoupling surface, with one leg committing inward (joining the saturated zone) and the other committing outward (joining the radiation field). Joint correlation is preserved globally; no committed structure is destroyed.

**Figure 13.7 — Area-law entropy form derived; 1/4 coefficient INHERITED.** A two-panel diagram. Left panel: area-law form $S = A/\ell_P^2 \cdot \log g$ derived from substrate participation-capacity at the decoupling surface. Right panel: 1/4 coefficient corresponds to $\log g \approx 1/4$, requires substrate motif counting beyond per-patch independence; INHERITED, OPEN item O2.

**Figure 13.8 — BHPT phase-shift structure.** A schematic showing minimal ED-channel propagating through the strong-curvature exterior of a maximal ED-structure, accumulating phase shift $\delta_{\ell m} = \int_\mathrm{path}\Delta\mathcal{A}\,d\lambda$ as a global path-integrated invariant. Helicity preservation (axisymmetric backgrounds) and helicity flip (frame-dragging backgrounds) shown as anisotropy-basis transport.

**Figure 13.9 — The cross-domain $\Gamma_\mathrm{cross}$-collapse echo.** A length-scale diagram showing the same substrate-condition mechanism producing horizon formation at gravitational-collapse scales (~$10^{38}\,\ell_P$ for stellar-mass black holes) and condition (ii) failure in QC at engineered-system scales (~$10^{-9}$ m for Josephson junctions). Two empirical phenomena, one substrate identity, ~50 orders of magnitude scale separation.

**Figure 13.10 — Form-FORCED vs Value-INHERITED at black-hole architecture.** A two-column diagram. Left column ("Form-FORCED"): single substrate condition, universal horizon mechanism, no singularities, paradoxes not generated, area-law form, BHPT phase-shift structure, helicity behavior, Kerr twist. Right column ("Value-INHERITED"): 1/4 coefficient ($\log g$), BHPT spectral details, $\beta_\mathrm{crit}$, V1 kernel width, specific Hawking temperature, superradiance amplitudes, Kerr interior details.
