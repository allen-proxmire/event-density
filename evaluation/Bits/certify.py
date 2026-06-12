"""Build Step 10 - the certification run.

Executes all four correctness gates together on the MWE substrate, consolidates
the results, and writes three artifacts:
  - certification_results.json  (machine-readable gate summary)
  - certification_log.txt       (pytest output)
  - certification_snapshot.md   (human-readable summary)

Exit 0 iff every gate passes and the simulator is CERTIFIED.
"""
import json
import os
import subprocess
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.join(_HERE, "examples"))

from mwe_demo import run_mwe, A_NODES, B_NODES, BRIDGE, MAX_STEPS  # noqa: E402
from analysis.entropy import mutual_information                    # noqa: E402

OUT_DIR = os.path.join(_HERE, "certification_output")


def run_pytest():
    """Run the full suite; return (passed_count, failed_count, raw_output)."""
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/", "-v", "--no-header"],
        cwd=_HERE, capture_output=True, text=True,
    )
    out = proc.stdout + ("\n" + proc.stderr if proc.stderr else "")
    passed = out.count(" PASSED")
    failed = out.count(" FAILED")
    return passed, failed, out, proc.returncode


def factorization_evidence():
    """Structural exactness + informational MI on a fresh ensemble."""
    base = run_mwe(seed_a=1, seed_b=2)
    pert_B = run_mwe(seed_a=1, seed_b=999)     # perturb B
    pert_A = run_mwe(seed_a=777, seed_b=2)     # perturb A

    def commits_in(rec, nodes):
        s = set(nodes)
        return [tuple(int(x) for x in row)
                for row in rec.committed_edges() if int(row[1]) in s]

    def final_rho(res, nodes):
        return [res["sv"][n].rho for n in nodes]

    A_exact = (commits_in(base["rec"], A_NODES) == commits_in(pert_B["rec"], A_NODES)
               and final_rho(base, A_NODES) == final_rho(pert_B, A_NODES))
    B_exact = (commits_in(base["rec"], B_NODES) == commits_in(pert_A["rec"], B_NODES)
               and final_rho(base, B_NODES) == final_rho(pert_A, B_NODES))

    N = 200
    a_sum, b_sum = [], []
    for k in range(N):
        r = run_mwe(seed_a=1000 + k, seed_b=5000 + k, record=False)
        a_sum.append(sum(r["sv"][n].rho for n in A_NODES))
        b_sum.append(sum(r["sv"][n].rho for n in B_NODES))
    a = np.array(a_sum)
    b = np.array(b_sum)
    rng = np.random.default_rng(0)
    b_shuf = b.copy()
    rng.shuffle(b_shuf)
    mi = float(mutual_information(a, b, bins=2))
    mi_shuf = float(mutual_information(a, b_shuf, bins=2))

    return {
        "A_independent_of_B_exact": bool(A_exact),
        "B_independent_of_A_exact": bool(B_exact),
        "mi_AB_nats": mi,
        "mi_A_shuffledB_nats": mi_shuf,
        "mi_tolerance_nats": 5e-3,
        "ensemble_N": N,
    }


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    # 1) Canonical MWE run.
    mwe = run_mwe(seed_a=1, seed_b=2)
    rho_A = [round(mwe["sv"][n].rho, 4) for n in A_NODES]
    rho_B = [round(mwe["sv"][n].rho, 4) for n in B_NODES]
    rho_hist = mwe["rec"].rho_history()
    orient_hist = mwe["rec"].orientation_history()

    # Gate 1: monotonicity.
    g1 = bool(np.all(np.diff(rho_hist, axis=0) >= -1e-12))

    # Gate 2: acyclicity.
    sigs = set()
    g2 = True
    for t in range(rho_hist.shape[0]):
        sig = (tuple(np.round(rho_hist[t], 12)),
               tuple(map(tuple, np.round(orient_hist[t], 12))))
        if sig in sigs:
            g2 = False
            break
        sigs.add(sig)

    # Gate 3: factorization.
    fac = factorization_evidence()
    g3 = (fac["A_independent_of_B_exact"] and fac["B_independent_of_A_exact"]
          and abs(fac["mi_AB_nats"]) < fac["mi_tolerance_nats"])

    # Gate 4: tie-break (delegated to the suite; summarized from pytest).
    # MWE integrity.
    two_strata = set(mwe["strata"].values()) == {0, 1}
    natural_term = mwe["steps_run"] < MAX_STEPS and mwe["total_commits"] > 0

    # 2) Full pytest suite.
    passed, failed, pytest_out, pytest_rc = run_pytest()
    g4 = (failed == 0 and "test_tiebreak" in pytest_out)
    suite_ok = (failed == 0 and passed >= 20)

    certified = (g1 and g2 and g3 and g4 and two_strata
                 and natural_term and suite_ok)

    results = {
        "certified": bool(certified),
        "suite": {"passed": passed, "failed": failed,
                  "pytest_returncode": pytest_rc},
        "gates": {
            "gate1_monotonicity": bool(g1),
            "gate2_acyclicity": bool(g2),
            "gate3_factorization": bool(g3),
            "gate4_tiebreak": bool(g4),
        },
        "mwe_integrity": {
            "two_strata": bool(two_strata),
            "decoupled_bridge": list(BRIDGE),
            "steps_run": mwe["steps_run"],
            "max_steps": MAX_STEPS,
            "terminated_naturally": bool(natural_term),
            "total_commits": mwe["total_commits"],
        },
        "factorization": fac,
        "final_rho_A": rho_A,
        "final_rho_B": rho_B,
        "seeds": {"A": 1, "B": 2},
    }

    # 3) Artifacts.
    with open(os.path.join(OUT_DIR, "certification_results.json"), "w",
              encoding="utf-8") as fh:
        json.dump(results, fh, indent=2, sort_keys=True)
    with open(os.path.join(OUT_DIR, "certification_log.txt"), "w",
              encoding="utf-8") as fh:
        fh.write(pytest_out)
    _write_snapshot(os.path.join(OUT_DIR, "certification_snapshot.md"), results)

    # 4) Console summary.
    print("=" * 64)
    print("BUILD STEP 10 - CERTIFICATION RUN")
    print("=" * 64)
    print(f"\n  pytest          : {passed} passed, {failed} failed")
    print(f"  Gate 1 mono     : {g1}")
    print(f"  Gate 2 acyclic  : {g2}")
    print(f"  Gate 3 factor   : {g3}  "
          f"(MI={fac['mi_AB_nats']:.6f} nats, exact A<->B "
          f"{fac['A_independent_of_B_exact'] and fac['B_independent_of_A_exact']})")
    print(f"  Gate 4 tiebreak : {g4}")
    print(f"  MWE integrity   : two_strata={two_strata}, "
          f"natural_term={natural_term} (step {mwe['steps_run']}/{MAX_STEPS})")
    print(f"  final rho A     : {rho_A}")
    print(f"  final rho B     : {rho_B}")
    print(f"\n  artifacts -> {os.path.relpath(OUT_DIR, _HERE)}/")
    print("\n" + "=" * 64)
    print(f"SIMULATOR: {'CERTIFIED' if certified else 'NOT CERTIFIED'}")
    if certified:
        print("Delta measurement is now PERMITTED.")
    print("=" * 64)
    return certified


def _write_snapshot(path, r):
    g = r["gates"]
    lines = [
        "# Certification Snapshot",
        "",
        f"**Verdict:** {'CERTIFIED' if r['certified'] else 'NOT CERTIFIED'}",
        f"**Suite:** {r['suite']['passed']} passed, {r['suite']['failed']} failed",
        "",
        "| Gate | Result |",
        "|---|---|",
        f"| 1 - Monotonicity | {'PASS' if g['gate1_monotonicity'] else 'FAIL'} |",
        f"| 2 - Acyclicity | {'PASS' if g['gate2_acyclicity'] else 'FAIL'} |",
        f"| 3 - Factorization | {'PASS' if g['gate3_factorization'] else 'FAIL'} |",
        f"| 4 - Tie-break | {'PASS' if g['gate4_tiebreak'] else 'FAIL'} |",
        "",
        "## Factorization evidence",
        f"- A independent of B (exact): {r['factorization']['A_independent_of_B_exact']}",
        f"- B independent of A (exact): {r['factorization']['B_independent_of_A_exact']}",
        f"- MI(A;B): {r['factorization']['mi_AB_nats']:.6f} nats "
        f"(tol {r['factorization']['mi_tolerance_nats']})",
        f"- MI(A;shuffled B): {r['factorization']['mi_A_shuffledB_nats']:.6f} nats",
        "",
        "## MWE",
        f"- two strata: {r['mwe_integrity']['two_strata']}, "
        f"bridge {r['mwe_integrity']['decoupled_bridge']}",
        f"- terminated naturally at step {r['mwe_integrity']['steps_run']} "
        f"(max {r['mwe_integrity']['max_steps']}), "
        f"{r['mwe_integrity']['total_commits']} commits",
        f"- final rho A: {r['final_rho_A']}",
        f"- final rho B: {r['final_rho_B']}",
        "",
        ("**Delta measurement is PERMITTED.**" if r["certified"]
         else "**Delta measurement is NOT permitted (gates failing).**"),
    ]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
