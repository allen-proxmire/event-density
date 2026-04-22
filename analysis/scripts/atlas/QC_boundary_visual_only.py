"""
Q-C boundary (ED-09.5) — visual-only illustration.

Prediction: the quantum-to-classical transition is structurally sharp
at a system-dependent internal-complexity threshold — not the smooth
environmental-decoherence fade predicted by standard quantum mechanics.

Composition:
  LEFT   : a stylized matter-wave / levitated-nanoparticle experiment
           (source + interference-pattern field).  A cool-navy backdrop
           signals "quantum regime."
  MAIN   : a coherence-vs-complexity plot with TWO predicted curves:
             AMBER DASHED : standard decoherence — smooth monotonic fade
             CORAL SOLID  : ED-09.5 — sharp cliff at the complexity
                            threshold, with an emphasized vertical drop
           A bright golden threshold line marks the ED-09.5 critical
           complexity.
  CORNER : pending hourglass badge.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch, Polygon, Ellipse,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\QC_boundary.png"


def build():
    fig, ax = plt.subplots(figsize=(13, 9), dpi=220)

    # deep-navy top half (quantum mood), warm floor at bottom
    N = 600
    grad = np.zeros((N, N, 3))
    for i in range(N):
        t = i / (N - 1)
        c_top = np.array([0.08, 0.11, 0.22])
        c_bot = np.array([0.12, 0.15, 0.28])
        grad[i, :, :] = (1 - t) * c_top + t * c_bot
    ax.imshow(grad, extent=[0, 14, 1.2, 10], aspect="auto", zorder=0)
    ax.add_patch(Rectangle((0, 0), 14, 1.3,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # faint starfield in top-left (experiment panel zone)
    rng_bg = np.random.default_rng(4)
    for _ in range(100):
        x = rng_bg.uniform(0.2, 6.0)
        y = rng_bg.uniform(1.5, 9.5)
        r = rng_bg.uniform(0.012, 0.04)
        a = rng_bg.uniform(0.2, 0.7)
        ax.add_patch(Circle((x, y), r,
                            facecolor="#eceaff",
                            edgecolor="none", alpha=a, zorder=1))

    # =============================================================
    # LEFT panel: matter-wave experiment
    # =============================================================
    ex0, ex1 = 0.5, 6.0
    ey0, ey1 = 2.0, 8.7

    # panel frame (translucent dark with lavender edge)
    for pad, a in [(0.25, 0.05), (0.15, 0.10), (0.08, 0.22)]:
        ax.add_patch(FancyBboxPatch(
            (ex0 - pad, ey0 - pad),
            ex1 - ex0 + 2 * pad, ey1 - ey0 + 2 * pad,
            boxstyle="round,pad=0.02,rounding_size=0.22",
            facecolor="#6a3fb0", edgecolor="none",
            alpha=a, zorder=2,
        ))
    ax.add_patch(FancyBboxPatch(
        (ex0, ey0), ex1 - ex0, ey1 - ey0,
        boxstyle="round,pad=0.02,rounding_size=0.22",
        facecolor="#131a2c", edgecolor="#8a5ac9",
        lw=2.6, alpha=0.93, zorder=3,
    ))

    # source (left side of experiment) — a levitated nanoparticle / oven
    src_cx, src_cy = ex0 + 0.8, (ey0 + ey1) / 2
    for rr, a in [(0.45, 0.10), (0.32, 0.22), (0.22, 0.45)]:
        ax.add_patch(Circle((src_cx, src_cy), rr,
                            facecolor="#9fe6f3",
                            edgecolor="none", alpha=a, zorder=4))
    ax.add_patch(Circle((src_cx, src_cy), 0.18,
                        facecolor="#57c6e6",
                        edgecolor="#0b4a68", lw=1.6, zorder=5))

    # slit assembly (middle of experiment)
    slit_x = ex0 + 2.2
    slit_y_top = ey1 - 0.55
    slit_y_bot = ey0 + 0.55
    # slit bars
    ax.add_patch(Rectangle((slit_x - 0.08, slit_y_top - 0.40),
                           0.16, 0.40,
                           facecolor="#e6d6ff",
                           edgecolor="#6a3fb0", lw=1.4, zorder=6))
    ax.add_patch(Rectangle((slit_x - 0.08, (ey0 + ey1) / 2 - 0.45),
                           0.16, 0.95,
                           facecolor="#e6d6ff",
                           edgecolor="#6a3fb0", lw=1.4, zorder=6))
    ax.add_patch(Rectangle((slit_x - 0.08, slit_y_bot),
                           0.16, 0.40,
                           facecolor="#e6d6ff",
                           edgecolor="#6a3fb0", lw=1.4, zorder=6))

    # matter-wave beam from source through slits
    # three curving wave fronts
    for phase in np.linspace(0, 4 * np.pi, 16):
        x_line = np.linspace(src_cx + 0.20, slit_x - 0.10, 80)
        # cylindrical wavefront expanding
        ampl = 0.12
        y_ref = src_cy
        # draw as a pair of faint lines
        ax.plot(x_line,
                y_ref + ampl * np.sin(
                    (x_line - src_cx) * 12 + phase),
                color="#9fe6f3", lw=0.9, alpha=0.20, zorder=4)

    # after the slits: two partial waves
    for yy in [(ey0 + ey1) / 2 + 0.75, (ey0 + ey1) / 2 - 0.75]:
        xs = np.linspace(slit_x + 0.10, ex1 - 0.55, 100)
        # emergent wavefronts
        for phase in np.linspace(0, 4 * np.pi, 12):
            ax.plot(xs,
                    yy + 0.10 * np.sin((xs - slit_x) * 14 + phase),
                    color="#c8aff0", lw=0.8, alpha=0.18, zorder=5)

    # detector screen (right side)
    det_x = ex1 - 0.35
    ax.add_patch(Rectangle((det_x, ey0 + 0.35),
                           0.08, ey1 - ey0 - 0.7,
                           facecolor="#e6d6ff",
                           edgecolor="#6a3fb0", lw=1.2, zorder=6))

    # interference fringes on detector (alternating bright bars)
    fringe_x = det_x - 0.45
    for i in range(9):
        fy = ey0 + 0.55 + i * ((ey1 - ey0 - 1.1) / 8)
        intensity = (np.cos(i * 1.1) + 1) / 2 * 0.9 + 0.1
        ax.add_patch(Rectangle(
            (fringe_x, fy - 0.06), 0.35, 0.12,
            facecolor="#ffd98a",
            edgecolor="none", alpha=intensity, zorder=7,
        ))

    # tiny "particle" dot at source (suggesting wave/particle)
    ax.add_patch(Circle((src_cx, src_cy), 0.07,
                        facecolor="#fff1b0",
                        edgecolor="#c97a10", lw=1.0, zorder=9))

    # =============================================================
    # MAIN PLOT: coherence vs complexity
    # =============================================================
    px0, px1 = 6.7, 13.7
    py0, py1 = 2.1, 7.7

    ax.add_patch(FancyBboxPatch(
        (px0, py0), px1 - px0, py1 - py0,
        boxstyle="round,pad=0.04,rounding_size=0.20",
        facecolor="white", edgecolor="#1f3b57",
        lw=1.6, alpha=0.94, zorder=3,
    ))

    ax_x0 = px0 + 0.45
    ax_x1 = px1 - 0.25
    ax_y0 = py0 + 0.55
    ax_y_top = py1 - 0.30

    # axes
    ax.plot([ax_x0, ax_x1], [ax_y0, ax_y0],
            color="#1f3b57", lw=1.8, alpha=0.85, zorder=4)
    ax.annotate("",
                xy=(ax_x1 + 0.08, ax_y0),
                xytext=(ax_x0, ax_y0),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1f3b57", lw=1.8),
                zorder=5)
    ax.plot([ax_x0, ax_x0], [ax_y0, ax_y_top],
            color="#1f3b57", lw=1.8, alpha=0.85, zorder=4)
    ax.annotate("",
                xy=(ax_x0, ax_y_top + 0.08),
                xytext=(ax_x0, ax_y0),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1f3b57", lw=1.8),
                zorder=5)

    # gridlines
    for frac in [0.25, 0.5, 0.75]:
        yh = ax_y0 + frac * (ax_y_top - ax_y0)
        ax.plot([ax_x0 + 0.02, ax_x1], [yh, yh],
                color="#1f3b57", lw=0.7, alpha=0.15,
                linestyle=(0, (4, 4)), zorder=4)

    # bright threshold vertical line at the ED-09.5 critical complexity
    thresh_frac = 0.58
    thresh_x = ax_x0 + thresh_frac * (ax_x1 - ax_x0)

    for gw, a in [(0.65, 0.08), (0.42, 0.16),
                  (0.26, 0.28), (0.14, 0.48)]:
        ax.add_patch(Rectangle(
            (thresh_x - gw / 2, ax_y0),
            gw, ax_y_top - ax_y0,
            facecolor="#ffc23a", edgecolor="none",
            alpha=a, zorder=4,
        ))
    ax.plot([thresh_x, thresh_x], [ax_y0, ax_y_top + 0.15],
            color="#ff9f1a", lw=4.2,
            solid_capstyle="round", zorder=6)
    ax.plot([thresh_x, thresh_x], [ax_y0, ax_y_top + 0.15],
            color="#fff1b0", lw=1.6,
            solid_capstyle="round", zorder=7)

    # threshold badge at top
    tbcx, tbcy = thresh_x, ax_y_top + 0.45
    for rr, a in [(0.38, 0.12), (0.28, 0.25)]:
        ax.add_patch(Circle((tbcx, tbcy), rr,
                            facecolor="#ffd24a",
                            edgecolor="none", alpha=a, zorder=9))
    ax.add_patch(Circle((tbcx, tbcy), 0.26,
                        facecolor="white", edgecolor="#c97a10",
                        lw=2.2, zorder=10))
    # simple "cliff" glyph: a step-down shape inside the badge
    step = [(tbcx - 0.16, tbcy + 0.12),
            (tbcx - 0.02, tbcy + 0.12),
            (tbcx - 0.02, tbcy - 0.10),
            (tbcx + 0.16, tbcy - 0.10)]
    ax.plot([p[0] for p in step], [p[1] for p in step],
            color="#c97a10", lw=2.4, solid_capstyle="round",
            zorder=11)

    # ---- CLASSICAL standard-decoherence curve (amber dashed) -----
    cs = np.linspace(ax_x0 + 0.25, ax_x1 - 0.25, 400)
    cn = (cs - cs[0]) / (cs[-1] - cs[0])
    # smooth exponential fade
    y_classical = ax_y_top - (ax_y_top - ax_y0) * (1 - np.exp(-2.5 * cn))
    for lw, col, a in [(10, "#ffd98a", 0.14),
                       (6, "#ffb347", 0.25)]:
        ax.plot(cs, y_classical, color=col, lw=lw, alpha=a,
                solid_capstyle="round", zorder=5)
    ax.plot(cs, y_classical, color="#c97a10", lw=2.8,
            linestyle=(0, (8, 4)), alpha=0.92,
            solid_capstyle="round", zorder=6)

    # ---- ED-09.5 sharp cliff (coral solid) ------------------------
    # high plateau before threshold, cliff at threshold, low plateau after
    y_ed = np.where(
        cs < thresh_x,
        ax_y_top - 0.30,          # high plateau (full coherence)
        ax_y0 + 0.20,             # low plateau (classical)
    )
    # smooth transition near threshold for readability (very narrow)
    sigma = 0.05 * (ax_x1 - ax_x0)
    y_ed_smooth = (ax_y0 + 0.20
                   + (ax_y_top - 0.30 - (ax_y0 + 0.20))
                   * (1 - 1 / (1 + np.exp(-(cs - thresh_x) / sigma))))
    for lw, col, a in [(12, "#ffd4b0", 0.14),
                       (8, "#ffae79", 0.26)]:
        ax.plot(cs, y_ed_smooth, color=col, lw=lw, alpha=a,
                solid_capstyle="round", zorder=6)
    ax.plot(cs, y_ed_smooth, color="#c94419", lw=3.6, alpha=0.98,
            solid_capstyle="round", zorder=7)

    # cliff emphasis: a vertical arrow on the cliff itself
    cliff_x = thresh_x
    cliff_y_top = ax_y_top - 0.30
    cliff_y_bot = ax_y0 + 0.30
    ax.annotate("",
                xy=(cliff_x + 0.10, cliff_y_bot),
                xytext=(cliff_x + 0.10, cliff_y_top),
                arrowprops=dict(arrowstyle="-|>",
                                color="#c94419", lw=2.8,
                                alpha=0.95),
                zorder=9)

    # legend swatches (no text in image)
    lx = ax_x0 + 0.15
    ax.plot([lx, lx + 0.55], [ax_y_top - 0.30, ax_y_top - 0.30],
            color="#c94419", lw=3.2,
            solid_capstyle="round", zorder=10)
    ax.add_patch(Circle((lx + 0.70, ax_y_top - 0.30), 0.10,
                        facecolor="#c94419", edgecolor="white",
                        lw=1.0, zorder=10))
    ax.plot([lx, lx + 0.55], [ax_y_top - 0.60, ax_y_top - 0.60],
            color="#c97a10", lw=3.0,
            linestyle=(0, (8, 4)), solid_capstyle="round",
            zorder=10)
    ax.add_patch(Circle((lx + 0.70, ax_y_top - 0.60), 0.10,
                        facecolor="#c97a10", edgecolor="white",
                        lw=1.0, zorder=10))

    # threshold tick on the x-axis
    ax.plot([thresh_x, thresh_x],
            [ax_y0 - 0.22, ax_y0 + 0.08],
            color="#ff9f1a", lw=3.0, zorder=7,
            solid_capstyle="round")
    for rr, a in [(0.34, 0.15), (0.22, 0.30), (0.15, 0.55)]:
        ax.add_patch(Circle((thresh_x, ax_y0 - 0.40), rr,
                            facecolor="#ffd24a",
                            edgecolor="none", alpha=a, zorder=8))
    ax.add_patch(Circle((thresh_x, ax_y0 - 0.40), 0.11,
                        facecolor="#fff1b0",
                        edgecolor="#d69a1a", lw=1.6, zorder=9))

    # =============================================================
    # Connector: source → plot start (interference coherence point)
    # =============================================================
    ax.annotate("",
                xy=(ax_x0 + 0.15, ax_y_top - 0.35),
                xytext=(ex1 - 0.10, (ey0 + ey1) / 2),
                arrowprops=dict(arrowstyle="-|>",
                                color="#c8aff0", lw=2.0, alpha=0.70,
                                connectionstyle="arc3,rad=-0.15",
                                linestyle=(0, (4, 3))),
                zorder=9)

    # =============================================================
    # Pending hourglass badge
    # =============================================================
    hb_x, hb_y = 13.4, 9.3
    for rr, a in [(0.55, 0.10), (0.42, 0.18)]:
        ax.add_patch(Circle((hb_x, hb_y), rr,
                            facecolor="#ffd24a",
                            edgecolor="none", alpha=a, zorder=9))
    ax.add_patch(Circle((hb_x, hb_y), 0.38,
                        facecolor="white", edgecolor="#c97a10",
                        lw=2.4, zorder=10))
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
                facecolor="#0a0e1a", edgecolor="none")
    plt.close(fig)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    build()
