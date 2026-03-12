import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

try:
    from scipy.ndimage import gaussian_filter
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

GR, GC   = 80, 100
R_CORE   = 8.0;  AMP = 0.90;  BG = 0.10;  SHIFT = 0.1
ROW_A0   = 50.0; COL_A0 = 30.0
ROW_B0   = 60.0; COL_B0 = 70.0
TAU_ROW  = 480.0
MERGE_T  = 75

ri, ci = np.ogrid[0:GR, 0:GC]
EXT    = [0, GC, GR, 0]

def gauss(r0, c0, amp=AMP, R=R_CORE):
    return amp * np.exp(-((ri - r0)**2 + (ci - c0)**2) / (2.0 * R**2))

def core_pos(t):
    cA = COL_A0 + SHIFT * t
    cB = COL_B0 - SHIFT * t
    rA = ROW_A0
    rB = ROW_A0 + (ROW_B0 - ROW_A0) * np.exp(-t / TAU_ROW)
    return (rA, cA), (rB, cB)

def two_peak_field(t):
    (rA, cA), (rB, cB) = core_pos(t)
    p = np.clip(BG + gauss(rA, cA) + gauss(rB, cB), 0, 1)
    if HAS_SCIPY:
        p = np.clip(gaussian_filter(p, sigma=0.5), 0, 1)
    return p, (rA, cA), (rB, cB)

def merged_field():
    (rA, cA), (rB, cB) = core_pos(MERGE_T)
    r_m = (rA + rB) / 2.0
    c_m = (cA + cB) / 2.0 + SHIFT * 0.05 * 55
    R_merge   = R_CORE * 1.55
    amp_merge = min(AMP * 1.6, 1.0 - BG)
    p = np.clip(BG + gauss(r_m, c_m, amp=amp_merge, R=R_merge), 0, 1)
    if HAS_SCIPY:
        p = np.clip(gaussian_filter(p, sigma=1.0), 0, 1)
    return p, (r_m, c_m)

T1, T2 = 50, 75
p1, (rA1, cA1), (rB1, cB1) = two_peak_field(T1)
p2, (rA2, cA2), (rB2, cB2) = two_peak_field(T2)
p3, (rM, cM)               = merged_field()
D1 = np.hypot(cB1 - cA1, rB1 - rA1)
D2 = np.hypot(cB2 - cA2, rB2 - rA2)

fig, axes = plt.subplots(1, 3, figsize=(14.5, 5.4),
                         gridspec_kw=dict(wspace=0.07,
                                          left=0.04, right=0.93,
                                          top=0.82, bottom=0.10))
fig.patch.set_facecolor('white')

CMAP_P = 'gray_r'
LEVELS = [0.12, 0.25, 0.40, 0.55, 0.70, 0.85]
VN, VX = 0.05, 1.0

# ── Panel data ────────────────────────────────────────────────────────────────
panels = [
    dict(p=p1, title='Two Peaks Approaching',
         sub='t = %d' % T1,
         markers=[(cA1, rA1, 'A'), (cB1, rB1, 'B')],
         stage='approaching', D=D1),
    dict(p=p2, title='Combined Peak Forming',
         sub='t = %d' % T2,
         markers=[(cA2, rA2, 'A'), (cB2, rB2, 'B')],
         stage='forming', D=D2),
    dict(p=p3, title='Single Merged Peak',
         sub='t = %d  (post-merge)' % (T2 + 55),
         markers=[(cM, rM, 'M')],
         stage='merged', D=None),
]

for ax, panel in zip(axes, panels):
    p     = panel['p']
    stage = panel['stage']

    im = ax.imshow(p, cmap=CMAP_P, vmin=VN, vmax=VX,
                   origin='upper', extent=EXT, aspect='equal')

    ax.contour(np.arange(GC), np.arange(GR), p,
               levels=LEVELS, colors='black',
               linewidths=[0.7, 0.8, 0.9, 1.0, 1.1, 1.2],
               alpha=0.70, zorder=4)

    # centroid markers
    for (cx, rx, lab) in panel['markers']:
        ms = 9.0 if stage == 'merged' else 7.0
        ax.plot(cx, rx, 'o', color='white', ms=ms,
                mec='black', mew=1.4, zorder=7)
        ax.text(cx, rx - 7, lab, ha='center', va='bottom',
                fontsize=11, fontweight='bold', color='black', zorder=8)

    # ── stage annotations ─────────────────────────────────────────────────────
    if stage == 'approaching':
        ax.annotate('', xy=(cB1, 38), xytext=(cA1, 38),
                    arrowprops=dict(arrowstyle='<->', color='dimgray',
                                    lw=1.4, mutation_scale=12), zorder=6)
        ax.text((cA1+cB1)/2, 35.5,
                'D = %.1f px' % D1,
                ha='center', va='bottom', fontsize=9,
                color='dimgray', style='italic')
        ax.text(cA1, rA1 + 10, 'Core A', ha='center', fontsize=9,
                color='royalblue', style='italic')
        ax.text(cB1, rB1 + 10, 'Core B', ha='center', fontsize=9,
                color='darkorange', style='italic')

    elif stage == 'forming':
        rm = (rA2 + rB2) / 2.0
        cm = (cA2 + cB2) / 2.0
        ax.annotate('bridge\nforming',
                    xy=(cm, rm), xytext=(cm + 16, rm - 12),
                    fontsize=8.5, color='firebrick',
                    ha='left', va='bottom', style='italic', zorder=8,
                    arrowprops=dict(arrowstyle='->',
                                    color='firebrick',
                                    lw=1.2, mutation_scale=10))
        ax.annotate('', xy=(cB2, 38), xytext=(cA2, 38),
                    arrowprops=dict(arrowstyle='<->', color='dimgray',
                                    lw=1.4, mutation_scale=12), zorder=6)
        ax.text((cA2+cB2)/2, 35.5,
                'D = %.1f px' % D2,
                ha='center', va='bottom', fontsize=9,
                color='dimgray', style='italic')

    elif stage == 'merged':
        theta  = np.linspace(0, 2 * np.pi, 200)
        r_ring = R_CORE * 1.55
        ax.plot(cM + r_ring * np.cos(theta),
                rM + r_ring * np.sin(theta),
                '--', color='firebrick', lw=1.5, alpha=0.72, zorder=6)
        ax.annotate('single\nidentity',
                    xy=(cM + r_ring * 0.72, rM - r_ring * 0.72),
                    xytext=(cM + 18, rM - 16),
                    fontsize=8.5, color='firebrick',
                    ha='left', va='bottom', style='italic', zorder=8,
                    arrowprops=dict(arrowstyle='->',
                                    color='firebrick',
                                    lw=1.2, mutation_scale=10))

    ax.set_title('%s\n(%s)' % (panel['title'], panel['sub']),
                 fontsize=12, fontweight='bold', pad=7, linespacing=1.45)
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_linewidth(1.2); sp.set_color('black')

# ── colorbar ──────────────────────────────────────────────────────────────────
cax  = fig.add_axes([0.943, 0.13, 0.014, 0.67])
cbar = fig.colorbar(im, cax=cax)
cbar.set_label('rho (norm.)', fontsize=10)
cbar.ax.tick_params(labelsize=8.5)
cbar.set_ticks([0.1, 0.3, 0.5, 0.7, 0.9])

# ── stage labels ──────────────────────────────────────────────────────────────
for x, slbl, sc in zip([0.175, 0.495, 0.810],
                        ['DISTINCT', 'TRANSITION', 'MERGED'],
                        ['royalblue', 'goldenrod', 'firebrick']):
    fig.text(x, 0.022, slbl, ha='center', va='bottom',
             fontsize=10.5, fontweight='bold', color=sc)

# ── title & caption ───────────────────────────────────────────────────────────
fig.suptitle('Dynamic Identity Collapse', fontsize=15, fontweight='bold', y=0.97)
fig.text(0.47, 0.002,
         'Scenario H  |  Shared-field ED  |  CoreType-QM1  |  '
         'D0=40px, b=10px  |  MERGE at t=75',
         ha='center', va='bottom', fontsize=8.2, color='dimgray', style='italic')

out = r'C:\Users\allen\OneDrive\Desktop\dynamic_identity_collapse.png'
fig.savefig(out, dpi=150, bbox_inches='tight')
print('SUCCESS: saved to ' + out)
