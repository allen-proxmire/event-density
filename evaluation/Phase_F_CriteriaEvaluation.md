# Phase F — Criteria Evaluation (Substrate-Level AD Criteria)

**Evaluation:** Architectural Distillation of the Event Density *substrate* (discrete relational layer)
**Phase:** F (Criteria Evaluation)
**AD step:** Step 5 — Validate Against Criteria
**Status:** The verdict phase; first and only phase that renders PASS / CONDITIONAL / FAIL
**Date filed:** June 2026
**Author:** Allen Proxmire
**Related:** `Phase_A1_SubstrateLevel_AD_Criteria.md` (criteria definitions — sole source); `Phase_B`–`Phase_E` (evidence); `Phase_TieBreak_Specification.md` (closes the Determinism CONDITIONAL — see upgrade note, §5 and §10)

> **Upgrade note (post-filing):** This phase returned **5 PASS / 1 CONDITIONAL** for the architecture *as then specified* (tie-breaking slot open, per Phase B §3). `Phase_TieBreak_Specification.md` subsequently filled that slot using only existing B1/B2 structure, closing Determinism's unique-maximizer component. **The current score is 6 PASS / 0 CONDITIONAL / 0 FAIL.** The original CONDITIONAL analysis below is retained unchanged — it is correct for the as-then-specified architecture and preserves the evaluation history. See §5 and §10 for the upgrade.

---

## 1. Purpose

Phase F evaluates the ED substrate against the **six substrate-level AD criteria** reformulated in Phase A1: minimality, locality, determinism, generative sufficiency, envelope tightness, structural optimality.

This is the **first and only phase that renders verdicts.** Phases B through E produced evidence and explicitly withheld judgment; every one of them ended by stating that the criteria verdicts belong to Phase F. Phase F now renders them. Each verdict is **PASS**, **CONDITIONAL**, or **FAIL**, and each must be **evidence-based** — grounded in specific results from Phases B–E, cited by phase. No verdict is asserted without the evidence that compels it.

The discipline from the scoping memo governs the whole phase: a CONDITIONAL or FAIL on some criterion is a **more** valuable result than a clean sweep, because it demonstrates the criteria have teeth and were not tuned to pass the system under test. Phase F does not aim for six passes. It aims for the verdict the evidence supports, criterion by criterion. Where the evidence is clean, it passes; where the evidence shows a genuine, specific gap, it reports a CONDITIONAL and names what would close it.

The circularity guard holds to the end: the criteria were fixed in Phase A1, stated for the general class of discrete relational architectures, before any contact with ED's evidence. Phase F applies those fixed criteria to the evidence; it does not adjust the criteria to fit the result.

---

## 2. Inputs

Phase F draws evidence from all prior phases and criteria definitions **exclusively** from Phase A1.

**Evidence (Phases B–E):**

- **Axioms B1–B7** and **evolution rule** Σ = Coh − Str − Grad (Phase B), with the **tie-breaking slot left open** (Phase B §3).
- **Channel table** — five channels, split into score-bearing (Coh, Str, Grad) and structural (orientation, decoupling) subspaces (Phase B, Phase E §3).
- **Candidate invariants I1–I5**, with their Phase B–E dispositions: **I4 established** (monotonicity forced, C-N2); **I2/I3 forced**; **I5 present, partially recoverable** (D §7); **I1 stratified** (E §7).
- **Envelope results (Phase C)** — F1–F5 (F4 resolved in E), N1–N4, inequalities E-I4/E-I5/E-I2, causal-cone factorization, two characterized ghost-state classes.
- **Extremal dynamics (Phase D)** — sharpening (non-diffusing) fronts, self-limiting concentration, **acyclic** dynamics with local-maximization fixed points as sole attractor, partial footprint recoverability, orientation-blind score dynamics.
- **Constraint surface (Phase E)** — four structural + four dynamical faces, **determinability boundary located at the decoupling surface**, **orientation STRATIFIED** (local invariant, derived not added), **closure: closed in the characterized sense**, surface type stability-resolved + reach-stratified + commitment-dissipative + locally graph-contractive.

**Criteria (Phase A1, sole source):** minimality, locality (graph-local, finite-reach), determinism (four components: forward determinism, stable dependence, reach-bounded determination, unique local maximizer), generative sufficiency, envelope tightness (forbidden excluded + necessary forced + no uncharacterized ghost states + decidable), structural optimality.

---

## 3. Criterion 1 — Minimality

**Criterion (A1):** no primitive, channel, or rule-term is redundant — none is derivable from or reducible to the others; the architecture carries no surplus structure.

**Evaluation.**

- *Axiom redundancy.* The seven axioms are mutually independent commitments. None is derivable from the others: events (B1), the participation relation (B2), adjacency/chains (B3), commitment density (B4), orientation (B5), decoupling (B6), and irreversibility (B7) each introduce structure the others do not supply. A positive minimality signal: **monotonicity is *not* an axiom** — it was *derived* (I4, forced by C-N2 from B7 + accumulation). The architecture did not double-count a forced consequence as a primitive. Likewise orientation *conservation* is not an axiom — it was derived as a stratified invariant (E §7). The axiom set states commitments and lets consequences fall out.
- *Channel redundancy.* Phase B flagged channel independence as a minimality question for this phase. Phase E §3 settles it: the three score-bearing channels (Coh, Str, Grad) make distinct contributions to Σ (reward, local penalty, gradient penalty) and do not reduce to one another; the two structural channels (orientation, decoupling) are independent of the score subspace and of each other (one carries direction, one bounds reach). No channel is redundant.
- *Rule-term redundancy.* Σ = Coh − Str − Grad has three terms doing three distinct jobs. Dropping any one changes the selection: without Coh there is no reward signal, without Str no local-density penalty, without Grad no gradient steering (Phase D §3–4 show Grad is what makes concentration self-limiting — it is not cosmetic). No term is surplus.

*One observation, recorded but not penalizing.* Orientation (B5) is the one axiom whose work is entirely **structural** — it bears no Σ score (Phase E §3). Its justification is that it carries the directional structure the architecture needs (and that coarse-grains to geometric features in the shadow), not that it participates in the dynamics. This is a *non-dynamical* axiom, not a *redundant* one: it does work no other axiom does. Minimality concerns redundancy, not dynamical participation, so this does not reduce the verdict — but it is the architecture's one axiom whose motivation is structural rather than rule-level, and it is noted for Phase G.

**Verdict: PASS.** No redundant axiom, channel, or rule-term; forced consequences (monotonicity, stratified orientation) are derived rather than posited, which is affirmative evidence of minimality.

---

## 4. Criterion 2 — Locality

**Criterion (A1):** the update is *direct, graph-local, and finite-reach* — it depends only on a bounded participation neighborhood; finite reach counts **toward** locality (decoupling surfaces are honored, not a defect).

**Evaluation.**

- *Graph-locality of updates.* Every input to Σ is drawn from a bounded participation neighborhood: Coh reads the current chain state, Str the local ρ, Grad the local ∇ρ (Phase B §3). No term reads a non-local or global quantity. The update is graph-local by construction.
- *Finite reach respected.* Decoupling surfaces (B6) bound the neighborhood from outside; the rule cannot consult any micro-event past a decoupling horizon (Phase B §3, N3, E-I2). Finite reach is not a limitation grafted onto a non-local rule — it is intrinsic. Under A1's reformulation, this counts *toward* locality: ED is finite-reach by axiom, the cleanest possible satisfaction of the reformulated criterion.
- *No non-local influence.* Phase E confirmed it directly: no channel — score-bearing or structural — reaches across a decoupling surface (causal-cone factorization, §6). The reachable set factorizes along reach boundaries, which is only possible if influence is strictly local-and-bounded. No non-local influence appears anywhere in the architecture.

**Verdict: PASS.** This is the criterion ED satisfies most characteristically: the substrate is graph-local and finite-reach by axiom, and finite reach — far from straining locality — *is* the reformulated locality criterion's central case. The reach-stratified constraint surface (Phase E §6) is the structural proof that locality holds globally.

---

## 5. Criterion 3 — Determinism

**Criterion (A1):** four components, each evaluated separately — (1) forward determinism, (2) stable dependence, (3) reach-bounded determination, (4) unique local maximizer.

**Component 1 — Forward determinism.** The rule selects the next state by maximizing Σ over local candidates; given a state and its neighborhood, the forward step is determined (no backward requirement is imposed — A1 explicitly does not demand reversibility). P11 (B7) supplies the forward arrow. **Component 1: PASS.**

**Component 2 — Stable dependence.** A1 requires that the determination not blow up under small changes — bounded, not necessarily continuous, dependence. Within a stratum, away from score-transition loci, dependence is stable: a small change in local ρ produces a bounded change in Σ and typically the same maximizer. *Sensitive loci exist:* at Σ-transition boundaries (sharp sign changes, Phase D §5) and at ties, a small change can flip the selected candidate. But a flip selects a *different admissible neighbor* — the outcome stays inside the envelope; it does not diverge or blow up. The sharpening character (Phase D §3) creates *sensitive* loci, not *unstable* ones. Bounded dependence holds. **Component 2: PASS**, with the noted caveat that sharpening localizes sensitivity at transition loci (bounded, not divergent).

**Component 3 — Reach-bounded determination.** A1 identifies this as the component with no continuum analogue — the seat of the determinability boundary — and requires that the substrate determine *within reach* and be structurally blind *beyond reach*, cleanly. Phase E §6 establishes exactly this: inside a reach stratum the substrate is fully determinable (all channels defined, rule has its information); across a decoupling surface no channel carries the determining information, and the determinability horizon coincides with the reach horizon. The orientation result (E §7) witnesses the same boundary in a second channel. ED does not merely *tolerate* reach-bounded determination — it instantiates it as a clean, multiply-witnessed geometric feature. **Component 3: PASS** (a strong, characteristic pass — this is the component ED was built to satisfy).

**Component 4 — Unique local maximizer.** A1 requires that the maximizing candidate be unique (no genuine ambiguity in the forward step). **This is where the evidence shows a gap.** Phase B §3 flagged the tie-breaking slot as open: where two or more candidates share the maximal Σ, the architecture as specified does not determine which is committed. Phases C–E did not close it — Phase E §7 identified orientation as the *leading candidate* tie-break mechanism but did not establish that orientation supplies a canonical, always-defined tie-break (and within a stratum orientation may not distinguish two coherent candidates). The unique-maximizer condition is therefore **not established**: in the tie set, forward determinism (Component 1) holds (some maximal candidate is committed) but uniqueness does not. **Component 4: CONDITIONAL** — the architecture needs a specified tie-breaking rule; until one is supplied, unique determination holds generically but not universally.

**Verdict: CONDITIONAL.** Three of four components PASS cleanly, including the characteristic reach-bounded-determination component. The fourth — unique local maximizer — rests on the tie-breaking slot left open since Phase B and never filled. This is a **genuine, specific, and closeable gap**: specify a deterministic tie-break (orientation-ordering and bandwidth-ordering are the leading candidates), and Component 4 closes to PASS. The CONDITIONAL is recorded honestly rather than waved through, in keeping with the scoping memo's standard.

---

## 6. Criterion 4 — Generative Sufficiency

**Criterion (A1):** every structural and dynamical phenomenon the substrate exhibits arises from the axioms (B1–B7) plus the rule (Σ) alone — no phenomenon requires an extra axiom smuggled in during evaluation.

**Evaluation.** The test is whether the evidence-phases ever had to *add* structure to explain what they found.

- *Envelope (Phase C)* — forbidden and necessary patterns, inequalities, ghost classes: all derived from B1–B7 + Σ. Monotonicity (I4) was *forced* from B7, not added.
- *Extremal dynamics (Phase D)* — sharpening fronts, self-limiting concentration, acyclicity, fixed-point attractors, partial recoverability: all derived from the rule + axioms. The acyclicity result came from E-I4 + F1, both already in hand; no new axiom.
- *Constraint surface & stratification (Phase E)* — the reach-stratified structure and the determinability boundary follow from B6 + factorization. **The decisive case is orientation:** it was the one phenomenon that *looked* like it might need an extra axiom (Phase D flagged the CONDITIONAL branch where orientation conservation would have to be *added*). Phase E §7 instead **derived** it as a stratified invariant from B3 + B6 + Σ-orientation-neutrality. The single best candidate for an "extra axiom" turned out to be generated, not added.

*Tie-breaking is not a counterexample.* The open tie-break slot is a gap in *unique determination* (booked under Criterion 3), not a *generative* deficit: every phenomenon — fronts, attractors, stratification — generates identically regardless of how ties resolve. No observed structure waits on the tie-break rule.

**Verdict: PASS.** Every phenomenon found in Phases C–E arises from B1–B7 + Σ. The strongest evidence is negative: the one candidate for a required extra axiom (orientation conservation) was derived from the existing architecture, not imported. Generative sufficiency holds.

---

## 7. Criterion 5 — Envelope Tightness

**Criterion (A1):** forbidden configurations are structurally excluded; necessary configurations are forced; there are **no uncharacterized ghost states** (admissible-but-unreachable regions must be either eliminated or structurally characterized); the envelope is decidable in principle.

**Evaluation.**

- *Forbidden excluded.* F1–F3, F5 are cleanly excluded at the axiom or rule level (Phase C §3); F4 (orientation reversal) was resolved in Phase E §7 — forbidden within a stratum, undefined across. No forbidden pattern slips through.
- *Necessary forced.* N1–N4 are all forced (Phase C §4); N2 promoted monotonicity to an established invariant. The necessary patterns are robust, with no flagged gap.
- *Ghost states.* Two classes exist — trans-decoupling and non-maximal-path (Phase C §7, E §8). Crucially, **both are structurally characterized and bounded**: the architecture states exactly why each is unreachable (trans-decoupling violates N3/finite reach; non-maximal violates the rule). They are not residual slack — they are *forced byproducts of finite reach and maximization*. A1's criterion forbids *uncharacterized* ghost states; ED has *only* characterized ones. Moreover, the trans-decoupling ghosts are themselves a *tightness* feature: their existence is a direct consequence of the reach axiom, not looseness in the envelope.
- *Closure & decidability.* Phase E §8 returns **closed in the characterized sense** — reachable equals admissible up to the two bounded ghost classes, no uncharacterized slack, no unresolved admissibility boundary (the orientation question that qualified Phase C's verdict was *resolved* in E §7). The envelope is decidable in principle: membership reduces to checking axiom-admissibility and rule-reachability, both finite within a stratum.

**Verdict: PASS.** Forbidden patterns are sharply excluded, necessary patterns forced, the only ghost states are fully characterized forced byproducts of finite reach (not slack), and closure is achieved in the characterized sense with no uncharacterized openness. The envelope is as tight as a finite-reach maximization architecture admits — and its ghost states are a signature of that finite reach, not a failure of tightness. *Interpretive note recorded for transparency:* this verdict reads A1's "no ghost states" as "no *uncharacterized* ghost states," consistent with A1's own introduction of the ghost-state concept as a characterization requirement; under a strict admissible-equals-reachable-identity reading, ED would score CONDITIONAL here. The PASS rests on the characterization reading, stated openly.

---

## 8. Criterion 6 — Structural Optimality

**Criterion (A1):** the architecture contains no anomalies (no unexplained or arbitrary structure); the constraint surface is economical (no redundant faces); and characteristic structural features are *forced* rather than accidental.

**Evaluation.**

- *Anomalies.* No anomaly surfaced across Phases B–E. Every face of the constraint surface (Phase E §4–5) traces to a named axiom or to the rule; no face is unexplained or arbitrary. The one structural curiosity — orientation's non-score-bearing status — is *explained* (it is the structural subspace, orthogonal to the rule's objective by design), not anomalous.
- *Economy of the constraint surface.* The surface has eight identified faces (four structural, four dynamical), each carrying distinct content; none duplicates another (Phase E §4–5). The score-bearing subspace *collapses* onto the maximization footprint (DF1), which is the opposite of redundancy — the rule reduces the effective degrees of freedom rather than adding them. The surface is economical.
- *Forced vs. accidental structure.* The defining feature — the **reach-stratified structure** — is *forced*, not accidental: it follows necessarily from B6 + causal-cone factorization (Phase E §6), and it is **multiply-witnessed** (it appears independently in SF1, DF3, the reach-stratified construction, and the orientation analysis). Multiple independent derivations converging on the same determinability boundary is the structural-optimality signature of a non-accidental feature — the substrate-level analogue of AD's overdetermination test. The stratification is not a modeling choice; it is compelled.

**Verdict: PASS.** No anomalies; an economical, non-redundant constraint surface; and the characteristic reach-stratified structure is forced and multiply-witnessed rather than accidental. The architecture's deepest structural feature is overdetermined by the axioms — strong evidence of structural optimality.

---

## 9. Six-Criteria Summary Table

| Criterion | Verdict | Evidence | Notes |
|---|---|---|---|
| **1. Minimality** | **PASS** | B (axioms independent); E §3 (channels independent); monotonicity & orientation *derived* not axiomatic | B5 is non-dynamical but not redundant; noted for G |
| **2. Locality** | **PASS** | B §3 (local Σ inputs); N3, E-I2 (finite reach); E §6 (factorization, no non-local influence) | Characteristic pass; finite reach *is* the reformulated criterion's central case |
| **3. Determinism** | **CONDITIONAL → PASS** | Components 1–3 PASS (forward, stable, reach-bounded); Component 4 closed by tie-break spec | Tie-breaking slot (B §3) **now filled** (`Phase_TieBreak_Specification.md`); unique-maximizer established → upgraded to PASS |
| **4. Generative Sufficiency** | **PASS** | C/D/E phenomena all from B1–B7 + Σ; orientation *derived* (E §7), not added | Strongest evidence is negative: no extra axiom ever needed |
| **5. Envelope Tightness** | **PASS** | C §3–4 (forbidden/necessary clean); C §7, E §8 (2 *characterized* ghost classes, closed) | Ghost states are forced byproducts of finite reach, not slack; rests on "no *uncharacterized* ghosts" reading |
| **6. Structural Optimality** | **PASS** | E §4–6 (no anomalies, economical surface, reach-stratification forced & multiply-witnessed) | Determinability boundary overdetermined → non-accidental |

---

## 10. AD Score

Counting PASS verdicts across the six criteria:

> **AD Score (as originally filed): 5 / 6 PASS, 1 CONDITIONAL, 0 FAIL.**
> **AD Score (current, post tie-break specification): 6 / 6 PASS, 0 CONDITIONAL, 0 FAIL.**

Stated neutrally: as originally filed, the ED substrate passed five of the six substrate-level AD criteria outright and received a CONDITIONAL on the sixth (Determinism), where three of four components passed and the fourth — unique local maximizer — rested on a tie-breaking rule the architecture had not yet specified. `Phase_TieBreak_Specification.md` has since supplied that rule (channel-bandwidth-ordering with a B1-distinctness final key, lexicographic and total within each reach stratum), closing Component 4 and lifting Determinism to PASS. **The current score is 6/6.**

Per the scoping memo's standard, the original CONDITIONAL was an asset to the evaluation, not a blemish on it. It demonstrated the criteria have teeth: applied honestly, they located a genuine, specific gap (the open tie-breaking slot, flagged since Phase B) rather than returning a frictionless six-for-six that would suggest the criteria had been tuned to the system. That the gap was real and the criteria caught it is the evidence of rigor; that it was then **closeable by a minimal addition using only existing structure** (channel-bandwidth-ordering, `Phase_TieBreak_Specification.md`) is the evidence the architecture was sound. Phase F deliberately did not perform that specification — it identified precisely what would close the gap and left the choice to the architecture's authors, who supplied it separately. The teeth stand; the gap is closed; the score is 6/6.

The score is recorded as evidence about the architecture; it is not a claim about the physical correctness of Event Density, which is outside AD's remit. AD evaluates structural well-builtness, not empirical truth.

---

## 11. Next Actions

Phase F completes **Step 5 of AD** (Validate Against Criteria). The ED substrate scores **5 PASS / 1 CONDITIONAL / 0 FAIL**, with the CONDITIONAL on Determinism's unique-maximizer component and a clear, single action to close it (specify the tie-break rule).

**Phase G begins Step 6 of AD** (Generalization and Taxonomy Extension). It addresses the questions Phase F deliberately set aside as outside the per-criterion verdicts:

- whether the ED substrate constitutes a **new pole** in AD's taxonomy or instances an existing one, given that its defining surface type (reach-stratified) has no continuum analogue (Phase A2, Phase E §9);
- whether the **determinability boundary** is a cross-domain structural invariant — the formal point of contact with the FS parallel (the parity barrier) and the AD note's proposed substrate-level extension;
- how the substrate-level evaluation relates back to the PDE-shadow evaluation (catalog entry #15) — in particular the substrate-sharpens / shadow-diffuses result (Phase D §3) as a concrete instance of a property manufactured by coarse-graining;
- and the open items this evaluation surfaced (the tie-breaking specification; B5's non-dynamical status; the quantification of the determinability boundary in bits, the standing deliverable parallel to FS).

Phase G is the integration and generalization phase; it does not revisit the verdicts, which are fixed here.

The criteria are evaluated. The generalization begins.

---

*End of Phase F. This phase rendered the AD criteria verdicts for the ED substrate: 5 PASS, 1 CONDITIONAL, 0 FAIL as originally filed; **6 PASS, 0 CONDITIONAL, 0 FAIL** after `Phase_TieBreak_Specification.md` closed the Determinism CONDITIONAL. The generalization and taxonomy extension begin at Phase G.*
