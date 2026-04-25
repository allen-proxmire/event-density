# The Numerical Atlas of Event Density

The computational companion to the Foundational Paper and the Dimensional Atlas. Demonstrates each theorem of Appendix C (PDE Analysis) numerically, by direct integration of the canonical Event Density system in $(D, \zeta, \tau)$-parameter space, and provides reference solutions, parameter maps, and quantitative benchmarks against which the predictions of the Applications Paper can be compared.

The Atlas does not prove theorems. Every mathematical claim rests on Appendix C of the Foundational Paper. The Atlas demonstrates that the theorems produce the phenomena they describe, maps quantitative dependence on parameters, and provides reproducible numerical evidence for every qualitative assertion in the ED-Arch series.

## Contents

| File | What it is |
|------|-----------|
| [`paper.md`](paper.md) | Canonical Markdown source — the full Numerical Atlas |

## What is inside

- **Demonstration:** local and global well-posedness, spectral decay and modal hierarchy, nonlinear stability and Lyapunov dissipation, the bifurcation at the critical-damping surface $\Delta = 1$, the three-stage convergence to equilibrium.
- **Exploration:** the $(D, \zeta, \tau)$-parameter landscape beyond the linearized neighborhoods — far-from-equilibrium transients, algebraic relaxation, triad coupling at large amplitude, mobility-collapse barrier $\rho \to \rho_{\max}$.
- **Calibration:** numerical values of decay rates, oscillation frequencies, triad amplitude ratios, convergence times.
- **Nine architectural laws** verified numerically across spatial dimensions $d = 1, 2, 3, 4$.

## Cross-references

- Canonical PDE: [`/theory/PDE.md`](../../theory/PDE.md)
- Foundational Paper (theorems demonstrated here): [`/papers/Foundations_of_Event_Density/`](../Foundations_of_Event_Density/)
- Universality framework: [`/papers/Foundations_of_Event_Density/Appendices/appendix_D_Universality Class.md`](../Foundations_of_Event_Density/Appendices/appendix_D_Universality%20Class.md)
- Dimensional Atlas: [`/papers/Dimensional_Atlas/`](../Dimensional_Atlas/)
- Simulation engine that integrates this PDE: [`/edsim/`](../../edsim/)
