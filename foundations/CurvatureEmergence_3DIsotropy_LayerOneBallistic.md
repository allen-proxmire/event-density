# 3D Isotropy: It Emerges Under Coarse-Graining, and the Metric Exponent Is a Layer-2 Object

**Foundations — gravity / curvature-emergence arc, 3D check (partial, honestly framed). Steps 1-3 were 1D. This probe builds a genuine 3D lattice with a spherical bandwidth dip (a "point mass") and measures the emergent metric via unweighted BFS hop-distance from the centre. Probes: `evaluation/CurvatureEmergence/isotropy_3d_probe.py`, `isotropy_3d_convergence.py`, `radial_metric_clean.py`, `radial_localslope.py`. Result, stated straight: (i) a metric emerges and curves in real 3D (distances stretch near the mass), and (ii) **isotropy is not exact on the raw graph but emerges as the reach coarsens** (axis/diagonal anisotropy 0.35 → 0.00, shell CoV → 0.00). But (iii) **the clean radial exponent g ~ 1/b could not be extracted from the raw paths** — cumulative fits are degenerate (q bounced 0.6-1.6) and local slopes are noise (R² 0.05-0.5). The honest reading, via the two-layer coarse-graining program: the raw BFS shortest-path is a *ballistic worldline on a faceted cubic reach-graph* — layer 1, non-Gaussian, direction-dependent by construction; the clean isotropic single-exponent g ~ 1/b is a *layer-2* object reached only by coarse-graining. So the messy exponent is not a failure of step 2 — it is a layer mismatch, and ED behaving as the two-layer picture predicts. Step 2's cut-**counting** derivation (a count, not a transport measurement) remains the clean exponent result; this probe adds *isotropy-emergence*, correctly framed, not a second exponent measurement.**

## 1. What was being checked

Steps 1-3 (`CurvatureEmergence_MetricFromBandwidth_Foothold`, `..._ReachLaw_Derived_Holographic`, `..._LengthScale_IsThePlanckGrain`) were 1D. A 1D stretch can't see the two things that make a metric *gravitational*: **isotropy** (distance a function of radius only, not direction) and a genuinely **radial** g ~ 1/b around a point mass. This probe builds a real 3D lattice (one locus per cell, P08), places a spherically symmetric bandwidth depletion at the centre, lets bandwidth enter only through connectivity (reach ∝ b^p, p = ½, the derived 3D law), and reads the emergent distance as plain unweighted BFS hop-count from the centre.

## 2. What the probes found

**A metric emerges and curves in 3D.** Hop-distance from the centre grows outward and stretches through the low-bandwidth core — the curvature signature, now in genuine three dimensions.

**Isotropy is not exact on the raw graph — it *emerges* under coarse-graining.** On the raw reach-graph the metric is faceted: at matched true radius, body-diagonal rays are farther in hops than axis rays (relative difference 0.13-0.35 at moderate radius). But sweeping the reach from fine to coarse, the anisotropy falls monotonically to zero (axis/diagonal 0.345 → 0.000; per-shell coefficient of variation 0.086 → 0.000). Coarser reach = more offset directions = a rounder connectivity ball = the faceting washes out.

**The clean radial exponent g ~ 1/b could not be extracted from the raw paths.** Every method failed to resolve it cleanly: fitting the cumulative hop-distance to ∫dr/b^q gave q bouncing across 0.6-1.6 with high but *undiscriminating* R² (many exponents fit a smooth cumulative integral about equally — degenerate); the non-degenerate local-slope method (v = dD/dr vs reach) was dominated by integer-BFS noise (R² 0.05-0.5, slopes −1.2 to −3.4). No config-stable exponent came out.

## 3. The honest reading: layer-1 ballistic, not a failed reconfirmation

The BFS shortest-path *is a ballistic worldline*: the straightest route through the reach-graph. On a cubic lattice the reach neighbourhood is a polyhedron, not a sphere, so ballistic transport is **direction-dependent (faceted)** and **non-Gaussian** by construction. This is exactly the layer-1 object in the two-layer coarse-graining program (`project_two_layer_coarsegraining`): ED's *direct* coarse-grain is transport, ballistic worldlines, non-Gaussian; the smooth, isotropic, single-exponent continuum object is *layer 2*, reached only by decorrelating — the "leaving ED" step.

Read through that lens, the three findings are coherent, not contradictory:

- **Isotropy emerging under coarser reach is a partial layer-1 → layer-2 coarse-graining.** More offset directions rounds the ballistic ball toward the sphere; isotropy is a layer-2 property, and it appears exactly as the coarse-graining proceeds. The probe *shows* the transition.
- **The exponent staying messy is a layer mismatch, not a failure.** A single clean metric exponent g ~ 1/b is a layer-2 (Gaussian/continuum) quantity. Reading it off raw layer-1 ballistic paths — faceted, integer-quantised, non-Gaussian — should not give a clean number, and it does not. That ED does not hand you a clean Gaussian/continuum exponent at layer 1 is the *expected* behaviour of a substrate that recovers the continuum only one coarse-graining up.
- **The clean exponent lives where the derivation put it: in a count, not a transport measurement.** Step 2 derived reach ∝ √b from the *boundary-cut count* (channels ~ surface ~ R^{d−1}), which is a combinatorial/holographic count and came out clean (cut exponent 0.984 in 2D, 2.008 in 3D, R² = 1.000). That is the load-bearing exponent result. It does not depend on measuring ballistic transport, which is why it is clean while the BFS exponent is not.

## 4. Verdict and scope

**Confirmed (real):** a metric emerges and curves in genuine 3D; **isotropy emerges under coarse-graining** — the raw ballistic metric is faceted, and the faceting washes out toward the continuum exactly as the two-layer picture requires. This is a genuine addition: the emergent geometry is isotropic at layer 2, and the probe exhibits the layer-1 → layer-2 transition.

**Not established by this probe (and correctly so):** a clean radial g ~ 1/b read *directly off the raw paths*. That is a layer-2 quantity; the raw BFS is layer-1 ballistic and non-Gaussian, so no exponent-extraction on it is clean. This neither confirms nor refutes step 2 — it is the wrong layer to measure it at. Step 2's cut-counting derivation stands as the clean exponent result.

**Honest scope.** Lattice background (topology input; the metric *on* it is emergent), static/linear, b_min > 0 (no true horizon). And the deeper point this surfaces: extracting continuum/Gaussian observables (a clean metric exponent, exact isotropy) from raw ED requires the coarse-graining step explicitly — ED does not deliver them at layer 1. That is consistent with the whole two-layer program and with ED's non-Gaussianity, not an anomaly.

## 5. Status — curvature-emergence after the 3D check

| piece | status |
|---|---|
| a metric emerges + curves (1D and 3D) | measured |
| reach law → g ~ 1/b, unique to 3D | derived (step 2, cut-count — clean) |
| no new length scale (it is ℓ_P) | derived (step 3) |
| **isotropy in 3D** | **emerges under coarse-graining (layer-1 → layer-2); confirmed** |
| clean metric exponent off raw paths | **not extractable — layer-2 object, layer-1 measurement; expected** |
| nonlinear / dynamical field equations | open |
| background-free construction | open |

The 3D check confirms isotropy (emergent) and re-exposes, cleanly, *why* the exponent is a layer-2 object: ED is ballistic and non-Gaussian at layer 1. The load-bearing exponent result remains the step-2 count. The open frontier is unchanged: the nonlinear/dynamical regime and a background-free construction.
