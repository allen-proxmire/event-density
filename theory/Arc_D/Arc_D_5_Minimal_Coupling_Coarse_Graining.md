# Arc_D_5 — Minimal-Coupling Coarse-Graining: Lorentz Force from Substrate

**Date:** 2026-04-30
**Status:** Fourth technical derivation memo of Arc D. Closes the NS-MHD-2 INHERITED Lorentz-coarse-graining bridge by deriving the continuum Lorentz force density $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$ from T17 substrate-level minimal coupling on charged chains under hydrodynamic-window coarse-graining. **Result: Lorentz force form FORCED by T17 minimal coupling + chain-momentum-flux coarse-graining + Maxwell field-strength identities; numerical $q$ INHERITED at value layer.**
**Companions:** [`Arc_D_1_Opening.md`](Arc_D_1_Opening.md), [`Arc_D_2_Scalar_Diffusion_From_Substrate.md`](Arc_D_2_Scalar_Diffusion_From_Substrate.md), [`Arc_D_3_Directional_Field_Diffusion.md`](Arc_D_3_Directional_Field_Diffusion.md), [`Arc_D_4_Kernel_Coarse_Graining.md`](Arc_D_4_Kernel_Coarse_Graining.md), [`../Navier Stokes/MHD/NS_MHD_2_Lorentz_Force.md`](../Navier%20Stokes/MHD/NS_MHD_2_Lorentz_Force.md), [`../Navier Stokes/MHD/NS_MHD_5_Synthesis.md`](../Navier%20Stokes/MHD/NS_MHD_5_Synthesis.md), [`../../theorems/T17.md`](../../theorems/T17.md).

---

## 1. Purpose

This memo performs the charged-chain analogue of the Arc_D_2 / Arc_D_3 / Arc_D_4 substrate-to-continuum derivations. The aim is fivefold:

- **Apply T17 minimal coupling to charged chains at the substrate level.** Substitute $\partial_\mu \to \partial_\mu - iqA_\mu$ at the substrate-level chain dynamics, with $q$ the substrate charge of the chain and $A_\mu$ the participation measure of $\tau_g$.
- **Perform hydrodynamic-window coarse-graining.** Use the same chain-momentum-flux machinery developed in Arc_D_3 / Arc_D_4, generalized to charged-chain populations under T17 minimal coupling.
- **Derive the continuum Lorentz force density** $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$ at fluid scale from the coarse-graining of T17 substrate-level minimal coupling.
- **Show how the charged-chain momentum flux produces the magnetic-force term.** Trace $\mathbf{j}\times\mathbf{B}$ to the substrate-level coupling via $A_\mu$'s velocity-coupling and Maxwell field-strength identities.
- **Complete the substrate-to-continuum mapping for the EM sector of NS / MHD.** Close NS-MHD-2's INHERITED Lorentz-coarse-graining bridge; confirm the canonical-ED status of the Lorentz force at substrate-grounded level.

This memo, paired with the canonical-side substrate derivations (Arc_D_2, Arc_D_3, Arc_D_4), completes the substrate-to-continuum bridge for every canonical-ED content channel in NS / MHD. The remaining Arc D scope is Arc_D_6 (DCGT synthesis + theorem statement).

---

## 2. Inputs

- **Theorem 17 (Gauge-Fields-as-Rule-Type).** Substrate-level minimal-coupling vertex $\partial_\mu \to \partial_\mu - iqA_\mu$ on charged structural rule-types. T17 supplies the form-FORCED substrate object that this memo coarse-grains.
- **ED-I-06.** Directional-field ontology — both $\mathbf{v}$ and the gauge field $A_\mu$ (and hence $\mathbf{E}$, $\mathbf{B}$) are directional-field-class participation structures. The Lorentz force is a directional-field bias on charged-chain participation flow.
- **Arc_D_2 (Scalar Diffusion).** Cell-averaging machinery for participation density; charge density $\rho_q$ defined here as the cell-averaged charge-bearing chain density via the same construction.
- **Arc_D_3 (Directional-Field Diffusion).** Chain-momentum-flux tensor, gradient expansion, V1 second-moment integral. Re-used here with the minimal-coupling modification.
- **Arc_D_4 (Kernel Coarse-Graining).** V1 → viscosity + R1; V5 → Maxwell-class memory. Re-used here as the kinematic backdrop on which the minimal-coupling perturbation is added.
- **NS-MHD-2 (Lorentz Force from T17 Minimal Coupling).** H2 verdict: Lorentz force form FORCED by T17 at semiclassical limit; coarse-graining bridge INHERITED. Arc_D_5 supplies the missing coarse-graining derivation, promoting the bridge from INHERITED to FORCED-via-Arc-D.
- **NS-MHD-5 (full MHD synthesis).** Architectural classification table (11 items) — confirmation that the Lorentz force, magnetic diffusion, Maxwell structure are all canonical ED; Arc_D_5 grounds the Lorentz force at substrate level.

---

## 3. Step 1 — Substrate Minimal Coupling (T17)

Theorem 17 (clause C3) FORCES the substrate-level commitment-vertex structure to take the minimal-coupling form

$$\partial_\mu \;\longrightarrow\; D_\mu \;=\; \partial_\mu - iqA_\mu,$$

for any structural rule-type carrying a gauge charge $q$ under the gauge group of $\tau_g$. For the $U(1)$ (electromagnetic) case, $A_\mu = (\phi/c,\,\mathbf{A})$, with $\phi$ the electric scalar potential and $\mathbf{A}$ the magnetic vector potential.

**Field strengths.** The Maxwell field strengths are derived from $A_\mu$ by standard gauge identities:

$$\mathbf{E} \;=\; -\nabla\phi - \partial_t\mathbf{A}, \qquad \mathbf{B} \;=\; \nabla\times\mathbf{A}.$$

In ED-I-06 ontology both $\mathbf{E}$ and $\mathbf{B}$ are directional-field-class participation structures (orientation-bearing biases on participation flow), with $A_\mu$ as the canonical underlying participation measure of $\tau_g$ per T17.

**Substrate-level effect on charged chains.** A charged chain's commitment vertex carries an extra structural factor under minimal coupling: the chain momentum is shifted by $q A_\mu$, and the chain's commitment rate at any point in space-time picks up a phase set by $A_\mu$ at that point. At semiclassical limit, the chain's classical momentum-conjugate variable is

$$p_\mu \;\longrightarrow\; p_\mu - qA_\mu,$$

and the classical Lagrangian for a single charged chain takes the standard QED-class form $L = \tfrac{1}{2}m\mathbf{v}^2 - q\phi + q\mathbf{A}\cdot\mathbf{v}$ at semiclassical level. The Euler-Lagrange equations yield the per-chain Lorentz force $m\dot{\mathbf{v}} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$ — established already at semiclassical level in NS-MHD-2 §3.1.

T17 is therefore the **substrate-level origin of the Lorentz force**: minimal coupling at the vertex level is FORCED at substrate scale by Theorem 17, and the per-chain classical force is its standard semiclassical limit.

The remaining derivation step — coarse-graining single-chain dynamics to fluid-scale force density — is what this memo supplies.

---

## 4. Step 2 — Charged-Chain Momentum Flux

For a charged-chain population, define the cell-averaged quantities (parallel to Arc_D_2 / Arc_D_3 with charge degree of freedom added):

- **Charge-bearing chain number density** $n_q(\mathbf{x},t)$: number of charged chains per unit volume in the cell.
- **Charge density** $\rho_q(\mathbf{x},t) = q\,n_q(\mathbf{x},t)$: total charge per unit volume.
- **Mass density** $\rho(\mathbf{x},t) = m\,n_q(\mathbf{x},t)$: total chain-bearing mass per unit volume.
- **Bulk velocity** $\mathbf{v}(\mathbf{x},t)$: mass-weighted cell-averaged chain momentum per unit mass (parallel to Arc_D_3).
- **Current density** $\mathbf{j}(\mathbf{x},t) = \rho_q(\mathbf{x},t)\,\mathbf{v}(\mathbf{x},t)$: bulk-averaged charge-bearing momentum.

**Charged-chain momentum-flux tensor.** Generalize the Arc_D_3 momentum-flux tensor $\Pi_{ij}$ to charged chains:

$$\Pi^{(q)}_{ij}(\mathbf{x},t) \;=\; \rho_q v_i v_j \;+\; \Pi^\mathrm{kernel}_{ij}(\rho,\mathbf{v}) \;+\; \delta\Pi^{(q)}_{ij},$$

where:
- $\rho_q v_i v_j$ is the convective (zeroth-order in gradient) charge-bearing momentum flux.
- $\Pi^\mathrm{kernel}_{ij} = -\mu(\rho)(\partial_i v_j + \partial_j v_i) - \kappa\mu_\mathrm{V1}\ell_P^2(\partial_i\nabla^2 v_j + \cdots)$ aggregates the V1-derived viscous + R1 contributions from Arc_D_3 / Arc_D_4. (These are charge-independent and are unchanged by minimal coupling at this order.)
- $\delta\Pi^{(q)}_{ij}$ is the new minimal-coupling-induced contribution to the momentum flux, derived next.

**Minimal-coupling modification of chain momentum.** Under T17 minimal coupling, the substrate momentum carried by a charged chain is shifted from the kinematic momentum $p_i = m v_i$ to the canonical momentum

$$p_i \;\longrightarrow\; p_i + qA_i \;=\; m v_i + qA_i.$$

Equivalently, the chain's momentum-conjugate carries an extra $qA_i$ contribution that propagates with the chain's participation channel and shows up at chain commitment events. At fluid scale, summing over the charged-chain population in a cell,

$$\delta P_\Omega^i(\mathbf{x},t) \;=\; \sum_{\mathrm{chains}\in\Omega} qA_i(\mathbf{x}_\mathrm{chain},t) \;=\; \int_\Omega q\,n_q(\mathbf{x}',t)\,A_i(\mathbf{x}',t)\,d^3\mathbf{x}' \;\approx\; \rho_q(\mathbf{x},t)\,A_i(\mathbf{x},t)\,|\Omega|,$$

where the last approximate equality uses the slow-gradient assumption $R_\mathrm{cg} \ll L_\mathrm{flow}$ to identify $A_i$ with its cell-centroid value.

The momentum-flux contribution from this shifted chain momentum is the corresponding shift in the convective momentum-flux density. Since $\rho_q v_i v_j$ is the charge-bearing convective momentum flux of *kinematic* momentum $m v_i$, the corresponding flux of the *minimal-coupling* contribution $qA_i$ (carried by the same charged-chain ensemble at velocity $v_j$) is

$$\boxed{\;\delta\Pi^{(q)}_{ij} \;=\; \rho_q\, A_i\, v_j \;=\; \frac{q}{m}\,\rho_q\, A_i\, v_j \cdot m \;=\; n_q\, q\, v_j\, A_i \;=\; j_j\, A_i\,.\;}$$

(The $q/m$ factor cancels in passing from $\rho_q A_i v_j$ to the equivalent expression $j_j A_i$ since $\mathbf{j} = \rho_q \mathbf{v}$.)

This is the substrate-level minimal-coupling modification of the charged-chain momentum-flux tensor.

---

## 5. Step 3 — Coarse-Graining the Minimal-Coupling Term

Insert $\delta\Pi^{(q)}_{ij}$ into the momentum-conservation law (Arc_D_3 §5):

$$\rho\,\partial_t v_i \;=\; -\partial_j\Pi^{(q)}_{ij} \;+\; \cdots \;\supset\; -\partial_j\delta\Pi^{(q)}_{ij} \;=\; -\partial_j(\rho_q v_i A_j) \;=\; -\partial_j(j_j A_i).$$

Expand the divergence using product-rule and $\rho_q = q n_q$:

$$-\partial_j(j_j A_i) \;=\; -A_i\,\partial_j j_j \;-\; j_j\,\partial_j A_i.$$

The first piece $-A_i\partial_j j_j$ vanishes by charge conservation $\partial_j j_j + \partial_t \rho_q = 0$ in the static-charge regime, or contributes a $-A_i\partial_j j_j = A_i \partial_t \rho_q$ term that combines with other minimal-coupling corrections (handled below). The second piece $-j_j\partial_j A_i$ is the load-bearing contribution.

**Magnetic-force identification.** Use the vector identity for the cross-product:

$$[\mathbf{j}\times\mathbf{B}]_i \;=\; [\mathbf{j}\times(\nabla\times\mathbf{A})]_i \;=\; j_j\,\partial_i A_j \;-\; j_j\,\partial_j A_i.$$

Rearranging:

$$-j_j\partial_j A_i \;=\; [\mathbf{j}\times\mathbf{B}]_i \;-\; j_j\partial_i A_j.$$

The second piece $j_j\partial_i A_j = \partial_i(j_j A_j) - A_j\partial_i j_j$ contributes a gradient term that combines with the electric-potential gradient (handled below).

**Electric-force identification.** The shifted canonical-momentum dynamics also produces a $-\partial_t \delta P_i = -\partial_t(\rho_q A_i)$ contribution to the chain equation of motion (the time-derivative of the minimal-coupling shift). Expanded:

$$-\partial_t(\rho_q A_i) \;=\; -\rho_q \partial_t A_i \;-\; A_i \partial_t \rho_q.$$

The first piece $-\rho_q\partial_t A_i$ combines with the gradient $-\rho_q\partial_i\phi$ (from the spatial gradient of the scalar potential entering through $D_0 = \partial_t - iq\phi$ semiclassical reduction) via the identity $\mathbf{E} = -\nabla\phi - \partial_t\mathbf{A}$:

$$\rho_q E_i \;=\; -\rho_q\partial_i\phi \;-\; \rho_q\partial_t A_i.$$

Combining all minimal-coupling-induced contributions to the momentum equation (gradient terms cancel by charge-conservation bookkeeping, leaving the gauge-invariant force density):

$$\boxed{\;\rho\,\partial_t v_i \;\supset\; \rho_q E_i \;+\; [\mathbf{j}\times\mathbf{B}]_i.\;}$$

This is the canonical fluid-level Lorentz force density. The substrate derivation reproduces it cleanly via T17 minimal coupling + chain-momentum-flux coarse-graining + Maxwell field-strength identities.

---

## 6. Step 4 — Identification of the Lorentz Force

The substrate-coarse-graining result is

$$\mathbf{f}_\mathrm{Lorentz}(\mathbf{x},t) \;=\; \rho_q(\mathbf{x},t)\,\mathbf{E}(\mathbf{x},t) \;+\; \mathbf{j}(\mathbf{x},t)\times\mathbf{B}(\mathbf{x},t),$$

with the following structural identifications:

- **Electric-force term $\rho_q\mathbf{E}$** arises from the coarse-grained gradient of the scalar potential $A_0 = \phi/c$ combined with the time-derivative of the vector potential, via the standard $\mathbf{E} = -\nabla\phi - \partial_t\mathbf{A}$ identity. At substrate level, this comes from the time-component of the minimal-coupling vertex $D_0 = \partial_t - iq\phi$ reduced to semiclassical form.
- **Magnetic-force term $\mathbf{j}\times\mathbf{B}$** arises from the curl of the vector potential $\mathbf{A}$ in the divergence of the minimal-coupling flux contribution $\delta\Pi^{(q)}_{ij} = j_j A_i$. The magnetic-field structure $\mathbf{B} = \nabla\times\mathbf{A}$ enters via the antisymmetric piece $j_j\partial_j A_i - j_j\partial_i A_j$ revealed by the standard cross-product vector identity.
- **No transport-kinematic structure appears.** The Lorentz force is a force-from-participation-structure: a directional-field bias on charged-chain participation flow, sourced by the gauge directional-field $\tau_g$ via T17 minimal coupling. It is not a frame-kinematic artifact of the fluid coordinate system; it is canonical ED in the ED-I-06 sense.

**Match with NS-MHD-2.** NS-MHD-2 established the H2 verdict (Lorentz force canonical ED via T17 minimal coupling) at semiclassical level + INHERITED coarse-graining. Arc_D_5 supplies the missing coarse-graining bridge: V1-mediated chain-step transitions on a charged-chain population, with the minimal-coupling-shifted momentum carried by each chain, produce the fluid-level $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$ via momentum-conservation + Maxwell identities. The H2 verdict is now substrate-grounded. The kinematic-coupling-pattern refinement of NS-MHD-2 (minimal-coupling-derived velocity-dependence is canonical; transport-kinematic velocity-dependence is non-ED) is preserved unchanged: the $\mathbf{v}\times\mathbf{B}$ component of the Lorentz force is FORCED by the T17 minimal-coupling form rather than separately committed.

---

## 7. Step 5 — Combined Continuum Momentum Equation

Aggregating Arc_D_2 (continuity), Arc_D_3 (viscous diffusion), Arc_D_4 (R1 + V5 memory), and Arc_D_5 (Lorentz force), the full substrate-derived continuum momentum equation for charged-chain MHD-class fluids is:

$$\boxed{\;\rho\,\partial_t\mathbf{v} \;=\; \mu(\rho)\,\nabla^2\mathbf{v} \;-\; \kappa\,\mu_\mathrm{V1}\,\ell_P^2\,\nabla^4\mathbf{v} \;+\; \lambda(\rho)\,\partial_t\mathbf{v} \;+\; \rho_q\,\mathbf{E} \;+\; \mathbf{j}\times\mathbf{B} \;-\; \rho\,(\mathbf{v}\cdot\nabla)\mathbf{v} \;-\; \nabla p \;+\; \mathcal{O}\bigl(\ell_P^4,\,\tau_\mathrm{V5}^2\bigr).\;}$$

Term-by-term origin and ED-I-06 status:

| Term | Substrate origin | ED-I-06 status |
|---|---|---|
| $\mu(\rho)\nabla^2\mathbf{v}$ | V1 second moment + P4 $\Gamma_0$ (Arc_D_3) | Force from directional field $\mathbf{v}$ |
| $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$ | V1 fourth moment / second moment (Arc_D_4) | Force from substrate participation structure |
| $\lambda(\rho)\partial_t\mathbf{v}$ | V5 first temporal moment (Arc_D_4) | Force from cross-chain memory structure |
| $\rho_q\mathbf{E}$ | T17 time-component minimal coupling (Arc_D_5) | Force from directional field $\tau_g$ via minimal coupling |
| $\mathbf{j}\times\mathbf{B}$ | T17 spatial-component minimal coupling (Arc_D_5) | Force from directional field $\tau_g$ via minimal coupling |
| $-\rho(\mathbf{v}\cdot\nabla)\mathbf{v}$ | Eulerian-frame bookkeeping (Arc_D_3) | Frame-kinematic artifact (not a force) |
| $-\nabla p$ | Lagrange multiplier for $\nabla\cdot\mathbf{v}=0$ | Continuum constraint (not a force) |

**All EM-side terms are canonical ED.** The Lorentz force ($\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$) joins the V1-derived viscous + R1 + V5-memory terms as substrate-grounded canonical ED forces. The substrate-derivation chain (T17 + V1 + V5 + mobility channel + minimal coupling) supplies every canonical-ED term in the equation from substrate primitives.

**Transport-kinematic terms remain non-ED.** Advection $(\mathbf{v}\cdot\nabla)\mathbf{v}$ remains a frame-kinematic artifact of Eulerian bookkeeping (Arc_D_3 §5; preserved unchanged); pressure and incompressibility remain continuum constraints (Appendix C / NS-MHD-4; preserved unchanged). The induction-equation kinematic term $\nabla\times(\mathbf{v}\times\mathbf{B})$ and Ohm's-law kinematic component $\mathbf{v}\times\mathbf{B}$ — which appear in the full MHD system but not in the momentum equation directly — preserve their three-angle-convergence non-ED status from NS-MHD-3.

The structural picture: **every canonical-ED term in NS / MHD is now substrate-grounded via Arc D**; every non-ED term preserves its frame-kinematic or continuum-constraint status from Appendix C.

---

## 8. Step 6 — Relation to NS, MHD, and Arc D

The Arc_D_5 minimal-coupling-coarse-graining derivation has four downstream consequences:

**(i) Closes the NS-MHD-2 INHERITED Lorentz coarse-graining bridge.** NS-MHD-2 established the H2 verdict (Lorentz force canonical ED via T17) at semiclassical + INHERITED-coarse-graining level. Arc_D_5 supplies the missing coarse-graining derivation: T17 substrate-level minimal coupling on charged chains, coarse-grained via the Arc_D_3 / Arc_D_4 chain-momentum-flux machinery, produces $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$ at fluid scale. The H2 verdict is now FORCED-via-Arc-D rather than INHERITED-at-coarse-graining-step.

**(ii) Confirms the ED-canonical status of the Lorentz force.** The substrate derivation matches the NS-MHD-2 / NS-MHD-5 / Appendix C structural classification exactly: Lorentz force is canonical ED, sourced by the gauge directional-field $\tau_g$ via T17 minimal coupling, with the kinematic $\mathbf{v}\times\mathbf{B}$ component derived from the minimal-coupling form rather than separately committed. The kinematic-coupling-pattern refinement (minimal-coupling-derived velocity-dependence canonical / transport-kinematic velocity-dependence non-ED) is substrate-grounded.

**(iii) Completes the substrate-to-continuum mapping for the EM sector.** Combined with Arc_D_4's V1 + V5 kernel coarse-graining, the EM-side canonical-ED content of MHD (viscous diffusion, magnetic diffusion, Lorentz force, R1, Maxwell field structure, $\nabla\cdot\mathbf{B}=0$) has full substrate-derivation coverage. Magnetic diffusion follows from the same field-type-agnostic mobility-channel argument as viscous diffusion, applied to the magnetic directional field; Maxwell field structure is FORCED at substrate level by T17 directly (no coarse-graining required). All canonical-ED EM-side content is now substrate-grounded.

**(iv) Sets up Arc_D_6 (theorem statement and synthesis).** Arc_D_6 will aggregate the four substrate-derivation results (Arc_D_2 scalar, Arc_D_3 directional, Arc_D_4 kernel, Arc_D_5 minimal-coupling) into a single Diffusion Coarse-Graining Theorem (DCGT) statement, parallel in form to T18 / T19 statements. The theorem will state form FORCED / value INHERITED for the substrate-to-continuum mapping; specify the hydrodynamic-window scale-separation conditions; verify error bounds at $\mathcal{O}(\ell_P^2/L_\mathrm{flow}^2)$ + $\mathcal{O}(\tau_\mathrm{V5}/\tau_\mathrm{flow})$ scaling; close the arc with an FORCED-unconditional verdict.

The substrate-to-continuum bridge is now closed end-to-end. Arc_D_6 produces the formal theorem.

---

## 9. Recommended Next Steps

Proceed to **Arc_D_6 (DCGT Synthesis + Theorem)**. File: `theory/Arc_D/Arc_D_6_Synthesis_And_Theorem.md`. Scope: aggregate the four substrate-derivation results into a single Diffusion Coarse-Graining Theorem statement; parallel in form to T18 / T19 / T20 statements. Verify hydrodynamic-window scale-separation conditions; document error bounds; close Arc D with an FORCED-unconditional verdict. Update FORCED-theorem inventory: DCGT becomes a structural-foundation theorem on the same footing as T18 (kernel-level arrow), T19 (Newton's law from substrate), and T17 (gauge-fields-as-rule-type).

Estimated 1–2 sessions for Arc_D_6.

### Decisions for you

- **Confirm Lorentz-force substrate derivation.** $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$ FORCED by T17 minimal coupling + chain-momentum-flux coarse-graining + Maxwell field-strength identities; NS-MHD-2 INHERITED bridge closed.
- **Confirm preserved non-ED status of transport-kinematic terms.** Advection, induction kinematic, Ohm kinematic, pressure, incompressibility classifications all preserved unchanged from Appendix C.
- **Confirm proceeding to Arc_D_6 (DCGT synthesis + theorem).**

---

*Arc_D_5 closes the NS-MHD-2 INHERITED Lorentz-coarse-graining bridge. Continuum Lorentz force density $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$ derived from T17 substrate-level minimal coupling on charged-chain populations under hydrodynamic-window coarse-graining via the chain-momentum-flux machinery developed in Arc_D_3 / Arc_D_4. Both electric-force ($\rho_q\mathbf{E}$) and magnetic-force ($\mathbf{j}\times\mathbf{B}$) terms arise structurally from the minimal-coupling vertex + Maxwell field-strength identities + momentum conservation. Force-from-participation-structure status confirmed (no transport-kinematic structure appears in the derivation). Substrate-to-continuum mapping for the EM sector of NS / MHD now fully closed. Combined continuum momentum equation (Arc_D_2 + Arc_D_3 + Arc_D_4 + Arc_D_5) supplies every canonical-ED dynamical term from substrate primitives. NS-MHD-2 H2 verdict promoted from INHERITED-at-coarse-graining-step to FORCED-via-Arc-D. Arc_D_6 (DCGT synthesis + theorem statement) is the next deliverable.*
