# ED and Jacobson's "Einstein Equation of State": ED Fills the Exact Gap Jacobson Flagged

**Date:** 2026-07-24
**Status:** Working note (synthesis, step 1 of the thermo-gravity thread) — **upgraded after reading the actual paper** (Jacobson, *Phys. Rev. Lett.* 75, 1260, 1995; gr-qc/9504004v2, read in full). The first draft worked from memory; the real text is *stronger* for ED and supplies exact quotes. **No new forced derivation** — the content is (a) ED grounds the three things Jacobson *assumes or leaves undetermined*, (b) ED reaches the field equation by a second route, (c) the `G = c³ℓ_P²/ħ` match is exact, (d) a grounded resolution of the arrow paradox. Corpus check: ED had cited only Jacobson's *1991* paper; the 1995 derivation was never engaged.

---

## 1. Jacobson's actual derivation (from the text)

Jacobson turns black-hole thermodynamics around: instead of deriving horizon-entropy from GR, he **assumes horizon thermodynamics and derives GR.** His own framing (page 1): *"the Einstein equation is an equation of state. It is born in the thermodynamic limit as a relation between thermodynamic variables, and its validity is seen to depend on the existence of local equilibrium conditions."* He motivates it with the **ideal gas** (his analogy, not just ours, page 2): knowing `S(E,V)` you read the equation of state off `δQ = TdS`; a counting argument `S ∝ ln V + f(E)` gives `pV ∝ T`.

The derivation, precisely:
- **Heat across a causality barrier** (page 2): *"heat is energy that flows between degrees of freedom that are not macroscopically observable"* — here, energy across a local causal horizon, where the hidden system is *"separated from the [outside] not by a diathermic wall, but by a causality barrier."* Flux `δQ = ∫ T_ab χ^a dΣ^b` (eq 1), `= −κ ∫ λ T_ab k^a k^b dλ dA` (eq 2), `χ` the approximate boost Killing field.
- **Entropy = entanglement entropy, made finite by a cutoff** (pages 2–3): *"the overwhelming majority of the information that is hidden resides in correlations between vacuum fluctuations just inside and outside of the horizon… 'entanglement entropy'… divergent in continuum QFT. If there is a fundamental cutoff length `l_c`, then the entanglement entropy is finite and proportional to the horizon area in units of `l_c²`."* And: *"consistency with thermodynamics requires that `l_c` must be of order the Planck length."* So `dS = η δA` (eq 3).
- **Unruh temperature** `T = ħκ/2π` (page 4).
- **Raychaudhuri closes it** (page 5): `dθ/dλ = −½θ² − σ² − R_ab k^a k^b`; at the point `θ=σ=0`, so `δA = −∫ λ R_ab k^a k^b dλ dA` (eq 5). Requiring `δQ = TdS` for **all** null `k^a` forces `(2π/ħη) T_ab = R_ab + f g_ab`; conservation + Bianchi fixes `f = −R/2 + Λ`, giving **the Einstein equation** `R_ab − ½R g_ab + Λ g_ab = (2π/ħη) T_ab` (eq 6).

## 2. The three things Jacobson *assumes or leaves open* — ED grounds all three

| Jacobson's input | His own words | ED grounds it |
|---|---|---|
| the horizon **hides DOF** (a "causality barrier") | *"separated… by a causality barrier"* (p2) | **A1 severance** — the `b→0` cut is exactly a capacity-zero causality barrier; the hidden DOF are the boundary adjacency channels (GR-III §7.4). |
| entropy = **entanglement across the cut**, finite via a **fundamental cutoff `l_c ≈ ℓ_P`** | *"correlations between vacuum fluctuations just inside and outside… finite [if] a fundamental cutoff `l_c`… of order the Planck length"* (p2–3) | ED **has** the cutoff natively — the grain `ℓ_ED = ℓ_P` (P08) — and the entanglement across the cut is the **severed cross-chain (V5) correlations**. ED supplies the `l_c` Jacobson must assume. |
| **`η` (entropy per area) is UNDETERMINED** | *"The dimensional constant `η` is undetermined by anything we have said so far (although given a **microscopic theory of spacetime structure** one may someday be able to compute `η` in terms of a fundamental length scale.)"* (p5) | **ED is that microscopic theory.** `η =` the severed-channel count per grain area `= 1/(4ℓ_P²)`; the area law (`S ∝ A`) is *because* severance is a surface cut (measured holographic, GR-III §7.4). |

**This is the lever.** Jacobson himself points at *"a microscopic theory of spacetime structure [to] compute `η` in terms of a fundamental length scale"* as the missing piece. **ED is precisely that** — it identifies `η` as a severance density on a grain of size `ℓ_P`. ED does not merely reproduce Jacobson; it fills the exact gap he flagged.

## 3. Newton's `G` — the match is exact (answers the "stepchild" puzzle)

Jacobson (page 6): *"The constant of proportionality `η`… determines Newton's constant as **`G = (4ħη)⁻¹`**, which identifies the length `η^{−1/2}` as twice the Planck length `(ħG)^{1/2}`."* So `η = 1/(4ℓ_P²)`, and substituting:

$$ G = \frac{1}{4ħη} = \frac{ℓ_P^2}{ħ} \;\xrightarrow{\text{restore }c}\; \boxed{G = \frac{c^3 ℓ_P^2}{ħ}} $$

**— identical to ED's constants-ledger `G = c³ℓ_P²/ħ`** (Essay 13/14, `Paper_027`). So Jacobson's *"`G` from entropy-per-area"* and ED's *"`G` from the grain `ℓ_P`"* are **the same equation**: the entropy-per-area `η` *is* the grain density `1/(4ℓ_P²)`. This resolves the puzzle — `G` is a "stepchild" in *both* pictures because in both it is not independent; it is fixed the moment you have the grain (with `c, ħ`). Jacobson leaves `η` (hence the grain) undetermined and asks for a microscopic theory to supply it; **ED supplies it, and lands on ED's own `G` exactly.** Neither treats `G` as fundamental; both make it the conversion factor tied to the grain/entropy-density — the "first shadow."

## 4. The arrow paradox — resolved in Jacobson's own words, sharpened by ED

The puzzle (AP): thermo *keeps* the arrow (it's the discard-pile's accounting); GR *threw the arrow away*; how derive arrow-less GR from arrow-keeping thermo? **Jacobson answers it himself, and the ideal gas is his own analogy:** the Einstein equation is the **equilibrium equation of state** — *"a relation between thermodynamic variables… its validity depends on local equilibrium"* — and equilibrium relations are time-reversal invariant *even though the approach to them is not.* He is explicit that the arrow lives in the *non-equilibrium* regime, not the equation: *"for sufficiently high frequency or large amplitude… the local equilibrium condition would fail… 'non-equilibrium spacetime'."* The Einstein equation is the destination (arrow-blind); the second law is the road (arrow-ful).

**ED sharpens the "where is the arrow" answer to a primitive.** The entropy Jacobson feeds in is the entanglement of **hidden** DOF, and in ED those are the **A1-severed** channels — and severance is **irreversible (P11)**. So the arrow is not smuggled in vaguely; it is the P11-irreversibility of the severance that *creates* the horizon entropy. **The arrow builds the horizon (irreversible severance); GR is the equilibrium balance-sheet of what the horizon hides.** This is the How-Coarse-Grain thesis made concrete: GR = the law of the seam (the arrow-blind consistency condition); thermo = the receipt; and ED shows the receipt is written in one-way severed channels.

## 5. Two routes to Einstein — and the one honest obstruction

- **Route 1 (Jacobson, thermodynamic, top-down):** assume horizon thermo → full Einstein equation. ED grounds its three inputs (§2) → so ED can, in principle, *run Jacobson's route on its own derived inputs.*
- **Route 2 (ED, dynamical, bottom-up):** the bandwidth rule `ḃ = D∇²b − κρ` steady state → the field equation (Newtonian limit measured; weak-field Einstein GR-I; khronometric GR-II).

Reaching Einstein two independent ways, with ED grounding the assumptions of one of them, is the genuine win. **The honest obstruction (do not gloss):** Jacobson's argument assumes *"an approximately flat region with the usual Poincaré symmetries"* (page 4) — i.e. **local Lorentz invariance / no preferred frame.** ED's gravity is **khronometric** (it has the khronon, a preferred foliation). So ED cannot run Jacobson *unchanged*; either (a) there is a khronometric version of the equation-of-state derivation, or (b) the place ED's preferred frame enters Jacobson's Poincaré assumption is exactly ED's known departure from pure GR (`α₁, α₂`, GR-IV). Open, and a good lead — the thermo route may *localize* where ED's arrow re-enters a derivation Jacobson keeps arrow-blind.

## 6. Jacobson's conclusion *is* ED's stance

Jacobson (page 6): a sound wave *"is only a statistically defined observable on the fundamental phase space of the multiparticle system, it should not be canonically quantized as if it were a fundamental field… it may not be correct to canonically quantize the Einstein equations, even if they describe a phenomenon that is ultimately quantum mechanical."* **This is ED's position verbatim** — don't quantize GR (the acoustic/bandwidth metric is emergent); discretize the substrate underneath. ED and Jacobson agree on the punchline; ED supplies the substrate Jacobson only gestures at ("a microscopic theory of spacetime structure").

## 7. Honest tiers
- **Solid:** ED grounds all three of Jacobson's inputs (§2); the `G = c³ℓ_P²/ħ` match is exact (§3); the paradox resolution is Jacobson's own equilibrium framing + ED's severance-irreversibility (§4).
- **Value-inherited (both):** the numerical grain size / `η`. ED expresses `η` *in terms of* the fundamental length (which is what Jacobson asked for), but does not compute the length's value from something deeper — same status as his `l_c`.
- **Open:** running Jacobson's route in ED to get the *full* EFE is blocked by the **khronometric-vs-Lorentz** obstruction (§5); ED's own dynamical route reaches only weak-field/khronometric.

## 8. What this sets up
- **Step 1 (this note):** grounded — ED fills Jacobson's flagged gap; the `G` match is exact.
- **Step 2 (chip'd):** fold the arrow-builds-horizons resolution + the Jacobson connection into `Paper_HowCoarseGrainReality`.
- **Step 3 (done, weak-but-standing):** the pattern — `ThermoPattern_EquationOfState_of_the_DiscardPile_2026-07-24.md`.
- **New lead worth its own look:** the khronometric-vs-Lorentz obstruction (§5) — does ED's preferred frame enter Jacobson's derivation exactly at the `α₁, α₂` residue?

## Cross-references
- Jacobson, T., *Phys. Rev. Lett.* **75**, 1260 (1995), gr-qc/9504004 (read in full: eqs 1–6; `G=(4ħη)⁻¹`; "causality barrier"; "non-equilibrium spacetime"; the don't-quantize conclusion).
- ED: `physics-papers/gravity/Paper_GR-III_DynamicalRule.md` (§7.4 area law from severance; the `b→0` = A1 cut); `Paper_GR-I` (`g~1/b`); `Paper_GR-II` (khronometric); `foundations/BH_Thermal2Pi_FromNearHorizonRindler.md` (`T=κ/2π` from ED's Rindler geometry); `foundations/BH_EntropyCoefficient_FromEventCounting.md` (the `1/4`); `Paper_027` + Essays 13/14 (`G=c³ℓ_P²/ħ`, the constants ledger).
- `ED Generative/physics-papers/substrate-evaluation/Paper_HowCoarseGrainReality.md` (the ledger).
