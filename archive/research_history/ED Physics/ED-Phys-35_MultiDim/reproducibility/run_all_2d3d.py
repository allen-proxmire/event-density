"""
run_all_2d3d.py
===============
Reproducibility pipeline for the ED 2D/3D extension project.

Phases:
  1. Environment check     — verify imports and versions
  2. 2D solver validation  — run core tests
  3. 3D solver validation  — run core tests
  4. 2D invariant tests    — verify invariant computations
  5. 3D invariant tests    — verify invariant computations
  6. 2D atlas generation   — four scenarios (A2D–D2D)
  7. 3D demonstration run  — single scenario
  8. Final figures          — synthesis figure set
  9. Summary report         — JSON export

Usage:
  python reproducibility/run_all_2d3d.py
  python reproducibility/run_all_2d3d.py --quick   # fast mode (smaller grids)
"""

import os
import sys
import json
import time
import subprocess
import argparse
from datetime import datetime, timezone

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_DIR = os.path.dirname(_SCRIPT_DIR)
sys.path.insert(0, _PROJECT_DIR)

OUT_DIR = os.path.join(_PROJECT_DIR, "edsim2d", "output", "reproducibility")
os.makedirs(OUT_DIR, exist_ok=True)


def run_step(name, script_or_cmd, cwd=None, timeout=600):
    """Run a Python script and return (success, elapsed, stdout_snippet)."""
    if cwd is None:
        cwd = _PROJECT_DIR
    t0 = time.time()
    try:
        result = subprocess.run(
            [sys.executable, "-c", script_or_cmd] if "\n" in script_or_cmd
            else [sys.executable, script_or_cmd],
            cwd=cwd, capture_output=True, text=True, timeout=timeout,
        )
        elapsed = time.time() - t0
        success = result.returncode == 0
        # Extract last few meaningful lines
        lines = (result.stdout + result.stderr).strip().split("\n")
        snippet = "\n".join(lines[-5:])
        return success, elapsed, snippet
    except subprocess.TimeoutExpired:
        return False, time.time() - t0, "TIMEOUT"
    except Exception as e:
        return False, time.time() - t0, str(e)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true", help="Fast mode (smaller grids)")
    args = parser.parse_args()

    pipeline_start = time.time()
    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": "quick" if args.quick else "full",
        "phases": {},
    }
    n_pass = 0
    n_fail = 0

    print("=" * 72)
    print("  ED 2D/3D REPRODUCIBILITY PIPELINE")
    print(f"  Mode: {'QUICK' if args.quick else 'FULL'}")
    print("=" * 72)

    # ----- Phase 1: Environment -----
    print("\n--- Phase 1: Environment check ---")
    env_script = """
import numpy as np
import scipy
import matplotlib
from scipy.fft import dctn, idctn
from scipy.linalg import solve_banded
print(f"numpy {np.__version__}")
print(f"scipy {scipy.__version__}")
print(f"matplotlib {matplotlib.__version__}")
print("All imports OK")
"""
    ok, t, msg = run_step("environment", env_script)
    status = "PASS" if ok else "FAIL"
    n_pass += ok; n_fail += (not ok)
    print(f"  {status} ({t:.1f}s)")
    report["phases"]["1_environment"] = {"status": status, "time_s": t, "detail": msg}

    # ----- Phase 2: 2D solver tests -----
    print("\n--- Phase 2: 2D solver validation ---")
    test_2d = """
import warnings; warnings.filterwarnings('ignore')
import sys; sys.path.insert(0, '.')
from edsim_solver_2d import *
# Quick tests
p = EDParameters2D(Nx=16, Ny=16, dt=1e-3, T=0.01, method='etdrk4', k_out=10)
s = initialize_state_2d(p, perturbation='uniform')
for _ in range(10): s = step_2d(s, p)
assert abs(s['rho'].mean() - 0.5) < 1e-12, "Uniform test failed"
# Energy test
p2 = EDParameters2D(Nx=16, Ny=16, dt=1e-3, T=0.05, method='etdrk4', k_out=10)
s2 = initialize_state_2d(p2, perturbation='gaussian', amplitude=0.05)
E0 = energy_2d(s2['rho'], s2['v'], p2)['total']
for _ in range(50): s2 = step_2d(s2, p2)
Ef = energy_2d(s2['rho'], s2['v'], p2)['total']
assert Ef <= E0, "Energy monotonicity failed"
print("2D solver: ALL PASS")
"""
    ok, t, msg = run_step("2d_solver", test_2d)
    status = "PASS" if ok else "FAIL"
    n_pass += ok; n_fail += (not ok)
    print(f"  {status} ({t:.1f}s)")
    report["phases"]["2_solver_2d"] = {"status": status, "time_s": t}

    # ----- Phase 3: 3D solver tests -----
    print("\n--- Phase 3: 3D solver validation ---")
    test_3d = """
import warnings; warnings.filterwarnings('ignore')
import sys; sys.path.insert(0, '.')
from edsim_solver_3d import *
p = EDParameters3D(Nx=12, Ny=12, Nz=12, dt=1e-3, T=0.01, method='etdrk4', k_out=10)
s = initialize_state_3d(p, perturbation='uniform')
for _ in range(10): s = step_3d(s, p)
assert abs(s['rho'].mean() - 0.5) < 1e-12
p2 = EDParameters3D(Nx=12, Ny=12, Nz=12, dt=1e-3, T=0.03, method='etdrk4', k_out=10)
s2 = initialize_state_3d(p2, perturbation='cosine', amplitude=0.03)
E0 = energy_3d(s2['rho'], s2['v'], p2)['total']
for _ in range(30): s2 = step_3d(s2, p2)
Ef = energy_3d(s2['rho'], s2['v'], p2)['total']
assert Ef <= E0
print("3D solver: ALL PASS")
"""
    ok, t, msg = run_step("3d_solver", test_3d)
    status = "PASS" if ok else "FAIL"
    n_pass += ok; n_fail += (not ok)
    print(f"  {status} ({t:.1f}s)")
    report["phases"]["3_solver_3d"] = {"status": status, "time_s": t}

    # ----- Phase 4: 2D invariant tests -----
    print("\n--- Phase 4: 2D invariant tests ---")
    ok, t, msg = run_step("2d_invariants", "test_invariants_2d.py", timeout=120)
    status = "PASS" if ok and "0 FAIL" in msg else "FAIL"
    n_pass += (status == "PASS"); n_fail += (status == "FAIL")
    print(f"  {status} ({t:.1f}s)")
    report["phases"]["4_invariants_2d"] = {"status": status, "time_s": t}

    # ----- Phase 5: 3D invariant tests -----
    print("\n--- Phase 5: 3D invariant tests ---")
    ok, t, msg = run_step("3d_invariants", "test_invariants_3d.py", timeout=120)
    status = "PASS" if ok and "0 FAIL" in msg else "FAIL"
    n_pass += (status == "PASS"); n_fail += (status == "FAIL")
    print(f"  {status} ({t:.1f}s)")
    report["phases"]["5_invariants_3d"] = {"status": status, "time_s": t}

    # ----- Phase 6: 2D atlas -----
    print("\n--- Phase 6: 2D atlas generation ---")
    N_atlas = 24 if args.quick else 48
    T_atlas = 0.2 if args.quick else 0.5
    atlas_2d = f"""
import warnings; warnings.filterwarnings('ignore')
import sys; sys.path.insert(0, '.')
from edsim2d.experiments_2d import run_atlas_2d
atlas = run_atlas_2d(N={N_atlas}, T={T_atlas}, dt=5e-4, generate_figures=False, verbose=True)
print(f"2D atlas: {{len(atlas['scenarios'])}} scenarios completed")
"""
    ok, t, msg = run_step("2d_atlas", atlas_2d, timeout=300)
    status = "PASS" if ok else "FAIL"
    n_pass += ok; n_fail += (not ok)
    print(f"  {status} ({t:.1f}s)")
    report["phases"]["6_atlas_2d"] = {"status": status, "time_s": t}

    # ----- Phase 7: 3D demo -----
    print("\n--- Phase 7: 3D demonstration run ---")
    N_3d = 12 if args.quick else 16
    demo_3d = (
        "import warnings; warnings.filterwarnings('ignore')\n"
        "import sys; sys.path.insert(0, '.')\n"
        "from edsim_solver_3d import *\n"
        "from invariants_3d import compute_invariants_3d\n"
        f"p = EDParameters3D(Nx={N_3d}, Ny={N_3d}, Nz={N_3d}, dt=1e-3, T=0.1,\n"
        "                   method='etdrk4', k_out=100)\n"
        "res = run_simulation_3d(p, perturbation='cosine', amplitude=0.03, verbose=True)\n"
        "rho_f = res['final_state']['rho']\n"
        "F = operator_F_fd_3d(rho_f, p)\n"
        "Fb = spatial_avg_3d(F, p.hx, p.hy, p.hz)\n"
        "inv = compute_invariants_3d(rho_f, res['v_history'][-1], Fb, p)\n"
        "print('H=' + str(round(inv['spectral']['spectral_entropy'], 4)))\n"
        "m = inv['geometric']['morphology']\n"
        "print('F/S/B=' + '/'.join(str(round(m[k],2)) for k in ['filament_fraction','sheet_fraction','blob_fraction']))\n"
        "print('3D demo: PASS')\n"
    )
    ok, t, msg = run_step("3d_demo", demo_3d, timeout=120)
    status = "PASS" if ok else "FAIL"
    n_pass += ok; n_fail += (not ok)
    print(f"  {status} ({t:.1f}s)")
    report["phases"]["7_demo_3d"] = {"status": status, "time_s": t}

    # ----- Phase 8: Final figures -----
    print("\n--- Phase 8: Final figures ---")
    ok, t, msg = run_step("figures", "generate_final_figures.py", timeout=60)
    status = "PASS" if ok else "FAIL"
    n_pass += ok; n_fail += (not ok)
    print(f"  {status} ({t:.1f}s)")
    report["phases"]["8_figures"] = {"status": status, "time_s": t}

    # ----- Phase 9: Summary -----
    total_time = time.time() - pipeline_start
    report["total_time_s"] = total_time
    report["n_pass"] = n_pass
    report["n_fail"] = n_fail
    report["verdict"] = "PASS" if n_fail == 0 else "FAIL"

    report_path = os.path.join(OUT_DIR, "pipeline_report.json")
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)

    print("\n" + "=" * 72)
    print(f"  PIPELINE COMPLETE: {n_pass} PASS, {n_fail} FAIL")
    print(f"  Total time: {total_time:.0f}s")
    print(f"  Verdict: {report['verdict']}")
    print(f"  Report: {report_path}")
    print("=" * 72)


if __name__ == "__main__":
    main()
