"""
4-Bin High-S/N GGL: Active vs Quiet at Fixed Mass
===================================================
Coarse binning for maximum signal-to-noise:
  2 mass bins (low/high at median M_baryon)
  × 2 sSFR bins (quiet/active, dropping moderate)
  = 4 bins

Uses the FULL GAMA lens sample (no max-lenses cap) with an
RA-presorted source catalog for ~10x speedup over the original pipeline.

Usage:
  python analysis/scripts/ggl_4bin.py
"""

import os
import sys
import time

import numpy as np
import pandas as pd
from astropy.io import fits
from astropy.cosmology import Planck18 as cosmo
import astropy.units as u

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LENS_CSV = os.path.join(REPO_ROOT, "data", "ED-WL-Activity", "gama_lens_catalog.csv")
KIDS_FITS = os.path.join(REPO_ROOT, "data", "KiDS-1000",
                         "KiDS_DR4.1_ugriZYJHKs_SOM_gold_WL_cat.fits")
OUTPUT_DIR = os.path.join(REPO_ROOT, "data", "ED-WL-Activity", "esd_profiles_4bin")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Radial bins: 30 kpc to 3 Mpc
R_EDGES_KPC = np.logspace(np.log10(30), np.log10(3000), 13)
R_MID_KPC = np.sqrt(R_EDGES_KPC[:-1] * R_EDGES_KPC[1:])
N_RBINS = len(R_MID_KPC)

DZ_MIN = 0.1
SIGMA_CRIT_PREFACTOR = 1.6629e9  # M_sun/pc^2 when D in kpc


def load_kids_presorted(fits_path):
    """Load KiDS catalog pre-sorted by RA. Uses float32 (~500 MB total)."""
    import gc
    print("Loading KiDS-1000 catalog...")
    t0 = time.time()

    # Step 1: get sort index from RA alone
    with fits.open(fits_path, memmap=True) as hdul:
        ra_raw = np.array(hdul[1].data["RAJ2000"], dtype=np.float32)
    n = len(ra_raw)
    print(f"  {n:,} sources, computing RA sort order...")
    sort_idx = np.argsort(ra_raw)
    del ra_raw
    gc.collect()

    # Step 2: load each column sorted, one at a time
    cols_out = {}
    for col, key in [("RAJ2000", "ra"), ("DECJ2000", "dec"),
                     ("e1", "e1"), ("e2", "e2"),
                     ("weight", "w"), ("Z_B", "zb")]:
        with fits.open(fits_path, memmap=True) as hdul:
            arr = np.array(hdul[1].data[col], dtype=np.float32)
        cols_out[key] = arr[sort_idx]
        del arr
        gc.collect()

    del sort_idx
    gc.collect()

    print(f"  Loaded + sorted in {time.time()-t0:.0f}s, "
          f"~{6 * n * 4 / 1e9:.1f} GB")
    return cols_out


def compute_esd_fast(lens_df, src, bin_label="test"):
    """
    Compute stacked ESD with RA-presorted source lookup.
    ~10x faster than the original pipeline for large lens samples.
    """
    dec_col = "dec" if "dec" in lens_df.columns else "DEC"
    lens_ra = lens_df["ra"].values
    lens_dec = lens_df[dec_col].values
    lens_z = lens_df["z_spec"].values
    n_lens = len(lens_ra)

    src_ra = src["ra"]
    src_dec = src["dec"]
    src_e1 = src["e1"]
    src_e2 = src["e2"]
    src_w = src["w"]
    src_zb = src["zb"]

    # Accumulators
    sum_wt_et = np.zeros(N_RBINS)
    sum_wt_ex = np.zeros(N_RBINS)
    sum_wt = np.zeros(N_RBINS)
    sum_wt2_sc2 = np.zeros(N_RBINS)  # for proper error: sum(w^2 * sigma_crit^2)
    n_pairs = np.zeros(N_RBINS, dtype=np.int64)

    chunk = max(1, n_lens // 20)
    t0 = time.time()

    for i in range(n_lens):
        z_l = lens_z[i]
        ra_l = lens_ra[i]
        dec_l = lens_dec[i]

        d_l = cosmo.angular_diameter_distance(z_l).to(u.kpc).value

        # Angular search radius (for R_max = 3000 kpc)
        theta_max = 3000.0 / d_l  # radians
        theta_max_deg = theta_max * 180 / np.pi

        cos_dec = np.cos(np.radians(dec_l))
        dra_max = theta_max_deg / max(cos_dec, 0.1)

        # RA binary search (the speedup)
        i_lo = np.searchsorted(src_ra, ra_l - dra_max)
        i_hi = np.searchsorted(src_ra, ra_l + dra_max)

        if i_hi <= i_lo:
            continue

        # Slice to RA strip
        s_ra = src_ra[i_lo:i_hi]
        s_dec = src_dec[i_lo:i_hi]
        s_e1 = src_e1[i_lo:i_hi]
        s_e2 = src_e2[i_lo:i_hi]
        s_w = src_w[i_lo:i_hi]
        s_zb = src_zb[i_lo:i_hi]

        # Dec cut + photo-z cut
        z_src_min = z_l + DZ_MIN
        mask = (np.abs(s_dec - dec_l) < theta_max_deg) & (s_zb > z_src_min)
        idx = np.where(mask)[0]
        if len(idx) == 0:
            continue

        # Angular separations
        dra = (s_ra[idx] - ra_l) * cos_dec * (np.pi / 180)
        ddec = (s_dec[idx] - dec_l) * (np.pi / 180)
        theta = np.sqrt(dra**2 + ddec**2)
        R_kpc = theta * d_l

        # Tangential/cross shear
        phi = np.arctan2(ddec, dra)
        cos2phi = np.cos(2 * phi)
        sin2phi = np.sin(2 * phi)
        e_t = -(s_e1[idx] * cos2phi + s_e2[idx] * sin2phi)
        e_x = -(s_e1[idx] * sin2phi - s_e2[idx] * cos2phi)

        # Sigma_crit
        d_s = cosmo.angular_diameter_distance(s_zb[idx]).to(u.kpc).value
        d_ls = cosmo.angular_diameter_distance_z1z2(z_l, s_zb[idx]).to(u.kpc).value
        sigma_crit = SIGMA_CRIT_PREFACTOR * d_s / (d_l * d_ls)

        # Weights and contributions
        wt = s_w[idx] / sigma_crit**2
        ds_c = wt * e_t * sigma_crit
        dx_c = wt * e_x * sigma_crit

        # Bin by radius
        bin_idx = np.digitize(R_kpc, R_EDGES_KPC) - 1
        for b in range(N_RBINS):
            m = (bin_idx == b)
            if np.any(m):
                sum_wt_et[b] += np.sum(ds_c[m])
                sum_wt_ex[b] += np.sum(dx_c[m])
                sum_wt[b] += np.sum(wt[m])
                sum_wt2_sc2[b] += np.sum(wt[m]**2 * sigma_crit[m]**2)
                n_pairs[b] += np.sum(m)

        if (i + 1) % chunk == 0:
            el = time.time() - t0
            eta = el * (n_lens / (i + 1) - 1)
            print(f"    [{bin_label}] Lens {i+1}/{n_lens} "
                  f"({100*(i+1)/n_lens:.0f}%) "
                  f"{el:.0f}s elapsed, ETA {eta:.0f}s")

    elapsed = time.time() - t0
    print(f"  [{bin_label}] Done: {n_lens} lenses, {n_pairs.sum():,} pairs, "
          f"{elapsed:.0f}s ({elapsed/n_lens:.3f} s/lens)")

    # Compute results
    with np.errstate(divide="ignore", invalid="ignore"):
        delta_sigma = np.where(sum_wt > 0, sum_wt_et / sum_wt, np.nan)
        cross_sigma = np.where(sum_wt > 0, sum_wt_ex / sum_wt, np.nan)
        # Proper shape-noise error:
        # sigma^2(DS) = sigma_e^2 * sum(w^2 * Sigma_crit^2) / (sum w)^2
        sigma_e = 0.27
        ds_err = np.where(
            sum_wt > 0,
            sigma_e * np.sqrt(sum_wt2_sc2) / sum_wt,
            np.nan
        )

    return pd.DataFrame({
        "R_kpc": R_MID_KPC,
        "delta_sigma": delta_sigma,
        "delta_sigma_err": ds_err,
        "cross_sigma": cross_sigma,
        "n_pairs": n_pairs,
    })


def main():
    t0_all = time.time()

    # Load and bin lenses
    print("Loading lens catalog...")
    lenses = pd.read_csv(LENS_CSV)
    lenses = lenses[lenses["ssfr_bin"].isin(["quiet", "active"])].copy()

    med_mb = lenses["log_mbaryon"].median()
    lenses["mass2"] = np.where(lenses["log_mbaryon"] <= med_mb, "low", "high")

    print(f"  {len(lenses)} lenses (quiet + active only)")
    print(f"  Mass split at log M_baryon = {med_mb:.2f}")
    print()

    # Population table
    pop = lenses.groupby(["mass2", "ssfr_bin"]).size()
    print("Bin populations:")
    print(pop)
    print(f"Total: {pop.sum()}")
    print()

    # Load KiDS (pre-sorted)
    src = load_kids_presorted(KIDS_FITS)

    # Run 4 bins
    all_results = []
    summaries = []
    groups = lenses.groupby(["mass2", "ssfr_bin"])

    for i, ((mb, ss), bin_df) in enumerate(groups):
        label = f"{mb}_{ss}"
        n = len(bin_df)
        print(f"\n{'='*60}")
        print(f"BIN {i+1}/4: {label} ({n} lenses)")
        print(f"{'='*60}")

        result = compute_esd_fast(bin_df, src, label)

        # Save
        out = os.path.join(OUTPUT_DIR, f"esd_{label}.csv")
        result.to_csv(out, index=False)

        # Summary stats (100-1000 kpc)
        mid = result[(result["R_kpc"] >= 100) & (result["R_kpc"] <= 1000)]
        mean_ds = mid["delta_sigma"].mean()
        mean_err = mid["delta_sigma_err"].mean()
        cross_rms = np.sqrt((mid["cross_sigma"]**2).mean())

        r_outer = result[result["R_kpc"] >= 500]
        cross_ok = bool((r_outer["cross_sigma"].abs() <
                         r_outer["delta_sigma"].abs()).all()) if len(r_outer) > 0 else False

        r_dec = result[result["R_kpc"] >= 200]
        monotonic = bool(np.all(np.diff(r_dec["delta_sigma"].values) <= 0)) \
            if len(r_dec) > 1 else False

        sn = abs(mean_ds) / mean_err if mean_err > 0 else 0

        summaries.append({
            "bin": label, "mass": mb, "ssfr": ss, "n_lenses": n,
            "mean_DS": mean_ds, "mean_err": mean_err, "cross_rms": cross_rms,
            "SN": sn, "cross_ok": cross_ok, "monotonic": monotonic,
            "total_pairs": int(result["n_pairs"].sum()),
        })

        print(f"  mean DS(100-1000) = {mean_ds:.3f} +/- {mean_err:.3f} Msun/pc2")
        print(f"  S/N = {sn:.1f}, cross_RMS = {cross_rms:.3f}")

        all_results.append(result)

    total_time = time.time() - t0_all
    sdf = pd.DataFrame(summaries)

    # Save
    all_df = pd.concat([r.assign(mass=s["mass"], ssfr=s["ssfr"])
                        for r, s in zip(all_results, summaries)], ignore_index=True)
    all_df.to_csv(os.path.join(REPO_ROOT, "data", "ED-WL-Activity",
                               "esd_summary_4bin.csv"), index=False)
    sdf.to_csv(os.path.join(REPO_ROOT, "data", "ED-WL-Activity",
                            "bin_summaries_4bin.csv"), index=False)

    # Final report
    print("\n" + "=" * 80)
    print("4-BIN GLOBAL SUMMARY")
    print("=" * 80)
    print(f"Runtime: {total_time:.0f}s ({total_time/3600:.1f} hours)")
    print(f"Total pairs: {sdf['total_pairs'].sum():,}")
    print()

    print(f"{'Bin':<15} {'n_lens':>7} {'mean_DS':>9} {'error':>8} "
          f"{'S/N':>6} {'cross_rms':>10} {'cross_ok':>9} {'mono':>6}")
    print("-" * 75)
    for _, s in sdf.iterrows():
        print(f"{s['bin']:<15} {s['n_lenses']:>7} {s['mean_DS']:>9.3f} "
              f"{s['mean_err']:>8.3f} {s['SN']:>6.1f} {s['cross_rms']:>10.3f} "
              f"{str(s['cross_ok']):>9} {str(s['monotonic']):>6}")

    # THE ED TEST
    print("\n" + "=" * 80)
    print("THE ED TEST: active - quiet at fixed mass")
    print("ED predicts: active > quiet (positive difference)")
    print("=" * 80)
    for mb in ["low", "high"]:
        q = sdf[(sdf["mass"] == mb) & (sdf["ssfr"] == "quiet")].iloc[0]
        a = sdf[(sdf["mass"] == mb) & (sdf["ssfr"] == "active")].iloc[0]
        diff = a["mean_DS"] - q["mean_DS"]
        err_diff = np.sqrt(a["mean_err"]**2 + q["mean_err"]**2)
        sig = abs(diff) / err_diff if err_diff > 0 else 0
        sign = "+" if diff > 0 else "-"
        verdict = "NOISE" if sig < 2 else ("MARGINAL" if sig < 3 else "SIGNIFICANT")
        print(f"  M_baryon={mb:>4}: quiet={q['mean_DS']:>8.3f}, "
              f"active={a['mean_DS']:>8.3f}, "
              f"diff={sign}{abs(diff):.3f} +/- {err_diff:.3f}, "
              f"significance={sig:.1f} sigma -> {verdict}")

    print(f"\nProfiles saved to: {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
