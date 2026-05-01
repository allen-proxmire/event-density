# Future Arc — P4 Mobility Saturation → Non-Newtonian Fluid Mechanics (Scoping)

**Date:** 2026-04-30
**Status:** Active scoping memo. Strongest productive route identified in the off-leash ED-NS exploration. Memo-ready immediately; full arc closure estimated 3–5 sessions.
**Companions:** [`ED-NS_Exploration_Roadmap.md`](ED-NS_Exploration_Roadmap.md) (route #4), [`../Architectural_Canon.md`](../Architectural_Canon.md) (P4), [`../PDE.md`](../PDE.md) §4.1 (Universal Mobility Law), [`NS-2.08_ED-PDE_Direct_Mapping.md`](NS-2.08_ED-PDE_Direct_Mapping.md) (mobility → viscosity mapping at vector-extension level).

---

## 1. Purpose

This arc investigates how the architectural canon's **P4 mobility-saturation principle** ($M(\rho_\mathrm{max}) = 0$ with $M(\rho) > 0$ for $\rho < \rho_\mathrm{max}$) — already empirically validated for soft matter via the Universal Mobility Law (PDE.md §4.1, R² > 0.986 across 10 chemically distinct systems) — extends to fluid mechanics to produce a structural derivation of:

- **Shear-thickening** (viscosity rising with shear rate or density),
- **Jamming** (viscosity diverging at packing threshold),
- **Krieger-Dougherty-class viscosity divergence** $\mu(\rho) = \mu_0 (1 - \rho/\rho_\mathrm{max})^{-\beta}$ near close-packing,
- And related non-Newtonian fluid behaviors.

This is the strongest productive route discovered in the off-leash ED-NS exploration ([ED-NS_Exploration_Roadmap.md](ED-NS_Exploration_Roadmap.md) §3 category A). Among all 13 catalogued routes, it is the only one that:

1. **Already has empirical anchoring** — Universal Mobility Law's 10-system validation gives the structural form an experimental footing.
2. **Delivers a form-FORCED prediction** — Krieger-Dougherty-class divergence with structurally-derived functional form (β value INHERITED).
3. **Extends ED's empirical reach** — moves ED from soft-matter-mobility-validated to fluid-mechanical-rheology-derived; broadens the program's empirical footprint.

The arc is not Clay-NS-relevant (smoothness obstruction lies in the advective term per NS-3.02b + NS-2.08); it is "ED on Earth" empirical territory — non-Newtonian rheology is one of the most data-rich applied branches of fluid mechanics, with extensive industrial and biomedical datasets to compare against.

---

## 2. Inputs

| Input | Source |
|---|---|
| P4 (mobility saturation): $M(\rho_\mathrm{max}) = 0$ | [`Architectural_Canon.md`](../Architectural_Canon.md) §2 |
| Universal Mobility Law $D(c) = D_0 (1 - c/c_\mathrm{max})^\beta$ | [`PDE.md`](../PDE.md) §4.1; `papers/Universal_Mobility_Law/` |
| 10-system empirical validation R² > 0.986 | Same |
| Mobility → viscosity mapping at vector-extension level | [`NS-2.08_ED-PDE_Direct_Mapping.md`](NS-2.08_ED-PDE_Direct_Mapping.md) §4.1 |
| Roadmap #4 priority and structural finding | [`ED-NS_Exploration_Roadmap.md`](ED-NS_Exploration_Roadmap.md) §3 (category A), §5.1 |
| Krieger-Dougherty empirical model | $\mu/\mu_0 = (1 - \phi/\phi_\mathrm{max})^{-[\eta]\phi_\mathrm{max}}$ |
| Power-law / Cross / Carreau / Bingham non-Newtonian models | Standard rheology literature |
| Compositional rule's gradient-penalty content | [`../Architectural_Canon.md`](../Architectural_Canon.md) §1 (configuration-space layer for the same physics) |
| V5 amplitude-INHERITED status | `arcs/arc-N/non_markov_forced.md` §6.5 (relevant for D5 viscoelastic extension) |

**Pre-arc check before D1 derivation begins:** confirm Universal Mobility Law's β-value distribution across the 10 systems and identify whether β values cluster around hard-sphere Krieger-Dougherty (β ≈ 1.82) or span a wider range. If wider, the arc's "Krieger-Dougherty-class" framing should accommodate INHERITED β rather than fixed β.

---

## 3. Structural Mapping

### 3.1 Mobility → viscosity at vector-extension level

Per NS-2.08 §4.1, the ED PDE mobility-channel structure $D \cdot \nabla \cdot [M(\rho) \nabla \rho]$ maps to the NS viscous term $\mu \nabla^2 v$ via component-wise application:

$$D \cdot \nabla \cdot [M(\rho_\mathrm{fluid}) \nabla v_i] \;\longrightarrow\; \mu(\rho_\mathrm{fluid}) \nabla^2 v_i$$

(at constant $M$, equivalent for spatially-uniform fluid density). The structural correspondence:

$$\boxed{\;\mu \;=\; \frac{1}{D \cdot M(\rho_\mathrm{fluid})}\;}$$

(or equivalently $\mu \propto 1/M$ with constant absorbed into the dimensional kinematic-viscosity coefficient).

**Key implication of P4.** Since $M(\rho_\mathrm{fluid}) \to 0$ as $\rho_\mathrm{fluid} \to \rho_\mathrm{max}$, **viscosity diverges at the packing-fraction limit:**

$$\mu(\rho_\mathrm{fluid}) \;\to\; \infty \;\;\;\mathrm{as}\;\;\; \rho_\mathrm{fluid} \to \rho_\mathrm{max}.$$

This is the structural prediction. The functional *form* of the divergence depends on $M$'s specific form near $\rho_\mathrm{max}$.

### 3.2 Three natural ED-derived classes

Based on the choice of mobility argument and saturation form:

| ED structural choice | Predicted fluid class | Empirical correspondence |
|---|---|---|
| $M(\rho_\mathrm{fluid}) = M_0 (1 - \rho/\rho_\mathrm{max})^\beta$ | **Density-driven jamming** | Krieger-Dougherty divergence in dense suspensions |
| $M(\dot\gamma) = M_0 (1 - \dot\gamma/\dot\gamma_\mathrm{max})^\beta$ | **Shear-rate-driven thickening / jamming** | Discontinuous shear thickening (DST), shear-thickening fluids (STFs) |
| $M(\dot\gamma) = M_0 / (1 + (\lambda \dot\gamma)^n)$ (monotone, no zero) | **Power-law / Carreau shear-thinning** | Polymer melts, blood, paint |

The first two are direct P4 applications (mobility vanishing at upper bound). The third is a P4-class generalization where mobility *decreases* monotonically without strict zero — admissible at the architectural level (P4 specifies a bound exists but doesn't forbid monotone-decrease-without-zero as a separate class).

### 3.3 What is form-FORCED, what is INHERITED

**Form-FORCED at architectural level:**
- Existence of viscosity divergence near a packing-fraction or strain-rate bound.
- Functional form of divergence $(1 - \rho/\rho_\mathrm{max})^{-\beta}$ class (ratio-of-distance-to-bound to power).
- Existence of shear-thickening and jamming regimes for dense suspensions.

**Value-INHERITED:**
- Specific value of $\beta$ (varies across the 10 Universal Mobility Law systems; system-specific).
- Specific value of $\rho_\mathrm{max}$ (depends on geometry, particle shape, polydispersity).
- Specific value of $\dot\gamma_\mathrm{max}$ when applicable (depends on inter-particle forces).
- Whether the saturation is continuous (smooth divergence) or discontinuous (DST regime jump).

This is the canonical form-FORCED / value-INHERITED methodology applied to the rheology domain.

---

## 4. Empirical Anchors

### 4.1 Universal Mobility Law (already in inventory)

PDE.md §4.1: ED's mobility law $D(c) = D_0 (1 - c/c_\mathrm{max})^\beta$ has been empirically validated across **10 chemically distinct soft-matter systems** with **R² > 0.986**. This is the empirical content of P4 in the soft-matter regime. The arc's first deliverable (D1) extends this from concentration to packing fraction in fluid mechanics.

### 4.2 Krieger-Dougherty divergence (literature anchor)

Standard rheology: suspension viscosity diverges near close-packing as:

$$\frac{\mu}{\mu_0} = \left(1 - \frac{\phi}{\phi_\mathrm{max}}\right)^{-[\eta]\phi_\mathrm{max}}$$

with $[\eta]$ the intrinsic viscosity (= 5/2 for hard spheres) and $\phi_\mathrm{max}$ the maximum packing fraction (~0.64 for random close packing of monodisperse spheres). For hard spheres the exponent $[\eta]\phi_\mathrm{max} \approx 1.82$. For other particle geometries / polydispersities, the exponent varies — *consistent with ED's form-FORCED structure + value-INHERITED β*.

### 4.3 Shear-thickening and jamming regimes (literature anchor)

Discontinuous shear-thickening (DST) in cornstarch + water, fumed silica suspensions, and shear-thickening fluids (STFs) used in body armor — viscosity jumps multiple orders of magnitude at critical strain rate. This is "shear-rate-driven jamming" in ED's framework: $M(\dot\gamma) \to 0$ at $\dot\gamma_\mathrm{max}$.

Jamming transition in granular materials and dense suspensions: viscosity diverges as packing fraction approaches φ_J (jamming threshold). This is "density-driven jamming" in ED's framework: $M(\rho) \to 0$ at $\rho_\mathrm{max}$.

Both regimes have extensive experimental literature with measured β values — direct comparison targets for D4.

### 4.4 ED's contribution

ED supplies a *structural* derivation: the divergence functional form is form-FORCED by P4; the architectural canon places jamming and shear-thickening within the same canonical-equation family as porous-medium soft matter (Universal Mobility Law). This is structurally significant because it unifies:

- Soft-matter mobility (concentration-driven),
- Suspension rheology near jamming (packing-driven),
- Shear-thickening fluid behavior (strain-rate-driven),

under a single architectural principle (P4) with universal functional form.

ED does *not* predict β values; these are INHERITED from material specifics (particle shape, inter-particle forces, fluid medium). This is consistent with the form-FORCED / value-INHERITED methodology that the program uses across all closures.

---

## 5. Deliverables for the Arc

### D1 — Derive μ(ρ_fluid) = μ₀ (1 − ρ/ρ_max)^(−β) from P4 + mobility→viscosity mapping

Concrete derivation memo. Steps:
1. Take P4: $M(\rho) = M_0 (1 - \rho/\rho_\mathrm{max})^\beta$ (specific form admissible per Architectural_Canon §5 — "specific shape of M(ρ) can vary as long as M(ρ_max) = 0").
2. Apply NS-2.08 §4.1 mapping $\mu = 1/(D \cdot M)$.
3. Result: $\mu(\rho) = \mu_0 (1 - \rho/\rho_\mathrm{max})^{-\beta}$, Krieger-Dougherty class.
4. Show this is the form-FORCED prediction for density-driven jamming.

Estimated 1 session. Cleanest of the five deliverables.

### D2 — Extend to shear-rate-dependent mobility M(γ̇)

Apply the mapping when $M$ depends on strain rate magnitude $\dot\gamma$ rather than density. Three structural sub-cases:
- $M(\dot\gamma) = M_0 (1 - \dot\gamma/\dot\gamma_\mathrm{max})^\beta$ → shear-rate-driven jamming / DST.
- $M(\dot\gamma) = M_0 / (1 + (\lambda \dot\gamma)^n)$ → shear-thinning (Cross / Carreau-class).
- Mixed dependencies $M(\rho, \dot\gamma)$ → suspension-rheology models.

Estimated 1–2 sessions.

### D3 — Identify which empirical rheology classes are ED-architectural vs. inherited

Catalogue. Four classes to audit:
- Newtonian: constant $M$. Special case (no saturation). Form-trivially-FORCED.
- Krieger-Dougherty / suspension-jamming: $M(\rho)$ saturating at $\rho_\mathrm{max}$. **Form-FORCED via P4.**
- DST / shear-thickening: $M(\dot\gamma)$ saturating at $\dot\gamma_\mathrm{max}$. **Form-FORCED via P4 generalization to strain rate.**
- Power-law / Carreau shear-thinning: $M(\dot\gamma)$ monotone-decreasing without zero. **Form-FORCED via monotone P4-class.**
- Bingham yield-stress: requires inverted P4 (M(γ̇)=0 at *lower* threshold rather than upper). **Not canonical P4; flagged as non-ED-architectural** (treatable via stress-dependent mobility but breaks the upper-bound canonical structure).
- Oldroyd-B / FENE-P / Giesekus: require additional constitutive structure (memory kernel, conformation tensor). Not derivable from P4 alone; flagged for future extensions.

Output: clean table mapping rheological classes to ED-architectural status. Estimated 1 session.

### D4 — Compare ED predictions to rheology datasets (qualitative first; quantitative optional)

Take Universal Mobility Law's β values for the 10 soft-matter systems and compare to:
- Krieger-Dougherty β values for hard-sphere suspensions (~1.82) and other particle geometries.
- DST β values for shear-thickening fluids.
- Cross / Carreau exponents for polymer melts.

Qualitative comparison: do the β value distributions overlap or diverge across regimes? If similar, ED's mobility law unifies disparate rheology regimes structurally; if different, ED's β is regime-dependent (still INHERITED but with class-specific patterns).

Quantitative comparison: optional. Would require dataset access (rheology databases) and full statistical analysis. Treat as appendix-class work; not core to the arc.

Estimated 1 session for qualitative; 2 additional for quantitative.

### D5 — Integrate viscoelastic V5 content as extension subsection

From roadmap #2 (partial productive finding): ED accommodates Maxwell-class viscoelasticity via V5 cross-chain correlations with finite memory time. Form-FORCED memory-kernel structure; values INHERITED. Brief sub-section noting that the same architectural framework that produces non-Newtonian rheology (D1–D3) also accommodates viscoelastic fluids when V5 memory time is finite at NS scales. Not a separate arc.

Estimated 0.5 sessions.

---

## 6. Risks and Non-Goals

### 6.1 Bingham yield-stress fluids — flagged as non-canonical

Bingham plastic behavior (yields below threshold stress, then Newtonian above) requires either:
- Inverted P4: $M = 0$ at *lower* threshold ($\dot\gamma_\mathrm{min} = 0$ in some sense), $M > 0$ above. This is *not* canonical P4 (which has $M = 0$ at upper bound).
- Stress-dependent mobility: $M$ depends on local stress rather than strain rate or density. Admissible at constitutive level but not directly P4-derivable.

The arc will flag Bingham as **non-canonically-ED** in D3 catalogue rather than attempt to force it into the framework. Yield-stress fluids exist empirically but require additional structural articulation.

### 6.2 Compressibility/shock behavior — out of scope

Roadmap #5 (compressibility/shocks via P4) is consistency-only, not derivation. The arc will not pursue gas-dynamics shocks; the porous-medium-class compact-support behavior is structurally different from Rankine-Hugoniot shock structure and the mapping is mismatched. Flagged in D3 as "ED's P4 is consistent with density-limit physics but does not derive shock dynamics."

### 6.3 Full constitutive models — out of scope

Oldroyd-B, FENE-P, Giesekus, and similar constitutive models require additional structural content beyond P4 (memory kernels with specific conformational dependence, finite extensibility constraints, etc.). The arc will not attempt to derive these; D5 limits viscoelastic content to "Maxwell-class memory-kernel structural compatibility" only.

### 6.4 Quantitative β prediction — out of scope (form-FORCED only, not value-FORCED)

The arc does not attempt to predict β values from substrate primitives. Per the form-FORCED / value-INHERITED methodology, β is INHERITED from material-specific physics (particle geometry, inter-particle forces, etc.). The Universal Mobility Law's β-value distribution across 10 systems is the empirical baseline; ED's contribution is the *structural form*, not the numerical exponent.

---

## 7. Timeline and Effort

Estimated session counts at demonstrated cycle pace:

| Phase | Sessions | Output |
|---|---|---|
| Scoping (this memo) | 1 | This document |
| D1 (density-driven jamming derivation) | 1 | Krieger-Dougherty form derived |
| D2 (shear-rate extension) | 1–2 | Three sub-class derivations |
| D3 (empirical-class audit) | 1 | Catalogue table |
| D4 (qualitative empirical comparison) | 1 | Cross-system β analysis |
| D5 (viscoelastic V5 integration) | 0.5 | Brief subsection |
| Synthesis memo | 1 | Arc closure deliverable |
| **Total core arc** | **6–7 sessions** | Closes arc + memo-ready paper draft |
| Optional quantitative empirical comparison | +2 | Full statistical analysis appendix |

Comparable in scale to the substrate-gravity arc's stages or to NS-2's seven-memo cycle. Achievable in 1–2 weeks at demonstrated pace.

---

## 8. Recommended Next Steps

1. **Begin D1 — derive the Krieger-Dougherty form from P4.** File: `theory/Navier Stokes/P4_NN_D1_Density_Jamming.md`. Direct derivation: P4 + mobility-viscosity mapping → $\mu(\rho) = \mu_0 (1 - \rho/\rho_\mathrm{max})^{-\beta}$. Estimated 1 session. Cleanest opening move; produces a memo-ready substantive result fast.

2. **Prepare mapping diagrams for M ↔ μ** (small visual deliverable). One-page schematic showing the structural correspondence between ED's mobility channel (porous-medium soft matter) and NS's viscous channel (suspension rheology). Useful for D1 + D3 visualization. Could live at `theory/Navier Stokes/figures/M_to_mu_mapping.svg` or as embedded markdown diagram in D1.

3. **Decide on empirical-comparison scope before D4.** Two options: (a) qualitative-only — compare β-value distributions across Universal Mobility Law systems vs. rheology literature without full statistics; (b) quantitative — add 2 sessions for dataset analysis. Recommend qualitative-only for the core arc; quantitative as optional appendix if the qualitative result is striking enough to warrant publication-grade analysis.

### Decisions for you

- **Confirm scope** as defined in §5 (5 deliverables D1–D5, no Bingham, no Oldroyd, no quantitative-β-prediction).
- **Confirm timeline expectation** — 6–7 sessions for core arc, plus 2 optional for quantitative empirical work.
- **Decide whether the arc produces a standalone paper** (recommend yes, given empirical anchoring) or feeds into a broader "ED-fluid-mechanical applications" paper combining #4 + #1 (turbulence) + #2 (viscoelastic).

---

*P4 → Non-Newtonian Fluid Mechanics arc scoped. Strongest productive route from off-leash exploration. Five deliverables (D1 density-jamming Krieger-Dougherty derivation, D2 shear-rate extension, D3 rheology-class audit, D4 qualitative empirical comparison, D5 viscoelastic V5 integration). Form-FORCED structural prediction: Krieger-Dougherty-class viscosity divergence near jamming. Value-INHERITED β values per material specifics. Empirical anchoring already in place via Universal Mobility Law's 10-system R² > 0.986 validation. Timeline: 6–7 sessions core arc; +2 optional quantitative empirical work. Begin with D1 (density-driven jamming derivation) — cleanest opening move.*
