"""
P6 Damping Discriminant — visual-only illustration.

Metaphor: a sharp bifurcation at D_crit between two regimes.
Value corrected 2026-04-22: D_crit ~ 0.896 at canon-default zeta=1/4,
not 0.5 (retired heuristic). See theory/D_crit_Resolution_Memo.md.
The diagram remains qualitatively correct; only the threshold value
is updated. The image geometry is centered for aesthetic symmetry and
is not a quantitative D-axis.

  - Left half  (D < D_crit) : UNDERDAMPED — a cyan damped sinusoid,
                              small mass-spring-damper icon with a light
                              dashpot, oscillating motion indicator.
  - Right half (D > D_crit) : OVERDAMPED  — an amber monotone decay,
                           same rig but with a heavy dashpot, no
                           oscillation indicator.
  - Between them: a bright glowing vertical threshold line with a
                  radial burst behind it, marked D_crit on the
                  axis below.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch, Polygon,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\P6_damping_discriminant.png"


def spring_path(p0, p1, coils=7, amplitude=0.14):
    p0 = np.asarray(p0, float)
    p1 = np.asarray(p1, float)
    v = p1 - p0
    L = np.linalg.norm(v)
    if L == 0:
        return np.array([p0[0]]), np.array([p0[1]])
    uhat = v / L
    nhat = np.array([-uhat[1], uhat[0]])
    n = 300
    t = np.linspace(0, 1, n)
    lead, tail = 0.14, 0.86
    coil_phase = np.zeros_like(t)
    m = (t >= lead) & (t <= tail)
    tt = (t[m] - lead) / (tail - lead)
    coil_phase[m] = np.sin(2 * np.pi * coils * tt)
    amp = np.where(m, amplitude, 0.0)
    pts = (p0[:, None]
           + uhat[:, None] * (t * L)
           + nhat[:, None] * (amp * coil_phase))
    return pts[0], pts[1]


def dashpot(ax, x_anchor, x_piston, y, width=0.22, heavy=False):
    """Draw a dashpot between x_anchor and x_piston at height y."""
    # piston rod from anchor to cylinder
    cyl_len = 0.48
    cyl_x1 = x_piston + (-0.28 if x_piston < x_anchor else 0.28)
    # cylinder body
    cyl_x0 = cyl_x1 - cyl_len if x_piston < x_anchor else cyl_x1 - cyl_len
    cyl_x0, cyl_x1 = sorted([cyl_x0, cyl_x1])
    edge_col = "#2f4d6b"
    fill_col = "#e9eef3" if not heavy else "#c3d3e1"
    ax.add_patch(FancyBboxPatch(
        (cyl_x0, y - width / 2), cyl_x1 - cyl_x0, width,
        boxstyle="round,pad=0.01,rounding_size=0.05",
        facecolor=fill_col, edgecolor=edge_col, lw=2.0, zorder=7,
    ))
    # oil level inside the cylinder (more oil if heavy)
    oil_w = (cyl_x1 - cyl_x0) * (0.85 if heavy else 0.45)
    ax.add_patch(Rectangle(
        (cyl_x0 + 0.02, y - width / 2 + 0.02),
        oil_w, width - 0.04,
        facecolor="#5b6b80" if heavy else "#8aa4c0",
        edgecolor="none", alpha=0.85, zorder=8,
    ))
    # piston plate
    if x_piston < x_anchor:
        plate_x = cyl_x1 - 0.05
    else:
        plate_x = cyl_x0 + 0.05
    ax.plot([plate_x, plate_x], [y - width / 2 + 0.02, y + width / 2 - 0.02],
            color=edge_col, lw=2.4, zorder=9)
    # rod from anchor to cylinder
    rod_start = (x_anchor, y)
    rod_end = (cyl_x0 if x_piston > x_anchor else cyl_x1, y)
    ax.plot([rod_start[0], rod_end[0]], [rod_start[1], rod_end[1]],
            color=edge_col, lw=2.2, zorder=7)
    # extension rod from piston plate to the mass
    ax.plot([plate_x, x_piston], [y, y],
            color=edge_col, lw=2.2, zorder=7)


def build():
    fig, ax = plt.subplots(figsize=(12, 9), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 13, 0, 10], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 13, 1.5,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # ---- panel backgrounds (soft washes) --------------------------
    L_wash = Rectangle((0.4, 1.9), 5.9, 7.4,
                       facecolor="#e6f4fa", edgecolor="none",
                       alpha=0.55, zorder=1)
    R_wash = Rectangle((6.7, 1.9), 5.9, 7.4,
                       facecolor="#fff2dc", edgecolor="none",
                       alpha=0.55, zorder=1)
    ax.add_patch(L_wash)
    ax.add_patch(R_wash)

    # ---- bright threshold line at D_crit (approx 0.896 at zeta=1/4) ----
    # The image x-coordinate Dc_x is a visual center, not a quantitative D value.
    Dc_x = 6.5
    thresh_y0, thresh_y1 = 1.6, 9.3

    # radial burst behind the line
    for rr, a in [(1.6, 0.05), (1.1, 0.10), (0.7, 0.18),
                  (0.42, 0.34), (0.24, 0.55)]:
        ax.add_patch(Circle(((thresh_y0 + thresh_y1) / 2 * 0 + Dc_x,
                             (thresh_y0 + thresh_y1) / 2), rr,
                            facecolor="#ffd24a", edgecolor="none",
                            alpha=a, zorder=2))
    # soft halo strip
    for gw, a in [(0.85, 0.10), (0.55, 0.16),
                  (0.35, 0.26), (0.22, 0.45)]:
        ax.add_patch(Rectangle(
            (Dc_x - gw / 2, thresh_y0), gw, thresh_y1 - thresh_y0,
            facecolor="#ffc23a", edgecolor="none", alpha=a, zorder=2,
        ))
    # main line
    ax.plot([Dc_x, Dc_x], [thresh_y0, thresh_y1],
            color="#ff9f1a", lw=5.5, solid_capstyle="round",
            zorder=4)
    ax.plot([Dc_x, Dc_x], [thresh_y0, thresh_y1],
            color="#fff1b0", lw=2.2, solid_capstyle="round",
            zorder=5)

    # ---- time-traces in upper halves of each panel ----------------
    def draw_trace(x0, x1, y_mid, fn, color_core, color_halo):
        ts = np.linspace(x0 + 0.15, x1 - 0.15, 600)
        ys = y_mid + fn((ts - x0) / (x1 - x0))
        for lw, col, a in [(11, color_halo, 0.10),
                           (6.5, color_halo, 0.20),
                           (3.4, color_core, 0.95)]:
            ax.plot(ts, ys, color=col, lw=lw, alpha=a,
                    solid_capstyle="round", zorder=6)
        return ts, ys

    # LEFT underdamped: damped sinusoid, slightly long-lived
    def fn_under(u):
        return 1.3 * np.exp(-1.8 * u) * np.cos(u * np.pi * 5.8)
    # RIGHT overdamped: smooth exponential-like decay
    def fn_over(u):
        return 1.3 * np.exp(-3.5 * u) * (1 + 0.2 * u)

    # trace baselines (within each panel)
    L_trace_y = 6.75
    R_trace_y = 6.75

    # zero-reference lines
    ax.plot([0.6, 6.35], [L_trace_y, L_trace_y],
            color="#1f3b57", lw=0.9, alpha=0.25,
            linestyle=(0, (4, 3)), zorder=5)
    ax.plot([6.65, 12.6], [R_trace_y, R_trace_y],
            color="#1f3b57", lw=0.9, alpha=0.25,
            linestyle=(0, (4, 3)), zorder=5)

    # actual traces
    draw_trace(0.6, 6.35, L_trace_y, fn_under,
               color_core="#1aa6c7", color_halo="#9fe6f3")
    draw_trace(6.65, 12.4, R_trace_y, fn_over,
               color_core="#c97a10", color_halo="#ffd98a")

    # ---- mass-spring-damper rigs in lower halves ------------------
    # Shared anchor wall for each side
    def draw_rig(anchor_x, mass_x, y_rig, heavy=False,
                 mass_color="#4fa3d8", mass_edge="#0b4a68",
                 spring_color="#1aa6c7"):
        # anchor wall (hatched vertical)
        wall_w = 0.18
        wall_h = 1.6
        wall_x = anchor_x - wall_w
        ax.add_patch(Rectangle((wall_x, y_rig - wall_h / 2), wall_w, wall_h,
                               facecolor="#2f4d6b", edgecolor="#142536",
                               lw=1.8, zorder=6))
        # hatch lines on the wall
        for hy in np.linspace(y_rig - wall_h / 2 + 0.08,
                              y_rig + wall_h / 2 - 0.08, 8):
            ax.plot([wall_x, wall_x - 0.18], [hy, hy - 0.18],
                    color="#6b8aa8", lw=1.2, alpha=0.85, zorder=7)

        # ground line under the rig
        ax.plot([wall_x - 0.25, mass_x + 0.95],
                [y_rig - 0.95, y_rig - 0.95],
                color="#1f3b57", lw=2.0, zorder=5)
        # small hatching below ground
        for gx in np.linspace(wall_x - 0.18, mass_x + 0.85, 12):
            ax.plot([gx, gx - 0.18],
                    [y_rig - 0.95, y_rig - 1.12],
                    color="#6b8aa8", lw=1.0, alpha=0.75, zorder=4)

        # spring on top path (anchor to mass), dashpot on bottom path
        spring_y = y_rig + 0.28
        dash_y = y_rig - 0.22

        sp0 = (anchor_x, spring_y)
        sp1 = (mass_x - 0.30, spring_y)
        xs, ys = spring_path(sp0, sp1, coils=7, amplitude=0.14)
        for lw, col, a in [(7.5, "#9fe6f3" if spring_color == "#1aa6c7"
                            else "#ffd98a",
                            0.25),
                           (4.5, spring_color, 0.55)]:
            ax.plot(xs, ys, color=col, lw=lw, alpha=a,
                    solid_capstyle="round", zorder=7)
        ax.plot(xs, ys, color="#1f3b57", lw=1.6, alpha=0.85, zorder=8)

        # anchor knobs at ends of spring
        ax.add_patch(Circle(sp0, 0.08, facecolor="#1f3b57",
                            edgecolor="none", zorder=9))
        ax.add_patch(Circle(sp1, 0.08, facecolor="#1f3b57",
                            edgecolor="none", zorder=9))
        # connect spring end to mass
        ax.plot([sp1[0], mass_x], [spring_y, spring_y],
                color="#1f3b57", lw=2.0, zorder=7)

        # dashpot
        dashpot(ax, anchor_x, mass_x - 0.30, dash_y,
                width=0.26, heavy=heavy)
        ax.plot([mass_x - 0.30, mass_x], [dash_y, dash_y],
                color="#2f4d6b", lw=2.0, zorder=7)

        # mass
        mw, mh = 0.95, 0.95
        ax.add_patch(FancyBboxPatch(
            (mass_x, y_rig - mh / 2), mw, mh,
            boxstyle="round,pad=0.01,rounding_size=0.12",
            facecolor=mass_color, edgecolor=mass_edge,
            lw=2.4, zorder=9,
        ))
        # mass highlight
        ax.add_patch(Rectangle(
            (mass_x + 0.10, y_rig + 0.18), 0.18, 0.40,
            facecolor="white", alpha=0.35, zorder=10,
        ))

        return mass_x + mw  # right edge of mass

    # LEFT rig: light dashpot -> oscillates
    rig_y_L = 3.8
    anchor_L = 0.95
    mass_L_x = 2.85
    right_edge_L = draw_rig(anchor_L, mass_L_x, rig_y_L, heavy=False,
                            mass_color="#4fa3d8", mass_edge="#0b4a68",
                            spring_color="#1aa6c7")
    # oscillation arrows on the mass (left/right)
    ax.annotate("", xy=(right_edge_L + 0.95, rig_y_L),
                xytext=(right_edge_L + 0.25, rig_y_L),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1aa6c7", lw=2.6),
                zorder=11)
    ax.annotate("", xy=(mass_L_x - 0.95, rig_y_L),
                xytext=(mass_L_x - 0.25, rig_y_L),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1aa6c7", lw=2.6),
                zorder=11)
    # motion-blur ghost of the mass
    for dx, a in [(-0.55, 0.20), (0.55, 0.20)]:
        ax.add_patch(FancyBboxPatch(
            (mass_L_x + dx, rig_y_L - 0.48), 0.95, 0.95,
            boxstyle="round,pad=0.01,rounding_size=0.12",
            facecolor="#4fa3d8", edgecolor="none",
            alpha=a, zorder=8,
        ))

    # RIGHT rig: heavy dashpot -> overdamped
    rig_y_R = 3.8
    anchor_R = 7.15
    mass_R_x = 9.15
    right_edge_R = draw_rig(anchor_R, mass_R_x, rig_y_R, heavy=True,
                            mass_color="#e0a060", mass_edge="#7a4a0a",
                            spring_color="#d69a1a")
    # single slow arrow toward equilibrium
    ax.annotate("", xy=(mass_R_x - 0.70, rig_y_R),
                xytext=(mass_R_x - 0.15, rig_y_R),
                arrowprops=dict(arrowstyle="-|>",
                                color="#c97a10", lw=2.6),
                zorder=11)
    # small "no-oscillation" indicator (a subtle 'x' next to the rig)
    nx, ny = right_edge_R + 1.1, rig_y_R + 0.55
    ax.add_patch(Circle((nx, ny), 0.22,
                        facecolor="white", edgecolor="#c23b3b",
                        lw=2.0, zorder=12))
    # tiny wavy line inside the circle, crossed out
    wx = np.linspace(nx - 0.14, nx + 0.14, 40)
    wy = ny + 0.05 * np.sin((wx - nx) * 90)
    ax.plot(wx, wy, color="#c23b3b", lw=1.6, alpha=0.9, zorder=13)
    ax.plot([nx - 0.17, nx + 0.17], [ny + 0.17, ny - 0.17],
            color="#c23b3b", lw=2.2, zorder=14,
            solid_capstyle="round")

    # ---- bottom D axis with D_crit tick ---------------------------
    ax_y = 1.35
    ax.plot([0.6, 12.4], [ax_y, ax_y],
            color="#1f3b57", lw=2.0, zorder=5)
    # 0 tick
    ax.plot([0.6, 0.6], [ax_y - 0.16, ax_y + 0.16],
            color="#1f3b57", lw=2.4, zorder=6)
    # 1 tick
    ax.plot([12.4, 12.4], [ax_y - 0.16, ax_y + 0.16],
            color="#1f3b57", lw=2.4, zorder=6)
    # D_crit tick (bright)
    ax.plot([Dc_x, Dc_x], [ax_y - 0.30, ax_y + 0.30],
            color="#ff9f1a", lw=3.2, zorder=7,
            solid_capstyle="round")
    for rr, a in [(0.38, 0.12), (0.26, 0.25), (0.17, 0.55)]:
        ax.add_patch(Circle((Dc_x, ax_y), rr,
                            facecolor="#ffd24a", edgecolor="none",
                            alpha=a, zorder=6))
    ax.add_patch(Circle((Dc_x, ax_y), 0.14,
                        facecolor="#fff1b0", edgecolor="#d69a1a",
                        lw=1.8, zorder=8))

    # arrow along axis
    ax.annotate("", xy=(12.2, ax_y),
                xytext=(0.8, ax_y),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1f3b57", lw=1.8),
                zorder=5)

    # ---- framing ---------------------------------------------------
    ax.set_xlim(0, 13)
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
