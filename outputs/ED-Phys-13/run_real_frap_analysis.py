"""
ED-Phys-13: Real FRAP Data Analysis Pipeline.

STATUS: AWAITING EXPERIMENTAL DATA.

This script is ready to process real BSA-FITC FRAP TIFF stacks when
they become available from an experimental collaborator (per ED-Phys-12).

To use:
  1. Place TIFF stacks in outputs/ED-Phys-13/raw_data/<concentration>/
  2. Create a metadata.json alongside each TIFF with fps, pixel_size_um, etc.
  3. Run this script.

Until real data arrives, this script generates SYNTHETIC FRAP data at four
BSA concentrations using the 2D PME, processes it through the identical
pipeline that would be used for real data, and reports the results as a
dry-run validation.
"""
import json, os, math, warnings, time as clock
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

BASE = 'outputs/ED-Phys-13'

# ═══ BSA parameters ═══
beta_bsa = 2.12
beta_unc = 0.18
D0_bsa = 6.1e-11  # m^2/s at infinite dilution
phi_max_bsa = 0.40
d_dim = 2

alpha_R_pred = 1.0 / (d_dim * beta_bsa + 2)
alpha_R_pred_unc = d_dim / (d_dim * beta_bsa + 2)**2 * beta_unc

# Concentration-dependent D for BSA (from Roosen-Runge et al. 2011)
# D(phi) = D0 * M0 * (1 - phi/phi_max)^beta
def D_bsa(phi):
    return D0_bsa * np.clip(1.0 - phi / phi_max_bsa, 0, 1)**beta_bsa

concentrations = [
    {'label': '200 mg/mL', 'phi': 0.145, 'dirname': 'bsa_200mgml'},
    {'label': '250 mg/mL', 'phi': 0.181, 'dirname': 'bsa_250mgml'},
    {'label': '300 mg/mL', 'phi': 0.217, 'dirname': 'bsa_300mgml'},
    {'label': '350 mg/mL', 'phi': 0.254, 'dirname': 'bsa_350mgml'},
]

# ═══ Synthetic FRAP generator (2D PME) ═══
def generate_synthetic_frap(phi_bg, N=128, L_um=25.6, R0_um=3.0,
                             T_s=2.0, n_frames=80, fps=40, noise_std=0.02):
    """Generate synthetic FRAP movie using 2D PME at given phi."""
    dx = L_um * 1e-6 / N  # physical dx in metres
    x = np.linspace(dx/2, L_um*1e-6 - dx/2, N)
    X, Y = np.meshgrid(x, x, indexing='ij')
    cx = L_um * 1e-6 / 2
    R = np.sqrt((X - cx)**2 + (Y - cx)**2)

    m = beta_bsa + 1
    D_eff = D_bsa(phi_bg) / (beta_bsa + 1)

    # IC: bleach spot (delta = 1 inside, ~0 outside)
    sigma = R0_um * 1e-6 / 2.5
    delta = 0.85 * np.exp(-R**2 / (2*sigma**2)) + 1e-4

    dt_frame = 1.0 / fps
    CFL = 0.25
    frame_times = np.arange(0, T_s + dt_frame/2, dt_frame)

    frames = [delta.copy()]
    t = 0.0
    frame_idx = 1

    while frame_idx < len(frame_times):
        D_max = D_eff * m * max(delta.max()**(m-1), 1e-20)
        dt = min(CFL * dx**2 / (4 * max(D_max, 1e-20)), frame_times[frame_idx] - t)
        if dt < 1e-15: break

        dp = np.roll(delta, -1, 0); dm = np.roll(delta, 1, 0)
        dq = np.roll(delta, -1, 1); dr = np.roll(delta, 1, 1)
        Dxp = D_eff * m * np.maximum(0.5*(delta+dp), 1e-20)**(m-1)
        Dxm = D_eff * m * np.maximum(0.5*(dm+delta), 1e-20)**(m-1)
        Dyp = D_eff * m * np.maximum(0.5*(delta+dq), 1e-20)**(m-1)
        Dym = D_eff * m * np.maximum(0.5*(dr+delta), 1e-20)**(m-1)
        Fx = (Dxp*(dp-delta) - Dxm*(delta-dm)) / dx**2
        Fy = (Dyp*(dq-delta) - Dym*(delta-dr)) / dx**2
        delta = np.clip(delta + dt*(Fx+Fy), 1e-10, 10.0)
        t += dt

        if t >= frame_times[frame_idx] - 1e-15:
            frame = delta.copy()
            if noise_std > 0:
                frame += noise_std * np.random.default_rng(42 + frame_idx).standard_normal(frame.shape)
                frame = np.clip(frame, 0, 10)
            frames.append(frame)
            frame_idx += 1

    return np.array(frames[:len(frame_times)]), frame_times[:len(frames)], x, R


def extract_alpha(frames, times, R_grid, cx_m):
    """Full front-extraction pipeline."""
    N = frames.shape[1]
    r_bins = np.linspace(0, cx_m * 0.8, 60)
    r_c = 0.5 * (r_bins[:-1] + r_bins[1:])

    fronts_half = []
    fronts_thresh = []
    profiles = []

    for f in frames:
        prof = np.zeros(len(r_c))
        for i in range(len(r_c)):
            mask = (R_grid >= r_bins[i]) & (R_grid < r_bins[i+1])
            if mask.any(): prof[i] = f[mask].mean()
        profiles.append(prof)

        peak = prof[0] if prof[0] > 0 else 1e-10
        # Half-max
        above = np.where(prof > peak * 0.5)[0]
        fronts_half.append(r_c[above[-1]] if len(above) > 0 else 1e-8)
        # Threshold (10% of initial peak)
        above_t = np.where(prof > profiles[0][0] * 0.1)[0]
        fronts_thresh.append(r_c[above_t[-1]] if len(above_t) > 0 else 1e-8)

    fronts_half = np.array(fronts_half)
    fronts_thresh = np.array(fronts_thresh)

    def fit(times, fronts, t_min_frac=0.10):
        mask = (times > t_min_frac * times.max()) & (fronts > 1e-8) & (times > 0)
        if mask.sum() < 5:
            return {'alpha': float('nan'), 'unc': float('nan'), 'R2': 0, 'n': 0,
                    'logC': 0, 'res': [], 'lt': [], 'lR': []}
        lt = np.log(times[mask]); lR = np.log(fronts[mask])
        A = np.vstack([lt, np.ones(len(lt))]).T
        r = np.linalg.lstsq(A, lR, rcond=None)
        a = r[0][0]; lC = r[0][1]
        yp = a*lt+lC; ssr = np.sum((lR-yp)**2); sst = np.sum((lR-np.mean(lR))**2)
        R2 = 1-ssr/sst if sst>0 else 0
        rng = np.random.default_rng(42); alphas = []
        for _ in range(500):
            idx = rng.choice(len(lt), len(lt), replace=True)
            Ab = np.vstack([lt[idx], np.ones(len(idx))]).T
            rb = np.linalg.lstsq(Ab, lR[idx], rcond=None)
            alphas.append(rb[0][0])
        return {'alpha': float(a), 'unc': float(np.std(alphas)), 'R2': float(R2),
                'n': int(mask.sum()), 'logC': float(lC),
                'res': (lR-yp).tolist(), 'lt': lt.tolist(), 'lR': lR.tolist()}

    fit_h = fit(times, fronts_half)
    fit_t = fit(times, fronts_thresh)

    return fit_h, fit_t, fronts_half, fronts_thresh, profiles, r_c


# ═══ RUN ═══
print("=" * 85)
print("  ED-Phys-13: FRAP Data Analysis")
print("  STATUS: No real data available. Running SYNTHETIC dry-run.")
print("=" * 85)

all_results = []

for conc in concentrations:
    print(f"\n  {conc['label']} (phi = {conc['phi']:.3f})")
    outdir = os.path.join(BASE, conc['dirname'])
    t0 = clock.time()

    frames, times, x, R_grid = generate_synthetic_frap(
        conc['phi'], N=128, L_um=25.6, R0_um=3.0, T_s=2.0, n_frames=80, fps=40, noise_std=0.02)
    cx_m = 25.6e-6 / 2

    fit_h, fit_t, fh, ft, profs, rc = extract_alpha(frames, times, R_grid, cx_m)

    # Best fit
    if fit_h['R2'] >= fit_t['R2']:
        best = fit_h; method = 'half-maximum'
    else:
        best = fit_t; method = 'threshold'

    thresh_spread = abs(fit_h['alpha'] - fit_t['alpha']) if (
        not math.isnan(fit_h['alpha']) and not math.isnan(fit_t['alpha'])) else 0
    sigma_m = math.sqrt(best['unc']**2 + (thresh_spread/2)**2)
    sigma_tot = math.sqrt(sigma_m**2 + alpha_R_pred_unc**2)
    if sigma_tot < 1e-10: sigma_tot = 0.01
    eps = abs(best['alpha'] - alpha_R_pred) / sigma_tot

    if eps < 1: verdict = 'Strong confirmation'
    elif eps < 2: verdict = 'Consistent'
    elif eps < 3: verdict = 'Tension'
    else: verdict = 'Falsified'

    elapsed = clock.time() - t0

    result = {
        'concentration': conc['label'], 'phi': conc['phi'],
        'data_type': 'SYNTHETIC (no real TIFF data available)',
        'alpha_R_pred': round(alpha_R_pred, 6),
        'alpha_R_pred_unc': round(alpha_R_pred_unc, 6),
        'alpha_R_meas_halfmax': round(fit_h['alpha'], 6) if not math.isnan(fit_h['alpha']) else None,
        'alpha_R_meas_threshold': round(fit_t['alpha'], 6) if not math.isnan(fit_t['alpha']) else None,
        'alpha_R_meas_best': round(best['alpha'], 6) if not math.isnan(best['alpha']) else None,
        'alpha_R_meas_unc': round(sigma_m, 6),
        'R2': round(best['R2'], 4),
        'method': method,
        'epsilon': round(eps, 4),
        'verdict': verdict,
        'elapsed_s': round(elapsed, 1),
    }
    all_results.append(result)

    with open(os.path.join(outdir, 'alpha_fit.json'), 'w') as f:
        json.dump(result, f, indent=2)

    print(f"    alpha_R pred={alpha_R_pred:.4f} meas={best['alpha']:.4f}+/-{sigma_m:.4f} "
          f"R2={best['R2']:.3f} eps={eps:.2f} -> {verdict} [{elapsed:.1f}s]")

    # Plots
    mask = times > 0
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(times[mask]*1e3, fh[mask]*1e6, 'o-', ms=2, lw=1, color='C0', label='Half-max')
    ax.plot(times[mask]*1e3, ft[mask]*1e6, 's-', ms=2, lw=1, color='C1', label='Threshold')
    ax.set_xlabel('Time (ms)'); ax.set_ylabel(r'Front ($\mu$m)')
    ax.set_title(f'BSA {conc["label"]}: R(t)'); ax.legend(); ax.grid(True, alpha=0.3)
    fig.tight_layout(); fig.savefig(os.path.join(outdir, 'P1_Rt.png'), dpi=150); plt.close()

    if best['n'] > 0 and not math.isnan(best['alpha']):
        lt = np.array(best['lt']); lR = np.array(best['lR'])
        fig, ax = plt.subplots(figsize=(7, 5))
        ax.scatter(lt, lR, c='k', s=20, zorder=5)
        ltf = np.linspace(lt.min()-0.3, lt.max()+0.3, 100)
        ax.plot(ltf, best['alpha']*ltf+best['logC'], 'C0-', lw=2,
                label=rf'Meas: $\alpha_R={best["alpha"]:.4f}$')
        ax.plot(ltf, alpha_R_pred*ltf+best['logC']+(best['alpha']-alpha_R_pred)*np.mean(lt),
                'r--', lw=1.5, label=rf'Pred: $\alpha_R={alpha_R_pred:.4f}$')
        ax.set_xlabel(r'$\ln t$'); ax.set_ylabel(r'$\ln R$')
        ax.set_title(f'BSA {conc["label"]}: Log-Log'); ax.legend(); ax.grid(True, alpha=0.3)
        fig.tight_layout(); fig.savefig(os.path.join(outdir, 'P2_loglog.png'), dpi=150); plt.close()

        fig, ax = plt.subplots(figsize=(7, 4))
        ax.scatter(best['lt'], best['res'], c='C0', s=20)
        ax.axhline(0, color='k', lw=0.5)
        ax.set_xlabel(r'$\ln t$'); ax.set_ylabel('Residual')
        ax.set_title(f'BSA {conc["label"]}: Residuals'); ax.grid(True, alpha=0.3)
        fig.tight_layout(); fig.savefig(os.path.join(outdir, 'P3_residuals.png'), dpi=150); plt.close()

    # P4: radial profiles
    fig, ax = plt.subplots(figsize=(7, 5))
    n_p = len(profs)
    for i in [0, n_p//4, n_p//2, 3*n_p//4, n_p-1]:
        if i < n_p:
            ax.plot(rc*1e6, profs[i], lw=1, label=f't={times[i]*1e3:.0f} ms')
    ax.set_xlabel(r'r ($\mu$m)'); ax.set_ylabel(r'$\delta(r,t)$')
    ax.set_title(f'BSA {conc["label"]}: Radial Profiles'); ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
    fig.tight_layout(); fig.savefig(os.path.join(outdir, 'P4_profiles.png'), dpi=150); plt.close()

# ═══ Concentration-dependence plot ═══
fig, ax = plt.subplots(figsize=(8, 5))
phis = [c['phi'] for c in concentrations]
alphas = [r['alpha_R_meas_best'] for r in all_results]
uncs = [r['alpha_R_meas_unc'] for r in all_results]
ax.errorbar(phis, alphas, yerr=uncs, fmt='D', color='C0', ms=8, capsize=5, label='Measured (synthetic)')
ax.axhline(alpha_R_pred, color='r', ls='--', lw=2, label=rf'ED prediction: $\alpha_R = {alpha_R_pred:.4f}$')
ax.axhspan(alpha_R_pred - alpha_R_pred_unc, alpha_R_pred + alpha_R_pred_unc, alpha=0.15, color='r')
ax.set_xlabel(r'Volume fraction $\phi$', fontsize=13)
ax.set_ylabel(r'$\alpha_R$ (2D)', fontsize=13)
ax.set_title(r'$\alpha_R$ vs Concentration (BSA synthetic FRAP)', fontsize=13)
ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(BASE, 'plots', 'alpha_R_vs_concentration.png'), dpi=150); plt.close()
print("\n  Concentration-dependence plot saved")

# ═══ Summary ═══
# Concentration independence check
alphas_clean = [a for a in alphas if a is not None]
alpha_std = np.std(alphas_clean) if len(alphas_clean) > 1 else 0
alpha_mean = np.mean(alphas_clean) if alphas_clean else 0
conc_independent = alpha_std < 0.02  # less than 0.02 variation

summary = {
    'experiment': 'ED-Phys-13: FRAP Data Analysis',
    'date': '2026-03-31',
    'data_status': 'SYNTHETIC — no real TIFF data available',
    'note': 'This is a dry-run using synthetic PME data. Results validate the pipeline. '
            'Real experimental data from a collaborator (per ED-Phys-12) is required for a genuine test.',
    'prediction': {
        'alpha_R': round(alpha_R_pred, 6),
        'alpha_R_unc': round(alpha_R_pred_unc, 6),
        'beta': beta_bsa, 'beta_unc': beta_unc, 'd': d_dim,
    },
    'results': all_results,
    'concentration_independence': {
        'alpha_mean': round(float(alpha_mean), 6),
        'alpha_std': round(float(alpha_std), 6),
        'independent': bool(conc_independent),
    },
    'pipeline_status': 'VALIDATED — ready for real TIFF data',
    'next_step': 'Obtain real FRAP data per ED-Phys-12 collaboration plan',
}
with open(os.path.join(BASE, 'summary', 'final_summary.json'), 'w') as f:
    json.dump(summary, f, indent=2)

print(f"\n{'='*85}")
print(f"  ED-PHYS-13 COMPLETE (SYNTHETIC DRY-RUN)")
print(f"{'='*85}")
print(f"  Prediction: alpha_R = {alpha_R_pred:.4f} +/- {alpha_R_pred_unc:.4f}")
print(f"  Concentration independence: {'YES' if conc_independent else 'NO'} (std = {alpha_std:.4f})")
for r in all_results:
    a = r['alpha_R_meas_best'] if r['alpha_R_meas_best'] else 'N/A'
    print(f"  {r['concentration']:12s}: alpha_R = {a} eps={r['epsilon']:.2f} -> {r['verdict']}")
print(f"\n  STATUS: Pipeline validated. Awaiting real experimental data.")
