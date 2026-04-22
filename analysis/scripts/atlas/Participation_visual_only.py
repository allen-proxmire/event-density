"""
Participation channel alone — visual-only illustration.

Metaphor: a driven-damped temporal response.  No spatial structure,
only a time-trace.

Composition (left-to-right):
  LEFT   : a pulsing cyan input node — the driver F[ρ] — with three
           expanding wave rings radiating outward (stylized "pulse").
  MIDDLE : a thick, glowing ν(t) response curve that rises from zero,
           peaks, slightly overshoots, and damps toward a steady state.
           Shaded soft fill underneath for readability.
  RIGHT  : the curve settles into a small warm-orange "settled" node
           with a faint halo.  Below the whole composition: a time axis.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\Participation_alone.png"


def build():
    fig, ax = plt.subplots(figsize=(12, 9), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 13, 0, 10], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 13, 1.5,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # =============================================================
    # Layout params
    # =============================================================
    t_axis_y = 2.0              # time axis baseline
    resp_mid = 5.2              # steady-state asymptote height
    peak_h = resp_mid + 2.3     # peak of the rising response
    trough_h = resp_mid - 0.5   # small overshoot trough
    x0_panel, x1_panel = 0.6, 12.4

    # =============================================================
    # (1) Time axis
    # =============================================================
    ax.plot([x0_panel, x1_panel], [t_axis_y, t_axis_y],
            color="#1f3b57", lw=1.8, alpha=0.85, zorder=4)
    ax.annotate("",
                xy=(x1_panel, t_axis_y),
                xytext=(x0_panel, t_axis_y),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1f3b57", lw=1.8),
                zorder=5)

    # faint horizontal asymptote (steady-state level)
    ax.plot([x0_panel, x1_panel], [resp_mid, resp_mid],
            color="#1f3b57", lw=0.9, alpha=0.30,
            linestyle=(0, (5, 4)), zorder=4)

    # =============================================================
    # (2) Pulsing input node on the left — F[ρ] driver
    # =============================================================
    in_cx, in_cy = 1.6, resp_mid
    # expanding ring "pulses"
    for rr, a, lw in [(1.30, 0.14, 2.4),
                      (0.95, 0.28, 2.6),
                      (0.62, 0.55, 2.8)]:
        ax.add_patch(Circle((in_cx, in_cy), rr,
                            facecolor="none", edgecolor="#1aa6c7",
                            lw=lw, alpha=a, zorder=5))

    # soft halo
    for rr, a in [(0.75, 0.10), (0.55, 0.20), (0.40, 0.38)]:
        ax.add_patch(Circle((in_cx, in_cy), rr,
                            facecolor="#9fe6f3", edgecolor="none",
                            alpha=a, zorder=5))
    # body
    ax.add_patch(Circle((in_cx, in_cy), 0.35,
                        facecolor="#57c6e6", edgecolor="#0b4a68",
                        lw=2.2, zorder=7))
    # highlight
    ax.add_patch(Circle((in_cx - 0.12, in_cy + 0.12), 0.12,
                        facecolor="white", alpha=0.80, zorder=8))

    # little "waveform" icon on top of the input node — the F[ρ] cue
    wx = np.linspace(in_cx - 0.18, in_cx + 0.18, 30)
    wy = in_cy + 0.05 * np.sin((wx - in_cx) * 30)
    ax.plot(wx, wy, color="white", lw=1.6,
            solid_capstyle="round", zorder=9)

    # =============================================================
    # (3) Driven-damped ν(t) response curve
    # =============================================================
    # time grid: response starts just after the input node
    ts = np.linspace(in_cx + 0.45, x1_panel - 0.6, 700)
    tn = (ts - ts[0]) / (ts[-1] - ts[0])

    # Standard underdamped second-order step response:
    #   y(t) = 1 - e^{-ζω_n t} [cos(ω_d t) + (ζ/√(1-ζ²)) sin(ω_d t)]
    # At t=0 -> 0.  Rises, overshoots once, settles to 1.
    zeta = 0.22
    wn = 10.0
    wd = wn * np.sqrt(1 - zeta ** 2)
    t_scaled = tn * 1.6           # stretch so the whole response fits nicely
    exp_env = np.exp(-zeta * wn * t_scaled)
    y = 1.0 - exp_env * (np.cos(wd * t_scaled)
                         + (zeta / np.sqrt(1 - zeta ** 2))
                         * np.sin(wd * t_scaled))

    # scale into panel coordinates: y=1 (final steady-state) → resp_mid
    # peak overshoot (~1.49 for ζ=0.22) will sit ~1.5× higher.
    rise_unit = resp_mid - t_axis_y
    resp = t_axis_y + y * rise_unit

    # shaded area under the curve
    ax.fill_between(ts, t_axis_y, resp,
                    color="#ffb08a", alpha=0.28, zorder=5)

    # glow passes
    for lw, col, a_ in [(14, "#ffd4b0", 0.12),
                        (9, "#ffae79", 0.24),
                        (5, "#f46d3b", 0.55)]:
        ax.plot(ts, resp, color=col, lw=lw, alpha=a_,
                solid_capstyle="round", zorder=6)

    # crisp stroke
    ax.plot(ts, resp, color="#c94419", lw=3.0, alpha=0.98,
            solid_capstyle="round", zorder=7)

    # ---- peak marker (brightest glow bubble) ----------------------
    peak_idx = np.argmax(resp)
    peak_x = ts[peak_idx]
    peak_y = resp[peak_idx]
    for rr, a in [(0.55, 0.08), (0.38, 0.18),
                  (0.26, 0.35), (0.18, 0.60)]:
        ax.add_patch(Circle((peak_x, peak_y), rr,
                            facecolor="#ffd98a", edgecolor="none",
                            alpha=a, zorder=7))
    ax.add_patch(Circle((peak_x, peak_y), 0.13,
                        facecolor="#ffae79", edgecolor="#c94419",
                        lw=1.8, zorder=9))

    # ---- "settled" node at the right — end of the response -------
    set_x, set_y = ts[-1], resp[-1]
    for rr, a in [(0.65, 0.09), (0.45, 0.20), (0.32, 0.38)]:
        ax.add_patch(Circle((set_x, set_y), rr,
                            facecolor="#ffae79", edgecolor="none",
                            alpha=a, zorder=7))
    ax.add_patch(Circle((set_x, set_y), 0.25,
                        facecolor="#f46d3b", edgecolor="#7a2d0b",
                        lw=2.0, zorder=9))
    ax.add_patch(Circle((set_x - 0.08, set_y + 0.08), 0.08,
                        facecolor="white", alpha=0.80, zorder=10))

    # faint guide line from peak down to time-axis tick
    ax.plot([peak_x, peak_x],
            [t_axis_y, peak_y - 0.08],
            color="#c94419", lw=1.0, alpha=0.35,
            linestyle=(0, (3, 3)), zorder=5)

    # =============================================================
    # (4) Connector from input node to the start of the response
    # =============================================================
    con_x0 = in_cx + 0.40
    con_x1 = ts[0] - 0.05
    con_y = t_axis_y + 0.15
    # small glowing arc connector
    for lw, col, a in [(8, "#9fe6f3", 0.12),
                       (5, "#6fd2e9", 0.22)]:
        ax.plot([con_x0, con_x1], [in_cy - 0.20, con_y],
                color=col, lw=lw, alpha=a,
                solid_capstyle="round", zorder=4)
    arrow_c = FancyArrowPatch(
        (con_x0, in_cy - 0.22),
        (con_x1, con_y),
        arrowstyle="-|>", mutation_scale=18,
        color="#1aa6c7", lw=2.4, zorder=6,
    )
    ax.add_patch(arrow_c)

    # =============================================================
    # (5) Small badges for clarity
    # =============================================================
    # "τ" badge above input arrow (time-constant cue): a stylized clock
    tb_x, tb_y = (con_x0 + con_x1) / 2, in_cy + 0.75
    ax.add_patch(Circle((tb_x, tb_y), 0.30,
                        facecolor="white", edgecolor="#1aa6c7",
                        lw=2.0, zorder=9))
    ax.add_patch(Circle((tb_x, tb_y), 0.05,
                        facecolor="#1aa6c7", zorder=10))
    ax.plot([tb_x, tb_x + 0.16], [tb_y, tb_y + 0.12],
            color="#1aa6c7", lw=1.8,
            solid_capstyle="round", zorder=10)
    ax.plot([tb_x, tb_x - 0.10], [tb_y, tb_y + 0.16],
            color="#1aa6c7", lw=1.5, alpha=0.7,
            solid_capstyle="round", zorder=10)

    # "damping" badge hovering above the tail of the response curve
    db_x, db_y = set_x - 1.0, set_y + 0.85
    ax.add_patch(Circle((db_x, db_y), 0.30,
                        facecolor="white", edgecolor="#5b6b80",
                        lw=2.0, zorder=9))
    # decay curve icon
    dx = np.linspace(db_x - 0.22, db_x + 0.22, 60)
    dt_ = (dx - dx[0]) / (dx[-1] - dx[0])
    dy_ = db_y - 0.18 + 0.36 * np.exp(-3.5 * dt_)
    ax.plot(dx, dy_, color="#5b6b80", lw=2.0,
            solid_capstyle="round", zorder=10)
    # connector from damping badge to the settled tail
    ax.plot([db_x, set_x - 0.25], [db_y - 0.30, set_y + 0.10],
            color="#5b6b80", lw=1.2, alpha=0.55,
            linestyle=(0, (3, 3)), zorder=6)

    # =============================================================
    # (6) Tiny ticks and legend dots on the left
    # =============================================================
    # a small legend dot on the y-axis region — input color + response color
    leg_x = x0_panel + 0.10
    ax.add_patch(Circle((leg_x, resp_mid + 1.7), 0.10,
                        facecolor="#57c6e6",
                        edgecolor="#0b4a68", lw=1.0, zorder=7))
    ax.add_patch(Circle((leg_x, resp_mid + 1.3), 0.10,
                        facecolor="#f46d3b",
                        edgecolor="#7a2d0b", lw=1.0, zorder=7))

    # ---- framing ---------------------------------------------------
    ax.set_xlim(0, 13)
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
