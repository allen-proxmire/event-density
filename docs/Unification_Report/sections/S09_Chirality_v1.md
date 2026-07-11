# §9 — Chirality: ED builds the stage, inherits the assignment

*Draft v1, 2026-07-10. Register: peer-facing. Tiers: operator grounding **structural**; the clean-vector result **derived (theorem)** at the transport level; "necessarily spontaneous" **derived (corollary)**; the casting **inherited** (account/rep-theory). Point-toward. Primary source (read-first): `Paper_CleanSubstrateVector_ParitySpontaneous` (supersedes `Paper_ParityWall_ChiralityVerdict` on the verdict's tier). Computation: `rep_spectrum_casting_winding.py`.*

---

**The arrow's job here.** Chirality is where the arrow does a half-job, and the honesty of the section is in saying which half. The chirality operator `γ⁵` factors, in ED, into the arrow times a spatial orientation, so the arrow literally *is* one of its two ingredients. And the arrow's parity-cleanness — the substrate has no reflection in its toolkit — is what forces the central theorem: the clean substrate is vector, and any parity violation must be spontaneous. What the arrow does *not* do is pick which force is chiral. That is inherited.

Parity violation, the fact that the weak force couples to left-handed fermions and not right, is one of the starkest facts in the Standard Model, and it is written into the law by hand. The question for ED is whether the substrate produces it or inherits it. The answer is precise: ED builds the entire stage on which chirality lives and inherits the one assignment.

## The operator is grounded

The Dirac chirality operator is `γ⁵ = iγ⁰γ¹γ²γ³`. Read its two factors in ED. `γ⁰` is the arrow: ED's timelike direction is the commitment order (P11, retarded transport). `γ¹γ²γ³` is the oriented volume element, a handedness of the spatial 3-frame that flips sign under reflection. So `γ⁵` is the arrow times a spatial orientation, both factors native. This grounds an operator the earlier parity work had found missing, and it explains why that work found "no local screw": `γ⁵` is not a per-channel object at all, it is global, the one arrow times the one global orientation.

The operator is only as real as its orientation factor, and two facts make it real. The orientation is **spontaneous** (derived): ED's rules are parity-symmetric, no primitive is a reflection, and a parity-symmetric rule set cannot fix a handedness, so any orientation the substrate carries is chosen by symmetry breaking, like a ferromagnet picking a direction. And the emergent space is **orientable** (structural): building a non-orientable space requires a reflection somewhere in the frame bundle, and ED has no reflection, so all frame relations are proper rotations and a single orientation propagates across the causal patch. The same one fact, no reflection primitive, does both jobs: it makes the orientation spontaneous and makes the space able to carry it globally.

## The theorem: the clean substrate is vector

Model a family of `N` channels as a commitment map on an emergent chain, `H(k) = e^{ik}A + e^{-ik}B`, with `A` the forward (arrow-directed) hop, `B` the backward hop, `k` the wavenumber. Net chirality is the **point-gap winding** of this map, the number of times `det H(k)` encircles a reference as `k` runs its period; nonzero is chiral, zero is vector.

Parity-cleanness fixes `B`. Parity is the spatial reflection `k → −k` together with the lane reflection `S` of the channel row, and parity-symmetry of `H` forces the backward hop to mirror the forward one, `B = S A S⁻¹`. Then

`S H(k) S⁻¹ = e^{ik}B + e^{−ik}A = H(−k)`,

so `det H(k) = det H(−k)`: the determinant is **even** in `k`. An even determinant retraces its own path over the period, encircling nothing, so the **winding is identically zero, for every `N` and every forward hop `A`.** This was checked directly for `N = 1` through `6` over many random hops, zero in every case.

> The parity-clean substrate carries no net chirality at any channel-count. It is vector for one channel, two, three, all of them.

The corollary is the strong positive: since the clean transport is vector, any parity violation must break the parity symmetry, which means it must be the spontaneous orientation choice. **If parity is violated in ED, its direction is necessarily spontaneous** — not a handedness written into the law, because the clean rules provably cannot carry one, but a contingent, symmetry-broken choice. This is what turns the earlier verdict from "we looked and did not find chirality" into "the clean rules cannot carry it, and here is the proof."

## Capability is not selection

Having a defined `γ⁵` is not yet parity violation; the dynamics has to treat the two handednesses differently. That splits into capability (is there a genuine left and right to couple to?) and selection (does the dynamics use it?). The capability structure is clean and is Allen's highway picture made precise: a parity-clean coupling that references the orientation must live in the reflection-odd part of the gauge structure. For `N = 1` (abelian) that sector is empty, so the coupling is **forced vector** — which is electromagnetism. For `N ≥ 2` it is nonempty, so a chiral coupling is **possible**. The geometry says whether the highway has a left and a right lane; it does not say whether the universe drives in one. That is the whole content of the wall.

## The casting is inherited

Which channel-count actually ends up chiral, once the symmetry is broken, is not a transport fact. The clean winding is `0` (the theorem); under a natural breaking it is `N`, monotone in the channel-count. The Standard Model's pattern is **non-monotone**: vector, chiral, vector for one, two, three channels. It matches neither `0` nor `N`. So the transport dynamics does not select it.

Where the selection lives is representation theory: the fundamental of `SU(2)` is **pseudoreal**, while the fundamentals of `SU(N ≥ 3)` are complex. "Two channels is special" is a group-theoretic fact, not a parity-of-`N` fact, and it is the genuine invariant behind the lane picture's correct hit on the weak force. ED inherits it, exactly as it inherits the gauge multiplicities and the constants (this is the same rep-spectrum question as §7 and §13). The contribution here is to name precisely what is behind the wall.

## The prediction, and the anomaly baseline

Because the clean substrate is provably vector, ED's parity violation is necessarily a spontaneous, per-universe orientation tied to the arrow, and the same arrow sets the matter/antimatter sign. So ED predicts the **gauge handedness and the matter/antimatter sign are correlated** — two faces of one first-commitment choice — against the Standard Model's fixed, uncorrelated, law-level handedness. The claim is theoretically firm (it rests on the vector theorem, not a stance), but its **testability is open**: the corpus register flags it as not testable with current data, so §14 carries it as a distinctive-but-not-yet-testable prediction rather than a live weapon.

The theorem also fixes the anomaly baseline: a vector theory is automatically anomaly-free, so the clean substrate carries no gauge anomaly (at the transport level, contingent on the substrate-to-Dirac descent). The Standard Model's nontrivial chiral cancellation is a property of the inherited chiral content, so it is inherited with that content (§12).

## Scope

- The casting is inherited, not derived. The wall is strengthened and explained, not breached.
- The theorem is at the channel-transport level; the relativistic descent to the full Dirac sector is the standing open arc (§10, §13).
- No representation spectrum, hypercharges, masses, or charge magnitudes.

## What this buys the report

Chirality is the arrow doing half a job cleanly: it *is* half of `γ⁵`, and its parity-cleanness forces the vector theorem, so parity violation is provably spontaneous rather than law-level. The other half — which force is chiral — is the representation-theoretic inheritance that also drives §7 and §12. And the correlated-handedness prediction is a distinctive claim (testability open, §14). The verdict is a clean division: ED builds the stage of chirality and inherits the one assignment.

---

*Draft notes for finalization:*
- *Do not state ED "derives parity violation" — it derives that parity violation must be spontaneous, and inherits which force is chiral. That distinction is the section.*
- *The theorem is transport-level; keep the relativistic-descent caveat (§8 of the source paper) attached wherever "vector" or "anomaly-free" is claimed.*
- *The correlated-handedness prediction belongs in §14's falsifier list; cross-reference, don't duplicate the full treatment.*
- *Casting → representation theory ties to §7/#1; keep the "same wall" language consistent so the report reads as one inheritance, not three separate ones.*
- *Length ~1150 words. Register OK: γ⁵, point-gap winding, pseudoreal/complex representations, reflection-odd sector named flat-out.*
