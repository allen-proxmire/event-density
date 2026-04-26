# Memo 01 — U2 Decomposition and Primitive Mapping

**Date:** 2026-04-26
**Arc:** `arcs/U2/`
**Predecessor:** [`00_arc_outline.md`](00_arc_outline.md)
**Status:** Structural inventory memo. Decomposes the upstream CANDIDATE U2 (sesquilinear inner product on the participation-measure complex span) into three sub-commitments (C3a, C3b, C3c), maps each to the relevant ED primitives, and classifies each by structural status (automatic / interpretive / load-bearing). Analogous in scope and intent to born_gleason Memo 01.
**Purpose:** Pin down the conceptual terrain so Memo 02 can target C3a + C3b directly and Memo 03 can focus entirely on the load-bearing C3c question.

---

## 1. The full sesquilinear-inner-product commitment

From `arcs/arc-foundations/participation_measure.md` line 240:

> "Complex-valued `P_K(x)` with sesquilinear inner product `⟨P | Q⟩ = Σ_K ∫ dx P_K*(x) Q_K(x)` provides this naturally — Hilbert-space structure emerges from the participation measure's defining properties."

This single sentence packages three structurally distinct commitments. Treating them as a single block obscures which parts are derivable from primitives and which are genuine independent choices. The decomposition:

- **C3a — Linearity.** The space of participation measures admits a complex-vector-space structure: sums P + Q and scalar multiples α·P (α ∈ ℂ) are themselves participation measures.
- **C3b — Conjugate-bilinearity (sesquilinearity).** There exists a pairing ⟨·|·⟩ : 𝒫 × 𝒫 → ℂ that is conjugate-linear in the first argument, linear in the second, and yields ⟨P | P⟩ ≥ 0 (so that the participation measure has a Hilbert-space norm).
- **C3c — Specific form.** ⟨P | Q⟩ = Σ_K ∫ dx P_K*(x) Q_K(x) — the channel-summed, position-integrated, complex-conjugate-product form, with counting measure on channels and Lebesgue (or graph-vertex) measure on positions.

Each downstream theorem (Born / Bell / Heisenberg) leans on a different combination of these. A clean U2-FORCED verdict requires deriving all three from the primitive stack. A partial verdict could close C3a + C3b but leave C3c as a residual.

---

## 2. C3a — Linearity

### 2.1 Precise statement

The set of participation measures 𝒫 = {P : 𝒦 × M → ℂ} (where 𝒦 is the channel index set and M the position manifold or vertex set) admits the operations:

```
(P + Q)_K(x) := P_K(x) + Q_K(x)              (componentwise complex addition)
(α · P)_K(x) := α · P_K(x), α ∈ ℂ              (scalar multiplication by complex number)
```

with these operations satisfying the standard complex-vector-space axioms (associativity, commutativity, additive identity, additive inverses, scalar-distributivity, scalar-associativity).

### 2.2 Primitive correspondents

The participation measure (Step 1 eq. †) is constructed as:

```
P_K(x, t) = √b_K(x, t) · e^{i π(K, x, t)}                                      (1)
```

— a complex number per (channel, position, time) tuple, fusing:

- **Primitive 04 (bandwidth):** supplies the real non-negative magnitude √b_K via b_K ≥ 0.
- **Primitive 09 (polarity / phase):** supplies the U(1)-valued phase factor e^{iπ_K} — verified above (Primitive 09 §1.16: "Polarity is not a binary in general — it is a phase in the full treatment").

Each (K, x) slot of P is therefore a complex number. The collection {P_K(x)} is a complex-valued array indexed by (K, x). Componentwise addition and scalar multiplication of such arrays yield well-defined arrays of the same type — i.e., the structure 𝒫 is closed under these operations.

### 2.3 What's needed for C3a

Two structural requirements:

- **(L1) Each P-slot is complex-valued.** Inherited from Primitive 04 + Primitive 09 via construction (1). **Status: automatic.**
- **(L2) The space 𝒫 is closed under componentwise sum and complex-scalar multiplication.** Closure of complex-valued functions under componentwise operations is a property of the codomain (ℂ), not an additional primitive commitment. **Status: automatic.**

### 2.4 Loophole locations

- **(L-loop-1) "Sums of participation measures may not themselves be participation measures."** Could there be a structural constraint — e.g., a normalization condition — that excludes generic sums P + Q from 𝒫? In principle yes: if every "participation measure" must satisfy `Σ_K ∫ |P_K|² = 1`, then arbitrary sums fail this. In practice, this is the difference between "the *space* of participation measures" (the linear span, on which the inner product lives) and "*physical states*" (the unit-norm rays in that space). The Hilbert-space construction needs the full linear span; physical states are the unit subset. **Resolution: standard Hilbert-space construction handles this; the linear structure is on the span, the physical interpretation is on the unit-norm subset.** No genuine loophole.

- **(L-loop-2) "Complex scalar multiplication may violate Primitive 04's bandwidth non-negativity."** If P → α·P with α ∈ ℂ and |α| ≠ 1, then b_K = |P_K|² → |α|² · b_K, which scales bandwidth. Is this allowed by Primitive 04? Primitive 04 §2 specifies bandwidth as edge-weight, with absolute scale set by the chain's persistence-regime budget. Scaling the participation measure by a complex constant rescales bandwidth proportionally — this is a *normalization* operation, not a primitive-violating operation. **Resolution: scalar multiplication is a re-normalization; the unit-norm convention picks the physical state.** No genuine loophole.

C3a is structurally automatic. The complex-vector-space structure is built into the participation-measure construction.

### 2.5 Status

**C3a — AUTOMATIC** (construction (1) yields complex values; complex-valued function spaces are closed under componentwise sum and complex-scalar multiplication).

---

## 3. C3b — Conjugate-bilinearity (sesquilinearity)

### 3.1 Precise statement

There exists a map ⟨·|·⟩ : 𝒫 × 𝒫 → ℂ satisfying:

- **(S1) Conjugate-linearity in first argument:** ⟨α P + β Q | R⟩ = α* ⟨P | R⟩ + β* ⟨Q | R⟩.
- **(S2) Linearity in second argument:** ⟨R | α P + β Q⟩ = α ⟨R | P⟩ + β ⟨R | Q⟩.
- **(S3) Conjugate symmetry:** ⟨P | Q⟩* = ⟨Q | P⟩.
- **(S4) Positive-definiteness:** ⟨P | P⟩ ≥ 0, with equality iff P = 0.

(S3) is implied by (S1) + (S2) for sesquilinear forms; (S4) is what makes ⟨P | P⟩ a norm-squared.

### 3.2 Primitive correspondents

Three primitive-level facts force this structure:

- **(P4-norm) Bandwidth is a non-negative real:** Primitive 04 §2 gives `w : E → ℝ_{≥0}`. Combined with construction (1), `b_K(x) = |P_K(x)|²` ≥ 0. Therefore the *expected pairing on a single (K, x) slot* must satisfy ⟨P_K(x) | P_K(x)⟩ = b_K(x) ≥ 0 — which forces the diagonal pairing to be `P_K*(x) · P_K(x)`, the squared modulus. Any other diagonal form (e.g., `P_K(x) · P_K(x)`) would not yield a non-negative real for arbitrary complex P_K.

- **(P9-U(1)) Polarity is U(1)-valued:** Primitive 09 §1.16 establishes polarity as a phase, and §1.30 ("Not a scalar") confirms its U(1)-valued character. The participation measure's phase factor e^{iπ_K} is U(1)-valued. This means physical content is invariant under global phase rotation P → e^{iα} P. The pairing ⟨P | Q⟩ must be invariant under this rotation when P = Q (else ⟨P | P⟩ would change with α — but bandwidth is α-invariant). Sesquilinearity is the unique form satisfying ⟨e^{iα}P | e^{iα}P⟩ = e^{-iα}e^{iα}⟨P | P⟩ = ⟨P | P⟩. A real-bilinear pairing fails this.

- **(P4-additivity) Bandwidth additivity over orthogonal channel-subsets:** Primitive 04 §2 (four-band conservation) and the disjoint-sum decomposition of bandwidth (Memo 03 of born_gleason §2) require `b(S₁ ⊔ S₂) = b(S₁) + b(S₂)` for disjoint channel-subsets. For this to be implementable via an inner-product structure ⟨P | P⟩, the inner product must be linear in *one* slot (so that orthogonal-projector restriction sums correctly across the partition). Combined with (P4-norm)'s diagonal positivity, the pairing is forced to be sesquilinear (linear in one slot, conjugate-linear in the other).

Together, (P4-norm) + (P9-U(1)) + (P4-additivity) force the pairing to satisfy (S1)–(S4). This is structurally analogous to the standard derivation of sesquilinear inner products on complex Hilbert spaces from positivity + complex-symmetry + linearity — but here the inputs are primitive-level structural commitments rather than abstract axioms.

### 3.3 What's needed for C3b

- **(B1) Existence of a pairing whose diagonal yields bandwidth.** Forced by Primitive 04 (bandwidth as a non-negative real associated with each P) + the participation-measure construction (1). **Status: forced.**
- **(B2) Sesquilinearity as the unique form respecting U(1) polarity invariance.** Forced by Primitive 09 (U(1) phase) + the requirement that bandwidth be α-invariant under global phase rotation. **Status: forced.**
- **(B3) Positive-definiteness.** Forced by Primitive 04's non-negativity of bandwidth. **Status: forced.**

### 3.4 Loophole locations

- **(F1 — non-sesquilinear bilinear pairing).** Could a real-bilinear pairing on the participation-measure space (treating ℂ as ℝ²) be consistent with the primitives? A real-bilinear pairing would give ⟨e^{iα}P | e^{iα}P⟩ = e^{2iα} ⟨P | P⟩ (or similar non-trivial dependence on α), violating U(1) invariance of bandwidth. **Resolution: blocked by Primitive 09's U(1) polarity.** No genuine loophole, but the verification is non-trivial — Memo 02 should walk through it explicitly.

- **(F4 — non-U(1) phase symmetry).** Could Primitive 09 admit a wider symmetry group than U(1) — e.g., SU(2)-valued polarity? If yes, the inner-product structure would generalize to a quaternionic or non-commutative setting, and the standard sesquilinear form would not be uniquely forced. Primitive 09's first-pass canonical statement (line 11) commits to "phase relation … two limiting cases" with full continuum between, and §1.30 ("Not a scalar") clarifies polarity is phase-valued, not multidimensional. The structural commitment is U(1). **Resolution: U(1) is the explicit choice in Primitive 09; SU(2) or higher polarity would be a primitive-level amendment, not a current ambiguity.** No genuine loophole at the current primitive stack.

- **(F1′ — alternative diagonal forms).** Could the diagonal pairing be defined as `b_K = f(P_K)` for some function f other than `|P_K|²`? Construction (1) explicitly defines `b_K = |P_K|²` (the square of the magnitude); any other diagonal form would conflict with the participation-measure construction. **Resolution: blocked by Step 1 construction (1).** No genuine loophole.

C3b is structurally forced by the joint action of Primitives 04 + 09 + the participation-measure construction. The derivation is not entirely automatic (it requires the explicit U(1)-invariance argument), but the structural inputs are all in hand.

### 3.5 Status

**C3b — FORCED, conditional on a careful derivation in Memo 02.** The primitive inputs are all in place; the load on Memo 02 is to make the derivation rigorous, not to find new structural inputs.

---

## 4. C3c — Specific form ⟨P | Q⟩ = Σ_K ∫ dx P_K*(x) Q_K(x)

### 4.1 Precise statement

Given that a sesquilinear inner product exists (C3a + C3b), the *specific* form is:

```
⟨P | Q⟩ = Σ_K ∫_M dx P_K*(x) Q_K(x)                                            (2)
```

— with three distinguishing features:

- **(c1) Channel measure: counting measure (Σ_K).** The inner product sums over channels with equal weight (counting measure on the channel index set 𝒦).
- **(c2) Position measure: Lebesgue / graph-vertex measure (∫ dx).** The inner product integrates over positions with the natural manifold volume form (or graph-vertex counting measure in the discrete case).
- **(c3) Pointwise pairing: complex-conjugate product (P_K*(x) Q_K(x)).** At each (channel, position) slot, the contribution is the complex-conjugate product of the slot values.

### 4.2 Primitive correspondents

Each sub-feature has its own structural support — and its own potential loophole.

#### 4.2.1 (c1) Channel measure

- **Primitive 07 §1:** "Countable. In any given region, the number of available channels of a given rule-type is finite (usually small)."
- **Primitive 07 ontological status:** channels are primitive sub-structures of the participation graph (born_gleason Memo 02 §2).

The natural measure on a finite or countable set of *primitive ontological objects* is counting measure: each primitive entity contributes equally by virtue of its primitive status. Weighted measures on the channel set would correspond to assigning unequal "structural weight" to different channels — but channels are primitively defined, with no structural feature distinguishing one from another in the channel-set sense (they differ in their *bandwidth*, not in their *measure-theoretic weight*).

**Status: plausibly forced by Primitive 07's primitive-channel-set ontology, but the explicit derivation is not in hand.** This is a load-bearing item for Memo 03.

#### 4.2.2 (c2) Position measure

- **Discrete-graph version:** the participation graph's vertex set V supplies a natural discrete measure (counting measure on vertices). Sums over V are the discrete analog of ∫ dx.
- **Thick-regime continuum version:** the emergent manifold (Primitive 12 thickening) supplies a volume form via the metric structure inherited from bandwidth gradients (Primitive 06 ED-gradient + Primitive 03 §5.2 distance ↔ inverse adjacency-bandwidth).

In the discrete case, counting measure is structurally natural. In the continuum case, the metric volume form is structurally natural. The transition from one to the other is the discrete-to-continuum lift of the participation-graph structure.

**Status: plausibly forced by the participation-graph vertex set (discrete) and the emergent-manifold volume form (continuum), but the lift's uniqueness is not fully verified.** This is a secondary load-bearing item for Memo 03.

#### 4.2.3 (c3) Complex-conjugate pointwise pairing

The pointwise pairing P_K*(x) Q_K(x) is the local analog of the sesquilinear inner product on ℂ (the trivial one-dimensional Hilbert space). Given C3b's sesquilinearity globally, the local pairing must be the unique conjugate-bilinear pairing on each ℂ-slot — which is, up to overall scaling, exactly P_K*(x) Q_K(x).

**Status: forced by C3b + the locality of the pairing (no cross-slot mixing in the basic inner-product definition).** The cross-slot question is itself a potential structural item — could the inner product include cross-slot terms like P_K(x) Q_{K'}(x') for K ≠ K' or x ≠ x'? In standard quantum mechanics no; in ED, the four-band orthogonality structure (Primitive 04 §1.5) plausibly forbids cross-channel terms in the basic inner product, with cross-channel coherence emerging only in the *coherent sum* Ψ = Σ P_K, not in ⟨P | Q⟩ itself.

**Status: forced conditional on the locality assumption, which itself follows from the four-band orthogonality. Memo 03 should verify.**

### 4.3 What's needed for C3c

To force the specific form (2), three sub-derivations:

- **(C3c-i) Channel measure is counting measure.** Forced by Primitive 07's primitive-channel ontology + the absence of structural distinctions among channels in the measure sense.
- **(C3c-ii) Position measure is the participation-graph vertex measure (discrete) / emergent-manifold volume form (continuum).** Forced by the participation-graph structure + the thick-regime emergent-manifold construction.
- **(C3c-iii) Pointwise pairing is complex-conjugate product, with no cross-slot terms.** Forced by C3b's sesquilinearity + the four-band orthogonality of Primitive 04 §1.5.

If all three close affirmatively, C3c is FORCED. If any closes with a genuine alternative, C3c is CONDITIONAL on the contested item.

### 4.4 Loophole locations

The arc outline §6 identified four sub-falsifiers (F1–F4). Three of them attach to C3c:

- **(F2 — alternative channel measure).** Could Primitive 07 admit a weighted measure on the channel set, where some channels carry more "structural weight" than others independent of their bandwidth? This would correspond to a participation-graph-level distinction between channels that is not captured by bandwidth or rule-type. **Resolution candidate:** Primitive 07's primitive-channel ontology forbids such distinctions — channels differ in their bandwidth and rule-type, not in any prior weighting. But the explicit derivation is needed in Memo 03.

- **(F3 — alternative position measure).** Could the participation graph admit non-counting (discrete) or non-Lebesgue (continuum) position measures consistent with the primitives? In the discrete case, vertex sets carry counting measure naturally — but a non-counting measure could in principle be defined if some vertices were "structurally weightier" than others. In the continuum case, the volume form is determined by the emergent metric — but alternative metrics (e.g., conformal rescalings) could in principle give alternative measures. **Resolution candidate:** the four-band structure pins down a unique metric structure and unique vertex measure (no structural distinction among graph vertices beyond what bandwidth records). Verification is the work of Memo 03.

- **(F1′ — non-local cross-slot terms).** Could the basic inner product include cross-slot mixing terms (P_K Q_{K'} for K ≠ K' or x ≠ x')? The four-band orthogonality of Primitive 04 §1.5 plausibly forbids this — orthogonal bands cannot contribute to each other's inner-product entries. **Resolution candidate:** four-band orthogonality forces the local-only structure of the basic inner product. Verification needed in Memo 03.

### 4.5 Status

**C3c — LOAD-BEARING.** The primitive inputs plausibly support each of (c1), (c2), (c3), but explicit derivations are needed for each, and the loopholes F2, F3, F1′ require explicit dismissal. This is the substantive work of Memo 03.

---

## 5. Joint structural status

| Sub-commitment | Description | Primitive correspondents | Status |
|---|---|---|---|
| **C3a** | Linearity of 𝒫 (complex-vector-space structure) | 04 (complex magnitude via √b) + 09 (U(1) phase) + closure of ℂ-valued functions | **AUTOMATIC** |
| **C3b** | Conjugate-bilinearity (sesquilinearity) | 04 (bandwidth = |P|², non-negative) + 09 (U(1) polarity invariance) + 04 §1.5 (band additivity) | **FORCED** (Memo 02 to derive rigorously) |
| **C3c-(i)** | Channel measure = counting | 07 (channels as primitive ontological objects, no inter-channel weighting) | **LOAD-BEARING** (Memo 03) |
| **C3c-(ii)** | Position measure = vertex-counting / Lebesgue | Participation-graph vertex set + Primitive 12 thickening (emergent manifold volume form) | **LOAD-BEARING** (Memo 03) |
| **C3c-(iii)** | Local complex-conjugate pointwise pairing (no cross-slot terms) | C3b + Primitive 04 §1.5 (four-band orthogonality) | **LOAD-BEARING** (Memo 03) |

**Summary:** of the three top-level sub-commitments, C3a is automatic, C3b is forced (Memo 02 will execute the derivation cleanly given primitive inputs already in hand), and C3c carries the substantive load via its three sub-features. Memo 03 will examine each of (c1), (c2), (c3) against the corresponding loopholes (F2, F3, F1′) and either close the arc positive (FORCED) or identify the precise residual (CONDITIONAL).

---

## 6. What this leaves for Memos 02 and 03

**Memo 02 scope:** rigorously derive C3a + C3b from the primitive inputs identified in §2.2 and §3.2. Anticipated outcome: clean closure. The work is verification, not discovery. Predicted memo length: shorter than this one — the structural inputs are simple and the derivation pattern is standard.

**Memo 03 scope:** examine each of (c1), (c2), (c3) against the loopholes (F2, F3, F1′). For each sub-feature, either:
- Show it is uniquely forced by the primitives, dismissing the corresponding loophole; or
- Identify the specific structural alternative that the primitives admit, downgrading to CONDITIONAL with a precise residual.

This is the load-bearing memo for the arc. It is structurally analogous to Memo 02 of born_gleason — the single substantive derivation that determines the verdict.

**Memo 04 scope:** synthesis + downstream theorem-status update.

---

## 7. Comparative observation

The U2 arc's structural shape mirrors the born_gleason arc:

| Parameter | born_gleason | U2 (current) |
|---|---|---|
| Top-level CANDIDATE | Born rule (with phase-independence residual) | U2 (sesquilinear inner product) |
| Decomposition into sub-claims | 8 Gleason assumptions | 3 sub-commitments (C3a, C3b, C3c) |
| Automatic / interpretive items | 5 of 8 | 1 of 3 (C3a) |
| Inherited-CANDIDATE items | 1 of 8 (Hilbert-space arena, dependent on U2 itself) | 0 of 3 |
| Load-bearing items | 2 of 8 (A4, A8 = same question) | 1 of 3 (C3c with three sub-features) |
| Single substantive memo carrying the load | Memo 02 | Memo 03 |
| Anticipated verdict | FORCED (which closed the arc) | FORCED (working hypothesis) |

The structural analogy is encouraging but not decisive — the load on C3c (channel measure + position measure + local-pointwise structure) is *broader* than the single non-contextuality question in born_gleason, even though both are formally one item. Memo 03 may accordingly be longer than born_gleason's Memo 02.

---

## 8. Recommended Next Steps

**(a) Begin Memo 02 (C3a + C3b derivation).** This is the natural next session step. Both sub-commitments have all their primitive inputs in hand; Memo 02 is verification work, not discovery work. Expected outcome: clean closure with explicit derivations of (i) complex-vector-space closure of 𝒫 from construction (1), and (ii) sesquilinearity from Primitive 04 non-negativity + Primitive 09 U(1) invariance + Primitive 04 §1.5 band additivity. Should be a shorter memo than this one.

**(b) Read `u3_evolution_derivation.md`, `u4_hamiltonian_form_derivation.md`, `u5_adjacency_partition_derivation.md` before drafting Memo 02.** These sibling derivations of other upstream CANDIDATEs establish the program's standard for what counts as a successful primitive-level derivation. A 15-minute calibration read before drafting Memo 02 will save time and ensure Memo 02's standards align with the existing program. (This is a re-statement of arc-outline §8(b); flagged here because Memo 02 is the natural moment to act on it.)

**(c) Pre-flag C3c-(ii)'s discrete-to-continuum lift as the most likely sticking point.** Of the three sub-features of C3c, (i) [counting measure on primitive channels] is structurally cleanest and (iii) [local complex-conjugate pairing] follows from C3b + four-band orthogonality. The discrete-to-continuum lift in (ii) involves the Primitive 12 thickening machinery, which has its own arc-level structural commitments (acoustic metric, kinematic curvature, etc.). Memo 03 will likely need to either (a) restrict the U2-FORCED claim to the discrete regime where (ii) is clean, or (b) bring in additional structural inputs from Primitive 12 / Phase-3 work to lift to the continuum. Worth flagging now so Memo 03's scope can be set deliberately.

---

## 9. Cross-references

- Arc outline: [`arcs/U2/00_arc_outline.md`](00_arc_outline.md)
- Step 1 participation-measure framework (constraint C3 source): [`arcs/arc-foundations/participation_measure.md`](../arc-foundations/participation_measure.md)
- Born_gleason Memo 01 (parallel inventory template): [`arcs/born_gleason/01_gleason_inventory.md`](../born_gleason/01_gleason_inventory.md)
- Born_gleason Memo 02 (parallel non-contextuality argument template): [`arcs/born_gleason/02_noncontextuality_argument.md`](../born_gleason/02_noncontextuality_argument.md)
- Sibling upstream-CANDIDATE derivations: [`arcs/arc-foundations/u3_evolution_derivation.md`](../arc-foundations/u3_evolution_derivation.md), [`arcs/arc-foundations/u4_hamiltonian_form_derivation.md`](../arc-foundations/u4_hamiltonian_form_derivation.md), [`arcs/arc-foundations/u5_adjacency_partition_derivation.md`](../arc-foundations/u5_adjacency_partition_derivation.md)
- Primitive 04 (bandwidth + four-band orthogonality): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 07 (channel countability + primitive ontology): `quantum/primitives/07_channel.md`
- Primitive 09 (polarity / U(1) phase): `quantum/primitives/09_tension_polarity.md`
- Primitive 12 (thickening / emergent manifold): `quantum/primitives/12_thickening.md`

---

## 10. One-line memo summary

> **U2 decomposes into C3a (linearity, AUTOMATIC), C3b (conjugate-bilinearity, FORCED via Primitive 04 non-negativity + Primitive 09 U(1) invariance + Primitive 04 §1.5 band additivity), and C3c (specific Σ_K ∫ form, LOAD-BEARING with three sub-features: (i) channel counting measure forced by Primitive 07's primitive ontology, (ii) position measure forced by participation-graph + emergent-manifold volume form (continuum lift potentially sticking point), (iii) local complex-conjugate pairing forced by C3b + four-band orthogonality). Memo 02 closes C3a + C3b cleanly; Memo 03 carries the load on C3c against falsifiers F2, F3, F1′. Structural shape parallels born_gleason but with broader load on the single substantive memo.**
