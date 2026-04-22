"""
FRAP on BSA — visual-only illustration.

Metaphor: a microscope field with a photobleached spot that recovers
with a DAMPED OSCILLATORY signature (ED participation-channel
prediction), not a smooth monotonic rise.

Composition:
  LEFT  : a circular microscope field-of-view disc.
          Dark field with glowing green fluorescent BSA particles
          scattered throughout.  A central BLEACHED spot (darker, mostly
          empty).  Pulsing coral/orange concentric rings emanate from
          the bleached region — the "ringing" recovery signature.
  RIGHT : a damped-oscillation recovery curve I(t) versus time, with
          an exponential-decay envelope, a baseline at 0 (fully
          bleached), and an asymptote at the pre-bleach level.  Three
          peak/trough snapshot dots.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\FRAP_BSA.png"


def build():
    fig, ax = plt.subplots(figsize=(13, 9), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 14, 0, 10], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 14, 1.5,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # =============================================================
    # LEFT — microscope field of view (circular)
    # =============================================================
    fov_cx, fov_cy = 4.0, 5.0
    fov_R = 3.35
    bleach_R = 1.15

    # dark microscope field disc
    # halo around the disc (biological sample ambient glow)
    for rr, a in [(fov_R + 0.55, 0.08),
                  (fov_R + 0.32, 0.15),
                  (fov_R + 0.16, 0.28)]:
        ax.add_patch(Circle((fov_cx, fov_cy), rr,
                            facecolor="#2a4c6e",
                            edgecolor="none", alpha=a, zorder=2))

    # dark field body
    ax.add_patch(Circle((fov_cx, fov_cy), fov_R,
                        facecolor="#0f2038",
                        edgecolor="#6b8aa8", lw=2.6, zorder=3))
    # inner subtle ring
    ax.add_patch(Circle((fov_cx, fov_cy), fov_R - 0.12,
                        facecolor="none", edgecolor="#8aa4c0",
                        lw=1.0, alpha=0.35, zorder=5))

    # ---- scattered fluorescent BSA particles around the field ----
    rng = np.random.default_rng(11)
    n_particles = 280

    def add_particle(x, y, bright=True):
        if bright:
            # green-yellow glowing dot
            for rr, a in [(0.11, 0.15), (0.08, 0.28), (0.06, 0.55)]:
                ax.add_patch(Circle((x, y), rr,
                                    facecolor="#b6f06a",
                                    edgecolor="none",
                                    alpha=a, zorder=4))
            ax.add_patch(Circle((x, y), 0.030,
                                facecolor="#ecffc1",
                                edgecolor="#548526", lw=0.4,
                                alpha=0.95, zorder=5))
        else:
            # dim / partially recovered particle inside the bleached region
            ax.add_patch(Circle((x, y), 0.04,
                                facecolor="#6a8f3a",
                                edgecolor="none",
                                alpha=0.45, zorder=4))

    placed_bright = 0
    placed_dim = 0
    for _ in range(n_particles * 3):
        x = rng.uniform(fov_cx - fov_R + 0.15, fov_cx + fov_R - 0.15)
        y = rng.uniform(fov_cy - fov_R + 0.15, fov_cy + fov_R - 0.15)
        r_from_c = np.hypot(x - fov_cx, y - fov_cy)
        if r_from_c > fov_R - 0.15:
            continue
        if r_from_c < bleach_R * 0.85:
            # inside the bleached region — rarely place a dim particle
            if rng.random() < 0.10 and placed_dim < 12:
                add_particle(x, y, bright=False)
                placed_dim += 1
            continue
        # outside the bleached region — bright particles
        if placed_bright < n_particles:
            add_particle(x, y, bright=True)
            placed_bright += 1

    # ---- BLEACHED spot (dark disc in the center) ------------------
    # soft inner vignette showing the bleach edge
    for rr, a in [(bleach_R + 0.45, 0.10),
                  (bleach_R + 0.30, 0.18),
                  (bleach_R + 0.15, 0.30)]:
        ax.add_patch(Circle((fov_cx, fov_cy), rr,
                            facecolor="#08142a",
                            edgecolor="none", alpha=a, zorder=6))
    # the bleached disc proper
    ax.add_patch(Circle((fov_cx, fov_cy), bleach_R,
                        facecolor="#081a30",
                        edgecolor="#3a557a", lw=2.0,
                        zorder=7))

    # ---- PULSING RECOVERY RINGS (the RLC-like signature) ----------
    # Multiple concentric coral rings with alternating bright/dim
    # amplitude to convey oscillatory recovery.  Draw from the outer
    # boundary inward.
    ring_radii = [bleach_R + 0.55, bleach_R + 1.05,
                  bleach_R + 1.55, bleach_R + 2.00]
    ring_alphas = [0.85, 0.55, 0.35, 0.20]   # damped
    ring_lws = [4.5, 3.6, 2.8, 2.2]

    for rr, a, lw in zip(ring_radii, ring_alphas, ring_lws):
        # glow underlay
        for lw_h, ah in [(lw + 6, a * 0.35),
                         (lw + 3, a * 0.55)]:
            ax.add_patch(Circle((fov_cx, fov_cy), rr,
                                facecolor="none",
                                edgecolor="#ffae79",
                                lw=lw_h, alpha=ah, zorder=8))
        # crisp ring
        ax.add_patch(Circle((fov_cx, fov_cy), rr,
                            facecolor="none",
                            edgecolor="#f46d3b",
                            lw=lw, alpha=a, zorder=9))

    # small sparkle highlights on the pulsing rings
    for rr, n_spark in [(ring_radii[0], 6),
                       (ring_radii[1], 4)]:
        for k in range(n_spark):
            th = k * 2 * np.pi / n_spark + 0.2 * rr
            px = fov_cx + rr * np.cos(th)
            py = fov_cy + rr * np.sin(th)
            ax.add_patch(Circle((px, py), 0.07,
                                facecolor="#ffd4b0",
                                edgecolor="#c94419", lw=0.9,
                                alpha=0.92, zorder=11))

    # tiny coral "pulse" dot at the very center
    for rr, a in [(0.38, 0.10), (0.26, 0.22), (0.17, 0.45)]:
        ax.add_patch(Circle((fov_cx, fov_cy), rr,
                            facecolor="#ffae79",
                            edgecolor="none", alpha=a, zorder=10))
    ax.add_patch(Circle((fov_cx, fov_cy), 0.12,
                        facecolor="#f46d3b",
                        edgecolor="#7a2d0b", lw=1.2,
                        zorder=11))

    # =============================================================
    # RIGHT — damped-oscillation recovery I(t)
    # =============================================================
    rx0, rx1 = 8.3, 13.4
    ry_base = 2.2         # fully bleached level
    ry_asymptote = 6.6    # pre-bleach / recovered level
    ry_top = 7.7          # top of plot range (peaks can rise above asymptote)

    # plot panel bg
    ax.add_patch(FancyBboxPatch(
        (rx0 - 0.35, ry_base - 0.40),
        rx1 - rx0 + 0.70, ry_top - ry_base + 0.70,
        boxstyle="round,pad=0.04,rounding_size=0.20",
        facecolor="white", edgecolor="#1f3b57",
        lw=1.6, alpha=0.92, zorder=3,
    ))

    # faint asymptote line
    ax.plot([rx0 + 0.1, rx1 - 0.1], [ry_asymptote, ry_asymptote],
            color="#1f3b57", lw=1.0, alpha=0.30,
            linestyle=(0, (5, 4)), zorder=5)

    # y-axis
    ax.plot([rx0 + 0.1, rx0 + 0.1], [ry_base + 0.1, ry_top - 0.1],
            color="#1f3b57", lw=1.6, alpha=0.70, zorder=5)
    # t-axis
    ax.plot([rx0 + 0.1, rx1 - 0.1], [ry_base, ry_base],
            color="#1f3b57", lw=1.6, alpha=0.75, zorder=5)
    ax.annotate("",
                xy=(rx1 - 0.1, ry_base),
                xytext=(rx0 + 0.1, ry_base),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1f3b57", lw=1.6, alpha=0.0),
                zorder=5)

    # ---- the damped-oscillatory recovery curve --------------------
    # I(t) = asymptote * [1 - e^{-ζω_n t} (cos(ω_d t) + (ζ/√(1-ζ²)) sin(ω_d t))]
    ts = np.linspace(rx0 + 0.3, rx1 - 0.25, 700)
    tn = (ts - ts[0]) / (ts[-1] - ts[0])
    zeta = 0.16
    wn = 16.0
    wd = wn * np.sqrt(1 - zeta ** 2)
    t_scaled = tn * 1.55
    y = 1.0 - np.exp(-zeta * wn * t_scaled) * (
        np.cos(wd * t_scaled)
        + (zeta / np.sqrt(1 - zeta ** 2)) * np.sin(wd * t_scaled)
    )

    # scale to plot: y=1 → asymptote, y can briefly exceed 1 at first peak
    scale = ry_asymptote - ry_base
    curve_y = ry_base + y * scale

    # envelope curves (outer ringing envelope = asymptote ± decay)
    env_amp = np.exp(-zeta * wn * t_scaled) * scale
    env_top = ry_asymptote + env_amp
    env_bot = ry_asymptote - env_amp
    env_bot = np.clip(env_bot, ry_base, ry_top)  # don't dip below bleached

    # envelope strokes (faint)
    for yarr in [env_top, env_bot]:
        for lw, a in [(7, 0.10), (4, 0.18)]:
            ax.plot(ts, yarr, color="#f46d3b", lw=lw, alpha=a,
                    solid_capstyle="round", zorder=5)
        ax.plot(ts, yarr, color="#f46d3b", lw=1.3, alpha=0.45,
                linestyle=(0, (6, 4)), zorder=6)

    # shaded area between the curve and the baseline
    ax.fill_between(ts, ry_base, curve_y,
                    color="#ffd4b0", alpha=0.25, zorder=5)

    # main curve with glow
    for lw, col, a in [(12, "#ffd4b0", 0.14),
                       (8, "#ffae79", 0.24),
                       (4.0, "#c94419", 0.98)]:
        ax.plot(ts, curve_y, color=col, lw=lw, alpha=a,
                solid_capstyle="round", zorder=7)

    # peak markers
    for i in range(1, len(curve_y) - 1):
        if (curve_y[i - 1] < curve_y[i] > curve_y[i + 1]
                and curve_y[i] > ry_asymptote - 0.05):
            px, py = ts[i], curve_y[i]
            for rr, a in [(0.32, 0.14), (0.22, 0.30)]:
                ax.add_patch(Circle((px, py), rr,
                                    facecolor="#ffd4b0",
                                    edgecolor="none",
                                    alpha=a, zorder=8))
            ax.add_patch(Circle((px, py), 0.12,
                                facecolor="#ffae79",
                                edgecolor="#7a2d0b",
                                lw=1.4, zorder=10))

    # tiny "bleach event" marker at t=0 — a short downward tick
    ax.plot([rx0 + 0.3, rx0 + 0.3],
            [ry_base, ry_base + 0.35],
            color="#c94419", lw=2.4, alpha=0.9,
            solid_capstyle="round", zorder=8)
    ax.add_patch(Circle((rx0 + 0.3, ry_base + 0.38), 0.10,
                        facecolor="#c94419", edgecolor="#7a2d0b",
                        lw=1.0, zorder=9))

    # =============================================================
    # Connector: bleached spot -> start of the recovery curve
    # =============================================================
    ax.annotate("",
                xy=(rx0 + 0.3, ry_base + 0.55),
                xytext=(fov_cx + bleach_R * 0.9, fov_cy - bleach_R * 0.75),
                arrowprops=dict(arrowstyle="-|>",
                                color="#c94419", lw=2.0, alpha=0.75,
                                connectionstyle="arc3,rad=-0.25",
                                linestyle=(0, (4, 3))),
                zorder=7)

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
