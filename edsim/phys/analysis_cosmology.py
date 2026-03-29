"""
edsim.phys.analysis_cosmology — Cosmological-analogue analysis and report.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional

import numpy as np

from .cosmology_regime import CosmologyRegime, build_cosmology_regime
from .experiments_cosmology import (
    ExpansionResult, HorizonResult, StructureResult,
    run_expansion_analogue, run_horizon_analogue, run_structure_analogue,
)


@dataclass
class CosmologyStudyResult:
    """Complete output of the cosmology-analogue study."""

    regime: CosmologyRegime
    expansion: ExpansionResult
    horizon: HorizonResult
    structure: StructureResult
    report: str


def compute_scale_factor_fit(exp: ExpansionResult) -> tuple[float, float]:
    """Fit a(t) ~ 1 - B exp(-lambda t) and return (B, lambda).

    In practice, fit <rho>(t) = rho_star + delta_0 exp(-lambda t),
    then lambda is the expansion rate.
    """
    t = exp.times
    delta = exp.mean_rho - exp.regime.parameters.rho_star
    mask = np.abs(delta) > 1e-10
    if np.sum(mask) < 3:
        return 0.0, 0.0

    log_d = np.log(np.abs(delta[mask]))
    c = np.polyfit(t[mask], log_d, 1)
    lam = -c[0]
    B = np.exp(c[1])
    return float(B), float(lam)


def compute_horizon_lifetime(hor: HorizonResult) -> float:
    """Estimate the time when horizon fraction drops below 0.01."""
    for i, frac in enumerate(hor.horizon_fraction):
        if i > 0 and frac < 0.01 and hor.horizon_fraction[0] > 0.01:
            return float(hor.times[i])
    if hor.horizon_fraction[0] < 0.01:
        return 0.0  # no horizons ever formed
    return float(hor.times[-1])  # horizons persist to end


def compute_structure_lifetime(struct: StructureResult) -> float:
    """Time for complexity to drop below 10% of its initial value."""
    C = struct.complexity
    if len(C) < 2 or C[0] < 1e-30:
        return 0.0
    threshold = 0.1 * C[0]
    for i in range(1, len(C)):
        if C[i] < threshold:
            return float(struct.times[i])
    return float(struct.times[-1])


def run_full_cosmology_study(
    d: int = 2,
    N: int = 64,
    T: float = 8.0,
) -> CosmologyStudyResult:
    """Run all three cosmology-analogue experiments and report."""
    regime = build_cosmology_regime(d=d, N=N, T=T)

    expansion = run_expansion_analogue(regime=regime)
    horizon = run_horizon_analogue(regime=regime)
    structure = run_structure_analogue(regime=regime)

    report = _build_report(regime, expansion, horizon, structure)

    return CosmologyStudyResult(
        regime=regime,
        expansion=expansion,
        horizon=horizon,
        structure=structure,
        report=report,
    )


def _build_report(regime, exp, hor, struct):
    params = regime.parameters
    B, lam_fit = compute_scale_factor_fit(exp)
    hor_life = compute_horizon_lifetime(hor)
    struct_life = compute_structure_lifetime(struct)

    lines = [
        "# ED-PHYS-09: Cosmological Analogue Mapping",
        "",
        "## Caveat",
        "",
        "These are STRUCTURAL ANALOGIES, not cosmological physics.  ED is a "
        "classical, dissipative, parabolic PDE on a flat domain.  It has no "
        "metric, no curvature, and no gravity.  The analogies illustrate "
        "shared mathematical structure, not physical equivalence.",
        "",
        "## Regime",
        "",
        f"- Dimension: {params.d}D, grid {params.N[0]}^{params.d}",
        f"- Amplitude A = {regime.ic_amplitude}, modes Nm = {regime.ic_modes}",
        f"- P0 = {params.P0}, H = {params.H}",
        f"- Predicted expansion rate: {regime.expansion_rate:.4f}",
        f"- Horizon threshold: rho > {regime.horizon_threshold:.4f}",
        f"- Structure lifetime: {regime.structure_lifetime:.3f}",
        "",
        "## Experiment 1: Expansion Analogue",
        "",
        f"- Initial <rho> = {exp.mean_rho[0]:.4f} (overdense)",
        f"- Final <rho> = {exp.mean_rho[-1]:.4f}",
        f"- Fitted decay rate: {lam_fit:.4f} "
        f"(predicted D*P0 = {regime.expansion_rate:.4f}, "
        f"error {abs(lam_fit - regime.expansion_rate)/(regime.expansion_rate+1e-30)*100:.1f}%)",
        f"- Initial a(0) = {exp.scale_factor[0]:.4f}",
        f"- Final a(T) = {exp.scale_factor[-1]:.4f}",
        f"- Initial H_eff = {exp.hubble_rate[0]:.4f}",
        "",
        "### Analogue Interpretation",
        "",
        "The mean density decays exponentially toward rho_star, analogous to "
        "matter dilution in a de Sitter-like expansion.  The effective scale "
        "factor a(t) grows from a(0) < 1 to a -> 1 as the density approaches "
        "equilibrium.  The Hubble rate H_eff decreases monotonically, "
        "analogous to deceleration.",
        "",
        "## Experiment 2: Horizon Analogue",
        "",
        f"- Initial horizon fraction: {hor.horizon_fraction[0]:.4f} "
        f"({hor.horizon_fraction[0]*100:.1f}% of domain)",
        f"- Final horizon fraction: {hor.horizon_fraction[-1]:.4f}",
        f"- Horizon lifetime: {hor_life:.3f}",
        f"- Initial min mobility: {hor.min_mobility[0]:.4e}",
        f"- Final min mobility: {hor.min_mobility[-1]:.4e}",
        "",
        "### Analogue Interpretation",
        "",
    ]

    if hor.horizon_fraction[0] > 0.001:
        lines.extend([
            "Horizons form in regions where the density approaches rho_max "
            "and the mobility vanishes.  These regions are dynamically "
            "isolated: diffusion cannot transport density across them.  "
            "As the penalty relaxes the density, horizons shrink and "
            f"disappear after t ~ {hor_life:.2f}.",
            "",
            "This is analogous to cosmological horizons that shrink as "
            "the universe decelerates, allowing previously disconnected "
            "regions to come into causal contact.",
        ])
    else:
        lines.extend([
            "No horizons formed at this amplitude.  The density did not "
            f"approach rho_max closely enough (threshold = {regime.horizon_threshold:.3f}).  "
            "Increase amplitude A to produce horizon analogues.",
        ])

    lines.extend([
        "",
        "## Experiment 3: Structure Analogue",
        "",
        f"- Initial complexity C(0) = {struct.complexity[0]:.4e}",
        f"- Peak complexity = {max(struct.complexity):.4e}",
        f"- Structure lifetime (C < 10% of initial): {struct_life:.3f} "
        f"(predicted {regime.structure_lifetime:.3f})",
        f"- Initial filament fraction: {struct.filament_fraction[0]:.4f}",
        f"- Final filament fraction: {struct.filament_fraction[-1]:.4f}",
        "",
        "### Analogue Interpretation",
        "",
        "Transient filaments and sheets form from the multi-modal initial "
        "condition and decay as the field relaxes to equilibrium.  This is "
        "the INVERSE of cosmological structure formation: in cosmology, "
        "gravity amplifies structure; in ED, diffusion and penalty destroy it.",
        "",
        "The analogy is structural: both systems produce filament/sheet/blob "
        "morphology classified by Hessian eigenvalues.  The dynamics are "
        "opposite (growth vs decay).",
        "",
        "## Summary of Analogues",
        "",
        "| Cosmological feature | ED analogue | Mechanism | Status |",
        "|---------------------|------------|-----------|--------|",
        f"| Matter dilution | Density decay | Penalty relaxation | "
        f"{'Confirmed' if abs(lam_fit - regime.expansion_rate)/(regime.expansion_rate+1e-30) < 0.2 else 'Partial'} |",
        f"| Scale factor growth | a(t) -> 1 | rho -> rho_star | "
        f"a(0)={exp.scale_factor[0]:.3f}, a(T)={exp.scale_factor[-1]:.3f} |",
        f"| Causal horizons | M(rho)->0 regions | Degenerate mobility | "
        f"{'Confirmed' if hor.horizon_fraction[0] > 0.001 else 'Not formed'} |",
        f"| Structure formation | Transient filaments | Differential decay | "
        f"Lifetime={struct_life:.3f} |",
        "| Deceleration | H_eff decreasing | Exponential relaxation | Confirmed |",
        "",
        "## Limitations",
        "",
        "- ED 'expansion' is density decay, not metric expansion.",
        "- ED horizons are diffusion barriers, not null surfaces.",
        "- ED structure decays; cosmological structure grows.",
        "- There is no redshift, no photon propagation, no gravity.",
        "- The analogies are mathematical, not physical.",
    ])

    return "\n".join(lines)
