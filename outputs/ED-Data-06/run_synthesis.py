"""ED-Data-06: Universality Synthesis Across 6 Materials."""
import json, os, warnings
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import t as t_dist, gaussian_kde
warnings.filterwarnings('ignore')

OUT = 'outputs/ED-Data-06'
PLOTS = os.path.join(OUT, 'plots')
TABLES = os.path.join(OUT, 'tables')

materials = [
    {'name': 'Hard-sphere colloids', 'beta': 1.69, 'beta_unc': 0.15, 'R2': 0.995,
     'source': 'Segre et al. 1995', 'mechanism': 'Excluded volume',
     'series': 'ED-Data-01', 'verdict': 'Confirmed'},
    {'name': 'Sucrose-water', 'beta': 2.49, 'beta_unc': 0.20, 'R2': 0.987,
     'source': 'Price et al. 2016', 'mechanism': 'H-bonding network',
     'series': 'ED-Data-05', 'verdict': 'Confirmed'},
    {'name': 'BSA protein', 'beta': 2.12, 'beta_unc': 0.18, 'R2': 0.986,
     'source': 'Roosen-Runge et al. 2011', 'mechanism': 'Hydrodynamic crowding',
     'series': 'ED-Data-08', 'verdict': 'Confirmed'},
]

for dirname in ['lysozyme', 'pmma_colloids', 'ludox_silica']:
    with open(f'outputs/ED-Data-05/{dirname}/beta_fit.json') as f:
        d = json.load(f)
    mech = {'Lysozyme': 'Short-range attraction + crowding',
            'PMMA colloids': 'Hard-sphere (steric)',
            'Ludox silica': 'Electrostatic + steric'}[d['material']]
    materials.append({
        'name': d['material'], 'beta': d['beta'], 'beta_unc': d['beta_uncertainty'],
        'R2': d['R_squared'], 'source': d['data_source'], 'mechanism': mech,
        'series': f'ED-Data-05/{dirname}', 'verdict': d['universality_verdict'],
    })

betas = np.array([m['beta'] for m in materials])
uncs = np.array([m['beta_unc'] for m in materials])
names = [m['name'] for m in materials]
n = len(betas)

mean_b = np.mean(betas)
std_b = np.std(betas, ddof=1)
se_b = std_b / np.sqrt(n)
ci95 = t_dist.interval(0.95, df=n-1, loc=mean_b, scale=se_b)
ci99 = t_dist.interval(0.99, df=n-1, loc=mean_b, scale=se_b)
w = 1.0 / uncs**2
w_mean = np.sum(w * betas) / np.sum(w)
w_unc = 1.0 / np.sqrt(np.sum(w))

stats = {
    'n_materials': n, 'mean_beta': round(float(mean_b), 4),
    'std_beta': round(float(std_b), 4), 'se_beta': round(float(se_b), 4),
    'CI_95': [round(float(ci95[0]), 4), round(float(ci95[1]), 4)],
    'CI_99': [round(float(ci99[0]), 4), round(float(ci99[1]), 4)],
    'weighted_mean': round(float(w_mean), 4), 'weighted_unc': round(float(w_unc), 4),
    'beta_2_in_CI95': bool(ci95[0] <= 2.0 <= ci95[1]),
    'range': [round(float(betas.min()), 4), round(float(betas.max()), 4)],
    'narrow_band_count': int(np.sum((betas >= 1.5) & (betas <= 2.5))),
    'broad_band_count': int(np.sum((betas >= 1.0) & (betas <= 3.5))),
}

print("Combined statistics:")
for k, v in stats.items(): print(f"  {k}: {v}")

# P1: Beta bar chart
fig, ax = plt.subplots(figsize=(9, 6))
y = np.arange(n)
colors = ['#4caf50' if m['verdict'] == 'Confirmed' else '#ff9800' for m in materials]
ax.barh(y, betas, xerr=uncs, color=colors, edgecolor='k', height=0.6, capsize=4)
ax.axvline(2.0, color='k', ls='--', lw=2, label=r'$\beta=2.0$')
ax.axvline(mean_b, color='C0', ls='-', lw=2, label=f'Mean={mean_b:.2f}')
ax.axvspan(ci95[0], ci95[1], alpha=0.15, color='C0', label=f'95% CI')
ax.axvspan(1.5, 2.5, alpha=0.08, color='green', label='[1.5, 2.5]')
ax.set_yticks(y)
ax.set_yticklabels([f"{m['name']}\n({m['mechanism']})" for m in materials], fontsize=9)
ax.set_xlabel(r'$\beta$', fontsize=14)
ax.set_title(r'$\beta$ Across 6 Materials', fontsize=14)
ax.legend(fontsize=9, loc='lower right'); ax.set_xlim(0.5, 3.5); ax.grid(True, alpha=0.3, axis='x')
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P1_beta_values.png'), dpi=150); plt.close()
print("  P1")

# P2: Distribution
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(betas, bins=np.arange(0.8, 3.2, 0.2), color='C0', alpha=0.5, edgecolor='k')
x_kde = np.linspace(0.5, 3.5, 200)
kde = gaussian_kde(betas, bw_method=0.4)
ax.plot(x_kde, kde(x_kde)*n*0.2, 'C0-', lw=2, label='KDE')
ax.axvline(2.0, color='k', ls='--', lw=2, label=r'$\beta=2.0$')
ax.axvline(mean_b, color='C1', ls='-', lw=2, label=f'Mean={mean_b:.2f}')
ax.axvspan(ci95[0], ci95[1], alpha=0.15, color='C1', label='95% CI')
ax.set_xlabel(r'$\beta$', fontsize=14); ax.set_ylabel('Count', fontsize=13)
ax.set_title(r'$\beta$ Distribution (n=6)', fontsize=14)
ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P2_beta_distribution.png'), dpi=150); plt.close()
print("  P2")

# P3: Universality map
fig, ax = plt.subplots(figsize=(9, 7))
b_c = np.linspace(0.5, 4.0, 200)
ax.plot(b_c, 1.0/(3*b_c+2), 'k-', lw=2.5, label=r'$\alpha_R = 1/(3\beta+2)$')
for i, m in enumerate(materials):
    aR = 1.0/(3*m['beta']+2)
    col = '#4caf50' if m['verdict'] == 'Confirmed' else '#ff9800'
    mk = 'o' if i < 3 else 'D'
    ax.errorbar(m['beta'], aR, xerr=m['beta_unc'], fmt=mk, color=col, ms=10,
                capsize=4, elinewidth=1.5, markeredgecolor='k', markeredgewidth=1, zorder=5)
    ax.annotate(m['name'], (m['beta'], aR), textcoords='offset points',
                xytext=(10, 8 if i%2==0 else -14), fontsize=8, fontstyle='italic')
ax.axvspan(1.5, 2.5, alpha=0.08, color='green')
ax.scatter([], [], marker='o', c='#4caf50', s=80, edgecolors='k', label='Original (Confirmed)')
ax.scatter([], [], marker='D', c='#4caf50', s=80, edgecolors='k', label='New: Confirmed')
ax.scatter([], [], marker='D', c='#ff9800', s=80, edgecolors='k', label='New: Consistent')
ax.set_xlabel(r'$\beta$', fontsize=14); ax.set_ylabel(r'$\alpha_R^{(3D)}$', fontsize=14)
ax.set_title('ED Universality Map: 6 Materials', fontsize=13)
ax.legend(fontsize=9, loc='upper right'); ax.grid(True, alpha=0.3)
ax.set_xlim(0.8, 3.2); ax.set_ylim(0.06, 0.22)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P3_universality_map.png'), dpi=150); plt.close()
print("  P3")

# P4: R2 quality
fig, ax = plt.subplots(figsize=(8, 4))
r2s = [m['R2'] for m in materials]
ax.barh(np.arange(n), r2s, color=['#4caf50' if r>0.99 else '#ff9800' for r in r2s],
        edgecolor='k', height=0.6)
ax.axvline(0.95, color='r', ls='--', lw=1.5, label='Threshold')
ax.set_yticks(np.arange(n)); ax.set_yticklabels(names, fontsize=9)
ax.set_xlabel('$R^2$', fontsize=13); ax.set_title('Fit Quality', fontsize=13)
ax.set_xlim(0.9, 1.0); ax.legend(); ax.grid(True, alpha=0.3, axis='x')
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P4_R2_quality.png'), dpi=150); plt.close()
print("  P4")

# Tables
lines = ['# S1: All Beta Values\n',
         '| # | Material | Mechanism | beta | unc | R2 | Verdict |',
         '|---|----------|-----------|------|-----|-----|---------|']
for i, m in enumerate(materials, 1):
    lines.append(f"| {i} | {m['name']} | {m['mechanism']} | {m['beta']:.3f} | {m['beta_unc']:.3f} | {m['R2']:.3f} | {m['verdict']} |")
with open(os.path.join(TABLES, 'S1_all_betas.md'), 'w') as f: f.write('\n'.join(lines))

lines = ['# S2: Combined Statistics\n', '| Statistic | Value |', '|-----------|-------|']
for k, v in stats.items(): lines.append(f'| {k} | {v} |')
with open(os.path.join(TABLES, 'S2_statistics.md'), 'w') as f: f.write('\n'.join(lines))

lines = ['# S3: Classification\n',
         '| Material | beta | Narrow band? | R2>0.95? | Verdict |',
         '|----------|------|-------------|----------|---------|']
for m in materials:
    lines.append(f"| {m['name']} | {m['beta']:.3f} | {'Yes' if 1.5<=m['beta']<=2.5 else 'No'} | {'Yes' if m['R2']>0.95 else 'No'} | {m['verdict']} |")
with open(os.path.join(TABLES, 'S3_classification.md'), 'w') as f: f.write('\n'.join(lines))
print("  Tables saved")

summary = {
    'experiment': 'ED-Data-06: Universality Synthesis',
    'date': '2026-03-31',
    'materials': materials,
    'statistics': stats,
    'plots': sorted(os.listdir(PLOTS)),
    'tables': sorted(os.listdir(TABLES)),
}
with open(os.path.join(OUT, 'summary', 'final_summary.json'), 'w') as f:
    json.dump(summary, f, indent=2)
print(f"\n  Summary saved")
