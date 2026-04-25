#!/usr/bin/env python3
"""
ED-Phys-26: Mobility Robustness
================================
Tests robustness of the unified ED cosmology PDE under small perturbations
to the mobility M(ρ).

Unified PDE (1D):
    ∂ρ/∂t = D·F[ρ] + H·v
    ∂v/∂t = (1/τ)(F[ρ] – ζ v)
    D + H = 1

Canonical operator:
    F[ρ] = M(ρ) ∇²ρ + M′(ρ)|∇ρ|² – P_SY2(ρ)

Mobility variants (ε = 0.05):
    1. Canonical:   M0 · (1 – ρ/ρ_max)²
    2. Steeper:     M · (1 + ε)
    3. Flatter:     M · (1 – ε)
    4. Asymmetric:  M · (1 + ε·sign(ρ – ρ*))
    5. Non-smooth:  M + ε·tanh(ρ – ρ*)
"""

import json
import numpy as np
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

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
D_FIXED  = 0.50
H_FIXED  = 0.50
AMP_IC   = 40.0
SIGMA_IC = 20.0
EPSILON  = 0.05

# ── Output ────────────────────────────────────────────────────────────
OUT = Path(__file__).parent / "results"
OUT.mkdir(exist_ok=True)

# Max PNG dimensions
MAX_W_IN = 1000 / 150   # ~6.67 inches at 150 dpi
MAX_H_IN = 800 / 150    # ~5.33 inches at 150 dpi


# ══════════════════════════════════════════════════════════════════════
# Core functions
# ══════════════════════════════════════════════════════════════════════

def canonical_mobility(rho):
    return M0 * np.maximum(1.0 - rho / RHO_MAX, 0.0) ** N_MOB

def canonical_mobility_prime(rho):
    return -M0 * (N_MOB / RHO_MAX) * np.maximum(1.0 - rho / RHO_MAX, 0.0) ** (N_MOB - 1)

def penalty_sy2(rho):
    delta = rho - RHO_STAR
    return ALPHA * GAMMA * delta / np.sqrt(delta * delta + RHO_0 * RHO_0)


# ── Mobility variant factories ───────────────────────────────────────

def make_mobility_steeper():
    """M = M0 · (1 + ε)"""
    scale = 1.0 + EPSILON
    def mob(rho):
        return scale * canonical_mobility(rho)
    def mob_p(rho):
        return scale * canonical_mobility_prime(rho)
    return mob, mob_p

def make_mobility_flatter():
    """M = M0 · (1 – ε)"""
    scale = 1.0 - EPSILON
    def mob(rho):
        return scale * canonical_mobility(rho)
    def mob_p(rho):
        return scale * canonical_mobility_prime(rho)
    return mob, mob_p

def make_mobility_asymmetric():
    """M = M0 · (1 + ε·sign(ρ – ρ*))"""
    def mob(rho):
        sign = np.sign(rho - RHO_STAR)
        return (1.0 + EPSILON * sign) * canonical_mobility(rho)
    def mob_p(rho):
        sign = np.sign(rho - RHO_STAR)
        return (1.0 + EPSILON * sign) * canonical_mobility_prime(rho)
    return mob, mob_p

def make_mobility_nonsmooth():
    """M = M0_canonical + ε·tanh(ρ – ρ*)"""
    def mob(rho):
        return canonical_mobility(rho) + EPSILON * np.tanh(rho - RHO_STAR)
    def mob_p(rho):
        return canonical_mobility_prime(rho) + EPSILON / np.cosh(rho - RHO_STAR)**2
    return mob, mob_p


MOBILITY_VARIANTS = [
    ("canonical",  canonical_mobility, canonical_mobility_prime),
    ("steeper",    *make_mobility_steeper()),
    ("flatter",    *make_mobility_flatter()),
    ("asymmetric", *make_mobility_asymmetric()),
    ("nonsmooth",  *make_mobility_nonsmooth()),
]


# ══════════════════════════════════════════════════════════════════════
# PDE integration
# ══════════════════════════════════════════════════════════════════════

def compute_rhs(rho, dx, mob_fn, mob_prime_fn):
    M  = mob_fn(rho)
    Mp = mob_prime_fn(rho)
    lap     = (np.roll(rho, 1) + np.roll(rho, -1) - 2.0 * rho) / (dx * dx)
    grad_sq = ((np.roll(rho, 1) - np.roll(rho, -1)) / (2.0 * dx)) ** 2
    return M * lap + Mp * grad_sq - penalty_sy2(rho)


def make_ic(nx):
    x = np.arange(nx, dtype=np.float64)
    center = nx / 2.0
    rho = RHO_STAR + AMP_IC * np.exp(-((x - center) / SIGMA_IC) ** 2)
    rho = np.clip(rho, EPS_NUM, RHO_MAX - EPS_NUM)
    v = np.zeros(nx, dtype=np.float64)
    return rho, v


def run_case(name, mob_fn, mob_prime_fn, D=D_FIXED, nx=NX, n_steps=N_STEPS,
             sample_every=SAMPLE, track_k3=True):
    H = 1.0 - D
    rho, v = make_ic(nx)
    peak_idx = nx // 2
    dt = ETA * DX * DX / (M0 + EPS_NUM)

    peak_hist = []
    mean_hist = []
    std_hist  = []
    time_hist = []
    k3_hist   = []
    clips_total = 0

    t = 0.0
    for step in range(n_steps):
        F = compute_rhs(rho, DX, mob_fn, mob_prime_fn)
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
            mean_hist.append(float(np.mean(rho)))
            std_hist.append(float(np.std(rho)))
            time_hist.append(t)
            if track_k3:
                k3_hist.append(mode_amplitude_1d(rho, 3))

    return {
        "name": name,
        "D": D, "H": H, "dt": dt, "n_steps": n_steps,
        "peak_hist": peak_hist,
        "mean_hist": mean_hist,
        "std_hist": std_hist,
        "time_hist": time_hist,
        "k3_hist": k3_hist,
        "total_clips": clips_total,
        "final_rho_peak": float(rho[peak_idx]),
        "final_rho_std": float(np.std(rho)),
    }


# ══════════════════════════════════════════════════════════════════════
# Analysis functions
# ══════════════════════════════════════════════════════════════════════

def mode_amplitude_1d(rho, k):
    delta = rho - RHO_STAR
    N = len(delta)
    fft = np.fft.rfft(delta) / N
    amps = 2.0 * np.abs(fft)
    if k < len(amps):
        return float(amps[k])
    return 0.0


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
    return n_cycles, amplitudes, crossings


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
    if len(below) > 0:
        return float(time_hist[below[0]])
    return float(time_hist[-1])


def early_diffusion_rate(peak_hist, time_hist, n_early=10):
    """Slope of peak decay in earliest samples (linear fit)."""
    if len(peak_hist) < n_early:
        n_early = len(peak_hist)
    t = np.array(time_hist[:n_early])
    p = np.array(peak_hist[:n_early])
    if len(t) < 2:
        return 0.0
    coeffs = np.polyfit(t, p, 1)
    return float(coeffs[0])  # slope (negative = decay)


def analyze_result(result):
    n_cycles, amplitudes, crossings = detect_oscillations(result["peak_hist"])
    undershoot, overshoot = measure_undershoot_overshoot(result["peak_hist"])
    relax = relaxation_time(result["std_hist"], result["time_hist"])
    diff_rate = early_diffusion_rate(result["peak_hist"], result["time_hist"])
    k3_max = float(np.max(result["k3_hist"])) if result["k3_hist"] else 0.0

    return {
        "name": result["name"],
        "D": result["D"],
        "n_cycles": n_cycles,
        "undershoot": undershoot,
        "overshoot": overshoot,
        "relax_time": relax,
        "early_diffusion_rate": diff_rate,
        "k3_max": k3_max,
        "total_clips": result["total_clips"],
        "final_std": result["final_rho_std"],
        "amplitudes": amplitudes,
    }


# ══════════════════════════════════════════════════════════════════════
# Plotting
# ══════════════════════════════════════════════════════════════════════

def plot_time_series(result, analysis, path):
    fig, ax = plt.subplots(figsize=(MAX_W_IN, MAX_H_IN))
    ax.plot(result["time_hist"], result["peak_hist"], "k-", lw=0.8)
    ax.axhline(RHO_STAR, color="blue", ls="--", alpha=0.5, label=r"$\rho^*$")
    ax.set_xlabel("Time")
    ax.set_ylabel(r"$\rho$ at peak site")
    ax.set_title(f"Peak density vs time — {result['name']}  "
                 f"({analysis['n_cycles']} cycles)")
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_envelope(result, analysis, path):
    fig, ax = plt.subplots(figsize=(MAX_W_IN, MAX_H_IN))
    if analysis["amplitudes"]:
        ax.plot(range(len(analysis["amplitudes"])), analysis["amplitudes"],
                "o-", color="darkred", ms=4, lw=1)
        ax.set_xlabel("Half-cycle index")
        ax.set_ylabel("Amplitude")
    else:
        ax.text(0.5, 0.5, "No oscillations detected", ha="center", va="center",
                transform=ax.transAxes, fontsize=14)
    ax.set_title(f"Oscillation envelope — {result['name']}")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_diffusion(result, analysis, path):
    fig, ax = plt.subplots(figsize=(MAX_W_IN, MAX_H_IN))
    ax.plot(result["time_hist"], result["std_hist"], "k-", lw=0.8)
    ax.set_xlabel("Time")
    ax.set_ylabel(r"$\sigma(\rho)$")
    rate = analysis["early_diffusion_rate"]
    ax.set_title(f"Spatial std evolution — {result['name']}  "
                 f"(early slope={rate:.4f})")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_mobility_comparison(all_results, all_analysis, path):
    fig, axes = plt.subplots(2, 2, figsize=(MAX_W_IN, MAX_H_IN))
    colors = ["black", "steelblue", "coral", "seagreen", "darkviolet"]

    # (0,0) Peak overlay
    ax = axes[0, 0]
    for i, (res, ana) in enumerate(zip(all_results, all_analysis)):
        lw = 1.8 if i == 0 else 0.9
        ls = "-" if i == 0 else "--"
        ax.plot(res["time_hist"], res["peak_hist"], color=colors[i],
                lw=lw, ls=ls, label=f"{res['name']} ({ana['n_cycles']}c)")
    ax.axhline(RHO_STAR, color="blue", ls=":", alpha=0.3)
    ax.set_xlabel("Time")
    ax.set_ylabel(r"$\rho_{\rm peak}$")
    ax.set_title("Peak density overlay")
    ax.legend(fontsize=7)

    # (0,1) Bar: oscillation count
    ax = axes[0, 1]
    names = [a["name"] for a in all_analysis]
    counts = [a["n_cycles"] for a in all_analysis]
    ax.bar(names, counts, color=colors[:len(names)])
    ax.set_ylabel("Oscillation cycles")
    ax.set_title("Oscillation count")
    ax.tick_params(axis="x", rotation=30, labelsize=8)

    # (1,0) Bar: undershoot / overshoot
    ax = axes[1, 0]
    x = np.arange(len(names))
    w = 0.35
    under = [a["undershoot"] for a in all_analysis]
    over  = [a["overshoot"] for a in all_analysis]
    ax.bar(x - w/2, under, w, label="Undershoot", color="steelblue")
    ax.bar(x + w/2, over,  w, label="Overshoot", color="coral")
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=30, fontsize=8)
    ax.set_ylabel("Amplitude")
    ax.set_title("Under/Overshoot")
    ax.legend(fontsize=7)

    # (1,1) Bar: relaxation time + diffusion rate
    ax = axes[1, 1]
    relax = [a["relax_time"] for a in all_analysis]
    ax.bar(names, relax, color=colors[:len(names)])
    ax.set_ylabel("Relaxation time")
    ax.set_title("Relaxation time")
    ax.tick_params(axis="x", rotation=30, labelsize=8)

    fig.suptitle("Mobility Robustness Comparison", fontsize=12, y=1.01)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


# ══════════════════════════════════════════════════════════════════════
# Boundary sweep (oscillation–death)
# ══════════════════════════════════════════════════════════════════════

def run_boundary_sweep(mob_fn, mob_prime_fn, name, D_values, n_steps=40_000):
    results = []
    dt = ETA * DX * DX / (M0 + EPS_NUM)
    for D in D_values:
        H = 1.0 - D
        rho, v = make_ic(NX)
        peak_idx = NX // 2
        peak_hist = []
        t = 0.0
        for step in range(n_steps):
            F = compute_rhs(rho, DX, mob_fn, mob_prime_fn)
            rho_new = rho + dt * (D * F + H * v)
            v_new   = v   + dt * (1.0 / TAU) * (F - ZETA * v)
            rho_new = np.clip(rho_new, EPS_NUM, RHO_MAX - EPS_NUM)
            rho = rho_new
            v   = v_new
            t  += dt
            if step % 100 == 0:
                peak_hist.append(float(rho[peak_idx]))
        n_cyc, _, _ = detect_oscillations(peak_hist)
        results.append({"D": D, "n_cycles": n_cyc})
    return results


# ══════════════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════════════

def main():
    print("=" * 70)
    print("ED-Phys-26: Mobility Robustness")
    print("=" * 70)
    print(f"Grid: {NX} sites, {N_STEPS} steps, sample every {SAMPLE}")
    print(f"Params: D={D_FIXED}, H={H_FIXED}, tau={TAU}, zeta={ZETA}")
    print(f"IC: Gaussian peak, A={AMP_IC}, sigma={SIGMA_IC}")
    print(f"Mobility perturbation: epsilon={EPSILON}")
    print("=" * 70)

    all_results  = []
    all_analysis = []

    # ── Run each mobility variant ─────────────────────────────────────
    for name, mob_fn, mob_prime_fn in MOBILITY_VARIANTS:
        print(f"\n>>> Running variant: {name}")
        result = run_case(name, mob_fn, mob_prime_fn)
        analysis = analyze_result(result)
        all_results.append(result)
        all_analysis.append(analysis)

        print(f"    cycles={analysis['n_cycles']}  undershoot={analysis['undershoot']:.4f}  "
              f"overshoot={analysis['overshoot']:.4f}  relax={analysis['relax_time']:.1f}  "
              f"diff_rate={analysis['early_diffusion_rate']:.6f}  k3_max={analysis['k3_max']:.4f}")

        # Per-variant plots
        plot_time_series(result, analysis, OUT / f"{name}_time_series.png")
        plot_envelope(result, analysis, OUT / f"{name}_envelope.png")
        plot_diffusion(result, analysis, OUT / f"{name}_diffusion.png")

    # ── Comparison plot ───────────────────────────────────────────────
    print("\n>>> Generating mobility comparison plot...")
    plot_mobility_comparison(all_results, all_analysis, OUT / "mobility_comparison.png")

    # ── Boundary sweep (oscillation–death) ────────────────────────────
    D_BOUNDARY = [0.44, 0.46, 0.48]
    print(f"\n>>> Boundary sweep: D = {D_BOUNDARY}")
    boundary_results = {}
    for name, mob_fn, mob_prime_fn in MOBILITY_VARIANTS:
        print(f"    sweeping {name}...")
        sweep = run_boundary_sweep(mob_fn, mob_prime_fn, name, D_BOUNDARY)
        boundary_results[name] = sweep
        for s in sweep:
            print(f"      D={s['D']:.2f} -> {s['n_cycles']} cycles")

    # ── Summary JSON ──────────────────────────────────────────────────
    export = {
        "experiment": "ED-Phys-26_MobilityRobustness",
        "parameters": {
            "NX": NX, "N_STEPS": N_STEPS, "SAMPLE": SAMPLE,
            "D": D_FIXED, "H": H_FIXED, "TAU": TAU, "ZETA": ZETA,
            "EPSILON": EPSILON, "AMP_IC": AMP_IC, "SIGMA_IC": SIGMA_IC,
            "RHO_STAR": RHO_STAR, "RHO_MAX": RHO_MAX,
        },
        "analysis": all_analysis,
        "boundary_sweep": boundary_results,
    }
    json_path = OUT / "mobility_robustness_summary.json"
    with open(json_path, "w") as f:
        json.dump(export, f, indent=2)
    print(f"\n>>> Summary written to {json_path}")

    # ── Print summary table ───────────────────────────────────────────
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"{'Variant':<14} {'Cycles':>7} {'Under':>9} {'Over':>9} "
          f"{'Relax':>9} {'DiffRate':>10} {'k3_max':>8}")
    print("-" * 70)
    for a in all_analysis:
        print(f"{a['name']:<14} {a['n_cycles']:>7} {a['undershoot']:>9.4f} "
              f"{a['overshoot']:>9.4f} {a['relax_time']:>9.1f} "
              f"{a['early_diffusion_rate']:>10.6f} {a['k3_max']:>8.4f}")
    print("=" * 70)

    print("\n>>> Boundary sweep results:")
    for name, sweep in boundary_results.items():
        cycles_str = ", ".join(f"D={s['D']:.2f}:{s['n_cycles']}c" for s in sweep)
        print(f"    {name}: {cycles_str}")

    print("\n>>> Done. All outputs in:", OUT)


if __name__ == "__main__":
    main()
