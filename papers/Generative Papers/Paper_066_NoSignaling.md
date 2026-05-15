# Paper 066 — No-Signaling FORCED Over-Determined (E-5)

**Series:** Wave-2 Generative Papers (Entanglement Arc, E-5)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_063 (E-1 tensor product), Paper_064 (E-3 Schmidt), Paper_065 (E-4 monogamy), Paper_067 (E-6 von Neumann), Paper_090 (V5 kernel).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim novel empirical content beyond standard quantum no-signaling.
2. It does **not** claim that no-signaling rules out all non-local correlations; entanglement-correlations are admissible and exhibited (Bell experiments).
3. It does **not** claim a substrate-level resolution of the Bell-inequality / Tsirelson-bound question; Bell-Tsirelson polytope reconstruction is addressed in Paper_069.
4. It does **not** introduce new substrate primitives.
5. "No-signaling" means: the marginal distribution $p(a|x)$ at one wing of a bipartite measurement does not depend on the measurement choice $y$ at the other wing: $p(a|x, y) = p(a|x)$ when marginalized over $b$.

---

## Abstract

No-signaling is FORCED over-determined in ED by three independent structural locks: (L1) **P-Bipartite-Mapping**: the bipartite chain partition supplies independent local algebras with vanishing commutator at space-like separation; (L2) **V5 cross-chain bandwidth** (Paper_090): finite bandwidth at substrate level cannot transmit operational signals exceeding the substrate $c$ propagation rate, and the marginal-independence at instantaneous (or space-like) separation follows from the tensor-product structure (Paper_063); (L3) **DCGT coarse-graining** (Paper_073): the local-operator coarse-graining preserves the algebra-locality structure. Each lock independently forces $p(a|x,y) = p(a|x)$ at the marginalization level; the over-determination is what justifies the "FORCED over-determined" verdict.

---

## §1 Introduction

No-signaling — that local measurement statistics at one wing of a bipartite quantum system do not depend on remote measurement choices — is a load-bearing structural feature of quantum mechanics. It is preserved by entanglement (despite non-local correlations) and is the principle preventing entangled-state-based superluminal communication.

This paper supplies the substrate audit: no-signaling is over-determined by three independent substrate-level locks. Refutation of any single lock leaves the others intact; refutation of all three would simultaneously falsify the substrate program at multiple foundational layers.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P01 (Chains)** — supplies the bipartite chain partition.
- **P02 (Participation)** — supplies the substrate-level state content.
- **P10 (Rule-type primitive)** — supplies V5 as kernel rule-type.
- **P11 (Commitment-irreversibility)** — supplies the directional structure preventing backward causation.

### 2.2 Upstream dependencies

- **I-063:** Tensor-product structure on bipartite chain pairs (Paper_063, E-1).
- **I-090:** V5 cross-chain correlation kernel with finite bandwidth (Paper_090).
- **I-073:** DCGT coarse-graining (Paper_073).
- **I-LocAlg:** Standard local-algebra theory of QFT (standard math).
- **I-Born:** Born rule (Paper_002).

### 2.3 Paper-specific postulates

- **P-Bipartite-Mapping:** The substrate-level chain partition into $A$ and $B$ subsystems supplies independent local operator algebras $\mathcal{A}_A$ and $\mathcal{A}_B$ with $[\mathcal{A}_A, \mathcal{A}_B] = 0$ at space-like separation (microcausality analog).
- **P-Substrate-Causality:** V5 kernel rule-type respects substrate causality: $K_{V5}(x, y; t, t') = 0$ for $(x,y)$ space-like separated relative to substrate $c$.

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | Bipartite chain partition $A \cup B$ | P-Bipartite-Mapping | Postulate; definitional setup. |
| 2 | Tensor-product structure $\mathcal{H}_A \otimes \mathcal{H}_B$ | I | Paper_063 (E-1). |
| 3 | Local algebras $\mathcal{A}_A$, $\mathcal{A}_B$ with $[\mathcal{A}_A, \mathcal{A}_B] = 0$ space-like | P-Bipartite-Mapping (microcausality clause) | Postulate. |
| 4 | V5 kernel respects substrate causality | P-Substrate-Causality | Postulate. |
| 5 | Born rule supplies probability assignment | I | Paper_002. |
| 6 | Marginal probability $p(a|x) = \mathrm{Tr}[\rho \cdot (E_a^x \otimes I)]$ | I | Standard born-rule application with I-LocAlg. |
| 7 | Lock L1: Marginal $p(a|x)$ depends only on $\rho_A$, not on $y$ | D-via-I | Application of partial-trace + tensor-product structure to step 6. |
| 8 | Lock L2: V5 cannot transmit operational signal exceeding substrate $c$ | D-via-I | Application of P-Substrate-Causality + finite V5 bandwidth. |
| 9 | Lock L3: DCGT coarse-graining preserves local-algebra structure | I | Paper_073. |
| 10 | Three independent locks → over-determination | A→position | Composite verdict. |
| 11 | Bell-Tsirelson bound | OPEN (Paper_069) | Not claimed here. |

---

## §3 The Three Locks

### 3.1 Lock L1 — Tensor-product + local-algebra microcausality

By I-063, the bipartite Hilbert space is $\mathcal{H}_A \otimes \mathcal{H}_B$. By P-Bipartite-Mapping, the local algebras $\mathcal{A}_A = \mathcal{B}(\mathcal{H}_A) \otimes I_B$ and $\mathcal{A}_B = I_A \otimes \mathcal{B}(\mathcal{H}_B)$ satisfy $[\mathcal{A}_A, \mathcal{A}_B] = 0$ at space-like separation.

Born rule (I-Born) gives marginal probability
$$p(a|x, y) = \sum_b \mathrm{Tr}[\rho \cdot (E_a^x \otimes F_b^y)] = \mathrm{Tr}[\rho \cdot (E_a^x \otimes I_B)] = p(a|x) ,$$
using $\sum_b F_b^y = I_B$ (POVM completeness; I).

**Lock L1: marginal independence of $y$ follows from tensor-product + POVM completeness.**

### 3.2 Lock L2 — V5 substrate-causality + finite bandwidth

V5 cross-chain kernel (Paper_090) has finite bandwidth $\ell_{V5}$. By P-Substrate-Causality, $K_{V5}(x, y; t, t') = 0$ for space-like-separated $(x,y)$ relative to substrate $c$.

Operationally, this prevents the **substrate-level transmission** of any signal between $A$-chains and $B$-chains at space-like separation: even if the marginal-independence of L1 were violated at a hypothetical state-prep level, the V5 substrate-causality prevents the violation from being **operationally accessed** at a remote wing within space-like separation.

**Lock L2: V5 substrate-causality prevents operational signal transmission space-like.**

### 3.3 Lock L3 — DCGT preserves local-algebra structure

DCGT (Paper_073) coarse-grains substrate algebra to continuum local algebras. The coarse-graining respects locality: operators with substrate-level support on $A$-chains coarse-grain to operators in $\mathcal{A}_A$ (and similarly for $B$).

**Lock L3: coarse-graining preserves the algebra-locality structure.**

### 3.4 Over-determination

Refutation of L1 alone (e.g., bipartite Hilbert structure fails) would leave L2 (V5 causality) intact: V5 still prevents space-like signal transmission. Refutation of L2 alone (V5 violates substrate-causality) would leave L1 (tensor-product marginal independence) intact: marginal would still be independent at the formal level. Refutation of L3 alone (DCGT scrambles locality) would leave L1 + L2 intact at substrate level.

Each lock independently forces $p(a|x,y) = p(a|x)$. The "FORCED over-determined" verdict reflects this redundancy.

---

## §4 What This Paper Supplies and Does Not Supply

**Supplies:** Three-lock substrate audit of no-signaling. Over-determination diagnostic.

**Does not supply:** Bell-inequality / Tsirelson-bound reconstruction (Paper_069). Quantum-correlation polytope (Paper_069). PR-box exclusion at the polytope-vertex level (Paper_069).

---

## §5 Open Structural Questions

- **O-NS-1:** Substrate derivation of P-Substrate-Causality from V5 kernel data — currently postulated.
- **O-NS-2:** Substrate derivation of P-Bipartite-Mapping microcausality clause from substrate combinatorics.
- **O-NS-3:** Connection to Bell-Tsirelson polytope (Paper_069 OPEN).
- **O-NS-4:** Multipartite no-signaling generalization.

---

## §6 Falsification Criteria

- **F1:** Empirical detection of superluminal operational signal transmission via entangled state — falsifies no-signaling (and the substrate program).
- **F2:** Demonstration that bipartite Hilbert structure (I-063) is incompatible with marginal-independence — refutes L1.
- **F3:** Demonstration that V5 kernel admits space-like correlation transmission with operational consequences — refutes L2.
- **F4:** Demonstration that DCGT coarse-graining can scramble local-algebra structure — refutes L3.

---

## §7 Position Statement

No-signaling is **FORCED over-determined** in ED by three independent substrate-level locks: tensor-product + microcausality (L1), V5 substrate-causality (L2), DCGT locality-preservation (L3). The composite verdict is **A→position**: refutation of any single lock leaves the others intact.

This is the E-5 step of the Entanglement Arc (Papers_063–070), composing with E-1 (tensor product), E-4 (monogamy via V5 budget), and supplying input to E-7 (synthesis) and the Bell-Tsirelson polytope work (Paper_069).

---

**End Paper 066 (FIXED).**
