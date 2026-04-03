"""
ED-Phys-11: Synthetic FRAP Simulation.

Solve the 2D PME in the delta variable:
    dt delta = D_pme * div[ m * delta^(m-1) * grad(delta) ]
            = D_pme * div[ grad(delta^m) / ... ]
            = D_pme * laplacian(delta^m) / m   (for radially symmetric)

Simplified: dt delta = D_eff * div(delta^(m-1) * grad(delta))
where m = beta + 1, D_eff = D_pme * m.

IC: FRAP geometry
    delta = delta_max * (1 - bleach_profile)
    bleach_profile = exp(-r^2 / (2*sigma^2)) with depth > 80%
    So delta(r<R0) ~ 0 (bleached, dense), delta(r>R0) ~ delta_max (unbleached)

Wait — we need to think carefully about the FRAP mapping:
  - Physical fluorescence: F = F_max at unbleached, F ~ 0 at bleached
  - delta = F_max - F = fluorescence DEFICIT
  - In the dense background: F = F_max, delta = 0
  - In the bleached spot: F ~ 0, delta ~ F_max

So the FRAP IC is: delta is LARGE inside the bleach spot, SMALL outside.
This is a standard Barenblatt bump — exactly the geometry ED-SIM uses.

The front = boundary of the bleach spot = where delta drops to threshold.
The front EXPANDS as the bleach spot spreads (delta bump spreading).
alpha_R = 1/(d*beta + 2) for this spreading.
"""
import json, os, math, warnings, time as clock
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

BASE = 'outputs/ED-Phys-11'

# ═══ Parameters ═══
beta = 2.12       # BSA
m = beta + 1      # PME exponent = 3.12
D0_phys = 6.1e-11 # m^2/s (BSA self-diffusion)
M0 = 1.0
D_pme = D0_phys * M0 / (beta + 1)  # effective PME diffusivity

# Grid
N = 256
L_phys = 51.2e-6  # 51.2 um domain
dx = L_phys / N    # 0.2 um
x = np.linspace(dx/2, L_phys - dx/2, N)
y = np.linspace(dx/2, L_phys - dx/2, N)
X, Y = np.meshgrid(x, y, indexing='ij')
cx, cy = L_phys/2, L_phys/2
R_grid = np.sqrt((X - cx)**2 + (Y - cy)**2)

# Bleach spot
R0 = 3.0e-6       # 3 um radius
sigma_bleach = R0 / 2.5  # Gaussian width

# Time
T_final = 1.5     # seconds
n_snaps = 80

# Predicted alpha_R
d_dim = 2
alpha_R_pred = 1.0 / (d_dim * beta + 2)
sigma_alpha_pred = d_dim / (d_dim * beta + 2)**2 * 0.18  # from beta_unc = 0.18

print("=" * 80)
print("  ED-Phys-11: Synthetic FRAP Simulation (2D PME)")
print("=" * 80)
print(f"  beta = {beta}, m = {m:.2f}")
print(f"  D_pme = {D_pme:.3e} m^2/s")
print(f"  Grid: {N}x{N}, dx = {dx*1e6:.2f} um")
print(f"  Bleach spot: R0 = {R0*1e6:.1f} um")
print(f"  T_final = {T_final} s")
print(f"  alpha_R_pred = {alpha_R_pred:.4f} +/- {sigma_alpha_pred:.4f}")

# ═══ Initial condition ═══
# delta = fluorescence deficit. Large in bleach spot, zero outside.
# Gaussian bleach: delta = A * exp(-r^2 / (2*sigma^2))
A = 1.0  # normalised maximum deficit
delta = A * np.exp(-R_grid**2 / (2 * sigma_bleach**2))
# Ensure compact-ish support: clip very small values
delta = np.where(delta > 1e-6, delta, 1e-6)

print(f"  IC: Gaussian bleach, peak delta = {delta.max():.4f}")

# ═══ Solver ═══
# PME: dt(delta) = D_pme * div[ m * delta^(m-1) * grad(delta) ]
#               = D_pme * laplacian(delta^m)    (since div(grad(delta^m)) = m*div(delta^(m-1)*grad(delta)))
# Actually: laplacian(delta^m) = m*(m-1)*delta^(m-2)*|grad(delta)|^2 + m*delta^(m-1)*laplacian(delta)
# Conservative form is better: flux F = D_pme * m * delta^(m-1) * grad(delta)

snap_dt = T_final / n_snaps
CFL = 0.25

# Storage
snap_times = []
front_half = []    # half-maximum front
front_thresh = []  # threshold front
radial_profiles = []

# Pre-compute radial bins for averaging
r_bins = np.linspace(0, L_phys/2 * 0.8, 100)
r_centres = 0.5 * (r_bins[:-1] + r_bins[1:])

def radial_average(field):
    """Azimuthal average."""
    prof = np.zeros(len(r_centres))
    for i in range(len(r_centres)):
        mask = (R_grid >= r_bins[i]) & (R_grid < r_bins[i+1])
        if mask.any():
            prof[i] = field[mask].mean()
    return prof

def measure_front(delta_field, threshold_frac=0.5):
    """Measure front radius at given fraction of peak."""
    prof = radial_average(delta_field)
    peak = prof[0] if prof[0] > 0 else delta_field.max()
    thresh = threshold_frac * peak
    above = np.where(prof > thresh)[0]
    if len(above) > 0:
        return r_centres[above[-1]]
    return 0.0

# Record IC
snap_times.append(0.0)
front_half.append(measure_front(delta, 0.5))
front_thresh.append(measure_front(delta, 0.1))
radial_profiles.append(radial_average(delta))

t = 0.0
step = 0
next_snap = snap_dt
t_start = clock.time()

print("\n  Running simulation...")

while t < T_final:
    # Adaptive dt
    D_max = D_pme * m * max(delta.max()**(m-1), 1e-20)
    dt = CFL * dx**2 / (4 * max(D_max, 1e-20))  # factor 4 for 2D
    dt = min(dt, next_snap - t, T_final - t)
    if dt < 1e-15:
        break

    # Conservative finite-difference PME flux
    # F_x = D_pme * m * delta^(m-1) * d(delta)/dx at faces
    delta_xp = np.roll(delta, -1, axis=0)
    delta_xm = np.roll(delta, 1, axis=0)
    delta_yp = np.roll(delta, -1, axis=1)
    delta_ym = np.roll(delta, 1, axis=1)

    # Face values (arithmetic mean)
    d_xp = 0.5 * (delta + delta_xp)
    d_xm = 0.5 * (delta_xm + delta)
    d_yp = 0.5 * (delta + delta_yp)
    d_ym = 0.5 * (delta_ym + delta)

    # Diffusivity at faces: D_pme * m * delta^(m-1)
    Dx_p = D_pme * m * np.maximum(d_xp, 1e-20)**(m-1)
    Dx_m = D_pme * m * np.maximum(d_xm, 1e-20)**(m-1)
    Dy_p = D_pme * m * np.maximum(d_yp, 1e-20)**(m-1)
    Dy_m = D_pme * m * np.maximum(d_ym, 1e-20)**(m-1)

    # Flux divergence
    Fx = (Dx_p * (delta_xp - delta) - Dx_m * (delta - delta_xm)) / dx**2
    Fy = (Dy_p * (delta_yp - delta) - Dy_m * (delta - delta_ym)) / dx**2

    delta_new = delta + dt * (Fx + Fy)
    delta_new = np.clip(delta_new, 1e-10, 10.0)

    delta = delta_new
    t += dt
    step += 1

    if t >= next_snap - 1e-15:
        snap_times.append(t)
        front_half.append(measure_front(delta, 0.5))
        front_thresh.append(measure_front(delta, 0.1))
        radial_profiles.append(radial_average(delta))
        next_snap += snap_dt

elapsed = clock.time() - t_start
print(f"  Done: {step} steps in {elapsed:.1f}s")

snap_times = np.array(snap_times)
front_half = np.array(front_half)
front_thresh = np.array(front_thresh)

# ═══ Save fields ═══
outdir = os.path.join(BASE, 'sim_bsa_frap')
np.savez_compressed(os.path.join(outdir, 'data.npz'),
    snap_times=snap_times, front_half=front_half, front_thresh=front_thresh,
    r_centres=r_centres, radial_profiles=np.array(radial_profiles))

# ═══ Front extraction ═══
def fit_alpha(times, fronts, t_min_frac=0.10):
    mask = (times > t_min_frac * times.max()) & (fronts > 1e-8) & (times > 0)
    if mask.sum() < 5:
        return {'alpha': float('nan'), 'alpha_unc': float('nan'), 'R2': 0,
                'n': 0, 'logC': 0, 'residuals': [], 'lt': [], 'lR': []}
    lt = np.log(times[mask]); lR = np.log(fronts[mask])
    A_mat = np.vstack([lt, np.ones(len(lt))]).T
    res = np.linalg.lstsq(A_mat, lR, rcond=None)
    alpha = res[0][0]; logC = res[0][1]
    y_pred = alpha * lt + logC
    SS_r = np.sum((lR - y_pred)**2); SS_t = np.sum((lR - np.mean(lR))**2)
    R2 = 1 - SS_r / SS_t if SS_t > 0 else 0
    residuals = (lR - y_pred).tolist()
    rng = np.random.default_rng(42); n = len(lt); alphas = []
    for _ in range(1000):
        idx = rng.choice(n, n, replace=True)
        Ab = np.vstack([lt[idx], np.ones(len(idx))]).T
        rb = np.linalg.lstsq(Ab, lR[idx], rcond=None)
        alphas.append(rb[0][0])
    return {'alpha': float(alpha), 'alpha_unc': float(np.std(alphas)), 'R2': float(R2),
            'n': int(n), 'logC': float(logC), 'residuals': residuals,
            'lt': lt.tolist(), 'lR': lR.tolist()}

fit_h = fit_alpha(snap_times, front_half)
fit_t = fit_alpha(snap_times, front_thresh)

# Use the better fit
if fit_h['R2'] >= fit_t['R2']:
    fit_best = fit_h; method = 'half-maximum'
else:
    fit_best = fit_t; method = 'threshold (10%)'

# Threshold sensitivity
thresh_spread = abs(fit_h['alpha'] - fit_t['alpha']) if (
    not math.isnan(fit_h['alpha']) and not math.isnan(fit_t['alpha'])) else 0
sigma_meas = math.sqrt(fit_best['alpha_unc']**2 + (thresh_spread/2)**2)

# Classification
sigma_tot = math.sqrt(sigma_meas**2 + sigma_alpha_pred**2)
if sigma_tot < 1e-10: sigma_tot = 0.01
epsilon = abs(fit_best['alpha'] - alpha_R_pred) / sigma_tot
if epsilon < 1: verdict = 'Strong confirmation'
elif epsilon < 2: verdict = 'Consistent'
elif epsilon < 3: verdict = 'Tension'
else: verdict = 'Falsified'

print(f"\n  Front extraction ({method}):")
print(f"    alpha_R_pred  = {alpha_R_pred:.4f} +/- {sigma_alpha_pred:.4f}")
print(f"    alpha_R_meas  = {fit_best['alpha']:.4f} +/- {sigma_meas:.4f}")
print(f"    R^2           = {fit_best['R2']:.4f}")
print(f"    epsilon       = {epsilon:.2f}")
print(f"    verdict       = {verdict}")
print(f"    half-max alpha  = {fit_h['alpha']:.4f}")
print(f"    threshold alpha = {fit_t['alpha']:.4f}")

# ═══ Save result ═══
result = {
    'material': 'BSA (synthetic FRAP)',
    'beta': beta, 'beta_unc': 0.18, 'd': d_dim,
    'alpha_R_pred': round(alpha_R_pred, 6),
    'alpha_R_pred_unc': round(sigma_alpha_pred, 6),
    'alpha_R_meas': round(fit_best['alpha'], 6),
    'alpha_R_meas_unc': round(sigma_meas, 6),
    'alpha_R_halfmax': round(fit_h['alpha'], 6) if not math.isnan(fit_h['alpha']) else None,
    'alpha_R_threshold': round(fit_t['alpha'], 6) if not math.isnan(fit_t['alpha']) else None,
    'R2': round(fit_best['R2'], 4),
    'n_points': fit_best['n'],
    'epsilon': round(epsilon, 4),
    'verdict': verdict,
    'method': method,
    'grid': f'{N}x{N}', 'dx_um': round(dx*1e6, 2),
    'R0_um': round(R0*1e6, 1),
    'T_final_s': T_final,
    'steps': step, 'elapsed_s': round(elapsed, 1),
}
with open(os.path.join(outdir, 'alpha_fit.json'), 'w') as f:
    json.dump(result, f, indent=2)

# ═══ Plots ═══
PLOTS = os.path.join(BASE, 'plots')

# P1: R(t) vs t
fig, ax = plt.subplots(figsize=(7, 5))
mask = snap_times > 0
ax.plot(snap_times[mask]*1e3, front_half[mask]*1e6, 'o-', ms=3, lw=1, color='C0', label='Half-max front')
ax.plot(snap_times[mask]*1e3, front_thresh[mask]*1e6, 's-', ms=3, lw=1, color='C1', label='10% threshold')
ax.set_xlabel('Time (ms)', fontsize=13); ax.set_ylabel(r'Front radius ($\mu$m)', fontsize=13)
ax.set_title('BSA Synthetic FRAP: Front Propagation', fontsize=13)
ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P1_Rt.png'), dpi=150); plt.close()

# P2: log-log with fit
fig, ax = plt.subplots(figsize=(7, 5))
if fit_best['n'] > 0:
    lt = np.array(fit_best['lt']); lR = np.array(fit_best['lR'])
    ax.scatter(lt, lR, c='k', s=30, zorder=5, label='Data')
    lt_f = np.linspace(lt.min()-0.5, lt.max()+0.5, 100)
    ax.plot(lt_f, fit_best['alpha']*lt_f + fit_best['logC'], 'C0-', lw=2,
            label=rf'Measured: $\alpha_R = {fit_best["alpha"]:.4f}$')
    ax.plot(lt_f, alpha_R_pred*lt_f + fit_best['logC'] + (fit_best['alpha']-alpha_R_pred)*np.mean(lt),
            'r--', lw=1.5, label=rf'Predicted: $\alpha_R = {alpha_R_pred:.4f}$')
ax.set_xlabel(r'$\ln\,t$ (s)', fontsize=13); ax.set_ylabel(r'$\ln\,R$ (m)', fontsize=13)
ax.set_title('Log-Log Front Fit (Synthetic FRAP)', fontsize=13)
ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P2_loglog.png'), dpi=150); plt.close()

# P3: residuals
fig, ax = plt.subplots(figsize=(7, 4))
if fit_best['n'] > 0:
    ax.scatter(fit_best['lt'], fit_best['residuals'], c='C0', s=30)
ax.axhline(0, color='k', ls='-', lw=0.5)
ax.set_xlabel(r'$\ln\,t$', fontsize=13); ax.set_ylabel('Residual', fontsize=13)
ax.set_title('Fit Residuals', fontsize=13); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P3_residuals.png'), dpi=150); plt.close()

# P4: radial profile snapshots
fig, ax = plt.subplots(figsize=(8, 5))
n_prof = len(radial_profiles)
for i in [0, n_prof//5, 2*n_prof//5, 3*n_prof//5, 4*n_prof//5, n_prof-1]:
    if i < n_prof:
        ax.plot(r_centres*1e6, radial_profiles[i], lw=1.2,
                label=f't = {snap_times[i]*1e3:.0f} ms')
ax.set_xlabel(r'Radius ($\mu$m)', fontsize=13); ax.set_ylabel(r'$\delta(r,t)$', fontsize=13)
ax.set_title('Radial Profiles (Synthetic FRAP)', fontsize=13)
ax.legend(fontsize=9); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P4_radial_profiles.png'), dpi=150); plt.close()

print("  Plots saved")

# ═══ Summary ═══
summary = {
    'experiment': 'ED-Phys-11: Synthetic FRAP Simulation',
    'date': '2026-03-31',
    'pde': '2D PME in delta variable (fluorescence deficit)',
    'result': result,
    'notes': [
        'IC: Gaussian bleach spot (R0=3um) in delta variable',
        'PME with m = beta+1 = 3.12, D_pme = D0/(beta+1)',
        'Front tracked via half-maximum and 10% threshold',
        'This validates the measurement pipeline for real FRAP data',
    ],
}
with open(os.path.join(BASE, 'summary', 'final_summary.json'), 'w') as f:
    json.dump(summary, f, indent=2)

print(f"\n{'='*80}")
print(f"  ED-PHYS-11 COMPLETE")
print(f"{'='*80}")
print(f"  alpha_R_pred = {alpha_R_pred:.4f}")
print(f"  alpha_R_meas = {fit_best['alpha']:.4f}")
print(f"  epsilon      = {epsilon:.2f}")
print(f"  verdict      = {verdict}")
