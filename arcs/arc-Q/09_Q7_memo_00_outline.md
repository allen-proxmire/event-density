# Q.7 Substage — Examination Outline (Memo 00)

**Stage:** Arc Q · Q.7 (second quantisation + lightlike-worldline reformulation)
**Date opened:** 2026-04-26
**Location:** `arcs/arc-Q/`
**Goal:** Discharge **R-1** (lightlike-worldline reformulation for $\tau_g$), **R-5 partial** (vacuum-field aspect of $\tau_g$'s vacuum-vs-particle status), and **the Q.7-side of R-3** (per-worldline accounting integrating Q.3's vertex-anchored commitment into the lightlike-worldline framework). Establish the second-quantised field / worldline correspondence for $\tau_g$ that the GRH closure trajectory needs.
**Predecessors:** [`grh_evaluation.md`](grh_evaluation.md) (Q.1) · [`00_grh_closure_roadmap.md`](00_grh_closure_roadmap.md) · Q.2 substage CLOSED CANDIDATE-FORCED (Memos 01-04 of Q.2 trajectory) · Q.3 substage CLOSED CANDIDATE-FORCED (Memos 05-08 of Q.3 trajectory) · [`08_Q3_memo_03_verdict.md`](08_Q3_memo_03_verdict.md) (Q.3 Memo 03 — Q.3 verdict + cascade map)
**Status:** Scoping memo. Defines Q.7's question, sub-feature decomposition, structural inputs, forbidden inputs, falsifier inventory, expected deliverables, dependency graph, and honest scope limits. Inherits Q.2 + Q.3's CLOSED CANDIDATE-FORCED commitments (gauge-group admissibility, kinematic + vertex-level gauge-quotient, vertex taxonomy, minimal coupling, vertex-anchored commitment Q.3-side) as background.
**Purpose:** Pin down the Q.7 terrain so subsequent Q.7 memos (Memo 01: lightlike-worldline reformulation; Memo 02: second-quantisation framework; Memo 03: vacuum-field aspect; Memo 04: verdict + cascade) can target specific load-bearing items without re-scoping. Q.7 is anticipated to be the substantively heaviest substage of the GRH closure trajectory due to the full second-quantisation framework requirement.

---

## 1. The Q.7 Question

### 1.1 Precise statement

Q.7 asks: **how do τ_g and the GRH structure lift from single-vertex / single-worldline (Q.3) to the full second-quantised field / worldline framework, given that τ_g has a lightlike worldline (no rest frame, no proper-time parametrisation)?**

More formally: given Q.3's vertex content (V1 four-vertex taxonomy; V2 minimal-coupling vertex form; V3 vertex-level gauge-quotient individuation; V4 Q.3-side vertex-anchored commitment for $\tau_g$), what is the structural framework for $\tau_g$'s propagation between vertices on its lightlike worldline, how does the Phase-1 commitment-dynamics specification (which assumed timelike worldlines parametrised by proper time $\tau_K$) reformulate for the lightlike case, and what is the structural status of $\tau_g$ as a vacuum-occupying background field versus as a propagating particle (creation/annihilation quanta)?

The answer must specify:
- The **affine-parameter machinery** for $\tau_g$'s lightlike worldline (replacing proper-time parametrisation that fails when $d\tau = 0$).
- The **per-worldline accounting** for Phase-1 commitment-dynamics in the affine-parameter framework, integrating Q.3's vertex-density-dependent commitment rate.
- The **second-quantised field / worldline correspondence** for $\tau_g$ (creation/annihilation operator structure; propagator content; relationship between the field $A^a_\mu(x)$ and the particle interpretation as $\tau_g$ quanta).
- The **vacuum-field aspect** of $\tau_g$ (the background-field interpretation; what $\tau_g$ looks like in a vacuum state; partial — full vacuum-state machinery is Q.8 work).

### 1.2 Q.7's position in the GRH-closure trajectory

The GRH closure roadmap sequences Q.7 as the third substage: Q.2 → Q.3 → **Q.7** → Q.8 → Arc Q synthesis → cascade to Arc M.

Q.7 sits structurally between Q.3 (vertex-level / single-vertex commitment) and Q.8 (full vacuum + zero-point). It is the lifting substage:

- **Q.3 supplied** vertex content (taxonomy, minimal coupling, vertex-level gauge-quotient, vertex-anchored commitment Q.3-side) at the single-vertex level.
- **Q.7 must establish** the lifting to per-worldline accounting + second-quantised framework + vacuum-field aspect — bridging from single-vertex content to a full quantum-field framework.
- **Q.8 will inherit** Q.7's framework + complete the vacuum-state structure (zero-point, vacuum polarisation, full vacuum-vs-particle reconciliation).

Q.7 is therefore the **substantive bridge** between vertex-level kinematics+dynamics (Q.3) and the full vacuum framework (Q.8). It carries the largest substantive load of any GRH closure substage.

### 1.3 Refinements Q.7 is responsible for

| Refinement | Description | Q.7 sub-feature(s) |
|---|---|---|
| **R-1** | Lightlike-worldline reformulation | W1 + W2 |
| **R-5 partial** | Vacuum-field aspect of $\tau_g$'s status | W3 + W5 |
| **R-3 Q.7-side** | Per-worldline accounting integrating vertex-anchored commitment | W4 |

Q.7 closes 2 of the 3 refinement items remaining after Q.3 (R-1 + R-5 partial). The remaining 1 (R-5 completion) is Q.8 content. R-3's Q.7-side is also closed at Q.7 (final R-3 closure pending Q.8 R-5 completion).

### 1.4 Possible verdicts

- **CLOSED — CANDIDATE-FORCED.** R-1, R-5 partial, R-3 Q.7-side all close affirmatively. Anticipated default mirroring Q.2 / Q.3 closure pattern.
- **CLOSED — CANDIDATE-admissible.** Refinements close but with weaker structural support than CANDIDATE-FORCED.
- **PARTIAL.** Some refinements close; others reveal structural gaps requiring sub-arc work.
- **REFUTED.** Some refinement reveals a primitive-level obstruction blocking GRH closure at the second-quantisation level. Would force major restructuring.

---

## 2. Decomposition into Sub-Features

Q.7 packages **six** structurally distinct sub-features. Each must be settled independently for Q.7 closure.

### 2.1 (W1) Lightlike-Worldline Structure Under GRH

- **Definition.** Establish the affine-parameter machinery for $\tau_g$'s lightlike worldline $\gamma_{\tau_g}$: a smooth parameter $\lambda$ such that the tangent vector $dx^\mu/d\lambda$ along $\gamma_{\tau_g}$ is well-defined and normalised in a structurally consistent way (for null curves, the natural normalisation is by an affine-parameter choice rather than the proper-time normalisation that fails when $d\tau = 0$).
- **Structural commitment.** $\tau_g$'s lightlike worldline carries an affine-parameter $\lambda$, with per-worldline content (commitment rates, vertex-density measurements) parametrised by $\lambda$ rather than by proper time.
- **Falsifier.** W1 fails if (a) no affine-parameter machinery is structurally admissible for $\tau_g$'s lightlike worldline (would force restriction of GRH to massive gauge rule-types, conflicting with GRH-4), or (b) the affine parameter introduces structural inconsistencies (e.g., parameter-choice ambiguity that changes physical observables).
- **Out of scope.** W1 does not address vacuum-state worldline content (Q.8); does not specify which field-theoretic propagator content is generated by the affine-parameter machinery (W2 work).
- **Status:** **forced-via-derivation** (anticipated). Affine-parameter machinery for null curves is standard differential geometry; W1 verifies primitive-level admissibility.

### 2.2 (W2) Second-Quantised Field / Worldline Correspondence

- **Definition.** Establish the structural correspondence between $\tau_g$ as a quantum field $A^a_\mu(x)$ and $\tau_g$ as a per-worldline propagating rule-type with creation/annihilation operator structure. Specify the propagator content for $\tau_g$ between vertices: how the field propagates from one interaction vertex (V1 type T1, T2, T3, T4) to the next along $\tau_g$'s lightlike trajectory.
- **Structural commitment.** $\tau_g$ admits both interpretations: as a quantum field (entire spatial extent, all configurations) and as per-worldline propagating quanta (creation at one vertex, propagation to another, annihilation). The two interpretations are complementary and structurally consistent.
- **Falsifier.** W2 fails if the field / particle correspondence is structurally inconsistent — e.g., if creation/annihilation operators cannot be defined consistently with Theorem 6 (canonical (anti-)commutation relations), or if propagator content is incompatible with Theorem 7 (UV-FIN — propagators must be finite without renormalisation).
- **Out of scope.** W2 does not specify scattering amplitudes (built from W2's framework but requiring multi-vertex computations); does not specify renormalisation procedures (Q.7 commits to UV-finiteness via Theorem 7 inheritance, but does not derive renormalisation prescriptions).
- **Status:** **load-bearing** (R-1 core).

### 2.3 (W3) τ_g Excitation vs. Background at the Worldline Level (R-5 Partial)

- **Definition.** Establish the structural distinction between $\tau_g$ as a background field (vacuum-occupying field configuration $\langle A^a_\mu \rangle$) and $\tau_g$ as a particle excitation (propagating quanta with creation/annihilation structure on top of the background). At the worldline level, this is the question of when $\tau_g$ contributes to the global background versus when it contributes to per-worldline propagating content.
- **Structural commitment.** $\tau_g$ admits a background-field aspect: in the absence of vertex events along a region of spacetime, $\tau_g$ is described by its background-field configuration (the global field $A^a_\mu$ as a structural object). Particle-aspect content (creation/annihilation of $\tau_g$ quanta) is on top of this background, sourced at vertex events.
- **Falsifier.** W3 fails if the background / particle distinction cannot be specified consistently — e.g., if background-field content cannot be cleanly separated from particle content (would force a more limited interpretation of $\tau_g$).
- **Out of scope.** W3 does not address the *zero-point* aspect (vacuum fluctuations, virtual particle pairs) — this is R-5 completion (Q.8). W3 only addresses the *background-field* aspect at the worldline level (R-5 partial).
- **Status:** **load-bearing** (R-5 partial).

### 2.4 (W4) Vertex-to-Worldline Lifting of Commitment Events (R-3 Q.7-Side)

- **Definition.** Establish the per-worldline accounting that lifts Q.3 V4's vertex-anchored commitment specification (commitment events sourced at V1 vertex types with vertex-density-dependent rate) to the affine-parameter framework of W1. Specifically: integrate Q.3's vertex-density commitment rate with Phase-1's per-worldline commitment-rate accounting, with proper-time parametrisation replaced by affine-parameter parametrisation.
- **Structural commitment.** The per-worldline commitment-event rate for $\tau_g$ is computed by integrating the vertex density along $\gamma_{\tau_g}$ in the affine-parameter framework. Phase-1's commitment-dynamics specification is fully reconciled with the lightlike + vertex-anchored framework.
- **Falsifier.** W4 fails if the lifting introduces structural inconsistencies — e.g., if the affine-parameter measure on the lightlike worldline is incompatible with the vertex-density measure from Q.3, or if the reconciliation requires content beyond Q.7's primitive-level inputs.
- **Out of scope.** W4 does not address vacuum-state vertex content (Q.8 work); does not derive specific scattering amplitudes from the per-worldline accounting.
- **Status:** **load-bearing** (R-3 Q.7-side).

### 2.5 (W5) Pre-Vacuum Structure (What Q.7 Can Say Before Q.8)

- **Definition.** Establish what Q.7's framework can say about $\tau_g$'s vacuum-related content *before* Q.8's full vacuum + zero-point work. Specifically: identify which vacuum-structural commitments are settled at Q.7 (background field configuration; absence of particle excitations at the worldline level; vacuum-field aspect of R-5 partial) and which are deferred to Q.8 (zero-point fluctuations; full vacuum-state structure; vacuum polarisation; reconciliation with Λ-from-V₁ derivation per Phase-3 background).
- **Structural commitment.** Q.7 specifies the vacuum-field-aspect content: the background field $\langle A^a_\mu \rangle$ as a primitive-level structural object, with absence of particle excitations as the "no vertex events" condition. Q.8 will add zero-point fluctuations as additional vacuum structure.
- **Falsifier.** W5 fails if Q.7's pre-vacuum content cannot be separated cleanly from Q.8's full vacuum content — e.g., if the background-field aspect requires zero-point content for its definition (would create Q.7 → Q.8 → Q.7 circular dependency).
- **Out of scope.** W5 does not specify zero-point fluctuations (Q.8 R-5 completion); does not address vacuum-energy contributions to Λ (Q.8 work integrating with Phase-3 V₁ kernel).
- **Status:** **forced-via-derivation** (Q.7-side honest scoping; bookkeeping).

### 2.6 (W6) Downstream Dependency Map for Q.8

- **Definition.** Specify what Q.8 (vacuum + zero-point + R-5 completion) must inherit from Q.7's closure — i.e., produce the precise structural-content handoffs Q.8 will use as background.
- **Structural commitment.** Q.7 issues a closure-state inventory: which content is settled (background field aspect, second-quantisation framework, lightlike-worldline machinery, per-worldline commitment accounting), which is deferred to Q.8 (zero-point, full vacuum-state, vacuum polarisation, Λ reconciliation).
- **Falsifier.** W6 fails if Q.7's closure cannot be cleanly handed off — e.g., if zero-point content (Q.8) requires Q.7's framework in a way that creates circular dependencies.
- **Out of scope.** W6 does not execute Q.8; only specifies what Q.8 inherits.
- **Status:** **forced-via-derivation** (bookkeeping).

### 2.7 Status Classification

| Sub-feature | Status | Reasoning |
|---|---|---|
| **W1** Lightlike-worldline structure | forced-via-derivation | Affine-parameter machinery is standard differential geometry; verifies primitive-level admissibility |
| **W2** Second-quantised field/worldline correspondence | **load-bearing** (R-1 core) | The substantive R-1 question; carries the second-quantisation framework load |
| **W3** Excitation vs. background (R-5 partial) | **load-bearing** (R-5 partial) | The substantive R-5 partial question; closure determines vacuum-field aspect |
| **W4** Vertex-to-worldline lifting (R-3 Q.7-side) | **load-bearing** (R-3 Q.7-side) | Reconciliation of Phase-1 commitment with lightlike-worldline framework |
| **W5** Pre-vacuum structure | forced-via-derivation | Honest-scoping; bookkeeping |
| **W6** Downstream dep map | forced-via-derivation | Bookkeeping integration |

Three load-bearing items (W2, W3, W4) — substantively heavier than Q.2 / Q.3 (which had two load-bearing each). This reflects Q.7's role as the lifting substage carrying both the second-quantisation framework requirement and the vacuum-field aspect.

---

## 3. Refinement Mapping

The three refinements assigned to Q.7 map onto the sub-features:

| Refinement | Maps primarily to | Supporting sub-features | Closure expected at |
|---|---|---|---|
| **R-1** Lightlike-worldline reformulation | W1 + W2 | W4 (per-worldline accounting integration) | Q.7 Memo 01 (W1 + W2 substantive derivation) |
| **R-5 partial** Vacuum-field aspect | W3 + W5 | W2 (field interpretation supplies the background-field aspect) | Q.7 Memo 02 (W3 substantive; W5 honest scoping) |
| **R-3 Q.7-side** Per-worldline accounting | W4 | W1 (affine-parameter machinery supplies the parametrisation) | Q.7 Memo 02 (W4 substantive) or Memo 03 (integration) |

R-1 closes if W1 (affine-parameter machinery) and W2 (second-quantised correspondence) both close. R-5 partial closes if W3 (background-field aspect) and W5 (pre-vacuum scoping) both close. R-3 Q.7-side closes if W4 (vertex-to-worldline lifting) closes.

**Load-bearing items: W2, W3, W4.** Three substantive sub-features; one forced-via-derivation (W1); two bookkeeping (W5, W6). The substantive load is heavier than Q.2 / Q.3 due to the second-quantisation framework requirement.

**GRH-3 load-bearing relevance.** W2 (second-quantised field/worldline correspondence) and W4 (vertex-to-worldline commitment lifting) are both directly load-bearing for GRH-3 (the L3-interface clause): the second-quantisation framework realises GRH-3's gauge-invariance constraint at the operator level, and the per-worldline commitment lifting realises it at the dynamical-events level.

---

## 4. Structural Inputs

### 4.1 Primitives drawn upon

- **Primitive 02** (worldline + ambient 3+1D manifold). Worldline-relevant content: $\tau_g$'s lightlike worldline structure; affine-parameter parametrisation; null curves on the manifold.
- **Primitive 04** (bandwidth fields). Worldline-relevant content: per-worldline bandwidth flow; vertex-density measurements along $\tau_g$'s trajectory.
- **Primitive 06** (four-gradient + Lorentz covariance). Worldline-relevant content: tangent vectors along worldlines; Lorentz transformations of the affine parameter.
- **Primitive 07** (rule-type taxonomy). Worldline-relevant content: L3 interface specifies how $\tau_g$ propagates between vertex events.
- **Primitive 10** (individuation threshold). Worldline-relevant content: per-worldline individuation of $\tau_g$ rule-type instances; second-quantised individuation respecting gauge equivalence (per Q.3 V3 inheritance).
- **Primitive 11** (commitment dynamics). Worldline-relevant content: **the central primitive for W4 (Q.7-side of R-3).** Per-worldline commitment-rate specification in the affine-parameter framework.
- **Primitive 13** (relational timing) — *implicitly* relevant for R-1's affine-parameter / proper-time relationship. The affine parameter is structurally a generalisation of proper time for null curves; Primitive 13's specification of relational time admits this generalisation.

### 4.2 Inherited FORCED upstream items

- **Theorems 1–9** (Phase-2 + Arc N + Phase-3 closures): background. Theorem 6 (canonical (anti-)commutation, Q.7) is **directly relevant** for W2's second-quantised framework — operator structure must be consistent with canonical (anti-)commutation. Theorem 7 (UV-FIN, Q.8) is **directly relevant** for W2's propagator content — propagators must be finite without renormalisation.
- **Theorem 8** (V₁ finite-width vacuum kernel, Arc N) is **directly relevant** for W3 + W5 — the V₁ kernel governs vacuum-state two-point correlations; W3's background-field aspect must be consistent with V₁'s finite-width structure.
- **Theorem 9** (V₁ with Synge world function, Phase-3) is relevant for W3 + W5 — the V₁ kernel extends to curved spacetime via Hadamard parametrix; W3's background-field interpretation must accommodate this extension at the structural level.
- **Theorems 10–16** (Phase-1 closure): background. Theorem 16 (U3, Schrödinger evolution) is most relevant — the time-evolution framework that Q.7's per-worldline accounting fits into.
- **Q.2 substage closure** (R-4 + R-2 partial CANDIDATE-FORCED). Non-Abelian admissibility and kinematic gauge-quotient inherited.
- **Q.3 substage closure** (R-2 completion + R-3 Q.3-side CANDIDATE-FORCED). Vertex taxonomy (V1), minimal coupling (V2), vertex-level gauge-quotient (V3), vertex-anchored commitment (V4 Q.3-side) all inherited as background.

### 4.3 GRH-1 through GRH-4 (background, with Q.2 + Q.3 generalisations)

Q.7 takes the four GRH clauses as background, with Q.2 + Q.3's generalisations:

- **(GRH-1)** $\tau_g$ Case P — at second-quantised level: $\tau_g$ creation/annihilation operators satisfy bosonic commutation $[a, a^\dagger] = \delta$ per Theorem 6.
- **(GRH-2)** $\tau_g$ (1/2, 1/2) Lorentz rep — at second-quantised level: $A^a_\mu$ field carries the four-vector representation.
- **(GRH-3)** L3 interface enforces gauge invariance — at second-quantised level: operator content is gauge-invariant; load-bearing for W2 + W4.
- **(GRH-4)** $\sigma_{\tau_g} = 0$ via MR-P — at second-quantised level: $\tau_g$ propagator is massless (lightlike worldline confirmed by W1).

### 4.4 Q.3 vertex content (background, not premise)

Q.3 substage's V1 (vertex taxonomy), V2 (minimal coupling vertex form), V3 (vertex-level gauge-quotient), V4 Q.3-side (vertex-anchored commitment) supply Q.7's vertex-content background. Q.7 uses these as *content* (the structural objects that Q.7's framework must accommodate) but does not re-derive them or invoke their derivation chains as Q.7-specific premises.

The discipline: **Q.3 establishes vertex content; Q.7 establishes how vertex content lifts to second-quantised + worldline-propagation framework.** Q.7 uses Q.3's content but does not re-derive it.

### 4.5 R.1 minimal coupling content + M.1.2 commitment-event framework (background)

R.1's minimal-coupling content (origin of $A_\mu$ for U(1), generalised to non-Abelian per Q.2 Memo 01) and M.1.2's commitment-event framework (origin of GRH; massless rule-types via MR-P) are background. Q.7 uses these as *content* but does not invoke their derivation chains.

### 4.6 Mathematical infrastructure

- **Standard differential-geometric machinery for null curves** (affine parameters, tangent vectors, Lie derivatives along null directions). Background; not derivation premise.
- **Standard second-quantisation framework** (creation/annihilation operators, Fock space construction, normal ordering — caveat: normal ordering is a Q.8 question; Q.7 commits to operator structure but defers normal-ordering specifics). Background; ED's analog must be derived from primitives, not imported.
- **Standard QFT propagator structure** (Feynman propagator, retarded/advanced propagators). Background only — Q.7 verifies that ED's propagator content reduces to standard propagator structure in the appropriate limit, but does NOT invoke standard propagator forms as derivation premise.

### 4.7 Scope conditions

- **Non-relativistic + relativistic single-particle scopes** (inherited from Phase-1 + Arc R; relevant for the second-quantisation framework's scope).
- **3+1D Minkowski background** (inherited).
- **Compact Lie group gauge structure** (Q.2 inheritance).
- **Lightlike scope for $\tau_g$** (per GRH-4; Q.7's central scope condition for W1 + W2).

---

## 5. Forbidden Inputs (Acyclicity Discipline)

Per the GRH closure roadmap §7 + Q.2 / Q.3 disciplines, the following inputs are explicitly forbidden as Q.7 derivation premises:

### 5.1 Substage-cross-contamination forbidden inputs

- **R-5 completion (zero-point aspect)** — Q.8 content. *Justification:* Q.8 work is downstream; using zero-point content here would invert dependencies.
- **Any Q.8 results** (full vacuum state, vacuum polarisation, virtual vertex pairs, Λ-from-V₁ derivation specifics). *Justification:* Q.8 is downstream.
- **Vacuum-state vertex content** at the full quantum level. *Justification:* Q.7 commits to background-field aspect (R-5 partial); full vacuum-state work is Q.8.

### 5.2 Standard Model specifics forbidden inputs

- **U(1) hypercharge assignments, SU(2) weak isospin, SU(3) color, electroweak / QED / QCD second-quantised content.** Empirical SM content. *Justification:* Q.7 establishes the second-quantisation framework structurally; specific SM content is empirical inheritance.
- **Specific QED, QCD, electroweak Feynman rules** — empirical SM content.
- **Yang-Mills Lagrangian with specific gauge group** — out of scope.
- **Spontaneous symmetry breaking** — Q.4 content.

### 5.3 Higgs sector forbidden inputs

- **Higgs field, Higgs propagator, Higgs vacuum expectation value** — Q.4 content.
- **W / Z boson mass-generation via SSB** — Q.4 content.

### 5.4 Generation structure forbidden inputs

- **Number of generations, flavor structure, generation-specific propagator content** — Q.6 / empirical.

### 5.5 Empirical coupling constants forbidden inputs

- **Coupling constant values** ($q$, $g_s$, $g_w$). *Justification:* Q.7 establishes structural framework; values are inherited.
- **Charge quantization pattern.**

### 5.6 Cascade-target forbidden inputs

- **F-M8 (massless slot existence, FORCED-conditional)** — the cascade target, not a premise.
- **F-GRH-A through F-GRH-E** (the cascade items).

### 5.7 Standard QFT machinery forbidden inputs

- **Yang-Mills Lagrangian as a postulate** — derivation target if anywhere; not premise.
- **Faddeev-Popov ghost vertices, BRST quantization** — would be Q.7 substantive content if derivable from primitives, but cannot be invoked as derivation premise.
- **Path-integral measure (gauge-fixed or otherwise)** — Q.8 content if derivable; not premise here.
- **Renormalization-group equations** — Q.8 content.
- **Specific renormalisation prescriptions** (dimensional regularisation, lattice regularisation, Pauli-Villars). Not derivation premise; ED's UV-finiteness via Theorem 7 inheritance avoids the need.

---

## 6. Falsifier Inventory

Q.7 closes affirmatively if all six sub-features (W1–W6) close uniquely under the available structural inputs. The following falsifiers state how each sub-feature could fail. Some are Q.7-specific; some are inherited from Q.3's downstream-test list.

### 6.1 Q.7-specific falsifiers

- **(WFal-1) Lightlike-worldline reformulation primitive incompatibility.** No affine-parameter machinery is structurally admissible for $\tau_g$'s lightlike worldline; some primitive (P-02, P-06, P-13) forbids the affine-parameter parametrisation. *Targets W1.* *Anticipated dispatch:* Q.7 Memo 01 primitive-level audit.

- **(WFal-2) Second-quantised framework incompatibility with ED primitives.** ED's primitive-level structure (Primitive 04 bandwidth, Primitive 07 L3 interface, Primitive 11 commitment dynamics) cannot accommodate the creation/annihilation operator structure that Theorem 6 supplies. *Targets W2.* *Anticipated dispatch:* Q.7 Memo 01 / Memo 02.

- **(WFal-3) Vacuum-field aspect cannot be defined consistent with R-5 partial.** The background-field aspect of $\tau_g$ cannot be cleanly separated from the particle-excitation aspect at the worldline level — would force a more limited interpretation of $\tau_g$. *Targets W3.* *Anticipated dispatch:* Q.7 Memo 02.

- **(WFal-4) Vertex-to-worldline lifting fails (Q.7-side of R-3).** The per-worldline accounting cannot integrate Q.3's vertex-density commitment rate with Phase-1's commitment-dynamics specification — would force restriction of GRH content to massive gauge rule-types (conflicting with GRH-4) or require revising the Phase-1 commitment-dynamics specification. *Targets W4.* *Anticipated dispatch:* Q.7 Memo 02.

- **(WFal-5) Q.7 ⟷ Q.8 circular dependency.** Q.7's closure (especially W3 background-field aspect or W5 pre-vacuum scoping) requires Q.8's full vacuum-state content for its own definition. *Targets W5 + W6.* *Anticipated dispatch:* Q.7 Memo 03 (verdict + cascade) dependency-map audit.

### 6.2 Inherited / downstream-test falsifiers from Q.3

- **(WFal-6) Theorem 6 inconsistency with worldline structure.** Canonical (anti-)commutation relations (Theorem 6) cannot be specified consistently with $\tau_g$'s lightlike-worldline structure — would force restructuring of either Theorem 6 or W1. *Targets W2.* *Anticipated dispatch:* Q.7 Memo 01 / Memo 02 verification of Theorem 6 inheritance.

- **(WFal-7) Phase-1 commitment-dynamics incompatibility.** Primitive 11's general specification (worldline-intrinsic commitment events as primitive-level dynamical content) cannot be reconciled with the lightlike-worldline + vertex-anchored framework even with affine-parameter machinery — would force revision of Primitive 11. *Targets W4.* *Anticipated dispatch:* Q.7 Memo 02.

- **(WFal-8) UV-FIN conflict with second-quantised vertex amplitudes.** Theorem 7 (UV-FIN) requires propagators to be finite without renormalisation; the second-quantised vertex amplitudes (built from W2's framework + Q.3's vertex content) introduce divergences that violate this. *Targets W2.* *Anticipated dispatch:* Q.7 Memo 02 verification of Theorem 7 inheritance.

### 6.3 Falsifier-source taxonomy

| Falsifier | Targets | Source layer | Anticipated dispatch |
|---|---|---|---|
| WFal-1 (W1 primitive incompat.) | W1 | Primitive | Q.7 Memo 01 |
| WFal-2 (second-quant. incompat.) | W2 | Primitive + Theorem 6 | Q.7 Memo 01 / 02 |
| WFal-3 (vacuum-field aspect) | W3 | Q.7-specific | Q.7 Memo 02 |
| WFal-4 (vertex-to-worldline lifting) | W4 | Q.7-specific (R-3 Q.7-side) | Q.7 Memo 02 |
| WFal-5 (Q.7 ⟷ Q.8 circular) | W5, W6 | Methodological | Q.7 Memo 03 |
| WFal-6 (Theorem 6 incompat.) | W2 | Inherited theorem | Q.7 Memo 01 / 02 |
| WFal-7 (P-11 incompat. lifting) | W4 | Inherited primitive (P-11 full reconciliation) | Q.7 Memo 02 |
| WFal-8 (UV-FIN conflict) | W2 | Inherited theorem | Q.7 Memo 02 |

Three Q.7-specific (WFal-3, WFal-4, WFal-5); three inherited theorem / primitive checks (WFal-6, WFal-7, WFal-8); two primitive-level (WFal-1, WFal-2). Pattern matches Q.2 / Q.3 load distributions.

---

## 7. Expected Deliverables

Q.7 closure must produce:

### 7.1 Affine-parameter machinery for τ_g

A clean specification of the affine-parameter $\lambda$ along $\tau_g$'s lightlike worldline, with: tangent-vector normalisation, parameter-shift admissibility (affine reparametrisations $\lambda \to a\lambda + b$), Lorentz-transformation behaviour. Anticipated form: standard differential-geometric affine parametrisation for null curves, verified at primitive-level.

### 7.2 Per-worldline accounting integrated with vertex-density commitment rate

A precise reconciliation of Q.3 V4's vertex-density commitment rate with Primitive 11's per-worldline commitment-dynamics specification, in the affine-parameter framework. The reconciliation should produce: $d N_{\mathrm{commit}} / d\lambda = \rho_V(\lambda)$, where $\rho_V$ is the local vertex density along $\tau_g$'s worldline at affine parameter $\lambda$.

### 7.3 Second-quantised field / particle correspondence

A clean specification of the relationship between $A^a_\mu(x)$ as a quantum field (defined on the spacetime manifold) and $\tau_g$ as per-worldline propagating quanta (creation/annihilation operators). Includes: operator structure consistent with Theorem 6; propagator content (between vertex events) consistent with Theorem 7 (UV-FIN).

### 7.4 Vacuum-field interpretation of τ_g (R-5 partial)

A precise specification of $\tau_g$'s background-field aspect: the field configuration $\langle A^a_\mu \rangle$ as a primitive-level structural object; the "no vertex events" condition characterising the absence of particle excitations; the structural content distinguishing background from excitation.

### 7.5 Closure plan for R-1, R-5 partial, R-3 Q.7-side

- **R-1 closure statement:** affine-parameter machinery established (W1); second-quantised framework operative (W2).
- **R-5 partial closure statement:** vacuum-field aspect of $\tau_g$ specified (W3); pre-vacuum scoping clean (W5).
- **R-3 Q.7-side closure statement:** per-worldline accounting integrating vertex-anchored commitment fully reconciled with Primitive 11 (W4).

### 7.6 Dependency map for Q.8

A precise inventory of what Q.8 inherits from Q.7's closure:

| Q.8 sub-feature (anticipated) | Q.7 inheritance | Q.8 deliverable |
|---|---|---|
| Vacuum state structure | Vacuum-field aspect (W3); pre-vacuum scoping (W5) | Full vacuum state with zero-point fluctuations |
| Zero-point fluctuations | Second-quantised operator framework (W2) | Specific zero-point content; reconciliation with V₁ kernel |
| Vacuum polarisation | Propagator content (W2); vertex content from Q.3 | Vacuum polarisation diagrams; renormalisation-style content |
| Λ from vacuum-vertex content | V₁ vacuum kernel (Theorem 8 + Theorem 9 inheritance) | Λ derivation refinement |

### 7.7 Verdict

Anticipated: **R-1, R-5 partial, R-3 Q.7-side all close affirmatively (CANDIDATE-FORCED); Q.7 substage CLOSED — CANDIDATE-FORCED; GRH closure trajectory advances to Q.8.**

---

## 8. Dependency Graph

### 8.1 Substage dependencies (post-Q.3)

```
                  Q.0 (scoping)              ← background
                       ↓
                  Q.1 (GRH evaluation)        ← background
                       ↓
                  Q.2 (gauge group scoping)   ← CLOSED CANDIDATE-FORCED
                       ↓
                  Q.3 (vertex classification) ← CLOSED CANDIDATE-FORCED
                       │  (R-2 FULLY closed; R-3 Q.3-side closed)
                       ↓
            ┌─────  Q.7 (THIS substage)  ─────┐
            │  W1 (lightlike worldline)        │
            │  W2 (second-quantised corresp.)  │  ← discharges R-1 (load-bearing)
            │  W3 (excitation vs background)   │  ← discharges R-5 partial (load-bearing)
            │  W4 (vertex-to-worldline lift)   │  ← discharges R-3 Q.7-side (load-bearing)
            │  W5 (pre-vacuum structure)       │
            │  W6 (downstream dep map)         │
            └────────────┬─────────────────────┘
                         ↓
              Q.8 (vacuum and zero-point)       ← discharges R-5 completion
                         ↓
              Arc Q synthesis                   ← promotes GRH to FORCED-uncond.
                         ↓
              Cascade to Arc M                  ← F-M8 promoted to FORCED-uncond.
                         ↓
              Theorem 17 added to inventory
```

### 8.2 Refinement-to-substage closure map (post-Q.3 update)

| Refinement | Status | Closure stage |
|---|---|---|
| **R-1 (lightlike worldline)** | **outstanding** | **Q.7 (W1 + W2)** |
| R-2 partial | ✅ CLOSED CANDIDATE-FORCED | Q.2 Memo 02 |
| R-2 completion | ✅ CLOSED CANDIDATE-FORCED | Q.3 Memo 02 |
| R-2 FULL | ✅✅ FULLY CLOSED | Q.2 + Q.3 |
| R-3 Q.3-side | ✅ CLOSED CANDIDATE-FORCED | Q.3 Memo 02 |
| **R-3 Q.7-side (per-worldline lift)** | **outstanding** | **Q.7 (W4)** |
| R-4 | ✅ CLOSED CANDIDATE-FORCED | Q.2 Memo 01 |
| **R-5 partial (vacuum-field aspect)** | **outstanding** | **Q.7 (W3 + W5)** |
| R-5 completion (zero-point) | outstanding | Q.8 |

### 8.3 How Q.7's commitments constrain Q.8

**To Q.8:**
- Background-field aspect of $\tau_g$ (W3) constrains Q.8's vacuum-state definition — vacuum state extends Q.7's background-field by adding zero-point structure.
- Second-quantised operator framework (W2) constrains Q.8's zero-point content — zero-point fluctuations are computed from Q.7's operator structure plus vacuum-state machinery.
- Pre-vacuum scoping (W5) explicitly identifies what Q.8 must add to complete the vacuum framework (zero-point fluctuations, vacuum polarisation, full vacuum-state structure).
- Per-worldline commitment lifting (W4) constrains Q.8's vacuum-state vertex content — vacuum vertices must be consistent with the affine-parameter framework Q.7 establishes.

These constraints flow one-way: Q.7 → Q.8. Q.8 does not feed back into Q.7 (per WFal-5 dispatch via W5).

---

## 9. Honest Scope Limits

Q.7 explicitly cannot resolve the following — these are empirical inheritance, downstream-substage content, or out-of-scope:

- **R-5 completion (zero-point aspect).** Q.8.
- **Full vacuum state structure with zero-point content.** Q.8.
- **Vacuum polarisation diagrams + virtual vertex pairs.** Q.8.
- **Λ derivation refinement** (extension of Theorem 9's V₁ + Synge content). Q.8.
- **Specific gauge group choice.** Empirical inheritance per Q.2 F4.
- **Coupling constant values.** Empirical via Dimensional Atlas.
- **Charged-rule-type representations.** Empirical / Q.4-onward.
- **Higgs sector / SSB.** Q.4; SPECULATIVE.
- **Generation structure / flavor.** Q.6 / empirical.
- **Charge quantization pattern.** Possibly Q.2 / Q.3 partial sub-memo or empirical.
- **Specific renormalisation prescriptions** (dim reg, lattice, etc.). ED inherits UV-FIN (Theorem 7); specific prescriptions are empirical / convention.
- **Standard QFT amplitude content** (cross-sections, S-matrix elements). Built from Q.7's framework but specific computations are downstream of GRH closure.

---

## 10. Recommended Next Memo

The natural next deliverable after this Memo 00 is:

**Q.7 Memo 01 — W1 + W2: Lightlike-Worldline Reformulation + Second-Quantised Field/Worldline Correspondence (R-1 closure)**

Memo 01 should:

- Derive W1 (lightlike-worldline structure under GRH) — primitive-by-primitive admissibility check for affine-parameter machinery; verification of Lorentz behaviour; reconciliation with Primitive 13 (relational timing).
- Derive W2 (second-quantised field / worldline correspondence) — operator structure consistent with Theorem 6 (canonical (anti-)commutation); propagator content consistent with Theorem 7 (UV-FIN); field/particle correspondence cleanly specified.
- Dispatch falsifiers WFal-1, WFal-2, WFal-6, WFal-8.
- State R-1 closure verdict (anticipated CANDIDATE-FORCED).

Anticipated length: **substantively heavier than Q.2 / Q.3 Memo 01s** due to the second-quantisation framework requirement.

After Memo 01, Memo 02 would address W3 (background-field aspect, R-5 partial) and W4 (vertex-to-worldline lifting, R-3 Q.7-side). Memo 03 would address W5 (pre-vacuum structure) + W6 (downstream dependency map) + verdict.

Q.7 may need a **Memo 04** if the second-quantisation framework requires more substantive work than fits in three memos. To be assessed after Memo 02.

---

## 11. One-Line Summary

> Q.7 substage scopes how $\tau_g$ and the GRH structure lift from single-vertex / single-worldline (Q.3) to the full second-quantised + lightlike-worldline framework, decomposing into six sub-features — lightlike-worldline structure under GRH (W1, forced-via-derivation; affine-parameter machinery for null curves), second-quantised field/worldline correspondence (W2, **load-bearing for R-1**), $\tau_g$ excitation vs background at worldline level (W3, **load-bearing for R-5 partial**), vertex-to-worldline lifting of commitment events (W4, **load-bearing for R-3 Q.7-side**), pre-vacuum structure (W5, honest scoping), downstream dependency map for Q.8 (W6, bookkeeping) — operating on Primitives 02/04/06/07/10/11 + 13 plus inherited FORCED items (Theorems 1–16, with Theorems 6/7/8/9 directly relevant) plus Q.2/Q.3's CLOSED CANDIDATE-FORCED structural commitments (gauge-group admissibility, kinematic + vertex-level gauge-quotient, vertex taxonomy + minimal coupling + vertex-anchored commitment Q.3-side), with strict forbidden-input discipline (R-5 completion + all Q.8 results forbidden, all SM specifics, Higgs/generations/coupling constants, F-M8 cascade target, standard QFT machinery as derivation premise) preserving acyclicity, anticipated to close affirmatively with R-1, R-5 partial, R-3 Q.7-side all at CANDIDATE-FORCED, advancing the GRH closure trajectory to Q.8 (R-5 completion via vacuum + zero-point work) with cumulative refinement count rising from 4/7 closed (post-Q.3) to anticipated 6/7 closed (post-Q.7) and one final R-5 completion remaining for Q.8 + Arc Q synthesis.

---

## Recommended Next Steps

**(a) Begin Q.7 Memo 01 (W1 + W2; R-1 closure).** The natural next deliverable. Following the section outline in §10, Memo 01 should: (i) derive W1 lightlike-worldline structure via primitive-by-primitive admissibility check; (ii) derive W2 second-quantised field / worldline correspondence; (iii) dispatch falsifiers WFal-1, WFal-2, WFal-6, WFal-8; (iv) state R-1 closure. Anticipated length: substantively heavier than Q.2 / Q.3 Memo 01s due to the second-quantisation framework.

**(b) Pre-Memo-01 audit of Theorem 6 (canonical (anti-)commutation) for compatibility with lightlike-worldline structure.** A 30–45 minute read of the Arc Q canonical-commutation derivation (Theorem 6, Q.7 background) to confirm: does Theorem 6's specification admit the lightlike-worldline operator structure that W2 requires, or does it impose timelike-worldline assumptions that need refinement? Particularly important for WFal-6 dispatch.

**(c) Pre-Memo-01 audit of Theorem 7 (UV-FIN) for compatibility with the propagator content W2 must specify.** A short audit confirming that Theorem 7's UV-FIN structure inherits cleanly into the second-quantised propagator framework. Important for WFal-8 dispatch.

**(d) Defer memory-record update until Q.7 closure (Memo 03 or Memo 04).** Per the discipline established. The bundled memory update will capture R-1 closure, R-5 partial closure, R-3 Q.7-side closure, Q.7 substage verdict, downstream handoffs to Q.8, cumulative refinement-closure status (anticipated 6/7 closed post-Q.7).

**(e) (Optional) Sketch Q.8 Memo 00 outline now.** With Q.7 substantive work scoped (Memo 00 done; Memos 01–04 anticipated), the Q.8 Memo 00 outline can be drafted in skeleton form: zero-point + full vacuum-state + R-5 completion; sub-features; falsifier inventory; dependency map; Arc Q synthesis preparation. Pre-sketching would let Q.8 land into a known scope; useful for trajectory planning.
