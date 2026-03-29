"""
edsim.regimes.atlas -- Regime atlas: multi-regime comparison engine.

Runs ED simulations across multiple physical regimes, classifies each,
computes physical observables, and produces publication-quality
comparison figures and tables.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

import numpy as np

from ..core.parameters import EDParameters
from ..experiments.scenarios import Scenario, get_scenario
from ..experiments.atlas import run_atlas
from ..units.scales import Scales, compute_scales
from ..units.wrapper import (
    PhysicalParameters,
    PhysicalTimeSeries,
    convert_time_series,
    run_physical_simulation,
)
from .manifold import Regime, build_regime_manifold
from .classifier import classify_scales, compute_dimensionless_groups
from .observables import (
    PhysicalObservables,
    compute_observables,
    observables_table,
    compare_observables,
)


@dataclass
class RegimeEntry:
    """One entry in the regime atlas.

    Attributes
    ----------
    regime : Regime
        Classified regime.
    scales : Scales
        Characteristic scales used.
    params : EDParameters
        Nondimensional parameters.
    pts : PhysicalTimeSeries
        Simulation output in physical units.
    observables : PhysicalObservables
        Extracted physical observables.
    groups : dict[str, float]
        Dimensionless groups.
    """

    regime: Regime
    scales: Scales
    params: EDParameters
    pts: PhysicalTimeSeries
    observables: PhysicalObservables
    groups: dict = field(default_factory=dict)


@dataclass
class RegimeAtlas:
    """Complete regime atlas with entries and figures.

    Attributes
    ----------
    entries : list[RegimeEntry]
        One entry per regime explored.
    figures : dict[str, object]
        Named matplotlib Figure objects.
    """

    entries: list[RegimeEntry] = field(default_factory=list)
    figures: dict = field(default_factory=dict)

    def summary_table(self) -> str:
        """Return a Markdown table summarising all entries."""
        return observables_table([e.observables for e in self.entries])

    def comparison_data(self) -> dict[str, list]:
        """Return cross-regime comparison dictionary."""
        return compare_observables([e.observables for e in self.entries])


# ══════════════════════════════════════════════════════════════════════
#  Atlas construction
# ══════════════════════════════════════════════════════════════════════

def run_regime_atlas(
    scenario: Optional[Scenario] = None,
    scales_list: Optional[list[Scales]] = None,
    physical_params_list: Optional[list[PhysicalParameters]] = None,
    make_figures: bool = True,
) -> RegimeAtlas:
    """Run a multi-regime atlas.

    Accepts either:
        (a) A scenario + list of Scales (run nondimensional, convert), or
        (b) A list of PhysicalParameters (convert, run, convert back).

    At least one of (scales_list, physical_params_list) must be provided.

    Parameters
    ----------
    scenario : Scenario, optional
        Nondimensional scenario to run (used with scales_list).
        Defaults to A_2d_cosine.
    scales_list : list[Scales], optional
        Scales for each regime to explore.
    physical_params_list : list[PhysicalParameters], optional
        Physical parameter sets to run.
    make_figures : bool
        Whether to generate matplotlib figures.

    Returns
    -------
    RegimeAtlas
        Atlas with entries and (optionally) figures.
    """
    atlas = RegimeAtlas()

    if scenario is None:
        scenario = get_scenario("A_2d_cosine")

    # Path A: scenario + multiple scales
    if scales_list is not None:
        params_nd, ts_nd = run_atlas(scenario)
        for sc in scales_list:
            regime = classify_scales(sc)
            pts = convert_time_series(ts_nd, sc)
            pts.params_nd = params_nd
            groups = compute_dimensionless_groups(sc, params_nd)
            obs = compute_observables(pts, regime_name=regime.label)
            atlas.entries.append(RegimeEntry(
                regime=regime, scales=sc, params=params_nd,
                pts=pts, observables=obs, groups=groups,
            ))

    # Path B: separate physical parameter sets
    if physical_params_list is not None:
        for pp in physical_params_list:
            params_nd, sc = pp.to_ed_parameters()
            regime = classify_scales(sc)
            pts = run_physical_simulation(pp)
            pts.params_nd = params_nd
            groups = compute_dimensionless_groups(sc, params_nd)
            obs = compute_observables(pts, regime_name=regime.label)
            atlas.entries.append(RegimeEntry(
                regime=regime, scales=sc, params=params_nd,
                pts=pts, observables=obs, groups=groups,
            ))

    if make_figures and atlas.entries:
        atlas.figures = _build_figures(atlas)

    return atlas


# ══════════════════════════════════════════════════════════════════════
#  Figure generation
# ══════════════════════════════════════════════════════════════════════

def _build_figures(atlas: RegimeAtlas) -> dict:
    """Generate publication-quality figures for the regime atlas."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    figs = {}

    entries = atlas.entries
    n = len(entries)

    # ── Figure 1: Regime scatter (L0 vs R0) ──────────────────────
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    for e in entries:
        ax1.scatter(
            e.scales.L0, e.scales.R0,
            c=e.regime.color, s=120, zorder=5,
            edgecolors="k", linewidths=0.5,
        )
        ax1.annotate(
            e.regime.label,
            (e.scales.L0, e.scales.R0),
            textcoords="offset points", xytext=(8, 4),
            fontsize=8,
        )

    # Shade regime regions
    for r in build_regime_manifold():
        ax1.axvspan(
            r.L0_range[0], r.L0_range[1],
            alpha=0.05, color=r.color,
        )

    ax1.set_xscale("log")
    ax1.set_yscale("log")
    ax1.set_xlabel("$L_0$ [m]", fontsize=11)
    ax1.set_ylabel("$R_0$ [kg m$^{-3}$]", fontsize=11)
    ax1.set_title("ED Regime Manifold", fontsize=12)
    ax1.grid(True, alpha=0.3, which="both")
    fig1.tight_layout()
    figs["regime_scatter"] = fig1

    # ── Figure 2: Energy evolution overlay ────────────────────────
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    for e in entries:
        if e.pts.energy_J:
            # Normalise energy to initial for overlay
            E = np.array(e.pts.energy_J)
            E_norm = E / (E[0] + 1e-300)
            t_norm = np.array(e.pts.times_s) / (e.pts.times_s[-1] + 1e-300)
            ax2.plot(t_norm, E_norm, label=e.regime.label,
                     color=e.regime.color, linewidth=1.5)
    ax2.set_xlabel("$t / T_{\\mathrm{final}}$", fontsize=11)
    ax2.set_ylabel("$E(t) / E(0)$", fontsize=11)
    ax2.set_title("Normalised Energy Decay Across Regimes", fontsize=12)
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)
    fig2.tight_layout()
    figs["energy_overlay"] = fig2

    # ── Figure 3: Invariant comparison bar chart ──────────────────
    fig3, axes3 = plt.subplots(1, 3, figsize=(12, 4))
    labels = [e.regime.label for e in entries]
    colors = [e.regime.color for e in entries]
    x = np.arange(n)

    # R_grad
    vals = [e.observables.R_grad_mean for e in entries]
    axes3[0].bar(x, vals, color=colors)
    axes3[0].set_xticks(x)
    axes3[0].set_xticklabels(labels, rotation=30, ha="right", fontsize=8)
    axes3[0].set_ylabel("$R_{\\mathrm{grad}}$")
    axes3[0].set_title("Gradient dissipation")
    axes3[0].set_ylim(0, 1)

    # Energy ratio
    vals = [e.observables.energy_ratio for e in entries]
    axes3[1].bar(x, vals, color=colors)
    axes3[1].set_xticks(x)
    axes3[1].set_xticklabels(labels, rotation=30, ha="right", fontsize=8)
    axes3[1].set_ylabel("$E_f / E_0$")
    axes3[1].set_title("Energy ratio")

    # xi growth
    vals = [e.observables.xi_growth_factor for e in entries]
    axes3[2].bar(x, vals, color=colors)
    axes3[2].set_xticks(x)
    axes3[2].set_xticklabels(labels, rotation=30, ha="right", fontsize=8)
    axes3[2].set_ylabel("$\\xi_f / \\xi_0$")
    axes3[2].set_title("Correlation growth")

    fig3.suptitle("Cross-Regime Invariant Comparison", fontsize=12)
    fig3.tight_layout()
    figs["invariant_comparison"] = fig3

    # ── Figure 4: Dimensionless group spider chart ────────────────
    fig4, ax4 = plt.subplots(figsize=(8, 5))
    group_keys = ["L0/l_Pl", "L0/kpc", "R0/rho_crit", "V0/c", "T0*H_0"]
    for e in entries:
        vals = [np.log10(max(abs(e.groups.get(k, 1e-300)), 1e-300)) for k in group_keys]
        ax4.plot(group_keys, vals, "o-", label=e.regime.label,
                 color=e.regime.color, linewidth=1.5, markersize=5)
    ax4.set_ylabel("$\\log_{10}$ (dimensionless group)", fontsize=11)
    ax4.set_title("Dimensionless Group Profiles", fontsize=12)
    ax4.legend(fontsize=9)
    ax4.grid(True, alpha=0.3)
    plt.xticks(rotation=20, fontsize=9)
    fig4.tight_layout()
    figs["dimensionless_groups"] = fig4

    plt.close("all")
    return figs


# ══════════════════════════════════════════════════════════════════════
#  Quick-run helpers
# ══════════════════════════════════════════════════════════════════════

def quick_regime_atlas(
    scenario_name: str = "A_2d_cosine",
) -> RegimeAtlas:
    """Run a quick 4-regime atlas using pre-built scale factories.

    Uses one nondimensional run + four scale conversions for speed.

    Parameters
    ----------
    scenario_name : str
        Scenario to run.

    Returns
    -------
    RegimeAtlas
    """
    from ..units.scales import (
        quantum_scales, condensed_matter_scales,
        galactic_scales, cosmological_scales,
    )
    from ..units.constants import m_e

    scenario = get_scenario(scenario_name)
    params = scenario.make_config().params

    scales_list = [
        quantum_scales(params, mass=m_e),
        condensed_matter_scales(params, L0=1e-6, R0=1e3),
        galactic_scales(params),
        cosmological_scales(params),
    ]

    return run_regime_atlas(
        scenario=scenario,
        scales_list=scales_list,
        make_figures=True,
    )
