# ED-Phys: Public Summary

## What is this?

ED-Phys is a computational physics project that starts from a single mathematical rule about how "event densities" combine and, without importing any standard physics, derives a universe that inflates, forms structure, and expands — reproducing key features of our own cosmology.

## The starting point

The Event Density (ED) framework describes reality as a density field ρ(x,t) governed by one compositional rule: when two regions merge, their combined density equals the sum of their individual densities minus three penalty terms that account for internal relationships, spatial gradients, and boundaries.

Taking the continuum limit of this rule produces a nonlinear diffusion equation — the ED-Phys governing PDE — with no free functions beyond those specified by the compositional rule itself.

## What we built

An eight-stage pipeline progressing from mathematical derivation through simulation to analytical theory:

1. **Update Rule** — Derived the governing PDE and its discretization
2. **Simulator** — Built a modular Python engine implementing the PDE
3. **Cosmological Timeline** — Ran baseline experiments confirming four cosmological epochs
4. **Physical Analogues** — Mapped ED variables to energy density, curvature, matter, and horizons
5. **Parameter Sweeps** — Explored 135 simulations across the full parameter space
6. **Emergent Phenomena** — Searched for 14 candidate phenomena; confirmed 6, ruled out 5
7. **Analytical Theory** — Derived 7 reduced ODEs and 8 scaling laws, all validated against simulation
8. **Documentation** — Synthesized everything into a single canonical reference

## What emerges

From the compositional rule alone, the PDE produces:

- **Cosmic inflation** — Gradients decay exponentially, exactly like de Sitter expansion, with equation of state w = −1.00
- **Structure formation** — Overdensities stabilize via a concave penalty mechanism, acting as proto-matter concentrations that persist indefinitely
- **Causal horizons** — At maximum density, mobility vanishes, creating regions from which nothing can escape — analogous to black holes
- **Cosmic expansion** — Total density decreases over time, with a Friedmann-like thinning law
- **A Jeans-like instability** — A critical scale separating growing from decaying perturbations, just as in gravitational physics

These are not put in by hand. They are consequences of the compositional rule.

## Key quantitative results

- Inflation rate scales linearly with effective mobility: λ₁ = C·M_eff (R² > 0.99)
- A sharp "inflation cliff" at γ ≈ 0.5–0.7 where inflation rate drops by three orders of magnitude
- Peak structures drift by less than 0.05% over 50,000 time steps
- Basin merging follows a logistic law with 50% loss at γ = 0.461
- Five universality classes capture all observed dynamical behavior

## What is missing

The canonical PDE is parabolic (diffusion-type), not hyperbolic (wave-type). This means it naturally produces the thermodynamic and gravitational aspects of cosmology but **cannot** produce:

- Wave propagation (light, sound, gravitational waves)
- Long-range forces between structures
- Anisotropic patterns (filaments, cosmic web)
- Oscillatory dynamics

This is the project's most important finding: the ED compositional rule, in its canonical form, generates a **cosmological sector** of physics. Extending it to the full dynamical sector — waves, forces, radiation — requires additional mathematical structure (a second time derivative, non-local coupling, or vector fields).

## Why it matters

ED-Phys demonstrates that a single rule about how densities compose is sufficient to generate the large-scale architecture of a universe. The fact that inflation, structure formation, horizons, and expansion all emerge from one equation — without importing general relativity, quantum field theory, or any standard physics — suggests that compositionality may be a deeper organizing principle than the field equations traditionally used as starting points.

The clear delineation of what the canonical framework produces and what it cannot provides a precise roadmap for extending the theory toward a more complete description of physical reality.
