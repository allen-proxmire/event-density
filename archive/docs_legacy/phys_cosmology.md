# ED-PHYS-09: Cosmological Analogue Mapping

## Purpose

ED-PHYS-09 tests whether ED can produce structural analogues of
cosmological phenomena.  These are MATHEMATICAL analogies, not claims
of cosmological physics.

## The Three Analogues

### 1. Expansion Analogue

Starting from an overdense state (rho > rho_star), the penalty drives
global density decay — analogous to matter dilution in expanding space.

- Scale factor: a(t) = (rho_star / <rho>(t))^(1/d)
- Hubble rate: H_eff = da/dt / a

### 2. Horizon Analogue

Regions where rho approaches rho_max have vanishing mobility M -> 0,
creating dynamically isolated zones — analogous to causal horizons.

- Horizon fraction: fraction of domain where M < 1% of M_star

### 3. Structure Analogue

Multi-modal initial conditions produce transient filaments and sheets —
analogous to the cosmic web.  The analogy is INVERTED: cosmological
structure grows via gravity; ED structure decays via diffusion.

## Metrics

| Metric | Definition | Analogue |
|--------|-----------|----------|
| a(t) | (rho_star / <rho>)^(1/d) | Scale factor |
| H_eff | da/dt / a | Hubble rate |
| R_H | fraction with M < 0.01 M* | Horizon size |
| tau_struct | time for C < 10% of C(0) | Structure lifetime |

## How to Run

```python
from edsim.phys import run_full_cosmology_study

study = run_full_cosmology_study(d=2, N=64, T=8.0)
print(study.report)
```

## Key Caveat

ED has no metric tensor, no curvature, and no gravity.  These analogies
illustrate shared mathematical structure (degenerate diffusion, Hessian
eigenvalue morphology, dissipative relaxation), not physical equivalence.
