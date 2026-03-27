"""
generate_certificate_figure.py
===============================
Renders the ED Architecture Certificate as a publication-ready figure.

Implements the full design specification from certificate_design_spec.md:
  - Four zones: Header, Verdict Banner, Metrics Table, Footer
  - Three verdict variants: PASS / PARTIAL / FAIL
  - Five diagnostic rows with geometric icons and verdict chips
  - Logarithmic-spiral watermark at 3% opacity
  - Dual export: PNG (300 DPI) + PDF (vector)

Usage:
    python generate_certificate_figure.py
    python generate_certificate_figure.py --verdict PASS
    python generate_certificate_figure.py --verdict PARTIAL
    python generate_certificate_figure.py --verdict FAIL

Outputs:
    output/atlas/ED_Architecture_Certificate.png
    output/atlas/ED_Architecture_Certificate.pdf

Requires: matplotlib, numpy.
"""

import os
import sys
import argparse
import datetime
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Arc, FancyArrowPatch
from matplotlib.lines import Line2D
from matplotlib.path import Path
import matplotlib.patheffects as pe

# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════

# --- Canvas ---
FIG_WIDTH = 6.0        # inches
FIG_HEIGHT = 8.0       # inches
DPI = 300
PAGE_BG = "#FAFBFC"
CARD_BG = "#FFFFFF"

# --- Zone positions [left, bottom, width, height] in figure fraction ---
ZONE_HEADER  = [0.08, 0.77, 0.84, 0.18]
ZONE_VERDICT = [0.08, 0.63, 0.84, 0.12]
ZONE_METRICS = [0.08, 0.19, 0.84, 0.42]
ZONE_FOOTER  = [0.08, 0.05, 0.84, 0.12]

# --- Neutral palette ---
CLR_TITLE    = "#1A1A2E"
CLR_BODY     = "#2B2D42"
CLR_MUTED    = "#8D99AE"
CLR_BORDER   = "#D6D9E0"
CLR_TABLE_HD = "#F0F1F5"

# --- Verdict palettes ---
PALETTES = {
    "PASS": {
        "bg":      "#E8F5E9",
        "border":  "#2E7D32",
        "text":    "#1B5E20",
        "accent":  "#43A047",
        "light":   "#A5D6A7",
        "dash":    "solid",
        "border_lw": 2.5,
        "subtext": "All diagnostics satisfactory",
        "mark":    "filled_circle",
    },
    "PARTIAL": {
        "bg":      "#FFF8E1",
        "border":  "#F9A825",
        "text":    "#E65100",
        "accent":  "#FFB300",
        "light":   "#FFE082",
        "dash":    "solid",
        "border_lw": 2.0,
        "subtext": "Some diagnostics weakly satisfactory",
        "mark":    "half_circle",
    },
    "FAIL": {
        "bg":      "#FFEBEE",
        "border":  "#C62828",
        "text":    "#B71C1C",
        "accent":  "#E53935",
        "light":   "#EF9A9A",
        "dash":    (0, (6, 3)),
        "border_lw": 2.0,
        "subtext": "Architecture inconsistency detected",
        "mark":    "open_circle",
    },
}

# --- Chip palettes ---
CHIP_POSITIVE = {"bg": None, "text": None, "border": None}  # set per-verdict
CHIP_MARGINAL = {"bg": "#FFF3E0", "text": "#E65100", "border": "#FFB300"}
CHIP_NEGATIVE = {"bg": "#FFEBEE", "text": "#C62828", "border": "#E53935"}

# --- Fonts ---
FONT_HEADING = "Inter"
FONT_MONO    = "JetBrains Mono"
FONT_HEADING_FB = "DejaVu Sans"
FONT_MONO_FB    = "DejaVu Sans Mono"

# --- Sample metric values (representative PASS data) ---
SAMPLE_METRICS = {
    "PASS": {
        "U": 0.9412, "U_verdict": "UNIVERSAL",
        "C": 0.8731, "C_verdict": "CONSISTENT",
        "n_pos": 0, "D_KY": 0.00, "D_eff": 1.2, "stab_verdict": "STABLE",
        "radius": 0.071, "emb_verdict": "COLLAPSED",
        "eps_cv": 0.032, "rec_verdict": "ROBUST",
        "pass_frac": "5/5",
    },
    "PARTIAL": {
        "U": 0.7823, "U_verdict": "WEAKLY",
        "C": 0.6104, "C_verdict": "PARTIAL",
        "n_pos": 0, "D_KY": 0.12, "D_eff": 2.8, "stab_verdict": "STABLE",
        "radius": 0.241, "emb_verdict": "DIFFUSE",
        "eps_cv": 0.089, "rec_verdict": "ROBUST",
        "pass_frac": "3/5",
    },
    "FAIL": {
        "U": 0.4912, "U_verdict": "NOT",
        "C": 0.3841, "C_verdict": "INCONSISTENT",
        "n_pos": 2, "D_KY": 1.84, "D_eff": 5.1, "stab_verdict": "UNSTABLE",
        "radius": 0.612, "emb_verdict": "SCATTERED",
        "eps_cv": 0.241, "rec_verdict": "FRAGILE",
        "pass_frac": "1/5",
    },
}


# ═══════════════════════════════════════════════════════════════════════════
# FONT RESOLUTION
# ═══════════════════════════════════════════════════════════════════════════

def _resolve_fonts():
    """Check which fonts are available and return resolved names."""
    from matplotlib.font_manager import fontManager
    available = {f.name for f in fontManager.ttflist}

    heading = FONT_HEADING if FONT_HEADING in available else FONT_HEADING_FB
    mono = FONT_MONO if FONT_MONO in available else FONT_MONO_FB
    return heading, mono


HEADING_FONT, MONO_FONT = _resolve_fonts()


# ═══════════════════════════════════════════════════════════════════════════
# DRAWING HELPERS
# ═══════════════════════════════════════════════════════════════════════════

def _make_zone_ax(fig, rect, facecolor=CARD_BG):
    """Create an axes for a zone with no ticks or spines."""
    ax = fig.add_axes(rect)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_facecolor(facecolor)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    return ax


def _draw_box(ax, x, y, w, h, facecolor="none", edgecolor=CLR_BORDER,
              linewidth=1.0, linestyle="solid", radius=0.0, zorder=1):
    """Draw a box (optionally rounded) on the given axes."""
    if radius > 0:
        box = FancyBboxPatch(
            (x, y), w, h,
            boxstyle=f"round,pad=0,rounding_size={radius}",
            facecolor=facecolor, edgecolor=edgecolor,
            linewidth=linewidth, linestyle=linestyle,
            zorder=zorder, clip_on=False,
        )
    else:
        box = mpatches.Rectangle(
            (x, y), w, h,
            facecolor=facecolor, edgecolor=edgecolor,
            linewidth=linewidth, linestyle=linestyle,
            zorder=zorder, clip_on=False,
        )
    ax.add_patch(box)
    return box


def _draw_chip(ax, x, y, text, bg, text_clr, border_clr):
    """Draw a small verdict chip (rounded rectangle with text)."""
    chip_w = 0.18
    chip_h = 0.045
    chip = FancyBboxPatch(
        (x - chip_w / 2, y - chip_h / 2), chip_w, chip_h,
        boxstyle="round,pad=0.003,rounding_size=0.012",
        facecolor=bg, edgecolor=border_clr,
        linewidth=0.8, zorder=5, clip_on=False,
    )
    ax.add_patch(chip)
    ax.text(
        x, y, text,
        fontfamily=HEADING_FONT, fontsize=5.5, fontweight="bold",
        color=text_clr, ha="center", va="center", zorder=6,
    )


def _chip_colors(verdict_class, pal):
    """Return (bg, text, border) for a chip given its class."""
    if verdict_class == "positive":
        return pal["light"], pal["accent"], pal["accent"]
    elif verdict_class == "marginal":
        return CHIP_MARGINAL["bg"], CHIP_MARGINAL["text"], CHIP_MARGINAL["border"]
    else:
        return CHIP_NEGATIVE["bg"], CHIP_NEGATIVE["text"], CHIP_NEGATIVE["border"]


def _classify_chip(verdict_text):
    """Map a verdict string to positive/marginal/negative."""
    pos = {"UNIVERSAL", "CONSISTENT", "STABLE", "COLLAPSED", "ROBUST"}
    marg = {"WEAKLY", "PARTIAL", "MARGINAL", "DIFFUSE", "SENSITIVE"}
    if verdict_text in pos:
        return "positive"
    elif verdict_text in marg:
        return "marginal"
    return "negative"


# ═══════════════════════════════════════════════════════════════════════════
# ICON DRAWING
# ═══════════════════════════════════════════════════════════════════════════

def _draw_icon_universality(ax, cx, cy, r, color):
    """Concentric circles: three rings sharing a common centre."""
    for radius in [r * 0.33, r * 0.66, r]:
        circle = Circle(
            (cx, cy), radius, fill=False,
            edgecolor=color, linewidth=1.2,
            capstyle="round", joinstyle="round", zorder=4,
        )
        ax.add_patch(circle)


def _draw_icon_consistency(ax, cx, cy, r, color):
    """Interlocking rings: two overlapping circles."""
    offset = r * 0.45
    for dx in [-offset, offset]:
        circle = Circle(
            (cx + dx, cy), r * 0.7, fill=False,
            edgecolor=color, linewidth=1.2,
            capstyle="round", joinstyle="round", zorder=4,
        )
        ax.add_patch(circle)


def _draw_icon_stability(ax, cx, cy, r, color):
    """Downward chevron: two lines meeting at a point below."""
    hw = r * 0.7
    hh = r * 0.8
    xs = [cx - hw, cx, cx + hw]
    ys = [cy + hh * 0.5, cy - hh * 0.5, cy + hh * 0.5]
    ax.plot(xs, ys, color=color, linewidth=1.2, solid_capstyle="round",
            solid_joinstyle="round", zorder=4)


def _draw_icon_embedding(ax, cx, cy, r, color):
    """Cluster dot: central filled dot + six outer dots at 50% opacity."""
    # Central dot
    ax.add_patch(Circle((cx, cy), r * 0.25, facecolor=color,
                        edgecolor="none", zorder=4))
    # Outer dots
    for angle in np.linspace(0, 2 * np.pi, 6, endpoint=False):
        ox = cx + r * 0.7 * np.cos(angle)
        oy = cy + r * 0.7 * np.sin(angle)
        ax.add_patch(Circle((ox, oy), r * 0.12, facecolor=color,
                            edgecolor="none", alpha=0.5, zorder=4))


def _draw_icon_recovery(ax, cx, cy, r, color):
    """Return arrow: 270° arc with arrowhead."""
    # Draw arc as a series of points
    angles = np.linspace(np.pi / 2, -np.pi, 60)
    xs = cx + r * 0.7 * np.cos(angles)
    ys = cy + r * 0.7 * np.sin(angles)
    ax.plot(xs, ys, color=color, linewidth=1.2, solid_capstyle="round",
            zorder=4)
    # Arrowhead at the end (pointing up-right toward 12 o'clock)
    end_x, end_y = xs[-1], ys[-1]
    arr_len = r * 0.3
    ax.annotate(
        "", xy=(end_x + arr_len * 0.3, end_y + arr_len),
        xytext=(end_x, end_y),
        arrowprops=dict(arrowstyle="-|>", color=color, lw=1.2),
        zorder=4,
    )


ICON_FUNCTIONS = [
    _draw_icon_universality,
    _draw_icon_consistency,
    _draw_icon_stability,
    _draw_icon_embedding,
    _draw_icon_recovery,
]


# ═══════════════════════════════════════════════════════════════════════════
# ZONE DRAWING FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def draw_header(fig):
    """Zone A: Title block with certificate name and version."""
    ax = _make_zone_ax(fig, ZONE_HEADER, facecolor=CARD_BG)

    # Outer border
    _draw_box(ax, 0, 0, 1, 1, edgecolor=CLR_BORDER, linewidth=1.5)

    # Title
    ax.text(
        0.5, 0.72, "ED  ARCHITECTURE",
        fontfamily=HEADING_FONT, fontsize=18, fontweight="bold",
        color=CLR_TITLE, ha="center", va="center",
    )

    # Subtitle
    ax.text(
        0.5, 0.45, "CONSISTENCY  CERTIFICATE",
        fontfamily=HEADING_FONT, fontsize=11, fontweight="normal",
        color=CLR_BODY, ha="center", va="center",
    )

    # Version
    ax.text(
        0.5, 0.18, "ED-SIM-01  ·  v1.0.0",
        fontfamily=MONO_FONT, fontsize=7, fontweight="normal",
        color=CLR_MUTED, ha="center", va="center",
    )

    # Thin rule below subtitle
    ax.plot([0.2, 0.8], [0.32, 0.32], color=CLR_BORDER, linewidth=0.6,
            zorder=2)

    return ax


def draw_verdict(fig, verdict: str):
    """Zone B: Verdict banner with symbolic mark and subtext."""
    pal = PALETTES[verdict]
    ax = _make_zone_ax(fig, ZONE_VERDICT, facecolor=pal["bg"])

    # Border
    _draw_box(ax, 0, 0, 1, 1,
              facecolor=pal["bg"], edgecolor=pal["border"],
              linewidth=pal["border_lw"], linestyle=pal["dash"],
              radius=0.03)

    # Symbolic mark
    mark_x = 0.38
    mark_y = 0.58
    mark_r = 0.035

    if pal["mark"] == "filled_circle":
        ax.add_patch(Circle((mark_x, mark_y), mark_r,
                            facecolor=pal["border"], edgecolor="none",
                            zorder=3))
    elif pal["mark"] == "half_circle":
        # Left half filled
        theta1, theta2 = 90, 270
        wedge = mpatches.Wedge((mark_x, mark_y), mark_r, theta1, theta2,
                               facecolor=pal["border"], edgecolor=pal["border"],
                               linewidth=1.0, zorder=3)
        ax.add_patch(wedge)
        ax.add_patch(Circle((mark_x, mark_y), mark_r,
                            facecolor="none", edgecolor=pal["border"],
                            linewidth=1.0, zorder=3))
    elif pal["mark"] == "open_circle":
        ax.add_patch(Circle((mark_x, mark_y), mark_r,
                            facecolor="none", edgecolor=pal["border"],
                            linewidth=1.2, zorder=3))

    # Verdict text
    ax.text(
        0.53, 0.58, verdict,
        fontfamily=HEADING_FONT, fontsize=24, fontweight="bold",
        color=pal["text"], ha="center", va="center",
        zorder=4,
    )

    # Subtext
    ax.text(
        0.5, 0.22, pal["subtext"],
        fontfamily=HEADING_FONT, fontsize=7.5, fontweight="normal",
        color=pal["accent"], ha="center", va="center",
    )

    return ax


def draw_metrics(fig, verdict: str):
    """Zone C: Five-row metrics table with icons, labels, and verdict chips."""
    pal = PALETTES[verdict]
    m = SAMPLE_METRICS[verdict]
    ax = _make_zone_ax(fig, ZONE_METRICS, facecolor=CARD_BG)

    # Outer border
    _draw_box(ax, 0, 0, 1, 1, edgecolor=CLR_BORDER, linewidth=1.0)

    # Column positions (in axes fraction)
    col_icon = 0.06       # centre of icon column
    col_label = 0.14      # left edge of label column
    col_value = 0.88      # right edge of value column
    col_chip = 0.82       # centre of chip

    # Row definitions: (y_centre, height, label, sublabel, value_str,
    #                    verdict_str, icon_func, has_submetrics)
    row_h = 0.155
    sub_h = 0.06
    gap = 0.015

    # Compute row positions from top
    rows = []
    y_cursor = 0.93

    # Row 1: Universality
    y_cursor -= row_h / 2
    rows.append({
        "y": y_cursor, "h": row_h,
        "label": "Universality",
        "sublabel": "Parameter-independence of invariant vectors",
        "value": f"U = {m['U']:.4f}",
        "verdict": m["U_verdict"],
        "icon": 0, "subs": [],
    })
    y_cursor -= row_h / 2 + gap

    # Row 2: Cross-Consistency
    y_cursor -= row_h / 2
    rows.append({
        "y": y_cursor, "h": row_h,
        "label": "Cross-Consistency",
        "sublabel": "Agreement between invariant families",
        "value": f"C = {m['C']:.4f}",
        "verdict": m["C_verdict"],
        "icon": 1, "subs": [],
    })
    y_cursor -= row_h / 2 + gap

    # Row 3: Stability (with sub-metrics)
    stab_total_h = row_h + 3 * sub_h
    y_cursor -= row_h / 2
    rows.append({
        "y": y_cursor, "h": row_h,
        "label": "Stability",
        "sublabel": "",
        "value": "",
        "verdict": m["stab_verdict"],
        "icon": 2,
        "subs": [
            (f"Positive Lyapunov exponents", f"n₊ = {m['n_pos']}"),
            (f"Kaplan–Yorke dimension", f"D_KY = {m['D_KY']:.2f}"),
            (f"Effective dimension (PCA)", f"D_eff = {m['D_eff']:.1f}"),
        ],
    })
    y_cursor -= row_h / 2 + 3 * sub_h + gap

    # Row 4: Embedding Collapse
    y_cursor -= row_h / 2
    rows.append({
        "y": y_cursor, "h": row_h,
        "label": "Embedding Collapse",
        "sublabel": "Invariant-space cluster tightness",
        "value": f"r = {m['radius']:.3f}",
        "verdict": m["emb_verdict"],
        "icon": 3, "subs": [],
    })
    y_cursor -= row_h / 2 + gap

    # Row 5: Perturbation Recovery
    y_cursor -= row_h / 2
    rows.append({
        "y": y_cursor, "h": row_h,
        "label": "Perturbation Recovery",
        "sublabel": "ε-independence of recovery rates",
        "value": f"CV = {m['eps_cv']:.3f}",
        "verdict": m["rec_verdict"],
        "icon": 4, "subs": [],
    })
    y_cursor -= row_h / 2

    # Draw rows
    for i, row in enumerate(rows):
        y = row["y"]

        # Row separator (except first)
        if i > 0:
            sep_y = y + row["h"] / 2 + gap / 2
            ax.plot([0.03, 0.97], [sep_y, sep_y],
                    color=CLR_BORDER, linewidth=0.5, zorder=2)

        # Icon
        icon_r = 0.028
        ICON_FUNCTIONS[row["icon"]](ax, col_icon, y, icon_r, pal["accent"])

        # Label
        ax.text(
            col_label, y + 0.01, row["label"],
            fontfamily=HEADING_FONT, fontsize=9, fontweight="semibold",
            color=CLR_BODY, ha="left", va="center", zorder=3,
        )

        # Sublabel
        if row["sublabel"]:
            ax.text(
                col_label, y - 0.04, row["sublabel"],
                fontfamily=HEADING_FONT, fontsize=6, fontweight="normal",
                color=CLR_MUTED, ha="left", va="center", zorder=3,
            )

        # Value
        if row["value"]:
            ax.text(
                col_value, y + 0.01, row["value"],
                fontfamily=MONO_FONT, fontsize=9, fontweight="medium",
                color=CLR_BODY, ha="right", va="center", zorder=3,
            )

        # Verdict chip
        cls = _classify_chip(row["verdict"])
        bg, txt, bdr = _chip_colors(cls, pal)
        _draw_chip(ax, col_chip, y - 0.05, row["verdict"], bg, txt, bdr)

        # Sub-metrics
        for j, (sub_label, sub_value) in enumerate(row.get("subs", [])):
            sub_y = y - 0.06 - j * sub_h
            ax.text(
                col_label + 0.04, sub_y, sub_label,
                fontfamily=HEADING_FONT, fontsize=6.5, fontweight="normal",
                color=CLR_MUTED, ha="left", va="center", zorder=3,
            )
            ax.text(
                col_value, sub_y, sub_value,
                fontfamily=MONO_FONT, fontsize=7, fontweight="normal",
                color=CLR_BODY, ha="right", va="center", zorder=3,
            )

    return ax


def draw_footer(fig, verdict: str):
    """Zone D: Statement, timestamp, version, and run count."""
    m = SAMPLE_METRICS[verdict]
    ax = _make_zone_ax(fig, ZONE_FOOTER, facecolor="none")

    # Top rule
    ax.plot([0, 1], [0.95, 0.95], color=CLR_BORDER, linewidth=0.6, zorder=2)

    # Statement
    ax.text(
        0.5, 0.72,
        "All invariants were computed from reproducible simulations",
        fontfamily=HEADING_FONT, fontsize=6.5, fontweight="normal",
        color=CLR_MUTED, ha="center", va="center",
    )
    ax.text(
        0.5, 0.56,
        "under the ED-SIM v1 pipeline. This certificate summarises the",
        fontfamily=HEADING_FONT, fontsize=6.5, fontweight="normal",
        color=CLR_MUTED, ha="center", va="center",
    )
    ax.text(
        0.5, 0.40,
        "structural consistency of the ED attractor across all tested regimes.",
        fontfamily=HEADING_FONT, fontsize=6.5, fontweight="normal",
        color=CLR_MUTED, ha="center", va="center",
    )

    # Rule
    ax.plot([0.3, 0.7], [0.28, 0.28], color=CLR_BORDER, linewidth=0.4,
            zorder=2)

    # Timestamp and version
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ax.text(
        0.0, 0.10, "Generated automatically by ED-SIM-01",
        fontfamily=HEADING_FONT, fontsize=6, fontweight="normal",
        color=CLR_MUTED, ha="left", va="center",
    )
    ax.text(
        1.0, 0.10, timestamp,
        fontfamily=MONO_FONT, fontsize=6, fontweight="normal",
        color=CLR_MUTED, ha="right", va="center",
    )

    return ax


def draw_watermark(fig):
    """Background logarithmic spiral at 3% opacity, centred on canvas."""
    ax = fig.add_axes([0, 0, 1, 1], zorder=-1)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_facecolor("none")
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Logarithmic spiral: r = a * exp(b * theta)
    # 3 full turns = 6*pi radians
    n_points = 500
    theta = np.linspace(0, 6 * np.pi, n_points)
    a = 0.005
    b = 0.08
    r = a * np.exp(b * theta)

    # Convert to Cartesian, centred at (0.5, 0.5)
    # Scale so outermost point reaches ~0.4 (80% of half-width)
    r_max = r[-1]
    scale = 0.4 / r_max
    x = 0.5 + scale * r * np.cos(theta)
    y = 0.5 + scale * r * np.sin(theta)

    ax.plot(x, y, color=CLR_BODY, linewidth=0.4, alpha=0.03, zorder=-1)

    return ax


# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

def generate_certificate(verdict: str = "PASS", output_dir: str = None):
    """Generate the complete ED Architecture Certificate figure.

    Parameters
    ----------
    verdict : str
        One of "PASS", "PARTIAL", "FAIL".
    output_dir : str or None
        Directory for output files. If None, defaults to
        <script_dir>/output/atlas/.
    """
    verdict = verdict.upper()
    if verdict not in PALETTES:
        print(f"ERROR: Invalid verdict '{verdict}'. Must be PASS, PARTIAL, or FAIL.")
        sys.exit(1)

    # Create figure
    fig = plt.figure(figsize=(FIG_WIDTH, FIG_HEIGHT), dpi=DPI)
    fig.patch.set_facecolor(PAGE_BG)

    # Draw layers (back to front)
    draw_watermark(fig)
    draw_header(fig)
    draw_verdict(fig, verdict)
    draw_metrics(fig, verdict)
    draw_footer(fig, verdict)

    # Output directory
    if output_dir is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        out_dir = os.path.join(script_dir, "output", "atlas")
    else:
        out_dir = output_dir
    os.makedirs(out_dir, exist_ok=True)

    # Save PNG
    png_path = os.path.join(out_dir, "ED_Architecture_Certificate.png")
    fig.savefig(
        png_path, dpi=DPI, facecolor=PAGE_BG,
        bbox_inches="tight", pad_inches=0.17,
    )
    print(f"  PNG: {png_path}")

    # Save PDF
    pdf_path = os.path.join(out_dir, "ED_Architecture_Certificate.pdf")
    fig.savefig(
        pdf_path, facecolor=PAGE_BG,
        bbox_inches="tight", pad_inches=0.17,
    )
    print(f"  PDF: {pdf_path}")

    plt.close(fig)
    print(f"\n  Verdict: {verdict}")
    print("  Certificate generated successfully.")


def main():
    parser = argparse.ArgumentParser(
        description="Generate the ED Architecture Certificate figure.",
    )
    parser.add_argument(
        "--verdict", type=str, default="PASS",
        choices=["PASS", "PARTIAL", "FAIL", "pass", "partial", "fail"],
        help="Certificate verdict (default: PASS).",
    )
    parser.add_argument(
        "--output-dir", type=str, default=None,
        help="Output directory for PNG/PDF (default: output/atlas/).",
    )
    args = parser.parse_args()

    print("  ED Architecture Certificate — Figure Generator")
    print("  " + "=" * 50)
    print()

    generate_certificate(args.verdict.upper(), output_dir=args.output_dir)


if __name__ == "__main__":
    main()
