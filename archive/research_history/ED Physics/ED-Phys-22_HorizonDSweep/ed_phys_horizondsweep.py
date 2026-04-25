"""
ED-Phys-22: Horizon D-Sweep
============================
Measures how horizon activation and horizon lifetime depend on the
mixing parameter D near the oscillation-death boundary.

Unified PDE:
    drho/dt = D*F[rho] + H*v
    dv/dt   = (1/tau)(F[rho] - zeta*v)
    D + H = 1

F[rho] = M(rho)*Lap(rho) + M'(rho)*|grad(rho)|^2 - P_SY2(rho)

IC: tall Gaussian peak that exceeds the ceiling (A=70, peak ~ 120).
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
ETA      = 0.2
EPS      = 1e-10

HORIZON_THRESH = 0.9 * RHO_MAX   # 90.0

# =========================================================================
#  Grid and sweep
# =========================================================================
NX       = 256
N_STEPS  = 80_000
SAMPLE   = 20          # finer sampling for horizon dynamics (4000 snapshots)

D_VALUES  = [0.45, 0.48, 0.50, 0.52, 0.55]
AMP_IC    = 70.0       # peak rho = 50 + 70 = 120, well above ceiling
SIGMA_IC  = 12.0

OUT = Path(__file__).parent / "results"
OUT.mkdir(exist_ok=True)


# =========================================================================
#  Core ED operators
# =========================================================================

def mobility(rho):
    return M0 * np.maximum(1.0 - rho / RHO_MAX, 0.0) ** N_MOB

def mobility_prime(rho):
    return -M0 * (N_MOB / RHO_MAX) * np.maximum(1.0 - rho / RHO_MAX, 0.0) ** (N_MOB - 1)

def penalty_sy2(rho):
    delta = rho - RHO_STAR
    return ALPHA * GAMMA * delta / np.sqrt(delta * delta + RHO_0 * RHO_0)

def compute_rhs(rho, dx):
    M  = mobility(rho)
    Mp = mobility_prime(rho)
    lap     = (np.roll(rho, 1) + np.roll(rho, -1) - 2.0 * rho) / (dx * dx)
    grad_sq = ((np.roll(rho, 1) - np.roll(rho, -1)) / (2.0 * dx)) ** 2
    return M * lap + Mp * grad_sq - penalty_sy2(rho)


# =========================================================================
#  Initial condition (horizon-activating)
# =========================================================================

def make_ic(nx, amplitude=AMP_IC, sigma=SIGMA_IC):
    x      = np.arange(nx, dtype=np.float64)
    center = nx / 2.0
    rho    = RHO_STAR + amplitude * np.exp(-0.5 * ((x - center) / sigma) ** 2)
    # clip to ceiling -- this is what creates the horizon plateau
    rho    = np.clip(rho, EPS, RHO_MAX - EPS)
    v      = np.zeros(nx, dtype=np.float64)
    return rho, v


# =========================================================================
#  Time integrator
# =========================================================================

def run_case(D, nx=NX, n_steps=N_STEPS, sample_every=SAMPLE):
    H = 1.0 - D
    rho, v = make_ic(nx)
    peak_idx = nx // 2
    dt = ETA * DX * DX / (M0 + EPS)

    # storage
    peak_hist       = []
    mean_hist       = []
    std_hist        = []
    time_hist       = []
    horizon_count   = []   # number of sites >= HORIZON_THRESH
    horizon_max_rho = []   # max rho in the field
    clips_total     = 0

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
            n_hor = int(np.sum(rho >= HORIZON_THRESH))
            horizon_count.append(n_hor)
            horizon_max_rho.append(float(np.max(rho)))

    return {
        "D": D, "H": H, "dt": dt, "n_steps": n_steps,
        "peak_hist":       peak_hist,
        "mean_hist":       mean_hist,
        "std_hist":        std_hist,
        "time_hist":       time_hist,
        "horizon_count":   horizon_count,
        "horizon_max_rho": horizon_max_rho,
        "total_clips":     clips_total,
        "final_rho_peak":  float(rho[peak_idx]),
        "final_rho_std":   float(np.std(rho)),
    }


# =========================================================================
#  Analysis
# =========================================================================

def detect_oscillations(peak_hist, rho_star=RHO_STAR):
    delta = np.array(peak_hist) - rho_star
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


def measure_undershoot(peak_hist, rho_star=RHO_STAR):
    delta = np.array(peak_hist) - rho_star
    return float(-np.min(delta)) if np.min(delta) < 0 else 0.0


def horizon_analysis(horizon_count, time_hist):
    """Detailed horizon metrics."""
    hc = np.array(horizon_count)
    active = hc > 0
    lifetime_samples = int(np.sum(active))
    max_width = int(np.max(hc)) if lifetime_samples > 0 else 0

    # Find contiguous horizon blocks
    if lifetime_samples > 0:
        active_times = np.array(time_hist)[active]
        first_active = float(active_times[0])
        last_active  = float(active_times[-1])
        duration_time = last_active - first_active
    else:
        first_active = 0.0
        last_active  = 0.0
        duration_time = 0.0

    # Check for non-monotonic collapse: does horizon width increase
    # after an initial decrease?
    non_monotonic = False
    if lifetime_samples > 2:
        # find peak width, then check if width increases after that
        peak_w_idx = int(np.argmax(hc))
        after_peak = hc[peak_w_idx:]
        for j in range(1, len(after_peak)):
            if after_peak[j] > after_peak[j - 1] and after_peak[j] > 0:
                non_monotonic = True
                break

    return {
        "lifetime_samples": lifetime_samples,
        "max_width":        max_width,
        "first_active_t":   first_active,
        "last_active_t":    last_active,
        "duration_time":    duration_time,
        "non_monotonic":    non_monotonic,
    }


def classify_regime(n_cycles):
    if n_cycles >= 3:
        return "oscillatory"
    elif n_cycles >= 1:
        return "hybrid"
    else:
        return "parabolic"


# =========================================================================
#  Plotting
# =========================================================================

def plot_time_series(result, path):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(result["time_hist"], result["peak_hist"], "k-", lw=0.8)
    ax.axhline(RHO_STAR, color="blue", ls="--", alpha=0.5, label=r"$\rho^*$")
    ax.axhline(HORIZON_THRESH, color="red", ls=":", alpha=0.5, label="Horizon threshold")
    ax.set_xlabel("Time")
    ax.set_ylabel(r"$\rho$ at peak site")
    ax.set_title(f"Peak density vs time   (D = {result['D']:.2f})")
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_horizon_lifetime(result, hor_info, path):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(result["time_hist"], result["horizon_count"], "g-", lw=0.8)
    ax.axhline(0, color="gray", ls="-", alpha=0.3)
    ax.set_xlabel("Time")
    ax.set_ylabel("Horizon sites")
    ax.set_title(f"Horizon sites vs time   (D = {result['D']:.2f},  "
                 f"lifetime = {hor_info['lifetime_samples']} samples)")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_horizon_width(result, hor_info, path):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.fill_between(result["time_hist"], result["horizon_count"],
                    alpha=0.4, color="seagreen")
    ax.plot(result["time_hist"], result["horizon_count"], "g-", lw=0.6)
    ax.set_xlabel("Time")
    ax.set_ylabel("Horizon width (sites)")
    ax.set_title(f"Horizon width vs time   (D = {result['D']:.2f},  "
                 f"max width = {hor_info['max_width']})")
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
    ax.set_title(f"Oscillation envelope   (D = {result['D']:.2f},  {n_cycles} cycles)")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_phase_flag(result, regime, n_cycles, path):
    cmap = {"oscillatory": "#2196F3", "hybrid": "#FF9800", "parabolic": "#4CAF50"}
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_axis_off()
    ax.add_patch(plt.Rectangle((0.05, 0.1), 0.9, 0.8,
                                facecolor=cmap.get(regime, "gray"),
                                edgecolor="black", lw=2, alpha=0.85))
    ax.text(0.5, 0.6, regime.upper(), ha="center", va="center",
            fontsize=28, fontweight="bold", color="white")
    ax.text(0.5, 0.35, f"D = {result['D']:.2f}   |   {n_cycles} cycles",
            ha="center", va="center", fontsize=14, color="white")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_overlay_peaks(all_results, all_analysis, path):
    fig, ax = plt.subplots(figsize=(12, 5))
    cmap = plt.cm.viridis
    n = len(all_results)
    for i, (res, ana) in enumerate(zip(all_results, all_analysis)):
        c = cmap(i / max(n - 1, 1))
        ax.plot(res["time_hist"], res["peak_hist"], color=c, lw=0.9,
                label=f"D={res['D']:.2f} ({ana['regime']}, {ana['n_cycles']}c)")
    ax.axhline(RHO_STAR, color="blue", ls="--", alpha=0.4)
    ax.axhline(HORIZON_THRESH, color="red", ls=":", alpha=0.4)
    ax.set_xlabel("Time")
    ax.set_ylabel(r"$\rho$ at peak site")
    ax.set_title("Horizon D-Sweep: Peak Density vs Time (A=70, horizon-activating)")
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_overlay_horizons(all_results, all_analysis, path):
    fig, axes = plt.subplots(2, 1, figsize=(12, 7), sharex=True)

    # Top: horizon width vs time for each D
    cmap = plt.cm.viridis
    n = len(all_results)
    for i, (res, ana) in enumerate(zip(all_results, all_analysis)):
        c = cmap(i / max(n - 1, 1))
        axes[0].plot(res["time_hist"], res["horizon_count"], color=c, lw=0.9,
                     label=f"D={res['D']:.2f}  (life={ana['horizon_lifetime']})")
    axes[0].set_ylabel("Horizon sites")
    axes[0].set_title("Horizon Width vs Time by D")
    axes[0].legend(fontsize=9)

    # Bottom: bar chart of horizon lifetime vs D
    Ds   = [a["D"] for a in all_analysis]
    hlfs = [a["horizon_lifetime"] for a in all_analysis]
    colors = [cmap(i / max(n - 1, 1)) for i in range(n)]
    axes[1].bar(range(len(Ds)), hlfs, color=colors, edgecolor="black", width=0.6)
    axes[1].set_xticks(range(len(Ds)))
    axes[1].set_xticklabels([f"{d:.2f}" for d in Ds])
    axes[1].set_xlabel("D (parabolic weight)")
    axes[1].set_ylabel("Horizon lifetime (samples)")
    axes[1].set_title("Horizon Lifetime vs D")

    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


# =========================================================================
#  Main
# =========================================================================

def main():
    print("=" * 70)
    print("ED-Phys-22: Horizon D-Sweep")
    print("=" * 70)
    print(f"Grid: {NX} sites, {N_STEPS} steps, sample every {SAMPLE}")
    print(f"Canonical: alpha={ALPHA}, gamma={GAMMA}, rho*={RHO_STAR}, rho0={RHO_0}")
    print(f"Oscillator: tau={TAU}, zeta={ZETA}")
    print(f"IC: Gaussian peak, A={AMP_IC}, sigma={SIGMA_IC}")
    print(f"   Unclipped peak = {RHO_STAR + AMP_IC:.0f} (clipped to {RHO_MAX - EPS:.1f})")
    print(f"Horizon threshold: {HORIZON_THRESH}")
    print(f"D values: {D_VALUES}")
    print("=" * 70)

    all_results  = []
    all_analysis = []

    for D in D_VALUES:
        print(f"\n-- D = {D:.2f}  (H = {1-D:.2f}) --")
        t0 = timer_mod.time()
        result = run_case(D)
        elapsed = timer_mod.time() - t0
        print(f"   Simulation: {elapsed:.1f}s,  clips={result['total_clips']}")

        # oscillation analysis
        n_cycles, amplitudes, crossings = detect_oscillations(result["peak_hist"])
        undershoot = measure_undershoot(result["peak_hist"])
        regime = classify_regime(n_cycles)

        # horizon analysis
        hor_info = horizon_analysis(result["horizon_count"], result["time_hist"])

        print(f"   Cycles: {n_cycles},  regime: {regime}")
        print(f"   Undershoot: {undershoot:.4f}")
        print(f"   Horizon lifetime: {hor_info['lifetime_samples']} samples, "
              f"max width: {hor_info['max_width']}")
        print(f"   Horizon duration: t={hor_info['first_active_t']:.1f} "
              f"to {hor_info['last_active_t']:.1f}")
        if hor_info["non_monotonic"]:
            print(f"   *** NON-MONOTONIC horizon collapse detected ***")
        if amplitudes:
            print(f"   Amp envelope: {amplitudes[0]:.4f} -> {amplitudes[-1]:.4f}")

        analysis = {
            "D":                  D,
            "H":                  1 - D,
            "n_cycles":           n_cycles,
            "regime":             regime,
            "undershoot":         undershoot,
            "horizon_lifetime":   hor_info["lifetime_samples"],
            "horizon_max_width":  hor_info["max_width"],
            "horizon_duration_t": hor_info["duration_time"],
            "horizon_first_t":    hor_info["first_active_t"],
            "horizon_last_t":     hor_info["last_active_t"],
            "horizon_non_mono":   hor_info["non_monotonic"],
            "n_crossings":        len(crossings),
            "amplitudes":         amplitudes[:20],
            "total_clips":        result["total_clips"],
            "final_std":          result["final_rho_std"],
        }

        all_results.append(result)
        all_analysis.append(analysis)

        # Per-D plots
        tag = f"D{D:.2f}".replace(".", "")
        plot_time_series(result, OUT / f"{tag}_time_series.png")
        plot_horizon_lifetime(result, hor_info, OUT / f"{tag}_horizon_lifetime.png")
        plot_horizon_width(result, hor_info, OUT / f"{tag}_horizon_width.png")
        plot_envelope(result, n_cycles, amplitudes, OUT / f"{tag}_oscillation_envelope.png")
        plot_phase_flag(result, regime, n_cycles, OUT / f"{tag}_phase_flag.png")
        print(f"   Plots saved: {tag}_*.png")

    # -- Summary plots --
    plot_overlay_peaks(all_results, all_analysis, OUT / "overlay_peak_dynamics.png")
    plot_overlay_horizons(all_results, all_analysis, OUT / "overlay_horizon_lifetimes.png")
    print("\nSummary plots saved.")

    # -- Summary table --
    print("\n" + "=" * 110)
    print(f"{'D':>6} | {'cycles':>6} | {'regime':>12} | {'under':>8} | "
          f"{'hor_life':>8} | {'max_w':>6} | {'hor_dur':>10} | "
          f"{'non_mono':>8} | {'clips':>6} | notes")
    print("-" * 110)
    for a in all_analysis:
        notes_parts = []
        if a["horizon_non_mono"]:
            notes_parts.append("NON-MONOTONIC")
        if a["total_clips"] > 0:
            notes_parts.append(f"{a['total_clips']} clips")
        notes = ", ".join(notes_parts) if notes_parts else "clean"
        print(f"{a['D']:>6.2f} | {a['n_cycles']:>6} | {a['regime']:>12} | "
              f"{a['undershoot']:>8.4f} | {a['horizon_lifetime']:>8} | "
              f"{a['horizon_max_width']:>6} | {a['horizon_duration_t']:>10.2f} | "
              f"{str(a['horizon_non_mono']):>8} | {a['total_clips']:>6} | {notes}")
    print("=" * 110)

    # -- JSON export --
    with open(OUT / "horizon_sweep_summary.json", "w") as f:
        json.dump(all_analysis, f, indent=2)
    print(f"\nJSON: {OUT / 'horizon_sweep_summary.json'}")
    print("Done.")


if __name__ == "__main__":
    main()
