# ED-Phys-12: Redesigning the Relational Penalty

Exploring alternative relational penalty forms that preserve ED ontology while removing the low-density singularity that blocks non-dissipative dynamics.

## Pipeline Position

```
ED-Phys-01 through ED-Phys-11 (canonical pipeline + extensions + multi-field + non-dissipative)
  -> ED-Phys-12 (Penalty Redesign)  <-- this module
    -> ED-Phys-13 (future)
```

## Contents

| File | Purpose |
|------|---------|
| `ED-Phys-12_Penalty.md` | Full analysis: diagnosis, 5 proposed families, 2 selected, 7 experiments, tradeoffs |
| `ed_phys_penalty.py` | Penalty variant simulator (canonical, soft-floor, symmetric) |
| `results/penalty_results.json` | All quantitative results |
| `results/2d_*.npy` | 2D density field snapshots |

## Key Findings

- **Soft-Floor Penalty** P(rho) = alpha*gamma*(rho+rho_0)^(gamma-1): removes singularity, behavior identical to canonical at rho >> rho_0. Classified as **ED-compatible improvement**.
- **Symmetric Penalty** P(rho) = alpha*gamma*(rho-rho_star)/(rho+rho_0): removes singularity AND enables channel recovery (rho=1 restored to rho=4.9 toward rho_star=5). Classified as **interesting but risky**.
- Soft-floor: no change to inflation, horizons, or peak dynamics
- Symmetric: 1.4-2.3x faster inflation, frozen peak separation, background maintained at rho_star
- Neither penalty produces oscillatory dynamics -- overdamping is structural, not just from the singularity
- **Recommendation**: Adopt soft-floor (rho_0~0.5) as canonical regularization; explore symmetric for combined use with hyperbolic extensions
