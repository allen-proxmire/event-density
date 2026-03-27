"""
invariant_spectral_complexity.py
=================================
Experiment / Analysis: Invariant Spectral Complexity (Rényi Entropy)

Scans all completed regime_D*_A*_Nm* runs, computes the Rényi entropies

    H_q(t) = (1/(1−q)) log( Σ_k p_k(t)^q )

for q ∈ {0, 0.5, 1, 2, 3, 4} where p_k = |a_k|²/Σ_j|a_j|² is the
normalised modal energy distribution (k ≥ 1), and analyses their
convergence toward late-time attractor values H_q^*.

The Rényi entropy family provides a multi-scale probe of spectral
complexity:
  q = 0  →  log(#active modes)   (Hartley / support size)
  q = 1  →  Shannon entropy       (information content)
  q = 2  →  −log(participation ratio)  (inverse participation)
  q > 2  →  sensitivity to dominant modes

Their attractor values are structural invariants of the ED architecture
(Appendix C.4–C.5), and their ratios encode the spectral shape beyond
what any single entropy measure captures.

Produces:
  (A) Spectral Complexity Evolution — H_q(t) for a representative run.
  (B) Attractor Complexity Profile — H_q^* vs D for all runs.
  (C) Convergence Heatmap — fraction converged per q.

All figures saved to output/figures/invariants/spectral_complexity/
as PNG (300 dpi).

Usage:
    python experiments/invariant_spectral_complexity.py

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
                        "spectral_complexity")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
Q_VALUES = [0.0, 0.5, 1.0, 2.0, 3.0, 4.0]
LATE_FRAC = 0.10
FIT_FRAC = 0.20
R2_THRESH = 0.95
LOG_FLOOR = 1e-30

# Active-mode threshold for q = 0 (Hartley entropy)
HARTLEY_THRESH = 1e-20

Q_COLORS = {
    0.0: "#1b9e77", 0.5: "#d95f02", 1.0: "#7570b3",
    2.0: "#e7298a", 3.0: "#66a61e", 4.0: "#e6ab02",
}
Q_LABELS = {
    0.0: r"$H_0$ (Hartley)",
    0.5: r"$H_{0.5}$",
    1.0: r"$H_1$ (Shannon)",
    2.0: r"$H_2$ (Rényi-2)",
    3.0: r"$H_3$",
    4.0: r"$H_4$",
}


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------
def discover_regime_runs() -> list[dict]:
    """Scan RUNS_DIR for regime_D*_A*_Nm* folders with modal data."""
    pattern = os.path.join(RUNS_DIR, "regime_D*_A*_Nm*")
    dirs = sorted(glob.glob(pattern))

    runs = []
    for d in dirs:
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

        runs.append({
            "dir": d,
            "name": name,
            "D": float(D_val),
            "A": float(A_val),
            "Nm": int(Nm_val),
            "metadata": meta,
            "t": t[:n],
            "modal": modal[:n],
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
# Rényi entropy computation
# ---------------------------------------------------------------------------
def _compute_renyi(p: np.ndarray, q: float) -> np.ndarray:
    """Compute Rényi entropy H_q for each row of the distribution matrix p.

    Parameters
    ----------
    p : ndarray, shape (n_steps, n_modes)
        Normalised modal energy distribution (rows sum to 1).
    q : float
        Rényi order.

    Returns
    -------
    H : ndarray, shape (n_steps,)
    """
    if abs(q - 1.0) < 1e-12:
        # Shannon limit: H_1 = −Σ p_k log p_k
        log_p = np.log(p + LOG_FLOOR)
        return -np.sum(p * log_p, axis=1)

    if abs(q) < 1e-12:
        # Hartley entropy: H_0 = log(|support|)
        support = np.sum(p > HARTLEY_THRESH, axis=1).astype(np.float64)
        return np.log(np.maximum(support, 1.0))

    # General case: H_q = (1/(1−q)) log(Σ p_k^q)
    p_q = np.power(p + LOG_FLOOR, q)
    sum_p_q = np.sum(p_q, axis=1)
    return np.log(np.maximum(sum_p_q, LOG_FLOOR)) / (1.0 - q)


# ---------------------------------------------------------------------------
# Per-run analysis (streaming over q values)
# ---------------------------------------------------------------------------
def analyse_run(run: dict) -> dict:
    """Compute Rényi entropies and attractor summaries for all q.

    Computes the normalised distribution p once (same size as modal[:,1:]),
    then streams through q values.
    """
    modal = run["modal"]
    t = run["t"]
    n_steps, n_modes = modal.shape

    # Modal energies for k >= 1
    E = modal[:, 1:] ** 2                           # (n_steps, n_modes-1)
    E_total = np.sum(E, axis=1, keepdims=True)       # (n_steps, 1)
    E_total = np.maximum(E_total, LOG_FLOOR)
    p = E / E_total                                   # (n_steps, n_modes-1)

    del E, E_total  # free

    entropies = {}
    n_converged = 0

    for q in Q_VALUES:
        H = _compute_renyi(p, q)

        # Late-time average
        start = max(0, int((1.0 - LATE_FRAC) * len(H)))
        H_star = float(np.mean(H[start:]))

        # Convergence fit
        fit = _fit_exponential(t[:len(H)], H, H_star)

        entropies[q] = {
            "H_star": H_star,
            "sigma": fit["sigma"],
            "R2": fit["R2"],
            "converged": fit["converged"],
        }
        if fit["converged"]:
            n_converged += 1

        del H

    del p

    frac = n_converged / max(len(Q_VALUES), 1)

    return {
        "entropies": entropies,
        "n_converged": n_converged,
        "frac_converged": frac,
    }


def _fit_exponential(t: np.ndarray, arr: np.ndarray,
                     target: float) -> dict:
    """Fit |arr(t) - target| ~ C exp(-sigma t) over the last FIT_FRAC."""
    result = {"sigma": 0.0, "R2": 0.0, "converged": False}

    n = len(t)
    start = max(0, int((1.0 - FIT_FRAC) * n))
    t_fit = t[start:]
    residual = np.abs(arr[start:] - target)

    valid = residual > 1e-30
    if np.sum(valid) < 10:
        return result

    log_r = np.log(residual[valid])
    t_v = t_fit[valid]

    try:
        coeffs = np.polyfit(t_v, log_r, 1)
        sigma = -coeffs[0]

        predicted = coeffs[0] * t_v + coeffs[1]
        ss_res = np.sum((log_r - predicted) ** 2)
        ss_tot = np.sum((log_r - np.mean(log_r)) ** 2)
        R2 = 1.0 - ss_res / max(ss_tot, 1e-30)

        result["sigma"] = float(sigma)
        result["R2"] = float(R2)
        result["converged"] = R2 > R2_THRESH and sigma > 0
    except (np.linalg.LinAlgError, ValueError):
        pass

    return result


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
# Figure A: Spectral Complexity Evolution (representative run)
# ---------------------------------------------------------------------------
def figure_complexity_evolution(runs: list[dict], analyses: list[dict]):
    """Plot H_q(t) for all q for the run with largest Nm.

    Recomputes entropies on-the-fly.
    """
    best_idx = max(range(len(runs)), key=lambda i: runs[i]["Nm"])
    run = runs[best_idx]
    ana = analyses[best_idx]

    t = run["t"]
    modal = run["modal"]

    E = modal[:, 1:] ** 2
    E_total = np.maximum(np.sum(E, axis=1, keepdims=True), LOG_FLOOR)
    p = E / E_total
    del E, E_total

    fig, ax = plt.subplots(figsize=(10, 6))

    for q in Q_VALUES:
        H = _compute_renyi(p, q)
        H_star = ana["entropies"][q]["H_star"]
        color = Q_COLORS[q]

        ax.plot(
            t[:len(H)], H,
            color=color, linewidth=1.4,
            label=Q_LABELS[q],
        )

        if H_star > 1e-10:
            ax.axhline(
                H_star, color=color, linestyle="--",
                linewidth=0.8, alpha=0.5,
            )

        del H

    del p

    setup_axes(
        ax,
        xlabel=r"Time $t$",
        ylabel=r"Rényi entropy $H_q(t)$",
        title=(f"Spectral Complexity — D={run['D']}, A={run['A']}, "
               f"Nm={run['Nm']}"),
    )
    ax.legend(fontsize=9, loc="center right", framealpha=0.9)
    ax.set_ylim(bottom=0)
    fig.tight_layout()

    fname = "complexity_evolution.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure B: Attractor Complexity Profile (H_q^* vs D)
# ---------------------------------------------------------------------------
def figure_attractor_profile(runs: list[dict], analyses: list[dict]):
    """One panel per q: H_q^* vs D."""
    A_vals = sorted(set(r["A"] for r in runs))
    Nm_vals = sorted(set(r["Nm"] for r in runs))

    A_cmap = plt.cm.viridis
    A_norm = mcolors.Normalize(
        vmin=min(A_vals) * 0.8 if A_vals else 0,
        vmax=max(A_vals) * 1.2 if A_vals else 1,
    )
    Nm_markers = {Nm_vals[i]: m for i, m in
                  zip(range(len(Nm_vals)),
                      ["o", "s", "^", "D", "v", "P", "*"])}

    n_q = len(Q_VALUES)
    n_cols = min(3, n_q)
    n_rows = (n_q + n_cols - 1) // n_cols

    fig, axes = plt.subplots(
        n_rows, n_cols,
        figsize=(5 * n_cols, 4 * n_rows),
        squeeze=False,
    )

    for panel_idx, q in enumerate(Q_VALUES):
        row, col = divmod(panel_idx, n_cols)
        ax = axes[row][col]

        all_H = [ana["entropies"][q]["H_star"]
                 for ana in analyses
                 if not np.isnan(ana["entropies"][q]["H_star"])]
        global_mean = np.mean(all_H) if all_H else np.nan

        for run, ana in zip(runs, analyses):
            H_star = ana["entropies"][q]["H_star"]
            if np.isnan(H_star):
                continue

            color = A_cmap(A_norm(run["A"]))
            marker = Nm_markers.get(run["Nm"], "o")

            ax.scatter(
                run["D"], H_star,
                color=color, marker=marker, s=40, alpha=0.7,
                edgecolors="0.3", linewidths=0.3,
            )

        if not np.isnan(global_mean):
            ax.axhline(global_mean, color="0.4", linestyle="--",
                       linewidth=0.9, alpha=0.5)

        setup_axes(
            ax,
            xlabel=r"$D$" if row == n_rows - 1 else "",
            ylabel=Q_LABELS[q] + r"$^*$" if col == 0 else "",
            title=Q_LABELS[q],
        )

    # Hide unused panels
    for panel_idx in range(n_q, n_rows * n_cols):
        r, c = divmod(panel_idx, n_cols)
        axes[r][c].set_visible(False)

    # Colorbar
    sm = plt.cm.ScalarMappable(cmap=A_cmap, norm=A_norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=axes.tolist(), label=r"Amplitude $A$",
                        shrink=0.7, pad=0.03)
    cbar.ax.tick_params(labelsize=9)

    # Marker legend
    legend_handles = [
        plt.Line2D([0], [0], marker=m, color="0.5", markersize=7,
                   linestyle="None", label=rf"$N_m = {Nm}$")
        for Nm, m in Nm_markers.items()
    ]
    axes[0][-1].legend(
        handles=legend_handles, fontsize=7, loc="upper right",
        framealpha=0.9, title="Seed count",
    )

    fig.suptitle(
        "Spectral Complexity Attractor — All Admissible Runs",
        fontsize=14, fontweight="bold", y=1.01,
    )
    fig.tight_layout()

    fname = "attractor_profile.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure C: Convergence Heatmap (one panel per q)
# ---------------------------------------------------------------------------
def figure_convergence_heatmap(runs: list[dict], analyses: list[dict]):
    """One panel per q; cell = fraction of Nm converged at each (D, A)."""
    D_vals = sorted(set(r["D"] for r in runs))
    A_vals = sorted(set(r["A"] for r in runs))
    Nm_vals = sorted(set(r["Nm"] for r in runs))

    n_q = len(Q_VALUES)
    n_cols = min(3, n_q)
    n_rows = (n_q + n_cols - 1) // n_cols

    fig, axes = plt.subplots(
        n_rows, n_cols,
        figsize=(4.2 * n_cols + 1.5,
                 max(3, 0.55 * len(D_vals) + 1.5) * n_rows),
        squeeze=False,
    )

    for panel_idx, q in enumerate(Q_VALUES):
        row, col = divmod(panel_idx, n_cols)
        ax = axes[row][col]

        conv_count = np.zeros((len(D_vals), len(A_vals)))
        total_count = np.zeros((len(D_vals), len(A_vals)))

        for run, ana in zip(runs, analyses):
            di = D_vals.index(run["D"]) if run["D"] in D_vals else None
            ai = A_vals.index(run["A"]) if run["A"] in A_vals else None
            if di is None or ai is None:
                continue
            total_count[di, ai] += 1
            if ana["entropies"][q]["converged"]:
                conv_count[di, ai] += 1

        with np.errstate(invalid="ignore"):
            grid = np.where(total_count > 0,
                            conv_count / total_count, np.nan)

        ax.imshow(
            grid, aspect="auto", origin="lower",
            cmap=plt.cm.RdYlGn, vmin=0.0, vmax=1.0,
            interpolation="nearest",
        )

        ax.set_xticks(range(len(A_vals)))
        ax.set_xticklabels([f"{a:.3f}" for a in A_vals],
                           fontsize=7, rotation=45)
        ax.set_yticks(range(len(D_vals)))
        ax.set_yticklabels([f"{d:.3f}" for d in D_vals], fontsize=7)

        if row == n_rows - 1:
            ax.set_xlabel(r"$A$", fontsize=9)
        if col == 0:
            ax.set_ylabel(r"$D$", fontsize=9)

        q_label = f"q={q:g}"
        ax.set_title(q_label, fontsize=11, fontweight="bold")

        for di_idx in range(len(D_vals)):
            for ai_idx in range(len(A_vals)):
                tot = int(total_count[di_idx, ai_idx])
                if tot == 0:
                    ax.text(ai_idx, di_idx, "—", ha="center", va="center",
                            fontsize=7, color="0.5")
                else:
                    cv = int(conv_count[di_idx, ai_idx])
                    val = grid[di_idx, ai_idx]
                    txt_color = "white" if val < 0.4 else "black"
                    ax.text(ai_idx, di_idx, f"{cv}/{tot}", ha="center",
                            va="center", fontsize=7, color=txt_color,
                            fontweight="bold")

    # Hide unused
    for panel_idx in range(n_q, n_rows * n_cols):
        r, c = divmod(panel_idx, n_cols)
        axes[r][c].set_visible(False)

    fig.colorbar(
        plt.cm.ScalarMappable(cmap=plt.cm.RdYlGn,
                              norm=mcolors.Normalize(0, 1)),
        ax=axes.tolist(),
        label="Fraction converged (across $N_m$)",
        shrink=0.7, pad=0.04,
    )

    fig.suptitle(
        r"Spectral Complexity Convergence — Heatmap per $q$",
        fontsize=14, fontweight="bold", y=1.02,
    )
    fig.tight_layout()

    fname = "convergence_heatmap.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Summary table and invariance verdict
# ---------------------------------------------------------------------------
def print_summary(runs: list[dict], analyses: list[dict]):
    print(f"\n{'='*130}")
    print("  Invariant Spectral Complexity (Rényi) — Summary Table")
    print(f"{'='*130}")

    q_hdr = "  ".join(f"H_{q:g}*" for q in Q_VALUES)
    print(f"  {'D':<7} {'A':<7} {'Nm':<5} "
          f"{'Conv':<8} {'Frac':<7} ", end="")
    for q in Q_VALUES:
        print(f"{'H_'+str(q)+'*':<12}", end="")
    print()
    print("  " + "-" * (45 + 12 * len(Q_VALUES)))

    all_H = {q: [] for q in Q_VALUES}

    for run, ana in zip(runs, analyses):
        ent = ana["entropies"]

        conv_str = ""
        for q in Q_VALUES:
            conv_str += "+" if ent[q]["converged"] else "."

        print(f"  {run['D']:<7.3f} {run['A']:<7.4f} {run['Nm']:<5d} "
              f"{conv_str:<8} {ana['frac_converged']:<7.1%} ", end="")

        for q in Q_VALUES:
            H_s = ent[q]["H_star"]
            print(f"{H_s:<12.6f}", end="")
            if not np.isnan(H_s):
                all_H[q].append(H_s)
        print()

    # --- Global statistics per q ---
    print(f"\n  {'Order q':<10} {'Mean':<14} {'Std':<14} "
          f"{'Min':<14} {'Max':<14} {'CV':<10} {'Verdict'}")
    print("  " + "-" * 82)

    for q in Q_VALUES:
        arr = np.array(all_H[q])
        if len(arr) == 0:
            print(f"  q={q:<7g} (no data)")
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

        print(f"  q={q:<7g} "
              f"{mean_v:<14.6f} {std_v:<14.6f} "
              f"{np.min(arr):<14.6f} {np.max(arr):<14.6f} "
              f"{cv:<10.4f} {verdict}")

    # Monotonicity check: H_0 >= H_0.5 >= H_1 >= H_2 >= ...
    means = {q: np.mean(all_H[q]) for q in Q_VALUES if len(all_H[q]) > 0}
    sorted_q = sorted(means.keys())
    monotone = all(
        means[sorted_q[i]] >= means[sorted_q[i + 1]] - 1e-8
        for i in range(len(sorted_q) - 1)
    )
    print(f"\n  Rényi monotonicity (H_q decreasing in q): "
          f"{'PASS' if monotone else 'FAIL'}")

    # Overall convergence
    total = len(runs) * len(Q_VALUES)
    total_conv = sum(ana["n_converged"] for ana in analyses)
    print(f"  Overall convergence: {total_conv}/{total} "
          f"({100*total_conv/max(total,1):.1f}%)")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(FIG_DIR, exist_ok=True)

    print("Discovering regime volume runs...")
    runs = discover_regime_runs()

    if not runs:
        print(f"\nERROR: No admissible regime_D*_A*_Nm* runs found in:")
        print(f"  {RUNS_DIR}")
        print("\nRun the regime volume experiment first:")
        print("  python experiments/regime_volume_3d.py")
        sys.exit(1)

    print(f"  Found {len(runs)} admissible runs.")
    print(f"  D range:  {min(r['D'] for r in runs):.3f} – "
          f"{max(r['D'] for r in runs):.3f}")
    print(f"  A range:  {min(r['A'] for r in runs):.4f} – "
          f"{max(r['A'] for r in runs):.4f}")
    print(f"  Nm range: {min(r['Nm'] for r in runs)} – "
          f"{max(r['Nm'] for r in runs)}")

    # --- Analyse all runs ---
    q_str = ", ".join(f"{q:g}" for q in Q_VALUES)
    print(f"\nComputing Rényi entropies (q ∈ {{{q_str}}})...")
    analyses = []
    for i, run in enumerate(runs):
        ana = analyse_run(run)
        analyses.append(ana)
        if (i + 1) % 10 == 0 or i == len(runs) - 1:
            n_c = ana["n_converged"]
            print(f"  [{i+1}/{len(runs)}] {run['name']}: "
                  f"{n_c}/{len(Q_VALUES)} converged")

    # --- Figures ---
    print("\n--- (A) Spectral Complexity Evolution ---")
    figure_complexity_evolution(runs, analyses)

    print("\n--- (B) Attractor Complexity Profile ---")
    figure_attractor_profile(runs, analyses)

    print("\n--- (C) Convergence Heatmap ---")
    figure_convergence_heatmap(runs, analyses)

    # --- Summary ---
    print_summary(runs, analyses)

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
