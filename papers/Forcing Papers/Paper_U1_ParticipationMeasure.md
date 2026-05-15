# Paper U1 — Participation Measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$ as Amplitude Carrier

**Series:** Wave-3 U-Series (Phase-1 Schrödinger Program, sub-result U1)
**Status:** Wave-3 generative paper; M3 verdict at write-time
**Companions:** Paper_002 (Born-Gleason), Paper_008 (Phase Structure), Paper_063 (E-1 tensor product), Paper_087.

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of the complex-valued participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$ from nothing. Result is conditional on the 13 ED primitives (Paper_087) + declared paper-specific postulates.
2. It does **not** claim closed-proof reconstruction in the Hardy 2001 / CDP 2011 / Coecke-Kissinger operational-reconstruction sense. ED sits in the substrate-ontology lineage ('t Hooft cellular-automaton, Wolfram Ruliad, causal-set), not the operational-reconstruction lineage.
3. It does **not** override Paper_095's three-tier verdict grammar. Verdict for this paper is stated in §1.
4. It does **not** claim derivation of the bandwidth measure $b_K$ itself from sub-primitive structure, nor derivation of specific motif-by-motif numerical values of $b_K$ or $\pi_K$.
5. The **complex-valued form** $P_K = \sqrt{b_K}\,e^{i\pi_K}$ is FORM-FORCED by P04 + P05 + P09 + interference requirement; the **numerical values** $b_K$ and $\pi_K$ per substrate motif are INHERITED via substrate-configuration content.

## Abstract

This paper supplies the substrate-level form of the QM amplitude carrier: the participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K} \in \mathbb{C}$ assigned to each substrate motif $K$, with magnitude $\sqrt{b_K}$ (P04 bandwidth content) and phase $\pi_K$ ($U(1)$ polarity per P09 + P05 polarity-transport). The complex-valued form is FORM-FORCED by three independent arguments — interference requirement under tensor-product composition (Paper_063 E-1), Born-rule structure (Paper_002), and polarity-transport content — while specific numerical $b_K, \pi_K$ values per motif are INHERITED. Verdict per Paper_095: **M3** at write-time. Key falsifier line: **F1** (substrate-level evidence that participation measure is real-valued only would refute the complex-valued claim and predict no continuous interference fringes).

---

## §1 Statement of Result

**Claim.** The substrate-level participation measure assigned to motif (substrate configuration) $K$ takes the form
$$P_K = \sqrt{b_K}\, e^{i\pi_K} \in \mathbb{C} ,$$
where $b_K \geq 0$ is the non-negative real P04 bandwidth content (so the amplitude magnitude is $\sqrt{b_K}$) and $\pi_K \in [0, 2\pi)$ is a $U(1)$-valued phase (P09 polarity content). $|P_K|^2 = b_K$ matches the Born rule (Paper_002): modulus-squared equals bandwidth content. $P_K$ is **complex-valued** by structural necessity: real-valued or positive-real participation measures would fail to produce interference phenomena and would not support the substrate-level analog of the Born rule (Paper_002).

The complex-valued participation measure is FORM-FORCED by P04 (bandwidth) + P09 ($U(1)$ polarity) + P05 (polarity-transport) + interference requirement under tensor-product composition (Paper_063 E-1). Numerical values $b_K$ and $\pi_K$ per specific motif are INHERITED via substrate-configuration content.

**Convention sync (Paper_002):** amplitude is $\sqrt{b_K}$, modulus-squared is $b_K$ (matches Born rule = bandwidth content). Earlier drafts of this paper carried $P_K = b_K e^{i\pi_K}$ giving $|P_K|^2 = b_K^2$; that is corrected here.

Verdict: **M3**.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P04 (Bandwidth)** — supplies the non-negative real amplitude content $b_K$.
- **P05 (Polarity-transport)** — supplies the substrate mechanism by which phase $\pi_K$ accumulates.
- **P09 ($U(1)$-valued polarity)** — supplies the $U(1)$ target group for $\pi_K$.
- **P10 (Rule-type primitive)** — supplies the motif structure on which $P_K$ is defined.

### 2.2 Upstream Dependencies

- **I-002:** Born-Gleason rule (Paper_002) — probability is $|P_K|^2$, requiring complex $P_K$.
- **I-008:** Phase structure on rule-types (Paper_008) — $S^1$ polarity propagation.
- **I-063:** Tensor-product composition (Paper_063, E-1) — composite-motif amplitude structure.
- **I-RQM-T8:** Canonical (anti-)commutation relations.
- **I-Interference:** Standard QM interference / superposition machinery.

---

## §3 Derivation

### 3.1 Substrate-level amplitude and phase from P04 + P09

Each substrate motif $K$ (a specific substrate-configuration class) is characterized by two structural features:
1. **Bandwidth content $b_K \geq 0$:** the P04-additive scalar measuring how much substrate participation supports the motif. Empty motifs have $b_K = 0$; populated motifs have $b_K > 0$.
2. **Phase content $\pi_K \in [0, 2\pi)$:** the $U(1)$-valued polarity (P09) accumulated by the motif's edge-content under P05 polarity-transport.

The natural substrate-level "measure" assigned to motif $K$ is the combination
$$P_K = \sqrt{b_K}\cdot e^{i\pi_K} \in \mathbb{C} .$$

This is the participation measure: a complex number with non-negative magnitude $|P_K| = \sqrt{b_K}$ and phase $\arg(P_K) = \pi_K$. Then $|P_K|^2 = b_K$ — the Born-rule probability equals the bandwidth content.

### 3.2 Why complex-valued, not real-valued

Three independent arguments force complex-valuedness:

**(A) Interference requirement.** Under tensor-product composition (Paper_063 E-1), the composite participation measure for two independent motifs $K_1$ and $K_2$ is
$$P_{K_1 \cup K_2} = P_{K_1} \cdot P_{K_2} \quad \text{(if independent)} ,$$
or a superposition
$$P_{\mathrm{composite}} = \alpha P_{K_1} + \beta P_{K_2} \quad \text{(if superposed)} .$$

For the superposition to produce **interference** (constructive or destructive depending on relative phase), the participation measure must carry phase information. Real-valued $P_K$ would allow only $\pm$ signs (no continuous phase), giving at most a binary interference pattern — incompatible with empirical QM (continuous-phase interference fringes).

**(B) Born rule structure.** Paper_002 derives the Born rule: probability of motif $K$ is $|P_K|^2 = b_K$. For probability to be non-negative real, $|P_K|^2 = b_K \geq 0$ requires only that $|P_K|$ be real (i.e., $P_K$ can be complex of arbitrary phase). If $P_K$ were restricted to real, $|P_K|^2$ would be the same magnitude, but the phase information would be absent for interference computations.

**(C) Polarity-transport structure.** P05 polarity-transport along edges accumulates polarity rotation. Under P09 ($U(1)$-valued polarity), the accumulated polarity is naturally $U(1)$-valued, i.e., $e^{i\pi_K}$. Real-valued participation measure would discard the polarity-rotation content, throwing away substrate-derivable structure.

Together, (A) + (B) + (C) force $P_K \in \mathbb{C}$.

### 3.3 What $\pi_K$ encodes structurally

The phase $\pi_K$ is the accumulated polarity rotation along the substrate-edge content underlying motif $K$. Specifically:
$$\pi_K = \int_{\partial K} A_\mu \, dx^\mu \pmod{2\pi} ,$$
where the integral is over the substrate-edge content of $K$ and $A_\mu$ is the (effective, possibly gauge) connection one-form (per T17, Paper_015).

Key implications:
- **Adjacency-bandwidth content** (P03 + P04): the phase accumulation depends on the specific channels and loci traversed.
- **Path dependence:** different paths underlying the same motif endpoints can yield different $\pi_K$ — this is the substrate origin of the Aharonov–Bohm phase (Paper_010).
- **Topological structure:** for closed-loop motifs, $\pi_K$ becomes the holonomy of the substrate connection (Berry phase, Paper_009).

### 3.4 Adjacency-bandwidth structure encoded in $\pi_K$

The adjacency content of substrate motif $K$ — which channels are connected to which neighboring channels via P03 locus indexing — directly determines $\pi_K$. Different adjacency patterns produce different phase accumulations because:
- Each substrate edge contributes a polarity-rotation increment.
- The total rotation depends on which edges are included in motif $K$.
- P04 bandwidth-additivity ensures each edge contributes consistently.

This is the substrate-level structural content of "phase information encodes path / configuration / adjacency content," which standard QM treats axiomatically but is here derivable from P03 + P04 + P05 + P09.

### 3.5 Composition rules for $P_K$

Multi-motif amplitudes follow standard QM composition rules:

**Independent motifs (tensor product):**
$$P_{K_1 \otimes K_2} = P_{K_1} \cdot P_{K_2} .$$

**Superposed motifs (linear combination):**
$$P_{K} = \sum_i \alpha_i \, e^{i\pi_i} P_{K_i} ,$$
with $\alpha_i$ amplitudes and $e^{i\pi_i}$ relative phases.

These composition rules are inherited from tensor-product structure (Paper_063) and standard QM superposition (downstream of Phase-1 QM emergence).

### 3.6 Connection to Born rule and probability

Probability of motif $K$ occurring under measurement is (Paper_002 Born-Gleason):
$$\text{Prob}(K) = |P_K|^2 = b_K .$$

This is the substrate-level Born rule. The complex-valued $P_K$ supports interference effects between motifs; the modulus-squared extracts the probability. Phase information is **operationally inaccessible** to single-outcome measurements but **operationally accessible** via interference experiments.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P04 bandwidth | P | Primitive. |
| 2 | P05 polarity-transport | P | Primitive. |
| 3 | P09 $U(1)$ polarity | P | Primitive. |
| 4 | P10 rule-type primitive | P | Primitive. |
| 5 | Motif $K$ has bandwidth content $b_K \geq 0$ (from P04) | D | From P04. |
| 6 | Motif $K$ has phase content $\pi_K \in [0, 2\pi)$ (from P05 + P09) | D | From P05 + P09. |
| 7 | $P_K = \sqrt{b_K}\,e^{i\pi_K}$ definition | D | Composition. Convention sync with Paper_002: amplitude is $\sqrt{b_K}$, modulus-squared is $b_K$ (matches Born rule = bandwidth content). |
| 8 | Interference requirement forces complex $P_K$ | D-via-I | Standard QM interference. |
| 9 | Born rule structure (Paper_002) supports complex $P_K$ | I | Paper_002. |
| 10 | Polarity-transport content forces phase content | D | From P05 + P09. |
| 11 | $\pi_K$ as integral of connection one-form | D-via-I | T17 + standard math. |
| 12 | Tensor-product composition rule | I | Paper_063 (E-1). |
| 13 | Specific $b_K$, $\pi_K$ values per motif | I | Substrate configuration content. |
| 14 | Probability $|P_K|^2 = b_K$ (Born) | I | Paper_002. |
| 15 | Verdict M3 | A→position | Per Paper_095. |

---

## §5 Falsification Criteria

- **F1: Substrate-level evidence that participation measure is real-valued only.** Would refute the complex-valued claim. Empirically: interference experiments (double-slit, Mach-Zehnder, etc.) would not produce continuous fringe patterns.

- **F2: Empirical detection of QM interference NOT consistent with $|P_K|^2$ probability rule.** Would propagate from Paper_002 falsifier.

- **F3: Substrate evidence that $\pi_K$ does NOT depend on substrate adjacency content.** Would refute the structural encoding of adjacency in phase.

- **F4: $P_K$ decomposition into $b_K \cdot e^{i\pi_K}$ shown to be unstable** (different decompositions yield different observables). Would refute the canonical form.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), **not** within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

This paper supplies the substrate-level form of the participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$ as the amplitude carrier for ED's substrate-level QM emergence.

**Relationship to other papers:**
- **Paper_002 (Born-Gleason):** $|P_K|^2$ probability rule depends on this amplitude form.
- **Paper_008 (Phase structure):** supplies $\pi_K$'s $S^1$ structure.
- **Paper_063 (E-1 tensor product):** supplies composition rule for $P_K$.
- **Papers U2–U5:** build on this amplitude form for inner-product + Schrödinger.

**Numerical content INHERITED.** Specific $b_K$, $\pi_K$ per substrate motif. **Form FORCED.** Complex-valued participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$.

**Future work.** Substrate-level computation of $\pi_K$ from substrate adjacency-bandwidth content for canonical motif classes; substrate audit of QFT path-integral phase as integrated chain-step participation phase.

Verdict: **M3**.

---

**End Paper U1.**
