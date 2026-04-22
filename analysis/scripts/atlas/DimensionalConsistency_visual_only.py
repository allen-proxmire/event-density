"""
Dimensional Consistency constraint — visual-only illustration.

Metaphor: a classical balance scale.  Both pans hold dimension-
tokens (stylized unit cubes); the beam is perfectly level because
every term in the ED equation carries the same units.

Composition:
  • Golden fulcrum triangle at center on a short pedestal.
  • A horizontal beam, perfectly level, with small dimension-tick
    marks along it.
  • Two round pans hanging from the beam ends by short chains.
  • Each pan holds three isometric-drawn UNIT CUBES of matching
    edge lengths (the different terms of the PDE rendered as
    dimensional tokens).  Each cube carries a tiny color-coded
    tag matching its ED role (cyan, amber, coral).
  • A faint ruler / tick grid at the bottom shows consistent
    scaling across the composition.
  • A golden crown above the fulcrum signals "universal invariant."
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, Ellipse, FancyArrowPatch,
    Polygon,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\DimensionalConsistency.png"


def unit_cube(ax, cx, cy, s, face_col, top_col, right_col,
              edge="#1f3b57", tag_col=None, zorder=10):
    """Draw an isometric unit cube centered at (cx, cy) with side s.
    Optionally place a tiny colored tag circle on top of the cube.
    """
    dx = 0.40 * s
    dy = 0.30 * s
    # front face corners
    F_bl = (cx - s / 2, cy - s / 2)
    F_br = (cx + s / 2, cy - s / 2)
    F_tr = (cx + s / 2, cy + s / 2)
    F_tl = (cx - s / 2, cy + s / 2)
    # back-shifted
    B_bl = (F_bl[0] + dx, F_bl[1] + dy)
    B_br = (F_br[0] + dx, F_br[1] + dy)
    B_tr = (F_tr[0] + dx, F_tr[1] + dy)
    B_tl = (F_tl[0] + dx, F_tl[1] + dy)
    # top face
    ax.add_patch(Polygon([F_tl, F_tr, B_tr, B_tl],
                         closed=True, facecolor=top_col,
                         edgecolor=edge, lw=1.8, zorder=zorder))
    # right face
    ax.add_patch(Polygon([F_br, F_tr, B_tr, B_br],
                         closed=True, facecolor=right_col,
                         edgecolor=edge, lw=1.8, zorder=zorder))
    # front face
    ax.add_patch(Polygon([F_bl, F_br, F_tr, F_tl],
                         closed=True, facecolor=face_col,
                         edgecolor=edge, lw=2.0,
                         zorder=zorder + 1))
    # matching edge-length tick marks on the three visible edges
    tick_col = "#fff1b0"
    # front-bottom tick (middle of the front-bottom edge)
    mx_fb = (F_bl[0] + F_br[0]) / 2
    my_fb = F_bl[1]
    ax.plot([mx_fb, mx_fb], [my_fb - 0.04, my_fb + 0.04],
            color=tick_col, lw=2.0, zorder=zorder + 2,
            solid_capstyle="round")
    # right-side middle tick
    mx_rs = (F_br[0] + F_tr[0]) / 2
    my_rs = (F_br[1] + F_tr[1]) / 2
    ax.plot([mx_rs - 0.04, mx_rs + 0.04],
            [my_rs, my_rs],
            color=tick_col, lw=2.0, zorder=zorder + 2,
            solid_capstyle="round")
    # top-middle tick (into depth)
    mx_tm = (F_tl[0] + B_tl[0]) / 2
    my_tm = (F_tl[1] + B_tl[1]) / 2
    ax.plot([mx_tm - 0.025, mx_tm + 0.025],
            [my_tm - 0.04, my_tm + 0.04],
            color=tick_col, lw=2.0, zorder=zorder + 2,
            solid_capstyle="round")

    # optional small color-coded tag circle on top face
    if tag_col is not None:
        tag_cx = (F_tl[0] + B_tr[0]) / 2
        tag_cy = (F_tl[1] + B_tr[1]) / 2
        ax.add_patch(Circle((tag_cx, tag_cy + 0.06 * s), 0.10 * s,
                            facecolor=tag_col, edgecolor="white",
                            lw=0.9, zorder=zorder + 3))


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
    # Fulcrum + pedestal
    # =============================================================
    fx_c = 7.0
    ped_w = 1.70
    ped_h = 0.90
    ped_y0 = 1.55

    # pedestal block
    ax.add_patch(FancyBboxPatch(
        (fx_c - ped_w / 2, ped_y0), ped_w, ped_h,
        boxstyle="round,pad=0.02,rounding_size=0.12",
        facecolor="#2f4d6b", edgecolor="#142536",
        lw=2.2, zorder=6,
    ))
    # pedestal shine
    ax.add_patch(Rectangle(
        (fx_c - ped_w / 2 + 0.15, ped_y0 + ped_h - 0.10),
        ped_w - 0.30, 0.08,
        facecolor="#6b8aa8", alpha=0.70, zorder=7,
    ))

    # fulcrum triangle (gold)
    tri_top_y = ped_y0 + ped_h + 1.75
    fulcrum = [(fx_c - 0.55, ped_y0 + ped_h),
               (fx_c + 0.55, ped_y0 + ped_h),
               (fx_c, tri_top_y)]
    # halo under fulcrum
    for pad, a in [(0.22, 0.08), (0.14, 0.16),
                   (0.08, 0.28)]:
        ax.add_patch(Polygon(
            [(fulcrum[0][0] - pad, fulcrum[0][1] - pad),
             (fulcrum[1][0] + pad, fulcrum[1][1] - pad),
             (fulcrum[2][0], fulcrum[2][1] + pad * 1.3)],
            closed=True, facecolor="#ffd24a",
            edgecolor="none", alpha=a, zorder=6,
        ))
    ax.add_patch(Polygon(fulcrum, closed=True,
                         facecolor="#ffd24a",
                         edgecolor="#c97a10", lw=2.6, zorder=8))
    # inner highlight line on the triangle
    ax.plot([fulcrum[0][0] + 0.12, fulcrum[2][0] - 0.06],
            [fulcrum[0][1] + 0.06, fulcrum[2][1] - 0.08],
            color="#fff1b0", lw=1.4, alpha=0.8,
            solid_capstyle="round", zorder=9)

    # =============================================================
    # Beam (perfectly level)
    # =============================================================
    beam_y = tri_top_y + 0.30
    beam_x0 = fx_c - 4.5
    beam_x1 = fx_c + 4.5

    # subtle shadow under beam
    ax.add_patch(FancyBboxPatch(
        (beam_x0 + 0.08, beam_y - 0.18 - 0.08),
        beam_x1 - beam_x0, 0.36,
        boxstyle="round,pad=0.02,rounding_size=0.12",
        facecolor="#00000014", edgecolor="none", zorder=8,
    ))
    # beam body
    ax.add_patch(FancyBboxPatch(
        (beam_x0, beam_y - 0.18),
        beam_x1 - beam_x0, 0.36,
        boxstyle="round,pad=0.02,rounding_size=0.14",
        facecolor="#d69a1a", edgecolor="#7a4a0a",
        lw=2.4, zorder=9,
    ))
    # beam highlight
    ax.add_patch(Rectangle(
        (beam_x0 + 0.20, beam_y + 0.05),
        beam_x1 - beam_x0 - 0.40, 0.06,
        facecolor="#fff1b0", alpha=0.85, zorder=10,
    ))
    # tick marks along the beam (dimension gradations)
    for tx in np.linspace(beam_x0 + 0.5, beam_x1 - 0.5, 11):
        ax.plot([tx, tx], [beam_y - 0.18, beam_y - 0.10],
                color="#7a4a0a", lw=1.2, alpha=0.85, zorder=11)
    # pivot pin on top of the fulcrum
    ax.add_patch(Circle((fx_c, beam_y), 0.12,
                        facecolor="#c97a10",
                        edgecolor="#7a4a0a", lw=1.4, zorder=11))

    # golden crown / tiny "invariant" indicator above the pivot
    crown_y = beam_y + 0.55
    for rr, a in [(0.32, 0.12), (0.22, 0.28)]:
        ax.add_patch(Circle((fx_c, crown_y), rr,
                            facecolor="#ffd24a",
                            edgecolor="none", alpha=a, zorder=10))
    ax.add_patch(Circle((fx_c, crown_y), 0.14,
                        facecolor="#fff1b0",
                        edgecolor="#c97a10", lw=1.6, zorder=11))
    # five-point star in the crown (match DimInv style)
    npts = 5
    sp = []
    for k in range(npts * 2):
        rr = 0.10 if k % 2 == 0 else 0.04
        th = np.pi / 2 + k * np.pi / npts
        sp.append((fx_c + rr * np.cos(th),
                   crown_y + rr * np.sin(th)))
    ax.add_patch(Polygon(sp, closed=True,
                         facecolor="#c97a10",
                         edgecolor="#7a4a0a", lw=0.9, zorder=12))

    # =============================================================
    # Chains hanging down from beam ends
    # =============================================================
    chain_len = 1.30
    pan_cy = beam_y - chain_len - 0.10
    for cx_end in [beam_x0 + 0.35, beam_x1 - 0.35]:
        # zigzag chain
        for k in range(5):
            y0_ = beam_y - 0.18 - k * (chain_len / 5)
            y1_ = beam_y - 0.18 - (k + 1) * (chain_len / 5)
            offset = 0.04 if k % 2 == 0 else -0.04
            ax.plot([cx_end, cx_end + offset],
                    [y0_, y1_],
                    color="#5b6b80", lw=1.8,
                    solid_capstyle="round", zorder=8)
        # small loop at the bottom
        ax.add_patch(Circle((cx_end, beam_y - 0.18 - chain_len),
                            0.10,
                            facecolor="#5b6b80",
                            edgecolor="#2f4d6b", lw=1.0,
                            zorder=9))

    # =============================================================
    # Two pans (left and right), each holding three matching cubes
    # =============================================================
    pan_R = 1.30
    left_cx = beam_x0 + 0.35
    right_cx = beam_x1 - 0.35
    pan_rim_y = beam_y - 0.18 - chain_len - 0.10
    # each pan top is an ellipse to look like a dish

    def draw_pan(cx_pan, cy_pan):
        # halo under pan
        for pad, a in [(0.25, 0.08), (0.14, 0.16)]:
            ax.add_patch(Ellipse((cx_pan, cy_pan - 0.15),
                                 2 * (pan_R + pad), 0.5 + pad * 2,
                                 facecolor="#00000014",
                                 edgecolor="none", alpha=a, zorder=6))
        # pan body (shallow bowl)
        ax.add_patch(Ellipse((cx_pan, cy_pan),
                             2 * pan_R, 0.45,
                             facecolor="#c9d4e0",
                             edgecolor="#1f3b57", lw=2.2, zorder=10))
        # inner rim highlight
        ax.add_patch(Ellipse((cx_pan, cy_pan + 0.05),
                             2 * (pan_R - 0.08), 0.30,
                             facecolor="none",
                             edgecolor="#8aa4c0", lw=1.0,
                             alpha=0.7, zorder=11))
        # pan suspender rod (from chain bottom down to pan center)
        ax.plot([cx_pan, cx_pan],
                [cy_pan + 0.15, pan_rim_y + 0.05],
                color="#2f4d6b", lw=1.6, zorder=8)

    draw_pan(left_cx, pan_rim_y - 0.20)
    draw_pan(right_cx, pan_rim_y - 0.20)

    # ---- place three cubes on each pan (matching dimensions) ----
    cube_size = 0.55
    cube_tags = [
        # (face, top, right, tag) — tags match ED channel colors
        ("#e6f4fa", "#c8dfec", "#8fc0d6", "#1aa6c7"),  # cyan  (mobility)
        ("#fff1d8", "#ffd98a", "#ffb347", "#c97a10"),  # amber (penalty)
        ("#ffe4d0", "#ffc4a0", "#f49470", "#c94419"),  # coral (participation)
    ]

    def place_cubes(cx_pan, pan_top_y):
        # 3 cubes stacked loosely on the pan top
        positions = [
            (cx_pan - 0.65, pan_top_y + cube_size / 2),
            (cx_pan + 0.65, pan_top_y + cube_size / 2),
            (cx_pan, pan_top_y + cube_size / 2 + cube_size * 0.85),
        ]
        for (px, py), (face, top, right, tag) in zip(positions, cube_tags):
            unit_cube(ax, px, py, cube_size,
                      face_col=face, top_col=top, right_col=right,
                      edge="#1f3b57", tag_col=tag, zorder=12)

    place_cubes(left_cx, pan_rim_y - 0.20 + 0.18)
    place_cubes(right_cx, pan_rim_y - 0.20 + 0.18)

    # =============================================================
    # Equality glyph below the fulcrum (a golden "=" sign)
    # =============================================================
    eq_x, eq_y = fx_c, ped_y0 - 0.40
    for rr, a in [(0.34, 0.12), (0.24, 0.28)]:
        ax.add_patch(Circle((eq_x, eq_y), rr,
                            facecolor="#ffd24a",
                            edgecolor="none", alpha=a, zorder=6))
    ax.add_patch(Circle((eq_x, eq_y), 0.22,
                        facecolor="white", edgecolor="#c97a10",
                        lw=2.2, zorder=7))
    ax.plot([eq_x - 0.12, eq_x + 0.12],
            [eq_y + 0.06, eq_y + 0.06],
            color="#c97a10", lw=2.6,
            solid_capstyle="round", zorder=8)
    ax.plot([eq_x - 0.12, eq_x + 0.12],
            [eq_y - 0.06, eq_y - 0.06],
            color="#c97a10", lw=2.6,
            solid_capstyle="round", zorder=8)

    # =============================================================
    # Bottom ruler / tick grid — reinforces consistent scaling
    # =============================================================
    ruler_y = 1.05
    ax.plot([0.8, 13.2], [ruler_y, ruler_y],
            color="#1f3b57", lw=1.6, alpha=0.80, zorder=4)
    for i, tx in enumerate(np.linspace(0.8, 13.2, 13)):
        long = (i % 2 == 0)
        th = 0.18 if long else 0.10
        ax.plot([tx, tx], [ruler_y - th, ruler_y + th],
                color="#1f3b57", lw=1.4 if long else 1.0,
                zorder=5, solid_capstyle="round")

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
