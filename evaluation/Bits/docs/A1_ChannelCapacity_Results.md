# A1 — Channel Capacity: Results

**Program:** Determinability-boundary bits-measurement (empirical arc) — robustness phase, axis A1 (channel capacity)
**Question:** Does channel *capacity* — observable-independent by construction — yield a *positive intrinsic* determinability invariant where single-observable Δ failed?
**Status:** Answered. **No — and the reason is a real structural finding.**
**Date run:** June 2026
**Author:** Allen Proxmire
**Code:** `analysis/capacity.py` (bias-corrected k-NN decoder MI); `examples/capacity_experiment.py`

---

## The question

The observable sweep showed single-observable mutual information is observable-*dependent*, so the scalar Δ is not intrinsic. **Channel capacity is the supremum of transmitted information over inputs and readouts — observable-independent by construction.** A1 asked: does capacity recover an intrinsic positive quantity (a "within-stratum capacity ceiling") that single-observable MI could not?

Method: a **coding experiment** — encode a K-ary message into region A's left-half initial condition, evolve the certified substrate, and try to decode the message from (i) A's right half [within-stratum channel] and (ii) region B [across the decoupling boundary].

## What the run found

The headline did not come from the estimator; it came from a **direct propagation diagnostic**, and it is exact:

> **Changing the A_left message from 0.0 to 0.45 leaves A_right's final state byte-identical — L2 difference = 0.000000 — across every baseline tested (5/5).** The message does not propagate to A_right *at all*. Not weakly. Exactly zero.

Same for B (across the boundary): exactly zero. And the **control passes**: A_right *does* respond to its *own* local initial condition (L2 = 1.8 for a 0.45 change) — so the simulator is working; A_right responds to *local* changes and is *exactly insensitive* to a distant region's input.

**Conclusion: the controlled (interventional) channel capacity between distinct regions is exactly zero — within a stratum and across the boundary alike.** A node's committed state depends only on its local neighborhood (ED's certified locality); it carries no information about a distant region's initial condition. There is no controllable channel to have a capacity.

(An estimator note, recorded for honesty: the first decoder-MI pass was wrong — naive k-NN decoder MI is positively biased by ~log₂K − log₂k when K ≫ k, so it read ~2.8 bits even across the *decoupled* boundary. The across-channel-as-null control caught it immediately; a shuffle-null correction fixed it. But once the diagnostic showed propagation is *exactly* zero, no capacity estimate was needed — there is nothing to estimate.)

## What it means

**1. Capacity gives no positive intrinsic invariant — it confirms, rather than rescues, the prior result.** At the one genuinely observable-independent level, the intrinsic quantity is **zero**, and it is zero *everywhere* — within and across. So capacity does not provide a "within > across" contrast, and there is no canonical positive determinability scalar to be found this way. The bits-work conclusion stands and is strengthened: the only observable-invariant content is a zero.

**2. The determinability boundary is an *observational* structure, not a *transmission* one.** This is the conceptual payoff. The bits-work Δ (within-stratum MI > 0) measured **observational correlation from a common cause**: within one run, both halves of a stratum share the run's seed and the front's passage, so across the ensemble they co-vary. A1 measures **interventional transmission** and finds it zero. The two diverge exactly because the within-stratum correlation is **common-cause, not causal-flow**:

- *Within a stratum:* the two halves are correlated because they share an origin (the same run), **not** because information flows between them.
- *Across the boundary:* independent origins (independent seeds) → no shared cause → no correlation.

So the "severance" the bits-work found is severance of **shared origin** (independent seeds make independent strata), not severance of a transmission channel — because there is no transmission channel anywhere. The determinability boundary is a fact about *common causes*, not about *signals*.

**3. A1 empirically confirms ED's locality — the "no unmediated nonlocal influence" property.** During the contrast-first work this was floated as a candidate prohibition (and then correctly set aside as belonging to ED's *locality* structure rather than to contrast-first). A1 demonstrates it directly and at the strongest level: **controlled transmission between distinct regions is exactly zero.** A committed fact in ED is strictly local — no distant intervention reaches it. ED's certified locality is not just an internal code property; it is observable as exact channel-zero.

## Honest verdict

A1 is a **clean negative on the capacity rescue, and a clean positive on the clarification**:

- *Negative:* capacity does not yield a positive intrinsic determinability number; it is zero everywhere. (The expected, allowed outcome — and still informative.)
- *Positive:* it sharpens *what the determinability boundary is* — an observational, common-cause correlation structure, not a transmission channel — and it empirically confirms ED's exact locality (no nonlocal controlled influence, within or across).

The throughline of the whole bits program holds: **what is observable-invariant about the boundary is a zero, not a scalar.** A1 adds: that zero, at the interventional level, is universal (locality), and the boundary's positive content lives entirely at the observational/common-cause level.

## Artifacts

- `analysis/capacity.py` — bias-corrected leave-one-out k-NN decoder MI (shuffle-null), reusable.
- `examples/capacity_experiment.py` — the coding experiment + the propagation diagnostic.

## Next, if pursued

The natural follow-on is **transfer entropy / common-cause decomposition**: formalize the observational-vs-interventional split (the determinability boundary lives in the common-cause term, with the transfer/causal term identically zero). That would turn this finding into a precise statement — but it is a reformulation, not a parameter sweep, and not required: A1 already answered its question.

---

*End of A1 results. Channel capacity between distinct regions is exactly zero — within strata and across the boundary — by ED's locality. Capacity yields no positive intrinsic determinability invariant; the boundary is an observational (common-cause) structure, not a transmission channel; and ED's "no nonlocal influence" is empirically confirmed as exact channel-zero.*
