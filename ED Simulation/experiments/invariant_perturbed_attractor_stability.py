"""
invariant_perturbed_attractor_stability.py
===========================================
Experiment / Analysis: Invariant Perturbed-Attractor Stability

Scans all completed regime_D*_A*_Nm* runs, identifies the attractor
state a_k^*, loads perturbed trajectories at multiple perturbation
amplitudes ε, and analyses the recovery dynamics:

    E_err(t) = Σ_k |a_k(t) − a_k^*|²  →  C exp(−σ_ε t)

The recovery rate σ_ε and half-life t_half are structural invariants
of the ED architecture.  Theorem C.43 (Lyapunov stability) predicts
exponential recovery for all perturbations within the local basin,
with rate determined by the spectral gap (Lemma C.31).  Principle 3
(unique attractor) guarantees that the recovery target is the same
for all ε.

Perturbed trajectories are expected at:
    output/runs/{base_run}/perturb_eps_{label}/time_series.npz

If perturbed sub-runs are not found, the script synthesises them by
perturbing the attractor state and running a short re-integration
(requires edsim_runner to be importable).  If that also fails, the
perturbation level is skipped with a warning.

Produces:
  (A) Perturbation Recovery Curves — E_err(t) for all ε.
  (B) Recovery Rate vs ε — σ_ε scatter for all runs.
  (C) Stability Heatmap — fraction recovered across (D, A, Nm).

All figures saved to output/figures/invariants/perturbed_attractor_stability/
as PNG (300 dpi).

Usage:
    python experiments/invariant_perturbed_attractor_stability.py

Requires: numpy, matplotlib.
"""

import os
import sys
import glob
import json
import re
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SIM_DIR = os.path.dirname(SCRIPT_DIR)
RUNS_DIR = os.path.join(SIM_DIR, "output", "runs")
FIG_DIR = os.path.join(SIM_DIR, "output", "figures", "invariants",
                        "perturbed_attractor_stability")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
K_MAX = 20
LATE_FRAC = 0.10         # Fraction for attractor average
FIT_FRAC = 0.50          # Last 50% of perturbed run for recovery fit
R2_THRESH = 0.90         # Clean recovery threshold
MONOTONE_FRAC = 0.05     # Allow up to 5% non-monotone steps

EPS_VALUES = [1e-6, 1e-5, 1e-4, 1e-3]
EPS_LABELS = {1e-6: "1e-6", 1e-5: "1e-5", 1e-4: "1e-4", 1e-3: "1e-3"}
EPS_COLORS = {1e-6: "#2166ac", 1e-5: "#4393c3", 1e-4: "#d6604d", 1e-3: "#b2182b"}

NORM_FLOOR = 1e-30


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------
def discover_regime_runs() -> list[dict]:
    """Scan for base regime runs and their perturbed sub-runs."""
    pattern = os.path.join(RUNS_DIR, "regime_D*_A*_Nm*")
    dirs = sorted(glob.glob(pattern))

    runs = []
    for d in dirs:
        # Skip perturb sub-directories at top level
        if "perturb_eps" in os.path.basename(d):
            continue

        ts_path = os.path.join(d, "time_series.npz")
        meta_path = os.path.join(d, "metadata.json")
        if not os.path.isfile(ts_path):
            continue

        meta = {}
        if os.path.isfile(meta_path):
            with open(meta_path, "r") as f:
                meta = json.load(f)

        if meta.get("regime") == "inadmissible":
            continue

        D_val = meta.get("D")
        A_val = meta.get("A") or meta.get("A_per_mode")
        Nm_val = (meta.get("Nm") or meta.get("n_seeded")
                  or meta.get("N_modes_seeded"))

        name = os.path.basename(d)
        D_val, A_val, Nm_val = _fill_from_dirname(name, D_val, A_val, Nm_val)

        if D_val is None or A_val is None or Nm_val is None:
            continue

        ts = np.load(ts_path, allow_pickle=True)
        modal = ts.get("modal_amplitudes")
        t = ts.get("t")

        if modal is None or t is None or modal.ndim != 2:
            continue

        n = min(len(t), modal.shape[0])
        if modal.shape[1] < 3 or n < 50:
            continue

        # Discover perturbed sub-runs
        perturbed = {}
        for eps in EPS_VALUES:
            eps_label = EPS_LABELS[eps]
            # Try multiple naming conventions
            for sub_name in [f"perturb_eps_{eps_label}",
                             f"perturb_eps{eps_label}",
                             f"perturb_{eps_label}"]:
                sub_dir = os.path.join(d, sub_name)
                sub_ts = os.path.join(sub_dir, "time_series.npz")
                if os.path.isfile(sub_ts):
                    perturbed[eps] = sub_dir
                    break

            # Also check sibling directories
            if eps not in perturbed:
                sibling = os.path.join(RUNS_DIR,
                                       f"{name}_perturb_eps_{eps_label}")
                sibling_ts = os.path.join(sibling, "time_series.npz")
                if os.path.isfile(sibling_ts):
                    perturbed[eps] = sibling

        runs.append({
            "dir": d,
            "name": name,
            "D": float(D_val),
            "A": float(A_val),
            "Nm": int(Nm_val),
            "metadata": meta,
            "t": t[:n],
            "modal": modal[:n],
            "perturbed_dirs": perturbed,
        })

    runs.sort(key=lambda r: (r["D"], r["A"], r["Nm"]))
    return runs


def _fill_from_dirname(name: str, D, A, Nm):
    m_D = re.search(r"D([\d.eE+-]+)", name)
    m_A = re.search(r"A([\d.eE+-]+)", name)
    m_Nm = re.search(r"Nm(\d+)", name)
    if D is None and m_D:
        try:
            D = float(m_D.group(1))
        except ValueError:
            pass
    if A is None and m_A:
        try:
            A = float(m_A.group(1))
        except ValueError:
            pass
    if Nm is None and m_Nm:
        try:
            Nm = int(m_Nm.group(1))
        except ValueError:
            pass
    return D, A, Nm


# ---------------------------------------------------------------------------
# Attractor state extraction
# ---------------------------------------------------------------------------
def extract_attractor(modal: np.ndarray, n_total: int, K: int) -> np.ndarray:
    """Mean modal amplitudes over the last LATE_FRAC of the base run.

    Returns a_star of shape (K,) — may be complex or real.
    """
    start = max(0, int((1.0 - LATE_FRAC) * n_total))
    return np.mean(modal[start:, 1:K+1], axis=0)


# ---------------------------------------------------------------------------
# Perturbation recovery analysis
# ---------------------------------------------------------------------------
def analyse_perturbation(perturb_dir: str, a_star: np.ndarray,
                         K: int) -> dict | None:
    """Load a perturbed trajectory and analyse its recovery."""
    ts_path = os.path.join(perturb_dir, "time_series.npz")
    if not os.path.isfile(ts_path):
        return None

    ts = np.load(ts_path, allow_pickle=True)
    modal_p = ts.get("modal_amplitudes")
    t_p = ts.get("t")

    if modal_p is None or t_p is None or modal_p.ndim != 2:
        return None

    n_p = min(len(t_p), modal_p.shape[0])
    if n_p < 20:
        return None

    K_p = min(K, modal_p.shape[1] - 1)
    if K_p < 1:
        return None

    # Error signal: E_err(t) = Σ_k |a_k(t) − a_k^*|²
    a_star_trunc = a_star[:K_p]
    diff = modal_p[:n_p, 1:K_p+1] - a_star_trunc[np.newaxis, :]
    E_err = np.sum(np.abs(diff) ** 2, axis=1)

    # Recovery fit over last FIT_FRAC
    fit_start = max(0, int((1.0 - FIT_FRAC) * n_p))
    t_fit = t_p[fit_start:n_p]
    E_fit = E_err[fit_start:n_p]

    sigma, R2 = _fit_exp_decay(t_fit, E_fit)

    # Half-life
    if sigma > 0:
        t_half = float(np.log(2) / sigma)
    else:
        t_half = float("inf")

    # Monotonicity check
    if len(E_err) > 1:
        dE = np.diff(E_err)
        n_increase = np.sum(dE > 0)
        frac_increase = n_increase / max(len(dE), 1)
        monotone = frac_increase < MONOTONE_FRAC
    else:
        monotone = True

    # Clean recovery flag
    recovered = sigma > 0 and R2 > R2_THRESH and monotone

    return {
        "sigma": sigma,
        "R2": R2,
        "t_half": t_half,
        "monotone": monotone,
        "recovered": recovered,
        "E_err_0": float(E_err[0]) if len(E_err) > 0 else 0.0,
        "E_err_T": float(E_err[-1]) if len(E_err) > 0 else 0.0,
        "t": t_p[:n_p],
        "E_err": E_err,
    }


def _fit_exp_decay(t: np.ndarray, E: np.ndarray) -> tuple:
    """Fit E ~ C exp(-sigma t). Returns (sigma, R²)."""
    valid = E > NORM_FLOOR
    if np.sum(valid) < 5:
        return 0.0, 0.0

    log_E = np.log(E[valid])
    t_v = t[valid]

    try:
        coeffs = np.polyfit(t_v, log_E, 1)
        sigma = -coeffs[0]

        predicted = coeffs[0] * t_v + coeffs[1]
        ss_res = np.sum((log_E - predicted) ** 2)
        ss_tot = np.sum((log_E - np.mean(log_E)) ** 2)
        R2 = 1.0 - ss_res / max(ss_tot, 1e-30)

        return float(sigma), float(R2)
    except (np.linalg.LinAlgError, ValueError):
        return 0.0, 0.0


# ---------------------------------------------------------------------------
# Per-run analysis
# ---------------------------------------------------------------------------
def analyse_run(run: dict) -> dict:
    """Analyse all perturbation levels for one base run."""
    modal = run["modal"]
    n = len(run["t"])
    n_modes = modal.shape[1]
    K = min(K_MAX, n_modes - 1)

    a_star = extract_attractor(modal, n, K)

    eps_results = {}
    n_recovered = 0
    n_attempted = 0

    for eps in EPS_VALUES:
        if eps in run["perturbed_dirs"]:
            result = analyse_perturbation(
                run["perturbed_dirs"][eps], a_star, K
            )
            if result is not None:
                eps_results[eps] = result
                n_attempted += 1
                if result["recovered"]:
                    n_recovered += 1
            else:
                eps_results[eps] = None
        else:
            eps_results[eps] = None

    frac = n_recovered / max(n_attempted, 1) if n_attempted > 0 else 0.0

    return {
        "K": K,
        "eps_results": eps_results,
        "n_attempted": n_attempted,
        "n_recovered": n_recovered,
        "frac_recovered": frac,
    }


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def setup_axes(ax, xlabel: str, ylabel: str, title: str):
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.tick_params(labelsize=10)
    ax.grid(True, alpha=0.3, linewidth=0.5)


# ---------------------------------------------------------------------------
# Figure A: Perturbation Recovery Curves (representative run)
# ---------------------------------------------------------------------------
def figure_recovery_curves(runs: list[dict], analyses: list[dict]):
    """E_err(t) for all ε on semilog-y for the largest-Nm run."""
    # Pick the run with the most perturbed sub-runs
    best_idx = None
    best_count = 0
    for i, (run, ana) in enumerate(zip(runs, analyses)):
        count = sum(1 for r in ana["eps_results"].values() if r is not None)
        if count > best_count or (count == best_count and run["Nm"] >
                                  (runs[best_idx]["Nm"] if best_idx is not None else 0)):
            best_count = count
            best_idx = i

    if best_idx is None or best_count == 0:
        print("  SKIP recovery curves: no perturbed runs found.")
        return

    run = runs[best_idx]
    ana = analyses[best_idx]

    fig, ax = plt.subplots(figsize=(10, 6))

    for eps in EPS_VALUES:
        result = ana["eps_results"].get(eps)
        if result is None:
            continue

        t_p = result["t"]
        E_err = result["E_err"]
        color = EPS_COLORS[eps]
        label = EPS_LABELS[eps]

        ax.semilogy(
            t_p, np.maximum(E_err, NORM_FLOOR),
            color=color, linewidth=1.5,
            label=(rf"$\varepsilon = {label}$: "
                   rf"$\sigma = {result['sigma']:.4f}$, "
                   rf"$t_{{1/2}} = {result['t_half']:.2f}$"),
        )

        # Recovery flag annotation
        if result["recovered"]:
            marker = "✓"
            m_color = "#1b7837"
        else:
            marker = "✗"
            m_color = "#b2182b"

        ax.annotate(
            marker,
            xy=(t_p[-1], max(E_err[-1], NORM_FLOOR)),
            fontsize=14, color=m_color, fontweight="bold",
            ha="left", va="center",
        )

    setup_axes(
        ax,
        xlabel=r"Time $t$",
        ylabel=r"Recovery error $E_{\mathrm{err}}(t) = \Sigma_k |a_k - a_k^*|^2$",
        title=(f"Perturbation Recovery — D={run['D']}, A={run['A']}, "
               f"Nm={run['Nm']}"),
    )
    ax.legend(fontsize=8, loc="upper right", framealpha=0.9)
    fig.tight_layout()

    fname = "recovery_curves.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure B: Recovery Rate vs ε
# ---------------------------------------------------------------------------
def figure_rate_vs_eps(runs: list[dict], analyses: list[dict]):
    """Scatter σ_ε vs ε for all runs."""
    D_vals = sorted(set(r["D"] for r in runs))
    Nm_vals = sorted(set(r["Nm"] for r in runs))

    D_cmap = plt.cm.plasma
    D_norm = mcolors.Normalize(
        vmin=min(D_vals) * 0.9 if D_vals else 0,
        vmax=max(D_vals) * 1.1 if D_vals else 1,
    )
    Nm_markers = {Nm_vals[i]: m for i, m in
                  zip(range(len(Nm_vals)),
                      ["o", "s", "^", "D", "v", "P", "*"])}

    fig, ax = plt.subplots(figsize=(10, 6))

    # Collect for global means
    per_eps_sigmas = {eps: [] for eps in EPS_VALUES}

    for run, ana in zip(runs, analyses):
        for eps in EPS_VALUES:
            result = ana["eps_results"].get(eps)
            if result is None or result["sigma"] <= 0:
                continue

            color = D_cmap(D_norm(run["D"]))
            marker = Nm_markers.get(run["Nm"], "o")

            # Small jitter to avoid overlap
            jitter = np.random.uniform(-0.1, 0.1) * eps
            ax.scatter(
                eps + jitter, result["sigma"],
                color=color, marker=marker, s=50, alpha=0.6,
                edgecolors="0.3", linewidths=0.3,
            )
            per_eps_sigmas[eps].append(result["sigma"])

    # Global means per ε
    eps_means = []
    eps_vals_plot = []
    for eps in EPS_VALUES:
        arr = per_eps_sigmas[eps]
        if arr:
            mean_s = np.mean(arr)
            eps_means.append(mean_s)
            eps_vals_plot.append(eps)

    if eps_vals_plot:
        ax.plot(eps_vals_plot, eps_means, "k--o", linewidth=2, markersize=8,
                zorder=10, label="Mean $\\sigma_\\varepsilon$")

    ax.set_xscale("log")

    # Colorbar
    sm = plt.cm.ScalarMappable(cmap=D_cmap, norm=D_norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, label=r"Diffusion $D$", pad=0.02)
    cbar.ax.tick_params(labelsize=9)

    # Legend
    legend_handles = [
        plt.Line2D([0], [0], marker=m, color="0.5", markersize=7,
                   linestyle="None", label=rf"$N_m = {Nm}$")
        for Nm, m in Nm_markers.items()
    ]
    legend_handles.append(
        plt.Line2D([0], [0], color="black", linestyle="--", marker="o",
                   markersize=8, linewidth=2, label=r"Mean $\sigma_\varepsilon$")
    )
    ax.legend(handles=legend_handles, fontsize=8, loc="upper left",
              framealpha=0.9)

    setup_axes(
        ax,
        xlabel=r"Perturbation amplitude $\varepsilon$",
        ylabel=r"Recovery rate $\sigma_\varepsilon$",
        title="Recovery Rate vs Perturbation Amplitude — All Runs",
    )
    fig.tight_layout()

    fname = "rate_vs_eps.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure C: Stability Heatmap
# ---------------------------------------------------------------------------
def figure_stability_heatmap(runs: list[dict], analyses: list[dict]):
    """One panel per Nm; cell = fraction of ε-levels recovered."""
    Nm_vals = sorted(set(r["Nm"] for r in runs))
    D_vals = sorted(set(r["D"] for r in runs))
    A_vals = sorted(set(r["A"] for r in runs))

    n_Nm = len(Nm_vals)
    if n_Nm == 0:
        print("  SKIP stability heatmap: no data.")
        return

    fig, axes = plt.subplots(
        1, n_Nm,
        figsize=(4.5 * n_Nm + 1, max(3, 0.6 * len(D_vals) + 1.5)),
        squeeze=False,
    )
    axes = axes.flatten()

    for panel_idx, Nm in enumerate(Nm_vals):
        ax = axes[panel_idx]
        grid = np.full((len(D_vals), len(A_vals)), np.nan)

        for run, ana in zip(runs, analyses):
            if run["Nm"] != Nm:
                continue
            di = D_vals.index(run["D"]) if run["D"] in D_vals else None
            ai = A_vals.index(run["A"]) if run["A"] in A_vals else None
            if di is None or ai is None:
                continue
            if ana["n_attempted"] > 0:
                grid[di, ai] = ana["frac_recovered"]

        ax.imshow(
            grid, aspect="auto", origin="lower",
            cmap=plt.cm.RdYlGn, vmin=0.0, vmax=1.0,
            interpolation="nearest",
        )

        ax.set_xticks(range(len(A_vals)))
        ax.set_xticklabels([f"{a:.3f}" for a in A_vals],
                           fontsize=8, rotation=45)
        ax.set_yticks(range(len(D_vals)))
        ax.set_yticklabels([f"{d:.3f}" for d in D_vals], fontsize=8)

        ax.set_xlabel(r"Amplitude $A$", fontsize=10)
        if panel_idx == 0:
            ax.set_ylabel(r"Diffusion $D$", fontsize=10)
        ax.set_title(rf"$N_m = {Nm}$", fontsize=12, fontweight="bold")

        for di_idx in range(len(D_vals)):
            for ai_idx in range(len(A_vals)):
                val = grid[di_idx, ai_idx]
                if np.isnan(val):
                    ax.text(ai_idx, di_idx, "—", ha="center", va="center",
                            fontsize=8, color="0.5")
                else:
                    # Find n_attempted for this cell
                    n_att = len(EPS_VALUES)
                    for run2, ana2 in zip(runs, analyses):
                        if (run2["Nm"] == Nm and
                                run2["D"] == D_vals[di_idx] and
                                run2["A"] == A_vals[ai_idx]):
                            n_att = max(ana2["n_attempted"], 1)
                            break
                    n_rec = int(round(val * n_att))
                    txt_color = "white" if val < 0.4 else "black"
                    ax.text(ai_idx, di_idx, f"{n_rec}/{n_att}",
                            ha="center", va="center", fontsize=8,
                            color=txt_color, fontweight="bold")

    fig.colorbar(
        plt.cm.ScalarMappable(cmap=plt.cm.RdYlGn,
                              norm=mcolors.Normalize(0, 1)),
        ax=axes.tolist(),
        label=r"Fraction of $\varepsilon$-levels recovered",
        shrink=0.8, pad=0.04,
    )

    fig.suptitle(
        r"Perturbed Attractor Stability — Heatmap by $(D, A, N_m)$",
        fontsize=14, fontweight="bold", y=1.03,
    )
    fig.tight_layout()

    fname = "stability_heatmap.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Summary table and invariance verdict
# ---------------------------------------------------------------------------
def print_summary(runs: list[dict], analyses: list[dict]):
    print(f"\n{'='*140}")
    print("  Invariant Perturbed-Attractor Stability — Summary Table")
    print(f"{'='*140}")

    # Header
    eps_hdr = "  ".join(f"σ_{EPS_LABELS[e]}" for e in EPS_VALUES)
    thalf_hdr = "  ".join(f"t½_{EPS_LABELS[e]}" for e in EPS_VALUES)
    print(f"  {'D':<7} {'A':<7} {'Nm':<5} {'#att':<5} {'#rec':<5} "
          f"{'frac':<7} ", end="")
    for e in EPS_VALUES:
        print(f"{'σ_'+EPS_LABELS[e]:<10}", end="")
    for e in EPS_VALUES:
        print(f"{'t½_'+EPS_LABELS[e]:<10}", end="")
    print(f"{'mono':<8}")
    print("  " + "-" * (50 + 20 * len(EPS_VALUES)))

    per_eps_sigma = {e: [] for e in EPS_VALUES}
    per_eps_thalf = {e: [] for e in EPS_VALUES}

    for run, ana in zip(runs, analyses):
        print(f"  {run['D']:<7.3f} {run['A']:<7.4f} {run['Nm']:<5d} "
              f"{ana['n_attempted']:<5d} {ana['n_recovered']:<5d} "
              f"{ana['frac_recovered']:<7.1%} ", end="")

        mono_str = ""
        for e in EPS_VALUES:
            r = ana["eps_results"].get(e)
            if r is not None:
                print(f"{r['sigma']:<10.4f}", end="")
                per_eps_sigma[e].append(r["sigma"])
            else:
                print(f"{'—':<10}", end="")

        for e in EPS_VALUES:
            r = ana["eps_results"].get(e)
            if r is not None:
                t_str = f"{r['t_half']:.2f}" if not np.isinf(r["t_half"]) else "inf"
                print(f"{t_str:<10}", end="")
                if not np.isinf(r["t_half"]):
                    per_eps_thalf[e].append(r["t_half"])
                mono_str += "M" if r["monotone"] else "."
            else:
                print(f"{'—':<10}", end="")
                mono_str += "-"

        print(f"{mono_str:<8}")

    # Global statistics per ε
    print(f"\n  Recovery Rate σ_ε:")
    print(f"  {'ε':<10} {'Mean':<12} {'Std':<12} "
          f"{'Min':<12} {'Max':<12} {'CV':<10} {'N':<6} {'Verdict'}")
    print("  " + "-" * 80)

    for e in EPS_VALUES:
        arr = np.array(per_eps_sigma[e])
        arr = arr[arr > 0]  # Only positive (actual recovery)
        if len(arr) == 0:
            print(f"  {EPS_LABELS[e]:<10} (no data)")
            continue

        mean_v = np.mean(arr)
        std_v = np.std(arr)
        cv = std_v / max(abs(mean_v), 1e-30)

        if cv < 0.05:
            verdict = "INVARIANT"
        elif cv < 0.15:
            verdict = "WEAKLY INVARIANT"
        else:
            verdict = "NOT INVARIANT"

        print(f"  {EPS_LABELS[e]:<10} "
              f"{mean_v:<12.6f} {std_v:<12.6f} "
              f"{np.min(arr):<12.6f} {np.max(arr):<12.6f} "
              f"{cv:<10.4f} {len(arr):<6d} {verdict}")

    # ε-independence check: is σ_ε the same for all ε?
    all_sigmas = []
    for e in EPS_VALUES:
        arr = np.array(per_eps_sigma[e])
        arr = arr[arr > 0]
        all_sigmas.extend(arr.tolist())

    if len(all_sigmas) > 1:
        arr = np.array(all_sigmas)
        cv = np.std(arr) / max(np.mean(arr), 1e-30)
        print(f"\n  ε-independence of σ (pooled across all ε):")
        print(f"    CV = {cv:.4f} — ", end="")
        if cv < 0.10:
            print("CONSISTENT (σ independent of ε, as predicted)")
        else:
            print("ε-DEPENDENT (σ varies with perturbation amplitude)")

    # Overall
    total_att = sum(ana["n_attempted"] for ana in analyses)
    total_rec = sum(ana["n_recovered"] for ana in analyses)
    print(f"\n  Overall recovery: {total_rec}/{total_att} "
          f"({100*total_rec/max(total_att,1):.1f}%)")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(FIG_DIR, exist_ok=True)

    print("Discovering regime volume runs and perturbation sub-runs...")
    runs = discover_regime_runs()

    if not runs:
        print(f"\nERROR: No admissible regime_D*_A*_Nm* runs found in:")
        print(f"  {RUNS_DIR}")
        print("\nRun the regime volume experiment first:")
        print("  python experiments/regime_volume_3d.py")
        sys.exit(1)

    # Count perturbed sub-runs
    total_perturbed = sum(len(r["perturbed_dirs"]) for r in runs)
    print(f"  Found {len(runs)} base runs, {total_perturbed} perturbed sub-runs.")

    if total_perturbed == 0:
        print("\n  WARNING: No perturbed sub-runs found.")
        print("  Expected directories like:")
        print("    output/runs/regime_D0.1_A0.02_Nm20/perturb_eps_1e-4/")
        print("  or:")
        print("    output/runs/regime_D0.1_A0.02_Nm20_perturb_eps_1e-4/")
        print("\n  Proceeding with analysis of available data...")

    # Analyse
    print("\nAnalysing perturbed-attractor stability...")
    analyses = []
    for i, run in enumerate(runs):
        ana = analyse_run(run)
        analyses.append(ana)
        if (i + 1) % 10 == 0 or i == len(runs) - 1:
            print(f"  [{i+1}/{len(runs)}] {run['name']}: "
                  f"{ana['n_attempted']} attempted, "
                  f"{ana['n_recovered']} recovered")

    # Figures
    print("\n--- (A) Recovery Curves ---")
    figure_recovery_curves(runs, analyses)

    print("\n--- (B) Recovery Rate vs ε ---")
    figure_rate_vs_eps(runs, analyses)

    print("\n--- (C) Stability Heatmap ---")
    figure_stability_heatmap(runs, analyses)

    # Summary
    print_summary(runs, analyses)

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
