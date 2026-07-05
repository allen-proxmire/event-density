# The Dwell Question, Answered — Is ED Mass Groundable, or Inherited at the Mechanism Level?

**Status:** Answer memo, 2026-07-05. Resolves the gate the H1-leg scoping (`H1_Leg_Scoping.md`) raised: does P04/P11 force extinction when no forward candidate clears the bar, or admit a commit-in-place *dwell* (sub-ballistic-but-surviving propagation)? The answer decides whether ED's mass sector is groundable-in-principle or inherited even at the mechanism level. **Method: read the primitive definitions, not a stand-in.**

## The answer, up front

**Dwell is admissible, not forbidden. ED mass is groundable-in-principle.** The reference substrate's ballistic-or-extinct behavior is an *implementation reduction*, not a primitive necessity, and the missing ingredient (an internal-band commitment) is exactly where the corpus's own mass functional σ_τ already puts mass. What is missing is a simulator that carries P04's full four-band structure and lets a chain commit internally; nothing in P04 or P11 forbids it.

## What the primitives actually say

- **P04 (bandwidth):** bandwidth $b_K(u) \ge 0$ is a non-negative additive scalar. In its §1.5 refinement it carries a **four-band partition: internal, adjacency, environmental, commitment-reserve.** The **adjacency** band is the spatial-neighbor/movement direction (Paper_087: "the chain's experienced acceleration is the negative gradient of Σ along its *adjacency direction*"); the **internal** band is the chain's at-locus content.
- **P11 (commitment):** a commitment event is where "a chain's multi-channel participation **collapses to a single channel**," irreversibly, with phase-randomization of the un-selected channels. **P11 says nothing about spatial advancement.** Commitment is channel *selection*, not a mandate to move to a new locus.

Neither primitive says a commitment must advance the chain to a neighbor. P04 explicitly carries an at-locus (internal) band distinct from the toward-neighbor (adjacency) band.

## Where the reference simulator diverges from the primitives

The certified `evaluation/Bits/simulator` is a **one-band reduction** of P04: each node carries a single scalar `rho` (commitment density) plus a Σ-blind `orientation`. It does **not** represent the four-band structure at all. Its update rule then makes two choices, and *ballistic-or-extinct is a consequence of those choices, not of P04/P11*:

1. **Commitment candidates = adjacency neighbors only** (`compute_candidates = admissible_neighbors`). The internal (at-locus) band is not a candidate, so committing-in-place is not even an option the rule considers.
2. **Optional extinction threshold** (`extinction_threshold`, which can be `None`): when the best neighbor is sub-threshold, the front dies rather than waits.

So the reference rule offers a chain exactly two outcomes each step: adjacency-commit (advance one hop) or extinguish. That is a *restriction* of P11 to the adjacency band, with the internal band dropped. It is not what the primitives force.

## The dwell, in primitive terms

A **dwell** is an **internal-band commitment**: the chain commits (raises its at-locus participation, advances in chain-time, irreversible per P11) *without* selecting an adjacency channel to a neighbor. Its spatial position is unchanged; its worldline advances in place. A chain that dwells for $k$ steps and then advances has covered one spatial hop in $k{+}1$ steps: **group velocity $1/(k{+}1) < 1$.** Dwell-fraction is a continuous group-velocity dial, and a reduced-but-surviving group velocity is exactly a **rest mass**.

P04 provides the internal band that a dwell commits to. P11's "collapse to a single channel" does not forbid that single channel being an at-locus one. So the dwell is **admissible**. It is not *explicitly licensed* either — P11 does not enumerate whether an at-locus channel is a legal commitment target — so the honest status is **admissible-but-unspecified**: a genuine degree of freedom in completing the substrate rule, currently resolved (by omission) toward no-dwell in the reference simulator.

## Why this converges with σ_τ (the corroboration)

This is not a convenient invention. Arc M's mass functional already lives in the four-band structure:

  σ_τ = ℏ · √( Σ_X w_τ^X · ⟨(∂_μ ln b_τ^X)(∂^μ ln b_τ^X)⟩ ),  X ∈ {internal, adjacency, environmental, commitment}.

σ_τ **sums over the internal band.** The corpus's own mass object is built from the very bandwidth structure the dwell would exercise. And E1's core negative now has a clean root cause: the reference simulator cannot carry a σ_τ mass because **it dropped the internal band** — it kept only ρ (commitment density, an adjacency/committed quantity) and a blind orientation. The same reduction that makes it ballistic-or-extinct (no internal-band commitment) makes it unable to host σ_τ (no internal-band field). One missing ingredient, two symptoms.

So the picture is coherent across three places: P04 (carries the internal band), P11 (permits collapsing to it), and Arc M σ_τ (locates mass partly in it). The reference simulator is the outlier, because it is a one-band reduction.

## Answer to the gate, and honest caveats

**Groundable-in-principle, not foreclosed.** The mass mechanism (internal-band commitment / dwell) is admissible in the primitives and coincides with where σ_τ already puts mass. ED mass is therefore *not* inherited-by-necessity at the mechanism level; the reference substrate's inability to carry it is an artifact of a one-band implementation.

Caveats, stated plainly:
- **Admissible ≠ licensed.** P11 does not explicitly say an at-locus channel is a legal commitment target. Pinning "dwell is a legal commitment" is a substrate-rule specification the corpus has not written. It is permitted, not mandated.
- **Groundable-in-principle ≠ grounded.** No mass has been produced. Producing one requires a simulator that carries the four-band P04 and implements internal-band commitment, then a demonstration that dwell-fraction gives a velocity gap (the very early-time velocity gap E1's Test 2b showed the one-band sim cannot).
- **Scope.** This is about the reference substrate and the stated primitives. A different completion that forbids internal-band commitment would push mass back to inherited; nothing here forces the licensing, it only shows nothing forbids it.

## Recommendation (a real fork for AP)

Three honest options, in rough order of ambition:

1. **Build the four-band / dwell extension** and re-run the E1 velocity-gap test on it. This is the actual path to *grounding* an ED rest mass: implement P04 §1.5's internal band as a real field, let a chain commit internally, and measure whether dwell-fraction produces the early-time velocity gap (deficit < 1 at early in-flight time, extinction off) that the one-band sim could not. Substantial, but it is the first genuinely mass-capable ED simulator, and it is grounded (it implements a stated primitive refinement, not a bolt-on). **This is the recommended real-work move if the mass sector is the target.**
2. **Escalate as a named gate.** Put "internal-band commitment (dwell) is the mass-groundability gate; admissible under P04/P11, unimplemented in the reference substrate, and coincident with σ_τ's internal-band content" into Arc M / `Paper_113` open-questions. Cheap, correct, and it reframes the mass sector's open status from "blocked/unknown" to "groundable pending a four-band + dwell simulator."
3. **Settle here.** Bank the diagnosis and move to a different frontier (the corpus map has several).

The clean line for AP: *the reference substrate can't carry a mass because it is a one-band reduction that dropped the internal band; the full primitives carry it, and a dwell (internal-band commitment) is the group-velocity dial. Mass is groundable; it needs a four-band simulator to show it.*
