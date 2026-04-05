#!/usr/bin/env python3
"""
ED-Phys-30: Stability Manifold
================================
Reconstructs the stable manifold of the unified ED cosmology PDE around
the global attractor (rho*, 0). Determines manifold geometry, curvature,
dimensionality, and approach direction from different initial conditions.

Unified PDE (1D):
    drho/dt = D*F[rho] + H*v
    dv/dt   = (1/tau)(F[rho] - zeta*v)
    D + H = 1

Canonical operator:
    F[rho] = M(rho) lap(rho) + M'(rho)|grad(rho)|^2 - P_SY2(rho)

Manifold probes:
    Pure density (6), pure velocity (3), mixed (6),
    orthogonal (1) = 16 ICs x 3 cosmologies = 48 runs.
"""

import json
import numpy as np
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# -- Canonical ED parameters -------------------------------------------
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

# -- Simulation --------------------------------------------------------
NX       = 256
N_STEPS  = 80_000
SAMPLE   = 20          # finer sampling for manifold reconstruction

# -- Output ------------------------------------------------------------
OUT = Path(__file__).parent / "results"
OUT.mkdir(exist_ok=True)

MAX_W_IN = 1000 / 150
MAX_H_IN = 800 / 150

# -- Cosmologies -------------------------------------------------------
COSMOLOGIES = [
    ("oscillatory", 0.0, 1.0),
    ("hybrid",      0.5, 0.5),
    ("parabolic",   1.0, 0.0),
]


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
# Initial condition library
# ======================================================================

def build_ic_set(nx):
    """Build the 16 manifold-probe ICs. Returns list of (rho, v, label, category)."""
    ics = []
    center = nx / 2.0
    x = np.arange(nx, dtype=np.float64)

    # 1. Pure density perturbations: A x L
    for A in [10, 20, 40]:
        for L in [4, 8]:
            rho = RHO_STAR + A * np.exp(-((x - center) / L) ** 2)
            rho = np.clip(rho, EPS_NUM, RHO_MAX - EPS_NUM)
            v = np.zeros(nx, dtype=np.float64)
            ics.append((rho.copy(), v.copy(), f"drho_A{A}_L{L}", "pure_density"))

    # 2. Pure velocity perturbations
    for B in [0.1, 0.5, 1.0]:
        rho = np.full(nx, RHO_STAR, dtype=np.float64)
        v = B * np.exp(-((x - center) / 8.0) ** 2)
        ics.append((rho.copy(), v.copy(), f"dv_B{B}", "pure_velocity"))

    # 3. Mixed perturbations: (A, B) x k
    for A, B in [(10, 0.1), (20, 0.5), (40, 1.0)]:
        for k in [4, 8]:
            kx = 2.0 * np.pi * k / nx
            rho = RHO_STAR + A * np.sin(kx * x)
            rho = np.clip(rho, EPS_NUM, RHO_MAX - EPS_NUM)
            v = B * np.sin(kx * x)
            ics.append((rho.copy(), v.copy(), f"mix_A{A}B{B}_k{k}", "mixed"))

    # 4. Orthogonal perturbation
    kx4 = 2.0 * np.pi * 4 / nx
    kx7 = 2.0 * np.pi * 7 / nx
    rho = RHO_STAR + 10.0 * np.sin(kx4 * x)
    rho = np.clip(rho, EPS_NUM, RHO_MAX - EPS_NUM)
    v = 0.5 * np.sin(kx7 * x)
    ics.append((rho.copy(), v.copy(), "ortho_k4k7", "orthogonal"))

    return ics


# ======================================================================
# PDE integration
# ======================================================================

def run_case(rho_init, v_init, ic_label, category, cosmo_name, D,
             nx=NX, n_steps=N_STEPS, sample_every=SAMPLE):
    H = 1.0 - D
    rho = rho_init.copy()
    v = v_init.copy()
    peak_idx = nx // 2
    dt = ETA * DX * DX / (M0 + EPS_NUM)

    rhopeak_hist = []
    vpeak_hist   = []
    std_hist     = []
    time_hist    = []
    dist_hist    = []

    t = 0.0
    for step in range(n_steps):
        F = compute_F(rho, DX)
        rho_new = rho + dt * (D * F + H * v)
        v_new   = v   + dt * (1.0 / TAU) * (F - ZETA * v)
        rho_new = np.clip(rho_new, EPS_NUM, RHO_MAX - EPS_NUM)
        rho = rho_new
        v   = v_new
        t  += dt

        if step % sample_every == 0:
            rp = float(rho[peak_idx])
            vp = float(v[peak_idx])
            rhopeak_hist.append(rp)
            vpeak_hist.append(vp)
            std_hist.append(float(np.std(rho)))
            time_hist.append(t)
            d = np.sqrt((rp - RHO_STAR)**2 + vp**2)
            dist_hist.append(d)

    return {
        "ic_label": ic_label,
        "category": category,
        "cosmo": cosmo_name,
        "D": D,
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
    """Fit log(d) ~ -lambda*t over the first half where d > floor."""
    d = np.array(dist_hist)
    t = np.array(time_hist)
    mask = d > 1e-10
    if np.sum(mask) < 10:
        return 0.0
    log_d = np.log(d[mask])
    t_m = t[mask]
    n = max(len(log_d) // 2, 10)
    log_d = log_d[:n]
    t_m = t_m[:n]
    if len(t_m) < 2:
        return 0.0
    coeffs = np.polyfit(t_m, log_d, 1)
    return float(-coeffs[0])


def detect_oscillatory_approach(rhopeak_hist):
    """Check whether the approach to rho* is oscillatory (sign changes in delta)."""
    delta = np.array(rhopeak_hist) - RHO_STAR
    crossings = 0
    for i in range(1, len(delta)):
        if delta[i - 1] * delta[i] < 0:
            crossings += 1
    return crossings > 1, crossings


def classify_approach_direction(rhopeak_hist, vpeak_hist):
    """Determine whether approach is along density axis, velocity axis, or mixed.
    Look at the initial displacement direction."""
    drho0 = abs(rhopeak_hist[0] - RHO_STAR)
    dv0 = abs(vpeak_hist[0])
    total = drho0 + dv0 + 1e-20
    rho_frac = drho0 / total
    if rho_frac > 0.9:
        return "density"
    elif rho_frac < 0.1:
        return "velocity"
    else:
        return "mixed"


def estimate_manifold_curvature(rhopeak_hist, vpeak_hist):
    """Estimate curvature of the (rho, v) trajectory near equilibrium.
    Use the last 1/3 of the trajectory and fit a quadratic."""
    rp = np.array(rhopeak_hist)
    vp = np.array(vpeak_hist)
    n = len(rp)
    start = 2 * n // 3  # last third
    rp_seg = rp[start:]
    vp_seg = vp[start:]

    # Remove points too close to equilibrium (noise)
    dr = rp_seg - RHO_STAR
    mask = np.abs(dr) > 1e-8
    if np.sum(mask) < 5:
        return 0.0
    dr = dr[mask]
    vp_seg = vp_seg[mask]

    if len(dr) < 3:
        return 0.0

    # Fit v = a*dr^2 + b*dr + c, curvature ~ 2a
    try:
        coeffs = np.polyfit(dr, vp_seg, 2)
        return float(2.0 * coeffs[0])  # curvature = 2a
    except (np.linalg.LinAlgError, ValueError):
        return 0.0


def check_manifold_collapse(all_results_cosmo):
    """Check if all trajectories collapse onto a single curve in (rho, v) space.
    Measure spread of v at fixed rho bins."""
    # Collect all (rho_peak - rho*, v_peak) points
    all_dr = []
    all_vp = []
    for r in all_results_cosmo:
        dr = np.array(r["rhopeak_hist"]) - RHO_STAR
        vp = np.array(r["vpeak_hist"])
        all_dr.extend(dr.tolist())
        all_vp.extend(vp.tolist())

    all_dr = np.array(all_dr)
    all_vp = np.array(all_vp)

    # Bin by |dr| and check v-spread in each bin
    bins = np.linspace(-30, 30, 31)
    spreads = []
    for i in range(len(bins) - 1):
        mask = (all_dr >= bins[i]) & (all_dr < bins[i + 1])
        if np.sum(mask) > 5:
            spreads.append(float(np.std(all_vp[mask])))

    if not spreads:
        return 1, 0.0  # trivially collapsed
    mean_spread = float(np.mean(spreads))
    # If mean spread is small relative to max |v|, it's 1D
    max_v = float(np.max(np.abs(all_vp))) + 1e-20
    if mean_spread / max_v < 0.3:
        return 1, mean_spread
    else:
        return 2, mean_spread


def analyze_result(result):
    lam = fit_convergence_rate(result["dist_hist"], result["time_hist"])
    is_osc, n_crossings = detect_oscillatory_approach(result["rhopeak_hist"])
    approach = classify_approach_direction(result["rhopeak_hist"], result["vpeak_hist"])
    curvature = estimate_manifold_curvature(result["rhopeak_hist"], result["vpeak_hist"])

    return {
        "ic_label": result["ic_label"],
        "category": result["category"],
        "cosmo": result["cosmo"],
        "D": result["D"],
        "convergence_rate": lam,
        "oscillatory_approach": is_osc,
        "n_crossings": n_crossings,
        "approach_direction": approach,
        "curvature": curvature,
        "final_dist": result["dist_hist"][-1],
    }


# ======================================================================
# Plotting
# ======================================================================

CAT_STYLES = {
    "pure_density":  {"color": "royalblue",  "ls": "-"},
    "pure_velocity": {"color": "firebrick",  "ls": "--"},
    "mixed":         {"color": "seagreen",   "ls": "-."},
    "orthogonal":    {"color": "darkorange", "ls": ":"},
}


def plot_manifold_phase(results, cosmo_name, path):
    """(rho_peak, v_peak) phase portrait for all ICs in one cosmology."""
    fig, ax = plt.subplots(figsize=(MAX_W_IN, MAX_H_IN))

    for r in results:
        sty = CAT_STYLES[r["category"]]
        rp = np.array(r["rhopeak_hist"])
        vp = np.array(r["vpeak_hist"])
        ax.plot(rp, vp, color=sty["color"], ls=sty["ls"], lw=0.5, alpha=0.7)
        ax.plot(rp[0], vp[0], "o", color=sty["color"], ms=4, alpha=0.8)

    ax.plot(RHO_STAR, 0.0, "k+", ms=12, mew=2, zorder=5)
    ax.axvline(RHO_STAR, color="gray", ls=":", alpha=0.2)
    ax.axhline(0.0, color="gray", ls=":", alpha=0.2)

    handles = [Line2D([0], [0], color=s["color"], ls=s["ls"], lw=1.5, label=cat)
               for cat, s in CAT_STYLES.items()]
    ax.legend(handles=handles, fontsize=8, loc="best")
    ax.set_xlabel(r"$\rho_{\rm peak}$", fontsize=10)
    ax.set_ylabel(r"$v_{\rm peak}$", fontsize=10)
    ax.set_title(f"Stable manifold phase portrait -- {cosmo_name}", fontsize=11)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_manifold_distance(results, cosmo_name, path):
    """d(t) for all ICs, log scale."""
    fig, ax = plt.subplots(figsize=(MAX_W_IN, MAX_H_IN))

    for r in results:
        sty = CAT_STYLES[r["category"]]
        d = np.array(r["dist_hist"])
        d_safe = np.maximum(d, 1e-15)
        ax.semilogy(r["time_hist"], d_safe, color=sty["color"],
                     ls=sty["ls"], lw=0.5, alpha=0.7)

    handles = [Line2D([0], [0], color=s["color"], ls=s["ls"], lw=1.5, label=cat)
               for cat, s in CAT_STYLES.items()]
    ax.legend(handles=handles, fontsize=8, loc="best")
    ax.set_xlabel("Time", fontsize=10)
    ax.set_ylabel("Distance to equilibrium (log)", fontsize=10)
    ax.set_title(f"Convergence to attractor -- {cosmo_name}", fontsize=11)
    ax.grid(True, alpha=0.15)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_manifold_convergence(analyses, cosmo_name, path):
    """Bar chart of lambda values colored by category."""
    fig, ax = plt.subplots(figsize=(MAX_W_IN, MAX_H_IN))

    labels = [a["ic_label"] for a in analyses]
    rates  = [a["convergence_rate"] for a in analyses]
    colors = [CAT_STYLES[a["category"]]["color"] for a in analyses]

    ax.barh(range(len(labels)), rates, color=colors, height=0.7)
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=7)
    ax.set_xlabel("Convergence rate (lambda)", fontsize=10)
    ax.set_title(f"Convergence rates -- {cosmo_name}", fontsize=11)
    ax.invert_yaxis()

    handles = [Line2D([0], [0], color=s["color"], lw=6, label=cat)
               for cat, s in CAT_STYLES.items()]
    ax.legend(handles=handles, fontsize=7, loc="lower right")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


# ======================================================================
# Main
# ======================================================================

def main():
    print("=" * 70)
    print("ED-Phys-30: Stability Manifold")
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

        cosmo_results  = []
        cosmo_analysis = []

        for rho_init, v_init, ic_label, category in ic_set:
            run_idx += 1
            result = run_case(rho_init, v_init, ic_label, category,
                              cosmo_name, D)
            analysis = analyze_result(result)
            cosmo_results.append(result)
            cosmo_analysis.append(analysis)
            all_results.append(result)
            all_analysis.append(analysis)

            osc_tag = " [OSC]" if analysis["oscillatory_approach"] else ""
            print(f"  [{run_idx:3d}/{total}] {ic_label:<22s} "
                  f"lam={analysis['convergence_rate']:>.5f}  "
                  f"dir={analysis['approach_direction']:<8s}  "
                  f"curv={analysis['curvature']:>8.4f}  "
                  f"cross={analysis['n_crossings']}{osc_tag}")

        # -- Per-cosmology plots ---------------------------------------
        print(f"  >>> Plotting {cosmo_name} manifold...")
        plot_manifold_phase(cosmo_results, cosmo_name,
                            OUT / f"{cosmo_name}_manifold_phase.png")
        plot_manifold_distance(cosmo_results, cosmo_name,
                               OUT / f"{cosmo_name}_manifold_distance.png")
        plot_manifold_convergence(cosmo_analysis, cosmo_name,
                                  OUT / f"{cosmo_name}_manifold_convergence.png")

        # -- Manifold collapse check -----------------------------------
        dim, spread = check_manifold_collapse(cosmo_results)
        print(f"  Manifold dimension: {dim}D  (v-spread={spread:.6f})")

    # -- Summary JSON --------------------------------------------------
    # Aggregate per-cosmology stats
    cosmo_summaries = {}
    for cosmo_name, _, _ in COSMOLOGIES:
        subset_a = [a for a in all_analysis if a["cosmo"] == cosmo_name]
        subset_r = [r for r in all_results if r["cosmo"] == cosmo_name]

        rates = [a["convergence_rate"] for a in subset_a if a["convergence_rate"] > 0]
        n_osc = sum(1 for a in subset_a if a["oscillatory_approach"])
        n_mono = sum(1 for a in subset_a if not a["oscillatory_approach"])
        curv_vals = [a["curvature"] for a in subset_a]
        dim, spread = check_manifold_collapse(subset_r)

        dir_counts = {}
        for a in subset_a:
            d = a["approach_direction"]
            dir_counts[d] = dir_counts.get(d, 0) + 1

        cosmo_summaries[cosmo_name] = {
            "manifold_dimension": dim,
            "manifold_v_spread": spread,
            "mean_convergence_rate": float(np.mean(rates)) if rates else 0.0,
            "std_convergence_rate": float(np.std(rates)) if rates else 0.0,
            "min_convergence_rate": float(np.min(rates)) if rates else 0.0,
            "max_convergence_rate": float(np.max(rates)) if rates else 0.0,
            "oscillatory_approach_count": n_osc,
            "monotonic_approach_count": n_mono,
            "mean_curvature": float(np.mean(curv_vals)),
            "approach_direction_counts": dir_counts,
        }

    # Check for secondary attractors
    secondary = [a for a in all_analysis if a["final_dist"] > 0.1]

    export = {
        "experiment": "ED-Phys-30_StabilityManifold",
        "parameters": {
            "NX": NX, "N_STEPS": N_STEPS, "SAMPLE": SAMPLE,
            "TAU": TAU, "ZETA": ZETA, "RHO_STAR": RHO_STAR,
        },
        "total_runs": total,
        "n_ics": n_ics,
        "single_global_attractor": len(secondary) == 0,
        "secondary_attractor_count": len(secondary),
        "cosmo_summaries": cosmo_summaries,
        "all_analysis": all_analysis,
    }

    json_path = OUT / "manifold_geometry.json"
    with open(json_path, "w") as f:
        json.dump(export, f, indent=2)
    print(f"\n>>> Summary written to {json_path}")

    # -- Print summary -------------------------------------------------
    print("\n" + "=" * 70)
    print("STABILITY MANIFOLD ANALYSIS")
    print("=" * 70)

    if len(secondary) == 0:
        print("All trajectories converge to (rho*, 0). Single global attractor.")
    else:
        print(f"WARNING: {len(secondary)} trajectories not converged.")

    for cosmo_name, stats in cosmo_summaries.items():
        print(f"\n  {cosmo_name}:")
        print(f"    Manifold dim: {stats['manifold_dimension']}D  "
              f"(v-spread={stats['manifold_v_spread']:.6f})")
        print(f"    Convergence: {stats['mean_convergence_rate']:.5f} "
              f"+/- {stats['std_convergence_rate']:.5f}  "
              f"[{stats['min_convergence_rate']:.5f}, "
              f"{stats['max_convergence_rate']:.5f}]")
        print(f"    Approach: {stats['oscillatory_approach_count']} oscillatory, "
              f"{stats['monotonic_approach_count']} monotonic")
        print(f"    Directions: {stats['approach_direction_counts']}")
        print(f"    Mean curvature: {stats['mean_curvature']:.6f}")

    print("\n" + "=" * 70)
    print(">>> Done. All outputs in:", OUT)


if __name__ == "__main__":
    main()
