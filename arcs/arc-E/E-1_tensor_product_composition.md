# Arc E — Memo 1: Tensor-Product Composition

**Status:** Gate memo for Arc E. Verdict determines downstream Arc E memos and retroactively updates Phase-1 Bell–Tsirelson inheritance ledger. No new primitives. Identification-not-derivation discipline observed (Bell–Tsirelson is identification target, not derivation premise).

**Date:** 2026-05-08

---

## 1. The CANDIDATE Statement

Restated verbatim from E-0 §2.3:

> **CANDIDATE (E1).** *Given two ED-substrate endpoints $A$ and $B$ that share a single undeveloped participation rule (in the sense of ED-I-02), the joint participation measure on the bilocal endpoint configuration is carried on the tensor product $\mathcal{H}_A \otimes \mathcal{H}_B$ of the single-endpoint Hilbert spaces (in the sense of U2), with the natural induced inner product $\langle \psi_A \otimes \psi_B \,|\, \phi_A \otimes \phi_B\rangle = \langle\psi_A|\phi_A\rangle \langle\psi_B|\phi_B\rangle$ extended bilinearly.*

The CANDIDATE has three substrate-level claims, in order of derivational precedence:

- **(C1) Bilinearity claim.** The joint-participation map $f: \mathcal{H}_A \times \mathcal{H}_B \to \mathcal{H}_{AB}$ that sends an independently-prepared pair $(|\psi_A\rangle, |\psi_B\rangle)$ to its joint-system representation is linear in each argument separately.
- **(C2) Universality claim.** The joint-system Hilbert space $\mathcal{H}_{AB}$ is the smallest complex inner-product space containing the image of $f$ and closed under linear combination — i.e., $\mathcal{H}_{AB} \cong \mathcal{H}_A \otimes \mathcal{H}_B$ via the universal property of tensor products.
- **(C3) Inner-product claim.** The inner product on $\mathcal{H}_{AB}$ that reproduces independent-preparation Born-rule factorization is the bilinearly-extended product inner product.

E-1 examines each in turn from the substrate side.

---

## 2. Substrate Inputs and the Assumption Audit

The derivation uses only the following inputs (each FORCED-unconditional or canonical guardrail at the time of writing):

| Input | Status | Role |
|---|---|---|
| **P04** (bandwidth additivity for independent contributions) | Primitive | Forces multiplicative factorization of joint participation contributions when subsystems are causally and structurally independent |
| **P09** (independence / U(1) phase structure) | Primitive | Forces complex-amplitude structure with $\mathbb{C}$-linearity, not $\mathbb{R}$ or $\mathbb{H}$ |
| **U2** (single-endpoint inner-product structure / T11–T12) | FORCED-unconditional | Supplies $\mathcal{H}_A$ and $\mathcal{H}_B$ as complex inner-product spaces with linear superposition |
| **T18** (V1 kernel forward-cone-only cross-chain correlations) | FORCED-unconditional | Inheritance check: cross-chain correlations propagate on a substrate-derived bilocal kernel — consistent with bilocal joint structure |
| **ED-I-02** (single undeveloped participation rule expressed at multiple endpoints) | Conceptual ground | Establishes that the bilocal joint system is *one rule, two endpoints*, not *two independent rules paired by external label* |
| **DCGT** (substrate-to-continuum bridge) | FORCED structural-foundation | Inheritance check: any substrate-FORCED joint-space structure survives coarse-graining to continuum |
| **ED-I-06** (no fundamental fields) | Canonical guardrail | Forbids cocycle / superselection-sector structure sourced by an ontologically-primary field |

**No new primitives introduced.** **No use of Bell–Tsirelson, Schmidt decomposition, monogamy, or any downstream Arc E content.**

---

## 3. Derivation of (C1): Bilinearity from Bilocal Participation

### 3.1 Independent preparation at the substrate level

Per ED-I-02 §3, two endpoints $A$ and $B$ that have *not* yet been individuated may nevertheless be in either of two configurations:

- **(SP) Single-rule shared configuration.** Both endpoints express one undeveloped participation rule (the entanglement case). The joint structure is *not* a product of independent single-endpoint structures.
- **(IP) Independent-preparation configuration.** Each endpoint expresses its own developed participation rule, and the two are causally and structurally independent. This is the substrate analogue of "Alice prepares $|\psi_A\rangle$ and Bob, in causal isolation, prepares $|\psi_B\rangle$."

Configurations (SP) and (IP) are both substrate-permitted; (SP) is the entanglement case and is what ED-I-02 §3 emphasizes. (IP) is the *non-entangled* case and is the substrate-level definition of a *product state*.

The joint-participation map $f$ is defined first on the (IP) configurations: $f$ sends an (IP) pair $(|\psi_A\rangle, |\psi_B\rangle)$ to its substrate joint representation $|\psi_A \otimes \psi_B\rangle$. The (SP) configurations are recovered downstream as superpositions of (IP) configurations once $\mathcal{H}_{AB}$ is constructed (this is what makes entanglement *generic* in the joint space — see E-2).

### 3.2 Bilinearity argument

Fix Bob's preparation at $|\chi\rangle_B$. Vary Alice's preparation as $|\psi_A\rangle = \alpha|\psi_1\rangle + \beta|\psi_2\rangle$, an admissible single-endpoint superposition by U2.

Two questions:

- **(Q1)** Is the joint state $f(|\psi_A\rangle, |\chi\rangle_B)$ a definite vector in $\mathcal{H}_{AB}$?
- **(Q2)** Does $f$ respect Alice's superposition: $f(\alpha|\psi_1\rangle + \beta|\psi_2\rangle, |\chi\rangle_B) = \alpha f(|\psi_1\rangle, |\chi\rangle_B) + \beta f(|\psi_2\rangle, |\chi\rangle_B)$?

(Q1) is automatic: U2 establishes that single-endpoint preparations have unique Hilbert-space representations, and (IP) extends this to the joint by causal-structural independence.

(Q2) is the bilinearity claim. Argue:

- **Step 1 (P04 contribution).** Alice's preparation is a superposition of two substrate channels $|\psi_1\rangle$ and $|\psi_2\rangle$. By P04 (bandwidth additivity for independent contributions), the substrate participation contributions of the two channels add. In an (IP) configuration, Alice's channels are causally and structurally independent of Bob's, so Bob's preparation $|\chi\rangle_B$ couples *separately* to each of Alice's channels — there is no substrate coupling between $|\psi_1\rangle$ and $|\psi_2\rangle$ that depends on $|\chi\rangle_B$. Hence the joint contribution decomposes channel-by-channel: contribution from $(|\psi_1\rangle, |\chi\rangle_B)$ + contribution from $(|\psi_2\rangle, |\chi\rangle_B)$.

- **Step 2 (P09 contribution).** The phases $\alpha$ and $\beta$ live in $U(1) \subset \mathbb{C}$ per P09. They modulate Alice's channel amplitudes without affecting Bob's. Because (IP) is causally and structurally independent, the substrate phase structure on Alice's side propagates through to the joint amplitude unchanged: Alice's contribution to $f(\alpha|\psi_1\rangle + \beta|\psi_2\rangle, |\chi\rangle_B)$ carries the same $\alpha, \beta$ weights it carried in Alice's single-endpoint preparation.

- **Step 3 (U2 contribution).** U2's single-endpoint inner-product structure says that the superposition $\alpha|\psi_1\rangle + \beta|\psi_2\rangle$ on Alice's side is the *same* substrate object as the formal $\mathbb{C}$-linear combination. There is no additional structure on Alice's side that distinguishes "single-endpoint $\alpha|\psi_1\rangle + \beta|\psi_2\rangle$" from "Alice's contribution to the joint $\alpha|\psi_1\rangle + \beta|\psi_2\rangle$."

Combining the three steps: $f(\alpha|\psi_1\rangle + \beta|\psi_2\rangle, |\chi\rangle_B) = \alpha f(|\psi_1\rangle, |\chi\rangle_B) + \beta f(|\psi_2\rangle, |\chi\rangle_B)$.

Bilinearity in Bob's argument follows by the same argument with $A$ and $B$ swapped (the substrate is symmetric in endpoint labels per ED-I-02).

**(C1) is FORCED by P04 + P09 + U2 + ED-I-02.**

### 3.3 What FORCED means here

Bilinearity is FORCED in the sense that no consistent substrate construction can produce a non-bilinear joint map without violating one of P04, P09, U2, or ED-I-02. A non-bilinear $f$ would require either: (a) a substrate channel coupling between $|\psi_1\rangle$ and $|\psi_2\rangle$ that depends on Bob's preparation, contradicting (IP) structural independence; or (b) a phase-modulation rule that violates P09; or (c) a single-endpoint structure that distinguishes "Alice's superposition in isolation" from "Alice's contribution to a joint preparation," contradicting U2.

---

## 4. Derivation of (C2): Tensor Product as Universal Bilinear Extension

### 4.1 The universal property and its substrate reading

The tensor product $\mathcal{H}_A \otimes \mathcal{H}_B$ is, by its standard mathematical definition, the universal complex vector space equipped with a bilinear map $\otimes: \mathcal{H}_A \times \mathcal{H}_B \to \mathcal{H}_A \otimes \mathcal{H}_B$ such that any other complex vector space $V$ with a bilinear map $g: \mathcal{H}_A \times \mathcal{H}_B \to V$ admits a unique linear $\tilde{g}: \mathcal{H}_A \otimes \mathcal{H}_B \to V$ with $g = \tilde{g} \circ \otimes$.

The substrate reading: $\mathcal{H}_{AB}$ is the smallest space carrying $f$ as a bilinear map and closed under linear combination — no more, no less.

- **No more:** $\mathcal{H}_{AB}$ contains nothing beyond what $f$ + linear closure produce, because anything more would be additional substrate structure not present in P04 / P09 / U2 / T18 / ED-I-02. The no-new-primitives discipline forbids it.
- **No less:** $\mathcal{H}_{AB}$ contains all linear combinations of (IP) joint states. Because $f$ is bilinear (§3) and U2 establishes linear closure on each side, the joint substrate must contain the full $\mathbb{C}$-linear span of $\{f(|\psi_A\rangle, |\psi_B\rangle) : |\psi_A\rangle \in \mathcal{H}_A, |\psi_B\rangle \in \mathcal{H}_B\}$. Anything less would forbid certain superpositions of independently-prepared states, contradicting U2's linear closure.

The universal property then identifies $\mathcal{H}_{AB}$ uniquely (up to $\mathbb{C}$-linear isomorphism) as $\mathcal{H}_A \otimes \mathcal{H}_B$.

### 4.2 ED-I-02's role: justifying that (SP) configurations live in the same space

(IP) configurations alone could in principle live in a smaller subspace consisting only of product states. The substrate forbids this restriction: ED-I-02 establishes that (SP) configurations — single-rule, multi-endpoint, structurally entangled — are substrate-permitted. (SP) configurations are *not* product states (otherwise they would carry two independent rules, contradicting "one rule"). So the joint space must contain non-product vectors.

Once non-product vectors are admitted *and* linear closure is enforced, the only complex inner-product space satisfying both is the full tensor product. Restricting to a strict subspace would either exclude some (SP) configurations (refuted by ED-I-02) or break linear closure (refuted by U2).

**(C2) is FORCED.**

### 4.3 Finite-dim vs. infinite-dim completion: a clean note

For finite-dimensional $\mathcal{H}_A$ and $\mathcal{H}_B$, the algebraic tensor product is already complete and the construction is pointwise FORCED.

For infinite-dimensional $\mathcal{H}_A$ and $\mathcal{H}_B$, $\mathcal{H}_A \otimes \mathcal{H}_B$ is the Hilbert-space tensor product (Cauchy completion of the algebraic tensor product in the induced norm). Completion is inherited from U2 (which establishes Hilbert-space — i.e., complete — inner-product structure on each side); the joint norm is bilinear-induced (§5), so completeness propagates. **No conditionality enters here** — completion is a downstream consequence of U2, not an auxiliary assumption.

---

## 5. Derivation of (C3): Induced Inner Product

### 5.1 Independent-preparation Born-rule factorization

In an (IP) configuration $(|\psi_A\rangle, |\psi_B\rangle)$ vs. $(|\phi_A\rangle, |\phi_B\rangle)$, the joint Born-rule transition probability is the product of marginals:

$$P(\psi \to \phi)_{AB}^{(IP)} = P(\psi \to \phi)_A \cdot P(\psi \to \phi)_B = |\langle\psi_A|\phi_A\rangle|^2 \cdot |\langle\psi_B|\phi_B\rangle|^2.$$

This is the substrate statement of *independence of the two preparations*: causal and structural separation forces the joint outcome statistics to factor multiplicatively. Loads on T10 (Born) at each endpoint and on P04 + ED-I-02 for the multiplicative factorization.

### 5.2 Inner product up to phase

The transition amplitude $\langle\psi_A \otimes \psi_B | \phi_A \otimes \phi_B\rangle$ on the joint space must satisfy $|\cdot|^2 = $ above factorization. Taking the natural choice

$$\langle\psi_A \otimes \psi_B | \phi_A \otimes \phi_B\rangle = \langle\psi_A|\phi_A\rangle \cdot \langle\psi_B|\phi_B\rangle$$

yields the correct $|\cdot|^2$. P09 (U(1) phase structure) fixes the global phase convention; no other sesquilinear form on $\mathcal{H}_A \otimes \mathcal{H}_B$ that reproduces the (IP) factorization is consistent with bilinear extension to (SP) configurations *and* with P09's phase convention (any non-natural choice would introduce an extra phase factor uncoordinated with P09's U(1)).

### 5.3 Sesquilinear extension

Bilinear extension of the inner product to all of $\mathcal{H}_A \otimes \mathcal{H}_B$ is an automatic consequence of $\mathbb{C}$-linearity in the second argument and conjugate-linearity in the first (the convention of U2). No conditionality.

**(C3) is FORCED.**

---

## 6. Audit of Alternatives

For each alternative joint-Hilbert-space construction, test consistency with P04, P09, U2, T18, ED-I-02, ED-I-06.

### 6.1 Direct sum $\mathcal{H}_A \oplus \mathcal{H}_B$

Vectors: ordered pairs $(\psi_A, \psi_B)$ with $\psi_A \in \mathcal{H}_A, \psi_B \in \mathcal{H}_B$. Dimension $d_A + d_B$.

- **Refutation 1 (P04):** Direct sum has no bilinear pairing. The joint-participation map $f$ would have to be defined as $f(\psi_A, \psi_B) = (\psi_A, \psi_B)$, but this is *additively* linear in each argument when the other is held fixed at zero — and *not at all* defined when both are nonzero in the natural (IP) sense. P04's multiplicative factorization of joint contributions has no representation.
- **Refutation 2 (ED-I-02):** Direct sum represents "either $A$ or $B$" structure (the standard QM use of direct sum for two non-interacting branches of a single system), not "$A$ and $B$ jointly." Cannot represent (SP) configurations at all.
- **Refutation 3 (U2 linear closure):** Linear combinations $\alpha(\psi_A, 0) + \beta(0, \psi_B) = (\alpha\psi_A, \beta\psi_B)$ produce vectors that are neither single-endpoint nor product-form joint. The joint reading is incoherent with substrate (IP).

**Refuted.**

### 6.2 Cartesian / classical product

Vectors: ordered pairs as in §6.1, but no superposition between configurations.

- **Refutation (U2):** Disallows joint superpositions. Cannot represent any (SP) configuration with non-trivial joint amplitudes.
- **Refutation (Bell–Tsirelson identification target):** Classical-product joint structure is the LHV joint structure; CHSH bound 2 not 2√2. Phase-1 Bell–Tsirelson 2√2 is FORCED-unconditional (modulo this memo's verdict on E-1's CANDIDATE), so classical product is identified as the structure that *fails* to recover the substrate-derived 2√2. (Identification, not derivation premise.)

**Refuted.**

### 6.3 Non-associative / exotic bilinear products

E.g., octonionic-tensor structures, twisted tensor products with non-trivial cocycle $\omega$, graded tensor products with non-$\mathbb{Z}_2$ grading.

- **Refutation 1 (P09):** P09 establishes U(1) — abelian, associative, commutative phase structure. Non-associative bilinear products require non-associative phase structure (e.g., octonionic), which contradicts P09.
- **Refutation 2 (no-new-primitives):** A cocycle $\omega$ would have to be a substrate-level object. ED's substrate inventory contains no source for $\omega$. Introducing one violates the no-new-primitives discipline of Arc E.
- **Refutation 3 (ED-I-06):** A graded structure or superselection-sector structure would be sourced by an ontologically-primary field, forbidden by ED-I-06.

**Refuted.**

### 6.4 Hybrid: direct sum of tensor products of subspaces

The structure of superselection sectors: $\mathcal{H}_{AB} = \bigoplus_i \mathcal{H}_A^{(i)} \otimes \mathcal{H}_B^{(i)}$ for some partitioning into sectors.

- **Refutation 1 (ED-I-06):** Superselection rules are sourced by ontologically-primary structure. ED-I-06 forbids fundamental fields; the substrate is structurally connected at the substrate level per ED-I-02.
- **Refutation 2 (ED-I-02):** ED-I-02's "single undeveloped participation rule" framework is incompatible with a-priori partition of the joint space into non-communicating sectors. Any sectorization at the joint level would require sectorization at the single-endpoint level (which U2 does not produce), and the substrate is uniform-non-sectorized per the ED-I-02 reading.

**Refuted as substrate-FORCED structure.** (Note: superselection sectors *can* arise as a derived consequence of einselection / decoherence — a downstream phenomenon, not a substrate-level joint-composition rule. Arc E does not forbid emergent sectorization; it forbids it as a substrate-level alternative to tensor product.)

### 6.5 Summary of audit

| Alternative | Refuted by | Status |
|---|---|---|
| Direct sum $\mathcal{H}_A \oplus \mathcal{H}_B$ | P04 + ED-I-02 + U2 | Refuted |
| Cartesian / classical product | U2 + Bell–Tsirelson identification target | Refuted |
| Non-associative / exotic bilinear | P09 + no-new-primitives + ED-I-06 | Refuted |
| Twisted tensor with cocycle | no-new-primitives + ED-I-06 | Refuted |
| Hybrid superselection-sector decomposition | ED-I-06 + ED-I-02 | Refuted at substrate level |

**No substrate-consistent alternative to tensor product survives.**

---

## 7. Gate Verdict

> **VERDICT (E1): FORM-FORCED.**
>
> Tensor-product composition of two single-endpoint Hilbert spaces $\mathcal{H}_A \otimes \mathcal{H}_B$, with the bilinearly-induced inner product $\langle\psi_A \otimes \psi_B | \phi_A \otimes \phi_B\rangle = \langle\psi_A|\phi_A\rangle \langle\psi_B|\phi_B\rangle$, is the unique substrate-consistent joint participation-measure structure. (C1) bilinearity is FORCED by P04 + P09 + U2 + ED-I-02. (C2) universality (i.e., tensor product as smallest closed bilinear-carrying space) is FORCED by U2 linear closure + ED-I-02 (SP)-configuration substrate-permittance + no-new-primitives. (C3) induced inner product is FORCED by Born-rule independent-preparation factorization (T10) + P09 phase convention. All five alternatives (direct sum, classical product, non-associative bilinear, twisted-with-cocycle, hybrid sectorization) are refuted on substrate-primitive grounds.

**Verdict-class details:**

- **Form-FORCED:** the *structural identity* of the joint Hilbert space as $\mathcal{H}_A \otimes \mathcal{H}_B$ with bilinear-induced inner product is FORCED.
- **Value-INHERITED is N/A** for E-1: there are no numerical coefficients in the joint-composition rule that need separate inheritance accounting. The Schmidt coefficients (E-3), entanglement-entropy coefficient (E-6), and monogamy CKW coefficient (E-4) are downstream and inherit from U2 / Born / Q-COMPUTE / DCGT respectively.
- **No CONDITIONAL caveat survived the audit.** The finite-dim/infinite-dim completion question (§4.3) was resolved as a downstream consequence of U2 completeness, not an auxiliary assumption.

---

## 8. Circularity Audit

| Potential circularity | Audit verdict |
|---|---|
| Bell–Tsirelson 2√2 used as derivation premise? | **No.** Bell–Tsirelson appears only in §6.2 as identification target for the *failure mode* of classical product (which would yield CHSH 2, not 2√2). Bell–Tsirelson does not appear anywhere in §3, §4, §5 (the derivation chain). |
| Schmidt decomposition used as derivation premise? | **No.** Schmidt is the subject of E-3, not invoked here. |
| Monogamy / CKW used as derivation premise? | **No.** Monogamy is the subject of E-4, not invoked here. |
| No-signaling used as derivation premise? | **No.** No-signaling is the subject of E-5, not invoked here. |
| Entanglement entropy used as derivation premise? | **No.** Entropy is the subject of E-6, not invoked here. |
| Phase-1 closure content (T10–T16) used as derivation premise? | **Only T10 (Born) and U2 (T11–T12) are used**, both as substrate inputs already FORCED-unconditional from prior closed arcs. Use as inputs (not premises) is permitted by the inheritance discipline. |
| Self-reference within E-1? | **No.** §3 → §4 → §5 derivation chain is acyclic; §6 audit consumes §3–§5 results; §7 verdict consumes §6. |

**Acyclicity confirmed.** The derivation chain depends only on already-closed substrate inputs and on E-1's own §3–§5 in linear order.

---

## 9. Falsification Section

For each verdict class, a concrete substrate-level falsifier:

### 9.1 Falsifier for FORM-FORCED verdict (current verdict)

A substrate construction satisfying all of P04, P09, U2, T18, ED-I-02, ED-I-06, and producing a joint Hilbert space $\mathcal{H}_{AB}$ that is *not* isomorphic (as a complex inner-product space) to $\mathcal{H}_A \otimes \mathcal{H}_B$ with bilinear-induced inner product. Concretely: (a) a non-product joint state for which the bilinearity of §3.2 fails, or (b) a substrate-level channel coupling between Alice's superposition components and Bob's preparation that contradicts (IP) structural independence, or (c) a substrate-level cocycle / sectorization not sourced from any active primitive but consistent with the existing primitive list.

If such a construction is exhibited, FORM-FORCED is downgraded.

### 9.2 Falsifier for CONDITIONAL verdict (not the current verdict, but registered)

An auxiliary assumption $A^*$ such that: (i) the §3–§5 derivation requires $A^*$ for one of its steps to go through; (ii) $A^*$ is not itself derivable from P04 + P09 + U2 + T18 + ED-I-02 + DCGT + ED-I-06; (iii) without $A^*$, a non-tensor-product alternative (or a refinement of one of the §6 alternatives) is admitted.

The audit in §3 and §4 above did *not* identify such an $A^*$. If a future memo identifies one, the verdict downgrades to CONDITIONAL-on-$A^*$.

### 9.3 Falsifier for NOT-FORCED verdict (rejected)

Two or more substrate-consistent joint-Hilbert-space constructions, both satisfying all primitives and ED-I-02, with no derivation selecting one over the other. This is precisely what the §6 alternative audit tested for and failed to find.

### 9.4 Empirical-side falsifier (independent of substrate-side)

Any experimental observation of bipartite quantum correlations that violate the joint-Hilbert-space tensor-product structure (e.g., observed CHSH $> 2\sqrt{2}$, or Bell-correlation patterns inconsistent with any density operator on $\mathcal{H}_A \otimes \mathcal{H}_B$). Such observations are not currently reported; the empirical record is consistent with tensor-product joint structure to high precision. Empirical falsification of E-1's verdict would require either a Tsirelson-bound violation (refuting tensor-product unitarity structure) or a non-density-operator joint statistical structure (refuting tensor-product Hilbert-space identity).

---

## 10. Consequences for the Arc

1. **E-1 closes as gate; E-2 through E-7 may now be drafted.** All downstream Arc E memos may use $\mathcal{H}_A \otimes \mathcal{H}_B$ with bilinear-induced inner product as a FORCED substrate structure rather than a CANDIDATE.

2. **Phase-1 Bell–Tsirelson inheritance ledger update.** Previously, Phase-1's FORCED-unconditional Bell–Tsirelson 2√2 carried tensor-product joint structure as an unjustified substrate input. With E-1's FORM-FORCED verdict, that input is now substrate-justified. Bell–Tsirelson's status is now genuinely unconditional, not conditional-on-tensor-product. (Documentation update only; no derivation-content change.)

3. **No active CANDIDATE introduced.** Active CANDIDATE inventory remains {} as of arc-opening tally. E-1 *closes* a candidate without opening one.

4. **Verdict-class projection for downstream items refined.** With E-1 FORM-FORCED:
   - E-2 (generic non-factorizability): now expected trivially-FORCED.
   - E-3 (Schmidt): now expected form-FORCED-values-INHERITED via spectral theorem.
   - E-4 (monogamy): still requires substantive derivation; depends on Q-COMPUTE/DCGT/BH-2 cross-bandwidth structure (not directly affected by E-1's FORCED status).
   - E-5 (no-signaling): now expected FORCED via partial-trace argument well-defined on $\mathcal{H}_A \otimes \mathcal{H}_B$.
   - E-6 (entropy form): still requires substantive derivation.
   - E-7 (synthesis): preparation phase only — wait until E-2 through E-6 close.

5. **Sensitivity flag.** The derivation in §3 loads on P09's *U(1) commutativity*. If a future amendment to P09 weakened the abelian / associative phase structure (e.g., promoted phase to non-abelian Lie group), §3.2 Step 2 and §6.3 Refutation 1 would require re-derivation. This is a known sensitivity, not an active concern; flag only.

---

## 11. Summary

**What this memo accomplished.**

- Stated the CANDIDATE for tensor-product joint composition (§1) and decomposed it into three claims (C1)–(C3).
- Derived (C1) bilinearity-from-bilocal-participation FORCED by P04 + P09 + U2 + ED-I-02 (§3).
- Derived (C2) tensor-product universality FORCED by U2 linear closure + ED-I-02 (SP)-permittance + no-new-primitives (§4).
- Derived (C3) bilinearly-induced inner product FORCED by Born-rule independent-preparation factorization + P09 (§5).
- Audited five alternative joint-space constructions and refuted each on substrate-primitive grounds (§6).
- Issued the gate verdict: **FORM-FORCED** (§7).
- Confirmed acyclicity / no-circularity (§8).
- Provided concrete substrate-level falsifiers for each verdict class (§9).
- Updated the inheritance ledger consequence for Phase-1 Bell–Tsirelson (§10).

**What this memo did not do.**

- Did not derive any of E-2 through E-7. Those are downstream and now structurally unblocked.
- Did not address identical-particle symmetrization (symmetric / antisymmetric subspaces of $\mathcal{H}_A \otimes \mathcal{H}_B$). That is a downstream refinement, not a competing joint-composition rule, and is out of scope for E-1's gate question.
- Did not address operator-algebra / second-quantization joint structures. These are downstream of Phase-1 + Arc Q QFT-extension content; E-1's tensor-product result is the foundation those structures rest on, not a competitor to them.
- Did not address infinite-dim continuum-limit subtleties beyond §4.3's brief note. DCGT supplies the substrate-to-continuum bridge; full continuum-tensor-product analysis is downstream.

**Recommended next steps.**

1. **E-2 (next memo): Generic non-factorizability and density of entangled states.** Now that tensor product is FORM-FORCED, articulate why non-factorizable (entangled) states are dense in $\mathcal{H}_A \otimes \mathcal{H}_B$ and structurally generic rather than exceptional. Expected verdict trivially-FORCED via standard density results in finite-dim and continuity in infinite-dim. File: `arcs/arc-E/E-2_generic_non_factorizability.md`. Estimated 0.5–1 session.

2. **Documentation update for Phase-1 inheritance ledger.** Update the structural-foundations-paper inheritance section to reflect tensor-product composition's new FORCED-via-E-1 status. This propagates to any synthesis-paper revision (Investigation Priority #4) — relevant when that revision occurs but not blocking. ~0.25 session.

3. **Stage E-3 (Schmidt) and E-5 (no-signaling) in parallel.** Both are now expected to close cleanly given E-1 + U2 (E-3) and E-1 + T18 + P11 (E-5). They can be written independently and reviewed together. The substantive derivation work in Arc E concentrates in E-4 (monogamy from cross-chain bandwidth budgets) and E-6 (entropy form), both of which inherit E-1 but require their own primitive-level arguments.

---

**Pause for further instruction.**
