"""
P7 Nonlinear Triad — visual-only illustration.

Metaphor: wave mixing.  Two input waves (k₁ cyan, k₂ teal) flow into a
glowing nonlinear mixer node, which emits a third wave (k₃ amber)
whose wavenumber is the sum of the inputs: k₃ = k₁ + k₂.

A small k-space triangle inset below reinforces the triad-resonance
condition as a vector sum.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch, Polygon,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\P7_nonlinear_triad.png"


def wave_on_path(ax, p0, p1, k, amp=0.22, color="#1aa6c7",
                 halo="#9fe6f3", envelope_fade=True, zorder=6):
    """Draw a sine wave traveling from p0 to p1 with wavenumber k."""
    p0 = np.asarray(p0, float)
    p1 = np.asarray(p1, float)
    v = p1 - p0
    L = np.linalg.norm(v)
    uhat = v / L
    nhat = np.array([-uhat[1], uhat[0]])
    n = 600
    t = np.linspace(0, 1, n)
    env = np.ones_like(t)
    if envelope_fade:
        # fade in/out at the ends
        env = np.where(t < 0.08, t / 0.08, env)
        env = np.where(t > 0.92, (1 - t) / 0.08, env)
        env = np.clip(env, 0, 1)
    phase = 2 * np.pi * k * t
    pts = (p0[:, None]
           + uhat[:, None] * (t * L)
           + nhat[:, None] * (amp * env * np.sin(phase)))
    xs, ys = pts[0], pts[1]
    for lw, col, a in [(10, halo, 0.12), (6, halo, 0.22),
                       (3.2, color, 0.95)]:
        ax.plot(xs, ys, color=col, lw=lw, alpha=a,
                solid_capstyle="round", zorder=zorder)
    return xs, ys


def build():
    fig, ax = plt.subplots(figsize=(11, 10), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 12, 0, 11], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 12, 1.8,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # =============================================================
    # Mixer node — centerpiece
    # =============================================================
    mx, my = 6.7, 6.5
    R_mix = 0.95

    # outer halos (radial burst)
    for rr, a in [(R_mix + 1.40, 0.04),
                  (R_mix + 0.95, 0.08),
                  (R_mix + 0.60, 0.14),
                  (R_mix + 0.35, 0.24),
                  (R_mix + 0.15, 0.40)]:
        ax.add_patch(Circle((mx, my), rr,
                            facecolor="#ffd24a", edgecolor="none",
                            alpha=a, zorder=3))

    # mixer body — a disc with a faint gear-like ring of teeth
    n_teeth = 14
    for k in range(n_teeth):
        th0 = k * 2 * np.pi / n_teeth
        th1 = th0 + (2 * np.pi / n_teeth) * 0.45
        r_in = R_mix
        r_out = R_mix + 0.14
        poly = [
            (mx + r_in * np.cos(th0), my + r_in * np.sin(th0)),
            (mx + r_out * np.cos(th0), my + r_out * np.sin(th0)),
            (mx + r_out * np.cos(th1), my + r_out * np.sin(th1)),
            (mx + r_in * np.cos(th1), my + r_in * np.sin(th1)),
        ]
        ax.add_patch(Polygon(poly, closed=True,
                             facecolor="#ffb347", edgecolor="#7a4a0a",
                             lw=0.8, alpha=0.85, zorder=4))

    # main disc
    ax.add_patch(Circle((mx, my), R_mix,
                        facecolor="#fff4d6", edgecolor="#7a4a0a",
                        lw=2.8, zorder=5))
    # inner subtle disc
    ax.add_patch(Circle((mx, my), R_mix - 0.18,
                        facecolor="#ffe9b0", edgecolor="#b57b12",
                        lw=1.6, alpha=0.85, zorder=6))

    # a ⊕ glyph in the middle (circle + cross)
    ax.add_patch(Circle((mx, my), 0.40,
                        facecolor="white", edgecolor="#1f3b57",
                        lw=2.6, zorder=7))
    ax.plot([mx - 0.27, mx + 0.27], [my, my],
            color="#1f3b57", lw=3.0, zorder=8,
            solid_capstyle="round")
    ax.plot([mx, mx], [my - 0.27, my + 0.27],
            color="#1f3b57", lw=3.0, zorder=8,
            solid_capstyle="round")

    # =============================================================
    # Incoming waves (k1, k2) and outgoing wave (k3)
    # =============================================================
    # k1: top-left -> mixer
    k1_start = (0.7, 8.9)
    k1_end = (mx - R_mix * 0.92, my + R_mix * 0.40)
    wave_on_path(ax, k1_start, k1_end, k=7.0, amp=0.26,
                 color="#1aa6c7", halo="#9fe6f3", zorder=5)
    # arrowhead at the mixer end
    ax.annotate("", xy=k1_end,
                xytext=(k1_end[0] - 0.35,
                        k1_end[1] - 0.08),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1aa6c7", lw=2.4),
                zorder=7)

    # k2: bottom-left -> mixer
    k2_start = (0.7, 3.4)
    k2_end = (mx - R_mix * 0.92, my - R_mix * 0.40)
    wave_on_path(ax, k2_start, k2_end, k=11.0, amp=0.22,
                 color="#2fb27a", halo="#b6e7cf", zorder=5)
    ax.annotate("", xy=k2_end,
                xytext=(k2_end[0] - 0.35,
                        k2_end[1] + 0.08),
                arrowprops=dict(arrowstyle="-|>",
                                color="#2fb27a", lw=2.4),
                zorder=7)

    # k3: mixer -> right  (higher wavenumber, shorter wavelength)
    k3_start = (mx + R_mix * 0.95, my)
    k3_end = (11.3, my + 0.6)
    wave_on_path(ax, k3_start, k3_end, k=17.0, amp=0.30,
                 color="#c97a10", halo="#ffd98a", zorder=5)
    ax.annotate("", xy=k3_end,
                xytext=(k3_end[0] - 0.4,
                        k3_end[1] - 0.06),
                arrowprops=dict(arrowstyle="-|>",
                                color="#c97a10", lw=2.6),
                zorder=7)

    # =============================================================
    # Small "labels" as icon badges (no text)
    # =============================================================
    def labeled_wave_badge(bx, by, color, halo, k_icon,
                          edge=None):
        edge = edge or color
        for rr, a in [(0.48, 0.10), (0.36, 0.20), (0.28, 0.42)]:
            ax.add_patch(Circle((bx, by), rr,
                                facecolor=halo, edgecolor="none",
                                alpha=a, zorder=8))
        ax.add_patch(Circle((bx, by), 0.40,
                            facecolor="white", edgecolor=edge,
                            lw=2.4, zorder=9))
        # tiny wave inside
        wx = np.linspace(bx - 0.24, bx + 0.24, 60)
        wy = by + 0.10 * np.sin((wx - bx) * (2 * np.pi * k_icon / 0.48))
        ax.plot(wx, wy, color=color, lw=2.4,
                solid_capstyle="round", zorder=10)

    # k1 badge near start of k1
    labeled_wave_badge(k1_start[0] - 0.05, k1_start[1] + 0.55,
                       color="#1aa6c7", halo="#9fe6f3", k_icon=2.0)
    # k2 badge near start of k2
    labeled_wave_badge(k2_start[0] - 0.05, k2_start[1] - 0.55,
                       color="#2fb27a", halo="#b6e7cf", k_icon=2.7)
    # k3 badge near end of k3
    labeled_wave_badge(k3_end[0] + 0.35, k3_end[1] + 0.55,
                       color="#c97a10", halo="#ffd98a", k_icon=3.4)

    # =============================================================
    # k-space vector triangle inset (bottom)
    # =============================================================
    # Draw a vector sum:  k1 + k2 = k3
    origin = (3.2, 2.1)
    vk1 = np.array([1.7, 0.45])
    vk2 = np.array([0.9, 1.25])
    vk3 = vk1 + vk2

    # panel background
    ax.add_patch(FancyBboxPatch(
        (origin[0] - 1.3, origin[1] - 0.4),
        4.5, 2.2,
        boxstyle="round,pad=0.04,rounding_size=0.15",
        facecolor="white", edgecolor="#1f3b57",
        lw=1.6, alpha=0.85, zorder=4,
    ))

    # small axes cross
    ax.plot([origin[0] - 0.3, origin[0] + 3.0],
            [origin[1], origin[1]],
            color="#1f3b57", lw=1.2, alpha=0.6, zorder=5)
    ax.plot([origin[0], origin[0]],
            [origin[1] - 0.3, origin[1] + 1.7],
            color="#1f3b57", lw=1.2, alpha=0.6, zorder=5)

    # vector k1
    p1 = (origin[0] + vk1[0], origin[1] + vk1[1])
    ax.annotate("", xy=p1, xytext=origin,
                arrowprops=dict(arrowstyle="-|>",
                                color="#1aa6c7", lw=3.0),
                zorder=7)
    # vector k2 tail at tip of k1
    p2 = (p1[0] + vk2[0], p1[1] + vk2[1])
    ax.annotate("", xy=p2, xytext=p1,
                arrowprops=dict(arrowstyle="-|>",
                                color="#2fb27a", lw=3.0),
                zorder=7)
    # resultant k3 from origin to tip
    ax.annotate("", xy=p2, xytext=origin,
                arrowprops=dict(arrowstyle="-|>",
                                color="#c97a10", lw=3.4),
                zorder=7)

    # small colored dots at the arrow tails for clarity
    ax.add_patch(Circle(origin, 0.09, facecolor="#1f3b57",
                        edgecolor="white", lw=1.4, zorder=8))
    # triangle closure hint: faint dashed line along k3
    # (already drawn as arrow — add subtle glow)
    for lw, a in [(8, 0.10), (5, 0.18)]:
        ax.plot([origin[0], p2[0]], [origin[1], p2[1]],
                color="#ffd98a", lw=lw, alpha=a, zorder=6,
                solid_capstyle="round")

    # ---- framing ---------------------------------------------------
    ax.set_xlim(0, 12)
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
