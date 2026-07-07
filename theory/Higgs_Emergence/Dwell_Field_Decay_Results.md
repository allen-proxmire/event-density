# Field-decay probe (AP's proposal) — results

**Date:** 2026-07-06
**Status:** RUN. First correct-sign mass signature in this whole line of probes — genuine slowing near a source, fading with distance. Proof-of-concept only; the "field" itself is hand-inserted, not yet derived. Read the honest scope before citing this as more than that.

## Where this came from

AP's proposal, verbatim: "I kind of see a chain's memory as diminishing away from its propagation." Test 1 (`Dwell_Trail_Detection_Results.md`) had found a front's dwell trail is real and detectable, but *permanent* — commit density can never shrink (P11's irreversibility), so already-visited ground stays elevated forever and repels a later front, the wrong sign for mass. The proposal reframes the question: not "does old, permanent history stick around forever," but "does a chain's *live* influence fade with distance from wherever it currently is" — a genuinely different, physically better-motivated hypothesis, since a real field (unlike a permanent trail) is supposed to be strong near its source and weak far away, not frozen wherever it happened to visit in the past.

## First attempt was invalid, caught before trusting it

The first version tested a front on a chain with **no self-loop** at all. Without a self-loop, a front can only ever step left or right — it has no "stay in place" option, so it is mechanically incapable of slowing down; a field bonus there could only ever bias *which direction* it stepped, never *how fast*. That version's control result (v_eff=0.702 instead of the expected ~1.0) was a symptom, not a real finding — this was a hand-rolled reimplementation of the update loop rather than reusing the certified functions directly (`compute_candidates`, `apply_tiebreak`), the exact mistake this program's own standing practice exists to catch. Rebuilt to reuse the certified functions verbatim, confirmed the control matched expectations, and — more importantly — redesigned the actual test to combine the field with the confirmed **self-loop dwell mechanism**, since dwelling (not direction-biasing) is the only way a front can genuinely slow down in this substrate.

## What was built

A front moves on a chain with self-loops (the confirmed dwell mechanism, at the certified default coefficients — which in isolation gives at most one free dwell then permanent advance, i.e. "light"/near-ballistic far from anything). One new, additive term is added, applying **only to the self-loop candidate**: a bonus that grows the closer the front's current position is to a fixed reference ("source") location, decaying exponentially with distance — `k_field * exp(-|position - source| / xi)`. Zero at `k_field=0` (exact recovery of the confirmed, already-tested certified dwell rule). Everything else — `compute_candidates`, `compute_sigma`, `apply_tiebreak`, `commit()` — reused verbatim from the certified module.

## Result

| | control (no field) | k_field=2, xi=15 | k_field=5, xi=15 | k_field=5, xi=30 |
|---|---|---|---|---|
| overall v_eff | 0.896 | 0.798 | 0.705 | 0.577 |
| overall dwell fraction | 0.0028 | 0.0746 | 0.1738 | 0.3034 |

And, decisively, dwell rate **as a function of distance to the source**: essentially zero far away, rising smoothly, peaking almost exactly at the source, and falling back to zero on the far side — a clean, symmetric bump centered on the source, wider when `xi` (the decay length) is set wider. At `k_field=5, xi=15`: dwell rate goes 0 → 0 → 0 → 0.29 → 0.50 → 0.57 → **0.58 (at the source)** → 0.50 → 0.33 → 0 → 0, reading outward from −60 to +40 hops away.

**This is the correct-sign signature.** The front genuinely slows down (dwells more, lower net velocity) as it nears the source, and speeds back up (dwells less, near-ballistic) as it moves away — fading with distance, not frozen in place the way Test 1's permanent trail was. Turning the source strength up (`k_field`) makes the slowing more pronounced everywhere; widening the decay length (`xi`) makes the region of influence broader. Both behave exactly the way a real field's strength and range should.

## Honest scope — what this proves and doesn't

**This is a proof-of-concept that the shape works, not a mechanism ED derives.** Two things were assumed, not derived, and both need to be named plainly:

1. **The "source" was a fixed reference point I hand-picked, not another chain's actual, dynamically-computed live position.** The next honest step is replacing the fixed `source_pos` with a *second, genuinely active, moving* chain, so the field bonus reads that chain's real current position each step (not a hardcoded number) — this test stands in for that, but doesn't yet build it.
2. **The field bonus itself — its existence, its exponential-decay shape, and its magnitude/length-scale — is a new ingredient I inserted to test the hypothesis, not something derived from P02/P04/P05/P07/P08/P11/P12.** It answers "if something like this existed, would it produce the right shape" (yes, cleanly) — not "does ED's substrate actually produce something like this." That's the same category of open question as the `kg > ks` dial from the earlier probe: admissible to test, not yet grounded.

## Update 2026-07-06 — checked whether P05, or the substrate's own natural length scale, could ground this

**P05 (polarity-transport, ED's actual gauge-content primitive) does not help.** Checked directly: `Gauge_02_P05_Transport_Is_a_LatticeGaugeConnection.md` is exhaustively edge-local — one hop at a time, no notion anywhere of influence reaching outward from an active chain. Ruled out cleanly, not just unexplored.

**The best real candidate is V1/V5's kernel machinery** (`Paper_089_V1Kernel.md`, `Paper_090_V5Kernel.md`) — an actual corpus theorem (N1) establishing a bounded, decaying-with-distance envelope at substrate scale `ℓ_ED`, extended cross-chain by V5. This is a genuine, existing precedent for "strong near a source, weaker far away," not something invented for this probe.

**But the theorem only specifies an admissible *class* of shapes (bounded, decaying, excludes both zero-width and infinite-width) — not one specific formula, and not a scale bigger than `ℓ_ED`.** Tested directly: rerunning the probe with the decay length set to the substrate's own actual scale (`xi=1`, one hop, matching `ℓ_ED`) instead of the arbitrary wide values used above (`xi=15-30`) —

| xi (hops) | k_field | overall v_eff | peak dwell rate |
|---|---|---|---|
| 1 | 5 | 0.882 | 0.60 |
| 1 | 15 | 0.865 | 0.71 |
| 1 | 50 | 0.828 | 0.85 |
| 4 | 50 | 0.663 | 0.87 |

At `xi=1`, even with a very strong source, the dwelling spike is real but confined to essentially one site — overall velocity barely moves off the control value (0.896). The dramatic, macroscopically-relevant slowing found earlier required a decay length many times wider than the substrate's own natural scale, with nothing in ED explaining why it should be that much larger. **This is the same category of gap as `kg > ks`: the shape of the mechanism is right, but the specific scale needed to make it matter has no primitive-level grounding — it would have to be imported from outside, exactly like every other free coefficient found tonight.**

## Tier verdict

**CANDIDATE, proof-of-concept confirmed, not yet derived.** This is the first result in the whole Higgs/EWSB probe line that gets the *sign* right — a passing front genuinely gets heavier near an active source and lighter far away, rather than the earlier finding's opposite (repelled by permanent history). The real next question this opens: can a live, distance-decaying influence like this be grounded in ED's own primitives (most plausibly via P05's polarity-transport, since that's ED's actual "gauge content" mechanism, or via some spatial-reach property of P04's bandwidth), or is it, like `kg > ks`, a free assumption with no existing support either way. That check hasn't been run yet.

## Relationship to prior results

Does not contradict or retract `Dwell_Trail_Detection_Results.md` — that test (permanent, undecayed history) and this one (a live, decaying field) are testing genuinely different hypotheses, and both are now honestly on the record: one gives the wrong sign, the other gives the right sign, for two different reasons. Both stay open findings in the corpus, not superseding each other.
