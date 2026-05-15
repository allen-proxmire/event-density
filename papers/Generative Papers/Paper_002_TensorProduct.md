# Paper_002 — Tensor-Product Composition (QM-Kinematics Level) from P02 + P03

**Series:** Event Density (ED) Generative Papers — Wave-2 QM-kinematics arc
**Author:** Allen Proxmire
**Status:** Publication draft (QM-kin-level companion to Paper_063 entanglement-arc tensor-product)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/qm-kinematics/Paper_002_TensorProduct.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System.

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 primitives are not derived** (Paper_087).
2. **No claim that tensor-product structure is derived from P02 + P03 alone.** It is derived under P-QMkin-Composition (this paper's substrate-level commitment) + P02 adjacency + P03 spatial homogeneity. The substrate-level mapping of independent-subsystem composition to standard tensor-product structure is a paper-specific postulate.
3. **No duplication of Paper_063 content.** Paper_063 develops the entanglement-arc E-1/E-2 tensor product + non-factorizability. This paper develops the **QM-kinematics-arc tensor product** at the kinematic structural level — composition of independent subsystems in the substrate framework, separate from the entanglement-specific bipartite content.
4. **No claim of standard tensor-product categorical axioms.** Standard axioms (universality, bilinearity, distributivity) emerge in the Hilbert-space completion (Paper_007); this paper supplies the substrate-level kinematic composition rules.
5. **No claim that multi-subsystem composition handles entangled states without V5.** Independent-subsystem composition gives product structure; entangled states (Paper_063 E-2) require V5 cross-chain correlation.

---

## Abstract

This paper develops **tensor-product composition at the QM-kinematics level** from P02 (participation) + P03 (channel + locus indexing + spatial homogeneity) + P-QMkin-Composition (this paper's substrate-level commitment that independent substrate-level subsystems compose with product structure). For two **independent subsystems** $\mathcal{S}_A$, $\mathcal{S}_B$ at distinct substrate-graph loci with no V5 cross-chain correlation, the joint substrate-level state is:

$$
\Psi^{AB} = \Psi^A \otimes \Psi^B = \left(\sum_{K_A} P_{K_A}^A |K_A\rangle\right) \otimes \left(\sum_{K_B} P_{K_B}^B |K_B\rangle\right) = \sum_{K_A, K_B} P_{K_A}^A P_{K_B}^B |K_A, K_B\rangle.
$$

The substrate-level mechanism: P02 + P03 establish substrate-level adjacency-graph independence for distinct loci with no shared participation channels; P-QMkin-Composition supplies the substrate-level composition rule that maps independence to product structure.

The paper supplies the **QM-kinematics tensor-product foundation** that Papers_001, 003, 007 build on; it is the kinematic-level companion to Paper_063's entanglement-arc E-1/E-2 development. The paper makes no claim of derivation of standard tensor-product axioms (Paper_007 territory), no duplication of Paper_063 entanglement content, and no claim that V5-entangled states factorize (Paper_063 E-2 establishes non-factorizability under V5).

---

## 1. Introduction

### 1.1 What this paper does

This paper supplies the **QM-kinematics-arc tensor-product foundation** distinct from but consistent with Paper_063 entanglement-arc. The relationship:

- **Paper_002 (this paper):** kinematic-level tensor-product composition for **independent subsystems** in the QM-kin context.
- **Paper_063:** entanglement-arc bipartite content E-1 (factorizable) + E-2 (non-factorizable via V5).

Paper_002 supplies the QM-kin-arc kinematic foundation; Paper_063 extends to the entanglement arc with explicit V5 cross-chain content.

**Justification for two papers covering similar content (round-7 honest acknowledgment).** Paper_002 and Paper_063 both describe substrate-level tensor-product structure for independent subsystems. They share the substrate-level commitment (P-QMkin-Composition in this paper, equivalent to the product-structure clause of Paper_063 P-Bipartite-Mapping). The two papers cover the same structural content **from the perspective of different arcs** — Paper_002 frames it as QM-kinematic foundation; Paper_063 frames it as the entanglement-arc E-1/E-2 development. **The current state is duplication**, not separation by structural content. **Consolidation into a single paper is a future structural-organization option**; the duplication is acknowledged here rather than papered over. Both papers' substrate-level postulates (P-QMkin-Composition, P-Bipartite-Mapping product clause) are equivalent statements of the same substrate-level commitment.

### 1.2 Why two papers on tensor product

The substrate-level tensor product appears in two structural contexts:
- **QM-kin context** (this paper): independent-subsystem composition; no V5 cross-chain content; product structure follows kinematically.
- **Entanglement context** (Paper_063): bipartite content with V5 cross-chain correlation; non-factorizable states.

Each paper serves its arc's foundational role. The two are **consistent at substrate level** — Paper_063's P-Bipartite-Mapping (round-5 fix: includes product structure for independent systems) is consistent with this paper's P-QMkin-Composition.

### 1.3 Arc context

- **Paper_001:** pre-individuation amplitudes (upstream).
- **Paper_002 (this paper):** tensor-product composition (QM-kin level).
- **Paper_003:** Born rule.
- **Paper_007:** Hilbert-space emergence.
- **Paper_063:** entanglement-arc tensor product + non-factorizability.

---

## 2. Primitive Inputs

**Substrate primitives (postulated, Paper_087):** P02 (participation), P03 (channel + locus indexing + spatial homogeneity), P04 (bandwidth), P07 (channel structure).

**Upstream paper dependencies:** Paper_087, Paper_001 (pre-individuation amplitudes).

**Paper-specific postulates:**

- **P-QMkin-Composition (Independent substrate-level subsystems compose with product structure):** *For two substrate-level subsystems $\mathcal{S}_A, \mathcal{S}_B$ at distinct substrate-graph loci with no shared participation channels and no V5 cross-chain correlation, the joint substrate-level state $\Psi^{AB}$ is the product $\Psi^A \otimes \Psi^B$ in the substrate-level joint-amplitude space indexed by $(K_A, K_B) \in \mathcal{K}_A \times \mathcal{K}_B$.* Substrate-level kinematic composition rule; not derivable from P02 + P03 alone (the structural mapping to product structure requires an explicit substrate-level commitment).

**Consistency with Paper_063 P-Bipartite-Mapping:** the two postulates are consistent. Paper_063's P-Bipartite-Mapping (round-5 form) includes "for independent chains, joint amplitude has product structure" — this paper's P-QMkin-Composition states the same content at the QM-kin level. Paper_063 then extends to V5-correlated content.

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| Pre-individuation amplitudes | D | Paper_001 |
| Substrate-graph adjacency-independence for distinct loci | **P (substrate-graph locality consequence of P02 + P03; folded into P-QMkin-Composition preconditions)** | §3.1 — adjacency-graph locality is an inherited substrate-graph structural assumption from P02 + P03 indexing structure, not an additional algebraic derivation. *(Round-7 relabel.)* |
| Joint subsystem state indexing by $(K_A, K_B)$ | P (definitional, part of P-QMkin-Composition) | §3.1 |
| Product structure $\Psi^{AB} = \Psi^A \otimes \Psi^B$ for independent subsystems | **P (P-QMkin-Composition)** | §2 substrate-level commitment; cannot be derived from P02 + P03 alone — the mapping of independence to product structure is the substantive content of the postulate. Standard-form construction folded into postulate. |
| Bilinearity, distributivity at QM-kin level | P (definitional) | §3.2 from product-structure construction |
| Standard tensor-product axioms (universality etc.) | I | Paper_007 (Hilbert-space completion) |
| Consistency with Paper_063 P-Bipartite-Mapping | D | §1.2 from substrate-level commitments aligning |

All rows P, D, or I. **No A (asserted) rows.**

---

## 3. Substrate-Level Tensor-Product Composition

### 3.1 Independent subsystems

Two substrate-level subsystems $\mathcal{S}_A, \mathcal{S}_B$ are **independent** at substrate level if:

- They occupy distinct substrate-graph loci with no shared participation channels.
- No V5 cross-chain correlation amplitude content spans between them.
- Their pre-individuation amplitude content $\{P_K^A\}, \{P_L^B\}$ is independently parameterized.

By P02 + P03 + adjacency-graph locality, two distinct substrate-graph loci have **adjacency-graph independence** in the absence of cross-locus content. This is the substrate-level basis for independent-subsystem composition.

### 3.2 The product-structure substrate-level commitment

By P-QMkin-Composition (§2), the joint state of independent subsystems has product structure:

$$
\Psi^{AB} = \Psi^A \otimes \Psi^B, \quad (\Psi^A \otimes \Psi^B)_{K_A K_B} = P_{K_A}^A \cdot P_{K_B}^B.
$$

**This is a substrate-level commitment, not a derivation from P02 + P03 alone.** The structural reason: P02 + P03 give substrate-graph adjacency-independence, but they do not force the joint substrate-level state to be expressible specifically as a product. The product-structure mapping is the substantive content of P-QMkin-Composition.

**Standard-form construction (folded into postulate per round-6 audit rule):** writing $\Psi^A \otimes \Psi^B$ in this specific tensor-product form matches the standard QM tensor-product structure. It is **constructed**, not derived. Honest framing: P-QMkin-Composition is the substrate-level commitment that maps independence to product structure.

**Dimensional check:** $P_{K_A}^A \cdot P_{K_B}^B$ has substrate-amplitude units$^2$; joint state $\Psi^{AB}$ is captured by these joint amplitudes. ✓

### 3.3 Bilinearity, distributivity (QM-kin level)

From the product-structure construction (P-QMkin-Composition):

- **Bilinearity:** $(c_1\Psi^A_1 + c_2\Psi^A_2) \otimes \Psi^B = c_1(\Psi^A_1 \otimes \Psi^B) + c_2(\Psi^A_2 \otimes \Psi^B)$.
- **Distributivity:** $\Psi^A \otimes (c_1\Psi^B_1 + c_2\Psi^B_2) = c_1(\Psi^A \otimes \Psi^B_1) + c_2(\Psi^A \otimes \Psi^B_2)$.

These follow definitionally from P-QMkin-Composition's product-structure construction.

### 3.4 Multi-subsystem composition

For $n$ independent subsystems $\mathcal{S}_1, \ldots, \mathcal{S}_n$:

$$
\Psi^{1\ldots n} = \Psi^1 \otimes \Psi^2 \otimes \cdots \otimes \Psi^n.
$$

Joint amplitudes indexed by $(K_1, K_2, \ldots, K_n) \in \mathcal{K}_1 \times \cdots \times \mathcal{K}_n$ with values $\prod_i P_{K_i}^i$.

### 3.5 Where this paper stops; Paper_063 picks up

This paper develops independent-subsystem composition only. **For V5-correlated subsystems (entangled states), Paper_063's E-2 mechanism applies: the joint amplitude acquires a bilocal $\Delta_{KL}^{AB}$ contribution and is no longer expressible as a product.** Paper_063 handles the entanglement-arc bipartite content; this paper handles the QM-kin-arc independent composition.

---

## 4. Connection to Hilbert-Space Composition (Paper_007)

Under Paper_007's Hilbert-space completion of motif algebra + sesquilinear inner product, the substrate-level tensor-product composition of this paper coarse-grains to standard Hilbert-space tensor product $\mathcal{H}_A \otimes \mathcal{H}_B$. Standard categorical-axiomatic tensor-product properties (universality, bilinearity) follow from Paper_007 completion machinery + this paper's substrate-level product-structure construction.

**Joint Hilbert-space pure states** in $\mathcal{H}_A \otimes \mathcal{H}_B$ separate into:
- **Product states** ($\Psi^{AB} = \Psi^A \otimes \Psi^B$): substrate-level independent subsystems (this paper's content).
- **Entangled states**: substrate-level V5-correlated subsystems (Paper_063 E-2 content).

---

## 5. Falsification Criteria

### 5.1 Product structure fails for independent subsystems

**Falsifier sentence:** *Empirical demonstration that two independent substrate-level subsystems (verified independent at substrate level) do not exhibit product-state composition — i.e., the joint amplitude is not expressible as $\Psi^A \otimes \Psi^B$ — would falsify P-QMkin-Composition.*

### 5.2 Substrate-graph adjacency-independence fails

**Falsifier sentence:** *Empirical demonstration that distinct substrate-graph loci exhibit non-trivial adjacency-graph dependence (without V5 cross-chain content) — would falsify P02 + P03 adjacency-graph locality assumption.*

### 5.3 Inconsistency with Paper_063

**Falsifier sentence:** *Empirical demonstration that this paper's P-QMkin-Composition product-structure for independent subsystems is inconsistent with Paper_063's P-Bipartite-Mapping product-structure clause — would force one of the two papers to revise its substrate-level commitment.*

### 5.4 Multi-subsystem composition fails

**Falsifier sentence:** *Empirical evidence that three or more independent substrate-level subsystems do not compose to the joint product $\Psi^1 \otimes \Psi^2 \otimes \Psi^3$ — would falsify §3.4 multi-subsystem extension.*

---

## 6. Position Statement

**Tensor-product composition at the QM-kinematics level** is a downstream structural identification under P02 + P03 + P-QMkin-Composition. The product structure $\Psi^{AB} = \Psi^A \otimes \Psi^B$ for independent subsystems is the substrate-level kinematic foundation that Papers_001, 003, 007 build on.

What this paper claims:

- Independent substrate-level subsystems compose with product structure under P-QMkin-Composition.
- This paper is the QM-kin-arc companion to Paper_063's entanglement-arc tensor-product content.
- Standard-form tensor-product structure is constructed via P-QMkin-Composition, not derived from P02 + P03 alone.

What this paper does *not* claim:

- Standard tensor-product axioms not derived (Paper_007).
- V5-correlated entangled states not covered (Paper_063 E-2).
- P-QMkin-Composition not derivable from canonical 13 alone.

**Series context.** Paper_002 of QM-kin arc.

---

## Appendix

**Cross-references:** Paper_087, Paper_001, Paper_003, Paper_007, Paper_063.

**Glossary:**
- **Tensor-product composition.** Joint substrate-level state of independent subsystems has product structure.
- **P-QMkin-Composition.** Substrate-level commitment that independent subsystems compose with product structure.
- **Independent subsystems.** Distinct substrate-graph loci with no shared channels + no V5 cross-chain correlation.

---

**End of Paper_002.**
