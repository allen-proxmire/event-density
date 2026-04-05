#!/usr/bin/env python3
"""
ED-Phys-29: Attractor Map
===========================
Maps the global attractor structure of the unified ED cosmology PDE.
Determines the basin geometry around ρ*, stable/unstable manifolds,
and trajectory convergence under many initial conditions and three
cosmology channels.

Unified PDE (1D):
    dρ/dt = D·F[ρ] + H·v
    dv/dt = (1/τ)(F[ρ] – ζ v)
    D + H = 1

Canonical operator:
    F[ρ] = M(ρ) ∇²ρ + M′(ρ)|∇ρ|² – P_SY2(ρ)

Cosmologies:
    Oscillatory: D=0.0, H=1.0
    Hybrid:      D=0.5, H=0.5
    Parabolic:   D=1.0, H=0.0

IC set: Gaussian peaks (12), sinusoidal modes (3), composites (3),
        step functions (2), random noise (2) = 22 ICs × 3 cosmologies = 66 runs.
"""

import json
import numpy as np
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# ── Canonical ED parameters ──────────────────────────────────────────
ALPHA    = 0.1
GAMMA    = 0.5
M0       = 1.0
RHO_MAX  = 100.0
N_MOB    = 2
RHO_STAR = 50.0
RHO_0    = 0.5
TAU      = 100.0
ZETA     = 0.5
DX       = 1.0
ETA      = 0.2
EPS_NUM  = 1e-10

# ── Simulation parameters ────────────────────────────────────────────
NX       = 256
N_STEPS  = 80_000
SAMPLE   = 40

# ── Output ────────────────────────────────────────────────────────────
OUT = Path(__file__).parent / "results"
OUT.mkdir(exist_ok=True)

MAX_W_IN = 1000 / 150
MAX_H_IN = 800 / 150

# ── Cosmologies ───────────────────────────────────────────────────────
COSMOLOGIES = [
    ("oscillatory", 0.0, 1.0),
    ("hybrid",      0.5, 0.5),
    ("parabolic",   1.0, 0.0),
]


# ══════════════════════════════════════════════════════════════════════
# Core physics
# ══════════════════════════════════════════════════════════════════════

def mobility(rho):
    return M0 * np.maximum(1.0 - rho / RHO_MAX, 0.0) ** N_MOB

def mobility_prime(rho):
    return -M0 * (N_MOB / RHO_MAX) * np.maximum(1.0 - rho / RHO_MAX, 0.0) ** (N_MOB - 1)

def penalty_sy2(rho):
    delta = rho - RHO_STAR
    return ALPHA * GAMMA * delta / np.sqrt(delta * delta + RHO_0 * RHO_0)

def compute_F(rho, dx):
    M  = mobility(rho)
    Mp = mobility_prime(rho)
    lap     = (np.roll(rho, 1) + np.roll(rho, -1) - 2.0 * rho) / (dx * dx)
    grad_sq = ((np.roll(rho, 1) - np.roll(rho, -1)) / (2.0 * dx)) ** 2
    return M * lap + Mp * grad_sq - penalty_sy2(rho)


# ══════════════════════════════════════════════════════════════════════
# Initial condition library
# ══════════════════════════════════════════════════════════════════════

def ic_gaussian(nx, amplitude, sigma):
    x = np.arange(nx, dtype=np.float64)
    center = nx / 2.0
    rho = RHO_STAR + amplitude * np.exp(-((x - center) / sigma) ** 2)
    rho = np.clip(rho, EPS_NUM, RHO_MAX - EPS_NUM)
    return rho, f"gauss_A{amplitude}_L{sigma}"

def ic_sine(nx, amplitude, k):
    x = np.arange(nx, dtype=np.float64)
    kx = 2.0 * np.pi * k / nx
    rho = RHO_STAR + amplitude * np.sin(kx * x)
    rho = np.clip(rho, EPS_NUM, RHO_MAX - EPS_NUM)
    return rho, f"sine_A{amplitude}_k{k}"

def ic_composite(nx, A1, A2, k1=4, k2=7):
    x = np.arange(nx, dtype=np.float64)
    kx1 = 2.0 * np.pi * k1 / nx
    kx2 = 2.0 * np.pi * k2 / nx
    rho = RHO_STAR + A1 * np.sin(kx1 * x) + A2 * np.sin(kx2 * x)
    rho = np.clip(rho, EPS_NUM, RHO_MAX - EPS_NUM)
    return rho, f"comp_A{A1}k{k1}_A{A2}k{k2}"

def ic_step(nx, amplitude, width_frac=0.5):
    rho = np.full(nx, RHO_STAR, dtype=np.float64)
    cutoff = int(nx * width_frac)
    rho[:cutoff] += amplitude
    rho = np.clip(rho, EPS_NUM, RHO_MAX - EPS_NUM)
    return rho, f"step_A{amplitude}"

def ic_noise(nx, amplitude, seed=42):
    rng = np.random.default_rng(seed)
    rho = RHO_STAR + rng.uniform(-amplitude, amplitude, nx)
    rho = np.clip(rho, EPS_NUM, RHO_MAX - EPS_NUM)
    return rho, f"noise_A{amplitude}_s{seed}"


def build_ic_set(nx):
    """Build the full IC set. Returns list of (rho_array, label)."""
    ics = []
    # Gaussian peaks: A × L
    for A in [10, 20, 40, 80]:
        for L in [4, 8, 16]:
            rho, label = ic_gaussian(nx, A, L)
            ics.append((rho.copy(), label))
    # Sinusoidal modes
    for k in [2, 4, 8]:
        rho, label = ic_sine(nx, 10, k)
        ics.append((rho.copy(), label))
    # Composites
    for A1, A2 in [(10, 10), (20, 5), (5, 20)]:
        rho, label = ic_composite(nx, A1, A2)
        ics.append((rho.copy(), label))
    # Step functions
    for A in [20, 40]:
        rho, label = ic_step(nx, A)
        ics.append((rho.copy(), label))
    # Random noise
    for A, seed in [(5, 42), (10, 99)]:
        rho, label = ic_noise(nx, A, seed)
        ics.append((rho.copy(), label))
    return ics


# ══════════════════════════════════════════════════════════════════════
# PDE integration
# ══════════════════════════════════════════════════════════════════════

def mode_amplitude_1d(rho, k):
    delta = rho - RHO_STAR
    N = len(delta)
    fft = np.fft.rfft(delta) / N
    amps = 2.0 * np.abs(fft)
    return float(amps[k]) if k < len(amps) else 0.0


def run_case(rho_init, ic_label, cosmo_name, D, nx=NX, n_steps=N_STEPS,
             sample_every=SAMPLE):
    H = 1.0 - D
    rho = rho_init.copy()
    v = np.zeros(nx, dtype=np.float64)
    peak_idx = nx // 2
    dt = ETA * DX * DX / (M0 + EPS_NUM)

    peak_hist  = []
    vpeak_hist = []
    std_hist   = []
    time_hist  = []
    k3_hist    = []
    horizon_hist = []
    dist_hist  = []
    clips_total = 0

    t = 0.0
    for step in range(n_steps):
        F = compute_F(rho, DX)
        rho_new = rho + dt * (D * F + H * v)
        v_new   = v   + dt * (1.0 / TAU) * (F - ZETA * v)

        clips = int(np.sum(rho_new < EPS_NUM))
        clips_total += clips
        rho_new = np.clip(rho_new, EPS_NUM, RHO_MAX - EPS_NUM)

        rho = rho_new
        v   = v_new
        t  += dt

        if step % sample_every == 0:
            peak_hist.append(float(rho[peak_idx]))
            vpeak_hist.append(float(v[peak_idx]))
            std_hist.append(float(np.std(rho)))
            time_hist.append(t)
            k3_hist.append(mode_amplitude_1d(rho, 3))
            horizon_hist.append(int(np.sum(rho >= 0.9 * RHO_MAX)))
            # Phase-space distance to equilibrium: sqrt(σ² + <v²>)
            d = np.sqrt(np.std(rho)**2 + np.mean(v**2))
            dist_hist.append(float(d))

    return {
        "ic_label": ic_label,
        "cosmo": cosmo_name,
        "D": D, "H": H, "dt": dt,
        "peak_hist": peak_hist,
        "vpeak_hist": vpeak_hist,
        "std_hist": std_hist,
        "time_hist": time_hist,
        "k3_hist": k3_hist,
        "horizon_hist": horizon_hist,
        "dist_hist": dist_hist,
        "total_clips": clips_total,
        "final_rho_std": float(np.std(rho)),
        "final_rho_mean": float(np.mean(rho)),
        "ic_std0": float(np.std(rho_init)),
        "ic_peak0": float(rho_init[peak_idx]),
    }


# ══════════════════════════════════════════════════════════════════════
# Analysis
# ══════════════════════════════════════════════════════════════════════

def detect_oscillations(peak_hist):
    delta = np.array(peak_hist) - RHO_STAR
    crossings = []
    for i in range(1, len(delta)):
        if delta[i - 1] * delta[i] < 0:
            crossings.append(i)
    n_cycles = len(crossings) // 2
    amplitudes = []
    for i in range(len(crossings) - 1):
        seg = delta[crossings[i]:crossings[i + 1]]
        if len(seg) > 0:
            amplitudes.append(float(np.max(np.abs(seg))))
    return n_cycles, amplitudes


def measure_undershoot_overshoot(peak_hist):
    delta = np.array(peak_hist) - RHO_STAR
    undershoot = float(-np.min(delta)) if np.min(delta) < 0 else 0.0
    below_idx = np.where(delta < 0)[0]
    if len(below_idx) > 0:
        after = delta[below_idx[0]:]
        overshoot = float(np.max(after)) if np.max(after) > 0 else 0.0
    else:
        overshoot = 0.0
    return undershoot, overshoot


def relaxation_time(std_hist, time_hist, threshold_frac=0.01):
    s = np.array(std_hist)
    if s[0] < 1e-20:
        return 0.0
    thresh = s[0] * threshold_frac
    below = np.where(s < thresh)[0]
    return float(time_hist[below[0]]) if len(below) > 0 else float(time_hist[-1])


def convergence_exponent(dist_hist, time_hist):
    """Fit log(dist) ~ -λ·t to get Lyapunov-like decay rate."""
    d = np.array(dist_hist)
    t = np.array(time_hist)
    mask = d > 1e-12
    if np.sum(mask) < 10:
        return 0.0
    log_d = np.log(d[mask])
    t_m = t[mask]
    # Use first half to avoid numerical floor
    n = max(len(log_d) // 2, 10)
    log_d = log_d[:n]
    t_m = t_m[:n]
    if len(t_m) < 2:
        return 0.0
    coeffs = np.polyfit(t_m, log_d, 1)
    return float(-coeffs[0])  # positive = decaying


def manifold_dimension_estimate(peak_hist, vpeak_hist, std_hist):
    """Rough estimate: if v stays ~0 throughout, trajectory is ~1D in ρ-space.
    If v activates, it's 2D. Check via max |v| relative to std excursion."""
    max_v = float(np.max(np.abs(vpeak_hist)))
    max_std = float(np.max(std_hist))
    if max_std < 1e-10:
        return 0  # trivial
    ratio = max_v / (max_std + 1e-20)
    if ratio < 0.001:
        return 1  # essentially 1D (pure diffusion)
    elif ratio < 0.1:
        return 1  # weakly 2D, effectively 1D approach
    else:
        return 2  # genuine 2D spiral/oscillatory approach


def analyze_result(result):
    n_cycles, amplitudes = detect_oscillations(result["peak_hist"])
    undershoot, overshoot = measure_undershoot_overshoot(result["peak_hist"])
    relax = relaxation_time(result["std_hist"], result["time_hist"])
    k3_max = float(np.max(result["k3_hist"])) if result["k3_hist"] else 0.0
    horizon_max = int(np.max(result["horizon_hist"])) if result["horizon_hist"] else 0
    conv_exp = convergence_exponent(result["dist_hist"], result["time_hist"])
    manifold_dim = manifold_dimension_estimate(
        result["peak_hist"], result["vpeak_hist"], result["std_hist"])
    drift = float(result["final_rho_mean"] - RHO_STAR)

    return {
        "ic_label": result["ic_label"],
        "cosmo": result["cosmo"],
        "D": result["D"],
        "n_cycles": n_cycles,
        "undershoot": undershoot,
        "overshoot": overshoot,
        "relax_time": relax,
        "k3_max": k3_max,
        "horizon_max": horizon_max,
        "horizon_activated": horizon_max > 0,
        "convergence_exponent": conv_exp,
        "manifold_dim": manifold_dim,
        "eq_drift": drift,
        "total_clips": result["total_clips"],
        "final_std": result["final_rho_std"],
        "ic_std0": result["ic_std0"],
    }


# ══════════════════════════════════════════════════════════════════════
# Plotting
# ══════════════════════════════════════════════════════════════════════

COSMO_COLORS = {
    "oscillatory": "royalblue",
    "hybrid":      "seagreen",
    "parabolic":   "firebrick",
}


def plot_attractor_map(all_analysis, path):
    """2D scatter: IC initial perturbation amplitude vs relaxation time,
    colored by cosmology, with horizon-activated points highlighted."""
    fig, ax = plt.subplots(figsize=(MAX_W_IN, MAX_H_IN))

    for a in all_analysis:
        color = COSMO_COLORS[a["cosmo"]]
        marker = "D" if a["horizon_activated"] else "o"
        edge = "gold" if a["horizon_activated"] else "none"
        ms = 8 if a["horizon_activated"] else 5
        ax.scatter(a["ic_std0"], a["relax_time"],
                   c=color, marker=marker, s=ms**2,
                   edgecolors=edge, linewidths=1.5, alpha=0.7, zorder=3)

    # Legend
    handles = [
        Line2D([0], [0], marker="o", color="w", markerfacecolor="royalblue",
               ms=8, label="Oscillatory (D=0)"),
        Line2D([0], [0], marker="o", color="w", markerfacecolor="seagreen",
               ms=8, label="Hybrid (D=0.5)"),
        Line2D([0], [0], marker="o", color="w", markerfacecolor="firebrick",
               ms=8, label="Parabolic (D=1)"),
        Line2D([0], [0], marker="D", color="w", markerfacecolor="gray",
               markeredgecolor="gold", ms=8, markeredgewidth=1.5,
               label="Horizon activated"),
    ]
    ax.legend(handles=handles, fontsize=8, loc="upper right")
    ax.set_xlabel(r"Initial perturbation $\sigma_0$", fontsize=10)
    ax.set_ylabel("Relaxation time", fontsize=10)
    ax.set_title("Attractor Map: IC perturbation vs relaxation", fontsize=11)
    ax.grid(True, alpha=0.2)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_convergence_paths(all_results, path):
    """Overlay of ρ_peak(t) for all ICs, one subplot per cosmology."""
    fig, axes = plt.subplots(1, 3, figsize=(MAX_W_IN, MAX_H_IN), sharey=True)

    for idx, (cosmo_name, _, _) in enumerate(COSMOLOGIES):
        ax = axes[idx]
        runs = [r for r in all_results if r["cosmo"] == cosmo_name]
        for r in runs:
            ax.plot(r["time_hist"], r["peak_hist"], lw=0.4, alpha=0.6)
        ax.axhline(RHO_STAR, color="blue", ls="--", alpha=0.4, lw=1)
        ax.set_xlabel("Time", fontsize=8)
        if idx == 0:
            ax.set_ylabel(r"$\rho_{\rm peak}$", fontsize=9)
        ax.set_title(f"{cosmo_name} (D={COSMOLOGIES[idx][1]})", fontsize=9)
        ax.tick_params(labelsize=7)

    fig.suptitle("Convergence Paths: all ICs", fontsize=11, y=1.01)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_manifold_geometry(all_results, path):
    """Phase portrait (ρ_peak, v_peak) approach to equilibrium, per cosmology."""
    fig, axes = plt.subplots(1, 3, figsize=(MAX_W_IN, MAX_H_IN))

    for idx, (cosmo_name, _, _) in enumerate(COSMOLOGIES):
        ax = axes[idx]
        runs = [r for r in all_results if r["cosmo"] == cosmo_name]
        for r in runs:
            rp = np.array(r["peak_hist"])
            vp = np.array(r["vpeak_hist"])
            ax.plot(rp, vp, lw=0.35, alpha=0.5)
        ax.axvline(RHO_STAR, color="blue", ls="--", alpha=0.3, lw=0.8)
        ax.axhline(0.0, color="gray", ls=":", alpha=0.3)
        ax.plot(RHO_STAR, 0.0, "k+", ms=10, mew=2, zorder=5)
        ax.set_xlabel(r"$\rho_{\rm peak}$", fontsize=8)
        if idx == 0:
            ax.set_ylabel(r"$v_{\rm peak}$", fontsize=9)
        ax.set_title(f"{cosmo_name}", fontsize=9)
        ax.tick_params(labelsize=7)

    fig.suptitle(r"Manifold geometry: $(\rho, v)$ phase portraits", fontsize=11, y=1.01)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


# ══════════════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════════════

def main():
    print("=" * 70)
    print("ED-Phys-29: Attractor Map")
    print("=" * 70)

    ic_set = build_ic_set(NX)
    n_ics = len(ic_set)
    n_cosmo = len(COSMOLOGIES)
    total = n_ics * n_cosmo
    print(f"ICs: {n_ics}    Cosmologies: {n_cosmo}    Total runs: {total}")
    print(f"Grid: {NX} sites, {N_STEPS} steps, sample every {SAMPLE}")
    print("=" * 70)

    all_results  = []
    all_analysis = []
    run_idx = 0

    for cosmo_name, D, H in COSMOLOGIES:
        print(f"\n{'-'*60}")
        print(f"Cosmology: {cosmo_name} (D={D}, H={H})")
        print(f"{'-'*60}")

        for rho_init, ic_label in ic_set:
            run_idx += 1
            result = run_case(rho_init, ic_label, cosmo_name, D)
            analysis = analyze_result(result)
            all_results.append(result)
            all_analysis.append(analysis)

            flag = ""
            if analysis["horizon_activated"]:
                flag += " [HORIZON]"
            if analysis["n_cycles"] > 0:
                flag += f" [{analysis['n_cycles']}c]"

            print(f"  [{run_idx:3d}/{total}] {ic_label:<28s} "
                  f"relax={analysis['relax_time']:>8.1f}  "
                  f"lam={analysis['convergence_exponent']:>.4f}  "
                  f"dim={analysis['manifold_dim']}  "
                  f"cyc={analysis['n_cycles']}{flag}")

    # ── Global plots ──────────────────────────────────────────────────
    print("\n>>> Generating attractor map...")
    plot_attractor_map(all_analysis, OUT / "attractor_map.png")

    print(">>> Generating convergence paths...")
    plot_convergence_paths(all_results, OUT / "convergence_paths.png")

    print(">>> Generating manifold geometry...")
    plot_manifold_geometry(all_results, OUT / "manifold_geometry.png")

    # ── Basin summary ─────────────────────────────────────────────────
    # Check for secondary attractors: anything that doesn't converge to ρ*
    secondary_attractors = []
    for a in all_analysis:
        if a["final_std"] > 0.1:
            secondary_attractors.append({
                "ic": a["ic_label"], "cosmo": a["cosmo"],
                "final_std": a["final_std"], "eq_drift": a["eq_drift"],
            })

    # Manifold statistics per cosmology
    manifold_stats = {}
    for cosmo_name, _, _ in COSMOLOGIES:
        subset = [a for a in all_analysis if a["cosmo"] == cosmo_name]
        dims = [a["manifold_dim"] for a in subset]
        conv_rates = [a["convergence_exponent"] for a in subset if a["convergence_exponent"] > 0]
        horizon_count = sum(1 for a in subset if a["horizon_activated"])
        osc_count = sum(1 for a in subset if a["n_cycles"] > 0)
        manifold_stats[cosmo_name] = {
            "n_runs": len(subset),
            "dim_counts": {str(d): dims.count(d) for d in sorted(set(dims))},
            "mean_convergence_rate": float(np.mean(conv_rates)) if conv_rates else 0.0,
            "std_convergence_rate": float(np.std(conv_rates)) if conv_rates else 0.0,
            "min_convergence_rate": float(np.min(conv_rates)) if conv_rates else 0.0,
            "max_convergence_rate": float(np.max(conv_rates)) if conv_rates else 0.0,
            "horizon_activated_count": horizon_count,
            "oscillatory_count": osc_count,
        }

    # ── Summary JSON ──────────────────────────────────────────────────
    export = {
        "experiment": "ED-Phys-29_AttractorMap",
        "parameters": {
            "NX": NX, "N_STEPS": N_STEPS, "SAMPLE": SAMPLE,
            "TAU": TAU, "ZETA": ZETA, "RHO_STAR": RHO_STAR, "RHO_MAX": RHO_MAX,
        },
        "total_runs": total,
        "n_ics": n_ics,
        "cosmologies": [c[0] for c in COSMOLOGIES],
        "basin_structure": {
            "single_global_attractor": len(secondary_attractors) == 0,
            "secondary_attractors": secondary_attractors,
        },
        "manifold_stats": manifold_stats,
        "all_analysis": all_analysis,
    }

    json_path = OUT / "attractor_summary.json"
    with open(json_path, "w") as f:
        json.dump(export, f, indent=2)
    print(f"\n>>> Summary written to {json_path}")

    # ── Print summary ─────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("GLOBAL ATTRACTOR ANALYSIS")
    print("=" * 70)

    if len(secondary_attractors) == 0:
        print("RESULT: Single global attractor at rho* = 50.0")
        print("        All 66 trajectories converge to equilibrium.")
    else:
        print(f"WARNING: {len(secondary_attractors)} trajectories did NOT converge:")
        for sa in secondary_attractors:
            print(f"  {sa['ic']} / {sa['cosmo']}: "
                  f"final_std={sa['final_std']:.4f}, drift={sa['eq_drift']:.2e}")

    print("\nManifold statistics per cosmology:")
    for cosmo, stats in manifold_stats.items():
        print(f"\n  {cosmo}:")
        print(f"    Dimension counts: {stats['dim_counts']}")
        print(f"    Convergence rate: {stats['mean_convergence_rate']:.5f} "
              f"± {stats['std_convergence_rate']:.5f}")
        print(f"    Range: [{stats['min_convergence_rate']:.5f}, "
              f"{stats['max_convergence_rate']:.5f}]")
        print(f"    Horizon activations: {stats['horizon_activated_count']}/{stats['n_runs']}")
        print(f"    Oscillatory trajectories: {stats['oscillatory_count']}/{stats['n_runs']}")

    print("\n" + "=" * 70)
    print(">>> Done. All outputs in:", OUT)


if __name__ == "__main__":
    main()
