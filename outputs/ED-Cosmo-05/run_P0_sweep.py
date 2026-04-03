"""
ED-Cosmo-05: P0 Sweep for Cosmological Matching.
Corrected system (ED-Cosmo-03/04): no dilution, no Hubble drag.
Sweep P0 in {1, 3, 10, 30} x IC {1, 2, 3}.
"""
import json, os, math, warnings, time as clock
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

BASE = 'outputs/ED-Cosmo-05'

# ═══ Fixed parameters ═══
D_nd = 0.3; H_part = D_nd; rho_star = 0.5; rho_max = 1.0
beta = 2.0; M0 = 1.0; zeta = 0.1; tau = 1.0; d_dim = 1
Gyr = 3.1557e16; H_0 = 2.184e-18; T0 = D_nd / H_0
t_present_nd = 13.8 / (T0 / Gyr)

N = 512; L = 1.0; dx = L / N
x = np.linspace(dx/2, L - dx/2, N)

P0_values = [1.0, 3.0, 10.0, 30.0]

def mobility(rho):
    return M0 * np.clip(rho_max - rho, 0, None)**beta

def enforce(rho):
    return np.clip(rho, 1e-10, rho_max - 1e-10)

def mobility_flux(rho, a_val, P0_val):
    rho_r = np.roll(rho, -1); rho_l = np.roll(rho, 1)
    M_r = mobility(0.5*(rho + rho_r)); M_l = mobility(0.5*(rho_l + rho))
    return (D_nd / a_val**2) * (M_r*(rho_r - rho)/dx - M_l*(rho - rho_l)/dx) / dx

def make_IC1():
    rho = np.full(N, 0.8)
    for k in range(1, 11): rho += (0.08/k)*np.cos(2*np.pi*k*x/L)
    return enforce(rho), 'Void-filament'

def make_IC2():
    rng = np.random.default_rng(42)
    k_arr = np.fft.rfftfreq(N, d=dx)*2*np.pi; k_arr[0] = 1.0
    Pk = (0.04)**2 * np.ones_like(k_arr); Pk[0] = 0
    Pk *= np.exp(-(k_arr/(2*np.pi*20/L))**2)
    fk = np.sqrt(Pk)*np.exp(1j*rng.uniform(0,2*np.pi,len(k_arr))); fk[0] = 0
    return enforce(0.8 + np.fft.irfft(fk, n=N)), 'Random field'

def make_IC3():
    return enforce(0.8 - 0.24*np.exp(-((x-L/2)**2)/(2*(L/8)**2))), 'Single void'

IC_makers = {1: make_IC1, 2: make_IC2, 3: make_IC3}

def run_one(ic_num, P0_val):
    rho0, ic_label = IC_makers[ic_num]()
    rho = rho0.copy(); v = np.zeros(N); a_val = 1.0
    rho_bar_0 = np.mean(rho)
    T_final = t_present_nd * 1.2
    CFL = 0.2

    n_snap = 150
    snap_times = np.linspace(0, T_final, n_snap+1)
    snap_idx = 1
    diag = {k: [] for k in ['t','rho_bar_com','a','H_hub','v_bar',
                              'sigma_rho','S','sigma2_H','H_void','H_fil']}

    t = 0.0; step = 0
    next_snap = snap_times[1]

    while t < T_final:
        M_max = max(np.max(mobility(rho)), 1e-15)
        dt = min(CFL*a_val**2*dx**2/(2*D_nd*M_max), CFL/(D_nd*P0_val), 0.001, next_snap - t)
        if dt < 1e-12: dt = 1e-9

        mob = mobility_flux(rho, a_val, P0_val)
        pen = -D_nd * P0_val * (rho - rho_star)
        part = H_part * v
        F_local = mob + pen

        rho_new = enforce(rho + dt*(mob + pen + part))
        v_new = v + dt*(1.0/tau)*(F_local - zeta*v)

        rho_bar = np.mean(rho_new); v_bar = np.mean(v_new)
        pen_bar = -D_nd*P0_val*(rho_bar - rho_star)
        da_dt = (a_val/(d_dim*rho_bar))*(pen_bar + H_part*v_bar)
        a_val = max(a_val + dt*da_dt, 0.01)
        H_hub = da_dt / max(a_val, 1e-15)

        rho = rho_new; v = v_new; t += dt; step += 1

        if t >= next_snap - 1e-12 and snap_idx <= n_snap:
            local_drho = mob + pen + part
            local_H = -local_drho / np.maximum(rho, 1e-15)
            mask_v = rho < rho_bar; mask_f = rho >= rho_bar
            H_v = float(np.mean(local_H[mask_v])) if mask_v.any() else 0
            H_f = float(np.mean(local_H[mask_f])) if mask_f.any() else 0
            std_lH = float(np.std(local_H)); mean_lH = float(np.mean(local_H))

            diag['t'].append(float(t))
            diag['rho_bar_com'].append(float(rho_bar))
            diag['a'].append(float(a_val))
            diag['H_hub'].append(float(H_hub))
            diag['v_bar'].append(float(np.mean(v)))
            diag['sigma_rho'].append(float(np.std(rho)))
            diag['S'].append(float(mean_lH/max(std_lH,1e-15)))
            diag['sigma2_H'].append(float(std_lH**2))
            diag['H_void'].append(H_v)
            diag['H_fil'].append(H_f)

            snap_idx += 1
            if snap_idx <= n_snap: next_snap = snap_times[snap_idx]

    # Post-process
    t_arr = np.array(diag['t']); H_arr = np.array(diag['H_hub'])
    dH = np.gradient(H_arr, t_arr)
    H_safe = np.where(np.abs(H_arr)>1e-15, H_arr, 1e-15)
    q_arr = -1.0 - dH/H_safe**2
    w_arr = (2*q_arr-1)/3
    diag['q'] = q_arr.tolist(); diag['w'] = w_arr.tolist()

    idx_now = np.argmin(np.abs(t_arr - t_present_nd))
    a_now = diag['a'][idx_now]
    H_now_nd = H_arr[idx_now]; H_now_phys = H_now_nd/T0
    H_mismatch = abs(H_now_phys - H_0)/H_0*100
    q_now = float(q_arr[idx_now])
    rho_bar_now = diag['rho_bar_com'][idx_now]
    eta_now = (rho_bar_now - rho_star)/rho_star if rho_star > 0 else 0
    P0_eta = P0_val * eta_now
    sig2_0 = diag['sigma2_H'][1] if len(diag['sigma2_H'])>1 else 1
    sig2_now = diag['sigma2_H'][idx_now]
    sync = sig2_now/sig2_0 if sig2_0>1e-20 else None
    H_v_now = diag['H_void'][idx_now]; H_f_now = diag['H_fil'][idx_now]

    F1 = H_mismatch < 20
    F2 = q_now < 0
    F3 = True  # c_ED = c by construction
    F4 = H_part/P0_val < 100
    F5 = a_now > 1.0
    F6 = sync is not None and sync < 0.5
    F7 = H_v_now > H_f_now

    result = {
        'ic': ic_num, 'label': ic_label, 'P0': P0_val,
        'H_over_P0': round(H_part/P0_val, 4), 'steps': step,
        'a_now': round(float(a_now), 6),
        'H_mismatch_pct': round(float(H_mismatch), 2),
        'q_now': round(q_now, 4), 'w_now': round(float(w_arr[idx_now]), 4),
        'rho_bar_now': round(float(rho_bar_now), 6),
        'eta_now': round(float(eta_now), 6),
        'P0_eta': round(float(P0_eta), 4),
        'S_now': round(float(diag['S'][idx_now]), 4),
        'sync_ratio': round(float(sync), 6) if sync else None,
        'H_void': round(float(H_v_now), 6), 'H_fil': round(float(H_f_now), 6),
        'F1': 'PASS' if F1 else 'FAIL', 'F2': 'PASS' if F2 else 'FAIL',
        'F3': 'PASS', 'F4': 'PASS' if F4 else 'FAIL',
        'F5': 'PASS' if F5 else 'FAIL', 'F6': 'PASS' if F6 else 'FAIL',
        'F7': 'PASS' if F7 else 'FAIL',
    }

    tag = f'IC_{ic_num}_P0_{int(P0_val)}'
    outdir = os.path.join(BASE, 'runs', tag)
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, 'result.json'), 'w') as f: json.dump(result, f, indent=2)
    with open(os.path.join(outdir, 'diagnostics.json'), 'w') as f: json.dump(diag, f)

    return result, diag

# ═══ RUN ALL ═══
print("="*85)
print("  ED-Cosmo-05: P0 Sweep for Cosmological Matching")
print("="*85)

all_results = []
all_diag = {}

for P0_val in P0_values:
    print(f"\n--- P0 = {P0_val} (H/P0 = {H_part/P0_val:.2f}) ---")
    for ic_num in [1, 2, 3]:
        t0 = clock.time()
        r, d = run_one(ic_num, P0_val)
        elapsed = clock.time() - t0
        r['elapsed_s'] = round(elapsed, 1)
        all_results.append(r)
        all_diag[(ic_num, P0_val)] = d
        score = sum(1 for i in range(1,8) if r[f'F{i}' if i<=2 else f'F{i}']=='PASS')
        # count correctly
        score = sum(1 for k in ['F1','F2','F3','F4','F5','F6','F7'] if r[k]=='PASS')
        fs = ''.join('P' if r[f'F{i}']=='PASS' else 'F' for i in range(1,8))
        print(f"  IC{ic_num} | a={r['a_now']:.4f} H_err={r['H_mismatch_pct']:6.1f}% "
              f"q={r['q_now']:+.3f} eta={r['eta_now']:.4f} P0*eta={r['P0_eta']:.3f} "
              f"sync={'%.4f'%r['sync_ratio'] if r['sync_ratio'] else 'N/A'} "
              f"| {fs} {score}/7 | {elapsed:.1f}s")

# ═══ PLOTS ═══
print("\nPlots...")
PLOTS = os.path.join(BASE, 'plots')
pcols = {1.0:'C0', 3.0:'C1', 10.0:'C2', 30.0:'C3'}

# P1–P3: one figure per IC, lines per P0
for obs, ylabel, title, fname, ylim in [
    ('a', '$a(t)$', 'Scale Factor', 'P1_a', None),
    ('H_hub', '$H$ (nd)', 'Hubble Parameter', 'P2_H', None),
    ('q', '$q(t)$', 'Deceleration', 'P3_q', (-3, 5)),
]:
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    for i, ic in enumerate([1,2,3]):
        for P0_val in P0_values:
            d = all_diag.get((ic, P0_val))
            if d is None: continue
            tg = np.array(d['t'])*T0/Gyr
            y = np.array(d[obs])
            if ylim: y = np.clip(y, ylim[0], ylim[1])
            axes[i].plot(tg, y, '-', color=pcols[P0_val], lw=1.5, label=f'P0={P0_val}')
        axes[i].axvline(13.8, color='k', ls='--', lw=0.5)
        if obs == 'a': axes[i].axhline(1.0, color='gray', ls=':', lw=0.5)
        if obs == 'q': axes[i].axhline(0, color='k', ls='-', lw=0.5); axes[i].axhline(-0.55, color='gray', ls='--', lw=0.5)
        axes[i].set_xlabel('Gyr'); axes[i].set_ylabel(ylabel)
        axes[i].set_title(f'IC{ic}'); axes[i].legend(fontsize=8); axes[i].grid(True, alpha=0.3)
        if ylim: axes[i].set_ylim(ylim)
    fig.suptitle(f'{title} vs P0', fontsize=14)
    fig.tight_layout(); fig.savefig(os.path.join(PLOTS, f'{fname}.png'), dpi=150); plt.close()
    print(f"  {fname}")

# P4: S(t) per IC
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
for i, ic in enumerate([1,2,3]):
    for P0_val in P0_values:
        d = all_diag.get((ic, P0_val))
        if d is None: continue
        axes[i].plot(np.array(d['t'])*T0/Gyr, d['S'], '-', color=pcols[P0_val], lw=1.5, label=f'P0={P0_val}')
    axes[i].axvline(13.8, color='k', ls='--', lw=0.5)
    axes[i].set_xlabel('Gyr'); axes[i].set_ylabel('S(t)'); axes[i].set_title(f'IC{ic}')
    axes[i].legend(fontsize=8); axes[i].grid(True, alpha=0.3)
fig.suptitle('P4: Synchronization vs P0', fontsize=14)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P4_sync.png'), dpi=150); plt.close(); print("  P4")

# P5: void vs filament for IC1
fig, axes = plt.subplots(1, 4, figsize=(18, 4))
for j, P0_val in enumerate(P0_values):
    d = all_diag.get((1, P0_val))
    if d is None: continue
    tg = np.array(d['t'])*T0/Gyr
    axes[j].plot(tg, d['H_void'], '-', color='C0', lw=1.5, label='Void')
    axes[j].plot(tg, d['H_fil'], '-', color='C3', lw=1.5, label='Filament')
    axes[j].axhline(0, color='k', ls='-', lw=0.5)
    axes[j].axvline(13.8, color='gray', ls=':', lw=0.5)
    axes[j].set_xlabel('Gyr'); axes[j].set_ylabel('Local H')
    axes[j].set_title(f'P0={P0_val}'); axes[j].legend(fontsize=8); axes[j].grid(True, alpha=0.3)
fig.suptitle('P5: Void vs Filament (IC1)', fontsize=14)
fig.tight_layout(); fig.savefig(os.path.join(PLOTS, 'P5_voidfil.png'), dpi=150); plt.close(); print("  P5")

# ═══ TABLES ═══
TABLES = os.path.join(BASE, 'tables')

lines = ['# S1: Sweep Parameters\n', '| P0 | H/P0 | ICs |', '|--|--|--|']
for p in P0_values: lines.append(f'| {p} | {H_part/p:.2f} | 1,2,3 |')
with open(os.path.join(TABLES, 'S1_parameters.md'), 'w') as f: f.write('\n'.join(lines))

lines = ['# S2: Key Observables at t0\n',
         '| IC | P0 | a(t0) | H_err% | q(t0) | eta | P0*eta |',
         '|--|--|--|--|--|--|--|']
for r in all_results:
    lines.append(f"| {r['ic']} | {r['P0']} | {r['a_now']:.4f} | {r['H_mismatch_pct']:.1f} | {r['q_now']:+.3f} | {r['eta_now']:.4f} | {r['P0_eta']:.3f} |")
with open(os.path.join(TABLES, 'S2_observables.md'), 'w') as f: f.write('\n'.join(lines))

lines = ['# S3: Falsification\n',
         '| IC | P0 | F1 | F2 | F3 | F4 | F5 | F6 | F7 | Score |',
         '|--|--|--|--|--|--|--|--|--|--|']
for r in all_results:
    score = sum(1 for k in ['F1','F2','F3','F4','F5','F6','F7'] if r[k]=='PASS')
    fs = ' | '.join(r[f'F{i}'] for i in range(1,8))
    lines.append(f"| {r['ic']} | {r['P0']} | {fs} | {score}/7 |")
with open(os.path.join(TABLES, 'S3_falsification.md'), 'w') as f: f.write('\n'.join(lines))

lines = ['# S4: P0*eta Constraint Check\n',
         '| IC | P0 | eta(t0) | P0*eta | Target (~1) | Match? |',
         '|--|--|--|--|--|--|']
for r in all_results:
    match = 'YES' if 0.5 < r['P0_eta'] < 2.0 else 'NO'
    lines.append(f"| {r['ic']} | {r['P0']} | {r['eta_now']:.4f} | {r['P0_eta']:.3f} | ~1 | {match} |")
with open(os.path.join(TABLES, 'S4_P0eta.md'), 'w') as f: f.write('\n'.join(lines))
print("  Tables saved")

# ═══ SUMMARY ═══
# Find best candidates
best = [r for r in all_results if r['F1']=='PASS' and r['F2']=='PASS' and r['F5']=='PASS']
summary = {
    'experiment': 'ED-Cosmo-05 P0 Sweep',
    'date': '2026-03-31',
    'P0_values': P0_values,
    'total_runs': len(all_results),
    'results': all_results,
    'best_candidates': best if best else 'None found',
    'falsification_tally': {},
}
for fi in range(1, 8):
    key = f'F{fi}'
    summary['falsification_tally'][key] = f"{sum(1 for r in all_results if r[key]=='PASS')}/{len(all_results)}"

with open(os.path.join(BASE, 'summary', 'final_summary.json'), 'w') as f:
    json.dump(summary, f, indent=2)

print("\n" + "="*85)
print("  ED-COSMO-05 COMPLETE")
print("="*85)
print(f"  Runs: {len(all_results)}")
for fi in range(1,8):
    key = f'F{fi}'
    print(f"  {key}: {summary['falsification_tally'][key]}")
if best:
    print(f"\n  BEST CANDIDATES ({len(best)}):")
    for b in best:
        print(f"    IC{b['ic']} P0={b['P0']}: a={b['a_now']:.4f} H_err={b['H_mismatch_pct']:.1f}% q={b['q_now']:+.3f}")
else:
    print("\n  No candidate satisfies F1+F2+F5 simultaneously.")
    print("  Closest:")
    for r in sorted(all_results, key=lambda x: x['H_mismatch_pct'])[:3]:
        print(f"    IC{r['ic']} P0={r['P0']}: a={r['a_now']:.4f} H_err={r['H_mismatch_pct']:.1f}% q={r['q_now']:+.3f}")
