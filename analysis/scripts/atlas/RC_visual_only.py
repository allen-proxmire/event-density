"""
Debye / RC Exponential — visual-only illustration.

Metaphor: a discharging RC circuit.
  - TOP-LEFT : a clean electrical schematic — battery/source on the
               left, zigzag resistor along the top wire, parallel-plate
               capacitor on the right side of a closed loop.  Small
               amber current-flow arrows run around the wire.
  - MAIN     : a ρ(t) exponential decay curve from ρ₀ down to ρ*,
               with a glowing amber ρ* baseline.
  - ON THE CURVE : three snapshot points, each tagged by a small
               capacitor-icon badge showing the charge level at that
               time (full → half → almost empty), dashed guide lines
               connecting each point up to its capacitor badge.
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, FancyBboxPatch, Circle, FancyArrowPatch, Polygon,
)

OUT = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas\RC_debye.png"


def zigzag(x0, x1, y, n_zigs=6, amp=0.18):
    """Return xs, ys for a zigzag resistor shape between x0 and x1."""
    pts_x = [x0]
    pts_y = [y]
    span = x1 - x0
    # short flat leads on each side
    lead = span * 0.12
    core_x0 = x0 + lead
    core_x1 = x1 - lead
    pts_x.append(core_x0)
    pts_y.append(y)
    # zigzag peaks
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


def capacitor_icon(ax, cx, cy, scale=1.0, charge=1.0,
                   zorder=10):
    """A tiny parallel-plate capacitor.
    `charge` in [0,1] controls a glowing band between the plates.
    """
    plate_h = 0.55 * scale
    gap = 0.18 * scale
    plate_w = 0.06 * scale
    # left plate
    ax.add_patch(Rectangle((cx - gap / 2 - plate_w,
                            cy - plate_h / 2),
                           plate_w, plate_h,
                           facecolor="#7a4a0a", edgecolor="none",
                           zorder=zorder))
    # right plate
    ax.add_patch(Rectangle((cx + gap / 2, cy - plate_h / 2),
                           plate_w, plate_h,
                           facecolor="#7a4a0a", edgecolor="none",
                           zorder=zorder))
    # leads
    lead_w = 0.20 * scale
    ax.plot([cx - gap / 2 - plate_w - lead_w,
             cx - gap / 2 - plate_w],
            [cy, cy],
            color="#7a4a0a", lw=2.0 * scale, zorder=zorder)
    ax.plot([cx + gap / 2 + plate_w,
             cx + gap / 2 + plate_w + lead_w],
            [cy, cy],
            color="#7a4a0a", lw=2.0 * scale, zorder=zorder)
    # charge glow between plates
    if charge > 0.001:
        glow_w = gap * 0.85
        glow_h = plate_h * 0.9 * charge
        # soft halos
        for rr, a in [(glow_w * 1.3, 0.10),
                      (glow_w * 1.1, 0.20),
                      (glow_w * 0.95, 0.45)]:
            ax.add_patch(Rectangle(
                (cx - rr / 2, cy - glow_h / 2),
                rr, glow_h,
                facecolor="#ffd24a", edgecolor="none",
                alpha=a, zorder=zorder - 1,
            ))
        ax.add_patch(Rectangle(
            (cx - glow_w / 2, cy - glow_h / 2),
            glow_w, glow_h,
            facecolor="#ffb347", edgecolor="#c97a10",
            lw=1.0 * scale, zorder=zorder,
        ))


def build():
    fig, ax = plt.subplots(figsize=(12, 10), dpi=220)

    # ---- backdrop --------------------------------------------------
    grad = np.linspace(0, 1, 500).reshape(-1, 1)
    grad = np.tile(grad, (1, 500))
    ax.imshow(grad, extent=[0, 13, 0, 11], aspect="auto",
              cmap="Blues_r", alpha=0.18, zorder=0)
    ax.add_patch(Rectangle((0, 0), 13, 1.6,
                           facecolor="#fff4d6", alpha=0.55, zorder=0))

    # =============================================================
    # (A) Circuit schematic panel — top-left
    # =============================================================
    cx0, cx1 = 0.8, 5.2
    cy0, cy1 = 7.0, 10.3
    # panel background
    ax.add_patch(FancyBboxPatch(
        (cx0, cy0), cx1 - cx0, cy1 - cy0,
        boxstyle="round,pad=0.04,rounding_size=0.22",
        facecolor="white", edgecolor="#c97a10",
        lw=2.2, alpha=0.95, zorder=2,
    ))
    # inner pin-stripe
    ax.add_patch(FancyBboxPatch(
        (cx0 + 0.15, cy0 + 0.15),
        cx1 - cx0 - 0.30, cy1 - cy0 - 0.30,
        boxstyle="round,pad=0.02,rounding_size=0.18",
        facecolor="none", edgecolor="#d69a1a",
        lw=1.0, alpha=0.7, zorder=3,
    ))

    # Circuit geometry
    loop_x0, loop_x1 = cx0 + 0.55, cx1 - 0.55
    loop_y_top = cy1 - 0.65
    loop_y_bot = cy0 + 0.55

    wire_color = "#7a4a0a"
    # bottom wire
    ax.plot([loop_x0, loop_x1], [loop_y_bot, loop_y_bot],
            color=wire_color, lw=2.6, zorder=6,
            solid_capstyle="round")
    # left wire (battery segment goes here)
    ax.plot([loop_x0, loop_x0], [loop_y_bot, loop_y_top],
            color=wire_color, lw=2.6, zorder=6,
            solid_capstyle="round")
    # right wire (capacitor goes here)
    ax.plot([loop_x1, loop_x1], [loop_y_bot, loop_y_top],
            color=wire_color, lw=2.6, zorder=6,
            solid_capstyle="round")
    # top wire with resistor
    # break top wire where resistor sits
    res_x0 = loop_x0 + (loop_x1 - loop_x0) * 0.22
    res_x1 = loop_x0 + (loop_x1 - loop_x0) * 0.78
    ax.plot([loop_x0, res_x0], [loop_y_top, loop_y_top],
            color=wire_color, lw=2.6, zorder=6,
            solid_capstyle="round")
    ax.plot([res_x1, loop_x1], [loop_y_top, loop_y_top],
            color=wire_color, lw=2.6, zorder=6,
            solid_capstyle="round")
    # resistor zigzag
    zx, zy = zigzag(res_x0, res_x1, loop_y_top, n_zigs=5, amp=0.22)
    # glow
    for lw, col, a in [(7, "#ffd98a", 0.20),
                       (4.5, "#ffb347", 0.40)]:
        ax.plot(zx, zy, color=col, lw=lw, alpha=a,
                solid_capstyle="round", zorder=6)
    ax.plot(zx, zy, color="#c97a10", lw=2.6,
            solid_capstyle="round", zorder=7)

    # Battery on the left wire (two parallel bars)
    bat_y = (loop_y_top + loop_y_bot) / 2
    # short bar (negative)
    ax.plot([loop_x0 - 0.20, loop_x0 + 0.20],
            [bat_y - 0.16, bat_y - 0.16],
            color=wire_color, lw=3.2, solid_capstyle="round",
            zorder=8)
    # long bar (positive)
    ax.plot([loop_x0 - 0.30, loop_x0 + 0.30],
            [bat_y + 0.16, bat_y + 0.16],
            color=wire_color, lw=3.8, solid_capstyle="round",
            zorder=8)

    # Capacitor on the right wire
    cap_y = (loop_y_top + loop_y_bot) / 2
    # top plate
    ax.plot([loop_x1 - 0.30, loop_x1 + 0.30],
            [cap_y + 0.16, cap_y + 0.16],
            color=wire_color, lw=3.4, solid_capstyle="round",
            zorder=8)
    # bottom plate
    ax.plot([loop_x1 - 0.30, loop_x1 + 0.30],
            [cap_y - 0.16, cap_y - 0.16],
            color=wire_color, lw=3.4, solid_capstyle="round",
            zorder=8)
    # glowing charge band between plates (full charge in schematic)
    for rr, a in [(0.40, 0.10), (0.30, 0.22), (0.22, 0.45)]:
        ax.add_patch(Rectangle(
            (loop_x1 - rr / 2, cap_y - 0.12),
            rr, 0.24,
            facecolor="#ffd24a", edgecolor="none",
            alpha=a, zorder=7,
        ))
    ax.add_patch(Rectangle(
        (loop_x1 - 0.15, cap_y - 0.12),
        0.30, 0.24,
        facecolor="#ffb347", edgecolor="#c97a10",
        lw=1.2, zorder=8,
    ))

    # Current-flow arrows around the loop (small amber arrows)
    arrow_specs = [
        ((loop_x0 + 0.4, loop_y_bot), (loop_x0 + 1.1, loop_y_bot)),
        ((loop_x1 - 0.4, loop_y_bot), (loop_x1 - 1.1, loop_y_bot)),
        ((loop_x1, loop_y_top - 0.4), (loop_x1, loop_y_top - 1.1)),
        ((loop_x0, loop_y_top - 1.1), (loop_x0, loop_y_top - 0.4)),
    ]
    # Wait, for discharging current direction: capacitor → resistor → battery.
    # Simpler: just show rotating flow.  Keep four arrows evenly placed.
    loop_arrows = [
        # bottom: right-to-left (back to battery)
        ((loop_x1 - 0.85, loop_y_bot), (loop_x1 - 1.55, loop_y_bot)),
        # left wire: going up
        ((loop_x0, bat_y - 0.9), (loop_x0, bat_y - 1.55)),
        # top: left-to-right (but must skip resistor)
        ((loop_x0 + 0.35, loop_y_top),
         (loop_x0 + 0.95, loop_y_top)),
        # right wire: going down (capacitor → bottom)
        ((loop_x1, cap_y - 0.90), (loop_x1, cap_y - 1.55)),
    ]
    for p0, p1 in loop_arrows:
        ax.add_patch(FancyArrowPatch(
            p0, p1,
            arrowstyle="-|>", mutation_scale=16,
            color="#d69a1a", lw=2.2, zorder=9,
        ))

    # =============================================================
    # (B) ρ(t) decay curve — main area
    # =============================================================
    ax_x0, ax_x1 = 1.1, 12.1
    ax_y0 = 2.3         # ρ* baseline (bottom)
    ax_y_top = 6.0      # top of plot region

    # plot panel background
    ax.add_patch(FancyBboxPatch(
        (ax_x0 - 0.28, ax_y0 - 0.40),
        ax_x1 - ax_x0 + 0.56,
        ax_y_top - ax_y0 + 0.70,
        boxstyle="round,pad=0.04,rounding_size=0.20",
        facecolor="white", edgecolor="#1f3b57",
        lw=1.5, alpha=0.88, zorder=2,
    ))

    # glowing ρ* baseline
    for glow_h, a in [(0.60, 0.06), (0.40, 0.12),
                      (0.24, 0.22), (0.14, 0.38), (0.08, 0.65)]:
        ax.add_patch(Rectangle(
            (ax_x0, ax_y0 - glow_h / 2),
            ax_x1 - ax_x0, glow_h,
            facecolor="#ffc23a", edgecolor="none",
            alpha=a, zorder=3,
        ))
    ax.plot([ax_x0, ax_x1], [ax_y0, ax_y0],
            color="#ff9f1a", lw=4.5, zorder=5,
            solid_capstyle="round")
    ax.plot([ax_x0, ax_x1], [ax_y0, ax_y0],
            color="#fff1b0", lw=1.8, zorder=6,
            solid_capstyle="round")

    # y-axis
    ax.plot([ax_x0, ax_x0], [ax_y0, ax_y_top],
            color="#1f3b57", lw=1.6, alpha=0.75, zorder=4)
    # t-axis arrow (below ρ*)
    ax.annotate("", xy=(ax_x1 - 0.08, ax_y0 - 0.45),
                xytext=(ax_x0, ax_y0 - 0.45),
                arrowprops=dict(arrowstyle="-|>",
                                color="#1f3b57", lw=1.8),
                zorder=5)

    # decay curve ρ(t) = ρ* + (ρ₀ − ρ*) e^{−t/τ}
    ts = np.linspace(ax_x0 + 0.25, ax_x1 - 0.25, 500)
    tn = (ts - ts[0]) / (ts[-1] - ts[0])
    rho0_top = ax_y_top - 0.25
    decay = (rho0_top - ax_y0) * np.exp(-3.2 * tn) + ax_y0

    # shaded area under curve
    ax.fill_between(ts, ax_y0, decay,
                    color="#ffd98a", alpha=0.33, zorder=4)
    # glow strokes
    for lw, col, a in [(12, "#ffd98a", 0.14),
                       (7, "#ffb347", 0.26),
                       (4.0, "#c97a10", 0.95)]:
        ax.plot(ts, decay, color=col, lw=lw, alpha=a,
                solid_capstyle="round", zorder=6)

    # =============================================================
    # (C) Three snapshot points + capacitor badges
    # =============================================================
    # normalized times for three snapshots: t_small, t_mid, t_late
    snap_tn = [0.06, 0.32, 0.80]
    charges = [0.95, 0.42, 0.10]

    # corresponding x and y on curve
    for t_val, q in zip(snap_tn, charges):
        x_pt = ts[0] + t_val * (ts[-1] - ts[0])
        y_pt = (rho0_top - ax_y0) * np.exp(-3.2 * t_val) + ax_y0
        # glowing dot on curve
        for rr, a in [(0.32, 0.14), (0.22, 0.30)]:
            ax.add_patch(Circle((x_pt, y_pt), rr,
                                facecolor="#ffd98a",
                                edgecolor="none", alpha=a, zorder=7))
        ax.add_patch(Circle((x_pt, y_pt), 0.14,
                            facecolor="#ffb347",
                            edgecolor="#7a4a0a", lw=1.6, zorder=9))

        # dashed guide upward to the capacitor badge
        badge_y = ax_y_top + 0.55
        ax.plot([x_pt, x_pt], [y_pt + 0.16, badge_y - 0.42],
                color="#7a4a0a", lw=1.0, alpha=0.50,
                linestyle=(0, (3, 3)), zorder=5)

        # capacitor badge (rounded square with cap-icon inside)
        bw, bh = 1.10, 0.92
        bx0 = x_pt - bw / 2
        by0 = badge_y - bh / 2
        # halo
        for pad, a in [(0.18, 0.10), (0.10, 0.18)]:
            ax.add_patch(FancyBboxPatch(
                (bx0 - pad, by0 - pad), bw + 2 * pad, bh + 2 * pad,
                boxstyle="round,pad=0.02,rounding_size=0.18",
                facecolor="#ffd24a", edgecolor="none",
                alpha=a, zorder=7,
            ))
        ax.add_patch(FancyBboxPatch(
            (bx0, by0), bw, bh,
            boxstyle="round,pad=0.02,rounding_size=0.18",
            facecolor="white", edgecolor="#c97a10",
            lw=2.0, zorder=8,
        ))
        # capacitor icon inside the badge
        capacitor_icon(ax, x_pt, badge_y, scale=1.3,
                       charge=q, zorder=10)

    # =============================================================
    # (D) Connector from circuit schematic to the curve
    # =============================================================
    # short arrow from the schematic's capacitor outward/down to the curve's first snapshot
    first_snap_x = ts[0] + snap_tn[0] * (ts[-1] - ts[0])
    first_snap_y = (rho0_top - ax_y0) * np.exp(-3.2 * snap_tn[0]) + ax_y0
    ax.annotate("", xy=(first_snap_x, first_snap_y + 0.22),
                xytext=(loop_x1 - 0.15, loop_y_bot - 0.12),
                arrowprops=dict(arrowstyle="-|>",
                                color="#c97a10", lw=2.0, alpha=0.75,
                                connectionstyle="arc3,rad=0.25",
                                linestyle=(0, (4, 3))),
                zorder=7)

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
