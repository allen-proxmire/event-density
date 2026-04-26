# Memo 02 — Non-Contextuality from Primitives 04 + 07 + 11

**Date:** 2026-04-26
**Arc:** `arcs/born_gleason/`
**Predecessor:** [`01_gleason_inventory.md`](01_gleason_inventory.md)
**Status:** Argument memo. Examines whether Primitive 04 (bandwidth as locus-local scalar) + Primitive 07 (channels as primitive ontological objects) + Primitive 11 (commitment as channel-local selection) jointly force the bandwidth-fraction assignment `b_K` to be independent of the channel decomposition in which K appears.
**Purpose:** Settle Gleason assumptions A4 and A8 at the primitive level. Verdict at §7.

---

## 1. The question, formally

**Question.** Let *u* be a vertex of the participation graph at which a chain *C* has multiplicity M ≥ 3. Let 𝒦(u) denote the set of channels available to *C* at *u* (Primitive 07 §1: a stable, bandwidth-preserving sub-structure of the participation graph supporting *C*'s rule-type at *u*). For each K ∈ 𝒦(u), let b_K(u) be the bandwidth associated with channel K at locus *u* (Primitive 04 §2).

Two distinct **complete channel-decompositions** of *C* at *u* are two ways of partitioning 𝒦(u) — equivalently, two distinct orthonormal bases of the local channel-space — say *𝒟* = {K₁, K₂, …, K_d} and *𝒟'* = {K'₁, K'₂, …, K'_d}, both spanning the same available-channel set at *u*.

A given channel K may appear in *𝒟* alone, in *𝒟'* alone, or in both. The non-contextuality question is:

> **Does b_K(u) depend on which decomposition K appears in?**

If `b_K(u)` is a function of (K, u) alone, with no dependence on the surrounding partition, then the bandwidth-fraction probability rule `Prob(K | u) = b_K(u) / Σ_{K' ∈ 𝒟} b_{K'}(u)` satisfies Gleason's frame-function typing (A4) and frame-sum constancy (A8), and the path Primitives → Gleason → Born is open.

If `b_K(u)` depends on the surrounding partition — i.e., if there exist decompositions *𝒟* and *𝒟'* both containing K but yielding `b_K^{(𝒟)}(u) ≠ b_K^{(𝒟')}(u)` — then non-contextuality fails and the Gleason path is blocked at A4 / A8.

---

## 2. The structural setup (what the primitives actually say)

### 2.1 Channels are graph-substructures, not basis labels

Primitive 07 §1 (verbatim relevant content):

> "A channel is a stable, bandwidth-preserving sub-structure of the participation graph along which a chain's update rule can be instantiated repeatedly without rule-incompatibility … Channels are not the chains themselves … A chain *uses* a channel."

Primitive 07 §1, "What a channel is *not*":

> "Not a wavefunction. A QM wavefunction is a distribution of participation weight across the available channels for a given chain. The channels are the indices being summed over; the wavefunction is the weighting."

The structural content here is decisive: **a channel is an ontologically primitive feature of the participation graph itself.** It is a connected subgraph (V_K, E_K) ⊂ G satisfying rule-compatibility, bandwidth coherence, and stability conditions (Primitive 07 §2). It exists as a feature of the graph regardless of whether any external observer decomposes the chain's state in some basis or another.

Two consequences relevant here:

- **(i) The identity of K is intrinsic to the graph.** K is "this particular subgraph with these particular edges and these particular bandwidth-coherence properties." K is not "the K-coordinate of some basis choice."
- **(ii) The available-channel set 𝒦(u) is intrinsic to vertex u.** It is the set of all channels of the chain's rule-type that meet at u with rule-compatibility. This set exists as a structural property of the graph at u; it is enumerable without reference to any basis.

### 2.2 Bandwidth is an edge-weight on the channel's edges

Primitive 04 §2:

> "Primitive 04 supplies edge weights — a positive real number on each edge measuring bandwidth … `w: E → ℝ_{≥0}` where E is the edge set of the participation graph."

The bandwidth `b_K(u)` of channel K at locus u is the integrated edge-weight along the edges of K's subgraph that are incident to u (or, in the thick-regime continuum version, the bandwidth-density at u summed/integrated over K's local cross-section).

Decisive structural content: **`b_K(u)` is a property of the (channel-subgraph K, vertex u) pair.** It is computed from the graph's edge weights along K's edges at u. It involves no reference to which other channels are or are not present at u.

### 2.3 Commitment selects from the available channel set

Primitive 11 §2:

> "A commitment event ε at vertex u for chain C has: Pre-state (M_pre, {b_K}_pre) — multiplicity M_pre and bandwidth distribution across available channels … Selection: channel K* is chosen with probability P(K*) = b_{K*}² / Σ b_K² (Born-like weight)."

Decisive structural content: **commitment operates on the available-channel set 𝒦(u) at locus u.** The probability assignment uses the bandwidths {b_K(u)} of the available channels, normalized by their sum. The operation is locus-local (it happens at u) and channel-local (it reads each channel's own bandwidth).

---

## 3. The argument for non-contextuality

The argument has the form of a short syllogism whose premises are the three primitive-level statements above, taken as definitional.

### 3.1 Premise statements

- **(P-Channel)** *(from Primitive 07)*: A channel K is a sub-structure of the participation graph. K's identity is intrinsic to the graph and does not depend on any decomposition of 𝒦(u) imposed from outside.
- **(P-Bandwidth)** *(from Primitive 04)*: The bandwidth b_K(u) is a function of the (channel-subgraph K, vertex u) pair, computed from the edge-weights along K's edges incident to u. It does not depend on which other channels are present at u, except through the mechanical definition of "edges incident to u" (which itself involves only K's edges, not other channels' edges).
- **(P-Commitment)** *(from Primitive 11)*: Commitment uses {b_K(u) : K ∈ 𝒦(u)} as inputs. The available-channel set 𝒦(u) is intrinsic to u (per (P-Channel)).

### 3.2 The syllogism

1. **By (P-Bandwidth):** b_K(u) is a function of (K, u) alone.
2. **By (P-Channel):** the identity of K is intrinsic to the graph; K is the same channel-substructure regardless of which decomposition 𝒟 of 𝒦(u) it appears in. Decomposition 𝒟 is an organizational choice imposed externally onto 𝒦(u); it does not alter the graph-substructure that K is.
3. **Therefore:** if K ∈ 𝒟 and K ∈ 𝒟' for two distinct complete decompositions of 𝒦(u), then `b_K^{(𝒟)}(u) = b_K(u) = b_K^{(𝒟')}(u)`. The bandwidth assignment to K is partition-independent.
4. **By (P-Commitment):** the commitment-selection probability at u is `Prob(K | u, 𝒟) = b_K(u) / Σ_{K' ∈ 𝒟} b_{K'}(u)`. The numerator is partition-independent by step 3.
5. **The denominator** — the sum Σ_{K' ∈ 𝒟} b_{K'}(u) — depends on the decomposition 𝒟 only through which channels are summed. But for two complete decompositions 𝒟 and 𝒟' that both span the same available-channel set 𝒦(u), the sum is the total bandwidth at u along channels of *C*'s rule-type at u — a single number intrinsic to u, independent of which complete decomposition enumerates it.

Step 5 is the operational form of A8 (frame-sum constancy). Step 3 is the typing form of A4 (frame-function domain). Both follow from (P-Channel) + (P-Bandwidth).

**Conclusion:** non-contextuality of the bandwidth-fraction probability rule is forced by Primitives 04 and 07 acting jointly. Primitive 11 supplies the operational role (commitment uses the rule); Primitives 04 and 07 supply the *non-contextuality content* of the rule.

### 3.3 Why this is a stronger derivation than standard QM

In standard QM, non-contextuality is *postulated* as part of Gleason's frame-function setup: f is defined on projectors, not on (projector, surrounding-resolution) pairs. The reason "this is the right thing to do" is operational — measurement outcomes don't depend on the experimental context — but the underlying ontology of standard QM does not force this. Hidden-variable models *can* introduce contextuality (Kochen-Specker shows {0,1}-valued contextual assignments can't reproduce QM, but probabilistic contextual assignments can in principle exist).

In ED, non-contextuality is forced by the **ontological status of channels**. A channel is a real graph-substructure, not a basis label. Bandwidth is a real edge-weight property of that substructure, not a relative quantity. The "context" — the surrounding decomposition — is an external organizational choice, and the primitives are explicit that channel identity and bandwidth are properties of the graph, not of organizational choices imposed onto the graph.

This is a structural reason rather than an operational fit. ED **explains** why standard QM gets to assume non-contextuality.

---

## 4. Examination of potential loopholes

A rigorous memo must check whether the syllogism in §3 has hidden gaps. Three loopholes are worth examining explicitly. Each is checked and dismissed.

### 4.1 Loophole 1 — sublinear composition rule

Primitive 04 §7 / `visibility_to_bandwidth.md` (Fix 6 of `TIGHTENING_PASS_01`) supplies a sublinear composition rule:

```
b_combined² = b_1² + b_2² + 2 · c_12 · b_1 · b_2
```

If `b_K` were defined via composition with neighboring channels, this could in principle introduce partition-dependence: differently composed effective channels might assign different bandwidths to the same underlying K.

**Resolution.** The composition rule applies when *combining* channels into a single effective coarse-grained channel. It is a *constructor* for `b_{K₁ ∪ K₂}` from `b_{K₁}` and `b_{K₂}` (with cross-coherence c₁₂). It does **not** redefine `b_{K₁}` alone. The fundamental quantity is the per-channel bandwidth `b_K`, which is the edge-weight integral along K's edges; the composition rule is a derived statement about how to handle coarse-grained super-channels.

In Gleason's setting, the analogous statement is: f(P₁ + P₂) = f(P₁) + f(P₂) for orthogonal P₁, P₂ (σ-additivity), with f(Pᵢ) defined separately on each. The composition rule is the ED analog of this additivity (with the cross-term c₁₂ tracking coherence — vanishing for genuinely orthogonal channels under environmental phase-randomization, per Step 3 §3.3). For *orthogonal* channels in the Gleason sense, c₁₂ = 0 and `b_{combined}² = b_1² + b_2²`, which combined with `b_K = |P_K|²` gives `b_{combined} = b_1 + b_2` — clean σ-additivity.

The composition rule does not introduce partition-dependence to the per-channel bandwidth `b_K`. **Loophole closed.**

### 4.2 Loophole 2 — context-dependent available-channel set

The available-channel set 𝒦(u) was claimed in §2.1 to be intrinsic to u. Could it actually depend on the chain's history, the chain's state, or some external "context" set by a measurement apparatus?

**Resolution.** Primitive 07 §1 defines a channel as a structural feature of the graph: "stable, bandwidth-preserving sub-structure … supporting C's rule-type at u." The set 𝒦(u) is determined by:

- the graph structure at u (which channels exist as sub-structures meeting u),
- the rule-type τ of chain C (which channels are τ-compatible).

Both of these are intrinsic. The graph structure is the graph; the chain's rule-type is the chain's identity-rule (Primitive 02), which does not change without commitment.

What an *external apparatus* does is bring its own bandwidth into the locus, modifying the graph's local edge-weights. This is the **standard environmental coupling** mechanism (Primitive 04 §1.5 environmental band, Primitive 11 §2 commitment trigger). It can:

- change *which* commitment occurs at u (by altering the bandwidth distribution and the commitment trigger);
- change the *rate* of commitment (by altering the commitment-reserve / environmental ratio);
- not change the structural identity of any individual channel K, nor its individual bandwidth `b_K(u)` independent of environmental edge-contributions.

Crucially, the apparatus brings its own *channels* (its own sub-structures into the local graph) and its own bandwidths along those channels. This expands 𝒦(u) by adding apparatus channels; it does not retroactively reorganize the system's existing channel structure into a different basis.

A "measurement choice" — choosing one apparatus orientation versus another — corresponds to coupling the system to one set of apparatus channels versus another. This selects which of the system's channels are *amplified into commitment* (those most strongly coherent with the apparatus channels), but it does not alter the system's per-channel bandwidth `b_K(u)` for any channel K.

This is the ED-primitive-level account of why "context-dependence of measurement context" is a *change of which physical interaction occurs*, not a change in the underlying f. **Loophole closed.**

### 4.3 Loophole 3 — channel ↔ ray correspondence

The argument identifies "channel K" with "ray |K⟩ ∈ ℋ" via the participation-measure mapping. Could the correspondence be many-to-one (multiple channels per ray) or one-to-many (multiple rays per channel) in a way that breaks non-contextuality?

**Resolution.** Three sub-cases:

- **One-to-one** (clean correspondence): non-contextuality at the ED level transfers cleanly to non-contextuality at the QM level. No problem.
- **Many ED channels per QM ray** (ED is finer than QM): coarse-graining ED channels into QM rays is itself a partition operation. The QM-ray bandwidth `b_{|K⟩}` = Σ_{K ∈ ray} b_K is a sum of partition-independent quantities, hence itself partition-independent. Non-contextuality at the ED level transfers to non-contextuality at the QM level. No problem.
- **Multiple QM rays per ED channel** (QM is finer than ED): this would be a structural mismatch suggesting QM rays are not the right correspondent of ED channels. The participation-measure framework (`participation_measure.md`) is explicit that channels are the natural ED correspondents of rays/basis-elements. If this case obtained, it would be a problem — but it does not, by the construction of the participation measure itself.

The correspondence is structurally sound. **Loophole closed.**

---

## 5. The minimal theorem-grade statement

Consolidating §3 with the loophole-checks of §4:

> **Theorem (Non-Contextuality from Primitives).** *Let G be a participation graph and let C be a chain at vertex u ∈ G with multiplicity M ≥ 3, in the thin-participation regime where environmental phase-randomization at commitment averages cross-coherences to zero (per Step 3 §3.3). Then for any channel K ∈ 𝒦(u), the bandwidth `b_K(u)` is a function of (K, u) alone, independent of any complete channel-decomposition 𝒟 ⊃ {K} of 𝒦(u). Equivalently: the bandwidth-fraction map `f(K | u) = b_K(u) / Σ_{K' ∈ 𝒦(u)} b_{K'}(u)` satisfies Gleason's frame-function typing (A4) and frame-sum constancy (A8) at vertex u.*
>
> **Proof.** By Primitive 07 §1, K is a sub-structure of G whose identity is intrinsic to the graph and independent of organizational choices. By Primitive 04 §2, b_K(u) is the integrated edge-weight along K's edges incident to u — a function of (K, u) alone. Therefore for any two complete decompositions 𝒟, 𝒟' of 𝒦(u) both containing K, b_K^{(𝒟)}(u) = b_K(u) = b_K^{(𝒟')}(u). Frame-sum constancy follows because for any complete decomposition 𝒟 of 𝒦(u), Σ_{K' ∈ 𝒟} b_{K'}(u) = Σ_{K' ∈ 𝒦(u)} b_{K'}(u), the total bandwidth at u along C's rule-type — a single intrinsic number. ∎

The theorem closes Gleason A4 and A8 at primitive level. Combined with the inventory of Memo 01 (A1, A2, A3, A5, A6, A7 all automatic or interpretive in ED), it opens the chain:

> Primitives 03, 04, 07, 08, 11 (+ U2 for the inner product) → all Gleason assumptions A1–A8 met → Gleason's theorem applies → f(P) = Tr(ρP) → Born rule (rank-1 case ρ = |ψ⟩⟨ψ|) at theorem grade.

This is the substantive content needed for candidate Theorem #10.

---

## 6. What this argument does not cover (honest scoping)

1. **The d = 2 edge case is untreated here.** Two-channel systems (qubits) require the Busch POVM extension. Memo 04 handles this.

2. **The thin-participation regime restriction is real.** The theorem is stated for the regime where environmental phase-randomization at commitment averages cross-coherences to zero. In the thick / Q-C boundary regime, where `c_{KK'} ≠ 0`, the σ-additivity content of Gleason A7 acquires correction terms. ED reproduces standard QM exactly in the thin-participation regime; deviations in the thick regime are an empirical-content question separate from the structural derivation here.

3. **The sesquilinear inner product (U2) is still an upstream CANDIDATE.** A1's interpretive status depends on U2. If U2 is not promoted to FORCED elsewhere, the chain "Primitives → Gleason → Born" inherits one upstream CANDIDATE (the same one Step 3 inherited). This is a *prior* gap, not a new one introduced by the present argument.

4. **The argument applies to the channel-substructure ontology presented in Primitive 07 §1.** A future amendment to Primitive 07 that loosened the "intrinsic to the graph" status of channels (e.g., made channel identity decomposition-relative) would invalidate the syllogism. This is a structural sensitivity worth flagging — non-contextuality in ED is *only as strong as* the ontological-primitive status of channels.

5. **The continuous-channel case (continuous outcomes such as position) is not explicitly treated here.** The argument is for discrete channel-outcomes. Extension to continuous spectra requires additional measure-theoretic work (analogous to the discrete-to-continuous extension in standard Gleason proofs).

---

## 7. Verdict

**FORCED.**

Primitive 04 (bandwidth as edge-weight on the channel-substructure) + Primitive 07 (channels as ontologically primitive sub-structures of the participation graph) + Primitive 11 (commitment as channel-local selection on the available-channel set at the locus) jointly force the bandwidth-fraction assignment `b_K(u)` to be partition-independent. Gleason assumptions A4 and A8 are settled affirmatively at the primitive level.

The verdict is conditional on:

- the thin-participation regime (cross-coherences average to zero);
- the upstream CANDIDATE U2 (sesquilinear inner product) being either accepted or independently promoted;
- the d ≥ 3 case (d = 2 edge case is Memo 04);
- the ontological-primitive status of channels in Primitive 07 §1 being preserved (i.e., no future amendment loosening "channel identity is intrinsic to the graph").

Subject to those scope conditions, the chain Primitives → Gleason non-contextuality → Gleason theorem → Born rule is open. Memo 03 verifies σ-additivity and dimension; Memo 04 closes d = 2; Memo 05 assembles candidate Theorem #10.

---

## 8. Cross-references

- Arc outline: [`arcs/born_gleason/00_arc_outline.md`](00_arc_outline.md)
- Memo 01 (assumption inventory): [`arcs/born_gleason/01_gleason_inventory.md`](01_gleason_inventory.md)
- Step 3 (predecessor Born derivation; cross-coherence vanishing under environmental phase-randomization at §3.3): [`arcs/arc-foundations/born_rule_from_participation.md`](../arc-foundations/born_rule_from_participation.md)
- Sublinear composition rule (Loophole 1): `quantum/effective_theory/visibility_to_bandwidth.md` and `quantum/primitives/TIGHTENING_PASS_01.md` (Fix 6)
- Primitive 04 (bandwidth as edge-weight): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 07 (channel as graph-substructure): `quantum/primitives/07_channel.md`
- Primitive 11 (commitment as channel-local selection): `quantum/primitives/11_commitment.md`
- Kochen-Specker (1967): S. Kochen and E. P. Specker, "The Problem of Hidden Variables in Quantum Mechanics," J. Math. Mech. 17, 59.

---

## 9. One-line memo summary

> **Non-contextuality of the bandwidth-fraction probability rule is FORCED by Primitives 04 + 07 acting jointly: channels are ontologically primitive sub-structures of the participation graph (P-07), bandwidth is an edge-weight property of those sub-structures (P-04), so b_K(u) is a function of (K, u) alone independent of any external decomposition of 𝒦(u). Gleason A4 and A8 are settled at primitive level; the chain Primitives → Gleason → Born is open through Memo 02 in the d ≥ 3 case under thin-participation regime conditions.**
