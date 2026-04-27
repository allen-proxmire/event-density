# Q.3 Memo 02 — V3 + V4 (Completion): Vertex-Level Gauge-Quotient + Vertex-Anchored Commitment (R-2 Completion + R-3 Q.3-Side Closure)

**Stage:** Arc Q · Q.3 · Memo 02 (load-bearing V3 + V4 final-Q.3-side derivation)
**Date:** 2026-04-26
**Location:** `arcs/arc-Q/`
**Goal:** Discharge **R-2 completion** (vertex-level gauge-quotient individuation) by deriving V3, and complete **R-3 Q.3-side closure** by integrating V3 with V4 (vertex-anchored commitment for $\tau_g$). Establish that Primitive 10 vertex-individuation respects gauge equivalence by consulting gauge-invariant vertex observables (Wilson loops, gauge-invariant vertex factors), and that the vertex-anchored commitment specification for $\tau_g$ is structurally complete at the Q.3 level pending Q.7's lightlike-worldline reformulation (R-1) and Q.8's vacuum-state machinery (R-5).
**Predecessors:** [`grh_evaluation.md`](grh_evaluation.md) (Q.1) · [`00_grh_closure_roadmap.md`](00_grh_closure_roadmap.md) · [`01_Q2_memo_00_outline.md`](01_Q2_memo_00_outline.md) · [`02_Q2_memo_01_non_abelian.md`](02_Q2_memo_01_non_abelian.md) · [`03_Q2_memo_02_gauge_quotient.md`](03_Q2_memo_02_gauge_quotient.md) · [`04_Q2_memo_03_verdict.md`](04_Q2_memo_03_verdict.md) (Q.2 substage CLOSED CANDIDATE-FORCED) · [`05_Q3_memo_00_outline.md`](05_Q3_memo_00_outline.md) (Q.3 Memo 00) · [`06_Q3_memo_01_vertex_minimal_coupling.md`](06_Q3_memo_01_vertex_minimal_coupling.md) (V1 + V2 closed CANDIDATE-FORCED; V4 partial CANDIDATE-FORCED Q.3-side; R-3 advanced to PARTIAL CLOSURE)
**Status:** Technical derivation memo. Operates under strict forbidden-input discipline (per Q.3 Memo 00 §5): no R-1, no R-5, no Q.7 / Q.8 results, no SM specifics, no Higgs / generations / coupling constants, no F-M8 cascade target, no Yang-Mills or BRST as derivation premise. Inherits Q.2's CLOSED CANDIDATE-FORCED commitments + Q.3 Memo 01's V1/V2/V4-partial closures as background.
**Purpose:** State and discharge V3 (R-2 completion) and V4 (R-3 Q.3-side closure) so Memo 03 can issue the Q.3 substage verdict and downstream cascade map.

---

## 1. The V3 and V4 Questions Restated

### 1.1 V3 question

**What does it mean for gauge equivalence to be respected at the vertex level?**

More formally: given Q.2 Memo 02's closure (kinematic gauge-quotient individuation via Q3-A automatic, with Primitive 10 respecting gauge equivalence on the configuration space $\mathcal{A} / \mathcal{G}$), and given Q.3 Memo 01's vertex taxonomy V1 (four vertex types T1–T4) and minimal-coupling vertex form V2, how does Primitive 10 individuation handle vertex events under gauge equivalence?

The answer must specify:
- Which vertex observables count as physical content (gauge-invariant vertex factors, Wilson loops, gauge-invariant vertex amplitudes).
- How vertex-counting respects gauge equivalence — i.e., gauge-equivalent vertex configurations count as ONE commitment event, not many.
- Whether Primitive 10 respects vertex-level gauge equivalence automatically (vertex-level analog of Q3-A) or via explicit construction (vertex-level analog of Q3-B).
- How the vertex-level structure interfaces with the kinematic gauge-quotient already established at Q.2 Memo 02.

V3 closes R-2 completion — the second half of R-2 begun by Q.2 Memo 02.

### 1.2 V4 question

**What does it mean for τ_g to be vertex-anchored once vertex structure is fully specified?**

V4 partial closure at Q.3 Memo 01 established:
- Commitment events for $\tau_g$ are sourced at V1 vertex types T1–T4.
- Vertex-density-dependent commitment rates extend Primitive 11's specification.
- Vertex-mediated individuation pending V3 closure.

V4 final closure at Memo 02 must integrate V3's vertex-level gauge-quotient with the V4 partial specification, producing a complete vertex-anchored commitment rule for $\tau_g$ at the Q.3 level. The remaining Q.7-side content (lightlike-worldline reformulation R-1, vacuum-vs-particle status R-5) is honestly scoped as outside Q.3.

### 1.3 How V3 and V4 complete R-2 and R-3 at the Q.3 level

| Refinement | Q.2 closure | Q.3 closure | Beyond Q.3 |
|---|---|---|---|
| **R-2** | partial: kinematic gauge-quotient (Memo 02 of Q.2) | **completion: vertex-level gauge-quotient (V3, this Memo)** | none — R-2 fully closed at Q.3 |
| **R-3** | n/a | **Q.3-side: vertex-anchored commitment specification (V4 full at Q.3 level, this Memo)** | Q.7 (R-1 lightlike-worldline reformulation), Q.8 (R-5 vacuum status) for full R-3 closure |

R-2 closes fully at Q.3 Memo 02. R-3 closes at Q.3-side at Q.3 Memo 02; full R-3 closure trajectory continues through Q.7 and Q.8.

### 1.4 Outcome criteria

For V3:
- **CANDIDATE-FORCED:** vertex-level individuation respects gauge equivalence automatically (vertex-level analog of Q3-A), via gauge-invariant vertex observables. Anticipated default.
- **CANDIDATE-admissible:** vertex-level individuation admissible but requires explicit vertex-level quotient construction (vertex-level analog of Q3-B).
- **REFUTED:** vertex-level individuation incompatible with gauge equivalence — would force restriction of GRH content.

For V4:
- **CANDIDATE-FORCED at Q.3-side:** vertex-anchored commitment specification structurally complete at the Q.3 level; full R-3 closure pending Q.7 + Q.8.
- **CANDIDATE-admissible at Q.3-side:** specification admissible but with structural gaps requiring downstream work.
- **REFUTED:** vertex-anchored commitment cannot be specified consistently with Primitive 11 — would force restriction of GRH content to massive gauge rule-types, conflicting with GRH-4.

---

## 2. Structural Requirements for V3 (Vertex-Level Quotient)

For V3 to close affirmatively, the framework must structurally support five distinct requirements. Each is stated with primitive dependencies, inherited theorems, and bounded by what it does *not* commit to.

### 2.1 (QV1) Gauge-invariant vertex observables

- **Statement.** The framework admits gauge-invariant vertex observables — quantities computed from vertex configurations that take equal values on gauge-equivalent vertex configurations. For Abelian gauge groups, gauge-invariant vertex observables include the vertex factor $-iq/\hbar \cdot \gamma^\mu$ contracted with gauge-invariant fermion currents. For non-Abelian gauge groups, vertex observables include traces of products of $T^a$ generators contracted with gauge-invariant external states.
- **Commits to:** physical vertex content lives in gauge-equivalence-class vertex observables, not in raw vertex-configuration content.
- **Does NOT commit to:** any specific gauge-fixing prescription; the choice of gauge-fix is description-level convenience. Does not commit to the Lagrangian-level structure that generates the vertex factor.
- **Primitive dependencies:** Primitive 06 (Lorentz-covariant vertex factors); Primitive 07 (L3 interface specifies gauge-invariant content); Primitive 04 (bandwidth content at vertex must be gauge-invariant for physical observables).
- **Inherited FORCED items:** Theorem 14 (U1, $P_K = \sqrt{b_K} \cdot e^{i\pi_K}$) — vertex events involve participation-measure components; gauge-invariant phase content is required (per Q.2 Memo 02's phase-observable discipline).
- **Status from Q.2 inheritance:** Q.2 Memo 02 §5 established the gauge-quotient structure at the kinematic level; QV1 lifts this to the vertex level.

### 2.2 (QV2) Vertex-density consistency

- **Statement.** The vertex-density commitment-rate construction (§5.3.2 of Q.3 Memo 01) is consistent with Primitive 11's general specification: the rate of $\tau_g$ commitment events along $\tau_g$'s lightlike trajectory is proportional to the local vertex density (number of interaction vertices per unit affine parameter), with the proportionality constant inheriting from the minimal-coupling vertex factor.
- **Commits to:** $\tau_g$'s commitment rate is *vertex-density-dependent* — a structural extension of Primitive 11's specification to the gauge-rule-type case.
- **Does NOT commit to:** the affine-parameter machinery itself (Q.7 content); the specific vertex density values (depend on local interaction content, empirical inheritance).
- **Primitive dependencies:** Primitive 11 (commitment dynamics); Primitive 02 (worldline structure for vertex-density measurement).
- **Inherited FORCED items:** Theorem 16 (U3, Schrödinger evolution) — vertex events fit into the time-evolution framework that Theorem 16 establishes.

### 2.3 (QV3) Wilson-loop / holonomy compatibility

- **Statement.** The framework admits Wilson-loop observables — gauge-invariant traces of path-ordered exponentials $W[\gamma] = \mathrm{Tr}\, \mathcal{P} \exp\left(ig \oint_\gamma A^a_\mu T^a \, dx^\mu\right)$ around closed loops $\gamma$ — as gauge-invariant vertex content. Wilson loops are Lorentz-invariant and gauge-invariant by construction; they capture the gauge-invariant content of $A_\mu$ along the loop, integrating over the path-ordered exponential.
- **Commits to:** Wilson loops are admissible gauge-invariant vertex observables; the holonomy structure (the path-ordered exponential's content) carries the gauge-invariant phase information for $\tau_g$ along closed trajectories.
- **Does NOT commit to:** specific Wilson-loop values (depend on the gauge-field configuration); the role of Wilson loops in second-quantisation amplitudes (Q.7 content).
- **Primitive dependencies:** Primitive 02 (manifold structure for closed loops); Primitive 06 (smooth integration along loops); Primitive 07 (L3 interface admits gauge-invariant traces).
- **Inherited FORCED items:** Q.2 Memo 02's gauge-quotient structure (Wilson loops are the natural construction supplying gauge-invariant content for the vertex level).

### 2.4 (QV4) Quotient-respecting vertex counting

- **Statement.** Vertex-counting under Primitive 10 individuation respects gauge equivalence — i.e., gauge-equivalent vertex configurations count as ONE commitment event, not many. Specifically: if vertex configurations $V$ and $V'$ are related by a gauge transformation $V' = U V U^{-1}$ (with $U$ acting on the gauge-rule-type and charged-rule-type content at the vertex), then $V$ and $V'$ count as one vertex event under Primitive 10's individuation threshold.
- **Commits to:** vertex individuation operates on gauge-equivalence-class vertex content $[V]$, not on raw vertex configurations $V$.
- **Does NOT commit to:** how vertex-equivalence-class objects are constructed in detail (this is the structural question addressed by V3's primitive-level audit in §3); the specific choice of representative for any equivalence class.
- **Primitive dependencies:** Primitive 10 (individuation threshold at the vertex level); Primitive 04 (bandwidth content per vertex must be gauge-invariant); Primitive 07 (L3 interface).
- **Inherited FORCED items:** Q.2 Memo 02's Q3-A automatic individuation (kinematic level); QV4 lifts this to the vertex level.

### 2.5 (QV5) Non-Abelian consistency conditions

- **Statement.** For non-Abelian gauge groups, the vertex-level gauge-quotient must respect the Lie-algebra structure: the structure constants $f^{abc}$ satisfy the Jacobi identity ($f^{abe} f^{cde} + f^{ace} f^{dbe} + f^{ade} f^{bce} = 0$); the closure of the Lie algebra under commutation $[T^a, T^b] = i f^{abc} T^c$ is preserved at the vertex level; the gauge-invariant Killing-form contractions (per Q.2 Memo 02 §3.2) supply the vertex-level physical content.
- **Commits to:** non-Abelian vertex content respects the full Lie-algebra structure (closure, Jacobi, Killing form).
- **Does NOT commit to:** specific Lie group choice; specific structure constant values (these depend on $G$, empirical).
- **Primitive dependencies:** Primitive 07 (L3 interface admits Lie-algebra-multiplicity content at vertices); Primitive 06 (Lorentz covariance compatible with the Lie-algebra index structure).
- **Inherited FORCED items:** Memo 01 (Q.2 Memo 01) — non-Abelian admissibility (R-4 closure); the Lie-algebra structure inherits.

### 2.6 Joint admissibility for V3

For V3 to close affirmatively, all five requirements (QV1–QV5) must be primitive-level admissible. QV1 + QV3 are inherited from Q.2 Memo 02's gauge-quotient structure lifted to the vertex level. QV2 is the vertex-density extension noted in Q.3 Memo 01 §5.3.2 (verified in §3 below). QV4 is the load-bearing requirement — vertex counting respecting gauge equivalence. QV5 is the non-Abelian consistency check.

---

## 3. Primitive-Level Audit for V3

Each primitive is tested against QV1–QV5. Classifications: **supports**, **neutral**, **constrains**, **forbids**.

### 3.1 Primitive 02 — worldline + ambient 3+1D manifold

- **Test (QV1).** Does the manifold admit gauge-invariant vertex observables computed from vertex configurations on it?
- **Analysis.** Vertices are point-like events on the manifold; gauge-invariant vertex factors are tensors at the vertex point, computed from charged-rule-type and gauge-rule-type content at that point. The manifold structure admits this trivially.
- **Test (QV3).** Does the manifold admit closed loops for Wilson-loop construction?
- **Analysis.** Smooth manifolds admit closed loops; Wilson loops as path-ordered exponentials of $A^a_\mu$ integrated over closed paths are standard differential-geometric objects.
- **Tension.** None at Q.3 level. The lightlike-worldline structure for $\tau_g$'s propagation between vertices is Q.7 content.
- **Falsifiers triggered.** None.
- **Classification:** **supports** (admits gauge-invariant vertex observables and Wilson loops as differential-geometric objects).

### 3.2 Primitive 04 — bandwidth fields

- **Test (QV1, QV4).** Does the four-band bandwidth content at vertex events descend to gauge-invariant physical content?
- **Analysis.** Per Q.2 Memo 02 §3.2, gauge-invariant bandwidth observables are Killing-form-contracted: $b^X = -g^{ab} b^X_a b^X_b$ for $X \in \{\mathrm{int}, \mathrm{adj}, \mathrm{env}, \mathrm{com}\}$. At vertex events, bandwidth content is exchanged between rule-types; the exchanged bandwidth is gauge-invariant when computed in the Killing-contracted form. Gauge-equivalent vertex configurations exchange the same Killing-contracted bandwidth content.
- **Test (QV5).** Does the bandwidth structure respect non-Abelian Lie-algebra content at vertex events?
- **Analysis.** Yes — the Lie-algebra multiplicity in $b^X_a$ generalises Primitive 04 §1.5's four-band orthogonality cleanly (per Q.2 Memo 03 §2.6 verification).
- **Tension.** None.
- **Falsifiers triggered.** None.
- **Classification:** **supports**.

### 3.3 Primitive 06 — four-gradient + Lorentz covariance

- **Test (QV1, QV3, QV5).** Does Lorentz covariance admit gauge-invariant vertex factors and Wilson loops?
- **Analysis.** Vertex factors $-ig/\hbar \cdot \gamma^\mu T^a$ are Lorentz-covariant tensors with internal index $a$; gauge-invariant combinations (traced or contracted with gauge-invariant external states) are Lorentz-scalars or Lorentz-tensors as appropriate. Wilson loops are Lorentz-invariant (the closed-path integral is parametrisation-independent and Lorentz-invariant for closed loops).
- **Tension.** None.
- **Falsifiers triggered.** None.
- **Classification:** **supports**.

### 3.4 Primitive 07 — rule-type taxonomy (L3 load-bearing)

- **L1 (bandwidth partition).** Vertex events shift bandwidth between rule-types; partition adjusts at vertices but the structural content of L1 (a partition exists per rule-type) is unchanged. **Supports.**
- **L2 (internal index).** Vertex factors involve internal-index content; gauge-quotient on the index space (adjoint action for non-Abelian gauge transformation) admits Killing-contracted gauge-invariant observables. **Supports.**
- **L3 (interface).** **The load-bearing lever.** L3 specifies gauge-invariance constraint at the vertex level (per Q.2 Memo 02 §4). The vertex-level lifting of L3-Q-1, L3-Q-2, L3-Q-3 conditions (per Q.2 Memo 02 §4):
  - **L3-Q-V1.** Vertex-level L3 content depends only on $[V]$ (gauge-equivalence class), not on representative $V$ — verified for QV1 gauge-invariant observables and QV3 Wilson loops.
  - **L3-Q-V2.** Vertex-level L3 content commutes with gauge transformations — verified for vertex factors and minimal-coupling structure (per Memo 01 §4).
  - **L3-Q-V3.** Vertex-level L3 content admits the vertex-equivalence-class projection — verified for QV4 quotient-respecting vertex counting.
  L3's general specification admits all three conditions at the vertex level. **Supports.**
- **L4 (statistics class).** Case-P statistics for $\tau_g$ + Case-R statistics for charged rule-types preserved at vertices. **Supports.**
- **Classification (overall):** **supports** — L3 is load-bearing and admits gauge-quotient at vertex level.

### 3.5 Primitive 10 — individuation threshold (load-bearing for QV4)

- **Test (QV4).** Does Primitive 10 respect gauge equivalence at vertex counting?
- **Analysis.** Per Q.2 Memo 02 §3.5's Q3-A outcome, Primitive 10's threshold consults *physical* (gauge-invariant) observables at the kinematic level. At the vertex level, the natural extension is: Primitive 10's vertex-individuation consults gauge-invariant *vertex* observables (QV1: gauge-invariant vertex factors, gauge-invariant fermion currents; QV3: Wilson loops; QV2: vertex-density measurements through Killing-contracted bandwidth content).
  
  Since all observables Primitive 10 consults at the vertex level are gauge-invariant, the threshold's output is the same on gauge-equivalent vertex configurations. **Primitive 10 vertex-individuation respects gauge equivalence automatically (vertex-level Q3-A).**
- **Subtlety.** Same as Q.2 Memo 02 §3.5: the discipline that Primitive 10 consults gauge-invariant observables (rather than gauge-non-invariant configuration-level content) is required. At the vertex level, this discipline is the same one verified at Q.2 Memo 03 §2.6 (phase-observable discipline confirmed against inherited theorem structure). The vertex-level lift is automatic.
- **Tension.** Mild — the same phase-observable discipline question lifts to the vertex level. Resolved by Q.2 Memo 03's audit.
- **Falsifiers triggered.** Fal-7 (vertex-counting fails to respect gauge equivalence) NOT triggered — the vertex-level Q3-A automatic outcome handles vertex-counting via gauge-invariant observables.
- **Classification:** **supports** (vertex-level Q3-A automatic, conditional on the inherited gauge-invariant-observable discipline).

### 3.6 Primitive 11 — commitment dynamics

- **Test (QV2).** Does the vertex-density commitment-rate construction respect Primitive 11's general specification?
- **Analysis.** Primitive 11 specifies commitment events as primitive-level dynamical content. The Phase-1 framework specialised to per-proper-time commitment rates along timelike worldlines. For $\tau_g$'s lightlike worldline, the per-proper-time specialisation does not apply (no rest frame), but the *general* commitment-event structure is preserved.
  
  The vertex-density extension (commitment rate per vertex density along $\tau_g$'s lightlike trajectory, with the proportionality constant from minimal-coupling vertex factor magnitudes) replaces "commitment rate per proper time" with "commitment rate per vertex density." This is structurally a *change of measure* on the worldline parametrisation — affine parameter rather than proper time, vertex density rather than per-proper-time rate.
  
  **Primitive 11 admits this measure-change** because its general specification commits to commitment events as primitive-level dynamical content, not to a specific worldline parametrisation.
- **Tension.** The full reconciliation requires Q.7's lightlike-worldline reformulation (R-1) — Q.7 will specify the affine-parameter machinery and verify the per-worldline vertex-density accounting. At Q.3 level, the Q.3-side admissibility is established; Q.7 will complete the reconciliation.
- **Falsifiers triggered.** Fal-8 (P-11 incompat with vertex commitment) NOT triggered at Q.3-side level. Full reconciliation pending Q.7.
- **Classification:** **supports** (admits vertex-density commitment rate as structural extension; full reconciliation Q.7-deferred).

### 3.7 Primitive-level audit summary for V3

| Primitive | Classification | Note |
|---|---|---|
| **P-02** | supports | Manifold admits gauge-invariant vertex observables and Wilson loops |
| **P-04** | supports | Killing-contracted bandwidth observables gauge-invariant; non-Abelian generalisation clean |
| **P-06** | supports | Lorentz covariance verifies vertex factors and Wilson loops |
| **P-07** | supports | L3 lever load-bearing; admits gauge-quotient at vertex level (L3-Q-V1/V2/V3 conditions) |
| **P-10** | supports (vertex-level Q3-A) | Vertex-individuation respects gauge equivalence automatically via gauge-invariant observables |
| **P-11** | supports (Q.3-side; Q.7 reconciliation) | Admits vertex-density commitment rate as structural extension |

**No primitive forbids V3. All six primitives support, with P-10 (vertex-level Q3-A automatic) and P-11 (vertex-density extension) the load-bearing supports. No falsifier (VFal-7, VFal-2, VFal-4, VFal-9) triggered at primitive-level audit.**

---

## 4. Structural Requirements for V4 (Vertex-Anchored Commitment, Final Q.3-Side Closure)

### 4.1 Integration of V1, V2, V3 into V4

The full vertex-anchored commitment specification for $\tau_g$ at the Q.3-side closure level integrates:

- **From V1 (Memo 01):** the vertex taxonomy T1–T4 supplies the commitment-event candidates. $\tau_g$'s commitment events occur at exactly these vertex types.
- **From V2 (Memo 01):** the minimal-coupling vertex form supplies the structural vertex content. Each commitment event's structural form is determined by $D_\mu = \partial_\mu + (ig/\hbar) A^a_\mu T^a$.
- **From V3 (this Memo):** vertex-mediated individuation respects gauge equivalence. $\tau_g$ commitment events at gauge-equivalent vertex configurations count as one commitment event.

### 4.2 The full vertex-anchored commitment rule for τ_g

**(R-3 Q.3-side specification, complete):**

For the gauge rule-type $\tau_g$:

1. **Source.** Commitment events are sourced exclusively at interaction vertices of types T1, T2, T3, T4 (per V1).
2. **Structural form.** Each commitment event has the structural form of the minimal-coupling vertex content at the corresponding vertex type (per V2). Vertex factor: $-ig/\hbar \cdot \gamma^\mu T^a$ for T1 / T2; structure-constant content $f^{abc}$ for T3; paired structure-constant contractions for T4.
3. **Gauge-equivalence-class counting.** Commitment events are individuated by gauge-equivalence-class vertex configuration $[V]$, not by raw vertex configuration $V$ (per V3). Two vertex configurations differing by a gauge transformation count as ONE commitment event.
4. **Vertex-density-dependent rate.** $\tau_g$'s per-worldline commitment-event rate is proportional to the local vertex density (number of vertex events per unit affine parameter along $\tau_g$'s lightlike trajectory).
5. **Primitive 11 admissibility.** This vertex-anchored commitment rule is a structural extension of Primitive 11's commitment-dynamics specification, replacing "per proper time" with "per vertex density" and "worldline-intrinsic events" with "vertex-anchored events."

### 4.3 Minimal structural form of commitment events

The minimal structural form of a commitment event for $\tau_g$ at vertex $V$:

$$
\langle \text{commitment event at } [V] \rangle = \langle \text{gauge-invariant vertex observable at } [V] \rangle \cdot \langle \text{vertex multiplicity factor for } \tau_g \rangle
$$

Where:
- The gauge-invariant vertex observable is built from QV1 (gauge-invariant vertex factors), QV3 (Wilson-loop content if applicable), QV5 (non-Abelian Killing-contracted content).
- The vertex multiplicity factor is the count of $\tau_g$ quanta participating in the vertex (1 for T1, 1 for T2, 3 for T3, 4 for T4).

This is the minimal structural form at the Q.3 level. The full quantum-mechanical content (amplitudes, propagators between vertices, etc.) is Q.7 second-quantisation work.

### 4.4 What's deferred to Q.7 / Q.8

- **R-1 (Q.7): lightlike-worldline reformulation.** Affine-parameter machinery for $\tau_g$'s propagation between vertices; per-worldline accounting of vertex-anchored commitment events in the affine-parameter framework; full reconciliation of the vertex-density commitment-rate construction with Primitive 11's general specification.
- **R-5 partial (Q.7): vacuum-vs-particle status, vacuum-field aspect.** Background field interpretation of $\tau_g$; whether $\tau_g$'s vertex events extend to vacuum-state configurations (vacuum polarisation, virtual vertex pairs).
- **R-5 completion (Q.8): zero-point aspect.** Zero-point fluctuations as primitive-level content of the vacuum; reconciliation with Λ-from-V₁ derivation (Phase-3 background).

The Q.3-side closure of R-3 is structurally complete pending these Q.7 / Q.8 items.

---

## 5. Primitive-Level Audit for V4

### 5.1 Primitive 11 — commitment dynamics (load-bearing for V4 + R-3)

- **Test.** Does Primitive 11 admit the full vertex-anchored commitment rule (per §4.2) as a structural extension?
- **Analysis.** Per §3.6 (V3 audit), Primitive 11 admits the vertex-density commitment-rate construction as a structural extension. Adding V3's gauge-equivalence-class counting (vertex-mediated individuation) to the specification does not introduce additional Primitive 11 obstructions — it specialises the *which vertex configurations count as distinct commitment events* question, which Primitive 11 hands off to Primitive 10 (per Q.2 Memo 02's individuation discipline).
  
  Adding V1's vertex taxonomy + V2's minimal-coupling structural form completes the specification: $\tau_g$'s commitment events are exactly the vertex events of types T1–T4 with the minimal-coupling structural content, individuated by gauge-equivalence-class.
- **Tension.** The full Phase-1 reconciliation (per-proper-time → per-vertex-density measure change) requires Q.7's lightlike-worldline reformulation. At Q.3 level, the Q.3-side admissibility is established; Q.7 will complete the reconciliation.
- **Falsifiers triggered.** **VFal-8 (P-11 incompat with vertex commitment) NOT triggered.** Final Q.3-side dispatch: Primitive 11 admits the vertex-anchored commitment rule as structural extension at Q.3 level.
- **Classification:** **supports** (Q.3-side full admissibility; Q.7 reconciliation).

### 5.2 Other primitives at V4 level

- **Primitive 02:** background — supplies the spacetime structure for vertex events along $\tau_g$'s lightlike trajectory. Q.3-side admissibility clean; Q.7 reformulation pending.
- **Primitive 04:** supports — bandwidth content at vertex events is consistent with Killing-contracted gauge-invariant observables (per V3 audit).
- **Primitive 06:** supports — Lorentz covariance preserved at vertex events.
- **Primitive 07:** supports — L3 interface admits the vertex-anchored commitment specification.
- **Primitive 10:** supports — vertex-mediated individuation respects gauge equivalence (per V3).

### 5.3 V4 audit summary

| Primitive | V4 classification | Note |
|---|---|---|
| **P-02** | neutral (Q.3-side); supports background | Manifold + lightlike worldline (Q.7 reformulation) |
| **P-04** | supports | Bandwidth content at vertex events gauge-invariant |
| **P-06** | supports | Lorentz covariance preserved |
| **P-07** | supports | L3 admits vertex-anchored commitment specification |
| **P-10** | supports | Vertex-mediated individuation per V3 closure |
| **P-11** | supports (Q.3-side) | Vertex-anchored commitment rule as structural extension; full reconciliation Q.7 |

**No primitive forbids V4. P-11 supports at Q.3-side level (load-bearing); other primitives support or are neutral background.** **VFal-8 NOT triggered at Q.3-side full closure level.**

---

## 6. Falsifier Analysis (VFal-7 and VFal-8)

### 6.1 VFal-7 — Vertex-level quotient failure

- **Statement.** Vertex-counting structurally distinguishes gauge-equivalent vertex configurations (commits each as a distinct event), or gauge-invariant vertex observables cannot be defined consistently with Primitive 10 + Primitive 11 at the vertex level.
- **Audit (per §2 + §3).** All five QV1–QV5 requirements structurally admissible at primitive level. P-10 supports vertex-level Q3-A automatic via gauge-invariant observables; P-11 supports vertex-density-dependent commitment rate. QV1 (gauge-invariant vertex observables), QV3 (Wilson loops), QV5 (non-Abelian Killing-contracted content) supply the gauge-invariant content. QV4 (quotient-respecting vertex counting) follows from QV1's gauge-invariance + Primitive 10's threshold operating on gauge-invariant observables.
- **Verdict on VFal-7: NOT triggered.** Vertex-level gauge-quotient individuation is structurally clean at the Q.3 level.

### 6.2 VFal-8 — Primitive 11 incompatibility with vertex-anchored commitment

- **Statement.** Primitive 11's commitment-dynamics specification requires worldline-intrinsic commitment events that lightlike $\gamma_{\tau_g}$ cannot supply, with no admissible vertex-anchored alternative.
- **Audit (per §5).** Primitive 11's general specification commits to commitment events as primitive-level dynamical content, not specifically to worldline-intrinsic events with per-proper-time accounting. The worldline-intrinsic + per-proper-time framing was a Phase-1 single-rule-type specialisation. The vertex-anchored + per-vertex-density specification is a structural extension to the gauge-rule-type case, admissible at Primitive 11's general level. The full reconciliation (e.g., explicit derivation of how the per-vertex-density measure relates to Primitive 11's general specification) requires Q.7's lightlike-worldline reformulation.
- **Verdict on VFal-8 (final Q.3-side dispatch): NOT triggered at Q.3-side closure level.** Full reconciliation pending Q.7.

### 6.3 Cumulative falsifier-status table for V3 + V4

| Falsifier | Status at Q.3 Memo 02 | Where dispatched |
|---|---|---|
| **VFal-1** (vertex primitive incompat.) | not triggered | Memo 01 §4 + Memo 02 §3 + §5 |
| **VFal-2** (vertex L3 incompat.) | **NOT triggered** at V3 level | Memo 02 §3.4 (L3-Q-V1/V2/V3 conditions) |
| **VFal-3** (vertex breaks GRH-1/2/4) | not triggered | Memo 01 §6 (V1 + V2 level) |
| **VFal-4** (cross-substage individ. failure) | **NOT triggered** at V3 level | Memo 02 §3 + §5 |
| **VFal-5** (vertex taxonomy inconsistent) | not triggered | Memo 01 §6.1 |
| **VFal-6** (minimal coupling not unique) | not triggered | Memo 01 §6.2 |
| **VFal-7** (vertex-counting fails gauge) | **NOT triggered** | Memo 02 §6.1 |
| **VFal-8** (P-11 incompat. vertex commitment) | **NOT triggered (Q.3-side full)** | Memo 02 §6.2 (final Q.3-side dispatch); full reconciliation Q.7 |
| **VFal-9** (Q.3 ⟷ Q.7 circular) | deferred to Memo 03 (V5 closure) | — |

**No falsifier triggered for V3 or V4 at the Q.3-side closure level.** VFal-9 (Q.3 ⟷ Q.7 circular) deferred to Memo 03 for V5 dependency-map audit.

---

## 7. Provisional Verdicts for V3 and V4

### 7.1 V3 verdict

**V3 (vertex-level gauge-quotient individuation, R-2 completion): CANDIDATE-FORCED.**

Specifically: vertex-level individuation respects gauge equivalence automatically (vertex-level Q3-A) because Primitive 10's vertex-individuation consults gauge-invariant vertex observables (gauge-invariant vertex factors per QV1, Wilson loops per QV3, Killing-contracted vertex content per QV5). All five structural requirements (QV1–QV5) are primitive-level admissible; no primitive forbids; no falsifier triggered (VFal-7 explicitly NOT triggered).

The "FORCED" force is **conditional on** the gauge-invariant-vertex-observable discipline, which lifts directly from Q.2 Memo 03's confirmed phase-observable discipline. The discipline is structurally inherited from the FORCED theorem structure (Theorems 10, 11–12, 14) — physical observables are gauge-invariant by construction.

R-2 completion: **CLOSED CANDIDATE-FORCED at Q.3 Memo 02.**

### 7.2 V4 verdict

**V4 (vertex-anchored commitment for $\tau_g$, full Q.3-side closure): CANDIDATE-FORCED at Q.3-side.**

Specifically: $\tau_g$'s commitment events are sourced at V1 vertex types T1–T4, with minimal-coupling structural form (V2), individuated by gauge-equivalence-class (V3), with vertex-density-dependent commitment rates extending Primitive 11's specification. Primitive 11 admits this vertex-anchored commitment rule as a structural extension at the Q.3 level; full Phase-1 reconciliation requires Q.7's lightlike-worldline reformulation.

VFal-8 (P-11 incompat) NOT triggered at Q.3-side full closure level.

R-3 (Q.3-side): **CLOSED CANDIDATE-FORCED at Q.3 Memo 02.** Full R-3 closure trajectory: Q.7 (R-1 lightlike-worldline + R-5 partial vacuum-field aspect) + Q.8 (R-5 completion zero-point aspect).

### 7.3 Justification

The two verdicts rest on:

- **Primitive-level audit (§3 + §5).** No primitive forbids V3 or V4. All six primitives support (with P-10 + P-11 load-bearing).
- **Inheritance from Q.2 + Memo 01.** Q.2's gauge-quotient structure lifts cleanly to the vertex level (Q3-A automatic individuation generalises). Memo 01's V1 vertex taxonomy and V2 minimal-coupling vertex form supply the structural backbone for V3 + V4.
- **Falsifier status (§6).** No falsifier triggered. VFal-7, VFal-8 explicitly NOT triggered; VFal-2, VFal-4 NOT triggered at V3 level; VFal-9 deferred to Memo 03.
- **Inherited theorem structure.** Theorems 10, 11–12, 14 supply the gauge-invariance discipline that QV1 + QV3 + QV5 leverage. Theorem 16 (U3 Schrödinger evolution) supplies the time-evolution framework that vertex events fit into.

### 7.4 Why CANDIDATE-FORCED rather than FORCED

V3 + V4 carry forward the same conditional-forcing structure as Q.2's verdict pattern:

- **Specific gauge-group choice empirical** (per Q.2 F4 closure inherited).
- **Coupling constants empirical** (per Dimensional Atlas).
- **Q.7 + Q.8 closures pending** for full R-3 closure (R-1 + R-5).
- **GRH itself promotes to FORCED-unconditional only when all five refinements close.**

The CANDIDATE-FORCED verdict is the strongest defensible substage-level closure.

---

## 8. Implications for R-2 and R-3

### 8.1 R-2 closure status

**R-2 CLOSED at Q.3 Memo 02.**

R-2 had two stages:
- **R-2 partial** (kinematic gauge-quotient, Q.2 Memo 02): ✅ CLOSED CANDIDATE-FORCED
- **R-2 completion** (vertex-level gauge-quotient, Q.3 Memo 02 / V3): ✅ **CLOSED CANDIDATE-FORCED at this Memo**

R-2 is now FULLY CLOSED in the GRH refinement-closure map. No further R-2 work in Q.7 or Q.8.

### 8.2 R-3 closure status

**R-3 CLOSED at Q.3-side at Q.3 Memo 02; full R-3 closure pending Q.7 + Q.8.**

R-3 has Q.3-side and Q.7/Q.8-side components:
- **Q.3-side** (vertex-anchored commitment specification, V4 full Q.3-side): ✅ **CLOSED CANDIDATE-FORCED at this Memo**
- **Q.7-side** (R-1 lightlike-worldline reformulation; per-worldline accounting in affine-parameter framework): outstanding
- **Q.8-side** (R-5 vacuum-state vertex content; vacuum-vs-particle status reconciliation): outstanding

R-3's Q.3-side closure is structurally complete; Q.7 + Q.8 closures will finalise R-3.

### 8.3 What remains for Q.7 / Q.8

For R-3's full closure:

- **Q.7 R-1 (lightlike-worldline reformulation):** affine-parameter machinery for $\tau_g$ propagation between vertices; per-worldline accounting with vertex-density commitment rate.
- **Q.7 R-5 partial (vacuum-field aspect):** background field interpretation of $\tau_g$; vacuum-state vertex events.
- **Q.8 R-5 completion (zero-point aspect):** zero-point fluctuations as primitive-level vacuum content.

For GRH's full closure (independent of R-3):

- **Q.7 + Q.8 substantive work** on lightlike-worldline + vacuum framework.
- **Arc Q synthesis** integrating Q.2 / Q.3 / Q.7 / Q.8 results; promoting GRH to FORCED-unconditional.
- **Cascade to Arc M** (F-M8 promotion).

### 8.4 Updated GRH refinement-closure map (post-Memo 02)

| Refinement | Pre-Memo-02 status | Post-Memo-02 status | Closure stage |
|---|---|---|---|
| **R-1** | outstanding | (unchanged) | Q.7 |
| **R-2 partial** | CLOSED (Q.2 Memo 02) | (unchanged) | Q.2 Memo 02 |
| **R-2 completion** | outstanding | **CLOSED CANDIDATE-FORCED ✅** | **Q.3 Memo 02 (this)** |
| **R-3** | partial closure (Memo 01) | **CLOSED Q.3-side; Q.7/Q.8 trajectory ongoing** | **Q.3 Memo 02 (this) + Q.7 + Q.8** |
| **R-4** | CLOSED (Q.2 Memo 01) | (unchanged) | Q.2 Memo 01 |
| **R-5 partial** | outstanding | (unchanged) | Q.7 |
| **R-5 completion** | outstanding | (unchanged) | Q.8 |

**Cumulative closure: 4/7 refinements closed (R-2 partial, R-2 completion, R-3 Q.3-side, R-4); 3/7 + Q.7/Q.8-side of R-3 outstanding.**

---

## 9. Honest Scope Limits

Memo 02 addresses V3 + V4 (Q.3-side full closure). The following are explicitly out of scope:

### 9.1 Deferred to Q.3 Memo 03

- **V5 (downstream dependency map for Q.7 / Q.8).** Memo 03 substantive content.
- **Q.3 substage verdict** (anticipated CLOSED CANDIDATE-FORCED).
- **VFal-9 (Q.3 ⟷ Q.7 circular) full dispatch** at V5 level.
- **Refinement-closure map final state for Q.3 substage.**

### 9.2 Deferred to Q.7

- **R-1 (lightlike-worldline reformulation for $\tau_g$).** Affine-parameter machinery.
- **R-5 partial (vacuum-field aspect of $\tau_g$).** Background field interpretation.
- **Per-worldline accounting in lightlike framework** with vertex-density commitment rate full reconciliation.
- **Vertex-level renormalisation procedures.** Counter-term content for vertex factors.
- **Standard QFT amplitude / scattering content.** Cross-sections, Feynman-diagram amplitudes.

### 9.3 Deferred to Q.8

- **R-5 completion (zero-point aspect).** Vacuum-state vertex content.
- **Vacuum polarisation contributions.** Virtual vertex pairs.
- **Λ from vacuum-vertex content.** Already partially established via Theorem 9 Phase-3 background.

### 9.4 Outside the GRH closure trajectory

- **Specific gauge group choice** ($SU(3) \times SU(2) \times U(1)$ or any other). Empirical inheritance per Q.2 F4.
- **Coupling constant values** ($q$, $g_s$, $g_w$). Empirical via Dimensional Atlas.
- **Charged-rule-type representations.** Empirical / Q.4-onward.
- **Higgs sector / SSB vertex content.** Q.4; SPECULATIVE.
- **Generation structure / flavor-changing vertex content.** Q.6 / empirical.
- **Charge quantization pattern.** Possibly Q.2 / Q.3 partial sub-memo or empirical.

These scope limits are honest structural boundaries inherited from the broader Q-substage scoping discipline.

---

## 10. One-Line Summary

> Q.3 Memo 02 closes V3 (vertex-level gauge-quotient individuation, R-2 completion) at **CANDIDATE-FORCED** via the vertex-level analog of Q.2 Memo 02's Q3-A automatic outcome — Primitive 10 vertex-individuation respects gauge equivalence by consulting gauge-invariant vertex observables (Wilson loops via QV3, gauge-invariant vertex factors via QV1, Killing-contracted vertex content via QV5), with all five structural requirements (QV1-QV5) primitive-level admissible across P-02/04/06/07/10/11 and no falsifier (VFal-7, VFal-2, VFal-4) triggered — and closes V4 (vertex-anchored commitment for $\tau_g$, full Q.3-side closure) at **CANDIDATE-FORCED at Q.3-side** by integrating V1 vertex taxonomy + V2 minimal-coupling structural vertex form + V3 vertex-mediated individuation into a complete vertex-anchored commitment specification (commitment events at vertex types T1-T4, gauge-equivalence-class counting, vertex-density-dependent commitment rate extending Primitive 11), with Primitive 11 admitting the structural extension at Q.3 level (VFal-8 NOT triggered at Q.3-side; full reconciliation Q.7) — discharging **R-2 completion** (R-2 now FULLY CLOSED in the GRH refinement-closure map) and **R-3 Q.3-side** (R-3 closure trajectory continues Q.7 + Q.8 for R-1 lightlike-worldline + R-5 vacuum status), with cumulative GRH closure progress now 4/7 refinements closed (R-2 partial + R-2 completion + R-3 Q.3-side + R-4), advancing the Q.3 substage to Memo 03 (verdict + cascade) and the full GRH closure trajectory to Q.7 (R-1 + R-5 partial) + Q.8 (R-5 completion).

---

## Recommended Next Steps

**(a) Begin Q.3 Memo 03 (verdict + cascade).** The natural next deliverable. Memo 03 should: (i) close V5 (downstream dependency map for Q.7 + Q.8); (ii) integrate V1-V4 closures into the Q.3 substage verdict; (iii) dispatch VFal-9 (Q.3 ⟷ Q.7 circular) at V5 level; (iv) issue the Q.3 substage verdict (anticipated: CLOSED CANDIDATE-FORCED, with R-2 fully closed + R-3 Q.3-side closed); (v) update the GRH refinement-closure map; (vi) sketch the cascade into Q.7 + Q.8 with explicit handoffs. Anticipated length: comparable to Q.2 Memo 03.

**(b) Pre-Memo-03 verification of the Wilson-loop / gauge-invariant vertex observable construction noted in §3.2.** A short audit (15-30 minutes) verifying that QV1 + QV3 + QV5 supply a complete observable algebra at the vertex level. Key sub-question: do Wilson loops + gauge-invariant vertex factors + Killing-contracted content fully generate the gauge-invariant vertex observable algebra, or are additional construction steps required? Anticipated yes (the standard mathematical machinery is sufficient), but worth pre-checking before Memo 03.

**(c) Defer memory-record update until Q.3 closure (Memo 03).** Per the discipline established in U3 / U4 / U5 arcs and the GRH closure roadmap §10. The bundled memory update will capture: R-2 fully closed (CANDIDATE-FORCED across Memo 02 + Q.2 Memo 02), R-3 Q.3-side closed (CANDIDATE-FORCED at this Memo), cumulative 4/7 refinements closed, Q.3 substage verdict, downstream handoffs to Q.7 / Q.8.

**(d) Sketch the Q.7 substage opening now.** With Q.3 substantive work nearly complete (Memos 01-02 closed; Memo 03 integration only), the Q.7 Memo 00 outline can be drafted. Q.7's load: R-1 (lightlike-worldline reformulation) + R-5 partial (vacuum-field aspect of $\tau_g$). Anticipated structure: 4-5 memos parallel to Q.2 / Q.3 pattern but substantively heavier (full second-quantisation framework). Pre-sketching now would let Q.7 land into a known scope when Q.3 closes; useful for trajectory planning.

**(e) (Optional) Sketch the GRH FORCED-theorem statement now.** With 4/7 refinements closed and the trajectory clean, the anticipated FORCED-GRH theorem statement (per `00_grh_closure_roadmap.md` §5 + Q.2 Memo 03 §7.4) can be drafted in skeleton form. This would let Arc Q synthesis (post-Q.7 / Q.8) work efficiently when reached. Optional but useful for trajectory visibility.
