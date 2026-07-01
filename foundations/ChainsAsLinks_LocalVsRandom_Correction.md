# Locality Doesn't Save the Caveat — a Correction to the Multi-Chain Reachability Note

**Foundations — matter-sector / #2b arc, continues and corrects one caveat in `ChainsAsLinks_MultichainV5_Reachable.md`. That note flagged, as an honest limit, that its positive result (uniform-random V5 coupling reaches a K6 minor at modest density) probably overstates reachability, because V5's real coupling is proximity-based, and local structure was expected to need much higher density to reach the same threshold. That expectation was tested directly and did not hold.**

## 1. What was tested

A proximity-based coupling model, built without assuming any spatial embedding (the same discipline as the rest of this arc): chains are given an abstract index ordering — a label, not coordinates — and V5 cross-links are built as a ring lattice, each chain connecting mainly to nearby-index chains within a reach parameter, mixed with a controllable amount of long-range (uniformly random) rewiring, a standard small-world construction. This isolates the actual variable of interest: does coupling shape (local vs. global) change the K6-reachability threshold, holding total density fixed?

Swept across three system sizes (40, 100, 200 chains), reach fractions from 2% to 20% of the network, and the full range from purely local (no long-range links at all) to purely random (recovering the earlier model).

## 2. Result

**Locality made no detectable difference at any configuration tested.** At every combination of system size and reach fraction, purely local coupling and purely random coupling reached (or failed to reach) the K6 threshold at essentially the same average degree — within the same reach/density setting, they agreed every time, both finding a witness or both not finding one. What determined reachability was total density (average degree), not the coupling's shape.

This directly contradicts the expectation stated in the reachability note, and the reachability note has been corrected accordingly (struck through, not deleted, per house style).

## 3. What this changes and what it doesn't

**Changes:** the earlier positive result (K6 reachable at modest coupling density) is *more* robust than first reported, not less — it does not depend on an unrealistic, unrestricted global coupling assumption. A geometrically local model, closer in spirit to V5's actual finite-reach character, gets to the same place at the same density.

**Does not change:** the other two honest limits from the reachability note stand untouched. There is still no substrate-level number for what ED's actual coupling density is, local or otherwise — this only shows the *shape* of coupling doesn't matter, not that any particular density is realistic. And the operational question — does undoing a committed order actually require passing through this structure — remains completely untested.

## 4. The one residual uncertainty worth naming

All configurations tested here were modest in scale (up to 200 chains). Classical small-world theory shows that purely local structures can behave very differently from randomized ones once systems get much larger, with reach held to a genuinely tiny fraction of the whole — a regime this check did not reach. So the honest statement is: **locality does not matter at these scales; whether that continues to hold at much larger scale is untested**, not that locality definitely never matters.

## 5. Status of #2b's fourth item

Unchanged in substance from the reachability note's conclusion, with one caveat removed and one uncertainty reworded: structurally reachable, demonstrated in a simplified model whose reachability does not depend on an unrealistic global-coupling assumption, still not shown to be ED's actual regime, and still not connected to the operational question of whether ED's order-holding mechanism actually uses this structure.
