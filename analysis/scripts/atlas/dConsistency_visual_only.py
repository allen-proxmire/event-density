"""
d-Consistency — visual-only illustration.

Metaphor: a dimensional ladder.  The same scaling rule
  α_R = 1 / (d(m−1) + 2)
holds exactly for d = 1, 2, 3 — a structural invariant across
dimension.

Composition:
  THREE COLUMN PANELS left-to-right, each showing a stylized Barenblatt-
  style spreading object in its respective dimension:
      1D : a horizontal line segment with a spreading hump
      2D : a flat square panel with a spreading circular "puddle"
      3D : an isometric-drawn cube with a spreading sphere inside
  Each panel is tagged by a colored "d = N" badge at the bottom.

  CENTER-TOP : a glowing gold invariant badge — the "same formula"
               star/orb — with thin dashed connectors linking each
               column panel to the badge.
  BOTTOM  : a horizontal "dimension ladder" axis with three bright
            ticks for d=1, 2, 3 and an α_R marker for each (same rule,
            different numerical value).
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, Polygon, FancyArrowPatch, Ellipse,
)
from matplotlib.path import Path
from matplotlib.patches import PathPatch

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\dConsistency.png"


def invariant_orb(ax, x, y, r=0.55, zorder=10):
    for rr, a in [(r * 2.2, 0.05),
                  (r * 1.7, 0.10),
                  (r * 1.35, 0.20),
                  (r * 1.12, 0.38)]:
        ax.add_patch(Circle((x, y), rr, facecolor="#ffd24a",
                            edgecolor="none", alpha=a,
                            zorder=zorder - 1))
    for rr, col in [(r * 0.95, "#fff1b0"),
                    (r * 0.80, "#ffd24a"),
                    (r * 0.62, "#ffb347"),
                    (r * 0.44, "#ff9f1a"),
                    (r * 0.28, "#e07b00")]:
        ax.add_patch(Circle((x, y), rr, facecolor=col,
                            edgecolor="none", zorder=zorder))
    ax.add_patch(Circle((x - r * 0.28, y + r * 0.30), r * 0.25,
                        facecolor="white", alpha=0.78,
                        zorder=zorder + 1))
    ax.add_patch(Circle((x, y), r, facecolor="none",
                        edgecolor="#c97a10", lw=2.0,
                        zorder=zorder + 2))


def dim_badge(ax, cx, cy, label, face, edge, hash_count):
    """Bottom badge showing a stylized 'd=N' marker using hash marks."""
    for rr, a in [(0.52, 0.08), (0.40, 0.16), (0.30, 0.30)]:
        ax.add_patch(Circle((cx, cy), rr, facecolor=face,
                            edgecolor="none", alpha=a, zorder=10))
    ax.add_patch(Circle((cx, cy), 0.32,
                        facecolor="white", edgecolor=edge,
                        lw=2.4, zorder=11))
    # hash marks inside
    total_w = 0.22
    for k in range(hash_count):
        gx = cx - total_w / 2 + k * (total_w / max(hash_count - 1, 1))
        ax.plot([gx, gx], [cy - 0.12, cy + 0.12],
                color=edge, lw=2.6, solid_capstyle="round",
                zorder=12)


def build():
    fig, ax = plt.subplots(figsize=(13, 10), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 14, 0, 11], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 14, 1.5,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # =============================================================
    # Central invariant orb (top-middle)
    # =============================================================
    ccx, ccy = 7.0, 9.3
    # starburst rays
    for ang_deg in np.linspace(0, 360, 24, endpoint=False):
        th = np.deg2rad(ang_deg)
        r0 = 0.75
        r1 = 1.45
        ax.plot([ccx + r0 * np.cos(th), ccx + r1 * np.cos(th)],
                [ccy + r0 * np.sin(th), ccy + r1 * np.sin(th)],
                color="#ffd98a", lw=1.6, alpha=0.24,
                solid_capstyle="round", zorder=2)
    invariant_orb(ax, ccx, ccy, r=0.80, zorder=11)

    # =============================================================
    # Three dimensional panels
    # =============================================================
    panel_h = 4.2
    panel_w = 3.8
    panel_y0 = 2.7
    gap = 0.35
    total_w = 3 * panel_w + 2 * gap
    start_x = (14 - total_w) / 2

    panel_centers = []

    # ---------- PANEL 1: 1D ----------
    p1_x0 = start_x
    p1_x1 = p1_x0 + panel_w

    # panel bg
    ax.add_patch(FancyBboxPatch(
        (p1_x0, panel_y0), panel_w, panel_h,
        boxstyle="round,pad=0.04,rounding_size=0.22",
        facecolor="#e6f4fa", edgecolor="#1aa6c7",
        lw=2.2, alpha=0.90, zorder=3,
    ))
    # horizontal line (the 1D ambient space)
    axis_y = panel_y0 + panel_h * 0.30
    ax.plot([p1_x0 + 0.45, p1_x1 - 0.45], [axis_y, axis_y],
            color="#1f3b57", lw=2.4, zorder=5,
            solid_capstyle="round")

    # spreading 1D bump: Barenblatt profile on a line
    xs_b = np.linspace(p1_x0 + 0.55, p1_x1 - 0.55, 240)
    mid1 = (p1_x0 + p1_x1) / 2
    R_1d = 1.25
    r_from_mid = np.abs(xs_b - mid1)
    # compact support flat-top profile
    bump = np.where(r_from_mid < R_1d,
                    (1 - (r_from_mid / R_1d) ** 2) ** 0.5,
                    0.0)
    y_bump = axis_y + bump * 1.35
    # fill under bump
    ax.fill_between(xs_b, axis_y, y_bump,
                    color="#9fe6f3", alpha=0.65, zorder=6)
    # glow + crisp outline
    for lw, col, a in [(9, "#9fe6f3", 0.20),
                       (5, "#6fd2e9", 0.38),
                       (2.8, "#1579a8", 0.98)]:
        ax.plot(xs_b, y_bump, color=col, lw=lw, alpha=a,
                solid_capstyle="round", zorder=7)
    # outward arrows on the line (spreading)
    for dx_ in [-1.4, +1.4]:
        ax.add_patch(FancyArrowPatch(
            (mid1 + dx_ * 0.6, axis_y),
            (mid1 + dx_, axis_y),
            arrowstyle="-|>", mutation_scale=16,
            color="#1aa6c7", lw=2.2, zorder=8,
        ))
    # badge bottom
    dim_badge(ax, mid1, panel_y0 + 0.50,
              label="1", face="#9fe6f3", edge="#1aa6c7",
              hash_count=1)
    panel_centers.append((mid1, panel_y0 + panel_h * 0.55))

    # ---------- PANEL 2: 2D ----------
    p2_x0 = p1_x1 + gap
    p2_x1 = p2_x0 + panel_w
    ax.add_patch(FancyBboxPatch(
        (p2_x0, panel_y0), panel_w, panel_h,
        boxstyle="round,pad=0.04,rounding_size=0.22",
        facecolor="#ecf9ec", edgecolor="#2fb27a",
        lw=2.2, alpha=0.90, zorder=3,
    ))
    # 2D inner square: the "ambient 2D space"
    mid2 = (p2_x0 + p2_x1) / 2
    sq_cy = panel_y0 + panel_h * 0.55
    sq_half = 1.35
    ax.add_patch(FancyBboxPatch(
        (mid2 - sq_half, sq_cy - sq_half),
        sq_half * 2, sq_half * 2,
        boxstyle="round,pad=0.02,rounding_size=0.12",
        facecolor="white", edgecolor="#1f3b57",
        lw=2.0, alpha=0.85, zorder=5,
    ))

    # Barenblatt 2D puddle (top-down circle with shading)
    N = 300
    xs_2 = np.linspace(mid2 - sq_half + 0.05, mid2 + sq_half - 0.05, N)
    ys_2 = np.linspace(sq_cy - sq_half + 0.05, sq_cy + sq_half - 0.05, N)
    X, Y = np.meshgrid(xs_2, ys_2)
    R_field = np.sqrt((X - mid2) ** 2 + (Y - sq_cy) ** 2)
    R_2d = 1.0
    Z = np.where(R_field < R_2d, (1 - (R_field / R_2d) ** 2) ** 0.5, 0.0)

    # render as imshow (green cmap)
    from matplotlib.colors import LinearSegmentedColormap
    cmap_green = LinearSegmentedColormap.from_list(
        "green_pme",
        [(0.00, (1.0, 1.0, 1.0, 0.0)),
         (0.08, (0.71, 0.91, 0.81, 0.65)),
         (0.40, (0.30, 0.70, 0.55, 0.90)),
         (0.80, (0.12, 0.47, 0.36, 0.98)),
         (1.00, (0.04, 0.25, 0.20, 1.00))],
    )
    ax.imshow(Z, extent=[xs_2[0], xs_2[-1], ys_2[0], ys_2[-1]],
              origin="lower", cmap=cmap_green, alpha=0.95, zorder=6,
              interpolation="bilinear")
    # sharp edge ring
    th_c = np.linspace(0, 2 * np.pi, 200)
    ex_c = mid2 + R_2d * np.cos(th_c)
    ey_c = sq_cy + R_2d * np.sin(th_c)
    for lw, col, a in [(8, "#b6e7cf", 0.20),
                       (4.5, "#6fd2e9", 0.30)]:
        ax.plot(ex_c, ey_c, color=col, lw=lw, alpha=a, zorder=7)
    ax.plot(ex_c, ey_c, color="#1b6f4a", lw=2.0, alpha=0.95, zorder=8)

    # outward arrows (4 directions)
    for ang in np.linspace(0, 2 * np.pi, 4, endpoint=False):
        ax.add_patch(FancyArrowPatch(
            (mid2 + (R_2d + 0.05) * np.cos(ang),
             sq_cy + (R_2d + 0.05) * np.sin(ang)),
            (mid2 + (R_2d + 0.30) * np.cos(ang),
             sq_cy + (R_2d + 0.30) * np.sin(ang)),
            arrowstyle="-|>", mutation_scale=14,
            color="#2fb27a", lw=2.0, zorder=8,
        ))

    dim_badge(ax, mid2, panel_y0 + 0.50,
              label="2", face="#b6e7cf", edge="#2fb27a",
              hash_count=2)
    panel_centers.append((mid2, panel_y0 + panel_h * 0.55))

    # ---------- PANEL 3: 3D ----------
    p3_x0 = p2_x1 + gap
    p3_x1 = p3_x0 + panel_w
    ax.add_patch(FancyBboxPatch(
        (p3_x0, panel_y0), panel_w, panel_h,
        boxstyle="round,pad=0.04,rounding_size=0.22",
        facecolor="#f1e6ff", edgecolor="#8a5ac9",
        lw=2.2, alpha=0.90, zorder=3,
    ))
    # draw an isometric-looking cube
    mid3 = (p3_x0 + p3_x1) / 2
    cube_cy = panel_y0 + panel_h * 0.58
    s = 1.25
    # depth offset
    dx_iso = 0.55
    dy_iso = 0.40
    # front face corners
    F_bl = (mid3 - s, cube_cy - s)
    F_br = (mid3 + s, cube_cy - s)
    F_tr = (mid3 + s, cube_cy + s)
    F_tl = (mid3 - s, cube_cy + s)
    # back face corners
    B_bl = (F_bl[0] + dx_iso, F_bl[1] + dy_iso)
    B_br = (F_br[0] + dx_iso, F_br[1] + dy_iso)
    B_tr = (F_tr[0] + dx_iso, F_tr[1] + dy_iso)
    B_tl = (F_tl[0] + dx_iso, F_tl[1] + dy_iso)

    # top face polygon
    ax.add_patch(Polygon([F_tl, F_tr, B_tr, B_tl],
                         closed=True, facecolor="#d4c1f0",
                         edgecolor="#6a3fb0",
                         lw=2.0, alpha=0.80, zorder=4))
    # right face polygon
    ax.add_patch(Polygon([F_br, F_tr, B_tr, B_br],
                         closed=True, facecolor="#b79ae0",
                         edgecolor="#6a3fb0",
                         lw=2.0, alpha=0.80, zorder=4))
    # front face
    ax.add_patch(Polygon([F_bl, F_br, F_tr, F_tl],
                         closed=True, facecolor="#eadfff",
                         edgecolor="#6a3fb0",
                         lw=2.4, alpha=0.92, zorder=5))

    # sphere inside the cube (centered)
    sph_cx = mid3 + dx_iso / 2
    sph_cy_ = cube_cy + dy_iso / 2
    sph_R = 0.85

    # layered halo
    for rr, a in [(sph_R * 1.8, 0.07),
                  (sph_R * 1.4, 0.14),
                  (sph_R * 1.1, 0.28)]:
        ax.add_patch(Circle((sph_cx, sph_cy_), rr,
                            facecolor="#c8aff0",
                            edgecolor="none", alpha=a, zorder=6))
    # sphere body (gradient via stacked circles)
    for rr, col in [(sph_R, "#c8aff0"),
                    (sph_R * 0.85, "#a57fe0"),
                    (sph_R * 0.68, "#8a5ac9"),
                    (sph_R * 0.50, "#6a3fb0"),
                    (sph_R * 0.32, "#4a1e85")]:
        ax.add_patch(Circle(
            (sph_cx - 0.05 * (sph_R - rr) / sph_R,
             sph_cy_ + 0.05 * (sph_R - rr) / sph_R),
            rr, facecolor=col, edgecolor="none", zorder=7,
        ))
    # specular
    ax.add_patch(Circle((sph_cx - sph_R * 0.30, sph_cy_ + sph_R * 0.30),
                        sph_R * 0.20,
                        facecolor="white", alpha=0.75, zorder=9))
    # outline
    ax.add_patch(Circle((sph_cx, sph_cy_), sph_R,
                        facecolor="none", edgecolor="#4a1e85",
                        lw=1.8, zorder=8))

    # outward arrows in 3D (8 directions on the sphere's surface)
    for ang in np.linspace(0, 2 * np.pi, 6, endpoint=False):
        p0 = (sph_cx + (sph_R + 0.08) * np.cos(ang),
              sph_cy_ + (sph_R + 0.08) * np.sin(ang))
        p1 = (sph_cx + (sph_R + 0.30) * np.cos(ang),
              sph_cy_ + (sph_R + 0.30) * np.sin(ang))
        ax.add_patch(FancyArrowPatch(
            p0, p1, arrowstyle="-|>",
            mutation_scale=12,
            color="#8a5ac9", lw=1.8, zorder=10,
        ))

    dim_badge(ax, mid3, panel_y0 + 0.50,
              label="3", face="#c8aff0", edge="#8a5ac9",
              hash_count=3)
    panel_centers.append((mid3, panel_y0 + panel_h * 0.55))

    # =============================================================
    # Connectors — each panel up to the central invariant orb
    # =============================================================
    for (px, py) in panel_centers:
        # dashed golden connector
        ax.plot([px, ccx], [panel_y0 + panel_h + 0.05,
                            ccy - 0.9],
                color="#c97a10", lw=1.5, alpha=0.55,
                linestyle=(0, (4, 3)), zorder=2)
        # small amber "same-rule" tick badge at the top of each panel
        tb_x = px
        tb_y = panel_y0 + panel_h + 0.05
        for rr, a in [(0.28, 0.15), (0.18, 0.35)]:
            ax.add_patch(Circle((tb_x, tb_y), rr,
                                facecolor="#ffd24a",
                                edgecolor="none", alpha=a, zorder=3))
        ax.add_patch(Circle((tb_x, tb_y), 0.10,
                            facecolor="#fff1b0",
                            edgecolor="#c97a10", lw=1.4, zorder=4))

    # =============================================================
    # Bottom: dimension-axis ladder
    # =============================================================
    ax_y = 1.55
    ax_x0, ax_x1 = 1.1, 12.9
    ax.plot([ax_x0, ax_x1], [ax_y, ax_y],
            color="#1f3b57", lw=2.0, zorder=5)
    ax.annotate("",
                xy=(ax_x1, ax_y),
                xytext=(ax_x0, ax_y),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1f3b57", lw=1.8),
                zorder=5)

    # three ticks for d=1,2,3 aligned under each panel
    tick_xs = [panel_centers[0][0],
               panel_centers[1][0],
               panel_centers[2][0]]
    tick_colors = ["#1aa6c7", "#2fb27a", "#8a5ac9"]
    # α_R values for d=1,2,3 with m=2 (β=1): 1/(d+2) -> 1/3, 1/4, 1/5
    alpha_R_vals = [1 / 3, 1 / 4, 1 / 5]
    for tx, col, a_val in zip(tick_xs, tick_colors, alpha_R_vals):
        ax.plot([tx, tx], [ax_y - 0.25, ax_y + 0.25],
                color=col, lw=2.8, zorder=6,
                solid_capstyle="round")
        # tick badge with an α_R-proportional amber fill indicator
        # (smaller fill for smaller exponent → visual "tightening")
        bar_h = 0.45
        ax.add_patch(FancyBboxPatch(
            (tx - 0.15, ax_y - 0.22 - bar_h - 0.10),
            0.30, bar_h,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            facecolor="#eef0f3", edgecolor=col,
            lw=1.4, zorder=6,
        ))
        ax.add_patch(FancyBboxPatch(
            (tx - 0.15, ax_y - 0.22 - bar_h - 0.10),
            0.30, bar_h * a_val * 3,        # scale for visibility
            boxstyle="round,pad=0.02,rounding_size=0.06",
            facecolor="#ffb347", edgecolor="#c97a10",
            lw=1.2, zorder=7,
        ))

    # ---- framing ---------------------------------------------------
    ax.set_xlim(0, 14)
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
