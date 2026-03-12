import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch

# ---------- grid & parameters ----------
GRID = 100
R_CORE = 8.0
CORE_AMP = 0.9
CORE_BG  = 0.10
P_MAX    = 1.0

row_A, col_A = 50, 30
row_B, col_B = 60, 70   # b = 10 px vertical offset

ri, ci = np.ogrid[0:GRID, 0:GRID]

dA2 = (ri - row_A)**2 + (ci - col_A)**2
dB2 = (ri - row_B)**2 + (ci - col_B)**2

p = np.clip(
    CORE_BG * P_MAX
    + CORE_AMP * P_MAX * np.exp(-dA2 / (2.0 * R_CORE**2))
    + CORE_AMP * P_MAX * np.exp(-dB2 / (2.0 * R_CORE**2)),
    0.0, P_MAX
)

# ---------- figure ----------
fig, ax = plt.subplots(figsize=(7, 6))
im = ax.imshow(p, origin='upper', cmap='gray_r', vmin=0.0, vmax=1.0,
               extent=[0, GRID, GRID, 0])

# contours
levels = [0.20, 0.40, 0.60, 0.80]
ax.contour(np.arange(GRID), np.arange(GRID), p,
           levels=levels, colors='black', linewidths=0.8, alpha=0.6)

# ---------- velocity arrows ----------
arrow_kw = dict(arrowstyle='->', color='black',
                lw=2.0, mutation_scale=18)

# Core A: rightward  (col 30 -> 44, row 50)
ax.annotate('', xy=(44, 50), xytext=(30, 50),
            arrowprops=dict(arrowstyle='->', color='black', lw=2.0, mutation_scale=18))
ax.text(47, 50, r'$+v_0$', va='center', ha='left', fontsize=11, color='black')

# Core B: leftward  (col 70 -> 56, row 60)
ax.annotate('', xy=(56, 60), xytext=(70, 60),
            arrowprops=dict(arrowstyle='->', color='black', lw=2.0, mutation_scale=18))
ax.text(53, 60, r'$-v_0$', va='center', ha='right', fontsize=11, color='black')

# ---------- D0 annotation (horizontal, at row 36) ----------
ax.annotate('', xy=(col_B, 36), xytext=(col_A, 36),
            arrowprops=dict(arrowstyle='<->', color='dimgray', lw=1.5, mutation_scale=14))
ax.text((col_A + col_B) / 2, 33, r'$D_0 = 40\,\mathrm{px}$',
        ha='center', va='bottom', fontsize=10, color='dimgray')

# ---------- b annotation (vertical, at col 78) ----------
ax.annotate('', xy=(78, row_B), xytext=(78, row_A),
            arrowprops=dict(arrowstyle='<->', color='dimgray', lw=1.5, mutation_scale=14))
ax.text(80, (row_A + row_B) / 2, r'$b = 10\,\mathrm{px}$',
        ha='left', va='center', fontsize=10, color='dimgray')

# ---------- core labels ----------
ax.text(col_A, row_A - 11, 'Core A', ha='center', va='bottom',
        fontsize=12, fontweight='bold', color='black')
ax.text(col_B, row_B - 11, 'Core B', ha='center', va='bottom',
        fontsize=12, fontweight='bold', color='black')

# ---------- cosmetics ----------
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_linewidth(1.2)
    spine.set_color('black')

cbar = fig.colorbar(im, ax=ax, fraction=0.035, pad=0.03)
cbar.set_label(r'$\rho$ (normalised)', fontsize=10)
cbar.ax.tick_params(labelsize=9)

ax.set_title('Two-Core Kinematic Geometry', fontsize=14, fontweight='bold', pad=10)

fig.tight_layout()
out = r'C:\Users\allen\OneDrive\Desktop\two_core_kinematic_geometry.png'
fig.savefig(out, dpi=150, bbox_inches='tight')
print(f'SUCCESS: saved to {out}')
