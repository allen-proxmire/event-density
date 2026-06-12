"""Robustness program, axis 2 - Delta vs observable (the decisive test).

Fix size S=64 (midpoint of the size-stable region), ensemble N=400, KSG
estimator. Measure Delta under four genuinely different readouts of the final
state:

  (A) summed_rho    - global scalar (baseline)
  (B) half_vectors  - per-node rho vectors (high-dim, vector MI)
  (C) subregion_rho - rho over a contiguous 4-node window (local scalar)
  (D) gradient_rho  - discrete gradient of rho (derivative, vector)

Question: does Delta stay ~1.0 +/- 0.1 bit across observables (-> intrinsic to
ED), or does it move (-> the ~1 bit was an artifact of summed_rho)? For each
observable Delta is computed at k=3,5,7 to confirm KSG-knob stability. M2 must
stay ~0 for all observables.
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from size_sweep import run_one  # noqa: E402  (reuses the parameterized substrate)
from analysis.observables import OBSERVABLES  # noqa: E402
from analysis.delta import compute_all  # noqa: E402

S = 64
N = 400
KS = [3, 5, 7]


def build_ensemble(S, N):
    """Run N independent substrates; return per-run final (sv, A, B) triples."""
    runs = []
    ms = 40 * S
    for k in range(N):
        sv, A, B, steps, term = run_one(S, 1000 + k, 5000 + k, ms)
        runs.append((sv, A, B))
    return runs


def dataset_for(observable_fn, kind, runs):
    """Stack per-run features into A, B, A_left, A_right ensemble arrays."""
    A, B, AL, AR = [], [], [], []
    for sv, a, b in runs:
        h = len(a) // 2
        A.append(observable_fn(sv, a))
        B.append(observable_fn(sv, b))
        AL.append(observable_fn(sv, a[:h]))
        AR.append(observable_fn(sv, a[h:]))
    stack = (lambda L: np.array(L)) if kind == "scalar" else (lambda L: np.vstack(L))
    return {"A": stack(A), "B": stack(B), "A_left": stack(AL), "A_right": stack(AR)}


def main():
    print("=" * 76)
    print(f"OBSERVABLE SWEEP - Delta vs observable   (S={S}, N={N}, KSG)")
    print("=" * 76)

    runs = build_ensemble(S, N)
    rows = []
    print(f"\n  {'observable':>14} {'kind':>7} {'k':>3} "
          f"{'M1':>8} {'M2':>8} {'M3':>8} {'Delta':>8}")
    print("  " + "-" * 64)

    for name, (fn, kind) in OBSERVABLES.items():
        ds = dataset_for(fn, kind, runs)
        deltas_k = []
        for k in KS:
            d = compute_all(ds, estimator="ksg", k=k)
            deltas_k.append(d["delta_bits"])
            print(f"  {name:>14} {kind:>7} {k:>3} "
                  f"{d['M1_bits']:>+8.3f} {d['M2_bits']:>+8.3f} "
                  f"{d['M3_bits']:>+8.3f} {d['delta_bits']:>+8.3f}")
        k_spread = max(deltas_k) - min(deltas_k)
        # Use k=5 as the reported value.
        d5 = compute_all(ds, estimator="ksg", k=5)
        rows.append({"observable": name, "kind": kind,
                     "delta_k5": d5["delta_bits"], "M2_k5": d5["M2_bits"],
                     "M3_k5": d5["M3_bits"], "k_spread": k_spread,
                     "delta_by_k": dict(zip(KS, deltas_k))})
        print(f"  {'':>14} {'':>7} {'':>3} -> k-spread = {k_spread:.3f} bits")
        print("  " + "-" * 64)

    # Cross-observable assessment (using k=5).
    d5s = [r["delta_k5"] for r in rows]
    obs_spread = max(d5s) - min(d5s)
    m2_all_zero = all(abs(r["M2_k5"]) < 0.10 for r in rows)

    print(f"\n  Delta (k=5) by observable:")
    for r in rows:
        print(f"    {r['observable']:>14}: {r['delta_k5']:>+7.3f} bits")
    print(f"\n  cross-observable Delta range : "
          f"[{min(d5s):+.3f}, {max(d5s):+.3f}]  spread = {obs_spread:.3f} bits")
    print(f"  M2 ~ 0 for all observables   : {m2_all_zero}")

    # Verdict.
    if obs_spread <= 0.30 and all(abs(d - 1.0) <= 0.3 for d in d5s):
        verdict = "STABLE near ~1 bit across observables -> INTRINSIC candidate"
    elif obs_spread <= 0.30:
        verdict = f"STABLE across observables (~{np.mean(d5s):.2f} bits), but not ~1.0"
    else:
        verdict = "VARIES across observables -> Delta is observable-DEPENDENT"
    print(f"\n  VERDICT: {verdict}")

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sweep_output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "observable_sweep.json"), "w", encoding="utf-8") as fh:
        json.dump({"S": S, "N": N, "ks": KS, "rows": rows,
                   "obs_spread": float(obs_spread),
                   "M2_all_zero": bool(m2_all_zero), "verdict": verdict},
                  fh, indent=2)

    print("\n" + "=" * 76)
    print(f"OBSERVABLE SWEEP COMPLETE — M2~0: {m2_all_zero}")
    print("=" * 76)
    return m2_all_zero


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
