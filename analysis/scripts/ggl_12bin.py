"""
12-Bin GGL Run: Active vs Quiet at Fixed Mass x Environment
=============================================================
Drops the "moderate" sSFR bin, keeps only "quiet" and "active."
Uses up to 5000 lenses per bin for higher S/N.

3 mass bins x 2 sSFR bins x 2 environment bins = 12 bins.

Usage:
  python analysis/scripts/ggl_12bin.py
"""

import os
import sys
import time

import numpy as np
import pandas as pd

# Import the GGL computation function from the main pipeline
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ggl_pipeline import (
    load_kids_catalog, compute_esd_for_bin,
    LENS_CSV, KIDS_FITS, R_MID_KPC, N_RBINS
)

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUTPUT_DIR = os.path.join(REPO_ROOT, "data", "ED-WL-Activity", "esd_profiles_12bin")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MAX_LENSES = 5000


def main():
    t0_total = time.time()

    # Load lens catalog
    print("Loading lens catalog...")
    lenses = pd.read_csv(LENS_CSV)
    print(f"  Total: {len(lenses)} galaxies")

    # Filter to quiet and active only (drop moderate)
    lenses_12 = lenses[lenses["ssfr_bin"].isin(["quiet", "active"])].copy()
    print(f"  After dropping 'moderate': {len(lenses_12)} galaxies")

    # Bin population report
    pop = lenses_12.groupby(
        ["mbaryon_bin", "ssfr_bin", "in_group"]
    ).size().reset_index(name="n_available")
    pop["env"] = pop["in_group"].map({0: "isolated", 1: "grouped"})
    pop["bin_label"] = pop["mbaryon_bin"] + "_" + pop["ssfr_bin"] + "_" + pop["env"]
    pop["n_used"] = pop["n_available"].clip(upper=MAX_LENSES)

    print(f"\n{'Bin':<30} {'Available':>10} {'Will use':>10}")
    print("-" * 55)
    for _, r in pop.iterrows():
        print(f"{r['bin_label']:<30} {r['n_available']:>10} {r['n_used']:>10}")
    print(f"{'TOTAL':<30} {pop['n_available'].sum():>10} {pop['n_used'].sum():>10}")

    # Save population report
    pop_path = os.path.join(REPO_ROOT, "data", "ED-WL-Activity",
                            "bin_populations_12bin.csv")
    pop.to_csv(pop_path, index=False)
    print(f"\nPopulation report saved: {pop_path}")

    # Load KiDS source catalog
    if not os.path.exists(KIDS_FITS):
        print(f"ERROR: KiDS catalog not found at {KIDS_FITS}")
        return
    src, n_src = load_kids_catalog(KIDS_FITS)

    # Run all 12 bins
    all_results = []
    bin_summaries = []

    groups = lenses_12.groupby(["mbaryon_bin", "ssfr_bin", "in_group"])
    n_bins = len(groups)
    i_bin = 0

    for (mb, ss, env_flag), bin_df in groups:
        i_bin += 1
        env_label = "isolated" if env_flag == 0 else "grouped"
        bin_label = f"{mb}_{ss}_{env_label}"
        n_available = len(bin_df)

        # Downsample if needed
        if n_available > MAX_LENSES:
            bin_df = bin_df.sample(n=MAX_LENSES, random_state=42)
        n_used = len(bin_df)

        print(f"\n[{i_bin}/{n_bins}] {bin_label}: "
              f"{n_used} lenses (of {n_available} available)")

        result = compute_esd_for_bin(bin_df, src, bin_label)
        result["mbaryon_bin"] = mb
        result["ssfr_bin"] = ss
        result["env"] = env_label

        # Save per-bin CSV
        out_path = os.path.join(OUTPUT_DIR, f"esd_{bin_label}.csv")
        result.to_csv(out_path, index=False)
        all_results.append(result)

        # Per-bin summary
        r_mid = result[(result["R_kpc"] >= 100) & (result["R_kpc"] <= 1000)]
        mean_ds = r_mid["delta_sigma"].mean() if len(r_mid) > 0 else np.nan

        r_outer = result[result["R_kpc"] >= 500]
        if len(r_outer) > 0:
            cross_ok = (r_outer["cross_sigma"].abs() <
                        r_outer["delta_sigma"].abs()).all()
        else:
            cross_ok = False

        r_dec = result[result["R_kpc"] >= 200]
        monotonic = bool(np.all(np.diff(r_dec["delta_sigma"].values) <= 0)) \
            if len(r_dec) > 1 else False

        summary = {
            "bin": bin_label,
            "mbaryon_bin": mb,
            "ssfr_bin": ss,
            "env": env_label,
            "n_available": n_available,
            "n_used": n_used,
            "mean_DS_100_1000": mean_ds,
            "cross_below_signal_R500": cross_ok,
            "monotonic_R200": monotonic,
            "total_pairs": int(result["n_pairs"].sum()),
        }
        bin_summaries.append(summary)

        elapsed = time.time() - t0_total
        eta = elapsed / i_bin * (n_bins - i_bin)
        print(f"  >> mean DS(100-1000)={mean_ds:.2f} Msun/pc2, "
              f"pairs={result['n_pairs'].sum():,}, "
              f"elapsed={elapsed/3600:.1f}h, ETA={eta/3600:.1f}h")

    # Save combined results
    all_df = pd.concat(all_results, ignore_index=True)
    summary_path = os.path.join(REPO_ROOT, "data", "ED-WL-Activity",
                                "esd_summary_12bin.csv")
    all_df.to_csv(summary_path, index=False)

    sum_df = pd.DataFrame(bin_summaries)
    sum_path = os.path.join(REPO_ROOT, "data", "ED-WL-Activity",
                            "bin_summaries_12bin.csv")
    sum_df.to_csv(sum_path, index=False)

    total_time = time.time() - t0_total

    # Global summary
    print("\n" + "=" * 80)
    print("12-BIN GLOBAL SUMMARY")
    print("=" * 80)
    print(f"Total runtime: {total_time:.0f}s ({total_time/3600:.1f} hours)")
    print(f"Bins completed: {len(bin_summaries)}")
    print(f"Total lens-source pairs: {sum_df['total_pairs'].sum():,}")
    print()

    print(f"{'Bin':<30} {'n_used':>6} {'mean_DS':>10} "
          f"{'cross_ok':>9} {'monoton':>8} {'pairs':>12}")
    print("-" * 80)
    for _, s in sum_df.iterrows():
        print(f"{s['bin']:<30} {s['n_used']:>6} "
              f"{s['mean_DS_100_1000']:>10.2f} "
              f"{str(s['cross_below_signal_R500']):>9} "
              f"{str(s['monotonic_R200']):>8} "
              f"{s['total_pairs']:>12,}")

    # The key ED comparison: active vs quiet at fixed mass + environment
    print("\n" + "=" * 80)
    print("KEY COMPARISON: active vs quiet at fixed mass + environment")
    print("ED predicts: active > quiet (positive difference)")
    print("=" * 80)
    for mb in ["low", "mid", "high"]:
        for env in ["isolated", "grouped"]:
            q = sum_df[(sum_df["mbaryon_bin"] == mb) &
                       (sum_df["ssfr_bin"] == "quiet") &
                       (sum_df["env"] == env)]
            a = sum_df[(sum_df["mbaryon_bin"] == mb) &
                       (sum_df["ssfr_bin"] == "active") &
                       (sum_df["env"] == env)]
            if len(q) > 0 and len(a) > 0:
                ds_q = q.iloc[0]["mean_DS_100_1000"]
                ds_a = a.iloc[0]["mean_DS_100_1000"]
                diff = ds_a - ds_q
                sign = "+" if diff > 0 else "-"
                print(f"  M_b={mb:>4}, env={env:<8}: "
                      f"quiet={ds_q:>7.2f}, active={ds_a:>7.2f}, "
                      f"diff={sign}{abs(diff):.2f}")

    # Environment comparison
    print("\n" + "=" * 80)
    print("ENVIRONMENT COMPARISON: grouped vs isolated at fixed mass + sSFR")
    print("ED predicts: grouped > isolated (environmental sourcing)")
    print("=" * 80)
    for mb in ["low", "mid", "high"]:
        for ss in ["quiet", "active"]:
            iso = sum_df[(sum_df["mbaryon_bin"] == mb) &
                         (sum_df["ssfr_bin"] == ss) &
                         (sum_df["env"] == "isolated")]
            grp = sum_df[(sum_df["mbaryon_bin"] == mb) &
                         (sum_df["ssfr_bin"] == ss) &
                         (sum_df["env"] == "grouped")]
            if len(iso) > 0 and len(grp) > 0:
                ds_i = iso.iloc[0]["mean_DS_100_1000"]
                ds_g = grp.iloc[0]["mean_DS_100_1000"]
                diff = ds_g - ds_i
                sign = "+" if diff > 0 else "-"
                print(f"  M_b={mb:>4}, sSFR={ss:<6}: "
                      f"iso={ds_i:>7.2f}, grp={ds_g:>7.2f}, "
                      f"diff={sign}{abs(diff):.2f}")

    print(f"\nAll profiles: {OUTPUT_DIR}/")
    print(f"Summary: {sum_path}")
    print(f"Combined: {summary_path}")
    print(f"Populations: {pop_path}")


if __name__ == "__main__":
    main()
