"""
P3 Penalty Equilibrium — visual-only illustration.

Metaphor: a smooth potential well with a single stable minimum.
  - A curved bowl drawn as a shaded 2D potential  P(ρ)
  - A glowing ball resting at the bottom (the equilibrium ρ*)
  - Two faded "ghost" balls at off-equilibrium positions with curved
    arrows pointing back toward the minimum (restoring force)
  - A glowing horizontal baseline at P = 0 beneath the minimum
  - A small amber indicator marks ρ* on that baseline
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch,
)
from matplotlib.collections import LineCollection

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\P3_penalty_equilibrium.png"


def build():
    fig, ax = plt.subplots(figsize=(11, 10), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 12, 0, 11], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 12, 1.6,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # ---- potential curve P(ρ) -------------------------------------
    # Soft quartic-ish bowl, centered at x = 6
    xmin, xmax = 1.0, 11.0
    x_eq = 6.0                      # equilibrium ρ*
    y_min_curve = 2.30              # P(ρ*) = 0 visually mapped here
    curve_scale = 0.18              # steepness

    x = np.linspace(xmin, xmax, 800)
    # a blend of quadratic (soft floor) and quartic (rising walls)
    y = y_min_curve + curve_scale * (0.6 * (x - x_eq) ** 2
                                     + 0.03 * (x - x_eq) ** 4)
    # cap the top so the walls don't run off the panel
    y_cap = 9.0
    y = np.minimum(y, y_cap)

    # ---- fill the inside of the bowl with a vertical gradient ----
    # Use many thin vertical slabs below the curve down to baseline.
    baseline_y = y_min_curve
    nx = 260
    for i in range(nx - 1):
        x0, x1 = x[i * (len(x) // nx)], x[(i + 1) * (len(x) // nx)]
        y_top = 0.5 * (y[i * (len(x) // nx)] + y[(i + 1) * (len(x) // nx)])
        # vertical gradient inside this slab
        nlayers = 25
        for j in range(nlayers):
            frac = j / nlayers
            yy0 = baseline_y + frac * (y_top - baseline_y)
            c = plt.cm.GnBu(0.28 + 0.30 * (1 - frac))
            ax.add_patch(Rectangle(
                (x0, yy0), x1 - x0,
                (y_top - baseline_y) / nlayers + 0.02,
                facecolor=c, edgecolor="none", alpha=0.55, zorder=2,
            ))

    # outer curve: soft glow underlay + crisp main stroke
    for lw, col, a in [(10, "#9fe6f3", 0.16),
                       (6, "#6fd2e9", 0.28),
                       (3.5, "#2a7fa3", 0.55)]:
        ax.plot(x, y, color=col, lw=lw, alpha=a,
                solid_capstyle="round", zorder=3)
    ax.plot(x, y, color="#1f3b57", lw=2.8,
            solid_capstyle="round", zorder=5)

    # A few faint iso-contour-style horizontal helper lines inside
    for yh in [3.3, 4.6, 6.2]:
        # find the x-range where y(x) ≥ yh
        mask = y >= yh
        if mask.any():
            x_lo = x[mask][0]
            x_hi = x[mask][-1]
            ax.plot([x_lo, x_hi], [yh, yh],
                    color="#1f3b57", lw=0.9, alpha=0.22,
                    linestyle=(0, (4, 3)), zorder=3)

    # ---- glowing P = 0 baseline at the bowl floor -----------------
    for glow_h, a in [(0.60, 0.06), (0.40, 0.12),
                      (0.24, 0.22), (0.14, 0.38), (0.08, 0.65)]:
        ax.add_patch(Rectangle(
            (xmin - 0.1, baseline_y - glow_h / 2),
            xmax - xmin + 0.2, glow_h,
            facecolor="#ffc23a", edgecolor="none", alpha=a, zorder=1,
        ))
    ax.plot([xmin + 0.1, xmax - 0.1], [baseline_y, baseline_y],
            color="#ff9f1a", lw=5.0, zorder=4, solid_capstyle="round")
    ax.plot([xmin + 0.1, xmax - 0.1], [baseline_y, baseline_y],
            color="#fff1b0", lw=2.0, zorder=5, solid_capstyle="round")

    # ---- equilibrium ball at the bottom ---------------------------
    ball_r = 0.42
    ball_cx = x_eq
    # rest position sits on the curve at its minimum
    ball_cy = baseline_y + ball_r  # so it sits on the baseline

    # soft halo
    for rr, a in [(ball_r * 2.1, 0.08),
                  (ball_r * 1.65, 0.15),
                  (ball_r * 1.30, 0.28)]:
        ax.add_patch(Circle((ball_cx, ball_cy), rr,
                            facecolor="#ffd24a", edgecolor="none",
                            alpha=a, zorder=6))

    # sphere (radial shading via stacked circles)
    for rr, col in [
        (ball_r, "#c23b3b"),
        (ball_r * 0.95, "#d84949"),
        (ball_r * 0.80, "#e36060"),
        (ball_r * 0.65, "#ec7e7e"),
        (ball_r * 0.50, "#f3a1a1"),
        (ball_r * 0.38, "#f8c2c2"),
    ]:
        ax.add_patch(Circle(
            (ball_cx - 0.05 * (ball_r - rr) / ball_r,
             ball_cy + 0.05 * (ball_r - rr) / ball_r),
            rr, facecolor=col, edgecolor="none", zorder=7,
        ))
    # specular highlight
    ax.add_patch(Circle(
        (ball_cx - 0.14, ball_cy + 0.17),
        0.12, facecolor="white", alpha=0.85, zorder=9,
    ))
    # crisp outline
    ax.add_patch(Circle(
        (ball_cx, ball_cy), ball_r,
        facecolor="none", edgecolor="#7a1d1d", lw=1.6, zorder=8,
    ))

    # small contact shadow under the ball
    ax.add_patch(Circle((ball_cx, baseline_y - 0.06), ball_r * 0.6,
                        facecolor="#000000", alpha=0.18, zorder=3))

    # ---- equilibrium marker ρ* on the baseline --------------------
    # vertical dashed line from baseline to ball
    ax.plot([ball_cx, ball_cx], [baseline_y - 0.7, baseline_y - 0.05],
            color="#c97a10", lw=1.8, linestyle=(0, (4, 3)),
            alpha=0.9, zorder=4)
    # star-burst / pin marker
    pin_x, pin_y = ball_cx, baseline_y - 0.80
    for rr, a in [(0.32, 0.15), (0.24, 0.28), (0.18, 0.55)]:
        ax.add_patch(Circle((pin_x, pin_y), rr,
                            facecolor="#ffd24a", edgecolor="none",
                            alpha=a, zorder=5))
    ax.add_patch(Circle((pin_x, pin_y), 0.14,
                        facecolor="#fff1b0", edgecolor="#c97a10",
                        lw=2.0, zorder=6))

    # ---- ghost balls with restoring arrows ------------------------
    def ghost_ball(gx):
        # find curve height at gx
        gy = baseline_y + curve_scale * (0.6 * (gx - x_eq) ** 2
                                          + 0.03 * (gx - x_eq) ** 4)
        # place on curve
        gcy = gy + ball_r * 0.9
        # faded sphere
        for rr, col in [
            (ball_r * 0.82, "#c23b3b"),
            (ball_r * 0.72, "#e07070"),
            (ball_r * 0.58, "#f1a1a1"),
            (ball_r * 0.42, "#f7c8c8"),
        ]:
            ax.add_patch(Circle((gx, gcy), rr,
                                facecolor=col, edgecolor="none",
                                alpha=0.45, zorder=6))
        ax.add_patch(Circle((gx, gcy), ball_r * 0.82,
                            facecolor="none", edgecolor="#7a1d1d",
                            lw=1.2, alpha=0.55, zorder=7))
        # highlight
        ax.add_patch(Circle((gx - 0.10, gcy + 0.12),
                            ball_r * 0.20,
                            facecolor="white", alpha=0.4, zorder=8))

        # curved restoring arrow from ghost back toward minimum
        # drop slightly below ghost toward the bowl path
        target = (ball_cx + (0.8 if gx < x_eq else -0.8),
                  ball_cy + 0.1)
        rad = 0.35 if gx < x_eq else -0.35
        arrow = FancyArrowPatch(
            (gx, gcy),
            target,
            arrowstyle="-|>", mutation_scale=20,
            color="#c23b3b", lw=2.6,
            connectionstyle=f"arc3,rad={rad}",
            alpha=0.85, zorder=9,
        )
        ax.add_patch(arrow)

    ghost_ball(3.5)
    ghost_ball(8.5)

    # ---- framing ---------------------------------------------------
    ax.set_xlim(0, 12)
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
