"""
Penalty channel alone — visual-only illustration.

Metaphor: three time snapshots of a *uniform* field relaxing toward
equilibrium ρ*.  The key visual point — distinct from P3's "ball in a
well" equilibrium image — is that there is NO spatial structure.  Each
snapshot is a flat uniform field.  Only the overall level decays over
time, exponentially approaching the glowing amber ρ* baseline.

Composition:
  TOP    : three stacked square panels, each rendered as a perfectly
           uniform color slab.  Left = high density (saturated amber),
           middle = intermediate, right = at ρ* (pale).  Arrows between
           them indicate time progression.
  BOTTOM : a time-trace ρ(t) showing pure exponential decay from high
           to ρ*, the glowing amber horizontal line as the asymptote.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\Penalty_alone.png"


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
    # Three time-snapshot slabs (uniform fields)
    # =============================================================
    slab_y = 6.3
    slab_h = 3.1
    slab_w = 2.7
    gap = 0.95
    total_w = 3 * slab_w + 2 * gap
    start_x = (13 - total_w) / 2

    # three fill colors decaying toward an asymptotic ρ* (pale amber)
    slab_levels = [
        ("#e07b00", "#c4640a"),   # t1 — saturated amber (high density)
        ("#ffb347", "#d48818"),   # t2 — mid amber
        ("#fff1b0", "#d4b56a"),   # t3 — near ρ*, pale
    ]

    slab_xs = []

    for i, (face, edge) in enumerate(slab_levels):
        x0 = start_x + i * (slab_w + gap)
        slab_xs.append(x0 + slab_w / 2)

        # soft shadow
        ax.add_patch(FancyBboxPatch(
            (x0 + 0.07, slab_y - 0.13), slab_w, slab_h,
            boxstyle="round,pad=0.02,rounding_size=0.22",
            facecolor="#00000018", edgecolor="none", zorder=2,
        ))
        # uniform fill
        ax.add_patch(FancyBboxPatch(
            (x0, slab_y), slab_w, slab_h,
            boxstyle="round,pad=0.02,rounding_size=0.22",
            facecolor=face, edgecolor=edge, lw=2.8, zorder=3,
        ))
        # subtle highlight to give the slab a glass-like face
        ax.add_patch(Rectangle(
            (x0 + 0.18, slab_y + 0.25), 0.32, slab_h - 0.55,
            facecolor="white", alpha=0.18, zorder=4,
        ))
        ax.add_patch(Rectangle(
            (x0 + slab_w - 0.28, slab_y + 0.35), 0.10, slab_h - 0.90,
            facecolor="white", alpha=0.10, zorder=4,
        ))
        # dot grid pattern — ALL uniform to emphasize "no spatial structure"
        # (equally spaced, equal intensity)
        rows, cols = 4, 5
        for rr in range(rows):
            for cc in range(cols):
                dx = x0 + 0.35 + cc * ((slab_w - 0.70) / (cols - 1))
                dy = slab_y + 0.55 + rr * ((slab_h - 1.15) / (rows - 1))
                ax.add_patch(Circle(
                    (dx, dy), 0.08,
                    facecolor="white", edgecolor="none",
                    alpha=0.55, zorder=5,
                ))

    # ---- arrows between slabs (time progression) ------------------
    for i in range(2):
        x_left = start_x + (i + 1) * slab_w + i * gap
        x_right = x_left + gap
        y_mid = slab_y + slab_h / 2
        arrow = FancyArrowPatch(
            (x_left + 0.10, y_mid),
            (x_right - 0.10, y_mid),
            arrowstyle="-|>", mutation_scale=24,
            color="#1f3b57", lw=3.0, zorder=6,
        )
        ax.add_patch(arrow)
        # small glow under arrow
        for lw, a in [(9, 0.12), (5, 0.22)]:
            ax.plot([x_left + 0.10, x_right - 0.10],
                    [y_mid, y_mid],
                    color="#ffd24a", lw=lw, alpha=a,
                    solid_capstyle="round", zorder=5)

    # ---- tiny clock-icon badge above each arrow -------------------
    for i in range(2):
        x_left = start_x + (i + 1) * slab_w + i * gap
        x_right = x_left + gap
        x_mid = (x_left + x_right) / 2
        y_badge = slab_y + slab_h / 2 + 0.72
        ax.add_patch(Circle((x_mid, y_badge), 0.24,
                            facecolor="white", edgecolor="#1f3b57",
                            lw=1.8, zorder=8))
        ax.add_patch(Circle((x_mid, y_badge), 0.05,
                            facecolor="#1f3b57", zorder=9))
        ax.plot([x_mid, x_mid + 0.14], [y_badge, y_badge + 0.11],
                color="#1f3b57", lw=1.8, solid_capstyle="round",
                zorder=9)

    # =============================================================
    # Bottom panel: ρ(t) exponential decay toward ρ*
    # =============================================================
    ax_x0, ax_x1 = 1.1, 11.9
    ax_y0 = 2.1       # ρ* baseline (bottom of curve)
    ax_y_top = 5.2    # top of plot region

    # panel background
    ax.add_patch(FancyBboxPatch(
        (ax_x0 - 0.25, ax_y0 - 0.40),
        ax_x1 - ax_x0 + 0.5,
        ax_y_top - ax_y0 + 0.55,
        boxstyle="round,pad=0.04,rounding_size=0.18",
        facecolor="white", edgecolor="#1f3b57",
        lw=1.5, alpha=0.88, zorder=2,
    ))

    # ---- glowing ρ* baseline (horizontal) -------------------------
    for glow_h, a in [(0.60, 0.06), (0.40, 0.12),
                      (0.24, 0.22), (0.14, 0.38), (0.08, 0.65)]:
        ax.add_patch(Rectangle(
            (ax_x0, ax_y0 - glow_h / 2),
            ax_x1 - ax_x0, glow_h,
            facecolor="#ffc23a", edgecolor="none",
            alpha=a, zorder=3,
        ))
    ax.plot([ax_x0, ax_x1], [ax_y0, ax_y0],
            color="#ff9f1a", lw=4.5, zorder=5,
            solid_capstyle="round")
    ax.plot([ax_x0, ax_x1], [ax_y0, ax_y0],
            color="#fff1b0", lw=1.8, zorder=6,
            solid_capstyle="round")

    # axes
    ax.plot([ax_x0, ax_x1], [ax_y0, ax_y0],
            color="#1f3b57", lw=1.2, alpha=0.0)   # invisible, baseline is glow
    # y-axis (subtle)
    ax.plot([ax_x0, ax_x0], [ax_y0, ax_y_top],
            color="#1f3b57", lw=1.6, alpha=0.75, zorder=4)
    # arrow on t axis
    ax.annotate("", xy=(ax_x1 - 0.08, ax_y0 - 0.35),
                xytext=(ax_x0, ax_y0 - 0.35),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1f3b57", lw=1.8),
                zorder=5)

    # exponential decay curve: ρ(t) = ρ* + (ρ0 - ρ*) e^{-k t}
    ts = np.linspace(ax_x0 + 0.2, ax_x1 - 0.2, 400)
    tn = (ts - ts[0]) / (ts[-1] - ts[0])
    rho0_top = ax_y_top - 0.25
    decay = (rho0_top - ax_y0) * np.exp(-3.5 * tn) + ax_y0

    # shaded area between curve and ρ* baseline
    ax.fill_between(ts, ax_y0, decay,
                    color="#ffd98a", alpha=0.35, zorder=4)

    # glow strokes
    for lw, col, a in [(11, "#ffd98a", 0.12),
                       (7, "#ffb347", 0.24),
                       (3.6, "#c97a10", 0.95)]:
        ax.plot(ts, decay, color=col, lw=lw, alpha=a,
                solid_capstyle="round", zorder=6)

    # dots at the three time points matching the slab snapshots
    t_pts = [0.05, 0.30, 0.75]
    for t_norm, (face, _) in zip(t_pts, slab_levels):
        x_pt = ts[0] + t_norm * (ts[-1] - ts[0])
        y_pt = (rho0_top - ax_y0) * np.exp(-3.5 * t_norm) + ax_y0
        for rr, a in [(0.26, 0.18), (0.18, 0.40)]:
            ax.add_patch(Circle((x_pt, y_pt), rr,
                                facecolor=face, edgecolor="none",
                                alpha=a, zorder=7))
        ax.add_patch(Circle((x_pt, y_pt), 0.13,
                            facecolor=face,
                            edgecolor="#1f3b57", lw=1.6, zorder=9))
        # vertical dashed line from the time-point to the corresponding slab
        # (only for first two, going upward — to show the slabs above
        # represent these time samples)
        ax.plot([x_pt, x_pt], [y_pt + 0.18, ax_y_top + 0.1],
                color="#1f3b57", lw=1.0, alpha=0.30,
                linestyle=(0, (3, 3)), zorder=4)

    # tiny pin/tick highlighting the ρ* convergence
    rho_star_x = ax_x1 - 0.45
    ax.add_patch(Circle((rho_star_x, ax_y0), 0.16,
                        facecolor="#fff1b0",
                        edgecolor="#c97a10", lw=1.8, zorder=9))

    # ---- faint coupling between slabs and their time-points ------
    for x_mid_slab, x_mid_time, face in zip(
        slab_xs, t_pts, [s[0] for s in slab_levels]
    ):
        x_t = ts[0] + x_mid_time * (ts[-1] - ts[0])
        ax.plot([x_mid_slab, x_t], [slab_y - 0.05, ax_y_top + 0.10],
                color=face, lw=1.2, alpha=0.40,
                linestyle=(0, (3, 4)), zorder=2)

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
