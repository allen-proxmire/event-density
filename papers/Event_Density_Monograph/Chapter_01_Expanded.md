# Chapter 1 — The Substrate Ontology: Primitives P1–P13

## 1.1 Chapter Overview

This chapter establishes the program's irreducible base. The Event Density framework rests on thirteen substrate primitives, labeled P01 through P13, that are not derived from anything more fundamental within the framework. They are the program's commitments about what reality is at the level the derivation chain starts from. Every theorem developed in the remaining fourteen chapters is ultimately reachable from a subset of these primitives plus mathematical structure (notably Gleason's 1957 theorem in Phase-1 and Stone's 1932 theorem on one-parameter unitary groups in the Schrödinger derivation, both of which act as bridges between substrate constraints and continuum mathematical structure).

The chapter has no upstream dependencies. It is read by every subsequent chapter; nothing in the program is reachable without it. The chapter's purpose is therefore not to derive but to *establish vocabulary* and *clarify the boundary* between substrate ontology and the emergent continuum physics that the subsequent chapters develop. Specific irreducible commitments — event discreteness, chain worldline structure, the bandwidth update rule, commitment irreversibility, proper-time ordering, and the remaining structural commitments covering participation, multiplicity, finite kernels, and substrate-locality conditions — are introduced in groups organized by the role each plays in the program's downstream theorems.

## 1.2 The Methodological Commitment

### 1.2.1 What the substrate ontology is

The framework treats reality, at the most fundamental level the program reaches, as a network of discrete *events* linked by relational structure. Particles are not fundamental in this picture; they are stable patterns of substrate participation. Fields are not fundamental; they are coarse-grained averages of how participation events relate. Spacetime is not fundamental; it emerges from the coarse-graining of dense, redundant, irreversibly-committed participation networks (Chapter 3 develops this transition formally via the Diffusion Coarse-Graining Theorem).

The thirteen primitives commit the framework to specific properties of the substrate: events are discrete; events live on chain worldlines; participation channels carry bounded bandwidth; commitments are irreversible; chains carry proper-time-ordered structure; and so on through the remaining seven structural commitments. Each primitive is a single sharp commitment that subsequent theorems either use directly in their derivation chain or inherit through intermediate constructions.

### 1.2.2 Why these primitives, not more or fewer

The number thirteen is the program's empirical answer to the question of how many irreducible substrate commitments suffice to derive the program's downstream content. The list is not arbitrary, and it is not minimal in any abstract mathematical sense — it is the smallest set the program has identified that produces the closed-arc inventory: Phase-1 closure of QM (Chapter 5), form-level QFT (Chapter 6), quantum computing architecture (Chapter 7), Navier–Stokes architectural foundations (Chapter 8), Yang–Mills (Chapter 9), soft-matter mobility (Chapter 10), substrate gravity (Chapter 11), curvature emergence (Chapter 12), and black-hole architecture (Chapter 13). Reducing the list further would require deriving one of the primitives from the others; expanding it would mean introducing redundancy. Neither has been needed across roughly thirty months of program development.

The methodological discipline is strict: when a derivation requires a substrate property not already present in the primitive list, the program's options are (a) re-derive the requirement from the existing primitives, (b) demonstrate that the requirement is in fact mathematical structure (in which case it does not require a new primitive), or (c) acknowledge that the derivation is not closed at the substrate level and flag the gap explicitly. The framework has never opted to add a fourteenth primitive to close a derivation. Every closed-arc result reaches its conclusion from a subset of the existing thirteen.

### 1.2.3 The form-FORCED / value-INHERITED methodology starts here

The program's signature methodological pattern — *form-FORCED at the structural level, value-INHERITED at the numerical level* — has its origin point in the substrate primitives. The primitives commit the framework to specific *forms* (events are discrete, commitments are irreversible, chains carry bandwidth) without committing to specific *values* (the precise substrate length scale, the V1 kernel functional shape, the bandwidth-capacity coefficient). Values inherit from substrate constants whose closed-form derivation lives downstream of the primitive layer or is acknowledged as open work. Every chapter respects this distinction; every theorem in the program is form-FORCED at the structural level, with specific numerical thresholds explicitly identified as INHERITED.

This methodology is not merely stylistic. It is the program's structural answer to the question of how a foundational ontology can produce predictive content without overcommitting to specific empirical numbers. The form-FORCED layer is where the framework's content lives; the value-INHERITED layer is where empirical anchors calibrate the form to specific platforms and observations. The primitives are the program's most fundamental form-FORCED layer.

## 1.3 Event-Structural Primitives

### 1.3.1 P01 — Event discreteness

The substrate consists of discrete events, not continuous fields. Each event is a finite, non-divisible occurrence; there are no infinitesimal events and no continuous limits in the substrate's basic ontology. Continuity, when it appears in the program's downstream content, is always the result of coarse-graining over many discrete events through the hydrodynamic-window machinery of Chapter 3.

**Structural role.** P01 is load-bearing for several downstream results. It supplies substrate-level UV-finiteness in form-level QFT (Chapter 6): because events are discrete, there is a smallest length scale built into the substrate, and the divergent loop integrals that motivate renormalization in standard QFT do not have substrate-level analogues. P01 is also load-bearing for the no-singularity result in black-hole architecture (Chapter 13): one of the three substrate constraints that jointly forbid divergent curvature is the discreteness of micro-events, which makes any continuum singularity statement that requires unboundedly many infinitely small events at one point inadmissible at the substrate level.

**Downstream consequences.** UV-finiteness in QFT (Chapter 6); no-singularity in BH-3 (Chapter 13); the discrete-event structure of P11 commitment (downstream); the cross-domain echo with the matter-wave Q-C boundary's mass-cap interpretation in Chapter 7 (large molecules accumulate too many activated internal events to sustain the unresolved regime).

### 1.3.2 P02 — Chain worldline structure

Events are not free-floating; they are linked into *chains* that carry persistent identity. A chain is a sequence of events linked by participation relations; chains have proper-time-ordered structure (handed off to P13 below) and they are the substrate-level object that, after coarse-graining, produces the appearance of particle worldlines.

**Structural role.** P02 supplies the chain forward-propagator structure used in Theorem 18's derivation of the kernel-level arrow of time (Chapter 4). The forward-propagator $U_K(n,m)$ between two chain commitments is identically zero for $n < m$; this property is what makes the chain-contribution sum produce a forward-cone-only kernel, ruling out symmetric, advanced, and hybrid kernels at the primitive level.

**Downstream consequences.** Theorem 18 retardation (Chapter 4); the substrate-level identification of "particle" as a chain pattern (rather than a fundamental object) used throughout Parts II and III; the chain identity that makes commitment-irreversibility (P11) propagate consistently across substrate dynamics.

## 1.4 Participation and Bandwidth Primitives

### 1.4.1 P04 — Bandwidth update rule

Participation channels carry bounded bandwidth. The bandwidth update rule constrains how much of a chain's available participation capacity can be active at any substrate moment, and it constrains how participation transfers across the chain ensemble. P04 is the primitive that gives rise to the multiplicity quantity introduced in Chapter 2 — the count of viable distinct ED-gradient pathways available locally is bounded above by the bandwidth update rule's per-chain capacity.

**Structural role.** P04 is the most heavily-used primitive across the program after P11. It supplies bandwidth conservation across orthogonal decompositions, which is the substrate-level prerequisite for the Born rule's squared form (Chapter 5; Gleason's theorem provides the mathematical bridge from non-contextuality + bandwidth conservation to the squared-amplitude functional). It supplies the finite-bandwidth substrate constraint that produces the Heisenberg uncertainty principle's $\hbar/2$ lower bound (Chapter 5). It supplies the mobility-capacity bound that produces the Universal Mobility Law $M(\rho) = M_0(1 - \rho/\rho_\mathrm{max})^\beta$ in soft-matter rheology (Chapter 10) and the Class A protection mechanism in quantum computing (Chapter 7).

**Downstream consequences.** Born rule (T1–T16, Chapter 5); Heisenberg uncertainty (T1–T16, Chapter 5); UV-finiteness contribution (Chapter 6); Universal Mobility Law (Chapter 10); P4-NonNewtonian rheology classification (Chapter 10); UR-1 condition (i) on multiplicity bounds (Chapter 7); architectural Class A engineered-low-multiplicity protection (Chapter 7).

### 1.4.2 Participation, multiplicity, and channel-structure primitives (grouped)

Several of the remaining primitives commit the framework to structural properties of participation: that participation has multiplicity (a count of locally available pathways); that participation channels can branch, scatter, and recombine; that the substrate supports a notion of participation density $\rho$ that is non-negative and increases monotonically as the universe unfolds. These primitives jointly define what *participation* means at the substrate level and supply the substrate-state quantities that recur across every closed sector.

**Structural role.** Together with P04, these primitives produce the load-bearing invariants developed in Chapter 2: the multiplicity $\mathcal{M}$ as the ED analogue of entropy, the gradient sparsity $\sigma$ as the substrate-scale dimensionless measure of how steeply $\rho$ varies, the cross-bandwidth $\Gamma_\mathrm{cross}$ as the substrate-mediated rate at which adjacent regions exchange correlated participation events. None of these emergent quantities is itself a primitive; each is constructed from the participation/multiplicity/channel primitives in a manner that remains form-FORCED throughout.

**Downstream consequences.** All multiplicity-driven results across Chapters 2, 7, 8, 10, 13. The participation-density gradient $\nabla\rho$ that enters DCGT cross-bandwidth (Chapter 3) and that controls horizon formation in BH-2 (Chapter 13). The participation-channel structure that ED-I-13 reframes as quantum information (Chapter 6).

## 1.5 Commitment and Irreversibility

### 1.5.1 P11 — Commitment irreversibility

P11 is the program's only direction-bearing primitive. Once a substrate event commits — once a participation channel resolves into a definite outcome at a chain endpoint — the commitment cannot be reversed. There is no un-committing, no rewinding, no substrate operation that returns a committed state to its uncommitted form. P11 is sharp: it is a single commitment in a single place. Every other primitive (V1 kernel, participation density, chain structure, bandwidth update) is time-symmetric in isolation; they become forward-oriented only when joined with P11.

**Structural role.** P11 is the substrate-level seed of the arrow of time. Theorem 18 (Chapter 4) propagates P11 through the V1 vacuum response kernel and through chain-sourced response structure to produce the forward-cone-only kernel — the kernel-level arrow of time as a primitive-level structural consequence rather than a postulate. P11 also produces the no-collapse measurement rule in Phase-1 closure of QM (Chapter 5): the standard measurement postulate is replaced by recognition that wavefunction collapse is the coarse-grained continuum signature of substrate-level commitment events. P11 produces the BH-4 information-architecture result (Chapter 13): committed structure cannot un-commit, so committed structure cannot cross a horizon and re-emerge; entanglement (uncommitted structure) can straddle freely. P11 produces the UR-1 commitment-injection failure mode in QC (Chapter 7): each P11 event at a system endpoint contributes to a Poisson-class accumulation that defines the third UR-1 condition's failure timescale.

**Downstream consequences.** Theorem 18 kernel-level arrow (Chapter 4); measurement rule in QM emergence (Chapter 5); information-non-paradox in BH-4 (Chapter 13); commitment-injection failure mode in UR-1 (Chapter 7); the structural basis for "decoherence" as the coarse-grained signature of substrate-level individuation (Chapters 5–7).

### 1.5.2 Why commitment-irreversibility is the only direction-bearing primitive

The framework's choice to put the arrow of time in the ontology — at the level of what reality *is* — rather than in the equations is structurally distinct from standard physics, where the arrow of time is variously assigned to thermodynamics (a boundary condition), cosmology (an expansion-direction choice), measurement (a separate postulate), or radiation (a solution-selection rule applied externally to time-symmetric equations). Each standard account passes the buck to a different layer; none derives the arrow from the laws.

P11 places the arrow at the deepest layer the framework reaches and lets it propagate everywhere else as a structural consequence rather than a postulate. The advantage is sharpness: P11 is a single commitment in a single place, and its propagation through the rest of the program is auditable directly. The cost is that the framework's irreducible base now contains a direction-bearing primitive that cannot be derived from anything else within the framework. The framework treats this cost as acceptable: directionality is one structural commitment that has to live somewhere, and the substrate ontology is the place that allows it to be most cleanly stated.

## 1.6 Temporal Structure

### 1.6.1 P13 — Proper-time ordering

Each chain carries a proper-time-ordered structure. Events along a chain are ordered, and the ordering is intrinsic to the chain — not imposed by an external time coordinate. P13 is the substrate-level analog of the worldline-parametrization of standard relativistic mechanics, but it is committed at the substrate ontological level rather than emerging as a continuum-geometry feature.

**Structural role.** P13 supplies the second piece (alongside P02 chain worldline and P11 commitment-irreversibility) of Theorem 18's forward-cone-only support. The chain forward-propagator $U_K(n,m) = 0$ for $n < m$ is a joint consequence of P02 (chain structure exists), P11 (commitments are irreversible), and P13 (the chain has proper-time ordering). Without P13, P11's irreversibility would not have a chain-internal direction to propagate against; without P02, P11 would not have a chain to propagate through.

**Downstream consequences.** Theorem 18 retardation (Chapter 4); the substrate-level chain ordering that makes substrate dynamics sensible across multiple chains; the proper-time interval used in UV-finiteness derivation (Chapter 6).

## 1.7 Finite-Kernel and Substrate-Locality Primitives

The remaining primitives commit the framework to two related properties: that substrate response kernels are finite-width (the V1 vacuum kernel and the V5 cross-chain memory kernel both have finite temporal width at the substrate scale, formalized later as Theorem N1), and that substrate dynamics are local in the sense that events couple to neighboring events through adjacency relations rather than acting at arbitrary distance.

### 1.7.1 Finite-kernel commitments

The V1 vacuum response kernel mediates participation events at the substrate level. The finite-width commitment — that the kernel has nonzero width at substrate scale rather than acting as an instantaneous delta — is what makes Theorem N1 a substantive result rather than a trivial restatement. The V5 cross-chain memory kernel mediates correlations between distinct chains; its finite width is what makes Maxwell-class viscoelasticity emerge under DCGT coarse-graining (Chapter 10).

**Structural role.** The finite-width commitment is what gives the substrate temporal smearing structure rather than instantaneous response. It is load-bearing for: Theorem N1 (V1 finite-width vacuum kernel, Chapter 4); the kernel-level arrow propagation in Theorem 18 (Chapter 4); the substrate-cutoff hyperviscous regularization R1 in Navier–Stokes (Chapter 8); the Yang–Mills mass-gap mechanism via V1 second-moment expansion (Chapter 9); the V5→Maxwell coarse-graining producing soft-matter viscoelasticity (Chapter 10); the per-patch motif alphabet in BH area-law entropy (Chapter 13).

### 1.7.2 Substrate-locality commitments

The substrate is local in a structural sense: a commitment event in one region can only reach events in its own causal neighborhood — its forward causal cone — not the whole forward time slab of the universe at once. This commitment is what makes the chain-time-forward structure of P11 + P02 + P13 produce a *spacetime-retarded* kernel rather than a forward-time-slab object. Without substrate locality, P11 would force chain-time-forward but the chain-summed kernel would fill the entire forward time slab uniformly; with substrate locality, the chain-summed kernel acquires forward-light-cone-only support.

**Structural role.** Substrate locality is the bridge between chain-time-forward and spacetime-retarded that completes Theorem 18's derivation (Chapter 4). It is also the structural basis for the cross-bandwidth structure $\Gamma_\mathrm{cross} \sim \exp[-\alpha\sigma]$ developed under DCGT (Chapter 3): the cross-bandwidth depends on substrate gradients along the *path* between regions, not on a global state of the entire universe, because substrate dynamics are local.

**Downstream consequences.** Theorem 18 light-cone-only kernel support (Chapter 4); DCGT cross-bandwidth structure (Chapter 3); the BH horizon mechanism as bandwidth-suppression at a *local* substrate-gradient threshold rather than a globally-defined geometric surface (Chapter 13); the QC condition (ii) cross-endpoint connectivity quantity used in UR-1 (Chapter 7).

## 1.8 The Full Roster: Structural Roles at a Glance

The thirteen primitives can be organized by the role each plays in the program's downstream content. The grouping below is for navigational convenience; primitives can and do contribute to multiple downstream theorems.

```math
\begin{array}{l|l}
\text{Group} & \text{Primitives} \\
\hline
\text{Event structure} & \text{P01 event discreteness, P02 chain worldline} \\
\text{Bandwidth and participation} & \text{P04 bandwidth update + participation/multiplicity primitives} \\
\text{Commitment direction} & \text{P11 commitment-irreversibility} \\
\text{Temporal structure} & \text{P13 proper-time ordering} \\
\text{Finite kernels} & \text{V1 / V5 finite-width commitments} \\
\text{Substrate locality} & \text{adjacency / causal-neighborhood commitments} \\
\end{array}
```

The dependency graph from primitives to first-tier downstream theorems can be sketched as follows.

**Phase-1 closure of QM (T1–T16, Chapter 5):** primarily P04 (bandwidth conservation for Born; finite-bandwidth for Heisenberg) plus P11 (measurement) plus P01 (UV-finiteness contribution). Mathematical bridges via Gleason's theorem (1957) and Stone's theorem (1932).

**Theorem 17 — Gauge-Field-as-Rule-Type (Chapter 6):** label-carrying-rule-type structure plus P04 plus DCGT (Chapter 3) coarse-graining of charged-chain populations.

**Theorem N1 + Theorem 18 (Chapter 4):** P02 + P04 + P11 + P13 + finite-width-kernel commitments + substrate-locality. The forcing chain propagates from P11 (forward-only commitments along chains) to spacetime-retarded V1 (forward-cone-only support).

**T19 + T20 + ECR + T21 (Chapter 11):** participation/multiplicity primitives + DCGT + cumulative-strain mechanism + holographic participation-count bound (which is itself a structural commitment, not a separate primitive, since it follows from substrate locality applied to participation-count surfaces).

**DCGT (Chapter 3):** P01 + P04 + finite-kernel commitments + substrate-locality + scale-separation hypothesis $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$.

**UR-1 (Chapter 7):** P04 (multiplicity bound and bandwidth conservation) + P11 (commitment-injection failure mode) + DCGT (cross-endpoint connectivity from substrate-locality + gradient sparsity).

The dependency graph is not flat. Primitives feed first-tier theorems (T1–T16, T17, T18, T19–T21, ECR, N1, GR1, DCGT, UR-1) which in turn feed second-tier results (architectural-class taxonomy, multiplicity-cap function $M$, NS three-angle convergence, MHD classification, Yang–Mills mass-gap, BH no-singularity). Appendix A of the Monograph Shell is the program's authoritative provenance map; this chapter establishes only the primitives at the root of the graph.

## 1.9 The Substrate Boundary

A central methodological task of this chapter is to make explicit the boundary between *substrate ontology* (everything in this chapter and the primitives within it) and *emergent continuum physics* (everything in subsequent chapters). The boundary is not negotiable in the program: substrate-level claims live below the boundary; coarse-grained continuum claims live above it; the bridge between them is DCGT (Chapter 3) and its non-Abelian generalization (Chapter 9).

### 1.9.1 What is substrate-ontological

- The thirteen primitives.
- The substrate-level objects defined directly from them: events, chains, participation channels, commitment events, substrate gradients of $\rho$, finite-width kernels.
- The substrate-level scalar quantities derived without coarse-graining: $\rho$ (participation density), $\nabla\rho$, $\sigma$, $\mathcal{M}$, $\Gamma_\mathrm{cross}$ (substrate-level cross-bandwidth before continuum interpretation), $\Lambda$ (commitment-injection rate at endpoints), $\mathcal{U}$ (participation-rule unresolvedness in UR-1).

### 1.9.2 What is emergent

- Spacetime as a smooth manifold (Chapter 12 makes this explicit at acoustic-metric class).
- Particles as persistent stable participation patterns (Phase-1 closure, Chapter 5).
- Fields as coarse-grained averages over participation events (Chapter 6 develops the gauge-field instance).
- Continuum equations: the Schrödinger equation (Chapter 5), Maxwell's equations (Chapter 9), the Yang–Mills equation (Chapter 9), the Navier–Stokes equation (Chapter 8), the modified Poisson equation (Chapter 11), the acoustic-metric scalar-tensor covariantization (Chapter 12), and so on. Every continuum equation in the program is reached from substrate primitives through DCGT or one of its generalizations.
- "Decoherence" as standardly understood: a coarse-grained signature of substrate-level commitment events, not a fundamental coupling-rate to environment (Chapter 7 develops this reframing for quantum computing).

### 1.9.3 Why the boundary matters

The framework's predictive content is precisely the cross-boundary content: results that follow at the continuum level from commitments made at the substrate level. The matter-wave quantum-classical boundary at 140–250 kDa molecular mass (Chapter 7) is a continuum-level empirical observation; it is identified at the substrate level as a multiplicity-bound crossing in Class A architectures. The slope-4 baryonic Tully-Fisher relation (Chapter 11) is a continuum-level empirical observation across hundreds of galaxies; it is identified at the substrate level as a structural consequence of T19 + T20 + ECR. The 1/4 coefficient in Bekenstein-Hawking entropy (Chapter 13) is a continuum-level GR/QFT result; it is identified at the substrate level as INHERITED from substrate motif counting whose closed-form derivation is downstream work.

The form-FORCED / value-INHERITED distinction lives at this boundary. Form-FORCED content is structurally fixed at the substrate level and propagates upward through coarse-graining. Value-INHERITED content acquires specific numerical values at the empirical or substrate-constants layer. The boundary between them is what gives the program its structure as a derivation chain rather than as a phenomenological assembly.

## 1.10 Form-FORCED vs. Value-INHERITED at the Primitive Level

### 1.10.1 What is form-FORCED at this layer

The thirteen primitives commit the framework to specific structural properties:
- Events are discrete (P01).
- Events live on chains with proper-time ordering (P02 + P13).
- Participation channels have bounded bandwidth (P04).
- Commitments are irreversible (P11).
- Substrate response kernels (V1, V5) are finite-width.
- Substrate dynamics are local in the causal-adjacency sense.

These commitments are form-FORCED in the sense that they fix the *shape* of substrate-level statements that any downstream theorem can reach. They do not commit the framework to specific numerical values for any substrate constant.

### 1.10.2 What is value-INHERITED at this layer

The primitives do not specify:
- The numerical scale of the substrate's smallest length (identified later, via T19 Newton-recovery, with the Planck length $\ell_P$).
- The specific functional shape of the V1 vacuum kernel (Theorem N1 establishes finite-width; the closed-form shape is INHERITED).
- The specific numerical values of any substrate-determined dimensionless threshold ($\beta_\mathrm{crit}$, $\mathcal{M}_\mathrm{crit}$, $\Gamma_\mathrm{min}$, etc., introduced in subsequent chapters).
- The specific numerical values of the substrate inputs ($\hbar$, $c$, $H_0$) used in derivations like T19 ($G = c^3\ell_P^2/\hbar$) and T20 ($a_0 = c\,H_0/(2\pi)$). These are taken as substrate inputs in the program; their specific values are calibrated empirically.

The primitive layer is therefore form-FORCED (the substrate has these properties) and value-anchored at substrate inputs (specific numerical values for $\hbar$, $c$, $H_0$, $\ell_P$ enter the program from outside the primitive layer; closed-form derivation of any of them from other primitives is downstream open work that the framework does not currently claim to have closed).

### 1.10.3 The methodological consistency

The form-FORCED / value-INHERITED pattern starts at the primitive layer and propagates through every chapter. Each downstream theorem inherits the pattern: T17 derives the *form* of gauge fields without committing to which specific gauge group nature realizes; T19 derives the *form* of Newton's law from substrate primitives with the Planck length identified as the substrate length scale through Newton-recovery; UR-1 derives the *form* of three substrate conditions for the unresolved regime with specific numerical thresholds INHERITED. The methodology's consistency across nine sectors of substrate-level architectural closure is itself a structural signature of the framework, addressed at length in Chapter 14.

## 1.11 Dependencies

### 1.11.1 Upstream dependencies

None. This chapter is the program's irreducible base. The thirteen primitives are not derived from anything more fundamental within the framework. The framework treats the question "are the primitives themselves derivable from something more fundamental?" as open work that lives entirely outside the program's current scope.

### 1.11.2 Downstream readers

Every other chapter depends on this chapter. The dependency-graph entries from Chapter 2 onward each cite the primitives that supply substrate content for the chapter's work. Specific primitive-to-chapter dependencies:

- **Chapter 2 — Load-Bearing Invariants.** P01, P02, P04, P11, P13, finite-kernel and substrate-locality primitives. The chapter constructs the load-bearing invariants ($\mathcal{M}$, $\sigma$, $\Gamma_\mathrm{cross}$, V1, P11-as-direction-primitive) directly from the primitives.
- **Chapter 3 — DCGT.** P01, P04, finite-kernel, substrate-locality. The hydrodynamic-window scale separation $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$ rests on substrate-locality and on the Planck-scale event discreteness contributed by P01.
- **Chapter 4 — Theorem N1 + Theorem 18.** P02, P04, P11, P13, finite-kernel, substrate-locality. The forcing chain explicitly cites P11 + P02 + P04 + P13 + Theorem N1 + Q.8 effective-vacuum factorisation.
- **Chapter 5 — Phase-1 closure.** P01, P04, P11. Plus mathematical bridges via Gleason's theorem and Stone's theorem.
- **Chapter 6 — Form-Level QFT and ED-I-13.** P01, P04, P13, label-carrying-rule-type structure (a structural commitment within the participation-channel primitive group).
- **Chapter 7 — Quantum Computation.** P04 (multiplicity bound), P11 (commitment-injection), substrate-locality (cross-endpoint connectivity), DCGT (Chapter 3) for cross-bandwidth structure.
- **Chapter 8 — Navier–Stokes.** P04 + finite-kernel (V1) + DCGT.
- **Chapter 9 — MHD and Yang–Mills.** Chapter 8's content + T17 (Chapter 6) + DCGT non-Abelian extension.
- **Chapter 10 — Soft-Matter Mobility.** P04 + V5 finite-width kernel + DCGT.
- **Chapter 11 — Substrate Gravity.** Participation-density primitives + cumulative-strain mechanism + holographic participation-count bound (substrate-locality applied to surfaces) + DCGT.
- **Chapter 12 — Curvature Emergence.** Chapter 11 + the substrate cumulative-strain four-index object as load-bearing curvature degree of freedom.
- **Chapter 13 — Black-Hole Architecture.** P01 + P04 + P11 + finite-kernel + DCGT + the single substrate condition $|\nabla\rho|\,\ell_P^2/\rho_\mathrm{local} \gtrsim \log(R_\mathrm{cg}/\ell_P)$.
- **Chapters 14–15.** Cross-platform unifications and empirical synthesis. Inherit dependencies from all preceding chapters.

This dependency graph is the program's audit trail. Any claim made in any chapter is traceable to a subset of the thirteen primitives plus mathematical structure.

## 1.12 Canonical Sources

The chapter is built from the following sources, exactly as listed in the Monograph Shell. These are the program's authoritative documents on the substrate ontology; the chapter does not introduce new content beyond what these sources establish.

- `papers/Event_Density_Ontology_and_Axioms/`
- `papers/Foundations_of_Event_Density/`
- `papers/ED_One_Substrate_Three_Domains/` (orientation context for the program-level scope of the substrate ontology)

The Monograph Shell's Appendix A theorem provenance map and Appendix B notation glossary are the cross-reference documents that connect the primitives in this chapter to the downstream theorems and notation used throughout the monograph.

## 1.13 Optional Figures

The following diagrams should appear in the final monograph at this chapter. Descriptions only; no images embedded.

**Figure 1.1 — The dependency graph from primitives to first-tier theorems.** A directed graph with thirteen nodes at the top (P01 through P13) and ten nodes at the bottom (T1–T16 collectively, T17, T18, T19, T20, ECR, T21, N1, GR1, DCGT, UR-1). Edges show which primitives feed which first-tier theorems. The graph makes visible the fact that several primitives (especially P04 and P11) feed many downstream theorems, while others (e.g., P13) play more specialized roles. The graph is the visual form of the dependency content of Section 1.8 and Section 1.11.

**Figure 1.2 — The substrate boundary.** A horizontal line dividing the page. Below the line: primitives, substrate quantities ($\rho$, $\nabla\rho$, $\sigma$, $\mathcal{M}$, $\Gamma_\mathrm{cross}$, $\Lambda$, $\mathcal{U}$), substrate kernels (V1, V5), substrate-locality and chain structures. Above the line: continuum quantities (smooth spacetime, fields, particles, the Schrödinger equation, Maxwell's equations, the Yang–Mills equation, Navier–Stokes, the modified Poisson equation, the acoustic metric, BH horizons). The line itself is labeled "DCGT and non-Abelian generalizations (Chapters 3, 9)." Arrows pass upward across the line for each derivation; no arrows pass downward (the framework does not claim to derive primitives from the continuum).

**Figure 1.3 — Form-FORCED vs Value-INHERITED at the primitive layer.** A two-column diagram. Left column ("Form-FORCED"): event discreteness, chain structure, bounded bandwidth, commitment-irreversibility, finite-kernel widths, substrate-locality. Right column ("Value-INHERITED"): specific numerical scale of $\ell_P$, specific functional shape of V1 kernel, specific values of the dimensionless thresholds $\beta_\mathrm{crit}$, $\mathcal{M}_\mathrm{crit}$, $\Gamma_\mathrm{min}$, the substrate inputs $\hbar$, $c$, $H_0$. The diagram makes explicit the distinction the chapter formalizes in Section 1.10 and that propagates through every subsequent chapter.

**Figure 1.4 — Primitives grouped by structural role.** A simple six-row table or schematic showing the grouping of Section 1.8: event-structure, bandwidth and participation, commitment direction, temporal structure, finite kernels, substrate locality. Each row contains the primitives that serve that role and the first-tier downstream theorems that consume them. This figure is the navigational summary that a reader can use to enter the substrate ontology by structural role rather than by primitive number.
