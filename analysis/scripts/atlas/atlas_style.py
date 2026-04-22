"""
Shared style + renderer for the ED Visual Atlas.

Every atlas PNG imports from here so the aesthetic stays locked.

Canonical style:
- 8 x 6 inch canvas, 200 dpi  ->  1600 x 1200 px
- top 25% : equation / title band
- bottom 75% : visual analog band
- two-tone palette: charcoal + muted navy
- thin precise linework, flat fills only, no gradients
- consistent sans-serif font
"""

from __future__ import annotations

import os
import matplotlib as mpl
import matplotlib.pyplot as plt

# ---- palette ---------------------------------------------------------------
INK        = "#2a2a2a"    # charcoal, primary line and text
ACCENT     = "#3b5380"    # muted navy (matches ED-Logic-Flow)
ACCENT_SOFT = "#c6cfdd"   # pale fill derived from accent
BG         = "#ffffff"    # canvas
MUTED      = "#888888"    # secondary linework / ticks
HATCH_BG   = "#f1f1f1"    # very light gray for forbidden regions

# ---- geometry --------------------------------------------------------------
FIG_W_IN   = 8.0
FIG_H_IN   = 6.0
DPI        = 200

# Canvas is drawn in "units" (not inches): 8 wide by 6 tall.
# Top band y in [4.5, 6.0]  (25%)
# Bottom band y in [0.0, 4.5]  (75%)
TOP_BAND_Y0 = 4.5
TOP_BAND_Y1 = 6.0
BOT_BAND_Y0 = 0.0
BOT_BAND_Y1 = 4.5

# ---- linework --------------------------------------------------------------
LW_PRIMARY   = 1.6
LW_SECONDARY = 1.0
LW_EMPHASIS  = 2.4   # used sparingly (e.g., the zero line)

# ---- fonts -----------------------------------------------------------------
mpl.rcParams["font.family"] = "DejaVu Sans"
mpl.rcParams["mathtext.default"] = "regular"
mpl.rcParams["axes.unicode_minus"] = False


def new_canvas():
    """Return (fig, ax) set up to the atlas standard."""
    fig, ax = plt.subplots(figsize=(FIG_W_IN, FIG_H_IN))
    ax.set_xlim(0, FIG_W_IN)
    ax.set_ylim(0, FIG_H_IN)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor(BG)
    return fig, ax


def equation_band(ax, text, fontsize=22, ypos=None):
    """Render the equation/title centered in the top band."""
    if ypos is None:
        ypos = (TOP_BAND_Y0 + TOP_BAND_Y1) / 2 + 0.10
    ax.text(FIG_W_IN / 2, ypos, text,
            ha="center", va="center",
            fontsize=fontsize, color=INK, fontweight="regular")


def save(fig, filename):
    """Save to docs/figures/atlas/<filename>."""
    out_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))))),
        "docs", "figures", "atlas",
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, filename)
    fig.savefig(path, dpi=DPI, bbox_inches="tight",
                facecolor=BG, pad_inches=0.15)
    plt.close(fig)
    return path
