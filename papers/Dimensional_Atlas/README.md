# The Dimensional Atlas of Event Density

The synthesis paper of the ED-Dimensional series. Maps the canonical Event Density PDE to physical (SI) units across **five physical regimes** spanning **61 orders of magnitude in length scale** — from the Planck length ($10^{-35}$ m) to the Hubble length ($10^{26}$ m).

In every regime, the universal nondimensional invariant

$$
D_{\rm phys} \cdot T_0 / L_0^2 \;=\; D_{\rm nd} \;=\; 0.3
$$

holds **exactly**. This is not a fit; it is a structural identity built into the canonical PDE under nondimensionalization. The same PDE, with the same constitutive functions, produces quantitative predictions in SI units for quantum diffusion, Planck-scale transport, condensed-matter relaxation, galactic dynamics, and cosmological evolution.

## Contents

| File | What it is |
|------|-----------|
| [`paper.md`](paper.md) | Canonical Markdown source — the master synthesis document |
| [`regimes/`](regimes/) | Five regime-specific monographs, one per physical scale |

### The five regime mappings

| # | Regime | $L_0$ anchor | $T_0$ anchor | Empirical correspondence |
|---|--------|---------------|---------------|--------------------------|
| 1 | [Quantum](regimes/ED-Dimensional-01_Quantum_Regime.md) | $\hbar / 2mc$ | $\hbar / 2mc^2$ | Schrödinger-like diffusion |
| 2 | [Planck](regimes/ED-Dimensional-02_Planck_Regime.md) | $\sqrt{\hbar G/c^3}$ | $\sqrt{\hbar G/c^5}$ | Quantum-gravity transport |
| 3 | [Condensed matter](regimes/ED-Dimensional-03_Condensed_Matter_Regime.md) | thermal diffusivity scale | molecular relaxation | Mobility law (UDM, this repo) |
| 4 | [Galactic](regimes/ED-Dimensional-04_Galactic_Regime.md) | $v_{\rm circ} \cdot L_0 \sim$ kpc | $L_0 / v_{\rm circ}$ | Cluster merger lag (Galaxy-15, this repo) |
| 5 | [Cosmological](regimes/ED-Dimensional-05_Cosmological_Regime.md) | $c^2 / H_0$ | $1 / H_0$ | Friedmann analogue |

## Cross-references

- Canonical PDE: [`/theory/PDE.md`](../../theory/PDE.md), §6 (dimensional summary)
- Empirical confirmation in the condensed-matter regime: [`/papers/Universal_Mobility_Law/`](../Universal_Mobility_Law/)
- Empirical confirmation in the galactic regime: [`/papers/Cluster_Merger_Lag_Evidence/`](../Cluster_Merger_Lag_Evidence/)
- Computational atlas (numerical realization): [`/papers/Numerical_Atlas/`](../Numerical_Atlas/)
