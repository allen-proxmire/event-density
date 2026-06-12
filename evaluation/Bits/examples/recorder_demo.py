"""Build Step 7 demo - HistoryRecorder.

Runs a few steps on the two-cluster graph with one front per stratum, records
per-step rho/orientation + commit log, exports .npz + JSON, and reloads to
verify the round-trip. Also checks that recording does not perturb the run
(identical final state with and without a recorder).
"""
import json
import os
import sys
import tempfile

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from simulator import (  # noqa: E402
    ParticipationGraph,
    NodeState,
    StateVector,
    SigmaCoeffs,
    compute_strata,
    assign_stratum_ids,
    step,
    HistoryRecorder,
)

STEPS = 5


def build_two_clusters():
    g = ParticipationGraph()
    g.add_edge(0, 1, bandwidth=0.5)
    g.add_edge(1, 2, bandwidth=0.5)
    g.add_edge(3, 4, bandwidth=0.5)
    g.add_edge(4, 5, bandwidth=0.5)
    g.add_edge(2, 3, bandwidth=0.5, decoupled=True)
    return g


def fresh_state(g, seeds):
    sv = StateVector()
    for n in sorted(g.nodes()):
        sv[n] = NodeState(rho=0.0, orientation=np.array([0.0, 0.0]))
    for s in seeds:
        sv[s].active = True
    return sv


def run(record=True, prefix=None):
    g = build_two_clusters()
    sv = fresh_state(g, seeds=[0, 3])
    strata = assign_stratum_ids(sv, g)
    coeffs = SigmaCoeffs()
    rec = None
    if record:
        rec = HistoryRecorder(g, strata=strata,
                              params={"kc": coeffs.kc, "ks": coeffs.ks,
                                      "kg": coeffs.kg, "rho_star": coeffs.rho_star},
                              seed=0)
        rec.snapshot(0, sv)  # initial state
    for t in range(1, STEPS + 1):
        step(sv, g, coeffs, strata=strata, recorder=rec, t=t)
    final_rho = [sv[n].rho for n in sorted(g.nodes())]
    paths = rec.export(prefix) if (record and prefix) else (None, None)
    return final_rho, rec, paths


def main():
    print("=" * 64)
    print("BUILD STEP 7 - HistoryRecorder")
    print("=" * 64)

    tmp = tempfile.mkdtemp(prefix="ed_rec_")
    prefix = os.path.join(tmp, "run")

    # Record a run.
    final_rho, rec, (npz_path, json_path) = run(record=True, prefix=prefix)

    rho_hist = rec.rho_history()
    orient_hist = rec.orientation_history()
    commits = rec.committed_edges()
    meta = rec.metadata()

    print(f"\n  rho_history shape         : {rho_hist.shape}   (T x |V|)")
    print(f"  orientation_history shape : {orient_hist.shape}   (T x |V| x k)")
    print(f"  committed_edges shape     : {commits.shape}   (C x 3: t,u,v)")
    print(f"  final rho                 : {final_rho}")
    print(f"  metadata.strata           : {meta['strata']}")
    print(f"  metadata.decoupled_edges  : {meta['decoupled_edges']}")
    print(f"  metadata.boundary_nodes   : {meta['boundary_nodes']}")
    print(f"  exported npz              : {os.path.basename(npz_path)}")
    print(f"  exported json             : {os.path.basename(json_path)}")

    # Reload round-trip.
    loaded = np.load(npz_path)
    rho_roundtrip = np.allclose(loaded["rho_history"], rho_hist)
    with open(json_path, encoding="utf-8") as fh:
        meta_loaded = json.load(fh)
    meta_roundtrip = (meta_loaded["strata"] == {str(k): v for k, v in meta["strata"].items()}
                      and meta_loaded["decoupled_edges"] == meta["decoupled_edges"])

    # No-perturbation: run again WITHOUT a recorder; final state must match.
    final_rho_norec, _, _ = run(record=False, prefix=None)
    no_perturb = (final_rho == final_rho_norec)

    # Append-only / monotonic across recorded snapshots.
    monotone = bool(np.all(np.diff(rho_hist, axis=0) >= -1e-12))

    # Metadata correctness. (strata uses string keys: JSON-compatible.)
    meta_ok = (meta["strata"] == {"0": 0, "1": 0, "2": 0, "3": 1, "4": 1, "5": 1}
               and meta["decoupled_edges"] == [[2, 3]]
               and meta["boundary_nodes"] == [2, 3])

    print("\nChecks")
    print(f"  npz round-trip (rho)         : {rho_roundtrip}")
    print(f"  json round-trip (metadata)   : {meta_roundtrip}")
    print(f"  recording does not perturb   : {no_perturb}")
    print(f"  recorded rho monotone        : {monotone}")
    print(f"  metadata correct             : {meta_ok}")

    passed = (rho_roundtrip and meta_roundtrip and no_perturb
              and monotone and meta_ok)
    print("\n" + "=" * 64)
    print(f"BUILD STEP 7: {'PASS' if passed else 'FAIL'}")
    print("=" * 64)
    return passed


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
