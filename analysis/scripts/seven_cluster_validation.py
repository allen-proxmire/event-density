"""
ED Test A1.0b VALIDATION
========================
Runs the same pipeline (Models 1-5 + LCDM + capped ED) on the 7-cluster
high-precision sample from papers/Cluster_Merger_Lag_Evidence/paper.md,
Table 1 (Section 3.10).

Purpose
-------
Confirm that the current analysis machinery reproduces the published
velocity-scaling result:

    4-cluster fit (Bullet, El Gordo, MACS J0025, Musket Ball)
        n = -1.07 +/- 0.20   (log(l) vs log(v_current))

If the pipeline recovers n within uncertainty, the pipeline is validated
and the A1.0b "flat wins on Finner" result is a statement about the
Finner sample, not about the framework.

Inputs  : data/ED-Finner/seven_cluster_validation.csv
Outputs :
    data/ED-Finner/plots/seven_cluster_validation_01_offset_vs_inv_v.png
    data/ED-Finner/plots/seven_cluster_validation_02_residuals.png
    data/ED-Finner/results/seven_cluster_validation_summary.txt

Usage
-----
    python analysis/scripts/seven_cluster_validation.py
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import spearmanr

# Reuse constants / prediction helpers from the Finner pipeline
from finner_a1_analysis import (
    D_T, kpc, Gyr, LCDM_BASELINE_KPC,
    ed_prediction_D_T_over_v, ed_prediction_capped,
    weighted_chi2, r_squared, bic,
    DATA_DIR, PLOTS_DIR, RESULTS_DIR,
)

INPUT_CSV = DATA_DIR / "seven_cluster_validation.csv"
SUMMARY_TXT = RESULTS_DIR / "seven_cluster_validation_summary.txt"
PLOT1 = PLOTS_DIR / "seven_cluster_validation_01_offset_vs_inv_v.png"
PLOT2 = PLOTS_DIR / "seven_cluster_validation_02_residuals.png"

# High-precision 4-cluster subset used by the merger-lag paper for the
# headline n = -1.07 +/- 0.20 velocity-scaling fit.
HP4 = ["Bullet", "ElGordo", "MACSJ0025", "MusketBall"]

PUBLISHED_N = -1.07
PUBLISHED_N_ERR = 0.20


# ---------------------------------------------------------------------------
# Fit routines (mirroring finner_a1_analysis.fit_models but streamlined)
# ---------------------------------------------------------------------------
def run_all_models(df: pd.DataFrame) -> dict:
    obs = df["offset_kpc"].values.astype(float)
    err = df["offset_err_kpc"].values.astype(float)
    vc = df["v_current_kms"].values.astype(float)
    tsp = df["TSP_Gyr"].values.astype(float)
    n = len(obs)
    out = {}

    # Model 1: offset = A / v_current
    def m1(v, A): return A / v
    try:
        popt, pcov = curve_fit(m1, vc, obs, p0=[1e5], sigma=err,
                               absolute_sigma=False)
        A1 = popt[0]; sA1 = float(np.sqrt(pcov[0, 0]))
    except Exception:
        A1 = float("nan"); sA1 = float("nan")
    pred1 = m1(vc, A1) if np.isfinite(A1) else np.full_like(obs, np.nan)
    c1 = weighted_chi2(obs, pred1, err)
    out["Model_1_ED_A_over_v"] = dict(
        A=A1, A_err=sA1, chi2=c1, dof=n - 1,
        reduced_chi2=c1 / max(n - 1, 1), r2=r_squared(obs, pred1),
        BIC=bic(c1, 1, n),
        formula="offset = A / v_current",
    )

    # Model 2: offset = B * TSP
    def m2(t, B): return B * t
    popt, pcov = curve_fit(m2, tsp, obs, p0=[100.0], sigma=err,
                           absolute_sigma=False)
    B2 = popt[0]; sB2 = float(np.sqrt(pcov[0, 0]))
    pred2 = m2(tsp, B2)
    c2 = weighted_chi2(obs, pred2, err)
    out["Model_2_ED_TSP_linear"] = dict(
        B=B2, B_err=sB2, chi2=c2, dof=n - 1,
        reduced_chi2=c2 / max(n - 1, 1), r2=r_squared(obs, pred2),
        BIC=bic(c2, 1, n),
        formula="offset = B * TSP",
    )

    # Model 3: zero-parameter capped ED
    pred3 = ed_prediction_capped(vc, tsp)
    c3 = weighted_chi2(obs, pred3, err)
    out["Model_3_ED_capped"] = dict(
        D_T=D_T, chi2=c3, dof=n,
        reduced_chi2=c3 / n, r2=r_squared(obs, pred3),
        BIC=bic(c3, 0, n),
        formula="offset = min(D_T/v_current, v_current*TSP)",
    )

    # Diagnostic: uncapped Model 3
    pred3u = ed_prediction_D_T_over_v(vc)
    c3u = weighted_chi2(obs, pred3u, err)
    out["Model_3_ED_uncapped_diag"] = dict(
        D_T=D_T, chi2=c3u, dof=n,
        reduced_chi2=c3u / n, r2=r_squared(obs, pred3u),
        BIC=bic(c3u, 0, n),
        formula="offset = D_T / v_current (uncapped)",
    )

    # Model 4: SIDM-like power law (log-log, unconstrained n)
    log_v = np.log(vc)
    log_o = np.log(np.clip(obs, 1e-3, None))
    log_err = err / np.clip(obs, 1e-3, None)
    if n >= 3:
        coef, cov = np.polyfit(log_v, log_o, 1, w=1.0 / log_err, cov=True)
        n4 = float(coef[0]); sn4 = float(np.sqrt(cov[0, 0]))
        D4 = float(np.exp(coef[1])); sD4 = float(D4 * np.sqrt(cov[1, 1]))
    else:
        # Underdetermined; skip
        n4 = float("nan"); sn4 = float("nan"); D4 = float("nan"); sD4 = float("nan")
    pred4 = D4 * vc ** n4 if np.isfinite(n4) else np.full_like(obs, np.nan)
    c4 = weighted_chi2(obs, pred4, err) if np.isfinite(n4) else float("nan")
    out["Model_4_power_law"] = dict(
        D=D4, D_err=sD4, n=n4, n_err=sn4,
        chi2=c4, dof=max(n - 2, 1),
        reduced_chi2=c4 / max(n - 2, 1) if np.isfinite(c4) else float("nan"),
        r2=r_squared(obs, pred4) if np.isfinite(n4) else float("nan"),
        BIC=bic(c4, 2, n) if np.isfinite(c4) else float("nan"),
        formula="offset = D * v_current^n  (log-log weighted fit)",
    )

    # Model 5: flat baseline
    def m5(v, C): return C * np.ones_like(v)
    popt, pcov = curve_fit(m5, vc, obs, p0=[50.0], sigma=err,
                           absolute_sigma=False)
    C5 = popt[0]; sC5 = float(np.sqrt(pcov[0, 0]))
    pred5 = m5(vc, C5)
    c5 = weighted_chi2(obs, pred5, err)
    out["Model_5_flat"] = dict(
        C=C5, C_err=sC5, chi2=c5, dof=n - 1,
        reduced_chi2=c5 / max(n - 1, 1), r2=r_squared(obs, pred5),
        BIC=bic(c5, 1, n),
        formula="offset = constant",
    )

    # LCDM baseline
    pred_lcdm = np.full_like(obs, LCDM_BASELINE_KPC)
    clcdm = weighted_chi2(obs, pred_lcdm, err)
    out["LCDM_baseline"] = dict(
        offset_kpc=LCDM_BASELINE_KPC, chi2=clcdm, dof=n,
        reduced_chi2=clcdm / n, r2=r_squared(obs, pred_lcdm),
        BIC=bic(clcdm, 0, n),
        formula=f"offset = {LCDM_BASELINE_KPC} kpc",
    )

    preds = dict(pred1=pred1, pred2=pred2, pred3=pred3,
                 pred3_uncap=pred3u, pred4=pred4, pred5=pred5,
                 pred_lcdm=pred_lcdm)
    return out, preds


# ---------------------------------------------------------------------------
# Plots
# ---------------------------------------------------------------------------
def plot_offset_vs_inv_v(df7, df4, fit7, fit4):
    fig, ax = plt.subplots(figsize=(9, 5.5))

    # Full 7-cluster sample, highlighting HP4 vs others
    hp_mask = df7["cluster"].isin(HP4).values
    vc_all = df7["v_current_kms"].values
    obs_all = df7["offset_kpc"].values
    err_all = df7["offset_err_kpc"].values

    ax.errorbar(1.0 / vc_all[hp_mask], obs_all[hp_mask],
                yerr=err_all[hp_mask], fmt="o", color="C0",
                ecolor="gray", capsize=2, ms=8,
                label="High-precision 4 (fit sample)")
    ax.errorbar(1.0 / vc_all[~hp_mask], obs_all[~hp_mask],
                yerr=err_all[~hp_mask], fmt="s", color="C3",
                ecolor="gray", capsize=2, ms=8, markerfacecolor="white",
                label="Other 3 (MACS J1149 SL / ZwCl 0008 / CIZA J2242)")

    # Label each point
    for _, row in df7.iterrows():
        ax.annotate(
            f"{row['cluster']} {row['subcluster_id']}",
            xy=(1.0 / row["v_current_kms"], row["offset_kpc"]),
            xytext=(4, 4), textcoords="offset points",
            fontsize=7, color="k", alpha=0.8,
        )

    # ED zero-parameter predictions across a v_current grid
    vc_grid = np.logspace(np.log10(50), np.log10(5000), 200)
    ax.plot(1.0 / vc_grid, ed_prediction_D_T_over_v(vc_grid), "--",
            color="C2", lw=1.2, alpha=0.55,
            label="ED uncapped  D_T / v_current")

    # Fitted power-law from HP4 Model 4 (this is the key validation curve)
    n4 = fit4["Model_4_power_law"]["n"]
    D4 = fit4["Model_4_power_law"]["D"]
    sn4 = fit4["Model_4_power_law"]["n_err"]
    ax.plot(1.0 / vc_grid, D4 * vc_grid ** n4, "-", color="C3", lw=2.0,
            label=f"HP4 power-law fit  n = {n4:.2f} +/- {sn4:.2f}")

    # Published reference: n = -1.07 +/- 0.20, anchor at Bullet
    b_row = df7[df7["cluster"] == "Bullet"].iloc[0]
    anchor_v = b_row["v_current_kms"]
    anchor_o = b_row["offset_kpc"]
    D_pub = anchor_o / anchor_v ** PUBLISHED_N
    ax.plot(1.0 / vc_grid, D_pub * vc_grid ** PUBLISHED_N, ":", color="k",
            lw=1.2, alpha=0.8,
            label=f"Published n = {PUBLISHED_N:.2f} (anchored at Bullet)")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("1 / v_current  [s/km]")
    ax.set_ylabel("Offset  [kpc]")
    ax.set_title("A1.0b Validation: 7-cluster sample, offset vs 1/v_current "
                 "(log-log)")
    ax.legend(loc="upper left", fontsize=8, framealpha=0.92)
    ax.grid(alpha=0.3, which="both")
    plt.tight_layout()
    plt.savefig(PLOT1, dpi=140)
    plt.close()


def plot_residuals(df7, preds7):
    obs = df7["offset_kpc"].values
    err = df7["offset_err_kpc"].values
    labels = [f"{c}_{s}" for c, s in
              zip(df7["cluster"], df7["subcluster_id"])]
    x = np.arange(len(obs))

    models = [
        ("Model 1  A/v fit",        preds7["pred1"],       "C3"),
        ("Model 3  ED capped",      preds7["pred3"],       "C2"),
        ("Model 3  ED uncapped",    preds7["pred3_uncap"], "C2"),
        ("Model 4  power-law fit",  preds7["pred4"],       "C1"),
        ("Model 5  flat",           preds7["pred5"],       "C4"),
        ("LCDM ~1 kpc",             preds7["pred_lcdm"],   "k"),
    ]

    fig, axes = plt.subplots(len(models), 1, figsize=(9.5, 1.7 * len(models)),
                             sharex=True)
    for ax, (name, pred, color) in zip(axes, models):
        res = obs - pred
        ax.errorbar(x, res, yerr=err, fmt="o", color=color, ecolor="gray",
                    capsize=2)
        ax.axhline(0, color="k", lw=0.5)
        c = weighted_chi2(obs, pred, err)
        ax.set_ylabel("residual [kpc]", fontsize=8)
        ax.set_title(f"{name}   chi2 = {c:.1f}   reduced = {c / max(len(obs)-1,1):.2f}",
                     fontsize=9)
        ax.grid(alpha=0.3)
    axes[-1].set_xticks(x)
    axes[-1].set_xticklabels(labels, rotation=40, ha="right", fontsize=8)
    plt.tight_layout()
    plt.savefig(PLOT2, dpi=140)
    plt.close()


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
def write_summary(df7, df4, fit7, fit4):
    n7 = fit7["Model_4_power_law"]["n"]
    sn7 = fit7["Model_4_power_law"]["n_err"]
    n4 = fit4["Model_4_power_law"]["n"]
    sn4 = fit4["Model_4_power_law"]["n_err"]

    vc7 = df7["v_current_kms"].values
    o7 = df7["offset_kpc"].values
    vc4 = df4["v_current_kms"].values
    o4 = df4["offset_kpc"].values
    tsp7 = df7["TSP_Gyr"].values

    rho7_v, p7_v = spearmanr(1.0 / vc7, o7)
    rho4_v, p4_v = spearmanr(1.0 / vc4, o4)
    rho7_t, p7_t = spearmanr(tsp7, o7)

    n_pub = PUBLISHED_N
    sn_pub = PUBLISHED_N_ERR
    diff = n4 - n_pub
    sigma = np.hypot(sn4, sn_pub)
    consistent = abs(diff) < 2.0 * sigma

    lines = []
    P = lines.append
    P("=" * 78)
    P("PIPELINE VALIDATION: ED-Finner A1.0b machinery on 7-cluster sample")
    P("=" * 78)
    P(f"Input          : {INPUT_CSV}")
    P(f"N (full)       : {len(df7)}")
    P(f"N (HP4 subset) : {len(df4)}  [{', '.join(HP4)}]")
    P("")
    P(f"Published headline fit (merger-lag paper Section 4.1):")
    P(f"    n = {n_pub:+.2f} +/- {sn_pub:.2f}   (log(l) vs log(v_current), HP4)")
    P("")

    P("-" * 78)
    P("Pipeline recovered power-law slope (Model 4, log-log weighted fit)")
    P("-" * 78)
    P(f"  HP4 (N=4)      : n = {n4:+.3f} +/- {sn4:.3f}")
    P(f"  Full 7 (N=7)   : n = {n7:+.3f} +/- {sn7:.3f}")
    P(f"  Published ref  : n = {n_pub:+.3f} +/- {sn_pub:.3f}")
    P("")
    P(f"  Delta(HP4 - published)       = {diff:+.3f}")
    P(f"  Joint sigma (quadrature)     = {sigma:.3f}")
    P(f"  Delta / sigma                = {diff / sigma:+.2f}")
    P(f"  Consistent within 2 sigma?   = {consistent}")
    P("")

    P("-" * 78)
    P("Spearman rank correlations")
    P("-" * 78)
    P(f"  Full 7: rho(offset, 1/v_current) = {rho7_v:+.3f}   p = {p7_v:.3f}")
    P(f"  HP4 : rho(offset, 1/v_current)   = {rho4_v:+.3f}   p = {p4_v:.3f}")
    P(f"  Full 7: rho(offset, TSP)         = {rho7_t:+.3f}   p = {p7_t:.3f}")
    P("")

    for label, fit, df in [("HP4", fit4, df4), ("Full 7", fit7, df7)]:
        P("-" * 78)
        P(f"Model comparison ({label}, N={len(df)})")
        P("-" * 78)
        P(f"{'Model':<32} {'chi2':>10} {'dof':>5} {'red_chi2':>10} {'BIC':>10}")
        for name, info in fit.items():
            if isinstance(info.get("chi2"), float) and np.isfinite(info["chi2"]):
                P(f"{name:<32} {info['chi2']:>10.2f} {info['dof']:>5.0f} "
                  f"{info['reduced_chi2']:>10.3f} {info['BIC']:>10.2f}")
            else:
                P(f"{name:<32} --")
        P("")

    # Per-system comparison
    P("-" * 78)
    P("Per-system: observed vs ED capped")
    P("-" * 78)
    P(f"{'system':<20} {'v_curr':>7} {'TSP':>5} {'obs':>8} {'pred_cap':>10} "
      f"{'pred_uncap':>12} {'z_cap':>8}")
    vc = df7["v_current_kms"].values
    ts = df7["TSP_Gyr"].values
    pc = ed_prediction_capped(vc, ts)
    pu = ed_prediction_D_T_over_v(vc)
    for i, row in df7.iterrows():
        z = (row["offset_kpc"] - pc[i]) / row["offset_err_kpc"]
        sys = f"{row['cluster']} {row['subcluster_id']}"
        P(f"{sys:<20} {row['v_current_kms']:>7.0f} {row['TSP_Gyr']:>5.2f} "
          f"{row['offset_kpc']:>8.1f} {pc[i]:>10.1f} {pu[i]:>12.1f} "
          f"{z:>+8.2f}")
    P("")

    P("=" * 78)
    verdict = "PIPELINE VALIDATED" if consistent else "PIPELINE DISCREPANCY"
    P(f"VERDICT: {verdict}")
    if consistent:
        P("The pipeline recovers the published n within 2 sigma on the HP4")
        P("sample. The A1.0b 'flat wins on Finner' result is therefore a")
        P("statement about the Finner sample's resolution limit and the")
        P("regime-mixing effect of the cap, not a framework failure.")
    else:
        P("The recovered slope on HP4 differs from the published value by")
        P(">2 sigma. Investigate input numbers (v_current, TSP, offset)")
        P("and weighting conventions before trusting the A1.0b output.")
    P("=" * 78)

    text = "\n".join(lines)
    SUMMARY_TXT.write_text(text, encoding="utf-8")
    print(text)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    df7 = pd.read_csv(INPUT_CSV)
    df4 = df7[df7["cluster"].isin(HP4)].copy().reset_index(drop=True)

    fit7, preds7 = run_all_models(df7)
    fit4, preds4 = run_all_models(df4)

    plot_offset_vs_inv_v(df7, df4, fit7, fit4)
    plot_residuals(df7, preds7)
    write_summary(df7, df4, fit7, fit4)

    print()
    print(f"Plots  : {PLOT1}")
    print(f"         {PLOT2}")
    print(f"Summary: {SUMMARY_TXT}")


if __name__ == "__main__":
    main()
