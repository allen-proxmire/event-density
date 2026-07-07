# Test 1 — does a second front detect the first front's dwell trail? Results

**Date:** 2026-07-06
**Status:** RUN, clean, decisive answer — but the answer points the opposite direction from what a Higgs-like mechanism needs.

## The question

`Dwell_To_GaugeBoson_Coupling_Scoping.md` named this as the cheapest diagnostic before attempting anything bigger: does a *second*, later front notice anything different about ground a *first* front already dwelled through — or is the dwell trail completely private bookkeeping, invisible to anything else?

## What was built and a bug caught along the way

`dwell_trail_detection_probe.py`: one shared initial substrate state, cloned into a TRAIL copy (front 1 runs through it first) and an untouched CONTROL copy. Front 2 then runs on both, from the identical starting position, and the two runs are compared.

First attempt was invalid and is not reported as a result: front 1 never actually reached the test region within the step budget given (a scoping error — should have used the already-confirmed long-run velocity, ~0.0105 hops/step, to size the budget), and separately, this dwell regime does not reliably extinguish, so front 1 was still active when front 2 started, silently mixing the two trajectories together. Both bugs fixed (budget corrected to the right order of magnitude; front 1 explicitly deactivated before front 2 starts; a hard runtime check added so this class of bug cannot silently reoccur) before trusting any numbers.

## Result, corrected run (10 seeds)

**Part A — is the ground actually different after front 1 passes?** Yes, dramatically: mean density in the test region rises from ~0.50 (untouched baseline) to ~9.6–10.4 after front 1's trail — about 20× the background level. Expected and unsurprising (density commits are permanent by construction), but confirms the trail is a real, substantial, lasting change to the substrate, not a fleeting one.

**Part B — does front 2 react to it?** Yes, unambiguously, and by a large margin:

| | control (fresh ground) | trail (front 1 already passed) |
|---|---|---|
| effective velocity | ~0.00 (near zero, matches confirmed baseline) | 0.20–0.36 (20–36× faster) |
| dwell count (out of 800 steps) | ~785–792 (almost every step) | 2–517 (highly variable, always far lower) |
| survival | always survives | always survives |

Every one of 10 seeds shows the same pattern, no exceptions.

## What this means — precise, not glossed over

**The trail is real and detectable — Test 1's literal question is answered YES, clearly.** This closes the worry (named in the scoping memo) that the dwell mechanism's output might be completely private to the front that made it. It isn't. A later front passing through the same ground behaves measurably, dramatically differently.

**But the direction of the effect is backwards from what a Higgs-like mass mechanism needs.** A real mass-generating background makes other particles *heavier* (slower) when they move through it. What was found here is the opposite: front 2 moves *faster* through ground front 1 already dwelled on, not slower. The mechanism is straightforward once seen: a heavily-dwelled node's density is now far from the target the substrate wants (`rho_star`), so *further* dwelling there is heavily penalized (the same math that eventually forces front 1 itself to stop dwelling and move on) — front 2 experiences that same penalty immediately on arrival, and races through rather than settling in. The trail acts like ground that's "already spent," repelling further dwelling, not like a field that attracts and slows other particles the way a Higgs condensate needs to.

## Verdict

**Test 1 passes on its own narrow question (the trail is real, not private) and fails the broader goal it was meant to serve (does this look like a mass-giving condensate).** The effect is real, large, and reproducible — genuinely interesting on its own terms — but it has the wrong sign for what gauge-boson-mass coupling would require. This doesn't reopen the four missing pieces named in the scoping memo; if anything it sharpens piece (iii): the dwell trail is not just "a different kind of object than a condensate" (as scoped), it actively behaves like the *opposite* of one when tested directly.

## Honest scope

This tests one specific hypothesis (front 2 directly re-treading front 1's exact path) under one specific coefficient regime. It doesn't rule out every possible way density history could matter to a different front — only this one, direct, same-path test. Test 2 from the scoping memo (ambient pre-set density, not dynamically produced by a prior front) remains a separate, un-run question.
