"""
ED-Data-17: Expanded z0MGS Cross-Match.

Combines the 20 galaxies from ED-Data-16 with 5 additional galaxies
recovered via targeted VizieR cone searches, for a total of 25 SPARC
galaxies with uniform z0MGS (Leroy+ 2019) GALEX+WISE SFR.

All z0MGS values retrieved from VizieR (J/ApJS/244/24/table4) on 2026-03-31.
"""
import json, os, warnings
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
warnings.filterwarnings('ignore')

BASE = 'data/ED-Data-17-z0MGS-Names'
FIG = os.path.join(BASE, 'figures')
RES = os.path.join(BASE, 'results')

# ═══ All z0MGS-matched SPARC galaxies ═══
# (name, T, logMb, Vflat, Q, PGC, logMstar_z0MGS, logSFR_z0MGS, Dist_Mpc)
data = [
    # From ED-Data-16 (20 galaxies)
    ("NGC2903",  4, 10.72, 183, 1, 27077, 10.42,  0.32,  8.5),
    ("NGC7331",  3, 11.11, 244, 1, 69327, 11.00,  0.53, 14.7),
    ("NGC5055",  4, 10.71, 194, 1, 46153, 10.72,  0.28,  8.9),
    ("NGC891",   3, 10.71, 212, 1,  9031, 10.72,  0.32,  9.9),
    ("NGC2403",  6, 10.01, 132, 1, 21396,  9.57, -0.35,  3.2),
    ("NGC3198",  5, 10.44, 150, 1, 30197, 10.05,  0.01, 13.8),
    ("NGC925",   7,  9.93, 117, 1,  9332,  9.75, -0.17,  9.2),
    ("NGC3621",  7, 10.13, 148, 1, 34554,  9.91, -0.08,  6.6),
    ("NGC300",   7,  9.47,  97, 1,  3238,  9.29, -0.83,  2.1),
    ("NGC55",    9,  9.33,  86, 1,  1014,  9.39, -0.90,  2.1),
    ("NGC7793",  7,  9.43, 107, 1, 73049,  9.25, -0.60,  3.6),
    ("NGC7814",  2, 10.68, 231, 1,   218, 10.49, -0.97, 13.2),
    ("NGC3521",  4, 10.64, 206, 1, 33550, 10.83,  0.42, 11.2),
    ("NGC5907",  5, 10.93, 227, 1, 54470, 10.84,  0.34, 17.2),
    ("NGC5033",  5, 10.62, 195, 1, 45948, 10.75,  0.46, 18.5),
    ("NGC4559",  6, 10.04, 122, 1, 42002,  9.81, -0.18,  8.9),
    ("NGC3031",  2, 10.78, 224, 1, 28630, 10.68, -0.27,  3.7),
    ("NGC4214", 10,  8.97,  60, 1, 39225,  8.55, -0.91,  2.9),
    ("IC2574",   9,  9.00,  66, 1, 30819,  8.72, -1.04,  3.9),
    ("NGC2976",  5,  9.42,  83, 1, 28120,  9.09, -1.06,  3.6),
    # ED-Data-17 additions (5 galaxies from targeted cone searches)
    ("NGC3726",  5, 10.27, 162, 1, 35676, 10.30,  0.17, 17.1),
    ("NGC4013",  3, 10.34, 178, 1, 37691, 10.53, -0.18, 17.1),
    ("NGC2683",  3, 10.42, 194, 1, 24930, 10.33, -0.62,  7.7),
    ("NGC3877",  5, 10.12, 164, 1, 36699, 10.37,  0.03, 17.1),
    ("NGC3893",  5, 10.38, 175, 1, 36875, 10.15,  0.26, 17.1),
]

print("=" * 85)
print("  ED-Data-17: Expanded z0MGS Cross-Match (25 galaxies)")
print("=" * 85)

names = [g[0] for g in data]
T_type = np.array([g[1] for g in data], dtype=float)
logMb = np.array([g[2] for g in data])
Vflat = np.array([g[3] for g in data], dtype=float)
logMstar = np.array([g[6] for g in data])
logSFR = np.array([g[7] for g in data])
logVf = np.log10(Vflat)
N = len(data)
logsSFR = logSFR - logMstar

print(f"  {N} SPARC galaxies with z0MGS SFR")

# ═══ BTFR ═══
res = stats.theilslopes(logMb, logVf)
B_fit, A_fit = res[0], res[1]
Delta = logMb - (A_fit + B_fit * logVf)
print(f"  BTFR slope = {B_fit:.3f}")

# ═══ CORRELATIONS ═══
r_s_sfr, p_s_sfr = stats.spearmanr(logSFR, Delta)
r_p_sfr, p_p_sfr = stats.pearsonr(logSFR, Delta)
r_s_ssfr, p_s_ssfr = stats.spearmanr(logsSFR, Delta)
tau_sfr, p_tau_sfr = stats.kendalltau(logSFR, Delta)

slope_fit, intercept_fit, _, _, _ = stats.linregress(logSFR, Delta)

rng = np.random.default_rng(42)
rho_boot = [stats.spearmanr(logSFR[rng.choice(N,N,True)], Delta[rng.choice(N,N,True)])[0]
            for _ in range(5000)]
ci = np.percentile(rho_boot, [2.5, 97.5])

idx_s = np.argsort(logSFR)
n3 = N // 3
D_lo = np.mean(Delta[idx_s[:n3]])
D_mi = np.mean(Delta[idx_s[n3:2*n3]])
D_hi = np.mean(Delta[idx_s[2*n3:]])
_, p_mw = stats.mannwhitneyu(Delta[idx_s[2*n3:]], Delta[idx_s[:n3]], alternative='greater')

sig = p_s_sfr < 0.05
direction = 'positive' if r_s_sfr > 0 else 'negative'

print(f"\n  Spearman rho(Delta, SFR)  = {r_s_sfr:+.4f} (p={p_s_sfr:.4f})")
print(f"  Pearson  r(Delta, SFR)   = {r_p_sfr:+.4f} (p={p_p_sfr:.4f})")
print(f"  Kendall  tau(Delta, SFR) = {tau_sfr:+.4f} (p={p_tau_sfr:.4f})")
print(f"  Spearman rho(Delta, sSFR)= {r_s_ssfr:+.4f} (p={p_s_ssfr:.4f})")
print(f"  Bootstrap CI: [{ci[0]:+.4f}, {ci[1]:+.4f}]")
print(f"  Tertiles: low={D_lo:+.4f} mid={D_mi:+.4f} high={D_hi:+.4f}")
print(f"  Mann-Whitney (high>low): p={p_mw:.4f}")

# ═══ FIGURES ═══
print("\n  Figures...")

fig, ax = plt.subplots(figsize=(9,7))
sc = ax.scatter(logVf, logMb, c=logSFR, cmap='RdYlBu_r', s=60, edgecolors='k', lw=0.5, zorder=5, vmin=-1.5, vmax=0.6)
vfl = np.linspace(logVf.min()-0.1, logVf.max()+0.1, 100)
ax.plot(vfl, A_fit+B_fit*vfl, 'k-', lw=2, label=f'BTFR slope={B_fit:.2f}')
plt.colorbar(sc, ax=ax, label='log SFR (z0MGS)')
ax.set_xlabel(r'$\log V_f$', fontsize=13); ax.set_ylabel(r'$\log M_b$', fontsize=13)
ax.set_title(f'BTFR with z0MGS SFR (n={N})', fontsize=14)
ax.legend(); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P1_BTFR.png'), dpi=150); plt.close()

fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(logSFR, Delta, c='C0', s=50, edgecolors='k', lw=0.4, zorder=5)
for i in range(N):
    ax.annotate(names[i].replace('NGC','N'), (logSFR[i], Delta[i]),
                fontsize=5, alpha=0.5, xytext=(3,3), textcoords='offset points')
xf = np.linspace(logSFR.min()-0.2, logSFR.max()+0.2, 100)
ax.plot(xf, slope_fit*xf+intercept_fit, 'k-', lw=2,
        label=rf'$\rho_s={r_s_sfr:+.3f}$, p={p_s_sfr:.3f}')
ax.axhline(0, color='gray', lw=0.5)
ax.set_xlabel('log SFR (z0MGS)', fontsize=13); ax.set_ylabel(r'$\Delta$', fontsize=13)
ax.set_title(f'BTFR Residual vs z0MGS SFR (n={N})', fontsize=13)
ax.legend(fontsize=11); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P2_Delta_SFR.png'), dpi=150); plt.close()

fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(logsSFR, Delta, c='C1', s=50, edgecolors='k', lw=0.4, zorder=5)
sl2, ic2, _, _, _ = stats.linregress(logsSFR, Delta)
xf2 = np.linspace(logsSFR.min()-0.2, logsSFR.max()+0.2, 100)
ax.plot(xf2, sl2*xf2+ic2, 'k-', lw=2, label=rf'$\rho_s={r_s_ssfr:+.3f}$, p={p_s_ssfr:.3f}')
ax.axhline(0, color='gray', lw=0.5)
ax.set_xlabel('log sSFR (z0MGS)', fontsize=13); ax.set_ylabel(r'$\Delta$', fontsize=13)
ax.set_title('BTFR Residual vs z0MGS sSFR', fontsize=13)
ax.legend(fontsize=11); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P3_Delta_sSFR.png'), dpi=150); plt.close()

fig, ax = plt.subplots(figsize=(8,5))
bins = np.linspace(-0.5, 0.5, 15)
ax.hist(Delta[idx_s[:n3]], bins=bins, alpha=0.5, color='C0', edgecolor='k',
        label=f'Low SFR ({D_lo:+.3f})')
ax.hist(Delta[idx_s[n3:2*n3]], bins=bins, alpha=0.5, color='C1', edgecolor='k',
        label=f'Mid SFR ({D_mi:+.3f})')
ax.hist(Delta[idx_s[2*n3:]], bins=bins, alpha=0.5, color='C3', edgecolor='k',
        label=f'High SFR ({D_hi:+.3f})')
ax.set_xlabel(r'$\Delta$'); ax.set_ylabel('Count')
ax.set_title('BTFR Residual by SFR Tertile'); ax.legend(fontsize=9); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P4_histogram.png'), dpi=150); plt.close()

fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(logMb, Delta, c=logSFR, cmap='RdYlBu_r', s=50, edgecolors='k', lw=0.4, vmin=-1.5, vmax=0.6)
ax.axhline(0, color='k', lw=0.5)
ax.set_xlabel(r'$\log M_b$'); ax.set_ylabel(r'$\Delta$')
ax.set_title('Residual vs Mass'); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P5_mass.png'), dpi=150); plt.close()
print("  Done")

# ═══ SAVE ═══
import csv
with open(os.path.join(RES, 'crossmatched_z0mgs_full.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Galaxy','T','logMb','Vflat','logVf','PGC','logMstar','logSFR','logsSFR','Dist','Delta'])
    for i in range(N):
        w.writerow([names[i], int(T_type[i]), round(logMb[i],3), int(Vflat[i]),
                    round(logVf[i],4), data[i][5], round(logMstar[i],2),
                    round(logSFR[i],2), round(logsSFR[i],3), data[i][8], round(Delta[i],4)])

if sig and direction == 'positive':
    verdict = 'CONSISTENT WITH ED'
elif not sig and direction == 'positive':
    verdict = 'SUGGESTIVE (positive, not yet significant)'
elif direction == 'negative' and sig:
    verdict = 'CONTRADICTS ED'
else:
    verdict = 'INCONCLUSIVE'

corr = {
    'spearman_rho_sfr': round(float(r_s_sfr),4), 'spearman_p_sfr': round(float(p_s_sfr),4),
    'pearson_r_sfr': round(float(r_p_sfr),4), 'pearson_p_sfr': round(float(p_p_sfr),4),
    'kendall_tau_sfr': round(float(tau_sfr),4), 'kendall_p_sfr': round(float(p_tau_sfr),4),
    'spearman_rho_ssfr': round(float(r_s_ssfr),4), 'spearman_p_ssfr': round(float(p_s_ssfr),4),
    'bootstrap_CI95': [round(float(ci[0]),4), round(float(ci[1]),4)],
    'tertile_low': round(float(D_lo),4), 'tertile_mid': round(float(D_mi),4),
    'tertile_high': round(float(D_hi),4),
    'mannwhitney_p': round(float(p_mw),4),
    'direction': direction, 'significant': bool(sig), 'n': N,
}
with open(os.path.join(RES, 'correlation_stats.json'), 'w') as f:
    json.dump(corr, f, indent=2)
with open(os.path.join(RES, 'btfr_fit.json'), 'w') as f:
    json.dump({'slope': round(float(B_fit),4), 'intercept': round(float(A_fit),4), 'n': N}, f, indent=2)

summary = {
    'experiment': 'ED-Data-17: Expanded z0MGS (25 galaxies)',
    'n_from_ED16': 20, 'n_new': 5, 'n_total': N,
    'data_source': 'z0MGS (Leroy+ 2019) via VizieR cone search',
    'btfr_slope': round(float(B_fit),3),
    'correlation': corr, 'verdict': verdict,
    'progression': {
        'ED-Data-12': {'n': 122, 'rho': 0.039, 'p': 0.667},
        'ED-Data-13': {'n': 116, 'rho': 0.263, 'p': 0.004},
        'ED-Data-14': {'n': 51, 'rho': 0.247, 'p': 0.081},
        'ED-Data-16': {'n': 20, 'rho': 0.356, 'p': 0.124},
        'ED-Data-17': {'n': N, 'rho': round(float(r_s_sfr),4), 'p': round(float(p_s_sfr),4)},
    },
}
with open(os.path.join(RES, 'final_summary.json'), 'w') as f:
    json.dump(summary, f, indent=2)

with open(os.path.join(RES, 'final_summary.md'), 'w') as f:
    f.write(f"""# ED-Data-17: Expanded z0MGS — Results

**{N} SPARC galaxies** with uniform z0MGS GALEX+WISE SFR.

## Primary: Delta vs log(SFR)
- Spearman rho = **{r_s_sfr:+.4f}** (p = {p_s_sfr:.4f})
- Pearson r = {r_p_sfr:+.4f} (p = {p_p_sfr:.4f})
- Kendall tau = {tau_sfr:+.4f} (p = {p_tau_sfr:.4f})
- Bootstrap CI: [{ci[0]:+.4f}, {ci[1]:+.4f}]

## Tertiles
| Tertile | n | Mean Delta |
|---------|---|------------|
| Low SFR | {n3} | {D_lo:+.4f} |
| Mid SFR | {n3} | {D_mi:+.4f} |
| High SFR | {N-2*n3} | {D_hi:+.4f} |
| Mann-Whitney | | p={p_mw:.4f} |

## Verdict: **{verdict}**

## Full Progression
| Module | Source | n | rho | p |
|--------|--------|---|-----|---|
| ED-Data-12 | T-type | 122 | +0.039 | 0.667 |
| ED-Data-13 | Calibrated | 116 | +0.263 | **0.004** |
| ED-Data-14 | Literature | 51 | +0.247 | 0.081 |
| ED-Data-16 | z0MGS | 20 | +0.356 | 0.124 |
| **ED-Data-17** | **z0MGS expanded** | **{N}** | **{r_s_sfr:+.3f}** | **{p_s_sfr:.3f}** |
""")

print(f"\n{'='*85}")
print(f"  ED-DATA-17 COMPLETE ({N} galaxies)")
print(f"{'='*85}")
print(f"  rho(SFR) = {r_s_sfr:+.4f}, p = {p_s_sfr:.4f}")
print(f"  Tertile MW: p = {p_mw:.4f}")
print(f"  VERDICT: {verdict}")
