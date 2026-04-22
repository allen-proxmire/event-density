"""
A3 Monotonicity — visual-only illustration (no text/equations baked in).

Metaphor: nested regions A ⊆ B with event-dots scattered inside.
  - Outer region B (large rounded rectangle, warm tint) contains every
    event-dot that is in A, PLUS additional dots in the annular region.
  - Inner region A (smaller rounded rectangle, cool tint) nested inside.
  - A pair of measurement "columns" on the right rise from the same
    glowing zero baseline (visual continuity with A1/A2):
        column_A (shorter)  ≤  column_B (taller).

Text is intentionally absent; the user overlays captions later.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, Ellipse, FancyArrowPatch,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\A3_monotonicity.png"


def glowing_dot(ax, x, y, r=0.11, core="#ffd24a", halo="#ffb347",
                zorder=10):
    """Event-dot with soft radial glow."""
    for rr, a in [(r * 2.6, 0.10),
                  (r * 2.0, 0.16),
                  (r * 1.5, 0.28),
                  (r * 1.15, 0.50)]:
        ax.add_patch(Circle((x, y), rr,
                            facecolor=halo, edgecolor="none",
                            alpha=a, zorder=zorder - 1))
    ax.add_patch(Circle((x, y), r,
                        facecolor=core, edgecolor="#a86d00",
                        lw=0.9, alpha=0.98, zorder=zorder))
    ax.add_patch(Circle((x - r * 0.28, y + r * 0.28), r * 0.35,
                        facecolor="white", alpha=0.75,
                        zorder=zorder + 1))


def build():
    fig, ax = plt.subplots(figsize=(10, 10), dpi=220)

    # ---- background ------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 11, 0, 11], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 11, 2.0,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # ---- OUTER region B -------------------------------------------
    bx, by, bw, bh = 1.0, 2.2, 6.4, 6.6
    # soft shadow
    ax.add_patch(FancyBboxPatch(
        (bx + 0.08, by - 0.12), bw, bh,
        boxstyle="round,pad=0.02,rounding_size=0.4",
        facecolor="#00000014", edgecolor="none", zorder=1,
    ))
    # fill
    ax.add_patch(FancyBboxPatch(
        (bx, by), bw, bh,
        boxstyle="round,pad=0.02,rounding_size=0.4",
        facecolor="#fff1c2", edgecolor="none", alpha=0.75, zorder=2,
    ))
    # outline
    ax.add_patch(FancyBboxPatch(
        (bx, by), bw, bh,
        boxstyle="round,pad=0.02,rounding_size=0.4",
        facecolor="none", edgecolor="#d69a1a", lw=3.4, zorder=6,
    ))

    # ---- INNER region A (nested inside B) -------------------------
    ax_x, ax_y, ax_w, ax_h = 1.9, 3.2, 3.2, 3.3
    ax.add_patch(FancyBboxPatch(
        (ax_x, ax_y), ax_w, ax_h,
        boxstyle="round,pad=0.02,rounding_size=0.3",
        facecolor="#c6e5f3", edgecolor="none", alpha=0.85, zorder=3,
    ))
    # dashed inner outline to emphasize subset boundary
    ax.add_patch(FancyBboxPatch(
        (ax_x, ax_y), ax_w, ax_h,
        boxstyle="round,pad=0.02,rounding_size=0.3",
        facecolor="none", edgecolor="#2a7fa3", lw=2.8,
        linestyle=(0, (6, 3)), zorder=5,
    ))
    # solid thin inner outline under the dashed for clarity
    ax.add_patch(FancyBboxPatch(
        (ax_x, ax_y), ax_w, ax_h,
        boxstyle="round,pad=0.02,rounding_size=0.3",
        facecolor="none", edgecolor="#1f3b57", lw=1.2, alpha=0.4, zorder=4,
    ))

    # ---- event dots ----------------------------------------------
    rng = np.random.default_rng(4)

    # dots inside A  (count = 8)
    A_dots = []
    while len(A_dots) < 8:
        x = rng.uniform(ax_x + 0.35, ax_x + ax_w - 0.35)
        y = rng.uniform(ax_y + 0.35, ax_y + ax_h - 0.35)
        # min-distance reject
        if all(np.hypot(x - xx, y - yy) > 0.55 for xx, yy in A_dots):
            A_dots.append((x, y))
    for (x, y) in A_dots:
        glowing_dot(ax, x, y, r=0.13,
                    core="#4fa3d8", halo="#7ec3de", zorder=10)

    # dots in B \ A  (count = 12)
    BA_dots = []
    target = 12
    tries = 0
    while len(BA_dots) < target and tries < 4000:
        tries += 1
        x = rng.uniform(bx + 0.35, bx + bw - 0.35)
        y = rng.uniform(by + 0.35, by + bh - 0.35)
        in_A = (ax_x + 0.15 < x < ax_x + ax_w - 0.15
                and ax_y + 0.15 < y < ax_y + ax_h - 0.15)
        if in_A:
            continue
        too_close = False
        for xx, yy in BA_dots + A_dots:
            if np.hypot(x - xx, y - yy) < 0.60:
                too_close = True
                break
        if too_close:
            continue
        BA_dots.append((x, y))
    for (x, y) in BA_dots:
        glowing_dot(ax, x, y, r=0.13,
                    core="#ffd24a", halo="#ffb347", zorder=10)

    # ---- measurement columns on the right -------------------------
    # Shared pedestal
    base_y = 1.55
    ped_x, ped_w, ped_h = 7.9, 2.8, 0.65
    ax.add_patch(FancyBboxPatch(
        (ped_x, base_y - ped_h), ped_w, ped_h,
        boxstyle="round,pad=0.02,rounding_size=0.10",
        facecolor="#2f4d6b", edgecolor="#142536", lw=2.0, zorder=7,
    ))
    ax.add_patch(Rectangle((ped_x + 0.12, base_y - 0.16),
                           ped_w - 0.24, 0.08,
                           facecolor="#6b8aa8", alpha=0.7, zorder=8))

    # glowing zero baseline spanning the pedestal (and beyond)
    for glow_h, a in [(0.60, 0.06), (0.40, 0.12),
                      (0.24, 0.22), (0.14, 0.38), (0.08, 0.65)]:
        ax.add_patch(Rectangle(
            (ped_x - 0.3, base_y - glow_h / 2),
            ped_w + 0.6, glow_h,
            facecolor="#ffc23a", edgecolor="none", alpha=a, zorder=6,
        ))
    ax.plot([ped_x - 0.1, ped_x + ped_w + 0.1], [base_y, base_y],
            color="#ff9f1a", lw=5.5, zorder=9, solid_capstyle="round")
    ax.plot([ped_x - 0.1, ped_x + ped_w + 0.1], [base_y, base_y],
            color="#fff1b0", lw=2.2, zorder=10, solid_capstyle="round")

    # column A  (shorter, cool blue — matches A dots)
    colA_x, colA_w = 8.2, 0.95
    colA_h = 2.8  # proportional to 8 units
    # column gradient
    nlayers = 60
    for i in range(nlayers):
        frac = i / nlayers
        y0 = base_y + frac * colA_h
        c = plt.cm.GnBu(0.45 + 0.35 * (1 - frac))
        ax.add_patch(Rectangle((colA_x, y0), colA_w,
                               colA_h / nlayers + 0.02,
                               facecolor=c, edgecolor="none",
                               alpha=0.95, zorder=8))
    ax.add_patch(FancyBboxPatch(
        (colA_x, base_y), colA_w, colA_h,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        facecolor="none", edgecolor="#1f3b57", lw=2.4, zorder=11,
    ))
    # small tick cap on top
    ax.plot([colA_x - 0.08, colA_x + colA_w + 0.08],
            [base_y + colA_h, base_y + colA_h],
            color="#2a7fa3", lw=3.0, zorder=12, solid_capstyle="round")

    # column B  (taller, warm amber — matches B-extra dots)
    colB_x, colB_w = 9.45, 1.05
    colB_h = 5.4  # proportional to 20 units
    for i in range(nlayers):
        frac = i / nlayers
        y0 = base_y + frac * colB_h
        c = plt.cm.YlOrBr(0.30 + 0.40 * (1 - frac))
        ax.add_patch(Rectangle((colB_x, y0), colB_w,
                               colB_h / nlayers + 0.02,
                               facecolor=c, edgecolor="none",
                               alpha=0.95, zorder=8))
    ax.add_patch(FancyBboxPatch(
        (colB_x, base_y), colB_w, colB_h,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        facecolor="none", edgecolor="#7a4a0a", lw=2.4, zorder=11,
    ))
    ax.plot([colB_x - 0.08, colB_x + colB_w + 0.08],
            [base_y + colB_h, base_y + colB_h],
            color="#d69a1a", lw=3.0, zorder=12, solid_capstyle="round")

    # connector arrow A → B (showing ≤)
    arrow = FancyArrowPatch(
        (colA_x + colA_w + 0.05, base_y + colA_h),
        (colB_x - 0.05, base_y + colA_h),
        arrowstyle="-|>", mutation_scale=18,
        color="#1f3b57", lw=2.2, zorder=13,
    )
    ax.add_patch(arrow)
    # upward hint from A top to B's greater height
    arrow2 = FancyArrowPatch(
        (colB_x + colB_w / 2, base_y + colA_h + 0.05),
        (colB_x + colB_w / 2, base_y + colB_h - 0.08),
        arrowstyle="-|>", mutation_scale=16,
        color="#7a4a0a", lw=2.0, zorder=13, alpha=0.85,
    )
    ax.add_patch(arrow2)

    # subtle "A inside B" indicator: a small inline glyph bottom-left of B
    # — a tiny circle-inside-circle motif
    gly_x, gly_y = bx + 0.55, by + 0.55
    ax.add_patch(Circle((gly_x, gly_y), 0.32,
                        facecolor="none", edgecolor="#d69a1a",
                        lw=2.3, zorder=7))
    ax.add_patch(Circle((gly_x - 0.04, gly_y + 0.02), 0.16,
                        facecolor="none", edgecolor="#2a7fa3",
                        lw=2.3, linestyle=(0, (3, 2)), zorder=8))

    # ---- framing ---------------------------------------------------
    ax.set_xlim(0, 11)
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
