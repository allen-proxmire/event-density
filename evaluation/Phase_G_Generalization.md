# Phase G — Generalization and Taxonomy Extension

**Evaluation:** Architectural Distillation of the Event Density *substrate* (discrete relational layer)
**Phase:** G (Generalization and Extension)
**AD step:** Step 6 — Generalize and Extend
**Status:** Final phase; integrates Phases B–F, assigns the pole, extends the taxonomy
**Date filed:** June 2026
**Author:** Allen Proxmire
**Related:** `Phase_B`–`Phase_F` (evidence and verdicts); `AD_Note_SubstrateBeneathTheShadow.md` (the motivating note); `evaluations/AD_Evaluation_EventDensity.md` (catalog entry #15, the PDE-shadow evaluation)

---

## 1. Purpose

Phase G performs **Step 6 of AD**: generalization, taxonomy placement, and cross-domain synthesis. With the verdicts rendered in Phase F (5 PASS / 1 CONDITIONAL / 0 FAIL), the per-criterion work is done. Phase G's job is not to re-judge but to **interpret** — to take the now-fixed evaluation and place it within the AD framework as a whole.

This phase explicitly **does not revisit verdicts.** They are fixed at Phase F. Phase G uses them, and the evidence beneath them, as the raw material for four integrative outputs:

- a **pole assignment** — where the ED substrate sits in AD's taxonomy (existing pole, hybrid, or new);
- **cross-domain structural parallels** — what the substrate shares with other atlas entries, the FS parallel chief among them;
- **transferable results** — which findings generalize beyond ED to any discrete relational substrate, and how they extend AD's machinery;
- **open-problem localization** — a clean statement of what remains open, sorted into architectural vs. empirical work.

One discipline governs this phase above all others, because it is the phase most exposed to overreach. **The cross-domain parallels Phase G draws are structural and methodological — claims about shared *architecture*, detected by a shared *evaluation framework*. They are not claims that ED explains primes, that FS explains physics, or that the two systems are the same object.** AD detects that two architectures share a structural motif; that is the entire claim, and it is a claim about form, not content. The scoping memo's neutrality requirement and the AD note's "structural analogies are invitations to measure, not conclusions" both apply here in full force.

---

## 2. Inputs

Phase G uses the complete evidence record and the fixed verdicts:

- **Architectural specification (Phase B)** — axioms B1–B7, rule Σ = Coh − Str − Grad, five channels, candidate invariants I1–I5, open tie-break slot.
- **Envelope extraction (Phase C)** — forbidden/necessary patterns, inequalities E-I4/E-I5/E-I2, causal-cone factorization, two characterized ghost-state classes.
- **Extremal dynamics (Phase D)** — sharpening (non-diffusing) fronts, self-limiting concentration, acyclic dynamics, local-maximization fixed points, partial footprint recoverability.
- **Constraint surface (Phase E)** — determinability boundary located at the decoupling surface, orientation stratified, closed-in-the-characterized-sense, surface type stability-resolved + reach-stratified + commitment-dissipative + locally graph-contractive.
- **Criteria evaluation (Phase F)** — **5 PASS / 1 CONDITIONAL / 0 FAIL**; CONDITIONAL on Determinism (unique-maximizer component, tie-break gap).

These are treated as evidence for generalization. Phase G adds no new extraction and no new verdict.

---

## 3. Pole Assignment

AD's existing pole taxonomy was developed for **continuum dynamical systems** — the seven poles (diffusive, hyperbolic, dispersive, geometric, aggregation, fluid, integrable) classify PDEs by their channel structure on the shadow side. The question is whether the ED *substrate* fits one of these, a hybrid, or requires a new pole.

**Why no existing pole fits.** The existing poles are defined by *continuum channel signatures* — what the differential operator does (diffuse, propagate, disperse). The substrate has no differential operator; it has a discrete maximization rule on a participation graph. More decisively, the substrate's defining features have **no continuum analogue**:

- the **reach-stratified constraint surface** (Phase E §6/§9) — a product surface that factorizes at decoupling boundaries, with the determinability boundary at the strata edges. No continuum pole has a stratified surface of this kind; continuum systems propagate without an intrinsic reach horizon.
- the **sharpening dynamics** (Phase D §3) — maximization selects extremes, the opposite of the diffusive averaging that defines the diffusive pole. Yet the substrate is not hyperbolic either (no wave operator, no two-way propagation); its "speed" is reach-bounded and bandwidth-modulated, not a fixed characteristic.
- the **acyclic attractor structure under monotonicity** (Phase D §6) — fixed-point-only dynamics forced by irreversibility, with cycles structurally excluded. The integrable pole has the opposite signature (recurrence, conserved tori); the aggregation pole is the nearest continuum cousin but lacks the reach stratification.
- the **local-maximization footprint** (Phase C N1, Phase D §7) — every reachable state carries an optimality stamp. No continuum pole is *selection-driven* in this sense; continuum laws are differential, not extremal-selective at each point.
- the **finite-reach determinability boundary** (Phase E §6) — a structural horizon internal to the architecture. No continuum pole carries a determinability boundary; continuum well-posedness assumes global determination.

**Assignment: a new pole — the *reach-stratified selection* pole (substrate-mode).** The ED substrate is the first atlas entry of a structural class the continuum poles cannot contain: a discrete, finite-reach, selection-driven architecture whose constraint surface is reach-stratified and whose dynamics are sharpening and acyclic. Provisionally named the **reach-stratified selection pole**, it is a *substrate-mode* pole — it classifies discrete relational substrates, not continuum shadows, and therefore sits in a substrate-mode wing of the taxonomy rather than alongside the seven continuum poles directly.

**Justification and caution.** The assignment rests on a *single worked example* (ED). AD's standard is that a pole is established by recurrence across multiple entries, not declared from one. Phase G therefore assigns the pole **provisionally**: the ED substrate *defines a candidate new pole*, and the candidate is confirmed only when a second, independent discrete relational substrate is evaluated and lands in the same structural class. The FS architecture (§4) is the leading candidate for that second entry — but it has not been run through a substrate-level AD evaluation, so the pole stands as candidate, not confirmed. This is the honest assignment: a new pole is *indicated*, not *established*.

---

## 4. Cross-Domain Structural Parallels

**Within the existing atlas.** The substrate's nearest continuum neighbor is the **aggregation pole** (irreversible accumulation, monotone growth, fixed-point attractors) — the parallel is the commitment-dissipative, acyclic character (Phase E §9, Phase D §6). But the parallel is partial: aggregation lacks reach stratification and the selection footprint. The substrate is *aggregation-like in its irreversibility, unlike aggregation in its reach structure*. This is a structural neighbor, not a home pole — consistent with the new-pole assignment.

**The FS ↔ ED parallel.** This is the parallel the AD note named and the substrate review was partly motivated to test. It is stated here as a structural correspondence detected by AD, and **nothing more** — FS is a theory of multiplicative integer structure; ED is a physical-substrate framework; they share no subject matter. What they share is *architectural form*, which is exactly what AD is built to compare. Three correspondences:

- **Determinability boundary ↔ parity barrier.** ED's determinability boundary is the decoupling surface (Phase E §6): the architecture determines within reach and is structurally blind across it. FS's parity barrier (Sarnak disjointness) is the locus past which the multiplicative architecture cannot determine sign/parity structure. Both are *finite-reach horizons made into determinability limits* — the architecture's reach and its determinability coincide. This is the central correspondence: two architectures, each with a structural horizon where determination ends, located by the same AD machinery.
- **Finite reach ↔ finite correlation length.** ED's reach is bounded by decoupling surfaces (B6); FS's effective "reach" is the finite correlation structure past which multiplicative templates decouple. In both, influence is local-and-bounded, and the bound is a positive structural feature, not a deficiency.
- **Sharpening vs. diffusive shadows.** Both architectures are *substrates whose continuum shadow is smoother than the substrate itself*. ED sharpens (maximization) while its PDE shadow diffuses (Phase D §3); FS's discrete escape/coverage structure projects to the smooth PNT density (the "shadow of escape density"). In both, the smoothness of the shadow is a coarse-graining artifact, not a substrate property.

**Does the ED substrate provide a new structural motif for AD?** Yes — and the FS parallel is what elevates it from an ED-specific finding to a candidate motif. The motif is: **a discrete finite-reach generative substrate + a determinability boundary at the reach horizon + a continuous projection shadow smoother than the substrate.** AD detected this motif once in FS (informally, via the note) and now formally in ED. Two instances make it a *candidate motif*; it is named here as the **finite-reach / determinability-boundary / projection-shadow** motif and proposed for the atlas — provisionally, pending the confirming second substrate-level evaluation (§3). The motif is structural; it makes **no** claim that the two domains are related in content.

---

## 5. Substrate vs. Shadow Analysis

The sharpest integrative result of the whole review is Phase D §3: **the substrate sharpens; the PDE shadow diffuses.** Phase G develops what this means for AD.

**Which AD features the shadow inherits.** The PDE shadow (catalog entry #15) inherited and was correctly evaluated on: locality (the substrate is local → the PDE is local), the monotone/irreversible character (P11 → the parabolic arrow), and the aggregation-like accumulation. These are *genuine inheritances* — features of the substrate that survive coarse-graining into the shadow. AD's evaluation of #15 was correct *about the shadow*, and these features are why.

**Which features are artifacts of coarse-graining.** The defining feature of #15 — its **diffusive (degenerate-parabolic) character** — is **not inherited; it is manufactured by coarse-graining.** The substrate is locally sharpening (maximization selects extremes); averaging a sharpening selection rule over many chain steps and many chains produces a diffusive averaged law. The diffusion is real *in the shadow* but absent *in the substrate*. So the property AD used to *classify* #15 (diffusive pole) is a coarse-graining artifact, not a substrate property. The substrate belongs to a different pole (§3) than its own shadow.

**What this means for AD's treatment of discrete vs. continuum systems.** This is a genuinely important methodological finding, stated carefully:

> **A system's pole on the shadow side need not match its pole on the substrate side.** Coarse-graining can manufacture a channel signature (here, diffusion) that the substrate does not possess. AD evaluating a continuum law is therefore evaluating the *shadow's* architecture, which may differ in pole from the substrate that casts it.

The consequence is not that AD's shadow-side evaluations are wrong — they are correct *about shadows*. The consequence is that **shadow-side and substrate-side evaluations are different evaluations of different objects**, and AD should treat them as such. The ED case is the worked demonstration: #15 (diffusive-pole shadow) and the ED substrate (reach-stratified-selection pole) are *the same physical theory evaluated at two levels*, landing in two different poles, because coarse-graining changed the channel signature. AD's atlas should record both, linked, and not assume the substrate inherits the shadow's classification.

---

## 6. Transferable Results

The following findings were established for ED but depend only on the *general* features of a discrete relational substrate (finite reach, irreversible commitment, local maximization) — not on anything ED-specific. They transfer to **any** discrete relational substrate with those features, and they are the substrate-level extension's genuine contributions to AD:

- **Reach-bounded determination.** Any finite-reach substrate has a determinability boundary at its reach horizon — determination within, structural blindness across (generalizes Phase E §6). This is a *general theorem-shape*, not an ED fact.
- **Stratified invariants.** Any substrate whose interaction structure factorizes at reach boundaries supports invariants that are *local within a stratum and undefined across* — conserved everywhere they are comparable, with comparability co-extensive with reach (generalizes the orientation result, Phase E §7).
- **Maximization footprints.** Any selection-driven substrate stamps every reachable state with a local-optimality signature; the *extensive* footprint (what was selected) is recoverable under irreversibility, the *intensive* footprint (margins, order) is not (generalizes Phase C N1 + Phase D §7).
- **Acyclic attractors under monotonicity.** Any substrate combining a monotone accumulated quantity with irreversibility is *acyclic* — cycles are structurally excluded, and the dynamics run to fixed points only (generalizes Phase D §6; the A2 "fixed-point-or-cycle" dichotomy collapses to fixed-point-only whenever monotonicity + irreversibility hold).
- **Ghost-state characterization.** Any finite-reach maximization substrate generates exactly two characterizable ghost-state classes — trans-reach (unreachable because construction would require crossing a reach boundary) and non-maximal-path (unreachable because the selection rule excludes them) — and these are tightness *signatures*, not slack (generalizes Phase C §7 / Phase E §8).

Each of these is a statement about a *class* of architectures, derived in the ED evaluation but not contingent on ED. Together they are the substrate-mode content that Phases A1/A2 introduced as *machinery* and that the ED evaluation has now *exercised and confirmed* on a real example.

---

## 7. Taxonomy Extensions

Phase G proposes the following extensions to AD's classification system, each marked as **core** (belongs in AD's domain-agnostic core) or **substrate-mode** (belongs in the discrete-substrate wing):

| Extension | What it adds | Placement | Rationale |
|---|---|---|---|
| **Reach-stratified surface type** | A constraint-surface type that factorizes at reach boundaries | **Substrate-mode** | No continuum analogue (Phase A2, E §9); only arises with finite reach |
| **Reach-bounded determination** (4th determinism component) | A determinism component for architectures with a determinability boundary | **Core** | Determinism is a core criterion; this component refines it for *any* architecture, finite-reach or not (continuum systems trivially satisfy it with infinite reach) |
| **Ghost-state characterization** (envelope concept) | The requirement that admissible-but-unreachable regions be characterized, not merely absent | **Core** | Sharpens envelope-tightness for all architectures; continuum systems can have ghost states too |
| **Sharpening-vs-diffusive dynamical signature** | A dynamical descriptor distinguishing extremal-selective from averaging dynamics | **Core** | Applies to the substrate-vs-shadow relation generally; bears on pole assignment at both levels |
| **Substrate/shadow pole-mismatch** (atlas convention) | The convention that a theory may hold different poles at substrate and shadow levels | **Core (convention)** | Demonstrated by ED (§5); a general caution for any multi-level evaluation |

**Recommended disposition.** The *surface type* is substrate-mode (it genuinely requires finite reach). The remaining four are **core**: reach-bounded determination, ghost-state characterization, the sharpening/diffusive signature, and the substrate/shadow pole-mismatch convention all generalize to architectures AD already evaluates, and they make the core framework *more* discriminating without restricting it to discrete substrates. The substrate-level review thus returns more to AD's core than to its substrate wing — which is the strongest argument that the review was worth doing as AD methodology, independent of its ED verdict.

---

## 8. Open-Problem Localization

Three open items remain. Each is localized as **architectural** (a question about the substrate's specification, answerable by stating or deriving structure) or **empirical** (a question requiring measurement or external confirmation).

**8.1 — Tie-breaking rule (the unique-maximizer gap).**
*Evidence:* Phase B §3 flagged the open tie-break slot; Phase F gave Determinism a CONDITIONAL solely on this. Where candidates tie on Σ, the architecture does not specify which commits.
*Work remaining:* specify a deterministic tie-break. Phase E §7 and Phase F name the leading candidates — orientation-ordering and channel-bandwidth-ordering. Establishing that one of these is always defined and canonical closes Determinism's Component 4 to PASS (→ 6/6).
*Type:* **architectural.** It is answered by stating (or deriving) one rule; no measurement is involved.

**8.2 — Orientation: axiom vs. derived local invariant.**
*Evidence:* B5 posits orientation as a primitive field; Phase E §7 derived its *conservation* as a stratified local invariant (not an added axiom); Phase F §3 noted B5 is the one non-dynamical axiom (it bears no Σ score).
*Work remaining:* determine whether orientation must remain a primitive (B5 as posited) or whether the orientation *field itself* — not just its conservation — can be derived from the participation/channel structure (B2, B3), which would remove an axiom and strengthen minimality. This is a genuine open architectural question: Phase G could not settle whether B5 is irreducible or reducible.
*Type:* **architectural.** It concerns whether a primitive is derivable from the others.

**8.3 — Quantitative measurement of the determinability boundary (bits).**
*Evidence:* Phase E §6 located the determinability boundary *structurally* (the decoupling surface). The AD note's standing deliverable is to quantify it *numerically*, in bits, paralleling FS's quantified parity barrier (escape ≈ 0.265, etc.).
*Work remaining:* define and compute an information-theoretic measure of how much determination is lost across a decoupling surface — the ED analogue of FS's bit-decomposition. This is the structural-side review (now complete) handing a target to the quantitative-side program.
*Type:* **empirical / quantitative.** It requires a measurement program, not just a specification. It is the one open item that exits the architectural domain entirely.

**Localization summary:** two architectural (tie-break, orientation-primitivity), one empirical (boundary in bits). The architectural items are closeable within the ED corpus; the empirical item launches a measurement program parallel to FS.

---

## 9. Summary Table

| Topic | Result | Domain | Notes |
|---|---|---|---|
| **Pole assignment** | New pole: *reach-stratified selection* (provisional) | Substrate | Candidate; confirmed only by a 2nd independent substrate evaluation |
| **Nearest existing pole** | Aggregation (partial) | Shadow/general | Shares irreversibility; lacks reach stratification |
| **FS ↔ ED parallel** | Structural motif, not content overlap | General | Det. boundary ↔ parity barrier; **no** claim of shared subject matter |
| **Shared motif** | Finite-reach substrate + det. boundary + smoother projection shadow | General | Candidate atlas motif; 2 instances (FS informal, ED formal) |
| **Substrate vs. shadow** | Substrate sharpens; shadow diffuses | Both | Diffusion is a coarse-graining artifact, not inherited |
| **Pole mismatch** | Substrate pole ≠ shadow pole for the same theory | General | ED substrate (reach-stratified) vs. #15 (diffusive) |
| **Reach-bounded determination** | General theorem-shape | General | Proposed core determinism component |
| **Stratified invariants** | General | General | Conserved within reach, undefined across |
| **Maximization footprints** | General | General | Extensive recoverable, intensive lost |
| **Acyclic-under-monotonicity** | General | General | A2 dichotomy collapses to fixed-point-only |
| **Ghost-state characterization** | General | General | Proposed core envelope concept |
| **AD score** | 5 PASS / 1 CONDITIONAL / 0 FAIL | ED-specific | CONDITIONAL on Determinism (tie-break) |
| **Open: tie-break** | Architectural | ED | Closes Determinism → 6/6 |
| **Open: orientation primitivity** | Architectural | ED | B5 irreducible or derivable? |
| **Open: boundary in bits** | Empirical | ED↔FS | Launches measurement program |

---

## 10. Next Actions

**The ED-substrate AD evaluation is now complete.** Seven phases (A scoping + A1/A2 methodology extension; B specification; C/D/E extraction; F verdicts; G generalization) have taken the discrete ED substrate from "not yet evaluable by AD" to a full evaluation with a score (5 PASS / 1 CONDITIONAL / 0 FAIL), a provisional pole, and an extended taxonomy. The review delivered on the scoping memo's promise: it did not merely apply AD to a new object — it *extended AD downward to the substrate level* and returned new core machinery in the process.

**Recommendations:**

1. **Archive the evaluation.** The `ED_Substrate/` folder (Memo_00, Phase_A, A1, A2, B, C, D, E, F, G) is a complete, self-contained substrate-level AD evaluation. Mark it closed; it is citable as the first worked substrate-mode evaluation.

2. **Integrate results into the AD atlas.** Specifically: add the ED substrate as a substrate-mode atlas entry, linked to its own shadow (#15) with the pole-mismatch noted; adopt the four **core** taxonomy extensions (reach-bounded determination, ghost-state characterization, sharpening/diffusive signature, substrate/shadow pole-mismatch convention); record the *reach-stratified surface type* in the substrate-mode wing; and list the **finite-reach / determinability-boundary / projection-shadow motif** as a candidate motif pending a confirming second entry.

3. **Close the two architectural open items when convenient.** Specify the tie-break rule (lifts Determinism to PASS, the evaluation to 6/6); and resolve whether B5 (orientation) is irreducible or derivable (bears on minimality). Both are internal to the ED corpus.

4. **Begin the determinability-boundary measurement program (optional).** The structural side is now complete and has handed the quantitative side a precise target: measure, in bits, the determination lost across a decoupling surface — the ED counterpart to FS's quantified parity barrier. This is the standing deliverable from the AD note, now fully scoped by the structural review. It is optional, separable, and the natural next body of work if the parallel is to be made quantitative.

A closing note on the circularity guard, which governed every phase. AD was extracted from FS; the motivation to extend it to the substrate came from the FS↔ED parallel. The guard required that all substrate-level criteria and modes be fixed (Phases A1/A2), stated for the general class, before ED was scored. They were. The result — 5 PASS and one honest CONDITIONAL on a specific, named, closeable gap — is what the fixed criteria returned when applied to the evidence. A clean six-for-six would have been the warning sign; the single CONDITIONAL is the evidence that the criteria kept their teeth to the end.

---

*End of Phase G, and of the ED-substrate AD evaluation. This phase generalizes and extends; it does not revisit the verdicts. The evaluation is complete and recommended for archiving and atlas integration. The determinability-boundary measurement program, if pursued, begins where this review ends.*
