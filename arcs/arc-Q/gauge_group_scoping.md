# Gauge-Group Scoping

**Stage Q.2 — Arc Q Sub-Memo**
**Status:** Scoping + partial-derivation memo. Headline verdict: **U(1) FORCED at primitive level (already at R.1); SU(N) for any finite N CANDIDATE-admissible structurally with multi-generator extension τ_g^a; specific SU(3) × SU(2) × U(1) Standard-Model group EMPIRICALLY INHERITED — not derivable from primitives. Refinement R-2 (gauge-quotient individuation) discharged via adjacency-equivalence-class construction. Refinement R-4 (non-Abelian extension) admissible but requires R.1 minimal-coupling argument to be repeated with internal-index enrichment; partial closure here, full closure in Q.3.**

---

## 1. Goal

Stage Q.1 closed GRH as CANDIDATE-STRONG with five outstanding refinements (R-1 through R-5). Stage Q.2 addresses two of those — **R-2 (gauge-quotient individuation)** and **R-4 (non-Abelian extension)** — by evaluating the admissibility of specific gauge-group structures within ED.

The driving question is:

(Q-Gauge) Given GRH (the gauge connection A_μ is the participation measure of a rule-type τ_g), what gauge-group structures are FORCED, CANDIDATE-admissible, or REFUTED at primitive level?

The space of candidate gauge groups under consideration:

- **U(1)** — single-generator, Abelian, the R.1 minimal-coupling baseline.
- **SU(2)** — three-generator, non-Abelian, simplest non-trivial non-Abelian.
- **SU(3)** — eight-generator, non-Abelian, QCD-analogue.
- **Direct products** — e.g., SU(3) × SU(2) × U(1) (SM gauge group).
- **Alternative groups** — SO(N), Sp(N), exceptional groups (G_2, F_4, E_6, E_7, E_8).
- **Non-compact gauge groups** — generally rejected on Hilbert-space-positivity grounds; not in primary scope.

This memo evaluates each at primitive level. It does **not** attempt to derive the SM gauge group — that is expected empirical inheritance per Q.0 §5.2.

---

## 2. Inputs from Q.1 (GRH closure)

GRH (Stage Q.1) produces τ_g with four properties:

- **(GRH-1)** τ_g is Case P (η = +1, integer spin, statistics-class compatible with s = 1).
- **(GRH-2)** τ_g carries (1/2, 1/2) Lorentz representation (four-vector A_μ).
- **(GRH-3)** τ_g's L3 interface enforces local gauge invariance.
- **(GRH-4)** σ_{τ_g} = 0 via MR-P.

CANDIDATE-strong status; five refinements outstanding; Q.2 attacks R-2 and R-4.

---

## 3. The Abelian baseline — U(1)

### 3.1 U(1) is FORCED at Stage R.1

Stage R.1's `kg_minimal_coupling_and_current.md` derived A_μ as the connection forced by local-phase-invariance of the participation-measure phase π_K. Local phase rotations form U(1); the connection that compensates them is U(1)-valued.

**FORCED:** U(1) gauge structure exists at primitive level. This is independent of GRH — it is established by R.1's minimal-coupling derivation regardless of whether A_μ is a separate structural object or a participation rule-type.

### 3.2 GRH refines U(1)'s status

Under GRH, the U(1) connection becomes a participation rule-type. This refines the R.1 result without changing it: U(1) was already FORCED; GRH adds the rule-type interpretation.

### 3.3 Charge quantisation under U(1)

Why does U(1) charge come in integer multiples of e (or e/3 for quarks)?

**Candidate primitive-level argument.** If U(1) is *compact* (i.e., U(1) = ℝ/2πℤ rather than ℝ), then the wavefunction-phase periodicity 2π forces charge quantisation: e^{iqα/ℏ} must be single-valued under α → α + 2π, so q must be a discrete unit times some base charge.

Whether U(1) is structurally compact in ED is a **CANDIDATE compactness claim (CC-U1)**. It is not directly forced by Primitives 01–13 as written, but it is consistent with Primitive 09's polarity-phase content (phase π_K is intrinsically periodic in 2π).

**Status of CC-U1:** CANDIDATE plausible. If FORCED, charge quantisation follows. If NOT FORCED, charge quantisation is empirical.

### 3.4 U(1) summary

| Aspect | Status |
|--------|--------|
| Existence of U(1) gauge structure | **FORCED (R.1)** |
| GRH-compatible rule-type realisation | **CANDIDATE-FORCED (Q.1)** |
| U(1) compactness ⇒ charge quantisation | **CANDIDATE plausible** (CC-U1) |
| Numerical value of e (electromagnetic charge) | **INHERITED** |

---

## 4. Non-Abelian extension — SU(N) generally

### 4.1 The structural extension required

For a non-Abelian gauge group SU(N), the gauge connection becomes Lie-algebra-valued:

  A_μ(x) = A^a_μ(x) · T^a,                                                    (1)

where T^a (a = 1, …, N²−1) are SU(N) generators satisfying [T^a, T^b] = if^{abc}T^c. The R.1 minimal-coupling derivation must be repeated with the gauge field carrying the additional internal index a.

**Required structural enrichment of τ_g:**

- The gauge rule-type τ_g must carry an internal index a beyond the (1/2, 1/2) Lorentz index. Total index space: (1/2, 1/2) ⊗ adjoint(SU(N)) — a (4 × (N²−1))-dimensional space per event.
- The L3 interface must enforce gauge invariance under SU(N), which is **non-linear**: A^a_μ → A^a_μ + ∂_μα^a − f^{abc} α^b A^c_μ.
- The gauge field self-interacts via [A_μ, A_ν] terms (no analogue in U(1)).

### 4.2 Primitive-level admissibility

**Primitive 07 (rule-type taxonomy):** Lever L2 (internal-index content) admits arbitrary finite-dimensional discrete index structures. Adding an SU(N)-adjoint index alongside the Lorentz (1/2, 1/2) index is structurally admissible. **Compatible.**

**Primitive 04 (bandwidth):** four-band decomposition applies index-by-index. b^a_K^X for each generator a. **Compatible.**

**Primitive 06 (four-gradient + Lorentz covariance):** non-Abelian gauge fields transform covariantly under SO⁺(3,1) since the internal SU(N) index is Lorentz-scalar. **Compatible.**

**Primitive 10 (individuation):** must respect gauge-quotient — see §6 for R-2 detailed treatment.

**Primitive 11 (commitment):** vertex-anchored (R-3 from Q.1); applies straightforwardly to non-Abelian vertices, with self-coupling vertices among gauge field bands. **Compatible with R-3 closure pending Q.3.**

**Stage R.2 (spin-statistics):** s = 1, η = +1 unchanged by adding internal index. **Compatible.**

**Stage M.2 (masslessness):** MR-P gauge-invariance route extends — if the non-Abelian L3 interface enforces SU(N) gauge invariance, the gauge field is structurally massless at tree level. (Higgs-like SSB can give mass; that is Q.4 content.) **Compatible.**

**Verdict:** SU(N) is **CANDIDATE-admissible at primitive level for any finite N**. No obstruction identified.

### 4.3 Is the R.1 minimal-coupling derivation extendable?

Stage R.1 derived U(1) from local-phase-invariance of the **scalar** participation-measure phase π_K. For SU(N), the analogue would be local invariance under SU(N) acting on a **multi-component** participation measure carrying an SU(N) representation index (fundamental, adjoint, etc.).

**Required structural extension:** a charged rule-type τ_q carrying an SU(N)-fundamental (or other) index, with participation measure Ψ^i_K (i = 1, …, N for fundamental). Local SU(N) invariance Ψ^i → U^i_j Ψ^j with U(x) ∈ SU(N) forces a connection A^a_μ exactly as the U(1) case forced A_μ.

This extension is **structurally clean** — Lever L2 admits the multi-component index — but it is **conditional on a charged rule-type carrying a non-trivial SU(N) representation existing**. Whether ED primitives force such a rule-type to exist (e.g., quark-like rule-types in fundamental of SU(3)) is **rule-type empirical data**, not primitive content.

**Status:** SU(N) gauge structure is structurally admissible. Whether ED forces it to be present is conditional on rule-type-data existence of charged matter in non-trivial representations.

### 4.4 Refinement R-4 (non-Abelian extension) status

R-4 from Q.1 §6.3: "Non-Abelian extension scoping."

**Closure (partial):**
- **Structural admissibility:** FORCED. SU(N) for any finite N is structurally admissible per §4.2.
- **Structural requirement:** NOT FORCED. ED does not force a specific N or even the non-Abelian case at all. Whether non-Abelian gauge structure is realised depends on rule-type empirical content.
- **Specific R.1-style derivation for SU(N):** CANDIDATE — a "Stage Q.3 minimal-coupling extension" memo would close this fully. Provisionally accepted as analogue of R.1 with multi-component matter.

**Verdict:** R-4 partially closed. Non-Abelian structure is admissible structurally; specific gauge groups present in ED are empirical inheritance.

---

## 5. Specific gauge groups

### 5.1 U(1)

Already covered §3. **FORCED at primitive level.** Charge quantisation CANDIDATE via CC-U1.

### 5.2 SU(2)

Three-generator non-Abelian; admissible per §4.2. Structurally clean.

**Empirical role:** weak isospin in SM (massive W^±, Z after SSB). At primitive level, ED admits an SU(2) gauge rule-type but does not force one.

**Status:** **CANDIDATE-admissible.** Empirical occupancy.

### 5.3 SU(3)

Eight-generator non-Abelian; admissible per §4.2.

**Empirical role:** colour gauge group of QCD. Quarks in fundamental (3); gluons in adjoint (8).

**Confinement subtlety:** SU(3) confines at low energy — quarks and gluons do not exist as asymptotic free states. ED's primitive structure does not directly reproduce confinement; this is a non-perturbative QFT phenomenon expected to emerge (if at all) at Q.7 second-quantisation level after gauge-coupling RG flow is added.

**Status:** **CANDIDATE-admissible.** Confinement structure deferred to Q.5 / Q.7.

### 5.4 Direct products (e.g., SU(3) × SU(2) × U(1))

A gauge rule-type carrying multiple commuting gauge structures is admissible — the internal index space becomes a direct product (1/2, 1/2) ⊗ adjoint(SU(3)) ⊗ adjoint(SU(2)) ⊗ U(1).

For the SM gauge group:
- SU(3) (colour, 8 gluons)
- SU(2) (weak isospin, 3 W bosons before SSB)
- U(1) (hypercharge, 1 B boson before SSB)
- After SSB: SU(3) × U(1)_em + 3 massive bosons (W^±, Z); MR-P only protects unbroken U(1)_em.

**Structurally admissible** at primitive level — direct products of admissible groups remain admissible.

**Whether SM is FORCED:** **NO.** ED primitives do not pick out SM gauge group from the space of admissible direct products. SO(10) GUT, SU(5) GUT, Pati-Salam SU(4) × SU(2) × SU(2), trinification SU(3)^3, etc. — all admissible.

**Status:** **CANDIDATE-admissible. SM-specific = EMPIRICAL.**

### 5.5 Alternative groups

#### 5.5.1 SO(N) and Sp(N)

Other compact simple Lie groups beyond SU(N). Structurally admissible per §4.2 (the argument generalises: any compact Lie group with finite-dim adjoint admits an analogous gauge connection rule-type).

**Status:** CANDIDATE-admissible. Empirical occupancy unclear (possibly relevant to GUT scenarios SO(10), SO(32) etc.).

#### 5.5.2 Exceptional groups (G_2, F_4, E_6, E_7, E_8)

Compact, simple, finite-dim adjoint. Structurally admissible per §4.2.

**Status:** CANDIDATE-admissible. Empirical relevance (E_6, E_8 in string-theoretic GUTs) outside ED scope.

#### 5.5.3 Non-compact gauge groups

Non-compact gauge groups (e.g., SL(2, ℝ), Lorentz group as gauge) generally produce indefinite-norm Hilbert spaces, breaking probabilistic interpretation. Stage R.2.4 §3.2 already noted that internal-index unitarity considerations restrict to finite-dim representations of compact-or-Lorentz structure.

**Status:** **STRUCTURALLY DISFAVOURED but not formally REFUTED.** Detailed Hilbert-space analysis is Q.7 content.

---

## 6. Refinement R-2 — gauge-quotient individuation

### 6.1 The problem

Two A_μ configurations differing by a pure-gauge term, A_μ and A'_μ = A_μ + ∂_μα, are physically equivalent. Primitive 10 individuation must respect this — they should not be counted as distinct rule-type instances.

For non-Abelian gauge fields, "pure gauge" is more complex: A_μ and A'_μ = U^{-1} A_μ U + (i/g) U^{-1} ∂_μ U are equivalent under U(x) ∈ SU(N).

**Question:** Does Primitive 10's individuation threshold automatically respect gauge-equivalence, or is an additional gauge-quotient structure required?

### 6.2 Adjacency-equivalence-class construction

Primitive 10 produces an adjacency graph at the chain-local scale, testing whether two same-type chains remain distinguishable. For gauge rule-types, the natural extension is:

**Definition (gauge-quotient adjacency).** Two gauge-rule-type events with participation measures A_μ and A'_μ are **gauge-adjacent** if they differ by a pure-gauge transformation. The individuation graph is then constructed on **gauge-equivalence classes** [A_μ] rather than raw A_μ configurations.

Under this construction:
- Primitive 10's individuation threshold tests adjacency on equivalence classes.
- Two physically distinct gauge configurations are individuated as separate; two gauge-equivalent configurations are unified into a single equivalence class.
- Primitive 11's commitment evolution operates on equivalence classes — gauge-equivalent A_μ produce identical commitment statistics.

### 6.3 Primitive-level admissibility

Is the gauge-quotient construction structurally compatible with Primitive 10?

**Yes.** Primitive 10's individuation threshold is a pairwise distinguishability relation; it admits any equivalence-class structure that respects rule-type symmetry. Gauge invariance is precisely such a structure (it is the L3 interface symmetry for τ_g per GRH-3). The gauge-quotient adjacency definition is consistent with Primitive 10's structural content.

**Caveat:** for non-Abelian SU(N), gauge-quotient is more complex (Wilson-loop / holonomy structure becomes the natural gauge-invariant data). At Stage Q.2 we record that this complexity exists; full implementation is a **Q.3 deliverable** when interaction vertices are specified.

### 6.4 R-2 closure

**Refinement R-2: closed structurally.** Gauge-quotient individuation is admissible at Primitive 10 level via the adjacency-equivalence-class construction. Implementation details for non-Abelian groups (Wilson loops as gauge-invariant content) deferred to Q.3.

---

## 7. FORCED / CANDIDATE / REFUTED table

### 7.1 Per gauge-group structure

| Gauge structure | Status | Reason |
|----------------|--------|--------|
| U(1) (existence) | **FORCED** | R.1 minimal coupling forces A_μ; GRH identifies as rule-type |
| U(1) compactness ⇒ charge quantisation | **CANDIDATE (CC-U1)** | Plausible from Primitive 09 phase periodicity; not yet derived |
| SU(2) | **CANDIDATE-admissible** | Primitive-compatible; empirical occupancy |
| SU(3) | **CANDIDATE-admissible** | Primitive-compatible; confinement structure deferred |
| Direct products generally | **CANDIDATE-admissible** | Sums of admissibles remain admissible |
| SU(3) × SU(2) × U(1) (SM) | **EMPIRICAL** | Specific direct product not forced |
| SO(N), Sp(N) | **CANDIDATE-admissible** | Compact simple Lie group; no obstruction |
| Exceptional (G_2, F_4, E_6, E_7, E_8) | **CANDIDATE-admissible** | Compact simple; no obstruction |
| Non-compact gauge groups | **STRUCTURALLY DISFAVOURED** | Hilbert-space positivity issues; Q.7 detail |
| Non-Abelian generally | **CANDIDATE-admissible** | R-4 partial closure (§4.4) |

### 7.2 Refinements

| Refinement | Status |
|-----------|--------|
| R-2 (gauge-quotient individuation) | **CLOSED structurally** (§6.4); non-Abelian implementation Q.3 |
| R-4 (non-Abelian extension) | **PARTIAL CLOSURE** (§4.4); full closure Q.3 |

### 7.3 Charge-quantisation patterns

| Pattern | Status |
|---------|--------|
| Integer-multiple charges (e, 2e, 3e, …) | **CANDIDATE** via CC-U1 |
| Fractional charges (e/3 for quarks) | **EMPIRICAL** — non-trivial, not derivable from CC-U1 alone |
| Rational charges generally | **CANDIDATE-admissible**, no primitive-level constraint forcing rationality |
| Irrational charges | **STRUCTURALLY DISFAVOURED** if CC-U1 holds; admissible if CC-U1 refuted |

---

## 8. Verdict

### 8.1 Which gauge groups are structurally admissible?

**All compact Lie groups** with finite-dimensional adjoint representation are CANDIDATE-admissible at primitive level. This includes U(1), SU(N) for any finite N, SO(N), Sp(N), and exceptional groups.

### 8.2 Which gauge groups are structurally preferred?

**U(1) is structurally FORCED** at the level of "at least one gauge rule-type exists" — this is the R.1 minimal-coupling output. Beyond U(1), no specific group is structurally preferred — non-Abelian extensions are admissible-but-not-forced.

**Compactness is structurally preferred** over non-compactness on Hilbert-space-positivity grounds, but this is not a strict primitive-level theorem at Q.2; full justification is Q.7.

### 8.3 Which gauge groups are structurally excluded?

**No gauge group is structurally REFUTED at Q.2.** Non-compact gauge groups are STRUCTURALLY DISFAVOURED but not formally rejected. All other candidates are admissible.

### 8.4 What remains inherited or empirical?

- **Specific gauge group of nature** (SU(3) × SU(2) × U(1)): EMPIRICAL.
- **Numerical coupling values** (g_s, g_w, g_Y / e, sin²θ_W): EMPIRICAL.
- **Specific charge quantisation pattern** (including e/3 fractionalisation): mostly EMPIRICAL; CC-U1 may give partial structural content.
- **Generation count, mixing matrices, CP phases:** EMPIRICAL (Q.6 / outside Arc Q scope).
- **GUT structure** (whether SM embeds in SU(5), SO(10), E_6, etc.): EMPIRICAL / SPECULATIVE.

---

## 9. Implications for downstream substages

### 9.1 To Q.3 (interaction vertices)

Q.3 inherits:
- Gauge-quotient individuation (R-2 closed structurally; non-Abelian implementation Q.3 detail).
- Vertex-anchored commitment (R-3 from Q.1).
- Specific gauge group is empirical input — Q.3 structures vertex classification *given* a gauge group, not deriving it.

### 9.2 To Q.4 (Higgs)

Q.4 inherits:
- Massless gauge rule-types from Q.1 + this Q.2 closure.
- The question of how W^±, Z become massive within an originally-massless SU(2) × U(1) sector — this is exactly the Higgs SSB question.

### 9.3 To Q.5 (radiative corrections)

Q.5 will require the gauge group as input for one-loop diagrams (running couplings, β-functions). All Q.5 numerical content is EMPIRICAL.

### 9.4 To Q.7 (second quantisation)

Q.7 will close R-1 (lightlike-worldline reformulation) and resolve the Hilbert-space-positivity argument for compact gauge groups, retroactively justifying the §5.5.3 disfavouring of non-compact cases.

### 9.5 Back-flow to Arc M

GRH closure remains pending the remaining Q.1 refinements (R-1, R-3, R-5). Q.2's discharge of R-2 and partial discharge of R-4 advances GRH toward unconditional FORCED but does not complete the promotion.

---

## 10. Honest framing

### 10.1 What Q.2 achieves

- **U(1) FORCED** at primitive level (already at R.1; GRH adds rule-type interpretation).
- **Non-Abelian extensions admissible** structurally with multi-generator τ_g^a.
- **R-2 closed structurally** — gauge-quotient individuation natively compatible with Primitive 10.
- **R-4 partially closed** — non-Abelian admissibility established; full minimal-coupling extension deferred to Q.3.

### 10.2 What Q.2 does not achieve (honest)

- **No derivation of SM gauge group.** SU(3) × SU(2) × U(1) is not forced by ED primitives. Confirmed empirical inheritance.
- **No prediction of coupling constants.** Numerical values inherited.
- **No confinement mechanism.** SU(3) confinement is non-perturbative QFT phenomenon; primitive-level account not provided.
- **No charge-quantisation derivation.** CC-U1 plausible but not forced; fractional charges fully empirical.
- **No GUT prediction.** GUT structure outside ED scope.

### 10.3 Verdict

This is the second Arc Q memo to settle largely-empirical at the level of specific group choice, paralleling Arc M's H1-dominant closure. The structural achievement is the *admissibility* layer — ED primitives admit any compact Lie group as a gauge rule-type, with R-2 cleanly closed and R-4 partially closed. Specific gauge-group occupancy is rule-type / empirical data.

This continues to support the Arc Q expected verdict: **form-level structural content cleanly admitted, specific occupants empirically inherited.**

---

## 11. FORCED / CANDIDATE / REFUTED summary

### 11.1 FORCED

- **F-Q2.1.** U(1) gauge rule-type exists at primitive level (from R.1 + GRH).
- **F-Q2.2.** Any compact Lie group with finite-dim adjoint is structurally admissible as a gauge rule-type.
- **F-Q2.3.** Direct products of admissible gauge groups are admissible.
- **F-Q2.4.** Gauge-quotient individuation is structurally compatible with Primitive 10 (R-2 closed).
- **F-Q2.5.** Non-Abelian extension admissible (R-4 partial; full closure Q.3).

### 11.2 CANDIDATE

- **C-Q2.1 (CC-U1).** U(1) is structurally compact ⇒ charge quantisation. Plausible via Primitive 09 phase periodicity.
- **C-Q2.2.** Confinement of non-Abelian gauge sectors at low energy. Q.5 / Q.7 deliverable.
- **C-Q2.3.** Hilbert-space-positivity disfavouring of non-compact gauge groups. Full justification Q.7.

### 11.3 REFUTED

- **R-Q2.1.** ED primitives force the SM gauge group SU(3) × SU(2) × U(1). REFUTED at Q.2 — empirical inheritance confirmed.
- **R-Q2.2.** Non-Abelian gauge structure is forced at primitive level. REFUTED — admissible but not forced.
- **R-Q2.3.** Specific GUT group is forced. REFUTED — outside ED scope.

### 11.4 INHERITED

- **I-Q2.1.** Specific gauge group of nature.
- **I-Q2.2.** Numerical coupling constants (e, g_s, g_w, sin²θ_W).
- **I-Q2.3.** Charge quantisation pattern, including fractional quark charges.
- **I-Q2.4.** Generation / flavour / CKM / PMNS structure.

---

## 12. Cross-references

- Upstream: `grh_evaluation.md` (Q.1), `qft_extension_scoping.md` (Q.0), `kg_minimal_coupling_and_current.md` (R.1), `chain_mass_synthesis.md` (M.2).
- Downstream placeholders: `interaction_vertex_classification.md` (Q.3 — closes R-3, completes R-4), `higgs_mechanism_scoping.md` (Q.4), `second_quantisation.md` (Q.7 — closes R-1, R-5, resolves §5.5.3).
- Refinement tracking: R-1 still open (Q.7); R-2 closed (this memo); R-3 open (Q.3); R-4 partial (Q.3 closes); R-5 open (Q.7/Q.8).

---

## 13. One-line summary

**Stage Q.2 finds that ED primitives admit any compact Lie group with finite-dim adjoint as a gauge rule-type structure (U(1) FORCED at R.1 baseline; SU(N), SO(N), Sp(N), exceptional groups, and direct products all CANDIDATE-admissible) but do not force any specific group beyond U(1) — the SM gauge group SU(3) × SU(2) × U(1) is REFUTED-as-forced-by-primitives and confirmed EMPIRICAL inheritance, charge quantisation is CANDIDATE via U(1)-compactness (CC-U1) plausibly from Primitive 09 phase periodicity, refinement R-2 (gauge-quotient individuation) is structurally closed via adjacency-equivalence-class construction, R-4 (non-Abelian extension) is partially closed pending Q.3 minimal-coupling extension memo, and Arc Q continues its expected pattern of form-level admissibility with specific-occupancy empirical inheritance.**
