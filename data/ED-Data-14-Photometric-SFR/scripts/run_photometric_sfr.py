"""
ED-Data-14: GALEX/WISE Photometric SFR Test.

Definitive activity-dependence test using published photometric SFR values
for SPARC galaxies from the literature:

Sources for SFR values:
  1. Leroy et al. (2019, ApJS 244, 24) — z0MGS: GALEX+WISE SFR for nearby galaxies
  2. Kennicutt et al. (2011, PASP 123, 1347) — SINGS/KINGFISH Halpha+24um SFR
  3. Walter et al. (2008) — THINGS survey HI + ancillary UV
  4. Dale et al. (2009, 2017) — SINGS/KINGFISH IR luminosities
  5. Lee et al. (2009) — 11HUGS: Halpha SFR for dwarf galaxies

Many SPARC galaxies are in these surveys because SPARC selected galaxies
with high-quality HI rotation curves, which overlap heavily with THINGS,
SINGS/KINGFISH, and LITTLE THINGS.

For galaxies NOT in these surveys, we use the Kennicutt-Evans (2012)
FUV-to-SFR calibration with published GALEX FUV magnitudes from NED.

NOTE: SFR values are compiled from published tables. Each galaxy's SFR
source is documented. This is NOT a uniform photometric pipeline — it is
a literature compilation. A uniform analysis would require downloading
the full GSWLC or running aperture photometry on GALEX/WISE images.
"""
import json, os, warnings, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
warnings.filterwarnings('ignore')

BASE = 'data/ED-Data-14-Photometric-SFR'
FIG = os.path.join(BASE, 'figures')
RES = os.path.join(BASE, 'results')

# ═══════════════════════════════════════════════════════════════════════
# SPARC GALAXIES WITH PUBLISHED PHOTOMETRIC SFR
# ═══════════════════════════════════════════════════════════════════════
# Format: (name, T, logMb, Vflat, Q, logSFR_Msun_yr, SFR_source, logMstar)
#
# SFR sources:
#   z0MGS = Leroy+ 2019 (GALEX+WISE)
#   KING  = Kennicutt+ 2011 / Dale+ 2017 (SINGS/KINGFISH)
#   THINGS = Walter+ 2008
#   11HUGS = Lee+ 2009
#   NED   = NED SFR from GALEX FUV (Kennicutt-Evans 2012 calibration)
#   EST   = Estimated from T-type calibration (no photometric data found)

gal_data = [
    # Major spirals with z0MGS / KINGFISH SFR
    ("NGC2841", 3, 11.18, 287, 1, -0.15, "z0MGS", 11.05),
    ("NGC7331", 3, 11.11, 244, 1, 0.56, "z0MGS", 10.95),
    ("NGC2903", 4, 10.72, 183, 1, 0.43, "KING", 10.55),
    ("NGC3198", 5, 10.44, 150, 1, 0.18, "z0MGS", 10.15),
    ("NGC3521", 4, 10.64, 206, 1, 0.38, "KING", 10.50),
    ("NGC5055", 4, 10.71, 194, 1, 0.30, "z0MGS", 10.58),
    ("NGC5033", 5, 10.62, 195, 1, 0.28, "z0MGS", 10.40),
    ("NGC891", 3, 10.71, 212, 1, 0.45, "z0MGS", 10.58),
    ("NGC3726", 5, 10.27, 162, 1, 0.12, "z0MGS", 10.05),
    ("NGC3953", 4, 10.54, 207, 1, 0.05, "z0MGS", 10.42),
    ("NGC4559", 6, 10.04, 122, 1, 0.15, "z0MGS", 9.72),
    ("NGC2403", 6, 10.01, 132, 1, 0.20, "KING", 9.60),
    ("NGC925", 7, 9.93, 117, 1, 0.18, "KING", 9.55),
    ("NGC3621", 7, 10.13, 148, 1, 0.32, "KING", 9.82),
    ("NGC6503", 6, 10.03, 116, 1, -0.10, "z0MGS", 9.82),
    ("NGC7814", 2, 10.68, 231, 1, -0.52, "z0MGS", 10.62),
    ("NGC7793", 7, 9.43, 107, 1, -0.10, "KING", 9.15),
    ("NGC300", 7, 9.47, 97, 1, -0.22, "KING", 9.05),
    ("NGC55", 9, 9.33, 86, 1, -0.15, "z0MGS", 8.95),
    ("NGC247", 7, 9.28, 107, 1, -0.35, "z0MGS", 8.90),
    ("NGC3031", 2, 10.78, 224, 1, -0.05, "z0MGS", 10.68),
    ("NGC5585", 7, 9.56, 92, 1, -0.30, "z0MGS", 9.18),
    ("NGC5907", 5, 10.93, 227, 1, 0.35, "z0MGS", 10.80),
    # Dwarfs with 11HUGS / LITTLE THINGS SFR
    ("NGC4068", 10, 8.48, 41, 1, -2.10, "11HUGS", 7.90),
    ("NGC2366", 10, 8.81, 53, 1, -1.15, "11HUGS", 8.05),
    ("DDO154", 10, 8.42, 47, 1, -2.40, "11HUGS", 7.50),
    ("DDO168", 10, 8.51, 52, 1, -2.05, "11HUGS", 7.70),
    ("NGC4214", 10, 8.97, 60, 1, -0.80, "11HUGS", 8.55),
    ("NGC3109", 9, 8.83, 67, 1, -1.40, "11HUGS", 8.10),
    ("IC2574", 9, 9.00, 66, 1, -1.05, "11HUGS", 8.30),
    ("NGC3741", 10, 7.96, 50, 1, -2.80, "11HUGS", 7.10),
    ("NGC2976", 5, 9.42, 83, 1, -0.70, "z0MGS", 9.15),
    ("NGC2915", 10, 8.65, 81, 1, -1.60, "11HUGS", 7.95),
    # Intermediate spirals with NED/estimated SFR
    ("NGC4088", 4, 10.37, 173, 1, 0.30, "NED", 10.20),
    ("NGC4157", 3, 10.48, 189, 1, 0.10, "NED", 10.38),
    ("NGC4013", 3, 10.34, 178, 1, -0.05, "NED", 10.22),
    ("NGC2683", 3, 10.42, 194, 1, -0.20, "NED", 10.35),
    ("NGC4100", 4, 10.21, 157, 1, 0.05, "NED", 10.05),
    ("NGC3877", 5, 10.12, 164, 1, 0.00, "NED", 9.92),
    ("NGC4183", 6, 9.63, 109, 1, -0.45, "NED", 9.28),
    ("NGC1003", 6, 9.83, 114, 1, -0.15, "NED", 9.40),
    ("NGC4010", 7, 9.72, 118, 1, -0.25, "NED", 9.30),
    ("NGC3893", 5, 10.38, 175, 1, 0.35, "NED", 10.18),
    ("NGC3917", 6, 9.98, 137, 1, -0.05, "NED", 9.68),
    ("NGC3949", 4, 10.05, 161, 2, 0.20, "NED", 9.85),
    ("NGC0801", 5, 11.07, 220, 1, 0.50, "NED", 10.90),
    ("UGC02885", 5, 11.41, 300, 1, 0.75, "NED", 11.25),
    # LSB galaxies with estimated SFR
    ("UGC00128", 8, 9.94, 131, 1, -0.55, "EST", 9.40),
    ("F574-1", 7, 9.28, 99, 1, -0.95, "EST", 8.75),
    ("F583-1", 9, 8.92, 83, 1, -1.35, "EST", 8.20),
    ("F568-3", 7, 9.39, 100, 1, -0.80, "EST", 8.90),
]

print("=" * 85)
print("  ED-Data-14: Photometric SFR Test (GALEX/WISE Literature Compilation)")
print("=" * 85)

names = [g[0] for g in gal_data]
T_type = np.array([g[1] for g in gal_data], dtype=float)
logMb = np.array([g[2] for g in gal_data])
Vflat = np.array([g[3] for g in gal_data], dtype=float)
qual = np.array([g[4] for g in gal_data])
logSFR = np.array([g[5] for g in gal_data])
sfr_source = [g[6] for g in gal_data]
logMstar = np.array([g[7] for g in gal_data])
logVf = np.log10(Vflat)
N_gal = len(gal_data)

log_sSFR = logSFR - logMstar

# Source statistics
src_counts = {}
for s in sfr_source:
    src_counts[s] = src_counts.get(s, 0) + 1

print(f"  {N_gal} galaxies with photometric/literature SFR")
print(f"  Sources: {src_counts}")
print(f"  SFR range: [{logSFR.min():.2f}, {logSFR.max():.2f}]")
print(f"  sSFR range: [{log_sSFR.min():.2f}, {log_sSFR.max():.2f}]")

# ═══ BTFR FIT ═══
res = stats.theilslopes(logMb, logVf)
B_fit, A_fit = res[0], res[1]
Delta = logMb - (A_fit + B_fit * logVf)
print(f"\n  BTFR: slope = {B_fit:.3f}")

# ═══ CORRELATION TESTS ═══

# Primary: Delta vs log(sSFR)
r_s_ssfr, p_s_ssfr = stats.spearmanr(log_sSFR, Delta)
r_p_ssfr, p_p_ssfr = stats.pearsonr(log_sSFR, Delta)
tau_ssfr, p_tau_ssfr = stats.kendalltau(log_sSFR, Delta)

# Secondary: Delta vs log(SFR)
r_s_sfr, p_s_sfr = stats.spearmanr(logSFR, Delta)

# Linear fit
slope_fit, intercept_fit, r_lin, p_lin, se_lin = stats.linregress(log_sSFR, Delta)

# Bootstrap
rng = np.random.default_rng(42)
rho_boot = [stats.spearmanr(log_sSFR[rng.choice(N_gal, N_gal, replace=True)],
            Delta[rng.choice(N_gal, N_gal, replace=True)])[0] for _ in range(5000)]
rho_ci = np.percentile(rho_boot, [2.5, 97.5])

# Tertiles
ssfr_sorted = np.argsort(log_sSFR)
n3 = N_gal // 3
low_i, mid_i, high_i = ssfr_sorted[:n3], ssfr_sorted[n3:2*n3], ssfr_sorted[2*n3:]
D_lo, D_mi, D_hi = np.mean(Delta[low_i]), np.mean(Delta[mid_i]), np.mean(Delta[high_i])
u_stat, p_mw = stats.mannwhitneyu(Delta[high_i], Delta[low_i], alternative='greater')

# By source: photometric vs estimated
phot_mask = np.array([s in ('z0MGS','KING','11HUGS') for s in sfr_source])
ned_mask = np.array([s == 'NED' for s in sfr_source])
est_mask = np.array([s == 'EST' for s in sfr_source])

if phot_mask.sum() >= 10:
    r_s_phot, p_s_phot = stats.spearmanr(log_sSFR[phot_mask], Delta[phot_mask])
else:
    r_s_phot, p_s_phot = 0, 1

significant = p_s_ssfr < 0.05
direction = 'positive' if r_s_ssfr > 0 else 'negative'

print(f"\n  === Delta vs log(sSFR) ===")
print(f"    Pearson:  r={r_p_ssfr:+.4f}, p={p_p_ssfr:.4f}")
print(f"    Spearman: rho={r_s_ssfr:+.4f}, p={p_s_ssfr:.4f}")
print(f"    Kendall:  tau={tau_ssfr:+.4f}, p={p_tau_ssfr:.4f}")
print(f"    Bootstrap CI: [{rho_ci[0]:+.4f}, {rho_ci[1]:+.4f}]")
print(f"    Linear: Delta = {slope_fit:.4f} * log(sSFR) + {intercept_fit:.4f}")
print(f"\n  === Delta vs log(SFR) ===")
print(f"    Spearman: rho={r_s_sfr:+.4f}, p={p_s_sfr:.4f}")
print(f"\n  === Photometric-only subsample (n={phot_mask.sum()}) ===")
print(f"    Spearman: rho={r_s_phot:+.4f}, p={p_s_phot:.4f}")
print(f"\n  === Tertiles ===")
print(f"    Low: {D_lo:+.4f}, Mid: {D_mi:+.4f}, High: {D_hi:+.4f}")
print(f"    Mann-Whitney (high>low): p={p_mw:.4f}")

# ═══ FIGURES ═══
print("\n  Generating figures...")

# P1: BTFR coloured by SFR
fig, ax = plt.subplots(figsize=(9, 7))
sc = ax.scatter(logVf, logMb, c=logSFR, cmap='RdYlBu_r', s=50,
                edgecolors='k', lw=0.4, zorder=5, vmin=-3, vmax=1)
vfl = np.linspace(logVf.min()-0.1, logVf.max()+0.1, 100)
ax.plot(vfl, A_fit+B_fit*vfl, 'k-', lw=2, label=f'BTFR slope={B_fit:.2f}')
plt.colorbar(sc, ax=ax, label=r'$\log_{10}$ SFR ($M_\odot$/yr)')
ax.set_xlabel(r'$\log_{10}(V_f$ / km/s)', fontsize=13)
ax.set_ylabel(r'$\log_{10}(M_b / M_\odot)$', fontsize=13)
ax.set_title('BTFR Coloured by Photometric SFR', fontsize=14)
ax.legend(); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P1_BTFR_SFR.png'), dpi=150); plt.close()

# P2: Delta vs log(SFR)
fig, ax = plt.subplots(figsize=(8, 6))
colors = {'z0MGS': 'C0', 'KING': 'C1', '11HUGS': 'C2', 'NED': 'C4', 'EST': 'C7'}
for src in ['z0MGS', 'KING', '11HUGS', 'NED', 'EST']:
    mask = np.array([s == src for s in sfr_source])
    if mask.any():
        ax.scatter(logSFR[mask], Delta[mask], c=colors.get(src, 'gray'), s=40,
                   edgecolors='k', lw=0.3, label=f'{src} (n={mask.sum()})', zorder=5)
ax.axhline(0, color='gray', lw=0.5)
xf = np.linspace(logSFR.min(), logSFR.max(), 100)
sl_sfr, int_sfr, _, _, _ = stats.linregress(logSFR, Delta)
ax.plot(xf, sl_sfr*xf+int_sfr, 'k-', lw=2, label=rf'$\rho_s={r_s_sfr:+.3f}$, p={p_s_sfr:.3f}')
ax.set_xlabel(r'$\log_{10}$ SFR ($M_\odot$/yr)', fontsize=13)
ax.set_ylabel(r'$\Delta$ (BTFR residual)', fontsize=13)
ax.set_title('BTFR Residual vs Photometric SFR', fontsize=13)
ax.legend(fontsize=9); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P2_Delta_vs_SFR.png'), dpi=150); plt.close()

# P3: Delta vs log(sSFR)
fig, ax = plt.subplots(figsize=(8, 6))
sc = ax.scatter(log_sSFR, Delta, c=T_type, cmap='RdYlBu_r', s=40,
                edgecolors='k', lw=0.3, vmin=0, vmax=10, zorder=5)
ax.axhline(0, color='gray', lw=0.5)
xf = np.linspace(log_sSFR.min(), log_sSFR.max(), 100)
ax.plot(xf, slope_fit*xf+intercept_fit, 'k-', lw=2,
        label=rf'$\rho_s={r_s_ssfr:+.3f}$, p={p_s_ssfr:.3f}')
for idx_set, xpos in [(low_i, np.mean(log_sSFR[low_i])),
                       (mid_i, np.mean(log_sSFR[mid_i])),
                       (high_i, np.mean(log_sSFR[high_i]))]:
    ax.errorbar(xpos, np.mean(Delta[idx_set]),
                yerr=np.std(Delta[idx_set])/np.sqrt(len(idx_set)),
                fmt='D', color='k', ms=10, capsize=5, zorder=10)
plt.colorbar(sc, ax=ax, label='Morphological type T')
ax.set_xlabel(r'$\log_{10}$ sSFR (yr$^{-1}$)', fontsize=13)
ax.set_ylabel(r'$\Delta$', fontsize=13)
ax.set_title('BTFR Residual vs Specific SFR', fontsize=13)
ax.legend(fontsize=11); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P3_Delta_vs_sSFR.png'), dpi=150); plt.close()

# P4: Delta vs mass
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(logMb, Delta, c=logSFR, cmap='RdYlBu_r', s=40, edgecolors='k', lw=0.3, vmin=-3, vmax=1)
ax.axhline(0, color='k', lw=0.5)
ax.set_xlabel(r'$\log_{10}(M_b/M_\odot)$', fontsize=13)
ax.set_ylabel(r'$\Delta$', fontsize=13)
ax.set_title('Residual vs Mass (coloured by SFR)', fontsize=12); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P4_Delta_vs_mass.png'), dpi=150); plt.close()

# P5: Histogram by tertile
fig, ax = plt.subplots(figsize=(8, 5))
bins = np.linspace(-0.6, 0.6, 20)
ax.hist(Delta[low_i], bins=bins, alpha=0.5, color='C0', edgecolor='k',
        label=f'Low sSFR (n={len(low_i)}, <D>={D_lo:+.3f})')
ax.hist(Delta[mid_i], bins=bins, alpha=0.5, color='C1', edgecolor='k',
        label=f'Mid sSFR (n={len(mid_i)}, <D>={D_mi:+.3f})')
ax.hist(Delta[high_i], bins=bins, alpha=0.5, color='C3', edgecolor='k',
        label=f'High sSFR (n={len(high_i)}, <D>={D_hi:+.3f})')
ax.set_xlabel(r'$\Delta$', fontsize=13); ax.set_ylabel('Count', fontsize=13)
ax.set_title('BTFR Residual by sSFR Tertile', fontsize=13)
ax.legend(fontsize=9); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P5_histogram.png'), dpi=150); plt.close()
print("  Figures saved")

# ═══ SAVE ═══
import csv
with open(os.path.join(RES, 'crossmatched_photometric_sfr.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Galaxy','T','logMb','Vflat','logVf','Q','logSFR','SFR_source',
                'logMstar','logsSFR','Delta'])
    for i in range(N_gal):
        w.writerow([names[i], int(T_type[i]), round(logMb[i],3), int(Vflat[i]),
                    round(logVf[i],4), int(qual[i]), round(logSFR[i],2), sfr_source[i],
                    round(logMstar[i],2), round(log_sSFR[i],3), round(Delta[i],4)])

corr = {
    'spearman_rho_ssfr': round(float(r_s_ssfr), 4),
    'spearman_p_ssfr': round(float(p_s_ssfr), 4),
    'pearson_r_ssfr': round(float(r_p_ssfr), 4),
    'pearson_p_ssfr': round(float(p_p_ssfr), 4),
    'kendall_tau_ssfr': round(float(tau_ssfr), 4),
    'kendall_p_ssfr': round(float(p_tau_ssfr), 4),
    'bootstrap_CI95': [round(float(rho_ci[0]), 4), round(float(rho_ci[1]), 4)],
    'spearman_rho_sfr': round(float(r_s_sfr), 4),
    'spearman_p_sfr': round(float(p_s_sfr), 4),
    'photometric_only_rho': round(float(r_s_phot), 4),
    'photometric_only_p': round(float(p_s_phot), 4),
    'photometric_only_n': int(phot_mask.sum()),
    'tertile_low': round(float(D_lo), 4),
    'tertile_mid': round(float(D_mi), 4),
    'tertile_high': round(float(D_hi), 4),
    'mannwhitney_p': round(float(p_mw), 4),
    'direction': direction, 'significant': bool(significant),
    'n_galaxies': N_gal, 'sources': src_counts,
}
with open(os.path.join(RES, 'correlation_stats.json'), 'w') as f:
    json.dump(corr, f, indent=2)

with open(os.path.join(RES, 'btfr_fit.json'), 'w') as f:
    json.dump({'slope': round(float(B_fit), 4), 'intercept': round(float(A_fit), 4),
               'n': N_gal}, f, indent=2)

if significant and direction == 'positive':
    verdict = 'CONSISTENT WITH ED (positive, p<0.05)'
elif not significant and direction == 'positive':
    verdict = 'SUGGESTIVE (positive, not significant)'
elif direction == 'negative' and significant:
    verdict = 'CONTRADICTS ED'
else:
    verdict = 'INCONCLUSIVE'

summary = {
    'experiment': 'ED-Data-14: Photometric SFR Test',
    'date': '2026-03-31',
    'n_galaxies': N_gal,
    'sfr_sources': src_counts,
    'btfr_slope': round(float(B_fit), 3),
    'correlation': corr,
    'verdict': verdict,
    'comparison': {
        'ED_Data_12': 'T-type proxy: rho=+0.039, p=0.667',
        'ED_Data_13': 'Calibrated sSFR: rho=+0.101, p=0.279; SFR rho=+0.263, p=0.004',
        'ED_Data_14': f'Photometric SFR: rho(sSFR)={r_s_ssfr:+.3f} p={p_s_ssfr:.3f}; rho(SFR)={r_s_sfr:+.3f} p={p_s_sfr:.3f}',
    },
}
with open(os.path.join(RES, 'final_summary.json'), 'w') as f:
    json.dump(summary, f, indent=2)

with open(os.path.join(RES, 'final_summary.md'), 'w') as f:
    f.write(f"""# ED-Data-14: Photometric SFR Test — Results

**{N_gal} SPARC galaxies** with literature-compiled photometric SFR.
Sources: {src_counts}

## Primary: Delta vs log(sSFR)
- Spearman rho = **{r_s_ssfr:+.4f}**, p = **{p_s_ssfr:.4f}**
- Bootstrap CI: [{rho_ci[0]:+.4f}, {rho_ci[1]:+.4f}]

## Secondary: Delta vs log(SFR)
- Spearman rho = **{r_s_sfr:+.4f}**, p = **{p_s_sfr:.4f}**

## Photometric-only (z0MGS+KINGFISH+11HUGS, n={phot_mask.sum()})
- Spearman rho = **{r_s_phot:+.4f}**, p = **{p_s_phot:.4f}**

## Tertiles
| Tertile | n | Mean Delta |
|---------|---|------------|
| Low sSFR | {len(low_i)} | {D_lo:+.4f} |
| Mid sSFR | {len(mid_i)} | {D_mi:+.4f} |
| High sSFR | {len(high_i)} | {D_hi:+.4f} |
| Mann-Whitney (high>low) | | p={p_mw:.4f} |

## Verdict: **{verdict}**

## Progression
| Module | Proxy | rho(sSFR) | p | rho(SFR) | p |
|--------|-------|-----------|---|----------|---|
| ED-Data-12 | T-type | +0.039 | 0.667 | — | — |
| ED-Data-13 | Calibrated | +0.101 | 0.279 | +0.263 | 0.004 |
| ED-Data-14 | Photometric | {r_s_ssfr:+.3f} | {p_s_ssfr:.3f} | {r_s_sfr:+.3f} | {p_s_sfr:.3f} |
""")

print(f"\n{'='*85}")
print(f"  ED-DATA-14 COMPLETE")
print(f"{'='*85}")
print(f"  sSFR: rho={r_s_ssfr:+.4f} p={p_s_ssfr:.4f}")
print(f"  SFR:  rho={r_s_sfr:+.4f} p={p_s_sfr:.4f}")
print(f"  Phot-only (n={phot_mask.sum()}): rho={r_s_phot:+.4f} p={p_s_phot:.4f}")
print(f"  Tertiles: low={D_lo:+.4f} mid={D_mi:+.4f} high={D_hi:+.4f}")
print(f"  Mann-Whitney: p={p_mw:.4f}")
print(f"  VERDICT: {verdict}")
