"""
ED-Phys-09 v2: Experimental Front-Propagation Extraction.

Fix: Use a compact bump IC (Gaussian) instead of step boundary.
The step boundary produces error-function spreading (no sharp front).
A localised bump with D(c) that vanishes at c=0 produces compact fronts.

We solve dc/dt = d/dx[D(c) dc/dx] where D(c) from published data,
with a Gaussian bump IC. The key physics: D(c) -> 0 as c -> c_max means
the *complementary* variable delta = c_max - c has D(delta) -> 0 as delta -> 0.
We set up a bump in delta (i.e., a dip in c away from c_max), which
produces a PME-like spreading front.
"""
import json, os, warnings, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

BASE = 'outputs/ED-Phys-09'

materials = {
    'sucrose': {
        'name': 'Sucrose-water', 'beta': 2.49, 'beta_unc': 0.20,
        'phi_max': 0.85, 'D0': 5.2e-10,
        'source': 'Vergara et al. 2001',
        # D(phi) from published data (phi = volume fraction of sucrose)
        'phi_data':  [0.00, 0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80],
        'D_data':    [5.2e-10, 4.7e-10, 4.1e-10, 3.1e-10, 2.2e-10, 1.4e-10, 8.5e-11, 4.2e-11, 1.5e-11, 2.5e-12],
    },
    'peg_water': {
        'name': 'PEG-water (6 kDa)', 'beta': 1.297, 'beta_unc': 0.054,
        'phi_max': 0.55, 'D0': 8.5e-11,
        'source': 'Vergara et al. 2001',
        'phi_data':  [0.00, 0.02, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50],
        'D_data':    [8.5e-11, 8.3e-11, 7.7e-11, 6.7e-11, 5.6e-11, 4.5e-11, 3.5e-11, 2.6e-11, 1.8e-11, 1.1e-11, 5.5e-12, 1.8e-12],
    },
    'glycerol_water': {
        'name': 'Glycerol-water', 'beta': 1.741, 'beta_unc': 0.034,
        'phi_max': 1.0, 'D0': 1.06e-9,
        'source': "D'Errico et al. 2004",
        'phi_data':  [0.00, 0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90],
        'D_data':    [1.06e-9, 1.00e-9, 9.2e-10, 7.6e-10, 6.0e-10, 4.6e-10, 3.2e-10, 2.1e-10, 1.3e-10, 6.4e-11, 2.1e-11],
    },
}


def D_from_data(c, c_max, phi_data, D_data):
    """Compute D at concentration c using interpolation of experimental D(phi)."""
    phi = np.clip(c / c_max, 0, 0.9999) * c_max
    return np.interp(phi, phi_data, D_data, left=D_data[0], right=max(D_data[-1], 1e-15))


def solve_bump_diffusion(phi_data, D_data, c_max, D0,
                          N=2000, L=0.02, T=14400.0, n_snaps=60):
    """
    Solve dc/dt = d/dx[D(c) dc/dx] with a Gaussian bump IC.
    c(x,0) = c_max - A * exp(-x^2/(2*sigma^2))
    where A controls the depth of the concentration dip.

    The front is where c drops below c_max - threshold.
    """
    dx = L / N
    x = np.linspace(-L/2 + dx/2, L/2 - dx/2, N)

    A = 0.3 * c_max  # 30% dip
    sigma = L / 20    # narrow initial bump

    # IC: background at c_max minus a Gaussian dip
    c = c_max - A * np.exp(-x**2 / (2 * sigma**2))
    c = np.clip(c, 0, c_max * 0.9999)

    # The complementary variable delta = c_max - c is the bump
    # delta(x,0) = A * exp(-x^2/(2*sigma^2))
    # D(delta) ~ D0 * (delta/c_max)^beta_effective

    snap_dt = T / n_snaps
    D_max = D0
    dt = 0.3 * dx**2 / (2 * D_max)

    times = [0.0]
    fronts_list = []

    # Measure initial front (half-max of delta bump)
    delta = c_max - c
    delta_max = delta.max()
    threshold = delta_max * 0.1  # 10% of peak
    mask = delta > threshold
    R0 = x[mask].max() if mask.any() else 0
    fronts_list.append(max(R0, 1e-8))

    t = 0.0; next_snap = snap_dt

    for step in range(int(T / dt) + 1):
        c_r = np.roll(c, -1); c_l = np.roll(c, 1)
        D_r = D_from_data(0.5*(c+c_r), c_max, phi_data, D_data)
        D_l = D_from_data(0.5*(c_l+c), c_max, phi_data, D_data)

        flux = (D_r*(c_r - c)/dx - D_l*(c - c_l)/dx) / dx
        c = np.clip(c + dt * flux, 0, c_max * 0.9999)
        t += dt

        if t >= next_snap:
            delta = c_max - c
            d_peak = delta[N//2]
            thresh_now = max(d_peak * 0.1, threshold * 0.5)
            mask = delta > thresh_now
            R = x[mask].max() if mask.any() else fronts_list[-1]
            times.append(t)
            fronts_list.append(max(R, 1e-8))
            next_snap += snap_dt

        if t >= T: break

    return np.array(times), np.array(fronts_list)


def fit_alpha(times, fronts, t_min_frac=0.15):
    mask = (times > t_min_frac * times.max()) & (fronts > 1e-7) & (times > 0)
    if mask.sum() < 5:
        return {'alpha': float('nan'), 'alpha_unc': float('nan'), 'R2': 0, 'n': 0,
                'logC': 0, 'residuals': [], 'lt': [], 'lR': []}
    lt = np.log(times[mask]); lR = np.log(fronts[mask])
    A = np.vstack([lt, np.ones(len(lt))]).T
    res = np.linalg.lstsq(A, lR, rcond=None)
    alpha = res[0][0]; logC = res[0][1]
    y_pred = alpha*lt + logC
    SS_r = np.sum((lR-y_pred)**2); SS_t = np.sum((lR-np.mean(lR))**2)
    R2 = 1 - SS_r/SS_t if SS_t > 0 else 0
    rng = np.random.default_rng(42); n = len(lt); alphas = []
    for _ in range(1000):
        idx = rng.choice(n, n, replace=True)
        Ab = np.vstack([lt[idx], np.ones(len(idx))]).T
        rb = np.linalg.lstsq(Ab, lR[idx], rcond=None)
        alphas.append(rb[0][0])
    return {'alpha': float(alpha), 'alpha_unc': float(np.std(alphas)), 'R2': float(R2),
            'n': int(n), 'logC': float(logC), 'residuals': (lR-y_pred).tolist(),
            'lt': lt.tolist(), 'lR': lR.tolist()}


def alpha_pred(beta, beta_unc, d=1):
    aR = 1.0/(d*beta+2); daR = d/(d*beta+2)**2 * beta_unc
    return aR, daR

def classify(a_m, a_p, s_m, s_p):
    s = math.sqrt(s_m**2 + s_p**2)
    if s < 1e-10: s = 0.01
    e = abs(a_m - a_p) / s
    if e < 1: return 'Strong confirmation', e
    elif e < 2: return 'Consistent', e
    elif e < 3: return 'Tension', e
    else: return 'Falsified', e

print("=" * 85)
print("  ED-Phys-09 v2: Experimental Front Extraction (bump IC, real D(c))")
print("=" * 85)

all_results = []
for dirname, mat in materials.items():
    print(f"\n  {mat['name']} (beta={mat['beta']:.3f})")
    outdir = os.path.join(BASE, dirname)

    aR_p, aR_pu = alpha_pred(mat['beta'], mat['beta_unc'], d=1)

    times, fronts = solve_bump_diffusion(
        mat['phi_data'], mat['D_data'], mat['phi_max'], mat['D0'],
        N=2000, L=0.02, T=14400.0, n_snaps=60)

    fit = fit_alpha(times, fronts)
    sigma_m = fit['alpha_unc'] if not math.isnan(fit['alpha_unc']) else 0.05

    if math.isnan(fit['alpha']):
        verdict, epsilon = 'No data', float('nan')
    else:
        verdict, epsilon = classify(fit['alpha'], aR_p, sigma_m, aR_pu)

    result = {
        'material': mat['name'], 'beta': mat['beta'], 'beta_unc': mat['beta_unc'],
        'alpha_R_pred': round(aR_p, 6), 'alpha_R_pred_unc': round(aR_pu, 6),
        'alpha_R_meas': round(fit['alpha'], 6) if not math.isnan(fit['alpha']) else None,
        'alpha_R_meas_unc': round(sigma_m, 6),
        'R2': round(fit['R2'], 4), 'n_points': fit['n'],
        'epsilon': round(epsilon, 4) if not math.isnan(epsilon) else None,
        'verdict': verdict, 'source': mat['source'],
        'method': 'Nonlinear diffusion with experimental D(c), bump IC',
    }
    all_results.append(result)
    with open(os.path.join(outdir, 'alpha_fit.json'), 'w') as f:
        json.dump(result, f, indent=2)

    a_str = f"{fit['alpha']:.4f}" if not math.isnan(fit['alpha']) else "N/A"
    e_str = f"{epsilon:.2f}" if not math.isnan(epsilon) else "N/A"
    print(f"    pred={aR_p:.4f} meas={a_str} R2={fit['R2']:.4f} eps={e_str} -> {verdict}")

    # Plots
    mask = times > 0
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(times[mask], fronts[mask]*1e3, 'o-', ms=3, lw=1, color='C0')
    ax.set_xlabel('Time (s)'); ax.set_ylabel('Front (mm)')
    ax.set_title(f'{mat["name"]}: Front (exp D(c))'); ax.grid(True, alpha=0.3)
    fig.tight_layout(); fig.savefig(os.path.join(outdir, 'P1_Rt.png'), dpi=150); plt.close()

    if fit['n'] > 0 and not math.isnan(fit['alpha']):
        fig, ax = plt.subplots(figsize=(7, 5))
        lt = np.array(fit['lt']); lR = np.array(fit['lR'])
        ax.scatter(lt, lR, c='k', s=30, zorder=5)
        lt_f = np.linspace(lt.min()-0.3, lt.max()+0.3, 100)
        ax.plot(lt_f, fit['alpha']*lt_f+fit['logC'], 'C0-', lw=2,
                label=rf'$\alpha_R={fit["alpha"]:.4f}$')
        ax.plot(lt_f, aR_p*lt_f+fit['logC']+(fit['alpha']-aR_p)*np.mean(lt),
                'r--', lw=1.5, label=rf'Pred={aR_p:.4f}')
        ax.set_xlabel(r'$\ln t$'); ax.set_ylabel(r'$\ln R$')
        ax.set_title(f'{mat["name"]}: Log-Log (exp)'); ax.legend(); ax.grid(True, alpha=0.3)
        fig.tight_layout(); fig.savefig(os.path.join(outdir, 'P2_loglog.png'), dpi=150); plt.close()

        fig, ax = plt.subplots(figsize=(7, 4))
        ax.scatter(fit['lt'], fit['residuals'], c='C0', s=30)
        ax.axhline(0, color='k', lw=0.5)
        ax.set_xlabel(r'$\ln t$'); ax.set_ylabel('Residual')
        ax.set_title(f'{mat["name"]}: Residuals'); ax.grid(True, alpha=0.3)
        fig.tight_layout(); fig.savefig(os.path.join(outdir, 'P3_residuals.png'), dpi=150); plt.close()

# Comparison
fig, ax = plt.subplots(figsize=(8, 6))
x_pos = np.arange(len(all_results))
preds = [r['alpha_R_pred'] for r in all_results]
meass = [r['alpha_R_meas'] if r['alpha_R_meas'] else 0 for r in all_results]
pu = [r['alpha_R_pred_unc'] for r in all_results]
mu = [r['alpha_R_meas_unc'] for r in all_results]
ax.errorbar(x_pos-0.12, preds, yerr=pu, fmt='s', color='C0', ms=10, capsize=5, label='ED prediction')
ax.errorbar(x_pos+0.12, meass, yerr=mu, fmt='D', color='C3', ms=10, capsize=5, label='Experimental D(c)')
ax.set_xticks(x_pos); ax.set_xticklabels([r['material'] for r in all_results], fontsize=9)
ax.set_ylabel(r'$\alpha_R$ (1D)', fontsize=14)
ax.set_title(r'ED Prediction vs Experimental $\alpha_R$', fontsize=14)
ax.legend(fontsize=11); ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(BASE, 'plots', 'alpha_R_comparison_v2.png'), dpi=150); plt.close()

summary = {
    'experiment': 'ED-Phys-09 v2: Experimental Front Extraction',
    'date': '2026-03-31',
    'method': 'Nonlinear diffusion with experimental D(c), bump IC, front tracking',
    'materials': all_results,
}
with open(os.path.join(BASE, 'summary', 'final_summary.json'), 'w') as f:
    json.dump(summary, f, indent=2)

print("\n" + "=" * 85)
print("  ED-PHYS-09 v2 COMPLETE")
print("=" * 85)
for r in all_results:
    a_str = f"{r['alpha_R_meas']:.4f}" if r['alpha_R_meas'] else "N/A"
    e_str = f"{r['epsilon']:.2f}" if r['epsilon'] else "N/A"
    print(f"  {r['material']:25s}: pred={r['alpha_R_pred']:.4f} meas={a_str} eps={e_str} -> {r['verdict']}")
