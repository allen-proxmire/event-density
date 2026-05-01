# NS-2.08 — ED PDE → Navier-Stokes Direct Architectural Mapping

**Date:** 2026-04-30
**Status:** Second-derivation memo for NS-2; fills the structural gap identified post-NS-3 closure. **Headline: NS is *partially* a vector-extension of the ED PDE architecture, not a literal one. The compositional rule's gradient-penalty term maps cleanly to NS's viscous μ∇²v contribution; the relational penalty maps to density-equilibrium relaxation in compressible flow; the boundary term maps to NS boundary conditions. But three NS-structural features have no clean ED PDE channel counterpart: the pressure-as-Lagrange-multiplier for incompressibility, the advective (v·∇)v convective term, and the incompressibility constraint ∇·v = 0 itself. NS is therefore best characterized as ED-architectural-in-its-viscous-content + fluid-mechanical-additions that require articulation extensions for a clean ED-canonical derivation.**
**Sources audited:** [`theory/PDE.md`](../PDE.md), [`theory/Architectural_Canon.md`](../Architectural_Canon.md), [`NS-2.07_Synthesis.md`](NS-2.07_Synthesis.md). Universal_Invariants.md referenced but not directly relevant to mapping.

---

## 1. Purpose

NS-2.08 provides a *second-derivation route* for the Navier-Stokes form, complementary to NS-2.01–NS-2.07's chain-substrate coarse-graining derivation. The route audited here is direct architectural: starting from ED's canonical PDE / compositional rule, ask whether NS is a vector-extension of the ED architecture, and if so, how the four ED-PDE channels (mobility, penalty, gradient, participation) and the compositional rule's three correction terms (relational penalty, gradient penalty, boundary) map onto NS structure.

The question is conceptually load-bearing for the program: if NS *is* a vector-extension of the ED PDE, then NS sits naturally within the canonical-ED-equation family alongside porous-medium soft matter (mobility channel), cluster-merger lensing (penalty channel), and RLC oscillation (participation channel). If NS is *not* a vector-extension — or only partially — then the chain-substrate route (NS-2.01–NS-2.07) is the operative derivation and ED's relationship to NS is structurally adjacent rather than canonical-instantiation.

The audit verdict: **NS is partially ED-architectural** (viscous content maps cleanly) **plus fluid-mechanical additions** (pressure, advection, incompressibility) that have no direct ED PDE channel counterpart. This is more honest than the user's initial intuition that NS is "a vector ED PDE" — but the partial-mapping content is real and structurally significant.

---

## 2. Inputs

| Input | Source |
|---|---|
| ED canonical scalar PDE: $\partial_t \rho = D[M(\rho)\nabla^2\rho + M'(\rho)\|\nabla\rho\|^2 - P(\rho)] + Hv$ | [`PDE.md`](../PDE.md) §1 |
| Compositional rule (cosmological specialization of A4): $p(A \cup B) = p(A) + p(B) - \alpha\int_{A\cap B} p^\gamma - \beta\int_{A \cup B} \|\nabla p\|^2 - \gamma\int_{\partial(A\cup B)} h(\|\nabla p\|)$ | [`Architectural_Canon.md`](../Architectural_Canon.md) §1 |
| Architectural principles P1–P7 | [`Architectural_Canon.md`](../Architectural_Canon.md) §2 |
| C5 (single scalar field) constraint at the canonical-PDE level | [`PDE.md`](../PDE.md) §3 |
| Four primitives: density ρ, mobility M, penalty P, participation v | [`PDE.md`](../PDE.md) §2 |
| Three channels: mobility, penalty, participation | [`PDE.md`](../PDE.md) §4 |
| NS standard form derived via chain-substrate route | [`NS-2.07_Synthesis.md`](NS-2.07_Synthesis.md) §3 |

---

## 3. Audit of C5 (Single-Scalar Constraint)

### 3.1 Two-layer structure of the canon

The architectural canon is two-layer:

- **PDE layer (PDE.md C1–C7).** Concrete instantiation of the canonical PDE on a single scalar field ρ. C5 explicitly: *"The state variable is one bounded scalar ρ ∈ [0, ρ_max] (no vector or tensor fields, no spinors)."* Forbids vector extensions at this layer.
- **Architectural layer (Architectural_Canon.md P1–P7).** Statement of architectural principles defining ED as a *class* of PDEs. The principles use ρ throughout but do not explicitly include a "scalar-only" architectural constraint analogous to C5.

The architectural canon §5 lists what cannot vary (the seven P-level principles) and what can vary (functional forms of M and P, parameter values, domain geometry, time rescaling). **It does not explicitly address whether the field type — scalar vs. vector vs. tensor — is allowed to vary.** This is a gray area in the current articulation.

### 3.2 Three readings of the C5 question

(i) **Strict reading.** C5 forbids vector extensions; the architectural canon implicitly inherits C5 because P1's operator $F[\rho]$ is stated for a scalar density field. Vector NS is not architecturally ED; the chain-substrate route (NS-2.01–NS-2.07) is the operative derivation. **No vector extension permitted.**

(ii) **Permissive reading.** The architectural canon is layer-separable from PDE.md's concrete instantiation. C5 is a *concrete-PDE* constraint, not a *P-level architectural* constraint. P1–P7 do not forbid vector or tensor extensions; they only describe scalar instantiation as the canonical case. A vector-extended ED PDE on velocity components is architecturally ED if it satisfies P1–P7 component-wise (each velocity component evolves under a P1-class operator with P2-class dual channel structure, etc.). **Vector extension permitted, conditional on each component obeying P1–P7.**

(iii) **Articulation-required reading.** The architectural canon is silent on vector/tensor extensions; neither permits nor forbids. To derive NS from the ED architecture, an explicit articulation extension would be needed — analogous to the kind of extension flagged for substrate-gravity (substrate_2pi_question) or for the diffusion-coarse-graining future arc. The extension would either ratify reading (ii) or formalize reading (i). **Vector extension under-determined.**

### 3.3 Verdict: conditionally permitted

Of the three readings, **(ii) permissive is the most defensible** under current articulation, with the caveat that explicit articulation would strengthen the case. Reasons:

- The compositional rule §1 of Architectural_Canon.md operates on configurations of micro-events with density assignment p(·). The compositional architecture is *measure-theoretic*, not field-type-specific; its three correction terms (relational, gradient, boundary) are operations on density-class quantities, not specifically on scalars.
- Architectural_Canon.md §5 explicitly lists "Domain geometry (1D, 2D, 3D; periodic / reflective / open)" as among what can vary without breaking the Canon. Generalization to vector/tensor field types is not explicitly listed, but neither is it excluded.
- The seven principles P1–P7 use ρ but their *content* (operator structure, channel complementarity, equilibrium uniqueness, mobility capacity, participation feedback, damping discriminant, triad coupling) is field-type-agnostic — these can be applied component-wise to a vector field with the principles preserved per component.

**Verdict: vector-extension of the ED PDE architecture is *conditionally permitted* under reading (ii). Strict reading (i) treats C5 as inherited at the architectural level, in which case NS is not architecturally ED. Articulation-required reading (iii) flags this as needing explicit articulation extension.**

This memo proceeds under reading (ii), with the explicit caveat that articulation extension would strengthen the result. NS-2.08 §8 includes a recommendation to produce that articulation extension as a separate memo.

---

## 4. Mapping the Four ED PDE Channels to NS Structure

### 4.1 Mobility channel

ED PDE form:
$$\nabla \cdot [M(\rho) \nabla \rho]$$

NS counterpart: viscous diffusion of velocity component $v_i$:
$$\mu \nabla^2 v_i$$

**Mapping:** apply the mobility-channel structure to each velocity component as a "density-like" field. With $M$ identified as a transport coefficient and the field as $v_i$ rather than ρ, the channel reduces to standard viscous diffusion when $M$ is constant (Newtonian fluid):
$$D \cdot \nabla \cdot [M(v_i) \nabla v_i] = \mu \nabla^2 v_i \qquad \text{(Newtonian, constant M)}.$$

For shear-rate-dependent mobility $M(|\nabla v|)$, the channel reduces to **non-Newtonian fluid behavior** — Carreau, power-law, or generalized-Newtonian classes. ED's degenerate-mobility structure with $M(\rho_\mathrm{max}) = 0$ corresponds to a *physical maximum strain rate* below which ordinary viscous behavior applies and above which mobility collapses (analog of yield-stress Bingham fluids).

**Concordance with NS-2:** the mobility channel maps to the standard Newtonian viscous term $\mu \nabla^2 v$ that NS-2.05 derived via kinetic-theory analog. Both routes give the same form. **Clean mapping.**

**Compressibility note:** in NS, mobility-channel degeneracy ($M(\rho_\mathrm{max}) = 0$) when applied to mass density ρ_fluid rather than velocity could correspond to compressibility limits (sonic speed, supersonic transitions). This is an interesting structural connection but speculative; flagged but not load-bearing.

### 4.2 Penalty channel

ED PDE form:
$$-P(\rho) \quad \text{with } P(\rho^*) = 0, \; P' > 0$$

The penalty channel restores ρ to its equilibrium $\rho^*$.

**Proposed NS counterpart:** pressure gradient $-\nabla p$.

**Honest issue with this mapping:** the ED penalty channel acts as a *restoring force on the field itself* ($-P(\rho)$ in the equation for ∂_t ρ). It pulls ρ back toward $\rho^*$ at every point. The NS pressure gradient $-\nabla p$ is **not** a restoring force on velocity; it is a *Lagrange multiplier* enforcing the incompressibility constraint $\nabla \cdot v = 0$ (in incompressible NS) or an external dynamical variable coupled to density via equation of state (in compressible NS).

The structural roles are different. The ED penalty channel produces exponential decay toward equilibrium when isolated (per PDE.md §4.2: $\rho(t) = \rho^* + (\rho_0 - \rho^*) e^{-DP_0 t}$). The NS pressure gradient produces incompressibility enforcement (in incompressible NS) or thermodynamic coupling (in compressible NS). Neither is a "decay-to-equilibrium" of velocity.

**Better mapping for compressible NS:** the penalty channel applied to *mass density* ρ_fluid (not velocity) corresponds to **density relaxation toward atmospheric / equilibrium density**. In a closed system without external forcing, the fluid eventually equilibrates to a uniform density profile. This is a real ED-penalty-class behavior in compressible NS.

**Verdict:** the penalty channel maps cleanly to **density-equilibrium relaxation in compressible NS**, not to pressure-gradient-on-velocity. The pressure-gradient is a *separate* fluid-mechanical structural feature that has no clean ED-PDE-channel counterpart. Pressure-as-Lagrange-multiplier in incompressible NS is even less ED-architectural — it is a constraint-enforcing variable, not a channel content.

### 4.3 Gradient channel (compositional rule layer)

The compositional rule's gradient-penalty term:
$$-\beta \int_{A \cup B} |\nabla p|^2 \, d\mu$$

is the configuration-space statement underlying P1's operator content $F[\rho] = M(\rho)\nabla^2 \rho + M'(\rho)|\nabla \rho|^2$ in PDE form (per Architectural_Canon.md §1: *"the compositional rule is the configuration-space statement; the PDE is its continuum-limit dynamics"*).

**NS counterpart:** the gradient-penalty content drives the smoothing of velocity gradients. In NS, $\mu \nabla^2 v$ smooths velocity gradients via viscous diffusion. The architectural source of this smoothing — gradients are penalized energetically; reducing $|\nabla v|^2$ minimizes a Dirichlet-class functional — is exactly the compositional-rule gradient-penalty content.

**Clean mapping.** $\mu \nabla^2 v$ as gradient-driven viscous diffusion *is* the gradient-penalty channel applied to velocity. This is the same mapping as §4.1 mobility-channel-to-viscous-term, viewed from the configuration-space layer rather than the PDE layer. The two layers are equivalent per Architectural_Canon.md §1.

### 4.4 Participation channel

ED PDE form:
$$\tau \dot v + \zeta v = \bar F(\rho), \quad \text{coupled back via } H \cdot v$$

Global feedback variable; produces RLC-class oscillation when isolated.

**Proposed NS counterpart:** external forcing + boundary conditions.

**Honest issue:** the ED participation channel is *integrated feedback* — it integrates $\bar F(\rho)$ over time with exponential decay and feeds back via $H \cdot v$ globally. NS's external forcing $f^\mathrm{ext}$ is typically *not* an integrated feedback; it is an externally specified field (gravity is constant; pressure boundary condition is set by environment; etc.). NS's boundary conditions are also externally specified, not integrated feedbacks.

The participation channel's *role* — supplying global / non-local content not derivable from local field structure — is analogous to the role of NS boundary conditions and external forcing. But the *mechanism* (integrated feedback with decay) is not generally what NS forcing does.

**Mapping verdict:** participation channel maps **structurally but not literally** to NS forcing/boundary content. The structural analogy is real: both supply non-local/global content to local field dynamics. The literal-form mapping fails: ED's participation is integrated feedback, NS's forcing is typically externally specified.

**Possible exception:** for self-gravitating fluids (astrophysical NS), the gravitational potential ϕ_grav from T19 is computed from the integrated mass distribution and feeds back into the velocity equation via $\rho \nabla \phi$. This is a form of integrated feedback. But it is gravity-specific, not generic to NS.

### 4.5 Boundary term (compositional rule layer)

The compositional rule's boundary term:
$$-\gamma \int_{\partial(A \cup B)} h(|\nabla p|) \, dS$$

produces horizon / holographic behavior at boundaries (per Architectural_Canon.md §1).

**NS counterpart:** NS boundary conditions on the flow domain ∂Ω. No-slip ($v = 0$ on solid walls), free-slip, periodic, inflow/outflow, etc.

**Clean mapping at structural level:** the compositional-rule boundary term enforces specific boundary behavior of the field, parallel in spirit to NS's boundary conditions. Both supply boundary-data content to the PDE.

**Less clean at functional level:** the specific functional form $h(|\nabla p|)$ in the compositional rule produces holographic-class behavior (related to T19's holographic bound and to ED-06 decoupling surfaces). Standard NS boundary conditions are simpler (Dirichlet, Neumann, etc.). The compositional-rule boundary term has more structural content than typical NS boundary conditions.

**Verdict:** structurally analogous (both supply boundary content); functionally distinct (compositional-rule boundary has holographic/horizon-class structure beyond what NS typically uses).

---

## 5. Vector-Extension Construction

Treating reading (ii) of §3 as the working framework, the vector-extended ED PDE for fluid kinematics:

### 5.1 Three coupled scalar ED PDEs (one per velocity component)

For $i \in \{x, y, z\}$:
$$\partial_t v_i = D \cdot \left[M_i(\rho_\mathrm{fluid}) \nabla^2 v_i + M_i'(\rho_\mathrm{fluid}) |\nabla v_i|^2 - P_i(v_i)\right] + H_i \cdot u_i + \mathrm{(coupling)}.$$

Each component obeys a P1-class operator on $v_i$. The constitutive functions $M_i$ depend on a shared field (mass density $\rho_\mathrm{fluid}$) — chosen this way to capture the fluid-mechanical content where viscosity $\mu$ depends on the underlying density / temperature, not on the velocity component being viscously transported.

### 5.2 Pressure as inter-component coupling

Pressure $p(x, t)$ enters the system as a *coupling term* between the three vector-extended scalar equations:
$$\partial_t v_i \supset -\frac{1}{\rho_\mathrm{fluid}} \partial_i p.$$

**This is not an ED PDE channel.** Pressure-gradient-on-velocity is a *coupling structure* added to the vector-extended ED system to enforce fluid-mechanical content (incompressibility constraint or compressible equation of state). It is required to produce NS but is not natively part of the ED architecture.

### 5.3 Advective term as kinematic coupling

The advective $(v \cdot \nabla) v_i$ term in NS — convective derivative content — is a *kinematic coupling between the three velocity components*. It arises from the fact that the velocity field both *is* the advecting flow *and* is being advected. This is a fluid-mechanical kinematic structure.

**This also is not an ED PDE channel.** The convective derivative is a structural feature of fluid flow, not derivable from the ED PDE's three channels.

### 5.4 Incompressibility constraint

The incompressibility constraint $\nabla \cdot v = 0$ (when applicable) is a *holonomic constraint* on the velocity field that is enforced by the pressure as a Lagrange multiplier. It is not derivable from any ED PDE channel; it is a fluid-mechanical commitment that must be added to make NS a closed system.

### 5.5 Aggregate vector-extended equation

Combining the vector-extended P1 operator (§5.1), the pressure coupling (§5.2), and the advective term (§5.3):

$$\partial_t v_i + (v \cdot \nabla) v_i = D \cdot \left[M(\rho)\nabla^2 v_i + \cdots \right] - \frac{1}{\rho} \partial_i p + (\mathrm{external\ forcing}).$$

For Newtonian fluid (constant $M$, identifying $D \cdot M = \nu = \mu/\rho$), this is precisely the **incompressible Navier-Stokes equation**:

$$\rho \frac{D v_i}{Dt} = -\partial_i p + \mu \nabla^2 v_i + \rho f_i^\mathrm{ext}.$$

with the constraint $\nabla \cdot v = 0$ to be enforced separately.

### 5.6 What this construction shows

The construction succeeds in producing the NS form, but with three explicit *additions* beyond the canonical ED PDE architecture:

- Pressure-coupling term (§5.2) — not native to ED PDE channels.
- Advective convective derivative (§5.3) — not native to ED PDE channels.
- Incompressibility constraint (§5.4) — not derivable from ED PDE structure.

The viscous content $\mu \nabla^2 v_i$ **does** map cleanly to the ED mobility/gradient channel (§4.1, §4.3). But the rest of NS structure is fluid-mechanical content layered on top of the ED architecture.

NS is therefore **partially ED-architectural** — its viscous content is a vector-extension of the ED mobility/gradient channel; the remaining structure (advection, pressure, incompressibility) is fluid-mechanical content not native to ED's canonical architecture.

---

## 6. Concordance with NS-2 Chain-Substrate Derivation

### 6.1 Both routes produce the same NS form

NS-2.01–NS-2.07 (chain-substrate route) derived NS via coarse-graining of substrate primitives → standard Newtonian-fluid NS form (NS-2.07 §3). NS-2.08 (this memo, ED-PDE-direct route) derived NS via vector-extension of ED PDE channels + pressure coupling + advection + incompressibility → standard NS form (§5.5).

Both routes produce $\rho Dv/Dt = -\nabla p + \mu \nabla^2 v + \rho f^\mathrm{ext}$. **Concordance confirmed.**

### 6.2 What each route explains

The two routes provide **complementary** content:

- **Chain-substrate route (NS-2.01–NS-2.07):** explains the *coefficient origin* — viscosity $\mu_\mathrm{total}$ from kinetic + V5 + V1 contributions; pressure $p_\mathrm{eff}$ from kinetic + V5 contributions; ED-specific residuals identified; values INHERITED at substrate level. Explains *where the numbers come from*.
- **ED-PDE-direct route (NS-2.08, this memo):** explains the *architectural form* — viscous content is ED's mobility/gradient channel; participation channel maps to forcing; relational and boundary terms map to fluid-mechanical structure. Identifies what's ED-architectural and what's fluid-mechanical-additive. Explains *why NS has the structure it has*.

Together, the two routes deliver NS in a way that places NS within the broader ED structural context: NS is partially an ED-class equation (its viscous content is canonical ED architecture vector-extended) plus fluid-mechanical content that extends beyond the canonical ED architecture.

### 6.3 Honest assessment of completeness

Neither route alone is complete:

- The chain-substrate route doesn't explain why NS has the *operator structure* it has; it derives NS from kinetic theory but doesn't connect to the canonical ED PDE family.
- The ED-PDE-direct route doesn't explain *coefficient values*; it identifies the architectural mapping but leaves μ, p, etc. as INHERITED.

Both routes together provide a fuller picture. The chain-substrate route is the operative derivation for empirical match; the ED-PDE-direct route is the operative derivation for structural-program-foundation.

---

## 7. Architectural Verdict

### 7.1 NS as a vector-extension of the ED PDE

**Partial.** NS is a vector-extension of the ED PDE *for its viscous content only*. The mobility/gradient channel applied component-wise to velocity gives the standard $\mu \nabla^2 v$ viscous term, with degenerate-mobility structure available for non-Newtonian fluids. **Clean mapping.**

The remaining NS structural content (pressure-coupling, advective derivative, incompressibility) is **not** a vector-extension of the ED PDE. These are fluid-mechanical-specific structural features layered on top of the ED architecture.

### 7.2 C5 status

**Conditionally permitted at the architectural P-level under reading (ii); strict at the canonical-PDE C-level.** The architectural canon (P1–P7) is field-type-agnostic in its content; C5's "single scalar field" applies to the concrete PDE.md instantiation, not necessarily to the architectural-class. Articulation extension would strengthen this.

**Recommendation:** produce a separate memo "Architectural Canon Vector-Extension" that explicitly addresses field-type generalization. Either ratify reading (ii) as canonical (vector extensions ED-architectural per-component-P1–P7) or formalize reading (i) as the binding case (vector NS structurally adjacent to but not architecturally ED).

### 7.3 Does the ED PDE architecture already implicitly contain NS structure?

**Partially.** The ED PDE architecture contains:
- Mobility/gradient channel → viscous content of NS (clean).
- Penalty channel → density-equilibrium relaxation in compressible NS (partial — penalty acts on density, not on velocity).
- Participation channel → forcing/boundary content (structural, not literal).
- Compositional rule boundary term → NS boundary conditions (clean at structural level).

The ED PDE architecture does **not** contain (i.e., requires explicit addition):
- Pressure-as-Lagrange-multiplier (incompressibility-enforcing).
- Advective convective derivative (kinematic coupling between velocity components).
- Incompressibility constraint $\nabla \cdot v = 0$.

**Net architectural verdict:** NS is *not* a literal vector-extension of the ED PDE; it is *partially ED-architectural with fluid-mechanical-specific additions*. The user's intuition was correct in pointing at the gradient-penalty/mobility/participation structure; this maps cleanly to NS's viscous content. But NS's complete structure includes additional fluid-mechanical content that has no clean ED-PDE-channel counterpart.

This is more honest than claiming "NS is a natural ED equation in the same family as porous-medium soft matter" without qualification. The viscous content of NS is in that family; the rest of NS is fluid-mechanical-specific and lies outside the canonical ED architecture.

### 7.4 Summary

**The honest aggregate:**

> *The ED canonical PDE / compositional rule architecture, applied component-wise to fluid velocity, reproduces the viscous content of Navier-Stokes ($\mu \nabla^2 v$) cleanly via the mobility/gradient channel. The pressure-coupling, advective convective derivative, and incompressibility constraint that complete the NS form are fluid-mechanical-specific structural additions not derivable from canonical ED PDE channels. NS is therefore best characterized as "partially ED-architectural with fluid-mechanical additions," not as "a literal vector-extension of the ED PDE." The viscous content is canonical ED; the rest is fluid-mechanical content that an ED-derivation must accept as additional articulation.*

This finding is structurally significant in two ways:
1. **It places NS's viscous content within the canonical ED equation family** (porous-medium, RLC, cluster-merger, viscous fluid). The same architectural mechanism that produces porous-medium spreading produces fluid viscosity.
2. **It identifies what NS adds beyond canonical ED** (pressure-coupling, advection, incompressibility). These are candidate sites for either (a) future architectural extensions to the ED canon (allowing constraint-enforcing Lagrange multipliers, kinematic cross-couplings, holonomic constraints) or (b) acceptance that some fluid-mechanical structure is not native to ED architecture and lives at a different structural layer.

---

## 8. Recommended Next Steps

In priority order.

1. **Produce the Architectural Canon Vector-Extension memo.** File: `theory/Architectural_Canon_Vector_Extension.md` (sits at `theory/` root, not in `Navier Stokes/` since it's a canon-level document). Recommended structure:
   - Statement of the C5 / P-level scalar-vs-vector ambiguity (per §3 of this memo).
   - Audit of P1–P7 for field-type-agnosticism (does each principle generalize to vector/tensor fields? Yes for P1 component-wise, P2 component-wise with shared dual-channel structure, P3 per-component, P4 per-component, P5 per-component or shared, P6 per-component, P7 per-component).
   - Formal statement of when a vector PDE is "architecturally ED" (e.g., each component obeys P1–P7 with shared constitutive functions).
   - Status of NS as partial vector-extension (per §7 of this memo): viscous content ED-architectural, other content fluid-mechanical-specific.
   - Conditions under which a vector-extension is "literal" vs. "partial" (component-wise P1–P7 obedience without additional structural content vs. with).
   This strengthens the program-level architectural canon and resolves the gray area surfaced by NS-2.08. Estimated 1–2 sessions.

2. **Refine C5 in [`PDE.md`](../PDE.md) §3** to explicitly distinguish "concrete-PDE-level C5" from "architectural-canon-level scalar/vector status." Add a one-paragraph note pointing at the new vector-extension memo. The change is: C5 currently reads as a *canonical* constraint; refine to read as a *concrete-PDE-level* constraint that is canonical for the specific PDE.md instantiation but does not bind the architectural canon. **Editorial pass; not a content change to the canon itself.**

3. **Integrate NS-2.08 into the NS-2 synthesis paper / external-facing material.** The synthesis paper recommended in NS-3.04 §9 should now be structured as **two-route concordance**: chain-substrate derivation (NS-2.01–NS-2.07) supplying coefficient values, ED-PDE-direct derivation (this memo) supplying architectural form. Both routes producing the same Newtonian-fluid NS form is itself a structural concordance result worth highlighting. Add a section to the synthesis paper draft titled "Two Routes to NS: Chain-Substrate and ED-PDE-Direct" with the §6 concordance content.

4. **Mark the three NS-architectural-additions as candidate articulation extensions.** §5.6 identifies pressure-as-Lagrange-multiplier, advective convective derivative, and incompressibility constraint as fluid-mechanical content not native to ED architecture. These are candidate sites for *future* canon extensions if the program ever needs them (e.g., for MHD, for relativistic fluid mechanics, for general-covariant fluid extensions). Recommend adding them to a "Candidate Architectural Extensions" tracking memo (file: `theory/Candidate_Architectural_Extensions.md`) for program-level tracking; not load-bearing for current work.

### Decisions for you

- **Confirm the partial-vector-extension verdict.** NS is partially ED-architectural (viscous content) plus fluid-mechanical additions (pressure, advection, incompressibility). More honest than "NS is a vector ED PDE" but less ambitious than the user's initial intuition. Structurally accurate.
- **Confirm proceeding with the Architectural Canon Vector-Extension memo as next deliverable.** Recommended; resolves the gray area and strengthens program-level canon.
- **Confirm integration into NS-2 synthesis paper** as two-route concordance. Enriches the synthesis from one derivation to two complementary derivations.
- **Confirm tracking the three architectural-extension candidates** for program-level prioritization (not immediate work).

---

*NS-2.08 closes the second-derivation gap. NS is partially ED-architectural — its viscous μ∇²v content is a clean vector-extension of the mobility/gradient channel via component-wise P1–P7 application. The pressure-coupling, advective derivative, and incompressibility constraint that complete NS form are fluid-mechanical-specific additions not native to ED PDE channels. Both NS-2's chain-substrate route and NS-2.08's ED-PDE-direct route produce the same Newtonian-fluid NS form (concordance). The two routes are complementary: chain-substrate explains coefficient values; ED-PDE-direct explains architectural form. C5 refinement and Architectural Canon Vector-Extension memo recommended as program-level cleanup.*
