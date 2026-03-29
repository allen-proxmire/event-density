# Cross-Framework Comparison: Event Density

This report compares the Event Density (ED) framework to six established theoretical frameworks along five structural axes: ontology, primitives, dynamics, invariants, and epistemology.

All comparisons are structural, not rhetorical.  No claims of equivalence or superiority are made.


## Framework Profiles

### Causal Set Theory

**Ontology:** Discrete partial order of events; No continuous manifold
**Primitives:** Events (elements of the causet); Causal order (partial order relation); Valence (local connectivity)
**Dynamics:** Classical sequential growth (Rideout-Sorkin); Stochastic element birth with causal constraints
**Invariants:** Causal diamond volumes (Myrheim-Meyer dimension); Order-interval counts; Benincasa-Dowker action (discrete Einstein-Hilbert)
**Epistemology:** Causal relations between events; Spacetime dimension (from order statistics); Discrete geodesic distance
**Notes:** Fundamentally discrete and Lorentzian.  No density field.  Dynamics is birth-process, not flow.

### Entropic Gravity (Verlinde)

**Ontology:** Holographic screens encoding information; Entropy as the fundamental quantity
**Primitives:** Entropy S; Temperature T; Holographic screen area A
**Dynamics:** F = T dS/dx (entropic force law); Equipartition: E = (1/2) N k_B T
**Invariants:** Total energy (first law); Entropy non-decrease (second law); Holographic bound (Bekenstein)
**Epistemology:** Gravitational acceleration; Temperature of holographic screens; Entropy of horizons
**Notes:** Gravity from thermodynamics.  No scalar field evolution.  Structural similarity to ED via entropy gradients.

### Constructor Theory (Deutsch-Marletto)

**Ontology:** Substrates (physical systems); Constructors (agents of transformation)
**Primitives:** Task T: input state -> output state; Constructor C: enables T without net change to C; Possibility/impossibility as fundamental
**Dynamics:** No evolution equation; Counterfactual structure: which tasks are possible
**Invariants:** Constructor invariance (C is unchanged after performing T); Interoperability (composability of tasks); Information conservation (in reversible tasks)
**Epistemology:** Which transformations are possible; Which are impossible and why; Composition of tasks
**Notes:** Meta-theory about possibility, not dynamics.  No PDE, no density field, no time evolution.  Structural parallel: ED's axioms constrain what dynamics are possible.

### Classical Hydrodynamics (Navier-Stokes)

**Ontology:** Continuous fluid (density, velocity, pressure fields); Newtonian spacetime
**Primitives:** Density rho(x,t); Velocity u(x,t); Pressure p(x,t)
**Dynamics:** Continuity: partial_t rho + div(rho u) = 0; Navier-Stokes: rho (partial_t u + u.grad u) = -grad p + nu laplacian u
**Invariants:** Mass (continuity equation); Momentum (Navier-Stokes); Energy (Bernoulli / energy equation)
**Epistemology:** Velocity fields (PIV, LDV); Pressure (manometry); Density (schlieren, interferometry)
**Notes:** Vector field dynamics (velocity).  ED is scalar (density only).  Hydrodynamics has advection; ED has diffusion + penalty.

### Statistical Mechanics (Equilibrium + Non-equilibrium)

**Ontology:** Microstates (phase space configurations); Macrostates (thermodynamic variables)
**Primitives:** Hamiltonian H(q, p); Phase space distribution f(q, p, t); Temperature T, entropy S, free energy F
**Dynamics:** Liouville equation: partial_t f = {H, f}; Boltzmann equation: partial_t f + v.grad f = C[f]
**Invariants:** Energy (Hamiltonian conservation); Entropy non-decrease (H-theorem); Free energy decrease (canonical ensemble)
**Epistemology:** Thermodynamic observables (T, P, S, F); Correlation functions; Response functions (susceptibility)
**Notes:** Closest established framework to ED's gradient-flow structure.  Fokker-Planck shares the diffusion + drift architecture.  ED adds degenerate mobility and participation coupling.

### Quantum Foundations (Operational / Information-theoretic)

**Ontology:** Hilbert space states |psi>; Observables (self-adjoint operators)
**Primitives:** State vector |psi> in H; Unitary evolution U(t); Born rule: P(a) = |<a|psi>|^2
**Dynamics:** Schrodinger equation: i hbar partial_t |psi> = H |psi>; von Neumann equation: partial_t rho = -i/hbar [H, rho]
**Invariants:** Unitarity (norm conservation); Trace preservation (density matrix); von Neumann entropy (constant under unitary evolution)
**Epistemology:** Measurement outcomes (discrete); Expectation values <A>; Transition probabilities
**Notes:** Linear, unitary, complex Hilbert space dynamics.  ED is nonlinear, dissipative, real scalar field.  Structural parallel: density matrix rho ~ ED density field rho.

### Event Density (ED)

**Ontology:** Scalar density field rho(x,t) on bounded domain; Global participation variable v(t)
**Primitives:** Density rho(x,t) in [0, rho_max]; Participation v(t) (scalar); Mobility M(rho) = M0 (rho_max - rho)^beta
**Dynamics:** partial_t rho = D [M(rho) laplacian(rho) + M'(rho)|grad rho|^2 - P(rho)] + H v; dot{v} = (1/tau)(bar{F} - zeta v)
**Invariants:** Law 1: Unique attractor; Law 2: Monotone energy decay; Law 3: Spectral concentration
**Epistemology:** Lyapunov energy E[rho]; ED-complexity C[rho] = int |grad rho|^2 dV; Spectral entropy H = -sum p_k log p_k
**Notes:** Scalar, nonlinear, dissipative, parabolic PDE with degenerate mobility and global participation coupling.  Nine architectural laws.  Verified in d=1,2,3,4.


## Comparison Matrix

Overlap scores: 0 = none, 1 = weak, 2 = moderate, 3 = strong.

| Framework | ontology | primitives | dynamics | invariants | epistemology | Total |
|---|---|---|---|---|---|---|
| causal_sets | 1 | 0 | 0 | 1 | 1 | 3 |
| entropic_gravity | 2 | 1 | 1 | 2 | 1 | 7 |
| constructor_theory | 1 | 0 | 0 | 1 | 0 | 2 |
| hydrodynamics | 2 | 2 | 2 | 2 | 2 | 10 |
| statistical_mechanics | 2 | 2 | 3 | 3 | 2 | 12 |
| quantum_foundations | 1 | 1 | 1 | 1 | 1 | 5 |


## Detailed Comparison

### causal_sets

**dynamics** (score 0): Causal sets: stochastic birth process.  ED: deterministic PDE.  Fundamentally different update rules.

**epistemology** (score 1): Both produce dimensional quantities.  Causal sets measure causal structure; ED measures density, gradients, spectra.

**invariants** (score 1): Both have volume-like invariants (diamond volumes vs mass).  Causal sets lack dissipation channels and spectral entropy.

**ontology** (score 1): Both start from events.  Causal sets use discrete partial orders; ED uses a continuous scalar field.  No continuous manifold in causal sets.

**primitives** (score 0): Causal sets: discrete elements + causal order.  ED: continuous density + mobility + penalty.  No structural overlap.

### constructor_theory

**dynamics** (score 0): Constructor theory has no evolution equation.  ED is defined by a PDE.  Fundamentally different.

**epistemology** (score 0): Constructor theory: which tasks are possible.  ED: quantitative field observables.  No overlap.

**invariants** (score 1): Constructor theory: constructor invariance, composability.  ED: Lyapunov energy, mass.  Shared: invariance under transformation, but different mathematical objects.

**ontology** (score 1): Constructor theory: tasks and possibility.  ED: density and flow.  Shared: both constrain what dynamics can occur via axioms.

**primitives** (score 0): Constructor theory: tasks, constructors.  ED: rho, M, P.  No structural overlap in primitives.

### entropic_gravity

**dynamics** (score 1): Entropic gravity: F = T dS/dx.  ED: gradient flow with Lyapunov functional.  Both are driven by entropy/energy gradients, but ED has a full PDE while entropic gravity has a force law.

**epistemology** (score 1): Entropic gravity: gravitational acceleration, horizon temperature.  ED: density field, gradients, spectra, topology.

**invariants** (score 2): Both have entropy non-decrease and energy conservation.  ED adds dissipation channel decomposition, spectral entropy, morphological invariants.

**ontology** (score 2): Both treat entropy as fundamental.  Entropic gravity uses holographic screens; ED uses a density field.  Shared: entropy gradients drive dynamics.

**primitives** (score 1): Entropic gravity: S, T, A.  ED: rho, M, P.  Shared concept of entropy, but different mathematical objects.

### hydrodynamics

**dynamics** (score 2): Both are parabolic PDEs with diffusion.  Navier-Stokes has advection (nonlinear transport); ED has degenerate mobility and penalty relaxation.  Shared: Laplacian smoothing.

**epistemology** (score 2): Both produce density fields, correlation functions, spectra.  Hydrodynamics adds velocity and pressure fields.

**invariants** (score 2): Both conserve mass.  Hydrodynamics conserves momentum and energy; ED has monotone energy decay (dissipative, not conservative).  Shared: mass conservation.  Different: energy treatment.

**ontology** (score 2): Both describe continuous fields on bounded domains.  Hydrodynamics has vector fields (velocity); ED is scalar only.

**primitives** (score 2): Both have density rho(x,t) as a primary field.  Hydrodynamics adds velocity and pressure; ED adds mobility, penalty, and participation.

### quantum_foundations

**dynamics** (score 1): Schrodinger is linear and unitary; ED is nonlinear and dissipative.  Both are second-order in space.  Shared: diffusion-like Laplacian.

**epistemology** (score 1): Quantum: measurement outcomes, expectation values.  ED: field observables, invariant atlas.  Different measurement theories.

**invariants** (score 1): Quantum: unitarity, norm, von Neumann entropy (constant).  ED: energy monotone, spectral entropy (decreasing).  Opposite entropy behaviour (constant vs decreasing).

**ontology** (score 1): Quantum: Hilbert space states.  ED: scalar density field.  Shared: density matrix rho ~ ED density rho (structural analogy).

**primitives** (score 1): Quantum: |psi>, H, Born rule.  ED: rho, M, P.  Shared: density-like primary object.

### statistical_mechanics

**dynamics** (score 3): Fokker-Planck equation is the closest structural match to ED.  Both: diffusion + drift/penalty.  Shared: gradient-flow structure.  Difference: ED has degenerate mobility and participation coupling.

**epistemology** (score 2): Both produce correlation functions, fluctuation spectra, thermodynamic-like observables.  StatMech adds response functions.

**invariants** (score 3): Both have entropy (spectral/Boltzmann), energy (Lyapunov/free energy), mass/probability conservation.  Shared: H-theorem ~ energy monotonicity.  ED adds morphological invariants and dissipation channels.

**ontology** (score 2): Both describe distributions evolving toward equilibrium.  StatMech uses phase-space distributions; ED uses a spatial density.

**primitives** (score 2): Both have density/distribution as primary.  StatMech has Hamiltonian and temperature; ED has mobility and penalty.  Shared: state-dependent diffusion.


## Structural Overlaps (score >= 2)

- **statistical_mechanics / dynamics** (score 3): Fokker-Planck equation is the closest structural match to ED.  Both: diffusion + drift/penalty.  Shared: gradient-flow structure.  Difference: ED has degenerate mobility and participation coupling.
- **statistical_mechanics / invariants** (score 3): Both have entropy (spectral/Boltzmann), energy (Lyapunov/free energy), mass/probability conservation.  Shared: H-theorem ~ energy monotonicity.  ED adds morphological invariants and dissipation channels.
- **entropic_gravity / invariants** (score 2): Both have entropy non-decrease and energy conservation.  ED adds dissipation channel decomposition, spectral entropy, morphological invariants.
- **entropic_gravity / ontology** (score 2): Both treat entropy as fundamental.  Entropic gravity uses holographic screens; ED uses a density field.  Shared: entropy gradients drive dynamics.
- **hydrodynamics / dynamics** (score 2): Both are parabolic PDEs with diffusion.  Navier-Stokes has advection (nonlinear transport); ED has degenerate mobility and penalty relaxation.  Shared: Laplacian smoothing.
- **hydrodynamics / epistemology** (score 2): Both produce density fields, correlation functions, spectra.  Hydrodynamics adds velocity and pressure fields.
- **hydrodynamics / invariants** (score 2): Both conserve mass.  Hydrodynamics conserves momentum and energy; ED has monotone energy decay (dissipative, not conservative).  Shared: mass conservation.  Different: energy treatment.
- **hydrodynamics / ontology** (score 2): Both describe continuous fields on bounded domains.  Hydrodynamics has vector fields (velocity); ED is scalar only.
- **hydrodynamics / primitives** (score 2): Both have density rho(x,t) as a primary field.  Hydrodynamics adds velocity and pressure; ED adds mobility, penalty, and participation.
- **statistical_mechanics / epistemology** (score 2): Both produce correlation functions, fluctuation spectra, thermodynamic-like observables.  StatMech adds response functions.
- **statistical_mechanics / ontology** (score 2): Both describe distributions evolving toward equilibrium.  StatMech uses phase-space distributions; ED uses a spatial density.
- **statistical_mechanics / primitives** (score 2): Both have density/distribution as primary.  StatMech has Hamiltonian and temperature; ED has mobility and penalty.  Shared: state-dependent diffusion.


## Structural Divergences (score <= 1)

- **causal_sets / dynamics:** Causal sets: stochastic birth process.  ED: deterministic PDE.  Fundamentally different update rules.
- **causal_sets / epistemology:** Both produce dimensional quantities.  Causal sets measure causal structure; ED measures density, gradients, spectra.
- **causal_sets / invariants:** Both have volume-like invariants (diamond volumes vs mass).  Causal sets lack dissipation channels and spectral entropy.
- **causal_sets / ontology:** Both start from events.  Causal sets use discrete partial orders; ED uses a continuous scalar field.  No continuous manifold in causal sets.
- **causal_sets / primitives:** Causal sets: discrete elements + causal order.  ED: continuous density + mobility + penalty.  No structural overlap.
- **constructor_theory / dynamics:** Constructor theory has no evolution equation.  ED is defined by a PDE.  Fundamentally different.
- **constructor_theory / epistemology:** Constructor theory: which tasks are possible.  ED: quantitative field observables.  No overlap.
- **constructor_theory / invariants:** Constructor theory: constructor invariance, composability.  ED: Lyapunov energy, mass.  Shared: invariance under transformation, but different mathematical objects.
- **constructor_theory / ontology:** Constructor theory: tasks and possibility.  ED: density and flow.  Shared: both constrain what dynamics can occur via axioms.
- **constructor_theory / primitives:** Constructor theory: tasks, constructors.  ED: rho, M, P.  No structural overlap in primitives.


## Features Unique to ED

The following features are present in ED and absent from all comparison frameworks:

**1. Penalty-driven unique attractor (Law 1)**
  ED possesses a single globally attracting equilibrium rho = rho* enforced by the penalty P(rho).  No comparison framework has this monostable, penalty-driven relaxation.

**2. Participation coupling**
  The global variable v(t) driven by the domain-averaged operator introduces non-local feedback.  No comparison framework has an analogous global mode.

**3. Factorial complexity dilution (Law 4)**
  C^(d) = C^(1)/d! is specific to the ED constitutive functions and isotropic Neumann eigenbasis.  Not observed in any comparison framework.

**4. Gradient-dissipation dominance law (Law 5)**
  R_grad = d*pi^2 / (d*pi^2 + P0^2/M*) is derived from the specific ED architecture.  No comparison framework has an analogous dissipation-ratio formula.

**5. Degenerate-mobility horizons (Law 7)**
  Horizons form where M(rho) -> 0, creating dynamically isolated regions.  While PME has free boundaries, the horizon-threshold scaling with dimension is unique to ED.

**6. Sheet-filament oscillation (Law 9)**
  Oscillatory morphological exchange between sheets and filaments during the transient is unique to ED in d >= 3.

**7. Nine architectural laws as a unified package**
  No comparison framework has a comparable set of nine interlocking laws governing attractor, energy, spectrum, dissipation, topology, and morphology simultaneously.


## Proximity Ranking

Frameworks ranked by total overlap score with ED:

| Rank | Framework | Total score |
|------|-----------|-------------|
| 1 | statistical_mechanics | 12 |
| 2 | hydrodynamics | 10 |
| 3 | entropic_gravity | 7 |
| 4 | quantum_foundations | 5 |
| 5 | causal_sets | 3 |
| 6 | constructor_theory | 2 |


## Summary

**Closest framework:** Statistical Mechanics (Fokker-Planck).  Shared gradient-flow structure, entropy non-decrease, and correlation functions.  Key difference: ED has degenerate mobility and participation coupling.

**Most distant:** Constructor Theory and Causal Sets.  Fundamentally different mathematical objects (tasks vs PDE, discrete vs continuous).

**Irreducible ED core:** Seven features not shared by any comparison framework define ED as a distinct mathematical architecture.