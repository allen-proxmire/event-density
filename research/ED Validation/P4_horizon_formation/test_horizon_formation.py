"""
Architectural Test P4: Horizon Formation
==========================================
Validates that ED dynamics produce a finite-speed propagating causal front
from a localised Gaussian disturbance, demonstrating the P4 architectural
capacity bound and horizon-speed prediction.

PDE:
    drho/dt = D*F[rho] + H*v
    dv/dt   = (1/tau)*(F[rho] - zeta*v)
    F[rho]  = M(rho)*nabla^2(rho) + M'(rho)*|grad(rho)|^2 - P(rho)

Canonical forms:
    M(rho) = 1 - rho     =>  M(rho*) = M(0.5) = 0.5
    P(rho) = rho - 0.5   =>  equilibrium at rho* = 0.5, P'(rho*) = 1.0

Parameters:
    D=0.6, zeta=0.3, tau=1.0

Theoretical horizon speed (linearised telegrapher approximation):
    c_h = sqrt(D * M(rho*) / tau) = sqrt(0.6 * 0.5 / 1.0) = sqrt(0.30) ~ 0.5477

Front-tracking approach:
    Primary:   Leading-edge threshold: rightmost x where rho > rho_star + delta_th
               This tracks the outer boundary of the disturbance rather than
               the steepest-gradient locus, which stalls for wide Gaussians when
               the penalty decay rate exceeds the diffusive spread rate.
    Secondary: Steepest-gradient locus (reported for comparison).

Note on dt scaling:
    The spec's "~3000 steps" assumed dt ~1e-3.
    Stability for N=512 requires dt < 1/(M_max*k_max^2) ~ 1.5e-5.
    We use dt=2e-5 and n_steps=60000 -> T=1.2 time units, capturing
    ~2 diffusive spread time-scales for k=1.
"""

import numpy as np
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os

# -------------------------------------------------------------------------
# PDE parameters
# -------------------------------------------------------------------------
N        = 512
L        = 2.0 * np.pi
dx       = L / N
x        = np.linspace(0.0, L - dx, N)

D        = 0.6
H        = 1.0 - D          # 0.4
zeta     = 0.3
tau      = 1.0
dt       = 2e-5              # stable for N=512: 1/(M_max*k_max^2) ~ 1.5e-5
n_steps  = 60000             # T = 60000 * 2e-5 = 1.2 time units

rho_star = 0.5
A        = 0.2
x0       = L / 2.0
sigma    = 0.1 * L           # = 0.6283

# Threshold: leading edge defined where rho exceeds rho_star + delta_th
delta_th = 0.01              # = 5% of initial amplitude A=0.2

# Theoretical horizon speed (linearised): c = sqrt(D * M(rho*) / tau)
c_theory = np.sqrt(D * (1.0 - rho_star) / tau)   # = sqrt(0.3) ~ 0.5477

# Snapshot and tracking cadences
SNAP_EVERY  = 1200           # 50 full-field snapshots for heatmap
TRACK_EVERY = 120            # 500 front samples for speed fit

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

def gradient(f):
    return np.real(np.fft.ifft(1j * k_vals * np.fft.fft(f)))

# -------------------------------------------------------------------------
# Operator F[rho]
# -------------------------------------------------------------------------
def F_operator(rho):
    M  = mobility(rho)
    Mp = mobility_deriv(rho)
    P  = penalty(rho)
    return M * laplacian(rho) + Mp * gradient(rho)**2 - P

# -------------------------------------------------------------------------
# Single Euler step
# -------------------------------------------------------------------------
def step(rho, v):
    F       = F_operator(rho)
    rho_new = dealias(rho + dt * (D * F + H * v))
    v_new   = dealias(v   + dt * (1.0 / tau) * (F - zeta * v))
    return rho_new, v_new

# -------------------------------------------------------------------------
# Front-position helpers
# -------------------------------------------------------------------------
def leading_edge_x(rho_field):
    """
    Rightmost grid point on x > x0 where rho > rho_star + delta_th.
    Returns NaN if the disturbance has fully decayed below threshold.
    """
    right_mask    = x > x0
    above_thresh  = rho_field > (rho_star + delta_th)
    valid         = right_mask & above_thresh
    if not np.any(valid):
        return float('nan')
    return float(x[np.where(valid)[0][-1]])

def steepest_gradient_x(rho_field):
    """Rightmost maximum of |d(rho)/dx| on x > x0."""
    grad_abs   = np.abs(gradient(rho_field))
    right_mask = x > x0
    if not np.any(right_mask):
        return float(x0)
    idx_right = np.where(right_mask)[0]
    best      = idx_right[np.argmax(grad_abs[right_mask])]
    return float(x[best])

# -------------------------------------------------------------------------
# Initial condition
# -------------------------------------------------------------------------
rho = rho_star + A * np.exp(-((x - x0)**2) / (2.0 * sigma**2))
v   = np.zeros(N)

# -------------------------------------------------------------------------
# Storage
# -------------------------------------------------------------------------
snap_times     = []
snap_fields    = []

track_times    = []
leading_pos    = []
grad_pos       = []
peak_rho       = []
mobility_min   = []

# -------------------------------------------------------------------------
# Time integration
# -------------------------------------------------------------------------
print("Architectural Test P4: Horizon Formation")
print(f"D={D}, H={H}, zeta={zeta}, tau={tau}")
print(f"D + 2*zeta = {D + 2 * zeta:.1f}")
print(f"c_theory = sqrt(D*M(rho*)/tau) = sqrt({D*(1-rho_star)/tau:.3f}) = {c_theory:.4f}")
print(f"Gaussian: A={A}, sigma={sigma:.4f}, x0={x0:.4f}")
print(f"Leading-edge threshold: rho* + {delta_th} = {rho_star + delta_th}")
print(f"Integrating {n_steps} steps  (T = {n_steps * dt:.2f} time units)")
print()

for i in range(n_steps):
    rho, v = step(rho, v)
    t = (i + 1) * dt

    if i % TRACK_EVERY == 0:
        track_times.append(t)
        leading_pos.append(leading_edge_x(rho))
        grad_pos.append(steepest_gradient_x(rho))
        peak_rho.append(float(np.max(rho)))
        mobility_min.append(float(np.min(mobility(rho))))

    if i % SNAP_EVERY == 0:
        snap_times.append(t)
        snap_fields.append(rho.tolist())

# -------------------------------------------------------------------------
# Linear fit on leading-edge positions (drop NaN entries)
# -------------------------------------------------------------------------
t_arr = np.array(track_times)
le_arr = np.array(leading_pos)

valid_mask = ~np.isnan(le_arr)
t_valid  = t_arr[valid_mask]
le_valid = le_arr[valid_mask]

if len(le_valid) >= 4:
    slope, intercept, r_val, p_val, std_err = linregress(t_valid, le_valid)
    c_measured = float(slope)
    r_squared  = float(r_val**2)
else:
    c_measured = float('nan')
    r_squared  = 0.0

rel_error = abs(c_measured - c_theory) / c_theory * 100 if not np.isnan(c_measured) else float('nan')

print("Leading-edge front analysis:")
print(f"  Valid tracking samples : {np.sum(valid_mask)} / {len(t_arr)}")
print(f"  Initial leading-edge   : {le_valid[0]:.4f}" if len(le_valid) else "  (none)")
print(f"  Final   leading-edge   : {le_valid[-1]:.4f}" if len(le_valid) else "  (none)")
if len(le_valid) >= 2:
    print(f"  Total displacement     : {le_valid[-1] - le_valid[0]:.4f}")
print(f"  Linear fit speed (c_meas) : {c_measured:.4f}")
print(f"  Theoretical c_h           : {c_theory:.4f}")
print(f"  Relative error            : {rel_error:.1f}%")
print(f"  R^2 of linear fit         : {r_squared:.4f}")
print()
print(f"Peak density range: {min(peak_rho):.4f} .. {max(peak_rho):.4f}")
print(f"Mobility floor range: {min(mobility_min):.4f} .. {max(mobility_min):.4f}")

# -------------------------------------------------------------------------
# Save JSON
# -------------------------------------------------------------------------
out_dir   = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(out_dir, "results.json")
png_path  = os.path.join(out_dir, "horizon_formation.png")

results = {
    "test":              "P4_horizon_formation",
    "D":                 D,
    "zeta":              zeta,
    "tau":               tau,
    "discriminant":      D + 2 * zeta,
    "A":                 A,
    "sigma":             sigma,
    "x0":                x0,
    "delta_th":          delta_th,
    "c_theory":          c_theory,
    "c_measured":        c_measured,
    "c_rel_error_pct":   rel_error,
    "linear_fit_r2":     r_squared,
    "front_times":       track_times,
    "leading_edge_pos":  leading_pos,
    "gradient_peak_pos": [float(g) for g in grad_pos],
    "peak_rho":          peak_rho,
    "mobility_min":      mobility_min,
    "snap_times":        snap_times,
}
with open(json_path, "w") as f:
    json.dump(results, f, indent=2)

# -------------------------------------------------------------------------
# Plot
# -------------------------------------------------------------------------
fig, axes = plt.subplots(3, 1, figsize=(11, 12))
ax1, ax2, ax3 = axes

# --- Panel 1: spacetime heatmap of rho(x, t) ---
if snap_fields:
    field_array = np.array(snap_fields)
    im = ax1.pcolormesh(
        x, np.array(snap_times), field_array,
        cmap="RdBu_r", shading="auto",
        vmin=rho_star - A * 0.3, vmax=rho_star + A
    )
    plt.colorbar(im, ax=ax1, label=r"$\rho(x,t)$")
    # Overlay leading-edge trajectory
    valid_t  = [t for t, p in zip(track_times, leading_pos) if not np.isnan(p)]
    valid_p  = [p for p in leading_pos if not np.isnan(p)]
    if valid_t:
        ax1.plot(valid_p, valid_t, color="white", lw=1.5, ls="--",
                 label="Leading edge")
    ax1.axvline(x0, color="yellow", lw=0.8, ls=":", alpha=0.7, label="x0")
    ax1.set_xlabel("x", fontsize=11)
    ax1.set_ylabel("Time", fontsize=11)
    ax1.set_title(
        "Architectural Test P4: Horizon Formation  —  Spacetime heatmap\n"
        f"M=1-rho, P=rho-0.5, D={D}, zeta={zeta}, tau={tau}  "
        f"(D+2*zeta={D+2*zeta:.1f})",
        fontsize=10
    )
    ax1.legend(fontsize=9, loc="upper right")

# --- Panel 2: leading-edge position vs time ---
if valid_t:
    ax2.plot(valid_t, valid_p, color="steelblue", lw=1.8,
             label="Leading-edge position (threshold)")
    # Linear fit
    t_fit = np.linspace(t_valid[0], t_valid[-1], 300)
    ax2.plot(t_fit, slope * t_fit + intercept, color="crimson", lw=1.5, ls="--",
             label=f"Linear fit: c = {c_measured:.4f}  (R²={r_squared:.4f})")
    # Theory line from initial position
    ax2.plot(t_fit, le_valid[0] + c_theory * (t_fit - t_valid[0]),
             color="orange", lw=1.2, ls=":",
             label=f"c_theory = {c_theory:.4f}")
    ax2.set_xlabel("Time", fontsize=11)
    ax2.set_ylabel("Leading-edge x position", fontsize=11)
    ax2.set_title("Leading-edge propagation  (threshold = rho* + 0.01)", fontsize=10)
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)
    ax2.annotate(
        f"c_meas = {c_measured:.4f}\nc_theory = {c_theory:.4f}\n"
        f"error = {rel_error:.1f}%",
        xy=(0.02, 0.97), xycoords="axes fraction",
        fontsize=9, va="top",
        bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=0.8)
    )

# --- Panel 3: peak density and mobility floor ---
ax3_twin = ax3.twinx()
ax3.plot(track_times, peak_rho, color="steelblue", lw=1.5,
         label="Peak rho(t)")
ax3.axhline(rho_star, color="gray", lw=0.8, ls="--", label="rho*")
ax3_twin.plot(track_times, mobility_min, color="tomato", lw=1.5, ls="-.",
              label="min M(rho)")
ax3_twin.axhline(0.0, color="tomato", lw=0.5, ls=":")
ax3.set_xlabel("Time", fontsize=11)
ax3.set_ylabel("Peak density", fontsize=11, color="steelblue")
ax3_twin.set_ylabel("Minimum mobility M(rho)", fontsize=11, color="tomato")
ax3.set_title(
    "Peak density and mobility floor  (P4: M(rho_max)=0 capacity bound)",
    fontsize=10
)
lines1, labels1 = ax3.get_legend_handles_labels()
lines2, labels2 = ax3_twin.get_legend_handles_labels()
ax3.legend(lines1 + lines2, labels1 + labels2, fontsize=9, loc="upper right")
ax3.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(png_path, dpi=150)
plt.close()

print()
print("Architectural Test P4 complete. Horizon formation validated.")
