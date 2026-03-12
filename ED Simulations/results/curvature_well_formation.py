import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

try:
    from scipy.ndimage import map_coordinates, gaussian_filter
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

GR, GC   = 80, 100
R_CORE   = 8.0
AMP      = 0.90
BG       = 0.10
SHIFT    = 0.1          # px / step
ROW_A0   = 50.0
ROW_B0   = 60.0         # b = 10 px
COL_A0   = 30.0
COL_B0   = 70.0
TAU_ROW  = 480.0        # row-coupling time constant

ri, ci = np.ogrid[0:GR, 0:GC]
EXT    = [0, GC, GR, 0]

def gauss(r0, c0, amp=AMP, R=R_CORE):
    return amp * np.exp(-((ri - r0)**2 + (ci - c0)**2) / (2.0 * R**2))

def laplacian_2d(p):
    '''Five-point discrete Laplacian.'''
    lap = np.zeros_like(p)
    lap[1:-1, 1:-1] = (p[:-2, 1:-1] + p[2:, 1:-1] +
                       p[1:-1, :-2] + p[1:-1, 2:] -
                       4.0 * p[1:-1, 1:-1])
    return lap

def bridge_boost(rA, cA, rB, cB):
    '''Shared-field coupling: mild density enhancement at the saddle.'''
    prox   = max(0.0, 1.0 - np.hypot(cB - cA, rB - rA) / 42.0)
    r_mid  = (rA + rB) / 2.0
    c_mid  = (cA + cB) / 2.0
    d2_mid = (ri - r_mid)**2 + (ci - c_mid)**2
    return 0.09 * prox * np.exp(-d2_mid / (2.0 * (R_CORE * 1.3)**2))

def make_field(t):
    cA     = COL_A0 + SHIFT * t
    cB     = COL_B0 - SHIFT * t
    rA     = ROW_A0
    rB     = ROW_A0 + (ROW_B0 - ROW_A0) * np.exp(-t / TAU_ROW)
    gA     = gauss(rA, cA)
    gB     = gauss(rB, cB)
    bridge = bridge_boost(rA, cA, rB, cB)
    p      = np.clip(BG + gA + gB + bridge, 0.0, 1.0)
    if HAS_SCIPY:
        p  = np.clip(gaussian_filter(p, sigma=0.4), 0.0, 1.0)
    lap    = laplacian_2d(p)
    return p, lap, (rA, cA), (rB, cB)

def sample_line(arr, r0, c0, r1, c1, n=150):
    '''Sample arr along a straight line from (r0,c0) to (r1,c1).'''
    rs = np.linspace(r0, r1, n)
    cs = np.linspace(c0, c1, n)
    if HAS_SCIPY:
        vals = map_coordinates(arr, [rs, cs], order=1, mode='nearest')
    else:
        # bilinear via nearest-integer fallback
        ri_i = np.clip(rs.astype(int), 0, GR - 1)
        ci_i = np.clip(cs.astype(int), 0, GC - 1)
        vals = arr[ri_i, ci_i]
    dist = np.linspace(0.0, np.hypot(c1 - c0, r1 - r0), n)
    return dist, vals

TIMES  = [18,   50,   70  ]
LABELS = ['Early', 'Mid', 'Late']
SUBS   = [r'$t = 18$', r'$t = 50$', r'$t = 70$']

fig = plt.figure(figsize=(14.5, 9.0))
gs  = gridspec.GridSpec(2, 3, figure=fig,
                        height_ratios=[2.2, 1.0],
                        hspace=0.38, wspace=0.10,
                        left=0.06, right=0.95, top=0.88, bottom=0.11)

LEVELS_P = [0.15, 0.30, 0.45, 0.60, 0.75, 0.90]
CMAP_P   = 'gray_r'
WELL_COL = 'steelblue'
last_im  = None

for idx, (t, lbl, sub) in enumerate(zip(TIMES, LABELS, SUBS)):

    p, lap, (rA, cA), (rB, cB) = make_field(t)

    r_mid = (rA + rB) / 2.0
    c_mid = (cA + cB) / 2.0
    D     = np.hypot(cB - cA, rB - rA)

    ax_top = fig.add_subplot(gs[0, idx])

    im = ax_top.imshow(p, cmap=CMAP_P, vmin=0.05, vmax=1.0,
                       origin='upper', extent=EXT, aspect='equal')
    last_im = im

    ax_top.contour(np.arange(GC), np.arange(GR), p,
                   levels=LEVELS_P, colors='black',
                   linewidths=0.85, alpha=0.68, zorder=4)

    d_to_mid = np.sqrt((ri - r_mid)**2 + (ci - c_mid)**2)
    well_mask = (lap > 5e-4) & (d_to_mid < R_CORE * 2.6) & (p > 0.13)
    well_rgba = np.zeros((GR, GC, 4), dtype=float)
    well_rgba[well_mask] = [0.27, 0.51, 0.71, 0.46]   # steelblue, semi-transparent
    ax_top.imshow(well_rgba, origin='upper', extent=EXT,
                  aspect='equal', zorder=5, interpolation='nearest')

    for cx, rx, lab in [(cA, rA, 'A'), (cB, rB, 'B')]:
        ax_top.plot(cx, rx, 'o', color='white', ms=6.5,
                    mec='black', mew=1.3, zorder=7)
        ax_top.text(cx, rx - 6, lab, ha='center', va='bottom',
                    fontsize=10, fontweight='bold', color='black', zorder=8)

    ax_top.annotate('curvature
well',
                    xy=(c_mid + 0.5, r_mid),
                    xytext=(c_mid + 16, r_mid - 10),
                    fontsize=8.5, color=WELL_COL, ha='left', va='bottom',
                    style='italic', zorder=9,
                    arrowprops=dict(arrowstyle='->', color=WELL_COL,
                                    lw=1.2, mutation_scale=10))

    ax_top.text(50, GR - 3, fr'$D = {D:.1f}$ px',
                ha='center', va='bottom', fontsize=9,
                color='dimgray', style='italic', zorder=9)

    ax_top.set_title(f'{lbl}   {sub}',
                     fontsize=12.5, fontweight='bold', pad=7)
    ax_top.set_xticks([]); ax_top.set_yticks([])
    for sp in ax_top.spines.values():
        sp.set_linewidth(1.2); sp.set_color('black')

    ax_bot = fig.add_subplot(gs[1, idx])

    dist, p_line   = sample_line(p,   rA, cA, rB, cB)
    _,    lap_line = sample_line(lap, rA, cA, rB, cB)

    ax_bot.plot(dist, p_line, '-', color='black', lw=2.0, zorder=5)

    ax_bot.fill_between(dist, p_line,
                         where=(lap_line > 0),
                         color=WELL_COL, alpha=0.30, zorder=4)

    mid_i = len(dist) // 2
    ax_bot.plot(dist[mid_i], p_line[mid_i], 'o',
                color=WELL_COL, ms=7, mec='black', mew=0.9, zorder=6)
    ax_bot.axhline(p_line[mid_i], ls=':', lw=1.0,
                   color=WELL_COL, alpha=0.65, zorder=3)

    ax_bot.text(dist[mid_i] + 0.5, p_line[mid_i] + 0.025,
                fr'$\rho_s={p_line[mid_i]:.3f}$',
                fontsize=8, color=WELL_COL, ha='left', va='bottom')

    ax_bot.set_xlim(0, dist[-1])
    ax_bot.set_ylim(0.07, 1.05)
    ax_bot.set_xlabel(r'$s$  (px, A$\rightarrow$B)', fontsize=9.5)
    if idx == 0:
        ax_bot.set_ylabel(r'$\rho$', fontsize=12)
    ax_bot.grid(True, ls='--', lw=0.5, alpha=0.35, color='gray')
    ax_bot.tick_params(labelsize=8.5)

    ax_bot.plot(dist[0],  p_line[0],  '^', color='royalblue',
                ms=7, mec='black', mew=0.8, zorder=6)
    ax_bot.plot(dist[-1], p_line[-1], 'v', color='darkorange',
                ms=7, mec='black', mew=0.8, zorder=6)
    if idx == 0:
        ax_bot.text(dist[3],    p_line[5]  + 0.04, 'A', fontsize=8.5,
                    color='royalblue', fontweight='bold', ha='left')
        ax_bot.text(dist[-4],   p_line[-5] + 0.04, 'B', fontsize=8.5,
                    color='darkorange', fontweight='bold', ha='right')

cax  = fig.add_axes([0.957, 0.56, 0.013, 0.29])
cbar = fig.colorbar(last_im, cax=cax)
cbar.set_label(r'$\rho$ (norm.)', fontsize=9.5)
cbar.ax.tick_params(labelsize=8)

leg_elems = [
    Line2D([0],[0], color='black', lw=2.0,
           label=r'density  $\rho$  (A$\rightarrow$B profile)'),
    Patch(facecolor=WELL_COL, alpha=0.30,
          label=r'curvature well  ($\nabla^2\rho > 0$)'),
    Line2D([0],[0], marker='o', color=WELL_COL, ms=7, ls='none',
           mec='black', mew=0.9, label='saddle point  $\\rho_s$'),
    Patch(facecolor=WELL_COL, alpha=0.46, edgecolor='none',
          label='well region  (2-D overlay)'),
]
fig.legend(handles=leg_elems, loc='lower center', ncol=4,
           fontsize=9.2, framealpha=0.92, edgecolor='lightgray',
           bbox_to_anchor=(0.48, 0.005), handlelength=1.8)

fig.suptitle('Curvature Well Formation', fontsize=15, fontweight='bold', y=0.965)

fig.text(0.48, 0.475,
         r'Scenario H  |  Shared-field ED  |  CoreType-QM1  |  '
         r'$D_0 = 40\,\mathrm{px}$,  $b = 10\,\mathrm{px}$  |  '
         r'Blue shading: $\nabla^2\rho > 0$ in bridge corridor',
         ha='center', va='top', fontsize=8.2, color='dimgray', style='italic')

out = r'C:\Users\allen\OneDrive\Desktop\curvature_well_formation.png'
fig.savefig(out, dpi=150, bbox_inches='tight')
print(f'SUCCESS: saved to {out}')
