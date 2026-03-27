"""
run_all.py
==========
Master Reproducibility Script for ED-SIM v1

Runs the complete ED-SIM v1 pipeline end-to-end:

  Phase 1: Environment checks
  Phase 2: Data integrity checks
  Phase 3: Regime volume experiment (if missing)
  Phase 4: All 16 invariant analyses
  Phase 5: Meta-analyses (universality, cross-consistency, embedding)
  Phase 6: Global atlas report
  Phase 7: Master index + ED Consistency Certificate
  Phase 8: Output validation

Robust to missing data and optional dependencies. Never crashes on
partial results — reports what succeeded and what was skipped.

Usage:
    python reproducibility/run_all.py [--skip-runs] [--skip-invariants]

Requires: numpy, scipy, matplotlib.
"""

import os
import sys
import time
import subprocess
import argparse
import json
import datetime

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SIM_DIR = os.path.dirname(SCRIPT_DIR)

# Add SIM_DIR to path so experiments/ can be found
sys.path.insert(0, SIM_DIR)

EXPERIMENTS_DIR = os.path.join(SIM_DIR, "experiments")
CHECKS_DIR = os.path.join(SCRIPT_DIR, "checks")
VALIDATION_DIR = os.path.join(SCRIPT_DIR, "validation")
ATLAS_DIR = os.path.join(SIM_DIR, "output", "atlas")


# ---------------------------------------------------------------------------
# Pipeline steps
# ---------------------------------------------------------------------------
PHASE_1_CHECKS = [
    ("Environment Check", os.path.join(CHECKS_DIR, "check_environment.py")),
]

PHASE_2_DATA = [
    ("Data Integrity", os.path.join(CHECKS_DIR, "check_data_integrity.py")),
]

PHASE_3_RUNS = [
    ("Regime Volume 3D", os.path.join(EXPERIMENTS_DIR,
                                       "regime_volume_3d.py")),
]

PHASE_4_INVARIANTS = [
    ("Low-Mode Collapse",
     os.path.join(EXPERIMENTS_DIR, "invariant_low_mode_collapse.py")),
    ("Mode-Energy Ratios",
     os.path.join(EXPERIMENTS_DIR, "invariant_mode_energy_ratios.py")),
    ("Modal Ratios",
     os.path.join(EXPERIMENTS_DIR, "invariant_modal_ratios.py")),
    ("Spectral Entropy",
     os.path.join(EXPERIMENTS_DIR, "invariant_spectral_entropy.py")),
    ("Spectral Complexity (Renyi)",
     os.path.join(EXPERIMENTS_DIR, "invariant_spectral_complexity.py")),
    ("Dissipation Partitions",
     os.path.join(EXPERIMENTS_DIR, "invariant_dissipation_partitions.py")),
    ("Energy-Entropy Geometry",
     os.path.join(EXPERIMENTS_DIR, "invariant_energy_entropy_geometry.py")),
    ("Broadband Cascade",
     os.path.join(EXPERIMENTS_DIR, "invariant_broadband_cascade.py")),
    ("Convergence Stability",
     os.path.join(EXPERIMENTS_DIR, "invariant_convergence_stability.py")),
    ("Modal Correlations",
     os.path.join(EXPERIMENTS_DIR, "invariant_modal_correlations.py")),
    ("Modal Overlap",
     os.path.join(EXPERIMENTS_DIR, "invariant_modal_overlap.py")),
    ("Phase Dynamics",
     os.path.join(EXPERIMENTS_DIR, "invariant_modal_phase_dynamics.py")),
    ("Phase-Amplitude Coupling",
     os.path.join(EXPERIMENTS_DIR,
                  "invariant_phase_amplitude_coupling.py")),
    ("Triad Balance",
     os.path.join(EXPERIMENTS_DIR, "invariant_triad_balance.py")),
    ("Lyapunov Spectrum",
     os.path.join(EXPERIMENTS_DIR, "invariant_lyapunov_spectrum.py")),
    ("Attractor Manifold",
     os.path.join(EXPERIMENTS_DIR, "invariant_attractor_manifold.py")),
]

PHASE_5_META = [
    ("Parameter Universality",
     os.path.join(EXPERIMENTS_DIR, "invariant_parameter_universality.py")),
    ("Cross-Consistency",
     os.path.join(EXPERIMENTS_DIR, "invariant_cross_consistency.py")),
    ("Embedding Map",
     os.path.join(EXPERIMENTS_DIR, "invariant_embedding_map.py")),
]

PHASE_6_REPORT = [
    ("Global Atlas Report",
     os.path.join(EXPERIMENTS_DIR, "generate_global_atlas_report.py")),
]

PHASE_7_CERT = [
    ("Master Index + Certificate",
     os.path.join(EXPERIMENTS_DIR,
                  "generate_master_index_and_certificate.py")),
]

PHASE_8_VALIDATE = [
    ("Output Validation",
     os.path.join(VALIDATION_DIR, "validate_outputs.py")),
]


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------
class PipelineRunner:

    def __init__(self, skip_runs: bool = False,
                 skip_invariants: bool = False):
        self.skip_runs = skip_runs
        self.skip_invariants = skip_invariants
        self.results = {}   # name -> {"status", "time_s", "message"}
        self.start_time = time.time()

    def run_step(self, name: str, script_path: str) -> bool:
        """Run a single Python script. Returns True on success."""
        if not os.path.isfile(script_path):
            self.results[name] = {
                "status": "SKIPPED",
                "time_s": 0.0,
                "message": f"Script not found: {script_path}",
            }
            return False

        print(f"\n  [{name}]")
        print(f"    Script: {os.path.relpath(script_path, SIM_DIR)}")

        t0 = time.time()
        try:
            result = subprocess.run(
                [sys.executable, script_path],
                cwd=SIM_DIR,
                capture_output=True,
                text=True,
                timeout=3600,  # 1 hour max per step
            )
            elapsed = time.time() - t0

            if result.returncode == 0:
                self.results[name] = {
                    "status": "PASS",
                    "time_s": elapsed,
                    "message": "Completed successfully.",
                }
                print(f"    Status: PASS ({elapsed:.1f}s)")
                return True
            else:
                # Non-zero exit — capture stderr
                stderr_tail = result.stderr.strip().split("\n")[-5:]
                msg = "\n".join(stderr_tail)
                self.results[name] = {
                    "status": "FAIL",
                    "time_s": elapsed,
                    "message": msg,
                }
                print(f"    Status: FAIL ({elapsed:.1f}s)")
                print(f"    Error:  {stderr_tail[-1] if stderr_tail else '(no output)'}")
                return False

        except subprocess.TimeoutExpired:
            elapsed = time.time() - t0
            self.results[name] = {
                "status": "TIMEOUT",
                "time_s": elapsed,
                "message": "Exceeded 1-hour timeout.",
            }
            print(f"    Status: TIMEOUT ({elapsed:.1f}s)")
            return False

        except Exception as e:
            elapsed = time.time() - t0
            self.results[name] = {
                "status": "ERROR",
                "time_s": elapsed,
                "message": str(e),
            }
            print(f"    Status: ERROR ({elapsed:.1f}s) — {e}")
            return False

    def run_phase(self, phase_name: str,
                  steps: list[tuple[str, str]]) -> int:
        """Run a phase (list of steps). Returns count of successes."""
        sep = "=" * 70
        print(f"\n{sep}")
        print(f"  PHASE: {phase_name}")
        print(f"{sep}")

        n_pass = 0
        for name, path in steps:
            if self.run_step(name, path):
                n_pass += 1
        return n_pass

    def run_pipeline(self):
        """Run the full ED-SIM v1 reproducibility pipeline."""
        print()
        print("  ╔════════════════════════════════════════════════════════╗")
        print("  ║   ED-SIM v1 — Full Reproducibility Pipeline           ║")
        print("  ╚════════════════════════════════════════════════════════╝")
        print()
        print(f"  Started: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  Working directory: {SIM_DIR}")

        # Phase 1: Environment
        self.run_phase("Environment Checks", PHASE_1_CHECKS)

        # Phase 2: Data Integrity
        self.run_phase("Data Integrity", PHASE_2_DATA)

        # Phase 3: Regime Volume Runs
        if self.skip_runs:
            print("\n" + "=" * 70)
            print("  PHASE: Regime Volume Runs — SKIPPED (--skip-runs)")
            print("=" * 70)
            for name, _ in PHASE_3_RUNS:
                self.results[name] = {
                    "status": "SKIPPED",
                    "time_s": 0.0,
                    "message": "Skipped by --skip-runs flag.",
                }
        else:
            self.run_phase("Regime Volume Runs", PHASE_3_RUNS)

        # Phase 4: Invariants
        if self.skip_invariants:
            print("\n" + "=" * 70)
            print("  PHASE: Invariant Analyses — SKIPPED (--skip-invariants)")
            print("=" * 70)
            for name, _ in PHASE_4_INVARIANTS:
                self.results[name] = {
                    "status": "SKIPPED",
                    "time_s": 0.0,
                    "message": "Skipped by --skip-invariants flag.",
                }
        else:
            self.run_phase("Invariant Analyses (16 families)",
                           PHASE_4_INVARIANTS)

        # Phase 5: Meta-analyses
        if self.skip_invariants:
            for name, _ in PHASE_5_META:
                self.results[name] = {
                    "status": "SKIPPED",
                    "time_s": 0.0,
                    "message": "Skipped (depends on invariants).",
                }
        else:
            self.run_phase("Meta-Analyses", PHASE_5_META)

        # Phase 6: Global Atlas Report
        self.run_phase("Global Atlas Report", PHASE_6_REPORT)

        # Phase 7: Master Index + Certificate
        self.run_phase("Master Index & Certificate", PHASE_7_CERT)

        # Phase 8: Validation
        self.run_phase("Output Validation", PHASE_8_VALIDATE)

        # Summary
        self.print_summary()
        self.save_report()

    def print_summary(self):
        elapsed = time.time() - self.start_time
        n_total = len(self.results)
        n_pass = sum(1 for r in self.results.values()
                     if r["status"] == "PASS")
        n_fail = sum(1 for r in self.results.values()
                     if r["status"] == "FAIL")
        n_skip = sum(1 for r in self.results.values()
                     if r["status"] == "SKIPPED")
        n_err = sum(1 for r in self.results.values()
                    if r["status"] in ("ERROR", "TIMEOUT"))

        print()
        print("  ╔════════════════════════════════════════════════════════╗")
        print("  ║   PIPELINE SUMMARY                                    ║")
        print("  ╚════════════════════════════════════════════════════════╝")
        print()
        print(f"  Total steps:    {n_total}")
        print(f"  Passed:         {n_pass}")
        print(f"  Failed:         {n_fail}")
        print(f"  Skipped:        {n_skip}")
        print(f"  Errors/Timeout: {n_err}")
        print(f"  Wall time:      {elapsed:.1f}s ({elapsed/60:.1f}m)")
        print()

        # Status table
        print(f"  {'Step':<35} {'Status':<10} {'Time':>8}")
        print("  " + "-" * 57)
        for name, r in self.results.items():
            status = r["status"]
            t = f"{r['time_s']:.1f}s" if r["time_s"] > 0 else "—"

            mark = {"PASS": "+", "FAIL": "x", "SKIPPED": "-",
                    "ERROR": "!", "TIMEOUT": "!"}
            print(f"  {mark.get(status, '?')} {name:<33} {status:<10} {t:>8}")

        # Final verdict
        print()
        cert_path = os.path.join(ATLAS_DIR,
                                  "ED_Consistency_Certificate.txt")
        if os.path.isfile(cert_path):
            print("  Certificate: output/atlas/ED_Consistency_Certificate.txt")
            print()

        if n_fail == 0 and n_err == 0:
            print("  ┌────────────────────────────────────────────────────┐")
            print("  │  ALL STEPS COMPLETED SUCCESSFULLY                  │")
            print("  └────────────────────────────────────────────────────┘")
        elif n_fail > 0:
            print("  ┌────────────────────────────────────────────────────┐")
            print(f"  │  {n_fail} STEP(S) FAILED — see details above"
                  f"{'':>{36-len(str(n_fail))}}│")
            print("  └────────────────────────────────────────────────────┘")
        print()

    def save_report(self):
        """Save pipeline results to JSON."""
        os.makedirs(ATLAS_DIR, exist_ok=True)
        report_path = os.path.join(ATLAS_DIR,
                                    "reproducibility_pipeline_report.json")
        report = {
            "timestamp": datetime.datetime.now().isoformat(),
            "wall_time_s": time.time() - self.start_time,
            "steps": self.results,
            "summary": {
                "total": len(self.results),
                "pass": sum(1 for r in self.results.values()
                            if r["status"] == "PASS"),
                "fail": sum(1 for r in self.results.values()
                            if r["status"] == "FAIL"),
                "skipped": sum(1 for r in self.results.values()
                               if r["status"] == "SKIPPED"),
                "error": sum(1 for r in self.results.values()
                             if r["status"] in ("ERROR", "TIMEOUT")),
            },
        }
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        print(f"  Pipeline report saved: {report_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="ED-SIM v1 Full Reproducibility Pipeline",
    )
    parser.add_argument(
        "--skip-runs", action="store_true",
        help="Skip the regime volume experiment (use existing runs).",
    )
    parser.add_argument(
        "--skip-invariants", action="store_true",
        help="Skip all invariant analyses (use existing JSONs).",
    )
    args = parser.parse_args()

    runner = PipelineRunner(
        skip_runs=args.skip_runs,
        skip_invariants=args.skip_invariants,
    )
    runner.run_pipeline()


if __name__ == "__main__":
    main()
