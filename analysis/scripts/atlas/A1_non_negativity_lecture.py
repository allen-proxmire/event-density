"""
ED Visual Atlas — A1 Non-negativity  (lecture-slide version).

More visually expressive than the minimal atlas entry: a rain gauge metaphor
with falling raindrops, a blue water gradient, subtle surface ripples, a
ground plane, and a bold zero baseline.

Output: docs/figures/atlas/A1_non_negativity_lecture.png
"""

from __future__ import annotations

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch, FancyBboxPatch, Rectangle
from matplotlib.colors import LinearSegmentedColormap

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from atlas_style import (
    new_canvas, equation_band, save,
    INK, ACCENT, ACCENT_SOFT, MUTED,
    LW_PRIMARY, LW_SECONDARY, LW_EMPHASIS,
    FIG_W_IN, FIG_H_IN,
)

# lecture palette additions (still within the atlas tone)
WATER_DEEP   = "#3e6a95"   # top-of-water surface line
WATER_MID    = "#6f92b7"
WATER_LIGHT  = "#c2d5e6"
DROP_BLUE    = "#5a86b0"
DROP_LIGHT   = "#8aa8c7"
GROUND       = "#e7e3dc"
GROUND_EDGE  = "#b8b0a2"
GAUGE_FACE   = "#f7f8fa"    # very soft tint to suggest glass
GAUGE_EDGE   = "#2f3a4a"

# water colormap (dark at bottom -> light at top when extent is y_base..water_level)
water_cmap = LinearSegmentedColormap.from_list(
    "atlas_water", [(0.0, WATER_DEEP), (0.55, WATER_MID), (1.0, WATER_LIGHT)]
)


# ---------------------------------------------------------------------------
# Teardrop shape  (bezier-rendered, pointed top + rounded bottom)
# ---------------------------------------------------------------------------

def teardrop(ax, cx, cy, size=0.12, color=DROP_BLUE, alpha=0.9, zorder=5):
    """Draw a raindrop centered near (cx, cy). `size` = half-width."""
    h = size * 1.85
    w = size
    # 4 quadratic-Bezier segments forming a closed teardrop
    top = (cx, cy + h)
    right_mid = (cx + w, cy + h * 0.10)
    bot = (cx, cy - h * 0.55)
    left_mid = (cx - w, cy + h * 0.10)

    verts = [
        top,
        (cx + w * 0.95, cy + h * 0.85),  # ctrl for top->right
        right_mid,
        (cx + w * 1.00, cy - h * 0.35),  # ctrl for right->bot
        bot,
        (cx - w * 1.00, cy - h * 0.35),  # ctrl for bot->left
        left_mid,
        (cx - w * 0.95, cy + h * 0.85),  # ctrl for left->top
        top,
    ]
    codes = [Path.MOVETO] + [Path.CURVE3, Path.CURVE3] * 4
    path = Path(verts, codes)
    patch = PathPatch(path, facecolor=color, edgecolor="none",
                      alpha=alpha, zorder=zorder)
    ax.add_patch(patch)
    # subtle highlight on upper-left
    hi = Path([
        (cx - w * 0.30, cy + h * 0.70),
        (cx - w * 0.55, cy + h * 0.60),
        (cx - w * 0.15, cy + h * 0.25),
        (cx - w * 0.05, cy + h * 0.55),
        (cx - w * 0.30, cy + h * 0.70),
    ], [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.CURVE3])
    ax.add_patch(PathPatch(hi, facecolor=DROP_LIGHT, edgecolor="none",
                            alpha=0.55, zorder=zorder + 1))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def build():
    fig, ax = new_canvas()

    # -----------------------------------------------------------------
    # TOP  —  equation band
    # -----------------------------------------------------------------
    equation_band(
        ax,
        r"A1  —  Non-negativity:    $\mathrm{ED}(A) \geq 0$",
        fontsize=24,
    )

    # -----------------------------------------------------------------
    # BOTTOM  —  rain gauge
    # -----------------------------------------------------------------
    # Layout
    cx = FIG_W_IN / 2                       # center of gauge
    gauge_w = 1.45
    gauge_h = 3.10
    x_left  = cx - gauge_w / 2
    x_right = cx + gauge_w / 2
    y_ground = 0.90                          # top surface of the ground strip
    y_rim    = y_ground + gauge_h

    # --- ground strip ---
    ground_h = 0.45
    ground = Rectangle(
        (0.2, y_ground - ground_h),
        FIG_W_IN - 0.4, ground_h,
        facecolor=GROUND, edgecolor=GROUND_EDGE,
        linewidth=LW_SECONDARY, zorder=1,
    )
    ax.add_patch(ground)
    # thin grass / soil tick marks on the ground
    rng = np.random.default_rng(42)
    for _ in range(26):
        gx = rng.uniform(0.3, FIG_W_IN - 0.3)
        gh = rng.uniform(0.05, 0.11)
        # skip ticks directly under the gauge so they don't clutter
        if x_left - 0.05 < gx < x_right + 0.05:
            continue
        ax.plot([gx, gx], [y_ground, y_ground + gh],
                color=GROUND_EDGE, linewidth=0.9, zorder=2)

    # --- soft ground shadow under gauge (very subtle) ---
    shadow = Rectangle(
        (x_left - 0.25, y_ground - 0.08),
        gauge_w + 0.5, 0.08,
        facecolor="#c0b8a8", edgecolor="none", alpha=0.5, zorder=2,
    )
    ax.add_patch(shadow)

    # --- water gradient fill inside the gauge ---
    water_level = y_ground + 0.58 * gauge_h
    # gradient from dark (bottom) to light (top): vertical array
    grad = np.linspace(1.0, 0.0, 200).reshape(-1, 1)  # 1 at bottom (dark)
    ax.imshow(
        grad,
        extent=[x_left + 0.04, x_right - 0.04, y_ground + 0.02, water_level],
        aspect="auto", cmap=water_cmap, alpha=0.92, zorder=3,
    )

    # --- water surface with a gentle wave ---
    xs = np.linspace(x_left + 0.04, x_right - 0.04, 200)
    wave_amp = 0.035
    wave = (water_level
            + wave_amp * np.sin(3.2 * np.pi * (xs - x_left) / gauge_w)
            + 0.5 * wave_amp * np.sin(7.0 * np.pi * (xs - x_left) / gauge_w))
    ax.fill_between(xs, water_level - 0.08, wave,
                    color=WATER_LIGHT, alpha=0.6, zorder=4,
                    linewidth=0)
    ax.plot(xs, wave, color=WATER_DEEP, linewidth=1.4, zorder=5)

    # --- gauge body (rectangle with soft tint to suggest glass) ---
    gauge_body = Rectangle(
        (x_left, y_ground),
        gauge_w, gauge_h,
        facecolor=GAUGE_FACE, edgecolor=GAUGE_EDGE,
        linewidth=LW_PRIMARY, zorder=3, alpha=0.35,
    )
    ax.add_patch(gauge_body)
    # explicit left + right + top walls (crisper than the filled rect alone)
    ax.plot([x_left, x_left], [y_ground, y_rim],
            color=GAUGE_EDGE, linewidth=LW_PRIMARY, zorder=6)
    ax.plot([x_right, x_right], [y_ground, y_rim],
            color=GAUGE_EDGE, linewidth=LW_PRIMARY, zorder=6)
    # slight flared rim
    flare = 0.14
    ax.plot([x_left, x_left - flare], [y_rim, y_rim + flare * 0.9],
            color=GAUGE_EDGE, linewidth=LW_PRIMARY, zorder=6)
    ax.plot([x_right, x_right + flare], [y_rim, y_rim + flare * 0.9],
            color=GAUGE_EDGE, linewidth=LW_PRIMARY, zorder=6)

    # --- scale ticks on the right side of the gauge ---
    n_major = 5
    for i in range(1, n_major + 1):
        ty = y_ground + (i / n_major) * gauge_h
        ax.plot([x_right - 0.22, x_right - 0.02], [ty, ty],
                color=GAUGE_EDGE, linewidth=LW_SECONDARY, zorder=7)
        # minor ticks
        if i < n_major:
            tym = y_ground + (i / n_major + 0.5 / n_major) * gauge_h
            ax.plot([x_right - 0.12, x_right - 0.02], [tym, tym],
                    color=GAUGE_EDGE, linewidth=0.8, zorder=7)

    # --- bold zero baseline ---
    ax.plot([0.25, FIG_W_IN - 0.25], [y_ground, y_ground],
            color=INK, linewidth=LW_EMPHASIS, solid_capstyle="butt", zorder=8)
    ax.text(0.35, y_ground - 0.20, "0",
            ha="left", va="center", fontsize=16, color=INK, fontweight="bold",
            zorder=9)

    # -----------------------------------------------------------------
    # Raindrops falling from above
    # -----------------------------------------------------------------
    drops = [
        # (x, y, size, alpha)
        (cx - 0.55, y_rim + 0.95, 0.11, 0.92),
        (cx - 0.05, y_rim + 0.55, 0.095, 0.95),
        (cx + 0.40, y_rim + 1.20, 0.10, 0.90),
        (cx - 0.35, y_rim + 1.60, 0.085, 0.80),
        (cx + 0.70, y_rim + 0.35, 0.09, 0.93),
        (cx + 0.20, y_rim + 1.75, 0.08, 0.78),
    ]
    for (dx, dy, sz, a) in drops:
        teardrop(ax, dx, dy, size=sz, color=DROP_BLUE, alpha=a)

    # Very subtle motion-streak hint: faint vertical line above each large drop
    for (dx, dy, sz, a) in drops[:3]:
        ax.plot([dx, dx], [dy + sz * 2.2, dy + sz * 4.8],
                color=DROP_LIGHT, linewidth=0.9, alpha=0.45, zorder=4,
                solid_capstyle="round")

    # -----------------------------------------------------------------
    # Save
    # -----------------------------------------------------------------
    path = save(fig, "A1_non_negativity_lecture.png")
    print(f"wrote {path}")
    return path


if __name__ == "__main__":
    build()
