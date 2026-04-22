"""
D.19 Uniqueness Theorem — visual-only illustration.

Metaphor: eleven constraint-streams (4 axioms A1–A4 + 7 canon principles
P1–P7) converge through a bright prism/lens into a single radiant
output — the uniquely determined PDE.  Alternative PDE candidates
hover faintly above and below the output, struck through to convey
"these were possible forms; the canon forbids them all but one."

Composition (left-to-right):
  1.  Left stack of 11 glowing colored orbs (axioms top, principles below)
  2.  Curved flow-lines from each orb converging on a central lens
  3.  Central lens: a radiant starburst prism
  4.  Single bright output beam from the lens
  5.  Large luminous orb on the right — THE unique PDE
  6.  Faded ghost-orbs above/below the beam, each with a red circle-slash
      to indicate "alternative forms are ruled out"
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch, Polygon,
)
from matplotlib.path import Path
from matplotlib.patches import PathPatch

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\D19_uniqueness.png"


def glowing_orb(ax, x, y, r, core, halo, edge=None, zorder=10):
    edge = edge or core
    for rr, a in [(r * 2.6, 0.08),
                  (r * 2.0, 0.14),
                  (r * 1.55, 0.24),
                  (r * 1.22, 0.40)]:
        ax.add_patch(Circle((x, y), rr, facecolor=halo,
                            edgecolor="none", alpha=a, zorder=zorder - 1))
    ax.add_patch(Circle((x, y), r, facecolor=core,
                        edgecolor=edge, lw=1.6, zorder=zorder))
    # specular highlight
    ax.add_patch(Circle((x - r * 0.32, y + r * 0.32),
                        r * 0.34, facecolor="white",
                        alpha=0.70, zorder=zorder + 1))


def bezier(ax, p0, p1, color, halo, lw=3.0, alpha=1.0, zorder=5,
           rad=0.0):
    """Smooth cubic curve with glow between two points."""
    p0 = np.asarray(p0, float)
    p1 = np.asarray(p1, float)
    # two control points — bend rightward toward target
    dx = p1[0] - p0[0]
    c1 = (p0[0] + dx * 0.55, p0[1])
    c2 = (p1[0] - dx * 0.30, p1[1] + rad * np.sign(p1[1] - p0[1]) * -0.2)
    verts = [p0, c1, c2, p1]
    codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
    path = Path(verts, codes)
    # glow passes
    for lw_, a_ in [(lw + 6, 0.12), (lw + 3, 0.22)]:
        ax.add_patch(PathPatch(path, facecolor="none", edgecolor=halo,
                               lw=lw_, alpha=a_, zorder=zorder))
    ax.add_patch(PathPatch(path, facecolor="none", edgecolor=color,
                           lw=lw, alpha=alpha, zorder=zorder + 1))


def build():
    fig, ax = plt.subplots(figsize=(13, 10), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 14, 0, 11], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 14, 1.6,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # =============================================================
    # (A) Left stack: 11 input constraint orbs
    # =============================================================
    col_x = 1.6
    # Top group = 4 axioms (A1–A4), bottom group = 7 principles (P1–P7)
    y_axiom = np.linspace(9.2, 7.4, 4)
    y_princ = np.linspace(6.4, 1.9, 7)

    axiom_colors = [
        ("#4fa3d8", "#9bd3ea"),   # A1 non-negativity — cool blue
        ("#ffb347", "#ffd98a"),   # A2 null baseline — amber
        ("#2fb27a", "#b6e7cf"),   # A3 monotonicity — green
        ("#8a5ac9", "#c8aff0"),   # A4 subadditivity — violet
    ]
    princ_colors = [
        ("#1aa6c7", "#9fe6f3"),   # P1 operator structure — cyan
        ("#d69a1a", "#ffd98a"),   # P2 channel complementarity — amber
        ("#c23b3b", "#f1a1a1"),   # P3 penalty equilibrium — red
        ("#5b6b80", "#c9d4e0"),   # P4 mobility capacity — steel
        ("#b57b12", "#f1c279"),   # P5 participation feedback — dark amber
        ("#2f8fb3", "#9cd0e3"),   # P6 damping discriminant — teal-blue
        ("#6a3fb0", "#c8aff0"),   # P7 nonlinear triad — purple
    ]

    axiom_pts = []
    princ_pts = []

    # divider band between the two groups (subtle)
    for dy, a in [(0.26, 0.04), (0.18, 0.08), (0.10, 0.18)]:
        ax.add_patch(Rectangle(
            (col_x - 0.95, 6.95 - dy / 2),
            1.9, dy,
            facecolor="#1f3b57", edgecolor="none",
            alpha=a, zorder=1,
        ))

    # axioms
    for (core, halo), y in zip(axiom_colors, y_axiom):
        glowing_orb(ax, col_x, y, r=0.30,
                    core=core, halo=halo, zorder=9)
        axiom_pts.append((col_x, y))

    # principles
    for (core, halo), y in zip(princ_colors, y_princ):
        glowing_orb(ax, col_x, y, r=0.30,
                    core=core, halo=halo, zorder=9)
        princ_pts.append((col_x, y))

    # =============================================================
    # (B) Central lens / prism (convergence point)
    # =============================================================
    lens_cx, lens_cy = 7.3, 5.6
    lens_R = 0.95

    # wide radial halo behind the prism
    for rr, a in [(4.2, 0.03), (3.0, 0.06), (2.1, 0.12),
                  (1.5, 0.22), (1.10, 0.38), (0.80, 0.60)]:
        ax.add_patch(Circle((lens_cx, lens_cy), rr,
                            facecolor="#ffd24a", edgecolor="none",
                            alpha=a, zorder=2))

    # rays of light bursting out from the prism (behind all)
    for ang_deg in np.linspace(0, 360, 24, endpoint=False):
        th = np.deg2rad(ang_deg)
        r0 = lens_R + 0.1
        r1 = lens_R + 2.4
        x0 = lens_cx + r0 * np.cos(th)
        y0 = lens_cy + r0 * np.sin(th)
        x1 = lens_cx + r1 * np.cos(th)
        y1 = lens_cy + r1 * np.sin(th)
        ax.plot([x0, x1], [y0, y1],
                color="#ffd98a", lw=2.2, alpha=0.25,
                solid_capstyle="round", zorder=2)

    # prism body — a hexagonal star
    n_pts = 6
    outer = 0.95
    inner = 0.42
    pts = []
    for k in range(n_pts * 2):
        r = outer if k % 2 == 0 else inner
        th = np.pi / 2 + k * np.pi / n_pts
        pts.append((lens_cx + r * np.cos(th),
                    lens_cy + r * np.sin(th)))
    ax.add_patch(Polygon(pts, closed=True,
                         facecolor="#fff7d6",
                         edgecolor="#c97a10",
                         lw=2.4, zorder=7))
    # inner disc
    ax.add_patch(Circle((lens_cx, lens_cy), 0.35,
                        facecolor="white",
                        edgecolor="#c97a10",
                        lw=2.0, zorder=8))
    # tiny center point
    ax.add_patch(Circle((lens_cx, lens_cy), 0.09,
                        facecolor="#c97a10", edgecolor="none",
                        zorder=9))

    # =============================================================
    # (C) Convergence flow-lines from orbs to lens
    # =============================================================
    lens_entry_x = lens_cx - lens_R * 0.92
    for (p, (core, halo)) in zip(axiom_pts + princ_pts,
                                  axiom_colors + princ_colors):
        p0 = (p[0] + 0.32, p[1])
        # aim at a fan of entry points on the lens left side, matching y
        # so the flow pattern fans naturally
        y_targ = lens_cy + (p[1] - 5.55) * 0.12
        p1 = (lens_entry_x, y_targ)
        bezier(ax, p0, p1, color=core, halo=halo,
               lw=2.6, alpha=0.95, zorder=5)

    # =============================================================
    # (D) Output beam + the unique PDE orb (right side)
    # =============================================================
    # bright horizontal beam
    beam_x0 = lens_cx + lens_R * 0.95
    beam_y = lens_cy
    beam_x1 = 12.3

    for lw, col, a in [(45, "#fff2b0", 0.07),
                       (32, "#ffe48a", 0.12),
                       (22, "#ffd24a", 0.20),
                       (14, "#ffb347", 0.32),
                       (8, "#ff9f1a", 0.60)]:
        ax.plot([beam_x0, beam_x1], [beam_y, beam_y],
                color=col, lw=lw, alpha=a,
                solid_capstyle="round", zorder=4)
    # crisp core beam
    ax.plot([beam_x0, beam_x1], [beam_y, beam_y],
            color="#fff1b0", lw=3.0, alpha=0.95,
            solid_capstyle="round", zorder=6)

    # the unique PDE orb at the right — the culmination
    pde_x, pde_y = 12.4, beam_y
    # big halo
    for rr, a in [(1.80, 0.05), (1.40, 0.10), (1.05, 0.18),
                  (0.78, 0.30), (0.58, 0.48), (0.44, 0.70)]:
        ax.add_patch(Circle((pde_x, pde_y), rr,
                            facecolor="#ffd24a", edgecolor="none",
                            alpha=a, zorder=5))
    # outer ring
    ax.add_patch(Circle((pde_x, pde_y), 0.62,
                        facecolor="#fff7d6",
                        edgecolor="#c97a10", lw=3.0, zorder=8))
    # inner glowing core
    for rr, col in [(0.52, "#ffdf85"),
                    (0.40, "#ffc23a"),
                    (0.28, "#ff9f1a"),
                    (0.18, "#e07b00")]:
        ax.add_patch(Circle((pde_x - 0.02, pde_y + 0.02), rr,
                            facecolor=col, edgecolor="none", zorder=9))
    # crown highlight
    ax.add_patch(Circle((pde_x - 0.16, pde_y + 0.18), 0.13,
                        facecolor="white", alpha=0.82, zorder=10))

    # =============================================================
    # (E) Ghost "alternative PDE" orbs — ruled out
    # =============================================================
    def ghost_alt(gx, gy):
        # faint orb
        ax.add_patch(Circle((gx, gy), 0.42,
                            facecolor="#dcdee3",
                            edgecolor="#8a8e96",
                            lw=1.6, alpha=0.55, zorder=6))
        ax.add_patch(Circle((gx - 0.12, gy + 0.14), 0.12,
                            facecolor="white", alpha=0.45, zorder=7))
        # red circle-slash
        ax.add_patch(Circle((gx, gy), 0.54,
                            facecolor="none",
                            edgecolor="#c23b3b", lw=2.4,
                            alpha=0.85, zorder=11))
        ax.plot([gx - 0.38, gx + 0.38],
                [gy + 0.38, gy - 0.38],
                color="#c23b3b", lw=2.6, alpha=0.85, zorder=12,
                solid_capstyle="round")

    # two above the beam, two below
    ghost_alt(10.3, beam_y + 2.2)
    ghost_alt(11.9, beam_y + 2.7)
    ghost_alt(10.3, beam_y - 2.2)
    ghost_alt(11.9, beam_y - 2.7)

    # faint lines from lens to each ghost, then "stopped"
    for gx, gy in [(10.3, beam_y + 2.2),
                   (11.9, beam_y + 2.7),
                   (10.3, beam_y - 2.2),
                   (11.9, beam_y - 2.7)]:
        ax.plot([beam_x0 + 0.2, gx - 0.55],
                [beam_y, gy],
                color="#8a8e96", lw=1.4, alpha=0.35,
                linestyle=(0, (3, 4)), zorder=4)

    # =============================================================
    # (F) corner sentinel glyph — a "1" indicator on the output beam
    #     (no text: we use a stylized single tally mark circled)
    # =============================================================
    oneg_x, oneg_y = pde_x, pde_y - 1.55
    ax.add_patch(Circle((oneg_x, oneg_y), 0.32,
                        facecolor="white",
                        edgecolor="#c97a10", lw=2.2, zorder=10))
    ax.plot([oneg_x, oneg_x],
            [oneg_y - 0.17, oneg_y + 0.17],
            color="#c97a10", lw=3.2, zorder=11,
            solid_capstyle="round")
    # small dashed arrow from tally to PDE orb
    ax.annotate("",
                xy=(pde_x - 0.05, pde_y - 0.55),
                xytext=(oneg_x + 0.05, oneg_y + 0.25),
                arrowprops=dict(arrowstyle="-|>",
                                color="#c97a10", lw=1.8,
                                linestyle=(0, (3, 2)),
                                alpha=0.8),
                zorder=10)

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
