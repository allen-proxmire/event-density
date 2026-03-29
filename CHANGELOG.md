# Changelog

All notable changes to the ED-SIM-02 platform are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/).
Versioning follows [Semantic Versioning](https://semver.org/).

## [0.1.0] - 2026-03-28

### Added

**Solver**
- Full FD + implicit Euler integrator for d = 2, 3, 4 with Neumann BCs
- ETD-RK4 spectral integrator for d = 2 with Neumann BCs (DCT-II basis)
- Coupled (rho, v) dynamics with exact exponential participation update
- Degenerate mobility M(rho), linear penalty P(rho), bounds enforcement

**Invariant Atlas**
- Lyapunov energy E[rho], ED-complexity C[rho], total mass M[rho]
- Spectral entropy H, modal hierarchy, spectral anisotropy, radial spectrum
- Morphology fractions via Hessian eigenvalues: blob, sheet, filament, pancake (4D)
- Dissipation channel ratios: R_grad, R_pen, R_part
- Correlation length xi via Wiener-Khinchin autocorrelation
- Second-order structure function S_2(r)
- Euler characteristic chi via cubical complex (2D/3D/4D)
- Betti numbers beta_0 (exact) + beta_1 estimate (2D/3D)

**Experiments**
- Six predefined scenarios (A-F) covering 2D/3D/4D, cosine/random/Gaussian ICs
- Parameter sweeps (run_sweep) over any EDParameters field or IC parameter
- Grid sweeps (run_grid_sweep) over two parameters
- Atlas runner (run_atlas) with compact summary extraction

**Reproducibility**
- Nine-phase validation pipeline checking Laws 1-6 and dimensional scaling
- Structured ReproducibilityCertificate with pass/fail and quantitative details
- CLI entry point: `python -m edsim.reproducibility.run_all`

**Testing**
- 112 pytest tests covering core numerics, invariants, and architectural laws
- Shared fixtures for small-grid 2D/3D/4D parameters
- Module-scoped fixtures for dimensional law tests (run once, test many)

**Documentation**
- Package README with quick start and repo layout
- docs/: index, usage guide, architecture overview, API reference
- examples/: lab tour Jupyter notebook

**Packaging**
- PEP 621 pyproject.toml with pip-installable structure
- CLI: `edsim info`, `edsim run`, `edsim sweep`, `edsim certify`
- `python -m edsim` entry point
