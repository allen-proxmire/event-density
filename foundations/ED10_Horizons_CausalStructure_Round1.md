# ED-10 — Horizons, Causal Structure, and Boundary Formation (Round 1)

**Causal-structure foundations arc. Not a GR derivation, not a corpus edit, not a new primitive.**
Analyzes how ED's emergent geometry produces horizons, causal cones, and determinability boundaries — **without requiring full EFE.** Builds only on established results: Phase-3 GR Rounds 2 & 4, A1, A2, and the V1/V5 kernels.
**Framing:** the corpus *already* has horizons (V5-saturated surfaces, Papers 039/047.5) with no EFE. This arc's contribution is the **unification** of those horizons with the A1/A2/Round-4 substrate-evaluation results into one geometric object, plus a **causal-type taxonomy**.

---

## 1. Horizon formation — the spatial sector

A horizon is a **metric degeneracy surface**. From Round 4, `g_ij ~ b_ij⁻¹` → ∞ as `b → 0`: the metric degenerates exactly where bandwidth collapses. The Round-2 admissible bandwidth dynamics (commitment-reserve drain) is what drives `b → 0`. So **a horizon is the surface the bandwidth-collapse rule produces, read through the emergent metric** — no EFE required, only (i) the admissible collapse mechanism and (ii) the `g ~ b⁻¹` degeneration.

**Stable vs transient.** The Round-2 admissible rule is **monotone** (reserve consumed irreversibly; P11). So once `b → 0`, it stays — **the horizon is stable/permanent by P11 irreversibility**, the same protection B4 found freezes committed facts. A *transient* horizon would require reversible bandwidth (replenishment), which Round 2 found **inadmissible**. So ED's horizons, formed by the admissible rule, are classically permanent — exactly the classical black-hole behavior. (The slow non-permanence — Hawking evaporation — is a *separate* effect: the **V5 finite memory** `τ_V5` permits leakage across the otherwise-frozen surface, the corpus's existing Hawking mechanism, Papers 040/047. So: P11 → classically stable horizon; V5 finite memory → slow quantum leak.)

**Identity with V5-saturated horizons.** V5 mediates cross-chain correlations; the corpus horizon is `Γ_cross → 0` (cross-chain bandwidth collapse, 039/047.5). That **is** a `b → 0` collapse — of the cross-chain/adjacency band. So **the V5-saturated horizon, A2's emergent cut, and Round-4's metric degeneration are the same `b → 0` locus** seen three ways (cross-chain / graph-cut / metric). The arc unifies them.

## 2. Causal structure — the temporal sector

The V1 retarded kernel (GR1/T18) supplies the causal cone: forward-only support `θ(t−t')`, propagating at the finite-width bandwidth-limit speed `c` (T8/N1). This is ED's light-cone analogue.

**Interaction with `b → 0`.** As `b → 0`, `g ~ b⁻¹ → ∞`: metric distances across the surface diverge, so a V1 signal's *coordinate* crossing speed → 0 — a signal approaching the surface slows asymptotically, never crossing in finite coarse-grained time. This is the **infinite-redshift surface** of a horizon. Whether the block is *exact* or *only in the limit* depends on the scale:

- **Discrete substrate:** `b` can reach **exactly 0** (a zero-weight edge → inadmissible → the front cannot cross). **Exact block** — and this is precisely **A1's capacity = 0**.
- **Thick-regime continuum:** `b → 0` asymptotically → an asymptotic infinite-redshift surface (never crossed in finite time).

So **A1's discrete exact-zero capacity is the substrate-level version of the continuum infinite-redshift horizon.** The horizon blocks V1 propagation exactly at the discrete level and asymptotically in the continuum — two faces of one surface.

## 3. Determinability boundaries — unifying A1/A2, and the causal-type taxonomy

The `b → 0` surface is the common locus; its **causal *type*** depends on the *directionality* of the collapse and the V1 cone:

- **Two-way (reciprocal) `b → 0`** — the certified A2/A1 case (symmetric edge, decoupled both directions). Nothing crosses either way: **A1's capacity = 0 in both directions.** This is a **determinability boundary** = a **cosmological/domain-type horizon** (two regions mutually causally disconnected). The two regions are severed *now* but, per A1, may carry a **common-cause correlation from a shared past origin** — which is *exactly the cosmological horizon problem* (CMB patches causally disconnected today, correlated via a shared early-universe origin). A1's "observational, not transmission" finding is therefore not in tension with "horizon" — it **is** the causal-disconnection signature of a two-way horizon, plus the shared-past structure that two-way horizons generically have.
- **One-way (directional) `b → 0`** — the `boundary.py` per-direction hook (decoupled in one direction only). Capacity = 0 *outward*, nonzero *inward*: a **one-way membrane = black-hole-type horizon.** A1's symmetric exact-zero does **not** apply here (capacity is asymmetric); the directionality is supplied by the **V1 retarded cone** (which way is "out").

So: determinability boundary (A1/A2, two-way) and black-hole horizon (one-way) are the **same geometric locus** (`b → 0`) of **distinct causal type** (two-way vs one-way) — distinguished by reciprocal-vs-directional collapse + V1 cone orientation. This refines the V5 horizon-universalization result (047.5: four horizon types = one V5 surface) by supplying *what distinguishes the types*: their causal directionality on the shared `b → 0` surface.

## 4. Geometry assembly

Per Round 4: space (`g_ij ~ b⁻¹`) + time-arrow/cone (V1 retarded, finite-width `c`) assemble into a causal-structure manifold `ds² = −c²dt² + g_ij dx^i dx^j`. **Static (non-rotating) horizons assemble cleanly** — Schwarzschild-like surfaces need no cross-terms. **Rotating horizons** (Kerr-like, ergosphere/frame-dragging) need the cross-terms `g_0i`, which require a **directed bandwidth flux** (Round 4's contingent gap) — present only dynamically, not in the static reciprocal baseline. So static horizons are in hand; rotating horizons inherit Round 4's directed-flux condition.

## 5. Mapping table

| Object | Mechanism | Relation to the others |
|---|---|---|
| **`b → 0` surface** (Round 4) | bandwidth collapse (Round-2 rule) | **THE common locus** |
| **A2 emergent cut** | reciprocal `b→0`, P11-frozen | **same** as `b→0` surface (two-way) |
| **A1 determinability boundary** | reciprocal cut, capacity 0 both ways | **same** as two-way `b→0`; supplies the capacity-0 + common-cause signature |
| **V5-saturated horizon** (039/047.5) | `Γ_cross → 0` (cross-chain band collapse) | **same** as `b→0` surface (cross-chain band) — the corpus horizon object |
| **V1 cone** | retarded forward-only propagation | **distinct** — the causal-structure *overlay* that sets horizon *type*, not a surface |
| **Black-hole horizon** | one-way `b→0` + V1 cone blocked outward | **conditionally identical** to the `b→0` locus; **distinct causal type** (one-way; A1's two-way capacity-0 does not apply) |

## 6. Verdict

**ED supports horizon formation, causal cones, and determinability boundaries as a unified geometric picture — *without* full EFE.** Every ingredient is already established: the `b → 0` collapse (Round-2 admissible rule), the metric degeneration (Round-4 `g ~ b⁻¹`), the causal cone (V1 retarded), the capacity-0 signature (A1), the permanence (P11), the corpus horizon object (V5-saturation). They are **the same `b → 0` locus**, with causal *type* (two-way determinability / cosmological vs one-way black-hole) set by collapse-directionality + V1 cone. The EFE keystone (the Round-3/4 covariance/Bianchi computation) is **not** needed for horizon *existence, permanence, causal character, or determinability signature**.

**The one thing that *does* still need EFE:** the **quantitative placement** of a horizon — *where* it forms given a mass (the Schwarzschild radius from `T`). That requires the `curvature = source` field equation (the EFE keystone) to fix `g` from the matter distribution. So the honest split is: **qualitative/structural horizon formation = YES, without EFE (conditional on the admissible Round-2 bandwidth rule); quantitative horizon placement = needs EFE.** This matches and tightens the corpus's existing V5-horizon results, now unified with the determinability-boundary program.

## 7. Round-2 (ED-10) questions

1. **Directional decoupling.** Formalize one-way `b → 0` (the `boundary.py` per-direction hook) — does V1 retardation naturally select the *outward* direction to block, giving a black-hole-type one-way membrane from the kernel alone?
2. **Exact ↔ asymptotic.** Relate the discrete exact-`b=0` block (A1 capacity 0) to the continuum infinite-redshift surface quantitatively (DCGT).
3. **Hawking rate.** Does the V5 finite memory `τ_V5` give a leakage rate across the P11-frozen horizon matching the Hawking temperature? (Connect to 040/047.)
4. **Cosmological horizon problem.** Does A1's common-cause structure across a two-way horizon reproduce the CMB-correlation/horizon-problem structure (disconnected now, shared past)?
5. **Rotating horizons.** Does directed bandwidth flux (Round-4 cross-terms) yield an ergosphere/frame-dragging structure?
6. **EFE-dependent placement.** Confirm that only the *quantitative* horizon radius (not its existence/type) depends on the EFE keystone — isolating exactly what ED-10 can and cannot do without Phase-3 GR closure.

---

*Round-1 ED-10 causal-structure analysis only. Verdict: ED supports horizon formation, causal cones, and determinability boundaries as one `b → 0` geometric picture WITHOUT full EFE (conditional on the admissible Round-2 bandwidth rule); only the quantitative horizon placement needs the EFE keystone. Unifies A1 (capacity 0) + A2 (emergent cut) + Round-4 (metric degeneration) + V5 (saturated horizon) as the same surface, with causal type set by collapse-directionality + the V1 cone. No corpus edits, no new primitives, no speculative physics.*
