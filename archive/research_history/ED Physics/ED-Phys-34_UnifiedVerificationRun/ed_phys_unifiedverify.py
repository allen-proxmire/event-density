#!/usr/bin/env python3
"""
ED-Phys-34: Unified Verification Run
=======================================
Comprehensive verification that the unified ED cosmology PDE reproduces
all major dynamical behaviors discovered across ED-Phys-01 through ED-Phys-33.

5 regimes x 4 ICs = 20 runs.
"""

import json
import numpy as np
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# -- Canonical parameters ----------------------------------------------
ALPHA    = 0.1
GAMMA    = 0.5
M0       = 1.0
RHO_MAX  = 100.0
N_MOB    = 2
RHO_STAR = 50.0
RHO_0    = 0.5
DX       = 1.0
ETA      = 0.2
EPS_NUM  = 1e-10

# -- Simulation --------------------------------------------------------
NX       = 256
N_STEPS  = 80_000
SAMPLE   = 30
SIGMA_IC = 8.0

# -- Output ------------------------------------------------------------
OUT = Path(__file__).parent / "results"
OUT.mkdir(exist_ok=True)
MAX_W_IN = 1000 / 150
MAX_H_IN = 800 / 150

# ======================================================================
# Regimes with predictions from ED-Phys-01..33
# ======================================================================

REGIMES = [
    {
        "name": "pure_oscillatory",
        "D": 0.0, "zeta": 0.25, "tau": 1.0,
        "predictions": {
            "many_cycles": True,
            "spiral_manifold": True,
            "horizon_at_A40": True,
            "monotonic": False,
            "fast_convergence": False,
        },
    },
    {
        "name": "hybrid_fast",
        "D": 0.25, "zeta": 0.25, "tau": 1.0,
        "predictions": {
            "many_cycles": False,
            "spiral_manifold": True,
            "horizon_at_A40": False,
            "monotonic": False,
            "fast_convergence": True,
        },
    },
    {
        "name": "hybrid_canonical",
        "D": 0.50, "zeta": 0.50, "tau": 1.0,
        "predictions": {
            "many_cycles": False,
            "spiral_manifold": False,
            "horizon_at_A40": False,
            "monotonic": True,
            "fast_convergence": False,
        },
    },
    {
        "name": "parabolic_monotonic",
        "D": 1.0, "zeta": 1.0, "tau": 1.0,
        "predictions": {
            "many_cycles": False,
            "spiral_manifold": False,
            "horizon_at_A40": False,
            "monotonic": True,
            "fast_convergence": False,
        },
    },
    {
        "name": "boundary_case",
        "D": 0.50, "zeta": 0.25, "tau": 1.0,
        "predictions": {
            "many_cycles": False,
            "spiral_manifold": True,
            "horizon_at_A40": False,
            "monotonic": False,
            "fast_convergence": False,
        },
    },
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
# ICs
# ======================================================================

def build_ics(nx):
    x = np.arange(nx, dtype=np.float64)
    center = nx / 2.0
    ics = []

    # Gaussian A=20
    rho = RHO_STAR + 20.0 * np.exp(-((x - center) / SIGMA_IC) ** 2)
    ics.append((np.clip(rho, EPS_NUM, RHO_MAX - EPS_NUM).copy(), "gauss_A20"))

    # Gaussian A=40
    rho = RHO_STAR + 40.0 * np.exp(-((x - center) / SIGMA_IC) ** 2)
    ics.append((np.clip(rho, EPS_NUM, RHO_MAX - EPS_NUM).copy(), "gauss_A40"))

    # Sine k=4
    kx = 2.0 * np.pi * 4 / nx
    rho = RHO_STAR + 20.0 * np.sin(kx * x)
    ics.append((np.clip(rho, EPS_NUM, RHO_MAX - EPS_NUM).copy(), "sine_k4"))

    # Mixed
    kx4 = 2.0 * np.pi * 4 / nx
    kx7 = 2.0 * np.pi * 7 / nx
    rho = RHO_STAR + 20.0 * np.sin(kx4 * x) + 10.0 * np.sin(kx7 * x)
    ics.append((np.clip(rho, EPS_NUM, RHO_MAX - EPS_NUM).copy(), "mixed_k4k7"))

    return ics


# ======================================================================
# PDE integration
# ======================================================================

def run_case(D, tau, zeta, rho_init):
    H = 1.0 - D
    rho = rho_init.copy()
    v = np.zeros(NX, dtype=np.float64)
    peak_idx = NX // 2
    dt = ETA * DX * DX / (M0 + EPS_NUM)

    rp_hist = []; vp_hist = []; std_hist = []
    time_hist = []; dist_hist = []; horizon_hist = []

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
            rp_hist.append(rp)
            vp_hist.append(vp)
            std_hist.append(float(np.std(rho)))
            time_hist.append(t)
            dist_hist.append(np.sqrt((rp - RHO_STAR)**2 + vp**2))
            horizon_hist.append(int(np.sum(rho >= 0.9 * RHO_MAX)))

    return {
        "rp": rp_hist, "vp": vp_hist, "std": std_hist,
        "time": time_hist, "dist": dist_hist, "horizon": horizon_hist,
    }


# ======================================================================
# Analysis
# ======================================================================

def fit_convergence(dist_hist, time_hist):
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


def count_oscillations(rp_hist):
    delta = np.array(rp_hist) - RHO_STAR
    crossings = 0
    for i in range(1, len(delta)):
        if delta[i - 1] * delta[i] < 0:
            crossings += 1
    return crossings // 2


def measure_extremes(rp_hist):
    delta = np.array(rp_hist) - RHO_STAR
    undershoot = float(-np.min(delta)) if np.min(delta) < 0 else 0.0
    below_idx = np.where(delta < 0)[0]
    if len(below_idx) > 0:
        overshoot = float(np.max(delta[below_idx[0]:])) if np.max(delta[below_idx[0]:]) > 0 else 0.0
    else:
        overshoot = 0.0
    return undershoot, overshoot


def classify_flow(rp_hist, vp_hist):
    delta = np.array(rp_hist) - RHO_STAR
    rho_cross = sum(1 for i in range(1, len(delta)) if delta[i-1]*delta[i] < 0)
    vp = np.array(vp_hist)
    v_cross = sum(1 for i in range(1, len(vp)) if vp[i-1]*vp[i] < 0)
    total = rho_cross + v_cross
    if total > 6:
        return "spiral"
    elif total > 1:
        return "damped"
    else:
        return "monotonic"


def analyze(result):
    lam = fit_convergence(result["dist"], result["time"])
    n_cyc = count_oscillations(result["rp"])
    undershoot, overshoot = measure_extremes(result["rp"])
    peak_v = float(np.max(np.abs(result["vp"])))
    flow = classify_flow(result["rp"], result["vp"])
    horizon_max = int(np.max(result["horizon"])) if result["horizon"] else 0
    return {
        "convergence_rate": lam,
        "n_cycles": n_cyc,
        "undershoot": undershoot,
        "overshoot": overshoot,
        "peak_v": peak_v,
        "flow_type": flow,
        "horizon_max": horizon_max,
        "horizon_activated": horizon_max > 0,
    }


def verify_predictions(regime, ic_label, ana):
    """Check observed behavior against predictions. Returns list of (check, pass/fail)."""
    pred = regime["predictions"]
    checks = []

    # many_cycles: >10 cycles expected
    if pred["many_cycles"]:
        checks.append(("many_cycles (>10)", ana["n_cycles"] > 10))
    else:
        checks.append(("few_cycles (<=10)", ana["n_cycles"] <= 10))

    # spiral manifold
    if pred["spiral_manifold"]:
        checks.append(("spiral_flow", ana["flow_type"] == "spiral"))
    else:
        checks.append(("non_spiral_flow", ana["flow_type"] != "spiral"))

    # horizon at A40
    if "A40" in ic_label:
        if pred["horizon_at_A40"]:
            checks.append(("horizon_at_A40", ana["horizon_activated"]))
        else:
            checks.append(("no_horizon_at_A40", not ana["horizon_activated"]))

    # monotonic
    if pred["monotonic"]:
        checks.append(("monotonic_approach", ana["flow_type"] == "monotonic"))

    # fast convergence: lambda > 0.03
    if pred["fast_convergence"]:
        checks.append(("fast_convergence (lam>0.03)", ana["convergence_rate"] > 0.03))

    return checks


# ======================================================================
# Plotting
# ======================================================================

REGIME_COLORS = {
    "pure_oscillatory": "royalblue",
    "hybrid_fast": "darkorange",
    "hybrid_canonical": "seagreen",
    "parabolic_monotonic": "firebrick",
    "boundary_case": "darkviolet",
}
IC_STYLES = {"gauss_A20": "-", "gauss_A40": "--", "sine_k4": "-.", "mixed_k4k7": ":"}


def plot_time_series(all_runs, path):
    """Overlaid rho_peak(t) for all regimes, one panel per IC."""
    ic_labels = list(IC_STYLES.keys())
    fig, axes = plt.subplots(2, 2, figsize=(MAX_W_IN, MAX_H_IN))

    for idx, ic_label in enumerate(ic_labels):
        row, col = divmod(idx, 2)
        ax = axes[row, col]
        for run in all_runs:
            if run["ic"] == ic_label:
                color = REGIME_COLORS[run["regime"]]
                ax.plot(run["result"]["time"], run["result"]["rp"],
                        color=color, lw=0.6, alpha=0.8, label=run["regime"])
        ax.axhline(RHO_STAR, color="gray", ls=":", alpha=0.3)
        ax.set_title(ic_label, fontsize=9)
        ax.tick_params(labelsize=7)
        if row == 1:
            ax.set_xlabel("Time", fontsize=8)
        if col == 0:
            ax.set_ylabel(r"$\rho_{\rm peak}$", fontsize=8)

    # Legend on first panel
    axes[0, 0].legend(fontsize=5, loc="upper right")
    fig.suptitle("Verification: time series across regimes", fontsize=10, y=1.01)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_phase_portraits(all_runs, path):
    """One panel per regime, all ICs overlaid."""
    fig, axes = plt.subplots(1, 5, figsize=(MAX_W_IN, MAX_H_IN))
    ic_colors = {"gauss_A20": "steelblue", "gauss_A40": "firebrick",
                 "sine_k4": "seagreen", "mixed_k4k7": "darkorange"}

    for idx, regime in enumerate(REGIMES):
        ax = axes[idx]
        rname = regime["name"]
        for run in all_runs:
            if run["regime"] == rname:
                rp = np.array(run["result"]["rp"])
                vp = np.array(run["result"]["vp"])
                ax.plot(rp, vp, color=ic_colors[run["ic"]], lw=0.4, alpha=0.7)
        ax.plot(RHO_STAR, 0.0, "k+", ms=6, mew=1.5)
        ax.set_title(rname.replace("_", "\n"), fontsize=6)
        ax.tick_params(labelsize=5)
        if idx == 0:
            ax.set_ylabel(r"$v_{\rm peak}$", fontsize=7)

    fig.suptitle("Verification: phase portraits", fontsize=10, y=1.01)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_convergence(all_runs, path):
    """Bar chart of lambda grouped by regime."""
    fig, ax = plt.subplots(figsize=(MAX_W_IN, MAX_H_IN))
    regime_names = [r["name"] for r in REGIMES]
    ic_labels = list(IC_STYLES.keys())
    n_r = len(regime_names)
    n_ic = len(ic_labels)
    width = 0.8 / n_ic
    ic_colors = ["steelblue", "firebrick", "seagreen", "darkorange"]

    for j, ic_label in enumerate(ic_labels):
        vals = []
        for rname in regime_names:
            match = [r for r in all_runs if r["regime"] == rname and r["ic"] == ic_label]
            vals.append(match[0]["analysis"]["convergence_rate"] if match else 0)
        x = np.arange(n_r) + j * width
        ax.bar(x, vals, width, label=ic_label, color=ic_colors[j], alpha=0.8)

    ax.set_xticks(np.arange(n_r) + width * (n_ic - 1) / 2)
    ax.set_xticklabels([r.replace("_", "\n") for r in regime_names], fontsize=7)
    ax.set_ylabel("Convergence rate (lambda)", fontsize=9)
    ax.set_title("Convergence rates across regimes", fontsize=10)
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_horizon(all_runs, path):
    """Horizon activation: grid of regime x IC."""
    fig, ax = plt.subplots(figsize=(MAX_W_IN, MAX_H_IN))
    regime_names = [r["name"] for r in REGIMES]
    ic_labels = list(IC_STYLES.keys())

    grid = np.zeros((len(ic_labels), len(regime_names)))
    for run in all_runs:
        i = ic_labels.index(run["ic"])
        j = regime_names.index(run["regime"])
        grid[i, j] = run["analysis"]["horizon_max"]

    im = ax.imshow(grid, aspect="auto", cmap="YlOrRd", origin="lower")
    ax.set_xticks(range(len(regime_names)))
    ax.set_xticklabels([r.replace("_", "\n") for r in regime_names], fontsize=7)
    ax.set_yticks(range(len(ic_labels)))
    ax.set_yticklabels(ic_labels, fontsize=8)
    ax.set_xlabel("Regime", fontsize=9)
    ax.set_ylabel("IC", fontsize=9)
    ax.set_title("Horizon activation (max sites at 0.9*rho_max)", fontsize=10)

    # Annotate cells
    for i in range(len(ic_labels)):
        for j in range(len(regime_names)):
            val = int(grid[i, j])
            color = "white" if val > 5 else "black"
            ax.text(j, i, str(val), ha="center", va="center", fontsize=9, color=color)

    fig.colorbar(im, ax=ax, shrink=0.8)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


# ======================================================================
# Main
# ======================================================================

def main():
    print("=" * 70)
    print("ED-Phys-34: Unified Verification Run")
    print("=" * 70)

    ics = build_ics(NX)
    total = len(REGIMES) * len(ics)
    print(f"Regimes: {len(REGIMES)}   ICs: {len(ics)}   Total: {total}")
    print("=" * 70)

    all_runs = []
    all_checks = []
    run_idx = 0

    for regime in REGIMES:
        rname = regime["name"]
        D = regime["D"]
        tau = regime["tau"]
        zeta = regime["zeta"]

        print(f"\n--- {rname} (D={D}, zeta={zeta}, tau={tau}) ---")

        for rho_init, ic_label in ics:
            run_idx += 1
            result = run_case(D, tau, zeta, rho_init)
            ana = analyze(result)
            checks = verify_predictions(regime, ic_label, ana)

            all_checks.extend([(rname, ic_label, c, p) for c, p in checks])
            all_runs.append({
                "regime": rname, "ic": ic_label,
                "result": result, "analysis": ana,
                "checks": checks,
            })

            pass_str = " ".join(
                f"{'PASS' if p else 'FAIL'}:{c.split('(')[0].strip()}"
                for c, p in checks
            )
            print(f"  [{run_idx:2d}/{total}] {ic_label:<14s} "
                  f"cyc={ana['n_cycles']:>4d}  "
                  f"lam={ana['convergence_rate']:.5f}  "
                  f"{ana['flow_type']:<9s} "
                  f"hor={'Y' if ana['horizon_activated'] else 'N'}  "
                  f"| {pass_str}")

    # -- Plots ---------------------------------------------------------
    print("\n>>> Generating verification plots...")
    plot_time_series(all_runs, OUT / "verification_time_series.png")
    plot_phase_portraits(all_runs, OUT / "verification_phase_portraits.png")
    plot_convergence(all_runs, OUT / "verification_convergence.png")
    plot_horizon(all_runs, OUT / "verification_horizon.png")

    # -- Verification summary ------------------------------------------
    total_checks = len(all_checks)
    passed = sum(1 for _, _, _, p in all_checks if p)
    failed = sum(1 for _, _, _, p in all_checks if not p)

    failures = [(r, ic, c, p) for r, ic, c, p in all_checks if not p]

    verification = []
    for regime in REGIMES:
        rname = regime["name"]
        regime_checks = [(ic, c, p) for r, ic, c, p in all_checks if r == rname]
        regime_pass = sum(1 for _, _, p in regime_checks if p)
        regime_total = len(regime_checks)
        regime_runs = [r for r in all_runs if r["regime"] == rname]

        entry = {
            "regime": rname,
            "D": regime["D"], "zeta": regime["zeta"], "tau": regime["tau"],
            "predictions": regime["predictions"],
            "observed": {},
            "checks_passed": regime_pass,
            "checks_total": regime_total,
            "match": regime_pass == regime_total,
        }

        # Aggregate observed for this regime
        for run in regime_runs:
            entry["observed"][run["ic"]] = run["analysis"]

        verification.append(entry)

    export = {
        "experiment": "ED-Phys-34_UnifiedVerificationRun",
        "total_runs": total,
        "total_checks": total_checks,
        "checks_passed": passed,
        "checks_failed": failed,
        "pass_rate": f"{passed/total_checks*100:.1f}%",
        "failures": [{"regime": r, "ic": ic, "check": c} for r, ic, c, p in failures],
        "verification": verification,
    }

    json_path = OUT / "unified_verification_summary.json"
    with open(json_path, "w") as f:
        json.dump(export, f, indent=2)
    print(f"\n>>> Summary written to {json_path}")

    # -- Print results -------------------------------------------------
    print("\n" + "=" * 70)
    print("UNIFIED VERIFICATION RESULTS")
    print("=" * 70)
    print(f"\nTotal checks: {total_checks}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Pass rate: {passed/total_checks*100:.1f}%")

    if failures:
        print(f"\nFAILURES ({failed}):")
        for r, ic, c, _ in failures:
            print(f"  {r} / {ic}: {c}")
    else:
        print("\nALL CHECKS PASSED.")

    print("\nPer-regime summary:")
    for v in verification:
        status = "PASS" if v["match"] else "FAIL"
        print(f"  [{status}] {v['regime']}: "
              f"{v['checks_passed']}/{v['checks_total']} checks")

    print("\n" + "=" * 70)
    print(">>> Done. All outputs in:", OUT)


if __name__ == "__main__":
    main()
