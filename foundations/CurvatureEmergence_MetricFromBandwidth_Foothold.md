# Curvature-Emergence Foothold: a Metric Emerges from Bandwidth-Connectivity, and It's g ~ 1/b

**Foundations — gravity / curvature-emergence arc. First runnable foothold into the deep open bridge under 3D, the area-law geometry, and the horizon location: how does a metric with a length scale emerge from a participation graph whose edges carry no length? Probe: `evaluation/CurvatureEmergence/metric_from_bandwidth_probe.py`. Result: a metric genuinely emerges from the raw graph's bandwidth-connectivity (unweighted hop-distance, no assigned lengths), it shows the curvature signature (a bandwidth depletion — a "mass" — reads as *far*), and it recovers GR-I's g ~ 1/b **exactly** under a natural connectivity law (reach ∝ √b), with the emergent metric exponent tracking the law to R² = 1.000. Tier: measured foothold. What it clears: a metric emerges, curvature appears, GR-I's power is reachable under a non-arbitrary law. What stays open: deriving that law from the substrate, the length scale (ℓ_P), the nonlinear regime, and a genuinely background-free construction.**

## 1. The question, scoped

GR-I *assigns* the emergent spatial metric g ~ 1/b (bandwidth field) at the continuum level. The deep open bridge is one level below: does the **raw graph** — connectivity only, no assigned lengths — actually *produce* distances that reproduce g ~ 1/b, or a different metric, or none? This is the piece Paper_039 §3.2 defers to (it borrows the horizon location r_H from GR for exactly this reason), the piece under the area-law probe's assumed geometry, and the second half of the 3D premise. This note is the first foothold, not the bridge.

## 2. The probe (non-circular by construction)

Nodes sit on a background **label** line (a bookkeeping index, not a metric). A bandwidth field b(x) varies along it: baseline 1, a Gaussian depletion to b_min = 0.2 — a "mass" that lowers the local bandwidth. Bandwidth enters **only through connectivity**: a higher-bandwidth node reaches further (b = participation capacity, P04), reach ∝ b^p. The emergent distance is then the plain **unweighted hop-count** (BFS) between nodes — read off the structure, never assigned. The trap from the chains-as-links work (assigning the answer by hand) is avoided: the metric exponent is *measured* from the emergent hop-distance, not put in.

What g ~ 1/b means, so we know what to look for: proper distance ds = dx/√b, i.e. hop-distance ~ ∫ dx/b^{1/2}. Generally, if hop-distance ~ ∫ dx/b^q then the emergent metric is g_xx = 1/b^{2q}, so **q = 1/2 ↔ g ~ 1/b (GR-I)** and q = 1 ↔ g ~ 1/b².

## 3. Result

**A metric emerges, and low bandwidth is far.** For every connectivity law tested, the hop-distance across the bandwidth dip exceeds the flat-bandwidth reference (+87 hops at reach ∝ √b, +250 at reach ∝ b). A depletion in bandwidth stretches distances — the qualitative curvature signature: a mass makes space "longer" around it, from connectivity alone.

**The emergent metric is clean and its exponent tracks the law exactly.** Fitting the hop-distance to ∫ dx/b^q gives R² = 1.000 in every case, and the emergent q tracks the connectivity exponent p almost perfectly:

| connectivity law (reach ∝ b^p) | emergent metric exponent q | metric |
|---|---|---|
| p = 0.25 | 0.25 | g ~ 1/b^0.5 |
| **p = 0.50** | **0.50** | **g ~ 1/b  (GR-I)** |
| p = 0.75 | 0.75 | g ~ 1/b^1.5 |
| p = 1.00 | 1.05 | g ~ 1/b² |
| p = 1.25 | 1.20 | g ~ 1/b^2.4 |

**GR-I's g ~ 1/b is recovered exactly at reach ∝ √b**, and √b is a *natural* law, not a tuning: read bandwidth as a capacity (area-like, a count of participations) and reach as a linear scale, and linear ∼ √area gives reach ∝ √b directly. So the substrate's own metric assignment (GR-I) sits at a physically-motivated point in the space of connectivity laws, not an arbitrary one.

## 4. What this clears, and what stays open

**Cleared (measured foothold):**
- A metric genuinely emerges from pure graph structure — bandwidth-connectivity produces a well-defined distance (R² = 1.000), not the trivial label-distance.
- The curvature signature is present: a bandwidth depletion (mass) reads as increased distance. Gravity's basic effect appears from connectivity.
- GR-I's specific g ~ 1/b is reachable, and reachable under a natural connectivity law (reach ∝ √b), not a fine-tuned one.

**Open (this is a foothold, not the bridge):**
- **The connectivity law is chosen, not derived.** The probe shows reach ∝ √b gives g ~ 1/b and offers a natural reading for it, but it does not *derive* reach ∝ √b from the primitives. That derivation — why bandwidth sets reach as √b — is the real next step.
- **The length scale is not addressed.** This gives the metric's *shape* (how distance varies with b), not its absolute scale (the tie to ℓ_P). The scale is still inherited.
- **Background-free is not reached.** A 1D label line and its topology are assumed; the metric emerges *on* that index. The distances are genuinely emergent (they stretch with 1/b, not with the index), but the index/topology itself is not derived from a truly background-free graph.
- **Linear/static only.** This is a static bandwidth field; the nonlinear, dynamical regime (the full field equations) is untouched.

## 5. Status

**The curvature-emergence bridge's first foothold is cleared, positively.** A metric emerges from the raw bandwidth-connectivity, it shows curvature (mass → distance stretches), and it recovers GR-I's g ~ 1/b under a natural connectivity law. This converts "does a metric come out of the graph at all" from an open question into a measured yes, and isolates the sharp next target: **derive the b → reach law (why √b)** from the substrate primitives, which would turn "g ~ 1/b is reachable" into "g ~ 1/b is forced." The length scale (ℓ_P) and the nonlinear field equations remain beyond this foothold, and are the rest of the bridge.
