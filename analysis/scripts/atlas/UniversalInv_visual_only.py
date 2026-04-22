"""
Universal Invariants — visual-only illustration.

Metaphor: different beginnings → one universal outcome.
  E_ground  and  τ_rel  are regime- and IC-independent.

Composition:
  MAIN  : a state-space portrait with a central golden ATTRACTOR orb.
          Eight trajectories, each a different color and starting from
          a different direction / distance, all curve inward and end
          at the same attractor — asserting "IC-independent endpoint."
  INSET : a bottom strip showing |state − attractor| vs time for each
          trajectory, with all curves collapsing onto a single
          universal exponential decay (the universal τ_rel).  Every
          trajectory reaches a common horizontal baseline (E_ground).
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\UniversalInv.png"


# palette for trajectories — 8 distinct colors
TRAJ_COLORS = [
    ("#4fa3d8", "#9bd3ea"),   # blue
    ("#e0584f", "#f1a1a1"),   # red
    ("#2fb27a", "#b6e7cf"),   # green
    ("#8a5ac9", "#c8aff0"),   # violet
    ("#ff9f1a", "#ffd98a"),   # amber
    ("#1aa6c7", "#9fe6f3"),   # cyan
    ("#d94f7b", "#f5c1d2"),   # pink
    ("#5b6b80", "#c9d4e0"),   # steel
]


def invariant_orb(ax, x, y, r=0.55, zorder=10):
    for rr, a in [(r * 2.2, 0.05),
                  (r * 1.7, 0.10),
                  (r * 1.35, 0.20),
                  (r * 1.12, 0.38)]:
        ax.add_patch(Circle((x, y), rr,
                            facecolor="#ffd24a", edgecolor="none",
                            alpha=a, zorder=zorder - 1))
    for rr, col in [(r * 0.95, "#fff1b0"),
                    (r * 0.80, "#ffd24a"),
                    (r * 0.62, "#ffb347"),
                    (r * 0.44, "#ff9f1a"),
                    (r * 0.28, "#e07b00")]:
        ax.add_patch(Circle((x, y), rr,
                            facecolor=col, edgecolor="none",
                            zorder=zorder))
    ax.add_patch(Circle((x - r * 0.28, y + r * 0.30), r * 0.25,
                        facecolor="white", alpha=0.78,
                        zorder=zorder + 1))
    ax.add_patch(Circle((x, y), r,
                        facecolor="none",
                        edgecolor="#c97a10", lw=2.0,
                        zorder=zorder + 2))


def build():
    fig, ax = plt.subplots(figsize=(12, 10), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 13, 0, 11], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 13, 1.7,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # =============================================================
    # Main panel — state-space portrait
    # =============================================================
    panel_x0, panel_x1 = 0.7, 12.3
    panel_y0, panel_y1 = 4.0, 10.5

    ax.add_patch(FancyBboxPatch(
        (panel_x0, panel_y0), panel_x1 - panel_x0, panel_y1 - panel_y0,
        boxstyle="round,pad=0.04,rounding_size=0.30",
        facecolor="white", edgecolor="#1f3b57",
        lw=1.6, alpha=0.93, zorder=1,
    ))

    # Attractor center (the universal invariant point)
    acx, acy = (panel_x0 + panel_x1) / 2, (panel_y0 + panel_y1) / 2
    # radial starburst
    for ang_deg in np.linspace(0, 360, 28, endpoint=False):
        th = np.deg2rad(ang_deg)
        r0 = 0.80
        r1 = 1.55
        ax.plot([acx + r0 * np.cos(th), acx + r1 * np.cos(th)],
                [acy + r0 * np.sin(th), acy + r1 * np.sin(th)],
                color="#ffd98a", lw=1.6, alpha=0.20,
                solid_capstyle="round", zorder=2)
    # outer halo
    for rr, a in [(1.85, 0.05), (1.35, 0.10),
                  (1.00, 0.18), (0.78, 0.30)]:
        ax.add_patch(Circle((acx, acy), rr,
                            facecolor="#ffd24a", edgecolor="none",
                            alpha=a, zorder=3))

    # =============================================================
    # Trajectories — 8 curves from different ICs into the attractor
    # =============================================================
    rng = np.random.default_rng(11)

    # pick starting points around the panel at various angles/distances
    start_angles = np.deg2rad([25, 75, 115, 150, 200, 240, 290, 335])
    start_radii = [3.2, 2.9, 2.6, 3.1, 2.7, 3.0, 2.8, 3.3]

    # for the inset: track each trajectory's radial distance as a function
    # of a normalized "time" parameter.  The universal invariant claim is
    # that each of them decays with the SAME rate toward 0 regardless of
    # initial condition.
    inset_traces = []

    for k, ((core, halo), ang, r_start) in enumerate(
        zip(TRAJ_COLORS, start_angles, start_radii)
    ):
        # start point
        sx = acx + r_start * np.cos(ang)
        sy = acy + r_start * np.sin(ang)

        # parametric curve: spiral-in with damped decay, slight rotation
        n = 240
        t_param = np.linspace(0, 1, n)
        # radial decay (common universal form: r(t) = r0 * exp(-k*t))
        k_decay = 3.5
        r_t = r_start * np.exp(-k_decay * t_param)
        # rotation differs per trajectory to spread them visually
        rot_total = (k % 4 - 1.5) * 1.2        # ± various angles
        th_t = ang + rot_total * t_param
        xs = acx + r_t * np.cos(th_t)
        ys = acy + r_t * np.sin(th_t)

        # glow underlay
        for lw, col, a in [(9, halo, 0.14),
                           (5.5, halo, 0.28)]:
            ax.plot(xs, ys, color=col, lw=lw, alpha=a,
                    solid_capstyle="round", zorder=5)
        # crisp curve
        ax.plot(xs, ys, color=core, lw=2.6, alpha=0.93,
                solid_capstyle="round", zorder=6)
        # start marker
        for rr, a in [(0.30, 0.16), (0.22, 0.30)]:
            ax.add_patch(Circle((sx, sy), rr, facecolor=halo,
                                edgecolor="none", alpha=a, zorder=7))
        ax.add_patch(Circle((sx, sy), 0.16,
                            facecolor=core, edgecolor="white",
                            lw=1.6, zorder=9))

        # little arrow near the end pointing inward
        tip_i = int(0.90 * n)
        ax.annotate("",
                    xy=(xs[tip_i + 4], ys[tip_i + 4]),
                    xytext=(xs[tip_i], ys[tip_i]),
                    arrowprops=dict(arrowstyle="-|>",
                                    color=core, lw=2.0, alpha=0.95),
                    zorder=8)

        # store trace for inset: universal normalized decay
        inset_traces.append((core, halo, r_t))

    # draw the attractor orb ON TOP of trajectories
    invariant_orb(ax, acx, acy, r=0.78, zorder=12)

    # =============================================================
    # Inset — universal decay panel
    # =============================================================
    in_x0, in_x1 = 1.0, 12.0
    in_y0 = 1.9       # baseline (E_ground)
    in_y_top = 3.55   # top of inset plot

    # panel bg
    ax.add_patch(FancyBboxPatch(
        (in_x0 - 0.25, in_y0 - 0.30),
        in_x1 - in_x0 + 0.5,
        in_y_top - in_y0 + 0.55,
        boxstyle="round,pad=0.04,rounding_size=0.20",
        facecolor="white", edgecolor="#1f3b57",
        lw=1.5, alpha=0.90, zorder=4,
    ))

    # universal E_ground baseline (glowing amber)
    for glow_h, a in [(0.55, 0.06), (0.36, 0.12),
                      (0.22, 0.22), (0.14, 0.38), (0.08, 0.65)]:
        ax.add_patch(Rectangle(
            (in_x0, in_y0 - glow_h / 2),
            in_x1 - in_x0, glow_h,
            facecolor="#ffc23a", edgecolor="none",
            alpha=a, zorder=5,
        ))
    ax.plot([in_x0 + 0.05, in_x1 - 0.05], [in_y0, in_y0],
            color="#ff9f1a", lw=4.0, zorder=7, solid_capstyle="round")
    ax.plot([in_x0 + 0.05, in_x1 - 0.05], [in_y0, in_y0],
            color="#fff1b0", lw=1.6, zorder=8, solid_capstyle="round")

    # y-axis
    ax.plot([in_x0 + 0.05, in_x0 + 0.05], [in_y0, in_y_top],
            color="#1f3b57", lw=1.5, alpha=0.7, zorder=5)
    # t-axis
    ax.plot([in_x0 + 0.05, in_x1 - 0.05], [in_y0 - 0.45, in_y0 - 0.45],
            color="#1f3b57", lw=1.5, alpha=0.70, zorder=5)
    ax.annotate("",
                xy=(in_x1 - 0.05, in_y0 - 0.45),
                xytext=(in_x0 + 0.05, in_y0 - 0.45),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1f3b57", lw=1.5),
                zorder=5)

    # Plot each trajectory's radial distance vs time — all SAME curve shape
    # (universal τ_rel) but normalized to their own initial condition so
    # they visually overlap except near t=0 where they fan out.
    ts_plot = np.linspace(in_x0 + 0.25, in_x1 - 0.30, 400)
    tn = (ts_plot - ts_plot[0]) / (ts_plot[-1] - ts_plot[0])

    y_range = in_y_top - in_y0 - 0.10

    # reuse the trace r_t data — sample each at normalized time
    n_t = 240
    t_sample_idx = np.linspace(0, n_t - 1, len(tn)).astype(int)

    for (core, halo, r_t) in inset_traces:
        # normalize r_t to the y axis of the inset
        r_normalized = r_t / max(r.max() for _, _, r in inset_traces)
        y_vals = in_y0 + r_normalized[t_sample_idx] * y_range

        # glow underlay
        for lw, col, a in [(7, halo, 0.14),
                           (4.2, halo, 0.28)]:
            ax.plot(ts_plot, y_vals, color=col, lw=lw, alpha=a,
                    solid_capstyle="round", zorder=6)
        # crisp line
        ax.plot(ts_plot, y_vals, color=core, lw=2.0,
                alpha=0.92, solid_capstyle="round", zorder=7)

    # τ_rel marker — a vertical dashed line at the universal time constant
    tau_x = ts_plot[0] + 0.28 * (ts_plot[-1] - ts_plot[0])
    ax.plot([tau_x, tau_x], [in_y0 + 0.04, in_y_top - 0.05],
            color="#c97a10", lw=1.6, alpha=0.55,
            linestyle=(0, (4, 3)), zorder=7)
    # little tag badge at the top
    ax.add_patch(Circle((tau_x, in_y_top + 0.12), 0.17,
                        facecolor="#fff1b0",
                        edgecolor="#c97a10", lw=1.6, zorder=9))
    # clock icon inside the badge
    ax.add_patch(Circle((tau_x, in_y_top + 0.12), 0.04,
                        facecolor="#c97a10", zorder=10))
    ax.plot([tau_x, tau_x + 0.10], [in_y_top + 0.12, in_y_top + 0.20],
            color="#c97a10", lw=1.6,
            solid_capstyle="round", zorder=10)

    # small "all converge" indicator near the right end
    end_x = ts_plot[-1] - 0.15
    for rr, a in [(0.30, 0.16), (0.22, 0.30)]:
        ax.add_patch(Circle((end_x, in_y0 + 0.08), rr,
                            facecolor="#ffd24a", edgecolor="none",
                            alpha=a, zorder=7))
    ax.add_patch(Circle((end_x, in_y0 + 0.08), 0.14,
                        facecolor="#fff1b0",
                        edgecolor="#d69a1a", lw=1.6, zorder=9))

    # =============================================================
    # Connector: central attractor -> end point of inset curves
    # =============================================================
    ax.annotate("",
                xy=(end_x, in_y0 + 0.28),
                xytext=(acx + 0.5, panel_y0 + 0.3),
                arrowprops=dict(arrowstyle="-|>",
                                color="#c97a10", lw=2.0, alpha=0.60,
                                connectionstyle="arc3,rad=0.20",
                                linestyle=(0, (4, 3))),
                zorder=6)

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
