# ED-PHYS-08: Physical Interpretation Framework

## ED Properties Used for Scoring

| # | Property | Source |
|---|----------|--------|
| P1 | Parabolic (diffusive) | PHYS-02 |
| P2 | Effective diffusion D_eff = D M_star | PHYS-01 |
| P3 | Effective reaction lambda = D P0 | PHYS-03 |
| P4 | Telegraph oscillation (H > 0) | PHYS-02 |
| P5 | No pattern formation | PHYS-04 |
| P6 | Non-Gaussian spreading | PHYS-05 |
| P7 | Five Lyapunov functionals | PHYS-07 |
| P8 | NOT a gradient flow | PHYS-07 |
| P9 | Unique attractor | All laws |
| P10 | Degenerate mobility (horizons) | PHYS-06 |

## Interpretation Matrix

| Domain | Match | Mismatch | Plausibility |
|--------|-------|----------|-------------|
| Population / agent density models | 8/10 | 2/10 | strong |
| Porous-medium / groundwater flow | 6/10 | 4/10 | moderate |
| Reaction-diffusion (chemical kinetics) | 6/10 | 4/10 | moderate |
| Statistical mechanics (Fokker-Planck) | 5/10 | 5/10 | weak |
| Telegraph / Cattaneo relaxation | 3/10 | 7/10 | poor |
| Thin-film / lubrication flow | 3/10 | 7/10 | poor |
| Hydrodynamic limits (coarse-grained fluid) | 3/10 | 7/10 | poor |
| Renormalisation group (RG) flow | 3/10 | 7/10 | poor |

## Top Candidate Interpretations

### Porous-medium / groundwater flow (6/10 matches)

**Governing equation:** d u/dt = div(u^m grad u)

**Matches:**

- P10_degenerate: PME mobility vanishes at u=0 (free boundary)
- P1_parabolic: PME is parabolic
- P2_diffusion: PME has effective D(u) = (m+1) u^m
- P5_no_patterns: PME does not form patterns
- P6_nonGaussian: PME produces non-Gaussian profiles (Barenblatt)
- P7_Lyapunov: PME has entropy-type Lyapunov functionals

**Mismatches:**

- P3_reaction: Pure PME has no reaction term
- P4_telegraph: PME has no global oscillator
- P8_not_gradflow: PME IS a gradient flow (Wasserstein)
- P9_attractor: PME attractor is Barenblatt, not uniform

**Notes:** Closest PDE relative (ED-Phys-38). ED = PME + penalty + participation.

### Reaction-diffusion (chemical kinetics) (6/10 matches)

**Governing equation:** d u/dt = D Lap(u) + f(u)

**Matches:**

- P1_parabolic: RD is parabolic
- P2_diffusion: RD has linear diffusion D Lap(u)
- P3_reaction: RD has reaction term f(u)
- P5_no_patterns: Monostable single-species RD has no patterns
- P7_Lyapunov: Many RD systems have Lyapunov functionals
- P9_attractor: Monostable RD has unique attractor

**Mismatches:**

- P10_degenerate: Standard RD has constant diffusion (no degeneracy)
- P4_telegraph: Standard RD has no global oscillator
- P6_nonGaussian: Linear diffusion gives Gaussian spreading
- P8_not_gradflow: Some RD are gradient flows (variational)

**Notes:** ED is a degenerate reaction-diffusion equation with penalty + participation.

### Population / agent density models (8/10 matches)

**Governing equation:** d rho/dt = div(D(rho) grad rho) + r(rho)

**Matches:**

- P10_degenerate: Crowding reduces mobility at high density
- P1_parabolic: Population models are parabolic
- P2_diffusion: Density-dependent diffusion D(rho)
- P3_reaction: Growth/death kinetics r(rho)
- P5_no_patterns: Single-species without chemotaxis has no patterns
- P6_nonGaussian: Nonlinear diffusion gives non-Gaussian fronts
- P7_Lyapunov: Population models often have Lyapunov functionals
- P9_attractor: Carrying capacity = unique steady state

**Mismatches:**

- P4_telegraph: No global oscillator in standard population models
- P8_not_gradflow: Many population models ARE gradient flows

**Notes:** Strong structural match: rho_max = carrying capacity, P = logistic penalty.

### Statistical mechanics (Fokker-Planck) (5/10 matches)

**Governing equation:** d p/dt = div(D grad p + p grad V)

**Matches:**

- P1_parabolic: FP is parabolic
- P2_diffusion: FP has diffusion D grad p
- P3_reaction: Drift p grad V acts like reaction
- P7_Lyapunov: FP has free energy Lyapunov functional
- P9_attractor: Boltzmann distribution is unique attractor

**Mismatches:**

- P10_degenerate: Standard FP has linear diffusion (no degeneracy)
- P4_telegraph: No global oscillator
- P5_no_patterns: FP has no patterns (match, but trivially)
- P6_nonGaussian: Linear FP gives Gaussian relaxation
- P8_not_gradflow: FP IS a Wasserstein gradient flow

**Notes:** Close structural relative. ED differs by degenerate mobility and participation.

## Synthesis

The ED PDE is best interpreted as a **degenerate nonlinear reaction-diffusion equation** with the following physical readings:

1. **Population/agent density** (8/10): rho is a population density with density-dependent dispersal, carrying capacity rho_max, and logistic-like penalty toward equilibrium rho_star.  This is the strongest single-domain interpretation.

2. **Porous-medium flow with reaction** (6/10): rho is a fluid density in a porous medium with degenerate permeability and a linear sink/source term.  The PME is ED's closest PDE relative.

3. **Reaction-diffusion** (6/10): rho is a chemical concentration with monostable kinetics.  The degenerate mobility is unusual but not unprecedented in biochemical models.

4. **Statistical mechanics** (5/10): rho is a probability density evolving under a modified Fokker-Planck equation.  The key mismatch is that ED is NOT a Wasserstein gradient flow.

## What ED is NOT

- **NOT a wave equation** (PHYS-02): no spatial propagation.
- **NOT a pattern-forming system** (PHYS-04): no Turing instability.
- **NOT a gradient flow** (PHYS-07): dissipative but not variational.
- **NOT quantum mechanics** (PHYS-05): classical, dissipative, no superposition principle.

## Conclusion

The ED PDE is a **degenerate parabolic reaction-diffusion equation with global feedback**.  Its natural physical domain is density-dependent transport with carrying capacity and relaxation — a mathematical framework that spans porous media, population dynamics, and coarse-grained statistical mechanics.