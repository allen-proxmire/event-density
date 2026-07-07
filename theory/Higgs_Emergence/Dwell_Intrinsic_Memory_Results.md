# Intrinsic-memory probe — results

**Date:** 2026-07-06
**Status:** RUN, confirmed over long runs. The strongest positive result of the night's whole Higgs/mass line — genuine, stable, bounded slowing, caused entirely by a chain's own carried history, no external reference position anywhere. Still requires new state (honestly named) and free coupling parameters — read the scope section before treating this as more than it is.

## The question

The fourth-pass structural finding (`V5_Envelope_Shape_From_P11_Scoping.md`) established the certified substrate has no channel for a chain's own history to be both carried forward *and* actually read by its movement rule — the two candidate channels (orientation, density) each have only one of those two properties, never both. The direct fix, and the most honest next test: build a third channel that genuinely has both, and see whether real (not faked) memory produces mass-like behavior on its own.

## What was built

A new, chain-carried scalar (`chain_mem`), tracked outside the certified `NodeState` object (so the certified code itself is untouched — this is an addition, not a modification). At every commit — dwell or advance, treated identically — the value updates by `new_mem = decay·old_mem + 1`, and is carried forward to whichever node the chain commits to next, exactly the way `orientation`'s transverse component already is. The one new piece of coupling: the self-loop candidate's Sigma value gets a bonus proportional to the chain's *own* current `chain_mem` — no fixed source position anywhere in the code, no reference to any other chain's history. Everything else (`compute_candidates`, `compute_sigma`, `apply_tiebreak`, `commit()`) reused verbatim from the certified module.

## Result

**With no fade (`decay=1.0`):** memory grows without bound, and velocity keeps falling continuously across the whole run (0.56 → 0.31 → 0.25 → 0.21 → 0.20 → 0.17 → 0.16 → 0.15, no sign of leveling off) — runaway, not mass. Ruled out as the right regime, exactly as predicted before running: real mass doesn't keep growing.

**With fading memory (`decay<1`):** the result changes qualitatively, not just quantitatively. Memory converges to a fixed steady-state value (as it must, algebraically, for any `decay<1`), and — this is the finding — **velocity converges too**, dropping from near-ballistic (~0.9) down to a stable plateau and then *staying there*. Confirmed over a much longer run (8000 steps, 6 seeds, `decay=0.95`): velocity drops through an initial transient (windows of 200 steps: ~0.8-0.9 → ~0.6-0.7) and then holds essentially flat for the rest of the run (last 1000 steps averaged: v_eff = 0.720 ± 0.020 across seeds). Every run reached the far boundary — full survival throughout, no stalling, no dying.

**The coupling strength and the fade rate trade off as expected, and sensibly.** A weaker coupling (`k_mem=0.05`) needs a slower fade (`decay=0.95`, steady-state memory ≈20) to produce a visible effect; the same coupling with a faster fade (`decay=0.8`, steady-state memory ≈5) shows no effect at all — but a stronger coupling (`k_mem=0.2`) at that same fast fade reproduces the same kind of plateau. What matters is the product of coupling strength and steady-state memory level, not either alone — internally consistent, not an accident.

## Why this is the strongest result of the night

Every earlier positive result in this line needed something external: the field-decay probe needed a fixed reference position (not itself justified); the dwell-channel's original `kg>ks` needed an unexplained coefficient asymmetry. This result needs neither. It's the first mechanism where the "heaviness" is a property the chain **carries with it**, not something tied to a place in space or an arbitrarily-tilted default — which is a much closer match to what mass actually is (an intrinsic property of a particle, not a location-dependent one).

## Honest scope — what this is and isn't

**This required adding new state to the certified reference substrate — named honestly, not smuggled in.** `chain_mem` is not something P02–P13 already provide "for free" — it's a genuinely new channel, of exactly the kind the fourth-pass finding said would be needed to close this gap. Whether *this specific* channel (a simple exponential-decay accumulator) is the *right* one, or whether it can be derived from existing primitives rather than added as new structure, is untested.

**Two free parameters, same pattern as everywhere else tonight.** The coupling strength (`k_mem`) and fade rate (`decay`) were both chosen to get a working demonstration — neither is derived. This is the same "form works, specific value not yet grounded" pattern found repeatedly tonight (`kg>ks`, the field-decay length), not a new kind of gap.

**This is still one lone particle, not a Higgs mechanism.** No gauge coupling, no symmetry breaking, no condensate — this shows a single chain can carry genuine, bounded, intrinsic sluggishness. Whether *this* mechanism (rather than the earlier field-decay one) can be extended toward an actual gauge-boson-mass story is a fresh, unexplored question — the four missing pieces named in `Dwell_To_GaugeBoson_Coupling_Scoping.md` (no gauge-boson object in the sim, H1's unfinished vertex, the field-vs-condensate mismatch, no standing background ever built) still all apply here as much as they did before; this result doesn't touch any of them directly, it solves a different, narrower problem (does *any* real, chain-carried mechanism give bounded intrinsic mass at all — yes).

## Attempt to reduce the two free parameters (same session, 2026-07-06)

Tried to eliminate the coupling strength `k_mem` by folding memory into the *existing* coherence weight `kc` instead of giving it its own new weight — shift the self-loop's coherence *target* by the chain's accumulated memory (`target = rho_star + chain_mem`, with `chain_mem` growing by `coeffs.increment`, the same quantity `rho` already grows by) rather than adding a separately-weighted bonus term. P12's own canonical definition is a fixed three-term functional; a fourth, independently-weighted term is more new structure than strictly necessary if it can be avoided.

**Result: failed, honestly.** At every ordinary fade rate tested (`decay = 0.9, 0.95, 0.98`), this version showed *no* slowing effect at all — velocity stayed at the pure-ballistic baseline (~0.97) regardless of decay rate, a flat, uninformative result across values that should have differed if the mechanism were doing anything. Only the extreme, unphysical `decay=1.0` case showed any effect, and it was messy and inconsistent across seeds (most runs failed to even reach the chain's far boundary within budget), not the clean plateau found before.

**Why it fails, understood, not just observed:** shifting the *target* a chain compares against is not mechanically equivalent to directly rewarding staying. When accumulated memory pushes the target far from where local density actually sits, it makes the self-loop's coherence term *worse* (density is now far from the shifted target), not better — the opposite of what's needed to make dwelling attractive. The original design's directly-additive bonus avoided this because it rewards staying unconditionally, regardless of density. **`k_mem` is not redundant with `kc` — it does genuinely separate work, and this specific economy attempt doesn't get to keep it.**

**The fade rate, by contrast, is not actually a new unknown — it should be named plainly as what it already is.** V1's own canonical definition (`Paper_089_V1Kernel.md`) is explicitly "chain C's response... to substrate-level perturbations at the same chain's earlier locus" — exactly what `chain_mem` implements. The fade rate here isn't a fresh, unexplained number invented for this probe; it's the corpus's own already-acknowledged, already-inherited V1 memory time τ_V1, now identified with a concrete, working piece of code for the first time (Paper_090 confirms no paper anywhere has implemented V1/V5 in running code before tonight). This doesn't derive τ_V1's *value* — Paper_089 itself says that value stays inherited, same as every other regime-specific τ_V5 identification in the corpus — but it means there is exactly **one** genuinely new free parameter here (`k_mem`), not two.

## Tier verdict

**CANDIDATE, positive, confirmed over long runs.** One parameter (`k_mem`, the coupling strength) is a genuine, separate, new addition — an honest attempt to eliminate it by reuse failed cleanly. The other (the fade rate) is not new at all — it's τ_V1, already inherited in the corpus, now attached to working code for the first time. The strongest result in the night's whole Higgs/mass probe line: genuine, bounded, survivable, intrinsic slowing, no external reference position, no faked field. Not FORCED, and not yet connected to an actual gauge/EWSB mechanism.
