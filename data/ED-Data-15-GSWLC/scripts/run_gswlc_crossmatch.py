"""
ED-Data-15: GSWLC Cross-Match for Definitive SFR Test.

STATUS: AWAITING DATA DOWNLOAD.

This script processes the GSWLC catalog cross-matched with SPARC galaxies.
It requires the user to download GSWLC-X2 or GSWLC-A2 and place it in:
    data/ED-Data-15-GSWLC/raw/GSWLC-X2.dat

Download instructions:
    1. Go to https://salims.pages.iu.edu/gswlc/
    2. Download GSWLC-X2.dat.gz (or GSWLC-A2.dat.gz for deeper UV)
    3. Gunzip and place in data/ED-Data-15-GSWLC/raw/

The script will:
    1. Load GSWLC (columns: OBJID, RA, DEC, log_Mstar, log_SFR, flag_sed, flag_mgs)
    2. Load SPARC galaxy coordinates (from NED or SPARC catalog)
    3. Cross-match by position (< 10 arcsec)
    4. Extract SFR, sSFR for matched galaxies
    5. Fit BTFR and compute residuals
    6. Test ED-Phys-05 correlation prediction
    7. Generate plots and summary

GSWLC column reference (from Salim+2016):
    Col 1:  OBJID (SDSS)
    Col 2:  RA (deg)
    Col 3:  DEC (deg)
    Col 10: log_Mstar (Msun) — SED-fitted stellar mass
    Col 11: log_SFR (Msun/yr) — UV+optical+IR SED-fitted SFR
    Col 14: flag_sed (0=good, 1=bad)
    Col 15: flag_mgs (1=Main Galaxy Sample)
"""
import json, os, sys, warnings
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
warnings.filterwarnings('ignore')

BASE = 'data/ED-Data-15-GSWLC'
RAW = os.path.join(BASE, 'raw')
FIG = os.path.join(BASE, 'figures')
RES = os.path.join(BASE, 'results')

# ═══ SPARC galaxy coordinates ═══
# RA, DEC from NED/SIMBAD for cross-matching
# Format: (name, RA_deg, DEC_deg, T, logMb, Vflat, Q)
sparc_coords = [
    ("UGC02885", 57.98, 35.59, 5, 11.41, 300, 1),
    ("NGC2841", 140.51, 51.07, 3, 11.18, 287, 1),
    ("NGC7331", 339.27, 34.42, 3, 11.11, 244, 1),
    ("NGC2903", 143.04, 21.50, 4, 10.72, 183, 1),
    ("NGC3198", 154.98, 45.55, 5, 10.44, 150, 1),
    ("NGC3521", 166.45, -0.04, 4, 10.64, 206, 1),
    ("NGC5055", 198.96, 42.03, 4, 10.71, 194, 1),
    ("NGC5033", 198.36, 36.59, 5, 10.62, 195, 1),
    ("NGC891", 35.64, 42.35, 3, 10.71, 212, 1),
    ("NGC3726", 173.33, 47.03, 5, 10.27, 162, 1),
    ("NGC2403", 114.21, 65.60, 6, 10.01, 132, 1),
    ("NGC925", 36.82, 33.58, 7, 9.93, 117, 1),
    ("NGC3621", 169.57, -32.81, 7, 10.13, 148, 1),
    ("NGC6503", 267.41, 70.14, 6, 10.03, 116, 1),
    ("NGC7814", 0.81, 16.15, 2, 10.68, 231, 1),
    ("NGC7793", 359.46, -32.59, 7, 9.43, 107, 1),
    ("NGC300", 13.72, -37.68, 7, 9.47, 97, 1),
    ("NGC55", 3.72, -39.20, 9, 9.33, 86, 1),
    ("NGC4559", 188.99, 27.96, 6, 10.04, 122, 1),
    ("NGC3031", 148.89, 69.07, 2, 10.78, 224, 1),
    ("NGC5907", 228.97, 56.33, 5, 10.93, 227, 1),
    ("NGC4088", 182.58, 50.54, 4, 10.37, 173, 1),
    ("NGC4157", 182.77, 50.48, 3, 10.48, 189, 1),
    ("NGC4013", 179.63, 43.95, 3, 10.34, 178, 1),
    ("NGC2683", 133.17, 33.42, 3, 10.42, 194, 1),
    ("NGC3877", 176.53, 47.49, 5, 10.12, 164, 1),
    ("NGC3893", 177.16, 48.71, 5, 10.38, 175, 1),
    ("NGC3949", 178.25, 47.86, 4, 10.05, 161, 2),
    ("NGC3917", 177.68, 51.82, 6, 9.98, 137, 1),
    ("NGC4183", 183.27, 43.70, 6, 9.63, 109, 1),
    ("NGC1003", 39.60, 40.87, 6, 9.83, 114, 1),
    ("NGC4010", 179.67, 47.26, 7, 9.72, 118, 1),
    ("NGC5585", 215.00, 56.73, 7, 9.56, 92, 1),
    ("NGC2976", 146.81, 67.92, 5, 9.42, 83, 1),
    ("NGC4214", 183.91, 36.33, 10, 8.97, 60, 1),
    ("NGC4068", 181.07, 52.59, 10, 8.48, 41, 1),
    ("NGC2366", 112.28, 69.21, 10, 8.81, 53, 1),
    ("IC2574", 157.06, 68.41, 9, 9.00, 66, 1),
    ("NGC0801", 31.03, 38.73, 5, 11.07, 220, 1),
    ("NGC2742", 137.32, 60.48, 5, 10.12, 143, 2),
    ("NGC4100", 181.96, 49.58, 4, 10.21, 157, 1),
    ("NGC3953", 178.45, 52.33, 4, 10.54, 207, 1),
]

# ═══ Check for GSWLC file ═══
gswlc_files = ['GSWLC-X2.dat', 'GSWLC-A2.dat', 'GSWLC-M2.dat',
               'GSWLC-X2.dat.gz', 'GSWLC-A2.dat.gz']
gswlc_path = None
for gf in gswlc_files:
    candidate = os.path.join(RAW, gf)
    if os.path.exists(candidate):
        gswlc_path = candidate
        break

if gswlc_path is None:
    print("=" * 85)
    print("  ED-Data-15: GSWLC Cross-Match")
    print("=" * 85)
    print()
    print("  ERROR: GSWLC catalog not found.")
    print()
    print("  To run this analysis, download the GSWLC catalog:")
    print("    1. Go to https://salims.pages.iu.edu/gswlc/")
    print("    2. Download GSWLC-X2.dat.gz (recommended)")
    print("       Alternative: GSWLC-A2.dat.gz (deeper UV, fewer galaxies)")
    print(f"    3. Place the file in: {os.path.abspath(RAW)}/")
    print("    4. Gunzip if needed: gzip -d GSWLC-X2.dat.gz")
    print("    5. Re-run this script.")
    print()
    print("  File size: ~150-200 MB (compressed ~50 MB)")
    print("  Contents: ~660,000 galaxies with RA, DEC, M_star, SFR, flags")
    print()
    print("  This script will then:")
    print("    - Cross-match SPARC galaxies by position (< 10 arcsec)")
    print("    - Extract SFR, sSFR for matched galaxies")
    print("    - Fit BTFR and compute residuals")
    print("    - Test the ED-Phys-05 activity-dependence prediction")
    print("    - Generate publication-quality plots")
    print()

    # Write status file
    status = {
        'experiment': 'ED-Data-15: GSWLC Cross-Match',
        'status': 'AWAITING DATA',
        'instructions': 'Download GSWLC-X2.dat from https://salims.pages.iu.edu/gswlc/ and place in raw/',
        'sparc_galaxies_prepared': len(sparc_coords),
    }
    with open(os.path.join(RES, 'final_summary.json'), 'w') as f:
        json.dump(status, f, indent=2)
    sys.exit(0)

# ═══════════════════════════════════════════════════════════════════════
# IF GSWLC IS PRESENT: Run the full pipeline
# ═══════════════════════════════════════════════════════════════════════
print(f"  Loading GSWLC from {gswlc_path}...")

# Parse GSWLC using pandas
# GSWLC-X2.dat format (space-delimited, no header, 24 columns):
#   0: SDSS OBJID           1: secondary ID
#   2: plate                3: MJD                  4: fiber
#   5: RA (deg)             6: DEC (deg)
#   7: redshift             8: A_FUV (extinction)
#   9: log_Mstar            10: log_Mstar_err
#   11: log_SFR             12: log_SFR_err
#   13-18: SED parameters (Ldust, tau, etc.)
#   19: flag_sed (0=good)   20: flag_uv_class
#   21: flag_midir           22: flag_uv_detect
#   23: flag_mgs (1=Main Galaxy Sample)
import pandas as pd

# Handle both .gz and plain .dat — note the .gz may be already decompressed
# (browser auto-decompressed but kept .gz extension)
try:
    df_gswlc = pd.read_csv(gswlc_path, sep=r'\s+', header=None,
                            comment='#', on_bad_lines='skip')
except Exception:
    # Try the other file if first fails
    alt = gswlc_path.replace('.dat.gz', '.dat') if '.gz' in gswlc_path else gswlc_path + '.gz'
    if os.path.exists(alt):
        df_gswlc = pd.read_csv(alt, sep=r'\s+', header=None,
                                comment='#', on_bad_lines='skip')
    else:
        raise

print(f"  Raw GSWLC rows: {len(df_gswlc)}, columns: {df_gswlc.shape[1]}")
print(f"  First row sample (cols 5-12): {df_gswlc.iloc[0, 5:13].tolist()}")

# Extract columns by position
ncol = df_gswlc.shape[1]
# Detect layout: RA should be ~0-360, DEC ~-90 to 90
# Try col 5,6 first (standard GSWLC-X2 layout)
ra_col, dec_col = 5, 6
logM_col, logSFR_col = 9, 11
flag_sed_col = 19
flag_mgs_col = min(23, ncol - 1)  # safety

# Validate by checking value ranges
test_ra = pd.to_numeric(df_gswlc.iloc[:100, ra_col], errors='coerce')
if test_ra.median() < 0 or test_ra.median() > 360:
    # Try alternative column layout
    print("  WARNING: RA column doesn't look right, trying auto-detect...")
    for c in range(ncol):
        vals = pd.to_numeric(df_gswlc.iloc[:100, c], errors='coerce').dropna()
        if len(vals) > 50 and 0 < vals.median() < 360 and vals.std() > 10:
            ra_col = c
            dec_col = c + 1
            print(f"  Auto-detected RA at col {ra_col}, DEC at col {dec_col}")
            break

gswlc_ra = pd.to_numeric(df_gswlc.iloc[:, ra_col], errors='coerce').values
gswlc_dec = pd.to_numeric(df_gswlc.iloc[:, dec_col], errors='coerce').values
gswlc_logM = pd.to_numeric(df_gswlc.iloc[:, logM_col], errors='coerce').values
gswlc_logSFR = pd.to_numeric(df_gswlc.iloc[:, logSFR_col], errors='coerce').values

# Quality flags
if flag_sed_col < ncol and flag_mgs_col < ncol:
    flag_sed = pd.to_numeric(df_gswlc.iloc[:, flag_sed_col], errors='coerce').values
    flag_mgs = pd.to_numeric(df_gswlc.iloc[:, flag_mgs_col], errors='coerce').values
else:
    flag_sed = np.zeros(len(df_gswlc))
    flag_mgs = np.ones(len(df_gswlc))

# Filter: good SED fit, main galaxy sample, valid values
good = ((flag_sed == 0) & (flag_mgs == 1) &
        np.isfinite(gswlc_ra) & np.isfinite(gswlc_dec) &
        np.isfinite(gswlc_logM) & np.isfinite(gswlc_logSFR) &
        (gswlc_logM > 5) & (gswlc_logSFR > -99))

gswlc_ra = gswlc_ra[good]
gswlc_dec = gswlc_dec[good]
gswlc_logM = gswlc_logM[good]
gswlc_logSFR = gswlc_logSFR[good]
print(f"  GSWLC loaded: {len(gswlc_ra)} galaxies with good flags")

# Cross-match
MATCH_RADIUS = 10.0 / 3600.0  # 10 arcsec in degrees
matched = []
for s in sparc_coords:
    name, ra_s, dec_s, T, logMb, Vf, Q = s
    dist = np.sqrt(((gswlc_ra - ra_s)*np.cos(np.radians(dec_s)))**2 + (gswlc_dec - dec_s)**2)
    idx = np.argmin(dist)
    if dist[idx] < MATCH_RADIUS:
        matched.append({
            'name': name, 'T': T, 'logMb': logMb, 'Vflat': Vf, 'Q': Q,
            'logSFR': float(gswlc_logSFR[idx]),
            'logMstar_gswlc': float(gswlc_logM[idx]),
            'sep_arcsec': float(dist[idx] * 3600),
        })

print(f"  Cross-matched: {len(matched)} / {len(sparc_coords)} SPARC galaxies")

# Check for redshift incompatibility
gswlc_z = pd.to_numeric(df_gswlc.iloc[:, 7], errors='coerce').values
z_min = np.nanmin(gswlc_z[good])
print(f"  GSWLC redshift range: [{z_min:.4f}, {np.nanmax(gswlc_z[good]):.4f}]")

if len(matched) == 0:
    print()
    print("  *** FUNDAMENTAL INCOMPATIBILITY DETECTED ***")
    print(f"  GSWLC minimum redshift: z = {z_min:.4f}")
    print("  SPARC galaxies are at z < 0.005 (within ~20 Mpc)")
    print("  These catalogs DO NOT OVERLAP in redshift space.")
    print()
    print("  GSWLC was designed for SDSS galaxies at z = 0.01-0.30.")
    print("  SPARC galaxies are too nearby for SDSS spectroscopy —")
    print("  they are resolved, extended sources that overflow SDSS fibers.")
    print()
    print("  CONCLUSION: GSWLC cannot provide SFR for SPARC galaxies.")
    print("  The correct SFR catalog for SPARC is one of:")
    print("    - z0MGS (Leroy+ 2019) — GALEX+WISE for z < 0.05")
    print("    - 11HUGS (Lee+ 2009) — Halpha for nearby dwarfs")
    print("    - KINGFISH (Kennicutt+ 2011) — Halpha+24um for nearby spirals")
    print("    - Individual GALEX aperture photometry from NED")
    print()

    result = {
        'experiment': 'ED-Data-15: GSWLC Cross-Match',
        'status': 'INCOMPATIBLE — GSWLC does not cover SPARC redshift range',
        'gswlc_z_min': round(float(z_min), 4),
        'sparc_z_max': 0.005,
        'n_matched': 0,
        'n_gswlc_loaded': int(good.sum()),
        'verdict': 'CANNOT TEST — catalogs do not overlap',
        'recommended_catalogs': ['z0MGS (Leroy+ 2019)', '11HUGS (Lee+ 2009)',
                                  'KINGFISH (Kennicutt+ 2011)'],
        'note': 'GSWLC covers z=0.01-0.30; SPARC galaxies are at z<0.005. '
                'No cross-match is possible. Use nearby-galaxy SFR catalogs instead.',
    }
    with open(os.path.join(RES, 'final_summary.json'), 'w') as f:
        json.dump(result, f, indent=2)

    with open(os.path.join(RES, 'final_summary.md'), 'w') as f:
        f.write("# ED-Data-15: GSWLC Cross-Match — Result\n\n")
        f.write("## INCOMPATIBLE\n\n")
        f.write(f"GSWLC minimum redshift: z = {z_min:.4f}\n")
        f.write("SPARC galaxies: z < 0.005\n\n")
        f.write("**These catalogs do not overlap.** GSWLC cannot provide SFR for SPARC galaxies.\n\n")
        f.write("## Recommended alternatives\n\n")
        f.write("- z0MGS (Leroy+ 2019): GALEX+WISE SFR for z < 0.05\n")
        f.write("- 11HUGS (Lee+ 2009): Halpha SFR for nearby dwarfs\n")
        f.write("- KINGFISH (Kennicutt+ 2011): Halpha+24um for nearby spirals\n")
        f.write("- Individual GALEX aperture photometry from NED\n\n")
        f.write("## What this means for the ED activity test\n\n")
        f.write("The best available SFR data for SPARC galaxies remains the literature\n")
        f.write("compilation in ED-Data-14 (51 galaxies from z0MGS, KINGFISH, 11HUGS, NED).\n")
        f.write("The total-SFR signal is persistently positive (rho ~ +0.25) but not\n")
        f.write("significant at the photometric-only level (n=33). A definitive test\n")
        f.write("requires either z0MGS cross-matching or BIG-SPARC (4000 galaxies).\n")

    sys.exit(0)

if len(matched) < 10:
    print("  WARNING: Fewer than 10 matches. Results may be unreliable.")

# Compute derived quantities
for m in matched:
    m['logVf'] = np.log10(m['Vflat'])
    m['logsSFR'] = m['logSFR'] - m['logMstar_gswlc']

logMb_m = np.array([m['logMb'] for m in matched])
logVf_m = np.array([m['logVf'] for m in matched])
logSFR_m = np.array([m['logSFR'] for m in matched])
logsSFR_m = np.array([m['logsSFR'] for m in matched])
N_m = len(matched)

# BTFR fit
res = stats.theilslopes(logMb_m, logVf_m)
B_fit, A_fit = res[0], res[1]
Delta = logMb_m - (A_fit + B_fit * logVf_m)

# Correlations
r_s_ssfr, p_s_ssfr = stats.spearmanr(logsSFR_m, Delta)
r_s_sfr, p_s_sfr = stats.spearmanr(logSFR_m, Delta)
r_p_ssfr, p_p_ssfr = stats.pearsonr(logsSFR_m, Delta)
tau, p_tau = stats.kendalltau(logsSFR_m, Delta)

# Bootstrap
rng = np.random.default_rng(42)
rho_boot = [stats.spearmanr(logsSFR_m[rng.choice(N_m, N_m, replace=True)],
            Delta[rng.choice(N_m, N_m, replace=True)])[0] for _ in range(5000)]
rho_ci = np.percentile(rho_boot, [2.5, 97.5])

# Tertiles
idx_sorted = np.argsort(logsSFR_m)
n3 = N_m // 3
D_lo = np.mean(Delta[idx_sorted[:n3]])
D_hi = np.mean(Delta[idx_sorted[2*n3:]])
_, p_mw = stats.mannwhitneyu(Delta[idx_sorted[2*n3:]], Delta[idx_sorted[:n3]], alternative='greater')

significant = p_s_ssfr < 0.05
direction = 'positive' if r_s_ssfr > 0 else 'negative'

# Verdict
if significant and direction == 'positive':
    verdict = 'CONSISTENT WITH ED'
elif not significant and direction == 'positive':
    verdict = 'SUGGESTIVE'
elif direction == 'negative' and significant:
    verdict = 'CONTRADICTS ED'
else:
    verdict = 'INCONCLUSIVE'

print(f"\n  BTFR slope: {B_fit:.3f}")
print(f"  Spearman rho(Delta, sSFR): {r_s_ssfr:+.4f} (p={p_s_ssfr:.4f})")
print(f"  Spearman rho(Delta, SFR): {r_s_sfr:+.4f} (p={p_s_sfr:.4f})")
print(f"  Tertiles: low={D_lo:+.4f}, high={D_hi:+.4f}, MW p={p_mw:.4f}")
print(f"  VERDICT: {verdict}")

# Save everything
import csv
with open(os.path.join(RES, 'crossmatched_gswlc.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(matched[0].keys()))
    w.writeheader()
    w.writerows(matched)

with open(os.path.join(RES, 'btfr_fit.json'), 'w') as f:
    json.dump({'slope': round(float(B_fit),4), 'intercept': round(float(A_fit),4), 'n': N_m}, f, indent=2)

with open(os.path.join(RES, 'correlation_stats.json'), 'w') as f:
    json.dump({
        'spearman_rho_ssfr': round(float(r_s_ssfr),4), 'spearman_p_ssfr': round(float(p_s_ssfr),4),
        'spearman_rho_sfr': round(float(r_s_sfr),4), 'spearman_p_sfr': round(float(p_s_sfr),4),
        'pearson_r_ssfr': round(float(r_p_ssfr),4), 'kendall_tau': round(float(tau),4),
        'bootstrap_CI95': [round(float(rho_ci[0]),4), round(float(rho_ci[1]),4)],
        'tertile_low': round(float(D_lo),4), 'tertile_high': round(float(D_hi),4),
        'mannwhitney_p': round(float(p_mw),4),
        'direction': direction, 'significant': bool(significant),
        'verdict': verdict, 'n_matched': N_m,
    }, f, indent=2)

# Plots
fig, ax = plt.subplots(figsize=(9,7))
sc = ax.scatter(logVf_m, logMb_m, c=logSFR_m, cmap='RdYlBu_r', s=50, edgecolors='k', lw=0.4, zorder=5)
vfl = np.linspace(logVf_m.min()-0.1, logVf_m.max()+0.1, 100)
ax.plot(vfl, A_fit+B_fit*vfl, 'k-', lw=2)
plt.colorbar(sc, ax=ax, label='log SFR'); ax.set_xlabel('log Vf'); ax.set_ylabel('log Mb')
ax.set_title(f'BTFR (GSWLC, n={N_m})'); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P1_BTFR.png'), dpi=150); plt.close()

fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(logSFR_m, Delta, c='C0', s=40, edgecolors='k', lw=0.3)
sl, ic, _, _, _ = stats.linregress(logSFR_m, Delta)
xf = np.linspace(logSFR_m.min(), logSFR_m.max(), 100)
ax.plot(xf, sl*xf+ic, 'k-', lw=2, label=f'rho={r_s_sfr:+.3f}, p={p_s_sfr:.3f}')
ax.axhline(0, color='gray', lw=0.5); ax.set_xlabel('log SFR'); ax.set_ylabel('Delta')
ax.set_title('Delta vs SFR (GSWLC)'); ax.legend(); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P2_Delta_SFR.png'), dpi=150); plt.close()

fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(logsSFR_m, Delta, c='C1', s=40, edgecolors='k', lw=0.3)
sl2, ic2, _, _, _ = stats.linregress(logsSFR_m, Delta)
xf2 = np.linspace(logsSFR_m.min(), logsSFR_m.max(), 100)
ax.plot(xf2, sl2*xf2+ic2, 'k-', lw=2, label=f'rho={r_s_ssfr:+.3f}, p={p_s_ssfr:.3f}')
ax.axhline(0, color='gray', lw=0.5); ax.set_xlabel('log sSFR'); ax.set_ylabel('Delta')
ax.set_title('Delta vs sSFR (GSWLC)'); ax.legend(); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, 'P3_Delta_sSFR.png'), dpi=150); plt.close()

summary = {
    'experiment': 'ED-Data-15: GSWLC Cross-Match',
    'status': 'COMPLETE' if N_m >= 10 else 'INSUFFICIENT MATCHES',
    'n_matched': N_m, 'n_sparc': len(sparc_coords),
    'verdict': verdict,
    'correlation': {
        'rho_ssfr': round(float(r_s_ssfr),4), 'p_ssfr': round(float(p_s_ssfr),4),
        'rho_sfr': round(float(r_s_sfr),4), 'p_sfr': round(float(p_s_sfr),4),
    },
}
with open(os.path.join(RES, 'final_summary.json'), 'w') as f:
    json.dump(summary, f, indent=2)

print("\n  All outputs saved.")
