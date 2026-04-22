"""
Scenario D "Noisy Universe" — visual-only illustration.

Metaphor: a 2D cosmological patch seeded with random noise that has
begun coalescing into filaments, pockets, and saddle geometry.  The
rendered field shows speckles + emergent structure simultaneously —
"seeded randomness → emergent geometry."

Composition:
  • A large rendered 2D scalar field on a dark-violet cosmological
    backdrop.  The field is the sum of:
      - broad low-k structure (large-scale modes)
      - mid-k Gaussian bumps (proto-clusters, placed randomly)
      - high-k pixel noise (initial speckle seeds)
  • Iso-contour lines overlay the field to reveal filament / saddle
    geometry.
  • Several small saddle markers (cross-hair ellipse glyphs) tag the
    Hessian saddle points — the ED-SC 2.0 signature at work in a
    noisy universe.
  • A frame around the panel ("patch of universe") and a faint
    starfield in the outer backdrop.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, Ellipse, FancyArrowPatch,
)
from matplotlib.colors import LinearSegmentedColormap
from scipy.ndimage import gaussian_filter

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\ScenarioD.png"


def build():
    fig, ax = plt.subplots(figsize=(12, 10), dpi=220)

    # =============================================================
    # Deep-space backdrop
    # =============================================================
    N = 600
    grad = np.zeros((N, N, 3))
    for i in range(N):
        t = i / (N - 1)
        c_top = np.array([0.09, 0.07, 0.18])
        c_bot = np.array([0.05, 0.06, 0.14])
        grad[i, :, :] = (1 - t) * c_top + t * c_bot
    ax.imshow(grad, extent=[0, 13, 0, 11], aspect="auto", zorder=0)

    # sparse starfield in the outer region
    rng_bg = np.random.default_rng(17)
    for _ in range(160):
        x = rng_bg.uniform(0, 13)
        y = rng_bg.uniform(0, 11)
        r = rng_bg.uniform(0.015, 0.05)
        a = rng_bg.uniform(0.30, 0.85)
        ax.add_patch(Circle((x, y), r,
                            facecolor="#eceaff", edgecolor="none",
                            alpha=a, zorder=1))

    # =============================================================
    # Cosmological patch — main 2D field
    # =============================================================
    patch_x0, patch_x1 = 1.0, 12.0
    patch_y0, patch_y1 = 1.5, 9.8

    # halo around the patch frame
    for pad, a in [(0.45, 0.06), (0.30, 0.10),
                   (0.18, 0.18), (0.10, 0.30)]:
        ax.add_patch(FancyBboxPatch(
            (patch_x0 - pad, patch_y0 - pad),
            patch_x1 - patch_x0 + 2 * pad,
            patch_y1 - patch_y0 + 2 * pad,
            boxstyle="round,pad=0.02,rounding_size=0.30",
            facecolor="#c8aff0", edgecolor="none",
            alpha=a, zorder=2,
        ))

    # ---- generate the noisy cosmological field --------------------
    rng = np.random.default_rng(42)
    Nf = 520
    # base white noise
    noise = rng.normal(0, 1.0, (Nf, Nf))
    # large-scale structure: heavy gaussian blur of noise
    large = gaussian_filter(noise, sigma=22) * 8.0
    # mid-scale structure: medium blur
    mid = gaussian_filter(noise, sigma=8) * 4.0
    # small-scale noise: lightly smoothed
    small = gaussian_filter(noise, sigma=1.2) * 0.65
    # seeded proto-clusters: random Gaussians at random positions
    proto = np.zeros_like(noise)
    n_proto = 14
    xs = rng.uniform(0.12, 0.88, n_proto) * Nf
    ys = rng.uniform(0.12, 0.88, n_proto) * Nf
    amps = rng.uniform(2.5, 6.5, n_proto)
    sigs = rng.uniform(8, 22, n_proto)
    yy, xx = np.meshgrid(np.arange(Nf), np.arange(Nf), indexing="ij")
    for x0, y0, a_, s_ in zip(xs, ys, amps, sigs):
        proto += a_ * np.exp(-((xx - x0) ** 2 + (yy - y0) ** 2)
                              / (2 * s_ ** 2))

    field = large + mid + small + proto
    # normalize
    field = (field - field.min()) / (field.max() - field.min())

    # cosmological warm colormap
    cmap_cos = LinearSegmentedColormap.from_list(
        "scenarioD",
        [
            (0.00, (0.06, 0.05, 0.16, 1.00)),    # dark navy-violet
            (0.18, (0.18, 0.10, 0.32, 1.00)),
            (0.38, (0.36, 0.18, 0.52, 1.00)),
            (0.55, (0.64, 0.32, 0.60, 1.00)),
            (0.72, (0.92, 0.54, 0.45, 1.00)),
            (0.88, (1.00, 0.80, 0.40, 1.00)),
            (1.00, (1.00, 0.97, 0.78, 1.00)),    # bright gold peaks
        ],
    )

    ax.imshow(field,
              extent=[patch_x0, patch_x1, patch_y0, patch_y1],
              origin="lower",
              cmap=cmap_cos,
              alpha=0.95,
              interpolation="bilinear",
              zorder=3)

    # ---- iso-contour overlay --------------------------------------
    x_grid = np.linspace(patch_x0, patch_x1, Nf)
    y_grid = np.linspace(patch_y0, patch_y1, Nf)
    Xg, Yg = np.meshgrid(x_grid, y_grid)
    # use light contours at a range of field levels
    ax.contour(Xg, Yg, field,
               levels=np.linspace(0.25, 0.90, 8),
               colors="#ffd98a", linewidths=0.7,
               alpha=0.35, zorder=4)
    # a few thicker contours at structural levels
    ax.contour(Xg, Yg, field,
               levels=[0.45, 0.65, 0.82],
               colors=["#f0c97a", "#f4a55c", "#ffb347"],
               linewidths=[1.4, 1.6, 1.8], alpha=0.75, zorder=5)

    # =============================================================
    # Saddle-point markers
    # =============================================================
    # Hessian via finite differences on the field.
    dy_ = np.gradient(field, axis=0)
    dx_ = np.gradient(field, axis=1)
    dxx = np.gradient(dx_, axis=1)
    dyy = np.gradient(dy_, axis=0)
    dxy = np.gradient(dx_, axis=0)
    det_H = dxx * dyy - dxy ** 2
    grad_mag = np.hypot(dx_, dy_)

    # Score candidates as "saddle-ness":  -det(H) / (1 + grad_mag)
    # but only in regions with non-trivial field value to avoid the
    # empty low-signal pixels near the frame.
    field_mask = field > 0.30            # must be in real structure
    margin = Nf // 10                    # stay away from edges
    interior = np.zeros_like(field, dtype=bool)
    interior[margin:Nf - margin, margin:Nf - margin] = True
    neg_det_mask = det_H < -5e-7
    eligible = field_mask & interior & neg_det_mask

    score = np.where(eligible,
                     (-det_H) / (grad_mag + 1e-3),
                     -np.inf)

    # greedy non-max suppression to pick the top-5 well-separated saddles
    candidates = []
    work = score.copy()
    min_sep = 1.4   # data-coord separation in plot units
    # precompute data-coord maps for speed
    for _ in range(5):
        idx = np.unravel_index(np.argmax(work), work.shape)
        if work[idx] == -np.inf:
            break
        i_s, j_s = idx
        gx = x_grid[j_s]
        gy = y_grid[i_s]
        candidates.append((gx, gy))
        # suppress neighborhood
        # convert min_sep (in data units) to pixel radius
        pix_per_unit_x = Nf / (patch_x1 - patch_x0)
        pix_per_unit_y = Nf / (patch_y1 - patch_y0)
        rx_pix = int(min_sep * pix_per_unit_x)
        ry_pix = int(min_sep * pix_per_unit_y)
        i0 = max(0, i_s - ry_pix); i1 = min(Nf, i_s + ry_pix + 1)
        j0 = max(0, j_s - rx_pix); j1 = min(Nf, j_s + rx_pix + 1)
        work[i0:i1, j0:j1] = -np.inf

    for (sx, sy) in candidates:
        # small cross-hair glyph — two crossing short ellipses
        ang = 0
        # compression axis (negative curvature direction)
        ax.add_patch(Ellipse((sx, sy), 0.55, 0.18,
                             angle=20, facecolor="none",
                             edgecolor="#e6d6ff", lw=2.0,
                             alpha=0.95, zorder=8))
        ax.add_patch(Ellipse((sx, sy), 0.18, 0.55,
                             angle=20, facecolor="none",
                             edgecolor="#e6d6ff", lw=2.0,
                             alpha=0.95, zorder=8))
        # inner dot with violet halo
        for rr, a in [(0.18, 0.20), (0.12, 0.45)]:
            ax.add_patch(Circle((sx, sy), rr,
                                facecolor="#c8aff0",
                                edgecolor="none", alpha=a, zorder=9))
        ax.add_patch(Circle((sx, sy), 0.07,
                            facecolor="#6a3fb0",
                            edgecolor="white", lw=1.0, zorder=10))

    # =============================================================
    # Frame + corner accents
    # =============================================================
    ax.add_patch(FancyBboxPatch(
        (patch_x0, patch_y0),
        patch_x1 - patch_x0, patch_y1 - patch_y0,
        boxstyle="round,pad=0.02,rounding_size=0.30",
        facecolor="none", edgecolor="#8a5ac9",
        lw=3.0, zorder=6,
    ))
    # inner stripe
    ax.add_patch(FancyBboxPatch(
        (patch_x0 + 0.15, patch_y0 + 0.15),
        patch_x1 - patch_x0 - 0.30, patch_y1 - patch_y0 - 0.30,
        boxstyle="round,pad=0.02,rounding_size=0.22",
        facecolor="none", edgecolor="#c8aff0",
        lw=1.0, alpha=0.55, zorder=6,
    ))

    # corner L-brackets (like a camera frame marking cosmological patch)
    bracket_len = 0.45
    bracket_lw = 3.2
    for (bx, by, dx, dy) in [
        (patch_x0, patch_y0, +1, +1),
        (patch_x1, patch_y0, -1, +1),
        (patch_x0, patch_y1, +1, -1),
        (patch_x1, patch_y1, -1, -1),
    ]:
        ax.plot([bx, bx + dx * bracket_len], [by, by],
                color="#fff1b0", lw=bracket_lw, alpha=0.95,
                solid_capstyle="round", zorder=9)
        ax.plot([bx, bx], [by, by + dy * bracket_len],
                color="#fff1b0", lw=bracket_lw, alpha=0.95,
                solid_capstyle="round", zorder=9)

    # faint "noise seeds" scatter dots overlaid on top (to emphasize
    # random seed origin)
    rng_seeds = np.random.default_rng(99)
    n_seeds = 120
    for _ in range(n_seeds):
        sx = rng_seeds.uniform(patch_x0 + 0.25, patch_x1 - 0.25)
        sy = rng_seeds.uniform(patch_y0 + 0.25, patch_y1 - 0.25)
        r = rng_seeds.uniform(0.015, 0.04)
        a = rng_seeds.uniform(0.15, 0.55)
        col = rng_seeds.choice(["#ffffff", "#e6d6ff", "#fff1b0"])
        ax.add_patch(Circle((sx, sy), r,
                            facecolor=col, edgecolor="none",
                            alpha=a, zorder=7))

    # ---- framing ---------------------------------------------------
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 11)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.tight_layout()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    plt.savefig(OUT, dpi=220, bbox_inches="tight",
                facecolor="#0a0a1a", edgecolor="none")
    plt.close(fig)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    build()
