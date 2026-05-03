---
title: |
  Quantum Computation in Event Density\
  \large A Substrate-Level Architecture and Its Limits
author: Allen Proxmire
date: May 2026
---

## Abstract

The Event Density (ED) framework provides a substrate-level account of quantum computation in which three substrate quantities — local **multiplicity** (the count of available participation pathways at the system's endpoints), **cross-endpoint connectivity** (the substrate-mediated bandwidth that links them), and **commitment-injection rate** (the rate at which the environment forces individuation) — jointly determine whether quantum computation is possible. The **Unresolved-Regime Characterization Theorem (UR-1)** identifies three independently-necessary conditions on these quantities, and the resulting QC operating window is given structurally by $\tau_{\mathrm{QC}} = \min(\tau_{(\mathrm{i})}, \tau_{(\mathrm{ii})}, \tau_{(\mathrm{iii})})$ over the three corresponding failure timescales. Each architectural platform binds on whichever timescale is shortest under its protection strategy.

Three architectural classes — **engineered-low-multiplicity (A)** covering superconducting qubits, trapped ions, and gate-model photonics; **global-geometric-rigidity (B)** covering topological qubits and photonic Chern channels; and **high-multiplicity-redundancy (C)** covering bosonic codes and multi-timescale photonics — exhaust the substrate-allowed strategies for holding the operational regime. Error correction, dynamical decoupling, reservoir engineering, and hybrid architectures are derived as compositions or extensions of the three classes rather than new strategies. The **multiplicity-cap function $M$** unifies the classes as three projections of one substrate object, with platform-specific behavior obtained by specializing class-dependent parameters.

The framework's strongest output is **cross-platform unification**: the matter-wave quantum-classical boundary observed empirically at 140–250 kDa molecular mass and the multiplicity walls that limit qubit-system scaling are the same substrate-determined boundary projected onto two different platforms, evaluated at consistent values of one underlying substrate constant. Sharp predictions follow directly: superconducting platforms encounter a hard scaling ceiling unless they are composed with logical-qubit encoding; topological qubits can outrun this ceiling exponentially in the topological gap if topology engineering can deliver stable structures; redundancy-based architectures saturate at a substrate-determined correlation budget. Four classes of near-term experimental tests with explicit falsification conditions are specified.

The structural form of the framework is derived from substrate primitives; specific numerical thresholds (the critical multiplicity, the correlation budget, the maximum stable topological gap, and the platform-specific wall locations) are downstream empirical calibrations rather than free parameters, with the empirical anchors that fix them identified explicitly. **The verdict is architectural-level structural completeness with an explicit empirical-calibration roadmap**: the substrate-level account of quantum computation is delivered, the predictions are sharp enough to be falsified by near-term measurements, and the calibration program that converts structural predictions into platform-specific numerical bounds is engineering-tractable rather than theoretically blocked.

---

## 1. Introduction

### 1.1 Motivation

Quantum computing has produced, over the past three decades, two compelling but partial pictures of itself. The first picture is engineering-led: quantum computers are devices that maintain coherence against decoherence, and progress is the steady reduction of the engineering distance between current platforms and a fault-tolerant million-qubit logical machine. The second picture is information-theoretic: quantum computation is the manipulation of entangled state-spaces whose dimension grows exponentially in qubit count, and the question is what classes of problems benefit from the exponential resource.

Neither picture answers the structural question: *what is quantum computation, at the level of physics, and what are its substrate-level limits?* Empirical scaling debates — when will logical-qubit lifetimes exceed physical T₁? when will topological qubits surpass superconducting? does multi-axis redundancy keep paying as you add axes? — are addressed pragmatically, platform by platform, with no shared structural framework predicting which architectures should hit which walls and why.

The Event Density program approaches this question from a substrate-ontological starting point. ED's primitives — local participation density, irreversible commitment events, finite-bandwidth substrate channels, V1 finite-width vacuum kernel — generate quantum mechanics as a coarse-grained continuum reading of substrate dynamics in the thin-participation regime (the program's Phase-1 closure of the QM postulates). Quantum computation is then a particular *engineered occupation* of this regime: a system held in the unresolved low-multiplicity state long enough for its substrate-level participation geometry to be manipulated, before environmental ED-injection forces individuation at readout.

This paper develops the substrate-level architecture of that picture. It establishes the gate-condition theorem for the unresolved regime, derives the three-class exhaustive taxonomy of architectural protection strategies, constructs the multiplicity-cap function $M$ that unifies QC platform behavior across substrate-distant scales, and delivers falsifiable predictive content with explicit demarcation between substrate-derived form and substrate-inherited values.

### 1.2 ED Ontology in Brief

ED treats reality, at its most fundamental level, as discrete *events* — atomic moments of becoming — linked by relational *participation channels*. Particles and fields are not fundamental; they are stable patterns of substrate participation. Spacetime is not fundamental; it emerges from the way events relate, with locality, causality, and metric structure as coarse-grained signatures of dense, redundant, irreversibly-committed participation networks. Time is not a primitive; time is the irreversible direction along which events commit to being something, with the asymmetry secured by the substrate primitive P11 (commitment-irreversibility).

For quantum computation, three substrate primitives are load-bearing.

- **Multiplicity** $\mathcal{M}$: the count of viable distinct ED-gradient pathways available to a system. Per ED-I-01 (Superconductivity, February 2026), multiplicity is the ED analogue of entropy. Low $\mathcal{M}$ means few alternative pathways; high $\mathcal{M}$ means many. Symmetry collapses multiplicity; thermal agitation raises it.

- **Cross-bandwidth** $\Gamma_{\mathrm{cross}}$: the substrate-mediated rate at which adjacent regions exchange correlated participation events. Established in Arc D (Diffusion Coarse-Graining Theorem, April 2026) as $\Gamma_{\mathrm{cross}} \sim \exp[-\alpha\sigma]$ where $\sigma = |\nabla\rho|\ell_P^2/\rho_{\mathrm{local}}$ is the substrate-scale gradient sparsity.

- **Commitment-injection rate** $\Lambda$: the rate at which P11 commitment events fire at a region's endpoints, sourced by environmental ED-injection plus internal participation dynamics.

A system performing quantum computation, in ED's reading, is a substrate region in which a participation rule remains *unresolved* across designated endpoints — its identity has not individuated to any specific configuration — for a finite substrate-time window long enough for the rule's geometry to be manipulated through engineered substrate operations (gates), before environmental ED-injection drives it to individuation (readout).

### 1.3 Why Standard QC Framing Misses the Substrate-Level Question

Standard QC treats coherence as a state property of a wavefunction and decoherence as the wavefunction's coupling to environmental degrees of freedom. The ontological picture is: there is a quantum system, it has a state, the state can be coherent or decoherent, and engineering reduces the coupling that drives state collapse.

ED's reframe is structurally distinct. There is no fundamental wavefunction in the substrate ontology; what exists is a participation structure with a rule spanning endpoints. Coherence is the integrity of that rule before commitment; decoherence is the substrate-level event of commitment occurring. Engineering doesn't slow down a coupling-rate to a state; it holds the substrate region in a low-multiplicity, well-connected, low-commitment-rate configuration, against the substrate's natural tendency to proliferate gradients and force individuation.

Three structural questions become tractable in this picture that are not addressable in the standard one:

1. *What is the substrate-level signature of "doing QC"?* Answer (this paper): a system satisfying the three conditions of the Unresolved-Regime Characterization Theorem (UR-1).

2. *What architectural strategies can hold the system in that regime?* Answer: three exhaustive substrate-level protection strategies — direct $\mathcal{M}$ control (Class A), direct $\sigma$-geometry control via topology (Class B), redundancy across pathways (Class C).

3. *What unifies coherence behavior across qualitatively different platforms — matter-wave interferometers, superconducting qubits, Josephson junctions, topological qubits, multi-timescale photonic lattices?* Answer: one substrate function $M$ with three architectural-class projections, on which all platforms place at consistent substrate-determined locations.

### 1.4 The Conceptual Shift: From Decoherence to Multiplicity

The reframing this paper develops is not a refinement of the standard quantum-computing picture; it is a substitution at the level of which substrate quantity is the load-bearing variable.

In the standard picture, *decoherence* is the central object — a coupling-rate between a quantum state and its environment, to be reduced by isolation engineering, dynamical decoupling, error-correcting codes, and similar techniques. Coherence times are explained by where the coupling-rate sits; scaling limits are explained by where the coupling-rate becomes irreducible.

In the substrate picture developed here, *multiplicity* is the central object — a substrate-state quantity that counts available ED-gradient pathways, with low-multiplicity regions admitting the unresolved-rule regime that quantum computation requires and high-multiplicity regions forcing individuation. Decoherence in the standard sense is the *coarse-grained signature* of substrate-level individuation events firing at endpoints whose multiplicity has risen above a substrate-determined threshold. The standard variable is real but downstream; the substrate variable is upstream and structurally prior.

This framework replaces the standard decoherence-centric view with a substrate-level multiplicity-centric account, unifying matter-wave interference, superconducting qubits, Josephson-junction devices, topological qubits, multi-timescale photonic platforms, and redundancy-based bosonic codes under a single substrate mechanism — the multiplicity-cap function $M$. The reframing has direct implications for how quantum-computing scaling limits are interpreted and pursued: limits that appear in the standard picture as engineering accidents (residual environmental couplings, fabrication imperfections, correlated noise channels) appear in the substrate picture as substrate-determined structural ceilings whose locations are constrained by the cross-platform identity of $M$.

The paper does not claim that engineering effort is misdirected — engineering against the substrate-level binding constraints is exactly the right work in the appropriate regime. It claims that the *interpretive frame* under which engineering progress is evaluated is shifted: progress against substrate-level walls is structurally bounded; progress that addresses non-binding constraints is wasted; and the cross-platform identity of substrate-level walls means that progress in one domain (e.g., matter-wave-interferometry mass-cap measurement) directly constrains what is achievable in another (e.g., superconducting-qubit system-multiplicity scaling).

### 1.5 Structure of the Paper

Section 2 develops the substrate primitives and DCGT machinery. Section 3 derives UR-1. Section 4 quantifies failure-mode rates. Section 5 audits the three architectural classes for substrate-level exhaustiveness. Section 6 constructs the multiplicity-cap function $M$. Section 7 delivers cross-platform unification and predictive content. Section 8 provides FORCED / INHERITED / OPEN classification. Section 9 is discussion and implications. Appendices and metadata follow.

---

## 2. Substrate Primitives and DCGT Machinery

### 2.1 Participation Density and Gradients

The substrate's load-bearing scalar field is the local participation density $\rho(\mathbf{x})$, defined as the density of viable participation-channel slots per coarse-graining cell of size $R_{\mathrm{cg}}$. Gradients $\nabla\rho$ encode spatial variation. The dimensionless ratio
$$
\sigma(\mathbf{x}) \equiv \frac{|\nabla\rho|\,\ell_P^2}{\rho_{\mathrm{local}}}
$$
measures the substrate-scale steepness of $\rho$ at the Planck length $\ell_P$. This is the load-bearing substrate quantity for cross-bandwidth derivation in Arc D and for the present arc's condition (ii) analysis.

### 2.2 V1 Finite-Width Kernel

The V1 vacuum kernel, established in Theorem N1 (April 2026) and refined in Theorem 18 (April 2026), is the finite-width temporal smearing kernel that mediates substrate participation events. Its width sets the temporal resolution of commitment events at a region. V1 carries the kernel-level arrow of time (Theorem 18): the kernel is forward-cone-only, propagating substrate correlations forward in P11-time only.

### 2.3 Multi-Scale Expansion and the Hydrodynamic Window

DCGT (Diffusion Coarse-Graining Theorem, Arc D, April 2026) establishes a hydrodynamic-window scale separation
$$
\ell_P \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}
$$
under which substrate dynamics admit a multi-scale expansion to coarse-grained continuum equations. DCGT supplies the cross-bandwidth structure used throughout this paper.

### 2.4 Cross-Bandwidth and Sparsity

For two adjacent substrate regions separated by a pathway of length $L$ along which $\sigma$ varies, the cross-bandwidth is
$$
\Gamma_{\mathrm{cross}}(\mathbf{x}_1, \mathbf{x}_2) \sim \exp\!\left[-\alpha\!\int_{\mathrm{path}}\sigma(\mathbf{x})\,d\ell\right]
$$
with $\alpha$ a substrate-determined dimensionless prefactor. The exponential structure is forced by the multi-scale expansion: large $|\nabla\rho|$ at the substrate scale creates steep barriers to participation-channel mediation between adjacent regions. This is the same machinery that produces the BH-2 horizon-formation condition (Arc BH, 2026-05-01); here it is applied at engineered-system scale rather than gravitational-collapse scale.

### 2.5 Multiplicity and the ED-Entropy Analogue

Per ED-I-01, multiplicity is the ED-substrate analogue of entropy. A region with high $\mathcal{M}$ supports many distinct participation pathways; ED-flow can branch, scatter, and decohere across them. A region with low $\mathcal{M}$ supports few distinct pathways; ED-flow is constrained. Symmetry, in ED, is not geometric ornamentation but a *reduction* in the number of distinct ED-gradient configurations the system can occupy. Decoherence is re-entry into high-multiplicity participation: when a system's substrate environment proliferates gradient pathways, the system's identity individuates to one of them.

This identification is load-bearing for the architectural classification in Section 5.

### 2.6 Commitment-Irreversibility (P11)

P11 is the substrate primitive that participation events, once committed, cannot be uncommitted. Commitment is the moment a chain "becomes" something it wasn't a moment before. P11 is the only direction-bearing substrate primitive in ED; every other primitive (V1 kernel, participation density, cross-bandwidth) is time-symmetric in isolation. The kernel-level arrow of time (Theorem 18) propagates from P11 through the V1 kernel to produce forward-cone-only causal structure at substrate level.

For QC: P11 fires every time the system commits a participation event — every gate operation, every ancilla reset, every measurement, every internal scattering event. The cumulative commitment density inside a system bounds how long the unresolved-rule regime can be held.

---

## 3. UR-1: The Unresolved-Regime Characterization Theorem

### 3.1 The Functional Form of $\mathcal{U}$

Define $\mathcal{U}(\mathcal{S},t) \in [0,1]$ as the integrity of an unresolved participation rule across the designated endpoints of substrate region $\mathcal{S}$ at substrate time $t$: $\mathcal{U} \to 1$ when the rule remains globally coherent across all endpoints (no individuation has occurred); $\mathcal{U} \to 0$ when full individuation has been reached.

Three substrate processes can degrade $\mathcal{U}$, each from a structurally distinct substrate quantity. They compose multiplicatively, because any one alone destroys $\mathcal{U}$ regardless of the others:
$$
\mathcal{U}(\mathcal{S},t) = \prod_{i \in \mathrm{endpts}(\mathcal{R})} \mu\!\left(\frac{\mathcal{M}_i(t)}{\mathcal{M}_{\mathrm{crit}}}\right) \cdot \prod_{(i,j) \in \mathcal{R}} \kappa\!\left(\frac{\gamma_{ij}(t)}{\Gamma_{\mathrm{min}}}\right) \cdot \exp\!\left[-\int_0^t \Lambda_{S}(t')\,dt'\right].
$$

The three factors correspond, in order, to *multiplicity headroom*, *rule-spanning connectivity*, and *commitment-survival*.

The form is **FORCED** by substrate machinery:

- $\mu, \kappa : [0,\infty) \to [0,1]$ are monotone functions. $\mu$ decreasing from 1 to 0 (more multiplicity = less unresolvedness preservation); $\kappa$ increasing from 0 to 1 (more cross-bandwidth = better rule-spanning). Specific shapes (Boltzmann, rational, sigmoid) are **INHERITED** from V1-kernel + DCGT closed-form details.
- The exponential survival factor is forced by the Poisson-class structure of P11 commitment events: if $\Lambda_{S}(t')$ is the local rate of individuation-driving commitments, the probability that no such event has fired in $[0,t]$ is exactly $\exp[-\int \Lambda dt']$.
- $\mathcal{R}$ is the set of endpoint-pairs across which the participation rule spans. $\mathcal{M}_{\mathrm{crit}}$ and $\Gamma_{\mathrm{min}}$ are substrate-determined critical thresholds, INHERITED.

### 3.2 The UR-1 Theorem

> **UR-1 (Unresolved-Regime Characterization Theorem).** Let $\mathcal{S}$ be a substrate region with designated participation-rule relation set $\mathcal{R}$ over endpoints $\{e_1, \ldots, e_n\}$. Let $\mathcal{U}_{\mathrm{min}} \in (0,1)$ be a target unresolvedness threshold. Then $\mathcal{U}(\mathcal{S},t) \geq \mathcal{U}_{\mathrm{min}}$ holds at substrate time $t$ if and only if:
>
> **(i) Multiplicity bounded.** $\mathcal{M}_i(t) \leq \mathcal{M}_{\mathrm{crit}}^{(\mu^{-1}(\mathcal{U}_{\mathrm{min}}^{1/n}))}$ for every endpoint $e_i$.
>
> **(ii) Cross-endpoint connectivity sustained.** $\gamma_{ij}(t) \geq \Gamma_{\mathrm{min}} \cdot \kappa^{-1}(\mathcal{U}_{\mathrm{min}}^{1/|\mathcal{R}|})$ for every pair $(i,j) \in \mathcal{R}$.
>
> **(iii) Commitment-injection bounded.** $\int_0^t \Lambda_{S}(t')\,dt' \leq \ln(1/\mathcal{U}_{\mathrm{min}}) - C_{(\mathrm{i})} - C_{(\mathrm{ii})}$, where $C_{(\mathrm{i})}, C_{(\mathrm{ii})}$ are negative-log deficits from conditions (i) and (ii).
>
> Each condition is independently necessary. Failure of any one drives $\mathcal{U}$ below $\mathcal{U}_{\mathrm{min}}$ at a substrate-determined rate. The conditions are coupled through substrate geometry (substrate configurations cannot independently dial all three), but each can fail without the others.

### 3.3 Reduction to Known Regimes

Three known regimes recover from UR-1, each with a different binding condition:

**Bulk superconductor (ED-I-01).** Lattice symmetry collapses local multiplicity to $\mathcal{M} \approx 1$ across the bulk; $\sigma$ is smooth, $\gamma_{ij}$ high. Below $T_c$, condition (iii) holds with margin: thermal ED-injection rate is below the substrate individuation threshold. Above $T_c$, thermal agitation overwhelms the symmetry-locking; condition (iii) crosses threshold; $\mathcal{U}$ drops; resistance reappears. **$T_c$ is identified as the substrate temperature at which condition (iii) crosses its threshold.**

**Josephson junction (ED-I-23).** Two low-$\mathcal{M}$ SC electrodes separated by a thin insulating barrier. (i) holds in both electrodes; (iii) holds with adequate isolation. Condition (ii) is the load-bearing constraint by design: the barrier is engineered such that $\gamma_{LR}$ is just above $\Gamma_{\mathrm{min}}$. **JJ MQT (Devoret-Martinis-Clarke 1985) corresponds to dynamical fluctuations at the (ii) boundary** — the rule globally reconfigures across the gap when $\gamma_{LR}$ momentarily drops below threshold. The MQT rate's WKB exponential structure is recovered directly from DCGT $\kappa$-function evaluation:
$$
\tau_{\mathrm{MQT}}^{-1} \sim \omega_0\,\exp\!\left[-\alpha\!\int_{\mathrm{barrier}}\sigma\,d\ell\right].
$$

**Free atomic-scale matter wave.** The molecule is itself a low-$\mathcal{M}$ ED-object whose internal $\mathcal{M}$ scales with mass (rotational + vibrational + electronic DOF activation). For low molecular mass, $\mathcal{M} \ll \mathcal{M}_{\mathrm{crit}}$ and (i) holds. For high mass, internal $\mathcal{M}$ rises; at the Q-C boundary ($M_\star \sim 140$–$250$ kDa empirically), internal $\mathcal{M}$ crosses $\mathcal{M}_{\mathrm{crit}}$. **The matter-wave Q-C boundary is identified as the molecular mass at which condition (i) crosses threshold.**

Three different empirical phenomena, three different UR-1 conditions, one substrate framework.

---

## 4. Failure-Mode Rates and the QC Operating Window

Each UR-1 condition admits a substrate-level dynamical equation governing the timescale at which it crosses threshold.

### 4.1 Condition (i): Multiplicity Dynamics

$$
\frac{d\mathcal{M}}{dt}\bigg|_{S} = \alpha_{\mathrm{env}}\,\Lambda_{\mathrm{env}}(t) + \alpha_{\mathrm{act}}\,S_{\mathrm{int}}(t) - A_{S}\,(\mathcal{M} - \mathcal{M}_{\mathrm{floor}})
$$

with:

- $\alpha_{\mathrm{env}}\,\Lambda_{\mathrm{env}}$: environmental ED-injection driving pathway-count growth.
- $\alpha_{\mathrm{act}}\,S_{\mathrm{int}}$: internal pathway-activation rate from thermal or operational stimulation.
- $A_{S}\,(\mathcal{M} - \mathcal{M}_{\mathrm{floor}})$: architectural restoring rate, returning $\mathcal{M}$ to the architecturally-imposed floor $\mathcal{M}_{\mathrm{floor}}$.

Two failure modes:

- **Static failure:** $\mathcal{M}_{\mathrm{floor}} \geq \mathcal{M}_{\mathrm{crit}}$. The system cannot be operated regardless of timescale. $\tau_{(\mathrm{i})} = 0$. *This is the matter-wave Q-C boundary regime.*
- **Dynamic failure:** $\mathcal{M}_{\mathrm{floor}} < \mathcal{M}_{\mathrm{crit}}$ but environmental injection drives steady-state above threshold. Finite $\tau_{(\mathrm{i})}$ set by net multiplicity-growth rate after architectural restoring.

### 4.2 Condition (ii): Cross-Bandwidth Dynamics

$$
\frac{d\gamma_{ij}}{dt} = -\frac{1}{\tau_{\mathrm{dec}}^{(\mathrm{ii})}}(\gamma_{ij} - \gamma_{\mathrm{floor}}) + \xi(t)
$$

with $\gamma_{\mathrm{floor}}$ the architecturally-supported steady-state and $\xi(t)$ stochastic substrate perturbation.

Two regimes:

- **Sustained-above-threshold:** $\gamma_{\mathrm{floor}} > \Gamma_{\mathrm{min}}$ with margin. $\tau_{(\mathrm{ii})}$ is exponentially long via Kramers-class escape from the protected configuration. *SC qubit T₂ regime.*
- **Near-threshold:** $\gamma_{\mathrm{floor}} \approx \Gamma_{\mathrm{min}}$, by architectural design (Josephson junction). Fluctuations frequently push below threshold; each crossing produces a global rule reconfiguration. **WKB MQT structure recovered directly from DCGT.**

### 4.3 Condition (iii): Commitment-Injection Dynamics

$$
\tau_{(\mathrm{iii})} = \frac{\ln(1/\mathcal{U}_{\mathrm{min}}^{(\mathrm{iii})})}{\Lambda_{\mathrm{env}} + \Lambda_{\mathrm{int}}}.
$$

$\Lambda_{\mathrm{env}}$ has additive contributions from thermal radiation, residual-gas collisions, Purcell decay, dielectric noise, magnetic-flux fluctuations, quasiparticle injection. Bounded below by V1 vacuum kernel residual. $\Lambda_{\mathrm{int}}$ from intentional + incidental commitment events.

### 4.4 The QC Operating Window

The QC operating window is the substrate time over which all three UR-1 conditions simultaneously hold:

$$
\boxed{\;\tau_{\mathrm{QC}}(\mathcal{S}, \mathcal{E}) = \min\!\left[\tau_{(\mathrm{i})}, \tau_{(\mathrm{ii})}, \tau_{(\mathrm{iii})}\right].\;}
$$

Three structural observations.

**Different architectures bind on different conditions.** An architectural class is characterized not by which timescale is longest but by which is shortest — i.e., which UR-1 condition is the architecture's binding constraint.

**The operating window is a substrate observable.** $\tau_{\mathrm{QC}}$ corresponds to what experimentalists call coherence time, T₁/T₂, fault-tolerance-headroom, or maximum coherent flight time. Cross-platform measurements are evaluations of $\tau_{\mathrm{QC}}$ for different binding conditions.

**Architectural design is the optimization of $\min(\cdot)$.** Improving the longest of three timescales is irrelevant; only improvement of the binding constraint extends the window. The substrate provides the structural reason for what platform-development teams empirically know.

### 4.5 Cross-Anchor Reductions

| Phenomenon | Binding condition | Substrate identification |
|---|---|---|
| Matter-wave Q-C boundary 140–250 kDa | (i) static failure | $\mathcal{M}_{\mathrm{floor}}(M_\star) = \mathcal{M}_{\mathrm{crit}}$ |
| SC qubit T₁ | (iii) | $\Lambda_{\mathrm{env}}$ Purcell + dielectric + quasiparticle |
| SC qubit T₂ | (ii) | Kramers escape from protected pathway |
| JJ MQT | (ii) near-threshold | WKB $\sim \omega_0\exp[-\alpha\int\sigma\,d\ell]$ |
| Topological-qubit error suppression | (iii) gap-suppressed | Most env modes don't couple to protected rule |
| Multi-timescale FPM relaxation (Hafezi 2025) | (i) relaxed by redundancy | Multi-axis pathway expansion |
| Quasiparticle poisoning | multi-condition (i)+(iii) | Single event raises $\mathcal{M}$ and $\Lambda$ |

---

## 5. Architectural-Class Taxonomy and Exhaustiveness

Three substrate-allowed protection strategies emerge as the base over UR-1's three conditions.

### 5.1 Class A — Engineered-Low-Multiplicity

**Protection target:** condition (i). The architecture commits structurally to suppressing local multiplicity via lattice symmetry, engineered ED-bottleneck, deep confinement, or mode engineering.

**Substrate mechanism.** A bulk superconductor's lattice symmetry collapses $\mathcal{M}$ to ≈ 1 (ED-I-01); a Josephson junction's barrier imposes a sparsity-bottleneck enforcing non-individuation across the gap (ED-I-23); a deeply trapped ion occupies a low-$\mathcal{M}$ region of substrate; a single-photon mode in a linear-optical circuit has minimum-channel multiplicity (ED-I-13).

**Suppression of non-target conditions.** (ii) handled by engineering low-$\sigma$ corridors between qubit endpoints; (iii) by isolation engineering (dilution refrigerators, ultra-high vacuum, low-loss substrates, magnetic shielding).

**Binding constraint.** Typically (ii) or (iii) — environmental coupling channels reach through the engineered isolation. T₁ and T₂ for SC qubits are the empirical binding.

**Examples:** Transmon and fluxonium SC qubits; trapped-ion qubits; gate-model photonic qubits; matter-wave-interferometry molecules.

### 5.2 Class B — Global-Geometric-Rigidity

**Protection target:** condition (ii). The architecture encodes the participation rule in *global ED-channel geometry* — topological invariants that cannot be perturbed by local environmental injection.

**Substrate mechanism.** Topological phases (Aharonov-Bohm, Berry, Aharonov-Casher) are global invariants of multiply-connected ED-channels with nontrivial curvature (ED-I-14). Photonic Chern channels carry information through edge-states that remain edge-localized under perturbation by virtue of topological gradient-rigidity (ED-I-12, ED-I-18 §7). Anyonic platforms exploit ED-I-14's degeneracy-sourced parameter-space curvature to produce phase shifts depending on holonomy of parameter loops, not on local rates.

**Suppression of non-target conditions.** (i) gap-suppressed: $\mathcal{M}_{\mathrm{floor}}$ in the protected sector held low by gap structure. (iii) gap-suppressed: most environmental modes don't couple to the rule because it's encoded in global geometry; $\Lambda_{\mathrm{env}}$ for protected subspace is exponentially suppressed in $\Delta_{\mathrm{top}}$.

**Binding constraint.** Topology-perturbation rate $\tau_{\mathrm{gap-stab}}(\mathcal{T})$ — gap-closing events, edge-state hybridization with bulk modes, anyonic non-Abelian braiding errors. Structurally distinct from Class A: limit is set by macroscopic substrate quality, not local environmental rate.

**Examples:** Majorana-class topological qubits; photonic Chern edge-state channels; geometric-phase quantum gates.

### 5.3 Class C — High-Multiplicity-Redundancy

**Protection target:** $\mathcal{U}$ via redundancy of pathways. Condition (i) is **relaxed by architectural design** — high $\mathcal{M}$ is permitted because the rule's integrity survives via parallel-pathway redundancy.

**Substrate mechanism.** The architecture configures multiple parallel ED-channels carrying the same participation rule. Single-pathway failure leaves the rule intact across surviving pathways. ED-I-18 establishes this for multi-timescale photonic lattices: a single-ring resonator is a low-$\mathcal{M}$ object with strict frequency-phase matching (FPM); a multi-timescale lattice expands ED-multiplicity along multiple axes and FPM relaxes from a sharp condition to a region with 100% device yield, two-octave bandwidth, and disorder tolerance.

**Suppression of non-target conditions.** Effective $\Gamma_{\mathrm{cross}}$ enhanced by multiple parallel pathways; effective $\Lambda$ for protected information distinct from $\Lambda$ for any single mode.

**Binding constraint.** Correlated errors across redundant pathways exceeding the *correlation budget* $N_{\mathrm{corr}}$ — common-mode noise, shared substrate defects, optical-mode crosstalk. Saturation is structural: beyond $N_{\mathrm{corr}}$, redundancy stops paying.

**Examples:** Hafezi multi-timescale photonic lattices; bosonic codes (cat states, GKP); generalized multi-axis architectures.

### 5.4 Exhaustiveness Argument

The three classes exhaust the substrate-level base protection strategies:

1. UR-1 has three conditions, set by three substrate quantities ($\mathcal{M}, \sigma$/$\gamma_{ij}, \Lambda$).
2. Two of these are *fixable structurally* — $\mathcal{M}$ via local simplification (Class A); $\sigma$ via global topological invariants (Class B). $\Lambda$ is not directly fixable structurally because it is intrinsically a coupling-rate at the boundary between protected region and environment; reducing $\Lambda$ is achieved as a *consequence* of the other classes' mechanisms.
3. The third strategy is *indirect* — provide redundancy so $\mathcal{U}$ survives partial failures (Class C).
4. No fourth substrate-level base strategy: only three substrate quantities, only two structurally fixable, redundancy provides the third option.

### 5.5 Meta-Architectures: Compositions and Techniques

Real systems are typically *compositions* of A/B/C, not pure single-class instances. A fault-tolerant SC quantum computer is Class A at the physical-qubit level, Class C in the logical encoding (e.g., surface code), with active restoring at the logical level (syndrome-guided correction). Hybrids (SC-photonic interconnects, topological-SC platforms) are A/B/C subsystems with substrate-geometric handoff boundaries.

Four techniques considered as Class D candidates and rejected:

- **Dynamical decoupling.** Reduces effective $\Lambda$ via temporal averaging. *Technique* for Class A.
- **Reservoir-engineered unresolvedness** (Mirrahimi-Devoret cat states). Implements $A_{S}$ restoring via structured environmental coupling. *Technique* for Class A.
- **Error-correction-as-architecture.** Class C encoding + Class A active restoring at logical level. *Meta-architecture composing existing classes.*
- **Hybrid systems.** *Compositions* of A/B/C across subsystems.

None introduces a fourth substrate-state quantity to fix.

---

## 6. The Multiplicity-Cap Function $M$

### 6.1 The Unified Function

$M$ is constructed as one substrate object with three architectural-class projections:

$$
\boxed{\;M(\mathcal{S}, K, \mathcal{E}, \mathcal{O}) = \min\!\left[\tau_{(\mathrm{i})}^{(K, \mathcal{O})}, \tau_{(\mathrm{ii})}^{(K, \mathcal{O})}, \tau_{(\mathrm{iii})}^{(K, \mathcal{O})}\right]\;}
$$

with inputs:
- System $\mathcal{S}$ (protected region's configuration, endpoints, $\mathcal{M}_{\mathrm{floor}}$, $\gamma_{\mathrm{floor}}$, redundancy count).
- Class $K \in \{A, B, C\}$.
- Environment $\mathcal{E}$ ($\Lambda_{\mathrm{env}}$, perturbation rates, temperature).
- Meta-architecture overlay $\mathcal{O}$ (dynamical decoupling, reservoir engineering, error correction, hybrid composition — any combination).

Each $\tau_j^{(K,\mathcal{O})}$ is evaluated using the rate equation from Section 4 with class-specific protection-mechanism modifiers.

### 6.2 Class A Projection $M_A$

$$
\tau_{(\mathrm{i})}^{(A)} = \begin{cases}
\dfrac{\mathcal{M}_{\mathrm{crit}} - \mathcal{M}_{\mathrm{floor}}(\mathcal{S})}{\dot{\mathcal{M}}_{\mathrm{eff}}^{(A)}} & \text{if } \mathcal{M}_{\mathrm{floor}}(\mathcal{S}) < \mathcal{M}_{\mathrm{crit}} \\[4pt]
0 & \text{if } \mathcal{M}_{\mathrm{floor}}(\mathcal{S}) \geq \mathcal{M}_{\mathrm{crit}} \quad\text{(static failure)}
\end{cases}
$$

$$
\tau_{(\mathrm{ii})}^{(A)} = \tau_{\mathrm{dec}}^{(\mathrm{ii})}\,\exp\!\left[\frac{(\gamma_{\mathrm{floor}}^{(A)} - \Gamma_{\mathrm{min}})^2}{2\sigma_\xi^2}\right]
$$

For JJ at engineered (ii) boundary: $\tau_{(\mathrm{ii})}^{(A,\mathrm{JJ})} \approx \omega_0^{-1}\exp[+\alpha\int_{\mathrm{barrier}}\sigma\,d\ell]$ — WKB MQT structure.

$$
\tau_{(\mathrm{iii})}^{(A)} = \frac{\ln(1/\mathcal{U}_{\mathrm{min}})}{\Lambda_{\mathrm{env}}^{(A)}(\mathcal{E}) + \Lambda_{\mathrm{int}}^{(A)}(\mathcal{S})}.
$$

### 6.3 Class B Projection $M_B$

$$
\tau_{(\mathrm{i})}^{(B)} = \tau_{(\mathrm{i})}^{\mathrm{trivial}}\cdot\exp(\Delta_{\mathrm{top}}/T_{\mathrm{eff}})
$$

$$
\tau_{(\mathrm{ii})}^{(B)} = \tau_{\mathrm{gap-stab}}(\mathcal{T})
$$

$$
\tau_{(\mathrm{iii})}^{(B)} = \frac{\ln(1/\mathcal{U}_{\mathrm{min}})}{\Lambda_{\mathrm{env}}^\mathrm{baseline}\cdot\exp(-\Delta_{\mathrm{top}}/T_{\mathrm{eff}})}
$$

Binding shifted from environmental rate to topology-perturbation rate $\tau_{\mathrm{gap-stab}}(\mathcal{T})$, set by macroscopic substrate quality. For Majorana platforms with $\Delta_{\mathrm{top}} \sim 0.1$ meV at $T_{\mathrm{eff}} \sim 20$ mK: gap factor $\sim e^{58} \sim 10^{25}$.

### 6.4 Class C Projection $M_C$

Three redundancy modifiers apply to the base rates:

- **Effect 1:** $\mathcal{M}^{\mathrm{eff}}(\mathcal{S}) = \mathcal{M}_{\mathrm{floor}}(\mathcal{S})\cdot g(N)$ with $g(N) \to 0$ as $N \to \infty$.
- **Effect 2:** $\gamma_{\mathrm{eff}}^{(C)} = \gamma_{\mathrm{floor}}\cdot h(N)$ with $h(N) > 1$ for $N > 1$.
- **Effect 3:** $\Lambda^{\mathrm{eff}}_{(C)}(N) = \Lambda^{\mathrm{single}}\cdot c(N)$ with $c(N) \sim \exp(-N/N_{\mathrm{corr}})$ for $N \ll N_{\mathrm{corr}}$, saturating at $N \gtrsim N_{\mathrm{corr}}$.

Form FORCED for all three; specific shapes INHERITED from the substrate-coupling pattern across $N$ pathways.

Class C ceiling: $\tau_{\mathrm{QC}}^{C,\mathrm{ceil}} = \tau_{\mathrm{QC}}^{\mathrm{single}}\cdot e$ asymptotically. **Class C is bounded-redundancy-advantage** — it cannot exceed single-pathway ceilings without bound; its role is extending the useful operating window before saturation and mitigating disorder/fabrication variations.

### 6.5 Meta-Architectural Overlays

Meta-architectures appear as boundary-condition modifiers, not new projections:

- **Dynamical decoupling.** Replaces $\Lambda_{\mathrm{env}}^{(K)}$ with temporally-averaged $\Lambda_{\mathrm{env}}^{\mathrm{DD}}(\omega_{\mathrm{decoup}})$.
- **Reservoir engineering.** Increases $A_{S}$ in the multiplicity dynamics.
- **Error correction.** Recursive overlay: $\tau_{\mathrm{QC}}^{\mathrm{logical}}$ derived from $\tau_{\mathrm{QC}}^{\mathrm{phys}}$ via code distance + threshold.
- **Hybrid composition.** $\min$ over subsystems' projections + handoff losses.

---

## 7. Cross-Platform Unification and Predictive Content

### 7.1 The Matter-Wave / Qubit-System Identity

The matter-wave Q-C boundary at 140–250 kDa and qubit-system multiplicity walls are **the same boundary projected onto two platforms**. Both arise from $\mathcal{M}_{\mathrm{floor}}^{(A)}(\mathcal{S}) = \mathcal{M}_{\mathrm{crit}}$ — the static-failure branch of the Class A $\tau_{(\mathrm{i})}$ projection.

| Platform | $\mathcal{S}$ | $f_{\mathrm{sys}}^{(A)}(\mathcal{S})$ scaling parameter | Q-C boundary |
|---|---|---|---|
| Matter-wave | molecule of mass $M_{\mathrm{mol}}$ | molecular internal-DOF activation $f_{\mathrm{int}}(M_{\mathrm{mol}})$ | 140–250 kDa (empirical) |
| SC qubit array | $N$-qubit register | cross-qubit pathway count $f_{\mathrm{xy}}(N_{\mathrm{qubits}}, \mathrm{architecture})$ | $N_\star$ qubits (INHERITED) |
| Trapped-ion array | $N$-ion crystal | inter-ion + motional-mode coupling | analogous $N_\star$ |
| Photonic gate-model | photonic-mode register | mode-coupling pathway count | analogous $N_\star$ |

**Sharp cross-platform claim:** the matter-wave boundary value (140–250 kDa), calibrated against $\mathcal{M}_{\mathrm{crit}}$, fixes the substrate-determined cap on Class A platforms across all instantiations. Sharper measurement of the matter-wave boundary directly constrains the system-multiplicity wall location for Class A qubit platforms via the substrate-level identity. Qubit-platform $N_\star$ values are not independent free parameters — they are determined (up to architecture-specific calibration) by the matter-wave anchor.

This is the kind of cross-platform consistency that distinguishes substrate-level frameworks from phenomenological assemblies.

### 7.2 Class-Specific Scaling Laws and Ceilings

**Class A.** System-multiplicity wall: as $f_{\mathrm{sys}}^{(A)}(\mathcal{S}) \to \mathcal{M}_{\mathrm{crit}}$, $\tau_{(\mathrm{i})}^{(A)} \to 0$ regardless of environmental engineering. Improving isolation, dynamical decoupling, or any environmental-side technique cannot push past this wall. *Form FORCED; wall location INHERITED.*

**Class B.** Exponential coherence enhancement by $\exp(\Delta_{\mathrm{top}}/T_{\mathrm{eff}})$ over Class A; binding shifted to topology-perturbation rate. Engineering effort that improves $\Delta_{\mathrm{top}}$ or topology stability produces exponential improvements; effort that improves isolation in the Class A sense produces diminishing returns. *Form FORCED; max gap and stability INHERITED.*

**Class C.** Correlation-budget plateau: exponential improvement for $N \ll N_{\mathrm{corr}}$, saturation at $\sim e\cdot\tau^{\mathrm{single}}$ for $N \gtrsim N_{\mathrm{corr}}$. Bounded-redundancy-advantage. *Form FORCED; $N_{\mathrm{corr}}$ INHERITED.*

### 7.3 Cross-Class Architectural Transitions

**Class A → Class C is mandatory at the wall.** When $f_{\mathrm{sys}}^{(A)}(\mathcal{S}) \to \mathcal{M}_{\mathrm{crit}}$, the only path past the wall is to *accept* high physical-level $\mathcal{M}$ and use redundancy to maintain logical-level $\mathcal{U}$. Sharp prediction: a SC-only architecture without logical encoding will plateau in effective $\tau_{\mathrm{QC}}^{\mathrm{logical}}$ before reaching the engineering frontier of physical-qubit count, even with continued T₁/T₂ improvements.

**Class B overtakes Class A at $\Delta_{\mathrm{top}}/T_{\mathrm{eff}} \gtrsim 10$–20.** For $T_{\mathrm{eff}} \sim 20$ mK, gaps $\gtrsim 0.5$–1 meV with stable topology on millisecond timescales would push Class B past current Class A coherence times by orders of magnitude.

**Class C saturation at $N \sim N_{\mathrm{corr}}$.** Hafezi-class platforms scaling beyond ~3–5 timescale axes will show diminishing returns. Bosonic codes scaling beyond a code-distance threshold will exhibit saturation due to correlated photon-loss.

### 7.4 Falsifiable Predictions and Near-Term Experimental Tests

**Test 1 — Coherence-scaling experiments (Class A wall).** Measure $\tau_{\mathrm{QC}}^{\mathrm{logical}}$ in scaled SC qubit systems vs $N_{\mathrm{qubits}}$ at fixed code distance, with continued T₁/T₂ engineering. Predicted plateau as $f_{\mathrm{xy}}(N_{\mathrm{qubits}})$ approaches $\mathcal{M}_{\mathrm{crit}}$. Continued unbounded improvement past the projected wall would refute.

**Test 2 — Multiplicity-growth probes.** Mass-matched molecular isomers with different DOF structure for matter waves; cross-qubit pathway tomography for qubit systems. Tests whether contrast/coherence scales with substrate-level $\mathcal{M}^{\mathrm{system}}$, not directly with mass/qubit-count.

**Test 3 — Topology-perturbation thresholds (Class B).** Measure $\tau_{\mathrm{QC}}$ in topological qubits as a function of $\Delta_{\mathrm{top}}$ and temperature. Predicted exponential dependence on $\Delta_{\mathrm{top}}/T_{\mathrm{eff}}$. Polynomial dependence would refute.

**Test 4 — Redundancy-saturation signatures (Class C).** Extend Hafezi-class to higher axis counts; scale bosonic-code distance. Predicted plateau emerges. Continued monotonic improvement past projected saturation would refute.

### 7.5 Decisive Falsifier of the Framework

The arc's central falsifier: identification of a platform whose coherence behavior is consistent with no class assignment in {A, B, C}, cannot be explained as meta-architectural composition, and fails to match $M$ under any substrate-allowed parameter calibration. Such a platform forces introduction of a Class D (refuting Section 5's exhaustiveness) or replacement of the framework. Conversely, continued cross-anchor consistency over the next decade of platform development is significant cross-platform evidence for the substrate framework.

---

## 8. FORCED / INHERITED / OPEN Classification

### FORCED (substrate-level form)

- UR-1 as necessary-and-sufficient characterization of the unresolved regime.
- Three-factor product structure of $\mathcal{U}$.
- $\min(\cdot)$ structure of $\tau_{\mathrm{QC}}$.
- Substrate-level dynamics of multiplicity, cross-bandwidth, and commitment-rate.
- Static-failure branch of $\tau_{(\mathrm{i})}$ at $\mathcal{M}_{\mathrm{floor}} = \mathcal{M}_{\mathrm{crit}}$.
- WKB-form exponential structure of MQT recovered from DCGT.
- Three-class architectural exhaustiveness.
- Meta-architectural overlay structure as modifiers, not new classes.
- Multiplicity-cap function $M$ as one substrate object with three projections.
- Exponential gap-suppression in Class B by $\exp(\Delta_{\mathrm{top}}/T_{\mathrm{eff}})$.
- Correlation-budget plateau in Class C; bounded redundancy advantage.
- Cross-platform unification: matter-wave Q-C boundary and qubit-system walls are one phenomenon.
- Three cross-class architectural transitions.
- Cross-domain echo with BH-2 ($\Gamma_{\mathrm{cross}}$ collapse mechanism).

### INHERITED (value-level)

- $\mathcal{M}_{\mathrm{crit}}$, $\Gamma_{\mathrm{min}}$, $\Lambda_{\mathrm{V1}}$ — substrate constants.
- Specific functional shapes of $\mu, \kappa, g, h, c$.
- Matter-wave Q-C boundary location (140–250 kDa).
- Architecture-specific $f_{\mathrm{sys}}^{(A)}$ scaling functions.
- Specific values of $N_\star$ for any qubit platform.
- Maximum stable topological gap $\Delta_{\mathrm{top}}^{\max}$, minimum substrate-equivalent temperature $T_{\mathrm{eff,\min}}$.
- Specific $N_{\mathrm{corr}}$ for any Class C platform.
- Specific cross-class transition thresholds (numerical).

### OPEN (future arcs)

- **O-QC-1:** Closed-form $\mathcal{M}_{\mathrm{crit}}$ from V1 kernel + ED-I-01 substrate constants. Structurally similar in difficulty to closed-form $\log g$ (BH-5).
- **O-QC-2:** Architecture-to-platform calibration program — map $\mathcal{M}_{\mathrm{floor}}^{(A)}(\mathcal{S})$ for canonical platforms; predict $N_\star$ values.
- **O-QC-3:** Closed-form $g, h, c(N)$ for Class C from extended DCGT.
- **O-QC-4:** Topology-stability theorem for Class B; substrate-level account of $\tau_{\mathrm{gap-stab}}(\mathcal{T})$.
- **O-QC-5:** Surface-code logical-qubit recursive-overlay derivation.
- **O-QC-6:** Hybrid-architecture handoff dynamics.

---

## 9. Discussion and Implications

### 9.1 Relation to Standard QC Theory

ED's substrate-level account does not predict that current quantum-computing experiments will give different numerical answers than standard QC theory predicts. SC qubit T₁/T₂ measurements will continue to look as they do; matter-wave interferometry will continue to lose coherence at the molecular masses it does; topological-qubit progress will continue to be paced by topology engineering. What changes is the *story underneath*: the question of why a particular platform hits a particular wall has a substrate-level structural answer, and the cross-platform identity of those walls is now visible.

### 9.2 Why ED Doesn't Solve QC Engineering — and That Is the Point

This paper does not deliver a constructive recipe for building a fault-tolerant quantum computer. The arc is structural, not engineering. What it does deliver is a framework in which engineering questions become substrate-resolvable:

- *Is there a hard wall on SC qubit scaling?* Yes, at the system-multiplicity boundary; same boundary as the matter-wave Q-C boundary.
- *Will adding more redundancy axes keep paying?* No, past the correlation budget; bounded-redundancy-advantage is structural.
- *Can topological qubits exceed SC coherence by a lot?* Yes in principle, by exponential factors; bound is topology engineering, not isolation.
- *Is error correction a different kind of solution from physical-qubit engineering?* No, it is a meta-architectural composition of the existing classes at logical level.

These answers are substrate-grounded, not phenomenological inferences from existing data. They make sharp, testable predictions about which engineering directions will continue to pay and which will not.

### 9.3 The Cross-Domain Echo with Black-Hole Architecture

The same substrate mechanism — cross-bandwidth $\Gamma_{\mathrm{cross}}$ collapse via DCGT-derived $\exp[-\alpha\sigma]$ structure — underlies black-hole horizon formation (Arc BH, BH-2) and condition (ii) failure in QC. Two faces of one substrate identity, applied at scales separated by ~50 orders of magnitude in physical length. This is the cross-domain consistency a substrate-level framework should produce; phenomenological frameworks cannot deliver it.

The structural lesson: the substrate doesn't care whether the gradient-collapse is happening at a black-hole event horizon or at a Josephson-junction barrier. The same DCGT machinery describes both. Different empirical phenomena, different physical scales, one substrate mechanism.

### 9.4 The QC Scaling Debates, Reframed

A recurring tension in quantum-computing research has been the debate between optimists (continued scaling will deliver fault tolerance through engineering) and skeptics (a fundamental limit prevents practical-scale QC). The ED account gives a structural framework that resolves the debate's framing without taking sides on whether practical-scale QC is achievable.

There *is* a fundamental limit — the substrate-level multiplicity wall — but it is not where skeptics typically place it. The wall is platform-architecture-dependent. Class A platforms hit a wall in physical-qubit count; Class B platforms can in principle exceed it by exponential factors at the cost of much harder engineering; Class C platforms hit a different wall (correlation-budget saturation) at a much lower scale. The optimists' continued-scaling expectation is correct *for Class A platforms below the wall*, incorrect *for Class A above the wall without composition*, and irrelevant *for Class B/C* which face structurally different binding constraints.

The framework dissolves the binary debate by structurally locating the limits — different limits, on different timescales, for different architectures — rather than resolving it within a single-platform engineering frame.

### 9.5 What This Changes for the Engineering Frontier

Three near-term implications for platform development:

- **For SC programs:** the system-multiplicity wall is a real structural feature; engineering effort beyond the wall must include composition with Class C (logical encoding) — pure-Class-A scaling will plateau.
- **For topological qubit programs:** the binding is *topology engineering*, not isolation engineering; effort to improve $\Delta_{\mathrm{top}}$ and gap stability is the lever, not effort to improve coupling-suppression.
- **For multi-axis / bosonic-code programs:** the bounded-redundancy-advantage is structural; sub-linear scaling past saturation is predicted, and this should be measured directly to validate or falsify the framework.

### 9.6 Implications for the Quantum-Computing Roadmap

The multiplicity-cap function $M$ implies that the dominant scaling limits of current quantum-computing platforms are **structural rather than technological**. The walls that platforms encounter at scale are not engineering accidents to be removed by improved isolation, fabrication, or error correction within their current architectural class — they are substrate-determined ceilings whose locations are set by substrate constants ($\mathcal{M}_{\mathrm{crit}}$, $\Gamma_{\mathrm{min}}$, $N_{\mathrm{corr}}$, $\Delta_{\mathrm{top}}^{\max}$) and whose existence is FORCED by the substrate machinery.

Five claims follow directly from $M$ and have direct roadmap consequences:

1. **The matter-wave Q-C boundary and qubit-platform multiplicity walls are the same substrate phenomenon.** Sharper measurement of the matter-wave boundary at 140–250 kDa directly constrains the system-multiplicity wall location for Class A qubit platforms. Progress in matter-wave interferometry and progress in superconducting-qubit scaling are not independent research programs; they probe the same substrate quantity from two platforms.

2. **Only Class B can outrun the Class A multiplicity wall by structural margin.** Class A platforms (superconducting qubits, trapped ions, photonic gate-model) face an exponential collapse of $\tau_{(\mathrm{i})}$ as their effective system-multiplicity approaches $\mathcal{M}_{\mathrm{crit}}$. No amount of isolation engineering, dynamical decoupling, or reservoir engineering pushes past this wall — these are techniques that extend Class A's environmental-binding timescales, not its multiplicity-binding timescale. Pushing past the wall requires either Class B's topological gradient-rigidity (binding shifted to topology engineering) or composition with Class C (logical encoding via redundancy, which is what error correction provides).

3. **Redundancy saturates.** Class C platforms exhibit a correlation-budget plateau at $N \sim N_{\mathrm{corr}}$. Beyond this, additional redundancy stops paying — multi-axis photonic platforms above ~3–5 axes and bosonic codes above a code-distance threshold will exhibit diminishing returns due to correlated noise channels. The redundancy advantage is bounded; Class C is not an unlimited-scaling strategy.

4. **The fault-tolerant-QC roadmap has a structural shape.** Surface-code-based fault-tolerant quantum computers are meta-architectural compositions of Class A (physical-qubit level) with Class C (logical encoding). Their scaling is governed by the substrate-level identity of their constituent layers: physical-layer Class A walls bound the substrate of the composition, and the logical-layer Class C correlation-budget bounds the gain from encoding. Strategies that aim to push the composition past *both* substrate-level bounds simultaneously must include a Class B subsystem, since Class A and Class C alone cannot.

5. **Long-term scaling strategy centers on topology-stabilized architectures.** Class B is the only architectural class whose ceiling is set by *macroscopic substrate quality* (gap engineering, sample homogeneity) rather than by environmental coupling rates. Its exponential scaling advantage over Class A — by $\exp(\Delta_{\mathrm{top}}/T_{\mathrm{eff}})$ — makes it the structurally distinct path past the matter-wave-class wall. The cost is much harder substrate engineering; the structural reward is a coherence ceiling not bounded by isolation-class techniques.

This unification suggests a re-evaluation of long-term scaling strategies in the quantum-computing field. The emphasis on isolation engineering and error-correcting overhead has historically been platform-specific and engineering-driven; the substrate-level account argues that this emphasis is correct *within Class A* but bounded by a structural wall whose location is empirically constrained by the matter-wave anchor. The path past the wall is either composition-with-Class-C (already the standard fault-tolerant approach, but bounded by correlation-budget saturation) or Class B (topology-stabilized architectures, with their structurally distinct binding mode).

The framework neither predicts that practical-scale quantum computing is achievable nor that it is impossible. What it does predict is that *which substrate-level wall is binding at what scale* determines what engineering effort will pay and what will not — and the cross-platform identity of these walls means that empirical progress in any one domain (matter-wave interferometry, SC scaling, topological-qubit gap stability, multi-axis-redundancy saturation) directly informs the substrate-level constraints on every other domain.

### 9.7 Roadmap for Numerical Calibration

The structural results presented here — UR-1, the three-class taxonomy, the multiplicity-cap function $M$, and the cross-platform unification — are complete in form. The numerical values that fix the locations of the substrate-level ceilings, however, are INHERITED rather than closed-form derived in this paper, and they require empirical calibration before quantitative platform-specific predictions become sharp. These calibrations are engineering-accessible measurements, not theoretical unknowns; the paper's role is to provide the structural form into which the calibrated values are inserted.

Five quantities, five calibration paths:

- **$\mathcal{M}_{\mathrm{crit}}$** — calibrated by matter-wave mass-cap refinement (sharper measurement of the 140–250 kDa Q-C boundary using mass-matched isomers with controlled internal-DOF structure) combined with qubit-platform multiplicity tomography (cross-talk and leakage characterization that maps physical $\mathcal{M}_{\mathrm{floor}}^{(A)}$). The two anchors converge on the same substrate constant via the cross-platform identity established in §7.
- **$N_{\mathrm{corr}}$** — calibrated by redundancy-saturation experiments in Class C platforms: extending Hafezi-class multi-timescale photonic lattices to higher axis counts and measuring where FPM-relaxation, harmonic-bandwidth, and yield improvements plateau; analogously, scaling bosonic-code distance and measuring logical-qubit lifetime saturation.
- **$\Delta_{\mathrm{top}}^{\max}$ and $T_{\mathrm{eff,\min}}$** — calibrated by gap-stability measurements in Class B platforms: gap spectroscopy in topological-qubit candidate materials combined with quasiparticle-poisoning and edge-state-hybridization rate measurements at varying temperature, mapping the achievable region of the $(\Delta_{\mathrm{top}}, T_{\mathrm{eff}})$ plane.
- **Architecture-specific $f_{\mathrm{sys}}^{(A)}(\mathcal{S})$** — calibrated by cross-platform comparison of how effective system-multiplicity scales with system size for canonical Class A platforms (transmon, fluxonium, trapped ion, photonic gate-model). Each architecture has its own scaling, and the cross-architecture comparison is itself informative for the substrate-coupling pattern.
- **Platform-specific $N_\star$** — calibrated by system-multiplicity scaling experiments in Class A qubit platforms: measuring effective $\tau_{\mathrm{QC}}^{\mathrm{logical}}$ as physical-qubit count rises at fixed code distance and locating the plateau predicted in §7.4.

These five calibration paths are mutually consistent with the cross-platform identity: the matter-wave anchor and the qubit-system anchor must yield consistent values of $\mathcal{M}_{\mathrm{crit}}$, and the four primary empirical anchors must lie at substrate-determined locations on $M$ across the calibrated parameter space. Calibration is downstream work; the structural framework is delivered.

### 9.8 Topology-Stability as a Downstream Theorem

Class B's ceiling is set by the topology-perturbation rate $\tau_{\mathrm{gap-stab}}(\mathcal{T})$, which the present arc names as a structural quantity but does not derive at platform-level specificity. A full **topology-stability theorem** would formalize how global ED-channel geometry resists local substrate perturbation across canonical topological structures (Majorana, Fibonacci anyons, Chern bands), expressing $\tau_{\mathrm{gap-stab}}(\mathcal{T})$ as a substrate-level functional of the topological invariant $\mathcal{T}$ and the substrate's local fluctuation spectrum.

Such a theorem is a natural follow-on arc (priority item O-QC-4) and is explicitly not solved in this paper. The architectural role of Class B is complete: its protection mechanism is identified (rigidity of ED-channel geometry under topological invariants, ED-I-14 + ED-I-18 §7), its binding constraint is named (topology-perturbation rather than environmental rate), and its substrate-level scaling is established ($\exp(\Delta_{\mathrm{top}}/T_{\mathrm{eff}})$ enhancement over Class A). The topology-stability theorem provides the platform-level bound on $\tau_{\mathrm{gap-stab}}(\mathcal{T})$ that converts the structural Class B ceiling into a closed-form numerical prediction for any specific topological architecture. The structural framework is in hand; the theorem that calibrates it remains downstream work, requiring the platform-specific geometric analysis that ED-I-14's interpretive content sketches but does not formalize.

---

## 10. Appendices

### Appendix A — UR-1 Proof Sketch

**Sufficient direction.** Assume UR-1's three conditions (i), (ii), (iii) hold. Then:

- By (i), $\mu(\mathcal{M}_i/\mathcal{M}_{\mathrm{crit}}) \geq \mu(\mu^{-1}(\mathcal{U}_{\mathrm{min}}^{1/n})) = \mathcal{U}_{\mathrm{min}}^{1/n}$ for each endpoint, so the multiplicity-headroom product satisfies $\prod_i \mu \geq \mathcal{U}_{\mathrm{min}}$.
- By (ii), an analogous bound on the connectivity product gives $\prod_{(i,j) \in \mathcal{R}} \kappa \geq \mathcal{U}_{\mathrm{min}}$.
- By (iii), $\exp[-\int_0^t \Lambda dt'] \geq \mathcal{U}_{\mathrm{min}} \cdot e^{C_{(\mathrm{i})} + C_{(\mathrm{ii})}}$.

Multiplying the three factors and accounting for cross-condition deficits: $\mathcal{U}(\mathcal{S},t) \geq \mathcal{U}_{\mathrm{min}}$. ∎

**Necessary direction.** Suppose $\mathcal{U}(\mathcal{S},t) \geq \mathcal{U}_{\mathrm{min}}$ but condition (i) fails at some endpoint $e_k$: $\mathcal{M}_k > \mathcal{M}_{\mathrm{crit}}^{(\mu^{-1}(\mathcal{U}_{\mathrm{min}}^{1/n}))}$. Then $\mu(\mathcal{M}_k/\mathcal{M}_{\mathrm{crit}}) < \mathcal{U}_{\mathrm{min}}^{1/n}$, so the multiplicity-headroom product is below $\mathcal{U}_{\mathrm{min}}$. Even with the other two factors at their maximum (1 each), $\mathcal{U} < \mathcal{U}_{\mathrm{min}}$, contradiction. The same argument applies for (ii) and (iii). ∎

The full closed-form proof requires the specific functional shapes of $\mu$ and $\kappa$, which are INHERITED. The structural argument is form-FORCED.

### Appendix B — DCGT-WKB Recovery of MQT

The Josephson-junction MQT rate inherits its WKB exponential structure directly from DCGT's cross-bandwidth formula. For a JJ engineered at the (ii) boundary with $\gamma_{\mathrm{floor}} \to \Gamma_{\mathrm{min}}$, the dominant contribution to $\tau_{(\mathrm{ii})}^{(A,\mathrm{JJ})}$ comes from below-threshold excursions of $\gamma_{LR}$. Each excursion produces a global rule reconfiguration (per ED-I-29). The rate of such excursions is set by the DCGT $\kappa$-function evaluated at the engineered $\sigma$-profile of the barrier:

$$
\tau_{\mathrm{MQT}}^{-1} = \omega_0\,\exp\!\left[-\alpha\!\int_{\mathrm{barrier}}\sigma(\mathbf{x})\,d\ell\right]
$$

with $\omega_0$ a substrate-attempt frequency (INHERITED) and $\alpha$ the DCGT prefactor. The integrand $\sigma = |\nabla\rho|\ell_P^2/\rho_{\mathrm{local}}$ is evaluated across the barrier; in standard JJ language, this maps to barrier height and width, recovering the standard WKB form.

### Appendix C — Cross-Anchor Consistency Table

| Anchor | Class | Binding condition | Substrate identification | Form FORCED | Value INHERITED |
|---|---|---|---|---|---|
| Bulk SC $T_c$ (ED-I-01) | A | (iii) | thermal $\Lambda_{\mathrm{env}}$ crosses threshold | yes | $T_c$ value |
| JJ MQT (Devoret-Martinis-Clarke) | A | (ii) near-threshold | WKB from DCGT | yes | prefactor, barrier $\sigma$ |
| SC qubit T₁ | A | (iii) | Purcell + dielectric + QP | yes | rates |
| SC qubit T₂ | A | (ii) | Kramers escape | yes | $\tau_{\mathrm{dec}}^{(\mathrm{ii})}$ |
| Matter-wave Q-C 140–250 kDa | A | (i) static | $\mathcal{M}_{\mathrm{floor}} = \mathcal{M}_{\mathrm{crit}}$ | yes | $M_\star$ value |
| Topological-gap suppression | B | (iii)/gap-stab | $\Lambda \cdot \exp(-\Delta/T_{\mathrm{eff}})$ | yes | $\Delta$, $\tau_{\mathrm{gap-stab}}$ |
| Photonic Chern channels | B | (ii) edge-state rigidity | global ED-channel invariant | yes | sample quality |
| Hafezi multi-timescale | C | (i) relaxed | $g(N), h(N), c(N)$ | yes | $N_{\mathrm{corr}}$ |
| Bosonic codes (cat, GKP) | C | redundancy budget | photon-number redundancy | yes | code parameters |
| Surface-code logical | Meta: A+C | logical binding | recursive overlay | yes | code distance |
| Reservoir-engineered cat | A (overlay) | (i) with active restoring | $A_{S}$ via env coupling | yes | engineering details |
| Dynamically-decoupled SC | A (overlay) | (iii) with reduced $\Lambda^{\mathrm{eff}}$ | temporal averaging | yes | pulse parameters |

### Appendix D — Comparison with Standard QC Frameworks

| Feature | Standard QC framing | ED substrate framing |
|---|---|---|
| Coherence | State property of wavefunction | Integrity of unresolved participation rule across endpoints |
| Decoherence | Coupling of state to environment | P11 commitment events firing at endpoints |
| Engineering target | Reduce coupling-rate to environment | Hold substrate region in low-$\mathcal{M}$ + high-$\gamma_{ij}$ + low-$\Lambda$ |
| Coherence-time | T₁ / T₂ as state-decay rates | $\tau_{\mathrm{QC}} = \min(\tau_{(\mathrm{i})}, \tau_{(\mathrm{ii})}, \tau_{(\mathrm{iii})})$ over substrate-condition crossings |
| Architectural classes | platform-specific (SC, ion, photonic, topo) | substrate-level (A: low-$\mathcal{M}$; B: rigid-$\sigma$; C: redundancy) |
| Cross-platform unification | not addressed | matter-wave Q-C boundary ↔ qubit-system $N_\star$ on one $M$ function |
| Hard limit on QC | open question / debated | substrate-determined wall in Class A; gap-stability in Class B; correlation budget in Class C |
| Error correction | logical encoding for fault tolerance | Class A + Class C meta-architectural composition |
| MQT rate | WKB postulated from QM | WKB derived from DCGT cross-bandwidth structure |

---

## 11. Metadata

**Keywords.** Event Density; Quantum Computation; Substrate Physics; Unresolved Regime; UR-1; Multiplicity-Cap Function; Architectural Class Taxonomy; Matter-Wave Q-C Boundary; Josephson Junction MQT; Topological Qubits; Multi-Timescale Photonics; Form-FORCED / Value-INHERITED Methodology.

**Version.** 1.0 — May 2026.

**Arc Q-COMPUTE references.** Seven memos in `theory/Quantum_Computing/`: Arc_QC_1_Opening; Arc_QC_2_UR1_Unresolved_Regime_Characterization; Arc_QC_3_Failure_Mode_Rates; Arc_QC_4_Architectural_Class_Audit; Arc_QC_5_Multiplicity_Cap_Function; Arc_QC_6_Predictive_Content; Arc_QC_7_Synthesis.

**Related ED Papers.** *Black Holes in Event Density: A Substrate-Level Architecture* (May 2026); *Foundations of Substrate Gravity: From Newtonian Limit to Curvature Emergence* (April 2026); *Event Density Foundations: A Unified Substrate Architecture for Quantum, Fluid, Gauge, and Gravitational Dynamics* (April 2026); *Navier-Stokes Synthesis Paper* (April 2026, with Appendices C/D/E covering MHD, DCGT, Yang-Mills); *Theorem 17: Gauge-Field-as-Rule-Type*; *Theorem 18: V1 Kernel Retardation*.

**ED-I Series Foundations.** ED-I-01 (Superconductivity); ED-I-12 (Photonics: Yablonovitch, Pendry, Capasso); ED-I-13 (Quantum Information: Bennett, Brassard, Deutsch, Jozsa, Shor); ED-I-14 (Topological Effects: Aharonov, Berry, Bohm, Casher, Tonomura); ED-I-18 (Multi-Timescale Photonics: Hafezi 2025); ED-I-23 (Josephson Junction Physics); ED-I-29 (Tunneling).

**Citation Block (Zenodo-safe).**

> Proxmire, A. (2026). *Quantum Computation in Event Density: A Substrate-Level Architecture and Its Limits.* Event Density Program, Quantum Computing Foundations Paper, May 2026.

**Conditional-Positive Verdict Disclaimer.** This paper presents a substrate-level architectural account of quantum computation. Form-derivations are FORCED from substrate machinery; value-layer details ($\mathcal{M}_{\mathrm{crit}}$, $N_\star$, $N_{\mathrm{corr}}$, $\Delta_{\mathrm{top}}^{\max}$, specific shapes of $\mu, \kappa, g/h/c$) are INHERITED and not closed-form derived at present. No constructive recipe for fault-tolerant QC is delivered; the arc is structural, not engineering. Open extensions (closed-form $\mathcal{M}_{\mathrm{crit}}$, architecture-to-platform calibration, topology-stability theorem, surface-code recursive-overlay derivation, hybrid-handoff dynamics) are explicitly named.
