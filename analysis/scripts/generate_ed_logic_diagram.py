"""
Generate the ED logic-flow diagram — the story of how the math "falls out":

    4 primitives
       v
    7 constraints (each with rationale)
       v
    one unique PDE  (uniqueness theorem)
       v
    three channels  (each reduces to known physics when isolated)
       v
    evidence (UDM, Cluster Merger-Lag, FRAP)

plus three "forks" showing the composite structural results that emerge from
the same PDE without additional assumptions (D_nd = 0.3 across 5 regimes,
D_crit sharp bifurcation = Q-C transition prediction (value corrected
2026-04-22 to D_crit ~ 0.896 at zeta=1/4; see theory/D_crit_Resolution_Memo.md)
saddle -> ED-SC 2.0 invariant r* = -1.304).

Output: docs/figures/ED-Logic-Flow.png
"""

from __future__ import annotations

import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


# ----------------------------------------------------------------------------
# Palette
# ----------------------------------------------------------------------------

PRIMITIVE  = "#e8edf3"  # light blue-gray
CANON      = "#d9e4f0"  # slightly darker blue
PDE        = "#3b5380"  # navy — the central object
CHANNEL    = "#f3ece1"  # parchment
PHYSICS    = "#ffffff"  # white
CONFIRMED  = "#d3ebd6"  # soft green
PENDING    = "#fce9c6"  # soft amber
UNTESTED   = "#ece1f3"  # soft lavender
FORK       = "#f5e1e6"  # soft burgundy
EDGE       = "#2a3a52"
EDGE_SOFT  = "#888888"

OUT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "docs", "figures", "ED-Logic-Flow.png",
)


# ----------------------------------------------------------------------------
# Drawing helpers
# ----------------------------------------------------------------------------

def box(ax, x, y, w, h, text, face="#ffffff", edge=EDGE, fontsize=10, bold=False,
        italic=False, pad=0.04, rounding=0.12):
    rect = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad={pad},rounding_size={rounding}",
        linewidth=1.6, edgecolor=edge, facecolor=face,
    )
    ax.add_patch(rect)
    weight = "bold" if bold else "normal"
    style = "italic" if italic else "normal"
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fontsize, fontweight=weight, fontstyle=style,
            color="white" if face == PDE else "black", wrap=True)


def arrow(ax, x1, y1, x2, y2, label="", color=EDGE, lw=1.6, ls="-",
          labelpos=0.5, labelbg="#ffffff"):
    ax.annotate(
        "", xy=(x2, y2), xytext=(x1, y1),
        arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                        mutation_scale=14, linestyle=ls),
    )
    if label:
        lx = x1 + (x2 - x1) * labelpos
        ly = y1 + (y2 - y1) * labelpos
        ax.text(lx, ly, label, ha="center", va="center",
                fontsize=8.5, style="italic", color=color,
                bbox=dict(facecolor=labelbg, edgecolor="none", pad=2, alpha=0.92))


# ----------------------------------------------------------------------------
# Build figure
# ----------------------------------------------------------------------------

def build():
    fig, ax = plt.subplots(figsize=(18, 11))
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 11)
    ax.axis("off")

    # Title
    ax.text(9, 10.55, "How Event Density's Math Falls Out",
            ha="center", va="center", fontsize=19, fontweight="bold",
            color=EDGE)
    ax.text(9, 10.18,
            "four ingredients -> seven structural demands -> one unique equation "
            "-> three channels that are already familiar physics",
            ha="center", va="center", fontsize=11, style="italic", color="#555")

    # -------------------------------------------------------------------
    # Tier 1: the four primitives (top row, left-center spine)
    # -------------------------------------------------------------------
    t1y, t1h = 9.10, 0.85
    prim_w, prim_gap = 2.0, 0.25
    prim_x0 = 0.5
    prims = [
        (r"$\rho(x,t)$" + "\ndensity\n(rate of becoming)"),
        (r"$v(t)$" + "\nparticipation\n(global memory)"),
        (r"$M(\rho)$" + "\nmobility\n(how becoming spreads)"),
        (r"$P(\rho)$" + "\npenalty\n(pull toward equilibrium)"),
    ]
    for i, label in enumerate(prims):
        xi = prim_x0 + i * (prim_w + prim_gap)
        box(ax, xi, t1y, prim_w, t1h, label, face=PRIMITIVE, fontsize=9.2)

    # Label bracket above
    ax.text(prim_x0 + (4 * prim_w + 3 * prim_gap) / 2, t1y + t1h + 0.22,
            "FOUR INGREDIENTS  (primitives)", ha="center", va="center",
            fontsize=11, fontweight="bold", color=EDGE)

    # -------------------------------------------------------------------
    # Tier 2: seven constraints with rationale (grouped box)
    # -------------------------------------------------------------------
    t2y, t2h = 6.55, 1.95
    t2x, t2w = 0.5, 4 * prim_w + 3 * prim_gap
    box(ax, t2x, t2y, t2w, t2h, "", face=CANON, edge=EDGE, fontsize=9)
    ax.text(t2x + t2w / 2, t2y + t2h - 0.22,
            "SEVEN STRUCTURAL DEMANDS  (each forced, not chosen)",
            ha="center", va="center", fontsize=10.5, fontweight="bold",
            color=EDGE)

    constraints = [
        ("P1", "there must be spatial dynamics",      "operator has diffusion + gradient + restoring term"),
        ("P2", "direct + memory both act",            "two channels sum to unity (D + H = 1)"),
        ("P3", "one unique rest state",               "penalty has a single zero, monotone around it"),
        ("P4", "capacity is finite",                  "mobility vanishes at the ceiling (rho_max)"),
        ("P5", "memory has its own clock",            "participation integrates the operator with damping"),
        ("P6", "regime transitions must exist",       "sharp bifurcation in damping discriminant"),
        ("P7", "nonlinear coupling must be coherent", "triad term: mode k=1 feeds k=3 at fixed ratio"),
    ]

    # Two-column layout inside the tier-2 box
    col_x = [t2x + 0.22, t2x + t2w / 2 + 0.05]
    row_h = 0.40
    rows_per_col = 4
    for i, (tag, reason, how) in enumerate(constraints):
        col = i // rows_per_col
        row = i % rows_per_col
        xi = col_x[col]
        yi = t2y + t2h - 0.55 - row * row_h
        ax.text(xi, yi, tag, ha="left", va="center", fontsize=9.5,
                fontweight="bold", color=EDGE)
        ax.text(xi + 0.35, yi + 0.10, reason, ha="left", va="center",
                fontsize=8.8, color="black")
        ax.text(xi + 0.35, yi - 0.10, "-> " + how, ha="left", va="center",
                fontsize=8.4, color="#555", style="italic")

    # Arrow from primitives to constraints
    arrow(ax, t2x + t2w / 2, t1y - 0.05,
          t2x + t2w / 2, t2y + t2h + 0.05,
          label="impose structure")

    # -------------------------------------------------------------------
    # Tier 3: unique PDE
    # -------------------------------------------------------------------
    t3y, t3h = 4.70, 1.40
    t3x, t3w = 0.5, t2w
    box(ax, t3x, t3y, t3w, t3h, "", face=PDE, edge=EDGE, pad=0.06)
    ax.text(t3x + t3w / 2, t3y + t3h - 0.28,
            "UNIQUENESS  ->  ONE EQUATION",
            ha="center", va="center", fontsize=12.5, fontweight="bold",
            color="white")
    ax.text(t3x + t3w / 2, t3y + t3h / 2 - 0.05,
            r"$\partial_t \rho \;=\; D \cdot F[\rho] \;+\; H \cdot v$",
            ha="center", va="center", fontsize=16, color="white")
    ax.text(t3x + t3w / 2, t3y + 0.28,
            "no free structural choices  -  D+H=1  -  "
            r"$F[\rho]$" + " built from M, P, and gradients",
            ha="center", va="center", fontsize=9, color="#e7e9ef",
            style="italic")

    arrow(ax, t2x + t2w / 2, t2y - 0.05,
          t3x + t3w / 2, t3y + t3h + 0.05,
          label="uniqueness theorem (D.19)")

    # -------------------------------------------------------------------
    # Tier 4: three channels (turn each on alone)
    # -------------------------------------------------------------------
    t4y, t4h = 3.10, 0.95
    ch_w, ch_gap = 2.9, 0.35
    ch_x0 = t3x + (t3w - (3 * ch_w + 2 * ch_gap)) / 2
    channels = [
        ("MOBILITY channel only",       "M(rho) spreads density,\nno penalty, no participation"),
        ("PENALTY channel only",        "P(rho) pulls to equilibrium,\nno spatial dynamics"),
        ("PARTICIPATION channel only",  "v(t) feeds back,\nno density gradients"),
    ]
    ch_centers = []
    for i, (title, desc) in enumerate(channels):
        xi = ch_x0 + i * (ch_w + ch_gap)
        box(ax, xi, t4y, ch_w, t4h, f"{title}\n{desc}", face=CHANNEL,
            fontsize=9)
        ch_centers.append(xi + ch_w / 2)

    ax.text(t3x + t3w / 2, t4y + t4h + 0.28,
            "TURN EACH CHANNEL ON ALONE",
            ha="center", va="center", fontsize=10.5, fontweight="bold",
            color=EDGE)

    # Three arrows splitting from the PDE
    for cx in ch_centers:
        arrow(ax, t3x + t3w / 2, t3y - 0.02, cx, t4y + t4h + 0.03,
              color=EDGE_SOFT, lw=1.3)

    # -------------------------------------------------------------------
    # Tier 5: known physics emerges
    # -------------------------------------------------------------------
    t5y, t5h = 1.85, 0.85
    physics_labels = [
        "POROUS MEDIUM EQUATION\n(nonlinear diffusion,\nBarenblatt spreading)",
        "DEBYE / RC EXPONENTIAL\n(linear relaxation to\nequilibrium)",
        "TELEGRAPH / RLC OSCILLATOR\n(damped wave with\nmemory)",
    ]
    for i, label in enumerate(physics_labels):
        xi = ch_x0 + i * (ch_w + ch_gap)
        box(ax, xi, t5y, ch_w, t5h, label, face=PHYSICS,
            edge=EDGE_SOFT, fontsize=8.8, italic=True)

    # Arrows from channels to physics with "reduces to" label on middle one
    for i, cx in enumerate(ch_centers):
        lbl = "each reduces exactly" if i == 1 else ""
        arrow(ax, cx, t4y - 0.02, cx, t5y + t5h + 0.02,
              color=EDGE_SOFT, lw=1.3, label=lbl)

    # -------------------------------------------------------------------
    # Tier 6: evidence (in-hand or in-flight)
    # -------------------------------------------------------------------
    t6y, t6h = 0.25, 1.20
    evidence = [
        ("UDM — 11 materials\n"
         r"$D(c) = D_0(1-c/c_{max})^\beta$" + "\n"
         "R^2 > 0.986", CONFIRMED, "CONFIRMED"),
        ("Cluster Merger-Lag\n"
         r"$\ell = D_T / v_{current}$" + "\n"
         "7 clusters + Finner+25", CONFIRMED, "CONFIRMED"),
        ("FRAP on high-conc BSA\n"
         "RLC-like recovery signature\n"
         "Creative Proteomics (in review)", PENDING, "PENDING"),
    ]
    for i, (label, face, tag) in enumerate(evidence):
        xi = ch_x0 + i * (ch_w + ch_gap)
        box(ax, xi, t6y, ch_w, t6h, label, face=face, fontsize=9.0)
        ax.text(xi + 0.10, t6y + t6h - 0.14, tag, ha="left", va="top",
                fontsize=8.0, fontweight="bold",
                color="#2d6142" if face == CONFIRMED else "#8a6d18")

    # Arrows from physics to evidence
    for i, cx in enumerate(ch_centers):
        arrow(ax, cx, t5y - 0.02, cx, t6y + t6h + 0.02,
              color=EDGE_SOFT, lw=1.3)

    # -------------------------------------------------------------------
    # Right column: structural forks (also fall out of the same PDE)
    # -------------------------------------------------------------------
    fx0, fw = 12.1, 5.4
    ax.text(fx0 + fw / 2, 10.10,
            "AND THE SAME PDE ALSO GIVES YOU...",
            ha="center", va="center", fontsize=12, fontweight="bold",
            color="#6b2e45")

    # Fork 1: D_nd = 0.3 dimensional invariant
    f1y, f1h = 7.85, 1.50
    box(ax, fx0, f1y, fw, f1h, "", face=FORK, edge="#6b2e45")
    ax.text(fx0 + fw / 2, f1y + f1h - 0.27,
            "FORK 1 — nondimensionalize",
            ha="center", va="center", fontsize=10, fontweight="bold",
            color="#6b2e45")
    ax.text(fx0 + fw / 2, f1y + f1h / 2 + 0.02,
            r"$D \cdot T_0 / L_0^2 \;=\; 0.3$" + "   (exact)",
            ha="center", va="center", fontsize=13)
    ax.text(fx0 + fw / 2, f1y + 0.28,
            "holds across 5 regimes spanning 61 orders of magnitude\n"
            "quantum | Planck | condensed matter | galactic | cosmological  —  CONFIRMED",
            ha="center", va="center", fontsize=8.7, style="italic",
            color="#2d6142")

    # Fork 2: D_crit sharp bifurcation (Q-C prediction). Value
    # corrected 2026-04-22 to D_crit ~ 0.896 at zeta=1/4 (not 0.5).
    f2y, f2h = 5.85, 1.70
    box(ax, fx0, f2y, fw, f2h, "", face=FORK, edge="#6b2e45")
    ax.text(fx0 + fw / 2, f2y + f2h - 0.27,
            "FORK 2 — damping discriminant (P6)",
            ha="center", va="center", fontsize=10, fontweight="bold",
            color="#6b2e45")
    ax.text(fx0 + fw / 2, f2y + f2h - 0.65,
            r"$(D - \zeta)^2 = 4(1 - D)$" + "   ->   sharp bifurcation at  " +
            r"$D_{crit}\!\approx\!0.896$ ($\zeta\!=\!1/4$)",
            ha="center", va="center", fontsize=11.5)
    ax.text(fx0 + fw / 2, f2y + 0.70,
            r"oscillatory ($D \ll D_{\rm crit}$)  |  hybrid  |  parabolic "
            r"($D \geq D_{\rm crit}$)"
            "\nquantum, reversible, waves  <->  classical, irreversible, structure",
            ha="center", va="center", fontsize=8.7, style="italic")
    ax.text(fx0 + fw / 2, f2y + 0.25,
            "ED-09.5 claim: this bifurcation IS the Q-C transition\n"
            "N_osc ~ 9, Q ~ 3.5, 3-6% harmonic  —  UNTESTED (candidate)",
            ha="center", va="center", fontsize=8.7, color="#5a3a74")

    # Fork 3: Scenario D saddle -> r* = -1.304 (ED-SC 2.0)
    f3y, f3h = 3.60, 2.00
    box(ax, fx0, f3y, fw, f3h, "", face=FORK, edge="#6b2e45")
    ax.text(fx0 + fw / 2, f3y + f3h - 0.27,
            "FORK 3 — add noise (ED-12.5 compositional form)",
            ha="center", va="center", fontsize=10, fontweight="bold",
            color="#6b2e45")
    ax.text(fx0 + fw / 2, f3y + f3h - 0.70,
            "Scenario D 4x4 sweep  ->  architectural saddle at (n*, sigma*)",
            ha="center", va="center", fontsize=9.5)
    ax.text(fx0 + fw / 2, f3y + f3h - 1.05,
            r"motif-conditioned median of $\nabla^2 E$" + "  ->  " +
            r"$r^* = -1.304$",
            ha="center", va="center", fontsize=11.5, fontweight="bold")
    ax.text(fx0 + fw / 2, f3y + f3h - 1.42,
            "matches Local Group mass sheet  +  Casimir cavity equilibria",
            ha="center", va="center", fontsize=8.7, style="italic")
    ax.text(fx0 + fw / 2, f3y + 0.25,
            "ED-SC 2.0 invariant (see docs/ED-SC-2.0.md)  —  CONFIRMED",
            ha="center", va="center", fontsize=8.7, fontweight="bold",
            color="#2d6142")

    # Fork 4: d=1,2,3 consistency -> ED-SIM-3D
    f4y, f4h = 1.85, 1.45
    box(ax, fx0, f4y, fw, f4h, "", face=FORK, edge="#6b2e45")
    ax.text(fx0 + fw / 2, f4y + f4h - 0.27,
            "FORK 4 — run the PDE in d = 1, 2, 3",
            ha="center", va="center", fontsize=10, fontweight="bold",
            color="#6b2e45")
    ax.text(fx0 + fw / 2, f4y + f4h / 2 - 0.05,
            "penalty + participation channels dimension-INDEPENDENT\n"
            r"mobility channel dimension-dependent per $\alpha_R = 1/(d(m-1)+2)$",
            ha="center", va="center", fontsize=9.2)
    ax.text(fx0 + fw / 2, f4y + 0.22,
            "ED-SIM-3D five-invariant mini-atlas  —  CONFIRMED",
            ha="center", va="center", fontsize=8.7, fontweight="bold",
            color="#2d6142")

    # Pipe from PDE to forks
    arrow(ax, t3x + t3w + 0.05, t3y + t3h / 2,
          fx0 - 0.05, (f1y + f4y + f4h) / 2,
          color=EDGE_SOFT, lw=1.6, ls="--",
          label="same equation, no extra assumptions")

    # -------------------------------------------------------------------
    # Legend
    # -------------------------------------------------------------------
    lx, ly, lw, lh = 0.5, 0.02, 10.0, 0.15
    ax.text(lx, ly + 0.03,
            "green = empirical confirmation   "
            "|   amber = in flight   "
            "|   lavender = predicted, untested   "
            "|   burgundy = structural fork (also falls out of the same PDE)",
            ha="left", va="bottom", fontsize=8.3, color="#555",
            style="italic")

    plt.tight_layout()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    fig.savefig(OUT, dpi=140, bbox_inches="tight", facecolor="white")
    print(f"wrote {OUT}")
    return OUT


if __name__ == "__main__":
    build()
