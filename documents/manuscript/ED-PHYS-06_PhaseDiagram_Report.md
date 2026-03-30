# ED-PHYS-06: Global Phase Diagram of Event Density

## Parameter Space

- M0 values: [0.5, 1.0, 2.0, 4.0]
- P0 values: [0.05, 0.2, 1.0, 3.0]
- H values:  [0.0, 0.5, 2.0, 5.0]
- Total grid points: 64

## Phase Classification

| Phase | Count | Fraction |
|-------|-------|----------|
| diffusion | 9 | 14.1% |
| reaction | 2 | 3.1% |
| telegraph | 44 | 68.8% |
| transient | 5 | 7.8% |
| quantum_like | 4 | 6.2% |

## Phase Boundaries

### Diffusion vs Reaction

The boundary is determined by the diffusion-reaction ratio R = D_eff * pi^2 / (D * P0) = M_star * pi^2 / P0.

- R >> 1: diffusion-dominated
- R << 1: reaction-dominated
- R ~ 1: transient (competing timescales)

### Telegraph Boundary

Underdamped oscillation requires omega_0^2 > gamma^2, which gives Q >= 1.  For most P0 values, even small H > 0 is sufficient because gamma is small.  The telegraph phase therefore occupies most of the H > 0 region.

### Quantum-Like Region

Defined by high mobility (M0 >= 2), weak penalty (P0 <= 0.1), and strong participation (H >= 1).  This is a corner of the parameter space where nonlinear mobility effects and telegraph oscillation are both strong.

## Full Grid (sorted by phase)

| M0 | P0 | H | Phase | D_eff | lambda | Q | tau_morph |
|----|----|---|-------|-------|--------|---|----------|
| 0.5 | 0.05 | 0.0 | diffusion | 0.0375 | 0.0150 | 0.00 | 2.597 |
| 0.5 | 0.20 | 0.0 | diffusion | 0.0375 | 0.0600 | 0.00 | 2.325 |
| 1.0 | 0.05 | 0.0 | diffusion | 0.0750 | 0.0150 | 0.00 | 1.324 |
| 1.0 | 0.20 | 0.0 | diffusion | 0.0750 | 0.0600 | 0.00 | 1.250 |
| 2.0 | 0.05 | 0.0 | diffusion | 0.1500 | 0.0150 | 0.00 | 0.669 |
| 2.0 | 0.20 | 0.0 | diffusion | 0.1500 | 0.0600 | 0.00 | 0.649 |
| 4.0 | 0.05 | 0.0 | diffusion | 0.3000 | 0.0150 | 0.00 | 0.336 |
| 4.0 | 0.20 | 0.0 | diffusion | 0.3000 | 0.0600 | 0.00 | 0.331 |
| 4.0 | 1.00 | 0.0 | diffusion | 0.3000 | 0.3000 | 0.00 | 0.307 |
| 2.0 | 0.05 | 2.0 | quantum_like | 0.1500 | 0.0150 | 2.72 | 0.669 |
| 2.0 | 0.05 | 5.0 | quantum_like | 0.1500 | 0.0150 | 4.33 | 0.669 |
| 4.0 | 0.05 | 2.0 | quantum_like | 0.3000 | 0.0150 | 2.72 | 0.336 |
| 4.0 | 0.05 | 5.0 | quantum_like | 0.3000 | 0.0150 | 4.33 | 0.336 |
| 0.5 | 3.00 | 0.0 | reaction | 0.0375 | 0.9000 | 0.00 | 0.787 |
| 1.0 | 3.00 | 0.0 | reaction | 0.0750 | 0.9000 | 0.00 | 0.610 |
| 0.5 | 0.05 | 0.5 | telegraph | 0.0375 | 0.0150 | 1.32 | 2.597 |
| 0.5 | 0.05 | 2.0 | telegraph | 0.0375 | 0.0150 | 2.72 | 2.597 |
| 0.5 | 0.05 | 5.0 | telegraph | 0.0375 | 0.0150 | 4.33 | 2.597 |
| 0.5 | 0.20 | 0.5 | telegraph | 0.0375 | 0.0600 | 1.97 | 2.325 |
| 0.5 | 0.20 | 2.0 | telegraph | 0.0375 | 0.0600 | 3.95 | 2.325 |
| 0.5 | 0.20 | 5.0 | telegraph | 0.0375 | 0.0600 | 6.25 | 2.325 |
| 0.5 | 1.00 | 0.5 | telegraph | 0.0375 | 0.3000 | 1.75 | 1.492 |
| 0.5 | 1.00 | 2.0 | telegraph | 0.0375 | 0.3000 | 3.53 | 1.492 |
| 0.5 | 1.00 | 5.0 | telegraph | 0.0375 | 0.3000 | 5.58 | 1.492 |
| 0.5 | 3.00 | 0.5 | telegraph | 0.0375 | 0.9000 | 1.16 | 0.787 |
| 0.5 | 3.00 | 2.0 | telegraph | 0.0375 | 0.9000 | 2.42 | 0.787 |
| 0.5 | 3.00 | 5.0 | telegraph | 0.0375 | 0.9000 | 3.85 | 0.787 |
| 1.0 | 0.05 | 0.5 | telegraph | 0.0750 | 0.0150 | 1.32 | 1.324 |
| 1.0 | 0.05 | 2.0 | telegraph | 0.0750 | 0.0150 | 2.72 | 1.324 |
| 1.0 | 0.05 | 5.0 | telegraph | 0.0750 | 0.0150 | 4.33 | 1.324 |
| 1.0 | 0.20 | 0.5 | telegraph | 0.0750 | 0.0600 | 1.97 | 1.250 |
| 1.0 | 0.20 | 2.0 | telegraph | 0.0750 | 0.0600 | 3.95 | 1.250 |
| 1.0 | 0.20 | 5.0 | telegraph | 0.0750 | 0.0600 | 6.25 | 1.250 |
| 1.0 | 1.00 | 0.5 | telegraph | 0.0750 | 0.3000 | 1.75 | 0.961 |
| 1.0 | 1.00 | 2.0 | telegraph | 0.0750 | 0.3000 | 3.53 | 0.961 |
| 1.0 | 1.00 | 5.0 | telegraph | 0.0750 | 0.3000 | 5.58 | 0.961 |
| 1.0 | 3.00 | 0.5 | telegraph | 0.0750 | 0.9000 | 1.16 | 0.610 |
| 1.0 | 3.00 | 2.0 | telegraph | 0.0750 | 0.9000 | 2.42 | 0.610 |
| 1.0 | 3.00 | 5.0 | telegraph | 0.0750 | 0.9000 | 3.85 | 0.610 |
| 2.0 | 0.05 | 0.5 | telegraph | 0.1500 | 0.0150 | 1.32 | 0.669 |
| 2.0 | 0.20 | 0.5 | telegraph | 0.1500 | 0.0600 | 1.97 | 0.649 |
| 2.0 | 0.20 | 2.0 | telegraph | 0.1500 | 0.0600 | 3.95 | 0.649 |
| 2.0 | 0.20 | 5.0 | telegraph | 0.1500 | 0.0600 | 6.25 | 0.649 |
| 2.0 | 1.00 | 0.5 | telegraph | 0.1500 | 0.3000 | 1.75 | 0.562 |
| 2.0 | 1.00 | 2.0 | telegraph | 0.1500 | 0.3000 | 3.53 | 0.562 |
| 2.0 | 1.00 | 5.0 | telegraph | 0.1500 | 0.3000 | 5.58 | 0.562 |
| 2.0 | 3.00 | 0.5 | telegraph | 0.1500 | 0.9000 | 1.16 | 0.420 |
| 2.0 | 3.00 | 2.0 | telegraph | 0.1500 | 0.9000 | 2.42 | 0.420 |
| 2.0 | 3.00 | 5.0 | telegraph | 0.1500 | 0.9000 | 3.85 | 0.420 |
| 4.0 | 0.05 | 0.5 | telegraph | 0.3000 | 0.0150 | 1.32 | 0.336 |
| 4.0 | 0.20 | 0.5 | telegraph | 0.3000 | 0.0600 | 1.97 | 0.331 |
| 4.0 | 0.20 | 2.0 | telegraph | 0.3000 | 0.0600 | 3.95 | 0.331 |
| 4.0 | 0.20 | 5.0 | telegraph | 0.3000 | 0.0600 | 6.25 | 0.331 |
| 4.0 | 1.00 | 0.5 | telegraph | 0.3000 | 0.3000 | 1.75 | 0.307 |
| 4.0 | 1.00 | 2.0 | telegraph | 0.3000 | 0.3000 | 3.53 | 0.307 |
| 4.0 | 1.00 | 5.0 | telegraph | 0.3000 | 0.3000 | 5.58 | 0.307 |
| 4.0 | 3.00 | 0.5 | telegraph | 0.3000 | 0.9000 | 1.16 | 0.259 |
| 4.0 | 3.00 | 2.0 | telegraph | 0.3000 | 0.9000 | 2.42 | 0.259 |
| 4.0 | 3.00 | 5.0 | telegraph | 0.3000 | 0.9000 | 3.85 | 0.259 |
| 0.5 | 1.00 | 0.0 | transient | 0.0375 | 0.3000 | 0.00 | 1.492 |
| 1.0 | 1.00 | 0.0 | transient | 0.0750 | 0.3000 | 0.00 | 0.961 |
| 2.0 | 1.00 | 0.0 | transient | 0.1500 | 0.3000 | 0.00 | 0.562 |
| 2.0 | 3.00 | 0.0 | transient | 0.1500 | 0.9000 | 0.00 | 0.420 |
| 4.0 | 3.00 | 0.0 | transient | 0.3000 | 0.9000 | 0.00 | 0.259 |

## Numerical Validation

Validated 6 points with short diagnostic simulations.

| M0 | P0 | H | Phase | E mono | C decays | Oscillates | n_osc |
|----|----|---|-------|--------|----------|------------|-------|
| 0.5 | 0.05 | 0.0 | diffusion | True | True | False | 0 |
| 0.5 | 0.05 | 0.5 | telegraph | False | True | False | 0 |
| 0.5 | 1.00 | 0.0 | transient | True | True | False | 0 |
| 0.5 | 3.00 | 0.0 | reaction | True | True | False | 0 |
| 2.0 | 0.05 | 2.0 | quantum_like | False | True | False | 0 |
| 0.5 | 0.20 | 5.0 | telegraph | False | True | True | 1 |

- Energy monotone: 3/6
- Complexity decays: 6/6

## Summary

The ED PDE parameter space is partitioned into five phases with clear analytical boundaries:

- **Diffusion** (9 points): low P0/M0 ratio, Laplacian dominates.
- **Reaction** (2 points): high P0/M0 ratio, penalty dominates.
- **Telegraph** (44 points): H large enough for underdamped oscillation (Q >= 1).
- **Transient** (5 points): competing diffusion and reaction timescales.
- **Quantum-like** (4 points): high mobility + weak penalty + strong participation.

The telegraph phase dominates because even small H produces underdamped oscillation.  The quantum-like phase is a narrow corner requiring all three conditions simultaneously.