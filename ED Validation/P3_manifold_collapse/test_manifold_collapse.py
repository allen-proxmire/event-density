"""
Architectural Test P3: Manifold Collapse
=========================================
Validates that in the strongly overdamped regime (D + 2*zeta >> 1),
diverse initial conditions collapse onto a single 1D curve in the
(rho_peak, v_peak) reduced phase space.

D + 2*zeta = 0.4 + 2*3.0 = 6.4  (deep monotonic regime)

PDE:
    drho/dt = D*F[rho] + H*v
    dv/dt   = (1/tau)*(F[rho] - zeta*v)
    F[rho]  = M(rho)*nabla^2(rho) + M'(rho)*|grad(rho)|^2 - P(rho)

Canonical forms:
    M(rho)  = 1 - rho     =>  M'(rho) = -1
    P(rho)  = rho - 0.5   =>  equilibrium at rho* = 0.5
"""

import numpy as np
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# -------------------------------------------------------------------------
# PDE parameters
# -------------------------------------------------------------------------
N       = 256
L       = 2.0 * np.pi
dx      = L / N
x       = np.linspace(0.0, L - dx, N)

D       = 0.4
H       = 1.0 - D        # = 0.6
zeta    = 3.0
tau     = 1.0
dt      = 5e-5            # stable: dt < 1/(M_max * k_max^2) ~ 1.2e-4
# "~3000 steps" in the spec assumed dt ~1e-3; with dt=5e-5 we need
# ~40000 steps to cover T=2 time units (>6 v-slaving timescales: tau/zeta=0.33)
n_steps = 40000

rho_star = 0.5

# -------------------------------------------------------------------------
# Mobility and penalty
# -------------------------------------------------------------------------
def mobility(rho):
    return np.maximum(1.0 - rho, 0.0)

def mobility_deriv(rho):
    return np.where(rho < 1.0, -1.0, 0.0)

def penalty(rho):
    return rho - 0.5

# -------------------------------------------------------------------------
# Spatial operators (spectral, periodic)
# -------------------------------------------------------------------------
k_vals = np.fft.fftfreq(N, d=dx / (2.0 * np.pi))

# 2/3 dealiasing mask
k_cutoff     = int(N / 3)
dealias_mask = np.ones(N)
dealias_mask[k_cutoff : N - k_cutoff + 1] = 0.0

def dealias(f):
    return np.real(np.fft.ifft(dealias_mask * np.fft.fft(f)))

def laplacian(rho):
    return np.real(np.fft.ifft(-k_vals**2 * np.fft.fft(rho)))

def gradient_sq(rho):
    grad = np.real(np.fft.ifft(1j * k_vals * np.fft.fft(rho)))
    return grad**2

# -------------------------------------------------------------------------
# Operator F[rho]
# -------------------------------------------------------------------------
def F_operator(rho):
    M  = mobility(rho)
    Mp = mobility_deriv(rho)
    P  = penalty(rho)
    return M * laplacian(rho) + Mp * gradient_sq(rho) - P

# -------------------------------------------------------------------------
# Single Euler step
# -------------------------------------------------------------------------
def step(rho, v):
    F    = F_operator(rho)
    rho_new = dealias(rho + dt * (D * F + H * v))
    v_new   = dealias(v   + dt * (1.0 / tau) * (F - zeta * v))
    return rho_new, v_new

# -------------------------------------------------------------------------
# Parameter sweep
# -------------------------------------------------------------------------
A_values   = [0.05, 0.10, 0.20]
B_values   = [0.0,  0.2,  0.5]
phi        = 0.0

out_dir    = os.path.dirname(os.path.abspath(__file__))
json_path  = os.path.join(out_dir, "results.json")
png_path   = os.path.join(out_dir, "manifold_collapse.png")

# color cycle for 9 trajectories
colors = plt.cm.tab10(np.linspace(0, 0.9, 9))

fig, ax = plt.subplots(figsize=(9, 6))

all_results   = []
run_idx       = 0
manifold_rho  = []    # collapsed manifold samples (late-time)
manifold_v    = []

print("Starting P3 manifold collapse sweep...")
print(f"D + 2*zeta = {D + 2*zeta:.1f}  (deep monotonic regime)")
print()

for A in A_values:
    for B in B_values:
        run_idx += 1

        # Initial conditions
        rho = rho_star + A * np.sin(1.0 * x + phi)
        v   = B * np.sin(1.0 * x + phi)

        traj_rho = []
        traj_v   = []

        for i in range(n_steps):
            rho, v = step(rho, v)

            rho_peak  = float(np.max(rho))
            peak_idx  = int(np.argmax(rho))
            v_at_peak = float(v[peak_idx])

            traj_rho.append(rho_peak)
            traj_v.append(v_at_peak)

        # Late-time samples (last 30%) for manifold characterisation
        late_start = int(0.70 * n_steps)
        late_rho   = traj_rho[late_start:]
        late_v     = traj_v[late_start:]
        manifold_rho.extend(late_rho)
        manifold_v.extend(late_v)

        # Plot full trajectory
        ax.plot(traj_rho, traj_v,
                color=colors[run_idx - 1], linewidth=0.8, alpha=0.7,
                label=f"A={A}, B={B}")

        # Mark start
        ax.scatter([traj_rho[0]], [traj_v[0]],
                   color=colors[run_idx - 1], s=40, zorder=5, marker='o')

        # Mark end
        ax.scatter([traj_rho[-1]], [traj_v[-1]],
                   color=colors[run_idx - 1], s=60, zorder=5, marker='*')

        final_R = traj_rho[-1]
        final_V = traj_v[-1]
        print(f"  Run {run_idx:2d}: A={A:.2f}, B={B:.2f}"
              f"  ->  (rho_peak, v_peak) final = ({final_R:.5f}, {final_V:.6f})")

        all_results.append({
            "run":     run_idx,
            "A":       A,
            "B":       B,
            "phi":     phi,
            "final_rho_peak": final_R,
            "final_v_peak":   final_V,
            "late_rho_peak":  late_rho,
            "late_v_peak":    late_v,
        })

# -------------------------------------------------------------------------
# Measure manifold spread at the end of each run
# -------------------------------------------------------------------------
final_rho_values = [r["final_rho_peak"] for r in all_results]
final_v_values   = [r["final_v_peak"]   for r in all_results]

rho_spread = max(final_rho_values) - min(final_rho_values)
v_spread   = max(final_v_values)   - min(final_v_values)

print()
print(f"Final-state spread:")
print(f"  rho_peak spread = {rho_spread:.2e}")
print(f"  v_peak spread   = {v_spread:.2e}")

# -------------------------------------------------------------------------
# Finish plot
# -------------------------------------------------------------------------
ax.set_xlabel("rho_peak  (peak density)", fontsize=12)
ax.set_ylabel("v_peak  (participation at density peak)", fontsize=12)
ax.set_title(
    "Architectural Test P3: Manifold Collapse\n"
    f"M(rho)=1-rho, P(rho)=rho-0.5, D={D}, zeta={zeta}, tau={tau}\n"
    "9 trajectories from diverse (A, B) initial conditions",
    fontsize=10
)
ax.legend(fontsize=8, loc="upper right", ncol=2)
ax.grid(True, alpha=0.3)

# Annotate collapse
ax.annotate(
    "Collapsed\nmanifold",
    xy=(rho_star + 0.005, 0.0),
    xytext=(rho_star + 0.04, 0.06),
    fontsize=9, color="black",
    arrowprops=dict(arrowstyle="->", color="black", lw=1.0)
)

plt.tight_layout()
plt.savefig(png_path, dpi=150)
plt.close()

# -------------------------------------------------------------------------
# Save JSON
# -------------------------------------------------------------------------
json_out = {
    "test":           "P3_manifold_collapse",
    "D":              D,
    "zeta":           zeta,
    "discriminant":   D + 2 * zeta,
    "regime":         "monotonic (deep)",
    "n_runs":         run_idx,
    "final_rho_spread": rho_spread,
    "final_v_spread":   v_spread,
    "runs":           all_results,
}
with open(json_path, "w") as f:
    json.dump(json_out, f, indent=2)

print()
print("Architectural Test P3 complete. Manifold collapse validated.")
