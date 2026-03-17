"""
ED-Arch: Amplitude Sweep at Fixed D = 0.50
===========================================
Measures how oscillatory behavior depends on initial peak amplitude
at the oscillation-death boundary D = 0.50 in the unified ED cosmology PDE:

    drho/dt = D*F[rho] + H*v
    dv/dt   = (1/tau)(F[rho] - zeta*v)
    D + H = 1,  D = H = 0.50

F[rho] = M(rho)*Lap(rho) + M'(rho)*|grad(rho)|^2 - P_SY2(rho)

Canonical parameters throughout.  Single Gaussian peak IC with variable A.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
import json
import time as timer_mod

# =========================================================================
#  Canonical Parameters
# =========================================================================
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
ETA      = 0.2        # CFL factor
EPS      = 1e-10

# =========================================================================
#  Grid
# =========================================================================
NX       = 256
N_STEPS  = 80_000
SAMPLE   = 40          # sample every 40 steps -> 2000 snapshots

# =========================================================================
#  Fixed mixing & sweep values
# =========================================================================
D_FIXED  = 0.50
H_FIXED  = 0.50
A_VALUES = [20.0, 30.0, 40.0, 50.0, 60.0]
SIGMA_IC = 12.0        # Gaussian width (same for all)

# =========================================================================
#  Output directory
# =========================================================================
OUT = Path(__file__).parent / "results"
OUT.mkdir(exist_ok=True)


# =========================================================================
#  Core ED operators  (identical to ED-Arch-OscDeath)
# =========================================================================

def mobility(rho):
    return M0 * np.maximum(1.0 - rho / RHO_MAX, 0.0) ** N_MOB

def mobility_prime(rho):
    return -M0 * (N_MOB / RHO_MAX) * np.maximum(1.0 - rho / RHO_MAX, 0.0) ** (N_MOB - 1)

def penalty_sy2(rho):
    delta = rho - RHO_STAR
    return ALPHA * GAMMA * delta / np.sqrt(delta * delta + RHO_0 * RHO_0)

def compute_rhs(rho, dx):
    """F[rho] = M*Lap + M'*|grad|^2 - P_SY2"""
    M  = mobility(rho)
    Mp = mobility_prime(rho)
    lap     = (np.roll(rho, 1) + np.roll(rho, -1) - 2.0 * rho) / (dx * dx)
    grad_sq = ((np.roll(rho, 1) - np.roll(rho, -1)) / (2.0 * dx)) ** 2
    return M * lap + Mp * grad_sq - penalty_sy2(rho)


# =========================================================================
#  Initial condition  (variable amplitude)
# =========================================================================

def make_ic(nx, amplitude, sigma=SIGMA_IC):
    """rho(x,0) = rho* + A*exp(-((x-center)/sigma)^2 / 2),  v=0."""
    x      = np.arange(nx, dtype=np.float64)
    center = nx / 2.0
    rho    = RHO_STAR + amplitude * np.exp(-0.5 * ((x - center) / sigma) ** 2)
    rho    = np.clip(rho, EPS, RHO_MAX - EPS)
    v      = np.zeros(nx, dtype=np.float64)
    return rho, v


# =========================================================================
#  Time integrator
# =========================================================================

def run_amplitude_case(amplitude, D=D_FIXED, nx=NX,
                       n_steps=N_STEPS, sample_every=SAMPLE):
    """Run the unified PDE for one amplitude value at fixed D."""
    H = 1.0 - D
    rho, v = make_ic(nx, amplitude)
    peak_idx = nx // 2

    dt = ETA * DX * DX / (M0 + EPS)

    # storage
    peak_hist    = []
    mean_hist    = []
    std_hist     = []
    time_hist    = []
    horizon_hist = []
    clips_total  = 0

    t = 0.0
    for step in range(n_steps):
        F = compute_rhs(rho, DX)

        rho_new = rho + dt * (D * F + H * v)
        v_new   = v   + dt * (1.0 / TAU) * (F - ZETA * v)

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
            horizon_hist.append(int(np.sum(rho >= 0.9 * RHO_MAX)))

    return {
        "amplitude":     amplitude,
        "D":             D,
        "H":             H,
        "dt":            dt,
        "n_steps":       n_steps,
        "peak_hist":     peak_hist,
        "mean_hist":     mean_hist,
        "std_hist":      std_hist,
        "time_hist":     time_hist,
        "horizon_hist":  horizon_hist,
        "total_clips":   clips_total,
        "final_rho_peak": float(rho[peak_idx]),
        "final_rho_std":  float(np.std(rho)),
        "initial_peak":  float(min(RHO_STAR + amplitude, RHO_MAX - EPS)),
    }


# =========================================================================
#  Analysis
# =========================================================================

def detect_oscillations(peak_hist, rho_star=RHO_STAR):
    """
    Count zero-crossings of (peak - rho_star).
    Returns: n_cycles, amplitudes[], crossing_indices[].
    """
    delta = np.array(peak_hist) - rho_star
    crossings = []
    for i in range(1, len(delta)):
        if delta[i - 1] * delta[i] < 0:
            crossings.append(i)

    n_cycles = len(crossings) // 2

    # amplitude envelope between successive crossings
    amplitudes = []
    for i in range(len(crossings) - 1):
        seg = delta[crossings[i]:crossings[i + 1]]
        if len(seg) > 0:
            amplitudes.append(float(np.max(np.abs(seg))))

    return n_cycles, amplitudes, crossings


def measure_undershoot_overshoot(peak_hist, rho_star=RHO_STAR):
    """Measure max undershoot and overshoot relative to rho*."""
    delta = np.array(peak_hist) - rho_star
    undershoot = float(-np.min(delta)) if np.min(delta) < 0 else 0.0
    # overshoot = any rise ABOVE rho* AFTER the initial decay
    # find first crossing below rho*
    below_idx = np.where(delta < 0)[0]
    if len(below_idx) > 0:
        first_below = below_idx[0]
        after = delta[first_below:]
        overshoot = float(np.max(after)) if np.max(after) > 0 else 0.0
    else:
        overshoot = 0.0
    return undershoot, overshoot


def horizon_lifetime(horizon_hist, threshold=0):
    return int(np.sum(np.array(horizon_hist) > threshold))


def classify_amplitude_regime(n_cycles, undershoot, overshoot):
    if n_cycles >= 2:
        return "multi-cycle"
    elif undershoot > 0.01:
        return "single-undershoot"
    else:
        return "parabolic-like"


# =========================================================================
#  Plotting
# =========================================================================

def plot_time_series(result, path):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(result["time_hist"], result["peak_hist"], "k-", lw=0.8)
    ax.axhline(RHO_STAR, color="blue", ls="--", alpha=0.5, label=r"$\rho^*$")
    ax.set_xlabel("Time")
    ax.set_ylabel(r"$\rho$ at peak site")
    ax.set_title(f"Peak density vs time   (A = {result['amplitude']:.0f},  D = {D_FIXED})")
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_envelope(result, n_cycles, amplitudes, path):
    fig, ax = plt.subplots(figsize=(10, 4))
    if amplitudes:
        ax.plot(range(len(amplitudes)), amplitudes, "o-", ms=3, color="crimson")
        ax.set_xlabel("Half-cycle index")
        ax.set_ylabel(r"Amplitude $|\rho - \rho^*|$")
    else:
        ax.text(0.5, 0.5, "No oscillations detected",
                transform=ax.transAxes, ha="center", va="center", fontsize=14)
    ax.set_title(f"Oscillation envelope   (A = {result['amplitude']:.0f},  {n_cycles} cycles)")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_horizon(result, hor_life, path):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(result["time_hist"], result["horizon_hist"], "g-", lw=0.8)
    ax.set_xlabel("Time")
    ax.set_ylabel(r"Horizon sites ($\rho \geq 0.9\,\rho_{max}$)")
    ax.set_title(f"Horizon extent vs time   (A = {result['amplitude']:.0f},  "
                 f"lifetime = {hor_life} samples)")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_phase_flag(result, regime, n_cycles, path):
    cmap = {"multi-cycle": "#2196F3",
            "single-undershoot": "#FF9800",
            "parabolic-like": "#4CAF50"}
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_axis_off()
    ax.add_patch(plt.Rectangle((0.05, 0.1), 0.9, 0.8,
                                facecolor=cmap.get(regime, "gray"),
                                edgecolor="black", lw=2, alpha=0.85))
    ax.text(0.5, 0.6, regime.upper().replace("-", " "),
            ha="center", va="center", fontsize=22, fontweight="bold", color="white")
    ax.text(0.5, 0.35, f"A = {result['amplitude']:.0f}   |   {n_cycles} cycles",
            ha="center", va="center", fontsize=14, color="white")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_overlay(all_results, all_analysis, path):
    """Overlay all amplitudes on one peak-vs-time plot."""
    fig, ax = plt.subplots(figsize=(12, 5))
    cmap = plt.cm.plasma
    n = len(all_results)
    for i, (res, ana) in enumerate(zip(all_results, all_analysis)):
        c = cmap(i / max(n - 1, 1))
        ax.plot(res["time_hist"], res["peak_hist"], color=c, lw=0.9,
                label=f"A={res['amplitude']:.0f} ({ana['regime']}, {ana['n_cycles']}c)")
    ax.axhline(RHO_STAR, color="blue", ls="--", alpha=0.4)
    ax.set_xlabel("Time")
    ax.set_ylabel(r"$\rho$ at peak site")
    ax.set_title(f"Amplitude Sweep at D = {D_FIXED}: Peak Density vs Time")
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_amplitude_vs_cycles(all_analysis, path):
    """Bar chart: cycles as a function of A."""
    fig, ax = plt.subplots(figsize=(8, 5))
    As     = [a["amplitude"] for a in all_analysis]
    cycles = [a["n_cycles"] for a in all_analysis]
    cmap_r = {"multi-cycle": "#2196F3",
              "single-undershoot": "#FF9800",
              "parabolic-like": "#4CAF50"}
    colors = [cmap_r[a["regime"]] for a in all_analysis]
    ax.bar(range(len(As)), cycles, color=colors, edgecolor="black", width=0.6)
    ax.set_xticks(range(len(As)))
    ax.set_xticklabels([f"{a:.0f}" for a in As])
    ax.set_xlabel("Initial amplitude A")
    ax.set_ylabel("Oscillation cycles")
    ax.set_title(f"Oscillation Count vs Amplitude  (D = {D_FIXED})")
    from matplotlib.patches import Patch
    legend_el = [Patch(facecolor=c, edgecolor="black", label=l)
                 for l, c in cmap_r.items()]
    ax.legend(handles=legend_el, fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_undershoot_overshoot(all_analysis, path):
    """Undershoot and overshoot depth vs amplitude."""
    fig, ax = plt.subplots(figsize=(8, 5))
    As = [a["amplitude"] for a in all_analysis]
    us = [a["undershoot"] for a in all_analysis]
    os_ = [a["overshoot"] for a in all_analysis]
    ax.plot(As, us, "o-", color="crimson", label="Undershoot depth", ms=6)
    ax.plot(As, os_, "s-", color="royalblue", label="Overshoot height", ms=6)
    ax.set_xlabel("Initial amplitude A")
    ax.set_ylabel(r"$|\rho - \rho^*|$")
    ax.set_title(f"Undershoot / Overshoot vs Amplitude  (D = {D_FIXED})")
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_horizon_vs_amplitude(all_analysis, path):
    """Horizon lifetime vs amplitude."""
    fig, ax = plt.subplots(figsize=(8, 5))
    As = [a["amplitude"] for a in all_analysis]
    hl = [a["horizon_lifetime"] for a in all_analysis]
    ax.bar(range(len(As)), hl, color="seagreen", edgecolor="black", width=0.6)
    ax.set_xticks(range(len(As)))
    ax.set_xticklabels([f"{a:.0f}" for a in As])
    ax.set_xlabel("Initial amplitude A")
    ax.set_ylabel("Horizon lifetime (samples)")
    ax.set_title(f"Horizon Lifetime vs Amplitude  (D = {D_FIXED})")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


# =========================================================================
#  Main
# =========================================================================

def main():
    print("=" * 70)
    print("ED-Arch: Amplitude Sweep at Fixed D = 0.50")
    print("=" * 70)
    print(f"Grid: {NX} sites, {N_STEPS} steps, sample every {SAMPLE}")
    print(f"Canonical: alpha={ALPHA}, gamma={GAMMA}, rho*={RHO_STAR}, rho0={RHO_0}")
    print(f"Oscillator: tau={TAU}, zeta={ZETA}")
    print(f"Fixed D={D_FIXED}, H={H_FIXED}")
    print(f"IC: Gaussian peak, sigma={SIGMA_IC}")
    print(f"A values: {A_VALUES}")
    print(f"Peak rho values: {[RHO_STAR + a for a in A_VALUES]}")
    print("=" * 70)

    all_results  = []
    all_analysis = []

    for A in A_VALUES:
        peak_rho = min(RHO_STAR + A, RHO_MAX - EPS)
        print(f"\n-- A = {A:.0f}  (peak rho = {peak_rho:.1f}) --")
        t0 = timer_mod.time()
        result = run_amplitude_case(A)
        elapsed = timer_mod.time() - t0
        print(f"   Simulation: {elapsed:.1f}s,  clips={result['total_clips']}")

        # Analyze
        n_cycles, amplitudes, crossings = detect_oscillations(result["peak_hist"])
        hor_life = horizon_lifetime(result["horizon_hist"])
        undershoot, overshoot = measure_undershoot_overshoot(result["peak_hist"])
        regime = classify_amplitude_regime(n_cycles, undershoot, overshoot)

        print(f"   Cycles: {n_cycles},  regime: {regime}")
        print(f"   Undershoot: {undershoot:.4f},  Overshoot: {overshoot:.4f}")
        print(f"   Horizon lifetime: {hor_life} samples")
        if amplitudes:
            print(f"   Amp envelope: {amplitudes[0]:.4f} -> {amplitudes[-1]:.4f}")

        # Check for non-monotonic amplitude decay
        non_monotonic = False
        if len(amplitudes) >= 3:
            for j in range(1, len(amplitudes)):
                if amplitudes[j] > amplitudes[j - 1] * 1.05:
                    non_monotonic = True
                    break

        analysis = {
            "amplitude":         A,
            "D":                 D_FIXED,
            "H":                 H_FIXED,
            "initial_peak_rho":  peak_rho,
            "n_cycles":          n_cycles,
            "n_crossings":       len(crossings),
            "regime":            regime,
            "undershoot":        undershoot,
            "overshoot":         overshoot,
            "horizon_lifetime":  hor_life,
            "horizon_activated": hor_life > 0,
            "non_monotonic_decay": non_monotonic,
            "amplitudes":        amplitudes,
            "total_clips":       result["total_clips"],
            "final_std":         result["final_rho_std"],
        }

        all_results.append(result)
        all_analysis.append(analysis)

        # Per-amplitude plots
        tag = f"A{int(A):02d}"
        plot_time_series(result, OUT / f"{tag}_time_series.png")
        plot_envelope(result, n_cycles, amplitudes, OUT / f"{tag}_oscillation_envelope.png")
        plot_horizon(result, hor_life, OUT / f"{tag}_horizon_lifetime.png")
        plot_phase_flag(result, regime, n_cycles, OUT / f"{tag}_phase_flag.png")
        print(f"   Plots saved: {tag}_*.png")

    # -- Summary plots --
    plot_overlay(all_results, all_analysis, OUT / "overlay_all_amplitudes.png")
    plot_amplitude_vs_cycles(all_analysis, OUT / "amplitude_vs_cycles.png")
    plot_undershoot_overshoot(all_analysis, OUT / "undershoot_overshoot.png")
    plot_horizon_vs_amplitude(all_analysis, OUT / "horizon_vs_amplitude.png")
    print("\nSummary plots saved.")

    # -- Summary table --
    print("\n" + "=" * 100)
    print(f"{'A':>5} | {'peak':>6} | {'cycles':>6} | {'regime':>18} | "
          f"{'under':>8} | {'over':>8} | {'hor_life':>8} | {'clips':>6} | {'non_mono':>8} | notes")
    print("-" * 100)
    for a in all_analysis:
        notes_parts = []
        if a["horizon_activated"]:
            notes_parts.append("horizon ON")
        if a["non_monotonic_decay"]:
            notes_parts.append("NON-MONOTONIC")
        if a["total_clips"] > 0:
            notes_parts.append(f"{a['total_clips']} clips")
        notes = ", ".join(notes_parts) if notes_parts else "clean"
        print(f"{a['amplitude']:>5.0f} | {a['initial_peak_rho']:>6.1f} | "
              f"{a['n_cycles']:>6} | {a['regime']:>18} | "
              f"{a['undershoot']:>8.4f} | {a['overshoot']:>8.4f} | "
              f"{a['horizon_lifetime']:>8} | {a['total_clips']:>6} | "
              f"{str(a['non_monotonic_decay']):>8} | {notes}")
    print("=" * 100)

    # -- JSON export --
    export = []
    for a in all_analysis:
        row = dict(a)
        row["amplitudes"] = row["amplitudes"][:20]
        export.append(row)
    with open(OUT / "amplitude_sweep_summary.json", "w") as f:
        json.dump(export, f, indent=2)
    print(f"\nJSON: {OUT / 'amplitude_sweep_summary.json'}")
    print("Done.")


if __name__ == "__main__":
    main()
