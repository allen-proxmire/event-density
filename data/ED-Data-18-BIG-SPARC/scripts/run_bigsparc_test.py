"""
ED-Data-18: BIG-SPARC Activity Test.

STATUS: AWAITING DATA RELEASE.

This script processes the BIG-SPARC catalog when it becomes available.
Place the catalog file(s) in data/ED-Data-18-BIG-SPARC/raw/ and re-run.

Expected file formats (based on the SPARC format and BIG-SPARC announcement):
  - A galaxy property table with columns including:
      Galaxy name, RA, DEC, Distance, Inclination, Vflat, M_b,
      WISE W1/W2/W3 fluxes or magnitudes, morphological type, quality flag

The script will:
  1. Load the catalog
  2. Compute SFR from WISE W3 (12 um) using Cluver+ 2017 calibration
  3. Fit the BTFR
  4. Test the ED-Phys-05 activity-dependence prediction
  5. Generate publication-quality plots
"""
import json, os, sys, warnings, glob
import numpy as np
warnings.filterwarnings('ignore')

BASE = 'data/ED-Data-18-BIG-SPARC'
RAW = os.path.join(BASE, 'raw')
RES = os.path.join(BASE, 'results')
FIG = os.path.join(BASE, 'figures')

# Check for data
catalog_files = glob.glob(os.path.join(RAW, '*.fits')) + \
                glob.glob(os.path.join(RAW, '*.csv')) + \
                glob.glob(os.path.join(RAW, '*.dat')) + \
                glob.glob(os.path.join(RAW, '*.txt')) + \
                glob.glob(os.path.join(RAW, '*.mrt'))

if not catalog_files:
    print("=" * 85)
    print("  ED-Data-18: BIG-SPARC Activity Test")
    print("=" * 85)
    print()
    print("  STATUS: AWAITING DATA RELEASE")
    print()
    print("  BIG-SPARC (Haubner, Lelli et al. 2024) has not been publicly released.")
    print("  When it is released:")
    print(f"    1. Download the catalog to: {os.path.abspath(RAW)}/")
    print("    2. Re-run this script.")
    print()
    print("  Check for updates: https://arxiv.org/abs/2411.13329")
    print()
    print("  Current best result (ED-Data-17, n=25):")
    print("    Spearman rho(Delta, SFR) = +0.324, p = 0.114")
    print("    Tertile (high > low): p = 0.030 (significant)")
    print("    Verdict: SUGGESTIVE")
    print()

    with open(os.path.join(RES, 'final_summary.json'), 'w') as f:
        json.dump({
            'experiment': 'ED-Data-18: BIG-SPARC',
            'status': 'AWAITING DATA RELEASE',
            'bigsparc_paper': 'arXiv:2411.13329',
            'best_current_result': {
                'module': 'ED-Data-17', 'n': 25,
                'rho_sfr': 0.324, 'p_sfr': 0.114,
                'tertile_p': 0.030, 'verdict': 'SUGGESTIVE',
            },
        }, f, indent=2)
    sys.exit(0)

# ═══ IF DATA EXISTS: Full pipeline ═══
print(f"  Found catalog files: {catalog_files}")
print("  Attempting to load BIG-SPARC...")

# The actual loading code would go here, adapted to whatever format
# Lelli et al. choose for the release. The SPARC format is space-delimited
# fixed-width with a header block, so we expect similar.

# Placeholder for when the data arrives:
# import pandas as pd
# from scipy import stats
# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt
#
# df = pd.read_csv(catalog_files[0], sep=r'\s+', comment='#', header=None)
# ... extract Vflat, Mb, W3 flux ...
# ... compute SFR from W3 ...
# ... fit BTFR, compute Delta ...
# ... test correlations ...
# ... generate plots ...

print("  NOTE: Parser not yet adapted to BIG-SPARC format.")
print("  When the data format is known, update this script's loader section.")
