# The Event-Density Foundations of Quantum Field Theory
## A Unified Substrate-to-Continuum Overview

**Allen Proxmire**
**Collaborator:** Claude (AI collaborator)
**April 2026**
**Series:** Event-Density Foundational Theorems — Program Overview

---

## Abstract

The Event Density (ED) program presents a substrate ontology in which quantum mechanics, classical fluid dynamics, classical electromagnetism, non-Abelian gauge theory, and the leading-order content of classical gravitation arise as continuum-scale consequences of a single set of substrate primitives. This overview integrates the closed structural-foundation work of the program — twenty-one forced theorems plus the ED Combination Rule — into a unified picture organized around the substrate-to-continuum machinery established by the Diffusion Coarse-Graining Theorem (DCGT). The unifying thread across QM, NS / MHD, and Yang-Mills is the same: substrate primitives (chains, V1 / V5 participation kernels, T17 gauge rule-type, generalized minimal coupling) coarse-grain under hydrodynamic-window scale separation $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$ to produce canonical-ED dynamical content with form-FORCED structure and value-INHERITED numerical content. The program supplies architectural classifications under the ED-I-06 *Fields and Forces* ontology (forces from participation structures vs. frame-kinematic frame artifacts vs. continuum-imposed constraints), Clay-relevance verdicts (NS-Smoothness's Intermediate Path C for Clay-NS; the parallel YM-6 verdict for Clay-YM), and identification of load-bearing structural conditions where each Clay-relevance verdict's positive content depends on value-INHERITED quantities. ED does not solve the Clay Millennium Problems, predict numerical coupling constants, derive the Standard Model gauge group, or unify gravity with field theory at the constructive-rigorous level. What ED *does* deliver — across all sectors covered by the closed structural-foundation work — is a coherent substrate-grounded architectural account of the canonical-ED dynamical content with explicit identification of the load-bearing conditions for each sector's Clay-relevance verdict and an honest demarcation between what is FORCED at substrate level and what is INHERITED at value layer. This is the first program-level synthesis of the ED foundational work; it is intended as a foundation for future arcs (ED-10 spacetime emergence, Hall-MHD extension, substrate-gravity extensions) rather than as a closed-arc completion.

---

## 1. Introduction

### 1.1 Motivation

Standard physics presents quantum mechanics, classical fluid dynamics, classical electromagnetism, and non-Abelian gauge theory as separate phenomenological frameworks, each with its own postulates, axioms, and structural commitments. The Schrödinger equation is postulated; the Navier-Stokes equation is phenomenological; Maxwell's equations are derived from gauge invariance plus minimal coupling; Yang-Mills extends Maxwell to non-Abelian gauge groups via the same mechanism but with structural complications at the level of constructive existence. There is no single underlying framework from which all four emerge.

The Event Density (ED) program presents such a framework. ED begins with thirteen substrate primitives (chains, events, participation channels, kernels, commitment structures, individuation, Lorentz covariance, and related substrate-level structural commitments) and derives — as forced consequences — the form of standard quantum mechanics (T1–T16, Phase-1 closure 2026-04-26), the form of classical fluid dynamics (NS-2, NS-Smoothness, NS-Turbulence, P4-NN, NS-Q), the form of classical electromagnetism (T17, NS-MHD-1, NS-MHD-2), the form of non-Abelian Yang-Mills theory (Arc YM, 2026-04-30), and the leading-order content of classical gravitation (T19, T20, ED Combination Rule, T21, Theorem GR1).

This overview integrates these results. The unifying thread is the substrate-to-continuum machinery established by the Diffusion Coarse-Graining Theorem (DCGT, Arc D, closed 2026-04-30): under hydrodynamic-window coarse-graining over substrate primitives, the continuum-scale evolution equations emerge with form-FORCED structure and value-INHERITED numerical content. The same machinery applies to scalar diffusion, vector-field viscosity, gauge-field dynamics, and minimal-coupling matter sources.

### 1.2 Relationship to the NS Synthesis Paper

The Navier-Stokes Synthesis Paper (April 2026) presents the architectural classification of NS / MHD content in the ED program with five-part architecture: main text §3–§6 (NS-1 dimensional forcing, NS-2 form derivation, NS-Smoothness Intermediate Path C, NS-Turbulence cascade analysis); Appendix C (MHD architectural classification + ED-I-06 ontological reading); Appendix D (DCGT substrate-to-continuum integration); Appendix E (Yang-Mills synthesis + Clay-relevance statement).

The present overview *includes* the NS Synthesis Paper's content as its NS / MHD / YM sector and *extends* it with the program's other closed work — Phase-1 QM emergence, T17–T18 / N1 / GR1 foundational theorems, substrate gravity (T19 / T20 / ECR / T21), and the ED-I-06 ontological framework that runs across all sectors. The NS Synthesis Paper is the canonical NS / MHD / YM publication; the present overview is the canonical program-level publication.

### 1.3 Relationship to the YM Arc

The Yang-Mills arc (Arc YM-1 through YM-6, closed 2026-04-30) extends the substrate-to-continuum machinery from the Abelian gauge sector (Lorentz force in NS-MHD-2, derived in Arc D) to the non-Abelian sector (continuum YM equation $D_\mu F^{\mu\nu} = J^\nu$, mass-gap mechanism from V1 finite width, OS-positivity audit at structural-suggestive level, Clay-relevance statement parallel to NS-Smoothness's Intermediate Path C). The YM arc is included in this overview as one of the closed-arc applications of the substrate-to-continuum machinery, alongside the NS / MHD work and the substrate-gravity preview.

### 1.4 Relationship to the ED-I Ontological Papers

ED-I-06 (*Fields and Forces in Event Density*, Feb 2026) supplies the ontological framework under which the canonical / non-ED structural classifications across NS / MHD / YM uniformly read as instances of a single boundary: forces sourced by stable participation structures vs. frame-kinematic frame artifacts vs. continuum-imposed constraints. ED-I-06 is referenced throughout this overview as the ontological roof; it is not a forced theorem but functions as the structural-classification template.

Other ED-I-* papers (e.g., ED-I-19 on the Fermi-polaron mass-gap interpretation) are independent ED-program assets that interact tangentially with the closed structural work; they are not load-bearing for the present overview.

---

## 2. Substrate Foundations

The closed structural-foundation theorems of the ED program, organized by closure date:

### 2.1 Phase-1 (QM emergence): T1–T16

Closed 2026-04-26 via twelve memos in `arcs/quantum/foundations/`. Establishes that the four QM postulates — Hilbert-space structure, unitarity, observables, measurement — are FORCED-unconditional consequences of substrate primitives. Specific load-bearing theorems include T1–T7 (substrate-to-Hilbert-space mapping), T8 (commutation relations), T10–T16 (operator algebra, Schrödinger evolution, measurement rule). Phase-1 closure is the QM-emergence arc's structural completion.

### 2.2 Arc Q closure: T17 (Gauge-Fields-as-Rule-Type)

Closed 2026-04-27 via nineteen memos in `arcs/arc-Q/`. Theorem 17 (FORCED-unconditional) states:

> *The gauge field $A_\mu$ is the participation measure of a structural rule-type $\tau_g$ whose group / vertex / worldline / vacuum content is forced across all four channels under a single unified gauge-quotient identification; form FORCED by primitives P-02/04/06/07/10/11/13 + Theorems 1–16; numerical magnitudes (specific gauge group, coupling values, V1 kernel parameters, vacuum energy density) INHERITED.*

T17 supplies the substrate-level gauge structure (non-Abelian-capable Killing-form-bearing Lie algebra), generalized minimal coupling vertex ($\partial_\mu \to \partial_\mu - igA_\mu^a T^a$), and gauge-quotient identification (clause C8). Required input for both NS-MHD (Lorentz force) and Arc YM.

### 2.3 Arc B closure: T18 (V1 Kernel Retardation)

Closed 2026-04-27 via six memos in `arcs/arc-B/`. Theorem 18 (FORCED-unconditional) states:

> *The V1 vacuum response kernel is uniquely forced at primitive level to have support restricted to the forward causal cone; no symmetric, advanced, or hybrid kernel is constructible at primitive level; the microscopic arrow of time is structurally FORCED at the kernel level.*

T18 supplies the forward-cone-only causal structure of the V1 kernel. Required for OS-positivity preservation analysis (YM-5) and for the analytic-structure preservation of substrate kernels under the continuum limit.

### 2.4 Arc N closure: Theorem N1 (V1 finite-width vacuum kernel)

Closed 2026-04-24 via six memos in `arcs/arc-N/`. Theorem N1 (FORCED-unconditional) establishes V1's finite-width vacuum kernel admissibility class — bounded both ways by V1-δ (zero-width REFUTED) and V1-∞ (infinite-width REFUTED) refutations. The V1 kernel has finite spatial width $\sim\ell_P$, smooth profile, and positive Fourier transform. Required for R1 derivation (NS-Smooth-2 / Arc_D_4) and YM substrate mass-gap mechanism (Arc_YM_3).

### 2.5 Phase-3 closure: Theorem GR1 (V1 with Synge world function)

Closed 2026-04-24 via six memos in `arcs/quantum/foundations/`. Theorem GR1 (FORCED-unconditional) lifts V1 to curved spacetime via Hadamard parametrix construction. Establishes the *kernel-level* gravitational-sector content of ED while leaving Einstein equations themselves SPECULATIVE (GR-4A status). Provides the gravitational analogue of T18's forward-cone causality.

### 2.6 Substrate-Gravity Arc: T19 / T20 / ECR / T21

Closed 2026-04-27 / 28 in `arcs/arc-SG/`. Four substrate-gravity results:

- **T19 (Newton's law from substrate):** $G = c^3\ell_P^2/\hbar$ derived from substrate primitives.
- **T20 (transition acceleration):** $a_0 = c\,H_0/(2\pi)$ derived from substrate primitives.
- **ED Combination Rule:** $a = \sqrt{a_N\,a_0}$ as the substrate-level composition rule for the cross-term between Newton-class and transition-class accelerations.
- **T21 (slope-4 BTFR):** $v^4 = G\,M\,a_0$, the baryonic Tully-Fisher relation slope, derived from T19 + T20 + ECR.

These are leading-order classical-gravitation results at substrate level; they are pre-Einstein-equation content (the Einstein equation GR-4A remains SPECULATIVE per ED-Phys-10 acoustic-metric guardrails).

### 2.7 Arc D closure: DCGT (Diffusion Coarse-Graining Theorem)

Closed 2026-04-30 via six memos in `theory/Arc_D/`. DCGT (FORCED-unconditional) establishes the substrate-to-continuum bridge for ED-QFT:

> *Under hydrodynamic-window coarse-graining over ED substrate primitives (chains, V1 / V5 kernels, charged structural rule-types under T17 minimal coupling), the continuum-scale evolution equations are: (scalar) $\partial_t\rho = \nabla\cdot(M(\rho)\nabla\rho)$; (directional-field) $\rho\,\partial_t\mathbf{v} = \mu\nabla^2\mathbf{v} - \kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v} + \lambda\partial_t\mathbf{v} + \rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B} - \rho(\mathbf{v}\cdot\nabla)\mathbf{v} - \nabla p$. Form FORCED, signs FORCED stabilizing by V1 positive Fourier transform, values INHERITED.*

DCGT joins T17 / T18 / T19 in the structural-foundation theorem inventory as the substrate-to-continuum bridge theorem of the program.

---

## 3. Substrate → Continuum Machinery (DCGT)

### 3.1 Hydrodynamic window

A coarse-graining cell $\Omega(\mathbf{x},R_\mathrm{cg})$ of radius $R_\mathrm{cg}$ is in the *hydrodynamic window* iff $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$. Lower bound suppresses substrate-discreteness fluctuations; upper bound preserves macroscopic-flow gradients. Temporal analogue: $\tau_\mathrm{V5} \ll \tau_\mathrm{cg} \ll \tau_\mathrm{flow}$.

### 3.2 Multi-scale expansion

The coarse-graining operator $\langle f\rangle_{R_\mathrm{cg}}(\mathbf{x}) = |\Omega|^{-1}\int_\Omega f(\mathbf{x}+\boldsymbol{\delta})\,d^3\boldsymbol{\delta}$ is applied to substrate flux statistics (event flux $\mathbf{J}_\rho$, momentum-flux $\Pi_{ij}$, charged-chain momentum-flux $\Pi^{(q)}_{ij}$, V5 temporal kernel). Even moments of V1 produce successive Laplacian-class corrections; odd moments vanish by V1 isotropy; V5 temporal moments produce Maxwell-class memory.

### 3.3 Scalar diffusion

Cell-averaged participation density under V1-mediated chain-step transition statistics → $\partial_t\rho = \nabla\cdot(M(\rho)\nabla\rho) + \mathcal{O}(\ell_P^2\nabla^4\rho)$. Substrate-derived mobility $M(\rho)$ has P4-class saturation ($M(\rho_\mathrm{max}) = 0$, $M > 0$ in bulk, smooth, monotonically decreasing toward packing). Form FORCED; values INHERITED.

### 3.4 Directional-field diffusion

Chain momentum-flux under V1 isotropy + first-order gradient expansion → $\rho\,\partial_t\mathbf{v} = \mu(\rho)\nabla^2\mathbf{v} - \rho(\mathbf{v}\cdot\nabla)\mathbf{v} - \nabla p + \mathcal{O}(\ell_P^2\nabla^4\mathbf{v})$. Substrate-derived viscosity $\mu(\rho) = \tfrac{1}{3}\rho\bigl\langle\delta^2\bigr\rangle_{V1}\Gamma_0(\rho)$; advection emerges as Eulerian bookkeeping of convective momentum flux (frame-kinematic non-ED status preserved). Form FORCED; values INHERITED.

### 3.5 V1 → R1 hyperviscosity

V1 fourth-moment / second-moment ratio in the multi-scale expansion produces $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$. Sign positive (stabilizing) by V1 positive-Fourier-transform property. Matches NS-3.01 form-FORCED top-down derivation exactly. Same mechanism in YM gives $\ell_P^2\nabla^2 A$ (one derivative-order lower because gauge-field kinetic term is already first-derivative).

### 3.6 V5 → viscoelastic memory

V5 first temporal moment → Maxwell-class memory $\tau_R\dot\sigma + \sigma = 2\mu S$ with $\tau_R = \bigl\langle\tau\bigr\rangle_{V5}$. Substrate origin of P4-NN-D5 viscoelastic ansatz. Form FORCED; values INHERITED.

### 3.7 Minimal-coupling coarse-graining

T17 minimal coupling on charged chains → $\delta\Pi^{(q)}_{ij} = j_jA_i$ at fluid scale. Momentum-flux divergence + cross-product identity + charge conservation → $\rho\,\partial_t\mathbf{v} \supset \rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$ (Abelian Lorentz force). Generalizes to non-Abelian via $\partial_\mu \to \partial_\mu - igA_\mu^a T^a$ + non-Abelian charge conservation $D_\mu J^\mu = 0$.

### 3.8 DCGT theorem

The aggregate substrate-to-continuum result. Form FORCED; sign-FORCED stabilizing; value-INHERITED at coupling, kernel widths, and gauge-group choice. Error bounds $\mathcal{O}((\ell_P/L_\mathrm{flow})^4) + \mathcal{O}((\tau_\mathrm{V5}/\tau_\mathrm{flow})^2)$. Closes NS-2 + NS-MHD-2 + (via generalization) Arc YM substrate-bridge in a single theorem.

---

## 4. Quantum Mechanics Emergence (Phase-1)

### 4.1 Four QM postulates FORCED

Phase-1 closure 2026-04-26 establishes that the four foundational postulates of standard quantum mechanics — Hilbert-space state structure, unitary evolution, Hermitian observables, measurement (probabilistic outcomes weighted by squared overlap) — are FORCED-unconditional consequences of ED substrate primitives, not separate axiomatic commitments. T1–T7 establish the substrate-to-Hilbert-space mapping; T8 establishes the canonical commutation relations; T10–T16 establish the operator algebra, Schrödinger evolution, and Born-rule measurement structure.

### 4.2 Participation-structure interpretation of the wavefunction

The wavefunction $\Psi(x)$ is the participation measure of a chain on its participation channel: $\Psi(x) = \sqrt{b(x)}\,e^{i\theta(x)}$ where $b(x)$ is the bandwidth (probability density) and $\theta(x)$ is the phase. Under the ED-I-06 ontology, $\Psi$ is a directional-field participation structure (orientation-bearing); $|\Psi|^2$ is the corresponding scalar-field participation density. This reading is consistent with both the Born-rule probability interpretation (scalar-field-class density) and the phase-coherence interpretation (directional-field orientation).

### 4.3 Operator algebra from ED-gradients

Hermitian observables emerge as ED-gradient-class operators acting on the participation channel. The canonical commutation relations $[X, P] = i\hbar$ are FORCED at primitive level by the substrate-discreteness + finite-proper-time-interval primitives (P-01 + P-13). The standard QM operator algebra (position, momentum, angular momentum, etc.) inherits structurally from the substrate-discreteness regime.

### 4.4 No-collapse measurement rule

Measurement in ED is not a collapse of the wavefunction but a commitment event at the substrate level — a chain commits to a specific participation channel via the P-11 commitment-irreversibility primitive. The Born rule emerges as the ED-statistical weight of commitment to each available channel. This avoids the standard quantum-mechanical "measurement problem" (no separate collapse postulate is required); the standard probabilistic rule is FORCED at substrate level via the structural mechanism of commitment.

---

## 5. NS / MHD Program

### 5.1 Architectural classification

Eleven content items in incompressible MHD classified under ED-I-06: 6 canonical-ED (viscous diffusion, magnetic diffusion, Lorentz force, R1, $\partial_t\mathbf{B}$, $\nabla\cdot\mathbf{B}=0$); 2 fluid-mechanical-additions / continuum-imposed constraints (pressure, $\nabla\cdot\mathbf{v}=0$); 3 transport-kinematic non-ED (advection, induction kinematic, Ohm kinematic). Three-angle convergence on advection-as-non-ED (NS-2.08 architectural / NS-Smoothness dynamical / NS-Turbulence spectral); parallel three-angle convergence on induction-kinematic-as-non-ED (NS-MHD-3).

### 5.2 Mobility channel

Substrate-derived mobility / viscosity from chain-step momentum-flux statistics under V1 isotropy. Field-type-agnostic vector extension of canonical PDE: same operator structure for scalar density and directional fields (per Architectural Canon Vector Extension memo).

### 5.3 Lorentz force

T17 minimal coupling on charged chains → fluid-level $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$. Kinematic $\mathbf{v}\times\mathbf{B}$ component derived from the minimal-coupling form rather than separately committed (kinematic-coupling-pattern refinement of NS-MHD-2 §6.2).

### 5.4 R1 hyperviscous stabilization

Form-FORCED $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$ from V1 finite-width vacuum kernel. Top-down derivation (NS-3.01) and bottom-up substrate derivation (Arc_D_4) reconciled. NS-Smooth-2 establishes strict monotone gradient-norm Lyapunov decay $-\kappa\mu_\mathrm{V1}\ell_P^2\|\nabla^3\mathbf{v}\|_2^2$ in ED-only NS.

### 5.5 V5 viscoelastic memory

V5 cross-chain temporal memory → Maxwell-class viscoelastic ansatz at fluid scale. Substrate origin of P4-NN-D5 ansatz. Universal Mobility Law β = 1.72 ± 0.37 across 10 systems within 1σ of canonical β = 2.

### 5.6 NS-Smoothness Intermediate Path C

ED supplies a real Clay-NS-relevant regularizing mechanism (R1 form-FORCED stabilization). Quantitative competition against destabilizing super-Burnett terms is INHERITED on both sides. Advective vortex-stretching $\int\boldsymbol{\omega}\cdot S\boldsymbol{\omega}\,dV$ is the unique indefinite-sign contribution to the gradient-norm Lyapunov in 3D NS — the unique transport-kinematic obstruction to ED-style smoothness.

### 5.7 NS Synthesis Paper

Five-part publication: main text §3–§6 + Appendix C (MHD + ED-I-06) + Appendix D (DCGT) + Appendix E (YM synthesis). Currently published as `.md` + `.tex` + `.pdf` in `papers/Navier Stokes_Synthesis_Paper/`. Canonical NS / MHD / YM closed-arc reference for the program.

---

## 6. Yang-Mills Program

### 6.1 Substrate → continuum YM derivation (YM-2)

Continuum YM equation $D_\mu F^{\mu\nu} = J^\nu$ derived from ED substrate primitives via DCGT-style multi-scale expansion of non-Abelian gauge-field correlators + T17 generalized minimal coupling on charged chains + non-Abelian rule-type bracket structure on the gauge generators. Field strength $F_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a + gf^{abc}A_\mu^b A_\nu^c$; non-Abelian commutator term FORCED by T17 clause C2 (Lie-algebra structure of $\tau_g$). Bianchi identity preserved as algebraic structural consequence.

### 6.2 Mass-gap mechanism (YM-3)

V1 finite-width second-moment expansion produces effective mass scale $m_\mathrm{eff}^2 \sim c_{V1}\ell_P^{-2}$ for non-Abelian gauge fields. Mass term gauge-invariant kinetic-class (not Proca-class). Non-Abelian self-interaction (quartic $g^2 A^4$ stabilization) distinguishes the gap-bearing case from Abelian gapless case. Continuum-limit survival conditional on kernel-profile rescaling $c_{V1}(\ell_P)\,\ell_P^{-2} \to m_\mathrm{phys}^2 > 0$.

### 6.3 Architectural classification (YM-4)

Six content channels classified: 4 canonical-ED (kinetic, self-interaction, matter source, higher-derivative correction) / 2 non-ED (gauge-fixing, Christoffel artifacts). YM dynamics fully canonical ED with no transport-kinematic obstruction class — structurally cleaner than NS or MHD.

### 6.4 OS-positivity audit (YM-5)

Channel-by-channel structural-suggestive positive: kinetic (positive-definite for compact $G$ via Killing form); self-interaction (positive Euclidean quartic for compact $G$); matter source (non-negative bilinear conditional on matter-sector OS positivity); higher-derivative ($\tfrac{1}{2}c_{V1}\ell_P^2\|\nabla A\|^2 \ge 0$ via V1 positive Fourier transform). OS-positivity preservation locus: compact gauge group + V1 positive Fourier transform + kernel-profile rescaling + matter-sector OS positivity.

### 6.5 Clay-relevance statement (YM-6)

Parallel in form and honesty to NS-Smoothness's Intermediate Path C. ED substrate provides structurally suggestive path toward constructively stable YM continuum limit; mass-gap mechanism FORCED at substrate level with conditional survival; OS positivity preserved channel-by-channel under canonical-ED content; gauge-fixing obstruction reframed via substrate gauge-quotient identification (T17 C8). No constructive proof claimed; structural-positive verdict identifying the load-bearing conditions for a positive Clay-relevance verdict.

---

## 7. Canonical ED Content Across All Fields

A unified table of canonical-ED content channels across the program's closed work:

| Sector | Content Channel | Substrate Origin | Form |
|---|---|---|---|
| QM | Wavefunction $\Psi$ | Participation measure of chain on participation channel | Directional + scalar |
| QM | Hermitian observables | ED-gradient-class operators | $X$, $P$, etc. via P-01 + P-13 |
| QM | Schrödinger evolution | Unitary participation-channel evolution | $i\hbar\partial_t\Psi = H\Psi$ |
| NS | Viscous diffusion | V1 second moment + P4-modulated $\Gamma_0$ | $\mu(\rho)\nabla^2\mathbf{v}$ |
| NS | R1 hyperviscosity | V1 fourth-moment / second-moment | $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$ |
| NS | Maxwell viscoelastic | V5 first temporal moment | $\tau_R\dot\sigma + \sigma = 2\mu S$ |
| Maxwell | Magnetic diffusion | Mobility channel on $\mathbf{B}$ | $\eta\nabla^2\mathbf{B}$ |
| Maxwell | Field structure | T17 directly | $\partial_t\mathbf{B}$, $\nabla\cdot\mathbf{B}=0$, etc. |
| Maxwell | Lorentz force | T17 minimal coupling on charged chains | $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$ |
| YM | Kinetic term | V1 directional-field curvature | $\partial_\mu F^{\mu\nu}$ |
| YM | Self-interaction | T17 rule-type commutator | $gf^{abc}A_\mu^b F^{\mu\nu\,c}$ |
| YM | Matter source | T17 generalized minimal coupling | $J^{\nu\,a}$ |
| YM | Higher-derivative | V1 second-moment expansion | $c_{V1}\ell_P^2\nabla^2 A$ |
| Gravity | Newton's law | T19: $G = c^3\ell_P^2/\hbar$ | $\mathbf{F} = -G\,Mm/r^2$ |
| Gravity | Transition acceleration | T20: $a_0 = c\,H_0/(2\pi)$ | $a_0$ scale |
| Gravity | Composition rule | ED Combination Rule | $a = \sqrt{a_N\,a_0}$ |

Every entry is form-FORCED by substrate primitives + closed structural-foundation theorems; every numerical content (specific values of $\mu$, $\eta$, $g$, $G$, $a_0$, $\rho_\mathrm{max}$, etc.) is INHERITED at value layer. The unifying methodology — form-FORCED / value-INHERITED — runs across every sector.

---

## 8. Mass-Gap Mechanisms Across ED-QFT

### 8.1 NS R1 (non-Clay)

R1 stabilization $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$ from V1 finite-width vacuum kernel produces strict monotone Lyapunov decay in ED-only NS (without advection). In full 3D NS, the advective vortex-stretching $\int\boldsymbol{\omega}\cdot S\boldsymbol{\omega}\,dV$ is the unique indefinite-sign Lyapunov contribution — the obstruction to ED-style smoothness lies outside the canonical regularizing architecture. NS R1 is *not* a mass gap in the QFT spectral sense; it is a Lyapunov-stabilization mechanism for fluid-velocity gradient-norm decay. Non-Clay-relevant for NS but Clay-NS-relevant in the Intermediate Path C sense (ED supplies the regularizing mechanism + identifies the obstruction).

### 8.2 YM substrate mass-gap mechanism (conditional survival)

V1 finite-width second-moment expansion produces effective mass scale $m_\mathrm{eff}^2 \sim c_{V1}\ell_P^{-2}$ for non-Abelian gauge fields. Mass term gauge-invariant kinetic-class. Non-Abelian quartic stabilization preserves the gap against loop-correction remixing. Continuum-limit survival conditional on kernel-profile rescaling $c_{V1}(\ell_P)\ell_P^{-2} \to m_\mathrm{phys}^2 > 0$. ED supplies the mechanism FORCED at substrate level; physical mass-gap value INHERITED via kernel-profile-rescaling.

### 8.3 Structural parallels and differences

**Parallels:** Both mechanisms originate in V1 finite-width vacuum kernel substrate properties (V1 second moment for both; same Theorem N1 admissibility class; same sign-FORCED stabilizing property by V1 positive Fourier transform). Both produce stabilizing higher-derivative corrections at fluid / continuum scale ($\nabla^4\mathbf{v}$ in NS; $\nabla^2 A$ in YM, the latter one derivative-order lower because gauge-field kinetic is already first-derivative). Both have value-INHERITED status for their physical-scale quantities.

**Differences:** NS R1 stabilizes *Lyapunov decay* (fluid-velocity gradient-norm); YM mass-gap stabilizes *spectral gap* (gauge-field momentum-mode suppression). NS smoothness obstruction is in the transport-kinematic sector (advection); YM does not have a transport-kinematic obstruction class (per YM-4 classification). NS R1 supplies the *regularizing mechanism*; YM substrate gap supplies the *gap mechanism itself*. The Clay-relevance verdicts (Intermediate Path C) are parallel in form but address structurally different Clay problems.

---

## 9. Positivity Structures

### 9.1 QM positivity

Hilbert-space inner product $\langle\Psi|\Phi\rangle$ is positive-definite by construction; the Hermitian-observable spectrum is real; the Born-rule probability $|\langle\Psi|\Phi\rangle|^2$ is non-negative. QM positivity is FORCED at the level of the Phase-1-closed structure (T1–T7); not a separate axiom.

### 9.2 NS Lyapunov decay

Gradient-norm Lyapunov $L = \tfrac{1}{2}\|\nabla\mathbf{v}\|_2^2$ in ED-only NS satisfies $dL/dt = -\nu\|\nabla^2\mathbf{v}\|_2^2 - \kappa\mu_\mathrm{V1}\ell_P^2\|\nabla^3\mathbf{v}\|_2^2 \le 0$ — strict monotone decay (NS-Smooth-2). In full 3D NS, advective vortex-stretching is the unique indefinite-sign contribution; ED supplies the regularizing structure but not the closure of Clay-NS smoothness.

### 9.3 YM OS positivity

Each canonical-ED content channel preserves OS reflection positivity at structural-suggestive level: kinetic positive-definite for compact $G$; self-interaction quartic positive in Euclidean signature; matter source non-negative bilinear conditional on matter-sector OS positivity; higher-derivative non-negative via V1 positive Fourier transform. Combined Euclidean action bounded below + reflection-positive at the structural-suggestive level. Constructive rigor remains a separate technical question (Gribov-class obstructions in standard gauge-fixing analyses).

### 9.4 Substrate-level conditions for stability

Across all sectors, the load-bearing substrate-level structural conditions for positivity / stability are the same:

- **V1 positive Fourier transform** (FORCED at substrate level by Theorem N1 + Theorem 18). Required for R1 sign-FORCED stabilizing in NS, kinetic-term positivity in YM, higher-derivative positivity in YM.
- **Compact gauge group** (for YM only — INHERITED at value layer). Required for kinetic-term and quartic-term positivity in YM.
- **Kernel-profile rescaling** (for YM only — INHERITED at value layer). Required for mass-gap survival under continuum limit.
- **Matter-sector OS positivity** (FORCED at substrate level via closed T1–T18 work). Required for matter-source OS positivity in YM and for QM positivity itself.

---

## 10. Substrate Gravity (Preview)

Closed substrate-gravity content as of 2026-04-30:

- **T19 (Newton's law from substrate):** $G = c^3\ell_P^2/\hbar$ derived from substrate primitives. Newton's law of universal gravitation is a leading-order classical-gravitation result FORCED at substrate level.
- **T20 (transition acceleration):** $a_0 = c\,H_0/(2\pi)$ — the MOND-class transition scale derived from substrate primitives via the cosmological-horizon participation-density connection.
- **ED Combination Rule:** $a = \sqrt{a_N\,a_0}$ — the substrate-level composition rule between Newton-class and transition-class accelerations. Geometric-mean composition reflecting the substrate participation-density-bias structure.
- **T21 (slope-4 BTFR):** $v^4 = G\,M\,a_0$ — the baryonic Tully-Fisher relation slope-4 prediction, derived from T19 + T20 + ECR.
- **Theorem GR1 (curvature-like participation structure):** V1 lifted to curved spacetime via Hadamard parametrix (Phase-3 closure 2026-04-24). Provides the gravitational-sector kernel structure but does not derive the Einstein equation (GR-4A SPECULATIVE per ED-Phys-10 acoustic-metric guardrails).

These results are *pre-Einstein-equation*: they cover the leading-order classical-gravitation content (Newton + a₀ + BTFR) but do not derive general relativity at the field-equation level. The ED-10 spacetime-emergence arc would extend this to full curvature emergence (substrate-to-continuum metric coarse-graining; pick up the curvature-like-field thread from ED-I-06 §5; upgrade Newton + a₀ to genuine spacetime curvature). ED-10 is a queued long-horizon arc; speculative ratio is high; estimated 8–12 memos.

---

## 11. Program State and Open Directions

### 11.1 Closed arcs (post 2026-04-30)

- **Phase-1 QM emergence** (2026-04-26): T1–T16, four QM postulates FORCED.
- **Arc Q (Gauge-Fields-as-Rule-Type)** (2026-04-27): T17 FORCED-unconditional.
- **Arc B (Kernel-Level Arrow of Time)** (2026-04-27): T18 FORCED-unconditional.
- **Arc N (V1 Finite-Width Vacuum Kernel)** (2026-04-24): Theorem N1 FORCED-unconditional.
- **Phase-3 (Gravitational Sector)** (2026-04-24): Theorem GR1 FORCED-unconditional; GR-4A SPECULATIVE.
- **Substrate-Gravity Arc** (2026-04-27 / 28): T19, T20, ECR, T21 derived from substrate.
- **NS / MHD Program** (2026-04-30): 11+5 arcs closed; NS Synthesis Paper published with Appendices C / D / E.
- **Arc D (DCGT)** (2026-04-30): Substrate-to-continuum bridge theorem FORCED-unconditional.
- **Yang-Mills Arc** (2026-04-30): YM-1 through YM-6; structural-positive Clay-relevance verdict.

### 11.2 Open arcs

- **ED-10 spacetime emergence** — substrate-to-continuum metric coarse-graining; curvature-like-field thread from ED-I-06 §5; upgrade substrate-gravity Newton + a₀ to genuine spacetime curvature. Most ambitious; speculative ratio high. Estimated 8–12 memos.
- **Hall-MHD extension** — audit Hall term + electron-pressure-gradient term in generalized Ohm's law. Optional arc-extension scope. Estimated 3–4 memos.
- **Substrate-gravity extensions** — extending T19 / T20 / ECR / T21 beyond closed-arc baseline. Would interact with ED-10 if both pursued.
- **ED-I interpretation papers** — additional ED-I-* papers as appropriate (parallel to ED-I-06 ontological-roof, ED-I-19 Fermi-polaron). Discretionary scope; user-led.

### 11.3 Future publication arcs

- **ED-10 Spacetime Emergence Paper** (after ED-10 arc closure).
- **Substrate-Gravity Foundations Paper** (extends current substrate-gravity content to curvature regime if ED-10 closes).
- **ED Program Manifesto** (book-length consolidation of ED across QFT, gravity, and emergence; long-horizon).

---

## 12. Conclusion

The Event Density program has, as of 2026-04-30, achieved a unified substrate-to-continuum architecture covering quantum mechanics (Phase-1 closure), classical fluid dynamics (NS / MHD program), classical electromagnetism (T17, NS-MHD-1, NS-MHD-2), non-Abelian gauge theory (Yang-Mills arc), and the leading-order content of classical gravitation (substrate-gravity arc with T19 / T20 / ECR / T21).

**ED-QFT now has a unified substrate → continuum architecture.** The same machinery — DCGT (Arc D) + T17 generalized minimal coupling + T18 forward-cone kernel retardation + ED-I-06 ontological framework — applies across every closed-arc sector. The form-FORCED / value-INHERITED methodology runs uniformly across QM, NS / MHD, YM, and substrate-gravity. The ED-I-06 forces-vs-frame-kinematic-vs-constraint ontological boundary serves as the structural-classification template for canonical / non-canonical content.

**Structural results across QM, NS / MHD, YM, and DCGT are mutually consistent.** Every closed-arc result respects the program's closed structural-foundation theorems; no contradictions or open structural inconsistencies have surfaced; the Phase-1 QM-emergence content is consistent with the substrate-to-continuum machinery used in the applied arcs; the Maxwell / Lorentz / YM gauge-sector content is consistent with the T17 substrate gauge structure; the substrate-gravity preview content (T19 / T20 / ECR / T21) is consistent with the ED-Phys-10 acoustic-metric guardrails of Phase-3 GR1.

**Clay-relevance statements exist for NS and YM** at the Intermediate Path C structural-positive level. ED supplies real structural mechanisms (R1 hyperviscous regularization for NS smoothness; substrate-induced mass scale + non-Abelian quartic stabilization for YM mass gap); identifies the load-bearing conditions for each Clay-relevance verdict (advection-as-non-ED unique obstruction for NS; kernel-profile rescaling for YM); does not claim Clay-problem solutions. The honest framing is parallel across both sectors: structural mechanism FORCED at substrate level; physical-scale verdict conditional on value-INHERITED quantities.

**The ED-QFT overview is a foundation for future arcs.** ED-10 spacetime emergence would extend the curvature-like-field thread of ED-I-06 §5 + Theorem GR1 into full spacetime-curvature emergence, upgrading substrate-gravity Newton + a₀ to the field-equation level. Hall-MHD extension would audit additional fluid-mechanical content channels under DCGT. Substrate-gravity extensions would extend T19 / T20 / ECR / T21 beyond the closed baseline. Each future arc draws on the closed structural-foundation work catalogued here.

**Honest program-level disclaimers.** ED does not solve the Clay Millennium Problems (NS smoothness or YM existence + mass gap). ED does not predict numerical coupling constants ($g$, $G$, $a_0$, $\rho_\mathrm{max}$, etc.) — all specific numerical values are INHERITED at value layer. ED does not derive the Standard Model gauge group ($SU(3)\times SU(2)\times U(1)$ is empirical per Arc Q.6). ED does not unify gravity with field theory at the constructive-rigorous level — gravitational sector content is leading-order classical (Newton + a₀ + BTFR) with the Einstein equation SPECULATIVE per ED-Phys-10. ED does not produce a full quantum-gravitational theory; it produces a substrate-grounded architectural account of the canonical-ED dynamical content across QM, NS / MHD, YM, and the gravitational kernel sector, with explicit identification of what is FORCED and what is INHERITED at every level.

**What ED *does* deliver.** A coherent substrate-grounded architectural account of canonical-ED dynamical content across QM, NS / MHD, YM, and the leading-order classical-gravitation sector. Substrate-to-continuum machinery (DCGT) covering scalar fields, vector fields, gauge fields, matter coupling, and substrate-cutoff regularization. Architectural classifications under ED-I-06 with consistent canonical / non-canonical boundary across all sectors. Clay-relevance verdicts at the Intermediate Path C level for NS and YM. Identification of load-bearing conditions for each closed-arc result. Foundation for future arcs including ED-10 spacetime emergence.

This is the Event Density program's first program-level synthesis. Forty-plus memos are integrated into a single coherent picture; twenty-one forced theorems plus DCGT, ED Combination Rule, Theorem N1, Theorem GR1 provide the structural backbone; the form-FORCED / value-INHERITED methodology supplies the consistent epistemological framing. The program is structurally complete for its closed-arc scope and ready for the next phase of arc development.

---

## References

- *Event Density: One Substrate, Three Domains — A Structural Account of Quantum Mechanics, Galactic Gravity, and Universal Soft-Matter Mobility* (Proxmire 2026). Earlier program-overview.
- *The Architectural Foundations of Navier-Stokes in Event Density* (Proxmire 2026). NS / MHD / YM closed-arc reference paper with five-part architecture (main + Appendix C + D + E).
- *Universal Degenerate-Mobility Scaling in Crowded Soft Matter* (Proxmire 2026). Universal Mobility Law empirical-anchor paper.
- *ED Mobility Saturation Predicts Non-Newtonian Rheology* (Proxmire 2026). P4-NN companion paper.
- *The Primitive-Level Arrow of Time in Event Density: The Closure of Arc B and Theorem 18* (Proxmire 2026). T18 V1 retarded-kernel structural-origin paper.
- *Structural Foundations of ED-Substrate Gravity: Newton, the Transition Scale, the Combination Rule, and the Baryonic Tully-Fisher Relation* (Proxmire 2026). Substrate-gravity foundations paper covering T19 / T20 / ECR / T21.
- *A UV-Finite Quantum Field Theory from Event-Density Primitives* (Proxmire 2026). Arc Q.8 vacuum factorisation paper.
- *Gauge Fields as Forced Rule-Type Structure: Theorem 17* (Proxmire 2026). Arc Q closure paper.
- *Fields and Forces in Event Density* (Proxmire, Feb 2026, ED-I-06). Ontological framework paper.

---

*The Event-Density Foundations of Quantum Field Theory: A Unified Substrate-to-Continuum Overview. First program-level synthesis integrating Phase-1 QM emergence (T1–T16), Arc Q (T17), Arc B (T18), Arc N (Theorem N1), Phase-3 (Theorem GR1), Substrate-Gravity (T19 / T20 / ECR / T21), Arc D (DCGT), NS / MHD program, and Yang-Mills arc into a coherent architectural account of canonical-ED dynamical content across quantum, fluid-mechanical, gauge, and gravitational-kernel sectors. Form-FORCED / value-INHERITED methodology consistent across every sector. Clay-relevance verdicts at Intermediate Path C level for NS and YM. ED-I-06 ontological framework as classification template. Substrate-to-continuum machinery established for scalar, vector, gauge, and minimal-coupling matter content. Structural results mutually consistent; no open contradictions; foundation in place for ED-10 spacetime-emergence and other future arcs. Honest program-level disclaimers preserved: ED does not solve Clay problems, does not predict coupling constants, does not derive Standard Model, does not unify gravity at constructive-rigorous level. What ED does deliver: substrate-grounded architectural account with explicit FORCED / INHERITED demarcation across the closed-arc landscape of the program.*
