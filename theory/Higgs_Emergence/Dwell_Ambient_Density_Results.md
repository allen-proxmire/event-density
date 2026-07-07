# Test 2 — pre-set ambient density bump, certified rule unmodified — results

**Date:** 2026-07-06
**Status:** RUN. Confirms the prediction cleanly — plain ambient density does not reproduce the field-decay probe's slowing signature. This sharpens, rather than weakens, that result.

## The question

Named in `Dwell_To_GaugeBoson_Coupling_Scoping.md` as the second cheap diagnostic: does a pre-set region of elevated ambient density, using the certified update rule completely unmodified (no new field term at all), produce genuine slowing near it — or does it behave like E1's already-established negative (channeling/termination, not a real dispersion gap)?

**Prediction stated before running:** should reproduce E1's negative, not the field-decay probe's clean bump. Reason: the field-decay probe's positive result came from an ingredient that treats the self-loop (dwell) candidate *asymmetrically* from neighbor (advance) candidates — favoring "stay" specifically, growing near a source. Plain ambient density, read through the certified, unmodified Coh/Str/Grad calculation, applies the *same* `rho_star` target to every candidate regardless of whether it's the self-loop or a neighbor — there's no built-in reason for it to single out staying over advancing.

## Result — confirmed exactly as predicted, on both counts

**With extinction off:** zero effect. Dwell rate is exactly 0.0000 in every distance bin near and inside the bump, at both tested amplitudes (2.0 and 5.0). Overall velocity is identical to the flat-background control (0.896 both). The front passes straight through as if the bump weren't there.

**With extinction on (the certified default threshold):** the front dies before it even reaches the bump. `extinguished_frac = 1.00` in every run — and the position data shows the front is extinguishing roughly 20-30 hops *before* the bump center, not within it. This is E1's finding exactly: elevated density triggers termination, not slowing.

## What this means

**The field-decay probe's positive result was not "ambient crowding in disguise."** It genuinely required a new kind of ingredient — something that makes *staying* specifically more attractive than *advancing*, as a function of distance to a source — not just "more density nearby," which the substrate's existing, symmetric Coh/Str/Grad calculation cannot produce on its own. This sharpens rather than weakens the open question from `Dwell_Field_Decay_Results.md`: whatever would ground that asymmetric, distance-decaying preference has to be a genuinely new mechanism, not a relabeling of density elevation ED's rules already handle.

## Relationship to prior results

Confirms E1 (`E1_MassFromStructure_Results.md`) generalizes to the self-loop-enabled substrate: patterned/elevated density still gives channeling or termination, never a real dispersion gap, whether or not dwelling is structurally possible. Does not touch the field-decay probe's own result (`Dwell_Field_Decay_Results.md`), which used a fundamentally different, asymmetric ingredient — that result stands, unweakened, and this test explains precisely why it needed to be asymmetric in the first place.
