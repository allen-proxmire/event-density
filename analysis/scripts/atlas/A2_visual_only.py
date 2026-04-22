"""
A2 Null baseline — visual-only illustration (no text/equations baked in).

Metaphor: the SAME rain gauge as A1, but empty.  No rain, no liquid.
The glowing zero floor is still there — now unambiguously read from
below the empty interior.  A single "0" vibe is conveyed by a
pulsing halo around the floor line.

Text is intentionally absent; the user overlays captions in the slide
layer.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Ellipse, Circle,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\A2_null_baseline.png"


def build():
    fig, ax = plt.subplots(figsize=(9, 10), dpi=220)

    # ---- background: calm clear sky (lighter than A1 stormy sky) ---
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(
        grad, extent=[0, 10, 0, 11], aspect="auto",
        cmap="Blues_r", alpha=0.18, zorder=0,
    )
    # warm floor glow underlay (same palette as A1 for continuity)
    ax.add_patch(Rectangle(
        (0, 0), 10, 2.4,
        facecolor="#fff4d6", alpha=0.55, zorder=0,
    ))

    # ---- faint sun / empty-sky indicator (no clouds, no rain) ------
    for r, a in [(1.05, 0.08), (0.85, 0.12), (0.65, 0.18), (0.48, 0.28)]:
        ax.add_patch(Circle(
            (8.3, 9.4), r,
            facecolor="#ffe48a", edgecolor="none", alpha=a, zorder=1,
        ))
    ax.add_patch(Circle(
        (8.3, 9.4), 0.35,
        facecolor="#ffd04a", edgecolor="#e6a800", lw=1.2,
        alpha=0.95, zorder=2,
    ))

    # ---- gauge geometry (identical to A1) -------------------------
    gx, gy, gw, gh = 3.75, 2.1, 2.5, 5.3
    floor_y = gy + 0.08

    # glass body (subtle cyan)
    body = FancyBboxPatch(
        (gx, gy), gw, gh,
        boxstyle="round,pad=0.02,rounding_size=0.26",
        facecolor="#eaf4fb", edgecolor="none",
        alpha=0.60, zorder=2,
    )
    ax.add_patch(body)

    # ---- EMPTY INTERIOR --------------------------------------------
    # A faint vertical gradient inside the glass to suggest air / emptiness
    for i in range(60):
        frac = i / 60
        y0 = floor_y + frac * (gh - 0.15)
        c = (0.93 + 0.03 * frac, 0.96 + 0.02 * frac, 0.99, 0.14 * (1 - frac))
        ax.add_patch(Rectangle(
            (gx + 0.12, y0), gw - 0.24, (gh - 0.15) / 60 + 0.01,
            facecolor=c, edgecolor="none", zorder=3,
        ))

    # A few lonely dust motes to emphasize "there's nothing in here"
    rng = np.random.default_rng(11)
    for _ in range(9):
        x = rng.uniform(gx + 0.25, gx + gw - 0.25)
        y = rng.uniform(floor_y + 0.4, gy + gh - 0.4)
        r = rng.uniform(0.012, 0.022)
        ax.add_patch(Circle(
            (x, y), r,
            facecolor="#9fb4c6", edgecolor="none", alpha=0.55, zorder=4,
        ))

    # glass highlights (left + thin right) - same as A1
    ax.add_patch(Rectangle(
        (gx + 0.18, gy + 0.45), 0.22, gh - 0.9,
        facecolor="white", alpha=0.38, zorder=5,
    ))
    ax.add_patch(Rectangle(
        (gx + gw - 0.30, gy + 1.2), 0.08, gh - 2.2,
        facecolor="white", alpha=0.25, zorder=5,
    ))

    # gauge outline
    outline = FancyBboxPatch(
        (gx, gy), gw, gh,
        boxstyle="round,pad=0.02,rounding_size=0.26",
        facecolor="none", edgecolor="#1f3b57",
        lw=3.2, zorder=6,
    )
    ax.add_patch(outline)

    # tick marks, right side (same as A1)
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

    # ---- GLOWING ZERO FLOOR (now the sole focal point) ------------
    # Slightly stronger glow than A1 because this is the star of the image.
    for glow_h, a in [(0.80, 0.05), (0.55, 0.09),
                      (0.36, 0.16), (0.22, 0.28),
                      (0.12, 0.48), (0.06, 0.75)]:
        ax.add_patch(Rectangle(
            (gx - 0.9, floor_y - glow_h / 2),
            gw + 1.8, glow_h,
            facecolor="#ffc23a", edgecolor="none",
            alpha=a, zorder=6,
        ))
    # bright core line
    ax.plot(
        [gx - 0.55, gx + gw + 0.55],
        [floor_y, floor_y],
        color="#ff9f1a", lw=6.5, zorder=9,
        solid_capstyle="round",
    )
    ax.plot(
        [gx - 0.55, gx + gw + 0.55],
        [floor_y, floor_y],
        color="#fff3b5", lw=2.8, zorder=10,
        solid_capstyle="round",
    )

    # ---- pedestal (same as A1) ------------------------------------
    base = FancyBboxPatch(
        (gx - 0.6, gy - 0.95), gw + 1.2, 1.05,
        boxstyle="round,pad=0.02,rounding_size=0.12",
        facecolor="#2f4d6b", edgecolor="#142536",
        lw=2.2, zorder=7,
    )
    ax.add_patch(base)
    ax.add_patch(Rectangle(
        (gx - 0.45, gy - 0.75), gw + 0.9, 0.12,
        facecolor="#6b8aa8", alpha=0.7, zorder=8,
    ))
    ax.add_patch(Rectangle(
        (gx - 0.45, gy - 0.05), gw + 0.9, 0.05,
        facecolor="#0b1a27", alpha=0.35, zorder=8,
    ))

    # ---- stylized "zero" halo -------------------------------------
    # A pale ring floating inside the empty gauge, centered vertically,
    # reinforcing "the reading is zero."
    halo_cx = gx + gw / 2
    halo_cy = floor_y + (gh - 0.15) * 0.45
    for r, lw, a in [(0.95, 4.5, 0.12),
                     (0.78, 3.5, 0.22),
                     (0.62, 2.8, 0.40)]:
        ax.add_patch(Circle(
            (halo_cx, halo_cy), r,
            facecolor="none", edgecolor="#ffb347",
            lw=lw, alpha=a, zorder=4,
        ))
    # Inner crisp ring (the "0" character without being a typographic 0)
    ax.add_patch(Circle(
        (halo_cx, halo_cy), 0.48,
        facecolor="none", edgecolor="#e07b00",
        lw=3.2, alpha=0.85, zorder=5,
    ))
    # faint fill to anchor the ring
    ax.add_patch(Circle(
        (halo_cx, halo_cy), 0.48,
        facecolor="#fff7e6", edgecolor="none",
        alpha=0.55, zorder=4,
    ))

    # ---- needle/pointer on the side pegged at zero ----------------
    # A small analog-style indicator showing the reading is pinned at bottom.
    nx, ny = gx - 1.35, floor_y + 0.8
    # dial arc
    theta = np.linspace(np.pi * 0.12, np.pi * 0.88, 60)
    dial_r = 0.70
    ax.plot(
        nx + dial_r * np.cos(theta),
        ny + dial_r * np.sin(theta),
        color="#1f3b57", lw=2.5, zorder=7,
    )
    # tick marks on dial
    for t in np.linspace(np.pi * 0.12, np.pi * 0.88, 7):
        x0 = nx + 0.60 * np.cos(t)
        y0 = ny + 0.60 * np.sin(t)
        x1 = nx + 0.75 * np.cos(t)
        y1 = ny + 0.75 * np.sin(t)
        ax.plot([x0, x1], [y0, y1], color="#1f3b57", lw=1.8, zorder=7)
    # needle pinned at the leftmost (zero) tick
    zero_t = np.pi * 0.88
    ax.plot(
        [nx, nx + 0.62 * np.cos(zero_t)],
        [ny, ny + 0.62 * np.sin(zero_t)],
        color="#c23b3b", lw=3.0, zorder=8,
        solid_capstyle="round",
    )
    # needle pivot
    ax.add_patch(Circle(
        (nx, ny), 0.07,
        facecolor="#1f3b57", edgecolor="none", zorder=9,
    ))
    # little highlight dot at zero tick to underline "pegged here"
    zx = nx + 0.82 * np.cos(zero_t)
    zy = ny + 0.82 * np.sin(zero_t)
    ax.add_patch(Circle(
        (zx, zy), 0.11,
        facecolor="#ffb347", edgecolor="#e07b00", lw=1.4,
        alpha=0.95, zorder=9,
    ))

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
