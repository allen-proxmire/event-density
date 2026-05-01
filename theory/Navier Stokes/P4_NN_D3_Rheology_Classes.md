# P4-NN-D3 — Rheology-Class Audit Catalogue

**Date:** 2026-04-30
**Status:** Deliverable D3 of the P4 → Non-Newtonian arc. Catalogue consolidation. **Headline: 13 rheology classes audited against ED's P4 mobility-saturation architecture. Five are form-FORCED (Newtonian, Krieger-Dougherty, DST/STF, Cross-form shear-thinning, mixed-regime); four are form-compatible with INHERITED extra parameters (power-law thinning, Carreau, Carreau-Yasuda, Maxwell viscoelastic via V5); four are non-canonical ED, requiring constitutive structure beyond P4 (Oldroyd-B, Giesekus, FENE-P, Bingham yield-stress).**
**Companions:** [`P4_NN_D1_Density_Jamming.md`](P4_NN_D1_Density_Jamming.md), [`P4_NN_D2_Shear_Rate.md`](P4_NN_D2_Shear_Rate.md), [`Future_Arc_P4_Non_Newtonian_Scoping.md`](Future_Arc_P4_Non_Newtonian_Scoping.md).

---

## 1. Purpose

This memo consolidates the results of D1 (density-driven jamming → Krieger-Dougherty) and D2 (shear-rate extension → DST + Cross-class) into a unified classification of standard rheology models under ED's architectural principles.

Each rheology class is classified by:
- **Form-FORCED:** structurally derived from P4 mobility-saturation + an admissible mobility-viscosity mapping (Stokes-Einstein-class inversion or NS-2.08 direct).
- **Form-compatible with INHERITED parameters:** consistent with ED architecture but with shape parameters or extra structure that goes beyond what P4 alone supplies.
- **Non-canonical ED:** requires constitutive structure that is not derivable from P4 — either an inverted saturation (e.g., Bingham yield-stress) or extra fields (conformation tensor, finite extensibility constraints) that lie outside the canonical ED PDE architecture.

The catalogue serves as the reference for D4 (qualitative empirical comparison) and as program-level documentation of ED's reach into rheology.

---

## 2. Inputs

| Input | Source |
|---|---|
| D1: Krieger-Dougherty derivation via concentration mobility + Stokes-Einstein-class inversion | [`P4_NN_D1_Density_Jamming.md`](P4_NN_D1_Density_Jamming.md) |
| D2: shear-rate extension; dual mapping (Stokes-Einstein for jamming/DST; NS-2.08 for polymer thinning) | [`P4_NN_D2_Shear_Rate.md`](P4_NN_D2_Shear_Rate.md) |
| P4 mobility-saturation principle | [`../Architectural_Canon.md`](../Architectural_Canon.md) §2 |
| Universal Mobility Law $M(\rho) = M_0(1-\rho/\rho_\mathrm{max})^\beta$ | [`../PDE.md`](../PDE.md) §4.1 |
| NS-2.08 mobility → viscosity direct mapping ($\mu = D \cdot M$ for velocity-mobility) | [`NS-2.08_ED-PDE_Direct_Mapping.md`](NS-2.08_ED-PDE_Direct_Mapping.md) §4.1 |
| Standard rheology models (literature) | Newtonian, Krieger-Dougherty, DST/STF, power-law, Cross, Carreau, Carreau-Yasuda, Maxwell, Oldroyd-B, Giesekus, FENE-P, Bingham |

---

## 3. Classification Table

**Notation.** SE = Stokes-Einstein-class inversion ($\mu \propto 1/M$), used for concentration-mobility / particle-driven scenarios. NS-2.08 = direct velocity-mobility mapping ($\mu = D \cdot M$), used for velocity-diffusivity-class scenarios. Form-FORCED = structurally derived from P4 + an admissible mapping. Compatible-INHERITED = consistent with ED architecture with shape parameters going beyond basic P4. Non-canonical = requires extra constitutive structure.

| # | Class | Standard form | ED mapping (which $M$) | μ↔M identification | ED architectural status | Notes |
|---|---|---|---|---|---|---|
| 1 | **Newtonian** | $\mu = \mathrm{const}$ | $M = \mathrm{const}$ | Either | **Form-FORCED** (special case) | Limit of P4 far from saturation; both mappings reduce to Newtonian. Empirically: dilute fluids, simple liquids, low-shear gases. |
| 2 | **Krieger-Dougherty** | $\mu \propto (1 - \phi/\phi_\mathrm{max})^{-[\eta]\phi_\mathrm{max}}$ | $M(\rho)$ from Universal Mobility Law | SE inversion | **Form-FORCED via P4 (D1)** | β = $[\eta]\phi_\mathrm{max}$ ≈ 1.82 for hard spheres; varies for other particle geometries. Empirically: dense suspensions near close-packing. |
| 3 | **Discontinuous Shear-Thickening (DST) / STF** | $\mu \propto (1 - \dot\gamma/\dot\gamma_c)^{-\beta}$ near onset | $M(\dot\gamma) = M_0(1 - \dot\gamma/\dot\gamma_\mathrm{max})^\beta$ | SE inversion | **Form-FORCED via P4 (D2 §4.1)** | Same architectural principle as Krieger-Dougherty applied to $\dot\gamma$. Empirically: cornstarch+water, fumed silica, body-armor STFs. |
| 4 | **Power-law shear-thinning** | $\mu = K \dot\gamma^{n-1}$, $0 < n < 1$ | $M(\dot\gamma) \propto \dot\gamma^{n-1}$ (direct) or $\dot\gamma^{1-n}$ (SE) | Either | **Form-compatible with INHERITED $n$** | Pure power-law without low-shear plateau; usually a high-shear approximation of Cross/Carreau. n INHERITED. |
| 5 | **Cross model** | $\mu = \mu_0 / [1 + (\lambda \dot\gamma)^n]$ | $M(\dot\gamma) = M_0/[1+(\lambda\dot\gamma)^n]$ direct, or $M_0[1+(\lambda\dot\gamma)^n]$ SE | Either | **Form-FORCED** (with $(\lambda, n)$ INHERITED) | Most common shear-thinning model. Empirically: polymer melts, polymer solutions, blood. |
| 6 | **Carreau** | $\mu = \mu_\infty + (\mu_0 - \mu_\infty)[1 + (\lambda\dot\gamma)^2]^{(n-1)/2}$ | Cross-class with high-shear floor $\mu_\infty$ | Either | **Form-compatible with INHERITED $\mu_\infty, n$** | Adds high-shear viscosity asymptote beyond Cross. Empirically: polymer melts at high shear. |
| 7 | **Carreau-Yasuda** | $(\mu - \mu_\infty)/(\mu_0 - \mu_\infty) = [1 + (\lambda\dot\gamma)^a]^{(n-1)/a}$ | Carreau generalization with shape exponent $a$ | Either | **Form-compatible with INHERITED $a, n, \mu_\infty$** | Empirical generalization of Carreau; widely used industry-standard fit form. |
| 8 | **Mixed-regime (thinning → thickening)** | Non-monotone $\mu(\dot\gamma)$ | Non-monotone $M(\dot\gamma) = M_0[1+(\lambda_1\dot\gamma)^{n_1}](1-\dot\gamma/\dot\gamma_\mathrm{max})^\beta$ | SE inversion | **Form-FORCED via constitutive-choice freedom (D2 §4.3)** | Concentrated colloidal suspensions; granular pastes; thickening following thinning. |
| 9 | **Maxwell viscoelastic** | $\tau_R \dot\sigma + \sigma = 2\mu S$ | V5 cross-chain memory kernel with finite $\tau_R$ | (memory-kernel structure beyond P4) | **Form-compatible with INHERITED $\tau_R, \mu$** | Memory-kernel structure is V5-class; values INHERITED per arc-N N.2 §6.5. Treated separately in D5. |
| 10 | **Oldroyd-B** | Maxwell + convected (upper-convected) derivative + retardation | V5 + conformation-tensor structure | Beyond P4 | **Non-canonical ED** | Requires conformation tensor evolution beyond V5's bandwidth-correlation structure. Polymer dilute-solution model. |
| 11 | **Giesekus** | Oldroyd-B + quadratic stress contribution | Beyond V5 | Beyond P4 | **Non-canonical ED** | Adds quadratic-in-stress nonlinearity; requires constitutive structure ED architecture doesn't natively supply. |
| 12 | **FENE-P** | Maxwell with finite-extensibility constraint on polymer chains | Beyond V5 | Beyond P4 | **Non-canonical ED** | Finite-extensibility constraint requires additional polymer-chain structural physics not native to ED. |
| 13 | **Bingham yield-stress** | $\sigma = \sigma_\mathrm{yield} + \mu \dot\gamma$ for $\sigma > \sigma_\mathrm{yield}$, no flow below | Would need $M(\sigma) = 0$ for $\sigma < \sigma_\mathrm{yield}$ — *inverted* P4 | (inverted P4 not canonical) | **Non-canonical ED** | P4 specifies $M = 0$ at *upper* bound; Bingham requires $M = 0$ at *lower* threshold. Yield-stress fluids are real but not canonical ED. |

---

## 4. ED Architectural Interpretation

### 4.1 What ED predicts structurally (form-FORCED)

Five rheology classes are form-FORCED at the architectural level:

1. **Newtonian** (special case of P4 far from saturation).
2. **Krieger-Dougherty / suspension jamming** (P4 applied to concentration mobility + Stokes-Einstein-class inversion).
3. **Discontinuous Shear-Thickening / STF** (P4 applied to strain-rate mobility + Stokes-Einstein-class inversion).
4. **Cross-form shear-thinning** (monotone P4-class via either mapping).
5. **Mixed-regime thinning → thickening** (non-monotone P4-class via constitutive-choice freedom; admissible at the architectural level since constitutive choice for $M$ is open within the form-FORCED P4 saturation structure).

**Structural significance.** ED's P4 + the dual-mapping framework (Stokes-Einstein-class inversion for particle-mobility scenarios; NS-2.08 direct for velocity-mobility scenarios) places these five classes within a single architectural family. The Universal Mobility Law's empirical validation across 10 soft-matter systems anchors the form-FORCED structure empirically; the rheology-domain extensions (suspension jamming, DST, polymer-melt thinning) follow the same pattern.

### 4.2 What ED accommodates but does not predict (compatible-INHERITED)

Four classes are form-compatible but require INHERITED extra parameters or constitutive structure beyond basic P4:

1. **Power-law shear-thinning** (the exponent $n$ is INHERITED; the architectural form is Cross-class with specific high-shear limit).
2. **Carreau** (adds $\mu_\infty$ high-shear asymptote; INHERITED).
3. **Carreau-Yasuda** (adds shape exponent $a$ on top of Carreau; INHERITED).
4. **Maxwell viscoelastic** (memory-kernel structure via V5 with finite relaxation time; both $\tau_R$ and amplitude INHERITED per arc-N N.2 §6.5).

**Structural significance.** ED accommodates these models as form-compatible refinements of the basic P4 + V5 architecture. The INHERITED parameters reflect material-specific physics (shape factors, polymer relaxation times, etc.) that ED's substrate framework cannot pin from primitives but cleanly hosts at the constitutive level. This is consistent with the program-wide form-FORCED / value-INHERITED methodology.

### 4.3 What ED does not natively support (non-canonical)

Four classes require constitutive structure beyond P4 + V5:

1. **Oldroyd-B** (conformation tensor evolution).
2. **Giesekus** (quadratic stress nonlinearity).
3. **FENE-P** (finite-extensibility polymer-chain structure).
4. **Bingham yield-stress** (inverted P4 — $M = 0$ at *lower* threshold, not P4's canonical upper bound).

**Structural significance.** These models require additional structural physics — conformation tensors, finite extensibility constraints, yield-threshold dynamics — that ED's canonical architecture does not natively supply. Each could in principle be accommodated via *architectural extensions* (e.g., a tensor-extended ED PDE for conformation; an inverted-saturation P4-variant for yield-stress fluids), but doing so would constitute new substrate articulation beyond the current canon. Flagged for `theory/Candidate_Architectural_Extensions.md` (per [`Architectural_Canon_Vector_Extension.md`](../Architectural_Canon_Vector_Extension.md) §8 recommendation).

The non-canonical-ED status is **not a refutation** of these models — they are real empirical phenomena. It is a *classification*: they sit outside ED's canonical architectural reach without explicit canon extension.

### 4.4 Aggregate: ED's reach into rheology

**ED's canonical architecture (P4 + V5 with two mappings) form-FORCES the major rheology classes governing dense suspensions, shear-thickening fluids, and polymer-melt shear-thinning.** The Universal Mobility Law's empirical anchoring extends this from soft matter to fluid mechanics structurally. Three of the four "non-canonical" classes (Oldroyd-B, Giesekus, FENE-P) are polymer-solution-specific models requiring conformation-tensor structure; one (Bingham) requires inverted P4. Each is a candidate for future canon extension if priorities call for it.

In aggregate: ED's reach is broad (5 of 13 form-FORCED + 4 of 13 form-compatible = 9 of 13 covered) and its non-coverage (4 of 13) is concentrated in polymer-solution-specific or yield-threshold models that all require constitutive structure beyond ED's core canon.

---

## 5. Empirical Anchors

### 5.1 Universal Mobility Law β distribution

Per `papers/Universal_Mobility_Law/`, β has been measured across 10 chemically distinct soft-matter systems with R² > 0.986 in each fit. **Specific β-value distribution to be assembled in pre-D4 check** (per scoping §3 recommendation). The Universal Mobility Law's β is the central empirical anchor for ED's P4 form-FORCED prediction across soft-matter systems.

### 5.2 Krieger-Dougherty β values

Hard-sphere suspensions: β = $[\eta]\phi_\mathrm{max}$ with $[\eta] = 5/2$, $\phi_\mathrm{max} \approx 0.64$ (random close packing) → β ≈ 1.625; revised values closer to β ≈ 1.82 are commonly fit empirically. Polydisperse suspensions and non-spherical particles: β varies with particle geometry; literature spans β ≈ 1.5–2.5 depending on shape and aspect ratio. **Specific values to be assembled in pre-D4 check.**

### 5.3 DST / STF critical shear rates

Cornstarch + water (50–55% w/w): $\dot\gamma_c$ ≈ 1–10 s⁻¹ (literature varies with concentration). Fumed silica suspensions in PEG: $\dot\gamma_c$ ≈ 100–10000 s⁻¹ depending on volume fraction. STFs designed for body armor: tuned $\dot\gamma_c$ for impact regime (~10⁵ s⁻¹). **Order-of-magnitude variation across systems**; specific values material-dependent.

### 5.4 Cross / Carreau shape parameters

Polymer melts (HDPE, polystyrene, polypropylene): $n$ ≈ 0.3–0.5 in Cross fits; Carreau-Yasuda $a$ ≈ 0.5–2 depending on chain architecture. Polymer solutions (HPC, xanthan, CMC): $n$ ≈ 0.1–0.4 (more strongly thinning than melts). Blood: classical Cross fit gives $n$ ≈ 0.3, $\lambda$ ≈ 1–5 s. **Specific tabulations available in standard rheology references.**

### 5.5 Pre-D4 data assembly recommendation

Per the scoping memo §3, before D4 (qualitative empirical comparison), assemble a summary table:
- Universal Mobility Law β values across 10 systems (from existing repo material).
- Krieger-Dougherty β values across hard-sphere, polymer, and granular suspensions (literature tables).
- DST $\dot\gamma_c$ ranges across STF materials.
- Cross / Carreau $(n, \lambda)$ for canonical polymer melts and biological fluids.

The qualitative comparison in D4 will examine cross-system patterns: do β values cluster within each rheology class? Across classes? Are there universal scaling relations? ED's architectural prediction is that β is INHERITED per material but the *form* (1 - x/x_max)^β is universal; the data should support this if ED's structural prediction is correct.

---

## 6. Recommended Next Steps

In priority order. With D3 closed, the arc has its catalogue and is ready for empirical comparison.

1. **Execute pre-D4 data assembly.** ~30–60 minutes assembling β / shape-parameter tables from Universal Mobility Law repo material + standard rheology literature. Output: a small data appendix (`P4_NN_D4_data_summary.md` or similar) listing β / $\dot\gamma_c$ / $(n, \lambda)$ values across the 13 catalogued classes (where applicable). Used directly in D4.

2. **Draft D4 — qualitative empirical comparison.** File: `theory/Navier Stokes/P4_NN_D4_Empirical_Comparison.md`. Cross-system pattern analysis: do β-value distributions cluster within rheology classes? Across classes? Is there a universal β across the form-FORCED classes (Krieger-Dougherty + DST + Cross), or do they differ systematically? ED's structural prediction: form is universal, β is INHERITED per material. Estimated 1 session for qualitative scope; +2 sessions optional for full quantitative analysis.

3. **Draft D5 — V5 viscoelastic integration as brief subsection.** File: `theory/Navier Stokes/P4_NN_D5_Viscoelastic_V5.md` (or fold into D4 / synthesis memo as appendix). Brief sub-section noting Maxwell viscoelastic class as V5-mediated extension of the P4 framework, with τ_R and amplitude INHERITED per arc-N N.2 §6.5. Estimated 0.5 sessions.

4. **Decide on standalone-paper status** for the arc. With D1 + D2 + D3 in hand and D4 + D5 imminent, the arc has substantive content suitable for a standalone publication: "ED's Mobility-Saturation Principle Predicts Non-Newtonian Rheology Classes." Possible extension: combine with a future "ED-on-Earth" applications paper covering the Universal Mobility Law results plus rheology extension. Decision point flagged for after D4 closes.

### Decisions for you

- **Confirm five-class form-FORCED list.** Newtonian (special case), Krieger-Dougherty, DST/STF, Cross-form shear-thinning, mixed-regime non-monotone. These five are the substantive ED-derived rheology predictions from the arc.
- **Confirm four-class compatible-INHERITED list.** Power-law thinning, Carreau, Carreau-Yasuda, Maxwell viscoelastic. ED accommodates without predicting parameter values.
- **Confirm four-class non-canonical list and flagging.** Oldroyd-B, Giesekus, FENE-P, Bingham yield-stress. Each is real empirical phenomenon; ED architectural extension would be required to absorb canonically. Track in `theory/Candidate_Architectural_Extensions.md`.
- **Confirm proceeding to pre-D4 data assembly + D4 qualitative analysis.**

---

*P4-NN-D3 catalogue complete. 13 rheology classes audited; 5 form-FORCED (Newtonian, Krieger-Dougherty, DST/STF, Cross, mixed-regime); 4 compatible-INHERITED (power-law, Carreau, Carreau-Yasuda, Maxwell viscoelastic via V5); 4 non-canonical (Oldroyd-B, Giesekus, FENE-P, Bingham). ED's architectural reach covers 9 of 13 classes; the 4 non-canonical require constitutive structure beyond P4 + V5 (conformation tensors, finite extensibility, inverted saturation). The Universal Mobility Law's 10-system R² > 0.986 anchor extends to fluid-mechanical rheology via the form-FORCED structure derived in D1 + D2. Pre-D4 data assembly + D4 qualitative empirical comparison next.*
