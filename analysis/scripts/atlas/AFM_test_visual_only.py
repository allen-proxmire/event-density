"""
AFM test — visual-only illustration.

Prediction: scanning a Casimir-like 2D substrate with an AFM yields a
height/potential map whose motif-conditioned field-space Hessian median
(ED-SC 2.0 invariant) lands at r* ≈ −1.304 — matching Scenario D and
the Local Group mass sheet.

Composition:
  TOP-LEFT : stylized AFM — triangular cantilever with a probe tip
             hovering over a 2D substrate.  A dashed scan path shows
             the tip traversing the substrate.
  MAIN     : the measured 2D field (warm-violet topography) showing
             saddles and micro-features.  A few cross-hair glyphs mark
             detected saddle points.
  RIGHT    : a histogram panel showing the measured ℛ_motif distribution
             peaking on the glowing violet r* ≈ −1.304 line — the
             ED-SC 2.0 prediction overlay.
  CORNER   : pending hourglass badge.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, Ellipse, FancyArrowPatch, Polygon,
)
from matplotlib.colors import LinearSegmentedColormap
from scipy.ndimage import gaussian_filter

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\AFM_test.png"


def build():
    fig, ax = plt.subplots(figsize=(13, 9), dpi=220)

    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 14, 0, 10], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 14, 1.5,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # =============================================================
    # Main scanned-surface panel
    # =============================================================
    sx0, sx1 = 0.8, 8.2
    sy0, sy1 = 2.0, 6.8

    # substrate frame
    for pad, a in [(0.25, 0.06), (0.14, 0.14), (0.07, 0.26)]:
        ax.add_patch(FancyBboxPatch(
            (sx0 - pad, sy0 - pad),
            sx1 - sx0 + 2 * pad, sy1 - sy0 + 2 * pad,
            boxstyle="round,pad=0.02,rounding_size=0.18",
            facecolor="#c8aff0", edgecolor="none",
            alpha=a, zorder=1,
        ))

    # generate 2D topographic field
    rng = np.random.default_rng(7)
    Nf = 420
    noise = rng.normal(0, 1, (Nf, Nf))
    large = gaussian_filter(noise, sigma=18) * 6.0
    mid = gaussian_filter(noise, sigma=7) * 3.0
    small = gaussian_filter(noise, sigma=1.3) * 0.55
    proto = np.zeros_like(noise)
    for _ in range(10):
        xp = rng.uniform(0.15, 0.85) * Nf
        yp = rng.uniform(0.15, 0.85) * Nf
        amp = rng.uniform(2.0, 5.5)
        sig = rng.uniform(7, 18)
        yy, xx = np.meshgrid(np.arange(Nf), np.arange(Nf), indexing="ij")
        proto += amp * np.exp(-((xx - xp) ** 2 + (yy - yp) ** 2)
                                / (2 * sig ** 2))
    field = large + mid + small + proto
    field = (field - field.min()) / (field.max() - field.min())

    cmap_afm = LinearSegmentedColormap.from_list(
        "afm_map",
        [(0.00, (0.10, 0.08, 0.22, 1.00)),
         (0.25, (0.26, 0.14, 0.40, 1.00)),
         (0.45, (0.48, 0.22, 0.56, 1.00)),
         (0.65, (0.76, 0.38, 0.58, 1.00)),
         (0.85, (1.00, 0.68, 0.40, 1.00)),
         (1.00, (1.00, 0.95, 0.72, 1.00))],
    )
    ax.imshow(field, extent=[sx0, sx1, sy0, sy1],
              origin="lower", cmap=cmap_afm, alpha=0.92,
              interpolation="bilinear", zorder=2)

    # contour overlay
    x_grid = np.linspace(sx0, sx1, Nf)
    y_grid = np.linspace(sy0, sy1, Nf)
    Xg, Yg = np.meshgrid(x_grid, y_grid)
    ax.contour(Xg, Yg, field,
               levels=np.linspace(0.25, 0.9, 7),
               colors="#ffd98a", linewidths=0.7,
               alpha=0.35, zorder=3)

    # substrate frame (crisp)
    ax.add_patch(FancyBboxPatch(
        (sx0, sy0), sx1 - sx0, sy1 - sy0,
        boxstyle="round,pad=0.02,rounding_size=0.18",
        facecolor="none", edgecolor="#8a5ac9",
        lw=2.6, zorder=4,
    ))

    # corner brackets
    bracket_len = 0.35
    for (bx, by, dx, dy) in [
        (sx0, sy0, +1, +1), (sx1, sy0, -1, +1),
        (sx0, sy1, +1, -1), (sx1, sy1, -1, -1),
    ]:
        ax.plot([bx, bx + dx * bracket_len], [by, by],
                color="#fff1b0", lw=2.6, alpha=0.95,
                solid_capstyle="round", zorder=5)
        ax.plot([bx, bx], [by, by + dy * bracket_len],
                color="#fff1b0", lw=2.6, alpha=0.95,
                solid_capstyle="round", zorder=5)

    # saddle detection → cross-hair glyphs
    dy_ = np.gradient(field, axis=0)
    dx_ = np.gradient(field, axis=1)
    dxx = np.gradient(dx_, axis=1)
    dyy = np.gradient(dy_, axis=0)
    dxy = np.gradient(dx_, axis=0)
    det_H = dxx * dyy - dxy ** 2
    grad_mag = np.hypot(dx_, dy_)

    field_mask = field > 0.30
    margin = Nf // 10
    interior = np.zeros_like(field, dtype=bool)
    interior[margin:Nf - margin, margin:Nf - margin] = True
    eligible = field_mask & interior & (det_H < -5e-7)
    score = np.where(eligible, (-det_H) / (grad_mag + 1e-3), -np.inf)

    candidates = []
    work = score.copy()
    min_sep = 1.2
    for _ in range(4):
        idx = np.unravel_index(np.argmax(work), work.shape)
        if work[idx] == -np.inf:
            break
        i_s, j_s = idx
        gx = x_grid[j_s]; gy = y_grid[i_s]
        candidates.append((gx, gy))
        rx_pix = int(min_sep * Nf / (sx1 - sx0))
        ry_pix = int(min_sep * Nf / (sy1 - sy0))
        i0 = max(0, i_s - ry_pix); i1 = min(Nf, i_s + ry_pix + 1)
        j0 = max(0, j_s - rx_pix); j1 = min(Nf, j_s + rx_pix + 1)
        work[i0:i1, j0:j1] = -np.inf

    for (ssx, ssy) in candidates:
        ax.add_patch(Ellipse((ssx, ssy), 0.50, 0.16,
                             angle=20, facecolor="none",
                             edgecolor="#e6d6ff", lw=1.8,
                             alpha=0.95, zorder=8))
        ax.add_patch(Ellipse((ssx, ssy), 0.16, 0.50,
                             angle=20, facecolor="none",
                             edgecolor="#e6d6ff", lw=1.8,
                             alpha=0.95, zorder=8))
        for rr, a in [(0.14, 0.22), (0.09, 0.50)]:
            ax.add_patch(Circle((ssx, ssy), rr,
                                facecolor="#c8aff0",
                                edgecolor="none", alpha=a, zorder=9))
        ax.add_patch(Circle((ssx, ssy), 0.06,
                            facecolor="#6a3fb0",
                            edgecolor="white", lw=1.0, zorder=10))

    # =============================================================
    # AFM cantilever + tip
    # =============================================================
    # cantilever base (above the substrate)
    cant_x0 = sx0 + 0.30
    cant_base_y = sy1 + 1.35
    cant_len = 2.0
    cant_tip_x = cant_x0 + cant_len
    cant_tip_y = cant_base_y - 0.25

    # cantilever beam (triangular strip)
    beam = [(cant_x0, cant_base_y + 0.15),
            (cant_x0, cant_base_y - 0.15),
            (cant_tip_x, cant_tip_y + 0.03),
            (cant_tip_x, cant_tip_y - 0.03)]
    ax.add_patch(Polygon(beam, closed=True,
                         facecolor="#c9d4e0",
                         edgecolor="#2f4d6b", lw=2.0, zorder=10))
    # cantilever holder block
    ax.add_patch(FancyBboxPatch(
        (cant_x0 - 0.55, cant_base_y - 0.40),
        0.65, 0.80,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        facecolor="#2f4d6b", edgecolor="#142536",
        lw=2.0, zorder=10,
    ))
    # probe tip (sharp triangle pointing down)
    tip_y_bottom = sy1 + 0.15
    tip = [(cant_tip_x, cant_tip_y),
           (cant_tip_x - 0.22, cant_tip_y - 0.15),
           (cant_tip_x + 0.22, cant_tip_y - 0.15),
           (cant_tip_x, tip_y_bottom)]
    ax.add_patch(Polygon(tip, closed=True,
                         facecolor="#5b6b80",
                         edgecolor="#142536", lw=1.8, zorder=11))
    # laser dot on cantilever (typical AFM detail)
    ax.add_patch(Circle((cant_tip_x - 0.35, cant_base_y + 0.05),
                        0.10,
                        facecolor="#ff4040",
                        edgecolor="#7a1d1d", lw=1.0,
                        alpha=0.95, zorder=12))
    for rr, a in [(0.22, 0.15), (0.15, 0.35)]:
        ax.add_patch(Circle((cant_tip_x - 0.35, cant_base_y + 0.05), rr,
                            facecolor="#ff8080",
                            edgecolor="none", alpha=a, zorder=11))

    # dashed scan path across the substrate
    scan_y_offsets = np.linspace(sy0 + 0.45, sy1 - 0.45, 5)
    for i, yy in enumerate(scan_y_offsets):
        direction = +1 if i % 2 == 0 else -1
        x_a = sx0 + 0.35 if direction > 0 else sx1 - 0.35
        x_b = sx1 - 0.35 if direction > 0 else sx0 + 0.35
        ax.plot([x_a, x_b], [yy, yy],
                color="#ff4040", lw=1.2, alpha=0.55,
                linestyle=(0, (4, 3)), zorder=6)

    # dashed arrow from tip down to a scan point
    ax.annotate("",
                xy=(cant_tip_x, sy1 + 0.02),
                xytext=(cant_tip_x, cant_tip_y - 0.20),
                arrowprops=dict(arrowstyle="-|>",
                                color="#ff4040", lw=1.6, alpha=0.7),
                zorder=11)

    # =============================================================
    # RIGHT panel: ℛ_motif histogram with r* prediction line
    # =============================================================
    px0, px1 = 8.9, 13.6
    py0, py1 = 2.0, 6.8

    ax.add_patch(FancyBboxPatch(
        (px0, py0), px1 - px0, py1 - py0,
        boxstyle="round,pad=0.04,rounding_size=0.20",
        facecolor="white", edgecolor="#1f3b57",
        lw=1.6, alpha=0.94, zorder=2,
    ))

    ax_x0 = px0 + 0.40
    ax_x1 = px1 - 0.25
    ax_y0 = py0 + 0.55
    ax_y_top = py1 - 0.30

    ax.plot([ax_x0, ax_x1], [ax_y0, ax_y0],
            color="#1f3b57", lw=1.6, alpha=0.85, zorder=4)
    # x-tick hints at -2, -1, 0
    def r_to_x(r_val):
        t = (r_val + 2.0) / 2.0
        return ax_x0 + t * (ax_x1 - ax_x0)
    for r_val in [-2.0, -1.5, -1.0, -0.5, 0.0]:
        xt = r_to_x(r_val)
        ax.plot([xt, xt], [ax_y0 - 0.10, ax_y0 + 0.10],
                color="#1f3b57", lw=1.4, alpha=0.6, zorder=4)

    # r* universal violet line
    r_star = -1.304
    rx_line = r_to_x(r_star)
    for rr, a in [(1.3, 0.06), (0.85, 0.13),
                  (0.55, 0.22), (0.35, 0.38)]:
        ax.add_patch(Circle((rx_line, (ax_y0 + ax_y_top) / 2), rr,
                            facecolor="#c8aff0",
                            edgecolor="none", alpha=a, zorder=3))
    for gw, a in [(0.55, 0.10), (0.35, 0.18),
                  (0.22, 0.30), (0.12, 0.50)]:
        ax.add_patch(Rectangle(
            (rx_line - gw / 2, ax_y0),
            gw, ax_y_top - ax_y0,
            facecolor="#b48cef", edgecolor="none",
            alpha=a, zorder=3,
        ))
    ax.plot([rx_line, rx_line], [ax_y0, ax_y_top + 0.30],
            color="#6a3fb0", lw=4.0,
            solid_capstyle="round", zorder=6)
    ax.plot([rx_line, rx_line], [ax_y0, ax_y_top + 0.30],
            color="#e6d6ff", lw=1.4,
            solid_capstyle="round", zorder=7)

    # r* star-badge
    bcx, bcy = rx_line, ax_y_top + 0.60
    for rr, a in [(0.42, 0.12), (0.30, 0.25)]:
        ax.add_patch(Circle((bcx, bcy), rr,
                            facecolor="#c8aff0",
                            edgecolor="none", alpha=a, zorder=9))
    ax.add_patch(Circle((bcx, bcy), 0.28,
                        facecolor="white", edgecolor="#6a3fb0",
                        lw=2.2, zorder=10))
    npts = 5
    sp = []
    for k in range(npts * 2):
        rr = 0.20 if k % 2 == 0 else 0.09
        th = np.pi / 2 + k * np.pi / npts
        sp.append((bcx + rr * np.cos(th), bcy + rr * np.sin(th)))
    ax.add_patch(Polygon(sp, closed=True,
                         facecolor="#6a3fb0",
                         edgecolor="#4a1e85", lw=1.2, zorder=11))

    # measured ℛ_motif distribution (violin peaking at r*)
    r_vals = np.linspace(-2.05, 0.05, 500)
    pdf = np.exp(-((r_vals + 1.30) ** 2) / (2 * 0.28 ** 2))
    pdf = pdf / pdf.max()
    xs_c = np.array([r_to_x(rv) for rv in r_vals])
    max_h = (ax_y_top - ax_y0) * 0.82
    ys_c = ax_y0 + pdf * max_h
    ax.fill_between(xs_c, ax_y0, ys_c,
                    color="#c8aff0", alpha=0.45, zorder=4)
    for lw, a in [(8, 0.12), (5, 0.22)]:
        ax.plot(xs_c, ys_c, color="#c8aff0", lw=lw, alpha=a,
                solid_capstyle="round", zorder=5)
    ax.plot(xs_c, ys_c, color="#6a3fb0", lw=2.6,
            solid_capstyle="round", zorder=6)

    # data-ish scatter dots on the histogram
    rng2 = np.random.default_rng(33)
    for _ in range(40):
        rv = rng2.normal(-1.30, 0.30)
        if rv > 0 or rv < -2.0:
            continue
        xv = r_to_x(rv)
        # place at a random height under the curve
        pdf_here = np.exp(-((rv + 1.30) ** 2) / (2 * 0.28 ** 2))
        y_max_here = ax_y0 + (pdf_here / pdf.max()) * max_h
        yv = rng2.uniform(ax_y0 + 0.05, y_max_here - 0.08)
        ax.add_patch(Circle((xv, yv), 0.05,
                            facecolor="#8a5ac9",
                            edgecolor="white", lw=0.6,
                            alpha=0.75, zorder=7))

    # x-axis tick at r*
    ax.plot([rx_line, rx_line], [ax_y0 - 0.22, ax_y0 + 0.08],
            color="#6a3fb0", lw=2.4, zorder=7,
            solid_capstyle="round")
    ax.add_patch(Circle((rx_line, ax_y0 - 0.36), 0.11,
                        facecolor="#e6d6ff",
                        edgecolor="#6a3fb0", lw=1.6, zorder=8))

    # =============================================================
    # Pending hourglass badge
    # =============================================================
    hb_x, hb_y = 13.4, 9.3
    for rr, a in [(0.55, 0.10), (0.42, 0.18)]:
        ax.add_patch(Circle((hb_x, hb_y), rr,
                            facecolor="#ffd24a",
                            edgecolor="none", alpha=a, zorder=9))
    ax.add_patch(Circle((hb_x, hb_y), 0.38,
                        facecolor="white", edgecolor="#c97a10",
                        lw=2.4, zorder=10))
    hg = [(hb_x - 0.17, hb_y + 0.20),
          (hb_x + 0.17, hb_y + 0.20),
          (hb_x - 0.17, hb_y - 0.20),
          (hb_x + 0.17, hb_y - 0.20)]
    ax.plot([hg[0][0], hg[1][0]], [hg[0][1], hg[1][1]],
            color="#c97a10", lw=2.6, zorder=11)
    ax.plot([hg[2][0], hg[3][0]], [hg[2][1], hg[3][1]],
            color="#c97a10", lw=2.6, zorder=11)
    ax.plot([hg[0][0], hg[3][0]], [hg[0][1], hg[3][1]],
            color="#c97a10", lw=2.2, zorder=11)
    ax.plot([hg[1][0], hg[2][0]], [hg[1][1], hg[2][1]],
            color="#c97a10", lw=2.2, zorder=11)
    ax.add_patch(Polygon([(hb_x - 0.10, hb_y - 0.18),
                          (hb_x + 0.10, hb_y - 0.18),
                          (hb_x, hb_y - 0.02)],
                         closed=True, facecolor="#ffb347",
                         edgecolor="none", alpha=0.85, zorder=11))

    # Connector — from substrate panel into histogram panel
    ax.annotate("",
                xy=(px0 + 0.30, (py0 + py1) / 2),
                xytext=(sx1 - 0.10, (sy0 + sy1) / 2),
                arrowprops=dict(arrowstyle="-|>",
                                color="#6a3fb0", lw=2.0, alpha=0.75,
                                connectionstyle="arc3,rad=0.0",
                                linestyle=(0, (4, 3))),
                zorder=10)

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
