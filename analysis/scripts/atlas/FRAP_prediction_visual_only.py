"""
FRAP prediction / experiment — visual-only illustration.

Prediction-experiment framing: contrast standard diffusion's smooth
monotone recovery against ED's damped-oscillatory recovery signature,
on the same axes. Decision fork is visually explicit.

Composition:
  LEFT  : microscope field disc with central bleached spot and coral
          ringing pulses (the ED prediction "live").
  RIGHT : two overlaid recovery curves on the same I(t) plot —
          AMBER DASHED : standard diffusion / classical prediction
                         (smooth monotone rise to asymptote)
          CORAL SOLID  : ED participation prediction (overshoot + ring)
          A small decision-fork diamond marks where the two curves
          diverge.
  CORNER: pending hourglass badge.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch, Polygon,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\FRAP_prediction.png"


def build():
    fig, ax = plt.subplots(figsize=(13, 9), dpi=220)

    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 14, 0, 10], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 14, 1.5,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # ---- LEFT: microscope field ----------------------------------
    fov_cx, fov_cy = 3.6, 5.0
    fov_R = 2.9
    bleach_R = 1.0

    for rr, a in [(fov_R + 0.45, 0.08), (fov_R + 0.25, 0.16),
                  (fov_R + 0.12, 0.28)]:
        ax.add_patch(Circle((fov_cx, fov_cy), rr,
                            facecolor="#2a4c6e",
                            edgecolor="none", alpha=a, zorder=2))
    ax.add_patch(Circle((fov_cx, fov_cy), fov_R,
                        facecolor="#0f2038",
                        edgecolor="#6b8aa8", lw=2.6, zorder=3))

    # fluorescent BSA particles
    rng = np.random.default_rng(5)
    placed = 0
    for _ in range(800):
        x = rng.uniform(fov_cx - fov_R + 0.15, fov_cx + fov_R - 0.15)
        y = rng.uniform(fov_cy - fov_R + 0.15, fov_cy + fov_R - 0.15)
        r_from_c = np.hypot(x - fov_cx, y - fov_cy)
        if r_from_c > fov_R - 0.15:
            continue
        if r_from_c < bleach_R * 0.9:
            continue
        if placed >= 220:
            break
        placed += 1
        for rr, aa in [(0.10, 0.15), (0.07, 0.30), (0.05, 0.55)]:
            ax.add_patch(Circle((x, y), rr,
                                facecolor="#b6f06a", edgecolor="none",
                                alpha=aa, zorder=4))
        ax.add_patch(Circle((x, y), 0.03,
                            facecolor="#ecffc1",
                            edgecolor="#548526", lw=0.4,
                            alpha=0.95, zorder=5))

    # bleached dark disc
    for rr, a in [(bleach_R + 0.35, 0.10), (bleach_R + 0.22, 0.18),
                  (bleach_R + 0.12, 0.30)]:
        ax.add_patch(Circle((fov_cx, fov_cy), rr,
                            facecolor="#08142a",
                            edgecolor="none", alpha=a, zorder=6))
    ax.add_patch(Circle((fov_cx, fov_cy), bleach_R,
                        facecolor="#081a30",
                        edgecolor="#3a557a", lw=2.0, zorder=7))

    # coral pulsing rings emanating from bleach
    for rr, a, lw in [(bleach_R + 0.45, 0.85, 4.0),
                      (bleach_R + 0.85, 0.55, 3.2),
                      (bleach_R + 1.25, 0.30, 2.6),
                      (bleach_R + 1.60, 0.18, 2.2)]:
        for lw_h, ah in [(lw + 6, a * 0.35), (lw + 3, a * 0.55)]:
            ax.add_patch(Circle((fov_cx, fov_cy), rr,
                                facecolor="none", edgecolor="#ffae79",
                                lw=lw_h, alpha=ah, zorder=8))
        ax.add_patch(Circle((fov_cx, fov_cy), rr,
                            facecolor="none", edgecolor="#f46d3b",
                            lw=lw, alpha=a, zorder=9))

    # center pulse
    for rr, a in [(0.30, 0.20), (0.20, 0.40)]:
        ax.add_patch(Circle((fov_cx, fov_cy), rr,
                            facecolor="#ffae79",
                            edgecolor="none", alpha=a, zorder=10))
    ax.add_patch(Circle((fov_cx, fov_cy), 0.10,
                        facecolor="#f46d3b",
                        edgecolor="#7a2d0b", lw=1.2, zorder=11))

    # ---- RIGHT: comparison recovery curves -----------------------
    rx0, rx1 = 7.8, 13.6
    ry_base = 2.2
    ry_asymp = 6.3
    ry_top = 7.9

    ax.add_patch(FancyBboxPatch(
        (rx0 - 0.30, ry_base - 0.40),
        rx1 - rx0 + 0.60, ry_top - ry_base + 0.70,
        boxstyle="round,pad=0.04,rounding_size=0.20",
        facecolor="white", edgecolor="#1f3b57",
        lw=1.5, alpha=0.92, zorder=3,
    ))

    # axes
    ax.plot([rx0 + 0.1, rx0 + 0.1], [ry_base + 0.1, ry_top - 0.1],
            color="#1f3b57", lw=1.6, alpha=0.7, zorder=5)
    ax.plot([rx0 + 0.1, rx1 - 0.1], [ry_base, ry_base],
            color="#1f3b57", lw=1.6, alpha=0.75, zorder=5)

    # asymptote
    ax.plot([rx0 + 0.1, rx1 - 0.1], [ry_asymp, ry_asymp],
            color="#1f3b57", lw=1.0, alpha=0.30,
            linestyle=(0, (5, 4)), zorder=5)

    ts = np.linspace(rx0 + 0.30, rx1 - 0.25, 700)
    tn = (ts - ts[0]) / (ts[-1] - ts[0])
    scale = ry_asymp - ry_base

    # CLASSICAL smooth recovery (amber dashed)
    y_classical = ry_base + (1 - np.exp(-3.2 * tn * 1.55)) * scale
    for lw, col, a in [(9, "#ffd98a", 0.14),
                       (5.5, "#ffb347", 0.25)]:
        ax.plot(ts, y_classical, color=col, lw=lw, alpha=a,
                solid_capstyle="round", zorder=6)
    ax.plot(ts, y_classical, color="#c97a10", lw=2.8,
            linestyle=(0, (8, 4)), alpha=0.92, zorder=7,
            solid_capstyle="round")

    # ED damped-oscillatory recovery (coral solid)
    zeta = 0.16
    wn = 16.0
    wd = wn * np.sqrt(1 - zeta ** 2)
    t_sc = tn * 1.55
    y_ed = 1.0 - np.exp(-zeta * wn * t_sc) * (
        np.cos(wd * t_sc)
        + (zeta / np.sqrt(1 - zeta ** 2)) * np.sin(wd * t_sc)
    )
    y_ed = ry_base + y_ed * scale
    for lw, col, a in [(12, "#ffd4b0", 0.14),
                       (8, "#ffae79", 0.24),
                       (4.0, "#c94419", 0.98)]:
        ax.plot(ts, y_ed, color=col, lw=lw, alpha=a,
                solid_capstyle="round", zorder=7)

    # start-of-divergence fork marker
    # find where |y_ed - y_classical| first exceeds threshold
    diff = np.abs(y_ed - y_classical)
    idx_fork = np.argmax(diff > 0.25 * scale)
    fx = ts[idx_fork]
    fy = (y_ed[idx_fork] + y_classical[idx_fork]) / 2
    # fork diamond
    for rr, a in [(0.30, 0.15), (0.20, 0.35)]:
        ax.add_patch(Circle((fx, fy), rr,
                            facecolor="#ffd24a", edgecolor="none",
                            alpha=a, zorder=9))
    diamond = [(fx, fy + 0.22), (fx + 0.22, fy),
               (fx, fy - 0.22), (fx - 0.22, fy)]
    ax.add_patch(Polygon(diamond, closed=True,
                         facecolor="white", edgecolor="#c97a10",
                         lw=2.0, zorder=10))
    ax.plot([fx - 0.10, fx + 0.10], [fy, fy],
            color="#c97a10", lw=2.0, zorder=11,
            solid_capstyle="round")
    ax.plot([fx, fx], [fy - 0.10, fy + 0.10],
            color="#c97a10", lw=2.0, zorder=11,
            solid_capstyle="round")

    # bleach event tick
    ax.plot([rx0 + 0.30, rx0 + 0.30], [ry_base, ry_base + 0.35],
            color="#c94419", lw=2.4, alpha=0.9,
            solid_capstyle="round", zorder=8)
    ax.add_patch(Circle((rx0 + 0.30, ry_base + 0.38), 0.10,
                        facecolor="#c94419", edgecolor="#7a2d0b",
                        lw=1.0, zorder=9))

    # legend swatches — two tiny color keys (no text in image)
    lx = rx0 + 0.4
    # ED swatch
    ax.plot([lx, lx + 0.55], [ry_top - 0.25, ry_top - 0.25],
            color="#c94419", lw=3.2, solid_capstyle="round", zorder=10)
    ax.add_patch(Circle((lx + 0.70, ry_top - 0.25), 0.10,
                        facecolor="#c94419", edgecolor="white",
                        lw=1.0, zorder=10))
    # Classical swatch
    ax.plot([lx, lx + 0.55], [ry_top - 0.55, ry_top - 0.55],
            color="#c97a10", lw=3.0,
            linestyle=(0, (8, 4)), solid_capstyle="round", zorder=10)
    ax.add_patch(Circle((lx + 0.70, ry_top - 0.55), 0.10,
                        facecolor="#c97a10", edgecolor="white",
                        lw=1.0, zorder=10))

    # Connector from bleach to curve-start
    ax.annotate("", xy=(rx0 + 0.30, ry_base + 0.55),
                xytext=(fov_cx + bleach_R * 0.9, fov_cy - bleach_R * 0.75),
                arrowprops=dict(arrowstyle="-|>",
                                color="#c94419", lw=2.0, alpha=0.70,
                                connectionstyle="arc3,rad=-0.25",
                                linestyle=(0, (4, 3))),
                zorder=7)

    # ---- Pending hourglass badge (corner) ------------------------
    hb_x, hb_y = 13.3, 9.3
    for rr, a in [(0.55, 0.10), (0.42, 0.18)]:
        ax.add_patch(Circle((hb_x, hb_y), rr,
                            facecolor="#ffd24a",
                            edgecolor="none", alpha=a, zorder=9))
    ax.add_patch(Circle((hb_x, hb_y), 0.38,
                        facecolor="white", edgecolor="#c97a10",
                        lw=2.4, zorder=10))
    # hourglass glyph
    hg = [(hb_x - 0.17, hb_y + 0.20),
          (hb_x + 0.17, hb_y + 0.20),
          (hb_x - 0.17, hb_y - 0.20),
          (hb_x + 0.17, hb_y - 0.20)]
    ax.plot([hg[0][0], hg[1][0]], [hg[0][1], hg[1][1]],
            color="#c97a10", lw=2.6, zorder=11)
    ax.plot([hg[2][0], hg[3][0]], [hg[2][1], hg[3][1]],
            color="#c97a10", lw=2.6, zorder=11)
    ax.plot([hg[0][0], hg[3][0]], [hg[0][1], hg[3][1]],
            color="#c97a10", lw=2.2, zorder=11)
    ax.plot([hg[1][0], hg[2][0]], [hg[1][1], hg[2][1]],
            color="#c97a10", lw=2.2, zorder=11)
    # sand in bottom half
    ax.add_patch(Polygon([(hb_x - 0.10, hb_y - 0.18),
                          (hb_x + 0.10, hb_y - 0.18),
                          (hb_x, hb_y - 0.02)],
                         closed=True, facecolor="#ffb347",
                         edgecolor="none", alpha=0.85, zorder=11))

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
