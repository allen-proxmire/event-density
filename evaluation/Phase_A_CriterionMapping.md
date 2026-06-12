# Phase A — Criterion Mapping

**Evaluation:** Architectural Distillation of the Event Density substrate
**Phase:** A (scoping execution)
**Status:** Phase A deliverable
**Date filed:** June 2026
**Author:** Allen Proxmire
**Follows:** `Memo_00_ED_Substrate_AD_Scoping.md`

---

## 1. Purpose of Phase A

Phase A determines whether AD's six criteria and six process steps transfer cleanly to a **discrete relational substrate**, rather than the continuum laws AD was developed on.

A precise statement of the object under assessment: **this document does not evaluate the substrate. It evaluates the applicability of AD itself.** Every verdict below is a verdict about whether an AD *criterion* or *step* translates to a discrete substrate — not a verdict about whether the substrate satisfies it. No PASS/CONDITIONAL/FAIL on the substrate appears here; that is the work of Phase F, against whatever criteria Phase A determines are usable.

The output is the four deliverables specified in Memo-00: a criterion mapping (Section 2), a step-applicability table (Section 3), a substrate-feature accommodation list (Section 4), and a proceed/extend decision (Section 5).

Neutrality governs throughout. The conclusion is allowed to be "AD applies directly," "AD needs extensions," or anything between — determined by the analysis, not assumed.

---

## 2. Mapping AD's Six Criteria to Substrate-Level Equivalents

### 2.1 Minimality

**AD definition.** No redundant axioms, operators, parameters, or channels; every component does independent structural work.

**Substrate-level analogue.** No redundant primitive, channel, or update-rule term. Each substrate primitive (micro-events, participation, adjacency, channels, chains, commitment density, decoupling surfaces, P11) must do work not produced by the others; each term of the stability score (Coh, Str, Grad) must be independent.

**Strain points.** Minimal. Minimality is a statement about independence of components, which is indifferent to whether the components are continuum operators or discrete primitives. The only adaptation is vocabulary: "primitive" and "channel" replace "axiom" and "operator."

**Verdict: DIRECTLY APPLICABLE.** Minimality transfers with vocabulary substitution only.

### 2.2 Locality

**AD definition.** Evolution at a point depends only on the state and its derivatives at that point or an infinitesimal neighborhood — no global integrals, nonlocal operators, or action at a distance.

**Substrate-level analogue.** The update at a micro-event depends only on its **graph-local neighborhood** — adjacent micro-events, the channels incident to it, the local commitment density, and the local gradient term in the stability score. "Local" means graph-local (bounded adjacency), not continuum-local (derivatives at a point).

**Strain points.** The continuum wording ("derivatives at a point") has no direct substrate referent; the substrate has no derivatives, it has local strain (Str against ρ_local) and a local gradient term (Grad against ∇ρ on the participation graph). More substantively: the substrate's **finite reach** (decoupling surfaces) is a locality-*strengthening* feature, not a violation — a parabolic PDE has infinite propagation speed, while the substrate's influence is bounded by its decoupling surfaces. The criterion must be restated to (a) use graph-locality and (b) recognize finite reach as enhanced locality rather than as a nonlocal sector to quarantine. The one genuinely relational feature — participation reaching across adjacency — must be checked to confirm it acts only within the graph-local neighborhood and not as a global coupling.

**Verdict: REQUIRES REFORMULATION.** The concept transfers and the substrate may satisfy it more cleanly than the PDE did, but the criterion must be restated in graph-local terms and must treat finite reach as a locality feature.

### 2.3 Determinism — *special attention*

**AD definition.** Well-posedness: existence, uniqueness, and continuous dependence on initial data; initial data uniquely determines the evolution for all time.

**The mismatch, stated exactly.** AD's determinism is continuum well-posedness, which carries three assumptions that a discrete relational substrate does not share in the same form:

1. **Continuous dependence.** There is no continuum metric on substrate configurations, so "continuous dependence on initial data" has no direct referent. The substrate needs *stable dependence*: a bounded change in the initial micro-event configuration produces a bounded change in the evolution, measured in a discrete (graph/configuration) metric.

2. **Determination "for all time" / everywhere.** Continuum well-posedness assumes initial data determines the solution throughout the domain. The substrate's **finite reach** means a region's evolution is determined only by data *within its decoupling-surface horizon*; data beyond the horizon does not propagate in. This is not a failure of determinism — it is a *refinement*: the substrate is determined within its reach and structurally undetermined beyond it. This is exactly the **determinability boundary** appearing inside the determinism criterion. A substrate-level determinism criterion must say "initial data within the reach horizon uniquely determines evolution within that horizon."

3. **Uniqueness of the update.** The substrate evolves by maximizing the stability score Σ. Determinism at the substrate level therefore requires that the maximizer be **generically unique** — that the stability landscape does not generically admit ties between distinct next-states. This is a discrete uniqueness question the continuum criterion does not directly pose (the continuum PDE's uniqueness is a theorem about the equation, not about a maximization step).

**What is *not* a mismatch.** The substrate's **forward-only** character (P11 irreversibility, the built-in arrow) might appear to conflict with well-posedness, but it does not. The parabolic PDE shadow is itself forward-well-posed and backward-ill-posed — parabolic smoothing is irreversible, information is lost at the continuum level too. The substrate's irreversibility is the discrete root of the shadow's irreversibility, not a deviation from it. A substrate-level determinism criterion should therefore be stated as **forward determinism** (initial data → forward evolution) and should *not* require backward determination. Forward-only is inherited, not anomalous.

**What a substrate-level determinism criterion must say.** Combining the three reformulations: *the substrate is deterministic if (i) the stability-score maximizer is generically unique at each step, (ii) initial data within a region's reach horizon uniquely determines that region's forward evolution, and (iii) evolution depends stably (boundedly) on the initial configuration in the discrete metric.* Backward determination is not required; finite-reach determination is explicit.

**Verdict: REQUIRES REFORMULATION** — and this is the most informative criterion in the mapping. Its reformulation forces the determinability boundary and finite reach into the criterion set explicitly, and distinguishes the genuine substrate features (uniqueness of the local maximizer, reach-bounded determination) from the inherited one (forward-only, shared with the shadow).

### 2.4 Generative Sufficiency

**AD definition.** The architecture generates all the laws, behaviors, and phenomena it is supposed to produce; zero gap between claimed and derivable output.

**Substrate-level analogue.** The substrate generates all its target structures: the quantum structures, the gravitational structures, the soft-matter PDE, and the catalogued forced theorems. Generative sufficiency asks whether every target output is derivable from the primitives plus the update rule.

**Strain points.** Minimal. This criterion is domain-agnostic and is, in fact, the criterion the substrate is most natively suited to — the ED program is framed precisely as "these structures follow as forced theorems from the substrate." The criterion transfers directly; the *assessment* (Phase F) will be substantial, but the criterion itself needs no reformulation.

**Verdict: DIRECTLY APPLICABLE.** Generative sufficiency transfers as-is and is the substrate's most natural criterion.

### 2.5 Envelope Tightness

**AD definition.** The system's bounds are tight — saturated by actual solutions or configurations — rather than loose.

**Substrate-level analogue.** The substrate's envelope bounds (the forbidden/necessary configurations and the inequalities derivable from the primitives) are tight if each is saturated by an explicit substrate **configuration**. Example candidates: the Bell–Tsirelson bound as a saturated envelope (achieved by explicit entangled configurations), and the decoupling-surface reach bound as a structural envelope.

**Strain points.** The notion of "saturated by an explicit solution" must be restated as "saturated by an explicit configuration," and the substrate's envelope must first be *defined* (Step 2 / Section 3) before its tightness can be assessed. The concept transfers but is not yet operationalized for discrete configurations; the operationalization is the reformulation required.

**Verdict: REQUIRES REFORMULATION.** The concept transfers; "configuration" replaces "solution," and the discrete envelope must be defined before tightness is meaningful.

### 2.6 Structural Optimality

**AD definition.** No simpler architecture produces the same set of laws; the architecture is the simplest structure capable of its generative output.

**Substrate-level analogue.** No smaller set of primitives and no simpler update rule generates the same target structures (the three domains plus the forced theorems). Removing any primitive, channel, or stability-score term either eliminates a target structure or introduces an anomaly.

**Strain points.** Minimal at the conceptual level — structural optimality is domain-agnostic (it is a minimality-of-the-whole statement, where minimality §2.1 is a no-redundant-part statement). The criterion transfers directly in concept. Its *assessment* is the most demanding of the six (it requires reasoning over alternative substrate architectures), but that is an assessment burden, not a translation problem.

**Verdict: DIRECTLY APPLICABLE.** Structural optimality transfers conceptually; the assessment is demanding but the criterion needs no reformulation.

### 2.7 Criterion mapping summary

| Criterion | Verdict | Reformulation required |
|---|---|---|
| Minimality | DIRECTLY APPLICABLE | Vocabulary only (primitive/channel for axiom/operator) |
| Locality | REQUIRES REFORMULATION | Graph-local restatement; finite reach as enhanced locality |
| Determinism | REQUIRES REFORMULATION | Forward + unique-maximizer + reach-bounded + stable-dependence |
| Generative sufficiency | DIRECTLY APPLICABLE | None |
| Envelope tightness | REQUIRES REFORMULATION | "Configuration" for "solution"; define discrete envelope first |
| Structural optimality | DIRECTLY APPLICABLE | None (assessment demanding, criterion intact) |

Three criteria transfer directly; three require reformulation. The three that transfer (minimality, generative sufficiency, structural optimality) are AD's domain-agnostic core. The three that require reformulation (locality, determinism, envelope tightness) are AD's continuum-flavored criteria — those whose original wording assumed a continuum law.

---

## 3. Step-Applicability Table (AD Steps 1–6)

| Step | Purpose | Direct? | Modification Needed | Notes |
|---|---|---|---|---|
| **1. Identify the architecture** | Decompose into axioms, operators, parameters, channels, governing equations | **Yes** | Vocabulary only | The substrate decomposes cleanly: primitives (axioms), stability-score (governing rule), channels/participation (interaction structure). Maps to Step 1 directly. |
| **2. Derive the envelope (Mode 1)** | Forbidden/necessary configurations, envelope inequalities, invariants from axioms alone | **With adaptation** | Define the *discrete envelope*: forbidden/necessary substrate configurations and bounds derivable from the primitives without running the update rule | The mode transfers; "configuration" replaces "state," and the envelope is over graph configurations rather than function spaces. |
| **3. Identify extremal dynamics (Mode 2)** | Front speeds, decay rates, stability, blow-up, universal inequalities from the governing equation | **With adaptation** | Restate extremal dynamics for a discrete update: reach/propagation behavior (front = reach horizon growth), strain relaxation (decay), stability of the maximization, irreversibility consequences | Front *speed* becomes reach-horizon behavior bounded by decoupling surfaces; decay becomes strain relaxation under repeated Σ-maximization. |
| **4. Construct the constraint surface (Mode 3)** | Channel interaction geometry, impossible/forced combinations, universality classes | **With adaptation** | Define the constraint surface of a *participation/adjacency graph*: how channels and participation co-constrain; impossible and forced participation combinations | The most adaptation-heavy step. AD's constraint surface is a geometric object in continuum channel space; the substrate's is the constraint geometry of the participation graph. |
| **5. Validate and evaluate** | Apply the six criteria; compile the constraint census; render verdicts | **Yes, conditional** | Apply the *reformulated* criteria from Section 2 (locality, determinism, envelope tightness) rather than their continuum forms | Step 5 applies directly once Section 2's reformulations exist; it is the step that consumes them. |
| **6. Generalize and extend** | Place the system in the taxonomy; extend poles if needed | **Yes** | None | Directly applicable: whether the substrate constitutes a new pole or a cross-domain invariant is exactly the Step 6 question, and connects to the determinability-boundary note. |

**Pattern.** Steps 1, 5, and 6 apply directly (Step 5 conditional on Section 2's reformulations existing). Steps 2, 3, and 4 — the three-mode extraction engine — require adaptation, because each was built to extract constraints from a continuum governing equation and must be restated to extract them from a discrete update rule over a graph. This mirrors the criterion split: AD's domain-agnostic scaffolding transfers; AD's continuum-extraction machinery needs discrete restatement.

---

## 4. Substrate-Specific Structural Features AD Must Accommodate

### 4.1 Finite reach (decoupling surfaces)

**Description.** Influence is bounded; reciprocal participation between regions ends at a decoupling surface. A region's determinations extend only to its reach horizon.

**Interacts with.** Locality (finite reach is enhanced locality), Determinism (reach-bounded determination — the determinability boundary), Envelope tightness (the reach bound is a candidate saturated envelope), Step 3 (the reach horizon is the substrate's "front").

**Forces modification?** **Yes.** Determinism must be restated as reach-bounded; locality must recognize finite reach as a feature, not a nonlocal sector. This is the single feature that most reshapes the criteria.

### 4.2 Forward-only evolution (P11 irreversibility)

**Description.** Every commitment is irreversible; the substrate has a built-in arrow and cannot be run backward.

**Interacts with.** Determinism.

**Forces modification?** **Mild.** The determinism criterion should be stated as forward determinism (no backward requirement). But this is inherited from the parabolic shadow's own irreversibility, not anomalous — so it adjusts the wording of determinism without introducing a new structural demand.

### 4.3 Discrete update rule (Σ = Coh − Str − Grad)

**Description.** The substrate evolves by extending each chain to the next state of maximum stability score.

**Interacts with.** Determinism (uniqueness of the maximizer), Locality (the rule is graph-local), Step 3 (the dynamics *are* the maximization).

**Forces modification?** **Yes.** Determinism requires a uniqueness-of-update clause (the Σ-maximizer is generically unique). Step 3's extremal-dynamics extraction must be restated to operate on a maximization rule rather than a differential equation.

### 4.4 Participation / adjacency graph structure

**Description.** The substrate is a relational graph: micro-events linked by adjacency, channels carrying bandwidth.

**Interacts with.** Locality (graph-locality), Step 4 (the graph *is* the interaction structure / constraint surface).

**Forces modification?** **Yes.** Locality must be restated graph-theoretically; the Step 4 constraint surface must be defined over the participation graph rather than continuum channel space.

### 4.5 Orientation conservation

**Description.** The conserved relational orientation carried by the channel structure (the discrete analogue of a conserved quantity).

**Interacts with.** Envelope (a conserved quantity is an envelope invariant), Step 2 (invariant extraction).

**Forces modification?** **No** — but it is a candidate substrate invariant to be confirmed in Step 2. It populates the envelope rather than reshaping a criterion.

### 4.6 Discrete curvature and commitment density

**Description.** The substrate-level geometric structure: the relational curvature of the participation graph and the local commitment density.

**Interacts with.** Envelope (bounds on curvature/density), Step 3 (their dynamics), AD's geometric pole language.

**Forces modification?** **Possibly.** AD's geometric vocabulary (curvature-driven evolution, the geometric pole) is continuum. If the substrate's discrete curvature is to be placed in the taxonomy (Step 6), a discrete-geometric analogue may be needed. Flagged, not resolved.

### 4.7 Chain stability and local maximization

**Description.** The substrate's dynamics are the per-step maximization of the stability landscape by each chain.

**Interacts with.** Determinism (uniqueness), Step 3 (this is the extremal dynamics).

**Forces modification?** **Yes** — jointly with 4.3. The substrate's "extremal dynamics" is literally a maximization, which is closer to AD's "extremal" language than a PDE is, but the extraction must be restated to read constraints off a maximization rather than off front speeds and decay rates.

---

## 5. Proceed / Extend Decision

**Decision: (B) — AD requires substrate-level extensions before evaluation.**

This is the evidence-based reading of Sections 2–4, stated neutrally. It is not a judgment that the substrate fails anything, nor that AD is inadequate; it is a determination that AD's continuum-flavored half must be restated for a discrete substrate before the criteria can be applied without distortion.

The evidence:

- **Three of six criteria require reformulation** (locality, determinism, envelope tightness). They cannot be applied in their continuum wording without referent-mismatch (derivatives, continuous dependence, solution-saturation).
- **Three of six steps require adaptation** (Steps 2, 3, 4 — the three-mode extraction engine). Each was built to extract constraints from a continuum governing equation.
- **The determinability boundary and finite reach enter the criterion set** through determinism, which cannot be stated for the substrate without a reach-bounded clause.

The other half transfers directly: minimality, generative sufficiency, and structural optimality need no reformulation, and Steps 1, 5, and 6 apply directly. So the extension required is **bounded and specific**, not a wholesale rebuild.

**The extensions required, listed explicitly:**

1. **A graph-local restatement of Locality** — locality defined over bounded adjacency, with finite reach recognized as a locality feature.
2. **A substrate-level Determinism criterion** — forward determinism with three clauses: generic uniqueness of the stability-score maximizer; reach-bounded determination (data within the decoupling-surface horizon determines forward evolution within it); stable dependence in a discrete configuration metric. No backward-determination requirement.
3. **A discrete Envelope-Tightness criterion** — saturation by explicit configurations, predicated on a prior definition of the discrete envelope.
4. **Discrete-substrate definitions for Steps 2–4** — the envelope (Mode 1), extremal dynamics (Mode 2), and constraint surface (Mode 3) restated to extract constraints from a maximization rule over a participation graph rather than from a continuum governing equation.

These four extensions are the prerequisite for a non-distorting evaluation. With them in place, Phases B–G run as a standard AD evaluation against the extended criteria; without them, the continuum criteria would be applied to an object they were not written for, and any verdict would be an artifact of the mismatch rather than a finding about the substrate.

**Neutrality note.** That the decision is (B) is itself a substantive, neutral result: it says the ED substrate is a genuinely *new kind of object* for AD — the first discrete relational substrate it has been asked to evaluate — and that evaluating it forces AD's downward extension to be built rather than assumed. This is exactly the outcome the motivating note (`AD_Note_SubstrateBeneathTheShadow.md`) anticipated. It neither flatters nor faults the substrate; it locates the work.

---

## 6. Recommended Next Actions

Because the decision is (B), the next document is **not** Phase B. The four extensions must be drafted first, as independent statements, before the substrate is scored against them — per the circularity guard in Memo-00 §5 (criteria stated in full and independently before application).

**Documents to produce next, in order:**

1. **`Phase_A1_SubstrateLevel_AD_Criteria.md`** — the reformulated criteria. Contains the graph-local Locality, the substrate-level forward/reach-bounded/unique-maximizer Determinism, and the discrete-configuration Envelope Tightness, each stated as a general criterion for *discrete relational architectures* (not for ED specifically), so that the criteria are domain-general and not reverse-engineered to fit the substrate.

2. **`Phase_A2_DiscreteExtraction_Modes.md`** — the discrete restatements of Modes 1–3: how to extract the envelope, extremal dynamics, and constraint surface from a maximization rule over a participation graph. This is the methodological extension that makes Steps 2–4 runnable.

Once both are filed and reviewed, the evaluation proceeds:

- **Phase B** — Architectural Specification (Step 1): enumerate the substrate's primitives, update rule, channels, and candidate invariants, against the now-extended methodology.
- **Phases C–E** — Envelope, extremal dynamics, constraint surface (Steps 2–4), using the discrete extraction modes.
- **Phase F** — Criteria evaluation (Step 5): the six criteria — three transferred, three reformulated — applied to the substrate, with PASS/CONDITIONAL/FAIL verdicts and a constraint census.
- **Phase G** — Generalization (Step 6): new pole or cross-domain invariant; integration with the determinability-boundary measurement and the FS parallel.

**Immediate next action:** draft `Phase_A1_SubstrateLevel_AD_Criteria.md` — the three reformulated criteria, stated independently and in full, as general criteria for discrete relational architectures.

---

*End of Phase A. Decision: (B), AD requires four bounded substrate-level extensions before evaluation. The extensions are named; the next document drafts the reformulated criteria. Phase A assesses AD's applicability; it does not evaluate the substrate.*
