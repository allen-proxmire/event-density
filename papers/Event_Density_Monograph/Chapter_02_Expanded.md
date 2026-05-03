# Chapter 2 — Load-Bearing Invariants: Multiplicity, Gradient Sparsity, Cross-Bandwidth, V1, P11

## 2.1 Chapter Overview

Five substrate quantities recur throughout the Event Density program and govern every closed-arc result. They are: **multiplicity** $\mathcal{M}$, **gradient sparsity** $\sigma$, **cross-bandwidth** $\Gamma_\mathrm{cross}$, the **V1 finite-width vacuum kernel**, and **P11 commitment-irreversibility**. This chapter introduces each, establishes its substrate-level definition, identifies its structural role across the program, and sets the notation that every subsequent chapter inherits. The five together constitute the framework's *load-bearing invariants*: the substrate-state quantities and substrate-structural commitments without which no continuum derivation in Parts II–IV closes.

The chapter's purpose is not derivational but architectural. The full derivations of $\Gamma_\mathrm{cross}$ from gradient sparsity (DCGT machinery) and of V1 kernel finite-width retardation (Theorem N1 + Theorem 18) live in Chapters 3 and 4 respectively. This chapter establishes only what each invariant *is* at the substrate level, why it is load-bearing for downstream content, and how it connects to the thirteen primitives of Chapter 1. After this chapter, every subsequent chapter can refer to these quantities by their canonical names without ambiguity, and the dependency map of the program rests on a stable vocabulary.

## 2.2 Why These Five, and Not More or Fewer

The program's closed-arc inventory — Phase-1 closure of QM (Chapter 5), form-level QFT (Chapter 6), QC architecture (Chapter 7), Navier–Stokes (Chapter 8), MHD and Yang–Mills (Chapter 9), soft-matter mobility (Chapter 10), substrate gravity (Chapter 11), curvature emergence (Chapter 12), black-hole architecture (Chapter 13) — touches different sectors of physics, but the load-bearing substrate machinery in each closed arc reduces to a small set of recurring quantities. The recurrence pattern is empirical: the program's audit identifies that each of these five invariants appears in at least four of the nine closed sectors, and that no closed arc proceeds without using at least three of them.

Multiplicity $\mathcal{M}$ enters the Born-rule derivation (Chapter 5), the gauge-field-as-rule-type theorem (Chapter 6), the QC architecture's UR-1 condition (i) (Chapter 7), the MHD architectural classification (Chapter 9), the Universal Mobility Law and P4-NonNewtonian rheology (Chapter 10), and the BH area-law entropy (Chapter 13). Gradient sparsity $\sigma$ enters DCGT cross-bandwidth (Chapter 3), the QC architecture's UR-1 condition (ii) (Chapter 7), substrate gravity's cumulative-strain mechanism (Chapter 11), and the BH horizon condition (Chapter 13). Cross-bandwidth $\Gamma_\mathrm{cross}$ governs the QC condition (ii) failure mode (Chapter 7) and the BH horizon-formation mechanism (Chapter 13) under the same DCGT-derived exponential structure. The V1 vacuum kernel mediates the kernel-level arrow of time (Chapter 4), the substrate-cutoff regularization R1 in Navier–Stokes (Chapter 8), the Yang–Mills mass-gap mechanism (Chapter 9), and the per-patch motif alphabet in BH area-law entropy (Chapter 13). P11 commitment-irreversibility is the substrate-level direction-bearing primitive that supplies the arrow of time in Theorem 18 (Chapter 4), the no-collapse measurement rule in Phase-1 (Chapter 5), the information-non-paradox in BH-4 (Chapter 13), and the commitment-injection failure mode in UR-1 (Chapter 7).

The five invariants therefore form the program's recurring vocabulary. Adding a sixth invariant would mean either renaming a downstream construction (such as the unresolvedness $\mathcal{U}$ of Chapter 7, which is built from these five but is not itself one of them) or introducing redundancy. Reducing to four would force at least one closed-arc derivation to lose its substrate-level handle. The framework treats five as the empirically correct count for the program's current scope.

## 2.3 Multiplicity $\mathcal{M}$: The ED Analogue of Entropy

### 2.3.1 Substrate-level definition

Multiplicity $\mathcal{M}(\mathcal{S})$ is the count of viable distinct ED-gradient pathways available locally to a substrate region $\mathcal{S}$. Operationally, it counts the substrate-resolvable participation channels that the region's current ED-structure can support. The quantity is not a probability and not an energy; it is a *count* — an integer at the substrate scale, smoothed to a continuous variable in the coarse-grained reading.

$\mathcal{M}$ is the substrate analogue of entropy. The identification is established in ED-I-01 (Superconductivity): a region with many available ED-gradient pathways has high $\mathcal{M}$, and the substrate's tendency is for $\mathcal{M}$ to grow under environmental forcing the way thermodynamic entropy tends to grow under environmental coupling. A region with few available pathways has low $\mathcal{M}$, and the substrate's tendency is for low-$\mathcal{M}$ states to be metastable rather than dynamically preferred — they require structural mechanisms (lattice symmetry, engineered barriers, topological invariants, redundancy) to be held against the substrate's natural tendency to proliferate gradients.

The two regimes:
- $\mathcal{M} \to 1$: only one viable participation pathway is locally accessible. Hyper-coherent regime. The substrate's gradient structure has collapsed to admit a single coherent channel; charge-related ED-flow is forced into laminar, unified motion. This is the substrate reading of bulk superconductivity (ED-I-01).
- $\mathcal{M} \to \infty$: arbitrarily many distinct pathways are locally accessible. Classical thermal regime. The substrate supports branching, scattering, and decoherence; ED-flow proliferates across many pathways simultaneously.

### 2.3.2 Why multiplicity is the entropy analogue

Standard entropy is the logarithm of the number of microstates compatible with a macrostate. Multiplicity at the substrate level is the count of locally available pathways compatible with a substrate region's current participation structure. The structural correspondence is direct: high $\mathcal{M}$ corresponds to many ways for the substrate to be locally configured, low $\mathcal{M}$ corresponds to few. The thermodynamic-analog readings of $\mathcal{M}$ used throughout the program — that thermal injection raises $\mathcal{M}$, that symmetry collapses it, that decoherence is re-entry into high $\mathcal{M}$ — are direct substrate-level translations of the corresponding entropy statements in standard physics.

The identification is sharper than analogy. ED-I-01 establishes that the macroscopic statistical properties of superconducting transitions (sharp drops in scattering channels at $T_c$, electronic-entropy collapse, simplification of the ED-flow landscape) are direct substrate-level signatures of $\mathcal{M}$ collapsing into a low-multiplicity configuration. Decoherence in the standard quantum-mechanical sense (ED-I-23, ED-I-29, Chapter 7) is identified as the coarse-grained signature of substrate-level commitment events triggered when local $\mathcal{M}$ rises above a threshold.

### 2.3.3 Multiplicity is per-region and per-substrate-timescale

Multiplicity is defined per substrate region per substrate-timescale. A composite system has a *system multiplicity* that depends both on the multiplicity of its constituent regions and on the substrate connectivity between them. This is the structural reason a multi-qubit array's effective multiplicity is not the sum of single-qubit multiplicities: cross-qubit pathway count contributes additively at the substrate level even when individual qubit multiplicities are held low by structural commitment.

Chapter 7 develops the system-multiplicity concept formally. The matter-wave Q-C boundary at 140–250 kDa molecular mass and the qubit-system multiplicity walls (Chapter 7) are both crossings of a single substrate threshold $\mathcal{M}_\mathrm{crit}$, evaluated for two different platform architectures. The cross-platform identity rests on $\mathcal{M}$ being the same substrate quantity in both cases.

### 2.3.4 Downstream consequences

- **Phase-1 closure (Chapter 5):** $\mathcal{M}$'s relationship to bandwidth conservation feeds the Born-rule derivation through Gleason's theorem.
- **Form-level QFT (Chapter 6):** The structural status of multiplicity-counting at substrate level supports the gauge-field-as-rule-type interpretation.
- **Quantum computing (Chapter 7):** UR-1 condition (i) is the explicit multiplicity bound $\mathcal{M}_i \leq \mathcal{M}_\mathrm{crit}$ at every endpoint; the multiplicity-cap function $M$'s Class A static-failure branch is set by $\mathcal{M}_\mathrm{floor}(\mathcal{S}) = \mathcal{M}_\mathrm{crit}$.
- **MHD architectural classification (Chapter 9):** Multiplicity governs whether a continuum content item is canonical-ED (low-$\mathcal{M}$ structural) or transport-kinematic (multiplicity-proliferating).
- **Soft-matter mobility (Chapter 10):** The mobility-capacity bound from P04 produces $M(\rho) = M_0(1-\rho/\rho_\mathrm{max})^\beta$ via the substrate's multiplicity-suppression mechanism near packing.
- **Black-hole entropy (Chapter 13):** $S \propto A/\ell_P^2 \cdot \log g$ is the count of viable commitment histories at the saturated participation surface — a multiplicity count.

## 2.4 Gradient Sparsity $\sigma$

### 2.4.1 Substrate-level definition

Gradient sparsity $\sigma$ is the substrate-scale dimensionless steepness of the participation-density field $\rho$:

```math
\sigma(\mathbf{x}) \equiv \frac{|\nabla\rho|\,\ell_P^2}{\rho_\mathrm{local}}.
```

The numerator measures how rapidly $\rho$ varies in space at the substrate scale (the Planck length $\ell_P$ enters as the substrate-natural length scale, identified with the actual Planck length through T19 Newton-recovery in Chapter 11). The denominator normalizes by the local participation density. The ratio $\sigma$ is dimensionless and substrate-natural: it does not depend on continuum-coordinate choices or on the choice of coarse-graining scale.

Two regimes:
- $\sigma \ll 1$: the substrate is locally smooth at the Planck scale. Continuum approximations are well-controlled; ordinary hydrodynamic-window coarse-graining proceeds without obstruction.
- $\sigma \gtrsim \log(R_\mathrm{cg}/\ell_P)$: the substrate has steepened to the threshold where the multi-scale expansion's small parameter ceases to be small. This is the *decoupling-surface threshold*. At and above this threshold, the substrate region cannot be treated as locally smooth at the coarse-graining scale, and several substrate quantities (cross-bandwidth, the acoustic-metric reading) lose their continuum-approximation validity.

### 2.4.2 Why sparsity, not gradient

The framework uses $\sigma$ rather than $|\nabla\rho|$ directly because the dimensionless ratio is the substrate-scale-natural object and because it admits a clean threshold interpretation. A bare gradient $|\nabla\rho|$ depends on the units used for $\rho$ and on the length scale at which it is measured; the ratio $\sigma$ removes these dependences.

The $\ell_P^2$ factor in the numerator is also substrate-natural: it is the area scale at the substrate's irreducible length, providing the substrate-area normalization that makes $\sigma$ a count-per-substrate-cell quantity. The threshold $\log(R_\mathrm{cg}/\ell_P)$ that recurs throughout the program is the substrate-natural scale-separation magnitude for the hydrodynamic-window expansion to remain controlled.

### 2.4.3 The decoupling-surface threshold

The threshold $\sigma \gtrsim \log(R_\mathrm{cg}/\ell_P)$ is the substrate condition that recurs across multiple closed sectors:

- **BH-2 horizon formation (Chapter 13):** A black-hole event horizon is the surface where $\sigma$ exceeds the threshold. The horizon is not a geometric primitive; it is a substrate-level statistical feature of $\sigma$ crossing.
- **BH-3 singularity replacement (Chapter 13):** The acoustic-metric reading breaks down when $\sigma$ exceeds the threshold; the substrate's saturated participation zone replaces the singular endpoint.
- **QC condition (ii) failure (Chapter 7):** Cross-bandwidth between rule-spanning endpoints collapses when $\sigma$ along the connecting pathway crosses the threshold. This is the structural reason MQT in a Josephson junction (Chapter 7) and horizon formation in a black hole (Chapter 13) share the same substrate mechanism.

The threshold's specific numerical prefactor — the $\log(R_\mathrm{cg}/\ell_P)$ scaling versus a bare numerical constant — is substrate-natural; the precise dimensionless coefficient is INHERITED.

### 2.4.4 Downstream consequences

- **DCGT (Chapter 3):** The cross-bandwidth structure $\Gamma_\mathrm{cross} \sim \exp[-\alpha\sigma]$ uses $\sigma$ as the substrate-scale exponent.
- **Substrate gravity (Chapter 11):** The cumulative-strain mechanism that produces Newton's law is built on integrated substrate gradients, with $\sigma$ controlling the substrate-scale contribution to the strain field.
- **Black-hole architecture (Chapter 13):** The single substrate condition unifying horizon formation, interior saturation, information blocking, participation-capacity saturation, and strong-curvature scattering region is a $\sigma$-threshold condition.
- **Quantum computing (Chapter 7):** $\sigma$ along participation-rule-spanning pathways controls the cross-bandwidth $\gamma_{ij}$ that enters UR-1 condition (ii).

## 2.5 Cross-Bandwidth $\Gamma_\mathrm{cross}$

### 2.5.1 Substrate-level definition

Cross-bandwidth $\Gamma_\mathrm{cross}(\mathbf{x}_1, \mathbf{x}_2)$ is the substrate-mediated rate at which participation events at $\mathbf{x}_1$ and $\mathbf{x}_2$ exchange correlated content. It is the substrate-scale measure of how strongly two regions participate in each other's substrate dynamics. Cross-bandwidth differs from local participation density: $\rho$ measures the participation-channel availability *at* a region; $\Gamma_\mathrm{cross}$ measures the substrate-mediated *exchange* between regions.

DCGT (Chapter 3) establishes the form

```math
\Gamma_\mathrm{cross}(\mathbf{x}_1, \mathbf{x}_2) \sim \exp\!\left[-\alpha\!\int_\mathrm{path}\sigma(\mathbf{x})\,d\ell\right],
```

where the integral runs along the substrate-locality-permitted pathway between the two regions and $\alpha$ is a substrate-determined dimensionless prefactor (INHERITED). The exponential structure follows from the multi-scale expansion's small-parameter behavior: large $\sigma$ along the path creates a steep substrate-scale barrier that suppresses cross-region participation exchange exponentially.

### 2.5.2 Two readings of cross-bandwidth

Cross-bandwidth admits two structurally equivalent readings:

**Substrate-level reading.** $\Gamma_\mathrm{cross}$ is the substrate-scale exchange rate between two regions, computed from substrate-level integrated $\sigma$.

**Coarse-grained reading.** $\Gamma_\mathrm{cross}$, after DCGT coarse-graining, is the continuum-level cross-section / coupling-rate between two regions in the appropriate continuum theory. In the QFT reading (Chapter 6), it relates to vacuum response correlators. In the QC reading (Chapter 7), it is the bandwidth-mediating-rule-integrity quantity that enters UR-1 condition (ii). In the BH reading (Chapter 13), it is the bandwidth that fails at the decoupling surface.

The two readings are the same quantity. The substrate-level reading is the source; the coarse-grained reading is the same quantity evaluated at the continuum scale.

### 2.5.3 Downstream consequences

- **DCGT (Chapter 3):** $\Gamma_\mathrm{cross}$ is the central substrate-to-continuum bridge quantity.
- **Quantum computing (Chapter 7):** UR-1 condition (ii) is $\gamma_{ij} \geq \Gamma_\mathrm{min}$ along every rule-spanning pathway.
- **Black-hole architecture (Chapter 13):** Horizon formation is precisely the surface where $\Gamma_\mathrm{cross}$ falls below hydrodynamic-window resolution. The same substrate mechanism that produces horizons at gravitational-collapse scales produces QC condition (ii) failure at engineered-system scales (Chapter 14 develops this cross-domain identity).
- **Form-level QFT (Chapter 6):** The substrate origin of vacuum-response analytic structure passes through $\Gamma_\mathrm{cross}$ via the V1 kernel mediation.

### 2.5.4 The cross-domain echo

The same $\Gamma_\mathrm{cross}$ structure $\sim \exp[-\alpha\sigma]$ governs both black-hole horizon formation (Chapter 13, scales of order $10^{38}\,\ell_P$ for stellar-mass black holes) and Josephson-junction macroscopic quantum tunneling (Chapter 7, scales of order $10^{-9}\,\mathrm{m}$). The same DCGT exponential structure, evaluated at very different platform scales, produces both phenomena. Chapter 14 develops this as the program's strongest cross-platform substrate-mechanism identity. The structural lesson: the substrate does not distinguish between "gravitational" and "engineered" gradient regions when evaluating cross-bandwidth; it applies the same DCGT machinery at both, and the empirical phenomena that result differ only by the platform-specific values of $\sigma$ along the pathway.

## 2.6 The V1 Finite-Width Vacuum Kernel

### 2.6.1 Substrate-level role

V1 is the substrate-level temporal smearing kernel that mediates participation events. It is the substrate analogue of a vacuum response kernel in standard QFT, but it is committed at the substrate-ontological level rather than emerging from an effective-field-theory construction. The finite-width commitment — that V1 has nonzero width at the substrate scale, rather than acting as an instantaneous delta — is one of the framework's primitive-level structural commitments (Chapter 1).

V1's structural role is to mediate substrate-level participation events with finite temporal smearing. A substrate event at chain endpoint $A$ does not affect chain endpoint $B$ instantaneously; V1 mediates the effect over a finite substrate-temporal width. The width is INHERITED — its specific functional shape is not closed-form derived from any other primitive — but its existence and finiteness are FORCED by the substrate-ontological commitment.

### 2.6.2 Theorem N1: V1 finite-width vacuum kernel

Theorem N1 establishes V1 formally as a finite-width chain-sourced response kernel. The theorem is developed in Chapter 4. Its content at this chapter's level is: the V1 kernel exists, is finite-width, and is sourced by chain-level participation events. The theorem is the substrate-level structural statement; it does not commit to a specific functional shape for the kernel (that is INHERITED).

### 2.6.3 Theorem 18: V1 kernel retardation

Theorem 18 (also Chapter 4) propagates P11 commitment-irreversibility plus chain structure (P02) plus bandwidth update (P04) plus proper-time ordering (P13) plus N1 finite-width through the chain-summed kernel construction to establish that V1 is uniquely forced at the primitive level to have forward-cone-only support. Symmetric, advanced, and hybrid kernels are non-constructible at the primitive level. The microscopic arrow of time is FORCED structurally.

### 2.6.4 Downstream consequences

- **Phase-1 closure (Chapter 5):** V1 mediates the substrate-level analogue of vacuum-response correlations that enter the Born-rule and Schrödinger derivations.
- **Form-level QFT (Chapter 6):** V1 is the substrate-level origin of the standard Wightman correlator and the retarded Green's function structure of QFT. The continuum-approximation structure inherits from V1's substrate-level form.
- **Theorem 18 and the kernel-level arrow (Chapter 4):** V1's forward-cone-only support is the primitive-level statement of the arrow of time.
- **Substrate-cutoff regularization R1 (Chapter 8):** V1's finite width produces the hyperviscous correction term $-\kappa\mu_\mathrm{V1}\ell_P^2 \nabla^4\mathbf{v}$ in Navier–Stokes through DCGT coarse-graining.
- **Yang–Mills mass-gap mechanism (Chapter 9):** V1's second-moment expansion produces the substrate-level mass-gap mechanism.
- **Black-hole area-law entropy (Chapter 13):** V1's per-patch substrate temporal width sets the per-patch motif alphabet $g$ in the BH entropy expression.

## 2.7 P11 Commitment-Irreversibility

### 2.7.1 The framework's only direction-bearing primitive

P11 commits the framework to substrate events being irreversible: once a participation channel resolves into a definite outcome at a chain endpoint, the resolution cannot be reversed. P11 is sharp and single — a single direction-bearing commitment in a single place in the substrate ontology. Every other primitive in the framework is time-symmetric in isolation; only when joined with P11 does any other primitive acquire forward orientation.

The methodological choice is structurally deliberate. Standard physics distributes the arrow of time across multiple incomplete accounts: the thermodynamic arrow (a low-entropy boundary condition at the universe's beginning), the cosmological arrow (an expansion-direction choice), the measurement arrow (a separate quantum-mechanical postulate), and the radiation arrow (a solution-selection rule applied externally to time-symmetric Maxwell equations). Each account passes the buck to a different layer; none derives the arrow from the underlying laws. P11 places the arrow at the deepest layer the framework reaches — the substrate ontology itself — and lets every downstream arrow propagate from it.

### 2.7.2 P11 as substrate-level seed

P11's role across the program:

- **Theorem 18 (Chapter 4):** P11 plus chain structure (P02) plus bandwidth update (P04) plus proper-time ordering (P13) plus V1 finite-width plus substrate locality jointly force the V1 kernel to forward-cone-only support. The kernel-level arrow of time is FORCED at the primitive level.
- **Phase-1 measurement rule (Chapter 5):** Wavefunction collapse is identified as the coarse-grained continuum signature of substrate-level commitment events. There is no separate measurement postulate in the QM emergence sector; P11 supplies the substrate-level mechanism.
- **BH-4 information-non-paradox (Chapter 13):** Committed structure cannot un-commit, so committed structure cannot cross a horizon and re-emerge. Entanglement (uncommitted structure) can straddle. The information paradox does not arise because the four assumptions that generate it (global unitarity, global Cauchy data, sharp geometric boundary, monogamy-at-boundary) are not imposed at the substrate level — and P11 is the primitive that makes the substrate-level account internally consistent.
- **UR-1 condition (iii) (Chapter 7):** Each P11 event at a system endpoint contributes to a Poisson-class accumulation $\int_0^t \Lambda_\mathcal{S}(t')\,dt'$ that defines the third UR-1 condition's failure timescale. The QC operating window's commitment-injection-bounded condition is a direct P11 consequence.
- **Cross-domain unification (Chapter 14):** P11 is the common substrate-level direction-bearing commitment that unifies the kernel-level arrow of time, the measurement rule, evaporation as participation re-routing, and the QC commitment-injection failure mode under one substrate ontology.

### 2.7.3 Why P11 is treated as a primitive rather than derived

The framework's stance on P11's primitive status is methodological. Directionality is one structural commitment that has to live somewhere; the alternative to placing it at the substrate level is to distribute it across multiple postulates downstream. The framework chooses the substrate-level placement because (a) it is sharper — a single commitment in a single place — and (b) it allows propagation to every downstream arrow as a structural consequence rather than as separate postulates.

The cost is that P11 cannot be derived from anything else within the framework. The framework treats this cost as acceptable; the alternative would be to lose either the unification (multiple separate arrow postulates) or the methodological sharpness (a single non-substrate postulate that is more obscurely placed).

## 2.8 The Five Invariants Together: A Structural Map

The five load-bearing invariants form a structural map of the substrate. The map is summarized below.

```math
\begin{array}{l|l|l}
\text{Invariant} & \text{What it measures} & \text{Direct primitive source} \\
\hline
\mathcal{M} & \text{Local pathway count} & \text{P04 + participation primitives} \\
\sigma & \text{Substrate-scale gradient steepness} & \text{Participation density primitives} \\
\Gamma_\mathrm{cross} & \text{Substrate-mediated exchange rate} & \text{P04 + substrate locality + V1} \\
\text{V1} & \text{Finite-width temporal smearing kernel} & \text{Finite-kernel commitment} \\
\text{P11} & \text{Direction-bearing commitment} & \text{P11 itself (primitive)} \\
\end{array}
```

The five interlock structurally. Multiplicity $\mathcal{M}$ is constructed from substrate participation primitives, including the bandwidth update P04 that bounds it from above. Gradient sparsity $\sigma$ is built from the substrate participation-density gradient, the substrate length scale $\ell_P$, and the local participation density. Cross-bandwidth $\Gamma_\mathrm{cross}$ is mediated by V1 and structured by integrated $\sigma$ along substrate-locality-permitted paths. V1 is the substrate-level temporal smearing kernel committed by the finite-kernel primitive and rendered forward-only by P11 + chain structure (Theorem 18). P11 is the direction-bearing commitment that makes the entire structure asymmetric in time.

The interlock is not optional. Removing $\mathcal{M}$ from the program loses the entropy-analogue mechanism that drives QM measurement, QC scaling walls, soft-matter mobility laws, and BH entropy. Removing $\sigma$ loses the substrate-scale gradient measure that drives DCGT, BH horizon formation, and substrate gravity. Removing $\Gamma_\mathrm{cross}$ loses the cross-domain identity between BH horizon formation and QC condition (ii) failure. Removing V1 loses the substrate temporal-smearing structure that supports the kernel-level arrow, R1 substrate-cutoff, and YM mass-gap. Removing P11 loses the direction-bearing primitive — and with it, every downstream arrow of time across the program.

## 2.9 The Five Invariants in the Closed-Arc Inventory

Each closed sector of the program uses the invariants in a specific combination. The combinations are summarized below.

```math
\begin{array}{l|l}
\text{Sector} & \text{Invariants used} \\
\hline
\text{Phase-1 closure of QM (Ch. 5)} & \mathcal{M}, \text{V1}, \text{P11} \\
\text{Form-level QFT (Ch. 6)} & \mathcal{M}, \text{V1}, \text{P11} \\
\text{Quantum computing (Ch. 7)} & \mathcal{M}, \sigma, \Gamma_\mathrm{cross}, \text{V1}, \text{P11} \\
\text{Navier–Stokes (Ch. 8)} & \text{V1} \\
\text{MHD and Yang–Mills (Ch. 9)} & \mathcal{M}, \text{V1} \\
\text{Soft-matter mobility (Ch. 10)} & \mathcal{M}, \text{V1 (V5)} \\
\text{Substrate gravity (Ch. 11)} & \sigma \\
\text{Curvature emergence (Ch. 12)} & \sigma \\
\text{Black-hole architecture (Ch. 13)} & \mathcal{M}, \sigma, \Gamma_\mathrm{cross}, \text{V1}, \text{P11} \\
\end{array}
```

Two sectors — quantum computing (Chapter 7) and black-hole architecture (Chapter 13) — use all five invariants. They are also the two sectors most directly connected by the cross-domain identity of Chapter 14: same $\Gamma_\mathrm{cross}$ collapse mechanism, same substrate-condition threshold $\sigma \gtrsim \log(R_\mathrm{cg}/\ell_P)$, separated by approximately fifty orders of magnitude in physical length. The structural reason both sectors use all five invariants is the same: both involve the full DCGT-mediated substrate-to-continuum machinery applied to gradient-sparsity-driven decoupling, in different platform regimes.

## 2.10 Notation Conventions

The notation introduced in this chapter is consistent with Appendix B of the Monograph Shell. Subsequent chapters use these symbols without redefinition.

- $\mathcal{M}(\mathcal{S})$ — multiplicity at substrate region $\mathcal{S}$.
- $\rho(\mathbf{x})$ — local participation density.
- $\nabla\rho$ — participation density gradient.
- $\sigma(\mathbf{x}) = |\nabla\rho|\,\ell_P^2/\rho_\mathrm{local}$ — substrate-scale gradient sparsity.
- $\Gamma_\mathrm{cross}(\mathbf{x}_1, \mathbf{x}_2)$ — substrate-mediated cross-bandwidth.
- V1 — finite-width vacuum response kernel (Theorem N1).
- V5 — finite-width cross-chain memory kernel (Chapter 10 develops the soft-matter use).
- P11 — substrate primitive of commitment-irreversibility.
- $\ell_P$ — Planck length / substrate length scale (identified with the standard Planck length via T19 Newton-recovery; Chapter 11).
- $R_\mathrm{cg}$ — coarse-graining length scale.
- $L_\mathrm{flow}$ — continuum-flow length scale.
- $\alpha$ — DCGT prefactor in the cross-bandwidth exponential structure.

## 2.11 Form-FORCED vs Value-INHERITED at the Invariant Layer

### 2.11.1 What is form-FORCED at this layer

- The existence and structural definition of multiplicity $\mathcal{M}$ as the count of viable distinct ED-gradient pathways available locally.
- The dimensionless form $\sigma = |\nabla\rho|\,\ell_P^2/\rho_\mathrm{local}$ for substrate-scale gradient sparsity.
- The exponential form $\Gamma_\mathrm{cross} \sim \exp[-\alpha\int_\mathrm{path}\sigma\,d\ell]$ for substrate-mediated cross-bandwidth (formally derived in Chapter 3 via DCGT).
- The existence and finite-width character of the V1 vacuum response kernel.
- The existence and direction-bearing character of P11 commitment-irreversibility.
- The substrate-natural threshold scale $\sigma \gtrsim \log(R_\mathrm{cg}/\ell_P)$ for decoupling-surface formation.

### 2.11.2 What is value-INHERITED at this layer

- The specific functional shape of V1 (finite-width is FORCED; closed-form shape is INHERITED).
- The numerical value of the prefactor $\alpha$ in the cross-bandwidth exponential.
- The numerical value of the dimensionless coefficient in the decoupling-surface threshold (the prefactor on $\log(R_\mathrm{cg}/\ell_P)$, here written as $\beta_\mathrm{crit}$ in subsequent chapters).
- The numerical scale of $\ell_P$ (taken as substrate input; identified with the standard Planck length via T19 Newton-recovery).
- The specific numerical thresholds $\mathcal{M}_\mathrm{crit}$, $\Gamma_\mathrm{min}$, and related quantities introduced in later chapters; these are calibrated against empirical anchors (Chapter 7's matter-wave Q-C boundary at 140–250 kDa is the canonical anchor for $\mathcal{M}_\mathrm{crit}$).

### 2.11.3 Why this matters at the invariant layer

The program's predictive content lives at the form-FORCED structural level. The fact that $\Gamma_\mathrm{cross}$ has exponential structure in integrated $\sigma$ produces all the cross-domain identities (BH horizon ↔ QC condition (ii) failure ↔ JJ macroscopic quantum tunneling). The fact that $\mathcal{M}$ is the substrate analogue of entropy produces all the multiplicity-driven phenomena. The numerical values, where they enter, are inherited from substrate constants whose closed-form derivation is downstream open work (the closed-form-substrate-constants program named in Chapter 15).

## 2.12 Dependencies

### 2.12.1 Upstream

- **Chapter 1.** All thirteen substrate primitives. The five load-bearing invariants are constructed from subsets of the primitives: $\mathcal{M}$ from P04 plus participation primitives; $\sigma$ from participation density primitives plus the substrate length scale; $\Gamma_\mathrm{cross}$ from substrate locality plus V1 plus integrated $\sigma$; V1 from the finite-kernel commitment; P11 from itself.

### 2.12.2 Downstream

- **Chapter 3 (DCGT).** Constructs the explicit form $\Gamma_\mathrm{cross} \sim \exp[-\alpha\sigma]$ from the multi-scale expansion using the invariants of this chapter.
- **Chapter 4 (Theorem N1 + Theorem 18).** Establishes V1's finite-width and forward-cone-only character formally; uses P11 + V1 as central components.
- **Chapter 5 (Phase-1 closure).** Uses $\mathcal{M}$ in the Born-rule derivation through bandwidth conservation; uses P11 in the measurement rule.
- **Chapter 6 (Form-level QFT).** Uses V1 for substrate-level vacuum response; uses $\mathcal{M}$ in gauge-field-as-rule-type interpretation.
- **Chapter 7 (Quantum computing).** All five invariants. Multiplicity bounds UR-1 condition (i); cross-bandwidth and gradient sparsity govern UR-1 condition (ii); commitment-injection (P11-driven) governs UR-1 condition (iii); V1 enters through DCGT.
- **Chapter 8 (Navier–Stokes).** V1's finite width produces the substrate-cutoff R1 hyperviscous term.
- **Chapter 9 (MHD and Yang–Mills).** $\mathcal{M}$ governs the canonical/non-canonical content classification; V1's second-moment produces the YM mass-gap mechanism.
- **Chapter 10 (Soft-matter mobility).** $\mathcal{M}$ enters the Universal Mobility Law; V5 (the V1-companion finite-width kernel) produces Maxwell viscoelasticity through DCGT.
- **Chapter 11 (Substrate gravity).** $\sigma$ enters the cumulative-strain mechanism.
- **Chapter 12 (Curvature emergence).** $\sigma$-structure persists to the covariantization.
- **Chapter 13 (Black-hole architecture).** All five invariants. The single substrate condition unifying horizon formation, interior saturation, information blocking, participation-capacity saturation, and strong-curvature scattering is a $\sigma$-threshold condition; $\Gamma_\mathrm{cross}$ collapses at the surface; $\mathcal{M}$ saturates in the interior; V1 sets the per-patch motif alphabet; P11 supplies the information-non-paradox.
- **Chapter 14 (Cross-platform unifications).** The cross-domain identity between BH horizon formation and QC condition (ii) failure rests on the same $\Gamma_\mathrm{cross}$ structure; the matter-wave ↔ qubit-system identity rests on the same $\mathcal{M}_\mathrm{crit}$ threshold.
- **Chapter 15 (Public test inventory).** Empirical anchors calibrate the value-INHERITED thresholds attached to these invariants.

## 2.13 Canonical Sources

- `papers/Event_Density_Ontology_and_Axioms/`
- ED-I-01 (Superconductivity, Feb 2026; multiplicity-as-entropy; bulk SC as low-$\mathcal{M}$ regime; $T_c$ as multiplicity-overwhelming-symmetry threshold).
- ED-I-23 (Josephson Junctions, Mar 2026; multiplicity at engineered low-$\mathcal{M}$ regions; JJ as deliberately engineered ED-bottleneck; macroscopic quantum coherence as preservation of low-multiplicity geometry).
- ED-I-29 (Tunneling, Mar 2026; sparse-$\sigma$ regions as global participation-rule reconfiguration; tunneling reframed as substrate global reconfiguration across $\sigma$-gap rather than as motion through a forbidden region).

The Monograph Shell's Appendix A theorem provenance map and Appendix B notation glossary are the cross-reference documents that connect the load-bearing invariants of this chapter to the downstream theorems and notation used throughout the monograph.

## 2.14 Optional Figures

**Figure 2.1 — The five load-bearing invariants and their cross-arc usage.** A grid: rows are the five invariants ($\mathcal{M}$, $\sigma$, $\Gamma_\mathrm{cross}$, V1, P11); columns are the nine closed sectors (Phase-1, form-level QFT, QC, NS, MHD/YM, soft-matter, substrate gravity, curvature emergence, BH). Cells are filled where the invariant is used in the sector. The figure makes visible the pattern: $\mathcal{M}$ and V1 appear most widely; $\sigma$ and $\Gamma_\mathrm{cross}$ are concentrated in QC and BH (the cross-domain identity sectors); P11 appears anywhere an arrow of time enters.

**Figure 2.2 — The substrate-natural threshold map.** A horizontal axis showing $\sigma$ from 0 to large values; a marked threshold at $\sigma = \log(R_\mathrm{cg}/\ell_P)$. Below the threshold: ordinary hydrodynamic-window coarse-graining is controlled. Above the threshold: decoupling-surface regime, with annotations for QC condition (ii) failure (Chapter 7), BH-2 horizon formation (Chapter 13), and BH-3 acoustic-metric breakdown (Chapter 13). The figure makes explicit that the same threshold governs phenomena across scales separated by ~50 orders of magnitude.

**Figure 2.3 — The cross-bandwidth path integral.** A schematic showing two regions $\mathbf{x}_1$ and $\mathbf{x}_2$ connected by a substrate-locality-permitted pathway. Along the path, $\sigma(\mathbf{x})$ varies; the integrated $\int_\mathrm{path}\sigma\,d\ell$ enters the exponential form $\Gamma_\mathrm{cross} \sim \exp[-\alpha\int_\mathrm{path}\sigma\,d\ell]$. The figure makes the substrate-locality basis of cross-bandwidth visible.

**Figure 2.4 — The interlock of five invariants.** A pentagonal diagram with the five invariants at the vertices and edges showing the structural dependences: $\mathcal{M}$–P04 (bandwidth update bounds multiplicity), $\sigma$–$\rho$ (sparsity is a gradient measure of participation density), $\Gamma_\mathrm{cross}$–$\sigma$ (cross-bandwidth is integrated sparsity), V1–$\Gamma_\mathrm{cross}$ (V1 mediates the kernel that becomes cross-bandwidth), P11–V1 (P11 forces V1 to forward-cone-only support via Theorem 18). The figure is the visual form of Section 2.8.

**Figure 2.5 — Multiplicity as entropy analogue.** A two-column figure. Left: standard thermodynamic statements (entropy increases under environmental forcing; symmetry collapses entropy; thermal injection raises entropy; decoherence is entropy production). Right: substrate-level statements (multiplicity grows under environmental ED-injection; symmetry collapses multiplicity; thermal injection raises multiplicity; decoherence is re-entry into high multiplicity). Each row shows the thermodynamic statement and its substrate-level translation, with ED-I-01 cited as the canonical source for the identification.
