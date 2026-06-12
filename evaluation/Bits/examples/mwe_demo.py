"""Build Step 8 - the Minimal Working Example (MWE).

The first full, measurement-shaped ED substrate run:
  - two isomorphic 8-node chain clusters A = {0..7}, B = {8..15};
  - a single DECOUPLED bridge (7, 8) -> two reach strata, one determinability
    boundary;
  - INDEPENDENT random initial conditions per cluster (different seeds), so B's
    state is genuinely independent of A's;
  - full recording (rho, orientation, commits) and .npz + JSON export.

Exposes run_mwe() so the test suite (Build Step 9) can regenerate the run
deterministically and perturb one stratum's seed for the factorization gate.
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from simulator import (  # noqa: E402
    ParticipationGraph,
    NodeState,
    StateVector,
    SigmaCoeffs,
    assign_stratum_ids,
    boundary_map,
    detect_decoupled_edges,
    step,
    HistoryRecorder,
)

CLUSTER_SIZE = 8
A_NODES = list(range(0, CLUSTER_SIZE))                  # 0..7
B_NODES = list(range(CLUSTER_SIZE, 2 * CLUSTER_SIZE))  # 8..15
BRIDGE = (7, 8)
SEED_A = 1
SEED_B = 2
MAX_STEPS = 200
ORIENT_DIM = 2

MWE_COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5,
                         extinction_threshold=-2.0)


def build_graph():
    """Two isomorphic 8-node chains joined by a decoupled bridge."""
    g = ParticipationGraph()
    for chain in (A_NODES, B_NODES):
        for i in range(len(chain) - 1):
            g.add_edge(chain[i], chain[i + 1], bandwidth=0.5)
    g.add_edge(BRIDGE[0], BRIDGE[1], bandwidth=0.5, decoupled=True)
    return g


def init_state(g, seed_a=SEED_A, seed_b=SEED_B):
    """Independent random rho + orientation per cluster (different seeds)."""
    sv = StateVector()
    rng_a = np.random.default_rng(seed_a)
    rng_b = np.random.default_rng(seed_b)
    for n in A_NODES:
        sv[n] = NodeState(rho=float(rng_a.uniform(0.0, 0.5)),
                          orientation=rng_a.normal(size=ORIENT_DIM))
    for n in B_NODES:
        sv[n] = NodeState(rho=float(rng_b.uniform(0.0, 0.5)),
                          orientation=rng_b.normal(size=ORIENT_DIM))
    sv[A_NODES[0]].active = True   # one front per cluster, corresponding ends
    sv[B_NODES[0]].active = True
    return sv


def run_mwe(seed_a=SEED_A, seed_b=SEED_B, record=True, max_steps=MAX_STEPS):
    """Build, seed, and evolve the MWE to a fixed point (or max_steps).
    Returns a dict with g, sv, strata, rec (or None), steps_run, total_commits."""
    g = build_graph()
    sv = init_state(g, seed_a=seed_a, seed_b=seed_b)
    strata = assign_stratum_ids(sv, g)
    coeffs = MWE_COEFFS

    rec = None
    if record:
        rec = HistoryRecorder(
            g, strata=strata,
            params={"kc": coeffs.kc, "ks": coeffs.ks, "kg": coeffs.kg,
                    "rho_star": coeffs.rho_star,
                    "extinction_threshold": coeffs.extinction_threshold,
                    "seed_A": seed_a, "seed_B": seed_b, "max_steps": max_steps},
            seed=seed_a,
        )
        rec.snapshot(0, sv)

    total_commits = 0
    steps_run = 0
    for t in range(1, max_steps + 1):
        c = step(sv, g, coeffs, strata=strata, recorder=rec, t=t)
        total_commits += c
        steps_run = t
        if c == 0:
            break

    return {"g": g, "sv": sv, "strata": strata, "rec": rec,
            "steps_run": steps_run, "total_commits": total_commits,
            "coeffs": coeffs}


def main():
    print("=" * 64)
    print("BUILD STEP 8 - Minimal Working Example (16-node, two clusters)")
    print("=" * 64)

    res = run_mwe()
    g, sv, strata, rec = res["g"], res["sv"], res["strata"], res["rec"]
    steps_run, total_commits = res["steps_run"], res["total_commits"]

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mwe_output")
    os.makedirs(out_dir, exist_ok=True)
    prefix = os.path.join(out_dir, "mwe_run")
    npz_path, _ = rec.export(prefix)
    json_path = os.path.join(out_dir, "mwe_metadata.json")
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(rec.metadata(), fh, indent=2, sort_keys=True)

    rho_A = [sv[n].rho for n in A_NODES]
    rho_B = [sv[n].rho for n in B_NODES]

    print(f"\n  strata (A->0, B->1)      : two strata, "
          f"|A|={sum(1 for v in strata.values() if v == 0)}, "
          f"|B|={sum(1 for v in strata.values() if v == 1)}")
    print(f"  decoupled bridge          : {detect_decoupled_edges(g)}")
    print(f"  boundary_map              : {boundary_map(g)}")
    print(f"  steps run                 : {steps_run}  (max {MAX_STEPS})")
    print(f"  total commits             : {total_commits}")
    print(f"  terminated naturally      : {steps_run < MAX_STEPS}")
    print(f"  final rho A {A_NODES}: {[round(x, 2) for x in rho_A]}")
    print(f"  final rho B {B_NODES}: {[round(x, 2) for x in rho_B]}")
    print(f"  exported                  : {os.path.basename(npz_path)}, "
          f"{os.path.basename(json_path)}")

    two_strata = set(strata.values()) == {0, 1}
    bridge_ok = detect_decoupled_edges(g) == [(7, 8)]
    independent_evolution = rho_A != rho_B
    terminated = (steps_run < MAX_STEPS) or (total_commits > 0)

    loaded = np.load(npz_path)
    rho_hist = rec.rho_history()
    roundtrip = (np.allclose(loaded["rho_history"], rho_hist)
                 and loaded["rho_history"].shape == rho_hist.shape)

    with open(json_path, encoding="utf-8") as fh:
        meta = json.load(fh)
    meta_ok = (meta["decoupled_edges"] == [[7, 8]]
               and set(int(v) for v in meta["strata"].values()) == {0, 1})

    print("\nChecks")
    print(f"  two strata                : {two_strata}")
    print(f"  decoupled bridge detected : {bridge_ok}")
    print(f"  independent evolution     : {independent_evolution}")
    print(f"  terminated cleanly        : {terminated}")
    print(f"  npz round-trip            : {roundtrip}")
    print(f"  json metadata valid       : {meta_ok}")

    passed = (two_strata and bridge_ok and independent_evolution
              and terminated and roundtrip and meta_ok)
    print("\n" + "=" * 64)
    print(f"BUILD STEP 8: {'PASS' if passed else 'FAIL'}")
    print("=" * 64)
    return passed


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
