# Memo 01 — Gleason's Assumptions: Inventory and ED Primitive Map

**Date:** 2026-04-26
**Arc:** `arcs/born_gleason/`
**Predecessor:** `arcs/born_gleason/00_arc_outline.md`
**Status:** Structural alignment memo. Inventories the load-bearing assumptions of Gleason's theorem and maps each to the ED primitive(s) that would have to underwrite it. **Does not argue for non-contextuality** — that is Memo 02.
**Purpose:** Pin down the conceptual terrain so Memo 02 can focus entirely on the single load-bearing question (does ED force non-contextuality?).

---

## 1. Gleason's theorem — canonical statement

**Theorem (Gleason, 1957).** Let ℋ be a separable Hilbert space over ℝ, ℂ, or ℍ with dim ℋ ≥ 3. Let *f* be a frame function on ℋ — that is, a map *f* : 𝒫(ℋ) → [0, 1] from the lattice of closed subspaces (equivalently, orthogonal projectors) to the unit interval — satisfying:

1. **Non-negativity:** f(P) ≥ 0 for every projector P.
2. **Normalization:** f(I) = 1.
3. **σ-additivity:** for any countable family {Pᵢ} of mutually orthogonal projectors, f(Σ Pᵢ) = Σ f(Pᵢ).

(The non-contextuality content is that *f* is defined on projectors P alone, not on ordered tuples (P, P', P'', …). The value f(P) does not depend on which orthogonal resolution P appears in. This is built into the *type signature* of *f*.)

**Then:** there exists a unique density operator ρ on ℋ such that f(P) = Tr(ρP) for every P. The Born rule is the special case ρ = |ψ⟩⟨ψ|.

The dimensional restriction d ≥ 3 is essential. The d = 2 case admits non-Born frame functions (Gleason fails for qubits in this form; the gap is closed by Busch's POVM extension, addressed in Memo 04).

---

## 2. The load-bearing assumptions, individually

For the inventory, the standard "three axioms" presentation (non-negativity, normalization, σ-additivity) hides several structural commitments that are normally taken for granted but matter explicitly when checking against ED. The full list:

### A1. Hilbert-space arena
A separable Hilbert space ℋ over ℝ, ℂ, or ℍ exists. Inner product is sesquilinear; closed subspaces form an orthomodular lattice 𝒫(ℋ).

### A2. Dimensional restriction
dim ℋ ≥ 3.

### A3. Projector lattice structure
The closed subspaces of ℋ form a complete orthomodular lattice. Orthogonal complements, joins, and meets are well-defined. Every projector P has a well-defined orthogonal complement P⊥.

### A4. Frame function domain
*f* is a function on projectors (equivalently, on closed subspaces; equivalently, on rays for the rank-1 case). Its domain is the projector lattice itself, **not** the set of ordered orthogonal resolutions. *This is where non-contextuality enters Gleason's theorem — as a typing constraint on f, not as a separate axiom.*

### A5. Non-negativity
f(P) ≥ 0 for every P.

### A6. Normalization
f(I) = 1.

### A7. σ-additivity over orthogonal families
For any countable {Pᵢ} with PᵢPⱼ = 0 (i ≠ j), f(Σ Pᵢ) = Σ f(Pᵢ).

### A8. Frame-sum constancy (derived consequence, but worth naming)
For any orthonormal basis {|eᵢ⟩}, Σᵢ f(|eᵢ⟩⟨eᵢ|) = f(I) = 1. The sum is the same number for *every* ONB. This is the substantive content of A4 + A6 + A7 combined: the value f assigns to a rank-1 projector |e⟩⟨e| does not depend on which complete ONB completes it. This is the non-contextuality statement in operational form.

---

## 3. Mapping each assumption to ED primitives

For each Gleason assumption, the corresponding ED structural element (or the ED structural element that would need to underwrite it).

### A1 — Hilbert-space arena

**ED correspondent:** the participation-measure space.

- The complex amplitude `P_K = √b_K · e^{iπ_K}` (Primitive 04 amplitude/bandwidth + Primitive 09 polarity phase) supplies the C-valued amplitude structure.
- The sesquilinear inner product on the participation manifold appears as constraint C3 in the QM-emergence Step-1 memo (`participation_measure.md`), itself adopted as upstream CANDIDATE U2.
- The lattice structure of "closed subspaces" corresponds to the lattice of channel-subsets — see A3.

**Underwriting primitives:** Primitive 04 (bandwidth → amplitude magnitude), Primitive 07 (channels → indices), Primitive 09 (polarity → phase).

### A2 — Dimensional restriction d ≥ 3

**ED correspondent:** generic ED chains have multiplicity M ≥ 3 because Primitive 07 (channel) supplies countably many available channels at any non-trivial chain locus, and Primitive 08 (multiplicity) measures how many are actively populated.

- Multi-channel coherent superposition is the generic case; single-channel (M = 1) is a post-commitment limit.
- Two-channel (M = 2) systems are special — they are the qubit edge case requiring separate treatment (Memo 04).

**Underwriting primitives:** Primitive 07 (channel countability), Primitive 08 (multiplicity ≥ 3 for generic chains).

### A3 — Projector lattice structure

**ED correspondent:** the partition lattice of channel-subsets at a commitment locus.

- A "projector" P in standard QM corresponds in ED to a *subset of channels selected by some commitment criterion* — equivalently, a partition class of the chain's available channels at vertex u.
- Orthogonality of projectors corresponds to disjointness of channel-subsets (no shared channels — this is structural disjointness at the participation-graph level, Primitive 03).
- Join (P ∨ Q) corresponds to channel-subset union; meet (P ∧ Q) to intersection; complement P⊥ to the complementary channel-subset within the available-channel set at that locus.
- Orthomodularity follows from the disjoint-union structure of channel-subsets.

**Underwriting primitives:** Primitive 03 (participation relation defines what "shared" vs "disjoint" means), Primitive 07 (channels are the lattice atoms), Primitive 11 (commitment locus determines which channel-set is in play).

### A4 — Frame function domain (the non-contextuality-typing constraint)

**ED correspondent:** the bandwidth-fraction map.

- ED's natural probability assignment is `Prob(K*) = b_{K*} / Σ b_K`. The numerator depends only on the bandwidth in channel K*. The denominator depends only on the total bandwidth at the commitment locus.
- *Whether this map is genuinely a function on K* alone — independent of which other channels happen to be in the resolution — is the precise question Memo 02 must answer.*
- The strong claim ED needs is: bandwidth `b_K` is a property of channel K and the commitment locus, not of the surrounding channel-partition. Primitives 04 and 07, taken at face value, suggest this — but the explicit derivation is the work of Memo 02.

**Underwriting primitives:** Primitive 04 (bandwidth as channel-local quantity), Primitive 07 (channel as primitive object), Primitive 11 (commitment selects on the channel-local quantity).

### A5 — Non-negativity

**ED correspondent:** bandwidth is a non-negative scalar.

- Primitive 04 §2 explicitly states `w: E → ℝ_{≥0}` (edge weights are non-negative reals); thick-regime bandwidth density `b(x, y) : M × M → ℝ_{≥0}` inherits this.
- Squared amplitude `|P_K|² = b_K ≥ 0` is automatic.

**Underwriting primitives:** Primitive 04 (bandwidth domain).

### A6 — Normalization

**ED correspondent:** total bandwidth at the commitment locus normalizes to 1 by construction of the probability rule.

- The normalization `Prob = b_K / Σ b_K` enforces Σ_K Prob(K) = 1 trivially.
- At a deeper level, the bandwidth-conservation constraint along an isolated chain (Primitive 04 §2 four-band sum) provides the structural normalization that the probability rule inherits.

**Underwriting primitives:** Primitive 04 (bandwidth conservation / total-budget structure), Primitive 11 (commitment locus selects which budget normalizes).

### A7 — σ-additivity over orthogonal families

**ED correspondent:** bandwidth additivity over disjoint channel-subsets.

- Bandwidths in disjoint channel-subsets sum: if `S₁, S₂` are disjoint subsets of available channels, then `Σ_{K ∈ S₁ ∪ S₂} b_K = Σ_{K ∈ S₁} b_K + Σ_{K ∈ S₂} b_K`. This is set-theoretic additivity of a non-negative function over disjoint subsets — automatic.
- Countable extension follows if the available-channel set is countable, which Primitive 07 §1 affirms ("Countable. In any given region, the number of available channels of a given rule-type is finite (usually small)").
- *The non-trivial content is whether `b_K` itself is well-defined independently of the partition into which K is embedded — that question is A4 / non-contextuality, addressed in Memo 02.*

**Underwriting primitives:** Primitive 04 (additivity of bandwidth across disjoint channel-subsets), Primitive 07 (countable channel set).

### A8 — Frame-sum constancy (the operational non-contextuality statement)

**ED correspondent:** total bandwidth at the commitment locus does not depend on which channel-decomposition is used to enumerate it.

- For ED to satisfy Gleason's frame-sum constancy: Σ_K b_K must equal the same total for every complete channel-decomposition of the chain at the commitment locus.
- This is the substantive non-contextuality content. Memo 02 addresses it directly.

**Underwriting primitives:** Primitive 04 (bandwidth as locus-property, not partition-dependent), Primitive 07 (channels as primitive, not basis-dependent).

---

## 4. Status classification of each mapping

Three categories:

- **Automatic** — the primitive structure straightforwardly supplies the assumption with no interpretive maneuvering.
- **Interpretive** — the primitive structure supplies a corresponding object, but the identification with the Gleason assumption requires a structural reading that is plausible and standard within the ED program but not literally definitional.
- **Nontrivial** — the assumption corresponds to an open structural question or one that requires a dedicated derivation argument (i.e., requires its own memo to settle).

| Gleason assumption | ED primitive(s) | Status |
|---|---|---|
| **A1** Hilbert-space arena | 04 (amplitude) + 07 (channels) + 09 (phase) + sesquilinear inner product (upstream CANDIDATE U2) | **Interpretive** — participation-measure structure supplies it; the sesquilinear inner product is itself a separate CANDIDATE (U2) |
| **A2** dim ≥ 3 | 07 (channel countability) + 08 (multiplicity) | **Automatic** for generic ED chains; d = 2 edge case requires Memo 04 |
| **A3** Projector lattice | 03 (participation) + 07 (channels) + 11 (commitment locus) | **Interpretive** — channel-subset lattice maps to projector lattice via partition structure; orthomodularity follows from disjoint-union structure |
| **A4** Frame function domain (non-contextuality typing) | 04 (bandwidth as channel-local) + 07 (channel as primitive) + 11 (commitment) | **Nontrivial** — load-bearing question for Memo 02 |
| **A5** Non-negativity | 04 (bandwidth domain ℝ_{≥0}) | **Automatic** |
| **A6** Normalization | 04 (bandwidth conservation) + 11 (commitment locus) | **Automatic** by construction of the bandwidth-fraction probability rule |
| **A7** σ-additivity | 04 (additivity over disjoint channel-subsets) + 07 (countable channel set) | **Automatic** for finite/countable channel sets, *conditional on A4 being settled* |
| **A8** Frame-sum constancy | 04 (locus-property) + 07 (primitive channels) | **Nontrivial** — operational form of A4; load-bearing for Memo 02 |

---

## 5. What this leaves for Memo 02

**Five of the eight assumptions (A2, A3, A5, A6, A7) are automatic or interpretive in ED** — they fall out of Primitives 04, 07, 08, 11 with no additional structural commitment beyond what the primitives already supply.

**One assumption (A1) is interpretive but inherits a known upstream CANDIDATE** — the sesquilinear inner product C3 is U2 in the QM-emergence program. This is not a Born-arc problem; it is a separate structural item that, if promoted to FORCED elsewhere, lifts A1 to FORCED automatically.

**Two assumptions (A4, A8) are the load-bearing nontrivial items**, and they are the *same* structural question stated two ways:

- **A4 (typing form):** is the bandwidth-fraction probability rule a function of channel K alone, independent of which surrounding channels populate the resolution?
- **A8 (operational form):** does Σ_K b_K equal the same total for every complete channel-decomposition of the chain at the commitment locus?

These are equivalent statements of **non-contextuality at the ED-primitive level**. Memo 02 addresses them directly.

If Memo 02 closes A4 / A8 affirmatively from the primitive structure, then the chain is:

> Primitives 03 + 04 + 07 + 08 + 11 (+ U2 for the inner product)
>   → all of Gleason's assumptions A1–A8 are met
>   → Gleason's theorem applies
>   → f(P) = Tr(ρP) for some ρ
>   → Born rule (rank-1 case ρ = |ψ⟩⟨ψ|) is FORCED at theorem grade.

If Memo 02 fails to close A4 / A8, the failure mode is informative: it identifies precisely which primitive would need amendment (most likely either Primitive 04's locus-locality of bandwidth, or Primitive 07's primitive-status of channels) to recover non-contextuality.

---

## 6. Cross-references

- Arc outline: [`arcs/born_gleason/00_arc_outline.md`](00_arc_outline.md)
- Step 3 (predecessor Born derivation): [`arcs/arc-foundations/born_rule_from_participation.md`](../arc-foundations/born_rule_from_participation.md)
- QM-emergence synthesis (upstream CANDIDATE inventory; U2 = sesquilinear inner product): [`papers/QM_Emergence_Structural_Completion/QM_Emergence_Structural_Completion.md`](../../papers/QM_Emergence_Structural_Completion/QM_Emergence_Structural_Completion.md)
- Primitive 03 (participation): `quantum/primitives/03_participation.md`
- Primitive 04 (bandwidth): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 07 (channel): `quantum/primitives/07_channel.md`
- Primitive 08 (multiplicity): `quantum/primitives/08_multiplicity.md`
- Primitive 09 (polarity / phase): `quantum/primitives/09_tension_polarity.md`
- Primitive 11 (commitment): `quantum/primitives/11_commitment.md`
- Gleason 1957: A. M. Gleason, "Measures on the closed subspaces of a Hilbert space," J. Math. Mech. 6, 885.
- Busch 2003 (POVM extension covering d=2): P. Busch, "Quantum states and generalized observables: a simple proof of Gleason's theorem," Phys. Rev. Lett. 91, 120403.

---

## 7. One-line memo summary

> **Of Gleason's eight load-bearing assumptions (A1–A8), five are automatic or interpretive in ED via Primitives 03, 04, 07, 08, 11; one (A1) is interpretive but depends on the upstream sesquilinear-inner-product CANDIDATE U2; and two (A4, A8) are equivalent statements of primitive-level non-contextuality and form the entire load-bearing question for Memo 02.**
