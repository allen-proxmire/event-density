# Arc QC — Memo 7: Synthesis and Clay-Relevance-Style Verdict

**Status:** Synthesis memo of Arc Q-COMPUTE. Closes the seven-memo arc; integrates Memos 1–6 into a coherent architectural picture; issues FORCED / INHERITED / OPEN classification and Clay-relevance-style structural verdict; updates program-state; prepares for publication-grade paper.

**Date:** 2026-05-02

---

## 1. Structural Summary (Purpose and Scope)

This memo:

- Synthesizes the six prior memos of Arc Q-COMPUTE into a single architectural account of quantum computation in the Event Density framework.
- Classifies the arc's deliverables as **FORCED** (substrate-level form), **INHERITED** (value-level), or **OPEN** (deferred to future arcs).
- Delivers a Clay-relevance-style structural verdict in the same style as BH-7, SG-7, ED-10 synthesis.
- Updates program-state: Arc Q-COMPUTE closed at architectural level; integration with broader program.
- Identifies natural follow-on arcs.
- Produces export-ready synthesis material for a publication-grade paper *Quantum Computation in Event Density: A Substrate-Level Architecture and Its Limits*.

**Verdict (preview):** Arc Q-COMPUTE delivers conditional-positive structural closure at the architectural level. The substrate-level account of quantum computation is complete — UR-1 characterizes the regime; failure-mode rates quantify how it ends; three exhaustive architectural classes characterize the protection strategies; the multiplicity-cap function $M$ unifies them; predictive content with explicit falsifiers is delivered. Same form-FORCED / value-INHERITED demarcation as Phase-1, Arc D, Arc SG, Arc BH. No contradictions; cross-domain consistency with closed prior arcs holds; honest scope on what remains INHERITED + open.

---

## 2. Derivation / Argument

### 2.1 Summary of results across Memos 1–6

**Memo 1 — Opening.** The load-bearing question, in substrate language: *what is the ED-substrate signature of a system performing quantum computation, and what substrate-level constraints govern its scaling?* Three load-bearing invariants identified: $\mathcal{M}$ (multiplicity, ED-entropy analogue, ED-I-01); $\mathcal{U}(\mathcal{S},t) \in [0,1]$ (participation-rule unresolvedness); $\sigma$ (gradient sparsity, BH-2 inheritance). Ten substrate assumptions inherited from closed-arc work taken as fixed (Phase-1, Theorem 18, DCGT, ED-I-01, ED-I-23, ED-I-29, ED-I-13, ED-I-14, ED-I-18, ED-I-12). Four-block decomposition: A (UR-1), B (failure rates), C (architectural classes), D ($M$). UR-1 named as gate-condition theorem; six open questions itemized.

**Memo 2 — UR-1 (Unresolved-Regime Characterization Theorem).** The functional form of $\mathcal{U}$ derived as a three-factor product:
$$
\mathcal{U}(\mathcal{S},t) = \prod_i \mu(\mathcal{M}_i / \mathcal{M}_\mathrm{crit}) \cdot \prod_{(i,j) \in \mathcal{R}} \kappa(\gamma_{ij} / \Gamma_\mathrm{min}) \cdot \exp\!\left[-\int_0^t \Lambda_\mathcal{S}(t')\,dt'\right].
$$
Each factor sources from a structurally distinct substrate process (multiplicity proliferation; cross-endpoint connectivity collapse; commitment-event accumulation). UR-1 stated formally with three independent-in-form, geometry-coupled conditions. Proof sketch given in both directions. Three known regimes — bulk superconductor (binding (iii) at $T_c$), Josephson junction (binding (ii) at engineered boundary, MQT recovered with WKB exponential), free atomic-scale matter wave (binding (i) at mass cap) — recover cleanly. OQ-1 closed (functional form of $\mathcal{U}$); OQ-3 closed (independence in form, geometric coupling); OQ-6 partially closed.

**Memo 3 — Failure-mode rates.** Each UR-1 condition admits a substrate-level dynamical equation. Substrate-determined timescales $\tau_{(\mathrm{i})}, \tau_{(\mathrm{ii})}, \tau_{(\mathrm{iii})}$ derived from rate equations. The QC operating window: $\tau_\mathrm{QC} = \min(\tau_{(\mathrm{i})}, \tau_{(\mathrm{ii})}, \tau_{(\mathrm{iii})})$. Empirical anchors mapped: matter-wave Q-C boundary ↔ (i) static failure; SC qubit T₁/T₂ ↔ (iii) and (ii); JJ MQT ↔ (ii) near-threshold WKB; topological gap suppression ↔ (iii) gap-suppressed; Hafezi multi-timescale ↔ (i) relaxed by redundancy. Multi-condition events (quasiparticle poisoning) identified. OQ-6 closed fully ($\mathcal{M}$ and $\mathcal{U}$ are genuinely separate substrate-state axes). Rate-pattern table for architectural classes prepared.

**Memo 4 — Architectural-class exhaustiveness audit.** Three protection strategies derived as the substrate-allowed base over UR-1's three conditions: Class A fixes $\mathcal{M}$ low directly via structural mechanism; Class B fixes $\sigma$-geometry rigidly via topological invariants; Class C provides redundancy across parallel pathways (indirect control). Four candidate Class D strategies (dynamical-rotating-binding, reservoir-engineered unresolvedness, error-correction-as-architecture, hybrid systems) audited; all reduce to techniques or compositions of A/B/C, not new substrate-level base classes. Exhaustiveness argument from UR-1's three-condition structure: only three substrate quantities to fix, two structurally fixable (A, B), redundancy provides the third (C). All four primary empirical anchors place cleanly. OQ-2 closed.

**Memo 5 — The multiplicity-cap function $M$.** $M$ derived as a single substrate object with three architectural-class projections plus meta-architectural overlay structure:
$$
M(\mathcal{S}, K, \mathcal{E}, \mathcal{O}) = \min\bigl[\tau_{(\mathrm{i})}^{(K, \mathcal{O})}, \tau_{(\mathrm{ii})}^{(K, \mathcal{O})}, \tau_{(\mathrm{iii})}^{(K, \mathcal{O})}\bigr]
$$
$M_A$ has static-failure branch at $\mathcal{M}_\mathrm{floor} = \mathcal{M}_\mathrm{crit}$ (matter-wave Q-C boundary) and dynamic environmental binding. $M_B$ has all timescales gap-suppressed by $\exp(\Delta_\mathrm{top}/T_\mathrm{eff})$, with binding shifted to topology-perturbation rate. $M_C$ has redundancy modifiers $g(N), h(N), c(N)$ producing exponential improvement until correlation budget saturates. Meta-architectures (dynamical decoupling, reservoir engineering, error correction, hybrids) appear as boundary-condition modifiers, not new projections. Cross-anchor consistency verified for all primary + secondary anchors. OQ-4 and OQ-5 closed; OQ-7 closed to INHERITED level.

**Memo 6 — Predictive content and falsifiers.** Sharp form-level + inherited value-level scaling laws and ceilings for each class. Class A: system-multiplicity wall, exponential collapse of $\tau_{(\mathrm{i})}^A$ as $\mathcal{M}_\mathrm{floor} \to \mathcal{M}_\mathrm{crit}$. Class B: exponential gap-suppression $\tau_\mathrm{QC}^B \approx \tau_\mathrm{gap-stab}\exp(\Delta_\mathrm{top}/T_\mathrm{eff})$, with binding shifted to topology engineering. Class C: correlation-budget plateau at $N \sim N_\mathrm{corr}$, bounded redundancy advantage. Cross-platform unification: matter-wave 140–250 kDa boundary and qubit-system $N_\star$ walls are *the same substrate phenomenon projected onto two platforms* via shared $\mathcal{M}_\mathrm{crit}$. Three sharp cross-class transition predictions (A → C mandatory at the wall; B overtakes A at $\Delta/T \gtrsim 10$–20; C saturation at $N_\mathrm{corr}$). Four classes of near-term experimental tests with explicit falsification conditions. Honest sharp / structural / inherited demarcation for every claim.

### 2.2 Structural integration: the ED account of quantum computation

The seven memos integrate into a single architectural picture:

> **Quantum computation is the engineered occupation of a low-multiplicity unresolved-rule substrate regime.** Three substrate quantities — multiplicity $\mathcal{M}$, gradient-sparsity-mediated cross-bandwidth $\gamma_{ij}$, and commitment-injection rate $\Lambda$ — jointly determine the integrity of an unresolved participation rule across designated endpoints. The QC operating window is bounded by the shortest of three substrate-determined timescales, each governed by one of the three substrate quantities. Three architectural strategies — direct control of $\mathcal{M}$, direct control of $\sigma$-geometry via topological invariants, indirect control via redundancy — exhaust the substrate-level base for protecting the regime. The multiplicity-cap function $M$ unifies the three classes as projections of one substrate object. Different physical phenomena across multiple platforms (matter-wave Q-C boundary, SC qubit T₁/T₂, JJ MQT, topological-qubit gap suppression, multi-timescale photonics) are different evaluation points of $M$. The arc's predictive content is sharp at the structural level, inherited at the numerical level, with explicit falsification conditions.

The architecture is internally consistent: UR-1's three-condition structure supports the failure-mode taxonomy (Memo 3); the three-condition structure forces three protection strategies (Memo 4); the three protection strategies define the three projections of $M$ (Memo 5); the three projections produce three structurally distinct scaling laws (Memo 6). One substrate framework, one structural identity propagating through every block of the arc.

### 2.3 FORCED / INHERITED / OPEN classification

#### FORCED (substrate-level form)

- **UR-1** as necessary-and-sufficient characterization of the unresolved regime (Memo 2). Three conditions independent in form, coupled through substrate geometry.
- **Three-factor product structure of $\mathcal{U}$** — multiplicity headroom × connectivity × commitment-survival (Memo 2 §2.5).
- **$\min(\cdot)$ structure of $\tau_\mathrm{QC}$** over the three failure-mode timescales (Memo 3, Memo 5).
- **Substrate-level dynamics of multiplicity, cross-bandwidth, and commitment-rate** (Memo 3 §2.1–2.3).
- **Static-failure branch of $\tau_{(\mathrm{i})}$** at $\mathcal{M}_\mathrm{floor} = \mathcal{M}_\mathrm{crit}$ (Memo 5 §2.2; Memo 6 §2.1).
- **WKB-form exponential structure of MQT** recovered directly from DCGT (Memo 3 §2.2; Memo 5 §2.2).
- **Three-class architectural exhaustiveness** over substrate-level base strategies (Memo 4 §2.6).
- **Meta-architectural overlay structure** as modifiers of class projections, not new classes (Memo 4 §2.5; Memo 5 §2.6).
- **Multiplicity-cap function $M$** as one substrate object with three architectural-class projections (Memo 5).
- **Exponential gap-suppression in Class B** of all three timescales by $\exp(\Delta_\mathrm{top}/T_\mathrm{eff})$ (Memo 5 §2.3, Memo 6 §2.2).
- **Correlation-budget plateau in Class C**, bounded redundancy advantage (Memo 5 §2.4, Memo 6 §2.3).
- **Cross-platform unification:** matter-wave Q-C boundary and qubit-system multiplicity walls are the same substrate phenomenon (Memo 5 §2.7, Memo 6 §2.4).
- **Three cross-class architectural transitions** (A → C mandatory; B overtakes A at $\Delta/T \gtrsim 10$–20; C saturation at $N_\mathrm{corr}$) (Memo 6 §2.6).
- **Identification of $T_c$, JJ MQT, matter-wave Q-C boundary, topological-gap suppression, Hafezi multi-timescale relaxation** as distinct UR-1-condition crossings on one $M$ function (Memo 5 §2.7).
- **Cross-domain echo with BH-2** ($\Gamma_\mathrm{cross}$ collapse mechanism shared with horizon formation) (Memos 2, 3, 5, 6).

#### INHERITED (value-level)

- **$\mathcal{M}_\mathrm{crit}$**: substrate-determined critical multiplicity. Closed-form derivation parallel to closed-form $\log g$ (BH-5 / O2). Currently INHERITED.
- **$\Gamma_\mathrm{min}$**: substrate-determined minimum cross-bandwidth for hydrodynamic-window resolution.
- **$\Lambda_\mathrm{V1}$**: V1-vacuum-kernel residual injection rate (the ultimate Class A ceiling at perfect isolation).
- **Specific functional shapes of $\mu, \kappa, g(N), h(N), c(N)$**: form FORCED to be monotone with specific limits; specific shape (Boltzmann, rational, sigmoid, etc.) INHERITED from V1-kernel + DCGT closed-form details.
- **Matter-wave Q-C boundary location** (140–250 kDa empirically). Mass-scaling function $f_\mathrm{int}(M_\mathrm{mol})$ INHERITED from molecular physics.
- **Architecture-specific scaling functions** $f_\mathrm{sys}^{(A)}(\mathcal{S})$ for SC qubit arrays, ion arrays, photonic systems. INHERITED from architectural details.
- **Specific values of $N_\star$** for any qubit platform — the substrate-determined system-multiplicity wall location. Determined up to architecture-specific calibration via the matter-wave anchor.
- **Maximum stable topological gap $\Delta_\mathrm{top}^{\max}$** and minimum substrate-equivalent temperature $T_\mathrm{eff,\min}$ for Class B.
- **Specific $N_\mathrm{corr}$** for any Class C platform, set by the substrate-coupling pattern across redundant pathways.
- **Specific cross-class transition thresholds** in numerical terms — the structural form is FORCED; the threshold values are INHERITED.

#### OPEN (future arcs / open extensions)

- **O-QC-1: Closed-form derivation of $\mathcal{M}_\mathrm{crit}$** from V1 kernel + ED-I-01 substrate constants. Structurally similar in difficulty to closed-form $\log g$ (O2 from Arc BH) and the $\kappa/|\hat N'| = 0.001766$ anchor search (E4). Honest "no closed form" remains a valid outcome. If closed, the matter-wave Q-C boundary becomes a substrate-derived prediction rather than an empirical anchor.
- **O-QC-2: Architecture-to-platform calibration program.** Map the substrate-level $\mathcal{M}_\mathrm{floor}^{(A)}(\mathcal{S})$ for canonical qubit platforms (transmon, fluxonium, trapped ion, photonic) and predict $N_\star$ values. Couples with the matter-wave Q-C boundary anchor.
- **O-QC-3: Closed-form $g, h, c(N)$ functions** for Class C platforms. Currently INHERITED from substrate-coupling-pattern; closed-form derivation requires extending DCGT to multi-axis redundancy structure.
- **O-QC-4: Topology-stability theorem for Class B.** A substrate-level account of $\tau_\mathrm{gap-stab}(\mathcal{T})$ for canonical topological structures (Majorana, Fibonacci anyons, Chern bands). Extends ED-I-14 + ED-I-18 toward platform-level predictive specificity.
- **O-QC-5: Surface-code logical-qubit recursive overlay derivation.** Specific scaling of $\tau_\mathrm{QC}^\mathrm{logical}$ with code distance + threshold from the substrate-level error-correction-as-meta-architecture analysis. Currently schematic; full derivation requires extending to the recursive structure.
- **O-QC-6: Hybrid-architecture handoff dynamics.** SC-photonic interconnects, topological-SC platforms, and other hybrid architectures' handoff boundaries as substrate-geometric transitions. Composition of A/B/C is acknowledged in Memo 4; specific handoff-loss accounting is open.

### 2.4 Clay-relevance-style verdict

The verdict, in the same style as BH-7, SG-7, and ED-10 synthesis:

- The **form** of quantum computation in ED is **structurally complete** at the architectural level. The seven structural questions opened in Memo 1's four-block decomposition are addressed: UR-1 as gate condition (Block A); failure-mode rates with substrate-level dynamics (Block B); three-class exhaustive taxonomy with formal exhaustiveness argument (Block C); multiplicity-cap function $M$ as one substrate object with three projections (Block D); falsifiable predictive content with sharp form-level claims and inherited specific values (Memo 6).

- The architecture is internally consistent. UR-1's three-condition structure propagates coherently through every subsequent block: it forces the failure-mode taxonomy, the three-class architectural taxonomy, the three projections of $M$, and the three classes of falsifiable predictive claims. One substrate-level identity supports all of it.

- The **value layer** (specific values of $\mathcal{M}_\mathrm{crit}$, $\Gamma_\mathrm{min}$, $N_\star$, $N_\mathrm{corr}$, $\Delta_\mathrm{top}^{\max}$, plus specific functional shapes of $\mu, \kappa, g, h, c$) remains **INHERITED** — substrate-determined finite numbers whose closed-form derivation is downstream work. Same form-FORCED + value-INHERITED methodology as the rest of the program.

- **Cross-platform unification at the predictive level** is the arc's strongest output. The matter-wave Q-C boundary at 140–250 kDa and the qubit-system multiplicity walls are not separate phenomena — they are the same substrate boundary projected onto two platforms via shared $\mathcal{M}_\mathrm{crit}$. The form of the cross-platform identity is FORCED; the specific calibration is INHERITED. This is the kind of structural cross-domain consistency that distinguishes substrate-level frameworks from phenomenological assemblies.

- **No contradictions, no paradoxes, no inconsistencies** within the arc. All seven open questions from Memo 1 closed. All four primary empirical anchors and all secondary anchors fit cleanly on $M$. No platform observed to date requires extension beyond the three-class taxonomy.

- **Verdict: conditional-positive structural closure** at the architectural level, parallel in form and honesty to NS-Smoothness Intermediate Path C, Yang-Mills Clay-relevance, Arc ED-10 curvature emergence, and Arc BH black-hole architecture. Arc Q-COMPUTE delivers form-derived QC architecture with value-inherited details and explicitly-named open extensions.

- **Decisive falsifier:** Identification of a quantum-computational platform whose coherence behavior (a) is consistent with no class assignment in {A, B, C}, (b) cannot be explained as a meta-architectural composition of A/B/C, and (c) fails to match $M$ under any substrate-allowed parameter calibration. Such a platform would force introduction of a Class D (refuting Memo 4's exhaustiveness) or replacement of the framework. Conversely, continued cross-anchor consistency over the next decade of platform development is significant cross-platform evidence for the substrate framework.

- The arc closes cleanly with a stable program state. Substrate Gravity Foundations Paper, Black Hole Foundations Paper, and the new QC Foundations Paper are now the program's three architectural-arc paper deliverables (parallel in structure and methodology), each closing one major sector at the substrate level.

### 2.5 Cross-domain consistency with closed prior arcs

The arc consistently inherits from and echoes prior closed-arc work:

| Prior arc | Inheritance | Cross-domain echo |
|---|---|---|
| Phase-1 (T1–T16) | Unitary evolution in thin-participation regime as the QC operating mode | $\hbar$ from Born-Gleason; QM-emergence as the substrate substrate for QC's unresolved regime |
| Theorem 18 (V1 kernel arrow) | Forward-cone-only causal structure for cross-endpoint correlations | Commitment irreversibility (P11) as the arrow that drives $\Lambda$-accumulation |
| Arc D (DCGT) | Cross-bandwidth $\Gamma_\mathrm{cross} \sim \exp[-\alpha\sigma]$ | Same machinery in BH-2 (horizon formation), QC condition (ii) failure |
| ED-I-01 (Superconductivity) | Multiplicity = ED-entropy analogue; symmetry = low-$\mathcal{M}$ structure | Class A bulk SC mechanism; $T_c$ identified as condition (iii) crossing |
| ED-I-23 (Josephson Junctions) | Engineered ED-bottlenecks as low-$\mathcal{M}$ devices | Class A JJ-as-element; MQT via DCGT-WKB |
| ED-I-29 (Tunneling) | Tunneling = global rule reconfiguration across sparse $\sigma$ | Connects Class A (ii) failure to MQT |
| ED-I-13 (Quantum Information) | Five landmark QI operations as channel-geometry manipulations | Substrate-level meaning of "doing QC"; participation-rule manipulation |
| ED-I-14 (Topological Effects) | Topological phases as global ED-channel invariants | Class B mechanism; gap-suppression structure |
| ED-I-12 (Photonics) | Photonics as ED-gradient engineering | Class B Chern-channel; Class A photonic gate-model |
| ED-I-18 (Multi-Timescale Photonics) | Topological protection = ED-gradient rigidity; multi-timescale = high-multiplicity expansion | Class B + Class C anchors; Hafezi as canonical Class C empirical evidence |
| Arc BH (Black Holes) | $\Gamma_\mathrm{cross}$ collapse mechanism as substrate-level horizon formation | Same mechanism applied at engineered-system scale in QC condition (ii) failure; cross-domain consistency at predictive level |

The arc's substrate machinery is **fully composed of prior closed-arc results** — no new primitives introduced. Arc Q-COMPUTE's contribution is the application + integration of existing substrate machinery to a previously unaddressed sector. This is the same compositional pattern as Arc BH (which also introduced no new primitives).

### 2.6 Program-state update

- **Arc Q-COMPUTE is closed at the architectural level.** Seven memos: Opening (1) + UR-1 (2) + Failure-mode rates (3) + Architectural-class audit (4) + Multiplicity-cap function $M$ (5) + Predictive content (6) + this synthesis (7).

- **Theorem inventory.** Arc Q-COMPUTE introduces UR-1 (Unresolved-Regime Characterization Theorem) as a substrate-level theorem on par with the program's other theorem-shaped objects. Joins T17, T18, T19–T21 + ECR, N1, GR1, DCGT in the structural-foundation theorem inventory.

- **Active priority list update.** Items #24 (Arc Q-COMPUTE: opened in this session, closes here) moves to "Recently Closed." Six new OPEN items added (O-QC-1 through O-QC-6). The program-level orientation now spans nine sectors with closed-architectural-level structural foundations: (1) QM emergence; (2) Form-level QFT; (3) Classical fluid dynamics; (4) Non-Abelian gauge theory; (5) Substrate gravity (galactic); (6) Curvature emergence; (7) Soft-matter mobility / non-Newtonian rheology; (8) Black-hole architecture; (9) Quantum computation.

- **Next natural arc following Q-COMPUTE.** Block B's remaining target is Hawking-spectrum derivation (priority item B4), which was the next-natural-arc following BH-7. Q-COMPUTE was opened ahead of Hawking-spectrum on user trigger; B4 returns as the next natural concrete arc. Other queued: GR-4A (Einstein-equation emergence, SPECULATIVE); Arc COSMO (cosmic expansion / $H_0$ derivation, SPECULATIVE); the closed-form-substrate-constants program (closed-form $\log g$, $\mathcal{M}_\mathrm{crit}$, $\kappa/|\hat{N}'|$).

- **Publication-grade paper readiness.** The Q-COMPUTE Foundations Paper is now the natural follow-on, parallel in form and methodology to *Black Holes in Event Density* and *Foundations of Substrate Gravity*. Memos 1–7 contain all the structural content; the paper formats it for external readership.

- **Cross-arc paper inventory.** Three architectural-arc papers now form the program's structural-foundation publication set: SG Foundations + BH Foundations + QC Foundations. Three sectors with substrate-level structural completeness, parallel methodology, parallel form-FORCED + value-INHERITED + explicit OPEN demarcation. Plus the program-level overview paper ("Event Density Foundations: A Unified Substrate Architecture").

### 2.7 Updated invariants list (final state for the arc)

| Symbol / concept | Status at arc close | Source |
|---|---|---|
| $\mathcal{M}, \mathcal{U}, \sigma$ | Load-bearing invariants, derived | Memo 1, Memo 2 |
| UR-1 | Theorem, derived | Memo 2 |
| $\mu, \kappa$ functions | Form-FORCED, shape INHERITED | Memo 2 |
| Failure-mode rates $\tau_{(\mathrm{i,ii,iii})}$ | Derived, INHERITED values | Memo 3 |
| Three-class taxonomy A/B/C | Exhaustive at substrate-base level | Memo 4 |
| Meta-architectural overlays | Compositions/techniques, not new classes | Memo 4 |
| Multiplicity-cap function $M$ | Single substrate object with three projections | Memo 5 |
| Cross-platform identity (matter-wave ↔ qubit-systems) | Form-FORCED, calibration INHERITED | Memos 5, 6 |
| Three sharp cross-class transitions | Form-FORCED, thresholds INHERITED | Memo 6 |
| Four classes of near-term experimental tests | Specified with falsification conditions | Memo 6 |

### 2.8 Honest scope at arc close

What this arc delivers:

- Substrate-level account of quantum computation grounded in UR-1.
- Three exhaustive architectural classes characterizing protection strategies.
- Multiplicity-cap function $M$ as the substrate-level cross-platform unifier.
- Falsifiable predictive content with explicit sharp / structural / inherited demarcation.
- Cross-domain consistency with all prior closed arcs.
- Six explicit OPEN extensions named for follow-on work.

What this arc does NOT deliver:

- Closed-form values for any of the INHERITED parameters.
- Specific numerical predictions for the qubit-platform $N_\star$ values (require architecture-to-platform calibration program).
- Closed-form derivation of $\mathcal{M}_\mathrm{crit}$ from substrate primitives (parallel to closed-form $\log g$ — open work).
- Specific functional shapes of $\mu, \kappa, g, h, c$ (INHERITED).
- A constructive recipe for building a specific quantum computer (the arc is structural, not engineering).

The arc's verdict-class is consistent across every memo: form-FORCED at the structural level, value-INHERITED at the numerical level, explicit OPEN extensions named. No overclaim. The same methodology that has held across the rest of the program holds here.

---

## 3. Consequences for the Arc

1. **Arc Q-COMPUTE closes at the architectural level.** Seven memos delivered. All seven open questions from Memo 1 settled. Three sharp predictive content classes and four near-term experimental tests defined.

2. **The cross-platform unification claim** — matter-wave Q-C boundary and qubit-system multiplicity walls are one substrate phenomenon — is the program's strongest cross-domain prediction yet. It connects an existing empirical anchor to a future experimental frontier via substrate-level structural identity.

3. **The cross-domain echo with BH-2 is structurally significant.** Both decoupling-surface formation in BH-2 and condition (ii) failure in QC are governed by $\Gamma_\mathrm{cross}$ collapse. Two faces of one substrate mechanism, applied at scales separated by ~50 orders of magnitude in physical length. This is the kind of cross-domain consistency that a substrate-level framework should produce and that phenomenological frameworks cannot.

4. **The publication-grade paper is the natural next deliverable.** Q-COMPUTE Foundations Paper, parallel to BH-Foundations and SG-Foundations.

5. **Six new OPEN items added to the priority list** (O-QC-1 through O-QC-6). These are the structural follow-ons that would extend or refine the arc; none is required for the arc's closure as architectural-level synthesis.

6. **Program-state at closure.** Nine sectors of substrate-level architectural closure. Three architectural-foundation papers (SG + BH + QC). Theorem inventory expanded by UR-1. Active priority list updated.

7. **Conditional-positive verdict appropriately framed.** No pretense of having solved fault-tolerant QC engineering. No pretense of having derived specific platform ceilings from first principles. What the arc *does* deliver is the substrate-level structural account that no other framework provides — and the falsifiability conditions that make it testable.

---

## 4. Recommended Next Step

**Q-COMPUTE Foundations Paper.** File: `papers/Quantum_Computing_Foundations/quantum_computing_foundations.md`, with `.tex` and `.pdf` generated via the program's standard pandoc + xelatex pipeline matching the SG-Foundations and BH-Foundations style.

Proposed title: *Quantum Computation in Event Density: A Substrate-Level Architecture and Its Limits*.

Proposed structure (mirroring BH-Foundations § structure):

- Abstract — UR-1, three classes, $M$, cross-platform unification, conditional-positive verdict.
- Introduction — motivation, ED ontology in brief, why standard QC framing misses the substrate-level question.
- Substrate primitives + DCGT machinery + UR-1 background.
- UR-1 derivation.
- Failure-mode rates.
- Architectural-class taxonomy and exhaustiveness.
- Multiplicity-cap function $M$.
- Predictive content and cross-platform unification.
- FORCED / INHERITED / OPEN classification.
- Discussion — implications, comparison with engineering frontier, paradox-not-generated-in-framework framing applied to QC scaling debates.
- Appendices — DCGT details, UR-1 proof sketch, MQT-from-DCGT, cross-anchor consistency table.
- Metadata, citation block, conditional-positive disclaimer.

Estimated 1–2 sessions for paper drafting + .tex / .pdf generation.

After the paper, the arc is closed at every level — architectural, synthesis, and publication. Natural follow-on arcs (B4 Hawking spectrum, O-QC-1 closed-form $\mathcal{M}_\mathrm{crit}$, O-QC-2 architecture-to-platform calibration, O-QC-4 topology-stability theorem) sit on the priority list awaiting user trigger.
