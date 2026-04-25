"""
Generate all new graphics for the ED Story video script.

Six graphics, all styled for 1080p video overlay:
  1. Turtle stack (foundations of physics)
  2. Four walls → room
  3. Two overlapping blobs (compositional rule)
  4. Four ingredients with labels
  5. Discrete grid → continuous field → PDE
  6. Seven axioms → PDE

Output: outputs/figures/video_*.png
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import (FancyBboxPatch, FancyArrowPatch,
                                 Rectangle, Circle, Polygon)
from matplotlib.lines import Line2D
import matplotlib.patheffects as pe

# ── Style constants ────────────────────────────────────────────────
BG = "#0F1117"
WHITE = "#F0F0F0"
DIM = "#6B7280"
ACCENT = "#38BDF8"
ACCENT2 = "#818CF8"  # indigo
RED = "#F87171"
GREEN = "#34D399"
ORANGE = "#FB923C"
PURPLE = "#A78BFA"

OUTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "..", "outputs", "figures")
os.makedirs(OUTDIR, exist_ok=True)


def save(fig, name):
    path = os.path.join(OUTDIR, name)
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor=BG,
                edgecolor="none")
    plt.close(fig)
    print(f"  Saved: {name} ({os.path.getsize(path)//1024} KB)")


# ══════════════════════════════════════════════════════════════════
#  1. TURTLE STACK
# ══════════════════════════════════════════════════════════════════

def make_turtle_stack():
    fig, ax = plt.subplots(figsize=(8, 9))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 9)
    ax.axis("off")

    layers = [
        ("Particles", RED),
        ("Atoms", ORANGE),
        ("Quantum Fields", ACCENT),
        ("Hilbert Space", ACCENT2),
        ("Spacetime", PURPLE),
    ]

    box_w = 5.0
    box_h = 0.9
    gap = 0.25
    x0 = (8 - box_w) / 2
    y_start = 2.5

    for i, (label, color) in enumerate(layers):
        y = y_start + i * (box_h + gap)
        box = FancyBboxPatch(
            (x0, y), box_w, box_h,
            boxstyle="round,pad=0.08,rounding_size=0.15",
            facecolor=color, edgecolor="none", alpha=0.85, zorder=2,
        )
        ax.add_patch(box)
        ax.text(x0 + box_w / 2, y + box_h / 2, label,
                ha="center", va="center", fontsize=18, fontweight="bold",
                color="white", zorder=3)

        # Arrow between layers
        if i > 0:
            ax.annotate(
                "", xy=(4, y + 0.02), xytext=(4, y - gap + 0.02),
                arrowprops=dict(arrowstyle="-|>", color=DIM,
                                linewidth=1.5, mutation_scale=15),
                zorder=1,
            )

    # Question mark at bottom
    y_q = y_start - gap - 0.5
    ax.text(4, y_q, "?", ha="center", va="center", fontsize=60,
            color=DIM, fontweight="bold", fontstyle="italic",
            fontfamily="serif")

    # Arrow from bottom layer to question mark
    ax.annotate(
        "", xy=(4, y_q + 0.45), xytext=(4, y_start - 0.05),
        arrowprops=dict(arrowstyle="-|>", color=DIM,
                        linewidth=1.5, mutation_scale=15),
    )

    # Title
    ax.text(4, 8.3, "What holds it up?",
            ha="center", va="center", fontsize=22, color=WHITE,
            fontweight="bold")

    # Subtitle
    ax.text(4, 7.7, "Every theory picks a turtle and stands on it.",
            ha="center", va="center", fontsize=13, color=DIM,
            fontstyle="italic")

    save(fig, "video_01_turtle_stack.png")


# ══════════════════════════════════════════════════════════════════
#  2. FOUR WALLS → ROOM
# ══════════════════════════════════════════════════════════════════

def make_walls_to_room():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.patch.set_facecolor(BG)

    titles = ["Four walls", "Configured", "A room"]

    for ax in axes:
        ax.set_facecolor(BG)
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.set_aspect("equal")
        ax.axis("off")

    # Panel 1: four disconnected walls
    ax = axes[0]
    lines = [
        ([-1.2, -1.2], [-0.8, 0.8]),   # left, slightly off
        ([1.3, 1.3], [-0.9, 0.7]),      # right, slightly off
        ([-0.7, 0.9], [1.1, 1.1]),      # top, slightly off
        ([-0.8, 0.7], [-1.2, -1.2]),    # bottom, slightly off
    ]
    colors = [RED, ACCENT, GREEN, ORANGE]
    for (xs, ys), col in zip(lines, colors):
        ax.plot(xs, ys, "-", color=col, linewidth=4, solid_capstyle="round")
    ax.text(0, -1.7, titles[0], ha="center", va="center",
            fontsize=16, color=DIM, fontstyle="italic")

    # Panel 2: walls connecting
    ax = axes[1]
    corners = [(-1, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]
    for i in range(4):
        x0c, y0c = corners[i]
        x1c, y1c = corners[i + 1]
        ax.plot([x0c, x1c], [y0c, y1c], "-", color=colors[i],
                linewidth=4, solid_capstyle="round")
    ax.text(0, -1.7, titles[1], ha="center", va="center",
            fontsize=16, color=DIM, fontstyle="italic")

    # Arrow between panels
    fig.text(0.365, 0.5, "\u2192", fontsize=36, color=DIM,
             ha="center", va="center")
    fig.text(0.66, 0.5, "\u2192", fontsize=36, color=DIM,
             ha="center", va="center")

    # Panel 3: a room (filled interior)
    ax = axes[2]
    room = Polygon([(-1, -1), (1, -1), (1, 1), (-1, 1)],
                   closed=True, facecolor=ACCENT, alpha=0.15,
                   edgecolor="none", zorder=1)
    ax.add_patch(room)
    for i in range(4):
        x0c, y0c = corners[i]
        x1c, y1c = corners[i + 1]
        ax.plot([x0c, x1c], [y0c, y1c], "-", color=colors[i],
                linewidth=4, solid_capstyle="round", zorder=2)
    ax.text(0, 0, "inside", ha="center", va="center",
            fontsize=14, color=ACCENT, fontstyle="italic", alpha=0.8)
    ax.text(0, -1.7, titles[2], ha="center", va="center",
            fontsize=16, color=WHITE, fontweight="bold")

    plt.subplots_adjust(wspace=0.15)
    save(fig, "video_02_walls_to_room.png")


# ══════════════════════════════════════════════════════════════════
#  3. OVERLAPPING BLOBS (COMPOSITIONAL RULE)
# ══════════════════════════════════════════════════════════════════

def make_overlapping_blobs():
    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-0.3, 1.8)
    ax.axis("off")

    x = np.linspace(-4, 4, 800)

    # Two Gaussians
    g1 = 1.0 * np.exp(-((x + 0.8) / 0.9) ** 2)
    g2 = 0.85 * np.exp(-((x - 0.8) / 1.0) ** 2)
    combined = g1 + g2

    # Plot individual blobs
    ax.fill_between(x, g1, 0, color=ACCENT, alpha=0.20, zorder=1)
    ax.plot(x, g1, "-", color=ACCENT, linewidth=2, alpha=0.6,
            label="Region A", zorder=2)

    ax.fill_between(x, g2, 0, color=PURPLE, alpha=0.20, zorder=1)
    ax.plot(x, g2, "-", color=PURPLE, linewidth=2, alpha=0.6,
            label="Region B", zorder=2)

    # Highlight overlap region
    overlap = np.minimum(g1, g2)
    ax.fill_between(x, overlap, 0, color=WHITE, alpha=0.15, zorder=3)

    # Combined profile
    ax.plot(x, combined, "-", color=WHITE, linewidth=2.5, zorder=4,
            label="Combined")

    # Boundary annotation
    # Find where g1 and g2 cross
    diff = g1 - g2
    cross_idx = np.where(np.diff(np.sign(diff)))[0]
    if len(cross_idx) > 0:
        cx = x[cross_idx[0]]
        cy = g1[cross_idx[0]]
        ax.plot(cx, cy, "o", color=ORANGE, markersize=10, zorder=5)
        ax.annotate("boundary", xy=(cx, cy),
                    xytext=(cx + 0.8, cy + 0.35),
                    fontsize=12, color=ORANGE, fontstyle="italic",
                    arrowprops=dict(arrowstyle="->", color=ORANGE,
                                   linewidth=1.2))

    # Overlap label
    ax.text(0, 0.25, "overlap", ha="center", va="center",
            fontsize=11, color=WHITE, alpha=0.6, fontstyle="italic")

    ax.text(0, 1.65, "How do two regions of activity combine?",
            ha="center", va="center", fontsize=18, color=WHITE,
            fontweight="bold")

    ax.legend(fontsize=10, loc="upper right",
              facecolor=BG, edgecolor=DIM, labelcolor=WHITE,
              framealpha=0.8)

    save(fig, "video_03_overlapping_blobs.png")


# ══════════════════════════════════════════════════════════════════
#  4. FOUR INGREDIENTS
# ══════════════════════════════════════════════════════════════════

def make_four_ingredients():
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis("off")

    items = [
        {
            "num": "1", "name": "Density",
            "symbol": r"$\rho(x, t)$",
            "desc": "How much is happening\nat each point",
            "color": ACCENT,
        },
        {
            "num": "2", "name": "Mobility",
            "symbol": r"$M(\rho)$",
            "desc": "How easily it spreads\n— shuts off at capacity",
            "color": GREEN,
        },
        {
            "num": "3", "name": "Penalty",
            "symbol": r"$P(\rho)$",
            "desc": "Pull toward a natural\nresting state",
            "color": RED,
        },
        {
            "num": "4", "name": "Participation",
            "symbol": r"$v(t)$",
            "desc": "A global pulse feeding\nback into every point",
            "color": ORANGE,
        },
    ]

    x_positions = [1.5, 4.5, 7.5, 10.5]
    y_center = 3.0

    for item, xc in zip(items, x_positions):
        col = item["color"]

        # Number circle
        circle = Circle((xc, y_center + 1.2), 0.35,
                        facecolor=col, edgecolor="none", alpha=0.9,
                        zorder=2)
        ax.add_patch(circle)
        ax.text(xc, y_center + 1.2, item["num"],
                ha="center", va="center", fontsize=18,
                fontweight="bold", color="white", zorder=3)

        # Name
        ax.text(xc, y_center + 0.5, item["name"],
                ha="center", va="center", fontsize=18,
                fontweight="bold", color=col)

        # Symbol
        ax.text(xc, y_center - 0.15, item["symbol"],
                ha="center", va="center", fontsize=20, color=WHITE)

        # Description
        ax.text(xc, y_center - 1.05, item["desc"],
                ha="center", va="center", fontsize=11,
                color=DIM, linespacing=1.4)

    # Title
    ax.text(6, 5.5, "Four Ingredients of the Compositional Rule",
            ha="center", va="center", fontsize=20, color=WHITE,
            fontweight="bold")

    save(fig, "video_04_four_ingredients.png")


# ══════════════════════════════════════════════════════════════════
#  5. DISCRETE GRID → CONTINUOUS FIELD → PDE
# ══════════════════════════════════════════════════════════════════

def make_grid_to_pde():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.patch.set_facecolor(BG)

    # Panel 1: discrete grid of cells with varying intensity
    ax = axes[0]
    ax.set_facecolor(BG)
    ax.set_xlim(-0.5, 7.5)
    ax.set_ylim(-0.5, 7.5)
    ax.axis("off")

    np.random.seed(42)
    grid = np.random.rand(8, 8) * 0.7 + 0.15
    # Add a central peak
    for i in range(8):
        for j in range(8):
            r = np.sqrt((i - 3.5) ** 2 + (j - 3.5) ** 2)
            grid[i, j] = max(grid[i, j], np.exp(-r ** 2 / 4))

    for i in range(8):
        for j in range(8):
            rect = Rectangle((j - 0.45, i - 0.45), 0.9, 0.9,
                             facecolor=ACCENT, alpha=grid[i, j] * 0.8,
                             edgecolor=DIM, linewidth=0.5, zorder=1)
            ax.add_patch(rect)

    ax.text(3.5, -1.0, "Discrete composition",
            ha="center", fontsize=13, color=DIM, fontstyle="italic")

    # Panel 2: smooth continuous field
    ax = axes[1]
    ax.set_facecolor(BG)
    ax.axis("off")

    xx, yy = np.meshgrid(np.linspace(0, 1, 200), np.linspace(0, 1, 200))
    field = np.exp(-((xx - 0.45) ** 2 + (yy - 0.45) ** 2) / 0.06)
    field += 0.4 * np.exp(-((xx - 0.7) ** 2 + (yy - 0.65) ** 2) / 0.04)
    ax.imshow(field, cmap="cool", alpha=0.85, extent=[0, 1, 0, 1],
              origin="lower")
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.15, 1.05)
    ax.text(0.5, -0.10, "Continuum limit",
            ha="center", fontsize=13, color=DIM, fontstyle="italic",
            transform=ax.transAxes)

    # Panel 3: the PDE
    ax = axes[2]
    ax.set_facecolor(BG)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    ax.text(5, 6.5,
            r"$\partial_t \rho = D\,[\,\nabla\!\cdot\!(M(\rho)\nabla\rho)$",
            ha="center", va="center", fontsize=20, color=WHITE)
    ax.text(5, 5.2,
            r"$-\; P(\rho)\,] + H\,v$",
            ha="center", va="center", fontsize=20, color=WHITE)
    ax.text(5, 3.5,
            r"$\dot v = (\bar F - \zeta v)/\tau$",
            ha="center", va="center", fontsize=18, color=ACCENT)

    ax.text(5, 1.5, "The canonical PDE",
            ha="center", fontsize=13, color=DIM, fontstyle="italic")

    # Arrows between panels
    fig.text(0.355, 0.5, "\u2192", fontsize=40, color=DIM,
             ha="center", va="center")
    fig.text(0.655, 0.5, "\u2192", fontsize=40, color=DIM,
             ha="center", va="center")

    plt.subplots_adjust(wspace=0.12)
    save(fig, "video_05_grid_to_pde.png")


# ══════════════════════════════════════════════════════════════════
#  6. SEVEN AXIOMS → UNIQUE PDE
# ══════════════════════════════════════════════════════════════════

def make_seven_axioms():
    fig, ax = plt.subplots(figsize=(12, 7))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")

    axioms = [
        ("P1", "Local"),
        ("P2", "Isotropic"),
        ("P3", "Gradient-driven"),
        ("P4", "Dissipative"),
        ("P5", "Scalar"),
        ("P6", "Minimal coupling"),
        ("P7", "Dimension-free"),
    ]

    colors = [RED, ORANGE, ACCENT, GREEN, PURPLE, ACCENT2, "#F472B6"]

    # Arrange in an arc above the PDE
    n = len(axioms)
    for i, ((label, name), col) in enumerate(zip(axioms, colors)):
        # Arc positions
        angle = np.pi * 0.15 + (np.pi * 0.7) * i / (n - 1)
        cx = 6 + 4.2 * np.cos(angle)
        cy = 2.8 + 3.0 * np.sin(angle)

        # Pill-shaped badge
        badge = FancyBboxPatch(
            (cx - 0.9, cy - 0.25), 1.8, 0.5,
            boxstyle="round,pad=0.05,rounding_size=0.2",
            facecolor=col, edgecolor="none", alpha=0.85, zorder=2,
        )
        ax.add_patch(badge)
        ax.text(cx, cy, f"{label}  {name}",
                ha="center", va="center", fontsize=10,
                fontweight="bold", color="white", zorder=3)

        # Line from badge down to PDE area
        ax.plot([cx, 6], [cy - 0.25, 1.8], "-", color=col,
                linewidth=0.8, alpha=0.3, zorder=1)

    # The PDE at the convergence point
    pde_box = FancyBboxPatch(
        (2.5, 0.6), 7, 1.3,
        boxstyle="round,pad=0.1,rounding_size=0.2",
        facecolor="#1E293B", edgecolor=ACCENT, linewidth=1.5,
        zorder=4,
    )
    ax.add_patch(pde_box)

    ax.text(6, 1.55,
            r"$\partial_t \rho = D\,[\nabla\!\cdot\!(M(\rho)\nabla\rho) - P(\rho)] + Hv$",
            ha="center", va="center", fontsize=17, color=WHITE, zorder=5)

    ax.text(6, 0.95, "unique",
            ha="center", va="center", fontsize=14, color=ACCENT,
            fontweight="bold", fontstyle="italic", zorder=5)

    save(fig, "video_06_seven_axioms.png")


# ══════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("Generating video graphics...")
    make_turtle_stack()
    make_walls_to_room()
    make_overlapping_blobs()
    make_four_ingredients()
    make_grid_to_pde()
    make_seven_axioms()
    print("Done.")
