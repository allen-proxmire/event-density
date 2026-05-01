# NS-MHD-2 — Lorentz Force from T17 Minimal Coupling (H2 Audit)

**Date:** 2026-04-30
**Status:** Load-bearing technical memo of the NS-MHD arc. Audits whether the fluid-level Lorentz force $\mathbf{j}\times\mathbf{B}$ derives cleanly from T17's substrate-level minimal coupling on charged chains, coarse-grained to fluid scale. **Verdict: H2 holds at form level; coarse-graining step INHERITED in parallel to NS-2.08's viscous-coarse-graining INHERITANCE; the kinematic $\mathbf{v}\times\mathbf{B}$ component is FORM-FORCED by T17 and is therefore canonical ED (not a fluid-mechanical addition).**
**Companions:** [`NS_MHD_1_Opening.md`](NS_MHD_1_Opening.md), [`../NS-2.08_ED-PDE_Direct_Mapping.md`](../NS-2.08_ED-PDE_Direct_Mapping.md), [`../../../papers/Gauge_Fields_Theorem_17/paper_gauge_fields_theorem_17.md`](../../../papers/Gauge_Fields_Theorem_17/paper_gauge_fields_theorem_17.md), [`../../Architectural_Canon_Vector_Extension.md`](../../Architectural_Canon_Vector_Extension.md).

---

## 1. The H2 Question

The arc-opening memo posed:

> **H2.** *The fluid-level Lorentz force $\mathbf{j}\times\mathbf{B}$ derives cleanly from T17's substrate-level minimal coupling on charged chains, coarse-grained to fluid scale. The Lorentz force is canonical ED, not a fluid-mechanical addition.*

This memo audits H2. The audit proceeds in four stages:

1. **Substrate-level statement.** What does T17 actually FORCE about minimal coupling at the vertex / commitment level?
2. **Single-chain reduction.** What classical equation of motion does a charged chain inherit when minimal coupling is lifted to its semiclassical limit?
3. **Coarse-graining to fluid scale.** What aggregate force density emerges from a chain population with charge density $\rho_q$ and bulk velocity $\mathbf{v}$?
4. **Architectural classification.** Does the result count as canonical ED, partial-canonical, or fluid-mechanical addition under the Architectural Canon Vector Extension framework?

The verdict is *partial-canonical with the same INHERITANCE structure as NS-2's viscous content*: the Lorentz form is FORCED by T17, the coarse-graining bridge is INHERITED, and the kinematic $\mathbf{v}\times\mathbf{B}$ component is a derived feature of the FORCED form rather than an additional fluid-mechanical commitment.

---

## 2. Substrate-Level Statement (T17 Minimal Coupling)

### 2.1 What T17 forces

T17 (GRH C3) states:

> *Commitment events are vertex-anchored; the minimal-coupling structural vertex is gauge-quotient-invariant; the vertex-quotient is the pullback of the group-quotient through coupling.*

Concretely, for a charged structural rule-type $\tau_c$ carrying gauge-group representation with charge $q$, minimal coupling FORCES the vertex-anchored commitment structure to take the form

$$\partial_\mu \;\longrightarrow\; D_\mu = \partial_\mu - iq A_\mu,$$

where $A_\mu$ is the participation measure of the gauge rule-type $\tau_g$ (T17 C1). This is the *form* of minimal coupling: the substitution is forced; the value of $q$ (and the gauge group, and the kernel parameters of $\tau_g$) is INHERITED at the value layer per T17's standard FORCED/INHERITED split.

For the $U(1)$ case (electromagnetism), $A_\mu = (\phi/c, \mathbf{A})$ and the form is the standard QED minimal coupling.

### 2.2 What T17 does *not* force

T17 does *not* directly write down a classical equation of motion. The vertex-anchored commitment structure is a participation-rate / second-quantised statement (per T17 C7 — second-quantised excitation lifting). The classical Lorentz force is a *coarse-grained / semiclassical* corollary, not a primitive of T17.

This parallels NS-2: the canonical PDE structure (mobility channel, etc.) is an architectural / form-level statement; the classical fluid equations emerge from coarse-graining a population of substrate excitations. The form is FORCED; the coarse-graining bridge is INHERITED in the standard way that the diffusion-coarse-graining theorem would supply (currently a deferred Arc D in the program).

### 2.3 Structural ingredients available

For the audit we have:

- **Form of minimal coupling.** $D_\mu = \partial_\mu - iqA_\mu$ at the vertex level (T17 C3 — FORCED).
- **Worldline structure.** $\tau_g$ excitations propagate on lightlike worldlines (T17 C5); charged $\tau_c$ excitations propagate on standard timelike worldlines under their own kinematic structure.
- **Vertex-anchored commitment.** Commitments occur at vertices where $\tau_c$ and $\tau_g$ excitations meet, with rates set by the minimal-coupling vertex (T17 C3 + C7).
- **Mobility channel for $\tau_c$.** The standard mobility channel applied to the participation measure of $\tau_c$ yields a Laplacian-class diffusion / kinematic-evolution operator parallel to the velocity-mobility channel of NS-2.08.

These ingredients suffice to audit H2 if the coarse-graining bridge is granted as INHERITED.

---

## 3. Single-Chain Reduction

### 3.1 Standard derivation of the Lorentz force from minimal coupling

The classical Lorentz force is the standard semiclassical limit of QED minimal coupling. The derivation is well-established and is not original to ED:

Starting from a charged-particle Lagrangian with minimal coupling

$$L = \tfrac{1}{2} m \mathbf{v}^2 - q\phi + q\mathbf{A}\cdot\mathbf{v},$$

the Euler-Lagrange equations yield

$$m\dot{\mathbf{v}} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B}),$$

with $\mathbf{E} = -\nabla\phi - \partial_t\mathbf{A}$ and $\mathbf{B} = \nabla\times\mathbf{A}$. The key structural fact is that the *cross-product* $\mathbf{v}\times\mathbf{B}$ emerges automatically from the velocity-coupled $q\mathbf{A}\cdot\mathbf{v}$ term in the Lagrangian when the curl of $\mathbf{A}$ is taken (specifically, from the $\nabla(\mathbf{A}\cdot\mathbf{v}) - (\mathbf{v}\cdot\nabla)\mathbf{A}$ identity).

### 3.2 What this gives us in ED

For an ED charged chain, the analogue derivation chain is:

1. T17 FORCES the form of minimal coupling: $D_\mu = \partial_\mu - iqA_\mu$.
2. The semiclassical limit of any minimally-coupled action $S = \int L\,dt$ where $L$ is built from $D_\mu\psi$ structures yields the standard $q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$ classical force on a chain excitation. This step is INHERITED from standard QED-to-classical reduction.
3. The chain's classical equation of motion under minimal coupling is therefore $m\dot{\mathbf{v}} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$.

The $\mathbf{v}\times\mathbf{B}$ structure is *not* separately committed — it is a derived consequence of the FORCED form $D_\mu = \partial_\mu - iqA_\mu$. The kinematic velocity-dependence of the magnetic-force component arises from the velocity-coupling $q\mathbf{A}\cdot\mathbf{v}$ that minimal coupling inserts at the vertex.

### 3.3 Status check: form vs. value

- *Form.* $q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$ is FORCED by T17 minimal coupling under the standard semiclassical reduction.
- *Value.* The numerical charge $q$, the chain mass $m$, and the field amplitudes $\mathbf{E}$, $\mathbf{B}$ are INHERITED at value layer (parallel to all other T17 INHERITED quantities and to the NS-2 viscosity coefficient $\mu$, which is INHERITED at fluid level).

This is *exactly* the form-FORCED / value-INHERITED split that runs throughout the ED program.

---

## 4. Coarse-Graining to Fluid Scale

### 4.1 The bridge

Take a population of charged chains with number density $n_q(\mathbf{x},t)$, charge $q$, and a velocity distribution with bulk-mean $\mathbf{v}(\mathbf{x},t)$. Define

$$\rho_q(\mathbf{x},t) = q\,n_q(\mathbf{x},t), \qquad \mathbf{j}(\mathbf{x},t) = \rho_q(\mathbf{x},t)\,\mathbf{v}(\mathbf{x},t).$$

The Lorentz force on each chain is $q(\mathbf{E} + \mathbf{v}_\mathrm{chain}\times\mathbf{B})$. Summing over the chain population per unit volume — the standard kinetic-theory bulk average — gives the force density

$$\mathbf{f}_\mathrm{Lorentz} = \rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}.$$

In the MHD limit, $\rho_q\mathbf{E}$ is suppressed at typical MHD scales (via charge quasi-neutrality), leaving

$$\mathbf{f}_\mathrm{Lorentz} \;\xrightarrow{\text{MHD}}\; \mathbf{j}\times\mathbf{B}.$$

This is the canonical Lorentz force per unit volume that appears in the MHD momentum equation (memo NS-MHD-1 §4.1 (ii)).

### 4.2 The coarse-graining step is INHERITED

The kinetic-theory averaging that takes single-chain forces to bulk force density is *not* an ED-internal derivation. It is the standard kinetic-to-fluid passage (BBGKY hierarchy / Boltzmann-to-Euler / Chapman-Enskog) that any continuum theory uses when transitioning from particle to field description.

In the ED program, this coarse-graining bridge is a deferred Arc D (diffusion-coarse-graining theorem) that would also supply the rigorous derivation of NS viscous content from chain mobility. Until Arc D closes, the coarse-graining step is INHERITED at the same status as NS-2's viscous-content coarse-graining: structurally legitimate, supported by analogy to standard physics, but not internally proven within the ED canon.

This is a clean parallel — the same INHERITANCE applies to both NS-2's viscous content and NS-MHD-2's Lorentz force. Whatever closes Arc D will close both simultaneously.

### 4.3 Status of the coarse-graining bridge

- **In NS-2:** mobility channel applied to velocity → kinematic-viscosity diffusion $\mu\nabla^2\mathbf{v}$ at fluid level. Form FORCED; coarse-graining bridge INHERITED.
- **In NS-MHD-2:** T17 minimal coupling on charged chains → fluid-level Lorentz force $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$. Form FORCED; coarse-graining bridge INHERITED in identical way.

The Lorentz force inherits the same form-FORCED / coarse-graining-INHERITED status that the NS viscous content has. They are on equal footing.

---

## 5. Architectural Classification

### 5.1 Apply the Architectural Canon Vector Extension framework

The Architectural Canon Vector Extension memo (`theory/Architectural_Canon_Vector_Extension.md`) classifies vector-field-level structural content into three tiers:

- **Tier 1 — Canonical ED.** Form FORCED by canonical channels (P1–P7) with INHERITED coarse-graining bridge (where Arc D closes).
- **Tier 2 — Partial-canonical.** Form partially forced; some structural commitment beyond canonical channels.
- **Tier 3 — Fluid-mechanical addition.** Structurally extra commitment not derivable from canonical channels.

Pure NS-2.08's classification:
- Viscous diffusion $\mu\nabla^2\mathbf{v}$ — Tier 1 (canonical ED via mobility channel).
- Advection $(\mathbf{v}\cdot\nabla)\mathbf{v}$ — Tier 3 (fluid-mechanical addition; non-ED).
- Pressure $-\nabla p$ — Tier 3 (Lagrange-multiplier for incompressibility constraint; fluid-mechanical addition).
- Incompressibility $\nabla\cdot\mathbf{v}=0$ — Tier 3 (fluid-mechanical constraint).

### 5.2 Lorentz force in this framework

The Lorentz force $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$ slots in as **Tier 1 — canonical ED**:

- Form FORCED by T17 minimal coupling (vertex-anchored commitment with $D_\mu = \partial_\mu - iqA_\mu$).
- Semiclassical reduction to classical force on charged chain is standard QED-to-classical limit (INHERITED at the same status as standard physics conventions).
- Bulk-density averaging from chain population to fluid-level force density is the same coarse-graining bridge that supplies NS-2 viscous content (INHERITED, deferred Arc D).
- No structural commitment beyond what T17 + the inherited coarse-graining bridge supply.

### 5.3 Crucial structural finding: kinematic $\mathbf{v}\times\mathbf{B}$ is FORM-FORCED

The most architecturally important point is that the *kinematic velocity-dependence* of the magnetic-force component $\mathbf{v}\times\mathbf{B}$ is **not** a separate commitment. It emerges automatically from the minimal-coupling FORM. This contrasts sharply with the kinematic velocity-dependence of advection $(\mathbf{v}\cdot\nabla)\mathbf{v}$, which is *not* derivable from any canonical ED channel and is the structural locus of NS's three-angle convergence on advection-as-non-ED.

The structural distinction:

| Term | Form forced by | Status |
|---|---|---|
| Viscous diffusion $\mu\nabla^2\mathbf{v}$ | Mobility channel (P-class — see NS-2.08) | Canonical ED |
| Magnetic diffusion $\eta\nabla^2\mathbf{B}$ | Mobility channel applied to $\mathbf{B}$ | Canonical ED (audited NS-MHD-4) |
| Advection $(\mathbf{v}\cdot\nabla)\mathbf{v}$ | *No canonical channel* | Fluid-mechanical addition |
| Lorentz force $\mathbf{j}\times\mathbf{B}$ | T17 minimal coupling | **Canonical ED** |

The Lorentz force is structurally on the same side of the canon as viscous and magnetic diffusion. Advection alone occupies the fluid-mechanical-addition position in the momentum equation.

---

## 6. Verdict on H2

**H2 holds.** The fluid-level Lorentz force $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$ is canonical ED, with the same FORCED-form / INHERITED-coarse-graining status as NS-2's viscous content. The kinematic $\mathbf{v}\times\mathbf{B}$ component is a derived feature of the FORCED minimal-coupling form, not an extra fluid-mechanical commitment.

**Qualifications.**

- *Coarse-graining bridge.* The single-chain → fluid-density averaging step is INHERITED in the same way that NS-2's viscous-content coarse-graining is INHERITED. Both await Arc D closure for full ED-internal status. Until then, both are at INHERITED status, not canon-FORCED at the coarse-graining step.
- *Value-layer inheritance.* All numerical values (charge $q$, gauge group, field amplitudes, conductivity $\sigma$) are INHERITED at value layer per T17's standard FORCED/INHERITED split. The arc audits architectural form only.
- *Quasi-neutrality assumption.* The MHD-limit suppression of $\rho_q\mathbf{E}$ relative to $\mathbf{j}\times\mathbf{B}$ is a fluid-mechanical assumption (charge quasi-neutrality at MHD scales). This assumption is itself a fluid-mechanical commitment, but it is on the *applicability* of MHD as a regime, not on the canonical form of the underlying coupling.

### 6.1 Implication for the arc

If H2 holds, the architectural decomposition of MHD is structurally cleaner than that of pure NS:

- *Pure NS:* viscous content canonical ED (1 of 4 momentum-equation features); 3 of 4 are fluid-mechanical additions (advection, pressure, incompressibility).
- *MHD addition (NS → MHD):* magnetic diffusion canonical ED, Maxwell field structure canonical ED via T17, Lorentz force canonical ED via T17 minimal coupling. **All EM-related additions to NS turn out canonical ED.** The MHD upgrade does not add new fluid-mechanical commitments to the momentum equation.
- *Remaining MHD-specific fluid-mechanical content:* the induction-equation kinematic term $\nabla\times(\mathbf{v}\times\mathbf{B})$ and the Ohm's-law $\mathbf{v}\times\mathbf{B}$ piece are auditable for non-ED status in NS-MHD-3 (likely H3 holds, parallel to advection).

The aggregate picture: MHD's *new* content (relative to pure NS) is largely canonical ED. The fluid-mechanical-addition catalogue for MHD is essentially: pure-NS additions (advection, pressure, incompressibility) plus possibly the induction-equation kinematic term plus possibly the Ohm $\mathbf{v}\times\mathbf{B}$ term — all of them *kinematic velocity-dependent couplings between two physical fields*, structurally a single class.

### 6.2 The kinematic-coupling pattern

The deepest structural finding visible at this stage is the emerging *kinematic-coupling pattern*: every fluid-mechanical addition catalogued so far in the NS / MHD program is a velocity-dependent coupling between two physical fields, with the velocity field appearing in a non-canonical-ED operator structure:

| Term | Coupling structure |
|---|---|
| Advection $(\mathbf{v}\cdot\nabla)\mathbf{v}$ | $\mathbf{v}$ couples to $\mathbf{v}$ via directional derivative |
| Induction kinematic $\nabla\times(\mathbf{v}\times\mathbf{B})$ | $\mathbf{v}$ couples to $\mathbf{B}$ via cross-product + curl |
| Ohm kinematic $\mathbf{v}\times\mathbf{B}$ | $\mathbf{v}$ couples to $\mathbf{B}$ via cross-product |

In contrast, the Lorentz $\mathbf{v}\times\mathbf{B}$ that *appears* in the same family is FORCED by T17's minimal-coupling form because the velocity dependence enters via the gauge-coupling Lagrangian $q\mathbf{A}\cdot\mathbf{v}$ — the velocity is the participation measure of the *charged* rule-type, and the cross-product is forced by the gauge-quotient identification.

The structural distinction is that minimal-coupling-derived velocity-dependence (Lorentz) is canonical ED via T17, while *advective* / *kinematic-transport* velocity-dependence (advection, induction kinematic, Ohm $\mathbf{v}\times\mathbf{B}$) is fluid-mechanical specific.

This is an architecturally important clarification: not all kinematic velocity-dependent terms have the same status. Only the ones derivable from minimal coupling are canonical.

---

## 7. Summary

- **H2 verdict: holds.** Lorentz force $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$ is canonical ED via T17 minimal coupling; FORCED at form level; coarse-graining bridge INHERITED in parallel to NS-2 viscous content.
- The kinematic $\mathbf{v}\times\mathbf{B}$ component is a derived feature of T17 minimal coupling, *not* a separate fluid-mechanical commitment.
- The MHD architectural picture under H2 + (likely) H3 + H1: all *EM-side* additions to NS are canonical ED; only *kinematic-transport* couplings (advection, induction kinematic, Ohm kinematic) remain as fluid-mechanical-additions.
- Working architectural classification: minimal-coupling-derived velocity-dependence is canonical; transport-kinematic velocity-dependence is non-ED. This refines the kinematic-coupling pattern and is the load-bearing structural finding so far in the NS-MHD arc.

---

## 8. Recommended Next Steps

1. **Proceed to NS-MHD-3 (Induction Equation Analysis).** File: `theory/Navier Stokes/MHD/NS_MHD_3_Induction.md`. Audit H3: is $\nabla\times(\mathbf{v}\times\mathbf{B})$ a fluid-mechanical addition parallel to advection? Apply three-angle convergence (architectural / dynamical / spectral) framework. Confirm magnetic diffusion $\eta\nabla^2\mathbf{B}$ as canonical ED (preview of NS-MHD-4).

2. **Document the kinematic-coupling pattern refinement.** The distinction between *minimal-coupling-derived* velocity-dependence (canonical) and *transport-kinematic* velocity-dependence (non-ED) should be carried forward as a structural insight into NS-MHD-5 synthesis.

### Decisions for you

- **Confirm H2 verdict.** Lorentz force canonical ED via T17 minimal coupling; FORCED form, INHERITED coarse-graining; structurally cleaner than pure-NS picture.
- **Confirm proceeding to NS-MHD-3 (induction equation H3 audit).**
- **Confirm carrying the kinematic-coupling-pattern refinement forward.** Minimal-coupling velocity-dependence vs. transport-kinematic velocity-dependence is the structural distinction; the latter alone is fluid-mechanical-specific.

---

*NS-MHD-2 H2 audit closed. Lorentz force $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$ is FORCED-form canonical ED via T17 minimal coupling; coarse-graining bridge INHERITED in parallel to NS-2 viscous content. The MHD upgrade (NS → MHD) adds only canonical ED content on the EM side: magnetic diffusion (mobility channel on $\mathbf{B}$), Maxwell structure (T17 directly), Lorentz force (T17 minimal coupling). The fluid-mechanical-addition catalogue for MHD is the pure-NS catalogue (advection, pressure, incompressibility) plus the kinematic-transport couplings of the induction equation and Ohm's law (likely H3 holds). Kinematic-coupling-pattern refinement: minimal-coupling-derived velocity-dependence is canonical; transport-kinematic velocity-dependence is fluid-mechanical-specific. NS-MHD-3 is the next deliverable.*
