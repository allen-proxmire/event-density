"""
Generate the ED Math Pipeline diagram v2 — adds the Seven Constraints block
as a pre-architectural "gate" between the ED-05 axioms and the Compositional
Rule.  Every other block is preserved from v1 in content; the canvas is
taller to accommodate the new row cleanly.

Flow:

    ED-05 axioms (A1-A4)
        |
    SEVEN CONSTRAINTS  (locality / isotropy / gradient-driven /
                        dissipative / single scalar field /
                        minimal coupling / dimensional consistency)
        |
    Compositional Rule
        |
    Architectural Canon (P1-P7)  +  D.19 uniqueness
        |
    UNIFIED PDE
        |
    Three channels isolated
        |
    Three textbook reductions
        |
    Three empirical modules
        |
    Structural forks (six invariants)

Output: docs/figures/ED-Math-Pipeline_v2.png
"""

from __future__ import annotations

import os
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import FancyBboxPatch


# ----------------------------------------------------------------------------
# Palette
# ----------------------------------------------------------------------------

AXIOM            = "#e3dcf0"
CONSTRAINT       = "#ece3f4"   # softer lavender for the gate / filter layer
CONSTRAINT_EDGE  = "#6d5aa1"
CANON            = "#d9e4f0"
PDE              = "#3b5380"
CHANNEL          = "#f3ece1"
REDUCTION        = "#e1eddf"
CONFIRMED        = "#d3ebd6"
PENDING          = "#fce9c6"
FORK             = "#f5e1e6"
EDGE             = "#2a3a52"
EDGE_SOFT        = "#888888"

mpl.rcParams["mathtext.default"] = "regular"

OUT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "docs", "figures", "ED-Math-Pipeline_v5.png",
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
    W, H = 22.0, 20.60
    fig, ax = plt.subplots(figsize=(W, H))
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")

    # Title ----------------------------------------------------------------
    txt(ax, W / 2, H - 0.40,
        "ED — The Math Pipeline  (v5)",
        fontsize=22, bold=True, color=EDGE)
    txt(ax, W / 2, H - 0.85,
        r"from ED-05 axioms through the Seven Constraints and the Canon "
        r"to a unique PDE, its channels, its predictions, and the structural invariants",
        fontsize=11, italic=True, color="#555")

    # Row 1 — Axioms (A1-A4), full width -----------------------------------
    ax_x, ax_y, ax_w, ax_h = 0.4, 17.65, 21.2, 1.80
    box(ax, ax_x, ax_y, ax_w, ax_h, face=AXIOM, edge=EDGE)
    txt(ax, ax_x + ax_w / 2, ax_y + ax_h - 0.25,
        "ED-05 — pre-PDE axioms (bare event domain)",
        fontsize=11.5, bold=True, color=EDGE)

    ax_lines = [
        ("A1", r"$\mathrm{ED}(A) \geq 0$", "non-negativity"),
        ("A2", r"$\mathrm{ED}(\emptyset) = 0$", "null baseline"),
        ("A3", r"$A \subseteq B \Rightarrow \mathrm{ED}(A) \leq \mathrm{ED}(B)$",
         "monotonicity"),
        ("A4", r"$\mathrm{ED}(A \cup B) \leq \mathrm{ED}(A) + \mathrm{ED}(B)$",
         "subadditivity"),
    ]
    col_w = (ax_w - 0.4) / 4
    for i, (tag, eq, label) in enumerate(ax_lines):
        xi = ax_x + 0.2 + i * col_w
        cy = ax_y + ax_h / 2 - 0.05
        txt(ax, xi + 0.20, cy + 0.18, tag, fontsize=10.5, bold=True, ha="left",
            color=EDGE)
        txt(ax, xi + 0.20, cy - 0.20, eq, fontsize=11.0, ha="left")
        txt(ax, xi + 0.20, cy - 0.58, label, fontsize=8.8, italic=True,
            color="#555", ha="left")

    # Row 2 — Seven Constraints (the "gate") -------------------------------
    cg_x, cg_y, cg_w, cg_h = 0.4, 15.35, 21.2, 1.95
    box(ax, cg_x, cg_y, cg_w, cg_h,
        face=CONSTRAINT, edge=CONSTRAINT_EDGE, lw=1.8)
    txt(ax, cg_x + cg_w / 2, cg_y + cg_h - 0.25,
        "Seven Constraints  —  the pre-architectural frame the PDE must live inside",
        fontsize=11.5, bold=True, color=CONSTRAINT_EDGE)

    # bracket bars on left/right reinforce "gate"
    for bx in (cg_x + 0.12, cg_x + cg_w - 0.12):
        ax.plot([bx, bx], [cg_y + 0.25, cg_y + cg_h - 0.55],
                color=CONSTRAINT_EDGE, lw=2.4, solid_capstyle="round")

    constraints = [
        ("Locality",              r"$F[\rho](x) \leftarrow \rho(x + \varepsilon)$"),
        ("Isotropy",              r"$F[R\rho] = R\,F[\rho]$"),
        ("Gradient-driven flow",  r"$J = -\,M(\rho)\,\nabla\rho$"),
        ("Dissipative",           r"$dE/dt \leq 0$"),
        ("Single scalar field",   r"$\rho : \mathbb{R}^d \times \mathbb{R} \to \mathbb{R}$"),
        ("Minimal coupling",      r"$\rho \leftrightarrow v$  (one loop)"),
        ("Dimensional consistency", r"$[\mathrm{LHS}] = [\mathrm{RHS}]$"),
    ]
    ncells = len(constraints)
    inner_x = cg_x + 0.40
    inner_w = cg_w - 0.80
    cell_w = inner_w / ncells
    for i, (name, eq) in enumerate(constraints):
        xi = inner_x + i * cell_w
        box(ax, xi + 0.06, cg_y + 0.30, cell_w - 0.12, cg_h - 1.00,
            face="#ffffff", edge=CONSTRAINT_EDGE, lw=1.1,
            pad=0.02, rounding=0.08)
        txt(ax, xi + cell_w / 2, cg_y + cg_h - 0.78, name,
            fontsize=9.4, bold=True, color=CONSTRAINT_EDGE)
        txt(ax, xi + cell_w / 2, cg_y + cg_h - 1.20, eq, fontsize=10.0)
        txt(ax, xi + 0.22, cg_y + cg_h - 0.55, f"C{i+1}",
            fontsize=7.8, bold=True, color="#8a7ab6", ha="left")

    arrow(ax, ax_x + ax_w / 2, ax_y - 0.05,
          cg_x + cg_w / 2, cg_y + cg_h + 0.05,
          color=EDGE_SOFT, label="counting is structured",
          lw=1.6)

    # Row 3 — Compositional Rule ------------------------------------------
    cr_x, cr_y, cr_w, cr_h = 0.4, 13.15, 21.2, 1.70
    box(ax, cr_x, cr_y, cr_w, cr_h, face=AXIOM, edge=EDGE)
    txt(ax, cr_x + cr_w / 2, cr_y + cr_h - 0.25,
        "Compositional Rule  (cosmological specialisation of A4, shaped by the Seven Constraints)",
        fontsize=11.5, bold=True, color=EDGE)
    txt(ax, cr_x + cr_w / 2, cr_y + cr_h / 2 - 0.05,
        r"$p(A \cup B) = p(A) + p(B) "
        r"- \alpha\!\int_{A\cap B} p^\gamma d\mu "
        r"- \beta\!\int_{A\cup B} |\nabla p|^2 d\mu "
        r"- \gamma\!\int_{\partial(A\cup B)} h(|\nabla p|)\, dS$",
        fontsize=12.0)
    txt(ax, cr_x + cr_w / 2, cr_y + 0.30,
        "three correction terms  ->  relational penalty  +  gradient penalty  +  boundary / horizon term",
        fontsize=8.8, italic=True, color="#555")

    arrow(ax, cg_x + cg_w / 2, cg_y - 0.05,
          cr_x + cr_w / 2, cr_y + cr_h + 0.05,
          color=CONSTRAINT_EDGE,
          label="filtered through the frame", lw=1.6)

    # Row 4 — Architectural Canon P1-P7 + D.19 uniqueness ------------------
    cn_x, cn_y, cn_w, cn_h = 0.4, 9.85, 21.2, 2.80
    box(ax, cn_x, cn_y, cn_w, cn_h, face=CANON, edge=EDGE)
    txt(ax, cn_x + cn_w / 2, cn_y + cn_h - 0.25,
        "Architectural Canon (00.2)  —  seven structural demands, each a forced consequence",
        fontsize=11.5, bold=True, color=EDGE)

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
         r"$(D-\zeta)^2 < 4(1-D);\; D_{\rm crit} \approx 0.896$ ($\zeta{=}1/4$, sharp)"),
        ("P7", "nonlinear triad",
         r"$M'(\rho)|\nabla\rho|^2$  generates  $k_3 = k_1 \pm k_2$"),
    ]

    col_w_p = (cn_w - 0.4) / 4
    row_h = 1.30
    row_y_base = cn_y + cn_h - 0.95
    for i, (tag, name, eq) in enumerate(pgrid):
        col = i % 4
        row = i // 4
        xi = cn_x + 0.2 + col * col_w_p
        yi = row_y_base - row * row_h
        txt(ax, xi, yi + 0.30, tag, fontsize=10.5, bold=True, ha="left",
            color=EDGE)
        txt(ax, xi + 0.42, yi + 0.30, name, fontsize=9.5, ha="left",
            color="black")
        txt(ax, xi + 0.05, yi - 0.05, eq, fontsize=10.2, ha="left")

    # 8th slot : D.19 uniqueness callout
    xi = cn_x + 0.2 + 3 * col_w_p
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

    arrow(ax, cr_x + cr_w / 2, cr_y - 0.05,
          cn_x + cn_w / 2, cn_y + cn_h + 0.05,
          color=EDGE_SOFT, label="structure")

    # Row 5 — Unified PDE --------------------------------------------------
    pde_x, pde_y, pde_w, pde_h = 2.0, 7.35, 18.0, 2.25
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
    txt(ax, pde_x + pde_w / 4, pde_y + 0.32,
        r"$M(\rho) = M_0(\rho_{\max}-\rho)^\beta$",
        fontsize=11.5, color="white")
    txt(ax, pde_x + 3 * pde_w / 4, pde_y + 0.32,
        r"$P_{\rm SY2}(\rho) = \alpha\gamma \cdot "
        r"\dfrac{\rho - \rho^*}{\sqrt{(\rho-\rho^*)^2 + \rho_0^2}}$",
        fontsize=11.5, color="white")

    arrow(ax, pde_x + pde_w / 2, cn_y - 0.05,
          pde_x + pde_w / 2, pde_y + pde_h + 0.05,
          color=EDGE, label="forced  (Theorem D.19)", lw=1.8)

    # Row 6 — Three channels isolated -------------------------------------
    ch_y, ch_h = 5.60, 1.50
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
        txt(ax, xi + ch_w / 2, ch_y + 0.22, note,
            fontsize=8.8, italic=True, color="#555")
        ch_centers.append(xi + ch_w / 2)

    for cx in ch_centers:
        arrow(ax, pde_x + pde_w / 2, pde_y + 0.02, cx, ch_y + ch_h + 0.02,
              color=EDGE_SOFT, lw=1.3)
    txt(ax, W / 2, ch_y + ch_h + 0.22,
        "turn each channel on alone",
        fontsize=10, italic=True, color=EDGE_SOFT)

    # Row 7 — Textbook reductions -----------------------------------------
    rd_y, rd_h = 3.80, 1.55
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
        txt(ax, xi + ch_w / 2, rd_y + rd_h - 0.24, title,
            fontsize=10.2, bold=True)
        txt(ax, xi + ch_w / 2, rd_y + rd_h - 0.78, main, fontsize=12)
        txt(ax, xi + ch_w / 2, rd_y + 0.30, extra, fontsize=10.2)

    for i, cx in enumerate(ch_centers):
        lbl = "reduces EXACTLY  ->" if i == 1 else ""
        arrow(ax, cx, ch_y - 0.02, cx, rd_y + rd_h + 0.02,
              color=EDGE_SOFT, lw=1.3, label=lbl)

    # Row 8 — Empirical predictions ---------------------------------------
    pr_y, pr_h = 1.95, 1.65
    predictions = [
        ("UDM", CONFIRMED,
         r"$D(c) = D_0\left(1 - c/c_{\max}\right)^\beta$",
         r"10 materials, 8 mechanisms, $R^2 > 0.986$",
         "CONFIRMED  -  one law, one exponent, no per-material tuning"),
        ("CLUSTER MERGER-LAG", CONFIRMED,
         r"$\ell = D_T / v_{\rm current}$",
         r"$D_T = 2.1\times 10^{27}\,\rm m^2/s$  (from Mistele WL)",
         "CONFIRMED  -  7 clusters + Finner+25 aggregate of 58 subclusters"),
        ("FRAP on BSA", PENDING,
         r"$\tau\,\ddot{\rho} + \zeta\,\dot{\rho} + \rho = 0$  recovery signature",
         "Creative Proteomics technician review",
         "PENDING  -  RLC-like recovery predicted, awaiting lab window"),
    ]
    for i, (title, face, eq, mid, bottom) in enumerate(predictions):
        xi = ch_x0 + i * (ch_w + ch_gap)
        box(ax, xi, pr_y, ch_w, pr_h, face=face)
        txt(ax, xi + ch_w / 2, pr_y + pr_h - 0.24, title,
            fontsize=10.5, bold=True)
        txt(ax, xi + ch_w / 2, pr_y + pr_h - 0.72, eq, fontsize=11.5)
        txt(ax, xi + ch_w / 2, pr_y + pr_h - 1.14, mid,
            fontsize=9.4, italic=True)
        status_color = "#2d6142" if face == CONFIRMED else "#8a6d18"
        txt(ax, xi + ch_w / 2, pr_y + 0.25, bottom,
            fontsize=8.8, bold=True, color=status_color)

    for cx in ch_centers:
        arrow(ax, cx, rd_y - 0.02, cx, pr_y + pr_h + 0.02,
              color=EDGE_SOFT, lw=1.3)

    # Row 9 — Structural forks ribbon (six invariants) ---------------------
    fk_x, fk_y, fk_w, fk_h = 0.4, 0.20, 21.2, 1.60
    box(ax, fk_x, fk_y, fk_w, fk_h, face=FORK, edge="#6b2e45")
    txt(ax, fk_x + fk_w / 2, fk_y + fk_h - 0.22,
        "...and these also fall out of the same equation, no additional assumptions",
        fontsize=10.2, bold=True, color="#6b2e45")

    forks = [
        ("dimensional invariant",
         r"$D \cdot T_0 / L_0^2 = 0.3$",
         "exact across 5 regimes (61 OOM)"),
        ("sharp bifurcation",
         r"$(D-\zeta)^2=4(1-D) \Rightarrow D_{\rm crit}\!\approx\!0.896$",
         r"ED-09.5 Q-C prediction ($\zeta{=}1/4$)"),
        ("universal invariants",
         r"$E_{\rm g}=\alpha\gamma\rho_0,\; t_{\rm rel}\approx\rho_0/(\alpha\gamma)$",
         "regime- and IC-independent"),
        ("triad coupling",
         r"$C \approx 0.03,\;\; k_3/k_1 = 3{-}6\%$",
         "spectral fingerprint of P7"),
        ("d-consistency",
         r"$\alpha_R = 1/(d(m-1)+2)$",
         "d=1,2,3 verified exactly"),
        ("ED-SC 2.0 invariant",
         r"$r^* = {\rm med}\,\mathcal{R}_{\rm motif}(\nabla^2 E) \approx -1.304$",
         "Scenario D = Local Group = Casimir"),
    ]
    ncells_f = len(forks)
    cell_w_f = (fk_w - 0.4) / ncells_f
    for i, (name, eq, note) in enumerate(forks):
        xi = fk_x + 0.2 + i * cell_w_f
        txt(ax, xi + cell_w_f / 2, fk_y + fk_h - 0.60, name,
            fontsize=9.6, bold=True, color="#6b2e45")
        txt(ax, xi + cell_w_f / 2, fk_y + fk_h - 0.95, eq, fontsize=10.0)
        txt(ax, xi + cell_w_f / 2, fk_y + 0.28, note, fontsize=8.3,
            italic=True, color="#555")

    # dashed arrows PDE -> forks ribbon
    arrow(ax, pde_x + pde_w / 2, pde_y - 0.05,
          fk_x + fk_w * 0.12, fk_y + fk_h + 0.05,
          color="#6b2e45", lw=1.2, ls="--",
          label="same equation", labelpos=0.72)
    arrow(ax, pde_x + pde_w / 2, pde_y - 0.05,
          fk_x + fk_w * 0.88, fk_y + fk_h + 0.05,
          color="#6b2e45", lw=1.2, ls="--")

    # Save -----------------------------------------------------------------
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    fig.savefig(OUT, dpi=140, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"wrote {OUT}")
    return OUT


if __name__ == "__main__":
    build()
