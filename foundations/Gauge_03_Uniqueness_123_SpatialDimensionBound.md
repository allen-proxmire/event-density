# Gauge Program · Step 3 — Why {1,2,3}? A Candidate: Channel Multiplicity Is Bounded by Spatial Dimension

**Foundations — step 3 (continues `Gauge_01/02`), the deep one: why do the gauge groups stop at SU(3)? The framework (step 1) gives SU(N) for *any* N, so {1,2,3} needs an extra constraint on the channel multiplicity. Candidate, and it is ED-native: **a channel is "a direction a chain can keep going in," channels form along the spatial ∇ρ structure, and indistinguishable same-rule-type channels occupy *independent spatial-frame directions* — so multiplicity is bounded by the number of spatial dimensions, N ≤ 3.** Time is the arrow, not a channel-direction, so the bound is 3 (spatial), not 4 (spacetime). If it holds, **the Standard Model gauge group U(1)×SU(2)×SU(3) is the *complete set* of channel-multiplicity gauge groups {SU(1), SU(2), SU(3)} allowed in 3 spatial dimensions — there are three forces because there are three spatial dimensions.** This is a real, falsifiable candidate for a famously unsolved problem. But it has three honest gaps I do not close: the bound *mechanism* (why independent directions, not many parallel channels), the "color is not spatial" objection (SU(3) color is rotationally invariant — its 3-ness vs space's 3-ness is either profound or numerology), and why all of {1,2,3} are realized. Tiered: a promising candidate, not a closed derivation.**

---

## 1. The question

Step 1 derived: gauge group = U(N) for a rule-type family of channel multiplicity N. This gives U(1), SU(2), SU(3) — but equally SU(4), SU(5), …. The framework alone does **not** stop at 3. The Standard Model does. So the real question is: **what bounds the channel multiplicity N?** Deriving `N ≤ 3` (and the realization of all of {1,2,3}) would be deriving the SM gauge group — which nothing in standard physics does.

## 2. The candidate: multiplicity is bounded by spatial dimension

Three substrate facts about channels, taken together, point at a bound:

1. **A channel is a spatial direction.** Per P07: a channel is *"a direction a chain can keep going in"* — channels are *directional*, and they *"form preferentially along ∇ρ or bandwidth-gradient structure"* (channel.md §1, §3). So a channel is anchored to a direction in the **spatial** gradient structure.
2. **Time is the arrow, not a channel.** Channels are about *propagation directions* (where a chain can go); the temporal direction is the arrow (P11/V1 retardation), which is not a "direction a chain chooses among" — it is the fixed forward sense. So channels live in the **3 spatial** dimensions (P06), not the 4 spacetime ones.
3. **Indistinguishable channels of one family must be *independent*.** For N same-rule-type channels to be a genuine multiplicity (N distinct channels, not one channel counted N times), they must be *structurally distinct* — and the structural distinction available to *same-rule-type* (otherwise-identical) channels is their **direction in the local spatial frame.** Channels sharing a direction are not independent; independent same-type channels occupy *independent spatial directions*.

The number of independent directions in the spatial frame is **D_spatial = 3** (P06). Therefore:
$$N \;\le\; D_{\text{spatial}} \;=\; 3 .$$

**The multiplicity of any stable same-rule-type channel family is bounded by 3 — the number of independent spatial-frame directions the indistinguishable channels can occupy.** The bound is 3, not 4, because time is the arrow, not a channel-direction.

## 3. The payoff (if it holds)

With `N ≤ 3` and the allowed multiplicities `{1, 2, 3}` all realized:
$$\{\,\text{gauge groups}\,\} = \{\,U(1),\; SU(2),\; SU(3)\,\} = \{\,SU(1),\,SU(2),\,SU(3)\,\}.$$

**The Standard-Model gauge group is the complete set of channel-multiplicity gauge groups allowed in three spatial dimensions.** ED's statement would be: *there are exactly three forces because there are three spatial dimensions*, and their groups are SU(N) for N = 1, 2, 3 — electromagnetism (the 1-channel/abelian case), the weak force (2 channels), and color (3 channels, saturating the spatial bound). The famously-arbitrary SM gauge group becomes the dimension-forced complete set. That is the prize this candidate is reaching for.

It also makes a **falsifiable prediction**: no stable fundamental force with gauge group SU(N≥4) — because there is no fourth independent spatial direction for a fourth independent same-type channel. A discovered SU(4)+ fundamental gauge force would refute it.

## 4. The three honest gaps (not closed)

This is a candidate, and the crank-rail demands the gaps be stated as loudly as the payoff:

1. **The bound mechanism is not rigorous.** §2.3 asserts that independent same-rule-type channels occupy *independent* (≈ orthogonal) spatial-frame directions, capping at 3. But channels form along *∇ρ*, and at a point there is *one* gradient direction, not three. Why a same-type *family* should span the *full* 3-frame (rather than, say, bundle many channels near one gradient direction, allowing N > 3) is not derived. The claim needs: a precise statement that same-rule-type channel independence ≡ spatial-frame-direction independence, with a stability argument forbidding two independent same-type channels in one direction. Not built.
2. **Color is not spatial (the sharpest objection).** SU(3) color is an *internal* symmetry — rotationally invariant, with no spatial meaning; the 3 colors are not 3 directions in space. If multiplicity = spatial directions, why is color blind to spatial rotations? A partial reconciliation: the **count** (3) is spatially bounded, but the SU(3) acts on the *internal channel-index* (which-channel), not on spacetime — so it is internal, with only its *size* dimensionally set; this evades Coleman–Mandula (internal and spacetime symmetries stay separate; only the rank is dimensionally bounded). But whether the 3-of-color genuinely equals the 3-of-space, or is a numerical coincidence, is **unresolved** — and this is exactly the kind of coincidence the crank-rail says not to oversell. I flag it as the candidate's central risk.
3. **Why all of {1,2,3} are realized.** The bound gives N ≤ 3; it does not force that families of *each* size 1, 2, 3 exist (vs only N=1). "The complete set up to the bound" is natural but not derived; it needs a reason every allowed multiplicity is populated by some stable rule-type family.

## 5. A complementary route: stability

The corpus independently hints at a bound from **stability**: channel.md §1 states multiplicity is *"usually small,"* and family stability = mutual rule-compatibility and bandwidth-coherence of all N channels under perturbation. A large-N family of mutually-coherent indistinguishable channels may be unstable (the coherence condition over many channels is harder to maintain) — giving a stability ceiling on N. This is *complementary* to the spatial-dimension bound (it could be the mechanism that *enforces* §2.3's independence, or an independent ceiling). It is equally unbuilt: no stability functional on N-channel families exists. But it is the natural place to make §4.1's bound mechanism rigorous — a stability calculation showing N-channel coherence fails for N > 3 (ideally tying the "3" to D=3).

## 6. Verdict

**There is a genuine, ED-native candidate for the SM gauge group's {1,2,3}: channel multiplicity is bounded by the spatial dimension (N ≤ 3), because indistinguishable same-rule-type channels occupy independent spatial-frame directions and time is the arrow, not a channel. If it holds, U(1)×SU(2)×SU(3) is the complete set of multiplicity gauge groups allowed in 3 spatial dimensions — *three forces because three spatial dimensions* — and it forbids stable SU(N≥4) forces (falsifiable).** This is real traction on a problem standard physics does not touch. **But it is not closed:** the bound mechanism (independent-directions, §4.1), the color-is-not-spatial objection (§4.2, the central risk — possibly profound, possibly numerology), and the realization of all of {1,2,3} (§4.3) are genuine gaps. The honest tier: **a promising, falsifiable candidate constraint — the most distinctive thing the gauge program can say — explicitly not a derivation.** The path to closing it runs through the stability route (§5): a coherence-stability calculation on N-channel families that forbids N > 3 and ties the bound to D=3. That calculation is the next concrete target if this thread is pursued.

---

*Gauge program step 3 (uniqueness). Framework (step 1) gives SU(N) for any N; {1,2,3} needs a multiplicity bound. Candidate: N ≤ D_spatial = 3, because (1) a channel is a spatial direction (P07: "a direction a chain can keep going in," forms along ∇ρ); (2) time is the arrow, not a channel → bound is 3 (spatial) not 4 (spacetime); (3) independent same-rule-type channels occupy independent spatial-frame directions → ≤3. Payoff: SM U(1)×SU(2)×SU(3) = complete set {SU(1),SU(2),SU(3)} of multiplicity gauge groups allowed in 3D — "three forces because three spatial dimensions"; falsifiable (no stable SU(N≥4)). Three honest gaps (NOT closed): (a) bound mechanism — why independent directions cap at 3 vs many channels per direction (channels form along ONE ∇ρ; the full-frame-spanning claim is unbuilt); (b) COLOR IS NOT SPATIAL — SU(3) is internal/rotation-invariant; 3-of-color vs 3-of-space is either profound or numerology (the central risk; partial reconcile: count spatially bounded, SU(3) acts on internal channel-index, evades Coleman-Mandula, but coincidence unresolved); (c) why all of {1,2,3} realized vs only N=1. Complementary route: channel-family STABILITY (channel.md "usually small") — a coherence ceiling on N; the place to make (a) rigorous (stability calc forbidding N>3, tying to D=3). Verdict: a genuine ED-native, falsifiable CANDIDATE — the most distinctive thing the gauge program can say — explicitly NOT a closed derivation. Crank-rail: payoff and gaps stated equally; color/space coincidence flagged as the risk, not sold. Next if pursued: the N-channel stability calculation.*
