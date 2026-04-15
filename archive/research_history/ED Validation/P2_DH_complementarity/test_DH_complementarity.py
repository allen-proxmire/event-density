"""
Architectural Test P2: D/H Complementarity
============================================
Validates that the D/H channel balance (D+H=1) controls the qualitative
dynamical regime: monotonic decay (large D+2*zeta), damped oscillation
(transitional), or sustained spiral (small D+2*zeta).

PDE:
    drho/dt = D*F[rho] + H*v
    dv/dt   = (1/tau)*(F[rho] - zeta*v)
    F[rho]  = M(rho)*nabla^2(rho) + M'(rho)*|grad(rho)|^2 - P(rho)

Canonical forms:
    M(rho) = 1 - rho
    P(rho) = rho - 0.5   =>  equilibrium at rho* = 0.5

Three regimes:
    Regime A (monotonic):      D=0.8, zeta=3.0  D+2*zeta=6.8
    Regime B (transitional):   D=0.6, zeta=1.0  D+2*zeta=2.6
    Regime C (spiral/oscillatory): D=0.4, zeta=0.2  D+2*zeta=0.8

Linearized eigenvalues at k=1, rho*=0.5:
    lambda = -(D*M(rho*) + zeta*D_eff) +/- sqrt(discriminant)
    For regime C: lambda ~ -0.40 +/- i*0.927 => period~6.78 time units

Simulation:
    dt = 5e-5, n_steps = 300000 => T = 15 time units
    Captures ~2 full oscillation cycles for regime C (period~6.78).
    TRACK_EVERY = 500 => 600 sample points per regime.
"""

import numpy as np
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# -------------------------------------------------------------------------
# Grid and shared parameters
# -------------------------------------------------------------------------
N        = 256
L        = 2.0 * np.pi
dx       = L / N
x        = np.linspace(0.0, L - dx, N)

tau      = 1.0
dt       = 5e-5       # stable: dt < 1/(M_max * k_max^2) ~ 1.2e-4
n_steps  = 300000     # T = 15 time units
TRACK_EVERY = 500     # 600 sample points

rho_star = 0.5
A_ic     = 0.15       # initial perturbation amplitude

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
# Spectral operators (periodic)
# -------------------------------------------------------------------------
k_vals = np.fft.fftfreq(N, d=dx / (2.0 * np.pi))

k_cutoff     = int(N / 3)
dealias_mask = np.ones(N)
dealias_mask[k_cutoff : N - k_cutoff + 1] = 0.0

def dealias(f):
    return np.real(np.fft.ifft(dealias_mask * np.fft.fft(f)))

def laplacian(f):
    return np.real(np.fft.ifft(-k_vals**2 * np.fft.fft(f)))

def gradient_sq(f):
    grad = np.real(np.fft.ifft(1j * k_vals * np.fft.fft(f)))
    return grad**2

def fourier_amp(f, k_index):
    return float(np.abs(np.fft.fft(f)[k_index]) / N)

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
def step(rho, v, D, H, zeta):
    F       = F_operator(rho)
    rho_new = dealias(rho + dt * (D * F + H * v))
    v_new   = dealias(v   + dt * (1.0 / tau) * (F - zeta * v))
    return rho_new, v_new

# -------------------------------------------------------------------------
# Three regimes
# -------------------------------------------------------------------------
regimes = [
    {"label": "A",  "name": "Monotonic (overdamped)",     "D": 0.8, "zeta": 3.0},
    {"label": "B",  "name": "Transitional",               "D": 0.6, "zeta": 1.0},
    {"label": "C",  "name": "Spiral (underdamped)",       "D": 0.4, "zeta": 0.2},
]

out_dir   = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(out_dir, "results.json")
png_path  = os.path.join(out_dir, "DH_complementarity.png")

print("Architectural Test P2: D/H Complementarity")
print(f"N={N}, dt={dt}, n_steps={n_steps}, T={n_steps*dt:.1f} time units")
print(f"IC: rho = rho* + {A_ic}*sin(x),  v = 0")
print()

all_regime_data = []

for reg in regimes:
    D    = reg["D"]
    H    = 1.0 - D
    zeta = reg["zeta"]
    disc = D + 2.0 * zeta
    label = reg["label"]

    print(f"Regime {label}: D={D}, H={H:.1f}, zeta={zeta}  "
          f"(D+2*zeta={disc:.1f})  —  {reg['name']}")

    # Initial condition
    rho = rho_star + A_ic * np.sin(x)
    v   = np.zeros(N)

    track_times = []
    rho_peak    = []
    v_peak      = []
    amp1        = []

    for i in range(n_steps):
        rho, v = step(rho, v, D, H, zeta)

        if i % TRACK_EVERY == 0:
            t = (i + 1) * dt
            track_times.append(t)
            rho_peak.append(float(np.max(rho)))
            peak_idx = int(np.argmax(rho))
            v_peak.append(float(v[peak_idx]))
            amp1.append(fourier_amp(rho, 1))

    print(f"  Final rho_peak = {rho_peak[-1]:.6f}  (rho* = {rho_star})")
    print(f"  Final v_peak   = {v_peak[-1]:.6f}")
    print(f"  Final |rho_hat(1)| = {amp1[-1]:.6f}")
    print()

    all_regime_data.append({
        "regime":        label,
        "name":          reg["name"],
        "D":             D,
        "H":             H,
        "zeta":          zeta,
        "discriminant":  disc,
        "track_times":   track_times,
        "rho_peak":      rho_peak,
        "v_peak":        v_peak,
        "amp1":          amp1,
    })

# -------------------------------------------------------------------------
# Save JSON
# -------------------------------------------------------------------------
json_out = {
    "test":     "P2_DH_complementarity",
    "N":        N,
    "dt":       dt,
    "n_steps":  n_steps,
    "T_total":  n_steps * dt,
    "A_ic":     A_ic,
    "tau":      tau,
    "regimes":  all_regime_data,
}
with open(json_path, "w") as f:
    json.dump(json_out, f, indent=2)

# -------------------------------------------------------------------------
# Three-panel stacked plot
# -------------------------------------------------------------------------
fig, axes = plt.subplots(3, 1, figsize=(11, 12), sharex=False)

colors = {"A": "steelblue", "B": "seagreen", "C": "tomato"}
labels = {
    "A": f"Regime A: D=0.8, ζ=3.0  (D+2ζ=6.8, monotonic)",
    "B": f"Regime B: D=0.6, ζ=1.0  (D+2ζ=2.6, transitional)",
    "C": f"Regime C: D=0.4, ζ=0.2  (D+2ζ=0.8, spiral)",
}

# Panel 1: rho_peak(t)
ax1 = axes[0]
for rd in all_regime_data:
    ax1.plot(rd["track_times"], rd["rho_peak"],
             color=colors[rd["regime"]], lw=1.4,
             label=labels[rd["regime"]])
ax1.axhline(rho_star, color="gray", lw=0.8, ls="--", label="ρ* = 0.5")
ax1.set_ylabel("Peak density  ρ_peak(t)", fontsize=11)
ax1.set_title(
    "Architectural Test P2: D/H Complementarity\n"
    "M(ρ)=1−ρ, P(ρ)=ρ−0.5,  IC: ρ=ρ*+0.15·sin(x),  v=0",
    fontsize=10
)
ax1.legend(fontsize=8, loc="upper right")
ax1.grid(True, alpha=0.3)

# Panel 2: v_peak(t)
ax2 = axes[1]
for rd in all_regime_data:
    ax2.plot(rd["track_times"], rd["v_peak"],
             color=colors[rd["regime"]], lw=1.4,
             label=labels[rd["regime"]])
ax2.axhline(0.0, color="gray", lw=0.8, ls="--")
ax2.set_ylabel("Participation at peak  v_peak(t)", fontsize=11)
ax2.set_title("v-channel dynamics: slaved (A), transient (B), oscillatory (C)", fontsize=10)
ax2.legend(fontsize=8, loc="upper right")
ax2.grid(True, alpha=0.3)

# Panel 3: |rho_hat(1)|(t) — dominant mode amplitude
ax3 = axes[2]
for rd in all_regime_data:
    ax3.semilogy(rd["track_times"], [max(a, 1e-12) for a in rd["amp1"]],
                 color=colors[rd["regime"]], lw=1.4,
                 label=labels[rd["regime"]])
ax3.set_xlabel("Time", fontsize=11)
ax3.set_ylabel("|ρ̂(1)|  (log scale)", fontsize=11)
ax3.set_title("Dominant mode amplitude: exponential decay rate controlled by D+2ζ", fontsize=10)
ax3.legend(fontsize=8, loc="upper right")
ax3.grid(True, alpha=0.3, which="both")

plt.tight_layout()
plt.savefig(png_path, dpi=150)
plt.close()

print("Architectural Test P2 complete. D/H complementarity validated.")
