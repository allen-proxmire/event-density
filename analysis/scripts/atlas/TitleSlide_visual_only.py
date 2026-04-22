"""
ED Title Slide — visual-only illustration.

An iconic title composition. The central glowing gold invariant core
represents the unified ED framework; an 11-orb constellation around
it encodes the four axioms + seven principles; a 3-color starburst
of rays in cyan / amber / coral evokes the three channels
(mobility / penalty / participation); scattered micro-event sparks
fill the field to reinforce "becoming."

The lower third of the canvas is a deliberate text-overlay zone: a
softly ruled amber band with decorative corner flourishes where the
user will place "Event Density" and subtitle text in the slide layer.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, Polygon, FancyArrowPatch,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\TitleSlide.png"


def invariant_core(ax, x, y, r=1.25, zorder=10):
    """Big radiant gold core, matching DimInv / UniversalInv style."""
    for rr, a in [(r * 3.8, 0.03),
                  (r * 3.0, 0.06),
                  (r * 2.3, 0.10),
                  (r * 1.8, 0.16),
                  (r * 1.45, 0.25),
                  (r * 1.20, 0.40)]:
        ax.add_patch(Circle((x, y), rr, facecolor="#ffd24a",
                            edgecolor="none", alpha=a,
                            zorder=zorder - 1))
    for rr, col in [(r * 0.95, "#fff1b0"),
                    (r * 0.82, "#ffd24a"),
                    (r * 0.65, "#ffb347"),
                    (r * 0.48, "#ff9f1a"),
                    (r * 0.32, "#e07b00"),
                    (r * 0.20, "#b45a00")]:
        ax.add_patch(Circle((x, y), rr, facecolor=col,
                            edgecolor="none", zorder=zorder))
    ax.add_patch(Circle((x - r * 0.28, y + r * 0.30), r * 0.22,
                        facecolor="white", alpha=0.82,
                        zorder=zorder + 1))
    ax.add_patch(Circle((x, y), r,
                        facecolor="none",
                        edgecolor="#c97a10", lw=2.4,
                        zorder=zorder + 2))


def glow_orb(ax, x, y, r, core, halo, edge=None, zorder=12):
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
    fig, ax = plt.subplots(figsize=(14, 10), dpi=220)

    # =============================================================
    # Deep-space backdrop, softened at the bottom for the text band
    # =============================================================
    N = 700
    grad = np.zeros((N, N, 3))
    for i in range(N):
        t = i / (N - 1)
        # top: cosmic-indigo; middle: violet-plum; bottom: warm dusk
        if t < 0.60:
            s = t / 0.60
            c_top = np.array([0.05, 0.07, 0.18])
            c_mid = np.array([0.14, 0.09, 0.24])
            c = (1 - s) * c_top + s * c_mid
        else:
            s = (t - 0.60) / 0.40
            c_mid = np.array([0.14, 0.09, 0.24])
            c_bot = np.array([0.24, 0.16, 0.20])
            c = (1 - s) * c_mid + s * c_bot
        grad[i, :, :] = c
    ax.imshow(grad, extent=[0, 14, 0, 10], aspect="auto", zorder=0)

    # =============================================================
    # Starfield — dense in the top two-thirds, sparser near the title band
    # =============================================================
    rng = np.random.default_rng(42)
    n_stars = 320
    for _ in range(n_stars):
        x = rng.uniform(0.2, 13.8)
        y = rng.uniform(3.0, 9.8)
        # denser near the top
        if rng.uniform() > (y - 3.0) / 6.8:
            continue
        r = rng.uniform(0.012, 0.055)
        a = rng.uniform(0.25, 0.92)
        col = rng.choice(["#ffffff", "#e8ecff", "#fff6d8",
                          "#d6e6ff", "#f6e0ff"])
        ax.add_patch(Circle((x, y), r,
                            facecolor=col, edgecolor="none",
                            alpha=a, zorder=1))
        if r > 0.035:
            for rr, aa in [(r * 3.5, 0.08), (r * 2.2, 0.18)]:
                ax.add_patch(Circle((x, y), rr,
                                    facecolor=col,
                                    edgecolor="none",
                                    alpha=aa, zorder=1))

    # a handful of larger "beacon" stars with cross-shaped twinkle
    for _ in range(5):
        x = rng.uniform(1.0, 13.0)
        y = rng.uniform(6.5, 9.5)
        for rr, a in [(0.25, 0.10), (0.15, 0.25), (0.08, 0.55)]:
            ax.add_patch(Circle((x, y), rr,
                                facecolor="#fff1b0",
                                edgecolor="none", alpha=a, zorder=1))
        # twinkle cross
        ax.plot([x - 0.45, x + 0.45], [y, y],
                color="#fff1b0", lw=1.0, alpha=0.35,
                solid_capstyle="round", zorder=2)
        ax.plot([x, x], [y - 0.45, y + 0.45],
                color="#fff1b0", lw=1.0, alpha=0.35,
                solid_capstyle="round", zorder=2)

    # =============================================================
    # Three-channel starburst rays
    # (cyan = mobility, amber-gold = penalty, coral = participation)
    # =============================================================
    ccx, ccy = 7.0, 6.5    # central core position (upper-middle)
    R_core = 1.25

    # three interleaved ray families
    ray_specs = [
        ("#9fe6f3", "#1aa6c7", 0),           # cyan — mobility
        ("#ffd98a", "#c97a10", np.pi / 18),  # amber — penalty
        ("#ffb894", "#c94419", np.pi / 9),   # coral — participation
    ]
    n_per_family = 20
    for halo_col, core_col, phase in ray_specs:
        for k in range(n_per_family):
            th = phase + k * 2 * np.pi / n_per_family
            r0 = R_core + 0.40
            r1 = R_core + 2.70
            x0 = ccx + r0 * np.cos(th)
            y0 = ccy + r0 * np.sin(th)
            x1 = ccx + r1 * np.cos(th)
            y1 = ccy + r1 * np.sin(th)
            # glow layer
            ax.plot([x0, x1], [y0, y1],
                    color=halo_col, lw=3.2, alpha=0.18,
                    solid_capstyle="round", zorder=3)
            ax.plot([x0, x1], [y0, y1],
                    color=core_col, lw=1.4, alpha=0.35,
                    solid_capstyle="round", zorder=4)

    # =============================================================
    # 11-orb constellation (4 axioms + 7 principles)
    # Arrange on a ring around the core.
    # =============================================================
    ring_R = 3.45
    # axiom colors (cool-leaning): blue, amber, teal-green, violet
    axiom_pal = [
        ("#4fa3d8", "#9bd3ea"),
        ("#ffb347", "#ffd98a"),
        ("#2fb27a", "#b6e7cf"),
        ("#8a5ac9", "#c8aff0"),
    ]
    # principle colors (mixed)
    princ_pal = [
        ("#1aa6c7", "#9fe6f3"),
        ("#d69a1a", "#ffd98a"),
        ("#c23b3b", "#f1a1a1"),
        ("#5b6b80", "#c9d4e0"),
        ("#b57b12", "#f1c279"),
        ("#2f8fb3", "#9cd0e3"),
        ("#6a3fb0", "#c8aff0"),
    ]
    # angles: 11 evenly spaced, starting slightly above-right
    angles = np.linspace(np.pi / 2 + 0.30,
                         np.pi / 2 + 0.30 + 2 * np.pi,
                         12)[:-1]
    # axioms first (top arc), then principles
    all_pal = axiom_pal + princ_pal

    orb_centers = []
    for th, (core, halo) in zip(angles, all_pal):
        ox = ccx + ring_R * np.cos(th)
        oy = ccy + ring_R * np.sin(th)
        # only place if not in the bottom title-band zone
        if oy < 3.5:
            # tuck orbs slightly upward if they'd overlap the title band
            oy = 3.55 + (oy - 3.5) * 0.15
        orb_centers.append((ox, oy, core, halo))
        glow_orb(ax, ox, oy, r=0.24, core=core, halo=halo,
                 edge=None, zorder=12)

    # faint connecting arc through the constellation
    orb_angles = [np.arctan2(y - ccy, x - ccx) for (x, y, _, _) in orb_centers]
    order = np.argsort(orb_angles)
    ordered_pts = [orb_centers[i] for i in order]
    # close the ring by adding the first point at the end
    xs_ring = [p[0] for p in ordered_pts] + [ordered_pts[0][0]]
    ys_ring = [p[1] for p in ordered_pts] + [ordered_pts[0][1]]
    ax.plot(xs_ring, ys_ring,
            color="#8a5ac9", lw=0.9, alpha=0.28,
            linestyle=(0, (4, 4)), zorder=3)

    # =============================================================
    # Scattered micro-event sparks (tiny colored dots in the field)
    # =============================================================
    spark_palette = [
        "#9fe6f3", "#ffd98a", "#ffae79", "#c8aff0", "#b6e7cf"
    ]
    n_sparks = 130
    for _ in range(n_sparks):
        x = rng.uniform(0.5, 13.5)
        y = rng.uniform(3.3, 9.7)
        # keep sparks outside the central orb's immediate glow
        if np.hypot(x - ccx, y - ccy) < R_core + 0.4:
            continue
        # density decreases near bottom
        if rng.uniform() > (y - 3.0) / 7.0:
            continue
        r = rng.uniform(0.025, 0.09)
        col = rng.choice(spark_palette)
        a = rng.uniform(0.30, 0.90)
        # tiny halo for some sparks
        if r > 0.06:
            ax.add_patch(Circle((x, y), r * 2.3,
                                facecolor=col,
                                edgecolor="none",
                                alpha=a * 0.22, zorder=5))
        ax.add_patch(Circle((x, y), r,
                            facecolor=col, edgecolor="white",
                            lw=0.4, alpha=a, zorder=6))

    # =============================================================
    # Central invariant core (drawn LAST so it sits on top)
    # =============================================================
    invariant_core(ax, ccx, ccy, r=R_core, zorder=15)

    # subtle "pulse" indicator at center — concentric rings
    for rr, a in [(R_core * 1.75, 0.10),
                  (R_core * 2.10, 0.06),
                  (R_core * 2.55, 0.04)]:
        ax.add_patch(Circle((ccx, ccy), rr,
                            facecolor="none", edgecolor="#fff1b0",
                            lw=1.4, alpha=a, zorder=14))

    # =============================================================
    # Bottom title-text band (decorative, text-free)
    # =============================================================
    band_y0 = 0.55
    band_y1 = 2.75
    band_x0 = 0.85
    band_x1 = 13.15

    # soft halo under the band
    for pad, a in [(0.30, 0.04), (0.18, 0.08),
                   (0.10, 0.14)]:
        ax.add_patch(FancyBboxPatch(
            (band_x0 - pad, band_y0 - pad),
            band_x1 - band_x0 + 2 * pad,
            band_y1 - band_y0 + 2 * pad,
            boxstyle="round,pad=0.02,rounding_size=0.30",
            facecolor="#ffd24a", edgecolor="none",
            alpha=a, zorder=7,
        ))
    # subtle translucent band itself — keeps inside cosmic feel
    ax.add_patch(FancyBboxPatch(
        (band_x0, band_y0),
        band_x1 - band_x0, band_y1 - band_y0,
        boxstyle="round,pad=0.02,rounding_size=0.28",
        facecolor="#1a1226", edgecolor="#c97a10",
        lw=2.8, alpha=0.78, zorder=8,
    ))
    # inner pin-stripe
    ax.add_patch(FancyBboxPatch(
        (band_x0 + 0.22, band_y0 + 0.22),
        band_x1 - band_x0 - 0.44, band_y1 - band_y0 - 0.44,
        boxstyle="round,pad=0.02,rounding_size=0.22",
        facecolor="none", edgecolor="#d69a1a",
        lw=1.0, alpha=0.75, zorder=9,
    ))

    # thin horizontal rule (decorative flourish) at top and bottom of band
    for ry in [band_y1 - 0.08, band_y0 + 0.08]:
        ax.plot([band_x0 + 0.55, band_x1 - 0.55], [ry, ry],
                color="#ffb347", lw=0.8, alpha=0.55,
                linestyle=(0, (8, 4)), zorder=10)

    # decorative corner flourishes (L-brackets)
    flourish_len = 0.60
    for (bx, by, dx, dy) in [
        (band_x0 + 0.18, band_y0 + 0.18, +1, +1),
        (band_x1 - 0.18, band_y0 + 0.18, -1, +1),
        (band_x0 + 0.18, band_y1 - 0.18, +1, -1),
        (band_x1 - 0.18, band_y1 - 0.18, -1, -1),
    ]:
        ax.plot([bx, bx + dx * flourish_len], [by, by],
                color="#fff1b0", lw=2.8, alpha=0.92,
                solid_capstyle="round", zorder=11)
        ax.plot([bx, bx], [by, by + dy * flourish_len],
                color="#fff1b0", lw=2.8, alpha=0.92,
                solid_capstyle="round", zorder=11)

    # central decorative three-dot motif in the band (cyan / amber / coral)
    # placed discreetly at the very top edge of the band so as not to
    # steal the space reserved for title text
    motif_y = band_y1 - 0.35
    motif_center_x = (band_x0 + band_x1) / 2
    for dx, col, edge in [
        (-0.60, "#1aa6c7", "#0b4a68"),
        (0.00, "#ff9f1a", "#7a4a0a"),
        (0.60, "#c94419", "#7a2d0b"),
    ]:
        for rr, a in [(0.17, 0.22), (0.12, 0.45)]:
            ax.add_patch(Circle((motif_center_x + dx, motif_y), rr,
                                facecolor=col, edgecolor="none",
                                alpha=a, zorder=11))
        ax.add_patch(Circle((motif_center_x + dx, motif_y), 0.10,
                            facecolor=col, edgecolor="white",
                            lw=1.0, zorder=12))

    # same motif as a small insignia at the band's bottom center
    insignia_y = band_y0 + 0.35
    for dx, col, edge in [
        (-0.30, "#1aa6c7", "#0b4a68"),
        (0.00, "#ff9f1a", "#7a4a0a"),
        (0.30, "#c94419", "#7a2d0b"),
    ]:
        ax.add_patch(Circle((motif_center_x + dx, insignia_y), 0.06,
                            facecolor=col, edgecolor="white",
                            lw=0.6, zorder=12))

    # Downward beam from the central core into the band (visual anchor)
    # very subtle, to tie the cosmic composition to the title zone
    ax.plot([ccx, motif_center_x],
            [ccy - R_core - 0.30, band_y1 + 0.10],
            color="#ffd24a", lw=1.6, alpha=0.25,
            linestyle=(0, (3, 3)), zorder=10)

    # =============================================================
    # Framing
    # =============================================================
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.tight_layout()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    plt.savefig(OUT, dpi=220, bbox_inches="tight",
                facecolor="#05060f", edgecolor="none")
    plt.close(fig)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    build()
