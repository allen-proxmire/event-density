# ED-SC 4.x Roadmap

**Date:** 2026-05-14
**Source:** Round 3 Phase B.3 deliverable
**Anchor paper:** Paper_SCBU (Substrate-Cosmology Boundary Unification)
**Methodology:** Paper_095 form-FORCED / value-INHERITED + three-tier verdict classification (M1/M2/M3)

---

## 1. Goal

ED-SC 4.x extends the ED-SC 3.x cross-scale invariance framework (Paper_096) using the unified substrate-cosmology boundary structure established in Paper_SCBU. The 3.x arc established cross-scale invariance within the wedges-arc/kernel-hierarchy at one canonical operating point (ξ_canonical = 1.7575 lu). The 4.x arc generalizes this to **multiple scale anchors across multiple arcs**, all of which inherit jointly from the substrate-cosmology boundary at $R_H = c/H_0$.

The roadmap defines how the unified boundary propagates into four downstream arcs and the new invariance structure, kernel-cascade integration, RG-regime alignment, and cross-arc falsifier propagation that ED-SC 4.x delivers.

---

## 2. Cross-Arc Propagation of the Unified Boundary

Paper_SCBU establishes that the substrate-cosmology boundary $R_H = c/H_0$ underlies two canon-internal scale anchors:
- **MOND:** $a_0 = cH_0/(2\pi)$ via dipole-projection (Paper_029).
- **ED-SC:** $\xi_{canonical} = 1.7575$ lu via cross-scale-invariance fixed-point (Paper_096).

ED-SC 4.x extends this propagation into four additional arc-anchor pairings, each of which is currently flagged as F4 in the SCBU paper's falsification criteria. The structural claim is that the same boundary $R_H$ supplies cross-arc anchoring for all of them. Numerical and mechanism-distinct projections vary; the substrate-cosmology origin is common.

### 2.1 BH horizon scale (Paper_039)

**Object:** BH horizon radius $r_H = 2GM/c^2$.
**Current status:** Anchored to local mass-energy content via standard GR; substrate-mechanism is decoupling-surface structure (Paper_039) where $\Gamma_{cross} \to 0$.
**Connection to $R_H$:** Both are decoupling surfaces — the BH horizon at finite $M$, the cosmic decoupling surface at cosmic-scale-mass-content. The decoupling-surface mechanism is shared (Paper_062 already echoes this for BH ↔ Q-COMPUTE via shared V5). ED-SC 4.x claim: $r_H$ and $R_H$ are two instantiations of substrate decoupling-surface formation at different mass-content scales.
**4.x extension paper:** A new paper formalizing the cross-mass-scale decoupling-surface continuum, with $r_H$ as local-mass limit and $R_H$ as cosmic-scale-mass limit.

### 2.2 MOND/galactic scale (Papers 029–034)

**Object:** $a_0$ + ED Combination Rule (Paper_030) + BTFR slope-4 (Paper_031, T21) + Deep-MOND limit (Paper_034).
**Current status:** Already substrate-anchored to $R_H = c/H_0$ via Paper_029 dipole-projection mechanism; Paper_SCBU establishes shared origin with $\xi_{canonical}$.
**Connection to $R_H$:** Direct via Paper_029. Paper_SCBU formalizes joint inheritance with the wedges arc's $\xi_{canonical}$.
**4.x extension paper:** Likely already saturated by Paper_SCBU and T20; further extension would be substrate-derivation of $\xi_{canonical}(H_0)$ from primitives, closing OPEN step 12 of Paper_SCBU and upgrading SCBU to M2.

### 2.3 Q-Compute platform scale (Paper_060)

**Object:** $\mathcal{M}_{crit}$ threshold and 140–250 kDa Class A matter-wave wall (Paper_056).
**Current status:** Cross-platform-universal substrate threshold (Paper_060 P-Mcrit-Unified, P-Cross-Platform-Universality); no current connection to $R_H$.
**Connection to $R_H$:** Conjectural at present. The Class A wall reflects substrate bandwidth saturation (P04 + V5 cross-chain budget under DCGT). Whether the saturation threshold inherits from substrate-cosmology content (via the cosmic decoupling surface bounding effective substrate cell-count globally) is OPEN. ED-SC 4.x claim: $\mathcal{M}_{crit}$ inherits an indirect bound from $R_H$ via global substrate-cell-count constraints.
**4.x extension paper:** A new paper exploring whether the cross-platform $\mathcal{M}_{crit}$ value is structurally constrained by substrate-cosmology global participation-count bounds. This is M3 at write-time; M2 if the substrate-derivation closes.

### 2.4 Soft-matter hydrodynamic scale (Paper_086, Paper_080)

**Object:** NS-Q canonical operating point Q ≈ 3.5 at canonical ξ (Paper_080); hydrodynamic-window $L_{flow}$ (Paper_076).
**Current status:** Anchored to canon-internal NS-Q saturation; no current connection to $R_H$ explicitly.
**Connection to $R_H$:** The hydrodynamic window has upper-scale cutoff $L_{flow}$ which in principle could be bounded by the substrate-cosmology boundary, but the relationship is several scales removed. ED-SC 4.x claim: $L_{flow}$ is bounded above by $R_H$ in principle, though numerical reach of this bound is empirically negligible.
**4.x extension paper:** Lower priority — the substrate-cosmology boundary is far above $L_{flow}$ at any realistic platform, so this connection is structural-only rather than empirically active. Likely a single brief audit paper.

---

## 3. New Invariance Structure

ED-SC 4.x introduces a **two-tier invariance structure** beyond Paper_096's S1/S2 split:

- **Tier-α — Substrate-cosmology invariance.** Quantities anchored jointly to $R_H = c/H_0$ scale jointly under $H_0$ variation. Currently: $a_0$ + $\xi_{canonical}$ (Paper_SCBU); extended in 4.x to $r_H$, $\mathcal{M}_{crit}$ (conjecturally), $L_{flow}$ (structurally).
- **Tier-β — Cross-scale (kernel-hierarchy) invariance.** Already established in Paper_096: substrate-level S1 kernel-content is invariant under scale rescaling within the kernel-hierarchy regime.

Tier-α is **inherited from substrate-cosmology**; Tier-β is **inherited from kernel-hierarchy**. The two tiers are complementary, not hierarchical: Tier-α anchors scales globally to the cosmological boundary; Tier-β fixes the substrate behavior within local scale-regimes.

**Combined invariance group (proposed for 4.x):**
- Substrate-cosmology rescaling (Tier-α): $H_0 \to H_0'$ jointly rescales all $R_H$-anchored quantities.
- Cross-scale rescaling (Tier-β): substrate ξ rescaling preserves S1 kernel-content within the hydrodynamic-window-extended regime.

The two tiers are jointly active under combined rescaling.

---

## 4. Kernel-Cascade Integration

Paper_091 establishes the V1/V5 memory-kernel cascade across scales. ED-SC 4.x integrates the substrate-cosmology boundary into the cascade endpoint:

- **UV endpoint:** $\ell_{V1}$ ≈ $\ell_P$ (Planck scale).
- **Transition regime:** $\ell_{V5}$ at canon-internal scale; transition-regime characterized by 0.6 exponent (Paper_097).
- **IR endpoint:** $R_H = c/H_0$ (substrate-cosmology boundary). **[NEW IN 4.x]**

Currently Paper_091 + Paper_097 describe the cascade with implicit far-IR endpoint at $L_{flow}$ (hydrodynamic-window upper scale). The ED-SC 4.x extension claims that the **true substrate-level far-IR endpoint is $R_H$**, not $L_{flow}$ — $L_{flow}$ is the hydrodynamic-window-specific cutoff for the soft-matter arc, but at substrate level the cascade continues up to the cosmic decoupling surface.

This implies a four-regime extended RG flow:
1. UV regime ($R \lesssim \ell_{V1}$): V1-dominated.
2. Transition regime ($R \sim \ell_{V5}$): V1+V5 cascade with 0.6 exponent (Paper_097).
3. IR regime ($R \gtrsim \ell_{V5}$): V5-dominated.
4. **Cosmological regime ($R \sim R_H$): boundary-saturated.** [NEW IN 4.x]

Beyond $R_H$, cross-locus substrate influence does not reach coherently (Paper_028); the kernel cascade has no operational meaning there.

---

## 5. RG-Regime Alignment Across Arcs

The four-regime extended RG flow aligns the cross-arc scale-regimes as follows:

| Scale regime | Range | Arcs operating here | Anchored scales |
|---|---|---|---|
| UV | $R \lesssim \ell_P$ | QFT regularization, BH substrate interior (Paper_042) | $\ell_P$ |
| Transition | $\ell_{V1} \ll R \ll \ell_{V5}$ | Substrate kernel cascade transition | 0.6 exponent (Paper_097) |
| IR (hydrodynamic-window) | $\ell_{V5} \ll R \ll L_{flow}$ | NS, MHD, Soft-matter, Q-COMPUTE platforms | $L_{flow}$; $\mathcal{M}_{crit}$; Q ≈ 3.5; $\xi_{canonical}$ |
| Cosmological | $R \sim R_H$ | MOND/a₀, ED-SC, BH horizon | $a_0$; $R_H$; $r_H$ |

**ED-SC 4.x claim:** The four-regime partition is globally consistent across all arcs. Within each regime, distinct canon-internal scales apply; across regimes, the substrate-cosmology boundary at $R_H$ provides the global anchor. This is the unified RG-regime alignment delivered by 4.x.

---

## 6. Cross-Arc Falsifier Propagation

Under ED-SC 4.x, falsification of substrate-cosmology boundary structure propagates across all four extension arcs simultaneously:

| Falsifier | Refutes | Propagates to |
|---|---|---|
| $a_0 \ne cH_0/(2\pi)$ (Paper_029 F1) | MOND projection | $\xi_{canonical}$ joint scaling; $\mathcal{M}_{crit}$ conjectural anchor; BH-horizon decoupling-shared-mechanism |
| Independent $\xi_{canonical}$ derivation without $H_0$ (Paper_SCBU F2) | Joint-inheritance claim | All four 4.x extension arcs lose substrate-cosmology bridge |
| $r_H$ not a decoupling surface in same sense as $R_H$ | BH ↔ ED-SC bridge | 4.x BH extension paper fails |
| $\mathcal{M}_{crit}$ independent of substrate-cosmology | Q-Compute bridge | 4.x Q-Compute extension paper fails |
| Hubble-tension resolution moves $H_0$ and $a_0$ does not co-vary | Joint scaling | Paper_SCBU F1; ED-SC 4.x globally |

The cross-arc falsifier propagation is the methodological strength of ED-SC 4.x: a single empirical refutation at the substrate-cosmology boundary level cascades into refutation of cross-arc claims simultaneously. This is high-leverage falsifiability — a small number of empirical observations probe a large number of substrate claims.

---

## 7. Recommended Paper Sequence for ED-SC 4.x

Suggested order, lowest effort + highest impact first:

1. **Paper ED-SC-4.1 — BH Horizon ↔ Cosmic Decoupling Surface.** Extends the decoupling-surface framework (Paper_039 + Paper_062) to claim shared substrate mechanism with $R_H$. ~2,500 words. Verdict tier M3.

2. **Paper ED-SC-4.2 — $\xi_{canonical}(H_0)$ substrate-derivation.** Closes OPEN step 12 of Paper_SCBU; upgrades SCBU from M3 to M2. Requires deriving the canon-internal value 1.7575 lu from $H_0$ via the kernel-hierarchy cross-scale-invariance fixed-point analogous to Paper_029's $a_0$ derivation. ~3,500 words. Highest leverage if it closes.

3. **Paper ED-SC-4.3 — $\mathcal{M}_{crit}$ Substrate-Cosmology Anchor.** Tests whether cross-platform $\mathcal{M}_{crit}$ value is structurally constrained by global substrate-cell-count bound at $R_H$. ~3,000 words. Verdict tier M3 at write-time.

4. **Paper ED-SC-4.4 — Four-Regime Extended RG Flow.** Formalizes the cosmological-regime extension of Paper_097's three-regime RG. ~2,500 words. Verdict tier M3.

5. **Paper ED-SC-4.5 — Hydrodynamic-window Cosmological Bound.** Audits whether $L_{flow}$ is bounded by $R_H$ at substrate level. Lower priority; mostly structural verification. ~1,500 words. Verdict tier M3.

6. **Paper ED-SC-4.6 — ED-SC 4.x Capstone.** Synthesizes the five extension papers. Follows Paper_086 / Paper_100 capstone template. ~3,500 words. Verdict tier M3 (synthesis-only, no new postulates).

Total: 6 papers, ~16,500 words. Estimated effort: 2–3 weeks of focused drafting.

---

## 8. Phase B.4 — Registry Implications

After SCBU + B.1 edits are reflected in registries, expect:

- **Postulate registry:** +1 entry (P-Substrate-Cosmology-Unified, source: Paper_SCBU); total 125.
- **Numerical-value registry:** No new anchors at write-time; existing $a_0$ and $\xi_{canonical}$ now have cross-cited shared origin.
- **Theorem inventory:** No change.
- **Citation graph:**
  - New top-level Paper_SCBU entry with upstream = [028, 029, 037, 062, 071, 091, 095, 096, 097] and downstream = [] (initially orphan, expected to gain ED-SC 4.x citers).
  - Downstream-list updates for Papers 028, 029, 037, 091, 096, 097 to include SCBU as new citer.
  - Paper_028 may enter top-10 most-cited (currently around #15; SCBU's load-bearing citation could push it up).
  - Paper_097 downstream gains 1 (now [Paper_098, Paper_100, Paper_101, Paper_SCBU]).

The Paper_SCBU orphan status at write-time is **by-design** (synthesis paper just produced); it will be cited by ED-SC 4.x extension papers as they are drafted.

---

**End ED-SC 4.x Roadmap.**
