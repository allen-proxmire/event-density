"""
ED Math Pipeline v6 — renders the full v6 specification in docs/ED-Math-Pipeline-v6-spec.md
to docs/figures/ED-Math-Pipeline_v6.png.

Layout:
  Top spine (full width):   Title -> Axioms -> 7 Constraints -> Compositional Rule
                            -> Canon P1-P7 + D.19 -> Unified PDE
  Three parallel branches:  A (channels -> reductions -> predictions)     [left]
                            B (RG spine: 10 rows)                          [centre]
                            C (dimensional dictionary + 0.6 resolution)    [right]
  Bottom spine:             Cross-scale invariance restated
                            Structural forks ribbon (v5 + v6 extensions)
"""
from __future__ import annotations
import os
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import FancyBboxPatch

mpl.rcParams["mathtext.default"] = "regular"

# --- palette ---------------------------------------------------------------
AXIOM            = "#e3dcf0"
CONSTRAINT       = "#ece3f4"
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

RG_SPINE         = "#dceafc"
RG_EDGE          = "#2b4d7a"
RG_ACCENT        = "#c7ddf7"

FP_G             = "#eef5ff"
FP_WF            = "#f5eef9"
FP_NM            = "#eef9ef"
FP_INF           = "#f9efef"
FP_EDGE          = "#3a5a8a"

REG_UV           = "#eef0f9"
REG_INT          = "#f3ece1"
REG_IR           = "#e7e2d4"

DICT_BG          = "#d3ebd6"
DICT_EDGE        = "#2d6142"

INV_BG           = "#fff4e1"
INV_EDGE         = "#a67b2a"

OUT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "docs", "figures", "ED-Math-Pipeline_v6.png",
)

# --- helpers ---------------------------------------------------------------
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

def arrow(ax, x1, y1, x2, y2, label="", color=EDGE, lw=1.5, ls="-", labelpos=0.5,
          labelsize=8.5):
    ax.annotate(
        "", xy=(x2, y2), xytext=(x1, y1),
        arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                        mutation_scale=14, linestyle=ls),
    )
    if label:
        lx = x1 + (x2 - x1) * labelpos
        ly = y1 + (y2 - y1) * labelpos
        ax.text(lx, ly, label, ha="center", va="center",
                fontsize=labelsize, style="italic", color=color,
                bbox=dict(facecolor="white", edgecolor="none", pad=2, alpha=0.92))

# --- main figure -----------------------------------------------------------
def build():
    W, H = 30.0, 60.0
    fig, ax = plt.subplots(figsize=(W, H))
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")

    # =====================================================================
    # TITLE
    # =====================================================================
    txt(ax, W/2, H - 0.55, "ED — The Math Pipeline  (v6)",
        fontsize=30, bold=True, color=EDGE)
    txt(ax, W/2, H - 1.25,
        "from ED-05 axioms  →  unique PDE  →  Wilsonian RG flow  →  three effective PDEs  →  dictionary + predictions + invariants",
        fontsize=13, italic=True, color="#555")
    txt(ax, W/2, H - 1.80,
        "sixth-pass v6: adds RG spine (form-closure, β-functions, fixed-point catalog, flow invariants, ED window, UV/Intermediate/IR PDEs) + 0.6 dictionary resolution",
        fontsize=11, italic=True, color="#777")

    # =====================================================================
    # ROW 1 — ED-05 AXIOMS A1-A4  (full width)
    # =====================================================================
    y = H - 4.20
    bw, bh = W - 1.2, 1.85
    bx = 0.6
    box(ax, bx, y, bw, bh, face=AXIOM, edge=EDGE)
    txt(ax, bx + bw/2, y + bh - 0.28,
        "ED-05 — pre-PDE axioms (bare event domain)",
        fontsize=13, bold=True, color=EDGE)
    ax_lines = [
        ("A1", r"$\mathrm{ED}(A) \geq 0$", "non-negativity"),
        ("A2", r"$\mathrm{ED}(\emptyset) = 0$", "null baseline"),
        ("A3", r"$A \subseteq B \Rightarrow \mathrm{ED}(A) \leq \mathrm{ED}(B)$", "monotonicity"),
        ("A4", r"$\mathrm{ED}(A \cup B) \leq \mathrm{ED}(A) + \mathrm{ED}(B)$", "subadditivity"),
    ]
    cw = (bw - 0.4) / 4
    for i, (tag, eq, lab) in enumerate(ax_lines):
        xi = bx + 0.2 + i * cw
        cy = y + bh/2 - 0.1
        txt(ax, xi + 0.20, cy + 0.22, tag, fontsize=12, bold=True, ha="left", color=EDGE)
        txt(ax, xi + 0.20, cy - 0.15, eq, fontsize=12.5, ha="left")
        txt(ax, xi + 0.20, cy - 0.55, lab, fontsize=9.5, italic=True, color="#555", ha="left")
    y_axioms_bot = y

    # =====================================================================
    # ROW 2 — Seven Constraints
    # =====================================================================
    y = y_axioms_bot - 2.35
    bh2 = 2.05
    box(ax, bx, y, bw, bh2, face=CONSTRAINT, edge=CONSTRAINT_EDGE, lw=1.8)
    txt(ax, bx + bw/2, y + bh2 - 0.28,
        "Seven Constraints  —  the pre-architectural frame the PDE must live inside",
        fontsize=13, bold=True, color=CONSTRAINT_EDGE)
    for bpx in (bx + 0.12, bx + bw - 0.12):
        ax.plot([bpx, bpx], [y + 0.25, y + bh2 - 0.55],
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
    inner_x = bx + 0.40
    inner_w = bw - 0.80
    n = len(constraints)
    cellw = inner_w / n
    for i, (name, eq) in enumerate(constraints):
        xi = inner_x + i * cellw
        box(ax, xi + 0.06, y + 0.30, cellw - 0.12, bh2 - 1.00,
            face="#ffffff", edge=CONSTRAINT_EDGE, lw=1.1, pad=0.02, rounding=0.08)
        txt(ax, xi + cellw/2, y + bh2 - 0.78, name,
            fontsize=10.5, bold=True, color=CONSTRAINT_EDGE)
        txt(ax, xi + cellw/2, y + bh2 - 1.22, eq, fontsize=11.2)
        txt(ax, xi + 0.22, y + bh2 - 0.55, f"C{i+1}",
            fontsize=9, bold=True, color="#8a7ab6", ha="left")
    y_c_bot = y
    arrow(ax, bx + bw/2, y_axioms_bot - 0.02,
          bx + bw/2, y + bh2 + 0.02,
          color=EDGE_SOFT, label="counting is structured")

    # =====================================================================
    # ROW 3 — Compositional Rule
    # =====================================================================
    y = y_c_bot - 2.15
    bh3 = 1.75
    box(ax, bx, y, bw, bh3, face=AXIOM, edge=EDGE)
    txt(ax, bx + bw/2, y + bh3 - 0.28,
        "Compositional Rule  (cosmological specialisation of A4, shaped by the Seven Constraints)",
        fontsize=12.5, bold=True, color=EDGE)
    txt(ax, bx + bw/2, y + bh3/2 - 0.05,
        r"$p(A \cup B) = p(A) + p(B) "
        r"- \alpha\!\int_{A\cap B} p^\gamma d\mu "
        r"- \beta\!\int_{A\cup B} |\nabla p|^2 d\mu "
        r"- \gamma\!\int_{\partial(A\cup B)} h(|\nabla p|)\, dS$",
        fontsize=13)
    txt(ax, bx + bw/2, y + 0.28,
        "three correction terms  →  relational penalty  +  gradient penalty  +  boundary / horizon term",
        fontsize=9.8, italic=True, color="#555")
    y_cr_bot = y
    arrow(ax, bx + bw/2, y_c_bot - 0.02,
          bx + bw/2, y + bh3 + 0.02,
          color=CONSTRAINT_EDGE, label="filtered through the frame")

    # =====================================================================
    # ROW 4 — Canon P1-P7 + D.19 uniqueness
    # =====================================================================
    y = y_cr_bot - 3.25
    bh4 = 2.90
    box(ax, bx, y, bw, bh4, face=CANON, edge=EDGE)
    txt(ax, bx + bw/2, y + bh4 - 0.28,
        "Architectural Canon (00.2)  —  seven structural demands, each a forced consequence",
        fontsize=13, bold=True, color=EDGE)
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
         r"$(D-\zeta)^2 < 4(1-D);\; D_{\rm crit} \approx 0.896$ ($\zeta{=}1/4$)"),
        ("P7", "nonlinear triad",
         r"$M'(\rho)|\nabla\rho|^2$  generates  $k_3 = k_1 \pm k_2$"),
    ]
    cw4 = (bw - 0.4) / 4
    rowh = 1.33
    row_y_base = y + bh4 - 0.95
    for i, (tag, name, eq) in enumerate(pgrid):
        col = i % 4
        row = i // 4
        xi = bx + 0.2 + col * cw4
        yi = row_y_base - row * rowh
        txt(ax, xi, yi + 0.30, tag, fontsize=11.5, bold=True, ha="left", color=EDGE)
        txt(ax, xi + 0.48, yi + 0.30, name, fontsize=10.5, ha="left", color="black")
        txt(ax, xi + 0.05, yi - 0.08, eq, fontsize=11, ha="left")
    # D.19 slot
    xi = bx + 0.2 + 3 * cw4
    yi = row_y_base - 1 * rowh
    txt(ax, xi, yi + 0.30, "D.19", fontsize=11.5, bold=True, ha="left", color="#6b2e45")
    txt(ax, xi + 0.70, yi + 0.30, "uniqueness theorem",
        fontsize=10.5, ha="left", color="black", bold=True)
    txt(ax, xi + 0.05, yi - 0.04,
        "no freedom to choose —", fontsize=10, ha="left", color="#6b2e45")
    txt(ax, xi + 0.05, yi - 0.30,
        "the PDE is selected uniquely", fontsize=10, ha="left", color="#6b2e45")
    y_cn_bot = y
    arrow(ax, bx + bw/2, y_cr_bot - 0.02,
          bx + bw/2, y + bh4 + 0.02, color=EDGE_SOFT, label="structure")

    # =====================================================================
    # ROW 5 — Unified PDE
    # =====================================================================
    y = y_cn_bot - 2.80
    pdeh = 2.40
    pdew = bw - 2.0
    pdex = bx + 1.0
    box(ax, pdex, y, pdew, pdeh, face=PDE, edge=EDGE, pad=0.06)
    txt(ax, pdex + pdew/2, y + pdeh - 0.30,
        "THE UNIFIED PDE  —  one scalar density field + one participation ODE",
        fontsize=15, bold=True, color="white")
    txt(ax, pdex + pdew/2, y + pdeh - 0.95,
        r"$\partial_t \rho \;=\; D \cdot \left[\, M(\rho)\,\nabla^2\rho "
        r"+ M'(\rho)\,|\nabla\rho|^2 - P(\rho)\, \right] \;+\; H \cdot v$",
        fontsize=18, color="white")
    txt(ax, pdex + pdew/2, y + pdeh - 1.52,
        r"$\tau\,\dot{v} = \bar F(\rho) - \zeta\,v$",
        fontsize=14, color="#e3e8f0")
    txt(ax, pdex + pdew/4, y + 0.62,
        r"$M(\rho) = M_0(\rho_{\max}-\rho)^\beta$", fontsize=12, color="white")
    txt(ax, pdex + 3*pdew/4, y + 0.62,
        r"$P_{\rm SY2}(\rho) = \alpha\gamma \cdot "
        r"\dfrac{\rho - \rho^*}{\sqrt{(\rho-\rho^*)^2 + \rho_0^2}}$",
        fontsize=12, color="white")
    txt(ax, pdex + pdew/2, y + 0.22,
        r"working form  $\delta := \rho-\rho^*,\;$ Z$_2$:  "
        r"$F[\delta] = M_0 \nabla^2\delta + \frac{1}{2}M_2\delta^2\nabla^2\delta + "
        r"M_2\delta|\nabla\delta|^2 - P_0\delta - \frac{1}{6}P_3\delta^3 + \cdots$",
        fontsize=10.2, color="#e9edf5", italic=True)
    y_pde_bot = y
    arrow(ax, bx + bw/2, y_cn_bot - 0.02,
          pdex + pdew/2, y + pdeh + 0.02,
          color=EDGE, label="forced  (Theorem D.19)", lw=2.0)

    # =====================================================================
    # BRANCH SPLIT — three columns below the PDE
    # =====================================================================
    # Column geometry
    col_gap = 0.35
    total_col_w = W - 1.2
    col_w = (total_col_w - 2 * col_gap) / 3.0
    col_A_x = 0.6
    col_B_x = col_A_x + col_w + col_gap
    col_C_x = col_B_x + col_w + col_gap

    # Branch labels
    y_branch_label = y_pde_bot - 0.55
    for cx, lab, clr in [
        (col_A_x + col_w/2, "Branch A — channels, reductions, predictions  (v5 spine)", EDGE),
        (col_B_x + col_w/2, "Branch B — Wilsonian RG spine  (NEW in v6)", RG_EDGE),
        (col_C_x + col_w/2, "Branch C — dimensional dictionary + 0.6 resolution  (NEW in v6)", DICT_EDGE),
    ]:
        txt(ax, cx, y_branch_label, lab, fontsize=11.5, bold=True, color=clr)

    # Arrows PDE -> three branches
    arrow(ax, pdex + pdew/4, y_pde_bot - 0.02,
          col_A_x + col_w/2, y_branch_label + 0.30,
          color=EDGE_SOFT, label="turn each channel on alone", lw=1.4, labelpos=0.65)
    arrow(ax, pdex + pdew/2, y_pde_bot - 0.02,
          col_B_x + col_w/2, y_branch_label + 0.30,
          color=RG_EDGE, label="coarse-grain:  b, z=2", lw=2.0, labelpos=0.65)
    arrow(ax, pdex + 3*pdew/4, y_pde_bot - 0.02,
          col_C_x + col_w/2, y_branch_label + 0.30,
          color=DICT_EDGE, label="dimensional anchoring", lw=1.6, labelpos=0.65)

    # =====================================================================
    # BRANCH B — RG SPINE   (centre column, 10 rows)
    # =====================================================================
    yB = y_branch_label - 0.35
    # Row 6 — Coarse-graining map
    bhB = 2.05
    yB -= bhB
    box(ax, col_B_x, yB, col_w, bhB, face=RG_SPINE, edge=RG_EDGE)
    txt(ax, col_B_x + col_w/2, yB + bhB - 0.28,
        "Row 6 — Wilsonian coarse-graining map",
        fontsize=12, bold=True, color=RG_EDGE)
    txt(ax, col_B_x + 0.25, yB + bhB - 0.72,
        r"Shell:   keep $|k| < \Lambda/b$,   integrate out $\Lambda/b \leq |k| < \Lambda$", fontsize=10.2, ha="left")
    txt(ax, col_B_x + 0.25, yB + bhB - 1.08,
        r"Rescale: $x' = x/b,\; t' = t/b^{z},\; \delta' = b^{\chi}\delta_{<},\; v' = b^{\chi_v}v_{<}$",
        fontsize=10.2, ha="left")
    txt(ax, col_B_x + 0.25, yB + bhB - 1.45,
        r"$z = 2$   (dynamic exponent — diffusive / Model A)",
        fontsize=10.2, ha="left")
    txt(ax, col_B_x + 0.25, yB + bhB - 1.80,
        r"$\chi$ free;   $\chi_v = \chi$ forced by $P_0$ cross-coupling",
        fontsize=10.2, ha="left")
    y_row6_bot = yB

    # Row 7 — Form-closure theorem
    bhB = 2.05
    yB = y_row6_bot - 0.35
    yB -= bhB
    box(ax, col_B_x, yB, col_w, bhB, face=RG_ACCENT, edge=RG_EDGE, lw=2.0)
    txt(ax, col_B_x + col_w/2, yB + bhB - 0.28,
        "Row 7 — Form-closure theorem",
        fontsize=12, bold=True, color=RG_EDGE)
    txt(ax, col_B_x + col_w/2, yB + bhB - 0.80,
        "At tree level AND one loop, coarse-graining generates no operators outside",
        fontsize=10.2, italic=True, color="#333")
    txt(ax, col_B_x + col_w/2, yB + bhB - 1.22,
        r"$\{\; \nabla^2\delta,\;\; \delta,\;\; \delta^3,\;\; \delta^2\nabla^2\delta,\;\; "
        r"\delta|\nabla\delta|^2,\;\; v,\;\; \dot v,\;\; Hv \;\}$",
        fontsize=12)
    txt(ax, col_B_x + col_w/2, yB + bhB - 1.62,
        r"Div-form identity:  $\nabla\!\cdot\!(M(\delta)\nabla\delta) = M(\delta)\nabla^2\delta + M'(\delta)|\nabla\delta|^2$",
        fontsize=9.8, color="#333")
    txt(ax, col_B_x + col_w/2, yB + 0.22,
        "⇒  ED operator ansatz is a THEOREM, not a guess.",
        fontsize=10.5, bold=True, color=RG_EDGE)
    y_row7_bot = yB

    arrow(ax, col_B_x + col_w/2, y_row6_bot - 0.02,
          col_B_x + col_w/2, y_row7_bot + bhB + 0.02,
          color=RG_EDGE, lw=1.3)

    # Row 8 — Scaling dimensions table
    bhB = 3.30
    yB = y_row7_bot - 0.35 - bhB
    box(ax, col_B_x, yB, col_w, bhB, face=RG_SPINE, edge=RG_EDGE)
    txt(ax, col_B_x + col_w/2, yB + bhB - 0.28,
        "Row 8 — Tree-level scaling dimensions  (z = 2)",
        fontsize=12, bold=True, color=RG_EDGE)
    # table
    header_y = yB + bhB - 0.60
    tx0 = col_B_x + 0.35
    col_xs = [tx0, tx0 + 2.3, tx0 + 3.9, tx0 + 5.1]
    txt(ax, col_xs[0], header_y, "Operator", fontsize=10, bold=True, ha="left", color=RG_EDGE)
    txt(ax, col_xs[1], header_y, "Coupling", fontsize=10, bold=True, ha="left", color=RG_EDGE)
    txt(ax, col_xs[2], header_y, r"dim $\lambda$", fontsize=10, bold=True, ha="left", color=RG_EDGE)
    txt(ax, col_xs[3], header_y, "relevance", fontsize=10, bold=True, ha="left", color=RG_EDGE)
    ax.plot([col_B_x + 0.25, col_B_x + col_w - 0.25],
            [header_y - 0.14, header_y - 0.14], color=RG_EDGE, lw=0.8)
    rows_dim = [
        (r"$\nabla^2\delta$",  r"$M_0$", "0",       "marginal"),
        (r"$\delta$",          r"$P_0$", "+2",      "relevant"),
        (r"$\dot v$",          r"$\tau$","−2",      "irrelevant"),
        (r"$v$",               r"$\zeta$","+2",     "relevant"),
        (r"$\delta^3$",        r"$P_3$", r"$2-2\chi$", "rel ($\\chi{<}1$) / marg ($\\chi{=}1$)"),
        (r"$\delta^2\nabla^2\delta$", r"$M_2$", r"$-2\chi$", "marg ($\\chi{=}0$) / irr ($\\chi{>}0$)"),
        (r"$\delta|\nabla\delta|^2$", r"$M_2$", r"$-2\chi$", "tied to $\\delta^2\\nabla^2\\delta$"),
        (r"$\nabla^4\delta$",  "—",     "−2",      "irr; NOT generated"),
    ]
    for i, r in enumerate(rows_dim):
        ry = header_y - 0.38 - i * 0.30
        for cx, cell in zip(col_xs, r):
            txt(ax, cx, ry, cell, fontsize=9.5, ha="left")
    # chi choices
    txt(ax, col_B_x + col_w/2, yB + 0.28,
        r"Two canonical choices:  $\chi=0$ Gaussian  ($M_2$ marg, $P_3$ rel)  |  "
        r"$\chi=1$ Wilson-Fisher-like  ($P_3$ marg, $M_2$ irr)",
        fontsize=9.6, italic=True, color=RG_EDGE)
    y_row8_bot = yB
    arrow(ax, col_B_x + col_w/2, y_row7_bot - 0.02,
          col_B_x + col_w/2, yB + bhB + 0.02, color=RG_EDGE, lw=1.3)

    # Row 9 — β-functions
    bhB = 2.75
    yB = y_row8_bot - 0.35 - bhB
    box(ax, col_B_x, yB, col_w, bhB, face=RG_ACCENT, edge=RG_EDGE)
    txt(ax, col_B_x + col_w/2, yB + bhB - 0.28,
        "Row 9 — β-functions",
        fontsize=12, bold=True, color=RG_EDGE)
    beta_lines = [
        r"$\beta_{M_0} = 0$    (marginal — never flows)",
        r"$\beta_{P_0} = +2\,P_0$",
        r"$\beta_{\zeta}   = +2\,\zeta$",
        r"$\beta_{\tau}   = -2\,\tau$",
        r"$\beta_{P_3} = (2-2\chi)\,P_3$",
        r"$\beta_{M_2} = -2\chi\,M_2$",
    ]
    for i, s in enumerate(beta_lines):
        txt(ax, col_B_x + 0.4, yB + bhB - 0.68 - i*0.28, s,
            fontsize=10.5, ha="left")
    txt(ax, col_B_x + col_w/2, yB + 0.58,
        r"Integrated ($\ell = \ln b$):  $P_0,\zeta \sim e^{+2\ell}$,  $\tau \sim e^{-2\ell}$",
        fontsize=9.8, ha="center", color="#333")
    txt(ax, col_B_x + col_w/2, yB + 0.26,
        "⇒  at physical couplings  (P_0, ζ, τ) ≠ 0  →  ED is NOT a fixed point.",
        fontsize=10.3, bold=True, color=RG_EDGE)
    y_row9_bot = yB
    arrow(ax, col_B_x + col_w/2, y_row8_bot - 0.02,
          col_B_x + col_w/2, yB + bhB + 0.02, color=RG_EDGE, lw=1.3)

    # Row 10 — Fixed-point catalog (four sub-boxes)
    bhB = 3.70
    yB = y_row9_bot - 0.35 - bhB
    box(ax, col_B_x, yB, col_w, bhB, face=RG_SPINE, edge=RG_EDGE)
    txt(ax, col_B_x + col_w/2, yB + bhB - 0.28,
        "Row 10 — Fixed-point catalog",
        fontsize=12, bold=True, color=RG_EDGE)
    fps = [
        ("Gaussian  G", FP_G,
         r"$P_0=\zeta=P_3=M_2=0$",
         "UV-stable",
         "codim 3 (χ=0) / 2 (χ=1)"),
        (r"WF line ($\chi=1$)", FP_WF,
         r"$P_3$ free, $M_2=0$",
         "marginal φ⁴ line",
         "cubic marginal"),
        (r"NM line ($\chi=0$)", FP_NM,
         r"$M_2$ free, $P_3=0$",
         "marginal NM line",
         "nonlinear-mobility"),
        ("Point at ∞", FP_INF,
         r"$P_0,\zeta \to \infty;\; \tau \to 0$",
         "universal IR sink",
         "trivial mass phase (δ≡0)"),
    ]
    sub_w = (col_w - 0.7) / 4
    for i, (name, face, eq, desc, tail) in enumerate(fps):
        xi = col_B_x + 0.35 + i * (sub_w + 0.05)
        sub_y = yB + 0.55
        sub_h = bhB - 0.95
        box(ax, xi, sub_y, sub_w, sub_h, face=face, edge=FP_EDGE, lw=1.2)
        txt(ax, xi + sub_w/2, sub_y + sub_h - 0.28, name, fontsize=10.2, bold=True, color=FP_EDGE)
        txt(ax, xi + sub_w/2, sub_y + sub_h - 0.78, eq, fontsize=9.5)
        txt(ax, xi + sub_w/2, sub_y + sub_h - 1.22, desc, fontsize=9, italic=True, color="#333")
        txt(ax, xi + sub_w/2, sub_y + 0.35, tail, fontsize=8.8, italic=True, color="#555")
    txt(ax, col_B_x + col_w/2, yB + 0.24,
        r"Jacobian $J_{ij}=\partial\beta_i/\partial g_j$ diagonal at every FP.   "
        r"At G: eigenvalues $(2,2,-2,2-2\chi,-2\chi)$ for $(P_0,\zeta,\tau,P_3,M_2)$.",
        fontsize=9.6, italic=True, color=RG_EDGE)
    y_row10_bot = yB
    arrow(ax, col_B_x + col_w/2, y_row9_bot - 0.02,
          col_B_x + col_w/2, yB + bhB + 0.02, color=RG_EDGE, lw=1.3)

    # Row 11 — Flow invariants
    bhB = 2.05
    yB = y_row10_bot - 0.35 - bhB
    box(ax, col_B_x, yB, col_w, bhB, face=INV_BG, edge=INV_EDGE, lw=1.6)
    txt(ax, col_B_x + col_w/2, yB + bhB - 0.28,
        "Row 11 — Flow invariants (exactly RG-conserved on every trajectory)",
        fontsize=12, bold=True, color=INV_EDGE)
    inv_lines = [
        (r"$R_1 = P_0 / \zeta$",           "penalty-to-damping ratio"),
        (r"$R_2 = P_0 \cdot \tau$",        "relevant × irrelevant"),
        (r"$R_3 = \zeta \cdot \tau$",      "relevant × irrelevant"),
    ]
    for i, (eq, lab) in enumerate(inv_lines):
        txt(ax, col_B_x + 0.5, yB + bhB - 0.68 - i*0.32, eq,
            fontsize=11, ha="left")
        txt(ax, col_B_x + 2.5, yB + bhB - 0.68 - i*0.32, lab,
            fontsize=9.8, ha="left", italic=True, color="#555")
    txt(ax, col_B_x + col_w/2, yB + 0.30,
        r"χ-dep:  $\chi=0$: $P_3/P_0$ invariant, $M_2$ const.   $\chi=1$: $P_3$ constant.",
        fontsize=9.8, italic=True, color=INV_EDGE)
    y_row11_bot = yB
    arrow(ax, col_B_x + col_w/2, y_row10_bot - 0.02,
          col_B_x + col_w/2, yB + bhB + 0.02, color=RG_EDGE, lw=1.3)

    # Row 12 — Crossover scales / ED window
    bhB = 2.60
    yB = y_row11_bot - 0.35 - bhB
    box(ax, col_B_x, yB, col_w, bhB, face=RG_ACCENT, edge=RG_EDGE, lw=1.8)
    txt(ax, col_B_x + col_w/2, yB + bhB - 0.28,
        "Row 12 — Crossover scales :: the ED window",
        fontsize=12, bold=True, color=RG_EDGE)
    txt(ax, col_B_x + 0.5, yB + bhB - 0.70,
        r"$\ell_v  = \frac{1}{2}\ln(\xi_v \Lambda)$   participation-slaving onset",
        fontsize=10.2, ha="left")
    txt(ax, col_B_x + 0.5, yB + bhB - 1.02,
        r"$\ell_\xi = \ln(\xi \Lambda)$   gap scale   ($\xi = \sqrt{M_0/P_0}$)",
        fontsize=10.2, ha="left")
    # number-line
    ln_y = yB + 0.85
    ln_x0 = col_B_x + 0.5
    ln_x1 = col_B_x + col_w - 0.5
    ax.plot([ln_x0, ln_x1], [ln_y, ln_y], color=RG_EDGE, lw=2.0)
    lv_x = ln_x0 + (ln_x1 - ln_x0) * 0.33
    lx_x = ln_x0 + (ln_x1 - ln_x0) * 0.66
    for xt, lab in [(ln_x0, r"$\ell\to-\infty$"), (lv_x, r"$\ell_v$"),
                     (lx_x, r"$\ell_\xi$"), (ln_x1, r"$\ell\to+\infty$")]:
        ax.plot([xt, xt], [ln_y - 0.09, ln_y + 0.09], color=RG_EDGE, lw=1.5)
        txt(ax, xt, ln_y + 0.25, lab, fontsize=9.2, color=RG_EDGE)
    txt(ax, (ln_x0 + lv_x)/2, ln_y - 0.28, "UV  (v free, waves)", fontsize=9.2, italic=True, color="#333")
    txt(ax, (lv_x + lx_x)/2, ln_y - 0.28, "INTERMEDIATE  (ED window)", fontsize=9.5, bold=True, italic=True, color="#6b2e45")
    txt(ax, (lx_x + ln_x1)/2, ln_y - 0.28, "IR  (δ → 0)", fontsize=9.2, italic=True, color="#333")
    txt(ax, col_B_x + col_w/2, yB + 0.24,
        "ED-specific phenomenology lives ONLY in  ℓ_v < ℓ < ℓ_ξ.",
        fontsize=10.2, bold=True, color="#6b2e45")
    y_row12_bot = yB
    arrow(ax, col_B_x + col_w/2, y_row11_bot - 0.02,
          col_B_x + col_w/2, yB + bhB + 0.02, color=RG_EDGE, lw=1.3)

    # Row 13 — Participation limit rules
    bhB = 2.05
    yB = y_row12_bot - 0.35 - bhB
    box(ax, col_B_x, yB, col_w, bhB, face=RG_SPINE, edge=RG_EDGE)
    txt(ax, col_B_x + col_w/2, yB + bhB - 0.28,
        "Row 13 — Participation-channel limit rules",
        fontsize=12, bold=True, color=RG_EDGE)
    txt(ax, col_B_x + 0.5, yB + bhB - 0.68,
        r"IR slaving  ($\tau \to 0$):   $v = F[\delta]/\zeta$   (v-ODE disappears)",
        fontsize=10.2, ha="left")
    txt(ax, col_B_x + 0.5, yB + bhB - 1.00,
        r"$\quad$ + correction:  $-(\tau/\zeta^2)\,\partial_t F[\delta] + \mathcal{O}(\tau^2)$",
        fontsize=9.6, ha="left", color="#555")
    txt(ax, col_B_x + 0.5, yB + bhB - 1.35,
        r"UV freezing ($\tau \to \infty$):  $\dot v \to 0,\; v(t) = v_0 + \mathcal{O}(1/\tau)$   static",
        fontsize=10.2, ha="left")
    txt(ax, col_B_x + 0.5, yB + bhB - 1.67,
        r"Intermediate:  slaved, $\zeta$ finite   $\Rightarrow$   $\Gamma_{\rm eff} = D + H/\zeta$",
        fontsize=10.2, ha="left")
    txt(ax, col_B_x + col_w/2, yB + 0.22,
        r"Opposite limits of one ODE:  $\tau\dot v = F[\delta] - \zeta v$.",
        fontsize=9.8, italic=True, color=RG_EDGE)
    y_row13_bot = yB
    arrow(ax, col_B_x + col_w/2, y_row12_bot - 0.02,
          col_B_x + col_w/2, yB + bhB + 0.02, color=RG_EDGE, lw=1.3)

    # Row 14 — Three effective PDEs (three stacked sub-boxes)
    bhB = 6.80
    yB = y_row13_bot - 0.45 - bhB
    box(ax, col_B_x, yB, col_w, bhB, face=RG_SPINE, edge=RG_EDGE, lw=2.2)
    txt(ax, col_B_x + col_w/2, yB + bhB - 0.30,
        "Row 14 — Three effective PDEs  (one boxed equation per regime)",
        fontsize=13, bold=True, color=RG_EDGE)
    sub_h = (bhB - 0.70) / 3
    # UV sub-box
    sy = yB + 0.20 + 2 * sub_h
    box(ax, col_B_x + 0.30, sy, col_w - 0.60, sub_h,
        face=REG_UV, edge=EDGE)
    txt(ax, col_B_x + col_w/2, sy + sub_h - 0.25,
        r"UV   ($\ell < \ell_v$)  —  free two-channel diffusion",
        fontsize=11.2, bold=True, color=EDGE)
    txt(ax, col_B_x + col_w/2, sy + sub_h - 0.68,
        r"$\partial_t \delta = D\,M_0 \nabla^2\delta + H\,v,\qquad \tau\,\dot v = M_0\nabla^2\delta$",
        fontsize=12.5)
    txt(ax, col_B_x + col_w/2, sy + sub_h - 1.12,
        r"v frozen at $\tau\to\infty$;  long-$\lambda$ dispersion $\omega^2 \propto k^2$  (WAVE-LIKE).",
        fontsize=9.8, italic=True, color="#333")
    txt(ax, col_B_x + col_w/2, sy + 0.30,
        r"matches kinematic acoustic-metric / free-scalar QFT (ED-10).  Crossover $k_* = \sqrt{H/(\tau D M_0)}$.",
        fontsize=9.2, italic=True, color="#555")
    # INTERMEDIATE sub-box
    sy = yB + 0.20 + sub_h
    box(ax, col_B_x + 0.30, sy, col_w - 0.60, sub_h,
        face=REG_INT, edge="#6b2e45", lw=1.8)
    txt(ax, col_B_x + col_w/2, sy + sub_h - 0.25,
        r"INTERMEDIATE   ($\ell_v < \ell < \ell_\xi$)  —  the ED window",
        fontsize=11.2, bold=True, color="#6b2e45")
    txt(ax, col_B_x + col_w/2, sy + sub_h - 0.70,
        r"$\partial_t \delta = \Gamma_{\rm eff}\!\left[ M_0\nabla^2\delta "
        r"+ \frac{1}{2}M_2\delta^2\nabla^2\delta + M_2\delta|\nabla\delta|^2 "
        r"- P_0\delta - \frac{1}{6}P_3\delta^3 \right]$", fontsize=11.5)
    txt(ax, col_B_x + col_w/2, sy + sub_h - 1.20,
        r"$\Gamma_{\rm eff} = D + H/\zeta$    (participation slaved; Model A universality)",
        fontsize=10, italic=True, color="#333")
    txt(ax, col_B_x + col_w/2, sy + 0.30,
        "home of  UDM β=2,  Q-C transition,  C7 triad,  mobility capacity,  saturating penalty,  horizons,  ED-SC 2.0.",
        fontsize=9.2, italic=True, color="#6b2e45")
    # IR sub-box
    sy = yB + 0.20
    box(ax, col_B_x + 0.30, sy, col_w - 0.60, sub_h,
        face=REG_IR, edge=EDGE)
    txt(ax, col_B_x + col_w/2, sy + sub_h - 0.25,
        r"IR   ($\ell > \ell_\xi$)  —  linear gapped diffusion",
        fontsize=11.2, bold=True, color=EDGE)
    txt(ax, col_B_x + col_w/2, sy + sub_h - 0.68,
        r"$\partial_t \delta = D\,M_0 \nabla^2\delta - D\,P_0(\ell)\,\delta,\quad P_0(\ell)\to\infty$",
        fontsize=12)
    txt(ax, col_B_x + col_w/2, sy + sub_h - 1.08,
        r"$\equiv D\,M_0\,(\nabla^2 - m^2(\ell))\,\delta,\quad m^2 = P_0/M_0$",
        fontsize=10.5, color="#333")
    txt(ax, col_B_x + col_w/2, sy + sub_h - 1.48,
        r"$\delta(x,t) = e^{-D M_0 m^2 t}\!\left[e^{D M_0 t \nabla^2}\delta(x,0)\right]\;\Rightarrow\;\delta \to 0$ exponentially",
        fontsize=10, color="#333")
    txt(ax, col_B_x + col_w/2, sy + 0.28,
        "two-stage nonlinearity elimination:  (i) RG irrelevance  (ii) field-amplitude suppression  |δ|→0.",
        fontsize=9.2, italic=True, color="#555")
    y_row14_bot = yB
    arrow(ax, col_B_x + col_w/2, y_row13_bot - 0.02,
          col_B_x + col_w/2, yB + bhB + 0.02, color=RG_EDGE, lw=1.6,
          label="integrate β to ℓ = ℓ_v, ℓ_ξ", labelpos=0.5)

    # Row 15 — Operator on/off map
    bhB = 3.10
    yB = y_row14_bot - 0.35 - bhB
    box(ax, col_B_x, yB, col_w, bhB, face=RG_SPINE, edge=RG_EDGE)
    txt(ax, col_B_x + col_w/2, yB + bhB - 0.28,
        "Row 15 — Operator on/off map across regimes",
        fontsize=12, bold=True, color=RG_EDGE)
    header_y = yB + bhB - 0.62
    col_xs = [col_B_x + 0.35,
              col_B_x + 2.8,
              col_B_x + 4.2,
              col_B_x + col_w - 1.8]
    for cx, cell in zip(col_xs, ["Operator", "UV", "Intermediate", "IR"]):
        txt(ax, cx, header_y, cell, fontsize=10, bold=True, ha="left", color=RG_EDGE)
    ax.plot([col_B_x + 0.25, col_B_x + col_w - 0.25],
            [header_y - 0.14, header_y - 0.14], color=RG_EDGE, lw=0.8)
    onoff_rows = [
        (r"$M_0\nabla^2\delta$", "ON", r"ON  ($\Gamma_{\rm eff} M_0$)", r"ON  ($D M_0$)"),
        (r"$P_0\delta$",         "off", r"ON  ($-\Gamma_{\rm eff}P_0$)", "ON (dominant)"),
        (r"$\delta^2\nabla^2\delta,\,\delta|\nabla\delta|^2$", "off", "ON  (χ-dep.)", "off  (|δ|→0)"),
        (r"$P_3\delta^3$",       "off", "ON  (χ-dep.)", "off  (|δ|→0)"),
        (r"$Hv$  (independent)", "ON",  r"slaved $\to (H/\zeta)F[\delta]$", r"$\to 0$  ($\zeta\to\infty$)"),
        (r"$\tau\dot v$",        "ON (frozen)", "slaved (drops)", "slaved (drops)"),
    ]
    for i, r in enumerate(onoff_rows):
        ry = header_y - 0.35 - i * 0.33
        for cx, cell in zip(col_xs, r):
            txt(ax, cx, ry, cell, fontsize=9.3, ha="left")
    y_row15_bot = yB
    arrow(ax, col_B_x + col_w/2, y_row14_bot - 0.02,
          col_B_x + col_w/2, yB + bhB + 0.02, color=RG_EDGE, lw=1.3)

    # =====================================================================
    # BRANCH A — channels / reductions / predictions  (left column)
    # =====================================================================
    yA = y_branch_label - 0.35
    # Three channels
    bhA = 2.05
    yA -= bhA
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
    sub_h_A = (bhA - 0.10) if False else bhA
    # stack the three channels vertically — each in its own row
    ch_block_h = 2.10
    positions_A = []
    for i, (title, eq, note) in enumerate(channels):
        ry = y_branch_label - 0.55 - (i + 1) * ch_block_h
        box(ax, col_A_x + 0.20, ry, col_w - 0.40, ch_block_h - 0.25, face=CHANNEL)
        txt(ax, col_A_x + col_w/2, ry + (ch_block_h - 0.25) - 0.28, title,
            fontsize=11, bold=True)
        txt(ax, col_A_x + col_w/2, ry + (ch_block_h - 0.25)/2 + 0.05, eq, fontsize=12.5)
        txt(ax, col_A_x + col_w/2, ry + 0.22, note,
            fontsize=9, italic=True, color="#555")
        positions_A.append((ry + (ch_block_h - 0.25)/2, ry))
    last_ch_bot = positions_A[-1][1]

    # Three textbook reductions
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
    red_block_h = 2.10
    y_red_top = last_ch_bot - 0.50
    for i, (title, main, extra) in enumerate(reductions):
        ry = y_red_top - (i + 1) * red_block_h
        box(ax, col_A_x + 0.20, ry, col_w - 0.40, red_block_h - 0.25,
            face=REDUCTION, edge=EDGE_SOFT)
        txt(ax, col_A_x + col_w/2, ry + (red_block_h - 0.25) - 0.28, title,
            fontsize=11, bold=True)
        txt(ax, col_A_x + col_w/2, ry + (red_block_h - 0.25)/2 + 0.02, main, fontsize=12)
        txt(ax, col_A_x + col_w/2, ry + 0.28, extra, fontsize=10)
    last_red_bot = y_red_top - 3 * red_block_h

    # Three empirical modules
    predictions = [
        ("UDM", CONFIRMED,
         r"$D(c) = D_0\left(1 - c/c_{\max}\right)^\beta$",
         r"10 materials, 8 mechanisms, $R^2 > 0.986$",
         "CONFIRMED  —  one law, one exponent"),
        ("CLUSTER MERGER-LAG", CONFIRMED,
         r"$\ell = D_T / v_{\rm current}$",
         r"$D_T = 2.1\times 10^{27}\,\rm m^2/s$  (Mistele WL)",
         "CONFIRMED  —  7 clusters + Finner+25 aggregate of 58"),
        ("FRAP on BSA", PENDING,
         r"$\tau\,\ddot{\rho} + \zeta\,\dot{\rho} + \rho = 0$",
         "Creative Proteomics technician review",
         "PENDING  —  RLC-like recovery predicted"),
    ]
    pred_block_h = 2.20
    y_pred_top = last_red_bot - 0.50
    for i, (title, face, eq, mid, bottom) in enumerate(predictions):
        ry = y_pred_top - (i + 1) * pred_block_h
        box(ax, col_A_x + 0.20, ry, col_w - 0.40, pred_block_h - 0.25, face=face)
        h = pred_block_h - 0.25
        txt(ax, col_A_x + col_w/2, ry + h - 0.28, title,
            fontsize=11, bold=True)
        txt(ax, col_A_x + col_w/2, ry + h - 0.78, eq, fontsize=11.5)
        txt(ax, col_A_x + col_w/2, ry + h - 1.20, mid, fontsize=9.4, italic=True)
        status_color = "#2d6142" if face == CONFIRMED else "#8a6d18"
        txt(ax, col_A_x + col_w/2, ry + 0.28, bottom,
            fontsize=9.4, bold=True, color=status_color)
    last_pred_bot = y_pred_top - 3 * pred_block_h

    # =====================================================================
    # BRANCH C — dictionary + 0.6 resolution  (right column)
    # =====================================================================
    yC = y_branch_label - 0.35
    # Row D1 — dictionary
    bhC = 3.10
    yC -= bhC + 0.30
    box(ax, col_C_x, yC, col_w, bhC, face=DICT_BG, edge=DICT_EDGE, lw=1.8)
    txt(ax, col_C_x + col_w/2, yC + bhC - 0.28,
        "Row D1 — ED dimensional dictionary",
        fontsize=12, bold=True, color=DICT_EDGE)
    txt(ax, col_C_x + col_w/2, yC + bhC - 0.78,
        r"$T_0 \;=\; L_0^{\,2}\,D_{\rm nd}\,/\,D_{\rm phys}$", fontsize=14)
    txt(ax, col_C_x + 0.4, yC + bhC - 1.30,
        "Quantum anchors  (Madelung theorem):",
        fontsize=10, bold=True, ha="left", color=DICT_EDGE)
    anch = [
        (r"$L_0 = \hbar / (mc)$",        "reduced Compton wavelength"),
        (r"$D_{\rm phys} = \hbar/(2m)$",  "Madelung diffusion"),
        (r"$D_{\rm nd} = 0.3$",           "cross-regime nondimensional invariant"),
    ]
    for i, (eq, lab) in enumerate(anch):
        ry = yC + bhC - 1.60 - i * 0.30
        txt(ax, col_C_x + 0.5, ry, eq, fontsize=10.5, ha="left")
        txt(ax, col_C_x + 2.7, ry, lab, fontsize=9.5, ha="left", italic=True, color="#333")
    txt(ax, col_C_x + col_w/2, yC + 0.26,
        r"universal:  $D_{\rm phys}\cdot T_0 / L_0^{\,2} = 0.3$   (5 regimes, ≈ 61 OOM)",
        fontsize=10, bold=True, color=DICT_EDGE)
    y_D1_bot = yC

    # Row D2 — 0.6 resolution
    bhC = 4.20
    yC = y_D1_bot - 0.40 - bhC
    box(ax, col_C_x, yC, col_w, bhC, face="#f5e1e6", edge="#6b2e45", lw=1.8)
    txt(ax, col_C_x + col_w/2, yC + bhC - 0.28,
        "Row D2 — 0.6 resolution",
        fontsize=12, bold=True, color="#6b2e45")
    txt(ax, col_C_x + col_w/2, yC + bhC - 0.84,
        r"$T_0 \;=\; 2\,D_{\rm nd}\cdot\hbar/(mc^2) \;=\; 0.6\,\hbar/(mc^2)$",
        fontsize=13.5)
    txt(ax, col_C_x + col_w/2, yC + bhC - 1.30,
        r"⇒  ‘‘0.6’’ is fixed by  $D_{\rm nd}=0.3$  — not a free constant.",
        fontsize=10.5, bold=True, color="#6b2e45")
    txt(ax, col_C_x + col_w/2, yC + bhC - 1.80,
        r"Side identity:   $c_0/c \;=\; 1/(2 D_{\rm nd})$;   $c_0 = c$ at $D_{\rm nd}=1/2$.",
        fontsize=10, italic=True, color="#333")
    txt(ax, col_C_x + 0.4, yC + bhC - 2.25,
        "Five-route audit — only the algebraic dictionary passes:",
        fontsize=10, bold=True, ha="left", color="#6b2e45")
    audit_rows = [
        ("(1) damping discriminant  $D_{\\rm crit}$",          "FAIL"),
        ("(2) reversible-slice QFT dispersion",                  "FAIL"),
        ("(3) acoustic-metric curvature",                        "FAIL"),
        ("(4) PME coarse-graining coincidence",                  "FAIL"),
        ("(5) ζ-interpolation",                                  "FAIL"),
        ("(★) algebraic dictionary identity",                    "PASS ✓"),
    ]
    for i, (eq, tag) in enumerate(audit_rows):
        ry = yC + bhC - 2.55 - i * 0.28
        txt(ax, col_C_x + 0.5, ry, eq, fontsize=9.8, ha="left")
        clr = "#2d6142" if "PASS" in tag else "#8a2a2a"
        bld = "PASS" in tag
        txt(ax, col_C_x + col_w - 0.6, ry, tag, fontsize=9.8, ha="right",
            bold=bld, color=clr)
    y_D2_bot = yC

    # =====================================================================
    # Determine bottom of branches
    # =====================================================================
    y_branches_bot = min(last_pred_bot, y_row15_bot, y_D2_bot)

    # =====================================================================
    # ROW 16 — Cross-scale invariance restated (full width)
    # Anchored to fixed bottom so the canvas always has space for it.
    # =====================================================================
    bh17 = 4.30
    y17_bot = 0.60
    y17_top = y17_bot + bh17

    bh16 = 3.50
    gap_16_17 = 0.55
    y = y17_top + gap_16_17   # y is the bottom of row 16
    bw16 = W - 1.2
    box(ax, 0.6, y, bw16, bh16, face="#fff4e1", edge="#a67b2a", lw=2.0)
    txt(ax, 0.6 + bw16/2, y + bh16 - 0.28,
        "Cross-scale invariance restated  —  structural in form, approximate in couplings",
        fontsize=14, bold=True, color="#a67b2a")
    txt(ax, 0.6 + bw16/2, y + bh16 - 0.78,
        r"‘‘ED across 20–60 OOM’’  is NOT coupling-invariance.  Couplings flow per the β-functions.",
        fontsize=11, italic=True, color="#333")
    # two columns: what recurs / what is regime-specific
    colL_x = 1.2
    colR_x = 0.6 + bw16/2 + 0.3
    txt(ax, colL_x, y + bh16 - 1.30, "What recurs across scales:",
        fontsize=11, bold=True, ha="left", color="#a67b2a")
    recurs = [
        "operator structure of the canonical PDE (form-closure)",
        "triad  { mobility , penalty , participation }",
        "Model A universality inside the ED window",
        "ED-SC 2.0 motif-conditioned Hessian invariant  r* ≈ −1.304",
    ]
    for i, s in enumerate(recurs):
        txt(ax, colL_x + 0.3, y + bh16 - 1.60 - i * 0.28,
            "▸ " + s, fontsize=10, ha="left")
    txt(ax, colR_x, y + bh16 - 1.30, "What is regime-specific:",
        fontsize=11, bold=True, ha="left", color="#a67b2a")
    regime_sp = [
        r"window location  ($\ell_v,\,\ell_\xi$ values)",
        r"coupling values  ($P_0,\,\zeta,\,\tau,\,M_0,\ldots$)",
        "which empirical signatures activate (UDM / merger-lag / FRAP / …)",
        "trajectory label (R_1, R_2, R_3) of flow invariants",
    ]
    for i, s in enumerate(regime_sp):
        txt(ax, colR_x + 0.3, y + bh16 - 1.60 - i * 0.28,
            "▸ " + s, fontsize=10, ha="left")
    y_row16_bot = y

    # =====================================================================
    # ROW 17 — Structural forks ribbon (v5 + v6 extensions)
    # Fixed bottom anchor.
    # =====================================================================
    y = y17_bot
    box(ax, 0.6, y, bw16, bh17, face=FORK, edge="#6b2e45", lw=2.0)
    txt(ax, 0.6 + bw16/2, y + bh17 - 0.28,
        "…and these also fall out of the same equation, no additional assumptions",
        fontsize=13, bold=True, color="#6b2e45")
    forks_v5 = [
        ("dimensional invariant",
         r"$D \cdot T_0 / L_0^2 = 0.3$",
         "exact across 5 regimes (61 OOM)"),
        ("sharp bifurcation",
         r"$(D-\zeta)^2=4(1-D) \Rightarrow D_{\rm crit}\!\approx\!0.896$",
         r"ED-09.5 Q-C ($\zeta=1/4$)"),
        ("universal invariants",
         r"$E_g = \alpha\gamma\rho_0;\; t_{\rm rel}\approx\rho_0/(\alpha\gamma)$",
         "regime- and IC-independent"),
        ("triad coupling",
         r"$K = A_3/A_1^{\,3}\approx 0.0148$",
         r"$K_2 = A_2/A_1^{\,2}\approx 0.279;\;\varphi_3 - 3\varphi_1 = \pi$"),
        ("d-consistency",
         r"$\alpha_R = 1/(d(m-1)+2)$",
         "d = 1, 2, 3 verified exactly"),
        ("ED-SC 2.0",
         r"$r^* = {\rm med}\,\mathcal{R}_{\rm motif}(\nabla^2 E)\approx -1.304$",
         "Scenario D = Local Group = Casimir"),
    ]
    forks_v6 = [
        ("form closure (RG)",
         r"tree + 1-loop basis closed",
         "ED ansatz is a theorem"),
        ("flow invariants",
         r"$R_1 = P_0/\zeta,\; R_2 = P_0\tau,\; R_3 = \zeta\tau$",
         "foliate the RG flow"),
        ("fixed-point geometry",
         r"$G + {\rm WF}(\chi{=}1) + {\rm NM}(\chi{=}0) + \infty$",
         "diagonal Jacobian at each"),
        ("ED window",
         r"$\ell_v = \frac{1}{2}\ln(\xi_v\Lambda);\;\ell_\xi = \ln(\xi\Lambda)$",
         "domain of ED-specific physics"),
        ("IR endpoint",
         r"$\delta \to 0$   (trivial massive phase)",
         "linear gapped diffusion"),
        ("UV endpoint",
         r"Gaussian G,   $\omega^2 \propto k^2$",
         "wave-like, free-scalar-QFT regime"),
        ("χ-selection",
         r"$\chi{=}0$ marg. $M_2$ / $\chi{=}1$ marg. $P_3$",
         "picks which nonlinearity is marginal"),
        ("0.6 identity",
         r"$0.6 = 2\,D_{\rm nd}({\rm quantum})$",
         r"$c_0 = c/0.6$ fixed by $D_{\rm nd}=0.3$"),
    ]
    # Layout: row 1 — six v5 forks;  row 2 — eight v6 forks
    sub_label_y_1 = y + bh17 - 0.62
    txt(ax, 0.8, sub_label_y_1, "v5 (preserved):", fontsize=10, bold=True,
        color="#6b2e45", ha="left")
    n1 = len(forks_v5)
    cell_w1 = (bw16 - 0.8) / n1
    for i, (name, eq, note) in enumerate(forks_v5):
        xi = 0.6 + 0.4 + i * cell_w1
        txt(ax, xi + cell_w1/2, y + bh17 - 1.02, name,
            fontsize=9.6, bold=True, color="#6b2e45")
        txt(ax, xi + cell_w1/2, y + bh17 - 1.32, eq, fontsize=9.6)
        txt(ax, xi + cell_w1/2, y + bh17 - 1.60, note,
            fontsize=8.3, italic=True, color="#555")
    # separator
    ax.plot([0.8, 0.6 + bw16 - 0.2], [y + bh17 - 1.95, y + bh17 - 1.95],
            color="#6b2e45", lw=0.9, linestyle=":")
    txt(ax, 0.8, y + bh17 - 2.18, "v6 (new):", fontsize=10, bold=True,
        color="#6b2e45", ha="left")
    n2 = len(forks_v6)
    cell_w2 = (bw16 - 0.8) / n2
    for i, (name, eq, note) in enumerate(forks_v6):
        xi = 0.6 + 0.4 + i * cell_w2
        txt(ax, xi + cell_w2/2, y + bh17 - 2.55, name,
            fontsize=9.6, bold=True, color="#6b2e45")
        txt(ax, xi + cell_w2/2, y + bh17 - 2.88, eq, fontsize=9.3)
        txt(ax, xi + cell_w2/2, y + bh17 - 3.20, note,
            fontsize=8.1, italic=True, color="#555")

    # PDE -> forks dashed arrows
    arrow(ax, pdex + pdew * 0.15, y_pde_bot - 0.02,
          0.6 + bw16 * 0.10, y + bh17 + 0.02,
          color="#6b2e45", lw=1.1, ls="--",
          label="same equation", labelpos=0.80)
    arrow(ax, pdex + pdew * 0.85, y_pde_bot - 0.02,
          0.6 + bw16 * 0.90, y + bh17 + 0.02,
          color="#6b2e45", lw=1.1, ls="--")

    # =====================================================================
    # Branch label footers
    # =====================================================================
    # Save
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    fig.savefig(OUT, dpi=130, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"wrote {OUT}")
    return OUT


if __name__ == "__main__":
    build()
