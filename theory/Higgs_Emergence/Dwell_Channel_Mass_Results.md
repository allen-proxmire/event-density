# Dwell-Channel Mass Probe — Results

**Date:** 2026-07-06
**Status:** Probe run and confirmed. A genuinely new, positive structural finding — not a full EWSB/Higgs derivation. Read the scope section before citing this anywhere.

## The question

H1 and H2 (Arc Q's two most promising Higgs candidates) both failed on the certified substrate because its update rule is **ballistic-or-extinct** — a front either advances exactly one hop, or dies. Neither H1 (inserted scalar) nor H2 (patterned condensate, tested directly in `E1_MassFromStructure_Results.md`) could produce a real mass, because a real mass needs a *third* option: propagation that continues, just slower (a dispersion gap), not propagation that stops (extinction) or never slows (pure ballistic).

The retracted `Dwell_Question_Answer.md` tried to license this third option via a four-band P04 partition — an archived, non-canonical structure, correctly withdrawn. This probe asks the real question instead: **do canonical P02 (participation) + P03 (channel/locus indexing) + P07 (channel structure) actually forbid a channel from a locus to itself?**

They don't. Nothing in any of the three primitives requires a channel to connect two *distinct* loci — that requirement turns out to be an artifact of how the certified graph is built in practice, not something the primitives assert. `graph.py`'s `add_edge(u, v, bandwidth)` has no check against `u == v`; the class already supports a self-loop without modification.

## What was built

`dwell_channel_mass_probe.py` (same directory) adds self-loop edges to the certified substrate graph — one per node, with a tunable bandwidth — and runs the completely unmodified certified update loop (`step`/`compute_sigma`/`commit`) on it. No new term, no new coupling, no bypass of the irreversibility chokepoint (`commit()` still the sole `rho` writer, `delta >= 0` still enforced). A single front is tracked from a fixed start position through a uniform `rho_star` background (no H2-style density patterning — this isolates the dwell mechanism alone, cleanly separate from the already-closed H2 result).

## What was found

**A self-loop, by itself, at the certified default coefficients (kc=ks=kg=1), gives at most a one-time delay, not a tunable mass.** Hand-derivation (confirmed by simulation, Tests 2-5) shows the decisive quantity at each potential dwell is

```
Sigma(self) - Sigma(neighbor) = -kc*(k*increment)^2 + k*increment*(kg - ks)
```

where `k` is the number of prior self-commits since arrival. With `kg == ks`, this is negative for all `k >= 1`: a front can win the very first commit decision (decided by tie-scale jitter alone, before any density has accumulated) but never again — exactly one dwell, then permanent advance, regardless of `kc`, `increment`, or the self-loop's own bandwidth. This is why Tests 2, 3, and 4 (sweeping `b_self`, `kc`, and `increment` respectively, all at `kg=ks=1`) returned **identical numbers in every row** — not a bug, a closed-form fact about the coefficient regime.

**Setting `kg > ks` unlocks genuine, repeated, tunable dwelling.** The same formula predicts a critical dwell count `k* ~ (kg-ks)/(kc*increment)` before advancing becomes forced — i.e., the front should dwell `k*` times, advance once, then repeat the cycle at the new node, giving an emergent average velocity `v_eff ~ 1/(k*+1)`. Tested directly (Test 6): as `kg/ks` and `1/(kc*increment)` increase, dwell counts rise from ~1 up to nearly the entire step budget, while `extinguished_frac` stays at exactly 0.00 throughout every row — the front is not dying, it is genuinely and repeatedly dwelling.

**Confirmed as a stable, repeating mechanism, not a step-budget artifact.** The most extreme regime tested at short range (`kg=10, ks=1, kc=1, increment=0.1`, predicted `k*=90`) was re-run over 20,000 steps and a 6000-node chain, 6 seeds:

| seed | final position | v_eff | dwells | advances | extinguished |
|---|---|---|---|---|---|
| 0 | 216 | 0.0106 | 19393 | 607 | False |
| 1 | 220 | 0.0107 | 19395 | 605 | False |
| 2 | 209 | 0.0102 | 18798 | 1202 | False |
| 3 | 214 | 0.0104 | 19243 | 757 | False |
| 4 | 207 | 0.0101 | 18610 | 1390 | False |
| 5 | 219 | 0.0107 | 19632 | 368 | False |

Mean `v_eff = 0.0105`, versus the hand-derived prediction `1/(k*+1) = 1/91 = 0.0110` — within ~5%. The front never extinguishes across any seed, and keeps advancing net-forward (hundreds of genuine hops, position growing steadily) rather than stalling. This is a real, stable, tunable, **surviving** sub-ballistic propagation mode.

## Honest scope — what this is and isn't

**This is not a Higgs mechanism, EWSB, or a gauge-boson mass derivation.** It shows that an individual propagating front (a "particle," in the loose ED sense) can carry an effective velocity below the maximal ballistic rate while continuing to exist — a genuine dispersion-gap analogue — via a structurally licensed but previously untried mechanism. It does not show gauge symmetry breaking, does not involve a vacuum expectation value or condensate, and does not connect to gauge-boson mass via a covariant-derivative coupling the way H1 or the SM Higgs mechanism does. In the Arc Q H1-H5 taxonomy, this is not any of the five named mechanisms — it's a new, sixth structural option, closer to "a new propagation mode the substrate admits" than "a Higgs field."

**This requires a genuine, nontrivial coefficient choice (`kg > ks`), not something that falls out for free.** At the certified default (`kg=ks=1`), the effect collapses to a single one-off delay. `SigmaCoeffs`'s own docstring states "qualitative roles are fixed... magnitudes are tunable" — `kg > ks` stays within that licensed design space (both remain destabilizing/penalizing terms, same sign, just different relative weight), so this is not smuggling in new primitive structure the way the four-band P04 error did. But it is a real, load-bearing parameter choice.

**CHECKED 2026-07-06 — `kg > ks` has zero grounding in either direction.** Canonical P12 itself (`Σ_C = Coh − Str − Grad`) uses implicit unit coefficients with no kc/ks/kg-style weighting at all — the primitive text is silent on relative magnitudes, not supportive of any particular ratio. The four papers P12 names as load-bearing (Newton's G via Str, a₀, the ECR combination rule, BH horizon decoupling via Grad) never introduce or need unequal weights either — each uses only one term (Str or Grad) in isolation, never a ratio between them. No paper anywhere assigns Coh/Str/Grad independent physical dimensions (checked against the corpus's own Dimensional Atlas, which never even mentions Σ_C/Coh/Str/Grad), so there's no dimensional-analysis argument for or against `kg > ks` either. Prior corpus use of unequal kg/ks (a topology-robustness sweep) is explicitly symmetric/exploratory — "not a substrate change, not a theory change" — testing both directions with no physics claim either way. **Conclusion: `kg > ks` is licensed (within the coefficients' own designed tuning range) but is a free empirical dial with no support from any primitive or existing result — not derivable, not contradicted, genuinely unaddressed until this check.** This caps the whole result at ADMISSIBLE, not stronger — the mechanism is real and reproducible, but the parameter that makes it work is currently just an assumption, not a consequence of anything in ED.

**The self-loop bandwidth itself turned out not to matter mechanically** (Test 2) — bandwidth only enters at the tie-break stage, which almost never triggers once jitter is present; the whole effect is driven by the Sigma computation itself (the self-candidate's Grad term is exactly zero by construction, always).

## Tier verdict

**ADMISSIBLE, demonstrated on the certified substrate, conditional on an asymmetric coefficient choice (`kg > ks`) that is licensed but not derived.** Not FORCED (nothing requires a self-loop channel to exist, nor `kg > ks`). Not a Higgs mechanism per se — a structurally new, previously-untested propagation mode that gives ED a real answer to "can a front have a survivable, tunable, sub-ballistic velocity at all" — which is exactly the gate that blocked both H1 and H2. Whether this can be built up into an actual Higgs-like mechanism (e.g., combined with H1's inserted-scalar coupling, or reinterpreted as a mass mechanism directly) is a new, open, and now genuinely tractable next question — not yet attempted.

## Relationship to existing corpus results

- Does not retract or contradict E1 (H2 stays negative) or the H1 blockage (both still stand — this is a structurally different mechanism, not a rescue of either).
- Does not retract the dwell-question's earlier finding that *its four-band justification* was wrong — that finding stands; this result reaches the same conclusion (a dwell state is admissible) via the correct, canonical-primitives-only route the retraction called for.
- `Paper_113` row 10 should be updated to note this new candidate exists, tested, admissible-conditional — not yet strong enough to close the row, but no longer "nothing new to report" either.
