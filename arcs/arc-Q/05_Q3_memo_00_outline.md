# Q.3 Substage — Examination Outline (Memo 00)

**Stage:** Arc Q · Q.3 (interaction vertex classification)
**Date opened:** 2026-04-26
**Location:** `arcs/arc-Q/`
**Goal:** Discharge **R-2 completion** (vertex-level gauge-quotient individuation) and **R-3** (vertex-anchored commitment for the gauge rule-type $\tau_g$) for the GRH closure trajectory. Establish what GRH commits to about interaction vertices and how gauge structure is realised at the vertex level.
**Predecessors:** [`grh_evaluation.md`](grh_evaluation.md) (Q.1) · [`00_grh_closure_roadmap.md`](00_grh_closure_roadmap.md) · [`01_Q2_memo_00_outline.md`](01_Q2_memo_00_outline.md) (Q.2 Memo 00) · [`02_Q2_memo_01_non_abelian.md`](02_Q2_memo_01_non_abelian.md) (R-4 closed CANDIDATE-FORCED) · [`03_Q2_memo_02_gauge_quotient.md`](03_Q2_memo_02_gauge_quotient.md) (R-2 partial closed CANDIDATE-FORCED) · [`04_Q2_memo_03_verdict.md`](04_Q2_memo_03_verdict.md) (Q.2 substage CLOSED CANDIDATE-FORCED)
**Status:** Scoping memo. Defines Q.3's question, sub-feature decomposition, structural inputs, forbidden inputs, falsifier inventory, expected deliverables, dependency graph, and honest scope limits. Inherits Q.2's structural commitments (non-Abelian admissibility, kinematic gauge-quotient individuation, L3 interface gauge-invariance structure) as background.
**Purpose:** Pin down the Q.3 terrain so subsequent Q.3 memos (Memo 01: vertex taxonomy + minimal coupling; Memo 02: vertex-level gauge-quotient + vertex-anchored commitment; Memo 03: verdict + cascade) can target specific load-bearing items without re-scoping.

---

## 1. The Q.3 Question

### 1.1 Precise statement

Q.3 asks: **how do interaction vertices classify under GRH, and how does the vertex structure realise (a) the gauge-quotient individuation at the vertex level (R-2 completion) and (b) the vertex-anchored commitment for $\tau_g$ (R-3)?**

More formally: given Q.2's closure (compact Lie groups admissible for $\tau_g$'s gauge structure; kinematic gauge-quotient $\mathcal{A} / \mathcal{G}$ individuation-respecting via Q3-A automatic), what is the structural taxonomy of interaction vertices involving $\tau_g$ and charged rule-types? How are vertex events counted as commitment events under gauge equivalence? Where are commitment events sourced for $\tau_g$ — given that $\tau_g$ has a lightlike worldline (R-1, deferred to Q.7) with no rest frame for worldline-intrinsic commitment events?

The answer must be **vertex-precise**: it should specify the admissible vertex types (emission, absorption, self-coupling, etc.), the structural form of the minimal-coupling vertex as inherited from R.1 background, the gauge-invariant vertex-counting prescription for R-2 completion, and the vertex-level commitment-event specification for R-3 — all without invoking Q.7's lightlike-worldline reformulation, Q.8's vacuum content, or any Standard Model specifics.

### 1.2 Position between Q.2 and Q.7/Q.8

Q.3 sits structurally between Q.2 (gauge-group scoping) and Q.7/Q.8 (worldline reformulation + vacuum):

- **Q.2 supplied** the kinematic structure: which gauge groups are admissible, how the gauge-quotient $\mathcal{A} / \mathcal{G}$ is constructed at fixed time, how Primitive 10 individuation respects gauge equivalence on the configuration space.
- **Q.3 must establish** the vertex / interaction structure: how rule-types interact under gauge invariance, how interaction vertices count as commitment events, where commitment is sourced for $\tau_g$.
- **Q.7 will inherit** Q.3's vertex content for the lightlike-worldline reformulation: the affine-parameter machinery for $\tau_g$ must accommodate the vertex-anchored commitment structure Q.3 establishes.
- **Q.8 will inherit** Q.3's vertex content for vacuum-state definition: vacuum-state interactions involve virtual vertex events, which must be gauge-quotient-respecting per Q.3's R-2 completion.

Q.3 is therefore the vertex / interaction substage of the GRH closure trajectory — it sits at the boundary between kinematics (Q.2) and dynamics (Q.7/Q.8).

### 1.3 Refinements Q.3 is responsible for

| Refinement | Description | Q.3 sub-feature(s) |
|---|---|---|
| **R-2 completion** | Vertex-level gauge-quotient individuation | V3 |
| **R-3** | Vertex-anchored commitment for $\tau_g$ | V1 + V4 (with V2 supplying the minimal-coupling structural background) |

Q.3 closes 2 of the 5 refinement items remaining after Q.2 (R-2 completion + R-3). The remaining 3 (R-1, R-5 partial, R-5 completion) are Q.7 / Q.8 content.

### 1.4 Possible verdicts

- **CLOSED — CANDIDATE-FORCED.** Both R-2 completion and R-3 close affirmatively, mirroring Q.2's closure pattern. *Anticipated default.*
- **CLOSED — CANDIDATE-admissible.** Refinements close but with weaker structural support than CANDIDATE-FORCED.
- **PARTIAL.** One refinement closes; the other reveals a structural gap requiring sub-arc work.
- **REFUTED.** Some refinement reveals a primitive-level obstruction that blocks GRH closure at the vertex level. Would force restriction of GRH content.

---

## 2. Decomposition into Sub-Features

Q.3 packages **five** structurally distinct sub-features. Each must be settled independently for Q.3 closure.

### 2.1 (V1) Vertex Taxonomy Under GRH

- **Definition.** Establish the structural classification of admissible interaction vertices involving $\tau_g$ and charged rule-types: emission vertices (charged → charged + gauge), absorption vertices (charged + gauge → charged), self-coupling vertices (gauge × gauge → gauge for non-Abelian cases), and any higher-order vertices (e.g., the four-gauge-boson vertex in non-Abelian Yang-Mills).
- **Structural commitment.** GRH admits a specific finite vertex taxonomy: the four standard vertex types (emission, absorption, self-coupling 3-gauge, self-coupling 4-gauge) cover the structurally admissible vertices for $\tau_g$ in the gauge-coupling-free scope. Higher vertex types (5-gauge, 6-gauge, etc.) are structurally excluded by primitive-level constraints (anticipated).
- **Falsifier.** V1 fails if (a) admissible vertices include exotic types not in the standard taxonomy (would extend the framework), or (b) the standard vertex types are not all admissible (would restrict GRH content).
- **Out of scope.** V1 does not specify *which* charged rule-types live in *which* gauge-group representations (empirical inheritance per Q.4-onward); does not specify coupling-constant values; does not address vertex factors at the second-quantisation level (Q.7).
- **Status:** **forced-via-derivation** (anticipated). The four-vertex taxonomy follows from F2's non-Abelian admissibility (Memo 01 §2.3) plus minimal-coupling background from R.1.

### 2.2 (V2) Gauge-Covariant Vertex Structure (Minimal Coupling as Structural Vertex)

- **Definition.** Establish that the minimal coupling structure $D_\mu = \partial_\mu + (iq/\hbar) A_\mu$ — derived as background by R.1's local-phase-invariance argument for U(1) and generalised to non-Abelian via Memo 01 — is the structural vertex content for charged-rule-type / $\tau_g$ interactions, *not* a Lagrangian add-on or quantisation procedure.
- **Structural commitment.** The minimal-coupling vertex is GRH's structural commitment to interaction content. F-GRH-D from Q.1 §4.4 ("Minimal coupling as a structural interaction") promotes from CANDIDATE-conditional to CANDIDATE-FORCED at this sub-feature.
- **Falsifier.** V2 fails if (a) minimal coupling is not unique as the structural vertex form (multiple admissible vertex structures exist with no primitive-level discriminator), or (b) minimal coupling cannot be specified without invoking Lagrangian / Yang-Mills machinery as a derivation premise (forbidden input violation).
- **Out of scope.** V2 does not derive the Yang-Mills Lagrangian (which would be Q.4-content if anywhere); does not specify the coupling-constant value $q$ (empirical inheritance via Dimensional Atlas); does not address vertex renormalisation (Q.7 / Q.8 second-quantisation work).
- **Status:** **forced-via-derivation** (anticipated). Inherits R.1 minimal-coupling content as background; promotes to vertex-level structural commitment via Q.3 work.

### 2.3 (V3) Vertex-Level Gauge-Quotient Individuation (R-2 Completion)

- **Definition.** Establish that interaction vertices count as commitment events under gauge equivalence in a manner consistent with Q.2's kinematic gauge-quotient closure. Specifically: gauge-equivalent vertex configurations count as ONE commitment event, not many; gauge-invariant vertex observables (Wilson loops, gauge-invariant vertex factors) provide the framework's vertex-level physical content.
- **Structural commitment.** Vertex-level individuation operates on gauge-equivalence-class vertex content $[V]$, not on raw vertex configurations $V$. The commitment is the vertex-level analog of Q.2 Memo 02's Q3-A automatic individuation.
- **Falsifier.** V3 fails if (a) vertex-counting structurally distinguishes gauge-equivalent vertex configurations (commit each as distinct events), or (b) gauge-invariant vertex observables cannot be defined consistently with Primitive 10 and Primitive 11 at the vertex level.
- **Out of scope.** V3 does not address vacuum-state vertex content (vacuum fluctuations, virtual vertex pair production — these are Q.8 work); does not specify vertex-level renormalisation procedures (Q.7); does not address scattering amplitudes per se (Q.7 second-quantisation).
- **Status:** **load-bearing** (R-2 completion). Anticipated to close CANDIDATE-FORCED via vertex-level analog of Q3-A automatic individuation.

### 2.4 (V4) Vertex-Anchored Commitment for $\tau_g$ (R-3)

- **Definition.** Establish that commitment events for the gauge rule-type $\tau_g$ are sourced at interaction vertices with charged rule-types, *not* at intrinsic points along the lightlike worldline $\gamma_{\tau_g}$. Specify the precise commitment-event-counting prescription at vertices and reconcile with Primitive 11's commitment-dynamics specification.
- **Structural commitment.** $\tau_g$'s commitment-event content is *vertex-sourced*, with each emission / absorption / self-coupling vertex contributing one commitment event (modulo gauge-quotient counting from V3). This reframes Primitive 11's worldline-anchored commitment specification for the gauge-rule-type case where the worldline carries no rest frame.
- **Falsifier.** V4 fails if (a) commitment cannot be consistently anchored at vertices for $\tau_g$ (e.g., if Primitive 11's specification *requires* worldline-intrinsic commitment events that lightlike $\gamma_{\tau_g}$ cannot supply), or (b) vertex-anchored commitment introduces structural inconsistency with the Q.7-deferred lightlike-worldline reformulation.
- **Out of scope.** V4 does not derive the lightlike-worldline reformulation (R-1 — Q.7); does not address commitment dynamics for non-gauge rule-types (already covered by Phase-1 + Arc M); does not specify second-quantisation amplitudes built from vertex commitment events (Q.7).
- **Status:** **load-bearing** (R-3). Anticipated to close CANDIDATE-FORCED.

### 2.5 (V5) Downstream Constraints on Q.7 and Q.8

- **Definition.** Specify what Q.7 (second quantisation, lightlike-worldline reformulation, R-1 + R-5 partial) and Q.8 (vacuum + zero-point, R-5 completion) must inherit from Q.3's closure — i.e., produce the precise structural-content handoffs that downstream substages will use as background.
- **Structural commitment.** Q.3 issues a closure-state inventory: which vertex content is settled, which is deferred to Q.7 / Q.8, and what each downstream substage will use.
- **Falsifier.** V5 fails if Q.3's closure cannot be cleanly handed off — for example, if vertex-anchored commitment requires Q.7 lightlike-worldline content for its own definition (creating a Q.3 → Q.7 → Q.3 circular dependency).
- **Out of scope.** V5 does not execute the downstream substages; it only specifies what they inherit.
- **Status:** **forced-via-derivation** (bookkeeping; assembled from V1–V4 outputs).

### 2.6 Status Classification

| Sub-feature | Status | Reasoning |
|---|---|---|
| **V1** Vertex taxonomy | forced-via-derivation | Inherits F2 admissibility + R.1 minimal-coupling background; vertex types are structurally enumerable |
| **V2** Minimal coupling at vertex level | forced-via-derivation | R.1 background promoted to vertex-level structural commitment |
| **V3** Vertex-level gauge-quotient (R-2 completion) | **load-bearing** | The substantive R-2 completion question; closure determines downstream individuation machinery |
| **V4** Vertex-anchored commitment (R-3) | **load-bearing** | The substantive R-3 question; closure determines $\tau_g$'s commitment-event structure |
| **V5** Downstream dep map | forced-via-derivation | Bookkeeping integration |

Two genuinely substantive items (V3, V4); two derivation items closing on inherited structure (V1, V2); one bookkeeping item (V5). Pattern parallels Q.2's load distribution (two load-bearing F2 + F3; three derivation/bookkeeping F1, F4, F5).

---

## 3. Refinement Mapping

The two refinements assigned to Q.3 map onto the sub-features:

| Refinement | Maps primarily to | Supporting sub-features | Closure expected at |
|---|---|---|---|
| **R-3** Vertex-anchored commitment | V4 | V1 (taxonomy supplies vertex types as commitment-event candidates), V2 (minimal coupling as structural vertex form) | Q.3 Memo 01 (V1 + V2 + V4) |
| **R-2 completion** Vertex-level gauge-quotient | V3 | V1 (taxonomy specifies which vertex types must be quotiented) | Q.3 Memo 02 (V3) |

R-3 closes if V4 specifies vertex-anchored commitment consistently with Primitive 11 at the gauge-rule-type level. The supporting sub-features V1 (taxonomy) and V2 (minimal coupling) supply the vertex types and their structural form.

R-2 completion closes if V3 specifies vertex-level individuation respecting gauge equivalence — the vertex-level analog of Q.2 Memo 02's Q3-A automatic outcome.

**Load-bearing items: V3 and V4.** V1, V2, V5 are derivation or bookkeeping work.

**GRH-3 load-bearing relevance.** V2 (minimal coupling as structural vertex) and V3 (vertex-level gauge-quotient) are both directly load-bearing for GRH-3 (the L3-interface clause). V1 and V4 supply the vertex taxonomy and commitment-event structure that GRH-3's vertex-level realisation requires.

---

## 4. Structural Inputs

### 4.1 Primitives drawn upon

- **Primitive 02** (worldline + ambient 3+1D manifold). Supplies the spacetime structure on which interaction vertices live. Vertex-relevant content: vertices are point-like events on the manifold; interaction vertices are intersections of multiple worldlines (charged-rule-type worldlines + $\tau_g$'s lightlike worldline trajectory through the vertex region).
- **Primitive 04** (bandwidth fields). Vertex-relevant content: vertex events involve bandwidth-flow exchanges between rule-types; vertex-counting depends on bandwidth content.
- **Primitive 06** (four-gradient + Lorentz covariance). Vertex-relevant content: vertices respect Lorentz covariance; vertex factors are Lorentz-invariant scalars built from spinor / vector content.
- **Primitive 07** (rule-type taxonomy, Levers L1–L4). Vertex-relevant content: L3 interface specifies how rule-types interact at vertices; L2 internal-index content determines representation-tensor structure of vertex factors.
- **Primitive 10** (individuation threshold). Vertex-relevant content: vertex-level individuation operates on gauge-equivalence-class vertex content (V3 / R-2 completion).
- **Primitive 11** (commitment dynamics). Vertex-relevant content: **the central primitive for V4 (R-3).** Commitment events are dynamical primitives; vertex-anchored commitment for $\tau_g$ requires reconciling Primitive 11's specification with the lightlike-worldline scope.

For each primitive, Q.3 commits to using its admissibility content (e.g., "Primitive 11 admits vertex-anchored commitment for the gauge-rule-type case") **but not** any further specification (e.g., "Primitive 11 forces the QED interaction Lagrangian"). The line between admissibility and forcing preserves honest scoping.

### 4.2 Inherited FORCED upstream items

- **Theorems 1–9** (Phase-2 + Arc N + Phase-3 closures from 2026-04-24): background. Theorem 6 (canonical (anti-)commutation) is most relevant for Q.3 — vertex content is consistent with canonical (anti-)commutation but may not be derived from it (Theorem 6's content is Q.7-relevant).
- **Theorems 10–16** (Phase-1 closure, 2026-04-26): background. Theorem 14 (U1, $P_K = \sqrt{b_K} \cdot e^{i\pi_K}$) most relevant — vertex events affect participation-measure components; Theorem 16 (U3, Schrödinger evolution) supplies the time-evolution framework that vertex commitment events fit into.
- **Q.2 Memo 01 closure** (R-4: non-Abelian admissibility CANDIDATE-FORCED). Vertex-level work inherits non-Abelian admissibility — vertex types must accommodate Lie-algebra-multiplicity content.
- **Q.2 Memo 02 closure** (R-2 partial: kinematic gauge-quotient CANDIDATE-FORCED via Q3-A). Vertex-level individuation builds on this kinematic structure.
- **Q.2 Memo 03 closure** (Q.2 substage CLOSED CANDIDATE-FORCED). The full Q.2 substage closure provides the structural backbone for Q.3.

### 4.3 GRH-1 through GRH-4 (background, with Q.2 generalisation)

Q.3 takes the four GRH clauses as background, with Q.2's non-Abelian generalisation:

- **(GRH-1)** $\tau_g$ Case P — vertex factors are bosonic; vertex statistics is consistent with $\eta = +1$.
- **(GRH-2)** $\tau_g$ (1/2, 1/2) Lorentz rep — vertex factors involve four-vector $A_\mu$ contractions with Lorentz-covariant content from charged rule-types.
- **(GRH-3)** L3 interface enforces gauge invariance — vertex content is gauge-invariant (V2 + V3); load-bearing for Q.3.
- **(GRH-4)** $\sigma_{\tau_g} = 0$ via MR-P — $\tau_g$ is massless; vertex-anchored commitment compatible with lightlike worldline (V4 + R-3 background; full lightlike-worldline reformulation is Q.7).

### 4.4 R.1 minimal coupling content (background, not premise)

R.1's `kg_minimal_coupling_and_current.md` derived $D_\mu = \partial_\mu + (iq/\hbar) A_\mu$ for U(1) from local-phase invariance. Memo 01 generalised admissibility to non-Abelian. Q.3 uses R.1's *content* as background (the minimal-coupling vertex form exists as a structural object) but does not use R.1's *derivation chain* as a premise for new vertex content (that would re-derive what V2 is meant to commit to at the vertex level).

The discipline: **R.1 establishes that minimal coupling is the local-phase-invariance-forced vertex form; Q.3 V2 establishes that this vertex form is the GRH structural commitment.** Q.3 uses the existence but not re-derives the identification.

### 4.5 M.1.2 commitment-event framework (background)

M.1.2's massless rule-type framework (origin of GRH) noted that for massless rule-types, commitment events are sourced off-worldline (vertex-anchored). Q.3's V4 builds on this background but does not invoke M.1.2 as a derivation premise for the specific R-3 closure (which would invert the dependency — M.1.2 → GRH → Q.3 → M.1.2).

### 4.6 Mathematical infrastructure

- **Standard differential-geometric vertex content** (gauge-invariant vertex factors, Wilson loop construction). Background only; not a derivation premise.
- **Lie group / Lie algebra vertex content** for non-Abelian vertices (structure constants $f^{abc}$ in 3-gauge vertex; symmetric tensor $d^{abc}$ if applicable in some constructions). Background; same caveat.
- **Standard QFT vertex factors** (e.g., QED vertex $-ie\gamma^\mu$ for the electron-photon vertex). Background only — Q.3 verifies that ED's vertex content reduces to standard vertex content in the appropriate limit, but does NOT invoke standard QFT vertex Lagrangians as a derivation premise.

### 4.7 Scope conditions

- **Non-relativistic + relativistic single-particle scopes** (inherited from Phase-1 + Arc R; relevant for vertex-content scoping).
- **3+1D Minkowski background** (inherited).
- **Compact Lie group gauge structure** (Q.2 inheritance with the compactness-from-unitarity discipline).

---

## 5. Forbidden Inputs (Acyclicity Discipline)

Per the GRH closure roadmap §7 + the U3 closure pattern + Q.2's discipline, the following inputs are explicitly forbidden as Q.3 derivation premises:

### 5.1 Substage-cross-contamination forbidden inputs

- **R-1 (lightlike worldline reformulation)** — Q.7 content. *Justification:* Q.7's affine-parameter machinery is downstream; Q.3 may *commit to* vertex-anchored commitment as an alternative to worldline-anchored commitment, but may not *invoke* the affine-parameter machinery itself.
- **R-5 (vacuum vs particle status of $\tau_g$)** — Q.7 / Q.8 content. *Justification:* Q.3's vertex content is at the interaction level, before vacuum-state machinery is in place.
- **Any Q.7 results** (second quantisation framework, creation/annihilation operators, propagators, scattering amplitudes). *Justification:* Q.7 is downstream; using its results would invert dependencies.
- **Any Q.8 results** (vacuum state, zero-point fluctuations, vacuum-energy contributions, Λ-from-V₁ derivation). *Justification:* Q.8 is downstream.

### 5.2 Standard Model specifics forbidden inputs

- **U(1) hypercharge assignments** — empirical SM content. *Justification:* Q.3 establishes vertex admissibility; the *specific* U(1) embedding is empirical.
- **SU(2) weak isospin identification, electroweak vertex factors** — empirical SM content.
- **SU(3) color identification, QCD vertex factors** — empirical SM content.
- **Specific QED, QCD, electroweak vertex Lagrangians** — empirical SM content. *Justification:* Q.3 verifies that ED's vertex structure is consistent with standard vertex content in the appropriate limit, but may not derive ED's vertex content from standard vertex Lagrangians.
- **Weak mixing angle, Cabibbo angle, CKM matrix** — empirical SM parameters.
- **Spontaneous symmetry breaking** — Q.4 content.

### 5.3 Higgs sector forbidden inputs

- **Higgs field, Higgs vacuum expectation value, Higgs mass** — Q.4 content.
- **W / Z boson mass-generation mechanism** — Q.4 content.

### 5.4 Generation structure forbidden inputs

- **Number of fermion generations** — Q.6 / empirical.
- **Flavor structure, generation-specific vertex content** — Q.6 / empirical.

### 5.5 Empirical coupling constants forbidden inputs

- **Coupling constant values** ($q$, $g_s$, $g_w$). *Justification:* Q.3 establishes structural vertex form; values are inherited via Dimensional Atlas.
- **Charge quantization pattern** ($e/3$ for quarks, $e$ for leptons). *Justification:* Q.3 may scope whether structural arguments admit charge quantization but may not force the specific quantization pattern.

### 5.6 Cascade-target forbidden inputs

- **F-M8 (massless slot existence, FORCED-conditional)** — the cascade target, not a premise.
- **F-GRH-A through F-GRH-E** (the cascade items) — these are the *outputs* of GRH closure, not derivation premises.

### 5.7 Standard QFT vertex machinery forbidden inputs

- **Yang-Mills Lagrangian as a postulate** — derivation target, not premise. *Justification:* If GRH closes affirmatively (with full Q-substage trajectory), Yang-Mills emerges; using it as input inverts the derivation.
- **Faddeev-Popov ghost vertices, BRST quantization** — Q.7 content.
- **Path-integral measure (gauge-fixed or otherwise)** — Q.7 / Q.8 content.
- **Renormalization-group equations on vertex factors** — Q.7 / Q.8 content.

---

## 6. Falsifier Inventory

Q.3 closes affirmatively if all five sub-features (V1–V5) close uniquely under the available structural inputs. The following falsifiers state how each sub-feature could fail. Some are vertex-level specialisations of Q.2 falsifiers; others are Q.3-specific.

### 6.1 Vertex-level specialisations of Q.2 falsifiers

- **(VFal-1) Vertex-level primitive incompatibility.** Some primitive (P-02, P-04, P-06, P-07, P-10, or P-11) structurally forbids the vertex-level realisation of one of V1–V4. Vertex analog of Memo 00 §6.1's Fal-2. *Targets V1, V2, V3, or V4.* *Anticipated dispatch:* Q.3 Memo 01 + Memo 02 primitive-by-primitive vertex-level audit.

- **(VFal-2) Vertex-level L3-interface incompatibility.** The L3 interface's gauge-invariance requirement cannot be realised at the vertex level — vertex content cannot be specified gauge-invariantly. Vertex analog of Q.2 Memo 02 §6.1's Fal-3. *Targets V2 + V3.* *Anticipated dispatch:* Q.3 Memo 02 vertex-level L3 audit.

- **(VFal-3) Vertex content forces structural changes to GRH-1/2/4.** Vertex specification at Q.3 requires generalising GRH-1 (Case P), GRH-2 ((1/2, 1/2) Lorentz), or GRH-4 (σ = 0). Vertex analog of Memo 01 §6.3's Fal-6. *Targets V1, V2, V4.* *Anticipated dispatch:* Q.3 Memo 01.

- **(VFal-4) Cross-cutting vertex-level individuation failure.** The vertex-level gauge-quotient individuation requires Q.7 / Q.8 content for its definition, creating a cross-substage circular dependency. Vertex analog of Q.2 Memo 02 §6.2's Fal-7. *Targets V3 + V5.* *Anticipated dispatch:* Q.3 Memo 02 + Memo 03.

### 6.2 Q.3-specific falsifiers

- **(VFal-5) Vertex-classification inconsistency.** The vertex taxonomy admits structurally inconsistent or redundant vertex types — for example, distinct vertex types that are gauge-equivalent at the kinematic level but counted separately, or vertex types that violate Lorentz covariance. *Targets V1.* *Anticipated dispatch:* Q.3 Memo 01.

- **(VFal-6) Minimal coupling fails as the unique structural vertex form.** Multiple non-equivalent vertex structures are admissible at the L3 interface level, with no primitive-level discriminator selecting minimal coupling as the unique form. Would weaken V2 from forced-via-derivation to CANDIDATE-admissible. *Targets V2.* *Anticipated dispatch:* Q.3 Memo 01.

- **(VFal-7) Vertex-counting fails to respect gauge equivalence.** Vertex commitment events count gauge-equivalent vertex configurations as distinct events, breaking Q.2 Memo 02's R-2 partial closure at the vertex level. *Targets V3.* *Anticipated dispatch:* Q.3 Memo 02.

- **(VFal-8) Vertex-anchored commitment cannot be defined consistently with Primitive 11.** Primitive 11's commitment-dynamics specification requires worldline-intrinsic commitment events that lightlike $\gamma_{\tau_g}$ cannot supply, with no admissible vertex-anchored alternative. Would force restriction of GRH content to massive gauge rule-types (which would conflict with GRH-4). *Targets V4.* *Anticipated dispatch:* Q.3 Memo 02 (or Memo 01 §V4 setup).

- **(VFal-9) Q.3 ⟷ Q.7 circular dependency.** Vertex-anchored commitment (V4) requires Q.7's lightlike-worldline reformulation for its own definition. *Targets V4 + V5.* *Anticipated dispatch:* Q.3 Memo 02 + Memo 03 dependency-map audit.

### 6.3 Falsifier-source taxonomy

| Falsifier | Targets | Source layer | Anticipated dispatch |
|---|---|---|---|
| VFal-1 (vertex primitive incompat.) | V1, V2, V3, V4 | Primitive | Q.3 Memo 01 / 02 |
| VFal-2 (vertex L3 incompat.) | V2, V3 | L3 interface | Q.3 Memo 02 |
| VFal-3 (vertex breaks GRH-1/2/4) | V1, V2, V4 | Cross-clause | Q.3 Memo 01 |
| VFal-4 (cross-substage individ. failure) | V3, V5 | Methodological | Q.3 Memo 02 / 03 |
| VFal-5 (vertex taxonomy inconsistent) | V1 | Q.3-specific | Q.3 Memo 01 |
| VFal-6 (minimal coupling not unique) | V2 | Q.3-specific | Q.3 Memo 01 |
| VFal-7 (vertex-counting fails gauge) | V3 | Q.3-specific (R-2 completion) | Q.3 Memo 02 |
| VFal-8 (P-11 incompat. vertex commitment) | V4 | Q.3-specific (R-3) | Q.3 Memo 02 |
| VFal-9 (Q.3 ⟷ Q.7 circular) | V4, V5 | Methodological | Q.3 Memo 02 / 03 |

Two genuinely substantive Q.3-specific falsifiers (VFal-7, VFal-8); two derivation-style (VFal-5, VFal-6); five inherited / methodological. Pattern matches Q.2's load distribution.

---

## 7. Expected Deliverables

Q.3 closure must produce:

### 7.1 Structural classification of admissible interaction vertices under GRH

A clean statement of which vertex types GRH structurally admits — anticipated forms:

- **Emission vertex** (charged → charged + gauge): structurally admissible per V1; minimal-coupling form per V2.
- **Absorption vertex** (charged + gauge → charged): structurally admissible; reverse of emission.
- **3-gauge self-coupling vertex** (gauge × gauge → gauge): admissible for non-Abelian gauge groups via Memo 01's C3 commitment; structure constants $f^{abc}$ supply the vertex factor.
- **4-gauge self-coupling vertex** (gauge × gauge × gauge × gauge): admissible for non-Abelian gauge groups; structure-constant contractions supply the vertex factor.
- **Higher-order vertices** (5-gauge, 6-gauge, etc.): structurally excluded by primitive-level constraints (anticipated; verification in V1 derivation).

### 7.2 Statement of what GRH commits to about minimal coupling as a structural vertex

A precise statement promoting F-GRH-D from CANDIDATE-conditional to CANDIDATE-FORCED at the vertex level. Anticipated form: "GRH commits to the minimal-coupling structure $D_\mu = \partial_\mu + (iq/\hbar) A_\mu$ as the structural vertex content for charged-rule-type / $\tau_g$ interactions, with $q$ inherited (empirical) and the operator structure forced by L3-interface gauge invariance plus $\tau_g$'s rule-type properties."

### 7.3 R-2 completion verdict (vertex-level gauge-quotient)

R-2 completion closes affirmatively at the vertex-level individuation: gauge-equivalent vertex configurations count as ONE commitment event; gauge-invariant vertex observables (Wilson loops, gauge-invariant vertex factors) are well-defined; vertex-level individuation is consistent with Q.2's kinematic individuation. Anticipated verdict: CANDIDATE-FORCED.

### 7.4 R-3 verdict (vertex-anchored commitment)

R-3 closes affirmatively: $\tau_g$'s commitment events are sourced at interaction vertices with charged rule-types; vertex-anchored commitment is consistent with Primitive 11's commitment-dynamics specification (with the gauge-rule-type case as a structural extension); the lightlike-worldline reformulation (R-1, Q.7) accommodates the vertex-anchored commitment without conflict. Anticipated verdict: CANDIDATE-FORCED.

### 7.5 Dependency map for Q.7 and Q.8

A precise inventory of what each downstream substage inherits from Q.3:

| Downstream | Inherits from Q.3 | Used for |
|---|---|---|
| **Q.7** | Vertex taxonomy (V1); minimal-coupling vertex form (V2); vertex-anchored commitment specification (V4) | Lightlike-worldline reformulation must accommodate vertex-anchored commitment; affine-parameter machinery for $\tau_g$ takes vertex-emission/absorption events as the commitment-event sequence |
| **Q.8** | Vertex-level gauge-quotient individuation (V3); gauge-invariant vertex observables | Vacuum-state interactions involve virtual vertex events; vacuum-state vertex observables must be gauge-quotient-respecting |

### 7.6 Verdict

Anticipated: **R-2 completion and R-3 both close affirmatively (CANDIDATE-FORCED); Q.3 substage CLOSED — CANDIDATE-FORCED; GRH closure trajectory advances to Q.7.**

If V3 fails: vertex-level gauge-quotient is structurally inconsistent with Q.2's kinematic closure — this would be a serious inconsistency requiring re-examination of Q.2's F3 closure.

If V4 fails: $\tau_g$'s commitment events cannot be structurally specified — would force restriction of GRH content to massive gauge rule-types, conflicting with GRH-4 (σ = 0); would re-open M.1.2's massless-slot question.

Both failure modes are anticipated NOT to obtain (V3 inherits cleanly from Q.2 Memo 02; V4's vertex-anchored commitment is exactly the M.1.2 framework anticipated outcome).

---

## 8. Dependency Graph

### 8.1 Substage dependencies (post-Q.2)

```
                  Q.0 (scoping)              ← background
                       ↓
                  Q.1 (GRH evaluation)        ← background; CANDIDATE-strong verdict
                       ↓
                  Q.2 (gauge group scoping)   ← CLOSED CANDIDATE-FORCED
                       │  (R-4, R-2 partial closed)
                       ↓
            ┌─────  Q.3 (THIS substage)  ─────┐
            │  V1 (vertex taxonomy)            │
            │  V2 (minimal coupling vertex)    │
            │  V3 (vertex gauge-quotient)      │  ← discharges R-2 completion
            │  V4 (vertex-anchored commitment) │  ← discharges R-3
            │  V5 (downstream dep map)         │
            └────────────┬─────────────────────┘
                         ↓
              Q.7 (second quantisation)         ← discharges R-1, R-5 partial
                         ↓
              Q.8 (vacuum and zero-point)       ← discharges R-5 completion
                         ↓
              Arc Q synthesis                   ← promotes GRH to FORCED-uncond.
                         ↓
              Cascade to Arc M                  ← F-M8 promoted to FORCED-uncond.
                         ↓
              Theorem 17 added to inventory
```

### 8.2 Refinement-to-substage closure map (post-Q.2 update)

| Refinement | Status | Closure stage |
|---|---|---|
| R-1 (lightlike worldline) | outstanding | Q.7 |
| R-2 partial (kinematic gauge-quotient) | ✅ CLOSED CANDIDATE-FORCED | Q.2 Memo 02 |
| **R-2 completion (vertex-level gauge-quotient)** | **outstanding** | **Q.3 (V3)** |
| **R-3 (vertex-anchored commitment)** | **outstanding** | **Q.3 (V4)** |
| R-4 (non-Abelian extension) | ✅ CLOSED CANDIDATE-FORCED | Q.2 Memo 01 |
| R-5 partial (vacuum-field aspect) | outstanding | Q.7 |
| R-5 completion (zero-point aspect) | outstanding | Q.8 |

### 8.3 How Q.3's commitments constrain Q.7 / Q.8

**To Q.7:**
- Vertex-anchored commitment for $\tau_g$ (V4) constrains Q.7's affine-parameter machinery: per-worldline accounting must accommodate vertex-anchored commitment events rather than worldline-intrinsic events.
- Vertex taxonomy (V1) constrains Q.7's second-quantisation amplitudes: amplitudes must be built from the admissible vertex types only.
- Minimal-coupling vertex form (V2) constrains Q.7's interaction-Hamiltonian content: the structural vertex form is fixed at Q.3; Q.7 supplies the second-quantisation framework on top.

**To Q.8:**
- Vertex-level gauge-quotient individuation (V3) constrains Q.8's vacuum-state vertex content: virtual vertex events in the vacuum must be gauge-quotient-respecting.
- Vertex taxonomy (V1) constrains Q.8's vacuum-state interactions: vacuum-state contributions to vertex content must use admissible vertex types only.

These constraints flow one-way: Q.3 → Q.7, Q.3 → Q.8. Q.7 and Q.8 do not feed back into Q.3 (per VFal-9 dispatch via V5).

---

## 9. Honest Scope Limits

Q.3 explicitly cannot resolve the following — these are empirical inheritance, downstream-substage content, or out-of-scope for the GRH closure trajectory:

- **Specific gauge group choice.** Whether the universe's gauge group is $SU(3) \times SU(2) \times U(1)$ or anything else. Empirical inheritance per Q.2 F4 closure (carried forward to Q.3).
- **Coupling constant values.** Numerical values of $q$, $g_s$, $g_w$, $\theta_W$, etc. Empirical inheritance via Dimensional Atlas.
- **Charged-rule-type representation assignments.** Which fermions transform under which representations of $G$ (e.g., why quarks are in fundamental of $SU(3)$ and leptons are singlets). Empirical / Q.4–Q.6 content.
- **Vertex-level renormalisation procedures.** Counter-term structure, beta-function content for vertex factors. Q.7 / Q.8 content.
- **Higgs sector / SSB vertices.** Higgs-mediated vertex content. Q.4; SPECULATIVE.
- **Generation structure / flavor-changing vertices.** Generation-specific vertex content (e.g., CKM-suppressed flavor-changing currents). Q.6 / empirical.
- **Charge quantization pattern.** Why charges come in integer multiples of $e/3$ (quarks) or $e$ (leptons). Possibly Q.2 / Q.3 partial sub-memo (Dirac-monopole-style topological argument), possibly empirical. Out of Q.3 default scope.
- **Standard QFT amplitude / scattering content.** Cross-sections, Feynman-diagram amplitudes, perturbation-theory expansions. Q.7 second-quantisation work.
- **Vacuum vertex contributions.** Vacuum polarisation, virtual vertex events, vacuum-energy renormalisation. Q.8 work.

These scope limits are honest structural boundaries inherited from Q.2's F4 closure and the broader Q-substage scoping discipline. Q.3 establishes vertex *admissibility* and vertex-level *individuation + commitment* structure; specific vertex *content* at the empirical level remains inheritance.

---

## 10. Recommended Next Memo

The natural next deliverable after this Memo 00 is:

**Q.3 Memo 01 — Vertex Taxonomy + Minimal Coupling at the Vertex Level (V1 + V2 + V4 partial; R-3 partial closure)**

Memo 01 should:

- Derive V1 (vertex taxonomy under GRH) — primitive-by-primitive admissibility check for the four standard vertex types (emission, absorption, 3-gauge, 4-gauge); explicit dismissal of higher-order vertices (5-gauge, 6-gauge) by primitive-level constraint
- Derive V2 (minimal coupling as structural vertex) — promotion of R.1's minimal-coupling content to vertex-level structural commitment; verification that minimal coupling is the unique vertex form (dispatching VFal-6)
- Begin V4 (vertex-anchored commitment) — establish the vertex-anchored commitment specification for $\tau_g$, with detailed Primitive 11 reconciliation (full V4 closure with R-3 deferred to Memo 02)
- Dispatch falsifiers VFal-1, VFal-3, VFal-5, VFal-6
- State R-3 partial closure verdict; full R-3 + R-2 completion closure deferred to Memo 02

Anticipated length: comparable to Q.2 Memo 01 (substantive primitive-level vertex-derivation work).

After Memo 01, Memo 02 would address V3 (vertex-level gauge-quotient, R-2 completion) and V4 completion (R-3 final closure). Memo 03 would address V5 (downstream dependency map) and the Q.3 substage verdict.

---

## 11. One-Line Summary

> Q.3 substage scopes what GRH structurally commits to about interaction vertices and how the vertex structure realises (a) the gauge-quotient individuation at the vertex level (R-2 completion via V3) and (b) the vertex-anchored commitment for $\tau_g$ (R-3 via V4 with V1 taxonomy + V2 minimal-coupling supporting), decomposing into five sub-features — vertex taxonomy under GRH (V1, forced-via-derivation), minimal coupling as structural vertex (V2, forced-via-derivation), vertex-level gauge-quotient individuation (V3, load-bearing for R-2 completion), vertex-anchored commitment (V4, load-bearing for R-3), downstream dependency map (V5, bookkeeping) — operating on Primitives 02/04/06/07/10/11 plus inherited FORCED items (Theorems 1–16) plus Q.2's CLOSED CANDIDATE-FORCED structural commitments (non-Abelian admissibility, kinematic gauge-quotient, L3-interface gauge-invariance), with strict forbidden-input discipline (R-1, R-5, all Q.7/Q.8 results, all SM specifics, Higgs, generations, coupling constants, F-M8 cascade target, standard QFT vertex Lagrangians as derivation premise) preserving acyclicity, anticipated to close affirmatively with R-2 completion and R-3 both at CANDIDATE-FORCED, advancing the GRH closure trajectory to Q.7 (lightlike-worldline reformulation, R-1 + R-5 partial) with the cumulative refinement count rising from 2/7 closed (post-Q.2) to 4/7 closed (post-Q.3) and three remaining for Q.7 + Q.8.

---

## Recommended Next Steps

**(a) Begin Q.3 Memo 01 (V1 + V2 + V4 partial; R-3 partial closure).** The natural next deliverable. Following the section outline in §10, Memo 01 should: (i) derive V1 vertex taxonomy via primitive-by-primitive admissibility check; (ii) derive V2 minimal coupling at vertex level by promoting R.1's content; (iii) begin V4 vertex-anchored commitment specification; (iv) dispatch falsifiers VFal-1, VFal-3, VFal-5, VFal-6; (v) state R-3 partial closure. Anticipated length: comparable to Q.2 Memo 01.

**(b) Pre-Memo-01 audit of Primitive 11's commitment-dynamics specification.** A 30–45 minute read of Primitive 11's specification (`quantum/primitives/11_*.md`) targeting the question: does Primitive 11 admit vertex-anchored commitment as a structural alternative to worldline-intrinsic commitment, or does it specify worldline-anchored commitment as the only admissible form? The answer determines V4's substantive content (light verification vs. heavy reformulation work). Particularly important for VFal-8 dispatch.

**(c) Verify the higher-order vertex exclusion claim noted in §7.1.** A short derivation (2–3 paragraphs) confirming that 5-gauge and higher vertex types are structurally excluded by primitive-level constraints (likely from Lorentz covariance + L3-interface specifications + Lie-algebra structure-constant content). This is a Memo 01 sub-derivation but worth pre-checking now.

**(d) Defer memory-record update until Q.3 closure (Memo 03).** Per the discipline established in U3 / U4 / U5 arcs and the GRH closure roadmap §10. The bundled memory update will capture all of: R-2 completion closed, R-3 closed, Q.3 substage verdict, downstream handoffs to Q.7 / Q.8, cumulative refinement-closure status (anticipated 4/7 closed post-Q.3).

**(e) (Optional) Sketch Q.7 Memo 00 outline now.** With Q.3 substantive work scoped (Memo 00 done; Memos 01–03 anticipated), the Q.7 Memo 00 outline can be drafted in skeleton form: lightlike-worldline reformulation (R-1), vacuum-vs-particle status partial (R-5 partial), second-quantisation framework, sub-features, falsifier inventory, dependency map. Drafting now would let Q.7 land into a known scope when Q.3 closes; optional but useful for trajectory planning.
