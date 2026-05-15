# Paper 008 — Phase Structure on Rule-Types from P09 + P10 — FIXED

**Series:** Wave-2 Generative Papers (Foundations, Phase Structure)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087 canonical enumeration) + paper-specific postulates declared in §2.

**FIXED notes (2026-05-13):**
- Primitive enumeration aligned with Paper_087: P09 (U(1)-valued polarity) supplies the native angular structure; P10 (Rule-type primitive) supplies discrete rule-types and their composition. Legacy "P05 rule-type individuation / P06 composition closure" framing replaced.
- Paper scope clarified: P09 supplies per-channel $U(1)$ polarity natively; this paper's content is the **propagation of phase structure to rule-types** under P10 composition (downstream of P09's canonical $U(1)$ assignment).
- "Flexibility & Correction Block" deleted; revision triggers folded into §6.

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim to derive the **value** of phase (e.g., $\hbar$-normalized units) from first principles; only the **structural existence** of phase variables on rule-types.
2. It does **not** claim that phase is observable independently of context.
3. It does **not** claim novel empirical content beyond what is already implied by P09 + P10.
4. It does **not** claim that phase periodicity on rule-types is unique; only that $2\pi$ periodicity is **forced** given the declared postulates.
5. It does **not** introduce new substrate primitives.
6. "Phase structure on rule-types" means: $U(1)$-valued/$S^1$-valued internal variable carried by each rule-type, descended from P09's per-channel polarity via P10 composition.
7. This paper supplies the structural origin of the rule-type-level $U(1)$ phase used by T17 (Paper_015), Born-Gleason (Paper_002), V1 kernel (Paper_089), Aharonov-Bohm walkthrough, and Berry-phase walkthrough.

---

## Abstract

P09 ($U(1)$-valued polarity, per Paper_087 canonical enumeration) supplies the substrate's native angular structure: each channel carries $U(1)$-valued polarity. P10 (Rule-type primitive) supplies discrete rule-types and their composition operation. We show that the rule-type-level phase structure — the $U(1)$ phase carried by each rule-type as an internal degree of freedom — is **FORM-FORCED** by P09 + P10 + three declared postulates: P-Composition-Cyclic (composition has cyclic substructure), P-Cyclic-Continuum (continuum limit preserves cyclic structure), P-Normalization (circumference $2\pi$, conventional). The structural form is FORCED; the numerical normalization is INHERITED.

---

## §1 Introduction

Phase structure is load-bearing in:

- Born–Gleason rule on complex Hilbert space (Paper_002).
- Aharonov–Bohm phase walkthrough.
- T17 gauge fields = $U(1)$ / non-Abelian rule-type bundles (Paper_015).
- V1 kernel complex-amplitude propagation (Paper_089).
- Berry-phase walkthrough.

P09 of Paper_087 supplies $U(1)$ polarity natively at the **channel** level. This paper traces the **rule-type-level** phase to P09 + P10 composition, closing the foundational question of how channel-level $U(1)$ polarity becomes rule-type-level phase under composition.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087 canonical enumeration)

- **P07 (Channel structure)** — supplies the per-channel substrate on which P09 polarity is defined.
- **P09 ($U(1)$-valued polarity)** — supplies the channel-level $U(1)$ angular structure natively.
- **P10 (Rule-type primitive)** — supplies discrete rule-types and their composition operation.

### 2.2 Inherited closed-arc results

- **I-DCGT:** Diffusion Coarse-Graining Theorem (Paper_073) — continuum limit of discrete substrate structures.

### 2.3 Paper-specific postulates

- **P-Composition-Cyclic:** The P10 composition operation on the rule-type set $R$ admits at least one cyclic substructure of order $n \geq 2$: there exists a rule-type $r \in R$ and integer $n \geq 2$ with $r^{\circ n} = e$ and $r^{\circ k} \neq e$ for $0 < k < n$.
- **P-Cyclic-Continuum:** The cyclic substructure passes to a continuous cyclic group $S^1$ in the continuum limit (under I-DCGT).
- **P-Normalization:** The continuum cyclic group is normalized to circumference $2\pi$. (Conventional.)

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P09 supplies channel-level $U(1)$ polarity | I-P | Primitive (Paper_087). |
| 2 | P10 supplies rule-types and composition | I-P | Primitive (Paper_087). |
| 3 | Discrete rule-type set $R$ with $\circ : R \times R \to R$ | I | From P10. |
| 4 | Existence of cyclic substructure under $\circ$ | P-Composition-Cyclic | Postulate. |
| 5 | Cyclic substructure has order $n \geq 2$ | P | From P-Composition-Cyclic. |
| 6 | Channel-level $U(1)$ propagates to rule-types via P10 composition | D | Application of P09 + P10. |
| 7 | Continuum limit produces $S^1$ on rule-types | P-Cyclic-Continuum + I-DCGT | Postulate + inheritance. |
| 8 | Normalization to $2\pi$ | P-Normalization | Conventional. |
| 9 | Phase variable $\theta \in S^1$ on rule-types | D | From step 6 + step 7. |
| 10 | $U(1)$-valued internal variable structure | D | Composite. |

No structural-analogy mislabel.

---

## §3 The Argument

### 3.1 Channel-level $U(1)$ from P09

P09 declares that each channel carries $U(1)$-valued polarity. This is **native to the substrate ontology** — it is not derived from a deeper structure in this paper.

### 3.2 Rule-types from P10

P10 supplies discrete rule-types $R$ with composition $\circ : R \times R \to R$.

### 3.3 Why P-Composition-Cyclic is needed

P10 alone permits a free monoid structure on $R$ (no cyclic relations). For rule-types to carry the channel-level $U(1)$ as an internal phase variable, the composition operation must support cyclic substructure compatible with $U(1)$'s additive-mod-$2\pi$ structure.

P-Composition-Cyclic declares this feature explicitly. It is the **load-bearing additional structural fact**.

### 3.4 Channel-$U(1)$ propagates to rule-types

Under P-Composition-Cyclic + P09, the channel-level $U(1)$ polarity descends to rule-type-level phase: each rule-type carries a $U(1)$-valued phase variable inherited from the channel polarities it composes from.

### 3.5 Continuum limit

Under DCGT (P-Cyclic-Continuum), the discrete cyclic substructure $\mathbb{Z}/n$ on rule-types passes to continuous $S^1 = U(1)$.

### 3.6 Normalization

Circumference $2\pi$ by convention (P-Normalization).

---

## §4 Connection to Phase Phenomena

Once rule-type $S^1$ phase is in place:

- **Aharonov–Bohm:** Phase accumulation around closed loops on $U(1)$ rule-type bundle.
- **Berry phase:** Geometric phase from $S^1$-bundle holonomy.
- **Born–Gleason:** $|\psi|^2$ rule on complex Hilbert space requires $S^1$ phase.
- **T17 gauge fields:** $U(1)$ rule-type bundle is the simplest example.
- **V1 kernel:** Complex-amplitude propagation uses $S^1$ phase rotation.

This paper supplies the substrate-level $S^1$ structure that all of the above **use**.

---

## §5 Why $2\pi$ Specifically?

$2\pi$ is **conventional**:

- Mathematical convention: $U(1) = \{e^{i\theta} : \theta \in [0, 2\pi)\}$ standard.
- Empirical normalization: Aharonov–Bohm flux quantum measured at $2\pi$ in standard $\hbar$-units.

P-Normalization is inherited.

---

## §6 Open Structural Questions

- **O-Phase-1:** Derivation of P-Composition-Cyclic from a deeper closure property of P10.
- **O-Phase-2:** Multiplicity of $S^1$ structures — per-rule-type or shared?
- **O-Phase-3:** Connection to spin (half-integer vs integer phase).
- **O-Phase-4:** Substrate origin of $2\pi$ normalization beyond convention.

**Revision triggers:**
- If P-Composition-Cyclic is derived (O-Phase-1), §3.3 strengthens to D-only.
- If P-Cyclic-Continuum is derived from DCGT extensions, §3.5 strengthens.
- If P-Normalization is replaced by a derived value, §5 strengthens.

---

## §7 Falsification Criteria

- **F1:** P10 admits closed-composition structure with no cyclic substructure — refutes P-Composition-Cyclic's necessity.
- **F2:** Empirical detection of internal phase variable with periodicity $\neq 2\pi n$.
- **F3:** Continuum limit of cyclic substructure yields non-$S^1$ topology — refutes P-Cyclic-Continuum.
- **F4:** Phase structure used in T17, AB, Berry, Born–Gleason not derivable from this paper's $S^1$.

---

## §8 Position Statement

Rule-type-level phase structure ($S^1$/$U(1)$-valued with $2\pi$ periodicity) is **FORM-FORCED** in ED by P09 + P10 + three declared postulates. P09 supplies channel-level $U(1)$ natively (per Paper_087); this paper supplies the propagation to rule-types under P10 composition. Numerical normalization is **INHERITED**.

The result composes with prior work: T17, Aharonov–Bohm walkthrough, Born–Gleason, V1 kernel all **use** the rule-type $S^1$ phase whose origin is established here.

---

## Appendix — Cyclic Structure Across the ED Corpus

| Object | Cyclic structure | Source |
|---|---|---|
| V1 kernel phase rotation | $U(1)$ | Paper_089 |
| Gauge group fiber | $U(1)$, $SU(2)$, $SU(3)$ via P09 + non-Abelian extension | Paper_015 / YM-1 |
| Aharonov–Bohm flux | $U(1)$ | Walkthrough |
| Berry-phase holonomy | $U(1)$ or higher | Walkthrough |
| Born–Gleason Hilbert space | $S^1$ phase | Paper_002 |
| Spinor bundle Cl(3,1) | $\mathrm{Spin}(3,1)$ | R.2.4 (legacy cross-reference) |

Repeated $U(1)$/$S^1$ appearance across the corpus is the empirical signature of P09 + P10 + P-Composition-Cyclic structural forcing.

---

**End Paper 008 (FIXED).**
