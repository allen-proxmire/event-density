"""
phase11_exploration_3d.py
=========================
Phase 11: Scientific exploration of the 3D ED system.

Runs:
  1. Parameter sweep across (D, amplitude, N_modes) — smaller grids for 3D
  2. Transient structure taxonomy
  3. Universality analysis
  4. Dimensional comparison (1D → 2D → 3D)
  5. Scientific figure generation

All results saved to edsim2d/output/phase11/
"""

import os, sys, json, time
import numpy as np
import warnings
warnings.filterwarnings('ignore')

_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _DIR)

from edsim_solver_3d import *
from invariants_3d import *
from edsim_solver_2d import (EDParameters2D, initialize_state_2d, step_2d,
                              energy_2d, total_mass_2d, spatial_avg_2d,
                              operator_F_fd_2d)
from invariants_2d import (compute_invariants_2d, ed_complexity_2d,
                           spectral_entropy_2d, modal_amplitudes_2d,
                           dissipation_channels_2d)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from visualization_3d import (STYLE, ED_COLORS, _setup_axes, _add_grid,
                               plot_density_slices, plot_morphology_slices,
                               plot_curvature_slices, plot_horizon_slices,
                               plot_invariants_3d, plot_anisotropy_ellipsoid,
                               plot_max_intensity_projection)

OUT = os.path.join(_DIR, "edsim2d", "output", "phase11")
os.makedirs(OUT, exist_ok=True)
FIG = os.path.join(OUT, "figures")
os.makedirs(FIG, exist_ok=True)


# =====================================================================
#  HELPER: run a 3D sim and extract invariant scalars
# =====================================================================

def run_and_measure_3d(params, rho_init, label="", verbose=False):
    state = initialize_state_3d(params, rho_init=rho_init)
    n_steps = int(np.ceil(params.T / params.dt))
    records = []

    def snap(s, t):
        F = operator_F_fd_3d(s['rho'], params)
        F_bar = spatial_avg_3d(F, params.hx, params.hy, params.hz)
        inv = compute_invariants_3d(s['rho'], s['v'], F_bar, params, K_max=6)
        E = energy_3d(s['rho'], s['v'], params)
        m = total_mass_3d(s['rho'], params.hx, params.hy, params.hz)
        sp = inv['spectral']; dy = inv['dynamical']; ge = inv['geometric']
        return {
            't': t, 'v': s['v'],
            'E_total': E['total'], 'mass': m,
            'spectral_entropy': sp['spectral_entropy'],
            'ed_complexity': dy['ed_complexity'],
            'isotropy': sp['spectral_anisotropy']['isotropy'],
            'planarity': sp['spectral_anisotropy']['planarity'],
            'linearity': sp['spectral_anisotropy']['linearity'],
            'filament_frac': ge['morphology']['filament_fraction'],
            'sheet_frac': ge['morphology']['sheet_fraction'],
            'blob_frac': ge['morphology']['blob_fraction'],
            'twist_rms': ge['twist']['twist_rms'],
            'H_curv_rms': ge['curvature']['mean_curvature_rms'],
            'K_curv_rms': ge['curvature']['gaussian_curvature_rms'],
            'horizon_prox': ge['horizon']['max_proximity'],
            'horizon_frac': ge['horizon']['horizon_fraction'],
            'R_grad': dy['dissipation_ratios']['R_grad'],
            'R_pen': dy['dissipation_ratios']['R_pen'],
            'R_part': dy['dissipation_ratios']['R_part'],
            'xi_x': ge['correlation_lengths']['xi_x'],
            'xi_y': ge['correlation_lengths']['xi_y'],
            'xi_z': ge['correlation_lengths']['xi_z'],
            'mink_chi': ge['minkowski']['chi'],
        }

    records.append(snap(state, 0.0))
    for n in range(1, n_steps + 1):
        state = step_3d(state, params)
        if n % params.k_out == 0 or n == n_steps:
            records.append(snap(state, state['t']))

    if verbose:
        r = records[-1]
        print(f"  {label}: E_ratio={r['E_total']/max(records[0]['E_total'],1e-30):.4f}, "
              f"H={r['spectral_entropy']:.3f}, F/S/B={r['filament_frac']:.2f}/"
              f"{r['sheet_frac']:.2f}/{r['blob_frac']:.2f}, "
              f"H_prox={r['horizon_prox']:.3f}")

    return {'records': records, 'final_rho': state['rho'],
            'final_v': state['v'], 'params': params, 'label': label}


# =====================================================================
#  HELPER: run equivalent 2D sim
# =====================================================================

def run_and_measure_2d(D, amp, Nm, N, T, dt):
    x = np.linspace(0, 1, N); y = np.linspace(0, 1, N)
    X, Y = np.meshgrid(x, y, indexing='ij')
    if Nm == 1:
        rho_init = 0.5 + amp * np.cos(np.pi * X) * np.cos(np.pi * Y)
    else:
        rho_init = np.full((N, N), 0.5)
        A_per = amp / np.sqrt(Nm)
        for kk in range(1, Nm + 1):
            rho_init += A_per * np.cos(kk * np.pi * X) * np.cos(kk * np.pi * Y)
    rho_init = np.clip(rho_init, 1e-12, 0.999999)
    p2 = EDParameters2D(Nx=N, Ny=N, D=min(max(D, 0.01), 0.99), dt=dt, T=T,
                        method='etdrk4', k_out=max(1, int(T/dt/10)))
    state = initialize_state_2d(p2, rho_init=rho_init)
    n_steps = int(np.ceil(T / dt))
    for _ in range(n_steps):
        state = step_2d(state, p2)
    F = operator_F_fd_2d(state['rho'], p2)
    F_bar = spatial_avg_2d(F, p2.hx, p2.hy)
    inv = compute_invariants_2d(state['rho'], state['v'], F_bar, p2)
    E = energy_2d(state['rho'], state['v'], p2)
    return {
        'E_total': E['total'],
        'ed_complexity': inv['dynamical']['ed_complexity'],
        'spectral_entropy': inv['spectral']['spectral_entropy'],
        'R_grad': inv['dynamical']['dissipation_ratios']['R_grad'],
        'R_pen': inv['dynamical']['dissipation_ratios']['R_pen'],
    }


# =====================================================================
print("=" * 72)
print("  PHASE 11: 3D SCIENTIFIC EXPLORATION")
print("=" * 72)

# =====================================================================
#  1. PARAMETER SWEEP
# =====================================================================

N3 = 16  # 3D grid: 16^3 = 4096 points (fast enough for sweep)
T_sw = 0.5
dt_sw = 1e-3

D_values = [0.1, 0.3, 0.5, 0.7, 0.9]
A_values = [0.01, 0.03]
Nm_values = [1, 2]  # single mode vs 8-mode (2^3)

print(f"\n--- 1. 3D Parameter sweep: {len(D_values)}x{len(A_values)}x{len(Nm_values)} = "
      f"{len(D_values)*len(A_values)*len(Nm_values)} runs, N={N3}^3 ---")

sweep = {}
t0 = time.time()

for D_val in D_values:
    for A_val in A_values:
        for Nm in Nm_values:
            label = f"D{D_val:.1f}_A{A_val:.2f}_Nm{Nm}"
            x = np.linspace(0, 1, N3); y = np.linspace(0, 1, N3); z = np.linspace(0, 1, N3)
            X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

            if Nm == 1:
                rho_init = 0.5 + A_val * np.cos(np.pi*X) * np.cos(np.pi*Y) * np.cos(np.pi*Z)
            else:
                rho_init = np.full((N3, N3, N3), 0.5)
                A_per = A_val / np.sqrt(Nm**3)
                for kx in range(1, Nm+1):
                    for ky in range(1, Nm+1):
                        for kz in range(1, Nm+1):
                            rho_init += A_per * np.cos(kx*np.pi*X)*np.cos(ky*np.pi*Y)*np.cos(kz*np.pi*Z)
            rho_init = np.clip(rho_init, 1e-12, 0.999999)

            params = EDParameters3D(Nx=N3, Ny=N3, Nz=N3, D=min(max(D_val,0.01),0.99),
                                    dt=dt_sw, T=T_sw, method='etdrk4',
                                    k_out=max(1, int(T_sw/dt_sw/10)))
            try:
                result = run_and_measure_3d(params, rho_init, label=label, verbose=True)
                sweep[label] = result
            except Exception as e:
                print(f"  {label}: FAILED ({e})")

elapsed = time.time() - t0
print(f"\nSweep: {len(sweep)} runs in {elapsed:.0f}s")


# =====================================================================
#  2. TRANSIENT STRUCTURE TAXONOMY
# =====================================================================

print("\n--- 2. 3D Transient structure taxonomy ---")

tax_key = "D0.3_A0.03_Nm2"
if tax_key in sweep:
    tax = sweep[tax_key]
    recs = tax['records']
    print(f"\n  Taxonomy for {tax_key} ({len(recs)} snapshots):")
    print(f"  {'t':>6s} {'H':>7s} {'F':>6s} {'S':>6s} {'B':>6s} "
          f"{'twist':>7s} {'H_curv':>7s} {'H_prox':>7s} {'chi':>5s}")
    for r in recs:
        print(f"  {r['t']:6.3f} {r['spectral_entropy']:7.3f} "
              f"{r['filament_frac']:6.3f} {r['sheet_frac']:6.3f} {r['blob_frac']:6.3f} "
              f"{r['twist_rms']:7.4f} {r['H_curv_rms']:7.4f} "
              f"{r['horizon_prox']:7.4f} {r['mink_chi']:5d}")

    print("\n  Structure classification over time:")
    for r in recs:
        structs = []
        if r['filament_frac'] > 0.4: structs.append("FILAMENT")
        if r['sheet_frac'] > 0.4: structs.append("SHEET")
        if r['blob_frac'] > 0.4: structs.append("BLOB")
        if r['twist_rms'] > 0.05: structs.append("TWIST")
        if r['horizon_prox'] > 0.5: structs.append("HORIZON")
        if r['H_curv_rms'] > 5: structs.append("HIGH_CURV")
        print(f"    t={r['t']:.3f}: {', '.join(structs) if structs else 'SMOOTH'}")


# =====================================================================
#  3. UNIVERSALITY ANALYSIS
# =====================================================================

print("\n--- 3. Universality analysis ---")

attractor_vecs = {}
for label, result in sweep.items():
    recs = result['records']
    n_late = max(1, len(recs) // 5)
    late = recs[-n_late:]
    vec = {}
    for key in ['spectral_entropy', 'filament_frac', 'sheet_frac', 'blob_frac',
                'R_grad', 'R_pen', 'twist_rms', 'H_curv_rms', 'xi_x']:
        vals = [r[key] for r in late]
        vec[key] = np.mean(vals)
    attractor_vecs[label] = vec

inv_keys = ['spectral_entropy', 'filament_frac', 'sheet_frac', 'R_grad', 'twist_rms']
labels_sorted = sorted(attractor_vecs.keys())
n_runs = len(labels_sorted)
vecs = np.zeros((n_runs, len(inv_keys)))
for i, lab in enumerate(labels_sorted):
    for j, key in enumerate(inv_keys):
        vecs[i, j] = attractor_vecs[lab][key]

col_std = np.std(vecs, axis=0)
col_std[col_std < 1e-15] = 1.0
vecs_norm = (vecs - np.mean(vecs, axis=0)) / col_std

dist_mat = np.zeros((n_runs, n_runs))
for i in range(n_runs):
    for j in range(n_runs):
        dist_mat[i, j] = np.linalg.norm(vecs_norm[i] - vecs_norm[j])

mean_dist = np.mean(dist_mat[np.triu_indices(n_runs, k=1)])
max_dist = np.max(dist_mat)
U_score = 1.0 - mean_dist / (np.sqrt(len(inv_keys)) * 2)

print(f"  Runs: {n_runs}")
print(f"  Mean pairwise distance: {mean_dist:.4f}")
print(f"  Universality score U: {U_score:.4f}")

print("\n  Cross-run CV of invariants:")
for key in inv_keys:
    vals = [attractor_vecs[lab][key] for lab in labels_sorted]
    cv = np.std(vals) / max(abs(np.mean(vals)), 1e-15)
    print(f"    {key:>20s}: mean={np.mean(vals):8.4f}, CV={cv:.4f}")


# =====================================================================
#  4. DIMENSIONAL COMPARISON (1D → 2D → 3D)
# =====================================================================

print("\n--- 4. Dimensional effects ---")

N_dim = 24  # Common grid size per axis
T_dim = 0.5
dt_dim = 5e-4
D_dim = 0.3
amp_dim = 0.03

# 3D single-mode run
print("  Running 3D single-mode...")
x3 = np.linspace(0,1,N_dim); y3 = np.linspace(0,1,N_dim); z3 = np.linspace(0,1,N_dim)
X3, Y3, Z3 = np.meshgrid(x3, y3, z3, indexing='ij')
rho3 = 0.5 + amp_dim * np.cos(np.pi*X3) * np.cos(np.pi*Y3) * np.cos(np.pi*Z3)
p3 = EDParameters3D(Nx=N_dim, Ny=N_dim, Nz=N_dim, D=D_dim, dt=dt_dim, T=T_dim,
                    method='etdrk4', k_out=max(1, int(T_dim/dt_dim/10)))
res3 = run_and_measure_3d(p3, rho3, label="3D_cos", verbose=True)
r3 = res3['records'][-1]

# 2D single-mode run
print("  Running 2D single-mode...")
r2 = run_and_measure_2d(D_dim, amp_dim, 1, N_dim, T_dim, dt_dim)

# 1D: embed in 2D (y-invariant)
print("  Running 1D-embedded...")
x1 = np.linspace(0,1,N_dim); y1 = np.linspace(0,1,N_dim)
X1, Y1 = np.meshgrid(x1, y1, indexing='ij')
rho1 = 0.5 + amp_dim * np.cos(np.pi * X1)
r1 = run_and_measure_2d(D_dim, amp_dim, 1, N_dim, T_dim, dt_dim)
# For 1D, use x-only IC
p1d = EDParameters2D(Nx=N_dim, Ny=N_dim, D=D_dim, dt=dt_dim, T=T_dim,
                     method='etdrk4', k_out=max(1, int(T_dim/dt_dim/10)))
state1 = initialize_state_2d(p1d, rho_init=rho1)
for _ in range(int(T_dim/dt_dim)):
    state1 = step_2d(state1, p1d)
C_1d = ed_complexity_2d(state1['rho'], p1d.hx, p1d.hy)

print(f"\n  Dimensional comparison (D={D_dim}, A={amp_dim}, T={T_dim}):")
print(f"  {'Measure':>25s} {'1D-embed':>12s} {'2D':>12s} {'3D':>12s}")
print(f"  {'ED complexity':>25s} {C_1d:12.6f} {r2['ed_complexity']:12.6f} {r3['ed_complexity']:12.6f}")
print(f"  {'Spectral entropy':>25s} {'--':>12s} {r2['spectral_entropy']:12.4f} {r3['spectral_entropy']:12.4f}")
print(f"  {'R_grad':>25s} {'--':>12s} {r2['R_grad']:12.4f} {r3['R_grad']:12.4f}")
print(f"  {'R_pen':>25s} {'--':>12s} {r2['R_pen']:12.4f} {r3['R_pen']:12.4f}")

# Complexity dilution ratios
if C_1d > 0 and r2['ed_complexity'] > 0:
    print(f"\n  Complexity dilution:")
    print(f"    C_2D / C_1D = {r2['ed_complexity'] / C_1d:.4f}")
    print(f"    C_3D / C_1D = {r3['ed_complexity'] / C_1d:.4f}")
    print(f"    C_3D / C_2D = {r3['ed_complexity'] / r2['ed_complexity']:.4f}")

# Morphology in 3D
print(f"\n  3D Morphology (late-time):")
print(f"    Filament: {r3['filament_frac']:.3f}")
print(f"    Sheet:    {r3['sheet_frac']:.3f}")
print(f"    Blob:     {r3['blob_frac']:.3f}")

# R_grad across dimensions
print(f"\n  R_grad scaling:")
print(f"    2D: {r2['R_grad']:.4f}")
print(f"    3D: {r3['R_grad']:.4f}")


# =====================================================================
#  5. SCIENTIFIC FIGURES
# =====================================================================

print("\n--- 5. Generating scientific figures ---")

# Fig 1: Density slices for multi-mode run
key_mm = "D0.3_A0.03_Nm2"
if key_mm in sweep:
    fig1 = plot_density_slices(sweep[key_mm]['final_rho'], sweep[key_mm]['params'],
                               title="Fig 1: 3D Density (D=0.3, multi-mode)")
    fig1.savefig(os.path.join(FIG, "fig1_density_slices.png"), dpi=200, bbox_inches='tight')
    plt.close(fig1)
    print("  fig1_density_slices.png")

# Fig 2: Morphology slices
if key_mm in sweep:
    fig2 = plot_morphology_slices(sweep[key_mm]['final_rho'], sweep[key_mm]['params'],
                                  title="Fig 2: 3D Morphology")
    fig2.savefig(os.path.join(FIG, "fig2_morphology.png"), dpi=200, bbox_inches='tight')
    plt.close(fig2)
    print("  fig2_morphology.png")

# Fig 3: Spectral entropy vs D
fig3, ax3 = plt.subplots(figsize=(8, 5))
for Nm in Nm_values:
    for A in A_values:
        Ds = []; Hs = []
        for D_val in D_values:
            key = f"D{D_val:.1f}_A{A:.2f}_Nm{Nm}"
            if key in attractor_vecs:
                Ds.append(D_val)
                Hs.append(attractor_vecs[key]['spectral_entropy'])
        if Ds:
            marker = 'o' if Nm == 1 else 's'
            ax3.plot(Ds, Hs, f'{marker}-', ms=5, lw=1.2, label=f"A={A}, Nm={Nm}")
ax3.legend(fontsize=8)
_setup_axes(ax3, "$D$", "$H^*$", "Fig 3: Attractor entropy vs $D$ (3D)")
_add_grid(ax3)
fig3.tight_layout()
fig3.savefig(os.path.join(FIG, "fig3_entropy_vs_D.png"), dpi=200, bbox_inches='tight')
plt.close(fig3)
print("  fig3_entropy_vs_D.png")

# Fig 4: Morphology fractions vs D (multi-mode)
fig4, ax4 = plt.subplots(figsize=(8, 5))
for D_val in D_values:
    key = f"D{D_val:.1f}_A0.03_Nm2"
    if key in attractor_vecs:
        v = attractor_vecs[key]
        ax4.bar(D_val - 0.03, v['filament_frac'], width=0.02, color=ED_COLORS["red"],
                label='Filament' if D_val == D_values[0] else "")
        ax4.bar(D_val, v['sheet_frac'], width=0.02, color=ED_COLORS["blue"],
                label='Sheet' if D_val == D_values[0] else "")
        ax4.bar(D_val + 0.03, v['blob_frac'], width=0.02, color=ED_COLORS["green"],
                label='Blob' if D_val == D_values[0] else "")
ax4.legend(fontsize=9)
_setup_axes(ax4, "$D$", "Volume fraction", "Fig 4: 3D Morphology vs $D$")
fig4.tight_layout()
fig4.savefig(os.path.join(FIG, "fig4_morphology_vs_D.png"), dpi=200, bbox_inches='tight')
plt.close(fig4)
print("  fig4_morphology_vs_D.png")

# Fig 5: Dissipation partition vs D
fig5, ax5 = plt.subplots(figsize=(8, 5))
for Nm in [1, 2]:
    Ds = []; Rgs = []
    for D_val in D_values:
        key = f"D{D_val:.1f}_A0.03_Nm{Nm}"
        if key in attractor_vecs:
            Ds.append(D_val)
            Rgs.append(attractor_vecs[key]['R_grad'])
    if Ds:
        marker = 'o' if Nm == 1 else 's'
        ax5.plot(Ds, Rgs, f'{marker}-', lw=1.5, label=f"Nm={Nm}")
ax5.legend(fontsize=9)
_setup_axes(ax5, "$D$", "$R_{grad}^*$", "Fig 5: Gradient dissipation fraction vs $D$ (3D)")
_add_grid(ax5)
fig5.tight_layout()
fig5.savefig(os.path.join(FIG, "fig5_Rgrad_vs_D.png"), dpi=200, bbox_inches='tight')
plt.close(fig5)
print("  fig5_Rgrad_vs_D.png")

# Fig 6: Complexity dilution bar chart (1D, 2D, 3D)
fig6, ax6 = plt.subplots(figsize=(6, 5))
cs = [C_1d, r2['ed_complexity'], r3['ed_complexity']]
bars = ax6.bar(['1D', '2D', '3D'], cs,
               color=[ED_COLORS["blue"], ED_COLORS["red"], ED_COLORS["green"]])
ax6.set_ylabel("$C_{ED}$", fontsize=STYLE["font_label"])
ax6.set_title("Fig 6: Complexity dilution (D=0.3, A=0.03)", fontsize=STYLE["font_title"], fontweight="bold")
for b, c in zip(bars, cs):
    ax6.text(b.get_x() + b.get_width()/2, b.get_height(), f"{c:.4e}",
             ha='center', va='bottom', fontsize=8)
fig6.tight_layout()
fig6.savefig(os.path.join(FIG, "fig6_complexity_dilution.png"), dpi=200, bbox_inches='tight')
plt.close(fig6)
print("  fig6_complexity_dilution.png")

# Fig 7: Horizon proximity for near-horizon run
near_key = "D0.9_A0.03_Nm2"
if near_key in sweep:
    fig7 = plot_horizon_slices(sweep[near_key]['final_rho'], sweep[near_key]['params'],
                               title="Fig 7: Horizon proximity (D=0.9)")
    fig7.savefig(os.path.join(FIG, "fig7_horizon.png"), dpi=200, bbox_inches='tight')
    plt.close(fig7)
    print("  fig7_horizon.png")

# Fig 8: MIP for Gaussian-like evolved field
sm_key = "D0.3_A0.03_Nm1"
if sm_key in sweep:
    fig8 = plot_max_intensity_projection(sweep[sm_key]['final_rho'], sweep[sm_key]['params'],
                                          title="Fig 8: Max-intensity projection (D=0.3)")
    fig8.savefig(os.path.join(FIG, "fig8_mip.png"), dpi=200, bbox_inches='tight')
    plt.close(fig8)
    print("  fig8_mip.png")

# Fig 9: Invariant dashboard for multi-mode
if key_mm in sweep:
    rho_f = sweep[key_mm]['final_rho']
    p_f = sweep[key_mm]['params']
    F_f = operator_F_fd_3d(rho_f, p_f)
    Fb = spatial_avg_3d(F_f, p_f.hx, p_f.hy, p_f.hz)
    inv_f = compute_invariants_3d(rho_f, sweep[key_mm]['final_v'], Fb, p_f)
    fig9 = plot_invariants_3d(inv_f, p_f)
    fig9.savefig(os.path.join(FIG, "fig9_invariants.png"), dpi=200, bbox_inches='tight')
    plt.close(fig9)
    print("  fig9_invariants.png")


# =====================================================================
#  SAVE SWEEP DATA
# =====================================================================

sweep_summary = {}
for label, result in sweep.items():
    recs = result['records']
    sweep_summary[label] = {
        'initial': {k: v for k, v in recs[0].items()},
        'final': {k: v for k, v in recs[-1].items()},
    }

with open(os.path.join(OUT, "sweep_summary_3d.json"), "w") as f:
    json.dump(sweep_summary, f, indent=2,
              default=lambda o: float(o) if isinstance(o, (np.floating, np.integer)) else str(o))

print(f"\nSweep data saved to {os.path.join(OUT, 'sweep_summary_3d.json')}")

print("\n" + "=" * 72)
print(f"  PHASE 11 COMPLETE — {len(sweep)} runs, 9 figures, {elapsed:.0f}s sweep")
print("=" * 72)
