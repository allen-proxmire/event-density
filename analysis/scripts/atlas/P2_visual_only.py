"""
P2 Channel Complementarity — visual-only illustration.

Metaphor: two communicating vessels whose total fill is fixed at 1.
  - Left vessel (cyan)  : the D channel (mobility / F[p])
  - Right vessel (amber): the H channel (participation / ν)
  - A thick linking tube at the bottom conserves the total.
  - Above the vessels, a unit-length bar is split cyan / amber at
    exactly the same ratio as the fills — visually asserting D + H = 1.

Glowing zero baseline carried over from A1–A4 for visual continuity.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, Ellipse, FancyArrowPatch, Polygon,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\P2_channel_complementarity.png"


def build():
    fig, ax = plt.subplots(figsize=(11, 10), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 12, 0, 11], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 12, 1.9,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # ---- geometry --------------------------------------------------
    # We choose a representative split: D = 0.62, H = 0.38 (sums to 1)
    D_frac = 0.62
    H_frac = 1.0 - D_frac

    # Vessel pair
    base_y = 2.05
    floor_y = base_y + 0.10       # glowing zero floor inside vessels
    vh = 4.6                      # vessel interior height
    vw = 1.95                     # vessel interior width
    gap = 2.0                     # horizontal gap between vessels
    total_w = 2 * vw + gap
    start_x = (12 - total_w) / 2
    vx_L = start_x
    vx_R = start_x + vw + gap

    def draw_vessel(x0, fill_frac, fill_cmap, outline_color,
                    glow_color, tick_color, vlabel_color):
        # body
        body = FancyBboxPatch(
            (x0, base_y), vw, vh,
            boxstyle="round,pad=0.02,rounding_size=0.22",
            facecolor="#eaf4fb", edgecolor="none",
            alpha=0.55, zorder=2,
        )
        ax.add_patch(body)

        # fill
        fill_h = fill_frac * (vh - 0.25)
        n = 80
        for i in range(n):
            frac = i / n
            y0 = floor_y + frac * fill_h
            c = fill_cmap(0.40 + 0.40 * (1 - frac))
            ax.add_patch(Rectangle(
                (x0 + 0.10, y0), vw - 0.20, fill_h / n + 0.02,
                facecolor=c, edgecolor="none", alpha=0.92, zorder=3,
            ))
        # meniscus
        ax.add_patch(Ellipse(
            (x0 + vw / 2, floor_y + fill_h),
            vw - 0.20, 0.18,
            facecolor=glow_color, edgecolor=vlabel_color,
            lw=1.4, alpha=0.92, zorder=4,
        ))
        # highlights
        ax.add_patch(Rectangle(
            (x0 + 0.14, base_y + 0.38), 0.18, vh - 0.75,
            facecolor="white", alpha=0.35, zorder=5,
        ))
        ax.add_patch(Rectangle(
            (x0 + vw - 0.26, base_y + 0.9), 0.07, vh - 1.6,
            facecolor="white", alpha=0.22, zorder=5,
        ))
        # outline
        ax.add_patch(FancyBboxPatch(
            (x0, base_y), vw, vh,
            boxstyle="round,pad=0.02,rounding_size=0.22",
            facecolor="none", edgecolor=outline_color,
            lw=3.0, zorder=6,
        ))
        # ticks (inside right edge)
        for i in range(1, 11):
            ty = base_y + 0.10 + (i / 10) * (vh - 0.25)
            long = (i % 2 == 0)
            tend = x0 + vw + (0.28 if long else 0.17)
            tlw = 2.5 if long else 1.6
            ax.plot([x0 + vw - 0.02, tend], [ty, ty],
                    color=tick_color, lw=tlw, zorder=7,
                    solid_capstyle="round")
        return fill_h

    # left (D) — cyan
    fh_L = draw_vessel(vx_L, D_frac, plt.cm.GnBu,
                       outline_color="#1f3b57",
                       glow_color="#7ec3de", tick_color="#1f3b57",
                       vlabel_color="#1a4e68")
    # right (H) — amber
    fh_R = draw_vessel(vx_R, H_frac, plt.cm.YlOrBr,
                       outline_color="#7a4a0a",
                       glow_color="#ffc470", tick_color="#7a4a0a",
                       vlabel_color="#7a4a0a")

    # ---- connecting pipe (communicating vessels) ------------------
    pipe_y = base_y - 0.55
    pipe_h = 0.55
    # vertical stubs down from each vessel floor
    for (x_cx, fill_col) in [(vx_L + vw / 2, "#3fa6d0"),
                             (vx_R + vw / 2, "#d69a1a")]:
        ax.add_patch(Rectangle(
            (x_cx - 0.22, base_y - 0.55), 0.44, 0.65,
            facecolor="#cfd8e0", edgecolor="#2f4d6b", lw=2.2, zorder=2,
        ))
    # horizontal connecting tube
    tube_x0 = vx_L + vw / 2 - 0.22
    tube_x1 = vx_R + vw / 2 + 0.22
    ax.add_patch(FancyBboxPatch(
        (tube_x0, pipe_y - pipe_h),
        tube_x1 - tube_x0, pipe_h,
        boxstyle="round,pad=0.02,rounding_size=0.12",
        facecolor="#cfd8e0", edgecolor="#2f4d6b", lw=2.4, zorder=2,
    ))
    # fluid inside connecting tube — a gradient mixing cyan→amber
    ngrad = 80
    for i in range(ngrad):
        frac = i / ngrad
        # color mix
        cR = np.array([0.247, 0.651, 0.816])   # cyan
        cA = np.array([0.839, 0.604, 0.102])   # amber
        col = (1 - frac) * cR + frac * cA
        x0 = tube_x0 + 0.06 + frac * (tube_x1 - tube_x0 - 0.12)
        w = (tube_x1 - tube_x0 - 0.12) / ngrad + 0.02
        ax.add_patch(Rectangle(
            (x0, pipe_y - pipe_h + 0.08), w, pipe_h - 0.20,
            facecolor=col, edgecolor="none", alpha=0.9, zorder=3,
        ))
    # small arrow on tube pointing toward the lower-fill side (H)
    arrow = FancyArrowPatch(
        (tube_x0 + 0.5, pipe_y - pipe_h / 2),
        (tube_x1 - 0.5, pipe_y - pipe_h / 2),
        arrowstyle="-|>", mutation_scale=18,
        color="#2f4d6b", lw=2.2, zorder=6,
    )
    ax.add_patch(arrow)

    # ---- pedestal --------------------------------------------------
    ped_x0 = vx_L - 0.8
    ped_x1 = vx_R + vw + 0.8
    ped_w = ped_x1 - ped_x0
    ped_y = base_y - 1.25
    ped_h = 0.55
    ax.add_patch(FancyBboxPatch(
        (ped_x0, ped_y), ped_w, ped_h,
        boxstyle="round,pad=0.02,rounding_size=0.12",
        facecolor="#2f4d6b", edgecolor="#142536", lw=2.0, zorder=7,
    ))
    ax.add_patch(Rectangle(
        (ped_x0 + 0.15, ped_y + ped_h - 0.12), ped_w - 0.30, 0.08,
        facecolor="#6b8aa8", alpha=0.7, zorder=8,
    ))

    # glowing zero floor spanning both vessels
    floor_line_y = floor_y
    for glow_h, a in [(0.60, 0.06), (0.40, 0.12),
                      (0.24, 0.22), (0.14, 0.38), (0.08, 0.65)]:
        ax.add_patch(Rectangle(
            (ped_x0 + 0.1, floor_line_y - glow_h / 2),
            ped_w - 0.2, glow_h,
            facecolor="#ffc23a", edgecolor="none", alpha=a, zorder=1,
        ))
    ax.plot([ped_x0 + 0.2, ped_x1 - 0.2],
            [floor_line_y, floor_line_y],
            color="#ff9f1a", lw=5.5, zorder=8, solid_capstyle="round")
    ax.plot([ped_x0 + 0.2, ped_x1 - 0.2],
            [floor_line_y, floor_line_y],
            color="#fff1b0", lw=2.2, zorder=9, solid_capstyle="round")

    # ---- TOP bar: "D + H = 1" unit-length indicator ---------------
    bar_y = base_y + vh + 0.95
    bar_x0 = vx_L
    bar_x1 = vx_R + vw
    bar_w = bar_x1 - bar_x0
    bar_h = 0.55

    # shadow
    ax.add_patch(FancyBboxPatch(
        (bar_x0 + 0.06, bar_y - 0.10), bar_w, bar_h,
        boxstyle="round,pad=0.02,rounding_size=0.20",
        facecolor="#00000014", edgecolor="none", zorder=4,
    ))

    # the cyan D segment
    D_w = D_frac * bar_w
    # draw as gradient-filled rounded-corner rectangle on the left.
    # Build via many thin vertical slices, then overlay a rounded mask.
    n = 120
    for i in range(n):
        frac = i / n
        c = plt.cm.GnBu(0.45 + 0.35 * (1 - frac))
        x0 = bar_x0 + i * D_w / n
        ax.add_patch(Rectangle(
            (x0, bar_y), D_w / n + 0.02, bar_h,
            facecolor=c, edgecolor="none", alpha=0.95, zorder=5,
        ))
    # amber H segment
    H_w = H_frac * bar_w
    for i in range(n):
        frac = i / n
        c = plt.cm.YlOrBr(0.30 + 0.40 * (1 - frac))
        x0 = bar_x0 + D_w + i * H_w / n
        ax.add_patch(Rectangle(
            (x0, bar_y), H_w / n + 0.02, bar_h,
            facecolor=c, edgecolor="none", alpha=0.95, zorder=5,
        ))
    # bar outline (rounded)
    ax.add_patch(FancyBboxPatch(
        (bar_x0, bar_y), bar_w, bar_h,
        boxstyle="round,pad=0.02,rounding_size=0.20",
        facecolor="none", edgecolor="#1f3b57", lw=2.6, zorder=6,
    ))
    # ticks 0 and 1 at the bar endpoints
    for tx, lbl in [(bar_x0, "0"), (bar_x1, "1")]:
        ax.plot([tx, tx], [bar_y - 0.08, bar_y - 0.22],
                color="#1f3b57", lw=2.4, zorder=7)
        ax.add_patch(Circle((tx, bar_y - 0.32), 0.11,
                            facecolor="white", edgecolor="#1f3b57",
                            lw=1.6, zorder=8))
    # knob / slider where D meets H
    knob_x = bar_x0 + D_w
    ax.plot([knob_x, knob_x], [bar_y - 0.06, bar_y + bar_h + 0.06],
            color="#1f3b57", lw=1.4, alpha=0.5, zorder=6)
    for rr, a in [(0.30, 0.15), (0.22, 0.30), (0.15, 0.60)]:
        ax.add_patch(Circle((knob_x, bar_y + bar_h / 2), rr,
                            facecolor="#ffd24a", edgecolor="none",
                            alpha=a, zorder=7))
    ax.add_patch(Circle((knob_x, bar_y + bar_h / 2), 0.18,
                        facecolor="white", edgecolor="#1f3b57",
                        lw=2.0, zorder=9))
    ax.add_patch(Circle((knob_x, bar_y + bar_h / 2), 0.07,
                        facecolor="#1f3b57", edgecolor="none",
                        zorder=10))

    # small arrow pair on the slider (left-right) to suggest the knob moves
    ax.annotate("", xy=(knob_x - 0.55, bar_y + bar_h / 2),
                xytext=(knob_x - 0.15, bar_y + bar_h / 2),
                arrowprops=dict(arrowstyle="-|>", color="#1f3b57",
                                lw=2.0),
                zorder=11)
    ax.annotate("", xy=(knob_x + 0.55, bar_y + bar_h / 2),
                xytext=(knob_x + 0.15, bar_y + bar_h / 2),
                arrowprops=dict(arrowstyle="-|>", color="#1f3b57",
                                lw=2.0),
                zorder=11)

    # ---- vertical connectors from bar segments to vessels --------
    # cyan connector
    ax.plot([bar_x0 + D_w / 2, vx_L + vw / 2],
            [bar_y, base_y + vh + 0.05],
            color="#2a7fa3", lw=1.6, alpha=0.35,
            linestyle=(0, (3, 3)), zorder=4)
    # amber connector
    ax.plot([bar_x0 + D_w + H_w / 2, vx_R + vw / 2],
            [bar_y, base_y + vh + 0.05],
            color="#b57b12", lw=1.6, alpha=0.35,
            linestyle=(0, (3, 3)), zorder=4)

    # ---- complementarity glyph ("⇄") bottom-center ---------------
    gx_, gy_ = 6.0, 0.95
    ax.add_patch(Circle((gx_, gy_), 0.45,
                        facecolor="#f4f7fb", edgecolor="#1f3b57",
                        lw=2.4, zorder=10))
    ax.annotate("", xy=(gx_ + 0.28, gy_ + 0.08),
                xytext=(gx_ - 0.28, gy_ + 0.08),
                arrowprops=dict(arrowstyle="-|>", color="#2a7fa3",
                                lw=2.4), zorder=11)
    ax.annotate("", xy=(gx_ - 0.28, gy_ - 0.08),
                xytext=(gx_ + 0.28, gy_ - 0.08),
                arrowprops=dict(arrowstyle="-|>", color="#b57b12",
                                lw=2.4), zorder=11)

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
