"""
A4 Subadditivity — visual-only illustration (no text/equations baked in).

Metaphor: two overlapping Venn regions.
  - Circle A (teal) on the left
  - Circle B (amber) on the right
  - Lens-shaped overlap glows violet — the shared events
  - Event-dots: blue inside A-only, amber inside B-only, violet inside overlap
  - Two comparison columns on the right:
        left column  = ED(A) + ED(B)  -- taller, with the overlap band
                       visibly duplicated via a translucent "phantom"
                       stripe to convey double-counting
        right column = ED(A ∪ B)      -- shorter (overlap counted once)
    Both rise from the shared glowing zero baseline (A1/A2 continuity).
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, Ellipse, FancyArrowPatch,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\A4_subadditivity.png"


def glowing_dot(ax, x, y, r=0.11, core="#ffd24a", halo="#ffb347",
                edge="#a86d00", zorder=10):
    for rr, a in [(r * 2.6, 0.10),
                  (r * 2.0, 0.16),
                  (r * 1.5, 0.28),
                  (r * 1.15, 0.50)]:
        ax.add_patch(Circle((x, y), rr, facecolor=halo,
                            edgecolor="none", alpha=a, zorder=zorder - 1))
    ax.add_patch(Circle((x, y), r, facecolor=core, edgecolor=edge,
                        lw=0.9, alpha=0.98, zorder=zorder))
    ax.add_patch(Circle((x - r * 0.28, y + r * 0.28), r * 0.35,
                        facecolor="white", alpha=0.75, zorder=zorder + 1))


def build():
    fig, ax = plt.subplots(figsize=(11, 10), dpi=220)

    # ---- background -----------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 12, 0, 11], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 12, 2.0,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # ---- Venn circles ---------------------------------------------
    # A (teal) centered left, B (amber) centered right, with overlap
    AC = (3.4, 5.7)
    BC = (5.8, 5.7)
    R = 2.1

    # soft drop-shadows
    ax.add_patch(Circle((AC[0] + 0.06, AC[1] - 0.12), R,
                        facecolor="#00000014", edgecolor="none", zorder=1))
    ax.add_patch(Circle((BC[0] + 0.06, BC[1] - 0.12), R,
                        facecolor="#00000014", edgecolor="none", zorder=1))

    # A fill + outline
    ax.add_patch(Circle(AC, R, facecolor="#bfe0f1",
                        edgecolor="none", alpha=0.80, zorder=2))
    # B fill + outline
    ax.add_patch(Circle(BC, R, facecolor="#ffe5a1",
                        edgecolor="none", alpha=0.80, zorder=2))

    # ---- overlap-lens emphasis (violet glow) -----------------------
    # Compute the intersection via a polygon mask using a parametric
    # approach: two circular arcs meeting at the lens points.
    d = BC[0] - AC[0]
    # half-chord and chord-y
    a = d / 2
    h = np.sqrt(max(R * R - a * a, 0))
    px = AC[0] + a
    ptop = (px, AC[1] + h)
    pbot = (px, AC[1] - h)

    # Layered violet glow inside the lens using clipped circles.
    # Draw repeated thin violet-tinted filled arcs using a polygon
    # built from the two arcs.
    th_A = np.linspace(-np.arcsin(h / R), np.arcsin(h / R), 60)
    arcA_x = AC[0] + R * np.cos(th_A)
    arcA_y = AC[1] + R * np.sin(th_A)
    th_B = np.linspace(np.pi + np.arcsin(h / R),
                       np.pi - np.arcsin(h / R), 60)
    arcB_x = BC[0] + R * np.cos(th_B)
    arcB_y = BC[1] + R * np.sin(th_B)
    lens_x = np.concatenate([arcA_x, arcB_x])
    lens_y = np.concatenate([arcA_y, arcB_y])

    # soft outer violet halos around the lens
    for dilate, a_val in [(0.35, 0.06), (0.22, 0.10),
                          (0.12, 0.17), (0.04, 0.28)]:
        cx = (AC[0] + BC[0]) / 2
        cy = AC[1]
        xs = cx + (lens_x - cx) * (1 + dilate)
        ys = cy + (lens_y - cy) * (1 + dilate)
        ax.fill(xs, ys, facecolor="#8a5ac9", edgecolor="none",
                alpha=a_val, zorder=3)

    # lens fill (violet)
    ax.fill(lens_x, lens_y, facecolor="#c8aff0",
            edgecolor="none", alpha=0.90, zorder=4)
    # lens outline
    ax.plot(lens_x, lens_y, color="#6a3fb0", lw=2.6,
            zorder=6)

    # circle outlines (drawn after lens fill)
    ax.add_patch(Circle(AC, R, facecolor="none",
                        edgecolor="#2a7fa3", lw=3.0, zorder=7))
    ax.add_patch(Circle(BC, R, facecolor="none",
                        edgecolor="#d69a1a", lw=3.0, zorder=7))

    # ---- event-dots -----------------------------------------------
    rng = np.random.default_rng(9)

    def in_circle(x, y, c, r):
        return (x - c[0]) ** 2 + (y - c[1]) ** 2 <= r * r

    A_only, B_only, AB = [], [], []

    # dots in overlap
    while len(AB) < 5:
        x = rng.uniform(px - 0.55, px + 0.55)
        y = rng.uniform(AC[1] - 1.2, AC[1] + 1.2)
        if (in_circle(x, y, AC, R - 0.22)
                and in_circle(x, y, BC, R - 0.22)):
            if all(np.hypot(x - xx, y - yy) > 0.55
                   for xx, yy in AB):
                AB.append((x, y))

    # dots in A only
    while len(A_only) < 7:
        x = rng.uniform(AC[0] - R + 0.35, AC[0] + R - 0.35)
        y = rng.uniform(AC[1] - R + 0.35, AC[1] + R - 0.35)
        if in_circle(x, y, AC, R - 0.28) and not in_circle(x, y, BC, R - 0.1):
            if all(np.hypot(x - xx, y - yy) > 0.55
                   for xx, yy in A_only + AB):
                A_only.append((x, y))

    # dots in B only
    while len(B_only) < 7:
        x = rng.uniform(BC[0] - R + 0.35, BC[0] + R - 0.35)
        y = rng.uniform(BC[1] - R + 0.35, BC[1] + R - 0.35)
        if in_circle(x, y, BC, R - 0.28) and not in_circle(x, y, AC, R - 0.1):
            if all(np.hypot(x - xx, y - yy) > 0.55
                   for xx, yy in B_only + AB):
                B_only.append((x, y))

    for (x, y) in A_only:
        glowing_dot(ax, x, y, r=0.13,
                    core="#4fa3d8", halo="#7ec3de",
                    edge="#1e3b57", zorder=11)
    for (x, y) in B_only:
        glowing_dot(ax, x, y, r=0.13,
                    core="#ffd24a", halo="#ffb347",
                    edge="#a86d00", zorder=11)
    for (x, y) in AB:
        # violet shared dots — visibly different
        glowing_dot(ax, x, y, r=0.14,
                    core="#b48cef", halo="#8a5ac9",
                    edge="#4a1e85", zorder=12)

    # ---- measurement columns on the right -------------------------
    base_y = 1.55
    ped_x, ped_w, ped_h = 8.5, 3.15, 0.65

    # pedestal
    ax.add_patch(FancyBboxPatch(
        (ped_x, base_y - ped_h), ped_w, ped_h,
        boxstyle="round,pad=0.02,rounding_size=0.10",
        facecolor="#2f4d6b", edgecolor="#142536", lw=2.0, zorder=7,
    ))
    ax.add_patch(Rectangle((ped_x + 0.12, base_y - 0.16),
                           ped_w - 0.24, 0.08,
                           facecolor="#6b8aa8", alpha=0.7, zorder=8))

    # glowing baseline
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

    # ---- LEFT column: ED(A) + ED(B)  (A stacked on B, with phantom
    # duplicate of overlap band to show double-counting)
    # Counts:   A_only (7) + AB (5) -> A-part  = 12
    #           B_only (7) + AB (5) -> B-part  = 12
    #   sum                                      = 24 (overlap counted twice)
    # Union = 7 + 5 + 7                        = 19

    unit = 0.20
    colL_x, colL_w = 8.75, 1.0

    # --- B segment (bottom): 12 units
    h_B = 12 * unit
    n = 50
    for i in range(n):
        frac = i / n
        y0 = base_y + frac * h_B
        c = plt.cm.YlOrBr(0.30 + 0.40 * (1 - frac))
        ax.add_patch(Rectangle((colL_x, y0), colL_w,
                               h_B / n + 0.02,
                               facecolor=c, edgecolor="none",
                               alpha=0.95, zorder=8))
    # within B's segment: the 5-unit overlap band highlighted
    overlap_y0 = base_y + (12 - 5) * unit
    overlap_h = 5 * unit
    ax.add_patch(Rectangle((colL_x, overlap_y0), colL_w, overlap_h,
                           facecolor="#c8aff0", edgecolor="#6a3fb0",
                           lw=1.5, alpha=0.75, zorder=9))

    # --- A segment stacked on top (12 units)
    h_A = 12 * unit
    stack_y0 = base_y + h_B
    for i in range(n):
        frac = i / n
        y0 = stack_y0 + frac * h_A
        c = plt.cm.GnBu(0.45 + 0.35 * (1 - frac))
        ax.add_patch(Rectangle((colL_x, y0), colL_w,
                               h_A / n + 0.02,
                               facecolor=c, edgecolor="none",
                               alpha=0.95, zorder=8))
    # within A's segment: the 5-unit overlap band (DUPLICATE) highlighted
    # this phantom band is the "double counted" portion.
    dup_y0 = stack_y0
    ax.add_patch(Rectangle((colL_x, dup_y0), colL_w, overlap_h,
                           facecolor="#c8aff0", edgecolor="#6a3fb0",
                           lw=1.5, linestyle=(0, (4, 2)),
                           alpha=0.55, zorder=9, hatch="////"))

    # divider line between A and B segments
    ax.plot([colL_x - 0.05, colL_x + colL_w + 0.05],
            [base_y + h_B, base_y + h_B],
            color="#1f3b57", lw=1.8, zorder=11, alpha=0.6)

    # column outline
    ax.add_patch(FancyBboxPatch(
        (colL_x, base_y), colL_w, h_A + h_B,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        facecolor="none", edgecolor="#1f3b57", lw=2.4, zorder=12,
    ))
    # top cap
    ax.plot([colL_x - 0.08, colL_x + colL_w + 0.08],
            [base_y + h_A + h_B, base_y + h_A + h_B],
            color="#2a7fa3", lw=3.0, zorder=12, solid_capstyle="round")

    # curved arrow indicating "duplicate band"
    ax.annotate(
        "", xy=(colL_x - 0.08, dup_y0 + overlap_h / 2),
        xytext=(colL_x - 0.70, dup_y0 + overlap_h / 2 + 0.5),
        arrowprops=dict(arrowstyle="->", color="#6a3fb0",
                        lw=2.2,
                        connectionstyle="arc3,rad=0.35"),
        zorder=14,
    )
    # small violet badge at the arrow tail to symbolize the duplication
    ax.add_patch(Circle((colL_x - 0.78, dup_y0 + overlap_h / 2 + 0.55),
                        0.20, facecolor="#c8aff0",
                        edgecolor="#6a3fb0", lw=2.0, zorder=14))
    ax.plot([colL_x - 0.78 - 0.10, colL_x - 0.78 + 0.10],
            [dup_y0 + overlap_h / 2 + 0.55,
             dup_y0 + overlap_h / 2 + 0.55],
            color="#6a3fb0", lw=2.4, zorder=15)

    # ---- RIGHT column: ED(A ∪ B)  = 19 units (overlap counted once)
    colR_x, colR_w = 10.35, 1.0
    h_U = 19 * unit
    # gradient: a blend (violet-top → amber → teal bottom hinted)
    for i in range(n):
        frac = i / n
        y0 = base_y + frac * h_U
        # colormap mixes cool→warm across the column
        cmix = plt.cm.plasma(0.15 + 0.55 * (1 - frac))
        ax.add_patch(Rectangle((colR_x, y0), colR_w,
                               h_U / n + 0.02,
                               facecolor=cmix, edgecolor="none",
                               alpha=0.88, zorder=8))
    # overlap stripe (single occurrence) at its natural place
    ov_y0 = base_y + (19 - 5) * unit * 0.5  # visually centered-ish
    ax.add_patch(Rectangle((colR_x, ov_y0), colR_w, overlap_h,
                           facecolor="#c8aff0", edgecolor="#6a3fb0",
                           lw=1.5, alpha=0.75, zorder=9))

    ax.add_patch(FancyBboxPatch(
        (colR_x, base_y), colR_w, h_U,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        facecolor="none", edgecolor="#1f3b57", lw=2.4, zorder=12,
    ))
    ax.plot([colR_x - 0.08, colR_x + colR_w + 0.08],
            [base_y + h_U, base_y + h_U],
            color="#6a3fb0", lw=3.0, zorder=12, solid_capstyle="round")

    # comparator arrow (LEFT col taller than RIGHT col)
    arrow_top_L = base_y + h_A + h_B
    arrow_top_R = base_y + h_U
    arrow = FancyArrowPatch(
        (colL_x + colL_w + 0.06, arrow_top_L),
        (colR_x - 0.06, arrow_top_R),
        arrowstyle="-|>", mutation_scale=18,
        color="#1f3b57", lw=2.3, zorder=13,
    )
    ax.add_patch(arrow)
    # small downward chevron to emphasize "reduction"
    ax.annotate(
        "", xy=(colR_x + colR_w / 2, arrow_top_R - 0.02),
        xytext=(colR_x + colR_w / 2, arrow_top_L - 0.04),
        arrowprops=dict(arrowstyle="-|>", color="#1f3b57",
                        lw=2.0, alpha=0.7),
        zorder=13,
    )

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
