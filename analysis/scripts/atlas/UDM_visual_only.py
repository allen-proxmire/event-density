"""
UDM — Universal Diffusion Mobility — visual-only illustration.

Metaphor: a universal data-collapse plot.  Many different materials —
rendered as different colors + different marker shapes — all fall onto
a single master curve  D(c) = D₀ (1 − c/c_max)^β.

Composition:
  MAIN  : a clean axis (c/c_max on x, D/D₀ on y) with a thick cyan
          master curve carrying a soft halo; 8 colored scatter series
          (each a distinct material) land on the curve with only tiny
          residual scatter — visually conveying "universal."
  BELOW : a row of small material-icon badges (no text), each colored
          + shaped to match its scatter series on the plot.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, Polygon, FancyArrowPatch,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\UDM_universal.png"


MATERIALS = [
    # (core, edge, marker_kind)
    ("#4fa3d8", "#0b4a68", "circle"),
    ("#e0584f", "#7a1d1d", "diamond"),
    ("#2fb27a", "#1b6f4a", "square"),
    ("#8a5ac9", "#3c1e6a", "triangle_up"),
    ("#ff9f1a", "#7a4a0a", "star"),
    ("#1aa6c7", "#0b4a68", "pentagon"),
    ("#d94f7b", "#7a2844", "hexagon"),
    ("#5b6b80", "#2a3a50", "triangle_down"),
]


def draw_marker(ax, x, y, kind, core, edge, size=0.12, zorder=10,
                alpha=0.95):
    """Draw a shape marker at (x,y) in data coords (ax equal-aspect)."""
    if kind == "circle":
        ax.add_patch(Circle((x, y), size, facecolor=core,
                            edgecolor=edge, lw=1.0,
                            alpha=alpha, zorder=zorder))
    elif kind == "diamond":
        pts = [(x, y + size), (x + size, y),
               (x, y - size), (x - size, y)]
        ax.add_patch(Polygon(pts, closed=True,
                             facecolor=core, edgecolor=edge,
                             lw=1.0, alpha=alpha, zorder=zorder))
    elif kind == "square":
        ax.add_patch(Rectangle((x - size * 0.9, y - size * 0.9),
                               size * 1.8, size * 1.8,
                               facecolor=core, edgecolor=edge,
                               lw=1.0, alpha=alpha, zorder=zorder))
    elif kind == "triangle_up":
        pts = [(x, y + size * 1.1),
               (x - size, y - size * 0.7),
               (x + size, y - size * 0.7)]
        ax.add_patch(Polygon(pts, closed=True,
                             facecolor=core, edgecolor=edge,
                             lw=1.0, alpha=alpha, zorder=zorder))
    elif kind == "triangle_down":
        pts = [(x, y - size * 1.1),
               (x - size, y + size * 0.7),
               (x + size, y + size * 0.7)]
        ax.add_patch(Polygon(pts, closed=True,
                             facecolor=core, edgecolor=edge,
                             lw=1.0, alpha=alpha, zorder=zorder))
    elif kind == "star":
        n = 5
        pts = []
        for k in range(n * 2):
            r = size * 1.25 if k % 2 == 0 else size * 0.55
            th = np.pi / 2 + k * np.pi / n
            pts.append((x + r * np.cos(th), y + r * np.sin(th)))
        ax.add_patch(Polygon(pts, closed=True,
                             facecolor=core, edgecolor=edge,
                             lw=1.0, alpha=alpha, zorder=zorder))
    elif kind == "pentagon":
        n = 5
        pts = []
        for k in range(n):
            th = np.pi / 2 + k * 2 * np.pi / n
            pts.append((x + size * 1.15 * np.cos(th),
                        y + size * 1.15 * np.sin(th)))
        ax.add_patch(Polygon(pts, closed=True,
                             facecolor=core, edgecolor=edge,
                             lw=1.0, alpha=alpha, zorder=zorder))
    elif kind == "hexagon":
        n = 6
        pts = []
        for k in range(n):
            th = k * 2 * np.pi / n
            pts.append((x + size * 1.05 * np.cos(th),
                        y + size * 1.05 * np.sin(th)))
        ax.add_patch(Polygon(pts, closed=True,
                             facecolor=core, edgecolor=edge,
                             lw=1.0, alpha=alpha, zorder=zorder))


def build():
    fig, ax = plt.subplots(figsize=(12, 10), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 13, 0, 11], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 13, 1.6,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # =============================================================
    # Main plot panel
    # =============================================================
    # axes in the figure's data coordinates:
    # x: c/c_max (0 on left, 1 on right)  -> mapped to data x in [1.4, 11.6]
    # y: D/D_0    (0 at bottom, 1 at top) -> mapped to data y in [2.8, 9.0]
    plot_x0, plot_x1 = 1.4, 11.6
    plot_y0, plot_y1 = 2.8, 9.0

    # plot panel background
    ax.add_patch(FancyBboxPatch(
        (plot_x0 - 0.35, plot_y0 - 0.40),
        plot_x1 - plot_x0 + 0.70,
        plot_y1 - plot_y0 + 0.80,
        boxstyle="round,pad=0.04,rounding_size=0.24",
        facecolor="white", edgecolor="#1f3b57",
        lw=1.6, alpha=0.92, zorder=2,
    ))

    # axes lines
    ax.plot([plot_x0, plot_x1], [plot_y0, plot_y0],
            color="#1f3b57", lw=1.8, alpha=0.85, zorder=4)
    ax.plot([plot_x0, plot_x0], [plot_y0, plot_y1],
            color="#1f3b57", lw=1.8, alpha=0.85, zorder=4)
    # x-axis arrow
    ax.annotate("",
                xy=(plot_x1 + 0.15, plot_y0),
                xytext=(plot_x0, plot_y0),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1f3b57", lw=1.8),
                zorder=5)
    # y-axis arrow
    ax.annotate("",
                xy=(plot_x0, plot_y1 + 0.15),
                xytext=(plot_x0, plot_y0),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1f3b57", lw=1.8),
                zorder=5)

    # subtle gridlines
    for y_frac in [0.25, 0.5, 0.75]:
        y_line = plot_y0 + y_frac * (plot_y1 - plot_y0)
        ax.plot([plot_x0 + 0.02, plot_x1], [y_line, y_line],
                color="#1f3b57", lw=0.7, alpha=0.15,
                linestyle=(0, (4, 4)), zorder=3)
    for x_frac in [0.25, 0.5, 0.75]:
        x_line = plot_x0 + x_frac * (plot_x1 - plot_x0)
        ax.plot([x_line, x_line], [plot_y0 + 0.02, plot_y1],
                color="#1f3b57", lw=0.7, alpha=0.15,
                linestyle=(0, (4, 4)), zorder=3)

    # =============================================================
    # Master UDM curve: D/D₀ = (1 − c/c_max)^β
    # =============================================================
    beta = 2.0
    cs_norm = np.linspace(0, 1, 400)
    Ds_norm = np.clip(1 - cs_norm, 0, 1) ** beta

    # map to plot coordinates
    def to_x(c):
        return plot_x0 + c * (plot_x1 - plot_x0)

    def to_y(D):
        return plot_y0 + D * (plot_y1 - plot_y0)

    xs_plot = to_x(cs_norm)
    ys_plot = to_y(Ds_norm)

    # soft confidence band around the master curve
    band = 0.035
    ys_upper = to_y(np.clip(Ds_norm + band, 0, 1))
    ys_lower = to_y(np.clip(Ds_norm - band, 0, 1))
    ax.fill_between(xs_plot, ys_lower, ys_upper,
                    color="#9fe6f3", alpha=0.35, zorder=5)

    # glow underlays + crisp master curve
    for lw, col, a in [(14, "#9fe6f3", 0.15),
                       (8, "#6fd2e9", 0.28),
                       (4.5, "#1579a8", 0.98)]:
        ax.plot(xs_plot, ys_plot, color=col, lw=lw, alpha=a,
                solid_capstyle="round", zorder=6)

    # endpoint emphasis dots: D₀ at c=0 and 0 at c=c_max
    ax.add_patch(Circle((xs_plot[0], ys_plot[0]), 0.16,
                        facecolor="#fff1b0", edgecolor="#d69a1a",
                        lw=1.6, zorder=9))
    ax.add_patch(Circle((xs_plot[-1], ys_plot[-1]), 0.16,
                        facecolor="#fff1b0", edgecolor="#c23b3b",
                        lw=1.6, zorder=9))

    # =============================================================
    # Material scatter series — all collapsing onto the master curve
    # =============================================================
    rng = np.random.default_rng(3)
    pts_per_material = 7
    for i, (core, edge, kind) in enumerate(MATERIALS):
        # spread sample points across c/c_max
        c_samples = np.linspace(0.06 + i * 0.012,
                                0.95 - (i % 3) * 0.03,
                                pts_per_material)
        for c_s in c_samples:
            # small residual scatter (the "universal" signature)
            noise_c = rng.normal(0, 0.012)
            noise_D = rng.normal(0, 0.028)
            c_val = np.clip(c_s + noise_c, 0, 1)
            D_master = (1 - c_val) ** beta
            D_val = np.clip(D_master + noise_D, 0, 1)
            draw_marker(ax,
                        to_x(c_val), to_y(D_val),
                        kind=kind, core=core, edge=edge,
                        size=0.13, zorder=11, alpha=0.92)

    # =============================================================
    # Legend strip — material badges in a row below the plot
    # =============================================================
    leg_y = 1.25
    leg_total = len(MATERIALS)
    leg_gap = 1.28
    leg_x_start = (13 - (leg_total - 1) * leg_gap) / 2

    # strip background
    ax.add_patch(FancyBboxPatch(
        (leg_x_start - 0.75, leg_y - 0.55),
        (leg_total - 1) * leg_gap + 1.5, 1.0,
        boxstyle="round,pad=0.04,rounding_size=0.18",
        facecolor="white", edgecolor="#1f3b57",
        lw=1.4, alpha=0.85, zorder=3,
    ))

    for i, (core, edge, kind) in enumerate(MATERIALS):
        bx = leg_x_start + i * leg_gap
        # soft halo
        for rr, a in [(0.38, 0.12), (0.30, 0.22)]:
            ax.add_patch(Circle((bx, leg_y), rr,
                                facecolor=core, edgecolor="none",
                                alpha=a, zorder=4))
        # badge disc
        ax.add_patch(Circle((bx, leg_y), 0.28,
                            facecolor="white", edgecolor=edge,
                            lw=1.8, zorder=5))
        # matching marker inside
        draw_marker(ax, bx, leg_y,
                    kind=kind, core=core, edge=edge,
                    size=0.14, zorder=7)

    # =============================================================
    # "Collapse to one law" visual cue: thin convergent guide lines
    # from legend badges up to the master curve
    # =============================================================
    for i, (core, _, _) in enumerate(MATERIALS):
        bx = leg_x_start + i * leg_gap
        # each badge -> a representative point on the curve
        target_c = (i + 0.5) / len(MATERIALS) * 0.90 + 0.05
        tx = to_x(target_c)
        ty = to_y((1 - target_c) ** beta)
        ax.plot([bx, tx], [leg_y + 0.3, ty - 0.18],
                color=core, lw=0.9, alpha=0.28,
                linestyle=(0, (3, 4)), zorder=2)

    # ---- small funnel-collapse hint at the right end of the curve
    # (a gathering glow at c near 0, showing many series starting together)
    for rr, a in [(0.55, 0.08), (0.40, 0.14), (0.28, 0.22)]:
        ax.add_patch(Circle((xs_plot[0], ys_plot[0]), rr,
                            facecolor="#ffd24a", edgecolor="none",
                            alpha=a, zorder=5))

    # ---- small "decrease" arrow alongside the curve (optional cue)
    ax.annotate("",
                xy=(to_x(0.75), to_y(0.05)),
                xytext=(to_x(0.15), to_y(0.80)),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1579a8", lw=1.6, alpha=0.35,
                                linestyle=(0, (5, 4))),
                zorder=5)

    # ---- framing ---------------------------------------------------
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 11)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.tight_layout()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    plt.savefig(OUT, dpi=220, bbox_inches="tight",
                facecolor="#f7fbfe", edgecolor="none")
    plt.close(fig)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    build()
