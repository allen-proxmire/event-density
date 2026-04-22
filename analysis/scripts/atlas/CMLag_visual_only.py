"""
Cluster Merger-Lag — visual-only illustration.

Metaphor: two galaxy clusters on a collision course, each trailing a
diffusive wake.  The offset ℓ between the cluster core and its trailing
density peak is the measurable "merger-lag" signature.

Composition:
  • Deep-space backdrop with a scattered starfield.
  • Two glowing galactic lobes — left cluster moving right, right
    cluster moving left, on a near-miss collision trajectory.
  • Each lobe leaves a trailing comet-like wake in the direction opposite
    its motion, with a distinct wake "tip" where the trailing density
    peaks.
  • A pair of bracket markers with a connecting bar measures the lag
    length ℓ between the cluster core and its wake peak — visually
    explicit.
  • Velocity arrows (bright) on each cluster showing the current motion.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, Ellipse, FancyArrowPatch, Polygon,
)
from matplotlib.colors import LinearSegmentedColormap

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\CMLag_merger.png"


def build():
    fig, ax = plt.subplots(figsize=(13, 9), dpi=220)

    # ---- deep-space backdrop --------------------------------------
    # navy→deep-violet gradient
    N = 600
    grad = np.zeros((N, N, 3))
    for i in range(N):
        t = i / (N - 1)
        # from navy-teal at top to deep violet at bottom
        c_top = np.array([0.06, 0.12, 0.22])
        c_bot = np.array([0.10, 0.07, 0.20])
        c = (1 - t) * c_top + t * c_bot
        grad[i, :, :] = c
    ax.imshow(grad, extent=[0, 14, 0, 10], aspect="auto",
              zorder=0)

    # starfield
    rng = np.random.default_rng(7)
    n_stars = 220
    for _ in range(n_stars):
        x = rng.uniform(0, 14)
        y = rng.uniform(0.2, 9.8)
        r = rng.uniform(0.012, 0.06)
        a = rng.uniform(0.35, 0.95)
        col = rng.choice(["#ffffff", "#e8ecff", "#fff6d8", "#d6e6ff"])
        ax.add_patch(Circle((x, y), r,
                            facecolor=col, edgecolor="none",
                            alpha=a, zorder=1))
        # a handful of bright stars with soft halos
        if r > 0.04:
            for rr, aa in [(r * 3.5, 0.08), (r * 2.2, 0.18)]:
                ax.add_patch(Circle((x, y), rr,
                                    facecolor=col, edgecolor="none",
                                    alpha=aa, zorder=1))

    # faint nebular wash across the middle (optional atmosphere)
    neb_grad = np.linspace(0, 1, 300).reshape(1, -1)
    ax.imshow(np.tile(neb_grad, (300, 1)),
              extent=[0, 14, 2.5, 7.5], aspect="auto",
              cmap="Purples", alpha=0.08, zorder=1)

    # =============================================================
    # Cluster geometry
    # =============================================================
    # LEFT cluster: core at x_L, moving RIGHT (+x)
    # RIGHT cluster: core at x_R, moving LEFT (-x)
    y_mid = 5.0
    x_L = 4.2
    x_R = 9.8
    core_R_L = 0.85
    core_R_R = 0.92

    def render_cluster(cx, cy, R_core, core_col, halo_col,
                       ring_col):
        """Draw a galaxy-cluster lobe: bright core, glow halo, faint outer ring."""
        # outer diffuse halo
        for rr, a in [(R_core * 4.0, 0.04),
                      (R_core * 3.2, 0.07),
                      (R_core * 2.5, 0.12),
                      (R_core * 2.0, 0.22),
                      (R_core * 1.6, 0.35)]:
            ax.add_patch(Circle((cx, cy), rr,
                                facecolor=halo_col, edgecolor="none",
                                alpha=a, zorder=5))
        # mid glow
        for rr, a in [(R_core * 1.30, 0.55),
                      (R_core * 1.12, 0.75)]:
            ax.add_patch(Circle((cx, cy), rr,
                                facecolor=core_col, edgecolor="none",
                                alpha=a, zorder=6))
        # bright core
        ax.add_patch(Circle((cx, cy), R_core * 0.85,
                            facecolor="white", edgecolor="none",
                            alpha=0.92, zorder=8))
        ax.add_patch(Circle((cx, cy), R_core * 0.58,
                            facecolor=core_col, edgecolor="none",
                            alpha=0.95, zorder=9))
        # subtle outer ring / iso-density (elongated ellipse)
        ax.add_patch(Ellipse((cx, cy), R_core * 3.2, R_core * 2.5,
                             facecolor="none", edgecolor=ring_col,
                             lw=1.2, alpha=0.35, zorder=7))

    # LEFT cluster — warm blue-cyan
    render_cluster(x_L, y_mid, core_R_L,
                   core_col="#7ec3de",
                   halo_col="#3fa6d0",
                   ring_col="#9fe6f3")
    # RIGHT cluster — warm amber
    render_cluster(x_R, y_mid, core_R_R,
                   core_col="#ffc470",
                   halo_col="#ff9f1a",
                   ring_col="#ffd98a")

    # =============================================================
    # Trailing WAKES (comet tails)
    # =============================================================
    def draw_wake(core_x, core_y, direction, length, width,
                  color_core, color_tail, tip_color):
        """direction = +1 for a wake extending to the RIGHT (left cluster wake),
                     = -1 for wake extending to the LEFT (right cluster wake).
        The wake is behind the motion, so LEFT cluster (moving +x) has wake
        to its LEFT (direction=-1 relative to motion but pointing leftward
        in image coords).
        """
        # The caller passes direction as the direction the wake EXTENDS IN.
        # Build a tapered polygon along that direction.
        n = 150
        s = np.linspace(0, 1, n)
        # taper width (widest near core, narrowing at tip)
        w = width * (1 - 0.6 * s)
        # slight downward drift to avoid cluster's own halo
        x_line = core_x + direction * s * length
        y_line = core_y + 0.05 * np.sin(s * np.pi) * 0.0  # straight

        # fill polygon (top + bottom edges)
        xs_poly = np.concatenate([x_line, x_line[::-1]])
        ys_poly = np.concatenate([core_y + w, (core_y - w)[::-1]])

        # soft outer halo layers
        for widen, a in [(1.8, 0.08), (1.4, 0.16), (1.15, 0.28)]:
            halo_ys = np.concatenate([core_y + w * widen,
                                      (core_y - w * widen)[::-1]])
            ax.fill(xs_poly, halo_ys,
                    facecolor=color_tail, edgecolor="none",
                    alpha=a, zorder=4)
        # main tail fill
        ax.fill(xs_poly, ys_poly,
                facecolor=color_core, edgecolor="none",
                alpha=0.72, zorder=4)

        # wake "tip" (the trailing density peak) — a distinct soft blob
        tip_x = core_x + direction * length * 0.55
        tip_y = core_y
        for rr, a in [(0.80, 0.10), (0.55, 0.22),
                      (0.38, 0.45), (0.26, 0.75)]:
            ax.add_patch(Circle((tip_x, tip_y), rr,
                                facecolor=tip_color, edgecolor="none",
                                alpha=a, zorder=5))
        ax.add_patch(Circle((tip_x, tip_y), 0.18,
                            facecolor="#ffffff", edgecolor=tip_color,
                            lw=1.4, alpha=0.95, zorder=6))
        return (tip_x, tip_y)

    # Wake for LEFT cluster — extends to the LEFT (behind its rightward motion)
    tipL = draw_wake(x_L, y_mid, direction=-1, length=3.0,
                     width=0.55,
                     color_core="#3fa6d0",
                     color_tail="#1579a8",
                     tip_color="#9fe6f3")
    # Wake for RIGHT cluster — extends to the RIGHT (behind its leftward motion)
    tipR = draw_wake(x_R, y_mid, direction=+1, length=3.0,
                     width=0.58,
                     color_core="#ff9f1a",
                     color_tail="#c97a10",
                     tip_color="#ffd98a")

    # =============================================================
    # Velocity arrows on each cluster (bright, pointing inward)
    # =============================================================
    # Left cluster moves RIGHT
    vx0 = x_L + core_R_L * 1.2
    vx1 = x_L + core_R_L * 2.2
    for lw, col, a in [(8, "#9fe6f3", 0.25),
                       (5, "#6fd2e9", 0.40)]:
        ax.plot([vx0, vx1], [y_mid, y_mid],
                color=col, lw=lw, alpha=a,
                solid_capstyle="round", zorder=7)
    ax.add_patch(FancyArrowPatch(
        (vx0, y_mid), (vx1, y_mid),
        arrowstyle="-|>", mutation_scale=22,
        color="#e0f5fb", lw=3.0, zorder=9,
    ))

    # Right cluster moves LEFT
    wx0 = x_R - core_R_R * 1.2
    wx1 = x_R - core_R_R * 2.2
    for lw, col, a in [(8, "#ffd98a", 0.25),
                       (5, "#ffb347", 0.40)]:
        ax.plot([wx0, wx1], [y_mid, y_mid],
                color=col, lw=lw, alpha=a,
                solid_capstyle="round", zorder=7)
    ax.add_patch(FancyArrowPatch(
        (wx0, y_mid), (wx1, y_mid),
        arrowstyle="-|>", mutation_scale=22,
        color="#fff4d6", lw=3.0, zorder=9,
    ))

    # =============================================================
    # Lag-length bracket markers ℓ (bottom)
    # =============================================================
    brack_y = y_mid - core_R_L * 2.5

    def lag_bracket(x_left, x_right, y, color):
        # vertical ticks at the ends
        ax.plot([x_left, x_left], [y - 0.22, y + 0.22],
                color=color, lw=2.6, zorder=10,
                solid_capstyle="round")
        ax.plot([x_right, x_right], [y - 0.22, y + 0.22],
                color=color, lw=2.6, zorder=10,
                solid_capstyle="round")
        # horizontal bar
        ax.plot([x_left, x_right], [y, y],
                color=color, lw=2.6, zorder=10,
                solid_capstyle="round")
        # mid-point circular badge (no text — just a distinguishing dot)
        mx = (x_left + x_right) / 2
        for rr, a in [(0.22, 0.20), (0.16, 0.40)]:
            ax.add_patch(Circle((mx, y), rr,
                                facecolor=color, edgecolor="none",
                                alpha=a, zorder=10))
        ax.add_patch(Circle((mx, y), 0.12,
                            facecolor="white", edgecolor=color,
                            lw=2.0, zorder=11))

    # Left cluster: bracket from wake-tip to cluster-core
    lag_bracket(tipL[0], x_L, brack_y, color="#9fe6f3")
    # Right cluster: bracket
    lag_bracket(x_R, tipR[0], brack_y, color="#ffd98a")

    # thin dashed vertical guides dropping from core and tip to bracket
    for gx, col in [(x_L, "#9fe6f3"),
                    (tipL[0], "#9fe6f3"),
                    (x_R, "#ffd98a"),
                    (tipR[0], "#ffd98a")]:
        ax.plot([gx, gx], [y_mid - core_R_L * 0.95, brack_y + 0.25],
                color=col, lw=0.9, alpha=0.45,
                linestyle=(0, (3, 3)), zorder=8)

    # =============================================================
    # Center "collision" hint — faint glow where clusters approach
    # =============================================================
    mid_x = (x_L + x_R) / 2
    for rr, a in [(1.9, 0.04), (1.4, 0.08), (1.0, 0.14)]:
        ax.add_patch(Circle((mid_x, y_mid), rr,
                            facecolor="#ffd24a", edgecolor="none",
                            alpha=a, zorder=6))

    # =============================================================
    # Small iconographic label for ℓ (a tiny "bracket" icon near the
    # right bracket, as a visual hint — no text)
    # =============================================================
    # Already have bracket markers above — leaving as-is.

    # ---- framing ---------------------------------------------------
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.tight_layout()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    plt.savefig(OUT, dpi=220, bbox_inches="tight",
                facecolor="#0a0e1a", edgecolor="none")
    plt.close(fig)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    build()
