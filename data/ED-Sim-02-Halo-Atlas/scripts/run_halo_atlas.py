"""
ED-Sim-02: ED-Poisson Halo Atlas.

Solves the steady-state ED-Poisson system in spherical symmetry:
    d/dr[r^2 M(rho) drho/dr] / r^2 = P0*(rho - rho_star(r))
    d/dr[r^2 dPhi/dr] / r^2 = 4*pi*G*rho
    rho_star(r) = rho_0 * exp(-Phi / sigma_v^2)

with M(rho) = rho^alpha * (rho_max - rho)^beta

Sweeps (alpha, beta, sigma_v) and extracts core radius, rotation curve,
and Burkert-match quality.
"""
import json, os, warnings, csv, time
import numpy as np
from scipy.integrate import solve_bvp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

BASE = 'data/ED-Sim-02-Halo-Atlas'
RES = os.path.join(BASE, 'results')
FIG = os.path.join(BASE, 'figures')

# ═══ Constants ═══
G = 4.302e-3  # pc Msun^-1 (km/s)^2 -> use kpc units
# G in kpc^3 / (Msun * Gyr^2) = 4.498e-6
# Simpler: work in units where G*rho has dimensions of 1/kpc^2
# For rho in Msun/kpc^3: G = 4.302e-3 (km/s)^2 pc/Msun = 4.302e-3 * 1e-3 (km/s)^2 kpc/Msun
G_kpc = 4.302e-6  # (km/s)^2 kpc / Msun

# ═══ Burkert profile for comparison ═══
def burkert_density(r, rho_0, r_c):
    """Burkert density profile."""
    x = r / r_c
    return rho_0 / ((1 + x) * (1 + x**2))

def burkert_mass(r, rho_0, r_c):
    """Enclosed mass for Burkert profile."""
    x = r / r_c
    return np.pi * rho_0 * r_c**3 * (np.log(1 + x**2) + 2*np.log(1 + x) - 2*np.arctan(x))

def burkert_vcirc(r, rho_0, r_c):
    """Circular velocity for Burkert."""
    M = burkert_mass(r, rho_0, r_c)
    return np.sqrt(G_kpc * M / np.maximum(r, 0.01))

# ═══ ED-Poisson solver (iterative relaxation) ═══
def solve_ed_poisson(alpha, beta, sigma_v, rho_max=1e8, P0=1.0,
                      N=500, R_max=50.0, n_iter=200, omega=0.3):
    """
    Solve the ED-Poisson system by iterative relaxation.

    Units: r in kpc, rho in Msun/kpc^3, Phi in (km/s)^2, sigma_v in km/s.
    """
    dr = R_max / N
    r = np.linspace(dr/2, R_max, N)

    # Initial guess: isothermal profile
    rho_0_central = (sigma_v / 10)**2 * 1e6  # rough central density
    r_iso = sigma_v / np.sqrt(4 * np.pi * G_kpc * rho_0_central)  # isothermal core
    rho = rho_0_central / (1 + (r / max(r_iso, 0.1))**2)
    rho = np.clip(rho, 1.0, rho_max * 0.99)

    Phi = np.zeros(N)

    for iteration in range(n_iter):
        # Step 1: Solve Poisson for Phi given rho
        # d/dr(r^2 dPhi/dr) = 4*pi*G*rho*r^2
        # Integrate from r=0 outward
        M_enc = np.cumsum(4 * np.pi * rho * r**2 * dr)
        Phi_new = np.zeros(N)
        # Phi(r) = -G * integral from r to inf of M(r')/r'^2 dr'
        # Approximate: Phi(r) = -G * sum_{j>=i} M_enc[j] * dr / r[j]^2
        # Actually simpler: Phi(r) = -G * M_enc(r) / r (Gauss's law)
        # But we need the full integral for accuracy
        for i in range(N-1, -1, -1):
            Phi_new[i] = -G_kpc * M_enc[i] / r[i]
        # Normalise so Phi(0) = 0 (relative potential)
        Phi_new -= Phi_new[0]

        # Step 2: Compute rho_star from Phi
        rho_star = rho_0_central * np.exp(-Phi_new / max(sigma_v**2, 1.0))
        rho_star = np.clip(rho_star, 1.0, rho_max * 0.99)

        # Step 3: Update rho using the ED mobility equation
        # In steady state: div(M(rho) grad(rho)) = P0*(rho - rho_star)
        # Relaxation: rho_new = rho + omega * dt * [div(M grad rho) - P0*(rho-rho_star)]
        # Use explicit diffusion step
        M = np.power(np.maximum(rho, 1e-10), alpha) * np.power(np.maximum(rho_max - rho, 1e-10), beta)

        # Spherical Laplacian of rho weighted by M
        rho_r = np.roll(rho, -1); rho_l = np.roll(rho, 1)
        M_r = 0.5 * (M + np.roll(M, -1))
        M_l = 0.5 * (np.roll(M, 1) + M)

        r_hp = 0.5 * (r + np.roll(r, -1)); r_hp[-1] = r[-1] + dr/2
        r_hm = 0.5 * (np.roll(r, 1) + r); r_hm[0] = dr/4

        flux = (r_hp**2 * M_r * (rho_r - rho) / dr - r_hm**2 * M_l * (rho - rho_l) / dr) / (r**2 * dr)

        # BC: drho/dr = 0 at r=0 (reflective)
        flux[0] = (r_hp[0]**2 * M_r[0] * (rho[1] - rho[0]) / dr) / (r[0]**2 * dr)
        # BC: rho -> 0 at R_max
        flux[-1] = (-r_hm[-1]**2 * M_l[-1] * (rho[-1] - rho[-2]) / dr) / (r[-1]**2 * dr)

        residual = flux - P0 * (rho - rho_star)
        rho_new = rho + omega * residual
        rho_new = np.clip(rho_new, 1.0, rho_max * 0.99)

        # Damped update
        rho = rho_new
        Phi = Phi_new

    # Extract observables
    M_enc = np.cumsum(4 * np.pi * rho * r**2 * dr)
    V_circ = np.sqrt(G_kpc * M_enc / r)

    # Core radius: where rho drops to half of central value
    rho_half = rho[0] / 2
    idx_half = np.argmax(rho < rho_half)
    r_core = r[idx_half] if idx_half > 0 else R_max

    return r, rho, V_circ, M_enc, r_core, Phi


def fit_burkert(r, rho, V_circ):
    """Find best-fit Burkert parameters and compute chi^2."""
    from scipy.optimize import minimize_scalar

    rho_0_fit = rho[0]

    def chi2(log_rc):
        rc = 10**log_rc
        V_burk = burkert_vcirc(r, rho_0_fit, rc)
        mask = (r > 0.5) & (r < 30) & (V_circ > 1)
        if mask.sum() < 5:
            return 1e10
        return np.sum((V_circ[mask] - V_burk[mask])**2) / mask.sum()

    result = minimize_scalar(chi2, bounds=(-1, 2), method='bounded')
    rc_best = 10**result.x
    chi2_best = result.fun

    return rc_best, chi2_best


# ═══ Parameter sweep ═══
alpha_values = np.linspace(0.0, 1.0, 8)
beta_values = np.linspace(1.0, 3.0, 8)
sigma_values = np.array([10, 20, 30, 50, 70, 100, 120, 150])  # km/s

print("=" * 85)
print("  ED-Sim-02: ED-Poisson Halo Atlas")
print("=" * 85)
total = len(alpha_values) * len(beta_values) * len(sigma_values)
print(f"  alpha: {len(alpha_values)} values [{alpha_values[0]:.1f}, {alpha_values[-1]:.1f}]")
print(f"  beta:  {len(beta_values)} values [{beta_values[0]:.1f}, {beta_values[-1]:.1f}]")
print(f"  sigma: {len(sigma_values)} values [{sigma_values[0]}, {sigma_values[-1]}] km/s")
print(f"  Total: {total} parameter sets")

t0 = time.time()
results = []
n_done = 0
n_dwarf = 0
n_spiral = 0
n_fail = 0

for sigma_v in sigma_values:
    for alpha in alpha_values:
        for beta in beta_values:
            try:
                r, rho, V_circ, M_enc, r_core, Phi = solve_ed_poisson(
                    alpha, beta, sigma_v, N=300, R_max=50.0, n_iter=150, omega=0.2)

                V_max = np.max(V_circ)
                V_flat = np.mean(V_circ[-50:]) if len(V_circ) > 50 else V_circ[-1]

                # Burkert fit
                rc_burk, chi2_burk = fit_burkert(r, rho, V_circ)

                # Classification
                if r_core < 0.5 or r_core > 49 or V_max < 5:
                    flag = 'fail'
                    n_fail += 1
                elif 1 <= r_core <= 5:
                    flag = 'dwarf'
                    n_dwarf += 1
                elif 3 <= r_core <= 15:
                    flag = 'spiral'
                    n_spiral += 1
                else:
                    flag = 'other'

                results.append({
                    'alpha': round(float(alpha), 3),
                    'beta': round(float(beta), 3),
                    'sigma_v': int(sigma_v),
                    'r_core': round(float(r_core), 3),
                    'V_max': round(float(V_max), 2),
                    'V_flat': round(float(V_flat), 2),
                    'rc_burkert': round(float(rc_burk), 3),
                    'chi2_burkert': round(float(chi2_burk), 2),
                    'rho_central': round(float(rho[0]), 1),
                    'flag': flag,
                })
            except Exception as e:
                results.append({
                    'alpha': round(float(alpha), 3),
                    'beta': round(float(beta), 3),
                    'sigma_v': int(sigma_v),
                    'r_core': -1, 'V_max': 0, 'V_flat': 0,
                    'rc_burkert': 0, 'chi2_burkert': 1e10,
                    'rho_central': 0, 'flag': 'error',
                })
                n_fail += 1

            n_done += 1

    elapsed = time.time() - t0
    print(f"  sigma_v={sigma_v:3d}: {n_done}/{total} done | "
          f"dwarf={n_dwarf} spiral={n_spiral} fail={n_fail} | {elapsed:.1f}s")

# ═══ Save CSV ═══
with open(os.path.join(RES, 'halo_scan.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(results[0].keys()))
    w.writeheader()
    w.writerows(results)
print(f"\n  halo_scan.csv saved ({len(results)} rows)")

# ═══ Figures ═══
print("  Generating figures...")

# Core radius heatmap for sigma_v = 30 km/s (dwarf) and 100 km/s (spiral)
for sv_plot in [30, 100]:
    rc_grid = np.full((len(alpha_values), len(beta_values)), np.nan)
    for res in results:
        if res['sigma_v'] == sv_plot and res['flag'] != 'error':
            i = np.argmin(np.abs(alpha_values - res['alpha']))
            j = np.argmin(np.abs(beta_values - res['beta']))
            rc_grid[i, j] = res['r_core']

    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.pcolormesh(beta_values, alpha_values, rc_grid, cmap='viridis',
                        vmin=0, vmax=min(20, np.nanmax(rc_grid)))
    plt.colorbar(im, ax=ax, label='Core radius (kpc)')
    ax.set_xlabel(r'$\beta$', fontsize=13)
    ax.set_ylabel(r'$\alpha$', fontsize=13)
    ax.set_title(f'ED-Poisson Core Radius ($\\sigma_v = {sv_plot}$ km/s)', fontsize=13)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, f'core_radius_map_sv{sv_plot}.png'), dpi=150)
    plt.close()

# Burkert match heatmap
for sv_plot in [30, 100]:
    chi2_grid = np.full((len(alpha_values), len(beta_values)), np.nan)
    for res in results:
        if res['sigma_v'] == sv_plot and res['flag'] != 'error':
            i = np.argmin(np.abs(alpha_values - res['alpha']))
            j = np.argmin(np.abs(beta_values - res['beta']))
            chi2_grid[i, j] = np.log10(max(res['chi2_burkert'], 0.01))

    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.pcolormesh(beta_values, alpha_values, chi2_grid, cmap='RdYlGn_r', vmin=-2, vmax=4)
    plt.colorbar(im, ax=ax, label=r'$\log_{10}\,\chi^2_{Burkert}$')
    ax.set_xlabel(r'$\beta$', fontsize=13)
    ax.set_ylabel(r'$\alpha$', fontsize=13)
    ax.set_title(f'Burkert Match Quality ($\\sigma_v = {sv_plot}$ km/s)', fontsize=13)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, f'burkert_match_sv{sv_plot}.png'), dpi=150)
    plt.close()

# Core radius vs sigma_v scaling
fig, ax = plt.subplots(figsize=(8, 6))
for alpha in [0.0, 0.5, 1.0]:
    for beta in [1.5, 2.0, 2.5]:
        sigs = []; rcs = []
        for res in results:
            if abs(res['alpha'] - alpha) < 0.05 and abs(res['beta'] - beta) < 0.05 and res['flag'] != 'error':
                sigs.append(res['sigma_v'])
                rcs.append(res['r_core'])
        if sigs:
            ax.plot(sigs, rcs, 'o-', ms=4, lw=1,
                    label=f'a={alpha:.1f}, b={beta:.1f}')
ax.set_xlabel(r'$\sigma_v$ (km/s)', fontsize=13)
ax.set_ylabel('Core radius (kpc)', fontsize=13)
ax.set_title(r'Core Radius vs $\sigma_v$', fontsize=13)
ax.legend(fontsize=7, ncol=3); ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(FIG, 'core_vs_sigma.png'), dpi=150)
plt.close()

# Representative profiles
fig, axes = plt.subplots(2, 3, figsize=(15, 9))
cases = [
    (0.0, 2.0, 30, 'Canonical dwarf'),
    (0.5, 2.0, 30, 'Generalized dwarf'),
    (0.5, 2.0, 100, 'Generalized spiral'),
    (0.0, 1.5, 30, 'Low beta dwarf'),
    (0.0, 3.0, 30, 'High beta dwarf'),
    (1.0, 2.0, 100, 'High alpha spiral'),
]
for idx, (a, b, sv, title) in enumerate(cases):
    ax = axes[idx // 3][idx % 3]
    try:
        r, rho, V, M, rc, Phi = solve_ed_poisson(a, b, sv, N=300, R_max=50.0, n_iter=150)
        ax.plot(r, V, 'C0-', lw=2, label=f'ED (rc={rc:.1f} kpc)')
        V_burk = burkert_vcirc(r, rho[0], rc)
        ax.plot(r, V_burk, 'k--', lw=1.5, label='Burkert')
        ax.set_title(f'{title}\na={a}, b={b}, sv={sv}', fontsize=10)
        ax.set_xlabel('r (kpc)'); ax.set_ylabel('V (km/s)')
        ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 40)
    except:
        ax.set_title(f'{title}\nFAILED')

fig.suptitle('Representative ED-Poisson Rotation Curves', fontsize=14)
fig.tight_layout()
fig.savefig(os.path.join(FIG, 'representative_profiles', 'rotation_curves.png'), dpi=150)
plt.close()

print("  Figures saved")

# ═══ Summary ═══
flag_counts = {}
for r in results:
    flag_counts[r['flag']] = flag_counts.get(r['flag'], 0) + 1

# Core radius ranges by flag
dwarf_cores = [r['r_core'] for r in results if r['flag'] == 'dwarf']
spiral_cores = [r['r_core'] for r in results if r['flag'] == 'spiral']

# Best Burkert matches
good_burk = [r for r in results if r['chi2_burkert'] < 100 and r['flag'] != 'error']
good_burk.sort(key=lambda x: x['chi2_burkert'])

summary = {
    'experiment': 'ED-Sim-02: ED-Poisson Halo Atlas',
    'total_sets': len(results),
    'flag_counts': flag_counts,
    'dwarf_core_range': [round(min(dwarf_cores), 2), round(max(dwarf_cores), 2)] if dwarf_cores else None,
    'spiral_core_range': [round(min(spiral_cores), 2), round(max(spiral_cores), 2)] if spiral_cores else None,
    'best_burkert_matches': good_burk[:5] if good_burk else [],
}

with open(os.path.join(RES, 'final_summary.json'), 'w') as f:
    json.dump(summary, f, indent=2)

with open(os.path.join(RES, 'final_summary.md'), 'w') as f:
    f.write(f"""# ED-Sim-02: ED-Poisson Halo Atlas - Results

## Overview
- **Total parameter sets:** {len(results)}
- **Classifications:** {flag_counts}

## Core Radius Ranges
- Dwarf-like (1-5 kpc): {len(dwarf_cores)} sets, range [{min(dwarf_cores):.1f}, {max(dwarf_cores):.1f}] kpc
- Spiral-like (3-15 kpc): {len(spiral_cores)} sets, range [{min(spiral_cores):.1f}, {max(spiral_cores):.1f}] kpc

## Best Burkert Matches (top 5)
""" if dwarf_cores and spiral_cores else f"# ED-Sim-02 Results\n\nTotal: {len(results)}, Flags: {flag_counts}\n")
    if good_burk:
        f.write("| alpha | beta | sigma_v | r_core | chi2 | flag |\n")
        f.write("|-------|------|---------|--------|------|------|\n")
        for g in good_burk[:10]:
            f.write(f"| {g['alpha']} | {g['beta']} | {g['sigma_v']} | {g['r_core']} | {g['chi2_burkert']:.1f} | {g['flag']} |\n")

print(f"\n{'='*85}")
print(f"  ED-SIM-02 COMPLETE")
print(f"{'='*85}")
print(f"  Total: {len(results)} sets")
print(f"  Flags: {flag_counts}")
if dwarf_cores:
    print(f"  Dwarf cores: {len(dwarf_cores)} sets, [{min(dwarf_cores):.1f}, {max(dwarf_cores):.1f}] kpc")
if spiral_cores:
    print(f"  Spiral cores: {len(spiral_cores)} sets, [{min(spiral_cores):.1f}, {max(spiral_cores):.1f}] kpc")
if good_burk:
    print(f"  Best Burkert chi2: {good_burk[0]['chi2_burkert']:.1f} at a={good_burk[0]['alpha']}, b={good_burk[0]['beta']}, sv={good_burk[0]['sigma_v']}")
