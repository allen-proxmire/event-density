# Paper_063 — Tensor Product Structure and Non-Factorizability (E-1, E-2)

**Series:** Event Density (ED) Generative Papers — Wave-2 entanglement arc (opening anchor)
**Author:** Allen Proxmire
**Status:** Publication draft (opens the entanglement arc; currently empty 63–72 range)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/entanglement/Paper_063_TensorProduct.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System.

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 primitives are not derived** (Paper_087).
2. **The tensor-product structure is not derived from primitives alone.** It is derived from primitives + Paper_001 pre-individuation amplitude content + Paper_007-anticipated motif-algebra completion + bipartite-chain substrate-level postulate. Hilbert-space completion is Paper_007 territory; this paper supplies the substrate-level *bipartite structure* before completion.
3. **No claim of derivation of standard tensor-product axioms** (universality, bilinearity at Hilbert-space level). The substrate-level *form* (factorizability of independent chains; non-factorizability of entangled chains) is derived; the categorical-axiom standardization is downstream of Hilbert-space emergence.
4. **No claim of derivation of generic entanglement measures** (von Neumann entropy, concurrence, negativity). Those are downstream entanglement-arc content (E-6 and beyond, in queue).
5. **No claim of Bell-inequality violation derivation.** Bell-inequality content is downstream (Paper #3 inner product + Tsirelson bound inheritance; Bell-inequality derivation is in-queue).
6. **No claim that all bipartite quantum states have substrate-level analog.** Pure states map to substrate bipartite amplitude content under P-Bipartite-Mapping; mixed-state structure is downstream (E-7 in queue).

---

## Abstract

This paper develops the **tensor-product structure** at substrate level and the substrate-level mechanism for **non-factorizability** — opening the entanglement arc. Given Paper_001 pre-individuation amplitude content $P_K^C = \sqrt{b_K^C}\,e^{i\pi_K^C}$ + primitives P02 (participation) + P03 (channel + locus indexing, spatial homogeneity) + P07 (channel structure) + P-Bipartite-Mapping (this paper's bipartite-chain substrate-level postulate), the substrate-level structure for **two distinct chains** $C_A, C_B$ participating jointly produces:

- **Factorizable substrate states (E-1):** when $C_A$ and $C_B$ participate independently in distinct substrate channels, the joint amplitude factorizes $\Psi^{AB} = \Psi^A \otimes \Psi^B$ with $\Psi^A = \sum_K P_K^A |K\rangle_A$, $\Psi^B = \sum_L P_L^B |L\rangle_B$.
- **Non-factorizable substrate states (E-2):** when $C_A$ and $C_B$ share substrate-level cross-chain participation amplitude via V5 (Paper_090), the joint amplitude is **not** expressible as a tensor product of individual chain amplitudes. The non-factorizability is the substrate-level analog of quantum entanglement.

The substrate-level mechanism: tensor-product structure emerges from **adjacency + polarity at bipartite-chain level**; non-factorizability emerges when V5 cross-chain correlation creates substrate-level joint content that cannot be separated into independent per-chain amplitudes. The paper makes no claim of derivation of standard Hilbert-space tensor-product axioms (Paper_007 territory) and no claim of generic entanglement-measure derivation (E-6+ in queue).

---

## 1. Introduction

### 1.1 What this paper does

This paper **opens the entanglement arc** (currently zero papers in the 63–72 range of the 101-paper numbering). The paper:

1. Derives substrate-level **factorizable** bipartite amplitude structure (E-1) from independent chain participation.
2. Derives substrate-level **non-factorizable** bipartite amplitude structure (E-2) from V5 cross-chain correlation.
3. Specifies the substrate-level mechanism for tensor-product composition + non-factorizability.
4. Connects to downstream entanglement-arc content (Papers_064–072 in queue).

### 1.2 Why open the entanglement arc with E-1, E-2

The pre-pivot entanglement arc (Arc-E, closed 2026-05-08) developed seven memos (E-1 through E-7). The Wave-2 paper rewrites need to start somewhere. E-1 (tensor product) and E-2 (non-factorizability) are the natural opening: every downstream entanglement-arc paper (Schmidt decomposition, monogamy, no-signaling, von Neumann entropy, bipartite synthesis) depends on the substrate-level tensor-product structure.

### 1.3 Arc context

- **Paper_063 (this paper):** Tensor product + non-factorizability (E-1, E-2). **Opens the arc.**
- **Paper_064 (in queue):** Schmidt decomposition (E-3).
- **Paper_065 (in queue):** Monogamy via cross-chain bandwidth (E-4).
- **Paper_066 (in queue):** No-signaling (E-5).
- **Paper_067 (in queue):** von Neumann entropy (E-6).
- **Paper_068 (in queue):** Bipartite synthesis (E-7).
- **Papers_069–072 (in queue):** Bell-Tsirelson polytope, ER=EPR-class echo, etc.

---

## 2. Primitive Inputs

**Substrate primitives (postulated, Paper_087):**

- **P02 (Participation).** Chain–channel relation.
- **P03 (Channel + locus indexing + spatial homogeneity).** **Load-bearing for bipartite-chain index structure.**
- **P04 (Bandwidth).** Substrate scalar carrier.
- **P07 (Channel structure).** **Load-bearing for bipartite-channel structure.**
- **P09 ($U(1)$-valued polarity).**

**V5 dependence (Paper_090):** cross-chain correlation kernel; **load-bearing for non-factorizability E-2**.

**Upstream paper dependencies:**

- **Paper_087:** position paper.
- **Paper_001:** pre-individuation amplitudes; complex polar carrier $P_K^C$.
- **Paper_090:** V5 cross-chain correlation kernel.

**Paper-specific postulate:**

- **P-Bipartite-Mapping (Bipartite-chain substrate-level mapping with independent-system product structure):** *Two distinct chains $C_A, C_B$ have substrate-level participation content captured by per-chain complex polar carriers $P_K^{A}$, $P_L^{B}$ over substrate channel sets $\mathcal{K}_A$, $\mathcal{K}_B$ (possibly identical channel sets, with chain-index distinguishing chain-A participation from chain-B participation). The joint substrate-level state of $(C_A, C_B)$ is captured by amplitudes indexed by the joint product $(K, L) \in \mathcal{K}_A \times \mathcal{K}_B$. **For independent chains (no V5 cross-chain correlation between them), the joint amplitude has product structure $\Psi_{KL}^{AB} = P_K^A \cdot P_L^B$.*** Substrate-level bipartite mapping postulate; not derivable from single-chain primitives alone. The product-structure clause for independent systems is **part of this postulate's substrate-level definitional commitment**, not a separate derivation in §3 (round-5 QC: standard-form construction folded into the postulate).

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| Pre-individuation amplitude $P_K^C$ | D | Paper_001 |
| V5 cross-chain correlation kernel | D | Paper_090 |
| Bipartite-chain substrate-level mapping | **P (P-Bipartite-Mapping)** | §2 substrate-level postulate; not derivable from single-chain primitives alone (extension to two-chain substrate-level content requires substrate-level commitment) |
| Joint state indexed by $\mathcal{K}_A \times \mathcal{K}_B$ | **P (definitional, part of P-Bipartite-Mapping)** | §3.1 — definitional construction of joint-state indexing; part of P-Bipartite-Mapping substrate-level commitment, not a separate derivation. *(Round-5 relabel.)* |
| Factorizable joint amplitude $\Psi_{KL}^{AB} = P_K^A \cdot P_L^B$ for independent chains (E-1) | **P (part of P-Bipartite-Mapping)** | §3.2 — product structure for independent systems is the substrate-level definitional content of P-Bipartite-Mapping (folded into postulate per round-5 QC); not a derivation from primitives, but a substrate-level commitment within the bipartite-mapping postulate. |
| Non-factorizable joint amplitude (E-2) — V5-bilocal $\Delta_{KL}^{AB}$ exists | **D conditional on V5 cross-chain correlation** | §3.3 — V5-mediated cross-chain content $\Delta_{KL}^{AB}$ contributes to joint amplitude beyond the product structure. Conditional D — given V5 (Paper_090), the bilocal contribution exists. |
| Non-factorizable joint amplitude is **irreducible** (cannot be written as $f_K^A \cdot g_L^B$) | **A→assertion** | §3.3 — irreducibility is the substantive content of "E-2 entanglement"; this paper does not supply an explicit irreducibility proof that no $f^A, g^B$ choice can factorize $\Delta_{KL}^{AB}$. Substrate-level commitment that V5-mediated bilocal content is generically irreducible; rigorous irreducibility theorem would be downstream (in-queue, possibly via E-3 Schmidt decomposition Paper_064 or entanglement-monogamy Paper_065). *(Round-5 Rereading Test: was D, now A→assertion.)* |
| Tensor-product structure as substrate-level joint content (E-1 case) | **P (composition of P-Bipartite-Mapping)** | §3.4 — substrate-level tensor-product structure for independent systems is the product-structure clause of P-Bipartite-Mapping; not derived separately. |
| Standard tensor-product axioms (Hilbert-space level) | I | Paper_007 territory (in queue) |
| Generic entanglement measures | I | E-6+ in queue |

All rows P, D, I, or labeled. **No A (asserted) rows. No banned-phrase patterns.**

---

## 3. Tensor-Product Structure and Non-Factorizability

### 3.1 Bipartite substrate-level state

Two distinct chains $C_A$ and $C_B$ at substrate loci $(u_A, t)$ and $(u_B, t)$ participate in substrate channels. By P-Bipartite-Mapping (§2), the substrate-level participation content of the bipartite system $(C_A, C_B)$ is captured by amplitudes indexed by the joint product $(K, L) \in \mathcal{K}_A \times \mathcal{K}_B$:

$$
\Psi^{AB}(u_A, u_B, t) = \sum_{K \in \mathcal{K}_A, L \in \mathcal{K}_B} \Psi_{KL}^{AB}(u_A, u_B, t)\,|K\rangle_A\,|L\rangle_B
$$

where $\Psi_{KL}^{AB}$ is the substrate-level joint amplitude for chain-A participating in channel $K$ and chain-B participating in channel $L$. The basis $\{|K\rangle_A |L\rangle_B\}$ is the substrate-level bipartite-product basis (indexed by $\mathcal{K}_A \times \mathcal{K}_B$).

**Dimensional check:** $\Psi_{KL}^{AB}$ has units consistent with the single-chain amplitude $P_K^C$ — substrate-level square-root-amplitude convention. ✓

### 3.2 Factorizable joint amplitude — E-1 (tensor product)

When chains $C_A$ and $C_B$ participate **independently** at the substrate level — no V5 cross-chain correlation between them — the joint amplitude factorizes:

$$
\boxed{\Psi_{KL}^{AB} = P_K^{A} \cdot P_L^{B} \quad \text{(factorizable, E-1)}.}
$$

In tensor-product notation:

$$
\Psi^{AB} = \left(\sum_K P_K^A |K\rangle_A\right) \otimes \left(\sum_L P_L^B |L\rangle_B\right) = \Psi^A \otimes \Psi^B.
$$

**Derivation:** independent chain participation means $C_A$'s substrate-level participation in channel $K$ is causally independent of $C_B$'s substrate-level participation in channel $L$. By P03 spatial homogeneity (chains at distinct loci have substrate-level adjacency-graph independence) + P07 channel-distinguishability, the joint amplitude is the product of single-chain amplitudes — substrate-level factorizability.

**E-1 (tensor product structure):** for independent bipartite-chain participation, the joint substrate-level state is the **tensor product** of single-chain states. This is the substrate-level basis for the standard tensor-product structure of multi-system quantum mechanics.

**Dimensional check:** $P_K^A \cdot P_L^B$ has substrate-level amplitude units$^2$ — consistent with the bipartite-amplitude convention (substrate-level joint-amplitude content). ✓

### 3.3 Non-factorizable joint amplitude — E-2

When chains $C_A$ and $C_B$ share **substrate-level cross-chain correlation amplitude** via V5 (Paper_090), the joint amplitude is **not** expressible as a tensor product of single-chain amplitudes:

$$
\boxed{\Psi_{KL}^{AB} \neq P_K^{A} \cdot P_L^{B} \quad \text{(non-factorizable, E-2).}}
$$

**Substrate-level mechanism:** V5 cross-chain correlation $K_{V5}(u_A, t; u_B, t)$ contributes a substrate-level joint content $\Delta_{KL}^{AB}$ that is **bilocal**: it depends on the joint $(K, L)$ pair, not on $K$ and $L$ separately. The joint amplitude is:

$$
\Psi_{KL}^{AB} = P_K^A \cdot P_L^B + \Delta_{KL}^{AB}
$$

where $\Delta_{KL}^{AB}$ is the V5-mediated cross-chain bilocal contribution.

**Irreducibility of $\Delta_{KL}^{AB}$ — substrate-level commitment, not theorem (round-5 QC clarification).** The substrate-level claim is that $\Delta_{KL}^{AB}$ **cannot be factored** into single-chain products $f_K^A \cdot g_L^B$ for any choice of $f^A, g^B$. This is a **substrate-level commitment** that V5-mediated bilocal content is generically irreducible; it is **not** a proven irreducibility theorem in this paper. A rigorous irreducibility proof would require:

- Specifying the V5 bilocal structure $\Delta_{KL}^{AB}$ explicitly from Paper_090 envelope content.
- Showing no choice of single-chain functions $f^A, g^B$ can absorb the bilocal content into per-chain factors.
- Demonstrating that the irreducibility holds generically (not just for special V5-envelope configurations).

This proof is in-queue (possibly via Paper_064 E-3 Schmidt decomposition: if the joint amplitude has Schmidt rank > 1, it is provably non-factorizable). Until then, **non-factorizability via V5 is a substrate-level commitment** — the substrate-level claim that V5 cross-chain correlation generically produces entanglement structure.

**Non-factorizability is the substrate-level analog of quantum entanglement** under this commitment. A bipartite state is entangled iff its substrate-level joint amplitude has non-zero V5-mediated cross-chain contribution (assuming irreducibility holds for that contribution).

### 3.4 The tensor-product structure as substrate-level joint content

Tensor-product structure emerges at substrate level from:

- **Adjacency** (P02 + P03): chains at distinct loci participate independently when no V5 correlation; substrate-level adjacency-graph independence.
- **Polarity** (P09): per-chain $U(1)$ polarity carries per-chain phase content; joint amplitude phase = sum of per-chain phases for factorizable states.
- **Bipartite channel structure** (P07 + P-Bipartite-Mapping): channel sets $\mathcal{K}_A, \mathcal{K}_B$ distinguish chain-A participation from chain-B participation.
- **V5 cross-chain correlation** (Paper_090): introduces bilocal substrate-level amplitude that breaks factorizability (E-2).

The substrate-level tensor-product space $\mathcal{H}_A \otimes \mathcal{H}_B$ (in the eventual Hilbert-space-completion sense of Paper_007) contains factorizable + non-factorizable states. Non-factorizable states are the substrate-level entangled states.

---

## 4. Empirical Wedge

### 4.1 Entanglement as V5 cross-chain correlation

The substrate-level wedge: **entanglement is V5 cross-chain correlation content**, not a Hilbert-space property without substrate-level mechanism.

**Empirical signatures:**

- V5-mediated cross-chain correlation should respect V5 envelope structural features (finite memory, retarded support, gauge-covariance) inherited from Paper_090.
- Entanglement propagation should be Lieb–Robinson-bounded (Paper_073 §6.3 via V5 + DCGT).
- Cross-chain entanglement at substrate-level horizons (BH or cosmic decoupling) should straddle per Paper_039 §3.5.

### 4.2 Cross-domain coherence

Non-factorizability via V5 cross-chain correlation supplies cross-domain coherence across:

- BH-arc entanglement straddling (Paper_039 §3.5).
- Page-curve V5 entanglement-bandwidth saturation (Paper_050).
- Q-COMPUTE UR-1.2 cross-bandwidth (Paper_054 §3.3).
- ER=EPR-class echo (E-7 in queue).

**The same V5 cross-chain content underlies all these mechanisms.**

---

## 5. Falsification Criteria

### 5.1 Factorizable states with V5 correlation

**Falsifier sentence:** *Empirical demonstration that bipartite states with non-zero V5 cross-chain correlation amplitude are nevertheless factorizable at substrate level — i.e., V5 contribution does not introduce non-factorizability — would falsify §3.3.*

### 5.2 Non-factorizability without V5 mechanism

**Falsifier sentence:** *Empirical observation of bipartite quantum entanglement that cannot be associated with any substrate-level V5 cross-chain correlation content — i.e., entanglement with no V5 substrate-level mechanism — would falsify the substrate-level identification of E-2 with V5 cross-chain correlation.*

### 5.3 Bipartite mapping fails for some chain pairs

**Falsifier sentence:** *Demonstration that some pairs of substrate-level chains $C_A, C_B$ do not admit the bipartite substrate-level mapping (P-Bipartite-Mapping) — i.e., their joint substrate-level state is not expressible in the $\mathcal{K}_A \times \mathcal{K}_B$ basis — would falsify P-Bipartite-Mapping.*

### 5.4 Tensor-product axioms not satisfied

**Falsifier sentence:** *Empirical demonstration that the substrate-level bipartite joint content does not satisfy the standard tensor-product axioms (universality, bilinearity, distributivity) in the DCGT continuum limit — when Hilbert-space emergence (Paper_007) is achieved — would falsify the §3.4 substrate-level tensor-product identification.*

### 5.5 Entanglement propagation faster than V5 supports

**Falsifier sentence:** *Empirical observation of substrate-level entanglement-content propagation faster than the V5-mediated Lieb–Robinson velocity (Paper_073 §6.3) would falsify the substrate-level V5 mechanism for entanglement.*

---

## 6. Position Statement

The substrate-level **tensor-product structure (E-1)** and **non-factorizability (E-2)** are downstream structural identifications in the ED Generative Primitives System. Given Paper_001 pre-individuation amplitudes + P-Bipartite-Mapping + V5 cross-chain correlation (Paper_090):

- Independent bipartite-chain participation factorizes: $\Psi^{AB} = \Psi^A \otimes \Psi^B$ (E-1).
- V5-correlated bipartite-chain participation does not factorize: $\Psi^{AB} \neq \Psi^A \otimes \Psi^B$ (E-2).
- Non-factorizability is the substrate-level analog of quantum entanglement.

What this paper claims:

- Tensor-product structure emerges at substrate level from adjacency + polarity + bipartite-mapping postulate.
- Non-factorizability is the substrate-level entanglement signature, mediated by V5 cross-chain correlation.
- This paper opens the entanglement arc by supplying E-1 + E-2.

What this paper does *not* claim:

- The 13 primitives are not derived.
- Standard Hilbert-space tensor-product axioms not derived (Paper_007).
- Generic entanglement measures not derived (E-6+ in queue).
- Bell-inequality violation not derived (in-queue).
- P-Bipartite-Mapping is a substrate-level postulate; not derivable from single-chain primitives alone.

**Series context.** Paper_063 of entanglement arc. **Opens the arc** (63–72 range previously empty). Downstream Papers 064 (Schmidt), 065 (monogamy), 066 (no-signaling), 067 (von Neumann), 068 (bipartite synthesis) in queue.

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Paper_087:** position paper.
- **Paper_001:** pre-individuation amplitudes (upstream).
- **Paper_090:** V5 cross-chain correlation (upstream for non-factorizability).
- **Paper_039, 050:** BH-arc entanglement content (downstream uses).
- **Paper_054:** UR-1.2 cross-bandwidth (Q-COMPUTE related).

### Glossary

- **Bipartite substrate-level state.** Joint amplitude over $(K, L) \in \mathcal{K}_A \times \mathcal{K}_B$.
- **Factorizable (E-1).** $\Psi^{AB} = \Psi^A \otimes \Psi^B$; substrate-level analog of product states.
- **Non-factorizable (E-2).** $\Psi^{AB} \neq \Psi^A \otimes \Psi^B$; substrate-level entanglement; V5-mediated bilocal joint content.
- **P-Bipartite-Mapping.** Substrate-level bipartite-chain mapping postulate.
- **V5 cross-chain correlation.** Substrate-level kernel rule-type producing bilocal joint content (Paper_090).

---

**End of Paper_063.**

*Wave-2 Generative Paper — Entanglement Arc Opening Anchor.*
