"""
P4 Mobility Capacity Bound — visual-only illustration.

Metaphor: traffic on a one-way channel, approaching a hard capacity wall.
  - Left side  : sparse dots with long motion trails  (fast mobility)
  - Middle     : denser dots with shorter trails       (slowing)
  - Right side : jammed cluster pressed against a bright "ρ_max" wall
                 with no motion trails at all           (M = 0)

Above the channel, a M(ρ) curve starts high on the left and decays
to zero at ρ_max on the right — a visual cue of the capacity-bound law.
The hard wall on the right has a glowing rim (continuity with A1/A2).
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch, Polygon,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\P4_mobility_capacity_bound.png"


def build():
    fig, ax = plt.subplots(figsize=(11, 9), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 12, 0, 10], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 12, 1.5,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # ==============================================================
    # Top panel: M(ρ) curve
    # ==============================================================
    curve_y0, curve_y_top = 6.8, 9.2
    curve_x0, curve_x1 = 1.2, 10.8

    # axis-ish baseline
    ax.plot([curve_x0, curve_x1], [curve_y0, curve_y0],
            color="#1f3b57", lw=1.8, alpha=0.6, zorder=4)
    # right wall tick at ρ_max
    ax.plot([curve_x1, curve_x1], [curve_y0 - 0.15, curve_y_top + 0.1],
            color="#c23b3b", lw=2.2, alpha=0.85,
            linestyle=(0, (4, 3)), zorder=4)

    # M(ρ): decays from M0 on the left to 0 at curve_x1
    xs = np.linspace(curve_x0, curve_x1, 400)
    t = (xs - curve_x0) / (curve_x1 - curve_x0)
    M = (1 - t) ** 1.6          # soft convex decay to zero
    M_y = curve_y0 + M * (curve_y_top - curve_y0)

    # soft fill under curve (gradient)
    for i in range(len(xs) - 1):
        frac = i / len(xs)
        col = plt.cm.viridis(0.15 + 0.55 * (1 - frac))
        ax.fill_between([xs[i], xs[i + 1]],
                        [curve_y0, curve_y0],
                        [M_y[i], M_y[i + 1]],
                        color=col, alpha=0.28, zorder=2)
    # curve strokes
    for lw, col, a in [(10, "#9fe6f3", 0.12),
                       (6, "#6fd2e9", 0.22),
                       (3.6, "#2a7fa3", 0.55)]:
        ax.plot(xs, M_y, color=col, lw=lw, alpha=a, zorder=3,
                solid_capstyle="round")
    ax.plot(xs, M_y, color="#1f3b57", lw=2.6, zorder=5,
            solid_capstyle="round")

    # emphasis dot where M meets 0 at ρ_max
    ax.add_patch(Circle((curve_x1, curve_y0), 0.14,
                        facecolor="#c23b3b", edgecolor="#7a1d1d",
                        lw=1.4, zorder=6))
    for rr, a in [(0.40, 0.10), (0.28, 0.18), (0.20, 0.35)]:
        ax.add_patch(Circle((curve_x1, curve_y0), rr,
                            facecolor="#c23b3b", edgecolor="none",
                            alpha=a, zorder=5))

    # downward indicator arrow from the curve tail toward the jam
    ax.annotate("",
                xy=(curve_x1 - 0.05, curve_y0 - 0.35),
                xytext=(curve_x1 - 0.05, M_y[-30] + 0.3),
                arrowprops=dict(arrowstyle="-|>",
                                color="#c23b3b", lw=2.2),
                zorder=6)

    # ==============================================================
    # Bottom panel: the channel (traffic)
    # ==============================================================
    ch_x0, ch_x1 = 1.0, 11.0
    ch_y0, ch_y1 = 2.4, 5.6
    ch_w = ch_x1 - ch_x0
    ch_h = ch_y1 - ch_y0

    # channel body with a left→right density gradient tint
    nslabs = 120
    for i in range(nslabs):
        frac = i / nslabs
        x0 = ch_x0 + frac * ch_w
        # cool teal to warm amber to red
        if frac < 0.5:
            mix = frac / 0.5
            c = ((1 - mix) * np.array([0.71, 0.88, 0.93])
                 + mix * np.array([1.00, 0.82, 0.50]))
        else:
            mix = (frac - 0.5) / 0.5
            c = ((1 - mix) * np.array([1.00, 0.82, 0.50])
                 + mix * np.array([0.88, 0.30, 0.30]))
        ax.add_patch(Rectangle(
            (x0, ch_y0), ch_w / nslabs + 0.02, ch_h,
            facecolor=c, edgecolor="none", alpha=0.40, zorder=2,
        ))

    # channel outline
    ax.add_patch(FancyBboxPatch(
        (ch_x0, ch_y0), ch_w, ch_h,
        boxstyle="round,pad=0.02,rounding_size=0.20",
        facecolor="none", edgecolor="#1f3b57", lw=3.0, zorder=7,
    ))

    # ---- hard ρ_max wall on the right -----------------------------
    wall_w = 0.45
    wall_x = ch_x1 - wall_w + 0.02
    # glow
    for glow, a in [(0.65, 0.08), (0.45, 0.16),
                    (0.28, 0.28), (0.15, 0.50)]:
        ax.add_patch(Rectangle(
            (wall_x - glow / 2, ch_y0 - glow / 2),
            wall_w + glow, ch_h + glow,
            facecolor="#ff5c5c", edgecolor="none",
            alpha=a, zorder=3,
        ))
    ax.add_patch(Rectangle(
        (wall_x, ch_y0), wall_w, ch_h,
        facecolor="#c23b3b", edgecolor="#7a1d1d", lw=2.2, zorder=8,
    ))
    # hatching on the wall to suggest impenetrability
    for hy in np.linspace(ch_y0 + 0.15, ch_y1 - 0.15, 12):
        ax.plot([wall_x + 0.05, wall_x + wall_w - 0.05],
                [hy, hy - 0.18],
                color="#fff1b0", lw=1.8, alpha=0.7, zorder=9)

    # ---- particles with velocity trails ---------------------------
    rng = np.random.default_rng(12)

    def trail(ax_obj, x, y, length, color, alpha, lw):
        # motion trail pointing left-to-right (ending at x)
        xs = np.linspace(x - length, x, 20)
        for i in range(len(xs) - 1):
            frac = i / (len(xs) - 1)
            ax_obj.plot([xs[i], xs[i + 1]], [y, y],
                        color=color, lw=lw * (0.2 + 0.8 * frac),
                        alpha=alpha * (0.15 + 0.85 * frac),
                        solid_capstyle="round", zorder=5)

    def particle(ax_obj, x, y, r, core, halo, edge,
                 trail_len=0.0, trail_col=None):
        if trail_len > 0 and trail_col is not None:
            trail(ax_obj, x, y, trail_len, trail_col, 0.85, lw=2.2)
        for rr, a in [(r * 2.1, 0.08), (r * 1.6, 0.18),
                      (r * 1.25, 0.35)]:
            ax_obj.add_patch(Circle((x, y), rr,
                                    facecolor=halo, edgecolor="none",
                                    alpha=a, zorder=6))
        ax_obj.add_patch(Circle((x, y), r,
                                facecolor=core, edgecolor=edge,
                                lw=1.0, zorder=7))
        ax_obj.add_patch(Circle((x - r * 0.3, y + r * 0.3),
                                r * 0.32,
                                facecolor="white", alpha=0.75, zorder=8))

    # Zone A: sparse & fast (cyan dots with long trails)
    A_dots = [
        (ch_x0 + 0.7, ch_y0 + 2.2),
        (ch_x0 + 1.2, ch_y0 + 0.8),
        (ch_x0 + 2.0, ch_y0 + 1.9),
        (ch_x0 + 2.4, ch_y0 + 2.7),
        (ch_x0 + 1.7, ch_y0 + 2.5),
    ]
    for (x, y) in A_dots:
        particle(ax, x, y, 0.20,
                 core="#4fa3d8", halo="#7ec3de", edge="#1e3b57",
                 trail_len=0.9, trail_col="#4fa3d8")

    # Zone B: medium density, shorter trails (amber)
    B_dots = [
        (ch_x0 + 3.4, ch_y0 + 2.4),
        (ch_x0 + 3.8, ch_y0 + 1.0),
        (ch_x0 + 4.1, ch_y0 + 2.0),
        (ch_x0 + 4.6, ch_y0 + 0.6),
        (ch_x0 + 4.9, ch_y0 + 2.5),
        (ch_x0 + 5.3, ch_y0 + 1.6),
        (ch_x0 + 5.6, ch_y0 + 2.2),
        (ch_x0 + 5.2, ch_y0 + 0.9),
    ]
    for (x, y) in B_dots:
        particle(ax, x, y, 0.22,
                 core="#ffc870", halo="#ffb347", edge="#8a5a1a",
                 trail_len=0.45, trail_col="#ffb347")

    # Zone C: jammed cluster pressed against the wall (red, no trails)
    # Arrange in a dense lattice pattern filling the rightmost area.
    jam_x0 = ch_x0 + 6.5
    jam_x1 = wall_x - 0.05
    jam_y0 = ch_y0 + 0.35
    jam_y1 = ch_y1 - 0.35
    r_jam = 0.22
    dx = r_jam * 2.05
    dy = r_jam * 2.15
    ny = int((jam_y1 - jam_y0) / dy) + 1
    nx = int((jam_x1 - jam_x0) / dx) + 1
    for i in range(ny):
        for j in range(nx):
            offset = (dx / 2) if (i % 2 == 1) else 0
            x = jam_x0 + j * dx + offset
            y = jam_y0 + i * dy
            if x > jam_x1 - 0.05:
                continue
            if y > jam_y1 - 0.05:
                continue
            # red particles with subtle heat glow
            particle(ax, x, y, r_jam,
                     core="#e0584f", halo="#f0867e", edge="#7a1d1d")

    # ---- zone dividers (faint) ------------------------------------
    for xv, col in [(ch_x0 + 3.1, "#1f3b57"),
                    (ch_x0 + 6.2, "#1f3b57")]:
        ax.plot([xv, xv], [ch_y0 + 0.15, ch_y1 - 0.15],
                color=col, lw=1.2, alpha=0.25,
                linestyle=(0, (3, 4)), zorder=4)

    # ---- ρ axis beneath the channel with tick at ρ_max -----------
    axis_y = ch_y0 - 0.85
    ax.plot([ch_x0, ch_x1], [axis_y, axis_y],
            color="#1f3b57", lw=2.0, alpha=0.75, zorder=5)
    # tick at 0 (left)
    ax.plot([ch_x0, ch_x0], [axis_y - 0.13, axis_y + 0.13],
            color="#1f3b57", lw=2.4, zorder=5)
    # tick at ρ_max (right) — highlight
    ax.plot([ch_x1, ch_x1], [axis_y - 0.18, axis_y + 0.18],
            color="#c23b3b", lw=3.0, zorder=6)
    for rr, a in [(0.32, 0.12), (0.22, 0.22), (0.14, 0.45)]:
        ax.add_patch(Circle((ch_x1, axis_y), rr,
                            facecolor="#c23b3b", edgecolor="none",
                            alpha=a, zorder=5))
    # arrow along axis
    ax.annotate("",
                xy=(ch_x1 - 0.1, axis_y),
                xytext=(ch_x0 + 0.4, axis_y),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1f3b57", lw=1.8),
                zorder=5)

    # ---- framing ---------------------------------------------------
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
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
