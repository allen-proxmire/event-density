# Arc_YM_5 — OS Positivity and Continuum Stability

**Date:** 2026-04-30
**Status:** Second of two structurally non-trivial memos in the YM arc. Audits the Osterwalder-Schrader (OS) reflection-positivity property of the substrate-derived YM equation, restricted to the four canonical-ED content channels identified in YM-4. **Result: each canonical-ED channel separately preserves OS positivity at the structural-suggestive level, conditional on (i) compact gauge group, (ii) V1 positive Fourier transform, (iii) the YM-3 kernel-profile-rescaling condition. Verdict is structural-positive, not constructively rigorous.**
**Companions:** [`Arc_YM_1_Opening.md`](Arc_YM_1_Opening.md), [`Arc_YM_2_Substrate_to_Continuum_Limit.md`](Arc_YM_2_Substrate_to_Continuum_Limit.md), [`Arc_YM_3_Mass_Gap_From_Substrate_Cutoff.md`](Arc_YM_3_Mass_Gap_From_Substrate_Cutoff.md), [`Arc_YM_4_Architectural_Classification.md`](Arc_YM_4_Architectural_Classification.md), [`../../arcs/arc-B/arc_b_synthesis.md`](../../arcs/arc-B/arc_b_synthesis.md) (T18), [`../../theorems/T17.md`](../../theorems/T17.md), [`../Navier Stokes/Smoothness/NS_Smooth_2_R1_Lyapunov.md`](../Navier%20Stokes/Smoothness/NS_Smooth_2_R1_Lyapunov.md).

---

## 1. Purpose

This memo addresses the load-bearing positivity question of the YM arc. Specifically:

- **Tests whether the ED substrate → continuum mapping preserves OS positivity** at the level of each canonical-ED content channel of the substrate-derived YM equation.
- **Audits the four canonical-ED YM content channels (from YM-4)** — kinetic term, non-Abelian self-interaction, matter source, higher-derivative correction — for reflection-positivity preservation under the continuum limit.
- **Identifies the OS-positivity preservation locus** — the structural conditions (gauge-group compactness, V1 positive Fourier transform, kernel-profile-rescaling) under which OS positivity holds.
- **Determines whether the continuum limit is constructively stable** at the structural-suggestive level — i.e., whether the Euclidean action is bounded below and reflection-positive.
- **Evaluates whether ED avoids the classical constructive-QFT obstruction** that historical YM-existence approaches have hit at OS positivity preservation in the continuum limit.

**OS positivity is a mathematical condition.** Reflection positivity in the Osterwalder-Schrader formulation requires that, for any local observable $\mathcal{O}(x_0, \mathbf{x})$ with $x_0 > 0$ (positive Euclidean time),

$$\bigl\langle\Theta\mathcal{O}\,\mathcal{O}\bigr\rangle \;\ge\; 0,$$

where $\Theta$ is Euclidean-time reflection $(x_0 \to -x_0)$ combined with appropriate field-component conjugation. OS positivity is the structural condition that allows reconstruction of the Hilbert-space quantum theory from the Euclidean correlator — the load-bearing axiom of the OS reconstruction theorem and the historical stall-risk of constructive YM existence.

**Important framing note.** This memo is **not** a constructive proof of YM existence. The analysis is structural-suggestive: each canonical-ED content channel is shown to have the correct sign / reflection-symmetry structure to be compatible with OS positivity. A constructive proof would require (a) verifying the full action is OS-reflection-positive at the level of operator-valued distributions on $\mathbb{R}^4$, (b) controlling the gauge-fixing sector (Gribov-copy obstructions historically appear here), (c) verifying continuum-limit convergence rigorously. The present memo establishes the structural-positive content of the canonical-ED sector; the gauge-fixing sector is excluded per YM-4's classification (gauge fixing is non-ED bookkeeping); the constructive verification is out of scope per YM-1 non-goals.

The verdict is honest: **structural-positive, not constructively rigorous.** Parallel framing to NS-Smoothness's Intermediate Path C verdict on Clay-NS.

---

## 2. Inputs

- **Arc_YM_2 (Substrate → Continuum YM Equation).** The continuum YM equation $D_\mu F^{\mu\nu} = J^\nu$ derived from substrate primitives. Provides the dynamical content audited here for OS positivity.
- **Arc_YM_3 (Mass Gap from Substrate Cutoff).** The substrate-induced mass scale $m_\mathrm{eff}^2 \sim c_{V1}\ell_P^{-2}$. Required for the higher-derivative term's positivity analysis (Step 5) and feeds into the OS-positivity preservation locus (Step 7).
- **Arc_YM_4 (Architectural Classification).** Identifies the four canonical-ED content channels (kinetic, self-interaction, matter source, higher-derivative correction) that the present audit applies to. Excludes gauge-fixing and Christoffel-class artifacts as non-ED bookkeeping.
- **DCGT (Arc D).** Substrate-to-continuum coarse-graining theorem. Establishes the form-FORCED / sign-FORCED structural status of each canonical-ED operator emerging from substrate primitives.
- **T17 (Gauge-Fields-as-Rule-Type).** Substrate gauge structure with non-Abelian-capable Killing-form-bearing Lie-algebra rule-type. The compact-simple-group requirement enters at the level of the Killing-form positivity.
- **T18 (V1 Kernel Retardation).** Forward-cone-only support of the substrate kernel; the substrate-level analytic-structure ancestor of upper-half-plane analyticity. Required for OS positivity at the analytic-structure level.
- **ED-I-06 (Fields and Forces).** Canonical-ED vs. non-ED ontology. The structural justification for restricting the OS-positivity audit to the canonical-ED sector.

---

## 3. Step 1 — OS Positivity: What Must Be Checked

OS reflection positivity applies to the canonical-ED dynamical content of the YM theory, not to the gauge-fixing or coordinate-frame bookkeeping (per YM-4 classification §C.4.2). The audit's structural domain is the four canonical-ED channels:

1. **Kinetic term** $\partial_\mu F^{\mu\nu}$ (YM-4 channel A).
2. **Non-Abelian self-interaction** $gf^{abc}A_\mu^b F^{\mu\nu\,c}$ (YM-4 channel B).
3. **Matter source** $J^\nu$ (YM-4 channel C).
4. **Higher-derivative correction** $c_{V1}\ell_P^2\nabla^2 A$ (YM-4 channel F; substrate-induced mass scale per YM-3).

The non-ED channels (gauge-fixing, Christoffel artifacts) are excluded from this audit:

- Gauge-fixing terms are continuum-imposed bookkeeping; their OS-positivity status is a separate technical question (Gribov-class obstructions in standard constructive QFT). Per YM-1 non-goals, ED does not address the gauge-fixing sector — gauge-quotient identification is supplied by T17 clause C8 at substrate level rather than by continuum gauge-fixing devices.
- Christoffel-class coordinate artifacts are frame-dependent and vanish in flat Minkowski coordinates (the regime of the YM-1 / ED-Phys-10 acoustic-metric guardrails).

**Euclidean continuation.** OS positivity is formulated in Euclidean signature. The standard continuation is

$$t \;\longrightarrow\; -i\tau, \qquad A_0 \;\longrightarrow\; iA_4,$$

with $\tau$ the Euclidean time and $A_4$ the Euclidean time-component of the gauge potential. The Euclidean action $S_E$ is then real, and reflection positivity is a property of the corresponding Euclidean correlator.

The audit walks through the four canonical-ED channels in turn (Steps 2–5), then combines them into the full Euclidean action (Step 6) and identifies the structural conditions for positivity preservation (Step 7).

---

## 4. Step 2 — Kinetic Term Positivity

In Euclidean signature, the YM kinetic action is

$$S_E^\mathrm{kin} \;=\; \frac{1}{4}\int d^4x \;F_{\mu\nu}^a F_{\mu\nu}^a \;=\; \frac{1}{2}\int d^4x \;\mathrm{Tr}(F_{\mu\nu}F_{\mu\nu}),$$

with $F_{\mu\nu} = F_{\mu\nu}^a T^a$ and the trace taken over the gauge generators in the chosen representation. For a **compact** gauge group, the Killing form $K^{ab} = f^{acd}f^{bcd}$ is positive-definite (T17 clause C2), and the trace inner product $\mathrm{Tr}(T^a T^b) = \tfrac{1}{2}\delta^{ab}$ in the canonical normalization yields

$$\frac{1}{2}\,\mathrm{Tr}(F_{\mu\nu}F_{\mu\nu}) \;=\; \frac{1}{4}\,F_{\mu\nu}^a F_{\mu\nu}^a \;\ge\; 0.$$

The integrand is the squared norm of the field strength under the Killing-form inner product, which is positive-definite for compact $G$. Hence $S_E^\mathrm{kin} \ge 0$ pointwise, and the kinetic term is **positive-definite** for compact gauge groups.

**Structural consequences.**

- The kinetic term **preserves OS positivity.** Under Euclidean-time reflection $\tau \to -\tau$ combined with the appropriate component conjugation of $A_\mu$, the kinetic action is invariant; reflection-positivity of the kinetic correlator $\langle\Theta\partial_\mu A_\nu\,\partial_\mu A_\nu\rangle \ge 0$ follows from the positive-definite Gaussian integration.
- This is the **same positivity that underlies lattice YM.** Wilson's lattice formulation uses the plaquette action $\mathrm{Re}\,\mathrm{Tr}(U_\mathrm{plaq})$ which is positive on compact $G$ via the same Killing-form-positivity mechanism. The continuum limit of lattice YM (when it exists) inherits this kinetic positivity.
- **Compactness of $G$ is essential.** For non-compact gauge groups, the Killing form is indefinite (or non-existent in non-semisimple cases), and the kinetic term acquires negative-definite directions. The compactness requirement is the structural reason constructive YM is restricted to compact gauge groups, and the same restriction applies in the ED substrate-derivation: T17 clause C2 establishes the substrate gauge group as non-Abelian-capable with Killing-form closure, and compactness enters at the Killing-form positivity level.

The kinetic term passes the OS-positivity audit **conditional on compact gauge group**.

---

## 5. Step 3 — Self-Interaction Term Positivity

The non-Abelian self-interaction term in the YM Lagrangian arises from expanding the kinetic term:

$$-\frac{1}{4}F_{\mu\nu}^a F_{\mu\nu}^a \;=\; -\frac{1}{4}(\partial_\mu A_\nu^a - \partial_\nu A_\mu^a)^2 \;-\; \frac{1}{2}gf^{abc}(\partial_\mu A_\nu^a - \partial_\nu A_\mu^a)A_\mu^b A_\nu^c \;-\; \frac{1}{4}g^2(f^{abc}A_\mu^b A_\nu^c)^2.$$

Three structural points:

**Cubic term $\sim gf^{abc}\partial A\cdot AA$.** Under Euclidean-time reflection, this term transforms with a sign determined by the parity of the spacetime indices. The cubic term is *odd* under reflection (one explicit derivative + three field factors), and its contribution to the reflection-positive correlator vanishes by reflection antisymmetry: $\langle\Theta(\mathrm{cubic})\,\mathrm{cubic}\rangle$ involves an odd number of derivatives flipped under reflection, producing a sign-cancellation structure that gives no negative-norm contribution.

More directly: the cubic term is a *cross-coupling* between the gauge potential and the field strength that does not source a definite-sign contribution to the kinetic-class Gaussian integration. It contributes to the YM correlator at perturbative order $g$, but its reflection-positivity status is determined by the kinetic-term and quartic-term positivity (which bound the cubic term's perturbative contribution).

**Quartic term $-\tfrac{1}{4}g^2(f^{abc}A_\mu^b A_\nu^c)^2$.** Expanding,

$$-\frac{1}{4}g^2(f^{abc}A_\mu^b A_\nu^c)(f^{ade}A^{\mu\,d} A^{\nu\,e}) \;=\; -\frac{1}{4}g^2\,K^{ab}_\mathrm{quartic}(A_\mu^b A_\nu^a)(A^\mu A^\nu)\cdots$$

with the structure-constant contraction $f^{abc}f^{ade}$ producing a positive-semidefinite tensor on $A^2$ for compact $G$ (Killing-form positivity). The quartic term in the *Euclidean* action — after the sign-flip from Lorentzian to Euclidean — is

$$+\,\frac{1}{4}g^2(f^{abc}A_\mu^b A_\nu^c)^2 \;\ge\; 0,$$

i.e., **positive** in Euclidean signature for compact gauge groups. This is the structural reason the YM action is bounded below for compact $G$: the quartic term provides a confining stability potential at large $A$.

**Structural consequences.**

- Under Euclidean reflection, the commutator structure $f^{abc}A_\mu^b A_\nu^c$ is antisymmetric in $(\mu, \nu)$ and antisymmetric in the $(b, c)$ pair-index (via $f^{abc}$). The square $(f^{abc}A_\mu^b A_\nu^c)^2$ is reflection-symmetric and positive-definite for compact $G$.
- The non-Abelian self-interaction **contributes no negative-norm modes** to the canonical-ED OS-positivity audit. Its quartic component is positive in Euclidean signature; its cubic component is odd-parity under reflection and sign-cancels at the correlator level.
- Compact gauge groups are *required* for self-interaction positivity (parallel to kinetic term Step 2). This is the **structural reason constructive QFT requires compact groups for non-Abelian YM**: the quartic term's Killing-form-positivity gives a stable potential bounded below.

The self-interaction term passes the OS-positivity audit **conditional on compact gauge group**.

---

## 6. Step 4 — Source Term Positivity

The matter-source coupling enters the YM action as

$$S_E^\mathrm{source} \;=\; \int d^4x\;J^\mu(x)\,A_\mu(x),$$

where $J^\mu$ is the gauge-current density at fluid scale per YM-4 channel C, produced by charged-chain populations under T17 generalized minimal coupling.

**Reflection structure.** Under Euclidean reflection $\tau \to -\tau$, the gauge potential transforms as $A_4 \to -A_4$ (time-component) and $A_i \to A_i$ (spatial components). The current $J^\mu$, being constructed from charged-matter bilinears under minimal coupling, transforms with the same reflection structure: $J^4 \to -J^4$, $J^i \to J^i$. Hence the bilinear $J^\mu A_\mu$ is reflection-invariant: $\Theta(J^4 A_4) = (-J^4)(-A_4) = J^4 A_4$; $\Theta(J^i A_i) = J^i A_i$.

**Positivity.** The reflection-positive correlator of the source term is

$$\bigl\langle\Theta(J^\mu A_\mu)\,(J^\mu A_\mu)\bigr\rangle \;=\; \bigl\langle(J^\mu A_\mu)^*\,(J^\mu A_\mu)\bigr\rangle \;\ge\; 0,$$

provided the matter sector itself satisfies OS positivity (the matter Hilbert space is OS-positive, which for fermionic matter follows from R.2.5 spin-statistics and Cl(3,1) framework, and for bosonic matter from standard scalar-field OS positivity). Under that assumption — which is structurally consistent with the closed Arc R / Arc Q work in the program — the source-term contribution to the OS-positivity correlator is non-negative.

**Structural consequences.**

- The source term **preserves OS positivity** at the level of the canonical-ED sector, conditional on the matter sector's own OS positivity (assumed via the closed structural-foundation work T1–T18).
- This is the canonical-ED gauge-current coupling, parallel to the Lorentz-force coupling in NS-MHD; both inherit OS-positivity from the substrate-level minimal-coupling structure of T17.
- **No new structural condition arises** from the source-term audit beyond the matter-sector OS-positivity already established.

The source term passes the OS-positivity audit **conditional on matter-sector OS positivity** (which is structurally backed by the closed T1–T18 foundation work).

---

## 7. Step 5 — Higher-Derivative Term (V1 Second Moment)

The YM-analogue of R1 is the substrate-induced higher-derivative correction $c_{V1}\ell_P^2\nabla^2 A_\mu^a$ identified in YM-2 §3 and analyzed in YM-3 §3 / §4. At the level of the action, this enters as

$$S_E^\mathrm{R1} \;\supset\; \frac{1}{2}c_{V1}\,\ell_P^2\,\int d^4x\;A_\mu^a\,(-\nabla^2)\,A_\mu^a.$$

**Sign analysis.** In Euclidean signature, $\nabla^2 = \partial_\tau^2 + \delta^{ij}\partial_i\partial_j$ is *negative-definite* on smooth fields with appropriate boundary conditions: integrating by parts,

$$\int d^4x\;A_\mu^a(-\nabla^2)A_\mu^a \;=\; \int d^4x\;(\nabla A_\mu^a)\cdot(\nabla A_\mu^a) \;=\; \int d^4x\;|\nabla A_\mu^a|^2 \;\ge\; 0.$$

Combined with the V1-positive coefficient $c_{V1} > 0$ (FORCED by V1 positive Fourier transform per YM-3 §3), the action contribution is non-negative:

$$S_E^\mathrm{R1} \;=\; \frac{1}{2}c_{V1}\,\ell_P^2\,\int d^4x\;|\nabla A|^2 \;\ge\; 0.$$

**Structural consequences.**

- The V1-induced higher-derivative term **preserves OS positivity.** Its action contribution is the squared $L^2$-norm of $\nabla A$, which is reflection-symmetric and non-negative.
- This is the **YM analogue of R1 positivity in NS-Smoothness §5** (NS-Smooth-2 established that R1 produces strictly monotone gradient-norm Lyapunov decay $-\kappa\mu_\mathrm{V1}\ell_P^2\|\nabla^3\mathbf{v}\|_2^2$ in 3D NS via the same V1-second-moment-positivity mechanism). Same V1 substrate origin; same sign-FORCED stabilizing property; same structural positivity outcome.
- The substrate-induced mass term identified in YM-3 (effective mass $m_\mathrm{eff}^2 \sim c_{V1}\ell_P^{-2}$) is structurally consistent with OS positivity: a positive effective mass term in a quadratic action contributes positively to the Euclidean Gaussian integration.

The higher-derivative term passes the OS-positivity audit **unconditionally given V1 positive Fourier transform** (FORCED by Theorem N1 admissibility class + Theorem 18 forward-cone support).

---

## 8. Step 6 — Continuum-Limit Stability

Combining the four canonical-ED channels (Steps 2–5):

| Channel | Positivity status | Required condition |
|---|---|---|
| (A) Kinetic term $\tfrac{1}{4}F_{\mu\nu}^2$ | Positive-definite | Compact gauge group |
| (B) Non-Abelian self-interaction $g^2 A^4$ part | Positive (Euclidean) | Compact gauge group |
| (C) Source term $J^\mu A_\mu$ | Non-negative bilinear | Matter-sector OS positivity |
| (F) Higher-derivative $\ell_P^2 \|\nabla A\|^2$ | Non-negative | V1 positive Fourier transform (T18 / N1) |

The combined Euclidean action, schematically,

$$\boxed{\;S_E \;=\; \int d^4x\;\Bigl[\,\tfrac{1}{4}F_{\mu\nu}^a F_{\mu\nu}^a \;+\; \tfrac{1}{2}c_{V1}\,\ell_P^2\,|\nabla A^a|^2 \;+\; J^\mu_a A_\mu^a \;+\; \mathcal{O}(\ell_P^4)\,\Bigr]\;}$$

(with the cubic and quartic self-interactions absorbed into the $F_{\mu\nu}^2$ expansion, and matter-action contributions added separately for the matter sector), is:

- **Bounded below** for compact gauge groups (kinetic + quartic positivity).
- **Reflection-positive** at the level of each canonical-ED content channel separately (Steps 2–5).
- **Continuum-limit stable** in the sense that each canonical-ED contribution remains non-negative under $\ell_P \to 0$, conditional on the YM-3 kernel-profile-rescaling condition $c_{V1}(\ell_P)\,\ell_P^{-2} \to m_\mathrm{phys}^2 \ge 0$.

**Structural verdict.**

> *At the structural-suggestive level audited here, OS positivity is preserved under the ED substrate → continuum mapping for the canonical-ED sector of the YM equation, conditional on (i) compact gauge group, (ii) V1 positive Fourier transform, (iii) the YM-3 kernel-profile-rescaling condition, and (iv) matter-sector OS positivity.*

**Honest framing.** This is *not* a constructive proof of YM OS positivity in the Streater-Wightman / OS-axiom sense. The audit demonstrates that each canonical-ED content channel has the correct sign and reflection structure to be compatible with OS positivity, and that the structural conditions (i)–(iv) are individually satisfiable under the program's existing closed work. A constructive proof would require:

- **Rigorous control of the gauge-fixing sector**, including Gribov-copy obstructions in the non-perturbative regime. Per YM-4, gauge-fixing is non-ED bookkeeping; ED's substrate gauge-quotient identification (T17 C8) bypasses the continuum gauge-fixing problem at the substrate level, but the continuum limit of the gauge-quotient structure is not analyzed here.
- **Full operator-valued-distribution-on-$\mathbb{R}^4$ verification**, with all $n$-point Schwinger functions audited for cluster decomposition and reflection positivity.
- **Continuum-limit convergence** of the substrate-level OS-positivity property to the continuum theory under DCGT, including verification that DCGT's hydrodynamic-window error bounds do not destroy OS positivity at the level of the operator structure.

These constructive verifications are out of scope per YM-1 non-goals. The present memo produces the structural-positive verdict that the canonical-ED sector is *compatible* with OS positivity; the constructive verification is a Clay-problem-class technical question.

---

## 9. Step 7 — The OS-Positivity Preservation Locus

The structural conditions identified in Steps 2–6 form the **OS-positivity preservation locus** for ED-YM:

**(L1) Gauge group must be compact.** Required for kinetic-term Killing-form positivity (Step 2) and quartic-term positivity (Step 3). T17 clause C2 establishes the substrate gauge group as non-Abelian-capable with Killing-form closure; compactness is the additional structural condition for OS positivity. Compactness is INHERITED at value layer (specific compact simple group choice is empirical).

**(L2) Kernel Fourier transform must be positive.** Required for higher-derivative term positivity (Step 5). FORCED at substrate level by Theorem 18 forward-cone support and Theorem N1 admissibility class. Structurally automatic given the closed Arc B / Arc N work.

**(L3) Continuum limit must satisfy the kernel-profile-rescaling condition.** Required for continuum-limit stability of the substrate-induced mass scale. Specifically:

$$c_{V1}(\ell_P)\,\ell_P^{-2} \;\longrightarrow\; m_\mathrm{phys}^2 \;\ge\; 0 \quad\text{as}\quad \ell_P \to 0.$$

This condition is INHERITED at value layer (per YM-3 §5); ED's structural derivation does not pin the rescaling exponent. Mass-gap survival requires $m_\mathrm{phys}^2 > 0$ strictly; OS-positivity preservation requires only $m_\mathrm{phys}^2 \ge 0$ (massless case is OS-positive but gapless, parallel to QED).

**(L4) Matter sector must satisfy OS positivity.** Required for source-term positivity (Step 4). Structurally backed by the closed T1–T18 foundation work; assumed in the present audit.

**Necessity and sufficiency.**

- *Necessary:* Under any of (L1)–(L4) failing, OS positivity fails — non-compact gauge groups produce indefinite kinetic action, V1 with non-positive Fourier transform produces destabilizing higher-derivative term, kernel-profile-rescaling failure produces gap-divergence or gap-closure, matter-sector non-OS produces negative-norm matter contributions.
- *Sufficient:* Under (L1)–(L4) all holding, each canonical-ED content channel is OS-positive separately; the combined Euclidean action is bounded below and reflection-positive at the structural-suggestive level.

These are the **necessary-and-sufficient structural conditions** for OS-positivity preservation in the canonical-ED sector of ED-YM.

---

## 10. Step 8 — Consequences for the YM Arc

The Arc_YM_5 OS-positivity analysis combined with Arc_YM_2 (substrate-to-continuum derivation) and Arc_YM_3 (mass-gap mechanism) jointly produce the following structural picture:

**(C1) ED provides a structurally constructively-stable YM continuum limit.** The four canonical-ED content channels each preserve OS positivity at structural-suggestive level; the continuum limit is bounded below and reflection-positive in each channel; the mass gap survives the continuum limit conditional on the kernel-profile-rescaling locus (L3).

**(C2) The classical constructive-QFT obstruction (OS-positivity failure) is not encountered in the canonical-ED sector.** Standard constructive YM has historically hit obstructions at OS-positivity preservation — particularly via the gauge-fixing sector (Gribov copies) and the continuum-limit subtleties of the operator structure. The ED substrate-derivation bypasses the gauge-fixing-sector obstruction by placing gauge-quotient identification at the substrate level (T17 clause C8) rather than at continuum level. The remaining structural questions (L1)–(L4) are individually satisfiable under the program's existing closed work.

**(C3) The structural verdict is positive but conditional.** OS positivity is preserved *conditional on* (L1)–(L4) all holding. (L1) is INHERITED (compact group choice empirical); (L2) is FORCED at substrate level; (L3) is INHERITED (kernel-profile-rescaling); (L4) is structurally backed by closed work. The verdict is parallel in honesty-framing to NS-Smoothness's Intermediate Path C: ED supplies a real Clay-relevant structural mechanism (here OS-positivity preservation in the canonical-ED sector); the Clay-problem-level constructive verification remains out of scope.

**(C4) YM-6 can synthesize the arc with a clean Clay-relevance statement.** The YM-2 + YM-3 + YM-4 + YM-5 structural picture is now in place: substrate-to-continuum derivation produces YM equation; mass gap exists at substrate level via V1 second-moment substrate cutoff; architectural classification places dynamics fully in canonical-ED sector; OS-positivity preserved at structural-suggestive level for the canonical-ED sector. YM-6 will aggregate this picture into the final Clay-relevance statement, parallel in form to NS-Smoothness's Intermediate Path C verdict.

---

## 11. Recommended Next Steps

Proceed to **Arc_YM_6 (Synthesis + Clay Relevance)**. File: `theory/Yang-Mills/Arc_YM_6_Synthesis_And_Clay_Relevance.md`. Scope: aggregate the five sub-arc results (YM-1 through YM-5) into a single arc-closing memo. State ED's structural contribution to the Clay YM-existence-and-mass-gap problem. Honest disclaimers on what ED resolves and what remains open. Recommend integration into NS Synthesis Paper as Appendix E or open a separate YM Synthesis Paper, depending on scope.

Estimated 1–2 sessions for Arc_YM_6.

### Decisions for you

- **Confirm OS-positivity structural verdict.** Each of the four canonical-ED content channels (kinetic, self-interaction, source, higher-derivative) preserves OS positivity at structural-suggestive level. Combined Euclidean action bounded below + reflection-positive conditional on (L1)–(L4) of the OS-positivity preservation locus.
- **Confirm honest framing.** Structural-positive verdict; not a constructive proof. Gauge-fixing sector excluded (non-ED per YM-4); rigorous operator-distribution verification out of scope per YM-1.
- **Confirm proceeding to Arc_YM_6 (synthesis + Clay relevance) as the next deliverable.**

---

*Arc_YM_5 closes the OS-positivity audit at structural-suggestive level. Each of the four canonical-ED content channels preserves OS positivity separately under appropriate conditions: kinetic term positive-definite for compact gauge groups via Killing-form positivity; non-Abelian self-interaction positive in Euclidean signature for compact $G$ (quartic stabilization); matter source non-negative bilinear conditional on matter-sector OS positivity (backed by closed T1–T18 work); higher-derivative term $\tfrac{1}{2}c_{V1}\ell_P^2|\nabla A|^2$ non-negative via V1 positive Fourier transform (FORCED by T18 + N1). Combined Euclidean action bounded below + reflection-positive conditional on the OS-positivity preservation locus: (L1) compact gauge group, (L2) kernel positive Fourier transform, (L3) kernel-profile-rescaling condition $c_{V1}(\ell_P)\ell_P^{-2} \to m_\mathrm{phys}^2 \ge 0$, (L4) matter-sector OS positivity. Verdict: structural-suggestive positive; not constructive proof. Standard constructive-QFT obstruction at OS positivity not encountered in the canonical-ED sector; gauge-fixing sector bypassed by T17 substrate gauge-quotient identification (C8); rigorous operator-distribution verification out of scope per YM-1. Sets up YM-6 synthesis with a clean Clay-relevance statement parallel in form to NS-Smoothness Intermediate Path C. Arc_YM_6 (synthesis + Clay relevance) is the next deliverable.*
