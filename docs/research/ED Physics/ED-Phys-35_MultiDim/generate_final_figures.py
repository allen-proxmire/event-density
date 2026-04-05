"""
generate_final_figures.py
=========================
Phase 12: Generate the synthesis figure set for the final report.

Figures:
  1. Complexity dilution scaling (1D/2D/3D)
  2. R_grad stability across dimensions
  3. Morphology fractions (3D)
  4. Horizon threshold comparison (2D vs 3D)
  5. Dimensional comparison table (visual)
  6. Energy decay across dimensions
"""
import os, sys, json
import numpy as np
import warnings
warnings.filterwarnings('ignore')

_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _DIR)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(_DIR, "edsim2d", "output", "final_figures")
os.makedirs(OUT, exist_ok=True)

STYLE = {"dpi": 300, "font_title": 14, "font_label": 12, "font_tick": 10,
         "font_legend": 10, "line_lw": 2.0, "grid_alpha": 0.3, "grid_lw": 0.5}
ED = {"blue": "#2166ac", "red": "#b2182b", "green": "#1b7837",
      "purple": "#762a83", "orange": "#e08214", "gray": "#999999"}

def _ax(ax, xl, yl, t):
    ax.set_xlabel(xl, fontsize=STYLE["font_label"])
    ax.set_ylabel(yl, fontsize=STYLE["font_label"])
    ax.set_title(t, fontsize=STYLE["font_title"], fontweight="bold")
    ax.tick_params(labelsize=STYLE["font_tick"])
    ax.grid(True, alpha=STYLE["grid_alpha"], linewidth=STYLE["grid_lw"])

print("Generating final figures...")

# =====================================================================
# Fig 1: Complexity dilution scaling
# =====================================================================
fig1, ax1 = plt.subplots(figsize=(7, 5))
dims = [1, 2, 3]
C_obs = [2.147e-3, 1.022e-3, 3.640e-4]
C_pred = [2.147e-3, 2.147e-3/2, 2.147e-3/6]
ax1.semilogy(dims, C_obs, 'o-', color=ED["blue"], lw=STYLE["line_lw"], ms=10,
             label="Observed $C_{ED}^{(d)}$", zorder=5)
ax1.semilogy(dims, C_pred, 's--', color=ED["red"], lw=1.5, ms=8,
             label=r"Predicted $C_{ED}^{(1)} / d!$", zorder=4)
for d, co, cp in zip(dims, C_obs, C_pred):
    ax1.annotate(f"{co:.2e}", (d, co), textcoords="offset points",
                 xytext=(12, 5), fontsize=9)
ax1.set_xticks([1, 2, 3])
ax1.set_xticklabels(["1D", "2D", "3D"])
ax1.legend(fontsize=STYLE["font_legend"])
_ax(ax1, "Dimension $d$", "$C_{ED}$",
    "Law 1: Complexity Dilution $C^{(d)} = C^{(1)}/d!$")
fig1.tight_layout()
fig1.savefig(os.path.join(OUT, "fig1_complexity_dilution.png"),
             dpi=STYLE["dpi"], bbox_inches="tight")
plt.close(fig1)
print("  fig1_complexity_dilution.png")

# =====================================================================
# Fig 2: R_grad across dimensions
# =====================================================================
fig2, ax2 = plt.subplots(figsize=(7, 5))
dims_r = [1, 2, 3]
Rg = [0.72, 0.83, 0.88]
Rg_cv = [0.0, 0.17, 0.02]  # approximate CVs
ax2.bar(dims_r, Rg, width=0.5, color=[ED["blue"], ED["red"], ED["green"]],
        alpha=0.8, edgecolor='black', linewidth=0.5)
for d, r, cv in zip(dims_r, Rg, Rg_cv):
    ax2.text(d, r + 0.01, f"{r:.2f}\nCV={cv:.0%}", ha='center',
             fontsize=10, fontweight='bold')
ax2.set_xticks([1, 2, 3])
ax2.set_xticklabels(["1D", "2D", "3D"])
ax2.set_ylim(0, 1.05)
ax2.axhline(1.0, color='gray', ls='--', lw=0.5)
_ax(ax2, "Dimension $d$", "$R_{grad}$",
    "Law 2: Gradient Dissipation Dominance")
fig2.tight_layout()
fig2.savefig(os.path.join(OUT, "fig2_Rgrad_stability.png"),
             dpi=STYLE["dpi"], bbox_inches="tight")
plt.close(fig2)
print("  fig2_Rgrad_stability.png")

# =====================================================================
# Fig 3: 3D Morphology fractions
# =====================================================================
fig3, axes3 = plt.subplots(1, 2, figsize=(12, 5))

# Single-mode
fracs_sm = [0.575, 0.232, 0.193]
labels_m = ["Filament", "Sheet", "Blob"]
colors_m = [ED["red"], ED["blue"], ED["green"]]
axes3[0].pie(fracs_sm, labels=labels_m, colors=colors_m, autopct='%1.0f%%',
             startangle=90, textprops={'fontsize': 12})
axes3[0].set_title("(a) Single-mode IC", fontsize=STYLE["font_title"], fontweight="bold")

# Multi-mode
fracs_mm = [0.41, 0.49, 0.10]
axes3[1].pie(fracs_mm, labels=labels_m, colors=colors_m, autopct='%1.0f%%',
             startangle=90, textprops={'fontsize': 12})
axes3[1].set_title("(b) Multi-mode IC", fontsize=STYLE["font_title"], fontweight="bold")

fig3.suptitle("3D Morphological Hierarchy", fontsize=STYLE["font_title"] + 2,
              fontweight="bold", y=1.02)
fig3.tight_layout()
fig3.savefig(os.path.join(OUT, "fig3_morphology_3d.png"),
             dpi=STYLE["dpi"], bbox_inches="tight")
plt.close(fig3)
print("  fig3_morphology_3d.png")

# =====================================================================
# Fig 4: Horizon threshold comparison
# =====================================================================
fig4, ax4 = plt.subplots(figsize=(8, 5))
dims_h = ["2D\n(Nm=4, 16 modes)", "3D\n(Nm=2, 8 modes)"]
max_prox = [1.0, 0.23]
horizon_formed = [True, False]
bars = ax4.bar([0, 1], max_prox, width=0.5,
               color=[ED["red"], ED["green"]], alpha=0.8,
               edgecolor='black', linewidth=0.5)
ax4.axhline(0.5, color='gray', ls='--', lw=1, label="Horizon threshold")
for i, (mp, hf) in enumerate(zip(max_prox, horizon_formed)):
    label = "HORIZON" if hf else "No horizon"
    ax4.text(i, mp + 0.03, f"{mp:.2f}\n{label}", ha='center',
             fontsize=11, fontweight='bold')
ax4.set_xticks([0, 1])
ax4.set_xticklabels(dims_h, fontsize=11)
ax4.set_ylim(0, 1.3)
ax4.legend(fontsize=STYLE["font_legend"])
_ax(ax4, "", "Max horizon proximity", "Law 3: Horizon Threshold Elevation (A=0.03)")
fig4.tight_layout()
fig4.savefig(os.path.join(OUT, "fig4_horizon_threshold.png"),
             dpi=STYLE["dpi"], bbox_inches="tight")
plt.close(fig4)
print("  fig4_horizon_threshold.png")

# =====================================================================
# Fig 5: Cross-dimensional summary table as figure
# =====================================================================
fig5, ax5 = plt.subplots(figsize=(10, 6))
ax5.axis('off')
table_data = [
    ["Unique attractor", "Yes", "Yes", "Yes"],
    ["Energy monotone", "Yes", "Yes", "Yes"],
    ["$R_{grad}$", "0.72", "0.83", "0.88"],
    ["$C_{ED}/C_{1D}$", "1.00", "0.48", "0.17"],
    ["Predicted $1/d!$", "1.00", "0.50", "0.17"],
    ["Morphology", "—", "F=0.48", "F=0.58, S=0.23, B=0.19"],
    ["Horizon (A=0.03)", "No", "Yes (Nm=4)", "No (Nm=2)"],
    ["Euler $\\chi$ conserved", "—", "—", "Yes"],
    ["Most stable inv.", "$H$", "$F$, $R_g$", "$R_g$ (CV=2%)"],
]
col_labels = ["Property", "1D", "2D", "3D"]
tbl = ax5.table(cellText=table_data, colLabels=col_labels,
                cellLoc='center', loc='center',
                colColours=['#f0f0f0']*4)
tbl.auto_set_font_size(False)
tbl.set_fontsize(11)
tbl.scale(1.2, 1.6)
for (row, col), cell in tbl.get_celld().items():
    if row == 0:
        cell.set_text_props(fontweight='bold')
        cell.set_facecolor('#d0d0d0')
    if col == 0:
        cell.set_text_props(fontweight='bold')
ax5.set_title("Cross-Dimensional Summary", fontsize=STYLE["font_title"] + 2,
              fontweight="bold", pad=20)
fig5.tight_layout()
fig5.savefig(os.path.join(OUT, "fig5_summary_table.png"),
             dpi=STYLE["dpi"], bbox_inches="tight")
plt.close(fig5)
print("  fig5_summary_table.png")

# =====================================================================
# Fig 6: Sheet-filament oscillation (3D multi-mode)
# =====================================================================
fig6, ax6 = plt.subplots(figsize=(8, 5))
t_osc = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
F_osc = [0.378, 0.424, 0.461, 0.489, 0.468, 0.417, 0.399, 0.382, 0.386, 0.401, 0.407]
S_osc = [0.450, 0.378, 0.334, 0.296, 0.301, 0.353, 0.400, 0.442, 0.461, 0.476, 0.493]
B_osc = [0.172, 0.198, 0.205, 0.215, 0.231, 0.230, 0.201, 0.176, 0.153, 0.123, 0.100]

ax6.plot(t_osc, F_osc, 'o-', color=ED["red"], lw=STYLE["line_lw"], label="Filament")
ax6.plot(t_osc, S_osc, 's-', color=ED["blue"], lw=STYLE["line_lw"], label="Sheet")
ax6.plot(t_osc, B_osc, '^-', color=ED["green"], lw=STYLE["line_lw"], label="Blob")
ax6.axhline(0.4, color='gray', ls=':', lw=0.5)
ax6.legend(fontsize=STYLE["font_legend"])
_ax(ax6, "$t$", "Volume fraction",
    "Sheet-Filament Oscillation (3D, D=0.3, multi-mode)")
fig6.tight_layout()
fig6.savefig(os.path.join(OUT, "fig6_sheet_filament_oscillation.png"),
             dpi=STYLE["dpi"], bbox_inches="tight")
plt.close(fig6)
print("  fig6_sheet_filament_oscillation.png")

print(f"\nAll figures saved to: {OUT}")
