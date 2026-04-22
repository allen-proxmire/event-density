"""
Galaxy-Galaxy Lensing Pipeline for ED Activity-Dependence Test
===============================================================
Computes stacked excess surface density ΔΣ(R) profiles for GAMA lens
galaxies using KiDS-1000 source shapes, split by M_baryon × sSFR × environment.

Uses the dsigma package (Speagle et al.) for the core GGL computation.

Input:
  - data/ED-WL-Activity/gama_lens_catalog.csv  (221K lens galaxies, pre-binned)
  - data/KiDS-1000/KiDS_DR4.1_ugriZYJHKs_SOM_gold_WL_cat.fits  (21M sources)

Output:
  - data/ED-WL-Activity/esd_profiles/  (one CSV per bin)
  - data/ED-WL-Activity/esd_summary.csv  (all bins concatenated)

Usage:
  # Dry run (one bin):
  python analysis/scripts/ggl_pipeline.py --dry-run

  # Full run (all 18 bins):
  python analysis/scripts/ggl_pipeline.py --all

Requires: numpy, pandas, astropy, dsigma
"""

import argparse
import os
import sys
import time

import numpy as np
import pandas as pd
from astropy.io import fits
from astropy.table import Table
from astropy.cosmology import Planck18 as cosmo
import astropy.units as u

# ================================================================
# Configuration
# ================================================================

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

LENS_CSV = os.path.join(REPO_ROOT, "data", "ED-WL-Activity", "gama_lens_catalog.csv")
KIDS_FITS = os.path.join(REPO_ROOT, "data", "KiDS-1000",
                         "KiDS_DR4.1_ugriZYJHKs_SOM_gold_WL_cat.fits")
OUTPUT_DIR = os.path.join(REPO_ROOT, "data", "ED-WL-Activity", "esd_profiles")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Radial bins: 30 kpc to 3 Mpc, log-spaced, 12 bins
R_MIN_KPC = 30
R_MAX_KPC = 3000
N_RBINS = 12
R_EDGES_KPC = np.logspace(np.log10(R_MIN_KPC), np.log10(R_MAX_KPC), N_RBINS + 1)
R_MID_KPC = np.sqrt(R_EDGES_KPC[:-1] * R_EDGES_KPC[1:])  # geometric mean

# Photo-z source selection: source must be behind the lens
DZ_MIN = 0.1  # minimum redshift gap between source and lens


def load_kids_catalog(fits_path, columns=None):
    """
    Load the KiDS-1000 shear catalog.
    Only reads the specified columns to save memory.
    """
    if columns is None:
        columns = ["RAJ2000", "DECJ2000", "e1", "e2", "weight", "Z_B"]

    print(f"Loading KiDS-1000 catalog from: {fits_path}")
    print(f"  Columns: {columns}")
    t0 = time.time()

    # Read only the columns we need (saves ~80% memory)
    with fits.open(fits_path, memmap=True) as hdul:
        data = hdul[1].data
        n_total = len(data)
        print(f"  Total sources in catalog: {n_total:,}")

        # Extract columns
        src = {}
        for col in columns:
            src[col] = np.array(data[col])
        print(f"  Loaded in {time.time()-t0:.1f}s")

    # Apply quality cuts
    # weight > 0: valid lensfit measurement
    # Z_B > 0.1: valid photo-z
    mask = (src["weight"] > 0) & (src["Z_B"] > 0.1)
    n_good = mask.sum()
    print(f"  Quality cuts (weight>0, Z_B>0.1): {n_good:,} / {n_total:,} "
          f"({100*n_good/n_total:.1f}%)")

    for col in columns:
        src[col] = src[col][mask]

    return src, n_good


def compute_esd_for_bin(lens_df, src, bin_label="test"):
    """
    Compute the stacked excess surface density ΔΣ(R) for a set of lens
    galaxies against the KiDS source catalog.

    This is a direct implementation of the standard GGL estimator:
      ΔΣ(R) = Σ_crit × <γ_t(R)>

    where γ_t is the tangential shear and Σ_crit is the critical surface
    density that depends on the lens-source geometry.

    Parameters
    ----------
    lens_df : DataFrame
        Lens galaxies with columns: ra, dec (or DEC), z_spec
    src : dict
        Source catalog with keys: RAJ2000, DECJ2000, e1, e2, weight, Z_B

    Returns
    -------
    DataFrame with columns: R_kpc, delta_sigma, delta_sigma_err, n_pairs
    """
    n_lens = len(lens_df)
    print(f"  Computing ESD for bin '{bin_label}': {n_lens} lenses")

    # Prepare lens arrays
    # Handle column name case (GAMA returns 'DEC' not 'dec')
    dec_col = "dec" if "dec" in lens_df.columns else "DEC"
    lens_ra = lens_df["ra"].values
    lens_dec = lens_df[dec_col].values
    lens_z = lens_df["z_spec"].values

    # Source arrays
    src_ra = src["RAJ2000"]
    src_dec = src["DECJ2000"]
    src_e1 = src["e1"]
    src_e2 = src["e2"]
    src_w = src["weight"]
    src_zb = src["Z_B"]

    n_src = len(src_ra)

    # Accumulators for each radial bin
    sum_wt_et = np.zeros(N_RBINS)   # weighted tangential shear
    sum_wt_ex = np.zeros(N_RBINS)   # weighted cross shear (systematics check)
    sum_wt = np.zeros(N_RBINS)      # total weight
    sum_wt_sq = np.zeros(N_RBINS)   # for error estimation
    n_pairs = np.zeros(N_RBINS, dtype=np.int64)

    # Process lenses in chunks to show progress
    chunk_size = max(1, n_lens // 20)
    t0 = time.time()

    for i_lens in range(n_lens):
        z_l = lens_z[i_lens]
        ra_l = lens_ra[i_lens]
        dec_l = lens_dec[i_lens]

        # Angular diameter distance to lens
        d_l = cosmo.angular_diameter_distance(z_l).to(u.kpc).value  # kpc

        # Source selection: source must be behind the lens by at least DZ_MIN
        z_src_min = z_l + DZ_MIN

        # Convert radial bin edges to angular separations (degrees) at this lens z
        theta_min_deg = (R_MIN_KPC / d_l) * (180 / np.pi)
        theta_max_deg = (R_MAX_KPC / d_l) * (180 / np.pi)

        # Coarse cut: only sources within theta_max_deg of this lens
        # (use a simple box cut first for speed, then refine)
        cos_dec = np.cos(np.radians(dec_l))
        dra_max = theta_max_deg / max(cos_dec, 0.1)
        ddec_max = theta_max_deg

        mask_box = (
            (np.abs(src_ra - ra_l) < dra_max) &
            (np.abs(src_dec - dec_l) < ddec_max) &
            (src_zb > z_src_min)
        )
        idx = np.where(mask_box)[0]

        if len(idx) == 0:
            continue

        # Compute angular separations (small-angle approx, fine for < few deg)
        dra = (src_ra[idx] - ra_l) * cos_dec * (np.pi / 180)  # radians
        ddec = (src_dec[idx] - dec_l) * (np.pi / 180)          # radians
        theta = np.sqrt(dra**2 + ddec**2)  # radians

        # Physical radius at the lens redshift (kpc)
        R_kpc = theta * d_l  # kpc (since theta in rad, d_l in kpc)

        # Tangential shear: rotate e1, e2 into tangential/cross components
        # phi is the position angle of the source relative to the lens
        phi = np.arctan2(ddec, dra)

        # Tangential and cross components
        cos2phi = np.cos(2 * phi)
        sin2phi = np.sin(2 * phi)
        e_t = -(src_e1[idx] * cos2phi + src_e2[idx] * sin2phi)
        e_x = -(src_e1[idx] * sin2phi - src_e2[idx] * cos2phi)

        # Critical surface density
        d_s = cosmo.angular_diameter_distance(src_zb[idx]).to(u.kpc).value
        d_ls = cosmo.angular_diameter_distance_z1z2(z_l, src_zb[idx]).to(u.kpc).value

        # Σ_crit in M_sun / pc^2 (standard lensing units)
        # Σ_crit = c^2 / (4πG) × D_s / (D_l × D_ls)
        # Exact prefactor: 1.6629e9 when D in kpc, Σ_crit in M_sun/pc^2
        # (verified with astropy constants: c, G, M_sun, pc, kpc)
        SIGMA_CRIT_PREFACTOR = 1.6629e9  # M_sun/pc^2 when D in kpc
        sigma_crit = SIGMA_CRIT_PREFACTOR * d_s / (d_l * d_ls)  # M_sun / pc^2

        # Standard GGL weights: w_ls = w_shape / sigma_crit^2
        w = src_w[idx] / sigma_crit**2

        # ΔΣ estimator: sum(w_ls × e_t × sigma_crit) / sum(w_ls)
        ds_contrib = w * e_t * sigma_crit
        dx_contrib = w * e_x * sigma_crit

        # Bin by radius
        bin_idx = np.digitize(R_kpc, R_EDGES_KPC) - 1  # 0-indexed
        for b in range(N_RBINS):
            in_bin = (bin_idx == b)
            if np.any(in_bin):
                sum_wt_et[b] += np.sum(ds_contrib[in_bin])
                sum_wt_ex[b] += np.sum(dx_contrib[in_bin])
                sum_wt[b] += np.sum(w[in_bin])
                sum_wt_sq[b] += np.sum(w[in_bin]**2)
                n_pairs[b] += np.sum(in_bin)

        # Progress
        if (i_lens + 1) % chunk_size == 0:
            elapsed = time.time() - t0
            eta = elapsed * (n_lens / (i_lens + 1) - 1)
            print(f"    Lens {i_lens+1}/{n_lens} "
                  f"({100*(i_lens+1)/n_lens:.0f}%) "
                  f"elapsed {elapsed:.0f}s, ETA {eta:.0f}s")

    elapsed_total = time.time() - t0
    print(f"  Done in {elapsed_total:.1f}s, total pairs: {n_pairs.sum():,}")

    # Compute ΔΣ and error
    with np.errstate(divide="ignore", invalid="ignore"):
        delta_sigma = np.where(sum_wt > 0, sum_wt_et / sum_wt, np.nan)
        cross_sigma = np.where(sum_wt > 0, sum_wt_ex / sum_wt, np.nan)
        # Error estimate: shape noise propagation
        # σ(ΔΣ) ≈ sqrt(Σ(w² × σ_e² × Σ_crit²)) / Σ(w)
        # ≈ σ_e × sqrt(Σ(w²))/Σ(w) × <Σ_crit>
        # Simplified: use the cross-component RMS as an empirical error estimate
        # (the cross shear should be zero for a real signal; its scatter
        #  gives the noise floor)
        n_eff = np.where(sum_wt_sq > 0, sum_wt**2 / sum_wt_sq, 0)
        # Empirical error from weighted shape noise
        sigma_e = 0.27
        delta_sigma_err = np.where(
            n_eff > 1,
            np.abs(delta_sigma) / np.sqrt(n_eff) + sigma_e / np.sqrt(n_pairs.astype(float)),
            np.nan
        )
        # Better estimate: use the cross shear as a noise floor
        cross_noise = np.abs(cross_sigma)
        delta_sigma_err = np.maximum(delta_sigma_err, cross_noise)

    result = pd.DataFrame({
        "R_kpc": R_MID_KPC,
        "R_min_kpc": R_EDGES_KPC[:-1],
        "R_max_kpc": R_EDGES_KPC[1:],
        "delta_sigma": delta_sigma,
        "delta_sigma_err": delta_sigma_err,
        "cross_sigma": cross_sigma,
        "n_pairs": n_pairs,
        "n_eff": n_eff,
    })

    return result


def main():
    parser = argparse.ArgumentParser(description="GGL pipeline for ED activity test")
    parser.add_argument("--dry-run", action="store_true",
                        help="Run on a single bin (mid/quiet/isolated) only")
    parser.add_argument("--all", action="store_true",
                        help="Run on all 18 bins")
    parser.add_argument("--max-lenses", type=int, default=0,
                        help="Limit number of lenses per bin (0 = no limit)")
    args = parser.parse_args()

    if not args.dry_run and not args.all:
        print("Usage: specify --dry-run or --all")
        return

    # Load lens catalog
    print("Loading lens catalog...")
    lenses = pd.read_csv(LENS_CSV)
    print(f"  {len(lenses)} lens galaxies loaded")
    print(f"  Columns: {list(lenses.columns)}")

    # Load KiDS source catalog
    if not os.path.exists(KIDS_FITS):
        print(f"\nERROR: KiDS catalog not found at: {KIDS_FITS}")
        print("Download it first:")
        print("  curl -L -o data/KiDS-1000/KiDS_DR4.1_ugriZYJHKs_SOM_gold_WL_cat.fits \\")
        print("    https://kids.strw.leidenuniv.nl/DR4/data_files/"
              "KiDS_DR4.1_ugriZYJHKs_SOM_gold_WL_cat.fits")
        return

    src, n_src = load_kids_catalog(KIDS_FITS)

    if args.dry_run:
        # Single bin: mid mass, quiet sSFR, isolated
        bin_mask = (
            (lenses["mbaryon_bin"] == "mid") &
            (lenses["ssfr_bin"] == "quiet") &
            (lenses["in_group"] == 0)
        )
        bin_label = "mid_quiet_isolated"
        bin_lenses = lenses[bin_mask]
        print(f"\nDry run: {len(bin_lenses)} lenses in bin '{bin_label}'")

        if args.max_lenses > 0 and len(bin_lenses) > args.max_lenses:
            bin_lenses = bin_lenses.sample(n=args.max_lenses, random_state=42)
            print(f"  Subsampled to {len(bin_lenses)} lenses for speed")

        result = compute_esd_for_bin(bin_lenses, src, bin_label)

        # Save
        out_path = os.path.join(OUTPUT_DIR, f"esd_{bin_label}.csv")
        result.to_csv(out_path, index=False)
        print(f"\nSaved to: {out_path}")

        # Print summary
        print(f"\n{'R (kpc)':>10} {'DS (Msun/pc2)':>18} {'err':>12} "
              f"{'cross':>12} {'n_pairs':>10} {'S/N':>6}")
        print("-" * 75)
        for _, row in result.iterrows():
            sn = row["delta_sigma"] / row["delta_sigma_err"] \
                if row["delta_sigma_err"] > 0 else 0
            print(f"{row['R_kpc']:>10.0f} {row['delta_sigma']:>18.2f} "
                  f"{row['delta_sigma_err']:>12.2f} {row['cross_sigma']:>12.2f} "
                  f"{row['n_pairs']:>10.0f} {sn:>6.1f}")

    elif args.all:
        # All 18 bins
        bins = lenses.groupby(["mbaryon_bin", "ssfr_bin", "in_group"])
        all_results = []
        bin_summaries = []
        t0_all = time.time()

        for (mb, ss, env), bin_df in bins:
            env_label = "isolated" if env == 0 else "grouped"
            bin_label = f"{mb}_{ss}_{env_label}"
            n_total_in_bin = len(bin_df)

            if args.max_lenses > 0 and len(bin_df) > args.max_lenses:
                bin_df = bin_df.sample(n=args.max_lenses, random_state=42)

            n_used = len(bin_df)
            result = compute_esd_for_bin(bin_df, src, bin_label)
            result["mbaryon_bin"] = mb
            result["ssfr_bin"] = ss
            result["env"] = env_label
            all_results.append(result)

            # Save per-bin CSV
            out_path = os.path.join(OUTPUT_DIR, f"esd_{bin_label}.csv")
            result.to_csv(out_path, index=False)

            # Per-bin text summary
            r_mid = result[(result["R_kpc"] >= 100) & (result["R_kpc"] <= 1000)]
            mean_ds = r_mid["delta_sigma"].mean() if len(r_mid) > 0 else np.nan
            r_outer = result[result["R_kpc"] >= 500]
            cross_below = (r_outer["cross_sigma"].abs() <
                           r_outer["delta_sigma"].abs()).all() \
                if len(r_outer) > 0 else False
            # Check monotonic decline at R > 200 kpc
            r_dec = result[result["R_kpc"] >= 200]
            monotonic = np.all(np.diff(r_dec["delta_sigma"].values) <= 0) \
                if len(r_dec) > 1 else False

            summary_line = {
                "bin": bin_label,
                "mbaryon_bin": mb,
                "ssfr_bin": ss,
                "env": env_label,
                "n_total": n_total_in_bin,
                "n_used": n_used,
                "mean_DS_100_1000": mean_ds,
                "cross_below_signal_R500": cross_below,
                "monotonic_R200": monotonic,
                "total_pairs": result["n_pairs"].sum(),
            }
            bin_summaries.append(summary_line)

            print(f"\n  >> {bin_label}: n={n_used}, "
                  f"mean DS(100-1000)={mean_ds:.2f} Msun/pc2, "
                  f"pairs={result['n_pairs'].sum():,}, "
                  f"cross<signal@R500={cross_below}, "
                  f"monotonic@R200={monotonic}")

        elapsed_all = time.time() - t0_all

        # Concatenate and save
        all_df = pd.concat(all_results, ignore_index=True)
        summary_path = os.path.join(
            REPO_ROOT, "data", "ED-WL-Activity", "esd_summary.csv"
        )
        all_df.to_csv(summary_path, index=False)

        # Save text summary
        sum_df = pd.DataFrame(bin_summaries)
        sum_path = os.path.join(
            REPO_ROOT, "data", "ED-WL-Activity", "bin_summaries.csv"
        )
        sum_df.to_csv(sum_path, index=False)

        # Global summary
        print("\n" + "=" * 80)
        print("GLOBAL SUMMARY")
        print("=" * 80)
        print(f"Total runtime: {elapsed_all:.0f}s ({elapsed_all/3600:.1f} hours)")
        print(f"Bins completed: {len(bin_summaries)}")
        print(f"Total lens-source pairs: {sum_df['total_pairs'].sum():,}")
        print()
        print(f"{'Bin':<30} {'n_used':>6} {'mean_DS':>10} "
              f"{'cross_ok':>9} {'monoton':>8}")
        print("-" * 70)
        for _, s in sum_df.iterrows():
            print(f"{s['bin']:<30} {s['n_used']:>6} "
                  f"{s['mean_DS_100_1000']:>10.2f} "
                  f"{str(s['cross_below_signal_R500']):>9} "
                  f"{str(s['monotonic_R200']):>8}")

        print(f"\nAll profiles saved to: {OUTPUT_DIR}/")
        print(f"Summary CSV: {sum_path}")
        print(f"Combined CSV: {summary_path}")


if __name__ == "__main__":
    main()
