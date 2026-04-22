"""
Generate the ED Math Pipeline diagram — the equation-rich version.

Shows the full derivation chain with actual math visible:

    ED-05 axioms + Compositional Rule
        |
    Architectural Canon (P1-P7) with their equations
        |
    UNIFIED PDE (with F[rho] operator and coupled v ODE)
        |
    Three channel isolations, each reducing to a known foundational equation
    (PME / Debye-RC / RLC oscillator)
        |
    Three predictions with their fitting laws (UDM, Cluster Merger-Lag, FRAP)

plus a bottom row of structural forks with formulas:
    D_nd = 0.3, D_crit ~ 0.896 (corrected 2026-04-22), universal invariants E_ground & t_rel,
    triad coupling C ≈ 0.03, dimensional formula alpha_R, ED-SC 2.0
    r* = −1.304, ED-XX 1/r source profile.

Output: docs/figures/ED-Math-Pipeline.png
"""

from __future__ import annotations

import os
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import FancyBboxPatch


# ----------------------------------------------------------------------------
# Palette
# ----------------------------------------------------------------------------

AXIOM     = "#e3dcf0"   # light purple
CANON     = "#d9e4f0"   # light blue
PDE       = "#3b5380"   # navy
CHANNEL   = "#f3ece1"   # parchment
REDUCTION = "#e1eddf"   # light green
CONFIRMED = "#d3ebd6"
PENDING   = "#fce9c6"
FORK      = "#f5e1e6"
EDGE      = "#2a3a52"
EDGE_SOFT = "#888888"

mpl.rcParams["mathtext.default"] = "regular"  # use regular weight for math

OUT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "docs", "figures", "ED-Math-Pipeline.png",
)


# ----------------------------------------------------------------------------
# Drawing helpers
# ----------------------------------------------------------------------------

def box(ax, x, y, w, h, face="#ffffff", edge=EDGE, pad=0.03, rounding=0.10, lw=1.4):
    rect = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad={pad},rounding_size={rounding}",
        linewidth=lw, edgecolor=edge, facecolor=face,
    )
    ax.add_patch(rect)


def txt(ax, x, y, s, fontsize=10, bold=False, italic=False, color="black",
        ha="center", va="center"):
    weight = "bold" if bold else "normal"
    style = "italic" if italic else "normal"
    ax.text(x, y, s, ha=ha, va=va, fontsize=fontsize,
            fontweight=weight, fontstyle=style, color=color)


def arrow(ax, x1, y1, x2, y2, label="", color=EDGE, lw=1.5, ls="-", labelpos=0.5):
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
                bbox=dict(facecolor="white", edgecolor="none", pad=2, alpha=0.92))


# ----------------------------------------------------------------------------
# Main figure
# ----------------------------------------------------------------------------

def build():
    W, H = 22.0, 16.0
    fig, ax = plt.subplots(figsize=(W, H))
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")

    # -------------------------------------------------------------------
    # Title
    # -------------------------------------------------------------------
    txt(ax, W / 2, H - 0.45,
        "ED — The Math Pipeline",
        fontsize=22, bold=True, color=EDGE)
    txt(ax, W / 2, H - 0.88,
        r"from ED-05 axioms through the Canon to a unique PDE, its channels, "
        r"its predictions, and the structural invariants that also fall out",
        fontsize=11, italic=True, color="#555")

    # -------------------------------------------------------------------
    # Row 1 : ED-05 axioms  +  Compositional Rule
    # -------------------------------------------------------------------
    ax_x, ax_y, ax_w, ax_h = 0.4, 13.1, 9.4, 1.75
    box(ax, ax_x, ax_y, ax_w, ax_h, face=AXIOM, edge=EDGE)
    txt(ax, ax_x + ax_w / 2, ax_y + ax_h - 0.22,
        "ED-05 — pre-PDE axioms (bare event domain)",
        fontsize=11, bold=True, color=EDGE)
    # 2-column axiom layout
    ax_lines = [
        (ax_x + 0.3, "A1", r"$\mathrm{ED}(A) \geq 0$", "non-negativity"),
        (ax_x + 0.3, "A2", r"$\mathrm{ED}(\emptyset) = 0$", "null baseline"),
        (ax_x + ax_w/2 + 0.15, "A3", r"$A \subseteq B \Rightarrow \mathrm{ED}(A) \leq \mathrm{ED}(B)$", "monotonicity"),
        (ax_x + ax_w/2 + 0.15, "A4", r"$\mathrm{ED}(A \cup B) \leq \mathrm{ED}(A) + \mathrm{ED}(B)$", "subadditivity"),
    ]
    for (xi, tag, eq, label) in ax_lines:
        yi = ax_y + ax_h - 0.70 - (["A1","A2","A3","A4"].index(tag) % 2) * 0.50
        txt(ax, xi, yi, tag, fontsize=10, bold=True, ha="left")
        txt(ax, xi + 0.40, yi, eq, fontsize=11, ha="left")
        txt(ax, xi + 0.40, yi - 0.26, label, fontsize=8.5, italic=True,
            color="#555", ha="left")

    # Compositional Rule (right)
    cr_x, cr_y, cr_w, cr_h = 10.0, 13.1, 11.6, 1.75
    box(ax, cr_x, cr_y, cr_w, cr_h, face=AXIOM, edge=EDGE)
    txt(ax, cr_x + cr_w / 2, cr_y + cr_h - 0.22,
        "Compositional Rule  (cosmological specialisation of A4)",
        fontsize=11, bold=True, color=EDGE)
    txt(ax, cr_x + cr_w / 2, cr_y + cr_h / 2 - 0.05,
        r"$p(A \cup B) = p(A) + p(B) "
        r"- \alpha\!\int_{A\cap B} p^\gamma d\mu "
        r"- \beta\!\int_{A\cup B} |\nabla p|^2 d\mu "
        r"- \gamma\!\int_{\partial(A\cup B)} h(|\nabla p|)\, dS$",
        fontsize=11.5)
    txt(ax, cr_x + cr_w / 2, cr_y + 0.30,
        "three correction terms  ->  relational penalty  +  gradient penalty  +  boundary / horizon term",
        fontsize=8.6, italic=True, color="#555")

    # -------------------------------------------------------------------
    # Row 2 : Architectural Canon P1-P7
    # -------------------------------------------------------------------
    cn_x, cn_y, cn_w, cn_h = 0.4, 9.50, 21.2, 3.35
    box(ax, cn_x, cn_y, cn_w, cn_h, face=CANON, edge=EDGE)
    txt(ax, cn_x + cn_w / 2, cn_y + cn_h - 0.25,
        "Architectural Canon (00.2)  —  seven structural demands, each a forced consequence",
        fontsize=11.5, bold=True, color=EDGE)

    # 4-column grid of P1-P7 plus uniqueness callout
    pgrid = [
        ("P1", "operator structure",
         r"$F[\rho] = M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho)$"),
        ("P2", "channel complementarity",
         r"$\partial_t \rho = D\cdot F[\rho] + H\cdot v,\; D+H=1$"),
        ("P3", "penalty equilibrium",
         r"$P(\rho^*) = 0,\; P'(\rho^*) > 0$"),
        ("P4", "mobility capacity bound",
         r"$M(\rho_{\max}) = 0,\; M(\rho) > 0$ for $\rho < \rho_{\max}$"),
        ("P5", "participation feedback",
         r"$\dot{v} = \frac{1}{\tau}(\,\bar F[\rho] - \zeta v\,)$"),
        ("P6", "damping discriminant",
         r"$(D-\zeta)^2 < 4(1-D); \; D_{\rm crit} \approx 0.896$ ($\zeta{=}1/4$)"),
        ("P7", "nonlinear triad",
         r"$M'(\rho)|\nabla\rho|^2$  generates  $k_3 = k_1 \pm k_2$"),
    ]

    col_w = (cn_w - 0.4) / 4
    row_h = 1.30
    row_y_base = cn_y + cn_h - 0.95  # first row text centerline
    for i, (tag, name, eq) in enumerate(pgrid):
        col = i % 4
        row = i // 4
        xi = cn_x + 0.2 + col * col_w
        yi = row_y_base - row * row_h
        txt(ax, xi, yi + 0.30, tag, fontsize=10.5, bold=True, ha="left",
            color=EDGE)
        txt(ax, xi + 0.42, yi + 0.30, name, fontsize=9.5, ha="left",
            color="black")
        txt(ax, xi + 0.05, yi - 0.05, eq, fontsize=10.2, ha="left")

    # 8th slot : uniqueness callout
    xi = cn_x + 0.2 + 3 * col_w
    yi = row_y_base - 1 * row_h
    txt(ax, xi, yi + 0.30, "D.19", fontsize=10.5, bold=True, ha="left",
        color="#6b2e45")
    txt(ax, xi + 0.55, yi + 0.30, "uniqueness theorem",
        fontsize=9.5, ha="left", color="black", bold=True)
    txt(ax, xi + 0.05, yi - 0.02,
        "no freedom to choose —",
        fontsize=9.3, ha="left", color="#6b2e45")
    txt(ax, xi + 0.05, yi - 0.25,
        "the PDE is selected uniquely",
        fontsize=9.3, ha="left", color="#6b2e45")

    # Arrows: axioms/rule --> canon
    arrow(ax, ax_x + ax_w / 2, ax_y - 0.05,
          ax_x + ax_w / 2 + 1.2, cn_y + cn_h + 0.05,
          color=EDGE_SOFT, label="structure")
    arrow(ax, cr_x + cr_w / 2, cr_y - 0.05,
          cr_x + cr_w / 2 - 2.0, cn_y + cn_h + 0.05,
          color=EDGE_SOFT)

    # -------------------------------------------------------------------
    # Row 3 : UNIFIED PDE
    # -------------------------------------------------------------------
    pde_x, pde_y, pde_w, pde_h = 2.0, 7.20, 18.0, 2.35
    box(ax, pde_x, pde_y, pde_w, pde_h, face=PDE, edge=EDGE, pad=0.06)
    txt(ax, pde_x + pde_w / 2, pde_y + pde_h - 0.28,
        "THE UNIFIED PDE  —  one scalar density field + one participation ODE",
        fontsize=13, bold=True, color="white")
    txt(ax, pde_x + pde_w / 2, pde_y + pde_h - 0.85,
        r"$\partial_t \rho \;=\; D \cdot \left[\, M(\rho)\,\nabla^2\rho "
        r"+ M'(\rho)\,|\nabla\rho|^2 - P(\rho)\, \right] \;+\; H \cdot v$",
        fontsize=16, color="white")
    txt(ax, pde_x + pde_w / 2, pde_y + pde_h - 1.40,
        r"$\tau\,\dot{v} = \bar F(\rho) - \zeta\,v$",
        fontsize=13, color="#e3e8f0")
    txt(ax, pde_x + pde_w / 4, pde_y + 0.35,
        r"$M(\rho) = M_0(\rho_{\max}-\rho)^\beta$",
        fontsize=11.5, color="white")
    txt(ax, pde_x + 3 * pde_w / 4, pde_y + 0.35,
        r"$P_{\rm SY2}(\rho) = \alpha\gamma \cdot "
        r"\dfrac{\rho - \rho^*}{\sqrt{(\rho-\rho^*)^2 + \rho_0^2}}$",
        fontsize=11.5, color="white")

    # arrow canon -> pde
    arrow(ax, pde_x + pde_w / 2, cn_y - 0.05,
          pde_x + pde_w / 2, pde_y + pde_h + 0.05,
          color=EDGE, label="forced  (Theorem D.19)", lw=1.8)

    # -------------------------------------------------------------------
    # Row 4 : three channels isolated (with the sub-equation each produces)
    # -------------------------------------------------------------------
    ch_y, ch_h = 5.35, 1.55
    ch_w = 6.5
    ch_gap = 0.25
    ch_x0 = (W - (3 * ch_w + 2 * ch_gap)) / 2
    channels = [
        ("MOBILITY channel alone",
         r"$\partial_t \rho = D\,\nabla\!\cdot\![M(\rho)\nabla\rho]$",
         "penalty = 0, participation = 0"),
        ("PENALTY channel alone",
         r"$\partial_t \rho = -D\,P_0(\rho - \rho^*)$",
         "uniform field, no spatial gradients"),
        ("PARTICIPATION channel alone",
         r"$\tau\,\dot{v} + \zeta\,v = \bar F(\rho)$",
         "uniform source, no density dynamics"),
    ]
    ch_centers = []
    for i, (title, eq, note) in enumerate(channels):
        xi = ch_x0 + i * (ch_w + ch_gap)
        box(ax, xi, ch_y, ch_w, ch_h, face=CHANNEL)
        txt(ax, xi + ch_w / 2, ch_y + ch_h - 0.28, title,
            fontsize=10.5, bold=True)
        txt(ax, xi + ch_w / 2, ch_y + ch_h - 0.80, eq, fontsize=12.5)
        txt(ax, xi + ch_w / 2, ch_y + 0.25, note,
            fontsize=8.8, italic=True, color="#555")
        ch_centers.append(xi + ch_w / 2)

    # arrow from PDE to each channel
    for cx in ch_centers:
        arrow(ax, pde_x + pde_w / 2, pde_y + 0.02, cx, ch_y + ch_h + 0.02,
              color=EDGE_SOFT, lw=1.3)
    # overall label
    txt(ax, W / 2, ch_y + ch_h + 0.25,
        "turn each channel on alone",
        fontsize=10, italic=True, color=EDGE_SOFT)

    # -------------------------------------------------------------------
    # Row 5 : each reduces to a known foundational equation
    # -------------------------------------------------------------------
    rd_y, rd_h = 3.50, 1.65
    reductions = [
        ("POROUS MEDIUM EQUATION",
         r"$\partial_t \delta = D_{\rm pme}\,\nabla^2(\delta^m),\;\; m = \beta + 1$",
         r"Barenblatt:  $R(t) \propto t^{\,1/(d(m-1)+2)}$"),
        ("DEBYE / RC EXPONENTIAL",
         r"$\rho(t) = \rho^* + (\rho_0 - \rho^*)\,e^{-DP_0\,t}$",
         r"time constant  $\tau_{\rm RC} = 1/(DP_0)$"),
        ("TELEGRAPH / RLC OSCILLATOR",
         r"$\tau\,\ddot{v} + \zeta\,\dot{v} + v = 0$",
         r"$\omega = \sqrt{1/\tau - (\zeta/2\tau)^2}$"),
    ]
    for i, (title, main, extra) in enumerate(reductions):
        xi = ch_x0 + i * (ch_w + ch_gap)
        box(ax, xi, rd_y, ch_w, rd_h, face=REDUCTION, edge=EDGE_SOFT)
        txt(ax, xi + ch_w / 2, rd_y + rd_h - 0.25, title,
            fontsize=10.2, bold=True, italic=False)
        txt(ax, xi + ch_w / 2, rd_y + rd_h - 0.80, main, fontsize=12)
        txt(ax, xi + ch_w / 2, rd_y + 0.38, extra, fontsize=10.2)

    # arrows channel -> reduction
    for i, cx in enumerate(ch_centers):
        lbl = "reduces EXACTLY  ->" if i == 1 else ""
        arrow(ax, cx, ch_y - 0.02, cx, rd_y + rd_h + 0.02,
              color=EDGE_SOFT, lw=1.3, label=lbl)

    # -------------------------------------------------------------------
    # Row 6 : predictions with math
    # -------------------------------------------------------------------
    pr_y, pr_h = 1.50, 1.75
    predictions = [
        ("UDM", CONFIRMED,
         r"$D(c) = D_0\left(1 - c/c_{\max}\right)^\beta$",
         r"11 materials, $R^2 > 0.986$",
         "CONFIRMED  -  one law, one exponent, no per-material tuning"),
        ("CLUSTER MERGER-LAG", CONFIRMED,
         r"$\ell = D_T / v_{\rm current}$",
         r"$D_T = 2.1\times 10^{27}\,\rm m^2/s$  (from Mistele WL)",
         "CONFIRMED  -  7 clusters + Finner+25 aggregate of 58 subclusters"),
        ("FRAP on BSA", PENDING,
         r"$\tau\,\ddot{\rho} + \zeta\,\dot{\rho} + \rho = 0$" +
         " recovery signature",
         "Creative Proteomics technician review",
         "PENDING  -  RLC-like recovery predicted, awaiting lab window"),
    ]
    for i, (title, face, eq, mid, bottom) in enumerate(predictions):
        xi = ch_x0 + i * (ch_w + ch_gap)
        box(ax, xi, pr_y, ch_w, pr_h, face=face)
        txt(ax, xi + ch_w / 2, pr_y + pr_h - 0.25, title,
            fontsize=10.5, bold=True)
        txt(ax, xi + ch_w / 2, pr_y + pr_h - 0.75, eq, fontsize=12)
        txt(ax, xi + ch_w / 2, pr_y + pr_h - 1.20, mid,
            fontsize=9.5, italic=True)
        status_color = "#2d6142" if face == CONFIRMED else "#8a6d18"
        txt(ax, xi + ch_w / 2, pr_y + 0.28, bottom,
            fontsize=8.8, bold=True, color=status_color)

    # arrows reduction -> prediction
    for i, cx in enumerate(ch_centers):
        arrow(ax, cx, rd_y - 0.02, cx, pr_y + pr_h + 0.02,
              color=EDGE_SOFT, lw=1.3)

    # -------------------------------------------------------------------
    # Bottom row : structural forks (in a single wide box with 6 cells)
    # -------------------------------------------------------------------
    fk_x, fk_y, fk_w, fk_h = 0.4, 0.20, 21.2, 1.25
    box(ax, fk_x, fk_y, fk_w, fk_h, face=FORK, edge="#6b2e45")
    txt(ax, fk_x + fk_w / 2, fk_y + fk_h - 0.18,
        "...and these also fall out of the same equation, no additional assumptions",
        fontsize=10.2, bold=True, color="#6b2e45")

    forks = [
        ("dimensional invariant",
         r"$D \cdot T_0 / L_0^2 = 0.3$",
         "exact across 5 regimes (61 OOM)"),
        ("sharp bifurcation",
         r"$(D-\zeta)^2 = 4(1-D) \Rightarrow D_{\rm crit}\approx 0.896$",
         "ED-09.5 Q-C prediction ($\\zeta=1/4$)"),
        ("universal invariants",
         r"$E_{\rm ground}=\alpha\gamma\rho_0,\; t_{\rm rel}\approx\rho_0/(\alpha\gamma)$",
         "regime- and IC-independent"),
        ("triad coupling",
         r"$C \approx 0.03,\;\; k_3/k_1 = 3{-}6\%$",
         "spectral fingerprint of P7"),
        ("d-consistency",
         r"$\alpha_R = 1/(d(m-1)+2)$",
         "d=1,2,3 verified exactly (P7 / SIM-3D)"),
        ("ED-SC 2.0 invariant",
         r"$r^* = {\rm med}\,\mathcal{R}_{\rm motif}(\nabla^2 E) = -1.304$",
         "Scenario D  =  Local Group  =  Casimir"),
    ]
    ncells = len(forks)
    cell_w = (fk_w - 0.4) / ncells
    for i, (name, eq, note) in enumerate(forks):
        xi = fk_x + 0.2 + i * cell_w
        txt(ax, xi + cell_w / 2, fk_y + fk_h - 0.50, name,
            fontsize=9.5, bold=True, color="#6b2e45")
        txt(ax, xi + cell_w / 2, fk_y + fk_h - 0.78, eq, fontsize=10)
        txt(ax, xi + cell_w / 2, fk_y + 0.18, note, fontsize=8.3,
            italic=True, color="#555")

    # arrow PDE --> forks (dashed)
    arrow(ax, pde_x + pde_w / 2, pde_y - 0.05,
          fk_x + fk_w * 0.12, fk_y + fk_h + 0.05,
          color="#6b2e45", lw=1.2, ls="--",
          label="same equation", labelpos=0.7)
    arrow(ax, pde_x + pde_w / 2, pde_y - 0.05,
          fk_x + fk_w * 0.88, fk_y + fk_h + 0.05,
          color="#6b2e45", lw=1.2, ls="--")

    # -------------------------------------------------------------------
    # Save
    # -------------------------------------------------------------------
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    fig.savefig(OUT, dpi=140, bbox_inches="tight", facecolor="white")
    print(f"wrote {OUT}")
    return OUT


if __name__ == "__main__":
    build()
