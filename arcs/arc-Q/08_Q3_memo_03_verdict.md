# Q.3 Memo 03 — Substage Verdict and Downstream Cascade

**Stage:** Arc Q · Q.3 · Memo 03 (substage closure)
**Date:** 2026-04-26
**Location:** `arcs/arc-Q/`
**Goal:** Integrate the results of Memo 01 (V1 + V2 closed CANDIDATE-FORCED; V4 partial CANDIDATE-FORCED Q.3-side; R-3 PARTIAL CLOSURE) and Memo 02 (V3 closed CANDIDATE-FORCED → R-2 completion; V4 full Q.3-side closed CANDIDATE-FORCED → R-3 Q.3-side closed), close V5 (downstream dependency map), dispatch VFal-9 (Q.3 ⟷ Q.7 circular dependency check), issue the Q.3 substage verdict, and produce the cascade map into Q.7 (R-1 + R-5 partial) and Q.8 (R-5 completion).
**Predecessors:** [`grh_evaluation.md`](grh_evaluation.md) (Q.1) · [`00_grh_closure_roadmap.md`](00_grh_closure_roadmap.md) · [`01_Q2_memo_00_outline.md`](01_Q2_memo_00_outline.md) · [`02_Q2_memo_01_non_abelian.md`](02_Q2_memo_01_non_abelian.md) · [`03_Q2_memo_02_gauge_quotient.md`](03_Q2_memo_02_gauge_quotient.md) · [`04_Q2_memo_03_verdict.md`](04_Q2_memo_03_verdict.md) · [`05_Q3_memo_00_outline.md`](05_Q3_memo_00_outline.md) · [`06_Q3_memo_01_vertex_minimal_coupling.md`](06_Q3_memo_01_vertex_minimal_coupling.md) · [`07_Q3_memo_02_vertex_quotient_commitment.md`](07_Q3_memo_02_vertex_quotient_commitment.md)
**Status:** Integration + verdict memo. Operates under the same forbidden-input discipline as Memos 00–02 (no R-1, R-5; no Q.7/Q.8 results; no SM specifics; no Higgs / generations / coupling constants; no F-M8 cascade target; no Yang-Mills / BRST as derivation premise). Inherits all structural commitments and falsifier dispatches from Memos 01–02.
**Purpose:** Issue the Q.3 substage verdict and prepare the GRH closure trajectory's advance to Q.7.

---

## 1. The Q.3 Question (Restated)

### 1.1 What Q.3 was tasked to determine

Q.3 was opened (per Memo 00) to discharge two refinements outstanding after Q.2's substage closure:

- **R-2 completion** (vertex-level gauge-quotient individuation): how does Primitive 10 vertex-individuation handle vertex events under gauge equivalence, given Q.2 Memo 02's kinematic-level gauge-quotient closure?
- **R-3** (vertex-anchored commitment for $\tau_g$): where are commitment events for the gauge rule-type $\tau_g$ sourced, given that $\tau_g$'s lightlike worldline carries no rest frame for worldline-intrinsic commitment events?

These two refinements are the vertex / interaction-level questions of the GRH closure trajectory. R-2 completion finishes the gauge-quotient individuation work begun by Q.2. R-3 establishes the vertex-anchored commitment specification for $\tau_g$ — partially at Q.3 (Q.3-side) and fully across Q.3 + Q.7 + Q.8 (full closure trajectory).

Q.3's full sub-feature decomposition (per Memo 00):

- **V1** Vertex taxonomy under GRH (forced-via-derivation)
- **V2** Minimal coupling as structural vertex (forced-via-derivation)
- **V3** Vertex-level gauge-quotient individuation (load-bearing; R-2 completion)
- **V4** Vertex-anchored commitment for $\tau_g$ (load-bearing; R-3 Q.3-side)
- **V5** Downstream dependency map (bookkeeping integration)

Memos 01 and 02 closed the four substantive sub-features (V1, V2, V3, V4 Q.3-side) at CANDIDATE-FORCED. Memo 03 integrates V1–V5, closes V5, audits the residual VFal-9 item, and issues the substage verdict.

### 1.2 Q.3's position in the GRH-closure trajectory

The GRH closure roadmap sequences the work as Q.2 → Q.3 → Q.7 → Q.8 → Arc Q synthesis → cascade to Arc M.

Q.3 is the vertex / interaction substage. It sets the structural boundary that Q.7 and Q.8 inherit:

- **Q.7** inherits Q.3's vertex content for the lightlike-worldline reformulation (R-1) and the vacuum-field aspect (R-5 partial).
- **Q.8** inherits Q.3's vertex-level gauge-quotient structure for the vacuum state (R-5 completion).

Q.3's verdict matters for the entire Q.7 + Q.8 trajectory.

### 1.3 Refinements Q.3 was responsible for

| Refinement | Description | Q.3 sub-feature | Closure scope |
|---|---|---|---|
| **R-2 completion** | Vertex-level gauge-quotient individuation | V3 | Full (R-2 fully closed at Q.3) |
| **R-3 Q.3-side** | Vertex-anchored commitment for $\tau_g$ | V4 | Q.3-side only (full R-3 closure trajectory continues to Q.7 + Q.8) |

Q.3 closes 2 of the 5 refinement items remaining after Q.2 (R-2 completion fully + R-3 Q.3-side). The remaining 3 (R-1, R-5 partial, R-5 completion) are Q.7 / Q.8 content.

---

## 2. Sub-Feature Integration (V1–V5)

### 2.1 V1 — Vertex Taxonomy Under GRH

**Status: CLOSED — CANDIDATE-FORCED (Memo 01).**

**Key structural findings (recap from Memo 01):**

- The vertex taxonomy under GRH consists of exactly four vertex types:
  - **T1** Emission ($\psi \to \psi + A_\mu$)
  - **T2** Absorption ($\psi + A_\mu \to \psi$)
  - **T3** 3-gauge self-coupling (non-Abelian only, $f^{abc}$ structure)
  - **T4** 4-gauge self-coupling (non-Abelian only, paired structure-constant contractions)
- Higher-order vertices (5-gauge and above) and non-minimal couplings (magnetic-moment, derivative couplings beyond minimal) are structurally excluded by primitive-level constraints.
- All four vertex types are Lorentz-invariant + gauge-invariant by construction.
- Per-primitive audit: P-04, P-06, P-07, P-11 actively support; P-02, P-10 neutral. **No primitive forbids.**
- Falsifier VFal-5 (taxonomy inconsistent) NOT triggered.

**Open items:** none from V1's own scope.

**Downstream dependencies:**
- Q.7 inherits the vertex taxonomy for second-quantisation amplitudes (Q.7 amplitudes built from these vertex types only).
- Q.8 inherits the vertex taxonomy for vacuum-state vertex content (vacuum interactions involve admissible vertex types only).

### 2.2 V2 — Minimal Coupling as Structural Vertex

**Status: CLOSED — CANDIDATE-FORCED (Memo 01).**

**Key structural findings (recap from Memo 01):**

- The minimal-coupling form $D_\mu = \partial_\mu + (ig/\hbar) A^a_\mu T^a$ is the unique lowest-order gauge-invariant Lorentz-covariant structural vertex content for charged-rule-type / $\tau_g$ interactions.
- Derivation: GRH-3 L3-interface gauge invariance + Primitive 06 Lorentz covariance + lowest-order constraint → minimal-coupling form is uniquely determined.
- F-GRH-D ("Minimal coupling as a structural interaction") promoted from CANDIDATE-conditional (Q.1) to **CANDIDATE-FORCED at the vertex level** at Memo 01.
- What's FORCED: operator structure, vertex content, uniqueness, non-Abelian extension. What's empirical: coupling constant value $g$, gauge group $G$, charged-rule-type representations $\rho$, value of $\hbar$ (per Dimensional Atlas).
- Falsifier VFal-6 (minimal coupling not unique) NOT triggered.

**Open items:** none from V2's own scope.

**Downstream dependencies:**
- Q.7 inherits the minimal-coupling vertex form for interaction-Hamiltonian content.
- Q.8 inherits the minimal-coupling vertex form for vacuum-state vertex content.

### 2.3 V3 — Vertex-Level Gauge-Quotient Individuation (R-2 Completion)

**Status: CLOSED — CANDIDATE-FORCED (Memo 02).**

**Key structural findings (recap from Memo 02):**

- Vertex-level individuation respects gauge equivalence automatically (vertex-level Q3-A) because Primitive 10 vertex-individuation consults gauge-invariant vertex observables.
- Five structural requirements (QV1 gauge-invariant vertex observables, QV2 vertex-density consistency, QV3 Wilson-loop / holonomy compatibility, QV4 quotient-respecting vertex counting — load-bearing, QV5 non-Abelian consistency) all primitive-level admissible.
- Per-primitive audit: all six primitives support; P-10 (vertex-level Q3-A automatic) and P-11 (vertex-density extension) load-bearing.
- Falsifier VFal-7 (vertex-counting fails gauge) NOT triggered.

**Open items:** none from V3's own scope.

**Downstream dependencies:**
- Q.8 inherits the vertex-level gauge-quotient structure for vacuum-state vertex events (vacuum polarisation, virtual vertex pairs must be gauge-quotient-respecting).

### 2.4 V4 — Vertex-Anchored Commitment for τ_g (R-3 Q.3-Side)

**Status: CLOSED Q.3-SIDE — CANDIDATE-FORCED (Memo 02; partial closure begun in Memo 01).**

**Key structural findings (recap from Memos 01 + 02):**

- $\tau_g$'s commitment events are sourced exclusively at V1 vertex types T1–T4.
- Each commitment event has the structural form of the minimal-coupling vertex content (V2).
- Commitment events are individuated by gauge-equivalence-class vertex configuration (V3).
- Per-worldline commitment-event rate is proportional to local vertex density (vertex-density-dependent rate, extending Primitive 11's specification).
- Primitive 11 admits the vertex-anchored commitment rule as a structural extension at Q.3 level.
- Falsifier VFal-8 (P-11 incompat with vertex commitment) NOT triggered at Q.3-side.

**Open items resolved at Q.3 level:**
- Vertex-mediated individuation closure (V3 supplies; integrated in Memo 02 §4).
- P-11 admissibility for vertex-density commitment-rate construction (verified in Memo 02 §5).

**Open items deferred:**
- Full Phase-1 reconciliation of per-vertex-density measure with Primitive 11's general specification — Q.7 (R-1 lightlike-worldline reformulation).
- Vacuum-state vertex events and vacuum-vs-particle status of $\tau_g$ — Q.8 (R-5 completion) + Q.7 (R-5 partial).

**Downstream dependencies:**
- Q.7 inherits the vertex-anchored commitment specification for the affine-parameter machinery and per-worldline accounting (R-1).
- Q.7 inherits the commitment structure for the vacuum-field aspect of $\tau_g$'s status (R-5 partial).
- Q.8 inherits for the zero-point aspect (R-5 completion).

### 2.5 V5 — Downstream Dependency Map

**Status: CLOSED — issued in §6 below.**

**Memo 03 closure.** V5 is bookkeeping: the precise inventory of what Q.7 and Q.8 inherit from Q.3's closure. The dependency map is built from V1–V4's outputs and is presented in §6 as the substantive cascade content.

**Open items:** none.

**Downstream dependencies:** V5 *is* the downstream-dependency specification; downstream substages depend on V5's content but V5 has no further dependencies of its own.

### 2.6 Residual Open Items: VFal-9 Dispatch + Q.3 ⟷ Q.7 Acyclicity Check

The remaining falsifier from Memos 00–02 requires explicit dispatch:

**VFal-9 — Q.3 ⟷ Q.7 circular dependency.** The falsifier asks whether Q.3's closure (especially V4 vertex-anchored commitment) requires Q.7's lightlike-worldline reformulation for its own definition, creating a circular dependency.

*Audit at Memo 03 level.* Q.3's V4 closure (Memo 02 §4-§5) commits to:
- Vertex-anchored commitment as structural extension of Primitive 11 (Memo 02 §5.1) — admissible at Q.3 level without invoking Q.7's affine-parameter machinery.
- Vertex-density-dependent commitment rate (Memo 02 §4.2 #4) — defined at Q.3 level using vertex density (vertex events per unit affine parameter), with the *value* of vertex density depending on the local vertex content (computable at Q.3) and the *parametrisation* (affine parameter machinery) being Q.7 content.

The Q.3-side commits to the *structure* of vertex-anchored commitment; Q.7 will supply the *parametrisation* (affine parameter) and the *full per-worldline accounting machinery*. These are complementary, not overlapping — Q.3's structural content is independent of Q.7's parametrisation choices.

Specifically:
- Q.3 commits: $\tau_g$'s commitment events are at vertex types T1–T4 with minimal-coupling form, individuated by gauge-equivalence class, with vertex-density-dependent rate.
- Q.7 will commit: the affine-parameter machinery for $\tau_g$'s lightlike worldline propagation between vertices; per-worldline accounting of vertex-anchored commitment events in the affine-parameter framework.

Q.3 → Q.7 is a clean one-way dependency: Q.7 inherits Q.3's vertex content and supplies the parametrisation. Q.7 does not feed back into Q.3 — the parametrisation choice does not affect the structural identification of vertex types, vertex factors, or vertex-mediated individuation.

**VFal-9 verdict: NOT triggered.** No Q.3 ⟷ Q.7 circular dependency identified.

The dispatch confirms V5's downstream dependency map (§6 below) is well-defined: Q.3 → Q.7 + Q.3 → Q.8 are clean one-way dependencies with no feedback loops.

---

## 3. Refinement-Closure Summary

| Refinement | Description | Closure stage | Q.3 closure status |
|---|---|---|---|
| **R-1** | Lightlike-worldline reformulation | Q.7 | (deferred) |
| **R-2 partial** | Gauge-quotient individuation, kinematic | Q.2 Memo 02 | **CLOSED — CANDIDATE-FORCED** ✅ |
| **R-2 completion** | Vertex-level gauge-quotient | Q.3 Memo 02 | **CLOSED — CANDIDATE-FORCED** ✅ |
| **R-2 (FULL)** | combined kinematic + vertex-level gauge-quotient | Q.2 Memo 02 + Q.3 Memo 02 | **R-2 FULLY CLOSED** ✅✅ |
| **R-3 Q.3-side** | Vertex-anchored commitment specification | Q.3 Memo 02 | **CLOSED — CANDIDATE-FORCED** ✅ |
| **R-3 Q.7/Q.8-side** | Lightlike-worldline + vacuum status reconciliation | Q.7 + Q.8 | (deferred) |
| **R-3 (FULL)** | combined Q.3 + Q.7/Q.8 sides | Q.3 Memo 02 + Q.7 + Q.8 | partial: Q.3-side closed, downstream pending |
| **R-4** | Non-Abelian extension scoping | Q.2 Memo 01 | **CLOSED — CANDIDATE-FORCED** ✅ |
| **R-5 partial** | Vacuum-field aspect of $\tau_g$ status | Q.7 | (deferred) |
| **R-5 completion** | Zero-point aspect | Q.8 | (deferred) |

**Q.3 closes two of the five refinement items remaining after Q.2 (R-2 completion + R-3 Q.3-side). Cumulative GRH refinement-closure progress: 4/7 items closed; 3/7 + R-3 Q.7/Q.8-side outstanding for Q.7 + Q.8.**

R-2 is now FULLY CLOSED in the GRH refinement-closure map (kinematic gauge-quotient + vertex-level gauge-quotient both done). R-3 is partially closed (Q.3-side done; Q.7/Q.8-side outstanding). R-4 closed at Q.2. The trajectory advances to Q.7.

---

## 4. Falsifier Status Table

### 4.1 Per-falsifier status across Memos 00–03

| Falsifier | Description | Memo tested | Status | Remaining downstream tests |
|---|---|---|---|---|
| **VFal-1** | Vertex-level primitive incompatibility (V1, V2, V3, V4) | Memo 01 §4 + Memo 02 §3 + §5 | **NOT triggered** | Q.7 vertex-level analog at second-quantisation level |
| **VFal-2** | Vertex L3-interface incompat. (V2, V3) | Memo 02 §3.4 | **NOT triggered** | Q.7 / Q.8 vertex-level checks |
| **VFal-3** | Vertex content breaks GRH-1/2/4 (V1, V2, V4) | Memo 01 §6 | **NOT triggered** | none |
| **VFal-4** | Cross-substage individ. failure (V3, V5) | Memo 02 §3 + §5 + Memo 03 §2.6 | **NOT triggered** | Q.7 / Q.8 cross-checks |
| **VFal-5** | Vertex-classification inconsistency (V1) | Memo 01 §6.1 | **NOT triggered** | none |
| **VFal-6** | Minimal coupling not unique (V2) | Memo 01 §6.2 | **NOT triggered** | none |
| **VFal-7** | Vertex-counting fails gauge (V3) | Memo 02 §6.1 | **NOT triggered** | Q.8 vacuum-state vertex-level analog |
| **VFal-8** | P-11 incompat with vertex commit. (V4) | Memo 02 §6.2 (Q.3-side dispatch); Memo 01 §6.3 (Q.3-side partial) | **NOT triggered (Q.3-side full)** | Q.7 full Phase-1 reconciliation |
| **VFal-9** | Q.3 ⟷ Q.7 circular dependency (V4, V5) | Memo 03 §2.6 | **NOT triggered** | none |

### 4.2 Cumulative Q.3 falsifier-status verdict

**All nine falsifiers (VFal-1 through VFal-9) NOT triggered for Q.3 substage.**

Q.3's structural admissibility for vertex taxonomy, minimal-coupling structural vertex form, vertex-level gauge-quotient individuation, and vertex-anchored commitment closes without falsifier obstruction.

The downstream tests noted (VFal-1 vertex-level analog at Q.7 second-quantisation level; VFal-2 Q.7/Q.8 checks; VFal-4 cross-checks; VFal-7 Q.8 vacuum-state analog; VFal-8 Q.7 full reconciliation) are *new* falsifier-tests at downstream scopes, not residual Q.3 falsifier-tests. Q.3's own falsifier inventory is fully discharged.

---

## 5. Q.3 Verdict

### 5.1 Verdict

**Q.3 substage: CLOSED — CANDIDATE-FORCED.**

Specifically: the Q.3 substage discharges its two assigned refinements (R-2 completion + R-3 Q.3-side) at CANDIDATE-FORCED, derives the vertex taxonomy (V1) and minimal-coupling structural vertex form (V2) at CANDIDATE-FORCED, establishes the vertex-anchored commitment specification for $\tau_g$ at Q.3-side (V4), and issues the downstream dependency map (V5). All nine Q.3 falsifiers are NOT triggered. The GRH closure trajectory advances to Q.7 (R-1 + R-5 partial).

### 5.2 Justification

The verdict rests on the integration of Memos 01 and 02:

- **V1 (Memo 01) closed CANDIDATE-FORCED.** Vertex taxonomy under GRH = exactly four vertex types (T1, T2, T3, T4); higher-order and non-minimal vertices structurally excluded; no primitive forbids; no falsifier triggered.
- **V2 (Memo 01) closed CANDIDATE-FORCED.** Minimal coupling derived as the unique lowest-order gauge-invariant Lorentz-covariant structural vertex content; F-GRH-D promoted from CANDIDATE-conditional to CANDIDATE-FORCED at vertex level.
- **V3 (Memo 02) closed CANDIDATE-FORCED.** Vertex-level individuation respects gauge equivalence automatically (vertex-level Q3-A) via gauge-invariant vertex observables; R-2 completion discharged.
- **V4 (Memo 02) closed CANDIDATE-FORCED at Q.3-side.** Vertex-anchored commitment specification for $\tau_g$ structurally complete at Q.3 level; R-3 Q.3-side discharged.
- **V5 closed via §6 below** — the dependency map for downstream substages.
- **VFal-9 dispatched** (Memo 03 §2.6) — no Q.3 ⟷ Q.7 circular dependency.
- **All nine falsifiers NOT triggered** (§4 above).

The CANDIDATE-FORCED designation reflects the same conditional-forcing structure that closed Memos 01 and 02: specific gauge-group choice + coupling values + charged-rule-type representations remain empirical inheritance per Arc M's "form FORCED, value INHERITED" methodology, and downstream substages (Q.7, Q.8) must close before GRH itself promotes to FORCED-unconditional.

### 5.3 Why CANDIDATE-FORCED rather than FORCED

Q.3's CANDIDATE-FORCED verdict carries forward the conditional-forcing aspects of Memos 01 and 02:

- **Specific gauge-group choice empirical** (per Q.2 F4 closure inherited).
- **Coupling constants empirical** (Dimensional Atlas).
- **Q.7 + Q.8 closures pending** for full R-3 closure (R-1 + R-5).
- **Cascade target F-M8 still conditional.**

Promoting Q.3 to FORCED unconditionally would require either (a) forcing the specific gauge-group choice from primitives (overstating per Memo 00 §9), or (b) downstream substages closing pre-emptively (inverting dependencies).

The CANDIDATE-FORCED verdict is the strongest defensible substage closure.

### 5.4 Why not weaker verdicts

- **CANDIDATE-admissible** would understate. All four substantive sub-features (V1, V2, V3, V4 Q.3-side) close at CANDIDATE-FORCED; the substage-level conditional-forcing characterisation is the strongest defensible.
- **SPECULATIVE-admissible** would imply substantial gaps. None remain at Q.3 level — VFal-9 dispatched in §2.6, V5 closed in §6.
- **REFUTED** would require a primitive-level obstruction. None identified across Memos 01–03.

---

## 6. Structural Cascade into Q.7 → Q.8

### 6.1 What Q.3 commits to downstream

The Q.3 substage commits to the following structural content, available for downstream substages to inherit as background (not as derivation premise):

**Vertex taxonomy (from V1):**
- Exactly four admissible vertex types: T1 (emission), T2 (absorption), T3 (3-gauge self-coupling, non-Abelian only), T4 (4-gauge self-coupling, non-Abelian only).
- Higher-order and non-minimal vertices structurally excluded.

**Minimal-coupling structural vertex form (from V2):**
- $D_\mu = \partial_\mu + (ig/\hbar) A^a_\mu T^a$ as the unique lowest-order gauge-invariant Lorentz-covariant vertex content.
- F-GRH-D promoted to CANDIDATE-FORCED at vertex level.

**Vertex-level gauge-quotient individuation (from V3):**
- Vertex-level individuation operates on gauge-equivalence-class vertex content $[V]$ (vertex-level Q3-A automatic).
- Gauge-invariant vertex observables: vertex factors (QV1), Wilson loops (QV3), Killing-contracted vertex content (QV5).
- Vertex-counting respects gauge equivalence (QV4).
- Non-Abelian consistency: Lie-algebra structure preserved at vertex level (QV5).

**Vertex-anchored commitment for $\tau_g$ (from V4 Q.3-side):**
- Commitment events sourced at V1 vertex types T1–T4.
- Vertex-density-dependent commitment rate (extending Primitive 11).
- Gauge-equivalence-class counting (per V3).
- Primitive 11 admits the structural extension at Q.3 level.

**Honest scoping (carried forward from Q.2):**
- Specific gauge-group choice empirical inheritance.
- Coupling constant values empirical via Dimensional Atlas.
- Charged-rule-type representations empirical / Q.4-onward.

### 6.2 What Q.3 does NOT commit to

- **Specific gauge group** (U(1) vs SU(2) vs SU(3) vs combinations).
- **Coupling constant values** ($q$, $g_s$, $g_w$).
- **Charged-rule-type representations** (which fermions transform under which $G$ representations).
- **Lightlike-worldline parametrisation** (R-1 — Q.7 work).
- **Vacuum-vs-particle status of $\tau_g$** (R-5 — Q.7 / Q.8 work).
- **Per-worldline accounting machinery** in affine-parameter framework (Q.7).
- **Vacuum-state vertex content** (Q.8).
- **Higgs / SSB sector** (Q.4, SPECULATIVE).
- **Generation structure** (Q.6 / empirical).
- **Charge quantization pattern** (possibly Q.2/Q.3 partial sub-memo or empirical).
- **Standard QFT scattering amplitudes / cross-sections** (Q.7 second-quantisation).

### 6.3 Dependency map: how Q.3 constrains Q.7 and Q.8

| Downstream substage | Q.3 sub-feature inheritance | Q.7 / Q.8 deliverable |
|---|---|---|
| **Q.7 R-1** (lightlike-worldline reformulation) | V4 vertex-anchored commitment specification; V1 vertex taxonomy | Affine-parameter machinery for $\tau_g$; per-worldline accounting integrating vertex-density commitment rate with Primitive 11's general specification |
| **Q.7 R-5 partial** (vacuum-field aspect) | V2 minimal-coupling vertex; V3 vertex-level gauge-quotient | Background-field interpretation of $\tau_g$; vacuum-state vertex events at admissible vertex types; vacuum-state vertex observables gauge-invariant |
| **Q.7 second-quantisation framework** | V1 vertex taxonomy; V2 minimal coupling; V3 gauge-quotient; V4 vertex-anchored commitment | Creation/annihilation operator structure for $\tau_g$; propagators between vertex events; scattering amplitudes built from admissible vertex content |
| **Q.8 R-5 completion** (zero-point aspect) | V3 vertex-level gauge-quotient; V4 vertex-anchored commitment | Zero-point fluctuations as primitive-level vacuum content; vacuum-vertex content gauge-quotient-respecting; reconciliation with Λ-from-V₁ derivation (Phase-3 background) |

Q.3 → Q.7 + Q.3 → Q.8 are clean one-way dependencies (per VFal-9 dispatch in §2.6).

### 6.4 Minimal deliverables Q.7 must produce to close R-1 and R-5 partial

For **R-1 closure**:
- Affine-parameter machinery for $\tau_g$'s lightlike worldline (replacing the proper-time parametrisation that fails for lightlike worldlines).
- Per-worldline commitment-rate accounting in the affine-parameter framework, integrating Q.3's vertex-density commitment rate.
- Full Phase-1 reconciliation: demonstrate that the per-vertex-density measure on the lightlike worldline is structurally consistent with Primitive 11's general commitment-events specification (closing the Q.3-side / Q.7-side reconciliation noted at Memo 02 §5).

For **R-5 partial closure**:
- Vacuum-field interpretation of $\tau_g$ (background field configuration).
- Reconciliation with the second-quantisation framework: $\tau_g$ as both a vacuum-occupying field and as a particle-like rule-type (creation/annihilation of $\tau_g$ quanta).
- Vacuum-state vertex events at admissible vertex types (V1-T1 through V1-T4) with gauge-quotient-respecting individuation (V3 inherited).

For full **R-3 closure** (Q.7-side):
- Integration of R-1 closure with Q.3's V4 specification, completing the per-worldline accounting of vertex-anchored commitment events.
- Verification that Primitive 11's general specification is fully reconciled with the lightlike-worldline + vertex-anchored commitment framework.

---

## 7. Implications for GRH Closure

### 7.1 Effect on GRH-3 (the load-bearing GRH clause)

GRH-3 asserts that $\tau_g$'s L3 interface enforces local gauge invariance. Q.3's closure advances GRH-3's status:

- **Pre-Q.3:** CANDIDATE-FORCED at gauge-group-scoping level (Q.2 closure).
- **Post-Q.3:** **CANDIDATE-FORCED at vertex level.** The L3-interface gauge-invariance constraint is now structurally established at both the kinematic (Q.2 Memo 02) and vertex (Q.3 Memo 02) levels; minimal coupling is the structural vertex form (V2); vertex-anchored commitment for $\tau_g$ is structurally complete at Q.3 level (V4).

GRH-3 still awaits:
- Q.7 closure (R-1 lightlike-worldline + R-5 partial vacuum-field) for the second-quantisation framework.
- Q.8 closure (R-5 completion) for the vacuum-state structure.

When both downstream substages close, GRH-3 promotes to FORCED-unconditional, and GRH itself (with GRH-1, GRH-2, GRH-4 already CANDIDATE-FORCED conditional on GRH-3) promotes to FORCED-unconditional.

### 7.2 Updated GRH refinement-closure map

| Refinement | Pre-Q.3 status | Post-Q.3 status | Closure stage |
|---|---|---|---|
| **R-1** | outstanding | outstanding | Q.7 |
| **R-2 partial** | CLOSED (Q.2 Memo 02) | (unchanged) | Q.2 Memo 02 |
| **R-2 completion** | outstanding | **CLOSED ✅** | **Q.3 Memo 02** |
| **R-2 (FULL)** | partial | **FULLY CLOSED ✅✅** | Q.2 + Q.3 |
| **R-3 Q.3-side** | partial closure (Memo 01) | **CLOSED ✅** | **Q.3 Memo 02** |
| **R-3 (FULL)** | outstanding | partial: Q.3-side closed; Q.7+Q.8-side outstanding | Q.3 + Q.7 + Q.8 |
| **R-4** | CLOSED (Q.2 Memo 01) | (unchanged) | Q.2 Memo 01 |
| **R-5 partial** | outstanding | outstanding | Q.7 |
| **R-5 completion** | outstanding | outstanding | Q.8 |

**Cumulative closure: 4/7 refinement items closed (R-2 partial + R-2 completion + R-3 Q.3-side + R-4); 3/7 + R-3 Q.7/Q.8-side outstanding.** R-2 is now FULLY CLOSED in the inventory; R-3 has one closed side (Q.3) and one outstanding side (Q.7+Q.8).

### 7.3 Remaining structural work before GRH promotes to FORCED at Arc Q synthesis

The path from "Q.3 closed" to "GRH FORCED-unconditional" requires:

1. **Q.7 substage closure** (second quantisation + R-1 + R-5 partial). Anticipated 4–5 memos (substantively heavier than Q.2 / Q.3 because of the full second-quantisation framework). Key deliverables: affine-parameter machinery for $\tau_g$; per-worldline accounting integrating Q.3's vertex-density commitment rate; vacuum-field interpretation of $\tau_g$; reconciliation of Phase-1 commitment-dynamics specification with the lightlike-worldline + vertex-anchored framework.
2. **Q.8 substage closure** (vacuum and zero-point + R-5 completion). Anticipated 3–4 memos. Key deliverables: zero-point fluctuations as primitive-level vacuum content; full vacuum-state structure; reconciliation with Λ-from-V₁ derivation (Phase-3 background).
3. **Arc Q synthesis** (integration of Q.2, Q.3, Q.7, Q.8 results; verification all five refinements affirmatively closed; verification zero new CANDIDATEs introduced; statement of FORCED GRH theorem). Anticipated 1–2 memos.
4. **Cascade promotion of Arc M's F-M8** (massless slot existence from FORCED-conditional to FORCED-unconditional). Memo back into Arc M.

Total anticipated remaining Q-substage memos: 8–11. Plus Arc M cascade memo. The trajectory is concrete and well-scoped; no structural blocker has been identified.

### 7.4 Position relative to the 16-theorem inventory

When GRH promotes to FORCED-unconditional, it becomes Theorem 17 in the structural-foundations inventory:

> **Theorem 17 (GRH — Gauge-Field-as-Rule-Type, anticipated).** The gauge connection $A_\mu$ is itself the participation measure of a rule-type $\tau_g$ (bosonic, four-vector, gauge-invariant L3 interface, structurally massless via MR-P), with the gauge group $G$ admissible as any compact Lie group (specific choice empirical inheritance). Local gauge invariance is an interface property of $\tau_g$'s L3 specification, not an externally-imposed symmetry principle. Vertex content: four admissible vertex types (T1–T4); minimal coupling as structural vertex; vertex-level gauge-quotient individuation respecting equivalence classes; vertex-anchored commitment for $\tau_g$ via vertex-density-dependent rates.

Cascade: Arc M's F-M8 (massless slot existence) promotes to FORCED-unconditional.

---

## 8. Honest Scope Limits

Per the discipline established across Memos 00–03, Q.3 explicitly cannot resolve:

### 8.1 Within-trajectory items (deferred to Q.7 / Q.8)

- **R-1 (lightlike-worldline reformulation).** Q.7. Q.3 commits to vertex-anchored commitment as structural alternative; affine-parameter machinery is Q.7.
- **R-5 partial (vacuum-field aspect of $\tau_g$).** Q.7. Q.3 commits to vertex content; vacuum-field interpretation is Q.7.
- **R-5 completion (zero-point aspect).** Q.8. Vacuum-state vertex content + zero-point fluctuations is Q.8.
- **R-3 full closure** (integration of Q.3-side with Q.7 + Q.8-side) — Q.7 + Q.8 work.

### 8.2 Outside-trajectory items (empirical inheritance or out of GRH scope)

- **Specific gauge group choice** ($SU(3) \times SU(2) \times U(1)$ or any other). Empirical inheritance per Q.2 F4.
- **Coupling constant values** ($q$, $g_s$, $g_w$). Empirical inheritance via Dimensional Atlas.
- **Charged-rule-type representations.** Empirical / Q.4-onward.
- **Higgs sector / SSB.** Q.4; SPECULATIVE.
- **Generation structure.** Q.6 / empirical.
- **Charge quantization pattern.** Possibly Q.2 / Q.3 partial sub-memo or empirical.
- **Standard QFT amplitude content.** Q.7 second-quantisation work.
- **Vacuum polarisation contributions.** Q.8 work.
- **Anomalous magnetic moment of the electron.** Standard QED loop-correction content; ED's analog Q.7 work.

### 8.3 Sensitivity flags carried forward

- **Phase-observable discipline** (from Q.2 Memo 03 §2.6). Confirmed at Q.2 closure; lifts cleanly to vertex level via Memo 02 §3.5.
- **Compactness of $G$** (from Q.2 Memo 01 §3.4.2). Derived constraint from unitarity (U2 inheritance); preserved at Q.3 vertex level.
- **Killing-form non-degeneracy** (from Q.2 Memo 03 §2.6). Verified for compact semi-simple groups; preserved at Q.3 vertex level via QV5 non-Abelian consistency.
- **Vertex-density commitment-rate construction** (Q.3 Memo 01 §5.3.2 + Memo 02 §3.6). Q.3-side admissibility established; full Phase-1 reconciliation deferred to Q.7's lightlike-worldline reformulation.

---

## 9. Recommended Next Memo

**Q.7 Memo 00 — Lightlike-Worldline Reformulation + Second Quantisation + R-1 + R-5 Partial**

The natural next deliverable. Q.7 Memo 00 should:

- Restate the Q.7 question: how does the lightlike-worldline structure for $\tau_g$ propagation between vertices integrate with the second-quantisation framework, and what does the vacuum-field aspect of $\tau_g$'s status look like?
- Decompose Q.7 into sub-features (likely: lightlike-worldline reformulation — affine parameter, per-worldline accounting, integration with vertex-anchored commitment from Q.3; second-quantisation framework — creation/annihilation operators, propagators, amplitudes; vacuum-field interpretation of $\tau_g$ — background-field aspect of R-5; downstream dependency map for Q.8).
- Inventory structural inputs (Primitives 02, 04, 06, 07, 10, 11; inherited theorems including Theorems 1–16; Q.2 + Q.3 closures as background; M.1.2 commitment-event framework as background).
- Set forbidden-input discipline (no R-5 completion — Q.8 work; no SM specifics; no Higgs / generations / coupling constants; no F-M8 cascade target; no full QFT amplitude machinery as derivation premise).
- Falsifier inventory for what would refute GRH at the lightlike-worldline + second-quantisation level.

Anticipated length: comparable to Q.2 / Q.3 Memo 00. Q.7's *substantive* memos (01, 02, 03, possibly 04) will be heavier than Q.2/Q.3 memos due to the full second-quantisation framework. Total Q.7 substage anticipated: 4–5 memos.

The subsequent Q.7 memos would address sub-feature derivations parallel to the Q.2 / Q.3 patterns.

---

## 10. One-Line Summary

> Q.3 substage closes **CANDIDATE-FORCED** at Memo 03: the GRH framework structurally admits exactly four vertex types (V1: T1 emission, T2 absorption, T3 3-gauge non-Abelian-only, T4 4-gauge non-Abelian-only) with higher-order and non-minimal vertices structurally excluded, the minimal-coupling form $D_\mu = \partial_\mu + (ig/\hbar) A^a_\mu T^a$ is the unique structural vertex content (V2: F-GRH-D CANDIDATE-FORCED at vertex level), Primitive 10 vertex-individuation respects gauge equivalence automatically via gauge-invariant vertex observables (V3: vertex-level Q3-A — R-2 completion CLOSED, making R-2 FULLY CLOSED in the inventory), $\tau_g$'s commitment events are vertex-anchored at vertex types T1-T4 with vertex-density-dependent commitment rates extending Primitive 11 (V4: R-3 Q.3-side CLOSED), the downstream dependency map (V5) is issued, all nine Q.3 falsifiers (VFal-1 through VFal-9) NOT triggered, four of seven GRH refinements now closed (R-4 + R-2 partial + R-2 completion + R-3 Q.3-side), three full refinements + R-3 Q.7/Q.8-side remaining for Q.7 (R-1 lightlike-worldline + R-5 partial vacuum-field) and Q.8 (R-5 completion zero-point), GRH-3 advancing from CANDIDATE-FORCED at gauge-group-scoping level to CANDIDATE-FORCED at vertex level, GRH itself awaiting Q.7 + Q.8 closures before promotion to FORCED-unconditional and addition as Theorem 17 to the structural-foundations inventory with cascade promotion of Arc M's F-M8 to FORCED-unconditional.

---

## Recommended Next Steps

**(a) Begin Q.7 Memo 00 (lightlike-worldline reformulation + second quantisation + R-1 + R-5 partial).** The natural next deliverable. Following the Q.2 / Q.3 Memo 00 template, Q.7 Memo 00 should decompose Q.7 into sub-features (lightlike-worldline reformulation; second-quantisation framework; vacuum-field aspect; downstream dependency map for Q.8), inventory structural inputs (with strict forbidden-input discipline), and prepare the substage opening. Anticipated length: comparable to Q.2 / Q.3 Memo 00. Q.7's substantive memos will be heavier — this is the first Q-substage with a *full second-quantisation framework* requirement.

**(b) Bundled memory-record update covering Q.3 closure.** Per the discipline established in U3 / U4 / U5 arcs and the GRH closure roadmap §10. The memory update should capture: R-2 completion closure (CANDIDATE-FORCED at Q.3 Memo 02; R-2 FULLY CLOSED in inventory); R-3 Q.3-side closure (CANDIDATE-FORCED at Q.3 Memo 02; full R-3 trajectory continues Q.7 + Q.8); Q.3 substage verdict (CLOSED CANDIDATE-FORCED); cumulative refinement-closure status (4/7 closed); GRH-3 status update (CANDIDATE-FORCED at vertex level); anticipated remaining trajectory (Q.7 → Q.8 → synthesis → cascade); sensitivity flags carried forward (phase-observable discipline, compactness of $G$, Killing-form non-degeneracy, vertex-density commitment-rate construction).

**(c) Update the Sixteen-Theorems desktop graphic if appropriate.** Theorem 5's GRH entry can now be honestly updated to reflect 4 of 5 refinements closed (R-4 + R-2 + R-3 Q.3-side; R-1 + R-5 + R-3 Q.7/Q.8-side outstanding). The graphic could either: (i) keep the CANDIDATE-strong framing with a "4/5 refinements closed at Q.2 + Q.3; R-1 + R-5 + R-3 Q.7/Q.8-side remaining" annotation, or (ii) defer the update until full GRH closure (anticipated several memos out). User preference.

**(d) Defer further substantive memo work until Q.7 Memo 00 is opened.** Per the discipline of one substage at a time, no Q.8 work should begin before Q.7 closes. The trajectory is well-scoped and the dependencies are clean.

**(e) (Optional) Sketch the Q.7 substage's full memo trajectory now.** With Q.2 + Q.3 demonstrating the four-memo pattern (Memo 00 outline + Memos 01–02 substantive derivations + Memo 03 verdict), Q.7's anticipated structure can be pre-drafted in skeleton form. Q.7 may need an extra memo (Memo 04) due to the substantive load of the second-quantisation framework. Pre-sketching would let Q.7 work proceed efficiently when opened. Optional but useful for trajectory planning.
