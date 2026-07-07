# Coupling the dwell-channel mass mechanism to gauge bosons — scoping (not built)

**Date:** 2026-07-06
**Status:** SCOPED, NOT YET BUILDABLE. Four separate missing pieces named, not one. This memo answers "is this a well-posed next step," not "here is the mechanism."

## The question

The dwell-channel probe (`Dwell_Channel_Mass_Results.md`) showed a single, isolated front can propagate at a real, tunable, surviving sub-ballistic velocity — a genuine mass-like effect for one particle. The natural next question: can this be coupled to gauge bosons, the way Arc Q's H1 candidate proposed (a scalar field's vacuum value, coupled via `|D_μφ|²`, giving gauge bosons an effective mass `m² ∝ g²⟨φ⟩²`), so the mechanism explains why particles like the W/Z bosons are heavy — not just why one lone front can move slowly?

## Verdict: not yet well-posed. Four separate missing pieces, all simultaneous.

**1. No gauge-boson-like object exists in the certified simulator at all.** The running code tracks exactly two things per node: commitment density (`rho`) and orientation. Orientation — the one internal degree of freedom that could plausibly stand in for a gauge/internal direction — is hard-invariant **invisible** to the Sigma calculation that decides how anything moves (`sigma.py`'s own docstring: "MUST NOT read NodeState.orientation"). This was already independently found in the H1 blockage (`H1_Leg_Scoping.md`): "the natural gauge sector in ED (orientation) is Σ-blind... it can carry no Σ-visible mass." There is nothing in the running code today that a gauge boson could even be.

**2. H1's own math was never finished, independent of this new work.** `higgs_mechanism_scoping.md`'s H1 imports the covariant derivative `D_μ` wholesale from standard QFT notation without building it from ED's own primitives. A separate paper (`Gauge_02_P05_Transport_Is_a_LatticeGaugeConnection.md`) does construct a real gauge connection from P05 (polarity-transport) + P04 (bandwidth conservation) + P11 (irreversibility) — a genuine substrate-grounded result — but that paper explicitly stops short of deriving the actual field dynamics, and nobody has ever connected it to H1's `|D_μφ|²` vertex. Two real pieces of work, never stitched together.

**3. The dwell mechanism's actual output is the wrong kind of object.** A Higgs-like mechanism needs a persistent, spatially-extended background — a field that's roughly there regardless of whether the original particle that "made" it is still around, so *other* particles can bump into it later. What the dwell mechanism produces is a single front's own local, path-dependent history — density it raised at the exact loci it visited, with no mechanism for that to reach or affect any nearby-but-unvisited locus. Whether this distinction is fatal, or whether it's fixable, is exactly what Test 1 (below) checks directly rather than by argument.

**4. Nobody has ever built a genuine standing background/condensate using only the certified update rule.** Every past attempt either hand-sets a density landscape as a starting condition rather than something the dynamics produce and sustain (E1), or requires new structure nobody has licensed yet (H2's "refined, spatially-patterned" version — flagged CANDIDATE, never built; H5, vacuum-anchored Higgs — deferred to unclosed later stages; the retracted four-band dwell attempt). This is the same rung (`Substrate_Higgs_Emergence_Scoping.md` calls it "E2 — Formation") that the corpus's own plan says not to attempt before a mechanism is grounded — and even the one that was grounded (E1) came back negative.

## Two cheap, buildable diagnostics (identified, not yet run at time of scoping)

- **Test 1** — does a *second* front, passing through the *same* nodes later, notice anything different from a fresh, never-visited chain? Cheapest possible check of whether the dwell trail is a real, lasting, detectable effect at all, before asking whether it's condensate-like.
- **Test 2** — directly re-test whether *ambient* (pre-set, not dynamically produced) elevated density changes an ordinary front's velocity, reusing E1's exact methodology. Predicted negative given E1's prior result, but worth closing explicitly rather than assuming it still applies unchanged.

## Bottom line

This is not "one build away." It's four separate open pieces stacked on each other — no gauge-boson object, an unfinished H1 vertex construction, a probable category mismatch between a private trail and a public field, and zero corpus precedent for a real standing condensate built from the actual rules. Worth continuing to probe piece by piece (starting with the cheap Test 1, next), not worth a full build attempt yet.
