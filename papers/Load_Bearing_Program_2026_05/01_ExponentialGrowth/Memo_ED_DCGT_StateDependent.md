# Memo_ED_DCGT_StateDependent — Construction Memo (Path-α Attempt)

**Series:** Wave-3 Construction Memo (Cosmology Arc; inflation sub-thread; Path-α from Memo_ED_ExponentialGrowth_Scoping)
**Status:** Substrate-graph attempt to derive exponential scale-growth $\dot a \propto a$ via DCGT (Paper_073) extension to saturation-regime behavior, after Path-β (Memo_ED_V1BoundaryExpansion) yielded a clean negative result on V1-structural mechanisms. **Not a derivation. No new primitives.** Outcome: **structurally promising route identified (M3 — DCGT-induced de-Sitter-like continuum geometry in saturation regime) with two load-bearing substrate-graph OPEN items.** The route does not require V1 to exceed substrate-c; exponential growth emerges via continuum-side metric structure DCGT produces, analogous to standard cosmology's de Sitter mechanism.
**Date:** 2026-05-16
**Anchors:** Paper_073 (DCGT, A→regime hydrodynamic-window); Paper_ED_Cos_01 (Inflation, row 13 OPEN); Memo_ED_ExponentialGrowth_Scoping; Memo_ED_V1BoundaryExpansion (Path-β negative); Paper_089 (V1); Paper_012 (P-RB-1); Paper_ED_SC_4_9 (substrate-action saddle Hessian); Paper_ED_CCC §3.7.

---

## §1 DCGT standard regime

Per Paper_073 (and ED_MEMORY anchor): DCGT is the substrate→continuum bridge for the ED corpus. It operates in the **hydrodynamic-window A→regime** scale-separation $\ell_{ED} \ll R_{cg} \ll L_{flow}$. Within this regime:

- $\Gamma_{\mathrm{diff}}$ (substrate-side diffusion rate) is approximately substrate-parameter-determined; bounded by substrate-c per Paper_012 P-RB-1.
- Effective $\ell_{V_1}$ is substrate-parameter-determined; not state-dependent in standard formulation.
- DCGT produces continuum-side equations of diffusion-form, propagator-form, constitutive-law-form. The substrate-side coefficients are INHERITED at empirical-matching level.

**Critical regime caveat (ED_MEMORY):** "DCGT is regime-conditional. It applies in the hydrodynamic-window scale separation. Outside this window (strong-gradient regimes, near-substrate-scale physics, near-singularity regimes), DCGT breaks down."

The post-SCBU saturation regime per Paper_ED_Cos_01 §3.4 has substrate event-density near maximum, $\Gamma_{\mathrm{diff}} \gtrsim \Gamma_{\mathrm{prod}}$, unbalanced saddle-Hessian content. **This regime is structurally close to the strong-gradient / near-substrate-scale boundary of DCGT's hydrodynamic window.** Saturation-regime DCGT may require extension beyond the standard formulation.

---

## §2 Three candidate substrate-graph routes

**M1 — Capacity-state-dependent $\Gamma_{\mathrm{diff}}$.** Could substrate event-density scaling cause $\Gamma_{\mathrm{diff}}$ to grow with substrate content?

Examination: $\Gamma_{\mathrm{diff}}$ is the *rate* of diffusion per substrate-graph state, not the *amount* diffused. Substrate event-density affects the *amount* of substrate content available to diffuse; the rate is set by V1 + V5 kernel finite-width parameters per Paper_073. **Capacity-state-dependence of $\Gamma_{\mathrm{diff}}$ would require V1 / V5 finite-width parameters to scale with substrate event-density**, which contradicts Paper_089's fixed-width V1.

Status: **negative.** Reduces to M2 (state-dependent $\ell_{V_1}$).

**M2 — State-dependent effective $\ell_{V_1}$.** Could DCGT produce an *effective* $\ell_{V_1,\mathrm{eff}}$ that scales with substrate state, even if substrate-level $\ell_{V_1}$ is fixed?

Examination: DCGT's coarse-graining can produce effective continuum parameters that differ from substrate-level parameters. In the saturation regime, the effective coarse-graining might produce $\ell_{V_1,\mathrm{eff}}$ scaling with substrate event-density. This is substrate-research-frontier; not currently derived in Paper_073's standard formulation.

Status: **potentially derivable; substrate-research-frontier.** Requires DCGT extension. Path-α candidate with medium-low confidence.

**M3 — DCGT-induced de-Sitter-like continuum geometry in saturation regime.** Could DCGT in saturation produce continuum-side metric structure (positive cosmological-constant-like curvature) that supports exponential scale-growth via the standard cosmology mechanism — even when substrate-graph propagation is at most substrate-c-bounded?

Examination: this is the substrate-graph analog of standard cosmology's de Sitter exponential expansion. In GR, de Sitter ($\Lambda$-dominated FRW) has $H = \sqrt{\Lambda/3}$ constant and $a(t) \propto e^{Ht}$, with local light-speed bounded by $c$. **Exponential growth emerges from the metric structure (positive cosmological-constant content), not from super-luminal propagation.**

Substrate-graph translation: if DCGT in the saturation regime produces a continuum-side effective metric with positive cosmological-constant-like curvature, GR Friedmann equations (which DCGT recovers at the continuum-side hydrodynamic-window limit) give $H = $ constant → $a(t) \propto e^{Ht}$.

The substrate-c bound is preserved at substrate-graph level; the exponential growth is a continuum-side coarse-grained-metric effect.

Status: **structurally the cleanest substrate-graph route**, leveraging the standard mechanism by which bounded local propagation produces exponential scale-growth in standard cosmology.

---

## §3 M3 in detail — the substrate-graph chain

**Step A:** In saturation regime ($\Gamma_{\mathrm{diff}} > \Gamma_{\mathrm{prod}}$), expansion-dominant Hessian axes (Paper_ED_SC_4_9) are sustained by diffusion-driven redistribution while compression-dominant axes are depleted (per Paper_ED_Cos_01 §3.3).

**Step B:** Under sustained expansion-dominant axis content, the substrate-action $S_{\mathrm{sub}}[\Psi]$ per unit substrate-graph volume is **effectively constant** across the saturation region. The diffusion redistributes content but the volumetric density is preserved by the diffusion–production balance at the saturation level.

**Step C:** DCGT coarse-graining translates this substrate-graph state to a continuum-side stress-energy tensor. Constant volumetric substrate-action density → constant volumetric continuum-side "vacuum-energy-like" energy density $\rho_{\mathrm{eff}}$. (This is the substrate-graph analog of the vacuum-energy hypothesis in standard inflation; substrate-side it emerges from the saturation-regime balance rather than from a postulated scalar field.)

**Step D:** Friedmann recovery from DCGT continuum bridge in the hydrodynamic-window limit gives, for constant $\rho_{\mathrm{eff}}$:
$$
H^2 = \frac{8\pi G_{\mathrm{eff}}}{3} \rho_{\mathrm{eff}} = \mathrm{constant}
$$
where $G_{\mathrm{eff}}$ is the continuum-side gravitational coupling DCGT produces (related to Paper_027 Newton's $G$).

**Step E:** $H$ constant → $a(t) = a_0 e^{Ht}$ → **exponential scale-growth.** This is the standard de-Sitter-like result.

**No substrate-c violation:** local substrate-graph propagation remains substrate-c-bounded throughout. The exponential growth is a continuum-side metric effect arising from the positive-vacuum-energy-like content produced by DCGT translating the saturation-regime substrate state.

**Structural parallel:** in GR de Sitter, $c$ is the local light-speed bound but $a(t) \sim e^{Ht}$ — exponential global growth with bounded local propagation. ED-side same pattern: substrate-c is the substrate-graph propagation bound, but DCGT-induced continuum-side de-Sitter geometry gives exponential scale-growth.

This is the cleanest substrate-graph mechanism the corpus admits for exponential growth.

---

## §4 Load-bearing OPEN items for M3 closure

**OPEN-1 (Step B):** Substrate-graph derivation that the saturation regime produces effectively constant $S_{\mathrm{sub}}[\Psi]$ density across the unbalanced region. Plausible from Paper_ED_Cos_01 §3.3 (diffusion–production balance maintains expansion-dominant axes), but the derivation that this gives volumetric-constant substrate-action density is not constructed. Requires examining Paper_ED_SC_4_9 saddle-Hessian dynamics + Paper_073 DCGT relationship in detail.

**OPEN-2 (Step C, applicability):** Substrate-graph derivation that DCGT applies (or admits clean extension) to the saturation regime, given that the saturation regime is structurally close to DCGT's hydrodynamic-window boundary. Per Paper_073 + ED_MEMORY anchor, DCGT is regime-conditional; outside hydrodynamic-window it "breaks down." Saturation regime may be:
- (i) Within DCGT's regime of applicability after all — saturation is not strong-gradient in the sense Paper_073 excludes
- (ii) A natural extension regime — DCGT admits an obvious saturation-regime extension preserving the substrate-to-continuum translation
- (iii) Outside DCGT's regime — DCGT breaks down in saturation; alternative substrate-graph bridge required

Determining which of (i), (ii), (iii) holds is substrate-research-frontier work on DCGT itself.

**OPEN-3 (Step C, translation):** Substrate-graph derivation that DCGT translates constant substrate-action density to continuum-side vacuum-energy-like stress-energy. This is the structural translation step. Standard DCGT supplies the *form* of continuum equations; whether the substrate-action density translates cleanly to vacuum-energy content is a translation-specific question worth examining.

**OPEN-4 (quantitative consolidation):** If OPEN-1 through OPEN-3 close, the GR-side Hubble parameter $H$ acquires a substrate-graph identification via $H = \sqrt{8\pi G_{\mathrm{eff}} \rho_{\mathrm{eff}} / 3}$ where $\rho_{\mathrm{eff}}$ is the DCGT-translated saturation-regime substrate-action density. Quantitative substrate-graph derivation of $H$ value would supply the inflation-fluctuation spectrum quantitative content (Paper_ED_Cos_01 row 12 OPEN; INHERITED from Planck CMB at present).

---

## §5 IDENTIFIED vs OPEN

### IDENTIFIED:

- **DCGT is regime-conditional;** standard formulation applies in hydrodynamic window. Saturation regime is at the boundary of (or potentially outside) this window.
- **M1 (capacity-state-dependent $\Gamma_{\mathrm{diff}}$) reduces to M2** (state-dependent $\ell_{V_1}$), which requires DCGT extension not in current corpus.
- **M3 (DCGT-induced de-Sitter-like continuum geometry) is structurally the cleanest closure path** for exponential growth. It uses the standard cosmology mechanism (bounded local propagation, exponential global scale-growth via positive-vacuum-energy continuum metric) translated to substrate-side via DCGT.
- **The substrate-c bound is preserved** at substrate-graph level under M3; exponential growth is a continuum-side metric effect from DCGT's translation of saturation-regime substrate state.

### OPEN (load-bearing for M3 closure):

- **OPEN-1:** Substrate-graph derivation of constant $S_{\mathrm{sub}}$ density in saturation regime. Requires Paper_ED_SC_4_9 + Paper_073 detailed examination.
- **OPEN-2:** Substrate-graph derivation of DCGT applicability/extension to saturation regime. Three sub-cases (i)/(ii)/(iii); determining which requires DCGT-frontier work.
- **OPEN-3:** Substrate-graph derivation that DCGT translates constant substrate-action density to vacuum-energy-like continuum stress-energy. Translation-specific.
- **OPEN-4:** Quantitative substrate-graph derivation of $H$ value. Conditional on OPEN-1, OPEN-2, OPEN-3 closure.

### Cross-arc impact:

- If M3 closes, it has **major cross-arc impact** — DCGT is upstream of every continuum-level corpus result. Saturation-regime DCGT extension would propagate to Paper_073 itself + every paper using DCGT inheritance (Paper_027 Newton's G, Paper_047 Hawking spectrum, Paper_039 horizon decoupling, plus inflation arc, plus dynamics arc).
- If M3 fails, **Path-γ remains** (accept linear, reframe Paper_ED_Cos_01 to lean entirely on SCBU inheritance for horizon resolution). Verdict stays M2 with row 13 reframed as fundamental substrate-graph limitation rather than derivation gap.

---

## §6 Recommended next steps

**M3 is the structurally cleanest substrate-graph closure route identified across Path-β and Path-α attempts.** It uses standard-cosmology's de Sitter mechanism translated to substrate-side via DCGT, without requiring V1 to exceed substrate-c or requiring substrate-graph features not currently in the corpus.

**Three honest paths:**

**Path-α.1 (attempt OPEN-1):** Focused construction memo examining whether saturation-regime substrate-action density is effectively constant. Uses Paper_ED_SC_4_9 + Paper_ED_Cos_01 §3.3 content. **Most-tractable of the OPEN items.** Plausibility: medium-high; the diffusion–production balance in saturation should produce sustained-content, but the volumetric-density-constancy derivation needs to be done.

**Path-α.2 (attempt OPEN-2):** Focused construction memo examining whether DCGT applies in saturation regime — case (i), (ii), or (iii). Foundational for M3 closure. Plausibility: medium; requires substrate-graph-frontier DCGT work.

**Path-α.3 (proceed to substantive paper draft):** If Path-α.1 + Path-α.2 close substrate-graph-derivably, draft the substantive paper closing Paper_ED_Cos_01 row 13. Upgrade verdict M2 → M3 retroactively.

**My recommended next step:** **Path-α.1 first** (substrate-action density constancy). This is the most tractable of the four OPEN items and supplies the foundational step for M3. If Path-α.1 closes, Path-α.2 becomes the next attempt; if Path-α.1 fails, we have a substrate-graph negative result that's informative either way.

**Comparison with Path-β:**

| Path | Approach | Outcome |
|---|---|---|
| Path-β (V1BoundaryExpansion) | V1-structural mechanisms for super-linear boundary expansion | Clean negative; five candidates all fail |
| Path-α (this memo) | DCGT extension to saturation regime | **Promising route identified (M3); four OPEN items** |

Path-α gives the corpus a non-trivial substrate-graph closure candidate that Path-β did not. The substrate-research frontier is now well-defined: examine DCGT's behavior in the saturation regime, focusing on substrate-action density constancy first.

**Note on structural pattern:** the load-bearing #1 attack is producing a substrate-research-frontier characterization parallel to (but more promising than) the chirality cascade. Where chirality concluded "substrate is chirality-symmetric; closure requires ontology extension," exponential-growth may conclude "DCGT extension to saturation regime supplies de-Sitter-like continuum geometry; closure tractable within existing primitives via DCGT extension." If M3 closes, load-bearing #1 produces a positive substrate-graph closure — substantively meaningful for the corpus.

---

**End Memo_ED_DCGT_StateDependent.**
