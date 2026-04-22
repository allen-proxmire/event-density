"""
ED-SC 2.0 Invariant — visual-only illustration.

Metaphor: three wildly different systems, one universal curvature
signature.  The motif-conditioned median of ∇²E Hessian-eigenvalue
ratios lands at the same negative value r* ≈ −1.304 regardless of
system.

Composition:
  TOP ROW    : three small "system" saddle-landscape badges.
    LEFT     — Scenario D (ED simulation) — a stylized saddle surface
    MIDDLE   — Local Group mass sheet (cosmological) — wider saddle with
               a small galaxy-pair dot at the stationary point
    RIGHT    — Casimir cavity (nanoscale) — two parallel plates with a
               small equilibrium dot between them
  MAIN PANEL : a histogram-overlay plot.  Three violin/distribution
               shapes for the ℛ_motif distributions of each system —
               cyan (Scenario D), green (Local Group), amber (Casimir)
               — ALL with their medians landing on the same glowing
               violet vertical line r* ≈ −1.304.
  Below the histogram: a horizontal axis representing the signed
  Hessian-ratio ℛ from −2.0 to 0.  The violet band at r* is emphasized
  with a radial halo + vertical glow strip.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch, Polygon, Ellipse,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\EDSC2.png"


def saddle_badge(ax, cx, cy, R=1.00, color_a="#9fe6f3",
                 color_b="#1aa6c7", outline="#0b4a68",
                 bg_face="#eaf4fb", bg_edge="#1aa6c7"):
    """A stylized saddle-shape icon in a rounded badge.
    Drawn via an ellipse pair with crossing iso-contour ovals.
    """
    # badge frame
    for p, a in [(0.25, 0.06), (0.16, 0.12), (0.08, 0.22)]:
        ax.add_patch(Circle((cx, cy), R + p,
                            facecolor=bg_edge, edgecolor="none",
                            alpha=a, zorder=3))
    ax.add_patch(Circle((cx, cy), R,
                        facecolor=bg_face, edgecolor=bg_edge,
                        lw=2.4, zorder=4))

    # saddle iso-contours: two ellipse families crossing at center
    # ellipses elongated along x: "valleys" (positive curvature axis)
    # ellipses elongated along y: "ridges"
    for scale in [0.25, 0.50, 0.78]:
        # horizontal saddle curves (ridge lines)
        ax.add_patch(Ellipse((cx, cy), R * scale * 2.2, R * scale * 0.6,
                             facecolor="none", edgecolor=color_a,
                             lw=1.6, alpha=0.75, zorder=5))
        ax.add_patch(Ellipse((cx, cy), R * scale * 0.6, R * scale * 2.2,
                             facecolor="none", edgecolor=color_b,
                             lw=1.6, alpha=0.75, zorder=5))
    # central stationary-point dot
    ax.add_patch(Circle((cx, cy), 0.10,
                        facecolor=outline, edgecolor="white",
                        lw=1.2, zorder=7))


def scene_cosmological(ax, cx, cy, R=1.00):
    """Cosmological saddle — wider ellipses + small galaxy-pair dots."""
    saddle_badge(ax, cx, cy, R,
                 color_a="#b6e7cf", color_b="#2fb27a",
                 outline="#1b6f4a",
                 bg_face="#ecf9ec", bg_edge="#2fb27a")
    # two small "galaxy" dots offset from stationary point
    for dx in [-0.28, +0.28]:
        ax.add_patch(Circle((cx + dx, cy), 0.07,
                            facecolor="#fff1b0",
                            edgecolor="#2fb27a", lw=1.0,
                            zorder=8))
        ax.add_patch(Circle((cx + dx, cy), 0.12,
                            facecolor="none", edgecolor="#2fb27a",
                            lw=0.8, alpha=0.5, zorder=8))


def scene_casimir(ax, cx, cy, R=1.00):
    """Casimir saddle — rendered as two parallel plates + eq-point dot."""
    # badge frame
    for p, a in [(0.25, 0.06), (0.16, 0.12), (0.08, 0.22)]:
        ax.add_patch(Circle((cx, cy), R + p,
                            facecolor="#ffb347", edgecolor="none",
                            alpha=a, zorder=3))
    ax.add_patch(Circle((cx, cy), R,
                        facecolor="#fff2dc", edgecolor="#c97a10",
                        lw=2.4, zorder=4))
    # top plate
    ax.add_patch(Rectangle((cx - R * 0.65, cy + R * 0.35),
                           R * 1.30, R * 0.14,
                           facecolor="#d69a1a",
                           edgecolor="#7a4a0a", lw=1.6, zorder=6))
    # bottom plate
    ax.add_patch(Rectangle((cx - R * 0.65, cy - R * 0.49),
                           R * 1.30, R * 0.14,
                           facecolor="#d69a1a",
                           edgecolor="#7a4a0a", lw=1.6, zorder=6))
    # faint cavity shading
    ax.add_patch(Rectangle((cx - R * 0.60, cy - R * 0.33),
                           R * 1.20, R * 0.68,
                           facecolor="#ffe9b0",
                           edgecolor="none", alpha=0.5, zorder=5))
    # saddle iso-contours inside the cavity (horizontal ellipses +
    # vertical ovals cross at the equilibrium point)
    for scale in [0.22, 0.45]:
        ax.add_patch(Ellipse((cx, cy), R * scale * 1.7, R * scale * 0.28,
                             facecolor="none", edgecolor="#ff9f1a",
                             lw=1.4, alpha=0.7, zorder=7))
        ax.add_patch(Ellipse((cx, cy), R * scale * 0.28, R * scale * 0.6,
                             facecolor="none", edgecolor="#c97a10",
                             lw=1.4, alpha=0.7, zorder=7))
    # equilibrium dot
    ax.add_patch(Circle((cx, cy), 0.10,
                        facecolor="#7a4a0a", edgecolor="white",
                        lw=1.2, zorder=9))


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
    # Top row: three system badges
    # =============================================================
    top_y = 9.0
    badge_R = 0.95
    # Scenario D (cyan)
    sd_x = 2.7
    saddle_badge(ax, sd_x, top_y, R=badge_R,
                 color_a="#9fe6f3", color_b="#1aa6c7",
                 outline="#0b4a68",
                 bg_face="#eaf4fb", bg_edge="#1aa6c7")

    # Local Group (green)
    lg_x = 7.0
    scene_cosmological(ax, lg_x, top_y, R=badge_R)

    # Casimir (amber)
    cas_x = 11.3
    scene_casimir(ax, cas_x, top_y, R=badge_R)

    # =============================================================
    # Main panel: histogram overlay of ℛ_motif distributions
    # =============================================================
    plot_x0, plot_x1 = 0.7, 13.3
    plot_y0, plot_y1 = 2.0, 7.3

    ax.add_patch(FancyBboxPatch(
        (plot_x0, plot_y0),
        plot_x1 - plot_x0, plot_y1 - plot_y0,
        boxstyle="round,pad=0.04,rounding_size=0.25",
        facecolor="white", edgecolor="#1f3b57",
        lw=1.6, alpha=0.94, zorder=2,
    ))

    ax_x0 = plot_x0 + 0.55
    ax_x1 = plot_x1 - 0.55
    ax_y0 = plot_y0 + 0.80
    ax_y_top = plot_y1 - 0.50

    # horizontal x-axis (ℛ from -2.0 on left to 0 on right)
    ax.plot([ax_x0, ax_x1], [ax_y0, ax_y0],
            color="#1f3b57", lw=1.8, alpha=0.85, zorder=4)
    ax.annotate("",
                xy=(ax_x1 + 0.08, ax_y0),
                xytext=(ax_x0, ax_y0),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1f3b57", lw=1.8),
                zorder=5)

    # axis tick marks at ℛ = -2, -1.5, -1, -0.5, 0
    def r_to_x(r_val):
        # map ℛ ∈ [-2, 0] to plot x
        t = (r_val - (-2.0)) / (0 - (-2.0))
        return ax_x0 + t * (ax_x1 - ax_x0)

    for r_val in [-2.0, -1.5, -1.0, -0.5, 0.0]:
        xt = r_to_x(r_val)
        ax.plot([xt, xt], [ax_y0 - 0.14, ax_y0 + 0.14],
                color="#1f3b57", lw=1.6, alpha=0.65, zorder=5)

    # gridlines
    for frac in [0.3, 0.6]:
        yh = ax_y0 + frac * (ax_y_top - ax_y0)
        ax.plot([ax_x0 + 0.02, ax_x1], [yh, yh],
                color="#1f3b57", lw=0.7, alpha=0.15,
                linestyle=(0, (4, 4)), zorder=3)

    # =============================================================
    # r* universal vertical line (bright violet)
    # =============================================================
    r_star = -1.304
    rx = r_to_x(r_star)

    # radial burst behind the line
    for rr, a in [(2.3, 0.04), (1.6, 0.08), (1.1, 0.15),
                  (0.75, 0.25), (0.50, 0.42)]:
        ax.add_patch(Circle((rx, (ax_y0 + ax_y_top) / 2), rr,
                            facecolor="#c8aff0", edgecolor="none",
                            alpha=a, zorder=3))

    # vertical glow strip
    for gw, a in [(0.70, 0.08), (0.45, 0.14),
                  (0.28, 0.24), (0.16, 0.40)]:
        ax.add_patch(Rectangle(
            (rx - gw / 2, ax_y0),
            gw, ax_y_top - ax_y0,
            facecolor="#b48cef", edgecolor="none",
            alpha=a, zorder=3,
        ))

    # the main violet line
    ax.plot([rx, rx], [ax_y0, ax_y_top + 0.3],
            color="#6a3fb0", lw=4.5,
            solid_capstyle="round", zorder=6)
    ax.plot([rx, rx], [ax_y0, ax_y_top + 0.3],
            color="#e6d6ff", lw=1.6,
            solid_capstyle="round", zorder=7)

    # badge above the r* line
    badge_cx, badge_cy = rx, ax_y_top + 0.75
    for rr, a in [(0.46, 0.10), (0.34, 0.22)]:
        ax.add_patch(Circle((badge_cx, badge_cy), rr,
                            facecolor="#c8aff0", edgecolor="none",
                            alpha=a, zorder=9))
    ax.add_patch(Circle((badge_cx, badge_cy), 0.32,
                        facecolor="white", edgecolor="#6a3fb0",
                        lw=2.4, zorder=10))
    # star glyph inside (5 pt)
    npts = 5
    star_pts = []
    for k in range(npts * 2):
        rr = 0.22 if k % 2 == 0 else 0.10
        th = np.pi / 2 + k * np.pi / npts
        star_pts.append((badge_cx + rr * np.cos(th),
                         badge_cy + rr * np.sin(th)))
    ax.add_patch(Polygon(star_pts, closed=True,
                         facecolor="#6a3fb0", edgecolor="#4a1e85",
                         lw=1.4, zorder=11))

    # small tick marker on the x-axis at r*
    ax.plot([rx, rx], [ax_y0 - 0.30, ax_y0 + 0.08],
            color="#6a3fb0", lw=3.0, zorder=8,
            solid_capstyle="round")
    for rr, a in [(0.38, 0.12), (0.26, 0.25), (0.18, 0.50)]:
        ax.add_patch(Circle((rx, ax_y0 - 0.45), rr,
                            facecolor="#c8aff0", edgecolor="none",
                            alpha=a, zorder=7))
    ax.add_patch(Circle((rx, ax_y0 - 0.45), 0.15,
                        facecolor="#e6d6ff",
                        edgecolor="#6a3fb0", lw=2.0, zorder=8))

    # =============================================================
    # Three overlaid distributions (Gaussian-like violins)
    # =============================================================
    rng_noise = np.random.default_rng(9)

    def violin_curve(center_r, width, heights_scale, color_core,
                     color_halo, lw=2.4):
        """Plot a Gaussian-shaped distribution curve (not filled
        under axis, but filled between baseline and curve)."""
        r_vals = np.linspace(-2.05, 0.05, 500)
        pdf = np.exp(-((r_vals - center_r) ** 2) / (2 * width ** 2))
        # slight asymmetric tail toward 0 for interest
        skew = 1 + 0.15 * np.tanh((r_vals - center_r) * 2)
        pdf = pdf * skew
        pdf = pdf / pdf.max()
        xs_curve = np.array([r_to_x(rv) for rv in r_vals])
        ys_curve = ax_y0 + pdf * heights_scale

        # fill
        ax.fill_between(xs_curve, ax_y0, ys_curve,
                        color=color_halo, alpha=0.40, zorder=5)
        # glow strokes
        for lw_h, a_ in [(lw + 6, 0.12),
                         (lw + 3, 0.22)]:
            ax.plot(xs_curve, ys_curve, color=color_halo,
                    lw=lw_h, alpha=a_, solid_capstyle="round",
                    zorder=6)
        ax.plot(xs_curve, ys_curve, color=color_core,
                lw=lw, alpha=0.95, solid_capstyle="round",
                zorder=7)

        # small marker at the peak = median position
        peak_idx = np.argmax(pdf)
        peak_x = xs_curve[peak_idx]
        peak_y = ys_curve[peak_idx]
        for rr, a in [(0.20, 0.25), (0.14, 0.50)]:
            ax.add_patch(Circle((peak_x, peak_y), rr,
                                facecolor=color_halo, edgecolor="none",
                                alpha=a, zorder=8))
        ax.add_patch(Circle((peak_x, peak_y), 0.10,
                            facecolor=color_core,
                            edgecolor="white", lw=1.2, zorder=9))
        return (peak_x, peak_y)

    max_h = (ax_y_top - ax_y0) * 0.82
    # All three distributions centered on r* with slightly different widths
    peak1 = violin_curve(-1.31, 0.22, max_h * 1.0,
                          color_core="#1aa6c7",
                          color_halo="#9fe6f3", lw=2.6)
    peak2 = violin_curve(-1.30, 0.28, max_h * 0.85,
                          color_core="#2fb27a",
                          color_halo="#b6e7cf", lw=2.6)
    peak3 = violin_curve(-1.29, 0.32, max_h * 0.70,
                          color_core="#c97a10",
                          color_halo="#ffd98a", lw=2.6)

    # =============================================================
    # Connectors: each top-row system badge down to its distribution
    # =============================================================
    for (sys_cx, peak_pt, col) in zip(
        [sd_x, lg_x, cas_x],
        [peak1, peak2, peak3],
        ["#1aa6c7", "#2fb27a", "#c97a10"],
    ):
        ax.plot([sys_cx, peak_pt[0]],
                [top_y - badge_R - 0.15,
                 peak_pt[1] + 0.22],
                color=col, lw=1.4, alpha=0.40,
                linestyle=(0, (4, 3)), zorder=4)
        # small arrowhead near the distribution peak
        ax.annotate("",
                    xy=(peak_pt[0], peak_pt[1] + 0.18),
                    xytext=(peak_pt[0] + (sys_cx - peak_pt[0]) * 0.12,
                            peak_pt[1] + 0.45),
                    arrowprops=dict(arrowstyle="-|>",
                                    color=col, lw=1.8,
                                    alpha=0.75),
                    zorder=5)

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
