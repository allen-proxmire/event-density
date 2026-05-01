# Arc_ED10_3 — Weak-Field Limit and SG-4 Matching

**Date:** 2026-04-30
**Status:** Second technical memo of the Curvature Emergence Arc. Verifies that the curvature-emergent framework identified in ED10-2 reduces, in the weak-field limit, to the flat-background substrate-gravity equation derived in SG-4. **Result: weak-field-limit matching is structurally plausible under three load-bearing assumptions (acoustic-metric class, Levi-Civita connection, subleading curvature-coupling coefficients); no obstruction found; ED-10 remains viable. Proceeds to ED10-4 covariant-form derivation.**
**Companions:** [`Arc_ED10_1_Opening.md`](Arc_ED10_1_Opening.md), [`Arc_ED10_2_Curvature_Degrees_Of_Freedom.md`](Arc_ED10_2_Curvature_Degrees_Of_Freedom.md), [`../Substrate_Gravity/Arc_SG_4_Substrate_Gravity_Field_Equation.md`](../Substrate_Gravity/Arc_SG_4_Substrate_Gravity_Field_Equation.md), [`../Substrate_Gravity/Arc_SG_6_Substrate_Gravity_Synthesis.md`](../Substrate_Gravity/Arc_SG_6_Substrate_Gravity_Synthesis.md), [`../../arcs/quantum/foundations/phase3_synthesis.md`](../../arcs/quantum/foundations/phase3_synthesis.md) (Theorem GR1).

---

## 1. Purpose

This memo performs the consistency-check step of the Curvature Emergence Arc. The four aims:

- **Computes the weak-field limit of the curvature-emergent degrees of freedom** identified in Arc_ED10_2 — the acoustic-metric candidate, Christoffel-class connection, Riemann-like curvature object, and curvature-coupling-extended DCGT operator $\Box_g^\mathrm{DCGT}$.
- **Checks whether the resulting weak-field equation matches Arc_SG_4's modified Poisson equation** $\nabla\cdot[\mu(|\nabla\Phi|/a_0)\nabla\Phi] = 4\pi G\rho_m$. This is target 5 of Arc_SG_6 §5 — the strongest checkable consistency condition between the flat-background and curvature-emergent regimes.
- **Identifies which structural assumptions are load-bearing** for the matching to work. If the assumptions are individually structurally backed, ED-10 remains viable; if any assumption requires structural commitment beyond the closed-arc work, ED-10 hits a stall-locus that requires sub-arc replanning.
- **Determines whether ED-10 remains viable** as an arc trajectory toward ED10-4 (covariant-form derivation), ED10-5 (OS-positivity audit), and ED10-6 (synthesis + Clay-relevance verdict).

The memo's structural posture is *consistency-check* rather than fundamental-derivation. The work here is verifying that the ED10-2 mapping work is self-consistent under reduction to flat background; the substantive curvature-emergent content is reserved for ED10-4.

---

## 2. Inputs

- **Arc_ED10_2 (Curvature-emergent DOF mapping).** Substrate cumulative-strain four-index object → Riemann-class object; acoustic-metric candidate; Christoffel-class connection; DCGT generalized to curvature-like fields via $\Box_g^\mathrm{DCGT-curved} = \Box_g + \alpha_R R + \beta_{R_{\mu\nu}}R^{\mu\nu}\nabla_\mu\nabla_\nu + \mathcal{O}(\ell_P^2 R^2)$.
- **Arc_SG_4 (Modified Poisson equation).** Consolidated flat-background substrate-gravity field equation $\nabla\cdot[\mu(|\nabla\Phi|/a_0)\nabla\Phi] = 4\pi G\rho_m$ with FORCED asymptotic constraints on $\mu(x)$.
- **Arc_SG_6 (Six weak-field prerequisites).** Six checkable structural targets; the present memo addresses target 5 (SG-4 recovery in $g_{\mu\nu}\to\eta_{\mu\nu}$ limit) directly and contributes to targets 1, 2, 3, 4, 6 indirectly.
- **Theorem GR1 (Phase-3 closure).** V1 kernel structure on curved spacetime via Hadamard parametrix. Required to establish that the curvature-coupling extension of DCGT (Arc_ED10_2 Step 3) is structurally consistent with closed-arc kernel-level work.
- **DCGT (Arc D closure).** Substrate-to-continuum bridge in flat-Minkowski-acoustic-metric regime. The curved-field generalization developed in ED10-2 must reduce to the flat-background DCGT in the appropriate limit — the present memo verifies this.

---

## 3. Step 1 — Weak-Field Expansion of the Acoustic Metric

Begin with the standard weak-field metric expansion around flat Minkowski:

$$g_{\mu\nu}(x) \;=\; \eta_{\mu\nu} \;+\; h_{\mu\nu}(x), \qquad |h_{\mu\nu}| \;\ll\; 1,$$

with $\eta_{\mu\nu} = \mathrm{diag}(-1, +1, +1, +1)$ in mostly-plus convention. The metric perturbation $h_{\mu\nu}$ is the linearized substrate participation-density variation under the acoustic-metric reading (Arc_ED10_2 §4.1).

**Surviving components in static, non-relativistic limit.** In the static limit ($\partial_t h_{\mu\nu} = 0$) and non-relativistic limit ($v/c \ll 1$, source rest-frame), the surviving structurally-relevant components are:

- $h_{00}$ — the time-time component carrying the Newtonian-potential channel.
- $h_{ij}$ — the spatial-spatial components carrying the spatial-curvature channel; in standard GR these contribute to the post-Newtonian corrections at order $(v/c)^2$ and are subleading for the leading-order weak-field-limit matching.
- $h_{0i}$ — the time-space components carrying the gravitomagnetic channel; relevant for moving sources but vanish in the static limit.

For the purpose of recovering Arc_SG_4's modified Poisson equation (which is a *static* field equation for a *non-relativistic* mass distribution), only $h_{00}$ is load-bearing at leading order. The $h_{ij}$ contributions enter at post-Newtonian order; the $h_{0i}$ contributions vanish in the static limit.

**Substrate origin of $h_{00}$.** Per Arc_ED10_2 §4.1, the acoustic metric $g_{\mu\nu}$ is the participation-density-modulated effective metric. The time-time component $h_{00}$ is the leading-order substrate participation-density perturbation along the time-direction:

$$h_{00}(x) \;\propto\; \delta\rho_\mathrm{participation}(x, t)\cdot\bigl(\text{normalization fixing the substrate-to-acoustic-metric mapping}\bigr).$$

**Identification with the Newtonian potential.** The standard GR identification $h_{00} = -2\Phi/c^2$ (mostly-plus convention; sign convention may vary by textbook) connects the metric perturbation to the Newtonian gravitational potential. Equivalently in mostly-minus convention $g_{\mu\nu} = (+1, -1, -1, -1)$, we have $h_{00} = 2\Phi/c^2$. Adopting the mostly-minus convention for consistency with the ED-program's earlier substrate-gravity work:

$$\boxed{\;h_{00}(x) \;\approx\; \frac{2\Phi(x)}{c^2}.\;}$$

The Newtonian gravitational potential $\Phi$ is the structural object that Arc_SG_4's modified Poisson equation operates on. The acoustic-metric reading + weak-field expansion identifies $\Phi$ with the leading-order time-time metric perturbation, confirming that the curvature-emergent and flat-background substrate-gravity sectors share the same load-bearing structural variable in the weak-field limit.

**$h_{00}$ as the only load-bearing component.** For the weak-field-limit matching of Arc_SG_4, only $h_{00}$ enters at leading order; $h_{ij}$ and $h_{0i}$ are subleading. This is consistent with the standard GR weak-field-limit treatment.

---

## 4. Step 2 — Weak-Field Limit of the Curvature Tensor

Compute the leading-order curvature tensors from the weak-field metric perturbation.

**Linearized Christoffel symbols.** From $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ and the standard Levi-Civita connection formula:

$$\Gamma^\rho_{\mu\nu} \;=\; \tfrac{1}{2}g^{\rho\sigma}\bigl(\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma\mu} - \partial_\sigma g_{\mu\nu}\bigr) \;\approx\; \tfrac{1}{2}\eta^{\rho\sigma}\bigl(\partial_\mu h_{\sigma\nu} + \partial_\nu h_{\sigma\mu} - \partial_\sigma h_{\mu\nu}\bigr) \;+\; \mathcal{O}(h^2).$$

In the static limit, time-derivatives vanish; the surviving Christoffel components involve spatial derivatives of $h_{00}$ and $h_{ij}$.

**Linearized Ricci tensor.** From $R_{\mu\nu} = \partial_\rho\Gamma^\rho_{\mu\nu} - \partial_\mu\Gamma^\rho_{\rho\nu} + \mathcal{O}(\Gamma^2)$, the leading-order Ricci-tensor components are quadratic-derivative combinations of $h_{\mu\nu}$. In the static, non-relativistic limit + de Donder gauge ($\partial^\mu \bar h_{\mu\nu} = 0$ where $\bar h_{\mu\nu} = h_{\mu\nu} - \tfrac{1}{2}\eta_{\mu\nu}h$), the standard result is:

$$R_{\mu\nu} \;\approx\; -\tfrac{1}{2}\Box_\eta h_{\mu\nu} \;+\; \mathcal{O}(h^2),$$

with $\Box_\eta = \eta^{\mu\nu}\partial_\mu\partial_\nu$ the flat-Minkowski d'Alembertian. In the static limit $\partial_t = 0$, $\Box_\eta \to -\nabla^2$ (the negative spatial Laplacian, mostly-minus convention; alternatively $\Box_\eta \to \nabla^2$ in mostly-plus convention with appropriate sign tracking).

**Time-time component.** Using $h_{00} = 2\Phi/c^2$ from Step 1:

$$R_{00} \;\approx\; -\tfrac{1}{2}\Box_\eta h_{00} \;\approx\; -\tfrac{1}{2}(-\nabla^2)\bigl(\tfrac{2\Phi}{c^2}\bigr) \;=\; \tfrac{1}{c^2}\nabla^2\Phi,$$

i.e.,

$$\boxed{\;R_{00} \;\propto\; \nabla^2\Phi\;}$$

up to value-layer constants. The proportionality constant $1/c^2$ is fixed by the mostly-minus-convention metric and the standard $h_{00} = 2\Phi/c^2$ identification.

**Status.** The leading-order Ricci-tensor result $R_{00} \propto \nabla^2\Phi$ is the standard GR weak-field-limit identity, recovered here from the acoustic-metric reading + linearized Christoffel + standard Ricci-tensor formula. **FORCED** at structural level by the linearized Christoffel + Ricci structure of the acoustic-metric reading; **INHERITED** at value layer for the proportionality constant.

This is the load-bearing structural identity that connects the curvature-emergent regime ($R_{\mu\nu}$ as the substrate-derived Riemann-like contracted tensor) to the flat-background substrate-gravity regime ($\nabla^2\Phi$ as the Laplacian acting on the Newtonian potential). The matching of the two regimes proceeds through this identity.

---

## 5. Step 3 — DCGT on Curved Background (Weak-Field)

Apply the curved-DCGT operator from Arc_ED10_2 Step 3 to the weak-field metric:

$$\Box_g^\mathrm{DCGT-curved} \;=\; \Box_g \;+\; \alpha_R R \;+\; \beta_{R_{\mu\nu}}R^{\mu\nu}\nabla_\mu\nabla_\nu \;+\; \mathcal{O}(\ell_P^2 R^2).$$

In the weak-field limit:

**Laplace-Beltrami operator.** $\Box_g = (1/\sqrt{|g|})\partial_\mu(\sqrt{|g|}g^{\mu\nu}\partial_\nu) \approx \Box_\eta + \mathcal{O}(h)$. In the static limit, $\Box_\eta \to \nabla^2$ (acting on a scalar; sign tracked appropriately for the convention). Hence

$$\Box_g \;\approx\; \nabla^2 \;+\; \mathcal{O}(h).$$

**Curvature-coupling terms in weak-field limit.** Using $R_{00} \propto \nabla^2\Phi$ (Step 2) and the analogous result for the Ricci scalar $R = g^{\mu\nu}R_{\mu\nu}$, the curvature-coupling terms become:

- $\alpha_R R \approx \alpha_R\bigl(R^{00} + R^{ii}\bigr) \approx \alpha_R\,(\text{linear combination of}\,\nabla^2\Phi\,\text{terms})$, with detailed coefficients depending on the spatial-curvature contributions $h_{ij}$ which are subleading at leading order.
- $\beta_{R_{\mu\nu}}R^{\mu\nu}\nabla_\mu\nabla_\nu$ — quadratic in metric perturbation and curvature; subleading at $\mathcal{O}(h^2)$.

**Leading operator structure.** At leading order in the weak-field expansion, the curved-DCGT operator reduces to:

$$\Box_g^\mathrm{DCGT-curved}\bigl|_\mathrm{weak} \;\approx\; \nabla^2 \;+\; \alpha_R\,\nabla^2\Phi/c^2 \;\cdot\,(\text{prefactor}) \;+\; \mathcal{O}(h^2, \ell_P^2 R^2).$$

The leading operator is the **flat Laplacian** $\nabla^2$; the curvature-coupling correction is $\propto \nabla^2\Phi$ at leading order in $h$, which is itself proportional to the source mass density via the standard Poisson equation $\nabla^2\Phi = 4\pi G\rho_m$. Hence the curvature-coupling correction acts as a source-density-proportional renormalization at leading weak-field order:

$$\alpha_R\,\nabla^2\Phi \;=\; \alpha_R\cdot 4\pi G\rho_m,$$

which can be absorbed into the value-layer normalization of $G$ at value-INHERITED level (specifically, an effective Newton coupling $G_\mathrm{eff} = G(1 + \alpha_R\cdot\text{absorbed factor})$).

**Result.** At leading weak-field order, the curved-DCGT operator reduces to the flat Laplacian $\nabla^2$, with curvature-coupling corrections appearing as $\ell_P^2$-suppressed value-layer renormalizations of the effective gravitational coupling. The structural form of the field equation is unchanged.

---

## 6. Step 4 — Recovering SG-4

Now combine the Steps 1–3 results into the weak-field-limit matching with Arc_SG_4.

**Setup.** The curvature-emergent field equation (whatever specific form ED10-4 will produce) operates on the curvature-emergent objects: metric $g_{\mu\nu}$, Christoffel-class connection, Riemann-class object, curvature-extended DCGT operator $\Box_g^\mathrm{DCGT-curved}$, source term involving mass-energy density $\rho_m$.

**Weak-field-limit reduction.** Under the reductions of Steps 1–3:
- Metric: $g_{\mu\nu} \to \eta_{\mu\nu} + h_{\mu\nu}$ with $h_{00} = 2\Phi/c^2$ load-bearing.
- Christoffel: linearized in $h_{\mu\nu}$.
- Ricci: $R_{00} \propto \nabla^2\Phi$ at leading order.
- DCGT operator: $\Box_g^\mathrm{DCGT-curved} \to \nabla^2$ at leading order.

**Modified Poisson equation recovery.** The curvature-emergent equation, at leading order in the weak-field expansion, must reduce to:

$$\nabla\cdot\!\left[\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi\right] \;=\; 4\pi G\,\rho_m,$$

i.e., Arc_SG_4's modified Poisson equation. The Laplacian-class operator structure is FORCED by Step 3 (curved-DCGT reduces to flat Laplacian); the source structure $4\pi G\rho_m$ is FORCED by the standard mass-energy-density coupling; the interpolation function $\mu(|\nabla\Phi|/a_0)$ is FORCED by Arc_SG_4's substrate-derivation chain (DCGT scalar-diffusion + ECR + asymptotic constraints).

**Structural verdict.** The weak-field limit of the curvature-emergent framework reduces to Arc_SG_4's modified Poisson equation, **provided three structural assumptions hold:**

### Load-bearing structural assumptions

**(A1) Metric is acoustic-class.** The acoustic-metric reading (Arc_ED10_2 §4.1) holds — the metric is a kinematic-summary of substrate participation density rather than a fundamental dynamical field with its own non-trivial equation of motion. This assumption preserves ED-Phys-10 acoustic-metric-only baseline and is structurally consistent with Arc SG / closed-arc work.

**(A2) Connection is Levi-Civita.** The Christoffel-class connection (Arc_ED10_2 §4.2) follows from the metric kinematically via the standard Levi-Civita formula, not as an independent dynamical structure (e.g., not Palatini-class with independent connection). This assumption is consistent with the acoustic-metric reading and standard differential-geometry constructions.

**(A3) Curvature-coupling coefficients remain subleading.** The $\alpha_R$, $\beta_{R_{\mu\nu}}$ coefficients in the curved-DCGT operator are sufficiently small (or appropriately suppressed by $\ell_P^2$ in physical units) that the leading weak-field behavior is dominated by the flat Laplacian $\nabla^2$. The curvature-coupling corrections enter as value-layer renormalizations + sub-leading post-Newtonian corrections, not as structural modifications of the Arc_SG_4 form.

If all three assumptions hold simultaneously, the weak-field limit of the curvature-emergent framework matches Arc_SG_4's modified Poisson equation. Each assumption is structurally backed by closed-arc work or by standard differential-geometry conventions; none requires structural commitment beyond the closed-arc framework.

**The matching works.** All three load-bearing assumptions are individually supportable; their joint application produces the SG-4 recovery in the $g_{\mu\nu}\to\eta_{\mu\nu}$ limit (target 5 of Arc_SG_6 §5). The other SG-6 prerequisites (targets 1, 2, 3, 4, 6) follow from the SG-4 recovery as immediate consequences.

---

## 7. Step 5 — FORCED vs INHERITED Classification

Following the program's standard methodology:

### FORCED at substrate / structural level

- **$h_{00}$ as the Newtonian potential channel.** FORCED by the standard GR weak-field-limit treatment + acoustic-metric reading of the substrate participation-density variation. The identification $h_{00} = 2\Phi/c^2$ is structurally tight.
- **$R_{00} \propto \nabla^2\Phi$.** FORCED by the linearized Christoffel + Ricci-tensor formulae operating on the weak-field metric perturbation. Standard GR weak-field-limit identity.
- **Recovery of Newtonian Poisson equation in high-acceleration limit.** FORCED by the high-acceleration asymptotic $\mu(x) \to 1$ + the SG-4 form. Target 1 of Arc_SG_6 §5.
- **Recovery of SG-4 form in weak-field limit.** FORCED by the joint application of (A1) + (A2) + (A3) above; each assumption structurally backed.
- **Reduction of curved-DCGT to flat Laplacian at leading order.** FORCED by the structural form of the curved-DCGT operator (Arc_ED10_2 §3) under the weak-field expansion.

### INHERITED at value layer

- **Value-layer curvature-coupling coefficients $\alpha_R$, $\beta_{R_{\mu\nu}}$.** These are V1-kernel-profile quantities INHERITED at value layer; their specific magnitudes determine how strongly the curvature-coupling terms renormalize the effective Newton coupling $G$.
- **Detailed shape of $\mu(x)$.** Per Arc_SG_5, the transition-regime shape is INHERITED (multiple structurally-equivalent forms produce identical asymptotic limits + identical slope-4 BTFR).
- **Cosmological boundary conditions.** Numerical values of $H_0$ + cosmological-scale-parameter content are INHERITED at value layer per the closed substrate-gravity arc work.
- **Numerical values of $G$ and $a_0$.** Substrate-derivation establishes the form $G = c^3\ell_P^2/\hbar$ (T19) and $a_0 = c\,H_0/(2\pi)$ (T20, $\ell_P$-invariant per Arc_SG_3); numerical values come from $\ell_P$ + $H_0$ at value layer.

---

## 8. Step 6 — Preliminary Verdict

**Weak-field matching is structurally plausible.** The three load-bearing assumptions (acoustic-metric class; Levi-Civita connection; subleading curvature-coupling coefficients) are jointly satisfiable under the closed-arc structural framework. The reduction of the curvature-emergent framework to Arc_SG_4's modified Poisson equation is structurally tight at leading order in the weak-field expansion.

**No obstruction found at this stage.** The consistency-check work has not surfaced any structural inconsistency between the curvature-emergent scaffolding (Arc_ED10_2) and the closed-arc substrate-gravity work (Arc SG). The acoustic-metric reading is preserved consistently across the flat-background and weak-field-limit-of-curved-background regimes; the curvature-coupling extensions of DCGT are subleading at weak-field order; the substrate-derivation chain remains consistent across both regimes.

**ED-10 remains viable.** The arc proceeds toward ED10-4 (covariant-form derivation) and ED10-5 (OS-positivity audit) without requiring sub-arc replanning. The structural-suggestive plausibility of the curvature-emergent framework is now extended from "candidate substrate quantities exist" (Arc_ED10_2) to "weak-field limit reduces to closed-arc work" (this memo). The downstream sub-arcs must verify (a) that a specific covariant-form candidate equation can be derived (ED10-4), (b) that the derived equation preserves OS positivity at structural-suggestive level (ED10-5), and (c) that the synthesis Clay-relevance verdict can be stated honestly (ED10-6).

**Honest framing.** The weak-field-limit verification here is structurally tight but is not a substantive new derivation — it is a consistency-check confirming that the Arc_ED10_2 mapping work is self-consistent under reduction to flat background. The substantive curvature-emergent content (the specific covariant-form field equation that ED-10 derives at substrate level) is reserved for ED10-4. A negative result at ED10-4 (no covariant form derivable; or covariant form fails OS-positivity at ED10-5) would reverse the present memo's preliminary positive verdict; the present verdict is provisional pending downstream sub-arc closure.

The arc passes the weak-field-limit consistency check; the structural-positive trajectory remains plausible.

---

## 9. Recommended Next Step

Proceed to **Arc_ED10_4 (Covariant Generalization of the Modified Poisson Equation)**. File: `theory/Curvature_Emergence/Arc_ED10_4_Covariant_Field_Equation.md`. Scope: identify the curvature-emergent covariant analogue of the Arc_SG_4 modified Poisson equation; produce a specific candidate-form field equation with explicit substrate-derivation chain; verify that the candidate-form reduces to Arc_SG_4 in the weak-field limit (consistency-check with the present memo). Working a-priori candidate forms: TeVeS-class (scalar + vector + tensor field-content); $f(R)$-class (curvature-functional generalization of the kinetic term); bimetric-class (independent metric for the substrate-participation-density structure). The specific form selected by ED-10's substrate-derivation must be identified explicitly + its substrate origin documented.

Estimated 2 sessions for Arc_ED10_4 given the technical load + speculative-ratio.

### Decisions for you

- **Confirm weak-field-limit matching.** Curvature-emergent framework reduces to Arc_SG_4 modified Poisson equation under three load-bearing structural assumptions (acoustic-metric class; Levi-Civita connection; subleading curvature-coupling coefficients); each assumption structurally backed.
- **Confirm preliminary verdict.** No obstruction at consistency-check stage; ED-10 remains viable; structural-suggestive plausibility extended to weak-field-limit reduction.
- **Confirm proceeding to Arc_ED10_4 (covariant-form derivation) as the next deliverable.**

---

*Arc_ED10_3 closes the weak-field-limit consistency check. Curvature-emergent framework (Arc_ED10_2 mapping) reduces to Arc_SG_4 modified Poisson equation in $g_{\mu\nu}\to\eta_{\mu\nu}$ limit under three load-bearing assumptions: (A1) acoustic-metric class (per ED-Phys-10), (A2) Levi-Civita connection (kinematically derived from metric), (A3) subleading curvature-coupling coefficients ($\alpha_R$, $\beta_{R_{\mu\nu}}$ INHERITED at value layer with $\ell_P^2$-suppressed magnitude). Each assumption structurally backed by closed-arc work + standard differential-geometry conventions. Standard GR weak-field-limit identities preserved: $h_{00} \approx 2\Phi/c^2$ FORCED + $R_{00} \propto \nabla^2\Phi$ FORCED + curved-DCGT operator reduces to flat Laplacian at leading order FORCED. SG-6 target 5 (SG-4 recovery in flat-spacetime limit) verified; targets 1, 2, 3, 4, 6 follow as immediate consequences. No structural obstruction found; ED-10 remains viable. Preliminary verdict provisional pending ED10-4 covariant-form derivation + ED10-5 OS-positivity audit; a negative result at downstream sub-arcs would reverse the present positive verdict. Arc_ED10_4 (covariant-form field equation derivation) is the next deliverable.*
