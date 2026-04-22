"""
Single Scalar Field constraint — visual-only illustration.

Metaphor: a smooth 2D scalar field ρ(x,t) — one number per point,
nothing else.  No arrows, no tensors, no components.

Composition:
  • A minimal, soft violet scalar field rendered as a heatmap
    (no directional arrows on top).
  • A thin "value probe" at one sample point: a small color swatch
    tied to a dashed leader line showing that each point gives exactly
    one scalar value.
  • Two corner "not-this" badges: one with struck-out vector arrows
    (not a vector field) and one with struck-out tensor ellipses
    (not a tensor field).  These make the minimality claim explicit.
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


OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\ScalarField.png"


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
    # Main field panel
    # =============================================================
    fx0, fx1 = 1.0, 12.0
    fy0, fy1 = 2.4, 9.6

    # panel halo
    for pad, a in [(0.22, 0.06), (0.12, 0.14), (0.06, 0.22)]:
        ax.add_patch(FancyBboxPatch(
            (fx0 - pad, fy0 - pad),
            fx1 - fx0 + 2 * pad, fy1 - fy0 + 2 * pad,
            boxstyle="round,pad=0.02,rounding_size=0.22",
            facecolor="#c8aff0", edgecolor="none",
            alpha=a, zorder=1,
        ))

    # =============================================================
    # The scalar field: smooth, gentle, minimal
    # =============================================================
    N = 420
    xs = np.linspace(fx0, fx1, N)
    ys = np.linspace(fy0, fy1, N)
    X, Y = np.meshgrid(xs, ys)
    # soft two-bump field plus gentle baseline
    bump1 = np.exp(-((X - 4.5) ** 2 + (Y - 6.2) ** 2) / (2 * 1.8 ** 2))
    bump2 = 0.55 * np.exp(-((X - 8.5) ** 2 + (Y - 5.0) ** 2)
                           / (2 * 1.4 ** 2))
    base = 0.18 * ((X - fx0) / (fx1 - fx0))
    Z = bump1 + bump2 + base
    Z = gaussian_filter(Z, sigma=3.5)
    Z = (Z - Z.min()) / (Z.max() - Z.min())

    # minimal violet colormap (one channel encodes density)
    cmap_violet = LinearSegmentedColormap.from_list(
        "scalar_violet",
        [
            (0.00, (0.97, 0.95, 1.00, 1.00)),
            (0.22, (0.88, 0.78, 0.96, 1.00)),
            (0.45, (0.68, 0.52, 0.88, 1.00)),
            (0.68, (0.48, 0.32, 0.80, 1.00)),
            (0.88, (0.32, 0.18, 0.62, 1.00)),
            (1.00, (0.18, 0.08, 0.42, 1.00)),
        ],
    )
    ax.imshow(Z, extent=[fx0, fx1, fy0, fy1],
              origin="lower", cmap=cmap_violet, alpha=0.96,
              interpolation="bilinear", zorder=2)

    # very faint iso-contours — JUST enough to hint at topography,
    # but no arrows and no directional markers
    ax.contour(X, Y, Z,
               levels=np.linspace(0.15, 0.92, 6),
               colors="#f1e6ff", linewidths=0.7,
               alpha=0.45, zorder=3)

    # panel outline
    ax.add_patch(FancyBboxPatch(
        (fx0, fy0), fx1 - fx0, fy1 - fy0,
        boxstyle="round,pad=0.02,rounding_size=0.22",
        facecolor="none", edgecolor="#6a3fb0",
        lw=2.8, zorder=5,
    ))
    # inner thin ring
    ax.add_patch(FancyBboxPatch(
        (fx0 + 0.15, fy0 + 0.15),
        fx1 - fx0 - 0.30, fy1 - fy0 - 0.30,
        boxstyle="round,pad=0.02,rounding_size=0.18",
        facecolor="none", edgecolor="#c8aff0",
        lw=0.9, alpha=0.65, zorder=5,
    ))

    # =============================================================
    # Value-probe at a sample point: dashed leader line to a small
    # color swatch with a single filled chip (one number per point)
    # =============================================================
    probe_x, probe_y = 6.1, 7.3
    # sample the field value there
    i_sample = int((probe_y - fy0) / (fy1 - fy0) * (N - 1))
    j_sample = int((probe_x - fx0) / (fx1 - fx0) * (N - 1))
    sample_val = float(Z[i_sample, j_sample])

    # probe dot on the field
    ax.add_patch(Circle((probe_x, probe_y), 0.16,
                        facecolor="white", edgecolor="#6a3fb0",
                        lw=2.2, zorder=11))
    ax.add_patch(Circle((probe_x, probe_y), 0.07,
                        facecolor="#6a3fb0", zorder=12))

    # leader line to a swatch-pill in the upper-right interior of the panel
    swatch_cx, swatch_cy = 10.3, 8.45
    ax.plot([probe_x + 0.12, swatch_cx - 0.55],
            [probe_y + 0.08, swatch_cy],
            color="#6a3fb0", lw=1.2, alpha=0.55,
            linestyle=(0, (3, 3)), zorder=10)

    # swatch-pill: a single chip (one value) — height-bar inside
    pill_w = 1.1
    pill_h = 0.70
    ax.add_patch(FancyBboxPatch(
        (swatch_cx - pill_w / 2, swatch_cy - pill_h / 2),
        pill_w, pill_h,
        boxstyle="round,pad=0.02,rounding_size=0.12",
        facecolor="white", edgecolor="#6a3fb0",
        lw=2.0, zorder=11,
    ))
    # inner fill chip showing the single scalar value (violet intensity)
    sample_col = cmap_violet(sample_val)
    ax.add_patch(FancyBboxPatch(
        (swatch_cx - pill_w / 2 + 0.10, swatch_cy - pill_h / 2 + 0.12),
        pill_w - 0.20, pill_h - 0.24,
        boxstyle="round,pad=0.02,rounding_size=0.06",
        facecolor=sample_col, edgecolor="none", zorder=12,
    ))
    # tiny value-dot on the right end of the chip
    ax.add_patch(Circle((swatch_cx + pill_w / 2 - 0.18, swatch_cy), 0.07,
                        facecolor="#6a3fb0", edgecolor="white",
                        lw=1.0, zorder=13))

    # =============================================================
    # "Not this" corner badges — vector & tensor, both struck out
    # =============================================================
    def no_badge(bx, by, draw_fn, outline="#c23b3b"):
        # soft halo + white disc + slash + draw_fn(bx, by) for content
        for rr, a in [(0.60, 0.08), (0.45, 0.16)]:
            ax.add_patch(Circle((bx, by), rr,
                                facecolor=outline,
                                edgecolor="none", alpha=a, zorder=9))
        ax.add_patch(Circle((bx, by), 0.40,
                            facecolor="white", edgecolor=outline,
                            lw=2.4, zorder=10))
        draw_fn(bx, by)
        ax.plot([bx - 0.30, bx + 0.30],
                [by + 0.30, by - 0.30],
                color=outline, lw=3.0,
                solid_capstyle="round", zorder=14)

    # VECTOR field icon: 3 small arrows inside a badge
    def vector_icon(bx, by):
        for ang_deg in [25, 115, 235]:
            ang = np.deg2rad(ang_deg)
            L = 0.22
            p0 = (bx - L * 0.5 * np.cos(ang),
                  by - L * 0.5 * np.sin(ang))
            p1 = (bx + L * np.cos(ang),
                  by + L * np.sin(ang))
            ax.add_patch(FancyArrowPatch(
                p0, p1, arrowstyle="-|>",
                mutation_scale=10,
                color="#5b6b80", lw=1.8, zorder=11,
            ))

    # TENSOR field icon: two small ellipses cross-hatched (principal axes)
    def tensor_icon(bx, by):
        ax.add_patch(Ellipse((bx, by), 0.50, 0.22,
                             angle=20, facecolor="none",
                             edgecolor="#5b6b80", lw=1.8,
                             zorder=11))
        ax.add_patch(Ellipse((bx, by), 0.22, 0.50,
                             angle=20, facecolor="none",
                             edgecolor="#5b6b80", lw=1.8,
                             zorder=11))

    # Place badges in upper-left and lower-right, outside the main
    # scalar-field panel so they read as meta-commentary
    no_badge(1.10, 9.45, vector_icon)
    no_badge(11.90, 2.55, tensor_icon)

    # =============================================================
    # A small "one-field" insignia in the lower-left: a single violet
    # scalar-number chip (just one), surrounded by nothing
    # =============================================================
    chip_cx, chip_cy = 1.70, 2.55
    for rr, a in [(0.50, 0.08), (0.36, 0.18)]:
        ax.add_patch(Circle((chip_cx, chip_cy), rr,
                            facecolor="#c8aff0",
                            edgecolor="none", alpha=a, zorder=9))
    ax.add_patch(Circle((chip_cx, chip_cy), 0.30,
                        facecolor="white", edgecolor="#6a3fb0",
                        lw=2.2, zorder=10))
    # single filled chip inside
    ax.add_patch(Circle((chip_cx, chip_cy), 0.15,
                        facecolor="#6a3fb0",
                        edgecolor="#4a1e85", lw=1.0, zorder=11))
    # tiny highlight
    ax.add_patch(Circle((chip_cx - 0.05, chip_cy + 0.05), 0.05,
                        facecolor="white", alpha=0.70,
                        zorder=12))

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
