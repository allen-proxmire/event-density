"""
Locality constraint — visual-only illustration.

Metaphor: a field of lattice points where a single central "update"
point receives contributions ONLY from its immediate neighbors.

Composition:
  • A soft lattice of dim grey points fills the panel (the "far field").
  • At the center, the update point glows brightly in cyan.
  • Its 8 immediate neighbors (3×3 stencil minus center) glow cyan
    around it, each with a short arrow pointing INTO the center.
  • Two or three distant dim points carry a red circle-slash badge
    connected to the center by a faded dashed line — visual assertion
    that long-range coupling is forbidden.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\Locality.png"


def glow_dot(ax, x, y, r, core, halo, edge=None, zorder=10):
    edge = edge or core
    for rr, a in [(r * 2.6, 0.08),
                  (r * 2.0, 0.14),
                  (r * 1.55, 0.24),
                  (r * 1.22, 0.40)]:
        ax.add_patch(Circle((x, y), rr, facecolor=halo,
                            edgecolor="none", alpha=a,
                            zorder=zorder - 1))
    ax.add_patch(Circle((x, y), r, facecolor=core,
                        edgecolor=edge, lw=1.4, zorder=zorder))
    ax.add_patch(Circle((x - r * 0.32, y + r * 0.32),
                        r * 0.32,
                        facecolor="white", alpha=0.75,
                        zorder=zorder + 1))


def build():
    fig, ax = plt.subplots(figsize=(11, 10), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 12, 0, 11], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 12, 1.6,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # =============================================================
    # Lattice grid of dim far-field points
    # =============================================================
    cx, cy = 6.0, 6.0
    spacing = 0.85
    n_rows = 9
    n_cols = 11
    # center the lattice on (cx, cy) with an odd count so center sits on a node
    i_center = n_rows // 2
    j_center = n_cols // 2
    far_pts = []
    for i in range(n_rows):
        for j in range(n_cols):
            x = cx + (j - j_center) * spacing
            y = cy + (i - i_center) * spacing
            # clip to a tidy circular-ish region
            if np.hypot(x - cx, y - cy) > 4.3:
                continue
            dist = max(abs(i - i_center), abs(j - j_center))
            far_pts.append((x, y, dist))

    # draw dim grey points for dist > 1
    for (x, y, dist) in far_pts:
        if dist > 1:
            ax.add_patch(Circle((x, y), 0.11,
                                facecolor="#c9d4e0",
                                edgecolor="#5b6b80",
                                lw=0.6, alpha=0.70, zorder=3))

    # =============================================================
    # The 3×3 local stencil (dist 0 and 1)
    # =============================================================
    stencil_pts = [(x, y, dist) for (x, y, dist) in far_pts if dist <= 1]
    # neighbors = dist == 1, center = dist == 0
    neighbor_pts = [(x, y) for (x, y, d) in stencil_pts if d == 1]
    center_pt = [(x, y) for (x, y, d) in stencil_pts if d == 0][0]

    # soft cyan glow covering the whole 3×3 region
    stencil_R = spacing * 1.55
    for rr, a in [(stencil_R * 1.40, 0.06),
                  (stencil_R * 1.18, 0.12),
                  (stencil_R * 1.02, 0.22)]:
        ax.add_patch(Circle(center_pt, rr,
                            facecolor="#9fe6f3",
                            edgecolor="none", alpha=a, zorder=4))

    # subtle rounded-square outline of the stencil
    ax.add_patch(FancyBboxPatch(
        (center_pt[0] - spacing * 1.45,
         center_pt[1] - spacing * 1.45),
        spacing * 2.90, spacing * 2.90,
        boxstyle="round,pad=0.02,rounding_size=0.18",
        facecolor="none", edgecolor="#1aa6c7",
        lw=2.4, alpha=0.80, zorder=5,
    ))
    # tiny inner dashed boundary
    ax.add_patch(FancyBboxPatch(
        (center_pt[0] - spacing * 1.35,
         center_pt[1] - spacing * 1.35),
        spacing * 2.70, spacing * 2.70,
        boxstyle="round,pad=0.02,rounding_size=0.14",
        facecolor="none", edgecolor="#6fd2e9",
        lw=1.2, alpha=0.55,
        linestyle=(0, (4, 3)), zorder=5,
    ))

    # neighbor points — glowing cyan
    for (nx, ny) in neighbor_pts:
        glow_dot(ax, nx, ny, r=0.16,
                 core="#4fa3d8", halo="#9fe6f3",
                 edge="#0b4a68", zorder=8)

    # short arrows from each neighbor INTO the center
    for (nx, ny) in neighbor_pts:
        # stop short of the center orb
        cx_, cy_ = center_pt
        dx_ = cx_ - nx
        dy_ = cy_ - ny
        L = np.hypot(dx_, dy_)
        uh = (dx_ / L, dy_ / L)
        p0 = (nx + uh[0] * 0.22, ny + uh[1] * 0.22)
        p1 = (cx_ - uh[0] * 0.38, cy_ - uh[1] * 0.38)
        # glow underlay
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]],
                color="#9fe6f3", lw=6, alpha=0.30,
                solid_capstyle="round", zorder=6)
        ax.add_patch(FancyArrowPatch(
            p0, p1,
            arrowstyle="-|>", mutation_scale=16,
            color="#1aa6c7", lw=2.4, zorder=9,
        ))

    # center update point (larger, brighter)
    glow_dot(ax, center_pt[0], center_pt[1], r=0.28,
             core="#2791c2", halo="#9fe6f3",
             edge="#0b4a68", zorder=12)

    # subtle pulsing rings around the center
    for rr, a in [(0.50, 0.25), (0.72, 0.15), (0.96, 0.08)]:
        ax.add_patch(Circle(center_pt, rr,
                            facecolor="none",
                            edgecolor="#1aa6c7",
                            lw=1.6, alpha=a, zorder=11))

    # =============================================================
    # Forbidden long-range coupling indicators
    # =============================================================
    # pick three distant points and show faded dashed lines to center
    # with red circle-slash badges near the distant end.
    far_dists = [(p[0], p[1], p[2]) for p in far_pts if p[2] >= 3]
    # pick three spread around
    forbidden_targets = []
    if far_dists:
        # hand-pick by angle for good spacing
        target_angles = [np.deg2rad(25),
                         np.deg2rad(155),
                         np.deg2rad(250)]
        for t_ang in target_angles:
            best = min(far_dists,
                       key=lambda p: abs(np.arctan2(p[1] - cy,
                                                     p[0] - cx) - t_ang)
                                      + abs(4.2 - np.hypot(p[0] - cx,
                                                            p[1] - cy)))
            forbidden_targets.append(best)

    for (fx, fy, _) in forbidden_targets:
        # faded dashed line from center to the far point
        ax.plot([center_pt[0], fx], [center_pt[1], fy],
                color="#c23b3b", lw=1.4, alpha=0.35,
                linestyle=(0, (3, 4)), zorder=6)
        # red circle-slash badge at the far end
        # "no" circle
        ax.add_patch(Circle((fx, fy), 0.28,
                            facecolor="white",
                            edgecolor="#c23b3b", lw=2.4,
                            alpha=0.95, zorder=11))
        # slash
        ax.plot([fx - 0.20, fx + 0.20],
                [fy + 0.20, fy - 0.20],
                color="#c23b3b", lw=2.6, alpha=0.95,
                solid_capstyle="round", zorder=12)

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
