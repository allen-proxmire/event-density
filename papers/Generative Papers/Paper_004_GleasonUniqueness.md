# Paper_004 — Gleason-Type Uniqueness from P07 + P08 (Partial Result)

**Series:** Event Density (ED) Generative Papers — Wave-2 QM-kinematics arc
**Author:** Allen Proxmire
**Status:** Publication draft (attempts substrate-level Gleason; partial result)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/qm-kinematics/Paper_004_GleasonUniqueness.md`
**Genre:** Conditional structural attempt within the 13-Primitive Generative System.

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 primitives are not derived** (Paper_087).
2. **No claim that standard Gleason's theorem is reproduced.** Standard Gleason (Gleason 1957) operates on closed subspaces of Hilbert space with dim ≥ 3 and assumes the inner-product structure. This paper attempts a substrate-level *analog* whose inputs are P07 + P08 + paper-specific postulates.
3. **The result is a partial success.** Under additional substrate-level postulates (P-Channel-Orthogonality, P-Gleason-Compatibility, §2), the inner-product form is determined up to overall normalization. **Without those postulates, the standard substrate-derivation of the inner product from P07 + P08 alone does not close.** This paper is honest about the obstruction.
4. **The Paper_007 inner-product I→D relabel is *conditional* on the additional postulates.** Under P-Channel-Orthogonality + P-Gleason-Compatibility, the inner product is substrate-derived (D). Without those, it remains I (Paper #3 inheritance). The choice between "relabel I → D under added postulates" vs. "keep I" is a substrate-level commitment about how much postulational scaffolding to accept.
5. **No claim of full Gleason proof at the substrate level.** The substrate-level Gleason-type result is **structural in form** but **requires the two paper-specific postulates** to close. Whether those postulates can themselves be derived from canonical 13 is open.
6. **No claim that the obstruction is fundamental.** The obstruction may be removable by future substrate analysis identifying an additional canonical-13-derivable structural constraint.

---

## Abstract

This paper attempts the **substrate-level Gleason-type uniqueness result** for the sesquilinear inner product on Paper_001 pre-individuation amplitudes. The attempt is **partially successful**: under two paper-specific postulates — **P-Channel-Orthogonality** (substrate-level channel basis is orthogonal in the inner-product structure) and **P-Gleason-Compatibility** (a Gleason-analog non-contextuality condition on substrate-level probability assignments) — the inner product $\langle\Psi|\Phi\rangle = \sum_K \overline{\Psi_K}\,\Phi_K$ is determined up to overall normalization. Without these postulates, the standard derivation from P07 + P08 alone does not close. The result is **honest about the obstruction**: closure requires additional substrate-level commitments beyond the canonical 13.

**Impact on Paper_007:** the inner-product row in Paper_007's §2.5 audit (currently labeled I via Paper #3 inheritance) can be **conditionally relabeled to D** — but only under the two new postulates. The substrate-framework user must choose between (a) accepting the two added postulates and relabeling I → D, or (b) keeping the inner-product structure I-inherited from Paper #3. Neither is mandatory; both are substrate-consistent. This paper's structural contribution is to **make the choice explicit** rather than hide the dependency.

The paper makes no claim of full Gleason proof at substrate level, no claim that the two added postulates are derivable from canonical 13 (structurally open), and no claim that the substrate-level Gleason-type result reproduces all standard Gleason content (this paper restricts to inner-product form; full closed-subspace probability measure assignment is downstream).

---

## 1. Introduction

### 1.1 What this paper does

This paper attempts the **substrate-level Gleason-type uniqueness theorem** for the sesquilinear inner product structure inherited in Paper_007 from Paper #3. Paper_007's forward-pointer named Paper_004 as the candidate that would relabel the inner-product row I → D. This paper delivers the **attempted derivation** and reports the result honestly.

### 1.2 What standard Gleason does

Standard Gleason's theorem (Gleason 1957): on a Hilbert space $\mathcal{H}$ with $\dim \mathcal{H} \geq 3$, any probability measure on closed subspaces of $\mathcal{H}$ is given by $P(\mathcal{S}) = \mathrm{Tr}(\rho\,\Pi_{\mathcal{S}})$ for some density matrix $\rho$. This essentially uniquely determines the Born rule structure (up to choice of $\rho$).

Standard Gleason **takes the Hilbert-space structure (and the inner product) as given**. ED's analog asks: can the substrate-level inner-product structure be derived rather than inherited?

### 1.3 The honest verdict

**Yes, under additional postulates.** No, not from P07 + P08 alone. The two needed postulates (P-Channel-Orthogonality, P-Gleason-Compatibility) are themselves substrate-level commitments; whether they reduce to canonical 13 is open.

### 1.4 Arc context

- **Paper_001:** pre-individuation amplitudes (upstream).
- **Paper_003:** Born rule from participation-frequency limit.
- **Paper_004 (this paper):** Gleason-type uniqueness attempt.
- **Paper_007:** Hilbert-space emergence; inner-product row potentially relabeled by this paper.

---

## 2. Primitive Inputs

**Substrate primitives (postulated, Paper_087):** P07 (channel structure), P08 (substrate scale), P02 (participation), P04 (bandwidth).

**Upstream paper dependencies:** Paper_087, Paper_001 (pre-individuation amplitudes), Paper_003 (Born rule via P-LinRate), Paper_007 (Hilbert-space emergence).

**Paper-specific postulates (new):**

- **P-Channel-Orthogonality:** *Distinct substrate channels $K \neq L$ are orthogonal in the substrate-level inner-product structure: $\langle K | L \rangle = \delta_{KL}$.* Substrate-level structural commitment going beyond P07 (P07 distinguishes channels but does not assert orthogonality). The orthogonality is an additional substrate-level commitment about how distinct channels relate in the substrate-amplitude space.

- **P-Gleason-Compatibility:** *Substrate-level probability assignments to channel-decompositions are non-contextual: the probability of outcome $K$ in any substrate-channel-decomposition containing $K$ depends only on $K$'s substrate amplitude content, not on the rest of the decomposition.* Substrate-level analog of Gleason's non-contextuality assumption.

**Empirical / value-layer inputs:** none required.

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| Pre-individuation amplitudes $P_K^C$ | D | Paper_001 |
| Channel basis $\{|K\rangle\}$ from P07 | P | Paper_087 §5.7 |
| Distinct channels orthogonal $\langle K|L\rangle = \delta_{KL}$ | **P (P-Channel-Orthogonality)** | §2 substrate-level commitment beyond P07; orthogonality is added structural content |
| Substrate probability non-contextuality | **P (P-Gleason-Compatibility)** | §2 Gleason-analog substrate-level commitment |
| Inner-product form determined up to normalization | **D conditional on P-Channel-Orthogonality + P-Gleason-Compatibility** | §3.2 — under both postulates, sesquilinear inner product is structurally determined via standard-linear-algebra composition (polarization-identity + Born-rule). Explicit sub-row below for the standard-math step. |
| Standard-math step (polarization identity / Born-rule composition) | **I (standard linear algebra)** | §3.2 step 3 — the bilinearity + complex-linearity composition producing the sesquilinear form is standard linear algebra, not substrate-derived. The substrate-level content is the two postulates; the construction of the inner-product form is inherited mathematical machinery. *(Round-7 sub-row added.)* |
| Standard Gleason theorem (closed subspaces, $\dim \geq 3$) | NOT CLAIMED | preamble item 5 |
| Paper_007 inner-product row I → D | **conditional relabel** | conditional on accepting two added postulates |
| Two added postulates derivable from canonical 13 | NOT CLAIMED | §3.4 obstruction discussion |

All rows P, D, or labeled. **No A (asserted) rows.**

---

## 3. The Substrate-Level Gleason-Type Attempt

### 3.1 Setup

Paper_001 supplies pre-individuation amplitude content $\Psi^C = \sum_K P_K^C |K\rangle$ with $P_K^C = \sqrt{b_K^C}\,e^{i\pi_K^C}$. Paper_003 supplies the Born-rule frequency limit $f_K = b_K/\sum b_{K'}$. The question: can the **sesquilinear inner product** $\langle\Psi|\Phi\rangle = \sum_K \overline{\Psi_K}\,\Phi_K$ be derived?

### 3.2 Under the two added postulates

**Given P-Channel-Orthogonality:** $\langle K|L\rangle = \delta_{KL}$ for distinct channels.

**Given P-Gleason-Compatibility:** substrate-level probability assignment $P(K)$ for outcome $K$ depends only on the substrate-amplitude content $P_K$ at channel $K$, not on the rest of the decomposition.

**Derivation steps:**

1. **From P-Channel-Orthogonality + bilinearity:** for any state $\Psi = \sum_K P_K |K\rangle$:
$$
\langle\Psi|\Psi\rangle = \sum_{K, L} \overline{P_K}\,P_L\,\langle K|L\rangle = \sum_K |P_K|^2.
$$

2. **From P-Gleason-Compatibility + Paper_003 Born rule:** $P(K) = b_K$ in normalized state. By the Paper_001 identification $b_K = |P_K|^2$:
$$
P(K) = |P_K|^2 = |\langle K|\Psi\rangle|^2.
$$

3. **From bilinearity + complex-linearity (definitional construction matching standard sesquilinear inner-product form):** $\langle\Psi|\Phi\rangle = \sum_K \overline{P_K^\Psi}\,P_K^\Phi$ — sesquilinear inner product.

**Honest framing (round-7):** step 3 is a **definitional construction matching the standard sesquilinear inner-product form** from the two postulates (P-Channel-Orthogonality giving orthonormality, P-Gleason-Compatibility giving non-contextuality). The derivation produces the standard form **by construction from the two postulates**, not by a uniqueness theorem proving "only this form is consistent." Under different postulates (e.g., real-symmetric inner product alternative), a different inner-product form would be similarly constructed.

**Result:** under the two postulates, the sesquilinear inner-product form $\langle\Psi|\Phi\rangle = \sum_K \overline{\Psi_K}\,\Phi_K$ is **constructed** to match standard QM. The substrate-level content is the two postulates; the inner-product form follows definitionally.

### 3.3 The conditional relabel for Paper_007

Under P-Channel-Orthogonality + P-Gleason-Compatibility, Paper_007's inner-product row (currently I via Paper #3) can be **conditionally relabeled to D** — derived from canonical 13 + Paper_001 + Paper_003 + the two added postulates.

**The user's choice:**
- (a) Accept the two added postulates → relabel Paper_007 inner-product row from I → D.
- (b) Keep Paper_007's inner-product row as I (Paper #3 inheritance).

Both are substrate-consistent. Option (a) reduces the corpus's external inheritance count by one (Paper #3 inner product) at the cost of adding two paper-specific postulates. Option (b) keeps the external inheritance but avoids the added postulates.

**This paper's recommendation:** label the relabel as **conditional** and let downstream papers / future analysis determine whether to accept the trade.

### 3.4 The obstruction — why P07 + P08 alone do not close

Without P-Channel-Orthogonality: distinct channels $|K\rangle, |L\rangle$ in the motif-algebra could have non-trivial overlap, breaking the basis structure on which the sesquilinear inner product is defined. P07 distinguishes channels but does not force orthogonality.

Without P-Gleason-Compatibility: substrate-level probability assignments could in principle be context-dependent, allowing different inner-product structures consistent with Paper_003's frequency limit.

The two postulates close these gaps. **The structural question** is whether canonical 13 + Paper_001 already imply both — i.e., whether P-Channel-Orthogonality and P-Gleason-Compatibility are *derivable* from substrate primitives.

**Open structural conjectures (round-7 framing: these are conjectures, not partial derivations):**

- **Conjecture 1:** P-Channel-Orthogonality may follow from P07's "structurally distinguishable" requirement applied at the inner-product level. **This is a conjecture, not a partial derivation.** P07 distinguishes channels operationally but does not, by itself, force orthonormality in the inner-product structure. A substrate-level argument linking P07 distinguishability to inner-product orthogonality is **not supplied** in this paper.

- **Conjecture 2:** P-Gleason-Compatibility may follow from P03 spatial-homogeneity + P11 commitment-irreversibility. **Conjecture, not partial derivation.** The substrate-level argument linking spatial-homogeneity + commitment-irreversibility to substrate-probability non-contextuality is **not supplied** in this paper.

**Both conjectures are open structural questions, not progress toward closure.** Calling them "tentative analysis" would be too generous — they are **open conjectures**. This paper makes no claim that either is provable from canonical 13 alone; both are explicitly open. Future substrate-level analysis could either close them (converting P-Channel-Orthogonality and P-Gleason-Compatibility to theorems) or refute them (forcing those postulates to remain substrate-level commitments).

**Honest verdict (round-7):** the substrate-level Gleason-type result requires two paper-specific postulates as substrate-level commitments. The conjectures sketched above are **open structural questions**, not partial-derivation progress.

---

## 4. Falsification Criteria

### 4.1 Channel non-orthogonality observed

**Falsifier sentence:** *Empirical demonstration that distinct substrate channels have non-trivial inner-product overlap — i.e., $\langle K|L\rangle \neq 0$ for $K \neq L$ in some substrate-level regime — would falsify P-Channel-Orthogonality and break the substrate-level inner-product derivation.*

### 4.2 Substrate probability contextuality

**Falsifier sentence:** *Empirical demonstration of substrate-level probability assignments that depend on channel-decomposition context (beyond what's in the substrate amplitude $P_K$) would falsify P-Gleason-Compatibility.*

### 4.3 Standard Gleason fails to recover under substrate completion

**Falsifier sentence:** *Demonstration that the substrate-level inner-product (under the two postulates) fails to recover standard Gleason's theorem in the Hilbert-space completion (Paper_007) — e.g., produces a non-standard probability measure on closed subspaces — would falsify the substrate-Gleason analog.*

### 4.4 Added postulates derivable from canonical 13

**Falsifier sentence (refinement):** *Demonstration that P-Channel-Orthogonality + P-Gleason-Compatibility are derivable from canonical 13 alone would strengthen this paper to a full substrate-derivation of the inner product, relabeling §2's postulates to derived results.*

---

## 5. Position Statement

**The substrate-level Gleason-type uniqueness result is partially achieved.** Under P-Channel-Orthogonality + P-Gleason-Compatibility, the sesquilinear inner-product form on Paper_001 pre-individuation amplitudes is structurally determined. Without these two postulates, the derivation from P07 + P08 alone does not close.

**For Paper_007's inner-product row:** conditional I → D relabel available under the two postulates; otherwise I retained.

What this paper claims:

- The substrate-level Gleason-type structural form is determined under two paper-specific postulates.
- Paper_007's inner-product row can be conditionally relabeled I → D under those postulates.
- The choice between accepting added postulates (and reducing external inheritance) vs. keeping inheritance is explicit, not hidden.

What this paper does *not* claim:

- Standard Gleason's theorem is not reproduced.
- The two added postulates are not derivable from canonical 13 alone (open).
- Full closure of substrate-level inner-product derivation from primitives alone is not achieved.

**Series context.** Paper_004 of QM-kinematics arc. Forward-cited from Paper_007 §3.2 forward-pointer. Outcome: partial result; honest about obstruction.

---

## Appendix: Cross-References and Glossary

**Cross-references:** Paper_087, Paper_001, Paper_003, Paper_007, Paper #3 (inner product + Tsirelson).

**Glossary:**
- **Gleason-type substrate result.** Substrate-level analog of standard Gleason's theorem.
- **P-Channel-Orthogonality.** Distinct substrate channels orthogonal in inner-product structure.
- **P-Gleason-Compatibility.** Substrate-level probability non-contextuality.
- **Conditional I → D relabel.** Paper_007's inner-product row reclassification, conditional on accepting added postulates.

---

**End of Paper_004.**
