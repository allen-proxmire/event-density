# Memo-00 — ED Substrate AD Review: Scoping

**Evaluation:** Architectural Distillation of the Event Density *substrate* (discrete relational layer)
**Memo:** 00 (scoping)
**Status:** Phase A entry
**Date filed:** June 2026
**Author:** Allen Proxmire
**Related:** `evaluations/AD_Evaluation_EventDensity.md` (the prior evaluation, of the *PDE shadow*); `AD_Note_SubstrateBeneathTheShadow.md` (the note that motivates this review)

---

## 1. Purpose

This memo scopes an Architectural Distillation (AD) review of the **Event Density substrate** — the discrete relational layer of micro-events, participation, and channels from which the rest of the framework is generated.

Three things this review is **not**:

- **Not a re-run of the existing ED evaluation.** AD has already evaluated Event Density once (catalog entry #15). That evaluation took as its object the *coarse-grained parabolic PDE* — the continuum law the substrate produces when averaged over many chain steps. It assessed the **shadow**, not the substrate that casts it. This review takes the substrate itself as its object.
- **Not a fresh application of settled machinery.** AD's six criteria, three-mode extraction, and pole taxonomy were developed for and tested on continuum dynamical systems — PDEs. Applying them to a discrete relational substrate is not a routine application; it is the first time AD has been pointed at an object of this kind.
- **Not a foregone conclusion.** This memo does not assume the substrate will pass, conditionally pass, or fail any criterion. It scopes the work and identifies what the work requires. The verdict is the output of the evaluation, not an input to the scoping.

What this review *is*: the first attempt to apply AD to a **discrete relational substrate** rather than a continuum law. Its goal is to determine which AD criteria and steps transfer cleanly, which require reformulation, and which expose structural features that AD's current machinery does not yet capture — finite reach, decoupling surfaces, forward-only evolution, and a determinability boundary.

This is Phase A. It clarifies the work before any of it is done.

---

## 2. Object of analysis

The object is the ED substrate as specified in the foundational corpus (notably *One Substrate, Three Domains* and the ED-substrate foundations papers). For AD's purposes it decomposes into three layers, matching AD's standard input requirements (axioms, evolution rule, interaction structure).

### 2.1 Substrate primitives (axiom-level)

- **Micro-events** — discrete acts of becoming; the substrate's fundamental constituents. The local production rate is the event density.
- **Participation and adjacency** — micro-events integrate one another's becoming; two are adjacent when they share participation bandwidth and maintain coherent relational timing.
- **Channels** — stable subgraphs along which micro-events propagate, carrying edge weights (bandwidth).
- **Chains** — sequences of micro-events maintaining coherent participation; the substrate-level objects that coarse-grain to particles.
- **Commitment density** — the local accumulation of committed micro-events.
- **Decoupling surfaces** — participation thresholds where reciprocal participation between two regions becomes one-sided.
- **Commitment irreversibility (P11)** — every commitment event is irreversible; once made, never unmade.

### 2.2 Substrate update rule (evolution-level)

A chain at a substrate position evaluates its next propagation step by maximizing a **stability score**:

> Σ(e′) = Coh(e′, s) − Str(e′, ρ_local) − Grad(e′, ∇ρ)

where Coh measures coherence with the current state, Str the participation strain against the local environment, and Grad the strain against the surrounding gradient. The chain extends to the next state of maximum Σ. This is an explicit, discrete, local update rule — the substrate's "evolution equation."

### 2.3 Substrate invariants (candidate structural features)

These are the features the review must hold in view from the start, because they are where AD's continuum-developed criteria are most likely to strain:

- **Locality** — the update at a position depends on the local state, local strain, and local gradient.
- **Finite reach** — influence is bounded by decoupling surfaces; reciprocal participation ends at a horizon.
- **Forward-only evolution** — P11 makes the update irreversible; the substrate has a built-in arrow.
- **Discrete curvature / orientation structure** — the relational geometry of the participation graph (the substrate-level analogue of the geometric features the continuum theory expresses as curvature and orientation).
- **Orientation conservation** — the conserved relational orientation carried by the channel structure (the discrete analogue of the conserved quantities AD looks for at the envelope level).

These are listed as *candidate* invariants. Whether each is genuinely conserved/structural under the update rule is a question for the evaluation, not an assumption of the scoping.

---

## 3. The central methodological question

The whole Phase A question is one sentence:

> **Do AD's six criteria — minimality, locality, determinism, generative sufficiency, envelope tightness, structural optimality — translate to a discrete relational substrate, and if not, which require reformulation?**

AD's criteria were stated for continuum systems. Several are framed in continuum language and may or may not survive contact with a discrete substrate:

- **Locality** is currently "evolution at a point depends only on local state and derivatives." The substrate has no derivatives in the continuum sense — it has local strain and local gradient terms in the stability score. Does locality restate cleanly, or does it need a graph-local reformulation?
- **Determinism** is currently well-posedness: existence, uniqueness, continuous dependence. The substrate's update is deterministic *forward* (maximize Σ) but irreversible (P11) and finite-reach (decoupling surfaces). Continuum well-posedness carries a flavor of time-reversibility and unbounded propagation that the substrate explicitly lacks. This is the criterion most likely to require reformulation, and the most informative if it does.
- **Envelope tightness** and **structural optimality** are framed against continuum constraint surfaces and inequalities. What is the *constraint surface* of a participation graph? What does a *tight envelope* mean for a discrete update rule? These need definition before they can be assessed.
- **Minimality** and **generative sufficiency** are the most domain-agnostic of the six and may transfer with little change — minimality (no redundant primitive/channel) and generative sufficiency (the substrate produces all its target structures) are already close to substrate-native.

**This memo does not prejudge any of these.** Each is an open question for Phase A to resolve. The output of Phase A is a *mapping* — criterion by criterion — not a verdict.

---

## 4. Deliverables of Phase A (scoping)

Phase A produces four things:

1. **A criterion mapping.** For each of AD's six criteria, a substrate-level equivalent: either a clean restatement (the criterion transfers as-is), a reformulation (the criterion needs new wording for a discrete substrate), or a flag (the criterion does not translate and a substitute is required).

2. **A step applicability table.** For each of AD's six process steps (Step 1 architecture spec, Step 2 envelope, Step 3 extremal dynamics, Step 4 constraint surface, Step 5 validate, Step 6 generalize), a determination of whether the step applies directly, applies with adaptation, or requires methodological extension before it can be run.

3. **A substrate-feature accommodation list.** The structural features AD must accommodate that the PDE evaluation never encountered: finite reach, decoupling surfaces, commitment irreversibility, and the discrete update rule. For each, a note on which AD criterion or step it stresses, and what accommodation it demands.

4. **A proceed/extend decision.** The Phase A verdict: either (a) the criteria and steps translate cleanly enough to proceed directly to a full AD evaluation (Phases B–G as a standard run), or (b) one or more criteria require reformulation first, in which case Phase A's mapping becomes a proposed *extension* of AD methodology, and the full evaluation runs against the extended criteria.

The deliverable is the decision plus its supporting mapping. Phase A does not run the evaluation; it determines what running it requires.

---

## 5. Boundaries

To keep the scoping disciplined:

- **This memo does not perform the AD evaluation.** No criterion is assessed here. No PASS/CONDITIONAL/FAIL verdict is reached. Phase A scopes; later phases evaluate.
- **This memo identifies methodological requirements only.** Where a criterion is flagged as needing reformulation, the memo names the need; it does not yet write the reformulation. That is Phase A's deliverable work, downstream of this scoping statement.
- **Neutrality is mandatory.** The review must not assume the substrate will pass or fail any criterion. The substrate is a candidate architecture; AD returns PASS, CONDITIONAL, or FAIL on evidence. A CONDITIONAL or FAIL on some criterion is a *more* valuable result than a clean PASS, because it demonstrates that the criteria have teeth and were not tuned to the system under test.

### The circularity guard

One discipline is load-bearing and is stated here explicitly so it governs every later phase.

AD was *extracted from* the Factor Skyline. The motivation for extending AD downward to the substrate level comes from the FS↔ED architectural parallel (the determinability-boundary note). There is therefore a self-reference risk: using a framework built in part from one project (FS) to evaluate a sibling project (ED), where the extension itself was motivated by their parallel.

The guard is the one AD already builds in: **any substrate-level criteria must be stated independently and in full before they are applied to the substrate.** Criteria are written first, as general statements about discrete relational architectures; the substrate is evaluated against them second; the verdict falls where the evidence puts it. A substrate that passes criteria reverse-engineered to make it pass tells us nothing. The value of the review depends entirely on the criteria being fixed before the object is scored against them.

---

## 6. Motivation

Three reasons this review is worth doing now.

**It is the downward extension the note proposed.** `AD_Note_SubstrateBeneathTheShadow.md` argued that AD currently evaluates shadow-side architectures (continuum laws), while two of the systems in its orbit — ED and FS — are each the continuum shadow of a discrete finite-reach substrate. The note proposed that AD's scope could extend to the substrate level. This review is that proposal made concrete: the ED substrate is the first worked example of a substrate-level AD evaluation.

**It is the structural counterpart to the determinability-boundary measurement.** The note's open task is to quantify ED's determinability boundary in bits, as FS has done for the parity barrier. That is the *quantitative* side. This review is the *structural* side: locating where AD's criteria — particularly locality and determinism — meet the substrate's finite reach and decoupling surfaces. The two efforts reinforce each other; the structural account tells the measurement where to look, and the measurement gives the structural account a number.

**The substrate is the deepest object in ED.** Every continuum face of the framework — the quantum structures, the gravitational structures, the parabolic PDE — is a projection of the substrate. AD has evaluated one face. Evaluating the substrate itself clarifies the architecture of the entire theory: it tests whether the well-builtness AD found in the PDE shadow is inherited from a well-built substrate, or is a property the coarse-graining introduces. Either answer is informative about the framework as a whole.

---

## 7. Recommended next-step plan

The review proceeds in seven phases, mirroring AD's six-step process with a scoping phase in front.

| Phase | Work | AD step |
|---|---|---|
| **A** | **Scoping** (this memo): criterion mapping, step applicability, feature accommodation, proceed/extend decision | — |
| **B** | **Architectural Specification**: enumerate substrate axioms, the update rule as evolution law, channels as interaction structure, candidate invariants | Step 1 |
| **C** | **Envelope extraction**: forbidden/necessary substrate configurations, envelope constraints, structural invariants derived from the primitives alone | Step 2 (Mode 1) |
| **D** | **Extremal dynamics**: propagation/reach behavior, irreversibility consequences, stability of the update rule, finite-reach front structure | Step 3 (Mode 2) |
| **E** | **Constraint surface**: channel/participation interaction structure, impossible and forced combinations, the substrate's constraint geometry | Step 4 (Mode 3) |
| **F** | **Criteria evaluation**: the six criteria (as mapped in Phase A) assessed against the substrate; PASS/CONDITIONAL/FAIL with evidence; constraint census | Step 5 |
| **G** | **Generalization and taxonomy extension**: whether the substrate constitutes a new pole or a cross-domain invariant; integration with the determinability-boundary note and the FS parallel | Step 6 |

**Immediate next action:** execute Phase A — produce the criterion mapping, the step applicability table, the feature accommodation list, and the proceed/extend decision. Phase A's output determines whether Phases B–G run as a standard AD evaluation or as an evaluation against extended substrate-level criteria.

Phase A does not assume which. It finds out.

---

*End of Memo-00. This memo scopes the AD review of the ED substrate; it does not perform it. The evaluation begins at Phase A.*
