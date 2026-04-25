"""
ED-Phys-25: Penalty Robustness
================================
Tests robustness of the unified ED cosmology PDE under small perturbations
to the canonical restoring penalty P_SY2(rho).

Unified PDE:
    drho/dt = D*F[rho] + H*v
    dv/dt   = (1/tau)(F[rho] - zeta*v)
    D + H = 1,  D = H = 0.50

F[rho] = M(rho)*Lap(rho) + M'(rho)*|grad(rho)|^2 - P(rho)
where P(rho) is varied across 5 penalty variants.

Penalty variants (eps = 0.05):
  0. canonical:   P_SY2(rho)
  1. steeper:     P_SY2(rho) * (1 + eps)
  2. flatter:     P_SY2(rho) * (1 - eps)
  3. asymmetric:  P_SY2(rho) * (1 + eps*sign(rho - rho*))
  4. non-smooth:  P_SY2(rho) + eps*tanh(rho - rho*)
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
EPS_NUM  = 1e-10

EPSILON  = 0.05        # perturbation magnitude

# =========================================================================
#  Grid
# =========================================================================
NX       = 256
N_STEPS  = 80_000
SAMPLE   = 40           # 2000 snapshots

D_FIXED  = 0.50
H_FIXED  = 0.50
AMP_IC   = 40.0
SIGMA_IC = 12.0

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


# =========================================================================
#  Penalty variants
# =========================================================================

def penalty_canonical(rho):
    return penalty_sy2(rho)

def penalty_steeper(rho):
    return penalty_sy2(rho) * (1.0 + EPSILON)

def penalty_flatter(rho):
    return penalty_sy2(rho) * (1.0 - EPSILON)

def penalty_asymmetric(rho):
    sign = np.sign(rho - RHO_STAR)
    return penalty_sy2(rho) * (1.0 + EPSILON * sign)

def penalty_nonsmooth(rho):
    return penalty_sy2(rho) + EPSILON * np.tanh(rho - RHO_STAR)

PENALTY_VARIANTS = [
    ("canonical",  penalty_canonical),
    ("steeper",    penalty_steeper),
    ("flatter",    penalty_flatter),
    ("asymmetric", penalty_asymmetric),
    ("nonsmooth",  penalty_nonsmooth),
]


# =========================================================================
#  RHS with pluggable penalty
# =========================================================================

def compute_rhs(rho, dx, penalty_fn):
    M  = mobility(rho)
    Mp = mobility_prime(rho)
    lap     = (np.roll(rho, 1) + np.roll(rho, -1) - 2.0 * rho) / (dx * dx)
    grad_sq = ((np.roll(rho, 1) - np.roll(rho, -1)) / (2.0 * dx)) ** 2
    return M * lap + Mp * grad_sq - penalty_fn(rho)


# =========================================================================
#  1D FFT mode tracking
# =========================================================================

def mode_amplitude_1d(rho, k, rho_star=RHO_STAR):
    delta = rho - rho_star
    N = len(delta)
    fft = np.fft.rfft(delta) / N
    amps = 2.0 * np.abs(fft)
    if k < len(amps):
        return float(amps[k])
    return 0.0


# =========================================================================
#  Initial condition
# =========================================================================

def make_ic(nx, amplitude=AMP_IC, sigma=SIGMA_IC):
    x = np.arange(nx, dtype=np.float64)
    center = nx / 2.0
    rho = RHO_STAR + amplitude * np.exp(-0.5 * ((x - center) / sigma) ** 2)
    rho = np.clip(rho, EPS_NUM, RHO_MAX - EPS_NUM)
    v = np.zeros(nx, dtype=np.float64)
    return rho, v


# =========================================================================
#  Time integrator
# =========================================================================

def run_case(penalty_name, penalty_fn, D=D_FIXED,
             nx=NX, n_steps=N_STEPS, sample_every=SAMPLE):
    H = 1.0 - D
    rho, v = make_ic(nx)
    peak_idx = nx // 2
    dt = ETA * DX * DX / (M0 + EPS_NUM)

    peak_hist    = []
    mean_hist    = []
    std_hist     = []
    time_hist    = []
    horizon_hist = []
    k3_hist      = []   # track k=3 harmonic for nonlinear coupling
    k6_hist      = []   # track k=6 (2nd harmonic of k=3)
    clips_total  = 0

    t = 0.0
    for step in range(n_steps):
        F = compute_rhs(rho, DX, penalty_fn)
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
            horizon_hist.append(int(np.sum(rho >= 0.9 * RHO_MAX)))
            k3_hist.append(mode_amplitude_1d(rho, 3))
            k6_hist.append(mode_amplitude_1d(rho, 6))

    return {
        "penalty":       penalty_name,
        "D": D, "H": H, "dt": dt, "n_steps": n_steps,
        "peak_hist":     peak_hist,
        "mean_hist":     mean_hist,
        "std_hist":      std_hist,
        "time_hist":     time_hist,
        "horizon_hist":  horizon_hist,
        "k3_hist":       k3_hist,
        "k6_hist":       k6_hist,
        "total_clips":   clips_total,
        "final_rho_peak": float(rho[peak_idx]),
        "final_rho_std":  float(np.std(rho)),
        "final_rho_mean": float(np.mean(rho)),
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

def measure_undershoot_overshoot(peak_hist, rho_star=RHO_STAR):
    delta = np.array(peak_hist) - rho_star
    undershoot = float(-np.min(delta)) if np.min(delta) < 0 else 0.0
    below_idx = np.where(delta < 0)[0]
    if len(below_idx) > 0:
        after = delta[below_idx[0]:]
        overshoot = float(np.max(after)) if np.max(after) > 0 else 0.0
    else:
        overshoot = 0.0
    return undershoot, overshoot

def relaxation_time(std_hist, time_hist, threshold_frac=0.01):
    """Time when std drops below threshold_frac of initial."""
    s = np.array(std_hist)
    if s[0] < 1e-20:
        return 0.0
    thresh = s[0] * threshold_frac
    below = np.where(s < thresh)[0]
    if len(below) > 0:
        return float(time_hist[below[0]])
    return float(time_hist[-1])  # didn't relax

def equilibrium_drift(mean_hist, rho_star=RHO_STAR):
    """Final mean - rho_star (measures if equilibrium shifted)."""
    return float(np.mean(mean_hist[-50:]) - rho_star)

def max_k3_amplitude(k3_hist):
    return float(np.max(k3_hist))


# =========================================================================
#  Plotting
# =========================================================================

def plot_time_series(result, path):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(result["time_hist"], result["peak_hist"], "k-", lw=0.8)
    ax.axhline(RHO_STAR, color="blue", ls="--", alpha=0.5, label=r"$\rho^*$")
    ax.set_xlabel("Time")
    ax.set_ylabel(r"$\rho$ at peak site")
    ax.set_title(f"Peak density vs time   ({result['penalty']})")
    ax.legend(fontsize=9)
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
    ax.set_title(f"Oscillation envelope   ({result['penalty']},  {n_cycles} cycles)")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)

def plot_harmonic(result, path):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(result["time_hist"], result["k3_hist"], "g-", lw=0.8, label="k=3")
    ax.plot(result["time_hist"], result["k6_hist"], "m--", lw=0.6, label="k=6")
    ax.set_xlabel("Time")
    ax.set_ylabel("Mode amplitude")
    ax.set_title(f"Harmonic generation   ({result['penalty']})")
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)

def plot_overlay_peaks(all_results, all_analysis, path):
    fig, ax = plt.subplots(figsize=(12, 5))
    colors = ["black", "steelblue", "coral", "seagreen", "darkviolet"]
    for i, (res, ana) in enumerate(zip(all_results, all_analysis)):
        lw = 2.0 if i == 0 else 0.9
        ls = "-" if i == 0 else "--"
        ax.plot(res["time_hist"], res["peak_hist"], color=colors[i], lw=lw,
                ls=ls, label=f"{res['penalty']} ({ana['n_cycles']}c)")
    ax.axhline(RHO_STAR, color="blue", ls=":", alpha=0.3)
    ax.set_xlabel("Time")
    ax.set_ylabel(r"$\rho$ at peak site")
    ax.set_title("Penalty Robustness: Peak Density vs Time")
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)

def plot_overlay_std(all_results, path):
    fig, ax = plt.subplots(figsize=(12, 5))
    colors = ["black", "steelblue", "coral", "seagreen", "darkviolet"]
    for i, res in enumerate(all_results):
        lw = 2.0 if i == 0 else 0.9
        ls = "-" if i == 0 else "--"
        ax.plot(res["time_hist"], res["std_hist"], color=colors[i],
                lw=lw, ls=ls, label=res["penalty"])
    ax.set_xlabel("Time")
    ax.set_ylabel(r"$\sigma(\rho)$")
    ax.set_title("Penalty Robustness: Relaxation Profile")
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)

def plot_summary_bars(all_analysis, path):
    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    names = [a["penalty"] for a in all_analysis]
    x = range(len(names))
    colors = ["black", "steelblue", "coral", "seagreen", "darkviolet"]

    # cycles
    ax = axes[0, 0]
    ax.bar(x, [a["n_cycles"] for a in all_analysis], color=colors, edgecolor="black")
    ax.set_title("Oscillation Cycles")
    ax.set_xticks(x); ax.set_xticklabels(names, rotation=30, fontsize=8)

    # undershoot
    ax = axes[0, 1]
    ax.bar(x, [a["undershoot"] for a in all_analysis], color=colors, edgecolor="black")
    ax.set_title("Undershoot Depth")
    ax.set_xticks(x); ax.set_xticklabels(names, rotation=30, fontsize=8)

    # overshoot
    ax = axes[0, 2]
    ax.bar(x, [a["overshoot"] for a in all_analysis], color=colors, edgecolor="black")
    ax.set_title("Overshoot Height")
    ax.set_xticks(x); ax.set_xticklabels(names, rotation=30, fontsize=8)

    # relaxation time
    ax = axes[1, 0]
    ax.bar(x, [a["relax_time"] for a in all_analysis], color=colors, edgecolor="black")
    ax.set_title("Relaxation Time (1% threshold)")
    ax.set_xticks(x); ax.set_xticklabels(names, rotation=30, fontsize=8)

    # equilibrium drift
    ax = axes[1, 1]
    drifts = [a["eq_drift"] for a in all_analysis]
    ax.bar(x, drifts, color=colors, edgecolor="black")
    ax.axhline(0, color="gray", ls="--", alpha=0.5)
    ax.set_title("Equilibrium Drift (mean - rho*)")
    ax.set_xticks(x); ax.set_xticklabels(names, rotation=30, fontsize=8)

    # k=3 harmonic max
    ax = axes[1, 2]
    ax.bar(x, [a["k3_max"] for a in all_analysis], color=colors, edgecolor="black")
    ax.set_title("Max k=3 Harmonic Amplitude")
    ax.set_xticks(x); ax.set_xticklabels(names, rotation=30, fontsize=8)

    fig.suptitle("Penalty Robustness: Summary Comparison", fontsize=14)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)

def plot_penalty_curves(path):
    """Plot the 5 penalty functions."""
    rho = np.linspace(30, 70, 500)
    fig, ax = plt.subplots(figsize=(10, 5))
    colors = ["black", "steelblue", "coral", "seagreen", "darkviolet"]
    for (name, fn), c in zip(PENALTY_VARIANTS, colors):
        lw = 2.0 if name == "canonical" else 1.0
        ax.plot(rho, fn(rho), color=c, lw=lw, label=name)
    ax.axhline(0, color="gray", ls="--", alpha=0.3)
    ax.axvline(RHO_STAR, color="gray", ls=":", alpha=0.3)
    ax.set_xlabel(r"$\rho$")
    ax.set_ylabel(r"$P(\rho)$")
    ax.set_title(f"Penalty Variants (eps={EPSILON})")
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


# =========================================================================
#  D-sweep for oscillation-death boundary shift
# =========================================================================

def run_d_sweep(penalty_fn, penalty_name, D_values, n_steps=40_000):
    """Quick sweep to find oscillation-death boundary."""
    results = []
    dt = ETA * DX * DX / (M0 + EPS_NUM)
    for D in D_values:
        H = 1.0 - D
        rho, v = make_ic(NX)
        peak_idx = NX // 2
        peak_hist = []
        t = 0.0
        for step in range(n_steps):
            F = compute_rhs(rho, DX, penalty_fn)
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


# =========================================================================
#  Main
# =========================================================================

def main():
    print("=" * 70)
    print("ED-Phys-25: Penalty Robustness")
    print("=" * 70)
    print(f"Grid: {NX} sites, {N_STEPS} steps, sample every {SAMPLE}")
    print(f"Hybrid: D={D_FIXED}, H={H_FIXED}")
    print(f"IC: Gaussian peak A={AMP_IC}, sigma={SIGMA_IC}")
    print(f"Perturbation eps={EPSILON}")
    print(f"Variants: {[name for name, _ in PENALTY_VARIANTS]}")
    print("=" * 70)

    # Plot penalty curves
    plot_penalty_curves(OUT / "penalty_curves.png")
    print("Penalty curves plotted.")

    all_results  = []
    all_analysis = []

    for name, fn in PENALTY_VARIANTS:
        print(f"\n-- Penalty: {name} --")
        t0 = timer_mod.time()
        result = run_case(name, fn)
        elapsed = timer_mod.time() - t0
        print(f"   Simulation: {elapsed:.1f}s, clips={result['total_clips']}")

        n_cycles, amplitudes, crossings = detect_oscillations(result["peak_hist"])
        undershoot, overshoot = measure_undershoot_overshoot(result["peak_hist"])
        relax_t = relaxation_time(result["std_hist"], result["time_hist"])
        eq_drift = equilibrium_drift(result["mean_hist"])
        k3_max = max_k3_amplitude(result["k3_hist"])
        hor_life = int(np.sum(np.array(result["horizon_hist"]) > 0))

        print(f"   Cycles: {n_cycles}")
        print(f"   Undershoot: {undershoot:.4f}, Overshoot: {overshoot:.4f}")
        print(f"   Relax time (1%): {relax_t:.1f}")
        print(f"   Eq drift: {eq_drift:.6f}")
        print(f"   k=3 max: {k3_max:.6f}")
        print(f"   Horizon life: {hor_life}")

        analysis = {
            "penalty":       name,
            "n_cycles":      n_cycles,
            "undershoot":    undershoot,
            "overshoot":     overshoot,
            "relax_time":    relax_t,
            "eq_drift":      eq_drift,
            "k3_max":        k3_max,
            "horizon_life":  hor_life,
            "total_clips":   result["total_clips"],
            "final_std":     result["final_rho_std"],
            "amplitudes":    amplitudes[:10],
        }

        all_results.append(result)
        all_analysis.append(analysis)

        # per-variant plots
        plot_time_series(result, OUT / f"{name}_time_series.png")
        plot_envelope(result, n_cycles, amplitudes, OUT / f"{name}_oscillation_envelope.png")
        plot_harmonic(result, OUT / f"{name}_harmonic.png")
        print(f"   Plots saved: {name}_*.png")

    # -- Summary plots --
    plot_overlay_peaks(all_results, all_analysis, OUT / "overlay_peaks.png")
    plot_overlay_std(all_results, OUT / "overlay_relaxation.png")
    plot_summary_bars(all_analysis, OUT / "summary_bars.png")
    print("\nSummary plots saved.")

    # -- D-sweep for boundary shift --
    print("\n== D-sweep for oscillation-death boundary ==")
    D_test = [0.40, 0.42, 0.44, 0.45, 0.46, 0.48, 0.50, 0.52, 0.55]
    boundary_results = {}
    for name, fn in PENALTY_VARIANTS:
        print(f"   {name}: ", end="", flush=True)
        dsweep = run_d_sweep(fn, name, D_test)
        boundary_results[name] = dsweep
        for r in dsweep:
            print(f"D={r['D']:.2f}:{r['n_cycles']}c ", end="")
        print()

    # Find D_crit for each variant (last D with >= 2 cycles)
    print("\n   D_crit (last D with >= 2 cycles):")
    d_crits = {}
    for name, dsweep in boundary_results.items():
        d_crit = 0.0
        for r in dsweep:
            if r["n_cycles"] >= 2:
                d_crit = r["D"]
        d_crits[name] = d_crit
        print(f"      {name}: D_crit = {d_crit:.2f}")

    # Plot boundary comparison
    fig, ax = plt.subplots(figsize=(10, 5))
    colors = ["black", "steelblue", "coral", "seagreen", "darkviolet"]
    for i, (name, dsweep) in enumerate(boundary_results.items()):
        Ds = [r["D"] for r in dsweep]
        cyc = [r["n_cycles"] for r in dsweep]
        lw = 2.5 if name == "canonical" else 1.2
        ax.plot(Ds, cyc, "o-", color=colors[i], lw=lw, ms=4, label=name)
    ax.set_xlabel("D (parabolic weight)")
    ax.set_ylabel("Oscillation cycles")
    ax.set_title("Oscillation-Death Boundary by Penalty Variant")
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(OUT / "boundary_comparison.png", dpi=150)
    plt.close(fig)
    print("   Boundary comparison plotted.")

    # -- Summary table --
    print("\n" + "=" * 110)
    print(f"{'penalty':>12} | {'cycles':>6} | {'under':>8} | {'over':>8} | "
          f"{'relax_t':>8} | {'eq_drift':>10} | {'k3_max':>8} | "
          f"{'hor_life':>8} | {'D_crit':>6} | {'clips':>6}")
    print("-" * 110)
    for a in all_analysis:
        dc = d_crits.get(a["penalty"], 0.0)
        print(f"{a['penalty']:>12} | {a['n_cycles']:>6} | {a['undershoot']:>8.4f} | "
              f"{a['overshoot']:>8.4f} | {a['relax_time']:>8.1f} | "
              f"{a['eq_drift']:>10.6f} | {a['k3_max']:>8.6f} | "
              f"{a['horizon_life']:>8} | {dc:>6.2f} | {a['total_clips']:>6}")
    print("=" * 110)

    # -- JSON --
    export = {
        "analysis": all_analysis,
        "d_crits": d_crits,
        "boundary_sweep": {k: v for k, v in boundary_results.items()},
    }
    with open(OUT / "penalty_robustness_summary.json", "w") as f:
        json.dump(export, f, indent=2)
    print(f"\nJSON: {OUT / 'penalty_robustness_summary.json'}")
    print("Done.")


if __name__ == "__main__":
    main()
