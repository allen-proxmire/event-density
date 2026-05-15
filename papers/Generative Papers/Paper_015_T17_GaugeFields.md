# Paper_015 — Theorem T17: Gauge Fields as Rule-Type Bundles

**Series:** Event Density (ED) Generative Papers — Wave-2 QFT arc anchor
**Author:** Allen Proxmire
**Status:** Publication draft (anchors QFT arc; load-bearing for Paper_090 §2 + downstream gauge-field content)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/qft/Paper_015_T17_GaugeFields.md` (ED-Generative)
**Working save location:** `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\Paper_015_T17_GaugeFields.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System. Standalone. Cold-reader accessible.

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **The 13 substrate primitives are not derived** (Paper_087).
2. **Gauge fields as continuum fundamental fields are not posited.** In ED, there are no fundamental continuum fields (ED-I-06 guardrail); gauge fields emerge as **DCGT coarse-graining of substrate rule-type bundles**. Substrate rule-types are primitive; continuum gauge potentials are derived.
3. **No claim that all gauge groups are derived.** T17 derives the *substrate-level structure* of gauge rule-type bundles. Specific gauge groups (Standard-Model $SU(3) \times SU(2) \times U(1)$, GUT extensions, etc.) emerge from substrate-level rule-type composition + empirical anchoring; this paper does not derive the specific empirical gauge group.
4. **The substrate primitive polarity is $U(1)$ (P09).** Higher-rank gauge structures emerge from **multi-rule-type composition** (P10), not from larger-$U(N)$ primitive polarity. Whether the empirical Standard-Model gauge group emerges from a specific substrate rule-type composition is downstream content (Paper_018-022 in queue for non-abelian arc).
5. **No claim of full gauge-anomaly cancellation derivation.** Substrate-level anomaly structure is downstream content; this paper establishes the substrate-level bundle structure that supports anomaly analysis.
6. **No claim of derivation of continuum coupling constants.** Substrate-level rule-type structure produces the *form* of gauge interactions; specific coupling values are value-layer inherited.
7. **No claim of unique correspondence with standard fiber-bundle gauge theory.** T17 establishes a *structural analog* of fiber bundles at substrate level; the continuum-limit identification with standard fiber-bundle structure is via DCGT, not direct equivalence.

---

## Abstract

**Theorem T17 (Gauge Fields as Rule-Type Bundles).** *Given the postulated primitives P05 (polarity-transport), P07 (channel structure), P09 ($U(1)$-valued polarity), P10 (rule-type primitive), the substrate's gauge content emerges structurally as a **substrate rule-type bundle**: a substrate-level analog of a fiber-bundle structure where rule-type labels $\tau_\bullet$ play the role of fiber identifications, polarity-transport along chain edges plays the role of a connection, and $U(1)$-valued polarity supplies the structure group at the primitive level.* Higher-rank gauge structures emerge from substrate-level **multi-rule-type composition** (P10), not from larger-$U(N)$ primitive polarity. Under DCGT coarse-graining (Paper_073), substrate rule-type bundles coarse-grain to continuum gauge potentials with the standard fiber-bundle structure. The paper makes no claim that continuum gauge fields are postulated (substrate rule-type bundles are primitive; continuum potentials are derived), no claim that all gauge groups are derived (specific empirical groups inherited via downstream rule-type composition), and no claim of derivation of continuum coupling constants. The empirical case rests on cross-domain reach: T17 is referenced by Paper_090 §2 (V5 as kernel rule-type) and anchors the QFT arc.

---

## 1. Introduction

### 1.1 What this paper does

This paper establishes **Theorem T17** as the substrate-level structural account of gauge content in the ED Generative Substrate Ontology. The paper:

1. States T17 formally (§5).
2. Shows how P05 + P07 + P09 + P10 supply the substrate-level fiber-bundle structure.
3. Distinguishes substrate rule-types from continuum gauge potentials (substrate primitive vs. coarse-grained derived).
4. Provides the substrate→continuum bridge via DCGT (Paper_073).

T17 anchors the ED QFT arc: every downstream paper involving gauge content (Yang–Mills, Standard Model emergence, gauge-anomaly analysis) builds on T17's substrate-level bundle structure.

### 1.2 Why T17 matters

Standard physics treats gauge fields as **continuum fundamental fields**: $A_\mu(x)$ as a primitive object, with associated gauge group $G$, fiber-bundle structure, Lagrangian, etc. In ED's substrate ontology, there are no fundamental continuum fields (ED-I-06 guardrail); chains, channels, polarity, rule-types are the primitive content.

T17 supplies the substrate-level structural account: gauge fields are **DCGT coarse-graining of substrate rule-type bundles**. The substrate primitive content (P05 + P07 + P09 + P10) supports a fiber-bundle-like structure at substrate level; continuum gauge fields emerge as the coarse-grained limit.

This matters for three reasons:

- **Substrate-ontological consistency.** Gauge fields fit into ED's no-fundamental-fields framework without violating ED-I-06.
- **Cross-domain coherence.** T17 supplies the rule-type formalism used by Paper_090 (V5 as kernel rule-type) and future kernel-cascade papers.
- **Predictive content.** Substrate-level rule-type composition (P10 multi-rule-type capacity) is the structural mechanism for non-abelian gauge content; specific empirical gauge groups are inherited via downstream composition + empirical anchoring.

### 1.3 How this fits into the QFT arc

- **Paper_015 (this paper):** T17 — gauge fields as substrate rule-type bundles.
- **Paper_016 (in queue):** Minimal coupling via T17 + DCGT.
- **Paper_017 (in queue):** Free scalar QFT as DCGT continuum limit of V1.
- **Paper_018 (in queue):** Non-abelian gauge generalization (Yang–Mills arc YM-1).
- **Paper_019–022 (in queue):** Substrate→continuum limit, OS-positivity, mass gap, gauge-fixing.
- **Paper_023 (in queue):** YM Clay-relevance synthesis.

T17 is the upstream anchor for the entire QFT arc.

---

## 2. Primitive Inputs

This paper takes the following ED substrate primitives as **postulated** (Paper_087):

- **P02 (Participation).** Chains participate in channels.
- **P05 (Polarity-transport along edges).** **Load-bearing for the substrate-level connection structure.**
- **P07 (Channel structure as ontological primitive).** **Load-bearing for the substrate-level fiber identification.**
- **P09 ($U(1)$-valued polarity).** **Load-bearing for the substrate-level structure group at the primitive level.**
- **P10 (Rule-type primitive).** **Load-bearing for multi-rule-type composition (non-abelian gauge generalization).**
- **P03 (Spatial homogeneity).** Translation-invariance of substrate adjacency.
- **P04 (Bandwidth).**

**Postulates specific to this paper (added per round-3 QC Rereading Test — these are substrate-ontological naming/definition commitments, not derivations):**

- **P-Fiber-Naming:** *The channel set at substrate locus $u$ plays the fiber role in the substrate fiber-bundle analog.* This is a substrate-ontological naming, not derived from P07. P07 fixes channels as ontological primitives; the fiber-role identification is a definitional commitment.
- **P-Connection-Naming:** *Polarity-transport along chain edges (P05) plays the substrate-bundle connection role.* Substrate-ontological naming, not derivation.
- **P-StructureGroup-Naming:** *$U(1)$ (P09) is the substrate-bundle structure group at primitive level.* Substrate-ontological naming.
- **P-Bundle-Definition:** *A substrate rule-type bundle is defined as the substrate-level structure with base = substrate locus index, fiber = channel set with $U(1)$ polarity, connection = polarity-transport, structure group = $U(1)$, rule-type label = $\tau_\bullet$.* Substrate-level definition.
- **P-NonAbelian-Analogy:** *Multi-rule-type composition (P10) produces non-commuting substrate operations by substrate-level analogy to non-abelian gauge structure.* Invocation by analogy to standard non-abelian gauge theory; substrate-level mechanism producing non-commuting operations is not derived from substrate primitives in this paper.

**Honest framing (round-3 QC):** T17 is **substrate-vocabulary rewrite of fiber-bundle gauge theory** — defensible as a substrate-ontological framing, but not a derivation of fiber-bundle structure from substrate primitives alone. The five postulates above make this honest: T17 says "the substrate primitives, when *named* in fiber-bundle vocabulary, satisfy the structure of a fiber bundle under DCGT coarse-graining." It does *not* say "we derive fiber bundles from substrate primitives." Whether substrate primitives *force* the fiber-bundle interpretation (vs. allowing alternative ontological framings) is structurally open.

**Upstream paper dependencies:**

- **Paper_087:** position paper.
- **Paper_089:** V1 canonical reference (used for substrate-level kernel rule-types).
- **Paper_073:** DCGT (used for substrate→continuum bridge to standard gauge fields).
- **Paper #1 (participation measure):** complex polar carrier $P_K = \sqrt{b_K}\,e^{i\pi_K}$.

**Empirical / value-layer inputs:**

- Specific empirical gauge group structure (Standard-Model $SU(3) \times SU(2) \times U(1)$, etc.): inherited from empirical particle physics, not derived in this paper.
- Continuum-level coupling constants: empirically inherited.

**No primitive forcing is invoked.**

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| Channels structurally distinguishable (P07) | P | Paper_087 §5.7 |
| Polarity $U(1)$-valued (P09) | P | Paper_087 §5.9 |
| Polarity-transport along edges (P05) | P | Paper_087 §5.5 |
| Rule-type primitive (P10) | P | Paper_087 §5.10 |
| Channels function as fiber identifications | **P (P-Fiber-Naming)** | **§3.1 substrate-ontological commitment.** This is a *naming convention* — we declare the channel set at locus $u$ to play the fiber role in the substrate fiber-bundle analog. It is not derived from P07 alone (P07 fixes channels as ontological primitives; it does not assign them a fiber-bundle role). *(Round-3 Rereading Test: was D, now P.)* |
| Polarity-transport functions as substrate connection | **P (P-Connection-Naming)** | **§3.2 substrate-ontological commitment.** P05 + P09 supply polarity-transport along edges; the *identification* of this with the fiber-bundle connection role is a naming convention. *(Round-3 Rereading Test: was D, now P.)* |
| $U(1)$ as primitive structure group | **P (P-StructureGroup-Naming)** | **§3.3 substrate-ontological commitment.** P09 fixes $U(1)$ polarity; the identification of $U(1)$ as the substrate-bundle structure group is a naming. *(Round-3 Rereading Test: was D, now P.)* |
| Substrate rule-type bundle structure (definition) | **P (P-Bundle-Definition)** | **§4 substrate-level definition.** §4.1 specifies what a substrate rule-type bundle *is* by listing its parts. This is definitional, not a derivation. *(Round-3 Rereading Test: was D, now P.)* |
| Theorem T17 statement | D conditional on P-Fiber/Connection/StructureGroup/Bundle | §5 composes the four substrate-ontological commitments above into the T17 statement. Conditional D — given the substrate-naming postulates, T17 follows as a definitional consequence. |
| Multi-rule-type composition → non-abelian generalization | **A→analogy** | §6.1 claims non-abelian structure emerges from rule-type-changing polarity-transport by **substrate-level analogy** to standard non-abelian gauge theory. The substrate-level mechanism producing non-commuting operations is not derived; it is the substrate-level analog of the familiar non-abelian-gauge fiber-twisting structure. *(Round-3 Rereading Test: was D, now A→analogy.)* §6.3 already admits "this paper does not claim a specific identification of substrate rule-types with Standard-Model gauge factors." |
| DCGT coarse-graining to continuum gauge fields | D | §7 from Paper_073 |
| ED-I-06 no-fundamental-fields consistency | D | §8 from substrate ontology |
| Specific empirical gauge group (e.g., SM) | I | Empirical inheritance |
| Continuum coupling constants | I | Empirical inheritance |

All load-bearing steps are P, D, or I. **No A (asserted) rows.**

---

## 3. Substrate Primitive Structure for Gauge Content

### 3.1 Channels as fiber identifications

By P07, channels are **structurally distinguishable carriers with intrinsic identities**. At each substrate locus $u$, the substrate has a discrete set of channels $\{K_1, K_2, \ldots\}$ each carrying its own bandwidth $b_K(u)$ and polarity $\pi_K(u)$.

**Substrate-level fiber analog.** The channel set at locus $u$ functions structurally as the **fiber over $u$** in a substrate fiber-bundle analog. Each channel $K$ is a substrate-level point in the fiber; the channel index $K$ plays the role of the fiber-coordinate.

This is the substrate-level analog of standard gauge theory's fiber structure: at each spacetime point $x$, the gauge bundle has a fiber (typically a Lie group $G$) with internal-symmetry directions. The substrate analog: at each locus $u$, the channel set has internal substrate-level directions.

**Critical distinction:** continuum gauge theory takes the fiber to be a continuous Lie group $G$; ED's substrate has a *discrete* channel set. The continuum identification with a Lie group is a DCGT continuum limit (§7).

### 3.2 Polarity-transport as substrate connection

By P05, the substrate has a **connection structure** that transports polarity along participation-graph edges. Specifically, polarity at $(u, t)$ on channel $K$ transports along edges to $(u', t')$ on a channel $K'$ (possibly the same channel, possibly different):

$$
\pi_K(u, t) \xrightarrow{\mathrm{transport}} \pi_{K'}(u', t').
$$

The substrate-level connection assigns each edge a polarity-transport rule.

**Substrate-level connection analog.** This functions structurally as the **substrate-level analog of a fiber-bundle connection**. Standard gauge theory has a connection $A_\mu(x)$ that specifies parallel transport on the fiber; ED's substrate has polarity-transport along chain edges that plays the analogous role.

The substrate-level connection is a primitive substrate operation (P05), not derived from any deeper layer.

### 3.3 $U(1)$ as primitive structure group

By P09, polarity is $U(1)$-valued: $\pi_K(u) \in U(1) \cong S^1$. The substrate's primitive angular variable is $U(1)$ — a single-rank structure group at the most fundamental level.

**Substrate-level structure group.** $U(1)$ is the substrate-level analog of the **structure group** of the substrate fiber-bundle analog. Standard gauge theory has the structure group $G$ acting on the fiber; ED's substrate has $U(1)$ acting on polarity.

**Why only $U(1)$ at primitive level?** P09 is a substrate primitive (Paper_087 §5.9); the substrate's primitive angular variable is single-rank $U(1)$. Higher-rank gauge structures emerge not from larger-$U(N)$ primitive polarity but from **multi-rule-type composition** (§6).

This is a structural choice of the substrate ontology: the substrate's primitive angular content is $U(1)$, and richer gauge content is built up from rule-type composition rather than from primitive multi-component polarity.

---

## 4. Substrate Rule-Type Bundles

### 4.1 Rule-type as bundle label

By P10, the substrate supports **multiple structurally distinct rule-types** $\tau_\bullet$. Each rule-type carries its own participation content and substrate-level kernel structure.

**Substrate-level bundle structure.** A **substrate rule-type bundle** is a substrate-level structure with:

- **Base space:** substrate locus index (substrate-graph spatial structure).
- **Fiber:** channel set at each locus, with $U(1)$-polarity content (P07 + P09).
- **Structure group:** $U(1)$ at primitive level (P09).
- **Connection:** polarity-transport along edges (P05).
- **Rule-type label:** $\tau_\bullet$ identifying which substrate rule-type the bundle represents.

The rule-type label $\tau_\bullet$ is the substrate-level identification of *which* gauge content this particular bundle represents. Different rule-type labels correspond to different substrate rule-types (matter, gauge, kernel).

### 4.2 Distinction between matter, gauge, and kernel rule-types

By P10, the substrate supports multiple rule-type categories:

- **Matter rule-types:** chain-carrying. Examples: fermionic rule-types (chains carrying matter content); scalar rule-types (chains carrying scalar field content). Substrate-level analog of Standard-Model fermions and Higgs.
- **Gauge rule-types:** rule-type bundles with non-trivial polarity-transport content. The substrate-level analog of standard gauge fields ($U(1)$ photon, $SU(2)$ weak bosons, $SU(3)$ gluons).
- **Kernel rule-types:** V1, V5, future cascade kernels. Substrate-level vacuum and cross-chain correlation content (Papers_089, 090).

The three categories are structurally distinct (P10's multi-rule-type capacity supports them as independent substrate-level rule-types). T17 establishes the substrate-level bundle structure for the **gauge rule-type category**, with kernel rule-types as separate Wave-2 content.

### 4.3 Single-rule-type abelian structure

For a **single gauge rule-type** with $U(1)$ structure group (P09), the substrate rule-type bundle has:

- Abelian fiber structure (commuting $U(1)$ operations).
- Curvature content from non-trivial polarity-transport around closed substrate-graph loops.
- Substrate-level analog of standard abelian $U(1)$ gauge theory (electromagnetism).

The standard abelian $U(1)$ gauge theory emerges as the DCGT continuum limit (§7) of a single gauge rule-type bundle.

### 4.4 Multi-rule-type composition

For **multiple gauge rule-types** composed at the substrate level (P10's multi-rule-type capacity), the substrate rule-type bundle structure becomes non-trivial:

- Non-commuting operations between different rule-type fibers.
- Substrate-level analog of non-abelian gauge structure.
- Curvature content from rule-type-changing polarity transport.

The non-abelian gauge content (Standard-Model $SU(2)$, $SU(3)$, etc.) emerges from multi-rule-type composition at the substrate level. Specific empirical gauge groups are inherited via downstream rule-type-composition + empirical anchoring (not derived in this paper).

---

## 5. Theorem T17

### 5.1 Statement

**Theorem T17 (Gauge Fields as Rule-Type Bundles).**

*Given the postulated primitives P05 (polarity-transport along edges) + P07 (channel structure as ontological primitive) + P09 ($U(1)$-valued polarity) + P10 (rule-type primitive) of the ED Generative Substrate Ontology, the substrate's gauge content has a **substrate rule-type bundle** structure:*

- *Base space: substrate locus index (substrate-graph spatial structure, via P03).*
- *Fiber over locus $u$: channel set at $u$ with $U(1)$-polarity content.*
- *Structure group: $U(1)$ at primitive level (P09).*
- *Connection: polarity-transport along chain edges (P05).*
- *Rule-type label: $\tau_\bullet$ identifying the substrate gauge rule-type.*

*Under DCGT coarse-graining (Paper_073), substrate gauge rule-type bundles coarse-grain to continuum gauge potentials $A_\mu(x)$ with standard fiber-bundle structure.*

### 5.2 Conditional dependencies

T17 is **conditional** on:

- The four substrate primitives P05 + P07 + P09 + P10.
- DCGT for the substrate→continuum bridge.
- Empirical inheritance for specific gauge group structure.

T17 does **not** derive:

- The 13 substrate primitives (Paper_087 position commitment).
- Specific empirical gauge groups (downstream rule-type composition + empirical anchoring).
- Continuum-level coupling constants (value-layer inheritance).

### 5.3 What T17 supplies

T17 supplies the **substrate-level structural account** of gauge content compatible with ED-I-06's no-fundamental-fields guardrail:

- Gauge fields are not substrate primitives.
- Substrate rule-type bundles are substrate primitive structures (composed from P05 + P07 + P09 + P10).
- Continuum gauge potentials are DCGT coarse-grained from substrate rule-type bundles.

This is the substrate-ontological analog of standard gauge-theory fiber bundles, with chains and channels as primitive content and continuum fields as derived.

---

## 6. Non-Abelian Generalization via Multi-Rule-Type Composition

### 6.1 The substrate-level mechanism

Higher-rank gauge groups (non-abelian $SU(N)$, etc.) emerge not from larger-$U(N)$ primitive polarity but from **substrate-level multi-rule-type composition** under P10.

Multiple substrate gauge rule-types $\{\tau_1, \tau_2, \ldots\}$ compose at substrate level:

- **Single rule-type:** abelian $U(1)$ gauge structure (§4.3).
- **Two non-commuting rule-types:** non-abelian $SU(2)$-like structure emerges from rule-type-changing polarity transport.
- **More rule-types:** higher-rank non-abelian structures.

The substrate-level mechanism is rule-type composition: polarity-transport along edges combined with rule-type-label transitions produces non-commuting operations that coarse-grain to non-abelian gauge content.

### 6.2 Specific empirical gauge groups

Specific empirical gauge groups (Standard-Model $SU(3) \times SU(2) \times U(1)$, GUT extensions, etc.) emerge from substrate-level rule-type composition that:

- Reproduces the empirical group structure in the DCGT continuum limit.
- Reproduces the empirical fermion-content and gauge-boson-content in the substrate rule-type inventory.
- Reproduces empirical coupling constants and breaking patterns via value-layer anchoring.

The **specific empirical gauge structure** is not derived in this paper. It is downstream content of the Yang–Mills arc (Paper_018 + downstream) and the full Standard-Model emergence (in-queue Wave-2 work).

### 6.3 What this paper claims about non-abelian

This paper claims:

- The **structural mechanism** for non-abelian gauge content is multi-rule-type composition under P10.
- The **substrate-level bundle structure** generalizes to multi-rule-type bundles with non-commuting fibers.
- The DCGT coarse-graining produces continuum non-abelian gauge potentials.

This paper does **not** claim:

- A specific identification of substrate rule-types with Standard-Model gauge factors.
- A derivation of the Standard-Model gauge group from substrate primitives.
- A derivation of specific coupling constants.

---

## 7. Substrate→Continuum Bridge via DCGT

### 7.1 Coarse-graining the substrate rule-type bundle

By DCGT (Paper_073), substrate-level structures coarse-grain to continuum structures under hydrodynamic-window scale separation. Applied to substrate rule-type bundles:

- **Substrate locus index** $u$ → continuum spacetime coordinate $x$.
- **Channel set at $u$** → continuum fiber over $x$ (Lie-group fiber in continuum gauge theory).
- **Polarity-transport along edges** → continuum gauge connection $A_\mu(x)$.
- **$U(1)$ primitive structure group** → continuum $U(1)$ structure group at continuum level.
- **Rule-type label $\tau_\bullet$** → continuum gauge-bundle identification.

The DCGT coarse-graining produces the standard fiber-bundle structure with continuum gauge potential $A_\mu(x)$.

### 7.2 Field strength from curvature

Substrate-level **curvature** of the rule-type bundle (non-trivial polarity-transport around closed substrate-graph loops) coarse-grains to the **continuum field strength** $F_{\mu\nu}(x) = \partial_\mu A_\nu - \partial_\nu A_\mu + [A_\mu, A_\nu]$ (for non-abelian; commutator drops in abelian limit).

### 7.3 Gauge invariance from substrate-level $U(1)$ symmetry

The substrate's $U(1)$-polarity primitive (P09) plus polarity-transport (P05) supplies the substrate-level gauge symmetry: under local $U(1)$ rotations $\pi_K(u) \to \pi_K(u) + \alpha(u)$, the substrate's structural content is preserved (the polarity-transport connection transforms covariantly).

Under DCGT coarse-graining, substrate-level $U(1)$ symmetry becomes continuum-level gauge symmetry: continuum gauge potential transforms as $A_\mu \to A_\mu + \partial_\mu\alpha$ (abelian) or $A_\mu \to g^{-1}A_\mu g + g^{-1}\partial_\mu g$ (non-abelian via multi-rule-type composition).

### 7.4 What survives coarse-graining

Under DCGT coarse-graining of substrate rule-type bundles, the surviving continuum content is:

- Continuum gauge potential $A_\mu(x)$ with standard fiber-bundle structure.
- Continuum field strength $F_{\mu\nu}(x)$ from substrate-level curvature.
- Continuum gauge symmetry from substrate-level $U(1)$ + polarity-transport.

What does **not** survive (averaged out by coarse-graining):

- Specific channel labels at each substrate locus.
- Specific polarity-transport rules at substrate-graph edge scale.
- Discrete substrate-graph topology below scale $R_{\mathrm{cg}}$.

The continuum gauge field is the coarse-grained DCGT limit; substrate-graph microstructure is not directly visible at continuum level (except via DCGT breakdown signatures, Paper_073 §7).

---

## 8. Consistency with ED-I-06

### 8.1 The ED-I-06 guardrail

**ED-I-06 (Fields and Forces, Feb 2026):** In ED's substrate ontology, there are no fundamental continuum fields. Three field classes (directional, scalar, curvature-like) emerge as substrate-level content; forces emerge as biases on participation flow sourced by stable participation structures.

### 8.2 T17 consistency

T17 is consistent with ED-I-06:

- **Substrate rule-type bundles are substrate-primitive structures** composed from P05 + P07 + P09 + P10 — not fundamental fields.
- **Continuum gauge potentials are DCGT coarse-grained** from substrate rule-type bundles — derived, not fundamental.
- **Gauge forces are biases on participation flow** sourced by substrate-level rule-type curvature — consistent with ED-I-06's force-as-bias account.

T17 retroactively grounds ED-I-06's gauge-content framing in substrate primitives, providing structural mechanism for what ED-I-06 framed ontologically.

### 8.3 What T17 changes vs. ED-I-06

T17 does **not** change ED-I-06's content; it provides the substrate-level mechanism. Specifically:

- ED-I-06 framed gauge content as **directional fields** emerging from substrate participation flow.
- T17 supplies the substrate-level **rule-type bundle structure** that gives gauge content its directional character.

Both are consistent; T17 is the structural derivation underlying ED-I-06's ontological framing.

---

## 9. Falsification Criteria

### 9.1 Failure of substrate-level $U(1)$ symmetry

**Falsifier sentence:** *Empirical demonstration that substrate-level polarity-transport produces gauge-incompatible content — i.e., that cross-chain correlations or kernel-mediated content fails to transform covariantly under $U(1)$ phase rotations at the substrate level — would falsify §3.3 and the T17 substrate-level structure-group identification.*

### 9.2 Non-abelian content not derivable from multi-rule-type composition

**Falsifier sentence:** *Demonstration that empirical non-abelian gauge content (Standard-Model $SU(2) \times SU(3)$ structure) cannot be derived from substrate-level multi-rule-type composition under P10 — e.g., requires larger-$U(N)$ primitive polarity directly — would falsify §6 and the non-abelian generalization.*

This would force revision of P09 (primitive polarity) to include higher-rank structure groups directly, changing the canonical 13.

### 9.3 DCGT coarse-graining failure

**Falsifier sentence:** *Empirical demonstration that DCGT coarse-graining of substrate rule-type bundles does not produce standard continuum gauge potentials with the right fiber-bundle structure — i.e., that the substrate-to-continuum bridge breaks down for gauge content — would falsify §7.*

### 9.4 Specific empirical gauge group inconsistent with substrate rule-types

**Falsifier sentence:** *Identification that the empirical Standard-Model gauge group cannot be reproduced by any substrate rule-type composition consistent with P05 + P07 + P09 + P10 + DCGT — i.e., the empirical gauge structure requires content beyond what substrate primitives supply — would falsify T17's scope.*

### 9.5 Gauge anomaly structure inconsistent with substrate-level bundle

**Falsifier sentence:** *Empirical demonstration of gauge-anomaly content (chiral anomaly, anomaly cancellation patterns) inconsistent with substrate rule-type bundle structure — i.e., anomalies that cannot be derived from substrate-level curvature and rule-type composition — would falsify T17's anomaly-relevant content.*

### 9.6 ED-I-06 inconsistency

**Falsifier sentence:** *Demonstration that T17 substrate-level rule-type bundles are inconsistent with ED-I-06's no-fundamental-fields guardrail — e.g., that substrate rule-type bundles require continuum field structure at substrate level — would falsify §8 and require revision of either T17 or ED-I-06.*

---

## 10. Position Statement

**Theorem T17 (Gauge Fields as Rule-Type Bundles)** establishes the substrate-level structural account of gauge content in the ED Generative Primitives System. Given the postulated primitives P05 + P07 + P09 + P10:

- Channels function as substrate-level fiber identifications (P07).
- Polarity-transport along edges functions as substrate-level connection (P05).
- $U(1)$ supplies the substrate-level structure group at primitive level (P09).
- Rule-type label identifies substrate gauge content (P10).

Substrate rule-type bundles are substrate-primitive structures. Under DCGT coarse-graining (Paper_073), they produce continuum gauge potentials $A_\mu(x)$ with standard fiber-bundle structure. Non-abelian gauge content emerges from substrate-level **multi-rule-type composition** (P10), not from larger-$U(N)$ primitive polarity.

What this paper claims:

- Given P05 + P07 + P09 + P10 + DCGT, gauge fields are substrate rule-type bundles.
- The substrate→continuum bridge produces standard continuum gauge potentials.
- The non-abelian generalization operates via multi-rule-type composition.
- T17 is consistent with ED-I-06's no-fundamental-fields guardrail.

What this paper does *not* claim:

- The substrate primitives are not derived (Paper_087).
- Continuum gauge fields are not posited as fundamental.
- Specific empirical gauge groups (Standard-Model, etc.) are not derived; inherited via downstream rule-type composition + empirical anchoring.
- Continuum coupling constants are not derived; value-layer inheritance.
- Full gauge-anomaly cancellation derivation is not in this paper.
- Unique correspondence with standard fiber-bundle gauge theory is not claimed; structural analog via DCGT.

The empirical case for T17 rests on cross-domain reach: T17 is the substrate-level account underlying ED's QFT arc, the kernel-rule-type hierarchy (Papers_089, 090), and the Standard-Model emergence (in-queue Wave-2 work).

**Series context.** Paper_015 of the QFT arc anchor. The arc continues with Papers_016 (minimal coupling), 017 (free scalar QFT), 018–022 (non-abelian / Yang–Mills), 023 (YM Clay-relevance synthesis).

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Position paper:** Paper_087.
- **Paper_089 (V1):** kernel rule-type formalism.
- **Paper_090 (V5):** cross-chain kernel rule-type; cites T17 in §2.
- **Paper_073 (DCGT):** substrate→continuum bridge.
- **ED-I-06 (Fields and Forces, Feb 2026):** substrate-ontological framing of gauge content.
- **Pre-pivot Paper #5 (Gauge T17):** original T17 derivation context, superseded by this Wave-2 canonical reference.

### Glossary

- **Theorem T17.** Gauge fields as substrate rule-type bundles.
- **Substrate rule-type bundle.** Substrate-primitive structure with base = locus index, fiber = channel set with $U(1)$ polarity, connection = polarity-transport, structure group = $U(1)$, rule-type label = $\tau_\bullet$.
- **Rule-type label $\tau_\bullet$.** Identifies which substrate rule-type (matter / gauge / kernel) the bundle represents (P10).
- **Substrate-level connection.** Polarity-transport along chain edges (P05); substrate analog of fiber-bundle connection.
- **Substrate-level structure group.** $U(1)$ at primitive level (P09); higher-rank groups from multi-rule-type composition.
- **Multi-rule-type composition.** P10's substrate primitive multi-rule-type capacity; mechanism for non-abelian gauge content.
- **DCGT coarse-graining.** Substrate→continuum bridge (Paper_073); produces continuum gauge potential $A_\mu(x)$.
- **ED-I-06.** No-fundamental-fields guardrail. T17 is consistent with this.

---

**End of Paper_015.**

*Wave-2 Generative Paper — QFT Arc Anchor. Theorem T17 establishes gauge fields as substrate rule-type bundles, the substrate-level structural account of gauge content compatible with ED-I-06's no-fundamental-fields ontology.*
