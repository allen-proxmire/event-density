"""
Generate Figure 1 for the foundational paper:
A schematic of the three constitutive channels of the canonical ED PDE.

Layout:
  Top:    The full canonical PDE
  Middle: Three boxes (Mobility | Penalty | Participation), each with
            - operator (math)
            - small inset plot showing the characteristic dynamics
            - physical correspondence (label)
  Bottom: One-line summary

Output: outputs/figures/channels_schematic.png
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.lines import Line2D


# ── Colours ────────────────────────────────────────────────────────
NAVY = "#1E3A8A"
BLUE = "#2563EB"
RED = "#DC2626"
GREEN = "#059669"
DIM = "#6B7280"
LIGHT_BG = "#F8FAFC"
BORDER = "#CBD5E1"


def channel_box(ax, x0, y0, w, h, title, equation, plot_func, physical, color):
    """Draw one channel box with title bar, equation, inset plot, label."""
    # Outer rounded box
    box = FancyBboxPatch(
        (x0, y0), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.06",
        linewidth=1.5, edgecolor=BORDER, facecolor=LIGHT_BG, zorder=1,
    )
    ax.add_patch(box)

    # Title bar (top ~12% of box height)
    bar_h = 0.40
    title_bar = FancyBboxPatch(
        (x0, y0 + h - bar_h), w, bar_h,
        boxstyle="round,pad=0.02,rounding_size=0.06",
        linewidth=0, facecolor=color, zorder=2,
    )
    ax.add_patch(title_bar)

    # Title text
    ax.text(x0 + w / 2, y0 + h - bar_h / 2, title,
            ha="center", va="center", fontsize=15, fontweight="bold",
            color="white", zorder=3)

    # Equation (just below title bar)
    ax.text(x0 + w / 2, y0 + h - bar_h - 0.40, equation,
            ha="center", va="center", fontsize=15, color="black", zorder=3)

    # Inset plot (occupies the middle band)
    inset_left = x0 + 0.30
    inset_width = w - 0.60
    inset_bottom = y0 + 0.85
    inset_height = h - bar_h - 1.40

    fig = ax.figure
    bbox_data = ax.transData.transform([
        [inset_left, inset_bottom],
        [inset_left + inset_width, inset_bottom + inset_height],
    ])
    bbox_fig = fig.transFigure.inverted().transform(bbox_data)
    inset_ax = fig.add_axes([
        bbox_fig[0, 0], bbox_fig[0, 1],
        bbox_fig[1, 0] - bbox_fig[0, 0],
        bbox_fig[1, 1] - bbox_fig[0, 1],
    ])
    plot_func(inset_ax, color)

    # Style the inset
    inset_ax.set_xticks([])
    inset_ax.set_yticks([])
    for spine in ["top", "right"]:
        inset_ax.spines[spine].set_visible(False)
    for spine in ["left", "bottom"]:
        inset_ax.spines[spine].set_color("#9CA3AF")
        inset_ax.spines[spine].set_linewidth(0.8)
    inset_ax.set_facecolor("white")

    # Physical correspondence label (bottom)
    ax.text(x0 + w / 2, y0 + 0.40, physical,
            ha="center", va="center", fontsize=10.5,
            color=DIM, fontstyle="italic", zorder=3,
            linespacing=1.4)


def plot_mobility(ax, color):
    """Compact-support spreading: profiles at three times."""
    x = np.linspace(-3, 3, 400)
    for i, (t, alpha) in enumerate([(0.3, 0.35), (1.0, 0.65), (3.0, 1.0)]):
        # Barenblatt-like compactly supported profile
        R = 0.8 * t ** 0.27
        peak = 1.0 / t ** 0.27
        inner = np.maximum(1 - (x / R) ** 2, 0)
        u = peak * inner ** (1 / 1.69)
        ax.plot(x, u, "-", color=color, linewidth=1.8, alpha=alpha)
        ax.fill_between(x, u, 0, color=color, alpha=alpha * 0.15)
    ax.set_xlim(-3, 3)
    ax.set_ylim(0, 1.4)
    ax.axhline(0, color="#9CA3AF", linewidth=0.6)


def plot_penalty(ax, color):
    """Pure exponential decay on log scale."""
    t = np.linspace(0, 5, 200)
    y = np.exp(-t)
    ax.plot(t, y, "-", color=color, linewidth=2.2)
    ax.fill_between(t, y, 0, color=color, alpha=0.15)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1.05)
    ax.axhline(0, color="#9CA3AF", linewidth=0.6)


def plot_participation(ax, color):
    """Damped oscillation."""
    t = np.linspace(0, 12, 400)
    y = np.exp(-0.18 * t) * np.cos(1.2 * t)
    ax.plot(t, y, "-", color=color, linewidth=2.0)
    ax.fill_between(t, y, 0, color=color, alpha=0.12)
    ax.set_xlim(0, 12)
    ax.set_ylim(-1.0, 1.0)
    ax.axhline(0, color="#9CA3AF", linewidth=0.6)


def main():
    fig = plt.figure(figsize=(14, 8), dpi=120)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.set_aspect("equal")
    ax.axis("off")

    # ── Top: full canonical PDE ─────────────────────────────────────
    pde_text = (
        r"$\partial_t \rho \;=\; D\,[\,\nabla\!\cdot\!(M(\rho)\,\nabla\rho) "
        r"\;-\; P(\rho)\,] \;+\; H\,v\,, "
        r"\qquad \dot v \;=\; (\bar F - \zeta v)/\tau$"
    )
    ax.text(7.0, 7.30, pde_text, ha="center", va="center", fontsize=16,
            color="black")

    ax.text(7.0, 6.75, "The Canonical ED PDE  —  three constitutive channels",
            ha="center", va="center", fontsize=11, color=DIM, fontstyle="italic")

    # ── Vertical separator arrows from PDE down to boxes ───────────
    for target_x in [2.40, 7.00, 11.60]:
        ax.annotate(
            "", xy=(target_x, 6.20), xytext=(7.0, 6.45),
            arrowprops=dict(arrowstyle="->", color=BORDER, linewidth=1.2),
        )

    # ── Three channel boxes ─────────────────────────────────────────
    box_w = 4.0
    box_h = 5.5
    box_y = 0.45

    # Mobility
    channel_box(
        ax, x0=0.40, y0=box_y, w=box_w, h=box_h,
        title="MOBILITY",
        equation=r"$\nabla\!\cdot\!\,[\,M(\rho)\,\nabla\rho\,]$",
        plot_func=plot_mobility,
        physical="Porous-medium equation\n(Barenblatt spreading)",
        color=BLUE,
    )

    # Penalty
    channel_box(
        ax, x0=5.00, y0=box_y, w=box_w, h=box_h,
        title="PENALTY",
        equation=r"$-\,P(\rho) = -P_0(\rho - \rho^{*})$",
        plot_func=plot_penalty,
        physical="RC circuit / Debye decay\n(exponential relaxation)",
        color=RED,
    )

    # Participation
    channel_box(
        ax, x0=9.60, y0=box_y, w=box_w, h=box_h,
        title="PARTICIPATION",
        equation=r"$+\,H\,v(t)$",
        plot_func=plot_participation,
        physical="Telegraph / RLC circuit\n(damped oscillation)",
        color=GREEN,
    )

    # ── Save ───────────────────────────────────────────────────────
    script_dir = os.path.dirname(os.path.abspath(__file__))
    outdir = os.path.join(script_dir, "..", "outputs", "figures")
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, "channels_schematic.png")
    fig.savefig(outpath, dpi=150, bbox_inches="tight",
                facecolor="white")
    plt.close()

    print(f"Saved: {outpath}")
    print(f"Size:  {os.path.getsize(outpath) / 1024:.0f} KB")


if __name__ == "__main__":
    main()
