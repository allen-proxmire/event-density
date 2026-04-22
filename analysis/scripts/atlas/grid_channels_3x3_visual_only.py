"""
3×3 story-grid — visual-only.

Rows = the three ED channels (mobility, penalty, participation).
Columns = level of abstraction (channel-alone → textbook analogue →
empirical module).

Row 1 (cyan):  Mobility_alone       | PME_porous_medium | UDM_universal
Row 2 (amber): Penalty_alone        | RC_debye          | CMLag_merger
Row 3 (coral): Participation_alone  | RLC_oscillator    | FRAP_BSA

No text is baked in — the user adds row labels ("Mobility / Penalty /
Participation") and column labels ("Channel / Textbook / Data") in the
slide or webpage layer.
"""

from __future__ import annotations

import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Rectangle, FancyBboxPatch

ATLAS_DIR = r"C:\Users\allen\GitHub\Event Density\docs\figures\atlas"
OUT = os.path.join(ATLAS_DIR, "Grid_3x3_story.png")

GRID = [
    # (row-color-core, row-color-halo), [image filenames]
    (
        ("#1aa6c7", "#9fe6f3"),  # mobility row — cyan
        [
            "Mobility_alone.png",
            "PME_porous_medium.png",
            "UDM_universal.png",
        ],
    ),
    (
        ("#c97a10", "#ffd98a"),  # penalty row — amber
        [
            "Penalty_alone.png",
            "RC_debye.png",
            "CMLag_merger.png",
        ],
    ),
    (
        ("#c94419", "#ffae79"),  # participation row — coral
        [
            "Participation_alone.png",
            "RLC_oscillator.png",
            "FRAP_BSA.png",
        ],
    ),
]

# Column accent palette (just subtle, no text)
COL_COLORS = ["#5b6b80", "#5b6b80", "#ffb347"]  # last column (Data) warm


def build():
    # Figure sized for good print/slide resolution
    fig = plt.figure(figsize=(15, 13), dpi=200)

    # overall background
    fig.patch.set_facecolor("#f7fbfe")

    # ----------------------------------------------------------
    # Layout: 3×3 image grid with a thin row-color accent strip
    # on the left of each row, plus a thin column accent strip
    # at the top of each column.
    # Implement via GridSpec: (1 row accent | 3 image cols) × (1 col accent | 3 image rows)
    # Actually keep it simple: draw a single big axes on which we
    # composite everything.
    # ----------------------------------------------------------
    big_ax = fig.add_axes([0.0, 0.0, 1.0, 1.0])
    big_ax.set_xlim(0, 15)
    big_ax.set_ylim(0, 13)
    big_ax.set_aspect("equal")
    big_ax.axis("off")

    # soft header band for column accents (top), and soft gutter for rows (left)
    # Column header strip
    col_header_y0 = 12.25
    col_header_h = 0.40
    row_accent_x0 = 0.40
    row_accent_w = 0.32

    # Cell geometry
    pad = 0.15
    grid_x0 = 1.0
    grid_y_top = 12.0
    grid_w = 14.0 - grid_x0
    cell_h = (12.0 - 1.0) / 3.0
    cell_w = grid_w / 3.0 - pad

    # Column header bars (three subtly distinct tone bars)
    for i, col_col in enumerate(COL_COLORS):
        x0 = grid_x0 + i * (cell_w + pad) + 0.05
        big_ax.add_patch(FancyBboxPatch(
            (x0, col_header_y0),
            cell_w - 0.10, col_header_h,
            boxstyle="round,pad=0.02,rounding_size=0.14",
            facecolor=col_col, edgecolor="none",
            alpha=0.75, zorder=2,
        ))
        # small bright cap at the right end of each column band
        big_ax.add_patch(FancyBboxPatch(
            (x0 + cell_w - 0.50, col_header_y0 + 0.05),
            0.35, col_header_h - 0.10,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor="white", edgecolor="none",
            alpha=0.45, zorder=3,
        ))

    # Row accent strips (vertical on the left of each row)
    for row_idx, ((row_core, row_halo), _) in enumerate(GRID):
        y0 = 12.0 - (row_idx + 1) * cell_h + 0.08
        # halo
        for pad_s, a in [(0.14, 0.10), (0.08, 0.18),
                         (0.04, 0.30)]:
            big_ax.add_patch(FancyBboxPatch(
                (row_accent_x0 - pad_s, y0 - pad_s),
                row_accent_w + 2 * pad_s, cell_h - 0.16 + 2 * pad_s,
                boxstyle="round,pad=0.02,rounding_size=0.15",
                facecolor=row_halo, edgecolor="none",
                alpha=a, zorder=2,
            ))
        big_ax.add_patch(FancyBboxPatch(
            (row_accent_x0, y0),
            row_accent_w, cell_h - 0.16,
            boxstyle="round,pad=0.02,rounding_size=0.15",
            facecolor=row_core, edgecolor="none",
            alpha=0.92, zorder=3,
        ))
        # little bright tick in the middle of the strip
        big_ax.add_patch(FancyBboxPatch(
            (row_accent_x0 + 0.03,
             y0 + (cell_h - 0.16) / 2 - 0.15),
            row_accent_w - 0.06, 0.30,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor="white", edgecolor="none",
            alpha=0.45, zorder=4,
        ))

    # ----------------------------------------------------------
    # Place each image in its cell
    # ----------------------------------------------------------
    for row_idx, ((row_core, row_halo), fnames) in enumerate(GRID):
        for col_idx, fname in enumerate(fnames):
            fpath = os.path.join(ATLAS_DIR, fname)
            if not os.path.exists(fpath):
                print(f"WARNING: missing {fpath}")
                continue
            img = mpimg.imread(fpath)

            # cell bounding box
            cx0 = grid_x0 + col_idx * (cell_w + pad) + 0.05
            cy_top = 12.0 - row_idx * cell_h - 0.08
            cy0 = cy_top - cell_h + 0.16

            # soft halo around each cell
            for hp, a in [(0.14, 0.06), (0.08, 0.12)]:
                big_ax.add_patch(FancyBboxPatch(
                    (cx0 - hp, cy0 - hp),
                    cell_w - 0.10 + 2 * hp,
                    cell_h - 0.16 + 2 * hp,
                    boxstyle="round,pad=0.02,rounding_size=0.14",
                    facecolor=row_core, edgecolor="none",
                    alpha=a, zorder=4,
                ))

            # white card background under the image
            big_ax.add_patch(FancyBboxPatch(
                (cx0, cy0),
                cell_w - 0.10, cell_h - 0.16,
                boxstyle="round,pad=0.02,rounding_size=0.14",
                facecolor="white", edgecolor=row_core,
                lw=1.8, zorder=5,
            ))

            # fit image inside the card while preserving aspect
            img_h, img_w = img.shape[:2]
            img_aspect = img_w / img_h
            card_w = cell_w - 0.30
            card_h = cell_h - 0.36
            card_aspect = card_w / card_h
            if img_aspect > card_aspect:
                # wider than card -> fit width, shrink height
                draw_w = card_w
                draw_h = card_w / img_aspect
            else:
                draw_h = card_h
                draw_w = card_h * img_aspect
            draw_x = cx0 + (cell_w - 0.10) / 2 - draw_w / 2
            draw_y = cy0 + (cell_h - 0.16) / 2 - draw_h / 2

            big_ax.imshow(
                img,
                extent=[draw_x, draw_x + draw_w,
                        draw_y, draw_y + draw_h],
                aspect="auto",
                zorder=6,
            )

    # subtle caption-zone placeholder at the very bottom (a thin gold bar)
    big_ax.add_patch(FancyBboxPatch(
        (0.4, 0.25), 14.2, 0.25,
        boxstyle="round,pad=0.02,rounding_size=0.10",
        facecolor="#ffd98a", edgecolor="none",
        alpha=0.45, zorder=2,
    ))

    plt.savefig(OUT, dpi=200, bbox_inches="tight",
                facecolor="#f7fbfe", edgecolor="none")
    plt.close(fig)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    build()
