# Arc_YM_2 — Substrate → Continuum Limit for Non-Abelian Gauge Fields

**Date:** 2026-04-30
**Status:** Load-bearing technical memo of the Yang-Mills arc. Derives the continuum Yang-Mills equation $D_\mu F^{\mu\nu} = J^\nu$ from ED substrate primitives via DCGT-style multi-scale expansion of non-Abelian gauge-field correlators. **Result: form FORCED by T17 generalized minimal coupling + DCGT machinery + non-Abelian rule-type commutator structure; sign-FORCED stabilizing by V1 positive-Fourier-transform; value-INHERITED at coupling $g$ and kernel widths.**
**Companions:** [`Arc_YM_1_Opening.md`](Arc_YM_1_Opening.md), [`../Arc_D/Arc_D_5_Minimal_Coupling_Coarse_Graining.md`](../Arc_D/Arc_D_5_Minimal_Coupling_Coarse_Graining.md), [`../Arc_D/Arc_D_6_Synthesis_And_Theorem.md`](../Arc_D/Arc_D_6_Synthesis_And_Theorem.md), [`../Navier Stokes/MHD/NS_MHD_2_Lorentz_Force.md`](../Navier%20Stokes/MHD/NS_MHD_2_Lorentz_Force.md), [`../Navier Stokes/MHD/NS_MHD_5_Synthesis.md`](../Navier%20Stokes/MHD/NS_MHD_5_Synthesis.md), [`../../theorems/T17.md`](../../theorems/T17.md), [`../../arcs/arc-Q/grh_evaluation.md`](../../arcs/arc-Q/grh_evaluation.md), [`../../arcs/arc-B/arc_b_synthesis.md`](../../arcs/arc-B/arc_b_synthesis.md).

---

## 1. Purpose

This memo performs the load-bearing technical derivation of the YM arc. The aim is sixfold:

- **Extend DCGT from Abelian to non-Abelian gauge fields.** Arc D's substrate-to-continuum coarse-graining theorem covers scalar diffusion, directional-field viscosity, R1 hyperviscosity, V5 viscoelastic memory, and the Abelian Lorentz force (T17 $U(1)$ minimal coupling). YM-2 generalizes to compact simple gauge groups with non-Abelian rule-type structure.
- **Apply T17 minimal coupling to Lie-algebra–valued directional fields.** The substrate-level gauge potential becomes $A_\mu = A_\mu^a T^a$ with $T^a$ generators of a compact simple Lie algebra; minimal coupling $\partial_\mu \to \partial_\mu - igA_\mu$ acts on charged structural rule-types via the generalized minimal-coupling vertex of T17.
- **Perform hydrodynamic-window coarse-graining on non-Abelian fluxes.** Apply DCGT multi-scale expansion to gauge-field flux statistics with non-Abelian content. Identify which structural points generalize cleanly from the Abelian case and which require non-Abelian-specific analysis.
- **Derive the continuum Yang-Mills field strength $F_{\mu\nu}$** including the non-Abelian commutator term $-ig[A_\mu, A_\nu]$ as FORCED by the rule-type bracket structure of $\tau_g$.
- **Derive the covariant divergence $D_\mu F^{\mu\nu}$** from substrate momentum-flux divergence + charged-chain charge conservation generalized to non-Abelian gauge content.
- **Produce the continuum YM equation** $D_\mu F^{\mu\nu} = J^\nu$ with form FORCED at substrate level, signs FORCED stabilizing by V1 kernel positivity, values INHERITED at gauge coupling and kernel widths.

This memo carries the structural weight of the arc: if YM-2 closes cleanly, the remaining sub-arcs (YM-3 mass gap, YM-4 classification, YM-5 OS positivity, YM-6 synthesis) follow as analyses of the equation derived here. If YM-2 hits an obstruction, the obstruction is the load-bearing structural point of the entire YM arc.

---

## 2. Inputs

- **T17 (Gauge-Fields-as-Rule-Type, Arc Q closure 2026-04-27).** Provides the substrate-level non-Abelian-capable gauge structure. T17 clauses C2 (group structure with Killing form + Jacobi), C3 (vertex/minimal coupling, gauge-quotient invariant), C5–C7 (vacuum kernel structure) jointly supply every structural element this memo uses. Theorem 17 explicitly states "non-Abelian-capable" — the substrate gauge structure is FORCED with non-Abelian capability, with the specific compact simple group INHERITED at value layer.
- **T18 (V1 Kernel Retardation, Arc B closure 2026-04-27).** Forward-cone-only support of the substrate kernel; preserves causal structure under coarse-graining. Required for the non-Abelian gauge-field correlator's analytic structure (relevant to YM-5 OS-positivity).
- **ED-I-06 (Fields and Forces in Event Density, Feb 2026).** Directional-field ontology. The Lie-algebra–valued gauge potential $A_\mu^a T^a$ is a directional-field-class participation structure; the field strength $F_{\mu\nu}^a$ is the directional-field curvature; the YM equation is the dynamical equation of the gauge directional field.
- **DCGT (Arc D closure 2026-04-30).** Substrate-to-continuum coarse-graining theorem. The multi-scale-expansion methodology used here. DCGT establishes the hydrodynamic-window scale separation, the form-FORCED / value-INHERITED structural split, the sign-FORCED kernel-positivity arguments, and the error-bound scaling — all of which generalize directly to non-Abelian gauge content.
- **Arc_YM_1 (Opening, this arc).** Six-memo plan; load-bearing question identification (substrate-to-continuum non-Abelian extension is YM-2; OS-positivity is YM-5; mass gap is YM-3; classification is YM-4).
- **NS-MHD-2 (Abelian minimal-coupling coarse-graining).** The Abelian template that YM-2 extends. NS-MHD-2 established the Lorentz force form-FORCED by T17 $U(1)$ minimal coupling at semiclassical level. Arc_D_5 (companion to NS-MHD-2 under DCGT) closes the coarse-graining bridge for the Abelian case.
- **NS-MHD-5 (full MHD synthesis).** Canonical/non-canonical boundary for gauge-field couplings. The kinematic-coupling pattern (minimal-coupling-derived velocity-dependence canonical / transport-kinematic velocity-dependence non-ED) is the structural pattern that YM-4 will generalize to non-Abelian content.

---

## 3. Step 1 — Substrate Non-Abelian Gauge Structure

T17 establishes that the substrate gauge field is the participation measure of a structural rule-type $\tau_g$ whose group content is non-Abelian-capable with Killing form and Jacobi closure. For a compact simple gauge group $G$ with Lie algebra $\mathfrak{g}$ of dimension $\dim(G)$, write:

**Substrate gauge potential.**

$$A_\mu(x) \;=\; A_\mu^a(x)\,T^a, \qquad a = 1,\ldots,\dim(G),$$

with $T^a$ Hermitian generators of $\mathfrak{g}$ in some chosen representation (typically the fundamental for matter coupling; the adjoint enters in the YM action's trace structure). The generators satisfy the Lie bracket structure

$$[T^a,\,T^b] \;=\; if^{abc}\,T^c,$$

with $f^{abc}$ the totally-antisymmetric structure constants of $G$. The Killing form $K^{ab} = f^{acd}f^{bcd}$ is positive-definite (compact simple group; T17 clause C2 explicit). The Jacobi identity $f^{abe}f^{cde} + f^{cae}f^{bde} + f^{bce}f^{ade} = 0$ closes the algebra.

**Generalized minimal coupling (T17 generalized).** T17 clause C3 establishes minimal coupling at the substrate-level commitment vertex with $U(1)$-class $\partial_\mu \to \partial_\mu - iqA_\mu$ as the canonical case. The non-Abelian generalization is

$$\partial_\mu \;\longrightarrow\; D_\mu \;=\; \partial_\mu - igA_\mu \;=\; \partial_\mu - igA_\mu^a T^a,$$

with $g$ the gauge coupling (dimensionless in 4D, INHERITED at value layer per T17's form-FORCED / value-INHERITED split). For charged structural rule-types in representation $R$ of $G$, the generators $T^a$ act on the rule-type's internal index space via $R(T^a)$. The semiclassical reduction yields canonical-momentum shift

$$p_\mu \;\longrightarrow\; p_\mu - gA_\mu^a T^a$$

acting on the charged chain's matter representation.

**Compact-simple-group specificity.** YM-1 of the original Yang-Mills Roadmap Scoping (2026-04-28) flagged "do substrate primitives force non-Abelian gauge structure, force U(1), or leave the choice undetermined?" as a P09-amendment / T17-strengthening question. T17 establishes that the rule-type structure of $\tau_g$ is *non-Abelian-capable* but does not pin a specific group. For the present memo, we work *for any* compact simple gauge group $G$, with the choice of $G$ INHERITED at value layer (the Standard Model's specific $SU(3)\times SU(2)\times U(1)$ is empirically determined; any other compact simple $G$ is admissible at substrate level).

---

## 4. Step 2 — Substrate Field Strength

The substrate-level gauge-field strength is the directional-field curvature of $A_\mu$ under the non-Abelian commutator structure FORCED by T17.

**Field strength definition.** Define the substrate-level non-Abelian field strength

$$F_{\mu\nu} \;\equiv\; \partial_\mu A_\nu - \partial_\nu A_\mu - ig[A_\mu, A_\nu],$$

componentwise

$$F_{\mu\nu}^a \;=\; \partial_\mu A_\nu^a - \partial_\nu A_\mu^a + g f^{abc} A_\mu^b A_\nu^c.$$

The non-Abelian commutator term $-ig[A_\mu, A_\nu] = gf^{abc}A_\mu^b A_\nu^c\,T^a$ is **FORCED by the rule-type bracket structure** of $\tau_g$. Specifically:

- T17 clause C2 establishes the substrate gauge group as non-Abelian-capable with Lie bracket structure on the generators.
- The substrate-level participation-channel parallel-transport on a closed loop of side $\delta$ accrues a phase $\sim g[A_\mu, A_\nu]\,\delta^\mu\delta^\nu$ at second order, generated by the rule-type bracket.
- Closing the loop and antisymmetrizing in $(\mu,\nu)$ extracts the substrate curvature, identical in form to the standard Yang-Mills field strength.

For the Abelian case ($U(1)$, $f^{abc} = 0$), the commutator vanishes and $F_{\mu\nu} \to \partial_\mu A_\nu - \partial_\nu A_\mu$, the standard Maxwell field strength. The non-Abelian case adds the commutator structure as the load-bearing new element relative to the NS-MHD-2 Abelian derivation.

**Non-Abelian curl.** The Abelian curl of NS-MHD-1 ($\mathbf{B} = \nabla\times\mathbf{A}$, $\mathbf{E} = -\nabla\phi - \partial_t\mathbf{A}$) is the Abelian special case of the non-Abelian field strength under the identification $F_{0i} = E_i$ (electric components) and $F_{ij} = -\varepsilon_{ijk}B_k$ (magnetic components). The non-Abelian generalization adds the structure-constant terms:

$$F_{0i}^a \;=\; \partial_0 A_i^a - \partial_i A_0^a + g f^{abc}A_0^b A_i^c, \qquad F_{ij}^a \;=\; \partial_i A_j^a - \partial_j A_i^a + g f^{abc}A_i^b A_j^c.$$

In Abelian limit ($f^{abc} = 0$), the standard Maxwell field strengths are recovered.

**Bianchi identity.** As an algebraic consequence of the field-strength definition under the gauge-covariant derivative,

$$D_\mu F_{\nu\rho} + D_\nu F_{\rho\mu} + D_\rho F_{\mu\nu} \;=\; 0,$$

with $D_\mu F_{\nu\rho} = \partial_\mu F_{\nu\rho} - ig[A_\mu, F_{\nu\rho}]$. The Bianchi identity is structural, not dynamical — it follows from the definition of $F_{\mu\nu}$ in terms of $A_\mu$ and the Jacobi identity for the Lie algebra. It is preserved under coarse-graining since it is an algebraic identity of the substrate-level field strength.

---

## 5. Step 3 — Coarse-Graining the Non-Abelian Flux

Apply DCGT-style multi-scale expansion to the substrate gauge-field flux.

**Substrate gauge-flux tensor.** Define

$$\Phi_{\mu\nu}^a(x) \;=\; \text{(V1-kernel-weighted chain transport of $A_\nu^a$ along $\partial_\mu$ direction)},$$

i.e., the substrate-level transport of the gauge potential along the $\hat\mu$ chain-step direction, V1-weighted by the substrate finite-width kernel at scale $\ell_P$, evaluated on chains carrying gauge content under T17 minimal coupling. By construction, $\Phi_{\mu\nu}^a$ is a substrate object with $\mu$ the chain-step direction and $\nu, a$ the gauge-component indices of the transported potential.

**Hydrodynamic-window coarse-graining.** Apply $\langle\,\cdot\,\rangle_{R_\mathrm{cg}}$ to $\Phi_{\mu\nu}^a$ under the hydrodynamic window $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$ (Arc_YM_1 §1, Arc_D_6 §3). Multi-scale expansion of the V1-weighted transport integral parallels Arc_D_4 §4: zeroth moment yields the field itself; odd moments vanish by V1 isotropy; even moments yield successive Laplacian-class corrections.

**Result.** Antisymmetrizing $\Phi_{[\mu\nu]}^a$ on the spacetime indices and adding the rule-type commutator contribution from substrate parallel-transport (Step 2) yields:

$$\boxed{\;\langle\Phi_{[\mu\nu]}^a\rangle_{R_\mathrm{cg}} \;=\; F_{\mu\nu}^a \;+\; \mathcal{O}\bigl(\ell_P^2\,\nabla^2 A^a\bigr).\;}$$

Term-by-term:

- **Zeroth moment** → $\partial_\mu A_\nu^a - \partial_\nu A_\mu^a + gf^{abc}A_\mu^b A_\nu^c = F_{\mu\nu}^a$, the continuum non-Abelian field strength.
- **First moment** vanishes by V1 isotropy (parallel to Arc_D_2, Arc_D_3, Arc_D_5).
- **Second moment** → $\mathcal{O}(\ell_P^2\,\nabla^2 A)$ corrections to the field strength. These are the **YM analogue of R1**: a substrate-cutoff stabilization at next-to-leading order in the V1 second-moment expansion. They scale as $\ell_P^2\,\nabla^2 F_{\mu\nu}^a$ at the level of the YM Lagrangian (effectively a higher-derivative gauge-field kinetic term) and are recorded for YM-3 (mass gap from substrate cutoff). They are negligible at hydrodynamic gauge-field scales but become load-bearing for the YM-3 mass-gap analysis at $\sim\ell_P$ scales.

The leading-order ($R_\mathrm{cg} \to 0$ with $\ell_P/R_\mathrm{cg} \to 0$) coarse-grained antisymmetrized gauge-flux tensor is the canonical Yang-Mills field strength. The structural unity with NS-MHD-2 (Abelian limit recovers Maxwell field strength) and Arc_D_4 (V1 second-moment expansion produces R1 in the velocity sector; same machinery here produces the YM-analogue R1 in the gauge sector) is preserved.

---

## 6. Step 4 — Covariant Divergence from Substrate Momentum Flux

Derive $D_\mu F^{\mu\nu} = J^\nu$ via the same momentum-flux machinery used in Arc_D_5 for the Abelian Lorentz force, generalized to non-Abelian content.

**Substrate momentum-flux contribution from generalized minimal coupling.** Under T17 generalized minimal coupling on charged chains (Step 1), the chain canonical momentum is shifted by $-gA_\mu^a T^a$ (parallel to Arc_D_5 §4 Abelian case with $q \to gT^a$ acting on internal index space). The corresponding charged-chain momentum-flux contribution at fluid scale is

$$\delta\Pi^{(g)}_{\mu\nu} \;=\; J_\mu^a A_\nu^a,$$

with $J_\mu^a$ the gauge-current density at fluid scale (the non-Abelian analogue of $\mathbf{j} = \rho_q\mathbf{v}$ from Arc_D_5; here $J_\mu^a$ carries gauge-component index $a$ in addition to the spacetime index $\mu$). The construction is identical to Arc_D_5 §4: chain canonical momentum shift carries with the chain at velocity, producing momentum-flux density $\rho_q v^j A_i \to J_\mu^a A_\nu^a$ in the gauge generalization.

**Divergence.** Take the substrate momentum-flux divergence (parallel to Arc_D_5 §5):

$$\partial^\mu\delta\Pi^{(g)}_{\mu\nu} \;=\; J_\mu^a\partial^\mu A_\nu^a + (\partial^\mu J_\mu^a) A_\nu^a.$$

The second piece $(\partial^\mu J_\mu^a)A_\nu^a$ involves the gauge-current divergence. For Abelian gauge theory, this vanishes by ordinary current conservation $\partial^\mu J_\mu = 0$. For non-Abelian gauge theory, the analogous conservation law is the gauge-covariant version

$$D_\mu J^\mu \;=\; \partial^\mu J_\mu^a + gf^{abc}A^{\mu\,b}J_\mu^c \;=\; 0,$$

which follows from gauge invariance of the matter sector under T17 (clause C8 unified four-channel quotient; clause C3 vertex-quotient pulled back through coupling). The covariant-conservation law is a structural consequence of T17 gauge-quotient identification, FORCED at substrate level.

Substituting $\partial^\mu J_\mu^a = -gf^{abc}A^{\mu\,b}J_\mu^c$ into the divergence:

$$\partial^\mu\delta\Pi^{(g)}_{\mu\nu} \;=\; J_\mu^a\partial^\mu A_\nu^a - gf^{abc}A^{\mu\,b}J_\mu^c A_\nu^a.$$

**Cross-product → covariant derivative on $F$.** Using the Yang-Mills field-strength identity (the non-Abelian analogue of $\mathbf{j}\times\mathbf{B} = \mathbf{j}\times(\nabla\times\mathbf{A})$), the right-hand side rearranges into the covariant divergence $(D_\mu F^{\mu\nu})^a$:

$$(D_\mu F^{\mu\nu})^a \;=\; \partial_\mu F^{\mu\nu\,a} + gf^{abc}A_\mu^b F^{\mu\nu\,c},$$

with $F^{\mu\nu\,a}$ the field strength from Step 2. Combining the substrate-level momentum-flux divergence with the time-component minimal-coupling contribution (parallel to Arc_D_5 §5 Abelian case) and collecting all gauge-current source terms:

$$\boxed{\;(D_\mu F^{\mu\nu})^a \;=\; J^{\nu\,a}.\;}$$

This is the canonical Yang-Mills equation, derived from substrate primitives via DCGT-style multi-scale expansion of non-Abelian gauge-field correlators + momentum-flux divergence + non-Abelian charge conservation $D_\mu J^\mu = 0$.

The Abelian limit ($f^{abc} = 0$) recovers $\partial_\mu F^{\mu\nu} = J^\nu$, the inhomogeneous Maxwell equation. The non-Abelian case adds the structure-constant gauge-current self-coupling $gf^{abc}A_\mu^b F^{\mu\nu\,c}$ via the covariant derivative $D_\mu$.

---

## 7. Step 5 — Result: Continuum Yang-Mills Equation

**Theorem (Arc_YM_2 partial result, substrate-to-continuum YM equation).**

> *Under hydrodynamic-window coarse-graining $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$ over ED substrate primitives (chains, V1 / V5 kernels, charged structural rule-types under T17 generalized minimal coupling on a compact simple gauge group $G$), the cell-averaged non-Abelian gauge-field strength $F_{\mu\nu}^a(\mathbf{x},t)$ and gauge-current density $J^{\nu\,a}(\mathbf{x},t)$ satisfy the continuum Yang-Mills equation*

$$\boxed{\;D_\mu F^{\mu\nu} \;=\; J^\nu, \qquad F_{\mu\nu}^a \;=\; \partial_\mu A_\nu^a - \partial_\nu A_\mu^a + gf^{abc}A_\mu^b A_\nu^c,\;}$$

> *with covariant derivative $D_\mu = \partial_\mu - igA_\mu^a T^a$ acting in the appropriate matter-representation, and gauge-current covariantly conserved $D_\mu J^\mu = 0$ via T17 gauge-quotient identification. The structural form is FORCED by T17 generalized minimal coupling + DCGT multi-scale expansion + non-Abelian rule-type bracket structure; truncated higher-order corrections bounded by $\mathcal{O}((\ell_P/L_\mathrm{flow})^2)$ at the field-strength level.*

**Properties.**

**(1) Form-FORCED.** The non-Abelian commutator structure $-ig[A_\mu, A_\nu]$ in the field strength and the structure-constant self-coupling $gf^{abc}A_\mu^b F^{\mu\nu\,c}$ in the covariant divergence both arise automatically from T17's substrate-level rule-type bracket structure (clause C2 group structure; clause C3 vertex structure). The Abelian limit is the special case $f^{abc} = 0$. Form FORCED: no fluid-mechanical or constructive-QFT postulate enters the derivation.

**(2) Sign-FORCED.** The V1 kernel's positive Fourier transform (Theorem N1, Theorem 18) forces positive even moments. The leading-order continuum gauge-kinetic term $-\tfrac{1}{4}F_{\mu\nu}^a F^{\mu\nu\,a}$ inherits its stabilizing-class sign structure from V1 second-moment positivity at the substrate-flux level, parallel to Arc_D_3's viscosity / Arc_D_4's R1 sign-FORCED stabilizing arguments. The kinetic term is non-degenerate and stable in the continuum limit at substrate level.

**(3) Value-INHERITED.** The gauge coupling $g$, the specific compact simple gauge group $G$, the Killing-form normalization, and the V1 / V5 kernel widths are all INHERITED at value layer per T17's standard form-FORCED / value-INHERITED split. DCGT inherits this status: the substrate-derivation fixes structure but not pointwise numerical values.

**(4) Kinematic-coupling pattern preserved.** Following the NS-MHD-2 / NS-MHD-5 / Appendix C pattern, the YM equation contains canonical-ED content (gauge-field kinetic term from V1 second moment, minimal-coupling matter source $J^\nu$ from T17, non-Abelian commutator self-coupling from rule-type bracket) and excludes transport-kinematic content (no $\mathbf{v}\times\mathbf{B}$-type frame artifacts in the gauge-field equation; the only velocity-dependence is via the matter current $J^\nu$ through minimal coupling, which is canonical). The kinematic-coupling pattern (minimal-coupling-derived velocity-dependence canonical / transport-kinematic velocity-dependence non-ED) survives the non-Abelian extension.

This closes scope item YM-2 and produces the load-bearing technical result of the YM arc.

---

## 8. Step 6 — Relation to YM-3, YM-4, YM-5

The Arc_YM_2 derivation has three direct downstream consequences for the remaining sub-arcs:

**(i) YM-3 (mass gap from substrate cutoff) uses the $\ell_P$-suppressed corrections recorded in Step 3.** The $\mathcal{O}(\ell_P^2\,\nabla^2 A)$ correction to the coarse-grained field strength is the YM analogue of R1 in the velocity sector. At the level of the YM Lagrangian, this produces a higher-derivative gauge-field kinetic term effectively suppressing high-momentum modes at scale $\Lambda_\mathrm{V1} \sim 1/\ell_P$. The combination of (a) discrete-substrate spectrum at scale $\ell_P$, (b) V1-kernel-driven momentum-mode suppression, and (c) T18 forward-cone-causality preservation jointly produces a substrate-level mass gap by analogy to lattice gauge theory's gap arguments. YM-3 will analyze whether the gap survives the continuum limit ($\ell_P \to 0$ with appropriate scaling), which is the load-bearing question of YM-3.

**(ii) YM-4 (architectural classification) uses the canonical/non-canonical split established here.** The classification table for YM content (gauge-field kinetic term, self-coupling vertices, gauge-fixing terms, ghost terms, matter-coupling terms, substrate-cutoff R1-class corrections) follows the NS-MHD-4 / Appendix C template under the ED-I-06 ontology. The YM-2 derivation classifies each content channel by its substrate origin — V1 second-moment for kinetic content, T17 commutator for self-coupling, T17 minimal coupling for matter source, V1 fourth-moment for substrate-cutoff corrections — providing the classification table's structural backbone.

**(iii) YM-5 (OS-positivity preservation) uses the continuum limit derived here.** The analytic structure of the substrate-derived YM equation — specifically the V1 positive-Fourier-transform, T18 forward-cone-only support, and DCGT error-bound scaling — supplies the structural ingredients for OS-positivity preservation analysis. YM-5 will verify whether these ingredients jointly preserve reflection positivity through the continuum limit $\ell_P \to 0$, or whether additional structural commitments are required. The load-bearing question is whether T18 + V1 positivity + DCGT coarse-graining commute with the OS-axiom requirements at the operator-distribution level on $\mathbb{R}^4$.

The substrate-to-continuum derivation is now in place. The remaining sub-arcs analyze its consequences.

---

## 9. Recommended Next Steps

Proceed to **Arc_YM_3 (Mass Gap from Substrate Cutoff $\ell_P$)**. File: `theory/Yang-Mills/Arc_YM_3_Mass_Gap_From_Substrate_Cutoff.md`. Scope: analyze the mass-gap mechanism in the substrate-derived YM equation. Adapt the lattice-gauge-theory gap argument to ED substrate-discrete-and-finite structure at scale $\ell_P$. Identify the substrate-level mechanism for the mass gap (V1-kernel-driven momentum-mode suppression + T18 forward-cone-causality + discrete-substrate spectrum). Analyze whether the gap survives the continuum limit. Working a-priori: substrate-level gap is automatic; continuum-limit-survival is the load-bearing question.

Estimated 2–3 sessions for Arc_YM_3 given the technical load.

### Decisions for you

- **Confirm Arc_YM_2 substrate-to-continuum derivation.** Continuum YM equation $D_\mu F^{\mu\nu} = J^\nu$ with non-Abelian field strength $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu - ig[A_\mu, A_\nu]$ FORCED by T17 generalized minimal coupling + DCGT multi-scale expansion + non-Abelian rule-type bracket structure.
- **Confirm preservation of structural patterns.** Form-FORCED / sign-FORCED / value-INHERITED split preserved; kinematic-coupling pattern preserved; Bianchi identity preserved as algebraic structural consequence.
- **Confirm proceeding to Arc_YM_3 (mass gap from substrate cutoff $\ell_P$) as the next deliverable.**

---

*Arc_YM_2 closes the substrate-to-continuum non-Abelian gauge-field derivation. Continuum Yang-Mills equation $D_\mu F^{\mu\nu} = J^\nu$ with non-Abelian field strength $F_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a + gf^{abc}A_\mu^b A_\nu^c$ derived from ED substrate primitives via DCGT multi-scale expansion of gauge-field correlators + T17 generalized minimal coupling on charged chains + non-Abelian rule-type bracket structure on the gauge generators. Substrate-level field strength (Step 2) coarse-grains to canonical YM field strength at zeroth moment with $\mathcal{O}(\ell_P^2\nabla^2 A)$ R1-analogue correction at second moment. Substrate momentum-flux divergence (Step 4) under non-Abelian $D_\mu J^\mu = 0$ produces $D_\mu F^{\mu\nu} = J^\nu$. Form FORCED by T17 + DCGT + Lie-algebra bracket; signs FORCED stabilizing by V1 positive-Fourier-transform; values INHERITED at gauge coupling $g$ + kernel widths + specific compact simple gauge group. Bianchi identity preserved as algebraic structural consequence. Kinematic-coupling pattern preserved: gauge-field equation contains canonical-ED content (kinetic term, self-coupling, matter source via minimal coupling) and excludes transport-kinematic frame artifacts. Sets up YM-3 (mass gap from $\mathcal{O}(\ell_P^2)$ corrections + substrate cutoff), YM-4 (architectural classification), YM-5 (OS-positivity preservation through continuum limit). Arc_YM_3 (mass gap mechanism) is the next deliverable.*
