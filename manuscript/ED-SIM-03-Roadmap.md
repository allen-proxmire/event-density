# ED-SIM-03 Roadmap

ED-SIM-03 extends the second-generation platform with multi-field coupling, stochastic forcing, GPU-native solvers, adaptive grids, higher-dimensional generalisation (d=5,6), interactive visualisation, formal proof infrastructure, and an experimental bridge to physical measurements.
  Target version: 0.2.0

---

## 1. Architecture

10 components are planned:

| Component | Title | Prerequisites |
|-----------|-------|---------------|
| multi_field | Multi-Field Coupling | (none) |
| stochastic | Stochastic Forcing | (none) |
| adaptive_grid | Adaptive Mesh Refinement (AMR) | gpu_solver |
| gpu_solver | GPU-Native Solver | (none) |
| spectral_fd_hybrid | Spectral-FD Hybrid Integrator | (none) |
| high_dim | 5D/6D Generalisation | gpu_solver |
| realtime_viz | Real-Time Visualisation | (none) |
| interactive_nb | Interactive Notebooks | realtime_viz |
| formal_proofs | Formal Proof Infrastructure | (none) |
| experimental_bridge | Experimental Bridge | multi_field |

### Component Details

#### Multi-Field Coupling (`multi_field`)

Extend the single-scalar ED PDE to coupled systems: (rho_1, rho_2, ..., rho_n) with cross-mobility and cross-penalty terms.  Enables ED models of multi-component systems and field-field interaction.

**Motivation:** ED-SIM-02 evolves a single density.  Physical systems often involve coupled fields (e.g., matter + radiation, two-fluid models).  Multi-field ED is the natural extension.

**Risks:**
- Cross-coupling may break the Lyapunov structure
- Constitutive function design is non-trivial
- Computational cost scales as n^2 per coupling

**Outputs:** Multi-field solver, Cross-mobility constitutive library, Coupled invariant atlas

#### Stochastic Forcing (`stochastic`)

Add multiplicative or additive noise to the ED PDE: d rho = F[rho] dt + sigma(rho) dW.  Enables the study of fluctuation-driven phenomena, nucleation, and noise-induced transitions.

**Motivation:** The deterministic ED PDE always relaxes to rho*.  Stochastic forcing can sustain non-trivial steady states, produce intermittency, and model thermal fluctuations.

**Risks:**
- Noise + degenerate mobility may produce blow-up
- Numerical stability of stochastic integrators
- Invariant definitions need adaptation for stochastic systems

**Outputs:** Stochastic integrator (Euler-Maruyama, Milstein), Noise-aware invariant atlas, Fluctuation spectrum analysis

#### Adaptive Mesh Refinement (AMR) (`adaptive_grid`)

Replace uniform grids with locally refined meshes that concentrate resolution near horizons, filaments, and sharp gradients.

**Motivation:** 4D simulations at N=64 require 16M grid points.  AMR can achieve equivalent accuracy with 10-100x fewer points by refining only where needed.

**Risks:**
- AMR + spectral methods is non-trivial
- Load balancing on GPU
- Invariant computation on non-uniform grids

**Outputs:** AMR data structure (quadtree/octree), Refinement criteria (gradient, curvature), AMR-aware operators

#### GPU-Native Solver (`gpu_solver`)

Rewrite the core solver in JAX or CuPy for GPU execution.  All operators, integrators, and invariants run on GPU without host-device transfer.

**Motivation:** 3D and 4D simulations are memory- and compute-bound.  GPU execution provides 10-100x speedup for structured grids.

**Risks:**
- JAX ecosystem maturity
- Memory constraints for 4D arrays on consumer GPUs
- Reproducibility across hardware

**Outputs:** JAX/CuPy solver backend, GPU-resident invariant computation, Benchmark suite (CPU vs GPU)

#### Spectral-FD Hybrid Integrator (`spectral_fd_hybrid`)

Combine spectral methods (FFT/DCT) for the linear part with finite differences for the nonlinear part in a dimension-agnostic IMEX framework.

**Motivation:** ETD-RK4 is currently 2D-only.  A general IMEX hybrid would provide spectral accuracy in all dimensions while handling nonlinearity robustly.

**Risks:**
- IMEX stability at high Reynolds-like numbers
- DCT compatibility with AMR

**Outputs:** IMEX-RK integrator (ARK4/5), Spectral Laplacian for d=1..6, Nonlinear FD evaluator

#### 5D/6D Generalisation (`high_dim`)

Extend the solver and invariant atlas to d=5 and d=6.  Test the factorial complexity law and gradient dominance at higher dimensions.

**Motivation:** ED-Phys-39 predicts asymptotic behaviour for d -> infinity.  Testing at d=5,6 validates these predictions and completes the dimensional program.

**Risks:**
- Memory: N^6 at N=16 = 16M points
- Morphology classification beyond d=4 is combinatorially complex
- Visualization in d>3 requires projection

**Outputs:** 5D/6D solver, 5D/6D invariant atlas, Dimensional law verification at d=5,6

#### Real-Time Visualisation (`realtime_viz`)

Interactive 3D visualisation of ED fields using WebGL or PyVista.  Live invariant dashboards during simulation.

**Motivation:** ED-SIM-02 generates static Matplotlib figures post-run.  Real-time visualisation enables exploratory science and parameter steering.

**Risks:**
- Browser-based rendering performance
- Data transfer overhead for large 3D fields

**Outputs:** Interactive 3D field viewer, Live invariant dashboard, Animation export (GIF/MP4)

#### Interactive Notebooks (`interactive_nb`)

Jupyter notebooks with ipywidgets for parameter exploration, regime selection, and cross-framework comparison.

**Motivation:** Lower the barrier to entry for new users.  Enable rapid exploration of the parameter space and regime manifold.

**Risks:**
- Widget compatibility across Jupyter versions
- Performance for 3D/4D simulations in notebooks

**Outputs:** Parameter explorer notebook, Regime navigator notebook, Law verification dashboard

#### Formal Proof Infrastructure (`formal_proofs`)

Machine-checkable proofs for Laws 2 and 5 (derived laws) using Lean 4 or Coq.  Provide a proof skeleton for the remaining laws.

**Motivation:** ED-Phys-36 provides partial derivations.  Formal proofs elevate the architectural laws from empirical observations to mathematical theorems.

**Risks:**
- Lean/Coq formalisation of nonlinear PDE theory is immature
- Proof engineering effort is high

**Outputs:** Lean 4 proof files for Laws 2, 5, Proof sketches for Laws 1, 3, 4, 6, Formal specification of the ED axiom system

#### Experimental Bridge (`experimental_bridge`)

Map ED predictions to specific experimental observables in condensed matter, astrophysics, or quantum systems.  Design concrete falsifiable experiments.

**Motivation:** ED-Phys-38 identifies PME as the closest structural relative.  An experimental bridge would anchor ED predictions to measurable quantities in real systems.

**Risks:**
- Parameter mapping may be degenerate
- ED predictions may be too generic to distinguish from PME

**Outputs:** Prediction catalogue for thin-film experiments, Prediction catalogue for dark-matter halo profiles, Experimental design document

---

## 2. Research Questions

### Physics

**P1** [very_high]: Can the ED PDE be derived as an effective equation from a microscopic Hamiltonian via coarse-graining?
  Rationale: This would establish ED as a hydrodynamic limit of a deeper theory, analogous to Navier-Stokes from Boltzmann.
  Dependencies: (none)

**P2** [high]: What happens when two ED fields are coupled with cross-mobility terms?  Does the attractor survive?
  Rationale: Multi-field ED could model matter-radiation or dark-matter-baryon interactions.
  Dependencies: multi_field

**P3** [medium]: Does stochastic forcing produce a non-trivial steady state that is distinct from rho*?
  Rationale: Noise-sustained structure would give ED a fluctuation theory analogous to thermal equilibrium.
  Dependencies: stochastic

**P4** [very_high]: Can ED reproduce the Tully-Fisher or baryonic Tully-Fisher relation in a galactic-scale simulation?
  Rationale: A quantitative match to galaxy rotation curves would be a strong falsifiable prediction.
  Dependencies: multi_field, experimental_bridge

**P5** [high]: Does the horizon formation threshold A_crit have a physical analogue (e.g., Chandrasekhar limit, Jeans mass)?
  Rationale: Mapping A_crit to a physical threshold would anchor the horizon concept to measurable physics.
  Dependencies: experimental_bridge

### Mathematics

**M1** [very_high]: Is the attractor rho* globally unique for all initial conditions in [0, rho_max], including non-smooth data?
  Rationale: Law 1 is only partially derived.  A full proof would be a major mathematical result.
  Dependencies: formal_proofs

**M2** [high]: Does the factorial complexity law C^(d) = C^(1)/d! hold exactly, or only asymptotically?
  Rationale: ED-Phys-36 provides a structural argument.  A rigorous derivation would clarify the O(1) corrections.
  Dependencies: high_dim

**M3** [high]: Can the topological conservation law d chi/dt = 0 be proved rigorously for the degenerate ED PDE?
  Rationale: The Morse-theoretic argument assumes non-degenerate critical points.  Degeneracy near rho_max may break it.
  Dependencies: formal_proofs

**M4** [medium]: What is the basin of attraction for the sheet-filament oscillation?  Is it generic or fine-tuned?
  Rationale: Law 9 is empirical.  Understanding its basin would determine whether it is an architectural law or a parameter-dependent phenomenon.
  Dependencies: (none)

### Computation

**C1** [medium]: Can a GPU-native JAX solver achieve 100x speedup for 3D simulations at N=128?
  Rationale: This would enable large-scale 3D parameter sweeps and real-time exploration.
  Dependencies: gpu_solver

**C2** [high]: Can AMR reduce 4D computation from O(N^4) to O(N^2 log N) while preserving invariant accuracy to 1%?
  Rationale: 4D at N=64 is barely feasible.  AMR could push to N_eff=128.
  Dependencies: adaptive_grid

**C3** [medium]: Can a spectral-FD IMEX integrator be stable and accurate in d=4,5,6 with degenerate mobility?
  Rationale: ETD-RK4 is 2D-only.  A general IMEX would unify all dimensions under one integrator.
  Dependencies: spectral_fd_hybrid

### Architecture

**A1** [high]: What is the minimal extension of the ED axiom system that admits multi-field coupling?
  Rationale: P5 (single scalar field) must be relaxed.  The question is what replaces it while preserving the Lyapunov structure.
  Dependencies: multi_field

**A2** [medium]: Can the nine laws be extended to stochastic ED?  Which laws survive, which break?
  Rationale: Noise will likely break Laws 2 (monotone energy) and 6 (topology).  Understanding which laws are robust determines the stochastic architectural skeleton.
  Dependencies: stochastic

### Interpretation

**I1** [high]: Can ED be interpreted as a pilot-wave theory for a classical probability density?
  Rationale: The ED PDE resembles a nonlinear Schrodinger-like equation in the quantum-scale regime.  A pilot-wave interpretation would connect ED to de Broglie-Bohm theory.
  Dependencies: (none)

**I2** [medium]: Is the ED participation variable v(t) interpretable as a gravitational potential or a cosmological expansion rate?
  Rationale: v is the only global mode.  Mapping it to a physical quantity would anchor the non-local coupling.
  Dependencies: experimental_bridge

**I3** [very_high]: Can the ED morphological taxonomy (filament/sheet/blob) be mapped quantitatively to the cosmic web?
  Rationale: ED-Phys-37 identifies a structural analogy.  A quantitative match would be a strong validation.
  Dependencies: multi_field, experimental_bridge

---

## 3. Dependency Graph

27 nodes, 20 edges.

| Node | Kind | Prerequisites | Depth |
|------|------|---------------|-------|
| multi_field | component | (none) | 0 |
| stochastic | component | (none) | 0 |
| gpu_solver | component | (none) | 0 |
| spectral_fd_hybrid | component | (none) | 0 |
| realtime_viz | component | (none) | 0 |
| formal_proofs | component | (none) | 0 |
| P1 | question | (none) | 0 |
| M4 | question | (none) | 0 |
| I1 | question | (none) | 0 |
| experimental_bridge | component | multi_field | 1 |
| P2 | question | multi_field | 1 |
| A1 | question | multi_field | 1 |
| P3 | question | stochastic | 1 |
| A2 | question | stochastic | 1 |
| adaptive_grid | component | gpu_solver | 1 |
| high_dim | component | gpu_solver | 1 |
| C1 | question | gpu_solver | 1 |
| C3 | question | spectral_fd_hybrid | 1 |
| interactive_nb | component | realtime_viz | 1 |
| M1 | question | formal_proofs | 1 |
| M3 | question | formal_proofs | 1 |
| P4 | question | multi_field, experimental_bridge | 2 |
| P5 | question | experimental_bridge | 2 |
| I2 | question | experimental_bridge | 2 |
| I3 | question | multi_field, experimental_bridge | 2 |
| C2 | question | adaptive_grid | 2 |
| M2 | question | high_dim | 2 |

### Mermaid Diagram

```mermaid
graph TD
    multi_field[Multi-Field Coupling]
    stochastic[Stochastic Forcing]
    adaptive_grid[Adaptive Mesh Refinement (AMR)]
    gpu_solver[GPU-Native Solver]
    spectral_fd_hybrid[Spectral-FD Hybrid Integrator]
    high_dim[5D/6D Generalisation]
    realtime_viz[Real-Time Visualisation]
    interactive_nb[Interactive Notebooks]
    formal_proofs[Formal Proof Infrastructure]
    experimental_bridge[Experimental Bridge]
    P1(Can the ED PDE be derived as an effective equation...)
    P2(What happens when two ED fields are coupled with c...)
    P3(Does stochastic forcing produce a non-trivial stea...)
    P4(Can ED reproduce the Tully-Fisher or baryonic Tull...)
    P5(Does the horizon formation threshold A_crit have a...)
    M1(Is the attractor rho* globally unique for all init...)
    M2(Does the factorial complexity law C^(d) = C^(1)/d!...)
    M3(Can the topological conservation law d chi/dt = 0 ...)
    M4(What is the basin of attraction for the sheet-fila...)
    C1(Can a GPU-native JAX solver achieve 100x speedup f...)
    C2(Can AMR reduce 4D computation from O(N^4) to O(N^2...)
    C3(Can a spectral-FD IMEX integrator be stable and ac...)
    A1(What is the minimal extension of the ED axiom syst...)
    A2(Can the nine laws be extended to stochastic ED?  W...)
    I1(Can ED be interpreted as a pilot-wave theory for a...)
    I2(Is the ED participation variable v(t) interpretabl...)
    I3(Can the ED morphological taxonomy (filament/sheet/...)
    gpu_solver --> adaptive_grid
    gpu_solver --> high_dim
    realtime_viz --> interactive_nb
    multi_field --> experimental_bridge
    multi_field --> P2
    stochastic --> P3
    multi_field --> P4
    experimental_bridge --> P4
    experimental_bridge --> P5
    formal_proofs --> M1
    high_dim --> M2
    formal_proofs --> M3
    gpu_solver --> C1
    adaptive_grid --> C2
    spectral_fd_hybrid --> C3
    multi_field --> A1
    stochastic --> A2
    experimental_bridge --> I2
    multi_field --> I3
    experimental_bridge --> I3
```

---

## 4. Milestone Plan

| Phase | Title | Tasks | Key outputs |
|-------|-------|-------|-------------|
| A | Foundations | 4 | JAX solver backend; IMEX-RK4 integrator; Multi-field solver; Euler-Maruyama inte |
| B | Engineering | 4 | AMR data structure; 5D solver; Interactive 3D viewer; Parameter explorer |
| C | Physics | 4 | Attractor existence proof/evidence; Steady-state distribution; Prediction catalo |
| D | Mathematics | 4 | Lean 4 proof file; Lean 4 proof file; Proof sketch document; Derivation with exp |
| E | Documentation and Manuscript | 4 | Manuscript draft; docs/ updates; run_all_v3.py; pyproject.toml v0.2.0 |

### Phase A: Foundations

Establish the core infrastructure for ED-SIM-03: GPU backend, spectral-FD hybrid integrator, and multi-field coupling framework.

- **A1: GPU-native solver backend (JAX/CuPy)** (gpu_solver)
  Outputs: JAX solver backend, CPU vs GPU benchmark
  Acceptance: 3D simulation at N=64 runs on GPU with <5% invariant error
- **A2: Spectral-FD IMEX integrator for d=1..4** (spectral_fd_hybrid)
  Outputs: IMEX-RK4 integrator, Stability analysis
  Acceptance: ETD-RK4 accuracy in d=2,3,4 with IMEX framework
- **A3: Multi-field coupling framework** (multi_field)
  Outputs: Multi-field solver, Cross-mobility library
  Acceptance: 2-field simulation converges to coupled attractor
- **A4: Stochastic forcing module** (stochastic)
  Outputs: Euler-Maruyama integrator, Noise-aware atlas
  Acceptance: Stochastic simulation matches expected fluctuation spectrum

### Phase B: Engineering

Scale the platform: adaptive grids, higher dimensions, and real-time visualisation.

- **B1: Adaptive mesh refinement (AMR)** (adaptive_grid)
  Outputs: AMR data structure, Refinement criteria
  Acceptance: 4D simulation with AMR achieves 10x cost reduction at 1% error
- **B2: 5D/6D solver and invariant atlas** (high_dim)
  Outputs: 5D solver, 6D solver, Dimensional law verification
  Acceptance: Factorial law verified at d=5,6 within 10%
- **B3: Real-time 3D visualisation** (realtime_viz)
  Outputs: Interactive 3D viewer, Live dashboard
  Acceptance: 3D field at N=64 rendered at >10 fps
- **B4: Interactive parameter explorer notebooks** (interactive_nb)
  Outputs: Parameter explorer, Regime navigator
  Acceptance: Notebooks run without errors in JupyterLab

### Phase C: Physics

Address the core physics questions: multi-field attractor, stochastic steady states, and experimental bridge.

- **C1: Multi-field attractor analysis** (multi_field)
  Outputs: Attractor existence proof/evidence, Coupled invariant atlas
  Acceptance: 2-field system converges for 10+ parameter sets
- **C2: Stochastic steady-state characterisation** (stochastic)
  Outputs: Steady-state distribution, Fluctuation spectrum
  Acceptance: Non-trivial steady state identified and characterised
- **C3: Experimental bridge: thin-film predictions** (experimental_bridge)
  Outputs: Prediction catalogue, Experimental design document
  Acceptance: 3 falsifiable predictions with quantitative values
- **C4: Horizon threshold physical mapping** (experimental_bridge)
  Outputs: A_crit physical analogue table
  Acceptance: A_crit mapped to at least 2 physical thresholds

### Phase D: Mathematics

Formal proofs, rigorous derivations, and mathematical extensions of the architectural laws.

- **D1: Formal proof of Law 2 (energy monotonicity)** (formal_proofs)
  Outputs: Lean 4 proof file
  Acceptance: Proof compiles without errors in Lean 4
- **D2: Formal proof of Law 5 (gradient dominance)** (formal_proofs)
  Outputs: Lean 4 proof file
  Acceptance: Proof compiles without errors in Lean 4
- **D3: Attractor uniqueness proof sketch** (formal_proofs)
  Outputs: Proof sketch document
  Acceptance: Sketch identifies all gaps and required lemmas
- **D4: Factorial law rigorous derivation** (formal_proofs)
  Outputs: Derivation with explicit error bounds
  Acceptance: Error bounds consistent with d=5,6 numerics

### Phase E: Documentation and Manuscript

Write the ED-SIM-03 paper, update documentation, and produce the reproducibility certificate.

- **E1: ED-SIM-03 paper: architecture + results** (interactive_nb)
  Outputs: Manuscript draft
  Acceptance: Complete draft with all figures and tables
- **E2: Updated documentation for all new modules** (interactive_nb)
  Outputs: docs/ updates
  Acceptance: All new modules documented with examples
- **E3: Extended reproducibility pipeline (v3)** (interactive_nb)
  Outputs: run_all_v3.py, Certificate v3
  Acceptance: All phases pass on CI with GPU and CPU
- **E4: Release engineering (v0.2.0)** (interactive_nb)
  Outputs: pyproject.toml v0.2.0, CHANGELOG update
  Acceptance: pip install succeeds; CLI runs all new commands

---

## 5. Manuscript Outline

# ED-SIM-03: A Multi-Scale Simulation Platform for Event Density

## 1  Introduction

Motivate the extension from ED-SIM-02 to ED-SIM-03.  Summarise the nine architectural laws and their verification in d=1-4.  State the goals: multi-field coupling, stochastic forcing, GPU solvers, higher dimensions, experimental bridge.

## 2  Architecture

Present the ED-SIM-03 component architecture.  Describe each of the 10 components, their motivations, and their inter-dependencies.  Show the dependency graph.
  Figures: Dependency graph (Mermaid or TikZ)
  Tables: Component summary table

## 3  Multi-Field ED

Define the multi-field extension: coupled (rho_1, rho_2) system with cross-mobility.  Derive the coupled Lyapunov functional.  Present attractor existence results.
  Figures: Coupled field evolution, Cross-mobility landscape

## 4  Stochastic ED

Add multiplicative noise to the ED PDE.  Derive the modified Lyapunov inequality.  Characterise the noise-sustained steady state.  Identify which of the nine laws survive.
  Figures: Fluctuation spectrum, Law survival table

## 5  Computational Extensions

GPU-native solver benchmarks.  Spectral-FD IMEX integrator validation.  Adaptive mesh refinement results.  5D/6D dimensional law tests.
  Figures: GPU speedup plot, AMR cost reduction, d=5,6 complexity
  Tables: Benchmark table (CPU vs GPU vs AMR)

## 6  Higher-Dimensional Results

Present the factorial law at d=5,6.  Verify R_grad predictions.  Characterise 5D/6D morphology.  Test horizon suppression.
  Figures: Complexity vs d (1-6), R_grad vs d, Morphology fractions vs d

## 7  Experimental Bridge

Map ED predictions to thin-film experiments and galactic rotation curves.  Present the prediction catalogue with quantitative values and error bars.
  Tables: Prediction catalogue

## 8  Formal Proofs

Present the Lean 4 proofs of Laws 2 and 5.  Summarise the proof sketch for Law 1.  Discuss the formal specification of the ED axiom system.

## 9  Discussion

Assess the state of the ED programme.  What has been established, what remains open.  Compare to the cross-framework analysis of ED-Phys-38.  Discuss the experimental falsifiability of ED predictions.

## 10  Future Work

Identify the open questions that ED-SIM-04 would address: full coarse-graining derivation, quantum-classical bridge, cosmological-scale validation, and formal proof completion.

---

## 6. Summary

ED-SIM-03 comprises 10 components, 17 research questions, 20 dependencies, and 5 development phases.

The closest framework (statistical mechanics, score 12/15) provides the starting point for the experimental bridge.  The seven unique ED features drive the core research agenda.

This roadmap is auto-generated by `edsim.roadmap.generator` and can be updated as components are completed.