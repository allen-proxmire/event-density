import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import FixedLocator, FixedFormatter

# ── Grid definition ───────────────────────────────────────────────────────────
b_over_R = np.array([0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75])
v_over_v0 = np.array([0.50, 0.75, 1.00, 1.25, 1.50])

NX = len(b_over_R)    # 7 columns
NY = len(v_over_v0)   # 5 rows

# ── Phase assignment: MERGE=0 for b/R <= 0.75, BIND=1 for b/R >= 1.00 ────────
# All rows identical (velocity has no effect in this regime)
row_pattern = np.where(b_over_R <= 0.75, 0.0, 1.0)   # 0=MERGE, 1=BIND
grid = np.tile(row_pattern, (NY, 1))                  # shape (NY, NX)

# ── Grayscale colormap: light gray = MERGE, dark gray = BIND ─────────────────
from matplotlib.colors import ListedColormap, BoundaryNorm
MERGE_GRAY = 0.82    # light
BIND_GRAY  = 0.28    # dark
cmap_2 = ListedColormap([
    [MERGE_GRAY, MERGE_GRAY, MERGE_GRAY],
    [BIND_GRAY,  BIND_GRAY,  BIND_GRAY ],
])
norm_2 = BoundaryNorm([0, 0.5, 1], ncolors=2)

# ── Figure ────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7.2, 4.8))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# pcolormesh gives cell-centred placement from edges
x_edges = np.append(b_over_R  - 0.125, b_over_R[-1]  + 0.125)
y_edges = np.append(v_over_v0 - 0.125, v_over_v0[-1] + 0.125)

mesh = ax.pcolormesh(x_edges, y_edges, grid,
                     cmap=cmap_2, norm=norm_2,
                     linewidth=0, rasterized=False)

# ── Phase boundary: vertical line between b/R = 0.75 and 1.00 ────────────────
boundary_x = 0.875   # midpoint of 0.75 and 1.00
ax.axvline(x=boundary_x, color='black', linewidth=2.0, linestyle='-', zorder=5)

# ── Cell text labels ──────────────────────────────────────────────────────────
for ix, bR in enumerate(b_over_R):
    for iy, vv in enumerate(v_over_v0):
        label = 'MERGE' if bR <= 0.75 else 'BIND'
        txt_color = 'black' if bR <= 0.75 else 'white'
        ax.text(bR, vv, label,
                ha='center', va='center',
                fontsize=9.5, fontweight='bold',
                color=txt_color, zorder=6)

# ── "Phase boundary" annotation ───────────────────────────────────────────────
ax.annotate('Phase\nboundary',
            xy=(boundary_x, v_over_v0[-1] + 0.12),
            xytext=(boundary_x + 0.22, v_over_v0[-1] + 0.12),
            ha='left', va='center', fontsize=9, color='black',
            arrowprops=dict(arrowstyle='->', color='black',
                            lw=1.3, mutation_scale=10),
            annotation_clip=False)

# ── "All rows identical" annotation (right side) ─────────────────────────────
# annotation_clip is not a valid kwarg for ax.text; omit it here
ax.text(b_over_R[-1] + 0.18, np.mean(v_over_v0),
        'all $v/v_0$ rows\nidentical',
        ha='left', va='center', fontsize=8.5, color='dimgray',
        style='italic',
        transform=ax.transData)

# ── Axis formatting ───────────────────────────────────────────────────────────
ax.set_xlim(x_edges[0], x_edges[-1])
ax.set_ylim(y_edges[0], y_edges[-1])

ax.set_xticks(b_over_R)
ax.set_xticklabels([f'{v:.2f}' for v in b_over_R], fontsize=10)
ax.set_yticks(v_over_v0)
ax.set_yticklabels([f'{v:.2f}' for v in v_over_v0], fontsize=10)

ax.set_xlabel(r'$b\,/\,R$', fontsize=13, labelpad=8)
ax.set_ylabel(r'$v\,/\,v_0$', fontsize=13, labelpad=8)

# No gridlines
ax.grid(False)

# Thin black border
for sp in ax.spines.values():
    sp.set_linewidth(1.2)
    sp.set_color('black')

# ── Legend patches ────────────────────────────────────────────────────────────
merge_patch = mpatches.Patch(
    facecolor=[MERGE_GRAY]*3, edgecolor='black', linewidth=0.8,
    label=r'MERGE  ($b/R \leq 0.75$)')
bind_patch  = mpatches.Patch(
    facecolor=[BIND_GRAY]*3,  edgecolor='black', linewidth=0.8,
    label=r'BIND   ($b/R \geq 1.00$)')
ax.legend(handles=[merge_patch, bind_patch],
          fontsize=9.5, loc='lower right',
          framealpha=0.92, edgecolor='lightgray',
          handlelength=1.6, borderpad=0.7)

# ── Title ─────────────────────────────────────────────────────────────────────
ax.set_title('MERGE / BIND  Phase Boundary',
             fontsize=14, fontweight='bold', pad=11)

# ── Caption ───────────────────────────────────────────────────────────────────
fig.text(0.50, 0.005,
         r'CoreType-QM1  |  $D_0 = 40\,\mathrm{px}$  |  '
         r'Shared-field ED + soft $\sigma$-partition  |  '
         r'Phase boundary at $b/R \approx 0.875$',
         ha='center', va='bottom', fontsize=7.8,
         color='dimgray', style='italic')

fig.tight_layout(rect=[0, 0.04, 0.88, 1.0])
out = r'C:\Users\allen\OneDrive\Desktop\merge_bind_phase_boundary.png'
fig.savefig(out, dpi=150, bbox_inches='tight')
print(f'SUCCESS: saved to {out}')
