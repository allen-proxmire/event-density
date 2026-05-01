# Arc_SG_3 — Transition Acceleration $a_0$ Under Kernel-Profile Scaling

**Date:** 2026-04-30
**Status:** Second technical derivation memo of the Substrate Gravity Extension Arc. Analyzes how the transition acceleration $a_0 = c\,H_0/(2\pi)$ behaves under V1 kernel-profile variation and the continuum limit $\ell_P \to 0$. **Result: $a_0$ is invariant under $\ell_P$ scaling — its substrate origin is cosmological-horizon participation density, not substrate-cutoff content. This is structurally different from the YM-3 mass-gap scaling result; $a_0$ requires no kernel-profile rescaling condition for survival.**
**Companions:** [`Arc_SG_1_Opening.md`](Arc_SG_1_Opening.md), [`Arc_SG_2_Newtonian_From_DCGT.md`](Arc_SG_2_Newtonian_From_DCGT.md), [`../Yang-Mills/Arc_YM_3_Mass_Gap_From_Substrate_Cutoff.md`](../Yang-Mills/Arc_YM_3_Mass_Gap_From_Substrate_Cutoff.md) (the YM analogue this memo contrasts with), [`../../arcs/arc-SG/substrate_a0_ed_native.md`](../../arcs/arc-SG/substrate_a0_ed_native.md), [`../../arcs/arc-SG/substrate_holographic_bound.md`](../../arcs/arc-SG/substrate_holographic_bound.md), [`../../arcs/arc-SG/substrate_2pi_question.md`](../../arcs/arc-SG/substrate_2pi_question.md), [`../../arcs/arc-B/arc_b_synthesis.md`](../../arcs/arc-B/arc_b_synthesis.md) (T18).

---

## 1. Purpose

This memo:

- **Analyzes how $a_0$ scales under V1 kernel-profile variation** and under the continuum limit $\ell_P \to 0$. The closed-arc substrate derivation of $a_0 = c\,H_0/(2\pi)$ (Arc-SG, 2026-04-27) does not by itself address the kernel-profile-scaling question; the present memo audits this question explicitly.
- **Determines which parts of $a_0$ are FORCED vs INHERITED** under the program's standard form-FORCED / value-INHERITED methodology.
- **Distinguishes $a_0$ scaling from YM mass-gap scaling** — the load-bearing structural distinction of this memo. YM-3's mass-gap mechanism produces a substrate-induced effective mass $m_\mathrm{eff}^2 \sim c_{V1}\ell_P^{-2}$ that requires a kernel-profile rescaling condition $c_{V1}(\ell_P)\ell_P^{-2} \to m_\mathrm{phys}^2 > 0$ for continuum-limit survival. The $a_0$ transition acceleration is structurally different: its substrate origin is cosmological-horizon participation density, not substrate-cutoff content. The continuum-limit survival question is structurally trivial for $a_0$.
- **Prepares the ground for SG-4** (consolidated substrate-gravity field equation in flat background). The $\ell_P$-invariance of $a_0$ established here is a load-bearing input for SG-4's transition-regime corrections.

The memo is structurally parallel to YM-3 (mass-gap scaling analysis) but with a different verdict at the substrate-origin level.

---

## 2. Inputs

- **T20 (Transition acceleration from substrate, 2026-04-27).** $a_0 = c\,H_0/(2\pi)$ derived from substrate primitives via the cosmological-horizon participation-density connection. The $2\pi$ prefactor is structurally derived (substrate spin-statistics + holographic bound) rather than fitted. Closed in `arcs/arc-SG/substrate_a0_ed_native.md` and `substrate_2pi_question.md`.
- **T19 (Newton's law from substrate).** $G = c^3\ell_P^2/\hbar$ — the substrate-cutoff-anchored Newton coupling. Structurally distinct from $a_0$ in that $G$ depends explicitly on $\ell_P$ while $a_0$ does not.
- **ED Combination Rule (ECR).** $a = \sqrt{a_N\,a_0}$ — composition rule between Newton-class and transition-class accelerations. The cross-term that connects $G$-anchored and $H_0$-anchored substrate content.
- **T21 (slope-4 BTFR).** $v^4 = G\,M\,a_0$ — empirical-anchor result. The $G\cdot a_0$ product depends on both $\ell_P^2$ (via $G$) and $H_0$ (via $a_0$); SG-5 will audit whether this product is robust under kernel variation.
- **DCGT (Arc D closure).** Substrate-to-continuum coarse-graining theorem. Provides the methodology for analyzing kernel-profile scaling.
- **Arc_SG_2 (Newtonian re-derivation).** Established the Newtonian sector under DCGT scalar-diffusion machinery. The present memo addresses the *transition-regime* sector that the consolidated SG-4 equation will combine with the Newtonian sector.
- **ED-I-06 (Fields and Forces).** Curvature-like-field thread (§5) for cosmological-horizon participation density. The $a_0$ transition acceleration is structurally a curvature-like-field-class quantity at substrate level (the cosmological horizon supplies the substrate participation-density boundary that produces the transition).

---

## 3. Step 1 — Recap of T20 Transition Acceleration

The closed-arc substrate derivation of $a_0$ (Arc-SG, 2026-04-27, papers `substrate_a0_ed_native.md` + `substrate_2pi_question.md`) routes through three structural anchors:

**(A1) Cosmological-horizon participation density.** The cosmological event horizon at radius $R_H = c/H_0$ supplies a substrate-level participation-density boundary. Beyond $R_H$, no substrate participation channels can communicate with the local participation network within the cosmological time available; the horizon truncates the substrate participation-flux integration at scale $R_H$. The horizon-scale participation density is the structural anchor of $a_0$.

**(A2) Retardation structure (T18 forward-cone causality).** T18's V1 kernel forward-cone-only support ensures that substrate participation flux respects causal structure. Combined with the cosmological horizon as an effective participation-density boundary, retardation produces the transition-regime behavior at acceleration scales near $a_0$ where the substrate response to mass content shifts from Newton-class (substrate-local) to MOND-class (horizon-coupled).

**(A3) $2\pi$ prefactor from substrate spin-statistics + holographic bound.** The closed-arc analysis (`substrate_2pi_question.md`) derived the $2\pi$ prefactor via the substrate-level spin-statistics structure and the holographic participation-count bound. Specifically, the cosmological-horizon-scale participation count is bounded by the holographic prescription $N \sim R_H^2/\ell_P^2$, and the substrate spin-statistics at the horizon-scale fluctuation level produces the $2\pi$ factor. The prefactor is structurally derived; it is not a phenomenological fit.

**Result.** $a_0 = c\,H_0/(2\pi)$ is FORCED at substrate level via the cosmological-horizon mechanism + retardation + holographic-bound + substrate spin-statistics. The numerical value of $a_0$ depends on the value of $H_0$ (the Hubble scale, INHERITED at value layer from cosmological observation), but the *form* and *prefactor* are FORCED.

**Structural distinction from YM mass gap.** The substrate origin of $a_0$ is fundamentally different from the substrate origin of the YM mass gap derived in YM-3:

| Substrate quantity | Substrate scale | Structural origin |
|---|---|---|
| YM mass gap $m_\mathrm{eff}^2$ | $\ell_P^{-2}$ (substrate cutoff) | V1 kernel finite-width second-moment expansion |
| $a_0$ transition acceleration | $c\,H_0$ (cosmological horizon) | Cosmological-horizon participation-density boundary |

The YM mass gap is a *substrate-cutoff effect*: it scales as $\ell_P^{-2}$ at substrate level, requires kernel-profile rescaling $c_{V1}(\ell_P)\ell_P^{-2} \to m_\mathrm{phys}^2$ for continuum-limit survival, and is fundamentally tied to the V1 kernel finite-width via the multi-scale expansion. The transition acceleration $a_0$ is an *infrared* effect: it scales with cosmological-horizon size $R_H = c/H_0$, has no fundamental dependence on $\ell_P$, and is structurally tied to the participation-density boundary at cosmological scales rather than to the substrate-discreteness scale.

These are two different sectors of the substrate-gravity ontology, with structurally different scaling behavior under the continuum limit.

---

## 4. Step 2 — Kernel-Profile Scaling

Analyze how V1 kernel variation affects three structural sectors:

**(S1) Local participation curvature.** The V1 kernel's finite spatial width $\sim \ell_P$ produces local participation-curvature corrections at substrate scales. Under DCGT multi-scale expansion (Arc_D_2 / Arc_D_4), this contributes to the substrate-derived mobility coefficient $\mu(\rho)$ and the R1 hyperviscous correction $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$ in the velocity sector, and to the analogous gauge-field substrate-cutoff correction $\ell_P^2\nabla^2 A$ in the YM sector. **For substrate gravity, the local-participation-curvature sector enters via T19's $G = c^3\ell_P^2/\hbar$** — the gravitational coupling is anchored on $\ell_P^2$ via the substrate-cutoff length-scale.

**(S2) Long-range participation imbalance.** The V1 kernel's *tail* behavior — its decay structure at distances much larger than $\ell_P$ — affects long-range participation-flux propagation. T18 forward-cone causality ensures the tail is forward-cone-only (no backward-cone contributions); the tail's spatial-decay structure is constrained by V1 admissibility (Theorem N1: V1 is bounded between V1-δ at zero width and V1-∞ at infinite range, both REFUTED at primitive level). The long-range tail is what couples local participation-imbalance to the cosmological-horizon-scale participation density.

**(S3) Horizon-scale retardation.** The interaction between V1 forward-cone-only support and the cosmological event horizon at $R_H = c/H_0$ produces the transition-regime behavior. Substrate participation flux from a local mass content propagates outward via V1-mediated chain transitions, eventually reaching the cosmological horizon at the timescale $H_0^{-1}$. Beyond this timescale, no further substrate response can be received from the receding distant universe; the participation-flux integration terminates at $R_H$. This horizon-truncation is the structural mechanism that produces the transition-regime acceleration scale.

**Effect of $\ell_P \to 0$ on each sector.**

- **(S1) Local participation curvature:** strongly affected. As $\ell_P \to 0$, the substrate-cutoff scale shrinks; T19's $G \propto \ell_P^2$ rescales accordingly. The Newton-class sector explicitly depends on $\ell_P$ via $G$.
- **(S2) Long-range participation imbalance:** unchanged. The V1 kernel's tail behavior at distances $r \gg \ell_P$ is governed by the kernel's overall integral structure, which is normalized by the kernel-profile-rescaling conditions independent of the substrate-cutoff scale shrinking.
- **(S3) Horizon-scale retardation:** unchanged. The cosmological event horizon $R_H = c/H_0$ is fixed by the cosmological scale parameters, not by substrate physics. As $\ell_P \to 0$, the horizon scale $R_H$ remains exactly the same.

**Local kernel width $\ell_P$ affects the Newtonian sector (T19) but does not affect $a_0$.** The structural decoupling of $a_0$ from $\ell_P$ is the load-bearing finding of this step.

---

## 5. Step 3 — Scaling Analysis

The substrate derivation of $a_0$ in Step 1 routes through three anchors (A1 cosmological-horizon participation density; A2 retardation structure; A3 $2\pi$ prefactor from substrate spin-statistics + holographic bound). Each is examined under $\ell_P$ rescaling:

**(A1) Cosmological-horizon participation density.** $R_H = c/H_0$ is independent of $\ell_P$. The horizon-scale participation density $\rho_H \sim H_0/c\cdot\rho_\mathrm{vac}$ depends on cosmological parameters ($H_0$, $\rho_\mathrm{vac}$) which are independent of substrate-cutoff scale. **Unchanged under $\ell_P \to 0$.**

**(A2) Retardation structure.** T18 forward-cone-only support is FORCED at primitive level; the forward-cone structure is a topological property of the V1 kernel that does not depend on the kernel's finite width. Under $\ell_P \to 0$, the V1 kernel narrows in physical units but retains forward-cone-only support. **Unchanged under $\ell_P \to 0$ in the relevant structural sense.**

**(A3) $2\pi$ prefactor.** The closed-arc derivation of the $2\pi$ prefactor in `substrate_2pi_question.md` routes through substrate spin-statistics (R.2.5 spin-statistics + Cl(3,1) substrate frame, T17 gauge-quotient identification at vertex level) and the holographic participation-count bound at horizon scale ($N \sim R_H^2/\ell_P^2$). The $\ell_P$-dependence of the holographic bound *cancels* against the substrate-spin-statistics normalization, leaving the $2\pi$ prefactor as a dimensionless substrate-derived constant. **Unchanged under $\ell_P \to 0$.**

**Result.**

$$\boxed{\;a_0 \;=\; \frac{c\,H_0}{2\pi} \quad\text{is invariant under } \ell_P \to 0,\;}$$

provided three structural conditions hold:

- **(C1) Kernel long-range tail remains isotropic.** V1's tail behavior at $r \gg \ell_P$ must preserve spherical isotropy (substrate-level rotational invariance at long-range scales).
- **(C2) Retardation structure (T18) is preserved.** Forward-cone-only support of V1 must hold in the continuum limit (FORCED at primitive level by Theorem 18).
- **(C3) Horizon-scale participation density is unchanged.** The cosmological-horizon participation density at scale $R_H = c/H_0$ must be set by cosmological parameters independent of substrate-cutoff variation.

All three conditions are structurally backed: (C1) by V1 admissibility class (Theorem N1) + substrate isotropy at long range; (C2) by Theorem 18 closure; (C3) by cosmological-parameter independence of substrate physics.

**Structural verdict.** $a_0$ is **FORCED** by cosmological-horizon structure + retardation + substrate spin-statistics + holographic bound. It is **not** FORCED by substrate-cutoff physics; the substrate-cutoff dependence ($\ell_P$) cancels out of the final expression. Continuum-limit survival is structurally automatic — no kernel-profile rescaling condition is required.

This is qualitatively different from the YM-3 mass-gap result, where the substrate-cutoff dependence is fundamental and continuum-limit survival requires an explicit kernel-profile-rescaling condition. The substrate-gravity transition acceleration is an *infrared* substrate effect; the YM mass gap is a *UV* substrate effect; their continuum-limit behaviors are structurally different.

---

## 6. Step 4 — FORCED vs INHERITED Classification

Following the program's standard form-FORCED / value-INHERITED methodology:

### FORCED at substrate level

- **Existence of a transition acceleration.** The cosmological-horizon participation-density mechanism + retardation produces a transition-regime acceleration scale unconditionally at substrate level.
- **Functional form $a_0 \propto c\,H_0$.** The cosmological-horizon scale $R_H = c/H_0$ + substrate retardation produce the dimensional combination $cH_0$ as the natural transition-acceleration scale. Form FORCED.
- **$2\pi$ prefactor.** Derived structurally from substrate spin-statistics + holographic bound at horizon scale (`substrate_2pi_question.md` closed-arc analysis). Form FORCED.
- **Horizon-scale participation density.** The participation-density boundary at cosmological-horizon scale is FORCED by T18 forward-cone causality + cosmological-horizon presence; structural feature of any cosmologically-bounded substrate participation network.
- **Retardation structure (T18).** Forward-cone-only support of V1 kernel; FORCED at primitive level (Theorem 18).
- **Continuum-limit invariance.** $a_0$'s independence of $\ell_P$ is FORCED by the cancellation of substrate-cutoff dependence through the holographic-bound + spin-statistics normalization.

### INHERITED at value layer

- **Numerical value of $H_0$.** The Hubble parameter is observationally determined; ED does not predict its numerical value.
- **Cosmological boundary conditions.** Specifications of cosmological-scale physics (vacuum energy, dark-energy content, etc.) are INHERITED at value layer.
- **Kernel long-range tail normalization.** The detailed long-range tail profile of V1 (subject to admissibility constraints from Theorem N1) is INHERITED at value layer; specific tail-decay exponents and amplitudes are not predicted by substrate physics.

### Comparison with YM-3 classification

| Quantity | FORCED at substrate level | INHERITED at value layer |
|---|---|---|
| YM mass gap $m_\mathrm{eff}^2$ | Existence; $\ell_P^{-2}$ scaling form; sign (stabilizing) | Numerical value; kernel-profile rescaling exponent; physical-scale survival |
| $a_0$ transition acceleration | Existence; $cH_0$ form; $2\pi$ prefactor; $\ell_P$ invariance | $H_0$ value; cosmological boundary conditions; kernel tail normalization |

The FORCED / INHERITED structure for $a_0$ is structurally cleaner than for the YM mass gap because the continuum-limit survival is automatic for $a_0$ while it is conditional for the YM mass gap. ED's substrate framing of $a_0$ is therefore stronger in the structural sense (more is FORCED, less is INHERITED) than its substrate framing of the YM mass gap.

---

## 7. Step 5 — Consequences for SG-4 and SG-5

Three direct downstream consequences for the remaining sub-arcs:

**(i) SG-4 (consolidated substrate-gravity field equation).** SG-4 will produce the consolidated equation governing the flat-background substrate-gravity regime. The Arc_SG_2 result supplies the Newtonian sector ($\nabla^2\Phi = 4\pi G\rho_m$); the present Arc_SG_3 result supplies the transition-regime $a_0$ sector with its $\ell_P$-invariance verdict. The consolidated equation will combine these via the ED Combination Rule cross-term $\sqrt{a_N\,a_0}$ to produce a unified substrate-gravity equation that recovers Newton at $a \gg a_0$ and MOND-class behavior at $a \ll a_0$. Working candidate form for SG-4:

$$\nabla\cdot\bigl[\mu\bigl(|\nabla\Phi|/a_0\bigr)\,\nabla\Phi\bigr] \;=\; 4\pi G\,\rho_m,$$

with the interpolation function $\mu(\cdot)$ FORCED at substrate level by ECR + holographic-bound structure. SG-4 will derive this explicitly.

**(ii) SG-5 (BTFR slope-4 robustness).** SG-5 will audit the slope-4 result $v^4 = G\,M\,a_0$ for robustness under kernel variation. The $a_0$-content's robustness is established here: $a_0$ is invariant under $\ell_P$ scaling and FORCED in functional form, so the $a_0$-factor in BTFR is structurally robust. The slope-4 robustness question reduces to the $G$-content's robustness (T19, FORCED via cumulative-strain mechanism) and the geometric-mean ECR composition's robustness (FORCED via substrate-level participation-curvature combination).

**(iii) Key structural input for SG-4.** The $\ell_P$-invariance of $a_0$ established here is a load-bearing structural input for SG-4. It means the consolidated substrate-gravity field equation can include the $a_0$-content cleanly without requiring additional kernel-profile-rescaling conditions. This is a structural simplification relative to the YM-3 case.

---

## 8. Recommended Next Step

Proceed to **Arc_SG_4 (Substrate-Gravity Field Equation in Flat Background)**. File: `theory/Substrate_Gravity/Arc_SG_4_Substrate_Gravity_Field_Equation.md`. Scope: produce the consolidated substrate-gravity field equation for the flat-spacetime regime, combining Arc_SG_2's Newtonian sector + Arc_SG_3's $\ell_P$-invariant transition-regime $a_0$ sector + ECR cross-term composition. The equation should recover Newton at $a \gg a_0$, MOND-class behavior at $a \ll a_0$, and BTFR slope-4 as the macroscopic galactic-dynamics consequence. Form FORCED at substrate level; values INHERITED.

Estimated 2 sessions for Arc_SG_4 given the technical load.

### Decisions for you

- **Confirm $a_0$ scaling analysis.** $a_0 = c\,H_0/(2\pi)$ is invariant under $\ell_P \to 0$; FORCED by cosmological-horizon structure + retardation + holographic bound + substrate spin-statistics; structurally different from YM mass-gap scaling (which requires kernel-profile rescaling for continuum-limit survival).
- **Confirm FORCED vs INHERITED classification.** Existence + functional form + $2\pi$ prefactor + $\ell_P$-invariance FORCED; $H_0$ value + cosmological boundary conditions + kernel tail normalization INHERITED.
- **Confirm proceeding to Arc_SG_4 (consolidated substrate-gravity field equation) as the next deliverable.**

---

*Arc_SG_3 closes the $a_0$ kernel-profile-scaling analysis. Transition acceleration $a_0 = c\,H_0/(2\pi)$ is invariant under $\ell_P \to 0$; substrate origin is cosmological-horizon participation density (R_H = c/H_0) + T18 retardation + substrate spin-statistics + holographic bound at horizon scale. Three structural anchors all preserved under $\ell_P$ rescaling: (A1) cosmological-horizon participation density independent of substrate-cutoff scale; (A2) T18 forward-cone-only support FORCED at primitive level independent of finite kernel width; (A3) $2\pi$ prefactor FORCED with $\ell_P$-dependence cancelling between holographic-bound and substrate-spin-statistics normalizations. Continuum-limit survival is structurally automatic; no kernel-profile-rescaling condition required (qualitatively different from YM-3 mass-gap result). FORCED/INHERITED classification: existence + functional form $cH_0$ + $2\pi$ prefactor + $\ell_P$-invariance FORCED; $H_0$ value + cosmological boundary conditions + kernel tail normalization INHERITED. Sets up SG-4 (consolidated substrate-gravity field equation combining Newton + transition-regime $a_0$ via ECR cross-term) and SG-5 (BTFR slope-4 robustness; $a_0$-content's robustness now established). Arc_SG_4 (consolidated substrate-gravity field equation) is the next deliverable.*
