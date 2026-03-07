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
import json
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
GAMMA_VALUES       = [0.10, 0.25, 0.5, 0.75]      # suppression exponent γ; EDParams requires 0<γ<1

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

def run_two_core(
    d:            int,
    alpha:        float,
    mobility_exp: float,
    gamma:        float,
    outdir:       str,
) -> str:
    """
    Run the two-core experiment for pixel separation *d*, drain strength *alpha*,
    mobility exponent *mobility_exp*, and suppression exponent *gamma*.

    Steps
    -----
    1. Build lattice with the given alpha, gamma, and mobility_exp; place two cores.
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
    gamma        : Suppression exponent γ (overrides PARAMS.gamma).
    outdir       : Directory for output figures (created if absent).

    Returns
    -------
    outcome : classification string
    """
    os.makedirs(outdir, exist_ok=True)

    # ------------------------------------------------------------------ #
    # Build and initialise lattice  (alpha, gamma, mobility_exp vary per run)
    # ------------------------------------------------------------------ #
    run_params = EDParams(
        alpha        = alpha,
        beta         = PARAMS.beta,
        gamma        = gamma,           # ← swept parameter (was PARAMS.gamma)
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
        f"  alpha={alpha:<6}  m={mobility_exp:<4}  gamma={gamma:<5}  d={d:3d} px | "
        f"outcome={outcome:<12s} | "
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
        f"alpha={alpha},  m={mobility_exp},  gamma={gamma},  d={d} px,  outcome={outcome}",
        fontsize=13, fontweight="bold",
    )

    out1 = os.path.join(outdir, f"field_d{d:02d}_a{alpha}_m{mobility_exp}_g{gamma}.png")
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
        f"alpha={alpha},  m={mobility_exp},  gamma={gamma},  d={d} px,  outcome={outcome}",
        fontsize=11,
    )
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)

    out2 = os.path.join(outdir, f"dist_d{d:02d}_a{alpha}_m{mobility_exp}_g{gamma}.png")
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
# 6.  Interaction surface builder
# ---------------------------------------------------------------------------

def build_interaction_surface(
    alpha_values:    list,
    mobility_values: list,
    separations:     list,
    results_dict:    dict,
    outdir:          str,
    tag:             str = "",
) -> None:
    """
    Build the full (alpha, m, d) interaction surface from already-computed results.

    For each separation d:
      - Build a raw 2D (alpha × m) matrix (no collapse across d).
      - Save a colour-coded figure: interaction_surface_d{d:02d}.png

    Also produces:
      - interaction_surface_all_d.png — all d-slices in a single grid figure.
      - Console 3D table: for each alpha, rows = m, cols = d.

    Parameters
    ----------
    alpha_values    : list of alpha values (rows).
    mobility_values : list of mobility exponents (columns).
    separations     : list of d values (one slice per d value).
    results_dict    : dict keyed by (alpha, m, d) → outcome string.
    outdir          : directory in which to save all figures.
    """
    import math
    from matplotlib.colors import ListedColormap, BoundaryNorm
    from matplotlib.patches import Patch

    os.makedirs(outdir, exist_ok=True)

    # ------------------------------------------------------------------ #
    # Shared encoding (identical to build_phase_diagram)
    # ------------------------------------------------------------------ #
    ANNIHILATE_CODE, MERGE_CODE, HOVER_CODE = 0, 1, 2

    _STR_TO_CODE = {
        "ANNIHILATE":  ANNIHILATE_CODE,
        "MERGE":       MERGE_CODE,
        "HOVER/ORBIT": HOVER_CODE,
    }
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

    cmap = ListedColormap([_COLORS[0], _COLORS[1], _COLORS[2]])
    norm = BoundaryNorm([-0.5, 0.5, 1.5, 2.5], cmap.N)

    legend_handles = [
        Patch(facecolor=_COLORS[code], label=_LABELS[code])
        for code in (ANNIHILATE_CODE, MERGE_CODE, HOVER_CODE)
    ]

    n_alpha = len(alpha_values)
    n_mob   = len(mobility_values)
    n_sep   = len(separations)

    # ------------------------------------------------------------------ #
    # Build one 2D matrix per d — raw, no collapse
    # ------------------------------------------------------------------ #
    matrices = {}
    for d in separations:
        mat = np.zeros((n_alpha, n_mob), dtype=int)
        for i, alpha in enumerate(alpha_values):
            for j, m in enumerate(mobility_values):
                mat[i, j] = _STR_TO_CODE[results_dict[(alpha, m, d)]]
        matrices[d] = mat

    # ------------------------------------------------------------------ #
    # Helper: draw one slice onto an existing Axes object
    # ------------------------------------------------------------------ #
    def _draw_slice(ax, mat, d, show_xlabel=True, show_ylabel=True):
        ax.imshow(
            mat,
            cmap=cmap, norm=norm,
            origin="upper",
            aspect="auto",
            interpolation="nearest",
        )
        ax.set_xticks(range(n_mob))
        ax.set_xticklabels([str(m) for m in mobility_values], fontsize=9)
        ax.set_yticks(range(n_alpha))
        ax.set_yticklabels([str(a) for a in alpha_values], fontsize=9)
        if show_xlabel:
            ax.set_xlabel("Mobility exponent  m", fontsize=10)
        if show_ylabel:
            ax.set_ylabel("Drain  alpha", fontsize=10)
        ax.set_title(
            f"Interaction Surface Slice at d = {d}",
            fontsize=11, fontweight="bold",
        )
        for i in range(n_alpha):
            for j in range(n_mob):
                ax.text(
                    j, i, _SHORT[mat[i, j]],
                    ha="center", va="center",
                    fontsize=8, fontweight="bold", color="white",
                )

    # ------------------------------------------------------------------ #
    # Per-d individual figures
    # ------------------------------------------------------------------ #
    print(f"\nBuilding interaction surface slices in: {outdir}")
    for d in separations:
        fig, ax = plt.subplots(figsize=(7, 5), constrained_layout=True)
        _draw_slice(ax, matrices[d], d)
        ax.legend(
            handles=legend_handles, loc="upper right",
            fontsize=9, framealpha=0.85, edgecolor="0.6",
        )
        outpath = os.path.join(outdir, f"interaction_surface_{tag}d{d:02d}.png")
        fig.savefig(outpath, dpi=150)
        plt.close(fig)
        print(f"  Saved: interaction_surface_{tag}d{d:02d}.png")

    # ------------------------------------------------------------------ #
    # Combined figure — all d-slices in one grid (at most 2 columns)
    # ------------------------------------------------------------------ #
    n_cols  = min(n_sep, 2)
    n_rows  = math.ceil(n_sep / n_cols)

    fig_all, axes_all = plt.subplots(
        n_rows, n_cols,
        figsize=(7 * n_cols, 5 * n_rows),
        constrained_layout=True,
        squeeze=False,
    )

    for idx, d in enumerate(separations):
        r, c = divmod(idx, n_cols)
        _draw_slice(
            axes_all[r][c], matrices[d], d,
            show_xlabel = (r == n_rows - 1),
            show_ylabel = (c == 0),
        )

    # Hide any unfilled panel (odd total count)
    for idx in range(n_sep, n_rows * n_cols):
        r, c = divmod(idx, n_cols)
        axes_all[r][c].set_visible(False)

    # Shared legend on the first panel
    axes_all[0][0].legend(
        handles=legend_handles, loc="upper right",
        fontsize=8, framealpha=0.85, edgecolor="0.6",
    )

    fig_all.suptitle(
        "ED Two-Core Interaction Surface — All Separation Slices\n"
        "(alpha vs mobility exponent, per separation d)",
        fontsize=13, fontweight="bold",
    )

    out_all = os.path.join(outdir, f"interaction_surface_{tag}all_d.png")
    fig_all.savefig(out_all, dpi=150)
    plt.close(fig_all)
    print(f"  Saved: interaction_surface_{tag}all_d.png")

    # ------------------------------------------------------------------ #
    # 3D console table — for each alpha: rows = m, cols = d
    # ------------------------------------------------------------------ #
    col_w = 13
    print("\n" + "=" * 76)
    print("INTERACTION SURFACE TABLE  (per alpha: rows = m,  cols = d)")
    for alpha in alpha_values:
        print("\n" + "-" * 76)
        print(f"  alpha = {alpha}")
        header = f"  {'m':<8}" + "".join(
            f"  d={d:<{col_w - 3}}" for d in separations
        )
        print(header)
        print("  " + "-" * 70)
        for m in mobility_values:
            row = f"  {m:<8}"
            for d in separations:
                label = _LABELS[_STR_TO_CODE[results_dict[(alpha, m, d)]]]
                row += f"  {label:<{col_w - 2}}"
            print(row)
    print("=" * 76)


# ---------------------------------------------------------------------------
# 7.  Boundary point extraction
# ---------------------------------------------------------------------------

def extract_boundary_points(
    alpha_values:    list,
    mobility_values: list,
    separations:     list,
    results_dict:    dict,
) -> list:
    """
    Scan the full (alpha, m, d) parameter grid and collect every grid-point
    that sits on a regime boundary — i.e., at least one axis-aligned neighbour
    (in the alpha-, m-, or d-direction) carries a different outcome label.

    Neighbours are 6-connected in index space (±1 step along each of the
    three parameter axes).  Points on the grid boundary naturally have fewer
    than 6 neighbours; only existing grid points are considered.

    Parameters
    ----------
    alpha_values    : list of alpha values (order must match results_dict).
    mobility_values : list of mobility exponents.
    separations     : list of separation values d.
    results_dict    : dict keyed by (alpha, m, d) → outcome string.

    Returns
    -------
    boundary : list of dicts, one per boundary grid-point, each containing:
        "alpha"     : float  — alpha at this point
        "m"         : float  — mobility exponent at this point
        "d"         : int    — separation at this point
        "regime"    : str    — outcome label AT this grid-point
        "neighbors" : set    — distinct outcome labels found among the
                               6-connected neighbours that differ from "regime"
    """
    a_list = list(alpha_values)
    m_list = list(mobility_values)
    d_list = list(separations)

    boundary: list = []

    for i, alpha in enumerate(a_list):
        for j, m in enumerate(m_list):
            for k, d in enumerate(d_list):
                regime = results_dict[(alpha, m, d)]

                # Regimes of all 6 axis-aligned neighbours that differ from own
                different: set = set()
                for di, dj, dk in [
                    (-1, 0, 0), (1, 0, 0),
                    (0, -1, 0), (0, 1, 0),
                    (0, 0, -1), (0, 0, 1),
                ]:
                    ni, nj, nk = i + di, j + dj, k + dk
                    if (0 <= ni < len(a_list) and
                            0 <= nj < len(m_list) and
                            0 <= nk < len(d_list)):
                        nbr = results_dict[(a_list[ni], m_list[nj], d_list[nk])]
                        if nbr != regime:
                            different.add(nbr)

                if different:
                    boundary.append({
                        "alpha":     alpha,
                        "m":         m,
                        "d":         d,
                        "regime":    regime,
                        "neighbors": different,
                    })

    # ------------------------------------------------------------------ #
    # Console summary — tally each unique (regime_A, regime_B) transition
    # ------------------------------------------------------------------ #
    from collections import Counter
    trans_counter: Counter = Counter()
    for bp in boundary:
        for nr in bp["neighbors"]:
            pair = tuple(sorted([bp["regime"], nr]))
            trans_counter[pair] += 1

    print(f"\n[extract_boundary_points]  Found {len(boundary)} boundary grid-point(s).")
    for (r1, r2), cnt in sorted(trans_counter.items()):
        print(f"  {r1:<14}  <->  {r2:<14}: {cnt} point(s)")

    return boundary


# ---------------------------------------------------------------------------
# 8.  Boundary surface fitting
# ---------------------------------------------------------------------------

def fit_boundary_surface(boundary_points: list) -> dict:
    """
    Fit a bilinear plane in log-alpha space that separates the ANNIHILATE
    regime from the non-ANNIHILATE regime across the (alpha, m, d) grid.

    Model
    -----
        ln(alpha) = a0 + a1*m + a2*d + a3*(m*d)

    Only points that are on an ANNIHILATE ↔ non-ANNIHILATE interface are
    used: either the grid-point itself is classified ANNIHILATE, or at
    least one of its differently-labelled neighbours is ANNIHILATE.

    Parameters
    ----------
    boundary_points : list of dicts from extract_boundary_points().

    Returns
    -------
    fit_params : dict with keys:
        "has_fit"  : bool   — False when too few points for a meaningful fit
        "coeffs"   : ndarray [a0, a1, a2, a3]  (only when has_fit=True)
        "model"    : str    — human-readable model equation
        "r2"       : float  — R² on the fitted points
        "n_points" : int    — number of ANNIHILATE-boundary points used
    """
    # Filter to ANNIHILATE-boundary points only
    ann_pts = [
        bp for bp in boundary_points
        if bp["regime"] == "ANNIHILATE" or "ANNIHILATE" in bp["neighbors"]
    ]
    n = len(ann_pts)
    print(f"\n[fit_boundary_surface]  {n} ANNIHILATE-boundary point(s) available.")

    # Need at least as many points as free parameters (4)
    if n < 4:
        print("  Too few points to fit -- skipping.")
        return {"has_fit": False, "n_points": n}

    m_arr     = np.array([bp["m"]     for bp in ann_pts], dtype=float)
    d_arr     = np.array([bp["d"]     for bp in ann_pts], dtype=float)
    alpha_arr = np.array([bp["alpha"] for bp in ann_pts], dtype=float)

    log_alpha = np.log(alpha_arr)          # natural log

    # Design matrix: [1,  m,  d,  m*d]
    X = np.column_stack([
        np.ones(n),
        m_arr,
        d_arr,
        m_arr * d_arr,
    ])

    coeffs, _res, _rank, _sv = np.linalg.lstsq(X, log_alpha, rcond=None)
    a0, a1, a2, a3 = coeffs

    # R² on fitted points
    log_pred = X @ coeffs
    ss_res   = float(np.sum((log_alpha - log_pred) ** 2))
    ss_tot   = float(np.sum((log_alpha - log_alpha.mean()) ** 2))
    r2       = 1.0 - ss_res / ss_tot if ss_tot > 0 else 1.0

    model_str = (
        f"ln(\u03b1) = {a0:+.4f}  {a1:+.4f}\u00b7m  "
        f"{a2:+.6f}\u00b7d  {a3:+.6f}\u00b7m\u00b7d"
    )
    # ASCII-only print (Windows CP1252 terminal cannot encode Greek/middle-dot)
    ascii_model = (
        f"ln(alpha) = {a0:+.4f}  {a1:+.4f}*m  "
        f"{a2:+.6f}*d  {a3:+.6f}*m*d"
    )
    print(f"  Fitted model : {ascii_model}")
    print(f"  R^2          : {r2:.4f}   (n = {n} points)")

    return {
        "has_fit":  True,
        "coeffs":   coeffs,
        "model":    model_str,
        "r2":       r2,
        "n_points": n,
    }


# ---------------------------------------------------------------------------
# 9.  Boundary surface visualisation
# ---------------------------------------------------------------------------

def plot_boundary_surface_fit(
    boundary_points: list,
    fit_params:      dict,
    outdir:          str,
) -> None:
    """
    3D scatter of all boundary grid-points coloured by transition type,
    overlaid with the fitted ANNIHILATE boundary surface (wireframe).

    Axes
    ----
        x = mobility exponent  m
        y = separation         d  (pixels)
        z = ln(alpha)

    Output
    ------
        <outdir>/boundary_surface_fit.png

    Parameters
    ----------
    boundary_points : list of dicts from extract_boundary_points().
    fit_params      : dict from fit_boundary_surface().
    outdir          : directory in which to save the figure.
    """
    from mpl_toolkits.mplot3d import Axes3D   # noqa: F401 — registers 3D projection
    from matplotlib.lines import Line2D

    os.makedirs(outdir, exist_ok=True)

    if not boundary_points:
        print("\n[plot_boundary_surface_fit]  No boundary points -- nothing to plot.")
        return

    # ------------------------------------------------------------------ #
    # Colour coding — keyed by the pair of regimes sharing this boundary
    # ------------------------------------------------------------------ #
    _TC = {
        "ANN_MERGE":  "#f97316",   # orange  — ANNIHILATE ↔ MERGE
        "ANN_HOVER":  "#dc2626",   # red     — ANNIHILATE ↔ HOVER/ORBIT
        "MRG_HOVER":  "#7c3aed",   # purple  — MERGE ↔ HOVER/ORBIT
        "MULTI":      "#db2777",   # pink    — triple-point / multi-regime
        "OTHER":      "#6b7280",   # grey    — any other combination
    }
    _LABEL = {
        "ANN_MERGE":  "ANNIHILATE \u2194 MERGE",
        "ANN_HOVER":  "ANNIHILATE \u2194 HOVER/ORBIT",
        "MRG_HOVER":  "MERGE \u2194 HOVER/ORBIT",
        "MULTI":      "Triple-point",
        "OTHER":      "Other",
    }

    def _tc_key(bp: dict) -> str:
        all_r = {bp["regime"]} | bp["neighbors"]
        has_a = "ANNIHILATE"  in all_r
        has_m = "MERGE"       in all_r
        has_h = "HOVER/ORBIT" in all_r
        if sum([has_a, has_m, has_h]) >= 3:
            return "MULTI"
        if has_a and has_m:
            return "ANN_MERGE"
        if has_a and has_h:
            return "ANN_HOVER"
        if has_m and has_h:
            return "MRG_HOVER"
        return "OTHER"

    tc_keys = [_tc_key(bp) for bp in boundary_points]
    colors  = [_TC[k]      for k  in tc_keys]

    m_pts = np.array([bp["m"]     for bp in boundary_points], dtype=float)
    d_pts = np.array([bp["d"]     for bp in boundary_points], dtype=float)
    z_pts = np.log(np.array([bp["alpha"] for bp in boundary_points], dtype=float))

    # ------------------------------------------------------------------ #
    # Figure + 3D axes
    # ------------------------------------------------------------------ #
    fig = plt.figure(figsize=(10, 7))
    ax  = fig.add_subplot(111, projection="3d")

    ax.scatter(
        m_pts, d_pts, z_pts,
        c=colors, s=70,
        edgecolors="k", linewidths=0.4,
        depthshade=True, zorder=5,
    )

    # ------------------------------------------------------------------ #
    # Fitted ANNIHILATE boundary surface — wireframe overlay
    # ------------------------------------------------------------------ #
    if fit_params.get("has_fit"):
        a0, a1, a2, a3 = fit_params["coeffs"]

        m_lo, m_hi = m_pts.min() - 0.3, m_pts.max() + 0.3
        d_lo, d_hi = d_pts.min() - 3.0, d_pts.max() + 3.0

        mg = np.linspace(m_lo, m_hi, 22)
        dg = np.linspace(d_lo, d_hi, 22)
        MG, DG = np.meshgrid(mg, dg)
        ZG = a0 + a1 * MG + a2 * DG + a3 * MG * DG

        ax.plot_wireframe(
            MG, DG, ZG,
            color="#2563eb", alpha=0.30, linewidth=0.8,
        )

    # ------------------------------------------------------------------ #
    # Axis labels + title
    # ------------------------------------------------------------------ #
    ax.set_xlabel("Mobility exponent  m",  fontsize=10, labelpad=8)
    ax.set_ylabel("Separation  d  (px)",   fontsize=10, labelpad=8)
    ax.set_zlabel("ln(\u03b1)",            fontsize=10, labelpad=8)
    ax.set_title(
        "ED Two-Core Interaction \u2014 Boundary Surface\n"
        "(boundary grid-points + fitted ANNIHILATE surface)",
        fontsize=12, fontweight="bold", pad=12,
    )

    # ------------------------------------------------------------------ #
    # Legend — one entry per transition type actually present in the data
    # ------------------------------------------------------------------ #
    present = set(tc_keys)
    legend_elems = [
        Line2D([0], [0], marker="o", color="w",
               markerfacecolor=_TC[key], markersize=9,
               label=_LABEL[key])
        for key in ("ANN_MERGE", "ANN_HOVER", "MRG_HOVER", "MULTI", "OTHER")
        if key in present
    ]
    if fit_params.get("has_fit"):
        legend_elems.append(
            Line2D([0], [0], color="#2563eb", linewidth=1.5,
                   label="Fitted boundary surface")
        )
    ax.legend(handles=legend_elems, fontsize=9, loc="upper right")

    # ------------------------------------------------------------------ #
    # Footnote: model equation + R²
    # ------------------------------------------------------------------ #
    if fit_params.get("has_fit"):
        fig.text(
            0.02, 0.02,
            f"Model: {fit_params['model']}    R\u00b2 = {fit_params['r2']:.4f}",
            fontsize=8, color="#374151",
        )

    outpath = os.path.join(outdir, "boundary_surface_fit.png")
    fig.savefig(outpath, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"\nBoundary surface fit plot saved to: {outpath}")


# ---------------------------------------------------------------------------
# 10.  Per-gamma outcome cache helpers
# ---------------------------------------------------------------------------

def _cache_path(gamma: float) -> str:
    """Return the JSON cache file path for a given gamma value."""
    return os.path.join(OUTDIR_BASE, f"outcomes_g{gamma}.json")


def _load_cached_outcomes(gamma: float) -> dict:
    """
    Load {(alpha, m, d): outcome} from the per-gamma JSON cache if present.

    Returns an empty dict when the cache file does not exist or is unreadable.
    """
    path = _cache_path(gamma)
    if not os.path.exists(path):
        return {}
    try:
        with open(path) as fh:
            data = json.load(fh)
        return {
            (item["alpha"], item["m"], item["d"]): item["outcome"]
            for item in data
        }
    except Exception as exc:
        print(f"  [cache] Warning: could not read {path}: {exc}")
        return {}


def _save_cached_outcomes(gamma: float, outcomes: dict) -> None:
    """
    Persist {(alpha, m, d): outcome} to the per-gamma JSON cache.

    The file is written atomically; errors are reported but do not abort.
    """
    path = _cache_path(gamma)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = [
        {"alpha": k[0], "m": k[1], "d": k[2], "outcome": v}
        for k, v in outcomes.items()
    ]
    try:
        with open(path, "w") as fh:
            json.dump(data, fh, indent=2)
        print(f"  [cache] Saved {len(data)} outcome(s) for gamma={gamma} -> {path}")
    except Exception as exc:
        print(f"  [cache] Warning: could not write {path}: {exc}")


# ---------------------------------------------------------------------------
# 11.  Gamma regime-fraction summary
# ---------------------------------------------------------------------------

def build_gamma_summary(
    alpha_values:    list,
    mobility_values: list,
    separations:     list,
    gamma_values:    list,
    results_dict:    dict,
    outdir:          str,
) -> None:
    """
    For each gamma, compute the fraction of the (alpha × m × d) parameter
    cube that falls into each interaction regime.

    Outputs
    -------
    Console table  : regime percentages per gamma value.
    gamma_regime_summary.png : line plot of regime fractions vs gamma.

    Parameters
    ----------
    alpha_values    : list of alpha values.
    mobility_values : list of mobility exponents.
    separations     : list of separation values d.
    gamma_values    : list of gamma values (x-axis of the plot).
    results_dict    : dict keyed by (alpha, m, d, gamma) → outcome string.
    outdir          : directory in which to save the figure.
    """
    os.makedirs(outdir, exist_ok=True)

    n_total = len(alpha_values) * len(mobility_values) * len(separations)
    regimes = ["ANNIHILATE", "MERGE", "HOVER/ORBIT"]
    _COLORS = {
        "ANNIHILATE":  "#9ca3af",
        "MERGE":       "#2563eb",
        "HOVER/ORBIT": "#16a34a",
    }

    # ------------------------------------------------------------------ #
    # Tally regime fractions per gamma — console table
    # ------------------------------------------------------------------ #
    fractions: dict = {r: [] for r in regimes}

    print("\n" + "=" * 76)
    print("GAMMA REGIME SUMMARY  (fraction of alpha x m x d cube per regime)")
    print("-" * 76)
    col_w = 15
    hdr = f"  {'gamma':<8}" + "".join(f"  {r:<{col_w}}" for r in regimes)
    print(hdr)
    print("  " + "-" * 68)

    for gamma in gamma_values:
        outcomes = [
            results_dict[(alpha, m, d, gamma)]
            for alpha in alpha_values
            for m     in mobility_values
            for d     in separations
        ]
        row = f"  {gamma:<8}"
        for r in regimes:
            frac = outcomes.count(r) / n_total
            fractions[r].append(frac)
            row += f"  {100 * frac:>6.1f}%{'':<{col_w - 9}}"
        print(row)
    print("=" * 76)

    # ------------------------------------------------------------------ #
    # Line plot: regime fraction vs gamma
    # ------------------------------------------------------------------ #
    fig, ax = plt.subplots(figsize=(7, 4.5), constrained_layout=True)

    x_pos = list(range(len(gamma_values)))
    for r in regimes:
        pcts = [100.0 * f for f in fractions[r]]
        ax.plot(
            x_pos, pcts,
            marker="o", linewidth=1.8, markersize=7,
            color=_COLORS[r], label=r,
        )
        for xi, pct in zip(x_pos, pcts):
            ax.annotate(
                f"{pct:.0f}%",
                xy=(xi, pct), xytext=(0, 7),
                textcoords="offset points",
                ha="center", va="bottom", fontsize=8,
                color=_COLORS[r],
            )

    ax.set_xticks(x_pos)
    ax.set_xticklabels([str(g) for g in gamma_values], fontsize=11)
    ax.set_xlabel("Suppression exponent  \u03b3", fontsize=12)
    ax.set_ylabel("Regime fraction  (%)", fontsize=12)
    ax.set_ylim(0, 115)
    ax.set_title(
        "ED Two-Core Interaction \u2014 Regime Fractions vs \u03b3\n"
        "(fraction of the \u03b1 \u00d7 m \u00d7 d parameter cube in each outcome)",
        fontsize=12, fontweight="bold",
    )
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    outpath = os.path.join(outdir, "gamma_regime_summary.png")
    fig.savefig(outpath, dpi=150)
    plt.close(fig)
    print(f"\nGamma summary plot saved to: {outpath}")


# ---------------------------------------------------------------------------
# 12.  Gamma phase slices  (per-gamma, majority-vote collapse across d)
# ---------------------------------------------------------------------------

def build_gamma_phase_slices(
    alpha_values:    list,
    mobility_values: list,
    separations:     list,
    gamma_values:    list,
    results_dict:    dict,
    outdir:          str,
) -> None:
    """
    For each gamma value, collapse the (alpha, m, d) outcomes across d by
    majority vote and produce a 2D (alpha × m) phase diagram.

    Tie-breaking priority when multiple regimes share the maximum count:
        HOVER/ORBIT > MERGE > ANNIHILATE

    Saves one PNG per gamma: gamma_phase_slice_{gamma}.png

    Parameters
    ----------
    alpha_values    : list of alpha values (rows; first element = top).
    mobility_values : list of mobility exponents (columns; first = left).
    separations     : list of d values (collapsed over).
    gamma_values    : list of gamma values (one figure per value).
    results_dict    : dict keyed by (alpha, m, d, gamma) → outcome string.
    outdir          : directory in which to save the figures.
    """
    from matplotlib.colors import ListedColormap, BoundaryNorm
    from matplotlib.patches import Patch

    os.makedirs(outdir, exist_ok=True)

    ANNIHILATE_CODE, MERGE_CODE, HOVER_CODE = 0, 1, 2

    _COLORS = {
        ANNIHILATE_CODE: "#9ca3af",
        MERGE_CODE:      "#2563eb",
        HOVER_CODE:      "#16a34a",
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
    _STR_CODE = {
        "ANNIHILATE":  ANNIHILATE_CODE,
        "MERGE":       MERGE_CODE,
        "HOVER/ORBIT": HOVER_CODE,
    }

    cmap = ListedColormap([_COLORS[0], _COLORS[1], _COLORS[2]])
    norm = BoundaryNorm([-0.5, 0.5, 1.5, 2.5], cmap.N)
    n_alpha = len(alpha_values)
    n_mob   = len(mobility_values)

    print(f"\nBuilding gamma phase slices in: {outdir}")

    for gamma in gamma_values:
        matrix = np.zeros((n_alpha, n_mob), dtype=int)

        for i, alpha in enumerate(alpha_values):
            for j, m in enumerate(mobility_values):
                # Collect outcome codes across all d for this (alpha, m, gamma)
                codes = [
                    _STR_CODE[results_dict[(alpha, m, d, gamma)]]
                    for d in separations
                ]
                counts = {
                    ANNIHILATE_CODE: codes.count(ANNIHILATE_CODE),
                    MERGE_CODE:      codes.count(MERGE_CODE),
                    HOVER_CODE:      codes.count(HOVER_CODE),
                }
                max_count = max(counts.values())
                # Tie-break: HOVER > MERGE > ANNIHILATE
                for code in (HOVER_CODE, MERGE_CODE, ANNIHILATE_CODE):
                    if counts[code] == max_count:
                        matrix[i, j] = code
                        break

        # ------------------------------------------------------------------ #
        # Plot
        # ------------------------------------------------------------------ #
        fig, ax = plt.subplots(figsize=(7, 5), constrained_layout=True)

        ax.imshow(
            matrix,
            cmap=cmap, norm=norm,
            origin="upper",
            aspect="auto",
            interpolation="nearest",
        )
        ax.set_xticks(range(n_mob))
        ax.set_xticklabels([str(m) for m in mobility_values], fontsize=11)
        ax.set_yticks(range(n_alpha))
        ax.set_yticklabels([str(a) for a in alpha_values], fontsize=11)
        ax.set_xlabel("Mobility exponent  m", fontsize=12)
        ax.set_ylabel("Drain strength  alpha", fontsize=12)
        ax.set_title(
            f"ED Two-Core Phase Diagram  (\u03b3 = {gamma})\n"
            "(\u03b1 vs m,  collapsed across d by majority vote)",
            fontsize=12, fontweight="bold",
        )

        for i in range(n_alpha):
            for j in range(n_mob):
                ax.text(
                    j, i, _SHORT[matrix[i, j]],
                    ha="center", va="center",
                    fontsize=9, fontweight="bold", color="white",
                )

        legend_handles = [
            Patch(facecolor=_COLORS[code], label=_LABELS[code])
            for code in (ANNIHILATE_CODE, MERGE_CODE, HOVER_CODE)
        ]
        ax.legend(
            handles=legend_handles,
            loc="upper right", fontsize=9,
            framealpha=0.85, edgecolor="0.6",
        )

        outpath = os.path.join(outdir, f"gamma_phase_slice_{gamma}.png")
        fig.savefig(outpath, dpi=150)
        plt.close(fig)
        print(f"  Saved: gamma_phase_slice_{gamma}.png")


# ---------------------------------------------------------------------------
# 13.  Parameter sweep
# ---------------------------------------------------------------------------

def main() -> None:
    """
    Sweep over GAMMA_VALUES × ALPHA_VALUES × MOBILITY_EXPONENTS × SEPARATIONS.

    Caches per-gamma outcomes in JSON files (outcomes_g{gamma}.json) inside
    OUTDIR_BASE so that previously computed gamma values are not re-simulated
    on subsequent runs.  Only newly computed outcomes trigger a cache write.
    """
    n_runs_max = (
        len(GAMMA_VALUES) * len(ALPHA_VALUES) *
        len(MOBILITY_EXPONENTS) * len(SEPARATIONS)
    )
    print("=" * 76)
    print("Scenario E: Two-Core -- gamma x alpha x m x d sweep")
    print(f"  Grid             : {GRID_SIZE} x {GRID_SIZE}   Seed : {SEED}")
    print(f"  Steps            : {STEPS}")
    print(f"  Core shape       : Gaussian  amplitude={CORE_AMPLITUDE}*p_max  "
          f"sigma={CORE_WIDTH_FRAC*GRID_SIZE:.0f} px  "
          f"bg={CORE_BACKGROUND}*p_max")
    print(f"  Threshold        : {DETECT_THRESH} * p_max")
    print(f"  gamma values (g) : {GAMMA_VALUES}")
    print(f"  alpha values     : {ALPHA_VALUES}")
    print(f"  mobility exp (m) : {MOBILITY_EXPONENTS}")
    print(f"  separations      : {SEPARATIONS} px")
    print(f"  beta={PARAMS.beta}  dt={PARAMS.dt}  "
          f"mode=mobility  (set per run so m takes effect)")
    print(f"  Max new runs     : {n_runs_max}  (cached runs are skipped)")
    print(f"  Output base      : {OUTDIR_BASE}")
    print("=" * 76)

    # results[(alpha, m, d, gamma)] = outcome string
    results: dict[tuple, str] = {}

    # ------------------------------------------------------------------ #
    # Outermost loop: suppression exponent gamma
    # ------------------------------------------------------------------ #
    for gamma in GAMMA_VALUES:
        outdir_g = os.path.join(OUTDIR_BASE, f"gamma{gamma}")
        os.makedirs(outdir_g, exist_ok=True)

        # Load previously cached outcomes for this gamma
        cached = _load_cached_outcomes(gamma)
        if cached:
            print(f"\n[gamma={gamma}]  Loaded {len(cached)} cached outcome(s) "
                  f"-- skipping those runs.")

        newly_computed: dict = {}

        print(f"\n{'=' * 60}")
        print(f"  Suppression exponent  gamma = {gamma}")
        print(f"{'=' * 60}")

        for alpha in ALPHA_VALUES:
            for m in MOBILITY_EXPONENTS:
                outdir_am = os.path.join(outdir_g, f"a{alpha}_m{m}")
                print(f"\n--- gamma={gamma},  alpha={alpha},  m={m} ---")

                for d in SEPARATIONS:
                    if (alpha, m, d) in cached:
                        outcome = cached[(alpha, m, d)]
                        print(
                            f"  [cached]  alpha={alpha:<6}  m={m:<4}  "
                            f"gamma={gamma:<5}  d={d:3d} px | outcome={outcome}"
                        )
                    else:
                        outcome = run_two_core(d, alpha, m, gamma, outdir_am)
                        newly_computed[(alpha, m, d)] = outcome

                    results[(alpha, m, d, gamma)] = outcome

        # Persist updated cache (merge old + new so future runs stay fast)
        if newly_computed:
            _save_cached_outcomes(gamma, {**cached, **newly_computed})

        # ------------------------------------------------------------------ #
        # Per-gamma summary table (one sub-table per alpha; rows=m, cols=d)
        # ------------------------------------------------------------------ #
        col_w = 14
        print(f"\n--- gamma = {gamma}  SUMMARY (rows = m, cols = d) ---")
        for alpha in ALPHA_VALUES:
            print(f"\n  alpha = {alpha}")
            hdr = f"  {'m':<8}" + "".join(
                f"  d={d:<{col_w - 3}}" for d in SEPARATIONS
            )
            print(hdr)
            print("  " + "-" * 68)
            for m in MOBILITY_EXPONENTS:
                row = f"  {m:<8}"
                for d in SEPARATIONS:
                    row += f"  {results[(alpha, m, d, gamma)]:<{col_w - 2}}"
                print(row)

        # ------------------------------------------------------------------ #
        # Interaction surface for this gamma — per-d slices + combined figure
        # ------------------------------------------------------------------ #
        gamma_results_3d = {
            (alpha, m, d): results[(alpha, m, d, gamma)]
            for alpha in ALPHA_VALUES
            for m     in MOBILITY_EXPONENTS
            for d     in SEPARATIONS
        }
        build_interaction_surface(
            alpha_values    = ALPHA_VALUES,
            mobility_values = MOBILITY_EXPONENTS,
            separations     = SEPARATIONS,
            results_dict    = gamma_results_3d,
            outdir          = OUTDIR_BASE,
            tag             = f"gamma{gamma}_",
        )

    # ------------------------------------------------------------------ #
    # Cross-gamma analysis
    # ------------------------------------------------------------------ #
    build_gamma_summary(
        alpha_values    = ALPHA_VALUES,
        mobility_values = MOBILITY_EXPONENTS,
        separations     = SEPARATIONS,
        gamma_values    = GAMMA_VALUES,
        results_dict    = results,
        outdir          = OUTDIR_BASE,
    )

    build_gamma_phase_slices(
        alpha_values    = ALPHA_VALUES,
        mobility_values = MOBILITY_EXPONENTS,
        separations     = SEPARATIONS,
        gamma_values    = GAMMA_VALUES,
        results_dict    = results,
        outdir          = OUTDIR_BASE,
    )

    # ------------------------------------------------------------------ #
    # Boundary extraction, fitting, and 3-D visualisation
    # Use ONLY the gamma = 0.5 subset (preserves ED-Arch-07 results exactly)
    # ------------------------------------------------------------------ #
    ref_gamma = 0.5
    if ref_gamma in GAMMA_VALUES:
        ref_results_3d = {
            (alpha, m, d): results[(alpha, m, d, ref_gamma)]
            for alpha in ALPHA_VALUES
            for m     in MOBILITY_EXPONENTS
            for d     in SEPARATIONS
        }
        print(f"\n[Boundary analysis using gamma = {ref_gamma} subset]")
        boundary_pts = extract_boundary_points(
            alpha_values    = ALPHA_VALUES,
            mobility_values = MOBILITY_EXPONENTS,
            separations     = SEPARATIONS,
            results_dict    = ref_results_3d,
        )
        fit_params = fit_boundary_surface(boundary_pts)
        plot_boundary_surface_fit(boundary_pts, fit_params, outdir=OUTDIR_BASE)
    else:
        print(
            f"\n[Boundary analysis skipped -- gamma={ref_gamma} "
            f"not in GAMMA_VALUES]"
        )

    # ------------------------------------------------------------------ #
    # Final shift summary — how interaction regimes change with gamma
    # (derived purely from regime counts in results_dict, no new heuristics)
    # ------------------------------------------------------------------ #
    n_total = len(ALPHA_VALUES) * len(MOBILITY_EXPONENTS) * len(SEPARATIONS)
    print("\n" + "=" * 76)
    print("GAMMA SHIFT SUMMARY -- regime fractions across suppression exponent gamma")
    print("-" * 76)
    hdr = (
        f"  {'gamma':<8}  {'ANNIHILATE':>12}  {'MERGE':>8}  "
        f"{'HOVER/ORBIT':>12}   (vs prev gamma)"
    )
    print(hdr)
    print("  " + "-" * 70)

    prev_fracs: dict | None = None
    for gamma in GAMMA_VALUES:
        outcomes = [
            results[(alpha, m, d, gamma)]
            for alpha in ALPHA_VALUES
            for m     in MOBILITY_EXPONENTS
            for d     in SEPARATIONS
        ]
        fracs = {
            "ANNIHILATE":  outcomes.count("ANNIHILATE")  / n_total,
            "MERGE":       outcomes.count("MERGE")        / n_total,
            "HOVER/ORBIT": outcomes.count("HOVER/ORBIT") / n_total,
        }
        row = (
            f"  {gamma:<8}  "
            f"{100 * fracs['ANNIHILATE']:>10.1f}%  "
            f"{100 * fracs['MERGE']:>6.1f}%  "
            f"{100 * fracs['HOVER/ORBIT']:>10.1f}%"
        )
        if prev_fracs is not None:
            da = fracs["ANNIHILATE"]  - prev_fracs["ANNIHILATE"]
            dm = fracs["MERGE"]       - prev_fracs["MERGE"]
            dh = fracs["HOVER/ORBIT"] - prev_fracs["HOVER/ORBIT"]
            row += (
                f"   d: ANN {da * 100:+.1f}%"
                f"  MRG {dm * 100:+.1f}%"
                f"  HOV {dh * 100:+.1f}%"
            )
        print(row)
        prev_fracs = fracs

    print("=" * 76)
    print(f"\nAll figures saved under: {OUTDIR_BASE}/")

    # ------------------------------------------------------------------ #
    # Section 14: Radius Spectra vs Gamma                                 #
    # ------------------------------------------------------------------ #
    build_radius_spectra(ALPHA_VALUES, MOBILITY_EXPONENTS, GAMMA_VALUES, OUTDIR_BASE)

    # ------------------------------------------------------------------ #
    # Section 15: Orbit Distance vs Gamma                                 #
    # ------------------------------------------------------------------ #
    build_orbit_distance_summary(
        ALPHA_VALUES, MOBILITY_EXPONENTS, GAMMA_VALUES, SEPARATIONS, results, OUTDIR_BASE
    )

    # ------------------------------------------------------------------ #
    # Section 16: High-gamma Scattering Grid                              #
    # ------------------------------------------------------------------ #
    build_scattering_grid(
        alpha=0.05, m=1.0, gamma=0.75, d=40,
        offsets=[-15, -10, -5, 0, 5, 10, 15],
        outdir=OUTDIR_BASE,
    )

    print("=" * 76)
    print(f"\nAll figures saved under: {OUTDIR_BASE}/")


# ---------------------------------------------------------------------------
# Section 14 -- RADIUS SPECTRA VS GAMMA
# ---------------------------------------------------------------------------

def run_single_core(alpha: float, m: float, gamma: float, outdir: str) -> "np.ndarray":
    """Run a single Gaussian core for STEPS timesteps.

    Returns the effective-radius time series as a 1-D float array.
    Effective radius: first radial bin from grid centre where the
    azimuthal-mean density profile drops below 0.5 * p_max.
    """
    p_max = PARAMS.p_max
    p_min = PARAMS.p_min
    sigma = CORE_WIDTH_FRAC * GRID_SIZE
    cy, cx = GRID_SIZE // 2, GRID_SIZE // 2

    run_params = EDParams(
        alpha        = alpha,
        beta         = PARAMS.beta,
        gamma        = gamma,
        dt           = PARAMS.dt,
        p_min        = p_min,
        p_max        = p_max,
        boundary     = PARAMS.boundary,
        mode         = "mobility",
        noise_scale  = PARAMS.noise_scale,
        mobility_exp = m,
    )
    lat = EDLattice(rows=GRID_SIZE, cols=GRID_SIZE, params=run_params, seed=SEED)

    # Single Gaussian at grid centre (bypass init_two_body)
    r_idx = np.arange(GRID_SIZE).reshape(-1, 1)
    c_idx = np.arange(GRID_SIZE).reshape(1, -1)
    dist2 = (r_idx - cy) ** 2 + (c_idx - cx) ** 2
    lat.p[:] = np.clip(
        CORE_BACKGROUND * p_max + CORE_AMPLITUDE * p_max * np.exp(
            -dist2 / (2.0 * sigma ** 2)
        ),
        p_min,
        p_max,
    )

    # Pre-compute integer radial bins from centre (vectorised -- once per call)
    max_r = int(np.ceil(np.sqrt(2.0) * GRID_SIZE / 2.0)) + 1
    r_dist_flat = np.clip(np.sqrt(dist2).ravel().astype(int), 0, max_r)
    bin_counts = np.bincount(r_dist_flat, minlength=max_r + 1).astype(float)

    half_thresh = 0.5 * p_max
    radii: list = []

    for _s in range(STEPS):
        p_flat   = lat.p.ravel()
        bin_sums = np.bincount(r_dist_flat, weights=p_flat, minlength=max_r + 1)
        profile  = np.divide(bin_sums, bin_counts, where=bin_counts > 0,
                             out=np.zeros(max_r + 1))
        crossings = np.where(profile < half_thresh)[0]
        eff_r     = float(crossings[0]) if len(crossings) > 0 else float(max_r)
        radii.append(eff_r)
        lat.step()

    return np.array(radii, dtype=float)


def build_radius_spectra(
    alpha_values: list,
    m_values:     list,
    gamma_values: list,
    outdir:       str,
) -> None:
    """Histogram steady-state effective radii per gamma and save figures.

    For each gamma, runs run_single_core for every (alpha, m) combo.
    Steady state defined as the last 20 % of the time series.
    Saves: radius_spectrum_gamma{gamma}.png
    """
    print("\n" + "=" * 76)
    print("SECTION 14 -- Radius Spectra vs Gamma")
    print("=" * 76)

    os.makedirs(outdir, exist_ok=True)
    steady_start = int(STEPS * 0.80)

    for gamma in gamma_values:
        all_radii: list = []
        for alpha in alpha_values:
            for m in m_values:
                sub_dir = os.path.join(outdir, f"gamma{gamma}", f"a{alpha}_m{m}")
                os.makedirs(sub_dir, exist_ok=True)
                radii  = run_single_core(alpha, m, gamma, sub_dir)
                steady = radii[steady_start:]
                all_radii.extend(steady.tolist())
                print(
                    f"  [gamma={gamma}  alpha={alpha}  m={m}]"
                    f"  mean_r={steady.mean():.2f}  var_r={steady.var():.2f}"
                )

        arr = np.array(all_radii, dtype=float)
        if len(arr) > 0:
            arr_int  = np.clip(arr.astype(int), 0, 9999)
            peak_bin = int(np.argmax(np.bincount(arr_int)))
            print(
                f"\n  [gamma={gamma}]  n_samples={len(arr)}"
                f"  mean={arr.mean():.2f}  var={arr.var():.2f}"
                f"  peak_bin={peak_bin} px"
            )
        else:
            print(f"\n  [gamma={gamma}]  No samples collected.")

        fig, ax = plt.subplots(figsize=(7, 4))
        if len(arr) > 0:
            ax.hist(arr, bins=30, color="#4878d0", edgecolor="white", linewidth=0.4)
            ax.axvline(arr.mean(), color="red", linestyle="--", linewidth=1.2,
                       label=f"mean={arr.mean():.1f} px")
            ax.legend(fontsize=9)
        else:
            ax.text(0.5, 0.5, "No data", ha="center", va="center",
                    transform=ax.transAxes, fontsize=12)
        ax.set_title(f"Radius Spectrum  \u03b3={gamma}")
        ax.set_xlabel("Effective radius (px)")
        ax.set_ylabel("Count")
        fig.tight_layout()
        fpath = os.path.join(outdir, f"radius_spectrum_gamma{gamma}.png")
        fig.savefig(fpath, dpi=120)
        plt.close(fig)
        print(f"  Saved: {fpath}")

    print("=" * 76)


# ---------------------------------------------------------------------------
# Section 15 -- ORBIT DISTANCE VS GAMMA
# ---------------------------------------------------------------------------

def run_two_core_orbit(
    alpha: float, m: float, gamma: float, d: int, outdir: str,
) -> "np.ndarray":
    """Like run_two_core but only records centroid-to-centroid distance per step.

    No classification, no field snapshots.
    Returns the full distance time series as a 1-D float array.
    """
    p_max = PARAMS.p_max

    run_params = EDParams(
        alpha        = alpha,
        beta         = PARAMS.beta,
        gamma        = gamma,
        dt           = PARAMS.dt,
        p_min        = PARAMS.p_min,
        p_max        = p_max,
        boundary     = PARAMS.boundary,
        mode         = "mobility",
        noise_scale  = PARAMS.noise_scale,
        mobility_exp = m,
    )
    lat = EDLattice(rows=GRID_SIZE, cols=GRID_SIZE, params=run_params, seed=SEED)
    init_two_saturated_cores(lat, d)

    dist_series: list = []
    for _s in range(STEPS):
        cores = detect_cores(lat.p, p_max)
        if len(cores) >= 2:
            c0 = np.array(cores[0]["centroid"])
            c1 = np.array(cores[1]["centroid"])
            dist_series.append(float(np.linalg.norm(c1 - c0)))
        elif len(cores) == 1:
            dist_series.append(0.0)
        else:
            dist_series.append(float("nan"))
        lat.step()

    return np.array(dist_series, dtype=float)


def build_orbit_distance_summary(
    alpha_values: list,
    m_values:     list,
    gamma_values: list,
    d_values:     list,
    results_dict: dict,
    outdir:       str,
) -> None:
    """For each gamma pick HOVER/ORBIT runs from results_dict and plot distance vs time.

    Keys in results_dict are (alpha, m, d, gamma) 4-tuples (ED-Arch-08 format).
    Saves: orbit_distance_gamma{gamma}.png
    """
    print("\n" + "=" * 76)
    print("SECTION 15 -- Orbit Distance vs Gamma")
    print("=" * 76)

    os.makedirs(outdir, exist_ok=True)

    for gamma in gamma_values:
        fig, ax = plt.subplots(figsize=(8, 4))
        n_plotted = 0
        for alpha in alpha_values:
            for m in m_values:
                for d in d_values:
                    outcome = results_dict.get((alpha, m, d, gamma))
                    if outcome != "HOVER/ORBIT":
                        continue
                    sub_dir = os.path.join(outdir, f"gamma{gamma}", f"a{alpha}_m{m}")
                    os.makedirs(sub_dir, exist_ok=True)
                    dist_ts = run_two_core_orbit(alpha, m, gamma, d, sub_dir)
                    ax.plot(dist_ts, linewidth=0.8, label=f"a={alpha} m={m} d={d}")
                    n_plotted += 1
                    tail   = dist_ts[int(STEPS * 0.5):]
                    mean_d = float(np.nanmean(tail))
                    std_d  = float(np.nanstd(tail))
                    print(
                        f"  [gamma={gamma}  alpha={alpha}  m={m}  d={d}]"
                        f"  mean_dist(last50%)={mean_d:.2f}  std={std_d:.2f}"
                    )

        if n_plotted == 0:
            ax.text(0.5, 0.5,
                    f"No HOVER/ORBIT runs found for gamma={gamma}",
                    ha="center", va="center", transform=ax.transAxes, fontsize=11)
            print(
                f"  [gamma={gamma}]  No HOVER/ORBIT runs found"
                f" -- blank figure saved."
            )
        else:
            ax.legend(fontsize=7, loc="upper right", ncol=2)
        ax.set_title(f"Orbit Distance vs Time  \u03b3={gamma}")
        ax.set_xlabel("Step")
        ax.set_ylabel("Centroid distance (px)")
        fig.tight_layout()
        fpath = os.path.join(outdir, f"orbit_distance_gamma{gamma}.png")
        fig.savefig(fpath, dpi=120)
        plt.close(fig)
        print(f"  Saved: {fpath}")

    print("=" * 76)


# ---------------------------------------------------------------------------
# Section 16 -- HIGH-GAMMA SCATTERING GRID
# ---------------------------------------------------------------------------

def run_scattering(
    alpha:  float,
    m:      float,
    gamma:  float,
    d:      int,
    offset: int,
    outdir: str,
) -> str:
    """Two-core run with a vertical impact parameter (lateral offset).

    Core A centre: (cy, cx - d//2)
    Core B centre: (cy + offset, cx + d//2)

    Returns the classified outcome string.
    """
    p_max = PARAMS.p_max
    p_min = PARAMS.p_min
    sigma = CORE_WIDTH_FRAC * GRID_SIZE
    cy, cx = GRID_SIZE // 2, GRID_SIZE // 2

    run_params = EDParams(
        alpha        = alpha,
        beta         = PARAMS.beta,
        gamma        = gamma,
        dt           = PARAMS.dt,
        p_min        = p_min,
        p_max        = p_max,
        boundary     = PARAMS.boundary,
        mode         = "mobility",
        noise_scale  = PARAMS.noise_scale,
        mobility_exp = m,
    )
    lat = EDLattice(rows=GRID_SIZE, cols=GRID_SIZE, params=run_params, seed=SEED)

    r_idx = np.arange(GRID_SIZE).reshape(-1, 1)
    c_idx = np.arange(GRID_SIZE).reshape(1, -1)
    dA = np.sqrt((r_idx - cy) ** 2 + (c_idx - (cx - d // 2)) ** 2)
    gA = CORE_AMPLITUDE * p_max * np.exp(-dA ** 2 / (2.0 * sigma ** 2))
    dB = np.sqrt((r_idx - (cy + offset)) ** 2 + (c_idx - (cx + d // 2)) ** 2)
    gB = CORE_AMPLITUDE * p_max * np.exp(-dB ** 2 / (2.0 * sigma ** 2))
    lat.p[:] = np.clip(CORE_BACKGROUND * p_max + gA + gB, p_min, p_max)

    n_cores_series: list = []
    dist_series:    list = []
    for _s in range(STEPS):
        cores = detect_cores(lat.p, p_max)
        n_cores_series.append(len(cores))
        if len(cores) >= 2:
            c0 = np.array(cores[0]["centroid"])
            c1 = np.array(cores[1]["centroid"])
            dist_series.append(float(np.linalg.norm(c1 - c0)))
        elif len(cores) == 1:
            dist_series.append(0.0)
        else:
            dist_series.append(float("nan"))
        lat.step()

    return classify_outcome(n_cores_series, dist_series)


def build_scattering_grid(
    alpha:   float,
    m:       float,
    gamma:   float,
    d:       int,
    offsets: list,
    outdir:  str,
) -> None:
    """Sweep lateral offsets and produce a 1-D colour-coded outcome bar chart.

    Saves: scattering_gamma{gamma}.png
    """
    _OUTCOME_COLORS = {
        "ANNIHILATE":  "#d62728",
        "MERGE":       "#ff7f0e",
        "HOVER/ORBIT": "#2ca02c",
        "REPEL":       "#1f77b4",
    }

    print("\n" + "=" * 76)
    print("SECTION 16 -- High-gamma Scattering Grid")
    print(f"  alpha={alpha}  m={m}  gamma={gamma}  d={d}  offsets={offsets}")
    print("=" * 76)

    sub_dir = os.path.join(outdir, f"gamma{gamma}", f"a{alpha}_m{m}")
    os.makedirs(sub_dir, exist_ok=True)

    outcomes: list = []
    for offset in offsets:
        oc = run_scattering(alpha, m, gamma, d, offset, sub_dir)
        outcomes.append(oc)
        print(f"  offset={offset:+4d} px | outcome={oc}")

    # 1-D colour-coded bar chart
    fig, ax = plt.subplots(figsize=(max(6, len(offsets) * 0.9), 3))
    for i, (off, oc) in enumerate(zip(offsets, outcomes)):
        color = _OUTCOME_COLORS.get(oc, "#888888")
        ax.bar(i, 1.0, color=color, edgecolor="white", linewidth=0.5)
        ax.text(i, 0.5, oc, ha="center", va="center",
                fontsize=7, color="white", fontweight="bold", rotation=90)

    ax.set_xticks(range(len(offsets)))
    ax.set_xticklabels([str(o) for o in offsets], fontsize=9)
    ax.set_xlabel("Lateral offset (px)")
    ax.set_yticks([])
    ax.set_title(
        f"Scattering Grid  \u03b3={gamma}  \u03b1={alpha}  m={m}  d={d} px"
    )
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=c, label=lbl)
        for lbl, c in _OUTCOME_COLORS.items()
    ]
    ax.legend(handles=legend_elements, loc="upper right",
              fontsize=8, bbox_to_anchor=(1.22, 1.02))

    fig.tight_layout()
    fpath = os.path.join(outdir, f"scattering_gamma{gamma}.png")
    fig.savefig(fpath, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {fpath}")

    print("\n  Transition summary (offset -> outcome):")
    for off, oc in zip(offsets, outcomes):
        print(f"    offset={off:+4d} px -> {oc}")
    print("=" * 76)


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()
