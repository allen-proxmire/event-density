#!/usr/bin/env python3
"""
ED-Phys-27: Participation Robustness
======================================
Tests robustness of the unified ED cosmology PDE under small perturbations
to the participation channel (the v-equation).

Unified PDE (1D):
    dρ/dt = D·F[ρ] + H·v
    dv/dt = (1/τ)(F[ρ] – ζ v)          [canonical]
    D + H = 1

Canonical operator:
    F[ρ] = M(ρ) ∇²ρ + M′(ρ)|∇ρ|² – P_SY2(ρ)

Participation variants (ε = 0.05):
    1. Canonical:   dv/dt = (1/τ)(F – ζ v)
    2. Stronger:    dv/dt = (1/τ)(F – ζ v)·(1 + ε)
    3. Weaker:      dv/dt = (1/τ)(F – ζ v)·(1 – ε)
    4. Asymmetric:  dv/dt = (1/τ)(F – ζ v)·(1 + ε·sign(F))
    5. Non-smooth:  dv/dt = (1/τ)(F – ζ v) + ε·tanh(F)
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

MAX_W_IN = 1000 / 150   # ~6.67 inches at 150 dpi
MAX_H_IN = 800 / 150    # ~5.33 inches at 150 dpi


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
# Participation variant v-update functions
# ══════════════════════════════════════════════════════════════════════
# Each returns dv/dt given (F, v, dt_factor=1/TAU).

def v_update_canonical(F, v):
    return (1.0 / TAU) * (F - ZETA * v)

def v_update_stronger(F, v):
    return (1.0 / TAU) * (F - ZETA * v) * (1.0 + EPSILON)

def v_update_weaker(F, v):
    return (1.0 / TAU) * (F - ZETA * v) * (1.0 - EPSILON)

def v_update_asymmetric(F, v):
    return (1.0 / TAU) * (F - ZETA * v) * (1.0 + EPSILON * np.sign(F))

def v_update_nonsmooth(F, v):
    return (1.0 / TAU) * (F - ZETA * v) + EPSILON * np.tanh(F)


PARTICIPATION_VARIANTS = [
    ("canonical",  v_update_canonical),
    ("stronger",   v_update_stronger),
    ("weaker",     v_update_weaker),
    ("asymmetric", v_update_asymmetric),
    ("nonsmooth",  v_update_nonsmooth),
]


# ══════════════════════════════════════════════════════════════════════
# Initial condition
# ══════════════════════════════════════════════════════════════════════

def make_ic(nx):
    x = np.arange(nx, dtype=np.float64)
    center = nx / 2.0
    rho = RHO_STAR + AMP_IC * np.exp(-((x - center) / SIGMA_IC) ** 2)
    rho = np.clip(rho, EPS_NUM, RHO_MAX - EPS_NUM)
    v = np.zeros(nx, dtype=np.float64)
    return rho, v


# ══════════════════════════════════════════════════════════════════════
# PDE integration
# ══════════════════════════════════════════════════════════════════════

def run_case(name, v_update_fn, D=D_FIXED, nx=NX, n_steps=N_STEPS,
             sample_every=SAMPLE):
    H = 1.0 - D
    rho, v = make_ic(nx)
    peak_idx = nx // 2
    dt = ETA * DX * DX / (M0 + EPS_NUM)

    peak_hist  = []
    vpeak_hist = []
    mean_hist  = []
    std_hist   = []
    time_hist  = []
    k3_hist    = []
    clips_total = 0

    t = 0.0
    for step in range(n_steps):
        F = compute_F(rho, DX)

        rho_new = rho + dt * (D * F + H * v)
        v_new   = v   + dt * v_update_fn(F, v)

        clips = int(np.sum(rho_new < EPS_NUM))
        clips_total += clips
        rho_new = np.clip(rho_new, EPS_NUM, RHO_MAX - EPS_NUM)

        rho = rho_new
        v   = v_new
        t  += dt

        if step % sample_every == 0:
            peak_hist.append(float(rho[peak_idx]))
            vpeak_hist.append(float(v[peak_idx]))
            mean_hist.append(float(np.mean(rho)))
            std_hist.append(float(np.std(rho)))
            time_hist.append(t)
            k3_hist.append(mode_amplitude_1d(rho, 3))

    return {
        "name": name,
        "D": D, "H": H, "dt": dt, "n_steps": n_steps,
        "peak_hist": peak_hist,
        "vpeak_hist": vpeak_hist,
        "mean_hist": mean_hist,
        "std_hist": std_hist,
        "time_hist": time_hist,
        "k3_hist": k3_hist,
        "total_clips": clips_total,
        "final_rho_peak": float(rho[peak_idx]),
        "final_rho_mean": float(np.mean(rho)),
        "final_rho_std": float(np.std(rho)),
    }


# ══════════════════════════════════════════════════════════════════════
# Analysis
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
    if len(peak_hist) < n_early:
        n_early = len(peak_hist)
    t = np.array(time_hist[:n_early])
    p = np.array(peak_hist[:n_early])
    if len(t) < 2:
        return 0.0
    coeffs = np.polyfit(t, p, 1)
    return float(coeffs[0])


def peak_v_first_cycle(vpeak_hist, peak_hist):
    """Peak |v| during the first oscillation cycle (before first zero-crossing of delta-rho)."""
    delta = np.array(peak_hist) - RHO_STAR
    # Find first zero crossing
    first_cross = len(delta)
    for i in range(1, len(delta)):
        if delta[i - 1] * delta[i] < 0:
            first_cross = i
            break
    seg = np.array(vpeak_hist[:first_cross])
    if len(seg) == 0:
        return 0.0
    return float(np.max(np.abs(seg)))


def eq_drift(mean_hist):
    """Drift of mean rho from rho_star at end of simulation."""
    return float(np.array(mean_hist[-1]) - RHO_STAR)


def analyze_result(result):
    n_cycles, amplitudes, crossings = detect_oscillations(result["peak_hist"])
    undershoot, overshoot = measure_undershoot_overshoot(result["peak_hist"])
    relax = relaxation_time(result["std_hist"], result["time_hist"])
    diff_rate = early_diffusion_rate(result["peak_hist"], result["time_hist"])
    k3_max = float(np.max(result["k3_hist"])) if result["k3_hist"] else 0.0
    vpeak = peak_v_first_cycle(result["vpeak_hist"], result["peak_hist"])
    drift = eq_drift(result["mean_hist"])

    return {
        "name": result["name"],
        "D": result["D"],
        "n_cycles": n_cycles,
        "undershoot": undershoot,
        "overshoot": overshoot,
        "relax_time": relax,
        "early_diffusion_rate": diff_rate,
        "peak_v_first_cycle": vpeak,
        "k3_max": k3_max,
        "eq_drift": drift,
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


def plot_v_channel(result, analysis, path):
    fig, ax = plt.subplots(figsize=(MAX_W_IN, MAX_H_IN))
    ax.plot(result["time_hist"], result["vpeak_hist"], "k-", lw=0.8)
    ax.axhline(0.0, color="gray", ls=":", alpha=0.4)
    vpeak = analysis["peak_v_first_cycle"]
    ax.set_xlabel("Time")
    ax.set_ylabel(r"$v$ at peak site")
    ax.set_title(f"Participation channel — {result['name']}  "
                 f"(peak |v| 1st cycle = {vpeak:.5f})")
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
                 f"(early slope = {rate:.4f})")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_phase_flag(result, analysis, path):
    """Phase portrait: rho_peak vs v_peak."""
    fig, ax = plt.subplots(figsize=(MAX_W_IN, MAX_H_IN))
    rp = np.array(result["peak_hist"])
    vp = np.array(result["vpeak_hist"])
    ax.plot(rp, vp, "k-", lw=0.5, alpha=0.7)
    ax.plot(rp[0], vp[0], "go", ms=8, label="start")
    ax.plot(rp[-1], vp[-1], "rs", ms=8, label="end")
    ax.axvline(RHO_STAR, color="blue", ls="--", alpha=0.3)
    ax.axhline(0.0, color="gray", ls=":", alpha=0.3)
    ax.set_xlabel(r"$\rho_{\rm peak}$")
    ax.set_ylabel(r"$v_{\rm peak}$")
    ax.set_title(f"Phase portrait — {result['name']}")
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_participation_comparison(all_results, all_analysis, path):
    fig, axes = plt.subplots(2, 3, figsize=(MAX_W_IN, MAX_H_IN))
    colors = ["black", "steelblue", "coral", "seagreen", "darkviolet"]
    names = [a["name"] for a in all_analysis]
    n = len(names)

    # (0,0) Peak density overlay
    ax = axes[0, 0]
    for i, (res, ana) in enumerate(zip(all_results, all_analysis)):
        lw = 1.8 if i == 0 else 0.9
        ls = "-" if i == 0 else "--"
        ax.plot(res["time_hist"], res["peak_hist"], color=colors[i],
                lw=lw, ls=ls, label=f"{res['name']} ({ana['n_cycles']}c)")
    ax.axhline(RHO_STAR, color="blue", ls=":", alpha=0.3)
    ax.set_xlabel("Time", fontsize=8)
    ax.set_ylabel(r"$\rho_{\rm peak}$", fontsize=8)
    ax.set_title("Peak density overlay", fontsize=9)
    ax.legend(fontsize=6)
    ax.tick_params(labelsize=7)

    # (0,1) v-channel overlay
    ax = axes[0, 1]
    for i, res in enumerate(all_results):
        lw = 1.8 if i == 0 else 0.9
        ls = "-" if i == 0 else "--"
        ax.plot(res["time_hist"], res["vpeak_hist"], color=colors[i],
                lw=lw, ls=ls, label=res["name"])
    ax.axhline(0.0, color="gray", ls=":", alpha=0.3)
    ax.set_xlabel("Time", fontsize=8)
    ax.set_ylabel(r"$v_{\rm peak}$", fontsize=8)
    ax.set_title("v-channel overlay", fontsize=9)
    ax.legend(fontsize=6)
    ax.tick_params(labelsize=7)

    # (0,2) Bar: oscillation count
    ax = axes[0, 2]
    counts = [a["n_cycles"] for a in all_analysis]
    ax.bar(names, counts, color=colors[:n])
    ax.set_ylabel("Cycles", fontsize=8)
    ax.set_title("Oscillation count", fontsize=9)
    ax.tick_params(axis="x", rotation=35, labelsize=7)
    ax.tick_params(axis="y", labelsize=7)

    # (1,0) Bar: undershoot / overshoot
    ax = axes[1, 0]
    x = np.arange(n)
    w = 0.35
    under = [a["undershoot"] for a in all_analysis]
    over  = [a["overshoot"] for a in all_analysis]
    ax.bar(x - w/2, under, w, label="Undershoot", color="steelblue")
    ax.bar(x + w/2, over,  w, label="Overshoot", color="coral")
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=35, fontsize=7)
    ax.set_ylabel("Amplitude", fontsize=8)
    ax.set_title("Under/Overshoot", fontsize=9)
    ax.legend(fontsize=6)
    ax.tick_params(axis="y", labelsize=7)

    # (1,1) Bar: peak |v| first cycle
    ax = axes[1, 1]
    vpvals = [a["peak_v_first_cycle"] for a in all_analysis]
    ax.bar(names, vpvals, color=colors[:n])
    ax.set_ylabel("Peak |v|", fontsize=8)
    ax.set_title("Participation strength (1st cycle)", fontsize=9)
    ax.tick_params(axis="x", rotation=35, labelsize=7)
    ax.tick_params(axis="y", labelsize=7)

    # (1,2) Bar: relaxation time
    ax = axes[1, 2]
    relax = [a["relax_time"] for a in all_analysis]
    ax.bar(names, relax, color=colors[:n])
    ax.set_ylabel("Relax time", fontsize=8)
    ax.set_title("Relaxation time", fontsize=9)
    ax.tick_params(axis="x", rotation=35, labelsize=7)
    ax.tick_params(axis="y", labelsize=7)

    fig.suptitle("Participation Robustness Comparison", fontsize=11, y=1.01)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


# ══════════════════════════════════════════════════════════════════════
# Boundary sweep (oscillation–death)
# ══════════════════════════════════════════════════════════════════════

def run_boundary_sweep(v_update_fn, name, D_values, n_steps=40_000):
    results = []
    dt = ETA * DX * DX / (M0 + EPS_NUM)
    for D in D_values:
        H = 1.0 - D
        rho, v = make_ic(NX)
        peak_idx = NX // 2
        peak_hist = []
        t = 0.0
        for step in range(n_steps):
            F = compute_F(rho, DX)
            rho_new = rho + dt * (D * F + H * v)
            v_new   = v   + dt * v_update_fn(F, v)
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
    print("ED-Phys-27: Participation Robustness")
    print("=" * 70)
    print(f"Grid: {NX} sites, {N_STEPS} steps, sample every {SAMPLE}")
    print(f"Params: D={D_FIXED}, H={H_FIXED}, tau={TAU}, zeta={ZETA}")
    print(f"IC: Gaussian peak, A={AMP_IC}, sigma={SIGMA_IC}")
    print(f"Participation perturbation: epsilon={EPSILON}")
    print("=" * 70)

    all_results  = []
    all_analysis = []

    # ── Run each participation variant ────────────────────────────────
    for name, v_fn in PARTICIPATION_VARIANTS:
        print(f"\n>>> Running variant: {name}")
        result = run_case(name, v_fn)
        analysis = analyze_result(result)
        all_results.append(result)
        all_analysis.append(analysis)

        print(f"    cycles={analysis['n_cycles']}  undershoot={analysis['undershoot']:.4f}  "
              f"overshoot={analysis['overshoot']:.4f}  relax={analysis['relax_time']:.1f}")
        print(f"    peak_v={analysis['peak_v_first_cycle']:.6f}  "
              f"diff_rate={analysis['early_diffusion_rate']:.6f}  "
              f"k3_max={analysis['k3_max']:.4f}  eq_drift={analysis['eq_drift']:.2e}")

        # Per-variant plots
        plot_time_series(result, analysis, OUT / f"{name}_time_series.png")
        plot_envelope(result, analysis, OUT / f"{name}_envelope.png")
        plot_v_channel(result, analysis, OUT / f"{name}_v_channel.png")
        plot_diffusion(result, analysis, OUT / f"{name}_diffusion.png")
        plot_phase_flag(result, analysis, OUT / f"{name}_phase_flag.png")

    # ── Comparison plot ───────────────────────────────────────────────
    print("\n>>> Generating participation comparison plot...")
    plot_participation_comparison(all_results, all_analysis,
                                  OUT / "participation_comparison.png")

    # ── Boundary sweep (oscillation–death) ────────────────────────────
    D_BOUNDARY = [0.44, 0.46, 0.48]
    print(f"\n>>> Boundary sweep: D = {D_BOUNDARY}")
    boundary_results = {}
    for name, v_fn in PARTICIPATION_VARIANTS:
        print(f"    sweeping {name}...")
        sweep = run_boundary_sweep(v_fn, name, D_BOUNDARY)
        boundary_results[name] = sweep
        for s in sweep:
            print(f"      D={s['D']:.2f} -> {s['n_cycles']} cycles")

    # ── Summary JSON ──────────────────────────────────────────────────
    export = {
        "experiment": "ED-Phys-27_ParticipationRobustness",
        "parameters": {
            "NX": NX, "N_STEPS": N_STEPS, "SAMPLE": SAMPLE,
            "D": D_FIXED, "H": H_FIXED, "TAU": TAU, "ZETA": ZETA,
            "EPSILON": EPSILON, "AMP_IC": AMP_IC, "SIGMA_IC": SIGMA_IC,
            "RHO_STAR": RHO_STAR, "RHO_MAX": RHO_MAX,
        },
        "analysis": all_analysis,
        "boundary_sweep": boundary_results,
    }
    json_path = OUT / "participation_robustness_summary.json"
    with open(json_path, "w") as f:
        json.dump(export, f, indent=2)
    print(f"\n>>> Summary written to {json_path}")

    # ── Print summary table ───────────────────────────────────────────
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"{'Variant':<14} {'Cyc':>4} {'Under':>9} {'Over':>9} "
          f"{'Relax':>8} {'PeakV':>10} {'DiffRate':>10} {'k3':>8} {'Drift':>10}")
    print("-" * 80)
    for a in all_analysis:
        print(f"{a['name']:<14} {a['n_cycles']:>4} {a['undershoot']:>9.4f} "
              f"{a['overshoot']:>9.4f} {a['relax_time']:>8.1f} "
              f"{a['peak_v_first_cycle']:>10.6f} "
              f"{a['early_diffusion_rate']:>10.6f} {a['k3_max']:>8.4f} "
              f"{a['eq_drift']:>10.2e}")
    print("=" * 80)

    print("\n>>> Boundary sweep results:")
    for name, sweep in boundary_results.items():
        cycles_str = ", ".join(f"D={s['D']:.2f}:{s['n_cycles']}c" for s in sweep)
        print(f"    {name}: {cycles_str}")

    print("\n>>> Done. All outputs in:", OUT)


if __name__ == "__main__":
    main()
