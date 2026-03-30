"""
ED-Arch: Oscillation-Death Phase Boundary Test Harness
======================================================
Measures the oscillation-death transition around D = 0.5 in the unified
ED cosmology PDE:

    dρ/dt = D·F[ρ] + H·v
    dv/dt = (1/τ)(F[ρ] − ζ·v)
    D + H = 1

F[ρ] = M(ρ)·∇²ρ + M'(ρ)·|∇ρ|² − P_SY2(ρ)

Canonical parameters throughout. Single Gaussian peak IC.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
import json
import time

# ── Canonical Parameters ──────────────────────────────────────────────
ALPHA   = 0.1
GAMMA   = 0.5
M0      = 1.0
RHO_MAX = 100.0
N_MOB   = 2
RHO_STAR = 50.0
RHO_0   = 0.5
TAU     = 100.0
ZETA    = 0.5
DX      = 1.0
ETA     = 0.2          # CFL factor
EPS     = 1e-10

# ── Grid ──────────────────────────────────────────────────────────────
NX       = 256
N_STEPS  = 80_000
SAMPLE   = 40           # sample every 40 steps -> 2000 snapshots

# ── Sweep values ──────────────────────────────────────────────────────
D_VALUES = [0.45, 0.48, 0.50, 0.52, 0.55]

# ── Output directory ──────────────────────────────────────────────────
OUT = Path(__file__).parent / "results"
OUT.mkdir(exist_ok=True)


# ═════════════════════════════════════════════════════════════════════
#  Core ED operators
# ═════════════════════════════════════════════════════════════════════

def mobility(rho):
    return M0 * np.maximum(1.0 - rho / RHO_MAX, 0.0) ** N_MOB

def mobility_prime(rho):
    return -M0 * (N_MOB / RHO_MAX) * np.maximum(1.0 - rho / RHO_MAX, 0.0) ** (N_MOB - 1)

def penalty_sy2(rho):
    delta = rho - RHO_STAR
    return ALPHA * GAMMA * delta / np.sqrt(delta * delta + RHO_0 * RHO_0)

def compute_rhs(rho, dx):
    """F[ρ] = M·∇²ρ + M'·|∇ρ|² − P_SY2"""
    M  = mobility(rho)
    Mp = mobility_prime(rho)
    lap = (np.roll(rho, 1) + np.roll(rho, -1) - 2.0 * rho) / (dx * dx)
    grad_sq = ((np.roll(rho, 1) - np.roll(rho, -1)) / (2.0 * dx)) ** 2
    return M * lap + Mp * grad_sq - penalty_sy2(rho)


# ═════════════════════════════════════════════════════════════════════
#  Initial condition
# ═════════════════════════════════════════════════════════════════════

def make_ic(nx, amplitude=40.0, sigma=12.0):
    """Single Gaussian peak: ρ* + A·exp(-(x-center)²/(2σ²)), v=0."""
    x = np.arange(nx, dtype=np.float64)
    center = nx / 2.0
    rho = RHO_STAR + amplitude * np.exp(-0.5 * ((x - center) / sigma) ** 2)
    rho = np.clip(rho, EPS, RHO_MAX - EPS)
    v   = np.zeros(nx, dtype=np.float64)
    return rho, v


# ═════════════════════════════════════════════════════════════════════
#  Time integrator (forward Euler, hybrid PDE)
# ═════════════════════════════════════════════════════════════════════

def run_sweep_case(D, nx=NX, n_steps=N_STEPS, sample_every=SAMPLE):
    """
    Run the unified PDE for a single D value.
    Returns dict with time series and diagnostics.
    """
    H = 1.0 - D
    rho, v = make_ic(nx)
    peak_idx = nx // 2

    # Adaptive dt from CFL
    M_max = M0
    dt = ETA * DX * DX / (M_max + EPS)

    # Storage
    peak_hist   = []
    mean_hist   = []
    std_hist    = []
    time_hist   = []
    clips_total = 0
    horizon_hist = []     # number of sites above 0.9*RHO_MAX

    t = 0.0
    for step in range(n_steps):
        F = compute_rhs(rho, DX)

        # Unified PDE update
        rho_new = rho + dt * (D * F + H * v)
        v_new   = v   + dt * (1.0 / TAU) * (F - ZETA * v)

        # Positivity clipping
        clips = int(np.sum(rho_new < EPS))
        clips_total += clips
        rho_new = np.clip(rho_new, EPS, RHO_MAX - EPS)

        rho = rho_new
        v   = v_new
        t  += dt

        if step % sample_every == 0:
            peak_hist.append(float(rho[peak_idx]))
            mean_hist.append(float(np.mean(rho)))
            std_hist.append(float(np.std(rho)))
            time_hist.append(t)
            n_horizon = int(np.sum(rho >= 0.9 * RHO_MAX))
            horizon_hist.append(n_horizon)

    return {
        "D": D,
        "H": H,
        "dt": dt,
        "n_steps": n_steps,
        "peak_hist":    peak_hist,
        "mean_hist":    mean_hist,
        "std_hist":     std_hist,
        "time_hist":    time_hist,
        "horizon_hist": horizon_hist,
        "total_clips":  clips_total,
        "final_rho_peak": float(rho[peak_idx]),
        "final_rho_std":  float(np.std(rho)),
    }


# ═════════════════════════════════════════════════════════════════════
#  Analysis helpers
# ═════════════════════════════════════════════════════════════════════

def detect_oscillations(peak_hist, rho_star=RHO_STAR, min_amp=0.05):
    """
    Count zero-crossings of (peak - rho_star) and extract amplitude envelope.
    Returns: n_cycles, amplitudes[], crossing_indices[].
    """
    delta = np.array(peak_hist) - rho_star
    crossings = []
    for i in range(1, len(delta)):
        if delta[i - 1] * delta[i] < 0:
            crossings.append(i)

    # Each pair of crossings = half cycle -> n_cycles = len(crossings) // 2
    n_cycles = len(crossings) // 2

    # Amplitude envelope: peak-to-peak between crossings
    amplitudes = []
    for i in range(len(crossings) - 1):
        seg = delta[crossings[i]:crossings[i + 1]]
        if len(seg) > 0:
            amplitudes.append(float(np.max(np.abs(seg))))

    return n_cycles, amplitudes, crossings


def horizon_lifetime(horizon_hist, threshold=0):
    """Number of samples where horizon sites > threshold."""
    return int(np.sum(np.array(horizon_hist) > threshold))


def classify_regime(n_cycles):
    if n_cycles >= 3:
        return "oscillatory"
    elif n_cycles >= 1:
        return "hybrid"
    else:
        return "parabolic"


# ═════════════════════════════════════════════════════════════════════
#  Plotting
# ═════════════════════════════════════════════════════════════════════

def plot_time_series(result, path):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(result["time_hist"], result["peak_hist"], "k-", linewidth=0.8)
    ax.axhline(RHO_STAR, color="blue", linestyle="--", alpha=0.5, label=r"$\rho^*$")
    ax.set_xlabel("Time")
    ax.set_ylabel(r"$\rho$ at peak site")
    ax.set_title(f"Peak density vs time   (D = {result['D']:.2f})")
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_envelope(result, n_cycles, amplitudes, path):
    fig, ax = plt.subplots(figsize=(10, 4))
    if amplitudes:
        ax.plot(range(len(amplitudes)), amplitudes, "o-", ms=3, color="crimson")
        ax.set_xlabel("Half-cycle index")
        ax.set_ylabel("Amplitude |ρ − ρ*|")
    else:
        ax.text(0.5, 0.5, "No oscillations detected",
                transform=ax.transAxes, ha="center", va="center", fontsize=14)
    ax.set_title(f"Oscillation envelope   (D = {result['D']:.2f},  {n_cycles} cycles)")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_horizon(result, hor_life, path):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(result["time_hist"], result["horizon_hist"], "g-", linewidth=0.8)
    ax.set_xlabel("Time")
    ax.set_ylabel("Horizon sites (ρ ≥ 0.9 ρ_max)")
    ax.set_title(f"Horizon extent vs time   (D = {result['D']:.2f},  lifetime = {hor_life} samples)")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_phase_flag(result, regime, n_cycles, path):
    colors = {"oscillatory": "#2196F3", "hybrid": "#FF9800", "parabolic": "#4CAF50"}
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_axis_off()
    ax.add_patch(plt.Rectangle((0.05, 0.1), 0.9, 0.8,
                                facecolor=colors.get(regime, "gray"),
                                edgecolor="black", linewidth=2, alpha=0.85))
    ax.text(0.5, 0.6, regime.upper(), ha="center", va="center",
            fontsize=28, fontweight="bold", color="white")
    ax.text(0.5, 0.35, f"D = {result['D']:.2f}   |   {n_cycles} cycles",
            ha="center", va="center", fontsize=14, color="white")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_overlay(all_results, all_analysis, path):
    """Overlay all D values on one peak-vs-time plot."""
    fig, ax = plt.subplots(figsize=(12, 5))
    cmap = plt.cm.viridis
    for i, (res, ana) in enumerate(zip(all_results, all_analysis)):
        c = cmap(i / max(len(all_results) - 1, 1))
        ax.plot(res["time_hist"], res["peak_hist"], color=c, linewidth=0.9,
                label=f"D={res['D']:.2f} ({ana['regime']}, {ana['n_cycles']}c)")
    ax.axhline(RHO_STAR, color="blue", linestyle="--", alpha=0.4)
    ax.set_xlabel("Time")
    ax.set_ylabel(r"$\rho$ at peak site")
    ax.set_title("Oscillation-Death Boundary: Peak Density vs Time")
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_phase_diagram(all_analysis, path):
    """Cycles vs D with regime coloring."""
    fig, ax = plt.subplots(figsize=(8, 5))
    Ds     = [a["D"] for a in all_analysis]
    cycles = [a["n_cycles"] for a in all_analysis]
    colors_map = {"oscillatory": "#2196F3", "hybrid": "#FF9800", "parabolic": "#4CAF50"}
    colors = [colors_map[a["regime"]] for a in all_analysis]
    ax.bar(range(len(Ds)), cycles, color=colors, edgecolor="black", width=0.6)
    ax.set_xticks(range(len(Ds)))
    ax.set_xticklabels([f"{d:.2f}" for d in Ds])
    ax.set_xlabel("D (parabolic weight)")
    ax.set_ylabel("Oscillation cycles")
    ax.set_title("Oscillation Count vs D")
    # Legend
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor=c, edgecolor="black", label=l)
                       for l, c in colors_map.items()]
    ax.legend(handles=legend_elements, fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


# ═════════════════════════════════════════════════════════════════════
#  Main
# ═════════════════════════════════════════════════════════════════════

def main():
    print("=" * 70)
    print("ED-Arch: Oscillation-Death Phase Boundary Experiment")
    print("=" * 70)
    print(f"Grid: {NX} sites, {N_STEPS} steps, sample every {SAMPLE}")
    print(f"Canonical: alpha={ALPHA}, gamma={GAMMA}, rho*={RHO_STAR}, rho0={RHO_0}")
    print(f"Oscillator: tau={TAU}, zeta={ZETA}")
    print(f"IC: Gaussian peak, A=40, sigma=12  (peak ~ 90, below ceiling)")
    print(f"D values: {D_VALUES}")
    print("=" * 70)

    all_results  = []
    all_analysis = []

    for D in D_VALUES:
        print(f"\n-- D = {D:.2f}  (H = {1-D:.2f}) --")
        t0 = time.time()
        result = run_sweep_case(D)
        elapsed = time.time() - t0
        print(f"   Simulation: {elapsed:.1f}s,  clips={result['total_clips']}")

        # Analyze
        n_cycles, amplitudes, crossings = detect_oscillations(result["peak_hist"])
        hor_life = horizon_lifetime(result["horizon_hist"])
        regime   = classify_regime(n_cycles)

        print(f"   Cycles: {n_cycles},  regime: {regime},  horizon life: {hor_life} samples")
        if amplitudes:
            print(f"   Amp range: {amplitudes[0]:.4f} -> {amplitudes[-1]:.4f}")

        analysis = {
            "D": D,
            "H": 1 - D,
            "n_cycles": n_cycles,
            "regime": regime,
            "horizon_lifetime": hor_life,
            "n_crossings": len(crossings),
            "amplitudes": amplitudes,
            "total_clips": result["total_clips"],
            "final_std": result["final_rho_std"],
        }

        all_results.append(result)
        all_analysis.append(analysis)

        # Per-D plots
        tag = f"D{D:.2f}".replace(".", "")
        plot_time_series(result, OUT / f"{tag}_time_series.png")
        plot_envelope(result, n_cycles, amplitudes, OUT / f"{tag}_oscillation_envelope.png")
        plot_horizon(result, hor_life, OUT / f"{tag}_horizon_lifetime.png")
        plot_phase_flag(result, regime, n_cycles, OUT / f"{tag}_phase_flag.png")
        print(f"   Plots saved: {tag}_*.png")

    # ── Summary plots ──
    plot_overlay(all_results, all_analysis, OUT / "overlay_all_D.png")
    plot_phase_diagram(all_analysis, OUT / "phase_diagram.png")
    print("\nSummary plots saved: overlay_all_D.png, phase_diagram.png")

    # ── Summary table ──
    print("\n" + "=" * 80)
    print(f"{'D':>6} | {'cycles':>6} | {'regime':>12} | {'hor_life':>10} | {'clips':>8} | {'final_std':>10} | notes")
    print("-" * 80)
    for a in all_analysis:
        notes = ""
        if a["n_cycles"] > 0 and a["amplitudes"]:
            notes = f"amp {a['amplitudes'][0]:.3f}->{a['amplitudes'][-1]:.4f}"
        elif a["n_cycles"] == 0:
            notes = "monotonic decay"
        print(f"{a['D']:>6.2f} | {a['n_cycles']:>6} | {a['regime']:>12} | "
              f"{a['horizon_lifetime']:>10} | {a['total_clips']:>8} | "
              f"{a['final_std']:>10.6f} | {notes}")
    print("=" * 80)

    # ── JSON export ──
    export = []
    for a in all_analysis:
        row = dict(a)
        row["amplitudes"] = row["amplitudes"][:20]  # truncate for readability
        export.append(row)
    with open(OUT / "oscdeath_summary.json", "w") as f:
        json.dump(export, f, indent=2)
    print(f"\nJSON summary: {OUT / 'oscdeath_summary.json'}")
    print("Done.")


if __name__ == "__main__":
    main()
