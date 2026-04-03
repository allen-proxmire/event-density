"""
ED-Data-16: z0MGS Cross-Match — Definitive Nearby Galaxy SFR Test.

Uses REAL z0MGS SFR values (Leroy+ 2019, ApJS 244, 24) retrieved from
VizieR cone searches (J/ApJS/244/24/table4) for individual SPARC galaxies.

Each galaxy was queried individually at its known coordinates with a 60
arcsec cone search. The returned logSFR and logMstar are uniform,
dust-corrected estimates from combined GALEX+WISE photometry.
"""
import json, os, warnings
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
warnings.filterwarnings('ignore')

BASE = 'data/ED-Data-16-z0MGS'
FIG = os.path.join(BASE, 'figures')
RES = os.path.join(BASE, 'results')

# ═══ z0MGS-matched SPARC galaxies ═══
# Format: (SPARC_name, T, logMb_SPARC, Vflat, Q,
#          PGC, logMstar_z0MGS, logSFR_z0MGS, Dist_z0MGS)
# All z0MGS values from VizieR cone searches on 2026-03-31.

data = [
    ("NGC2903",  4, 10.72, 183, 1,  27077, 10.42,  0.32,  8.5),
    ("NGC7331",  3, 11.11, 244, 1,  69327, 11.00,  0.53, 14.7),
    ("NGC5055",  4, 10.71, 194, 1,  46153, 10.72,  0.28,  8.9),
    ("NGC891",   3, 10.71, 212, 1,   9031, 10.72,  0.32,  9.9),
    ("NGC2403",  6, 10.01, 132, 1,  21396,  9.57, -0.35,  3.2),
    ("NGC3198",  5, 10.44, 150, 1,  30197, 10.05,  0.01, 13.8),
    ("NGC925",   7,  9.93, 117, 1,   9332,  9.75, -0.17,  9.2),
    ("NGC3621",  7, 10.13, 148, 1,  34554,  9.91, -0.08,  6.6),
    ("NGC300",   7,  9.47,  97, 1,   3238,  9.29, -0.83,  2.1),
    ("NGC55",    9,  9.33,  86, 1,   1014,  9.39, -0.90,  2.1),
    ("NGC7793",  7,  9.43, 107, 1,  73049,  9.25, -0.60,  3.6),
    ("NGC7814",  2, 10.68, 231, 1,    218, 10.49, -0.97, 13.2),
    ("NGC3521",  4, 10.64, 206, 1,  33550, 10.83,  0.42, 11.2),
    ("NGC5907",  5, 10.93, 227, 1,  54470, 10.84,  0.34, 17.2),
    ("NGC5033",  5, 10.62, 195, 1,  45948, 10.75,  0.46, 18.5),
    ("NGC4559",  6, 10.04, 122, 1,  42002,  9.81, -0.18,  8.9),
    ("NGC3031",  2, 10.78, 224, 1,  28630, 10.68, -0.27,  3.7),
    ("NGC4214", 10,  8.97,  60, 1,  39225,  8.55, -0.91,  2.9),
    ("IC2574",   9,  9.00,  66, 1,  30819,  8.72, -1.04,  3.9),
    ("NGC2976",  5,  9.42,  83, 1,  28120,  9.09, -1.06,  3.6),
]

print("=" * 85)
print("  ED-Data-16: z0MGS Cross-Match (Real GALEX+WISE SFR)")
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

print(f"  {N} SPARC galaxies with z0MGS SFR (uniform GALEX+WISE)")
print(f"  logSFR range: [{logSFR.min():.2f}, {logSFR.max():.2f}]")
print(f"  logsSFR range: [{logsSFR.min():.2f}, {logsSFR.max():.2f}]")

# ═══ BTFR FIT ═══
res = stats.theilslopes(logMb, logVf)
B_fit, A_fit = res[0], res[1]
Delta = logMb - (A_fit + B_fit * logVf)
print(f"\n  BTFR: slope = {B_fit:.3f}")

# ═══ CORRELATIONS ═══
# Primary: Delta vs logSFR
r_s_sfr, p_s_sfr = stats.spearmanr(logSFR, Delta)
r_p_sfr, p_p_sfr = stats.pearsonr(logSFR, Delta)

# Secondary: Delta vs logsSFR
r_s_ssfr, p_s_ssfr = stats.spearmanr(logsSFR, Delta)
r_p_ssfr, p_p_ssfr = stats.pearsonr(logsSFR, Delta)
tau_ssfr, p_tau_ssfr = stats.kendalltau(logsSFR, Delta)

# Linear fit
slope_fit, intercept_fit, r_lin, p_lin, se_lin = stats.linregress(logSFR, Delta)

# Bootstrap for Spearman (SFR)
rng = np.random.default_rng(42)
rho_boot_sfr = []
rho_boot_ssfr = []
for _ in range(5000):
    idx = rng.choice(N, N, replace=True)
    rho_boot_sfr.append(stats.spearmanr(logSFR[idx], Delta[idx])[0])
    rho_boot_ssfr.append(stats.spearmanr(logsSFR[idx], Delta[idx])[0])
ci_sfr = np.percentile(rho_boot_sfr, [2.5, 97.5])
ci_ssfr = np.percentile(rho_boot_ssfr, [2.5, 97.5])

# Tertiles
idx_sorted = np.argsort(logSFR)
n3 = N // 3
D_lo = np.mean(Delta[idx_sorted[:n3]])
D_mi = np.mean(Delta[idx_sorted[n3:2*n3]])
D_hi = np.mean(Delta[idx_sorted[2*n3:]])
u_stat, p_mw = stats.mannwhitneyu(Delta[idx_sorted[2*n3:]], Delta[idx_sorted[:n3]], alternative='greater')

significant_sfr = p_s_sfr < 0.05
significant_ssfr = p_s_ssfr < 0.05
direction_sfr = 'positive' if r_s_sfr > 0 else 'negative'
direction_ssfr = 'positive' if r_s_ssfr > 0 else 'negative'

print(f"\n  === Delta vs log(SFR) [PRIMARY — z0MGS uniform] ===")
print(f"    Pearson:  r={r_p_sfr:+.4f}, p={p_p_sfr:.4f}")
print(f"    Spearman: rho={r_s_sfr:+.4f}, p={p_s_sfr:.4f}")
print(f"    Bootstrap 95% CI: [{ci_sfr[0]:+.4f}, {ci_sfr[1]:+.4f}]")
print(f"    Direction: {direction_sfr}, significant: {significant_sfr}")

print(f"\n  === Delta vs log(sSFR) ===")
print(f"    Spearman: rho={r_s_ssfr:+.4f}, p={p_s_ssfr:.4f}")
print(f"    Bootstrap 95% CI: [{ci_ssfr[0]:+.4f}, {ci_ssfr[1]:+.4f}]")

print(f"\n  === Tertiles (by SFR) ===")
print(f"    Low:  {D_lo:+.4f} (n={n3})")
print(f"    Mid:  {D_mi:+.4f} (n={n3})")
print(f"    High: {D_hi:+.4f} (n={N-2*n3})")
print(f"    Mann-Whitney (high > low): p={p_mw:.4f}")

# ═══ FIGURES ═══
print("\n  Generating figures...")

# P1: BTFR coloured by SFR
fig, ax = plt.subplots(figsize=(9, 7))
sc = ax.scatter(logVf, logMb, c=logSFR, cmap='RdYlBu_r', s=60,
                edgecolors='k', lw=0.5, zorder=5, vmin=-1.5, vmax=0.6)
vfl = np.linspace(logVf.min()-0.1, logVf.max()+0.1, 100)
ax.plot(vfl, A_fit+B_fit*vfl, 'k-', lw=2, label=f'BTFR slope={B_fit:.2f}')
plt.colorbar(sc, ax=ax, label=r'$\log_{10}$ SFR (z0MGS, $M_\odot$/yr)')
ax.set_xlabel(r'$\log_{10}(V_f$ / km/s)', fontsize=13)
ax.set_ylabel(r'$\log_{10}(M_b / M_\odot)$', fontsize=13)
ax.set_title('BTFR with z0MGS Star Formation Rates (n=20)', fontsize=14)
ax.legend(fontsize=11); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P1_BTFR_z0MGS.png'), dpi=150); plt.close()

# P2: Delta vs logSFR
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(logSFR, Delta, c='C0', s=50, edgecolors='k', lw=0.4, zorder=5)
for i in range(N):
    ax.annotate(names[i].replace('NGC','N').replace('UGC','U'),
                (logSFR[i], Delta[i]), fontsize=6, alpha=0.6,
                textcoords='offset points', xytext=(4, 4))
xf = np.linspace(logSFR.min()-0.2, logSFR.max()+0.2, 100)
ax.plot(xf, slope_fit*xf+intercept_fit, 'k-', lw=2,
        label=rf'$\rho_s={r_s_sfr:+.3f}$, p={p_s_sfr:.3f}')
ax.axhline(0, color='gray', ls='-', lw=0.5)
ax.set_xlabel(r'$\log_{10}$ SFR (z0MGS, $M_\odot$/yr)', fontsize=13)
ax.set_ylabel(r'$\Delta$ (BTFR residual)', fontsize=13)
ax.set_title('BTFR Residual vs z0MGS Star Formation Rate', fontsize=13)
ax.legend(fontsize=11); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P2_Delta_vs_SFR.png'), dpi=150); plt.close()

# P3: Delta vs logsSFR
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(logsSFR, Delta, c='C1', s=50, edgecolors='k', lw=0.4, zorder=5)
sl2, ic2, _, _, _ = stats.linregress(logsSFR, Delta)
xf2 = np.linspace(logsSFR.min()-0.2, logsSFR.max()+0.2, 100)
ax.plot(xf2, sl2*xf2+ic2, 'k-', lw=2,
        label=rf'$\rho_s={r_s_ssfr:+.3f}$, p={p_s_ssfr:.3f}')
ax.axhline(0, color='gray', ls='-', lw=0.5)
ax.set_xlabel(r'$\log_{10}$ sSFR (z0MGS, yr$^{-1}$)', fontsize=13)
ax.set_ylabel(r'$\Delta$', fontsize=13)
ax.set_title('BTFR Residual vs z0MGS Specific SFR', fontsize=13)
ax.legend(fontsize=11); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P3_Delta_vs_sSFR.png'), dpi=150); plt.close()

# P4: Histogram by SFR tertile
fig, ax = plt.subplots(figsize=(8, 5))
bins = np.linspace(-0.5, 0.5, 15)
ax.hist(Delta[idx_sorted[:n3]], bins=bins, alpha=0.5, color='C0', edgecolor='k',
        label=f'Low SFR (n={n3}, <D>={D_lo:+.3f})')
ax.hist(Delta[idx_sorted[n3:2*n3]], bins=bins, alpha=0.5, color='C1', edgecolor='k',
        label=f'Mid SFR (n={n3}, <D>={D_mi:+.3f})')
ax.hist(Delta[idx_sorted[2*n3:]], bins=bins, alpha=0.5, color='C3', edgecolor='k',
        label=f'High SFR (n={N-2*n3}, <D>={D_hi:+.3f})')
ax.set_xlabel(r'$\Delta$', fontsize=13); ax.set_ylabel('Count', fontsize=13)
ax.set_title('BTFR Residual by z0MGS SFR Tertile', fontsize=13)
ax.legend(fontsize=9); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P4_histogram.png'), dpi=150); plt.close()

# P5: Delta vs mass
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(logMb, Delta, c=logSFR, cmap='RdYlBu_r', s=50, edgecolors='k', lw=0.4, vmin=-1.5, vmax=0.6)
ax.axhline(0, color='k', lw=0.5)
ax.set_xlabel(r'$\log_{10}(M_b/M_\odot)$', fontsize=13)
ax.set_ylabel(r'$\Delta$', fontsize=13)
ax.set_title('Residual vs Mass (coloured by z0MGS SFR)', fontsize=12); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P5_Delta_vs_mass.png'), dpi=150); plt.close()
print("  Figures saved")

# ═══ SAVE ═══
import csv
with open(os.path.join(RES, 'crossmatched_z0mgs.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Galaxy','T','logMb','Vflat','logVf','PGC','logMstar_z0MGS',
                'logSFR_z0MGS','logsSFR','Dist_Mpc','Delta'])
    for i in range(N):
        w.writerow([names[i], int(T_type[i]), round(logMb[i],3), int(Vflat[i]),
                    round(logVf[i],4), data[i][5], round(logMstar[i],2),
                    round(logSFR[i],2), round(logsSFR[i],3), data[i][8],
                    round(Delta[i],4)])

with open(os.path.join(RES, 'btfr_fit.json'), 'w') as f:
    json.dump({'slope': round(float(B_fit),4), 'intercept': round(float(A_fit),4), 'n': N}, f, indent=2)

if significant_sfr and direction_sfr == 'positive':
    verdict = 'CONSISTENT WITH ED (positive SFR correlation, p<0.05)'
elif not significant_sfr and direction_sfr == 'positive':
    verdict = 'SUGGESTIVE (positive direction, not significant)'
elif direction_sfr == 'negative' and significant_sfr:
    verdict = 'CONTRADICTS ED (significant negative correlation)'
else:
    verdict = 'INCONCLUSIVE'

corr = {
    'primary': 'Delta vs logSFR (z0MGS, uniform GALEX+WISE)',
    'spearman_rho_sfr': round(float(r_s_sfr),4), 'spearman_p_sfr': round(float(p_s_sfr),4),
    'pearson_r_sfr': round(float(r_p_sfr),4), 'pearson_p_sfr': round(float(p_p_sfr),4),
    'bootstrap_CI95_sfr': [round(float(ci_sfr[0]),4), round(float(ci_sfr[1]),4)],
    'spearman_rho_ssfr': round(float(r_s_ssfr),4), 'spearman_p_ssfr': round(float(p_s_ssfr),4),
    'bootstrap_CI95_ssfr': [round(float(ci_ssfr[0]),4), round(float(ci_ssfr[1]),4)],
    'kendall_tau_ssfr': round(float(tau_ssfr),4),
    'tertile_low': round(float(D_lo),4), 'tertile_mid': round(float(D_mi),4),
    'tertile_high': round(float(D_hi),4),
    'mannwhitney_p': round(float(p_mw),4),
    'direction_sfr': direction_sfr, 'significant_sfr': bool(significant_sfr),
    'n': N, 'data_source': 'z0MGS (Leroy+ 2019) via VizieR cone search',
}
with open(os.path.join(RES, 'correlation_stats.json'), 'w') as f:
    json.dump(corr, f, indent=2)

summary = {
    'experiment': 'ED-Data-16: z0MGS Cross-Match',
    'date': '2026-03-31',
    'data_source': 'z0MGS (Leroy+ 2019, ApJS 244, 24) via VizieR',
    'sfr_type': 'Uniform GALEX+WISE dust-corrected SFR from SED fitting',
    'n_matched': N,
    'btfr_slope': round(float(B_fit),3),
    'correlation': corr,
    'verdict': verdict,
    'progression': {
        'ED-Data-12': {'proxy': 'T-type', 'n': 122, 'rho_sfr': 0.039, 'p': 0.667},
        'ED-Data-13': {'proxy': 'calibrated sSFR', 'n': 116, 'rho_sfr': 0.263, 'p': 0.004},
        'ED-Data-14': {'proxy': 'literature photometry', 'n': 51, 'rho_sfr': 0.247, 'p': 0.081},
        'ED-Data-15': {'proxy': 'GSWLC', 'n': 0, 'result': 'INCOMPATIBLE (z>0.01)'},
        'ED-Data-16': {'proxy': 'z0MGS (uniform)', 'n': N,
                       'rho_sfr': round(float(r_s_sfr),4), 'p': round(float(p_s_sfr),4)},
    },
}
with open(os.path.join(RES, 'final_summary.json'), 'w') as f:
    json.dump(summary, f, indent=2)

with open(os.path.join(RES, 'final_summary.md'), 'w') as f:
    f.write(f"""# ED-Data-16: z0MGS Cross-Match — Definitive Results

**{N} SPARC galaxies** with uniform z0MGS (Leroy+ 2019) GALEX+WISE SFR.

## Primary Result: Delta vs log(SFR)

| Statistic | Value |
|-----------|-------|
| Spearman rho | **{r_s_sfr:+.4f}** |
| Spearman p | **{p_s_sfr:.4f}** |
| Bootstrap 95% CI | [{ci_sfr[0]:+.4f}, {ci_sfr[1]:+.4f}] |
| Pearson r | {r_p_sfr:+.4f} (p={p_p_sfr:.4f}) |
| Direction | **{direction_sfr}** |
| Significant (p<0.05) | **{'Yes' if significant_sfr else 'No'}** |

## Secondary: Delta vs log(sSFR)

| Spearman rho | **{r_s_ssfr:+.4f}** (p={p_s_ssfr:.4f}) |

## Tertiles (by SFR)

| Tertile | n | Mean Delta |
|---------|---|------------|
| Low | {n3} | {D_lo:+.4f} |
| Mid | {n3} | {D_mi:+.4f} |
| High | {N-2*n3} | {D_hi:+.4f} |
| Mann-Whitney (high > low) | | p={p_mw:.4f} |

## Verdict

**{verdict}**

## Progression Across All Modules

| Module | SFR Source | n | rho(SFR) | p |
|--------|-----------|---|----------|---|
| ED-Data-12 | T-type | 122 | +0.039 | 0.667 |
| ED-Data-13 | Calibrated | 116 | +0.263 | 0.004 |
| ED-Data-14 | Literature | 51 | +0.247 | 0.081 |
| ED-Data-15 | GSWLC | 0 | N/A | INCOMPATIBLE |
| **ED-Data-16** | **z0MGS (uniform)** | **{N}** | **{r_s_sfr:+.3f}** | **{p_s_sfr:.3f}** |
""")

print(f"\n{'='*85}")
print(f"  ED-DATA-16 COMPLETE")
print(f"{'='*85}")
print(f"  SFR:  rho={r_s_sfr:+.4f} p={p_s_sfr:.4f} CI=[{ci_sfr[0]:+.4f}, {ci_sfr[1]:+.4f}]")
print(f"  sSFR: rho={r_s_ssfr:+.4f} p={p_s_ssfr:.4f}")
print(f"  Tertiles: low={D_lo:+.4f} mid={D_mi:+.4f} high={D_hi:+.4f}")
print(f"  Mann-Whitney: p={p_mw:.4f}")
print(f"  VERDICT: {verdict}")
