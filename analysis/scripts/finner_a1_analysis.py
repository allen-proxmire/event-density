"""
ED Test A1.0: Finner et al. (2025) 25-Subcluster Analysis
==========================================================
Purpose
-------
Pipeline infrastructure for the Event Density cluster-merger wake test
using the 25 subclusters from the existing Table 2 compilation in
papers/Cluster_Merger_Lag_Evidence/paper.md, section 3.10.

Per-subcluster BCG-WL offsets are from Finner et al. (2025) Figure 36,
visually digitized in the merger-lag paper. v_peri and TSP are
literature-sourced per cluster (Golovich+2019, MCMAC reconstructions,
and individual dynamical studies -- see merger-lag paper Table 2).

v_current is computed from (v_peri, TSP) via the Keplerian deceleration
trajectory used in analysis/scripts/wake_derivation.py:
    v(t) = v_peri * sqrt(max(0, 1 - (t/T_apo)^2)),  T_apo = 1.0 Gyr default.

Five models are fit and compared:
    Model 1  ED velocity scaling  : offset = A / v_current        (1 free)
    Model 2  ED deceleration      : offset = B * TSP              (1 free)
    Model 3  ED full prediction   : offset = D_T / v_current       (0 free)
    Model 4  SIDM-like            : offset = D * v_current^n       (2 free)
    Model 5  flat baseline        : offset = const                 (1 free)
    LCDM reference                : offset ~ 1 kpc (Roche+2024)

Outputs (all under data/ED-Finner/):
    merged_table.csv
    plots/01_offset_vs_inv_vcurrent.png
    plots/02_offset_vs_TSP.png
    plots/03_residuals.png
    plots/04_offset_histogram.png
    results/fit_coefficients.csv
    results/summary.txt

This is A1.0 (infrastructure stage). It does NOT digitize the remaining
33 Finner points, and it does NOT attempt scientific interpretation.
It just runs the fits on the existing 25 and reports the numbers.

Usage
-----
    python analysis/scripts/finner_a1_analysis.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import spearmanr, pearsonr

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
D_T = 2.1e27           # m^2 / s   (ED temporal diffusivity)
kpc = 3.086e19          # m per kpc
Gyr = 3.156e16          # s per Gyr
LCDM_BASELINE_KPC = 1.0  # Roche+2024 median DM-BCG offset in LCDM

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "data" / "ED-Finner"
PLOTS_DIR = DATA_DIR / "plots"
RESULTS_DIR = DATA_DIR / "results"
OFFSETS_CSV = DATA_DIR / "digitized_offsets.csv"
MERGED_CSV = DATA_DIR / "merged_table.csv"

for d in (PLOTS_DIR, RESULTS_DIR):
    d.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Per-cluster TSP and v_peri (literature, keyed by cluster)
# Sources: merger-lag paper Table 2 + figS4_finner_TSP_distribution compilation
# ---------------------------------------------------------------------------
CLUSTER_META = {
    # cluster_key : (v_peri_kms, TSP_Gyr, T_apo_Gyr, v_peri_source)
    "1RXSJ0603": (1500, 1.3,  1.5, "Bruggen+2012 sim"),
    "A115":      (1600, 0.10, 1.5, "Barrena+2007 vLOS (pre-pericenter)"),
    "A2034":     (547,  0.20, 1.0, "Machado+2021 3D"),
    "A2163":     (4500, 0.50, 1.2, "Bourdin+2011 shock Mach"),
    "A2255":     (2635, 0.15, 1.2, "Sakelliou+2006"),
    "A2744":     (4500, 0.55, 1.5, "Owers+2011 vLOS"),
    "A3411":     (800,  1.00, 1.0, "van Weeren+2017 / this work"),
    "CIZAJ2242": (2500, 1.00, 1.2, "Molnar+2017 hydro sim"),
    "MACSJ1149": (2770, 1.16, 1.5, "Golovich+2016 MCMAC"),
    "ZwCl0008":  (1800, 0.76, 1.05, "Golovich+2017 MCMAC"),
    "ZwCl2341":  (1900, 0.50, 1.2, "Benson+2017 MCMAC"),
}


def v_current(v_peri_kms: float, TSP_Gyr: float, T_apo_Gyr: float) -> float:
    """Keplerian deceleration: v(t) = v_peri * sqrt(max(0, 1 - (t/T_apo)^2)).

    Returns v_current in km/s.
    """
    if TSP_Gyr >= T_apo_Gyr:
        # Past apocenter -- set to a floor so 1/v_current remains finite.
        return 50.0
    ratio = TSP_Gyr / T_apo_Gyr
    return float(v_peri_kms * np.sqrt(max(0.0, 1.0 - ratio * ratio)))


# ---------------------------------------------------------------------------
# Step 1: load digitized offsets and build the merged table
# ---------------------------------------------------------------------------
def build_merged_table() -> pd.DataFrame:
    df = pd.read_csv(OFFSETS_CSV)
    n = len(df)

    v_peri_arr = np.empty(n)
    TSP_arr = np.empty(n)
    Tapo_arr = np.empty(n)
    v_now_arr = np.empty(n)
    src_arr = []

    for i, row in df.iterrows():
        meta = CLUSTER_META.get(row["cluster"])
        if meta is None:
            raise KeyError(f"No CLUSTER_META for {row['cluster']}")
        vp, tsp, ta, src = meta
        vn = v_current(vp, tsp, ta)
        v_peri_arr[i] = vp
        TSP_arr[i] = tsp
        Tapo_arr[i] = ta
        v_now_arr[i] = vn
        src_arr.append(src)

    df["v_peri_kms"] = v_peri_arr
    df["TSP_Gyr"] = TSP_arr
    df["T_apo_Gyr"] = Tapo_arr
    df["v_current_kms"] = v_now_arr
    df["v_peri_source"] = src_arr

    ordered_cols = [
        "cluster", "subcluster_id", "offset_kpc", "offset_err_kpc",
        "tracer_type", "v_peri_kms", "TSP_Gyr", "T_apo_Gyr",
        "v_current_kms", "v_peri_source", "source_note",
    ]
    df = df[ordered_cols]
    df.to_csv(MERGED_CSV, index=False)
    return df


# ---------------------------------------------------------------------------
# Step 2: five-model fits
# ---------------------------------------------------------------------------
def ed_prediction_D_T_over_v(v_kms):
    """ED steady-state offset in kpc: D_T / v. Uncapped."""
    v = np.asarray(v_kms) * 1e3   # m/s
    return (D_T / v) / kpc         # kpc


def ed_prediction_capped(v_kms, TSP_Gyr):
    """
    ED offset with apocenter / equilibration-time cap (A1.0b correction).

    Physics: the wake reaches its steady-state length D_T/v on timescale
    t_lag = D_T / v^2.  If TSP < t_lag, the wake has only partially filled
    to a length v*TSP (the distance the source has travelled), so the
    observable offset is bounded above by v*TSP.

    Implementation:
        l_cap = min(D_T / v_current ,  v_current * TSP)

    This is equivalent to (D_T/v) * min(1, TSP / t_lag), which is the
    finite-time equilibration limit used implicitly for ZwCl 0008 in
    papers/Cluster_Merger_Lag_Evidence/paper.md.
    """
    v = np.asarray(v_kms) * 1e3                    # m/s
    t = np.asarray(TSP_Gyr) * Gyr                  # s
    l_steady = (D_T / v) / kpc                     # kpc
    l_filled = (v * t) / kpc                       # kpc
    return np.minimum(l_steady, l_filled)


def weighted_chi2(obs, model, err):
    return float(np.sum(((obs - model) / err) ** 2))


def r_squared(obs, model):
    ss_res = np.sum((obs - model) ** 2)
    ss_tot = np.sum((obs - np.mean(obs)) ** 2)
    return float(1.0 - ss_res / ss_tot) if ss_tot > 0 else 0.0


def bic(chi2, k_params, n):
    return chi2 + k_params * np.log(n)


def fit_models(df: pd.DataFrame) -> dict:
    obs = df["offset_kpc"].values.astype(float)
    err = df["offset_err_kpc"].values.astype(float)
    vc = df["v_current_kms"].values.astype(float)
    tsp = df["TSP_Gyr"].values.astype(float)
    n = len(obs)

    results = {}

    # Model 1: offset = A / v_current
    def m1(v, A): return A / v
    popt, pcov = curve_fit(m1, vc, obs, p0=[1e5], sigma=err, absolute_sigma=False)
    A1 = popt[0]
    sA1 = float(np.sqrt(pcov[0, 0]))
    pred1 = m1(vc, A1)
    chi2_1 = weighted_chi2(obs, pred1, err)
    results["Model_1_ED_inv_v"] = dict(
        A=A1, A_err=sA1,
        chi2=chi2_1, dof=n - 1, reduced_chi2=chi2_1 / (n - 1),
        r2=r_squared(obs, pred1),
        BIC=bic(chi2_1, 1, n),
        formula="offset = A * (1 / v_current)",
    )

    # Model 2: offset = B * TSP (monotonic-in-TSP test; simplest linear)
    def m2(t, B): return B * t
    popt, pcov = curve_fit(m2, tsp, obs, p0=[100.0], sigma=err, absolute_sigma=False)
    B2 = popt[0]
    sB2 = float(np.sqrt(pcov[0, 0]))
    pred2 = m2(tsp, B2)
    chi2_2 = weighted_chi2(obs, pred2, err)
    results["Model_2_ED_TSP_linear"] = dict(
        B=B2, B_err=sB2,
        chi2=chi2_2, dof=n - 1, reduced_chi2=chi2_2 / (n - 1),
        r2=r_squared(obs, pred2),
        BIC=bic(chi2_2, 1, n),
        formula="offset = B * TSP",
    )

    # Model 3 (A1.0b): offset = min(D_T / v_current, v_current * TSP)  (zero free params)
    # Apocenter / equilibration-time cap applied.
    pred3 = ed_prediction_capped(vc, tsp)
    chi2_3 = weighted_chi2(obs, pred3, err)
    n_capped = int(np.sum(
        (vc * tsp * Gyr / kpc) < ed_prediction_D_T_over_v(vc)
    ))
    results["Model_3_ED_capped"] = dict(
        D_T=D_T, D_T_unit="m^2/s",
        n_points_capped=n_capped,
        chi2=chi2_3, dof=n, reduced_chi2=chi2_3 / n,
        r2=r_squared(obs, pred3),
        BIC=bic(chi2_3, 0, n),
        formula="offset = min(D_T/v_current, v_current*TSP)  (D_T fixed, cap applied)",
    )

    # Diagnostic: uncapped Model 3 (for comparison with A1.0 baseline)
    pred3_uncap = ed_prediction_D_T_over_v(vc)
    chi2_3u = weighted_chi2(obs, pred3_uncap, err)
    results["Model_3_ED_uncapped_diag"] = dict(
        D_T=D_T, D_T_unit="m^2/s",
        chi2=chi2_3u, dof=n, reduced_chi2=chi2_3u / n,
        r2=r_squared(obs, pred3_uncap),
        BIC=bic(chi2_3u, 0, n),
        formula="offset = D_T / v_current  (diagnostic, uncapped -- A1.0 baseline)",
    )

    # Model 4: offset = D * v_current^n  (log-log fit, n unconstrained)
    #   Fit log(offset) = log(D) + n * log(v_current) weighted by err/obs
    log_v = np.log(vc)
    log_o = np.log(np.clip(obs, 1e-3, None))
    log_err = err / np.clip(obs, 1e-3, None)
    coef, cov = np.polyfit(log_v, log_o, 1, w=1.0 / log_err, cov=True)
    n4 = float(coef[0])
    sn4 = float(np.sqrt(cov[0, 0]))
    D4 = float(np.exp(coef[1]))
    sD4 = float(D4 * np.sqrt(cov[1, 1]))
    pred4 = D4 * vc ** n4
    chi2_4 = weighted_chi2(obs, pred4, err)
    results["Model_4_SIDM_power"] = dict(
        D=D4, D_err=sD4, n=n4, n_err=sn4,
        n_positive=bool(n4 > 0),
        chi2=chi2_4, dof=n - 2, reduced_chi2=chi2_4 / max(n - 2, 1),
        r2=r_squared(obs, pred4),
        BIC=bic(chi2_4, 2, n),
        formula="offset = D * v_current^n  (SIDM-like if n > 0)",
    )

    # Model 5: flat baseline
    def m5(v, C): return C * np.ones_like(v)
    popt, pcov = curve_fit(m5, vc, obs, p0=[80.0], sigma=err, absolute_sigma=False)
    C5 = popt[0]
    sC5 = float(np.sqrt(pcov[0, 0]))
    pred5 = m5(vc, C5)
    chi2_5 = weighted_chi2(obs, pred5, err)
    results["Model_5_flat"] = dict(
        C=C5, C_err=sC5,
        chi2=chi2_5, dof=n - 1, reduced_chi2=chi2_5 / (n - 1),
        r2=r_squared(obs, pred5),
        BIC=bic(chi2_5, 1, n),
        formula="offset = constant",
    )

    # LCDM reference
    pred_lcdm = np.full_like(obs, LCDM_BASELINE_KPC)
    chi2_lcdm = weighted_chi2(obs, pred_lcdm, err)
    results["LCDM_baseline"] = dict(
        offset_kpc=LCDM_BASELINE_KPC,
        chi2=chi2_lcdm, dof=n, reduced_chi2=chi2_lcdm / n,
        r2=r_squared(obs, pred_lcdm),
        BIC=bic(chi2_lcdm, 0, n),
        formula=f"offset = {LCDM_BASELINE_KPC} kpc (Roche+2024 LCDM)",
    )

    # Predictions for plotting / residuals
    return results, dict(pred1=pred1, pred2=pred2, pred3=pred3,
                          pred3_uncap=pred3_uncap,
                          pred4=pred4, pred5=pred5, pred_lcdm=pred_lcdm)


# ---------------------------------------------------------------------------
# Step 3: plots
# ---------------------------------------------------------------------------
def plot_offset_vs_inv_vcurrent(df, fits):
    vc = df["v_current_kms"].values
    obs = df["offset_kpc"].values
    err = df["offset_err_kpc"].values
    inv_v = 1.0 / vc

    fig, ax = plt.subplots(figsize=(8.5, 5.5))
    ax.errorbar(inv_v, obs, yerr=err, fmt="o", color="C0",
                ecolor="gray", capsize=2, label="Finner 25 subclusters (BCG)")

    grid_vc = np.linspace(vc.min() * 0.9, vc.max() * 1.1, 200)
    grid_inv = 1.0 / grid_vc

    # Model 1 ED fit
    A1 = fits[0]["Model_1_ED_inv_v"]["A"]
    ax.plot(grid_inv, A1 * grid_inv, "-", color="C3", lw=2,
            label=f"Model 1  offset = {A1:.1f} / v_current")

    # Model 3 uncapped (A1.0 baseline, dashed)
    ax.plot(grid_inv, ed_prediction_D_T_over_v(grid_vc), "--", color="C2", lw=1.2,
            alpha=0.55,
            label="Model 3 uncapped  D_T / v_current  (A1.0 baseline)")

    # Model 3 CAPPED (A1.0b, solid): plot capped prediction at each data point
    # -- the cap depends on TSP, so a per-point scatter is more faithful than
    # a smooth curve over v alone.
    vc_arr = df["v_current_kms"].values
    tsp_arr = df["TSP_Gyr"].values
    pred3_capped = ed_prediction_capped(vc_arr, tsp_arr)
    ax.scatter(1.0 / vc_arr, pred3_capped, marker="x", s=55, color="C2",
               linewidth=2,
               label="Model 3 capped  min(D_T/v, v*TSP)  (A1.0b, per point)")

    # Model 5 flat
    C5 = fits[0]["Model_5_flat"]["C"]
    ax.axhline(C5, color="C4", lw=1.5, ls=":", label=f"Model 5  flat = {C5:.1f} kpc")

    # LCDM baseline
    ax.axhline(LCDM_BASELINE_KPC, color="k", lw=0.8, ls="-.",
               label=f"LCDM ~ {LCDM_BASELINE_KPC} kpc")

    ax.set_xlabel("1 / v_current  [s/km]")
    ax.set_ylabel("DM-BCG offset  [kpc]")
    ax.set_title("ED Test A1.0: Offset vs 1/v_current (N=25 Finner subclusters)")
    ax.legend(loc="upper left", fontsize=9, framealpha=0.92)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    out = PLOTS_DIR / "01_offset_vs_inv_vcurrent.png"
    plt.savefig(out, dpi=140)
    plt.close()
    return out


def plot_offset_vs_TSP(df, fits):
    tsp = df["TSP_Gyr"].values
    obs = df["offset_kpc"].values
    err = df["offset_err_kpc"].values

    fig, ax = plt.subplots(figsize=(8.5, 5.5))
    ax.errorbar(tsp, obs, yerr=err, fmt="o", color="C0",
                ecolor="gray", capsize=2, label="Finner 25 subclusters (BCG)")

    # Model 2: offset = B * TSP
    B2 = fits[0]["Model_2_ED_TSP_linear"]["B"]
    grid = np.linspace(0, max(tsp) * 1.1, 100)
    ax.plot(grid, B2 * grid, "-", color="C3", lw=2,
            label=f"Model 2  offset = {B2:.1f} * TSP [kpc/Gyr]")

    # Spearman correlation
    rho, pval = spearmanr(tsp, obs)
    ax.text(0.02, 0.95,
            f"Spearman rho = {rho:.2f}\np-value = {pval:.3f}\n"
            f"ED predicts rho > 0 (offset grows with TSP)",
            transform=ax.transAxes, fontsize=9, va="top",
            bbox=dict(facecolor="lightyellow", alpha=0.9))

    ax.set_xlabel("Time since pericenter  [Gyr]")
    ax.set_ylabel("DM-BCG offset  [kpc]")
    ax.set_title("ED Test A1.0: Offset vs TSP (N=25 Finner subclusters)")
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    out = PLOTS_DIR / "02_offset_vs_TSP.png"
    plt.savefig(out, dpi=140)
    plt.close()
    return out


def plot_residuals(df, fits):
    fits_dict, preds = fits
    obs = df["offset_kpc"].values
    err = df["offset_err_kpc"].values
    x = np.arange(len(obs))

    models = [
        ("Model 1 (ED 1/v fit)",       preds["pred1"], "C3"),
        ("Model 3 (ED capped)",        preds["pred3"], "C2"),
        ("Model 3 (ED uncapped, diag)", preds["pred3_uncap"], "C2"),
        ("Model 4 (SIDM v^n)",         preds["pred4"], "C1"),
        ("Model 5 (flat)",             preds["pred5"], "C4"),
        ("LCDM ~1 kpc",                preds["pred_lcdm"], "k"),
    ]

    fig, axes = plt.subplots(len(models), 1, figsize=(10, 1.8 * len(models)),
                             sharex=True)
    for ax, (name, pred, color) in zip(axes, models):
        res = obs - pred
        ax.errorbar(x, res, yerr=err, fmt="o", color=color, ecolor="gray",
                    capsize=2)
        ax.axhline(0, color="k", lw=0.5)
        chi2 = weighted_chi2(obs, pred, err)
        rchi2 = chi2 / max(len(obs) - 1, 1)
        ax.set_ylabel("residual [kpc]", fontsize=8)
        ax.set_title(f"{name}   chi2 = {chi2:.1f}   reduced = {rchi2:.2f}",
                     fontsize=9)
        ax.grid(alpha=0.3)
    axes[-1].set_xticks(x)
    axes[-1].set_xticklabels(
        [f"{c}_{s}" for c, s in zip(df["cluster"], df["subcluster_id"])],
        rotation=60, ha="right", fontsize=6,
    )
    plt.tight_layout()
    out = PLOTS_DIR / "03_residuals.png"
    plt.savefig(out, dpi=140)
    plt.close()
    return out


def plot_histogram(df):
    obs = df["offset_kpc"].values
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    ax.hist(obs, bins=np.linspace(0, 300, 13), edgecolor="black",
            color="C0", alpha=0.8)
    med = np.median(obs)
    mean = np.mean(obs)
    ax.axvline(med, color="C3", ls="--", lw=2, label=f"median = {med:.0f} kpc")
    ax.axvline(mean, color="C2", ls=":", lw=2, label=f"mean = {mean:.0f} kpc")
    ax.axvline(79, color="k", ls="-", lw=1,
               label="Finner+25 aggregate median = 79 kpc")
    ax.set_xlabel("DM-BCG offset  [kpc]")
    ax.set_ylabel("Number of subclusters")
    ax.set_title(f"Offset histogram (N={len(obs)})")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    out = PLOTS_DIR / "04_offset_histogram.png"
    plt.savefig(out, dpi=140)
    plt.close()
    return out


# ---------------------------------------------------------------------------
# Step 4: write results files
# ---------------------------------------------------------------------------
def write_fit_csv(fits_dict):
    rows = []
    for name, info in fits_dict.items():
        row = dict(model=name)
        for k, v in info.items():
            row[k] = v
        rows.append(row)
    df = pd.DataFrame(rows)
    out = RESULTS_DIR / "fit_coefficients.csv"
    df.to_csv(out, index=False)
    return out


def write_summary(df, fits_dict):
    obs = df["offset_kpc"].values
    tsp = df["TSP_Gyr"].values
    vc = df["v_current_kms"].values
    vp = df["v_peri_kms"].values
    n = len(obs)

    rho_tsp, p_tsp = spearmanr(tsp, obs)
    rho_invv, p_invv = spearmanr(1.0 / vc, obs)

    # Identify outliers: |residual| > 2 sigma vs the CAPPED Model 3
    pred3 = ed_prediction_capped(vc, tsp)
    pred3_uncap = ed_prediction_D_T_over_v(vc)
    err = df["offset_err_kpc"].values
    z = (obs - pred3) / err
    z_uncap = (obs - pred3_uncap) / err
    outlier_idx = np.where(np.abs(z) > 2.0)[0]
    outliers = df.iloc[outlier_idx].copy()
    outliers["pred_capped_kpc"] = pred3[outlier_idx]
    outliers["pred_uncapped_kpc"] = pred3_uncap[outlier_idx]
    outliers["resid_kpc"] = obs[outlier_idx] - pred3[outlier_idx]
    outliers["z_capped"] = z[outlier_idx]
    outliers["z_uncapped"] = z_uncap[outlier_idx]

    lines = []
    P = lines.append
    P("=" * 78)
    P("ED TEST A1.0 : Finner 25-subcluster BCG-offset analysis")
    P("=" * 78)
    P(f"N subclusters : {n}")
    P(f"tracer        : BCG (blue stars in Finner Fig 36)")
    P(f"offset median : {np.median(obs):.1f} kpc   (Finner aggregate: 79 +/- 14 kpc)")
    P(f"offset mean   : {np.mean(obs):.1f} kpc")
    P(f"v_peri range  : {vp.min():.0f} - {vp.max():.0f} km/s")
    P(f"v_current range: {vc.min():.0f} - {vc.max():.0f} km/s")
    P(f"TSP range     : {tsp.min():.2f} - {tsp.max():.2f} Gyr")
    P("")

    P("-" * 78)
    P("Fit results")
    P("-" * 78)
    for name, info in fits_dict.items():
        P(f"[{name}]")
        P(f"  formula : {info['formula']}")
        for k, v in info.items():
            if k in ("formula", "D_T_unit"):
                continue
            if isinstance(v, float):
                P(f"  {k:<16} = {v: .4g}")
            else:
                P(f"  {k:<16} = {v}")
        P("")

    P("-" * 78)
    P("Monotonicity & correlation tests")
    P("-" * 78)
    P(f"Spearman (offset vs TSP)       : rho = {rho_tsp: .3f}   p = {p_tsp:.3f}")
    P(f"Spearman (offset vs 1/v_current): rho = {rho_invv: .3f}   p = {p_invv:.3f}")
    P("ED predicts both rho > 0 at significance p < 0.05 if the trend is real.")
    P("")

    P("-" * 78)
    P("Model comparison summary")
    P("-" * 78)
    P(f"{'Model':<32} {'chi2':>10} {'dof':>5} {'red_chi2':>10} {'R^2':>8} {'BIC':>10}")
    for name, info in fits_dict.items():
        P(f"{name:<32} {info['chi2']:>10.2f} {info['dof']:>5.0f} "
          f"{info['reduced_chi2']:>10.3f} {info['r2']:>8.3f} {info['BIC']:>10.2f}")
    P("")
    P("Preferred model: lowest BIC.")
    P("")

    P("-" * 78)
    P("Outliers vs Model 3 CAPPED  (|z_capped| > 2)")
    P("-" * 78)
    if len(outliers) == 0:
        P("None -- cap brings every subcluster within 2 sigma of the ED prediction.")
    else:
        P(f"{'subcluster':<16} {'obs':>8} {'pred_cap':>10} {'pred_uncap':>12} "
          f"{'z_cap':>8} {'z_uncap':>9}")
        for _, row in outliers.iterrows():
            name = f"{row['cluster']}_{row['subcluster_id']}"
            P(f"{name:<16} "
              f"{row['offset_kpc']:>8.0f} {row['pred_capped_kpc']:>10.0f} "
              f"{row['pred_uncapped_kpc']:>12.0f} "
              f"{row['z_capped']:>+8.2f} {row['z_uncapped']:>+9.2f}")
    P("")

    P("=" * 78)
    P("End of A1.0 summary. Interpretation deferred.")
    P("=" * 78)

    text = "\n".join(lines)
    out = RESULTS_DIR / "summary.txt"
    out.write_text(text, encoding="utf-8")
    print(text)
    return out


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    if not OFFSETS_CSV.exists():
        sys.exit(f"Missing input: {OFFSETS_CSV}")

    print(f"Repo root   : {REPO_ROOT}")
    print(f"Data dir    : {DATA_DIR}")
    print(f"Offsets CSV : {OFFSETS_CSV}")
    print()

    df = build_merged_table()
    print(f"Merged table written: {MERGED_CSV}   (n = {len(df)})")
    print()

    fits = fit_models(df)
    fits_dict, _ = fits

    p1 = plot_offset_vs_inv_vcurrent(df, fits)
    p2 = plot_offset_vs_TSP(df, fits)
    p3 = plot_residuals(df, fits)
    p4 = plot_histogram(df)
    print("Plots written:")
    for p in (p1, p2, p3, p4):
        print(f"  {p}")
    print()

    fit_csv = write_fit_csv(fits_dict)
    summary = write_summary(df, fits_dict)
    print()
    print(f"Fit table : {fit_csv}")
    print(f"Summary   : {summary}")


if __name__ == "__main__":
    main()
