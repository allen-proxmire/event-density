#!/usr/bin/env python3
"""
ED-Phys-31: Parameter Geometry
================================
Maps how the stable manifold of the unified ED cosmology PDE deforms
across the parameter space (D, tau, zeta, A).

Unified PDE (1D):
    drho/dt = D*F[rho] + H*v
    dv/dt   = (1/tau)(F[rho] - zeta*v)
    D + H = 1

Parameter sweep:
    D     in {0.0, 0.25, 0.50, 0.75, 1.0}
    tau   in {0.5, 1.0, 2.0}
    zeta  in {0.25, 0.50, 1.00}
    A     in {10, 20, 40}
    Total: 5 x 3 x 3 x 3 = 135 runs
"""

import json
import itertools
import numpy as np
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# -- Fixed canonical parameters ----------------------------------------
ALPHA   = 0.1
GAMMA   = 0.5
M0      = 1.0
RHO_MAX = 100.0
N_MOB   = 2
RHO_STAR = 50.0
RHO_0   = 0.5
DX      = 1.0
ETA     = 0.2
EPS_NUM = 1e-10

# -- Simulation --------------------------------------------------------
NX      = 256
N_STEPS = 60_000
SAMPLE  = 40
SIGMA_IC = 8.0

# -- Sweep ranges ------------------------------------------------------
D_VALUES   = [0.0, 0.25, 0.50, 0.75, 1.0]
TAU_VALUES = [0.5, 1.0, 2.0]
ZETA_VALUES = [0.25, 0.50, 1.00]
A_VALUES   = [10, 20, 40]

# -- Output ------------------------------------------------------------
OUT = Path(__file__).parent / "results"
OUT.mkdir(exist_ok=True)
MAX_W_IN = 1000 / 150
MAX_H_IN = 800 / 150


# ======================================================================
# Core physics
# ======================================================================

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


# ======================================================================
# IC and integration
# ======================================================================

def make_ic(nx, A):
    x = np.arange(nx, dtype=np.float64)
    center = nx / 2.0
    rho = RHO_STAR + A * np.exp(-((x - center) / SIGMA_IC) ** 2)
    rho = np.clip(rho, EPS_NUM, RHO_MAX - EPS_NUM)
    v = np.zeros(nx, dtype=np.float64)
    return rho, v


def run_case(D, tau, zeta, A):
    H = 1.0 - D
    rho, v = make_ic(NX, A)
    peak_idx = NX // 2
    dt = ETA * DX * DX / (M0 + EPS_NUM)

    rhopeak_hist = []
    vpeak_hist   = []
    std_hist     = []
    time_hist    = []
    dist_hist    = []

    t = 0.0
    for step in range(N_STEPS):
        F_val = compute_F(rho, DX)
        rho_new = rho + dt * (D * F_val + H * v)
        v_new   = v   + dt * (1.0 / tau) * (F_val - zeta * v)
        rho_new = np.clip(rho_new, EPS_NUM, RHO_MAX - EPS_NUM)
        rho = rho_new
        v   = v_new
        t  += dt

        if step % SAMPLE == 0:
            rp = float(rho[peak_idx])
            vp = float(v[peak_idx])
            rhopeak_hist.append(rp)
            vpeak_hist.append(vp)
            std_hist.append(float(np.std(rho)))
            time_hist.append(t)
            dist_hist.append(np.sqrt((rp - RHO_STAR)**2 + vp**2))

    return {
        "rhopeak_hist": rhopeak_hist,
        "vpeak_hist": vpeak_hist,
        "std_hist": std_hist,
        "time_hist": time_hist,
        "dist_hist": dist_hist,
    }


# ======================================================================
# Analysis
# ======================================================================

def fit_convergence_rate(dist_hist, time_hist):
    d = np.array(dist_hist)
    t = np.array(time_hist)
    mask = d > 1e-10
    if np.sum(mask) < 10:
        return 0.0
    log_d = np.log(d[mask])
    t_m = t[mask]
    n = max(len(log_d) // 2, 10)
    if n < 2:
        return 0.0
    coeffs = np.polyfit(t_m[:n], log_d[:n], 1)
    return float(-coeffs[0])


def count_oscillations(rhopeak_hist):
    delta = np.array(rhopeak_hist) - RHO_STAR
    crossings = 0
    for i in range(1, len(delta)):
        if delta[i - 1] * delta[i] < 0:
            crossings += 1
    return crossings // 2


def measure_extremes(rhopeak_hist):
    delta = np.array(rhopeak_hist) - RHO_STAR
    undershoot = float(-np.min(delta)) if np.min(delta) < 0 else 0.0
    below_idx = np.where(delta < 0)[0]
    if len(below_idx) > 0:
        after = delta[below_idx[0]:]
        overshoot = float(np.max(after)) if np.max(after) > 0 else 0.0
    else:
        overshoot = 0.0
    return undershoot, overshoot


def manifold_curvature(rhopeak_hist, vpeak_hist):
    rp = np.array(rhopeak_hist)
    vp = np.array(vpeak_hist)
    n = len(rp)
    start = 2 * n // 3
    dr = rp[start:] - RHO_STAR
    vs = vp[start:]
    mask = np.abs(dr) > 1e-8
    if np.sum(mask) < 5:
        return 0.0
    dr = dr[mask]
    vs = vs[mask]
    try:
        coeffs = np.polyfit(dr, vs, 2)
        return float(2.0 * coeffs[0])
    except (np.linalg.LinAlgError, ValueError):
        return 0.0


def analyze(result):
    lam = fit_convergence_rate(result["dist_hist"], result["time_hist"])
    n_cyc = count_oscillations(result["rhopeak_hist"])
    undershoot, overshoot = measure_extremes(result["rhopeak_hist"])
    peak_v = float(np.max(np.abs(result["vpeak_hist"])))
    curv = manifold_curvature(result["rhopeak_hist"], result["vpeak_hist"])
    return {
        "convergence_rate": lam,
        "n_cycles": n_cyc,
        "undershoot": undershoot,
        "overshoot": overshoot,
        "peak_v": peak_v,
        "curvature": curv,
    }


# ======================================================================
# Plotting
# ======================================================================

def plot_lambda_vs_D(records, path):
    """Convergence rate vs D, one curve per (tau, zeta), averaged over A."""
    fig, ax = plt.subplots(figsize=(MAX_W_IN, MAX_H_IN))
    styles = [("-", "o"), ("--", "s"), ("-.", "^")]
    colors = ["royalblue", "seagreen", "firebrick"]

    for i, tau in enumerate(TAU_VALUES):
        for j, zeta in enumerate(ZETA_VALUES):
            d_vals = []
            lam_vals = []
            for D in D_VALUES:
                subset = [r for r in records
                          if r["D"] == D and r["tau"] == tau and r["zeta"] == zeta]
                if subset:
                    mean_lam = np.mean([r["convergence_rate"] for r in subset])
                    d_vals.append(D)
                    lam_vals.append(mean_lam)
            ls, mk = styles[j]
            ax.plot(d_vals, lam_vals, color=colors[i], ls=ls, marker=mk,
                    ms=5, lw=1.2, alpha=0.8,
                    label=f"tau={tau}, zeta={zeta}")

    ax.set_xlabel("D (parabolic weight)", fontsize=10)
    ax.set_ylabel("Convergence rate (lambda)", fontsize=10)
    ax.set_title("Convergence rate vs D", fontsize=11)
    ax.legend(fontsize=6, ncol=3, loc="upper center")
    ax.grid(True, alpha=0.15)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_cycles_vs_D(records, path):
    """Oscillation count vs D, one curve per (tau, zeta), averaged over A."""
    fig, ax = plt.subplots(figsize=(MAX_W_IN, MAX_H_IN))
    styles = [("-", "o"), ("--", "s"), ("-.", "^")]
    colors = ["royalblue", "seagreen", "firebrick"]

    for i, tau in enumerate(TAU_VALUES):
        for j, zeta in enumerate(ZETA_VALUES):
            d_vals = []
            cyc_vals = []
            for D in D_VALUES:
                subset = [r for r in records
                          if r["D"] == D and r["tau"] == tau and r["zeta"] == zeta]
                if subset:
                    mean_c = np.mean([r["n_cycles"] for r in subset])
                    d_vals.append(D)
                    cyc_vals.append(mean_c)
            ls, mk = styles[j]
            ax.plot(d_vals, cyc_vals, color=colors[i], ls=ls, marker=mk,
                    ms=5, lw=1.2, alpha=0.8,
                    label=f"tau={tau}, zeta={zeta}")

    ax.set_xlabel("D", fontsize=10)
    ax.set_ylabel("Oscillation cycles (avg over A)", fontsize=10)
    ax.set_title("Oscillation count vs D", fontsize=11)
    ax.legend(fontsize=6, ncol=3, loc="upper right")
    ax.grid(True, alpha=0.15)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_peak_v_heatmap(records, path):
    """Heatmap of peak|v| in (D, tau) plane, averaged over zeta and A."""
    fig, ax = plt.subplots(figsize=(MAX_W_IN, MAX_H_IN))
    grid = np.zeros((len(TAU_VALUES), len(D_VALUES)))
    for i, tau in enumerate(TAU_VALUES):
        for j, D in enumerate(D_VALUES):
            subset = [r for r in records if r["D"] == D and r["tau"] == tau]
            if subset:
                grid[i, j] = np.mean([r["peak_v"] for r in subset])

    im = ax.imshow(grid, aspect="auto", origin="lower",
                   extent=[-0.125, 1.125, -0.5, len(TAU_VALUES) - 0.5],
                   cmap="inferno")
    ax.set_xticks(D_VALUES)
    ax.set_yticks(range(len(TAU_VALUES)))
    ax.set_yticklabels([str(t) for t in TAU_VALUES])
    ax.set_xlabel("D", fontsize=10)
    ax.set_ylabel("tau", fontsize=10)
    ax.set_title("Peak |v| (avg over zeta, A)", fontsize=11)
    fig.colorbar(im, ax=ax, label="Peak |v|")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_undershoot_heatmap(records, path):
    """Heatmap of undershoot in (D, zeta) plane, averaged over tau and A."""
    fig, ax = plt.subplots(figsize=(MAX_W_IN, MAX_H_IN))
    grid = np.zeros((len(ZETA_VALUES), len(D_VALUES)))
    for i, zeta in enumerate(ZETA_VALUES):
        for j, D in enumerate(D_VALUES):
            subset = [r for r in records if r["D"] == D and r["zeta"] == zeta]
            if subset:
                grid[i, j] = np.mean([r["undershoot"] for r in subset])

    im = ax.imshow(grid, aspect="auto", origin="lower",
                   extent=[-0.125, 1.125, -0.5, len(ZETA_VALUES) - 0.5],
                   cmap="YlOrRd")
    ax.set_xticks(D_VALUES)
    ax.set_yticks(range(len(ZETA_VALUES)))
    ax.set_yticklabels([str(z) for z in ZETA_VALUES])
    ax.set_xlabel("D", fontsize=10)
    ax.set_ylabel("zeta", fontsize=10)
    ax.set_title("Undershoot depth (avg over tau, A)", fontsize=11)
    fig.colorbar(im, ax=ax, label="Undershoot")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_manifold_deformation(records, path):
    """Phase portraits (rho_peak, v_peak) for select parameter combos."""
    fig, axes = plt.subplots(2, 3, figsize=(MAX_W_IN, MAX_H_IN))
    # Show D sweep at fixed tau=1.0, zeta=0.5, A=20
    combos = [(D, 1.0, 0.5, 20) for D in D_VALUES]

    for idx, (D, tau, zeta, A) in enumerate(combos):
        row, col = divmod(idx, 3)
        ax = axes[row, col]
        match = [r for r in records
                 if r["D"] == D and r["tau"] == tau
                 and r["zeta"] == zeta and r["A"] == A]
        if match:
            r = match[0]
            rp = np.array(r["rhopeak_hist"])
            vp = np.array(r["vpeak_hist"])
            ax.plot(rp, vp, "k-", lw=0.5, alpha=0.7)
            ax.plot(rp[0], vp[0], "go", ms=5)
            ax.plot(RHO_STAR, 0.0, "r+", ms=8, mew=2)
        ax.set_title(f"D={D}", fontsize=9)
        ax.tick_params(labelsize=7)
        if col == 0:
            ax.set_ylabel(r"$v_{\rm peak}$", fontsize=8)
        if row == 1:
            ax.set_xlabel(r"$\rho_{\rm peak}$", fontsize=8)

    # Hide unused subplot
    axes[1, 2].set_visible(False)
    fig.suptitle("Manifold deformation across D (tau=1, zeta=0.5, A=20)",
                 fontsize=10, y=1.01)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_tau_zeta_sensitivity(records, path):
    """3x3 grid: tau vs zeta, each cell shows lambda bar for D=0.5, avg over A."""
    fig, axes = plt.subplots(3, 3, figsize=(MAX_W_IN, MAX_H_IN))

    for i, tau in enumerate(TAU_VALUES):
        for j, zeta in enumerate(ZETA_VALUES):
            ax = axes[i, j]
            a_lams = []
            for A in A_VALUES:
                match = [r for r in records
                         if r["D"] == 0.5 and r["tau"] == tau
                         and r["zeta"] == zeta and r["A"] == A]
                if match:
                    a_lams.append((A, match[0]["convergence_rate"]))
            if a_lams:
                aa, ll = zip(*a_lams)
                ax.bar([str(a) for a in aa], ll, color="steelblue")
            ax.set_title(f"tau={tau}, z={zeta}", fontsize=7)
            ax.tick_params(labelsize=6)
            if i == 2:
                ax.set_xlabel("A", fontsize=7)
            if j == 0:
                ax.set_ylabel("lambda", fontsize=7)

    fig.suptitle("Convergence rate: tau x zeta grid (D=0.5)", fontsize=10, y=1.01)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


# ======================================================================
# Main
# ======================================================================

def main():
    print("=" * 70)
    print("ED-Phys-31: Parameter Geometry")
    print("=" * 70)

    sweep = list(itertools.product(D_VALUES, TAU_VALUES, ZETA_VALUES, A_VALUES))
    total = len(sweep)
    print(f"Parameter combinations: {total}")
    print(f"D: {D_VALUES}")
    print(f"tau: {TAU_VALUES}   zeta: {ZETA_VALUES}   A: {A_VALUES}")
    print(f"Grid: {NX} sites, {N_STEPS} steps")
    print("=" * 70)

    records = []

    for idx, (D, tau, zeta, A) in enumerate(sweep):
        result = run_case(D, tau, zeta, A)
        ana = analyze(result)

        rec = {
            "D": D, "tau": tau, "zeta": zeta, "A": A,
            **ana,
            "rhopeak_hist": result["rhopeak_hist"],
            "vpeak_hist": result["vpeak_hist"],
        }
        records.append(rec)

        if (idx + 1) % 15 == 0 or idx == 0 or idx == total - 1:
            print(f"  [{idx+1:3d}/{total}] D={D:.2f} tau={tau:.1f} "
                  f"zeta={zeta:.2f} A={A:2d}  "
                  f"lam={ana['convergence_rate']:.5f}  "
                  f"cyc={ana['n_cycles']}  "
                  f"under={ana['undershoot']:.3f}  "
                  f"peakv={ana['peak_v']:.5f}")

    # -- Plots ---------------------------------------------------------
    print("\n>>> Generating plots...")
    # Strip heavy history from export records
    export_records = [{k: v for k, v in r.items()
                       if k not in ("rhopeak_hist", "vpeak_hist")}
                      for r in records]

    plot_lambda_vs_D(records, OUT / "lambda_vs_D.png")
    plot_cycles_vs_D(records, OUT / "cycles_vs_D.png")
    plot_peak_v_heatmap(records, OUT / "peak_v_heatmap.png")
    plot_undershoot_heatmap(records, OUT / "undershoot_heatmap.png")
    plot_manifold_deformation(records, OUT / "manifold_deformation.png")
    plot_tau_zeta_sensitivity(records, OUT / "tau_zeta_sensitivity.png")

    # -- Aggregate stats -----------------------------------------------
    # Per-D statistics (averaged over tau, zeta, A)
    per_D = {}
    for D in D_VALUES:
        sub = [r for r in export_records if r["D"] == D]
        per_D[str(D)] = {
            "mean_lambda": float(np.mean([r["convergence_rate"] for r in sub])),
            "mean_cycles": float(np.mean([r["n_cycles"] for r in sub])),
            "mean_undershoot": float(np.mean([r["undershoot"] for r in sub])),
            "mean_peak_v": float(np.mean([r["peak_v"] for r in sub])),
        }

    # Per-tau
    per_tau = {}
    for tau in TAU_VALUES:
        sub = [r for r in export_records if r["tau"] == tau]
        per_tau[str(tau)] = {
            "mean_lambda": float(np.mean([r["convergence_rate"] for r in sub])),
            "mean_cycles": float(np.mean([r["n_cycles"] for r in sub])),
            "mean_peak_v": float(np.mean([r["peak_v"] for r in sub])),
        }

    # Per-zeta
    per_zeta = {}
    for zeta in ZETA_VALUES:
        sub = [r for r in export_records if r["zeta"] == zeta]
        per_zeta[str(zeta)] = {
            "mean_lambda": float(np.mean([r["convergence_rate"] for r in sub])),
            "mean_cycles": float(np.mean([r["n_cycles"] for r in sub])),
            "mean_undershoot": float(np.mean([r["undershoot"] for r in sub])),
        }

    export = {
        "experiment": "ED-Phys-31_ParameterGeometry",
        "parameters": {
            "NX": NX, "N_STEPS": N_STEPS, "SAMPLE": SAMPLE,
            "SIGMA_IC": SIGMA_IC, "RHO_STAR": RHO_STAR,
            "D_VALUES": D_VALUES, "TAU_VALUES": TAU_VALUES,
            "ZETA_VALUES": ZETA_VALUES, "A_VALUES": A_VALUES,
        },
        "total_runs": total,
        "per_D": per_D,
        "per_tau": per_tau,
        "per_zeta": per_zeta,
        "all_records": export_records,
    }

    json_path = OUT / "parameter_geometry_summary.json"
    with open(json_path, "w") as f:
        json.dump(export, f, indent=2)
    print(f">>> Summary written to {json_path}")

    # -- Print summary -------------------------------------------------
    print("\n" + "=" * 70)
    print("PARAMETER GEOMETRY SUMMARY")
    print("=" * 70)

    print("\nPer-D averages:")
    print(f"  {'D':>5s}  {'lambda':>10s}  {'cycles':>8s}  {'undershoot':>10s}  {'peak_v':>10s}")
    for D in D_VALUES:
        s = per_D[str(D)]
        print(f"  {D:>5.2f}  {s['mean_lambda']:>10.5f}  {s['mean_cycles']:>8.1f}  "
              f"{s['mean_undershoot']:>10.3f}  {s['mean_peak_v']:>10.5f}")

    print("\nPer-tau averages:")
    for tau in TAU_VALUES:
        s = per_tau[str(tau)]
        print(f"  tau={tau}: lambda={s['mean_lambda']:.5f}  "
              f"cycles={s['mean_cycles']:.1f}  peak_v={s['mean_peak_v']:.5f}")

    print("\nPer-zeta averages:")
    for zeta in ZETA_VALUES:
        s = per_zeta[str(zeta)]
        print(f"  zeta={zeta}: lambda={s['mean_lambda']:.5f}  "
              f"cycles={s['mean_cycles']:.1f}  undershoot={s['mean_undershoot']:.3f}")

    print("\n" + "=" * 70)
    print(">>> Done. All outputs in:", OUT)


if __name__ == "__main__":
    main()
