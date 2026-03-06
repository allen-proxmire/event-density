"""
Scenario_E_TwoCore.py
=====================
Two-core interaction experiment: how do two saturated ED cores interact?

This script extends the existing ED simulation engine WITHOUT modifying any
core update rules, parameters, or plotting utilities.  It adds four things:

  1. init_two_saturated_cores()  — place two Gaussian cores at a given
                                   pixel separation d, using the same
                                   amplitude/width as Scenario B.

  2. detect_cores()              — threshold + connected-component label;
                                   returns centroid, mass, radius per core.

  3. classify_outcome()          — MERGE / REPEL / ANNIHILATE / HOVER based
                                   on the time series of core count and
                                   inter-centroid distance.

  4. run_two_core()              — single-run driver: evolve, track, classify,
                                   save figures, print summary.

  5. main()                      — sweep over separations = [20, 40, 60, 80] px.

UNCHANGED ENGINE PARAMETERS
----------------------------
  alpha=0.05, beta=0.25, gamma=0.5, dt=0.1
  p_min=0.01, p_max=1.0, boundary="periodic", mode="standard"

CORE SHAPE (same as init_two_body defaults in Scenario B)
----------------------------------------------------------
  Gaussian, amplitude = 0.9 * p_max above background
  sigma    = 0.08 * min(rows, cols)   [= 8 px on a 100-grid]
  background = 0.10 * p_max

OUTPUT (per separation d)
-------------------------
  results/two_core/field_d{d:02d}.png  — density field at t=0, t=mid, t=final
  results/two_core/dist_d{d:02d}.png   — centroid distance vs time
  Console: classification summary line
"""

from __future__ import annotations

import os
import sys
import warnings

import numpy as np
import matplotlib
matplotlib.use("Agg")   # headless rendering
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Path setup — allow importing engine files from the same directory
# ---------------------------------------------------------------------------

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from ED_Lattice import EDLattice, EDParams

try:
    from scipy.ndimage import label as nd_label, center_of_mass as nd_com
    _SCIPY = True
except ImportError:
    _SCIPY = False
    warnings.warn(
        "scipy not found — core detection will use a pure-numpy BFS fallback. "
        "Install scipy for faster connected-component labelling.",
        ImportWarning,
        stacklevel=2,
    )


# ---------------------------------------------------------------------------
# Pure-numpy BFS connected-component labelling (scipy-free fallback)
# ---------------------------------------------------------------------------

def _bfs_label(binary: np.ndarray):
    """
    4-connected component labelling via breadth-first search.

    Used only when scipy is unavailable.  O(N) in the number of True cells.

    Parameters
    ----------
    binary : 2D boolean array.

    Returns
    -------
    labeled      : 2D int array, same shape as binary; 0 = background.
    n_components : int, number of distinct connected components.
    """
    from collections import deque

    rows, cols  = binary.shape
    labeled     = np.zeros_like(binary, dtype=np.int32)
    n_components = 0

    for r0 in range(rows):
        for c0 in range(cols):
            if binary[r0, c0] and labeled[r0, c0] == 0:
                n_components += 1
                q = deque([(r0, c0)])
                labeled[r0, c0] = n_components
                while q:
                    r, c = q.popleft()
                    for nr, nc in ((r - 1, c), (r + 1, c),
                                   (r, c - 1), (r, c + 1)):
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if binary[nr, nc] and labeled[nr, nc] == 0:
                                labeled[nr, nc] = n_components
                                q.append((nr, nc))

    return labeled, n_components


# ---------------------------------------------------------------------------
# Experiment-level constants
# ---------------------------------------------------------------------------

GRID_SIZE   = 100        # square grid (pixels) — larger than default 64 to
                         # give cores room to interact without boundary aliasing
STEPS       = 500        # total simulation steps
SEED        = 42         # reproducibility

# Core shape — intentionally identical to init_two_body() defaults in Scenario B
CORE_AMPLITUDE  = 0.9   # peak height above background as fraction of p_max
CORE_WIDTH_FRAC = 0.08  # Gaussian sigma as fraction of grid size  (= 8 px here)
CORE_BACKGROUND = 0.10  # background ED as fraction of p_max

# Core detection: sites above this fraction of p_max are "core"
DETECT_THRESH = 0.50

# Parameter set — UNCHANGED from standard ED engine defaults
PARAMS = EDParams(
    alpha        = 0.05,
    beta         = 0.25,
    gamma        = 0.5,
    dt           = 0.1,
    p_min        = 0.01,
    p_max        = 1.0,
    boundary     = "periodic",
    mode         = "standard",
    noise_scale  = 0.0,
    mobility_exp = 1.0,
)

# Sweep values
SEPARATIONS        = [20, 40, 60, 80]              # centre-to-centre separation in pixels
ALPHA_VALUES       = [0.05, 0.02, 0.01, 0.005, 0.001]  # relational drain strengths to sweep
MOBILITY_EXPONENTS = [1.0, 2.0, 3.0, 4.0]         # M(rho)=((rho_max-rho)/rho_max)^m exponents

OUTDIR_BASE = os.path.join(_HERE, "results", "two_core")


# ---------------------------------------------------------------------------
# 1.  Initial condition: two saturated cores
# ---------------------------------------------------------------------------

def init_two_saturated_cores(lat: EDLattice, d: int) -> EDLattice:
    """
    Initialise two Gaussian ED cores at pixel separation d.

    Delegates entirely to the existing ``EDLattice.init_two_body()`` method,
    which places:
        Core A at column  cols/2 - d/2,  row  rows/2
        Core B at column  cols/2 + d/2,  row  rows/2

    The Gaussian shape (amplitude, width, background) is the same as the
    Scenario-B defaults so that results are directly comparable.

    Parameters
    ----------
    lat : EDLattice  (already constructed; its field is overwritten)
    d   : Centre-to-centre separation in **pixels**.

    Returns
    -------
    lat (modified in-place, returned for chaining)
    """
    # init_two_body expects separation as a fraction of grid width
    separation_frac = d / lat.cols
    lat.init_two_body(
        separation = separation_frac,
        amplitude  = CORE_AMPLITUDE,
        width      = CORE_WIDTH_FRAC,
        background = CORE_BACKGROUND,
    )
    return lat


# ---------------------------------------------------------------------------
# 2.  Core detection and tracking
# ---------------------------------------------------------------------------

def detect_cores(p: np.ndarray, p_max: float = 1.0) -> list:
    """
    Identify connected high-density regions ("cores") in the field p.

    Thresholds at DETECT_THRESH * p_max, then uses scipy's connected-component
    labelling (``scipy.ndimage.label``).

    Parameters
    ----------
    p     : 2D density array, shape (rows, cols).
    p_max : Saturation ceiling; sets the detection threshold.

    Returns
    -------
    cores : list of dicts, one per connected component, sorted left-to-right.
        Each dict contains:
            "label"    : integer component label (1-indexed)
            "centroid" : (row, col) float tuple — density-weighted centre of mass
            "mass"     : total density sum inside the component
            "radius"   : RMS distance from centroid to member pixels (pixels)
    """
    threshold = DETECT_THRESH * p_max
    binary    = (p >= threshold)

    if _SCIPY:
        labeled, n_components = nd_label(binary)
    else:
        labeled, n_components = _bfs_label(binary)

    if n_components == 0:
        return []

    r_idx, c_idx = np.indices(p.shape, dtype=float)
    cores = []

    for k in range(1, n_components + 1):
        mask = (labeled == k)
        mass = float(p[mask].sum())

        # Density-weighted centroid (= centre of mass with p as weights)
        if _SCIPY:
            centroid = nd_com(p, labels=labeled, index=k)   # returns (row, col)
        else:
            # Manual weighted centroid
            w = p[mask]
            w_sum = w.sum()
            cr = float(np.sum(r_idx[mask] * w) / w_sum)
            cc = float(np.sum(c_idx[mask] * w) / w_sum)
            centroid = (cr, cc)

        # Approximate radius: RMS distance from centroid to member pixels
        dr     = r_idx[mask] - centroid[0]
        dc     = c_idx[mask] - centroid[1]
        radius = float(np.sqrt(np.mean(dr**2 + dc**2)))

        cores.append({
            "label":    k,
            "centroid": centroid,
            "mass":     mass,
            "radius":   radius,
        })

    # Sort by column position (left → right) for consistent Core A / B labelling
    cores.sort(key=lambda c: c["centroid"][1])
    return cores


# ---------------------------------------------------------------------------
# 3.  Outcome classification
# ---------------------------------------------------------------------------

def classify_outcome(
    n_cores_series: np.ndarray,
    dist_series:    np.ndarray,
    n_init:         int = 2,
) -> str:
    """
    Classify the two-core interaction from the recorded time series.

    Rules (applied in priority order):
    ┌──────────────┬──────────────────────────────────────────────────────┐
    │ ANNIHILATE   │ mean core count over last 20% of steps < 0.5        │
    │ MERGE        │ mean core count over last 20% of steps ≈ 1          │
    │ REPEL        │ 2 cores persist AND distance grows by > 10%         │
    │ HOVER/ORBIT  │ 2 cores persist AND distance roughly constant (±10%)│
    └──────────────┴──────────────────────────────────────────────────────┘

    Parameters
    ----------
    n_cores_series : 1D int-like array; core count at each recorded step.
    dist_series    : 1D float array; inter-centroid distance (NaN if < 2 cores).
    n_init         : Core count at step 0 (may be 1 if cores overlap at init).

    Returns
    -------
    label : "MERGE" | "REPEL" | "ANNIHILATE" | "HOVER/ORBIT"
    """
    n     = len(n_cores_series)
    tail  = max(1, n // 5)    # last 20 % of steps
    head  = max(1, n // 10)   # first 10 % of steps

    mean_n_tail = float(np.mean(n_cores_series[-tail:]))

    if mean_n_tail < 0.5:
        return "ANNIHILATE"

    if mean_n_tail < 1.5:
        return "MERGE"

    # Two cores persist — compare early vs late inter-centroid distance
    valid = dist_series[~np.isnan(dist_series)]
    if len(valid) < 2:
        return "HOVER/ORBIT"

    d_early = float(np.nanmean(dist_series[:head]))
    d_late  = float(np.nanmean(dist_series[-tail:]))

    if d_early > 0:
        change = (d_late - d_early) / d_early
        if change > 0.10:
            return "REPEL"

    return "HOVER/ORBIT"


# ---------------------------------------------------------------------------
# 4.  Single-run driver
# ---------------------------------------------------------------------------

def run_two_core(d: int, alpha: float, mobility_exp: float, outdir: str) -> str:
    """
    Run the two-core experiment for pixel separation *d*, drain strength *alpha*,
    and mobility exponent *mobility_exp*.

    Steps
    -----
    1. Build lattice with the given alpha and mobility_exp; place two cores at d.
    2. Evolve for STEPS steps, detecting cores at every step.
    3. Classify outcome.
    4. Save field-snapshot figure and centroid-distance figure.
    5. Print one-line summary.

    Parameters
    ----------
    d            : Centre-to-centre core separation in pixels.
    alpha        : Relational drain strength (overrides PARAMS.alpha).
    mobility_exp : Mobility exponent m in M(rho)=((rho_max-rho)/rho_max)^m
                   (overrides PARAMS.mobility_exp).  Only takes effect when
                   mode="mobility"; mode is set to "mobility" here so that
                   varying m produces observable differences.
    outdir       : Directory for output figures (created if absent).

    Returns
    -------
    outcome : classification string
    """
    os.makedirs(outdir, exist_ok=True)

    # ------------------------------------------------------------------ #
    # Build and initialise lattice  (alpha and mobility_exp vary per run)
    # ------------------------------------------------------------------ #
    run_params = EDParams(
        alpha        = alpha,
        beta         = PARAMS.beta,
        gamma        = PARAMS.gamma,
        dt           = PARAMS.dt,
        p_min        = PARAMS.p_min,
        p_max        = PARAMS.p_max,
        boundary     = PARAMS.boundary,
        mode         = "mobility",      # mobility_exp only acts in this mode
        noise_scale  = PARAMS.noise_scale,
        mobility_exp = mobility_exp,    # ← the new swept parameter
    )
    lat = EDLattice(rows=GRID_SIZE, cols=GRID_SIZE, params=run_params, seed=SEED)
    init_two_saturated_cores(lat, d)

    mid_step = STEPS // 2          # step at which to capture mid snapshot

    # ------------------------------------------------------------------ #
    # Storage
    # ------------------------------------------------------------------ #
    n_cores_list: list[int]   = []
    dist_list:    list[float] = []

    p_initial = lat.p.copy()       # snapshot at t = 0
    p_mid:    np.ndarray | None = None

    # ------------------------------------------------------------------ #
    # Evolution loop — detect BEFORE stepping so index s matches step s
    # ------------------------------------------------------------------ #
    for s in range(STEPS):

        # --- core detection at current state (after s steps) ---
        cores = detect_cores(lat.p, run_params.p_max)
        n     = len(cores)
        n_cores_list.append(n)

        if n >= 2:
            c0 = np.array(cores[0]["centroid"])
            c1 = np.array(cores[1]["centroid"])
            dist_list.append(float(np.linalg.norm(c1 - c0)))
        else:
            dist_list.append(float("nan"))

        # --- mid-point snapshot ---
        if s == mid_step:
            p_mid = lat.p.copy()

        # --- advance one step ---
        lat.step()

    # Capture final state (after all STEPS steps)
    p_final = lat.p.copy()
    if p_mid is None:               # guard for STEPS == 0
        p_mid = p_initial

    # ------------------------------------------------------------------ #
    # Arrays and classification
    # ------------------------------------------------------------------ #
    n_cores_series = np.array(n_cores_list, dtype=float)
    dist_series    = np.array(dist_list,    dtype=float)

    n_init  = int(n_cores_series[0])
    outcome = classify_outcome(n_cores_series, dist_series, n_init)

    # ------------------------------------------------------------------ #
    # Console summary
    # ------------------------------------------------------------------ #
    d_init_str  = f"{dist_series[0]:.1f}"  if not np.isnan(dist_series[0])  else "n/a"
    d_final_arr = dist_series[-max(1, STEPS // 5):]
    d_final_str = f"{float(np.nanmean(d_final_arr)):.1f}" \
                  if not np.all(np.isnan(d_final_arr)) else "n/a"

    init_note = f"  [WARNING: initial n_cores={n_init}, cores may overlap]" \
                if n_init != 2 else ""
    print(
        f"  alpha={alpha:<6}  m={mobility_exp:<4}  d={d:3d} px | outcome={outcome:<12s} | "
        f"n_cores: {n_init} -> {int(n_cores_series[-1])} | "
        f"dist_init={d_init_str}  dist_final={d_final_str}{init_note}"
    )

    # ------------------------------------------------------------------ #
    # Figure 1: density field at t=0, t=mid, t=final
    # ------------------------------------------------------------------ #
    fig1, axes = plt.subplots(
        1, 3, figsize=(13, 4.5), constrained_layout=True
    )

    panels = [
        (p_initial, "t = 0  (initial)"),
        (p_mid,     f"t = {mid_step}  (mid)"),
        (p_final,   f"t = {STEPS}  (final)"),
    ]

    for ax, (field, title) in zip(axes, panels):
        im = ax.imshow(
            field, origin="lower", cmap="viridis",
            vmin=run_params.p_min, vmax=run_params.p_max,
            interpolation="nearest",
        )
        ax.set_title(title, fontsize=11)
        ax.set_xlabel("x  (col)")
        ax.set_ylabel("y  (row)")

    fig1.colorbar(im, ax=axes, label="ED density  rho", shrink=0.82)
    fig1.suptitle(
        f"Scenario E — Two-Core Interaction   "
        f"alpha = {alpha},   m = {mobility_exp},   d = {d} px,   outcome = {outcome}",
        fontsize=13, fontweight="bold",
    )

    out1 = os.path.join(outdir, f"field_d{d:02d}_a{alpha}_m{mobility_exp}.png")
    fig1.savefig(out1, dpi=150)
    plt.close(fig1)

    # ------------------------------------------------------------------ #
    # Figure 2: centroid distance vs time
    # ------------------------------------------------------------------ #
    steps_axis = np.arange(STEPS)

    fig2, ax2 = plt.subplots(figsize=(8, 4), constrained_layout=True)

    ax2.plot(
        steps_axis, dist_series,
        color="#2563eb", linewidth=1.6, label="inter-centroid distance",
    )
    ax2.axhline(
        d, color="#9ca3af", linestyle="--", linewidth=1.2,
        label=f"initial separation ({d} px)",
    )

    # shade n_cores == 1 regions in amber
    merged_mask = (n_cores_series < 1.5)
    if merged_mask.any():
        ax2.fill_between(
            steps_axis, 0, ax2.get_ylim()[1] if ax2.get_ylim()[1] > 0 else 1,
            where=merged_mask, alpha=0.12, color="#d97706",
            label="n_cores = 1  (merged)",
        )

    ax2.set_xlabel("step",                  fontsize=11)
    ax2.set_ylabel("centroid distance (px)", fontsize=11)
    ax2.set_title(
        f"Scenario E — Centroid Distance vs Time   "
        f"alpha = {alpha},   m = {mobility_exp},   d = {d} px,   outcome = {outcome}",
        fontsize=11,
    )
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)

    out2 = os.path.join(outdir, f"dist_d{d:02d}_a{alpha}_m{mobility_exp}.png")
    fig2.savefig(out2, dpi=150)
    plt.close(fig2)

    return outcome


# ---------------------------------------------------------------------------
# 5.  Phase diagram builder
# ---------------------------------------------------------------------------

def build_phase_diagram(
    alpha_values:    list,
    mobility_values: list,
    separations:     list,
    results_dict:    dict,
    outdir:          str,
) -> None:
    """
    Collapse the (alpha, m, d) sweep results into a 2D (alpha, m) phase diagram
    and save it as a PNG.

    Collapse rule (applied in priority order for each (alpha, m) pair):
      HOVER      — any separation d yields "HOVER/ORBIT"
      MERGE      — else, any separation d yields "MERGE"
      ANNIHILATE — all separations yield "ANNIHILATE"

    Parameters
    ----------
    alpha_values    : list of alpha values (rows, top = first element).
    mobility_values : list of mobility exponents (columns, left = first).
    separations     : list of d values used to collapse over d.
    results_dict    : dict keyed by (alpha, m, d) → outcome string.
    outdir          : directory in which to save phase_diagram_alpha_m.png.
    """
    from matplotlib.colors import ListedColormap, BoundaryNorm
    from matplotlib.patches import Patch

    os.makedirs(outdir, exist_ok=True)

    # ------------------------------------------------------------------ #
    # Regime encoding
    # ------------------------------------------------------------------ #
    ANNIHILATE_CODE, MERGE_CODE, HOVER_CODE = 0, 1, 2

    _COLORS = {
        ANNIHILATE_CODE: "#9ca3af",   # grey
        MERGE_CODE:      "#2563eb",   # blue
        HOVER_CODE:      "#16a34a",   # green
    }
    _LABELS = {
        ANNIHILATE_CODE: "ANNIHILATE",
        MERGE_CODE:      "MERGE",
        HOVER_CODE:      "HOVER/ORBIT",
    }
    _SHORT = {
        ANNIHILATE_CODE: "ANNH",
        MERGE_CODE:      "MERGE",
        HOVER_CODE:      "HOVER",
    }

    # ------------------------------------------------------------------ #
    # Build 2D matrix  (rows = alpha index, cols = m index)
    # ------------------------------------------------------------------ #
    n_alpha = len(alpha_values)
    n_mob   = len(mobility_values)
    matrix  = np.zeros((n_alpha, n_mob), dtype=int)

    for i, alpha in enumerate(alpha_values):
        for j, m in enumerate(mobility_values):
            outcomes = [results_dict[(alpha, m, d)] for d in separations]
            if "HOVER/ORBIT" in outcomes:
                matrix[i, j] = HOVER_CODE
            elif "MERGE" in outcomes:
                matrix[i, j] = MERGE_CODE
            else:
                matrix[i, j] = ANNIHILATE_CODE

    # ------------------------------------------------------------------ #
    # Plot
    # ------------------------------------------------------------------ #
    cmap = ListedColormap([_COLORS[0], _COLORS[1], _COLORS[2]])
    norm = BoundaryNorm([-0.5, 0.5, 1.5, 2.5], cmap.N)

    fig, ax = plt.subplots(figsize=(7, 5), constrained_layout=True)

    ax.imshow(
        matrix,
        cmap=cmap, norm=norm,
        origin="upper",       # row 0 (alpha_values[0]) at top
        aspect="auto",
        interpolation="nearest",
    )

    # Axis ticks — alpha on y, m on x
    ax.set_xticks(range(n_mob))
    ax.set_xticklabels([str(m) for m in mobility_values], fontsize=11)
    ax.set_yticks(range(n_alpha))
    ax.set_yticklabels([str(a) for a in alpha_values], fontsize=11)

    ax.set_xlabel("Mobility exponent  m", fontsize=12)
    ax.set_ylabel("Drain strength  alpha", fontsize=12)
    ax.set_title(
        "ED Two-Core Interaction Phase Diagram\n(alpha vs mobility exponent)",
        fontsize=13, fontweight="bold",
    )

    # Cell annotations
    for i in range(n_alpha):
        for j in range(n_mob):
            ax.text(
                j, i, _SHORT[matrix[i, j]],
                ha="center", va="center",
                fontsize=9, fontweight="bold", color="white",
            )

    # Legend (patches, more reliable than colorbar for 3-class discrete maps)
    legend_handles = [
        Patch(facecolor=_COLORS[code], label=_LABELS[code])
        for code in (ANNIHILATE_CODE, MERGE_CODE, HOVER_CODE)
    ]
    ax.legend(
        handles=legend_handles,
        loc="upper right", fontsize=9,
        framealpha=0.85, edgecolor="0.6",
    )

    outpath = os.path.join(outdir, "phase_diagram_alpha_m.png")
    fig.savefig(outpath, dpi=150)
    plt.close(fig)
    print(f"\nPhase diagram saved to: {outpath}")

    # ------------------------------------------------------------------ #
    # Console printout of the collapsed 2D table
    # ------------------------------------------------------------------ #
    col_w = 12
    print("\n" + "=" * 76)
    print("PHASE DIAGRAM  (alpha vs m,  collapsed over all separations d)")
    print("-" * 76)
    header = f"  {'alpha':<10}" + "".join(f"  m={m:<{col_w-3}}" for m in mobility_values)
    print(header)
    print("  " + "-" * 72)
    for i, alpha in enumerate(alpha_values):
        row = f"  {alpha:<10}"
        for j in range(n_mob):
            row += f"  {_LABELS[matrix[i, j]]:<{col_w-2}}"
        print(row)
    print("=" * 76)


# ---------------------------------------------------------------------------
# 6.  Parameter sweep
# ---------------------------------------------------------------------------

def main() -> None:
    """Sweep over ALPHA_VALUES × MOBILITY_EXPONENTS × SEPARATIONS."""

    n_runs = len(ALPHA_VALUES) * len(MOBILITY_EXPONENTS) * len(SEPARATIONS)
    print("=" * 76)
    print("Scenario E: Two-Core Interaction — alpha × m × separation sweep")
    print(f"  Grid             : {GRID_SIZE} x {GRID_SIZE}   Seed : {SEED}")
    print(f"  Steps            : {STEPS}")
    print(f"  Core shape       : Gaussian  amplitude={CORE_AMPLITUDE}*p_max  "
          f"sigma={CORE_WIDTH_FRAC*GRID_SIZE:.0f} px  "
          f"bg={CORE_BACKGROUND}*p_max")
    print(f"  Threshold        : {DETECT_THRESH} * p_max")
    print(f"  alpha values     : {ALPHA_VALUES}")
    print(f"  mobility exp (m) : {MOBILITY_EXPONENTS}")
    print(f"  separations      : {SEPARATIONS} px")
    print(f"  beta={PARAMS.beta}  gamma={PARAMS.gamma}  dt={PARAMS.dt}  "
          f"mode=mobility  (set per run so m takes effect)")
    print(f"  Total runs       : {n_runs}")
    print(f"  Output base      : {OUTDIR_BASE}")
    print("=" * 76)

    # results[(alpha, m, d)] = outcome string
    results: dict[tuple, str] = {}

    for alpha in ALPHA_VALUES:
        for m in MOBILITY_EXPONENTS:
            outdir = os.path.join(OUTDIR_BASE, f"a{alpha}_m{m}")
            print(f"\n--- alpha = {alpha},  m = {m} ---")
            for d in SEPARATIONS:
                outcome = run_two_core(d, alpha, m, outdir)
                results[(alpha, m, d)] = outcome
                print(f"  alpha={alpha}, m={m}, d={d} => {outcome}")

    # ------------------------------------------------------------------ #
    # Final summary table — one sub-table per alpha, rows = m, cols = d
    # ------------------------------------------------------------------ #
    col_w = 14
    print("\n" + "=" * 76)
    print("FULL SWEEP SUMMARY  (rows = mobility exp m,  cols = separation d)")
    for alpha in ALPHA_VALUES:
        print("\n" + "-" * 76)
        print(f"  alpha = {alpha}")
        header = f"  {'m':<8}" + "".join(f"  d={d:<{col_w-3}}" for d in SEPARATIONS)
        print(header)
        print("  " + "-" * 72)
        for m in MOBILITY_EXPONENTS:
            row = f"  {m:<8}"
            for d in SEPARATIONS:
                outcome = results[(alpha, m, d)]
                row += f"  {outcome:<{col_w-2}}"
            print(row)
    print("=" * 76)
    print(f"\nFigures saved under: {OUTDIR_BASE}/")

    # ------------------------------------------------------------------ #
    # Phase diagram — collapse (alpha, m, d) → (alpha, m) and plot
    # ------------------------------------------------------------------ #
    build_phase_diagram(
        alpha_values    = ALPHA_VALUES,
        mobility_values = MOBILITY_EXPONENTS,
        separations     = SEPARATIONS,
        results_dict    = results,
        outdir          = OUTDIR_BASE,
    )


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()
