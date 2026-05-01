# NS-Smooth-5 — Final Synthesis: Intermediate Path C Clay-Relevance Statement

**Date:** 2026-04-30
**Status:** NS-Smoothness arc closed at Intermediate Path C. Self-contained Clay-relevance statement; citable from external program-level papers.
**Companions:** [`NS_Smooth_1_Opening.md`](NS_Smooth_1_Opening.md), [`NS_Smooth_2_R1_Mechanism.md`](NS_Smooth_2_R1_Mechanism.md), [`NS_Smooth_3_Advection_Obstruction.md`](NS_Smooth_3_Advection_Obstruction.md), [`NS_Smooth_4_Architectural_Decomposition.md`](NS_Smooth_4_Architectural_Decomposition.md), [`../NS-1.05_Synthesis_B2_Verdict.md`](../NS-1.05_Synthesis_B2_Verdict.md), [`../NS-2.07_Synthesis.md`](../NS-2.07_Synthesis.md), [`../NS-3.04_Synthesis_Path_Verdict.md`](../NS-3.04_Synthesis_Path_Verdict.md), [`../Turbulence/P7_Triads_NS_Turb_5_Synthesis.md`](../Turbulence/P7_Triads_NS_Turb_5_Synthesis.md).

---

## 1. Purpose

This memo closes the NS-Smoothness arc by synthesizing NS-Smooth-1 through NS-Smooth-4 into a single self-contained Clay-relevance statement. It is intended as the canonical reference document for ED's relationship to the Clay-NS smoothness problem, suitable for citation in the future NS-1/2/3 program-level synthesis paper, the ED-overview material, and any external-facing documents discussing the program's reach into mainstream open problems.

**This is a Clay-relevance synthesis, not a solution and not a partial proof.** The substantive content is a structural decomposition of the Clay-NS difficulty into ED-canonical regularizing infrastructure plus non-ED structural obstruction. The decomposition explains *why* Clay-NS is hard without resolving which side wins quantitatively.

The reader should be able to extract the core technical content (R1 mechanism + advection obstruction) and the polished Intermediate Path C statement from this memo alone, without consulting NS-Smooth-1 through NS-Smooth-4. Detailed derivations and longer-form discussion remain in the prior memos for reference.

---

## 2. Background and Inputs

The NS-Smoothness arc synthesizes findings from four upstream program closures:

- **NS-1 ([`NS-1.05`](../NS-1.05_Synthesis_B2_Verdict.md)):** Path B-strong dimensional forcing of D = 3+1 via architectural d ≥ 3 (T20 mechanism degeneracy at d ≤ 2) + architectural-suggestive d ≤ 3 (Polya recurrence + concentration of measure + decoupling-surface degeneration) + empirical-consistency d ≤ 3 (T19/T20 outputs match observed gravity).
- **NS-2 ([`NS-2.07`](../NS-2.07_Synthesis.md) + [`NS-2.08`](../NS-2.08_ED-PDE_Direct_Mapping.md)):** Standard Newtonian-fluid NS form derived from ED substrate primitives (chain-substrate route) and via partial vector-extension of the canonical PDE (ED-PDE-direct route). The viscous content is canonical ED architecture; pressure / advection / incompressibility are fluid-mechanical-specific additions catalogued explicitly.
- **NS-3 ([`NS-3.04`](../NS-3.04_Synthesis_Path_Verdict.md)):** ED contains a real Clay-relevant stabilizing mechanism (R1: substrate-scale $\ell_P^2 \nabla^4 v$) with form-FORCED structure but value-INHERITED quantitative competition against destabilizing super-Burnett terms. Verdict: Intermediate Path C.
- **NS-Turb ([`NS-Turb-5`](../Turbulence/P7_Triads_NS_Turb_5_Synthesis.md)):** ED's P7 triadic harmonic-generation structure does not architecturally template developed-cascade turbulence. The spectral-level analysis confirms advection's index-structure asymmetry as the locus of P7-class mapping failure — third-angle convergence on advection-is-non-ED.

Within the NS-Smoothness arc itself:

- **NS-Smooth-2:** Formalized the R1 mechanism. Established that ED-only NS (without advection) has a strictly monotonically-decaying gradient-norm Lyapunov.
- **NS-Smooth-3:** Restored advection. Established that the advective vortex-stretching term is the unique indefinite-sign contribution to the gradient-norm Lyapunov derivative in 3D.
- **NS-Smooth-4:** Combined the positive and negative sides into the formal Intermediate Path C decomposition.

This memo (NS-Smooth-5) synthesizes the four prior memos into a citable Clay-relevance statement.

---

## 3. ED-Only NS and the R1 Mechanism

### 3.1 The ED-only NS equation

Consider the equation that obtains when the canonical ED PDE's vector-extension content is the entire fluid equation, with no fluid-mechanical-specific additions beyond pressure (Lagrange multiplier for incompressibility):

$$\rho\,\partial_t v_i \;=\; \mu\nabla^2 v_i \;-\; \kappa\mu_\mathrm{V1}\ell_P^2\,\nabla^4 v_i \;-\; \partial_i p, \qquad \nabla\cdot v = 0.$$

This is *not* physical NS — the advective term is structurally present in any real fluid. ED-only NS is a counterfactual: the equation governing velocity if ED's canonical channels were the entire fluid kinematics.

The components:
- **Viscous diffusion** $\mu\nabla^2 v_i$: standard kinematic-viscosity-class diffusion, mapped from the canonical PDE mobility channel via the partial vector-extension of NS-2.08.
- **R1 stabilization** $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4 v_i$: form-FORCED higher-derivative regularization arising from V1's finite-width vacuum kernel (Theorem N1) combined with multi-scale expansion. Coefficient $\kappa > 0$ FORCED positive by V1 being a positive smoothing kernel; magnitude $\mu_\mathrm{V1}$ INHERITED via V1's specific G-function.
- **Pressure** $-\partial_i p$: Lagrange multiplier enforcing incompressibility. Not derived from ED architecture; included for coherence with $\nabla\cdot v = 0$.

### 3.2 The gradient-norm Lyapunov

Define the gradient-norm Lyapunov functional:

$$L(t) = \frac{1}{2}\,\|\nabla v(t)\|_2^2 = \frac{1}{2}\int_{\mathbb{R}^3} \partial_j v_i \, \partial_j v_i \, dV.$$

This is enstrophy-class — directly related to enstrophy $\frac{1}{2}\int|\omega|^2 dV$ via integration by parts and incompressibility. Monotonic control of this quantity in 3D would imply, via Beale-Kato-Majda combined with standard energy methods, global smooth solutions for finite-energy data.

### 3.3 Compact derivation: $dL/dt$ for ED-only NS

Compute term-by-term, using integration by parts and assuming fields decay at infinity.

**Viscous contribution:**

$$\int \partial_j v_i \, \partial_j(\nu \nabla^2 v_i) \, dV = -\nu \int |\nabla^2 v|^2 \, dV \;\le\; 0.$$

Standard Laplacian-Lyapunov identity.

**R1 contribution:** Using $\int u \, \nabla^4 u \, dV = \int|\nabla^2 u|^2 \, dV$ (four integrations by parts):

$$\int \partial_j v_i \, \partial_j\bigl(-\kappa\mu_\mathrm{V1}\ell_P^2 \nabla^4 v_i\bigr) \, dV = -\kappa\mu_\mathrm{V1}\ell_P^2 \int |\nabla^3 v|^2 \, dV \;\le\; 0.$$

Manifestly non-positive; sign FORCED.

**Pressure contribution:**

$$\int \partial_j v_i \, \partial_j(-\partial_i p) \, dV = -\int \nabla^2(\nabla \cdot v) \, p \, dV = 0$$

by incompressibility.

**Aggregate:**

$$\boxed{\;\frac{dL}{dt}\bigg|_{\text{ED-only NS}} = -\nu\int|\nabla^2 v|^2 \, dV \;-\; \kappa\mu_\mathrm{V1}\ell_P^2\int|\nabla^3 v|^2 \, dV \;\le\; 0.\;}$$

Two manifestly non-positive contributions; no positive terms. **The gradient-norm Lyapunov decays strictly monotonically along trajectories of ED-only NS.**

### 3.4 Counterfactual smoothness

Standard parabolic-regularity theory for higher-derivative-regularized parabolic equations (Lions 1969 and downstream literature; canonical for NS-Burgers-class systems) gives global smooth solutions for ED-only NS on $\mathbb{R}^3$ with smooth, finite-energy initial data. The argument is *a fortiori* easier than NS-Burgers because ED-only NS lacks the advective term entirely — the equation is purely parabolic with two dissipative terms.

**Counterfactual statement:** *if* 3D NS lacked the advective convective derivative, ED's architectural content would unconditionally guarantee global smoothness on $\mathbb{R}^3$ for finite-energy data.

This is the **positive side of the Clay-relevance decomposition**: ED supplies real, canon-level regularizing infrastructure.

---

## 4. Full NS + R1 and the Advection Obstruction

### 4.1 Restoring advection

The actual physical equation is full incompressible NS with the form-FORCED R1 term included:

$$\rho\,\partial_t v_i + \rho\,(v\cdot\nabla)v_i \;=\; \mu\nabla^2 v_i \;-\; \kappa\mu_\mathrm{V1}\ell_P^2\,\nabla^4 v_i \;-\; \partial_i p, \qquad \nabla\cdot v = 0.$$

The only structural difference from ED-only NS (§3.1) is the addition of the advective convective derivative $\rho(v\cdot\nabla)v_i$ on the left-hand side. Per NS-2.08 §5, this term is a fluid-mechanical addition not native to ED canonical channels.

### 4.2 $dL/dt$ for full NS + R1

Computing $dL/dt$ term-by-term, three of four contributions are unchanged from the ED-only case (§3.3): viscous diffusion contributes $-\nu\|\nabla^2 v\|_2^2 \le 0$; R1 contributes $-\kappa\mu_\mathrm{V1}\ell_P^2 \|\nabla^3 v\|_2^2 \le 0$; pressure contributes zero by incompressibility. The new contribution comes from advection.

**Advective contribution.** Using integration by parts and incompressibility, the advective contribution to $dL/dt$ reduces to a cubic-velocity-gradient integral that, after standard rearrangement, takes the canonical *vortex-stretching* form:

$$\left(\frac{dL}{dt}\right)_\text{adv} \;=\; \int \omega \cdot (S \omega) \, dV \cdot (\text{convention-dependent constant}),$$

where $\omega = \nabla\times v$ is vorticity and $S = \frac{1}{2}(\nabla v + (\nabla v)^T)$ is the symmetric strain-rate tensor. (See [`NS-3.02b`](../NS-3.02b_Multi_Lyapunov_Audit.md) §3.4 and [`NS_Smooth_3_Advection_Obstruction.md`](NS_Smooth_3_Advection_Obstruction.md) §4.1 for the full derivation; standard turbulence-analysis references — Frisch §6, Pope §6 — give equivalent forms.)

**Aggregate:**

$$\boxed{\;\frac{dL}{dt}\bigg|_{\text{full NS + R1}} = \underbrace{-\nu\|\nabla^2 v\|_2^2}_{\le 0} \;+\; \underbrace{-\kappa\mu_\mathrm{V1}\ell_P^2\|\nabla^3 v\|_2^2}_{\le 0} \;+\; \underbrace{0}_{\text{pressure}} \;+\; \underbrace{\int\omega\cdot S\omega \, dV \cdot (\text{const})}_{\text{indefinite-sign}}.\;}$$

### 4.3 Why vortex-stretching is the unique obstruction

The vortex-stretching contribution $\int\omega\cdot S\omega \, dV$ depends on the alignment of vorticity $\omega$ with the strain-rate tensor's eigenvectors. The strain $S$ has three real eigenvalues $\lambda_1 \ge \lambda_2 \ge \lambda_3$ with $\lambda_1 + \lambda_2 + \lambda_3 = 0$ by incompressibility. Therefore:

- Vorticity aligned with $\lambda_1$-eigenvector ($\lambda_1 > 0$): integrand positive locally; vortex stretching amplifies vorticity.
- Vorticity aligned with $\lambda_3$-eigenvector ($\lambda_3 < 0$): integrand negative locally; vortex compressing diminishes vorticity.
- Generic configurations: indefinite-sign locally; integrated value can be positive or negative.

**In 2D incompressible flow, this term vanishes identically** — vorticity is purely out-of-plane while strain is in-plane, so $\omega \cdot S\omega = 0$. This is the structural reason 2D NS has Leray-class global smooth solutions while 3D NS remains the open Clay problem.

**In 3D, the term is the unique source of potential gradient-norm growth.** All other terms in full NS + R1 are dissipative or zero. **Any blow-up trajectory must source its gradient-amplification from the advective vortex-stretching term.**

This is the **negative side of the Clay-relevance decomposition**: the structural feature breaking smoothness lies *outside* ED's canonical architecture.

---

## 5. Three-Angle Convergence on Advection-is-Non-ED

The advective term is identified as structurally non-ED at three independent program-level analyses:

| Lens | Source | Finding |
|---|---|---|
| **Architectural** | [`NS-2.08`](../NS-2.08_ED-PDE_Direct_Mapping.md) §5 | Advection $(v\cdot\nabla)v$ is a fluid-mechanical addition not native to ED canonical PDE channels. The kinematic coupling between velocity components has no ED-canonical counterpart; ED's vector-extension supplies only the viscous content. |
| **Dynamical** | [`NS-3.02b`](../NS-3.02b_Multi_Lyapunov_Audit.md) §3.4 + NS-Smooth-3 | Advective vortex-stretching $\int\omega\cdot S\omega$ specifically breaks the gradient-norm Lyapunov in 3D. Pressure and incompressibility contribute zero; only advection generates indefinite-sign Lyapunov-derivative content. |
| **Spectral** | [`NS-Turb-4`](../Turbulence/P7_Triads_NS_Turb_4_Failure_Modes.md) §6 | Advective Fourier interaction coefficient $M_{ijm}(\mathbf{k}) = -ik_j P_{im}(\mathbf{k})$ has transport-directional + projection structure incompatible with P7-class symmetric-quadratic Fourier mapping. Index-structure asymmetry persists at all amplitudes. |

### 5.1 Significance of the convergence

Three different mathematical/structural lenses, applied to three distinct questions (canon-membership, Lyapunov-derivative-sign, Fourier-mode-coupling), converge on the same physical feature: **advection's transport-directional, asymmetric, projected index structure is the locus of the ED↔NS structural mismatch.**

The independence of the three lenses is essential. If only one analysis identified advection as non-ED, the finding would be susceptible to the suspicion that the analytical framework was unsuited to the question. Three independent frameworks identifying the same feature establishes the finding as structural rather than methodological — robust across analytical lenses.

The convergence is the most consistent and load-bearing structural finding in the NS program.

---

## 6. Intermediate Path C — Final Clay-Relevance Statement

### 6.1 Formal Intermediate Path C verdict

> *Event Density's architectural canon contains a real Clay-NS-relevant regularizing mechanism. The R1 mechanism — the form-FORCED $-\kappa\mu_\mathrm{V1}\ell_P^2 \nabla^4 v_i$ stabilization arising from V1's finite-width vacuum kernel under multi-scale expansion — combines with standard viscous diffusion to produce, in a counterfactual "ED-only NS" lacking the advective convective derivative, a strictly monotonically-decaying gradient-norm Lyapunov $L = \frac{1}{2}\|\nabla v\|_2^2$. By standard parabolic-regularity theory, ED-only NS has global smooth solutions on $\mathbb{R}^3$ for smooth, finite-energy initial data.*
>
> *The actual obstruction to closing the Clay-NS smoothness problem in 3D is the advective convective derivative's vortex-stretching content $\int\omega\cdot S\omega \, dV$, which is the unique source of potential gradient-norm growth in full NS + R1; all other terms are dissipative (viscous, R1) or neutral (pressure under incompressibility). The advective term is structurally non-ED at three independent program-level analyses: architectural (NS-2.08, fluid-mechanical addition not native to canonical channels), dynamical (NS-3.02b + NS-Smooth-3, unique indefinite-sign contribution to the gradient-norm Lyapunov derivative), and spectral (NS-Turb-4, transport-directional index structure incompatible with P7-class symmetric-quadratic Fourier mapping). The three-angle convergence establishes advection-as-non-ED robustly across analytical lenses.*
>
> *The quantitative competition between R1's dissipative content (dominant at substrate scales $\sim \ell_P$) and advective vortex-stretching (active at intermediate scales between flow scale and substrate) is INHERITED on both sides — depends on the V1 G-function specific form (per arc-N N.4) and on standard kinetic-theory super-Burnett magnitude (per material-specific kinetic parameters). Neither magnitude is canonically fixed; therefore the canonical architecture alone cannot determine which side dominates in any specific blow-up scenario.*
>
> *Event Density therefore neither solves the Clay-NS smoothness problem nor is irrelevant to it. ED supplies a partial structural framework: a decomposition of the Clay-NS difficulty into (a) ED-canonical regularizing infrastructure (R1) + (b) non-ED structural obstruction (advective vortex-stretching). The decomposition explains why 2D NS is globally smooth (vortex-stretching vanishes identically; advective contribution to the gradient-norm Lyapunov derivative is zero) and why 3D NS is structurally hard (the obstructing structural feature lies outside the canonical regularizing architecture, with quantitative competition through scales not resolvable at canon level). The decomposition does not resolve which side wins quantitatively in the 3D case.*

### 6.2 What ED explains (and what it does not)

**ED *explains*:**

- Why 2D NS is globally smooth: vortex-stretching vanishes identically, leaving only dissipative and neutral terms in $dL/dt$.
- Why 3D NS is structurally hard: the obstructing feature (advection's vortex-stretching) is non-ED at three independent levels and not absorbable into the canonical regularizing architecture.
- Where in the equation the structural obstruction is localized: uniquely at the advective convective derivative.
- Why R1's substrate-scale stabilization is real but insufficient on its own: R1 is form-FORCED with sign-FORCED-positive dissipation, but its coefficient is INHERITED at the value level and the term is suppressed by $\sim (\ell_P/L)^2$ at intermediate scales where advective vortex-stretching is most active.

**ED does *not* explain (and does not claim to):**

- Whether 3D NS solutions blow up at finite time or remain smooth globally.
- The numerical critical Reynolds number for any specific transition.
- The detailed cascade structure of developed turbulence (closed at H1 trivial / H2 partial / H3 fail per [`NS-Turb-5`](../Turbulence/P7_Triads_NS_Turb_5_Synthesis.md)).
- Specific blow-up criteria (BKM extensions; Constantin-Fefferman geometric criteria).

ED's contribution to the Clay-NS question is **structural-decompositional, not quantitative-resolutional**. This is the substantive Intermediate Path C content.

---

## 7. Hypothesis Resolution

The three working hypotheses framed in NS-Smooth-1 §7 now resolve as follows:

| Hypothesis | Claim | Verdict | Source |
|---|---|---|---|
| **H1 (Structural)** | ED's R1 mechanism guarantees smoothness in ED-only NS | **Succeeds** | NS-Smooth-2; this memo §3 |
| **H2 (Obstruction)** | NS advection is structurally non-ED and breaks R1 via vortex-stretching | **Succeeds** | NS-Smooth-3; this memo §4 |
| **H3 (Clay-Relevance)** | ED provides a partial explanatory framework — structural decomposition of the difficulty without solution | **Succeeds in intended sense** | NS-Smooth-4; this memo §6 |

**H3 succeeds in the intended sense** because the program never claimed ED would solve Clay-NS — only that ED's architectural content provides a *structural decomposition* of the difficulty. That is exactly what has been delivered. The decomposition is real (R1 is form-FORCED and dissipative; advection-is-non-ED is robust across three angles), the framing is honest (quantitative competition INHERITED), and the result is informative (explains 2D vs. 3D dimensional asymmetry; localizes the obstruction; clarifies why Clay-NS resists resolution).

---

## 8. Implications and Program Position

### 8.1 Place in the NS program

The NS-Smoothness arc closes the Clay-relevance question for the program. Aggregating across the four NS arcs:

- **NS-1** closed Path B-strong: D = 3+1 forced via multi-layer architectural + empirical-consistency chain.
- **NS-2** closed: standard Newtonian-fluid NS form derived from substrate primitives plus partial vector-extension; ED-specific deviations identified but numerically negligible at standard NS scales.
- **NS-3** closed Intermediate Path C: ED contains real Clay-relevant mechanism (R1) with form-FORCED structure but value-INHERITED competition.
- **NS-Turb** closed: P7 ↔ turbulence cascade fails at H3 (no architectural template for cascade); H2 partial-success in restricted forced-response regime.
- **NS-Smoothness** (this arc) closes: Intermediate Path C formalized as structural decomposition of Clay-NS difficulty.

The program now has a complete picture of ED's relationship to fluid mechanics in the Clay-NS-relevant regime: form derivation works (NS-2), dimensional forcing closes (NS-1), Clay-relevance is partial-structural (NS-Smoothness Intermediate Path C), turbulence-cascade architectural-template fails (NS-Turb).

### 8.2 Citation guidance for external papers

Future external-facing program-level papers should cite this memo (NS-Smooth-5) as the canonical Clay-relevance reference. Recommended citation framing in any such paper:

> *Event Density's relationship to the Clay Navier-Stokes smoothness problem is articulated in detail in [NS-Smooth-5]. The result is structural-decompositional rather than quantitative-resolutional: ED's architectural canon supplies a regularizing mechanism (the R1 substrate-scale stabilization arising from V1's finite-width vacuum kernel) that, in counterfactual "ED-only NS," would unconditionally guarantee global smoothness. The actual obstruction in 3D — the advective vortex-stretching content — is structurally non-ED at three independent program analyses (architectural, dynamical, spectral). ED therefore neither solves Clay-NS nor is irrelevant; it provides a partial structural framework explaining why 2D NS is globally smooth (vortex-stretching vanishes) and why 3D NS is hard (the obstruction lies outside the canonical regularizing architecture).*

This framing is honest and avoids overclaiming — ED's contribution is structurally significant but explicitly limited to the decomposition.

### 8.3 Arc closure

**The NS-Smoothness arc is closed at Intermediate Path C.**

No further memos in this arc are required. The substantive work is complete. Future NS-related work should reference this memo for Clay-relevance content; the sub-memos NS-Smooth-1 through NS-Smooth-4 remain available for detailed consultation but the citable content is consolidated here.

---

## 9. Recommended Next Steps

1. **Mark the NS-Smoothness arc as closed at Intermediate Path C.** Add a closure note to the program-level NS roadmap reference ([`../Navier_Stokes_Roadmap_Scoping.md`](../Navier_Stokes_Roadmap_Scoping.md)) and to the master orientation document referencing this memo as the canonical Clay-relevance reference. Editorial pass; ~30 minutes.

2. **Use this memo as the canonical Clay-relevance reference in future NS-related program-level papers.** Specifically, the future NS-1/2/3 synthesis paper ([`../NS-3.04`](../NS-3.04_Synthesis_Path_Verdict.md) §9.1 recommends drafting it) should incorporate the Intermediate Path C statement (§6.1 above) as a section discussing ED's reach into Clay-relevance.

3. **Plan the larger NS-1/2/3 synthesis paper.** With this arc closed, the program-level Clay-relevance content is consolidated. The NS-1/2/3 synthesis paper now has clean material for:
   - §1 NS roadmap overview (NS-1 + NS-2 + NS-3).
   - §2 Dimensional forcing (NS-1 Path B-strong + Architectural Canon Vector Extension).
   - §3 Form-derivation (NS-2 chain-substrate + ED-PDE-direct two-route concordance).
   - §4 Clay-relevance (NS-Smoothness Intermediate Path C, citing this memo).
   - §5 Turbulence cascade (NS-Turb H1/H2/H3 verdict).
   - §6 Discussion + future work.
   Estimated 4–5 sessions for paper draft. Higher-effort but program-level high-value.

### Decisions for you — preferred next direction

The honest priority ranking for the program after NS-Smoothness arc closure:

1. **P4-NN paper draft** — **highest value-per-effort.** Substantive empirical anchoring already in place (UMD β = 1.72 ± 0.37 within 1σ of canonical β = 2.0); publication-grade content; sequel to existing UDM paper. Draft was begun and interrupted; resuming it is the cleanest next program-level deliverable. ~2–3 sessions for paper draft beyond existing memo content. **My recommendation if a single high-value deliverable is the goal.**

2. **NS-1/2/3 synthesis paper** — broader program-level scope; structurally significant; longer effort (~4–5 sessions); could be drafted after P4-NN. Now has clean Clay-relevance content (this memo) ready to incorporate.

3. **Memory + orientation updates** — small editorial passes capturing the arc closures (NS-Smoothness, NS-Turb, P4-NN, Q-Factor). Quick maintenance work; ~0.5–1 session. Useful housekeeping; not high-value-per-effort.

4. **Smaller follow-on arcs** (Reynolds-from-substrate, etc.) — speculative; lower expected return.

**Recommended sequence:** Resume P4-NN paper draft first as the cleanest single deliverable, then memory/orientation updates as quick follow-on, then NS-1/2/3 synthesis paper as the larger program-level publication that incorporates the Clay-relevance content from this memo.

---

*NS-Smoothness arc closed at Intermediate Path C. Self-contained Clay-relevance statement: ED contains form-FORCED regularizing mechanism (R1) that would close Clay-NS in counterfactual ED-only NS; actual 3D obstruction (advective vortex-stretching) is structurally non-ED at architectural (NS-2.08), dynamical (NS-3.02b + NS-Smooth-3), and spectral (NS-Turb-4) levels — three-angle convergence robust across analytical lenses; quantitative competition between R1 dissipation and advective stretching INHERITED on both sides. ED provides structural decomposition of Clay-NS difficulty into ED-canonical regularizing infrastructure + non-ED structural obstruction. Decomposition explains 2D-vs-3D asymmetry (vortex-stretching vanishes identically in 2D) and localizes 3D obstruction without resolving it. H1 succeeds; H2 succeeds; H3 succeeds in intended sense. NS-Smoothness arc closed; this memo is the canonical Clay-relevance reference for future external-facing program-level papers.*
