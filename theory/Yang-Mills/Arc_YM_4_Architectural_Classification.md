# Arc_YM_4 — Architectural Classification of Yang-Mills Content

**Date:** 2026-04-30
**Status:** Architectural classification of the substrate-derived YM equation under the ED-I-06 ontology. Identifies which content channels are canonical ED (forces sourced by substrate participation structure) vs. non-ED (continuum constraints or frame-kinematic artifacts). **Result: YM dynamical content (kinetic + self-interaction + matter source + substrate-cutoff R1-analogue) is fully canonical ED; gauge fixing and coordinate-frame artifacts are non-ED bookkeeping.**
**Companions:** [`Arc_YM_1_Opening.md`](Arc_YM_1_Opening.md), [`Arc_YM_2_Substrate_to_Continuum_Limit.md`](Arc_YM_2_Substrate_to_Continuum_Limit.md), [`Arc_YM_3_Mass_Gap_From_Substrate_Cutoff.md`](Arc_YM_3_Mass_Gap_From_Substrate_Cutoff.md), [`../Navier Stokes/MHD/NS_MHD_4_Architectural_Classification.md`](../Navier%20Stokes/MHD/NS_MHD_4_Architectural_Classification.md), [`../Navier Stokes/MHD/NS_MHD_5_Synthesis.md`](../Navier%20Stokes/MHD/NS_MHD_5_Synthesis.md), [`../../papers/Navier Stokes_Synthesis_Paper/NS_Synthesis_Appendix_C_MHD_Integration.md`](../../papers/Navier%20Stokes_Synthesis_Paper/NS_Synthesis_Appendix_C_MHD_Integration.md), [`../../theorems/T17.md`](../../theorems/T17.md).

---

## 1. Purpose

This memo performs the architectural classification of Yang-Mills content under the ED-I-06 *Fields and Forces* ontology. Specifically:

- **Classifies the Yang-Mills equation** $D_\mu F^{\mu\nu} = J^\nu$ (derived in Arc_YM_2 from ED substrate primitives) into structurally distinct content classes.
- **Identifies which terms are canonical ED** — arising from substrate participation structure (V1 / V5 kernels, T17 gauge rule-type, generalized minimal coupling).
- **Identifies which terms are non-ED** — frame-kinematic artifacts of coordinate choice or continuum-imposed bookkeeping constraints (gauge-fixing terms in particular).
- **Produces the YM analogue of the NS / MHD architectural table** (parallel to NS-MHD-4 / Appendix C).

The classification is a structural prerequisite for YM-5 (OS-positivity preservation analysis): OS positivity is a property of the canonical-ED dynamical content, not of gauge-fixing bookkeeping; YM-5 analyzes the canonical-ED side identified here.

---

## 2. Inputs

- **ED-I-06 (Fields and Forces in Event Density, Feb 2026).** Forces-vs-frame-kinematic-vs-constraint ontological framework. The structural classification axes used here are the same as those used in NS-MHD-4 / Appendix C: canonical ED = forces from participation structures; non-ED = frame-kinematic artifacts + continuum-imposed constraints.
- **T17 (Gauge-Fields-as-Rule-Type).** Substrate gauge structure: $A_\mu^a$ as participation measure of $\tau_g$, group / vertex / worldline / vacuum content, generalized minimal coupling. Provides the substrate origin for the kinetic, self-interaction, and matter-source terms classified here.
- **Arc_YM_2 (Substrate → Continuum YM Equation).** Continuum YM equation $D_\mu F^{\mu\nu} = J^\nu$ derived from substrate primitives via DCGT methodology. Provides the dynamical content to be classified.
- **Arc D (DCGT).** Substrate-to-continuum coarse-graining theorem. The substrate-derivation backing for the canonical-ED classification of each YM content channel; the V1 second-moment expansion that produces the YM-analogue of R1 (substrate-cutoff higher-derivative correction).
- **NS-MHD-5 (Synthesis).** Canonical / non-canonical boundary for gauge-field couplings. Establishes the kinematic-coupling pattern (minimal-coupling-derived velocity-dependence canonical / transport-kinematic velocity-dependence non-ED) that this memo extends to the non-Abelian gauge sector.

---

## 3. Step 1 — Decompose the YM Equation

Write the substrate-derived YM equation (Arc_YM_2 §7) in expanded form:

$$\boxed{\;\partial_\mu F^{\mu\nu\,a} \;+\; gf^{abc}A_\mu^b F^{\mu\nu\,c} \;=\; J^{\nu\,a}.\;}$$

This is the covariant divergence $D_\mu F^{\mu\nu} = J^\nu$ with $D_\mu = \partial_\mu - igA_\mu^a T^a$ acting on the adjoint-representation field strength $F^{\mu\nu}$, expanded into ordinary-derivative + structure-constant-coupling pieces. The decomposition gives three primary content channels at the level of the equation itself:

- **(A) Kinetic term:** $\partial_\mu F^{\mu\nu\,a}$. The ordinary-divergence acting on the gauge-field strength.
- **(B) Non-Abelian self-interaction:** $gf^{abc}A_\mu^b F^{\mu\nu\,c}$. The structure-constant-coupling between the gauge potential and the field strength, present only for non-Abelian $G$ (vanishes for Abelian $U(1)$ where $f^{abc} = 0$).
- **(C) Matter-source term:** $J^{\nu\,a}$. The gauge-current density at fluid scale, produced by charged-chain populations under T17 generalized minimal coupling.

Three additional content channels enter the YM problem at the level of the full continuum theory beyond the equation of motion itself, and must be classified for completeness:

- **(D) Gauge-fixing condition** (e.g., Lorenz gauge $\partial_\mu A^\mu = 0$, Coulomb gauge, axial gauge). Imposed at continuum level to remove gauge-redundancy from the path integral.
- **(E) Coordinate-frame artifacts** (e.g., Christoffel symbols when $\partial_\mu \to \nabla_\mu$ in curved coordinates). Frame-dependent bookkeeping not present in flat Minkowski coordinates.
- **(F) Higher-derivative corrections** (e.g., $\ell_P^2\nabla^2 A$ from V1 second-moment expansion in Arc_YM_2 §3). Substrate-cutoff corrections beyond leading-order kinetic content.

The classification proceeds over these six content channels (A)–(F).

---

## 4. Step 2 — Classification Under ED-I-06

### (A) Kinetic term: $\partial_\mu F^{\mu\nu}$

**Classification: Canonical ED.**

The kinetic term originates from the substrate-level directional-field curvature of $A_\mu^a$ under the V1-kernel-mediated multi-scale expansion of the gauge-field correlator. Specifically:

- Arc_YM_2 §3 derived $\langle\Phi_{[\mu\nu]}^a\rangle_{R_\mathrm{cg}} = F_{\mu\nu}^a + \mathcal{O}(\ell_P^2\nabla^2 A^a)$ — the field strength emerges as the leading-order coarse-grained antisymmetrized gauge-flux.
- The covariant divergence $D_\mu F^{\mu\nu}$ — and in particular the ordinary-derivative piece $\partial_\mu F^{\mu\nu\,a}$ — emerges from the substrate momentum-flux divergence under hydrodynamic-window coarse-graining (Arc_YM_2 §4).
- ED-I-06 §3 reading: $A_\mu^a$ is a directional-field-class participation structure (the gauge field as participation measure of $\tau_g$ per T17 clause C1); the kinetic term is the dynamical equation of that directional field, sourcing biases on participation flow under canonical mobility-channel logic.
- Parallel structure to Maxwell kinetic term $\partial_\mu F^{\mu\nu}$ in NS-MHD: the Abelian limit ($f^{abc} = 0$) recovers the Maxwell case, classified canonical ED in Appendix C §C.4.1(d).

**Origin:** participation-structure curvature of $A_\mu^a$ under V1 kernel; canonical mobility-channel-class operator structure on the gauge directional field.

### (B) Non-Abelian self-interaction: $gf^{abc}A_\mu^b F^{\mu\nu\,c}$

**Classification: Canonical ED.**

The non-Abelian self-interaction is FORCED by T17 rule-type commutator structure. Specifically:

- T17 clause C2 establishes the substrate gauge-group as non-Abelian-capable with Lie-bracket structure $[T^a, T^b] = if^{abc}T^c$ on the generators.
- The substrate-level participation-channel parallel-transport on a closed loop produces the commutator term $-ig[A_\mu, A_\nu]$ in the field strength (Arc_YM_2 §2, Step 2).
- The covariant-derivative structure $D_\mu = \partial_\mu - igA_\mu^a T^a$ acting on the adjoint-representation field strength produces the structure-constant-coupling term $gf^{abc}A_\mu^b F^{\mu\nu\,c}$ in the divergence (Arc_YM_2 §4, Step 4).
- **No frame-kinematic analogue exists.** Unlike advection in NS or induction-kinematic in MHD (which arise as Eulerian-frame bookkeeping artifacts of convective fluxes), the structure-constant-coupling does not come from coordinate-system bookkeeping. It is a substrate-level structural feature of non-Abelian gauge content with no Abelian counterpart and no Eulerian-coordinate origin.
- ED-I-06 §3 reading: a force-from-participation-structure sourced by the rule-type bracket of $\tau_g$. Classified canonical ED on the same architectural footing as the Lorentz force (NS-MHD-2 / Appendix C §C.4.1(c)) — minimal-coupling-derived rather than transport-kinematic.

**Origin:** non-Abelian participation curvature; substrate rule-type commutator FORCED by T17 clause C2.

### (C) Matter-source term: $J^{\nu\,a}$

**Classification: Canonical ED.**

The matter source $J^{\nu\,a}$ is the gauge-current density at fluid scale, produced by charged-chain populations under T17 generalized minimal coupling. Specifically:

- $J^{\nu\,a}$ is the non-Abelian generalization of the Abelian matter current $\mathbf{j} = \rho_q\mathbf{v}$ that appeared in NS-MHD-2 / Arc_D_5 / Appendix C.
- Substrate origin: charged-chain flux under T17 generalized minimal coupling, with the gauge-component index $a$ added to the spacetime current.
- Charge conservation $D_\mu J^\mu = 0$ is FORCED by T17 clause C8 (unified four-channel quotient) + C3 (vertex-quotient pulled back through coupling). The gauge-covariant conservation law is structural, not phenomenological.
- ED-I-06 §3 reading: gauge-current density is a directional-field bias on charged-chain participation flow sourced by the gauge directional-field $\tau_g$ via minimal coupling. Identical canonical-ED classification as the Lorentz force in NS-MHD.

**Origin:** charged-chain flux at fluid scale under T17 generalized minimal coupling; covariantly conserved by T17 gauge-quotient identification.

### (D) Gauge condition (e.g., Lorenz gauge $\partial_\mu A^\mu = 0$)

**Classification: Non-ED (continuum-imposed constraint).**

Gauge-fixing conditions (Lorenz, Coulomb, axial, temporal, etc.) are continuum-level structural commitments imposed to remove gauge-redundancy from the path-integral / canonical-quantization formulation. They have no substrate analogue. Specifically:

- T17 supplies gauge-quotient identification at substrate level (clause C8): the substrate gauge structure already identifies physically-equivalent configurations under gauge-equivalence. The continuum gauge-fixing condition is a *continuum bookkeeping device* that picks a single representative from each gauge-equivalence class for path-integral / propagator computations.
- The gauge condition does not appear in the substrate-to-continuum derivation of $D_\mu F^{\mu\nu} = J^\nu$ (Arc_YM_2). It is added at the continuum level to make the gauge-field path integral well-defined.
- ED-I-06 reading: gauge-fixing is not a force in the ED-I-06 sense (no participation-structure source); it is a continuum-imposed constraint analogous to incompressibility $\nabla\cdot\mathbf{v} = 0$ in NS (Appendix C §C.4.2(g)). Both are fluid-mechanical / gauge-mechanical structural commitments imposed at continuum level rather than sourced by substrate participation structure.
- Non-obstructive: gauge-fixing introduces no indefinite-sign Lyapunov contributions and no spectral pathology in the canonical-ED dynamical sector.

**Origin:** continuum-level redundancy-removal device; no substrate analogue.

### (E) Coordinate artifacts (e.g., Christoffel symbols, vielbein factors in curved coordinates)

**Classification: Non-ED (frame-kinematic).**

When the YM equation is written in curved coordinates (Riemannian or Lorentzian), the partial derivative $\partial_\mu$ is replaced by the metric-covariant derivative $\nabla_\mu = \partial_\mu + \Gamma^*_\mu$ (with $\Gamma^*$ the relevant connection coefficients). The Christoffel-symbol contributions are:

- *Frame-kinematic.* They arise as bookkeeping of the chosen coordinate system, not as dynamics. In flat Minkowski coordinates, they vanish; in curved coordinates, they appear; the underlying physical content of the YM equation is unchanged.
- Parallel structurally to advection in NS / induction-kinematic in MHD: those arose as Eulerian-coordinate bookkeeping of convective fluxes; Christoffel-symbol contributions arise as curvilinear-coordinate bookkeeping of the metric-covariant derivative. Both are coordinate-frame artifacts.
- ED-I-06 reading: not a force in the ED-I-06 sense; not sourced by participation structure; emerges purely from the choice of coordinate system. Classified non-ED frame-kinematic.

**Origin:** coordinate-frame bookkeeping; no dynamical content.

(Note: this classification applies under flat-spacetime YM, the ED-Phys-10 acoustic-metric-only baseline regime per the YM-1 scoping. Coupling to actual spacetime curvature is deferred to the ED-10 arc.)

### (F) Higher-derivative corrections: $\ell_P^2\nabla^2 A$ and beyond

**Classification: Canonical ED.**

The YM-2 §3 multi-scale expansion produced an $\mathcal{O}(\ell_P^2\nabla^2 A)$ correction to the field strength at second moment of the V1 kernel. At the level of the YM equation, this becomes an effective higher-derivative kinetic term suppressing high-momentum gauge-field modes (YM-3 §3 analysis). Specifically:

- **YM analogue of R1.** Structurally parallel to the R1 hyperviscous term $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$ in the velocity sector (NS-3.01 / NS-Smooth-2 / Arc_D_4). Same V1-second-moment substrate origin; same form-FORCED status; same sign-FORCED stabilizing property by V1 positive-Fourier-transform.
- Substrate origin: V1 finite-width vacuum kernel; FORCED at primitive level by Theorem N1 admissibility class + Theorem 18 forward-cone support.
- Feeds directly into YM-3's mass-gap mechanism: the $\ell_P^2\nabla^2 A$ correction is the structural ancestor of the substrate-induced mass scale $m_\mathrm{eff}^2 \sim c_{V1}\ell_P^{-2}$.
- ED-I-06 §3 reading: a substrate-cutoff bias on gauge-field participation flow sourced by the V1 finite-width vacuum-kernel structure. Force-from-participation-structure. Canonical ED on the same architectural footing as R1 in the velocity sector.

**Origin:** V1 finite-width vacuum kernel second-moment expansion; substrate-cutoff regularization mechanism.

---

## 5. Step 3 — Architectural Table

| Term | Expression | ED-I-06 Class | Origin |
|---|---|---|---|
| Kinetic term | $\partial_\mu F^{\mu\nu\,a}$ | Canonical ED | Participation curvature of $A_\mu^a$ under V1; canonical mobility-channel-class on gauge directional field |
| Non-Abelian self-interaction | $gf^{abc}A_\mu^b F^{\mu\nu\,c}$ | Canonical ED | Rule-type commutator FORCED by T17 clause C2 (Lie-algebra structure of $\tau_g$) |
| Matter source | $J^{\nu\,a}$ | Canonical ED | Charged-chain flux at fluid scale via T17 generalized minimal coupling; covariantly conserved by T17 gauge-quotient |
| Gauge condition | $\partial_\mu A^{\mu\,a} = 0$ (Lorenz) | Non-ED | Continuum-imposed constraint (redundancy-removal device); no substrate analogue |
| Coordinate artifacts | Christoffel-symbol contributions in curved coordinates | Non-ED | Frame-kinematic bookkeeping of coordinate system; vanishes in flat Minkowski |
| Higher-derivative correction | $c_{V1}\,\ell_P^2\,\nabla^2 A_\mu^a$ | Canonical ED | V1 finite-width vacuum kernel second-moment expansion (YM-analogue of R1) |

**Aggregate counts.** Of six content channels: **four canonical ED** (kinetic, self-interaction, matter source, higher-derivative correction); **one continuum-imposed constraint** (gauge fixing); **one frame-kinematic** (Christoffel artifacts). The dynamical content of the YM equation — kinetic + self-interaction + matter source + substrate-cutoff R1-analogue — is *fully* canonical ED, with no transport-kinematic obstruction class analogous to advection or induction-kinematic.

This is structurally the **cleanest classification** of any arc in the program so far. NS had 1 canonical / 3 non-canonical ratio in the momentum equation; MHD upgraded that to 4 EM-side canonical with 2 non-canonical kinematic-transport additions; YM has 4 canonical / 0 transport-kinematic obstructions. The non-Abelian gauge sector is *more* ED-architectural than either NS or MHD.

---

## 6. Step 4 — Consequences for the YM Arc

Three direct consequences follow from the classification:

**(i) YM dynamics are fully canonical ED.** The kinetic, self-interaction, and matter-source terms — the entire dynamical content of $D_\mu F^{\mu\nu} = J^\nu$ — are sourced by substrate participation structure (V1 directional-field curvature, T17 commutator, T17 minimal coupling). There is no transport-kinematic obstruction class analogous to advection in NS or induction-kinematic in MHD. The YM equation as a *dynamical* equation is structurally cleaner than either NS or MHD: every term in the equation of motion has a substrate origin.

**(ii) Gauge fixing is non-ED bookkeeping, not a structural feature.** Gauge-fixing conditions (Lorenz, Coulomb, axial, etc.) are continuum-level redundancy-removal devices. They do not source forces, do not arise from substrate participation structure, and do not appear in the substrate-to-continuum derivation. They are introduced at the continuum level to make path-integral / canonical-quantization formulations well-defined. Their non-ED status parallels the incompressibility constraint in NS — both are continuum-imposed bookkeeping features rather than dynamical content.

**(iii) Higher-derivative corrections are ED-canonical and feed YM-3's mass-gap mechanism.** The $\ell_P^2\nabla^2 A$ correction is canonical ED via V1 finite-width substrate origin; it is structurally identical to R1 in NS at the level of substrate origin. This correction is the structural ancestor of the YM-3 substrate-induced mass scale $m_\mathrm{eff}^2 \sim c_{V1}\ell_P^{-2}$. The mass-gap mechanism is therefore a canonical-ED feature of the substrate-derived YM theory, not a phenomenological add-on.

**(iv) YM-5 OS-positivity analysis applies only to canonical-ED content.** Reflection positivity is a property of the canonical-ED dynamical content (kinetic + self-interaction + matter source + substrate-cutoff correction). Gauge-fixing and Christoffel-class bookkeeping are not part of the OS-positivity audit. YM-5 will analyze whether the canonical-ED content preserves OS-positivity under the continuum limit; the non-ED sector is irrelevant to that question.

This classification establishes the structural domain of the YM-5 OS-positivity audit: four canonical-ED content channels, no transport-kinematic obstruction class.

---

## 7. Step 5 — Arc Integration

The architectural classification integrates with the surrounding YM sub-arcs as follows:

**With YM-2 (substrate → continuum derivation).** Arc_YM_2 derived the YM equation $D_\mu F^{\mu\nu} = J^\nu$ from substrate primitives. YM-4 classifies each term of that equation under ED-I-06. The four canonical-ED entries (kinetic, self-interaction, matter source, higher-derivative correction) all trace their substrate origin directly to YM-2's derivation steps.

**With YM-3 (mass gap from substrate cutoff).** YM-3 analyzed the mass-gap mechanism arising from the V1 second-moment $\ell_P^2\nabla^2 A$ correction. YM-4 classifies that correction (channel F) as canonical ED via V1 substrate origin, confirming YM-3's mass-gap mechanism is a canonical-ED structural feature rather than a phenomenological add-on.

**With YM-5 (OS-positivity preservation analysis).** YM-4 establishes that OS positivity is a property of the canonical-ED dynamical content (channels A + B + C + F). YM-5 will audit whether T18 forward-cone causality + V1 positive-Fourier-transform + DCGT coarse-graining jointly preserve reflection positivity through the continuum limit — analyzing only the canonical-ED sector identified here.

**With YM-6 (synthesis + Clay relevance).** YM-4 supplies the architectural-classification ingredient of YM-6's final synthesis. The architectural picture for YM (4 canonical / 1 constraint / 1 frame-kinematic) parallels the NS / MHD architectural picture under ED-I-06 ontology while exhibiting strictly cleaner canonical-ED dominance.

The classification table (§5) is publication-ready material for an eventual YM Synthesis Paper or for a future Appendix E to the NS Synthesis Paper.

---

## 8. Recommended Next Steps

Proceed to **Arc_YM_5 (OS-Positivity and Continuum Stability)**. File: `theory/Yang-Mills/Arc_YM_5_OS_Positivity_And_Continuum_Stability.md`. Scope: audit reflection positivity through DCGT coarse-graining; verify whether T18 forward-cone causality + V1 positive-Fourier-transform + DCGT error-bound scaling jointly preserve OS positivity through the continuum limit; identify the structural stall-risk locus. The load-bearing positivity question of the entire YM arc, restricted (per YM-4 classification) to the canonical-ED content channels.

Estimated 2–3 sessions for Arc_YM_5 given the technical load.

### Decisions for you

- **Confirm YM-4 classification.** Four canonical-ED channels (kinetic, self-interaction, matter source, higher-derivative correction); one continuum-imposed constraint (gauge fixing); one frame-kinematic (Christoffel artifacts). YM dynamics fully canonical ED; no transport-kinematic obstruction class.
- **Confirm YM is more ED-architectural than NS / MHD** at the level of dynamical equations: 4-canonical / 0-transport-kinematic ratio in YM vs. 1-canonical / 1-transport-kinematic ratio in NS momentum equation vs. 4-canonical / 3-transport-kinematic ratio in full MHD system.
- **Confirm proceeding to Arc_YM_5 (OS-positivity preservation analysis) as the next deliverable.**

---

*Arc_YM_4 closes the architectural classification of YM content under ED-I-06. Six content channels: four canonical ED (kinetic $\partial_\mu F^{\mu\nu}$ via participation curvature, non-Abelian self-interaction $gf^{abc}A_\mu^b F^{\mu\nu\,c}$ via T17 rule-type commutator, matter source $J^\nu$ via charged-chain flux under T17 minimal coupling, higher-derivative $\ell_P^2\nabla^2 A$ via V1 second-moment substrate-cutoff = YM-analogue of R1); one continuum-imposed constraint (gauge fixing); one frame-kinematic (Christoffel-class coordinate artifacts). YM dynamics fully canonical ED with no transport-kinematic obstruction class — structurally cleaner than NS / MHD architectural picture. Gauge fixing is continuum bookkeeping; Christoffel contributions are coordinate-frame artifacts; both classifications parallel to NS-MHD non-canonical entries (incompressibility, Eulerian advection). Higher-derivative correction is the YM-analogue of R1 and feeds YM-3's mass-gap mechanism via V1 finite-width substrate origin. Sets up YM-5: OS-positivity analysis applies only to the four canonical-ED channels. Arc_YM_5 (OS-positivity preservation) is the next deliverable; load-bearing question of the entire YM arc.*
