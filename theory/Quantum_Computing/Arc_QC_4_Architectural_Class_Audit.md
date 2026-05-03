# Arc QC — Memo 4: Architectural-Class Exhaustiveness Audit

**Status:** Memo 4 of Arc Q-COMPUTE. Block C opens. Architect-mode active.

**Date:** 2026-05-02

---

## 1. Structural Summary

This memo audits whether the three hypothesized architectural classes — (A) engineered-low-multiplicity, (B) global-geometric-rigidity, (C) high-multiplicity-redundancy — exhaust the substrate-admissible strategies for maintaining $\mathcal{U} \approx 1$ across UR-1's three conditions.

The audit proceeds in three steps:

1. **Class characterization.** For each of A/B/C, derive how its substrate-geometric configuration enforces its protection target and which mechanism suppresses the two non-target conditions, using closed-arc results.

2. **Class D candidate audit.** Evaluate four candidate strategies — dynamical-rotating-binding, reservoir-engineered unresolvedness, error-correction-as-architecture, hybrid/multi-regime systems — to determine whether any constitutes a genuinely distinct substrate-level protection strategy.

3. **Exhaustiveness verdict.** Argue from UR-1's three-condition structure why the three classes are exhaustive over substrate-level *base* strategies, and characterize meta-architectures as compositions/techniques layered on the three.

**Verdict (preview):** Classes A/B/C are exhaustive over substrate-level base protection strategies. Meta-architectures (dynamical decoupling, reservoir engineering, error correction, hybrids) are *compositions* of A/B/C or *techniques* for extending one of the three timescales; none introduces a fourth substrate-state quantity to fix. **OQ-2 closes.** OQ-4 advances (the multiplicity-cap function $M$ has three architecturally-modulated projections, with meta-architectures appearing as boundary-condition modifiers). OQ-5 advances (matter-wave Q-C boundary is in Class A's $\tau_{(\mathrm{i})}$ projection of $M$).

---

## 2. Derivation / Argument

### 2.1 Class A — engineered-low-multiplicity

**Protection target:** Condition (i) — $\mathcal{M}$ held bounded.

**Substrate-geometric configuration.** The architecture commits structurally to suppressing local multiplicity. The protection target is $\mathcal{M}_\mathrm{floor}$ engineered well below $\mathcal{M}_\mathrm{crit}$, with active architectural restoring (the $A_\mathcal{S}$ term in Memo 3 §2.1) returning $\mathcal{M}$ to floor under environmental perturbation.

**Mechanism — derived from closed-arc results.**

- **Bulk superconductor (ED-I-01).** Lattice symmetry collapses local $\mathcal{M}$ to ≈ 1 by removing branching pathways. Cooper-pairing and BCS coherence are the macroscopic signatures of this collapse; the substrate-level mechanism is symmetry-induced multiplicity suppression. ED-I-01 §3: "the ED-gradients inside the material lock into a low-multiplicity configuration — a state with so few available pathways that ED-flow cannot scatter."

- **Josephson junction qubits (ED-I-23).** A JJ is a deliberately engineered ED-bottleneck: two low-$\mathcal{M}$ SC electrodes separated by a thin barrier whose ED-gradients are sparse enough to support only a small number of participation channels. The transmon, fluxonium, and other JJ-based qubits inherit the SC bulk's $\mathcal{M}$ suppression and add the JJ's barrier-imposed sparsity-bottleneck. ED-I-23 §10: "circuit design becomes the art of shaping ED-gradients so that multiplicity cannot proliferate."

- **Trapped-ion qubits.** A deeply confined ion in a Paul or Penning trap occupies a single low-$\mathcal{M}$ region of substrate. The trap's confining potential creates a local minimum in $\sigma$-geometry where the ion's participation rule has only the engineered (qubit) pathways. Lasers driving Raman transitions act on this low-$\mathcal{M}$ region.

- **Gate-model photonic.** Single-photon states in engineered linear-optical circuits are minimal-channel objects (ED-I-13: minimal channels enforce strict alignment). The mode structure of the circuit suppresses pathway count to those of the engineered modes. Mode mismatch and scattering are $\mathcal{M}$-rises that reduce the effective protected pathway count.

**Suppression of non-target conditions.**

- Condition (ii): The engineered geometry creates low-$\sigma$ corridors between qubit endpoints (e.g., the JJ phase-coherent pathway across the barrier; the photonic waveguide mode; the ion's vibrational ground-state cross-coherence). $\gamma_\mathrm{floor}$ is held above $\Gamma_\mathrm{min}$ by the architectural geometry. Class A handles (ii) by *engineering the substrate gradient profile*, not by topological invariants.

- Condition (iii): Held by *isolation* — physical-shielding-style suppression of $\Lambda_\mathrm{env}$ via dilution refrigerators (SC), ultra-high vacuum + magnetic shielding (ions), low-loss substrates and cryogenic operation. $\Lambda_\mathrm{env}$ is not zero; it is engineered below the threshold for the system's target $\tau_{(\mathrm{iii})}$.

**Binding constraint.** Typically (ii) or (iii) — environmental coupling channels reach through the engineered isolation. T₁ and T₂ for SC qubits are the empirical binding. The architecture's protection on (i) is *strong* (the structural commitment); the binding is whichever environmental channel survives the isolation engineering.

### 2.2 Class B — global-geometric-rigidity

**Protection target:** Condition (ii) — cross-endpoint connectivity rigidly maintained via global topology.

**Substrate-geometric configuration.** The architecture encodes the participation rule in *global ED-channel geometry* — topological invariants of the substrate's gradient structure that cannot be perturbed by local environmental injection. The participation rule's integrity is a property of channel connectivity, not of local timing.

**Mechanism — derived from closed-arc results.**

- **Topological phases as global ED-channel invariants (ED-I-14).** Aharonov-Bohm phases, Berry phases, and Aharonov-Casher phases are all reframed as global invariants of multiply-connected ED-channels with nontrivial curvature. ED-I-14 §8: "topological phases are global invariants of ED-channel geometry. They arise when a chain traverses a channel with nontrivial global curvature. They do not require fields, forces, or potentials—only global structure." A topological qubit encodes information in *which homotopy class* the participation rule traverses, which cannot be changed by local perturbation without spanning the entire channel topology.

- **Photonic Chern channels (ED-I-12 + ED-I-18).** ED-I-12 §5: "negative index arises when the local relaxation direction of ED-flow is inverted relative to the chain's update rule" — engineered ED-gradient inversion produces topologically nontrivial channel structure. ED-I-18 §7: "topological protection is rigidity of ED-gradients. Edge states are high-multiplicity ED-channels that cannot collapse under perturbation. Harmonics inherit this rigidity because they are expressions of the same ED-flow." Photonic Chern channels in the Hafezi multi-timescale lattice carry information through edge-states that remain edge-localized under perturbation by virtue of topological protection.

- **Geometric-phase computing.** Anyonic platforms and Berry-phase quantum gates exploit ED-I-14's degeneracy-sourced parameter-space curvature to produce phase shifts that depend only on the holonomy of the parameter loop, not on the local rate of traversal.

**Suppression of non-target conditions.**

- Condition (i): The topological gap suppresses $\mathcal{M}$ in the protected subspace. Local environmental perturbations cannot mix the protected manifold with non-protected sectors because doing so requires energy (or substrate-coupling) above the gap. So $\mathcal{M}_\mathrm{floor}$ for the protected sector is held low by the gap structure itself — a *consequence* of topology, not a separate engineering commitment.

- Condition (iii): Most environmental modes do not couple to the topologically protected rule because the rule is encoded in global geometry that local environmental ED-injection cannot reach. $\Lambda_\mathrm{env}$ for the protected subspace is exponentially suppressed in the topological gap. ED-I-14 §9: "topological protection arising from ED-geometry rather than wavefunction structure."

**Binding constraint.** When the topological structure itself fails — gap closure under perturbation, edge-state hybridization with bulk modes, anyonic non-Abelian braiding errors — the protection collapses. $\tau_{(\mathrm{ii})}$ for Class B is set by the *robustness of the global geometry under perturbation*, not by environmental coupling rate. This is structurally distinct from Class A, where binding is set by environmental rates against a robust local engineering.

### 2.3 Class C — high-multiplicity-redundancy

**Protection target:** $\mathcal{U}$ itself, maintained via redundancy of pathways. Condition (i) is **relaxed** by architectural design — high $\mathcal{M}$ is permitted, but the rule's integrity survives because multiple parallel pathways carry the same participation structure.

**Substrate-geometric configuration.** The architecture configures multiple parallel ED-channels that carry the same participation rule. Environmental ED-injection that drives any single pathway toward individuation is absorbed; the rule's integrity is sustained by the surviving channels.

**Mechanism — derived from closed-arc results.**

- **Hafezi multi-timescale photonic lattices (ED-I-18).** A single-ring resonator is a low-multiplicity ED-object with a narrow set of stable pathways and strict frequency-phase matching. A multi-timescale lattice (super-ring + ring) is a high-multiplicity ED-object — a 2D ED-gradient structure with combinatorial pathway expansion. ED-I-18 §5: "in EHF [ED] terms: adding a second timescale increases the system's ED-multiplicity, expanding the number of stable participation pathways. Phase matching becomes a region, not a point. Disorder becomes irrelevant because many pathways remain viable." 100% device yield, two-octave harmonic generation, and disorder-tolerance are the empirical signatures of Class C protection.

- **Multi-axis architectures.** Any system with multiple independent ED-axes (multi-mode cavities, multi-resonator lattices, multi-frequency comb systems, multi-scale mechanical/acoustic, multi-layered quantum materials) realizes Class C structure when the architecture uses the redundancy for protection rather than for additional function. ED-I-18 §9 generalizes: "any system with multiple independent timescales will exhibit relaxed FPM. Any system with increased ED-multiplicity will exhibit broader bandwidth, more harmonics, higher yield, greater disorder tolerance."

- **Bosonic codes (cat states, GKP states).** Information encoded in nontrivial superpositions of high-photon-number Fock states. The encoding is across many physical photon-number states; redundancy of the encoding makes single-photon-loss errors detectable and correctable. Substrate-level reading: the protected logical participation rule is spread across many physical participation pathways.

**Suppression of non-target conditions.**

- Condition (ii): Effective $\Gamma_\mathrm{cross}$ for the protected information is enhanced by the multiple parallel pathways. The probability that *all* parallel pathways simultaneously fall below $\Gamma_\mathrm{min}$ is exponentially suppressed in the redundancy count.

- Condition (iii): The effective $\Lambda$ for the *protected information* is distinct from the $\Lambda$ for any single physical mode. Single-mode loss events are absorbed; the rule's integrity is preserved.

**Binding constraint.** Class C binds when redundancy fails — when correlated errors across multiple parallel pathways exceed the architecture's redundancy budget. This is a different structural failure than Classes A or B: not local-injection-overcoming-isolation (Class A) and not topology-perturbed-by-fluctuation (Class B), but redundancy-count-exceeded-by-correlated-errors.

### 2.4 Three protection targets, three substrate-state quantities

Each class commits structurally to controlling one substrate-state quantity:

| Class | Substrate-state quantity controlled | Mode |
|---|---|---|
| A | $\mathcal{M}$ — local pathway count | Direct: hold $\mathcal{M}_\mathrm{floor}$ low by structural mechanism |
| B | $\sigma$ — substrate-gradient geometry | Direct: hold globally rigid via topological invariants |
| C | Redundancy across parallel pathways | Indirect: provide many copies, accept high local $\mathcal{M}$ |

Note that Class C is *indirect*: it does not fix a single substrate quantity but fixes a *meta-property* (redundancy count). This is a structurally distinct protection mode from A and B's direct fixings.

The three protection modes correspond to three structurally distinct ways of holding $\mathcal{U}$ above threshold given UR-1's three-condition product structure:

- A controls the multiplicity-headroom factor $\prod_i \mu(\mathcal{M}_i/\mathcal{M}_\mathrm{crit})$ directly.
- B controls the connectivity factor $\prod_{(i,j)} \kappa(\gamma_{ij}/\Gamma_\mathrm{min})$ via topology.
- C controls $\mathcal{U}$'s overall robustness by providing redundancy that mitigates single-factor degradation.

### 2.5 Class D candidate audit

Four candidate strategies are evaluated for genuine distinctness from A/B/C.

#### 2.5.1 Dynamical-rotating-binding architectures (e.g., dynamical decoupling)

**Strategy:** Apply periodic control pulses that temporally average out the environmental coupling driving (iii) failure. Net effect: reduce the effective $\int_0^t \Lambda_\mathrm{env}(t')\,dt'$ by introducing cancellations.

**Substrate-level analysis:** The strategy reduces *effective* $\Lambda$ via temporal averaging; it does not introduce a new substrate-state quantity to fix. The pulses themselves are P11 commitment events (controlled $\Lambda_\mathrm{int}$) that target the system's coupling to environment, with structured cancellation patterns that average $\Lambda_\mathrm{env}$ contributions to zero at leading order.

**Verdict:** Not a new class. **Technique** for extending $\tau_{(\mathrm{iii})}$ within Class A protection, by reducing the effective integrated $\Lambda$. The architecture remains Class A; dynamical decoupling is a temporal manipulation that improves Class A's $\tau_{(\mathrm{iii})}$ without changing what substrate quantity is being structurally fixed.

#### 2.5.2 Reservoir-engineered unresolvedness (e.g., Mirrahimi-Devoret cat-state stabilization)

**Strategy:** Engineer the environmental coupling such that the bath actively pushes the system toward a target subspace whenever it leaves. Dissipation becomes a stabilizing mechanism rather than a decoherence channel.

**Substrate-level analysis:** Reservoir engineering tailors $\Lambda_\mathrm{env}$ at the system endpoints to be *structured* rather than random — environmental ED-injection is biased toward the protected subspace. The architectural restoring rate $A_\mathcal{S}$ in the multiplicity-dynamics equation is implemented via environmental coupling rather than internal structural mechanism.

**Verdict:** Not a new class. **Implementation technique** for Class A's architectural restoring term ($A_\mathcal{S}$ in the dynamics of Memo 3 §2.1). Class A's mechanism includes both system-side engineering (low-$\mathcal{M}$ structural commitment) and environment-side engineering (isolation, reservoir engineering, etc.). The substrate-level protection target remains (i); reservoir engineering is a particular environmental-side technique. The substrate state quantity being fixed is still $\mathcal{M}$.

(Subtlety: very aggressive reservoir engineering can blur the line between Class A and Class C if it stabilizes a high-$\mathcal{M}$ logical subspace via redundancy across many physical states. In this regime the strategy is best classified as Class C with active reservoir-mediated restoring. The protection mode is determined by *what is being preserved*, not by *how it is being maintained*.)

#### 2.5.3 Error-correction-as-architecture

**Strategy:** Encode logical information across many physical qubits; periodically measure stabilizers to detect errors; apply correction operations to restore the encoded state.

**Substrate-level analysis:** Error correction operates at *meta-architectural* level. The encoding is Class C (redundancy across physical pathways: a logical qubit lives across many physical qubits). The correction operations are Class A active restoring (the $A_\mathcal{S}$ term, applied to the *logical* multiplicity rather than the physical one). The stabilizer measurements are controlled commitment events that target the syndrome subspace without individuating the logical information.

**Verdict:** Not a new class. **Meta-architecture** that composes Class C (redundancy at the physical level) with Class A active restoring (syndrome-guided correction). The substrate doesn't gain a new protection target; the architecture nests existing protections at a higher logical level.

The hierarchy is real and important: error correction extends $\tau_\mathrm{QC}^\mathrm{logical} \gg \tau_\mathrm{QC}^\mathrm{physical}$ via the composition. But the substrate-level taxonomy is unchanged.

#### 2.5.4 Hybrid / multi-regime systems (e.g., SC-photonic interconnects, topological-SC platforms)

**Strategy:** Use Class A protection in some regions, Class B or C in others, with controlled handoff between them.

**Substrate-level analysis:** Each subsystem is one of Classes A/B/C. The handoff between subsystems is a *substrate-geometric transition* where one class's protection mechanism transitions to another's. The handoff itself is a substrate operation but not a new protection strategy; it is a controlled boundary between regions of different class structure.

**Verdict:** Not a new class. **Composition** of A/B/C across subsystems. The substrate-level taxonomy is preserved; hybrids inherit the binding constraints of their *weakest* subsystem (the binding constraint of the hybrid is the minimum $\tau_\mathrm{QC}$ over the constituent subsystems, plus losses at handoff boundaries).

#### 2.5.5 Quantum Zeno / measurement-based protection

**Strategy:** Frequent projective measurements onto the protected subspace prevent leakage. The measurements add commitments but target the leakage operator, not the protected subspace.

**Substrate-level analysis:** Frequent P11 commitments at the leakage boundary. Effectively this is a structured $\Lambda_\mathrm{int}$ that suppresses transitions out of the protected subspace by repeated re-projection. Substrate-level: this is *active reservoir engineering with measurement instead of dissipation as the mechanism*.

**Verdict:** Not a new class. **Technique** for Class A active restoring, using measurement-driven projection rather than environmental dissipation.

### 2.6 Exhaustiveness verdict

The three classes A/B/C exhaust the substrate-level base protection strategies, by the following structural argument:

1. UR-1 has three conditions (i), (ii), (iii), each set by a substrate quantity ($\mathcal{M}$, $\sigma$/$\gamma_{ij}$, $\Lambda$).
2. Two of these substrate quantities are *fixable structurally* — $\mathcal{M}$ via local structural simplification (Class A), and $\sigma$ via global topological invariants (Class B). $\Lambda$ is not fixable structurally because it is intrinsically a coupling-rate at the boundary between protected region and environment; reducing $\Lambda$ is achieved as a *consequence* of one of the other classes (low-$\mathcal{M}$ system isolated → low coupling, Class A; topological gap → suppressed coupling to most environmental modes, Class B; redundancy → reduced impact of any single coupling event, Class C).
3. The third strategy is *indirect* — instead of fixing a substrate quantity, provide redundancy so $\mathcal{U}$ survives partial failures (Class C).
4. No fourth substrate-level base strategy exists because (a) there are only three substrate quantities to fix in UR-1's structure, (b) only two of them are structurally fixable, (c) the redundancy strategy provides the third option, and (d) all candidate Class D strategies audited are either techniques for extending one of A/B/C's timescales or compositions of A/B/C.

**Verdict: Three classes are exhaustive over substrate-level base protection strategies. OQ-2 closes.**

This does not mean the architectural landscape is three-fold simple. Real systems are typically *meta-architectures* layering multiple classes at different scales (e.g., a fault-tolerant SC quantum computer is Class A at the physical-qubit level, Class C in the logical encoding, with Class A active restoring in the syndrome-guided correction — a three-layer composition). The three-class structure characterizes the substrate-level base from which all real architectures are composed.

### 2.7 Implications for the multiplicity-cap function $M$

The three-class structure constrains $M$'s form. With UR-1's three conditions and three classes corresponding to which condition is each architecture's protection target:

- $M$ has at minimum three architectural-class projections.
- Each projection has its own substrate-determined ceiling for $\tau_\mathrm{QC}$.
- Meta-architectures (error correction, hybrids, dynamical decoupling) appear in $M$ as boundary-condition modifiers — they extend each class's $\tau_\mathrm{QC}$ without introducing a new ceiling structure.

This sharpens OQ-4 toward the conclusion that $M$ is one substrate object with three architectural-class projections + meta-architectural modifiers, rather than three independent functions.

### 2.8 Empirical-anchor placement on the class taxonomy

| Anchor | Class | Binding condition (protection target) |
|---|---|---|
| Matter-wave Q-C boundary 140–250 kDa | Class A (structural simplicity of the molecule itself) | (i) static failure at mass cap |
| SC qubit T₁/T₂ | Class A | (ii) or (iii) environmental |
| JJ MQT | Class A (engineered at (ii) boundary) | (ii) marginal |
| Topological qubit (anyonic) | Class B | (ii) topology-rigidity, with (iii) gap-suppressed |
| Photonic Chern channels | Class B | (ii) edge-state rigidity |
| Hafezi multi-timescale | Class C | (i) relaxed, (ii)/(iii) by redundancy |
| Bosonic cat / GKP codes | Class C | (i) relaxed, redundancy in photon-number |
| Logical qubit (surface code) | Meta: A + C | logical $\tau_\mathrm{QC}^\mathrm{logical}$ via composition |
| Reservoir-engineered cat | Class A (technique-extended) | (i) with active restoring |
| Dynamically-decoupled SC qubit | Class A (technique-extended) | (iii) with reduced effective $\Lambda$ |

All four empirical anchors flagged in Memo 1 (matter-wave, Hafezi, SC-progress, topological) place cleanly on the taxonomy.

### 2.9 Updated invariants / definitions list

| Symbol / concept | Status | Source |
|---|---|---|
| Class A protection mechanism: hold $\mathcal{M}$ low | DERIVED | this memo §2.1, ED-I-01, ED-I-23 |
| Class B protection mechanism: hold $\sigma$-geometry rigid via topology | DERIVED | this memo §2.2, ED-I-14, ED-I-12, ED-I-18 |
| Class C protection mechanism: redundancy across parallel pathways | DERIVED | this memo §2.3, ED-I-18 |
| Three-class exhaustiveness | ESTABLISHED | this memo §2.6 |
| Meta-architecture: composition of A/B/C | DEFINED | this memo §2.5–2.6 |
| Technique-extension of a class's timescale | DEFINED | this memo §2.5 |

### 2.10 Open questions (updated)

- **OQ-1 — CLOSED** (Memo 2)
- **OQ-2 — CLOSED** (this memo §2.6)
- **OQ-3 — CLOSED** (Memo 2)
- **OQ-4 — partially closed.** $M$ has three architectural-class projections + meta-architectural modifiers. Block D will produce the full functional form.
- **OQ-5 — partially advanced.** Matter-wave Q-C boundary is in Class A's $\tau_{(\mathrm{i})}$ projection of $M$. Showing that the QC ceilings on Classes A/B/C, plus the matter-wave boundary, all live on one $M$ function is Block D's deliverable.
- **OQ-6 — CLOSED** (Memo 3)
- **OQ-7 — open.** Specific shape of $\mu$, $\kappa$. Likely INHERITED. Will close (or remain INHERITED) when Block D specifies functional form.

### 2.11 Honest scope

What this memo delivers:

- Class A/B/C mechanisms derived from closed-arc results.
- Four Class D candidates audited and identified as techniques or compositions, not new classes.
- Exhaustiveness argument from UR-1's three-condition structure: three classes are substrate-level base; meta-architectures compose them.
- OQ-2 closed; OQ-4 and OQ-5 advanced.
- Empirical anchors placed on the class taxonomy.

What this memo does NOT deliver:

- The multiplicity-cap function $M$ itself (Block D).
- Closed-form values of class-specific $\tau_\mathrm{QC}$ ceilings.
- Specific shape of $\mu$, $\kappa$ (still INHERITED).

Verdict-class projection consistent with prior memos: form-FORCED on the class taxonomy and exhaustiveness; value-INHERITED on specific ceilings.

---

## 3. Consequences for the Arc

1. **Block C closes.** Three-class structure is exhaustive over substrate-level base strategies.

2. **Meta-architectural distinction is now formal.** Real systems are typically compositions: physical-layer Class A + logical-layer Class C + active restoring at logical level (= the standard fault-tolerant QC stack). The three-class taxonomy describes the *base*; meta-architectures are the *compositions*. This distinction will matter for $M$.

3. **Block D is now sharply specified.** $M$ is one substrate object with three architectural-class projections + meta-architectural boundary-condition modifiers. The function takes:
   - System-level inputs: target $\tau_\mathrm{QC}$, system-multiplicity load, environmental conditions.
   - Architectural inputs: which class (A/B/C), which meta-architectural compositions.
   - Outputs: substrate-determined feasibility region, with form-FORCED structure and value-INHERITED ceiling values.

4. **The matter-wave Q-C boundary at 140–250 kDa is in Class A's $\tau_{(\mathrm{i})}$ projection.** Specifically: the molecule itself is a Class A object (structural simplicity), whose $\mathcal{M}_\mathrm{floor}(M)$ rises monotonically with molecular mass. The boundary is where $\mathcal{M}_\mathrm{floor}(M_\star) = \mathcal{M}_\mathrm{crit}$. Block D must reproduce this as a hard consistency check on $M$'s Class A projection.

5. **No falsifying empirical anchor.** All four primary anchors (matter-wave, Hafezi, SC-progress, topological) plus the secondary anchors (JJ MQT, photonic Chern, bosonic codes, reservoir-engineered cat) fit cleanly on the three-class taxonomy. No platform observed to date has required a fourth class.

6. **Predictive content begins to emerge.** With Block C closed, the arc can begin specifying *what each class predicts* for scaling, ceiling location, and architecture-class-specific failure signatures. But predictive content is downstream of $M$'s functional form — Block D first.

---

## 4. Recommended Next Step

**Memo 5 — Derive the multiplicity-cap function $M$ (Block D opens).**

File: `theory/Quantum_Computing/Arc_QC_5_Multiplicity_Cap_Function.md`.

Scope:

- Construct $M$ as one substrate object with three architectural-class projections.
- For each class, derive the projection's functional form from UR-1 + the class's protection mechanism + the failure-mode rates.
- Show that the three projections jointly form a single substrate function with class-modulated boundary conditions.
- Verify cross-anchor consistency: all four primary empirical anchors must lie on $M$'s appropriate class-projection at consistent substrate-determined locations.
- Explicitly reproduce the matter-wave Q-C boundary at 140–250 kDa from $M$'s Class A $\tau_{(\mathrm{i})}$ projection. Hard consistency check.
- Specify how meta-architectures (error correction, hybrids, dynamical decoupling, reservoir engineering) appear in $M$ as boundary-condition modifiers.
- Honest verdict on form-FORCED / value-INHERITED demarcation across the function.

Closes OQ-4 and OQ-5. Likely closes OQ-7 to the same INHERITED level as $\log g$ in BH-5.

Estimated 2–3 sessions.

If $M$ closes cleanly with all four anchors on one function, Memo 6 is the predictive-content memo: substrate-level predictions for scaling, ceilings, and class-specific signatures, including the falsifiable boundary statements that Arc Q-COMPUTE was opened to deliver. If a structural piece doesn't close, Memo 6 is whatever the math exposes.
