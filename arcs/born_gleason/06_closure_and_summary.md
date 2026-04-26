# Memo 06 — Arc Closure and Canonical Summary

**Date:** 2026-04-26
**Arc:** `arcs/born_gleason/`
**Predecessors:** Memos [01](01_gleason_inventory.md), [02](02_noncontextuality_argument.md), [03](03_sigma_additivity_and_dimension.md), [04](04_busch_extension_d2.md), [05](05_synthesis_theorem10.md)
**Status:** Closure memo. Provides the canonical summary of the arc and its public-facing explanation. Integrates Theorem #10 into the QM-emergence program and prepares its memory-record entry.
**Purpose:** Close the born_gleason arc with a single document that serves both internal cross-reference (a canonical entry-point) and external explanation (a self-contained narrative).

---

## 1. Arc summary in one paragraph

The born_gleason arc asked a sharp question: does ED's primitive structure force the non-contextuality assumption that Gleason's theorem requires? Memo 01 inventoried Gleason's eight load-bearing assumptions and mapped each to ED primitives, finding that five are automatic, one is interpretive (conditional on the inherited inner-product CANDIDATE U2), and two are the same load-bearing question stated two ways — non-contextuality. Memo 02 settled that question affirmatively: channels are ontologically primitive sub-structures of the participation graph (Primitive 07), bandwidth is an edge-weight property of those sub-structures (Primitive 04), so the per-channel bandwidth `b_K(u)` is a function of (K, u) alone, partition-independent by construction. Memo 03 verified σ-additivity (automatic from non-negativity, countable channel sets, and bounded total bandwidth) and dimension ≥ 3 (generic for any non-trivial quantum subsystem), deferring the d = 2 edge case. Memo 04 closed d = 2 via Busch's POVM extension, with weighted channel-subsets supplying the effect structure and the spectral construction generating the full Bloch-sphere effect lattice. Memo 05 assembled the four-link chain into Theorem #10: the Born rule for d ≥ 2 in the thin-participation regime is FORCED at theorem grade, conditional only on inherited U2. The arc's net contribution: it eliminates the QM-emergence Step 3 phase-independence CANDIDATE, extends Born coverage to POVM measurements, introduces zero new CANDIDATEs, and identifies U2 as the single residual structural item gating Born, Bell/Tsirelson, and Heisenberg simultaneously.

---

## 2. The arc's structure, narratively

**The question (Memo 00).** The QM-emergence Step 3 derivation had established the Born rule conditional on a single CANDIDATE — the phase-independence of environmental random phases at commitment. That conditionality was the structural-derivation residual. Gleason's 1957 theorem offered an alternative path that requires only one substantive assumption (non-contextuality) plus structural admissibility (σ-additivity, dimension). The arc's question: does ED's primitive structure force Gleason's non-contextuality assumption? If yes, Born promotes from CANDIDATE-with-decoherence-residual to fully FORCED.

**The inventory (Memo 01).** Gleason's apparent "three axioms" presentation hides several structural commitments. Carefully unpacked, the load decomposes into eight assumptions, of which:
- five (non-negativity, normalization, σ-additivity, dimension ≥ 3, projector-lattice structure) are automatic or interpretive in ED;
- one (Hilbert-space arena) is interpretive but inherits the upstream CANDIDATE U2;
- two (frame-function typing and frame-sum constancy) are the same load-bearing question stated two ways — primitive-level non-contextuality.

The inventory's net result: of all the structural work Gleason requires, only one item is genuinely up for grabs in ED. The other seven follow from the primitive stack with no interpretive maneuvering.

**The decisive result (Memo 02).** The non-contextuality argument is short and structural. ED's channels (Primitive 07) are ontologically primitive sub-structures of the participation graph; their identity is intrinsic to the graph, not to any external decomposition. ED's bandwidth (Primitive 04) is an edge-weight integral along the channel's edges at the locus; it depends on the channel and the locus alone. Therefore the per-channel bandwidth `b_K(u)` is partition-independent: for any two complete decompositions of the available-channel set both containing K, the bandwidth assigned to K is the same number. This *is* Gleason's non-contextuality, derived rather than postulated. Three potential loopholes (sublinear composition rule, context-dependent available-channel set, channel ↔ ray correspondence) are checked and dismissed.

The result is structurally stronger than standard QM's treatment: standard QM postulates non-contextuality operationally, while ED *forces* it ontologically. ED **explains** why the Gleason setup gets to assume non-contextuality.

**The admissibility check (Memo 03).** With non-contextuality settled, the remaining structural prerequisites — σ-additivity over countable orthogonal families, and dimension ≥ 3 — fall out by direct verification. σ-additivity follows from non-negativity of bandwidth, at-most-countable channel sets at any locus, finiteness of total chain-bandwidth, and Memo 02's partition-independence — no new structural commitment. Dimension ≥ 3 holds for every non-degenerate physical regime (multi-level atoms, matter-wave interferometers, BECs, continuous spatial channels), with the d = 2 edge case (qubits, polarization, spin-1/2) deferred to Memo 04.

**The d = 2 closure (Memo 04).** Two-channel systems are real, named, and physically central — they cannot be waved away. Busch's 2003 extension of Gleason replaces projectors with POVM effects and proves the same Born-rule conclusion for all d ≥ 2. The ED translation is mechanical: weighted channel-subsets supply the effect structure, with bandwidth × weight giving the effect-value. All four Busch axioms inherit from Memos 02–03 plus weight-linearity. The continuous Bloch-sphere structure that pure projectors cannot supply in d = 2 is generated by varying both the channel-decomposition and the weights — the union over all decompositions generates the full effect lattice on ℂ² by spectral decomposition. Three potential mismatches are audited and resolved.

**The synthesis (Memo 05).** The four-link chain Primitives → non-contextuality (Memo 02) → admissibility (Memo 03) → Busch closure (Memo 04) → Gleason/Busch theorem applied → ρ(u) such that f(E) = Tr(ρE) → Born rule. Theorem #10 is stated cleanly. Its single residual conditionality (U2) is identified, and its supersession of Step 3 is explained.

---

## 3. Theorem #10, stated cleanly

> **Theorem #10 (Born Rule from Primitives, via Gleason–Busch).** Let G be a participation graph and let C be a chain at vertex u in the thin-participation regime. Assume the ED primitive stack (03, 04, 07, 08, 11) and the inherited sesquilinear inner product U2 on the local channel-space ℋ(u). Let 𝒦(u) be the available-channel set with d = dim ℋ(u) ≥ 2. Then there exists a unique density operator ρ(u) on ℋ(u) such that for every effect E on ℋ(u):
>
> ```
> f(S, w | u) = b(S, w | u) / b(𝒦(u) | u) = Tr(ρ(u) · E).
> ```
>
> In particular, for projective measurements:
>
> ```
> Prob(K | u) = b_K(u) / Σ_{K'} b_{K'}(u) = |⟨K|ψ(u)⟩|².
> ```
>
> The Born rule is a structural consequence of the participation-graph ontology and is not an additional postulate.

**Status:** FORCED, conditional only on inherited upstream CANDIDATE U2. Promoting U2 makes Theorem #10 unconditional.

**Scope conditions:**
- Thin-participation regime (cross-coherences average to zero at commitment).
- Discrete-channel case (continuous-spectrum extensions are out-of-scope, flagged for future work).
- Channel-as-primitive ontology of Primitive 07 §1 preserved.

---

## 4. What Theorem #10 supersedes

The QM-emergence Step 3 derivation (`born_rule_from_participation.md`) established the Born rule via a primitive-level decoherence argument: environmental phase-randomization at commitment averages cross-channel coherences to zero, leaving the bandwidth-fraction probability rule on the post-decoherence diagonal mixture. The result was FORCED conditional on one CANDIDATE: the phase-independence of environmental random phases across channels.

**Theorem #10 supersedes Step 3 in three ways:**

1. **Eliminates the phase-independence CANDIDATE.** Memo 02's non-contextuality argument is more fundamental: it derives partition-independence of per-channel bandwidth directly from the channel-as-primitive ontology, without needing environmental decoherence as the mechanism.

2. **Extends to POVM measurements.** Step 3 covered projective measurements (single-channel commitment outcomes) only. Theorem #10 covers all generalized measurements via Busch — partial measurements, joint measurements of incompatible observables, continuous monitoring with finite efficiency.

3. **Anchors the result in established mathematical-physics theorems.** Step 3 was a primitive-level derivation; Theorem #10 is a primitive-level admissibility check followed by quotation of Gleason and Busch. The latter is structurally cleaner and more transferable.

Step 3 is not invalidated — its derivation remains correct as an alternative route to the projective-Born case. Theorem #10 is the structurally superior derivation and should be cited as the canonical Born-rule result going forward.

---

## 5. The single remaining dependency: U2

After Theorem #10, the entire Born-rule derivation chain has exactly one residual structural item: the **sesquilinear inner product on the participation manifold**, designated U2 in the QM-emergence Step-1 program (`participation_measure.md` constraint C3; `qm_emergence_synthesis.md` §4.1).

U2 is not a born_gleason-arc residual. It is inherited from the QM-emergence Step-1 framework, where it appears as a structural commitment whose primitive-level derivation is deferred. The same CANDIDATE gates:

- **Theorem #10 (this arc):** Born rule unconditional ← U2.
- **QM-emergence Step 4:** Bell-CHSH violations + Tsirelson bound unconditional ← U2.
- **QM-emergence Step 5:** Heisenberg uncertainty relations unconditional ← U2.

**Promoting U2 to FORCED in a future arc would simultaneously promote three theorems** — the Born rule, the Bell/Tsirelson result, and the Heisenberg inequality — to fully unconditional status. This is the highest-leverage single derivation target remaining in the QM-emergence program.

The U2 arc would parallel the structure of the present born_gleason arc: ask whether Primitive 04 (bandwidth) + Primitive 09 (polarity / phase) + the four-band orthogonality structure jointly force the sesquilinear inner product C3, or whether C3 remains a genuinely independent commitment. The structural analogy to Memo 02's argument — that a derived constraint follows automatically from primitive-level ontological commitments — suggests the U2 arc has reasonable prospects of closing positive.

---

## 6. Public-facing explainer

*Suitable for general scientific audience; reuses the registers established by the desktop ScienceFriday-style explainer.*

### The hundred-year puzzle

The Born rule says: when you measure a quantum system, the probability of any outcome is the squared magnitude of that outcome's amplitude. *Squared.* Not absolute value, not cubed — squared.

Why? For a hundred years, that exponent has been a postulate. Quantum mechanics asks us to accept it as a brute fact about how the world works.

There is a famous theorem from 1957, Gleason's theorem, that goes part of the way: it says that *if* you accept a few structural conditions about how probabilities can be assigned to quantum measurement outcomes, then the Born rule's squared form is mathematically forced — there is no other consistent choice.

But Gleason's theorem still leans on one substantive assumption: **non-contextuality**. The probability of an outcome can't depend on which other outcomes happen to be in the surrounding measurement context. It can only depend on the outcome itself.

Standard quantum mechanics postulates non-contextuality. It seems true experimentally, and assuming it makes the math work. But nothing about standard quantum mechanics's underlying ontology *forces* non-contextuality. It's an extra ingredient.

### What Event Density adds

Event Density (ED) starts from a different ontology. Instead of treating the quantum state as the primitive object, ED treats the underlying participation graph as primitive — and inside that graph, **channels** (the pathways along which the quantum system's evolution rule can play out) are themselves ontologically primitive sub-structures.

A channel, in ED, is not a basis label that some observer chose to slap onto the state. It is a real structural feature of the graph — a particular subgraph with particular bandwidth-coherence properties — that exists whether anyone is measuring or not.

**Bandwidth** is an edge-weight on the graph. The bandwidth of a channel is an integral of edge-weights along that channel's edges. It is a property of the channel itself, not of any organizational scheme imposed onto it from outside.

Once you accept these two structural facts, non-contextuality follows automatically. The probability of selecting channel K is the bandwidth of K divided by the total bandwidth at the measurement locus. The numerator depends on K alone. The denominator is the total bandwidth at that locus — a single number that doesn't change depending on how someone chooses to enumerate the channels.

There is no room for the probability to depend on the surrounding context. The "context" is an external organizational choice; the bandwidth is intrinsic.

### What this gives us

With non-contextuality forced rather than postulated, Gleason's theorem (and its Busch extension covering qubit-like two-state systems) applies directly to ED. The conclusion is the Born rule — squared amplitudes, the same exponent that has been mysterious for a century — now derived as a structural consequence of the participation-graph ontology rather than postulated as a separate axiom.

The squared exponent is not arbitrary. It is the same squared exponent that defines bandwidth as squared amplitude in the participation-measure construction. Once you have channels as primitive ontological objects with bandwidth as their edge-weight property, the Born rule isn't a new ingredient — it's a consequence of how the framework is built.

### The honest framing

Theorem #10 doesn't predict that quantum mechanics will behave differently in any current laboratory experiment. The Born rule is the Born rule, and ED reproduces it exactly.

What the theorem changes is the *grammar* of the answer to the question "why?" In standard quantum mechanics: "because we postulate it." In ED: "because channels are graph-substructures, bandwidth is their edge-weight, and what you call probability is the bandwidth fraction at the measurement locus — and that fraction is, by structural necessity, partition-independent and squared."

The explanatory burden moves from the Born rule itself to the deeper structural commitment underneath it. That is what physics has always called progress when it has worked: Maxwell explained electricity-and-magnetism as one thing rather than two; Einstein explained space-and-time as one thing; the Standard Model explained the weak-and-electromagnetic forces as one thing. Each move replaced a brute postulate with a structural consequence of a deeper framework. Theorem #10 is the same kind of move applied to one of quantum mechanics's most famous brute postulates.

---

## 7. Integration into the QM-emergence program

**Memory record updates** (recommended; see Recommended Next Steps below):

- `project_qm_emergence_arc.md` — add Theorem #10 to the FORCED-theorem inventory (now 10 theorems). Note Step 3 supersession, POVM extension, U2 conditionality shared with Steps 4 + 5.

**Synthesis paper updates** (recommended):

- `papers/QM_Emergence_Structural_Completion/QM_Emergence_Structural_Completion.md` — update §3.3 (Step 3 — Born Rule) to cite Theorem #10 as the canonical derivation, with §4 (upstream CANDIDATEs) noting that the phase-independence CANDIDATE is eliminated by Theorem #10 and only U2 remains for the Born result.

**Theorem inventory entry:**

> **Theorem #10 — Born Rule (Gleason–Busch path).** FORCED for d ≥ 2 in the thin-participation regime, via the chain Primitives 03+04+07+08+11 → non-contextuality (Memo 02) → σ-additivity + dimension (Memo 03) → Busch d = 2 closure (Memo 04) → Gleason/Busch → ρ(u) such that f(E) = Tr(ρ E). Conditional only on inherited upstream CANDIDATE U2 (sesquilinear inner product). Subsumes and strengthens QM-emergence Step 3.

---

## 8. Verdict

The born_gleason arc is **closed**.

**Theorem #10 established, conditional on U2.**

The Born rule, in the thin-participation regime, for any dimension d ≥ 2, is no longer a postulate of quantum mechanics. It is a structural consequence of the ED primitive stack — derivable, citable, and compositional with the rest of the QM-emergence program. The single residual conditionality (U2) is shared with two other major program results and represents the natural next high-leverage target.

The arc produced six memos, no new CANDIDATEs, one new theorem, and one cleaned-up replacement for a previous CANDIDATE-residual derivation. By the standards of structural-foundations work, this is a clean closure.

---

## 9. Recommended Next Steps

**(a) Update the project memory record `project_qm_emergence_arc.md`.** Add the Theorem #10 entry; update the FORCED-theorem count from 9 → 10; flag U2 as the high-leverage single residual gating Born + Bell/Tsirelson + Heisenberg simultaneously. This is the immediate cross-session integration step — without it, future sessions will not know to cite Theorem #10 or to treat U2 as a high-leverage target.

**(b) Update the QM-emergence synthesis paper `QM_Emergence_Structural_Completion.md`.** §3.3 (Step 3 — Born Rule) and §4 (upstream CANDIDATEs) need light updates to cite Theorem #10 as the canonical Born derivation and to note the elimination of the phase-independence CANDIDATE. The synthesis paper is the cross-program reference document; updating it propagates the result.

**(c) Open the U2 arc as the next foundational structural target.** With Theorem #10 in hand, U2 is now demonstrably the single highest-leverage open derivation in the QM-emergence program: one arc, three downstream theorems unconditionalized. The U2 arc would parallel born_gleason in structure (does Primitive 04 + Primitive 09 + four-band orthogonality force the sesquilinear inner product C3?). Worth opening soon while the structural-derivation reasoning patterns from this arc are still warm.

---

## 10. Cross-references

**Within the arc:**
- [`00_arc_outline.md`](00_arc_outline.md) — initial scoping
- [`01_gleason_inventory.md`](01_gleason_inventory.md) — Gleason assumption inventory
- [`02_noncontextuality_argument.md`](02_noncontextuality_argument.md) — load-bearing non-contextuality result
- [`03_sigma_additivity_and_dimension.md`](03_sigma_additivity_and_dimension.md) — admissibility (A7, A2)
- [`04_busch_extension_d2.md`](04_busch_extension_d2.md) — d = 2 closure via Busch
- [`05_synthesis_theorem10.md`](05_synthesis_theorem10.md) — Theorem #10 synthesis

**Predecessors and cross-arc references:**
- [`arcs/arc-foundations/born_rule_from_participation.md`](../arc-foundations/born_rule_from_participation.md) — QM-emergence Step 3 (superseded by Theorem #10)
- [`arcs/arc-foundations/participation_measure.md`](../arc-foundations/participation_measure.md) — QM-emergence Step 1, source of upstream CANDIDATE U2
- [`papers/QM_Emergence_Structural_Completion/QM_Emergence_Structural_Completion.md`](../../papers/QM_Emergence_Structural_Completion/QM_Emergence_Structural_Completion.md) — program synthesis paper

**Primitives:**
- Primitive 03 — `quantum/primitives/03_participation.md`
- Primitive 04 — `quantum/primitives/04_participation_bandwidth.md`
- Primitive 07 — `quantum/primitives/07_channel.md`
- Primitive 08 — `quantum/primitives/08_multiplicity.md`
- Primitive 09 — `quantum/primitives/09_tension_polarity.md`
- Primitive 11 — `quantum/primitives/11_commitment.md`

**External literature:**
- Gleason 1957: A. M. Gleason, "Measures on the closed subspaces of a Hilbert space," J. Math. Mech. 6, 885.
- Busch 2003: P. Busch, "Quantum states and generalized observables: a simple proof of Gleason's theorem," Phys. Rev. Lett. 91, 120403.
- Caves-Fuchs-Manne-Renes 2004: C. M. Caves, C. A. Fuchs, K. K. Manne, J. M. Renes, "Gleason-Type Derivations of the Quantum Probability Rule for Generalized Measurements," Found. Phys. 34, 193.

**Public-facing companion:**
- `C:\Users\allen\Desktop\ED_Exponent2_Explainer.md` — ScienceFriday-style explainer covering the broader Exponent-2 thread (Born + Schrödinger + Heisenberg). Theorem #10 sharpens the Born portion of that explainer; a follow-up explainer dedicated to Theorem #10 alone is a candidate output (see Memo 05 §8(b)).

---

## 11. One-line memo summary

> **Born_gleason arc closed. Theorem #10 (Born Rule from Primitives, via Gleason–Busch) is FORCED for d ≥ 2 in the thin-participation regime, conditional only on inherited upstream CANDIDATE U2. The arc supersedes QM-emergence Step 3, eliminates its phase-independence CANDIDATE, extends Born to POVM measurements, introduces zero new CANDIDATEs, and identifies U2 as the highest-leverage single residual structural item in the QM-emergence program (gates Born + Bell/Tsirelson + Heisenberg simultaneously). Six memos, one new theorem, one cleaned-up supersession; clean structural-foundations closure.**
