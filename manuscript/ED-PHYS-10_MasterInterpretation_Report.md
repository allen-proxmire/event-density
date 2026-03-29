# ED-PHYS-10: Master Interpretation and Synthesis

## Mathematical Identity

Quasilinear degenerate parabolic PDE with monostable penalty and global scalar feedback.

## Physical Identity

Density-dependent transport with carrying capacity, relaxation toward equilibrium, and global feedback.

## Experimental Programme Summary

| # | Experiment | Key Result | Accuracy |
|---|-----------|------------|----------|
| 1 | Diffusion limit | D_eff = D * M_star with 7.5% accuracy | 7.5% |
| 2 | Wave/telegraph limit | Telegraph oscillation omega = 0.0% error; no spatial waves | omega: 0.0%, sigma(k): 0.1-0.8% |
| 3 | Reaction limit | lambda = D * P0 with 0.03% accuracy, perfect symmetry | 0.03% |
| 4 | Pattern formation | No instability: all sigma_k < 0 for all k | Decisive negative |
| 5 | Quantum-like regime | Non-Gaussian profiles, nonlinear superposition breakdown | Qualitative |
| 6 | Phase diagram | 5 phases: telegraph (69%), diffusion (14%), transient (8%), quantum-like (6%), reaction (3%) | 64-point grid, 6 validated |
| 7 | Energy/Lyapunov structure | 5 simultaneous Lyapunov functionals; NOT a gradient flow (995% residual); Boltzmann entropy increases | Machine precision for monotonicity |
| 8 | Physical interpretation | Population/agent density is strongest match (8/10) | Scoring matrix, 8 domains |
| 9 | Cosmological analogues | All 5 structural analogues confirmed: expansion, horizons, structure, deceleration, scale factor | Qualitative confirmation |

## Universality Class

**Degenerate parabolic reaction-diffusion with global feedback**

### Defining Properties

- Second-order quasilinear parabolic
- Degenerate mobility M(rho) -> 0 at capacity bound
- Monostable linear penalty (unique attractor)
- Global scalar feedback (participation variable v)
- Five simultaneous Lyapunov functionals (H=0)
- No pattern formation (unconditionally stable)

### Nearest Relatives

- **Porous-medium equation:** Identical principal operator
- **Monostable reaction-diffusion:** Same diffusion + penalty structure
- **Population density with crowding:** 8/10 property match
- **Fokker-Planck:** Gradient-flow relative, differs by degeneracy

### Distinguishing Features

- Participation coupling v(t) — no other comparison PDE has this
- Telegraph oscillation of the k=0 mode
- Five simultaneous Lyapunov functionals
- NOT a gradient flow despite being dissipative
- Degenerate mobility creating horizon-like free boundaries

## What ED Is

The ED PDE is a degenerate parabolic reaction-diffusion equation with global feedback.  Its natural interpretation is as a model of DENSITY-DEPENDENT TRANSPORT WITH CARRYING CAPACITY:

- rho(x,t) is a density field (population, concentration, probability)
- M(rho) = M0 (rho_max - rho)^beta is crowding-reduced mobility
- P(rho) = P0 (rho - rho*) is a restoring force toward equilibrium
- v(t) is a global feedback variable (resource, environment)
- rho_max is the carrying capacity / packing limit

This framework is mathematically unique: no other PDE in the comparison set (PME, AC, CH, FP, TFE, MCF) combines all five of ED's distinguishing features (degenerate mobility, monostable penalty, participation coupling, five Lyapunov functionals, non-gradient-flow dissipation).

## What ED Is Not

### Not Quantum

ED is classical, dissipative, and parabolic.  It has no Planck constant, no superposition principle, no entanglement, and no measurement problem.  The non-Gaussian spreading is a porous-medium effect, not a quantum signature.

### Not Hydrodynamic

ED evolves a scalar density, not a velocity field.  There is no advection, no Reynolds number, no turbulence.  The participation variable v(t) is a global scalar, not a spatially resolved velocity.

### Not Thermodynamic

ED does not maximise entropy.  Boltzmann entropy increases but is not a Lyapunov functional.  ED is not a detailed-balance system and cannot be derived from a partition function.

### Not Variational

ED possesses five Lyapunov functionals but is NOT a gradient flow of any of them.  The operator residual between ED and the gradient flow of its Lyapunov functional is ~995%.  ED is dissipative but not variational.

### Not Relativistic

ED has no metric tensor, no curvature tensor, no geodesics, no Lorentz invariance.  The cosmological analogues are structural (shared PDE features), not physical (no gravity).

## Structural Analogues

### Cosmological expansion

- **Mechanism:** Penalty-driven density decay
- **Quality:** Strong (exponential decay matches qualitatively)
- **Caveat:** No metric, no curvature, not physical expansion

### Causal horizons

- **Mechanism:** Degenerate mobility M -> 0
- **Quality:** Strong (regions dynamically isolated)
- **Caveat:** Diffusion barrier, not null surface

### Cosmic web

- **Mechanism:** Hessian eigenvalue morphology
- **Quality:** Moderate (filament/sheet/blob taxonomy matches)
- **Caveat:** ED structure decays; cosmic structure grows

### Quantum spreading

- **Mechanism:** Density-dependent mobility
- **Quality:** Weak (non-Gaussian profiles)
- **Caveat:** Classical nonlinear diffusion, not quantum

### Telegraph communication

- **Mechanism:** Participation coupling
- **Quality:** Strong (exact telegraph equation for k=0 mode)
- **Caveat:** Only the uniform mode oscillates

## Limitations

- No experimental validation against physical data.
- Constitutive functions (M, P) are postulated, not derived.
- No microscopic derivation from statistical mechanics.
- Deterministic only: no noise term.
- Single scalar field: no multi-component coupling.
- The cosmological analogues are structural, not physical.
- The quantum-like signatures are classical nonlinear effects.

## Open Questions

- Can ED be derived as a hydrodynamic limit of a microscopic model?
- What physical system has exactly the ED constitutive structure?
- Does stochastic ED (with noise) produce qualitatively new phenomena?
- Can the participation coupling be given a thermodynamic interpretation?
- Do the five Lyapunov functionals have independent physical meanings?
- Is there a natural generalisation of ED to multi-field coupling?
- Can the cosmological analogues be sharpened to quantitative predictions?

## Closing Statement

The Event Density PDE is a mathematically well-defined object whose structure has been characterised across nine experiments.  It is a degenerate parabolic reaction-diffusion equation with global feedback — the simplest PDE that simultaneously exhibits degenerate mobility, monostable penalty, five Lyapunov functionals, telegraph-like oscillation, and transient morphological structure.  Its natural physical domain is density-dependent transport with carrying capacity.  Its structural analogies to cosmology, statistical mechanics, and population dynamics are mathematically precise but physically non-committal.  The framework is complete, reproducible, and falsifiable.