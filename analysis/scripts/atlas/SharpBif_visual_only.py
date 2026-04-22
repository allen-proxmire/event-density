"""
Sharp Bifurcation — visual-only illustration.

Metaphor: a universal knife-edge transition at Δ_crit.

Framed here as an INVARIANT (not a principle like P6): the sharp flip
lives at Δ = 0.5 regardless of the system.

Composition:
  TOP  : two side-by-side phase-portrait regions split by a bright
         golden vertical threshold ridge.
            LEFT  (Δ < 0.5) — four cyan SPIRAL trajectories from
                               different initial conditions, all
                               winding inward toward the origin.
            RIGHT (Δ > 0.5) — four amber MONOTONE trajectories from
                               different initial conditions, each a
                               straight exponential glide toward the
                               origin.
  RIDGE: a glowing vertical bar with a radial starburst behind it.
         A small balanced "knob" sits on top of the ridge at the
         critical point.
  BOTTOM: a Δ-axis from 0 to 1 with a bright golden tick at Δ = 0.5.
         Cyan / amber sub-axes on either side convey the two regimes.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\SharpBif.png"


def build():
    fig, ax = plt.subplots(figsize=(13, 9), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 14, 0, 10], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 14, 1.4,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # =============================================================
    # Layout
    # =============================================================
    ridge_x = 7.0               # glowing threshold position
    panel_x0, panel_x1 = 0.7, 13.3
    panel_y0, panel_y1 = 2.4, 9.3

    # soft washes for two regime panels
    ax.add_patch(FancyBboxPatch(
        (panel_x0, panel_y0), ridge_x - panel_x0 - 0.12, panel_y1 - panel_y0,
        boxstyle="round,pad=0.02,rounding_size=0.28",
        facecolor="#e6f4fa", edgecolor="none", alpha=0.75, zorder=1,
    ))
    ax.add_patch(FancyBboxPatch(
        (ridge_x + 0.12, panel_y0),
        panel_x1 - ridge_x - 0.12, panel_y1 - panel_y0,
        boxstyle="round,pad=0.02,rounding_size=0.28",
        facecolor="#fff2dc", edgecolor="none", alpha=0.75, zorder=1,
    ))

    # =============================================================
    # LEFT phase portrait — spirals (underdamped)
    # =============================================================
    left_cx = (panel_x0 + ridge_x) / 2
    left_cy = (panel_y0 + panel_y1) / 2

    # subtle axes (cross at origin)
    ax.plot([panel_x0 + 0.4, ridge_x - 0.4],
            [left_cy, left_cy],
            color="#1f3b57", lw=1.0, alpha=0.3, zorder=3)
    ax.plot([left_cx, left_cx],
            [panel_y0 + 0.4, panel_y1 - 0.4],
            color="#1f3b57", lw=1.0, alpha=0.3, zorder=3)

    # origin marker
    ax.add_patch(Circle((left_cx, left_cy), 0.11,
                        facecolor="#1f3b57", edgecolor="white",
                        lw=1.4, zorder=8))

    # four spiral trajectories
    def spiral(x0, y0, ccx, ccy, n=300, turns=3.2, decay=0.55,
               color="#1aa6c7", halo="#9fe6f3"):
        # polar approach: start at radius r0 with angle θ0, spiral inward
        dx0, dy0 = x0 - ccx, y0 - ccy
        r0 = np.hypot(dx0, dy0)
        th0 = np.arctan2(dy0, dx0)
        th = th0 + np.linspace(0, turns * 2 * np.pi, n)
        r = r0 * np.exp(-decay * np.linspace(0, 1, n)
                        * turns * 2 * np.pi / (turns * 2 * np.pi))
        r = r0 * np.exp(-decay * np.linspace(0, turns * 2 * np.pi, n)
                        / (2 * np.pi))
        xs = ccx + r * np.cos(th)
        ys = ccy + r * np.sin(th)
        for lw, col, a in [(9, halo, 0.12),
                           (5.5, halo, 0.22),
                           (2.8, color, 0.92)]:
            ax.plot(xs, ys, color=col, lw=lw, alpha=a,
                    solid_capstyle="round", zorder=5)
        # starting-point marker
        ax.add_patch(Circle((xs[0], ys[0]), 0.12,
                            facecolor=color, edgecolor="white",
                            lw=1.4, zorder=9))
        # arrowhead near the inner end
        tip_i = int(0.92 * n)
        ax.annotate("",
                    xy=(xs[tip_i], ys[tip_i]),
                    xytext=(xs[tip_i - 4], ys[tip_i - 4]),
                    arrowprops=dict(arrowstyle="-|>",
                                    color=color, lw=2.0, alpha=0.92),
                    zorder=6)

    spiral_starts = [
        (left_cx + 2.5, left_cy + 1.5),
        (left_cx - 2.1, left_cy + 1.9),
        (left_cx - 2.4, left_cy - 1.6),
        (left_cx + 1.8, left_cy - 2.0),
    ]
    for (sx, sy) in spiral_starts:
        spiral(sx, sy, left_cx, left_cy)

    # regime icon — wavy line in the top-left corner (small badge)
    b_x, b_y = panel_x0 + 0.75, panel_y1 - 0.55
    ax.add_patch(Circle((b_x, b_y), 0.38,
                        facecolor="white", edgecolor="#1aa6c7",
                        lw=2.2, zorder=7))
    wx = np.linspace(b_x - 0.23, b_x + 0.23, 60)
    wy = b_y + 0.11 * np.sin((wx - b_x) * 28)
    ax.plot(wx, wy, color="#1aa6c7", lw=2.4,
            solid_capstyle="round", zorder=8)

    # =============================================================
    # RIGHT phase portrait — monotone decays (overdamped)
    # =============================================================
    right_cx = (ridge_x + panel_x1) / 2
    right_cy = left_cy

    # axes cross
    ax.plot([ridge_x + 0.4, panel_x1 - 0.4],
            [right_cy, right_cy],
            color="#1f3b57", lw=1.0, alpha=0.3, zorder=3)
    ax.plot([right_cx, right_cx],
            [panel_y0 + 0.4, panel_y1 - 0.4],
            color="#1f3b57", lw=1.0, alpha=0.3, zorder=3)

    # origin
    ax.add_patch(Circle((right_cx, right_cy), 0.11,
                        facecolor="#1f3b57", edgecolor="white",
                        lw=1.4, zorder=8))

    # straight monotone decay trajectories — simply lines from IC
    # to the origin, with exponentially dense dots near the origin.
    decay_starts = [
        (right_cx + 2.5, right_cy + 1.6),
        (right_cx - 2.0, right_cy + 2.2),
        (right_cx - 2.5, right_cy - 1.8),
        (right_cx + 2.0, right_cy - 2.2),
    ]
    for (sx, sy) in decay_starts:
        # smooth curve that bends slightly toward origin (critical damping-ish)
        ts_ = np.linspace(0, 1, 200)
        # exponential parametrization for "slows as it approaches"
        dx_ = sx - right_cx
        dy_ = sy - right_cy
        # s(t) = (1 - exp(-k t)) / (1 - exp(-k))  for strong early motion
        k = 3.2
        s = (1 - np.exp(-k * ts_)) / (1 - np.exp(-k))
        xs = right_cx + dx_ * (1 - s)
        ys = right_cy + dy_ * (1 - s)
        for lw, col, a in [(9, "#ffd98a", 0.12),
                           (5.5, "#ffd98a", 0.22),
                           (2.8, "#c97a10", 0.92)]:
            ax.plot(xs, ys, color=col, lw=lw, alpha=a,
                    solid_capstyle="round", zorder=5)
        # start marker
        ax.add_patch(Circle((sx, sy), 0.12,
                            facecolor="#c97a10", edgecolor="white",
                            lw=1.4, zorder=9))
        # arrowhead near origin
        ax.annotate("",
                    xy=(xs[-4], ys[-4]),
                    xytext=(xs[-10], ys[-10]),
                    arrowprops=dict(arrowstyle="-|>",
                                    color="#c97a10",
                                    lw=2.0, alpha=0.92),
                    zorder=6)

    # regime icon — monotone decaying curve, top-right corner
    b_x, b_y = panel_x1 - 0.85, panel_y1 - 0.55
    ax.add_patch(Circle((b_x, b_y), 0.38,
                        facecolor="white", edgecolor="#c97a10",
                        lw=2.2, zorder=7))
    dx_ = np.linspace(b_x - 0.25, b_x + 0.25, 60)
    dn = (dx_ - dx_[0]) / (dx_[-1] - dx_[0])
    dy_ = b_y - 0.15 + 0.28 * np.exp(-3.0 * dn)
    ax.plot(dx_, dy_, color="#c97a10", lw=2.4,
            solid_capstyle="round", zorder=8)

    # =============================================================
    # CENTER — glowing vertical threshold ridge
    # =============================================================
    ridge_y0 = panel_y0 - 0.20
    ridge_y1 = panel_y1 + 0.35

    # radial burst behind the ridge
    for rr, a in [(3.6, 0.03), (2.6, 0.06), (1.8, 0.12),
                  (1.2, 0.22), (0.80, 0.40), (0.50, 0.62)]:
        ax.add_patch(Circle((ridge_x, (ridge_y0 + ridge_y1) / 2), rr,
                            facecolor="#ffd24a", edgecolor="none",
                            alpha=a, zorder=2))

    # soft halo strip
    for gw, a in [(0.95, 0.10), (0.65, 0.17),
                  (0.40, 0.28), (0.24, 0.48)]:
        ax.add_patch(Rectangle(
            (ridge_x - gw / 2, ridge_y0),
            gw, ridge_y1 - ridge_y0,
            facecolor="#ffc23a", edgecolor="none", alpha=a, zorder=3,
        ))

    # main ridge line
    ax.plot([ridge_x, ridge_x], [ridge_y0, ridge_y1],
            color="#ff9f1a", lw=6.0, solid_capstyle="round",
            zorder=5)
    ax.plot([ridge_x, ridge_x], [ridge_y0, ridge_y1],
            color="#fff1b0", lw=2.4, solid_capstyle="round",
            zorder=6)

    # balanced "knob" (ball) on top of the ridge
    kx, ky = ridge_x, ridge_y1 - 0.05
    for rr, a in [(0.42, 0.10), (0.30, 0.22), (0.22, 0.45)]:
        ax.add_patch(Circle((kx, ky + 0.25), rr,
                            facecolor="#ffd24a",
                            edgecolor="none", alpha=a, zorder=8))
    for rr, col in [(0.22, "#ffae79"),
                    (0.18, "#f46d3b"),
                    (0.13, "#c94419")]:
        ax.add_patch(Circle((kx, ky + 0.25), rr,
                            facecolor=col, edgecolor="none", zorder=9))
    ax.add_patch(Circle((kx - 0.06, ky + 0.30), 0.05,
                        facecolor="white", alpha=0.85, zorder=10))
    # little left/right "can tip either way" arrows
    ax.annotate("",
                xy=(kx - 0.62, ky + 0.25),
                xytext=(kx - 0.28, ky + 0.25),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1aa6c7", lw=1.8, alpha=0.75),
                zorder=10)
    ax.annotate("",
                xy=(kx + 0.62, ky + 0.25),
                xytext=(kx + 0.28, ky + 0.25),
                arrowprops=dict(arrowstyle="-|>",
                                color="#c97a10", lw=1.8, alpha=0.75),
                zorder=10)

    # =============================================================
    # Δ-axis at the bottom
    # =============================================================
    ax_y = 1.35
    ax.plot([panel_x0, panel_x1], [ax_y, ax_y],
            color="#1f3b57", lw=2.0, zorder=5)
    ax.annotate("",
                xy=(panel_x1, ax_y),
                xytext=(panel_x0, ax_y),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1f3b57", lw=1.8),
                zorder=5)

    # 0 tick
    ax.plot([panel_x0, panel_x0], [ax_y - 0.16, ax_y + 0.16],
            color="#1f3b57", lw=2.4, zorder=6)
    # 1 tick
    ax.plot([panel_x1, panel_x1], [ax_y - 0.16, ax_y + 0.16],
            color="#1f3b57", lw=2.4, zorder=6)
    # critical tick at Δ = 0.5 (= ridge_x on this axis)
    ax.plot([ridge_x, ridge_x], [ax_y - 0.32, ax_y + 0.32],
            color="#ff9f1a", lw=3.4, zorder=7,
            solid_capstyle="round")
    for rr, a in [(0.42, 0.10), (0.30, 0.22), (0.20, 0.50)]:
        ax.add_patch(Circle((ridge_x, ax_y), rr,
                            facecolor="#ffd24a",
                            edgecolor="none", alpha=a, zorder=6))
    ax.add_patch(Circle((ridge_x, ax_y), 0.16,
                        facecolor="#fff1b0",
                        edgecolor="#d69a1a", lw=2.0, zorder=8))

    # small "left regime" / "right regime" colored segments on axis
    ax.plot([panel_x0 + 0.1, ridge_x - 0.16], [ax_y - 0.55, ax_y - 0.55],
            color="#1aa6c7", lw=6.0, solid_capstyle="round",
            alpha=0.6, zorder=5)
    ax.plot([ridge_x + 0.16, panel_x1 - 0.1], [ax_y - 0.55, ax_y - 0.55],
            color="#c97a10", lw=6.0, solid_capstyle="round",
            alpha=0.6, zorder=5)

    # ---- framing ---------------------------------------------------
    ax.set_xlim(0, 14)
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
