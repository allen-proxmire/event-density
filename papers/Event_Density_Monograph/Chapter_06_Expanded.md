# Chapter 6 — Form-Level QFT and Quantum Information: T17, UV-Finiteness, ED-I-13

## 6.1 Chapter Overview

Phase-1 (Chapter 5) closes the four postulates of non-relativistic quantum mechanics at the substrate level. This chapter extends the closure into form-level quantum field theory and quantum information. Three results combine to establish the form-level QFT and QI closure: **Theorem 17 (Gauge-Field-as-Rule-Type)** which establishes gauge fields as participation measures of structural rule-types in the substrate; **substrate-level UV-finiteness**, derived from primitives P01 (event discreteness), P13 (proper-time ordering with finite intervals), and P04 (bounded bandwidth), and reframing renormalization as a continuum-approximation tool rather than a substrate requirement; and **ED-I-13 (Quantum Information: Channel Geometry)**, which reinterprets the five landmark results of quantum information theory — Deutsch (1985/92), Deutsch–Jozsa (1992), Bennett–Brassard 1984 (BB84), teleportation (Bennett et al. 1993), and Shor (1994/96) — as five different manipulations of substrate channel geometry.

The chapter does not produce a constructive QFT or a closed-form derivation of the Standard Model. It establishes the *form-level* content: the structural shape of gauge invariance and gauge-field structure (T17), the substrate origin of UV-finiteness (replacing renormalization as a foundational requirement), and the substrate-level vocabulary in which quantum information lives (channel geometry rather than Hilbert-space mystery). The Standard Model gauge group remains empirical input; the framework derives the form of gauge fields without committing to which specific compact-simple-group structure nature realizes. After this chapter, Chapter 7 builds directly on T17, UV-finiteness, and ED-I-13 to develop the substrate-level architecture of quantum computation.

## 6.2 Why Form-Level QFT Closure Matters

### 6.2.1 Two open questions that Phase-1 alone does not close

Phase-1 (Chapter 5) closes non-relativistic QM at the substrate level. Two structural questions remain open after Phase-1 that the form-level QFT chapter addresses:

- **Where do gauge fields come from?** Standard QFT treats gauge invariance as a fundamental principle: pick a symmetry group, require local invariance, and dynamical gauge fields appear as a consequence. Why this principle? Why these specific gauge groups? Why does nature use gauge fields at all? Standard QFT does not say.
- **Why doesn't QFT diverge?** Loop integrals in standard QFT are divergent, and the divergences are absorbed by renormalization. Why does the universe avoid the divergences in practice? Why is renormalization needed in the formalism but not in nature? Standard QFT treats this as a feature of effective-theory machinery rather than as a structural property of reality.

ED reframes both questions. T17 establishes that gauge fields are not fundamental dynamical fields; they are participation measures of structural rule-types in the substrate. The structural origin of gauge invariance is the interface property of label-carrying rule-types — gauge invariance is the symmetry under which rule-type labels can be freely chosen. The substrate-level UV-finiteness establishes that the divergences of standard QFT are artifacts of the continuum approximation rather than properties of reality; the substrate ontology has built-in finiteness through P01 + P13 + P04, and renormalization survives only as a continuum-approximation tool.

### 6.2.2 The third question: what is quantum information?

Standard quantum information theory is built on top of standard QM's Hilbert-space formalism. Five landmark results — Deutsch's first quantum algorithm, Deutsch–Jozsa, BB84 cryptography, teleportation, Shor's factoring algorithm — are treated as ingenious applications of Hilbert-space machinery. Why does each work? The standard answer points to specific Hilbert-space properties (superposition, interference, entanglement, no-cloning, measurement collapse) without identifying a unifying structural mechanism.

ED-I-13 reframes quantum information as the geometry of substrate channels. The five landmark results become five distinct manipulations of substrate channel geometry, each exploiting a different aspect of the substrate's participation structure: high-multiplicity channels supporting global access, minimal channels enforcing rewrite-on-measurement, unresolved participation rules enabling identity reassignment, high-multiplicity channels carrying global periodicity natively. The unifying structural mechanism is the substrate's channel geometry; quantum information becomes a branch of ED-architecture rather than a Hilbert-space mystery.

### 6.2.3 What this chapter delivers structurally

Three closures, each at form level:

1. **Gauge structure closure.** T17 establishes the form of gauge fields and gauge invariance from substrate primitives. The Standard Model gauge group remains empirical input; the structural form is FORCED.
2. **UV-finiteness closure.** Substrate primitives P01 + P13 + P04 deliver UV-finiteness as a substrate property. Renormalization is reframed as continuum-approximation machinery; it is not load-bearing at the substrate level.
3. **Quantum information closure.** ED-I-13 reinterprets the five landmark QI results as substrate channel-geometry manipulations. Quantum information acquires a substrate-level structural foundation.

Together these three closures establish form-level QFT and QI content, complete the form-level closure of the quantum sector that Phase-1 began, and set up Chapter 7's quantum-computing architecture.

## 6.3 Theorem 17: Gauge-Field-as-Rule-Type

### 6.3.1 The structural question

What are gauge fields, structurally? Standard QFT treats them as dynamical fields whose existence follows from gauge invariance. The photon, the gluons, the W and Z bosons, and the Higgs boson are dynamical fields associated with specific gauge groups (U(1), SU(3), SU(2)×U(1), and the Higgs sector). Standard QFT derives the existence of these fields from the gauge principle, but the gauge principle itself — local symmetry under group transformations — is a postulate rather than a derived structural feature.

The structural question becomes: where does the gauge principle come from? Why does nature use gauge fields at all? Why these specific gauge groups?

### 6.3.2 T17's structural content

Theorem 17 establishes gauge fields as **participation measures of structural rule-types** in the substrate. The structural content has three parts:

1. **Rule-type structure.** The substrate's participation channels carry internal labels — labels that distinguish one type of rule from another. A "rule-type" is a class of substrate-level participation rules characterized by its label structure. Charge labels (U(1) labels), color labels (SU(3) labels), and isospin labels (SU(2) labels) are the canonical examples; the structural commitment is that the substrate supports rule-types with internal label-carrying structure.
2. **Participation measure.** A gauge field, structurally, is the participation measure of a rule-type. It measures how participation channels carrying that rule-type's label distribute across the substrate. The "field" is not a fundamental dynamical object in the standard-QFT sense; it is the substrate-level density of label-carrying participation events.
3. **Interface property.** Gauge invariance is the *interface property* of a rule-type — the symmetry under which the rule-type's label can be freely chosen at each substrate location. The structural origin of gauge invariance is the freedom to relabel rule-types without changing the substrate-level participation dynamics. This is structurally distinct from the standard-QFT presentation of gauge invariance as a fundamental principle imposed on the theory.

### 6.3.3 Coverage of Abelian and non-Abelian gauge structures

T17 covers both Abelian (single-label) and non-Abelian (multi-label with non-commuting structure) gauge structures. The Abelian case (U(1)) is the substrate origin of standard electromagnetism: charge labels, charge-carrying participation events, and the gauge-field-as-charge-density-measure structural identification. The non-Abelian case generalizes to compact-simple-group rule-types: SU(2) and SU(3) labels carry non-commuting structure, and the substrate's participation rules across non-commuting labels produce the non-Abelian gauge content.

The structural commitment: T17 is form-FORCED for any compact-simple-group rule-type structure. It does not commit to which specific group nature realizes; the Standard Model's $SU(3) \times SU(2) \times U(1)$ structure is empirical input. What T17 commits to is the *form* — that gauge fields are interface measures of rule-types, that gauge invariance is the rule-type label-relabeling symmetry, and that this form covers Abelian and non-Abelian structures alike.

### 6.3.4 What T17 does and does not derive

T17 derives:
- The structural form of gauge fields (as participation measures of rule-types).
- The structural form of gauge invariance (as interface property under rule-type relabeling).
- The coverage of Abelian and non-Abelian compact-simple-group structures.
- The substrate-level mechanism by which gauge fields mediate interactions between label-carrying participation events.
- The connection to T17-vacuum-coupling-clauses C5–C7, which Theorem 18 (Chapter 4) refines to forward-only directionality.

T17 does not derive:
- Which specific gauge group nature realizes. The Standard Model's $SU(3) \times SU(2) \times U(1)$ structure is empirical input.
- The specific values of gauge couplings (the fine structure constant $\alpha$, the strong coupling $\alpha_s$, the weak coupling, the Higgs vacuum expectation value). These are INHERITED from particle-physics empirical input.
- The Higgs sector's specific structure or mass. Empirical input.
- The number of generations of fundamental fermions or the fermion mass spectrum. Empirical input.

The framework's empirical posture on the Standard Model: the form of gauge structure is FORCED by T17; the specific gauge group, the coupling constants, the particle content, and the masses are INHERITED. This is the form-FORCED / value-INHERITED methodology applied to the gauge sector.

### 6.3.5 The substrate-level mechanism for charge and label conservation

Charge conservation in standard QFT is a Noether consequence of the gauge invariance postulate. In ED, charge conservation is the substrate-level statement that rule-type labels are conserved under substrate dynamics — the labels are intrinsic to chains carrying the rule-type, and substrate dynamics preserve them. The Noether structure inherits from the substrate-level conservation; it is not a separate postulate.

The same applies to other gauge-invariance-derived conservation laws. Color conservation in QCD inherits from substrate-level color-label conservation; weak-isospin conservation inherits from substrate-level weak-isospin-label conservation; etc. The conservation structure is form-FORCED at the substrate level; the specific charge values (electron's $-e$, quark's $\pm \frac{1}{3}e$ or $\pm \frac{2}{3}e$, etc.) are INHERITED.

## 6.4 Substrate-Level UV-Finiteness

### 6.4.1 The structural question

Why is renormalization needed in standard QFT, and why does the universe appear to avoid the divergences that motivate it? Standard QFT loop integrals diverge at high momentum (UV divergence), and the divergences are absorbed by renormalization. Renormalization is technically successful — it produces finite predictions — but it is universally understood to be a workaround for an underlying structural issue. The structural question: where does the universe's UV-finiteness come from?

### 6.4.2 The substrate-level answer

ED supplies a structural answer through three substrate primitives:

- **P01 event discreteness.** Substrate events are discrete; there is a smallest length scale built into the substrate. The continuum limit, where loop integrals run over arbitrary high momentum, does not have a substrate-level counterpart — substrate events do not exist at sub-Planckian length scales because the substrate's irreducible length is the Planck length (identified through T19 in Chapter 11).
- **P13 finite proper-time intervals.** The substrate's proper-time ordering on chains uses finite intervals; there are no infinitesimal proper-time steps at the substrate level. This bounds substrate dynamics' temporal resolution and prevents infinitesimal-time-step divergences from arising.
- **P04 bounded bandwidth.** Participation channels carry bounded bandwidth; the substrate cannot support unbounded high-frequency content at chain endpoints. This caps the substrate's high-frequency dynamics and prevents the integrand of substrate-level loop analogues from diverging at high momentum.

Together, these three primitives make the substrate UV-finite by construction. The substrate-level analogues of standard-QFT loop integrals do not diverge because the substrate has built-in cutoffs at the substrate length scale, the substrate proper-time-step scale, and the substrate bandwidth-quantum scale.

### 6.4.3 Renormalization reframed

Renormalization in standard QFT is not refuted; it is reframed. The continuum approximation that produces standard QFT's loop integrals is a coarse-grained reading of substrate dynamics. The continuum approximation extends substrate dynamics to arbitrary high momentum because it does not see the substrate's discreteness. Renormalization is the technical machinery that handles the resulting apparent divergences in the continuum approximation; it is a continuum-approximation tool rather than a substrate-level requirement.

The framework's stance: standard QFT's renormalization machinery survives as effective-theory machinery for performing continuum-approximation calculations. The substrate ontology does not need it; the divergences renormalization handles do not exist at the substrate level. The Wilsonian effective-theory framing of renormalization (where renormalization is interpreted as integrating out high-momentum modes above a cutoff) is consistent with the substrate-level account: the substrate's UV cutoff is at the substrate length scale, and Wilsonian flow describes how the continuum-approximation effective theory changes as the cutoff is varied within the continuum-approximation regime.

### 6.4.4 The structural payoff

UV-finiteness shifts from a Wilsonian effective-theory consolation to a substrate-level structural property. The framework's claim is not that renormalization is wrong — it is technically successful — but that the structural reason the universe avoids the divergences is the substrate's discrete, bounded character. The continuum approximation produces divergences because it abstracts away from the substrate's structure; the substrate itself does not have them.

The same structural payoff appears in Chapter 13's no-singularity result for black-hole interiors: P01 event discreteness contributes (alongside P04 bounded bandwidth and the gradient-saturation primitive) to forbidding curvature divergences at the substrate level. The continuum singularities of GR are artifacts of the continuum approximation; the substrate has no singularities. The cross-domain consistency between UV-finiteness (Chapter 6) and no-singularity (Chapter 13) is a structural signature of the framework — both are substrate-level structural consequences of the same primitives.

## 6.5 ED-I-13: Quantum Information as Channel Geometry

### 6.5.1 The structural question

Why do the five landmark results of quantum information theory work? Standard quantum information explains each result by appealing to specific Hilbert-space properties — superposition, interference, entanglement, no-cloning, measurement collapse — without identifying a unifying structural mechanism. The five results are presented as ingenious applications of QM machinery, each exploiting a different feature of the formalism.

ED-I-13 reframes the question. Quantum information is the geometry of substrate channels; the five landmark results are five different manipulations of substrate channel geometry. The unifying mechanism is structural: each result exploits a specific aspect of the substrate's participation structure.

### 6.5.2 The substrate-level vocabulary for QI

ED-I-13 introduces the substrate-level vocabulary in which quantum information lives:

- **Multiplicity.** The count of viable distinct ED-gradient pathways available locally, as introduced in Chapter 2. High-multiplicity channels support many simultaneous participation rules; minimal channels enforce strict alignment.
- **Channels.** Substrate-level participation pathways. A channel is defined by its rule-type, its multiplicity, and its endpoint structure. Channels are the substrate-level analogue of "qubits" or "modes" in standard QI.
- **Identity alignment.** A chain's substrate-level identity is encoded in its participation rule. Identity alignment is the substrate-level structure that makes "the same chain" coherent across multiple substrate locations. Operations on identity alignment underlie teleportation in the standard formalism.
- **Global participation.** High-multiplicity channels can carry rules whose content is *global* — properties of the entire channel's geometry rather than properties of any single endpoint. Global participation underlies Deutsch and Deutsch–Jozsa in the standard formalism.
- **Rewrite-on-measurement.** Minimal-multiplicity channels enforce that a measurement event triggers a substrate-level rewrite of the channel's participation rule. Rewrite-on-measurement underlies BB84 cryptography in the standard formalism.

These are not new substrate primitives — they are substrate-level structures that the existing primitives (P01 through P13, the load-bearing invariants of Chapter 2) jointly produce. ED-I-13's contribution is to identify that quantum information lives in this substrate-level vocabulary rather than in Hilbert-space abstractions.

### 6.5.3 The five landmark QI results, restated

ED-I-13 re-derives the five landmark results structurally:

**Deutsch (1985/92): global access via high-multiplicity channels.** The Deutsch algorithm determines whether a function is constant or balanced with a single oracle query. Standard QI explains this through superposition: the oracle is queried "in parallel" on both inputs. ED-I-13 explains it through high-multiplicity channels: the substrate channel carrying the input/output relationship has enough multiplicity to support both function-evaluation pathways simultaneously, and the algorithm reads off the channel's global structure rather than any single pathway. The structural mechanism is multiplicity supporting global access.

**Deutsch–Jozsa (1992): constraint extraction through multiplicity.** The Deutsch–Jozsa algorithm determines whether a function is constant or balanced (over $2^n$ inputs) with a single oracle query. Standard QI explains this through interference. ED-I-13 explains it through global constraint extraction: the substrate channel's global structure encodes the constraint, and the algorithm extracts the structural property without traversing all $2^n$ pathways individually. The structural mechanism is multiplicity-mediated global constraint extraction.

**BB84 (1984): rewrite-on-measurement in minimal channels.** The BB84 quantum cryptography protocol uses non-orthogonal measurement bases to detect eavesdropping. Standard QI explains this through no-cloning. ED-I-13 explains it through rewrite-on-measurement: a minimal-multiplicity channel cannot simultaneously preserve participation rules in non-orthogonal bases; an eavesdropper's measurement triggers a substrate-level rewrite that the legitimate parties can detect. The structural mechanism is rewrite-on-measurement in minimal channels.

**Teleportation (Bennett et al. 1993): identity reassignment across unresolved channels.** Quantum teleportation transfers a quantum state from one location to another using entanglement plus classical communication. Standard QI explains this through entanglement plus classical-bit assistance. ED-I-13 explains it through identity reassignment: an entangled pair establishes an unresolved participation rule across two substrate endpoints; the sender's measurement plus the receiver's correction reassigns the identity alignment from the sender's location to the receiver's location, all through manipulations of the unresolved rule's substrate structure. No state "travels"; identity is reassigned across the unresolved channel. The structural mechanism is identity reassignment.

**Shor (1994/96): symmetry extraction through global geometry.** Shor's factoring algorithm extracts the period of a modular function exponentially faster than classical algorithms. Standard QI explains this through quantum Fourier transform on superposition states. ED-I-13 explains it through symmetry extraction: the periodic structure of the modular function induces a global participation pattern in a high-multiplicity channel; the QFT reads out the global symmetry directly without traversing each input individually. The structural mechanism is global symmetry extraction.

### 6.5.4 The unifying structural mechanism

The five landmark results are not five separate ingenious applications of QM machinery; they are five different manipulations of substrate channel geometry. The unifying mechanism is the substrate's channel structure — multiplicity, identity alignment, global participation, rewrite-on-measurement. Each result exploits a different aspect of the substrate's participation structure, but the underlying structural framework is unified.

The framework's claim is not that the standard explanations of these results are wrong; they are technically correct. The framework reframes the structural origin of why each result works. Quantum information's "magic tricks" become substrate-level architectural moves on channel geometry.

### 6.5.5 ED-I-13's open predictions

ED-I-13 predicts directions for future quantum-information work that follow from the substrate-level reframing:

- **New algorithmic classes** based on symmetry extraction and global constraint resolution. The substrate-level vocabulary identifies dimensions of channel geometry that standard quantum-information theory has not systematically exploited.
- **Structural limits on measurement disturbance** determined by channel multiplicity. This is one of the predictive contents that Chapter 7 develops in the UR-1 architecture and the multiplicity-cap function $M$.
- **New cryptographic primitives** based on channel incompatibility rather than no-cloning.
- **Reinterpretation of entanglement as undeveloped identity** rather than stored correlation. Identity alignment across unresolved channels is the structural object; "entanglement" is the standard-QI label for it.
- **Error correction via distributed alignment** rather than redundancy of states. This is the structural content that Chapter 7 develops as Class C high-multiplicity-redundancy architecture.
- **Computation as manipulation of participation geometry** as a unifying design principle. This is the structural framing that Chapter 7's quantum computing architecture develops formally.

These are form-level structural predictions; specific algorithmic implementations and quantitative measures are downstream open work. ED-I-13's role in this chapter is to establish the substrate-level vocabulary; Chapter 7 develops the architecture that exploits it.

## 6.6 The Form-Level QFT and QI Closure as a Whole

### 6.6.1 What is closed at form level

The chapter closes form-level structural content for QFT and QI:

- **Gauge structure form-closure.** T17 establishes gauge fields as participation measures of structural rule-types; gauge invariance as interface property; coverage of Abelian and non-Abelian compact-simple-group structures.
- **UV-finiteness substrate-closure.** Substrate UV-finiteness from P01 + P13 + P04; renormalization reframed as continuum-approximation tool.
- **Quantum information channel-geometry-closure.** ED-I-13 reinterpretation of five landmark QI results as substrate channel-geometry manipulations; substrate-level vocabulary for QI (multiplicity, channels, identity alignment, global participation, rewrite-on-measurement).

What is *not* closed at form level: the specific gauge group (Standard Model gauge group is empirical input); specific coupling constants, particle masses, and Higgs sector structure (all INHERITED); a constructive proof of QFT existence at Streater–Wightman / Osterwalder–Schrader rigor (Yang–Mills constructive existence is structurally addressed in Chapter 9 at the same Path-C-style verdict); specific quantum algorithms exploiting the substrate-level vocabulary (downstream open work).

### 6.6.2 What this enables for Chapter 7 (Quantum Computation)

The chapter sets up Chapter 7's quantum-computing architecture directly. The substrate-level vocabulary of ED-I-13 — multiplicity, channels, identity alignment, global participation — is exactly the vocabulary in which UR-1 (the Unresolved-Regime Characterization Theorem of Chapter 7) operates. The three substrate conditions of UR-1 are:

- **(i) Multiplicity bounded.** $\mathcal{M}_i \leq \mathcal{M}_\mathrm{crit}$ at every endpoint. ED-I-13's multiplicity vocabulary supplies the substrate-level definition.
- **(ii) Cross-endpoint connectivity sustained.** $\gamma_{ij} \geq \Gamma_\mathrm{min}$ along every rule-spanning pathway. ED-I-13's channel and rule-spanning vocabulary supplies the substrate-level definition.
- **(iii) Commitment-injection bounded.** Inherits from P11 commitment-irreversibility (Chapter 1) and Theorem 18 (Chapter 4).

Chapter 7 also identifies the three architectural classes (engineered-low-multiplicity, global-geometric-rigidity, high-multiplicity-redundancy) that exhaust the substrate-allowed strategies for protecting the unresolved-rule regime; each class's substrate-level mechanism uses the vocabulary established in ED-I-13.

### 6.6.3 The position of form-level QFT closure in the program

Form-level QFT closure sits between Phase-1 closure (Chapter 5) and the continuum theories of Parts III and IV. Phase-1 closes non-relativistic QM at the substrate level; the form-level QFT closure extends to relativistic and gauge-theoretic territory. The continuum theories of Parts III and IV (Navier–Stokes, MHD, Yang–Mills, soft-matter mobility, substrate gravity, curvature emergence, black-hole architecture) build on the form-level closure: T17's minimal-coupling content provides the Lorentz force in MHD (Chapter 9); T17's non-Abelian extension produces the Yang–Mills equation (Chapter 9); UV-finiteness underlies the substrate-cutoff regularization in NS (Chapter 8) and the Yang–Mills mass-gap mechanism (Chapter 9).

The form-level closure is therefore a structural waypoint: it consolidates what Phase-1 establishes about the quantum sector, extends it to gauge-theoretic territory, and sets up the continuum theories that downstream chapters develop.

## 6.7 The CR Framing Applied to Form-Level QFT

The continuum-approximation (CR) framing introduced in Chapter 4 (distinguishing primitive-level retarded V1 from continuum-level Wightman correlator) extends to the form-level QFT closure. Two layers:

- **Primitive level.** T17 gauge-field-as-rule-type; substrate UV-finiteness from P01 + P13 + P04; ED-I-13 substrate channel-geometry vocabulary. These are substrate-level structural commitments.
- **Continuum approximation.** Standard QFT machinery — gauge fields as dynamical fields, gauge invariance as a fundamental principle, renormalization as the technical apparatus for absorbing divergences, Hilbert-space quantum-information theory as the standard formalism for QI. This is continuum-level effective machinery.

The two layers are separately consistent. The primitive level is form-FORCED by substrate primitives; the continuum approximation is the standard machinery used in calculations. The natural correspondences: T17 ↔ standard gauge-field theory; substrate UV-finiteness ↔ Wilsonian effective-theory framing of renormalization; ED-I-13 substrate channel-geometry ↔ standard Hilbert-space quantum information.

The CR framing's value is that it preserves the empirical content of standard QFT and standard QI exactly. ED does not change any standard QFT calculation or any standard QI prediction; it changes the *story underneath*. Form-level QFT closure is a structural-foundational claim, not a discriminating-from-standard-physics claim. The empirical posture is consistent with Chapter 4's empirical posture for Theorem 18.

## 6.8 Form-FORCED vs Value-INHERITED

### 6.8.1 What is form-FORCED

- **T17's structural form** of gauge fields as participation measures of structural rule-types.
- **T17's coverage** of Abelian and non-Abelian compact-simple-group structures.
- **The interface-property origin** of gauge invariance.
- **Substrate-level UV-finiteness** from P01 + P13 + P04.
- **The reframing of renormalization** as a continuum-approximation tool rather than a substrate-level requirement.
- **ED-I-13's substrate channel-geometry vocabulary** for quantum information (multiplicity, channels, identity alignment, global participation, rewrite-on-measurement).
- **The substrate-level reinterpretation of the five landmark QI results** as channel-geometry manipulations.
- **The structural unification** of QI under substrate channel geometry (replacing the standard treatment as five distinct Hilbert-space tricks).

### 6.8.2 What is value-INHERITED

- **The specific gauge group** nature realizes (Standard Model's $SU(3) \times SU(2) \times U(1)$ structure). Empirical input.
- **Specific gauge couplings** (the fine structure constant $\alpha$, the strong coupling $\alpha_s$, the weak couplings, the Higgs vacuum expectation value). Empirical input.
- **Specific particle masses** in the Standard Model. Empirical input.
- **The Higgs sector's specific structure**. Empirical input.
- **The number of generations** of fundamental fermions. Empirical input.
- **Specific quantum algorithms** beyond the five landmark results (depending on substrate channel-geometry properties yet to be systematically exploited).
- **Specific cryptographic primitives** based on substrate channel incompatibility.
- **Specific error-correction schemes** based on distributed alignment.

### 6.8.3 What is open

Several open extensions are flagged for downstream work:

- **Closed-form derivation of substrate constants** entering gauge couplings. This is part of the broader closed-form-substrate-constants program (alongside $\mathcal{M}_\mathrm{crit}$ in Chapter 7, $\log g$ in Chapter 13, and $\kappa/|\hat{N}'|$ in the ED-SC arc).
- **Constructive QFT existence** at Streater–Wightman / OS-axiom rigor. Yang–Mills (Chapter 9) gives a structural-positive verdict at substrate-suggestive level; full constructive existence remains open.
- **Substrate-level account of the Higgs mechanism**. The framework treats this as out of scope for the form-level closure.
- **Generation structure** of fundamental fermions. The framework does not derive the number of generations or the mass spectrum.

## 6.9 Dependencies

### 6.9.1 Upstream

- **Chapter 1.** Substrate primitives, especially P01 (event discreteness, foundational for UV-finiteness), P04 (bandwidth update rule, foundational for UV-finiteness and rule-type label structure), and P13 (proper-time ordering with finite intervals, foundational for UV-finiteness). Plus the participation primitives that supply rule-type label structure.
- **Chapter 2.** Load-bearing invariants. Multiplicity $\mathcal{M}$ enters ED-I-13's substrate channel-geometry vocabulary directly. The V1 kernel mediates substrate-level vacuum response that enters T17 vacuum-coupling content.
- **Chapter 4.** Theorem 18 kernel-level arrow. T17 vacuum-coupling clauses C5–C7 are refined to forward-only directionality through Theorem 18. ED-I-13 inherits the kernel-level arrow indirectly through the substrate-level structural foundation.
- **Chapter 5.** Phase-1 closure. The form-level QFT closure of this chapter extends the QM closure of Chapter 5 to relativistic and gauge-theoretic territory. ED-I-13 builds on Phase-1's substrate-level account of quantum systems.

### 6.9.2 Downstream

- **Chapter 7 (Quantum Computation).** UR-1's substrate-level conditions use the channel-geometry vocabulary established in ED-I-13. The three architectural classes (engineered-low-multiplicity, global-geometric-rigidity, high-multiplicity-redundancy) inherit substrate-level mechanisms from this chapter. The multiplicity-cap function $M$ is the QC-architecture-specific reading of substrate channel-geometry constraints.
- **Chapter 8 (Navier–Stokes).** Substrate UV-finiteness (specifically through V1's finite width producing R1 substrate-cutoff regularization) is the substrate-level content that connects to the NS architectural decomposition.
- **Chapter 9 (MHD and Yang–Mills).** T17 minimal coupling provides the substrate-to-continuum bridge for the Lorentz force; T17's non-Abelian extension produces the Yang–Mills equation; substrate UV-finiteness produces the Yang–Mills mass-gap mechanism through V1's second-moment expansion.
- **Chapter 12 (Curvature Emergence).** ED-Phys-10 acoustic-metric guardrails are consistent with the form-level QFT closure of this chapter; the substrate-level structural commitments (UV-finiteness, no-singularity through P01) are preserved across the gravity sector.
- **Chapter 13 (Black-Hole Architecture).** The cross-domain consistency between substrate UV-finiteness and the no-singularity result of BH-3 inherits from this chapter; both are substrate-level structural consequences of P01 plus related primitives.
- **Chapter 14 (Cross-Platform Unifications).** The form-FORCED methodology, including form-level QFT closure as an example of the program's structural reach, is one of the cross-domain consistency signatures.

## 6.10 Canonical Sources

- `papers/Gauge_Fields_Theorem_17/`
- ED-I-13 (Quantum Information: Channel Geometry, Feb 2026)
- `papers/Arc_Q/`
- `papers/Arc_R/`

The Gauge_Fields_Theorem_17 paper presents Theorem 17 in publication-grade form with the formal derivation of gauge-field-as-rule-type structure. ED-I-13 (the canonical source for the substrate channel-geometry framework) presents the reinterpretation of the five landmark QI results. Arc_Q contains the closure memos for the Arc Q gauge-sector closure that produced T17. Arc_R contains the relativistic-extension memos covering Cl(3,1) signature on the spinor bundle, R.2.5 spin-statistics, and R.3 Dirac equation derivation that connect to T17's relativistic content.

The Monograph Shell's Appendix A theorem provenance map lists T17 with its substrate-input dependencies. The Notation Glossary in Appendix B lists the symbols used in this chapter, including multiplicity $\mathcal{M}$, V1 kernel, and the substrate-level rule-type vocabulary.

## 6.11 Optional Figures

**Figure 6.1 — T17 structural content.** A three-panel diagram. Left panel: standard QFT presentation of gauge fields (gauge invariance as fundamental principle; gauge fields as dynamical objects; renormalization as essential machinery). Middle panel: T17 substrate-level reframing (rule-type label structure on participation channels; gauge fields as participation measures of rule-types; gauge invariance as interface property of rule-types). Right panel: structural correspondence (Abelian U(1) ↔ charge labels; non-Abelian SU(N) ↔ multi-component labels; Standard Model gauge group ↔ empirical input). The figure makes visible the structural transition from postulate-to-theorem at the gauge-field level.

**Figure 6.2 — Substrate UV-finiteness.** A two-panel diagram. Left panel: standard QFT loop integrals diverging at high momentum, with renormalization absorbing the divergences. Right panel: substrate-level UV-finiteness through P01 (event discreteness sets a smallest length scale at $\ell_P$), P13 (finite proper-time intervals bound temporal resolution), P04 (bounded bandwidth caps high-frequency content). A note observes that renormalization survives as continuum-approximation machinery but is not load-bearing at the substrate level.

**Figure 6.3 — The five landmark QI results as channel-geometry manipulations.** A five-row diagram. Each row corresponds to one landmark result (Deutsch, Deutsch–Jozsa, BB84, teleportation, Shor). Columns: (i) Standard QI explanation (superposition, interference, no-cloning, entanglement, quantum Fourier transform); (ii) ED-I-13 substrate-level mechanism (global access via high multiplicity, global constraint extraction, rewrite-on-measurement in minimal channels, identity reassignment across unresolved channels, global symmetry extraction); (iii) The substrate-channel-geometry property exploited. The figure makes visible the unifying structural mechanism across the five results.

**Figure 6.4 — The substrate-level vocabulary for quantum information.** A central diagram showing five interlocking concepts: multiplicity (count of viable pathways); channels (substrate-level participation pathways); identity alignment (substrate-level identity coherence); global participation (high-multiplicity channels carrying global structure); rewrite-on-measurement (minimal-multiplicity channels enforcing substrate-level rule rewrites under measurement). Each concept is annotated with the standard-QI feature it replaces or reframes.

**Figure 6.5 — Form-level QFT closure as a structural waypoint.** A flow diagram showing the seven-stage transition from substrate primitives to QC architecture: substrate primitives (Chapter 1) → load-bearing invariants (Chapter 2) → DCGT bridge (Chapter 3) → kernel-level arrow (Chapter 4) → Phase-1 QM closure (Chapter 5) → form-level QFT and QI closure (Chapter 6, this chapter) → QC architecture (Chapter 7). The figure makes visible the chapter's position in the program's derivation chain.

**Figure 6.6 — Form-FORCED vs Value-INHERITED at form-level QFT.** A two-column diagram. Left column ("Form-FORCED"): T17 gauge-field-as-rule-type structure, Abelian/non-Abelian coverage, gauge invariance as interface property, substrate UV-finiteness, ED-I-13 channel-geometry vocabulary, substrate-level reinterpretation of five landmark QI results. Right column ("Value-INHERITED"): Standard Model gauge group, gauge couplings, particle masses, Higgs sector structure, generation structure, specific quantum algorithms beyond the five landmark results. The figure makes visible the demarcation that propagates through Chapters 7, 9, and 13.
