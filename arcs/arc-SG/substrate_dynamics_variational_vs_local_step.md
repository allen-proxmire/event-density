# Substrate Dynamics: Variational vs Local-Step

**Date:** 2026-04-27
**Type:** Substrate-foundations analysis (single-file memo, no arc numbering)
**Sources:** ED-07 §5.1 criteria (b) and (c); ED-I-06 §6. Only these two passages are treated as authoritative for this analysis.
**Status:** Resolves Fork F3 from the substrate-attempt analysis. **Verdict: ED's substrate dynamics are local-step at the substrate level, with variational language in ED-07 §5.1 being a global description of behavior emerging from local-step rules.** The two interpretations are not contradictory; they describe the same dynamics at different ontological levels (substrate vs coarse-grained). For galactic-scale channel dynamics, the local-step interpretation is the appropriate working framework, with channels understood as emergent collective structures arising from many micro-events making local choices in a shared participation environment.

---

## 1. The two interpretations, precisely stated

### 1.1 Variational interpretation

A chain (or system) γ is described by a path between specified endpoints. The principle of least disruption is taken as a path-functional:

> The "inertial path" is the path γ that extremizes a functional `S[γ]` whose integrand encodes ED-07 §5.1 criteria — internal coherence (b) and participation strain (c) along the path.

Under this reading:
- The path is a global object — its full trajectory matters for the variational evaluation.
- Selection among possible paths requires comparing functional values across the path space.
- The "principle of least action" analogy from ED-07 §5.1 is interpreted literally: ED's dynamics is a Lagrangian variational principle.

### 1.2 Local-step interpretation

Micro-events propagate one at a time. At each propagation step, the next micro-event state is chosen from the currently-available options:

> At each micro-event step, the chain extends to the next state that maximizes local internal coherence (b) and minimizes local participation strain (c), among the states available given the current participation environment.

Under this reading:
- Decisions are local — each step depends only on the current state and immediate neighborhood.
- Channels emerge as stable persistent structures from the collective behavior of many micro-events all making local choices.
- ED-I-06 §6's phrasing ("micro-events follow the most stable participation channels available to them") is interpreted literally: dynamics is causal/Markovian/local.

---

## 2. What each interpretation says about the four sub-questions

### 2.1 What counts as a "stable channel"

**Variational:** A stable channel is a path that is a stationary point of the action functional `S[γ]`. Stability is a property of the *whole path* — small perturbations to any segment increase the functional. The channel exists as a unified global object.

**Local-step:** A stable channel is a sequence of locally-stable transitions that *self-consistently closes* — the next-state-chosen at each step happens to produce a continuation that the previous step's chooser would also have selected. The channel exists as a *consistency pattern* in many independent local choices, not as a global object that anyone "selected."

### 2.2 How channel stability is evaluated

**Variational:** Globally. The functional `S[γ]` is computed over the entire path; stability is checked by varying the path and seeing if `S` is at a stationary point.

**Local-step:** Locally. At each micro-event step, only the current state and immediate options matter. Stability of a channel as a global structure is *emergent* — nobody computes it directly; it emerges from many local-step choices being mutually consistent.

### 2.3 How channel structure scales with enclosed mass M_b

**Variational:** Channel structure is determined by the action functional. Scaling with M_b is set by how M_b enters the functional. If `S[γ]` depends linearly on M_b (mass-density source linearly in Lagrangian), channel structure scales linearly. If non-linearly, otherwise. The scaling is a property of the chosen Lagrangian.

**Local-step:** Channel structure emerges from many local choices. Scaling with M_b is determined by *how the local stability landscape changes* as the participation environment around increasing M_b changes. This can produce nonlinear scaling **without any nonlinear functional** — self-organization in local-step systems frequently produces emergent scaling laws (universality classes, critical exponents) that aren't visible in the local rules.

This is the structurally crucial difference. Variational systems get their scaling from their Lagrangian. Local-step systems get their scaling from collective self-organization. **The latter can produce scaling exponents that no Lagrangian-extremization would have produced from the same local rules.**

### 2.4 Support for global channel topology

**Variational:** Channels are global objects by construction. Topology is intrinsic. Supports global channel topology naturally.

**Local-step:** Channels emerge as stable patterns from local dynamics. Their topology is *emergent*, not built in. Supports global channel topology via emergence — and additionally supports topological transitions and reorganizations (when the participation environment changes, channels reorganize through cascades of local-step adjustments).

Both support topology. Local-step additionally supports topological *dynamics* (reorganization), which is relevant for cosmic structure formation, galaxy mergers, etc.

### 2.5 Support for cosmic-environment coupling

**Variational:** Cosmic-environment coupling enters as a term in the action functional — typically a "background curvature" term or a non-local kernel. Coupling is built into the chosen Lagrangian.

**Local-step:** Cosmic-environment is part of the participation environment that determines local stability at each step. As cosmic-environment varies, local stability at each step varies, and channels self-organize differently. Coupling is intrinsic to the local-step framework, not a separate term.

Local-step supports cosmic-environment coupling more naturally, because the coupling is just "the participation environment includes cosmic-environment contributions." No separate machinery needed.

### 2.6 Support for √M_b scaling (as required by BTFR)

**Variational:** Requires the action functional to have a structure that, upon extremization, produces √M_b scaling in the asymptotic-channel velocity. This requires a non-quadratic kinetic term (MOND-style μ(|∇φ|²) modification) or a sublinear coupling. Both are postulates within the variational framework.

**Local-step:** Could produce √M_b scaling through self-organization, *if* the local stability rules and cosmic-environment coupling combine to give that universality class. This is empirical to the local rules — not derivable in advance without committing to specific substrate dynamics, but also not requiring a postulated nonlinear functional.

The local-step framework is **more permissive** of √M_b scaling, because the scaling can emerge without being put in by hand. But it doesn't *guarantee* √M_b scaling; that depends on what the substrate rules actually are.

### 2.7 Support for a universal acceleration scale a₀ ~ c·H₀

**Variational:** a₀ is built into the Lagrangian as a parameter (e.g., MOND's a₀ in the interpolation function). It can be set to c·H₀ but the value is a postulate.

**Local-step:** a₀ emerges as the natural scale where local-stability transitions from baryon-environment-dominated to cosmic-environment-dominated. Cosmic-environment scales are set by cosmic-evolution time scales (~1/H₀); a₀ ~ c·H₀ falls out structurally, *not* as a postulate.

Local-step supports a₀ ~ c·H₀ as a *derived* rather than *postulated* quantity. This is the cleanest structural advantage of local-step over variational for the BTFR question.

---

## 3. Direct textual analysis

### 3.1 ED-07 §5.1 (b) and (c)

The relevant text:
> "(b) the system's internal micro-event structure remains maximally coherent
> (c) participation with the surrounding field is least strained"

Item (b) is about *internal* structure — the chain's own micro-event coherence. Item (c) is *relational* — strain between chain and surroundings.

Neither (b) nor (c) is intrinsically variational or local-step. They state criteria; they don't specify how the criteria are evaluated. The variational reading of ED-07 §5.1 comes from the surrounding context ("ED analogue of the principle of least action"), but (b) and (c) by themselves are interpretation-neutral.

**Important asymmetry:** "maximally coherent" (b) is a maximum-property — at each moment, coherence has a value. It can be evaluated locally without lookahead. "Least strained" (c) is similarly a current-state property. **Both criteria admit local evaluation.** The variational reading interprets them as *integrated along a path*; the local-step reading interprets them as *evaluated at each step*. ED-07 §5.1's text doesn't force either interpretation — but neither does it require integration.

### 3.2 ED-I-06 §6

The relevant text:
> "Micro-events follow the most stable participation channels available to them. When the participation environment changes, the system experiences a force."

Two phrases are decisive:
- **"available to them"** — present-tense, suggests options currently accessible to the micro-event. This is local-availability language, not global-path-comparison language.
- **"the most stable channels"** — channels (plural) that are available; the micro-event follows the most stable. This implies a local *selection* among present options, not a *path-extremization* over all possible paths.

The phrasing is consistently local. There is no language suggesting global path comparison.

**ED-I-06 §6 commits to local-step, explicitly.**

### 3.3 The relationship between ED-07 §5.1 and ED-I-06 §6

ED-07 (February 2026) phrases the principle in classical-physics-analogous language ("principle of least action"), which carries variational connotations. ED-I-06 (also February 2026, but later in the I-series) is more architecturally specific and commits to local-step phrasing.

**Both can be true simultaneously** if we accept the standard physics result that variational principles can emerge from local dynamics. Hamilton's principle in classical mechanics is equivalent to Newton's local equations of motion. The substrate is local; the variational description is a global re-encoding.

Under this synthesis: ED's substrate dynamics is local-step. The variational framing in ED-07 §5.1 is a *coarse-grained or emergent description* — useful for analyzing global stable structures, but not the substrate-level statement of dynamics.

This is the structurally clean reading. It preserves both texts and is consistent with how local-vs-variational works in known physics.

---

## 4. Compatibility with ED's known results

### 4.1 GR-3A (eikonal-limit geodesic worldlines)

GR-3A states that free chains in the eikonal (high-frequency) limit follow geodesics. In standard physics, geodesics admit both derivations:
- **Variational:** geodesics extremize proper time (Hamilton's principle for free particles).
- **Local-step:** geodesics are paths along which a particle's local equation of motion is satisfied (parallel transport).

Both readings reproduce GR-3A. **GR-3A does not pin down the fork.**

### 4.2 Theorem N1 (V1 finite-width vacuum kernel)

N1 is a result about the vacuum kernel structure. It uses field-theoretic/QFT language because that's the natural coarse-grained description. As a *coarse-grained* result, N1 doesn't directly speak to substrate dynamics. **N1 is consistent with either fork.**

### 4.3 Tension with the four-arc closure (DM.0/1/G/MCD)

The four arcs derived linear field equations from variational Lagrangian constructions. Under the variational reading, these are direct substrate-level analyses, and the linearity wall is a substrate-level result.

**Under the local-step reading, the four arcs are coarse-grained analyses of an emergent description, not substrate-level dynamics.** The linearity wall applies to the coarse-grained description, not necessarily to the substrate.

This is structurally consistent with what ED-I-06 actually says (fields are emergent, coarse-grained summaries). The four arcs were doing field theory on top of ED, not substrate-level ED. **Adopting the local-step reading is consistent with — and in fact required by — taking ED-I-06 seriously as the substrate-level articulation.**

---

## 5. Structural verdict

> **ED's substrate dynamics are local-step.** ED-I-06 §6 explicitly commits to this in language that admits no other reading ("micro-events follow the most stable participation channels available to them"). ED-07 §5.1's variational-flavored phrasing ("ED analogue of the principle of least action") is naturally read as a coarse-grained emergent description rather than a substrate-level commitment.
>
> **The two interpretations are compatible** under the standard physics result that variational principles can emerge from local dynamics. The variational global description is a useful reformulation, not a competing substrate framework.
>
> **For galactic-scale channel dynamics, the local-step framework is the appropriate working level.** Channels emerge as collective self-organized structures from many micro-events making local stability-maximizing choices. This framing:
>
> - Naturally supports cosmic-environment coupling (cosmic structure is part of the participation environment that shapes local stability).
> - Naturally produces a₀ ~ c·H₀ as the transition scale (where baryon-environment-dominated local stability gives way to cosmic-environment-dominated local stability) — derived, not postulated.
> - Permits but does not guarantee √M_b scaling — the scaling depends on collective self-organization properties of the local rules, which are not yet articulated at sufficient detail.
> - Decouples the BTFR question from the four-arc linearity wall (the wall is a property of the field-theoretic coarse-grained description, not of the substrate).

The fork resolves cleanly. Local-step is the substrate dynamics. The four-arc closure is recharacterized as a refutation of one *coarse-grained description* of ED-substrate dynamics, not a refutation of ED-substrate dynamics itself.

---

## 6. Implications for the substrate-level gravitational analysis

Three structural consequences flow from this verdict:

**(I-1) The substrate-level question for BTFR reframes from PDE derivation to self-organization analysis.**

Under variational, the question would be: "what action functional gives slope-4 BTFR upon extremization?" The four arcs answered this: no canonical Lagrangian gives slope-4 without postulated nonlinearity.

Under local-step, the question is: "what local stability rules produce a self-organized channel structure with √M_b scaling at galactic scales?" This is a different mathematical question — closer to critical phenomena, statistical mechanics, and emergent universality than to variational calculus.

**(I-2) Forks F1 and F2 (from the prior substrate-attempt analysis) are now constrained.**

- **F1 (channel-density / info-theoretic / holographic scaling):** Under local-step, F1c (holographic-style emergent scaling) is the most natural framework, because emergent universality from local rules is exactly how holographic constructions work. F1a and F1b would require postulated rules; F1c would emerge.
- **F2 (mean-field vs galaxy-specific cosmic-environment coupling):** Under local-step with self-organization, mean-field (F2a) is the natural framing — many galaxies in similar cosmic environments self-organize into similar channel structures, producing universal BTFR. The empirical universality is consistent with this; under variational, it would require additional explanation.

**(I-3) The cosmic-environment empirical anchor (Wempe-type reconstructions) connects naturally.**

Under local-step, cosmic-environment structure is part of the participation environment that shapes local stability. Wempe's reconstruction provides the actual cosmic-environment configuration for the Local Group; this configuration, fed into local-step substrate dynamics, would determine the channel structure of galaxies in the Local Group. **The empirical input becomes a tractable computational input** rather than just a confirmatory observation.

---

## 7. Open structural commitments still required

The verdict resolves which substrate-level *framework* applies. It does not specify the substrate-level *rules*. Three open commitments remain:

- **What precisely defines "stability" of a channel at substrate level?** ED-I-06 doesn't specify. Candidate readings: lowest-strain configuration, lowest-rate-of-disruption, highest-coherence-preservation, or some combination. Different readings give different self-organization dynamics.
- **What precisely defines "available channels" at a given micro-event?** This is the local stability landscape's enumeration of options. ED-I-06 implies there are multiple, but doesn't specify how many or how their availability is determined.
- **How does cosmic-environment information reach a local micro-event?** Local-step requires that cosmic-environment effects propagate to local stability assessments through some causal mechanism. This could be through long-range participation correlations, through the ED-gradient field's spatial structure, or through some other route. ED-I-06 doesn't specify.

These are foundational commitments to be made in subsequent substrate-level work. They aren't "fork choices" in the sense of F1/F2/F3 — they're more granular sub-commitments within the local-step framework that's now established as the right level.

---

## Recommended Next Step

Three concrete actions, in priority order:

1. **Articulate substrate-level rules for "channel stability" and "available channels."** This is the immediate next foundational task. Without specifying these rules, no quantitative substrate-level prediction is possible. The articulation should be minimal — the smallest commitment that captures ED-07 §5.1 (b)+(c) and ED-I-06 §6 — and explicitly distinguish what's structural (forced by the substrate ontology) from what's parametric (could in principle vary across substrate-physics realizations).

2. **Test the local-step framework on a known result first, before BTFR.** Specifically: derive Newton's law of gravity from local-step substrate dynamics in the high-baryon-density regime (where local stability is dominated by local mass distribution). If the framework correctly recovers `a = -GM/R²` from substrate rules, that validates the framework before applying it to the harder BTFR question. If it doesn't, the substrate rules need adjustment before any galactic-scale analysis.

3. **Map the cosmic-environment coupling explicitly.** Use Wempe-type reconstructions of the Local Group as concrete empirical input. With substrate-level rules defined (per item 1) and Newton recovered (per item 2), feed the Local Group's cosmic-environment structure into the local-step dynamics for a Milky Way-mass galaxy. Compute the predicted rotation-curve at large R. Compare to observed rotation curve. This is the first concrete test of whether substrate-level local-step ED, fed real cosmic-environment data, produces galactic-scale BTFR-compatible behavior.

These three steps are sequential. Item 1 is foundational and must come first. Item 2 is a sanity check before any speculative work. Item 3 is the first empirical test. Together they constitute the minimal program for moving substrate-level ED gravity from "structurally reframed" (this memo) to "concretely derivable" (subsequent work).

The four-arc closure is now correctly understood as ruling out the field-theoretic coarse-grained description of ED gravity. It does not rule out substrate-level ED gravity. **Substrate-level ED gravity remains an open structural question, with the local-step framework as the established substrate dynamics, and items 1–3 above as the path forward.**

Status: complete.
