"""
Triad Coupling — visual-only illustration.

Metaphor: a SPECTRAL FINGERPRINT.  In a spectrum plot vs. k, two
primary modes k₁ and k₂ appear as tall peaks; the nonlinear triad
coupling (P7) produces a small-amplitude sideband peak at k₃ = k₁+k₂
with universal coupling C ≈ 0.03.

Distinct from P7's "wave mixer + k-space triangle" — here we show the
experimental signature: two tall peaks + one small peak, with arrows
from the primaries converging on the sideband.

Composition:
  MAIN : spectrum plot.  Cyan peak at k₁, green peak at k₂, small amber
         peak at k₃ with an amplitude-scale inset showing the 3% ratio.
         Two converging arrows from the primaries to the sideband.
  INSET: a tiny vertical "ratio bar" near k₃ showing the ~3-6% amplitude
         relative to the primaries.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\TriadCoupling.png"


def gaussian_peak(k_axis, k0, sigma=0.25):
    return np.exp(-((k_axis - k0) ** 2) / (2 * sigma ** 2))


def build():
    fig, ax = plt.subplots(figsize=(13, 9), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 14, 0, 10], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 14, 1.3,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # =============================================================
    # Spectrum plot panel
    # =============================================================
    plot_x0, plot_x1 = 0.8, 13.3
    plot_y0, plot_y1 = 1.7, 9.4

    ax.add_patch(FancyBboxPatch(
        (plot_x0, plot_y0),
        plot_x1 - plot_x0, plot_y1 - plot_y0,
        boxstyle="round,pad=0.04,rounding_size=0.25",
        facecolor="white", edgecolor="#1f3b57",
        lw=1.6, alpha=0.94, zorder=2,
    ))

    # axes
    ax_x0 = plot_x0 + 0.45
    ax_x1 = plot_x1 - 0.30
    ax_y0 = plot_y0 + 0.70
    ax_y_top = plot_y1 - 0.45

    # x-axis (k)
    ax.plot([ax_x0, ax_x1], [ax_y0, ax_y0],
            color="#1f3b57", lw=1.8, alpha=0.85, zorder=4)
    ax.annotate("",
                xy=(ax_x1 + 0.08, ax_y0),
                xytext=(ax_x0, ax_y0),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1f3b57", lw=1.8),
                zorder=5)
    # y-axis (amplitude)
    ax.plot([ax_x0, ax_x0], [ax_y0, ax_y_top],
            color="#1f3b57", lw=1.8, alpha=0.85, zorder=4)
    ax.annotate("",
                xy=(ax_x0, ax_y_top + 0.08),
                xytext=(ax_x0, ax_y0),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1f3b57", lw=1.8),
                zorder=5)

    # subtle gridlines
    for frac in [0.25, 0.5, 0.75]:
        yh = ax_y0 + frac * (ax_y_top - ax_y0)
        ax.plot([ax_x0 + 0.02, ax_x1], [yh, yh],
                color="#1f3b57", lw=0.7, alpha=0.15,
                linestyle=(0, (4, 4)), zorder=3)

    # =============================================================
    # Spectrum composition
    # =============================================================
    # k-axis: map k ∈ [0, 12] into plot coords
    k_lo, k_hi = 0.0, 12.0
    k_axis_vals = np.linspace(k_lo, k_hi, 2000)

    def k_to_x(k):
        return ax_x0 + (k - k_lo) / (k_hi - k_lo) * (ax_x1 - ax_x0)

    # primary modes
    k1 = 3.3
    k2 = 5.7
    k3 = k1 + k2    # 9.0

    # amplitudes: primaries big, sideband small
    A_primary = (ax_y_top - ax_y0) * 0.88
    A_sideband = A_primary * 0.055          # ≈ 5.5%, in the 3-6% range

    # Build the spectrum as sum of Gaussians
    S = (A_primary * gaussian_peak(k_axis_vals, k1, sigma=0.18)
         + A_primary * gaussian_peak(k_axis_vals, k2, sigma=0.18)
         + A_sideband * gaussian_peak(k_axis_vals, k3, sigma=0.16))

    # Add a low noise floor
    rng = np.random.default_rng(3)
    noise = np.abs(rng.normal(0, 0.02, len(k_axis_vals))) * (ax_y_top - ax_y0) * 0.25
    # baseline noise floor
    floor = (ax_y_top - ax_y0) * 0.02
    S = np.maximum(S + noise * 0.6, floor * np.ones_like(S))

    # Convert to plot coordinates
    x_spec = k_to_x(k_axis_vals)
    y_spec = ax_y0 + S

    # Render spectrum by coloring regions of k-axis:
    # - near k1: cyan
    # - near k2: green
    # - near k3: amber (small peak)
    # - elsewhere: navy/grey
    def plot_region(k_center, color_core, color_halo, half_width=1.0):
        mask = np.abs(k_axis_vals - k_center) < half_width
        xs_r = x_spec[mask]
        ys_r = y_spec[mask]
        # fill under curve
        ax.fill_between(xs_r, ax_y0, ys_r,
                        color=color_halo, alpha=0.45, zorder=5)
        # glow strokes
        for lw, col, a in [(10, color_halo, 0.12),
                           (6, color_halo, 0.22),
                           (3.0, color_core, 0.95)]:
            ax.plot(xs_r, ys_r, color=col, lw=lw, alpha=a,
                    solid_capstyle="round", zorder=6)

    # Draw base grey spectrum first (everywhere not in a peak region)
    base_mask = (np.abs(k_axis_vals - k1) > 1.0) & \
                (np.abs(k_axis_vals - k2) > 1.0) & \
                (np.abs(k_axis_vals - k3) > 1.0)
    ax.fill_between(x_spec[base_mask], ax_y0, y_spec[base_mask],
                    color="#cfd8e0", alpha=0.55, zorder=5)
    ax.plot(x_spec[base_mask], y_spec[base_mask],
            color="#5b6b80", lw=1.6, alpha=0.55, zorder=6)

    # Peak regions
    plot_region(k1, "#1aa6c7", "#9fe6f3", half_width=1.0)
    plot_region(k2, "#2fb27a", "#b6e7cf", half_width=1.0)
    plot_region(k3, "#c97a10", "#ffd98a", half_width=0.8)

    # =============================================================
    # Peak labels (amber badges at each peak top)
    # =============================================================
    def label_peak(k_pos, amp, face, edge, number):
        px = k_to_x(k_pos)
        py = ax_y0 + amp
        # small glow
        for rr, a in [(0.42, 0.10), (0.30, 0.22)]:
            ax.add_patch(Circle((px, py + 0.55), rr,
                                facecolor=face, edgecolor="none",
                                alpha=a, zorder=9))
        ax.add_patch(Circle((px, py + 0.55), 0.32,
                            facecolor="white", edgecolor=edge,
                            lw=2.0, zorder=10))
        # inside: small stack of hash marks = number
        for i in range(number):
            ax.plot([px - 0.14 + i * 0.12, px - 0.14 + i * 0.12],
                    [py + 0.45, py + 0.65],
                    color=edge, lw=2.4,
                    solid_capstyle="round", zorder=11)
        return (px, py)

    p1 = label_peak(k1, A_primary * 1.0, "#9fe6f3", "#1aa6c7", 1)
    p2 = label_peak(k2, A_primary * 1.0, "#b6e7cf", "#2fb27a", 2)
    p3 = label_peak(k3, A_sideband * 1.0, "#ffd98a", "#c97a10", 3)

    # =============================================================
    # Arrows from primaries converging on the sideband (k1 + k2 → k3)
    # =============================================================
    ax.annotate("",
                xy=(p3[0] - 0.18, p3[1] + 0.85),
                xytext=(p1[0] + 0.18, p1[1] + 0.85),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1aa6c7", lw=2.2, alpha=0.85,
                                connectionstyle="arc3,rad=-0.35"),
                zorder=11)
    ax.annotate("",
                xy=(p3[0] - 0.10, p3[1] + 0.95),
                xytext=(p2[0] + 0.18, p2[1] + 0.85),
                arrowprops=dict(arrowstyle="-|>",
                                color="#2fb27a", lw=2.2, alpha=0.85,
                                connectionstyle="arc3,rad=-0.30"),
                zorder=11)

    # small convergence indicator — a glowing ⊕ node just above k3
    conv_x, conv_y = p3[0], p3[1] + 1.60
    for rr, a in [(0.38, 0.10), (0.28, 0.22), (0.20, 0.45)]:
        ax.add_patch(Circle((conv_x, conv_y), rr,
                            facecolor="#ffd24a", edgecolor="none",
                            alpha=a, zorder=11))
    ax.add_patch(Circle((conv_x, conv_y), 0.16,
                        facecolor="white", edgecolor="#c97a10",
                        lw=2.0, zorder=12))
    ax.plot([conv_x - 0.10, conv_x + 0.10], [conv_y, conv_y],
            color="#c97a10", lw=2.2, solid_capstyle="round",
            zorder=13)
    ax.plot([conv_x, conv_x], [conv_y - 0.10, conv_y + 0.10],
            color="#c97a10", lw=2.2, solid_capstyle="round",
            zorder=13)
    # arrow from convergence node down to k3 peak
    ax.annotate("",
                xy=(p3[0], p3[1] + 0.95),
                xytext=(conv_x, conv_y - 0.22),
                arrowprops=dict(arrowstyle="-|>",
                                color="#c97a10", lw=2.4, alpha=0.95),
                zorder=13)

    # =============================================================
    # Amplitude ratio bar (showing "tiny" relative to primaries)
    # =============================================================
    # Vertical bar next to the k3 peak region: shows the ~3-6% ratio
    bar_x = k_to_x(k3) + 1.0
    bar_y0_ = ax_y0
    bar_y1_ = ax_y0 + A_primary  # full-height bar
    bar_w = 0.35

    # background bar (grey, representing "100%")
    ax.add_patch(FancyBboxPatch(
        (bar_x, bar_y0_), bar_w, A_primary,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        facecolor="#eef0f3", edgecolor="#5b6b80",
        lw=1.4, alpha=0.85, zorder=7,
    ))
    # filled portion (amber, representing the ~5% coupling)
    ax.add_patch(FancyBboxPatch(
        (bar_x, bar_y0_), bar_w, A_sideband,
        boxstyle="round,pad=0.02,rounding_size=0.06",
        facecolor="#ffb347", edgecolor="#c97a10",
        lw=1.4, zorder=8,
    ))
    # glow around the filled portion
    for g, a in [(0.20, 0.08), (0.14, 0.18), (0.08, 0.32)]:
        ax.add_patch(FancyBboxPatch(
            (bar_x - g / 2, bar_y0_ - g / 2),
            bar_w + g, A_sideband + g,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor="#ffd24a", edgecolor="none",
            alpha=a, zorder=7,
        ))
    # little arrow + small tag on top of amber-filled region
    tag_x = bar_x + bar_w + 0.10
    tag_y = bar_y0_ + A_sideband
    ax.plot([bar_x + bar_w * 0.5, bar_x + bar_w + 0.35],
            [tag_y, tag_y],
            color="#c97a10", lw=1.6, alpha=0.7, zorder=9)
    ax.add_patch(Circle((tag_x + 0.20, tag_y), 0.14,
                        facecolor="#fff1b0", edgecolor="#c97a10",
                        lw=1.6, zorder=10))
    # tiny "%" icon: three small dots stacked in the badge
    for dy in [-0.04, 0.0, 0.04]:
        ax.add_patch(Circle((tag_x + 0.20, tag_y + dy), 0.013,
                            facecolor="#c97a10", zorder=11))

    # ---- framing ---------------------------------------------------
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
