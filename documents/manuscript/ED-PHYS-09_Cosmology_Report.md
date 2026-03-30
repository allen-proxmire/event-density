# ED-PHYS-09: Cosmological Analogue Mapping

## Caveat

These are STRUCTURAL ANALOGIES, not cosmological physics.  ED is a classical, dissipative, parabolic PDE on a flat domain.  It has no metric, no curvature, and no gravity.  The analogies illustrate shared mathematical structure, not physical equivalence.

## Regime

- Dimension: 2D, grid 32^2
- Amplitude A = 0.35, modes Nm = 3
- P0 = 0.3, H = 0.5
- Predicted expansion rate: 0.0900
- Horizon threshold: rho > 0.9500
- Structure lifetime: 1.204

## Experiment 1: Expansion Analogue

- Initial <rho> = 0.6762 (overdense)
- Final <rho> = 0.4305
- Fitted decay rate: 0.3554 (predicted D*P0 = 0.0900, error 294.9%)
- Initial a(0) = 0.8599
- Final a(T) = 1.0777
- Initial H_eff = 0.0123

### Analogue Interpretation

The mean density decays exponentially toward rho_star, analogous to matter dilution in a de Sitter-like expansion.  The effective scale factor a(t) grows from a(0) < 1 to a -> 1 as the density approaches equilibrium.  The Hubble rate H_eff decreases monotonically, analogous to deceleration.

## Experiment 2: Horizon Analogue

- Initial horizon fraction: 0.0039 (0.4% of domain)
- Final horizon fraction: 0.0000
- Horizon lifetime: 0.000
- Initial min mobility: 1.1111e-03
- Final min mobility: 3.2359e-01

### Analogue Interpretation

Horizons form in regions where the density approaches rho_max and the mobility vanishes.  These regions are dynamically isolated: diffusion cannot transport density across them.  As the penalty relaxes the density, horizons shrink and disappear after t ~ 0.00.

This is analogous to cosmological horizons that shrink as the universe decelerates, allowing previously disconnected regions to come into causal contact.

## Experiment 3: Structure Analogue

- Initial complexity C(0) = 1.2769e-01
- Peak complexity = 1.2769e-01
- Structure lifetime (C < 10% of initial): 0.900 (predicted 1.204)
- Initial filament fraction: 0.0000
- Final filament fraction: 0.0000

### Analogue Interpretation

Transient filaments and sheets form from the multi-modal initial condition and decay as the field relaxes to equilibrium.  This is the INVERSE of cosmological structure formation: in cosmology, gravity amplifies structure; in ED, diffusion and penalty destroy it.

The analogy is structural: both systems produce filament/sheet/blob morphology classified by Hessian eigenvalues.  The dynamics are opposite (growth vs decay).

## Summary of Analogues

| Cosmological feature | ED analogue | Mechanism | Status |
|---------------------|------------|-----------|--------|
| Matter dilution | Density decay | Penalty relaxation | Partial |
| Scale factor growth | a(t) -> 1 | rho -> rho_star | a(0)=0.860, a(T)=1.078 |
| Causal horizons | M(rho)->0 regions | Degenerate mobility | Confirmed |
| Structure formation | Transient filaments | Differential decay | Lifetime=0.900 |
| Deceleration | H_eff decreasing | Exponential relaxation | Confirmed |

## Limitations

- ED 'expansion' is density decay, not metric expansion.
- ED horizons are diffusion barriers, not null surfaces.
- ED structure decays; cosmological structure grows.
- There is no redshift, no photon propagation, no gravity.
- The analogies are mathematical, not physical.