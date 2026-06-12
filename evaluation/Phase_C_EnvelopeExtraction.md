# Phase C — Envelope Extraction (Discrete Mode 1)

**Evaluation:** Architectural Distillation of the Event Density *substrate* (discrete relational layer)
**Phase:** C (Envelope Extraction)
**AD step:** Step 2 — Mode 1 (Envelope)
**Status:** First extraction phase; first substantive findings about the ED substrate
**Date filed:** June 2026
**Author:** Allen Proxmire
**Related:** `Phase_B_ArchitecturalSpecification.md` (inputs); `Phase_A2_DiscreteExtraction_Modes.md` (discrete Mode 1 machinery); `Phase_A1_SubstrateLevel_AD_Criteria.md` (envelope-tightness criterion, ghost states)

---

## 1. Purpose

Phase C applies the **discrete Mode 1 — Envelope Extraction** defined in Phase A2 to the ED substrate specified in Phase B. This is the first phase that produces substantive findings about ED rather than methodology or specification.

The envelope, in discrete Mode 1, is the set of substrate configurations that are both **admissible** (not excluded by the axioms or the update rule) and **reachable** (produced by some sequence of updates from an admissible start). Extracting it means identifying:

- **Forbidden graph patterns** — configurations that cannot occur under the axioms or the update rule;
- **Necessary graph patterns** — configurations that must occur under the update rule;
- **Envelope inequalities** — the quantitative bounds the axioms and invariants impose on reachable states;
- **Reachability constraints** — how finite reach restricts which admissible states are actually reachable;
- **Envelope closure status** — whether the admissible region and the reachable region coincide (closed), nearly coincide (partially open), or diverge (open), with explicit identification of any **ghost states** (admissible but unreachable).

Phase C extracts; it does not yet evaluate against the criteria. The PASS/CONDITIONAL/FAIL judgments on envelope tightness belong to Phase F. Phase C produces the envelope's structure as evidence for that later judgment, stated neutrally.

---

## 2. Inputs

Phase C uses **only** the Phase B specification and the general discrete Mode 1 machinery from Phase A2. Nothing is imported from the continuum theory, the PDE evaluation, or the FS parallel. The inputs are:

- **Axioms B1–B7** — events as atomic units (B1); channels / participation relations (B2); adjacency and chain formation (B3); commitment density ρ (B4); orientation field (B5); decoupling surfaces / finite reach (B6); P11 irreversibility (B7).
- **Evolution rule** — Σ(e′) = Coh(e′, s) − Str(e′, ρ_local) − Grad(e′, ∇ρ), with the chain extending to the maximum-Σ candidate; graph-local with finite reach; tie-breaking flagged open.
- **Channel table** — five channels: coherence (stabilizing), strain (destabilizing), gradient strain (destabilizing/steering), orientation (structuring/neutral), decoupling (bounding).
- **Candidate invariants I1–I5** — orientation conservation (I1); finite reach (I2); forward-only evolution (I3); commitment-density monotonicity (I4); local-maximization footprint (I5).

The discipline of the scoping memo applies: the candidate invariants are *hypotheses*, not premises. Phase C tests whether each is enforced by the axioms and rule. Where an invariant is forced, it generates necessary patterns and envelope inequalities; where it is merely consistent but not forced, that gap is itself a finding.

---

## 3. Forbidden Graph Patterns

A pattern is **structurally forbidden** if the axioms exclude it outright (no update rule can produce it because the configuration is not even admissible). It is **dynamically forbidden** if it is admissible as a static configuration but cannot be *reached* — the update rule never produces it from an admissible start.

**F1 — Commitment reversal (uncommitment).**
*Pattern:* a configuration in which a previously committed micro-event is absent in a later state along the same chain — commitment density ρ decreasing at a position over update steps.
*Why forbidden:* P11 (B7) makes every commitment irreversible; no operation in the architecture uncommits. A monotone-decreasing ρ at a position is excluded at the axiom level.
*Classification:* **structurally forbidden** (axiom B7).

**F2 — Reciprocal participation across a decoupling surface.**
*Pattern:* two regions separated by a decoupling surface that nonetheless maintain *two-sided* participation — influence returning across the surface.
*Why forbidden:* B6 defines a decoupling surface precisely as the locus where reciprocal participation becomes one-sided. Two-sided participation across it contradicts the definition of the surface.
*Classification:* **structurally forbidden** (axiom B6).

**F3 — Broken chain continuity (orphan adjacency jump).**
*Pattern:* a chain that extends to a next state not adjacent (in the B3 sense) to its current state — a propagation step crossing a non-adjacent gap, i.e., between micro-events that share no participation bandwidth or fail coherent relational timing.
*Why forbidden:* B3 defines chain formation as a sequence of *adjacent* micro-events; the evolution rule (§3) selects the next state from the *local* candidate neighborhood. A jump to a non-adjacent state is outside the candidate set the rule ranges over.
*Classification:* **structurally forbidden** (axiom B3 + rule locality). Note: this is forbidden by the *intersection* of an axiom and the rule's candidate-set definition; it is recorded as structural because the candidate set is fixed by B3.

**F4 — Spontaneous orientation reversal.**
*Pattern:* a chain whose carried orientation (B5) reverses between adjacent states with no structural cause in the channel layer.
*Why forbidden — conditionally:* if orientation conservation (I1) is enforced by the architecture, spontaneous reversal is forbidden. **But B5 specifies orientation as carried by the channel structure without yet specifying a rule that prohibits reversal.** This pattern is therefore forbidden *only if* I1 is a genuine invariant.
*Classification:* **dynamically forbidden — pending I1**. This is a flagged gap: the axioms assert orientation exists and is carried, but Phase B did not establish a conservation law for it. Whether F4 is forbidden is **open** until orientation conservation is either derived from the rule or added as an axiom. *Recorded as the first envelope-level gap.*

**F5 — Committed state that was not locally maximal (footprint violation).**
*Pattern:* a committed step that was, at the moment of commitment, *not* the maximum-Σ candidate in its neighborhood.
*Why forbidden:* the evolution rule commits the maximum-Σ candidate by construction. A committed non-maximal step contradicts the rule directly.
*Classification:* **dynamically forbidden** (evolution rule). *Caveat:* in a tie, multiple candidates share the maximal Σ; a committed tied candidate is still maximal, so F5 is unaffected by the open tie-breaking point. F5 forbids only *sub*-maximal commitments.

**Reading of §3.** Three of the five forbidden patterns are clean and axiom- or rule-grounded (F1, F2, F5; with F3 structural via the candidate-set definition). One — F4 — is **not yet forbidden**, because the architecture asserts orientation without a conservation rule. This is the most informative finding of the section: the envelope has an identified soft edge at orientation, and Phase C names it rather than assuming I1 closes it.

---

## 4. Necessary Graph Patterns

A pattern is a **structural necessity** if the axioms force it in every admissible configuration. It is a **dynamical necessity** if the update rule forces it in every reachable configuration.

**N1 — Local-maximization footprint on every committed step.**
*Pattern:* every committed step carries the stamp of having been the maximum-Σ candidate in its neighborhood at commitment time (the I5 footprint).
*Why forced:* the evolution rule commits the maximum-Σ candidate by construction (the direct converse of F5). Every reachable state is therefore a concatenation of locally-maximal commitments.
*Classification:* **dynamical necessity** (evolution rule). This establishes I5's footprint as *present* on every reachable state; whether it is *recoverable* (invertible back to the selection that produced it) is a sharper question deferred to the constraint-surface phase (E).

**N2 — Monotone commitment-density ordering along chains.**
*Pattern:* along any chain, commitment density ρ at each position is non-decreasing over update steps — committed events accumulate, producing a monotone ordering of states by ρ.
*Why forced:* F1 forbids ρ-decrease (P11/B7); commitments accumulate as the chain extends. The combination forces non-decreasing ρ. This is I4 (monotonicity) established as a genuine invariant, not merely a candidate.
*Classification:* **dynamical necessity** (axiom B7 via F1). *This promotes I4 from candidate to forced* — a key Phase C result, since I4 is the substrate's candidate envelope inequality (see §5).

**N3 — Reach-bounded propagation front.**
*Pattern:* propagation from any micro-event reaches only within the finite-reach neighborhood bounded by decoupling surfaces; a chain's influence has a front that cannot cross a decoupling horizon (B6).
*Why forced:* the rule reads only local candidates and decoupling surfaces bound reciprocal participation (B6). Influence therefore propagates as a bounded front, never instantaneously or globally.
*Classification:* **structural necessity** (axiom B6 + rule locality). This is the discrete analogue of a finite propagation speed — forced by the architecture, not assumed.

**N4 — Coherence–strain balance at every commitment.**
*Pattern:* every committed step reflects a resolved balance between the stabilizing coherence channel and the two destabilizing strain channels — Σ maximal means coherence gained net of strain costs.
*Why forced:* Σ = Coh − Str − Grad maximized means no admissible candidate offered a better coherence-minus-strain tradeoff. Every reachable state encodes this balance locally.
*Classification:* **dynamical necessity** (evolution rule). N4 is the channel-level content of N1: the footprint is specifically a *coherence-minus-strain-optimal* footprint.

**Reading of §4.** N1–N4 are all forced and cleanly grounded. The most consequential is **N2**: it converts the monotonicity candidate I4 into an established invariant, which directly supplies the envelope inequality E-I4 below. N3 establishes finite propagation as structural. Unlike §3, this section has no flagged gap — the necessary patterns are robust. The asymmetry is itself informative: the architecture *forces* its accumulation and locality structure cleanly, while leaving its *orientation* structure (F4) under-specified.

---

## 5. Envelope Inequalities

The forced patterns of §4 yield quantitative bounds on reachable states. An inequality is **sharp** if reachable states attain it (the bound is tight); **loose** if a gap remains between the bound and what the dynamics actually reach.

**E-I4 — Commitment-density monotonicity.**
*Formal:* for any chain position x and update steps t₁ < t₂: **ρ(x, t₂) ≥ ρ(x, t₁)**.
*Origin:* invariant I4, forced by N2 (axiom B7 via F1).
*Sharpness:* **sharp at the lower bound.** Equality holds exactly when no new commitment occurs at x between t₁ and t₂ (a quiescent position). Both the equality case and the strict-increase case are reachable, so the bound is attained — sharp.

**E-I5 — Local-maximization footprint bound.**
*Formal:* for any committed step e′ in neighborhood 𝒩: **Σ(e′) ≥ Σ(c) for all admissible candidates c ∈ 𝒩**.
*Origin:* invariant I5, forced by N1 (evolution rule).
*Sharpness:* **sharp by construction.** The committed step is the maximizer, so equality with itself is trivial and the inequality against all other candidates is exactly what the rule enforces. The bound is the rule. *Note:* this makes E-I5 sharp but not independently informative as a *constraint* — it restates the rule. Its value is structural (it certifies the footprint), not as a slack-bounding inequality.

**E-I2 — Finite-reach bound.**
*Formal:* for any micro-event e and any event e″ influenced by e: **d_participation(e, e″) ≤ R_decouple(e)**, where d_participation is graph distance in the participation structure and R_decouple(e) is the reach to e's nearest decoupling surface.
*Origin:* invariant I2, forced by N3 (axiom B6).
*Sharpness:* **sharp at the boundary, loose in the interior.** The bound is attained by chains that propagate all the way to a decoupling surface (sharp there); chains that decohere or extinguish before reaching the surface leave interior slack (loose there). The envelope therefore has a *tight outer boundary* (reach) but *interior slack* (not every within-reach state is reached). This split sharpness is the key quantitative finding of §5.

**Reading of §5.** Two of three inequalities are sharp (E-I4 at its lower bound; E-I5 by construction). The third, E-I2, is sharp on its boundary but loose in its interior — and that interior looseness is exactly where the closure question (§7) lives: the existence of within-reach-but-unreached states is the candidate ghost-state region.

---

## 6. Reachability Constraints

**The finite-reach causal cone.** For a micro-event e, define its **forward causal cone** as the set of micro-events reachable by some chain propagating from e without crossing a decoupling surface. By N3 and E-I2, this cone is bounded: its radius is R_decouple(e), the participation-graph distance to e's nearest decoupling horizon. The cone is the discrete analogue of a forward light cone, with decoupling surfaces playing the role of a causal boundary — but unlike a relativistic cone, its boundary is set by the *participation architecture*, not by a fixed propagation speed, and can vary from event to event.

**How reach restricts the envelope.** Reachability is the binding constraint that distinguishes the envelope from the merely-admissible set. A configuration can satisfy every axiom (be admissible) yet require, to be reached, an influence path that crosses a decoupling surface — which N3/F2 forbid. Such a configuration is admissible but **unreachable**: a ghost-state candidate. Finite reach therefore does real work in tightening the envelope: it removes from the reachable set every admissible configuration whose construction would demand trans-decoupling influence.

**Reach-induced patterns.**

- *Reach-induced forbidden pattern:* any configuration requiring a single chain to influence two regions on opposite sides of a decoupling surface it lies behind. Admissible as a static picture; unreachable dynamically (a refinement of F2 at the configuration level).
- *Reach-induced necessary pattern:* every reachable configuration decomposes into causal cones — regions separated by decoupling surfaces are causally independent, so the reachable set factorizes along decoupling boundaries. This **factorization** is forced (N3) and is a structural property the constraint-surface phase (E) will use directly.

The reachability constraint is thus *productive*: it both forbids (trans-decoupling configurations) and forces (causal-cone factorization). It is the substrate-level mechanism by which finite reach shapes the envelope, and it is precisely the feature continuum Mode 1 has no analogue for.

---

## 7. Envelope Closure Assessment

The closure question: does the **reachable** region coincide with the **admissible** region? Three verdicts are possible — fully closed (they coincide), partially open (some admissible states unreachable, but the gap is structurally characterized), or open (large, uncharacterized slack).

**Assessment by region:**

- **The ρ-monotonicity face is closed.** Every admissible monotone-ρ history is reachable (E-I4 is sharp at both equality and strict-increase). No ghost states here.
- **The footprint face is closed.** Every reachable state carries the maximization footprint by construction (N1/E-I5); there are no admissible-but-footprint-free reachable states, because reachability *is* the footprint. No ghost states here.
- **The reach face is partially open.** E-I2 is sharp on its boundary but loose in its interior. There exist admissible within-reach configurations that no update sequence produces — specifically, configurations requiring trans-decoupling influence (forbidden by N3) and configurations that are within-reach but only constructible through a non-maximal step (forbidden by F5/N1). These are **ghost states**: admissible as static configurations, unreachable under the dynamics.

**Ghost states identified.** Two classes:

1. **Trans-decoupling ghosts** — admissible configurations whose construction requires influence across a decoupling surface. Structurally characterized: they are exactly the configurations violating causal-cone factorization (§6). *Cleanly bounded.*
2. **Non-maximal-path ghosts** — admissible configurations reachable only via a step that was sub-maximal in Σ at commitment. Forbidden by the rule (F5). *Cleanly bounded.*

Both ghost classes are **structurally characterized**, not residual slack — the architecture says exactly why each is unreachable.

**The orientation gap.** Separately, F4 (spontaneous orientation reversal) remains *neither forbidden nor forced*: the architecture under-specifies whether orientation-reversed configurations are admissible. This is **not** a ghost state (ghosts are admissible-but-unreachable; orientation-reversed states have undetermined admissibility). It is an **open admissibility question** — a different kind of gap, recorded distinctly.

**Closure verdict (neutral).** The envelope is **partially open, with fully characterized openness**: the reachable region is strictly smaller than the admissible region, but every gap is structurally explained — two ghost-state classes, both cleanly bounded by the axioms/rule, plus one open admissibility question (orientation) that is *under-specification*, not slack. There is **no large uncharacterized slack**. In Phase A1's envelope-tightness vocabulary, the substrate has *no uncharacterized ghost states* but *one unresolved admissibility boundary*. This is recorded as evidence for Phase F; it is not yet a verdict on the envelope-tightness criterion.

---

## 8. Summary Table

| Pattern / Inequality | Type | Origin | Status | Notes |
|---|---|---|---|---|
| **F1** Commitment reversal | Structurally forbidden | Axiom B7 (P11) | Forbidden | Clean; underwrites N2/E-I4 |
| **F2** Trans-decoupling reciprocity | Structurally forbidden | Axiom B6 | Forbidden | Defines the reach boundary |
| **F3** Broken chain continuity | Structurally forbidden | Axiom B3 + rule locality | Forbidden | Outside the candidate set |
| **F4** Spontaneous orientation reversal | Dynamically forbidden — *pending I1* | B5 (no conservation rule yet) | **Open** | Soft edge; I1 not yet established |
| **F5** Sub-maximal commitment | Dynamically forbidden | Evolution rule | Forbidden | Unaffected by tie-breaking |
| **N1** Maximization footprint | Dynamical necessity | Evolution rule | Necessary | Establishes I5 present (recoverability → Phase E) |
| **N2** Monotone ρ ordering | Dynamical necessity | B7 via F1 | Necessary | **Promotes I4 candidate → invariant** |
| **N3** Reach-bounded front | Structural necessity | B6 + rule locality | Necessary | Discrete finite propagation |
| **N4** Coherence–strain balance | Dynamical necessity | Evolution rule | Necessary | Channel content of N1 |
| **E-I4** ρ(x,t₂) ≥ ρ(x,t₁) | Envelope inequality | I4 via N2 | Sharp | Attained at equality and strict increase |
| **E-I5** Σ(e′) ≥ Σ(c) ∀c∈𝒩 | Envelope inequality | I5 via N1 | Sharp (by construction) | Restates rule; structural not slack-bounding |
| **E-I2** d_part(e,e″) ≤ R_decouple(e) | Envelope inequality | I2 via N3 | Sharp boundary / loose interior | Interior looseness = ghost-state region |
| **Closure** | Envelope status | §7 | Partially open, characterized | 2 ghost classes (bounded) + 1 open admissibility (orientation) |

---

## 9. Next Actions

Phase C completes **Step 2 of AD** (Mode 1 — Envelope). The envelope of the ED substrate is extracted: five forbidden patterns (four clean, one open at orientation), four necessary patterns (all clean, one promoting I4 to an established invariant), three envelope inequalities (two sharp, one boundary-sharp/interior-loose), a characterized reachability structure (finite causal cone with forced factorization), and a closure verdict of **partially open with fully characterized openness** — no uncharacterized slack, two bounded ghost-state classes, one open orientation-admissibility question carried forward.

**Phase D begins Step 3 of AD.** It applies the **discrete Mode 2 — Extremal Dynamics** defined in Phase A2: propagation fronts (the reach horizon of N3 as a dynamical front), concentration and extinction behavior, score-transition loci, and the attractor structure of the update rule (the A2 result that bounded substrates necessarily reach a fixed point or cycle). Phase D will also take up two items Phase C deferred: the *recoverability* of the maximization footprint (sharpening N1), and whether the orientation gap (F4) is resolved by the dynamics or remains open into the constraint-surface phase.

The envelope is extracted. The extremal dynamics begin.

---

*End of Phase C. This phase extracts the ED substrate's Mode 1 envelope as evidence; it does not render the envelope-tightness verdict, which is Phase F. The extremal-dynamics extraction begins at Phase D.*
