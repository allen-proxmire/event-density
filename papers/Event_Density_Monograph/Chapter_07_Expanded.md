# Chapter 7 — Quantum Computation: UR-1, the Multiplicity-Cap Function $M$, Architectural Taxonomy

## 7.1 Chapter Overview

Quantum computation, in the Event Density framework, is the **deliberate engineered occupation of a low-multiplicity unresolved-rule substrate regime** — a region of substrate where a participation rule remains unresolved across designated endpoints long enough for its geometry to be manipulated, before environmental ED-injection forces irreversible individuation. The **Unresolved-Regime Characterization Theorem (UR-1)** identifies three independently-necessary substrate conditions for the regime: (i) bounded multiplicity, (ii) sustained cross-endpoint connectivity, and (iii) bounded commitment-injection. The QC operating window is given structurally by $\tau_\mathrm{QC} = \min(\tau_{(\mathrm{i})}, \tau_{(\mathrm{ii})}, \tau_{(\mathrm{iii})})$ over the three condition-failure timescales.

Three architectural classes — **engineered-low-multiplicity (A)**, **global-geometric-rigidity (B)**, **high-multiplicity-redundancy (C)** — exhaust the substrate-allowed strategies for protecting the regime. The **multiplicity-cap function $M$** unifies the classes as projections of one substrate object. The chapter's strongest result is **cross-platform unification**: the matter-wave quantum-classical boundary at 140–250 kDa molecular mass and the qubit-system multiplicity walls are the same substrate-determined boundary projected onto two different platforms via shared substrate constants. The framework's reframing replaces decoherence (the standard variable) with multiplicity (the upstream substrate variable), and the chapter develops the substrate-level architecture of QC under this reframing.

The chapter does not deliver a constructive recipe for fault-tolerant quantum computing. It is a structural account: it establishes what QC *is* at the substrate level, what its limits are, and how those limits manifest across the platform inventory. After this chapter, every continuum theory in Parts III and IV inherits the substrate ontology developed here for the quantum sector.

## 7.2 The Substrate-Level Reframing

### 7.2.1 The standard QC framing and what it misses

Standard quantum computing treats coherence as a state property of a wavefunction and decoherence as the wavefunction's coupling to environmental degrees of freedom. The operative variable is the coupling rate; engineering reduces the rate; coherence times scale inversely with the irreducible coupling-rate floor. Scaling limits are explained by where the engineering cannot push the coupling rate any lower.

This framing is empirically successful but structurally incomplete. It does not say *why* certain platforms hit walls at certain scales. It does not unify the matter-wave quantum-classical boundary (a foundational-physics observation about giant molecules) with qubit-system scaling limits (an engineering question about coherence preservation in arrays). It treats different platforms (superconducting, ion, photonic, topological, bosonic) as different problems requiring different solutions, when the substrate-level analysis says they are the same problem viewed from different architectural angles.

### 7.2.2 The substrate variable

ED reframes the central organizing variable. **Multiplicity** $\mathcal{M}$ — the count of viable distinct ED-gradient pathways available locally, established in Chapter 2 as the substrate analogue of entropy — is the upstream substrate-state quantity. Decoherence in the standard sense is the *coarse-grained signature* of substrate-level individuation events firing at endpoints whose multiplicity has risen above a substrate-determined threshold. The standard variable is real but downstream; the substrate variable is upstream and structurally prior.

The reframing has direct structural consequences:

- **Coherence is not a state property.** It is the integrity of an *unresolved participation rule* spanning designated endpoints (the substrate-level analogue of the wavefunction superposition).
- **Decoherence is not a coupling rate.** It is the substrate-level event of P11 commitment occurring before the protocol intends. P11 commitment is the substrate-level mechanism; decoherence rate is the coarse-grained measurement of how often the mechanism fires.
- **Engineering effort is not "reducing decoherence."** It is *holding the substrate region in a low-multiplicity, well-connected, low-commitment-rate configuration*, against the substrate's natural tendency to proliferate gradients and force individuation.

The framing change is structurally significant because it shifts the question from "how do we engineer-down a coupling rate?" to "what substrate conditions must be held, and what architectural strategies hold them?" The latter question has a substrate-level structural answer (UR-1, Section 7.4); the former does not.

### 7.2.3 What QC is, in substrate language

Quantum computation, in ED's reading, is structurally the same kind of object as a Josephson junction (ED-I-23), a bulk superconductor (ED-I-01), a Tonomura-class topological-phase setup (ED-I-14), a multi-timescale photonic lattice (ED-I-18), or the inside of a saturated participation zone (BH-3). Each is a substrate region of low-multiplicity ED-flow held against the substrate's tendency to proliferate gradients and force individuation. The differences across platforms are not in *what* is being held but in *how* it is being held — which substrate-state quantity the architecture commits to fix, and through what mechanism.

A QC, specifically, uses the regime as an *operating substrate* on which to manipulate unresolved participation geometry. Quantum gates are substrate-level operations that reshape the geometry of the unresolved rule before it commits. Readout is the controlled triggering of P11 commitment events at designated endpoints. The substrate-level account makes the standard QC machinery legible without changing any of its empirical content.

## 7.3 Substrate State and Substrate-State Quantities

### 7.3.1 The five substrate-state quantities for QC

Five substrate-level quantities govern the QC sector. Each is established in Chapter 2 as a load-bearing invariant; this chapter applies them in the QC-architectural reading:

- **Multiplicity** $\mathcal{M}(\mathcal{S})$ at substrate region $\mathcal{S}$. The count of viable distinct ED-gradient pathways available locally.
- **Gradient sparsity** $\sigma(\mathbf{x}) = |\nabla\rho|\,\ell_P^2/\rho_\mathrm{local}$ at substrate point $\mathbf{x}$. The substrate-scale dimensionless steepness of participation density.
- **Cross-bandwidth** $\gamma_{ij}$ along a rule-spanning pathway between endpoints $e_i$ and $e_j$. The substrate-mediated rate at which the two endpoints exchange correlated participation events.
- **Commitment-injection rate** $\Lambda_\mathcal{S}(t) = \Lambda_\mathrm{env}(t) + \Lambda_\mathrm{int}(t)$. The rate at which P11 commitment events fire at $\mathcal{S}$'s endpoints, sourced by environmental ED-injection plus internal participation dynamics.
- **Unresolvedness** $\mathcal{U}(\mathcal{S}, t) \in [0, 1]$. The integrity of an unresolved participation rule across the designated endpoints of $\mathcal{S}$ at substrate time $t$. $\mathcal{U} \to 1$ when the rule is fully unresolved; $\mathcal{U} \to 0$ when full individuation has been reached.

The QC architecture's substrate-level analysis is a function of these five quantities and the architectural mechanisms that hold them within their operational regimes.

### 7.3.2 The unresolvedness function

The unresolvedness $\mathcal{U}(\mathcal{S}, t)$ takes a specific form-FORCED structure derived in UR-1 (Section 7.4). It is a three-factor product:

```math
\mathcal{U}(\mathcal{S}, t) = \prod_{i \in \mathrm{endpts}(\mathcal{R})} \mu\!\left(\frac{\mathcal{M}_i(t)}{\mathcal{M}_\mathrm{crit}}\right) \cdot \prod_{(i,j) \in \mathcal{R}} \kappa\!\left(\frac{\gamma_{ij}(t)}{\Gamma_\mathrm{min}}\right) \cdot \exp\!\left[-\int_0^t \Lambda_\mathcal{S}(t')\,dt'\right]
```

The three factors correspond, in order, to:

- **Multiplicity headroom.** Whether each endpoint's local multiplicity is bounded below the substrate-determined critical value $\mathcal{M}_\mathrm{crit}$.
- **Rule-spanning connectivity.** Whether each rule-spanning pathway maintains cross-bandwidth above the substrate-determined minimum $\Gamma_\mathrm{min}$.
- **Commitment survival.** Whether the cumulative commitment-injection rate has not yet driven the rule to individuation.

The product structure is form-FORCED: the rule fails to remain unresolved if *any* of the three factors collapses. The functional shapes $\mu$ and $\kappa$ are form-FORCED to be monotone with specific limiting behavior; their specific functional forms are INHERITED from the substrate-level V1-kernel and DCGT machinery.

### 7.3.3 The relation set $\mathcal{R}$

The relation set $\mathcal{R}$ identifies which endpoint pairs the rule spans. For a single qubit, $\mathcal{R}$ is the set of designated $\{|0\rangle, |1\rangle\}$ endpoints. For a multi-qubit entangled register, $\mathcal{R}$ extends across all qubits' designated endpoints. For a matter-wave interferometer, $\mathcal{R}$ is the pair of arms. The structural content of $\mathcal{R}$ is that it specifies *which* substrate endpoints the rule must remain unresolved across; $\mathcal{R}$ is platform-specific but the UR-1 structural form is platform-independent.

## 7.4 UR-1: The Unresolved-Regime Characterization Theorem

### 7.4.1 The theorem statement

**UR-1 (Unresolved-Regime Characterization Theorem).** Let $\mathcal{S}$ be a substrate region with designated participation-rule relation set $\mathcal{R}$ over endpoints $\{e_1, \ldots, e_n\}$. Let $\mathcal{U}_\mathrm{min} \in (0, 1)$ be a target unresolvedness threshold. Then $\mathcal{U}(\mathcal{S}, t) \geq \mathcal{U}_\mathrm{min}$ holds at substrate time $t$ if and only if:

- **(i) Multiplicity bounded.** For every endpoint $e_i$, $\mathcal{M}_i(t) \leq \mathcal{M}_\mathrm{crit}$.
- **(ii) Cross-endpoint connectivity sustained.** For every pair $(i, j) \in \mathcal{R}$, $\gamma_{ij}(t) \geq \Gamma_\mathrm{min}$.
- **(iii) Commitment-injection bounded.** $\int_0^t \Lambda_\mathcal{S}(t')\,dt' \leq \ln(1/\mathcal{U}_\mathrm{min})$ (with appropriate corrections from the per-condition negative-log deficits).

Each condition is independently necessary. Failure of any one drives $\mathcal{U}$ below $\mathcal{U}_\mathrm{min}$ at a substrate-determined rate. The conditions are coupled through substrate geometry — physical substrate configurations cannot independently dial all three — but each can fail without the others.

### 7.4.2 Why three conditions, not more or fewer

The three-factor product form of $\mathcal{U}$ is forced by the substrate-level structure of the unresolved rule. Three substrate-level processes can independently degrade $\mathcal{U}$:

- **Local multiplicity proliferation** at any endpoint of the rule. If the count of viable pathways at one endpoint exceeds $\mathcal{M}_\mathrm{crit}$, the rule cannot remain coherently spread across that endpoint.
- **Cross-endpoint bandwidth collapse** along any rule-spanning pathway. If the substrate-mediated cross-bandwidth between two endpoints falls below $\Gamma_\mathrm{min}$, the rule cannot remain coherent across that pair.
- **Commitment-event accumulation** at any endpoint of the rule. Each P11 commitment event at an endpoint is an irreversible individuation; cumulative commitment-injection drives $\mathcal{U}$ to zero exponentially.

These three processes are structurally distinct (they arise from different substrate quantities) but compose multiplicatively on $\mathcal{U}$, because any of them alone can drive the rule to $\mathcal{U} \to 0$ regardless of the others. The functional form must therefore be a product of three factors, one per process. UR-1's three-condition structure is the substrate-level statement that all three factors must be held.

### 7.4.3 Independence and substrate-geometric coupling

UR-1's three conditions are **independent in form** (each can fail alone, each is independently necessary, the proof establishes that violation of any one drops $\mathcal{U}$ below threshold even with the other two satisfied) but **coupled through substrate geometry** (a physical substrate region cannot independently dial $\mathcal{M}$, $\sigma$, $\Lambda$ to arbitrary values; substrate constraints link them). For Block-B failure-mode rate analysis (Section 7.5) and Block-D multiplicity-cap-function construction (Section 7.7), each condition is treated independently. For Block-C architectural classification (Section 7.6), the geometric coupling matters — different architectures use different substrate-geometric tactics to satisfy multiple conditions simultaneously, and the substrate-coupling structure is what distinguishes one architecture class from another.

### 7.4.4 Reduction to known regimes

UR-1 reproduces three known regimes cleanly, each with a different binding condition:

- **Bulk superconductor (ED-I-01).** Below $T_c$, conditions (i) and (ii) hold robustly; condition (iii) holds because thermal ED-injection rate is below the substrate individuation threshold. Above $T_c$, thermal injection drives condition (iii) failure; $\mathcal{U}$ drops; resistance reappears. **$T_c$ is identified as the substrate temperature at which condition (iii) crosses its threshold.**
- **Josephson junction (ED-I-23).** Two low-$\mathcal{M}$ SC electrodes separated by a thin barrier. Conditions (i) and (iii) hold; condition (ii) is the *load-bearing* condition by design — the barrier creates a high-$\sigma$ region with $\gamma_{LR}$ engineered just above $\Gamma_\mathrm{min}$. The JJ lives at the (ii) boundary. **Macroscopic quantum tunneling (Devoret-Martinis-Clarke 1985) corresponds to dynamical fluctuations at the (ii) boundary** — the rule globally reconfigures across the gap when $\gamma_{LR}$ momentarily drops below threshold. The MQT rate's WKB exponential structure is recovered directly from DCGT $\kappa$-function evaluation.
- **Free atomic-scale matter wave.** The molecule is a low-$\mathcal{M}$ ED-object whose internal $\mathcal{M}$ scales with mass (rotational + vibrational + electronic DOF activation). For low molecular mass, $\mathcal{M} \ll \mathcal{M}_\mathrm{crit}$ and condition (i) holds. For high mass (140–250 kDa), internal $\mathcal{M}$ rises and crosses $\mathcal{M}_\mathrm{crit}$. **The matter-wave Q-C boundary is identified as the molecular mass at which condition (i) crosses threshold.**

Three different empirical phenomena, three different UR-1 conditions, one substrate framework.

## 7.5 Failure-Mode Rates and the QC Operating Window

### 7.5.1 Three substrate-level dynamics

Each UR-1 condition admits a substrate-level dynamical equation governing the timescale at which it crosses threshold.

**Condition (i) multiplicity dynamics.** The substrate-level evolution of $\mathcal{M}$ is

```math
\frac{d\mathcal{M}}{dt}\bigg|_\mathcal{S} = \alpha_\mathrm{env}\,\Lambda_\mathrm{env}(t) + \alpha_\mathrm{act}\,S_\mathrm{int}(t) - A_\mathcal{S}(\mathcal{M} - \mathcal{M}_\mathrm{floor})
```

with $\alpha_\mathrm{env}\Lambda_\mathrm{env}$ environmental ED-injection driving pathway-count growth, $\alpha_\mathrm{act}S_\mathrm{int}$ internal pathway-activation rate from thermal or operational stimulation, and $A_\mathcal{S}(\mathcal{M} - \mathcal{M}_\mathrm{floor})$ architectural restoring rate returning $\mathcal{M}$ to the architecturally-imposed floor. Two failure modes: **static** when $\mathcal{M}_\mathrm{floor} \geq \mathcal{M}_\mathrm{crit}$ (the system cannot be operated regardless of timescale; this is the matter-wave Q-C boundary regime) and **dynamic** when $\mathcal{M}_\mathrm{floor} < \mathcal{M}_\mathrm{crit}$ but environmental injection drives the steady state above threshold.

**Condition (ii) cross-bandwidth dynamics.** The cross-bandwidth $\gamma_{ij}(t)$ evolves under substrate gradient erosion plus architectural pumping, with the form $d\gamma_{ij}/dt = -(\gamma_{ij} - \gamma_\mathrm{floor})/\tau_\mathrm{dec}^{(\mathrm{ii})} + \xi(t)$ where $\xi(t)$ is stochastic substrate perturbation. Two regimes: **sustained-above-threshold** ($\gamma_\mathrm{floor} > \Gamma_\mathrm{min}$ with margin; $\tau_{(\mathrm{ii})}$ exponentially long via Kramers-class escape) and **near-threshold** ($\gamma_\mathrm{floor} \approx \Gamma_\mathrm{min}$ by design, as in JJ; fluctuations push below threshold; each crossing produces global rule reconfiguration with WKB MQT rate $\sim \omega_0 \exp[-\alpha\int_\mathrm{barrier}\sigma\,d\ell]$).

**Condition (iii) commitment-injection dynamics.** The commitment-survival factor crosses threshold at

```math
\tau_{(\mathrm{iii})} = \frac{\ln(1/\mathcal{U}_\mathrm{min})}{\Lambda_\mathrm{env} + \Lambda_\mathrm{int}}.
```

$\Lambda_\mathrm{env}$ has additive contributions from thermal radiation, residual-gas collisions, Purcell decay into electromagnetic modes, dielectric noise, magnetic-flux fluctuations, quasiparticle injection from above-gap excitations. Bounded below by V1 vacuum kernel residual rate $\Lambda_{V1}$. $\Lambda_\mathrm{int}$ accumulates from intentional commitments (gates, ancilla resets, intermediate measurements) and incidental commitments.

### 7.5.2 The QC operating window

Combining: the QC operating window is the substrate time over which all three UR-1 conditions simultaneously hold,

```math
\tau_\mathrm{QC} = \min\bigl[\tau_{(\mathrm{i})}, \tau_{(\mathrm{ii})}, \tau_{(\mathrm{iii})}\bigr].
```

Three structural observations follow.

**Different architectures bind on different conditions.** Each architectural class is characterized not by which timescale is *longest* but by which is *shortest* — i.e., which UR-1 condition is the architecture's binding constraint. The class taxonomy of Section 7.6 pivots on this observation.

**The operating window is a substrate observable.** $\tau_\mathrm{QC}$ corresponds to what experimentalists call coherence time, T₁/T₂, fault-tolerance-headroom, or maximum coherent flight time. Cross-platform measurements are evaluations of $\tau_\mathrm{QC}$ for different binding conditions.

**Architectural design is the optimization of $\min(\cdot)$.** Improving the longest of the three timescales is irrelevant; only improvement of the *binding* timescale extends the window. The substrate provides the structural reason for what platform-development teams empirically know.

### 7.5.3 Empirical anchor reductions

Cross-platform anchors map cleanly to the three conditions:

| Phenomenon | Binding condition | Substrate identification |
|---|---|---|
| Matter-wave Q-C boundary 140–250 kDa | (i) static failure | $\mathcal{M}_\mathrm{floor}(M_\star) = \mathcal{M}_\mathrm{crit}$ |
| SC qubit T₁ | (iii) | $\Lambda_\mathrm{env}$ Purcell + dielectric + quasiparticle |
| SC qubit T₂ | (ii) | Kramers escape from protected pathway |
| JJ MQT (Devoret-Martinis-Clarke) | (ii) near-threshold | WKB $\sim \omega_0 \exp[-\alpha\int\sigma\,d\ell]$ |
| Topological-qubit error suppression | (iii) gap-suppressed | Most env modes don't couple to protected rule |
| Multi-timescale FPM relaxation (Hafezi 2025) | (i) relaxed by redundancy | Multi-axis pathway expansion |
| Quasiparticle poisoning | multi-condition (i)+(iii) | Single event raises $\mathcal{M}$ and $\Lambda$ |

The pattern is: each empirical phenomenon is the substrate-level signature of one UR-1 condition crossing threshold (or, for poisoning-class events, of multiple conditions crossing simultaneously). The taxonomy is one substrate framework, multiple platform projections.

## 7.6 The Three-Class Architectural Taxonomy

### 7.6.1 Three substrate-allowed protection strategies

Three architectural classes exhaust the substrate-level base strategies for protecting the unresolved-rule regime. The exhaustiveness argument is structural and is developed in detail in Arc Q-COMPUTE Memo 4; the chapter summarizes the result.

**Class A — engineered-low-multiplicity.** Protection target: condition (i) bounded multiplicity. The architecture commits structurally to suppressing local multiplicity via lattice symmetry, engineered ED-bottleneck, deep confinement, or mode engineering. Examples: bulk superconductors (ED-I-01: lattice symmetry collapses $\mathcal{M}$ to ≈ 1); Josephson junction qubits (ED-I-23: deliberately engineered ED-bottlenecks); trapped ions (deeply confined low-$\mathcal{M}$ regions); gate-model photonic platforms (single-photon states in engineered linear-optical circuits, ED-I-12 + ED-I-13). Mechanism: structural simplification of the substrate's gradient landscape, holding $\mathcal{M}_\mathrm{floor}$ low by design. Binding constraint: typically (ii) or (iii) — environmental coupling channels reaching through engineered isolation.

**Class B — global-geometric-rigidity.** Protection target: condition (ii) cross-endpoint connectivity. The architecture encodes the participation rule in *global ED-channel geometry* — topological invariants of the substrate's gradient structure that cannot be perturbed by local environmental injection. The participation rule's integrity is a property of channel connectivity, not of local timing. Examples: topological qubits (Majorana, anyonic platforms; ED-I-14 establishes topological phases as global invariants of ED-channel geometry); photonic Chern channels (ED-I-12 + ED-I-18: edge states with topologically protected gradient rigidity); geometric-phase quantum gates. Mechanism: encoding identity in homotopy-class structure of ED-channel geometry; local environmental perturbation cannot reach the encoded information without spanning the entire channel topology. Binding constraint: $\tau_\mathrm{gap-stab}(\mathcal{T})$ — the substrate-level rate at which the global topological structure $\mathcal{T}$ can be perturbed (gap-closing events, edge-state hybridization, anyonic non-Abelian braiding errors).

**Class C — high-multiplicity-redundancy.** Protection target: $\mathcal{U}$ via redundancy of pathways. Condition (i) is *relaxed* by architectural design — high $\mathcal{M}$ is permitted, but the rule's integrity survives because multiple parallel pathways carry the same participation structure. Examples: multi-timescale photonic lattices (ED-I-18: Hafezi 2025 multi-axis ring resonators with 100% device yield via redundancy expansion); bosonic codes (cat states, GKP states; encoding logical information across many physical photon-number states); generalized multi-axis architectures. Mechanism: parallel ED-channels carrying the same participation rule; environmental ED-injection driving any single pathway toward individuation is absorbed by the redundancy; the rule's integrity is sustained by surviving channels. Binding constraint: correlated errors across redundant pathways exceeding the *correlation budget* $N_\mathrm{corr}$ — common-mode noise, shared substrate defects, optical-mode crosstalk that defeat pathway-independence.

### 7.6.2 Exhaustiveness over substrate-level base strategies

The three classes are exhaustive over substrate-level base protection strategies, by the following structural argument:

1. UR-1 has three conditions, each set by a substrate quantity ($\mathcal{M}$, $\sigma$/$\gamma_{ij}$, $\Lambda$).
2. Two of these substrate quantities are *fixable structurally* — $\mathcal{M}$ via local structural simplification (Class A), and $\sigma$ via global topological invariants (Class B). $\Lambda$ is not fixable structurally because it is intrinsically a coupling rate at the boundary between protected region and environment; reducing $\Lambda$ is achieved as a *consequence* of the other classes' mechanisms (low-$\mathcal{M}$ system isolated → low coupling, Class A; topological gap → suppressed coupling, Class B; redundancy → reduced impact of any single coupling event, Class C).
3. The third strategy is *indirect* — instead of fixing a substrate quantity, provide redundancy so that $\mathcal{U}$ survives partial failures (Class C).
4. No fourth substrate-level base strategy exists because (a) there are only three substrate quantities to fix in UR-1's structure, (b) only two are structurally fixable, (c) the redundancy strategy provides the third option, and (d) all candidate Class D strategies audited in Arc Q-COMPUTE Memo 4 are either techniques for extending one of A/B/C's timescales or compositions of A/B/C.

The three-class structure is therefore exhaustive at the substrate-level base; the closure status is FORCED.

### 7.6.3 Meta-architectures: compositions and techniques

Real systems are typically *compositions* of A/B/C. Four candidate Class D strategies were audited in Arc Q-COMPUTE Memo 4 and rejected as new substrate-level classes:

- **Dynamical decoupling.** Reduces effective $\Lambda$ via temporal averaging. Technique for extending $\tau_{(\mathrm{iii})}$ within Class A; not a new substrate-level strategy.
- **Reservoir engineering (Mirrahimi-Devoret cat states).** Implements the architectural restoring rate $A_\mathcal{S}$ via structured environmental coupling. Technique for Class A's restoring mechanism; not a new substrate-level strategy.
- **Error-correction-as-architecture.** Class C encoding (logical via redundancy across physical qubits) plus Class A active restoring (syndrome-guided correction) at logical level. Meta-architectural composition of A and C; not a new substrate-level strategy.
- **Hybrid systems (SC-photonic, topological-SC).** Compositions of A/B/C subsystems with substrate-geometric handoff boundaries. Compositions; not new substrate-level strategies.

The substrate-level taxonomy is unchanged by the existence of meta-architectures. The three-class structure describes the *base*; meta-architectures are the *compositions* layered on the base.

## 7.7 The Multiplicity-Cap Function $M$

### 7.7.1 The unified function

The multiplicity-cap function $M$ is a single substrate object with three architectural-class projections:

```math
M(\mathcal{S}, K, \mathcal{E}, \mathcal{O}) = \min\bigl[\tau_{(\mathrm{i})}^{(K, \mathcal{O})}(\mathcal{S}, \mathcal{E}),\ \tau_{(\mathrm{ii})}^{(K, \mathcal{O})}(\mathcal{S}, \mathcal{E}),\ \tau_{(\mathrm{iii})}^{(K, \mathcal{O})}(\mathcal{S}, \mathcal{E})\bigr]
```

with inputs:

- **System** $\mathcal{S}$: the protected region's configuration, including endpoints, $\mathcal{M}_\mathrm{floor}$, $\gamma_\mathrm{floor}$, and any architectural redundancy count.
- **Class** $K \in \{A, B, C\}$: the architectural-class assignment.
- **Environment** $\mathcal{E}$: $\Lambda_\mathrm{env}$, perturbation rates, temperature.
- **Meta-architecture overlay** $\mathcal{O}$: dynamical decoupling, reservoir engineering, error correction, hybrid composition (any combination).

Each $\tau_j^{(K,\mathcal{O})}$ is evaluated using the rate equation from Section 7.5 with class-specific protection-mechanism modifiers and meta-architectural overlay extensions.

### 7.7.2 The class projections

**$M_A$ — Class A projection.** The $\tau_{(\mathrm{i})}^{(A)}$ is split into static-failure and dynamic-failure branches; static failure occurs if $\mathcal{M}_\mathrm{floor}(\mathcal{S}) \geq \mathcal{M}_\mathrm{crit}$. The $\tau_{(\mathrm{ii})}^{(A)}$ is Kramers-class escape from engineered low-$\sigma$ pathways. The $\tau_{(\mathrm{iii})}^{(A)}$ is environmental binding from Purcell + dielectric + quasiparticle channels. JJ-class engineering at the (ii) boundary recovers WKB MQT structure directly from DCGT.

**$M_B$ — Class B projection.** All three timescales are gap-suppressed by $\exp(\Delta_\mathrm{top}/T_\mathrm{eff})$. Binding shifts from environmental rate to topology-perturbation rate $\tau_\mathrm{gap-stab}(\mathcal{T})$, set by macroscopic substrate quality (sample homogeneity, edge purity, defect density, anyonic fusion-error rates), not by local environmental coupling. For Majorana platforms with $\Delta_\mathrm{top} \sim 0.1$ meV at $T_\mathrm{eff} \sim 20$ mK, the gap factor is order $10^{25}$. Class B can in principle exceed Class A coherence by exponential factors at the cost of much harder topology engineering.

**$M_C$ — Class C projection.** Three redundancy modifiers apply: $g(N)$ suppresses effective $\mathcal{M}$ (Class C *relaxes* condition (i)); $h(N)$ enhances effective $\Gamma_\mathrm{cross}$; $c(N) \sim \exp(-N/N_\mathrm{corr})$ suppresses effective $\Lambda$ until correlation budget saturates. Class C ceiling: $\tau_\mathrm{QC}^{C, \mathrm{ceil}} = \tau_\mathrm{QC}^\mathrm{single} \cdot e$ asymptotically. Class C is **bounded-redundancy-advantage** — it cannot exceed single-pathway ceilings without bound; its role is extending the useful operating window before saturation.

### 7.7.3 Meta-architectural overlays

Meta-architectures appear as boundary-condition modifiers, not new projections:

- **Dynamical decoupling.** Replaces $\Lambda_\mathrm{env}^{(K)}$ with a temporally-averaged $\Lambda_\mathrm{env}^\mathrm{DD}(\omega_\mathrm{decoup})$.
- **Reservoir engineering.** Increases $A_\mathcal{S}$ in the multiplicity dynamics via structured environmental coupling.
- **Error correction.** Recursive overlay: $\tau_\mathrm{QC}^\mathrm{logical}$ is derived from $\tau_\mathrm{QC}^\mathrm{phys}$ via code distance and threshold. The meta-architecture takes the physical $M$ and applies a *recursive overlay* at the logical level, outputting the logical $M$.
- **Hybrid composition.** $\min$ over subsystems' projections plus losses at handoff boundaries; no new projection.

### 7.7.4 OQ closure status

Arc Q-COMPUTE's seven memos closed seven open questions during the arc's development. The Block-D level result (this section's content) closes:

- $M$ is one substrate object with three class-projections plus meta-architectural overlays, not three independent functions. (OQ-4 closed.)
- The matter-wave Q-C boundary at 140–250 kDa is in $M_A$'s $\tau_{(\mathrm{i})}$ static-failure branch. The qubit-system multiplicity walls of various platforms lie at corresponding evaluation points of $M_A$ and the meta-architectures. The cross-platform identity is a substrate-level structural consequence. (OQ-5 closed.)
- Specific functional shapes of $\mu, \kappa, g/h/c(N)$ are INHERITED at the same level as $\log g$ in BH-5 (Chapter 13). (OQ-7 closed to INHERITED level.)

## 7.8 Cross-Platform Unification: Matter-Wave ↔ Qubit-System Identity

### 7.8.1 The strongest output

The framework's strongest cross-platform result is the substrate-level identity between two empirically distinct phenomena: the matter-wave quantum-classical boundary at 140–250 kDa molecular mass and the qubit-system multiplicity walls of various Class A platforms. These are not analogous phenomena; they are the *same* substrate-determined boundary projected onto two different platforms via shared substrate constants.

The matter-wave boundary is observed in matter-wave interferometry experiments. Below the boundary, large molecules show interference fringes consistent with quantum-mechanical superposition. Above the boundary, fringes wash out and the molecule behaves classically. The boundary is empirically located at 140–250 kDa molecular mass, depending on molecular structure, internal-DOF activation, and environmental conditions.

The qubit-system multiplicity wall is the structural ceiling on Class A QC platforms. Each platform (transmon SC qubits, fluxonium SC qubits, trapped ions, photonic gate-model) has an architecture-specific scaling function $f_\mathrm{sys}^{(A)}(\mathcal{S})$ mapping system size to effective system multiplicity. At a substrate-determined system size $N_\star$ (the platform-specific wall), $f_\mathrm{sys}^{(A)}$ crosses $\mathcal{M}_\mathrm{crit}$ and the platform's effective coherence collapses.

The substrate-level identity: both the matter-wave boundary mass $M_\star$ and the qubit-system $N_\star$ are crossings of the same substrate constant $\mathcal{M}_\mathrm{crit}$, evaluated for two different scaling-function inputs. Sharper measurement of $M_\star$ directly constrains the substrate constant $\mathcal{M}_\mathrm{crit}$, which in turn constrains $N_\star$ for any qubit platform with a calibrated $f_\mathrm{sys}^{(A)}$.

### 7.8.2 Implications

The identity has direct consequences for the QC roadmap:

- **Matter-wave interferometry becomes a direct probe of QC ceilings.** The Vienna and Basel matter-wave-interferometry programs are reframed as the cleanest available probe of the substrate constant $\mathcal{M}_\mathrm{crit}$ that determines qubit-array walls. Investment in matter-wave-boundary measurement (mass-matched isomer experiments, ultra-cold-vacuum extension, internal-DOF-controlled molecular probes) is investment in characterizing the limits of the qubit-based QC roadmap.
- **The two communities study the same substrate phenomenon.** The matter-wave-interferometry program (foundational physics, no commercial QC application) and the SC-qubit-scaling program (commercial QC, no foundational-physics application) are studying the same substrate-determined boundary from two empirical directions.
- **Cross-platform calibration is structurally valuable.** A national or institutional research program coordinating matter-wave-boundary measurement with qubit-platform multiplicity tomography produces consistency checks unavailable in either community alone.

### 7.8.3 Sharp predictions

The cross-platform identity supports sharp predictions:

- **Class A → Class C transition is mandatory at the wall.** Pure Class A scaling cannot pass the substrate-determined system-multiplicity wall. The path past the wall is composition with logical-qubit encoding (Class C); error correction is the standard meta-architectural composition that achieves this.
- **Class B exponential coherence advantage.** Topological qubits can outrun Class A coherence by an exponential factor $\exp(\Delta_\mathrm{top}/T_\mathrm{eff})$ in the topological gap, but only if topology engineering can deliver stable gaps. The binding shifts from isolation engineering to topology engineering.
- **Class C correlation-budget plateau.** Redundancy-based architectures saturate at a substrate-determined correlation budget $N_\mathrm{corr}$. Beyond this, additional redundancy stops paying.
- **Cross-class architectural transitions.** A → C mandatory at the wall; B overtakes A at $\Delta/T \gtrsim 10$–20; C saturates at $N_\mathrm{corr}$.

These are testable structural predictions with explicit falsification conditions. The QC sector's empirical anchor map is developed in Chapter 15 (Public Test Inventory).

## 7.9 What QC in ED Does and Does Not Deliver

### 7.9.1 What is delivered

- A substrate-level account of quantum computation grounded in UR-1.
- Three exhaustive architectural classes (A, B, C) characterizing protection strategies.
- The multiplicity-cap function $M$ as the substrate-level cross-platform unifier.
- Cross-platform unification between the matter-wave Q-C boundary and qubit-system multiplicity walls.
- Falsifiable predictive content with explicit sharp/structural/inherited demarcation.
- Cross-domain consistency with all prior closed arcs (Phase-1, T17, T18, DCGT, Arc SG, Arc BH).
- Six explicit OPEN extensions named for follow-on work (closed-form $\mathcal{M}_\mathrm{crit}$; architecture-to-platform calibration; closed-form $g/h/c(N)$; topology-stability theorem for Class B; surface-code recursive-overlay derivation; hybrid-architecture handoff dynamics).

### 7.9.2 What is not delivered

- Closed-form values for INHERITED parameters ($\mathcal{M}_\mathrm{crit}$, $N_\mathrm{corr}$, $\Delta_\mathrm{top}^{\max}$, etc.). These are calibrated empirically; the closed-form-substrate-constants program is downstream open work.
- A constructive recipe for fault-tolerant quantum computing. The arc is structural, not engineering. Engineering against the substrate-level binding constraints is exactly the right work in the appropriate regime; the framework changes the *interpretive frame* under which engineering progress is evaluated, not the engineering itself.
- Specific numerical predictions for any specific QC platform. Architecture-to-platform calibration (O-QC-2) is the engineering-tractable program that converts the framework's structural predictions into platform-specific numerical bounds.
- A claim that practical-scale QC is achievable or impossible. The framework predicts *which substrate-level wall is binding at what scale* and *which architectures can outrun which walls* — not whether the engineering effort to reach a given scale will or will not succeed.

### 7.9.3 The decisive falsifier

The framework's central falsifier is the cross-platform unification claim. If a future platform is identified that exhibits coherence behavior consistent with no class assignment in {A, B, C}, cannot be explained as meta-architectural composition of A/B/C, and fails to match $M$ under any substrate-allowed parameter calibration, then the framework needs extension (introduce a Class D) or replacement.

Conversely, continued cross-anchor consistency over the next decade of platform development — particularly the consistency of $\mathcal{M}_\mathrm{crit}$ extracted from matter-wave-boundary measurement with $\mathcal{M}_\mathrm{crit}$ inferred from qubit-platform multiplicity walls — is significant cross-platform evidence for the substrate framework.

## 7.10 Form-FORCED vs Value-INHERITED at the QC Architecture

### 7.10.1 What is form-FORCED

- **UR-1's three-condition characterization** of the unresolved-rule regime.
- **The three-factor product form of $\mathcal{U}$** (multiplicity headroom × rule-spanning connectivity × commitment-survival).
- **The QC operating window structure** $\tau_\mathrm{QC} = \min(\tau_{(\mathrm{i})}, \tau_{(\mathrm{ii})}, \tau_{(\mathrm{iii})})$.
- **The three-class architectural exhaustiveness** at substrate-level base.
- **The reframing of meta-architectures** (error correction, dynamical decoupling, reservoir engineering, hybrid composition) as compositions or techniques rather than new substrate-level strategies.
- **The multiplicity-cap function $M$** as one substrate object with three projections plus meta-architectural overlays.
- **The static-failure branch** of $\tau_{(\mathrm{i})}$ at $\mathcal{M}_\mathrm{floor} = \mathcal{M}_\mathrm{crit}$.
- **The exponential gap-suppression** of all three timescales in Class B by $\exp(\Delta_\mathrm{top}/T_\mathrm{eff})$.
- **The correlation-budget plateau** in Class C with bounded redundancy advantage.
- **The cross-platform identity** between matter-wave Q-C boundary and qubit-system multiplicity walls via shared $\mathcal{M}_\mathrm{crit}$.
- **The WKB-form recovery of MQT** from DCGT $\kappa$-function evaluation at engineered JJ barriers.
- **Three cross-class architectural transitions** (A → C mandatory, B overtakes A, C saturation).

### 7.10.2 What is value-INHERITED

- **$\mathcal{M}_\mathrm{crit}$.** Anchored empirically by matter-wave Q-C boundary at 140–250 kDa. Closed-form derivation is open (O-QC-1).
- **$\Gamma_\mathrm{min}$.** Minimum cross-bandwidth for hydrodynamic-window resolution.
- **$\Lambda_{V1}$.** V1 vacuum residual injection rate; bounds Class A perfect-isolation ceiling.
- **$\beta_\mathrm{crit} \sim \log(R_\mathrm{cg}/\ell_P)$.** Critical gradient threshold for decoupling-surface formation; substrate-determined dimensionless number.
- **$N_\mathrm{corr}$.** Correlation budget for Class C platforms; INHERITED, platform-specific.
- **$\Delta_\mathrm{top}^{\max}$.** Maximum stable topological gap for Class B platforms.
- **$T_\mathrm{eff}^{\min}$.** Minimum substrate-equivalent perturbation temperature.
- **Specific shapes of $\mu, \kappa, g(N), h(N), c(N)$.** Form-FORCED to be monotone with specific limits; specific functional shapes INHERITED.
- **Architecture-specific scaling functions** $f_\mathrm{sys}^{(A)}(\mathcal{S})$. INHERITED from architecture-to-platform calibration (O-QC-2).
- **Platform-specific $N_\star$ values.** Determined by architecture-specific $f_\mathrm{sys}^{(A)}$ + the substrate-shared $\mathcal{M}_\mathrm{crit}$.

### 7.10.3 Six open extensions

Six O-QC items carried forward as named open extensions:

- **O-QC-1.** Closed-form derivation of $\mathcal{M}_\mathrm{crit}$ from V1 kernel and ED-I-01 substrate constants. Structurally similar in difficulty to closed-form $\log g$ (O2 from Arc BH).
- **O-QC-2.** Architecture-to-platform calibration program. Map $\mathcal{M}_\mathrm{floor}^{(A)}(\mathcal{S})$ for canonical qubit platforms (transmon, fluxonium, trapped ion, photonic) and predict $N_\star$ values via the cross-platform identity with the matter-wave anchor.
- **O-QC-3.** Closed-form $g(N), h(N), c(N)$ for Class C platforms. Currently INHERITED; closed-form derivation requires extending DCGT to multi-axis redundancy structure.
- **O-QC-4.** Topology-stability theorem for Class B. Substrate-level account of $\tau_\mathrm{gap-stab}(\mathcal{T})$ for canonical topological structures (Majorana, Fibonacci anyons, Chern bands).
- **O-QC-5.** Surface-code logical-qubit recursive-overlay derivation. Specific scaling of $\tau_\mathrm{QC}^\mathrm{logical}$ with code distance + threshold from the substrate-level error-correction-as-meta-architecture analysis.
- **O-QC-6.** Hybrid-architecture handoff dynamics. SC-photonic interconnects, topological-SC platforms, and other hybrid architectures' handoff boundaries as substrate-geometric transitions.

## 7.11 Dependencies

### 7.11.1 Upstream

- **Chapter 1.** All thirteen substrate primitives. Especially: P04 bandwidth update rule (multiplicity bound and bandwidth conservation underlying UR-1 condition (i)); P11 commitment-irreversibility (commitment-injection underlying UR-1 condition (iii)); P01 event discreteness, P02 chain worldline structure, P13 proper-time ordering, finite-kernel and substrate-locality commitments.
- **Chapter 2.** Load-bearing invariants — multiplicity $\mathcal{M}$, gradient sparsity $\sigma$, cross-bandwidth $\Gamma_\mathrm{cross}$, V1 finite-width vacuum kernel, P11 commitment-irreversibility. All five enter the QC architectural reading.
- **Chapter 3.** DCGT cross-bandwidth structure $\Gamma_\mathrm{cross} \sim \exp[-\alpha\sigma]$ underlies UR-1 condition (ii). The hydrodynamic-window scale separation is the substrate-level prerequisite for the QC operating regime.
- **Chapter 4.** Theorem 18 kernel-level arrow. Provides the substrate-level structural foundation for P11's directional content as it enters UR-1 condition (iii) commitment-injection accumulation.
- **Chapter 5.** Phase-1 closure. Identifies QC as the engineered occupation of the thin-participation regime characterized by Phase-1; supplies the substrate-level QM foundation on which UR-1's three substrate conditions are formulated.
- **Chapter 6.** T17 gauge-field-as-rule-type and ED-I-13 channel-geometry quantum information. T17 supports the substrate-level vocabulary for participation rules with rule-type label structure; ED-I-13 supplies the multiplicity-as-channel-geometry vocabulary that UR-1's three substrate conditions inherit.

### 7.11.2 Downstream

- **Chapter 13 (Black-Hole Architecture).** Cross-domain $\Gamma_\mathrm{cross}$ collapse mechanism shared with QC condition (ii) failure at scales separated by ~50 orders of magnitude. The substrate condition $|\nabla\rho|\,\ell_P^2/\rho_\mathrm{local} \gtrsim \log(R_\mathrm{cg}/\ell_P)$ unifies horizon formation in BH-2 with $\gamma_{ij}$ collapse in QC condition (ii).
- **Chapter 14 (Cross-Platform Unifications).** The cross-platform identity between matter-wave Q-C boundary and qubit-system multiplicity walls is the strongest cross-platform claim in the program; Chapter 14 develops it as the central output of the cross-domain unification program.
- **Chapter 15 (Public Test Inventory).** Empirical anchors for the QC sector — matter-wave Q-C boundary, JJ MQT, SC qubit T₁/T₂, Hafezi multi-timescale, topological-gap suppression — are catalogued in Chapter 15 with status taxonomy (PASSED / ANCHORED / IN PROGRESS / ACTIVE / OPEN).

## 7.12 Canonical Sources

- `papers/Quantum_Computing_Foundations/`
- Arc Q-COMPUTE memos in `theory/Quantum_Computing/`
- ED-I-23 (Josephson Junctions, Mar 2026)
- ED-I-14 (Topological Effects, Feb 2026)
- ED-I-18 (Multi-Timescale Photonics, Feb 2026)
- ED-I-12 (Photonics, Feb 2026)

The Quantum_Computing_Foundations paper presents the publication-grade architectural account of the QC sector, including UR-1, the three-class taxonomy, the multiplicity-cap function $M$, cross-platform unification, FORCED/INHERITED/OPEN classification, and the conceptual-shift framing (decoherence-centric → multiplicity-centric). Arc Q-COMPUTE memos (seven memos: Opening, UR-1 derivation, failure-mode rates, architectural-class audit, multiplicity-cap function $M$, predictive content, synthesis) develop each component in detail.

ED-I-23 (Josephson Junctions) is the canonical source for the substrate-level account of JJ as engineered ED-bottleneck and the Class A reading. ED-I-14 (Topological Effects) is the canonical source for topological phases as global ED-channel invariants and the Class B reading. ED-I-18 (Multi-Timescale Photonics) is the canonical source for the Class C reading through Hafezi-class multi-axis architectures. ED-I-12 (Photonics) supplies the broader photonic substrate-level account underlying gate-model photonic platforms.

The Monograph Shell's Appendix A theorem provenance map lists UR-1 with its substrate-input dependencies. The Notation Glossary in Appendix B lists the symbols used in this chapter, including $\mathcal{U}$, $\mathcal{M}$, $\sigma$, $\gamma_{ij}$, $\Lambda$, $\tau_\mathrm{QC}$, $M(\mathcal{S}, K, \mathcal{E}, \mathcal{O})$, $\mathcal{M}_\mathrm{crit}$, $\Gamma_\mathrm{min}$, $N_\mathrm{corr}$, $\Delta_\mathrm{top}$, $T_\mathrm{eff}$, $\mu$, $\kappa$, $g(N)$, $h(N)$, $c(N)$, $f_\mathrm{sys}^{(A)}$.

## 7.13 Optional Figures

**Figure 7.1 — The substrate-level reframing.** A two-column diagram. Left column ("Standard QC framing"): coherence as state property; decoherence as coupling rate; engineering target = reduce coupling. Right column ("ED substrate framing"): coherence as integrity of unresolved participation rule; decoherence as P11 commitment events at endpoints; engineering target = hold low-$\mathcal{M}$, high-$\gamma$, low-$\Lambda$ regime. A central arrow labeled "the upstream variable is multiplicity $\mathcal{M}$, not decoherence rate" makes the reframing explicit.

**Figure 7.2 — UR-1's three conditions and the QC operating window.** A diagram showing the three failure-mode timescales $\tau_{(\mathrm{i})}$, $\tau_{(\mathrm{ii})}$, $\tau_{(\mathrm{iii})}$ as horizontal bars of variable length. The QC operating window $\tau_\mathrm{QC} = \min(\cdot)$ is highlighted as the shortest bar. Labels identify the substrate-level mechanism each timescale corresponds to: (i) multiplicity proliferation; (ii) cross-bandwidth collapse; (iii) commitment-injection accumulation. A note identifies which condition binds for each canonical empirical anchor.

**Figure 7.3 — The three-class taxonomy.** A radial diagram with $M$ at the center and three spokes labeled Class A (engineered-low-multiplicity), Class B (global-geometric-rigidity), Class C (high-multiplicity-redundancy). Each spoke is annotated with: the protection target (which UR-1 condition is structurally fixed); the substrate mechanism; the typical binding constraint; example platforms (SC qubits / ions / photonic for A; topological qubits / Chern channels for B; bosonic codes / multi-timescale photonics for C).

**Figure 7.4 — Meta-architectures as compositions.** A diagram showing how the four meta-architectural strategies (dynamical decoupling, reservoir engineering, error correction, hybrid composition) reduce to compositions or techniques over the three substrate-level base classes. Each meta-architecture is labeled with which class it extends or composes.

**Figure 7.5 — The multiplicity-cap function $M$ and its three projections.** A schematic with $M(\mathcal{S}, K, \mathcal{E}, \mathcal{O})$ as a single substrate object. Three projection arrows extend to $M_A$, $M_B$, $M_C$, each annotated with the class-specific modifier (multiplicity static-failure for A, gap-suppression $\exp(\Delta_\mathrm{top}/T_\mathrm{eff})$ for B, redundancy modifiers $g/h/c(N)$ for C). Meta-architectural overlays $\mathcal{O}$ are shown as annotations on each projection.

**Figure 7.6 — The cross-platform identity.** A diagram with two empirical phenomena on the left (matter-wave Q-C boundary at 140–250 kDa; qubit-system multiplicity wall at platform-specific $N_\star$) and a single substrate constant $\mathcal{M}_\mathrm{crit}$ on the right. Arrows from each empirical phenomenon converge on $\mathcal{M}_\mathrm{crit}$, indicating that both are crossings of the same substrate threshold projected onto two different platform-scaling functions $f_\mathrm{sys}^{(A)}$. A note observes that sharper measurement of either anchor constrains the other.

**Figure 7.7 — Form-FORCED vs Value-INHERITED at QC.** A two-column diagram. Left column ("Form-FORCED"): UR-1 three-condition characterization, three-factor product form of $\mathcal{U}$, three-class architectural exhaustiveness, $M$ as one substrate object with three projections, cross-platform identity, exponential gap-suppression in Class B, correlation-budget plateau in Class C. Right column ("Value-INHERITED"): $\mathcal{M}_\mathrm{crit}$, $\Gamma_\mathrm{min}$, $N_\mathrm{corr}$, $\Delta_\mathrm{top}^{\max}$, specific functional shapes of $\mu/\kappa/g/h/c$, architecture-specific $f_\mathrm{sys}^{(A)}$, platform-specific $N_\star$. The figure makes visible the demarcation that propagates through Chapter 14's cross-platform unification analysis.

**Figure 7.8 — The cross-domain $\Gamma_\mathrm{cross}$ collapse echo.** A length-scale diagram showing the same DCGT-derived exponential structure $\Gamma_\mathrm{cross} \sim \exp[-\alpha\int_\mathrm{path}\sigma\,d\ell]$ producing phenomena at scales separated by ~50 orders of magnitude: Josephson-junction MQT at $\sim 10^{-9}$ m; QC condition (ii) failure at $\sim 10^{-3}$ m; black-hole horizon formation at $\sim 10^{4}$ m for stellar-mass black holes. The figure makes visible the cross-domain identity between QC condition (ii) failure and BH-2 horizon formation.
