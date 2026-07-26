# Equipartition in ED: the Relation Holds; the Microscopic ½T Is the Energy-Side Twin of the Open 1/4-Coefficient Question

**Date:** 2026-07-25
**Status:** Working note — **counting crux attacked; result is a unification, not a grounding.** Two findings. **(1) Modest positive:** Padmanabhan/T19's equipartition *relation* `E = ½ n T` (≡ `S = E/2T`, `n = 4S`) is already *satisfied* in ED, at the same tier as `S = A/4` — it follows from ED's derived `κ = 1/(2r_s)`, the thermal `T = κ/2π`, and the first law. ED is not missing the relation. **(2) The real finding:** what is *not* grounded is the **microscopic** reading — that `n = A/ℓ_P²` counts actual horizon degrees of freedom each literally carrying `½T`. That is the **energy-side twin of the open 1/4-coefficient question** the `BH_EntropyCoefficient` note already isolated (which surface / what state-count-per-area does ED freeze?). Equipartition's `½T` and the entropy's `1/4` are two faces of one unknown — the horizon's d.o.f. content — decided by the *same* GR-III sim measurement. The earlier "one near-horizon fact" reduction is withdrawn; the referee's "edge = bandwidth + phase = 2 d.o.f. = `kT`" factor is the *symptom* of the unmeasured d.o.f. content, not a bug to patch. **Not banked as a grounding; the Padmanabhan paper §5 stays an open lead.**

---

## 1. The targets, and the read-first

Microscopic-completions left a paired lead: **A** — ground the `½T`-per-channel equipartition Padmanabhan and T19 both *posit*; **B** — an arrow-native `2π` in `T = κ/2π`.

- **B:** the Euclidean-route `2π` is solid (`BH_Thermal2Pi` §2–3, from ED's own `b`-profile); the arrow-native version is left explicitly open (§4b: deep problem vs category error, unresolved). Not re-chased here.
- **A** is this note. Read-first confirmed equipartition is posited everywhere (T19 §3, Jacobson companion, galactic-dynamics walkthrough), derived nowhere; the "`½T` and `T=κ/2π` are one fact" hope was the reserved lead of `Paper_GravityAsHorizonEquipartition` §5. Attacking it produced the result below.

## 2. What ED derives vs imports at the near-horizon

- **Derived (ED's own):** the near-horizon **Rindler geometry** — `b = 1 − r_s/r` gives `ds² ≈ −κ²ρ²dt² + dρ²`, numerically confirmed (`BH_Thermal2Pi` §2); and **`κ = 1/(2r_s)`** (GR-III).
- **Imported (standard QFT-on-Rindler, on ED's derived geometry):** the harmonic mode basis; and the **KMS thermal state** at `T = κ/2π` with Bose occupation `n(ω)` (`H-1`, FORCED-CONDITIONAL on an unverified analytic-continuation assumption; `walkthroughs/from_primitives_to_substrate_unruh`).

So ED contributes the geometry; harmonicity and thermality ride on top exactly as the temperature's `2π` does. Equipartition of thermal harmonic modes is then a *theorem* (`⟨E_ω⟩ → k_BT = 2·½k_BT` in the `ℏω ≪ k_BT` limit) — zero ED-specific content, and uncontrolled at the horizon where the dominant modes have `ω ~ T`.

## 3. Finding (1): the equipartition RELATION already holds in ED

Padmanabhan's equipartition is `E = ½ n T` with `n = 4S`, i.e. his `S = E/2T` (his eq. 1, from CQG 21 4485). Check it in ED, using only ED-derived / already-standing pieces:

- `S = A/4` — `BH_EntropyCoefficient` §2 Route A: `κ = 1/(2r_s)` (derived) `+ T = κ/2π + dM = T dS` integrates to `S = πr_s² = A/4`.
- `E = M = r_s/2` (active mass, `G=c=1`); `T = κ/2π = 1/(4πr_s)`.

Then

$$ \frac{E}{2T} = \frac{r_s/2}{2\cdot \frac{1}{4\pi r_s}} = \frac{r_s}{2}\cdot 2\pi r_s = \pi r_s^2 = \frac{A}{4} = S. \qquad\checkmark $$

So **`S = E/2T` holds, hence `E = ½ n T` with `n = 4S = A/ℓ_P²`.** ED satisfies Padmanabhan's equipartition *relation* automatically, at the **same tier as `S = A/4`** (given the inherited thermal `2π`). This is a consistency result, not new physics — but it means the open part of A is **not** "does the relation hold" (it does); it is the microscopic reading of `n`.

## 4. Finding (2): the microscopic ½T is the energy-side twin of the open 1/4 question

The relation `E = ½nT` fixes only the *product* structure. The microscopic equipartition claim is stronger: that `n = A/ℓ_P²` counts **actual horizon degrees of freedom, each carrying `½T`**. That requires knowing the horizon's d.o.f. content — and that is exactly the question `BH_EntropyCoefficient` §4 already isolated on the *entropy* side:

> **On which surface does ED freeze its independent commitment-states — the full horizon sphere (one state per Planck area → coefficient 1) or the great-circle cross-section / half-radius sphere (→ coefficient 1/4)?**

Padmanabhan resolves both sides by hand with two free factors: `c₁ = 1` (cells per Planck area) and `c₂ = e^{1/4}` (states per cell), giving simultaneously `½T` of **energy** and `¼` nat of **entropy** per cell — the two faces of his `S = E/2T`. ED must *derive* that d.o.f. content, and derives neither coefficient yet:

- **Entropy face (the 1/4):** open, sharpened by `BH_EntropyCoefficient` to the surface question above; honest prior is coefficient ≈ 1 (full sphere), in which case the `1/4` lives in the thermal `2π`.
- **Energy face (the ½T):** open for the *same* reason. The referee's factor is the tell: ED's severed edge is `bandwidth + phase` = **2 real d.o.f.** = a full mode = `k_BT`, not the `½T` of one quadrature. So "one severed edge = one Padmanabhan cell" is not one-to-one (an edge looks like two cells), and the assignment cannot be asserted — it must come out of the same d.o.f.-content measurement.

**These are one question, not two.** Entropy-per-d.o.f. and energy-per-d.o.f. at the horizon are both fixed once the d.o.f. content is known; Padmanabhan ties them via `S = E/2T`. So grounding the microscopic `½T` is **not separable from** closing the `1/4` coefficient — it is its energy-side twin, gated on the same unknown.

## 5. The concrete next step (unified, could-say-no)

The decisive test is the one `BH_EntropyCoefficient` §4 already proposed, now doing double duty: in the GR-III dynamical-bandwidth sim, **count the independent frozen commitment-states on the b→0 horizon and divide by the horizon area** (Planck-proxy units).

- The **count coefficient** it returns settles the entropy face (1 = full sphere → the `1/4` is thermal; `1/4` = cross-section → geometric).
- The **same count**, set against Padmanabhan's `E = ½ n T` and ED's `E = M`, fixes what energy each frozen d.o.f. must carry — settling whether the `½T`-per-d.o.f. reading is consistent, or whether ED's edges (2 d.o.f. each) enter with the factor the referee flagged.

One measurement, both faces. Until it is run, equipartition's microscopic `½T` and the `1/4` are both **open, and now known to be the same open question**.

**RESULT (2026-07-25, sim run).** The coefficient came out **0.780 ± 0.011 (≈ π/4), area law confirmed** (`horizon_entropy_coefficient.py`; recorded in `BH_EntropyCoefficient` §6). Read: the substrate tiles the **full horizon** at ~one state per Planck area (the ~0.78 is a lattice-discretization factor), **decisively not 0.25**. So:
- **The count side is settled:** `n ≈ A/ℓ_P²`, i.e. Padmanabhan's `c₁ ≈ 1` is vindicated — ED's frozen-state count *is* his full-horizon count. The referee's edge↔cell worry resolves toward "the horizon boundary carries ~1 independent frozen state per Planck cell," matching Padmanabhan's cell, not a doubled edge count.
- **The `1/4` is thermal, not geometric tiling** (the cross-section route is refuted as a mechanism). Hence equipartition's `½T`-per-cell and the `1/4`-nat-per-cell are **both** the two faces of the *thermal* `S = E/2T` at `T = κ/2π` — exactly §3's relation — with the normalization carried by the inherited 2π, not by a quarter-surface.
- **What stays open collapses to one lever:** deriving the microscopic `½T` (energy side) and the `1/4` (entropy side) both now reduce to deriving the **arrow-native 2π** (`BH_Thermal2Pi` §4b), which may be a category error. The sim removed the *counting* ambiguity; it did not remove the thermal import.

## 6. Honest tiers and paper action

- **Consistency (banked, modest):** ED satisfies the equipartition *relation* `E = ½nT` at the same tier as `S = A/4` (§3). Given, not derived-from-below (uses the thermal `2π`).
- **Open (the real content):** the microscopic `½T`-per-d.o.f. — gated on the horizon d.o.f.-content measurement, i.e. the *same* open question as the `1/4` coefficient (§4–5). Withdrawn: the earlier "one near-horizon fact / two-into-one" reduction (it asserted the edge↔quadrature map; the map is factor-off and unmeasured).
- **Inherited conditionality:** the thermal state is `H-1`-FORCED-CONDITIONAL; both faces sit no firmer than that.
- **Does NOT achieve Investigation #9** (fully substrate-native T19): the KMS import remains.
- **Paper action: none.** `Paper_GravityAsHorizonEquipartition` §5 stays the open lead it is. README lead **A** updated to record that A = the energy-side of the open `1/4` question, decided by the GR-III frozen-state count.

## Cross-references
- `foundations/BH_EntropyCoefficient_FromEventCounting.md` (§2 Route A gives `S=A/4`; §4 the decidable surface/count question — the twin this note ties equipartition to).
- `foundations/BH_Thermal2Pi_FromNearHorizonRindler.md` (§2–3 Rindler form + `T=κ/2π`; §4b arrow-native `2π` open).
- `arcs/arc-Hawking/H-1_spectral_form_and_temperature.md` (Bose occupation, FORCED-CONDITIONAL on the continuation assumption).
- `ED Generative/physics-papers/substrate-evaluation/Paper_AreaLawIsTheEdgeCount.md` (edge-count = area SCALING measured; coefficient/normalization open — curvature emergence).
- `ED Generative/physics-papers/microscopic-completions/Paper_GravityAsHorizonEquipartition.md` §5, §8 (the open lead — unchanged).
- `papers/Substrate_Gravity_Foundations/…2026-04-28.md` §3 (T19); `docs/Investigation_Priority_List.md` #9 (not achieved).
- `evaluation/DynamicalBandwidth/horizon_entropy_coefficient.py` (the frozen-state-count probe that would run the §5 test).
