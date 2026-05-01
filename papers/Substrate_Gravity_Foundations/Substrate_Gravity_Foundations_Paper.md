# Foundations of Substrate Gravity
## From Newtonian Limit to Curvature Emergence in the Event Density Framework

**Allen Proxmire**
**Collaborator:** Claude (AI collaborator)
**April 2026**
**Series:** Event-Density Foundational Theorems — Substrate Gravity Foundations

---

## Abstract

The Event Density (ED) program presents a substrate ontology in which classical gravitation emerges as a structural consequence of substrate participation-channel dynamics rather than as a fundamental field theory. This paper consolidates the closed structural-foundation work of the program's substrate-gravity sector into a single architectural-and-substrate account spanning flat-background regime through curvature emergence. **Theorem T19** derives Newton's gravitational constant $G = c^3\ell_P^2/\hbar$ from substrate participation imbalance + cumulative-strain mechanism + holographic participation-count bound. **Theorem T20** derives the transition acceleration $a_0 = c\,H_0/(2\pi)$ from cosmological-horizon participation density + retardation + substrate spin-statistics + holographic bound; the result is $\ell_P$-invariant under continuum limit, structurally distinct from substrate-cutoff-anchored mass-gap mechanisms in other ED sectors. The **ED Combination Rule** $a = \sqrt{a_N\,a_0}$ supplies the substrate-level geometric-mean composition between Newton-class and transition-class accelerations. **Theorem T21** derives the baryonic Tully-Fisher relation $v^4 = G\,M\,a_0$ as a substrate consequence of T19 + T20 + ECR. Under DCGT (Diffusion Coarse-Graining Theorem) the substrate-gravity content consolidates into the modified Poisson equation $\nabla\cdot[\mu(|\nabla\Phi|/a_0)\nabla\Phi] = 4\pi G\rho_m$ with FORCED asymptotic constraints; BTFR slope-4 is robust under all admissible kernel-profile / interpolation-function / substrate-discreteness variations.

The curvature-emergence extension (Arc ED-10) identifies the substrate cumulative-strain four-index object as the load-bearing curvature degree of freedom and produces an acoustic-metric-class scalar-tensor covariantization $\nabla_\mu[\mu(\sqrt{g^{\alpha\beta}\nabla_\alpha\Phi\nabla_\beta\Phi}/a_0)\nabla^\mu\Phi] = 4\pi G\,T$ as the substrate-FORCED covariant generalization. The covariant equation reduces to the flat-background modified Poisson equation in the weak-field limit; it preserves OS positivity + ghost-freedom + gradient stability under structural conditions; deep-MOND superluminality is structurally inherited from the substrate-derivation chain as the only structural cost. The verdict is **conditional-positive at structural-suggestive level** parallel in form and honesty to the program's NS-Smoothness Intermediate Path C and Yang-Mills Clay-relevance verdicts. **No claim of general relativity emergence is made**; the Einstein equation $G_{\mu\nu} = 8\pi G\,T_{\mu\nu}$ remains SPECULATIVE per ED-Phys-10 acoustic-metric-only baseline. What ED *does* deliver is a substrate-grounded architectural account of Newtonian gravity + MOND-class behavior + BTFR slope-4 + acoustic-metric curvature emergence with explicit form-FORCED / value-INHERITED demarcation. The paper is the canonical substrate-gravity-and-curvature-emergence reference for the ED program.

---

## 1. Introduction

### 1.1 Motivation

Classical gravitation is presented in standard physics as either Newton's law of universal gravitation (a phenomenological inverse-square attractive force) at solar-system scales, or as Einstein's general relativity (a fundamental dynamical field theory of the spacetime metric) at relativistic scales. The MOND-class modification — Milgrom's hypothesis $\mu(|\mathbf{a}|/a_0)\mathbf{a} = \mathbf{a}_N$ at the level of acceleration scaling — was introduced phenomenologically to explain galactic rotation curves without invoking dark matter, and has been extensively studied as both a phenomenological framework and via various covariantization attempts (RAQUAL, scalar-tensor MOND, full TeVeS, etc.) since Bekenstein-Milgrom 1984. The empirical regularity of the baryonic Tully-Fisher relation $v^4 \propto M$ across galaxy samples is one of the strongest empirical anchors of the MOND-class framework; standard physics has no first-principles derivation of the slope-4 power.

The Event Density (ED) program supplies a substrate ontology under which Newton's gravitational coupling, the MOND transition acceleration $a_0$, the geometric-mean composition rule between Newton-class and transition-class regimes, the BTFR slope-4 relation, and the modified-Poisson-class field equation all emerge as substrate consequences of a single set of substrate primitives. The goal is not to replace general relativity at the constructive-rigorous level, but to identify the substrate-derivation chain that produces the leading-order classical-gravitation content + its empirically-anchored MOND-class extensions.

### 1.2 Relation to ED Program

The substrate-gravity content sits within the broader Event Density structural-foundation work that includes Phase-1 QM emergence (sixteen forced theorems for the four QM postulates), the closed structural-foundation theorems T17 (gauge-fields-as-rule-type), T18 (V1 kernel retardation), Theorem N1 (V1 finite-width vacuum kernel), Theorem GR1 (V1 with Synge world function on curved spacetime), and the substrate-to-continuum bridge theorem DCGT (Arc D, 2026-04-30). The substrate-gravity work draws on T18 + Theorem N1 + GR1 + DCGT directly; the form-FORCED / value-INHERITED methodology is consistent across every ED program sector.

The substrate-gravity content has been developed across three closed arcs: (a) the original substrate-gravity arc (T19 / T20 / ECR / T21, 2026-04-27/28), (b) the Substrate Gravity Extension Arc (Arc SG, 2026-04-30) consolidating the closed substrate-gravity work under DCGT methodology + producing the modified Poisson equation, (c) the Curvature Emergence Arc (Arc ED-10, 2026-04-30) extending to acoustic-metric-class curvature emergence + producing the scalar-tensor covariantization. The present paper integrates all three arcs into a single canonical reference.

### 1.3 Scope

The paper covers the flat-background regime + curvature-emergent regime under the acoustic-metric-class baseline of ED-Phys-10. Scope items:

- Substrate origin of Newton's $G$ and the transition acceleration $a_0$.
- Substrate origin of the geometric-mean composition rule.
- BTFR slope-4 derivation + robustness audit.
- Modified Poisson equation as flat-background substrate-gravity field equation.
- Curvature-emergent scalar-tensor covariantization.
- OS positivity + ghost-freedom + gradient-stability audit at structural-suggestive level.

### 1.4 Non-goals

Explicitly out of scope:

- **No claim of deriving general relativity.** The Einstein equation $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ remains SPECULATIVE per ED-Phys-10 acoustic-metric-only baseline.
- **No new primitives.** The thirteen-primitive substrate framework is preserved throughout.
- **No cosmology or dark-energy modeling beyond what $a_0$ supplies.** Specific cosmological-scale physics (vacuum energy, dark-energy equation of state, structure formation) out of scope.
- **No metric dynamics beyond what substrate structure forces.** Gravitational waves, black-hole solutions, cosmological metric evolution are addressed only insofar as substrate-derivation FORCES specific structural content.
- **No claim of solving any Clay Millennium Problem.** Curvature emergence is not itself a Clay problem; the structural-positive content is the substrate-grounding of MOND-class behavior.

---

## 2. Substrate Primitives and Participation Structure

The ED substrate consists of a network of *chains* — fundamental discrete entities that carry participation channels between substrate-level events. Chains support participation channels via finite-bandwidth commitments at substrate-level events; the substrate dynamics is governed by thirteen primitives (P-01 through P-13) that fix the structural content without committing to numerical values at substrate level.

**V1 kernel** — the vacuum-response participation kernel — supplies the substrate-level finite-width spatial smoothing structure. By Theorem N1 (Arc N closure), the V1 kernel has finite spatial width $\sim\ell_P$, smooth profile, isotropic by substrate-level rotational invariance, and positive Fourier transform. By Theorem 18 (Arc B closure), the V1 kernel has forward-cone-only support, anchoring the kernel-level arrow of time at substrate level.

**Participation density** — the substrate-level participation-channel density at a given spacetime point — is the scalar-field-class quantity that maps under DCGT (Arc D closure) to the macroscopic mass density at fluid-mechanical / gravitational-substrate scale. Variations in participation density source the gravitational potential gradient via the acoustic-metric reading of Arc ED-10.

**Directional bias** — the substrate-level orientation-bearing participation structure — supplies the directional-field-class quantities that map to vector fields (velocity, gauge potentials, magnetic field) at continuum scale. Per ED-I-06 (Fields and Forces, Feb 2026), the three field classes (directional, scalar, curvature-like) are exhaustive at substrate level.

**Cumulative strain** — the substrate-level multi-point participation-channel correlation that captures how parallel transport across multi-point substrate loops deviates from triviality — is the load-bearing substrate quantity for both T19's substrate-gravity mechanism and Arc ED-10's curvature-emergent degrees of freedom. The four-point cumulative-strain object supplies the substrate origin of Riemann curvature at continuum scale.

**DCGT (Diffusion Coarse-Graining Theorem)** — the substrate-to-continuum bridge theorem closed in Arc D — establishes the methodology for deriving continuum-scale equations from substrate flux statistics under hydrodynamic-window scale separation $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$. Multi-scale expansion of substrate fluxes produces continuum-scale operators with form-FORCED structure + value-INHERITED coefficients. DCGT covers scalar diffusion (mobility-channel), directional-field viscosity, V1-second-moment hyperviscous corrections, V5 cross-chain temporal-memory contributions, T17-minimal-coupling matter-source content, and (per Arc ED-10 §3) generalized to curvature-like-field-class content via Laplace-Beltrami operator + V1-second-moment curvature-coupling terms.

These five structural ingredients (V1 kernel, participation density, directional bias, cumulative strain, DCGT) form the substrate basis of the substrate-gravity work that follows.

---

## 3. Theorem T19 — Newton Constant from Substrate

### Theorem statement

> **Theorem T19 (Newton's gravitational constant from substrate, FORCED-unconditional).** *Under ED substrate primitives + cumulative-strain mechanism + holographic participation-count bound + dimensional-analysis closure, Newton's gravitational constant takes the form*
>
> $$G \;=\; \frac{c^3\,\ell_P^2}{\hbar}.$$
>
> *The form is FORCED at substrate level by the dimensional-analysis-tight combination of substrate length scale $\ell_P$, substrate-level light-speed scale $c$, and substrate-level participation-quantum scale $\hbar$. The numerical value of $G$ is INHERITED at value layer through $\ell_P$, $c$, $\hbar$ as substrate inputs.*

### Derivation sketch

The substrate-derivation chain runs through three structural anchors:

**(a) Substrate participation imbalance.** Mass content $M$ at a substrate position sources a participation-density bias that propagates outward through the chain network with $1/r^2$ geometric dilution (3D spherical isotropy). The participation-flux density at radius $r$ is set by the total mass-content modulated by substrate participation-conservation.

**(b) Cumulative-strain mechanism.** The substrate-level cumulative strain across a substrate region of size $r$ accumulates from the participation imbalance integrated over the region; the strain-content scales with the holographic participation-count bound at the region's boundary.

**(c) Holographic participation-count bound + dimensional analysis.** The participation-count at scale $r$ is bounded as $N \sim r^2/\ell_P^2$ (holographic-class). Combining this with the substrate-level proper-time scale ($\sim \ell_P/c$) and the substrate-level participation-quantum ($\hbar$) gives the dimensionally-tight combination producing $G$.

The detailed derivation closure is in `arcs/arc-SG/`; the result is FORCED at substrate level with value INHERITED via $\ell_P$ + $c$ + $\hbar$.

### Structural meaning

Newton's gravitational coupling is not a fundamental constant in the ED framework; it is a substrate-derived combination of more fundamental substrate scales. The $\ell_P^2$ scaling identifies $G$ as a substrate-cutoff-anchored quantity: variations of the substrate length scale $\ell_P$ produce proportional variations in $G$ at value layer. The substrate-derivation supplies a structural reason why $G$ has its specific dimensional form — it is the unique combination of substrate scales producing a quantity with $G$'s dimensions.

This positions Newton's gravity as a substrate-structural feature rather than a phenomenologically-fitted coupling. Standard physics treats $G$ as an empirical constant; the ED substrate-derivation supplies its substrate origin while preserving the empirical-input nature of the numerical value.

---

## 4. Theorem T20 — Transition Acceleration $a_0$

### Theorem statement

> **Theorem T20 (Transition acceleration from substrate, FORCED-unconditional).** *Under ED substrate primitives + cosmological-horizon participation density + T18 retardation + substrate spin-statistics + holographic bound at horizon scale, the transition acceleration takes the form*
>
> $$a_0 \;=\; \frac{c\,H_0}{2\pi}.$$
>
> *The form is FORCED at substrate level + the $2\pi$ prefactor is structurally derived from substrate spin-statistics + holographic-bound normalizations. The numerical value of $a_0$ depends on the cosmological Hubble parameter $H_0$, INHERITED at value layer.*

### $\ell_P$-invariance under continuum limit

Per Arc_SG_3 (Substrate Gravity Extension), $a_0$ is **invariant under $\ell_P \to 0$**. The substrate-derivation routes through three anchors all preserved under substrate-cutoff scale variation:

**(A1) Cosmological-horizon participation density.** $R_H = c/H_0$ is independent of substrate-cutoff scale. The horizon-scale participation density depends on cosmological parameters ($H_0$, vacuum-energy content) which are independent of $\ell_P$.

**(A2) Retardation structure (T18).** Forward-cone-only support of V1 kernel is FORCED at primitive level (Arc B closure); preservation under $\ell_P \to 0$ structural.

**(A3) $2\pi$ prefactor.** Substrate-spin-statistics + holographic-bound normalizations cancel the $\ell_P$-dependence ($N \sim R_H^2/\ell_P^2$ × substrate-spin-statistics-normalization-with-$\ell_P^{-2}$-suppression). The prefactor is dimensionless + $\ell_P$-independent.

### Horizon-scale participation density

The cosmological event horizon at radius $R_H = c/H_0$ supplies a substrate-level participation-density boundary. Beyond $R_H$, no substrate participation channels can communicate with the local participation network within the cosmological time available; the horizon truncates substrate participation-flux integration at scale $R_H$. The horizon-truncation at scale $R_H$ produces the transition-regime acceleration scale $a_0 \sim cH_0$ via dimensional analysis + substrate-derivation chain.

### Contrast with YM mass-gap scaling

The substrate origin of $a_0$ is fundamentally different from the substrate origin of mass gaps in other ED sectors. Specifically, contrast with the Yang-Mills mass-gap mechanism (Arc YM-3):

| Substrate quantity | Substrate scale | Continuum-limit survival |
|---|---|---|
| YM mass gap $m_\mathrm{eff}^2$ | $\ell_P^{-2}$ (substrate cutoff, UV) | **Conditional** on kernel-profile rescaling |
| $a_0$ transition acceleration | $cH_0$ (cosmological horizon, IR) | **Automatic**; no rescaling required |

The YM mass gap is a *substrate-cutoff effect* (UV); $a_0$ is a *cosmological-horizon effect* (IR). YM mass gap requires kernel-profile rescaling for continuum-limit survival; $a_0$ inherits no $\ell_P$-dependence and survives automatically. This structural distinction is one of the key findings of the substrate-gravity arc.

---

## 5. ECR — ED Combination Rule

### Statement

The ED Combination Rule (ECR), closed in `arcs/arc-SG/ED_combination_rule.md`, states that the magnitude of the substrate-gravitational acceleration is the geometric mean of the Newton-class and transition-class accelerations in the deep-MOND regime:

$$a \;=\; \sqrt{a_N\,a_0}, \qquad a_N \;=\; |\nabla\Phi_N|,$$

where $\Phi_N$ is the Newtonian potential satisfying the standard Poisson equation. Squaring,

$$a^2 \;=\; a_N\,a_0,$$

at the magnitude level of the substrate-gravitational acceleration in the deep-MOND regime.

### Substrate origin

ECR is FORCED at substrate level by the participation-curvature combination at the cross-term scale between Newton-class (substrate-cutoff-anchored) and transition-class (cosmological-horizon-anchored) substrate sectors. The substrate-derivation routes through the cross-term $\sqrt{GMa_0}\cdot\log(R/R_0)$ in the deep-MOND regime; the geometric-mean composition reflects the substrate-level participation-curvature interpolation between the two regimes.

### Role in deep-MOND behavior

ECR's geometric-mean composition is the substrate origin of MOND-class behavior. Specifically:

- In the high-acceleration regime ($a_N \gg a_0$), the substrate-gravity acceleration approaches $a_N$ — Newton's law is recovered.
- In the deep-MOND regime ($a_N \ll a_0$), the substrate-gravity acceleration approaches $\sqrt{a_N\,a_0}$ — the substrate-level MOND-class behavior.
- The crossover occurs at acceleration scale $a_0$.

ECR supplies the structural framework within which the modified Poisson equation (Section 7) emerges as the field-equation-level expression of the substrate composition.

### Naming convention

Per program-level memory: the substrate rule is called "the ED Combination Rule" (ECR) — no number assigned. "P11" is reserved for Primitive 11 (commitment-irreversibility); "ED-11" should not be used in naming.

---

## 6. Theorem T21 — BTFR Slope-4

### Derivation

In the deep-MOND regime, ECR supplies $a^2 = a_N\,a_0$ with $a_N = GM/r^2$ for spherical mass distribution. Substituting:

$$a^2 \;=\; \frac{G\,M\,a_0}{r^2} \quad\Longrightarrow\quad |a(r)| \;=\; \frac{\sqrt{G\,M\,a_0}}{r}.$$

For a circular orbit at radius $r$, centripetal balance gives $v^2/r = |a(r)|$, hence $v^2 = \sqrt{G\,M\,a_0}$. Squaring,

$$\boxed{\;v^4 \;=\; G\,M\,a_0.\;}$$

This is the **baryonic Tully-Fisher relation** at slope-4 — Theorem T21.

### Why slope-4 is FORCED

Slope-4 is FORCED by:

- **ECR's geometric-mean composition** at substrate level (FORCED via closed-arc derivation).
- **Spherical symmetry** of test-mass distribution (assumed for galactic-rotation-curve idealization at large radii).
- **Circular-orbit centripetal balance** (kinematic).
- **Dimensional analysis.** The only dimensional combination of $G$, $M$, and $a_0$ producing [velocity]⁴ is $GMa_0$.

Each ingredient is structurally backed; their combination yields slope-4 as a substrate consequence.

### Robustness

Per Arc_SG_5 (BTFR robustness audit), slope-4 is **structurally robust** under all admissible variations:

- V1 kernel-profile variations (within Theorem N1 admissibility class).
- Interpolation-function $\mu(x)$ variations (within asymptotic-constraint class — Section 7).
- Substrate-discreteness variations (within DCGT hydrodynamic-window conditions).
- Coarse-graining-window variations (within hydrodynamic window).

ED substrate-gravity predicts **zero intrinsic scatter** in the deep-MOND asymptotic regime. Observed BTFR scatter (sub-0.1 dex in SPARC samples; slope $\sim 3.85 \pm 0.15$) is dominated by baryonic-mass measurement uncertainty + transition-regime $\mu(x)$ + baryonic geometry. This is consistent with empirical galaxy-rotation-curve data and supplies an empirical anchor for the substrate-derivation chain.

---

## 7. Arc SG Synthesis — Flat-Background Substrate Gravity

### Consolidated field equation

Under DCGT methodology, the closed substrate-gravity work consolidates into the modified Poisson equation in flat background:

$$\boxed{\;\nabla\cdot\!\left[\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi\right] \;=\; 4\pi G\,\rho_m,\;}$$

with substrate-derived gravitational coupling $G = c^3\ell_P^2/\hbar$ (T19), substrate-derived transition acceleration $a_0 = c\,H_0/(2\pi)$ (T20, $\ell_P$-invariant), and dimensionless interpolation function $\mu(x)$ satisfying FORCED asymptotic constraints.

### Newtonian limit

In the high-acceleration limit ($|\nabla\Phi| \gg a_0$, equivalently $x \gg 1$), $\mu(x) \to 1$ and the field equation reduces to the standard Newtonian Poisson equation:

$$\nabla^2\Phi \;=\; 4\pi G\,\rho_m.$$

Newton's law of gravitation $\Phi(r) = -GM/r$ + force law $\mathbf{F} = -GMm/r^2\,\hat r$ are recovered as standard 3D Green's-function solutions.

### Deep-MOND limit

In the low-acceleration regime ($|\nabla\Phi| \ll a_0$, equivalently $x \ll 1$), $\mu(x) \to x$ and the field equation reduces to:

$$\nabla\cdot\!\left[\frac{|\nabla\Phi|}{a_0}\,\nabla\Phi\right] \;=\; 4\pi G\,\rho_m.$$

For spherical symmetry, the first integral outside the source gives $|\nabla\Phi|^2 = GMa_0/r^2$ (Section 6 derivation); circular-orbit balance produces BTFR slope-4 $v^4 = GMa_0$.

### BTFR

BTFR slope-4 follows from the deep-MOND asymptotic + spherical symmetry + circular-orbit balance + dimensional analysis. T21's empirical-anchor result is recovered as a substrate consequence.

### FORCED vs INHERITED structure

**FORCED at substrate level:**
- Modified Poisson equation form (DCGT scalar-diffusion + ECR substrate composition).
- Asymptotic constraint $\mu(x) \to 1$ at $x \to \infty$ (Newtonian-regime substrate consistency).
- Asymptotic constraint $\mu(x) \to x$ at $x \to 0$ (ECR substrate composition).
- BTFR slope-4 (deep-MOND asymptotic + dimensional analysis).
- Reduction to Newtonian Poisson at high acceleration.

**INHERITED at value layer:**
- Detailed shape of $\mu(x)$ in transition regime (multiple structurally-equivalent forms: "simple" $x/\sqrt{1+x^2}$, "standard" $x/(1+x)$, exponential, rational families).
- Numerical values of $G$ and $a_0$ (via $\ell_P$ and $H_0$).
- Cosmological boundary conditions; specific mass distributions.

The flat-background substrate-gravity sector is structurally complete at the field-equation level under DCGT methodology.

---

## 8. Curvature Emergence (Arc ED-10)

### Curvature-like degrees of freedom

Per Arc_ED10_2, the substrate quantities with curvature-like index structure are:

- **Cumulative-strain four-index object** — the load-bearing substrate degree of freedom for curvature. The genuine independent substrate quantity capturing loop-holonomy-class participation-curvature content.
- **Participation-curvature tensor from GR1** — diagnostic / cross-checking; derived from underlying metric structure.
- **Directional-bias-gradient commutators** — secondary; right index structure but not curvature-vanishing in flat space.
- **Kernel-shape second-derivative structure** — diagnostic; responds to curvature, doesn't produce it.

The cumulative-strain four-index object is uniquely the substrate origin of Riemann curvature at continuum scale.

### Acoustic metric

The substrate participation-channel network supplies a metric-like quantity at continuum scale via the participation-density-modulated effective metric:

$$g_{\mu\nu}^\mathrm{acoustic}(x) \;\propto\; \bigl(\text{participation-density-modulated effective metric}\bigr).$$

The acoustic-metric reading is the standard ED interpretation per ED-Phys-10 acoustic-metric-only baseline: the metric is *kinematic* (a continuum-level summary of substrate participation-density variation) rather than *dynamical* (an independent field with its own equation of motion). The Christoffel-class connection follows kinematically; the Riemann-like curvature object follows kinematically from the metric.

### Weak-field reduction to SG-4

Per Arc_ED10_3, the curvature-emergent framework reduces to the flat-background modified Poisson equation in the $g_{\mu\nu}\to\eta_{\mu\nu}$ limit under three load-bearing structural assumptions:

- **(A1) Acoustic-metric class** (kinematic metric, not fundamental dynamical).
- **(A2) Levi-Civita connection** (metric-derived kinematically).
- **(A3) Subleading curvature-coupling coefficients** ($\alpha_R$, $\beta_{R_{\mu\nu}}$ from curved-DCGT operator $\ell_P^2$-suppressed at leading weak-field order).

Standard GR weak-field-limit identities are preserved: $h_{00} \approx 2\Phi/c^2$ FORCED + $R_{00} \propto \nabla^2\Phi$ FORCED + curved-DCGT operator reduces to flat Laplacian at leading order FORCED. All six SG-6 weak-field-limit prerequisites verified.

### Scalar-tensor covariantization

Per Arc_ED10_4, three structural families audited against five substrate-compatibility constraints:

| Family | Status |
|---|---|
| TeVeS-class scalar-tensor (in scalar-tensor reduced form) | **Compatible** — passes all five constraints |
| $f(R)$-class | **Inadmissible** — violates ED-Phys-10 (introduces scalaron + dynamical metric) |
| Bimetric-class | **Equivalent to TeVeS-class** under acoustic-metric identification |

The substrate FORCES the scalar-tensor acoustic-metric covariantization as the unique compatible candidate-form. The result is structurally equivalent to RAQUAL / scalar-tensor MOND covariantizations in the standard literature; the ED-program-specific contribution is the substrate-derivation chain identifying this form as substrate-FORCED.

### OS positivity + ghost-free + gradient-stable

Per Arc_ED10_5:
- **OS positivity preserved** under (C1) monotone-increasing $\mu(x)$ + (C2) kinetic-matrix positivity $\mu(x) + x\mu'(x) > 0$ + (C3) V1 positive Fourier transform.
- **Ghost-freedom holds** under (C2). Kinetic matrix positive-definite in transverse + longitudinal directions.
- **Gradient stability holds** under (C2). No spatial-mode instabilities at linearized scalar-sector level.

Conditions (C1)–(C3) are structurally backed by closed-arc work; (C1) and (C2) FORCED in asymptotic limits + standard $\mu(x)$ forms; (C3) FORCED unconditionally by Theorem 18 + Theorem N1.

### Deep-MOND superluminality (structural-conditional)

Per Arc_ED10_5 Step 3: in the deep-MOND regime ($\mu \to x$, $\mu' \to 1$), the longitudinal scalar-mode propagates superluminally relative to the acoustic light cone (longitudinal/transverse eigenvalue ratio = 2; longitudinal cone wider by factor $\sqrt{2}$). The superluminality is **structurally FORCED by the substrate-derivation chain** that produces SG-4 + ECR + BTFR slope-4. Avoidance routes structurally inadmissible:

- Adding an independent vector field (Bekenstein full TeVeS) violates the no-new-primitives constraint.
- Modifying $\mu(x)$ to $\mu' \to 0$ in deep-MOND violates the BTFR slope-4 FORCED-asymptotic.

Superluminality is the structural cost of obtaining the substrate-derived MOND-covariantization. Causality is preserved via effective $g_\mathrm{eff}$-cone consistency in physically reasonable backgrounds (standard scalar-tensor MOND-covariantization-literature view).

---

## 9. Covariant Field Equation

The substrate-FORCED covariant generalization of the modified Poisson equation (Section 7) is:

$$\boxed{\;\nabla_\mu\!\left[\mu\!\left(\frac{\sqrt{g^{\alpha\beta}\nabla_\alpha\Phi\,\nabla_\beta\Phi}}{a_0}\right)\nabla^\mu\Phi\right] \;=\; 4\pi G\,T,\;}$$

with:

- $g_{\mu\nu}$ the acoustic metric (Section 8) — kinematic-summary of substrate participation-density variation per ED-Phys-10 baseline.
- $\nabla_\mu$ the metric-covariant derivative associated with the Levi-Civita connection of $g_{\mu\nu}$.
- $\mu(x)$ the dimensionless interpolation function with FORCED asymptotic constraints from Section 7 ($\mu(x) \to 1$ at $x \to \infty$, $\mu(x) \to x$ at $x \to 0$).
- $T$ the trace of the matter stress-energy tensor (or $T^{00}/c^2$ in the static limit), serving as the covariant scalar source.
- $a_0 = c\,H_0/(2\pi)$ from Theorem T20.
- $G = c^3\ell_P^2/\hbar$ from Theorem T19.

**Structural status.** Form FORCED at substrate level by Arc_ED10_4 candidate-form selection chain: scalar-tensor acoustic-metric uniquely substrate-compatible; $f(R)$ inadmissible; bimetric collapses to scalar-tensor. Weak-field limit reduces to Section 7's modified Poisson equation under three load-bearing structural assumptions. OS positivity preserved + ghost-free + gradient-stable under structural conditions; deep-MOND superluminality structurally inherited.

**This is not GR.** No Einstein-Hilbert kinetic term for the metric; no dynamical-metric-as-fundamental-field content. The metric is acoustic-class kinematic; the equation is a substrate-derived covariantization of the MOND-class modified Poisson equation, structurally equivalent to the standard RAQUAL / scalar-tensor MOND covariantizations in the literature with the ED-program-specific contribution being the substrate-derivation chain.

---

## 10. Structural Verdict

### What is FORCED at substrate level

- Newton's gravitational coupling form $G = c^3\ell_P^2/\hbar$ (T19).
- Transition acceleration form $a_0 = c\,H_0/(2\pi)$ + $\ell_P$-invariance under continuum limit (T20).
- ED Combination Rule $a = \sqrt{a_N\,a_0}$ (ECR).
- BTFR slope-4 relation $v^4 = G\,M\,a_0$ (T21).
- Modified Poisson equation form + asymptotic constraints on $\mu(x)$ (Section 7).
- Substrate cumulative-strain four-index → Riemann-class object (Section 8).
- Acoustic-metric + Christoffel-class connection + Riemann-like curvature mappings (Section 8).
- Scalar-tensor acoustic-metric covariantization as the unique substrate-compatible form (Section 9).
- Weak-field limit reduction of covariant equation to flat-background modified Poisson (Section 8).
- OS positivity + ghost-freedom + gradient stability under structural conditions (Section 8).

### What is INHERITED at value layer

- Numerical values of $G$ and $a_0$ (via $\ell_P$ and $H_0$).
- Detailed shape of $\mu(x)$ in transition regime.
- Curvature-coupling coefficients $\alpha_R$, $\beta_{R_{\mu\nu}}$ at value layer.
- Cosmological boundary conditions; specific mass distributions.
- Specific compact gauge group choice (for the matter sector via T17 minimal coupling).

### What is structurally conditional

- **Deep-MOND superluminality** is structurally FORCED in the deep-MOND regime as the structural cost of the substrate-derivation chain. Avoidance routes structurally inadmissible.
- **Curvature-coupling coefficients must remain subleading** for the weak-field limit to reduce cleanly to SG-4. Per closed-arc work; not structurally proven within Arc ED-10.
- **Acoustic metric must remain Lorentzian and non-degenerate.** FORCED in non-extreme regimes per ED-Phys-10; could fail near extreme substrate-density configurations (out of scope).

### What is not obtained

- **No general relativity emergence.** The Einstein equation $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ is not derived; remains SPECULATIVE per ED-Phys-10 acoustic-metric-only baseline.
- **No metric dynamics beyond kinematic content.** Gravitational waves, black-hole solutions, cosmological metric evolution out of scope.
- **No prediction of numerical $G$, $a_0$, or $H_0$ values.** Numerical content INHERITED throughout.
- **No solution of any Clay Millennium Problem.** Curvature emergence is not itself a Clay problem.
- **No constructive-rigorous OS reconstruction theorem.** OS-positivity audit is structural-suggestive level only.

The verdict is **conditional-positive at structural-suggestive level** parallel in form and honesty to the program's NS-Smoothness Intermediate Path C verdict for Clay-NS and the Yang-Mills Clay-relevance verdict.

---

## 11. Discussion and Outlook

### Relation to MOND literature

The substrate-derived modified Poisson equation (Section 7) is structurally equivalent to the standard MOND-class AQUAL field equation introduced by Bekenstein-Milgrom 1984. The substrate-derived scalar-tensor covariantization (Section 9) is structurally equivalent to RAQUAL / scalar-tensor MOND covariantizations studied since the same period. The ED-program-specific contribution is **not** novel field-equation content; it is the **substrate-derivation chain** identifying these equations as substrate-FORCED rather than phenomenologically chosen. The originality lies in the substrate-grounding of form-selection, not in the form itself.

This positions ED's substrate-gravity work as a *foundational* contribution to the MOND-class research program rather than as an additional phenomenological MOND-variant. Whether MOND-class behavior is the correct phenomenological framework for galactic dynamics + cosmological-scale gravity is an empirical question that the ED substrate-derivation does not by itself resolve; what the ED substrate-derivation supplies is a structural reason *why* MOND-class equations could be expected to emerge from a deeper structural framework.

### Relation to analog gravity

The acoustic-metric reading of curvature emergence (Section 8) connects to the analog-gravity research program studying acoustic / hydrodynamic / condensed-matter analogs of gravitational physics. In the standard analog-gravity framework, the metric emerges as the effective metric experienced by acoustic perturbations propagating through a flowing fluid; the metric is kinematic in the sense identified here. ED's substrate-derivation supplies an analog-gravity-class metric-emergence at the deeper substrate level, with the difference that ED's substrate is not a fluid in the standard hydrodynamic sense but a participation-channel network. The acoustic-metric emergence is structurally common; the substrate identification is ED-specific.

### Future arcs

Several future arcs could extend the substrate-gravity content:

- **Substrate Gravity Phase-2.** Optional extensions within the flat-background regime — dynamic mass-distribution-evolution effects, cosmological-perturbation-class extensions, explicit MOND empirical-fit work. Discretionary scope.
- **Cosmological extensions.** The transition acceleration $a_0 \propto H_0$ supplies a cosmological-scale connection that could be developed further at the level of substrate-gravity-cosmology coupling. Out of scope of the present paper but a natural extension direction.
- **Stronger curvature regimes.** If ED-Phys-10's acoustic-metric-only baseline is revisited, the curvature-emergent framework could potentially extend to genuinely curvature-dominated regimes (black-hole-class substrate configurations, gravitational-wave-class metric perturbations). This would require structural commitment beyond the present arc and is not undertaken here.

### ED Program Manifesto

The substrate-gravity content presented here is one sector of the broader Event Density program. The full program covers Phase-1 QM emergence, the closed structural-foundation theorems (T17 / T18 / N1 / GR1 / DCGT), the NS / MHD applied-arc program with NS Synthesis Paper, the Yang-Mills arc, and the present substrate-gravity work. A long-horizon ED Program Manifesto would consolidate all of this into a single book-length program-overview publication. The present substrate-gravity-foundations paper + the existing NS Synthesis Paper + the ED-QFT Unified Overview Paper form the publication-grade backbone for that future Manifesto.

---

## References

(Placeholder for later insertion. Anticipated references include:)

- *Event Density: One Substrate, Three Domains — A Structural Account of Quantum Mechanics, Galactic Gravity, and Universal Soft-Matter Mobility* (Proxmire 2026). Earlier program-overview.
- *The Architectural Foundations of Navier-Stokes in Event Density* (Proxmire 2026). NS / MHD / YM closed-arc reference paper.
- *The Event-Density Foundations of Quantum Field Theory: A Unified Substrate-to-Continuum Overview* (Proxmire 2026). Program-level synthesis.
- *The Primitive-Level Arrow of Time in Event Density: The Closure of Arc B and Theorem 18* (Proxmire 2026). T18 paper.
- *Gauge Fields as Forced Rule-Type Structure: Theorem 17* (Proxmire 2026). Arc Q closure paper.
- *Fields and Forces in Event Density* (Proxmire, Feb 2026, ED-I-06). Ontological framework paper.
- Bekenstein, J.D. and Milgrom, M. (1984). Does the missing mass problem signal the breakdown of Newtonian gravity? Astrophys. J. 286.
- Milgrom, M. (1983). A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis. Astrophys. J. 270.
- Bekenstein, J.D. (2004). Relativistic gravitation theory for the modified Newtonian dynamics paradigm. Phys. Rev. D 70.
- Sanders, R.H. and McGaugh, S.S. (2002). Modified Newtonian dynamics as an alternative to dark matter. Annu. Rev. Astron. Astrophys. 40.
- Lelli, F., McGaugh, S.S., Schombert, J.M. (2016). SPARC: Mass models for 175 disk galaxies with Spitzer photometry and accurate rotation curves. Astron. J. 152.

---

*Foundations of Substrate Gravity: From Newtonian Limit to Curvature Emergence in the Event Density Framework. Canonical substrate-gravity-and-curvature-emergence reference for the ED program. Integrates T19 (Newton's $G$ from substrate) + T20 ($a_0$ horizon-scale + $\ell_P$-invariant) + ECR (geometric-mean composition) + T21 (BTFR slope-4) + Arc SG (flat-background modified Poisson equation) + Arc ED-10 (scalar-tensor acoustic-metric covariantization) into a single publication-grade synthesis. Form-FORCED / value-INHERITED methodology consistent across every section. Conditional-positive structural verdict parallel in form and honesty to NS-Smoothness Intermediate Path C and Yang-Mills Clay-relevance verdicts. No claim of GR derivation; ED-Phys-10 acoustic-metric guardrails preserved. Substrate-derivation chain identifies MOND-class field equation + scalar-tensor covariantization as substrate-FORCED + supplies structural reason for BTFR slope-4 + identifies deep-MOND superluminality as structural cost.*
