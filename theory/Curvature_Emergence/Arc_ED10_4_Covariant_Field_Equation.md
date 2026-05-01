# Arc_ED10_4 — Covariant Generalization of the Modified Poisson Equation

**Date:** 2026-04-30
**Status:** Third technical memo of the Curvature Emergence Arc. Derives a substrate-grounded covariant generalization of the Arc_SG_4 modified Poisson equation using the curvature-emergent degrees of freedom from ED10-2 and the weak-field constraints from ED10-3. **Result: a scalar-tensor acoustic-metric-class covariant equation is the only structural-derivation candidate compatible with substrate rules; TeVeS-class scalar-tensor form FORCED at structural level; bimetric-class collapses to it under acoustic-metric identification; $f(R)$-class violates ED-Phys-10 by requiring new curvature degrees of freedom. ED-10 remains viable; covariant candidate is structurally consistent; proceeds to ED10-5 OS-positivity audit.**
**Companions:** [`Arc_ED10_1_Opening.md`](Arc_ED10_1_Opening.md), [`Arc_ED10_2_Curvature_Degrees_Of_Freedom.md`](Arc_ED10_2_Curvature_Degrees_Of_Freedom.md), [`Arc_ED10_3_Weak_Field_Limit.md`](Arc_ED10_3_Weak_Field_Limit.md), [`../Substrate_Gravity/Arc_SG_4_Substrate_Gravity_Field_Equation.md`](../Substrate_Gravity/Arc_SG_4_Substrate_Gravity_Field_Equation.md), [`../Substrate_Gravity/Arc_SG_6_Substrate_Gravity_Synthesis.md`](../Substrate_Gravity/Arc_SG_6_Substrate_Gravity_Synthesis.md), [`../../arcs/quantum/foundations/phase3_synthesis.md`](../../arcs/quantum/foundations/phase3_synthesis.md) (Theorem GR1).

---

## 1. Purpose

This memo performs the substantive derivation step of the Curvature Emergence Arc — the load-bearing question of whether ED-10 produces a substrate-derived covariant field equation at all. Specifically:

- **Proposes a covariant field equation whose weak-field limit reduces to Arc_SG_4's modified Poisson equation.** Per Arc_ED10_3 §6, three load-bearing assumptions (acoustic-metric class, Levi-Civita connection, subleading curvature-coupling coefficients) must hold; the present memo selects from candidate covariant forms compatible with these assumptions.
- **Identifies which covariant structures are FORCED by the substrate.** Following the program's standard form-FORCED / value-INHERITED methodology, classify which features of the candidate covariant equation are FORCED at substrate level vs. INHERITED at value layer.
- **Distinguishes between three structural-family candidates.** TeVeS-class (scalar-tensor with extra scalar field carrying the modified-Poisson dynamics), $f(R)$-class (curvature-functional generalization of the Einstein-Hilbert kinetic term), and bimetric-class (independent metric for the substrate-participation-density structure). Audit each for substrate-derivation compatibility.
- **Determines whether a substrate-derived covariant form exists at all.** If no candidate-family is compatible with substrate rules, ED-10 hits a stall-locus at the covariant-form derivation step. If exactly one candidate-family is compatible, the substrate FORCES that family. Working a-priori (per Arc_ED10_3 verdict): exactly one family — scalar-tensor acoustic-metric — is compatible.

The memo's structural posture is *candidate-form selection* rather than full Lagrangian derivation. The candidate equation supplies a starting point for ED10-5's OS-positivity audit; specific Lagrangian / action-functional details + variational formulation are reserved for further work if the present candidate passes ED10-5.

---

## 2. Inputs

- **Arc_ED10_2 (Curvature-emergent DOF mapping).** Substrate cumulative-strain four-index → Riemann-class object; acoustic-metric candidate; Christoffel-class connection; DCGT generalized to curvature-like fields via $\Box_g^\mathrm{DCGT-curved}$.
- **Arc_ED10_3 (Weak-field-limit matching).** Three load-bearing structural assumptions for SG-4 recovery: (A1) acoustic-metric class; (A2) Levi-Civita connection; (A3) subleading curvature-coupling coefficients.
- **Arc_SG_4 (Modified Poisson equation).** Flat-background substrate-gravity field equation $\nabla\cdot[\mu(|\nabla\Phi|/a_0)\nabla\Phi] = 4\pi G\rho_m$ with FORCED asymptotic constraints.
- **Arc_SG_6 (Six weak-field prerequisites).** Targets 1–6: Newtonian Poisson recovery, modified Poisson recovery with $\mu$ asymptotics, BTFR slope-4, $a_0$ horizon-scale invariance, SG-4 recovery in flat-spacetime limit, GR1 generalization.
- **Theorem GR1 (Phase-3 closure).** V1 kernel structure on curved spacetime. The candidate covariant form must reduce to GR1 at the kernel level.
- **DCGT (Arc D closure).** Substrate-to-continuum coarse-graining methodology, generalized to curvature-like fields per Arc_ED10_2 §3.

---

## 3. Step 1 — Covariantization Strategy

The covariant generalization of Arc_SG_4 must satisfy five structural requirements:

**(R1) Must reduce to SG-4 in the static weak-field limit.** Per Arc_ED10_3, the weak-field reduction $g_{\mu\nu} \to \eta_{\mu\nu} + h_{\mu\nu}$ with $h_{00} = 2\Phi/c^2$ must produce $\nabla\cdot[\mu(|\nabla\Phi|/a_0)\nabla\Phi] = 4\pi G\rho_m$ at leading order.

**(R2) Must preserve $a_0$ as horizon-scale invariant.** Per Arc_SG_3, $a_0 = c\,H_0/(2\pi)$ is $\ell_P$-invariant under the continuum limit; its substrate origin is cosmological-horizon participation density. The covariant equation must preserve this horizon-scale anchoring; the covariant analogue of $|\nabla\Phi|/a_0$ must remain a substrate-derived dimensionless quantity with cosmological-horizon-anchored normalization.

**(R3) Must preserve BTFR slope-4 in the deep-MOND regime.** Per Arc_SG_5, slope-4 is robust under all admissible variations within the structural-derivation framework. The covariant equation's deep-MOND limit must inherit this robustness.

**(R4) Must use only curvature-emergent degrees of freedom (no new primitives).** Per Arc_ED10_1 non-goals + Arc SG closure: no primitive amendments. The covariant equation must operate entirely on substrate-derived structural quantities — metric, connection, curvature, scalar potential $\Phi$, mass-energy density / stress-energy tensor — with no additional fields beyond those present in the closed substrate-derivation framework.

**(R5) Must remain acoustic-metric-class (ED-Phys-10 guardrail).** Per ED-Phys-10 + closed substrate-gravity arc: the metric is kinematic-summary of substrate participation density rather than fundamental dynamical field. The covariant equation must respect this status; deviating into dynamical-metric-as-fundamental-field territory would break ED-Phys-10 + require explicit user-decision on whether to revise the guardrail.

These five constraints jointly eliminate many naive covariantizations. Specifically, any candidate that (a) introduces dynamical metric content with an Einstein-Hilbert-class kinetic term (violates R5), (b) modifies the gravitational-coupling structure at fundamental level (likely to violate R1 in the weak-field limit), (c) introduces additional scalar / vector / tensor fields beyond the substrate-derived $\Phi$ + acoustic metric (violates R4), or (d) modifies the $\mu(x)$ asymptotic constraints away from $\mu \to 1$ + $\mu \to x$ (violates R1, R3) is structurally inadmissible.

The candidate-form selection in Step 2 is restricted to forms compatible with all five constraints jointly.

---

## 4. Step 2 — Candidate Covariant Forms

Three structural families are commonly identified in the standard MOND-covariantization literature. Each is audited against the five constraints from Step 1.

### (A) TeVeS-class scalar-tensor form

In its scalar-tensor minimal form (sometimes called RAQUAL — Relativistic A QUAdratic Lagrangian — or scalar-MOND), the field equation for the gravitational potential $\Phi$ (a scalar field on curved background) is:

$$\nabla_\mu\!\left[\mu\!\left(\frac{\sqrt{g^{\alpha\beta}\nabla_\alpha\Phi\,\nabla_\beta\Phi}}{a_0}\right)\nabla^\mu\Phi\right] \;=\; 4\pi G\,T,$$

with $\nabla_\mu$ the metric-covariant derivative, $g^{\alpha\beta}\nabla_\alpha\Phi\nabla_\beta\Phi$ the squared-magnitude-of-gradient covariant scalar (the covariant analogue of $|\nabla\Phi|^2$), $\mu(x)$ the interpolation function with the same asymptotic constraints as in Arc_SG_4, and $T$ a covariant scalar source related to the trace of the matter stress-energy tensor (typically $T = T^\mu_\mu$ or $T = T^{00}/c^2$ depending on convention).

**Note on naming.** Bekenstein's full TeVeS theory (Tensor-Vector-Scalar) involves a scalar field + a vector field + a tensor field as independent dynamical degrees of freedom. The form above is a *scalar-tensor reduced* version with only the scalar field $\Phi$ + acoustic-metric (no independent vector field). For the present substrate-derivation purposes, the scalar-tensor reduced form is the substrate-compatible candidate; the full TeVeS theory introduces an independent vector field that would violate constraint (R4). We use "TeVeS-class" loosely to refer to the scalar-tensor reduced form.

**Constraint check:**
- (R1) Weak-field reduction: $g_{\mu\nu} \to \eta_{\mu\nu}$, $\nabla_\mu \to \partial_\mu$, $g^{\alpha\beta}\nabla_\alpha\Phi\nabla_\beta\Phi \to \delta^{ij}\partial_i\Phi\partial_j\Phi = |\nabla\Phi|^2$ (in the static limit), $T \to \rho_m$. Result: $\nabla\cdot[\mu(|\nabla\Phi|/a_0)\nabla\Phi] = 4\pi G\rho_m$, exactly Arc_SG_4. ✓
- (R2) $a_0$ remains the substrate-derived dimensionful constant from T20; the covariant argument $\sqrt{g^{\alpha\beta}\nabla_\alpha\Phi\nabla_\beta\Phi}$ has the right dimensions and reduces to $|\nabla\Phi|$ in flat spacetime; horizon-scale anchoring preserved. ✓
- (R3) Deep-MOND limit + spherical symmetry + circular-orbit balance (parallel to Arc_SG_4 §5) recovers slope-4. ✓
- (R4) Uses only substrate-derived quantities (acoustic metric + scalar $\Phi$). ✓
- (R5) Metric is acoustic-class kinematic-summary; not dynamical fundamental. ✓

**TeVeS-class scalar-tensor form passes all five constraints.**

### (B) $f(R)$-class curvature-modified form

In its standard form, $f(R)$ gravity replaces the Einstein-Hilbert kinetic term with a non-linear curvature-functional:

$$f_R\,R_{\mu\nu} \;-\; \tfrac{1}{2}f\,g_{\mu\nu} \;+\; (\text{higher-derivative terms involving }\nabla_\mu\nabla_\nu f_R) \;=\; 8\pi G\,T_{\mu\nu},$$

with $f(R)$ a non-linear function of the Ricci scalar $R$, $f_R = df/dR$. The field equation introduces additional scalar-like degrees of freedom via the higher-derivative content (the so-called "scalaron" mode in $f(R)$ gravity).

**Constraint check:**
- (R1) Weak-field reduction can in principle reproduce Newton + MOND-class behavior under specific $f(R)$ choices, but the natural weak-field limit produces post-Newtonian corrections governed by the scalaron rather than the SG-4 modified Poisson equation. The reduction is non-trivial and would require fitting $f(R)$ phenomenologically.
- (R2) $a_0$ would have to be incorporated as a dimensionful scale in $f(R)$; $\ell_P$-invariance is not natural in this form.
- (R3) BTFR slope-4 in deep-MOND would have to be inherited via a specific phenomenological $f(R)$ choice; not robust.
- (R4) **Violates (R4):** the scalaron is an independent curvature degree of freedom that does not arise from the substrate-derivation framework; requires either a primitive amendment or absorption into existing substrate quantities (which is not natural at substrate level).
- (R5) **Violates (R5):** $f(R)$ gravity treats the metric as a fundamental dynamical field with an Einstein-Hilbert-class kinetic term + curvature-functional modification. The metric is no longer acoustic-class kinematic-summary; it is independently dynamical via the $f(R)$ field equation. ED-Phys-10 baseline broken.

**$f(R)$-class form fails constraints (R4) and (R5).** Inadmissible at substrate-derivation level without primitive amendment.

### (C) Bimetric-class form

In the bimetric class, the gravitational dynamics involves two metrics: a "physical" metric $g_{\mu\nu}$ that couples to matter, and an independent "fiducial" metric $\tilde g_{\mu\nu}$ that supplies the geometric-dynamical content. The substrate-derivation analogue is to identify $g_{\mu\nu}^\mathrm{physical} = g_{\mu\nu}^\mathrm{acoustic}(\rho_\mathrm{participation})$ as the acoustic metric per Arc_ED10_2, with the fiducial metric playing the role of the underlying flat Minkowski reference. The field equation then takes a form similar to the TeVeS-class form (A):

$$\nabla_\mu\!\left[\mu\!\left(\frac{\sqrt{g^{\alpha\beta}\nabla_\alpha\Phi\,\nabla_\beta\Phi}}{a_0}\right)\nabla^\mu\Phi\right] \;=\; 4\pi G\,T \quad\text{with}\quad g_{\mu\nu} \;=\; g_{\mu\nu}^\mathrm{acoustic}(\rho_\mathrm{part}).$$

**Constraint check:**
- (R1) Weak-field reduction parallels (A) once the acoustic-metric identification is made. ✓
- (R2) $a_0$ horizon-scale anchoring preserved. ✓
- (R3) BTFR slope-4 inherited from (A) under acoustic-metric identification. ✓
- (R4) Uses only substrate-derived quantities. ✓
- (R5) Acoustic-metric reading preserved via $g_{\mu\nu} = g_{\mu\nu}^\mathrm{acoustic}(\rho_\mathrm{part})$; the bimetric structure is *not* introducing an independent dynamical fiducial metric — it's identifying the physical metric with the substrate-derived acoustic metric. Bimetric-class **collapses to TeVeS-class** under acoustic-metric identification.

**Bimetric-class form is structurally equivalent to TeVeS-class** under the acoustic-metric reading. It is not a structurally distinct candidate.

### Summary of candidate-form audit

| Family | (R1) Weak-field | (R2) $a_0$ | (R3) BTFR | (R4) No new primitives | (R5) Acoustic-metric | Verdict |
|---|---|---|---|---|---|---|
| **(A) TeVeS-class scalar-tensor** | ✓ | ✓ | ✓ | ✓ | ✓ | **Compatible** |
| **(B) $f(R)$-class** | partial | not natural | non-robust | ✗ (scalaron) | ✗ (dynamical metric) | **Inadmissible** |
| **(C) Bimetric-class** | ✓ | ✓ | ✓ | ✓ | ✓ | **Equivalent to (A)** |

Only (A) — the TeVeS-class scalar-tensor form (in its scalar-tensor reduced version) — survives all five constraints and is structurally distinct from inadmissible forms.

---

## 5. Step 3 — Substrate-Derivation Constraints

The Step 2 audit shows:

**(C1) The scalar-tensor TeVeS-class form is the only candidate whose weak-field limit *exactly* reproduces SG-4** at leading order. The reduction $g_{\mu\nu} \to \eta_{\mu\nu}$, $\nabla_\mu \to \partial_\mu$ produces Arc_SG_4's modified Poisson equation directly, without phenomenological fitting or non-trivial coefficient adjustment.

**(C2) The bimetric-class form collapses to TeVeS-class** under acoustic-metric identification. Bimetric is not structurally distinct; the acoustic-metric reading absorbs the bimetric fiducial-metric structure into the substrate-derived acoustic metric. There is one structural-derivation candidate, not three.

**(C3) $f(R)$-class forms violate ED-Phys-10 acoustic-metric guardrail** by introducing dynamical metric content + scalaron-class new curvature degrees of freedom. The $f(R)$ family requires either a primitive amendment (introducing the scalaron as an independent substrate degree of freedom) or absorption into existing substrate quantities (which is not natural). Either route is inadmissible per Arc_ED10_1 non-goals.

**Therefore the substrate FORCES a scalar-tensor acoustic-metric covariantization.** This is the structural verdict of the candidate-form selection: ED-10's covariant generalization of Arc_SG_4 is uniquely identified at the structural-form level as the scalar-tensor TeVeS-class equation.

**Honest framing.** This conclusion is a *substrate-derivation constraint result*, not an independent ED prediction of TeVeS / scalar-tensor MOND. The scalar-tensor MOND-class covariantization has been extensively studied in the standard MOND literature (Bekenstein, Sanders, Milgrom, and others); the ED-program-specific contribution at this stage is the *substrate-derivation chain* identifying which of the standard candidate families is compatible with substrate rules. Originality lies in the substrate-grounding of the form-selection, not in the form itself.

---

## 6. Step 4 — Proposed Covariant Field Equation

Based on the candidate-form audit + substrate-derivation constraints, the proposed substrate-derived covariant generalization of Arc_SG_4 is:

$$\boxed{\;\nabla_\mu\!\left[\mu\!\left(\frac{\sqrt{g^{\alpha\beta}\nabla_\alpha\Phi\,\nabla_\beta\Phi}}{a_0}\right)\nabla^\mu\Phi\right] \;=\; 4\pi G\,T,\;}$$

with:

- **$g_{\mu\nu}$** the acoustic metric from Arc_ED10_2 — kinematic-summary of substrate participation-density variation per ED-Phys-10 baseline.
- **$\nabla_\mu$** the metric-covariant derivative associated with the Levi-Civita connection of $g_{\mu\nu}$ (per Arc_ED10_3 assumption A2).
- **$\mu(x)$** the dimensionless interpolation function satisfying the asymptotic constraints from Arc_SG_4 ($\mu(x) \to 1$ as $x \to \infty$, $\mu(x) \to x$ as $x \to 0$).
- **$T$** the trace of the matter stress-energy tensor (or the time-time component $T^{00}/c^2$ in the static limit), serving as the covariant scalar source.
- **$a_0 = c\,H_0/(2\pi)$** the substrate-derived transition acceleration (T20, $\ell_P$-invariant per Arc_SG_3).
- **$G = c^3\ell_P^2/\hbar$** the substrate-derived gravitational coupling (T19).

**Honest disclaimers.**

- **This is not GR.** The equation is not Einstein's $G_{\mu\nu} = 8\pi G T_{\mu\nu}$. There is no Einstein-Hilbert kinetic term for the metric; the metric is acoustic-class kinematic, not fundamental dynamical. The equation is a substrate-derived covariant generalization of the modified Poisson equation, not a substrate-derivation of general relativity.
- **It is a substrate-derived covariant generalization of SG-4.** The structural origin is the acoustic-metric reading + scalar-tensor structure + Arc_SG_4 modified-Poisson form lifted to curved background. The substrate-derivation chain runs through ED10-2 (DOF mapping) + ED10-3 (weak-field consistency check) + Arc SG (closed flat-background substrate-gravity work).
- **The candidate form is structural-suggestive, not structural-positive.** The present memo identifies the candidate; ED10-5 must verify OS-positivity preservation; ED10-6 must produce the synthesis Clay-relevance-style verdict. The structural-positive content depends on downstream sub-arc closure.

**Relation to standard MOND-covariantization literature.** The proposed form is structurally equivalent to RAQUAL / scalar-tensor MOND covariantizations studied since Bekenstein-Milgrom 1984 and refined in subsequent work. The ED-program-specific contribution is the substrate-derivation chain identifying the form as substrate-FORCED rather than phenomenologically chosen.

---

## 7. Step 5 — FORCED vs INHERITED Classification

Following the program's standard methodology:

### FORCED at substrate level

- **Scalar-tensor structure.** FORCED by the candidate-form audit (Step 2) + substrate-derivation constraints (Step 3): the scalar-tensor TeVeS-class form is the only candidate compatible with all five constraints; bimetric collapses to it; $f(R)$ violates ED-Phys-10.
- **Acoustic metric** $g_{\mu\nu} = g_{\mu\nu}^\mathrm{acoustic}(\rho_\mathrm{part})$. FORCED by ED-Phys-10 acoustic-metric guardrail + Arc_ED10_2 §4.1 substrate-derivation chain.
- **Covariant divergence form** $\nabla_\mu[\mu(\cdot)\nabla^\mu\Phi]$. FORCED by the natural covariantization of Arc_SG_4's modified-Poisson form under the metric-covariant derivative + the acoustic-metric reading.
- **$\mu(x)$ asymptotic constraints** ($\mu \to 1$ at high acceleration, $\mu \to x$ at low acceleration). FORCED by the Arc_SG_4 substrate-derivation + ECR substrate-level composition; preserved under covariantization.
- **Weak-field reduction to SG-4.** FORCED by the candidate-form construction (verified in Arc_ED10_3 + present memo Step 2 (R1)).

### INHERITED at value layer

- **Detailed shape of $\mu(x)$** in the transition regime. Multiple structurally-equivalent forms; specific selection empirical (per Arc_SG_5).
- **Value-layer curvature-coupling coefficients** $\alpha_R$, $\beta_{R_{\mu\nu}}$ from the curved-DCGT operator (Arc_ED10_2 §3). The covariant equation here does not explicitly include these terms at leading order (assumption A3 of Arc_ED10_3); their inclusion at sub-leading order would produce post-Newtonian corrections that are out of scope at present.
- **Cosmological boundary conditions.** Numerical values of $H_0$ + cosmological-scale parameters INHERITED at value layer.
- **Numerical values of $G$ and $a_0$.** Substrate-derivation establishes the form; numerical values come from $\ell_P$ + $H_0$ at value layer.

---

## 8. Step 6 — Preliminary Verdict

**A structurally consistent covariant generalization exists.** The substrate-derivation chain identifies a unique candidate-form (scalar-tensor acoustic-metric class) satisfying all five constraints (R1)–(R5) + reducing exactly to Arc_SG_4 in the weak-field limit + preserving the SG-6 prerequisites + remaining within ED-Phys-10 baseline.

**It is scalar-tensor acoustic-metric class.** Structurally equivalent to RAQUAL / scalar-tensor MOND covariantizations in the standard literature. The ED-program-specific contribution is the substrate-derivation chain identifying this form as substrate-FORCED.

**No new primitives required.** The candidate operates entirely on substrate-derived quantities: acoustic metric (Arc_ED10_2), Levi-Civita connection (kinematically derived), scalar $\Phi$ (Newtonian-potential channel from weak-field expansion), mass-energy density / stress-energy trace $T$ (matter-sector content). Closed-arc structural framework preserved.

**ED-10 remains viable and proceeds to OS-positivity audit.** The candidate form is structurally consistent at the candidate-selection level + the weak-field-consistency level. The downstream ED10-5 audit must verify that the candidate preserves OS positivity at structural-suggestive level under Euclidean continuation; ED10-6 must produce the synthesis Clay-relevance-style verdict.

**Honest framing preserved.** The present memo does not claim a novel covariant gravity theory. It claims that the standard scalar-tensor MOND-class covariantization is the substrate-FORCED form under ED's structural framework. The structural-positive content depends on downstream sub-arc closure; a negative result at ED10-5 (OS-positivity failure) would reverse the present positive verdict.

The arc passes the candidate-form selection step. ED-10's structural trajectory toward a Clay-relevance-style synthesis verdict remains plausible.

---

## 9. Recommended Next Step

Proceed to **Arc_ED10_5 (OS-Positivity and Stability Constraints for Curvature)**. File: `theory/Curvature_Emergence/Arc_ED10_5_OS_Positivity_and_Stability.md`. Scope: audit the proposed scalar-tensor covariant equation for OS-positivity preservation at structural-suggestive level under Euclidean continuation; identify the load-bearing structural conditions for OS positivity; address known stability-class concerns for scalar-tensor MOND-covariantizations (superluminal scalar propagation, ghost-mode issues, instability in cosmological backgrounds); flag any structural obstruction that would reverse the present positive verdict.

Estimated 2 sessions for Arc_ED10_5 given the technical load + the higher speculative-ratio of OS-positivity-class questions in the curvature-emergent regime.

### Decisions for you

- **Confirm covariant candidate.** Scalar-tensor acoustic-metric-class equation $\nabla_\mu[\mu(\sqrt{g^{\alpha\beta}\nabla_\alpha\Phi\nabla_\beta\Phi}/a_0)\nabla^\mu\Phi] = 4\pi GT$ as the substrate-FORCED covariantization of Arc_SG_4. Not GR; structurally equivalent to RAQUAL / scalar-tensor MOND.
- **Confirm structural verdict.** $f(R)$ inadmissible (ED-Phys-10 violation); bimetric collapses to scalar-tensor under acoustic-metric identification; scalar-tensor uniquely substrate-FORCED.
- **Confirm proceeding to Arc_ED10_5 (OS-positivity audit) as the next deliverable.**

---

*Arc_ED10_4 closes the covariant-form selection step. Three structural families audited against five substrate-derivation constraints (R1 weak-field reduction; R2 $a_0$ horizon-scale invariance; R3 BTFR slope-4 robustness; R4 no new primitives; R5 acoustic-metric class): TeVeS-class scalar-tensor (in scalar-tensor reduced version) passes all five; $f(R)$-class fails R4 + R5 (introduces scalaron + dynamical metric, violating ED-Phys-10); bimetric-class collapses to scalar-tensor under acoustic-metric identification. Substrate FORCES scalar-tensor acoustic-metric covariantization as the unique compatible candidate-form. Proposed covariant field equation: $\nabla_\mu[\mu(\sqrt{g^{\alpha\beta}\nabla_\alpha\Phi\nabla_\beta\Phi}/a_0)\nabla^\mu\Phi] = 4\pi GT$ with acoustic metric, Levi-Civita connection, substrate-derived $\Phi$, matter-trace source $T$. Not GR; substrate-derived covariantization of Arc_SG_4. Structurally equivalent to standard RAQUAL / scalar-tensor MOND covariantizations; ED-program-specific contribution is the substrate-derivation chain identifying this form as substrate-FORCED. FORCED/INHERITED: scalar-tensor structure + acoustic metric + covariant-divergence form + $\mu(x)$ asymptotics + weak-field SG-4 reduction FORCED; transition-regime $\mu(x)$ shape + curvature-coupling coefficients + cosmological boundary conditions + numerical $G$/$a_0$ values INHERITED. Preliminary verdict: structurally consistent covariant candidate exists; no new primitives required; ED-10 remains viable; structural-positive content depends on ED10-5 OS-positivity audit. Arc_ED10_5 (OS-positivity + stability constraints) is the next deliverable.*
