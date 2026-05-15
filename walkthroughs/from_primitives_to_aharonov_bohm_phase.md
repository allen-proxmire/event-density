# From Primitives to the Aharonov-Bohm Phase

## A Walkthrough of the Event Density Derivation

**Allen Proxmire** · May 2026

---

## 1. The Question

In 1959, Yakir Aharonov and David Bohm proposed an experiment that should have been impossible according to the standard intuitions of classical electromagnetism. A charged particle is sent through a double-slit apparatus, but with a long thin solenoid placed *between* the two paths, on the side away from the screen. The solenoid contains a magnetic field; the regions traversed by the particle do not. In classical mechanics, the particle should be entirely unaffected by the solenoid — there is no force on it, no torque, no Lorentz coupling. The interference pattern on the screen should be unchanged whether the solenoid is on or off.

It isn't. When the solenoid is energized, the interference pattern shifts. The shift depends on the *enclosed magnetic flux* through the solenoid:

$$
\Delta \varphi = (q/\hbar) \cdot \Phi
$$

where $\Phi = \int \mathbf{B} \cdot d\mathbf{A}$ is the magnetic flux threading the solenoid and $q$ is the particle's charge. The particle's quantum-mechanical wavefunction registers a region of magnetic field through which the particle never travels.

The experiment was performed by Robert Chambers in 1960 using thin iron whiskers as flux sources, and confirmed by Akira Tonomura in 1986 with definitive nanometer-scale superconducting measurements. The Aharonov-Bohm effect is now standard textbook material, demonstrated in dozens of variant experiments, and recognized as one of the deepest empirical phenomena in quantum mechanics.

The puzzle the experiment poses is structural. In classical electromagnetism, the magnetic vector potential $\mathbf{A}$ was treated as a mathematical convenience — a quantity from which the magnetic field $\mathbf{B} = \nabla \times \mathbf{A}$ could be computed, but with no independent physical reality. Different choices of $\mathbf{A}$ giving the same $\mathbf{B}$ — *gauge equivalent* potentials — were considered physically identical. The classical equations of motion depend only on $\mathbf{B}$ and $\mathbf{E}$, never on $\mathbf{A}$ or the scalar potential $\phi$ in any way that distinguishes different gauges.

The Aharonov-Bohm effect breaks this picture. The interference shift depends on $\oint \mathbf{A} \cdot d\mathbf{x}$ around the closed path encircling the solenoid. This integral is gauge-invariant (different gauges give different $\mathbf{A}$ but the same $\oint$), but it is non-zero in regions where $\mathbf{B} = 0$. The vector potential carries physical information that the magnetic field alone does not.

Standard quantum mechanics accommodates this by accepting that the gauge potential is the physically meaningful quantity in the quantum context, with the magnetic field being a derived quantity. The textbook formulation: the wavefunction's phase responds to $\mathbf{A}$ through minimal coupling, and the phase difference around a closed loop is the gauge-invariant quantity $\oint \mathbf{A} \cdot d\mathbf{x} = \Phi$ that the experiment measures. This works mathematically. But it leaves a deeper question open: why should $\mathbf{A}$ have physical reality at all? What ontological status does the gauge potential have, and why does it manifest only in topologically non-trivial situations?

The Event Density framework provides an answer. Theorem 17 establishes that gauge fields are the continuum-level appearance of the substrate's rule-type connection — the substrate object that carries rule-type label information from one substrate region to another. The gauge potential $\mathbf{A}$ is not a mathematical convenience; it is the substrate's parallel-transport infrastructure for the rule-type relabeling group. The Aharonov-Bohm phase is the integral of this substrate connection around a non-contractible loop in a multiply-connected substrate channel — a substrate-level invariant that has observable consequences whenever the substrate's topology supports closed loops the particle's wavefunction can wind around.

This walkthrough makes the math explicit. The AB phase is downstream of T17: once the gauge field is established as a substrate connection, the closed-loop integral is the parallel-transport monodromy of the connection around the loop, and Stokes' theorem connects this monodromy to the enclosed flux. The structural new content is the substrate-level ontology of multiple-connectivity — the substrate explanation for why such loops exist in the first place — and the resolution of the gauge-reality question.

The chain has six structural moves:

1. T17 establishes the gauge field $A_\mu$ as the substrate's rule-type connection: a substrate object that carries rule-type label information from point to point in the continuum.

2. The substrate's participation graph supports multiply-connected topologies: substrate channels can have "holes" — regions of substrate that are excluded from the chain's accessible pathway, but around which the chain's wavefunction can wind.

3. Parallel transport of the participation measure along a path $\gamma$ multiplies the wavefunction by a phase factor $\exp\left[(iq/\hbar)\int_\gamma A_\mu dx^\mu\right]$.

4. The phase difference between two paths $\gamma_1$ and $\gamma_2$ around a non-contractible loop is $\Delta\phi = (q/\hbar)\oint A_\mu dx^\mu$, where the closed-loop integral is gauge-invariant and substrate-physically meaningful.

5. Stokes' theorem identifies the closed-loop integral with the integrated field strength through any surface bounded by the loop: $\oint A_\mu dx^\mu = \int F_{\mu\nu} d\Sigma^{\mu\nu} = \Phi$, where $\Phi$ is the enclosed magnetic flux.

6. The Aharonov-Bohm phase $\Delta\phi = q\Phi/\hbar$ is therefore the substrate-level monodromy of the rule-type connection around the closed loop, observable through wavefunction interference and gauge-invariant by construction.

The structural payoff: the AB phase is not a mysterious nonlocal effect of the gauge potential. It is the substrate-level monodromy of the rule-type connection around a closed loop in a multiply-connected substrate region. The gauge potential's physical reality is not a postulate; it is what T17 establishes the substrate to provide. The non-trivial topology — the "hole" the loop winds around — is a substrate-level feature of the participation graph, not an artifact of how we describe the system.

---

## 2. The Primitives That Matter

The framework rests on substrate-level ontological commitments. The Aharonov-Bohm walkthrough uses the same working subset as the gauge-fields walkthrough, with one additional structural element specific to topologically non-trivial regions.

**Micro-events (P01).** Discrete acts of becoming, vertices in a graph spanning the event manifold.

**Chains (P02).** Stable subgraphs along which a chain can repeatedly instantiate its update rule.

**Bandwidth (P04).** Non-negative real edge weight, with bandwidth-additivity for independent contributions.

**Polarity / U(1) phase (P09).** $U(1)$-valued phase relation between a chain's update rule and the local ED-flow direction.

**ED gradient.** Continuous spatial axis with no preferred origin.

**Substrate locality.** Participation contributions at one substrate region combine with those at another only via mediating substrate structure (chains, V1 kernel, channels). No instantaneous non-local action.

**Rule-type (Primitive 07).** Each chain carries a primitive label classifying the structural form of its update rule.

**Substrate channel topology.** The substrate's participation graph carries topological structure beyond mere connectivity. Specific substrate channels — paths along which a chain's participation measure can develop — can be multiply-connected, in the sense that the channel's cross-sectional topology has non-contractible loops. This topological structure is a primitive feature of the substrate, not derivable from more basic structure.

Three forced theorems load-bear here:

**T14 (Participation measure form).** $P_K = \sqrt{b_K} \, e^{i\pi_K}$ with the complex phase forced by Frobenius's theorem.

**U2 (Inner product on the participation-measure space).** Sesquilinear, complex, with the Hilbert-space structure forced by primitive-level aggregation arguments.

**T17 (Gauge-field-as-rule-type connection).** Establishes the gauge field $A_\mu$ as the substrate's rule-type connection — the parallel-transport infrastructure for the rule-type relabeling group at the continuum level. This is the load-bearing prerequisite for the AB derivation.

The Diffusion Coarse-Graining Theorem (DCGT) is a structural prerequisite for T17's continuum-level statement of $A_\mu$. The substrate-level rule-type connection becomes the continuum gauge field through DCGT's substrate-to-continuum bridge.

That's the structural setup. The Aharonov-Bohm argument runs on this.

---

## 3. The Substrate Reading of Multiple-Connectivity

Before the AB derivation can proceed, the substrate-level meaning of "multiply-connected substrate channel" must be made explicit. This is what makes the substrate ontology distinct from the standard mathematical-physics treatment of fiber bundles over multiply-connected base spaces.

### 3.1 Simply-connected vs. multiply-connected substrate channels

A *simply-connected* substrate channel is one whose accessible pathway has the property that any closed loop in the channel can be continuously deformed to a point without leaving the channel. The chain's wavefunction has only contractible loops to wind around; there are no topologically non-trivial cycles.

A *multiply-connected* substrate channel has accessible pathways that exclude certain regions — substrate "holes" — that the chain cannot enter. Around such a hole, closed loops are non-contractible: a loop encircling the hole cannot be continuously deformed to a point without crossing the excluded region.

The Aharonov-Bohm setup is the substrate-level instance of a multiply-connected substrate channel. The chain (the charged particle) accesses a substrate region that excludes the solenoid's interior. Loops around the solenoid are non-contractible in the chain's accessible substrate.

### 3.2 What makes a substrate channel multiply-connected

The substrate channel's topology is determined by what regions of substrate are accessible to the chain. In the AB experiment, the chain is excluded from the solenoid's interior because the solenoid contains a region of high participation density — a coil of conducting wire carrying current. The chain, propagating as a low-multiplicity participation rule, cannot enter this region without massive substrate disruption that would force individuation. The chain's accessible substrate is the region *outside* the solenoid, which is multiply-connected.

This is structurally analogous to other multiply-connected substrate situations:

- A particle propagating around a region containing a black-hole interior (the chain is excluded from the saturated participation zone inside the horizon).
- A flux quantum penetrating a superconducting ring (the chain — a Cooper pair — propagates around but not through the magnetic-flux region).
- A ground-state electron orbital around a nucleus (the chain is excluded from a small region around the nuclear charge density).

In each case, the substrate channel is multiply-connected because the chain's accessibility excludes a region. The non-contractible loops are the loops winding around the excluded region.

### 3.3 The fiber bundle reading

In the language of fiber bundles, the substrate's rule-type structure forms a $G$-bundle over the substrate's accessible base space, where $G$ is the rule-type relabeling group ($U(1)$ for QED contexts; non-Abelian for Yang-Mills contexts). When the base space (the chain's accessible substrate) is simply-connected, the bundle has only the trivial topological class. When the base space is multiply-connected, the bundle can support non-trivial topological structure: parallel transport around a non-contractible loop can produce a non-trivial monodromy.

The substrate ontology of multiple-connectivity is what supplies the non-trivial topology in the first place. Standard physics takes the multiple-connectivity as given (the experimentalist arranges for a region with a hole) and computes the resulting AB phase. ED supplies the substrate-level meaning of the hole: it is a region the chain cannot access because of high local participation density or saturation.

---

## 4. Parallel Transport on the Rule-Type Bundle

T17 establishes the gauge field $A_\mu$ as the substrate's rule-type connection. The parallel-transport operation associated with this connection is the central mathematical object of the AB derivation.

### 4.1 The connection's transport rule

When the participation measure $\Psi(x)$ is transported along a path $\gamma$ from point $x_0$ to point $x_1$, the rule-type relabeling at $x_1$ relative to the choice at $x_0$ is determined by the integrated gauge field along $\gamma$. The participation measure at the endpoint, parallel-transported from the starting point, is:

$$
\Psi_{\mathrm{transported}}(x_1) = \exp[(iq/\hbar) \int_\gamma A_\mu dx^\mu] \cdot \Psi (x_0)
$$

The exponent is the *holonomy* of the connection along the path. The factor $q/\hbar$ comes from the gauge coupling — specifically, the rule-type-coupling charge $q$ that T17 derives as the substrate-level coupling strength of the rule-type's relabeling, scaled by $\hbar$ from the U2-derived inner-product normalization.

### 4.2 What parallel transport means at the substrate level

In the substrate ontology, parallel transport is the substrate-level operation of carrying a chain's rule-type label from one substrate region to another while preserving the chain's participation structure. The rule-type label at $x_0$ is a choice; the rule-type label at $x_1$ is determined by the substrate's connection structure between the two points.

If the connection is trivial (no gauge field anywhere), parallel transport is the identity: the rule-type label at $x_1$ is the same as at $x_0$. The participation measure transports without phase change.

If the connection is non-trivial (gauge field present), parallel transport accumulates a phase factor as the chain traverses the path. The phase is the integral of $A_\mu$ along the path, scaled by $q/\hbar$.

This is the substrate reading of why a chain in an electromagnetic field acquires a phase as it moves: the substrate's rule-type connection is non-trivial in the field region, and parallel transport along the chain's path accumulates the connection's contribution.

### 4.3 Path-dependence in multiply-connected regions

For a simply-connected accessible substrate, the integral $\int_\gamma A_\mu dx^\mu$ depends on $\gamma$ only through its endpoints — different paths between the same endpoints give the same integral, because by Stokes' theorem the difference is the integrated $F_{\mu\nu}$ over the bounded surface, and this surface lies entirely in the accessible substrate where $F_{\mu\nu}$ is whatever it is.

For a multiply-connected accessible substrate, paths between the same endpoints can have different integrals, *because* the difference between two paths bounds a surface that may pass through the inaccessible region (the "hole"). If $F_{\mu\nu}$ is non-zero in the hole, the path-difference integral does not vanish.

This path-dependence is what makes the AB phase observable. For a chain that travels through a double-slit apparatus with the solenoid between the slits, the upper path and the lower path both go around the solenoid — but on opposite sides. The two paths together form a closed loop encircling the solenoid. The phase difference between them is the closed-loop integral of $A_\mu$ around the solenoid.

---

## 5. The Closed-Loop Phase

The AB phase is the closed-loop integral of $A_\mu$ around a non-contractible loop. Computing it is straightforward once parallel transport is in hand.

### 5.1 The setup

In the AB experiment, a chain (a charged particle's worldline) splits into two sub-paths $\gamma_1$ and $\gamma_2$ at a beam-splitter, traverses opposite sides of a flux-containing region (a solenoid), and recombines at a detector. The two sub-paths form a closed loop $\gamma = \gamma_1 - \gamma_2$ encircling the solenoid.

The chain's participation measure at the detector is a coherent superposition of contributions from the two paths:

$$
\Psi_{\mathrm{detector}} \propto [\exp((iq/\hbar) \int_{\gamma_1} A_\mu dx^\mu) + \exp((iq/\hbar) \int_{\gamma_2} A_\mu dx^\mu)] \cdot \Psi_{\mathrm{source}}
$$

up to amplitude factors that are common to both paths and do not affect the phase analysis.

### 5.2 The relative phase

Factoring out the path-1 phase, the superposition becomes:

$$
\Psi_{\mathrm{detector}} \propto [1 + \exp((iq/\hbar) (\int_{\gamma_2} - \int_{\gamma_1}) A_\mu dx^\mu)] \cdot \exp((iq/\hbar) \int_{\gamma_1} A_\mu dx^\mu) \cdot \Psi_{\mathrm{source}}
$$

The relative phase between the two paths is:

$$
\Delta \varphi = (q/\hbar) (\int_{\gamma_2} - \int_{\gamma_1}) A_\mu dx^\mu = (q/\hbar) \oint_\gamma A_\mu dx^\mu
$$

where the closed-loop integral is taken with $\gamma_2$ traversed forward and $\gamma_1$ traversed backward, encircling the solenoid.

### 5.3 The interference pattern

The intensity at the detector is proportional to $|\Psi_\mathrm{detector}|^2$. Working through the modulus-squared:

$$
|\Psi_{\mathrm{detector}}|^{2} \propto |1 + \exp(i\Delta \varphi)|^{2} = 2(1 + \cos \Delta \varphi) = 4 \cos^{2}(\Delta \varphi /2)
$$

The interference pattern is determined by $\Delta\phi$. As $\Delta\phi$ varies from 0 to $2\pi$ — for example, by changing the flux through the solenoid — the interference pattern shifts: maxima become minima and vice versa.

The shift is observable. The empirical signature is the dependence of the interference pattern on the enclosed flux, even though the chain never enters the flux region.

---

## 6. Stokes' Theorem and the Topological Identity

The closed-loop integral of $A_\mu$ has a direct topological meaning. By Stokes' theorem on any surface $\Sigma$ bounded by the loop $\gamma$:

$$
\oint_\gamma A_\mu dx^\mu = \int_\Sigma F_{\mu \nu} d\Sigma^{\mu \nu}
$$

where $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ is the field strength. In the $U(1)$ case relevant for electromagnetic AB, this is:

$$
\oint_\gamma A \cdot dx = \int_\Sigma B \cdot dA = \Phi
$$

where $\Phi$ is the magnetic flux through any surface bounded by $\gamma$.

### 6.1 Why the surface integral is well-defined

Stokes' theorem requires the surface $\Sigma$ to lie in a region where $A_\mu$ is defined and $F_{\mu\nu}$ is the curl of $A_\mu$. In the AB setup, the chain's accessible substrate excludes the solenoid's interior, but the surface $\Sigma$ — bounded by $\gamma$ outside the solenoid — *passes through* the solenoid's interior, where $F_{\mu\nu} \neq 0$ (the magnetic field is concentrated there).

This is the topological subtlety. The surface $\Sigma$ is not entirely in the chain's accessible region — it crosses the inaccessible solenoid interior. Stokes' theorem still applies because the gauge field $A_\mu$ is defined throughout (it has the form of a flux-line vector potential outside the solenoid, smoothly continued into the solenoid where $F_{\mu\nu}$ is non-zero), and the field strength's integral over $\Sigma$ counts the enclosed flux exactly once.

### 6.2 Independence of surface choice

Different choices of surface $\Sigma$ bounded by the same loop $\gamma$ give the same flux integral, by Gauss's law: $\nabla \cdot \mathbf{B} = 0$ implies that the flux through any closed surface is zero, so the flux through two surfaces with the same boundary is the same. The closed-loop integral $\oint A_\mu dx^\mu$ depends only on the loop, not on how the surface is chosen — it is a topological invariant of the loop in the gauge field.

### 6.3 Independence of gauge

Different gauge choices $A_\mu \to A_\mu + \partial_\mu \alpha$ change the line integral of $A_\mu$ along open paths (by $\alpha(x_1) - \alpha(x_0)$), but they do *not* change the closed-loop integral: $\oint \partial_\mu \alpha \, dx^\mu = \alpha(x) - \alpha(x) = 0$. The AB phase is gauge-invariant by this elementary argument.

This is structurally important: the AB phase is observable, and it must be gauge-invariant for the framework to be self-consistent. Stokes' theorem and the gauge-invariance of $F_{\mu\nu}$ together guarantee that the AB phase is a well-defined physical quantity, dependent only on the enclosed flux and the chain's charge.

### 6.4 The AB phase formula

Combining the closed-loop integral with Stokes' theorem:

$$
\Delta \varphi = (q/\hbar) \oint_\gamma A_\mu dx^\mu = (q/\hbar) \Phi
$$

The Aharonov-Bohm phase shift is the chain's charge times the enclosed flux divided by Planck's constant. The phase is:

- *Topological*: depends only on the homotopy class of the loop $\gamma$ around the flux region, not on the loop's specific shape.
- *Gauge-invariant*: independent of the choice of $A_\mu$ within its gauge equivalence class.
- *Universal* (in the sense of multivaluedness): defined modulo $2\pi$, since adding $2\pi$ to $\Delta\phi$ produces an indistinguishable interference pattern. This is consistent with $\Phi/\Phi_0$ being defined modulo 1, where $\Phi_0 = 2\pi\hbar/q$ is the fundamental flux quantum.

### 6.5 The flux quantum

The phase $\Delta\phi = q\Phi/\hbar$ becomes $2\pi$ when $\Phi = 2\pi\hbar/q$. This is the *flux quantum* $\Phi_0 = 2\pi\hbar/q = h/q$. For an electron ($q = e$), $\Phi_0 = h/e \approx 4.14 \times 10^{-15}$ Wb. For a Cooper pair ($q = 2e$), $\Phi_0 = h/(2e) \approx 2.07 \times 10^{-15}$ Wb — the famous superconducting flux quantum.

The flux quantum's appearance in the AB phase formula is structurally meaningful: it is the amount of flux that produces a full $2\pi$ phase rotation, equivalent to no observable effect. In a multiply-connected substrate channel, only the flux *modulo* $\Phi_0$ is physically relevant; integer multiples of $\Phi_0$ are invisible to the AB measurement.

---

## 7. The Empirical Setup and Observable Consequences

The Aharonov-Bohm experiment, in its canonical form, places a thin solenoid between the two slits of a double-slit interferometer. The solenoid is energized to produce a magnetic flux $\Phi$ through its interior. The interference pattern on the detector screen is observed.

### 7.1 The classical baseline

If the gauge potential were a mere mathematical convenience with no physical reality, classical reasoning predicts: there is no force on the particle (since $\mathbf{B} = 0$ along its path), no torque, no Lorentz coupling. The interference pattern should be unaffected by whether the solenoid is energized.

### 7.2 The empirical observation

The interference pattern *does* shift when the solenoid is energized. The shift is sinusoidal in $\Phi$, with one full period corresponding to one flux quantum $\Phi_0$. The functional form is exactly $\Delta\phi = q\Phi/\hbar$ as predicted.

The Tonomura experiment of 1986 used superconducting niobium tori as flux sources, achieving sub-quantum precision on the flux measurement. The interference shift matched the AB prediction to better than 1% accuracy. Subsequent experiments with electron holography, Aharonov-Casher (electric AB analogue), Berry phase generalizations, and condensed-matter analogues (mesoscopic rings in metals) have all confirmed the AB structure across many platforms and many decades.

### 7.3 Substrate-level reading of the empirics

In the substrate ontology, the empirical observation is straightforward. The chain's accessible substrate is multiply-connected because the solenoid's interior is excluded. The chain's two paths in the double-slit apparatus form a closed loop encircling the solenoid. Parallel transport of the chain's participation measure around the loop accumulates a phase determined by the integrated gauge field along the loop. Stokes' theorem connects this to the enclosed flux. The interference pattern responds to the relative phase between the two paths.

There is no nonlocal mystery. The chain interacts with the substrate's rule-type connection (the gauge field) along its actual path. The connection's structure depends on the global field configuration — including the flux in the solenoid, even though the field is zero on the chain's path. This is what a connection on a fiber bundle with non-trivial topology is supposed to do.

### 7.4 Generalizations and analogues

The AB structure generalizes beyond the magnetic case:

- **Electric AB.** A line of electric scalar potential through a region the chain does not access produces the same kind of phase shift, integrated as $\int q \phi \, dt$ along the chain's worldline.
- **Aharonov-Casher.** A neutral particle with magnetic moment moving around a line of charge picks up a phase analogous to AB but with role of charge and moment swapped.
- **Berry phase.** When the chain's parameters undergo a closed cyclic evolution, the geometric phase accumulated is the holonomy of an analogous bundle connection on parameter space.

In each case, the substrate-level reading is the same: parallel transport of the participation measure along a closed loop in a connection-bearing space accumulates a holonomy that depends on the enclosed structure. The AB phase is the prototype; the others are generalizations of the same parallel-transport mechanism.

---

## 8. The Gauge-Reality Question Resolved

The deepest question the AB effect poses for standard physics is the ontological status of the gauge potential. In classical electromagnetism, $\mathbf{A}$ was a mathematical convenience. The AB effect demonstrates that quantum mechanics is sensitive to $\mathbf{A}$ in ways classical mechanics is not. Standard physics absorbs this by accepting that the gauge potential is the physically meaningful quantity in the quantum context, with the magnetic field being a derived quantity.

But this leaves a question hanging: *why* should the gauge potential have physical reality? The answer, in standard physics, is roughly "because experiments show it does." This is empirically correct but ontologically unsatisfying.

### 8.1 The substrate ontology's answer

The substrate ontology answers the question structurally. The gauge potential $A_\mu$ is, per T17, the continuum-level appearance of the substrate's rule-type connection. The connection is a primitive piece of substrate infrastructure — it is what carries rule-type label information from one substrate region to another. The continuum-level $A_\mu$ field is not a mathematical convenience and not an emergent abstraction; it is a coarse-grained reading of substrate machinery that was already present at the substrate level.

The reality of the gauge potential is therefore not a postulate of quantum mechanics. It is the continuum reflection of substrate ontology. Classical electromagnetism, which sees only the field strength, was looking at the wrong level of structure: it captured the curvature of the connection but missed the connection itself.

### 8.2 What the AB phase reveals

The AB phase is what happens when a chain's wavefunction can detect the connection's holonomy independently of the curvature in any region the chain visits. The chain interacts with the connection along its path. When the path forms a closed loop in a multiply-connected substrate, the connection's loop-integral (its monodromy) registers the enclosed connection structure even when the chain itself never visits the curvature region.

Standard physics frames this as "the gauge potential has reality." The substrate ontology frames it as "the rule-type connection is a primitive piece of substrate structure, with non-trivial topology in multiply-connected regions, and the chain detects this through parallel transport of its participation measure."

These framings are not in conflict. The substrate ontology supplies the structural account of *why* the gauge potential has reality, namely because it is the continuum reading of a primitive substrate object.

### 8.3 Gauge-redundancy and physical content

The puzzle of *gauge redundancy* — different $A_\mu$ giving the same physics — is structurally clear in the substrate ontology. Gauge transformations $A_\mu \to A_\mu - \partial_\mu \alpha$ correspond to local rule-type relabelings. Rule-type *labels* are not physical (the substrate's rule-type *content* is what's physical, not the choice of label). Different choices of label correspond to different gauge representations of the same substrate connection.

What is physical is the connection itself — the substrate-level parallel-transport infrastructure — which is gauge-invariant content. The AB phase, the field strength $F_{\mu\nu}$, and observable quantities derived from them are all gauge-invariant because they capture connection content rather than label content.

This is not a postulate. It is what T17's substrate reading of the gauge field implies, applied to the AB context.

---

## 9. What's Forced, What's Inherited, What's Open

It is worth being precise about what changes when the AB derivation is in place versus when it isn't.

### 9.1 What's forced

The AB phase formula $\Delta\phi = q\Phi/\hbar$ is forced as a consequence of T17 (gauge field as substrate connection) plus parallel transport along a non-contractible loop.

The closed-loop integral $\oint A_\mu dx^\mu$ is gauge-invariant by elementary integration: gauge transformations contribute $\oint \partial_\mu \alpha \, dx^\mu = 0$.

Stokes' theorem connecting the closed-loop integral to the enclosed flux is forced by standard differential geometry applied to the substrate connection.

The path-dependence of the line integral in multiply-connected regions is forced by the topological structure of the substrate channel: non-contractible loops bound surfaces that pass through the inaccessible region, and the field strength's integral over those surfaces does not vanish.

The gauge-reality question's resolution is forced by the substrate ontology of T17: $A_\mu$ has physical reality because it is the continuum reading of the substrate's rule-type connection, which is a primitive substrate object.

The flux-quantum structure $\Phi_0 = 2\pi\hbar/q$ as the period of the AB phase is forced by the $2\pi$-periodicity of the complex exponential in the participation measure.

The independence of the AB phase from the chain's specific path within a homotopy class is forced by the topological character of the holonomy.

### 9.2 What's inherited

The numerical value of the gauge coupling $q$ for any specific chain is INHERITED from the rule-type taxonomy of our universe. For electrons, $q = e$ (the elementary charge); for Cooper pairs, $q = 2e$; for other charged species, $q$ is whatever the rule-type provides. The framework establishes that the AB phase is proportional to $q$; the specific value of $q$ for any species comes from outside the structural-foundations work.

The numerical value of $\hbar$ in the AB formula is INHERITED from the dimensional atlas via the U2 / Madelung anchoring.

The value of the flux $\Phi$ in any specific experiment is INHERITED from the experimental setup — the solenoid current, the geometry of the flux-source, the magnetic susceptibility of the materials.

The specific topology of the multiply-connected region (the geometric arrangement of the experiment) is INHERITED from the experimentalist's choice of apparatus.

The substrate-level mechanism by which the chain is excluded from the inaccessible region (high participation density, saturation, geometric exclusion) is INHERITED from the specific substrate configuration of the experimental setup.

### 9.3 What's open

The closed-form derivation of the substrate-level mechanism by which a region becomes inaccessible to a chain is partially open. The framework establishes that high participation density excludes low-multiplicity chain propagation; the precise threshold for exclusion as a function of participation density and chain rule-type has not been derived to closed form.

The connection between AB's topological content and the broader index-theoretic framework of substrate-level topology is open. The framework's $G$-bundle structure for rule-type relabeling is structurally well-defined; the substrate-level meaning of higher-dimensional topological invariants (Chern numbers, $\theta$-angles, Pontryagin densities) has not been fully developed.

The non-Abelian generalization of AB — the Wu-Yang phase factor for non-Abelian gauge theories — follows the same structural pattern as the Abelian AB derivation, but with the connection becoming Lie-algebra-valued and the holonomy becoming a path-ordered exponential. The framework's T17 already extends to non-Abelian gauge groups; the explicit non-Abelian AB walkthrough is downstream content that has not been developed in detail in this walkthrough.

The relationship between AB phases and the $\theta$-angle in QCD-like theories is open. $\theta$-angles are global topological parameters of non-Abelian gauge theory analogous in some respects to AB phases; the framework's substrate reading of $\theta$-angles has not been fully articulated.

---

## 10. What This Argument Establishes

The chain runs:

Substrate primitives (micro-events, chains, bandwidth, polarity, ED gradient, locality, rule-type, substrate channel topology) → T14 (participation measure form forced) → U2 (inner product on participation-measure space forced) → T17 (gauge field as substrate rule-type connection forced) → DCGT (substrate-to-continuum bridge) → multiply-connected substrate channels (substrate-level topology) → parallel transport of participation measure along a path multiplies wavefunction by phase factor $\exp[(iq/\hbar)\int_\gamma A_\mu dx^\mu]$ → closed-loop integral around non-contractible loop is gauge-invariant phase $(q/\hbar)\oint A_\mu dx^\mu$ → Stokes' theorem identifies closed-loop integral with enclosed flux → AB phase $\Delta\phi = q\Phi/\hbar$ observable through wavefunction interference.

The Aharonov-Bohm phase is now a derived consequence of substrate ontology rather than a postulate-level commitment. The mathematical content of the standard AB derivation — the parallel-transport phase, the closed-loop monodromy, Stokes' theorem identification with enclosed flux — is unchanged. What changes is the foundational status: the AB phase is the substrate-level parallel-transport monodromy of the rule-type connection around a non-contractible loop in a multiply-connected substrate channel. The gauge potential is not a mathematical convenience; it is the continuum reflection of substrate machinery that was already there.

The framework reproduces standard AB physics exactly. The phase formula is the same. The topology is the same. The empirical predictions are the same. The Tonomura experimental confirmation, the flux-quantum periodicity, the gauge-invariance of the observable quantity — all reproduce standard quantum mechanics.

What's new is the answer to "why does the gauge potential have physical reality?" In standard physics, this is accepted as an empirical fact about quantum mechanics that classical mechanics fails to capture. In ED, it is the continuum reading of T17's substrate ontology: the gauge potential is the rule-type connection of the substrate, and the connection is a primitive substrate object, not an emergent abstraction. The AB effect demonstrates the connection's reality through its observable holonomy in topologically non-trivial configurations.

The cross-domain reading is also worth emphasizing. The same substrate-level topology that makes AB phases possible for electromagnetic gauge fields produces the analogous phenomena for other gauge groups. The Wu-Yang non-Abelian phase factor is the non-Abelian analogue, with the connection becoming Lie-algebra-valued. The Berry phase for parameter-space cyclic evolution is the same parallel-transport mechanism applied to a different bundle. The Aharonov-Casher phase for neutral particles with magnetic moment in electric fields is the dual structure. Each is a substrate-level instance of the same parallel-transport machinery applied to a different connection on a different bundle.

The factor that's worth emphasizing: the AB walkthrough introduces no new substrate primitive. The substrate channel topology was already in the framework's primitive inventory; T17 was already established as the substrate origin of gauge fields; DCGT was already established as the substrate-to-continuum bridge. The AB phase is what falls out when these prior structures are combined and applied to a multiply-connected substrate channel. The substrate inventory is unchanged; the structural-foundations theorem inventory does not grow — the AB phase is a downstream consequence of T17 rather than a new theorem at the same structural level.

Whether the substrate primitives themselves are right is the load-bearing empirical question, as in every walkthrough. The framework stands or falls on whether participation, bandwidth, channels, polarity, locality, rule-type, substrate channel topology, and the V1 / V5 kernels are the correct foundational concepts. The empirical exposure of the framework lives across closed sectors — soft-matter mobility, substrate-derived gravity transitions, quantum-computational ceilings, Clay-relevance results — not in the AB phase, where the framework reproduces the empirically validated standard quantum mechanics without modification.

For the AB phase specifically, the structural case is closed. The phase is the substrate-level monodromy of the rule-type connection around a non-contractible loop. The gauge-reality question is resolved by the substrate ontology: $A_\mu$ has reality because it is the continuum reading of a primitive substrate object. The topological character of the AB phase is the topological character of the substrate channel's multiple-connectivity, with the chain's accessible region excluding flux-source regions because of high local participation density. Standard quantum mechanics has been right about the AB phase since 1959; ED supplies the substrate-level account of why.

---

## 11. References

- Aharonov, Y., Bohm, D. "Significance of Electromagnetic Potentials in the Quantum Theory." *Physical Review* 115, 485–491 (1959).
- Chambers, R. G. "Shift of an Electron Interference Pattern by Enclosed Magnetic Flux." *Physical Review Letters* 5, 3–5 (1960).
- Tonomura, A., Osakabe, N., Matsuda, T., et al. "Evidence for Aharonov-Bohm Effect with Magnetic Field Completely Shielded from Electron Wave." *Physical Review Letters* 56, 792–795 (1986).
- Aharonov, Y., Casher, A. "Topological Quantum Effects for Neutral Particles." *Physical Review Letters* 53, 319–321 (1984).
- Berry, M. V. "Quantal Phase Factors Accompanying Adiabatic Changes." *Proceedings of the Royal Society A* 392, 45–57 (1984).
- Wu, T. T., Yang, C. N. "Concept of Nonintegrable Phase Factors and Global Formulation of Gauge Fields." *Physical Review D* 12, 3845–3857 (1975).
- Dirac, P. A. M. "Quantised Singularities in the Electromagnetic Field." *Proceedings of the Royal Society A* 133, 60–72 (1931).
- Nakahara, M. *Geometry, Topology and Physics.* Institute of Physics Publishing, 2nd edition, 2003.
- Proxmire, A. *Theorem 17: Gauge-Field-as-Rule-Type — The Substrate Origin of Gauge Fields and Minimal Coupling.* April 2026.
- Proxmire, A. *The Diffusion Coarse-Graining Theorem: Substrate-to-Continuum Bridge for Canonical-ED Dynamical Content.* April 2026.
- Proxmire, A. *ED-I-14: Topological Effects — Structure of Phase Without Force.* February 2026.
- Proxmire, A. *The Born Rule as a Forced Theorem of Event Density: A Gleason–Busch Reconstruction from First Principles.* April 2026.
- Proxmire, A. *Event Density: One Substrate, Three Domains.* April 2026.
- Peshkin, M., Tonomura, A. *The Aharonov-Bohm Effect.* Springer Lecture Notes in Physics 340, 1989.
- The full Event Density corpus, including all forced theorems and supporting memos, is available at https://github.com/allen-proxmire/event-density.
