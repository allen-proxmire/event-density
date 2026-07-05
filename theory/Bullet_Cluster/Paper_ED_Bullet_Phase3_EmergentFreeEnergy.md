# The Emergent-Free-Energy Question: a Faint Common-Cause Thread, Not a Robust Ordering Coupling

**Author:** Allen Proxmire
**Arc:** Bullet_Arc (ED-Bullet-01) — Phase-3 (theory)
**Status:** Measured result on the certified substrate. Probe: `emergent_free_energy_probe.py`. Attacks the one next target set by `Phase3_Status_and_NextTarget` / `Paper_ED_Bullet_Phase3_PathB_FirstResult`: does an ordering director coupling *emerge* when the orientation-blind substrate is coarse-grained, or must it be added by hand? Honest, weak-positive result, tiered carefully so it is neither over- nor under-sold.
**Headline:** Beyond a strong short-range coherence and a weak global drift, the emergent commit-flow director carries a **statistically real but physically tiny** long-range correlation (+0.005 above the drift floor, 3.1σ over 80 randomized-seed runs). This is a faint **common-cause** residual (shared front history), exactly the only kind of long-range correlation an orientation-blind rule can produce, and it is far too weak to constitute the robust ordered field with protected defects the arc needs. **The ordering coupling does not robustly emerge from coarse-graining; a faint common-cause thread survives, not nothing.**

---

## 1. The question, and how to answer it without cheating

The Path-B first result showed the certified substrate gives a *displaceable* director (commit-flow) but only short-range coherent, with no topological-defect signal, traced to Σ being orientation-blind (no micro director–director coupling). The open question was whether coarse-graining nonetheless produces an *effective* ordering interaction — the emergent-free-energy question. The trap is to insert an O(3) coupling and "find" ordering; that measures the coupling you inserted. The honest route is to read the real substrate and ask whether an ordering interaction is already implicit in the front dynamics.

The non-circular diagnostic used here: the **long-range behavior of the direction correlation** C(r) = ⟨n(0)·n(r)⟩ of the derived commit-flow field, tested against a **direction-shuffle baseline** (same nodes and positions, directions randomly re-paired). A shuffle removes all spatial structure but preserves the global mean, so it isolates the drift floor |⟨n⟩|². If real C(r) at large r decays to the shuffle floor, the field is disordered (no emergent coupling). If it holds significantly above the floor, an ordering correlation has emerged. Seeds were **randomized** across runs so any surviving long-range signal is intrinsic, not fixed-geometry artifact.

(A first attempt used order-parameter scaling M ∼ N^α; it failed — the accessible N range was too narrow and the scatter swamped it, R² = 0.01, with the shuffle control not even reaching the −1/2 it must. That method is not reportable at these scales; the correlation-function route below is the reliable one.)

## 2. What was measured (80 runs, certified 2D Σ-substrate, randomized seeds, sides 41–65)

| r | C_real (mean ± SE) | C_shuffle (mean ± SE) | real − shuffle |
|---|---|---|---|
| 1 | +0.141 ± 0.004 | +0.006 ± 0.003 | **+0.135** |
| 2 | +0.023 ± 0.004 | +0.005 | +0.018 |
| 3–4 | ~+0.012 | ~+0.008 | ~+0.004 |
| 5 | +0.024 ± 0.004 | +0.009 | +0.015 |
| 6–10 | ~+0.013 | ~+0.007 | ~+0.007 |
| 11–14 | ~+0.008 | ~+0.008 | ~0 |

**The decisive quantity — the long-range plateau (r ≥ 5):**
- C_real = +0.0124 ± 0.0013
- C_shuffle = +0.0075 ± 0.0009
- real − shuffle = **+0.0049, at +3.1σ**

Three facts to hold together:
1. **Short-range coherence is strong** (r=1: +0.135 above shuffle) — local front continuity, as before.
2. **There is a weak global drift** — the shuffle floor is +0.0075, not zero, i.e. |⟨n⟩| ≈ 0.09: the field has a faint net direction.
3. **Beyond that drift, a faint long-range correlation is real** — +0.005 above the shuffle floor at 3.1σ, roughly flat over r = 5–10, fading by r ≈ 11–14.

## 3. Reading it honestly (neither over- nor under-sold)

**Do not call this "ordering emerges."** The long-range excess is 0.5% alignment, against 14% at short range. It is statistically detectable but physically tiny. It is not a robust ordered phase, and it is nowhere near strong enough to support a stable, protected texture: a winding needs an ordered background to be protected *in*, and a 0.5% long-range correlation is not that background.

**Do not call it "nothing," either.** The excess is 3.1σ over 80 randomized-seed runs, robust to the fixed-geometry confound. There is a genuine long-range correlation in the emergent director beyond the global drift.

**What it actually is:** a faint **common-cause** long-range residual. Because Σ is orientation-blind, no *interaction* order is possible — the substrate has no term that aligns neighboring directions. The only mechanism that can correlate distant commit-flows is a **shared front history**: one front sweeping through distant regions imprints a common bias on their flow. That is exactly the A1 "common cause, not channel" structure (`Bits/` determinability work), now seen in the director sector: the long-range correlation that exists is shared-origin co-variation, not a coupling. And it is faint because **sparse becoming** (fronts extinguish quickly, ~283 commits on a ~2500-node grid) keeps the shared-history reach short, washing out most of it.

## 4. The answer to the emergent-free-energy question

**The ordering coupling does not robustly emerge from coarse-graining the orientation-blind rule.** What emerges is a faint common-cause long-range correlation, three-sigma-real but physically negligible, sitting on the disordered side of any ordering transition. There is no relevant aligning coupling; there is a weak shared-history thread that sparse becoming nearly erases.

For the Bullet arc this sharpens the Path-B verdict rather than overturning it:
- The arc's requirement of a **robust ordered S² field supporting protected monopoles** is **not met** by the certified primitives, even after coarse-graining. The emergent order is far too weak.
- But the emergent director is not structureless: it has strong short-range order, a weak global drift, and a faint common-cause long-range tail. The *ingredients* of an order parameter are present in miniature; what is absent is the *relevant coupling* that would grow them into a true ordered phase.
- So the honest status of the topological-defect mechanism is unchanged in kind and now measured in degree: its ordered-field-with-defects premise is an **input**, not an emergent output, and the gap between what the substrate supplies (a faint common-cause thread) and what the mechanism needs (a robust ordered phase) is large, not marginal.

## 5. Where this leaves the arc, and the honest options

The emergent-free-energy route has now been tried directly and returns a clear-enough answer at accessible scales: **no robust ordering emerges; the coupling is at most a faint common-cause residual.** That is a real, if deflating, finding, and it is the kind of load-bearing negative the program treats as health.

- **The observational protocol is unaffected** and remains the live test. It needs only that *some* all-or-nothing ordering transition occurs in the real cluster field; it does not depend on grounding that transition in the certified toy, and the certified toy's 2D, sparse, orientation-blind limits do not bind the 3D cluster field.
- **The two honest ways forward** are now clearer than before:
  1. **Accept that the ordered-field premise is an emergent-scale input the certified microrule does not supply**, and either (a) seek the ordering coupling in a *different* derived field (not commit-flow — perhaps a slower, non-extinguishing organizational variable that sparse becoming does not erase), or (b) accept the topological-defect mechanism as a coarse-grained *model* whose microscopic grounding is open, and lean on the observational test to decide it empirically.
  2. **Path C, still the standing fallback:** carry ν ≈ 0.70 (3D O(3)) as a flagged assumption for a working knee number, tiered as inherited, not measured.
- **The trap remains refused:** inserting an O(3) alignment term and "finding" ordering + ν ≈ 0.70 would measure the insertion, not ED.

Net: the emergent-free-energy question is answered at the level a probe can answer it — no robust emergent ordering, a faint common-cause thread — and the residual is honestly relocated once more: from "measure ν" to "is there any derived organizational field, other than the quickly-extinguishing commit-flow, in which an ordering coupling could emerge?" That is a well-posed next question, and it is the natural place to stop and think rather than run.

## 6. Honest scope

One certified substrate, 2D, sides 41–65, 80 randomized-seed runs, sparse commit records; O(2) at most by construction. The measurement cleanly distinguishes presence/absence of long-range order beyond a shuffle baseline and finds a 3.1σ but physically tiny excess. It does not reach the O(3) universality class or ν (which need a 3D substrate and, first, a robust ordering coupling that this probe does not find). The "no robust ordering" conclusion is measured at these scales and structurally expected (orientation-blindness ⇒ common-cause only ⇒ sparse-becoming-suppressed); it is stated as "not present / not robustly grounded in the certified rule," not as "impossible for any emergent 3D field."
