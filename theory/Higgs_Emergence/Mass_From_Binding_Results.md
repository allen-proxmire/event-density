# Mass From Binding: V5-Bound Ballistic Fronts Form a Sub-Luminal Composite — "Mass Without Mass," Surviving the Ballistic-or-Extinct Wall

**Theory / Higgs_Emergence — RAN 2026-07-10 (`mass_from_binding_probe.py`, certified simulator). The mass-sector wall (`H1_Leg_Scoping`) is that the certified rule is *ballistic-or-extinct*: an individual front advances one hop or dies, no sub-ballistic surviving mode, so no INDIVIDUAL rest mass. This probe tests the standard-physics escape — rest mass is mostly BINDING (a box of photons, or quarks+gluons in a proton, has rest mass = internal energy; its COM moves sub-luminally though the constituents move at c). The composite COM is a different object from the individual front. RESULT: V5 finite-reach binding CONFINES ballistic (v=c) fronts into a bound composite that moves SUB-LUMINALLY, with the residual COM drift shrinking toward rest as cluster size grows — rest mass from binding. Crank-rail ON: the caveats (V5 = structural addition, not primitive-forced; binding mass only, fundamental Higgs mass separate) are load-bearing and stated.**

## 1. The test, made faithful
- **Fronts:** 2D grid; each front's per-step choice is the certified `compute_sigma` on the real ρ field. No dwell — the front MUST advance every step (path-speed = 1, the constituent at c), faithful to ballistic-or-extinct. It avoids its own high-ρ trail → moves into fresh ground → ballistic. Ties among equal-Σ fresh neighbors are broken by the front's **orientation/heading** (persistence) — faithful to the certified `(ρ, orientation)` front, since Σ is orientation-blind, so orientation can only break Σ-ties (this reproduces the Continuum paper's ballistic worldline, persistence ~0.7).
- **V5 binding:** its actual known structure — retarded (previous-step positions), finite transverse reach `exp(-|Δr|/ell_V5)` attraction toward the reach-weighted centroid of the *other* fronts. NOT rigged to bind: whether a finite reach can confine `v=c` fronts is the open question — if they outrun it, the probe returns "unbound."
- **Controls:** a single free front (massless, expect `v≈1`); the cluster with V5 off (expect dispersal).

## 2. Results (3 seeds, N=8 unless noted)
| case | outcome |
|---|---|
| **single free front** | `v = 0.98` — ballistic, massless, moves at `c` ✓ |
| **cluster, V5 OFF** | **UNBOUND** — rms grows 28 → 55, fronts radiate away ✓ (control) |
| **cluster, V5 ON** (all `A_V5∈{1,2,4}`, `ell_V5∈{5,15,40}`) | **BOUND** — rms stays **1.4–2.3** (tightly confined); COM moves at **~0.5** (sub-luminal, `< c=0.98`) |

**The finite-reach binding confines ballistic fronts** — rms 55 (unbound) → ~1.5 (bound), robust across every coupling strength and reach tested. And the **bound composite moves sub-luminally** (`v_COM ≈ 0.5 < v_free = 0.98`): it is *massive*, moving slower than its massless constituents.

**The residual COM drift is a finite-N momentum fluctuation → rest in the large-N limit:**
| N | 8 | 16 | 24 | 32 |
|---|---|---|---|---|
| `v_COM` | 0.54 | 0.49 | 0.44 | 0.31 |
| rms_end | 1.4 | 3.0 | 4.7 | 8.6 |

The drift **shrinks monotonically as the cluster grows** (more constituents → better internal-momentum cancellation), consistent with a finite-N fluctuation of a composite that is genuinely at rest in the large-N limit. So a large V5-bound cluster is a **composite at rest whose parts each move at `c`** — the "mass without mass" signature.

## 2b. Inertia (the defining property of mass) — CONFIRMED, with an equivalence-principle twist
Kinematic sub-luminality (§2) is one signature; the *defining* property of mass is **inertia** — resistance to acceleration. Applied a uniform external force (+x) and measured the drift response `v_x`:
- **free front, force F=0.5: `v_x = 0.98`** — at `c`, unresisted (massless: a force only steers it, can't slow it).
- **V5-bound composite, same force: `v_x ≈ 0.72 < 0.98`** — the binding **resists** the force; the composite accelerates *less* than a free front. **It has inertia — it is massive.**

The force response is ~N-independent (rel. mass ≈ 1.0–1.1 across N=8→32). That is not a null — it is the **equivalence principle**: a *uniform* force (like gravity) accelerates all masses equally, so the drift *velocity* is mass-independent (velocity is intensive). The mass *magnitude* (extensive, `∝` internal energy `∝ N` by `E=mc²` — bind more constituents, more rest energy, more mass) lives in momentum/energy, precisely where a uniform force cannot resolve it. So the two facts cohere: the composite **has inertia** (sub-luminal force response, massive) **and** shows **universal acceleration under a uniform force** (equivalence-principle-consistent) — both correct behaviors of mass. *(Tier: sub-luminal force response = measured/solid; the equivalence-principle reading = a consistent interpretation, not independently proven.)*

## 2c. Mass (binding/inertia) is NOT the same as k₁₁ (commitment-rate/time-dilation) — a clean separation
The corpus flagged a cross-connection (`Mass_GR_SparseCommitment_CrossConnection`): the "mass-memory fade rate" and the GR sparse-commitment parameter share the factor `k₁₁` — suggesting mass might unify with gravity under one number. Tested it directly with the inertia discriminator: a lone front carrying **commitment-memory** (the dwell mechanism = the `k₁₁`/commitment-rate mass candidate), pushed by a force.

| `k_mem` | path_speed | `v_x` | `v_x / path` |
|---|---|---|---|
| 0.00 | 1.00 | 1.00 | 1.00 |
| 0.40 | 0.55 | 0.55 | **1.00** |
| 0.80 | 0.38 | 0.38 | **1.00** |

**`v_x / path_speed = 1.00` at every memory level.** The memory front dwells (path speed drops), but its forward drift *tracks the path speed exactly* — every advance it makes still aligns fully to the force. There is **no directional inertia**: commitment-memory makes a **slow clock** (dwells → advances less → slower overall), which is **time dilation**, not mass. Contrast the bound composite (§2b): `v_x(COM) = 0.72` while each constituent's path_speed `= 1` — the composite **resists** (`v_x << constituent speed`) = **directional inertia = mass**.

> **So `k₁₁` and mass are DIFFERENT phenomena.** `k₁₁` (the commitment/sparse-commitment rate) governs the **clock rate = time dilation** — which is exactly why it also appears in the GR sparse-commitment / gravitational-time-dilation parameter (the cross-connection is real, but it is about *time dilation*, not mass). **Mass (inertia) is a separate thing — it comes from BINDING (V5), not from the commitment rate.** The two do not unify under `k₁₁`. This *sharpens* the corpus: relabel the "mass-memory fade rate" as the **clock/time-dilation rate** (`k₁₁`), and keep **mass = binding** (V5) as the distinct object.

## 3. Verdict
**YES — V5-binding gives ED a native mass mechanism, and it survives the ballistic-or-extinct wall.** The wall is about *individual* fronts (no sub-ballistic single-front mode); the *composite* is a different object, and a V5-bound cluster of ballistic fronts is confined (measured) and moves sub-luminally (measured), with its COM heading to rest as N grows (extrapolated). This is exactly the physical origin of most real mass — **binding, "mass without mass"** (the bulk of hadron mass is binding, not the Higgs coupling). ED reproduces the *dominant* form of mass ED-natively, where before it had "no native rest mass at all."

## 4. Honest tiers and caveats (load-bearing)
- **MEASURED (solid):** the confinement (rms 55 → 1.5, robust) and the sub-luminal composite (`v_COM ≈ 0.5 < c`, robust across `A_V5`, `ell_V5`). Real certified `compute_sigma` + V5's known structure.
- **EXTRAPOLATED (not proven-zero):** the clean at-rest limit. `v_COM` trends 0.54 → 0.31 over N=8 → 32 (a finite-N fluctuation shrinking toward rest); it is not a single measured zero. Honest: the trend is clear and monotone, the strict `v_COM → 0` is an extrapolation.
- **V5 is a structural ADDITION, not primitive-forced.** Faithful to Paper_090's finite-reach retarded form, but the bare certified substrate has no V5 (same standing caveat as all V5 work). So this shows *V5's known structure yields binding-mass*, not that the bare 13 primitives force it. The open forward question (target A2): do the primitives *force* V5.
- **The orientation-persistence tie-break** is faithful to the certified `(ρ,orientation)` front (Σ-blind, so orientation only breaks ties) but is a modeling choice; flagged.
- **This is BINDING mass (composites) only.** The *fundamental* Higgs/EWSB mass (electron, current-quark, W/Z from spontaneous symmetry breaking) is NOT addressed here — and the condensate route (`E1_MassFromStructure_Results`) already showed that's not natively realized on the certified field. So the honest split: **binding mass native (via V5); fundamental Higgs mass separate, open/inherited.**

## 5. Net for the mass sector (#2)
Before: "the certified substrate has no native rest-mass mechanism" (ballistic-or-extinct; condensate route fails). After: **ED has a native BINDING-mass mechanism** — V5-bound ballistic fronts form a confined, sub-luminal, at-rest-in-the-large-N-limit composite = rest mass from binding, the physically dominant form of mass, surviving the wall. What stays open/inherited: the *fundamental* Higgs/EWSB mass, and the forward derivation that the primitives *force* V5. So #2 moves from "unbuilt/no-mechanism" to **"binding mass mechanism demonstrated (V5-conditional); fundamental Higgs mass open/inherited."** Crank-rail: reported the confinement + sub-luminal composite as measured, the at-rest limit as an N-extrapolation, and kept the V5-not-primitive-forced + binding-vs-fundamental caveats front and center; did not claim the bare primitives force mass, and did not conflate binding mass with the Higgs mechanism.
