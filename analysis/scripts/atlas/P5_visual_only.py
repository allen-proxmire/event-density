"""
P5 Participation Feedback — visual-only illustration.

Metaphor: a control loop. Four iconographic nodes on a circulating
feedback path, with a ν-response trace below showing the result.

Nodes (no text; each a small rounded tile with an icon):
  (1) Driver  — cyan sine-wave icon (the input F[ρ])
  (2) Summer  — circle with a "+" on the driver-entry side and a "−"
                on the feedback-entry side
  (3) Integrator — amber rising-curve icon (produces ν)
  (4) Damping tap — grey decaying-curve icon (multiplies by ζ before
                   feeding back into the summer)

A big translucent circular flow-arrow behind the four nodes makes the
"loop" legible from across a room.  Below the loop, a time-trace:
the cyan driver wave and, overlaid, the amber ν response — rising,
slightly overshooting, then settling — the damped-feedback signature.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch, Wedge,
)
from matplotlib.path import Path

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\P5_participation_feedback.png"


def build():
    fig, ax = plt.subplots(figsize=(11, 10), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 12, 0, 11], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 12, 1.8,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # =============================================================
    # TOP HALF — feedback loop
    # =============================================================
    cx, cy = 6.0, 7.4
    R = 2.5

    # ---- background circular flow-arrow ---------------------------
    # Soft translucent annulus with a big arrow suggesting clockwise flow.
    theta_full = np.linspace(0, 2 * np.pi, 300)
    # annulus via stacked rings
    for rr, lw, a in [(R + 0.55, 34, 0.05),
                      (R + 0.35, 22, 0.08),
                      (R + 0.15, 12, 0.12)]:
        ax.plot(cx + rr * np.cos(theta_full),
                cy + rr * np.sin(theta_full),
                color="#8aa4c0", lw=lw, alpha=a, zorder=1)
    # thick dashed flow ring
    ax.plot(cx + R * np.cos(theta_full),
            cy + R * np.sin(theta_full),
            color="#2a4c6e", lw=2.0, alpha=0.35,
            linestyle=(0, (6, 5)), zorder=2)
    # clockwise arrowhead on the ring, top-center
    arrow_t = np.pi * 0.55
    a0 = (cx + R * np.cos(arrow_t), cy + R * np.sin(arrow_t))
    a1 = (cx + R * np.cos(arrow_t - 0.10),
          cy + R * np.sin(arrow_t - 0.10))
    ax.annotate("", xy=a1, xytext=a0,
                arrowprops=dict(arrowstyle="-|>", color="#2a4c6e",
                                lw=2.4, alpha=0.8),
                zorder=3)

    # ---- node tile helper -----------------------------------------
    def tile(x, y, w, h, face, edge, glow):
        for g, a in [(0.32, 0.08), (0.20, 0.16), (0.10, 0.30)]:
            ax.add_patch(FancyBboxPatch(
                (x - g / 2, y - g / 2), w + g, h + g,
                boxstyle="round,pad=0.02,rounding_size=0.20",
                facecolor=glow, edgecolor="none",
                alpha=a, zorder=3,
            ))
        ax.add_patch(FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.02,rounding_size=0.20",
            facecolor=face, edgecolor=edge, lw=2.6, zorder=5,
        ))

    tw, th = 1.55, 1.10

    # Node positions at four compass points around the loop
    # Driver (left), Summer (top), Integrator (right), Damping (bottom)
    P_driver = (cx - R - 0.05, cy - th / 2)
    P_summer = (cx - tw / 2, cy + R - 0.55)
    P_integ = (cx + R - tw + 0.05, cy - th / 2)
    P_damp = (cx - tw / 2, cy - R - 0.55)

    # ---- (1) DRIVER tile: cyan sine wave icon ---------------------
    x0, y0 = P_driver
    tile(x0, y0, tw, th, "#eaf7fb", "#1aa6c7", "#9fe6f3")
    tx = np.linspace(x0 + 0.20, x0 + tw - 0.20, 120)
    ty = y0 + th / 2 + 0.28 * np.sin(
        (tx - x0) * 2 * np.pi / (tw - 0.40) * 1.4)
    ax.plot(tx, ty, color="#1aa6c7", lw=3.0,
            solid_capstyle="round", zorder=7)

    # ---- (2) SUMMER: circle with + (driver in) and − (feedback in) -
    sx, sy = P_summer[0] + tw / 2, P_summer[1] + th / 2
    # circular summer (bigger than the tile slightly)
    for rr, a in [(0.85, 0.09), (0.70, 0.17), (0.60, 0.30)]:
        ax.add_patch(Circle((sx, sy), rr,
                            facecolor="#ffd47a", edgecolor="none",
                            alpha=a, zorder=3))
    ax.add_patch(Circle((sx, sy), 0.52,
                        facecolor="white", edgecolor="#1f3b57",
                        lw=2.6, zorder=6))
    # "+" on the left quadrant
    ax.plot([sx - 0.35, sx - 0.15], [sy, sy],
            color="#1aa6c7", lw=3.0, zorder=7,
            solid_capstyle="round")
    ax.plot([sx - 0.25, sx - 0.25], [sy - 0.10, sy + 0.10],
            color="#1aa6c7", lw=3.0, zorder=7,
            solid_capstyle="round")
    # "−" on the bottom quadrant
    ax.plot([sx - 0.10, sx + 0.10], [sy - 0.32, sy - 0.32],
            color="#c23b3b", lw=3.4, zorder=7,
            solid_capstyle="round")
    # cross hairs inside the summer (very faint)
    ax.plot([sx - 0.52, sx + 0.52], [sy, sy],
            color="#1f3b57", lw=0.8, alpha=0.3, zorder=6)
    ax.plot([sx, sx], [sy - 0.52, sy + 0.52],
            color="#1f3b57", lw=0.8, alpha=0.3, zorder=6)

    # ---- (3) INTEGRATOR tile: rising curve icon -------------------
    x0, y0 = P_integ
    tile(x0, y0, tw, th, "#fff1d8", "#d69a1a", "#ffd98a")
    ix = np.linspace(x0 + 0.20, x0 + tw - 0.20, 120)
    # sigmoid-ish rise with mild overshoot
    t = (ix - ix[0]) / (ix[-1] - ix[0])
    iy = (y0 + 0.20 + 0.70 * (1 - np.exp(-4 * t))
          * (1 + 0.08 * np.sin(t * np.pi * 2.2)))
    ax.plot(ix, iy, color="#c97a10", lw=3.0,
            solid_capstyle="round", zorder=7)

    # ---- (4) DAMPING tile: decaying curve icon --------------------
    x0, y0 = P_damp
    tile(x0, y0, tw, th, "#f0f2f5", "#5b6b80", "#c9d4e0")
    dx = np.linspace(x0 + 0.20, x0 + tw - 0.20, 120)
    dt = (dx - dx[0]) / (dx[-1] - dx[0])
    dy = y0 + 0.25 + 0.60 * np.exp(-3.2 * dt)
    ax.plot(dx, dy, color="#5b6b80", lw=3.0,
            solid_capstyle="round", zorder=7)

    # ---- directional arrows connecting nodes ----------------------
    def arc_arrow(p_from, p_to, color, rad=0.22, lw=2.6, z=6):
        a = FancyArrowPatch(
            p_from, p_to,
            arrowstyle="-|>", mutation_scale=20,
            color=color, lw=lw,
            connectionstyle=f"arc3,rad={rad}",
            zorder=z,
        )
        ax.add_patch(a)

    # Driver -> Summer  (cyan)
    arc_arrow(
        (P_driver[0] + tw, P_driver[1] + th / 2 + 0.1),
        (sx - 0.55, sy - 0.05),
        color="#1aa6c7", rad=-0.28, lw=3.0,
    )
    # Summer -> Integrator  (navy)
    arc_arrow(
        (sx + 0.55, sy - 0.05),
        (P_integ[0], P_integ[1] + th / 2 + 0.1),
        color="#1f3b57", rad=-0.28, lw=3.0,
    )
    # Integrator -> Damping (amber, long loop downward)
    arc_arrow(
        (P_integ[0] + tw / 2, P_integ[1]),
        (P_damp[0] + tw, P_damp[1] + th / 2),
        color="#d69a1a", rad=-0.28, lw=3.0,
    )
    # Damping -> Summer (grey, feedback returning up to "−" port)
    arc_arrow(
        (P_damp[0] + tw / 2, P_damp[1] + th),
        (sx + 0.02, sy - 0.55),
        color="#5b6b80", rad=-0.28, lw=3.0,
    )

    # small color-coded endpoint dots on the summer indicating ports
    ax.add_patch(Circle((sx - 0.55, sy - 0.05), 0.10,
                        facecolor="#1aa6c7", edgecolor="white",
                        lw=1.6, zorder=8))
    ax.add_patch(Circle((sx + 0.02, sy - 0.55), 0.10,
                        facecolor="#5b6b80", edgecolor="white",
                        lw=1.6, zorder=8))

    # =============================================================
    # BOTTOM HALF — time trace (driver vs response)
    # =============================================================
    # Axes
    tx0, tx1 = 0.9, 11.1
    ty0 = 1.9
    ty_top = 4.2
    # axis baseline
    ax.plot([tx0, tx1], [ty0, ty0],
            color="#1f3b57", lw=1.8, alpha=0.7, zorder=4)
    # subtle horizontal zero-ref gridline
    for yh in [ty0 + 0.8, ty0 + 1.6]:
        ax.plot([tx0, tx1], [yh, yh],
                color="#1f3b57", lw=0.8, alpha=0.15,
                linestyle=(0, (4, 4)), zorder=3)

    # time grid
    tgrid = np.linspace(tx0 + 0.2, tx1 - 0.2, 600)
    tnorm = (tgrid - tgrid[0]) / (tgrid[-1] - tgrid[0])

    # driver: a clean sine wave (cyan) centered near ty0 + 1.5
    drv_y = ty0 + 1.4 + 0.55 * np.sin(tnorm * 2 * np.pi * 1.6)
    # drive envelope-fade near the left edge to feel "starting"
    drv_env = 1 - np.exp(-4 * tnorm)
    drv_y = (ty0 + 1.4) + (drv_y - (ty0 + 1.4)) * drv_env
    for lw, col, a in [(9, "#9fe6f3", 0.12),
                       (5, "#6fd2e9", 0.22),
                       (3.0, "#1aa6c7", 0.85)]:
        ax.plot(tgrid, drv_y, color=col, lw=lw, alpha=a,
                solid_capstyle="round", zorder=4)

    # response ν(t): a damped second-order response to the driver
    # (integrator + damping -> follows driver with phase lag + settling)
    # Compute numerically: dν/dτ = k*(drv - ν), with small inertia.
    n = len(tgrid)
    dt = (tgrid[-1] - tgrid[0]) / (n - 1)
    nu = np.zeros(n)
    v = np.zeros(n)
    k1, k2 = 6.0, 2.0   # response gain, damping
    for i in range(1, n):
        drive = drv_y[i] - (ty0 + 1.4)
        a_ = k1 * (drive - nu[i - 1]) - k2 * v[i - 1]
        v[i] = v[i - 1] + a_ * dt
        nu[i] = nu[i - 1] + v[i] * dt
    resp_y = (ty0 + 1.4) + nu * 0.95  # slight attenuation

    for lw, col, a in [(10, "#ffd98a", 0.12),
                       (6, "#ffb347", 0.22),
                       (3.4, "#c97a10", 0.95)]:
        ax.plot(tgrid, resp_y, color=col, lw=lw, alpha=a,
                solid_capstyle="round", zorder=5)

    # shaded "delay" gap between driver and response to hint lag
    # (only where they differ noticeably)
    ax.fill_between(tgrid, drv_y, resp_y,
                    where=(drv_y > resp_y),
                    color="#ffb347", alpha=0.15, zorder=3)
    ax.fill_between(tgrid, drv_y, resp_y,
                    where=(drv_y < resp_y),
                    color="#1aa6c7", alpha=0.10, zorder=3)

    # marker legend dots on the left (icon-only)
    ax.add_patch(Circle((tx0 + 0.18, ty0 + 2.05), 0.14,
                        facecolor="#1aa6c7",
                        edgecolor="#0b4a68", lw=1.3, zorder=6))
    ax.add_patch(Circle((tx0 + 0.18, ty0 + 1.45), 0.14,
                        facecolor="#c97a10",
                        edgecolor="#7a4a0a", lw=1.3, zorder=6))

    # downward bracket from loop into time-trace to suggest "output"
    ax.annotate("",
                xy=((tx0 + tx1) / 2, ty_top - 0.2),
                xytext=(cx, cy - R - 1.4),
                arrowprops=dict(arrowstyle="-|>", color="#1f3b57",
                                lw=1.6, alpha=0.45,
                                linestyle=(0, (4, 3))),
                zorder=3)

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
