# Event Density

## A Generative Substrate Ontology for Cross-Scale Physics

**Whitepaper — Program Overview, Architecture, and Falsification Path**

*Wave-3 generative document. Public-facing, non-technical orientation layer. Standalone, citable, repo-top-level document.*

---

## Executive Summary

**Event Density (ED)** is a research program that asks a single foundational question: *can the diverse phenomena of physics — quantum mechanics, gauge theory, gravity, black holes, turbulence, decoherence, entanglement — be generated from a small, well-specified substrate ontology?*

The program's answer is conditional: **yes, given thirteen posited primitives and a kernel calculus built from two substrate-level memory kernels**. The thirteen primitives are listed in a position paper and form a minimal generative ontology. The two kernels — designated V1 (a finite-width retarded kernel) and V5 (a finite-memory cross-chain correlation kernel) — supply the dynamical content from which physical structure is derived.

What ED claims is *cross-domain reach plus methodological consistency*. Across eight closed research arcs (quantum kinematics, form-level quantum field theory, gravity, black holes, quantum computing limits, entanglement, soft matter / Navier–Stokes, foundational kernel theory), ED produces results that are **form-forced** by the primitives and an honestly-disclosed set of paper-specific postulates. Numerical values are inherited from empirical matching rather than derived from first principles. This split — *form forced, values inherited* — is the program's methodological signature.

The program's most ambitious recent result is the **Substrate–Cosmology Boundary Unification (SCBU)** synthesis and its six-paper extension arc, the **ED-SC 4.x series**. SCBU identifies the black-hole horizon, the cosmic decoupling surface, the deep-MOND galactic asymptote, the quantum-computing platform-coherence threshold, the soft-matter hydrodynamic Q-factor, and the substrate-scale fixed-point parameter as *six projections of a single substrate–cosmology boundary onto distinct parameter axes*. ED-SC 4.x integrates these projections into a unified four-regime cross-scale model (ultraviolet / transition / infrared / cosmological).

The program is **falsifiable**. Each result carries explicit falsification criteria, and the SCBU framework predicts synchronized co-variation of six observable quantities under Hubble-tension-class shifts of $H_0$ — a sharp observational test.

This whitepaper is the front door. It explains what ED is, what it claims, what it does not claim, and how to navigate the 100+ research papers that constitute the program (the numbered Paper_NNN series plus theorem-stub additions T19–T21, the cross-arc synthesis Paper_SCBU, and the six-paper ED-SC 4.x extension arc).

---

## §1 — Motivation

Physics, considered as a single intellectual artifact, is a patchwork. Quantum mechanics and general relativity remain unreconciled in their foundations. Standard-model gauge theory works at one scale; cosmological dynamics works at another. The black-hole information paradox lives in a third register; turbulence and condensed-matter rheology in a fourth. Each domain has its own framework, its own postulates, and its own community.

A generative substrate ontology proposes an alternative architecture: *rather than treating each domain as autonomous, derive each domain's structural content from a common substrate*. The substrate is posited, not derived. From the substrate, dynamical kernels are built. From the kernels, coarse-grained continuum theories emerge. From the continuum theories, specific physical predictions follow.

The motivation for ED is not that the patchwork is wrong — each domain's predictions are excellent within their regimes — but that the patchwork hides **cross-domain structure**. If a single substrate object can produce the black-hole horizon, the cosmic decoupling surface, the substrate-scale fixed-point, the deep-MOND galactic acceleration, the matter-wave quantum-classical boundary, *and* the Navier–Stokes Q-factor as six projections of one boundary, that cross-domain structure is itself a physical fact worth identifying.

ED's role is to make this cross-domain structure explicit, falsifiable, and structurally honest. The program does not replace standard physics operationally; it supplements it with a substrate-level account of why the standard results take the forms they do.

---

## §2 — The 13 Primitives

ED's substrate is specified by thirteen primitives. They are posited — not derived from anything deeper — and they are intended to be minimal: removing any one of them would block at least one downstream structural derivation in the corpus.

The thirteen primitives, in plain language:

**P01 — Chains.** The substrate's irreducible objects. Chains are the carriers of substrate-level content; everything else is built from chains, their relations, and the rule-types acting on them.

**P02 — Participation.** The substrate-level relation between chains. Participation supplies the "state content" that downstream coarse-graining elevates to Hilbert-space states, density fields, etc.

**P03 — Channel and locus indexing; spatial homogeneity.** Substrate-level spatial structure. The substrate is indexed by channel and locus, and is homogeneous (no preferred location).

**P04 — Bandwidth.** A non-negative additive scalar attached to each substrate cell. P04 supplies the "budget" structure that propagates upward into participation counts, entropy bounds, and saturation phenomena.

**P05 — Polarity-transport along edges.** The substrate carries polarity (a $U(1)$-valued internal variable, per P09) along its edges. Polarity-transport is the substrate-level origin of phase, gauge connection, and parallel-transport phenomena.

**P06 — Spatial dimension $D = 3+1$.** The substrate's spacetime dimensionality is posited as 3+1, consistent with multiple independent derivations elsewhere in the corpus (PDE-uniqueness axioms, spinor-bundle structure, acoustic-metric signature).

**P07 — Channel structure.** Channel structure is an ontological primitive at the substrate level — not a derived feature.

**P08 — Substrate scale $\ell_{\mathrm{ED}}$.** The substrate has a characteristic length scale, identified phenomenologically with the Planck length. P08 supplies the substrate-side anchor for Newton's $G = c^3 \ell_P^2 / \hbar$.

**P09 — $U(1)$-valued polarity.** The substrate's polarity content is $U(1)$-valued, supplying the angular / phase structure that propagates to gauge fields and quantum phase.

**P10 — Rule-type primitive.** Substrate dynamics are carried by *rule-types* — discrete, distinguishable, composable objects. The V1 and V5 kernels (see §3) are rule-types.

**P11 — Commitment-irreversibility.** Substrate commitments, once made, are irreversible. P11 supplies the directional content of time, the retardation property of the V1 kernel, the second-law-like structure of substrate entropy, and the arrow of forward causality.

**P12 — Stability landscape.** Substrate configurations have stability content (cumulative strain), supplying the substrate-level analog of energy-landscape phenomena and the substrate origin of the gravitational potential $\Phi$.

**P13 — Time homogeneity.** The substrate's temporal-translation symmetry. P13 supplies $H_0$ as a cosmological-rate parameter and underwrites the rate-of-becoming postulate.

A fourteenth slot, **P14**, is reserved as a placeholder for bilocal strain coupling but is not currently in the canonical 13. Whether P14 should be elevated, or whether its content can be derived from the existing 13, is structurally open.

The thirteen primitives are **the** ontological commitment of the ED program. Every result in the corpus rests on them.

---

## §3 — Kernel Calculus (V1 / V5)

ED's substrate dynamics are carried by two substrate kernel rule-types (in the sense of P10). Both are finite — neither requires infinite-resolution data — and both are forward-causal under P11.

**V1 — Finite-width retarded vacuum kernel.** V1 propagates substrate amplitudes from prior to later times with a characteristic width $\ell_{V1} \sim \ell_P$ and a retardation property forced by P11. V1 supplies:

- The substrate-level propagator entering quantum field theory.
- The UV regulator at the Planck scale (preventing trans-Planckian divergences).
- The kinematic viscosity scale entering hydrodynamics ($\nu \sim \ell_{V1}^2 / \tau_{V1}$).
- The friction coefficient entering the Universal Mobility Law.
- The propagation rate identified as substrate $c$ (constant under coarse-graining).

**V5 — Cross-chain finite-memory correlation kernel.** V5 supplies cross-chain correlations with finite bandwidth $\ell_{V5}$ and finite memory $\tau_{V5}$. V5 carries the cross-chain content that V1 (within-chain) does not. V5 supplies:

- Maxwell-form stress-relaxation in viscoelastic materials ($\tau_M \sim \tau_{V5}$).
- The substrate origin of bipartite entanglement budget partitioning (monogamy).
- The cross-chain bandwidth that caps Q-Compute multiplicity.
- The decoupling-surface mechanism at black-hole horizons ($\Gamma_{\mathrm{cross}} \to 0$).
- The Page-curve mechanism for Hawking radiation entanglement.
- The cutoff $\omega_c = c/\ell_P$ resolving the trans-Planckian problem.

The two kernels together form a **kernel calculus**: a small, complete set of substrate-level objects from which coarse-grained continuum theories emerge under the Diffusion Coarse-Graining Theorem (DCGT).

**Why only two kernels?** A central structural claim of ED is that V1 + V5 are sufficient. Higher-order kernels are admissible in principle but, across all closed research arcs, V1 and V5 suffice. The same V5 object plays roles in soft-matter viscoelasticity, black-hole horizon physics, Hawking-radiation cutoff, entanglement-bandwidth modulation, and Q-Compute platform-coherence saturation — six distinct domains, one substrate primitive, no contradiction.

This cross-domain universality of V5 is the program's most striking pattern. The whitepaper returns to it in §7 (SCBU) and §8 (ED-SC 4.x).

---

## §4 — The ED Architecture

The ED program has a four-layer architecture:

**Layer 1 — Substrate primitives (P01–P13).** Posited ontology. The thirteen primitives.

**Layer 2 — Kernel calculus (V1 / V5).** Substrate dynamics. The two kernels, classified by characteristic scale, retardation order, and cross-chain rank.

**Layer 3 — Domain arcs.** Closed research arcs deriving specific physical structures from primitives + kernels + paper-specific postulates. Each arc is structurally coherent within itself and integrated with the substrate.

**Layer 4 — Cross-scale synthesis.** The Scale Correspondence (SC) program and SCBU unification, integrating multiple arcs into a unified cross-scale invariance model.

Conceptually:

```
                  ┌─────────────────────────────────┐
                  │  Layer 1: 13 Primitives (P01–P13) │
                  └───────────────┬─────────────────┘
                                  │
                  ┌───────────────▼─────────────────┐
                  │  Layer 2: Kernel Calculus (V1, V5) │
                  └───────────────┬─────────────────┘
                                  │
        ┌────────────────────┬────┴────┬──────────────────┐
        │                    │         │                  │
   ┌────▼────┐         ┌─────▼───┐  ┌──▼────┐      ┌──────▼──────┐
   │ QM Arc  │         │ QFT Arc │  │ Gravity│ ...   │  Soft Matter │
   │  Phase-1│         │ T17/T18 │  │ Arc    │      │  / NS-MHD   │
   └────┬────┘         └────┬────┘  └──┬────┘      └──────┬──────┘
        │                   │           │                   │
        └─────────┬─────────┴─────┬─────┴─────────┬─────────┘
                  │               │               │
                  ▼               ▼               ▼
            ┌─────────────────────────────────────────┐
            │   Layer 4: Cross-Scale Synthesis (SC, SCBU) │
            └─────────────────────────────────────────┘
```

The architecture is **bottom-up**: every result in Layers 3 and 4 traces back through the kernel calculus to the substrate primitives. The architecture is also **falsifiable at each layer**: refutation of a primitive falsifies downstream results; refutation of a kernel-level claim falsifies dependent arc results; refutation of an arc result limits but does not destroy the substrate.

This layered falsifiability is the program's structural integrity.

---

## §5 — The Domain Arcs

The ED corpus is organized into eight closed research arcs. Each arc:

- States its substrate-level inputs explicitly.
- Identifies its paper-specific postulates (declared, not derived).
- Derives or composes its structural content.
- Distinguishes form-forced content from value-inherited content.
- Provides explicit falsification criteria.

The eight arcs:

**Quantum Kinematics (Papers 001–012).** The Phase-1 program. Sixteen theorems closing the four standard quantum-mechanical postulates as substrate-derived results. Born rule, tensor-product structure, projective measurement, unitary evolution: all derived from substrate primitives. Berry phase, Aharonov–Bohm phase, Bloch theorem, local rate of becoming.

**Quantum Field Theory (Papers 013–024).** Form-level QFT scaffolding. T17 identifies gauge fields as connections on rule-type bundles. T18 establishes the kernel-level arrow of time. The Yang–Mills arc (YM-1 through YM-6) supplies substrate-level non-abelian gauge theory, OS-positivity audit, and mass-gap mechanism. Verdict: structural-positive on Clay-relevance.

**Gravity (Papers 025–038).** Substrate-level derivations of Newton's law ($G = c^3 \ell_P^2 / \hbar$), the transition acceleration $a_0 = c H_0 / (2\pi)$, the ED Combination Rule $a = \sqrt{a_N a_0}$, and the BTFR slope-4 relation $v^4 = G M a_0$. Arc ED-10 extends to scalar-tensor acoustic-metric covariantization. Substrate gravity explains galactic dynamics without dark matter.

**Black Holes (Papers 039–052).** The Arc Hawking program. Horizon as decoupling surface ($\Gamma_{\mathrm{cross}} \to 0$). Hawking spectrum at $T_H = \kappa/(2\pi)$ via substrate-Unruh / KMS. Trans-Planckian problem resolved by V5 cutoff at $\omega_c = c/\ell_P$. Planck-mass remnant ($M_\star = c_\star \ell_P$) as forced endpoint (Scenario C). Information paradox not generated at substrate level. Important framing: Planck-mass remnants are **not** a dark-matter candidate — galactic dynamics are explained by substrate gravity, not remnants.

**Q-Compute (Papers 053–062).** The substrate origin of quantum-computing limits. The multiplicity-cap function $\mathcal{M}_{\mathrm{cap}}$ as one substrate object with three projections (Class A engineered-low-multiplicity, Class B global-geometric-rigidity, Class C high-multiplicity-redundancy). Cross-platform unification via critical multiplicity $\mathcal{M}_{\mathrm{crit}}$: matter-wave quantum-classical boundary (140–250 kDa) and qubit-array walls are the same substrate phenomenon. Decoherence-centric → multiplicity-centric reframing.

**Entanglement (Papers 063–072).** Bipartite entanglement architecture substrate-derived. Tensor product, Schmidt decomposition, monogamy (via V5 cross-chain bandwidth), no-signaling (over-determined by three substrate locks), von Neumann entropy via Shannon–Khinchin axioms at substrate level, Bell–Tsirelson polytope. Interpretive capstone: entanglement is the unresolved regime of participation-rule individuation.

**Soft Matter / Navier–Stokes (Papers 073–086).** The substrate-level NS / MHD program. NS-1 dimensional forcing to $D = 3+1$. NS-2 substrate→continuum coarse-graining. NS-Smoothness at Intermediate Path C verdict. NS-MHD H1/H2/H3 closure. Krieger–Dougherty + Maxwell viscoelastic. Canonical NS-Q operating point with $Q \approx 3.5$. Universal Mobility Law. Vortex-stretching obstruction at substrate level.

**Wedges / Kernel Theory (Papers 087–101).** Foundational substrate-level theorems. The 13-primitive position paper (Paper 087). V1 and V5 canonical references. Memory-kernel cascade across scales. Kernel hierarchy unification. T18 kernel-level arrow of time. Forward-causal primitive structure. Form-FORCED / value-INHERITED methodology formalized. Cross-scale invariance (ED-SC 3.x). Three-regime renormalization-group / 0.6 problem. NS synthesis. Five-sector program overview. Falsification register.

Each arc is a complete research program in its own right. Each composes with the others through the substrate primitives and the kernel calculus.

---

## §6 — Scale Correspondence (SC) Program

The Scale Correspondence (SC) program is ED's account of how substrate-level structure manifests at the scales accessible to physical experiment.

**Why SC is needed.** The substrate operates at the Planck scale ($\ell_P \sim 10^{-35}$ m). Physical experiments operate at scales from atomic to cosmological. The gap is sixty-plus orders of magnitude. For ED's substrate to make contact with physics, a *scale correspondence* between substrate content and experimentally-accessible content must be identified.

**SC versus Wedges/RG.** The Wedges arc (Papers 087–097) establishes the substrate's renormalization-group structure: three regimes (ultraviolet / transition / infrared) with characteristic 0.6 transition exponent, cross-scale invariance at the canonical operating point $\xi_{\mathrm{canonical}}$, and the kernel cascade across scales. This is the **internal substrate-side** structure of cross-scale relations.

The SC program is the **external** counterpart: how does substrate-level structure project onto physically-observable scales? Where do the experimental signatures live? Why does $a_0$ have the value it has? Why does the matter-wave quantum-classical boundary sit at 140–250 kDa?

**Role of SCBU.** The Substrate–Cosmology Boundary Unification supplies the central anchor for the SC program. By identifying the substrate-cosmology boundary as a single shared object whose multiple projections supply the canonical scales of physics, SCBU provides the substrate-level *reason* why specific empirical scales exist where they do.

---

## §7 — SCBU: Substrate–Cosmology Boundary Unification

**What SCBU claims.** The substrate-cosmology boundary — the substrate-level structure at the cosmological scale $R_H = c / H_0$ where V5 cross-chain bandwidth saturates — is a single object. Multiple physical quantities at different domains are projections of this single object onto different parameter axes.

The six major projections identified in the corpus (counting Paper_ED_SC_4.1's two parameter-axis arms — $r_H$ at local-gravitational mass and $R_H$ at global cosmological rate — as two separate projections):

| Projection | Parameter axis | Substrate identity |
|---|---|---|
| Black-hole horizon $r_H = 2GM/c^2$ | local gravitational mass $M$ | cosmological-regime, local-grav arm |
| Cosmic decoupling $R_H = c/H_0$ | global cosmological rate $H_0$ | cosmological-regime, global arm |
| Substrate fixed-point $\xi_{\mathrm{canonical}}$ | substrate-scale fixed-point | spans IR-to-cosmological |
| Deep-MOND acceleration $a_0 = c H_0/(2\pi)$ | local galactic acceleration | IR-galactic projection |
| Q-Compute threshold $\mathcal{M}_{\mathrm{crit}}$ | multiplicity-budget | IR-platform projection |
| NS-Q canonical $Q \approx 3.5$ | hydrodynamic Q-factor | IR-hydrodynamic projection |

The cosmological regime (regime 4) carries two arms; the IR regime (regime 3) hosts three sub-projection manifestations. Together these form the canonical six-projection view of the unified four-regime SCBU model (per Paper_ED_SC_4.6).

**Why SCBU matters.** Each of these quantities was, prior to SCBU, an independent feature: $a_0$ derived in the gravity arc, $\mathcal{M}_{\mathrm{crit}}$ in the Q-Compute arc, $Q$ in the soft-matter arc. They share a striking common feature: each is anchored to the cosmological rate $H_0$ through the substrate-cosmology boundary, even though each lives in a domain (galactic dynamics / quantum-computing / hydrodynamics) that has no operational connection to cosmology.

SCBU explains why. The substrate-cosmology boundary is a single substrate object; the apparent independence of these quantities is an artifact of viewing them through their domain-specific parameter axes. From the substrate's perspective, they are the *same* boundary observed via different projection mechanisms.

This is the most far-reaching structural claim in the ED program: **one substrate, one boundary, six projections**.

---

## §8 — The ED-SC 4.x Arc

The ED-SC 4.x arc is a six-paper extension that formalizes the SCBU framework's six projections and integrates them into a unified four-regime cross-scale model.

**Paper ED-SC 4.1 — BH ↔ cosmic boundary projection.** Establishes that the black-hole horizon $r_H$ and the cosmic decoupling surface $R_H$ are two arms of one substrate-cosmology boundary, parameterized by local mass $M$ and global cosmological rate $H_0$ respectively. Two distinct projection mechanisms are identified: the BH-horizon arm uses a cross-scale fixed-point + Schwarzschild matching, while the cosmic decoupling arm uses Paper_028's substrate-causality / decoupling-surface argument (kernel-propagation-rate / Hubble-expansion-rate crossover). Both arms share the substrate-cosmology boundary anchor but employ different projection mechanisms.

**Paper ED-SC 4.2 — Substrate-derivation attempt of $\xi_{\mathrm{canonical}}(H_0)$.** The highest-leverage paper. Attempts a first-principles substrate derivation of the canonical operating point as a function of $H_0$. *The derivation does not close.* The structural setup is established — $\xi_{\mathrm{canonical}}$ is a fixed point of substrate renormalization-group flow on the interval $[\ell_P, R_H]$ — but three substrate-derived inputs are missing (designated Routes A, B, C). The honest outcome: structural framework supplied, numerical closure open. Closing Route A — a substrate-derived relation $\ell_{V5}(H_0)$ between V5 bandwidth and the cosmological rate — is identified as the highest-impact open derivation in the ED program.

**Paper ED-SC 4.3 — MOND/galactic IR projection.** Establishes the deep-MOND acceleration scale $a_0 = c H_0/(2\pi)$ as the galactic-acceleration sub-projection of the substrate-cosmology boundary, with the factor $1/(2\pi)$ arising from Paper_029's azimuthal-Fourier-mode normalization on the residual SO(2) symmetry of an accelerating chain. This is a **distinct** projection mechanism from $R_H$'s substrate-causality argument (4.1) — $a_0$ and $R_H$ share the boundary anchor but use different mechanisms onto different parameter axes. BTFR slope-4 emerges as the infrared-regime scaling law at the boundary.

**Paper ED-SC 4.4 — Q-Compute ↔ SCBU IR projection.** Establishes $\mathcal{M}_{\mathrm{crit}}$ and the Class A/B/C saturation structure as the multiplicity-budget projection of the boundary. The three architectural classes correspond to which of the three substrate constituents ($N_{\mathrm{bw}}, N_{\mathrm{V5}}, N_{\mathrm{commit}}$) saturates first as the boundary is approached. Cross-platform universality (matter-wave at 140–250 kDa, qubit-array walls) inherits from the substrate's structural invariance.

**Paper ED-SC 4.5 — Soft-matter NS-Q IR projection.** Establishes $Q \approx 3.5$ at the canonical NS-Q operating point as the hydrodynamic-Q projection of the boundary. V5's appearance as the Maxwell relaxation timescale ($\tau_M \sim \tau_{V5}$) shares the substrate object that saturates at the boundary. The Universal Mobility Law inherits from the same substrate kernel hierarchy.

**Paper ED-SC 4.6 — Unified four-regime model (capstone).** Integrates all five prior extensions. The substrate-cosmology boundary induces a unified four-regime renormalization-group structure: ultraviolet (V1-dominated), transition (V1↔V5 cascade with 0.6 exponent), infrared (V5-modulated, multi-sector projection regime), cosmological (V5-saturated boundary). All six SCBU projections occupy distinct, predictable positions within this structure.

**What the arc accomplished.** The ED-SC 4.x arc completes ED's cross-scale synthesis. The substrate-cosmology boundary's structure is now mapped across domains; the regime classification is portable; and the framework supplies multiple testable predictions (see §9). One open derivation — Route A — would simultaneously upgrade the entire arc's verdict structure, producing the first cross-arc *fully derived* result in the corpus.

---

## §9 — Falsification Program

ED is a falsifiable program. Each closed result carries explicit falsification criteria, and the program-level synthesis carries cross-arc tests.

**Observational falsifiers (corpus-wide):**

- *Direct detection of substrate $c$ variation.* P-RB-1 (Paper 012) commits to substrate $c$ being constant. Detection of fundamental-constant drift in $c$ that cannot be accounted for as a dressed-object coarse-graining effect refutes the framework.
- *Empirical failure of BTFR slope-4* (Paper 031). Substrate gravity predicts the Baryonic Tully–Fisher Relation with slope exactly 4 and zero intrinsic scatter in the deep-MOND asymptotic.
- *Empirical detection of complete black-hole evaporation* (Paper 041). Substrate dynamics force a Planck-mass remnant endpoint. Complete evaporation refutes the V5-cutoff mechanism.
- *Empirical detection of intrinsic scatter in BTFR beyond observational error.* Refutes Paper 031 and propagates upward.

**Structural falsifiers:**

- *Discovery of a fourth Q-Compute architectural class beyond A/B/C* (Paper 055). Refutes the three-constituent exhaustiveness of $\mathcal{M}_{\mathrm{cap}}$.
- *Demonstration that V5 admits trans-Planckian modes.* Refutes Paper 040's resolution of the trans-Planckian problem.
- *Substrate-level evidence that any of the 13 primitives is inconsistent or derivable from another.* Refutes the minimality claim.
- *Discovery of substrate-level structure below $\ell_P$.* Refutes the substrate-interior cutoff (Paper 042).

**Cross-arc falsifiers (the SCBU framework's signature tests):**

- *Hubble-tension-class predictions.* SCBU predicts synchronized co-variation of six quantities under $H_0$ shifts: $\xi_{\mathrm{canonical}}$, $a_0$, $\mathcal{M}_{\mathrm{crit}}$, $Q$, $r_H/R_H$ scales, and the substrate-cosmology boundary anchor itself. If $H_0$ is observed to differ between the early universe and the local universe (the Hubble tension), SCBU predicts that the cosmological-anchored quantities should co-vary in synchrony with $H_0$. Empirical detection of asynchrony — e.g., $a_0$ co-varying with $H_0$ but $\mathcal{M}_{\mathrm{crit}}$ remaining constant — refutes the SCBU-projection identification for the asynchronous quantity.
- *Multi-axis consistency.* Systems parameterizable by multiple SCBU-projection axes (e.g., a high-mass-fluid molecular system at galactic-disc accelerations) should exhibit consistent predictions across all relevant axes.
- *Cross-platform universality.* Different platforms probing the same SCBU projection should yield substrate-mapped agreement. Different platforms probing $\mathcal{M}_{\mathrm{crit}}$ (matter-wave vs qubit-array) must map to the same substrate threshold.

These tests are sharp. They do not require new physics to perform — they require careful observation of existing measurable quantities under cosmologically-varied conditions. The Hubble tension, if it persists, is itself a candidate testing ground.

---

## §10 — How to Read the ED Corpus

The full corpus comprises 100+ research papers (101 numbered + theorem-stub and synthesis additions). A complete reading is not necessary for orientation. The following **core papers** form a coherent introductory path:

**Foundational (read first):**

1. **Paper 087** — The 13 primitives (position paper). Sets the substrate ontology.
2. **Paper 089** — V1 finite-width retarded kernel (canonical reference). The first kernel.
3. **Paper 090** — V5 cross-chain correlation kernel. The second kernel.
4. **Paper 073** — Diffusion Coarse-Graining Theorem (DCGT). The substrate-to-continuum bridge.
5. **Paper 095** — Form-FORCED / value-INHERITED methodology. The corpus's methodological discipline formalized.

**One paper per major arc (read in any order):**

6. **Paper 002** — Born–Gleason rule (quantum kinematics anchor).
7. **Paper 027** — Newton's $G = c^3 \ell_P^2 / \hbar$ (gravity arc anchor).
8. **Paper 047** — Hawking spectrum via substrate-Unruh (black-hole arc anchor).
9. **Paper 060** — Matter-wave / qubit unification via $\mathcal{M}_{\mathrm{crit}}$ (Q-Compute anchor).
10. **Paper 076** — NS-2 substrate→continuum (soft-matter / NS anchor).

**Synthesis (read after core):**

11. **Paper 098** — ED-QFT Unified Overview. Program synthesis covering five sectors.
12. **Paper 100** — Five-Sector Program Overview. The 100-paper milestone capstone.
13. **Paper SCBU** — Substrate–Cosmology Boundary Unification.
14. **Paper ED-SC 4.6** — Unified four-regime model (ED-SC 4.x arc capstone).

**Navigation strategy:**

- Each paper begins with a **Preamble** listing what the paper does *not* claim. Read these first when sampling.
- Each paper has a **§2.5 Load-Bearing Step Audit Table** that lists every step in the derivation with its discipline-label (postulate / inherited / derived / position-claim). The audit table is the paper's structural skeleton.
- Each paper closes with explicit **Falsification Criteria** and a **Position Statement**.
- Cross-references are dense but the corpus is structured to allow targeted reading: enter at an arc anchor, follow citations to dependencies, exit when the dependency chain becomes shallow.

The corpus rewards focused reading. A physicist coming from quantum mechanics can profitably read the quantum-kinematics arc + the entanglement arc + the form-level QFT arc without touching gravity. A cosmologist can read the gravity arc + the BH arc + the SCBU synthesis. A condensed-matter physicist can read the soft-matter arc + the Q-Compute arc without touching cosmology.

---

## §11 — Future Work

Several open lines of work would significantly advance the program:

**Route A closure (highest priority).** A substrate-level derivation of $\ell_{V5}(H_0)$ — the relation between V5 bandwidth and the cosmological rate — would simultaneously upgrade the verdict of all six ED-SC 4.x extension papers from form-forced-only to fully-derived, producing the first cross-arc completely-derived result in the corpus. The substrate-cosmology coupling parameter is the load-bearing missing link.

**Routes B and C (alternative closure paths).** Substrate-derived $\beta(K)$ functional form (Route B) and substrate-derived $K_{\mathrm{boundary}}$ at $R_H$ (Route C) supply alternative paths to the same closure. Either or both, combined, would also upgrade the arc.

**Hawking ↔ cosmological-redshift extension.** A natural next ED-SC 4.x extension paper: substrate-Unruh KMS structure at the SCBU boundary should connect Hawking temperature to cosmological redshift via the same boundary-projection mechanism that connects $a_0$ and $\mathcal{M}_{\mathrm{crit}}$. This would add a seventh SCBU projection on the Hawking-temperature parameter axis.

**Remnant ↔ cosmological-relic-abundance extension.** Paper 049 introduces the Planck-mass remnant relic abundance under standard FRW dilution. An explicit SCBU framing would tighten the structural anchoring of remnants to the substrate-cosmology boundary.

**Entanglement V5-saturation ↔ SCBU.** Paper 071 establishes an ER=EPR-class structural echo between V5 in the entanglement arc and V5 in the BH arc. An explicit SCBU framing would integrate the entanglement arc into the cross-scale synthesis.

**Yang–Mills ↔ SCBU.** The deepest open connection. Yang–Mills mass-gap mechanism (Paper 021) and OS-positivity audit (Paper 020) both invoke V5 at substrate level. An explicit SCBU framing would integrate the YM arc into the unified four-regime model, conjecturally as a tenth projection.

**Phase-3 GR Einstein equation emergence.** The deepest open question. Substrate-level Newton's law (Paper 027), $a_0$ (Paper 029), and BTFR slope-4 (Paper 031) are derived. The full general-relativity Einstein equation is not. Whether a substrate-level emergence of the Einstein equation is possible — and at what verdict level — remains genuinely open.

**Empirical program.** Observational programs targeting the SCBU synchronized co-variation prediction under Hubble tension; precision galactic-rotation-curve measurements of BTFR scatter; matter-wave decoherence experiments at the 140–250 kDa boundary; substrate-cutoff signatures in Hawking-radiation analog systems.

---

## §12 — Summary

Event Density (ED) is a generative substrate ontology for cross-scale physics built on:

- **One substrate** — the thirteen primitives.
- **Two kernels** — V1 (finite-width retarded) and V5 (cross-chain finite-memory).
- **Eight closed research arcs** spanning quantum mechanics, gauge theory, gravity, black holes, quantum computing limits, entanglement, soft matter, and foundational kernel theory.
- **One boundary** — the substrate-cosmology boundary at $R_H = c/H_0$.
- **Six projections** of that boundary onto distinct parameter axes (black-hole horizon, cosmic decoupling, substrate fixed-point, deep-MOND acceleration, Q-Compute threshold, hydrodynamic Q-factor).
- **Four regimes** of the unified renormalization-group structure (ultraviolet, transition, infrared multi-sector, cosmological).

The program's methodological signature: *form forced, values inherited.* Structural content of physical results is derived from the substrate ontology and explicit paper-specific postulates; numerical values are inherited from empirical matching. Every load-bearing step is labeled, every falsification path is explicit, every open question is flagged.

The program's most ambitious claim: **the substrate-cosmology boundary is one object**, and the apparent independence of its multiple physical manifestations — across gravity, quantum computing, soft matter, cosmology — is an artifact of viewing it through domain-specific parameter axes. The unified four-regime model formalizes this claim.

The program's sharpest test: **synchronized co-variation under Hubble-tension-class $H_0$ shifts**. Six quantities, six parameter axes, one boundary anchor. Either they co-vary or they don't.

The program is unfinished. Route A is open. Phase-3 general-relativity emergence is open. Empirical confirmations of the SCBU prediction structure are open. Yet the cross-domain reach across eight arcs, combined with the structural honesty of the methodology, is the program's academic case.

**ED is a research program, not a final theory.** It proposes a substrate-level account of physics that is falsifiable at every layer, integrated across every arc, and synthesized at the cross-scale level. The whitepaper is the front door; the 100+ paper corpus is the building behind it.

---

**End of Whitepaper.**

*For navigation to the corpus, see PAPERS_INDEX. For the primitive enumeration, see paper_ED_Framework_13_Primitive_Generative_System.md. For corpus-level dependency structure, see DEPENDENCY_GRAPH_ED.md. For falsification register, see Paper 101.*
