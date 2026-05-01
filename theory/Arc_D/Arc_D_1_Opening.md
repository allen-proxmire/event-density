# Arc D — The Diffusion Coarse-Graining Theorem (Arc Opening)

**Date:** 2026-04-30
**Status:** Arc opening. **Arc D** — the diffusion coarse-graining arc. Closes the INHERITED bridges in NS-2 (viscous content) and NS-MHD-2 (Lorentz coarse-graining); supplies the substrate-to-continuum derivation of mobility-channel diffusion; completes the architectural foundation for all fluid-mechanical arcs.
**Companions:** [`../Navier Stokes/NS-2.08_ED-PDE_Direct_Mapping.md`](../Navier%20Stokes/NS-2.08_ED-PDE_Direct_Mapping.md), [`../Navier Stokes/MHD/NS_MHD_2_Lorentz_Force.md`](../Navier%20Stokes/MHD/NS_MHD_2_Lorentz_Force.md), [`../../papers/NS_Synthesis_Paper/NS_Synthesis_Paper.md`](../../papers/NS_Synthesis_Paper/NS_Synthesis_Paper.md), [`../../papers/NS_Synthesis_Paper/NS_Synthesis_Appendix_C_MHD_Integration.md`](../../papers/NS_Synthesis_Paper/NS_Synthesis_Appendix_C_MHD_Integration.md), [`../../theorems/T17.md`](../../theorems/T17.md), [`../../arcs/arc-B/arc_b_synthesis.md`](../../arcs/arc-B/arc_b_synthesis.md) (T18 V1 kernel retardation), [`../Architectural_Canon_Vector_Extension.md`](../Architectural_Canon_Vector_Extension.md).

---

## 1. Purpose

This arc proves the **Diffusion Coarse-Graining Theorem (DCGT)**:

> *Starting from ED substrate primitives — chains, events, participation channels, V1 / V5 kernels — coarse-graining over a cell of radius $R_\mathrm{cg}$ in the hydrodynamic window produces a continuum diffusion operator of the form*
>
> $$\partial_t \rho = \nabla\cdot\bigl(M(\rho)\,\nabla\rho\bigr) + \cdots$$
>
> *for scalar fields, and*
>
> $$\partial_t \mathbf{v} = \mu\,\nabla^2\mathbf{v} + \cdots$$
>
> *for directional fields, where $M(\rho)$ is the substrate-derived mobility coefficient and $\mu$ is the substrate-derived kinematic viscosity (both INHERITED at value layer).*

The DCGT delivers four structural payoffs:

- **Closes the INHERITED bridge in NS-2 viscous content.** NS-2 derived the form $\mu\nabla^2\mathbf{v}$ from the canonical mobility channel via partial vector-extension and chain-substrate coarse-graining heuristics. The coarse-graining step itself was not internally proven; it was INHERITED from standard kinetic-theory practice. DCGT supplies the missing internal derivation.
- **Closes the INHERITED bridge in NS-MHD-2 Lorentz coarse-graining.** NS-MHD-2 derived the fluid-level Lorentz force $(\nabla\times\mathbf{B})\times\mathbf{B}$ from T17 substrate-level minimal coupling on charged chains, with the chain-population averaging step INHERITED in parallel. DCGT supplies the same coarse-graining bridge for charged-chain populations.
- **Provides the substrate-level origin of mobility-channel diffusion.** ED's canonical PDE postulates a mobility-channel operator structure; DCGT derives that structure as the natural coarse-graining limit of substrate participation-channel statistics, grounding the canonical PDE itself at substrate level.
- **Completes the architectural foundation for all fluid-mechanical arcs.** Once DCGT is proved, every fluid-mechanical-arc result that depends on the mobility-channel coarse-graining bridge — NS-2, NS-3, NS-Smoothness, NS-Turb, P4-NN, NS-MHD — reads as substrate-grounded rather than INHERITED-at-the-coarse-graining-step.

DCGT does **not** introduce new physics or revise any closed-arc conclusion. It proves the bridge that those arcs already structurally require.

---

## 2. Motivation

Three considerations make Arc D the natural next major arc.

**The NS / MHD program is otherwise structurally complete.** As of 2026-04-30, NS-1 (dimensional forcing), NS-2 (form derivation), NS-3 / NS-Smoothness (Intermediate Path C, R1 mechanism, vortex-stretching obstruction), NS-Turb (P7 ↔ cascade, no template), P4-NN (Krieger-Dougherty + Maxwell viscoelastic), NS-Q (Q ≈ 3.5 canon-internal), and NS-MHD (5 memos, full classification under ED-I-06) are all closed. The NS Synthesis Paper is published with Appendix C integration of the MHD classification and ED-I-06 ontological reading. The only remaining structural gap in the fluid-mechanical foundation is the substrate-to-continuum derivation of diffusion.

**Arc D is required for publication-grade closure of the NS Synthesis Paper and MHD classification.** The synthesis paper currently states form FORCED / coarse-graining INHERITED for the canonical viscous content and the Lorentz force. This is honest, but it leaves a closable structural hole: every reader sufficiently versed in kinetic theory will note that the coarse-graining step is standard machinery and ask whether ED supplies its own internal derivation. Arc D answers yes and closes the hole. Once Arc D closes, the synthesis paper can be revised to state form FORCED / coarse-graining FORCED via Arc D — strictly stronger framing.

**Arc D is upstream of future major arcs.** The Hall-MHD / Resistive-MHD extension, the Yang-Mills roadmap, and the ED-10 spacetime-emergence arc all depend on coarse-graining-bridge content that Arc D supplies. Hall-MHD requires charged-chain statistical bridge with finite electron inertia; Yang-Mills requires substrate-to-continuum gauge-field correlator coarse-graining (in particular OS-positivity preservation, which is the Yang-Mills stall-risk locus); ED-10 requires substrate-to-continuum metric-emergence coarse-graining building on the curvature-like-field thread of ED-I-06 §5. All three benefit from a clean DCGT in place. Arc D is therefore the highest-leverage open item in the program.

---

## 3. Scope

Arc D's scope is precisely defined by the structural bridges it must close.

**(S1) Derive scalar diffusion from substrate event-flux statistics.** Starting from a chain-population participation-density field $\rho(\mathbf{x},t) = \langle\rho_\mathrm{chain}\rangle_{R_\mathrm{cg}}$ defined as the cell-averaged number density of chain commitments, derive the continuum equation $\partial_t\rho = \nabla\cdot(M(\rho)\nabla\rho) + \cdots$ via the standard coarse-graining of substrate event-flux statistics $\mathbf{j} = -M(\rho)\nabla\rho$ (Fick's-law-class) plus continuity. The mobility coefficient $M(\rho)$ identified at substrate level via the chain-step statistics; functional form FORCED, numerical value INHERITED.

**(S2) Derive directional-field diffusion (viscosity) from chain momentum-flux statistics.** Starting from a chain-population velocity field $\mathbf{v}(\mathbf{x},t)$ defined as the cell-averaged participation-momentum density divided by mass density, derive the continuum equation $\partial_t\mathbf{v} = \mu\nabla^2\mathbf{v} + \cdots$ via the coarse-graining of substrate momentum-flux statistics. The kinematic viscosity $\mu$ identified at substrate level via the chain-step momentum-statistics. Functional form FORCED via the field-type-agnostic vector-extension of the mobility channel (per Architectural Canon Vector Extension memo); numerical value INHERITED.

**(S3) Derive the coarse-grained form of V1 / V5 kernel contributions.** Coarse-grain the V1 finite-width vacuum kernel and the V5 cross-chain kernel over $R_\mathrm{cg}$. Identify the emergent macroscopic operators: V1 → R1 substrate-cutoff hyperviscous term $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$ (NS-3.01 / NS-Smooth-2); V5 → cross-chain memory contribution at fluid scale (per NS-P4-NN-D5 viscoelastic ansatz). Confirm consistency with the closed-arc V1/V5 results.

**(S4) Establish the hydrodynamic window.** The coarse-graining cell radius must satisfy
$$\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow},$$
where $\ell_P$ is the substrate length scale (Planck-class for the canonical ED program) and $L_\mathrm{flow}$ is the macroscopic flow length scale. The lower bound ensures statistical regularity (enough chains per cell for averaging); the upper bound ensures the cell is small relative to flow gradients (so that gradient-expansion truncation is valid). Identify the parametric scaling of error terms (gradient-expansion remainder, statistical-fluctuation remainder).

**(S5) Produce the continuum limit and identify the mobility coefficient.** Take the limit $R_\mathrm{cg} \to 0$ with $\ell_P / R_\mathrm{cg} \to 0$ at fixed $L_\mathrm{flow}$. Show that the continuum mobility / viscosity coefficient is well-defined as the substrate-derived quantity, with the value INHERITED at value layer. State and prove the diffusion coarse-graining theorem in canonical form.

**(S6) Show how minimal coupling (T17) interacts with coarse-graining for Lorentz force.** Coarse-grain a charged-chain population whose substrate dynamics include the T17 minimal-coupling vertex $\partial_\mu \to \partial_\mu - iqA_\mu$. Confirm that the coarse-grained force density is the canonical $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$, closing NS-MHD-2's INHERITED coarse-graining bridge. Identify any correction terms at next-to-leading order in $R_\mathrm{cg}$ for completeness.

The arc covers exactly these six scope items. It is methodologically a substrate-to-continuum derivation arc, parallel in scope to but technically distinct from the NS / MHD architectural-classification arcs.

---

## 4. Non-Goals

Arc D explicitly does **not**:

- **Derive numerical viscosity values.** All numerical coefficients ($\mu$, $\eta$, $M(\rho)$ pointwise values) are INHERITED at value layer per the program's standard form-FORCED / value-INHERITED methodology. Arc D fixes the form of mobility coefficients via substrate statistics; it does not predict their numerical values.
- **Derive turbulence models.** NS-Turb closed the P7 ↔ turbulence-cascade question with H1 trivial / H2 partial / H3 fail (no architectural template for developed-cascade turbulence). Arc D does not re-attempt that question; the coarse-graining bridge is upstream of turbulence-regime dynamics.
- **Derive compressible NS.** Arc D's scope is the incompressible regime, matching the NS / MHD synthesis paper's scope. Compressible-fluid extensions (compressible NS, compressible MHD, relativistic hydrodynamics) are out of scope and deferred to potential future arcs.
- **Derive Maxwell's equations.** Maxwell field structure is canonical ED via T17 directly (NS-MHD-1, NS-MHD-4, Appendix C §C.4.1(d)). Arc D's role for the EM sector is to coarse-grain charged-chain dynamics under T17 minimal coupling (S6), not to derive Maxwell from substrate.
- **Extend to ED-10 curvature-geometry.** ED-I-06 §5's curvature-like-field thread and the eventual ED-10 spacetime-emergence arc are out of scope. DCGT operates in flat-spacetime kinematic-acoustic-metric regime per ED-Phys-10 guardrails.
- **Re-open any closed arc.** NS-1 through NS-MHD-5 are all preserved in their current closure status. Arc D supplies the substrate bridge those arcs require; it does not revise any of their conclusions.

---

## 5. Inputs (Upstream Arcs)

Arc D depends structurally on the following upstream content:

- **ED-I-06 (Fields and Forces in Event Density).** Three field classes (directional / scalar / curvature-like); forces-vs-frame-kinematic ontology. DCGT is naturally read under ED-I-06 as the substrate-to-continuum derivation of the *force* content of fluid mechanics — the biases on participation flow sourced by participation structures. Arc D explicitly uses ED-I-06 ontology to organize the scalar-diffusion / directional-diffusion split (S1 vs. S2).
- **Theorem 17 (Gauge-Fields-as-Rule-Type).** Substrate-level minimal coupling structure $\partial_\mu \to \partial_\mu - iqA_\mu$ on charged rule-types. Required for S6 (Lorentz force coarse-graining).
- **Theorem 18 (V1 Kernel Retardation).** V1's forward-cone-only support structure. Required for S3 (V1 kernel coarse-graining → R1 emergence) and ensures the coarse-grained kernel inherits causal structure.
- **NS-2 viscous content classification.** The form-FORCED viscous-diffusion result that Arc D's S2 grounds at substrate level. Specifically NS-2.04 (momentum balance), NS-2.05 (stress tensor), NS-2.07 (synthesis), NS-2.08 (ED-PDE direct mapping).
- **NS-MHD-2 Lorentz coarse-graining.** The form-FORCED Lorentz-force-via-T17 result that Arc D's S6 grounds at substrate level.
- **NS Synthesis Paper.** Architectural context — the canonical / non-canonical classification under which DCGT supplies the canonical-side substrate bridge. Arc D does not affect non-canonical-side content (advection, induction kinematic, Ohm kinematic, pressure, incompressibility).
- **NS-MHD-5 (final MHD classification).** The eleven-item classification table that Arc D's substrate bridge grounds for the canonical-ED items.
- **Architectural Canon Vector Extension.** The field-type-agnostic vector-extension of the mobility channel that Arc D's S2 invokes to derive directional-field diffusion alongside scalar-field diffusion.

These seven inputs supply the structural prerequisites. No new primitives or theorems are required as inputs; Arc D builds entirely on existing closed content.

---

## 6. Planned Structure of Arc D (6 memos)

The arc is planned as six memos parallel in scope to NS-Smoothness and NS-MHD:

1. **Arc_D_1_Opening.md** *(this memo)* — Framing, scope, non-goals, inputs, plan.

2. **Arc_D_2_Scalar_Diffusion_From_Substrate.md** — Derive scalar diffusion $\partial_t\rho = \nabla\cdot(M(\rho)\nabla\rho)$ from event-flux statistics. Define cell-averaged participation density; identify chain-step transition probabilities; derive Fick's-law-class flux $\mathbf{j} = -M(\rho)\nabla\rho$ at substrate level via gradient expansion; identify $M(\rho)$ as substrate-statistics quantity. Confirm consistency with ED canonical PDE's mobility-channel structure.

3. **Arc_D_3_Directional_Field_Diffusion.md** — Derive viscosity $\mu\nabla^2\mathbf{v}$ from chain momentum-flux statistics. Define cell-averaged momentum density and velocity field; identify the substrate momentum-flux tensor; derive the Newtonian stress-tensor structure under gradient expansion; identify $\mu$ as substrate-statistics quantity. Apply field-type-agnostic vector-extension to confirm canonical structure.

4. **Arc_D_4_Kernel_Coarse_Graining.md** — Coarse-grain V1 finite-width vacuum kernel and V5 cross-chain kernel. Identify R1 emergence from V1 at fluid scale ($-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$); confirm consistency with NS-3.01 form-FORCED derivation. Identify V5-induced cross-chain memory contribution at fluid scale; confirm consistency with P4-NN-D5 viscoelastic ansatz. Verify causal-structure preservation under coarse-graining (T18 inherited).

5. **Arc_D_5_Minimal_Coupling_Coarse_Graining.md** — Coarse-grain T17 minimal-coupling structure on charged-chain population. Derive the fluid-level Lorentz force density $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$ at substrate level; close NS-MHD-2's INHERITED bridge. Identify next-to-leading-order corrections in $R_\mathrm{cg} / L_\mathrm{flow}$; classify them under ED-I-06 ontology.

6. **Arc_D_6_Synthesis_And_Theorem.md** — State and prove the Diffusion Coarse-Graining Theorem in canonical form. Aggregate the four substrate-derivation results (scalar diffusion, directional diffusion, kernel coarse-graining, minimal-coupling coarse-graining) into a single theorem statement. Verify hydrodynamic-window scaling and error bounds. Close the arc with a verdict and update the program inventory (DCGT becomes a structural-foundation theorem on the same footing as T18 / T19).

Estimated effort: 6 memos at the demonstrated pace, comparable to NS-Smoothness (5 memos) and NS-MHD (5 memos). Total estimated 5–7 effective sessions.

---

## 7. Deliverables

Final outputs of Arc D:

- **A formal theorem statement.** The Diffusion Coarse-Graining Theorem in canonical form, stating (i) the substrate-to-continuum mapping, (ii) the hydrodynamic-window conditions, (iii) the form-FORCED / value-INHERITED split, (iv) the resulting continuum diffusion operators for scalar and directional fields, (v) the closure of NS-2 and NS-MHD-2 INHERITED bridges. Parallel in form to T18 and T19 statements.
- **A derivation of scalar and directional diffusion.** Substrate-level event-flux and momentum-flux statistics; gradient-expansion derivation; identification of mobility / viscosity coefficients as substrate quantities; consistency verification with canonical ED PDE structure.
- **A unified substrate-to-continuum mapping.** Single coarse-graining framework covering scalar fields, directional fields, V1 / V5 kernel content, and T17 minimal-coupling content. Parametric error bounds in $R_\mathrm{cg} / L_\mathrm{flow}$ and $\ell_P / R_\mathrm{cg}$.
- **A clean closure of the INHERITED bridges in NS-2 and NS-MHD-2.** Both bridges promoted from INHERITED-at-coarse-graining-step to FORCED-via-Arc-D. Updates to NS-2.08, NS-MHD-2 §4, NS-MHD-4, and Appendix C of the NS Synthesis Paper accordingly.
- **A publishable appendix for the NS Synthesis Paper.** Appendix D: the diffusion coarse-graining theorem as a substrate-grounding addendum. Parallel in scope to Appendix C (MHD extension + ED-I-06 integration).

Once Arc D closes, the NS / MHD architectural foundation will be substrate-grounded end-to-end: substrate primitives → DCGT → canonical PDE → NS form-derivation → NS architectural classification → MHD architectural classification under ED-I-06 ontology.

---

## 8. Recommended Next Steps

After this opening memo, proceed to **Arc_D_2_Scalar_Diffusion_From_Substrate.md**. Scope: derive scalar diffusion $\partial_t\rho = \nabla\cdot(M(\rho)\nabla\rho)$ from substrate event-flux statistics. Define the cell-averaged participation density on a hydrodynamic-window cell; identify chain-step transition probabilities under V1 retarded propagation; derive the Fick's-law-class flux at substrate level via gradient expansion; identify $M(\rho)$ as the substrate-statistics quantity. Confirm form consistency with the ED canonical PDE's mobility-channel operator structure.

Estimated 1–2 sessions for Arc_D_2.

### Decisions for you

- **Confirm arc framing.** Arc D as the diffusion coarse-graining theorem closing NS-2 + NS-MHD-2 INHERITED bridges; substrate-to-continuum derivation of mobility-channel diffusion.
- **Confirm six-memo plan.** Estimated 5–7 effective sessions parallel in scope to NS-Smoothness and NS-MHD.
- **Confirm proceeding to Arc_D_2 (scalar diffusion from substrate) as the next deliverable.**

---

*Arc D opened. Diffusion Coarse-Graining Theorem (DCGT) as the substrate-to-continuum derivation of mobility-channel diffusion, closing NS-2 viscous-content and NS-MHD-2 Lorentz-coarse-graining INHERITED bridges. Six-memo plan parallel to NS-Smoothness and NS-MHD scope. Arc completes the architectural foundation for all fluid-mechanical arcs and is upstream of Hall-MHD, Yang-Mills, and ED-10 future arcs. No closed arc re-opens; no new primitives or theorems required as inputs. Arc_D_2 (scalar diffusion from substrate) is the next deliverable.*
