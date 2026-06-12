"""Delta driver - the determinability-boundary bits measurement.

Generates an ensemble of independent MWE runs, extracts per-stratum summaries,
and computes:

  M1 = within-stratum predictability  = MI(A_left ; A_right)   [bits]
  M2 = across-boundary predictability = MI(A ; B)              [bits]
  M3 = shuffle control                = MI(A ; shuffled B)     [bits]
  Delta = M1 - M2                                              [bits]

Sanity checks:
  - M2 ~ M3        (no across-boundary information beyond the estimator floor)
  - M1 > M2        (information propagates within a stratum, not across)
  - Delta stable across ensemble sizes.
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mwe_demo import run_mwe, A_NODES, B_NODES  # noqa: E402
from analysis.delta import compute_M1, compute_M2, compute_M3, compute_delta  # noqa: E402

# Split stratum A into two reach-connected halves for the within-stratum measure.
A_LEFT = A_NODES[: len(A_NODES) // 2]    # 0..3
A_RIGHT = A_NODES[len(A_NODES) // 2:]    # 4..7


def build_dataset(N, base_a=1000, base_b=5000):
    """Ensemble of N independent runs; per-run summaries = summed final rho."""
    A, B, AL, AR = [], [], [], []
    for k in range(N):
        sv = run_mwe(seed_a=base_a + k, seed_b=base_b + k, record=False)["sv"]
        A.append(sum(sv[n].rho for n in A_NODES))
        B.append(sum(sv[n].rho for n in B_NODES))
        AL.append(sum(sv[n].rho for n in A_LEFT))
        AR.append(sum(sv[n].rho for n in A_RIGHT))
    return {"A": np.array(A), "B": np.array(B),
            "A_left": np.array(AL), "A_right": np.array(AR)}


def measure(N, bins=2):
    ds = build_dataset(N)
    M1 = compute_M1(ds, bins=bins)
    M2 = compute_M2(ds, bins=bins)
    M3 = compute_M3(ds, bins=bins)
    d = compute_delta(M1, M2, M3)
    return d


def main():
    print("=" * 68)
    print("DELTA - determinability-boundary bits measurement")
    print("=" * 68)

    N = 200
    d = measure(N)
    print(f"\n  ensemble N = {N}, bins = 2, Miller-Madow corrected, units = bits")
    print(f"  M1  within-stratum   MI(A_left; A_right) : {d['M1_bits']:+.5f} bits")
    print(f"  M2  across-boundary  MI(A; B)            : {d['M2_bits']:+.5f} bits")
    print(f"  M3  shuffle control  MI(A; shuffled B)   : {d['M3_bits']:+.5f} bits")
    print(f"  -------------------------------------------------------------")
    print(f"  Delta = M1 - M2                          : {d['delta_bits']:+.5f} bits")
    print(f"  residual M2 - M3 (should be ~0)          : {d['M2_minus_M3_bits']:+.5f} bits")

    # Stability across ensemble sizes.
    print("\n  Delta stability across ensemble sizes:")
    deltas = {}
    for n in (100, 200, 400):
        dn = measure(n)
        deltas[n] = dn["delta_bits"]
        print(f"    N={n:>4}:  M1={dn['M1_bits']:+.4f}  M2={dn['M2_bits']:+.4f}  "
              f"Delta={dn['delta_bits']:+.4f} bits")

    # Acceptance checks.
    m2_near_m3 = abs(d["M2_minus_M3_bits"]) < 0.02
    m1_gt_m2 = d["M1_bits"] > d["M2_bits"]
    delta_positive = d["delta_bits"] > 0.0
    spread = max(deltas.values()) - min(deltas.values())
    delta_stable = spread < 0.10

    print("\nChecks")
    print(f"  M2 ~ M3 (across-boundary independence) : {m2_near_m3}")
    print(f"  M1 > M2 (within-stratum predictability): {m1_gt_m2}")
    print(f"  Delta > 0                              : {delta_positive}")
    print(f"  Delta stable across N (spread {spread:.4f}<0.10): {delta_stable}")

    passed = m2_near_m3 and m1_gt_m2 and delta_positive and delta_stable
    print("\n" + "=" * 68)
    print(f"DELTA MEASUREMENT: {'PASS' if passed else 'FAIL'}")
    print("=" * 68)
    return passed


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
