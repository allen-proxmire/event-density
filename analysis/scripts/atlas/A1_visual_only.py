"""
A1 Non-negativity — visual-only illustration (no text/equations baked in).

Metaphor: a rain gauge with a glowing zero floor.
  - rain falls from above and accumulates
  - a bright, impenetrable floor marks zero
  - a dimmed "forbidden" region below reinforces the ≥ 0 constraint

Text is intentionally absent; the user overlays captions and equations
in the slide layer.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Ellipse, Circle, PathPatch,
)
from matplotlib.path import Path

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\A1_non_negativity.png"


def draw_cloud(ax, cx, cy, scale=1.0, alpha=0.85):
    """Soft stylized cloud out of stacked ellipses."""
    lobes = [
        (-0.55, 0.00, 0.55, 0.42),
        (-0.15, 0.18, 0.60, 0.50),
        ( 0.30, 0.10, 0.55, 0.45),
        ( 0.55, -0.05, 0.45, 0.38),
        (-0.30, -0.10, 0.50, 0.38),
    ]
    for dx, dy, w, h in lobes:
        ax.add_patch(Ellipse(
            (cx + dx * scale, cy + dy * scale),
            w * scale, h * scale,
            facecolor="white", edgecolor="#c9d7e6",
            lw=1.2, alpha=alpha, zorder=2,
        ))
    # subtle shadow
    for dx, dy, w, h in lobes[:3]:
        ax.add_patch(Ellipse(
            (cx + dx * scale, cy + dy * scale - 0.08 * scale),
            w * scale * 0.9, h * scale * 0.5,
            facecolor="#b9c9d8", edgecolor="none",
            alpha=0.18 * alpha, zorder=1,
        ))


def build():
    fig, ax = plt.subplots(figsize=(9, 10), dpi=220)

    # ---- background: soft sky gradient -----------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(
        grad, extent=[0, 10, 0, 11], aspect="auto",
        cmap="Blues_r", alpha=0.28, zorder=0,
    )
    # warm floor glow underlay
    ax.add_patch(Rectangle(
        (0, 0), 10, 2.4,
        facecolor="#fff4d6", alpha=0.55, zorder=0,
    ))

    # ---- clouds ----------------------------------------------------
    draw_cloud(ax, 2.1, 9.5, scale=0.95, alpha=0.95)
    draw_cloud(ax, 7.6, 9.7, scale=1.05, alpha=0.95)
    draw_cloud(ax, 5.0, 10.1, scale=0.80, alpha=0.9)

    # ---- rain ------------------------------------------------------
    rng = np.random.default_rng(3)
    for _ in range(70):
        x = rng.uniform(1.2, 8.8)
        y = rng.uniform(5.8, 9.2)
        length = rng.uniform(0.18, 0.38)
        ax.plot(
            [x, x - 0.05], [y, y - length],
            color="#4f9fcf", lw=1.8, alpha=0.65,
            solid_capstyle="round", zorder=3,
        )

    # teardrop-shaped drops in-flight heading into gauge
    for x, y in [(4.5, 7.2), (5.2, 6.6), (4.8, 5.9),
                 (5.5, 7.6), (4.3, 5.3), (5.0, 8.1)]:
        ax.add_patch(Ellipse(
            (x, y), 0.13, 0.24,
            facecolor="#4f9fcf", edgecolor="#25506d",
            lw=0.8, alpha=0.92, zorder=4,
        ))
        ax.add_patch(Ellipse(
            (x - 0.035, y + 0.05), 0.035, 0.08,
            facecolor="white", alpha=0.75, zorder=5,
        ))

    # ---- gauge geometry -------------------------------------------
    gx, gy, gw, gh = 3.75, 2.1, 2.5, 5.3
    floor_y = gy + 0.08

    # glass body (subtle cyan) with rounded bottom
    body = FancyBboxPatch(
        (gx, gy), gw, gh,
        boxstyle="round,pad=0.02,rounding_size=0.26",
        facecolor="#e9f3fa", edgecolor="none",
        alpha=0.55, zorder=2,
    )
    ax.add_patch(body)

    # ---- liquid fill (gradient stack) -----------------------------
    liquid_h = 3.0
    n = 90
    for i in range(n):
        frac = i / n
        y0 = floor_y + frac * liquid_h
        c = plt.cm.GnBu(0.40 + 0.42 * (1 - frac))
        ax.add_patch(Rectangle(
            (gx + 0.12, y0), gw - 0.24, liquid_h / n + 0.02,
            facecolor=c, edgecolor="none", alpha=0.92, zorder=3,
        ))

    # meniscus (curved surface)
    men_y = floor_y + liquid_h
    ax.add_patch(Ellipse(
        (gx + gw / 2, men_y), gw - 0.24, 0.20,
        facecolor="#7ec3de", edgecolor="#3a7fa0",
        lw=1.4, alpha=0.95, zorder=4,
    ))
    # ripple highlights
    for rx, rr in [(gx + 0.95, 0.17), (gx + 1.55, 0.12),
                   (gx + 1.2, 0.22)]:
        ax.add_patch(Ellipse(
            (rx, men_y + 0.015), rr, rr * 0.28,
            facecolor="none", edgecolor="white",
            lw=1.5, alpha=0.8, zorder=5,
        ))

    # glass highlight (left)
    ax.add_patch(Rectangle(
        (gx + 0.18, gy + 0.45), 0.22, gh - 0.9,
        facecolor="white", alpha=0.35, zorder=5,
    ))
    # glass highlight (thin right)
    ax.add_patch(Rectangle(
        (gx + gw - 0.30, gy + 1.2), 0.08, gh - 2.2,
        facecolor="white", alpha=0.22, zorder=5,
    ))

    # gauge outline
    outline = FancyBboxPatch(
        (gx, gy), gw, gh,
        boxstyle="round,pad=0.02,rounding_size=0.26",
        facecolor="none", edgecolor="#1f3b57",
        lw=3.2, zorder=6,
    )
    ax.add_patch(outline)

    # tick marks, right side
    for i in range(1, 9):
        ty = gy + i * (gh / 9)
        long = (i % 2 == 0)
        xend = gx + gw + (0.30 if long else 0.18)
        lw = 2.6 if long else 1.8
        ax.plot(
            [gx + gw - 0.02, xend], [ty, ty],
            color="#1f3b57", lw=lw, zorder=7,
            solid_capstyle="round",
        )

    # ---- GLOWING ZERO FLOOR ---------------------------------------
    for glow_h, a in [(0.60, 0.06), (0.42, 0.10),
                      (0.28, 0.18), (0.18, 0.30), (0.10, 0.55)]:
        ax.add_patch(Rectangle(
            (gx - 0.8, floor_y - glow_h / 2),
            gw + 1.6, glow_h,
            facecolor="#ffc23a", edgecolor="none",
            alpha=a, zorder=6,
        ))
    # bright core line
    ax.plot(
        [gx - 0.45, gx + gw + 0.45],
        [floor_y, floor_y],
        color="#ff9f1a", lw=6, zorder=9,
        solid_capstyle="round",
    )
    ax.plot(
        [gx - 0.45, gx + gw + 0.45],
        [floor_y, floor_y],
        color="#fff1b0", lw=2.5, zorder=10,
        solid_capstyle="round",
    )

    # ---- solid pedestal (impenetrable base) -----------------------
    base = FancyBboxPatch(
        (gx - 0.6, gy - 0.95), gw + 1.2, 1.05,
        boxstyle="round,pad=0.02,rounding_size=0.12",
        facecolor="#2f4d6b", edgecolor="#142536",
        lw=2.2, zorder=7,
    )
    ax.add_patch(base)
    # base top shine
    ax.add_patch(Rectangle(
        (gx - 0.45, gy - 0.75), gw + 0.9, 0.12,
        facecolor="#6b8aa8", alpha=0.7, zorder=8,
    ))
    # base bottom shadow
    ax.add_patch(Rectangle(
        (gx - 0.45, gy - 0.05), gw + 0.9, 0.05,
        facecolor="#0b1a27", alpha=0.35, zorder=8,
    ))

    # ---- "forbidden" zone below: faded downward arrows + ghost drop
    for x in np.linspace(gx + 0.35, gx + gw - 0.35, 4):
        ax.annotate(
            "", xy=(x, gy - 0.55), xytext=(x, gy - 0.08),
            arrowprops=dict(
                arrowstyle="->", color="#c23b3b",
                lw=1.6, alpha=0.0,
            ),
            zorder=6,
        )

    # red circle-slash below the pedestal, off to the side, to signal "no"
    no_x, no_y = gx + gw + 1.05, gy - 0.42
    ax.add_patch(Circle(
        (no_x, no_y), 0.30,
        facecolor="white", edgecolor="#c23b3b",
        lw=3.2, alpha=0.95, zorder=11,
    ))
    ax.plot(
        [no_x - 0.21, no_x + 0.21],
        [no_y + 0.21, no_y - 0.21],
        color="#c23b3b", lw=3.2, zorder=12,
        solid_capstyle="round",
    )
    # tiny downward arrow inside the red circle to imply "negative not allowed"
    ax.annotate(
        "", xy=(no_x, no_y - 0.12), xytext=(no_x, no_y + 0.12),
        arrowprops=dict(
            arrowstyle="->", color="#c23b3b",
            lw=2.0,
        ),
        zorder=13,
    )

    # ---- framing ---------------------------------------------------
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 11)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.tight_layout()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    plt.savefig(
        OUT, dpi=220, bbox_inches="tight",
        facecolor="#f7fbfe", edgecolor="none",
    )
    plt.close(fig)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    build()
