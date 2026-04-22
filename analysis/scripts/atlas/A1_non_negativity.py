"""
ED Visual Atlas — A1 Non-negativity.

Metaphor: a measuring beaker.  Fluid level can fill the vessel but cannot
extend below the hard zero baseline; a forbidden region below zero is
shown as a hatched panel.
"""

from __future__ import annotations

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from atlas_style import (
    new_canvas, equation_band, save,
    INK, ACCENT, ACCENT_SOFT, MUTED, HATCH_BG,
    LW_PRIMARY, LW_SECONDARY, LW_EMPHASIS,
)


def build():
    fig, ax = new_canvas()

    # -----------------------------------------------------------------
    # TOP  —  equation band
    # -----------------------------------------------------------------
    equation_band(
        ax,
        r"A1  —  Non-negativity:    $\mathrm{ED}(A) \geq 0$",
        fontsize=22,
    )

    # -----------------------------------------------------------------
    # BOTTOM  —  beaker metaphor
    # -----------------------------------------------------------------
    # Beaker geometry
    cx = 4.0                 # center x of beaker
    bw = 1.55                # inner width
    bh = 3.20                # inner height from baseline to rim
    x_left  = cx - bw / 2
    x_right = cx + bw / 2
    y_base  = 0.75           # baseline y (hard zero)
    y_rim   = y_base + bh

    # Forbidden region below the baseline (hatched, soft gray)
    forbid_h = 0.50
    forbid = Rectangle(
        (x_left - 0.55, y_base - forbid_h),
        bw + 1.10, forbid_h,
        facecolor=HATCH_BG, edgecolor=MUTED,
        linewidth=LW_SECONDARY, hatch="////",
    )
    ax.add_patch(forbid)
    # set hatch color via rcParams-equivalent: matplotlib uses edgecolor for hatch
    forbid.set_edgecolor(MUTED)

    # Fluid fill inside beaker (arbitrary positive level)
    fluid_level = y_base + 0.55 * bh
    fluid = Rectangle(
        (x_left + 0.03, y_base + 0.02),
        bw - 0.06, fluid_level - y_base - 0.02,
        facecolor=ACCENT_SOFT, edgecolor="none",
    )
    ax.add_patch(fluid)
    # fluid surface as a thin accent line
    ax.plot([x_left + 0.03, x_right - 0.03],
            [fluid_level, fluid_level],
            color=ACCENT, linewidth=LW_SECONDARY)

    # Beaker walls (open top)
    # Left wall
    ax.plot([x_left, x_left], [y_base, y_rim],
            color=INK, linewidth=LW_PRIMARY, solid_capstyle="butt")
    # Right wall
    ax.plot([x_right, x_right], [y_base, y_rim],
            color=INK, linewidth=LW_PRIMARY, solid_capstyle="butt")
    # Slight lip on top (flared corner)
    lip_dx = 0.10
    lip_dy = 0.10
    ax.plot([x_left, x_left - lip_dx], [y_rim, y_rim + lip_dy],
            color=INK, linewidth=LW_PRIMARY)
    ax.plot([x_right, x_right + lip_dx], [y_rim, y_rim + lip_dy],
            color=INK, linewidth=LW_PRIMARY)

    # Emphasized zero baseline (extends slightly beyond the beaker)
    ax.plot([x_left - 0.35, x_right + 0.35],
            [y_base, y_base],
            color=INK, linewidth=LW_EMPHASIS, solid_capstyle="round")

    # Small "0" label to the left of the baseline
    ax.text(x_left - 0.55, y_base, "0",
            ha="right", va="center", fontsize=13,
            color=INK, fontweight="bold")

    # Tick marks on inside right wall (scale), equally spaced
    n_ticks = 5
    tick_len = 0.12
    for i in range(1, n_ticks + 1):
        ty = y_base + (i / n_ticks) * bh
        ax.plot([x_right - tick_len, x_right],
                [ty, ty],
                color=MUTED, linewidth=LW_SECONDARY)

    # Indicator arrow: pointing UP on the left of the beaker,
    # showing the allowed direction
    arrow_x = x_left - 0.90
    arrow = FancyArrowPatch(
        (arrow_x, y_base),
        (arrow_x, y_rim - 0.05),
        arrowstyle="-|>", mutation_scale=16,
        color=INK, linewidth=LW_PRIMARY,
    )
    ax.add_patch(arrow)
    # small plus sign above the arrow
    ax.text(arrow_x, y_rim + 0.10, "+",
            ha="center", va="bottom", fontsize=16,
            color=INK, fontweight="bold")

    # Tiny annotation indicating the forbidden band (a minus sign in the hatched zone)
    ax.text(arrow_x, y_base - forbid_h / 2, "–",
            ha="center", va="center", fontsize=18,
            color=MUTED, fontweight="bold")

    # -----------------------------------------------------------------
    # Save
    # -----------------------------------------------------------------
    path = save(fig, "A1_non_negativity.png")
    print(f"wrote {path}")
    return path


if __name__ == "__main__":
    build()
