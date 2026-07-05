# H1-Leg Scoping — Mass from Amplitude-Coupling, and the Deeper Gate E1 Exposed

**Status:** Scoping memo, 2026-07-05. Follows the E1 negative (`E1_MassFromStructure_Results.md`), which killed the H2 (σ_τ / gradient) route on the certified substrate's native ρ-field. **CORRECTION (2026-07-05): the "dwell question" §3–§4 below leaned on P04 carrying a four-band internal band. It does NOT — that structure comes from an ARCHIVED M-series forcing paper, not canonical P04 (Paper_087). See `Dwell_Question_Answer.md` (RETRACTED). The dwell is NOT licensed by the existing primitives; do not build a four-band/dwell simulator on it. The mass sector reverts to: H2 doesn't ground (E1), H1 blocked (§2, survives), mass OPEN/inherited. §2's two H1 obstructions stand; §3–§4's "ballistic-or-extinct is a primitive-forced/reversible gate" framing is withdrawn to "a fact about the reference code, not a licensed dwell."** This memo scopes the H1 (inserted scalar τ_H, mass-from-|D_μφ|²) route and finds that H1 and H2 are blocked on the **same single missing substrate ingredient**, which is more fundamental than either mechanism. No probe is run here; the scope reaches a structural obstruction that a probe on the reference substrate cannot get past without becoming a stand-in.

## 1. What H1 is, and why it looked like the escape from E1

H1: a Case-P scalar rule-type τ_H with a non-zero ground-state amplitude ⟨φ⟩, coupled to a gauge channel via a covariant-derivative vertex |D_μφ|² = |(∂_μ − igA_μ)φ|². The gauge boson gets mass g²⟨φ⟩²A_μA^μ. The feature that made H1 look like the escape from the E1 negative: **it works for a uniform ⟨φ⟩.** The mass comes not from any gradient of the propagating field (the H2/σ_τ route E1 killed) but from a *gauge coupling to a second field's amplitude*. The gauge field enters through the covariant derivative even when ∂_μφ = 0. So H1 sidesteps exactly the log-derivative blindness that defines H2.

## 2. Mapping H1 onto the certified substrate — two obstructions

To run H1 on `evaluation/Bits/simulator` you need two things the reference substrate does not have.

**(a) A second Σ-visible field to play φ.** The certified state is ρ (commitment density) + orientation, and Σ = kc·Coh(ρ) − ks·ρ − kg·|Δρ| reads only ρ and graph structure. There is exactly **one** Σ-visible field, ρ, and it is the propagating/"matter" field. There is no second Σ-visible scalar to carry an independent amplitude ⟨φ⟩. You cannot couple a gauge channel to φ's amplitude when there is no φ.

**(b) A gauge DOF that Σ can mass.** The one internal degree of freedom the substrate carries is **orientation** (B5), and Σ is **hard-blind** to it by invariant (`sigma.py`: "compute_sigma ... MUST NOT read NodeState.orientation"). Orientation is the natural analog of a gauge/internal direction, and it is exactly the DOF the dynamics cannot see. A mass is a Σ-visible modification of propagation; an orientation-carried "gauge boson" is invisible to Σ, so it can carry no Σ-visible mass. **This is the blindness invariant again** (`Paper_BlindnessInvariant_KnotsNotCrystals`): the rule-blind sector cannot acquire an interaction-visible property, and here the natural gauge sector is precisely the blind one.

So H1 cannot be built on the reference substrate without adding a second field and a coupling term to Σ. That is a hand-built stand-in, not a test of the certified substrate, and the standing discipline forbids reading a substrate conclusion off it.

## 3. The deeper gate: the update rule is ballistic-or-extinct

Step back from H1 vs H2 and ask what "mass" can even mean at the front level in the certified dynamics. A Lorentz-scalar mass is a **reduced group velocity** — a dispersion gap that makes a mode propagate slower while it keeps propagating.

The certified update (`update.py`) admits no such state. Each step, an active front either **commits to exactly one neighbor and advances one hop**, or it **extinguishes**. There is no stall, no wait, no fractional advance. Surviving-front speed is quantized to exactly **1 hop per step**; the only alternative is **0 (death)**. So the *only* ways structure can affect propagation are:

- **change which neighbor** the front takes (direction / path tortuosity) → a medium / refractive effect → a **crystal** (Test 3);
- **kill the front** (Σ below the continuation threshold) → **termination** (Test 4's late-time confinement).

A **reduced-but-surviving group velocity is not representable.** This is why E1 found no early-time velocity gap (Test 2b: patterned reach ≈ uniform reach at early in-flight time, extinction on or off): the front cannot be slowed, only redirected or killed. **Both H1 and H2 are blocked on this one missing ingredient** — the substrate has no dispersive, sub-ballistic-but-surviving propagation mode for any field to carry a mass. H2 fails because ρ-gradients redirect/terminate rather than slow; H1 fails for the same reason plus the two obstructions in §2.

This is the real result of the whole Higgs excursion, and it is bigger than the Higgs-mechanism enumeration: **grounding the mass sector needs a substrate propagation mode that is slower-than-ballistic yet survives.** The reference rule (exactly one hop or death) does not have it.

## 4. What a mass-capable ED substrate would need (and whether it is admissible)

The missing ingredient is an update-rule feature, not a Higgs-mechanism choice: a front must be able to **advance sub-ballistically without extinguishing** — e.g. a "wait" state (commit locally without advancing), a probabilistic/fractional hop, or a propagation speed set by a local field. Any of these would give a tunable group velocity = a mass dial.

The honest question is whether such a mode is **derivable from the primitives** or would be a bolt-on. This is not settled here, but the direction is clear:
- It must come from the substrate rule, not from adding a term to Σ (that would be a stand-in).
- The natural candidate is P11/P04: does the commitment rule admit a front that commits *in place* (raises local ρ) without selecting a forward neighbor — a "dwell" — when no forward candidate clears the bar but the front is not forced dead? The reference rule collapses this case to extinction; a mass-capable rule would distinguish "dwell" from "die." Whether the primitives force extinction or permit dwell is a real, answerable substrate question.
- If the primitives permit dwell, dwell-time is the group-velocity dial, and mass becomes groundable. If they force extinction, ED's substrate genuinely has no rest mass at the reference layer, and mass is inherited (which is consistent with the corpus's form-forced/value-inherited posture, but sharper: not even the *mechanism* is native).

## 5. Recommendation

Do not build an H1 probe on the reference substrate — it cannot be done without a stand-in, and the obstruction is already diagnosed. Instead:

1. **Escalate the reframed gate.** The mass-sector open question is not "which Higgs mechanism (H1/H2/H3)"; it is **"does the ED substrate admit a slower-than-ballistic surviving propagation mode (a dwell), and is it forced or forbidden by P04/P11?"** That single question gates every mass mechanism. It belongs in Arc M / `Paper_113` open-questions next to the σ_τ-faithfulness point (same root: the substrate lacks both the amplitude-invariant field σ_τ assumes *and* the dispersive mode any mass needs).
2. **The one runnable follow-up** is the dwell question itself, and it *is* grounded: read the P04/P11 commitment rule and the `apply_update` extinction branch, and determine whether "no forward candidate clears the bar" is forced to extinction by the primitives or whether a dwell (commit-in-place) is admissible. That is a primitives-reading + minimal-rule question, not a stand-in, and it decides whether the mass sector can ever be native.
3. **Bank the structural finding:** the natural gauge sector in ED (orientation) is Σ-blind, so it cannot carry a Σ-visible mass — the blindness invariant reaches the gauge-mass question directly. This is a clean cross-arc link (blindness ↔ mass) worth a line in both the blindness paper and the mass paper.

## Bottom line

H1 is not the escape from E1; it is blocked by the same wall plus two of its own. The wall is that the certified substrate propagates ballistically-or-not-at-all, with no dispersive mode for a rest mass to live in, and its one internal DOF (orientation) is invisible to the dynamics. The mass sector's real gate is a substrate-rule question — does P04/P11 admit a dwell — and that, not the Higgs-mechanism menu, is what to take upstream.
