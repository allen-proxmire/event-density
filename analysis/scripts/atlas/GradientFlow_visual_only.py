"""
Gradient-Driven Flow constraint — visual-only illustration.

Metaphor: a smooth scalar field with flux responding to its gradient.
Flow always points downhill; arrow density scales with steepness.

Composition:
  • A 2D scalar field rendered as a warm-to-cool heatmap (high amber
    on the left, low violet/navy on the right — a diagonal slope plus
    a ridge).
  • Iso-level contour lines overlay the field to make the topography
    legible.
  • A quiver-style grid of cyan arrows, each pointing in the downhill
    direction of the local gradient, with lengths scaled by ‖∇ρ‖.
  • Small corner badges: a hill-icon ("high") on the upper-left and a
    valley-icon ("low") on the lower-right.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch, Polygon,
)
from matplotlib.colors import LinearSegmentedColormap
from scipy.ndimage import gaussian_filter

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\GradientFlow.png"


def build():
    fig, ax = plt.subplots(figsize=(12, 10), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad_bg = np.linspace(0, 1, 500).reshape(-1, 1)
    grad_bg = np.tile(grad_bg, (1, 500))
    ax.imshow(grad_bg, extent=[0, 13, 0, 11], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 13, 1.5,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # =============================================================
    # Field panel
    # =============================================================
    fx0, fx1 = 1.0, 12.0
    fy0, fy1 = 2.0, 9.6

    # panel frame
    for pad, a in [(0.22, 0.06), (0.12, 0.14), (0.06, 0.24)]:
        ax.add_patch(FancyBboxPatch(
            (fx0 - pad, fy0 - pad),
            fx1 - fx0 + 2 * pad, fy1 - fy0 + 2 * pad,
            boxstyle="round,pad=0.02,rounding_size=0.22",
            facecolor="#c8aff0", edgecolor="none",
            alpha=a, zorder=1,
        ))

    # =============================================================
    # Scalar field: a smooth sloping ridge
    # =============================================================
    N = 400
    xs = np.linspace(fx0, fx1, N)
    ys = np.linspace(fy0, fy1, N)
    X, Y = np.meshgrid(xs, ys)

    # A ridge that falls from upper-left (high, warm) to lower-right
    # (low, cool), plus a soft Gaussian peak near the upper-left for
    # visual interest.
    slope = -(X - fx0) * 1.0 + (Y - fy0) * 0.8
    peak = 4.5 * np.exp(-((X - (fx0 + 2.6)) ** 2
                           + (Y - (fy0 + 5.4)) ** 2) / (2 * 1.8 ** 2))
    Z = slope + peak
    Z = gaussian_filter(Z, sigma=4)
    Z = (Z - Z.min()) / (Z.max() - Z.min())

    # warm-to-cool colormap tuned for the ED palette
    cmap = LinearSegmentedColormap.from_list(
        "flow_warmcool",
        [
            (0.00, (0.10, 0.08, 0.22, 1.00)),   # deep violet (low)
            (0.20, (0.22, 0.22, 0.45, 1.00)),
            (0.42, (0.42, 0.56, 0.72, 1.00)),
            (0.62, (0.90, 0.78, 0.55, 1.00)),
            (0.82, (1.00, 0.70, 0.40, 1.00)),
            (1.00, (1.00, 0.95, 0.72, 1.00)),   # bright amber (high)
        ],
    )
    ax.imshow(Z, extent=[fx0, fx1, fy0, fy1],
              origin="lower", cmap=cmap, alpha=0.95,
              interpolation="bilinear", zorder=2)

    # iso-contour lines
    ax.contour(X, Y, Z,
               levels=np.linspace(0.12, 0.92, 9),
               colors="#fff1b0", linewidths=0.8,
               alpha=0.45, zorder=3)
    # a few stronger iso-lines to read topography
    ax.contour(X, Y, Z,
               levels=[0.35, 0.60, 0.80],
               colors=["#ffd98a", "#ffb347", "#ff9f1a"],
               linewidths=[1.4, 1.6, 1.8], alpha=0.8, zorder=4)

    # panel outline
    ax.add_patch(FancyBboxPatch(
        (fx0, fy0), fx1 - fx0, fy1 - fy0,
        boxstyle="round,pad=0.02,rounding_size=0.22",
        facecolor="none", edgecolor="#1aa6c7",
        lw=3.0, zorder=5,
    ))

    # =============================================================
    # Downhill gradient-flow arrows
    # =============================================================
    # compute ∇Z on a coarser grid for arrow placement
    nx_arrows = 14
    ny_arrows = 10
    xs_q = np.linspace(fx0 + 0.6, fx1 - 0.6, nx_arrows)
    ys_q = np.linspace(fy0 + 0.6, fy1 - 0.6, ny_arrows)
    Xq, Yq = np.meshgrid(xs_q, ys_q)

    # finite-difference gradient on the fine Z grid, then sample
    dy, dx = np.gradient(Z, ys[1] - ys[0], xs[1] - xs[0])
    # map (x,y) → (i,j) indices in the fine grid
    def sample(arr, xq, yq):
        out = np.zeros_like(xq)
        for i in range(xq.shape[0]):
            for j in range(xq.shape[1]):
                ii = int((yq[i, j] - fy0) / (fy1 - fy0) * (N - 1))
                jj = int((xq[i, j] - fx0) / (fx1 - fx0) * (N - 1))
                ii = np.clip(ii, 0, N - 1)
                jj = np.clip(jj, 0, N - 1)
                out[i, j] = arr[ii, jj]
        return out

    gx_q = sample(dx, Xq, Yq)
    gy_q = sample(dy, Xq, Yq)
    # downhill = −∇Z
    fx_dir = -gx_q
    fy_dir = -gy_q
    mag = np.hypot(fx_dir, fy_dir)
    max_mag = mag.max() if mag.max() > 0 else 1.0

    # arrow length scales with gradient magnitude (capped)
    max_arrow = 0.55
    for i in range(ny_arrows):
        for j in range(nx_arrows):
            m = mag[i, j] / max_mag
            if m < 0.10:
                continue    # skip near-flat regions
            L = max_arrow * (0.40 + 0.60 * m)
            # unit vector
            uh = fx_dir[i, j] / mag[i, j]
            vh = fy_dir[i, j] / mag[i, j]
            x0 = Xq[i, j]
            y0 = Yq[i, j]
            x1 = x0 + uh * L
            y1 = y0 + vh * L

            # glow
            ax.plot([x0, x1], [y0, y1],
                    color="#9fe6f3", lw=5, alpha=0.22,
                    solid_capstyle="round", zorder=6)
            ax.add_patch(FancyArrowPatch(
                (x0, y0), (x1, y1),
                arrowstyle="-|>", mutation_scale=11,
                color="#1aa6c7", lw=2.0, zorder=7,
            ))

    # =============================================================
    # Corner badges: "high" (hill icon) upper-left, "low" (valley)
    # lower-right
    # =============================================================
    def badge_frame(bx, by, R=0.50, face="white", edge="#1f3b57"):
        for rr, a in [(R * 1.35, 0.08),
                      (R * 1.18, 0.16),
                      (R * 1.05, 0.28)]:
            ax.add_patch(Circle((bx, by), rr, facecolor=edge,
                                edgecolor="none", alpha=a,
                                zorder=9))
        ax.add_patch(Circle((bx, by), R,
                            facecolor=face, edgecolor=edge,
                            lw=2.2, zorder=10))

    # HIGH badge — upper-left corner of the panel, a mini hill glyph
    hb_x, hb_y = fx0 + 0.80, fy1 - 0.80
    badge_frame(hb_x, hb_y, R=0.46, edge="#c97a10")
    # triangle "hill" glyph
    hill_pts = [(hb_x - 0.26, hb_y - 0.16),
                (hb_x - 0.05, hb_y + 0.22),
                (hb_x + 0.08, hb_y - 0.02),
                (hb_x + 0.26, hb_y + 0.16),
                (hb_x + 0.26, hb_y - 0.16)]
    ax.add_patch(Polygon(hill_pts, closed=True,
                         facecolor="#ffb347", edgecolor="#7a4a0a",
                         lw=1.4, zorder=11))
    # upward arrow above the hill
    ax.annotate("",
                xy=(hb_x, hb_y + 0.32),
                xytext=(hb_x, hb_y + 0.08),
                arrowprops=dict(arrowstyle="-|>",
                                color="#c97a10", lw=2.0),
                zorder=12)

    # LOW badge — lower-right corner, a valley glyph
    lb_x, lb_y = fx1 - 0.80, fy0 + 0.80
    badge_frame(lb_x, lb_y, R=0.46, edge="#5b6b80")
    # valley/downward V
    val_pts = [(lb_x - 0.26, lb_y + 0.18),
               (lb_x, lb_y - 0.16),
               (lb_x + 0.26, lb_y + 0.18)]
    ax.plot([p[0] for p in val_pts],
            [p[1] for p in val_pts],
            color="#5b6b80", lw=2.8,
            solid_capstyle="round", zorder=11)
    # downward arrow
    ax.annotate("",
                xy=(lb_x, lb_y - 0.32),
                xytext=(lb_x, lb_y - 0.08),
                arrowprops=dict(arrowstyle="-|>",
                                color="#5b6b80", lw=2.0),
                zorder=12)

    # ---- framing ---------------------------------------------------
    ax.set_xlim(0, 13)
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
