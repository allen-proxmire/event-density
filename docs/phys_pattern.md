# ED-PHYS-04: Nonlinear Pattern Formation in Event Density

## Purpose

ED-PHYS-04 tests whether the canonical ED PDE can support pattern formation
(Turing patterns, spinodal decomposition, symmetry-breaking instabilities).

## Key Result

**ED does NOT support pattern formation.** The uniform equilibrium is
linearly stable to perturbations of ALL wavenumbers:

$$\sigma_k = -D\,(M^*\,\mu_k + P_0) < 0 \quad \text{for all } k.$$

There is no instability band, no Turing mechanism, no spinodal decomposition.

## Why No Patterns?

Pattern formation requires a positive growth rate for some wavenumber range.
This is absent in ED because:

1. **M_star > 0:** The diffusion coefficient is always positive (stabilising).
2. **P0 > 0:** The penalty is always restoring (stabilising).
3. **Single scalar field:** No activator-inhibitor dynamics.
4. **Monostable penalty:** No double-well energy or spinodal region.

## What ED Does Instead: Transient Morphology

ED creates rich transient structure through **differential decay rates**.
High-k modes decay much faster than low-k modes (by a factor of ~13x at
k=4 vs k=1 for canonical parameters).  This creates:

- A transient hierarchy of spatial scales
- Filaments, sheets, and blobs (ED-Phys-35)
- Oscillatory morphological exchange (Law 9)
- A characteristic morphological lifetime ~ 1/sigma_k1

## Experiments

### Experiment 1: Noise Instability

Small random noise is evolved.  No mode grows; all decay exponentially.
Transient amplification ratio is ~1 (no amplification).

### Experiment 2: Filament Stability

A thin ridge decays smoothly without breakup.

### Experiment 3: Spot Evolution

A localised bump diffuses and decays without developing ring structure.

## How to Run

```python
from edsim.phys import run_full_pattern_study

study = run_full_pattern_study(d=2, N=64, T=2.0)
print(study.report)
```

## Significance

The absence of pattern formation is a **distinguishing feature** of ED.
It separates ED from Allen-Cahn (domain walls), Cahn-Hilliard (labyrinthine
patterns), and other reaction-diffusion systems.  ED's structure is entirely
transient — a unique dynamical phenomenon that cannot be produced by any
standard pattern-forming PDE.
