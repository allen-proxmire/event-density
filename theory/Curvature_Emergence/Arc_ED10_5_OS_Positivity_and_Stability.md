# Arc_ED10_5 — OS Positivity and Stability Constraints for Curvature

**Date:** 2026-04-30
**Status:** Fourth technical memo of the Curvature Emergence Arc + the load-bearing positivity question of ED-10. Audits the proposed scalar-tensor acoustic-metric covariant equation (Arc_ED10_4) for OS-positivity preservation, ghost-freedom, gradient stability, and superluminality. **Result: OS positivity preserved + ghost-freedom holds under conditions C1–C3 (FORCED at substrate level); gradient stability holds under C2 (kinetic-matrix positivity); superluminal scalar propagation is structurally present in the deep-MOND regime — a known stability-class concern in the standard scalar-tensor MOND covariantization literature that the substrate-compatible scalar-tensor reduced form cannot fully avoid. Structural verdict is conditional-positive with explicit honesty on the superluminality locus.**
**Companions:** [`Arc_ED10_1_Opening.md`](Arc_ED10_1_Opening.md), [`Arc_ED10_2_Curvature_Degrees_Of_Freedom.md`](Arc_ED10_2_Curvature_Degrees_Of_Freedom.md), [`Arc_ED10_3_Weak_Field_Limit.md`](Arc_ED10_3_Weak_Field_Limit.md), [`Arc_ED10_4_Covariant_Field_Equation.md`](Arc_ED10_4_Covariant_Field_Equation.md), [`../Yang-Mills/Arc_YM_5_OS_Positivity_And_Continuum_Stability.md`](../Yang-Mills/Arc_YM_5_OS_Positivity_And_Continuum_Stability.md) (parallel YM OS-positivity audit template).

---

## 1. Purpose

This memo addresses the load-bearing positivity question of ED-10. Specifically:

- **Tests whether the ED10-4 covariant equation preserves OS positivity** under Euclidean continuation $t \to -i\tau$.
- **Checks for ghost modes, gradient instabilities, and superluminal propagation** in the substrate-derived scalar-tensor acoustic-metric covariant field equation.
- **Identifies load-bearing structural conditions for stability** — the minimal substrate-derivation conditions under which the candidate equation is OS-positive + ghost-free + gradient-stable + (possibly) sub-luminal.
- **Determines whether ED-10 remains viable.** A clean structural-positive verdict carries ED-10 to ED10-6 synthesis; a stability-class obstruction would force ED-10 to either accept the obstruction as structural-conditional content or stall.

The memo is the structural analogue of Arc_YM_5 (OS-positivity audit for Yang-Mills) but with substantially higher technical complexity: scalar-tensor MOND-class covariantizations have known stability-class issues in the standard literature (superluminality in particular), and the substrate-compatible scalar-tensor reduced form (lacking the independent vector field of full TeVeS) inherits these issues.

**Honest framing.** This is the most technically delicate memo of ED-10. Standard scalar-tensor MOND covariantizations (RAQUAL, scalar-tensor reduced TeVeS) have been studied extensively since Bekenstein-Milgrom 1984; the OS-positivity / stability landscape is well-mapped in the standard literature. The present memo's contribution is the substrate-derivation reading of which conditions are FORCED at substrate level vs. INHERITED — not novel positivity-class findings.

---

## 2. Inputs

- **Arc_ED10_4 (Covariant candidate).** Substrate-derived scalar-tensor acoustic-metric covariant field equation $\nabla_\mu[\mu(\sqrt{g^{\alpha\beta}\nabla_\alpha\Phi\nabla_\beta\Phi}/a_0)\nabla^\mu\Phi] = 4\pi GT$.
- **Arc_ED10_3 (Weak-field limit).** Three load-bearing assumptions (acoustic-metric class, Levi-Civita connection, subleading curvature-coupling coefficients) for SG-4 recovery in $g_{\mu\nu}\to\eta_{\mu\nu}$ limit.
- **Arc_SG_4 (Modified Poisson equation).** Flat-background substrate-gravity field equation; provides the weak-field limit that the covariant equation must reproduce.
- **Theorem GR1 (Phase-3 closure).** V1 kernel structure on curved spacetime; provides analytic-structure ingredients for OS positivity audit.
- **DCGT (Arc D closure).** Substrate-to-continuum coarse-graining; provides V1 positive Fourier transform property (FORCED at substrate level by Theorem 18 + Theorem N1).
- **Standard OS-positivity criteria.** Reflection positivity under Euclidean-time reflection $\Theta$; bounded-below Euclidean action; positive-definite kinetic matrix; absence of negative-norm modes.
- **Arc_YM_5 (Yang-Mills OS-positivity audit template).** Parallel structural framework for OS-positivity preservation locus identification.

---

## 3. Step 1 — Euclidean Continuation and OS Positivity

Perform the Wick rotation $t \to -i\tau$ + Lorentzian-to-Euclidean metric transformation:

$$g_{\mu\nu}^{(L)} \;\longrightarrow\; g_{\mu\nu}^{(E)}, \qquad \det g^{(E)} \;>\; 0,$$

with $g^{(E)}$ Euclidean signature ($+, +, +, +$).

**Euclidean action for the scalar sector.** From the Arc_ED10_4 field equation, the corresponding Lagrangian density (assuming a variational formulation derived from a Lagrangian $\mathcal{L}_\Phi$) takes the form

$$\mathcal{L}_\Phi^{(E)} \;\propto\; F(X)\,\sqrt{g_E},$$

where $X = g_E^{\alpha\beta}\nabla_\alpha\Phi\,\nabla_\beta\Phi/a_0^2$ is the dimensionless squared-magnitude-of-gradient (covariant scalar; positive in Euclidean signature) and $F(X)$ is an interpolation-function-derived dimensionless function with $F'(X) = \mu(X^{1/2})\cdot a_0^2$ chosen so that the Euler-Lagrange equation reproduces the field equation. The Euclidean action is

$$S_E[\Phi] \;=\; \int d^4x \sqrt{g_E}\;F(X) \;\propto\; \int d^4x\sqrt{g_E}\;\mu\!\left(\frac{\sqrt{g_E^{\alpha\beta}\nabla_\alpha\Phi\,\nabla_\beta\Phi}}{a_0}\right)g_E^{\mu\nu}\nabla_\mu\Phi\,\nabla_\nu\Phi,$$

with the precise integrand fixed by the choice of $F(X)$.

**Three positivity checks.**

**(A) Positivity of the quadratic form.** In Euclidean signature, $g_E^{\alpha\beta}\nabla_\alpha\Phi\,\nabla_\beta\Phi \ge 0$ for any real $\Phi$ (positive-definite metric inner product). Combined with $\mu(x) > 0$ for $x > 0$ (FORCED by the asymptotic constraints + the standard MOND interpolation-function class), the integrand is non-negative pointwise. **Positive.**

**(B) Absence of negative-norm states.** A negative-norm state would correspond to a field configuration $\delta\Phi$ such that $\langle\Theta\delta\Phi\,\delta\Phi\rangle < 0$ under Euclidean-time reflection $\Theta$. The Lagrangian's quadratic form in $\delta\Phi$ at any background $\Phi_0$ has a kinetic matrix $Z^{\mu\nu}(\Phi_0)$ (computed in Step 2). Negative-norm states are absent if $Z^{\mu\nu}$ is positive-definite. Step 2 audits this explicitly.

**(C) Convexity of the Euclidean action.** Convexity of $F(X)$ — equivalently, positivity of the second-derivative $F''(X)$ — guarantees that the Euclidean action is bounded below + convex, ensuring the standard Hilbert-space reconstruction works. Convexity is conditional on the specific $\mu(x)$ choice; the asymptotic constraints alone do not guarantee convexity in the transition regime, but specific structurally-admissible $\mu(x)$ forms (e.g., the "simple" form $\mu(x) = x/\sqrt{1+x^2}$) preserve convexity.

**FORCED at substrate level:**
- Positivity of the quadratic form $g_E^{\alpha\beta}\nabla_\alpha\Phi\,\nabla_\beta\Phi \ge 0$ (Euclidean signature property).
- $\mu(x) > 0$ in the bulk (FORCED by V1 positive Fourier transform per Theorem 18 + Theorem N1, structurally analogous to the YM-5 mechanism of Arc_YM_5 Step 5).
- Pointwise non-negativity of the Euclidean Lagrangian integrand.

**INHERITED at value layer:**
- Convexity of $F(X)$ in the transition regime (depends on specific $\mu(x)$ shape; preserved under "simple" / "standard" / structurally-admissible forms but not guaranteed by asymptotic constraints alone).

**Step 1 verdict.** OS-positivity audit at the level of pointwise integrand positivity passes; convexity-based reconstruction passes conditional on transition-regime $\mu(x)$ shape (INHERITED). The structural-suggestive verdict is **OS-positive at this level**.

---

## 4. Step 2 — Ghost-Freedom and Gradient Stability

Linearize the field equation around a background solution $\Phi_0$:

$$\Phi(x) \;=\; \Phi_0(x) \;+\; \delta\Phi(x), \qquad |\delta\Phi| \;\ll\; |\Phi_0|.$$

The linearized action's kinetic term takes the form

$$\mathcal{L}_\mathrm{kin}^{(E)} \;\sim\; \tfrac{1}{2}\,Z^{\mu\nu}(\Phi_0)\,\nabla_\mu\delta\Phi\,\nabla_\nu\delta\Phi,$$

with the kinetic matrix

$$Z^{\mu\nu}(\Phi_0) \;=\; \mu(X_0)\,g^{\mu\nu} \;+\; \mu'(X_0)\,\frac{\nabla^\mu\Phi_0\,\nabla^\nu\Phi_0}{X_0\,a_0^2}\cdot\bigl(\text{normalization factor}\bigr),$$

where $X_0 = g^{\alpha\beta}\nabla_\alpha\Phi_0\,\nabla_\beta\Phi_0/a_0^2$ is the background squared-gradient and $\mu'(X_0) = d\mu/dX|_{X_0}$. (The precise normalization depends on the specific $F(X)$ choice; the general structure is correct under any standard variational formulation.)

**Ghost-freedom check ($Z^{00} > 0$).** In Euclidean signature, $Z^{\mu\nu}$ must be positive-definite for ghost-freedom. The eigenvalue structure of $Z^{\mu\nu}$:

- **Transverse direction** (eigenvector orthogonal to $\nabla\Phi_0$): eigenvalue $= \mu(X_0)$. Positive whenever $\mu > 0$ — **FORCED** by V1 positive Fourier transform.
- **Longitudinal direction** (eigenvector parallel to $\nabla\Phi_0$): eigenvalue $= \mu(X_0) + 2X_0\mu'(X_0) = (X_0\mu)'$ where $'$ denotes $d/dX_0$. (Often written as $\mu(X) + X\mu'(X)$ or $\mu(\sqrt{X}) + \tfrac{1}{2}\sqrt{X}\mu'(\sqrt{X})$ depending on conventions.) Positive iff $(X\mu)' > 0$, equivalently iff the function $X\mu(X)$ is monotonically increasing.

**Standard MOND-covariantization condition.** The condition $(X\mu)' > 0$ is equivalent to the standard kinetic-matrix-positivity condition in AQUAL / RAQUAL theories: $\mu(x) + x\mu'(x) > 0$ in conventional notation. This condition holds in both asymptotic limits (Newtonian: $\mu = 1$, $\mu' = 0$, condition gives $1 > 0$ ✓; deep-MOND: $\mu = x$, $\mu' = 1$, condition gives $x + x = 2x > 0$ for $x > 0$ ✓) but must be checked in the transition regime for any specific $\mu(x)$ choice. Standard "simple" + "standard" forms both satisfy this condition; some non-standard forms do not.

**Gradient stability check.** Spatial-eigenvalue positivity of $Z^{ij}$ ensures absence of gradient instabilities (modes that grow exponentially in space). For the kinetic matrix above, the spatial eigenvalues are $\mu(X_0)$ in transverse spatial directions and $\mu(X_0) + 2X_0^{\Vert}\mu'(X_0)$ in the longitudinal-spatial direction (with $X_0^{\Vert}$ the spatial-component contribution to $X_0$). Both are positive under the same condition $(X\mu)' > 0$.

**Step 2 verdict.**
- **Ghost-freedom: holds** under condition (C2): $\mu(x) + x\mu'(x) > 0$ — FORCED in asymptotic limits, FORCED in transition regime under standard $\mu(x)$ forms (INHERITED at value layer for the specific transition-regime shape selection).
- **Gradient stability: holds** under the same condition (C2). The substrate-derivation does not introduce gradient instabilities at the level of the linearized scalar-sector dynamics.

The candidate equation is **ghost-free + gradient-stable** under condition (C2), which is structurally backed by the asymptotic-limit + standard-$\mu(x)$-shape arguments.

---

## 5. Step 3 — Superluminality Audit

The most delicate stability question for scalar-tensor MOND-covariantizations is the propagation-speed of the scalar field $\Phi$ relative to the acoustic light cone. In standard AQUAL/RAQUAL theories, the scalar field is known to propagate **superluminally** in some regimes — a structural feature, not an avoidable artifact.

**Effective propagation metric.** Linearized scalar-field perturbations propagate on the effective metric

$$g_\mathrm{eff}^{\mu\nu} \;=\; \mu(X_0)\,g^{\mu\nu} \;+\; \mu'(X_0)\,\frac{\nabla^\mu\Phi_0\,\nabla^\nu\Phi_0}{a_0^2 |\nabla\Phi_0|}\cdot\bigl(\text{normalization factor}\bigr),$$

(equivalent to the inverse of the kinetic matrix $Z^{\mu\nu}$ with appropriate factor structure). The characteristic speed of perturbations in the longitudinal direction (parallel to $\nabla\Phi_0$) is set by the eigenvalue structure of $g_\mathrm{eff}^{\mu\nu}$ along that direction.

**Comparison with acoustic light cone.**

- **Newtonian regime** ($X_0 \to \infty$, $\mu \to 1$, $\mu' \to 0$): $g_\mathrm{eff}^{\mu\nu} \to g^{\mu\nu}$. Scalar propagates at the speed of light along the acoustic metric — **subluminal/luminal**, identical to the metric cone. ✓
- **Deep-MOND regime** ($X_0 \to 0$, $\mu \to X_0^{1/2}$, $\mu' \to \tfrac{1}{2}X_0^{-1/2}$): the longitudinal eigenvalue of $g_\mathrm{eff}^{\mu\nu}$ becomes $\mu + 2X_0\mu' = X_0^{1/2}(1 + 1) = 2X_0^{1/2}$, while the transverse eigenvalue is $\mu = X_0^{1/2}$. The longitudinal/transverse ratio is 2 — **the longitudinal propagation cone is wider than the metric cone by a factor of $\sqrt{2}$**. **Superluminal** in the longitudinal direction.
- **Transition regime**: depends on $\mu(x)$ specific shape; superluminality typically present for any standard interpolation function with $\mu' > 0$.

**Superluminality is structurally present in the deep-MOND regime.** This is a known result in the standard scalar-tensor MOND literature (Bekenstein-Sanders 1994, Bruneton-Esposito-Farese 2007, and others). The superluminality is a structural feature of the scalar-tensor reduced form — not an avoidable artifact.

**Why superluminality occurs.** In the deep-MOND regime, the kinetic matrix $Z^{\mu\nu}$ has a strong anisotropy: the longitudinal direction (along $\nabla\Phi$) acquires extra "stiffness" from the $\mu'\nabla^\mu\Phi\nabla^\nu\Phi$ contribution. This anisotropy is precisely what produces the geometric-mean ECR composition $a^2 = a_N\,a_0$ at substrate level (Arc_SG_4 §3); removing the anisotropy would remove the deep-MOND behavior + BTFR slope-4. **The superluminality is structurally tied to the substrate-derivation chain that produces SG-4.**

**Causality implications.** Superluminal propagation does not by itself violate causality, provided the propagation respects an effective causal cone (the $g_\mathrm{eff}$-cone) consistently across the spacetime. In the standard MOND-covariantization literature, the conclusion is that scalar-tensor RAQUAL-class theories admit closed-timelike-curve-class issues only in pathological backgrounds; in physically reasonable backgrounds (cosmological, galactic), superluminality coexists with effective causality. This is the standard view; ED-10 inherits it.

**Avoidance options.** Two structural routes to avoid superluminality:

- **Route 1: Add an independent vector field.** Bekenstein's full TeVeS theory (Tensor-Vector-Scalar) introduces an independent vector field that absorbs the scalar's longitudinal mode, restoring subluminal propagation. **Inadmissible at substrate level** per constraint (R4) of Arc_ED10_4 (no new primitives) — the vector field has no substrate-derivation chain in the closed-arc framework.
- **Route 2: Choose $\mu(x)$ with $\mu' \to 0$ in the deep-MOND regime.** This would violate the deep-MOND asymptotic $\mu(x) \to x$ that is FORCED by ECR (Arc_SG_4 + Arc_SG_5). **Inadmissible at structural level** because it would break the BTFR slope-4 derivation.

Neither avoidance route is structurally available to the ED-10 substrate-compatible candidate. **Superluminality is structurally FORCED in the deep-MOND regime** under the present candidate-form.

**Step 3 verdict.** The substrate-compatible scalar-tensor reduced covariant equation is **superluminal in the deep-MOND regime**, structurally forced by the substrate-derivation chain that produces SG-4 + ECR + BTFR slope-4. The superluminality coexists with effective causality in physically reasonable backgrounds (standard MOND-covariantization-literature view). Whether superluminality constitutes a structural-positivity obstruction depends on whether OS positivity (Euclidean-action + reconstruction-theorem) requires sub-luminal Lorentzian propagation — which is *not* generally required for OS-positive reconstructions, but is a known stability-class concern.

This is the load-bearing structural concern for ED-10's positivity verdict.

---

## 6. Step 4 — Load-Bearing Structural Conditions

Identify the minimal substrate-derivation conditions required for OS positivity + ghost-freedom + gradient stability. Five conditions:

**(C1) $\mu(x)$ must be monotone increasing.** $\mu'(x) > 0$ in the bulk. FORCED in asymptotic limits ($\mu \to 1$ at high $x$, $\mu \to x$ at low $x$, both monotone-increasing transitions); FORCED in transition regime under standard $\mu(x)$ forms (INHERITED at value layer for specific shape).

**(C2) Kinetic-matrix positivity: $\mu(x) + x\mu'(x) > 0$.** Required for ghost-freedom + gradient stability (Step 2). FORCED in asymptotic limits; FORCED in transition regime under standard $\mu(x)$ forms.

**(C3) V1 kernel Fourier transform strictly positive.** Required for $\mu(x) > 0$ in the bulk + Step 1 OS-positive integrand. FORCED at substrate level by Theorem N1 admissibility class + Theorem 18 forward-cone support (per Arc_YM_5 §7 and parallel substrate derivations).

**(C4) Curvature-coupling coefficients remain subleading.** $\alpha_R$, $\beta_{R_{\mu\nu}}$ from the curved-DCGT operator (Arc_ED10_2 §3) must be sufficiently small that the leading weak-field behavior is dominated by the flat Laplacian. Per Arc_ED10_3 assumption (A3); INHERITED at value layer.

**(C5) Acoustic metric remains Lorentzian and non-degenerate.** Per ED-Phys-10 acoustic-metric guardrail; the substrate participation density must remain in a regime where the acoustic metric has Lorentzian signature ($-,+,+,+$) without metric degeneracy. FORCED structurally for non-extreme-substrate-density regimes; could fail near substrate-density singularities (e.g., black-hole-class substrate configurations where the acoustic-metric reading might break down — out of scope per ED-Phys-10).

**FORCED at substrate level:**
- (C1) monotone-increasing $\mu(x)$ — FORCED in asymptotic limits + standard forms.
- (C2) kinetic-matrix positivity — FORCED in asymptotic limits + standard forms.
- (C3) V1 positive Fourier transform — FORCED unconditionally by closed structural-foundation work.
- (C5) Lorentzian acoustic metric — FORCED in non-extreme regimes per ED-Phys-10.

**INHERITED at value layer:**
- (C1) and (C2) transition-regime shapes — INHERITED via specific $\mu(x)$ shape selection.
- (C4) curvature-coupling coefficient magnitudes — INHERITED at value layer.

The five conditions jointly define the structural framework within which OS positivity + ghost-freedom + gradient stability hold for the ED-10 covariant candidate. **Superluminality is not in the list** — it is a structural feature, not a positivity-class obstruction in the standard literature reading.

---

## 7. Step 5 — Preliminary Verdict

**OS positivity is preserved** under conditions (C1)–(C3) jointly. The Euclidean action is non-negative pointwise + bounded below + convex under standard $\mu(x)$ forms. Reconstruction theorem applies at structural-suggestive level under conditions (C1)–(C3) + (C4) subleading-curvature-coupling.

**Ghost-freedom holds** under condition (C2). The kinetic matrix $Z^{\mu\nu}$ is positive-definite in both transverse and longitudinal directions for $\mu(x) + x\mu'(x) > 0$.

**Gradient stability holds** under the same condition (C2). No spatial-mode instabilities at the linearized scalar-sector level.

**Superluminality is structurally present in the deep-MOND regime** — a known stability-class concern in the standard scalar-tensor MOND-covariantization literature. The substrate-compatible scalar-tensor reduced form *cannot* avoid superluminality without violating either the no-new-primitives constraint (R4) or the deep-MOND asymptotic $\mu(x) \to x$ (FORCED by ECR + BTFR slope-4). **Avoidance routes structurally inadmissible.**

**The superluminality is structurally tied to the substrate-derivation chain.** Removing it would remove the substrate-derivation of MOND-class behavior + BTFR slope-4. The superluminality is the structural cost of obtaining the substrate-derived MOND-covariantization — not a phenomenological adjustment that could be made without affecting the substrate-positive content.

**ED-10 remains viable, with explicit honesty on superluminality.** The structural verdict is **conditional-positive at the OS-positivity / ghost-freedom / gradient-stability levels**, with the explicit caveat that the deep-MOND regime carries structurally-FORCED superluminal scalar propagation as an inherited feature of the substrate-derivation chain. This is parallel in honesty-framing to:

- **Arc_YM_6 Clay-relevance verdict**: structural-positive at Intermediate Path C level with explicit honesty on Gribov-class gauge-fixing-sector questions reframed-not-resolved.
- **NS-Smoothness Intermediate Path C verdict**: real Clay-relevant regularizing mechanism with explicit honesty on advection-as-non-ED transport-kinematic obstruction.

The ED-10 verdict mirrors these honest-framings: substrate-derivation produces a structurally consistent + OS-positive + ghost-free + gradient-stable scalar-tensor covariantization, with superluminality as the structurally-forced stability-class feature inherited from the standard scalar-tensor MOND-covariantization literature. The ED-program-specific contribution is the substrate-derivation chain identifying this form as substrate-FORCED + identifying superluminality as substrate-FORCED rather than phenomenologically adjustable.

**ED-10 proceeds to ED10-6 synthesis** under this conditional-positive structural verdict.

---

## 8. Recommended Next Step

Proceed to **Arc_ED10_6 (Synthesis + Clay-Relevance-Style Verdict)**. File: `theory/Curvature_Emergence/Arc_ED10_6_Synthesis.md`. Scope: aggregate Arc_ED10_1 through Arc_ED10_5 into a single arc-closing memo; produce the ED-10 Clay-relevance-style structural verdict parallel to NS-Smoothness Intermediate Path C and Arc_YM_6 Clay-YM-relevance statement; honest framing on what ED-10 resolves (substrate-derived covariant generalization of SG-4 with OS-positivity + ghost-freedom + gradient stability under conditions C1–C5) and what remains open (deep-MOND superluminality structurally inherited; full constructive-rigorous OS-reconstruction not claimed; cosmological-background stability not audited).

Estimated 1–2 sessions for Arc_ED10_6.

### Decisions for you

- **Confirm OS-positivity verdict.** Preserved under conditions (C1)–(C3); reconstruction-theorem applies at structural-suggestive level.
- **Confirm ghost-freedom + gradient-stability verdict.** Hold under condition (C2); no instabilities at linearized scalar-sector level.
- **Confirm honest framing on superluminality.** Structurally FORCED in deep-MOND regime; avoidance routes structurally inadmissible (would violate either no-new-primitives or BTFR-slope-4); inherited from standard scalar-tensor MOND-covariantization stability landscape.
- **Confirm proceeding to Arc_ED10_6 (synthesis + Clay-relevance-style verdict) as the next deliverable.**
- **Or override:** if superluminality is judged to be a stall-locus rather than acceptable structural-conditional content, ED-10 stalls here rather than proceeding to synthesis. (This is a user-decision-class judgment; the present memo's preliminary verdict is conditional-positive but the conditional content is non-trivial.)

---

*Arc_ED10_5 closes the OS-positivity / stability audit at the load-bearing technical question of ED-10. OS positivity preserved under (C1) monotone-increasing $\mu(x)$ + (C2) kinetic-matrix positivity $\mu(x) + x\mu'(x) > 0$ + (C3) V1 positive Fourier transform; reconstruction-theorem applies at structural-suggestive level. Ghost-freedom holds under (C2); gradient stability holds under (C2). Superluminal scalar propagation in deep-MOND regime is structurally FORCED by the substrate-derivation chain (cannot avoid without violating no-new-primitives constraint R4 or BTFR-slope-4 FORCED-asymptotic); inherited from standard scalar-tensor MOND-covariantization literature stability landscape. Avoidance routes structurally inadmissible at substrate level. Conditional-positive structural verdict: OS-positive + ghost-free + gradient-stable under (C1)–(C5); deep-MOND superluminality structurally inherited as substrate-FORCED feature. Parallel in honesty-framing to NS-Smoothness Intermediate Path C + Arc_YM_6 Clay-YM-relevance statement: structural-positive content + explicit honesty on the structural-conditional content. ED-10 remains viable; proceeds to ED10-6 synthesis under conditional-positive verdict. Arc_ED10_6 (synthesis + Clay-relevance-style verdict) is the next deliverable.*
