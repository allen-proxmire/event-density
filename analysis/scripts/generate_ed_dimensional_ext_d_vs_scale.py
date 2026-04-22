"""
Generate the unified D-vs-scale diagram for ED-Dimensional-01-Ext.md §7.2.

Plots the dimensionless channel weight D against characteristic system scale
(log meters) across ~30 orders of magnitude, showing where each regime sits
relative to the bifurcation D_crit (canonical value 0.896, NOT the retired
heuristic 0.5 -- see theory/D_crit_Resolution_Memo.md, 2026-04-22).

Output: docs/figures/atlas/ED-Dimensional-Ext-D-vs-Scale.png

See ED-Dimensional-01-Ext.md §7.2 for the figure specification.
"""

from __future__ import annotations

import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

from edsim.math.damping import D_CRIT_CANONICAL   # approx 0.896 at zeta=1/4


# ---------------------------------------------------------------------------
# Plot data — scale, D value (or range), regime class, label
# ---------------------------------------------------------------------------

# Format: (log10(scale/m), D_low, D_high, label, regime_class, marker)
# When D_low == D_high, plot as a point; otherwise plot as a vertical band.

POINTS = [
    # Cavity QED — vertical bands spanning the bifurcation
    (-3.0, 0.0, 1.0, "Cavity-QED Rydberg", "cavity", "band"),
    (-5.0, 0.0, 1.0, "Cavity-QED optical", "cavity", "band"),
    # BEC — temperature-dependent band
    (-5.0, 0.02, 1.0, "BEC at finite T", "condmat", "band"),
    # FRAP — point with error bar
    (-6.0, 0.3, 0.6, "FRAP (BSA)", "condmat", "band"),
    # Optomechanics — points (deep quantum)
    (-7.0, 1e-9, 1e-9, "Optomechanics (Delic 2020)", "optomech", "point"),
    (-7.0, 4e-6, 4e-6, "Optomechanics (Chan 2011)", "optomech", "point"),
    # SC film — temperature-dependent band
    (-8.0, 0.0, 1.0, "SC film near T_c", "condmat", "band"),
    # Spin glass — formal port, deep parabolic
    (-9.0, 0.99, 0.99, "Spin glass (formal port)", "condmat", "point"),
    # Pure Debye — scope limit
    (-8.5, 1.0, 1.0, "Pure Debye (scope limit)", "condmat", "point"),
    # Galactic
    (np.log10(3e19), 0.04, 0.04, "MW spiral", "galactic", "point"),
    (np.log10(2e19), 0.20, 0.20, "Dwarf (Quiet)", "galactic", "point"),
    (np.log10(2e19), 0.45, 0.45, "Dwarf (Active)", "galactic", "point"),
    (np.log10(3e22), 0.91, 0.91, "Galaxy cluster", "galactic", "point"),
    # Cosmological
    # Cosmic-web bifurcation: the CLAIM is that the system sits at D = D_crit.
    # Under the corrected 2026-04-22 value D_crit ~ 0.896 (not the retired
    # heuristic 0.5), update this anchor in line with theory/D_crit_Resolution_Memo.md.
    (np.log10(8e23), D_CRIT_CANONICAL, D_CRIT_CANONICAL,
     "Cosmic-web bifurcation k_*", "cosmo", "point"),
    (26.0, 0.0, 0.0, "Super-horizon (Hubble)", "cosmo", "point"),
]


REGIME_COLORS = {
    "cavity": "#2D6A8C",      # blue
    "optomech": "#6B3F8C",    # purple
    "condmat": "#8C4A2D",     # rust
    "galactic": "#2D8C4A",    # green
    "cosmo": "#8C2D5F",       # magenta
}

REGIME_LABELS = {
    "cavity": "Cavity-coupled (QED)",
    "optomech": "Optomechanics",
    "condmat": "Condensed matter",
    "galactic": "Galactic",
    "cosmo": "Cosmological",
}


# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------

def main() -> None:
    fig, ax = plt.subplots(figsize=(13, 8))

    # D_crit reference line (corrected 2026-04-22: 0.896, not 0.5)
    ax.axhline(y=D_CRIT_CANONICAL, color="black", linestyle="--", linewidth=1.2,
               alpha=0.7,
               label=rf"$D_{{\rm crit}} = {D_CRIT_CANONICAL:.3f}$ (bifurcation)")

    # Shaded regions: oscillatory / hybrid / parabolic
    ax.axhspan(0.0, 0.1, alpha=0.05, color="blue", zorder=0)
    ax.axhspan(D_CRIT_CANONICAL, 1.0, alpha=0.05, color="red", zorder=0)
    ax.text(-9.5, 0.05, "oscillatory", fontsize=9, color="blue", alpha=0.7,
            style="italic")
    ax.text(-9.5, 0.98, "parabolic", fontsize=9, color="red", alpha=0.7,
            style="italic")

    # Plot points and bands
    plotted_classes = set()
    for x, d_low, d_high, label, regime_class, marker in POINTS:
        color = REGIME_COLORS[regime_class]
        if marker == "band":
            # Vertical band spanning [d_low, d_high]
            rect = Rectangle((x - 0.25, d_low), 0.5, d_high - d_low,
                             facecolor=color, alpha=0.35,
                             edgecolor=color, linewidth=1.2)
            ax.add_patch(rect)
            ax.annotate(label, xy=(x, (d_low + d_high) / 2),
                        xytext=(x + 0.6, (d_low + d_high) / 2),
                        fontsize=8, va="center",
                        arrowprops=dict(arrowstyle="-", color=color,
                                        alpha=0.5, linewidth=0.5))
        else:
            # Point
            ax.plot(x, d_low, "o", color=color, markersize=8,
                    markeredgecolor="black", markeredgewidth=0.5)
            # Position label to avoid overlap based on D value relative to D_crit
            offset_x = 0.5 if d_low < D_CRIT_CANONICAL else -0.5
            ha = "left" if d_low < D_CRIT_CANONICAL else "right"
            ax.annotate(label, xy=(x, d_low),
                        xytext=(x + offset_x, d_low + 0.03),
                        fontsize=8, va="bottom", ha=ha,
                        arrowprops=dict(arrowstyle="-", color=color,
                                        alpha=0.5, linewidth=0.5))
        if regime_class not in plotted_classes:
            plotted_classes.add(regime_class)

    # Legend (regime classes)
    legend_handles = [
        plt.Line2D([0], [0], marker="o", color="w",
                   markerfacecolor=REGIME_COLORS[k],
                   markersize=8, label=REGIME_LABELS[k])
        for k in REGIME_LABELS
    ]
    legend_handles.insert(0, plt.Line2D(
        [0], [0], color="black", linestyle="--",
        label=rf"$D_{{\rm crit}} = {D_CRIT_CANONICAL:.3f}$"))
    ax.legend(handles=legend_handles, loc="center right",
              fontsize=9, framealpha=0.9)

    # Axes
    ax.set_xlim(-11, 27)
    ax.set_ylim(-0.05, 1.05)
    ax.set_xlabel(r"$\log_{10}$(characteristic scale / m)", fontsize=11)
    ax.set_ylabel(r"$D = \gamma_{\rm dec} / (\gamma_{\rm dec} + \omega_{\rm sys})$",
                  fontsize=11)
    ax.set_title("Cross-regime D-vs-scale: rate-balance template\n"
                 "across ~30 orders of magnitude (ED-Dimensional-01-Ext §7.2)",
                 fontsize=12)

    # Scale annotations along x-axis
    scale_ticks = [-10, -5, 0, 5, 10, 15, 20, 25]
    scale_labels = [r"$10^{-10}$", r"$10^{-5}$", r"$10^{0}$",
                    r"$10^{5}$", r"$10^{10}$", r"$10^{15}$",
                    r"$10^{20}$", r"$10^{25}$"]
    ax.set_xticks(scale_ticks)
    ax.set_xticklabels(scale_labels)

    # Grid
    ax.grid(True, alpha=0.2, linestyle=":")

    # Caption-style note at bottom
    fig.text(0.5, 0.02,
             "All five quantum-mechanical regimes (cavity QED, optomechanics, BEC) "
             "sit deep oscillatory or span the bifurcation. Most condensed-matter "
             "systems are deep parabolic (Debye scope limit). Galactic regime "
             "spans the bifurcation between dwarf (D~0.3) and cluster (D~0.9). "
             "Cosmological bifurcation is at the cosmic-web scale ~27 Mpc.",
             ha="center", fontsize=8, style="italic", wrap=True)

    plt.tight_layout(rect=[0, 0.05, 1, 1])

    # Save
    out_dir = os.path.join(os.path.dirname(__file__), "..", "..",
                           "docs", "figures", "atlas")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "ED-Dimensional-Ext-D-vs-Scale.png")
    plt.savefig(out_path, dpi=160, bbox_inches="tight")
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
