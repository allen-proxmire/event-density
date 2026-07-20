# The Cluster/CMB Debt Map

**What this is.** A map of one owed problem, not a to-do list. It states what the CMB acoustic peaks and galaxy clusters *require* of Event Density, where MOND-class theories characteristically fail, what ED's candidate answers are, and what is proven versus open. Public port and update of the `event-density` Khronon–MOND Round-5 cosmology mapping, extended with the 2026-07 dark-sector findings. Nothing here is discharged; the debt is *mapped and shown addressable*, not paid.

## 1. Why there is a debt at all

MOND (ED's khronon, KM-I) fits galaxies without a dark-matter particle. It does **not** fit two things, and this is a *known* feature of every MOND-class theory, flagged in KM-I §8:

- **Clusters:** MOND under-predicts cluster masses by a factor of ~2 — the "cluster-scale missing-mass shortfall."
- **The CMB acoustic peaks:** the pattern of peak heights requires a component that gravitates but does **not** oscillate with the baryon–photon fluid (a decoupled, pre-formed potential well), diluting as `a⁻³` so it has ~5× the baryon abundance at recombination. A boost to baryon gravity (which is what MOND is) cannot supply this — it deepens the sloshing, it does not hold a well still. This is *why* MOND-class theories die at the CMB.

## 2. What the data require of ED's sector

| Epoch / probe | Requirement |
|---|---|
| **BBN** | any `H²`-tracking contribution stays inside the `G_cosmo/G_N` bound |
| **CMB acoustic peaks** | a component of the right abundance (~5× baryons) that clusters like pressureless dust (`w ≈ 0`, `c_s ≈ 0`) at recombination — decoupled from the photon fluid |
| **Clusters** | the same component supplying the missing cluster mass MOND alone cannot cover |
| **Galaxies** | the component must **not** dominate galactic dynamics (MOND already fits those) → it must be diffuse at galactic scale |
| **Late times** | the Λ-order constant (automatic in the khronon cosmological sector) |
| **Čerenkov / stability** | perturbations ghost/gradient-stable on FRW; propagation within bounds |

The hard rows are the CMB and clusters, and the galactic row is the constraint that keeps a solution honest (no double-counting with MOND).

## 3. ED's candidate answers, and their status

Two candidate routes have been examined. **Route A (the khronon dial) is a modified-gravity route; Route B (a committed neutral relic) is a component route.** They are not mutually exclusive.

**Route A — the khronon cosmological dial `𝒲(A²,Θ)`.** The khronon's cosmological sector is a dark fluid whose near-zero-sound-speed perturbation mode clusters like dust (Round-5 §4; the "soft spot is the doorway"). *Status:* the dust *clustering* condition (`c_s ≈ 0`) is available, but a 2026-07 no-go shows a **local function of the expansion rate cannot supply the dust *abundance*** (`a⁻³` requires volume memory a function of `H` lacks). Three native routes to put the abundance in the khronon itself were checked and failed (the aether gives `∝H²` not `a⁻³`; the arrow primitives P11/P13 do not force the mimetic unit-gradient constraint; the emergent-metric conformal mode is a slaved bandwidth field, not a free dust field). Getting the abundance from the khronon requires an *added* mimetic constraint — an addition, not native. **Route A supplies clustering, not abundance, natively.**

**Route B — a committed neutral relic (the current best native candidate).** At the inflation/saturation exit, ED's baryogenesis admission mechanism (Paper_ED_Baryogenesis, M3) commits matter; commitment to a **neutral channel** gives a decoupled relic (baryons are the charged-channel sibling). It is decoupled (neutral, no EM winding), cold-capable (binding mass, measured), `a⁻³`, and survives reheating (committed, P11). *Status:* form-complete and native; the **relic mass — hence free-streaming length — is value-inherited** and natural-scale arguments lean cold (the galaxy-unfriendly end). See `Paper_ED_DarkSector_Position.md` §6.

## 4. The reconciliation that avoids double-counting

MOND (galaxies) and the component (clusters + CMB) do not double-count because they dominate different scales, separated by the component's **free-streaming length**:

- Galaxies (~kpc): component too diffuse to fall in → MOND unaffected.
- Clusters (~Mpc): component concentrates → fills the shortfall.
- CMB: component provides the decoupled dust; khronon dial sequestered (Orthogonality, KM-II).
- **Bullet Cluster:** being collisionless (neutral, no ram pressure), the component sails through a cluster merger with the galaxies while the gas is stripped, producing the gas–lensing offset the standard (ΛCDM-class) way. The Bullet is a *relic* phenomenon, not a MOND one, consistent with its being a cluster-scale event — and the same warm-`keV` window that keeps the relic out of galaxies keeps it clumped at cluster scale, so the offset follows for free. This supersedes the topological-defect reading (`gravity/Paper_117`) as the *primary* account; the defect's offset-velocity law survives only as a speculative distinctive-if-present bonus signal.

This is the MOND + neutral-component picture (νHDM; AeST is the field version) — an existence proof that the needle *can* be threaded, conditional on the free-streaming length landing near cluster scale.

## 5. What is proven, what is open

**Established (structural / mapped):**
- The debt is real, specific, and the same debt for every MOND-class theory (KM-I §8).
- The requirements map (§2) and the galaxy/cluster/CMB scale split (§4) — corpus-native.
- Route A supplies dust *clustering* (`c_s ≈ 0`) natively; a native mechanism (Route B) for a decoupled `a⁻³` *component* exists (baryogenesis + neutral channel + binding mass).
- Abundance (~5×) is value-inherited under ED's methodology (as is `η_B`), not a defect.

**Open (and named):**
- No CMB acoustic spectrum is computed from ED; no cluster profile is fit.
- Route A cannot supply the abundance without an added mimetic constraint (checked three ways).
- Route B's relic mass / free-streaming length is inherited and expected cold — the live risk. If forced cold *and* cold breaks the galaxy fits, the sector fails.

**Update (2026-07-19) — Route B now has a Lagrangian first construction (`Paper_ED_RelicLagrangian_v1.md`).** The relic field `Φ = √(ρ/m_R)e^{iθ}` carries a *conserved commitment number* (P11 read at the field level: a committed chain cannot un-commit), so `∇_μJ^μ = 0` gives `ρ ∝ a⁻³` as a **derived** result — precisely the volume memory §3 shows Route A structurally lacks. So the `a⁻³` abundance *form* is no longer owed: it is native to the relic field, with only the *amount* (`Ω_c ≈ 0.12`) inherited (at the `η_B` tier). The remaining open items narrow to: (i) the superfluid self-term `L_self` from coarse-graining V5 (decides one-substance vs two-component); (ii) the relic mass value / free-streaming length (still the live risk); (iii) the CMB spectrum itself (feed the action to a Boltzmann code, AeST-style). The construction is a *skeleton*, honestly tiered — it fixes the form and the `a⁻³`, not the two numbers or the self-term.

**Update (2026-07-19) — item (i) resolved: `L_self` is canonical → TWO-COMPONENT** (`v5_coarsegrain_Lself_probe.py`; `Paper_ED_RelicLagrangian_v1.md` §3.3). Coarse-graining the real V5 functional gives a canonical kinetic term (`p ≈ 1.99`, density-response included), with no non-analytic `(∇θ)^{3/2}` and no `a₀` — the relic self-interaction is (super)fluid-CDM stiffness, not a MOND source. So the sector is a **CDM relic + the separate matter↔horizon interference MOND** (`Paper_QuadraticStrain_v1`); the one-substance route is closed (perturbatively; a vortex-sector edge is flagged). This makes the reconciliation of §4 the operative one: no double-count *because the two are different scales/pairings*, with the relic kept diffuse in galaxies by a large free-streaming length — which is exactly item (ii), now the dominant live risk. Item (iii) is thereby well-specified: standard (super)fluid-CDM perturbations on an `a⁻³`-native action, gated only on the mass/abundance.

**Update (2026-07-19) — item (ii) bounded: the relic must be WARM, ~0.2–0.7 keV** (`relic_mass_bound.py`). Two-component consistency squeezes the relic from both sides — warm enough to be diffuse in galaxies (no MOND double-count), cold enough to cluster at cluster scale and be dust by recombination (the CMB). The thermal-equivalent window is **~0.2–0.7 keV (warm dark matter)**, coinciding with the keV sterile-neutrino candidate. This is a **falsifiable directional prediction** (ED ⟹ warm ~keV DM, not cold WIMP CDM) — but the **tension is now quantified**: ED's mass mechanism gives GeV (~6 orders too heavy) to Planck (~26 orders), both cold. Softening note: the standard Lyman-α bound (`m_WDM ≳ 3–5 keV`) that would exclude a sub-keV relic assumes the relic makes small-scale structure; in ED, MOND does, so it does not directly apply, and the relic may sit warmer/lighter — tying its viability to MOND's small-scale (Lyman-α) success.

## 6. One-line status

**The cluster/CMB debt is mapped and shown addressable — via a native committed-neutral-relic component (Route B), reconciled with galactic MOND by scale separation — but not discharged: no spectrum is computed, and the one free value (the relic's free-streaming length) is inherited and expected to sit on the galaxy-unfriendly side.** A frontier with a named failure path, not a solved sector.

---

*Ported and extended from `event-density/foundations/KhrononMOND_Round5_Cosmology.md`. The Round-5 original maps Route A (the khronon dial) in full; this port adds Route B (the committed relic) and the 2026-07 no-go/reconciliation findings, and states the whole debt in the public repo.*
