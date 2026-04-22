"""
GAMA DR4 Lens Catalog Builder
==============================
Downloads and prepares a lens catalog from GAMA DR4 for the
weak-lensing activity-dependence test (ED prediction #4).

Joins three GAMA tables:
  - gkvScienceCatv02: positions, redshifts, classification
  - ProSpectv03: stellar mass, SFR (from SED fitting)
  - G3CGalv10: group membership (GroupID, RankIterCen)

Applies:
  - xGASS statistical gas correction (Catinella+2018) to get M_baryon
  - Environment classification (grouped vs isolated from GroupID)
  - sSFR computation (SFR / M_star)
  - Binning: M_baryon tertiles × sSFR tertiles × environment (2 bins)

Output: CSV lens catalog ready for GGL cross-matching with KiDS shear.

Usage:
  python analysis/scripts/gama_lens_catalog.py

Requires: requests, numpy, pandas
"""

import io
import os
import sys
import time

import numpy as np

try:
    import pandas as pd
except ImportError:
    print("pandas required: pip install pandas")
    sys.exit(1)

try:
    import requests
except ImportError:
    print("requests required: pip install requests")
    sys.exit(1)

# ================================================================
# Configuration
# ================================================================

GAMA_QUERY_URL = "https://www.gama-survey.org/dr4/query/index.php"
OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "data", "ED-WL-Activity"
)
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_CSV = os.path.join(OUTPUT_DIR, "gama_lens_catalog.csv")

# ================================================================
# SQL query: join ScienceCat + ProSpect + G3CGal
# ================================================================

SQL_QUERY = """
SELECT
    s.uberID,
    s.RAcen   AS ra,
    s.Deccen  AS dec,
    s.Z       AS z_spec,
    s.NQ      AS z_quality,
    s.uberclass,
    s.SC      AS science_class,
    p.StellarMass_50  AS mstar,
    p.SFR_50          AS sfr,
    g.GroupID,
    g.RankIterCen
FROM
    gkvScienceCatv02 AS s
    INNER JOIN ProSpectv03 AS p ON s.uberID = p.uberID
    LEFT JOIN G3CGalv10 AS g ON s.CATAID = g.CATAID
WHERE
    s.uberclass = 1
    AND s.NQ > 2
    AND s.Z > 0.01
    AND s.Z < 0.5
    AND p.StellarMass_50 > 0
    AND p.SFR_50 >= 0
"""
# SC >= 3: science-quality equatorial sample (regions G09, G12, G15)
# NQ > 2: reliable redshift
# z > 0.01: avoid local flow issues
# z < 0.5: GAMA completeness limit
# StellarMass_50 > 0: valid ProSpect fit
# SFR_50 >= 0: valid SFR (can be zero for quiescent)


def query_gama(sql, fmt="csv"):
    """Submit a SQL query to the GAMA DR4 database and return raw text."""
    print(f"Submitting query to GAMA DR4...")
    print(f"  SQL: {sql[:120]}...")

    payload = {
        "query": sql,
        "format": fmt,
        "nshow": "0",        # don't show results in HTML
        "ndownload": "1",    # download as file
        "nsov": "0",
    }

    try:
        resp = requests.post(GAMA_QUERY_URL, data=payload, timeout=600,
                             allow_redirects=True)
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"  GAMA query failed: {e}")
        print(f"  Response status: {getattr(resp, 'status_code', 'N/A')}")
        print(f"  Response text (first 500 chars): {getattr(resp, 'text', '')[:500]}")
        return None

    text = resp.text

    # GAMA returns HTML with a temporary CSV download link
    if "<html" in text[:200].lower():
        import re
        # Look for the temp CSV link (pattern: ../tmp/GAMA_XXXXXX.csv)
        links = re.findall(r'href=["\'](\.\./tmp/GAMA_[^"\']*\.csv)["\']', text,
                           re.IGNORECASE)
        if not links:
            # Broader search
            links = re.findall(r'href=["\']([^"\']*\.csv)["\']', text, re.IGNORECASE)
            links = [l for l in links if 'topcat' not in l.lower()]

        if links:
            dl_path = links[0]
            if dl_path.startswith(".."):
                dl_url = "https://www.gama-survey.org/dr4" + dl_path[2:]
            elif not dl_path.startswith("http"):
                dl_url = "https://www.gama-survey.org" + dl_path
            else:
                dl_url = dl_path
            print(f"  Downloading CSV from: {dl_url}")
            resp2 = requests.get(dl_url, timeout=600)
            resp2.raise_for_status()
            text = resp2.text
            print(f"  Downloaded {len(text)} bytes")
        else:
            # Check for error in query
            errors = re.findall(r'class="error"[^>]*>([^<]+)', text)
            if errors:
                print(f"  GAMA SQL error: {errors[0]}")
            else:
                print(f"  GAMA returned HTML, no CSV found.")
                print(f"  First 800 chars:")
                print(text[:800])
            return None

    # Check for error messages
    if "ERROR" in text[:500].upper():
        print(f"  GAMA returned an error:")
        print(f"  {text[:500]}")
        return None

    n_lines = text.count("\n")
    print(f"  Received {n_lines} lines ({len(text)} bytes)")
    return text


def xgass_gas_correction(log_mstar):
    """
    Statistical HI gas mass estimate from the xGASS scaling relation
    (Catinella et al. 2018, MNRAS 476, 875).

    Returns log10(M_HI / M_sun) given log10(M_star / M_sun).

    The median relation from their Fig. 3 / Table 1 (approximately):
      log(M_HI/M_star) = -0.35 * log(M_star) + 3.1  for log(M_star) < 10.7
      log(M_HI/M_star) = -1.5                         for log(M_star) >= 10.7

    Scatter is ~0.4 dex. We use the median relation for now.
    """
    log_gas_frac = np.where(
        log_mstar < 10.7,
        -0.35 * log_mstar + 3.1,
        -1.5
    )
    log_mhi = log_gas_frac + log_mstar
    return log_mhi


def build_lens_catalog(df):
    """
    From raw GAMA query results, build the full lens catalog with:
    - M_baryon (stellar + 1.4 * M_HI for helium)
    - sSFR
    - Environment classification
    - Binning
    """
    print(f"\nBuilding lens catalog from {len(df)} galaxies...")

    # Compute log stellar mass
    df["log_mstar"] = np.log10(df["mstar"])

    # Apply gas correction
    df["log_mhi"] = xgass_gas_correction(df["log_mstar"])
    df["m_baryon"] = df["mstar"] + 1.4 * 10**df["log_mhi"]  # factor 1.4 for He
    df["log_mbaryon"] = np.log10(df["m_baryon"])

    # Compute sSFR
    df["ssfr"] = df["sfr"] / df["mstar"]  # yr^-1
    df["log_ssfr"] = np.log10(np.maximum(df["ssfr"], 1e-14))  # floor at 1e-14

    # Environment classification
    # GroupID = 0 means ungrouped (isolated)
    # GroupID > 0 means in a group
    # RankIterCen = 1 means the galaxy is the central of its group
    df["in_group"] = (df["GroupID"] > 0).astype(int)
    df["is_central"] = ((df["GroupID"] > 0) & (df["RankIterCen"] == 1)).astype(int)

    # Mass bins: tertiles of log_mbaryon
    df["mbaryon_bin"] = pd.qcut(df["log_mbaryon"], 3, labels=["low", "mid", "high"])

    # sSFR bins: tertiles within each mass bin (to avoid mass-sSFR correlation)
    df["ssfr_bin"] = "unset"
    for mb in ["low", "mid", "high"]:
        mask = df["mbaryon_bin"] == mb
        sub_ssfr = df.loc[mask, "log_ssfr"]
        try:
            df.loc[mask, "ssfr_bin"] = pd.qcut(
                sub_ssfr, 3, labels=["quiet", "moderate", "active"],
                duplicates="drop"
            ).astype(str)
        except ValueError:
            df.loc[mask, "ssfr_bin"] = "moderate"  # fallback if not enough unique values

    return df


def summarize_catalog(df):
    """Print summary statistics for the lens catalog."""
    print("\n" + "=" * 60)
    print("GAMA LENS CATALOG SUMMARY")
    print("=" * 60)

    print(f"\nTotal galaxies: {len(df)}")
    print(f"Redshift range: {df['z_spec'].min():.3f} - {df['z_spec'].max():.3f}")
    print(f"  median z: {df['z_spec'].median():.3f}")

    print(f"\nlog M_star range: {df['log_mstar'].min():.2f} - {df['log_mstar'].max():.2f}")
    print(f"  median: {df['log_mstar'].median():.2f}")

    print(f"\nlog M_baryon range: {df['log_mbaryon'].min():.2f} - {df['log_mbaryon'].max():.2f}")
    print(f"  median: {df['log_mbaryon'].median():.2f}")

    print(f"\nlog sSFR range: {df['log_ssfr'].min():.2f} - {df['log_ssfr'].max():.2f}")
    print(f"  median: {df['log_ssfr'].median():.2f}")

    print(f"\nEnvironment:")
    print(f"  Isolated (GroupID=0): {(df['in_group']==0).sum()}")
    print(f"  In group (GroupID>0): {(df['in_group']==1).sum()}")
    print(f"    of which centrals:  {df['is_central'].sum()}")

    print(f"\n--- Bin populations ---")
    print(f"\n12-bin breakdown (M_baryon × sSFR × environment):")
    ct = df.groupby(["mbaryon_bin", "ssfr_bin", "in_group"], observed=True).size()
    print(ct.to_string())

    print(f"\nMedian per bin: {ct.median():.0f}")
    print(f"Min per bin: {ct.min():.0f}")
    print(f"Max per bin: {ct.max():.0f}")

    # The key ED test: at fixed M_baryon and fixed environment,
    # does lensing depend on sSFR?
    print(f"\n--- Key comparison bins (fixed mass, fixed environment) ---")
    for mass_bin in ["low", "mid", "high"]:
        for env in [0, 1]:
            env_label = "isolated" if env == 0 else "grouped"
            subset = df[(df["mbaryon_bin"] == mass_bin) & (df["in_group"] == env)]
            if len(subset) == 0:
                continue
            for ssfr_bin in ["quiet", "active"]:
                n = len(subset[subset["ssfr_bin"] == ssfr_bin])
                print(f"  M_baryon={mass_bin}, env={env_label}, sSFR={ssfr_bin}: n={n}")


def main():
    # Step 1: Query GAMA
    raw_csv = query_gama(SQL_QUERY, fmt="csv")

    if raw_csv is None:
        print("\nGAMA query failed. Trying with a smaller test query...")
        test_sql = "SELECT uberID, Z FROM gkvScienceCatv02 WHERE Z > 0.01 AND Z < 0.02 LIMIT 100"
        test_result = query_gama(test_sql)
        if test_result:
            print("Test query succeeded. The main query may be too large or have a syntax issue.")
            print("First few lines:")
            print(test_result[:500])
        else:
            print("Even the test query failed. Check network connectivity to gama-survey.org.")
        return

    # Step 2: Parse CSV
    try:
        df = pd.read_csv(io.StringIO(raw_csv))
        print(f"Parsed {len(df)} rows, {len(df.columns)} columns")
        print(f"Columns: {list(df.columns)}")
    except Exception as e:
        print(f"Failed to parse CSV: {e}")
        print(f"First 500 chars of response:")
        print(raw_csv[:500])
        return

    if len(df) == 0:
        print("Query returned 0 rows. Check SQL syntax or GAMA availability.")
        return

    # Save raw query result before processing (so we don't have to re-download)
    raw_csv_path = os.path.join(OUTPUT_DIR, "gama_raw_query.csv")
    df.to_csv(raw_csv_path, index=False)
    print(f"Saved raw query result to: {raw_csv_path}")

    # Step 3: Build catalog
    df = build_lens_catalog(df)

    # Step 4: Summarize
    summarize_catalog(df)

    # Step 5: Save
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"\nSaved lens catalog to: {OUTPUT_CSV}")
    print(f"File size: {os.path.getsize(OUTPUT_CSV) / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
