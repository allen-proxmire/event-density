# The Reach Law Is Forced by the Holographic Channel-Count, and Only 3D Gives g ~ 1/b

**Foundations — gravity / curvature-emergence arc, second step. The foothold (`CurvatureEmergence_MetricFromBandwidth_Foothold`) showed a metric emerges from bandwidth-connectivity and that reach ∝ √b recovers GR-I's g ~ 1/b, but the √b was put in by hand and only called "natural." This note derives it. Probe: `evaluation/CurvatureEmergence/holographic_reach_law_probe.py`. Result: the reach exponent p is fixed by ED's own holographic channel-count to p = 1/(d−1); the boundary-cut measurement gives d−1 exactly (0.984 in 2D, 2.008 in 3D), so p = 1 in 2D and p = ½ in 3D; and feeding that *derived* p into the emergent metric gives g ~ 1/b² in 2D and g ~ 1/b (GR-I) in 3D (R² = 1.000). Tier: derived, conditional on the holographic surface-count (an established ED result) — a self-consistency/fixed-point, not from-nothing. It converts "√b is natural" into "√b is forced by the holographic channel-count, and only in three dimensions" — the same number 3 the linking argument independently lands on.**

## 1. What was left open, and the idea

The foothold established that the raw participation graph produces a metric, that a "mass" (bandwidth depletion) reads as *far* (curvature signature), and that GR-I's g ~ 1/b is recovered when reach ∝ b^p with p = ½. But p was a free exponent set by hand: reach ∝ b^p gives g ~ 1/b^{2p}, and nothing yet forced p = ½ over p = 1 (which gives g ~ 1/b²) or anything else. This note closes that: **p is not free — it is fixed by how many independent channels a bandwidth budget can actually sustain, and that count is holographic.**

The chain:

- **P04** — bandwidth b is participation capacity: the number of independent relational channels a locus sustains.
- **P08 + the area-law-as-edge-count result** (`AreaLaw_FromStraddlingEdges`, Paper_025) — for a locus reaching to radius R in a short-range d-dimensional substrate, the number of *independent* channels threading its neighborhood is the boundary **cut**: the edges crossing the ball's surface. For short-range edges that cut scales as the **surface**, R^{d−1}, not the volume R^d. This is ED's holographic bound, already established.
- Therefore a fixed channel budget b buys reach **R ~ b^{1/(d−1)}**, i.e. **p = 1/(d−1)**.
- **d = 2**: p = 1 → g ~ 1/b². **d = 3**: p = ½ → **g ~ 1/b (GR-I)**.

So p = ½ is forced by the holographic channel-count *in three dimensions*, and 3D is the unique dimension where the holographic reach law reproduces GR-I.

## 2. The probe (both measurable links tested, nothing assumed)

Two links in the chain are measurable, and the probe tests each on real graphs rather than asserting them:

**(A) The holographic step.** Build a short-range (nearest-neighbor) d-dimensional lattice. For a ball of radius R, count the edges crossing its boundary (the cut). Fit cut ~ R^s and read s — expected d−1 if the channel-count is holographic (surface), d if it were volume.

**(B) The metric under the derived law.** Take the reach exponent p = 1/(measured s), feed reach ∝ b^p into the emergent-metric measurement (a bandwidth dip on a background label line, distance = unweighted BFS hop-count, exactly the foothold's non-circular setup), and read the emergent metric exponent q. Expected g ~ 1/b^{2p} = 1/b^{2/(d−1)}.

## 3. Result

| step | d = 2 | d = 3 |
|---|---|---|
| (A) measured ball-cut exponent s | 0.984 | 2.008 |
| expected d−1 | 1 | 2 |
| derived reach exponent p = 1/s | 1.02 | **0.498** |
| (B) emergent metric exponent q | 1.05 | **0.500** |
| emergent metric g ~ 1/b^{2q} | g ~ 1/b² | **g ~ 1/b (GR-I)** |
| metric fit R² | 1.000 | 1.000 |

The cut scales as the surface (d−1) to within a percent, so the reach law is **p = 1/(d−1)**, derived. Feeding it back, the emergent metric is g ~ 1/b² in 2D and **g ~ 1/b, GR-I, in 3D**, fit R² = 1.000. **Three dimensions is the unique case where the holographic reach law reproduces the GR-I metric.**

## 4. What this converts, and the honest scope

**Converted.** The foothold's "√b is a natural choice" becomes "**p = ½ is forced by the holographic channel-count, and only in 3D.**" GR-I's spatial metric g ~ 1/b is no longer an assignment the graph happens to be able to match under a hand-picked exponent; it is the metric the graph is *driven* to by ED's own holographic bound, in three dimensions and no other. The reach law is now tied to the same holographic principle that gives S ∝ A and the area law, not to a separate assumption.

**Honest scope — this is a fixed-point / self-consistency result, not a from-nothing derivation.** It inherits two things and should be stated as inheriting them:

1. **The holographic surface-count.** That the independent-channel count is the boundary cut (rather than the volume) rests on short-range edges dominating — the area-law-as-edge-count result. That result is established in the corpus, but it is an input here, not re-derived. If the substrate were long-range-dominated, the cut would go as the volume, p would be 1/d, and the metric would differ.
2. **The reading b = independent-channel count = cut.** This is a reading of P04 (capacity = channels) joined to the area-law cut. It is the natural reading, but it is a reading.

What it does **not** yet do: derive the absolute length scale (ℓ_P enters only as the reach normalization), or leave the static/linear regime (the nonlinear field equations are untouched), or construct the substrate background-free (a d-dimensional lattice is assumed for the cut measurement; the *emergent metric on top of it* is genuine, but the lattice/topology is input).

**A structural convergence worth flagging, not overclaiming.** The dimension this argument selects — 3 — is the same dimension the linking argument (MS-II §7, `ThreeDimensions_ConsolidatedReview`) independently selects as the one where a spatial link can hold committed order. Two different requirements, the metric matching GR-I and the topology holding order, both single out three. That is genuine internal coherence: two independent faces of the geometry landing on the same number. It is *not* a proof that ED forces 3D — both arguments inherit inputs (the holographic count here, the linking premise there) — but two independent selections of the same value is the kind of convergence that makes the reading trustworthy rather than fitted.

## 5. Status

**The reach law is derived.** Curvature-emergence now has: a metric emerges from the graph (foothold), it shows curvature (foothold), and the specific reach law that gives GR-I's g ~ 1/b is forced by the holographic channel-count in 3D (this note) — with 3D uniquely selected. What remains of the bridge is the absolute length scale (ℓ_P), the nonlinear/dynamical field equations, and a background-free construction. The step from "g ~ 1/b is reachable under a natural law" to "g ~ 1/b is forced by holography, uniquely in 3D" is done.
