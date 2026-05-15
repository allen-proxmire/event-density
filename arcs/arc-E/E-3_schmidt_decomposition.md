# Arc E — Memo 3: Schmidt Decomposition — Form-FORCED, Values-INHERITED

**Status:** Articulation memo conditional on E-1 (tensor product FORM-FORCED) and E-2 (generic non-factorizability FORCED). No new primitives. Identification-not-derivation discipline observed. Acyclicity audit at §6.

**Date:** 2026-05-08

---

## 1. The CANDIDATE Statement

> **CANDIDATE (E3).** *Every pure bipartite state $|\Psi\rangle \in \mathcal{H}_A \otimes \mathcal{H}_B$ admits a Schmidt decomposition*
> $$|\Psi\rangle = \sum_{i=1}^{r} \sqrt{\lambda_i} \, |i\rangle_A \otimes |i\rangle_B$$
> *with $r \leq \min(d_A, d_B)$ the Schmidt rank, $\{|i\rangle_A\}$ and $\{|i\rangle_B\}$ orthonormal sets in $\mathcal{H}_A$ and $\mathcal{H}_B$ respectively, and $\lambda_i > 0$ with $\sum_i \lambda_i = 1$. The decomposition's structural form is FORCED by E-1 + U2 + T10. The specific values $\{\lambda_i\}$, the Schmidt rank $r$, and the orthonormal bases $\{|i\rangle_A\}, \{|i\rangle_B\}$ are INHERITED from the state $|\Psi\rangle$ and are not substrate-FORCED.*

The CANDIDATE has two distinct claims:

- **(S1) Form claim.** Existence of orthonormal Schmidt bases on each subsystem; non-negativity of coefficients; biorthogonal pairing of basis indices; equality of Schmidt rank as seen from $A$ and from $B$; normalization $\sum_i \lambda_i = 1$.
- **(S2) Inheritance claim.** The values $\{\lambda_i\}$, the Schmidt rank $r$, and the bases are state-specific and INHERITED from $|\Psi\rangle$. The substrate forces *that* a decomposition exists with given form, not *which particular* decomposition any specific state has.

E-3 is expected to be an articulation memo: the mathematical content is the standard SVD / spectral-theorem result, and the substrate-level work is confirming no hidden restriction interferes.

---

## 2. Substrate Inputs (Inheritance)

| Input | Status | Role |
|---|---|---|
| **E-1** (tensor product FORM-FORCED) | Closed (this arc) | Joint state $|\Psi\rangle$ lives in $\mathcal{H}_A \otimes \mathcal{H}_B$ with bilinearly-induced inner product |
| **E-2** (generic non-factorizability FORCED) | Closed (this arc) | Schmidt rank $r > 1$ is generic; $r = 1$ corresponds to the measure-zero Segre variety |
| **U2** (single-endpoint inner-product structure) | FORCED-unconditional | Orthonormal bases exist on each $\mathcal{H}_A, \mathcal{H}_B$ via Gram-Schmidt; spectral theorem applies on each |
| **T10** (Born rule) | FORCED-unconditional | State normalization $\langle\Psi|\Psi\rangle = 1$; $\lambda_i$ as outcome probabilities for a measurement in the Schmidt basis |
| **Standard Hilbert-space mathematics** | Free | Singular value decomposition, spectral theorem, partial trace, polar decomposition |
| **ED-I-02** (single undeveloped participation rule) | Conceptual ground | Substrate reading: Schmidt rank $r$ measures the *degree of undevelopment* of the joint participation rule |
| **ED-I-06** (no fundamental fields) | Canonical guardrail | Forbids field-sourced superselection that could obstruct decomposition |

**No new primitives.** **No use of E-4 (monogamy), E-5 (no-signaling), E-6 (entropy form), or E-7 (synthesis) content.**

---

## 3. Derivation of (S1) via the Reduced Density Operator

### 3.1 Setup in a product basis

Choose any orthonormal bases $\{|m\rangle_A\}_{m=1}^{d_A}$ on $\mathcal{H}_A$ and $\{|n\rangle_B\}_{n=1}^{d_B}$ on $\mathcal{H}_B$ — these exist by U2 + Gram-Schmidt. Any $|\Psi\rangle \in \mathcal{H}_A \otimes \mathcal{H}_B$ expands as

$$|\Psi\rangle = \sum_{m=1}^{d_A} \sum_{n=1}^{d_B} c_{mn} \, |m\rangle_A \otimes |n\rangle_B.$$

Let $C \in \mathbb{C}^{d_A \times d_B}$ denote the coefficient matrix $C_{mn} = c_{mn}$. Normalization (T10) gives $\sum_{mn} |c_{mn}|^2 = \mathrm{Tr}(CC^\dagger) = 1$.

### 3.2 Reduced density operator on $A$

The reduced density operator $\rho_A = \mathrm{Tr}_B(|\Psi\rangle\langle\Psi|)$ has matrix elements

$$(\rho_A)_{mm'} = \sum_n c_{mn} c_{m'n}^* = (CC^\dagger)_{mm'}.$$

Three properties of $\rho_A = CC^\dagger$:

- **Hermitian.** $(CC^\dagger)^\dagger = CC^\dagger$. Always.
- **Positive semi-definite.** $\langle\phi|CC^\dagger|\phi\rangle = \|C^\dagger\phi\|^2 \geq 0$.
- **Trace one.** $\mathrm{Tr}(CC^\dagger) = \sum_{mn}|c_{mn}|^2 = 1$ by T10.

By the spectral theorem (a theorem of standard finite-dim linear algebra applied to U2's complex inner-product structure on $\mathcal{H}_A$), $\rho_A$ has a complete orthonormal eigenbasis $\{|i\rangle_A\}_{i=1}^{d_A}$ with non-negative eigenvalues $\{\lambda_i\}_{i=1}^{d_A}$:

$$\rho_A = \sum_{i=1}^{d_A} \lambda_i \, |i\rangle_A \langle i|_A, \qquad \lambda_i \geq 0, \qquad \sum_i \lambda_i = 1.$$

Let $r$ denote the rank of $\rho_A$ (number of strictly positive eigenvalues). This is the **Schmidt rank**.

### 3.3 Construction of the Schmidt decomposition

Define, for each $i$ with $\lambda_i > 0$,

$$|i\rangle_B := \frac{1}{\sqrt{\lambda_i}} \sum_n \langle i|_A C |n\rangle_B \cdot |n\rangle_B = \frac{1}{\sqrt{\lambda_i}} \langle i|_A \otimes \mathbb{1}_B \, |\Psi\rangle.$$

Direct computation, using orthonormality of $\{|i\rangle_A\}$ as eigenvectors of $\rho_A = CC^\dagger$:

- **Orthonormality on $B$.** $\langle i|_B \, j\rangle_B = \frac{1}{\sqrt{\lambda_i \lambda_j}} \langle\Psi| (|i\rangle_A\langle j|_A \otimes \mathbb{1}_B)|\Psi\rangle = \frac{1}{\sqrt{\lambda_i \lambda_j}} \langle j|_A \rho_A |i\rangle_A = \frac{\lambda_i}{\sqrt{\lambda_i \lambda_j}} \delta_{ij} = \delta_{ij}$.
- **Recovery of $|\Psi\rangle$.** $\sum_i \sqrt{\lambda_i} |i\rangle_A \otimes |i\rangle_B = \sum_i |i\rangle_A \otimes \langle i|_A \otimes \mathbb{1}_B \, |\Psi\rangle = (\sum_i |i\rangle_A\langle i|_A) \otimes \mathbb{1}_B \, |\Psi\rangle = |\Psi\rangle$ since $\{|i\rangle_A\}$ is complete.

Restricting the sum to $i$ with $\lambda_i > 0$ (dropping zero-eigenvalue terms which contribute nothing) gives

$$|\Psi\rangle = \sum_{i=1}^{r} \sqrt{\lambda_i} \, |i\rangle_A \otimes |i\rangle_B$$

with $\{|i\rangle_A\}_{i=1}^{r}$ orthonormal in $\mathcal{H}_A$, $\{|i\rangle_B\}_{i=1}^{r}$ orthonormal in $\mathcal{H}_B$, and $\lambda_i > 0$ with $\sum_i \lambda_i = 1$.

### 3.4 Equality of Schmidt rank from each side

The same construction with $A \leftrightarrow B$ gives $\rho_B = C^\dagger C$. Standard linear algebra: $CC^\dagger$ and $C^\dagger C$ have the same nonzero spectrum (same nonzero eigenvalues with the same multiplicities). So the Schmidt rank is the same whether computed from $\rho_A$ or $\rho_B$, and the same nonzero $\{\lambda_i\}$ appear.

### 3.5 Existence + uniqueness up to degeneracy

The decomposition exists for every $|\Psi\rangle$ (the construction in §3.3 is well-defined whenever $\rho_A$ is well-defined, which is always). It is unique up to:

- **Permutation of indices** (relabeling).
- **Phases on biorthogonal pairs** in non-degenerate sectors: $|i\rangle_A \to e^{i\theta_i}|i\rangle_A$, $|i\rangle_B \to e^{-i\theta_i}|i\rangle_B$ leaves the sum invariant.
- **Unitary mixing within degenerate eigenspaces** of $\rho_A$ (i.e., when several $\lambda_i$ coincide).

The values $\{\lambda_i\}$ themselves are uniquely determined (as the eigenvalues of $\rho_A$).

**(S1) is FORCED** as a structural theorem of the algebra established by E-1 + U2 + T10. No additional substrate input enters the construction.

---

## 4. Derivation of (S2): Values-INHERITED

### 4.1 The values are state-determined

The Schmidt rank $r$ and the eigenvalues $\{\lambda_i\}$ are fully determined by $\rho_A = CC^\dagger$, which is fully determined by the coefficient matrix $C$, which is fully determined by the state $|\Psi\rangle$ in any chosen product basis. There is no substrate input that picks $r$ or $\{\lambda_i\}$ independently of $|\Psi\rangle$.

The Schmidt bases $\{|i\rangle_A\}$ and $\{|i\rangle_B\}$ are also state-determined (eigenbases of the state-specific $\rho_A$ and $\rho_B$).

### 4.2 What "value-INHERITED" means here

In the form-FORCED / value-INHERITED framework used in earlier closed arcs:

- **U4** (kinetic energy form $\hat{H} = \hat{p}^2/(2m)$): the form is FORCED by Galilean Lie algebra; the value $m$ is INHERITED per Arc M.
- **BH-5** (entropy area-law): the form $S \propto A$ is FORCED; the coefficient is INHERITED.
- **T19** (Newton's $G$): the relationship $G = c^3 \ell_P^2 / \hbar$ is FORCED; the values $c, \ell_P, \hbar$ are INHERITED from the substrate.

For E-3:

- The form *of the decomposition* (orthonormal biorthogonal pairs, non-negative coefficients, normalized to one, Schmidt rank well-defined) is FORCED by E-1 + U2 + T10.
- The *specific values* of $\{\lambda_i\}, r, \{|i\rangle_A\}, \{|i\rangle_B\}$ are INHERITED from the state $|\Psi\rangle$, which is itself a substrate object whose specifics depend on substrate history (preparation, interaction, partial individuation).

This is exactly the canonical form-FORCED-values-INHERITED pattern.

**(S2) is FORCED** (i.e., the inheritance claim is structurally correct: there is no substrate mechanism that picks values independent of the state).

---

## 5. Substrate Audit

### 5.1 ED-I-02 reading

ED-I-02 says entanglement is the persistence of a single undeveloped participation rule expressed at multiple endpoints. The Schmidt rank $r$ is the substrate-natural measure of *how undeveloped* that rule is:

- **Schmidt rank $r = 1$** (product state): one rule with Schmidt-coefficient 1, no shared structure beyond a single product configuration. This corresponds to (IP) — independent preparation; the "rule" is fully decomposed into separate single-endpoint rules.
- **Schmidt rank $r > 1$** (entangled state): one rule with multiple shared structural channels. The number of nonzero $\lambda_i$ is the count of substrate-shared participation channels between the two endpoints.
- **Schmidt rank $r = \min(d_A, d_B)$ with all $\lambda_i$ equal** (maximally entangled): the rule is *maximally undeveloped* — no preferential shared channel; all substrate-shared structure is uniformly distributed across the available joint dimension.

This substrate reading is exactly what ED-I-02 §3.4 ("one participation rule, two locations") and §4 ("perfect correlations because not yet differentiated") describe at the qualitative level. Schmidt decomposition is the formal mathematical statement of that ontology.

The Schmidt coefficients $\sqrt{\lambda_i}$ are substrate-natural: they encode the *amplitude weight* of each shared channel in the undeveloped rule. By T10, $\lambda_i$ is the probability of finding outcome $|i\rangle_A$ on a measurement of $A$ in the Schmidt basis; by ED-I-02 §6, this is the probability of forced individuation along channel $i$ when measurement injects ED.

### 5.2 No superselection obstructs the decomposition

A substrate-level superselection rule that obstructed Schmidt decomposition would have to either (a) restrict the joint Hilbert space such that some $|\Psi\rangle$ has no well-defined $\rho_A$, or (b) restrict the eigenbasis of $\rho_A$ in a way that violates the spectral theorem. Both contradict E-1 (tensor product FORM-FORCED, with $\rho_A$ well-defined as partial trace) + U2 (spectral theorem applies on $\mathcal{H}_A$).

ED-I-06's no-fundamental-fields guardrail forbids a field-sourced superselection rule. The closed-arc audit (E-2 §4.3) confirms no inherited substrate-level joint-space restriction.

### 5.3 No conditionality from the rank issue

When $d_A \neq d_B$, the Schmidt rank is bounded by $\min(d_A, d_B)$. This is not a substrate restriction; it is a structural feature of the dimensions $d_A, d_B$ themselves, which are INHERITED from the substrate single-endpoint state-space dimensions. No separate substrate input picks Schmidt rank.

---

## 6. Verdict

> **VERDICT (E3): FORM-FORCED, VALUES-INHERITED.**
>
> Every pure bipartite state $|\Psi\rangle \in \mathcal{H}_A \otimes \mathcal{H}_B$ admits a Schmidt decomposition. The structural form (orthonormal biorthogonal bases on each side, non-negative coefficients summing to one, equality of Schmidt rank from either side, well-definedness of Schmidt rank) is FORCED by E-1 + U2 + T10 via standard SVD / spectral-theorem mathematics. The specific values $\{\lambda_i\}$, the Schmidt rank $r$, and the bases $\{|i\rangle_A\}, \{|i\rangle_B\}$ are INHERITED from the state $|\Psi\rangle$, in the canonical form-FORCED-values-INHERITED pattern shared with U4, BH-5, T19. Substrate audit confirms ED-I-02 reading is consistent and indeed sharpens (Schmidt rank measures degree of undevelopment); ED-I-06 forbids any superselection that could obstruct.

**Verdict-class details:**

- **No CONDITIONAL caveat survived the audit.** Continuum extension is downstream of DCGT; identical-particle symmetrization is a downstream sub-space restriction, not a competing decomposition.
- **No NOT-FORCED option survived.** No substrate construction obstructs the decomposition.
- **No new active CANDIDATEs.** Active CANDIDATE inventory remains {}.

---

## 7. Circularity Audit

| Potential circularity | Audit verdict |
|---|---|
| E-4 (monogamy) used as derivation premise? | **No.** Not invoked. |
| E-5 (no-signaling) used as derivation premise? | **No.** §3 uses the partial trace $\rho_A = \mathrm{Tr}_B(|\Psi\rangle\langle\Psi|)$ as a mathematical object, not as a no-signaling theorem. |
| E-6 (entropy form) used as derivation premise? | **No.** Schmidt coefficients $\{\lambda_i\}$ feed into entanglement-entropy $S = -\sum \lambda_i \log \lambda_i$ in E-6, but E-3 does not invoke any entropy structure. |
| E-7 (synthesis) used as derivation premise? | **No.** Not invoked. |
| Self-reference of E-3 within itself? | **No.** §3 → §4 → §5 → §6 derivation chain is acyclic. |
| E-1 and E-2 used only as inputs, not as conclusions? | **Confirmed.** E-1 supplies the joint Hilbert space; E-2 supplies the substrate reading of Schmidt-rank-$r$-vs-$r=1$ as generic-vs-exceptional. Neither is re-derived. |
| Bell–Tsirelson used as derivation premise? | **No.** Bell–Tsirelson is identified later as observable-side cross-link to maximally-entangled-state Schmidt structure, but does not appear in §3–§5. |

**Acyclicity confirmed.**

---

## 8. Falsification

### 8.1 Falsifier for FORM-FORCED, VALUES-INHERITED verdict (current verdict)

A substrate construction satisfying E-1 + U2 + T10, in which:

- (a) some pure $|\Psi\rangle \in \mathcal{H}_A \otimes \mathcal{H}_B$ has no Schmidt decomposition (fails (S1)) — would require failure of the spectral theorem on the substrate-derived $\mathcal{H}_A$, contradicting U2; or
- (b) the values $\{\lambda_i\}$ are substrate-FORCED to some specific spectrum independent of $|\Psi\rangle$ (fails (S2)) — would require the substrate to specify state-independent $\lambda_i$, which contradicts the state-determined nature of $\rho_A$.

Neither is mathematically possible given the inputs.

### 8.2 Falsifier for CONDITIONAL verdict (rejected)

An auxiliary assumption beyond E-1 + U2 + T10 + standard Hilbert-space mathematics that is required for the decomposition. The audit identified none. (Continuum extension is downstream of DCGT, not auxiliary.)

### 8.3 Falsifier for NOT-FORCED verdict (rejected)

A substrate-level superselection rule that obstructs the decomposition for some states. Refuted by E-1 §6.4 + ED-I-06 + closed-arc audit.

### 8.4 Empirical-side falsifier

Any experimental observation of bipartite-state correlations inconsistent with a density operator on $\mathcal{H}_A \otimes \mathcal{H}_B$ admitting spectral decomposition (e.g., observed reduced state with non-real or negative "eigenvalues"). Such observations would refute Schmidt decomposition's empirical correctness; none are reported.

---

## 9. Consequences for the Arc

1. **E-3 closes cleanly as articulation memo.** Schmidt decomposition is FORM-FORCED, VALUES-INHERITED. Downstream Arc E memos may invoke Schmidt decomposition as a substrate-derived theorem.

2. **The substrate reading of Schmidt rank as "degree of undevelopment of the participation rule"** sharpens ED-I-02 §3 conceptually. The qualitative claim "single undeveloped participation rule" is now formally articulated as: the Schmidt rank counts the substrate-shared participation channels, and the Schmidt coefficients $\sqrt{\lambda_i}$ weight them. This sharpening is useful for E-6 (entropy as the substrate measure of undevelopment) and E-7 (synthesis with BH-4 entanglement-straddling, where straddling occurs via the same shared-channel structure).

3. **E-6 (entropy form) is now structurally enabled.** Once the Schmidt eigenvalues $\{\lambda_i\}$ are in hand as the spectrum of $\rho_A$, the Shannon-Khinchin axioms applied at the substrate level produce the von Neumann entanglement entropy $S(\rho_A) = -\sum_i \lambda_i \log \lambda_i$. E-6 is the substantive derivation that does this work.

4. **E-4 (monogamy) is still independent of E-3 at the structural level.** Monogamy loads on cross-chain bandwidth budgets (Q-COMPUTE / DCGT / BH-2), not on Schmidt structure per se. E-3 and E-4 may close in either order.

5. **No new active CANDIDATEs.** Active CANDIDATE inventory remains {}.

6. **No new sensitivity flags.** E-3 inherits E-1 + U2 load-bearings without adding new ones.

---

## 10. Summary

**What this memo accomplished.**

- Stated the E-3 CANDIDATE (§1), decomposed it into (S1) form claim and (S2) inheritance claim.
- Derived Schmidt decomposition from $\rho_A = \mathrm{Tr}_B(|\Psi\rangle\langle\Psi|) = CC^\dagger$ via spectral theorem on U2's inner-product structure, with biorthogonal pairing constructed explicitly (§3).
- Confirmed Schmidt-rank equality from either side via $CC^\dagger$ vs $C^\dagger C$ same-nonzero-spectrum (§3.4).
- Articulated the value-INHERITED claim via the canonical form-FORCED-values-INHERITED framework (§4), placing E-3 alongside U4, BH-5, T19.
- Substrate-audited (§5): ED-I-02 reading actually sharpens to "Schmidt rank = degree of undevelopment, Schmidt coefficients = amplitude weights of shared channels"; ED-I-06 forbids obstructing superselection.
- Issued the verdict: **FORM-FORCED, VALUES-INHERITED** (§6).
- Confirmed acyclicity (§7) and provided substrate-level falsifiers (§8).

**What this memo did not do.**

- Did not derive entanglement entropy $S = -\sum_i \lambda_i \log \lambda_i$ — that is E-6's deliverable.
- Did not derive monogamy — that is E-4's deliverable.
- Did not address mixed-state Schmidt structure (operator-Schmidt decomposition, Hilbert–Schmidt decomposition of operators on $\mathcal{H}_A \otimes \mathcal{H}_B$). This is downstream content; if relevant for E-7 it can be added then.
- Did not address infinite-dimensional Schmidt subtleties beyond noting DCGT supplies the substrate-to-continuum bridge.
- Did not address gauge-invariance or symmetry-restricted Schmidt decompositions (relevant in QFT contexts via Arc Q's T17, but not load-bearing for Arc E's gate-and-foundations memos).

**Recommended next steps.**

1. **E-5 (next memo): No-signaling from V1 retardation + P11.** Now that partial trace and reduced density operator are formally articulated (§3.2), the partial-trace-independence-under-measurement-basis-change argument can be made rigorously. Substrate inputs: T18 (forward-cone-only V1 kernel correlations) + P11 (commitment irreversibility) + E-1 + E-3. Expected verdict: FORCED. Estimated 0.5–1 session.

2. **(Defer to substantive-derivation phase) E-4 (monogamy from cross-chain bandwidth).** The first substantive derivation memo of Arc E. Loads on Q-COMPUTE Memo 1's $\Gamma_\mathrm{cross}$ structure, BH-2's decoupling-surface bandwidth, and DCGT's hydrodynamic-window scale separation. Expected to require 1–2 sessions.

3. **(Defer to substantive-derivation phase) E-6 (entropy form).** Now structurally enabled by E-3 (Schmidt eigenvalues in hand). Will derive von Neumann form via Shannon-Khinchin substrate-counting + ED-I-01 multiplicity-as-entropy reading. Expected verdict form-FORCED-coefficient-INHERITED, parallel to BH-5. Estimated 1–2 sessions.

4. **(Documentation) Phase-1 inheritance ledger update.** With E-1 + E-2 + E-3 closed, the Bell–Tsirelson 2√2 inheritance can now be tightened with explicit pointers to the Schmidt structure of maximally-entangled states (where CHSH saturates 2√2). This is documentation, not new derivation.

---

**Pause for further instruction.**
