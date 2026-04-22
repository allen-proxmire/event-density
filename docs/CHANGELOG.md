# Changelog

All notable changes to the Event Density project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/).
Versioning follows [Semantic Versioning](https://semver.org/).

## [Unreleased] — 2026-04-22

### Fixed

- **`edsim/phys/analogues/telegraph_pme.py` — Analogue 5 participation-ODE forcing term.**
  Previous implementation passed `params.D * F_local` to `spatial_average` before
  forwarding to `advance_v` (line 162). The PDE specification (FPv2 §2.1) is
  `τv̇ = ⟨F[ρ]⟩ − ζv` — the domain-averaged operator *without* the `D` prefactor.
  The extra `D` shifted the off-diagonal of the coupled-mode 2D matrix from
  `P₀/τ` (intended) to `D·P₀/τ` (buggy), producing a spurious eigenmode
  `ω_coded = √(DP₀(H+ζ)/τ − γ²)` whose ratio to the intended
  `ω_linear = √((DP₀ζ + HP₀)/τ − γ²)` asymptotes to `√D ≈ 0.548`. This is the
  origin of the "54% renormalization" reported in Foundational Paper v2 §8.4
  at H ∈ {10, 20, 50} (matches 0.1662, 0.2400, 0.3842 to 4 sig figs).
  One-character fix — remove `params.D *` — restores `ω_measured ≈ ω_linear`
  at all tested H to within FFT-bin resolution.
  Full diagnosis: [`analysis/scripts/telegraph_pme/v1.4_bug_diagnosis/memo.md`](../analysis/scripts/telegraph_pme/v1.4_bug_diagnosis/memo.md).
  Solver-independence audit that motivated the forensic: [`analysis/scripts/telegraph_pme/v1.3_solver_independence/memo.md`](../analysis/scripts/telegraph_pme/v1.3_solver_independence/memo.md).

### Added

- **`analysis/scripts/telegraph_pme/v1.4_bug_diagnosis/`** — forensic root-cause
  analysis of the FPv2 §8.4 54% renormalization, with a diagnostic script
  (`diagnostic_runs.py`) containing three tests: reproduce-the-54%, amplitude-
  independence, and patch-verification.

- **Updated `analysis/scripts/telegraph_pme/v1.3_solver_independence/architectural_followthrough.md`**
  — Part 2 drop-in correction block for FPv2 §8.4 v3 revision now includes the
  line-level root-cause diagnosis (upgraded from "solver-specific, not physical"
  to "one-character code patch").

### Impact on published claims

- The Analogue-5 qualitative structure (telegraph-modulated PME, v–δ frequency
  match, participation-channel coupling) **is unaffected**. The coupling exists;
  both `v(t)` and `ρ_center(t)` oscillate at a matched frequency.
- The specific quantitative table in FPv2 §8.4 (ω_v = 0.1662, 0.2400, 0.3842
  at H = 10, 20, 50 with a systematic "54% of linear" interpretation)
  **is withdrawn and replaced** by the standard linear-eigenmode prediction
  `ω = √((DP₀ζ + HP₀)/τ − γ²)`, which the patched code reproduces at
  FFT-bin precision.
- All other analogue modules (`rc_debye.py`, `barenblatt.py`, `horizon.py`,
  `temporal_tension.py`) are audited and correct; this was a localised error.

---

## [2.0.0] - 2026-03-29

### Added

**Structural Analogues (Six Falsifiable Tests)**
- Analogue 1: RC/Debye relaxation (penalty channel, 0.00% error)
- Analogue 2: Barenblatt PME self-similarity (mobility channel, 1.1% accuracy)
- Analogue 3: Stefan horizon dynamics (mobility + penalty, 2.5% threshold error)
- Analogue 4: Telegraph-modulated horizons (negative result, architectural limit)
- Analogue 5: Telegraph-modulated PME (mobility + participation, 0.03% frequency match)
- Analogue 6: Temporal tension interaction (emergent nonlinear repulsion discovered)
- All analogues in `edsim/phys/analogues/`

**Physics Experiments (ED-PHYS-01 through ED-PHYS-10)**
- Diffusion regime, wave/telegraph regime, reaction regime
- Pattern formation (negative result: no Turing instability)
- Quantum-like regime, global phase diagram
- Energy/Lyapunov structure, physical interpretation matrix
- Cosmological analogues, master interpretation synthesis
- All experiments in `edsim/phys/`

**BAO Analogue**
- Telegraph-modulated correlation feature in 2D
- H-controlled peak radius, absent at H=0
- Paper: `manuscript/ED_BAO_Paper.md` and `.tex`

**Foundational Paper**
- Full manuscript: six analogues, falsification, synthesis
- LaTeX source (Overleaf-ready): `manuscript/foundational_paper/`

**Units, Regimes, Math, Comparison Layers**
- Physical units with five scale factories (Planck to cosmological)
- Regime manifold with five canonical domains
- Formal mathematical development (axioms, laws, transients)
- Cross-framework comparison against six theoretical frameworks

**Monograph**
- Full research monograph: `manuscript/monograph/ED_Monograph.md`

**Documentation**
- WHAT_IS_ED.md, HOW_TO_RUN_ANALOGUES.md, REPRODUCING_FOUNDATIONS_PAPER.md
- Updated README, CONTRIBUTING, CHANGELOG

**Repository Refactor**
- Research archive moved to `research/` with index
- Clean top-level layout for public release

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
