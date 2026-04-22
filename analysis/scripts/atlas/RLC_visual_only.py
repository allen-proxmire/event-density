"""
Telegraph / RLC Oscillator — visual-only illustration.

Metaphor: an RLC electrical loop ringing down.  Distinct from the
mass-spring-damper rigs of P6 and from the step-response of the
Participation channel — here the emphasis is on the HOMOGENEOUS
oscillation (no forcing) decaying through R.

Composition:
  TOP-LEFT  : a stylized RLC circuit — inductor coil on the top wire,
              capacitor plates on the right, resistor zigzag on the
              bottom, connected into a closed loop with a glowing
              current pulse indicator.
  MAIN AREA : a clean damped-sinusoid v(t) waveform with its
              exponential envelope drawn faintly above/below.  Peaks
              dotted and glow-tagged.  Time axis runs along bottom.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\RLC_oscillator.png"


def inductor_coil(x0, x1, y, n_loops=5, r=0.20):
    """Return (xs, ys) for an inductor coil shape between x0 and x1."""
    # short flat leads
    lead = (x1 - x0) * 0.10
    core_x0 = x0 + lead
    core_x1 = x1 - lead
    xs = [x0, core_x0]
    ys = [y, y]
    loop_span = (core_x1 - core_x0) / n_loops
    for k in range(n_loops):
        cx = core_x0 + (k + 0.5) * loop_span
        th = np.linspace(np.pi, 0, 30)
        lx = cx + (loop_span / 2) * np.cos(th)
        ly = y + r * np.sin(th)
        xs.extend(lx.tolist())
        ys.extend(ly.tolist())
    xs.extend([core_x1, x1])
    ys.extend([y, y])
    return np.array(xs), np.array(ys)


def zigzag(x0, x1, y, n_zigs=5, amp=0.20):
    lead = (x1 - x0) * 0.12
    core_x0 = x0 + lead
    core_x1 = x1 - lead
    pts_x = [x0, core_x0]
    pts_y = [y, y]
    seg = (core_x1 - core_x0) / (n_zigs * 2)
    for k in range(n_zigs * 2):
        cx = core_x0 + (k + 0.5) * seg
        peak = amp if k % 2 == 0 else -amp
        pts_x.append(cx)
        pts_y.append(y + peak)
    pts_x.append(core_x1)
    pts_y.append(y)
    pts_x.append(x1)
    pts_y.append(y)
    return np.array(pts_x), np.array(pts_y)


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
    # (A) RLC circuit schematic — top-left
    # =============================================================
    cx0, cx1 = 0.8, 5.6
    cy0, cy1 = 6.9, 10.3
    # outer panel
    ax.add_patch(FancyBboxPatch(
        (cx0, cy0), cx1 - cx0, cy1 - cy0,
        boxstyle="round,pad=0.04,rounding_size=0.22",
        facecolor="white", edgecolor="#c94419",
        lw=2.4, alpha=0.95, zorder=2,
    ))
    # inner pin-stripe
    ax.add_patch(FancyBboxPatch(
        (cx0 + 0.15, cy0 + 0.15),
        cx1 - cx0 - 0.30, cy1 - cy0 - 0.30,
        boxstyle="round,pad=0.02,rounding_size=0.18",
        facecolor="none", edgecolor="#f46d3b",
        lw=1.0, alpha=0.7, zorder=3,
    ))

    # loop geometry
    lx0, lx1 = cx0 + 0.55, cx1 - 0.55
    ly_top = cy1 - 0.65
    ly_bot = cy0 + 0.55
    wire_col = "#7a2d0b"

    # wires: left and right (simple verticals)
    ax.plot([lx0, lx0], [ly_bot, ly_top],
            color=wire_col, lw=2.6, zorder=6, solid_capstyle="round")
    ax.plot([lx1, lx1], [ly_bot, ly_top],
            color=wire_col, lw=2.6, zorder=6, solid_capstyle="round")

    # TOP wire with inductor coil
    ind_x0 = lx0 + (lx1 - lx0) * 0.22
    ind_x1 = lx0 + (lx1 - lx0) * 0.78
    ax.plot([lx0, ind_x0], [ly_top, ly_top],
            color=wire_col, lw=2.6, zorder=6, solid_capstyle="round")
    ax.plot([ind_x1, lx1], [ly_top, ly_top],
            color=wire_col, lw=2.6, zorder=6, solid_capstyle="round")
    ix, iy = inductor_coil(ind_x0, ind_x1, ly_top, n_loops=5, r=0.22)
    for lw, col, a in [(7, "#ffb08a", 0.25),
                       (4.5, "#f46d3b", 0.50)]:
        ax.plot(ix, iy, color=col, lw=lw, alpha=a,
                solid_capstyle="round", zorder=6)
    ax.plot(ix, iy, color="#c94419", lw=2.6,
            solid_capstyle="round", zorder=7)

    # BOTTOM wire with resistor
    res_x0 = lx0 + (lx1 - lx0) * 0.22
    res_x1 = lx0 + (lx1 - lx0) * 0.78
    ax.plot([lx0, res_x0], [ly_bot, ly_bot],
            color=wire_col, lw=2.6, zorder=6, solid_capstyle="round")
    ax.plot([res_x1, lx1], [ly_bot, ly_bot],
            color=wire_col, lw=2.6, zorder=6, solid_capstyle="round")
    zx, zy = zigzag(res_x0, res_x1, ly_bot, n_zigs=5, amp=0.18)
    for lw, col, a in [(7, "#9fe6f3", 0.22),
                       (4.5, "#5b6b80", 0.55)]:
        ax.plot(zx, zy, color=col, lw=lw, alpha=a,
                solid_capstyle="round", zorder=6)
    ax.plot(zx, zy, color="#2f4d6b", lw=2.4,
            solid_capstyle="round", zorder=7)

    # RIGHT wire break — capacitor
    cap_y = (ly_top + ly_bot) / 2
    # break the right wire near the capacitor
    ax.plot([lx1, lx1], [ly_bot, cap_y - 0.20],
            color=wire_col, lw=2.6, zorder=6, solid_capstyle="round")
    ax.plot([lx1, lx1], [cap_y + 0.20, ly_top],
            color=wire_col, lw=2.6, zorder=6, solid_capstyle="round")
    # plates
    ax.plot([lx1 - 0.30, lx1 + 0.30],
            [cap_y + 0.16, cap_y + 0.16],
            color=wire_col, lw=3.4, solid_capstyle="round", zorder=8)
    ax.plot([lx1 - 0.30, lx1 + 0.30],
            [cap_y - 0.16, cap_y - 0.16],
            color=wire_col, lw=3.4, solid_capstyle="round", zorder=8)
    # glow between plates
    for rr, a in [(0.40, 0.10), (0.30, 0.22), (0.22, 0.45)]:
        ax.add_patch(Rectangle(
            (lx1 - rr / 2, cap_y - 0.12),
            rr, 0.24,
            facecolor="#ffd24a", edgecolor="none",
            alpha=a, zorder=7,
        ))
    ax.add_patch(Rectangle(
        (lx1 - 0.15, cap_y - 0.12),
        0.30, 0.24,
        facecolor="#ff9f1a", edgecolor="#7a4a0a",
        lw=1.2, zorder=8,
    ))

    # circulating current pulse — a glowing dot cluster traveling the wire
    # Put a cluster on the top-right curve going clockwise
    for (px, py, rr, a) in [
        (lx0 + (lx1 - lx0) * 0.55, ly_top + 0.24, 0.18, 0.70),
        (lx1, ly_top - 0.55, 0.14, 0.50),
        (lx1 - 0.1, cap_y + 0.50, 0.12, 0.35),
    ]:
        for rrH, aH in [(rr * 2.0, 0.18),
                        (rr * 1.5, 0.32),
                        (rr * 1.1, 0.55)]:
            ax.add_patch(Circle((px, py), rrH,
                                facecolor="#ffd24a",
                                edgecolor="none",
                                alpha=a * aH, zorder=9))
        ax.add_patch(Circle((px, py), rr * 0.55,
                            facecolor="#ff9f1a",
                            edgecolor="#7a2d0b", lw=1.0,
                            alpha=a, zorder=10))

    # a circulating arrow hint in the loop interior (clockwise)
    th_circ = np.linspace(np.pi * 0.55, np.pi * 0.10, 20)
    cc = ((lx0 + lx1) / 2, (ly_top + ly_bot) / 2)
    rcir = 0.75
    arc_x = cc[0] + rcir * np.cos(th_circ)
    arc_y = cc[1] + rcir * np.sin(th_circ)
    ax.plot(arc_x, arc_y, color="#c94419", lw=2.0,
            alpha=0.5, solid_capstyle="round", zorder=8)
    ax.annotate("", xy=(arc_x[-1], arc_y[-1]),
                xytext=(arc_x[-3], arc_y[-3]),
                arrowprops=dict(arrowstyle="-|>",
                                color="#c94419", lw=2.0, alpha=0.7),
                zorder=8)

    # =============================================================
    # (B) Damped sinusoid v(t) in main area
    # =============================================================
    ax_x0, ax_x1 = 0.9, 13.3
    ax_y_mid = 3.8          # midline (zero crossing)
    ax_y_top = 6.5          # top extent
    ax_y_bot = 1.8          # bottom extent

    # plot panel background
    ax.add_patch(FancyBboxPatch(
        (ax_x0 - 0.15, ax_y_bot - 0.20),
        ax_x1 - ax_x0 + 0.30,
        ax_y_top - ax_y_bot + 0.45,
        boxstyle="round,pad=0.04,rounding_size=0.20",
        facecolor="white", edgecolor="#1f3b57",
        lw=1.5, alpha=0.88, zorder=2,
    ))

    # midline
    ax.plot([ax_x0 + 0.1, ax_x1 - 0.1], [ax_y_mid, ax_y_mid],
            color="#1f3b57", lw=1.2, alpha=0.35,
            linestyle=(0, (5, 4)), zorder=4)

    # y-axis
    ax.plot([ax_x0 + 0.15, ax_x0 + 0.15], [ax_y_bot + 0.1, ax_y_top - 0.1],
            color="#1f3b57", lw=1.6, alpha=0.75, zorder=4)
    # t-axis arrow
    ax.annotate("", xy=(ax_x1 - 0.18, ax_y_mid),
                xytext=(ax_x0 + 0.15, ax_y_mid),
                arrowprops=dict(arrowstyle="-|>", color="#1f3b57",
                                lw=1.4, alpha=0.0),  # invisible; we use dashed midline instead
                zorder=4)

    # generate the damped sinusoid
    ts = np.linspace(ax_x0 + 0.5, ax_x1 - 0.35, 900)
    tn = (ts - ts[0]) / (ts[-1] - ts[0])
    zeta = 0.14       # lightly damped for visible rings
    wn = 24.0         # ringing frequency
    wd = wn * np.sqrt(1 - zeta ** 2)
    t_scaled = tn
    A0 = min((ax_y_top - ax_y_mid), (ax_y_mid - ax_y_bot)) * 0.92
    env = A0 * np.exp(-zeta * wn * t_scaled)
    v = env * np.cos(wd * t_scaled)
    y_curve = ax_y_mid + v

    # envelope curves (top & bottom, faint)
    y_env_top = ax_y_mid + env
    y_env_bot = ax_y_mid - env
    for yarr, col in [(y_env_top, "#f46d3b"),
                      (y_env_bot, "#f46d3b")]:
        for lw, a in [(9, 0.08), (5, 0.14)]:
            ax.plot(ts, yarr, color=col, lw=lw, alpha=a,
                    solid_capstyle="round", zorder=5)
        ax.plot(ts, yarr, color="#f46d3b", lw=1.6, alpha=0.55,
                linestyle=(0, (6, 4)), zorder=6)

    # shade between envelopes (very soft)
    ax.fill_between(ts, y_env_bot, y_env_top,
                    color="#ffd4b0", alpha=0.18, zorder=5)

    # main damped sinusoid with glow
    for lw, col, a in [(12, "#ffd4b0", 0.14),
                       (8, "#ffae79", 0.22),
                       (4.0, "#c94419", 0.98)]:
        ax.plot(ts, y_curve, color=col, lw=lw, alpha=a,
                solid_capstyle="round", zorder=7)

    # ---- mark peaks with glowing dots -----------------------------
    # Peaks occur at zeros of derivative; approximate with cos' = 0
    # For simplicity, find local maxima numerically.
    peaks = []
    for i in range(1, len(y_curve) - 1):
        if y_curve[i - 1] < y_curve[i] > y_curve[i + 1]:
            if y_curve[i] > ax_y_mid + 0.08:
                peaks.append(i)
    # take first 4 peaks
    peaks = peaks[:4]
    for i in peaks:
        px, py = ts[i], y_curve[i]
        for rr, a in [(0.35, 0.14), (0.24, 0.28)]:
            ax.add_patch(Circle((px, py), rr,
                                facecolor="#ffd4b0",
                                edgecolor="none", alpha=a, zorder=8))
        ax.add_patch(Circle((px, py), 0.14,
                            facecolor="#ffae79",
                            edgecolor="#7a2d0b", lw=1.6, zorder=10))

    # ---- connector from capacitor to the first peak of the curve --
    first_peak_x, first_peak_y = ts[peaks[0]], y_curve[peaks[0]]
    ax.annotate("", xy=(first_peak_x, first_peak_y + 0.25),
                xytext=(lx1 + 0.18, cap_y - 0.3),
                arrowprops=dict(arrowstyle="-|>",
                                color="#c94419", lw=2.0, alpha=0.75,
                                connectionstyle="arc3,rad=-0.25",
                                linestyle=(0, (4, 3))),
                zorder=7)

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
