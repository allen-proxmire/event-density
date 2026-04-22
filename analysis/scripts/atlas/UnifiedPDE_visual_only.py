"""
Unified PDE — visual-only illustration.

Metaphor: one grand, luminous enclosure holding two coupled machines.
  - LEFT  : the ρ-field "engine" — a big warm density globe with three
            satellite operator badges clinging to its rim, one for each
            term in F[ρ]:
              • cyan divergence icon       →  M(ρ)∇²ρ  (mobility diffusion)
              • violet wave-mix icon        →  M'(ρ)|∇ρ|² (nonlinear triad)
              • amber spring icon           →  −P(ρ)     (penalty)
  - RIGHT : the ν "oscillator" — a smaller amber sphere with a rising
            then settling curve icon, the participation channel, plus a
            grey decaying-curve icon for the ζν damping term.
  - BETWEEN : a thick pulsing coupling shaft with bidirectional arrows:
              top arrow   (cyan → amber)  =  F[ρ] drives ν
              bottom arrow (amber → cyan) =  H·ν  feeds back into ρ

The whole composition is enclosed in a glowing rounded frame (the
"one unified equation" box).
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch, Polygon, Ellipse,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\UnifiedPDE.png"


def spring_path(p0, p1, coils=6, amplitude=0.09):
    p0 = np.asarray(p0, float)
    p1 = np.asarray(p1, float)
    v = p1 - p0
    L = np.linalg.norm(v)
    if L == 0:
        return np.array([p0[0]]), np.array([p0[1]])
    uhat = v / L
    nhat = np.array([-uhat[1], uhat[0]])
    n = 260
    t = np.linspace(0, 1, n)
    lead, tail = 0.12, 0.88
    m = (t >= lead) & (t <= tail)
    coil_phase = np.zeros_like(t)
    tt = (t[m] - lead) / (tail - lead)
    coil_phase[m] = np.sin(2 * np.pi * coils * tt)
    amp = np.where(m, amplitude, 0.0)
    pts = (p0[:, None]
           + uhat[:, None] * (t * L)
           + nhat[:, None] * (amp * coil_phase))
    return pts[0], pts[1]


def glowing_ball(ax, x, y, r, layers, highlight=True, zorder=10):
    """Render a radially-shaded sphere from a list (r_frac, color)."""
    # soft halo first
    for rr, a in [(r * 1.9, 0.07),
                  (r * 1.5, 0.14),
                  (r * 1.22, 0.28)]:
        ax.add_patch(Circle((x, y), rr,
                            facecolor=layers[0][1],
                            edgecolor="none", alpha=a, zorder=zorder - 1))
    for frac, col in layers:
        ax.add_patch(Circle((x - 0.03 * (1 - frac),
                             y + 0.03 * (1 - frac)),
                            r * frac, facecolor=col,
                            edgecolor="none", zorder=zorder))
    if highlight:
        ax.add_patch(Circle((x - r * 0.32, y + r * 0.32),
                            r * 0.30, facecolor="white",
                            alpha=0.78, zorder=zorder + 1))


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
    # Enclosing "one equation" frame
    # =============================================================
    fx, fy, fw, fh = 0.65, 1.4, 12.7, 8.3
    # halo layers outside the frame
    for pad, a in [(0.55, 0.05), (0.38, 0.10),
                   (0.25, 0.18), (0.14, 0.30)]:
        ax.add_patch(FancyBboxPatch(
            (fx - pad, fy - pad), fw + 2 * pad, fh + 2 * pad,
            boxstyle="round,pad=0.02,rounding_size=0.55",
            facecolor="#ffd24a", edgecolor="none", alpha=a, zorder=1,
        ))
    # soft interior wash
    ax.add_patch(FancyBboxPatch(
        (fx, fy), fw, fh,
        boxstyle="round,pad=0.02,rounding_size=0.48",
        facecolor="#fffaed", edgecolor="none", alpha=0.75, zorder=2,
    ))
    # crisp frame
    ax.add_patch(FancyBboxPatch(
        (fx, fy), fw, fh,
        boxstyle="round,pad=0.02,rounding_size=0.48",
        facecolor="none", edgecolor="#c97a10", lw=3.4, zorder=3,
    ))
    # inner pin-stripe frame (double-line crest effect)
    ax.add_patch(FancyBboxPatch(
        (fx + 0.20, fy + 0.20), fw - 0.40, fh - 0.40,
        boxstyle="round,pad=0.02,rounding_size=0.40",
        facecolor="none", edgecolor="#d69a1a",
        lw=1.4, alpha=0.8, zorder=3,
    ))

    # =============================================================
    # LEFT side — ρ field engine
    # =============================================================
    rho_cx, rho_cy = 4.2, 5.6
    rho_R = 1.65

    # background iso-contour rings (density field)
    for rr, a, col in [
        (rho_R * 1.70, 0.05, "#b8dcef"),
        (rho_R * 1.45, 0.10, "#9bcde6"),
        (rho_R * 1.22, 0.18, "#6fbadb"),
        (rho_R * 1.02, 0.30, "#3fa6d0"),
        (rho_R * 0.82, 0.46, "#2791c2"),
        (rho_R * 0.64, 0.70, "#1579a8"),
        (rho_R * 0.45, 0.90, "#0f5e85"),
    ]:
        ax.add_patch(Circle((rho_cx, rho_cy), rr,
                            facecolor=col, edgecolor="none",
                            alpha=a, zorder=4))
    # core
    ax.add_patch(Circle((rho_cx, rho_cy), 0.40,
                        facecolor="#57c6e6", edgecolor="#0b4a68",
                        lw=1.8, zorder=6))
    ax.add_patch(Circle((rho_cx - 0.14, rho_cy + 0.14), 0.17,
                        facecolor="white", alpha=0.75, zorder=7))

    # faint iso-lines
    for rr in [rho_R * 0.72, rho_R * 1.00, rho_R * 1.28]:
        ax.add_patch(Circle((rho_cx, rho_cy), rr,
                            facecolor="none", edgecolor="#2a3a50",
                            lw=0.7, alpha=0.25, zorder=5))

    # ---- three operator-satellite badges around ρ -----------------
    def draw_badge(bx, by, face, edge, r=0.42, z=12):
        for rr, a in [(r * 1.45, 0.08),
                      (r * 1.22, 0.16),
                      (r * 1.08, 0.30)]:
            ax.add_patch(Circle((bx, by), rr, facecolor=edge,
                                edgecolor="none", alpha=a, zorder=z - 1))
        ax.add_patch(Circle((bx, by), r,
                            facecolor=face, edgecolor=edge,
                            lw=2.4, zorder=z))

    # positions on the rho-orbit
    orbit_R = rho_R + 1.25
    positions = []
    for ang_deg in [60, 180, 300]:  # upper, left, lower
        th = np.deg2rad(ang_deg)
        positions.append((rho_cx + orbit_R * np.cos(th),
                          rho_cy + orbit_R * np.sin(th)))

    p_div, p_triad, p_pen = positions

    # (1) divergence badge — mobility / ∇² (cyan)
    dx, dy = p_div
    draw_badge(dx, dy, "#dff3f8", "#1aa6c7", r=0.44)
    for ang in [np.pi * 0.15, np.pi * 0.50, np.pi * 0.85]:
        x0, y0 = dx - 0.10, dy - 0.10
        dx_, dy_ = 0.35 * np.cos(ang), 0.35 * np.sin(ang)
        ax.annotate("",
                    xy=(x0 + dx_, y0 + dy_),
                    xytext=(x0, y0),
                    arrowprops=dict(arrowstyle="-|>",
                                    color="#1aa6c7", lw=2.2),
                    zorder=13)

    # (2) triad / wave-mix badge — violet
    tx, ty = p_triad
    draw_badge(tx, ty, "#f1e6ff", "#6a3fb0", r=0.44)
    # three intersecting short sine segments
    colors_tri = ["#6a3fb0", "#1aa6c7", "#d69a1a"]
    for i, col in enumerate(colors_tri):
        ang = i * 2 * np.pi / 3 + np.pi / 6
        c0 = (tx + 0.28 * np.cos(ang), ty + 0.28 * np.sin(ang))
        c1 = (tx - 0.28 * np.cos(ang), ty - 0.28 * np.sin(ang))
        # a small sine across the chord
        n = 30
        t = np.linspace(0, 1, n)
        x_line = np.linspace(c0[0], c1[0], n)
        y_line = np.linspace(c0[1], c1[1], n)
        perp = np.array([-(c1[1] - c0[1]), (c1[0] - c0[0])])
        perp = perp / np.linalg.norm(perp)
        wave = 0.07 * np.sin(t * 2 * np.pi * 1.5)
        x_line += perp[0] * wave
        y_line += perp[1] * wave
        ax.plot(x_line, y_line, color=col, lw=2.2,
                solid_capstyle="round", zorder=13)
    ax.add_patch(Circle((tx, ty), 0.08,
                        facecolor="#6a3fb0", edgecolor="none", zorder=14))

    # (3) penalty spring badge — amber
    px, py = p_pen
    draw_badge(px, py, "#fff1d8", "#c97a10", r=0.44)
    xs, ys = spring_path((px - 0.30, py), (px + 0.30, py),
                         coils=4, amplitude=0.10)
    ax.plot(xs, ys, color="#c97a10", lw=2.3,
            solid_capstyle="round", zorder=13)
    ax.add_patch(Circle((px - 0.30, py), 0.06,
                        facecolor="#c97a10", edgecolor="none", zorder=14))
    ax.add_patch(Circle((px + 0.30, py), 0.06,
                        facecolor="#c97a10", edgecolor="none", zorder=14))

    # connecting lines from each badge to the rho sphere
    for (bx, by), col in zip([p_div, p_triad, p_pen],
                              ["#1aa6c7", "#6a3fb0", "#c97a10"]):
        # compute end points on sphere surface
        dx_, dy_ = bx - rho_cx, by - rho_cy
        th = np.arctan2(dy_, dx_)
        ex = rho_cx + rho_R * 1.08 * np.cos(th)
        ey = rho_cy + rho_R * 1.08 * np.sin(th)
        sx = bx - 0.42 * np.cos(th)
        sy = by - 0.42 * np.sin(th)
        # glow + line
        for lw, a in [(7, 0.10), (4.5, 0.22)]:
            ax.plot([ex, sx], [ey, sy],
                    color=col, lw=lw, alpha=a, zorder=9)
        ax.plot([ex, sx], [ey, sy],
                color=col, lw=2.2, alpha=0.85, zorder=10)

    # small "ρ" sentinel dot at the center (no text, just a highlighted point)
    ax.add_patch(Circle((rho_cx, rho_cy), 0.10,
                        facecolor="white",
                        edgecolor="#0b4a68", lw=1.2, zorder=12))

    # =============================================================
    # RIGHT side — ν oscillator
    # =============================================================
    nu_cx, nu_cy = 10.4, 5.6
    nu_R = 1.05

    # soft warm halo
    for rr, a in [(nu_R * 1.90, 0.08),
                  (nu_R * 1.55, 0.16),
                  (nu_R * 1.25, 0.32)]:
        ax.add_patch(Circle((nu_cx, nu_cy), rr,
                            facecolor="#ffd98a",
                            edgecolor="none", alpha=a, zorder=4))
    # body
    glowing_ball(ax, nu_cx, nu_cy, nu_R,
                 layers=[
                     (1.00, "#ffe9b0"),
                     (0.90, "#ffd98a"),
                     (0.76, "#ffc470"),
                     (0.62, "#ff9f1a"),
                     (0.48, "#e07b00"),
                     (0.32, "#b45a00"),
                 ],
                 highlight=True, zorder=6)

    # crisp outline
    ax.add_patch(Circle((nu_cx, nu_cy), nu_R,
                        facecolor="none",
                        edgecolor="#7a4a0a", lw=2.4, zorder=8))

    # tiny icon badges attached to ν: integrator + damping
    # integrator badge (above ν)
    ib_x, ib_y = nu_cx - 0.85, nu_cy + 1.55
    draw_badge(ib_x, ib_y, "#fff1d8", "#d69a1a", r=0.42)
    ix = np.linspace(ib_x - 0.28, ib_x + 0.28, 80)
    t_ = (ix - ix[0]) / (ix[-1] - ix[0])
    iy = ib_y - 0.18 + 0.40 * (1 - np.exp(-4 * t_))
    ax.plot(ix, iy, color="#c97a10", lw=2.3,
            solid_capstyle="round", zorder=13)

    # damping badge (below ν)
    db_x, db_y = nu_cx - 0.85, nu_cy - 1.55
    draw_badge(db_x, db_y, "#eef0f3", "#5b6b80", r=0.42)
    dx_ = np.linspace(db_x - 0.28, db_x + 0.28, 80)
    dt_ = (dx_ - dx_[0]) / (dx_[-1] - dx_[0])
    dy_ = db_y - 0.14 + 0.40 * np.exp(-3.2 * dt_)
    ax.plot(dx_, dy_, color="#5b6b80", lw=2.3,
            solid_capstyle="round", zorder=13)

    # connector lines from badges to ν
    for (bx, by), col in zip([(ib_x, ib_y), (db_x, db_y)],
                              ["#d69a1a", "#5b6b80"]):
        dx_, dy_ = bx - nu_cx, by - nu_cy
        th = np.arctan2(dy_, dx_)
        ex = nu_cx + nu_R * 1.05 * np.cos(th)
        ey = nu_cy + nu_R * 1.05 * np.sin(th)
        sx = bx - 0.42 * np.cos(th)
        sy = by - 0.42 * np.sin(th)
        for lw, a in [(7, 0.10), (4.5, 0.20)]:
            ax.plot([ex, sx], [ey, sy],
                    color=col, lw=lw, alpha=a, zorder=9)
        ax.plot([ex, sx], [ey, sy],
                color=col, lw=2.2, alpha=0.85, zorder=10)

    # "ν" sentinel dot
    ax.add_patch(Circle((nu_cx, nu_cy), 0.10,
                        facecolor="white",
                        edgecolor="#7a4a0a", lw=1.2, zorder=12))

    # =============================================================
    # CENTER — coupling shaft between ρ and ν
    # =============================================================
    shaft_x0 = rho_cx + rho_R + 0.35
    shaft_x1 = nu_cx - nu_R - 0.35
    shaft_y = rho_cy

    # shaft body (wide, pulsing look)
    for h, a in [(0.90, 0.06), (0.65, 0.12),
                 (0.45, 0.22), (0.32, 0.36)]:
        ax.add_patch(FancyBboxPatch(
            (shaft_x0, shaft_y - h / 2),
            shaft_x1 - shaft_x0, h,
            boxstyle="round,pad=0.02,rounding_size=0.15",
            facecolor="#ffd24a", edgecolor="none",
            alpha=a, zorder=5,
        ))
    # core shaft
    ax.add_patch(FancyBboxPatch(
        (shaft_x0, shaft_y - 0.22),
        shaft_x1 - shaft_x0, 0.44,
        boxstyle="round,pad=0.02,rounding_size=0.10",
        facecolor="#fff1b0", edgecolor="#c97a10", lw=2.0, zorder=7,
    ))
    # small pulsing lights along the shaft
    for i, xt in enumerate(np.linspace(shaft_x0 + 0.5, shaft_x1 - 0.5, 5)):
        ax.add_patch(Circle((xt, shaft_y), 0.10,
                            facecolor="#ff9f1a",
                            edgecolor="#7a4a0a", lw=0.9, zorder=9))
        ax.add_patch(Circle((xt, shaft_y), 0.18,
                            facecolor="#ffd24a",
                            edgecolor="none", alpha=0.4, zorder=8))

    # top arrow (ρ → ν) feed-forward
    top_arrow = FancyArrowPatch(
        (shaft_x0 + 0.1, shaft_y + 0.55),
        (shaft_x1 - 0.1, shaft_y + 0.55),
        arrowstyle="-|>", mutation_scale=22,
        color="#1aa6c7", lw=3.2, zorder=10,
    )
    ax.add_patch(top_arrow)
    # small cyan badge on the arrow showing F[ρ] icon (wave)
    ba_x, ba_y = (shaft_x0 + shaft_x1) / 2, shaft_y + 1.05
    draw_badge(ba_x, ba_y, "#dff3f8", "#1aa6c7", r=0.35, z=11)
    wx = np.linspace(ba_x - 0.22, ba_x + 0.22, 60)
    wy = ba_y + 0.10 * np.sin((wx - ba_x) * 20)
    ax.plot(wx, wy, color="#1aa6c7", lw=2.2,
            solid_capstyle="round", zorder=12)
    # thin connector
    ax.plot([ba_x, ba_x], [ba_y - 0.37, shaft_y + 0.55],
            color="#1aa6c7", lw=1.2, alpha=0.55,
            linestyle=(0, (3, 3)), zorder=10)

    # bottom arrow (ν → ρ) feedback
    bot_arrow = FancyArrowPatch(
        (shaft_x1 - 0.1, shaft_y - 0.55),
        (shaft_x0 + 0.1, shaft_y - 0.55),
        arrowstyle="-|>", mutation_scale=22,
        color="#c97a10", lw=3.2, zorder=10,
    )
    ax.add_patch(bot_arrow)
    # amber badge with "H·ν" suggestion (a scaled sphere icon)
    bb_x, bb_y = (shaft_x0 + shaft_x1) / 2, shaft_y - 1.05
    draw_badge(bb_x, bb_y, "#fff1d8", "#c97a10", r=0.35, z=11)
    ax.add_patch(Circle((bb_x, bb_y), 0.15,
                        facecolor="#ffb347", edgecolor="#7a4a0a",
                        lw=1.4, zorder=12))
    ax.add_patch(Circle((bb_x - 0.04, bb_y + 0.04), 0.06,
                        facecolor="white", alpha=0.75, zorder=13))
    ax.plot([bb_x, bb_x], [shaft_y - 0.55, bb_y + 0.37],
            color="#c97a10", lw=1.2, alpha=0.55,
            linestyle=(0, (3, 3)), zorder=10)

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
