# Does GR-III's Nonlinear (Horizon-Forming) Rule Survive on a Coordinate-Free Graph?

**Date:** 2026-07-26
**Status:** Working note. One **qualitative** result banked; the **quantitative** leg is **not extractable with this rule** and would duplicate an already-known noisy corpus result. Adversarially reviewed against: the archived linear-relational note (`remove from repo/gravity-reinvention-2026-07-09/foundations/CurvatureEmergence_BackgroundFree_RelationalYesTopologyWall.md` — method only, not cited as a result), `Paper_GR-III` (dynamical bandwidth rule), `Paper_MetricFromTheGraph_ForcedTo3D`, `Paper_AreaLawIsTheEdgeCount`, and this folder's own `dynamical_bandwidth_3d.py` / `horizon_entropy_coefficient.py`.

## The question
The corpus already has the **linear/static** curvature-emergence result done coordinate-free: on a random geometric graph (RGG) with coordinates discarded, the graph Laplacian's Green's function goes as `1/k` (hop-distance) in 3D and `log` in 2D (archived note, R²=0.987). What was **never** done relationally is the **nonlinear, horizon-forming** half of `Paper_GR-III`: the rule `ḃ = D∇²b − κρ`, `b≥0`, `b=1` at frame, where a region driven to `b→0` is a horizon. Does that horizon form on a length-less participation graph, or does it secretly need the embedding lattice?

## Setup (`relational_nonlinear_horizon_probe.py`)
Faithful GR-III rule on an RGG: `b += D·(deg⁻¹·A·b − b) − κρ; clip(b,0); b[frame]=1`. Graph is built ~d-dimensional (P06 accepted as input — this tests the *dynamics* are relational, **not** that the dimension is derived). Every **measurement** is graph-intrinsic: hop-distance by BFS, frozen-core radius `r_s` = max hop with `b<10⁻⁶`, surface = straddling-edge count `fz·A·(1−fz)`. Hard lever-arm guard: **no exponent is quoted unless `r_s` spans ≥ 0.7 decade.**

## Result

### Qualitative — SURVIVES (the banked finding)
On the coordinate-free graph the nonlinear clip rule **forms a `b→0` frozen core** — a horizon — in both 3D (N≈120k, dim measured 3.09) and 2D (dim 2.10). The frozen region and its straddling-edge boundary are well-defined graph-intrinsically. **This extends the archived linear-relational result into the nonlinear regime:** not just the `1/r` potential but the horizon itself is a relational object, needing no background lattice.

### Quantitative — INCONCLUSIVE, and here's the honest reason
Sweeping κ over a decade (0.8→32, i.e. 40×) moved `r_s` only **3→5** in 3D and **5→5** in 2D. The guard correctly refused to quote any exponent (0.22 and 0.00 decades of lever arm). This is **not** noise — it's a real property of the elliptic rule:

> **The `b≥0` clip caps the effective injected mass.** Once the source region hits `b=0`, further `κρ` is subtracted from nodes already pinned at zero and does nothing. So the horizon radius is set by diffusion/geometry, not by source strength — cranking κ past the freezing threshold cannot grow `r_s`. `N_frozen` grows (62→151) while `r_s` barely moves: the core deepens/fills, it does not expand.

This is **consistent with GR-III's own statement** that the *elliptic* rule does not give Schwarzschild `r_s∝M` or Hawking `κ∼1/r_h` scaling — those need the hyperbolic rule. The elliptic horizon is real but its radius does not track mass.

## Why we stop here rather than swing again
To grow `r_s` a decade one must sweep the **source size** σ, not κ. But measuring the boundary of a σ-grown frozen ball vs `r_s` **is essentially the archived note's holographic cut-shell measurement** — which the corpus already did and already labels **"roughly holographic but noisy on irregular graphs (≈2.38 in 3D vs target 2); the lattice is the clean version."** A σ-sweep here would, at best, reproduce that known-noisy conclusion. It is **not new**. The clean quantitative area law already lives on the lattice (`Paper_AreaLawIsTheEdgeCount`, r^2.02); the coordinate-free version is already known to be qualitatively-holographic-but-noisy.

Three attempts at a clean *quantitative* coordinate-free horizon-scaling exponent, all correctly rejected (v1 lever 0.15 dec; v2 mass-scaling = linearity tautology + area fit-illusion; v3/this κ-sweep saturates by the clip). That pattern is the signal to bank the sound qualitative result and stop, not to force a fourth.

## Net (tiered honestly)
- **NEW + SOUND (qualitative):** the nonlinear, horizon-forming GR-III rule is **relational** — a `b→0` core forms on a coordinate-free graph. Advance over the archived *linear* relational result.
- **NOT a result here:** any quantitative coordinate-free horizon-scaling (mass-scaling or area-law exponent). The elliptic clip saturates `r_s` (no lever arm), and the area-law-on-graph duplicates the archived noisy cut-shell. The clean area law stays where it already is: the lattice.
- **Unchanged:** curvature emergence overall is still `g∼1/b` derived (reach law forced to 3D holographically, `Paper_MetricFromTheGraph_ForcedTo3D`) + nonlinear Einstein reached two ways (GR-III, khronometric `δQ=TdS`). This probe does **not** move that tier; it closes one specific "is the *horizon* relational too?" sub-question at the qualitative level.

## Files
- `relational_nonlinear_horizon_probe.py` (this probe, v2 — κ-sweep, guarded).
- `dynamical_bandwidth_3d.py` (the faithful lattice GR-III rule).
- `horizon_entropy_coefficient.py` (lattice 1/4 / area-tiling).
