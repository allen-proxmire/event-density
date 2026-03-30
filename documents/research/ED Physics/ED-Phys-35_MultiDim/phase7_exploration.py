"""
phase7_exploration.py
=====================
Phase 7: Scientific exploration of the 2D ED system.

Runs:
  1. Parameter sweep across (D, amplitude, N_modes)
  2. Transient structure taxonomy
  3. Universality analysis
  4. Dimensional comparison (2D vs 1D)
  5. Scientific figure generation

All results saved to edsim2d/output/phase7/
"""

import os
import sys
import json
import time
import numpy as np
import warnings
warnings.filterwarnings('ignore')

_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _DIR)

from edsim_solver_2d import *
from invariants_2d import *

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from visualization_2d import (
    STYLE, ED_COLORS, _setup_axes, _add_grid, _make_xy_grid,
    plot_field_quad, plot_snapshot_evolution, plot_geometry_2d,
    plot_horizon_2d,
)

OUT = os.path.join(_DIR, "edsim2d", "output", "phase7")
os.makedirs(OUT, exist_ok=True)
FIG = os.path.join(OUT, "figures")
os.makedirs(FIG, exist_ok=True)


# =====================================================================
#  HELPER: run a quick simulation and return invariants at multiple times
# =====================================================================

def run_and_measure(params, rho_init, label="", verbose=False):
    """Run simulation, collect invariants at output steps."""
    state = initialize_state_2d(params, rho_init=rho_init)
    n_steps = int(np.ceil(params.T / params.dt))

    records = []
    rho_snaps = [state['rho'].copy()]
    snap_times = [0.0]

    # Initial
    F_rho = operator_F_fd_2d(state['rho'], params)
    F_bar = spatial_avg_2d(F_rho, params.hx, params.hy)
    inv0 = compute_invariants_2d(state['rho'], state['v'], F_bar, params)
    E0 = energy_2d(state['rho'], state['v'], params)
    m0 = total_mass_2d(state['rho'], params.hx, params.hy)
    records.append(_extract_scalars(inv0, E0, m0, 0.0, state['v']))

    for n in range(1, n_steps + 1):
        state = step_2d(state, params)
        if n % params.k_out == 0 or n == n_steps:
            F_rho = operator_F_fd_2d(state['rho'], params)
            F_bar = spatial_avg_2d(F_rho, params.hx, params.hy)
            inv = compute_invariants_2d(state['rho'], state['v'], F_bar, params)
            E = energy_2d(state['rho'], state['v'], params)
            m = total_mass_2d(state['rho'], params.hx, params.hy)
            records.append(_extract_scalars(inv, E, m, state['t'], state['v']))
            rho_snaps.append(state['rho'].copy())
            snap_times.append(state['t'])

    if verbose:
        print(f"  {label}: E_ratio={records[-1]['E_total']/max(records[0]['E_total'],1e-30):.4f}, "
              f"H={records[-1]['spectral_entropy']:.4f}, "
              f"A_spec={records[-1]['A_spec']:.4f}, "
              f"F={records[-1]['filamentarity']:.4f}")

    return {
        'records': records,
        'rho_snapshots': rho_snaps,
        'times': snap_times,
        'final_rho': state['rho'],
        'final_v': state['v'],
        'params': params,
        'label': label,
    }


def _extract_scalars(inv, E, m, t, v):
    spec = inv['spectral']
    dyn = inv['dynamical']
    geo = inv['geometric']
    return {
        't': t, 'v': v,
        'E_total': E['total'], 'E_potential': E['potential'], 'E_kinetic': E['kinetic'],
        'mass': m,
        'spectral_entropy': spec['spectral_entropy'],
        'renyi_2': spec['renyi_2'],
        'ed_complexity': dyn['ed_complexity'],
        'A_spec': spec['spectral_anisotropy']['anisotropy'],
        'eccentricity': spec['spectral_anisotropy']['eccentricity'],
        'filamentarity': geo['filamentarity']['filamentarity_mean'],
        'saddle_fraction': geo['filamentarity']['saddle_fraction'],
        'sheetness': geo['filamentarity']['sheetness_fraction'],
        'A_geom': geo['anisotropy_geometric']['anisotropy_geometric'],
        'curvature_rms': geo['level_set_curvature']['curvature_rms'],
        'twist_rms': geo['vorticity_structure']['twist_rms'],
        'xi_x': geo['correlation_lengths']['xi_x'],
        'xi_y': geo['correlation_lengths']['xi_y'],
        'horizon_prox': geo['horizon']['max_proximity'],
        'R_grad': dyn['dissipation_ratios']['R_grad'],
        'R_pen': dyn['dissipation_ratios']['R_pen'],
        'R_part': dyn['dissipation_ratios']['R_part'],
    }


# =====================================================================
#  1. PARAMETER SWEEP
# =====================================================================

print("=" * 72)
print("  PHASE 7: 2D SCIENTIFIC EXPLORATION")
print("=" * 72)

N_grid = 48
T_sweep = 1.0
dt_sweep = 5e-4

D_values = [0.1, 0.3, 0.5, 0.7, 0.9]
A_values = [0.01, 0.03, 0.05]
Nm_values = [1, 4]  # 1 = single mode, 4 = multi-mode

print(f"\n--- 1. Parameter sweep: {len(D_values)}x{len(A_values)}x{len(Nm_values)} = "
      f"{len(D_values)*len(A_values)*len(Nm_values)} runs ---")

sweep_results = {}
t0_total = time.time()

for D_val in D_values:
    for A_val in A_values:
        for Nm in Nm_values:
            label = f"D{D_val:.1f}_A{A_val:.2f}_Nm{Nm}"

            # Construct IC
            x = np.linspace(0, 1.0, N_grid)
            y = np.linspace(0, 1.0, N_grid)
            X, Y = np.meshgrid(x, y, indexing='ij')

            if Nm == 1:
                rho_init = 0.5 + A_val * np.cos(np.pi * X) * np.cos(np.pi * Y)
            else:
                rho_init = np.full((N_grid, N_grid), 0.5)
                A_per = A_val / np.sqrt(Nm)
                for kx in range(1, Nm + 1):
                    for ky in range(1, Nm + 1):
                        rho_init += A_per * np.cos(kx * np.pi * X) * np.cos(ky * np.pi * Y)

            rho_init = np.clip(rho_init, 1e-12, 0.999999)

            # Clamp D to valid range
            D_eff = min(max(D_val, 0.01), 0.99)

            params = EDParameters2D(
                Nx=N_grid, Ny=N_grid, Lx=1.0, Ly=1.0,
                D=D_eff, zeta=0.1, tau=1.0,
                dt=dt_sweep, T=T_sweep, method='etdrk4',
                k_out=max(1, int(T_sweep / dt_sweep / 40)),
            )

            try:
                result = run_and_measure(params, rho_init, label=label, verbose=True)
                sweep_results[label] = result
            except Exception as e:
                print(f"  {label}: FAILED ({e})")

elapsed_sweep = time.time() - t0_total
print(f"\nSweep complete: {len(sweep_results)} runs in {elapsed_sweep:.0f}s")


# =====================================================================
#  2. TRANSIENT STRUCTURE TAXONOMY
# =====================================================================

print("\n--- 2. Transient structure taxonomy ---")

# Use a representative multi-mode run to track structures over time
tax_key = "D0.3_A0.05_Nm4"
if tax_key in sweep_results:
    tax = sweep_results[tax_key]
    recs = tax['records']

    print(f"\n  Taxonomy for {tax_key} ({len(recs)} snapshots):")
    print(f"  {'t':>6s} {'H':>8s} {'F':>8s} {'saddle':>8s} {'sheet':>8s} "
          f"{'twist':>8s} {'kappa':>8s} {'H_prox':>8s}")
    for r in recs[::max(1, len(recs)//10)]:
        print(f"  {r['t']:6.3f} {r['spectral_entropy']:8.4f} {r['filamentarity']:8.4f} "
              f"{r['saddle_fraction']:8.4f} {r['sheetness']:8.4f} "
              f"{r['twist_rms']:8.4f} {r['curvature_rms']:8.4f} {r['horizon_prox']:8.4f}")

    # Classification logic
    for r in recs:
        structures = []
        if r['filamentarity'] > 0.7:
            structures.append("FILAMENT")
        if r['saddle_fraction'] > 0.3:
            structures.append("SADDLE")
        if r['sheetness'] > 0.7:
            structures.append("SHEET")
        if r['twist_rms'] > 0.1:
            structures.append("TWIST")
        if r['horizon_prox'] > 0.5:
            structures.append("HORIZON")
        if r['curvature_rms'] > 10.0:
            structures.append("HIGH_CURVATURE")
        r['structures'] = structures

    print("\n  Structure evolution:")
    for r in recs[::max(1, len(recs)//8)]:
        structs = r.get('structures', [])
        print(f"    t={r['t']:.3f}: {', '.join(structs) if structs else 'SMOOTH'}")


# =====================================================================
#  3. UNIVERSALITY ANALYSIS
# =====================================================================

print("\n--- 3. Universality analysis ---")

# Extract late-time attractor values for each run
attractor_vectors = {}
for label, result in sweep_results.items():
    recs = result['records']
    # Late-time average (last 20%)
    n_late = max(1, len(recs) // 5)
    late = recs[-n_late:]

    vec = {}
    for key in ['spectral_entropy', 'filamentarity', 'A_spec', 'A_geom',
                'R_grad', 'R_pen', 'R_part', 'curvature_rms', 'twist_rms',
                'saddle_fraction', 'xi_x', 'xi_y']:
        vals = [r[key] for r in late]
        vec[key] = np.mean(vals)
        vec[key + '_cv'] = np.std(vals) / max(abs(np.mean(vals)), 1e-15) if len(vals) > 1 else 0

    attractor_vectors[label] = vec

# Compute pairwise distances in invariant space
inv_keys = ['spectral_entropy', 'filamentarity', 'R_grad', 'R_pen',
            'saddle_fraction', 'curvature_rms']

labels_sorted = sorted(attractor_vectors.keys())
n_runs = len(labels_sorted)
vecs = np.zeros((n_runs, len(inv_keys)))
for i, lab in enumerate(labels_sorted):
    for j, key in enumerate(inv_keys):
        vecs[i, j] = attractor_vectors[lab][key]

# Normalise each column
col_std = np.std(vecs, axis=0)
col_std[col_std < 1e-15] = 1.0
vecs_norm = (vecs - np.mean(vecs, axis=0)) / col_std

# Pairwise distance matrix
dist_matrix = np.zeros((n_runs, n_runs))
for i in range(n_runs):
    for j in range(n_runs):
        dist_matrix[i, j] = np.linalg.norm(vecs_norm[i] - vecs_norm[j])

mean_dist = np.mean(dist_matrix[np.triu_indices(n_runs, k=1)])
max_dist = np.max(dist_matrix)

# Universality score: U = 1 - mean_dist/max_possible
max_possible = np.sqrt(len(inv_keys)) * 2  # rough upper bound in normalised space
U_score = 1.0 - mean_dist / max_possible

print(f"  Runs analysed: {n_runs}")
print(f"  Mean pairwise distance: {mean_dist:.4f}")
print(f"  Max pairwise distance: {max_dist:.4f}")
print(f"  Universality score U: {U_score:.4f}")

# Check which invariants are most stable (low CV)
print("\n  Late-time coefficient of variation (cross-run):")
for key in inv_keys:
    vals = [attractor_vectors[lab][key] for lab in labels_sorted]
    cv = np.std(vals) / max(abs(np.mean(vals)), 1e-15)
    mean_val = np.mean(vals)
    verdict = "STABLE" if cv < 0.3 else "VARIABLE"
    print(f"    {key:>20s}: mean={mean_val:8.4f}, CV={cv:.4f} [{verdict}]")

# Check convergence: does each run's late-time invariant plateau?
print("\n  Per-run convergence (spectral entropy CV in last 20%):")
n_converged = 0
for lab in labels_sorted:
    cv = attractor_vectors[lab].get('spectral_entropy_cv', 0)
    converged = cv < 0.05
    n_converged += converged
print(f"  Converged: {n_converged}/{n_runs} (CV < 5%)")


# =====================================================================
#  4. DIMENSIONAL EFFECTS (2D vs 1D comparison)
# =====================================================================

print("\n--- 4. Dimensional effects ---")

# Run a 1D-embedded simulation (y-invariant IC in 2D)
print("  Running 1D-embedded comparison...")
x1d = np.linspace(0, 1, N_grid)
y1d = np.linspace(0, 1, N_grid)
X1d, Y1d = np.meshgrid(x1d, y1d, indexing='ij')
rho_1d_in_2d = 0.5 + 0.05 * np.cos(np.pi * X1d)
params_1d = EDParameters2D(Nx=N_grid, Ny=N_grid, dt=dt_sweep, T=T_sweep,
                           D=0.3, method='etdrk4',
                           k_out=max(1, int(T_sweep / dt_sweep / 40)))
res_1d = run_and_measure(params_1d, rho_1d_in_2d, label="1D_embed", verbose=True)

# Run the isotropic 2D cosine with same amplitude
rho_2d_cos = 0.5 + 0.05 * np.cos(np.pi * X1d) * np.cos(np.pi * Y1d)
params_2d = EDParameters2D(Nx=N_grid, Ny=N_grid, dt=dt_sweep, T=T_sweep,
                           D=0.3, method='etdrk4',
                           k_out=max(1, int(T_sweep / dt_sweep / 40)))
res_2d = run_and_measure(params_2d, rho_2d_cos, label="2D_cos", verbose=True)

# Compare late-time
late_1d = res_1d['records'][-1]
late_2d = res_2d['records'][-1]

print("\n  1D-embedded vs 2D isotropic (late-time):")
print(f"  {'Invariant':>20s} {'1D-embed':>12s} {'2D-iso':>12s} {'Ratio':>10s}")
for key in ['spectral_entropy', 'ed_complexity', 'filamentarity', 'A_spec',
            'saddle_fraction', 'curvature_rms', 'R_grad', 'R_pen']:
    v1 = late_1d[key]
    v2 = late_2d[key]
    ratio = v2 / max(abs(v1), 1e-15) if abs(v1) > 1e-15 else float('inf')
    print(f"  {key:>20s} {v1:12.6f} {v2:12.6f} {ratio:10.4f}")

# Unique attractor test: do runs with different ICs converge to same attractor?
print("\n  Unique attractor test (same D, different ICs):")
d03_runs = {k: v for k, v in sweep_results.items() if k.startswith("D0.3")}
if len(d03_runs) >= 2:
    d03_labels = sorted(d03_runs.keys())
    H_late = [d03_runs[lab]['records'][-1]['spectral_entropy'] for lab in d03_labels]
    C_late = [d03_runs[lab]['records'][-1]['ed_complexity'] for lab in d03_labels]
    print(f"  D=0.3 runs: {d03_labels}")
    print(f"  H_late: {[f'{h:.4f}' for h in H_late]}")
    print(f"  C_late: {[f'{c:.6f}' for c in C_late]}")
    print(f"  H spread: {np.std(H_late):.4f} (CV={np.std(H_late)/max(np.mean(H_late),1e-15):.4f})")
    print(f"  C spread: {np.std(C_late):.6f}")


# =====================================================================
#  5. SCIENTIFIC FIGURES
# =====================================================================

print("\n--- 5. Generating scientific figures ---")

# Fig 1: Transient evolution for multi-mode run
if tax_key in sweep_results:
    tax = sweep_results[tax_key]
    fig = plot_snapshot_evolution(tax['rho_snapshots'], tax['times'],
                                 tax['params'], n_show=6)
    fig.savefig(os.path.join(FIG, "fig1_transient_evolution.png"),
                dpi=200, bbox_inches='tight')
    plt.close(fig)
    print("  fig1_transient_evolution.png")

# Fig 2: Spectral entropy evolution across D values
fig, ax = plt.subplots(figsize=(8, 5))
for D_val in D_values:
    key = f"D{D_val:.1f}_A0.05_Nm1"
    if key in sweep_results:
        recs = sweep_results[key]['records']
        ts = [r['t'] for r in recs]
        Hs = [r['spectral_entropy'] for r in recs]
        ax.plot(ts, Hs, lw=1.5, label=f"D={D_val}")
ax.legend(fontsize=9)
_setup_axes(ax, "$t$", "Spectral entropy $H$", "Spectral entropy vs $D$")
_add_grid(ax)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig2_spectral_entropy_vs_D.png"),
            dpi=200, bbox_inches='tight')
plt.close(fig)
print("  fig2_spectral_entropy_vs_D.png")

# Fig 3: Filamentarity evolution across D values
fig, ax = plt.subplots(figsize=(8, 5))
for D_val in D_values:
    key = f"D{D_val:.1f}_A0.05_Nm4"
    if key in sweep_results:
        recs = sweep_results[key]['records']
        ts = [r['t'] for r in recs]
        Fs = [r['filamentarity'] for r in recs]
        ax.plot(ts, Fs, lw=1.5, label=f"D={D_val}")
ax.legend(fontsize=9)
_setup_axes(ax, "$t$", "Filamentarity $F$", "Filamentarity vs $D$ (multi-mode)")
_add_grid(ax)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig3_filamentarity_vs_D.png"),
            dpi=200, bbox_inches='tight')
plt.close(fig)
print("  fig3_filamentarity_vs_D.png")

# Fig 4: Energy decay across D values
fig, ax = plt.subplots(figsize=(8, 5))
for D_val in D_values:
    key = f"D{D_val:.1f}_A0.05_Nm1"
    if key in sweep_results:
        recs = sweep_results[key]['records']
        ts = [r['t'] for r in recs]
        Es = [r['E_total'] for r in recs]
        E0 = max(Es[0], 1e-30)
        ax.semilogy(ts, [e/E0 for e in Es], lw=1.5, label=f"D={D_val}")
ax.legend(fontsize=9)
_setup_axes(ax, "$t$", "$E(t)/E(0)$", "Energy decay vs $D$")
_add_grid(ax)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig4_energy_decay_vs_D.png"),
            dpi=200, bbox_inches='tight')
plt.close(fig)
print("  fig4_energy_decay_vs_D.png")

# Fig 5: Dissipation ratio evolution
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for i_ax, (channel, title) in enumerate([('R_grad', '$R_{grad}$'),
                                          ('R_pen', '$R_{pen}$'),
                                          ('R_part', '$R_{part}$')]):
    for D_val in [0.1, 0.3, 0.5, 0.9]:
        key = f"D{D_val:.1f}_A0.05_Nm1"
        if key in sweep_results:
            recs = sweep_results[key]['records']
            ts = [r['t'] for r in recs]
            vals = [r[channel] for r in recs]
            axes[i_ax].plot(ts, vals, lw=1.5, label=f"D={D_val}")
    axes[i_ax].legend(fontsize=8)
    _setup_axes(axes[i_ax], "$t$", title, title)
    _add_grid(axes[i_ax])
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig5_dissipation_ratios.png"),
            dpi=200, bbox_inches='tight')
plt.close(fig)
print("  fig5_dissipation_ratios.png")

# Fig 6: Anisotropy trajectory (A_spec, A_geom) over time
fig, ax = plt.subplots(figsize=(7, 6))
for key_label, color in [("D0.3_A0.05_Nm4", ED_COLORS["blue"]),
                          ("D0.7_A0.05_Nm4", ED_COLORS["red"]),
                          ("D0.1_A0.05_Nm4", ED_COLORS["green"])]:
    if key_label in sweep_results:
        recs = sweep_results[key_label]['records']
        As = [r['A_spec'] for r in recs]
        Ag = [r['A_geom'] for r in recs]
        ax.plot(As, Ag, '-o', ms=3, lw=1.2, color=color,
                label=key_label, alpha=0.7)
        ax.plot(As[0], Ag[0], 'o', ms=8, color=color)  # start
        ax.plot(As[-1], Ag[-1], 's', ms=8, color=color)  # end
ax.plot([0, 1], [0, 1], 'k--', lw=0.5, alpha=0.3)
ax.legend(fontsize=8)
_setup_axes(ax, "$A_{spec}$", "$A_{geom}$", "Anisotropy trajectory")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig6_anisotropy_trajectory.png"),
            dpi=200, bbox_inches='tight')
plt.close(fig)
print("  fig6_anisotropy_trajectory.png")

# Fig 7: Geometry quad for multi-mode at late time
for key_label in ["D0.3_A0.05_Nm4"]:
    if key_label in sweep_results:
        r = sweep_results[key_label]
        fig = plot_geometry_2d(r['final_rho'], r['params'])
        fig.savefig(os.path.join(FIG, f"fig7_geometry_{key_label}.png"),
                    dpi=200, bbox_inches='tight')
        plt.close(fig)
        print(f"  fig7_geometry_{key_label}.png")

# Fig 8: Universality scatter (H_late vs D)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
for Nm in [1, 4]:
    for A_val in A_values:
        Ds = []
        Hs = []
        Cs = []
        for D_val in D_values:
            key = f"D{D_val:.1f}_A{A_val:.2f}_Nm{Nm}"
            if key in attractor_vectors:
                Ds.append(D_val)
                Hs.append(attractor_vectors[key]['spectral_entropy'])
                Cs.append(attractor_vectors[key].get('R_grad', 0))
        if Ds:
            marker = 'o' if Nm == 1 else 's'
            axes[0].plot(Ds, Hs, f'{marker}-', ms=5, lw=1,
                        label=f"A={A_val}, Nm={Nm}", alpha=0.7)
            axes[1].plot(Ds, Cs, f'{marker}-', ms=5, lw=1,
                        label=f"A={A_val}, Nm={Nm}", alpha=0.7)
axes[0].legend(fontsize=7)
_setup_axes(axes[0], "$D$", "$H^*$", "(a) Attractor entropy vs $D$")
_add_grid(axes[0])
axes[1].legend(fontsize=7)
_setup_axes(axes[1], "$D$", "$R_{grad}^*$", "(b) Gradient fraction vs $D$")
_add_grid(axes[1])
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig8_universality_scatter.png"),
            dpi=200, bbox_inches='tight')
plt.close(fig)
print("  fig8_universality_scatter.png")


# =====================================================================
#  SAVE SWEEP DATA
# =====================================================================

sweep_summary = {}
for label, result in sweep_results.items():
    recs = result['records']
    sweep_summary[label] = {
        'initial': {k: v for k, v in recs[0].items() if k != 'structures'},
        'final': {k: v for k, v in recs[-1].items() if k != 'structures'},
    }

with open(os.path.join(OUT, "sweep_summary.json"), "w") as f:
    json.dump(sweep_summary, f, indent=2, default=lambda o: float(o) if isinstance(o, (np.floating, np.integer)) else str(o))
print(f"\nSweep summary saved to {os.path.join(OUT, 'sweep_summary.json')}")


# =====================================================================
print("\n" + "=" * 72)
print(f"  PHASE 7 COMPLETE — {len(sweep_results)} runs, "
      f"8 figures, {elapsed_sweep:.0f}s total")
print("=" * 72)
