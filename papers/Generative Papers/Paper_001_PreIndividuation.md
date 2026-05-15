# Paper_001 — Pre-Individuation Amplitudes from P01–P04

**Series:** Event Density (ED) Generative Papers — Wave-2 QM-kinematics arc (upstream anchor)
**Author:** Allen Proxmire
**Status:** Publication draft (upstream of Paper_003 Born rule)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/qm-kinematics/Paper_001_PreIndividuation.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System.

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 primitives are not derived** (Paper_087).
2. **No claim that complex-valued amplitudes are forced from P01–P04 alone.** The complex polar carrier $P_K = \sqrt{b_K}\,e^{i\pi_K}$ is derived under P01–P04 + P09 ($U(1)$-valued polarity) jointly. Without P09, only the real-valued $b_K$ structure follows; the angular structure $\pi_K \in U(1)$ requires P09 as load-bearing.
3. **No claim that the Born rule is in this paper.** Paper_003 supplies the participation-frequency-limit derivation downstream; this paper supplies the *amplitude structure* on which Paper_003 operates.
4. **No claim of Hilbert-space emergence.** Paper_007 supplies that downstream (completion of motif algebra).
5. **No claim of derivation of the inner-product / sesquilinear-bilinear form.** Paper #3 (pre-pivot inner product + Tsirelson) inherits the sesquilinear structure; this paper provides amplitude content on which the inner product operates.
6. **No claim that pre-individuation amplitudes have direct empirical-observable status.** Pre-individuation amplitudes are substrate-level content; empirical observables emerge post-commitment via the Born-rule mechanism (Paper_003).

---

## Abstract

This paper develops **pre-individuation amplitudes** as the substrate-level participation structure preceding commitment events, from primitives P01 (chains as primitive ontological objects), P02 (participation), P03 (channel + locus indexing + spatial homogeneity), and P04 (bandwidth as non-negative additive scalar). Given P01–P04 + P09 ($U(1)$-valued polarity), the substrate-level participation content at each (chain, channel, locus) tuple is captured by the **complex polar carrier**:

$$
P_K^C(u, t) = \sqrt{b_K^C(u, t)}\,e^{i\pi_K^C(u, t)}
$$

where $b_K^C \geq 0$ is the substrate-level bandwidth (P04) and $\pi_K^C \in U(1)$ is the substrate-level polarity (P09). The complex polar carrier is the substrate-level analog of a quantum-mechanical amplitude — *before* commitment events have selected single-channel content (P11). This is the **pre-individuation** structure on which the Born-rule participation-frequency-limit (Paper_003) and the Hilbert-space completion (Paper_007) operate.

The substrate-level identifications: amplitude magnitude $|P_K|^2 = b_K$; amplitude phase $\arg P_K = \pi_K$. Under commitment (P11), the complex polar structure collapses to single-channel content, with selection statistics governed by P-LinRate (Paper_003) producing the Born-rule frequency limit $f_K = |c_K|^2$.

The paper makes no claim of derivation of complex Hilbert space (Paper_007 downstream), no claim of derivation of the Born rule (Paper_003 downstream), no claim of derivation of the inner-product structure (Paper #3 inheritance), and no claim that complex-valued amplitudes are forced from P01–P04 alone — P09 is load-bearing for the angular structure.

---

## 1. Introduction

### 1.1 What this paper does

This paper supplies the **upstream anchor** for the ED QM-kinematics arc: the substrate-level pre-individuation amplitude structure on which Paper_003 (Born rule) and Paper_007 (Hilbert-space emergence) operate. The paper:

1. States substrate-level participation content carriers from P01–P04 + P09.
2. Derives the complex polar carrier $P_K^C = \sqrt{b_K^C}\,e^{i\pi_K^C}$.
3. Specifies the pre-individuation regime (before P11 commitment events).
4. Connects to downstream Paper_003 (Born rule from participation-frequency limit).

### 1.2 Why "pre-individuation"

"Individuation" refers to substrate-level commitment events (P11) at which a chain's multi-channel participation collapses to single-channel content. **Pre-individuation amplitudes** are the substrate-level structure *before* any commitment has occurred — the substrate-level analog of a quantum state in superposition before measurement.

The pre-individuation amplitude structure is the substrate-level carrier of "amplitude content" in the standard quantum-mechanical sense, but encoded at the substrate-graph level (chains + channels + bandwidth + polarity) rather than in a Hilbert-space arena (which emerges via Paper_007).

### 1.3 Arc context

- **Paper_001 (this paper):** Pre-individuation amplitudes from P01–P04 + P09. **Upstream anchor.**
- **Paper_002 (in queue):** Tensor-product composition from P02 + P03.
- **Paper_003:** Born rule from participation-frequency limit (uses this paper).
- **Paper_007:** Hilbert-space emergence as completion of motif algebra (uses this paper).
- **Papers_004–006, 008–012 (in queue):** Gleason, projective measurement, unitary evolution, phase structure, Berry, AB, Bloch, P-RB-1.

---

## 2. Primitive Inputs

**Substrate primitives (postulated, Paper_087):**

- **P01 (Chains as primitive ontological objects).** Forward-causal substrate sequences. **Load-bearing.**
- **P02 (Participation).** Chain-channel relation.
- **P03 (Channel + locus indexing + spatial homogeneity).** Discrete index sets.
- **P04 (Bandwidth as non-negative additive scalar).** Substrate-level scalar carrier of participation amount.
- **P09 ($U(1)$-valued polarity).** **Load-bearing for angular/complex structure.**

**Upstream paper dependencies:**

- **Paper_087:** position paper.
- (No prior Wave-2 papers — this is an upstream anchor for the QM-kinematics arc.)

**Empirical / value-layer inputs:** none required at this paper's level (substrate-level structure only; numerical values inherited at downstream papers).

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| Chains are forward-causal substrate sequences (P01) | P | Paper_087 §5.1 |
| Participation relation between chains and channels (P02) | P | Paper_087 §5.2 |
| Channel set $\mathcal{K}$ + locus set indexed discretely (P03) | P | Paper_087 §5.3 |
| Bandwidth $b_K^C(u, t) \geq 0$ as substrate scalar (P04) | P | Paper_087 §5.4 |
| Polarity $\pi_K^C(u, t) \in U(1)$ (P09) | P | Paper_087 §5.9 |
| Bandwidth additivity under channel decomposition | P | P04 |
| Complex polar carrier $P_K^C = \sqrt{b_K^C}\,e^{i\pi_K^C}$ as canonical substrate-level participation amplitude | **D** | §3.2 from joint substrate-level structure of $b_K$ and $\pi_K$ — bandwidth magnitude + $U(1)$ phase combine to a single complex variable via square-root-amplitude convention. |
| Identification $|P_K|^2 = b_K$ | D | §3.3 explicit algebra: $|P_K|^2 = |\sqrt{b_K}|^2 \cdot |e^{i\pi_K}|^2 = b_K \cdot 1 = b_K$ |
| Identification $\arg(P_K) = \pi_K$ | **P (definition)** | §3.3 — definitional consequence of $P_K = \sqrt{b_K}\,e^{i\pi_K}$ construction; tautological from the polar-form definition itself, not an algebraic derivation |
| Gauge-covariance under $U(1)$ polarity-transport: $P_K^C \to P_K^C\,e^{i\alpha(u)}$ | D | §3.4 explicit algebra: $P_K^C = \sqrt{b_K^C}\,e^{i\pi_K^C} \to \sqrt{b_K^C}\,e^{i(\pi_K^C + \alpha)} = P_K^C\,e^{i\alpha}$ under P05 polarity-transport gauge transformation |
| Substrate-level multi-channel coherent state $\Psi^C = \sum_K P_K^C |K\rangle$ in motif-algebra form | **P (motif-algebra placeholder definition)** | §4.1 — definitional: we define the multi-channel state as the formal sum over channels; full motif-algebra structure + Hilbert-space completion is Paper_007 territory; this row is definitional, not algebraic |
| Pre-individuation regime (before P11 commitment) | P (definition) | §4.2 substrate-level definitional choice |
| Square-root-amplitude convention (rather than $b_K$ directly) | **P (convention)** | §3.2 substrate-level convention — alternative ($P_K = b_K \cdot e^{i\pi_K}$ with magnitude $b_K$) would give a different relationship to Born rule; the square-root convention reproduces standard QM under Paper_003 frequency limit + Paper #1 participation-measure identification. |

All rows P, D, or labeled. **No A (asserted) rows. No banned-phrase patterns.**

---

## 3. The Complex Polar Carrier

### 3.1 Substrate-level participation content

A chain $C$ at substrate locus $u$ at substrate time $t$ participates in channels $K \in \mathcal{K}$ with substrate-level content:

- **Bandwidth content:** $b_K^C(u, t) \geq 0$, non-negative additive substrate scalar (P04).
- **Polarity content:** $\pi_K^C(u, t) \in U(1) \cong [0, 2\pi)$, substrate-level angular variable (P09).

These two are the substrate-level participation content per (chain, channel, locus, time) tuple. Together they constitute the substrate-level amplitude carrier.

### 3.2 The complex polar carrier — derivation

The substrate-level bandwidth $b_K$ and polarity $\pi_K$ combine naturally into a **complex polar carrier**:

$$
P_K^C(u, t) = \sqrt{b_K^C(u, t)} \cdot e^{i\pi_K^C(u, t)}.
$$

**Where the square-root convention comes from:** the substrate-level identification $|P_K|^2 = b_K$ is the structurally-natural choice that makes the Born-rule downstream derivation (Paper_003) reproduce empirical QM. Specifically:

- Under participation-frequency-limit (Paper_003): $f_K = b_K/\sum b_{K'}$.
- Under empirical Born rule: $P(K) = |c_K|^2$ where $c_K$ is the QM amplitude.
- The match $f_K = |c_K|^2$ requires the identification $b_K = |c_K|^2$, which in polar form gives $c_K = \pm\sqrt{b_K}\,e^{i\pi_K} = P_K$ (sign conventionally positive).

The square-root convention is therefore the **substrate-level convention** (P-convention in audit table) that makes the substrate→QM identification work. Alternative conventions ($P_K = b_K\,e^{i\pi_K}$) would give a non-Born downstream limit and are inconsistent with empirical QM.

**Honest framing:** the square-root-amplitude is a substrate-level convention; together with P-LinRate (Paper_003 substrate-level commitment-rate linear in bandwidth) and the frequentist interpretation, it reproduces the empirical Born rule. The convention is structurally distinct from the empirical Born rule itself.

### 3.3 Algebraic identifications

From $P_K = \sqrt{b_K}\,e^{i\pi_K}$:

- $|P_K|^2 = (\sqrt{b_K})^2 \cdot |e^{i\pi_K}|^2 = b_K \cdot 1 = b_K$.
- $\arg(P_K) = \pi_K \in U(1)$.
- $P_K$ has substrate-level units of $\sqrt{\mathrm{bandwidth}}$.

**Dimensional check:** $b_K$ has substrate-level bandwidth units (dimensionless in normalized substrate-amplitude convention; otherwise inherits substrate-level scaling from P04); $\sqrt{b_K}$ has units of $\sqrt{\mathrm{bandwidth}}$. ✓

### 3.4 Gauge-covariance under P05 polarity-transport

Under $U(1)$ gauge transformations $\pi_K^C(u) \to \pi_K^C(u) + \alpha(u)$ (per P05 polarity-transport):

$$
P_K^C(u) \to P_K^C(u) \cdot e^{i\alpha(u)}.
$$

The complex polar carrier transforms covariantly under $U(1)$ gauge — the substrate-level gauge structure inherited from P05 + P09. This is the substrate-level basis for gauge-coupled QM (downstream via T17 / Paper_015).

---

## 4. Pre-Individuation Multi-Channel State

### 4.1 Multi-channel substrate-level state

A chain $C$ participating in multiple channels simultaneously at substrate locus $(u, t)$ has substrate-level multi-channel state captured by the collection $\{P_K^C(u, t)\}_{K \in \mathcal{K}}$. In motif-algebra form (Paper_007 in queue):

$$
\Psi^C(u, t) = \sum_K P_K^C(u, t)\,|K\rangle
$$

where $|K\rangle$ is the substrate-level basis ket for channel $K$. (This is the substrate-level analog of a quantum-state expansion in a basis; the Hilbert-space structure on $\{|K\rangle\}$ is Paper_007 territory.)

### 4.2 The pre-individuation regime

The **pre-individuation regime** is the substrate-level regime *before* any commitment events have occurred for chain $C$:

- All bandwidth content $b_K^C(u, t) \geq 0$ is potentially non-zero.
- All polarity content $\pi_K^C(u, t) \in U(1)$ is well-defined.
- The chain participates *coherently* in multi-channel content (no commitment selection has occurred).

This is the substrate-level analog of "quantum superposition" — a chain's substrate-level participation is distributed across multiple channels with well-defined complex amplitudes.

### 4.3 Transition to post-individuation via commitment (P11)

At a commitment event (P11), the chain's multi-channel content collapses to single-channel content:

- Pre-commitment: $\Psi^C = \sum_K P_K^C\,|K\rangle$ (multiple non-zero $P_K^C$).
- Commitment event at $t = t_{\mathrm{commit}}$: substrate-level selection of channel $K^*$ with substrate-level rate $\propto b_{K^*}$ (P-LinRate, Paper_003).
- Post-commitment: $\Psi^C(t > t_{\mathrm{commit}}) = P_{K^*}^C\,|K^*\rangle$ (single channel; un-selected channels' phase content randomized per P11).

The transition pre-individuation → post-individuation is **discrete and irreversible** (P11). Downstream:

- Paper_003 supplies the substrate-level participation-frequency-limit mechanism producing the Born rule.
- Paper_007 supplies the Hilbert-space completion on which the pre-individuation amplitude content lives.

---

## 5. Connecting to Downstream Papers

### 5.1 Paper_003 (Born rule)

Paper_003 uses the pre-individuation amplitude structure of this paper + P-LinRate (substrate-level commit-rate linear in bandwidth) + frequentist interpretation of substrate-level frequencies to derive the Born rule:

$$
f_K = |P_K|^2 = b_K \quad \text{(normalized)}.
$$

This paper supplies the **amplitude carrier** $P_K$; Paper_003 supplies the **selection statistics**.

### 5.2 Paper_002 (tensor-product, in queue)

Paper_002 will derive tensor-product composition of pre-individuation amplitude content across multiple chains, from P02 + P03. This is the substrate-level basis for multi-system quantum-mechanical content.

### 5.3 Paper_007 (Hilbert-space emergence)

Paper_007 will derive the Hilbert-space completion: motif-algebra structure on $\{P_K\}$ + sesquilinear inner product (Paper #3 inheritance) → Cauchy completion → Hilbert space. The pre-individuation amplitude content of this paper is the substrate-level content that the Hilbert space contains.

### 5.4 Paper_015 (T17 gauge fields)

The complex polar carrier's $U(1)$ gauge-covariance (§3.4) is the substrate-level basis for T17 gauge-rule-type bundles (Paper_015). Pre-individuation amplitude content carries the gauge phase; gauge fields emerge as DCGT coarse-graining of polarity-transport structure.

---

## 6. Falsification Criteria

### 6.1 Complex amplitude structure not required at substrate level

**Falsifier sentence:** *Demonstration that substrate-level participation content can be captured by real-valued amplitudes alone — without the $U(1)$ angular structure of P09 + the complex polar combination — and still reproduce empirical quantum-mechanical phenomena (interference, gauge-coupled Berry phase, Aharonov–Bohm) — would falsify the §3 complex-polar-carrier derivation.*

### 6.2 Square-root-amplitude convention is not the empirically-correct convention

**Falsifier sentence:** *Empirical demonstration that an alternative substrate-level amplitude convention ($P_K = b_K\,e^{i\pi_K}$ with magnitude $b_K$; or $P_K = b_K^{1/3}\,e^{i\pi_K}$, etc.) reproduces empirical quantum mechanics under the downstream Paper_003 frequency-limit + Paper_007 Hilbert-space emergence — better than the square-root convention — would falsify the §3.2 substrate-level convention choice.*

### 6.3 Pre-individuation regime not empirically realized

**Falsifier sentence:** *Empirical demonstration that quantum-mechanical "superposition" is not the substrate-level pre-individuation regime — i.e., that empirical superposition has non-substrate-level character not captured by multi-channel participation content — would falsify the §4 pre-individuation framework.*

### 6.4 P09 ($U(1)$-valued polarity) is not load-bearing

**Falsifier sentence:** *Demonstration that the substrate-level participation content can be derived from P01–P04 alone — without P09's $U(1)$-valued polarity — and still produce the complex polar carrier structure — would falsify the §3.2 P09-load-bearing claim. Conversely: demonstration that P09 implies non-$U(1)$ structure (e.g., higher-rank groups at primitive level) would force revision of P09.*

### 6.5 Multi-channel pre-individuation incompatible with P03 spatial homogeneity

**Falsifier sentence:** *Demonstration that pre-individuation amplitude content cannot consistently coexist with P03's substrate-graph spatial homogeneity at all loci — i.e., translation-invariance breaks for pre-individuation states — would falsify the §4 substrate-level pre-individuation framework.*

---

## 7. Position Statement

**Pre-individuation amplitudes** are the substrate-level participation structure preceding commitment events, captured by the complex polar carrier:

$$
\boxed{P_K^C(u, t) = \sqrt{b_K^C(u, t)}\,e^{i\pi_K^C(u, t)}}
$$

derived from P01–P04 + P09 + square-root-amplitude convention.

What this paper claims:

- The complex polar carrier is the substrate-level analog of a quantum-mechanical amplitude.
- Identifications $|P_K|^2 = b_K$ and $\arg(P_K) = \pi_K$ are substrate-level algebraic consequences.
- The pre-individuation regime is the substrate-level "before commitment" regime; multi-channel coherent participation lives here.
- Gauge-covariance under $U(1)$ inherits from P05 + P09; substrate-level basis for downstream gauge content.

What this paper does *not* claim:

- The 13 primitives are not derived.
- Complex amplitudes are not forced from P01–P04 alone; P09 is load-bearing.
- Born rule is not in this paper (Paper_003 downstream).
- Hilbert space is not in this paper (Paper_007 downstream).
- Square-root-amplitude convention is a substrate-level convention, not derived from primitives alone.
- Inner-product structure not derived (Paper #3 inheritance).

**Series context.** Paper_001 of QM-kinematics arc. Upstream anchor for Papers_002 (tensor product), 003 (Born rule), 004 (Gleason), 005 (projection), 006 (unitary evolution), 007 (Hilbert space), 008–012 (phase, Berry, AB, Bloch, P-RB-1).

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Paper_087:** position paper.
- **Paper_003:** Born rule from participation-frequency limit.
- **Paper_007:** Hilbert-space emergence.
- **Paper_015:** T17 gauge fields.
- **Paper #3 (pre-pivot):** inner product + Tsirelson.

### Glossary

- **Pre-individuation amplitude.** Substrate-level participation content before commitment events; complex polar carrier $P_K^C = \sqrt{b_K^C}\,e^{i\pi_K^C}$.
- **Complex polar carrier $P_K$.** Substrate-level participation amplitude with magnitude $\sqrt{b_K}$ and phase $\pi_K \in U(1)$.
- **Square-root-amplitude convention.** Substrate-level convention $|P_K|^2 = b_K$; required for reproducing Born rule downstream.
- **Pre-individuation regime.** Substrate-level state before commitment (P11) has selected single-channel content.
- **Post-individuation regime.** Substrate-level state after commitment; single-channel content with un-selected phase randomized.
- **Multi-channel coherent state.** $\Psi^C = \sum_K P_K^C\,|K\rangle$ — substrate-level analog of QM superposition.

---

**End of Paper_001.**

*Wave-2 Generative Paper — QM-Kinematics Arc Upstream Anchor.*
