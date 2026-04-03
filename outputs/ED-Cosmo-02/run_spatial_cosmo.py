"""
ED-Cosmo-02: 1D Expanding-Coordinate ED PDE for Spatial Cosmology.

PDE system (comoving coords, self-consistent a(t)):
  dt rho = (D/a^2) dx[M(rho) dx rho] - D*P0*(rho - rho*) + H*v - H_hub*rho
  dt v   = (1/tau)( (D/a^2) dx[M(rho) dx rho] - D*P0*(rho - rho*) - zeta*v ) - H_hub*v

  a(t) = rho_bar(0) / rho_bar(t)
  H_hub(t) = -d(rho_bar)/dt / rho_bar
"""
import json, os, math, warnings, time as clock
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

BASE = 'outputs/ED-Cosmo-02'

# ═══ Physical / nondimensional constants ═══
D_nd = 0.3
H_part = D_nd         # participation coupling (Compton/Hubble anchoring)
rho_star = 0.5
rho_max = 1.0
beta = 2.0
M0 = 1.0
P0 = 0.1              # moderate penalty (inside Lyapunov region: H/P0 = 3)
zeta = 0.1
tau = 1.0

Gyr = 3.1557e16
H_0 = 2.184e-18
T0 = D_nd / H_0       # 4.35 Gyr
t_present_nd = 13.8 / (T0 / Gyr)  # ~3.17

# ═══ Grid ═══
N = 512
L = 1.0
dx = L / N
x = np.linspace(dx/2, L - dx/2, N)  # cell centres (periodic)

# ═══ Constitutive ═══
def mobility(rho):
    delta = np.clip(rho_max - rho, 0, None)
    return M0 * delta**beta

def mobility_deriv(rho):
    delta = np.clip(rho_max - rho, 1e-15, None)
    return -beta * M0 * delta**(beta - 1)

def enforce(rho):
    return np.clip(rho, 1e-10, rho_max - 1e-10)

# ═══ Spatial operators (periodic, conservative) ═══
def mobility_flux(rho, a_val):
    """Compute (D/a^2) * d/dx[M(rho) d/dx rho] using conservative FD."""
    rho_r = np.roll(rho, -1)
    rho_l = np.roll(rho, 1)
    # face mobilities
    M_rface = mobility(0.5*(rho + rho_r))
    M_lface = mobility(0.5*(rho_l + rho))
    # fluxes
    F_r = M_rface * (rho_r - rho) / dx
    F_l = M_lface * (rho - rho_l) / dx
    return (D_nd / a_val**2) * (F_r - F_l) / dx

# ═══ Build ICs ═══
def make_IC1():
    """Void-filament deterministic: sum of cosine modes."""
    rho0_mean = 0.8
    A0 = 0.08
    rho = np.full(N, rho0_mean)
    for k in range(1, 11):
        rho += (A0 / k) * np.cos(2*np.pi*k*x/L)
    return enforce(rho), 'Void-filament (deterministic)'

def make_IC2():
    """Gaussian random field with 1/k spectrum."""
    rho0_mean = 0.8
    rng = np.random.default_rng(42)
    P0_amp = (0.05 * rho0_mean)**2
    k_arr = np.fft.rfftfreq(N, d=dx) * 2*np.pi
    k_arr[0] = 1.0  # avoid div by zero
    Pk = P0_amp * k_arr**0  # scale-invariant (flat in k)
    Pk[0] = 0  # no DC perturbation
    k_cut = 2*np.pi*20/L
    Pk *= np.exp(-(k_arr/k_cut)**2)
    phases = rng.uniform(0, 2*np.pi, len(k_arr))
    fk = np.sqrt(Pk) * np.exp(1j*phases)
    fk[0] = 0
    pert = np.fft.irfft(fk, n=N)
    rho = rho0_mean + pert
    return enforce(rho), 'Gaussian random field'

def make_IC3():
    """Single large void."""
    rho0_mean = 0.8
    A_void = 0.3 * rho0_mean
    sigma_void = L / 8
    rho = rho0_mean - A_void * np.exp(-((x - L/2)**2) / (2*sigma_void**2))
    return enforce(rho), 'Single void'

# ═══ Integrator ═══
def run_simulation(rho0, ic_label, ic_num):
    """Run the full 1D expanding-coordinate ED PDE."""
    t_start = clock.time()
    rho = rho0.copy()
    v = np.zeros(N)
    rho_bar_0 = np.mean(rho)

    T_final = t_present_nd * 1.3  # run slightly past present
    CFL = 0.25

    # Storage
    n_snap = 200
    snap_times = np.linspace(0, T_final, n_snap + 1)
    snap_idx = 0
    rho_snaps = np.zeros((n_snap + 1, N))
    v_snaps = np.zeros((n_snap + 1, N))
    diag = {k: [] for k in [
        't', 'rho_bar', 'a', 'H_hub', 'q', 'w', 'v_bar',
        'sigma_rho', 'sigma_v', 'S', 'sigma2_H',
        'Phi_mob', 'Phi_part', 'H_void', 'H_fil'
    ]}

    # Save IC
    rho_snaps[0] = rho
    v_snaps[0] = v
    snap_idx = 1

    t = 0.0
    a_val = 1.0
    H_hub = 0.0
    step = 0
    next_snap = snap_times[1] if len(snap_times) > 1 else T_final

    while t < T_final:
        # Adaptive timestep
        M_max = max(np.max(mobility(rho)), 1e-15)
        dt_cfl = CFL * a_val**2 * dx**2 / (2 * D_nd * M_max)
        dt_pen = CFL / max(D_nd * P0, 1e-10)
        dt = min(dt_cfl, dt_pen, 0.001, next_snap - t)
        if dt < 1e-12:
            dt = 1e-8

        # ── Compute RHS ──
        mob = mobility_flux(rho, a_val)
        penalty = -D_nd * P0 * (rho - rho_star)
        part = H_part * v
        dilution = -H_hub * rho

        F_local = mob + penalty  # local forcing for v equation

        drho = mob + penalty + part + dilution
        dv = (1.0/tau) * (F_local - zeta * v) - H_hub * v

        # ── Forward Euler step ──
        rho_new = rho + dt * drho
        v_new = v + dt * dv
        rho_new = enforce(rho_new)

        rho = rho_new
        v = v_new
        t += dt
        step += 1

        # ── Update scale factor ──
        rho_bar = np.mean(rho)
        a_val = rho_bar_0 / max(rho_bar, 1e-15)
        # H_hub from finite difference
        rho_bar_prev = rho_bar_0 / max(a_val, 1e-15)  # current
        drho_bar = np.mean(drho)  # d(rho_bar)/dt
        H_hub = -drho_bar / max(rho_bar, 1e-15)

        # ── Snapshot? ──
        if t >= next_snap - 1e-12 and snap_idx <= n_snap:
            rho_snaps[snap_idx] = rho
            v_snaps[snap_idx] = v

            # Diagnostics
            local_H = np.zeros(N)
            drho_local = mob + penalty + part + dilution
            local_H = -drho_local / np.maximum(rho, 1e-15)

            H_void_mask = rho < rho_bar
            H_fil_mask = rho >= rho_bar
            H_void_val = np.mean(local_H[H_void_mask]) if H_void_mask.any() else 0
            H_fil_val = np.mean(local_H[H_fil_mask]) if H_fil_mask.any() else 0

            mean_localH = np.mean(local_H)
            std_localH = np.std(local_H)
            S_val = mean_localH / max(std_localH, 1e-15)
            sigma2_H = std_localH**2

            Phi_mob = np.mean(np.abs(mob))
            Phi_part = np.mean(np.abs(H_part * v * rho))

            # q from H_hub change
            diag['t'].append(t)
            diag['rho_bar'].append(rho_bar)
            diag['a'].append(a_val)
            diag['H_hub'].append(H_hub)
            diag['v_bar'].append(np.mean(v))
            diag['sigma_rho'].append(np.std(rho))
            diag['sigma_v'].append(np.std(v))
            diag['S'].append(S_val)
            diag['sigma2_H'].append(sigma2_H)
            diag['Phi_mob'].append(Phi_mob)
            diag['Phi_part'].append(Phi_part)
            diag['H_void'].append(H_void_val)
            diag['H_fil'].append(H_fil_val)

            snap_idx += 1
            if snap_idx <= n_snap:
                next_snap = snap_times[snap_idx]

    # Compute q and w from H_hub time series
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
        snap_times=snap_times[:snap_idx],
        rho=rho_snaps[:snap_idx], v=v_snaps[:snap_idx], x=x)
    for k in diag:
        diag[k] = [float(v) if isinstance(v, (np.floating, float)) else v for v in diag[k]]
    with open(os.path.join(outdir, 'diagnostics.json'), 'w') as f:
        json.dump(diag, f)

    # Present-time values
    idx_now = np.argmin(np.abs(t_arr - t_present_nd))
    H_now_nd = H_arr[idx_now]
    H_now_phys = H_now_nd / T0
    H_mismatch = abs(H_now_phys - H_0) / H_0 * 100
    q_now = q_arr[idx_now]
    w_now = w_arr[idx_now]
    a_now = diag['a'][idx_now]
    S_now = diag['S'][idx_now]
    sig2H_0 = diag['sigma2_H'][1] if len(diag['sigma2_H']) > 1 else 1
    sig2H_now = diag['sigma2_H'][idx_now]
    H_void_now = diag['H_void'][idx_now]
    H_fil_now = diag['H_fil'][idx_now]

    # Falsification
    c_ED = math.sqrt(D_nd * H_part / tau)
    F1 = H_mismatch < 20
    F2 = q_now < 0
    F3 = abs(c_ED * (3.0/D_nd) - 1.0) < 0.01  # c_ED*V0 ~ c? (c_ED_nd * V0/c = c_ED_nd / D_nd)
    F4 = H_part / P0 < 100
    F5 = a_now > 1.0  # universe expanded
    F6 = sig2H_now < 0.5 * sig2H_0 if sig2H_0 > 1e-20 else False
    F7 = H_void_now > H_fil_now

    result = {
        'ic': ic_num, 'label': ic_label,
        'N': N, 'T_final': round(T_final, 4), 'steps': step,
        'elapsed_s': round(elapsed, 1),
        'P0': P0, 'H_part': H_part, 'H_over_P0': H_part/P0,
        'a_now': round(float(a_now), 6),
        'H_now_nd': round(float(H_now_nd), 6),
        'H_mismatch_pct': round(float(H_mismatch), 2),
        'q_now': round(float(q_now), 4),
        'w_now': round(float(w_now), 4),
        'S_now': round(float(S_now), 4),
        'sigma2_H_0': round(float(sig2H_0), 8),
        'sigma2_H_now': round(float(sig2H_now), 8),
        'sync_ratio': round(float(sig2H_now / sig2H_0), 6) if sig2H_0 > 1e-20 else None,
        'H_void_now': round(float(H_void_now), 6),
        'H_fil_now': round(float(H_fil_now), 6),
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


# ═══ RUN ALL ICs ═══
print("=" * 80)
print("  ED-Cosmo-02: 1D Spatial Cosmology")
print("=" * 80)

ics = [(make_IC1, 1), (make_IC2, 2), (make_IC3, 3)]
all_results = {}
all_diag = {}
all_snaps = {}

for ic_fn, ic_num in ics:
    rho0, label = ic_fn()
    print(f"\n  IC {ic_num}: {label} (N={N}, rho_mean={np.mean(rho0):.4f})")
    result, diag, rho_s, v_s, st = run_simulation(rho0, label, ic_num)
    all_results[ic_num] = result
    all_diag[ic_num] = diag
    all_snaps[ic_num] = (rho_s, v_s, st)

    score = sum(1 for k in [f'F_cosmo_{i}' for i in range(1,8)] if result[k] == 'PASS')
    print(f"    {result['elapsed_s']:.1f}s | {result['steps']} steps | "
          f"a_now={result['a_now']:.4f} | H_err={result['H_mismatch_pct']:.1f}% | "
          f"q={result['q_now']:+.3f} | S={result['S_now']:.3f} | "
          f"sync={result['sync_ratio']:.4f} | "
          f"F1={'P' if result['F_cosmo_1']=='PASS' else 'F'} "
          f"F2={'P' if result['F_cosmo_2']=='PASS' else 'F'} "
          f"F6={'P' if result['F_cosmo_6']=='PASS' else 'F'} "
          f"F7={'P' if result['F_cosmo_7']=='PASS' else 'F'} "
          f"| {score}/7")


# ═══ PLOTS ═══
print("\nGenerating plots...")
PLOTS = os.path.join(BASE, 'plots')
cols = {1: 'C0', 2: 'C1', 3: 'C2'}
labels = {1: 'IC1: Void-filament', 2: 'IC2: Random field', 3: 'IC3: Single void'}

# P1: a(t)
fig, ax = plt.subplots(figsize=(9, 6))
for ic in [1, 2, 3]:
    d = all_diag[ic]
    t_Gyr = np.array(d['t']) * T0 / Gyr
    ax.plot(t_Gyr, d['a'], '-', color=cols[ic], lw=2, label=labels[ic])
ax.axvline(13.8, color='k', ls='--', lw=1, alpha=0.5, label='Present')
ax.set_xlabel('Time (Gyr)', fontsize=13); ax.set_ylabel('$a(t)$', fontsize=13)
ax.set_title('P1: Scale Factor (Spatial ED)', fontsize=14)
ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P1_scale_factor.png'), dpi=150)
plt.close(fig); print("  P1")

# P2: H_ED(t) in km/s/Mpc
fig, ax = plt.subplots(figsize=(9, 6))
for ic in [1, 2, 3]:
    d = all_diag[ic]
    t_Gyr = np.array(d['t']) * T0 / Gyr
    H_phys = np.array(d['H_hub']) / T0 * 3.0857e22 / 1e3
    ax.plot(t_Gyr, H_phys, '-', color=cols[ic], lw=2, label=labels[ic])
ax.axhline(67.4, color='k', ls='--', lw=1, alpha=0.5, label='$H_0=67.4$')
ax.axvline(13.8, color='gray', ls=':', lw=1, alpha=0.5)
ax.set_xlabel('Time (Gyr)', fontsize=13); ax.set_ylabel('$H$ (km/s/Mpc)', fontsize=13)
ax.set_title('P2: Hubble Parameter (Spatial ED)', fontsize=14)
ax.legend(fontsize=10); ax.grid(True, alpha=0.3); ax.set_ylim(-50, 300)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P2_Hubble.png'), dpi=150)
plt.close(fig); print("  P2")

# P3: q(t)
fig, ax = plt.subplots(figsize=(9, 6))
for ic in [1, 2, 3]:
    d = all_diag[ic]
    t_Gyr = np.array(d['t']) * T0 / Gyr
    q = np.clip(d['q'], -5, 5)
    ax.plot(t_Gyr, q, '-', color=cols[ic], lw=2, label=labels[ic])
ax.axhline(0, color='k', ls='-', lw=0.5)
ax.axhline(-0.55, color='gray', ls='--', alpha=0.5, label='$q_0=-0.55$ (obs)')
ax.axvline(13.8, color='gray', ls=':', lw=1, alpha=0.5)
ax.set_xlabel('Time (Gyr)', fontsize=13); ax.set_ylabel('$q(t)$', fontsize=13)
ax.set_title('P3: Deceleration Parameter', fontsize=14)
ax.legend(fontsize=10); ax.grid(True, alpha=0.3); ax.set_ylim(-3, 3)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P3_deceleration.png'), dpi=150)
plt.close(fig); print("  P3")

# P4: S(t) synchronization
fig, ax = plt.subplots(figsize=(9, 6))
for ic in [1, 2, 3]:
    d = all_diag[ic]
    t_Gyr = np.array(d['t']) * T0 / Gyr
    ax.plot(t_Gyr, d['S'], '-', color=cols[ic], lw=2, label=labels[ic])
ax.axvline(13.8, color='gray', ls=':', lw=1, alpha=0.5)
ax.set_xlabel('Time (Gyr)', fontsize=13); ax.set_ylabel('$S(t)$', fontsize=13)
ax.set_title('P4: Synchronization Metric', fontsize=14)
ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P4_synchronization.png'), dpi=150)
plt.close(fig); print("  P4")

# P5: sigma2_H(t)
fig, ax = plt.subplots(figsize=(9, 6))
for ic in [1, 2, 3]:
    d = all_diag[ic]
    t_Gyr = np.array(d['t']) * T0 / Gyr
    s2 = np.array(d['sigma2_H'])
    s2_norm = s2 / max(s2[1] if len(s2) > 1 else 1, 1e-20)
    ax.semilogy(t_Gyr, s2_norm, '-', color=cols[ic], lw=2, label=labels[ic])
ax.axhline(0.5, color='r', ls='--', lw=1, label='F6 threshold (50%)')
ax.axvline(13.8, color='gray', ls=':', lw=1, alpha=0.5)
ax.set_xlabel('Time (Gyr)', fontsize=13)
ax.set_ylabel(r'$\sigma^2_H(t) / \sigma^2_H(0)$', fontsize=13)
ax.set_title('P5: Expansion-Rate Variance (normalised)', fontsize=14)
ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P5_variance.png'), dpi=150)
plt.close(fig); print("  P5")

# P6: void vs filament expansion
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for i, ic in enumerate([1, 2, 3]):
    d = all_diag[ic]
    t_Gyr = np.array(d['t']) * T0 / Gyr
    axes[i].plot(t_Gyr, d['H_void'], '-', color='C0', lw=1.5, label='Void')
    axes[i].plot(t_Gyr, d['H_fil'], '-', color='C3', lw=1.5, label='Filament')
    axes[i].axhline(0, color='k', ls='-', lw=0.5)
    axes[i].axvline(13.8, color='gray', ls=':', lw=0.5)
    axes[i].set_xlabel('Time (Gyr)'); axes[i].set_ylabel('Local $H$')
    axes[i].set_title(labels[ic]); axes[i].legend(fontsize=9)
    axes[i].grid(True, alpha=0.3)
fig.suptitle('P6: Void vs Filament Expansion Rates', fontsize=14)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P6_void_filament.png'), dpi=150)
plt.close(fig); print("  P6")

# P7: spatial snapshots of rho
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for i, ic in enumerate([1, 2, 3]):
    rho_s, v_s, st = all_snaps[ic]
    n_s = len(st)
    for j in [0, n_s//4, n_s//2, 3*n_s//4, n_s-1]:
        if j < len(rho_s):
            t_gyr = st[j] * T0 / Gyr
            axes[i].plot(x, rho_s[j], lw=0.8, label=f't={t_gyr:.1f} Gyr')
    axes[i].axhline(rho_star, color='k', ls=':', lw=0.5, alpha=0.5)
    axes[i].set_xlabel('x (comoving)'); axes[i].set_ylabel(r'$\rho$')
    axes[i].set_title(labels[ic]); axes[i].legend(fontsize=7)
    axes[i].grid(True, alpha=0.3)
fig.suptitle(r'P7: Density Snapshots $\rho(x,t)$', fontsize=14)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P7_density_snapshots.png'), dpi=150)
plt.close(fig); print("  P7")

# P8: spatial snapshots of v
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for i, ic in enumerate([1, 2, 3]):
    rho_s, v_s, st = all_snaps[ic]
    n_s = len(st)
    for j in [0, n_s//4, n_s//2, 3*n_s//4, n_s-1]:
        if j < len(v_s):
            t_gyr = st[j] * T0 / Gyr
            axes[i].plot(x, v_s[j], lw=0.8, label=f't={t_gyr:.1f} Gyr')
    axes[i].axhline(0, color='k', ls='-', lw=0.5)
    axes[i].set_xlabel('x (comoving)'); axes[i].set_ylabel('$v(x,t)$')
    axes[i].set_title(labels[ic]); axes[i].legend(fontsize=7)
    axes[i].grid(True, alpha=0.3)
fig.suptitle('P8: Participation Field Snapshots $v(x,t)$', fontsize=14)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P8_participation_snapshots.png'), dpi=150)
plt.close(fig); print("  P8")

# ═══ TABLES ═══
TABLES = os.path.join(BASE, 'tables')

# S1
lines = ['# Table S1: IC Parameters\n',
         '| IC | Label | N | rho_mean | Structure | P0 | H/P0 |',
         '|----|-------|---|----------|-----------|----|----|']
for ic in [1,2,3]:
    r = all_results[ic]
    lines.append(f"| {ic} | {r['label']} | {N} | 0.8 | see spec | {P0} | {H_part/P0} |")
with open(os.path.join(TABLES, 'S1_IC_parameters.md'), 'w') as f:
    f.write('\n'.join(lines))

# S2
lines = ['# Table S2: Asymptotic Behaviors\n',
         '| IC | a(t_now) | H_now (% off) | Late-time | Steps |',
         '|----|----------|---------------|-----------|-------|']
for ic in [1,2,3]:
    r = all_results[ic]
    lines.append(f"| {ic} | {r['a_now']:.4f} | {r['H_mismatch_pct']:.1f}% | attractor | {r['steps']} |")
with open(os.path.join(TABLES, 'S2_asymptotic.md'), 'w') as f:
    f.write('\n'.join(lines))

# S3
lines = ['# Table S3: Synchronization Metrics\n',
         '| IC | S(t_now) | sync_ratio | H_void | H_fil | void > fil? |',
         '|----|----------|------------|--------|-------|-------------|']
for ic in [1,2,3]:
    r = all_results[ic]
    lines.append(f"| {ic} | {r['S_now']:.4f} | {r['sync_ratio']:.4f} | {r['H_void_now']:.4f} | {r['H_fil_now']:.4f} | {'YES' if r['F_cosmo_7']=='PASS' else 'NO'} |")
with open(os.path.join(TABLES, 'S3_synchronization.md'), 'w') as f:
    f.write('\n'.join(lines))

# S4
lines = ['# Table S4: Falsification Results\n',
         '| IC | F1 (H) | F2 (q<0) | F3 (c_ED) | F4 (H/P0) | F5 (expand) | F6 (sync) | F7 (void>fil) | Score |',
         '|----|--------|----------|-----------|-----------|-------------|-----------|---------------|-------|']
for ic in [1,2,3]:
    r = all_results[ic]
    score = sum(1 for i in range(1,8) if r[f'F_cosmo_{i}']=='PASS')
    fs = ' | '.join(r[f'F_cosmo_{i}'] for i in range(1,8))
    lines.append(f"| {ic} | {fs} | {score}/7 |")
with open(os.path.join(TABLES, 'S4_falsification.md'), 'w') as f:
    f.write('\n'.join(lines))

print("  Tables saved")

# ═══ FINAL SUMMARY ═══
summary = {
    'experiment': 'ED-Cosmo-02 Spatial Cosmology',
    'date': '2026-03-31',
    'pde': '1D expanding-coordinate ED with self-consistent a(t)',
    'grid': {'N': N, 'L': L, 'dx': dx},
    'parameters': {'D': D_nd, 'H_part': H_part, 'P0': P0, 'beta': beta,
                   'zeta': zeta, 'tau': tau, 'rho_star': rho_star},
    'results': {str(k): v for k, v in all_results.items()},
    'falsification_tally': {},
    'plots': sorted(os.listdir(PLOTS)),
    'tables': sorted(os.listdir(TABLES)),
}
for fi in range(1, 8):
    key = f'F_cosmo_{fi}'
    n_pass = sum(1 for ic in [1,2,3] if all_results[ic][key] == 'PASS')
    summary['falsification_tally'][key] = f"{n_pass}/3"

with open(os.path.join(BASE, 'summary', 'final_summary.json'), 'w') as f:
    json.dump(summary, f, indent=2)

print("\n" + "=" * 80)
print("  ED-COSMO-02 COMPLETE")
print("=" * 80)
print(f"  Runs:    3 ICs")
print(f"  Plots:   {len(os.listdir(PLOTS))}")
print(f"  Tables:  {len(os.listdir(TABLES))}")
print(f"  Summary: {BASE}/summary/final_summary.json")
print("\n  Falsification tally:")
for fi in range(1, 8):
    key = f'F_cosmo_{fi}'
    print(f"    {key}: {summary['falsification_tally'][key]}")
