"""
Porous Medium Equation — visual-only illustration.

Metaphor: a thick, honey-like viscous fluid spreading over a porous
surface.  The Barenblatt self-similar solution has COMPACT SUPPORT —
the fluid has a crisp outer edge, not a soft tail — and the front
decelerates as it advances.  This distinguishes PME (nonlinear
diffusion) from the linear-diffusion image in the Mobility slide.

Composition:
  • Background: a stippled "porous medium" texture (pores of varying
    sizes on a warm beige field).
  • Center: a glossy teal puddle with a flat-top plateau and a sharp
    compact-support edge.
  • Two earlier-time ghosts shown as nested sharp-edged rings (smaller,
    taller look) to indicate the Barenblatt spreading history.
  • Short outward-pointing arrows around the rim, decreasing in length
    to hint "front decelerates."
  • Below: an inset 1D Barenblatt profile (flat plateau + sharp drop
    to zero) stacked across three time snapshots.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch,
)
from matplotlib.colors import LinearSegmentedColormap

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\PME_porous_medium.png"


def barenblatt_r_profile(r, R, beta):
    """Radial Barenblatt profile: (1 - (r/R)^2)^(1/β) for r<R, else 0."""
    out = np.zeros_like(r)
    mask = r < R
    out[mask] = (1.0 - (r[mask] / R) ** 2) ** (1.0 / beta)
    return out


def build():
    fig, ax = plt.subplots(figsize=(11, 11), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 12, 0, 12], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 12, 1.6,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # =============================================================
    # Main panel background — porous-medium "surface"
    # =============================================================
    panel_x0, panel_x1 = 0.9, 11.1
    panel_y0, panel_y1 = 4.0, 10.8
    panel_w = panel_x1 - panel_x0
    panel_h = panel_y1 - panel_y0

    # warm beige wash — the "sand/sponge" surface
    ax.add_patch(FancyBboxPatch(
        (panel_x0, panel_y0), panel_w, panel_h,
        boxstyle="round,pad=0.02,rounding_size=0.30",
        facecolor="#f4e6c9", edgecolor="#c9a66b",
        lw=2.4, alpha=0.95, zorder=2,
    ))

    # porous-medium texture — circles of varied size scattered
    rng = np.random.default_rng(5)
    n_pores = 260
    for _ in range(n_pores):
        x = rng.uniform(panel_x0 + 0.25, panel_x1 - 0.25)
        y = rng.uniform(panel_y0 + 0.25, panel_y1 - 0.25)
        r = rng.uniform(0.04, 0.13)
        col = rng.choice(["#d9b67d", "#c09955", "#e8cf9b"])
        ax.add_patch(Circle((x, y), r,
                            facecolor=col, edgecolor="none",
                            alpha=0.55, zorder=3))
        # subtle shadow inside pore
        ax.add_patch(Circle((x + r * 0.15, y - r * 0.15), r * 0.55,
                            facecolor="#8c6a2c", edgecolor="none",
                            alpha=0.35, zorder=4))

    # =============================================================
    # Center — viscous puddle with sharp compact-support edges
    # =============================================================
    pcx, pcy = 6.0, 6.80
    beta = 2.0   # β=2 (m=3) — canonical PME exponent

    # Three snapshot radii (earlier time = smaller radius)
    snapshot_radii = [3.60, 2.70, 1.80]
    snapshot_alphas = [0.85, 0.50, 0.25]   # outer most-recent largest,
    snapshot_linestyles = ["solid", "dashed", "dotted"]
    snapshot_colors = ["#0f5e85", "#2a7fa3", "#3fa6d0"]

    # Render the NEWEST snapshot as a filled 2D field (the actual puddle)
    R_now = snapshot_radii[0]
    N = 500
    xs = np.linspace(pcx - R_now - 0.3, pcx + R_now + 0.3, N)
    ys = np.linspace(pcy - R_now - 0.3, pcy + R_now + 0.3, N)
    X, Y = np.meshgrid(xs, ys)
    R_field = np.sqrt((X - pcx) ** 2 + (Y - pcy) ** 2)
    Z = barenblatt_r_profile(R_field.flatten(), R_now, beta).reshape(X.shape)

    # teal colormap with a punchy plateau & glossy top
    cmap = LinearSegmentedColormap.from_list(
        "pme_teal",
        [
            (0.00, (1.0, 1.0, 1.0, 0.0)),
            (0.02, (0.80, 0.92, 0.97, 0.0)),
            (0.08, (0.62, 0.86, 0.94, 0.70)),
            (0.30, (0.30, 0.70, 0.88, 0.92)),
            (0.60, (0.12, 0.50, 0.72, 0.98)),
            (1.00, (0.05, 0.30, 0.50, 1.00)),
        ],
    )

    # soft outer shadow first
    ax.add_patch(Circle((pcx + 0.12, pcy - 0.18), R_now + 0.05,
                        facecolor="#000000", alpha=0.10, zorder=5))
    # the field
    ax.imshow(
        Z, extent=[xs[0], xs[-1], ys[0], ys[-1]],
        origin="lower", cmap=cmap, alpha=0.95, zorder=6,
        interpolation="bilinear",
    )

    # crisp compact-support edge (the signature of PME vs linear diffusion)
    th = np.linspace(0, 2 * np.pi, 400)
    ex = pcx + R_now * np.cos(th)
    ey = pcy + R_now * np.sin(th)
    # glow
    for lw, col, a in [(10, "#9fe6f3", 0.18),
                       (6, "#6fd2e9", 0.30)]:
        ax.plot(ex, ey, color=col, lw=lw, alpha=a, zorder=7,
                solid_capstyle="round")
    ax.plot(ex, ey, color="#0b4a68", lw=2.6, alpha=0.95,
            zorder=8, solid_capstyle="round")

    # glossy highlight atop the puddle
    hl_x = pcx - 0.7
    hl_y = pcy + R_now * 0.35
    ax.add_patch(FancyBboxPatch(
        (hl_x, hl_y - 0.25), 1.8, 0.45,
        boxstyle="round,pad=0.02,rounding_size=0.20",
        facecolor="white", edgecolor="none",
        alpha=0.45, zorder=9,
    ))
    ax.add_patch(FancyBboxPatch(
        (hl_x + 0.25, hl_y + 0.05), 0.9, 0.18,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        facecolor="white", edgecolor="none",
        alpha=0.72, zorder=10,
    ))

    # ---- earlier-time snapshot rings (smaller, nested) ------------
    for R_s, col, style in zip(snapshot_radii[1:],
                               snapshot_colors[1:],
                               snapshot_linestyles[1:]):
        rx = pcx + R_s * np.cos(th)
        ry = pcy + R_s * np.sin(th)
        for lw, c2, a in [(8, col, 0.15)]:
            ax.plot(rx, ry, color=c2, lw=lw, alpha=a, zorder=6,
                    solid_capstyle="round")
        ax.plot(rx, ry, color=col, lw=2.2,
                linestyle=style, alpha=0.85, zorder=7,
                solid_capstyle="round")

    # ---- decelerating front arrows around the rim ----------------
    # Arrows are SHORT (decelerating); spaced around the circle.
    n_arrows = 12
    for k in range(n_arrows):
        th_k = (k + 0.5) * 2 * np.pi / n_arrows
        p0 = (pcx + (R_now + 0.08) * np.cos(th_k),
              pcy + (R_now + 0.08) * np.sin(th_k))
        arrow_len = 0.45  # deliberately short — slow front
        p1 = (pcx + (R_now + 0.08 + arrow_len) * np.cos(th_k),
              pcy + (R_now + 0.08 + arrow_len) * np.sin(th_k))
        for lw, col, a in [(5, "#9fe6f3", 0.25)]:
            ax.plot([p0[0], p1[0]], [p0[1], p1[1]],
                    color=col, lw=lw, alpha=a,
                    solid_capstyle="round", zorder=7)
        ax.add_patch(FancyArrowPatch(
            p0, p1,
            arrowstyle="-|>", mutation_scale=14,
            color="#1aa6c7", lw=2.0, zorder=8,
        ))
        # tiny "speed gauge" dot — faded to hint slowdown
        ax.add_patch(Circle(p1, 0.055,
                            facecolor="#1aa6c7", edgecolor="none",
                            alpha=0.55, zorder=8))

    # ---- "viscous drip" hints at the rim (2 small drips) ----------
    for drip_th in [np.deg2rad(235), np.deg2rad(305)]:
        dx = pcx + (R_now + 0.05) * np.cos(drip_th)
        dy = pcy + (R_now + 0.05) * np.sin(drip_th)
        # teardrop
        ax.add_patch(Circle((dx, dy - 0.12), 0.18,
                            facecolor="#3fa6d0", edgecolor="#0b4a68",
                            lw=1.4, alpha=0.95, zorder=9))
        ax.add_patch(Circle((dx - 0.05, dy - 0.07), 0.05,
                            facecolor="white", alpha=0.75, zorder=10))

    # =============================================================
    # Bottom inset: stacked 1D Barenblatt profiles
    # =============================================================
    inset_x0, inset_x1 = 1.3, 10.7
    inset_y_base = 1.95
    inset_y_top = 3.50

    ax.add_patch(FancyBboxPatch(
        (inset_x0 - 0.25, inset_y_base - 0.25),
        inset_x1 - inset_x0 + 0.5,
        inset_y_top - inset_y_base + 0.4,
        boxstyle="round,pad=0.04,rounding_size=0.18",
        facecolor="white", edgecolor="#1f3b57",
        lw=1.6, alpha=0.90, zorder=5,
    ))
    # baseline
    ax.plot([inset_x0, inset_x1], [inset_y_base, inset_y_base],
            color="#1f3b57", lw=1.6, alpha=0.85, zorder=6)

    mid_x = (inset_x0 + inset_x1) / 2
    profile_top = inset_y_top - 0.10
    scale_y = profile_top - inset_y_base

    # three profiles: tall & narrow → flat & wide (all with SHARP edge)
    profile_specs = [
        (1.35, 1.00, "#0f5e85", 2.8, "solid"),
        (2.30, 0.70, "#2a7fa3", 2.6, "dashed"),
        (3.50, 0.50, "#3fa6d0", 2.4, "dotted"),
    ]
    xs_p = np.linspace(inset_x0 + 0.15, inset_x1 - 0.15, 500)

    for R_b, h, col, lw, style in profile_specs:
        r = np.abs(xs_p - mid_x)
        prof = barenblatt_r_profile(r, R_b, beta=beta)
        ys_p = inset_y_base + h * prof * scale_y
        # glow
        for lw_halo, a in [(lw + 5, 0.12), (lw + 3, 0.22)]:
            ax.plot(xs_p, ys_p, color=col, lw=lw_halo,
                    alpha=a, solid_capstyle="round", zorder=6)
        ax.plot(xs_p, ys_p, color=col, lw=lw,
                linestyle=style, alpha=0.95, zorder=7,
                solid_capstyle="round")
        # sharp drop reinforcements at the endpoints
        left_edge = mid_x - R_b
        right_edge = mid_x + R_b
        for ex_ in [left_edge, right_edge]:
            ax.plot([ex_, ex_],
                    [inset_y_base, inset_y_base + 0.015],
                    color=col, lw=lw + 1, alpha=0.8, zorder=8,
                    solid_capstyle="round")
        # fill for the narrowest (tallest)
        if R_b == 1.35:
            ax.fill_between(xs_p, inset_y_base, ys_p,
                            color=col, alpha=0.12, zorder=6)

    # "time →" indicator arrow
    ax.annotate("",
                xy=(inset_x1 - 0.30, inset_y_base + 0.55),
                xytext=(inset_x1 - 1.30, inset_y_base + 0.20),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1f3b57", lw=2.0,
                                connectionstyle="arc3,rad=-0.25"),
                zorder=9)
    tbx, tby = inset_x1 - 1.50, inset_y_base + 0.18
    ax.add_patch(Circle((tbx, tby), 0.22,
                        facecolor="white", edgecolor="#1f3b57",
                        lw=1.8, zorder=10))
    ax.add_patch(Circle((tbx, tby), 0.05,
                        facecolor="#1f3b57", zorder=11))
    ax.plot([tbx, tbx + 0.14], [tby, tby + 0.10],
            color="#1f3b57", lw=1.8,
            solid_capstyle="round", zorder=11)

    # legend dots (3 snapshots)
    for i, (col, style) in enumerate(
        [("#0f5e85", "solid"),
         ("#2a7fa3", "dashed"),
         ("#3fa6d0", "dotted")]):
        ly = inset_y_top - 0.15 - i * 0.30
        ax.add_patch(Circle((inset_x0 + 0.15, ly), 0.08,
                            facecolor=col, edgecolor="white",
                            lw=1.2, zorder=10))

    # ---- framing ---------------------------------------------------
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
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
