# ED and Jacobson's "Einstein Equation of State": ED Grounds the Inputs Jacobson Assumes

**Date:** 2026-07-24
**Status:** Working note (synthesis, step 1 of the thermo-gravity thread). Assembles existing ED results (GR-I/II/III, the horizon-thermo foundations notes, A1 severance) against Jacobson's 1995 derivation of the Einstein equation from thermodynamics. **No new forced derivation** — the content is (a) ED grounds all three of Jacobson's *assumed* inputs, (b) ED reaches the field equation by a second independent route, and (c) a sharpened resolution of the "arrow-less GR from arrow-keeping thermo" paradox. Corpus check: ED currently cites only Jacobson's *1991* trans-Planckian paper; the *1995* thermodynamics-of-spacetime derivation is **not** engaged anywhere — this note fills that gap.

---

## 1. What Jacobson 1995 does

Jacobson ("Thermodynamics of Spacetime: The Einstein Equation of State," PRL 75, 1260) applies the Clausius relation `δQ = T dS` to a **local Rindler horizon at every point and direction** in spacetime, feeding in three inputs:

1. **Area-law entropy** `S = η A` (Bekenstein–Hawking),
2. **Unruh temperature** `T ∝ acceleration` (the thermal bath an accelerated observer sees),
3. **Heat = energy flux** `δQ = ∫ T_μν χ^μ dΣ^ν` (stress-energy across the horizon).

Demanding `δQ = T dS` hold for *all* local horizons forces the **Einstein field equation** `G_μν = 8πG T_μν`, with `G` fixed by the entropy density η. Conclusion: **gravity is an equation of state** — an equilibrium thermodynamic relation of unknown microscopic DOF, not a fundamental field. All three inputs are *postulated*; the microstates are hypothetical.

## 2. ED grounds all three inputs — from the substrate

Where Jacobson assumes, ED derives (from the one bandwidth rule + severance):

| Jacobson's input | His status | ED's status |
|---|---|---|
| **`S ∝ A`** (area law) | assumed (BH) | **Derived (form, measured):** the frozen `b→0` horizon's entropy is the count of **A1-severed** boundary adjacency channels, and it scales as the **perimeter** (`r_h^0.96`), not the bulk (`r_h^2.01`) — GR-III §7.4, `Paper_043`. Holographic, from severance. |
| **`T` = Unruh** (`T ∝ a`) | assumed (Unruh effect) | **Derived:** ED's own vacuum profile `b = 1 − r_s/r` has **Rindler form** at the horizon (`ds² ≈ −κ²ρ²dt² + dρ²`, confirmed numerically), and smoothness/no-conical-defect forces `T = κ/2π` — `BH_Thermal2Pi_FromNearHorizonRindler.md`. |
| **`δQ = T dS`** (Clausius) | assumed (equilibrium thermo) | Holds on ED's derived horizon: the first law `dM = T dS` with `κ = ½ b′(r_s) = 1/(2r_s)` (derived) integrates to `S = A/4` — `BH_EntropyCoefficient_FromEventCounting.md` §2. |
| **OUTPUT: Einstein eqn** | derived (from the three) | **Derived independently:** GR-III's dynamical bandwidth rule `ḃ = D∇²b − κρ` has the field equation as its steady state (Newtonian limit measured; weak-field Einstein GR-I; khronometric class GR-II). |

So **ED and Jacobson are two routes to the same place that meet:** Jacobson's is *top-down thermodynamic* (assume horizon thermo → get Einstein); ED's is *bottom-up dynamical* (substrate bandwidth rule → get Einstein *and* the horizon thermo as emergent). **ED supplies the substrate `why` for every postulate Jacobson has to assume.** The microstates Jacobson calls hypothetical, ED names: the severed adjacency channels across the `b→0` cut.

## 3. The paradox resolved — and sharpened by ED

**The puzzle (AP):** in the coarse-graining ledger (`Paper_HowCoarseGrainReality`), thermodynamics is the *one* continuum theory that **keeps** the arrow (it is the accounting of the discard pile). GR is a theory that **threw the arrow away**. So how does Jacobson derive arrow-less GR *from* arrow-keeping thermo?

**The resolution — the gas law makes it click:** `PV = nRT` is time-symmetric (shows no arrow), yet it is the equilibrium equation of state of a gas whose *approach* to equilibrium was violently irreversible. The arrow lives in the *second law* (the approach), not in the *equation of state* (the destination). Gravity is the same: **GR is the arrow-blind equilibrium equation of state; the arrow is upstream, hidden inside the assumption `S ∝ A`.**

**ED sharpens this from "hidden" to explicit.** In ED, the horizon entropy Jacobson feeds in **is the count of A1-severed channels** — and severance is **irreversible** (A1 capacity-zero is a one-way cut; P11). So:

> The arrow is not *in* GR. The arrow is what **builds the horizons** — via irreversible severance — whose entropy is the very input Jacobson assumes. GR is the equilibrium balance-sheet of those arrow-built horizons; a balance-sheet at equilibrium is arrow-blind even though the arrow filled it in.

This is exactly the How-Coarse-Grain thesis (GR = the coarse-grained consistency condition / "law of the seam"; thermo = the receipt) — now realized concretely: **Jacobson shows GR *is* the receipt, balanced at every horizon, and ED shows the receipt is written in irreversibly-severed channels.**

**An echo one level down (worth flagging).** Even ED's *temperature* factor exhibits the same pattern: the thermal `2π` is obtained via the **Euclidean continuation** (a reversible-time device), and `BH_Thermal2Pi` §4 flags honestly that a *continuation-free* derivation from raw commitment statistics is open — the `2π` "may be a continuum feature that lives at the smooth-horizon level, not below." So the thermal structure looks arrow-blind (reversible-time trick) even though it is built from irreversible commitments — the arrow-builds-it-but-the-relation-is-blind pattern, recurring at the temperature itself.

## 4. A genuine potential payoff (flagged, not claimed)

Jacobson's route reaches the **full** Einstein equation; ED's dynamical-rule route currently reaches only **weak-field + khronometric** (GR-I/II/III; the full nonlinear EFE is open, GR-III preamble 2). So **if ED's grounding of Jacobson's inputs holds, ED may inherit a *route to the full field equation* it does not otherwise have** — run Jacobson's argument on ED's *derived* (not assumed) area law + Unruh temperature.

**But the honest obstruction is real and interesting:** Jacobson's local-Rindler-horizon argument assumes **Lorentz invariance / no preferred frame**. ED's gravity is **khronometric** — it *has* a preferred foliation (the khronon). So ED cannot simply run Jacobson unchanged; either (a) there is a *khronometric* modification of the equation-of-state derivation, or (b) the place where ED's preferred frame enters Jacobson's argument is exactly ED's known departure from pure GR (the `α₁, α₂` residue, GR-IV). This is an **open question and a good one** — the thermo-gravity route may pinpoint *where* ED's arrow re-enters a derivation that standard Jacobson keeps arrow-blind. Do not claim ED "gets the full EFE via Jacobson" until this is worked.

## 5. Honest tiers

- **Derived / measured (solid):** `S ∝ A` form (severance count ~ perimeter, measured); `T = κ/2π` (Rindler near-horizon geometry, derived); `κ = 1/(2r_s)`; weak-field Einstein + khronometric class + Newtonian fixed point.
- **Synthesis (this note):** ED grounds Jacobson's three postulates; two routes meet; the arrow-in-`S∝A` resolution of the paradox. New as an *arrangement* of existing results, not a new derivation.
- **Open:** the `1/4` coefficient's cleanest derivation (one decidable sim, `BH_EntropyCoefficient` §4); the continuation-free `2π`; the full nonlinear EFE; **and specifically the khronometric-vs-Lorentz obstruction to running Jacobson's route in ED (§4).**

## 6. What this sets up (the thread)

- **Step 1 (this note):** ED ↔ Jacobson — grounded. Done.
- **Step 2:** promote the paradox resolution ("the arrow builds the horizons; GR is their equation of state") to a stated ED result that sharpens `Paper_HowCoarseGrainReality`.
- **Step 3 (the prize, speculative):** the **pattern** — is each theory recoverable as "the equilibrium equation of state of its own discard pile"? Jacobson did GR; Verlinde did Newton. ED is uniquely equipped because it makes the discard pile *explicit* (committed events, thrown-away correlations). Pick one more ledger theory and honestly test whether the recipe recovers it. Flag as speculation; let it be a real could-say-no.

## Cross-references
- Jacobson, T., *Phys. Rev. Lett.* **75**, 1260 (1995) — "Thermodynamics of Spacetime: The Einstein Equation of State."
- ED: `physics-papers/gravity/Paper_GR-III_DynamicalRule.md` (§7.4 area law; §8 Hawking; the `b→0` horizon = A1 cut); `Paper_GR-I` (`g~1/b`, `N²~b`); `Paper_GR-II` (khronometric class); `foundations/BH_Thermal2Pi_FromNearHorizonRindler.md` (`T=κ/2π` from Rindler geometry); `foundations/BH_EntropyCoefficient_FromEventCounting.md` (the `1/4`, first law); A1 (`evaluation/Bits/…` channel-capacity zero = severance).
- `ED Generative/physics-papers/substrate-evaluation/Paper_HowCoarseGrainReality.md` (the ledger; GR as law-of-the-seam; thermo as the receipt).
