# Memo_ED_ChainArrowChirality — Construction Memo for Chain-Arrow Chirality as a Substrate-Graph Quantity

**Series:** Wave-3 Construction Memo (Cosmology Arc; pre-baryogenesis prerequisite)
**Status:** Substrate-graph construction of chain-arrow chirality $\chi_C$ from existing primitives + upstream content. **Not a derivation of baryogenesis. Not a generative paper. No new primitives proposed.**
**Date:** 2026-05-15
**Anchors:** Paper_087 (primitives); Paper_072 (individuation regime); Paper_089 (V1 retarded kernel); Paper_090 (V5 cross-chain kernel); Paper_093 (T18 kernel-arrow of time); Papers SC-4.x (cross-scale invariance, curvature-moment collapse); Paper_028 + SCBU; Paper_ED_CCC §3.7 (post-boundary ignition + kernel-arrow homogeneity); Paper_095 (verdict grammar).
**Memo target:** Define chirality at the substrate-graph level operationally; identify what is IDENTIFIED, what is OPEN, what would require ontology extension. **No baryogenesis content** beyond the structural placement.

---

## §1 Purpose

Chain-arrow chirality $\chi_C$ is the load-bearing OPEN construction (a) in `Memo_ED_Baryogenesis_Scoping.md` §4. Before any baryogenesis-arc generative paper can be drafted, $\chi_C$ must be operationally defined as a substrate-graph quantity from existing primitives. This memo supplies the construction (at the substrate-identification level, not the full substrate-graph rigour level), identifies which downstream claims are structurally supported, and flags which remain OPEN.

**What this memo delivers:**
- An operational substrate-graph definition of $\chi_C$ at each P11 commitment event.
- A P05-transport rule giving $\chi_C$'s evolution along a chain.
- The structural reason the post-SCBU ignition regime admits only binary $\chi_C \in \{0, \pi\}$ (partially IDENTIFIED, partially OPEN).
- Audit table + falsifiers.

**What this memo does not deliver:**
- A substrate-graph derivation of the admission filter selecting one chirality class.
- A connection to baryogenesis dynamics.
- Any quantitative substrate-graph computation.

---

## §2 Primitive Inputs + Upstream Dependencies

**Primitives invoked (Paper_087):**
- **P02** (participation): chain $C$ participates in substrate channels.
- **P04** (bandwidth): $b_K \ge 0$, additive across channels.
- **P05** (polarity-transport along edges): transports P09 polarity content along chain + cross-chain edges.
- **P07** (channel structure): substrate channel decomposition.
- **P09** ($U(1)$-valued polarity): $\pi_K \in S^1$ at each channel.
- **P11** (commitment-irreversibility): commitment events are directed; supply the per-chain ordering.
- **P13** (kernel-driven dynamics + time homogeneity): supplies the substrate-side kernel structure that V1 + V5 implement.

**Upstream:**
- Paper_089: V1 finite-width retarded kernel. Supplies the substrate carrier of causal influence between commitment events.
- Paper_090: V5 cross-chain finite-memory kernel. Supplies cross-chain correlation content (not load-bearing for chirality definition; load-bearing for cross-chain consistency check, §3.5).
- Paper_093 T18: Kernel-arrow of time — the direction of V1 retarded support at each substrate locus. The kernel-arrow is the substrate-side directional content against which chirality is measured.
- Paper_072: Individuation regime — chain-identity preservation criterion under V1/V5 dynamics.
- Papers SC-4.x: Cross-scale invariance + curvature-moment collapse content; supplies the substrate-side reason for post-boundary kernel-arrow homogeneity.
- Paper_028 + SCBU + Paper_ED_CCC §3.7: Post-boundary substrate state with globally-coherent kernel-arrow.

**No new primitives. No new postulates. No paper-specific naming convention beyond labeling $\chi_C$ itself.**

---

## §3 Construction

### 3.1 Chain-arrow $\sigma_C$

A chain $C$ is a sequence of P11 commitment events $\{e_1, e_2, \ldots\}$ ordered by P11 commitment-irreversibility. Between consecutive events $e_n, e_{n+1}$, the chain content is transported by V1 retarded propagation (Paper_089) along a substrate edge (or short edge-sequence).

Define the **chain-arrow at event $e_n$** as the directed edge-content $\sigma_C(e_n) := (e_n \to e_{n+1})$: the substrate direction in which the chain advances from event $e_n$ to event $e_{n+1}$. The chain-arrow is well-defined per P11 commitment-irreversibility (every chain has a unique successor edge under P11 + Paper_089 V1 propagation) and is a substrate-graph quantity: it is a directed edge at substrate-graph level, not a vector in continuous spacetime.

**Status: IDENTIFIED.** $\sigma_C(e_n)$ is constructible from P11 + Paper_089 content alone; no additional content required.

### 3.2 Kernel-arrow $\sigma_K$ at the chain's locus

Per Paper_093 T18, V1's retarded support has a substrate-side direction at each locus: the **kernel-arrow** $\sigma_K(\ell)$ at substrate locus $\ell$. The kernel-arrow is the substrate-side directional content of V1 finite-width retarded propagation.

At each event $e_n$, the chain occupies a substrate locus $\ell(e_n)$; the kernel-arrow at that locus is $\sigma_K(\ell(e_n))$. This is a substrate-graph quantity inherited directly from Paper_093.

**Status: IDENTIFIED (direct inheritance, Paper_093 T18).**

### 3.3 Chirality $\chi_C$ as P09-valued phase difference

Both $\sigma_C(e_n)$ and $\sigma_K(\ell(e_n))$ are directed substrate-graph quantities at the same substrate locus. Under P09's $U(1)$-valued polarity assignment to substrate channels, each directional content has a corresponding P09 phase representation: $\pi_C(e_n) \in S^1$ for the chain-arrow direction, $\pi_K(\ell(e_n)) \in S^1$ for the kernel-arrow direction. These phase representations are well-defined per P09 + the channel-direction identification at locus $\ell(e_n)$.

Define **chain-arrow chirality at event $e_n$**:

$$
\boxed{\chi_C(e_n) := \pi_C(e_n) - \pi_K(\ell(e_n)) \pmod{2\pi}.}
$$

$\chi_C \in S^1$ is a P09-valued substrate-graph quantity at every P11 commitment event of $C$. It measures the phase relationship between the chain-arrow and the kernel-arrow at the chain's current locus.

**Special values:**
- $\chi_C = 0$: chain-arrow co-aligned with kernel-arrow ("aligned-tension" in ED-I-11 vocabulary).
- $\chi_C = \pi$: chain-arrow anti-aligned with kernel-arrow ("anti-aligned-tension").
- $\chi_C \in (0, 2\pi) \setminus \{0, \pi\}$: intermediate orientations.

**Status: IDENTIFIED (composition of P09 + chain-arrow + kernel-arrow content).** $\chi_C$ is operationally well-defined; the construction is at substrate-identification level per Paper_095 §2.3 (composition of upstream substrate-graph quantities under explicit identification).

### 3.4 Transport of $\chi_C$ along the chain

Between events $e_n$ and $e_{n+1}$, P05 polarity-transport carries $\pi_C$ along the chain edge per the chain's V1 propagation pattern. Simultaneously, the kernel-arrow at locus $\ell(e_{n+1})$ may differ from the kernel-arrow at $\ell(e_n)$ if the substrate-side kernel-arrow varies between loci (Paper_093 T18 allows kernel-arrow variation at scale $\gtrsim \ell_{V1}$).

The evolution of $\chi_C$ between commitment events is therefore:

$$
\chi_C(e_{n+1}) = \chi_C(e_n) + \Delta\pi_C^{P05}(e_n \to e_{n+1}) - \Delta\pi_K(\ell(e_n) \to \ell(e_{n+1})) \pmod{2\pi},
$$

where $\Delta\pi_C^{P05}$ is the P05-transported phase change along the chain edge and $\Delta\pi_K$ is the kernel-arrow phase change between successive loci.

In a regime where kernel-arrow is constant across loci ($\Delta\pi_K = 0$), $\chi_C$ evolves only by the P05 chain-transport content $\Delta\pi_C^{P05}$. If the chain-transport is itself trivial (P05 carries $\pi_C$ without rotation in the locally-homogeneous regime), then $\chi_C$ is conserved along the chain: $\chi_C(e_{n+1}) = \chi_C(e_n)$ for all $n$.

**Status:**
- Transport rule **IDENTIFIED** as a composition of P05 + Paper_093 content.
- Whether the transport is non-trivial in the general substrate regime (i.e., whether $\Delta\pi_C^{P05}$ or $\Delta\pi_K$ has substrate-graph derivable structure beyond the inherited content) is **OPEN**.
- The conservation property in the locally-homogeneous regime is **D-via-I** under §3.5 below.

### 3.5 Post-SCBU ignition regime: structural binary character

Per Paper_ED_CCC §3.6 + §3.7, the post-SCBU ignition regime has the following substrate-side properties (inherited):

(i) **Globally-coherent kernel-arrow.** Per Papers SC-4.x cross-scale invariance + curvature-moment collapse at the SCBU boundary: post-boundary substrate has no remaining local content to encode absolute phase orientation. The kernel-arrow $\sigma_K(\ell)$ is therefore globally coherent across cosmic-scale substrate — $\pi_K(\ell)$ is constant up to a global $U(1)$ choice. **$\Delta\pi_K = 0$ everywhere in this regime.**

(ii) **Chain-transport content trivial.** With no local substrate inhomogeneity, P05 carries $\pi_C$ without rotation along the chain. **$\Delta\pi_C^{P05} = 0$.**

(iii) **$\chi_C$ is therefore conserved** along the chain in the post-SCBU ignition regime: each chain carries a fixed $\chi_C$ value through its commitment sequence.

Under (i)–(iii), $\chi_C$ is a global $S^1$-valued quantity attached to each chain in the post-SCBU regime. It does not vary along the chain. **It does vary across chains in $S^1$ in principle**.

**The binary-character claim** (only $\chi_C \in \{0, \pi\}$ are admitted in this regime) requires an additional substrate-graph criterion: an admission filter selecting which $\chi_C$ values are compatible with Paper_072 individuation in the globally-coherent kernel-arrow regime.

Two possible admission criteria, both currently OPEN:

**Criterion-A (structural):** the globally-coherent kernel-arrow supplies the substrate with two structurally-distinguishable orientations (forward and reverse). Intermediate $\chi_C$ values require the substrate to encode a local phase orientation that the scale-collapsed substrate cannot supply — Paper_072 individuation fails for intermediate $\chi_C$ because chain-identity cannot be preserved across substrate loci that lack the local content to register intermediate orientation. Under Criterion-A, only $\chi_C \in \{0, \pi\}$ admits individuation.

**Criterion-B (V1/V5 finite-width):** V1's finite-width retarded kernel + V5 cross-chain correlations at intermediate $\chi_C$ require substrate slack (capacity beyond chain-admission demand) to maintain coherent propagation; in saturation, the slack is absent. Under Criterion-B, intermediate $\chi_C$ fail Paper_072 individuation for capacity reasons (not orientation reasons).

**Status of binary-character claim:**
- The conservation property along chains in this regime is **D-via-I** (composition of §3.4 + Paper_ED_CCC §3.6 / §3.7 + SC-4.x).
- The **selection of $\chi_C \in \{0, \pi\}$ over intermediate values** is **OPEN**: either Criterion-A or Criterion-B (or both) requires substrate-graph derivation.

This is the load-bearing OPEN structural content for any downstream baryogenesis paper. **It is what the eventual baryogenesis paper must close.** This memo does not attempt it.

---

## §4 IDENTIFIED vs OPEN

| Construction step | Status |
|---|---|
| Chain-arrow $\sigma_C(e_n)$ as directed substrate-graph edge | **IDENTIFIED** (P11 + Paper_089) |
| Kernel-arrow $\sigma_K(\ell)$ at substrate locus | **IDENTIFIED** (Paper_093 T18 inheritance) |
| Phase representations $\pi_C, \pi_K \in S^1$ | **IDENTIFIED** (P09 + channel-direction identification) |
| Chirality $\chi_C(e_n) := \pi_C - \pi_K \pmod{2\pi}$ | **IDENTIFIED** (composition under Paper_095 §2.3) |
| P05-transport rule for $\chi_C$ along chain | **IDENTIFIED** (P05 + Paper_093 composition) |
| Conservation of $\chi_C$ in post-SCBU regime ($\Delta\pi_C^{P05} = \Delta\pi_K = 0$) | **D-via-I** (composition of §3.4 + Paper_ED_CCC §3.6 + §3.7 + SC-4.x) |
| **Substrate-graph derivation that only $\chi_C \in \{0, \pi\}$ admit Paper_072 individuation in post-SCBU regime** | **OPEN (load-bearing)** |
| Substrate-graph derivation of Criterion-A (structural-orientation-based admission filter) | **OPEN** |
| Substrate-graph derivation of Criterion-B (V1/V5 capacity-based admission filter) | **OPEN** |
| Substrate-graph derivation that one of $\chi_C \in \{0, \pi\}$ is asymmetrically admitted vs the other | **OPEN** (this is the baryogenesis-specific construction; out of scope for this memo) |
| Substrate-graph derivation of $\chi_C$'s relation to standard QFT charge conjugation $C$ | **OPEN** (deferred to RQM-arc follow-up) |

**Items potentially derivable without ontology extension:** the conservation property (already D-via-I); Criterion-A or Criterion-B at the substrate-identification level; the chain-by-chain $\chi_C$ assignment in general substrate regimes.

**Items potentially requiring ontology extension:** none identified at the construction-memo level. Criterion-A and Criterion-B both appear constructible from existing P02 + P04 + P05 + P07 + P09 + Paper_072 + Paper_089 + Paper_090 + Paper_093 + SC-4.x content. **If neither closes** in a future construction attempt, the framework would need either (a) a paper-specific postulate or (b) ontology-level work.

**Compatibility with the modern architecture:** the construction sits cleanly within the post-Paper_072 / SC-series / SCBU / Paper_ED_CCC content. No primitives or postulates conflict.

---

## §5 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P02, P04, P05, P07, P09, P11, P13 | P | Paper_087. |
| 2 | V1 retarded kernel | I | Paper_089. |
| 3 | V5 cross-chain kernel | I | Paper_090. |
| 4 | Kernel-arrow $\sigma_K(\ell)$ at locus | I | Paper_093 T18. |
| 5 | Paper_072 individuation regime | I | Paper_072. |
| 6 | SC-4.x cross-scale invariance + curvature-moment collapse | I | Papers SC-4.x. |
| 7 | Post-SCBU substrate homogeneity + globally-coherent kernel-arrow | I | Paper_ED_CCC §3.6 + §3.7. |
| 8 | Chain-arrow $\sigma_C(e_n)$ as directed edge $(e_n \to e_{n+1})$ | **D-via-I** | Composition of P11 + Paper_089; §3.1. |
| 9 | P09 phase representations $\pi_C, \pi_K \in S^1$ | **D-via-I** | Composition of P09 + channel-direction identification; §3.3. |
| 10 | Chirality $\chi_C := \pi_C - \pi_K \pmod{2\pi}$ | **D-via-I** | Composition of rows 8 + 9; §3.3. **Operational substrate-graph definition delivered.** |
| 11 | $\chi_C$ transport rule along chain (P05 + kernel-arrow variation) | **D-via-I** | Composition of P05 + Paper_093; §3.4. |
| 12 | $\chi_C$ conservation in post-SCBU regime ($\Delta\pi_K = 0$, $\Delta\pi_C^{P05} = 0$) | **D-via-I** | Composition of §3.4 + rows 6 + 7; §3.5. |
| 13 | $\chi_C \in S^1$ in general regimes; chain-attached quantity in post-SCBU regime | **D-via-I** | Composition of rows 10 + 12. |
| 14 | Substrate-graph admission filter selecting $\chi_C \in \{0, \pi\}$ in post-SCBU regime | **OPEN (load-bearing)** | Either Criterion-A (structural) or Criterion-B (V1/V5 capacity) required; §3.5. |
| 15 | Substrate-graph derivation that one of $\{0, \pi\}$ is asymmetrically admitted | **OPEN** | Out of scope for this memo; deferred to baryogenesis-arc generative paper. |
| 16 | $\chi_C$ relation to standard QFT charge-conjugation $C$ | **OPEN** | Deferred to RQM-arc follow-up. |
| 17 | Verdict: chirality is OPERATIONALLY DEFINED as substrate-graph quantity; binary character + admission filter OPEN | **A→position** | Per Paper_095 §3.3. |

**Zero pure-D rows.** Operational substrate-graph definition of $\chi_C$ is delivered at D-via-I (composition of upstream content under substrate identification). The two load-bearing OPEN items (rows 14, 15) name the substrate-graph derivations required for a baryogenesis paper to be feasible.

---

## §6 Falsification Criteria

- **F1:** Empirical or substrate-graph evidence that chain identity is not preserved under P09-valued phase transport along chain edges in any regime — refutes the construction at row 11 (the chirality is not a transportable quantity).

- **F2:** Substrate-graph evidence that the kernel-arrow $\sigma_K(\ell)$ is not globally coherent in the post-SCBU ignition regime — refutes the conservation property at row 12 and undermines the binary-character claim.

- **F3:** Substrate-graph derivation showing that Paper_072 individuation criterion is satisfied for $\chi_C \in S^1$ uniformly (all chiralities admissible, not just $\{0, \pi\}$, in the post-SCBU regime) — refutes both Criterion-A and Criterion-B simultaneously. **This is the framework-killing test for any downstream baryogenesis paper.**

- **F4:** Substrate-graph derivation showing that V1 + V5 + Paper_072 individuation admit a finer chirality structure ($\chi_C \in \{0, 2\pi/3, 4\pi/3\}$ or similar discrete-but-non-binary structure) in the post-SCBU regime — would require revising the binary-character claim and the eventual baryogenesis architecture.

- **F5:** Discovery that the chain-arrow $\sigma_C$ and kernel-arrow $\sigma_K$ do not share a common P09 phase representation at substrate-graph level — refutes the construction at row 9 (the chirality is not well-defined as a phase difference) and would force ontology-level reconsideration of P09's role.

---

## §7 Verdict + Recommended Next Steps

**Verdict per Paper_095:** **operational substrate-graph definition of $\chi_C$ DELIVERED at D-via-I level** (composition of P09 + P11 + P05 + Paper_089 + Paper_093 + Paper_072 + SC-4.x + Paper_ED_CCC §3.7 under substrate identification). **No new primitives. No new postulates.** Verdict for this memo: **M3 (form-IDENTIFIED + value-INHERITED)** at the construction level — the substrate-graph quantity is operationally defined; the binary-character + admission-filter content is OPEN (rows 14, 15).

**What this memo enables for downstream papers:**
- Any downstream paper invoking chain-arrow chirality can cite **this memo** as the operational definition.
- The conservation property (row 12) is usable as inherited content for any downstream paper restricted to the post-SCBU regime.
- The OPEN items (rows 14, 15) are named here; downstream papers carrying them must flag the same OPEN status.

**Recommended next steps:**
1. **Attempt the row-14 closure** (substrate-graph derivation of admission filter selecting $\chi_C \in \{0, \pi\}$). Either Criterion-A (structural orientation) or Criterion-B (V1/V5 capacity) is a candidate; both are substrate-graph constructions deferred to follow-up work. Closing row 14 is the next prerequisite for the baryogenesis-arc generative paper.
2. **Hold row 15** (asymmetric admission of one of $\{0, \pi\}$ over the other) for the baryogenesis-arc generative paper itself; this is the baryogenesis-specific structural derivation and is appropriate to attempt only after row 14 closes.
3. **Defer row 16** (relation of $\chi_C$ to standard QFT $C$ conjugation) to an RQM-arc follow-up; this is the bridge between substrate chirality and Standard-Model charge conjugation and is not load-bearing for the baryogenesis-arc paper.

**Compatibility check.** The construction is consistent with: Paper_072 (individuation regime); Papers SC-4.x (scale-collapse); Paper_028 + SCBU; Paper_089/090 (V1/V5 kernels); Paper_093 (kernel-arrow T18); Paper_ED_CCC §3.6 / §3.7 (post-boundary kernel-arrow homogeneity). No conflicts with primitives or upstream postulates identified.

**Cosmology-arc placement.** Chain-arrow chirality is structurally placed as a P09-valued chain-attached quantity that becomes a globally-relevant binary structure in the post-SCBU ignition regime. The construction inherits its cosmic-scale relevance from Paper_ED_CCC §3.7 + SC-4.x; it has no cosmic-scale relevance outside that regime in current substrate content (general-regime $\chi_C$ is a continuous chain-attached quantity with no global structure).

---

**End Memo_ED_ChainArrowChirality.**
