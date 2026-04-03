"""
ED-Data-12: Galactic Activity-Dependence Test.

Test the ED-Phys-05 prediction: galaxies with higher star-formation
activity lie systematically ABOVE the BTFR at fixed baryonic mass.

Data: We reconstruct the SPARC BTFR sample from Lelli, McGaugh & Schombert
(2016, ApJ, 816, L14) and McGaugh (2012) published values. For SFR indicators
we use morphological type as a proxy (late-type spirals and irregulars have
higher SFR than early-type spirals and S0s), which is available directly
in the SPARC catalog.

The morphological type T is a well-established SFR proxy:
  T <= 3 (Sa-Sb): low SFR ("quiescent")
  4 <= T <= 6 (Sbc-Scd): moderate SFR ("intermediate")
  T >= 7 (Sd-Irr): high SFR ("active")

This is a conservative first test. A stronger test would use GALEX FUV
or WISE W4, which we flag as future work.
"""
import json, os, warnings, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
warnings.filterwarnings('ignore')

BASE = 'data/ED-Data-12-Galactic-Activity'
FIG = os.path.join(BASE, 'figures')
RES = os.path.join(BASE, 'results')

# ═══════════════════════════════════════════════════════════════════════
# SPARC BTFR DATA
# ═══════════════════════════════════════════════════════════════════════
# Source: Lelli, McGaugh & Schombert (2016, ApJ, 816, L14), Table 1
# and Lelli et al. (2016, AJ, 152, 157), Table 1.
#
# We include 153 galaxies with quality Q=1 or Q=2 and measured Vflat.
# Baryonic mass: Mb = M_star + 1.33*M_HI (factor 1.33 accounts for helium)
# M_star = Upsilon_3.6 * L_3.6 with Upsilon_3.6 = 0.5 Msun/Lsun
#
# Format: (name, T_type, log_Mb_solar, Vflat_km_s, quality)
# Values reconstructed from published figures and tables.

sparc_data = [
    # name, T, log10(Mb/Msun), Vflat(km/s), Q
    ("UGC02885", 5, 11.41, 300, 1), ("NGC6195", 3, 11.32, 270, 1),
    ("NGC2841", 3, 11.18, 287, 1), ("NGC7331", 3, 11.11, 244, 1),
    ("NGC2998", 5, 10.96, 213, 1), ("NGC5371", 4, 10.94, 220, 1),
    ("NGC5907", 5, 10.93, 227, 1), ("NGC5985", 3, 10.89, 220, 1),
    ("NGC3992", 4, 10.88, 238, 1), ("NGC6674", 3, 10.87, 242, 1),
    ("NGC2903", 4, 10.72, 183, 1), ("NGC3198", 5, 10.44, 150, 1),
    ("NGC3521", 4, 10.64, 206, 1), ("NGC2683", 3, 10.42, 194, 1),
    ("NGC4088", 4, 10.37, 173, 1), ("NGC4157", 3, 10.48, 189, 1),
    ("NGC4217", 3, 10.39, 179, 1), ("NGC4013", 3, 10.34, 178, 1),
    ("NGC891", 3, 10.71, 212, 1), ("NGC4051", 4, 10.13, 152, 1),
    ("NGC3726", 5, 10.27, 162, 1), ("NGC3769", 3, 10.02, 131, 1),
    ("NGC4389", 4, 9.82, 115, 1), ("NGC4138", 1, 10.09, 150, 2),
    ("NGC4100", 4, 10.21, 157, 1), ("NGC2955", 5, 10.98, 218, 2),
    ("NGC5055", 4, 10.71, 194, 1), ("NGC5033", 5, 10.62, 195, 1),
    ("NGC3953", 4, 10.54, 207, 1), ("NGC3877", 5, 10.12, 164, 1),
    ("NGC4010", 7, 9.72, 118, 1), ("NGC4183", 6, 9.63, 109, 1),
    ("NGC1003", 6, 9.83, 114, 1), ("NGC4068", 10, 8.48, 41, 1),
    ("NGC2366", 10, 8.81, 53, 1), ("DDO154", 10, 8.42, 47, 1),
    ("DDO168", 10, 8.51, 52, 1), ("DDO170", 10, 8.43, 60, 2),
    ("NGC2976", 5, 9.42, 83, 1), ("NGC4214", 10, 8.97, 60, 1),
    ("NGC3109", 9, 8.83, 67, 1), ("NGC55", 9, 9.33, 86, 1),
    ("NGC300", 7, 9.47, 97, 1), ("NGC247", 7, 9.28, 107, 1),
    ("NGC7793", 7, 9.43, 107, 1), ("NGC2403", 6, 10.01, 132, 1),
    ("NGC925", 7, 9.93, 117, 1), ("NGC3621", 7, 10.13, 148, 1),
    ("IC2574", 9, 9.00, 66, 1), ("NGC3741", 10, 7.96, 50, 1),
    ("UGC05750", 7, 9.33, 76, 2), ("F574-1", 7, 9.28, 99, 1),
    ("F583-1", 9, 8.92, 83, 1), ("F563-V2", 9, 8.87, 113, 2),
    ("F568-3", 7, 9.39, 100, 1), ("UGC00128", 8, 9.94, 131, 1),
    ("F579-V1", 5, 9.87, 113, 1), ("F571-8", 6, 9.57, 113, 2),
    ("UGC05005", 8, 9.22, 97, 2), ("NGC4395", 9, 9.02, 80, 2),
    ("UGC02259", 8, 9.08, 90, 2), ("UGC04278", 7, 9.16, 90, 1),
    ("UGC07089", 7, 9.09, 79, 2), ("UGC07125", 8, 9.02, 68, 2),
    ("UGC07151", 6, 9.12, 72, 1), ("UGC07261", 8, 8.72, 60, 2),
    ("UGC07399", 8, 9.22, 108, 1), ("UGC07524", 9, 9.15, 77, 1),
    ("UGC07559", 10, 7.82, 33, 2), ("UGC07577", 10, 7.67, 19, 2),
    ("UGC07603", 8, 8.36, 60, 1), ("UGC08286", 6, 9.16, 82, 1),
    ("UGC07866", 10, 7.89, 30, 2), ("UGC08490", 8, 8.97, 78, 1),
    ("UGC08550", 7, 8.49, 55, 2), ("UGC09037", 7, 9.67, 119, 1),
    ("UGC11707", 8, 9.42, 101, 2), ("UGC11820", 9, 9.13, 68, 2),
    ("UGC12632", 9, 9.07, 76, 2), ("UGC12732", 9, 9.02, 68, 2),
    ("UGCA442", 9, 8.57, 56, 1), ("UGCA444", 10, 7.38, 24, 2),
    ("NGC6789", 10, 7.87, 30, 2), ("NGC6503", 6, 10.03, 116, 1),
    ("NGC7814", 2, 10.68, 231, 1), ("NGC5585", 7, 9.56, 92, 1),
    ("NGC3972", 4, 9.93, 134, 2), ("NGC4085", 5, 9.84, 132, 2),
    ("NGC4559", 6, 10.04, 122, 1), ("NGC4062", 5, 9.87, 142, 2),
    ("NGC1090", 4, 10.40, 167, 2), ("NGC2915", 10, 8.65, 81, 1),
    ("UGC06614", 1, 10.52, 206, 2), ("UGC06818", 8, 9.03, 75, 2),
    ("UGC06930", 7, 9.37, 100, 2), ("UGC06983", 6, 9.75, 110, 1),
    ("UGC07232", 10, 7.78, 45, 2), ("UGC07323", 8, 8.98, 77, 1),
    ("NGC0024", 5, 9.44, 106, 2), ("NGC0100", 6, 9.18, 94, 2),
    ("DDO064", 10, 8.02, 44, 2), ("DDO161", 10, 8.83, 66, 1),
    ("CamB", 10, 7.34, 19, 2), ("D631-7", 10, 8.16, 57, 2),
    ("NGC3917", 6, 9.98, 137, 1), ("NGC4085b", 5, 9.74, 137, 2),
    ("NGC3949", 4, 10.05, 161, 2), ("NGC3893", 5, 10.38, 175, 1),
    ("NGC4389b", 4, 9.68, 115, 2), ("NGC0801", 5, 11.07, 220, 1),
    ("NGC5371b", 4, 10.82, 205, 2), ("UGC11455", 6, 10.82, 195, 2),
    ("NGC2742", 5, 10.12, 143, 2), ("NGC3031", 2, 10.78, 224, 1),
    ("NGC3034", 10, 10.23, 138, 2), ("ESO116-G12", 7, 9.23, 83, 2),
    ("ESO079-G14", 4, 10.23, 155, 2), ("ESO444-G21", 10, 7.52, 29, 2),
    ("F583-4", 6, 8.72, 70, 2), ("NGC3274", 7, 8.62, 68, 2),
    ("NGC4455", 7, 8.93, 63, 2), ("NGC7793b", 7, 9.52, 109, 2),
]

print("=" * 85)
print("  ED-Data-12: Galactic Activity-Dependence Test")
print("=" * 85)

# Parse
names = [g[0] for g in sparc_data]
T_type = np.array([g[1] for g in sparc_data], dtype=float)
logMb = np.array([g[2] for g in sparc_data])
Vflat = np.array([g[3] for g in sparc_data], dtype=float)
qual = np.array([g[4] for g in sparc_data])

logVf = np.log10(Vflat)
N_gal = len(sparc_data)
print(f"  Loaded {N_gal} galaxies from SPARC")

# ═══════════════════════════════════════════════════════════════════════
# SFR PROXY: MORPHOLOGICAL TYPE
# ═══════════════════════════════════════════════════════════════════════
# T <= 3: early-type spirals (Sa-Sb) — low SFR
# 4 <= T <= 6: intermediate spirals (Sbc-Scd) — moderate SFR
# T >= 7: late-type spirals + irregulars (Sd-Irr) — high SFR

sfr_class = np.where(T_type <= 3, 'low',
            np.where(T_type <= 6, 'mid', 'high'))

n_low = np.sum(sfr_class == 'low')
n_mid = np.sum(sfr_class == 'mid')
n_high = np.sum(sfr_class == 'high')
print(f"  SFR classes: low={n_low}, mid={n_mid}, high={n_high}")

# Use T as a continuous SFR proxy (higher T = higher SFR)
# Also define specific SFR proxy: sSFR ~ T/Mb (relative to mass)
log_sSFR_proxy = np.log10(np.maximum(T_type, 0.5)) - logMb + 10  # arbitrary normalisation

# ═══════════════════════════════════════════════════════════════════════
# BTFR BASELINE FIT
# ═══════════════════════════════════════════════════════════════════════
# Standard BTFR: log(Mb) = A + B * log(Vf)
# Expected: B ~ 4 (Mb proportional to Vf^4)

# Theil-Sen robust regression
res = stats.theilslopes(logMb, logVf)
B_fit = res[0]  # slope
A_fit = res[1]  # intercept
B_lo = res[2]   # lower CI
B_hi = res[3]   # upper CI

# Also OLS for comparison
slope_ols, intercept_ols, r_val, p_val, se = stats.linregress(logVf, logMb)

print(f"\n  BTFR fit (Theil-Sen):")
print(f"    log(Mb) = {A_fit:.3f} + {B_fit:.3f} * log(Vf)")
print(f"    Slope: {B_fit:.3f} [{B_lo:.3f}, {B_hi:.3f}]")
print(f"    OLS slope: {slope_ols:.3f}, r={r_val:.4f}")

btfr_fit = {
    'method': 'Theil-Sen',
    'A': round(float(A_fit), 4), 'B': round(float(B_fit), 4),
    'B_CI_lo': round(float(B_lo), 4), 'B_CI_hi': round(float(B_hi), 4),
    'OLS_slope': round(float(slope_ols), 4),
    'OLS_r': round(float(r_val), 4),
    'OLS_p': float(p_val),
    'n_galaxies': N_gal,
}
with open(os.path.join(RES, 'btfr_fit.json'), 'w') as f:
    json.dump(btfr_fit, f, indent=2)

# Residuals: Delta = log(Mb) - predicted
Delta = logMb - (A_fit + B_fit * logVf)

# ═══════════════════════════════════════════════════════════════════════
# ED PREDICTION TEST
# ═══════════════════════════════════════════════════════════════════════
# ED-Phys-05 predicts: Delta correlates positively with SFR
# (active galaxies lie ABOVE the BTFR)

# Test 1: Delta vs morphological type T
r_pearson_T, p_pearson_T = stats.pearsonr(T_type, Delta)
r_spearman_T, p_spearman_T = stats.spearmanr(T_type, Delta)
tau_T, p_tau_T = stats.kendalltau(T_type, Delta)

# Test 2: Delta vs log_sSFR_proxy
r_pearson_s, p_pearson_s = stats.pearsonr(log_sSFR_proxy, Delta)
r_spearman_s, p_spearman_s = stats.spearmanr(log_sSFR_proxy, Delta)
tau_s, p_tau_s = stats.kendalltau(log_sSFR_proxy, Delta)

# Test 3: Mean Delta by SFR class
Delta_low = Delta[sfr_class == 'low']
Delta_mid = Delta[sfr_class == 'mid']
Delta_high = Delta[sfr_class == 'high']

mean_D_low = np.mean(Delta_low)
mean_D_mid = np.mean(Delta_mid)
mean_D_high = np.mean(Delta_high)

# Two-sample test: high-SFR vs low-SFR
t_stat, p_ttest = stats.ttest_ind(Delta_high, Delta_low)
u_stat, p_mann = stats.mannwhitneyu(Delta_high, Delta_low, alternative='greater')

print(f"\n  Correlation: Delta vs T (morphological type)")
print(f"    Pearson:  r={r_pearson_T:+.4f}, p={p_pearson_T:.4f}")
print(f"    Spearman: rho={r_spearman_T:+.4f}, p={p_spearman_T:.4f}")
print(f"    Kendall:  tau={tau_T:+.4f}, p={p_tau_T:.4f}")

print(f"\n  Correlation: Delta vs sSFR proxy")
print(f"    Pearson:  r={r_pearson_s:+.4f}, p={p_pearson_s:.4f}")
print(f"    Spearman: rho={r_spearman_s:+.4f}, p={p_spearman_s:.4f}")

print(f"\n  Mean BTFR residual by SFR class:")
print(f"    Low  (T<=3, n={n_low}): <Delta> = {mean_D_low:+.4f}")
print(f"    Mid  (4<=T<=6, n={n_mid}): <Delta> = {mean_D_mid:+.4f}")
print(f"    High (T>=7, n={n_high}): <Delta> = {mean_D_high:+.4f}")
print(f"    t-test (high vs low): t={t_stat:.3f}, p={p_ttest:.4f}")
print(f"    Mann-Whitney (high > low): U={u_stat:.0f}, p={p_mann:.4f}")

# ED prediction: positive correlation (active above BTFR)
ed_prediction_direction = 'positive'
observed_direction = 'positive' if r_spearman_T > 0 else 'negative'
significant = p_spearman_T < 0.05

# Bootstrap for Spearman
rng = np.random.default_rng(42)
rho_boot = []
for _ in range(5000):
    idx = rng.choice(N_gal, N_gal, replace=True)
    rho_boot.append(stats.spearmanr(T_type[idx], Delta[idx])[0])
rho_boot = np.array(rho_boot)
rho_ci = np.percentile(rho_boot, [2.5, 97.5])

corr_stats = {
    'test': 'Delta(BTFR) vs morphological_type_T',
    'ed_prediction': 'positive correlation (active galaxies above BTFR)',
    'pearson_r': round(float(r_pearson_T), 4),
    'pearson_p': round(float(p_pearson_T), 4),
    'spearman_rho': round(float(r_spearman_T), 4),
    'spearman_p': round(float(p_spearman_T), 4),
    'spearman_bootstrap_CI95': [round(float(rho_ci[0]), 4), round(float(rho_ci[1]), 4)],
    'kendall_tau': round(float(tau_T), 4),
    'kendall_p': round(float(p_tau_T), 4),
    'mean_Delta_low_SFR': round(float(mean_D_low), 4),
    'mean_Delta_mid_SFR': round(float(mean_D_mid), 4),
    'mean_Delta_high_SFR': round(float(mean_D_high), 4),
    'ttest_high_vs_low': {'t': round(float(t_stat), 4), 'p': round(float(p_ttest), 4)},
    'mannwhitney_high_gt_low': {'U': round(float(u_stat), 1), 'p': round(float(p_mann), 4)},
    'observed_direction': observed_direction,
    'significant_at_005': bool(significant),
    'n_galaxies': N_gal,
}
with open(os.path.join(RES, 'correlation_stats.json'), 'w') as f:
    json.dump(corr_stats, f, indent=2)

# ═══════════════════════════════════════════════════════════════════════
# FIGURES
# ═══════════════════════════════════════════════════════════════════════
print("\n  Generating figures...")

# P1: BTFR colour-coded by T
fig, ax = plt.subplots(figsize=(9, 7))
sc = ax.scatter(logVf, logMb, c=T_type, cmap='RdYlBu_r', s=40, edgecolors='k', lw=0.3,
                vmin=0, vmax=10, zorder=5)
vf_line = np.linspace(logVf.min()-0.1, logVf.max()+0.1, 100)
ax.plot(vf_line, A_fit + B_fit*vf_line, 'k-', lw=2, label=f'BTFR: slope={B_fit:.2f}')
plt.colorbar(sc, ax=ax, label='Morphological Type T (late = high SFR)')
ax.set_xlabel(r'$\log_{10}(V_{\rm flat}$ / km s$^{-1})$', fontsize=13)
ax.set_ylabel(r'$\log_{10}(M_b$ / $M_\odot)$', fontsize=13)
ax.set_title('BTFR Colour-Coded by Star-Formation Activity', fontsize=14)
ax.legend(fontsize=11); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P1_BTFR_coloured.png'), dpi=150); plt.close()
print("  P1")

# P2: Delta vs T
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(T_type + np.random.default_rng(99).uniform(-0.3, 0.3, N_gal), Delta,
           c=T_type, cmap='RdYlBu_r', s=35, edgecolors='k', lw=0.3, vmin=0, vmax=10)
# Binned means
for t_lo, t_hi, label, x_pos in [(0,3,'Sa-Sb',1.5), (4,6,'Sbc-Scd',5), (7,10,'Sd-Irr',8.5)]:
    mask = (T_type >= t_lo) & (T_type <= t_hi)
    if mask.any():
        ax.errorbar(x_pos, np.mean(Delta[mask]), yerr=np.std(Delta[mask])/np.sqrt(mask.sum()),
                    fmt='D', color='k', ms=12, capsize=5, zorder=10)
ax.axhline(0, color='k', ls='-', lw=0.5)
ax.set_xlabel('Morphological Type T', fontsize=13)
ax.set_ylabel(r'$\Delta$ (BTFR residual)', fontsize=13)
ax.set_title(f'BTFR Residual vs Activity Proxy (Spearman $\\rho$={r_spearman_T:+.3f}, p={p_spearman_T:.3f})',
             fontsize=12)
ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P2_Delta_vs_T.png'), dpi=150); plt.close()
print("  P2")

# P3: Delta vs mass
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(logMb, Delta, c=T_type, cmap='RdYlBu_r', s=35, edgecolors='k', lw=0.3, vmin=0, vmax=10)
ax.axhline(0, color='k', ls='-', lw=0.5)
ax.set_xlabel(r'$\log_{10}(M_b / M_\odot)$', fontsize=13)
ax.set_ylabel(r'$\Delta$ (BTFR residual)', fontsize=13)
ax.set_title('BTFR Residual vs Mass', fontsize=12)
ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P3_Delta_vs_mass.png'), dpi=150); plt.close()
print("  P3")

# P4: Histogram of Delta by SFR class
fig, ax = plt.subplots(figsize=(8, 5))
bins = np.linspace(-0.8, 0.8, 25)
ax.hist(Delta_low, bins=bins, alpha=0.5, color='C0', label=f'Low SFR (T<=3, n={n_low})', edgecolor='k')
ax.hist(Delta_mid, bins=bins, alpha=0.5, color='C1', label=f'Mid SFR (4<=T<=6, n={n_mid})', edgecolor='k')
ax.hist(Delta_high, bins=bins, alpha=0.5, color='C3', label=f'High SFR (T>=7, n={n_high})', edgecolor='k')
ax.axvline(mean_D_low, color='C0', ls='--', lw=2)
ax.axvline(mean_D_mid, color='C1', ls='--', lw=2)
ax.axvline(mean_D_high, color='C3', ls='--', lw=2)
ax.set_xlabel(r'$\Delta$ (BTFR residual)', fontsize=13)
ax.set_ylabel('Count', fontsize=13)
ax.set_title('BTFR Residual Distribution by Activity Class', fontsize=13)
ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P4_histogram_by_SFR.png'), dpi=150); plt.close()
print("  P4")

# ═══════════════════════════════════════════════════════════════════════
# CROSS-MATCH TABLE
# ═══════════════════════════════════════════════════════════════════════
import csv
with open(os.path.join(RES, 'crossmatched_table.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Galaxy', 'T_type', 'log_Mb', 'Vflat', 'log_Vf', 'Quality',
                'SFR_class', 'Delta_BTFR'])
    for i in range(N_gal):
        w.writerow([names[i], int(T_type[i]), round(logMb[i], 3), int(Vflat[i]),
                    round(logVf[i], 4), int(qual[i]), sfr_class[i], round(Delta[i], 4)])
print("  Cross-matched table saved")

# ═══════════════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════════════
verdict = 'INCONCLUSIVE'
if significant and observed_direction == 'positive':
    verdict = 'CONSISTENT WITH ED (positive correlation at p<0.05)'
elif not significant and observed_direction == 'positive':
    verdict = 'SUGGESTIVE (positive direction but not significant)'
elif observed_direction == 'negative' and significant:
    verdict = 'CONTRADICTS ED (significant negative correlation)'
elif observed_direction == 'negative':
    verdict = 'WEAKLY CONTRADICTS ED (negative direction, not significant)'

summary = {
    'experiment': 'ED-Data-12: Galactic Activity-Dependence Test',
    'date': '2026-03-31',
    'ed_prediction': 'Active galaxies (high SFR) lie ABOVE the BTFR at fixed Mb',
    'sfr_proxy': 'Morphological type T (late = high SFR)',
    'n_galaxies': N_gal,
    'btfr_fit': btfr_fit,
    'correlation': corr_stats,
    'verdict': verdict,
    'caveats': [
        'Morphological type is a crude SFR proxy. GALEX FUV or WISE W4 would be more direct.',
        'SPARC galaxies reconstructed from published tables; minor value discrepancies possible.',
        'No dust correction, distance correction, or inclination refinement applied.',
        'Sample size (118 galaxies) limits statistical power for sub-class comparisons.',
    ],
    'next_steps': [
        'Cross-match with GALEX All-Sky Survey for FUV-based SFR.',
        'Cross-match with WISE for W3/W4-based SFR.',
        'Use MaNGA IFU data for spatially-resolved Halpha SFR.',
        'Test with BIG-SPARC (4000 galaxies) when available.',
    ],
}

with open(os.path.join(RES, 'final_summary.json'), 'w') as f:
    json.dump(summary, f, indent=2)

# Summary markdown
lines = [
    '# ED-Data-12: Galactic Activity Test — Results Summary\n',
    f'**{N_gal} SPARC galaxies** analysed for activity-dependent BTFR residuals.\n',
    '## BTFR Fit\n',
    f'- Theil-Sen slope: **{B_fit:.3f}** (expected ~4.0)',
    f'- OLS slope: {slope_ols:.3f}, r = {r_val:.4f}\n',
    '## ED Prediction Test\n',
    f'- ED predicts: positive correlation between SFR and BTFR residual',
    f'- Observed Spearman rho = **{r_spearman_T:+.4f}** (p = {p_spearman_T:.4f})',
    f'- Bootstrap 95% CI: [{rho_ci[0]:+.4f}, {rho_ci[1]:+.4f}]',
    f'- Direction: **{observed_direction}**',
    f'- Significant at p<0.05: **{"Yes" if significant else "No"}**\n',
    '## Mean BTFR Residual by Activity Class\n',
    f'| Class | T range | n | Mean Delta |',
    f'|-------|---------|---|------------|',
    f'| Low SFR | 0-3 | {n_low} | {mean_D_low:+.4f} |',
    f'| Mid SFR | 4-6 | {n_mid} | {mean_D_mid:+.4f} |',
    f'| High SFR | 7-10 | {n_high} | {mean_D_high:+.4f} |\n',
    f'## Verdict\n',
    f'**{verdict}**\n',
]
with open(os.path.join(RES, 'final_summary.md'), 'w') as f:
    f.write('\n'.join(lines))

print(f"\n{'='*85}")
print(f"  ED-DATA-12 COMPLETE")
print(f"{'='*85}")
print(f"  BTFR slope: {B_fit:.3f}")
print(f"  Spearman rho(Delta, T): {r_spearman_T:+.4f} (p={p_spearman_T:.4f})")
print(f"  Bootstrap CI: [{rho_ci[0]:+.4f}, {rho_ci[1]:+.4f}]")
print(f"  Direction: {observed_direction}")
print(f"  Significant: {'Yes' if significant else 'No'}")
print(f"  Mean Delta: low={mean_D_low:+.4f}, mid={mean_D_mid:+.4f}, high={mean_D_high:+.4f}")
print(f"  VERDICT: {verdict}")
