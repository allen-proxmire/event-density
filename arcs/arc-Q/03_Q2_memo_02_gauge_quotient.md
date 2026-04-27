# Q.2 Memo 02 — F3: Gauge-Quotient Individuation (R-2 Partial Closure)

**Stage:** Arc Q · Q.2 · Memo 02 (load-bearing F3 derivation)
**Date:** 2026-04-26
**Location:** `arcs/arc-Q/`
**Goal:** Discharge **R-2 partial** (gauge-quotient individuation at the gauge-group-scoping level) by deriving F3 — the structural compatibility of Primitive 10's individuation threshold with the gauge equivalence relation $A_\mu \sim U A_\mu U^{-1} + (i/g) U \partial_\mu U^{-1}$ established as admissible in Memo 01. Determine whether Primitive 10 respects gauge equivalence automatically, or requires an explicit gauge-quotient construction at the framework level. Either outcome closes R-2 partially; the difference is the downstream machinery propagating to Q.3 (vertex-level quotient, R-2 completion).
**Predecessors:** [`grh_evaluation.md`](grh_evaluation.md) (Q.1) · [`00_grh_closure_roadmap.md`](00_grh_closure_roadmap.md) · [`01_Q2_memo_00_outline.md`](01_Q2_memo_00_outline.md) (Q.2 Memo 00; F3 designated load-bearing alongside F2) · [`02_Q2_memo_01_non_abelian.md`](02_Q2_memo_01_non_abelian.md) (Q.2 Memo 01; F2 closed CANDIDATE-FORCED; gauge equivalence relation established as well-defined; gauge-quotient existence confirmed; *construction* deferred to this memo)
**Status:** Technical derivation memo. Operates under strict forbidden-input discipline (per Memo 00 §5): no R-1, R-3, R-5; no SM specifics; no Higgs, generations, or coupling constants; no F-M8 cascade; no Yang-Mills or BRST as derivation premise. Inherits Memo 01's CANDIDATE-FORCED closure of F2 as background — non-Abelian admissibility may be assumed; this memo addresses the *individuation* of the redundancy.
**Purpose:** State and discharge F3 with the strongest defensible verdict, completing the load-bearing primitive-level work for the Q.2 substage so Memo 03 can integrate F1 / F4 / F5 and issue the Q.2 verdict.

---

## 1. The F3 Question (Restated)

### 1.1 Precise statement

F3 asks: **how does Primitive 10's individuation threshold interact with the gauge equivalence relation $A_\mu \sim U A_\mu U^{-1} + (i/g) U \partial_\mu U^{-1}$ — does Primitive 10 respect this equivalence automatically (counting gauge-equivalent configurations as one rule-type instance), or does the framework require an explicit gauge-quotient construction $[A_\mu] = A_\mu / \mathcal{G}$ at the individuation level?**

The question is *not* whether the gauge equivalence relation exists as a well-defined mathematical object — that was Memo 01's work (§5: equivalence relation well-defined for compact $G$; quotient space $\mathcal{A} / \mathcal{G}$ structurally well-behaved modulo the global Gribov ambiguity, deferred to Q.7).

The question is also *not* whether vertex-level interactions respect gauge equivalence — that is **R-2 completion**, deferred to Q.3 (vertex classification). Q.3 will address how interaction vertices count as commitment events under gauge equivalence.

F3 at Memo 02 addresses only the **individuation-threshold-level** question: when Primitive 10 counts rule-type instances at fixed time on the participation graph, does the counting respect $[A_\mu]$ equivalence classes?

### 1.2 Relation to GRH-3 and R-2

**To GRH-3.** GRH-3 asserts that $\tau_g$'s L3 interface enforces local gauge invariance. The L3 interface specifies *how* the rule-type interacts with charged rule-types and with itself; if Primitive 10 individuation does not respect gauge equivalence, the L3-enforced invariance becomes inconsistent at the kinematic level (two gauge-equivalent configurations would be interface-equivalent but individuation-distinct, a structural contradiction).

F3 is therefore the individuation-side consistency check on GRH-3: the L3 interface side of GRH-3 is established (Memo 01 §4); F3 verifies the individuation side.

**To R-2.** The Q.1 evaluation memo §3.5 introduced R-2 as: "Whether Primitive 10's individuation threshold automatically respects gauge-equivalence, or requires an additional gauge-quotient structure at the individuation level." This is precisely F3's question.

R-2 has two stages:
- **R-2 partial** (this Memo): the gauge-group-scoping individuation structure — how Primitive 10 handles $A_\mu$ configurations under gauge equivalence at fixed time.
- **R-2 completion** (Q.3): the vertex-level quotient — how interaction vertices respect gauge equivalence as commitment events.

R-2 partial closure here advances the GRH closure trajectory; R-2 completion at Q.3 finishes it.

### 1.3 Outcome criteria

- **FORCED:** Primitive 10 individuation *automatically* respects gauge equivalence with no additional framework-level machinery — counting is on equivalence classes by construction. Anticipated as the strongest possible outcome.
- **CANDIDATE-FORCED:** the gauge-quotient is *structurally forced* at the framework level, requiring an explicit construction step that Primitive 10 then operates on. Counting is on equivalence classes via the explicit quotient projection. Anticipated default outcome.
- **CANDIDATE-admissible:** the gauge-quotient is admissible but the construction is not uniquely forced (multiple admissible quotient procedures, or the choice of representative matters at some level). Anticipated fallback if the construction has gauge-fixing ambiguities Q.2 cannot resolve.
- **SPECULATIVE-admissible:** weak admissibility; substantial refinement needed before R-2 partial can close.
- **REFUTED:** Primitive 10 individuation is *incompatible* with gauge equivalence at the kinematic level — no quotient construction can reconcile them. This would force restriction of GRH content to gauge groups for which the conflict doesn't arise.

The work below establishes which outcome obtains.

---

## 2. Structural Requirements for a Valid Gauge Quotient

For Primitive 10 individuation to operate consistently with gauge equivalence, the framework must structurally support five distinct requirements. Each is stated, mapped to its primitive dependencies, and bounded by what it does *not* commit to.

### 2.1 (Q1) Equivalence-relation well-definedness

- **Statement.** The gauge equivalence relation $A_\mu \sim A'_\mu \iff \exists U: \mathcal{M} \to G, \; A'_\mu = U A_\mu U^{-1} + (i/g) U \partial_\mu U^{-1}$ is reflexive, symmetric, transitive, and smooth on the configuration space of $A_\mu$ fields.
- **Commits to:** the equivalence relation is a structurally well-defined object on the participation-graph configuration space.
- **Does NOT commit to:** any specific gauge group $G$; this is admissibility for *any* compact Lie group inherited from Memo 01's F2 closure.
- **Primitive dependencies:** Primitive 06 (smoothness on the spacetime manifold); Primitive 02 (smooth manifold structure for $U: \mathcal{M} \to G$).
- **Inherited FORCED items:** none directly (this is structural mathematics).
- **Status from Memo 01:** **established** (Memo 01 §5 — equivalence relation well-defined for compact $G$; clean by principal-bundle theory).

### 2.2 (Q2) Quotient-space structural consistency

- **Statement.** The quotient space $\mathcal{A} / \mathcal{G}$ — configurations modulo gauge transformations — is a structurally consistent object: Hausdorff (modulo the Gribov ambiguity, deferred), smoothly parameterised by gauge-invariant content, and supports a well-defined participation-measure structure derived from $\tau_g$'s rule-type properties.
- **Commits to:** physical content lives on $\mathcal{A} / \mathcal{G}$, not on $\mathcal{A}$.
- **Does NOT commit to:** any specific gauge-fixing prescription (e.g., Lorenz gauge, Coulomb gauge); the choice of gauge fix is a description-level convenience, not a structural commitment.
- **Primitive dependencies:** Primitive 04 (bandwidth fields must descend to gauge-invariant content on the quotient); Primitive 06 (smooth structure preserved under quotient).
- **Inherited FORCED items:** Theorems 11–12 (U2-Discrete + U2-Continuum; the Hilbert-space inner product must descend to the quotient — gauge-equivalent configurations must be inner-product-equivalent).
- **Status from Memo 01:** **established at the existence level** (Memo 01 §5 confirmed quotient space structurally well-behaved); construction details addressed here.

### 2.3 (Q3) Primitive 10 compatibility

- **Statement.** Primitive 10's individuation threshold operates on $\mathcal{A} / \mathcal{G}$ rather than on $\mathcal{A}$ — i.e., the threshold for distinguishing two $\tau_g$ rule-type instances is sensitive to the gauge-equivalence-class content, not to the specific gauge representative.
- **Commits to:** Primitive 10 individuation respects gauge equivalence at the kinematic level.
- **Does NOT commit to:** *how* it respects gauge equivalence — automatically (Q3-A: Primitive 10 is gauge-quotient-respecting natively) or via explicit construction (Q3-B: Primitive 10 operates on gauge-quotient projections supplied by an explicit framework-level mechanism).
- **Primitive dependencies:** Primitive 10 (the central primitive); Primitive 04 (bandwidth content tracked under quotient); Primitive 06 (smooth quotient structure for individuation threshold to operate on).
- **Inherited FORCED items:** Theorem 14 (U1 — participation-measure construction must respect gauge equivalence at the magnitude+phase level).
- **Load-bearing:** this is the substantive content of F3.

### 2.4 (Q4) Gauge-invariance of physical observables

- **Statement.** All physical observables (bandwidth content, individuation-threshold values, U2 inner products, Born-rule probabilities, etc.) are gauge-invariant — i.e., they take equal values on gauge-equivalent $A_\mu$ configurations.
- **Commits to:** physical content is intrinsic to $[A_\mu]$, not to choice of representative.
- **Does NOT commit to:** a specific gauge-invariant observable algebra; the structural commitment is to gauge-invariance of *whatever* physical observables the framework supports.
- **Primitive dependencies:** Primitive 04 (gauge-invariant bandwidth content); Primitive 10 (gauge-invariant individuation values); Primitive 11 (gauge-invariant commitment events; partial — vertex-level invariance is R-3 / Q.3 content).
- **Inherited FORCED items:** Theorem 10 (Born rule must give gauge-invariant probabilities); Theorems 11–12 (U2 inner product gauge-invariant); Theorem 14 (U1 participation-measure gauge-covariant).

### 2.5 (Q5) Topological consistency (Gribov ambiguity scoping)

- **Statement.** The gauge-quotient construction is locally well-defined; global topological obstructions (Gribov copies, principal-bundle non-trivialities) are scoped as Q.7 / second-quantisation content, not Q.2-level obstructions.
- **Commits to:** Q.2's gauge-quotient closure is at the *local* primitive-level kinematic level; global topology is downstream.
- **Does NOT commit to:** a resolution of the Gribov ambiguity; the global topological structure of $\mathcal{A} / \mathcal{G}$ is genuinely a Q.7 question.
- **Primitive dependencies:** Primitive 02 (manifold topology); Primitive 06 (smoothness).
- **Inherited FORCED items:** none directly.
- **Status:** explicitly scoped here as out of Q.2 detail; flagged as Q.7 work.

### 2.6 Joint admissibility

For F3 to close affirmatively, **all five** requirements (Q1–Q5) must be primitive-level admissible. Q1 and Q2 are established by Memo 01. Q4 follows from inherited theorems (Born + U2 + U1 are gauge-invariant by structural construction). Q5 is honestly scoped to Q.7. **Q3 is the load-bearing requirement** — whether Primitive 10 respects gauge equivalence automatically (Q3-A) or via explicit construction (Q3-B) is the substantive content of F3.

---

## 3. Primitive-Level Individuation Audit

Each primitive is tested against Q1–Q5. Classifications: **supports** (positively admits gauge-quotient individuation), **neutral** (does not interact), **constrains** (admits only restricted forms), **forbids** (Fal-3 triggered).

### 3.1 Primitive 02 — worldline + ambient 3+1D manifold

- **Test.** Does the spacetime manifold structure support the smooth $G$-valued field $U: \mathcal{M} \to G$ that defines gauge equivalence?
- **Analysis.** Primitive 02 supplies a smooth 3+1D Lorentzian manifold. Smooth $G$-valued maps are standard objects on smooth manifolds (gauge transformations are sections of the trivial $G$-bundle locally). The local structure is clean. Global topological subtleties (non-trivial principal bundles) are Q.5 scoping (Q.7-deferred).
- **Tension.** None at the local Q.2 level.
- **Falsifiers triggered.** None.
- **Classification:** **supports** (locally; global topology Q.7-deferred).

### 3.2 Primitive 04 — bandwidth fields

- **Test.** Does Primitive 04's four-band bandwidth structure descend to gauge-invariant content on the quotient $\mathcal{A} / \mathcal{G}$?
- **Analysis.** Primitive 04's four-band decomposition $\{b^{\mathrm{int}}, b^{\mathrm{adj}}, b^{\mathrm{env}}, b^{\mathrm{com}}\}$ is by-rule-type. For $\tau_g$ in the non-Abelian case (Memo 01 §3.2), each band carries Lie-algebra multiplicity: $b^X_a$ for $a = 1, \ldots, \dim \mathfrak{g}$. Under gauge transformation, the band content transforms covariantly: $b^X_a \to U^{ab} b^X_b$ (adjoint representation action). The gauge-invariant content is built from quadratic combinations: $b^X = \delta^{ab} b^X_a b^X_b$ (Killing-form-contracted), which is invariant under adjoint action.
  
  This gives the framework gauge-invariant bandwidth observables — the Killing-contracted band totals — that descend cleanly to the quotient. The component-level bandwidth $b^X_a$ does not descend (it is gauge-covariant, not gauge-invariant), but physical observables built from it do.
- **Tension.** Mild: which combinations of band content are physical observables (and thus gauge-invariant) is partly empirical inheritance and partly Q.7 / Q.8 work. At Q.2 level, the Killing-contracted observables suffice for individuation purposes.
- **Falsifiers triggered.** None.
- **Classification:** **supports** (with the understanding that gauge-invariant observables are Killing-contracted band content; component-level $b^X_a$ does not descend).

### 3.3 Primitive 06 — four-gradient + Lorentz covariance

- **Test.** Does the four-gradient structure preserve the gauge-quotient under spacetime symmetries?
- **Analysis.** Lorentz transformations act on the spacetime index $\mu$; gauge transformations act on the internal index $a$. The two actions commute (independent index spaces, per Memo 01 §3.3). The quotient $\mathcal{A} / \mathcal{G}$ inherits Lorentz covariance from $\mathcal{A}$ — Lorentz acts on equivalence classes by acting on representatives and projecting. The quotient is Lorentz-covariant.
- **Tension.** None.
- **Falsifiers triggered.** None.
- **Classification:** **supports**.

### 3.4 Primitive 07 — rule-type taxonomy

The L3 interface compatibility is the load-bearing question; full analysis in §4. At the primitive-level audit:

- **L1 (bandwidth partition):** L1 is gauge-invariant trivially (the partition $w^X_{\tau_g}$ is rule-type-data, independent of $A_\mu$ representative). Supports.
- **L2 (internal index):** the internal index $a$ transforms under the adjoint representation; L2 admits this transformation, with gauge-invariant content built from it (per §3.2). Supports.
- **L3 (interface):** the load-bearing lever — full analysis §4. Supports (anticipated).
- **L4 (statistics class):** Case P assignment is gauge-invariant (statistics depend on Lorentz content, which is unchanged under gauge transformations). Supports.

**Classification (overall): supports** — pending §4's L3 analysis.

### 3.5 Primitive 10 — individuation threshold (the load-bearing primitive)

- **Test.** Does Primitive 10's threshold operate on $\mathcal{A} / \mathcal{G}$ rather than on $\mathcal{A}$? Is this automatic (Q3-A) or via explicit construction (Q3-B)?

- **Analysis.** Primitive 10's specification (per the rule-type taxonomy synthesis) gives the individuation threshold as a function of *physical* rule-type content — bandwidth content, polarity-phase content, channel content. Per §3.2, physical bandwidth observables are gauge-invariant Killing-contracted combinations $b^X = \delta^{ab} b^X_a b^X_b$. Under gauge transformation, $b^X_a \to U^{ab} b^X_b$ but $b^X = \delta^{ab} b^X_a b^X_b \to b^X$ (invariant).
  
  Therefore: when Primitive 10's threshold consults physical bandwidth content for $\tau_g$, the values consulted are gauge-invariant, and the threshold output is the same on gauge-equivalent representatives. **Primitive 10 individuation respects gauge equivalence by virtue of operating on gauge-invariant observables.**
  
  This is the **Q3-A** outcome — Primitive 10 respects gauge equivalence *automatically*, not via explicit framework-level quotient construction. The "automatic" structure inherits from the gauge-invariance of physical observables (Q4); the gauge-quotient projection happens implicitly through the choice of which observables Primitive 10 consults.

- **Subtlety.** This argument requires that *all* the observables Primitive 10 consults are gauge-invariant. For bandwidth content, this is established (§3.2). For polarity-phase content: the polarity phase $\pi_K$ enters the U1 participation-measure construction $P_K = \sqrt{b_K} \cdot e^{i\pi_K}$. Under gauge transformation, the phase undergoes the standard gauge transformation $\pi_K \to \pi_K + q\alpha/\hbar$ (for U(1)) or its non-Abelian generalisation. This is *not* trivially gauge-invariant — but the *physical* phase content (relative phases between channels at the same point, gauge-invariant phase cycles around closed loops, etc.) is.
  
  Primitive 10's individuation threshold — to the extent it depends on phase content — must consult gauge-invariant phase observables. This is structurally available (gauge-invariant Wilson loops, relative phases, etc.), but it requires the discipline that Primitive 10's specification of phase-dependent threshold content uses gauge-invariant phase observables.

- **Refinement.** Memo 02 establishes Q3-A *conditional on* Primitive 10's threshold consulting gauge-invariant observables. If a later refinement reveals that Primitive 10's specification depends on gauge-non-invariant phase content (e.g., absolute phase rather than relative phase), Q3 would shift to Q3-B (explicit gauge-quotient construction needed at the framework level). This is a small refinement, not a structural blocker.

- **Tension.** Mild — the phase-content sub-question. Anticipated to close at Q3-A pending Memo 03's review of Primitive 10's specification.

- **Falsifiers triggered.** Fal-3 not triggered (Primitive 10 is structurally compatible). Fal-7 (cross-cutting individuation failure) not triggered at the local level.

- **Classification:** **supports** (Q3-A automatic, conditional on gauge-invariant-phase-observable discipline).

### 3.6 Primitive 11 — commitment dynamics

- **Test.** Are commitment events for $\tau_g$ gauge-invariant?
- **Analysis.** Per Memo 01 §3.6, commitment for $\tau_g$ is vertex-anchored (R-3, deferred to Q.3). Vertex-level commitment-event-counting under gauge equivalence is **R-2 completion**, the Q.3 deliverable. Q.2 commits only that the *existence* of vertex slots is admissible.
  
  At Q.2 level, the question reduces to: do non-vertex (worldline-intrinsic) commitment events exist for $\tau_g$? For $\tau_g$ on a lightlike worldline, the answer is no (per `grh_evaluation.md` §3.6 — commitment is at vertices only, no worldline-intrinsic events). So there are no Q.2-level commitment events to test for gauge invariance — the question is empty here.
- **Tension.** None at Q.2.
- **Falsifiers triggered.** None at Q.2 (vertex-level question is Q.3).
- **Classification:** **neutral** at Q.2; vertex-level work is Q.3.

### 3.7 Primitive-level audit summary

| Primitive | Classification | Note |
|---|---|---|
| **P-02** worldline + 3+1D | supports (locally) | Smooth $G$-valued maps standard; global topology Q.7-deferred |
| **P-04** bandwidth fields | supports | Killing-contracted band observables gauge-invariant; component $b^X_a$ does not descend |
| **P-06** four-gradient + Lorentz | supports | Lorentz × gauge act on independent index spaces |
| **P-07** rule-type taxonomy | supports | L1, L2, L4 trivially gauge-invariant; L3 — full analysis §4 |
| **P-10** individuation | supports (Q3-A automatic) | Conditional on gauge-invariant-phase-observable discipline |
| **P-11** commitment | neutral at Q.2 | Vertex-level question is R-3 / Q.3 |

**No primitive forbids gauge-quotient individuation. Primitive 10 supports the Q3-A outcome (automatic respect of gauge equivalence) conditional on its threshold consulting gauge-invariant observables — a discipline rather than a structural commitment.**

---

## 4. Compatibility with the L3 Interface

### 4.1 The L3 interface and the gauge quotient

The L3 interface specifies how $\tau_g$'s rule-type-specific interactions interface with charged rule-types and with itself. Under gauge equivalence, the L3 interface must satisfy three structural conditions:

- **(L3-Q-1)** The L3 interface content depends only on $[A_\mu]$, not on the choice of representative $A_\mu \in [A_\mu]$.
- **(L3-Q-2)** The L3 interface commutes with gauge transformations: applying a gauge transformation before evaluating the interface gives the same result as applying it after.
- **(L3-Q-3)** The L3 interface admits the gauge-quotient projection $\mathcal{A} \to \mathcal{A} / \mathcal{G}$ — i.e., there is a well-defined map from raw $A_\mu$ configurations to equivalence classes that is consistent with L3's structural specification.

### 4.2 (L3-Q-1) Equivalence-class action

For the Abelian case, the L3 interface for $\tau_g$ depends on $A_\mu$ through gauge-invariant combinations (the field strength $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, which is invariant under $A_\mu \to A_\mu + \partial_\mu \alpha$). For the non-Abelian case, the field strength is $F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + g f^{abc} A^b_\mu A^c_\nu$, which transforms covariantly under gauge transformations: $F^a_{\mu\nu} \to U^{ab} F^b_{\mu\nu}$. Gauge-invariant combinations are quadratic: $\mathrm{tr}(F_{\mu\nu} F^{\mu\nu}) = \delta^{ab} F^a_{\mu\nu} F^{b\mu\nu}$ (Killing-form-contracted), which is invariant.

The L3 interface content for $\tau_g$ thus depends on $A_\mu$ through gauge-invariant combinations of $F^a_{\mu\nu}$ (and gauge-covariant combinations of charged-rule-type fields, which combine with $A_\mu$-dependent terms to give gauge-invariant L3 content).

(L3-Q-1) is structurally satisfied: the L3 interface depends on $[A_\mu]$ via gauge-invariant constructions.

### 4.3 (L3-Q-2) Gauge-transformation commutation

For both Abelian and non-Abelian cases, gauge transformations act on the configuration space of $A_\mu$ and on charged-rule-type fields simultaneously (charged fields transform under representations $\rho(U)$ of $G$; $A_\mu$ transforms via the Maurer-Cartan rule). The L3 interface — which couples charged rule-types to $\tau_g$ — must commute with this joint transformation: the gauge-transformed L3 interface acts on gauge-transformed inputs to give a gauge-transformed output, identical to the un-transformed interface acting on un-transformed inputs.

This is the standard gauge-covariance of the minimal-coupling vertex (Stage R.1 background, inherited as content here, not as derivation premise). The structural admissibility was established in Memo 01 §4.4: GRH-1, GRH-2, GRH-4 are preserved under non-Abelian generalisation, which inherits the gauge-covariance structure.

(L3-Q-2) is structurally satisfied.

### 4.4 (L3-Q-3) Quotient projection

The map $\mathcal{A} \to \mathcal{A} / \mathcal{G}$ is well-defined when the equivalence relation is well-defined (Q1 from §2.1, established). The L3 interface admits this projection in the sense that L3 content evaluated on a representative $A_\mu \in [A_\mu]$ equals L3 content evaluated on the equivalence class itself — by (L3-Q-1).

(L3-Q-3) is structurally satisfied.

### 4.5 Consequences for GRH-3

GRH-3 — "the L3 interface enforces local gauge invariance" — is now consistent with Primitive 10 individuation operating on the quotient. The L3-enforced invariance and the individuation-threshold operation on $\mathcal{A} / \mathcal{G}$ are the *same* invariance, manifested at two structural levels:

- **L3 level** (interface specification): rule-type interactions are gauge-invariant
- **Primitive 10 level** (individuation): rule-type counting respects gauge equivalence

These two manifestations are mutually consistent. Inconsistency would have required either L3 enforcing invariance that Primitive 10 fails to respect, or vice versa — neither obtains.

### 4.6 Fal-3 status

**Fal-3 (L3-interface incompatibility with the gauge quotient): NOT triggered.**

The three conditions (L3-Q-1), (L3-Q-2), (L3-Q-3) are all structurally satisfied. The L3 interface admits the gauge-quotient construction without obstruction.

---

## 5. Boundary Between F2 and F3

### 5.1 What Memo 01 (F2) established

- The gauge equivalence relation is well-defined for compact Lie groups $G$ (Memo 01 §5.1).
- The quotient space $\mathcal{A} / \mathcal{G}$ is structurally well-behaved at the local kinematic level (Memo 01 §5.2).
- No primitive forbids non-Abelian extension; four primitives actively support, two are neutral (Memo 01 §3.7).
- The L3 interface admits non-Abelian gauge-invariance constraints, with the Maurer-Cartan structure (Memo 01 §4.5).
- Verdict: **F2 CANDIDATE-FORCED**, R-4 closed.

In short, Memo 01 established the **existence and admissibility** of the non-Abelian gauge structure.

### 5.2 What Memo 02 (F3) must establish

- Whether Primitive 10 individuation operates on $\mathcal{A} / \mathcal{G}$ (Q3-A automatic, or Q3-B via explicit construction).
- Whether the L3 interface is consistent with this individuation (the three (L3-Q-i) conditions of §4).
- Whether physical observables (Q4) are gauge-invariant, supporting the individuation framework.
- Whether the cross-cutting requirements (gauge-invariant phase observables for Primitive 10's threshold) hold structurally.

In short, Memo 02 establishes the **construction and consistency** of the gauge-quotient individuation.

### 5.3 Minimum quotient structure required for downstream Q.3

Q.3 (vertex classification, R-2 completion + R-3) inherits from Memo 02:

- The gauge-quotient $\mathcal{A} / \mathcal{G}$ as a structurally well-defined object.
- Q3-A automatic individuation (or Q3-B explicit construction) as the framework's individuation behaviour.
- The L3 interface's gauge-invariance structure for inheriting into vertex specifications.
- Gauge-invariant observable algebra (Killing-contracted bandwidth, gauge-invariant phase content, etc.) for vertex-level commitment counting.

Q.3 must then specify: how do interaction vertices count as commitment events under gauge equivalence? This is **R-2 completion**. The vertex-level question is genuinely separate from the kinematic-individuation question — vertices involve dynamical content (interactions over time), whereas Q.2 individuation is at fixed time on the participation graph.

---

## 6. Falsifier Analysis (Fal-3, Fal-7)

### 6.1 Fal-3 — L3-interface incompatibility with the quotient

- **Statement.** The L3 interface cannot enforce gauge invariance in a way consistent with the gauge-quotient construction. Either (L3-Q-1) fails (interface depends on choice of representative), or (L3-Q-2) fails (gauge transformation does not commute with interface evaluation), or (L3-Q-3) fails (quotient projection is undefined at the L3 level).

- **Audit (per §4).** All three conditions structurally satisfied. The L3 interface depends on gauge-invariant constructions (field-strength contractions, gauge-covariant combinations of charged-field and gauge-field content); gauge transformations commute with interface evaluation by the standard gauge-covariance structure inherited from R.1; the quotient projection is admitted by (L3-Q-1).

- **Verdict on Fal-3: NOT triggered.**

### 6.2 Fal-7 — Cross-cutting individuation failure

- **Statement.** The gauge-quotient individuation requires content from another substage (vacuum, vertices, or worldline reformulation) for its own definition, creating a cross-substage circular dependency.

- **Audit.**
  - **Vacuum content (Q.8).** Does the gauge-quotient individuation require vacuum-state machinery? The kinematic individuation at fixed time on the participation graph does not invoke vacuum content — the equivalence relation is defined on the configuration space without reference to a vacuum state. Vacuum-state work is Q.8; Q.2 individuation is independent.
  - **Vertex content (Q.3).** Does the gauge-quotient individuation require vertex specifications? No — the kinematic individuation is at fixed time, before any commitment-event vertex structure enters. Vertex-level individuation (R-2 completion) is Q.3, but it inherits *from* Q.2's kinematic individuation, not the reverse.
  - **Worldline reformulation (Q.7).** Does the gauge-quotient individuation require lightlike-worldline machinery? No — kinematic individuation at fixed time does not reference the worldline parametrisation. Q.7 work is for $\tau_g$'s second-quantisation framework, downstream of Q.2.
  - **Phase-observable discipline.** §3.5's noted discipline (Primitive 10's threshold consulting gauge-invariant phase observables) is internal to Q.2 — not a cross-substage dependency. It is a refinement to be confirmed in Memo 03 from Primitive 10's specification.

- **Verdict on Fal-7: NOT triggered.** No cross-substage circular dependency identified.

### 6.3 Cumulative falsifier status for F3

| Falsifier | Status | Where dispatched |
|---|---|---|
| **Fal-1** (U(1) baseline incompat.) | not triggered | Memo 01 background; F1 verifies in Memo 03 |
| **Fal-2** (non-Abelian primitive blocked) | not triggered | Memo 01 §6.1 |
| **Fal-3** (L3-interface incompat.) | **NOT triggered** | §4 + §6.1 |
| **Fal-6** (non-Abelian breaks GRH-1/2/4) | not triggered | Memo 01 §6.3 |
| **Fal-7** (cross-cutting individ. failure) | **NOT triggered** | §6.2 |

**No falsifier is triggered for F3. The framework structurally admits gauge-quotient individuation, with Primitive 10 respecting gauge equivalence automatically (Q3-A) conditional on the gauge-invariant-phase-observable discipline.**

---

## 7. Provisional Verdict for F3

### 7.1 Verdict

**F3: CANDIDATE-FORCED.**

Specifically: **Primitive 10 individuation respects gauge equivalence automatically (Q3-A), because Primitive 10's threshold consults gauge-invariant physical observables (bandwidth content via Killing-form contraction; phase content via gauge-invariant phase combinations) rather than gauge-non-invariant configuration-level content.** The gauge-quotient $[A_\mu] = A_\mu / \mathcal{G}$ is structurally well-defined; the L3 interface admits the quotient construction; physical observables are gauge-invariant by inherited theorem structure (Theorems 10, 11–12, 14); Primitive 10's threshold operates on these gauge-invariant observables and therefore on equivalence classes.

The "FORCED" force is **conditional on** the gauge-invariant-phase-observable discipline — i.e., the discipline that Primitive 10's threshold specification uses gauge-invariant phase content. This discipline is structurally available (gauge-invariant phase observables exist) but is a specification choice for Primitive 10, to be confirmed in Memo 03's audit of Primitive 10's specification.

### 7.2 Justification

The verdict rests on five converging lines of evidence:

- **Primitive-level audit (§3).** No primitive forbids gauge-quotient individuation. Five primitives (P-02, P-04, P-06, P-07, P-10) actively support; one (P-11) is neutral at Q.2. Primitive 10 specifically supports Q3-A conditional on the gauge-invariant-phase-observable discipline.
- **L3 interface compatibility (§4).** All three conditions ((L3-Q-1), (L3-Q-2), (L3-Q-3)) structurally satisfied. The L3 interface admits the quotient construction.
- **Quotient-construction analysis (§5).** The boundary between F2 and F3 is clean: F2 establishes existence and admissibility; F3 establishes construction and consistency. The minimum quotient structure required for Q.3 is supplied.
- **Falsifier status (§6).** Neither Fal-3 nor Fal-7 is triggered. No cross-cutting failures identified.
- **Inheritance from forced theorems.** Theorems 10, 11–12, 14 (Born, U2, U1) all give gauge-invariant content by structural construction; Theorem 16 (U3, Schrödinger evolution) is gauge-covariant and gauge-invariant in physical observables. The framework's foundational theorems already commit to gauge-invariance; F3 inherits this commitment.

### 7.3 Why CANDIDATE-FORCED rather than FORCED

Forcing F3 unconditionally would require Primitive 10's specification to be already on record as using gauge-invariant phase observables. Q.2 has not audited that specification in detail — Memo 03's recommended pre-Memo audit will do so. If the specification is consistent with the gauge-invariant-phase-observable discipline, F3 promotes to FORCED at Memo 03 closure. If not, F3 shifts to Q3-B (explicit gauge-quotient construction needed), which is still admissible but requires additional framework-level machinery.

The honest framing — CANDIDATE-FORCED conditional on a specification audit — is the strongest defensible verdict at this memo's level.

### 7.4 Why not weaker verdicts

- **CANDIDATE-admissible** would understate. Five primitives actively support; no falsifier triggered; the conditional-forcing characterisation is the strongest defensible.
- **SPECULATIVE-admissible** would imply substantial gaps. The work above leaves only the phase-observable discipline as an open audit item — a small refinement, not substantial.
- **REFUTED** would require a primitive-level obstruction. None identified.

### 7.5 Why not FORCED unconditionally

The phase-observable discipline is the gating item. The discipline is structurally available (gauge-invariant phase observables exist as mathematical objects), but Primitive 10's specification of which phase content the threshold consults is a separate question — to be confirmed in Memo 03. CANDIDATE-FORCED captures both the strength of the structural support and the residual specification audit.

---

## 8. Implications for GRH Closure

### 8.1 Effect on GRH-3

GRH-3 (generalised, per Memo 01 §4.4) is now consistent with Primitive 10 individuation at the kinematic level. The L3-enforced gauge invariance and the individuation-threshold operation on $\mathcal{A} / \mathcal{G}$ are structurally compatible (per §4.5).

GRH-3's closure status remains: CANDIDATE-FORCED at the gauge-group-scoping level, conditional on:

- **F3 closure (this Memo)** — ✅ achieved at CANDIDATE-FORCED
- F1 verification (Memo 03)
- F4 honest scoping (Memo 03)
- F5 dependency map (Memo 03)
- Q.3 closure (R-2 completion + R-3 vertex-anchored commitment)
- Q.7 closure (R-1 lightlike worldline + R-5 partial vacuum-field aspect)
- Q.8 closure (R-5 completion)

GRH-3's structural admissibility advances from "CANDIDATE-strong with refinements outstanding" to "CANDIDATE-FORCED at Q.2 level; awaiting Q.3 / Q.7 / Q.8 closures."

### 8.2 R-2 partial closure

**R-2 partial (gauge-quotient individuation at the kinematic level) closes affirmatively at Memo 02.**

R-2 has two stages per the GRH closure roadmap:
- **R-2 partial:** kinematic individuation under gauge equivalence — *closed here, CANDIDATE-FORCED.*
- **R-2 completion:** vertex-level individuation under gauge equivalence — Q.3 deliverable.

R-2's status flag at this point:

- Pre-Memo-02: "CANDIDATE-strong; outstanding"
- Post-Memo-02: "**partial closure: CANDIDATE-FORCED at Q.2 (kinematic level); awaiting Q.3 for vertex-level completion**"

### 8.3 Updated refinement-closure map

| Refinement | Pre-Memo-02 status | Post-Memo-02 status | Closure stage |
|---|---|---|---|
| **R-1** (lightlike worldline) | outstanding | (unchanged) | Q.7 |
| **R-2 partial** (gauge-quotient kinematic) | outstanding | **CLOSED — CANDIDATE-FORCED** | **Q.2 Memo 02 (this)** |
| **R-2 completion** (vertex gauge-quotient) | outstanding | (unchanged) | Q.3 |
| **R-3** (vertex-anchored commitment) | outstanding | (unchanged) | Q.3 |
| **R-4** (non-Abelian extension scoping) | CLOSED (Memo 01) | (unchanged) | Q.2 Memo 01 |
| **R-5 partial** (vacuum-field aspect) | outstanding | (unchanged) | Q.7 |
| **R-5 completion** (zero-point aspect) | outstanding | (unchanged) | Q.8 |

**Two refinements closed (R-4 + R-2 partial); three full refinements + R-2 completion remaining.** Q.2's substantive closure work is complete after Memo 02; Memo 03 will integrate F1 / F4 / F5 and issue the substage verdict.

### 8.4 What remains for Q.3 to complete R-2

Q.3 must address the **vertex-level** gauge-quotient: how do interaction vertices count as commitment events under gauge equivalence?

Specifically, Q.3 deliverables for R-2 completion include:

- **Vertex-counting under gauge equivalence.** A gauge-invariant emission vertex (charged + gauge → charged) must count as one commitment event, not many — even though gauge transformations relate different "configurations" of the vertex.
- **Self-coupling vertex gauge invariance.** The non-Abelian self-coupling vertex ($\tau_g \times \tau_g \to \tau_g$ via $f^{abc}$) must be gauge-invariant in the same sense.
- **Vertex-level Wilson loop / gauge-invariant observable construction.** Q.3 must specify which vertex-level observables are gauge-invariant and therefore Primitive 10-individuation-respecting.

Q.3 inherits from Memo 02:
- The kinematic gauge-quotient $\mathcal{A} / \mathcal{G}$ is well-defined.
- Q3-A automatic individuation is structurally available (modulo the phase-observable discipline confirmed in Memo 03).
- The L3 interface is gauge-invariance-consistent.

These provide Q.3's structural backbone; the vertex-level work builds on top.

---

## 9. Honest Scope Limits

Memo 02 addresses F3 only — *kinematic* gauge-quotient individuation at the fixed-time participation-graph level. The following are explicitly out of scope for this memo:

### 9.1 Deferred to other memos within Q.2

- **F1 (U(1) baseline confirmation).** Bookkeeping verification — Memo 03.
- **F4 (specific-gauge-group deferral, honest scoping).** Memo 03.
- **F5 (downstream dependency map).** Memo 03.
- **Phase-observable discipline audit.** §3.5's noted refinement — confirmed against Primitive 10's specification in Memo 03.

### 9.2 Deferred to Q.3 (R-2 completion)

- **Vertex-level gauge-quotient.** How interaction vertices count as commitment events under gauge equivalence — Q.3 deliverable.
- **Self-coupling vertex content.** Detailed vertex factors for the non-Abelian self-coupling $\tau_g \times \tau_g \to \tau_g$ — Q.3 deliverable.
- **Wilson loop / gauge-invariant observable algebra.** Vertex-level — Q.3 deliverable.

### 9.3 Deferred to other Q substages

- **R-1 (lightlike-worldline reformulation for $A^a_\mu$).** Q.7. Memo 02 confirms admissibility at Q.2 level (P-02 supports locally; global topology Q.7-deferred).
- **R-5 (vacuum-vs-particle status of $\tau_g$).** Q.7 / Q.8. Memo 02 establishes that the kinematic individuation does not require vacuum-state machinery; vacuum-level work is Q.8.
- **Gribov ambiguity (global topological obstruction).** Q.7. Honestly scoped here as out of Q.2 detail.

### 9.4 Outside the GRH closure trajectory entirely

- **Specific gauge group choice** ($SU(3) \times SU(2) \times U(1)$ or any other). Empirical inheritance per Memo 00 §9.
- **Coupling constant values** ($q$, $g_s$, $g_w$). Empirical inheritance via Dimensional Atlas.
- **Charged-rule-type representations** (which fermions transform under which $G$). Empirical / Q.4-onward.
- **Higgs sector / spontaneous symmetry breaking.** Q.4; SPECULATIVE.
- **Generation structure.** Q.6 / empirical.
- **Charge quantization pattern.** Possibly Q.2 partial (later memo) or empirical.

These scope limits are honest structural boundaries. The kinematic gauge-quotient individuation closure does not depend on any of them.

---

## 10. One-Line Summary

> F3 — gauge-quotient individuation at the kinematic level — **closes CANDIDATE-FORCED at Memo 02**: Primitive 10's individuation threshold respects gauge equivalence *automatically* (Q3-A outcome) because the threshold consults gauge-invariant physical observables (Killing-form-contracted bandwidth content, gauge-invariant phase combinations, U2 inner-product values, Born-rule probabilities — all gauge-invariant by inherited theorem structure), with the gauge-quotient $[A_\mu] = A_\mu / \mathcal{G}$ structurally well-defined for compact Lie groups, the L3 interface admitting all three (L3-Q-i) consistency conditions, and no falsifier (Fal-3, Fal-7) triggered — discharging **R-2 partial** at Q.2 level and advancing the GRH closure trajectory; R-2 completion at the vertex level remains as Q.3 deliverable; the conditional-forcing characterisation reflects the residual phase-observable discipline audit (Memo 03) confirming Primitive 10's specification consults gauge-invariant phase content.

---

## Recommended Next Steps

**(a) Begin Q.2 Memo 03 (verdict + cascade).** The natural next deliverable. Memo 03 should: (i) verify F1 (U(1) baseline confirmation, bookkeeping); (ii) execute the phase-observable discipline audit against Primitive 10's specification (the residual gating item from this Memo's verdict); (iii) close F4 (specific-gauge-group deferral, honest scoping with REFUTED on the SM-forcing question); (iv) finalise F5 (downstream dependency map for Q.3 / Q.7 / Q.8); (v) issue the Q.2 substage verdict (anticipated: CLOSED — R-4 closed CANDIDATE-FORCED, R-2 partial closed CANDIDATE-FORCED, GRH closure trajectory advances to Q.3).

**(b) Pre-Memo-03 audit of Primitive 10's specification.** A 30–45 minute read of Primitive 10's specification (`quantum/primitives/10_*.md`) targeting two specific questions: (1) what observables does Primitive 10's threshold consult? (2) are these observables gauge-invariant for $\tau_g$? The answers determine whether F3 promotes from CANDIDATE-FORCED to FORCED at Memo 03, or remains CANDIDATE-FORCED with the discipline as a Q.2 closure caveat.

**(c) Verify the Killing-form-contracted bandwidth observable construction noted in §3.2 + §4.2.** A short derivation (2–3 paragraphs) confirming that $\delta^{ab} b^X_a b^X_b$ is the natural gauge-invariant Killing-form contraction for the four-band content under adjoint action. This is straightforward Lie-algebra mathematics but should be explicitly stated in Memo 03 or as a sub-memo for completeness.

**(d) Defer memory-record update until Q.2 closure (Memo 03).** Per the discipline established in U3 / U4 / U5 arcs and Memo 00 §10. The bundled memory update will capture all of: R-4 closed (CANDIDATE-FORCED at Memo 01), R-2 partial closed (CANDIDATE-FORCED at Memo 02), Q.2 substage verdict, downstream handoffs to Q.3 / Q.7 / Q.8.

**(e) (Optional) Sketch the Q.3 Memo 00 outline now.** With Q.2 substantive work nearly complete (Memos 01–02 closed; Memo 03 integration only), the Q.3 Memo 00 outline can be drafted in skeleton form: vertex-level R-2 completion, R-3 vertex-anchored commitment, Q.3-specific sub-features, falsifier inventory, dependency map. Drafting now would let Q.3 land into a known scope when Q.2 closes; optional but useful for trajectory planning.
