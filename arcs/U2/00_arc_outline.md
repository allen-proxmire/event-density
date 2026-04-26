# U2 Arc — Examination Outline

**Date opened:** 2026-04-26
**Location:** `arcs/U2/`
**Goal:** Determine whether the sesquilinear inner product on the participation-measure complex span (constraint C3 of QM-emergence Step 1, designated upstream CANDIDATE U2) is FORCED by ED's primitive structure, CONDITIONAL on a genuine independent commitment, or NOT FORCED.
**Predecessor work:** `arcs/arc-foundations/participation_measure.md` (Step 1, where C3 is adopted as constraint); `arcs/born_gleason/05_synthesis_theorem10.md` (where U2 is the single residual conditionality on Theorem #10).
**High-leverage status:** U2 is the single shared residual conditionality on three downstream theorems — Born rule (Theorem #10), Bell/Tsirelson (Step 4), Heisenberg (Step 5). Resolving it unblocks all three simultaneously.

---

## 1. The precise formulation of U2

### 1.1 As stated in the participation-measure framework

From `arcs/arc-foundations/participation_measure.md` line 240:

> "Complex-valued `P_K(x)` with sesquilinear inner product `⟨P | Q⟩ = Σ_K ∫ dx P_K*(x) Q_K(x)` provides this naturally — Hilbert-space structure emerges from the participation measure's defining properties."

From the same file's constraint list (line 299):

> **C3. Sesquilinear inner product.** Enables Hilbert-space structure, orthogonal partitions, uncertainty inequalities.

### 1.2 The structural commitment, decomposed

C3 is the conjunction of three sub-commitments, only some of which may be primitive-derivable:

- **(C3a) Linearity.** The space of participation measures admits a linear structure — sums P + Q and scalar multiples α·P make sense as participation measures.
- **(C3b) Conjugate-bilinearity (sesquilinearity).** There exists a map ⟨·|·⟩ : P × P → ℂ that is conjugate-linear in the first argument and linear in the second.
- **(C3c) Specific form.** ⟨P | Q⟩ = Σ_K ∫ dx P_K*(x) Q_K(x) — the channel-summed, position-integrated, complex-conjugate-product form.

A clean U2-FORCED result would derive **all three** from primitives. A partial result might force C3a + C3b but leave the specific form C3c as a CANDIDATE.

### 1.3 What U2 enables downstream

Three downstream items depend on U2:

- **Theorem #10 (Born rule, Gleason–Busch path).** U2 supplies Gleason's A1 (Hilbert-space arena). Without U2, Gleason / Busch has no ambient Hilbert space to apply.
- **QM-emergence Step 4 (Bell / Tsirelson).** Tsirelson's bound 2√2 derives from operator-norm / Cauchy-Schwarz inequalities on the Hilbert space ℋ_A ⊗ ℋ_B. The sesquilinear inner product is what makes "operator norm" and "Cauchy-Schwarz" meaningful here.
- **QM-emergence Step 5 (Heisenberg).** The Fourier-uncertainty theorem applies to L² Fourier pairs; the L² norm is a consequence of the sesquilinear inner product (specifically, ⟨Ψ | Ψ⟩ = ∫|Ψ|²).

Each downstream item uses a different *aspect* of the inner product:
- Theorem #10 uses the lattice-of-projectors structure derived from inner-product orthogonality.
- Step 4 uses Cauchy-Schwarz and operator-norm bounds derived from the inner product.
- Step 5 uses the L² norm as a special case of ⟨P | P⟩.

A robust U2-FORCED result needs to underwrite all three uses.

---

## 2. The structural prospects

### 2.1 The working intuition (to be tested)

The participation-measure construction `P_K(x, t) = √b_K(x, t) · e^{iπ_K(x, t)}` (Step 1 eq. †) is **already complex-valued** by virtue of fusing Primitive 04 (bandwidth, real non-negative) with Primitive 09 (polarity phase, U(1)-valued angle). This means linearity (C3a) of the participation-measure space inherits from complex-vector-space structure on each channel slot — it is not a separate commitment.

Conjugate-bilinearity (C3b) is the natural pairing on any complex-valued field-like object: `⟨P | Q⟩ = ∫ P* Q` is the unique-up-to-normalization sesquilinear pairing on ℂ-valued functions. It is forced by linearity + the requirement that ⟨P | P⟩ be a non-negative real (norm-like) — which is forced by the requirement that bandwidth `b = |P|²` be a non-negative real, which is itself forced by Primitive 04.

The specific form (C3c) is where the load actually sits. The channel-sum + position-integral structure could in principle be replaced by other measure choices (weighted sums over channels, integrals against alternative position measures), and the question is whether the four-band structure of Primitive 04 plus the channel ontology of Primitive 07 force the specific form ⟨P | Q⟩ = Σ_K ∫ P_K* Q_K.

**Working hypothesis:** U2 is FORCED, in a manner structurally analogous to the born_gleason arc's non-contextuality result. The complex-valued participation measure is built from primitive-level commitments (bandwidth + polarity), and the sesquilinear pairing is the unique natural pairing on the resulting structure that respects (a) bandwidth as squared norm, (b) channel orthogonality as inner-product orthogonality, (c) four-band decomposition as inner-product-orthogonal direct sum.

The arc's job is to make this rigorous or find the loophole.

### 2.2 Where the loophole could live

Three places to scrutinize:

- **The channel-sum measure.** Why Σ_K and not ∫ dμ(K) with some non-trivial measure on the channel set? Primitive 07's countable-channel statement and the discrete-channel setting Memo 02–04 of the born_gleason arc operated in suggest counting measure is forced — but the explicit derivation should be checked.
- **The position-integral measure.** Why ∫ dx with Lebesgue measure (or its participation-graph analog) and not some weighted measure? In the discrete-graph setting this is sum-over-vertices; in the thick-regime continuum setting it inherits from the emergent manifold's volume form. The lift from discrete to continuum is where alternative measures could in principle creep in.
- **The complex-conjugate structure.** Why P* (complex conjugate) and not some other involution? This is forced by U(1) invariance of polarity (Primitive 09): the inner product must be invariant under global phase rotation P → e^{iα}P, which uniquely picks out P*Q over P P or other bilinear forms.

If any of these three turns out to admit genuine alternatives consistent with the primitives, U2 is CONDITIONAL. If all three are forced, U2 is FORCED.

---

## 3. What the verdicts would mean

### 3.1 FORCED

The sesquilinear inner product is uniquely determined by the primitives — Primitive 04 (bandwidth as squared norm), Primitive 07 (channels as primitive set, supplying counting measure), Primitive 09 (polarity as U(1)-valued, forcing complex-conjugate involution), and the four-band orthogonality from Primitive 04 §1.5.

Consequence: Theorem #10 promotes from "FORCED conditional on U2" to FORCED unconditional. Steps 4 and 5 of the QM-emergence program promote analogously. Three structural items of the program lift from CANDIDATE-conditional to FORCED-unconditional in a single arc. The QM-emergence theorem inventory grows by zero (no new theorems) but its conditional surface area shrinks substantially.

### 3.2 CONDITIONAL

U2 reduces to a smaller residual CANDIDATE — one of the three sub-components C3a, C3b, C3c, or to a specific structural commitment (e.g., the Lebesgue position measure) that is not derivable from current primitives but is also not pathological.

Consequence: the Born / Bell / Heisenberg results remain conditional, but the conditionality is sharpened. This is a partial-progress outcome and an honest one — it identifies precisely which structural item would need to be elevated to a primitive (or derived from a future primitive amendment) to close the chain.

### 3.3 NOT FORCED

The primitives admit consistent alternative inner-product structures (for example, a non-sesquilinear bilinear pairing, or a sesquilinear pairing with a non-Lebesgue position measure, or a non-channel-summed measure) that produce a different downstream phenomenology than standard QM.

Consequence: U2 is a genuine independent structural commitment. The QM-emergence program inherits an ineliminable CANDIDATE that would need either an amendment to the primitive stack or an independent justification (e.g., empirical fit) to close. This would be the program's first explicit acknowledgment that QM is not fully primitive-derivable from the current primitive set — a substantive structural finding.

NOT FORCED is an admissible outcome and would not invalidate prior work; it would clarify the structural status of the QM-emergence program.

---

## 4. Memo structure (4 memos)

### Memo 1: `01_u2_decomposition_and_targets.md`
Decompose U2 into C3a (linearity), C3b (conjugate-bilinearity), C3c (specific form). For each sub-commitment, identify which primitive(s) would underwrite it. Inventory parallels born_gleason Memo 01: the goal is to map the structural terrain so subsequent memos can target specific load-bearing items rather than re-arguing the whole structure each time. Status: pure structural inventory; no derivation yet.

### Memo 2: `02_linearity_and_sesquilinearity.md`
The first derivation memo. Argue rigorously that C3a (linearity of the participation-measure space) follows from the complex-valued construction of P (Primitive 04 amplitude + Primitive 09 phase), and that C3b (conjugate-bilinearity of the natural pairing) follows from C3a + the requirement that bandwidth `b = |P|²` be a non-negative real (Primitive 04 non-negativity) + U(1) invariance under global phase rotation (Primitive 09). Predicted outcome: C3a + C3b are FORCED jointly; the load lies entirely on C3c.

### Memo 3: `03_specific_form_and_measures.md`
The load-bearing memo for the arc. Examine whether the specific form ⟨P | Q⟩ = Σ_K ∫ dx P_K* Q_K is uniquely forced, or whether genuine alternative inner-products are consistent with the primitives. Three sub-questions:
- (a) Is the channel-sum measure forced (by Primitive 07's channel countability)?
- (b) Is the position-integral measure forced (by the participation-graph vertex-set / emergent manifold volume form)?
- (c) Is the complex-conjugate involution forced (by Primitive 09's U(1) polarity invariance)?

If all three close affirmatively, C3c is FORCED and the arc closes positive. If any closes negatively, the arc closes CONDITIONAL with a precise residual identified.

### Memo 4: `04_synthesis_and_verdict.md`
Assemble Memos 02–03 into a single verdict on U2. State the structural conclusion (FORCED / CONDITIONAL / NOT FORCED). Update the downstream-theorem status table: Theorem #10, Step 4 (Bell/Tsirelson), Step 5 (Heisenberg) move accordingly. Cross-reference into the QM-emergence synthesis paper. Define follow-up arcs if any.

---

## 5. First-session scope

Memos 01 and 02. Memo 01 establishes the decomposition; Memo 02 closes C3a + C3b which are anticipated to be straightforward. The substantive load lands in Memo 03, which is a distinct session-length effort.

**Predicted outcome for Memos 01–02 (to be tested, not assumed):** C3a (linearity) and C3b (conjugate-bilinearity) close cleanly. The participation measure is built complex-valued from primitives, and the natural pairing on a complex-valued space with a non-negative-norm requirement and U(1) phase invariance is uniquely sesquilinear up to the choice of measure. The genuinely contested question is C3c (the specific Σ_K ∫ dx form), addressed in Memo 03.

---

## 6. Falsification conditions

The arc is **closed FORCED** if Memos 02–03 collectively establish that all of C3a, C3b, C3c follow uniquely from the primitive stack.

The arc is **closed CONDITIONAL** if Memo 02 closes C3a + C3b but Memo 03 reveals that C3c admits genuine non-trivial alternatives consistent with the primitives — i.e., if one or more of (channel-sum measure, position-integral measure, complex-conjugate involution) is not uniquely forced, but the alternatives are non-pathological.

The arc is **closed NOT FORCED** if any of C3a, C3b, C3c admits a *consistent and physically distinct* alternative — meaning a different inner-product choice that satisfies the primitives but produces a different downstream phenomenology than standard QM. This would be the strongest negative result: U2 would be revealed as a genuine independent structural commitment, not derivable from the current primitive stack.

**Specific sub-falsifiers to watch for:**

- **(F1) Non-sesquilinear bilinear pairing.** If a real-bilinear (rather than complex-conjugate-bilinear) pairing on the participation-measure space is consistent with all primitives and produces well-defined orthogonality and norm structures, then C3b is not forced.
- **(F2) Alternative channel measure.** If Primitive 07 admits a non-counting measure on the channel set (e.g., a weighting that depends on rule-type or environmental coupling), then C3c's Σ_K is not forced.
- **(F3) Alternative position measure.** If the participation-graph vertex measure / emergent manifold volume form admits non-Lebesgue alternatives consistent with the four-band structure, then C3c's ∫ dx is not forced.
- **(F4) Non-U(1) phase symmetry.** If Primitive 09's polarity admits a wider symmetry group than U(1) (e.g., a SU(2) or SO(3)-valued polarity), then C3c's complex-conjugate involution would generalize and the specific sesquilinear form would not be forced.

Each sub-falsifier corresponds to a structural feature of the primitive stack that the arc must verify. The expectation, based on current primitive statements, is that none of F1–F4 obtains — but the verification is the work of Memos 02–03.

---

## 7. Cross-references

- Born rule arc (downstream beneficiary): `arcs/born_gleason/05_synthesis_theorem10.md`, `arcs/born_gleason/06_closure_and_summary.md`
- Step 1 participation-measure framework: `arcs/arc-foundations/participation_measure.md` (constraint C3 at line 299; sesquilinear-inner-product comment at line 240)
- Step 4 (Bell / Tsirelson, downstream beneficiary): `arcs/arc-foundations/bell_correlations_from_participation.md`
- Step 5 (Heisenberg, downstream beneficiary): `arcs/arc-foundations/uncertainty_from_participation.md`
- QM-emergence synthesis (upstream CANDIDATE inventory; U2 as part of the §4.1 minimal set): `papers/QM_Emergence_Structural_Completion/QM_Emergence_Structural_Completion.md`
- Primitive 04 (bandwidth as non-negative real, four-band structure): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 07 (channel countability): `quantum/primitives/07_channel.md`
- Primitive 09 (polarity / U(1) phase): `quantum/primitives/09_tension_polarity.md`
- Other completed upstream-CANDIDATE derivations (parallel structural template): `arcs/arc-foundations/u3_evolution_derivation.md`, `arcs/arc-foundations/u4_hamiltonian_form_derivation.md`, `arcs/arc-foundations/u5_adjacency_partition_derivation.md`

---

## 8. Recommended Next Steps

**(a) Begin Memo 01 (U2 decomposition).** This is the natural next session step. The decomposition into C3a + C3b + C3c is the structural prerequisite for everything downstream; doing it cleanly up front lets Memos 02–03 target specific load-bearing items rather than re-arguing the whole structure each time. Memo 01 is structurally analogous to born_gleason Memo 01 and should be of similar size.

**(b) Audit `u3_evolution_derivation.md`, `u4_hamiltonian_form_derivation.md`, `u5_adjacency_partition_derivation.md` before drafting Memo 02.** These three sibling memos have already attempted derivations of the other upstream CANDIDATEs (U3, U4, U5) from primitives. Their structural template — what counted as a successful derivation, what was conceded as residual — is directly relevant to U2 and will save time / sharpen standards in Memo 02. A short pre-Memo-02 read of each will set the calibration.

**(c) Hold off on updating downstream theorem-status tables until Memo 04 verdict.** Theorem #10's status as "FORCED conditional on U2" is the current canonical statement; updating it speculatively before the U2 verdict is known would create memory churn. The single exception: if the user wants the project memory record `project_qm_emergence_arc.md` updated with Theorem #10 as a new entry (separate from this arc), that should be done before Memo 01 begins so the memory baseline is current at the start of the U2 work.

---

## 9. One-line arc summary

> **Test whether the sesquilinear inner product on the participation-measure complex span (C3 of Step 1, designated U2) is FORCED by primitives — specifically, whether linearity (C3a), conjugate-bilinearity (C3b), and the specific form ⟨P | Q⟩ = Σ_K ∫ dx P_K* Q_K (C3c) follow uniquely from Primitives 04 + 07 + 09 + the four-band structure. If yes, three downstream theorems (Born #10, Bell/Tsirelson, Heisenberg) promote from CONDITIONAL to FORCED simultaneously. If no, U2 is identified as a genuine independent structural commitment with consequences for the QM-emergence program's primitive-derivability claim.**
