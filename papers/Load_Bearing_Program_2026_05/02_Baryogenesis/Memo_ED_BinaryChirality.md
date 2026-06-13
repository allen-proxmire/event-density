# Memo_ED_BinaryChirality — Construction Attempt: Native ℤ₂ Reduction of Chain-Arrow Chirality

**Series:** Wave-3 Construction Memo (Cosmology Arc; pre-baryogenesis prerequisite)
**Status:** Substrate-graph attempt to reformulate chirality $\chi_C$ natively as a binary quantity $\hat\chi_C \in \{+1, -1\}$ from P11 directed-event structure (Criterion-A(3) from `Memo_ED_AdmissionFilter`). **Not a derivation of baryogenesis. Not a generative paper. No new primitives proposed.**
**Date:** 2026-05-15
**Anchors:** Paper_087 (primitives); Paper_072 (individuation regime); Paper_089 (V1 retarded kernel; T18 advanced-V1 refuted); Paper_090 (V5 cross-chain); Paper_093 (T18 kernel-arrow); Papers SC-4.x; Paper_ED_CCC §3.7; Memo_ED_ChainArrowChirality; Memo_ED_AdmissionFilter; Paper_095 (verdict grammar).
**Outcome (advance summary):** **All three reduction paths (R1, R2, R3) fail to close at substrate-graph level from existing primitives.** The corpus does not currently supply a native $\mathbb{Z}_2$ chain-attribute. Recommended fallback: Path-2 of `Memo_ED_AdmissionFilter` — declare **P-BinaryAdmission** as paper-specific postulate in the eventual baryogenesis paper, accepting verdict **M2**.

---

## §1 Purpose

The chirality memo delivers $\chi_C \in S^1$ at D-via-I level as a P09 phase difference. The admission-filter memo identifies binary admission $\chi_C \in \{0, \pi\}$ as OPEN, with Criterion-A(3) — native $\mathbb{Z}_2$ reformulation — as the closest path to closure. This memo attempts that reformulation through three reduction paths and reports the result.

**What this memo aims to construct:** $\hat\chi_C \in \{+1, -1\}$ as a substrate-graph chain-attribute derivable from existing primitives + upstream content, without new primitives or postulates.

**What this memo does not deliver (advance summary):** the construction. All three paths fail. The substantive finding is the **structural reason** for the failure: the corpus currently has one native $\mathbb{Z}_2$ structure (P11 commitment-irreversibility's binary directed-event content), but Paper_089 T18's retarded-only V1 forecloses the most natural binary-chirality reduction.

---

## §2 Inputs

**Upstream content:**
- $\chi_C(e_n) := \pi_C - \pi_K \pmod{2\pi}$, continuous $S^1$-valued (Memo_ED_ChainArrowChirality §3.3).
- $\sigma_C(e_n) = (e_n \to e_{n+1})$, directed P11-edge inheritable as chain-arrow.
- $\sigma_K(\ell)$, V1 retarded-support direction (Paper_093 T18).
- Post-SCBU regime: $\sigma_K$ globally coherent (Paper_ED_CCC §3.7 + SC-4.x).
- V1 strictly retarded; advanced V1 refuted by P11 (Paper_089 T18).
- P09 polarity carrier: continuous $U(1)$-valued.
- Paper_072 individuation regime as the admissibility criterion.

**No primitive supplies a native chain-attached $\mathbb{Z}_2$ attribute as currently constructed.** The substrate-graph $\mathbb{Z}_2$ candidates in the corpus are:

(i) P11 commitment-irreversibility's forward-vs-reverse binary at the event level.
(ii) The $\mathbb{Z}_2 \subset U(1)$ subgroup $\{0, \pi\}$ inside P09 (mathematical but not load-bearing).
(iii) The chain-existence binary (individuated vs failed-individuation) per Paper_072 (binary on existence, not on chain TYPE).

None of (i), (ii), (iii) currently functions as a chain-typing binary in the corpus.

---

## §3 Reduction Path R1 — Sign of alignment $\sigma_C \cdot \sigma_K$

**Statement:** Define $\hat\chi_C := \text{sign}(\sigma_C \cdot \sigma_K)$, with $+1$ when chain-arrow is co-directional with kernel-arrow and $-1$ when anti-directional.

### 3.1 What follows

$\sigma_C(e_n) = (e_n \to e_{n+1})$ is a directed P11-edge from $\ell(e_n)$ to $\ell(e_{n+1})$. $\sigma_K(\ell(e_n))$ is the kernel-arrow at the chain's current locus. Both are directed substrate-graph quantities.

### 3.2 Critical obstruction: Paper_089 T18 (advanced V1 refuted)

Per Paper_089 T18, advanced V1 is refuted by P11. **Every chain advances via V1 retarded propagation, which has support only along the kernel-arrow forward direction.** A chain whose $\sigma_C$ is anti-directional with $\sigma_K$ would require advanced V1 support — refuted.

**Consequence:** at substrate-graph level, $\sigma_C$ is *always* co-directional with $\sigma_K$. Every chain satisfies $\hat\chi_C^{R1} = +1$. The $-1$ class is *empty*. R1 does not produce a binary; it collapses to a monary.

### 3.3 Status

**R1 FAILS.** Paper_089 T18 forecloses the most natural binary reduction. There is no anti-aligned class of chains under literal edge-direction reading. The reading of "anti-aligned-tension chain" in ED-I-11 cannot be the spatial reverse of $\sigma_K$; it must mean something else.

ED-I-11's own framing supports this: *"Tension polarity is not motion, not force, and not orientation in space. It is a phase relationship between a chain's update rule and the ED-flow that surrounds it."* So the literal R1 reading was never the intended interpretation. R1 is included for completeness; the result is a negative finding: literal alignment-sign is excluded by Paper_089 T18.

---

## §4 Reduction Path R2 — Parity of directed-edge composition

**Statement:** Define $\hat\chi_C := (-1)^{N(C)}$ for some substrate-graph parity $N(C)$ computable from the chain's edge composition or commitment-event content.

### 4.1 Candidate parities

| Candidate | Substrate-graph content | Status |
|---|---|---|
| Number of commitment events $|C|$ mod 2 | Chain length parity | Not a chain-typing invariant; varies with chain age, not chirality. |
| Number of V5 cross-chain couplings mod 2 | Cross-chain count parity | Not a chain-typing invariant; varies with interaction history. |
| Sign of an alternating P09 phase product $\prod_n (-1)^{[\pi_C(e_n) > \pi_K]}$ | Phase-step parity | Requires defining "phase-step direction," which inherits the continuous P09 problem. |
| Signature of a chain-attached substrate involution | Chain-level $\mathbb{Z}_2$ from a substrate involution | The corpus does not currently name a chain-attached substrate involution. |

### 4.2 Critical obstruction: no chain-typing parity exists

P11 supplies binary at the event-direction level (forward/reverse for the SUBSTRATE EDGE), but every chain's edges are forward (per Paper_089 T18). Composition of forward edges is forward — no parity arises from edge composition along the chain.

V5 cross-chain content (Paper_090) supplies chain-pair correlation structure but does not tag individual chains with a binary attribute. V5 couples chains; it does not type them.

Paper_072 individuation supplies the chain-existence binary (individuated / failed), but this is a yes/no on chain *existence*, not a chirality distinction between *types of individuated chains*.

P09 admits the $\mathbb{Z}_2 \subset U(1)$ subgroup $\{0, \pi\}$, but membership in this subgroup is a property of phase VALUE, not of substrate structure. The substrate does not natively distinguish "phase = 0" from "phase = $\pi/4$" — both are P09-admissible.

### 4.3 Status

**R2 FAILS.** No substrate-graph parity over chain-edge composition or commitment-event content yields a chain-typing binary that distinguishes matter from antimatter. The candidate parities (chain length, V5 count, alternating phase product) are either not chain-typing (vary with history rather than identity) or inherit the continuous P09 obstruction.

---

## §5 Reduction Path R3 — Collapse of continuous P09 to binary under SC-4.x + post-SCBU homogeneity

**Statement:** In the homogeneous post-SCBU regime, continuous P09 phase values collapse to a binary class $\hat\chi_C \in \{+1, -1\}$ corresponding to $\chi_C \in \{0\}$ and $\chi_C \in \{\pi\}$ respectively. The collapse is forced by substrate homogeneity + SC-4.x scale-collapse.

### 5.1 What scale-collapse actually does

SC-4.x cross-scale invariance + curvature-moment collapse removes *scale information* from the substrate (Papers SC-4.x). At the boundary, no local content distinguishes scales because the matter content that supplied the scale information has dilluted below substrate-relevance.

**Scale-collapse is about scales, not orientations.** A scale-collapsed substrate can still have continuous orientational content. The flat plane is scale-invariant (no preferred length scale) yet has continuous orientations.

### 5.2 What post-SCBU homogeneity supplies

Paper_ED_CCC §3.7 establishes that post-SCBU substrate has a globally-coherent kernel-arrow. This means $\pi_K(\ell)$ is uniform across substrate up to a global $U(1)$ choice. It does **not** restrict $\pi_C(\ell)$ values — chains can carry any P09 phase.

### 5.3 Critical obstruction: no substrate-graph mechanism for $S^1 \to \mathbb{Z}_2$ collapse

For $\chi_C \in S^1$ to collapse to $\hat\chi_C \in \mathbb{Z}_2$, the substrate must supply a mechanism that maps continuous phases to binary classes. Candidate mechanisms:

- **Spontaneous symmetry breaking:** the substrate's $U(1)$ symmetry breaks to $\mathbb{Z}_2$ in the post-SCBU regime. Would require a substrate-graph derivation of the breaking; not constructed.
- **Energy-minimization:** intermediate $\chi_C$ values have higher substrate-graph energy than $\{0, \pi\}$, so they are not realized in equilibrium. Would require a substrate-graph "energy" or "cost" function; not currently named.
- **Discretization of P09:** P09's $U(1)$ structure is fundamentally discrete at substrate-graph level, with only $\{0, \pi\}$ admissible. **Inconsistent with P09 as defined in Paper_087 (continuous $U(1)$-valued polarity).**

### 5.4 Status

**R3 FAILS.** Homogeneity and scale-collapse do not, by themselves, force a continuous-to-binary phase collapse. No substrate-graph mechanism in the current corpus implements an $S^1 \to \mathbb{Z}_2$ reduction. The discretization-of-P09 candidate is inconsistent with P09's continuous definition.

---

## §6 Combined verdict: Criterion-A(3) does not close

| Reduction path | Status | Reason for failure |
|---|---|---|
| **R1** — sign of alignment $\sigma_C \cdot \sigma_K$ | **FAILS** | Paper_089 T18: advanced V1 refuted; all chains have $\sigma_C$ co-aligned with $\sigma_K$; no $-1$ class exists. |
| **R2** — parity of directed-edge composition | **FAILS** | No chain-typing parity available from P11 + Paper_089 + V5 + Paper_072 substrate content. Candidate parities are either not chain-typing or inherit the continuous P09 problem. |
| **R3** — collapse of $S^1$ to $\mathbb{Z}_2$ under SC-4.x + homogeneity | **FAILS** | Scale-collapse + homogeneity do not force continuous-to-binary phase reduction. No substrate-graph mechanism in the corpus implements $S^1 \to \mathbb{Z}_2$. |

**Substantive finding:** **the ED corpus, as currently constructed, does not supply a native chain-typing $\mathbb{Z}_2$ attribute derivable from existing primitives.** The substrate has:

- Binary structure at the event-direction level (P11 forward/reverse), but Paper_089 T18 forecloses its use as a chirality binary at the chain level.
- Continuous structure at the P09 phase level, which cannot be collapsed to binary without additional substrate machinery not currently named.
- Cross-chain coupling structure (V5), which is chain-pair-typing in some senses but not single-chain-typing.

**Without a chain-typing binary at substrate-graph level, the admission filter $\chi_C \in \{0, \pi\}$ cannot be derived from existing primitives.** Criterion-A(3) is the closest path to closure identified in `Memo_ED_AdmissionFilter`; this memo confirms it does not close.

---

## §7 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P02, P04, P05, P07, P09, P11, P13 | P | Paper_087. |
| 2 | V1 retarded kernel; T18 advanced-V1 refuted | I | Paper_089. |
| 3 | V5 cross-chain kernel | I | Paper_090. |
| 4 | Kernel-arrow $\sigma_K(\ell)$ | I | Paper_093 T18. |
| 5 | Paper_072 individuation regime | I | Paper_072. |
| 6 | Continuous chirality $\chi_C \in S^1$ | I | Memo_ED_ChainArrowChirality. |
| 7 | Post-SCBU regime + globally-coherent kernel-arrow | I | Paper_ED_CCC §3.6 + §3.7. |
| 8 | R1 (alignment-sign): $\sigma_C$ always co-aligned with $\sigma_K$ per Paper_089 T18 | **D-via-I (negative result)** | $\hat\chi_C^{R1} = +1$ for all chains. No $-1$ class. R1 produces monary, not binary. §3.2. |
| 9 | R2 (edge-composition parity): no chain-typing parity available | **D-via-I (negative result)** | Composition of forward edges is forward; V5 / Paper_072 do not supply chain-typing parity. §4.2. |
| 10 | R3 (continuous-to-binary collapse): no substrate-graph $S^1 \to \mathbb{Z}_2$ mechanism | **D-via-I (negative result)** | Scale-collapse ≠ orientation-collapse; homogeneity does not force binary phase restriction. §5.3. |
| 11 | Native chain-typing $\mathbb{Z}_2$ attribute in the corpus | **OPEN / does not exist as currently constructed** | The corpus has event-direction $\mathbb{Z}_2$ (foreclosed by T18) and P09 $U(1)$ continuous; no chain-typing $\mathbb{Z}_2$ identified. |
| 12 | Criterion-A(3) closure | **OPEN — FAILED ATTEMPT** | Three reduction paths attempted; none closes from existing primitives. §6. |
| 13 | Alternative paths: substrate-graph extension introducing a chain-typing involution | **OPEN; structural-extension-required** | Would require adding a substrate-graph involution attaching to chains, e.g., a V5-symmetry generator with $\mathbb{Z}_2$ structure. Not in current corpus. |
| 14 | Alternative paths: paper-specific postulate (P-BinaryAdmission) | **Available (verdict M2)** | Per Memo_ED_AdmissionFilter Path-2. Eventual baryogenesis paper acceptable at M2. |
| 15 | Verdict: native $\mathbb{Z}_2$ chirality NOT derivable from existing primitives | **A→position** | Per Paper_095 §3.3. |

**No pure-D rows.** Three negative-result D-via-I rows (8, 9, 10) plus one structural-finding row (11). The corpus lacks a chain-typing $\mathbb{Z}_2$ attribute as currently constructed; this is the load-bearing substantive finding.

---

## §8 Falsification Criteria

- **F1 (framework-confirming, not killing):** Substrate-graph construction supplying a native chain-typing $\mathbb{Z}_2$ attribute from existing primitives WITHOUT requiring new substrate-graph machinery. Would refute this memo's negative result and supply the missing admission-filter content. Three known candidate constructions ruled out (R1, R2, R3); discovery of a fourth would close the framework.

- **F2 (framework-killing):** Substrate-graph derivation proving that **no chain-typing $\mathbb{Z}_2$ attribute is constructible from existing primitives — not just from R1/R2/R3, but from any reduction path**. Would close the corpus-level conclusion that ED's substrate genuinely lacks a chirality binary, forcing either:
  - Ontology extension (new primitive supplying $\mathbb{Z}_2$ structure), or
  - Acceptance that ED's substrate is intrinsically chirality-neutral and baryogenesis is not a substrate-side mechanism.

- **F3:** Discovery that Paper_089 T18 admits a weaker reading permitting reverse-direction substrate edges under some regime (e.g., post-SCBU substrate with non-standard P11 behavior). Would reopen R1 as a candidate. Currently inconsistent with Paper_089 T18 as constructed.

- **F4:** Discovery that V5 cross-chain coupling (Paper_090) carries a chain-typing $\mathbb{Z}_2$ generator. Would reopen a V5-based R2-variant. Currently not supported by Paper_090 as constructed.

---

## §9 Recommended Next Steps

The three-memo construction sequence (`Memo_ED_ChainArrowChirality` → `Memo_ED_AdmissionFilter` → this memo) has arrived at a clear conclusion: **the eventual baryogenesis paper cannot be drafted at M3-form-IDENTIFIED without ontology extension.** Two paths forward:

### Path-A (Path-1 from AdmissionFilter): Ontology extension

A new substrate-graph construction supplying a chain-typing $\mathbb{Z}_2$ attribute. Likely candidates:

- A new V5-attached substrate generator with $\mathbb{Z}_2$ structure (would require revising Paper_090).
- A substrate involution on chain-content not currently named (would require a focused construction memo on chain-level discrete symmetries).
- An emergent $\mathbb{Z}_2$ from V1/V5 interaction structure (would require a focused construction memo on V1/V5 algebraic content).

**This is genuinely substrate-research work, not paper-drafting work.** It is outside the scope of the immediate baryogenesis-paper preparation and may not yield closure quickly.

### Path-B (Path-2 from AdmissionFilter, recommended): Paper-specific postulate

Declare **P-BinaryAdmission** as the paper-specific postulate in the eventual baryogenesis paper:

> **P-BinaryAdmission:** *In the post-SCBU ignition regime, Paper_072 individuation admits only chain-arrow chirality values $\chi_C \in \{0, \pi\}$ (binary). Continuous intermediate values fail individuation. Substrate-graph derivation OPEN.*

This is the honest reading of the three-memo result: the framework requires a chirality binary that the substrate does not currently supply; the postulate names the load-bearing OPEN derivation explicitly.

**Verdict for the eventual baryogenesis paper: M2 (Intermediate Path C with declared paper-specific postulates).** Substrate mechanism identified at the structural level; constructive derivation of P-BinaryAdmission OPEN. This is consistent with Paper_095's M2 verdict-tier and matches the pattern of other M2 papers in the corpus (e.g., GR_Lambda_V1, U_FourPostulatesUnification, RQM_GRH_D1).

### Recommendation

**Proceed via Path-B.** The three memos have rigorously mapped the substrate-graph terrain; Criterion-A(3) closure does not exist within existing primitives. Acceptance of M2 verdict with explicit P-BinaryAdmission postulate is the honest path forward and unblocks the baryogenesis-arc generative paper. Path-A (ontology extension) remains available as a future research direction; if a substrate-graph derivation of $\mathbb{Z}_2$ chirality is discovered later, the baryogenesis paper's verdict can be upgraded M2 → M3.

**Bottom line:** the next memo / paper in this sequence is the eventual baryogenesis-arc generative paper itself, written at **M2** with **P-BinaryAdmission** as the named paper-specific postulate and substrate-graph chirality derivation as the central OPEN item. The roadmap from `Memo_ED_Baryogenesis_Scoping` §6 is fully consistent with this conclusion.

---

**End Memo_ED_BinaryChirality.**
