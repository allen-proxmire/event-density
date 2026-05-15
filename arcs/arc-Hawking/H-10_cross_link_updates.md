# Arc Hawking — Memo 10: Cross-Link Update Record

**Status:** Documentation memo. Records all updates to H-7 synthesis, BH-information-paradox-resolution paper, and cross-arc connections following H-8 (stable Planck-mass remnant FORCED) and H-9 (relic-abundance calculation, relic-matter framing). Removes residual DM-explanation language. Maintains cross-arc consistency between Arc Hawking, BH-architecture walkthrough, and galactic_dynamics walkthrough.

**Date:** 2026-05-09

---

## 1. The Issue

H-7 (Arc Hawking synthesis) and the BH-information-paradox-resolution paper at `papers/BH_Information_Paradox_Resolution/bh_information_paradox_resolution.md` were drafted *before* H-8 (higher-order resummation) and H-9 (relic abundance) closed. Both documents framed the Planck-mass remnant as:

- A *conditional* prediction (CONDITIONAL on higher-order analysis).
- A *dark-matter candidate* with cosmological implications.

Both framings are now incorrect:

- **Per H-8:** Scenario C (stable Planck-mass remnant) is FORCED at substrate-structural level. The conditional framing is superseded.
- **Per H-9 + galactic_dynamics walkthrough:** ED's substrate-gravity already explains galactic dynamics without invoking dark matter. The remnant population is a *separate* structural cosmological prediction about relic-matter content, not a DM-explanation candidate.

This memo documents all updates required to bring H-7 and the BH-information-paradox-resolution paper into alignment with H-8, H-9, and the framework's substrate-gravity content.

---

## 2. Cross-Arc Dependency Summary

The framework's substrate-level account of black-hole physics, Hawking radiation, and cosmological relic content involves three structurally distinct arcs that produce empirically distinguishable predictions. The cross-arc dependency map:

### 2.1 The three arcs and what each delivers

| Arc | Delivers | Status |
|---|---|---|
| **Arc BH** (`theory/Black_Holes/`) | BH architecture: horizon as decoupling surface, no singularities, information architecture, area-law entropy, scattering structure | Closed (Memos 1–7) |
| **Arc Hawking** (`arcs/arc-Hawking/`) | Hawking radiation: spectrum, greybody factors, Page rate, Page curve, V5 cutoff, Scenario C remnant FORCED, relic-matter abundance | Closed (Memos 0–9) + Memo 10 (this) |
| **Substrate-gravity arc** (galactic_dynamics walkthrough; T19, T20, T21, ECR) | Galactic dynamics: Newton's law, transition acceleration, Combination Rule, BTFR, **without invoking dark matter** | Closed |

### 2.2 What each arc requires from the others

```
Substrate-gravity arc
   │
   │ supplies: ℓ_P (T19), G = c³ℓ_P²/ℏ, a₀ = cH₀/(2π)
   │
   ▼
Arc BH ───────────────┐
   │                   │
   │ supplies:         │ supplies:
   │ - decoupling      │ - saturated zone (BH-3)
   │   surface (BH-2)  │ - motif alphabet g (BH-5)
   │ - entanglement-   │ - bandwidth-budget
   │   straddling (BH-4)│   structure (BH-2)
   │                   │
   ▼                   ▼
Arc Hawking ───────────┘
   │
   │ produces: spectrum (H-1), greybody (H-2), Page rate (H-3),
   │           V5 cutoff (H-4), Page curve (H-5), regulated-
   │           completion verdict (H-6), synthesis (H-7),
   │           Scenario C FORCED (H-8), relic abundance (H-9)
   │
   ▼
Cosmology (downstream)
   │
   │ inherits: stable Planck-mass remnant, scenario-dependent Ω_relic
   │
   ▼
Cosmic energy budget includes structural relic-matter component
```

### 2.3 The galactic-dynamics independence

The substrate-gravity arc (galactic_dynamics walkthrough) explains:
- Newton's law in the high-acceleration regime
- The transition acceleration $a_0 = cH_0/(2\pi)$
- Flat rotation curves and the slope-4 BTFR
- The radial-acceleration relation

**without invoking dark matter** at any step. ED's substrate-gravity content does not require, and does not posit, a dark-matter particle population. What ΛCDM attributes to dark-matter halos, ED attributes to substrate-level dipole-mode projection plus geometric-mean composition (the Combination Rule).

The Arc Hawking + cosmology content therefore must *not* be framed as supplying dark matter to ED. The Planck-mass remnant population from H-8 + H-9 is a *separate* structural cosmological prediction. It is a relic-matter component of the cosmic energy budget, derived from the substrate-cutoff endpoint of PBH evaporation. It is observationally testable as a relic-matter signature, not as a DM-detection target.

### 2.4 Cross-arc consistency requirements

For consistency across the three arcs:

1. **Substrate-gravity walkthrough must remain DM-free.** The galactic_dynamics walkthrough's framing (rotation curves explained without DM) must be preserved.

2. **Arc Hawking outputs must not claim DM-explanation.** Hawking-arc memos and paper must frame remnant cosmology as relic-matter content, not as DM candidates.

3. **Cosmological inheritance must be framed as relic-matter.** The Planck-mass remnant population's cosmological abundance is $\Omega_{\mathrm{relic}}$, computed in H-9, with no DM-explanation framing.

4. **All references to "dark matter" in Arc Hawking content must be removed or recontextualized.** Where dark matter appears in cited literature (e.g., Carr et al. "Primordial Black Holes as Dark Matter"), the title is preserved as standard literature reference but the framework's framing is explicitly relic-matter, not DM-explanation.

---

## 3. H-7 Update Record

The following sections of `arcs/arc-Hawking/H-7_synthesis.md` are updated to reflect H-8 and H-9 closure plus relic-matter framing. The original H-7 text is preserved as a record; the updated content is documented here and applied to the file.

### 3.1 Section 1 (Consolidated Arc Hawking Verdict) — UPDATED

**Original phrasing:**
> "Late-time scenario CONDITIONAL on higher-order resummation"

**Updated phrasing:**
> "Late-time scenario RESOLVED via H-8 higher-order resummation: Scenario C (stable Planck-mass remnant at $M_* = c_*\ell_P$) FORCED at substrate-structural level. Planck-mass remnant population is a structural *relic-matter component* of the cosmic energy budget per H-9, not a dark-matter candidate (ED's substrate-gravity already explains galactic dynamics without DM)."

### 3.2 Section 4 (Final Verdict Class) — UPDATED

**Original phrasing:**
> "Modified-theory content at extreme scales (conditional on Planck-mass remnant scenario)"

**Updated phrasing:**
> "Modified-theory content at extreme scales (Scenario C Planck-mass remnant FORCED via H-8). The framework predicts stable Planck-mass remnants from PBH evaporation, with cosmological relic-matter abundance $\Omega_{\mathrm{relic}}$ scenario-dependent per H-9. The remnant population is a structural relic-matter component, not a dark-matter candidate."

### 3.3 Section 7 (Late-Time A/B/C Scenario Branching) — REWRITTEN

**Original framing:** Three scenarios as conditional possibilities.

**Updated framing:**

- **Scenario A (Full Recovery, no remnant):** REFUTED by H-8. Substrate constraints (P4 + DCGT + P11) jointly forbid full evaporation to $M = 0$.

- **Scenario B (Modified Turnover, no remnant):** INCOMPLETE per H-8. V5-alone analysis produces this; full substrate inventory produces Scenario C.

- **Scenario C (Stable Planck-mass remnant):** **FORCED at substrate-structural level via H-8.** The combination of V5 finite-memory + DCGT hydrodynamic-window closure + P4 bandwidth-finiteness + P11 commitment irreversibility produces a stable substrate-determined endpoint at $M_* = c_*\ell_P$ where $c_*$ is order-unity (INHERITED from substrate microscopic details). The substrate-saturated cluster at $M = M_*$ is permanent (P11-locked), DCGT-closed, P4-bounded.

The framework's late-time prediction is **definite**, not conditional. ED predicts stable Planck-mass remnants from PBH evaporation. The cosmological-abundance question (what fraction of the cosmic energy budget the remnants occupy) is computed in H-9 and is scenario-dependent on the empirical PBH formation history.

### 3.4 Section 8 (Falsifiable Predictions) — RELIC-MATTER FRAMING

**Original §8.4 phrasing:** "Long-range: Dark-matter remnant searches"

**Updated §8.4 phrasing:** "Long-range: Relic-matter signature searches"

**Updated §8.4 content:** Per H-9, the Planck-mass remnant population is a *structural relic-matter component* of the cosmic energy budget, not a dark-matter candidate. ED's substrate-gravity explains galactic dynamics without DM. Searches for relic-matter signatures (microlensing constraints on Planck-mass relics, cosmic-ray collisions, structure-formation effects) constrain the relic-matter abundance $\Omega_{\mathrm{relic}}$ but do not constrain dark matter (which the framework does not posit).

### 3.5 Section 13 (What Arc Hawking Closed) — UPDATED LIST

**Original list:** Seven results (H-1 through H-7).

**Updated list:** Nine results (H-1 through H-9):

1. H-1: Hawking thermal spectrum and temperature $T_H = \kappa/(2\pi)$.
2. H-2: Greybody factors from substrate-channel scattering.
3. H-3: Page evaporation rate $\dot M = -\alpha_{\mathrm{Page}}/M^2$ at leading order.
4. H-4: First explicit substrate-derived corrections at $(\ell_P/M)^2$.
5. H-5: Page curve and bipartite-entanglement evolution with substrate-level information-recovery mechanism.
6. H-6: Regulated-completion classification of ED relative to standard semiclassical Hawking.
7. H-7: Cross-domain unification (V5 kernel doing three jobs across closed sectors).
8. **H-8: Higher-order resummation. Scenario C (stable Planck-mass remnant) FORCED at substrate-structural level.**
9. **H-9: Cosmological relic-matter abundance from PBH evaporation. $\Omega_{\mathrm{relic}}$ scenario-dependent on PBH formation history; not framed as dark matter.**

---

## 4. BH-Information-Paradox-Resolution Paper Update Record

The following sections of `papers/BH_Information_Paradox_Resolution/bh_information_paradox_resolution.md` are updated.

### 4.1 Abstract — UPDATED

**Original phrasing:**
> "...conditional Planck-mass remnant scenario with cosmologically significant implications for primordial-BH-remnant dark matter."

**Updated phrasing:**
> "...structural Planck-mass remnant prediction (FORCED via H-8 substrate-cutoff resummation) with the present-day cosmological relic-matter fraction $\Omega_{\mathrm{relic}}$ computed in H-9 as scenario-dependent on the empirical PBH formation history. **Critical framing note:** ED's substrate-gravity (separate galactic_dynamics walkthrough) explains galactic phenomenology — flat rotation curves, slope-4 BTFR, transition acceleration $a_0 = cH_0/(2\pi)$ — without invoking dark matter. The Planck-mass remnant population is therefore a *separate structural cosmological prediction* about cosmic relic-matter content, not a dark-matter candidate."

### 4.2 §11 (Late-Time Scenarios) — REWRITTEN

**Original framing:** Three conditional scenarios; remnant cosmologically significant as DM candidate.

**Updated framing:**

The H-8 higher-order resummation analysis produces a definite verdict on the late-time evaporation profile:

- **Scenario A** (full recovery to $M = 0$) is REFUTED by substrate constraints (P4 + DCGT + P11 jointly forbid).
- **Scenario B** (modified turnover with eventual full evaporation) is INCOMPLETE — produced by V5-alone analysis but not by the full substrate inventory.
- **Scenario C** (stable Planck-mass remnant at $M_* = c_*\ell_P$, $c_*$ order-unity INHERITED) is **FORCED at the substrate-structural level**.

The substrate-saturated cluster at $M = M_*$ is permanent (P11-locked), DCGT-closed (substrate-to-continuum bridge fails at $L_{\mathrm{flow}} \sim \ell_P$), and P4-bounded (finite participation density). The framework's late-time evaporation profile is therefore definite, not conditional.

**Critical framing note:** ED's substrate-gravity (galactic_dynamics walkthrough) explains galactic dynamics — rotation curves, BTFR, transition acceleration — *without* invoking dark matter. The framework does not require, and does not posit, a dark-matter particle population. The Planck-mass remnant population from PBH evaporation is therefore *not* a dark-matter candidate. It is a structural cosmological prediction about *relic-matter content* — a separate component of the cosmic energy budget.

The cosmological abundance of remnants is computed in H-9 [reference] and depends on the empirical PBH formation history. For standard scale-invariant or critical-collapse PBH formation: $\Omega_{\mathrm{relic}}$ is negligibly small (cosmologically subdominant). For blue-tilted or inflationary-spike scenarios: $\Omega_{\mathrm{relic}}$ can range from $10^{-15}$ to $\sim 10^{-3}$ within current observational constraints. Larger values are excluded by BBN, CMB-distortion, and gamma-ray-background constraints on the parent PBH population.

The framework predicts a structurally non-zero relic-matter component (FORCED via H-8); the specific abundance is INHERITED from the empirical cosmological PBH formation history.

### 4.3 §12.4 (Falsifiable Predictions) — RENAMED AND REWRITTEN

**Original heading:** "12.4 Dark-matter remnant searches (long-range)"

**Updated heading:** "12.4 Relic-matter signature searches (long-range)"

**Original content:** Framed as DM-detection candidate.

**Updated content:**

If Scenario C realizes (FORCED per H-8), primordial-BH-remnant relic-matter has specific cosmological signatures:
- Microlensing: not feasible (Planck-mass too small for current sensitivity).
- Gravitational lensing: not feasible (gravity per particle too weak).
- Cosmic-ray collisions involving Planck-mass relics: extreme-energy detector signatures (current sensitivity insufficient).
- Structure-formation effects: weak gravitational signatures (Planck-mass particle population too dilute in standard scenarios).

Continued absence of Planck-mass relic-matter signatures at improving experimental sensitivity continues to constrain the relic-matter abundance. This is *not* a dark-matter constraint (the framework does not posit DM); it is a constraint on the structural relic-matter component predicted by H-8 + H-9.

Direct detection at any specific abundance level would corroborate the framework's substrate-cutoff endpoint mechanism plus the assumed PBH formation history.

### 4.4 §13 (Regulated-Completion Verdict) — UPDATED

**Original phrasing:**
> "Modified-theory content at extreme scales (Scenario C remnant scenario, conditional on higher-order analysis)"

**Updated phrasing:**
> "Modified-theory content at extreme scales (Scenario C Planck-mass remnant FORCED via H-8 substrate-cutoff resummation). The Planck-mass remnant population is a structural cosmological prediction about relic-matter content, with abundance $\Omega_{\mathrm{relic}}$ scenario-dependent (per H-9); not a dark-matter candidate."

### 4.5 §15 (Conclusions) — UPDATED

**Original phrasing:**
> "...possible Planck-mass remnant scenario with cosmologically significant implications for primordial-BH-remnant dark matter."

**Updated phrasing:**
> "...definite Planck-mass remnant prediction (FORCED per H-8 substrate-cutoff resummation), with structural cosmological relic-matter implications computed in H-9. **The framework does not invoke dark matter at any stage:** substrate-gravity (separate galactic_dynamics walkthrough) explains galactic dynamics, and the Planck-mass remnant population is a *separate* relic-matter component of the cosmic energy budget."

### 4.6 References — UPDATED

Add references [14, 15, 16] from H-9:
- [14] Proxmire, A. *Arc Hawking H-8: Higher-Order Resummation and the Late-Time Evaporation Endpoint.* May 2026.
- [15] Proxmire, A. *Walkthrough: From Primitives to Galactic Dynamics.* May 2026. *(Substrate-gravity content explaining galactic phenomenology without DM)*.
- [16] Proxmire, A. *Arc Hawking H-9: PBH Remnant Relic-Abundance.* May 2026.

Add framing note for reference [1] (Carr et al. "Primordial Black Holes as Dark Matter"):
> "[1] Carr, B., Kuhnel, F., Sandstad, M. ... [Standard compilation of PBH constraints; framing note: the title's 'as Dark Matter' refers to the standard literature's framing, not to ED's framework, which does not require DM.]"

---

## 5. Cross-Link Additions to galactic_dynamics Walkthrough

The galactic_dynamics walkthrough (`from_primitives_to_galactic_dynamics.md`) currently does not reference Arc Hawking or the relic-matter content. A short cross-reference paragraph should be added to clarify the relationship between substrate-gravity (which handles galactic dynamics without DM) and the Hawking-arc remnant content (which produces a separate cosmological relic-matter component).

### 5.1 Recommended addition — placed in §8 ("What This Argument Establishes") or as a footnote

```
Note on the framework's broader cosmological content:

The framework's substrate-gravity content (this walkthrough) explains the
empirical phenomenology of galactic dynamics — flat rotation curves,
slope-4 BTFR, transition acceleration — without invoking dark matter.
ED does not require, and does not posit, a dark-matter particle population
to explain galactic dynamics.

A separate structural prediction in the framework's Black Hole arc
(Arc Hawking, Memos H-8 and H-9) concerns the cosmological remnants of
primordial black-hole evaporation. Per H-8's higher-order resummation
analysis, all PBHs that have fully evaporated by the present epoch leave
stable Planck-mass remnants. Per H-9's relic-abundance calculation,
these remnants form a structural relic-matter component of the cosmic
energy budget, with abundance Ω_relic scenario-dependent on the empirical
PBH formation history.

The Planck-mass remnant population is *not* a dark-matter candidate.
It is a separate cosmological prediction about cosmic relic-matter
content, derived from the substrate-cutoff endpoint of PBH evaporation.
The substrate-gravity content of this walkthrough handles galactic
dynamics independently of any relic-matter contribution from PBH
evaporation.
```

This cross-reference clarifies that (a) substrate-gravity does not need DM, and (b) the H-arc remnant content is a separate structural prediction not framed as DM.

---

## 6. The Updated Cross-Arc Verdict

Combining the updates:

> **Updated Arc Hawking + BH + Substrate-Gravity verdict:**
>
> 1. **Galactic dynamics** (rotation curves, BTFR, transition scale, radial-acceleration relation) are explained by ED's substrate-gravity content at substrate-structural level, **without dark matter**.
>
> 2. **Black-hole architecture** (horizon as decoupling surface, no singularities, information architecture, area-law entropy, scattering structure) is closed via Arc BH.
>
> 3. **Hawking radiation** (spectrum, greybody, Page rate, Page curve, V5 cutoff, regulated-completion verdict) is closed via Arc Hawking H-1 through H-7.
>
> 4. **Late-time evaporation profile** is closed via H-8: Scenario C (stable Planck-mass remnant at $M_* = c_*\ell_P$) FORCED at substrate-structural level.
>
> 5. **Cosmological relic-matter abundance** is closed via H-9: $\Omega_{\mathrm{relic}}$ scenario-dependent on PBH formation history, with bounds from observational constraints.
>
> 6. **The framework predicts a structural relic-matter component** of the cosmic energy budget from PBH evaporation. **It does not predict, require, or posit dark matter.**
>
> 7. **The relic-matter component is observationally testable** through CMB-distortion, gamma-ray-background, and structure-formation searches that constrain parent PBH populations and thereby the relic abundance.

---

## 7. Updated Repository State

After this memo, the framework's repository state for the BH-Hawking-cosmology sector:

| Document | Status |
|---|---|
| `from_primitives_to_galactic_dynamics.md` | Unchanged (substrate-gravity, no DM); cross-link addition recommended |
| `from_primitives_to_black_hole_architecture.md` | Unchanged (BH architecture; no DM-framing required) |
| `theory/Black_Holes/Arc_BH_*` | Unchanged (Arc BH closed before H-arc) |
| `arcs/arc-Hawking/H-0_opening.md` | Unchanged |
| `arcs/arc-Hawking/H-1_spectral_form_and_temperature.md` | Unchanged |
| `arcs/arc-Hawking/H-2_greybody_factors.md` | Unchanged |
| `arcs/arc-Hawking/H-3_page_rate_corrected.md` | Unchanged (note: late-time content now superseded by H-8) |
| `arcs/arc-Hawking/H-4_v5_cutoff_corrections.md` | Unchanged |
| `arcs/arc-Hawking/H-5_information_correlations.md` | Unchanged (note: late-time scenarios now resolved by H-8) |
| `arcs/arc-Hawking/H-6_semiclassical_equivalence.md` | Unchanged (Scenario C now FORCED rather than conditional) |
| `arcs/arc-Hawking/H-7_synthesis.md` | **TO BE UPDATED** per §3 of this memo |
| `arcs/arc-Hawking/H-8_higher_order_resummation.md` | Unchanged (this is the source memo) |
| `arcs/arc-Hawking/H-9_pbh_remnant_relic_abundance.md` | Unchanged (this is the source memo) |
| `arcs/arc-Hawking/H-10_cross_link_updates.md` | This memo |
| `papers/BH_Information_Paradox_Resolution/bh_information_paradox_resolution.md` | **TO BE UPDATED** per §4 of this memo |
| `from_primitives_to_hawking_radiation.md` | Cross-link addition recommended (§5) |

---

## 8. Maintenance Discipline

**No new active CANDIDATEs introduced.** The framework's CANDIDATE inventory remains {} as of arc-opening tally and post-H-9 closure tally.

**No new substrate primitives introduced.** Updates are documentation-level reframing of existing closed-arc content.

**The framing change from "DM candidate" to "relic-matter component" is structurally important.** It correctly aligns the framework's Hawking-arc cosmological predictions with the substrate-gravity content (which explains galactic dynamics without DM). The two arcs now produce empirically distinguishable predictions in their respective domains:
- Substrate-gravity → galactic dynamics observables (rotation curves, BTFR, RAR).
- Arc Hawking → cosmological relic-matter observables (abundance constraints, signature searches).

These are *separate* empirical domains tested by *separate* observational programs.

---

## 9. Summary

**What this memo accomplished.**

- Documented all updates to H-7 synthesis (§3) reflecting H-8 + H-9 closure and removing DM framing.
- Documented all updates to BH-information-paradox-resolution paper (§4) reflecting H-8 + H-9 closure and removing DM framing.
- Recommended cross-link addition to galactic_dynamics walkthrough (§5) clarifying substrate-gravity / Hawking-arc / cosmology relationships.
- Produced cross-arc dependency summary (§2 and §6) clarifying that substrate-gravity handles galactic dynamics without DM, while Arc Hawking + cosmology produces a separate relic-matter prediction.
- Maintained CANDIDATE inventory discipline (§8): no new primitives, no new active CANDIDATEs.

**Brief 2–3 sentence summary:** This memo records the cross-link updates needed to bring H-7 synthesis and the BH-information-paradox-resolution paper into alignment with H-8 (Scenario C Planck-mass remnant FORCED) and H-9 (cosmological relic-matter abundance), while removing residual dark-matter-explanation framing from both documents. The framework's architectural verdict is now: substrate-gravity explains galactic dynamics without dark matter; Arc Hawking + cosmology produce a *separate* structural relic-matter component of the cosmic energy budget from stable Planck-mass remnants of PBH evaporation. The cross-arc dependency map is clean: substrate-gravity supplies cosmological constants ($\ell_P$, $G$, $a_0$) to Arc BH and Arc Hawking, which produce the relic-matter prediction; the substrate-gravity walkthrough itself handles galactic dynamics independently of any relic-matter contribution.

---

## 10. Recommended Next Steps

Multiple options, in decreasing order of immediate productivity:

1. **(Editorial pass) Apply §3 updates to H-7 synthesis.** Targeted edits to the §1, §4, §7, §8, §13 portions of `H-7_synthesis.md`. Estimated 0.5 sessions.

2. **(Editorial pass) Apply §4 updates to BH-information-paradox-resolution paper.** Targeted edits to abstract, §11, §12.4, §13, §15, references of the paper. Estimated 1 session.

3. **(Cross-link addition) Add §5 cross-reference paragraph to galactic_dynamics walkthrough.** Brief addition clarifying substrate-gravity / Hawking-arc / relic-matter relationships. Estimated 0.25 sessions.

4. **(Memory update) Document H-8 + H-9 + H-10 closures in MEMORY.md.** Update the framework's auto-memory to reflect Arc Hawking closure with Scenario C FORCED + relic-matter framing. Brief documentation pass.

5. **(Walkthrough on substrate-cutoff regularization)** A walkthrough articulating the substrate-cutoff regularization pattern across multiple framework sectors (V5 cutoff in Hawking, DCGT closure at Planck mass, substrate-saturation regime in BH interior, possible substrate-cosmology limits). Title: `from_primitives_to_substrate_cutoff_regularization.md`. Estimated 1–2 sessions.

6. **(Substrate cosmology Arc COSMO scoping)** With the relic-matter content now framed correctly, the substrate-cosmology arc becomes the natural follow-on. Substrate-derived Friedmann-class equations, $H_0$ derivation, expansion history. Estimated 2–4 sessions for scoping.

7. **(Continue priority list)** Other items: O1 (superradiance amplitude), O3 (full Kerr interior), B5 (SM gauge group residue), C1/GR-4A (Einstein-equation emergence) become the next-natural-arc candidates.

---

**Pause for further instruction.**
