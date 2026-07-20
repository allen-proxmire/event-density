# Dark Matter — ED Source Inventory (build map for the comprehensive paper)

**What this is.** The assembled, sorted source list for the eventual comprehensive *"ED Takes on Dark Matter"* paper. Every dark-matter-relevant artifact in the corpus, organized by the **two-crimes** spine (galactic vs cluster/CMB), each with a one-line note on what it contributes and which crime it belongs to. Built 2026-07-19. This is the map; the paper is written from it.

*(This is a working doc in the `event-density` repo, `theory/Dark_Sector/`. Paper paths below like `gravity/…`, `dark-sector/…`, `cosmology/…` are relative to the **EDG papers repo** `ED Generative/physics-papers/`; `event-density/…` paths are this repo.)*

## The spine (the organizing frame)

"Dark matter" is one word for **two distinct problems** that the field assumed were one substance:

- **Crime 1 — galaxies.** Rotation curves, the baryonic Tully–Fisher relation, `a₀`, and the "dark-matter-free" galaxies. **Culprit: the horizon.** ED's answer is MOND, read as the matter↔horizon interference cross-term. **No particle.**
- **Crime 2 — clusters and the CMB.** The cluster missing-mass shortfall, gravitational lensing, the cosmic web, the acoustic peaks, and the Bullet. **Culprit: a relic.** ED's answer is a warm neutral relic (real, collisionless dark matter). **A particle.**

Mechanism-unified (both are the same bilinear interference cross-term of `P = √b·e^{iπ}`), substance-separate. The two roles differ by whether the horizon is one of the interfering partners. Full framing: `outreach/ED_DarkMatter_OneWordTwoProblems.md`.

---

## Crime 1 — Galactic (MOND / the horizon; no particle)

| Paper | Contributes |
|---|---|
| `gravity/Paper_029_a0.md` | **Derives `a₀ = cH₀/(2π)`** — the MOND scale as the cosmic horizon expressed as an acceleration. The keystone of the galactic account. |
| `gravity/Paper_028_CosmicDecoupling.md` | `R_H = c/H₀`, the horizon that `a₀` is built from. |
| `gravity/Paper_QuadraticStrain_v1.md` | **MOND = the off-diagonal interference cross-term** (`Str = |Σ P|²`, diagonal = Newton, off-diagonal = matter↔horizon); discharges the bilocal-coupling postulate — the `√(a_N a₀)` is *forced*. The mechanism paper. |
| `gravity/Paper_030_CombinationRule.md` | The Newton+MOND combination rule; §8.4 is the MOND-line form the interference reading sharpens. |
| `gravity/Paper_031_BTFR.md` | **Slope-4, zero-parameter baryonic Tully–Fisher** — the "conspiracy" Khoury highlights, as an exact ED prediction. |
| `gravity/Paper_034_DeepMOND.md` | Deep-MOND regime behaviour in ED. |
| `gravity/Paper_036_MOND_FieldEquation.md` | ED reading of the MOND field equation. |
| `gravity/Paper_037_a0_Invariance.md` | Scale-invariance properties of `a₀`. |
| `gravity/Paper_KM-I_KhrononMOND.md` | The khronon = MOND deep field; §8 flags the cluster/CMB debt as *separate* (the seed of the two-crimes split). |
| `cosmology/Paper_ED_DF2_DF4_GroupSuppression.md` | **DF2/DF4 (dark-matter-"free" galaxies)** via the external-field effect / commitment-density saturation. Galactic, MOND-regime; predicts a *sharper* suppression knee than MOND. See "open work" — the suppression function is not yet derived. |
| `gravity/Paper_038_6_Pred_WeakLensing_Activity.md` | A galactic/lensing activity prediction (check scope on read). |

**Reframe note for the paper:** in ED *no* galaxy has a dark-matter halo (galaxies are MOND, the relic is diffuse there), so "dark-matter-free" is universal, not special to DF2/DF4 — what is special about them is only the *Newtonian-not-MOND* part (the EFE).

---

## Crime 2 — Clusters + CMB (the relic; a particle)

| Paper | Contributes |
|---|---|
| `dark-sector/Paper_ED_DarkSector.md` | **The flagship** — the two-component synthesis; start here. |
| `dark-sector/Paper_ED_RelicLagrangian_v1.md` | **The relic's Lagrangian**; `ρ ∝ a⁻³` *derived* from the P11-conserved commitment number (the volume memory a modified-gravity dial lacks). |
| `dark-sector/Paper_ED_DarkSector_Position.md` | Canonical position statement; the warm-`keV` mass bound and the honest crux. |
| `dark-sector/DarkSector_DebtMap.md` | What clusters and the CMB *require*; where MOND-class theories die; the reconciliation (incl. the Bullet). |
| `dark-sector/DarkSector_SuperfluidRelic_Program.md` | The one-substance (Berezhiani–Khoury) exploration and its resolution to two-component. |
| `cosmology/Paper_ED_Baryogenesis.md` | The relic's origin — the neutral-channel sibling of the baryons (single-template admission, P11 lock). |
| `substrate-evaluation/Paper_MassWithoutMass_BindingInertia.md` | The relic's mass = **binding** (cold-capable, V5-conditional); why a lone front is massless. |
| `qft/Paper_MS-II_MatterSectorFromTheArrow.md` | The neutral-channel field content (channel + polarity) the relic is built from. |
| `cosmology/Paper_ED_Cos_03_CMBAcoustic.md` | The CMB acoustic peaks — currently inherits `Ω_c`; the relic is its ED field-theoretic home. |
| `cosmology/Paper_ED_Cos_04_StructureFormation.md` | Linear structure formation / the cosmic web (relic clusters). |
| `gravity/Paper_KM-II_KhrononCosmology.md` | Khronon cosmology; states plainly that the cluster/CMB debt is *not* discharged. |
| `gravity/Paper_OneField_Letter.md` | The one-field capstone (carries a 2026-07-19 correction banner: the khronon does *not* natively carry the dust). |
| `gravity/Paper_117_Bullet_TopologicalDefect.md` | **The Bullet.** Repositioned 2026-07-19: the **relic** gives the offset (collisionless, ΛCDM-class) as the *primary* account; the topological-defect mechanism is a speculative alternative. |
| `gravity/Paper_OffsetVelocityLaw_MergingClusterTest.md` | The defect mechanism's distinctive **offset-velocity law** (sharp knee) — now a distinctive-if-present *bonus* signal, not the primary Bullet account. |

---

## Ruled-out / boundary candidates (state them, so the paper is complete)

| Paper | Contributes |
|---|---|
| `black-hole/Paper_041_RemnantMass.md` | Planck-mass evaporation remnants are **explicitly not** the dark-matter candidate. |
| `event-density/evaluation/DarkSector/v5_coarsegrain_Lself_probe.py` | The coarse-graining that **closed** the one-substance (superfluid) route → two-component. |
| `event-density/evaluation/DarkSector/relic_mass_bound.py` | The warm ~0.2–0.7 keV mass bound (the falsifiable warm-DM prediction). |
| `event-density/evaluation/DarkSector/v5_condensation_probe.py`, `v5_thermal_decoherence_probe.py`, `v5_offdiagonal_relic_probe.py` | The condensation / thermal-split / off-diagonal probes behind the relic's DM physics. |

---

## The evidence exhibits (Khoury's jury, mapped to ED)

The comprehensive paper walks these in order, each assigned to a crime:

1. **Flat rotation curves** → Crime 1 → MOND (029, KM-I, QuadraticStrain).
2. **Baryonic Tully–Fisher conspiracy** → Crime 1 → exact MOND prediction (031).
3. **DF2/DF4 (DM-free galaxies)** → Crime 1 → EFE/capacity saturation (DF2_DF4); ED: all galaxies halo-free.
4. **Cluster missing mass + hot gas** → Crime 2 → relic fills the shortfall (DebtMap, KM-II §8).
5. **Bullet Cluster (offset lensing)** → Crime 2 → relic passes through collisionlessly (117 repositioned); offset-velocity law = bonus (OffsetVelocity).
6. **Gravitational lensing (clusters)** → Crime 2 → relic gravitates (+ 038_6 weak-lensing).
7. **Cosmic web / large-scale structure** → Crime 2 → relic clusters (Cos_04).
8. **CMB acoustic peaks** → Crime 2 → relic = the decoupled a⁻³ dust (Cos_03 + relic Lagrangian).

---

## Open work the comprehensive paper must do (not yet in the corpus)

1. **The DF2/DF4 suppression function** — derive the external-field-effect / capacity-saturation suppression (the "sharper knee") from primitives; recast in the interference-cross-term language (the external field swamping the local matter↔horizon interference). Currently order-of-magnitude only.
2. **The CMB spectrum from the relic** — the AeST-style Boltzmann computation on the a⁻³ action, gated on the inherited relic mass. The sector's headline undelivered piece.
3. **Galactic small-scale puzzles Khoury raises** — missing satellites, the planes-of-satellites — ED has not addressed these; state them as open, do not paper over.
4. **The Bullet, written properly as a relic account** — replace the bannered reposition of Paper_117 with a first-class relic-Bullet section (free-streaming check is inherited from the mass bound; the offset magnitude is inherited `Ω_c`).

---

*Build map for the comprehensive dark-matter paper. Spine: two crimes (galaxies = horizon/MOND, clusters+CMB = relic), one mechanism (interference), substance-separate. Crime 1 papers hold up unchanged under the two-component pivot; Crime 2 is the relic arc; the Bullet moved from Crime-1-style "no particle" to Crime 2 (relic). Framing in `outreach/ED_DarkMatter_OneWordTwoProblems.md`.*
