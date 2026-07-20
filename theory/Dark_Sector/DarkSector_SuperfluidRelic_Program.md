# The Superfluid-Relic Program: One Substance for Dark Matter and MOND, and the One Calculation That Decides It

**Allen Proxmire**

**July 2026**

**Series:** Event Density (ED) Generative Papers — dark-sector program note.

**Status (updated 2026-07-19): the unification is of MECHANISM, not of substance — now DERIVED, not asserted. The relic Lagrangian's `L_self` was coarse-grained from the real V5 functional (`Paper_ED_RelicLagrangian_v1.md` §3.3; `evaluation/DarkSector/v5_coarsegrain_Lself_probe.py`) and comes out CANONICAL (`p ≈ 1.99`): the relic self-interaction is (super)fluid-CDM stiffness, not a MOND source. So the sector is TWO-COMPONENT — a CDM relic plus the separate matter↔horizon interference MOND (`Paper_QuadraticStrain_v1`, `a₀` from the horizon). The one-substance (Berezhiani–Khoury) route is closed at the perturbative level, because MOND's non-analytic `(∇θ)^{3/2}` and its `a₀` require the horizon, which the relic's local self-pairing lacks. The two roles are the same bilinear cross-term of `P = √b e^{iθ}`, differing only in whether the horizon is a partner. (The earlier khronon-mode "falsification" was retracted as a wrong-variable artifact; the horizon-`a₀` derivation located the correct structure; this coarse-graining now settles the substance question.)**

The khronon-mode probe (`v5_khronon_mode_probe.py`) measured the V5 phonon's *diagonal* self-energy (`(∇φ)^{2.00}`) and I briefly read it as falsifying the unification. **Retracted:** the probe measured the wrong term. ED's own gravity line (`Paper_QuadraticStrain_v1`, sharpening Paper_030 §8.4) reads gravitational strain as **quadratic in the participation amplitude**, `Str = |Σ_a P^{(a)}|²` with `P = √b·e^{iπ}` — and **the diagonal is Newton, the off-diagonal is MOND.** The MOND `√(a_N a₀)` is the interference *cross-term* `2√(b_loc b_horizon)cos(Δπ)` between the local source and the horizon (`a₀ = cH₀/2π` from the horizon, Paper_029). My probe computed the diagonal (Newton) and missed the off-diagonal (MOND) entirely — precisely the term the corpus labels as MOND.

**What this gives, honestly tiered:**
- **Corpus-established:** MOND = the off-diagonal interference cross-term (`Paper_QuadraticStrain_v1`); the `√` is forced by `P=√b`; the one open piece is the *constructive sign*, which that paper states is *the same* open question as the V5 kernel's attractive-coherence sign (Paper_090) — discharged with it by the P12-coherence work.
- **The unification (of mechanism):** the off-diagonal cross-term `Σ P_i* P_j` (`P=√b`) *is* the V5 cross-chain coherence form. **MOND** is that cross-term for **matter↔horizon**; the **relic's dark-matter coherence** is that cross-term for **relic↔relic**. One structure, two roles — grounded, and it explains the retraction (diagonal vs off-diagonal).
- **The honest limit (not one substance):** MOND does galaxies *without* the relic (matter↔horizon interference); the relic is still a *separate* dark component for the CMB (relic↔relic). So this unifies the *mechanism*, not the substance — the two-component reality and the galactic double-counting question between MOND and the relic **survive**. The earlier "one substance does both" is corrected to "one interference structure, two roles."
- **The correct probe (not yet run):** the *off-diagonal* cross-term with the horizon in it (matter↔horizon, and relic↔relic), read as the interference force — a different calculation from the diagonal self-energy the retracted probe ran.

The unification sections below are the live *mechanism-level* hypothesis; read them with this correction.

---

## Thesis, in one paragraph

Dark matter and MOND are **one substance read two ways.** The substance is a **committed neutral relic** — matter frozen at the inflation/saturation exit, decoupled from light because it is uncharged. Where it is **dispersed** (galaxy clusters, the CMB, cosmic voids), it acts as ordinary cold dark matter: it clusters, feeds the missing cluster mass, and shapes the acoustic peaks — the "5× the baryons." Where it is **condensed** (inside galaxies, in the calm low-acceleration regime below `a₀`), it forms a coherent state whose collective mode **is the khronon**, and that mode produces the MOND force. So the galactic "dark matter" is not an extra halo added to MOND — it **is** MOND, and the same substance is CDM everywhere else. One thing, two phases, split by the acceleration scale `a₀` that ED already carries. This is the Event Density form of *superfluid dark matter* (Berezhiani–Khoury 2015), and it repairs the over-reach in `Paper_OneField_Letter` (which asserted the khronon alone carries the dust — it does not; see that paper's 2026-07-19 correction banner).

---

## How the chain was arrived at (so the reasoning is auditable)

1. **The debt.** ED explains galaxies with MOND and *no dark-matter particle needed* (KM-I), but MOND-class theories do not cover the cluster-scale missing mass or the CMB acoustic peaks (`DarkSector_DebtMap.md`). ED does not refute a particle (Paper_029/031) — the door was open.
2. **Native routes to a field-only answer, killed.** Putting the CMB dust *abundance* in the khronon field itself fails three ways (FRW reduction → `∝H²` not `a⁻³`; the arrow primitives P11/P13 do not force the mimetic unit-gradient constraint; the emergent-metric conformal mode is a slaved bandwidth field). The abundance needs a real matter component.
3. **The committed-relic candidate.** Baryogenesis in ED (Paper_ED_Baryogenesis, M3) commits matter at the saturation exit; commit to a neutral channel and you get a decoupled, cold-capable (binding mass, Paper_MassWithoutMass), `a⁻³`, reheating-surviving relic — the neutral-channel sibling of the baryons. Form-complete, native.
4. **The abundance is comparable, not predicted.** This is an *asymmetric dark matter* mechanism, so it naturally explains why dark and ordinary matter are the *same order of magnitude* (a puzzle ΛCDM leaves as coincidence) — but the precise 5× and the relic mass are value-inherited.
5. **The mass tension.** The mass that makes the abundance natural (~proton-scale, cold) is the mass that would clump the relic into galaxies and break MOND; the mass that spares galaxies (light, warm) undermines the abundance. The two inherited numbers pull opposite ways.
6. **The unification that dissolves the tension.** If the galactic clumping *is* MOND (superfluid phase), it is not added to MOND, so it cannot double-count — the mass can be abundance-friendly and still leave galaxies to MOND. This is the superfluid-relic picture.

---

## The unification, stated cleanly

- **Substance:** the committed neutral relic (`a⁻³`, decoupled, cold-capable).
- **Dispersed phase (large scales):** CDM — clusters, CMB, the abundance.
- **Condensed phase (galaxies, below `a₀`):** a coherent state; its collective (phonon) mode is the khronon; the mode produces MOND.
- **Phase boundary:** set by whatever physically *decoheres* the relic phases — **which is now derived and is thermal.** [2026-07-19: the `a₀` boundary was retracted by the condensation calculation, then the decoherence source was identified by the thermal-decoherence probe.] ED-native decoherence is **P11 commitment on encounter** (interaction → single-channel collapse randomizes the phase); the kinetic encounter rate ∝ relative velocity, so the decoherence rate is **provably ∝ velocity dispersion** (measured exponent ≈ 1.00) — *thermal*, with acceleration nowhere in it. So galaxies (cold disks) condense → MOND; clusters (hot) disperse → CDM. The galaxy-vs-cluster dispersion ratio is ~20–100×, so the transition need only fall in that wide gap. The boundary is *not* `a₀` — it is temperature, derived from the primitives.
- **The mimetic constraint, for free:** a superfluid's phase–density conjugacy *is* the mimetic (unit-gradient) structure, so the constraint a standalone khronon would need *added* to carry dust is a *derived* consequence here: relic **density** = the dust; relic **phase** = the MOND khronon.

### Reconciliation with the standing khronon (GR-II)

ED already derives a khronon — the foliation scalar from the arrow-in-the-law (GR-II). Is it the *same* object as the relic's collective mode? **Partial, and promising.** GR-II derives its khronon by *dividing out* the normalization (the khronometric formulation): it keeps the direction (→ MOND/geometry) and discards the size (the density). The superfluid *keeps* the size as the condensate density (→ the dust). So **GR-II is the density-blind projection of the same object** — restore what it divided out, and the dust is there. This explains cleanly why GR-II carried no dust and why we kept "adding it back." It is not a naming coincidence.

---

## Tiers — what is standing, candidate, and open

| Element | Tier |
|---|---|
| Galactic MOND, no particle needed (khronon deep field) | **Standing result** (KM-I / 027–031) |
| ED does not refute a DM particle | **Stated corpus position** (Paper_029/031) |
| Cluster/CMB debt: separate, mapped, addressable | **Mapped, not discharged** (`DarkSector_DebtMap.md`) |
| Committed neutral relic (decoupled, cold-capable, `a⁻³`, survives) | **Form-complete / native** (baryogenesis M3 + MS-II + binding mass) |
| Asymmetric-DM comparability of dark:baryon abundance | **Account-tier** (explains the coincidence; precise 5× inherited) |
| One substance, two phases (superfluid-relic); MOND = the condensed mode | **Candidate hypothesis** (literature-backed; §"unification") |
| Khronon = the relic's collective mode; GR-II = density-blind projection | **Partial reconciliation** (same type; three dynamical tensions open) |
| The relic mass / free-streaming lands in a viable window | **Value-inherited; expected problematic** |
| A CMB spectrum computed from ED | **Not done** |

---

## The one calculation that decides it

Every open brake — the khronon speed (`c_s=c` vs a slow MOND phonon), the normalization (khronometric vs mimetic), the regime mapping, and the mass tension — collapses into a single physical question:

> **Does ED's committed neutral relic condense in the calm, low-acceleration environment of a galaxy — and does it fail to, in the hot environment of a cluster?**

Two framings, and the second is the ED-native one that could resolve the mass tension:

- **Standard BEC (Khoury):** condensation needs a *light* boson (de Broglie wavelength > interparticle spacing). This re-imposes the mass tension (light-to-condense vs. heavy-for-abundance).
- **ED-native — V5-coherence phase-locking (the calculation to run):** ED's relics are committed (P11) and coupled by the V5 cross-chain coherence kernel (P12-Coh rewards phase alignment, finite reach). "Condensation" here is V5 phase-locking, which survives only where **decoherence is low = the environment is calm**. Below `a₀` (galaxies) → V5-coherent → condensed → khronon → MOND; above `a₀` / hot (clusters) → V5-decohered → dispersed → CDM. **`a₀` becomes the V5 coherence boundary** — the MOND scale identified with where the relics can stay phase-coherent. If condensation is coherence-driven (not de-Broglie-driven), the light-boson requirement may not apply and the mass tension may dissolve.

**The decisive test — RUN 2026-07-19** (`event-density/evaluation/DarkSector/v5_condensation_probe.py` + `V5_Condensation_Findings.md`), on ED's real V5 coherence functional `E = Σ exp(−r/ℓ)cos(Δφ)`:

- **(c) Mass-independence — PASSED, the make-or-break.** The V5 functional contains only positions and phases; **no mass term.** So condensation cannot depend on the relic mass (unlike BEC, which needs a light boson). A heavy, abundance-friendly relic can still phase-lock. **The mass tension is dissolved** — the central threat to the program is removed.
- **(a) Condensation happens** (calm → coherence order parameter 1.00, rising decoherence → falls toward 0), **but the boundary is the decoherence *source*, not `a₀`** — it must be *thermal* (velocity dispersion) for the galaxy/cluster split to work (acceleration would wrongly condense clusters). Plus a new caveat: condensation is **density-dependent** (denser resists decoherence), so "clusters disperse to CDM" is a live heat-vs-density competition, not automatic.
- **(b) The khronon-mode test — attempted 2026-07-19, result RETRACTED as a wrong-variable artifact.** The probe (`v5_khronon_mode_probe.py`) found the bare V5 phonon's phase-stiffness is standard (`ΔE ~ (∇φ)^{2.00}`), and this was *briefly* read as falsifying the unification. **Retracted the same day:** the probe cannot test MOND because it omitted **`a₀`** (MOND's defining scale, which in ED is a *horizon* property, KM-I — a scale-free setup is analytic and *must* return `(∇φ)²`, so the Newtonian result was forced by the missing scale) and the **density–phase coupling** (where superfluid MOND actually lives; the probe held density fixed). So the phase-stiffness is standard, but *the force law is untested*. **The correct decisive probe:** the relic condensate coupled to the horizon-derived `a₀`, sourced by localized baryons, density responding, force law read off (`Newtonian` vs `√(g_N a₀)`). Not yet run.

**Follow-on — thermal-decoherence probe, RUN 2026-07-19** (`v5_thermal_decoherence_probe.py`): the decoherence source is now identified and derived. P11-commitment-on-encounter, with the encounter rate ∝ relative velocity, makes the decoherence rate **provably ∝ velocity dispersion** (exponent ≈ 1.00) — **thermal, not acceleration.** Cold (galaxy) → C=0.86 condensed → MOND; hot (cluster) → C=0.00 dispersed → CDM. **This resolves the "what decoheres the phases" question in favor of the version that works** (thermal), replacing the retracted `a₀` boundary with a temperature boundary derived from the primitives.

**Net:** the decisive calculation passed on the one question that could have killed the program (mass-independent condensation), and the follow-on resolved the decoherence source as thermal (derived) — so the galaxy=MOND / cluster=CDM split now rests on primitives, not assertion. Remaining open: the *quantitative* transition dispersion (needs ED's V5 numbers); a targeted *heat-vs-density* check for dense-and-hot clusters; whether the condensed mode is genuinely the khronon (with the right `a₀`); and whether a *background* (non-encounter) commitment adds a second decoherence channel.

**Update (2026-07-19) — the relic Lagrangian's first construction is written** (`Paper_ED_RelicLagrangian_v1.md`). It assembles the relic field `Φ = √(ρ/m_R)e^{iθ}` (ρ = the dust, θ = the candidate MOND khronon) from Baryogenesis + Mass-Without-Mass + MS-II, and *derives* `ρ ∝ a⁻³` from the P11-conserved commitment number — the CDM-relic (Route B) skeleton, with the `a⁻³` native and only the amount inherited. Crucially, it fixes the **attachment point** for the superfluid term: `L_self(Φ,∂Φ;u)`, the non-canonical kinetic functional whose deep limit must give `√(a_N a₀)`. So "the one calculation that decides it" is now sharply posed as *a term in a written action*: **coarse-grain the V5 coherence functional `E = Σ exp(−r/ℓ)cos Δφ` and read off `L_self`** — Berezhiani–Khoury-class `F(X)` → one substance, two phases; plain contact term → two components (CDM relic + the standing matter–horizon interference MOND).

**RUN 2026-07-19 (`v5_coarsegrain_Lself_probe.py`) — the answer is the plain term: TWO COMPONENTS.** `cos` is analytic (even powers only), so a gradient expansion of the finite-reach relic↔relic kernel gives `E = const + c_2(∇θ)² + c_4(∇θ)⁴ + …` — canonical, no non-analytic `(∇θ)^{3/2}` at any order, and no `a₀` (no horizon in the kernel). Measured on the real functional: `p = 1.99` (uniform), `1.99` (with density response — the concern the retracted probe missed), `1.97` (other reach); pure power, no intrinsic scale, so the force is linear in `∇θ` (Newtonian). **`L_self` is canonical → the relic is (super)fluid CDM, not a MOND source.** The Berezhiani–Khoury one-substance route needs an engineered fractional term that an analytic ED kernel cannot produce; MOND's non-analyticity + `a₀` live in the separate matter↔horizon term. Held to the negative-bar: real functional, right (small-gradient) regime, density-response included, one flagged edge (non-perturbative/vortex sector, uncovered). Consequence for the program: the mass tension and the galactic double-counting are **not** dissolved by condensation-as-MOND (that route is closed); they revert to the standard two-component constraint — the relic must be diffuse in galaxies (free-streaming length near cluster scale), the live risk. The condensation / mass-independence / thermal-split results still stand as the relic's *dark-matter* physics; they simply do not also deliver MOND.

---

## Falsifiers

- **F1:** V5 coherence of a relic gas does **not** track the `a₀` boundary (locks and decoheres at the wrong scale, or not at all) — kills the coherence-condensation mechanism and the `a₀` identification.
- **F2:** Condensation is shown to require a light boson regardless of framing, and a light relic cannot supply the inherited abundance — the mass tension is fatal, and the superfluid-relic picture reduces to ordinary (disfavored) MOND + a separately-tuned particle.
- **F3:** The condensed collective mode does not reproduce ED's specific khronometric structure (`c_s=c`, `α₂=0`) — the mode is not the khronon, and the reconciliation with GR-II fails.
- **F4:** A cold relic at the ~5× abundance is shown to break ED's galactic MOND fits *even in the condensed picture* (the clumping is not fully reorganized into MOND) — the double-counting was not actually dissolved.

---

## Position

The superfluid-relic program is a **coherent, ED-native candidate** that unifies dark matter and MOND as one committed substance in two phases, repairs the OneField over-reach, supplies the mimetic constraint for free, and identifies `a₀` with a coherence boundary — with every honest brake named and all of them converged onto **one testable question** (V5-coherence condensation). It is not a result. It is a research program with a decisive calculation queued, stated here in its "before" state so that calculation has an honest baseline. If the V5-coherence condensation tracks `a₀` mass-independently and its collective mode is the khronon, ED has one substance carrying gravity's dark sector end to end. If it does not, the sector falls back to MOND (standing) plus an inherited, tension-bound relic — still native, still honest, but not unified.
