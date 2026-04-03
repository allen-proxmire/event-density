"""
ED-Cosmo-01: Simulate the cosmological limit of the ED PDE.

Reduced 2-ODE telegraph system from ED-Cosmo-01_CosmologicalLimit.md:
    d(rho_bar)/dt = -D*P0*(rho_bar - rho_star) + H*v
    dv/dt         = (1/tau)*(-D*P0*(rho_bar - rho_star) - zeta*v)

Cosmological mapping:
    a(t)    = (rho_0 / rho_bar(t))^(1/3)
    H_ED(t) = -d(rho_bar)/dt / (3*rho_bar)
    q_ED(t) = -1 - dH_ED/dt / H_ED^2
    w_ED(t) = (2*q_ED - 1) / 3
"""
import json, os, math, warnings
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

BASE = 'outputs/ED-Cosmo-01'

# ══════════════════════════════════════════════════════════════════════
# Physical constants (from edsim/units/constants.py)
# ══════════════════════════════════════════════════════════════════════
H_0 = 2.184e-18       # s^-1 (67.4 km/s/Mpc)
c_light = 2.998e8     # m/s
G_N = 6.674e-11       # m^3 kg^-1 s^-2
rho_crit = 8.53e-27   # kg/m^3
t_H = 1/H_0           # Hubble time ~ 14.5 Gyr
Gyr = 3.1557e16       # seconds per Gyr

# ED nondimensional scales
D_nd = 0.3
L0 = c_light / H_0
T0 = D_nd / H_0       # 4.35 Gyr
V0 = c_light / D_nd

# ══════════════════════════════════════════════════════════════════════
# Candidate parameter sets (nondimensional)
# ══════════════════════════════════════════════════════════════════════
candidates = {
    'A': {'P0': 1.0,  'zeta': 0.1, 'tau': 1.0, 'label': 'Canonical'},
    'B': {'P0': 0.1,  'zeta': 0.1, 'tau': 1.0, 'label': 'Weak penalty'},
    'C': {'P0': 1.0,  'zeta': 1.0, 'tau': 1.0, 'label': 'Strong damping'},
    'D': {'P0': 0.3,  'zeta': 0.3, 'tau': 1.0, 'label': 'Matched (P0=zeta=D)'},
    'E': {'P0': 0.23, 'zeta': 0.1, 'tau': 1.0, 'label': 'Hubble-matched'},
}

# Cosmological participation coupling (from ED-Phys-05 causality: H = D_nd)
H_participation = D_nd  # = 0.3

# Initial conditions (nondimensional)
rho_star = 0.5
rho_max = 1.0
rho_0 = 0.95  # initial density ~ 0.95 * rho_crit (above equilibrium)
v_0 = 0.0     # no initial participation

# Integration span: 0 to 5 T0 = 0 to ~21.8 Gyr
t_span_nd = (0.0, 8.0)  # in units of T0 (~34.8 Gyr)
t_eval = np.linspace(0, 8.0, 10000)

# Present time: t_0 = 13.8 Gyr = 13.8/4.35 T0 = 3.172 T0
t_present_nd = 13.8 / (T0 / Gyr)


def compute_telegraph_params(D, P0, zeta, tau, H):
    """Compute telegraph parameters gamma, omega_0, omega."""
    gamma = (D * P0 + zeta / tau) / 2.0
    omega0_sq = (D * P0 * zeta + H * P0) / tau
    if omega0_sq > gamma**2:
        omega = math.sqrt(omega0_sq - gamma**2)
        regime = 'underdamped'
    elif abs(omega0_sq - gamma**2) < 1e-10:
        omega = 0.0
        regime = 'critical'
    else:
        omega = 0.0
        regime = 'overdamped'
    return gamma, math.sqrt(max(omega0_sq, 0)), omega, regime


def run_candidate(name, params):
    """Run one candidate cosmological simulation."""
    P0 = params['P0']
    zeta = params['zeta']
    tau = params['tau']
    H = H_participation
    D = D_nd

    gamma, omega0, omega, regime = compute_telegraph_params(D, P0, zeta, tau, H)

    # ODE system: y = [rho_bar, v]
    def rhs(t, y):
        rho_bar, v = y
        delta = rho_bar - rho_star
        drho = -D * P0 * delta + H * v
        dv = (1.0 / tau) * (-D * P0 * delta - zeta * v)
        return [drho, dv]

    sol = solve_ivp(rhs, t_span_nd, [rho_0, v_0], t_eval=t_eval,
                    method='RK45', rtol=1e-12, atol=1e-14)

    t = sol.t
    rho_bar = sol.y[0]
    v = sol.y[1]

    # Derived quantities
    # Scale factor: a = (rho_0 / rho_bar)^(1/3)
    a = (rho_0 / np.maximum(rho_bar, 1e-20))**(1.0/3.0)

    # drho/dt from the ODE
    drho = -D * P0 * (rho_bar - rho_star) + H * v

    # Hubble parameter: H_ED = -drho / (3*rho_bar)
    H_ED = -drho / (3.0 * np.maximum(rho_bar, 1e-20))

    # dH_ED/dt (numerical derivative)
    dH_ED = np.gradient(H_ED, t)

    # Deceleration: q = -1 - dH/dt / H^2
    H_ED_safe = np.where(np.abs(H_ED) > 1e-15, H_ED, 1e-15)
    q_ED = -1.0 - dH_ED / H_ED_safe**2

    # Equation of state: w = (2q - 1) / 3
    w_ED = (2.0 * q_ED - 1.0) / 3.0

    # Horizon propagation speed (c_ED = sqrt(D*H/tau) = sqrt(0.3*0.3/1) = 0.3 nd)
    c_ED_nd = math.sqrt(D * H / tau)
    c_ED_phys = c_ED_nd * V0  # should be ~c

    # Physical time in Gyr
    t_phys = t * T0 / Gyr

    # Values at present time
    idx_now = np.argmin(np.abs(t - t_present_nd))
    H_ED_now_nd = H_ED[idx_now]
    H_ED_now_phys = H_ED_now_nd / T0  # convert to s^-1
    q_now = q_ED[idx_now]
    w_now = w_ED[idx_now]
    rho_now = rho_bar[idx_now]
    a_now = a[idx_now]

    # Falsification checks
    H_mismatch = abs(H_ED_now_phys - H_0) / H_0 * 100  # percent
    F1 = H_mismatch < 20  # within 20%?
    F2 = q_now < 0         # accelerating?
    F3 = abs(c_ED_phys - c_light) / c_light < 0.01  # horizon speed = c?
    F4 = H / P0 < 100      # inside Lyapunov region?
    # F5 checked qualitatively (expansion scaling)
    F5_note = 'monotonic' if np.all(np.diff(a) >= -1e-10) else 'non-monotonic'

    result = {
        'name': name,
        'label': params['label'],
        'P0': P0, 'zeta': zeta, 'tau': tau,
        'H': H, 'D': D, 'H_over_P0': round(H/P0, 4),
        'gamma': round(gamma, 6), 'omega0': round(omega0, 6),
        'omega': round(omega, 6), 'regime': regime,
        'rho_0': rho_0, 'rho_star': rho_star,
        't_present_nd': round(t_present_nd, 4),
        'H_ED_now_nd': round(float(H_ED_now_nd), 6),
        'H_ED_now_phys': float(H_ED_now_phys),
        'H_0_observed': H_0,
        'H_mismatch_pct': round(H_mismatch, 2),
        'q_now': round(float(q_now), 6),
        'w_now': round(float(w_now), 6),
        'a_now': round(float(a_now), 6),
        'rho_now': round(float(rho_now), 6),
        'c_ED_nd': round(c_ED_nd, 6),
        'c_ED_phys_over_c': round(c_ED_phys / c_light, 6),
        'expansion_type': F5_note,
        'F_cosmo_1': 'PASS' if F1 else 'FAIL',
        'F_cosmo_2': 'PASS' if F2 else 'FAIL',
        'F_cosmo_3': 'PASS' if F3 else 'FAIL',
        'F_cosmo_4': 'PASS' if F4 else 'FAIL',
        'F_cosmo_5': F5_note,
    }

    # Save per-candidate
    outdir = os.path.join(BASE, 'candidate_runs', f'set_{name}')
    with open(os.path.join(outdir, 'result.json'), 'w') as f:
        json.dump(result, f, indent=2)
    np.savez_compressed(os.path.join(outdir, 'timeseries.npz'),
        t_nd=t, t_Gyr=t_phys, rho_bar=rho_bar, v=v,
        a=a, H_ED=H_ED, q_ED=q_ED, w_ED=w_ED)

    return result, t, t_phys, rho_bar, v, a, H_ED, q_ED, w_ED


# ══════════════════════════════════════════════════════════════════════
# RUN ALL CANDIDATES
# ══════════════════════════════════════════════════════════════════════
print("=" * 80)
print("  ED-Cosmo-01: Cosmological Limit Simulations")
print("=" * 80)

all_results = {}
all_data = {}

for name in ['A', 'B', 'C', 'D', 'E']:
    result, t, t_phys, rho, v, a, H_ED, q_ED, w_ED = run_candidate(name, candidates[name])
    all_results[name] = result
    all_data[name] = {
        't': t, 't_Gyr': t_phys, 'rho': rho, 'v': v,
        'a': a, 'H_ED': H_ED, 'q_ED': q_ED, 'w_ED': w_ED
    }
    print(f"  Set {name} ({result['label']:20s}): regime={result['regime']:12s} "
          f"H/P0={result['H_over_P0']:6.2f} | "
          f"H_ED_now={result['H_mismatch_pct']:5.1f}% off | "
          f"q_now={result['q_now']:+.4f} | "
          f"F1={'P' if result['F_cosmo_1']=='PASS' else 'F'} "
          f"F2={'P' if result['F_cosmo_2']=='PASS' else 'F'} "
          f"F3={'P' if result['F_cosmo_3']=='PASS' else 'F'} "
          f"F4={'P' if result['F_cosmo_4']=='PASS' else 'F'}")

# ══════════════════════════════════════════════════════════════════════
# GENERATE PLOTS
# ══════════════════════════════════════════════════════════════════════
print("\nGenerating plots...")
PLOTS = os.path.join(BASE, 'plots')
colors = {'A': 'C0', 'B': 'C1', 'C': 'C2', 'D': 'C3', 'E': 'C4'}
styles = {'A': '-', 'B': '--', 'C': '-.', 'D': ':', 'E': '-'}

# P1: Scale factor a(t)
fig, ax = plt.subplots(figsize=(9, 6))
for name in ['A', 'B', 'C', 'D', 'E']:
    d = all_data[name]
    ax.plot(d['t_Gyr'], d['a'], styles[name], color=colors[name], lw=2,
            label=f"Set {name}: {candidates[name]['label']}")
ax.axvline(13.8, color='k', ls='--', lw=1, alpha=0.5, label='Present (13.8 Gyr)')
ax.set_xlabel('Time (Gyr)', fontsize=13)
ax.set_ylabel('Scale factor $a(t)$', fontsize=13)
ax.set_title('P1: ED Cosmological Scale Factor', fontsize=14)
ax.legend(fontsize=9, loc='upper left')
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 35)
fig.tight_layout()
fig.savefig(os.path.join(PLOTS, 'P1_scale_factor.png'), dpi=150)
plt.close(fig)
print("  P1 saved")

# P2: H_ED(t)
fig, ax = plt.subplots(figsize=(9, 6))
for name in ['A', 'B', 'C', 'D', 'E']:
    d = all_data[name]
    # Convert H_ED from nondimensional to physical (km/s/Mpc)
    H_phys = d['H_ED'] / T0 * 3.0857e22 / 1e3  # s^-1 -> km/s/Mpc
    ax.plot(d['t_Gyr'], H_phys, styles[name], color=colors[name], lw=2,
            label=f"Set {name}")
ax.axhline(67.4, color='k', ls='--', lw=1, alpha=0.5, label='$H_0 = 67.4$ km/s/Mpc')
ax.axvline(13.8, color='gray', ls=':', lw=1, alpha=0.5)
ax.set_xlabel('Time (Gyr)', fontsize=13)
ax.set_ylabel('$H_{\\mathrm{ED}}$ (km/s/Mpc)', fontsize=13)
ax.set_title('P2: ED Hubble Parameter', fontsize=14)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 35)
ax.set_ylim(-20, 200)
fig.tight_layout()
fig.savefig(os.path.join(PLOTS, 'P2_Hubble_parameter.png'), dpi=150)
plt.close(fig)
print("  P2 saved")

# P3: q_ED(t)
fig, ax = plt.subplots(figsize=(9, 6))
for name in ['A', 'B', 'C', 'D', 'E']:
    d = all_data[name]
    # Clip q for display (can have transients)
    q_clip = np.clip(d['q_ED'], -5, 5)
    ax.plot(d['t_Gyr'], q_clip, styles[name], color=colors[name], lw=2,
            label=f"Set {name}")
ax.axhline(0, color='k', ls='-', lw=0.5)
ax.axhline(-0.55, color='gray', ls='--', lw=1, alpha=0.5, label='$q_0 \\approx -0.55$ (observed)')
ax.axvline(13.8, color='gray', ls=':', lw=1, alpha=0.5)
ax.set_xlabel('Time (Gyr)', fontsize=13)
ax.set_ylabel('$q_{\\mathrm{ED}}(t)$', fontsize=13)
ax.set_title('P3: ED Deceleration Parameter', fontsize=14)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 35)
ax.set_ylim(-3, 3)
fig.tight_layout()
fig.savefig(os.path.join(PLOTS, 'P3_deceleration.png'), dpi=150)
plt.close(fig)
print("  P3 saved")

# P4: w_ED(t)
fig, ax = plt.subplots(figsize=(9, 6))
for name in ['A', 'B', 'C', 'D', 'E']:
    d = all_data[name]
    w_clip = np.clip(d['w_ED'], -5, 5)
    ax.plot(d['t_Gyr'], w_clip, styles[name], color=colors[name], lw=2,
            label=f"Set {name}")
ax.axhline(-1, color='k', ls='--', lw=1, alpha=0.5, label='$w = -1$ (cosmological constant)')
ax.axhline(-1/3, color='gray', ls=':', lw=1, alpha=0.3, label='$w = -1/3$ (accel. boundary)')
ax.axvline(13.8, color='gray', ls=':', lw=1, alpha=0.5)
ax.set_xlabel('Time (Gyr)', fontsize=13)
ax.set_ylabel('$w_{\\mathrm{ED}}(t)$', fontsize=13)
ax.set_title('P4: ED Equation of State', fontsize=14)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 35)
ax.set_ylim(-4, 2)
fig.tight_layout()
fig.savefig(os.path.join(PLOTS, 'P4_equation_of_state.png'), dpi=150)
plt.close(fig)
print("  P4 saved")

# P5: Phase portrait (rho, v)
fig, ax = plt.subplots(figsize=(7, 7))
for name in ['A', 'B', 'C', 'D', 'E']:
    d = all_data[name]
    ax.plot(d['rho'], d['v'], styles[name], color=colors[name], lw=1.5,
            label=f"Set {name}")
    ax.plot(d['rho'][0], d['v'][0], 'o', color=colors[name], ms=8)
ax.plot(0.5, 0, 'k*', ms=15, zorder=10, label=r'Attractor $(\rho^*, 0)$')
ax.set_xlabel(r'$\bar{\rho}$', fontsize=14)
ax.set_ylabel(r'$v(t)$', fontsize=14)
ax.set_title(r'P5: Phase Portrait $(\bar{\rho}, v)$', fontsize=14)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(PLOTS, 'P5_phase_portrait.png'), dpi=150)
plt.close(fig)
print("  P5 saved")

# P6: Telegraph regime classification (bar chart)
fig, ax = plt.subplots(figsize=(8, 5))
names = list(all_results.keys())
regimes = [all_results[n]['regime'] for n in names]
gamma_vals = [all_results[n]['gamma'] for n in names]
omega0_vals = [all_results[n]['omega0'] for n in names]
x = np.arange(len(names))
w_bar = 0.35
ax.bar(x - w_bar/2, gamma_vals, w_bar, label=r'$\gamma$ (damping)', color='C3', edgecolor='k')
ax.bar(x + w_bar/2, omega0_vals, w_bar, label=r'$\omega_0$ (natural freq)', color='C0', edgecolor='k')
for i, (n, r) in enumerate(zip(names, regimes)):
    ax.text(i, max(gamma_vals[i], omega0_vals[i]) + 0.02, r.upper(),
            ha='center', fontsize=9, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels([f"Set {n}\n({candidates[n]['label']})" for n in names], fontsize=8)
ax.set_ylabel('Rate (nondimensional)', fontsize=12)
ax.set_title('P6: Telegraph Regime Classification', fontsize=14)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, axis='y')
fig.tight_layout()
fig.savefig(os.path.join(PLOTS, 'P6_telegraph_classification.png'), dpi=150)
plt.close(fig)
print("  P6 saved")

# P7: Horizon propagation speed (trivially c for all candidates)
fig, ax = plt.subplots(figsize=(8, 4))
c_ratios = [all_results[n]['c_ED_phys_over_c'] for n in names]
ax.bar(x, c_ratios, color='C0', edgecolor='k')
ax.axhline(1.0, color='r', ls='--', lw=1.5, label='$c_{\\mathrm{ED}} = c$')
ax.set_xticks(x)
ax.set_xticklabels([f"Set {n}" for n in names])
ax.set_ylabel('$c_{\\mathrm{ED}} / c$', fontsize=13)
ax.set_title('P7: Horizon Propagation Speed', fontsize=14)
ax.set_ylim(0.95, 1.05)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3, axis='y')
fig.tight_layout()
fig.savefig(os.path.join(PLOTS, 'P7_horizon_speed.png'), dpi=150)
plt.close(fig)
print("  P7 saved")

# ══════════════════════════════════════════════════════════════════════
# SUMMARY TABLES
# ══════════════════════════════════════════════════════════════════════
TABLES = os.path.join(BASE, 'tables')

# S1: Parameter sets
lines = ['# Table S1: Candidate Parameter Sets\n',
         '| Set | Label | P0 | zeta | tau | H | D | H/P0 |',
         '|-----|-------|----|------|-----|---|---|------|']
for n in names:
    r = all_results[n]
    lines.append(f"| {n} | {r['label']} | {r['P0']} | {r['zeta']} | {r['tau']} | {r['H']} | {r['D']} | {r['H_over_P0']} |")
with open(os.path.join(TABLES, 'S1_parameter_sets.md'), 'w') as f:
    f.write('\n'.join(lines))
print("  S1 saved")

# S2: Asymptotic behaviors
lines = ['# Table S2: Asymptotic Behaviors\n',
         '| Set | Early-time | Late-time | Relaxation time (Gyr) | a(t_now) |',
         '|-----|-----------|-----------|----------------------|----------|']
for n in names:
    r = all_results[n]
    tau_relax = 1.0 / r['gamma'] * T0 / Gyr
    early = 'de Sitter (exp. expansion)' if r['rho_0'] > r['rho_star'] else 'contraction'
    late = f"static attractor (rho -> {r['rho_star']})"
    lines.append(f"| {n} | {early} | {late} | {tau_relax:.1f} | {r['a_now']:.4f} |")
with open(os.path.join(TABLES, 'S2_asymptotic.md'), 'w') as f:
    f.write('\n'.join(lines))
print("  S2 saved")

# S3: Telegraph classification
lines = ['# Table S3: Telegraph Classification\n',
         '| Set | gamma | omega_0 | omega | Regime | gamma/omega_0 | T_osc (Gyr) |',
         '|-----|-------|---------|-------|--------|---------------|-------------|']
for n in names:
    r = all_results[n]
    T_osc = (2*math.pi/r['omega'] * T0 / Gyr) if r['omega'] > 0 else float('inf')
    T_osc_str = f"{T_osc:.1f}" if T_osc < 1e6 else "inf"
    lines.append(f"| {n} | {r['gamma']:.4f} | {r['omega0']:.4f} | {r['omega']:.4f} | "
                 f"{r['regime']} | {r['gamma']/r['omega0']:.3f} | {T_osc_str} |")
with open(os.path.join(TABLES, 'S3_telegraph.md'), 'w') as f:
    f.write('\n'.join(lines))
print("  S3 saved")

# S4: Falsification checks
lines = ['# Table S4: Falsification Evaluation\n',
         '| Set | F1 (H mismatch) | F2 (q<0) | F3 (c_ED=c) | F4 (H/P0) | F5 (expansion) |',
         '|-----|-----------------|----------|-------------|-----------|----------------|']
for n in names:
    r = all_results[n]
    lines.append(f"| {n} | {r['F_cosmo_1']} ({r['H_mismatch_pct']:.1f}%) | "
                 f"{r['F_cosmo_2']} (q={r['q_now']:+.3f}) | "
                 f"{r['F_cosmo_3']} (c_ED/c={r['c_ED_phys_over_c']:.4f}) | "
                 f"{r['F_cosmo_4']} (H/P0={r['H_over_P0']}) | "
                 f"{r['F_cosmo_5']} |")
with open(os.path.join(TABLES, 'S4_falsification.md'), 'w') as f:
    f.write('\n'.join(lines))
print("  S4 saved")

# ══════════════════════════════════════════════════════════════════════
# FINAL SUMMARY
# ══════════════════════════════════════════════════════════════════════
summary = {
    'experiment': 'ED-Cosmo-01 Cosmological Limit',
    'date': '2026-03-31',
    'system': 'Reduced 2-ODE telegraph (rho_bar, v)',
    'anchoring': {
        'D': D_nd, 'H': H_participation,
        'D_phys': 'c^2/H_0', 'L0': 'c/H_0', 'T0_Gyr': round(T0/Gyr, 2),
        'c_ED': 'c (exact)',
    },
    'initial_conditions': {'rho_0': rho_0, 'v_0': v_0, 'rho_star': rho_star},
    'candidates': all_results,
    'falsification_summary': {},
    'plots': sorted(os.listdir(PLOTS)),
    'tables': sorted(os.listdir(TABLES)),
}

# Tally falsification
for fi in ['F_cosmo_1', 'F_cosmo_2', 'F_cosmo_3', 'F_cosmo_4']:
    n_pass = sum(1 for n in names if all_results[n][fi] == 'PASS')
    summary['falsification_summary'][fi] = f"{n_pass}/5 PASS"

with open(os.path.join(BASE, 'summary', 'final_summary.json'), 'w') as f:
    json.dump(summary, f, indent=2)

print("\n" + "=" * 80)
print("  ED-COSMO-01 COMPLETE")
print("=" * 80)
print(f"  Candidates:  {len(all_results)}")
print(f"  Plots:       {len(os.listdir(PLOTS))}")
print(f"  Tables:      {len(os.listdir(TABLES))}")
print(f"  Summary:     {BASE}/summary/final_summary.json")
print()
print("  Falsification tally:")
for fi in ['F_cosmo_1', 'F_cosmo_2', 'F_cosmo_3', 'F_cosmo_4']:
    print(f"    {fi}: {summary['falsification_summary'][fi]}")
print()
for n in names:
    r = all_results[n]
    score = sum(1 for k in ['F_cosmo_1','F_cosmo_2','F_cosmo_3','F_cosmo_4']
                if r[k] == 'PASS')
    print(f"  Set {n} ({r['label']:20s}): {score}/4 pass | "
          f"regime={r['regime']} | q_now={r['q_now']:+.4f} | "
          f"H_err={r['H_mismatch_pct']:.1f}%")
