# ED-PHYS-08: Physical Interpretation Framework

## Purpose

ED-PHYS-08 maps the ED PDE's mathematical structure to candidate physical
domains, scoring each on 10 empirically established properties from
PHYS-01 through PHYS-07.

## The 10 Scoring Properties

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

## Ranking

| Domain | Score | Plausibility |
|--------|-------|-------------|
| Population/agent density | **8/10** | **Strong** |
| Porous-medium (+ reaction) | 6/10 | Moderate |
| Reaction-diffusion | 6/10 | Moderate |
| Statistical mechanics (FP) | 5/10 | Weak |
| Telegraph, thin-film, hydro, RG | 3/10 each | Poor |

## The Strongest Interpretation

**Population/agent density models** match 8 of 10 ED properties:

- rho = population density
- M(rho) = density-dependent dispersal (crowding reduces mobility)
- rho_max = carrying capacity
- P(rho) = logistic-like penalty toward equilibrium
- rho_star = target/equilibrium density

The only mismatches are: no global oscillator in standard population models
(P4), and many population models are gradient flows (P8).

## How to Run

```python
from edsim.phys import run_full_interpretation_study

study = run_full_interpretation_study()
print(study.report)
```

## How to Read the Matrix

Each domain is scored on how many of the 10 ED properties it shares
(match) and how many it contradicts (mismatch).  Properties that are
not applicable (e.g., spatial patterns for an ODE system) count as
mismatches.

A "strong" interpretation (8+) means the domain reproduces most of ED's
structure.  A "moderate" interpretation (6-7) shares the core but differs
in important details.  A "weak" interpretation (4-5) has partial overlap.
A "poor" interpretation (< 4) is metaphorical at best.
