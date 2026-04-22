"""
Minimal Coupling constraint — visual-only illustration.

Metaphor: a simple two-node loop.  ρ ↔ ν with one clean coupling
shaft — nothing else.  Simplified from the Unified PDE centerpiece
(no operator satellites, no extra machinery).  Faded "no extra
channels / no hidden variables" ghost nodes hang struck-out above
and below the pair to make the minimality claim visually explicit.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch, Polygon,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\MinimalCoupling.png"


def glow_ball(ax, x, y, r, layers, highlight=True, zorder=10):
    for rr, a in [(r * 1.9, 0.07),
                  (r * 1.5, 0.14),
                  (r * 1.22, 0.28)]:
        ax.add_patch(Circle((x, y), rr,
                            facecolor=layers[0][1],
                            edgecolor="none", alpha=a,
                            zorder=zorder - 1))
    for frac, col in layers:
        ax.add_patch(Circle((x - 0.03 * (1 - frac),
                             y + 0.03 * (1 - frac)),
                            r * frac, facecolor=col,
                            edgecolor="none", zorder=zorder))
    if highlight:
        ax.add_patch(Circle((x - r * 0.32, y + r * 0.32),
                            r * 0.30,
                            facecolor="white", alpha=0.78,
                            zorder=zorder + 1))


def build():
    fig, ax = plt.subplots(figsize=(13, 9), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 14, 0, 10], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 14, 1.5,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # =============================================================
    # The two nodes: ρ (left, blue) and ν (right, amber)
    # =============================================================
    rho_cx, rho_cy = 4.2, 5.0
    rho_R = 1.20
    nu_cx, nu_cy = 9.8, 5.0
    nu_R = 1.00

    # ρ globe — blue, layered (matches UnifiedPDE ρ)
    glow_ball(ax, rho_cx, rho_cy, rho_R,
              layers=[
                  (1.00, "#b8dcef"),
                  (0.90, "#8fc8de"),
                  (0.78, "#57c6e6"),
                  (0.62, "#2791c2"),
                  (0.46, "#0f5e85"),
                  (0.30, "#0a3d56"),
              ],
              highlight=True, zorder=8)
    ax.add_patch(Circle((rho_cx, rho_cy), rho_R,
                        facecolor="none", edgecolor="#0b4a68",
                        lw=2.4, zorder=10))
    # ρ sentinel dot
    ax.add_patch(Circle((rho_cx, rho_cy), 0.10,
                        facecolor="white",
                        edgecolor="#0b4a68", lw=1.2, zorder=12))

    # ν sphere — amber (matches UnifiedPDE ν)
    glow_ball(ax, nu_cx, nu_cy, nu_R,
              layers=[
                  (1.00, "#ffe9b0"),
                  (0.90, "#ffd98a"),
                  (0.76, "#ffc470"),
                  (0.62, "#ff9f1a"),
                  (0.48, "#e07b00"),
                  (0.32, "#b45a00"),
              ],
              highlight=True, zorder=8)
    ax.add_patch(Circle((nu_cx, nu_cy), nu_R,
                        facecolor="none", edgecolor="#7a4a0a",
                        lw=2.4, zorder=10))
    ax.add_patch(Circle((nu_cx, nu_cy), 0.10,
                        facecolor="white",
                        edgecolor="#7a4a0a", lw=1.2, zorder=12))

    # =============================================================
    # Coupling shaft between them
    # =============================================================
    shaft_x0 = rho_cx + rho_R + 0.30
    shaft_x1 = nu_cx - nu_R - 0.30
    shaft_y = rho_cy

    # soft shaft glow layers (amber → cyan gradient hint)
    for h, a in [(0.80, 0.06), (0.60, 0.12),
                 (0.42, 0.22), (0.30, 0.36)]:
        ax.add_patch(FancyBboxPatch(
            (shaft_x0, shaft_y - h / 2),
            shaft_x1 - shaft_x0, h,
            boxstyle="round,pad=0.02,rounding_size=0.14",
            facecolor="#ffd24a", edgecolor="none",
            alpha=a, zorder=5,
        ))
    # core shaft body
    ax.add_patch(FancyBboxPatch(
        (shaft_x0, shaft_y - 0.20),
        shaft_x1 - shaft_x0, 0.40,
        boxstyle="round,pad=0.02,rounding_size=0.10",
        facecolor="#fff1b0", edgecolor="#c97a10", lw=2.0, zorder=7,
    ))

    # pulsing lights along the shaft (a mix of cyan and amber dots)
    n_pulses = 4
    for i, xt in enumerate(np.linspace(shaft_x0 + 0.45,
                                        shaft_x1 - 0.45, n_pulses)):
        if i % 2 == 0:
            inner = "#1aa6c7"
            outer = "#9fe6f3"
        else:
            inner = "#ff9f1a"
            outer = "#ffd98a"
        ax.add_patch(Circle((xt, shaft_y), 0.20,
                            facecolor=outer, edgecolor="none",
                            alpha=0.40, zorder=8))
        ax.add_patch(Circle((xt, shaft_y), 0.10,
                            facecolor=inner,
                            edgecolor="#1f3b57", lw=0.9,
                            zorder=9))

    # forward arrow (ρ → ν) along top of shaft (cyan: F[ρ] input to ν)
    top_arrow = FancyArrowPatch(
        (shaft_x0 + 0.15, shaft_y + 0.55),
        (shaft_x1 - 0.15, shaft_y + 0.55),
        arrowstyle="-|>", mutation_scale=22,
        color="#1aa6c7", lw=3.2, zorder=10,
    )
    ax.add_patch(top_arrow)
    # soft underlay
    for lw, a in [(9, 0.14), (5.5, 0.24)]:
        ax.plot([shaft_x0 + 0.15, shaft_x1 - 0.15],
                [shaft_y + 0.55, shaft_y + 0.55],
                color="#9fe6f3", lw=lw, alpha=a,
                solid_capstyle="round", zorder=9)

    # return arrow (ν → ρ) along bottom of shaft (amber: H·ν feedback)
    bot_arrow = FancyArrowPatch(
        (shaft_x1 - 0.15, shaft_y - 0.55),
        (shaft_x0 + 0.15, shaft_y - 0.55),
        arrowstyle="-|>", mutation_scale=22,
        color="#c97a10", lw=3.2, zorder=10,
    )
    ax.add_patch(bot_arrow)
    for lw, a in [(9, 0.14), (5.5, 0.24)]:
        ax.plot([shaft_x1 - 0.15, shaft_x0 + 0.15],
                [shaft_y - 0.55, shaft_y - 0.55],
                color="#ffd98a", lw=lw, alpha=a,
                solid_capstyle="round", zorder=9)

    # =============================================================
    # "No extra channels / hidden variables" indicators
    # Faded ghost nodes above and below, struck out.
    # =============================================================
    def ghost_no(gx, gy, fill="#c9d4e0", edge="#8a8e96"):
        # faded ghost orb
        ax.add_patch(Circle((gx, gy), 0.42,
                            facecolor=fill,
                            edgecolor=edge, lw=1.6,
                            alpha=0.55, zorder=6))
        ax.add_patch(Circle((gx - 0.12, gy + 0.14), 0.12,
                            facecolor="white", alpha=0.45, zorder=7))
        # red "no" circle-slash
        ax.add_patch(Circle((gx, gy), 0.54,
                            facecolor="none",
                            edgecolor="#c23b3b", lw=2.4,
                            alpha=0.85, zorder=11))
        ax.plot([gx - 0.38, gx + 0.38],
                [gy + 0.38, gy - 0.38],
                color="#c23b3b", lw=2.6, alpha=0.85,
                solid_capstyle="round", zorder=12)

    # Two ghosts above the shaft (would-be extra channels)
    ghost_no(5.2, 8.3)
    ghost_no(8.8, 8.3)
    # Two ghosts below (would-be hidden variables)
    ghost_no(5.2, 1.9)
    ghost_no(8.8, 1.9)

    # faded dashed "would-be" connector lines from the ghosts to the
    # main pair — to suggest the coupling THEY would have required
    # (also struck out by red slashes)
    for gx, gy, target_x, target_y in [
        (5.2, 8.3, rho_cx, rho_cy + rho_R * 0.7),
        (8.8, 8.3, nu_cx, nu_cy + nu_R * 0.7),
        (5.2, 1.9, rho_cx, rho_cy - rho_R * 0.7),
        (8.8, 1.9, nu_cx, nu_cy - nu_R * 0.7),
    ]:
        ax.plot([gx, target_x], [gy, target_y],
                color="#8a8e96", lw=1.2, alpha=0.35,
                linestyle=(0, (3, 4)), zorder=5)

    # ---- framing ---------------------------------------------------
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
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
