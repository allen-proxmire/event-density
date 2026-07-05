# Path-B First Result: a Displaceable but Non-Ordering Director — the Arc's Order Parameter Is Not Yet Grounded in the Certified Substrate

**Author:** Allen Proxmire
**Arc:** Bullet_Arc (ED-Bullet-01) — Phase-3 (theory, Path B first step)
**Status:** Measured result on the certified substrate. Probe: `nu_pathB_orderparameter_probe.py`. Follows `Paper_ED_Bullet_Phase3_NuScope` (which redirected from measuring ν to first identifying whether the arc's order parameter exists in the primitives). Honest mixed result, tiered.
**Headline:** On the certified 2D Σ-substrate, the dynamical sector produces a director field (commit-flow) that is *decoupled from the density* (displaceable, the one arc-critical property) but is *only short-range coherent* and shows *no topological-defect capacity beyond noise*. The reason is structural, not statistical: the Σ-rule is orientation-blind, so there is no director–director coupling to build long-range order or protected windings. The arc's ordering-S²-field-with-monopoles premise is therefore **not grounded in the certified primitives**; it lives entirely in an assumed coarse-grained coupling the certified rule does not supply.

---

## 1. The question this probe actually answers

`Paper_ED_Bullet_Phase3_NuScope` showed ν cannot be measured on the certified substrate (orientation is inert and 2D), and redirected to the prior question: is there, in ED's *dynamical* sector, an emergent director field that can (a) order and carry topologically protected windings, and (b) be displaced from the matter, so the winding can sit offset from the gas (the Bullet)? This probe asks that on the real simulator, avoiding the hand-built-stand-in trap by *reading a derived field off the certified run* rather than adding any coupling.

Two candidate directors, both derived from a certified run (no rule change):
- **grad-rho** — the density gradient. Density-slaved by construction, so the null: it cannot be displaced from the matter.
- **commit-flow** — the coarse-grained direction fronts actually propagated (the frozen record of past becoming, from the commit log). The arc-relevant candidate: it carries the memory of motion, not the current density.

Grounding limit, stated up front: the certified sim is spatially 2D and its orientation is 2D, so any emergent director is O(2) at most — vortices ($\pi_1(S^1)=\mathbb{Z}$), the 2D analog of the arc's O(3) monopoles ($\pi_2(S^2)=\mathbb{Z}$), never the monopoles themselves. This probe tests the *kind* (coherent? displaceable? defect-capable?), not the O(3) form or ν, which need a 3D substrate.

## 2. What was measured (12-seed average, certified 51×51 Σ-substrate)

Per run: ~283 commits, ~68 active coarse cells. The low fill is itself a real feature — the certified fronts extinguish (sparse becoming), so the frozen flow record is sparse.

| Test | Result | Read |
|---|---|---|
| **(A) Coherence** C(r=1), commit-flow | real $+0.116\pm0.020$ vs shuffle $+0.005\pm0.019$ | a genuine coherent director (~5σ), but **short-range only** (gone by r=2) |
| (A) Coherence, grad-rho (reference) | real $+0.186\pm0.020$ vs shuffle $-0.035$ | density gradient is smoother, as expected |
| **(B) Decoupling** $\lvert\cos(\text{flow},\nabla\rho)\rvert$ | $0.587\pm0.011$ vs random baseline $0.637$ | commit-flow is **decoupled from density** (even slightly below random): displaceable ✓ |
| **(C) Topological capacity** $\lvert w\rvert$/plaquette, commit-flow | real $0.345\pm0.032$ vs shuffle $0.331\pm0.036$ | **no signal**: windings are at the random-field level |

## 3. What is grounded, and what is not

**Grounded (measured, real):** the dynamical sector produces a director — commit-flow — that is **displaceable from the matter**. Its alignment with the density gradient sits at (slightly below) the random baseline, so it is genuinely not density-slaved. This is the single property the Bullet mechanism most needs at the base level: a directional field that can carry a frozen record offset from the gas. That property is real in the certified primitives.

**Not grounded (measured absent, at this scale):** the two properties the *topological-defect* mechanism actually rests on —
- **Long-range orientational order.** commit-flow is coherent only over one coarse cell; there is no order parameter that stays finite over the field. A protected texture needs a genuinely ordered background to be protected *in*; this substrate does not supply one.
- **Topological-defect capacity.** The vortex-winding content of commit-flow is indistinguishable from a random field. The substrate shows no tendency to form the integer windings that are the whole mechanism (even in their 2D O(2) vortex form).

## 4. Why this is structural, not a statistics artifact

The natural objection is that a 51×51, sparsely-committed 2D toy is too small to show long-range order or count vortices, and that a bigger or 3D substrate would. That is partly fair, and the O(3)/3D limit is real. But the deeper reason is mechanistic and does not go away with size:

**The certified Σ-rule is orientation-blind (hard invariant), so there is no director–director coupling.** Long-range orientational order and protected windings are *produced by* an aligning interaction between neighboring directions (an exchange/stiffness term). The certified rule has none — selection reads density and graph-local structure only, never orientation or flow direction. The short-range coherence in (A) is just local continuity of front propagation (a front tends to keep going the way it was going across one cell), not an ordering interaction. With no coupling, there is no mechanism to grow that local continuity into long-range order or to stabilize a winding against smoothing. So the absence in §3 is what the orientation-blind rule *predicts*, not a resolution limit.

This closes the loop with the ν-scope: the same orientation-blindness that makes ν unmeasurable also makes the ordering and the defects unmeasurable, for one reason — there is no coupling in the director sector.

## 5. What this means for the Bullet arc, honestly

The Bullet topological-defect mechanism assumes a cluster-scale organizational field that (i) orders on S² and (ii) supports protected monopoles. This probe shows that, at the level of the certified primitives, **(i) and (ii) are not present** — only displaceability is. The ordering and the topology are therefore **assumed at the coarse-grained level**, resting on an effective director–director coupling that the certified rule does not contain and that has not been shown to emerge from coarse-graining.

Tiered plainly:
- **Displaceable dynamical director:** measured, grounded (§3).
- **Long-range order + topological-defect capacity:** not present in the certified rule; assumed at coarse-grained level; **the load-bearing open gap under the whole arc**, now localized precisely.
- The arc is not refuted — a real emergent coupling could arise on coarse-graining a 3D substrate — but the mechanism's two central requirements are shown to be *inputs*, not *outputs*, of the primitives as certified. That is a sharper and more honest statement of the arc's status than "account with two open ingredients."

## 6. The fork this creates, and the recommendation

Path B's real content is now singular and clear: **does an aligning (ordering) director coupling emerge when the substrate is coarse-grained, or must it be added by hand?** Two routes:

- **The honest, hard route:** show from the primitives that coarse-graining the orientation-blind rule generates an effective stiffness for a derived director (e.g. commit-flow) at cluster scale — i.e. that order-blindness at the micro scale gives way to an ordering interaction at the macro scale. If it does, the class of that interaction (O(2)? O(3)? on a 3D substrate) fixes the topology and ν. If it does not, the arc's order parameter has no substrate home and the topological-defect mechanism needs rebuilding on a different field. This is the genuine emergent-free-energy problem, and it is a research program, not a probe.
- **The trap to refuse:** add an O(3) alignment term, run it in 3D, and "find" ordering with monopoles and ν ≈ 0.70. That measures the coupling you inserted, not ED.

Recommendation: **do not build the inserted-coupling version.** State the arc's ordering + topology as assumed inputs (this note does), keep the observational protocol as the live, grounding-independent test, and treat "does an ordering director coupling emerge from coarse-graining?" as the one real theory target — the same emergent-free-energy question that also sits under curvature emergence. It is the honest next step, and it is bigger than the Bullet.

## 7. Honest scope

One certified substrate, 2D, 51×51, 12 seeds, sparse commit records; O(2) at most by construction. The displaceability result is robust within that; the order/topology negatives are structural (traced to orientation-blindness) but were *measured* only at this scale and in 2D, so they are stated as "not present / not grounded in the certified rule," not as "impossible in a 3D emergent field." The probe reads derived fields off the real simulator and adds no coupling, so it is grounded, but it cannot reach the O(3) form or ν, which need a 3D substrate and, first, a demonstrated ordering interaction.
