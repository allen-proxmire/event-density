"""
P1 Operator Structure — visual-only illustration.

Metaphor: a central density cloud caught in a tug-of-war.
  - OUTWARD cyan flow-arrows radiate from the blob (mobility-driven
    spreading, the M∇²p + M'|∇p|² terms).
  - INWARD amber springs wrap from an outer anchor ring back to the
    blob's surface (the penalty term P(p) restoring toward equilibrium).

The eye reads "two competing forces → one operator" instantly.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch,
)
from matplotlib.colors import LinearSegmentedColormap

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\P1_operator_structure.png"


def spring_path(p0, p1, coils=7, amplitude=0.18,
                lead_frac=0.12, tail_frac=0.12):
    """Return (xs, ys) for a stylized spring between two points."""
    p0, p1 = np.asarray(p0), np.asarray(p1)
    v = p1 - p0
    L = np.linalg.norm(v)
    if L == 0:
        return np.array([p0[0]]), np.array([p0[1]])
    uhat = v / L
    nhat = np.array([-uhat[1], uhat[0]])

    n_pts = 400
    t = np.linspace(0, 1, n_pts)
    # flat leads at both ends, sine coils in the middle
    lead = lead_frac
    tail = 1 - tail_frac
    amp = np.where((t < lead) | (t > tail),
                   0.0,
                   amplitude)
    # ramp amplitude in/out smoothly
    ramp = np.ones_like(t)
    ramp = np.where(t < lead, 0, ramp)
    ramp = np.where(t > tail, 0, ramp)
    # local phase only in the coil region
    coil_phase = np.zeros_like(t)
    in_coil = (t >= lead) & (t <= tail)
    tt = (t[in_coil] - lead) / (tail - lead)
    coil_phase[in_coil] = np.sin(2 * np.pi * coils * tt)

    pts = (p0[:, None]
           + uhat[:, None] * (t * L)
           + nhat[:, None] * (amp * coil_phase))
    return pts[0], pts[1]


def build():
    fig, ax = plt.subplots(figsize=(10, 10), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 11, 0, 11], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 11, 2.0,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # ---- central density cloud ------------------------------------
    cx, cy = 5.5, 5.6
    # radial Gaussian field rendered via concentric soft rings
    for rr, a, col in [
        (2.55, 0.05, "#b8dcef"),
        (2.20, 0.10, "#9bcde6"),
        (1.90, 0.18, "#6fbadb"),
        (1.60, 0.30, "#3fa6d0"),
        (1.30, 0.48, "#2791c2"),
        (1.00, 0.70, "#1579a8"),
        (0.72, 0.90, "#0f5e85"),
    ]:
        ax.add_patch(Circle((cx, cy), rr,
                            facecolor=col, edgecolor="none",
                            alpha=a, zorder=3))

    # crisp inner core
    ax.add_patch(Circle((cx, cy), 0.45,
                        facecolor="#57c6e6", edgecolor="#0b4a68",
                        lw=1.8, alpha=0.92, zorder=4))
    ax.add_patch(Circle((cx - 0.15, cy + 0.15), 0.18,
                        facecolor="white", alpha=0.7, zorder=5))

    # faint concentric iso-level rings (visual texture)
    for rr in [1.10, 1.55, 2.05]:
        ax.add_patch(Circle((cx, cy), rr,
                            facecolor="none", edgecolor="#2a3a50",
                            lw=0.8, alpha=0.25, zorder=4))

    # ---- OUTWARD mobility flow arrows -----------------------------
    # radial arrows originating from inner blob and pointing outward
    n_out = 8
    r_start = 1.15
    r_end = 2.45
    for k in range(n_out):
        th = (k + 0.5) * 2 * np.pi / n_out
        p0 = (cx + r_start * np.cos(th), cy + r_start * np.sin(th))
        p1 = (cx + r_end * np.cos(th), cy + r_end * np.sin(th))
        # arrow with soft cyan glow
        for lw, col, a in [(7.5, "#9fe6f3", 0.18),
                           (5.5, "#6fd2e9", 0.30),
                           (4.0, "#3fb8d4", 0.55)]:
            ax.plot([p0[0], p1[0]], [p0[1], p1[1]],
                    color=col, lw=lw, alpha=a,
                    solid_capstyle="round", zorder=5)
        arrow = FancyArrowPatch(
            p0, p1,
            arrowstyle="-|>", mutation_scale=20,
            color="#1aa6c7", lw=3.0, zorder=6,
        )
        ax.add_patch(arrow)

    # ---- outer anchor ring (equilibrium) --------------------------
    R_anchor = 4.35
    # anchor ring drawn as a dashed golden circle
    theta = np.linspace(0, 2 * np.pi, 400)
    ax_ring_x = cx + R_anchor * np.cos(theta)
    ax_ring_y = cy + R_anchor * np.sin(theta)
    # soft halo
    for lw, col, a in [(12, "#ffd24a", 0.08),
                       (7, "#ffb347", 0.20),
                       (4.0, "#ff9f1a", 0.40)]:
        ax.plot(ax_ring_x, ax_ring_y,
                color=col, lw=lw, alpha=a, zorder=2)
    # crisp ring, dashed to hint "equilibrium contour"
    ax.plot(ax_ring_x, ax_ring_y,
            color="#d69a1a", lw=2.4, linestyle=(0, (8, 4)),
            alpha=0.95, zorder=7)

    # ---- INWARD penalty springs -----------------------------------
    # springs go from the anchor ring back to the blob boundary
    n_sp = 8
    r_blob = 2.55
    for k in range(n_sp):
        th = (k * 2 * np.pi / n_sp)  # offset from outward arrows
        p_out = (cx + R_anchor * np.cos(th), cy + R_anchor * np.sin(th))
        p_in = (cx + r_blob * np.cos(th), cy + r_blob * np.sin(th))
        xs, ys = spring_path(p_out, p_in, coils=6, amplitude=0.18)
        # glow pass
        ax.plot(xs, ys, color="#ffd98a", lw=7, alpha=0.20, zorder=6,
                solid_capstyle="round")
        ax.plot(xs, ys, color="#ffb347", lw=4.5, alpha=0.45, zorder=6,
                solid_capstyle="round")
        # crisp spring
        ax.plot(xs, ys, color="#c97a10", lw=2.2, alpha=0.98, zorder=7,
                solid_capstyle="round")

        # anchor dot on outer ring
        ax.add_patch(Circle(p_out, 0.11,
                            facecolor="#d69a1a", edgecolor="#7a4a0a",
                            lw=1.3, zorder=8))
        # small red-hot "pulling tip" where the spring grabs the blob
        ax.add_patch(Circle(p_in, 0.09,
                            facecolor="#ff9f1a", edgecolor="#7a4a0a",
                            lw=1.0, zorder=8))

    # ---- legend-style corner glyphs (no text; icons only) ---------
    # Top-left: "outward flow" glyph  -> cyan arrow set
    def draw_badge(bx, by, face, edge, r=0.42):
        for rr, a in [(r * 1.45, 0.08),
                      (r * 1.22, 0.16),
                      (r * 1.08, 0.30)]:
            ax.add_patch(Circle((bx, by), rr, facecolor=edge,
                                edgecolor="none", alpha=a, zorder=9))
        ax.add_patch(Circle((bx, by), r,
                            facecolor=face, edgecolor=edge,
                            lw=2.4, zorder=10))

    # Mobility badge (top-right)
    mb_x, mb_y = 9.9, 9.6
    draw_badge(mb_x, mb_y, "#dff3f8", "#1aa6c7")
    # three diverging arrows inside
    for ang in [np.pi * 0.15, np.pi * 0.50, np.pi * 0.85]:
        x0, y0 = mb_x - 0.15, mb_y - 0.15
        dx, dy = 0.38 * np.cos(ang), 0.38 * np.sin(ang)
        ax.annotate("",
                    xy=(x0 + dx, y0 + dy),
                    xytext=(x0, y0),
                    arrowprops=dict(arrowstyle="-|>", color="#1aa6c7",
                                    lw=2.2),
                    zorder=11)

    # Penalty badge (bottom-right)
    pb_x, pb_y = 9.9, 1.15
    draw_badge(pb_x, pb_y, "#fff1d8", "#c97a10")
    # spring glyph inside the badge
    xs, ys = spring_path((pb_x - 0.3, pb_y), (pb_x + 0.3, pb_y),
                         coils=4, amplitude=0.10)
    ax.plot(xs, ys, color="#c97a10", lw=2.4, solid_capstyle="round",
            zorder=11)
    # two anchor dots
    ax.add_patch(Circle((pb_x - 0.30, pb_y), 0.06,
                        facecolor="#c97a10", edgecolor="none", zorder=12))
    ax.add_patch(Circle((pb_x + 0.30, pb_y), 0.06,
                        facecolor="#c97a10", edgecolor="none", zorder=12))

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
