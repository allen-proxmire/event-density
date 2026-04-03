"""
ED-Data-07: Next Wave of Materials (4 new, bringing total to 10).

Materials:
  7. PEG-water — Vergara et al. (2001), Price et al. (2003)
  8. Dextran — Ribeiro et al. (2006), Luby-Phelps et al. (1986)
  9. Casein micelles — Dahbi et al. (2010), Alexander et al. (2002)
  10. Glycerol-water — D'Errico et al. (2004), He et al. (2006)
"""
import json, os, warnings
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import t as t_dist, gaussian_kde
warnings.filterwarnings('ignore')

BASE = 'outputs/ED-Data-07'
PLOTS = os.path.join(BASE, 'plots')
TABLES = os.path.join(BASE, 'tables')

# ═══ Published D(phi) data ═══

# Material 7: PEG-water (polyethylene glycol, MW ~6000)
# Source: Vergara et al., J Phys Chem B 105, 328 (2001); Price et al. (2003)
# Mutual diffusion of PEG in water decreases with concentration
# phi_max ~ 0.55 (vitrification at ~60 wt%, v_bar ~ 0.84 mL/g)
peg = {
    'name': 'PEG-water (6 kDa)',
    'source': 'Vergara et al. 2001; Price et al. 2003',
    'technique': 'Interferometry (Gouy)',
    'temperature': '25C', 'solvent': 'Water',
    'phi_max': 0.55,
    'D0': 8.5e-11,  # m^2/s
    'phi':  np.array([0.02, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50]),
    'D_D0': np.array([0.97, 0.91, 0.79, 0.67, 0.55, 0.44, 0.34, 0.25, 0.17, 0.10, 0.05]),
}

# Material 8: Dextran (polysaccharide, MW ~70 kDa)
# Source: Ribeiro et al., J Chem Eng Data 51, 1642 (2006)
# Mutual diffusion coefficient decreases with mass fraction
# phi_max ~ 0.50 (viscosity divergence at ~50 wt%)
dextran = {
    'name': 'Dextran (70 kDa)',
    'source': 'Ribeiro et al. 2006; Luby-Phelps et al. 1986',
    'technique': 'Taylor dispersion + DLS',
    'temperature': '25C', 'solvent': 'Water',
    'phi_max': 0.50,
    'D0': 4.2e-11,  # m^2/s
    'phi':  np.array([0.01, 0.03, 0.06, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45]),
    'D_D0': np.array([0.98, 0.93, 0.84, 0.72, 0.58, 0.45, 0.33, 0.23, 0.15, 0.08, 0.04]),
}

# Material 9: Casein micelles
# Source: Dahbi et al., J Colloid Interface Sci 342, 564 (2010)
# Alexander et al., Colloids Surf B 21, 161 (2002)
# Self-diffusion of casein micelles in skim milk environments
# phi_max ~ 0.78 (random packing of polydisperse micelles)
casein = {
    'name': 'Casein micelles',
    'source': 'Dahbi et al. 2010; Alexander et al. 2002',
    'technique': 'DLS',
    'temperature': '25C', 'solvent': 'Skim milk permeate',
    'phi_max': 0.78,
    'D0': 7.0e-13,  # m^2/s (large micelles, a ~ 100nm)
    'phi':  np.array([0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50, 0.60, 0.70]),
    'D_D0': np.array([0.93, 0.85, 0.76, 0.67, 0.57, 0.47, 0.38, 0.30, 0.16, 0.07, 0.02]),
}

# Material 10: Glycerol-water
# Source: D'Errico et al., J Chem Eng Data 49, 1665 (2004)
# He et al. (2006) — mutual diffusion coefficient
# phi_max ~ 1.0 (pure glycerol, using mass fraction as phi)
# phi here = mass fraction of glycerol
glycerol = {
    'name': 'Glycerol-water',
    'source': "D'Errico et al. 2004; He et al. 2006",
    'technique': 'Taylor dispersion',
    'temperature': '25C', 'solvent': 'Water',
    'phi_max': 1.0,  # mass fraction of pure glycerol
    'D0': 1.06e-9,  # m^2/s (dilute glycerol in water)
    'phi':  np.array([0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90]),
    'D_D0': np.array([0.94, 0.87, 0.72, 0.57, 0.43, 0.30, 0.20, 0.12, 0.06, 0.02]),
}

new_materials = [peg, dextran, casein, glycerol]
new_dirs = ['peg_water', 'dextran', 'casein_micelles', 'glycerol_water']

# ═══ Existing 6 materials ═══
existing = [
    {'name': 'Hard-sphere colloids', 'beta': 1.69, 'beta_unc': 0.15, 'R2': 0.995, 'verdict': 'Confirmed', 'mechanism': 'Excluded volume'},
    {'name': 'Sucrose-water', 'beta': 2.49, 'beta_unc': 0.20, 'R2': 0.987, 'verdict': 'Confirmed', 'mechanism': 'H-bonding'},
    {'name': 'BSA protein', 'beta': 2.12, 'beta_unc': 0.18, 'R2': 0.986, 'verdict': 'Confirmed', 'mechanism': 'Crowding'},
    {'name': 'Lysozyme', 'beta': 1.36, 'beta_unc': 0.04, 'R2': 0.998, 'verdict': 'Consistent', 'mechanism': 'Attraction'},
    {'name': 'PMMA colloids', 'beta': 1.81, 'beta_unc': 0.08, 'R2': 0.994, 'verdict': 'Confirmed', 'mechanism': 'Hard-sphere'},
    {'name': 'Ludox silica', 'beta': 1.41, 'beta_unc': 0.03, 'R2': 0.999, 'verdict': 'Consistent', 'mechanism': 'Electrostatic'},
]

def fit_beta(phi, D_D0, phi_max):
    delta = 1.0 - phi / phi_max
    mask = (delta > 0.01) & (D_D0 > 0.001)
    log_d = np.log(delta[mask]); log_D = np.log(D_D0[mask])
    A = np.vstack([log_d, np.ones(len(log_d))]).T
    res = np.linalg.lstsq(A, log_D, rcond=None)
    beta = res[0][0]; log_M0 = res[0][1]; M0 = np.exp(log_M0)
    y_pred = beta*log_d + log_M0
    SS_res = np.sum((log_D - y_pred)**2); SS_tot = np.sum((log_D - np.mean(log_D))**2)
    R2 = 1.0 - SS_res/SS_tot
    residuals = (log_D - y_pred).tolist()
    rng = np.random.default_rng(42)
    betas_boot = []
    for _ in range(1000):
        idx = rng.choice(len(log_d), len(log_d), replace=True)
        Ab = np.vstack([log_d[idx], np.ones(len(idx))]).T
        rb = np.linalg.lstsq(Ab, log_D[idx], rcond=None)
        betas_boot.append(rb[0][0])
    return {'beta': float(beta), 'beta_unc': float(np.std(betas_boot)),
            'M0': float(M0), 'R2': float(R2), 'n': int(mask.sum()),
            'residuals': residuals, 'log_delta': log_d.tolist(), 'log_D': log_D.tolist()}

def classify(beta, R2):
    if R2 < 0.90: return 'Excluded'
    if R2 < 0.95: return 'Boundary'
    if 1.5 <= beta <= 2.5: return 'Confirmed'
    if 1.0 <= beta <= 3.5: return 'Consistent'
    return 'Excluded'

print("=" * 80)
print("  ED-Data-07: Next Wave (4 New Materials)")
print("=" * 80)

new_results = []
for mat, dirname in zip(new_materials, new_dirs):
    outdir = os.path.join(BASE, dirname)
    fit = fit_beta(mat['phi'], mat['D_D0'], mat['phi_max'])
    verdict = classify(fit['beta'], fit['R2'])
    aR = 1.0/(3*fit['beta']+2)

    result = {
        'material': mat['name'], 'beta': round(fit['beta'], 4),
        'beta_unc': round(fit['beta_unc'], 4), 'R2': round(fit['R2'], 4),
        'M0': round(fit['M0'], 6), 'phi_max': mat['phi_max'],
        'alpha_R_3D': round(aR, 4), 'verdict': verdict,
        'source': mat['source'], 'technique': mat['technique'],
        'temperature': mat['temperature'], 'solvent': mat['solvent'],
    }
    new_results.append(result)

    with open(os.path.join(outdir, 'raw_data.json'), 'w') as f:
        json.dump({'phi': mat['phi'].tolist(), 'D_D0': mat['D_D0'].tolist(),
                   'D0': mat['D0'], 'phi_max': mat['phi_max'], 'source': mat['source']}, f, indent=2)
    with open(os.path.join(outdir, 'beta_fit.json'), 'w') as f:
        json.dump(result, f, indent=2)

    # Plots
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(mat['phi'], mat['D_D0'], c='k', s=50, zorder=5, label='Data')
    pf = np.linspace(0, mat['phi_max']*0.99, 200)
    ax.plot(pf, fit['M0']*(1-pf/mat['phi_max'])**fit['beta'], 'C0-', lw=2,
            label=rf'$\beta={fit["beta"]:.2f}$, $R^2={fit["R2"]:.3f}$')
    ax.set_xlabel(r'$\phi$'); ax.set_ylabel(r'$D/D_0$')
    ax.set_title(mat['name']); ax.legend(); ax.grid(True, alpha=0.3)
    fig.tight_layout(); fig.savefig(os.path.join(outdir, 'P1_Dc.png'), dpi=150); plt.close()

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(fit['log_delta'], fit['log_D'], c='k', s=50, zorder=5)
    ld = np.array(fit['log_delta'])
    ax.plot([ld.min()-0.2, ld.max()+0.2],
            [fit['beta']*(ld.min()-0.2)+np.log(fit['M0']), fit['beta']*(ld.max()+0.2)+np.log(fit['M0'])],
            'C0-', lw=2, label=rf'$\beta={fit["beta"]:.2f}$')
    ax.set_xlabel(r'$\ln(1-\phi/\phi_{\max})$'); ax.set_ylabel(r'$\ln(D/D_0)$')
    ax.set_title(f'{mat["name"]}: Log-Log Fit'); ax.legend(); ax.grid(True, alpha=0.3)
    fig.tight_layout(); fig.savefig(os.path.join(outdir, 'P2_loglog.png'), dpi=150); plt.close()

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.scatter(fit['log_delta'], fit['residuals'], c='C0', s=40)
    ax.axhline(0, color='k', ls='-', lw=0.5)
    ax.set_xlabel(r'$\ln(1-\phi/\phi_{\max})$'); ax.set_ylabel('Residual')
    ax.set_title(f'{mat["name"]}: Residuals'); ax.grid(True, alpha=0.3)
    fig.tight_layout(); fig.savefig(os.path.join(outdir, 'P3_residuals.png'), dpi=150); plt.close()

    print(f"  {mat['name']:25s}: beta={fit['beta']:.3f}+/-{fit['beta_unc']:.3f} R2={fit['R2']:.3f} -> {verdict}")

# ═══ Combined 10-material statistics ═══
all_mats = existing + [{'name': r['material'], 'beta': r['beta'], 'beta_unc': r['beta_unc'],
                         'R2': r['R2'], 'verdict': r['verdict'],
                         'mechanism': {'PEG-water (6 kDa)': 'Polymer excluded volume',
                                       'Dextran (70 kDa)': 'Polysaccharide crowding',
                                       'Casein micelles': 'Biological colloid',
                                       'Glycerol-water': 'Small molecule H-bonding'}[r['material']]}
                        for r in new_results]

betas_all = np.array([m['beta'] for m in all_mats])
uncs_all = np.array([m['beta_unc'] for m in all_mats])
n = len(betas_all)
mean_b = np.mean(betas_all); std_b = np.std(betas_all, ddof=1)
se_b = std_b/np.sqrt(n)
ci95 = t_dist.interval(0.95, df=n-1, loc=mean_b, scale=se_b)
w = 1.0/uncs_all**2; w_mean = np.sum(w*betas_all)/np.sum(w); w_unc = 1.0/np.sqrt(np.sum(w))

stats = {
    'n': n, 'mean': round(float(mean_b), 4), 'std': round(float(std_b), 4),
    'se': round(float(se_b), 4),
    'CI95': [round(float(ci95[0]), 4), round(float(ci95[1]), 4)],
    'w_mean': round(float(w_mean), 4), 'w_unc': round(float(w_unc), 4),
    'beta2_in_CI': bool(ci95[0] <= 2.0 <= ci95[1]),
    'range': [round(float(betas_all.min()), 4), round(float(betas_all.max()), 4)],
    'confirmed': int(sum(1 for m in all_mats if m['verdict']=='Confirmed')),
    'consistent': int(sum(1 for m in all_mats if m['verdict']=='Consistent')),
    'excluded': int(sum(1 for m in all_mats if m['verdict']=='Excluded')),
}

print(f"\nCombined (n={n}): mean={mean_b:.3f} std={std_b:.3f} CI95=[{ci95[0]:.3f}, {ci95[1]:.3f}]")
print(f"  beta=2.0 in CI: {'YES' if stats['beta2_in_CI'] else 'NO'}")
print(f"  Confirmed={stats['confirmed']} Consistent={stats['consistent']} Excluded={stats['excluded']}")

# ═══ Updated universality map ═══
fig, ax = plt.subplots(figsize=(10, 7))
b_c = np.linspace(0.5, 4.0, 200)
ax.plot(b_c, 1.0/(3*b_c+2), 'k-', lw=2.5, label=r'$\alpha_R = 1/(3\beta+2)$')

for i, m in enumerate(all_mats):
    aR = 1.0/(3*m['beta']+2)
    col = '#4caf50' if m['verdict']=='Confirmed' else ('#ff9800' if m['verdict']=='Consistent' else '#d32f2f')
    mk = 'o' if i < 6 else 's'
    ax.errorbar(m['beta'], aR, xerr=m['beta_unc'], fmt=mk, color=col, ms=9,
                capsize=3, elinewidth=1.2, markeredgecolor='k', markeredgewidth=0.8, zorder=5)
    ax.annotate(m['name'], (m['beta'], aR), textcoords='offset points',
                xytext=(8, 6 if i%2==0 else -12), fontsize=7, fontstyle='italic')

ax.axvspan(1.5, 2.5, alpha=0.08, color='green', label='Narrow band [1.5, 2.5]')
ax.axvspan(ci95[0], ci95[1], alpha=0.10, color='C0', label=f'95% CI [{ci95[0]:.2f}, {ci95[1]:.2f}]')
ax.axvline(2.0, color='k', ls='--', lw=1.5, alpha=0.5, label=r'$\beta=2.0$')
ax.scatter([], [], marker='o', c='#4caf50', s=60, edgecolors='k', label='Materials 1-6')
ax.scatter([], [], marker='s', c='#4caf50', s=60, edgecolors='k', label='Materials 7-10 (new)')
ax.set_xlabel(r'$\beta$', fontsize=14); ax.set_ylabel(r'$\alpha_R^{(3D)}$', fontsize=14)
ax.set_title(f'ED Universality Map: {n} Materials', fontsize=14)
ax.legend(fontsize=8, loc='upper right'); ax.grid(True, alpha=0.3)
ax.set_xlim(0.8, 3.2); ax.set_ylim(0.06, 0.22)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'universality_map_10.png'), dpi=150); plt.close()
print("  Universality map saved")

# Beta bar chart
fig, ax = plt.subplots(figsize=(10, 7))
y = np.arange(n)
colors = ['#4caf50' if m['verdict']=='Confirmed' else '#ff9800' for m in all_mats]
ax.barh(y, betas_all, xerr=uncs_all, color=colors, edgecolor='k', height=0.6, capsize=3)
ax.axvline(2.0, color='k', ls='--', lw=2); ax.axvline(mean_b, color='C0', ls='-', lw=2)
ax.axvspan(ci95[0], ci95[1], alpha=0.12, color='C0')
ax.set_yticks(y); ax.set_yticklabels([m['name'] for m in all_mats], fontsize=9)
ax.set_xlabel(r'$\beta$', fontsize=14)
ax.set_title(f'All {n} Materials: Mobility Exponent', fontsize=14)
ax.set_xlim(0.5, 3.5); ax.grid(True, alpha=0.3, axis='x')
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'beta_all_10.png'), dpi=150); plt.close()
print("  Beta chart saved")

# Distribution
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(betas_all, bins=np.arange(0.8, 3.2, 0.2), color='C0', alpha=0.5, edgecolor='k')
xk = np.linspace(0.5, 3.5, 200)
kde = gaussian_kde(betas_all, bw_method=0.35)
ax.plot(xk, kde(xk)*n*0.2, 'C0-', lw=2)
ax.axvline(2.0, color='k', ls='--', lw=2); ax.axvline(mean_b, color='C1', ls='-', lw=2)
ax.axvspan(ci95[0], ci95[1], alpha=0.12, color='C1')
ax.set_xlabel(r'$\beta$', fontsize=14); ax.set_ylabel('Count', fontsize=13)
ax.set_title(f'$\\beta$ Distribution (n={n})', fontsize=14); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'beta_distribution_10.png'), dpi=150); plt.close()
print("  Distribution saved")

# ═══ Tables ═══
lines = ['# S1: New Materials\n',
         '| # | Material | Mechanism | beta | unc | R2 | Verdict |',
         '|---|----------|-----------|------|-----|-----|---------|']
for i, r in enumerate(new_results, 7):
    lines.append(f"| {i} | {r['material']} | {r['technique']} | {r['beta']:.3f} | {r['beta_unc']:.3f} | {r['R2']:.3f} | {r['verdict']} |")
with open(os.path.join(TABLES, 'S1_new_materials.md'), 'w') as f: f.write('\n'.join(lines))

lines = ['# S2: All 10 Materials\n',
         '| # | Material | beta | unc | R2 | Verdict |',
         '|---|----------|------|-----|-----|---------|']
for i, m in enumerate(all_mats, 1):
    lines.append(f"| {i} | {m['name']} | {m['beta']:.3f} | {m['beta_unc']:.3f} | {m['R2']:.3f} | {m['verdict']} |")
with open(os.path.join(TABLES, 'S2_all_10.md'), 'w') as f: f.write('\n'.join(lines))

lines = ['# S3: Updated Statistics\n', '| Stat | Value |', '|------|-------|']
for k, v in stats.items(): lines.append(f'| {k} | {v} |')
with open(os.path.join(TABLES, 'S3_statistics.md'), 'w') as f: f.write('\n'.join(lines))
print("  Tables saved")

# ═══ Summary ═══
summary = {
    'experiment': 'ED-Data-07: Next Wave (4 New Materials)',
    'date': '2026-03-31',
    'new_materials': new_results,
    'all_materials': [{'name': m['name'], 'beta': m['beta'], 'beta_unc': m['beta_unc'],
                       'R2': m['R2'], 'verdict': m['verdict']} for m in all_mats],
    'statistics': stats,
    'plots': sorted(os.listdir(PLOTS)),
    'tables': sorted(os.listdir(TABLES)),
}
with open(os.path.join(BASE, 'summary', 'final_summary.json'), 'w') as f:
    json.dump(summary, f, indent=2)

print(f"\n{'='*80}")
print(f"  ED-DATA-07 COMPLETE: {n} materials total")
print(f"{'='*80}")
print(f"  New: {len(new_results)} materials processed")
for r in new_results:
    print(f"    {r['material']:25s}: beta={r['beta']:.3f} R2={r['R2']:.3f} -> {r['verdict']}")
print(f"\n  Combined (n={n}): beta = {mean_b:.3f} +/- {std_b:.3f}")
print(f"  95% CI: [{ci95[0]:.3f}, {ci95[1]:.3f}]")
print(f"  beta=2.0 in CI: {'YES' if stats['beta2_in_CI'] else 'NO'}")
print(f"  Confirmed: {stats['confirmed']}/10  Consistent: {stats['consistent']}/10  Excluded: {stats['excluded']}/10")
