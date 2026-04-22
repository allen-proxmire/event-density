"""
Dimensional Invariant — visual-only illustration.

Metaphor: one dimensionless core value (D · T₀ / L₀² ≈ 0.3) shared
across five radically different physical regimes.

Composition:
  • Central GOLDEN CORE orb — the dimensionless invariant.  Surrounded
    by a radial starburst of rays.
  • Five iconic regime badges arranged in a pentagon around the core,
    each a small circular window showing a stylized scene at that
    scale:
        top         — cosmological filament (large scale structure)
        upper-right — galactic (spiral disc)
        lower-right — condensed matter (ordered dot lattice)
        lower-left  — quantum (atom with orbital ellipses)
        upper-left  — Planck / sub-quantum (spacetime foam, tiny mesh)
  • Each badge has an embedded "tag" copy of the SAME golden invariant
    orb (same size, same color) to assert "identical value."
  • Glowing lines connect each badge back to the central core.
  • A subtle outer "scales" motif — different-sized ruler marks — on
    each connector hints that the physical L₀ differs wildly, but the
    dimensionless ratio does not.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, Ellipse, FancyArrowPatch, Polygon,
)
from matplotlib.path import Path
from matplotlib.patches import PathPatch

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\DimInv.png"


def invariant_orb(ax, x, y, r=0.55, zorder=10):
    """The signature amber/gold invariant orb (reused in each badge)."""
    for rr, a in [(r * 2.2, 0.05),
                  (r * 1.7, 0.10),
                  (r * 1.35, 0.20),
                  (r * 1.12, 0.38)]:
        ax.add_patch(Circle((x, y), rr,
                            facecolor="#ffd24a", edgecolor="none",
                            alpha=a, zorder=zorder - 1))
    for rr, col in [(r * 0.95, "#fff1b0"),
                    (r * 0.80, "#ffd24a"),
                    (r * 0.62, "#ffb347"),
                    (r * 0.44, "#ff9f1a"),
                    (r * 0.28, "#e07b00")]:
        ax.add_patch(Circle((x, y), rr,
                            facecolor=col, edgecolor="none",
                            zorder=zorder))
    # crown highlight
    ax.add_patch(Circle((x - r * 0.28, y + r * 0.30), r * 0.25,
                        facecolor="white", alpha=0.78,
                        zorder=zorder + 1))
    # outer crisp ring
    ax.add_patch(Circle((x, y), r,
                        facecolor="none",
                        edgecolor="#c97a10", lw=2.0,
                        zorder=zorder + 2))


def badge_frame(ax, cx, cy, R=1.10, outline="#1f3b57",
                halo="#9aaed0"):
    """A round badge frame (dark interior, soft halo)."""
    # halo
    for rr, a in [(R * 1.40, 0.05),
                  (R * 1.22, 0.10),
                  (R * 1.08, 0.18)]:
        ax.add_patch(Circle((cx, cy), rr, facecolor=halo,
                            edgecolor="none", alpha=a, zorder=3))
    # dark interior
    ax.add_patch(Circle((cx, cy), R,
                        facecolor="#0f2038",
                        edgecolor=outline, lw=2.4, zorder=5))
    # inner rim
    ax.add_patch(Circle((cx, cy), R - 0.12,
                        facecolor="none", edgecolor="#6b8aa8",
                        lw=0.9, alpha=0.55, zorder=6))


def scene_cosmological(ax, cx, cy, R=1.10):
    """Filament / cosmic-web stick-figure inside a badge."""
    badge_frame(ax, cx, cy, R)
    # scattered node dots with connecting "filaments"
    rng = np.random.default_rng(8)
    nodes = []
    for _ in range(9):
        x = cx + rng.uniform(-R * 0.75, R * 0.75)
        y = cy + rng.uniform(-R * 0.75, R * 0.75)
        if np.hypot(x - cx, y - cy) < R * 0.85:
            nodes.append((x, y))
    # connections (short filaments between neighbors)
    for i, (x, y) in enumerate(nodes):
        # connect to 2 nearest neighbors
        dists = sorted(
            [(j, np.hypot(x - nx, y - ny))
             for j, (nx, ny) in enumerate(nodes) if j != i],
            key=lambda t: t[1],
        )
        for j, _ in dists[:2]:
            nx_, ny_ = nodes[j]
            ax.plot([x, nx_], [y, ny_],
                    color="#7ec3de", lw=1.4, alpha=0.55, zorder=7)
    for (x, y) in nodes:
        ax.add_patch(Circle((x, y), 0.07,
                            facecolor="#9fe6f3",
                            edgecolor="#1aa6c7", lw=0.9,
                            alpha=0.95, zorder=8))


def scene_galactic(ax, cx, cy, R=1.10):
    """Stylized spiral galaxy."""
    badge_frame(ax, cx, cy, R)
    # spiral arms (logarithmic)
    thetas = np.linspace(0, 3.8 * np.pi, 160)
    a_spiral = 0.12
    b_spiral = 0.095
    for phase in [0, np.pi]:
        rs = a_spiral * np.exp(b_spiral * thetas)
        rs = rs / rs.max() * (R * 0.82)
        xs = cx + rs * np.cos(thetas + phase)
        ys = cy + rs * np.sin(thetas + phase)
        for lw, col, alp in [(6, "#9fe6f3", 0.15),
                             (3.2, "#6fd2e9", 0.35),
                             (1.6, "#ecf9ff", 0.9)]:
            ax.plot(xs, ys, color=col, lw=lw, alpha=alp,
                    solid_capstyle="round", zorder=7)
    # bright core
    for rr, a in [(0.30, 0.20), (0.22, 0.40)]:
        ax.add_patch(Circle((cx, cy), rr,
                            facecolor="#fff1b0",
                            edgecolor="none", alpha=a, zorder=8))
    ax.add_patch(Circle((cx, cy), 0.15,
                        facecolor="#ffd24a",
                        edgecolor="#c97a10", lw=1.0, zorder=9))


def scene_condensed_matter(ax, cx, cy, R=1.10):
    """Ordered hexagonal-ish dot lattice."""
    badge_frame(ax, cx, cy, R)
    # hexagonal lattice of dots
    a = 0.35
    for i in range(-3, 4):
        for j in range(-3, 4):
            x = cx + (i + 0.5 * (j % 2)) * a
            y = cy + j * (a * np.sqrt(3) / 2)
            if np.hypot(x - cx, y - cy) < R * 0.82:
                ax.add_patch(Circle((x, y), 0.09,
                                    facecolor="#c8aff0",
                                    edgecolor="#6a3fb0", lw=0.9,
                                    alpha=0.95, zorder=7))
    # thin connecting lattice lines (soft)
    for ang in [0, np.pi / 3, 2 * np.pi / 3]:
        for shift in np.linspace(-R * 0.7, R * 0.7, 7):
            # draw a line at orientation `ang` with perpendicular offset shift
            u = np.array([np.cos(ang), np.sin(ang)])
            n = np.array([-u[1], u[0]])
            p0 = np.array([cx, cy]) + n * shift - u * R
            p1 = np.array([cx, cy]) + n * shift + u * R
            ax.plot([p0[0], p1[0]], [p0[1], p1[1]],
                    color="#8a5ac9", lw=0.6, alpha=0.18, zorder=6)


def scene_quantum(ax, cx, cy, R=1.10):
    """Atom: nucleus + elliptical orbits."""
    badge_frame(ax, cx, cy, R)
    # orbits
    for tilt, ra, rb, col in [
        (np.deg2rad(20), R * 0.78, R * 0.32, "#6fd2e9"),
        (np.deg2rad(-40), R * 0.80, R * 0.28, "#9fe6f3"),
        (np.deg2rad(75), R * 0.75, R * 0.30, "#7ec3de"),
    ]:
        th_loc = np.linspace(0, 2 * np.pi, 200)
        x0 = ra * np.cos(th_loc)
        y0 = rb * np.sin(th_loc)
        xs = cx + np.cos(tilt) * x0 - np.sin(tilt) * y0
        ys = cy + np.sin(tilt) * x0 + np.cos(tilt) * y0
        ax.plot(xs, ys, color=col, lw=1.6, alpha=0.85, zorder=7)
    # nucleus
    for rr, a in [(0.25, 0.18), (0.18, 0.40)]:
        ax.add_patch(Circle((cx, cy), rr,
                            facecolor="#ffd24a",
                            edgecolor="none", alpha=a, zorder=8))
    ax.add_patch(Circle((cx, cy), 0.12,
                        facecolor="#ffae79",
                        edgecolor="#7a2d0b", lw=1.0, zorder=9))
    # a couple of orbiting electrons
    electron_positions = [
        (cx + R * 0.55, cy + R * 0.35),
        (cx - R * 0.45, cy - R * 0.25),
    ]
    for (ex, ey) in electron_positions:
        ax.add_patch(Circle((ex, ey), 0.08,
                            facecolor="#9fe6f3",
                            edgecolor="#1aa6c7", lw=0.9,
                            alpha=0.95, zorder=10))


def scene_planck(ax, cx, cy, R=1.10):
    """Planck-scale foam: a dense random mesh."""
    badge_frame(ax, cx, cy, R)
    rng = np.random.default_rng(22)
    # small random nodes + connections (foam-like)
    pts = []
    while len(pts) < 22:
        x = cx + rng.uniform(-R * 0.75, R * 0.75)
        y = cy + rng.uniform(-R * 0.75, R * 0.75)
        if np.hypot(x - cx, y - cy) < R * 0.85:
            pts.append((x, y))
    # connect each to 2-3 nearest neighbors
    for i, (x, y) in enumerate(pts):
        dists = sorted(
            [(j, np.hypot(x - nx, y - ny))
             for j, (nx, ny) in enumerate(pts) if j != i],
            key=lambda t: t[1],
        )
        for j, _ in dists[:3]:
            nx_, ny_ = pts[j]
            ax.plot([x, nx_], [y, ny_],
                    color="#c8aff0", lw=0.8, alpha=0.35, zorder=7)
    for (x, y) in pts:
        ax.add_patch(Circle((x, y), 0.045,
                            facecolor="#e6d6ff",
                            edgecolor="#6a3fb0", lw=0.5,
                            alpha=0.9, zorder=8))


def build():
    fig, ax = plt.subplots(figsize=(11, 11), dpi=220)

    # ---- dark-neutral cosmic backdrop with soft glow --------------
    N = 600
    grad = np.zeros((N, N, 3))
    for i in range(N):
        t = i / (N - 1)
        c_top = np.array([0.08, 0.11, 0.22])
        c_bot = np.array([0.05, 0.07, 0.14])
        grad[i, :, :] = (1 - t) * c_top + t * c_bot
    ax.imshow(grad, extent=[0, 12, 0, 12], aspect="auto", zorder=0)

    # sparse starfield
    rng_bg = np.random.default_rng(3)
    for _ in range(180):
        x = rng_bg.uniform(0, 12)
        y = rng_bg.uniform(0, 12)
        r = rng_bg.uniform(0.01, 0.045)
        a = rng_bg.uniform(0.25, 0.85)
        ax.add_patch(Circle((x, y), r,
                            facecolor="#eceaff", edgecolor="none",
                            alpha=a, zorder=1))

    # =============================================================
    # Central invariant core
    # =============================================================
    ccx, ccy = 6.0, 6.0
    core_R = 1.35

    # radial starburst rays
    for ang_deg in np.linspace(0, 360, 36, endpoint=False):
        th = np.deg2rad(ang_deg)
        r0 = core_R + 0.25
        r1 = core_R + 1.30
        ax.plot([ccx + r0 * np.cos(th), ccx + r1 * np.cos(th)],
                [ccy + r0 * np.sin(th), ccy + r1 * np.sin(th)],
                color="#ffd98a", lw=1.6, alpha=0.25,
                solid_capstyle="round", zorder=2)

    # big outer halo
    for rr, a in [(core_R * 3.0, 0.04),
                  (core_R * 2.3, 0.08),
                  (core_R * 1.8, 0.15),
                  (core_R * 1.45, 0.25)]:
        ax.add_patch(Circle((ccx, ccy), rr,
                            facecolor="#ffd24a", edgecolor="none",
                            alpha=a, zorder=3))

    invariant_orb(ax, ccx, ccy, r=core_R, zorder=10)

    # =============================================================
    # Five regime badges in a pentagon around the core
    # =============================================================
    scenes = [
        ("cosmological", scene_cosmological),
        ("galactic", scene_galactic),
        ("condensed", scene_condensed_matter),
        ("quantum", scene_quantum),
        ("planck", scene_planck),
    ]

    badge_R = 1.15
    ring_R = 4.4
    # top, then clockwise
    angles = [90, 90 - 72, 90 - 144, 90 - 216, 90 - 288]
    badge_centers = []

    for ang_deg, (name, scene_fn) in zip(angles, scenes):
        th = np.deg2rad(ang_deg)
        bx = ccx + ring_R * np.cos(th)
        by = ccy + ring_R * np.sin(th)
        badge_centers.append((bx, by))
        scene_fn(ax, bx, by, R=badge_R)
        # small invariant tag inside each badge at the bottom-right
        tag_x = bx + badge_R * 0.55
        tag_y = by - badge_R * 0.55
        invariant_orb(ax, tag_x, tag_y, r=0.24, zorder=12)

    # =============================================================
    # Connecting rays from each badge to the core
    # =============================================================
    for (bx, by) in badge_centers:
        # compute start on the badge rim toward the core
        dx_, dy_ = ccx - bx, ccy - by
        L = np.hypot(dx_, dy_)
        uh = (dx_ / L, dy_ / L)
        p0 = (bx + uh[0] * badge_R * 1.05,
              by + uh[1] * badge_R * 1.05)
        # end just outside the core rim
        p1 = (ccx - uh[0] * core_R * 1.05,
              ccy - uh[1] * core_R * 1.05)
        # glow
        for lw, col, a in [(9, "#ffd98a", 0.12),
                           (5.5, "#ffb347", 0.25)]:
            ax.plot([p0[0], p1[0]], [p0[1], p1[1]],
                    color=col, lw=lw, alpha=a,
                    solid_capstyle="round", zorder=3)
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]],
                color="#c97a10", lw=2.2, alpha=0.92,
                solid_capstyle="round", zorder=4)

        # a little "ruler" motif along the connector — 4 tick marks
        # perpendicular to the line, sized differently to hint
        # "different physical scales, same ratio"
        nh = (-uh[1], uh[0])
        for k, tsize in zip(np.linspace(0.25, 0.78, 4),
                            [0.05, 0.10, 0.17, 0.24]):
            mx = p0[0] + k * (p1[0] - p0[0])
            my = p0[1] + k * (p1[1] - p0[1])
            x_t0 = mx - nh[0] * tsize
            y_t0 = my - nh[1] * tsize
            x_t1 = mx + nh[0] * tsize
            y_t1 = my + nh[1] * tsize
            ax.plot([x_t0, x_t1], [y_t0, y_t1],
                    color="#fff1b0", lw=1.4, alpha=0.7, zorder=5,
                    solid_capstyle="round")

    # ---- framing ---------------------------------------------------
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
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
