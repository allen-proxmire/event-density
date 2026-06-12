# Phase B — Architectural Specification of the ED Substrate

**Evaluation:** Architectural Distillation of the Event Density *substrate* (discrete relational layer)
**Phase:** B (Architectural Specification)
**AD step:** Step 1 — Identify the Architecture
**Status:** First application of the extended substrate-level AD framework to ED itself
**Date filed:** June 2026
**Author:** Allen Proxmire
**Related:** `Memo_00_ED_Substrate_AD_Scoping.md`; `Phase_A_CriterionMapping.md`; `Phase_A1_SubstrateLevel_AD_Criteria.md`; `Phase_A2_DiscreteExtraction_Modes.md`

---

## 1. Purpose

Phase B **identifies the architecture of the ED substrate**. It corresponds to Step 1 of AD: before any envelope, extremal-dynamics, or constraint-surface extraction can be run, the object of evaluation must be specified cleanly — its primitive commitments, its dynamical law, its interaction structure, and its candidate invariants laid out as a fixed target.

This is the **first phase that applies the extended AD framework to ED itself**. Phase A and its two technical companions (A1, A2) did methodological work: they reformulated AD's six criteria and three extraction modes for the general class of discrete relational architectures, stated independently and in advance of any contact with ED. That work is now fixed. Phase B is the turn from methodology to object. From here forward, the ED substrate is the thing being specified and — in later phases — scored.

Phase B does **not** evaluate. It specifies. No criterion is assessed, no envelope is extracted, no PASS/CONDITIONAL/FAIL verdict is reached. The output of Phase B is a clean architectural specification: a set of **axioms**, **primitives**, **channels**, and **structural commitments** that the subsequent extraction phases (C, D, E) take as their input. A specification error here propagates everywhere downstream, so the work of this phase is to state the architecture exactly as the foundational corpus gives it, with no smoothing and no anticipation of the verdict.

The discipline of the scoping memo carries forward unchanged: the substrate is a candidate architecture. Phase B describes it; it does not defend it.

---

## 2. Substrate Axioms (Structural Commitments)

The ED substrate is specified by the following primitive commitments. Each is stated cleanly and independently — as a structural commitment the architecture makes, not as a derived consequence. Together they constitute the axiom layer that Step 1 of AD requires.

**Axiom B1 — Events as atomic units.**
The substrate's fundamental constituents are discrete **micro-events**: atomic acts of becoming. There is no sub-event structure; the micro-event is indivisible. The local production rate of micro-events is the *event density*. Nothing in the substrate is continuous at this layer — the continuum appears only as a coarse-grained shadow, never as a primitive.

**Axiom B2 — Channels (participation relations).**
Micro-events stand in **participation relations** to one another: one micro-event integrates another's becoming. Participation is carried along **channels** — stable subgraphs of the participation structure — each bearing an edge weight (bandwidth) that bounds how much becoming can be integrated across it. Participation, not position, is the substrate's primitive relation; spatial and geometric notions are downstream of it.

**Axiom B3 — Adjacency and chain formation.**
Two micro-events are **adjacent** when they share participation bandwidth and maintain coherent relational timing. A sequence of adjacent micro-events that maintains coherent participation forms a **chain**. Chains are the substrate-level objects that coarse-grain to particles. Adjacency is local and bandwidth-gated: it is not a global relation imposed on the graph but a condition that holds or fails between specific micro-events.

**Axiom B4 — Commitment density.**
Micro-events, once they occur, are **committed**. The local accumulation of committed micro-events is the **commitment density** ρ. Commitment density is the substrate-level state variable: the quantity whose local value, strain, and gradient enter the evolution rule. It is an accumulation, not a flow — it records what has become, not what is becoming.

**Axiom B5 — Orientation field.**
The channel structure carries a relational **orientation** — a directionality in how participation is integrated along chains and across the participation graph. Orientation is the substrate-level analogue of the conserved directional structure the continuum theory expresses geometrically. It is a structural feature of the channel layer, carried by the architecture rather than by any individual micro-event.

**Axiom B6 — Decoupling surfaces (finite reach).**
Participation has **finite reach**. At a **decoupling surface**, reciprocal participation between two regions becomes one-sided: beyond the surface, influence does not return. Reach is bounded not by convention but by the architecture — every region of the substrate has a horizon past which reciprocal participation ends. Finite reach is a positive structural commitment, not an absence of one.

**Axiom B7 — P11 irreversibility (forward-only evolution).**
Every commitment event is **irreversible**: once made, never unmade (commitment irreversibility, P11). Evolution is forward-only. The substrate carries a built-in arrow at the level of its primitives — not as an emergent statistical tendency but as an axiom of how commitment works. There is no operation in the architecture that uncommits a committed micro-event.

These seven commitments are the architecture's axiom layer. Axioms B1–B3 specify *what exists* (events, channels, chains); B4–B5 specify *the state and its structure* (commitment density, orientation); B6–B7 specify *the boundaries of evolution* (finite reach, irreversibility). The evolution rule (§3) acts on this layer; it is not part of it.

---

## 3. Evolution Rule

The substrate's dynamical law is an explicit, discrete, local update. A chain at a given substrate position selects its next propagation step by **maximizing a stability score** Σ over the candidate next states:

> **Σ(e′) = Coh(e′, s) − Str(e′, ρ_local) − Grad(e′, ∇ρ)**

The chain extends to the candidate state e′ of **maximum Σ**. This is the substrate's evolution equation — the discrete analogue of a continuum dynamical law, but stated as a local selection rule rather than a differential equation.

**Inputs to Σ.** Three terms, each local:

- **Coh(e′, s)** — *coherence*: how well the candidate state e′ coheres with the current chain state s. A coherence-increasing step scores higher. This is the constructive term — the one Σ rewards.
- **Str(e′, ρ_local)** — *strain*: the participation strain the candidate state incurs against the local commitment density ρ_local. Subtracted: strain against the local environment penalizes a candidate.
- **Grad(e′, ∇ρ)** — *gradient strain*: the strain the candidate incurs against the surrounding commitment-density gradient ∇ρ. Subtracted: a step that fights the local gradient structure is penalized.

The score is a single signed scalar per candidate: coherence earned, minus the two strain costs. The architecture commits the step that maximizes it.

**Locality radius.** Every input to Σ is drawn from a bounded neighborhood of the chain's current position. Coh reads the current chain state; Str reads the local commitment density; Grad reads the local density gradient. There is no term in Σ that reads a non-local or global quantity. The update is **graph-local with finite reach**: the locality radius is the bandwidth-gated participation neighborhood, and decoupling surfaces (Axiom B6) bound it from outside. The rule cannot consult any micro-event past a decoupling horizon, because reciprocal participation does not reach there.

**Tie-breaking.** The rule as stated selects the *maximum-Σ* candidate. Where two or more candidates share the maximal score, the architecture requires a tie-breaking commitment to remain deterministic forward (the determinism criterion of Phase A1 distinguishes *forward determinism* from *unique local maximizer*, and ties are exactly where these can come apart). The specification flags tie-breaking as a structural slot the architecture must fill — whether by orientation (Axiom B5) supplying a canonical direction, by bandwidth ordering on the channels (Axiom B2), or by an explicit rule in the corpus. **Phase B records this as an open specification point**; resolving whether the unique-maximizer condition holds, and by what mechanism, is work for the envelope and constraint-surface phases (C, E). It is named here, not settled here.

This section defines the substrate's dynamical law. Sections §4 and §5 decompose the structure the law acts on.

---

## 4. Channel Decomposition

AD Step 1 requires the **interaction structure** to be decomposed into independent channels. The substrate's interaction structure is the participation graph; its channels are the distinguishable pathways along which participation, strain, and orientation propagate. The three terms of Σ map onto three dynamical channels, with the orientation and reach structure supplying two further channels of a different character.

For each channel: its **locality class** (all are graph-local; the question is reach), its **linearity**, its **stability role** (does it stabilize, destabilize, or remain neutral under the update), and its **scale action** (the scale at which it acts — local, meso, or global).

| Channel | Source | Locality class | Linearity | Stability role | Scale action |
|---|---|---|---|---|---|
| **Coherence** | Coh term in Σ | Graph-local, finite reach | Nonlinear (coherence-gated) | **Stabilizing** — rewards coherent continuation; drives chains toward locally consistent states | Local |
| **Strain** | Str term in Σ | Graph-local, finite reach | Nonlinear (strain against ρ_local) | **Destabilizing** — penalizes high-density continuation; opposes over-commitment | Local |
| **Gradient strain** | Grad term in Σ | Graph-local, finite reach | Nonlinear (strain against ∇ρ) | **Destabilizing / steering** — opposes steps fighting the density gradient; couples the local step to the meso-scale density field | Meso |
| **Orientation** | Axiom B5 (orientation field) | Graph-local, propagated along chains | Approximately linear (carried, not generated locally) | **Neutral / structuring** — does not add or remove stability score but constrains the direction of admissible propagation; candidate tie-breaker | Meso–global |
| **Decoupling / reach** | Axiom B6 (decoupling surfaces) | Graph-local boundary, finite reach | Nonlinear (threshold) | **Bounding** — neither stabilizing nor destabilizing the score; sets the boundary past which no channel reaches | Local boundary → global partition |

**Reading of the table.** The three Σ-channels are the dynamically active ones — coherence pulling toward consistency, the two strain channels pushing back against over-commitment and against fighting the gradient. Their balance is what the maximization resolves at each step. The orientation and decoupling channels are *structural* rather than score-bearing: orientation shapes which directions are admissible and is the leading tie-break candidate; decoupling sets the finite-reach boundary that bounds every other channel's locality. No channel in the substrate is globally-acting in the continuum sense — even orientation and decoupling, which have global *consequences* (a partition of the substrate, a coherent directional structure), act through strictly local mechanisms. This is the channel-level signature of finite reach, and it is exactly the feature Phase A1 reformulated locality to honor.

The independence claim — that these are genuinely separable channels and not redundant restatements of one another — is a **minimality** question, assessed in Phase F, not asserted here. Phase B records the decomposition; it does not yet certify it is irredundant.

---

## 5. Candidate Invariants

AD Step 1 closes by identifying the **candidate invariants** — the quantities or structural features the architecture may conserve or enforce under the update rule, which the later phases test. These are *candidates*: Phase B lists them; Phases C (envelope) and E (constraint surface) determine whether each genuinely holds.

**I1 — Orientation conservation.**
The relational orientation carried by the channel structure (Axiom B5) is a candidate conserved quantity. The claim to be tested: orientation is propagated along chains and across channels without spontaneous reversal, so that the substrate carries a coherent directional structure that the update rule preserves. This is the discrete analogue of the conserved directional quantities AD looks for at the envelope level.

**I2 — Finite reach (decoupling surfaces).**
Finite reach (Axiom B6) is a candidate *structural* invariant: the claim that no propagation, under any sequence of updates, crosses a decoupling surface to re-establish reciprocal participation. If it holds, finite reach is not merely an initial condition but a property preserved by the dynamics — once decoupled, regions stay decoupled. This is the seat of the **reach-bounded determination** introduced in Phase A1 and the **reach-stratified surface** introduced in Phase A2.

**I3 — Forward-only evolution.**
P11 irreversibility (Axiom B7) is a candidate invariant of the dynamics: the claim that no update sequence uncommits a committed micro-event, so the substrate's arrow is preserved at every step. Forward-only evolution is asserted at the axiom level; the invariant claim is that the update rule never violates it — that maximizing Σ never requires undoing a prior commitment.

**I4 — Commitment-density monotonicity.**
Commitment density ρ (Axiom B4) is a candidate **monotone** quantity: the claim that local committed-event count is non-decreasing under the update, since commitments accumulate and never reverse (a consequence the I3 arrow would underwrite). Monotonicity is the substrate's candidate envelope-level inequality — the discrete analogue of a continuum monotone functional, and a primary target for Phase C's Mode 1 envelope extraction.

**I5 — Local-maximization footprint.**
The selection rule (§3) stamps every reachable state with a **local-optimality signature**: every committed step was, at the moment of commitment, the maximum-Σ candidate in its neighborhood. The candidate invariant is that this footprint is *recoverable* — that any state the substrate produces carries the trace of having been locally maximal. This is the **maximization footprint** introduced in Phase A2's Mode 1, here named as an ED-substrate candidate for the first time. It is the structural feature most specific to a selection-driven substrate and has no continuum analogue.

These five are the candidates for the envelope (Phase C) and constraint-surface (Phase E) analyses. I1–I3 are conservation/structural claims; I4 is a monotonicity claim; I5 is an optimality-trace claim. None is assumed to hold. Each is a hypothesis the extraction phases test against the axioms and the update rule.

---

## 6. Architectural Summary Table

| Axiom | Description | Role | Notes |
|---|---|---|---|
| **B1** Events as atomic units | Indivisible micro-events; their local rate is the event density | Primitive constituent | No sub-event structure; continuum is a shadow, never a primitive |
| **B2** Channels (participation relations) | Stable subgraphs carrying participation bandwidth | Primitive relation / interaction structure | Participation, not position, is primitive; geometry is downstream |
| **B3** Adjacency and chain formation | Bandwidth-gated coherent adjacency; chains of adjacent events | Primitive composition | Chains coarse-grain to particles; adjacency is local, not global |
| **B4** Commitment density | Local accumulation ρ of committed micro-events | State variable | Inputs Str and Grad in Σ; an accumulation, not a flow |
| **B5** Orientation field | Relational directionality carried by channel structure | Structural field | Candidate conserved quantity (I1); candidate tie-breaker |
| **B6** Decoupling surfaces (finite reach) | Horizon where reciprocal participation goes one-sided | Reach boundary | Positive commitment, not an absence; bounds every channel's locality |
| **B7** P11 irreversibility | Every commitment irreversible; forward-only evolution | Arrow / evolution boundary | Axiom-level arrow, not emergent statistics |
| **Σ rule** Evolution rule | Σ = Coh − Str − Grad, maximized over local candidates | Dynamical law | Graph-local, finite reach; tie-breaking flagged as open spec point |

The axiom layer (B1–B7) plus the evolution rule constitute the complete Step-1 architectural specification. Channels (§4) decompose the interaction structure of B2; candidate invariants (§5) are the hypotheses the specification offers to the extraction phases.

---

## 7. Next Actions

Phase B completes **Step 1 of AD** (Identify the Architecture). The ED substrate is now specified as a fixed target: seven axioms, one evolution rule, five channels, five candidate invariants, with one open specification point (tie-breaking, §3) recorded for resolution downstream.

**Phase C begins Step 2 of AD.** It performs **Mode 1 — Envelope Extraction**, using the *discrete Mode 1* defined in Phase A2: it derives the forbidden and necessary substrate configurations (forbidden/necessary graph patterns), the reachability bounds set by finite reach, and the envelope constraints implied by the axioms and the update rule alone — including the first tests of the monotonicity candidate (I4) and the maximization-footprint candidate (I5). The envelope is the admissible-and-reachable region; Phase C extracts it.

The specification is fixed. The extraction begins.

---

*End of Phase B. This phase specifies the ED substrate's architecture as the input to AD's extraction phases; it does not evaluate it. The envelope extraction begins at Phase C.*
