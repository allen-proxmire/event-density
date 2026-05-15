# Arc E — Memo 5: No-Signaling from V1 Retardation + P11 + Locality

**Status:** Identification memo. Conditional on E-1 (tensor product FORM-FORCED), E-2 (generic non-factorizability FORCED), E-3 (Schmidt FORM-FORCED, values-INHERITED). No new primitives. Identification-not-derivation discipline observed: standard partial-trace algebra is identified as the substrate-level marginalization operation, not derived from no-signaling axioms.

**Date:** 2026-05-08

---

## 1. The CANDIDATE Statement

> **CANDIDATE (E5).** *Given E-1 (tensor product joint Hilbert space $\mathcal{H}_A \otimes \mathcal{H}_B$), T18 (V1 kernel forward-cone-only cross-chain correlations), P11 (commitment irreversibility), ED-I-06 (no fundamental fields → substrate locality), and T10 (Born rule), Bob's reduced state $\rho_B = \mathrm{Tr}_A(|\Psi\rangle\langle\Psi|)$ is independent of Alice's measurement-basis choice. Consequently no classical information is transmitted from Alice to Bob through entanglement alone, and any apparent "instantaneous correlation" produced by Alice's measurement does not constitute a signaling channel.*

The CANDIDATE has three operational pieces:

- **(N1) Marginal-invariance claim.** For any bipartite state $|\Psi\rangle$ and any complete-projective Alice-side measurement basis $\{|a_i\rangle_A\}$, Bob's marginal probability distribution $p_B(b) = \sum_i p(a_i, b)$ is independent of Alice's basis choice.
- **(N2) Substrate causal-justification claim.** T18 + P11 + ED-I-06 forbid any substrate channel by which Alice's basis choice could influence Bob's marginal distribution outside the forward light cone (or, equivalently, after Bob has committed via P11).
- **(N3) Algebraic-identification claim.** The mathematical operation that produces Bob's marginal — the partial trace $\mathrm{Tr}_A$ on $\mathcal{B}(\mathcal{H}_A \otimes \mathcal{H}_B)$ — is the substrate-correct marginalization operation, identified via E-1's tensor-product structure and T10's Born-rule probability assignment.

---

## 2. Substrate Inputs (Inheritance)

| Input | Status | Role |
|---|---|---|
| **E-1** (tensor product FORM-FORCED) | Closed (this arc) | Joint Hilbert space; partial trace $\mathrm{Tr}_A$ well-defined |
| **E-2** (generic non-factorizability FORCED) | Closed (this arc) | Confirms (SP)/(IP) substrate distinction; no-signaling claim is operationally non-trivial only for (SP) configurations |
| **E-3** (Schmidt FORM-FORCED, values-INHERITED) | Closed (this arc) | $\rho_A$ and $\rho_B$ share the same nonzero spectrum (Schmidt eigenvalues); useful for the basis-invariance argument |
| **T18** (V1 kernel forward-cone-only) | FORCED-unconditional | Substrate cross-chain correlations propagate causally only; no backward-cone influence |
| **P11** (commitment irreversibility) | Primitive | Once a participation rule commits (individuation event), the commitment cannot be retroactively updated |
| **ED-I-06** (no fundamental fields) | Canonical guardrail | Forbids any field-sourced non-local signaling channel; substrate locality is what's left |
| **T10** (Born rule) | FORCED-unconditional | Marginal probability $p_B(b)$ is given by the diagonal of $\rho_B$ in the measurement basis |
| **Standard partial-trace algebra** | Free | Linearity, cyclicity of trace, $\mathrm{Tr}_A(E_i \otimes \mathbb{1}_B) X (E_i \otimes \mathbb{1}_B)^\dagger$ structure |

**No new primitives.** **No use of E-4 (monogamy), E-6 (entropy form), or E-7 (synthesis).**

---

## 3. Derivation of (N1): Marginal-Invariance via Partial-Trace Algebra

### 3.1 Setup

Let $|\Psi\rangle \in \mathcal{H}_A \otimes \mathcal{H}_B$ be the joint state. Let $\{|a_i\rangle_A\}_{i=1}^{d_A}$ be a complete orthonormal Alice-side measurement basis with corresponding rank-1 projectors $E_i^A = |a_i\rangle_A\langle a_i|_A$. Let $\{|b_j\rangle_B\}_{j=1}^{d_B}$ be Bob's measurement basis with projectors $F_j^B = |b_j\rangle_B\langle b_j|_B$.

By T10, the joint outcome probability is

$$p(a_i, b_j) = \langle\Psi| (E_i^A \otimes F_j^B) |\Psi\rangle.$$

Bob's marginal probability for outcome $j$, averaged over Alice's outcomes, is

$$p_B(b_j) = \sum_i p(a_i, b_j) = \sum_i \langle\Psi| (E_i^A \otimes F_j^B) |\Psi\rangle.$$

### 3.2 Completeness and partial-trace reduction

The Alice-side projectors are complete: $\sum_i E_i^A = \mathbb{1}_A$. Substituting:

$$p_B(b_j) = \langle\Psi| (\mathbb{1}_A \otimes F_j^B) |\Psi\rangle = \mathrm{Tr}_B\big(F_j^B \cdot \mathrm{Tr}_A(|\Psi\rangle\langle\Psi|)\big) = \mathrm{Tr}_B(F_j^B \rho_B).$$

The reduced state $\rho_B = \mathrm{Tr}_A(|\Psi\rangle\langle\Psi|)$ depends only on $|\Psi\rangle$ and on the choice of "trace out Alice's degrees of freedom." It does **not** depend on the specific basis $\{|a_i\rangle_A\}$ Alice chose to measure in: the sum $\sum_i E_i^A = \mathbb{1}_A$ is the same regardless of which orthonormal Alice-basis is summed.

### 3.3 Basis-invariance of $\rho_B$

Algebraically, for any two complete-orthonormal Alice-side bases $\{|a_i\rangle_A\}$ and $\{|a'_k\rangle_A\}$ related by a unitary $U_A$ on $\mathcal{H}_A$:

$$\sum_i |a_i\rangle_A\langle a_i|_A = \sum_k |a'_k\rangle_A\langle a'_k|_A = \mathbb{1}_A,$$

so the partial trace is computed identically in either basis. The reduced state $\rho_B$ — and therefore Bob's marginal $p_B(b_j) = \mathrm{Tr}_B(F_j^B \rho_B)$ — is invariant under Alice's basis choice.

This is the standard QM no-signaling result. **(N1) is FORCED** as a theorem of the partial-trace algebra applied to E-1's tensor product.

### 3.4 Extension to Alice-side measurements with post-selection

If Alice post-selects on a particular outcome $i$, Bob's *conditional* distribution $p(b_j | a_i) = p(a_i, b_j) / p(a_i)$ does generally depend on Alice's basis. This is the source of correlations. But the *unconditional* marginal $p_B(b_j) = \sum_i p(a_i, b_j)$ — which is what Bob observes when he has no access to Alice's outcomes — remains basis-invariant.

The substrate reading: Bob, in causal isolation from Alice's outcome record, sees a marginal distribution determined solely by the substrate-shared participation rule's structure on Bob's side — not by Alice's basis choice. Correlations exist but require classical communication (transmission of Alice's outcome record at speed-of-light or slower) to become *visible* as patterns. Pure entanglement does not transmit Alice's choice.

### 3.5 Generalization to POVM measurements on Alice's side

For a generic Alice-side POVM $\{M_i^A\}$ with $\sum_i M_i^A = \mathbb{1}_A$ and each $M_i^A$ positive, the same completeness relation gives

$$\sum_i p(M_i^A, b_j) = \langle\Psi| (\mathbb{1}_A \otimes F_j^B) |\Psi\rangle = \mathrm{Tr}_B(F_j^B \rho_B),$$

so basis-invariance generalizes to POVM-invariance. Alice's most general measurement strategy still leaves Bob's marginal unchanged.

---

## 4. Derivation of (N2): Substrate Causal-Justification

The algebraic argument in §3 produces the basis-invariance result. The substrate-side question is: *why does the substrate respect the algebraic argument?* In particular, what forbids a substrate channel that would let Alice's basis choice modify Bob's marginal in violation of the partial-trace independence?

The substrate forbids it via three independent locks.

### 4.1 Lock 1: T18 forward-cone-only V1 kernel

T18 establishes that the V1 vacuum kernel — the substrate object that mediates cross-chain correlations between separated endpoints — is forward-cone-only. Any substrate-level influence from Alice's region to Bob's region propagates strictly forward-in-time within the light cone.

For spacelike-separated Alice and Bob measurements: there is no V1-mediated channel from Alice's basis-choice event to Bob's measurement event. Alice cannot influence Bob's substrate state during the spacelike-separated interval.

For timelike-separated measurements with Alice in Bob's past: Alice's basis-choice event lies in Bob's past light cone; V1-mediated influence is permitted, but it is constrained to whatever Alice's measurement *physically does* on her side — committing her endpoint per ED-I-02 §6 — which propagates forward only as Alice's commitment record (a classical signal traveling at speed-of-light or slower). This is exactly the classical-communication channel that no-signaling is allowed to use; it does not violate the no-signaling theorem.

T18 thus forbids the only candidate substrate-mediated mechanism by which Alice's basis choice could non-classically reach Bob.

### 4.2 Lock 2: P11 commitment irreversibility

P11 establishes that once a participation rule commits (individuates), the commitment is irreversible. If Bob has already committed (measured / individuated) before Alice makes her basis choice, Bob's substrate state is locked. Alice's later choice cannot retroactively update Bob's already-committed individuation.

For simultaneous-measurement (or spacelike-separated) protocols, Bob's commitment occurs in a substrate region causally disjoint from Alice's basis-choice event; the V1-kernel forward-cone-only propagation (Lock 1) ensures no cross-influence, and P11 ensures that even if a non-T18 channel somehow existed (it doesn't, per ED-I-06), Bob's commitment record could not be retroactively rewritten.

P11 therefore closes the only conceivable backdoor — retroactive update of an already-committed substrate record — that could allow Alice's later basis choice to "look like" it influences Bob's marginal.

### 4.3 Lock 3: ED-I-06 forbids field-sourced non-local channels

ED-I-06 (no fundamental fields) forbids the existence of an ontologically-primary field that could carry Alice's basis information non-locally. Any candidate "instantaneous influence field" — the kind of thing standard quantum-foundations literature sometimes posits to make the EPR mechanism "physical" — is structurally absent from ED's substrate.

The substrate has chains, V1 kernel, decoupling surfaces, gradient sparsity, multiplicity, commitment events, and the participation-measure structure. None of these has the type-signature of an instantaneous non-local information channel. ED-I-06 *forbids* the only ontological category that would.

### 4.4 The three locks are independent

T18 (Lock 1) addresses the *propagation* side: cross-chain influence is forward-cone-only.

P11 (Lock 2) addresses the *retroactive-update* side: even if some substrate event happened "later," it cannot rewrite an "earlier" commitment.

ED-I-06 (Lock 3) addresses the *ontological-source* side: there is no fundamental field type that could host non-local signaling.

Each lock independently forbids a specific class of no-signaling-violation. Removing any one of T18, P11, or ED-I-06 would re-open one of the violation classes. Together they cover every conceivable substrate channel.

**(N2) is FORCED** by the conjunction T18 + P11 + ED-I-06.

---

## 5. Identification of (N3): Partial Trace as Substrate-Correct Marginalization

The partial trace $\mathrm{Tr}_A: \mathcal{B}(\mathcal{H}_A \otimes \mathcal{H}_B) \to \mathcal{B}(\mathcal{H}_B)$ is identified — not derived — as the substrate-correct marginalization operation via the following fit:

- **E-1 supplies the joint space**: $\rho_{AB} = |\Psi\rangle\langle\Psi|$ lives on $\mathcal{H}_A \otimes \mathcal{H}_B$.
- **T10 supplies the probability semantics**: $p(a_i, b_j) = \mathrm{Tr}((E_i^A \otimes F_j^B)\rho_{AB}) = \langle\Psi|(E_i^A \otimes F_j^B)|\Psi\rangle$.
- **Marginal probability** $p_B(b_j) = \sum_i p(a_i, b_j)$ identifies algebraically with $\mathrm{Tr}_B(F_j^B \rho_B)$ where $\rho_B = \mathrm{Tr}_A(\rho_{AB})$ — this is §3's derivation.

The identification is unique: for any state $\rho_{AB}$ and any Bob-side observable $F^B$, the marginal $\langle F^B\rangle_{\Psi} = \mathrm{Tr}((F^B)\rho_B) = \mathrm{Tr}((\mathbb{1}_A \otimes F^B) \rho_{AB})$ characterizes $\rho_B$ completely (as it must — Bob's accessible expectation values are by definition $\mathrm{Tr}((\mathbb{1}_A \otimes F^B) \rho_{AB})$ for all $F^B$). The partial trace is the unique map that produces such a $\rho_B$ from any $\rho_{AB}$.

This is identification-not-derivation: partial trace is identified as the substrate-correct marginalization because (a) it produces the correct marginal probabilities under Born + tensor product, and (b) it is mathematically unique up to the universal property of the partial trace as a contraction over $\mathcal{H}_A$. We do not derive partial trace from a more primitive substrate operation; we identify it as the operation E-1 + T10 + marginalization-of-probability collectively pick out.

**(N3) is FORCED** as identification.

---

## 6. Substrate Audit: ED-I-02 Consistency

ED-I-02 §3 says fragments share a single undeveloped participation rule. Could this "shared rule" carry information from Alice's choice to Bob in a way that violates T18 + P11?

### 6.1 The shared rule pre-dates Alice's choice

The shared participation rule was established at the time the parent system fragmented (ED-I-02 §3.1). Alice's later basis choice does not modify the *structure* of the shared rule; it only forces Alice's endpoint to *individuate along* the shared rule's available channels.

Substrate-mechanism reading: when Alice individuates, she "completes" the shared rule on her side. This completion has no backward-cone effect on Bob's side (T18 lock) and no retroactive effect on Bob's already-existing substrate state (P11 lock). What Bob sees on his side is the *pre-existing* shared rule's amplitude weights $\{\sqrt{\lambda_i}\}$ (Schmidt coefficients per E-3) — the same regardless of which basis Alice chose for her completion.

The correlation pattern $p(a_i, b_j)$ depends on Alice's basis choice. The marginal $p_B(b_j) = \sum_i p(a_i, b_j)$ does not, because summing over Alice's choices effectively averages over the basis-dependent post-individuation states, leaving only the basis-independent shared-rule structure visible to Bob.

### 6.2 No hidden channel introduced by ED-I-02

ED-I-02 §9 (entanglement swapping and teleportation) explicitly states: *no information travels; no influence crosses space; no hidden variables are exchanged; no state is transmitted*. The mechanism ED-I-02 attributes to swapping/teleportation is *reassignment / completion of a pre-existing undeveloped rule*, not signal propagation. This is exactly consistent with no-signaling.

ED-I-02's conceptual content is therefore not only consistent with no-signaling — it *predicts* no-signaling at the ontological level. The mathematical no-signaling theorem (§3) is the formal statement of what ED-I-02 §9 says ontologically.

### 6.3 No substrate-level backdoor surfaces in the audit

A complete audit requires checking each substrate channel:

| Substrate channel | Could it carry Alice's basis choice to Bob? | Lock |
|---|---|---|
| V1 kernel cross-chain correlation | No, forward-cone-only | T18 |
| Direct chain coupling at separated endpoints | No, ED-I-06 forbids field-sourced non-locality | ED-I-06 |
| Retroactive update of Bob's prior commitment | No, P11 forbids | P11 |
| Pre-existing shared participation rule | No, the rule was set before Alice's choice and Alice's choice does not modify the rule's structure | ED-I-02 §3 + T18 |
| Decoupling-surface bandwidth (BH-2 / BH-4 style) | No, $\Gamma_{\mathrm{cross}}$ propagation is itself V1-kernel-mediated, hence forward-cone-only | T18 inherited |
| Gauge-rule-type (Arc Q / T17) | No, gauge rule-types are description-level, not substrate channels | T17 + ED-I-06 |
| Substrate gravity (Arc SG / Arc ED-10) | No, substrate gravity propagates via the same V1-kernel-class structures and is forward-cone-only | T18 + Arc SG/ED-10 closure |

All substrate channels checked are locked.

---

## 7. Verdict

> **VERDICT (E5): FORCED.**
>
> No-signaling is a direct consequence of T18 (V1 forward-cone-only) + P11 (commitment irreversibility) + ED-I-06 (no fundamental fields → substrate locality), combined with E-1's tensor-product structure and T10's Born-rule probability assignment. (N1) marginal-invariance is FORCED by the partial-trace algebra applied to E-1. (N2) substrate causal-justification is FORCED by the three independent locks T18, P11, ED-I-06, each closing a distinct class of conceivable signaling channel. (N3) partial trace is identified as the substrate-correct marginalization via E-1 + T10 + uniqueness. ED-I-02 substrate reading is consistent and indeed predicts no-signaling at the ontological level.

**Verdict-class details:**

- **No CONDITIONAL caveat survived the audit.** All substrate channels were checked and locked.
- **No NOT-FORCED option survived.** No substrate-level signaling backdoor identified.
- **Strongest possible structural verdict.** No-signaling in ED is *over-determined*: each of the three locks T18, P11, ED-I-06 independently forbids no-signaling-violation. Removing any one lock would still leave the other two enforcing no-signaling for most violation classes.
- **No new active CANDIDATEs.** Active CANDIDATE inventory remains {}.

---

## 8. Circularity Audit

| Potential circularity | Audit verdict |
|---|---|
| E-4 (monogamy) used as derivation premise? | **No.** Monogamy is not invoked. |
| E-6 (entropy form) used as derivation premise? | **No.** No entropy structure invoked. |
| E-7 (synthesis) used as derivation premise? | **No.** Not invoked. |
| Self-reference of E-5 within itself? | **No.** §3 → §4 → §5 → §6 derivation chain is acyclic. |
| E-1, E-2, E-3 used only as inputs? | **Confirmed.** E-1 supplies tensor product; E-2 supplies (IP)/(SP) substrate distinction reading; E-3 supplies Schmidt structure used in §6.1's "amplitude weights" reading. None re-derived. |
| Bell–Tsirelson used as derivation premise? | **No.** Bell–Tsirelson and CHSH violation are *consistent with* no-signaling (CHSH 2√2 is the maximum violation that is *also* no-signaling-respecting), but not used as a premise here. |
| T18, P11, ED-I-06 treated as primitives, not re-derived? | **Confirmed.** T18 is FORCED-unconditional from Arc B closure; P11 is a primitive; ED-I-06 is canonical guardrail. Used as inputs only. |

**Acyclicity confirmed.**

---

## 9. Falsification

### 9.1 Falsifier for FORCED verdict (current verdict)

A substrate-level construction satisfying all of T18, P11, ED-I-06, E-1, T10, and ED-I-02, in which Bob's marginal $\rho_B$ depends on Alice's measurement-basis choice. Concretely: a substrate channel such that for some bipartite state $|\Psi\rangle$ and some pair of Alice-side bases $\{|a_i\rangle_A\}$ and $\{|a'_k\rangle_A\}$, the marginals computed by Bob differ depending on which basis Alice measures in.

Per §3.3, this is mathematically impossible given the algebraic inputs (partial trace is basis-independent). Per §4 and §6, this is substrate-impossible given the three locks.

A successful exhibition of such a construction would refute *one* of the inputs — most likely T18 or ED-I-06.

### 9.2 Falsifier for CONDITIONAL verdict (rejected)

An auxiliary assumption beyond T18 + P11 + ED-I-06 + E-1 + T10 that is required for the §3 derivation. The audit identifies none. (Standard partial-trace algebra is mathematics, not auxiliary substrate assumption.)

### 9.3 Falsifier for NOT-FORCED verdict (rejected)

A substrate-level signaling channel consistent with all primitives. The §6 audit checks each candidate channel and locks it against signaling. A future arc identifying a non-V1-non-field substrate channel that could carry Alice's basis choice would re-open this audit.

### 9.4 Empirical-side falsifier

Any experimental observation of faster-than-light classical information transmission via entanglement-only — i.e., Bob extracting Alice's basis choice from his marginal alone, without classical communication. Such observations are not reported and would refute either E-5's substrate inputs or quantum mechanics itself.

Modern Bell-test experiments with strict-locality enforcement (e.g., Hensen 2015, Giustina 2015, Shalm 2015) consistently confirm no-signaling: violations of Bell inequalities occur, but no usable signal is extractable from one party's marginal.

### 9.5 Subtle empirical edge case

If the locality loophole in some Bell test were *closable* with a true superluminal-signaling protocol, the falsifier above would apply. Current experiments instead confirm the no-signaling-respecting Tsirelson 2√2 violation, consistent with E-5's verdict.

---

## 10. Consequences for the Arc

1. **E-5 closes cleanly as identification memo.** No-signaling is FORCED in ED, and its substrate-level over-determination by three independent locks (T18, P11, ED-I-06) is a structural feature stronger than the standard QM single-derivation result.

2. **Quantum-information cross-link.** The combination "Bell-Tsirelson 2√2 violation + no-signaling" is the structural signature of *quantum* (vs. *post-quantum*) bipartite correlations. The Popescu-Rohrlich box achieves CHSH = 4 while still respecting no-signaling but is not realizable in QM. ED inherits both the Tsirelson 2√2 ceiling (Phase-1) and no-signaling (E-5); together they characterize quantum-correlation strength as the substrate-FORCED outcome. This is identification-content for Arc E's E-7 synthesis.

3. **Substrate over-determination as a structural feature.** No-signaling in ED is forbidden through three independent mechanisms. This is unusual: most no-signaling derivations in the QM literature are single-derivation (relativistic causality + linearity of QM). ED's three-lock structure (causal kernel + commitment irreversibility + no fundamental fields) is robust against amendment of any single lock. This robustness is structurally similar to the over-determination noted in B1 (time's arrow extended via cascade-from-V1 + R1-bypass) per the Investigation Priority List.

4. **Substantive-derivation pair next.** With E-1, E-2, E-3, E-5 closed (all articulation/identification memos), the remaining open work in Arc E is the substantive-derivation pair E-4 (monogamy from cross-chain bandwidth) and E-6 (entropy form). Both require substrate-level arguments beyond standard Hilbert-space mathematics.

5. **No new active CANDIDATEs.** Active CANDIDATE inventory remains {}.

6. **No new sensitivity flags.** E-5 inherits T18, P11, ED-I-06 load-bearings without adding new ones. Any future amendment to T18 (e.g., relaxation of forward-cone-only kernel) would require re-deriving the §4.1 lock; this is a known sensitivity, not an active concern.

---

## 11. Summary

**What this memo accomplished.**

- Stated the E-5 CANDIDATE (§1) and decomposed it into (N1) marginal-invariance, (N2) substrate causal-justification, (N3) algebraic identification.
- Derived (N1) via standard partial-trace algebra applied to E-1's tensor-product joint space + T10's Born-rule probability assignment (§3).
- Derived (N2) via three independent substrate locks: T18 (forward-cone-only V1 kernel) + P11 (commitment irreversibility) + ED-I-06 (no fundamental fields). Each lock independently forbids a specific class of no-signaling-violation (§4).
- Identified (N3): partial trace is the substrate-correct marginalization operation via E-1 + T10 uniqueness (§5).
- Substrate-audited via ED-I-02 (§6): the "shared participation rule" carries no information from Alice's *choice* to Bob; ED-I-02 §9 explicitly endorses no-signaling at the ontological level.
- Issued the verdict: **FORCED** (§7).
- Confirmed acyclicity (§8) and provided substrate-level falsifiers (§9).
- Identified the structural over-determination as a feature parallel to B1 (§10).

**What this memo did not do.**

- Did not derive Tsirelson 2√2 bound — that is FORCED-unconditional from Phase-1, used here only as identification target.
- Did not derive monogamy — that is E-4's deliverable, structurally independent of no-signaling.
- Did not derive entanglement entropy — that is E-6's deliverable.
- Did not address the relativistic-frame-dependence of measurement timing in Bell tests. Standard QM is no-signaling under any choice of frame; ED inherits the same property via T18's forward-cone-only kernel being Lorentz-covariant after DCGT coarse-graining. This is downstream content; flag if relevant for E-7 synthesis.
- Did not address the role of vacuum entanglement / Reeh-Schlieder-style structure in QFT contexts. Phase-1 Bell–Tsirelson handles particle-mechanics-level CHSH; QFT-level no-signaling is downstream of Arc Q's QFT-extension content.

**Recommended next steps.**

1. **E-4 (next memo): Monogamy from cross-chain bandwidth budgets.** First substantive-derivation memo of Arc E. Loads on Q-COMPUTE Memo 1's $\Gamma_{\mathrm{cross}}$ structure, BH-2's decoupling-surface bandwidth, DCGT's hydrodynamic-window scale separation, and substrate bandwidth-additivity (P04). Expected verdict: form-FORCED qualitatively (full A-B entanglement precludes additional A-C entanglement), coefficient-INHERITED (specific CKW coefficient and squared structure from substrate-derived bandwidth scaling). Estimated 1–2 sessions.

2. **E-6 (after E-4): Entanglement-entropy form $S = -\mathrm{Tr}(\rho \log \rho)$.** Second substantive-derivation memo. Substrate inputs: E-3 Schmidt eigenvalues + ED-I-01 multiplicity-as-entropy-analogue + Shannon-Khinchin axioms applied at substrate level. Expected verdict: form-FORCED, coefficient-INHERITED, parallel to BH-5 area-law. Estimated 1–2 sessions.

3. **(After E-6) E-7 synthesis.** Cross-domain echoes with BH-4 (entanglement straddling), Q-COMPUTE (Γ_cross ceiling), and Phase-1 (Bell–Tsirelson with no-signaling jointly characterizing quantum correlations). ER=EPR-class structural reading if it surfaces; honest "no echo found" is a valid outcome.

4. **(Documentation, low priority) Phase-1 inheritance ledger update.** With E-1, E-2, E-3, E-5 closed, the Bell–Tsirelson 2√2 inheritance is now substantially tightened. Documentation pass when convenient.

---

**Pause for further instruction.**
