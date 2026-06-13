# Memo_ED_RadiationLaw_Scoping — Scoping Memo for Load-Bearing Derivation #4

**Series:** Wave-3 Scoping Memo (Cosmology + Dynamics Arcs; load-bearing derivation #4 from Memo_ED_CosmologyAndDynamics_ResearchDirections §4)
**Status:** Substrate-graph scoping of whether the radiation law — ED-side analog of EM Larmor formula + GW quadrupole formula — can be derived from existing ED substrate content. Closure would unlock Paper_ED_Dyn_03 (proposed Radiation Law paper) + retroactively close Paper_ED_GW_00 audit row 12 (substrate-graph derivation of source-amplitude formula). **Not a derivation. No new primitives proposed.**
**Date:** 2026-05-16
**Anchors:** Paper_ED_Cos_01 (M3-upgraded; M3-chain template); Paper_ED_GW_00 (saddle-Hessian reconfiguration; row 12 OPEN for source amplitude); Paper_073 (DCGT); Paper_ED_SC_4_9 ($S_{\mathrm{sub}}$); Paper_089 (V1); Paper_090 (V5); Paper_032 (weak-field 1/r dilution); Paper_027 (Newton's $G$); Paper_015 (T17 gauge fields, for EM Larmor analog); seven exponential-growth memos (M3-template reference); Memo_ED_HorizonMotion_Scoping + NonSaturation memos (load-bearing #3 chain).
**Headline:** **Load-bearing #4 closure plausibility HIGH via M3-template.** Radiation is a standard hydrodynamic-flux phenomenon; DCGT handles fluxes naturally; substrate-side time-varying stress-energy → continuum radiation formulas inherit cleanly. **Expected to follow the load-bearings #1 and #3 closure pattern** — substrate-side Noether stress-energy with time-varying content → DCGT translation → standard EM/GR radiation formulas via Friedmann/Maxwell inheritance.

---

## §1 Standard physics radiation laws

**EM Larmor formula** for accelerated charge:
$$
P_{\mathrm{Larmor}} = \frac{q^2 a^2}{6\pi \epsilon_0 c^3}
$$
Power radiated $\propto$ (acceleration)². Dependencies: $q$ (charge), $a$ (acceleration), $c$ (light-speed), $\epsilon_0$ (vacuum permittivity).

**GW quadrupole formula** for time-varying mass-quadrupole:
$$
P_{\mathrm{GW}} = \frac{G}{5 c^5} \langle \dddot Q_{ij} \dddot Q^{ij} \rangle
$$
Power radiated $\propto$ (third time-derivative of mass-quadrupole)². Dependencies: $G$ (Newton's), $c$, $Q$ (mass-quadrupole tensor).

**Common structural pattern:** power radiated $\propto$ (time-derivative of multipole)² $\times$ coupling-constant / $c^n$. The dependence on time-derivatives reflects that radiation requires time-varying source content (accelerated charges; time-varying quadrupoles). Stationary sources don't radiate.

---

## §2 Candidate substrate-graph quantities for radiation emission

Four candidates for "what substrate-side quantity governs radiation emission":

**(α) V1 retarded propagation flux.** V1 carries substrate-side content forward at substrate-c. A time-varying source produces time-varying V1-propagated content outward. The radial flux of this content at large distance is the substrate-side radiation. **Direct parallel to standard Maxwell / linearized Einstein retarded-Green's-function radiation.**

**(β) V5 cross-chain coupling time-variation.** V5 supplies cross-chain correlations. Time-varying cross-chain coupling could produce radiative content via long-range correlations. Less direct than (α); V5's finite-memory may dampen radiative content.

**(γ) Saddle-Hessian eigenvalue time-evolution.** Per Paper_ED_GW_00, GW is identified as propagating saddle-Hessian reconfigurations. Time-varying Hessian content at a source produces propagating Hessian-pattern at the boundary → radiation. The source amplitude depends on the time-derivative magnitude of the source's Hessian content.

**(δ) DCGT coarse-grained stress-energy flux.** Substrate-side Noether $T^{\mu\nu}_{\mathrm{sub}}$ has flux components $T^{0i}_{\mathrm{sub}}$ representing energy transport. DCGT coarse-grains to continuum stress-energy flux $T^{0i}_{\mathrm{eff}}$. For time-varying sources, the continuum flux is the radiation power. **Direct parallel to standard hydrodynamics-from-microscopics.**

These overlap structurally — (α) (γ) (δ) are different views of the same substrate-side radiation mechanism: substrate-side time-varying content + retarded propagation + flux through coarse-grained continuum. (β) is more specialized.

---

## §3 M3-chain template applicability to radiation

The M3-template (closed for inflation, load-bearing #3 for non-saturation states) pattern:

1. Substrate-side $S_{\mathrm{sub}}[\Psi]$ has specific content for the regime
2. Substrate-side Noether procedure gives substrate stress-energy $T^{\mu\nu}_{\mathrm{sub}}$
3. DCGT translates to continuum $T^{\mu\nu}_{\mathrm{eff}}$
4. Standard physics formulas (Friedmann / Maxwell / Einstein) inherit cleanly

**For radiation:** the source is a time-varying substrate-side state (accelerated chain, time-varying multipole). Substrate-side Noether produces time-varying $T^{\mu\nu}_{\mathrm{sub}}$. DCGT translates to time-varying continuum $T^{\mu\nu}_{\mathrm{eff}}$. Standard Maxwell/Einstein retarded-Green's-function machinery gives the radiation formula.

**Plausibility:** very high. **Radiation is exactly the kind of phenomenon DCGT was built to handle** — hydrodynamic-window scale-separation; flux through coarse-grained continuum; standard physics inheritance for the source-to-far-field relationship.

**Cleaner than load-bearings #1 and #3 in some respects:**
- Load #1 required uniform-saturation closure (at edge of hydrodynamic window)
- Load #3 required non-saturation-regime closure (analog inheritance for chain-class identification)
- **Load #4 (radiation) sits cleanly within DCGT's regime** — source content + flux + standard retarded Green's function

**The Paper_ED_GW_00 audit row 12 ("substrate-graph derivation of source-amplitude formula — substrate analog of GR quadrupole") is exactly the load-bearing #4 closure target for GW.** Closing #4 closes Paper_ED_GW_00 row 12 retroactively.

---

## §4 Candidate closure routes

Five candidate routes:

**Route R1 — Noether stress-energy flux through DCGT (M3-template).**

Mechanism: substrate-side Noether $T^{\mu\nu}_{\mathrm{sub}}$ for time-varying $\Psi$ content. Flux components $T^{0i}_{\mathrm{sub}}$ represent substrate-side energy transport. DCGT coarse-grains to continuum stress-energy flux. For time-varying sources, the far-field flux gives the radiation power.

Plausibility: **HIGH.** Direct application of M3-template to time-varying substrate states. Standard hydrodynamics-from-microscopics analog.

Load-bearing requirement: substrate-side Noether for time-varying $\Psi$ + DCGT flux translation. Both follow established M3-template inheritance patterns.

**Route R2 — V1 retarded Green's function with substrate-side multipole expansion.**

Mechanism: V1's retarded kernel acts as substrate-side analog of standard retarded Green's function. Multipole expansion of substrate-side source content (V1+V5 supplying multipole-like decomposition) gives radiation amplitude via standard formulas.

Plausibility: **MEDIUM-HIGH.** V1 retarded structure (Paper_089) is structurally similar to standard retarded Green's function. Multipole expansion is standard mathematical machinery.

Load-bearing requirement: substrate-side identification of multipole moments + V1 retarded coupling. Likely closes via standard analog inheritance.

**Route R3 — Saddle-Hessian curvature-moment dynamics (Paper_ED_GW_00 framework).**

Mechanism: time-varying saddle-Hessian content at source produces propagating Hessian-pattern outward (per Paper_ED_GW_00 P-GW-SaddleReconfiguration). Source amplitude depends on time-derivative of Hessian content.

Plausibility: **MEDIUM-HIGH.** Direct extension of Paper_ED_GW_00 framework; closes row 12 of that paper specifically.

Load-bearing requirement: substrate-graph derivation of Hessian-reconfiguration source-amplitude formula in terms of substrate-side time-derivatives. Subset of Route R1.

**Route R4 — Standard EM/GR inheritance via DCGT continuum metric.**

Mechanism: once DCGT supplies continuum metric + continuum stress-energy, standard Maxwell (for EM radiation) and linearized Einstein (for GW radiation) machinery gives the radiation formulas directly.

Plausibility: **HIGH (conditional on Routes R1/R2 closing).**

Load-bearing requirement: standard physics inheritance through DCGT bridge.

**Route R5 — Specialized substrate-graph radiation mechanism beyond standard analog.**

Mechanism: substrate-side might supply radiation content not captured by standard EM/GR analog — e.g., specific to V5 cross-chain coupling structure, or to substrate-side discrete-event content.

Plausibility: **LOW** (most physical radiation phenomena are well-captured by standard EM/GR; substrate-side specialized mechanism beyond standard analog seems unlikely to be load-bearing).

Load-bearing requirement: substantive substrate-graph derivation of specialized radiation content. Substrate-research-frontier; not load-bearing for standard radiation phenomenology.

---

## §5 Load-bearing vs vocabulary-level

| Route | Mechanism | Plausibility | M3-template parallel? |
|---|---|---|---|
| **R1** (Noether flux through DCGT) | M3-template for time-varying states | **HIGH** | YES — direct parallel |
| **R2** (V1 retarded Green's + multipole) | Standard analog with substrate kernel | MEDIUM-HIGH | Partial parallel |
| **R3** (Hessian-moment dynamics) | Paper_ED_GW_00 framework extension | MEDIUM-HIGH | Subset of R1 |
| **R4** (EM/GR inheritance via DCGT) | Standard physics inheritance | HIGH conditional on R1/R2 | YES — standard inheritance |
| **R5** (Specialized substrate-graph) | Substrate-side specialized mechanism | LOW | NO — substrate-research-frontier |

**Net assessment:**

- **Routes R1 + R4 are the cleanest substrate-graph closure path** — direct parallel to M3-template for time-varying states. Plausibility HIGH.
- **Routes R2 + R3 are substantive but largely subsumed by R1 + R4** under standard hydrodynamic-window DCGT.
- **Route R5 is specialized** to substrate-research-frontier work beyond load-bearing #4 itself.

The substrate-research pattern: **load-bearing #4 likely closes via the same M3-template as #1 and #3, with even higher plausibility because radiation is exactly the hydrodynamic-flux phenomenon DCGT was built to handle.**

---

## §6 IDENTIFIED vs OPEN

### IDENTIFIED:

- **Standard radiation phenomenology** (Larmor + quadrupole formulas) is well-established at standard physics level.
- **Substrate-side V1 retarded propagation** (Paper_089) is structurally analogous to standard retarded Green's function machinery.
- **Substrate-side Noether stress-energy + DCGT flux translation** follows M3-template pattern for time-varying source states.
- **Paper_ED_GW_00 framework** (saddle-Hessian reconfigurations) already supplies the qualitative GW source mechanism; row 12 OPEN is exactly the load-bearing #4 target.
- **Route R1 closure plausibility HIGH** — substrate-research-frontier work expected to follow M3-template inheritance.

### OPEN (load-bearing for load-bearing #4 closure):

- **Substrate-side Noether stress-energy for time-varying $\Psi$ content** (Route R1 Step B-analog). Substrate-research-frontier; plausibly closes via standard QFT-analog inheritance applied to substrate-side Lagrangian.
- **DCGT flux translation for time-varying sources** (Route R1 Step C-analog). Standard hydrodynamics inheritance; plausibly closes.
- **Substrate-side multipole identification** (Routes R2, R3). Standard analog inheritance.
- **Quantitative coefficient derivation** (Larmor $q^2/6\pi\epsilon_0 c^3$; quadrupole $G/5c^5$). $G$ via Paper_027; $q$ via Paper_015 T17 + standard EM inheritance. Quantitative consolidation likely follows load-bearing #4 closure.

### Comparison with load-bearings #1 and #3

| # | Question type | M3-template applicability | Closure plausibility |
|---|---|---|---|
| 1 | Qualitative-structure (exponential growth?) | YES — direct (saturation regime) | CLOSED D-via-I (robust) |
| 3 | Qualitative-structure (phase-dependent horizon evolution?) | YES — applied to non-saturation states | CLOSED D-via-I (weaker, analog-inheritance) |
| **4** | **Qualitative-form (radiation from time-varying sources)** | **YES — direct (hydrodynamic-flux regime, DCGT's strength)** | **HIGH plausibility for closure via M3-template** |
| 5 | Quantitative-magnitude (why Λ small?) | NO directly; reduces to Route A | Conditional pending Route A |

**Load-bearing #4 is structurally similar to #1 and #3** — qualitative-form question handled cleanly by M3-template + DCGT inheritance. Plausibility may be even higher than #1 because radiation is sweet-spot DCGT territory (standard hydrodynamic flux phenomenon).

---

## §7 Recommended next steps

The load-bearing #4 closure most cleanly proceeds via Route R1 (Noether flux through DCGT), parallel to load-bearings #1 and #3.

**Three honest paths:**

**Path-R-1 (attempt Route R1 — Noether flux through DCGT for time-varying states).** Focused construction memo deriving substrate-side Noether stress-energy flux for time-varying $\Psi$ content + DCGT continuum translation. Uses M3-template directly applied to time-varying substrate states. **Most-tractable closure path.**

**Path-R-2 (proceed directly to draft Paper_ED_Dyn_03).** Given the closure plausibility is HIGH via Route R1, draft Paper_ED_Dyn_03 (Radiation Law paper) at M3 form-IDENTIFIED with explicit reference to Route R1 substrate-graph chain. Mirror Paper_ED_Cos_01 + Dyn_02 closure pattern.

**Path-R-3 (close Paper_ED_GW_00 row 12 directly).** Update Paper_ED_GW_00 to reflect row 12 closure via Route R1 substrate-graph chain. Maintains the consistency of GW paper with the M3-template program.

**My recommended next step:** **Path-R-1 first** (focused construction memo) — establishes the substrate-graph chain explicitly; supplies the substantive content for Path-R-2 + Path-R-3 follow-ups. Same discipline as load-bearings #1 and #3 (scoping → construction → audit → paper update).

If Path-R-1 closes with audit acceptance, **load-bearing #4 closes at D-via-I**, joining loads #1 and #3. The final load-bearing-program tally would be:

| # | Item | Status |
|---|---|---|
| 1 | Exponential growth | **CLOSED D-via-I (robust)** |
| 2 | Chirality $\mathbb{Z}_2$ | OPEN; substrate is chirality-symmetric |
| 3 | Horizon motion | **CLOSED D-via-I (weaker)** |
| **4** | **ED radiation law** | **CLOSED D-via-I (likely; pending construction + audit)** |
| 5 | Λ smallness | Conditional pending Route A |

**Three closed + one negative finding (#2) + one conditional on Route A (#5).** This would be substantively complete substrate-research closure of the load-bearing program, with **Route A as the single highest-leverage remaining open derivation** (per ED_MEMORY anchor 7 + this scoping's identification that load #5 reduces to Route A).

### Cross-arc note: the radiation law's reach

If load-bearing #4 closes via Route R1:
- **Paper_ED_GW_00 row 12** closes retroactively
- **Paper_ED_Dyn_03** (Radiation Law) becomes draftable at M3
- **Paper_ED_Dyn_05** (Inspiral dynamics) becomes draftable (depends on Dyn_01 + Dyn_03 per research-directions memo)
- **Paper_ED_GW_01** (BH ringdown spectroscopy) gains substantive radiation-amplitude content

**Cross-arc impact: substantial.** Closing load-bearing #4 advances both the Dynamics Arc and the GW sub-arc significantly.

### Substrate-research-pattern consolidation

The M3-template pattern is now **demonstrated to handle**:
- Load #1 (exponential growth, saturation regime) — robust closure
- Load #3 (horizon motion, non-saturation regimes) — weaker closure with analog-inheritance qualifications
- Load #4 (radiation law, hydrodynamic-flux regime) — expected closure with HIGH plausibility (this scoping)

And **doesn't directly handle**:
- Load #2 (chirality $\mathbb{Z}_2$) — requires specialized substrate-graph machinery; negative
- Load #5 (Λ smallness, quantitative magnitude) — reduces to Route A; not a qualitative-form question

The substrate-research-frontier characterization continues to robustly support: **ED's substrate ontology supports standard cosmology + radiation phenomenology via DCGT + standard QFT/cosmology inheritance, with substrate-research-frontier limits at (i) specialized substrate-graph derivations beyond standard physics inheritance (chirality), and (ii) quantitative-magnitude items requiring Route A closure (Λ smallness).**

---

**End Memo_ED_RadiationLaw_Scoping.**
