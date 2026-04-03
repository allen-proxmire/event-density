"""
ED-Cosmo-04: Corrected Spatial Cosmology Execution.

Corrected system from ED-Cosmo-03:
  dt rho_com = (D/a^2) dx[M(rho) dx rho] - D*P0*(rho - rho*) + H*v
  dt v       = (1/tau)( (D/a^2) dx[M(rho) dx rho] - D*P0*(rho - rho*) - zeta*v )
  da/dt      = (a / (d * rho_bar)) * [ -D*P0*(rho_bar - rho*) + H*v_bar ]

Key changes from ED-Cosmo-02:
  - NO explicit -H_hub*rho dilution term in rho equation
  - NO explicit -H_hub*v Hubble drag in v equation
  - Scale factor from penalty mass flow ODE (not from mean density ratio)
  - rho_phys = rho_com / a^d (separate interpretation)
"""
import json, os, math, warnings, time as clock
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

BASE = 'outputs/ED-Cosmo-04'

# ═══ Constants ═══
D_nd = 0.3
H_part = D_nd
rho_star = 0.5
rho_max = 1.0
beta = 2.0
M0 = 1.0
P0 = 0.1
zeta = 0.1
tau = 1.0
d_dim = 1  # spatial dimension

Gyr = 3.1557e16
H_0 = 2.184e-18
T0 = D_nd / H_0
t_present_nd = 13.8 / (T0 / Gyr)

# ═══ Grid ═══
N = 512
L = 1.0
dx = L / N
x = np.linspace(dx/2, L - dx/2, N)

# ═══ Constitutive ═══
def mobility(rho):
    return M0 * np.clip(rho_max - rho, 0, None)**beta

def enforce(rho):
    return np.clip(rho, 1e-10, rho_max - 1e-10)

def mobility_flux(rho, a_val):
    rho_r = np.roll(rho, -1)
    rho_l = np.roll(rho, 1)
    M_r = mobility(0.5*(rho + rho_r))
    M_l = mobility(0.5*(rho_l + rho))
    F_r = M_r * (rho_r - rho) / dx
    F_l = M_l * (rho - rho_l) / dx
    return (D_nd / a_val**2) * (F_r - F_l) / dx

# ═══ ICs ═══
def make_IC1():
    rho0_mean = 0.8
    rho = np.full(N, rho0_mean)
    for k in range(1, 11):
        rho += (0.08 / k) * np.cos(2*np.pi*k*x/L)
    return enforce(rho), 'Void-filament (deterministic)'

def make_IC2():
    rho0_mean = 0.8
    rng = np.random.default_rng(42)
    P0_amp = (0.05 * rho0_mean)**2
    k_arr = np.fft.rfftfreq(N, d=dx) * 2*np.pi
    k_arr[0] = 1.0
    Pk = P0_amp * np.ones_like(k_arr)
    Pk[0] = 0
    Pk *= np.exp(-(k_arr / (2*np.pi*20/L))**2)
    phases = rng.uniform(0, 2*np.pi, len(k_arr))
    fk = np.sqrt(Pk) * np.exp(1j*phases)
    fk[0] = 0
    pert = np.fft.irfft(fk, n=N)
    return enforce(rho0_mean + pert), 'Gaussian random field'

def make_IC3():
    rho0_mean = 0.8
    rho = rho0_mean - 0.24 * np.exp(-((x - L/2)**2) / (2*(L/8)**2))
    return enforce(rho), 'Single void'

# ═══ Corrected integrator ═══
def run_simulation(rho0, ic_label, ic_num):
    t_start = clock.time()
    rho = rho0.copy()
    v = np.zeros(N)
    a_val = 1.0
    rho_bar_0 = np.mean(rho)

    T_final = t_present_nd * 1.3
    CFL = 0.25

    n_snap = 200
    snap_times = np.linspace(0, T_final, n_snap + 1)
    snap_idx = 0
    rho_snaps = np.zeros((n_snap + 1, N))
    v_snaps = np.zeros((n_snap + 1, N))
    diag = {k: [] for k in [
        't', 'rho_bar_com', 'rho_bar_phys', 'a', 'H_hub', 'q', 'w',
        'v_bar', 'sigma_rho', 'sigma_v', 'S', 'sigma2_H',
        'Phi_mob', 'Phi_part', 'H_void', 'H_fil'
    ]}

    rho_snaps[0] = rho
    v_snaps[0] = v
    snap_idx = 1

    t = 0.0
    step = 0
    next_snap = snap_times[1] if len(snap_times) > 1 else T_final

    while t < T_final:
        # Adaptive timestep
        M_max = max(np.max(mobility(rho)), 1e-15)
        dt_cfl = CFL * a_val**2 * dx**2 / (2 * D_nd * M_max)
        dt_pen = CFL / max(D_nd * P0, 1e-10)
        dt = min(dt_cfl, dt_pen, 0.002, next_snap - t)
        if dt < 1e-12:
            dt = 1e-8

        # ── CORRECTED RHS: no dilution, no Hubble drag ──
        mob = mobility_flux(rho, a_val)
        penalty = -D_nd * P0 * (rho - rho_star)
        part = H_part * v
        F_local = mob + penalty

        drho = mob + penalty + part           # NO -H_hub*rho
        dv = (1.0/tau) * (F_local - zeta * v) # NO -H_hub*v

        # Forward Euler
        rho_new = enforce(rho + dt * drho)
        v_new = v + dt * dv

        # ── CORRECTED scale factor ODE ──
        rho_bar = np.mean(rho_new)
        v_bar = np.mean(v_new)
        # da/dt = (a / (d * rho_bar)) * [-D*P0*(rho_bar - rho*) + H*v_bar]
        penalty_bar = -D_nd * P0 * (rho_bar - rho_star)
        da_dt = (a_val / (d_dim * rho_bar)) * (penalty_bar + H_part * v_bar)
        a_new = a_val + dt * da_dt
        if a_new < 0.1:
            a_new = 0.1  # safety floor

        # Hubble parameter (for diagnostics only)
        H_hub = da_dt / max(a_val, 1e-15)

        rho = rho_new
        v = v_new
        a_val = a_new
        t += dt
        step += 1

        # ── Snapshot ──
        if t >= next_snap - 1e-12 and snap_idx <= n_snap:
            rho_snaps[snap_idx] = rho
            v_snaps[snap_idx] = v

            rho_bar_now = np.mean(rho)
            rho_phys = rho_bar_now / a_val**d_dim

            # Local expansion rates (from local drho/rho)
            local_drho = mob + penalty + H_part * v
            local_H = -local_drho / np.maximum(rho, 1e-15)

            H_void_mask = rho < rho_bar_now
            H_fil_mask = rho >= rho_bar_now
            H_void_val = float(np.mean(local_H[H_void_mask])) if H_void_mask.any() else 0
            H_fil_val = float(np.mean(local_H[H_fil_mask])) if H_fil_mask.any() else 0

            mean_lH = np.mean(local_H)
            std_lH = np.std(local_H)
            S_val = mean_lH / max(std_lH, 1e-15)
            sig2H = std_lH**2

            diag['t'].append(float(t))
            diag['rho_bar_com'].append(float(rho_bar_now))
            diag['rho_bar_phys'].append(float(rho_phys))
            diag['a'].append(float(a_val))
            diag['H_hub'].append(float(H_hub))
            diag['v_bar'].append(float(np.mean(v)))
            diag['sigma_rho'].append(float(np.std(rho)))
            diag['sigma_v'].append(float(np.std(v)))
            diag['S'].append(float(S_val))
            diag['sigma2_H'].append(float(sig2H))
            diag['Phi_mob'].append(float(np.mean(np.abs(mob))))
            diag['Phi_part'].append(float(np.mean(np.abs(H_part * v * rho))))
            diag['H_void'].append(float(H_void_val))
            diag['H_fil'].append(float(H_fil_val))

            snap_idx += 1
            if snap_idx <= n_snap:
                next_snap = snap_times[snap_idx]

    # Post-process q, w from H_hub
    t_arr = np.array(diag['t'])
    H_arr = np.array(diag['H_hub'])
    dH = np.gradient(H_arr, t_arr)
    H_safe = np.where(np.abs(H_arr) > 1e-15, H_arr, 1e-15)
    q_arr = -1.0 - dH / H_safe**2
    w_arr = (2*q_arr - 1) / 3
    diag['q'] = q_arr.tolist()
    diag['w'] = w_arr.tolist()

    elapsed = clock.time() - t_start

    # Save
    outdir = os.path.join(BASE, 'runs', f'IC_{ic_num}')
    np.savez_compressed(os.path.join(outdir, 'fields.npz'),
        snap_times=snap_times[:snap_idx], rho=rho_snaps[:snap_idx],
        v=v_snaps[:snap_idx], x=x)
    with open(os.path.join(outdir, 'diagnostics.json'), 'w') as f:
        json.dump(diag, f)

    # Present-time values
    idx_now = np.argmin(np.abs(t_arr - t_present_nd))
    a_now = diag['a'][idx_now]
    H_now_nd = H_arr[idx_now]
    H_now_phys = H_now_nd / T0
    H_mismatch = abs(H_now_phys - H_0) / H_0 * 100
    q_now = float(q_arr[idx_now])
    w_now = float(w_arr[idx_now])
    S_now = diag['S'][idx_now]
    sig2H_0 = diag['sigma2_H'][1] if len(diag['sigma2_H']) > 1 else 1
    sig2H_now = diag['sigma2_H'][idx_now]
    sync_ratio = sig2H_now / sig2H_0 if sig2H_0 > 1e-20 else None
    H_void_now = diag['H_void'][idx_now]
    H_fil_now = diag['H_fil'][idx_now]

    c_ED = math.sqrt(D_nd * H_part / tau)
    F1 = H_mismatch < 20
    F2 = q_now < 0
    F3 = abs(c_ED / D_nd - 1.0) < 0.01  # c_ED_nd/D_nd should be 1 (c_ED_phys = c)
    F4 = H_part / P0 < 100
    F5 = a_now > 1.0
    F6 = (sync_ratio is not None and sync_ratio < 0.5)
    F7 = H_void_now > H_fil_now

    result = {
        'ic': ic_num, 'label': ic_label,
        'N': N, 'steps': step, 'elapsed_s': round(elapsed, 1),
        'P0': P0, 'H_part': H_part, 'H_over_P0': H_part/P0,
        'a_now': round(float(a_now), 6),
        'H_now_nd': round(float(H_now_nd), 8),
        'H_mismatch_pct': round(float(H_mismatch), 2),
        'q_now': round(q_now, 4),
        'w_now': round(w_now, 4),
        'S_now': round(float(S_now), 4),
        'sigma2_H_0': round(float(sig2H_0), 8),
        'sigma2_H_now': round(float(sig2H_now), 8),
        'sync_ratio': round(float(sync_ratio), 6) if sync_ratio else None,
        'H_void_now': round(float(H_void_now), 6),
        'H_fil_now': round(float(H_fil_now), 6),
        'rho_bar_com_now': round(float(diag['rho_bar_com'][idx_now]), 6),
        'rho_bar_phys_now': round(float(diag['rho_bar_phys'][idx_now]), 6),
        'F_cosmo_1': 'PASS' if F1 else 'FAIL',
        'F_cosmo_2': 'PASS' if F2 else 'FAIL',
        'F_cosmo_3': 'PASS' if F3 else 'FAIL',
        'F_cosmo_4': 'PASS' if F4 else 'FAIL',
        'F_cosmo_5': 'PASS' if F5 else 'FAIL',
        'F_cosmo_6': 'PASS' if F6 else 'FAIL',
        'F_cosmo_7': 'PASS' if F7 else 'FAIL',
    }
    with open(os.path.join(outdir, 'result.json'), 'w') as f:
        json.dump(result, f, indent=2)

    return result, diag, rho_snaps[:snap_idx], v_snaps[:snap_idx], snap_times[:snap_idx]


# ═══ RUN ═══
print("=" * 80)
print("  ED-Cosmo-04: Corrected Spatial Cosmology")
print("  (no dilution term, no Hubble drag, scale factor from penalty mass flow)")
print("=" * 80)

ics = [(make_IC1, 1), (make_IC2, 2), (make_IC3, 3)]
all_results = {}
all_diag = {}
all_snaps = {}

for ic_fn, ic_num in ics:
    rho0, label = ic_fn()
    print(f"\n  IC {ic_num}: {label}")
    result, diag, rho_s, v_s, st = run_simulation(rho0, label, ic_num)
    all_results[ic_num] = result
    all_diag[ic_num] = diag
    all_snaps[ic_num] = (rho_s, v_s, st)

    score = sum(1 for i in range(1,8) if result[f'F_cosmo_{i}'] == 'PASS')
    print(f"    {result['elapsed_s']:.1f}s | {result['steps']} steps | "
          f"a={result['a_now']:.4f} | H_err={result['H_mismatch_pct']:.1f}% | "
          f"q={result['q_now']:+.4f} | S={result['S_now']:.3f} | "
          f"sync={'%.4f'%result['sync_ratio'] if result['sync_ratio'] else 'N/A'} | "
          f"{''.join('P' if result[f'F_cosmo_{i}']=='PASS' else 'F' for i in range(1,8))} "
          f"| {score}/7")


# ═══ PLOTS ═══
print("\nGenerating plots...")
PLOTS = os.path.join(BASE, 'plots')
cols = {1: 'C0', 2: 'C1', 3: 'C2'}
labels = {1: 'IC1: Void-filament', 2: 'IC2: Random field', 3: 'IC3: Single void'}

def t_gyr(d): return np.array(d['t']) * T0 / Gyr

# P1: a(t)
fig, ax = plt.subplots(figsize=(9, 6))
for ic in [1,2,3]:
    ax.plot(t_gyr(all_diag[ic]), all_diag[ic]['a'], '-', color=cols[ic], lw=2, label=labels[ic])
ax.axvline(13.8, color='k', ls='--', lw=1, alpha=0.5, label='Present')
ax.axhline(1.0, color='gray', ls=':', lw=1, alpha=0.3)
ax.set_xlabel('Time (Gyr)', fontsize=13); ax.set_ylabel('$a(t)$', fontsize=13)
ax.set_title('P1: Scale Factor (Corrected)', fontsize=14)
ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P1_scale_factor.png'), dpi=150); plt.close(); print("  P1")

# P2: H_ED(t)
fig, ax = plt.subplots(figsize=(9, 6))
for ic in [1,2,3]:
    H_phys = np.array(all_diag[ic]['H_hub']) / T0 * 3.0857e22 / 1e3
    ax.plot(t_gyr(all_diag[ic]), H_phys, '-', color=cols[ic], lw=2, label=labels[ic])
ax.axhline(67.4, color='k', ls='--', lw=1, alpha=0.5, label='$H_0=67.4$')
ax.axvline(13.8, color='gray', ls=':', lw=1, alpha=0.5)
ax.set_xlabel('Time (Gyr)', fontsize=13); ax.set_ylabel('$H$ (km/s/Mpc)', fontsize=13)
ax.set_title('P2: Hubble Parameter (Corrected)', fontsize=14)
ax.legend(fontsize=10); ax.grid(True, alpha=0.3); ax.set_ylim(-50, 300)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P2_Hubble.png'), dpi=150); plt.close(); print("  P2")

# P3: q(t)
fig, ax = plt.subplots(figsize=(9, 6))
for ic in [1,2,3]:
    ax.plot(t_gyr(all_diag[ic]), np.clip(all_diag[ic]['q'], -5, 5), '-', color=cols[ic], lw=2, label=labels[ic])
ax.axhline(0, color='k', ls='-', lw=0.5)
ax.axhline(-0.55, color='gray', ls='--', alpha=0.5, label='$q_0=-0.55$')
ax.axvline(13.8, color='gray', ls=':', lw=1, alpha=0.5)
ax.set_xlabel('Time (Gyr)', fontsize=13); ax.set_ylabel('$q(t)$', fontsize=13)
ax.set_title('P3: Deceleration (Corrected)', fontsize=14)
ax.legend(fontsize=10); ax.grid(True, alpha=0.3); ax.set_ylim(-3, 3)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P3_deceleration.png'), dpi=150); plt.close(); print("  P3")

# P4: S(t)
fig, ax = plt.subplots(figsize=(9, 6))
for ic in [1,2,3]:
    ax.plot(t_gyr(all_diag[ic]), all_diag[ic]['S'], '-', color=cols[ic], lw=2, label=labels[ic])
ax.axvline(13.8, color='gray', ls=':', lw=1, alpha=0.5)
ax.set_xlabel('Time (Gyr)', fontsize=13); ax.set_ylabel('$S(t)$', fontsize=13)
ax.set_title('P4: Synchronization (Corrected)', fontsize=14)
ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P4_synchronization.png'), dpi=150); plt.close(); print("  P4")

# P5: sigma2_H
fig, ax = plt.subplots(figsize=(9, 6))
for ic in [1,2,3]:
    s2 = np.array(all_diag[ic]['sigma2_H'])
    s2_0 = s2[1] if len(s2) > 1 else 1
    if s2_0 > 1e-20:
        ax.semilogy(t_gyr(all_diag[ic]), s2/s2_0, '-', color=cols[ic], lw=2, label=labels[ic])
ax.axhline(0.5, color='r', ls='--', lw=1, label='F6 threshold')
ax.axvline(13.8, color='gray', ls=':', lw=1, alpha=0.5)
ax.set_xlabel('Time (Gyr)', fontsize=13); ax.set_ylabel(r'$\sigma^2_H / \sigma^2_H(0)$', fontsize=13)
ax.set_title('P5: Expansion-Rate Variance (Corrected)', fontsize=14)
ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P5_variance.png'), dpi=150); plt.close(); print("  P5")

# P6: void vs filament
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for i, ic in enumerate([1,2,3]):
    axes[i].plot(t_gyr(all_diag[ic]), all_diag[ic]['H_void'], '-', color='C0', lw=1.5, label='Void')
    axes[i].plot(t_gyr(all_diag[ic]), all_diag[ic]['H_fil'], '-', color='C3', lw=1.5, label='Filament')
    axes[i].axhline(0, color='k', ls='-', lw=0.5)
    axes[i].axvline(13.8, color='gray', ls=':', lw=0.5)
    axes[i].set_xlabel('Gyr'); axes[i].set_ylabel('Local H'); axes[i].set_title(labels[ic])
    axes[i].legend(fontsize=9); axes[i].grid(True, alpha=0.3)
fig.suptitle('P6: Void vs Filament (Corrected)', fontsize=14)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P6_void_filament.png'), dpi=150); plt.close(); print("  P6")

# P7: rho snapshots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for i, ic in enumerate([1,2,3]):
    rho_s, v_s, st = all_snaps[ic]
    ns = len(st)
    for j in [0, ns//4, ns//2, 3*ns//4, ns-1]:
        if j < len(rho_s):
            axes[i].plot(x, rho_s[j], lw=0.8, label=f't={st[j]*T0/Gyr:.1f}')
    axes[i].axhline(rho_star, color='k', ls=':', lw=0.5)
    axes[i].set_xlabel('x'); axes[i].set_ylabel(r'$\rho$'); axes[i].set_title(labels[ic])
    axes[i].legend(fontsize=7); axes[i].grid(True, alpha=0.3)
fig.suptitle(r'P7: $\rho(x,t)$ Snapshots (Corrected)', fontsize=14)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P7_density.png'), dpi=150); plt.close(); print("  P7")

# P8: v snapshots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for i, ic in enumerate([1,2,3]):
    rho_s, v_s, st = all_snaps[ic]
    ns = len(st)
    for j in [0, ns//4, ns//2, 3*ns//4, ns-1]:
        if j < len(v_s):
            axes[i].plot(x, v_s[j], lw=0.8, label=f't={st[j]*T0/Gyr:.1f}')
    axes[i].axhline(0, color='k', ls='-', lw=0.5)
    axes[i].set_xlabel('x'); axes[i].set_ylabel('$v$'); axes[i].set_title(labels[ic])
    axes[i].legend(fontsize=7); axes[i].grid(True, alpha=0.3)
fig.suptitle('P8: $v(x,t)$ Snapshots (Corrected)', fontsize=14)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P8_participation.png'), dpi=150); plt.close(); print("  P8")

# ═══ TABLES ═══
TABLES = os.path.join(BASE, 'tables')
lines = ['# S1: IC Parameters\n', '| IC | Label | N | rho0 | P0 | H/P0 |', '|--|--|--|--|--|--|']
for ic in [1,2,3]:
    r = all_results[ic]
    lines.append(f"| {ic} | {r['label']} | {N} | 0.8 | {P0} | {H_part/P0} |")
with open(os.path.join(TABLES, 'S1_parameters.md'), 'w') as f: f.write('\n'.join(lines))

lines = ['# S2: Asymptotic\n', '| IC | a(t0) | rho_com | rho_phys | H_err% | Steps |', '|--|--|--|--|--|--|']
for ic in [1,2,3]:
    r = all_results[ic]
    lines.append(f"| {ic} | {r['a_now']:.4f} | {r['rho_bar_com_now']:.4f} | {r['rho_bar_phys_now']:.4f} | {r['H_mismatch_pct']:.1f} | {r['steps']} |")
with open(os.path.join(TABLES, 'S2_asymptotic.md'), 'w') as f: f.write('\n'.join(lines))

lines = ['# S3: Synchronization\n', '| IC | S(t0) | sync_ratio | H_void | H_fil | void>fil |', '|--|--|--|--|--|--|']
for ic in [1,2,3]:
    r = all_results[ic]
    sr = f"{r['sync_ratio']:.4f}" if r['sync_ratio'] else 'N/A'
    lines.append(f"| {ic} | {r['S_now']:.4f} | {sr} | {r['H_void_now']:.4f} | {r['H_fil_now']:.4f} | {'Y' if r['F_cosmo_7']=='PASS' else 'N'} |")
with open(os.path.join(TABLES, 'S3_synchronization.md'), 'w') as f: f.write('\n'.join(lines))

lines = ['# S4: Falsification\n', '| IC | F1 | F2 | F3 | F4 | F5 | F6 | F7 | Score |', '|--|--|--|--|--|--|--|--|--|']
for ic in [1,2,3]:
    r = all_results[ic]
    score = sum(1 for i in range(1,8) if r[f'F_cosmo_{i}']=='PASS')
    fs = ' | '.join(r[f'F_cosmo_{i}'] for i in range(1,8))
    lines.append(f"| {ic} | {fs} | {score}/7 |")
with open(os.path.join(TABLES, 'S4_falsification.md'), 'w') as f: f.write('\n'.join(lines))
print("  Tables saved")

# ═══ SUMMARY ═══
summary = {
    'experiment': 'ED-Cosmo-04 Corrected Spatial Cosmology',
    'date': '2026-03-31',
    'correction': 'Removed dilution term and Hubble drag per ED-Cosmo-03',
    'parameters': {'D': D_nd, 'H': H_part, 'P0': P0, 'beta': beta, 'zeta': zeta, 'tau': tau},
    'results': {str(k): v for k, v in all_results.items()},
    'falsification_tally': {},
    'plots': sorted(os.listdir(PLOTS)),
    'tables': sorted(os.listdir(TABLES)),
}
for fi in range(1, 8):
    key = f'F_cosmo_{fi}'
    summary['falsification_tally'][key] = f"{sum(1 for ic in [1,2,3] if all_results[ic][key]=='PASS')}/3"

with open(os.path.join(BASE, 'summary', 'final_summary.json'), 'w') as f:
    json.dump(summary, f, indent=2)

print("\n" + "=" * 80)
print("  ED-COSMO-04 COMPLETE")
print("=" * 80)
for fi in range(1, 8):
    key = f'F_cosmo_{fi}'
    print(f"  {key}: {summary['falsification_tally'][key]}")
