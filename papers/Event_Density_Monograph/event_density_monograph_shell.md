---
title: |
  Event Density: A Substrate-Level Architecture of Physics
  \large{Foundations, Theorems, and Architectural Closure Across Nine Sectors}
author: Allen Proxmire
date: May 2026 (Shell v0.1)
---

# Title Page

**Event Density: A Substrate-Level Architecture of Physics**

*Foundations, Theorems, and Architectural Closure Across Nine Sectors*

Allen Proxmire — May 2026

**Status:** Monograph Shell v0.1. Each chapter is a structural summary; full integrated derivations live in the canonical sources cited per chapter. The shell is intended to be navigated as a single document and progressively expanded chapter-by-chapter into the full monograph.

---

# Foreword

The Event Density (ED) program develops the substrate-level physics underneath quantum mechanics, classical field theory, fluid dynamics, gauge theory, gravitation, and quantum information. Across roughly thirty months of development the program closed nine sectors at the architectural level — each producing a publication-grade Foundations paper or Synthesis paper, each derived from the same set of substrate primitives, each consistent with every other closed sector. The body of work is now too large to navigate without an integrating document.

This monograph provides that integrating document. It does not replace the existing publication-grade papers; it organizes them, unifies the vocabulary, maps the dependency graph between theorems, and gives any reader — internal or external — a single canonical entry point to the program.

The shell organizes the program into five Parts and fifteen chapters. Each chapter establishes what the chapter contributes architecturally, names its dependencies on earlier chapters and theorems, and points to the canonical source paper(s) carrying the full derivation. Four appendices give the theorem provenance map, a notation glossary, a paper-to-chapter cross-reference, and a substrate-constants table.

The shell is itself the navigation. As the program continues, the shell progressively absorbs each chapter's full content; chapters that have been expanded retain the same dependency graph as their summary. The shell stays valid even if no chapter is ever fully expanded, and any chapter that does get fully written progressively replaces its placeholder summary in place. This is the standard pattern by which large research programs incrementally produce a monograph from an existing publication corpus.

The methodological commitment is consistent across the program: **the structural form of each result is derived from substrate primitives; specific numerical thresholds are calibrated empirically rather than computed in closed form.** The shell preserves this distinction throughout; every chapter notes form-FORCED content separately from value-INHERITED content, and the appendices identify which substrate constants currently sit at which empirical anchors.

---

# How to Read This Monograph

Three reading paths.

**Linear.** Read Parts I–V in order. Part I establishes the substrate ontology and the coarse-graining bridge to continuum physics; Part II derives quantum mechanics and quantum computation as substrate consequences; Part III handles classical field theory and fluid dynamics; Part IV handles the gravitational sector; Part V provides the empirical synthesis and open extensions.

**By sector.** A reader interested in a specific sector can jump directly to the relevant chapter. Each chapter is self-contained at the structural-summary level and points to its canonical sources; readers who want full derivational detail follow the source pointers into the existing publication-grade papers.

**By theorem.** Readers tracking the theorem inventory (T1–T21, plus the foundational theorems N1, GR1, DCGT, ECR, and UR-1) can use Appendix A as the navigation map. The provenance graph in Appendix A names the source paper for each theorem and the dependency chain from substrate primitives.

**Cross-references.** Each chapter cites its canonical source paper(s) by repository path. Each appendix is consistent with the chapters: Appendix A's theorem provenance map matches the dependency chains stated in the chapters; Appendix B's notation glossary covers every symbol used in the chapter summaries; Appendix C assigns each existing publication-grade paper to exactly one chapter; Appendix D collects every substrate constant referenced.

The shell does not duplicate derivations. When a chapter says "T17 establishes that..." and points to the T17 paper, the reader who wants the proof reads the T17 paper. When a chapter says "the multiplicity-cap function $M$ takes the form..." and points to the QC Foundations Paper, the reader who wants the construction reads that paper. The shell's role is to make the dependency structure visible and the navigation tractable.

The methodological vocabulary is consistent throughout. **Form-FORCED** means: the structural form of a result is derived from substrate primitives. **Value-INHERITED** means: specific numerical thresholds inherit from substrate constants whose closed-form derivation is downstream work. Every chapter respects this distinction.

---

# Table of Contents

**Part I — Substrate Foundations**

- Chapter 1: The Substrate Ontology — Primitives P1–P13
- Chapter 2: Load-Bearing Invariants — Multiplicity, Gradient Sparsity, Cross-Bandwidth, V1, P11
- Chapter 3: The Coarse-Graining Bridge — DCGT, Hydrodynamic Window, Multi-Scale Expansion
- Chapter 4: Kernel-Level Arrow of Time — Theorem N1 + Theorem 18

**Part II — Quantum Sector**

- Chapter 5: Phase-1 Closure of Quantum Mechanics — T1–T16
- Chapter 6: Form-Level QFT and Quantum Information — T17, UV-Finiteness, ED-I-13
- Chapter 7: Quantum Computation — UR-1, the Multiplicity-Cap Function $M$, Architectural Taxonomy

**Part III — Continuum and Dynamics**

- Chapter 8: Navier–Stokes Architectural Foundations — Form-FORCED, R1, Path C
- Chapter 9: Magnetohydrodynamics and Yang–Mills — T17 Coupling, DCGT Continuum, Mass-Gap Mechanism
- Chapter 10: Soft-Matter Mobility and Non-Newtonian Rheology — UDM, P4-NN, V5

**Part IV — Gravity and Cosmology**

- Chapter 11: Substrate Gravity at Galactic Scale — T19, T20, ECR, T21
- Chapter 12: Curvature Emergence — Arc ED-10, Acoustic-Metric Covariantization
- Chapter 13: Black-Hole Architecture — Arc BH, Horizons, Area Law, Phase-Shift Structure

**Part V — Empirical Synthesis**

- Chapter 14: Cross-Platform Unifications — Matter-Wave ↔ Qubit, $\Gamma_\mathrm{cross}$ Collapse, Methodology
- Chapter 15: Public Test Inventory and Open Extensions

**Appendices**

- Appendix A: Theorem Provenance Map
- Appendix B: Notation Glossary
- Appendix C: Paper-to-Chapter Cross-Reference
- Appendix D: Substrate Constants and Inherited Values

**Closing Note**

\newpage

# Part I — Substrate Foundations

Part I establishes the substrate ontology that every subsequent chapter rests on. It introduces the thirteen primitives, names the load-bearing substrate quantities, develops the coarse-graining bridge from substrate to continuum, and proves the kernel-level arrow of time. After Part I, every continuum theory in Parts II–IV is reachable as a coarse-grained consequence of the substrate machinery developed here.

## Chapter 1 — The Substrate Ontology: Primitives P1–P13

The Event Density framework's substrate ontology is built from thirteen primitives, P1 through P13. The primitives are not derived from anything more fundamental; they are the irreducible commitments of the framework. Every theorem in the program is ultimately reachable from a subset of these primitives plus mathematical structure. This chapter lists the primitives, explains their structural role, and establishes the canonical vocabulary in which subsequent chapters operate.

The primitives include event discreteness (P01), chain worldline structure (P02), bandwidth update rule (P04), commitment irreversibility (P11), proper-time ordering (P13), and seven additional structural commitments covering participation, multiplicity, finite kernels, and substrate-locality conditions. Together they define what the substrate is and what it can do; everything else in the monograph is a consequence.

### What this chapter establishes

- The thirteen substrate primitives P1–P13 and their irreducible status.
- The structural role of each primitive in the program's downstream theorems.
- The boundary between substrate ontology (this chapter) and emergent continuum physics (later chapters).
- The canonical vocabulary for participation events, chain structure, commitment, and substrate locality.

### Dependencies

- None. This chapter is the program's irreducible base.

### Canonical sources

- `papers/Event_Density_Ontology_and_Axioms/`
- `papers/Foundations_of_Event_Density/`
- `papers/ED_One_Substrate_Three_Domains/` (orientation context)

\newpage

## Chapter 2 — Load-Bearing Invariants: Multiplicity, Gradient Sparsity, Cross-Bandwidth, V1, P11

Five substrate quantities recur throughout the program and govern every closed-arc result. This chapter introduces each, establishes its structural role, and sets the notation used in every subsequent chapter.

**Multiplicity** $\mathcal{M}$ is the count of viable distinct ED-gradient pathways available locally — the substrate analogue of entropy. **Gradient sparsity** $\sigma = |\nabla\rho|\,\ell_P^2/\rho_\mathrm{local}$ is the substrate-scale steepness of participation density. **Cross-bandwidth** $\Gamma_\mathrm{cross}$ is the substrate-mediated rate at which adjacent regions exchange correlated participation events; DCGT establishes $\Gamma_\mathrm{cross} \sim \exp[-\alpha\sigma]$. **The V1 finite-width vacuum kernel** is the substrate-level temporal smearing kernel mediating participation events, established formally as Theorem N1. **P11 commitment-irreversibility** is the only direction-bearing primitive in the program — once a substrate event commits, the commitment cannot be reversed.

The chapter clarifies why these five quantities are load-bearing: every continuum equation derived in Parts II–IV is governed by their substrate-level dynamics, and every architectural classification across the closed arcs (NS, MHD, YM, SG, BH, QC) is expressible in terms of how these quantities behave under coarse-graining.

### What this chapter establishes

- Multiplicity $\mathcal{M}$ as the ED analogue of entropy, with its substrate-level definition and role.
- Gradient sparsity $\sigma$ as the substrate-scale dimensionless gradient measure.
- Cross-bandwidth $\Gamma_\mathrm{cross}$ as the substrate exchange rate between regions, with its DCGT-derived form.
- The V1 finite-width vacuum kernel as substrate temporal-smearing structure (full derivation in Chapter 4).
- P11 commitment-irreversibility as the substrate's sole direction-bearing primitive.

### Dependencies

- Chapter 1 (the substrate primitives).

### Canonical sources

- `papers/Event_Density_Ontology_and_Axioms/`
- ED-I-01 (Superconductivity, Feb 2026; multiplicity-as-entropy)
- ED-I-23 (Josephson Junctions, Mar 2026; multiplicity at engineered low-$\mathcal{M}$ regions)
- ED-I-29 (Tunneling, Mar 2026; sparse-$\sigma$ regions and global reconfiguration)

\newpage

## Chapter 3 — The Coarse-Graining Bridge: DCGT, Hydrodynamic Window, Multi-Scale Expansion

The Diffusion Coarse-Graining Theorem (DCGT) is the substrate-to-continuum bridge for canonical-ED dynamical content. Its significance is that *every* continuum theory developed in Parts II–IV passes through DCGT or its non-Abelian generalization. Without DCGT, the program would have substrate primitives on one side and standard continuum physics on the other with no derivation chain connecting them; with DCGT, the chain is explicit.

The chapter establishes the hydrodynamic-window scale separation $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$ under which substrate dynamics admit a controlled multi-scale expansion. Within the window, scalar diffusion, directional viscosity (NS), V1→R1 substrate-cutoff regularization, V5→Maxwell viscoelastic memory, and T17 minimal-coupling Lorentz force are all derived as leading-order coarse-grained consequences. The same machinery generalizes to non-Abelian gauge theory in Chapter 9 and produces the modified Poisson equation in Chapter 11.

DCGT also sets the substrate-level cross-bandwidth structure $\Gamma_\mathrm{cross}(\mathbf{x}) \sim \exp[-\alpha\int_\mathrm{path}\sigma\,d\ell]$ used throughout the program. This cross-bandwidth structure recurs in Black-Hole horizon formation (Chapter 13) and Quantum Computing condition-(ii) failure (Chapter 7) — the same DCGT structure at scales separated by ~50 orders of magnitude.

### What this chapter establishes

- The hydrodynamic-window scale separation $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$.
- The Diffusion Coarse-Graining Theorem (DCGT) as substrate-to-continuum bridge.
- The cross-bandwidth structure $\Gamma_\mathrm{cross} \sim \exp[-\alpha\sigma]$.
- The leading-order coarse-grained content reachable through DCGT: scalar diffusion, directional viscosity, V1 regularization, V5 memory, T17 minimal coupling.
- The framework's universal coarse-graining machinery used in every continuum derivation downstream.

### Dependencies

- Chapter 1 (primitives).
- Chapter 2 (load-bearing invariants, especially V1 kernel and gradient sparsity).

### Canonical sources

- Arc D memos in `theory/Arc_D/`
- NS Synthesis Paper Appendix D — `papers/Navier Stokes_Synthesis_Paper/`
- ED-QFT Unified Overview Paper — `papers/ED_QFT_Overview/`

\newpage

## Chapter 4 — Kernel-Level Arrow of Time: Theorem N1 + Theorem 18

Two foundational theorems together establish the substrate-level arrow of time. **Theorem N1** establishes the V1 vacuum response kernel as finite-width and chain-sourced. **Theorem 18** establishes that the V1 kernel is uniquely forced to have forward-cone-only support by the combination of P11 (commitment-irreversibility), P02 (chain worldlines), P04 (bandwidth update), P13 (proper-time ordering), and N1 itself. No symmetric, advanced, or hybrid kernel is constructible at the primitive level; the microscopic arrow of time is FORCED structurally rather than postulated.

Theorem 18's significance extends beyond its formal statement. It provides the substrate-level structural foundation for upper-half-plane analyticity in standard QFT (which is postulated rather than derived in conventional treatments). It strengthens N1-E directionality via cascade-from-V1 and R1-bypass redundancy (over-determined-forced). It refines T17 vacuum coupling to forward-only directionality. It supplies the kernel-level arrow that Phase-3 GR1 inherits in curved-spacetime extension. The standard time-symmetric correlator (Wightman) remains a distinct continuum-level object; Theorem 18 distinguishes response kernel from correlator and shows both are internally consistent.

The chapter clarifies why the kernel-level arrow is the *only* arrow of time the framework currently derives at the substrate level. The thermodynamic arrow, the cosmological arrow, the measurement arrow, and the radiation arrow are downstream structural follow-ons (out of scope for Theorem 18) that would inherit Theorem 18 as their kernel-level foundation.

### What this chapter establishes

- Theorem N1: V1 finite-width vacuum kernel as substrate temporal-smearing structure.
- Theorem 18: V1 kernel retardation as primitive-level structural consequence; symmetric, advanced, and hybrid kernels non-constructible at primitive level.
- The forcing chain: V1 as response kernel → chain forward-only along proper time → forward-cone-only support.
- Cross-arc strengthening of N1-E directionality (over-determined-forced).
- The CR (continuum-approximation) framing distinguishing primitive-level retarded V1 from continuum-level Wightman correlator.

### Dependencies

- Chapter 1 (primitives, especially P11, P02, P04, P13).
- Chapter 2 (V1 kernel as load-bearing invariant).
- Chapter 3 (DCGT as the continuum-approximation bridge).

### Canonical sources

- `papers/Time_Arrow_Theorem_18/`
- Theorem N1 paper (in V1 vacuum kernel inventory)
- `arcs/arc-B/` (Arc B closure memos)

\newpage

# Part II — Quantum Sector

Part II derives quantum mechanics, form-level quantum field theory, and quantum computation as substrate consequences of the foundations developed in Part I. The four QM postulates are derived rather than postulated (Chapter 5); the form-level structure of QFT including gauge invariance and UV-finiteness is derived (Chapter 6); the substrate-level architecture of quantum computation is established with the Unresolved-Regime Characterization Theorem and the multiplicity-cap function (Chapter 7).

## Chapter 5 — Phase-1 Closure of Quantum Mechanics: T1–T16

Phase-1 of the Event Density program closes the four postulates of quantum mechanics as derived theorems. Sixteen forced theorems (T1–T16) collectively establish that the Born rule (T-Born), the Schrödinger equation (T-Schrödinger), the Heisenberg uncertainty principle (T-Uncertainty), and the no-collapse measurement rule (T-Measurement) all emerge from substrate primitives plus standard mathematical theorems (Gleason 1957 for Born; Stone 1932 for Schrödinger).

The substrate-level structure: the Born rule's squared form follows from substrate non-contextuality plus bandwidth conservation across orthogonal decompositions, with Gleason's theorem providing the mathematical bridge. The Schrödinger equation's existence, uniqueness, linearity, first-order-in-time character, and Hamiltonian content all follow from substrate time-translation symmetry plus Stone's theorem. The Heisenberg lower bound on joint position-momentum precision follows from finite-bandwidth substrate constraints with the substrate origin of $\hbar/2$. The measurement rule emerges directly from P11 commitment-irreversibility — no separate collapse postulate is required.

Phase-1 closure means: all four QM postulates, plus extensions covering spin-statistics, the Dirac equation including the $g=2$ electron magnetic moment, canonical commutation relations, and the structural account of measurement, are derived from substrate primitives. The chapter establishes Phase-1 as the program's foundational closure of the quantum-mechanical sector and the basis on which Chapters 6 and 7 build.

### What this chapter establishes

- T1–T16 as the sixteen forced theorems closing the four QM postulates.
- The Born rule's squared form as substrate non-contextuality + Gleason 1957.
- The Schrödinger equation as substrate time-translation symmetry + Stone 1932.
- The Heisenberg uncertainty principle as a substrate finite-bandwidth consequence.
- The measurement rule as substrate-level commitment via P11 (no separate collapse postulate).
- Extensions: spin-statistics, Dirac equation, $g=2$, canonical commutation relations.

### Dependencies

- Chapter 1 (primitives, especially P11, P04).
- Chapter 2 (load-bearing invariants).
- Chapter 4 (kernel-level arrow as foundation for measurement-irreversibility).

### Canonical sources

- `papers/Phase_1/`
- `papers/QM_Emergence_Structural_Completion/`
- `papers/Born_Gleason/`
- `papers/U1_Participation_Measure/`, `papers/U2_Inner_Product/`, `papers/U3_Time_Translation_Schrodinger/`, `papers/U4_Hamiltonian_Form/`, `papers/U5_Translation_Momentum/`

\newpage

## Chapter 6 — Form-Level QFT and Quantum Information: T17, UV-Finiteness, ED-I-13

Theorem 17 (Gauge-Field-as-Rule-Type) establishes gauge fields as participation measures of structural rule-types in the substrate, rather than as fundamental dynamical fields. The theorem covers Abelian (U(1) electromagnetism) and non-Abelian (general compact-simple-group) gauge structures. It does *not* derive which specific gauge group nature realizes — the Standard Model gauge group remains empirical input — but it derives the *form* of gauge invariance and the structural role of gauge fields as interface properties of rule-types.

The chapter also establishes substrate-level UV-finiteness from event-discreteness (P01), finite proper-time intervals (P13), and bounded-bandwidth (P04). Standard QFT's renormalization machinery survives as a continuum-approximation tool but is not load-bearing at the substrate level. Together T17 and UV-finiteness constitute form-level closure of QFT structural content.

ED-I-13 (Quantum Information: Channel Geometry) reinterprets the five landmark quantum-information results — Deutsch (1985/92), Deutsch-Jozsa (1992), BB84 (1984), teleportation (Bennett et al., 1993), Shor (1994/96) — as five different manipulations of substrate channel geometry. Quantum information becomes the geometry of ED-channels: multiplicity supports global access; minimal channels enforce rewrite-on-measurement; unresolved participation rules enable identity reassignment; high-multiplicity channels carry global periodicity natively. The chapter closes the form-level account of quantum information and sets up Chapter 7's quantum-computing architecture.

### What this chapter establishes

- T17 (Gauge-Field-as-Rule-Type): gauge fields as participation measures of structural rule-types.
- T17's coverage of Abelian and non-Abelian gauge structures.
- Substrate-level UV-finiteness from P01 + P13 + P04.
- The reframing of renormalization as a continuum-approximation tool, not a substrate requirement.
- ED-I-13's reinterpretation of five landmark QI results as channel-geometry manipulations.
- The substrate-level vocabulary for quantum information (multiplicity, channel, identity alignment, global participation).

### Dependencies

- Chapter 1 (primitives, especially P01, P04, P13).
- Chapter 2 (load-bearing invariants).
- Chapter 4 (kernel-level arrow).
- Chapter 5 (Phase-1 closure as the substrate-quantum starting point).

### Canonical sources

- `papers/Gauge_Fields_Theorem_17/`
- ED-I-13 (Quantum Information: Channel Geometry, Feb 2026)
- `papers/Arc_Q/`
- `papers/Arc_R/`

\newpage

## Chapter 7 — Quantum Computation: UR-1, the Multiplicity-Cap Function $M$, Architectural Taxonomy

Quantum computation, in ED, is the deliberate engineered occupation of a low-multiplicity unresolved-rule substrate regime. The **Unresolved-Regime Characterization Theorem (UR-1)** identifies three independently-necessary substrate conditions for the regime: (i) bounded multiplicity, (ii) sustained cross-endpoint connectivity, (iii) bounded commitment-injection. The QC operating window is given structurally by $\tau_\mathrm{QC} = \min(\tau_{(\mathrm{i})}, \tau_{(\mathrm{ii})}, \tau_{(\mathrm{iii})})$ over the three corresponding failure timescales.

Three architectural classes — **engineered-low-multiplicity (A)**, **global-geometric-rigidity (B)**, **high-multiplicity-redundancy (C)** — exhaust the substrate-allowed strategies for protecting the regime. Standard meta-architectural techniques (error correction, dynamical decoupling, reservoir engineering, hybrid composition) are derived as compositions or extensions of the three classes, not new strategies. The **multiplicity-cap function $M$** unifies the classes as projections of one substrate object.

The chapter's strongest result is cross-platform unification: the matter-wave quantum-classical boundary at 140–250 kDa and the qubit-system multiplicity walls are the same substrate-determined boundary projected onto two different platforms via shared substrate constants. Sharp predictions follow: superconducting platforms hit a hard scaling ceiling without composition with logical-qubit encoding; topological qubits can outrun this ceiling exponentially in the topological gap; redundancy-based architectures saturate at a substrate-determined correlation budget.

### What this chapter establishes

- UR-1 (Unresolved-Regime Characterization Theorem) as the gate-condition theorem for quantum computation.
- The functional form of unresolvedness $\mathcal{U}$: three-factor product (multiplicity headroom × rule-spanning connectivity × commitment-survival exponential).
- The QC operating window $\tau_\mathrm{QC} = \min(\tau_{(\mathrm{i})}, \tau_{(\mathrm{ii})}, \tau_{(\mathrm{iii})})$.
- The three-class architectural taxonomy (A/B/C) and its substrate-level exhaustiveness.
- Meta-architectures (error correction, dynamical decoupling, reservoir engineering, hybrids) as compositions or techniques, not new classes.
- The multiplicity-cap function $M$ as one substrate object with three projections.
- Cross-platform unification: matter-wave Q-C boundary ↔ qubit-system multiplicity walls.

### Dependencies

- Chapter 1 (primitives).
- Chapter 2 (load-bearing invariants — multiplicity, gradient sparsity, cross-bandwidth, V1, P11).
- Chapter 3 (DCGT for cross-bandwidth structure).
- Chapter 5 (Phase-1 closure).
- Chapter 6 (T17 and channel-geometry quantum information).

### Canonical sources

- `papers/Quantum_Computing_Foundations/`
- Arc Q-COMPUTE memos in `theory/Quantum_Computing/`
- ED-I-23 (Josephson Junctions), ED-I-14 (Topological Effects), ED-I-18 (Multi-Timescale Photonics), ED-I-12 (Photonics)

\newpage

# Part III — Continuum and Dynamics

Part III handles the classical field-theoretic and fluid-dynamical continuum sectors. Each chapter derives a continuum theory through DCGT (Chapter 3) plus T17 minimal coupling (Chapter 6) where applicable, distinguishing form-FORCED substrate-derived content from continuum-imposed constraints and frame-kinematic artifacts.

## Chapter 8 — Navier–Stokes Architectural Foundations: Form-FORCED, R1, Path C

The Navier–Stokes equation is structurally a hybrid: viscous diffusion is substrate-derived (via DCGT scalar→vector extension); the substrate-cutoff hyperviscous term R1 is form-FORCED from V1 finite-width kernel; advection is a frame-kinematic artifact of laboratory-frame coordinates rather than a substrate force; pressure and incompressibility are continuum-imposed constraints. Two of the four kinds of structure in NS are substrate-grounded; one is frame-kinematic; one is continuum-imposed.

The R1 term $-\kappa\mu_\mathrm{V1}\ell_P^2 \nabla^4\mathbf{v}$ supplies a real Clay-NS-relevant regularizing mechanism. The framework gives an honest **Intermediate Path C** verdict on Clay-NS: the substrate-cutoff R1 mechanism produces strict monotone decay of the gradient-norm Lyapunov in any version of the equation that drops the advective term, but the advective vortex-stretching term — the unique non-sign-definite contribution to the Lyapunov balance — sits in the frame-kinematic sector that the substrate does not natively control. Three-angle convergence (architectural / dynamical / spectral) confirms advection-as-non-ED.

Chapter 8 also handles the dimensional-forcing question: 2D NS smoothness and the open status of 3D NS smoothness both fall out of the dimensional structure (vortex-stretching identically vanishes in 2D; in 3D the obstruction is real). Turbulence is identified as the dynamical signature of the non-substrate-derived advective sector; no substrate-level canonical turbulence template is forthcoming because the substrate doesn't generate turbulence.

### What this chapter establishes

- The four-fold architectural decomposition of Navier–Stokes: viscous diffusion (form-FORCED), R1 substrate-cutoff (form-FORCED), advection (frame-kinematic), pressure + incompressibility (continuum-imposed).
- R1 as form-FORCED substrate-cutoff regularization from V1 finite-width kernel.
- The Intermediate Path C verdict on Clay-NS: real regularizing mechanism + structural identification of obstruction.
- The dimensional-structure account: 2D smoothness (vortex-stretching vanishes), 3D obstruction (vortex-stretching from advection).
- Turbulence as the dynamical signature of the non-substrate-derived advective sector; no substrate canonical template.

### Dependencies

- Chapter 1 (primitives).
- Chapter 2 (V1 kernel).
- Chapter 3 (DCGT).

### Canonical sources

- `papers/Navier Stokes_Synthesis_Paper/` (main + Appendices C/D/E)
- ED-I-06 (Fields and Forces in Event Density, Feb 2026)

\newpage

## Chapter 9 — Magnetohydrodynamics and Yang–Mills: T17 Coupling, DCGT Continuum, Mass-Gap Mechanism

Magnetohydrodynamics extends Chapter 8 by adding T17 minimal coupling on charged-chain populations. The Lorentz force $\mathbf{F} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$ is derived from T17 minimal coupling at substrate level rather than postulated. Maxwell's equations follow from T17's gauge content. MHD's full content classifies into 6 canonical-ED forces (viscous, magnetic diffusion, Lorentz via T17, R1, $\partial_t\mathbf{B}$, $\nabla\cdot\mathbf{B}=0$), 2 continuum-imposed constraints (pressure, $\nabla\cdot\mathbf{v}=0$), and 3 transport-kinematic non-ED items (advection, induction kinematic, Ohm kinematic). MHD has strictly more canonical content on the EM side than pure NS but shares the same canonical/non-canonical boundary and the same transport-kinematic obstruction class.

Yang–Mills theory generalizes T17 minimal coupling to non-Abelian gauge groups. The continuum equation $D_\mu F^{\mu\nu} = J^\nu$ emerges directly from DCGT applied non-Abelianly to charged chains in compact-simple-group structures. A substrate-level **mass-gap mechanism** arises from the V1 finite-width vacuum kernel's second-moment expansion plus non-Abelian quartic stabilization; survival of the gap is conditional on kernel-profile rescaling under continuum-limit flow. The framework's verdict on the Clay Yang–Mills problem (existence + mass gap on $\mathbb{R}^4$) is structural-positive at the substrate-suggestive level — the same Path-C-style conditional-positive verdict as Clay-NS — with the Gribov-class gauge-fixing obstruction reframed via T17's substrate-level gauge-quotient identification but not constructively resolved.

### What this chapter establishes

- Magnetohydrodynamics: 11-content-item classification (6 canonical-ED / 2 continuum-imposed / 3 transport-kinematic non-ED).
- Lorentz force as T17 minimal coupling on charged chains, derived rather than postulated.
- Yang–Mills continuum equation $D_\mu F^{\mu\nu} = J^\nu$ from DCGT non-Abelian extension + T17 generalized minimal coupling.
- Substrate-level mass-gap mechanism from V1 second-moment + non-Abelian quartic stabilization.
- Conditional-positive structural-suggestive verdict on the Clay Yang–Mills problem.
- The kinematic-coupling-pattern boundary in continuum field theory: minimal-coupling-derived (canonical ED) vs transport-kinematic (non-ED).

### Dependencies

- Chapter 1 (primitives).
- Chapter 2 (load-bearing invariants).
- Chapter 3 (DCGT, generalized non-Abelianly).
- Chapter 6 (T17 minimal coupling).
- Chapter 8 (NS architectural decomposition as MHD's pure-fluid baseline).

### Canonical sources

- `papers/Navier Stokes_Synthesis_Paper/` Appendix C (MHD) + Appendix E (Yang–Mills)
- Arc YM memos in `theory/Yang_Mills/`
- `papers/Gauge_Fields_Theorem_17/`

\newpage

## Chapter 10 — Soft-Matter Mobility and Non-Newtonian Rheology: UDM, P4-NN, V5

The Universal Mobility Law (UDM) establishes that mobility in concentrated soft-matter systems takes the form $M(\rho) = M_0(1 - \rho/\rho_\mathrm{max})^\beta$ with $\beta$ near 2, derived from the substrate's mobility-capacity bound (P4). Empirical validation across ten chemically unrelated systems — colloidal suspensions, sugar-water, glycerol-water, multiple protein solutions, polymer-water mixes, casein micelles, silica — yields $\beta = 1.72 \pm 0.37$ with $R^2 > 0.986$ in every fit. The canonical ED value is $\beta = 2$; mechanism-clustered scatter (cooperative networks $\bar\beta \approx 2.31$, steric $\approx 1.76$, gradual/electrostatic $\approx 1.38$) tracks the predicted dependence on saturation cooperativity.

The P4-NonNewtonian extension (P4-NN) generalizes the same architectural principle from concentration-driven mobility to flow-state-variable mobility. Different applications of P4 to different state variables produce four of the five canonical non-Newtonian families: Krieger–Dougherty divergence (volume fraction), discontinuous shear-thickening (strain rate above critical), Cross-class shear-thinning (strain rate, monotone-decreasing), mixed regimes (non-monotone). The fifth family — Maxwell-class viscoelasticity (silly putty) — comes from V5 cross-chain memory, which under DCGT coarse-graining produces the standard $\tau_R \dot\sigma + \sigma = 2\mu S$ Maxwell equation with the relaxation time identified as V5's first temporal moment.

Five separately-modeled rheology families now share one architectural origin (P4 for four; V5 for the fifth). The exponent class $\beta \approx 2$ recurs across diffusion + suspension viscosity + shear-thickening because they share the same mobility-capacity bound applied to different state variables.

### What this chapter establishes

- Universal Mobility Law: $M(\rho) = M_0(1 - \rho/\rho_\mathrm{max})^\beta$, $\beta \approx 2$, derived from P4 mobility-capacity bound.
- Empirical validation across 10 chemically unrelated soft-matter systems with mechanism-clustered $\beta$ scatter.
- P4-NonNewtonian: same architectural principle applied to different state variables produces Krieger–Dougherty, DST, Cross-class shear-thinning, mixed regimes.
- Maxwell viscoelasticity from V5 cross-chain memory under DCGT coarse-graining.
- Five canonical non-Newtonian families unified under two structural commitments (P4 + V5).

### Dependencies

- Chapter 1 (primitives, especially P4 mobility-capacity bound).
- Chapter 2 (load-bearing invariants, V5 cross-chain memory).
- Chapter 3 (DCGT for V5→Maxwell coarse-graining).

### Canonical sources

- `papers/Universal_Mobility_Law/`
- `papers/P4_NonNewtonian_Paper_Draft/`

\newpage

# Part IV — Gravity and Cosmology

Part IV handles the gravitational sector. Substrate gravity at galactic scale is derived parameter-free from substrate primitives (Chapter 11); a covariant scalar-tensor extension produces curvature emergence at acoustic-metric class (Chapter 12); the architectural account of black holes follows from the same substrate machinery applied at the saturated-gradient regime (Chapter 13). The framework does not derive Einstein's general relativity; the acoustic-metric reading is kinematic, not full GR.

## Chapter 11 — Substrate Gravity at Galactic Scale: T19, T20, ECR, T21

Four results derive the entire flat-spacetime gravitational sector of galactic physics from substrate primitives without free parameters.

**Theorem T19** derives Newton's gravitational constant: $G = c^3\ell_P^2/\hbar$ from substrate cumulative-strain mechanism plus holographic participation-count bound. The substrate length scale is identified with the Planck length as a derived consequence of Newton-recovery, not a postulate.

**Theorem T20** derives the MOND transition acceleration: $a_0 = c\,H_0/(2\pi)$ from the cosmic horizon's dipole-projection contribution to a local accelerating object's substrate environment. The factor of $2\pi$ is structural (the azimuthal period of the leading anisotropic projection mode), not phenomenological. The numerical prediction matches the empirical MOND constant within approximately 10% parameter-free.

**The ED Combination Rule (ECR)** establishes how Newton-class and cosmic-horizon-class accelerations combine in the deep-galactic regime: $a = \sqrt{a_N \cdot a_0}$, the geometric mean of the two substrate strain scales. ECR is the substrate-derived multiplicative-participation rule replacing MOND's phenomenological interpolation function in the asymptotic regime.

**Theorem T21** derives the slope-4 baryonic Tully–Fisher relation: $v^4 = G \cdot M \cdot a_0$, with the proportionality constant $G\,a_0$ expressed entirely in fundamental substrate quantities. Flat rotation curves follow as a corollary of the math. T21 is robust under all admissible variations of the framework's substrate kernels and interpolation functions; the framework predicts zero intrinsic scatter in the asymptotic deep-MOND regime.

### What this chapter establishes

- T19: $G = c^3\ell_P^2/\hbar$ from substrate primitives.
- T20: $a_0 = c\,H_0/(2\pi)$ from cosmic-horizon dipole-projection, parameter-free, ~10% empirical match.
- ED Combination Rule: $a = \sqrt{a_N\,a_0}$ as substrate-derived deep-regime composition.
- T21: $v^4 = G\,M\,a_0$ slope-4 baryonic Tully–Fisher with prefactor in substrate quantities; zero intrinsic scatter in asymptotic deep-MOND regime.
- Flat rotation curves as corollary.

### Dependencies

- Chapter 1 (primitives).
- Chapter 2 (load-bearing invariants).
- Chapter 3 (DCGT consolidates substrate-gravity content under modified Poisson equation).

### Canonical sources

- `papers/Substrate_Gravity_Foundations/`
- `papers/Substrate_Gravity_Foundations/ED_substrate_gravity_foundations_2026-04-28.{md,tex,pdf}` (detailed-derivation companion)

\newpage

## Chapter 12 — Curvature Emergence: Arc ED-10, Acoustic-Metric Covariantization

The substrate-gravity content of Chapter 11 extends to a curvature-emergent regime via Arc ED-10, which produces a substrate-FORCED covariant generalization of the modified Poisson equation. The substrate cumulative-strain four-index object is identified as the load-bearing curvature degree of freedom; the acoustic-metric scalar-tensor covariantization takes the form

```math
\nabla_\mu\!\left[\mu\!\left(\frac{\sqrt{g^{\alpha\beta}\nabla_\alpha\Phi\,\nabla_\beta\Phi}}{a_0}\right)\nabla^\mu\Phi\right] = 4\pi G\,T,
```

with $g_{\mu\nu}$ the substrate-derived acoustic metric (a kinematic-summary of substrate participation density), $\mu(x)$ an interpolation function with the same asymptotic constraints as the flat-spacetime modified Poisson equation, and $T$ the trace of the matter stress-energy tensor.

The chapter is honest about scope. The covariant equation is structurally equivalent to the standard scalar-tensor MOND covariantization (RAQUAL-class) studied in the relativistic-MOND literature since Bekenstein-Milgrom 1984. The framework's specific contribution is identification of this form as substrate-FORCED rather than phenomenologically chosen. **The chapter explicitly does not derive Einstein's general relativity.** The acoustic metric is kinematic-class, not the dynamical metric of Einstein's theory. The covariant equation has known stability-class features (deep-MOND superluminal scalar propagation) inherited from the standard scalar-tensor MOND-covariantization literature; the framework identifies these as structurally inevitable consequences of producing the substrate-derived MOND behavior without introducing additional dynamical fields.

The verdict is conditional-positive at structural-suggestive level: the substrate-derivation produces a coherent, OS-positive, ghost-free, gradient-stable scalar-tensor framework that recovers all flat-spacetime substrate-gravity results (Chapter 11) in the weak-field limit, with deep-MOND superluminality as the only structural cost. Honest framing parallel to NS-Smoothness Path C and Yang–Mills Clay-relevance.

### What this chapter establishes

- Arc ED-10: substrate-FORCED scalar-tensor acoustic-metric covariantization of the modified Poisson equation.
- Acoustic metric $g_{\mu\nu}^\mathrm{ac}$ as kinematic-summary of substrate participation density (not dynamical-fundamental).
- Reduction to flat-spacetime substrate-gravity (Chapter 11) in the weak-field limit.
- Deep-MOND superluminal scalar propagation as structurally inherited consequence.
- Conditional-positive verdict at structural-suggestive level.
- Explicit non-derivation of Einstein's general relativity.

### Dependencies

- Chapter 11 (substrate gravity at galactic scale).
- Chapter 3 (DCGT).
- Chapters 1–2 (primitives, invariants).

### Canonical sources

- `papers/Substrate_Gravity_Foundations/` (curvature-emergence section)
- Arc ED-10 memos in `theory/Substrate_Gravity/`

\newpage

## Chapter 13 — Black-Hole Architecture: Arc BH, Horizons, Area Law, Phase-Shift Structure

Black-hole architecture in ED follows from a single substrate condition: $|\nabla\rho|\,\ell_P^2/\rho_\mathrm{local} \gtrsim \log(R_\mathrm{cg}/\ell_P)$. This condition supports six derivations across Arc BH.

**Horizon as decoupling surface (BH-2).** The substrate-level horizon is the surface where $\sigma$ crosses the threshold and $\Gamma_\mathrm{cross}$ falls below hydrodynamic-window resolution. Universal across BH / Rindler / cosmic / acoustic horizons. The four standardly-similar thermodynamic-style horizon classes share one substrate mechanism.

**Singularity replacement (BH-3).** Three substrate constraints (finite participation, discrete micro-events, gradient saturation) jointly forbid divergent curvature/energy/tidal/incompleteness. Singularities do not exist as physical objects; the acoustic-metric coarse-grained reading breaks down at $\sigma \gtrsim \beta_\mathrm{crit}$ while substrate dynamics remain finite. Replacement: finite-thickness saturated participation zone.

**Information and evaporation (BH-4).** Committed structure cannot cross the horizon (participation-bandwidth prohibition, not causal); entanglement straddles freely. Evaporation = pair-creation-class events at the saturated decoupling surface, with one leg committing inward (joining the saturated zone) and one outward (joining the radiation field), joint correlation preserved globally. The four assumptions generating the standard information paradox / firewall / complementarity puzzle are not imposed at substrate level — paradoxes do not arise.

**Area-law entropy (BH-5).** Form $S = (A/\ell_P^2)\log g$ derived from substrate participation-capacity at the decoupling surface. The Bekenstein-Hawking $1/4$ coefficient corresponds to $\log g \approx 1/4$ as INHERITED from substrate motif counting; closed-form derivation is downstream work.

**Wave-BH scattering (BH-6).** BHPT phase shift $\delta_{\ell m} = \int_\mathrm{path}\Delta\mathcal{A}\,d\lambda$ derived as global path-integrated invariant of minimal ED-channels. Helicity preservation/flip from anisotropy-basis transport (axisymmetric vs frame-dragging). Kerr twist from integrated frame-dragging vorticity.

**Verdict (BH-7).** Conditional-positive structural closure at the architectural level. Hawking-spectrum derivation is the next natural arc (B4) — the mechanism is in hand; the explicit V5 cross-chain correlation calculation that produces the spectrum is the remaining work.

### What this chapter establishes

- The single substrate condition unifying horizon formation, interior saturation, information blocking, participation-capacity saturation, and strong-curvature scattering.
- Universal horizon mechanism across BH / Rindler / cosmic / acoustic.
- No singularities; finite-thickness saturated participation zone replacement.
- Information / firewall / complementarity / singularity paradoxes not generated in framework.
- Area-law form derived; $1/4$ coefficient INHERITED.
- BHPT phase-shift structure derived as global path-integrated invariant.
- Conditional-positive structural closure at architectural level.

### Dependencies

- Chapter 1 (primitives, especially P11).
- Chapter 2 (load-bearing invariants — gradient sparsity, cross-bandwidth).
- Chapter 3 (DCGT).
- Chapter 12 (acoustic-metric scalar-tensor framework).

### Canonical sources

- `papers/Black_Hole_Foundations/`
- Arc BH memos in `theory/Black_Holes/`

\newpage

# Part V — Empirical Synthesis

Part V synthesizes the program's empirical posture across all closed sectors. Chapter 14 collects the cross-domain unifications — places where the same substrate mechanism produces different empirical phenomena at different scales — as a structural signature of the framework. Chapter 15 catalogs the public test inventory of falsifiable predictions and identifies the open extensions that future arcs will pursue.

## Chapter 14 — Cross-Platform Unifications: Matter-Wave ↔ Qubit, $\Gamma_\mathrm{cross}$ Collapse, Methodology

Three kinds of cross-platform unification recur across the program.

**Same-substrate-quantity at different platforms.** The matter-wave quantum-classical boundary at 140–250 kDa molecular mass and the qubit-system multiplicity walls of Class A architectures are the same substrate-determined boundary projected onto two different platforms via shared $\mathcal{M}_\mathrm{crit}$. Sharper measurement of one anchors the other. This is the strongest cross-platform identity in the program; it is testable at the form-FORCED level and falsifiable by inconsistent calibration between the two platforms.

**Same-substrate-mechanism at different scales.** $\Gamma_\mathrm{cross}$ collapse via DCGT-derived $\exp[-\alpha\sigma]$ is the same substrate mechanism for black-hole horizon formation (Chapter 13) and quantum-computing condition-(ii) failure (Chapter 7). Two faces of one substrate identity at scales separated by approximately fifty orders of magnitude in physical length. The substrate doesn't care whether the gradient-collapse occurs at a black-hole event horizon or at a Josephson-junction barrier — the same DCGT machinery describes both.

**Same-architectural-principle across content channels.** The mobility-capacity bound P4 produces both the Universal Mobility Law in soft-matter diffusion (Chapter 10) and the Class A engineered-low-multiplicity protection mechanism in quantum computing (Chapter 7). The V1 finite-width vacuum kernel (Chapter 4) underlies the kernel-level arrow of time, the substrate-cutoff regularization R1 in NS (Chapter 8), the mass-gap mechanism in Yang-Mills (Chapter 9), and the per-patch motif alphabet entering BH area-law entropy (Chapter 13). Each architectural commitment in the substrate produces consequences across multiple sectors.

The chapter also establishes the program's **form-FORCED / value-INHERITED methodology** as a cross-domain signature in its own right. Across every closed sector, the framework derives the form of empirical regularities and inherits specific numerical values from substrate constants. This methodological consistency is testable: closed-form derivation of any inherited substrate constant (e.g., $\mathcal{M}_\mathrm{crit}$ in QC, $\log g$ in BH, $\beta$ in soft matter) should produce mutually consistent values when projected to different sectors.

### What this chapter establishes

- Matter-wave ↔ qubit-system cross-platform identity via shared $\mathcal{M}_\mathrm{crit}$.
- $\Gamma_\mathrm{cross}$ collapse as one substrate mechanism unifying BH-2 horizon formation and QC condition-(ii) failure across ~50 orders of magnitude in length.
- P4 mobility-capacity bound unifying Universal Mobility Law (soft matter) and Class A engineered-low-multiplicity (QC).
- V1 finite-width kernel unifying T18 (kernel arrow), R1 (NS regularization), YM mass-gap, and BH area-law motif counting.
- Form-FORCED / value-INHERITED methodology as cross-domain testable signature.

### Dependencies

- All preceding chapters.

### Canonical sources

- `papers/ED_QFT_Overview/` (program-level synthesis)
- `papers/ED_One_Substrate_Three_Domains/` (program-overview, three-domains framing)
- Cross-references to all Foundations papers (SG, BH, QC) and the NS Synthesis Paper.

\newpage

## Chapter 15 — Public Test Inventory and Open Extensions

The framework's empirical content is collected as a public test inventory across the nine closed sectors. Each test is a falsifiable substrate-level prediction with explicit confirmation/refutation conditions. The status taxonomy is consistent across sectors: PASSED (empirical confirmation in published data), ANCHORED (prediction calibrated to existing observation), IN PROGRESS (active experimental program awaiting result), ACTIVE (test specified, awaiting execution), OPEN (prediction stated, technique requires development).

The chapter summarizes the major status assignments. **Passed:** dwarf galaxy outer-radius mass discrepancy (Active > Quiet) from Chapter 11; multi-timescale FPM relaxation (Hafezi 2025) from Chapter 7; Universal Mobility Law $\beta \approx 1.72$ across ten chemically unrelated systems from Chapter 10. **Anchored:** matter-wave Q-C boundary as multiplicity wall; Newton's $G$ from substrate; MOND $a_0$ within 10%; slope-4 Tully–Fisher; hyper-coherence in ultra-symmetric superconductors; Josephson MQT WKB structure recovered from DCGT; Krieger–Dougherty and DST; BH area-law form; BHPT phase-shift structure; universal horizon mechanism; high-Tc as intrinsically low-multiplicity; cross-domain $\Gamma_\mathrm{cross}$ collapse; form-FORCED / value-INHERITED methodology. **In progress:** SC-qubit system-multiplicity wall; FRAP $t^{1/6}$ scaling at high BSA; quantum error correction as Class A + Class C composition. **Active:** mass-matched isomer matter-wave test; cross-platform $\mathcal{M}_\mathrm{crit}$ calibration; Class C correlation-budget plateau; Bell correlation degradation with multiplicity; halo lag in cluster collisions; activity-dependent halo strength; post-starburst hysteresis; reduced small-scale substructure; mesoscopic transport threshold; SC phase-stiffness saturation; Casimir-gradient saturation; microresonator linewidth asymmetry; photonic-crystal ED-gradient limit; multi-timescale comb formation; ED-limited soliton step; chiral-phonon vorticity; orbital Seebeck. **Open:** Class B exponential coherence advantage (topological qubits); Hawking spectrum; no-singularity interior observation; ED-entrainment universality across rotating fields.

The chapter also names the program's open extensions — the natural follow-on arcs that future closed-arc work will address. **B4 Hawking spectrum** (next natural arc): mechanism in hand from Chapter 13; explicit V5 cross-chain correlation calculation remains. **Closed-form substrate constants program**: $\mathcal{M}_\mathrm{crit}$ (O-QC-1), $\log g$ (O2 from Arc BH), $\kappa/|\hat{N}'|$ (E4 from ED-SC). All three are structurally similar. **Architecture-to-platform calibration** (O-QC-2). **Topology-stability theorem** (O-QC-4). **Arc COSMO** (cosmic expansion / $H_0$ from substrate; speculative). **GR-4A** (Einstein-equation emergence; speculative). **Six O-QC items** carried forward from Arc Q-COMPUTE. **Three O items** (O1, O2, O3) carried forward from Arc BH.

### What this chapter establishes

- The public test inventory as the program's empirical-status reference.
- Status taxonomy consistent across sectors: PASSED / ANCHORED / IN PROGRESS / ACTIVE / OPEN.
- Three PASSED predictions, thirteen ANCHORED, three IN PROGRESS, seventeen ACTIVE, four OPEN.
- The named open-extension list: B4 (Hawking spectrum), closed-form substrate constants, architecture-to-platform calibration, topology-stability theorem, Arc COSMO, GR-4A, plus six O-QC and three O items.
- The map from open extensions to future architectural-level arcs.

### Dependencies

- All preceding chapters.

### Canonical sources

- `Desktop/ED_Public_Test_Inventory.md` (living test catalog)
- `docs/Investigation_Priority_List.md` (active priority list with open extensions)
- All Foundations papers and Synthesis papers for sector-specific predictions.

\newpage

# Appendix A — Theorem Provenance Map

The program's structural-foundation theorem inventory. For each theorem: a one-to-two-sentence statement of what it establishes, the dependency chain from substrate primitives, and the canonical source paper.

## T1–T16 — Phase-1 closure of QM postulates

**Statement.** Sixteen forced theorems collectively deriving the four QM postulates (Born rule, Schrödinger evolution, Heisenberg uncertainty, no-collapse measurement) from substrate primitives plus mathematical theorems (Gleason 1957, Stone 1932). The squared form of the Born rule, the linearity and first-order-in-time character of the Schrödinger equation, the $\hbar/2$ factor in Heisenberg's bound, and the irreversibility of measurement are all derived rather than postulated.

**Dependency chain.** Substrate primitives P01, P02, P04, P11, P13 → bandwidth conservation across orthogonal decompositions + substrate non-contextuality → Gleason → Born rule. Substrate time-translation symmetry → Stone → Schrödinger equation. Substrate finite-bandwidth → Heisenberg lower bound. P11 commitment-irreversibility → measurement rule.

**Canonical source.** `papers/Phase_1/`, `papers/QM_Emergence_Structural_Completion/`, `papers/Born_Gleason/`.

## T17 — Gauge-Field-as-Rule-Type

**Statement.** Gauge fields are participation measures of structural rule-types in the substrate. Gauge invariance is the interface property of label-carrying participation rules; gauge fields' specific structural role (mediating interactions between labeled events) emerges from coarse-graining. Covers Abelian and non-Abelian compact-simple-group gauge structures.

**Dependency chain.** Substrate primitives + label-carrying rule-type structure + DCGT coarse-graining → gauge field as interface property + gauge invariance as interface symmetry.

**Canonical source.** `papers/Gauge_Fields_Theorem_17/`.

## T18 — V1 Kernel Retardation (Kernel-Level Arrow of Time)

**Statement.** The V1 vacuum response kernel is uniquely forced at the primitive level to have support restricted to the forward causal cone. No symmetric, advanced, or hybrid kernel is constructible at primitive level. The microscopic arrow of time is FORCED structurally rather than postulated.

**Dependency chain.** P01 + P02 + P04 + P11 + P13 + Theorem N1 (V1 finite-width vacuum kernel) + Q.8 effective-vacuum factorization → V1 retarded.

**Canonical source.** `papers/Time_Arrow_Theorem_18/`.

## T19 — Newton's Gravitational Constant from Substrate

**Statement.** $G = c^3\ell_P^2/\hbar$. Newton's gravitational constant derived from substrate cumulative-strain mechanism plus holographic participation-count bound. The substrate length scale is identified with the Planck length as a derived consequence of Newton-recovery.

**Dependency chain.** Substrate cumulative-strain mechanism + holographic participation-count bound on a sphere of radius $R$ + substrate-level equipartition → inverse-square form + proportionality constant fixed.

**Canonical source.** `papers/Substrate_Gravity_Foundations/` (T19 derivation).

## T20 — MOND Transition Acceleration from Cosmic-Horizon Dipole

**Statement.** $a_0 = c\,H_0/(2\pi)$. The MOND transition acceleration derived from the cosmic horizon's dipole-projection contribution to a local accelerating object's substrate environment. The factor of $2\pi$ is the azimuthal period of the leading anisotropic projection mode; numerical match to empirics is within ~10% parameter-free.

**Dependency chain.** Cosmic-horizon participation density + accelerating chain's anisotropic environment + dipole projection along acceleration axis + azimuthal period $2\pi$ → $a_0$.

**Canonical source.** `papers/Substrate_Gravity_Foundations/` (T20 derivation).

## ECR — ED Combination Rule

**Statement.** $a = \sqrt{a_N \cdot a_0}$. Newton-class and cosmic-horizon-class accelerations combine multiplicatively (geometric mean) in the deep-galactic regime. The substrate-derived multiplicative-participation rule replacing MOND's phenomenological interpolation function in the asymptotic regime.

**Dependency chain.** T19 + T20 + substrate logarithmic stability landscape → cross-term $\sqrt{G\,M\,a_0}\,\log(R/R_0)$ → geometric-mean composition.

**Canonical source.** `papers/Substrate_Gravity_Foundations/` (ECR derivation).

## T21 — Slope-4 Baryonic Tully–Fisher Relation

**Statement.** $v^4 = G\,M\,a_0$. The slope-4 baryonic Tully–Fisher relation derived from substrate primitives with proportionality constant in fundamental quantities. Zero intrinsic scatter predicted in asymptotic deep-MOND regime; observed scatter dominated by mass-measurement uncertainty.

**Dependency chain.** T19 + T20 + ECR + circular-orbit centripetal balance → $v^4 = G\,M\,a_0$.

**Canonical source.** `papers/Substrate_Gravity_Foundations/` (T21 derivation).

## N1 — V1 Finite-Width Vacuum Kernel

**Statement.** The V1 vacuum response kernel is finite-width and chain-sourced. Establishes the substrate-level temporal-smearing structure mediating participation events.

**Dependency chain.** Substrate primitives → effective-vacuum response + finite-width temporal kernel.

**Canonical source.** Theorem N1 paper (V1 kernel inventory).

## GR1 — V1 Curved-Spacetime Extension (Phase-3)

**Statement.** The V1 vacuum kernel extends to curved spacetime via Hadamard-parametrix causal-future restriction with Synge world function. Inherits Theorem 18's forward-cone-only support; preserves P11 time orientation along curved geodesics.

**Dependency chain.** N1 + T18 + Hadamard parametrix + Synge world function on curved background → curved-spacetime V1 retarded.

**Canonical source.** Phase-3 GR1 derivation.

## DCGT — Diffusion Coarse-Graining Theorem

**Statement.** The substrate-to-continuum bridge for canonical-ED dynamical content. Within the hydrodynamic-window scale separation $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$, substrate dynamics admit a multi-scale expansion to coarse-grained continuum equations covering scalar diffusion, directional viscosity, V1→R1 substrate-cutoff regularization, V5→Maxwell viscoelastic memory, and T17 minimal-coupling Lorentz force.

**Dependency chain.** Substrate primitives + hydrodynamic-window scale separation + multi-scale expansion → cross-bandwidth $\Gamma_\mathrm{cross} \sim \exp[-\alpha\sigma]$ + leading-order continuum content.

**Canonical source.** Arc D memos in `theory/Arc_D/`; NS Synthesis Paper Appendix D.

## UR-1 — Unresolved-Regime Characterization Theorem

**Statement.** Three independently-necessary substrate conditions for the unresolved-rule regime that quantum computation requires: (i) bounded multiplicity, (ii) sustained cross-endpoint connectivity, (iii) bounded commitment-injection. The unresolvedness $\mathcal{U}$ is a three-factor product (multiplicity headroom × rule-spanning connectivity × commitment-survival exponential); the QC operating window is $\tau_\mathrm{QC} = \min(\tau_{(\mathrm{i})}, \tau_{(\mathrm{ii})}, \tau_{(\mathrm{iii})})$.

**Dependency chain.** Substrate primitives (especially P11) + DCGT + V1 + multiplicity-as-entropy → three-factor product form of $\mathcal{U}$ → three independent conditions.

**Canonical source.** `papers/Quantum_Computing_Foundations/`; Arc Q-COMPUTE Memo 2.

\newpage

# Appendix B — Notation Glossary

Symbols used throughout the monograph. One-line definitions; canonical definitions live in the source papers.

**Substrate quantities and primitives**

- $\rho$ — local participation density
- $\nabla\rho$ — participation density gradient
- $\sigma = |\nabla\rho|\,\ell_P^2/\rho_\mathrm{local}$ — substrate-scale gradient sparsity (dimensionless)
- $\Gamma_\mathrm{cross}$ — substrate-mediated cross-bandwidth between adjacent regions
- $\mathcal{M}$ — multiplicity (count of viable distinct ED-gradient pathways; ED analogue of entropy)
- $\mathcal{U}(\mathcal{S},t) \in [0,1]$ — participation-rule unresolvedness across designated endpoints
- $\Lambda$ — local commitment-injection rate ($\Lambda_\mathrm{env} + \Lambda_\mathrm{int}$)
- V1, V5 — finite-width vacuum kernel and cross-chain memory kernel
- P1–P13 — the thirteen substrate primitives (including P01 event discreteness, P02 chain structure, P04 bandwidth update, P11 commitment-irreversibility, P13 proper-time ordering)
- R1 — substrate-cutoff hyperviscous regularization term ($-\kappa\mu_\mathrm{V1}\ell_P^2 \nabla^4\mathbf{v}$)

**Length and time scales**

- $\ell_P$ — Planck length (substrate length scale, derived to be Planck length via T19)
- $R_\mathrm{cg}$ — coarse-graining length scale
- $L_\mathrm{flow}$ — continuum-flow length scale
- $\tau_\mathrm{QC}$ — QC operating window
- $\tau_{(\mathrm{i})}, \tau_{(\mathrm{ii})}, \tau_{(\mathrm{iii})}$ — UR-1 condition-failure timescales

**Substrate constants and coupling parameters**

- $\hbar$ — Planck's constant (substrate input)
- $c$ — speed of light (substrate input)
- $H_0$ — Hubble rate (substrate input)
- $G$ — gravitational constant (derived: $c^3\ell_P^2/\hbar$)
- $a_0$ — MOND transition acceleration (derived: $c\,H_0/(2\pi)$)
- $\alpha$ — DCGT prefactor in cross-bandwidth structure
- $\beta$ — mobility exponent in Universal Mobility Law (canonical 2; empirical $\approx 1.72 \pm 0.37$)

**UR-1 thresholds (INHERITED)**

- $\mathcal{M}_\mathrm{crit}$ — critical multiplicity threshold
- $\Gamma_\mathrm{min}$ — minimum cross-bandwidth for hydrodynamic-window resolution
- $\Lambda_\mathrm{V1}$ — V1 vacuum residual injection rate (Class A perfect-isolation ceiling)
- $\beta_\mathrm{crit} \sim \log(R_\mathrm{cg}/\ell_P)$ — critical gradient threshold for decoupling-surface formation
- $N_\mathrm{corr}$ — correlation budget (Class C saturation)
- $\Delta_\mathrm{top}$ — topological gap (Class B)
- $T_\mathrm{eff}$ — substrate-equivalent perturbation temperature

**UR-1 functional shapes (form-FORCED, shape INHERITED)**

- $\mu(x)$ — multiplicity-headroom factor (monotone-decreasing from 1 to 0)
- $\kappa(x)$ — rule-spanning connectivity factor (monotone-increasing from 0 to 1)
- $g(N), h(N), c(N)$ — Class C redundancy modifier functions

**Multiplicity-cap function and architectural classes**

- $M(\mathcal{S}, K, \mathcal{E}, \mathcal{O})$ — multiplicity-cap function (one substrate object with three architectural-class projections)
- $K \in \{A, B, C\}$ — architectural class (engineered-low-multiplicity / global-geometric-rigidity / high-multiplicity-redundancy)
- $\mathcal{O}$ — meta-architectural overlay (error correction, dynamical decoupling, reservoir engineering, hybrid composition)
- $\mathcal{S}$ — substrate-region system input
- $\mathcal{E}$ — environment input
- $\mathcal{M}_\mathrm{floor}, \gamma_\mathrm{floor}$ — architecturally-imposed multiplicity and connectivity floors
- $A_S$ — architectural restoring rate
- $f_\mathrm{int}, f_\mathrm{xy}, f_\mathrm{sys}^{(A)}$ — architecture-specific scaling functions

**Substrate-gravity quantities**

- $\Phi$ — gravitational potential (substrate-derived)
- $\mu(|\nabla\Phi|/a_0)$ — interpolation function in modified Poisson equation
- $g_{\mu\nu}^\mathrm{ac}$ — acoustic metric (kinematic-summary of participation density; not Einstein metric)
- $T$ — trace of matter stress-energy tensor (in covariantization)
- $v_\mathrm{flat}$ — asymptotic flat-rotation-curve speed
- $M_b$ — baryonic mass

**Black-hole quantities**

- $\Sigma_H$ — decoupling surface (substrate-level horizon)
- $A$ — coarse-grained acoustic-metric area of $\Sigma_H$
- $S$ — black-hole entropy (form: $A/\ell_P^2 \cdot \log g$)
- $\log g$ — entropy coefficient (INHERITED; $\approx 1/4$ corresponds to BH match)
- $\delta_{\ell m}$ — BHPT phase shift (global path-integrated invariant)
- $\Delta\mathcal{A}$ — channel action density excess along trajectory
- $\Delta\phi_\mathrm{twist}$ — Kerr-twist accumulated frame-dragging vorticity
- $\omega_\mathrm{FD}$ — local frame-dragging angular velocity
- $\mathcal{T}$ — topological structure label
- $T_H$ — Hawking temperature ($\kappa/(2\pi)$, where $\kappa$ is surface gravity)
- $\tau_\mathrm{gap-stab}(\mathcal{T})$ — Class B topology-perturbation rate

**Soft-matter mobility**

- $M(\rho)$ — mobility (Universal Mobility Law)
- $\rho_\mathrm{max}$ — packing limit
- $\tau_R$ — Maxwell viscoelastic relaxation time (V5 first temporal moment)

\newpage

# Appendix C — Paper-to-Chapter Cross-Reference

Every publication-grade ED paper assigned to exactly one chapter. Repository paths relative to `event-density/`.

**Chapter 1 — The Substrate Ontology (P1–P13)**

- `papers/Event_Density_Ontology_and_Axioms/`
- `papers/Foundations_of_Event_Density/`
- `papers/ED_One_Substrate_Three_Domains/` (program-overview / orientation context)

**Chapter 2 — Load-Bearing Invariants**

- ED-I-01 (Superconductivity) — multiplicity-as-entropy reading
- ED-I-23 (Josephson Junctions) — multiplicity at engineered low-$\mathcal{M}$ regions
- ED-I-29 (Tunneling) — sparse-$\sigma$ regions and global rule reconfiguration
- ED-I-06 (Fields and Forces in Event Density) — ontological roof providing field/force vocabulary

**Chapter 3 — The Coarse-Graining Bridge (DCGT)**

- `papers/Navier Stokes_Synthesis_Paper/` Appendix D (DCGT)
- Arc D memos in `theory/Arc_D/`
- `papers/ED_QFT_Overview/` (program-level synthesis with DCGT central)

**Chapter 4 — Kernel-Level Arrow of Time (N1 + T18)**

- `papers/Time_Arrow_Theorem_18/`
- N1 derivation paper (V1 finite-width kernel)
- `arcs/arc-B/` Arc B closure memos

**Chapter 5 — Phase-1 Closure of QM (T1–T16)**

- `papers/Phase_1/`
- `papers/QM_Emergence_Structural_Completion/`
- `papers/Born_Gleason/`
- `papers/U1_Participation_Measure/`
- `papers/U2_Inner_Product/`
- `papers/U3_Time_Translation_Schrodinger/`
- `papers/U4_Hamiltonian_Form/`
- `papers/U5_Translation_Momentum/`

**Chapter 6 — Form-Level QFT and Quantum Information (T17, UV-FIN, ED-I-13)**

- `papers/Gauge_Fields_Theorem_17/`
- ED-I-13 (Quantum Information: Channel Geometry)
- `papers/Arc_Q/`
- `papers/Arc_R/`

**Chapter 7 — Quantum Computation (UR-1, $M$, A/B/C)**

- `papers/Quantum_Computing_Foundations/`
- Arc Q-COMPUTE memos in `theory/Quantum_Computing/`
- ED-I-14 (Topological Effects)
- ED-I-18 (Multi-Timescale Photonics)
- ED-I-12 (Photonics)

**Chapter 8 — Navier–Stokes Architectural Foundations**

- `papers/Navier Stokes_Synthesis_Paper/` (main + Appendix C)
- Arc NS memos in `theory/Navier Stokes/`
- ED-I-06 (Fields and Forces) — ontological roof for NS classification

**Chapter 9 — Magnetohydrodynamics and Yang–Mills**

- `papers/Navier Stokes_Synthesis_Paper/` Appendix C (MHD)
- `papers/Navier Stokes_Synthesis_Paper/` Appendix E (Yang–Mills)
- Arc YM memos in `theory/Yang_Mills/`

**Chapter 10 — Soft-Matter Mobility and Non-Newtonian Rheology**

- `papers/Universal_Mobility_Law/`
- `papers/P4_NonNewtonian_Paper_Draft/`

**Chapter 11 — Substrate Gravity at Galactic Scale (T19, T20, ECR, T21)**

- `papers/Substrate_Gravity_Foundations/Substrate_Gravity_Foundations_Paper.{md,tex,pdf}`
- `papers/Substrate_Gravity_Foundations/ED_substrate_gravity_foundations_2026-04-28.{md,tex,pdf}` (detailed-derivation companion)

**Chapter 12 — Curvature Emergence (Arc ED-10)**

- `papers/Substrate_Gravity_Foundations/` (curvature-emergence section in extended-scope paper)
- Arc ED-10 memos in `theory/Substrate_Gravity/`

**Chapter 13 — Black-Hole Architecture (Arc BH)**

- `papers/Black_Hole_Foundations/`
- Arc BH memos in `theory/Black_Holes/` (BH-1 through BH-7)

**Chapter 14 — Cross-Platform Unifications and Methodology**

- `papers/ED_QFT_Overview/` (program-level synthesis)
- `papers/ED_One_Substrate_Three_Domains/`

**Chapter 15 — Public Test Inventory and Open Extensions**

- `Desktop/ED_Public_Test_Inventory.md` (living test catalog)
- `docs/Investigation_Priority_List.md` (active priority list with open extensions)
- Various ED-I interpretation papers as sector-specific prediction sources

\newpage

# Appendix D — Substrate Constants and Inherited Values

Every substrate constant referenced in the monograph. One-line description and canonical source.

**Substrate inputs (taken as given)**

- $\hbar$ — Planck's constant. Substrate input in T19 derivation.
- $c$ — speed of light. Substrate input in T19, T20.
- $H_0$ — Hubble rate. Substrate input in T20; Hubble-tension band 67–73 km/s/Mpc translates to ~15% prediction band on $a_0$.
- $\ell_P$ — Planck length / substrate length scale. Identified with substrate length scale via T19 Newton-recovery (derived, not postulated).

**Derived substrate constants (form-FORCED, value follows from inputs)**

- $G = c^3\ell_P^2/\hbar$ — Newton's gravitational constant. Derived in T19. (`Chapter 11`)
- $a_0 = c\,H_0/(2\pi) \approx 1.08 \times 10^{-10}$ m/s² — MOND transition acceleration. Derived in T20; matches empirical $\approx 1.2 \times 10^{-10}$ m/s² within ~10%. (`Chapter 11`)

**INHERITED substrate constants (form-FORCED in role; specific value calibrated empirically or downstream)**

- $\mathcal{M}_\mathrm{crit}$ — critical multiplicity threshold. Anchored empirically by matter-wave Q-C boundary at 140–250 kDa molecular mass. Closed-form derivation is open (O-QC-1). (`Chapter 7`, `Chapter 14`)
- $\Gamma_\mathrm{min}$ — minimum cross-bandwidth for hydrodynamic-window resolution. INHERITED from V1-kernel + DCGT closed-form details. (`Chapters 3, 7`)
- $\Lambda_\mathrm{V1}$ — V1 vacuum residual injection rate. INHERITED; bounds Class A perfect-isolation ceiling. (`Chapter 7`)
- $\beta_\mathrm{crit} \sim \log(R_\mathrm{cg}/\ell_P)$ — critical gradient threshold for decoupling-surface formation. Substrate-determined dimensionless number; precise prefactor depends on coarse-graining choices. (`Chapters 7, 13`)
- $N_\mathrm{corr}$ — correlation budget for Class C platforms. INHERITED from substrate-coupling pattern across redundant pathways; platform-specific. (`Chapter 7`)
- $\Delta_\mathrm{top}^{\max}$ — maximum stable topological gap for Class B platforms. INHERITED from material/topology engineering. (`Chapter 7`)
- $T_\mathrm{eff}^{\min}$ — minimum substrate-equivalent perturbation temperature. INHERITED from environmental engineering. (`Chapter 7`)
- $\log g$ — black-hole area-law entropy coefficient. INHERITED from substrate motif counting; matches Bekenstein-Hawking $1/4$ at $\log g \approx 1/4$ (i.e., $g \approx 1.28$, non-integer). Closed-form derivation is open (O2 from Arc BH). (`Chapter 13`)
- $\beta$ — mobility exponent in Universal Mobility Law. Canonical ED value $\beta = 2$; empirical $\beta = 1.72 \pm 0.37$ across 10 systems with mechanism-clustered scatter. (`Chapter 10`)
- $\kappa/|\hat{N}'| \approx 0.001766$ — ED-SC anchor (cross-scale invariance). INHERITED; closed-form derivation is open (E4). (Cross-reference: ED-SC arc work, not within this monograph's nine sectors but flagged for completeness.)

**Class-specific INHERITED quantities**

- $\mu(x), \kappa(x)$ — UR-1 functional shapes. Form-FORCED to be monotone with specific limits; specific shape (Boltzmann, rational, sigmoid, etc.) INHERITED from V1-kernel + DCGT closed-form details. (`Chapter 7`)
- $g(N), h(N), c(N)$ — Class C redundancy modifier functions. Form-FORCED; specific shapes INHERITED. (`Chapter 7`)
- $f_\mathrm{int}(M_\mathrm{mol}), f_\mathrm{xy}(N_\mathrm{qubits}), f_\mathrm{sys}^{(A)}(\mathcal{S})$ — architecture-specific scaling functions mapping system size to effective multiplicity. INHERITED from architecture-to-platform calibration (O-QC-2). (`Chapters 7, 14`)
- $\tau_\mathrm{gap-stab}(\mathcal{T})$ — Class B topology-perturbation rate. Form named; topology-stability theorem (O-QC-4) is the natural follow-on for substrate-level derivation. (`Chapter 7`)

**Note on the closed-form-substrate-constants program.** Three INHERITED constants — $\mathcal{M}_\mathrm{crit}$ (Chapter 7 / O-QC-1), $\log g$ (Chapter 13 / O2), and $\kappa/|\hat{N}'|$ (ED-SC arc / E4) — are structurally similar and form the program's closed-form-substrate-constants program. Each calibrates a substrate constant from empirical anchors; closed-form derivation in any one constrains the others by the form-FORCED / value-INHERITED methodology's cross-domain consistency requirement.

\newpage

# Closing Note

This shell is the first draft of a monograph that the program is large enough to need. Fifteen chapters, five Parts, four appendices. ~250–350 pages typeset when chapters are progressively expanded from structural summaries into full integrated derivations.

The shell exists to make the program navigable today. Any reader can use it to enter the program at any chapter, follow the dependency graph to earlier chapters as needed, and reach the canonical source paper for any result through the cross-reference table. The shell stays valid as the canonical entry point even if no chapter is ever expanded; chapters that do get expanded progressively replace their summaries in place without changing the dependency structure.

The methodological commitment is preserved across every chapter: form-FORCED at the structural level, value-INHERITED at the numerical level, with empirical anchors and downstream-theorem programs explicitly named. The framework's empirical posture is mixed by design — predictions sharp enough to be falsified, specific numerical thresholds calibrated rather than computed in closed form. The shell honors this distinction and makes it visible across nine sectors of substrate-level architectural closure.

Future work proceeds along three parallel tracks. The **closed-form substrate-constants program** (O-QC-1, O2 from Arc BH, E4 from ED-SC) attacks the INHERITED-constant boundary from below, deriving values currently anchored to empirical observation. The **next-arc program** opens new structural fronts (B4 Hawking spectrum as the immediate next concrete arc; Arc COSMO and GR-4A as long-horizon speculative arcs). The **chapter-expansion program** progressively replaces each shell summary with the full integrated treatment — a progression of multiple sessions per chapter, paced by which sector's derivation is most actively being clarified.

The shell completes the program's current internal organization. The program's external posture — the public test inventory, the architectural-foundation papers (SG, BH, QC), the ED-QFT Unified Overview, the Universal Mobility Law and P4-NonNewtonian papers, and the public explainers — remains the program's interface to readers who do not need the monograph's depth. The shell is the spine connecting them.

— Allen Proxmire, May 2026
