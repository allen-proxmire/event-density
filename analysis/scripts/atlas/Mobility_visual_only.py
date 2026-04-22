"""
Mobility channel alone — visual-only illustration.

Metaphor: ink-drop diffusion.  A density source at the center spreads
outward smoothly.  Three time-snapshot rings (t1 < t2 < t3) are drawn
concentrically — the profile is tight and bright at t1, wider and
dimmer at t2, widest and dimmest at t3 — the self-similar spreading
signature of the porous-medium / Barenblatt equation.

Radial outward flow arrows ring the density cloud.  A small 1D cross-
section inset at the bottom shows the stacked profiles (tall-narrow
→ short-broad) to reinforce "mass conserved, spatial extent grows."
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch,
)
from matplotlib.colors import LinearSegmentedColormap

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\Mobility_alone.png"


def build():
    fig, ax = plt.subplots(figsize=(11, 10), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 12, 0, 11], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 12, 1.6,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # =============================================================
    # Main panel: 2D density cloud (top, ~y >= 3.5)
    # =============================================================
    cx, cy = 6.0, 6.6
    panel_R = 4.0

    # ---- rendered 2D Gaussian density field -----------------------
    N = 700
    xs = np.linspace(cx - panel_R - 0.3, cx + panel_R + 0.3, N)
    ys = np.linspace(cy - panel_R - 0.3, cy + panel_R + 0.3, N)
    X, Y = np.meshgrid(xs, ys)
    sigma = 0.90  # the "t1" tight core
    Z1 = np.exp(-((X - cx) ** 2 + (Y - cy) ** 2) / (2 * sigma ** 2))
    # composite with broader snapshots (wider sigmas) to suggest the
    # diffusing stack
    Z = Z1.copy()
    for s, w in [(1.35, 0.55), (1.95, 0.30), (2.70, 0.18)]:
        Z += w * np.exp(-((X - cx) ** 2 + (Y - cy) ** 2) / (2 * s ** 2))
    Z = Z / Z.max()

    cmap = LinearSegmentedColormap.from_list(
        "mobility_teal",
        [
            (0.00, (1.0, 1.0, 1.0, 0.0)),
            (0.15, (0.83, 0.93, 0.98, 0.22)),
            (0.35, (0.62, 0.86, 0.94, 0.50)),
            (0.55, (0.25, 0.67, 0.87, 0.85)),
            (0.75, (0.10, 0.47, 0.68, 0.95)),
            (1.00, (0.04, 0.28, 0.47, 1.00)),
        ],
    )
    ax.imshow(
        Z, extent=[xs[0], xs[-1], ys[0], ys[-1]],
        origin="lower", cmap=cmap, alpha=0.90, zorder=2,
        interpolation="bilinear",
    )

    # ---- three time-snapshot rings (tight → broad) ----------------
    # Represent as iso-contours of Gaussians at three widths, each with
    # a distinct line style to read as "time snapshots."
    snapshots = [
        (1.00, "#1579a8", 2.8, (0, ())),         # t1 solid
        (1.75, "#3fa6d0", 2.4, (0, (8, 4))),     # t2 dashed
        (2.60, "#7ec3de", 2.0, (0, (3, 3))),     # t3 dotted
    ]
    for sig, col, lw, style in snapshots:
        # halo underlay
        Zring = np.exp(-((X - cx) ** 2 + (Y - cy) ** 2) / (2 * sig ** 2))
        for lw_halo, a in [(lw + 6, 0.10), (lw + 3, 0.20)]:
            ax.contour(X, Y, Zring,
                       levels=[np.exp(-0.5)],
                       colors=col, linewidths=lw_halo,
                       linestyles="solid", alpha=a, zorder=4)
        ax.contour(X, Y, Zring,
                   levels=[np.exp(-0.5)],
                   colors=col, linewidths=lw,
                   linestyles=[style], alpha=0.92, zorder=5)

    # ---- central source marker ------------------------------------
    ax.add_patch(Circle((cx, cy), 0.18,
                        facecolor="#0b4a68",
                        edgecolor="#021d2e", lw=1.4, zorder=9))
    ax.add_patch(Circle((cx - 0.05, cy + 0.05), 0.07,
                        facecolor="white", alpha=0.85, zorder=10))

    # ---- radial outward flow arrows -------------------------------
    n_arrows = 10
    for k in range(n_arrows):
        th = (k + 0.5) * 2 * np.pi / n_arrows
        r0 = 3.2
        r1 = 4.1
        p0 = (cx + r0 * np.cos(th), cy + r0 * np.sin(th))
        p1 = (cx + r1 * np.cos(th), cy + r1 * np.sin(th))
        # glow
        for lw, col, a in [(8, "#9fe6f3", 0.14),
                           (5, "#6fd2e9", 0.26)]:
            ax.plot([p0[0], p1[0]], [p0[1], p1[1]],
                    color=col, lw=lw, alpha=a,
                    solid_capstyle="round", zorder=3)
        arrow = FancyArrowPatch(
            p0, p1,
            arrowstyle="-|>", mutation_scale=18,
            color="#1aa6c7", lw=2.6, zorder=6,
        )
        ax.add_patch(arrow)

    # =============================================================
    # Bottom inset: 1D profile stack  (y ~ 1.8 to 3.3)
    # =============================================================
    inset_x0, inset_x1 = 1.3, 10.7
    inset_y_base = 1.95
    inset_y_top = 3.55

    # inset panel
    ax.add_patch(FancyBboxPatch(
        (inset_x0 - 0.25, inset_y_base - 0.25),
        inset_x1 - inset_x0 + 0.5,
        inset_y_top - inset_y_base + 0.4,
        boxstyle="round,pad=0.04,rounding_size=0.18",
        facecolor="white", edgecolor="#1f3b57",
        lw=1.6, alpha=0.88, zorder=5,
    ))

    # axes baseline
    ax.plot([inset_x0, inset_x1], [inset_y_base, inset_y_base],
            color="#1f3b57", lw=1.6, alpha=0.85, zorder=6)
    # vertical midline for symmetry hint
    mid_x = (inset_x0 + inset_x1) / 2
    ax.plot([mid_x, mid_x], [inset_y_base - 0.06, inset_y_base + 0.06],
            color="#1f3b57", lw=1.2, alpha=0.6, zorder=6)

    # three profiles — same total integral, narrower → broader
    xs_p = np.linspace(inset_x0 + 0.1, inset_x1 - 0.1, 400)
    profile_top = inset_y_top - 0.15
    scale_y = profile_top - inset_y_base

    for sig, col, lw, style in [
        (0.55, "#1579a8", 3.0, (0, ())),
        (0.95, "#3fa6d0", 2.7, (0, (8, 4))),
        (1.55, "#7ec3de", 2.5, (0, (3, 3))),
    ]:
        peak = 1.0 / (sig * np.sqrt(2 * np.pi))
        amp_norm = 1.0 / (peak)
        gauss = (1.0 / (sig * np.sqrt(2 * np.pi))
                 * np.exp(-((xs_p - mid_x) ** 2) / (2 * sig ** 2)))
        # normalize so each profile reaches a consistent visual scale
        # (peak of narrowest = full height, broader lower)
        norm = gauss / (1.0 / (0.55 * np.sqrt(2 * np.pi)))
        ys_p = inset_y_base + norm * scale_y
        # glow underlay
        for lw_halo, a in [(lw + 5, 0.12), (lw + 3, 0.22)]:
            ax.plot(xs_p, ys_p, color=col, lw=lw_halo,
                    alpha=a, solid_capstyle="round", zorder=6)
        ax.plot(xs_p, ys_p, color=col, lw=lw,
                linestyle=style, alpha=0.95, zorder=7,
                solid_capstyle="round")
        # shaded fill for the narrowest profile only (subtle)
        if sig == 0.55:
            ax.fill_between(xs_p, inset_y_base, ys_p,
                            color=col, alpha=0.10, zorder=6)

    # small arrow indicating "time increases → profile broadens"
    ax.annotate("",
                xy=(inset_x1 - 0.35, inset_y_base + 0.65),
                xytext=(inset_x1 - 1.40, inset_y_base + 0.25),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1f3b57", lw=2.0,
                                connectionstyle="arc3,rad=-0.25"),
                zorder=9)
    # badge at arrow tail = a clock-ish icon (circle + tick)
    tbx, tby = inset_x1 - 1.60, inset_y_base + 0.22
    ax.add_patch(Circle((tbx, tby), 0.22,
                        facecolor="white", edgecolor="#1f3b57",
                        lw=1.8, zorder=10))
    ax.add_patch(Circle((tbx, tby), 0.05,
                        facecolor="#1f3b57", edgecolor="none", zorder=11))
    ax.plot([tbx, tbx + 0.14], [tby, tby + 0.10],
            color="#1f3b57", lw=1.8, solid_capstyle="round", zorder=11)

    # legend dots on the left of the inset for t1/t2/t3
    for i, (col, style) in enumerate(
        [("#1579a8", "solid"),
         ("#3fa6d0", "dashed"),
         ("#7ec3de", "dotted")]):
        ly = inset_y_top - 0.15 - i * 0.30
        ax.add_patch(Circle((inset_x0 + 0.15, ly), 0.08,
                            facecolor=col, edgecolor="white",
                            lw=1.2, zorder=10))

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
