"""
Compositional Rule — visual-only illustration (no text baked in).

Cosmological specialization of A4.  Two overlapping density-mounds
rendered as a 2D scalar field, with the three geometric penalties made
visually explicit:

  1. RELATIONAL penalty (overlap)   -> violet lens where the two mounds
                                        coincide, glowing brightest at
                                        the shared centre.
  2. GRADIENT penalty (steepness)   -> tightly packed contour "wall"
                                        along the ridge between the two
                                        peaks — the steep shoulder.
  3. BOUNDARY / HORIZON term (edge) -> a luminous amber rim traced
                                        around the outer perimeter of
                                        the union (an iso-level of the
                                        combined field).

Three small indicator badges sit outside the field, each a purely
iconic marker (no text) cueing which penalty it refers to:
  - violet interlocking-rings badge    (relational)
  - slanted-stripes badge              (gradient)
  - bright ring badge                  (boundary)
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, Ellipse, FancyArrowPatch,
)
from matplotlib.colors import LinearSegmentedColormap

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\Compositional_Rule.png"


def build():
    fig, ax = plt.subplots(figsize=(11, 10), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 12, 0, 11], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 12, 2.0,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # ---- density field: two Gaussian mounds -----------------------
    # Place the field in a central panel
    x_min, x_max = 1.2, 10.8
    y_min, y_max = 2.1, 9.5
    N = 700
    xs = np.linspace(x_min, x_max, N)
    ys = np.linspace(y_min, y_max, N)
    X, Y = np.meshgrid(xs, ys)

    # two Gaussians (A, B)  — closer together for a proper overlap lens
    A_c = (4.85, 5.85); A_s = 1.55
    B_c = (7.15, 5.85); B_s = 1.55
    ZA = np.exp(-(((X - A_c[0]) / A_s) ** 2 + ((Y - A_c[1]) / A_s) ** 2))
    ZB = np.exp(-(((X - B_c[0]) / B_s) ** 2 + ((Y - B_c[1]) / B_s) ** 2))
    Z = ZA + ZB
    Z_norm = Z / Z.max()

    # custom warm-to-cool colormap tuned for ED palette
    cmap = LinearSegmentedColormap.from_list(
        "ED_warm",
        [
            (0.00, "#f7fbfe"),
            (0.10, "#e6ecf2"),
            (0.25, "#c9d9e6"),
            (0.40, "#f3d6b3"),
            (0.55, "#ffb774"),
            (0.72, "#ff8a3c"),
            (0.88, "#d94f7b"),
            (1.00, "#6a3fb0"),
        ],
    )

    # field image (slightly transparent so it blends with backdrop)
    ax.imshow(
        Z_norm, extent=[x_min, x_max, y_min, y_max],
        origin="lower", cmap=cmap, alpha=0.92, zorder=2,
        interpolation="bilinear",
    )

    # a few subtle full-field contours (lighter, fewer)
    ax.contour(
        X, Y, Z_norm,
        levels=np.linspace(0.18, 0.90, 5),
        colors="#2a3a50", linewidths=0.6, alpha=0.18, zorder=3,
    )

    # ---- (1) RELATIONAL penalty: violet overlap glow --------------
    # highlight cells where BOTH ZA and ZB are non-trivially positive
    overlap_mask = (ZA > 0.25) & (ZB > 0.25)
    overlap_field = np.where(overlap_mask, ZA * ZB, np.nan)
    # plot as a violet-tinted overlay
    violet_cmap = LinearSegmentedColormap.from_list(
        "violet_over",
        [(0, (0.70, 0.55, 0.90, 0.0)),
         (1, (0.38, 0.18, 0.68, 0.95))],
    )
    ax.imshow(
        overlap_field, extent=[x_min, x_max, y_min, y_max],
        origin="lower", cmap=violet_cmap, alpha=0.95, zorder=4,
        interpolation="bilinear",
    )
    # inner lens iso-line
    ax.contour(
        X, Y, ZA * ZB,
        levels=[0.10, 0.25, 0.45],
        colors=["#a373d8", "#8a5ac9", "#6a3fb0"],
        linewidths=[1.2, 1.8, 2.4], alpha=0.95, zorder=5,
    )

    # ---- (2) GRADIENT penalty: steep-ridge band --------------------
    # compute |∇Z|; restrict the "gradient band" to one flank so it
    # reads as a single steep shoulder rather than a full contour map.
    gy, gx = np.gradient(Z_norm)
    gmag = np.hypot(gx, gy)
    gmag_n = gmag / gmag.max()

    # band-mask: only the upper-right flank of the union
    # (visually distinct from overlap and perimeter).
    cx_mid, cy_mid = (A_c[0] + B_c[0]) / 2, (A_c[1] + B_c[1]) / 2
    # we pick a quadrant on the outside of mound B (upper-right of B)
    flank_mask = (X > B_c[0] - 0.2) & (Y > B_c[1] - 0.2)
    gmag_masked = np.where(flank_mask, gmag_n, np.nan)

    # soft glow behind the flank
    ax.contourf(
        X, Y, gmag_masked,
        levels=[0.30, 1.01],
        colors=["#9fe6f3"], alpha=0.32, zorder=5,
    )
    # tightly packed steep-slope contours in saturated cyan
    ax.contour(
        X, Y, gmag_masked,
        levels=np.linspace(0.32, 0.85, 6),
        colors="#1aa6c7", linewidths=2.0, alpha=0.95, zorder=6,
    )

    # ---- (3) BOUNDARY / horizon penalty: luminous perimeter -------
    # outer iso-contour traces the union's edge
    outer_level = 0.12
    # three layered passes: wide soft halo, then bright core
    for lw, col, a in [(9.0, "#ffd24a", 0.18),
                       (6.0, "#ffb347", 0.30),
                       (4.2, "#ff9f1a", 0.60),
                       (2.4, "#fff1b0", 0.95)]:
        ax.contour(
            X, Y, Z_norm, levels=[outer_level],
            colors=col, linewidths=lw, alpha=a, zorder=7,
        )

    # ---- peaks: mark the two centres with glowing dots ------------
    for c, col, halo in [(A_c, "#ffd24a", "#ffb347"),
                         (B_c, "#ffd24a", "#ffb347")]:
        for rr, a in [(0.32, 0.10), (0.22, 0.20),
                      (0.15, 0.40), (0.10, 0.75)]:
            ax.add_patch(Circle(c, rr, facecolor=halo,
                                edgecolor="none", alpha=a, zorder=8))
        ax.add_patch(Circle(c, 0.09, facecolor=col,
                            edgecolor="#a86d00", lw=1.0, zorder=9))

    # =================================================================
    # Indicator badges (no text) — purely iconographic
    # =================================================================
    def draw_badge(bx, by, face, edge, r=0.45):
        for rr, a in [(r * 1.45, 0.08), (r * 1.22, 0.15),
                      (r * 1.08, 0.28)]:
            ax.add_patch(Circle((bx, by), rr, facecolor=edge,
                                edgecolor="none", alpha=a, zorder=10))
        ax.add_patch(Circle((bx, by), r,
                            facecolor=face, edgecolor=edge,
                            lw=2.6, zorder=11))

    # --- RELATIONAL badge (violet interlocking rings) — bottom centre
    rb_x, rb_y = 5.9, 1.10
    draw_badge(rb_x, rb_y, "#f1e6ff", "#6a3fb0", r=0.46)
    ax.add_patch(Circle((rb_x - 0.12, rb_y), 0.20,
                        facecolor="none", edgecolor="#6a3fb0",
                        lw=2.4, zorder=12))
    ax.add_patch(Circle((rb_x + 0.12, rb_y), 0.20,
                        facecolor="none", edgecolor="#6a3fb0",
                        lw=2.4, zorder=12))
    # arrow to overlap centre
    mid_overlap = ((A_c[0] + B_c[0]) / 2, (A_c[1] + B_c[1]) / 2)
    ax.annotate(
        "", xy=(mid_overlap[0], mid_overlap[1] - 0.2),
        xytext=(rb_x, rb_y + 0.55),
        arrowprops=dict(arrowstyle="->", color="#6a3fb0",
                        lw=2.2, alpha=0.9,
                        connectionstyle="arc3,rad=0.25"),
        zorder=12,
    )

    # --- GRADIENT badge (slanted stripes) — left side
    gb_x, gb_y = 1.0, 3.2
    draw_badge(gb_x, gb_y, "#dff3f8", "#1aa6c7", r=0.46)
    # diagonal stripes inside
    for s in np.linspace(-0.30, 0.30, 4):
        ax.plot([gb_x - 0.28 + s, gb_x + 0.05 + s],
                [gb_y - 0.28, gb_y + 0.28],
                color="#1aa6c7", lw=2.6, zorder=12,
                solid_capstyle="round")
    # arrow to the steep flank (upper-right of B)
    ridge_pt = (B_c[0] + 1.25, B_c[1] + 1.0)
    ax.annotate(
        "", xy=ridge_pt, xytext=(gb_x + 0.6, gb_y + 0.2),
        arrowprops=dict(arrowstyle="->", color="#1aa6c7",
                        lw=2.2, alpha=0.9,
                        connectionstyle="arc3,rad=-0.35"),
        zorder=12,
    )

    # --- BOUNDARY badge (bright ring) — right side
    bb_x, bb_y = 11.0, 3.2
    draw_badge(bb_x, bb_y, "#fff4d6", "#ff9f1a", r=0.46)
    ax.add_patch(Circle((bb_x, bb_y), 0.26,
                        facecolor="none", edgecolor="#ff9f1a",
                        lw=3.0, zorder=12))
    ax.add_patch(Circle((bb_x, bb_y), 0.26,
                        facecolor="none", edgecolor="#fff1b0",
                        lw=1.3, zorder=13))
    # arrow to outer rim (lower-right, away from the gradient flank)
    rim_pt = (B_c[0] + 1.55, B_c[1] - 1.25)
    ax.annotate(
        "", xy=rim_pt, xytext=(bb_x - 0.55, bb_y + 0.2),
        arrowprops=dict(arrowstyle="->", color="#ff9f1a",
                        lw=2.4, alpha=0.95,
                        connectionstyle="arc3,rad=0.25"),
        zorder=12,
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
