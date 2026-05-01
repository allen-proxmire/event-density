# Appendix C — MHD Extension and ED-I-06 Ontological Integration

*Companion appendix to* The Architectural Foundations of Navier-Stokes in Event Density: Form Derivation, Clay-Relevance Decomposition, and the Structural Status of Turbulence.

---

## C.1 Purpose

This appendix extends the architectural account of the main paper in two complementary directions.

First, it extends the NS architectural classification (Sections §3–§6 of the main paper) to **incompressible magnetohydrodynamics (MHD)**, the canonical theory of electrically conducting fluids that couples Navier-Stokes to Maxwell's equations through Ohm's law and the induction equation. The appendix shows that the canonical / non-canonical boundary established for pure NS generalizes cleanly to MHD, with two structural refinements: every electromagnetic-side addition introduced by the MHD upgrade is ED-canonical, and the new fluid-mechanical-specific structural commitments (induction-equation kinematic term, Ohm's-law kinematic component) belong to a single transport-kinematic class shared with NS advection.

Second, it integrates the **ED-I-06 *Fields and Forces* ontology** (Proxmire, *Fields and Forces in Event Density*, 2026) as the conceptual framework that explains *why* the canonical / non-canonical boundary lives where it does. The ED-I-06 ontology supplies a forces-vs-frame-kinematic reading under which the structural classifications of NS-2.08, NS-Smoothness, NS-Turbulence, and the MHD arc all read as instances of a single ontological distinction.

The appendix delivers a final architectural classification table covering all eleven content items of the standard incompressible MHD system, with both structural and ontological status indicated for each. The main results of the NS Synthesis Paper remain unchanged; the ontological integration provides ED-I-06-grounded framing for those results without revising any technical conclusion.

---

## C.2 ED-I-06 Ontology: Forces, Fields, and Participation Structures

ED-I-06 reframes fields and forces in terms of stable participation structures. Three structural classes of field-like participation arise naturally from the internal organization of participation channels:

- **Directional fields** — channels with a preferred orientation. ED-I-06 cites magnetic structure, spin textures, and *vorticity-like fluid structures* explicitly (§3). In the NS / MHD context, the velocity field $\mathbf{v}$, the vorticity $\boldsymbol{\omega}$, the magnetic field $\mathbf{B}$, and the gauge field $A_\mu$ (formalized as $\tau_g$'s participation measure under T17) are all directional fields.
- **Scalar fields** — gradients in participation density. Pressure $p$ and mass density $\rho$ in fluid mechanics, electric and chemical potentials, energy landscapes — all are emergent properties of how participation density varies across space (ED-I-06 §4).
- **Curvature-like fields** — pre-geometric participation patterns where propagation paths are biased in geometric-bending-like ways. ED-I-06 §5 designates this class as the conceptual bridge to spacetime emergence in ED-10. Substrate-gravity content (Theorems 19, 20, ED Combination Rule, T21) belongs to this class at substrate level.

**Forces.** ED-I-06 defines forces as **biases in participation flow sourced by stable participation structures** (§6). The underlying principle: *micro-events follow the most stable participation channels available to them.* When directional, scalar, or curvature-like structures bias propagation, the system experiences what is conventionally interpreted as a force.

**Non-forces.** Two structurally distinct classes of non-force content can appear in continuum equations:

- **Transport-kinematic frame terms** — bilinear couplings between transport fields that arise specifically when dynamics are written in a fluid (Eulerian) coordinate system. These are coordinate-frame artifacts of the fluid description, not biases sourced by stability.
- **Continuum-imposed constraints** — fluid-mechanical structural commitments (incompressibility, pressure as Lagrange multiplier) imposed at continuum level rather than sourced by participation structure.

The key ontological boundary is:

> *Canonical ED content corresponds to forces from participation structures.*
>
> *Non-ED content corresponds to transport-kinematic frame terms and continuum constraints.*

This single boundary unifies six previously separate findings of the NS / MHD program:

- **NS-2.08** classified advection, pressure, and incompressibility as fluid-mechanical-additions not native to ED canonical channels.
- **NS-Smoothness** (Section §5 of the main paper) identified the advective vortex-stretching $\int\boldsymbol{\omega}\cdot S\boldsymbol{\omega}\,dV$ as the unique indefinite-sign contribution to the gradient-norm Lyapunov in 3D NS.
- **NS-Turbulence** (Section §6 of the main paper) found the NS advective triad to be spectrally incompatible with P7's symmetric quadratic class.
- **NS-MHD-2** identified the Lorentz force as canonical ED via T17 minimal coupling, with the kinematic $\mathbf{v}\times\mathbf{B}$ component derived from the minimal-coupling form rather than separately committed.
- **NS-MHD-3** established three-angle convergence on the induction-equation kinematic term as non-ED at architectural / dynamical / spectral levels — the magnetic-side analogue of NS advection.
- **NS-MHD-4** consolidated the eleven-item architectural classification of incompressible MHD.

Under the ED-I-06 ontology, all six findings read as instances of the single forces-vs-frame-kinematic distinction. The transport-kinematic class (advection, induction kinematic, Ohm kinematic) consists of frame artifacts of the fluid coordinate system; the canonical-ED class (viscous diffusion, magnetic diffusion, Lorentz force, Maxwell structure, R1 substrate cutoff) consists of biases sourced by stable participation structures (directional fields, the V1 vacuum kernel, the gauge directional-field $\tau_g$).

---

## C.3 The Incompressible MHD System

The standard incompressible resistive MHD equations couple Navier-Stokes to Maxwell's equations via the Lorentz force in the momentum equation and the induction equation for the magnetic field:

**Momentum equation:**
$$\rho\bigl(\partial_t\mathbf{v} + (\mathbf{v}\cdot\nabla)\mathbf{v}\bigr) = -\nabla p + \mu\nabla^2\mathbf{v} + (\nabla\times\mathbf{B})\times\mathbf{B} + \rho\mathbf{f}^\mathrm{ext}.$$

**Induction equation:**
$$\partial_t\mathbf{B} = \nabla\times(\mathbf{v}\times\mathbf{B}) + \eta\nabla^2\mathbf{B}.$$

**Constraints:**
$$\nabla\cdot\mathbf{v} = 0, \qquad \nabla\cdot\mathbf{B} = 0.$$

The Lorentz force per unit volume in the MHD limit is $\mathbf{j}\times\mathbf{B} = \mu_0^{-1}(\nabla\times\mathbf{B})\times\mathbf{B}$, with quasi-neutrality suppressing the $\rho_q\mathbf{E}$ contribution at typical MHD scales. The magnetic diffusivity is $\eta = 1/(\sigma\mu_0)$, with $\sigma$ the electrical conductivity. The **ED-augmented momentum equation** carries an additional R1 term $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$ inherited from the velocity sector (§4 of the main paper, NS-3.01 / NS-Smoothness-2):

$$\rho\bigl(\partial_t\mathbf{v} + (\mathbf{v}\cdot\nabla)\mathbf{v}\bigr) = -\nabla p + \mu\nabla^2\mathbf{v} - \kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v} + (\nabla\times\mathbf{B})\times\mathbf{B} + \rho\mathbf{f}^\mathrm{ext}.$$

The generalized resistive Ohm's law is

$$\mathbf{j} = \sigma\bigl(\mathbf{E} + \mathbf{v}\times\mathbf{B}\bigr).$$

Its $\mathbf{v}\times\mathbf{B}$ piece is a transport-kinematic component classified alongside the induction kinematic term.

This eleven-item content set covers every term in standard incompressible resistive MHD. The classification that follows is over these eleven items.

---

## C.4 Architectural Classification of MHD Terms

The four sub-arc memos NS-MHD-1 through NS-MHD-5 jointly classify every MHD content channel. Three classes emerge.

### C.4.1 Canonical ED content (6 items)

Each item is FORCED at form level by a canonical ED channel and is ontologically a force sourced by a stable participation structure:

**(a) Viscous diffusion $\mu\nabla^2\mathbf{v}$.** The mobility channel applied component-wise to velocity. Per the field-type-agnostic vector-extension of the canonical PDE (Architectural Canon Vector Extension memo), the mobility channel produces a Laplacian-class diffusion structure on any vector field at fluid scale. Ontologically, $\mu\nabla^2\mathbf{v}$ is a participation-flow bias toward smoother velocity orientation, sourced by the directional-field structure of $\mathbf{v}$ itself. Form FORCED; coefficient $\mu$ INHERITED at value layer.

**(b) Magnetic diffusion $\eta\nabla^2\mathbf{B}$.** The mobility channel applied component-wise to the magnetic field. Structurally identical to (a) at the level of canonical-channel derivation — the vector-extension is field-type-agnostic, so the same mobility-channel argument that produces $\mu\nabla^2\mathbf{v}$ produces $\eta\nabla^2\mathbf{B}$. Ontologically, a participation-flow bias on the magnetic directional field. Form FORCED; resistivity $\eta = 1/(\sigma\mu_0)$ INHERITED.

**(c) Lorentz force $(\nabla\times\mathbf{B})\times\mathbf{B}$.** Theorem 17 (Gauge-Fields-as-Rule-Type) FORCES the substrate-level minimal-coupling form $\partial_\mu \to \partial_\mu - iqA_\mu$ on charged structural rule-types. The classical semiclassical limit yields the per-chain force $q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$; coarse-graining to fluid scale yields the force density $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$, which reduces in the MHD limit to $(\nabla\times\mathbf{B})\times\mathbf{B}$. Ontologically, the bias on charged-chain participation flow imposed by the gauge directional-field $\tau_g$. Form FORCED by T17 minimal coupling; the kinematic $\mathbf{v}\times\mathbf{B}$ component is *derived* from the minimal-coupling form rather than separately committed (NS-MHD-2 §3.2). Coarse-graining bridge INHERITED in parallel to the NS-2 viscous-content coarse-graining.

**(d) Maxwell field structure ($\partial_t\mathbf{B}$, $\nabla\times\mathbf{B}$, $\nabla\cdot\mathbf{B} = 0$).** Theorem 17's gauge content directly FORCES the four-channel structure of $\tau_g$ (group, vertex, worldline, vacuum), from which Maxwell's equations follow under gauge-quotient identification. The magnetic-divergence-free constraint $\nabla\cdot\mathbf{B} = 0$ is the no-monopoles structural feature of the canonical $U(1)$ gauge content — distinct in status from the velocity incompressibility constraint (which is fluid-mechanical-imposed). Ontologically, directional-field dynamics for $\tau_g$. Form FORCED; field amplitudes INHERITED.

**(e) R1 substrate-cutoff term $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$.** The form-FORCED hyperviscous stabilization arising from V1's finite-width vacuum kernel (Section §5 of the main paper). Inherits into the MHD momentum equation by virtue of being a canonical-ED augmentation of the velocity sector independent of EM coupling. Ontologically, a substrate-level participation-stability mechanism (T18-class kernel retardation expressed at V1 vacuum-kernel scale) imposing a hyperviscous bias on velocity-gradient cascade. Form FORCED; coefficient $\kappa$ INHERITED.

All six items are forces in the ED-I-06 sense — biases on participation flow sourced by stable participation structures.

### C.4.2 Continuum constraints (non-obstructive, 2 items)

These items are not forces in the ED-I-06 sense and are not derivable from any canonical ED channel. They are continuum-level structural commitments imposed at fluid scale rather than sourced by participation structure. Crucially, they are also *non-obstructive*: they introduce no indefinite-sign Lyapunov contributions and no spectral pathology.

**(f) Pressure $-\nabla p$.** Scalar-gradient in form (the gradient of a scalar density-class quantity) but *imposed* as a Lagrange multiplier for the incompressibility constraint, not sourced as a participation-density bias from below. Ontologically, a constraint-derived field rather than a force-from-stability. Sign-definite contribution to the kinetic-energy budget.

**(g) Velocity incompressibility $\nabla\cdot\mathbf{v} = 0$.** Continuum kinematic constraint, not derivable from any canonical channel. The canonical ED PDE does not commit to divergence-free participation-measure evolution; the assumption is imposed at the fluid level. Non-obstructive.

(The magnetic-divergence-free constraint $\nabla\cdot\mathbf{B} = 0$ is in a different category, as noted in §C.4.1(d); it is FORCED by Maxwell field structure under T17 and is canonical ED.)

### C.4.3 Transport-kinematic non-ED terms (obstructive, 3 items)

The three remaining items share a single structural class. They are not sourced by participation structures, are not produced by minimal coupling, and are dynamically and spectrally obstructive in parallel ways.

**(h) Advection $(\mathbf{v}\cdot\nabla)\mathbf{v}$.** Bilinear in velocity with a directional derivative. Three-angle convergence on non-ED status established in NS-2.08 (architectural — no canonical channel produces this index-and-derivative structure), NS-Smoothness §5 (dynamical — supplies the unique indefinite-sign contribution to the gradient-norm Lyapunov via vortex-stretching), and NS-Turbulence §6 (spectral — bilinear-with-transverse-projector triad incompatible with P7 symmetric quadratic class).

**(i) Induction kinematic $\nabla\times(\mathbf{v}\times\mathbf{B})$.** Bilinear in $(\mathbf{v},\mathbf{B})$ with cross-product followed by curl. Expanded under incompressibility, $(\mathbf{B}\cdot\nabla)\mathbf{v} - (\mathbf{v}\cdot\nabla)\mathbf{B}$ — the magnetic-tension stretching term and the magnetic advection term, both transport-kinematic bilinear couplings. Three-angle convergence on non-ED status established in NS-MHD-3: architectural (no canonical channel for bilinear $\mathbf{v}$-$\mathbf{B}$ transport-kinematic structure), dynamical (unique indefinite-sign contribution to magnetic-energy Lyapunov $E_M = \tfrac{1}{2}\int|\mathbf{B}|^2\,dV$, structurally parallel to vortex-stretching's role in 3D NS), and spectral (bilinear-with-Levi-Civita-projection triad incompatible with P7 symmetric quadratic class).

**(j) Ohm kinematic $\mathbf{v}\times\mathbf{B}$.** Cross-product velocity-magnetic coupling appearing in the generalized Ohm's law. Same structural class as (h) and (i): bilinear with antisymmetric Levi-Civita projection between two transport fields, not produced by any canonical channel.

**Common structural features.**

- *Not sourced by participation structures.* None corresponds to a directional-field bias, a scalar-density gradient, or a curvature-like-field bias on participation flow.
- *Frame-kinematic.* All three are bilinear couplings between two transport fields that arise specifically when dynamics are written in the fluid (Eulerian) coordinate system. They are coordinate artifacts of the fluid frame.
- *Same algebraic class.* Bilinear-with-projection between two transport fields (transverse projector $P_{ij}$ for advection; Levi-Civita $\varepsilon_{ijk}$ for induction kinematic and Ohm kinematic).
- *Spectrally incompatible with P7.* P7 generates symmetric-quadratic triad couplings; the transport-kinematic class is antisymmetric / projector-mediated and is structurally incompatible with the only canonical nonlinear-coupling channel.
- *Dynamically obstructive.* Each supplies an indefinite-sign contribution to a Lyapunov functional that would otherwise be monotonically decaying.

Ontologically under ED-I-06, these are *frame artifacts* of the fluid coordinate system — not forces at all.

---

## C.5 Final Architectural Classification Table

| Term | Equation | Origin | Architectural Status | Ontological Status (ED-I-06) | Notes |
|---|---|---|---|---|---|
| Viscous diffusion | $\mu\nabla^2\mathbf{v}$ | Mobility channel on $\mathbf{v}$ | Canonical ED | Force from directional field $\mathbf{v}$ | Form FORCED; coefficient INHERITED |
| Magnetic diffusion | $\eta\nabla^2\mathbf{B}$ | Mobility channel on $\mathbf{B}$ | Canonical ED | Force from directional field $\mathbf{B}$ | Field-type-agnostic vector extension |
| Lorentz force | $(\nabla\times\mathbf{B})\times\mathbf{B}$ | T17 minimal coupling | Canonical ED | Force from directional field $\tau_g$ via minimal coupling | Kinematic $\mathbf{v}\times\mathbf{B}$ derived from minimal-coupling form |
| R1 substrate cutoff | $-\kappa\mu_\mathrm{V1}\ell_P^2\nabla^4\mathbf{v}$ | V1 finite-width vacuum kernel | Canonical ED | Force from substrate participation structure | Hyperviscous Lyapunov stabilization |
| Magnetic time-evolution | $\partial_t\mathbf{B}$ | T17 gauge-field dynamics | Canonical ED | Directional-field dynamics | Standard time-derivative on $A_\mu$ |
| Magnetic divergence-free | $\nabla\cdot\mathbf{B} = 0$ | T17 / Maxwell structure | Canonical ED | Directional-field structural constraint | FORCED by gauge content |
| Pressure | $-\nabla p$ | Lagrange multiplier for $\nabla\cdot\mathbf{v}=0$ | Continuum constraint | Imposed (not a force) | Non-obstructive; sign-definite |
| Velocity incompressibility | $\nabla\cdot\mathbf{v} = 0$ | Fluid kinematic constraint | Continuum constraint | Imposed (not a force) | Non-obstructive |
| Advection | $(\mathbf{v}\cdot\nabla)\mathbf{v}$ | Eulerian-frame bilinear | Non-ED (obstructive) | Frame-kinematic (not a force) | NS-2.08 / NS-Smoothness §5 / NS-Turbulence §6 |
| Induction kinematic | $\nabla\times(\mathbf{v}\times\mathbf{B})$ | Eulerian-frame bilinear | Non-ED (obstructive) | Frame-kinematic (not a force) | NS-MHD-3 three-angle convergence |
| Ohm kinematic | $\mathbf{v}\times\mathbf{B}$ in Ohm's law | Eulerian-frame bilinear | Non-ED (obstructive) | Frame-kinematic (not a force) | Same structural class |

**Aggregate counts.** Of eleven content items: six canonical-ED forces, two continuum-imposed constraints, three transport-kinematic non-forces. Only six of eleven items are forces in the ED-I-06 sense; the remaining five are constraints or frame artifacts of the fluid coordinate system.

---

## C.6 Structural Verdict

The four sub-arc closures (NS-MHD-1 / 2 / 3 / 4) and the consolidated classification table (§C.5) jointly support five structural verdicts:

**(V1) MHD is partially ED-architectural, exactly like NS.** The canonical / non-canonical boundary in incompressible MHD is the same boundary that runs through pure NS: forces from participation structures on one side, frame-kinematic terms and continuum constraints on the other. The structural shape of the classification is preserved under the NS → MHD upgrade.

**(V2) MHD has strictly more canonical content on the EM side.** Maxwell field structure, Lorentz force, magnetic divergence-free constraint, and magnetic diffusion are all canonical ED via Theorem 17 and the mobility channel. The MHD upgrade does not add any new fluid-mechanical-addition or non-ED obstructive term on the EM side; it adds only canonical-ED forces. The canonical : non-canonical ratio for the EM-side additions is 4 : 2; for the pure-NS momentum equation it is 1 : 3. The aggregate MHD ratio (six canonical : five non-canonical) is dominated by canonical content.

**(V3) The canonical / non-canonical boundary is the kinematic-coupling pattern.** Velocity-dependence in continuum equations splits into two structurally distinct classes:

- *Minimal-coupling-derived velocity-dependence* (Lorentz $\mathbf{v}\times\mathbf{B}$): canonical ED via Theorem 17. A force sourced by the gauge directional-field $\tau_g$ acting on charged chains.
- *Transport-kinematic velocity-dependence* (advection, induction kinematic, Ohm kinematic): non-ED. A frame-kinematic artifact of the fluid (Eulerian) coordinate system, not a force.

This is the load-bearing architectural insight of the MHD arc and refines the NS-2.08 classification of pure NS by giving it an ontological grounding under ED-I-06.

**(V4) The induction term is the magnetic-side analogue of NS advection.** Both are bilinear-with-projection couplings between two transport fields. Both are non-ED at architectural / dynamical / spectral levels. Both supply the unique indefinite-sign contribution to their respective Lyapunov functionals — gradient-norm Lyapunov for NS advection (Section §5 of the main paper), magnetic-energy Lyapunov for the induction kinematic term (NS-MHD-3 §4.2). The structural parallel is exact, validating the kinematic-coupling pattern as a generalizable architectural feature rather than an NS-specific finding.

**(V5) MHD inherits the same structural obstruction class as NS.** ED supplies real architectural regularization (R1 + magnetic diffusion + viscous diffusion), genuine canonical force-content (Lorentz + Maxwell), and an architectural account of the EM-side additions. But the obstruction to ED-style smoothness in MHD lies entirely in the transport-kinematic sector — advection plus induction kinematic plus Ohm kinematic — exactly as in pure NS. The Clay-NS-relevant decomposition of the main paper extends to MHD with the obstruction class enlarged from one item (advection) to three items in the same structural class.

The structural picture is that **MHD is *more* ED-architectural than pure NS** in the precise sense that the EM-side additions are predominantly canonical, while the new fluid-mechanical-specific structural commitments belong to a single class with a single architectural origin (transport-kinematic) and a single architectural defect (no canonical channel, frame-kinematic in ED-I-06 ontology, spectrally incompatible with P7).

---

## C.7 Relation to the Main NS Synthesis

This appendix extends the architectural picture of the main paper without revising any of its conclusions:

- The main paper's Section §3 (NS-1 dimensional forcing via Path B-strong) is preserved.
- The main paper's Section §4 (NS-2 form derivation via partial vector-extension) extends to MHD via the field-type-agnostic vector-extension argument (§C.4.1(b), magnetic diffusion).
- The main paper's Section §5 (NS-Smoothness Intermediate Path C verdict, R1 mechanism, vortex-stretching as unique indefinite-sign Lyapunov contribution) extends to MHD with the induction kinematic term playing the same structural role on the magnetic side (§C.6 V4).
- The main paper's Section §6 (NS-Turbulence H1 trivial / H2 partial / H3 fail; advection spectrally incompatible with P7) extends to MHD with induction kinematic and Ohm kinematic spectrally incompatible with P7 in the same way.
- The main paper's three-angle convergence on advection-as-non-ED (architectural NS-2.08, dynamical NS-Smoothness, spectral NS-Turbulence) is now joined by a second three-angle convergence on the induction kinematic term (NS-MHD-3), validating the kinematic-coupling pattern as a generalizable architectural feature.

The ED-I-06 ontology supplies the conceptual unification under which all of these structural results read as instances of a single forces-vs-frame-kinematic-or-constraint distinction. The canonical / non-canonical boundary, established in the main paper at structural-architectural level, is now also grounded ontologically: canonical ED content is force-from-stability; non-ED content is frame-kinematic or imposed-constraint.

The main paper's headline disclaimers remain unchanged: ED does not resolve whether 3D NS blows up at finite time, does not predict critical Reynolds numbers, and does not supply a turbulence-cascade architectural template. The MHD extension preserves these disclaimers and adds parallel ones for MHD: ED does not derive dynamo theory, does not supply an MHD-turbulence cascade architectural template, and does not predict the magnetic-reconnection rate. What ED *does* deliver — for both NS and MHD, under both structural and ontological readings — is a complete account of which content channels are forces sourced by participation structures, which are frame artifacts of the fluid coordinate system, and which are continuum-imposed constraints. That account is unchanged in substance by the integration of the ED-I-06 ontology; it is strengthened in framing.

---

*Appendix C closes the integration of the NS-MHD arc and the ED-I-06 ontology into the NS Synthesis Paper. Eleven incompressible-MHD content items are classified into six canonical-ED forces, two continuum-imposed constraints, and three transport-kinematic non-forces. The kinematic-coupling pattern — minimal-coupling-derived velocity-dependence canonical, transport-kinematic velocity-dependence non-ED — is the canonical / non-canonical boundary in continuum fluid mechanics. The ED-I-06 ontology grounds this boundary as the forces-vs-frame-kinematic distinction, unifying the classification results of NS-2.08, NS-Smoothness, NS-Turbulence, NS-MHD-2, NS-MHD-3, and NS-MHD-4 under a single ontological framework. The main NS Synthesis Paper's results are preserved and ontologically strengthened.*
