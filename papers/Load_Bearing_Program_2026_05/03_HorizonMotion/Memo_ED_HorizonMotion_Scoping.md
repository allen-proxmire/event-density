# Memo_ED_HorizonMotion_Scoping — Scoping Memo for Load-Bearing Derivation #3

**Series:** Wave-3 Scoping Memo (Cosmology + Dynamics Arcs; load-bearing derivation #3 from Memo_ED_CosmologyAndDynamics_ResearchDirections §4)
**Status:** Substrate-graph scoping of whether the horizon-motion law (ED-side analog of GR's $\dot H + H^2$ + causal structure governing horizon advance/recession) can be derived from existing ED substrate content. Closure would unlock the Paper_ED_Dyn_02 (proposed Horizon-Motion-Law paper) + Paper_ED_Cos_05 (Dark energy) + Paper_ED_Dyn_04 (Gravitational collapse), per the research-directions memo §4. **Not a derivation. No new primitives proposed.**
**Date:** 2026-05-16
**Anchors:** Paper_ED_Cos_01 (updated M3; M3 substrate-graph chain established for inflation-phase exponential growth); Paper_073 (DCGT); Paper_ED_SC_4_9 (substrate-action saddle Hessian); Paper_089 (V1 retarded kernel + T18); Paper_093 (T18 kernel-arrow); Paper_090 (V5 cross-chain); Paper_ED_GW_00 ("horizons are the dynamics" corpus statement); Paper_ED_CCC §3.4 (horizon-universalization content); Papers SC-4.x; Memo_ED_CosmologyAndDynamics_ResearchDirections §4 (load-bearing derivation #3); seven exponential-growth memos (inflation-arc precedent for substrate-research closure pattern).

---

## §1 Standard cosmology horizon-motion (brief recap)

Three distinct horizon quantities are used in standard cosmology:

- **Particle horizon** $r_P(t) = a(t) \int_0^t dt'/a(t')$ — maximum comoving distance from which light could have reached us by time $t$.
- **Event horizon** $r_E(t) = a(t) \int_t^\infty dt'/a(t')$ — maximum comoving distance to which a signal sent at $t$ could reach.
- **Hubble radius** $r_H(t) = 1/H(t)$ — characteristic length scale of cosmological expansion.

The horizon-motion law is governed by Friedmann equations:

$$
H^2 = \frac{8\pi G}{3}\rho - \frac{k}{a^2}, \qquad \dot H + H^2 = -\frac{4\pi G}{3}(\rho + 3p) = -\frac{4\pi G}{3}\rho(1+3w)
$$

Different cosmological phases (with different equations of state $w$) give different horizon evolutions:

- **De Sitter** ($w = -1$): $\dot H = 0$, $H$ constant, Hubble radius constant in comoving coordinates, particle horizon grows exponentially in physical coordinates. **Covered by M3 chain (Paper_ED_Cos_01, inflation-phase).**
- **Radiation-dominated** ($w = 1/3$): $a \propto t^{1/2}$, $H \propto 1/t$, particle horizon $\propto t$.
- **Matter-dominated** ($w = 0$): $a \propto t^{2/3}$, $H \propto 1/t$, particle horizon $\propto t$.
- **$\Lambda$-dominated late universe** ($w = -1$): same as de Sitter; late-universe Hubble parameter $H_0$.

The horizon-motion law fundamentally connects causal structure + cosmological expansion + energy-momentum content via the Friedmann equations.

---

## §2 Candidate substrate-graph quantities for horizon advance/recession

Four substrate-side candidates exist for "what governs horizon motion at substrate-graph level":

**(α) Substrate-c causal cones via V1 retarded support.** Per Paper_089 + Paper_093 T18, V1 retarded propagation establishes substrate-graph causal structure at substrate-c. Each substrate-graph locus has a forward-causal cone of V1-reach within $\ell_{V_1}$ per substrate-time-step. Aggregated over many substrate-time-steps, V1 establishes the substrate-side analog of the GR continuum light cone.

**(β) V5 cross-chain coupling structure.** Per Paper_090, V5 supplies cross-chain correlations with finite memory $\tau_{V_5}$. V5 doesn't directly establish causal horizons (it's not propagation; it's correlation), but V5 affects which chains are causally entangled — relevant for the horizon-as-thermodynamic-boundary reading (Bekenstein-Hawking-class).

**(γ) Saddle-Hessian boundary dynamics.** Per Paper_ED_SC_4_9 + Paper_ED_GW_00 §3.1 corpus statement: *"the saddle is the geometry; the gradients are the calculus; the boundaries are the topology; the horizons are the dynamics."* Saddle-Hessian eigenvalue-sign boundaries (where Hessian signature transitions) ARE substrate-graph horizons. Their evolution under V1 + V5 dynamics IS horizon motion at substrate level.

**(δ) DCGT-induced effective metric and continuum causal cones.** DCGT (Paper_073) translates substrate-graph causal structure to continuum-side metric content. The continuum-side horizon is the boundary of the continuum-side causal cone, derived from the continuum metric DCGT produces from substrate-graph V1 content.

These four quantities are not mutually exclusive — they likely all contribute to a full substrate-graph horizon-motion derivation.

---

## §3 M3 chain's relation to horizon motion

The audited M3 substrate-graph chain (Paper_ED_Cos_01 §3.8) closes the exponential-growth derivation for the inflation regime via DCGT translating constant substrate-action density to vacuum-energy-like continuum stress-energy with $w \approx -1$ → Friedmann recovery → $a(t) \propto e^{Ht}$.

**Direct implication for horizon motion in the inflation phase:**

- $H$ constant during inflation (per M3 chain) → Hubble radius constant in comoving coordinates
- Particle horizon grows exponentially in physical coordinates
- Event horizon $= 1/H$ constant

**This is the standard de Sitter horizon structure, inherited from M3 chain Steps D + E.**

**For non-inflation phases (RDE, MDE, LDE late universe):** the M3 chain does NOT directly apply. The substrate-side reading of $w$ in non-saturation regimes requires separate substrate-graph derivation (substrate-action content with non-uniform diffusion-production balance produces non-vacuum-energy equation of state).

**Implication:** load-bearing #3 (horizon-motion law) has two distinct aspects:

- **Inflation-phase horizon motion** — closes via M3 chain inheritance (already done).
- **Non-inflation-phase horizon motion** (RDE, MDE, LDE) — requires separate substrate-graph derivation parallel to the M3 chain pattern but for non-saturation substrate states.

Load-bearing #3 targets primarily the non-inflation-phase case. The M3 chain established the pattern (substrate-graph state → DCGT translation → continuum stress-energy → Friedmann recovery → horizon evolution); load-bearing #3 needs to apply the same pattern to non-saturation regimes.

---

## §4 Candidate closure routes

Five candidate routes for the load-bearing #3 closure:

**Route 1: Substrate-c causal cones + DCGT continuum metric → standard cosmology horizon evolution (parallel to M3 chain).**

Mechanism: V1 establishes substrate-graph causal cones. DCGT coarse-grains to continuum light cones with effective light-speed $c$. Substrate-side stress-energy (Noether on $S_{\mathrm{sub}}$ for non-saturation states) gives non-vacuum-energy continuum stress-energy via DCGT. Standard Friedmann equations + horizon-evolution standard inheritance give the horizon-motion law for each cosmological phase.

**Plausibility: HIGH.** Direct parallel to M3 chain; uses same substrate-side Noether + DCGT translation + Friedmann inheritance machinery; just applied to non-saturation substrate states.

**Load-bearing requirement:** substrate-graph derivation of substrate stress-energy for non-saturation states. Likely closes at D-via-I via the same kind of chain as M3 (with appropriate state-dependent calculations replacing the constant-density saturation case).

**Route 2: Saddle-Hessian boundary dynamics as substrate-graph horizon motion.**

Mechanism: per Paper_ED_GW_00 §3.1 + Paper_ED_SC_4_9, saddle-Hessian eigenvalue-sign boundaries are substrate-graph horizons. Horizon motion = evolution of these boundaries under V1 + V5 + DCGT dynamics.

**Plausibility: MEDIUM.** Substantive substrate-graph work; requires explicit construction of saddle-Hessian boundary motion under substrate-side dynamics. May not reduce to standard cosmology horizon evolution directly (would be ED-specific substrate-graph horizon content).

**Load-bearing requirement:** substrate-graph derivation of how saddle-Hessian eigenvalue-sign boundaries evolve. Genuinely new substrate-research; potentially produces results beyond standard cosmology horizon-motion law (e.g., black-hole horizon dynamics could share substrate-graph machinery with cosmological horizons).

**Route 3: V1/V5 causal-structure composition under DCGT → effective horizon-motion law.**

Mechanism: explicit composition of V1 retarded causal structure + V5 cross-chain coupling under DCGT produces an effective causal-structure framework at the continuum side. This framework determines horizon advance/recession via the substrate-side analog of geodesic equations.

**Plausibility: MEDIUM-HIGH.** Uses existing kernels + DCGT; substantive composition work; closure plausibility depends on whether V1/V5 + DCGT composition reproduces standard cosmology causal-structure cleanly.

**Load-bearing requirement:** substrate-graph derivation of V1 + V5 composition under DCGT. Substantive; may produce ED-specific horizon-motion content beyond standard cosmology.

**Route 4: Friedmann-equation substrate-graph inheritance (via Route 1 + standard Friedmann recovery).**

Mechanism: this is essentially Route 1 + the standard-cosmology inheritance step. Substrate-side stress-energy from Noether on $S_{\mathrm{sub}}$ → DCGT continuum stress-energy → Friedmann equations $\dot H + H^2 = -(4\pi G/3)\rho(1+3w)$ inherited → horizon-motion law for each phase.

**Plausibility: HIGH** (conditional on Route 1 closing).

**Load-bearing requirement:** Route 1 closure for substrate-side stress-energy in non-saturation states. Standard cosmology Friedmann + horizon evolution is then automatic inheritance.

**Route 5: Bekenstein-Hawking-class horizon area-entropy law (BH-arc analog).**

Mechanism: BH horizons (Paper_039, Paper_047) have Bekenstein-Hawking entropy = area/4. Cosmological horizons may have analogous structure (de Sitter horizon temperature $T = H/(2\pi)$ per Gibbons-Hawking 1977). Substrate-graph derivation of horizon area-entropy relation would give substrate-side reading of thermodynamic horizon properties.

**Plausibility: MEDIUM.** Substantive but specialized to thermodynamic-horizon content (BH-arc + cosmological-horizon thermodynamics). Less directly relevant to cosmological horizon-motion than Routes 1, 3, 4.

**Load-bearing requirement:** substrate-graph derivation of horizon area-entropy from V5 cross-chain content + DCGT. Specialized to thermodynamic-horizon arc.

---

## §5 Load-bearing vs vocabulary-level routes

| Route | Load-bearing? | Pattern parallel to M3 chain? |
|---|---|---|
| **Route 1** (substrate-c + DCGT + Friedmann) | **YES — load-bearing for full horizon-motion law** | YES — same pattern as M3 chain applied to non-saturation states |
| **Route 2** (saddle-Hessian boundary dynamics) | Substantive but specialized; substrate-graph-specific horizon content | NO — substrate-graph-specific; potentially produces ED-distinctive content |
| **Route 3** (V1/V5 composition under DCGT) | Substantive; could supply substrate-side identification | Partial parallel |
| **Route 4** (Friedmann inheritance) | Standard inheritance conditional on Route 1 | YES — Route 4 = Route 1 + standard inheritance |
| **Route 5** (area-entropy law) | Specialized to thermodynamic-horizon arc; not load-bearing for general horizon-motion | NO |

**Net assessment:**

- **Routes 1 + 4 are the cleanest substrate-graph closure path** — direct parallel to M3 chain pattern, applied to non-saturation substrate states. Closure plausibility high.
- **Route 2 (saddle-Hessian dynamics) is a substantively distinct substrate-graph route** that could supply ED-specific horizon content beyond standard cosmology. Plausibility medium; potentially valuable for cross-arc applications (BH-arc, cosmology-arc, dynamics-arc).
- **Route 3 (V1/V5 composition) is intermediate** — substantive but may largely reduce to Route 1 + 4 under standard hydrodynamic-window DCGT.
- **Route 5 is specialized** to thermodynamic-horizon content; relevant for BH-arc and dark-energy thermodynamics; not load-bearing for general horizon-motion law.

---

## §6 IDENTIFIED vs OPEN

### IDENTIFIED:

- **Inflation-phase horizon motion** (de Sitter) is closed via M3 chain inheritance (Paper_ED_Cos_01 §3.8). $H$ constant; Hubble radius constant comoving; particle horizon grows exponentially in physical coordinates. ✓
- **Standard cosmology Friedmann equations** + horizon evolution for each phase are well-established continuum-side. Inheriting these via DCGT continuum bridge is the path Route 4 takes.
- **Saddle-Hessian boundaries as substrate-graph horizons** (per Paper_ED_GW_00 §3.1 corpus statement). The corpus identifies horizons as saddle-Hessian boundary phenomena.
- **Pattern from M3 chain** (substrate-side Noether → DCGT continuum stress-energy → Friedmann recovery) is replicable for non-saturation states under Route 1.

### OPEN (load-bearing for load-bearing #3):

- **Substrate-side stress-energy for non-saturation states** — derivable via Noether on $S_{\mathrm{sub}}$ for non-constant $\Psi$ content. Substantively similar to M3 chain Step B + C but for non-uniform substrate states. Plausibly closes at D-via-I via Route 1. **OPEN-HM-1.**
- **DCGT translation of non-uniform substrate stress-energy to continuum stress-energy with appropriate equation of state** ($w = 1/3$ for radiation, $w = 0$ for matter, etc.). Plausibly closes at D-via-I via Route 4. **OPEN-HM-2.**
- **Substrate-graph derivation of saddle-Hessian boundary motion** (Route 2). Substrate-research-frontier; ED-specific substrate-graph content. **OPEN-HM-3.**
- **Substrate-graph derivation of horizon area-entropy law** (Route 5). Specialized to thermodynamic-horizon content. **OPEN-HM-4.**

### Cross-arc dependencies:

- Route 1 + 4 closure would enable Paper_ED_Dyn_02 (Horizon-Motion-Law paper) at M3 form-IDENTIFIED with non-load-bearing OPEN items remaining.
- Closure also propagates to Paper_ED_Cos_05 (Dark energy) — late-universe horizon dynamics in $\Lambda$-dominated regime.
- Closure propagates to Paper_ED_Dyn_04 (Gravitational collapse) — collapse-side horizon dynamics analog to inflation-side expansion-dominant-axis runaway.

### Cross-arc note:

The M3 chain pattern (substrate-side Noether + DCGT + Friedmann recovery) appears to be a **general substrate-research closure template** applicable across cosmology arc problems. Load-bearing #3 likely closes via the same template applied to non-saturation states. Load-bearing #5 (Λ smallness) likely also closes via the same template (Λ-dominated late universe substrate-side reading).

This template's robustness is itself a substantive substrate-ontology finding: **ED's substrate ontology supports standard cosmology phenomenology via DCGT + standard QFT/cosmology inheritance applied to substrate-side analogs.** The chirality-cascade negative finding (substrate is chirality-symmetric, can't supply chain-typing $\mathbb{Z}_2$) and the M3-chain positive finding (substrate supports exponential growth via DCGT vacuum-energy translation) are complementary characterizations.

---

## §7 Recommended next steps

The load-bearing #3 closure most cleanly proceeds via Route 1 + 4, parallel to the M3 chain pattern.

**Three honest paths:**

**Path-HM-1 (attempt Route 1 — substrate-side stress-energy for non-saturation states).** Focused construction memo deriving Noether stress-energy from $S_{\mathrm{sub}}$ for non-constant $\Psi$ content. Substrate-side $T^{\mu\nu}_{\mathrm{sub}}$ for radiation-dominated, matter-dominated regimes. **Most-tractable starting point.**

**Path-HM-2 (attempt Route 4 — DCGT translation + Friedmann inheritance).** Conditional on Path-HM-1 closure. Focused construction memo establishing that DCGT translates non-uniform substrate stress-energy to continuum stress-energy with appropriate equation of state, and that standard Friedmann equations + horizon evolution inherit cleanly.

**Path-HM-3 (attempt Route 2 — saddle-Hessian boundary dynamics).** Substantively distinct substrate-graph derivation. ED-specific content; potentially valuable beyond standard cosmology horizon-motion. Lower priority than Path-HM-1 + 2 for closure of load-bearing #3 itself.

**My recommendation:** **Path-HM-1 first** — most-tractable; uses M3-chain template; foundational for Path-HM-2. If Path-HM-1 + Path-HM-2 close (likely via the M3 chain pattern), load-bearing #3 reaches D-via-I; Paper_ED_Dyn_02 becomes draftable at M3 form-IDENTIFIED.

**Cross-load-bearing pattern note:** if the M3-chain template (substrate-side Noether + DCGT + Friedmann) closes load-bearing #3 via Route 1 + 4, the same template likely closes load-bearing #5 (Λ smallness) for late-universe $\Lambda$-dominated regime. Load-bearing #3 + #5 may close together via the same substrate-research template.

**Path-HM-3 (saddle-Hessian)** can be pursued in parallel as substrate-research-frontier work supplying ED-specific horizon-motion content beyond standard cosmology inheritance. This would advance the dynamics arc (Paper_ED_GW_00 + Paper_ED_Dyn_01 saddle dynamics) substantively.

**Comparison with chirality cascade vs M3 chain outcomes:**

| Arc | Substrate-research pattern | Result |
|---|---|---|
| Chirality cascade | Specialized substrate-graph machinery required; not available | Negative — all closure attempts rejected |
| **M3 chain (load-bearing #1)** | **Standard QFT/cosmology template via DCGT** | **Positive — closes at D-via-I via standard inheritance** |
| **Horizon-motion (load-bearing #3)** | **Likely standard cosmology template via DCGT** | **Plausibility HIGH for closure via M3-chain template** |
| Load-bearing #5 (Λ smallness) | Likely same M3-chain template applied to Λ-dominated regime | Likely plausibility HIGH (TBD via focused work) |

The substrate-research pattern is emerging: **load-bearing OPEN items that follow standard QFT/cosmology templates close via DCGT inheritance** (loads #1, #3 probably, #5 probably); **load-bearing OPEN items requiring specialized substrate-graph machinery beyond existing primitives don't close** (load #2 chirality $\mathbb{Z}_2$).

---

**End Memo_ED_HorizonMotion_Scoping.**
