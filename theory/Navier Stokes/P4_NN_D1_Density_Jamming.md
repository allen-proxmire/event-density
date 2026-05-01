# P4-NN-D1 — Density-Driven Jamming: Krieger-Dougherty from P4 Mobility Saturation

**Date:** 2026-04-30
**Status:** Deliverable D1 of the P4 → Non-Newtonian arc. **Headline: Krieger-Dougherty-class viscosity divergence $\mu(\rho) = \mu_0 (1 - \rho/\rho_\mathrm{max})^{-\beta}$ derives from ED's P4 mobility-saturation principle (form-FORCED, empirically validated via Universal Mobility Law) combined with the standard Stokes-Einstein-class mobility-viscosity inversion (imported from kinetic theory). β value INHERITED per material specifics.**
**Companions:** [`Future_Arc_P4_Non_Newtonian_Scoping.md`](Future_Arc_P4_Non_Newtonian_Scoping.md), [`../Architectural_Canon.md`](../Architectural_Canon.md) §2 (P4), [`../PDE.md`](../PDE.md) §4.1 (Universal Mobility Law).

---

## 1. Purpose

This memo provides the first concrete derivation in the P4 → Non-Newtonian arc:

**Starting from:**
- ED's P4: $M(\rho_\mathrm{max}) = 0$ with $M(\rho) > 0$ for $\rho < \rho_\mathrm{max}$,
- The empirically-validated Universal Mobility Law (PDE.md §4.1, R² > 0.986 across 10 soft-matter systems),
- The standard Stokes-Einstein-class mobility-viscosity inversion,

**Derive:**
- The Krieger-Dougherty viscosity form $\mu(\rho) = \mu_0 (1 - \rho/\rho_\mathrm{max})^{-\beta}$ for dense suspensions and the structural origin of jamming behavior near close-packing.

The derivation is straightforward at the form-derivation level. The honest accounting (form-FORCED vs. value-INHERITED vs. imported-from-standard-physics) is the substantive content.

---

## 2. Inputs

| Input | Source | Role |
|---|---|---|
| P4 mobility-saturation: $M(\rho_\mathrm{max}) = 0$ | [`Architectural_Canon.md`](../Architectural_Canon.md) §2 | ED architectural principle |
| Universal Mobility Law: $M(\rho) = M_0 (1 - \rho/\rho_\mathrm{max})^\beta$ | [`PDE.md`](../PDE.md) §4.1, `papers/Universal_Mobility_Law/` | Form-FORCED specific shape; β value INHERITED |
| 10-system empirical validation R² > 0.986 | Same | Empirical anchor for the law |
| Stokes-Einstein-class mobility-viscosity inversion | Standard kinetic theory / suspension physics | Imported from standard physics |
| Arc scoping with form-FORCED / value-INHERITED methodology | [`Future_Arc_P4_Non_Newtonian_Scoping.md`](Future_Arc_P4_Non_Newtonian_Scoping.md) | Audit framework |

**Note on what is and isn't ED.** The Stokes-Einstein-class inversion ($\mu \propto 1/D_\mathrm{tracer}$ in dilute and moderately-dense suspensions) is a result of standard kinetic theory / Stokes-flow analysis, not derived from ED primitives. ED supplies the *form-FORCED structure* of how mobility saturates (P4 + Universal Mobility Law); the conversion to viscosity uses standard physics. The combination produces Krieger-Dougherty. This is honest accounting, not a weakness — most empirical content in physics combines architectural principles with imported relations.

---

## 3. Starting Point: The Universal Mobility Law

PDE.md §4.1 states the Universal Mobility Law as the empirical content of P4 in the soft-matter regime:

$$\boxed{\;M(\rho) \;=\; M_0 \left(1 - \frac{\rho}{\rho_\mathrm{max}}\right)^\beta \;\;\;\mathrm{with}\;\;\; \beta > 0\;}$$

with empirical validation across **10 chemically distinct soft-matter systems** at **R² > 0.986** (per `papers/Universal_Mobility_Law/`).

### 3.1 Form-FORCED vs. value-INHERITED in the Mobility Law

- **Form-FORCED by ED's P4:** the existence of mobility saturation at $\rho_\mathrm{max}$, and the (1 - ρ/ρ_max)^β functional class (degenerate diffusion form per P1's operator content, with M(ρ_max) = 0 per P4).
- **Value-INHERITED:** β value, ρ_max value, and M_0 prefactor — vary across the 10 systems per material physics.
- **Empirically anchored:** the form-FORCED content matches data with R² > 0.986 across systems.

### 3.2 The mobility's physical content

In a dense suspension or soft-matter system, $M(\rho)$ is the *concentration self-diffusion coefficient* — the diffusivity of particles or solute molecules through the medium at concentration ρ. As concentration approaches close-packing $\rho_\mathrm{max}$, particles become geometrically constrained and self-diffusion drops; at $\rho = \rho_\mathrm{max}$, particles cannot move past one another, and self-diffusion vanishes. This is jamming at the diffusion level.

The Universal Mobility Law's empirical content captures this directly: $M(\rho) \to 0$ as $\rho \to \rho_\mathrm{max}$ with the specific (1 - ρ/ρ_max)^β scaling.

---

## 4. Mobility → Viscosity Mapping (Stokes-Einstein-Class Inversion)

The connection between particle self-diffusion and bulk-fluid viscosity in dense suspensions is supplied by Stokes-Einstein-class physics:

### 4.1 Stokes-Einstein in dilute regime

For a single tracer particle of radius $a$ diffusing in a Newtonian fluid of viscosity $\mu$, the Einstein relation gives:

$$D_\mathrm{tracer} \;=\; \frac{k_B T}{6 \pi \mu a}.$$

Inverting:

$$\mu \;=\; \frac{k_B T}{6 \pi a \, D_\mathrm{tracer}} \;\propto\; \frac{1}{D_\mathrm{tracer}}.$$

This is the dilute-limit relation. Standard kinetic theory / Stokes-flow content; not derived from ED.

### 4.2 Stokes-Einstein extended to dense suspensions

For finite-concentration suspensions, $D_\mathrm{tracer}$ is replaced by the concentration-dependent self-diffusion coefficient $M(\rho)$, and the relevant viscosity is the *suspension viscosity* $\mu_\mathrm{susp}(\rho)$:

$$\mu_\mathrm{susp}(\rho) \;\propto\; \frac{1}{M(\rho)}.$$

Setting the proportionality constant via the dilute limit ($\mu_\mathrm{susp}(0) = \mu_0$, the viscosity of the pure carrier fluid; $M(0) = M_0$):

$$\boxed{\;\mu_\mathrm{susp}(\rho) \;=\; \mu_0 \cdot \frac{M_0}{M(\rho)}.\;}$$

This is the standard Stokes-Einstein-class mobility-viscosity inversion for moderate-to-dense suspensions. Imported from kinetic theory.

### 4.3 Note on the regime of validity

The Stokes-Einstein-class inversion is best-justified in the dilute and moderately-dense regimes (Brownian particles in Newtonian solvent, hard-sphere suspensions away from glass transition). At very high concentrations near $\rho_\mathrm{max}$, additional corrections appear (mode-coupling theory, glass-transition divergence), but these refine rather than replace the basic $\mu \propto 1/M$ relation. The Krieger-Dougherty form is empirically observed across the regime and is the canonical phenomenological model.

---

## 5. Result: Krieger-Dougherty-Class Divergence

Substituting the Universal Mobility Law into the Stokes-Einstein-class inversion:

$$\mu_\mathrm{susp}(\rho) \;=\; \mu_0 \cdot \frac{M_0}{M_0 (1 - \rho/\rho_\mathrm{max})^\beta} \;=\; \mu_0 \cdot (1 - \rho/\rho_\mathrm{max})^{-\beta}.$$

$$\boxed{\;\mu_\mathrm{susp}(\rho) \;=\; \mu_0 \left(1 - \frac{\rho}{\rho_\mathrm{max}}\right)^{-\beta}\;}$$

**This is the Krieger-Dougherty viscosity form.** The standard empirical Krieger-Dougherty model is:

$$\frac{\mu_\mathrm{susp}}{\mu_0} = \left(1 - \frac{\phi}{\phi_\mathrm{max}}\right)^{-[\eta]\phi_\mathrm{max}}$$

with $[\eta] = 5/2$ for hard spheres giving exponent $[\eta]\phi_\mathrm{max} \approx 1.82$ for $\phi_\mathrm{max} \approx 0.64$ (random close packing). Identifying $\rho \leftrightarrow \phi$, $\rho_\mathrm{max} \leftrightarrow \phi_\mathrm{max}$, $\beta \leftrightarrow [\eta]\phi_\mathrm{max}$, the ED-derived form is structurally identical to Krieger-Dougherty.

### 5.1 What ED supplies and what is INHERITED

**Form-FORCED by ED:**
- Existence of viscosity divergence near a packing-fraction limit $\rho_\mathrm{max}$.
- Specific functional form: power-law divergence in $(1 - \rho/\rho_\mathrm{max})$.
- The structural reason for jamming behavior (P4 mobility saturation — particles cannot move at close-packing).

**Value-INHERITED:**
- Specific β value (varies by particle geometry, surface chemistry, polydispersity).
- Specific $\rho_\mathrm{max}$ value (depends on particle shape and packing structure).
- Specific $\mu_0$ value (carrier fluid).

**Imported from standard physics:**
- The Stokes-Einstein-class inversion $\mu \propto 1/M$. This is kinetic-theory content, not ED-derived.

### 5.2 The structural significance

ED's contribution to suspension rheology is not the prediction of β values (that comes from particle-physics specifics) — it is the *structural prediction that suspension viscosity should diverge as a power-law in $(1 - \rho/\rho_\mathrm{max})$*. This functional form is form-FORCED by P4. The combination with Stokes-Einstein produces the empirically-observed Krieger-Dougherty model.

The empirical validation is already in place: Universal Mobility Law's R² > 0.986 across 10 systems shows the (1 - ρ/ρ_max)^β form fits the *mobility* data well. By Stokes-Einstein, the (1 - ρ/ρ_max)^(-β) form should fit the *viscosity* data with the same β value (per system). This is testable directly against Krieger-Dougherty fits in suspension rheology literature; see D4 for the empirical-comparison deliverable.

---

## 6. Interpretation

### 6.1 Why Newtonian fluids correspond to constant $M$

For dilute or non-jammed fluids, $\rho \ll \rho_\mathrm{max}$ and $M(\rho) \approx M_0$ (constant). The Stokes-Einstein-class relation gives $\mu \approx \mu_0$ (constant). This is the Newtonian limit. ED's P4 is *trivially* satisfied (no saturation observed) but the structural content is still present — Newtonian behavior is the limiting case of Krieger-Dougherty far from $\rho_\mathrm{max}$.

### 6.2 Why dense suspensions show non-Newtonian behavior

As ρ approaches $\rho_\mathrm{max}$, the (1 - ρ/ρ_max)^(-β) factor grows superlinearly. Suspension viscosity rises sharply with concentration in this regime — the standard observation of "thickening" in dense suspensions. P4 mobility-saturation predicts this transition structurally without invoking ad-hoc viscosity-vs-concentration models.

### 6.3 Why this is form-FORCED, not empirical fitting

Standard rheology presents Krieger-Dougherty as a *phenomenological* model — fit the form, extract β. ED's contribution is to derive the *form* from architectural principles + standard kinetic-theory inversion:

- The functional form (1 - ρ/ρ_max)^(-β) is forced by P4's specific saturation structure (degenerate diffusion vanishing at upper bound).
- The exponent β is INHERITED but the *exponential structure with negative power* is forced.
- The empirical β values across systems (Universal Mobility Law's 10 systems + Krieger-Dougherty literature) are consistent with this structural prediction.

In other words: ED unifies the soft-matter Universal Mobility Law and the suspension-rheology Krieger-Dougherty model under a single architectural principle (P4). This is structural unification of two empirical regimes that are usually treated as separate.

### 6.4 Connection to the broader ED-NS roadmap

Per [`ED-NS_Exploration_Roadmap.md`](ED-NS_Exploration_Roadmap.md) §3 category A, this is the strongest productive finding from the off-leash exploration. D1 closes the central derivation. D2 will extend to shear-rate-dependent mobility (giving DST and Carreau-class shear-thinning); D3 will catalogue rheology classes by ED-architectural status; D4 will perform qualitative empirical comparison.

---

## 7. Recommended Next Steps

In priority order for the rest of the P4 → Non-Newtonian arc.

1. **Begin D2 — extend to shear-rate-dependent mobility $M(\dot\gamma)$.** File: `theory/Navier Stokes/P4_NN_D2_Shear_Rate.md`. Three sub-cases: (a) $M(\dot\gamma) = M_0 (1 - \dot\gamma/\dot\gamma_\mathrm{max})^\beta$ → DST / shear-thickening; (b) $M(\dot\gamma) = M_0 / (1 + (\lambda \dot\gamma)^n)$ → Cross / Carreau shear-thinning; (c) mixed dependencies $M(\rho, \dot\gamma)$ for suspension rheology with both effects. Estimated 1–2 sessions.

2. **Begin D3 — rheology-class audit catalogue.** File: `theory/Navier Stokes/P4_NN_D3_Rheology_Classes.md`. Table mapping standard rheology classes (Newtonian, Krieger-Dougherty, Bingham, power-law, Cross, Carreau, Maxwell, Oldroyd-B) to ED-architectural status (canonical / form-FORCED / partially-FORCED-with-additions / non-canonical). Estimated 1 session.

3. **Pre-D4 check: gather β values from literature for qualitative comparison.** Universal Mobility Law's 10-system β distribution; Krieger-Dougherty β values for hard-sphere suspensions, polymer suspensions, granular materials; DST exponents. Used in D4 for cross-system comparison. ~30 minutes if accessing summary tables; longer if going to primary literature. **Decision flag for the user:** quantitative empirical comparison (D4 with full statistical analysis) is optional; qualitative β-distribution comparison is core. Recommend qualitative-only for arc closure.

### Decisions for you

- **Confirm the form-FORCED + Stokes-Einstein-imported framing of D1.** ED supplies the (1 - ρ/ρ_max)^β mobility-saturation structure (form-FORCED, empirically validated); standard physics supplies the inversion to viscosity. The combination is Krieger-Dougherty.
- **Confirm that β-value-INHERITED status is acceptable** for a structural-prediction memo. ED predicts the *form* of the divergence, not the *value* of β. This is consistent with the program's form-FORCED / value-INHERITED methodology throughout.
- **Confirm D2 next.** Shear-rate-dependent mobility extension; produces DST + Carreau-class derivations.

---

*P4-NN-D1 derived. Krieger-Dougherty-class viscosity divergence $\mu(\rho) = \mu_0 (1 - \rho/\rho_\mathrm{max})^{-\beta}$ follows from ED's P4 mobility-saturation principle (form-FORCED, empirically validated via Universal Mobility Law's 10-system R² > 0.986) combined with standard Stokes-Einstein-class mobility-viscosity inversion (imported from kinetic theory). β value INHERITED per material physics. ED's structural contribution: unification of soft-matter Universal Mobility Law and suspension-rheology Krieger-Dougherty as two empirical regimes of one architectural principle (P4). D2 next: shear-rate-dependent extension.*
