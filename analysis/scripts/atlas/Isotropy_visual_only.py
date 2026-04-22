"""
Isotropy constraint — visual-only illustration.

Metaphor: a point of influence with equal reach in every direction.
  - Central glowing orb
  - Dense ring of equal-length radial arrows
  - Three concentric perfectly-circular wavefront rings
  - Two small corner badges showing struck-through directional arrows
    (no preferred axis)
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch, Polygon,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\Isotropy.png"


def build():
    fig, ax = plt.subplots(figsize=(10, 10), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 11, 0, 11], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 11, 1.6,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # =============================================================
    # Central glowing orb
    # =============================================================
    cx, cy = 5.5, 5.8
    core_R = 0.55

    # radial halo
    for rr, a in [(core_R * 3.2, 0.05),
                  (core_R * 2.4, 0.09),
                  (core_R * 1.8, 0.18),
                  (core_R * 1.4, 0.32)]:
        ax.add_patch(Circle((cx, cy), rr,
                            facecolor="#9fe6f3",
                            edgecolor="none", alpha=a, zorder=3))

    # body (radial shaded)
    for rr, col in [(core_R * 1.00, "#9fe6f3"),
                    (core_R * 0.85, "#6fd2e9"),
                    (core_R * 0.68, "#3fa6d0"),
                    (core_R * 0.50, "#2791c2"),
                    (core_R * 0.34, "#0f5e85")]:
        ax.add_patch(Circle((cx - 0.015 * (core_R - rr) / core_R,
                             cy + 0.015 * (core_R - rr) / core_R),
                            rr, facecolor=col,
                            edgecolor="none", zorder=7))
    # highlight
    ax.add_patch(Circle((cx - core_R * 0.32, cy + core_R * 0.32),
                        core_R * 0.26,
                        facecolor="white", alpha=0.80, zorder=9))
    # outline
    ax.add_patch(Circle((cx, cy), core_R,
                        facecolor="none", edgecolor="#0b4a68",
                        lw=2.0, zorder=8))

    # =============================================================
    # Concentric wavefront rings (perfectly circular — signature of isotropy)
    # =============================================================
    for R_ring, a, lw, style in [
        (1.70, 0.85, 2.6, "solid"),
        (2.55, 0.50, 2.2, (0, (8, 4))),
        (3.40, 0.30, 2.0, (0, (3, 3))),
    ]:
        for lw_h, ah in [(lw + 6, a * 0.18), (lw + 3, a * 0.35)]:
            ax.add_patch(Circle((cx, cy), R_ring,
                                facecolor="none",
                                edgecolor="#9fe6f3", lw=lw_h,
                                alpha=ah, zorder=4))
        ax.add_patch(Circle((cx, cy), R_ring,
                            facecolor="none",
                            edgecolor="#1aa6c7", lw=lw,
                            alpha=a, linestyle=style, zorder=5))

    # =============================================================
    # Radial arrows — EQUAL LENGTH in every direction
    # =============================================================
    n_arrows = 16
    arrow_r0 = core_R + 0.22
    arrow_r1 = 1.45
    for k in range(n_arrows):
        th = k * 2 * np.pi / n_arrows
        p0 = (cx + arrow_r0 * np.cos(th),
              cy + arrow_r0 * np.sin(th))
        p1 = (cx + arrow_r1 * np.cos(th),
              cy + arrow_r1 * np.sin(th))
        # soft glow
        for lw_h, a_ in [(6, 0.18), (3.5, 0.34)]:
            ax.plot([p0[0], p1[0]], [p0[1], p1[1]],
                    color="#9fe6f3", lw=lw_h, alpha=a_,
                    solid_capstyle="round", zorder=6)
        ax.add_patch(FancyArrowPatch(
            p0, p1,
            arrowstyle="-|>", mutation_scale=16,
            color="#1aa6c7", lw=2.4, zorder=7,
        ))
        # small tick at the arrow tip — emphasizes equal reach
        ax.add_patch(Circle(p1, 0.06,
                            facecolor="#1aa6c7",
                            edgecolor="white", lw=0.6,
                            alpha=0.92, zorder=8))

    # =============================================================
    # Rotation-symmetry indicator: faint circular arrow around the
    # outer wavefront suggesting "rotate — nothing changes"
    # =============================================================
    rot_R = 4.05
    th_arc = np.linspace(np.pi * 0.15, np.pi * 0.85, 80)
    arc_x = cx + rot_R * np.cos(th_arc)
    arc_y = cy + rot_R * np.sin(th_arc)
    for lw_h, a_ in [(7, 0.10), (4, 0.20)]:
        ax.plot(arc_x, arc_y, color="#c8aff0", lw=lw_h, alpha=a_,
                solid_capstyle="round", zorder=3)
    ax.plot(arc_x, arc_y, color="#6a3fb0", lw=2.0, alpha=0.80,
            solid_capstyle="round", zorder=4)
    # arrowhead at the end of the arc
    ax.annotate("",
                xy=(arc_x[-1], arc_y[-1]),
                xytext=(arc_x[-4], arc_y[-4]),
                arrowprops=dict(arrowstyle="-|>",
                                color="#6a3fb0", lw=2.4),
                zorder=5)
    # mirror the rotation arc below (second half)
    th_arc2 = np.linspace(np.pi * 1.15, np.pi * 1.85, 80)
    arc_x2 = cx + rot_R * np.cos(th_arc2)
    arc_y2 = cy + rot_R * np.sin(th_arc2)
    for lw_h, a_ in [(7, 0.10), (4, 0.20)]:
        ax.plot(arc_x2, arc_y2, color="#c8aff0", lw=lw_h, alpha=a_,
                solid_capstyle="round", zorder=3)
    ax.plot(arc_x2, arc_y2, color="#6a3fb0", lw=2.0, alpha=0.80,
            solid_capstyle="round", zorder=4)
    ax.annotate("",
                xy=(arc_x2[-1], arc_y2[-1]),
                xytext=(arc_x2[-4], arc_y2[-4]),
                arrowprops=dict(arrowstyle="-|>",
                                color="#6a3fb0", lw=2.4),
                zorder=5)

    # =============================================================
    # "No preferred direction" corner badges (upper-right: a
    # directional arrow with a red slash)
    # =============================================================
    def no_direction_badge(bx, by, ang_deg):
        for rr, a in [(0.58, 0.08), (0.44, 0.16)]:
            ax.add_patch(Circle((bx, by), rr,
                                facecolor="#c23b3b",
                                edgecolor="none", alpha=a, zorder=9))
        ax.add_patch(Circle((bx, by), 0.38,
                            facecolor="white",
                            edgecolor="#c23b3b", lw=2.4, zorder=10))
        # directional arrow inside
        ang = np.deg2rad(ang_deg)
        L = 0.30
        p0 = (bx - L * np.cos(ang), by - L * np.sin(ang))
        p1 = (bx + L * np.cos(ang), by + L * np.sin(ang))
        ax.add_patch(FancyArrowPatch(
            p0, p1, arrowstyle="-|>",
            mutation_scale=14,
            color="#5b6b80", lw=2.2, zorder=11,
        ))
        # red slash
        ax.plot([bx - 0.28, bx + 0.28],
                [by + 0.28, by - 0.28],
                color="#c23b3b", lw=3.0,
                solid_capstyle="round", zorder=12)

    no_direction_badge(9.8, 9.6, ang_deg=10)
    no_direction_badge(1.2, 9.6, ang_deg=140)

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
