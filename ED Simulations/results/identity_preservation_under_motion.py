import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ── parameters ────────────────────────────────────────────────────────────────
GRID     = 100
R_CORE   = 8.0
AMP      = 0.9
BG       = 0.10
P_MAX    = 1.0
SHIFT    = 0.1        # px per step
ROW_A    = 50.0
ROW_B    = 60.0       # b = 10 px
COL_A0   = 30.0
COL_B0   = 70.0

ri, ci = np.ogrid[0:GRID, 0:GRID]

def field_at(t):
    cA = COL_A0 + SHIFT * t
    cB = COL_B0 - SHIFT * t
    dA2 = (ri - ROW_A)**2 + (ci - cA)**2
    dB2 = (ri - ROW_B)**2 + (ci - cB)**2
    p = np.clip(
        BG + AMP * np.exp(-dA2 / (2.0 * R_CORE**2))
           + AMP * np.exp(-dB2 / (2.0 * R_CORE**2)),
        0.0, P_MAX
    )
    return p, cA, cB

# ── time points ───────────────────────────────────────────────────────────────
steps   = [60,    200,   340]
titles  = ["Before", "Closest Approach", "After"]
subtitles = ["$t = 60$", "$t = 200$", "$t = 340$"]

# ── figure ────────────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(14, 5.2))
gs  = gridspec.GridSpec(1, 3, figure=fig, wspace=0.08, left=0.04, right=0.88,
                        top=0.84, bottom=0.12)

LEVELS   = [0.20, 0.40, 0.60, 0.80]
EXTENT   = [0, GRID, GRID, 0]

axes = []
ims  = []
for idx, (t, title, sub) in enumerate(zip(steps, titles, subtitles)):
    ax = fig.add_subplot(gs[0, idx])
    p, cA, cB = field_at(t)

    im = ax.imshow(p, cmap='gray_r', vmin=0.05, vmax=1.0,
                   origin='upper', extent=EXTENT, aspect='equal')
    ims.append(im)

    ax.contour(np.arange(GRID), np.arange(GRID), p,
               levels=LEVELS, colors='black', linewidths=0.8, alpha=0.65)

    # centroid dots
    ax.plot(cA, ROW_A, 'o', color='white', markersize=6,
            markeredgecolor='black', markeredgewidth=1.2, zorder=6)
    ax.plot(cB, ROW_B, 'o', color='white', markersize=6,
            markeredgecolor='black', markeredgewidth=1.2, zorder=6)

    # centroid labels
    ax.text(cA, ROW_A - 5.5, 'A', ha='center', va='bottom',
            fontsize=10, fontweight='bold', color='black', zorder=7)
    ax.text(cB, ROW_B - 5.5, 'B', ha='center', va='bottom',
            fontsize=10, fontweight='bold', color='black', zorder=7)

    # ── panel-specific annotations ─────────────────────────────────────────
    if idx == 0:
        # separation distance annotation
        sep = np.sqrt((cB - cA)**2 + (ROW_B - ROW_A)**2)
        mid_c = (cA + cB) / 2.0
        ax.annotate('', xy=(cB, 37), xytext=(cA, 37),
                    arrowprops=dict(arrowstyle='<->', color='dimgray',
                                    lw=1.4, mutation_scale=13))
        ax.text(mid_c, 34.0, f'D ≈ {sep:.1f} px',
                ha='center', va='bottom', fontsize=9, color='dimgray')

    if idx == 1:
        # vertical b-annotation between the two centroids (both at col≈50)
        x_ann = cA + 8.0   # slight right offset so arrow is visible
        ax.annotate('', xy=(x_ann, ROW_B), xytext=(x_ann, ROW_A),
                    arrowprops=dict(arrowstyle='<->', color='dimgray',
                                    lw=1.4, mutation_scale=13))
        ax.text(x_ann + 2.0, (ROW_A + ROW_B) / 2.0, 'b = 10 px',
                ha='left', va='center', fontsize=9, color='dimgray')
        # highlight that cores are distinct despite overlap region
        ax.text(50, 88, 'Two distinct peaks', ha='center', va='bottom',
                fontsize=8.5, color='dimgray', style='italic')

    if idx == 2:
        ax.text(50, 88, 'Cores intact', ha='center', va='bottom',
                fontsize=9, color='dimgray', style='italic')

    # panel title
    ax.set_title(f'{title}\n{sub}', fontsize=13, fontweight='bold', pad=6)

    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_linewidth(1.2)
        sp.set_color('black')

    axes.append(ax)

# ── shared colorbar ───────────────────────────────────────────────────────────
cax  = fig.add_axes([0.90, 0.14, 0.018, 0.68])
cbar = fig.colorbar(ims[0], cax=cax)
cbar.set_label(r'$\rho$ (normalised)', fontsize=10)
cbar.ax.tick_params(labelsize=8)

# ── figure title & caption ────────────────────────────────────────────────────
fig.suptitle('Identity Preservation Under Motion',
             fontsize=15, fontweight='bold', y=0.97)

fig.text(0.46, 0.02,
         r'CoreType-QM1  |  $D_0 = 40\,\mathrm{px}$  |  $b = 10\,\mathrm{px}$'
         r'  |  $v = \pm0.1\,\mathrm{px/step}$  |  Independent fields (no coupling)',
         ha='center', va='bottom', fontsize=8.5, color='dimgray', style='italic')

# ── save ──────────────────────────────────────────────────────────────────────
out = r'C:\Users\allen\OneDrive\Desktop\identity_preservation_under_motion.png'
fig.savefig(out, dpi=150, bbox_inches='tight')
print(f'SUCCESS: saved to {out}')
