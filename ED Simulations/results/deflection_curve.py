import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ── Scenario I sweep data ─────────────────────────────────────────────────────
b_px    = np.array([  0,    5,   10,   15,   20,   25,   30 ], dtype=float)
b_over_R= np.array([0.00, 0.62, 1.25, 1.88, 2.50, 3.12, 3.75])
theta_A = np.array([0.00, 0.00, 0.00, 0.00, 0.43, 2.53, 90.00])
theta_B = np.array([0.00, 4.17, 6.89, 20.45, 16.69, 18.14, 9.48])
states  = ['MERGE','MERGE','MERGE','MERGE','MERGE','MERGE','BIND']

MERGE_mask = np.array([s == 'MERGE' for s in states])
BIND_mask  = ~MERGE_mask

# ── Figure ────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7.8, 5.2))
fig.patch.set_facecolor('white')
ax.set_facecolor('#fafafa')

# Lines
ax.plot(b_px, theta_A, '-o', color='royalblue',  lw=2.2, ms=7,
        mec='white', mew=1.2, label='Core A  (theta_A)', zorder=5)
ax.plot(b_px, theta_B, '-s', color='darkorange', lw=2.2, ms=7,
        mec='white', mew=1.2, label='Core B  (theta_B)', zorder=5)

# Mark BIND point distinctly
for th, col in [(theta_A[-1], 'royalblue'), (theta_B[-1], 'darkorange')]:
    ax.plot(b_px[-1], th, '*', color=col, ms=14,
            mec='black', mew=0.8, zorder=7)

# MERGE / BIND region shading
ax.axvspan(b_px[0]  - 1.5, 27.5, color='royalblue',  alpha=0.06, zorder=1)
ax.axvspan(27.5,             33,  color='firebrick',   alpha=0.08, zorder=1)

# Vertical boundary line
ax.axvline(x=27.5, color='dimgray', lw=1.2, ls='--', zorder=3)
ax.text(27.6, 82, 'MERGE | BIND', ha='left', va='top',
        fontsize=8.5, color='dimgray', style='italic')

# Annotate the b=30 BIND star
ax.annotate('BIND\n(theta_A = 90 deg)',
            xy=(30, 90), xytext=(24.5, 74),
            fontsize=8.5, color='firebrick', ha='right', va='top',
            style='italic',
            arrowprops=dict(arrowstyle='->', color='firebrick',
                            lw=1.1, mutation_scale=10))

# Annotate peak of theta_B at b=15
ax.annotate('peak deflection\n(theta_B = 20.5 deg)',
            xy=(15, 20.45), xytext=(17.5, 30),
            fontsize=8.5, color='darkorange', ha='left',
            style='italic',
            arrowprops=dict(arrowstyle='->', color='darkorange',
                            lw=1.1, mutation_scale=10))

# Data labels at each point
for bv, tA, tB in zip(b_px, theta_A, theta_B):
    if bv < 30:
        ax.text(bv, tA + 2.5, '%.1f' % tA, ha='center', va='bottom',
                fontsize=7.5, color='royalblue', alpha=0.85)
        ax.text(bv, tB + 2.5, '%.1f' % tB, ha='center', va='bottom',
                fontsize=7.5, color='darkorange', alpha=0.85)

# ── Axes ──────────────────────────────────────────────────────────────────────
ax.set_xlim(-2, 33)
ax.set_ylim(-4, 100)
ax.set_xticks(b_px)
ax.set_xticklabels(['%d' % int(b) for b in b_px], fontsize=10)
ax.set_yticks([0, 10, 20, 30, 45, 60, 90])
ax.set_yticklabels(['0', '10', '20', '30', '45', '60', '90'], fontsize=10)

ax.set_xlabel('Impact parameter  b  (px)', fontsize=12, labelpad=7)
ax.set_ylabel('Deflection angle  theta  (deg)', fontsize=12, labelpad=7)

# Secondary x-axis: b/R
ax2 = ax.twiny()
ax2.set_xlim(ax.get_xlim())
ax2.set_xticks(b_px)
ax2.set_xticklabels(['%.2f' % v for v in b_over_R], fontsize=8.5)
ax2.set_xlabel('b / R', fontsize=10, labelpad=5)

# Clean spines
ax.grid(True, ls='--', lw=0.5, alpha=0.35, color='gray')
for sp in ax.spines.values():
    sp.set_linewidth(1.0); sp.set_color('black')

ax.legend(fontsize=10, loc='upper left', framealpha=0.90,
          edgecolor='lightgray', handlelength=2.0)

# ── MERGE/BIND region text ────────────────────────────────────────────────────
ax.text(13, 93, 'MERGE', ha='center', va='top',
        fontsize=9, color='royalblue', fontweight='bold', alpha=0.55)
ax.text(30.5, 93, 'BIND', ha='center', va='top',
        fontsize=9, color='firebrick', fontweight='bold', alpha=0.65)

# ── Title & caption ───────────────────────────────────────────────────────────
ax.set_title('Deflection Curve  theta(b)', fontsize=14, fontweight='bold', pad=28)

fig.text(0.52, 0.005,
         'Scenario I  |  Shared-field ED  |  CoreType-QM1  |  '
         'D0=40px, v=+/-0.1px/step  |  R=8px',
         ha='center', va='bottom', fontsize=8, color='dimgray', style='italic')

fig.tight_layout(rect=[0, 0.03, 1, 1])
out = r'C:\Users\allen\OneDrive\Desktop\deflection_curve.png'
fig.savefig(out, dpi=150, bbox_inches='tight')
print('SUCCESS: saved to ' + out)
