"""
Dissipative Structure constraint — visual-only illustration.

Metaphor: three time snapshots of the same system. A glowing amber
hot-spot loses energy over time — brighter and tighter at t₁,
dimmer and broader at t₂, barely present at t₃. Below, the E(t)
curve decays monotonically. A red one-way badge reinforces "no
going back — dissipation is irreversible."
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, Ellipse, FancyArrowPatch,
)
from matplotlib.colors import LinearSegmentedColormap

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\Dissipative.png"


def build():
    fig, ax = plt.subplots(figsize=(13, 10), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad_bg = np.linspace(0, 1, 500).reshape(-1, 1)
    grad_bg = np.tile(grad_bg, (1, 500))
    ax.imshow(grad_bg, extent=[0, 13, 0, 11], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 13, 1.5,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # =============================================================
    # Three snapshot panels (top row)
    # =============================================================
    snap_y0 = 6.0
    snap_y1 = 9.6
    snap_w = 2.8
    gap = 0.80
    total_w = 3 * snap_w + 2 * gap
    start_x = (13 - total_w) / 2

    # each snapshot has a different energy level + spread
    snapshots = [
        # (amplitude, sigma, outline_color, edge_glow)
        (1.00, 0.50, "#ff9f1a", "#ffd98a"),   # t1: bright, tight
        (0.55, 0.80, "#d69a1a", "#ffb347"),   # t2: dimmer, broader
        (0.18, 1.20, "#c9a66b", "#f4e6c9"),   # t3: faint, diffuse
    ]

    panel_centers = []
    bar_frac_stored = []

    for i, (amp, sig, edge_col, glow_col) in enumerate(snapshots):
        x0 = start_x + i * (snap_w + gap)
        cx = x0 + snap_w / 2
        cy = (snap_y0 + snap_y1) / 2
        panel_centers.append((cx, cy))

        # shadow + halo
        ax.add_patch(FancyBboxPatch(
            (x0 + 0.08, snap_y0 - 0.12), snap_w, snap_y1 - snap_y0,
            boxstyle="round,pad=0.02,rounding_size=0.22",
            facecolor="#00000018", edgecolor="none", zorder=2,
        ))
        # panel fill (light cool background)
        ax.add_patch(FancyBboxPatch(
            (x0, snap_y0), snap_w, snap_y1 - snap_y0,
            boxstyle="round,pad=0.02,rounding_size=0.22",
            facecolor="#f4f7fb", edgecolor="#1f3b57",
            lw=2.4, zorder=3,
        ))

        # render the glowing hot-spot as a 2D gaussian
        N = 200
        xs = np.linspace(x0 + 0.10, x0 + snap_w - 0.10, N)
        ys = np.linspace(snap_y0 + 0.10, snap_y1 - 0.10, N)
        X, Y = np.meshgrid(xs, ys)
        Z = amp * np.exp(-((X - cx) ** 2 + (Y - cy) ** 2)
                         / (2 * sig ** 2))

        # warm dissipation colormap (bright at center, fades to panel bg)
        cmap_dis = LinearSegmentedColormap.from_list(
            "diss_warm",
            [(0.00, (1.0, 1.0, 1.0, 0.0)),
             (0.10, (1.00, 0.95, 0.70, 0.25)),
             (0.30, (1.00, 0.80, 0.40, 0.60)),
             (0.55, (1.00, 0.65, 0.28, 0.90)),
             (0.80, (0.90, 0.42, 0.15, 1.00)),
             (1.00, (0.70, 0.25, 0.08, 1.00))],
        )
        ax.imshow(Z, extent=[x0 + 0.10, x0 + snap_w - 0.10,
                              snap_y0 + 0.10, snap_y1 - 0.10],
                  origin="lower", cmap=cmap_dis,
                  alpha=0.90, interpolation="bilinear",
                  zorder=4,
                  vmin=0, vmax=1.0)

        # a few soft iso-level rings to show structure
        for lvl, lw_, a in [(amp * 0.25, 1.4, 0.65),
                            (amp * 0.55, 1.2, 0.55),
                            (amp * 0.80, 1.0, 0.40)]:
            if lvl > 0.08:
                ax.contour(X, Y, Z, levels=[lvl],
                           colors=edge_col, linewidths=lw_,
                           alpha=a, zorder=5)

        # energy bar on the right side of each panel
        bar_x = x0 + snap_w - 0.35
        bar_y0_ = snap_y0 + 0.35
        bar_h = snap_y1 - snap_y0 - 0.70
        ax.add_patch(FancyBboxPatch(
            (bar_x, bar_y0_), 0.25, bar_h,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            facecolor="#eef0f3", edgecolor="#5b6b80",
            lw=1.2, zorder=7,
        ))
        fill_h = amp * bar_h
        ax.add_patch(FancyBboxPatch(
            (bar_x, bar_y0_), 0.25, fill_h,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            facecolor=edge_col, edgecolor="#7a4a0a",
            lw=1.0, zorder=8,
        ))
        # subtle glow around the fill
        for gg, aa in [(0.14, 0.14), (0.08, 0.28)]:
            ax.add_patch(FancyBboxPatch(
                (bar_x - gg / 2, bar_y0_ - gg / 2),
                0.25 + gg, fill_h + gg,
                boxstyle="round,pad=0.02,rounding_size=0.06",
                facecolor=glow_col, edgecolor="none",
                alpha=aa, zorder=7,
            ))
        bar_frac_stored.append(amp)

    # ---- arrows between snapshots (time progression) -------------
    for i in range(2):
        x_left = start_x + (i + 1) * snap_w + i * gap
        x_right = x_left + gap
        y_mid = (snap_y0 + snap_y1) / 2
        arrow = FancyArrowPatch(
            (x_left + 0.10, y_mid),
            (x_right - 0.10, y_mid),
            arrowstyle="-|>", mutation_scale=24,
            color="#1f3b57", lw=3.0, zorder=6,
        )
        ax.add_patch(arrow)
        for lw_h, aa in [(9, 0.12), (5, 0.22)]:
            ax.plot([x_left + 0.10, x_right - 0.10],
                    [y_mid, y_mid],
                    color="#ffd24a", lw=lw_h, alpha=aa,
                    solid_capstyle="round", zorder=5)

        # clock badge above arrow
        x_mid = (x_left + x_right) / 2
        y_badge = y_mid + 0.70
        ax.add_patch(Circle((x_mid, y_badge), 0.24,
                            facecolor="white",
                            edgecolor="#1f3b57", lw=1.8, zorder=8))
        ax.add_patch(Circle((x_mid, y_badge), 0.05,
                            facecolor="#1f3b57", zorder=9))
        ax.plot([x_mid, x_mid + 0.14],
                [y_badge, y_badge + 0.10],
                color="#1f3b57", lw=1.8,
                solid_capstyle="round", zorder=9)

    # =============================================================
    # Bottom: E(t) decay curve
    # =============================================================
    ax_x0_ = 1.1
    ax_x1_ = 11.9
    ax_y0_ = 2.3
    ax_y_top_ = 5.2

    ax.add_patch(FancyBboxPatch(
        (ax_x0_ - 0.25, ax_y0_ - 0.40),
        ax_x1_ - ax_x0_ + 0.5,
        ax_y_top_ - ax_y0_ + 0.55,
        boxstyle="round,pad=0.04,rounding_size=0.18",
        facecolor="white", edgecolor="#1f3b57",
        lw=1.5, alpha=0.88, zorder=2,
    ))

    # x-axis (time)
    ax.plot([ax_x0_ + 0.05, ax_x1_ - 0.05],
            [ax_y0_, ax_y0_],
            color="#1f3b57", lw=1.6, alpha=0.80, zorder=4)
    ax.annotate("",
                xy=(ax_x1_ - 0.05, ax_y0_),
                xytext=(ax_x0_ + 0.05, ax_y0_),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1f3b57", lw=1.6),
                zorder=5)

    # y-axis (energy)
    ax.plot([ax_x0_ + 0.05, ax_x0_ + 0.05],
            [ax_y0_, ax_y_top_],
            color="#1f3b57", lw=1.6, alpha=0.80, zorder=4)

    # E(t) exponential decay
    ts = np.linspace(ax_x0_ + 0.25, ax_x1_ - 0.30, 500)
    tn = (ts - ts[0]) / (ts[-1] - ts[0])
    E0 = ax_y_top_ - 0.20
    E = ax_y0_ + (E0 - ax_y0_) * np.exp(-2.8 * tn)

    # shaded area
    ax.fill_between(ts, ax_y0_, E,
                    color="#ffd98a", alpha=0.32, zorder=4)
    # glow + crisp stroke
    for lw_h, col, a in [(12, "#ffd98a", 0.14),
                         (7, "#ffb347", 0.26),
                         (4.0, "#c97a10", 0.96)]:
        ax.plot(ts, E, color=col, lw=lw_h, alpha=a,
                solid_capstyle="round", zorder=5)

    # three dots on the curve matching the snapshot colors/levels
    t_positions = [0.06, 0.34, 0.78]
    amp_levels = bar_frac_stored
    sn_colors = [s[2] for s in snapshots]
    for t_norm, amp_lvl, col in zip(t_positions, amp_levels, sn_colors):
        x_pt = ts[0] + t_norm * (ts[-1] - ts[0])
        y_pt = ax_y0_ + (E0 - ax_y0_) * np.exp(-2.8 * t_norm)
        for rr, a in [(0.22, 0.18), (0.15, 0.40)]:
            ax.add_patch(Circle((x_pt, y_pt), rr,
                                facecolor=col, edgecolor="none",
                                alpha=a, zorder=6))
        ax.add_patch(Circle((x_pt, y_pt), 0.12,
                            facecolor=col, edgecolor="#1f3b57",
                            lw=1.4, zorder=8))
        # vertical dashed line linking curve-dot to the snapshot above
        # (only for first two, to avoid clutter)
        ax.plot([x_pt, x_pt],
                [y_pt + 0.16, ax_y_top_ + 0.05],
                color="#1f3b57", lw=0.9, alpha=0.25,
                linestyle=(0, (3, 3)), zorder=4)

    # slim connectors from snapshots down to the curve dots
    for (snap_cx, snap_cy), t_norm, col in zip(
        panel_centers, t_positions,
        [s[2] for s in snapshots]
    ):
        x_t = ts[0] + t_norm * (ts[-1] - ts[0])
        ax.plot([snap_cx, x_t],
                [snap_y0 - 0.08, ax_y_top_ + 0.10],
                color=col, lw=1.2, alpha=0.30,
                linestyle=(0, (3, 4)), zorder=2)

    # =============================================================
    # "Arrow of time / no return" badge, lower-right
    # =============================================================
    nr_x, nr_y = ax_x1_ + 0.15, ax_y0_ + 0.30
    # NO BADGE — we don't want to over-clutter. Use a subtle
    # one-way double-chevron tag on the t-axis right end instead.
    # Two chevrons pointing right.
    for dx_ in [-0.08, 0.14]:
        ax.plot([ax_x1_ - 0.60 + dx_, ax_x1_ - 0.35 + dx_],
                [ax_y0_ + 0.18, ax_y0_],
                color="#c23b3b", lw=2.6, alpha=0.9,
                solid_capstyle="round", zorder=7)
        ax.plot([ax_x1_ - 0.60 + dx_, ax_x1_ - 0.35 + dx_],
                [ax_y0_ - 0.18, ax_y0_],
                color="#c23b3b", lw=2.6, alpha=0.9,
                solid_capstyle="round", zorder=7)

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
