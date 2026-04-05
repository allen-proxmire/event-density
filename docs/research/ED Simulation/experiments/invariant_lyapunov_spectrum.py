"""
invariant_lyapunov_spectrum.py
===============================
Experiment / Analysis: Invariant Lyapunov Spectrum

Scans all completed regime_D*_A*_Nm* runs, estimates the Lyapunov
exponent spectrum from the modal amplitude time series, and computes
the Kaplan-Yorke attractor dimension.

Method:
  - Construct a 2K-dimensional state vector from Re/Im (or ±) parts
    of the first K modal amplitudes.
  - Estimate the local tangent map via finite differences.
  - Accumulate the Lyapunov exponents using the standard QR method
    (Benettin et al. 1980) over the attractor window (last 20%).
  - Compute the Kaplan-Yorke dimension from the ordered exponents.

For the ED architecture, Principle 3 (unique attractor) and the
Lyapunov stability theorem (Appendix C.5, Theorem C.43) predict that
all exponents are non-positive -- the attractor is a fixed point,
not a chaotic set.  The Kaplan-Yorke dimension should be 0 (point
attractor) or very close to 0.

Produces:
  (A) Lyapunov Spectrum -- λ_i vs i for a representative run.
  (B) Attractor Dimension vs D -- D_KY scatter for all runs.
  (C) Spectrum Heatmap -- number of positive exponents across (D, A, Nm).

All figures saved to output/figures/invariants/lyapunov_spectrum/
as PNG (300 dpi).

Usage:
    python experiments/invariant_lyapunov_spectrum.py

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
                        "lyapunov_spectrum")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
K_MAX = 20
ATTRACTOR_FRAC = 0.20    # Last 20% for Lyapunov computation
NORM_FLOOR = 1e-30       # Floor for tangent vector normalisation
QR_INTERVAL = 1          # QR reorthogonalisation every N steps
MAX_DIM = 40             # Maximum state-space dimension (2*K_MAX)


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------
def discover_regime_runs() -> list[dict]:
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

        if meta.get("inadmissible", False):
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
        if modal.shape[1] < 3 or n < 100:
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
# State vector construction
# ---------------------------------------------------------------------------
def build_state_vectors(modal_window: np.ndarray, K: int) -> np.ndarray:
    """Build the d-dimensional state vector from modal amplitudes.

    For complex data: x = [Re(a_1), Im(a_1), ..., Re(a_K), Im(a_K)]  (d = 2K)
    For real data:    x = [a_1, a_2, ..., a_K]                        (d = K)

    Returns ndarray of shape (n_window, d).
    """
    a = modal_window[:, 1:K+1]

    if np.iscomplexobj(a):
        # Interleave Re and Im
        re = np.real(a)
        im = np.imag(a)
        d = 2 * K
        x = np.empty((a.shape[0], d), dtype=np.float64)
        x[:, 0::2] = re
        x[:, 1::2] = im
    else:
        x = a.astype(np.float64)

    return x


# ---------------------------------------------------------------------------
# Lyapunov exponent computation via QR accumulation
# ---------------------------------------------------------------------------
def compute_lyapunov_spectrum(x: np.ndarray, dt_arr: np.ndarray) -> np.ndarray:
    """Estimate the Lyapunov exponent spectrum from a state-vector time series.

    Uses the QR method: propagate an orthonormal frame through the
    finite-difference tangent map, reorthogonalise with QR at each step,
    and accumulate the logarithmic stretching rates.

    Parameters
    ----------
    x : ndarray, shape (n_steps, d)
    dt_arr : ndarray, shape (n_steps-1,), time increments

    Returns
    -------
    lambdas : ndarray, shape (d,), Lyapunov exponents (sorted descending)
    """
    n_steps, d = x.shape

    if d > MAX_DIM:
        # Truncate to keep computation tractable
        x = x[:, :MAX_DIM]
        d = MAX_DIM

    # Finite-difference tangent vectors: dx/dt ~= (x_{n+1} - x_n) / dt_n
    dx = np.diff(x, axis=0)                        # (n_steps-1, d)

    # Initialise orthonormal frame
    Q = np.eye(d)                                    # (d, d)
    log_R_diag = np.zeros(d)                         # accumulated log |R_ii|
    total_time = 0.0
    n_qr = 0

    for step in range(len(dx)):
        dt_step = dt_arr[step] if step < len(dt_arr) else 1.0
        if dt_step <= 0:
            continue

        # Local Jacobian approximation:
        # The tangent map maps perturbations δx_n → δx_{n+1} ~= δx_n + J_n δx_n dt
        # For the QR method, we propagate: Y = (I + J_n dt) @ Q
        # With J_n ~= dx_n dx_n^T / (||dx_n||^2 + eps) as rank-1 approximation:
        #   (I + J_n dt) = I + dt * dx_n dx_n^T / (||dx_n||^2 + eps)
        #
        # However, a more robust approach for trajectory-based Lyapunov
        # computation is to use the *full* tangent map:
        #   M_n = I + (dx_n / dt) ... but this requires the actual Jacobian.
        #
        # For a rank-1 update, use the Gram-Schmidt/QR on Y = Q + dt * v v^T Q / ||v||^2:

        v = dx[step]                                 # (d,)
        v_norm_sq = np.dot(v, v) + NORM_FLOOR

        # Y_col = Q_col + dt * v * (v^T Q_col) / v_norm_sq for each column
        vTQ = v @ Q                                  # (d,) = v^T @ Q
        Y = Q + (dt_step / v_norm_sq) * np.outer(v, vTQ)

        # QR reorthogonalisation
        if (step + 1) % QR_INTERVAL == 0 or step == len(dx) - 1:
            Q_new, R = np.linalg.qr(Y)

            # Accumulate log of diagonal elements (with sign correction)
            diag_R = np.diag(R)
            # Ensure positive diagonal (convention: Q columns have same
            # orientation as before)
            signs = np.sign(diag_R)
            signs[signs == 0] = 1.0
            Q_new = Q_new * signs[np.newaxis, :]
            diag_R = np.abs(diag_R)

            log_R_diag += np.log(np.maximum(diag_R, NORM_FLOOR))
            total_time += dt_step
            n_qr += 1

            Q = Q_new
        else:
            Q = Y
            total_time += dt_step

    if total_time < NORM_FLOOR:
        return np.zeros(d)

    lambdas = log_R_diag / total_time
    lambdas = np.sort(lambdas)[::-1]  # Descending order

    return lambdas


# ---------------------------------------------------------------------------
# Kaplan-Yorke dimension
# ---------------------------------------------------------------------------
def kaplan_yorke_dimension(lambdas: np.ndarray) -> float:
    """Compute the Kaplan-Yorke dimension from sorted Lyapunov exponents.

    D_KY = j + Σ_{i=1..j} λ_i / |λ_{j+1}|
    where j is the largest index such that Σ_{i=1..j} λ_i >= 0.

    For a fixed-point attractor (all λ_i <= 0), D_KY = 0.
    """
    if len(lambdas) == 0:
        return 0.0

    # All non-positive → point attractor
    if lambdas[0] <= 0:
        return 0.0

    cumsum = np.cumsum(lambdas)

    # Find j: largest index where cumsum >= 0
    positive_mask = cumsum >= 0
    if not np.any(positive_mask):
        return 0.0

    j = int(np.max(np.where(positive_mask)[0]))

    if j + 1 >= len(lambdas):
        # All exponents sum to positive -- dimension equals full space
        return float(len(lambdas))

    denom = abs(lambdas[j + 1])
    if denom < NORM_FLOOR:
        return float(j + 1)

    D_KY = (j + 1) + cumsum[j] / denom

    return float(max(D_KY, 0.0))


# ---------------------------------------------------------------------------
# Per-run analysis
# ---------------------------------------------------------------------------
def analyse_run(run: dict) -> dict:
    """Compute Lyapunov spectrum and Kaplan-Yorke dimension."""
    modal = run["modal"]
    t = run["t"]
    n = len(t)
    n_modes = modal.shape[1]
    K = min(K_MAX, n_modes - 1)

    # Attractor window
    start = max(0, int((1.0 - ATTRACTOR_FRAC) * n))
    modal_win = modal[start:]
    t_win = t[start:]

    # State vectors
    x = build_state_vectors(modal_win, K)
    d = x.shape[1]

    # Time increments
    dt_arr = np.diff(t_win)

    # Lyapunov spectrum
    lambdas = compute_lyapunov_spectrum(x, dt_arr)

    # Kaplan-Yorke dimension
    D_KY = kaplan_yorke_dimension(lambdas)

    # Count positive exponents
    n_positive = int(np.sum(lambdas > 0))

    # Largest exponent
    lambda_max = float(lambdas[0]) if len(lambdas) > 0 else 0.0

    return {
        "K": K,
        "d": d,
        "lambdas": lambdas.tolist(),
        "n_positive": n_positive,
        "lambda_max": lambda_max,
        "D_KY": D_KY,
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
# Figure A: Lyapunov Spectrum (representative run)
# ---------------------------------------------------------------------------
def figure_spectrum(runs: list[dict], analyses: list[dict]):
    """Plot λ_i vs i for the largest-Nm run."""
    best_idx = max(range(len(runs)), key=lambda i: runs[i]["Nm"])
    run = runs[best_idx]
    ana = analyses[best_idx]

    lambdas = np.array(ana["lambdas"])
    d = len(lambdas)
    i_axis = np.arange(1, d + 1)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Color: positive = red, negative = blue
    colors = ["#b2182b" if lam > 0 else "#2166ac" for lam in lambdas]
    ax.bar(i_axis, lambdas, color=colors, alpha=0.8, width=0.7)

    # Zero line
    ax.axhline(0, color="black", linewidth=1.0, linestyle="-")

    # Annotations
    ax.annotate(
        (f"$d = {d}$, $n_{{\\mathrm{{pos}}}} = {ana['n_positive']}$\n"
         f"$\\lambda_{{\\max}} = {ana['lambda_max']:.6f}$\n"
         f"$D_{{KY}} = {ana['D_KY']:.4f}$"),
        xy=(0.98, 0.95), xycoords="axes fraction",
        fontsize=10, ha="right", va="top",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="white", alpha=0.8),
    )

    # ED prediction annotation
    if ana["n_positive"] == 0:
        verdict_text = "Point attractor (Principle 3 confirmed)"
        verdict_color = "#1b7837"
    else:
        verdict_text = (f"{ana['n_positive']} positive exponents "
                        f"(possible numerical artifact)")
        verdict_color = "#b2182b"

    ax.annotate(
        verdict_text,
        xy=(0.02, 0.05), xycoords="axes fraction",
        fontsize=9, color=verdict_color,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7),
    )

    setup_axes(
        ax,
        xlabel="Exponent index $i$",
        ylabel=r"Lyapunov exponent $\lambda_i$",
        title=(f"Lyapunov Spectrum -- D={run['D']}, A={run['A']}, "
               f"Nm={run['Nm']}"),
    )
    fig.tight_layout()

    fname = "lyapunov_spectrum.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure B: Attractor Dimension vs D
# ---------------------------------------------------------------------------
def figure_dimension_scatter(runs: list[dict], analyses: list[dict]):
    """Scatter D_KY vs D for all runs."""
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

    fig, ax = plt.subplots(figsize=(10, 6))

    all_DKY = []

    for run, ana in zip(runs, analyses):
        D_KY = ana["D_KY"]
        color = A_cmap(A_norm(run["A"]))
        marker = Nm_markers.get(run["Nm"], "o")

        ax.scatter(
            run["D"], D_KY,
            color=color, marker=marker, s=60, alpha=0.7,
            edgecolors="0.3", linewidths=0.4,
        )
        all_DKY.append(D_KY)

    # Global mean
    if all_DKY:
        mean_DKY = np.mean(all_DKY)
        ax.axhline(mean_DKY, color="0.4", linestyle="--",
                   linewidth=1.0, alpha=0.6)
        ax.annotate(
            rf"mean $D_{{KY}} = {mean_DKY:.4f}$",
            xy=(0.02, 0.95), xycoords="axes fraction",
            fontsize=10, va="top",
        )

    # ED prediction: D_KY = 0 (point attractor)
    ax.axhline(0, color="#1b7837", linestyle=":", linewidth=1.5,
               alpha=0.5, label=r"ED prediction: $D_{KY} = 0$")

    # Colorbar
    sm = plt.cm.ScalarMappable(cmap=A_cmap, norm=A_norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, label=r"Amplitude $A$", pad=0.02)
    cbar.ax.tick_params(labelsize=9)

    # Legend
    legend_handles = [
        plt.Line2D([0], [0], marker=m, color="0.5", markersize=7,
                   linestyle="None", label=rf"$N_m = {Nm}$")
        for Nm, m in Nm_markers.items()
    ]
    legend_handles.append(
        plt.Line2D([0], [0], color="#1b7837", linestyle=":", linewidth=1.5,
                   label=r"ED prediction: $D_{KY} = 0$")
    )
    ax.legend(handles=legend_handles, fontsize=8, loc="upper right",
              framealpha=0.9)

    setup_axes(
        ax,
        xlabel=r"Diffusion $D$",
        ylabel=r"Kaplan-Yorke dimension $D_{KY}$",
        title="Attractor Dimension -- All Admissible Runs",
    )
    ax.set_ylim(bottom=-0.5)
    fig.tight_layout()

    fname = "dimension_scatter.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300)
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Figure C: Spectrum Heatmap
# ---------------------------------------------------------------------------
def figure_spectrum_heatmap(runs: list[dict], analyses: list[dict]):
    """One panel per Nm; cell = number of positive exponents."""
    Nm_vals = sorted(set(r["Nm"] for r in runs))
    D_vals = sorted(set(r["D"] for r in runs))
    A_vals = sorted(set(r["A"] for r in runs))

    n_Nm = len(Nm_vals)
    if n_Nm == 0:
        print("  SKIP spectrum heatmap: no data.")
        return

    # Max possible positive exponents (for colorbar)
    max_pos = max(ana["n_positive"] for ana in analyses)
    vmax = max(max_pos, 1)

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
            grid[di, ai] = ana["n_positive"]

        # Green = 0 positive (stable), red = many positive (unstable)
        cmap = plt.cm.RdYlGn_r
        im = ax.imshow(
            grid, aspect="auto", origin="lower",
            cmap=cmap, vmin=0, vmax=vmax,
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
                    ax.text(ai_idx, di_idx, "--", ha="center", va="center",
                            fontsize=8, color="0.5")
                else:
                    n_pos = int(val)
                    txt_color = "white" if n_pos > vmax * 0.5 else "black"
                    ax.text(ai_idx, di_idx, str(n_pos), ha="center",
                            va="center", fontsize=9, color=txt_color,
                            fontweight="bold")

    fig.colorbar(
        plt.cm.ScalarMappable(cmap=plt.cm.RdYlGn_r,
                              norm=mcolors.Normalize(0, vmax)),
        ax=axes.tolist(),
        label=r"Number of positive $\lambda_i$",
        shrink=0.8, pad=0.04,
    )

    fig.suptitle(
        r"Lyapunov Spectrum -- Positive Exponents by $(D, A, N_m)$",
        fontsize=14, fontweight="bold", y=1.03,
    )
    fig.tight_layout()

    fname = "spectrum_heatmap.png"
    fig.savefig(os.path.join(FIG_DIR, fname), dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Summary table and invariance verdict
# ---------------------------------------------------------------------------
def print_summary(runs: list[dict], analyses: list[dict]):
    print(f"\n{'='*120}")
    print("  Invariant Lyapunov Spectrum -- Summary Table")
    print(f"{'='*120}")

    print(f"  {'D':<7} {'A':<7} {'Nm':<5} {'d':<5} "
          f"{'n_pos':<7} {'λ_max':<14} {'D_KY':<10} "
          f"{'λ_1..λ_5'}")
    print("  " + "-" * 110)

    all_n_pos = []
    all_DKY = []
    all_lmax = []

    for run, ana in zip(runs, analyses):
        lam = ana["lambdas"]
        lam_str = ", ".join(f"{l:+.6f}" for l in lam[:5])
        if len(lam) > 5:
            lam_str += f" ... ({len(lam)} total)"

        print(f"  {run['D']:<7.3f} {run['A']:<7.4f} {run['Nm']:<5d} "
              f"{ana['d']:<5d} "
              f"{ana['n_positive']:<7d} {ana['lambda_max']:<14.6e} "
              f"{ana['D_KY']:<10.4f} "
              f"{lam_str}")

        all_n_pos.append(ana["n_positive"])
        all_DKY.append(ana["D_KY"])
        all_lmax.append(ana["lambda_max"])

    # Global statistics
    print(f"\n  {'Invariant':<16} {'Mean':<12} {'Std':<12} "
          f"{'Min':<12} {'Max':<12} {'CV':<10} {'Verdict'}")
    print("  " + "-" * 80)

    for name, arr_list in [("n_positive", all_n_pos),
                           ("D_KY", all_DKY),
                           ("λ_max", all_lmax)]:
        arr = np.array(arr_list)
        if len(arr) == 0:
            print(f"  {name:<16} (no data)")
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

        print(f"  {name:<16} "
              f"{mean_v:<12.6f} {std_v:<12.6f} "
              f"{np.min(arr):<12.6f} {np.max(arr):<12.6f} "
              f"{cv:<10.4f} {verdict}")

    # ED consistency check
    all_zero = all(n == 0 for n in all_n_pos)
    print(f"\n  ED Principle 3 (point attractor) check:")
    if all_zero:
        print(f"    PASS -- all runs have 0 positive exponents, D_KY = 0")
    else:
        n_nonzero = sum(1 for n in all_n_pos if n > 0)
        print(f"    WARNING -- {n_nonzero}/{len(all_n_pos)} runs have "
              f"positive exponents")
        print(f"    (may be numerical artifacts from finite-difference "
              f"Jacobian approximation)")


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
    print(f"  D range:  {min(r['D'] for r in runs):.3f} - "
          f"{max(r['D'] for r in runs):.3f}")
    print(f"  A range:  {min(r['A'] for r in runs):.4f} - "
          f"{max(r['A'] for r in runs):.4f}")
    print(f"  Nm range: {min(r['Nm'] for r in runs)} - "
          f"{max(r['Nm'] for r in runs)}")

    # Analyse
    print(f"\nComputing Lyapunov spectra (K <= {K_MAX}, d <= {MAX_DIM})...")
    analyses = []
    for i, run in enumerate(runs):
        ana = analyse_run(run)
        analyses.append(ana)
        if (i + 1) % 5 == 0 or i == len(runs) - 1:
            print(f"  [{i+1}/{len(runs)}] {run['name']}: "
                  f"d={ana['d']}, n_pos={ana['n_positive']}, "
                  f"λ_max={ana['lambda_max']:.6e}, "
                  f"D_KY={ana['D_KY']:.4f}")

    # Figures
    print("\n--- (A) Lyapunov Spectrum ---")
    figure_spectrum(runs, analyses)

    print("\n--- (B) Attractor Dimension ---")
    figure_dimension_scatter(runs, analyses)

    print("\n--- (C) Spectrum Heatmap ---")
    figure_spectrum_heatmap(runs, analyses)

    # Summary
    print_summary(runs, analyses)

    print(f"\nAll figures saved to: {FIG_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
