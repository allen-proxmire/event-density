# Gauge Fields as Forced Rule-Type Structure: The Closure of Arc Q and Theorem 17

**Author:** Allen Proxmire
**Collaborator:** Claude (AI collaborator)
**Date:** April 2026
**Series:** Event-Density Foundational Theorems — Arc Q

---

## Abstract

We close Arc Q of the Event-Density (ED) program by promoting the Gauge-field-as-Rule-Type Hypothesis (GRH) from form-level structural commitment to a FORCED-unconditional structural theorem (Theorem 17). Earlier Arc Q work established GRH at the form level (Theorem 5), canonical (anti-)commutation (Theorem 6), and primitive-level UV-finiteness UV-FIN (Theorem 7), but left five refinement axes unresolved: lightlike worldline structure (R-1), gauge-quotient individuation (R-2), commitment-axis structure (R-3), non-Abelian extension (R-4), and the vacuum-vs-particle vacuum-side classification (R-5). We present a four-substage closure trajectory — Q.2 (gauge group + quotient), Q.3 (vertex taxonomy + minimal coupling), Q.7 (worldline + second-quantisation), Q.8 (vacuum + zero-point) — followed by a synthesis stage (global integration + falsifier audit + Theorem 17 statement). All seven refinement items close substage-CANDIDATE-FORCED with all twelve substage-level falsifiers and all six synthesis-level falsifiers dispatched dark; in particular, the Arc M circularity check (SFal-5) verifies that the Theorem 17 derivation chain invokes no downstream input. **Theorem 17 (GRH FORCED-unconditional)** asserts that the gauge field $A_\mu$ is the participation measure of a structural rule-type $\tau_g$ whose group / vertex / worldline / vacuum content is forced across all four channels under a single unified gauge-quotient identification, with form FORCED by ED primitives plus Theorems 1–16 and numerical magnitudes (specific gauge group, coupling values, V1 kernel parameters, vacuum energy density) inherited from the value layer. Theorem 17 advances the FORCED-theorem inventory from sixteen to seventeen, closes Arc Q, and unblocks the Arc M F-M8 cascade (the $\tau_g$-mediated mass-form channel through the V1 vacuum kernel).

---

## 1. Introduction

### 1.1 Motivation: gauge invariance as structural consequence

In standard quantum field theory, gauge invariance is *postulated*. One selects a Lie group, declares a gauge field with prescribed transformation behaviour, and constructs the matter sector in representations of the group. The procedure is operationally successful but structurally opaque: nothing in the foundational machinery *forces* the existence of a gauge field, *forces* its non-Abelian capability, or *forces* its vacuum structure to take any particular form. Each commitment is a modelling choice.

Event-Density (ED) takes the opposite stance. The ED programme begins from a small primitive stack (the thirteen primitives P-01 through P-13) on a 3+1-dimensional event manifold, and asks which physical structures are *forced* by those primitives plus the consequences derived from them. A "FORCED-unconditional" structural theorem in ED is one whose statement is derivable from primitives and prior FORCED theorems alone, without introducing any new CANDIDATE assumption.

Arc Q opens the question whether *gauge invariance itself* — the existence and structure of the gauge field $A_\mu$ — is FORCED in this sense.

### 1.2 Historical framing: from postulate to derived property

Earlier Arc Q work established three foundational FORCED theorems:

- **Theorem 5** — GRH unconditional at the **form level**: the gauge field is a participation measure of a rule-type $\tau_g$, where the term "form level" indicates that the structural identification is forced but the full refinement programme (gauge-group structure, vertex content, worldline content, vacuum content) is not yet closed.
- **Theorem 6** — canonical (anti-)commutation relations FORCED.
- **Theorem 7** — primitive-level UV-finiteness (UV-FIN) FORCED.

These results established the *form-level* identification of the gauge field with a rule-type, but five refinement items remained open:

- **R-1** — lightlike worldline structure for $\tau_g$ excitations.
- **R-2** — gauge-quotient individuation across all four structural channels.
- **R-3** — commitment-axis structure (vertex / worldline / vacuum branches).
- **R-4** — non-Abelian extension capability.
- **R-5** — vacuum-vs-particle classification, including the vacuum-side (R-5 completion) and excitation-side (R-5 partial).

Each refinement was a structural commitment that GRH would be expected to deliver if it were FORCED-unconditional rather than merely form-level. Until all five close, GRH cannot be promoted.

### 1.3 Arc Q's role in the ED programme

Within the broader ED programme, Arc Q occupies the gauge-and-vacuum position in the Phase-2 form-level sector: alongside Arc R (relativistic kinematics: Klein–Gordon, spin–statistics, Cl(3,1), Dirac), Arc M (chain-mass: form FORCED, value INHERITED), and Arc N (kernel-level memory structure: V1 vacuum kernel FORCED), Arc Q owns the gauge-field structural sector. Phase-1 produced the non-relativistic single-particle quantum mechanics from primitives. Arc Q's closure is the analogous structural closure for the gauge sector.

### 1.4 Summary of results

This paper presents **Theorem 17 (GRH FORCED-unconditional)**: the seventeenth FORCED structural theorem in the ED inventory. The result is reached via a four-substage closure trajectory followed by a synthesis stage:

```
Q.1 (form-level baseline, Theorem 5) ──┐
                                       │
Q.2 (gauge-group + quotient)           │
Q.3 (vertex + minimal coupling)        │  ──► Arc Q Synthesis ──► Theorem 17
Q.7 (worldline + second-quantisation)  │       (Memos 00, 01, 02)
Q.8 (vacuum + zero-point)              │
                                       │
                                       ──► Arc M F-M8 cascade
```

All twelve substage-level falsifiers and all six synthesis-level falsifiers were dispatched without trigger; in particular, the Arc M circularity check (SFal-5) confirmed that the Theorem 17 derivation does not invoke any downstream input. The refinement-closure map advances to 7/7 (R-1, R-2 FULL, R-3 FULL, R-4, R-5 FULL all CLOSED).

The paper proceeds as follows. §2 inventories the primitives, prior FORCED theorems, and refinement structure relevant to Arc Q. §3 surveys the Arc Q architecture across the four substages plus synthesis. §4 states Theorem 17 in physics-facing and structural-clausal forms. §5 presents the proof sketch with per-clause provenance. §6 catalogues the structural consequences. §7 maps the Arc M F-M8 cascade. §8 discusses the conceptual shift and limitations. §9 concludes. Appendices A–E supply the detailed refinement-closure map, primitive audits, falsifier tables, the worldline–field correspondence derivation, and the synthesis falsifier dispatch ledger.

---

## 2. Background and Preliminaries

### 2.1 ED primitives load-bearing in Arc Q

The seven primitives load-bearing in Arc Q's closure are:

| Primitive | Statement (ED-internal canonical form) |
|---|---|
| **P-02** | Rule-types are structural carriers; any rule-type that exists structurally has a participation measure on every admissible state. |
| **P-04** | Bandwidth additivity: independent rule-type sectors compose additively in bandwidth. |
| **P-06** | Commitment events are the fundamental ontology of structural commitment. |
| **P-07** | Commitments require an anchor: vertex-anchored in the excitation regime. |
| **P-10** | Gauge-quotient identification: gauge-equivalent configurations are identified at primitive level. |
| **P-11** | UV-finiteness: structural envelopes are UV-finite at every scale. |
| **P-13** | Continuous-time evolution closure: the global structural envelope is closed under continuous time evolution. |

The remaining primitives (P-01, P-03, P-05, P-08, P-09, P-12) are not directly load-bearing in Arc Q's closure but are consistent with all Arc Q commitments.

### 2.2 Prior FORCED theorems 1–16

Theorem 17 is derived from primitives plus the existing inventory of sixteen FORCED structural theorems. The most directly load-bearing for Arc Q's closure are:

- **Theorem 5** — GRH unconditional, form-level (Q.1 + Q.8 form-level baseline).
- **Theorem 6** — canonical (anti-)commutation, FORCED at Q.7's worldline-quantisation derivation.
- **Theorem 7** — UV-FIN, FORCED at Q.8's primitive-level UV-finiteness derivation.
- **Theorem 8** — V1 finite-width vacuum kernel, FORCED in Arc N (N.5); supplies the vacuum-kernel form that Q.8's VQ1 inherits.
- **Theorem 16** — time-translation Schrödinger evolution, FORCED in Phase-1 Arc U3; supplies stationarity and time-translation closure across the vacuum sector.

Theorems 1, 2, 3, 4, 9, 10, 11, 12, 13, 14, 15 are available as upstream inventory and are consistent with all Arc Q commitments; they are not directly load-bearing for Theorem 17's derivation.

### 2.3 Refinement structure (R-1 through R-5)

The five refinement axes of GRH were identified at Arc Q's opening as the items that must close before GRH can be promoted from form-level (Theorem 5) to FORCED-unconditional. They are:

- **R-1** — *Lightlike worldline.* Excitations of $\tau_g$ propagate on lightlike worldlines (null-geodesic structure forced from primitives).
- **R-2** — *Gauge-quotient individuation* (FULL = partial + completion). Gauge-equivalent configurations are identified at group, vertex, worldline, and vacuum levels under a single unified quotient.
- **R-3** — *Commitment-axis structure* (FULL = Q.3-side + Q.7-side + Q.8-side). Commitment events are vertex-anchored at the excitation level, lift to the worldline ledger, and reduce to strict non-commitment plus an additive background functional at the vacuum level.
- **R-4** — *Non-Abelian extension.* $\tau_g$ admits a non-Abelian-capable gauge-group structure with Killing-form / Jacobi closure.
- **R-5** — *Vacuum-vs-particle classification* (FULL = excitation-side partial + vacuum-side completion). The structural status of $\tau_g$ in both excitation and no-excitation sectors is consistent and forced.

### 2.4 Rule-types and participation measures

The ED ontology assigns to each structural rule-type $\tau$ a **participation measure** — a structural object encoding the rule-type's contribution to commitment-rate ledgers across the event manifold. The Gauge-field-as-Rule-Type Hypothesis (GRH) asserts that the conventional gauge field $A_\mu$ is identified with the participation measure of a rule-type $\tau_g$ whose internal structure (group, vertex, worldline, vacuum) is to be determined by Arc Q.

The form-level identification (Theorem 5) commits $A_\mu = $ participation measure of $\tau_g$ but leaves the four structural axes underdetermined. Arc Q closes them.

---

## 3. Arc Q Architecture

Arc Q's closure trajectory is a four-substage program followed by a three-memo synthesis. Each substage was structured as Memo 00 (scoping) + Memos 01–02 (substantive derivations) + Memo 03 (substage verdict + falsifier dispatch + cascade map). Each substage closed CANDIDATE-FORCED at the substage level — meaning the substage payload is forced *given* upstream consistency and *given* that no global cross-substage falsifier triggers. The synthesis stage discharges those global conditions.

### 3.1 Q.2 — Gauge-group admissibility and quotient structure

**Refinements owned:** R-2 partial (gauge-quotient at group level), R-4 (non-Abelian extension).

Q.2 decomposes into five sub-features (F1 group axiomatisation, F2 non-Abelian closure, F3 quotient extension, F4 representation-theoretic admissibility, F5 cross-substage hand-off). The substage closure delivers:

- A non-Abelian-capable gauge-group structure for $\tau_g$ with Killing-form and Jacobi closure (F2 / R-4).
- Gauge-quotient identification at the group level (F3 / R-2 partial).
- Structure-constant admissibility (F2 internal).

Substage-level falsifiers (F-falsifiers) dispatched dark in Q.2 Memo 03.

### 3.2 Q.3 — Vertex taxonomy and minimal coupling

**Refinements owned:** R-2 completion (vertex-quotient extension), R-3 Q.3-side (vertex-anchored commitment).

Q.3 decomposes into five sub-features (V1 vertex taxonomy, V2 minimal coupling, V3 vertex-quotient, V4 cross-substage extension, V5 cross-substage hand-off). The substage closure delivers:

- A vertex taxonomy with the minimal-coupling structural vertex as the canonical entry (V1 / V2).
- Vertex-quotient extension that pulls back the group-quotient through coupling (V3 / V4 / R-2 completion).
- Vertex-anchored commitment via P-06 + P-07 (R-3 Q.3-side).

Substage-level V-falsifiers dispatched dark in Q.3 Memo 03.

### 3.3 Q.7 — Worldline and second-quantised structure

**Refinements owned:** R-1 (lightlike worldline), R-3 Q.7-side (worldline-anchored commitment), R-5 partial (excitation-side vacuum-vs-particle).

Q.7 decomposes into six sub-features (W1 lightlike worldline, W2 affine-parameter consistency, W3 second-quantisation lifting, W4 commitment-ledger extension to worldline, W5 pre-vacuum scoping, W6 cross-substage hand-off). The substage closure delivers:

- The eikonal/null-geodesic limit forces lightlike worldlines for $\tau_g$ excitations (W1+W2 / R-1).
- Vertex commitments lift to an ordered worldline ledger $\{v_i\}$ (W3+W4 / R-3 Q.7-side).
- Second-quantised excitation lifting via Theorem 6 supplies a Fock-style count (W3+W4 / R-5 partial).
- Pre-vacuum scoping in W5; downstream dependency map for Q.8 in W6.

Substage-level W-falsifiers (including WFal-5 circularity check) dispatched dark in Q.7 Memo 03.

### 3.4 Q.8 — Vacuum and zero-point structure

**Refinements owned:** R-3 Q.8-side (vacuum-level commitment), R-5 completion (vacuum-side vacuum-vs-particle).

Q.8 decomposes into six sub-features (VQ1 zero-point structure, VQ2 vacuum classification, VQ3 vacuum-level commitment, VQ4 vacuum-level gauge-quotient audit, VQ5 downstream dependency map, VQ6 bookkeeping). The substage closure delivers:

- A gauge-invariant, UV-finite, V1-form, stationary vacuum kernel for $\tau_g$ (VQ1 / R-5 completion form-side).
- Three vacuum classes (background / excitation / mixed) on two orthogonal axes; excitation-vacuum minimal FORCED (VQ2).
- Strict non-commitment at vacuum + V1-form additive background functional $B[v;\tau_g]$ contributing to vertex-anchored commitment rates in non-vacuum states (VQ3 / R-3 Q.8-side).
- Full gauge-quotient consistency across kernel / classification / commitment / cross-substage channels (VQ4).

Substage-level VQ-falsifiers (including VQFal-4 circularity check on synthesis) dispatched dark in Q.8 Memo 03.

### 3.5 Synthesis — global integration, falsifier audit, Theorem 17

The synthesis stage runs three memos:

- **Memo 00** (scoping): inventories the four substage payloads, defines the synthesis-level falsifier set (SFal-1 cross-substage inconsistency, SFal-2 global quotient inconsistency, SFal-3 commitment-ledger inconsistency, SFal-4 primitive-level global incompatibility, SFal-5 Arc M circularity, SFal-6 acyclicity break), and lists allowed and forbidden inputs.
- **Memo 01** (global integration + audit): constructs the unified four-axis structural object, the unified commitment ledger ($\Gamma_{\text{global}}[v;s] = \Gamma_{\text{excitation}}[v;\tau_g,s] + B[v;\tau_g]$), and the unified gauge-quotient ledger; dispatches SFal-1, SFal-2, SFal-3, SFal-4, SFal-6 (all NOT TRIGGERED); issues a "ready-for-Theorem-17" certification.
- **Memo 02** (Theorem 17 + verdict + cascade): states Theorem 17 in canonical form, presents the per-clause proof sketch, dispatches SFal-5 (NOT TRIGGERED), issues the FORCED-unconditional verdict, and maps the Arc M F-M8 cascade.

The synthesis stage closes Arc Q.

---

## 4. Statement of Theorem 17 (GRH)

### 4.1 Physics-facing statement

> **Theorem 17 (Gauge-field-as-Rule-Type Hypothesis, FORCED-unconditional).**
>
> *In the Event-Density framework, the gauge field $A_\mu$ is the participation measure of a structural rule-type $\tau_g$. The rule-type $\tau_g$ admits a non-Abelian-capable gauge-group structure with Killing-form and Jacobi closure; its excitations propagate on lightlike worldlines with second-quantised excitation lifting; commitments are vertex-anchored at the excitation level via a structural minimal-coupling vertex; the vacuum sector carries a gauge-invariant, UV-finite, V1-form, stationary fluctuation envelope, is strict-non-committing, and contributes a gauge-invariant V1-form background functional $B[v;\tau_g]$ additively to vertex-anchored commitment rates in non-vacuum states; all four channels (group, vertex, worldline, vacuum) respect a single unified gauge-quotient identification under the gauge group. The form of these structural commitments is forced by ED primitives P-02, P-04, P-06, P-07, P-10, P-11, P-13 and Theorems 1–16; the numerical magnitudes (specific gauge group, coupling values, V1 kernel parameters, $B[v]$ amplitude, vacuum energy density) are inherited from the value layer and are not committed by the theorem.*

### 4.2 Structural / refinement-indexed statement

The theorem decomposes into nine clauses (C1)–(C9). Each clause attaches to an upstream Q-substage or synthesis-level dispatch.

> **Theorem 17 (GRH, structural form).**
>
> Under ED primitives P-02, P-04, P-06, P-07, P-10, P-11, P-13 and FORCED theorems 1–16, the structural rule-type $\tau_g$ whose participation measure is the gauge field $A_\mu$ satisfies:
>
> **(C1) Carrier.** $\tau_g$ is a rule-type (P-02) with a non-empty participation measure on the gauge-Lie-algebra fibre (GRH-1, GRH-2; Q.1 baseline = Theorem 5).
>
> **(C2) Group structure.** $\tau_g$ admits a non-Abelian-capable gauge-group structure with Killing-form and Jacobi closure; gauge-equivalent group elements are identified (R-2 partial + R-4; Q.2).
>
> **(C3) Vertex.** Commitment events are vertex-anchored; the minimal-coupling structural vertex is gauge-quotient-invariant; the vertex-quotient is the pullback of the group-quotient through coupling (R-2 completion + R-3 Q.3-side; Q.3).
>
> **(C4) Worldline.** Excitations of $\tau_g$ propagate on lightlike worldlines (R-1); the vertex-anchored commitment ledger lifts to an ordered worldline ledger $\{v_i\}$; second-quantised excitation lifting supplies a Fock-style count (R-1 + R-3 Q.7-side + R-5 partial; Q.7; Theorem 6 inheritance).
>
> **(C5) Vacuum kernel.** The no-excitation sector of $\tau_g$ carries a gauge-invariant, UV-finite, V1-form, stationary fluctuation envelope, inherited as the restriction of the global V1 vacuum kernel (Theorem 8) to the $\tau_g$ sector (R-5 completion form-side; Q.8 Memo 01; Theorems 7, 8 inheritance).
>
> **(C6) Vacuum classification.** Three admissible vacuum classes (background / excitation / mixed) on two orthogonal axes (background expectation $\times$ worldline support); excitation-vacuum is the minimal FORCED class (Q.8 Memo 01).
>
> **(C7) Vacuum commitment.** The vacuum is strict-non-committing (forced by P-06 + P-07); a gauge-invariant V1-form background functional $B[v;\tau_g]$ contributes additively (P-04) to vertex-anchored commitment rates: $\Gamma_{\text{global}}[v;s] = \Gamma_{\text{excitation}}[v;\tau_g,s] + B[v;\tau_g]$ in non-vacuum states (R-3 Q.8-side + R-5 completion commitment-side; Q.8 Memo 02; Synthesis Memo 01 §3).
>
> **(C8) Unified quotient.** All four channels (group, vertex, worldline, vacuum) respect a single unified gauge-quotient identification given by the orbits of the Q.2 gauge group; non-Abelian Killing-form and Jacobi consistency propagate through all four channels (Q.8 VQ4 + Synthesis Memo 01 §4).
>
> **(C9) Acyclic derivability.** Clauses (C1)–(C8) are derivable from P-02..P-13 + Theorems 1–16 + Q-substage verdicts alone, with no input from Arc M or any other downstream stage (Synthesis Memo 01 §6.5 + Synthesis Memo 02 §4).
>
> Numerical magnitudes are INHERITED from the value layer.

**Status:** form FORCED, value INHERITED. **FORCED-unconditional at the structural level.**

---

## 5. Proof Sketch of Theorem 17

The proof traces each clause to its primitive-level, theorem-level, and Q-substage provenance.

### 5.1 (C1) — Carrier

*Provenance:* P-02 + GRH-1 + GRH-2 + Theorem 5.

P-02 commits $\tau_g$ to existence as a rule-type. GRH-1 and GRH-2 commit $A_\mu$ to being the participation measure of $\tau_g$ on the gauge-Lie-algebra fibre. Theorem 5 (GRH unconditional, form-level) is the prior Arc Q baseline establishing form-level identification. **No additional CANDIDATE.**

### 5.2 (C2) — Group structure

*Provenance:* P-10 + Q.2 verdict + R-2 partial + R-4.

P-10 supplies the gauge-quotient identification. Q.2 Memo 01 (F2 derivation) closes R-4 by demonstrating that the Killing form, Jacobi identity, and structure-constant admissibility together force a non-Abelian-capable group structure on $\tau_g$. Q.2 Memo 02 (F3 derivation) closes R-2 partial via the gauge-quotient extension at group level. Q.2 Memo 03 dispatches all F-falsifiers. **No additional CANDIDATE.**

### 5.3 (C3) — Vertex

*Provenance:* P-06 + P-07 + P-10 + Q.3 verdict + R-2 completion + R-3 Q.3-side.

P-06 supplies commitment-event ontology; P-07 forces vertex anchoring in the excitation regime. Q.3 Memo 01 (V1+V2+V4 partial) derives the vertex taxonomy and the minimal-coupling structural vertex. Q.3 Memo 02 (V3+V4) closes R-2 completion via the vertex-quotient extension and R-3 Q.3-side via the vertex-anchored commitment derivation. Q.3 Memo 03 dispatches all V-falsifiers. **No additional CANDIDATE.**

### 5.4 (C4) — Worldline

*Provenance:* P-13 + Q.7 verdict + Theorem 6 + R-1 + R-3 Q.7-side + R-5 partial.

P-13 supplies continuous-time evolution closure. Q.7 Memo 01 (W1+W2) closes R-1 via the eikonal/null-geodesic limit on $\tau_g$ excitations: the bandwidth-limited carrier with vanishing structural mass-form (at form level) propagates on null geodesics. Q.7 Memo 02 (W3+W4) lifts the vertex commitment ledger onto the worldline (R-3 Q.7-side) and supplies the second-quantised excitation lifting (R-5 partial) by inheriting Theorem 6 (canonical (anti-)commutation). Q.7 Memo 03 dispatches all W-falsifiers including WFal-5 circularity. **No additional CANDIDATE.**

### 5.5 (C5) — Vacuum kernel

*Provenance:* P-02 + P-04 + P-10 + P-11 + P-13 + Theorem 7 + Theorem 8 + Q.8 Memo 01 + R-5 completion form-side.

Q.8 Memo 01 derives the vacuum kernel via six constraints:

1. **Non-vacuity** (from P-02 + GRH-2): $\tau_g$ has structural content in the no-excitation sector.
2. **UV-finiteness** (from P-11 + Theorem 7): the kernel is UV-finite.
3. **V1 form** (from Theorem 8 + Arc N kernel discipline): restriction of the global V1 vacuum kernel to the $\tau_g$ sector preserves V1 form.
4. **Gauge invariance** (from R-2 + P-10): the kernel is gauge-invariant.
5. **Bandwidth additivity** (from P-04): the kernel composes additively with other independent rule-type sectors.
6. **Stationarity** (from P-13 + Theorem 16): time-translation-invariant in the minimal branch.

**No additional CANDIDATE.**

### 5.6 (C6) — Vacuum classification

*Provenance:* Q.7 worldline + VQ1 + R-2 + Q.8 Memo 01.

Two orthogonal axes (background expectation $\times$ worldline support) yield three admissible classes. Excitation-vacuum (zero expectation, degenerate Q.7 worldline support) is minimal FORCED; background-vacuum (non-zero gauge-invariant scalar expectation, no worldline support) and mixed-vacuum are FORCED-admissible at form level. **No additional CANDIDATE.**

### 5.7 (C7) — Vacuum commitment

*Provenance:* P-04 + P-06 + P-07 + Q.8 Memo 02 + R-3 Q.8-side + R-5 completion commitment-side + Synthesis Memo 01 §3.

P-07 forces strict non-commitment at vacuum (no vertex anchor in pure vacuum). P-04 forces additive composition. The V1-form background functional $B[v;\tau_g]$ inherits from VQ1 and contributes additively to vertex-anchored commitment rates in non-vacuum states. Synthesis Memo 01 §3 verifies acyclicity of the global integration rule (vacuum-to-vertex contribution is forward-only additive, not a back-edge). **No additional CANDIDATE.**

### 5.8 (C8) — Unified quotient

*Provenance:* P-10 + Q.8 Memo 02 + Synthesis Memo 01 §4 + R-2 + R-4.

The four channels (group, vertex, worldline, vacuum) are individually gauge-quotient-consistent at substage level. Synthesis Memo 01 §4 dispatches the global six-pair cross-channel audit (group$\leftrightarrow$vertex, group$\leftrightarrow$worldline, group$\leftrightarrow$vacuum, vertex$\leftrightarrow$worldline, vertex$\leftrightarrow$vacuum, worldline$\leftrightarrow$vacuum), all PASS. Non-Abelian Killing-form / Jacobi consistency propagates from R-4 through all channels. **No additional CANDIDATE.**

### 5.9 (C9) — Acyclic derivability

*Provenance:* Synthesis Memo 02 §4 (SFal-5 dispatch).

Per-clause trace verifies that every input to (C1)–(C8) traces to either (i) an ED primitive, (ii) a Theorem in the 1–16 inventory, or (iii) a Q-substage verdict (Q.1, Q.2, Q.3, Q.7, Q.8). No Arc M result, no Phase-3 GR result, no SM-specific input, no QFT vacuum prescription is invoked. The Arc M F-M8 item is *consequence* of Theorem 17, not input. **SFal-5 NOT TRIGGERED.**

### 5.10 Falsifier-level provenance

| Falsifier source | Status |
|---|---|
| Q.2 substage F-falsifiers | All NOT TRIGGERED |
| Q.3 substage V-falsifiers | All NOT TRIGGERED |
| Q.7 substage W-falsifiers (incl. WFal-5 circularity) | All NOT TRIGGERED |
| Q.8 substage VQ-falsifiers (incl. VQFal-4 circularity) | All NOT TRIGGERED |
| Synthesis SFal-1 (cross-substage) | NOT TRIGGERED |
| Synthesis SFal-2 (global quotient) | NOT TRIGGERED |
| Synthesis SFal-3 (commitment-ledger) | NOT TRIGGERED |
| Synthesis SFal-4 (primitive global) | NOT TRIGGERED |
| Synthesis SFal-5 (Arc M circularity) | NOT TRIGGERED |
| Synthesis SFal-6 (acyclicity) | NOT TRIGGERED |

All eighteen falsifiers (twelve substage + six synthesis) dispatched dark. **No falsifier blocks Theorem 17.** $\square$

---

## 6. Structural Consequences

### 6.1 Gauge invariance as interface property of $\tau_g$

In standard QFT, gauge invariance is a postulated symmetry of the action under prescribed transformations. Theorem 17 reframes it: gauge invariance is the **interface property** of the rule-type $\tau_g$ — the equivalence relation under which structurally-identical $\tau_g$ configurations are identified at primitive level (P-10). It is not a chosen symmetry of a chosen action; it is the structural identification rule built into the primitive layer.

Concretely, what was previously framed as "we impose gauge invariance" becomes "the rule-type interface forces gauge-equivalent configurations to be the same configuration." The transformation freedom is not a redundancy added on top of a structure; it is the absence of distinction between structurally-identical primitive-level objects.

### 6.2 Masslessness as structural, not contingent

Clause (C4) commits $\tau_g$ excitations to lightlike worldlines at the form level. This is the structural form of "the gauge boson is massless." The numerical magnitude of any mass-form correction (e.g., from F-M8 cascade, see §7) is value-layer / INHERITED. Critically, this means:

- *Form-level masslessness is FORCED.* No mechanism in Theorem 17 alone produces a non-zero rest mass for $\tau_g$ excitations.
- *Value-level mass corrections are inherited.* If empirical inputs demand a non-zero gauge-boson mass (as for $W^\pm$ and $Z$ in the SM), Theorem 17 does not derive it — the relevant mass-form contributions live in Arc M's chain-mass ledger, with $\tau_g$-mediated contributions activated by the F-M8 cascade.
- *No Higgs mechanism is invoked or excluded.* Theorem 17 commits to the structural form; SSB-style mass generation is forbidden as an SM-specific input but is not contradicted as a *value-layer* mechanism.

### 6.3 Unified quotient structure

Clause (C8) certifies that the four structural channels share a single gauge-quotient identification. This unification — group, vertex, worldline, vacuum all under one quotient — is itself a structural prediction: any putative gauge-equivalent classification that distinguishes channel-specific gauge fixings is structurally inadmissible.

### 6.4 Vacuum-level commitment rule

Clause (C7) supplies the structural form of the commitment-rate ledger:

$$\Gamma_{\text{global}}[v;s] \;=\; \Gamma_{\text{excitation}}[v;\tau_g,s] \;+\; B[v;\tau_g]$$

where $B[v;\tau_g]$ is the gauge-invariant V1-form background functional from the $\tau_g$ vacuum kernel. The implications are:

- The vacuum is *strict-non-committing*: in a pure vacuum state with no excitations, the global commitment rate vanishes (no anchor exists).
- In any non-vacuum state, the vacuum kernel contributes an additive background to the vertex-anchored rate.
- This structurally corresponds to the role of "vacuum polarisation" in standard QFT, but is derived from primitives rather than postulated as a renormalisation phenomenon.

### 6.5 Worldline → vacuum → vertex consistency

The four-axis × three-branch × four-channel global object is internally consistent (Synthesis Memo 01 §2.5–§4). The worldline degenerates cleanly into the vacuum (excitation count $\to 0$); the vacuum kernel feeds back into the vertex commitment rate (forward-only additive contribution); the vertex commits anchor the worldline ledger. The unified gauge-quotient ties all three branches together.

---

## 7. Implications for Arc M

### 7.1 F-M8 promotion

Arc M's chain-mass program closed earlier under the verdict "form FORCED, value INHERITED" but left F-M8 — the $\tau_g$-mediated mass-form contribution channel through the V1 vacuum kernel — in CANDIDATE status pending GRH closure. Theorem 17 satisfies F-M8's antecedent:

- (C5) supplies the V1 vacuum kernel form.
- (C7) supplies the $B[v;\tau_g]$ additive background functional.
- (C8) supplies the gauge-invariance certification.
- (C9) supplies acyclic derivability.

F-M8 promotes from CANDIDATE to **FORCED-unconditional within Arc M cascade scope**.

### 7.2 Massless-slot resolution

The F-M8 promotion identifies the structural mechanism by which the chain-mass ledger receives a $\tau_g$-mediated contribution: the V1 background functional adds to vertex-anchored commitment rates of any rule-type whose excitation traverses vertex anchors on the $\tau_g$ vacuum kernel support. This contributes to the chain-mass ledger via the standard chain-mass map. Whether $\tau_g$ itself acquires mass through this channel is the M.1 (massless-slot resolution) question; the anticipated answer is "$\tau_g$ remains massless at form level; F-M8 fires on other rule-types via cross-sector coupling."

### 7.3 Cross-sector coupling constraints

The unified quotient (C8) constrains how $B[v;\tau_g]$ couples to other rule-types' commitment rates: cross-sector coupling must respect the unified gauge-quotient. M.3 (cross-sector coupling audit) will derive the structural coupling rule.

### 7.4 Downstream M.1–M.4 cascade

The Arc M cascade entered with the F-M8 promotion comprises:

- **M.1** — massless-slot resolution audit.
- **M.2** — mass-form additivity audit (F-M8 composes additively with other items per P-04).
- **M.3** — $\tau_g$ cross-sector coupling audit.
- **M.4** — Arc M synthesis verdict refresh.

Acyclicity is preserved: Arc M downstream items cannot feed back into Theorem 17 (SFal-5 dispatch in Synthesis Memo 02 §4 + Arc M Cascade Memo §5).

---

## 8. Discussion

### 8.1 Conceptual shift: gauge fields as rule-types

Theorem 17 reframes the gauge field as a derived structural object rather than a chosen physical field. The reframing is not a re-interpretation: it is a structural derivation in which the form-level content (group structure, vertex content, worldline content, vacuum content) is forced from the primitive layer. The numerical value layer (specific group, couplings, magnitudes) remains inherited — Theorem 17 does not derive Standard Model content; it derives the *structural form* that any gauge-field-like rule-type must take.

### 8.2 Comparison with traditional gauge theory

| Traditional QFT | Event-Density (Theorem 17) |
|---|---|
| Gauge group postulated | Non-Abelian-capable group structure FORCED (C2). |
| Gauge field $A_\mu$ postulated | $A_\mu$ identified as participation measure of $\tau_g$ (C1). |
| Minimal coupling postulated | Minimal coupling forced as structural vertex (C3). |
| Vacuum constructed via path integral / canonical quantisation | Vacuum kernel forced as gauge-invariant UV-finite V1 form (C5–C7). |
| Gauge invariance postulated symmetry | Unified gauge-quotient as primitive-level identification (C8). |
| Mass generation: Higgs mechanism postulated | Form-level masslessness (C4) + value-layer F-M8 cascade (Arc M). |

The shift is ontological: gauge structure is *derived* from primitives, not *imposed* on a Lagrangian.

### 8.3 Implications for unification and emergent structure

Theorem 17 commits to a single unified gauge-quotient (C8) across all four structural channels. This is a structural unification at the level of the rule-type — the gauge field's group, vertex, worldline, and vacuum content are not independent commitments but are aspects of the same $\tau_g$ rule-type under one quotient. Whether this structural unification has implications for empirical-level unification (e.g., grand unified theories) is a question for downstream value-layer analysis; Theorem 17 does not force any specific empirical unification scheme.

### 8.4 Limitations and open questions

Theorem 17 does *not* derive:

- The specific gauge group of nature (SU(3)$\times$SU(2)$\times$U(1) or otherwise).
- Specific coupling magnitudes ($\alpha$, $\alpha_s$, $\sin^2\theta_W$).
- Specific representation content of matter rule-types.
- The Higgs mechanism (or any value-layer mass-generation scheme).
- Specific vacuum-energy magnitudes or the cosmological constant.
- Anomaly cancellation specifics.
- Renormalisation-group running of couplings.

Open questions for future Arc-Q-adjacent work:

- *M.1–M.4 cascade closure* — whether F-M8 promotion materially refines Arc M's synthesis verdict.
- *Phase-3 GR integration* — whether $B[v;\tau_g]$ contributes to the curved-spacetime extension of the V1 vacuum kernel (Arc N + Phase-3 GR).
- *Empirical signatures of $B[v;\tau_g]$* — whether the additive vacuum-background contribution is detectable via vertex-anchored commitment-rate measurements.
- *Multi-rule-type gauge sectors* — whether multiple distinct $\tau_g$-style rule-types coexist with disjoint or overlapping vacuum kernels.

---

## 9. Conclusion

### 9.1 Summary of Arc Q

Arc Q closes via a four-substage trajectory (Q.2, Q.3, Q.7, Q.8) plus a three-memo synthesis. All seven refinement items (R-1, R-2 partial, R-2 completion, R-3 Q.3-side, R-3 Q.7-side, R-3 Q.8-side, R-4, R-5 partial, R-5 completion) close at substage level with all twelve substage-level falsifiers and all six synthesis-level falsifiers dispatched dark. The synthesis stage promotes GRH from form-level (Theorem 5) to FORCED-unconditional (Theorem 17), the seventeenth FORCED structural theorem in the ED inventory.

### 9.2 Role of Theorem 17 in the ED programme

Theorem 17 supplies the structural foundation for ED's gauge-and-vacuum sector. Together with the other Arc Q form-level theorems (Theorem 5 GRH form-level, Theorem 6 canonical (anti-)commutation, Theorem 7 UV-FIN), the Arc N kernel-level theorem (Theorem 8 V1 vacuum kernel), and the Phase-1 QM-emergence theorems (Theorems 10–16), it completes the structural picture of ED's quantum sector. The Phase-2 form-level closure (Arc R + Arc M + Arc Q) plus the kernel-level closure (Arc N) plus the Phase-1 emergence layer is now structurally integrated.

### 9.3 Forward trajectory into Arc M

The immediate downstream consequence of Theorem 17 is the Arc M F-M8 cascade (§7), which promotes the $\tau_g$-mediated chain-mass contribution channel and opens the M.1–M.4 follow-on items. Beyond Arc M, the Phase-3 GR programme (Arc N + Phase-3 GR) inherits the $B[v;\tau_g]$ structural object as a candidate channel for vacuum-mediated curvature corrections. Empirically, Theorem 17 does not directly produce predictions but constrains the *form* of all gauge-sector predictions in any downstream value-layer derivation.

---

## Appendix A — Detailed Refinement-Closure Map

| Refinement item | Status | Closing substage | Closing mechanism |
|---|---|---|---|
| R-1 (lightlike worldline) | CLOSED | Q.7 (Memo 01, W1+W2) | Eikonal/null-geodesic limit on $\tau_g$ excitations. |
| R-2 partial (gauge-quotient at group level) | CLOSED | Q.2 (Memo 02, F3) | P-10 + Q.2 group-structure scaffold. |
| R-2 completion (vertex-quotient extension) | CLOSED | Q.3 (Memo 02, V3+V4) | Pullback of group-quotient through coupling. |
| **R-2 FULL** | CLOSED | Q.2 + Q.3 | — |
| R-3 Q.3-side (vertex commitment) | CLOSED | Q.3 (Memo 02) | P-06 + P-07 + vertex-anchored ledger. |
| R-3 Q.7-side (worldline commitment) | CLOSED | Q.7 (Memo 02, W3+W4) | Vertex ledger lifted to worldline. |
| R-3 Q.8-side (vacuum commitment) | CLOSED | Q.8 (Memo 02, VQ3) | Strict non-commitment + V1 background functional $B[v]$. |
| **R-3 FULL** | CLOSED | Q.3 + Q.7 + Q.8 | — |
| R-4 (non-Abelian extension) | CLOSED | Q.2 (Memo 01, F2) | Killing form + Jacobi + structure-constant admissibility. |
| R-5 partial (excitation-side) | CLOSED | Q.7 (Memo 02, W3+W4) | Second-quantisation lifting + Theorem 6 inheritance. |
| R-5 completion (vacuum-side) | CLOSED | Q.8 (Memos 01 + 02, VQ1+VQ2+VQ3+VQ4) | V1 kernel + classification + commitment + quotient audit. |
| **R-5 FULL** | CLOSED | Q.7 + Q.8 | — |

**Map: 7/7 refinement items CLOSED; 5/5 top-level refinement axes FULLY CLOSED.**

---

## Appendix B — Primitive-Level Audits

### B.1 Per-substage primitive load

| Primitive | Q.2 | Q.3 | Q.7 | Q.8 | Synthesis | Forbidden anywhere? |
|---|---|---|---|---|---|---|
| P-02 | supports | supports | supports | constrains (VQ1 non-vacuity) | supports | No. |
| P-04 | neutral | constrains (V4) | constrains (W4) | constrains (VQ1 + VQ3) | constrains (load-bearing) | No. |
| P-06 | neutral | constrains (R-3) | constrains (R-3) | constrains (VQ3 strict non-commitment) | constrains | No. |
| P-07 | neutral | constrains (R-3) | constrains (R-3) | constrains (decisively, VQ3) | constrains | No. |
| P-10 | constrains (R-2 partial) | constrains (R-2 completion) | constrains (W4) | constrains (VQ1 + VQ4) | constrains (load-bearing) | No. |
| P-11 | neutral | neutral | neutral | constrains (VQ1 UV-FIN) | constrains | No. |
| P-13 | neutral | neutral | constrains (W2) | constrains (VQ1 stationarity + VQ4) | constrains | No. |

**No primitive forbids any Arc Q result; no new CANDIDATE introduced.**

### B.2 Synthesis-level global primitive audit

All seven primitives consistent globally (Synthesis Memo 01 §5). SFal-4 NOT TRIGGERED.

---

## Appendix C — Falsifier Tables

### C.1 Substage falsifier ledger

| Falsifier | Substage | Sub-feature | Status |
|---|---|---|---|
| F-1 through F-5 | Q.2 | F1–F5 | All NOT TRIGGERED |
| V-1 through V-5 | Q.3 | V1–V5 | All NOT TRIGGERED |
| WFal-1 through WFal-8 (incl. WFal-5 circularity) | Q.7 | W1–W6 | All NOT TRIGGERED |
| VQFal-1 through VQFal-7 (incl. VQFal-4 circularity) | Q.8 | VQ1–VQ6 | All NOT TRIGGERED |

### C.2 Synthesis falsifier ledger

| Falsifier | Description | Tested in | Status |
|---|---|---|---|
| SFal-1 | Cross-substage inconsistency | Synthesis Memo 01 §6.1 | NOT TRIGGERED |
| SFal-2 | Global quotient inconsistency | Synthesis Memo 01 §6.2 | NOT TRIGGERED |
| SFal-3 | Commitment-ledger inconsistency | Synthesis Memo 01 §6.3 | NOT TRIGGERED |
| SFal-4 | Primitive-level global incompatibility | Synthesis Memo 01 §6.4 | NOT TRIGGERED |
| SFal-5 | Arc M circularity | Synthesis Memo 02 §4 | NOT TRIGGERED |
| SFal-6 | Acyclicity break | Synthesis Memo 01 §6.5 | NOT TRIGGERED |

**Cumulative: 18 falsifiers (12 substage + 6 synthesis), all NOT TRIGGERED.**

---

## Appendix D — Worldline / Field Correspondence Derivation

The lightlike-worldline structure for $\tau_g$ excitations (clause C4 / R-1) is derived in Q.7 Memo 01 via the eikonal limit. Sketch:

1. By P-13 (continuous-time evolution closure) and Theorem 16 (time-translation Schrödinger evolution from Phase-1 Arc U3), every rule-type carrier admits a continuous-time evolution generator.
2. By the form-level vanishing of structural mass-form for $\tau_g$ at the bare level (clause C4 form-side), the dispersion relation in the eikonal limit is null: $g^{\mu\nu} k_\mu k_\nu = 0$.
3. The associated worldline (the integral curve of the wavevector under the eikonal flow) is a null geodesic: $g^{\mu\nu} \dot{x}_\mu \dot{x}_\nu = 0$.
4. The vertex-anchored commitment ledger (C3) lifts onto this null worldline as an ordered set of vertex events $\{v_i\}$ along the affine parameter (Q.7 Memo 02 W4).
5. Second-quantised excitation lifting (clause C4 worldline-side, R-5 partial) inherits Theorem 6 (canonical (anti-)commutation), supplying a Fock-style count over the worldline support.

The field-side correspondence is the standard map between the worldline ledger and the participation measure $A_\mu$: each worldline configuration of $\tau_g$ corresponds to a configuration of $A_\mu$ on the event manifold, with the worldline ledger entries supplying the vertex anchors of commitment events. This is the structural form of "particle/field duality" for the gauge sector.

---

## Appendix E — Synthesis Falsifier Dispatch Ledger

Detailed dispatch traces for each synthesis falsifier appear in Synthesis Memo 01 (§6.1–§6.5) and Synthesis Memo 02 (§4). Summary:

- **SFal-1 (cross-substage):** all six pairs (Q.2$\leftrightarrow$Q.3, Q.2$\leftrightarrow$Q.7, Q.2$\leftrightarrow$Q.8, Q.3$\leftrightarrow$Q.7, Q.3$\leftrightarrow$Q.8, Q.7$\leftrightarrow$Q.8) and four triples PASS.
- **SFal-2 (global quotient):** all six cross-channel pairs PASS; non-Abelian global consistency PASSES.
- **SFal-3 (commitment-ledger):** unified rule $\Gamma_{\text{global}} = \Gamma_{\text{excitation}} + B$ consistent with no double-counting; acyclicity preserved.
- **SFal-4 (primitive global):** all seven primitives consistent globally.
- **SFal-5 (Arc M circularity):** per-clause trace verifies no Arc M input invoked; F-M8 is consequence of Theorem 17, not input.
- **SFal-6 (acyclicity):** dependency graph has no back-edges.

All six dispatched dark.

---

## References (Internal)

- ED primitive stack (P-01 through P-13). *Foundations of Event-Density.*
- Phase-1 non-relativistic QM-emergence. *Phase-1 Synthesis.*
- Arc R relativistic kinematics. *Why the Universe is Structurally Mandatory.*
- Arc M chain-mass program. *Chain-Mass Synthesis.*
- Arc N non-Markovian kernel structure. *Non-Markovian Structure as a Forced Memory-Kernel Layer of Event-Density Theory.*
- Arc Q form-level baseline (Theorems 5, 6, 7). *Quantum Field Theory from Event-Density Primitives.*
- Arc Q Q.2 substage memos (00–03). `arcs/arc-Q/01–04`.
- Arc Q Q.3 substage memos (00–03). `arcs/arc-Q/05–08`.
- Arc Q Q.7 substage memos (00–03). `arcs/arc-Q/09–12`.
- Arc Q Q.8 substage memos (00–03). `arcs/arc-Q/13–16`.
- Arc Q synthesis memos (00–02). `arcs/arc-Q/17–19`.
- Arc M F-M8 cascade memo. `arcs/arc-M/cascade_memo_F_M8_promotion.md`.
- U3 time-translation Schrödinger evolution (Theorem 16). `papers/U3_Time_Translation_Schrodinger`.
- ED FORCED-theorem inventory (Theorems 1–17). `memory/project_qm_emergence_arc.md`.

---

*End of paper.*
