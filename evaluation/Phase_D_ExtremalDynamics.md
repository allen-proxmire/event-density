# Phase D — Extremal Dynamics (Discrete Mode 2)

**Evaluation:** Architectural Distillation of the Event Density *substrate* (discrete relational layer)
**Phase:** D (Extremal Dynamics)
**AD step:** Step 3 — Mode 2 (Extremal Dynamics)
**Status:** Second extraction phase; resolves two deferrals from Phase C
**Date filed:** June 2026
**Author:** Allen Proxmire
**Related:** `Phase_B_ArchitecturalSpecification.md`; `Phase_C_EnvelopeExtraction.md`; `Phase_A2_DiscreteExtraction_Modes.md` (discrete Mode 2 machinery, attractor taxonomy)

---

## 1. Purpose

Phase D applies the **discrete Mode 2 — Extremal Dynamics** machinery from Phase A2 to the ED substrate. Where Mode 1 (Phase C) extracted the *static* envelope — what configurations can and must occur — Mode 2 extracts the *dynamical* behavior: what the substrate does at the extremes of its evolution, where it drives, and where it settles.

The goal is to identify:

- **Propagation fronts** — the structure of the reach-bounded front from Phase C's N3, now treated as a moving object;
- **Concentration and extinction behaviors** — where commitment density concentrates, where channels collapse, where orientation stabilizes or collapses;
- **Score-transition loci** — where Σ changes sign or relative candidate ordering, and whether these loci correlate with decoupling surfaces;
- **Attractor types** — fixed points, cycles, quasi-stable patterns, classified by the A2 attractor taxonomy;
- **Orientation-gap resolution** — whether the dynamics enforce, break, or leave open the orientation conservation question flagged in Phase C (F4/I1). This is the largest open question carried forward;
- **Footprint recoverability** — whether the maximization footprint (present on every reachable state by N1) is *recoverable* from late-time states, or only present.

Phase D extracts dynamical structure as evidence; it does not render criteria verdicts (Phase F). Two Phase C deferrals are explicitly resolved here: footprint recoverability (§7) and the orientation gap's disposition (§8).

---

## 2. Inputs

Phase D uses **only** the Phase B specification, the Phase C extraction results, and the general discrete Mode 2 machinery from Phase A2. Inputs:

- **Axioms B1–B7** and the **evolution rule** Σ = Coh − Str − Grad (maximized, graph-local, finite reach, tie-breaking open).
- **Channel table** — coherence (stabilizing), strain (destabilizing), gradient strain (destabilizing/steering), orientation (structuring/neutral), decoupling (bounding).
- **Candidate invariants I1–I5**, with **I4 now established** (promoted to invariant by Phase C N2) and **I1 still open** (orientation conservation not yet grounded).
- **Phase C forbidden/necessary patterns** — F1–F5 (F4 open), N1–N4.
- **Envelope inequalities** — E-I4 (ρ monotone, sharp), E-I5 (footprint, sharp by construction), E-I2 (reach, boundary-sharp/interior-loose).
- **Reachability structure** — finite causal cone; **causal-cone factorization** (regions across decoupling surfaces are causally independent; reachable set factorizes along decoupling boundaries).

The A2 Mode 2 result most relevant here: **a bounded substrate necessarily reaches a fixed point or a cycle** (pigeonhole on a finite state space). This governs §6.

---

## 3. Propagation Fronts

Phase C established the propagation front as a *structural necessity* (N3): influence propagates as a reach-bounded front that cannot cross a decoupling surface. Phase D treats that front as a dynamical object and characterizes its motion.

**Front speed — bounded by reach, set by bandwidth.** A chain extends one adjacency step per update (B3 + rule locality). The front therefore advances at a bounded rate: at most one participation-graph edge per update step, and never past a decoupling surface (E-I2). This is the discrete analogue of a finite, bounded propagation speed — but it is *not* a fixed constant. The local advance rate is gated by channel bandwidth (B2): a high-bandwidth channel admits adjacency steps that a low-bandwidth channel does not. The front speed is therefore **bounded above by reach and modulated below by local bandwidth** — finite everywhere, constant nowhere.

**Front shape — graph-local, gradient-steered.** The front's local shape is set by which candidates maximize Σ. The gradient-strain channel (Grad) steers the front: it penalizes steps fighting ∇ρ, so the front preferentially advances down coherent-extension directions and resists advancing into high-gradient regions. The front shape is thus **graph-local and gradient-conformant** — it follows the participation-graph geometry, biased by the local density gradient. No global term shapes it.

**Front behavior — sharpening, not diffusing.** This is the key §3 finding. The continuum PDE shadow is *parabolic* (degenerate-parabolic), and parabolic equations diffuse — fronts smooth out. But the substrate front is driven by **maximization**, not averaging. At each step the front commits the single maximum-Σ candidate, not a weighted blend. Maximization is sharpening: it selects an extreme, not a mean. So the substrate front **sharpens** (or, where coherence and strain balance exactly, remains neutral); it does **not** diffuse. *This is a substrate-vs-shadow distinction worth recording:* the diffusive character of the PDE is an artifact of coarse-graining (averaging over many maximization steps), not a property of the substrate dynamics. The substrate is locally sharpening; the shadow is diffusive. Both can be true because coarse-graining a sharpening selection rule over many steps and many chains produces an averaged, diffusive law.

**Fronts and orientation.** The front carries orientation (B5) along its advance. Whether it *preserves* orientation under advance is exactly the open I1 question — deferred to §8. Recorded here: the front transports orientation; whether it conserves it is unresolved at the front level.

---

## 4. Concentration and Extinction Behaviors

Mode 2 asks where the dynamics drive density and structure to extremes.

**Commitment-density concentration.** ρ concentrates where coherence is repeatedly rewarded against low strain — regions where the coherence channel dominates the two strain channels. By E-I4, ρ is monotone non-decreasing everywhere; concentration is the *relative* phenomenon of some positions accumulating commitments faster than others. The gradient-strain channel **opposes** runaway concentration: as ρ concentrates, ∇ρ steepens, and Grad penalizes further commitment fighting that gradient. **Concentration is therefore self-limiting** — a forced consequence of the channel structure, not an imposed bound. There is no mechanism for unbounded local blow-up; the destabilizing channels cap it.

**Channel extinction and collapse.** A channel extinguishes when no candidate along it achieves positive net Σ — coherence can no longer overcome strain. The chain ceases to extend along that channel (it does not reverse — P11/F1 forbids that; it simply stops). Extinction is **terminal and local**: an extinguished channel is a chain that has reached a position with no positive-Σ continuation. This is one of the two attractor mechanisms (§6): extinction produces a fixed point.

**Orientation collapse vs. stabilization.** Orientation can, in principle, either *stabilize* (the channel structure settles into a coherent directional pattern that persists) or *collapse* (directional structure is lost — neighboring chains carry inconsistent orientation). The axioms do not yet force either outcome (the open I1 question). Mode 2 can say *when* each would occur: orientation stabilizes where the front advances coherently into a consistent neighborhood; orientation is at risk of collapse where fronts from causally independent cones (across a decoupling surface) meet and carry inconsistent orientation. **Decoupling-surface junctions are the candidate sites of orientation collapse** — flagged for §8.

**Interaction with monotonicity (E-I4).** Crucially, none of these behaviors violates E-I4. Concentration is monotone-ρ accumulation; extinction halts accumulation (the equality case of E-I4, ρ constant at a quiescent position); orientation behavior is orthogonal to ρ (orientation is a channel-layer field, not a function of commitment count). The monotonicity inequality is **compatible with all three extremal behaviors** — it bounds ρ from below regardless of whether the local dynamics concentrate, extinguish, or reorient. This consistency is a positive check: the Phase C envelope inequality survives contact with the Mode 2 extremes.

---

## 5. Score-Transition Loci

A score-transition locus is a position where Σ changes sign (positive net stability becomes negative, or vice versa) or where the *relative ordering* of candidate steps changes (a previously sub-maximal candidate becomes maximal).

**Sign transitions create sharp boundaries.** Where net Σ crosses zero, the front's behavior changes qualitatively: positive-Σ regions admit continuation, zero/negative-Σ regions extinguish. The Σ = 0 locus is therefore a **sharp boundary** between extending and extinguished substrate — not a gradual transition, because the maximization rule acts on the sign discretely (extend iff a positive-Σ candidate exists). These boundaries are the dynamical signature of extinction (§4) and are *sharp by the same mechanism that makes fronts sharpen* (§3): maximization is a discrete selector.

**Transitions correlate with decoupling surfaces — partially.** Two distinct loci must not be conflated:

- **Decoupling surfaces (B6)** are *participation-reach* boundaries: where reciprocal participation goes one-sided. Set by the architecture's reach structure.
- **Σ-transition loci** are *score-sign* boundaries: where net stability crosses zero. Set by the local coherence–strain balance.

These **need not coincide**, but they correlate: approaching a decoupling surface, reciprocal participation weakens, coherence support drops, and net Σ tends toward zero — so Σ-transitions *cluster near* decoupling surfaces without being identical to them. The finding: **decoupling surfaces are reach boundaries; Σ-transitions are dynamical boundaries; they correlate but are distinct objects.** Phase E (constraint surface) will need both, kept separate.

**Transitions and the orientation gap.** Do Σ-transitions resolve or worsen the orientation gap? Σ is a function of Coh, Str, Grad — none of which is an orientation term (the orientation channel was classified *neutral / structuring*, contributing no stability score). **Σ-transitions are therefore orientation-blind.** They neither enforce nor break orientation conservation; the score dynamics simply do not see orientation. This is a sharpening of the gap: it tells us the *score* machinery cannot close the orientation question, because orientation is outside Σ. Whatever resolves the gap must come from the channel structure (B2/B5), not the evolution rule. This routes the §8 analysis decisively.

---

## 6. Attractor Structure

Applying the A2 Mode 2 attractor taxonomy. The governing A2 result: **a bounded substrate necessarily reaches a fixed point or a cycle.** ED's substrate is bounded within any single causal cone (finite reach, E-I2), so within a cone the result applies directly.

**Fixed points — present, and the dominant attractor.** A fixed point is a configuration where no chain has a positive-Σ continuation: every front has extinguished (§4). By P11/F1, no committed state can be undone, so once every channel extinguishes the configuration is frozen — a **local-maximization fixed point**. These are the substrate's primary attractors. They are *terminal*: the monotone-ρ + irreversibility structure means the substrate runs *toward* extinction-frozen states and stays there. Every causal cone, evolved to completion, reaches such a fixed point.

**Cycles — structurally excluded within a cone.** A cycle requires the configuration to *return* to a prior state. But E-I4 makes ρ monotone non-decreasing, and a genuine cycle would require ρ to return to an earlier (lower-or-equal) value at some position — which F1 forbids. **Monotonicity + irreversibility together forbid cycles within a causal cone.** This is a clean, important result: the substrate is **acyclic by construction.** The A2 "fixed point *or* cycle" dichotomy collapses, for this substrate, to *fixed point only*. (The pigeonhole argument still applies to the finite state space; monotonicity is what excludes the cycle branch of its conclusion.)

*Caveat — reach-induced quasi-cycles across cones.* While a single cone is acyclic, the orientation field at decoupling-surface junctions (§4) could in principle produce *quasi-periodic* patterns in the directional structure across cones, without any ρ returning. These are not true cycles (no state recurs) and depend on the unresolved orientation behavior. Recorded as a **conditional, open** possibility, contingent on §8.

**Quasi-stable patterns — present as long-relaxation transients.** Between active propagation and the terminal fixed point, the substrate passes through quasi-stable configurations: fronts that advance very slowly because coherence and strain nearly balance (Σ ≈ 0 but slightly positive). These are not attractors proper but **long-lived transients** on the approach to a fixed point — the discrete analogue of slow relaxation. They are *quasi-stable*, not stable: monotonicity guarantees they eventually resolve to a fixed point; they cannot persist forever.

**Attractor classification summary.** The substrate's attractors are:

- **Local-maximization fixed points** — *yes, dominant and terminal* (§6 primary result);
- **Reach-induced cycles** — *no within a cone* (excluded by E-I4 + F1); *quasi-periodic cross-cone patterns conditionally possible*, pending orientation;
- **Orientation-stabilized vs. orientation-ambiguous** — the fixed points are stabilized in ρ and footprint but **orientation-ambiguous**: nothing in the attractor structure forces a unique orientation at the fixed point. This is the orientation gap reappearing at the attractor level, and it sets up §8.

---

## 7. Recoverability of the Maximization Footprint

Phase C established (N1) that every reachable state *carries* the footprint — every committed step was maximum-Σ at commitment. Phase C deferred the sharper question: is that footprint **recoverable** from a late-time state — can one infer the Σ-maximization history from the frozen attractor?

**The three options (A2 framing):** present-but-unrecoverable (the footprint is destroyed by subsequent evolution), partially recoverable (some maximization information survives), fully recoverable (the entire selection history is reconstructable from the final state).

**Assessment: partially recoverable.** The reasoning:

- **What is recoverable.** Because evolution is forward-only (P11/F1) and ρ is monotone (E-I4), the final state *preserves every commitment ever made* — nothing is overwritten or erased. The committed structure of a fixed point is the *cumulative record* of the whole history. In particular, the *set* of committed micro-events and their commitment-density profile are fully present at late time. The fact that each was maximal-Σ at commitment (N1) is therefore *attached* to a state that still exists.

- **What is lost.** What is *not* directly recoverable is the **order** and the **counterfactual margin**. The final state records *that* each step was maximal but not, in general, *by how much* it beat the runner-up candidate (the Σ margin), nor the *sequence* in which causally-independent commitments across different cones were made (causal-cone factorization makes cross-cone order physically meaningless, but even within a cone, two commitments at incomparable positions leave no order trace). The selection *margins* are not stored; only the *outcomes* are.

- **The tie-breaking residue.** Where ties occurred (the open spec point from Phase B), the late-time state cannot reveal which tie-break was taken vs. merely that *a* maximal candidate was committed. Unresolved tie-breaking thus directly limits recoverability.

**Conclusion.** The footprint is **partially recoverable**: the *committed outcomes* and *that-each-was-maximal* are fully present (forced by irreversibility + monotonicity); the *margins, fine-grained order, and tie resolutions* are not stored and are lost. In A2 terms: the substrate preserves the **extensive** footprint (what was selected) but not the **intensive** footprint (how decisively, in what order). What can be inferred from a late-time state: the full set of commitments, their density profile, and the certification that each respected the maximization rule — a strong but not complete reconstruction.

*This is a favorable result for the substrate's legibility:* irreversibility, often a limitation, here works *for* recoverability — because nothing is erased, the cumulative record survives. The losses (margin, order) are exactly the information a maximization rule does not need to retain.

---

## 8. Orientation-Gap Resolution

The largest open question from Phase C: do the dynamics **enforce** orientation conservation (closing the gap), **break** it (opening it), or **leave it unresolved** (handing it to Phase E)?

**The §5 result routes this decisively.** Σ-transitions are *orientation-blind*: orientation contributes no stability score (neutral/structuring channel), so the maximization rule does not see orientation. **The evolution rule cannot enforce orientation conservation, because the quantity is outside its objective function.** This rules out "the dynamics enforce it" as stated: nothing in Σ-maximization pushes toward orientation conservation.

**Does the rule then *break* it?** Also no — for the same reason. A rule blind to orientation neither conserves nor violates it; it transports whatever orientation the channel structure carries (§3) without acting on it. The dynamics are *orientation-passive*.

**So the disposition is: unresolved by the dynamics — and now we know precisely why.** The orientation gap is **not closeable at the Mode 2 level**, because orientation conservation, if it holds, must be a property of the **channel/participation structure (B2, B5)** — the substrate's interaction geometry — not of the evolution rule. Phase D's contribution is to *locate* the gap correctly:

- It is **not** a dynamical-law question (the rule is orientation-blind — §5).
- It is **not** an envelope question (Phase C correctly found the axioms under-specify it).
- It **is** a constraint-surface question: whether the *channel structure itself* admits, forbids, or forces consistent orientation across adjacent channels and across decoupling-surface junctions (the candidate collapse sites, §4).

**Verdict (neutral): the dynamics leave the orientation gap unresolved, and hand it to Phase E — with a sharpened specification.** Phase E (Mode 3, constraint surface) must determine whether orientation conservation is a structural property of the channel space — i.e., whether the participation graph's channel geometry admits orientation-reversed configurations as faces of the constraint surface, or excludes them. Phase D has converted "is orientation conserved?" from an open question into a *located* one: it lives in the channel constraint surface, not in the dynamics. That is the most useful thing Mode 2 can do with it.

**Stakes recorded for Phase E/F.** If Phase E finds the channel structure forces orientation consistency, I1 becomes an established invariant, F4 becomes genuinely forbidden, and the envelope closes fully. If Phase E finds the channel structure *admits* orientation reversal, then orientation conservation is an *additional axiom* the substrate would need (not derivable from B1–B7 + rule), and that is a CONDITIONAL-flavored finding for Phase F — a real, honest gap in the architecture as specified.

---

## 9. Summary Table

| Feature | Behavior | Origin | Notes |
|---|---|---|---|
| **Propagation front speed** | Bounded by reach, modulated by bandwidth; finite, not constant | N3, B6, B2 | Discrete bounded propagation; no fixed speed |
| **Front shape** | Graph-local, gradient-steered | Grad channel | Follows participation geometry, biased by ∇ρ |
| **Front character** | **Sharpening (or neutral), not diffusing** | Maximization rule | Substrate sharpens; PDE shadow diffuses (coarse-graining artifact) |
| **Concentration** | Self-limiting | Grad channel vs. coherence | ∇ρ steepens → Grad caps blow-up; no unbounded concentration |
| **Extinction** | Terminal, local; halts (never reverses) | F1/P11, Σ ≤ 0 | Produces fixed points |
| **Orientation (concentration/extinction)** | Stabilizes coherently; collapse-risk at decoupling junctions | B5, open I1 | Junctions flagged as collapse sites → §8 |
| **Σ-transition loci** | Sharp sign boundaries | Maximization (discrete selector) | Sharp like fronts; same mechanism |
| **Σ-transitions vs. decoupling surfaces** | Correlate but distinct | B6 vs. Σ-sign | Reach boundary ≠ dynamical boundary; both needed in Phase E |
| **Σ-transitions vs. orientation** | **Orientation-blind** | Orientation outside Σ | Routes §8: rule cannot close the gap |
| **Fixed points** | **Present, dominant, terminal** | Local-max + F1 | Primary attractor |
| **Cycles** | **Excluded within a cone** | E-I4 + F1 (acyclic) | A2 dichotomy collapses to fixed-point-only |
| **Quasi-stable patterns** | Long-relaxation transients | Σ ≈ 0⁺ | Resolve to fixed points eventually |
| **Footprint recoverability** | **Partially recoverable** | F1 + E-I4 preserve record | Outcomes recoverable; margins/order/ties lost |
| **Orientation gap** | **Unresolved by dynamics; located in channel structure** | §5 orientation-blindness | Handed to Phase E with sharpened spec |

---

## 10. Next Actions

Phase D completes **Step 3 of AD** (Mode 2 — Extremal Dynamics). Results: propagation fronts are reach-bounded, bandwidth-modulated, and **sharpening** (distinguishing the substrate from its diffusive PDE shadow); concentration is self-limiting; the substrate is **acyclic** (cycles excluded by monotonicity + irreversibility), with **local-maximization fixed points as the dominant, terminal attractor**; the maximization footprint is **partially recoverable** (outcomes preserved by irreversibility, margins/order/ties lost); and the orientation gap is **unresolved by the dynamics but now precisely located** — it is a channel-structure question, not a dynamical-law one, because the evolution rule is orientation-blind.

**Phase E begins Step 4 of AD.** It constructs the substrate's **constraint surface** using the discrete Mode 3 from Phase A2: the channel space of the participation graph, its structural / dynamical / reach-bounded faces, and closure (no ghost faces, no unreachable admissible regions). Phase E inherits two sharpened tasks from Phase D:

1. **Resolve the orientation gap** at the channel-structure level — determine whether the channel constraint surface forbids, admits, or forces orientation-reversed configurations (closing or formally opening I1/F4).
2. **Use the distinct reach vs. Σ-transition boundaries** (§5) as two separate constraint-surface features — reach-stratified faces (decoupling surfaces) and dynamical faces (Σ-sign boundaries).

The extremal dynamics are extracted. The constraint surface begins.

---

*End of Phase D. This phase extracts the ED substrate's Mode 2 extremal dynamics as evidence; it does not render criteria verdicts (Phase F). The constraint-surface construction begins at Phase E.*
