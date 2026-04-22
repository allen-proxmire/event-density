"""
ED-BTFR-Activity Union Test
===========================

Pre-BIG-SPARC combined test of the ED-unique activity-dependence prediction:
at fixed baryonic mass, galaxies with higher star-formation activity should
lie above the baryonic Tully-Fisher relation (BTFR), because the ED
participation field v(t) is out of equilibrium for galaxies with recent
activity.  MOND and LCDM do not predict this correlation.

This script combines the five usable SFR-cross-match modules
(ED-Data-12, 13, 14, 16, 17) -- none of which are fully independent,
all applied to mostly-overlapping subsets of SPARC -- into a single
union-sample analysis with one consistent BTFR fit and one consistent
SFR value per galaxy.

SFR precedence (highest fidelity first):
    1. z0MGS uniform UV+IR  (ED-Data-17 full sample preferred, fallback to 16)
    2. Calibrated sSFR (Salim/Schombert via T-type)  (ED-Data-13)
    3. Literature / mixed photometric SFR  (ED-Data-14)
    4. T-type only  (ED-Data-12 -- fallback only, excluded from primary)

Primary analysis: Q = 1 SPARC galaxies with any of the top three proxies.
Full SPARC (Q != 1 included) is run as a robustness check.

Outputs
-------
    data/ED-BTFR-Activity/union_table.csv
    data/ED-BTFR-Activity/results/main_results.json
    data/ED-BTFR-Activity/results/robustness.csv
    data/ED-BTFR-Activity/plots/*.png

This is a repo-ready pre-BIG-SPARC analysis, not a full standalone paper.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import spearmanr, kendalltau, mannwhitneyu, theilslopes


# ---------------------------------------------------------------------------
# Constants & paths
# ---------------------------------------------------------------------------
RNG = np.random.default_rng(20260417)
N_BOOT = 10_000
N_PERM = 10_000

REPO_ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = REPO_ROOT / "data" / "ED-BTFR-Activity"
PLOTS = OUT_DIR / "plots"
RESULTS = OUT_DIR / "results"
for d in (PLOTS, RESULTS):
    d.mkdir(parents=True, exist_ok=True)

UNION_CSV = OUT_DIR / "union_table.csv"
MAIN_JSON = RESULTS / "main_results.json"
ROBUST_CSV = RESULTS / "robustness.csv"

MODULE_PATHS = {
    "12": REPO_ROOT / "data/ED-Data-12-Galactic-Activity/results/crossmatched_table.csv",
    "13": REPO_ROOT / "data/ED-Data-13-Real-SFR/results/crossmatched_real_sfr.csv",
    "14": REPO_ROOT / "data/ED-Data-14-Photometric-SFR/results/crossmatched_photometric_sfr.csv",
    "16": REPO_ROOT / "data/ED-Data-16-z0MGS/results/crossmatched_z0mgs.csv",
    "17": REPO_ROOT / "data/ED-Data-17-z0MGS-Names/results/crossmatched_z0mgs_full.csv",
}


# ---------------------------------------------------------------------------
# Load & harmonize
# ---------------------------------------------------------------------------
def load_modules() -> pd.DataFrame:
    """Merge the five modules on Galaxy, keeping the raw SFR columns tagged."""
    m12 = pd.read_csv(MODULE_PATHS["12"]).rename(
        columns={"T_type": "T", "log_Mb": "logMb", "Quality": "Q"}
    )[["Galaxy", "T", "logMb", "Vflat", "Q"]]

    m13 = pd.read_csv(MODULE_PATHS["13"])[["Galaxy", "logSFR", "logsSFR"]].rename(
        columns={"logSFR": "logSFR_calibrated",
                 "logsSFR": "logsSFR_calibrated"}
    )

    m14 = pd.read_csv(MODULE_PATHS["14"])[["Galaxy", "logSFR", "logsSFR"]].rename(
        columns={"logSFR": "logSFR_literature",
                 "logsSFR": "logsSFR_literature"}
    )

    m16 = pd.read_csv(MODULE_PATHS["16"])[["Galaxy", "logSFR_z0MGS", "logsSFR"]].rename(
        columns={"logSFR_z0MGS": "logSFR_z0MGS_16",
                 "logsSFR": "logsSFR_z0MGS_16"}
    )

    m17 = pd.read_csv(MODULE_PATHS["17"])[["Galaxy", "logSFR", "logsSFR"]].rename(
        columns={"logSFR": "logSFR_z0MGS_17",
                 "logsSFR": "logsSFR_z0MGS_17"}
    )

    # Module 12 is the baseline (all 122 SPARC galaxies with T-type + Vflat).
    union = m12
    for m in (m13, m14, m16, m17):
        union = union.merge(m, on="Galaxy", how="left")

    return union


def assign_proxy(row) -> tuple[float, str]:
    """Apply the user-specified precedence ladder."""
    # z0MGS: prefer expanded (17) over original (16) when both present
    if pd.notna(row.get("logSFR_z0MGS_17")):
        return float(row["logSFR_z0MGS_17"]), "z0MGS"
    if pd.notna(row.get("logSFR_z0MGS_16")):
        return float(row["logSFR_z0MGS_16"]), "z0MGS"
    if pd.notna(row.get("logSFR_calibrated")):
        return float(row["logSFR_calibrated"]), "calibrated"
    if pd.notna(row.get("logSFR_literature")):
        return float(row["logSFR_literature"]), "literature"
    return np.nan, "T-type-only"


# ---------------------------------------------------------------------------
# BTFR fit and residual computation
# ---------------------------------------------------------------------------
def fit_btfr_and_residuals(df: pd.DataFrame,
                            convention: str = "V_on_M"
                            ) -> tuple[pd.DataFrame, dict]:
    """
    Theil-Sen BTFR fit + residuals in log V.

    convention:
      "V_on_M" -- fit log V = a + b * log M (clean test of V at fixed M;
                   residuals have NO mass trend by construction).
                   This is the right convention for the ED-activity test
                   because ED predicts V at fixed M.
      "M_on_V" -- fit log M = a + b * log V (the convention used by
                   ED-Data-12..17 modules -- slope 3.72 reported there).
                   Residuals are inverted to log V space.  This leaves
                   a small mass trend in Delta because of regression
                   dilution in the V direction.  Included for backward
                   reproduction only.
    """
    x = df["logMb"].values
    y = np.log10(df["Vflat"].values)

    if convention == "V_on_M":
        slope, intercept, slope_lo, slope_hi = theilslopes(y, x, 0.95)
        delta = y - (intercept + slope * x)
        # Effective slope in V-space = slope
        v_slope = float(slope)
        v_intercept = float(intercept)
    elif convention == "M_on_V":
        # Fit log M on log V, Delta in M-space (module 13 convention).
        # log M = intercept_MV + slope_MV * log V, slope ~ 3.72 for BTFR.
        slope_MV, intercept_MV, lo_MV, hi_MV = theilslopes(x, y, 0.95)
        delta = x - (intercept_MV + slope_MV * y)  # log M residual
        # For reporting, also record the inverted V-space slope
        v_slope = 1.0 / float(slope_MV)
        v_intercept = -float(intercept_MV) / float(slope_MV)
        slope_lo = 1.0 / float(hi_MV)
        slope_hi = 1.0 / float(lo_MV)
    else:
        raise ValueError(f"Unknown convention: {convention}")

    out = df.copy()
    out["logVflat"] = y
    out["Delta"] = delta

    fit_info = {
        "convention": convention,
        "slope_V_on_M_equiv": v_slope,
        "intercept_V_on_M_equiv": v_intercept,
        "slope_95_lo": float(slope_lo),
        "slope_95_hi": float(slope_hi),
        "n": int(len(df)),
        "ED_slope_fixed": 0.25,
        "LCDM_virial_slope_fixed": 1.0 / 3,
    }
    return out, fit_info


# ---------------------------------------------------------------------------
# Statistical tests
# ---------------------------------------------------------------------------
def spearman_with_bootstrap(x, y, n_boot=N_BOOT, rng=RNG):
    rho, p_two = spearmanr(x, y)
    # Bootstrap resample (paired)
    n = len(x)
    rhos = np.empty(n_boot)
    for i in range(n_boot):
        idx = rng.integers(0, n, size=n)
        rhos[i] = spearmanr(x[idx], y[idx]).statistic
    ci_lo, ci_hi = np.percentile(rhos, [2.5, 97.5])
    return dict(
        rho=float(rho),
        p_two_tailed=float(p_two),
        p_one_tailed=float(p_two / 2 if rho > 0 else 1 - p_two / 2),
        ci_95=(float(ci_lo), float(ci_hi)),
        bootstrap_rhos=rhos,
    )


def permutation_p(x, y, n_perm=N_PERM, rng=RNG):
    """One-tailed permutation p-value for ED (expect rho > 0)."""
    rho_obs, _ = spearmanr(x, y)
    y_perm = y.copy()
    count = 0
    for _ in range(n_perm):
        rng.shuffle(y_perm)
        if spearmanr(x, y_perm).statistic >= rho_obs:
            count += 1
    return float((count + 1) / (n_perm + 1))  # add-one estimator


def tertile_test(df, x_col="logSFR", y_col="Delta"):
    """Split into thirds by x, Mann-Whitney one-tailed high vs. low."""
    n = len(df)
    sorted_df = df.sort_values(x_col).reset_index(drop=True)
    t1 = n // 3
    t2 = 2 * n // 3
    low = sorted_df[y_col].iloc[:t1].values
    high = sorted_df[y_col].iloc[t2:].values
    mid = sorted_df[y_col].iloc[t1:t2].values
    stat, p = mannwhitneyu(high, low, alternative="greater")
    return dict(
        n_low=int(len(low)), n_mid=int(len(mid)), n_high=int(len(high)),
        mean_low=float(np.mean(low)),
        mean_mid=float(np.mean(mid)),
        mean_high=float(np.mean(high)),
        mw_U=float(stat),
        mw_p_one_tailed=float(p),
    )


def partial_spearman_rho_control_mass(df,
                                       x_col="logSFR", y_col="Delta",
                                       z_col="logMb"):
    """
    Partial Spearman correlation rho(x, y | z): regress ranks of x on ranks
    of z and similarly for y, then take Spearman on the residuals.
    """
    from scipy.stats import rankdata

    rx = rankdata(df[x_col].values)
    ry = rankdata(df[y_col].values)
    rz = rankdata(df[z_col].values)

    def resid(a, b):
        X = np.vstack([np.ones_like(b), b]).T
        beta, *_ = np.linalg.lstsq(X, a, rcond=None)
        return a - X @ beta

    rx_res = resid(rx, rz)
    ry_res = resid(ry, rz)
    rho, p = spearmanr(rx_res, ry_res)
    return dict(
        partial_rho=float(rho),
        p_two_tailed=float(p),
        p_one_tailed=float(p / 2 if rho > 0 else 1 - p / 2),
    )


def kendall_summary(x, y):
    tau, p = kendalltau(x, y)
    return dict(tau=float(tau), p_two_tailed=float(p))


# ---------------------------------------------------------------------------
# Plots
# ---------------------------------------------------------------------------
PROXY_COLORS = {
    "z0MGS": "#1f77b4",
    "calibrated": "#ff7f0e",
    "literature": "#2ca02c",
    "T-type-only": "#777777",
}


def plot_btfr(fit_df, fit_info, out):
    fig, ax = plt.subplots(figsize=(8, 6))
    for tier, g in fit_df.groupby("proxy_tier"):
        ax.scatter(g["logMb"], g["logVflat"],
                   c=PROXY_COLORS.get(tier, "k"),
                   label=f"{tier} (n={len(g)})",
                   s=35, edgecolor="black", linewidth=0.4, alpha=0.85)
    x_fit = np.linspace(fit_df["logMb"].min() - 0.2,
                         fit_df["logMb"].max() + 0.2, 200)
    b = fit_info["slope_V_on_M_equiv"]
    a = fit_info["intercept_V_on_M_equiv"]
    ax.plot(x_fit, a + b * x_fit,
            "k-", lw=2,
            label=f"Theil-Sen {fit_info['convention']}  (slope={b:.3f})")
    ax.plot(x_fit, a + 0.25 * x_fit,
            "r--", lw=1.2, alpha=0.7,
            label="slope = 1/4 (ED / MOND reference)")
    ax.set_xlabel(r"$\log_{10}(M_b / M_\odot)$")
    ax.set_ylabel(r"$\log_{10}(V_{\rm flat} / \mathrm{km\,s^{-1}})$")
    ax.set_title("BTFR on union sample (Q = 1, best-available SFR proxy)")
    ax.legend(loc="lower right", fontsize=9)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(out, dpi=140)
    plt.close()


def plot_delta_vs_sfr(fit_df, rho_info, out):
    fig, ax = plt.subplots(figsize=(8, 6))
    for tier, g in fit_df.groupby("proxy_tier"):
        ax.scatter(g["logSFR"], g["Delta"],
                   c=PROXY_COLORS.get(tier, "k"),
                   label=f"{tier} (n={len(g)})",
                   s=35, edgecolor="black", linewidth=0.4, alpha=0.85)
    ax.axhline(0, color="k", lw=0.5)
    ax.text(0.02, 0.97,
            f"Spearman rho = {rho_info['rho']:+.3f}\n"
            f"95% CI = [{rho_info['ci_95'][0]:+.3f}, {rho_info['ci_95'][1]:+.3f}]\n"
            f"one-tailed p = {rho_info['p_one_tailed']:.4f}",
            transform=ax.transAxes, fontsize=10, va="top",
            bbox=dict(facecolor="lightyellow", alpha=0.9))
    ax.set_xlabel(r"$\log_{10}(\mathrm{SFR} / M_\odot\,\mathrm{yr}^{-1})$")
    ax.set_ylabel(r"BTFR residual  $\Delta = \log V_{\rm flat} - \mathrm{fit}$")
    ax.set_title("ED activity-dependence: residual vs. log SFR on the union sample")
    ax.legend(loc="lower right", fontsize=9)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(out, dpi=140)
    plt.close()


def plot_tertile_box(fit_df, tert_info, out):
    """Box plot of Delta in low / mid / high SFR tertiles."""
    x = fit_df.sort_values("logSFR")["Delta"].values
    n = len(x)
    t1, t2 = n // 3, 2 * n // 3
    groups = [x[:t1], x[t1:t2], x[t2:]]
    labels = [f"Low SFR\n(n={tert_info['n_low']})",
              f"Mid SFR\n(n={tert_info['n_mid']})",
              f"High SFR\n(n={tert_info['n_high']})"]
    fig, ax = plt.subplots(figsize=(7, 5))
    parts = ax.boxplot(groups, tick_labels=labels, patch_artist=True, widths=0.55)
    for patch, color in zip(parts["boxes"], ["#d62728", "#bcbd22", "#2ca02c"]):
        patch.set_facecolor(color)
        patch.set_alpha(0.6)
    ax.axhline(0, color="k", lw=0.5)
    for i, g in enumerate(groups):
        ax.scatter(np.full(len(g), i + 1) + RNG.uniform(-0.08, 0.08, len(g)),
                   g, color="black", s=15, alpha=0.6, zorder=3)
    ax.set_ylabel(r"BTFR residual $\Delta$")
    ax.set_title(f"Tertile test: high - low = "
                 f"{tert_info['mean_high'] - tert_info['mean_low']:+.3f} dex "
                 f"(one-tailed p = {tert_info['mw_p_one_tailed']:.4f})")
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(out, dpi=140)
    plt.close()


def plot_bootstrap(rho_info, out):
    rhos = rho_info["bootstrap_rhos"]
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.hist(rhos, bins=60, color="#4a90e2", edgecolor="black", alpha=0.8)
    ax.axvline(rho_info["rho"], color="red", lw=2, label=f"observed rho = {rho_info['rho']:+.3f}")
    ax.axvline(0, color="k", lw=0.5, ls="--")
    ax.axvspan(rho_info["ci_95"][0], rho_info["ci_95"][1],
               color="red", alpha=0.12, label=f"95% CI")
    ax.set_xlabel("Bootstrap Spearman rho")
    ax.set_ylabel("count")
    ax.set_title(f"Bootstrap of Spearman rho (N_boot = {len(rhos):,})")
    ax.legend(fontsize=9)
    plt.tight_layout()
    plt.savefig(out, dpi=140)
    plt.close()


def plot_proxy_comparison(df, out):
    """Run Spearman with each proxy as the primary variable."""
    proxies = {
        "z0MGS":        "logSFR_z0MGS_17",
        "z0MGS (16)":   "logSFR_z0MGS_16",
        "calibrated":   "logSFR_calibrated",
        "literature":   "logSFR_literature",
        "T-type":       "T",
    }
    rhos, ps, ns, labels = [], [], [], []
    for label, col in proxies.items():
        # Refit BTFR on each proxy's sub-sample
        sub = df[df[col].notna() & (df["Q"] == 1)]
        if len(sub) < 5:
            continue
        fit_sub, _ = fit_btfr_and_residuals(sub)
        rho, p = spearmanr(fit_sub[col], fit_sub["Delta"])
        rhos.append(rho)
        ps.append(p / 2 if rho > 0 else 1 - p / 2)
        ns.append(len(sub))
        labels.append(f"{label}\n(n={len(sub)})")
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(labels, rhos, color=["#1f77b4", "#1f77b4", "#ff7f0e",
                                          "#2ca02c", "#777777"][:len(rhos)],
                   edgecolor="black")
    for bar, rho, p in zip(bars, rhos, ps):
        ax.text(bar.get_x() + bar.get_width() / 2, rho + 0.02,
                f"rho={rho:+.2f}\np={p:.3f}", ha="center", fontsize=9)
    ax.axhline(0, color="k", lw=0.5)
    ax.set_ylabel("Spearman rho(logSFR, Delta)")
    ax.set_title("Proxy swap: each SFR proxy as the primary variable (Q=1)")
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(out, dpi=140)
    plt.close()


# ---------------------------------------------------------------------------
# Robustness runner
# ---------------------------------------------------------------------------
def single_test(df, label, x_col="logSFR", y_col="Delta"):
    if len(df) < 5:
        return dict(label=label, n=len(df), rho=np.nan, p_two=np.nan,
                    p_one=np.nan, note="n < 5")
    rho, p2 = spearmanr(df[x_col], df[y_col])
    tau, p_k = kendalltau(df[x_col], df[y_col])
    return dict(
        label=label, n=int(len(df)),
        rho=float(rho), p_two=float(p2),
        p_one=float(p2 / 2 if rho > 0 else 1 - p2 / 2),
        kendall_tau=float(tau), kendall_p=float(p_k),
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 78)
    print("ED-BTFR-Activity Union Test")
    print("=" * 78)

    # 1. Load and assign proxies
    union = load_modules()
    proxy = union.apply(assign_proxy, axis=1, result_type="expand")
    proxy.columns = ["logSFR", "proxy_tier"]
    union = pd.concat([union, proxy], axis=1)
    union.to_csv(UNION_CSV, index=False)
    print(f"\nUnion table written: {UNION_CSV}")
    print(f"Total galaxies in union: {len(union)}")
    print("Breakdown by proxy tier:")
    print(union["proxy_tier"].value_counts().to_string())
    print("\nBreakdown by Q flag:")
    print(union["Q"].value_counts().to_string())

    # 2. Primary sample: Q=1, non-null logSFR
    primary = union[(union["Q"] == 1) & union["logSFR"].notna()].copy()
    print(f"\nPrimary sample (Q=1, has logSFR): n = {len(primary)}")

    # Fit under BOTH conventions and compare.
    fit_primary, fit_info = fit_btfr_and_residuals(primary, "V_on_M")
    fit_primary_MV, fit_info_MV = fit_btfr_and_residuals(primary, "M_on_V")

    print(f"\nBTFR fit -- two conventions:")
    print(f"  V-on-M Theil-Sen: slope = {fit_info['slope_V_on_M_equiv']:.4f}  "
          f"intercept = {fit_info['intercept_V_on_M_equiv']:.4f}")
    print(f"  M-on-V Theil-Sen (inverted): slope = {fit_info_MV['slope_V_on_M_equiv']:.4f}  "
          f"intercept = {fit_info_MV['intercept_V_on_M_equiv']:.4f}")
    print(f"  ED predicts 0.250  |  LCDM virial predicts 0.333")

    # Sanity: check that V-on-M residuals have no mass trend while
    # M-on-V-inverted residuals DO (the core of the methodology issue).
    rho_mass_V, _ = spearmanr(fit_primary["logMb"], fit_primary["Delta"])
    rho_mass_M, _ = spearmanr(fit_primary_MV["logMb"], fit_primary_MV["Delta"])
    print(f"\nSpearman(logMb, Delta) -- tests whether fit is properly de-trended:")
    print(f"  V-on-M Delta:   rho(logMb, Delta) = {rho_mass_V:+.3f}  (should be ~0)")
    print(f"  M-on-V Delta:   rho(logMb, Delta) = {rho_mass_M:+.3f}  (nonzero => mass bias)")

    # Correlation of SFR with mass (needed to understand confound magnitude)
    rho_sfr_mass, _ = spearmanr(primary["logSFR"], primary["logMb"])
    print(f"  SFR-mass main sequence: rho(logSFR, logMb) = {rho_sfr_mass:+.3f}")
    print(f"  => With mass-biased Delta, some of the SFR-Delta correlation")
    print(f"     is a proxy for the SFR-mass main sequence.")

    # 3. Main Spearman under BOTH conventions (bootstrap on V-on-M = primary).
    rho_main = spearman_with_bootstrap(
        fit_primary["logSFR"].values, fit_primary["Delta"].values)
    rho_main_MV, _ = spearmanr(fit_primary_MV["logSFR"], fit_primary_MV["Delta"])
    p_main_MV = spearmanr(fit_primary_MV["logSFR"], fit_primary_MV["Delta"])[1]
    print(f"\nMain Spearman rho(logSFR, Delta):")
    print(f"  V-on-M convention (clean):     rho = {rho_main['rho']:+.3f}  "
          f"p_2 = {rho_main['p_two_tailed']:.4f}  "
          f"p_1(ED+) = {rho_main['p_one_tailed']:.4f}")
    print(f"  M-on-V convention (reproduces published modules):  "
          f"rho = {rho_main_MV:+.3f}  p_2 = {p_main_MV:.4f}")
    print(f"  95% bootstrap CI (V-on-M) = "
          f"[{rho_main['ci_95'][0]:+.3f}, {rho_main['ci_95'][1]:+.3f}]")

    # 4. Permutation null
    p_perm = permutation_p(
        fit_primary["logSFR"].values, fit_primary["Delta"].values)
    print(f"  permutation-null one-tailed p = {p_perm:.4f} (N_perm = {N_PERM:,})")

    # 5. Tertile test
    tert = tertile_test(fit_primary)
    print(f"\nTertile test (Mann-Whitney high > low, one-tailed):")
    print(f"  low (n={tert['n_low']}):  mean Delta = {tert['mean_low']:+.4f}")
    print(f"  mid (n={tert['n_mid']}):  mean Delta = {tert['mean_mid']:+.4f}")
    print(f"  high (n={tert['n_high']}): mean Delta = {tert['mean_high']:+.4f}")
    print(f"  delta high-low = {tert['mean_high'] - tert['mean_low']:+.4f} dex")
    print(f"  U = {tert['mw_U']:.1f},  p = {tert['mw_p_one_tailed']:.4f}")

    # 6. Partial correlation (mass-controlled) in BOTH conventions.
    #    This is the definitive test -- it removes the mass confound.
    partial = partial_spearman_rho_control_mass(fit_primary)
    partial_MV = partial_spearman_rho_control_mass(fit_primary_MV)
    print(f"\nPartial Spearman rho(logSFR, Delta | logMb)"
          f"  -- the definitive test:")
    print(f"  V-on-M convention: rho_partial = {partial['partial_rho']:+.3f}  "
          f"p_2 = {partial['p_two_tailed']:.4f}")
    print(f"  M-on-V convention: rho_partial = {partial_MV['partial_rho']:+.3f}  "
          f"p_2 = {partial_MV['p_two_tailed']:.4f}")
    print(f"  ED prediction: rho_partial > 0 and significant.")
    print(f"  Both conventions should converge after mass is partialled out.")

    # 7. Kendall tau (robustness number)
    ken = kendall_summary(fit_primary["logSFR"].values,
                           fit_primary["Delta"].values)
    print(f"\nKendall tau = {ken['tau']:+.3f}  p = {ken['p_two_tailed']:.4f}")

    # 8. Robustness checks
    print("\n" + "-" * 78)
    print("Robustness checks")
    print("-" * 78)
    robustness_rows = []

    # a) z0MGS-only (uses z0MGS rank)
    z0mgs_sub = primary[primary["proxy_tier"] == "z0MGS"].copy()
    z0mgs_sub, _ = fit_btfr_and_residuals(z0mgs_sub)
    robustness_rows.append(single_test(z0mgs_sub, "z0MGS-only (Q=1)"))

    # b) Drop T-type -- union primary already excludes T-type-only.
    #    So this reduces to the main sample; include for transparency.
    robustness_rows.append(single_test(fit_primary, "Primary (no T-type-only)"))

    # c) Q=all (include Q != 1)
    full = union[union["logSFR"].notna()].copy()
    full, _ = fit_btfr_and_residuals(full)
    robustness_rows.append(single_test(full, "Q = all"))

    # d) Proxy swap: each proxy as primary
    for label, col in [("z0MGS (17)", "logSFR_z0MGS_17"),
                        ("z0MGS (16)", "logSFR_z0MGS_16"),
                        ("calibrated", "logSFR_calibrated"),
                        ("literature", "logSFR_literature"),
                        ("T-type ordinal", "T")]:
        sub = union[union[col].notna() & (union["Q"] == 1)].copy()
        if len(sub) < 5:
            robustness_rows.append(dict(
                label=f"{label} (primary, Q=1)", n=len(sub),
                rho=np.nan, p_two=np.nan, p_one=np.nan,
                note="n < 5"))
            continue
        sub, _ = fit_btfr_and_residuals(sub)
        test = single_test(sub, f"{label} primary (Q=1)", x_col=col)
        robustness_rows.append(test)

    # e) Tertile partial / other diagnostics
    robustness_df = pd.DataFrame(robustness_rows)
    robustness_df.to_csv(ROBUST_CSV, index=False)
    print(robustness_df.to_string(index=False))

    # 9. Plots
    print("\n" + "-" * 78)
    print("Plots")
    print("-" * 78)
    plot_btfr(fit_primary, fit_info, PLOTS / "01_btfr_union.png")
    plot_delta_vs_sfr(fit_primary, rho_main, PLOTS / "02_delta_vs_logSFR.png")
    plot_tertile_box(fit_primary, tert, PLOTS / "03_tertile_box.png")
    plot_bootstrap(rho_main, PLOTS / "04_bootstrap_rho.png")
    plot_proxy_comparison(union, PLOTS / "05_proxy_swap.png")
    for p in PLOTS.iterdir():
        print(f"  {p}")

    # 10. Save main results
    main_out = {
        "n_primary": int(len(primary)),
        "n_total_union": int(len(union)),
        "btfr_fit_V_on_M": fit_info,
        "btfr_fit_M_on_V_reproduction": fit_info_MV,
        "mass_trend_in_delta": {
            "V_on_M_convention_rho_mass_delta": float(rho_mass_V),
            "M_on_V_convention_rho_mass_delta": float(rho_mass_M),
            "main_sequence_rho_sfr_mass": float(rho_sfr_mass),
        },
        "spearman_main_V_on_M": {
            k: v for k, v in rho_main.items() if k != "bootstrap_rhos"
        },
        "spearman_main_M_on_V_reproduction": {
            "rho": float(rho_main_MV),
            "p_two_tailed": float(p_main_MV),
        },
        "permutation_p_one_tailed": float(p_perm),
        "tertile": tert,
        "partial_spearman_mass_controlled": {
            "V_on_M": partial,
            "M_on_V": partial_MV,
        },
        "kendall": ken,
        "proxy_tier_counts": union["proxy_tier"].value_counts().to_dict(),
    }
    with open(MAIN_JSON, "w") as f:
        json.dump(main_out, f, indent=2, default=float)
    print(f"\nMain results: {MAIN_JSON}")
    print(f"Robustness table: {ROBUST_CSV}")

    # 11. Console headline
    print("\n" + "=" * 78)
    print("HEADLINE")
    print("=" * 78)
    print(f"Union primary sample: n = {len(primary)}, Q = 1, SFR precedence = "
          f"z0MGS > calibrated > literature.")
    print()
    print("Raw Spearman rho(logSFR, Delta):")
    print(f"  V-on-M convention:   rho = {rho_main['rho']:+.3f}  "
          f"p_2 = {rho_main['p_two_tailed']:.4f}")
    print(f"  M-on-V convention:   rho = {rho_main_MV:+.3f}  "
          f"p_2 = {p_main_MV:.4f}")
    print()
    print("SIGN-FLIP IDENTITY:  at fixed M, Delta_M = -B * Delta_V (B approx slope).")
    print("So the two partial-correlation numbers are ALGEBRAICALLY FORCED to")
    print("equal magnitudes with opposite signs -- they measure the SAME underlying")
    print("question (does V at fixed M depend on SFR?).")
    print()
    print(f"Partial Spearman rho(logSFR, Delta | logMb)  -- the physical test:")
    print(f"  V-on-M:  rho_partial = {partial['partial_rho']:+.3f}  "
          f"p_2 = {partial['p_two_tailed']:.4f}")
    print(f"  M-on-V:  rho_partial = {partial_MV['partial_rho']:+.3f}  "
          f"p_2 = {partial_MV['p_two_tailed']:.4f}")
    print(f"  Sum (identity check, should be approx 0): "
          f"{partial['partial_rho'] + partial_MV['partial_rho']:+.4f}")
    print()
    print("INTERPRETATION")
    print(f"  ED prediction: at fixed M, active galaxies rotate FASTER,")
    print(f"     i.e. rho(Delta_V, logSFR | M) > 0.")
    print(f"  Observed:      rho(Delta_V, logSFR | M) = {partial['partial_rho']:+.3f}")
    direction_ok = partial["partial_rho"] > 0
    p_low = partial["p_two_tailed"] < 0.05
    if direction_ok and p_low:
        status = "ED direction confirmed at 5%."
    elif (not direction_ok) and p_low:
        status = (
            "OPPOSITE sign to ED prediction, at the 5% level.\n"
            "   The published M-on-V +0.263 signal reflects the sign-flip "
            "identity above;\n"
            "   interpreted physically, active galaxies rotate SLIGHTLY SLOWER "
            "at fixed M."
        )
    elif direction_ok and not p_low:
        status = "ED direction, not significant at 5%."
    else:
        status = "Opposite sign to ED, not significant at 5%."
    print(f"  Verdict: {status}")
    print("=" * 78)


if __name__ == "__main__":
    main()
