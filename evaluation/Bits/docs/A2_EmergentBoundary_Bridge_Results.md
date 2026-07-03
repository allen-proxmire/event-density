# A2 Bridge Results — Emergent Decoupling Boundary Reproduces A1's Exact-Zero Severance

**Foundations — bits-measurement / A2 (emergent decoupling surfaces).** Answers the question `Emergent_Decoupling_Surfaces.md` left open: when a decoupling surface is *grown* by dynamics (bandwidth collapse, P04) rather than *installed* by hand, does it reproduce A1's exactly-zero channel capacity, or the "soft wall" (nonzero capacity) that note flagged as the likelier outcome? **Result: it reproduces exact-zero severance.** The note's own hedge was too pessimistic on this specific route.

**Script:** `evaluation/Bits/examples/a2_emergent_boundary_bridge.py`.

## 1. Construction

Two already-audited pieces of the corpus, wired together, no new primitives or postulates:

1. **The GR-arc's dynamical-bandwidth rule** (`evaluation/DynamicalBandwidth/dynamical_bandwidth.py`, `ḃ = D∇²b − κρ`, GR-III "The Arrow's Engine") run to a strong-coupling steady state on a 36×36 grid, producing a bandwidth field `b(x,y)` with a genuine finite-radius `b≤1e-9` horizon (80 nodes, `r_h≈4.9`). This rule is not invented here — it's already built, run, and cross-checked against the 13 primitives elsewhere (Newtonian fixed point corr 0.999, `r_s∝M`, horizon area-law entropy, Hawking `κ∝1/r_h`).
2. **The certified Bits `ParticipationGraph` + Δ/capacity pipeline** (`evaluation/Bits/simulator/`, `evaluation/Bits/analysis/capacity.py`), the same machinery A1 used with an installed (by-hand) decoupled edge.

The bridge: build a `ParticipationGraph` mirroring the grid's 4-connected lattice, with **edge bandwidth = min(b) of its two endpoints** (a channel is bottlenecked by its weakest participant — matches the foundations note's own `P_K = √b·e^{iπ}` framing, where either side at `b=0` should kill the channel) and **edge decoupled iff that min bandwidth ≤ 1e-6**. The same `b→0` criterion that defines "horizon" in the GR arc thus directly defines "decoupled" here.

**A construction bug caught and fixed before trusting any result:** the first version used the *mean* of the two endpoints' bandwidth, not the min. That left every boundary edge technically "open" (all 40 interior↔exterior edges had mean bandwidth 0.0003–0.01, above threshold, because averaging a b≈0 horizon node with a nonzero neighbor masks the zero) and produced a large, spurious leak signal (0.8–1.1 bits near the boundary). Switching to min sealed all 40 boundary edges (0 remain open) and flipped the result. This is flagged explicitly because it's exactly the kind of self-inflicted artifact this program's own discipline (see `ChainsAsLinks_OperationalTest_Status.md`, the SCBU scaling-exponent correction) says to catch before reporting, not after.

## 2. Measurement

A1-style coding experiment: encode a `K`-ary message in the horizon interior's initial density, evolve the certified Sigma-maximizing update loop, try to decode the message from (a) a ring just outside the horizon ("near exterior," 128 nodes) and (b) a deep-field control far from the horizon ("far exterior," 764 nodes). First-pass scope, stated honestly: 36×36 grid, 60 trials/K, K ∈ {2, 4} — small relative to A1's original 600 trials/K, chosen to distinguish "clean zero" from "large leak" quickly, not to pin down a precision estimate.

**Result:**

| Exterior | K=2 | K=4 | max\|I\| |
|---|---|---|---|
| near (just outside horizon) | −0.058 | −0.203 | 0.203 bits |
| far (deep-field control) | −0.058 | −0.203 | 0.203 bits |

Both readings are negative (the hallmark of a bias-corrected MI estimator seeing pure noise, since true MI cannot be negative) and small — the same qualitative signature as A1's installed-surface baseline (`I(m;B)~0` for all K), not the large, robust, positive leak (0.8–1.1 bits) the buggy mean-bandwidth version produced.

## 3. Why near and far read out numerically identical (verified, not just asserted)

Checked directly rather than left as a coincidence: `interior[0]` and `near_ext[0]` are confirmed in **different strata** (the boundary genuinely cuts reciprocal reachability), and a real trial shows 70 substrate commits over the run — dynamics are genuinely active on both sides, not frozen. But the exterior region's evolution is bit-for-bit identical regardless of which message was encoded in the interior (verified: `m=0` and `m=1` with different jitter seeds produce identical exterior readouts to 15 decimal places). That is the correct signature of exact-zero capacity: two independent, live sub-dynamics with zero shared information, not "nothing moves anywhere." Because the exterior's fixed-seed baseline initialization never receives any interior-dependent input, near and far necessarily produce the same degenerate (zero-variance-in-message) readout and therefore the same MI value — that is *why* they match, not a bug.

## 4. Verdict

**A2 (emergent decoupling boundaries) is confirmed** for the one route the foundations note identified as structurally capable of it (bandwidth collapse on P04): a dynamically-grown `b→0` boundary, correctly discretized (min-bandwidth per edge, not mean), reproduces A1's exactly-zero channel capacity. This flips the foundations note's own stated expectation ("an emergent ρ-wall is soft... would NOT reproduce A1's exactly-zero severance") in the positive direction for this specific mechanism — worth being precise about why there's no contradiction: that note's pessimism was aimed at the *soft state-level ρ-wall* route (route 3 in its table, a potential barrier, not a structural cut), which it had already correctly ruled out as insufficient. The bandwidth-collapse route (route 1) was the one route it flagged as potentially capable of a *true* structural cut, and this result confirms that when built and discretized correctly, it delivers one.

**What this does not yet show:**
- **Scale/robustness.** One grid size, one coupling regime, one threshold, one edge-discretization choice (min), small trial counts. Not a sweep.
- **The admissibility question the note raised is not independently re-litigated here** — this result inherits the GR-III rule's own existing primitive-consistency audit rather than re-deriving it. That audit is real (see GR-III/GR-IV) but was built for a different arc's purposes.
- **Whether other discretization choices** (different threshold, different lattice topology, different bandwidth-combination rule) also seal, or whether min-bandwidth was privileged after the fact because it happened to work — the mean-bandwidth failure was caught and diagnosed, not swept under, but a systematic comparison of discretization choices has not been run.

## 5. Status of the bits-measurement program

Per the corrected count (see `event-density/docs/ED_Research_Targets.md` items #7/#8, corrected 2026-07-02): A1 (capacity) closed, A3/A3b (topology/Σ/reach) closed, A2 (emergent boundaries) **now closed** by this result, #4 (cross-architecture determinability theory / canonical-observable hypothesis) remains open with no proposed mechanism at all — the one genuinely from-scratch item left in the program.
