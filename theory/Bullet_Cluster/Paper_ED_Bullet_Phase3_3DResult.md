# The 2D Cap Lifted: Even in 3D, With Monopoles Reachable, the Certified Rule Produces No Spontaneous Order

**Author:** Allen Proxmire
**Arc:** Bullet_Arc (ED-Bullet-01) — Phase-3 (theory), the decisive test
**Status:** Measured result on the certified substrate, 3D. Probe: `emergent_3d_director_probe.py` (monopole-charge code validated on a synthetic hedgehog first). Closes the emergent-free-energy question for the commit-flow director by removing the one caveat that limited every prior probe: dimensionality.
**Headline:** Running the certified Σ-rule on a 3D lattice graph — the *same certified rule*, only the edge set changes — makes O(3) and π₂(S²)=ℤ hedgehog monopoles genuinely reachable for the first time. With the topological-charge tool validated (hedgehog Q=+1.000, uniform Q=0.000) and a dense run (12,347 commits, 336 closed cubes), the result is a clean, decisive negative: **no spontaneous long-range order (the director is anti-correlated at range — outward splay from seeds, not alignment), no monopole capacity beyond noise (smoother than random), only a displaceable, short-range-coherent, common-cause-textured director.** Persistence did not help (accumulated ≈ momentary). The arc's ordered-S²-field-with-protected-monopoles premise is **not grounded in the certified primitives, in 2D or 3D**, and the cause is structural: orientation-blindness means no aligning coupling, so the only structure available is common-cause, not order.

---

## 1. Why 3D settles what 2D could not

Every prior probe in this arc carried the same caveat: the certified `Bits` simulator ran on a 2D grid, so its emergent directors were O(2), capable at most of vortices (π₁(S¹)=ℤ), never the O(3) hedgehog monopoles (π₂(S²)=ℤ) the Bullet mechanism actually needs. Each negative could therefore be waved off as "maybe 3D is different."

That caveat was never fundamental. The certified Σ-rule is **graph-based** (`ParticipationGraph`, arbitrary edges) and **orientation-blind** (reads rho and graph-local structure only). Running it on a 3D lattice graph changes nothing about the rule — only the edge set. It is the certified rule, not a stand-in. And on a 3D lattice, the spatial commit-flow director is a genuine **3D vector field**, so it *can* host hedgehog monopoles. This probe does exactly that, so the O(3)/monopole question is asked, grounded, for the first time.

**Tool discipline (chains-as-links lesson).** The 3D topological-charge computation (solid-angle sum over each cube's outward-oriented surface triangulation, Van Oosterom–Strackee) was validated before use: a synthetic radial hedgehog returns Q = +1.000 and a uniform field returns Q = 0.000. The tool is trustworthy; the substrate numbers below are not a tooling artifact.

## 2. What was measured (certified 3D Σ-substrate, 24³, dense seeding, 6 runs, block B=3)

Per run: ~12,347 commits, ~511 filled coarse blocks, ~336 closed cubes for the charge computation. Both the *momentary* director (first commit into a node) and the *accumulated* director (all commit displacements through a region — a persistent memory field) were measured, since the emergent-free-energy result suggested a persistent field might survive sparse becoming where the momentary one washes out.

| Test | Result | Read |
|---|---|---|
| **(a) Ordering** C(r), accumulated | r=1 +0.043 (vs shuffle +0.008); long-range r≥4 = **−0.016 ± 0.006 vs shuffle +0.009, −4.2σ** | weak short-range coherence, then **long-range ANTI-correlation** — not order |
| **(b) Monopoles** total\|Q\|/cube | real 0.305 ± 0.012 vs shuffle 0.359 ± 0.015; net Q ≈ +8.6/run | **smoother than random** (fewer windings); net charge is just seed sources, not spontaneous monopoles |
| **(c) Displaceability** \|cos(flow, ∇rho)\| | accumulated 0.496 ± 0.005, momentary 0.499 (3D-random baseline = 0.500) | **decoupled from density** — displaceable ✓ |
| Persistence (accumulated vs momentary) | r=1: +0.043 vs +0.044; both anti-correlate at range | **the persistent field behaves like the momentary one — persistence did not help** |

## 3. Reading it

**No spontaneous ordering.** The short-range coherence is weak (+0.043, far below the 2D +0.14, itself just local front continuity), and the long-range correlation is *negative*, four sigma below the shuffle floor. That is the opposite of ferromagnetic order. Its physical origin is transparent: with the volume seeded at ~5% and fronts emanating outward from each seed, distant regions carry oppositely-directed flow — an outward-**splay** texture. Splay is a common-cause pattern imposed by the initial seed distribution, not a spontaneously-aligned phase. There is no aligning tendency; there is seed-imprinted divergence.

**No monopole capacity.** With the tool validated and monopoles now geometrically possible, the field's total winding content is *below* a random control — it is smoother than random, hosting *fewer* defects, not more. The net charge (~+8.6) simply counts the seed regions as sources (each outward-splaying seed is a +1 source); it is not a population of spontaneous, protected bulk monopoles. The arc needs the field to spontaneously support stable protected windings against a robust ordered background; the certified rule supplies neither the background nor the windings.

**Displaceable — the one property that survives.** As in 2D, the director is cleanly decoupled from the density gradient (0.496 ≈ 0.500), so it *can* be offset from the matter. This is the single arc-relevant property the certified primitives do produce, and it is robust across 2D and 3D.

**Persistence was not the missing ingredient.** The accumulated (memory) field, built to let common-cause correlations survive sparse becoming, behaves essentially identically to the momentary flow. So the failure to order is not a sparse-becoming washout that a longer memory would cure; it is the absence of an aligning interaction in the first place.

## 4. The verdict, now without the dimensional caveat

Across 2D and 3D, with the O(3)/monopole question genuinely reachable and the measuring tool validated, the certified Σ-rule produces a **displaceable, short-range-coherent, seed-splay director** and **not** the robust ordered S² field with spontaneous protected monopoles the Bullet topological-defect mechanism requires. The root cause is one fact, visible from the start and now confirmed at every scale: **Σ is orientation-blind, so there is no director–director aligning coupling, so the only long-range structure available is common-cause (shared seed/front history), which produces splay textures and net source-charge, never spontaneous ordering or protected defects.**

For the arc, this settles the grounding question in the negative, cleanly:

- **Grounded (output of the primitives):** a director that is displaceable from the matter. Real, robust.
- **Not grounded (not outputs, in 2D or 3D):** long-range orientational order; spontaneous topological-defect (monopole) capacity. These are **inputs** the mechanism assumes at the coarse-grained level, resting on an aligning coupling the certified rule does not contain and that does not emerge from it — not from coarse-graining (the emergent-free-energy probe), not from persistence (the accumulated field), and not from lifting to 3D (this probe).

## 5. What this does and does not mean for the Bullet arc

It does **not** falsify the Bullet phenomenon or the observational test. The offset–velocity protocol stands untouched; it needs only that *some* ordering transition occurs in the real 3D cluster field, and this probe speaks to the certified microrule, not to whether a coarse-grained astrophysical field (built from physics the toy substrate does not include — actual gas, gravity, magnetic fields) could order.

It **does** mean, honestly, that the topological-defect *mechanism's* microscopic grounding in ED's certified primitives is now a measured negative, not an open hope. The mechanism is a coarse-grained **model** whose ordered-field-with-monopoles ingredient is an assumed input with no home in the certified rule. That is a sharper and more honest status than "account with two open ingredients," and it was reached by exhausting the grounded routes (coarse-graining, persistence, 3D) rather than by assumption.

## 6. Where the residual actually lives now

The honest next question is no longer "does the commit-flow director order?" — measured, no, in 2D and 3D. It is: **is there any organizational field at all whose ordering is an output of ED's primitives, or does every route require an aligning coupling the orientation-blind rule structurally lacks?** The candidates left are not derived directors of the certified rule (those are exhausted) but fields from *extended* primitives — and adding an aligning rule is the trap (it measures the insertion, not ED). So the realistic options are two, both honest:

1. **Accept the topological-defect mechanism as a coarse-grained model** whose ordering ingredient is an input, not derived, and let the **observational test** decide it empirically. The mechanism can be right about the cluster field even if the certified toy does not display the ordering, because the cluster field carries physics (gas, gravity) the toy omits.
2. **Path C for the number:** carry ν ≈ 0.70 (3D O(3)) as a flagged assumption to give the offset–velocity paper a concrete knee, tiered as inherited.

The one thing now firmly closed: expecting the ordering to *emerge from the certified primitives themselves* — it does not, and 3D was the last caveat standing.

## 7. Honest scope

One certified rule, 3D lattice, 24³, dense seeding, 6 runs; the monopole tool validated on synthetic fields. The negatives (no spontaneous order, no monopole capacity) are measured with O(3) genuinely reachable, so they are not dimensional artifacts; they are traced structurally to orientation-blindness. The long-range anti-correlation depends on the seed distribution (splay from distributed sources); a single-region "merger" seeding would change the *texture* but not the core finding (no aligning coupling ⇒ no spontaneous order), since that finding rests on the absence of a director–director term in the rule, which no seeding changes. The result speaks to the certified microrule; it does not claim a coarse-grained astrophysical field with additional physics cannot order.
