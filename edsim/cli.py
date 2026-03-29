"""
edsim.cli — Command-line interface for ED-SIM-02.

Provides four commands:
    edsim info      Print version and environment info
    edsim run       Run a named scenario
    edsim sweep     Run a parameter sweep
    edsim certify   Run the reproducibility pipeline

All commands are thin wrappers around existing Python functions.
"""

from __future__ import annotations

import argparse
import platform
import sys
import time


def _cmd_info(args: argparse.Namespace) -> int:
    """Print version and environment information."""
    from .version import VERSION, CODENAME
    import numpy as np
    import scipy

    print(f"{CODENAME} v{VERSION}")
    print(f"Python:     {sys.version.split()[0]}")
    print(f"NumPy:      {np.__version__}")
    print(f"SciPy:      {scipy.__version__}")
    print(f"Platform:   {platform.platform()}")
    print(f"Package:    {__file__}")
    return 0


def _cmd_run(args: argparse.Namespace) -> int:
    """Run a named scenario and print a summary."""
    from .experiments.scenarios import get_scenario, get_scenarios
    from .experiments.atlas import run_atlas, summarize_time_series

    name = args.scenario

    # List available scenarios if requested
    if name == "list":
        print("Available scenarios:")
        for sname, sc in sorted(get_scenarios().items()):
            config = sc.make_config()
            p = config.params
            print(f"  {sname:25s}  d={p.d}  N={p.N[0]:2d}  T={p.T:.2f}  ic={config.ic_type}")
        return 0

    try:
        scenario = get_scenario(name)
    except KeyError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    print(f"Running scenario: {name}")
    print(f"  {scenario.description}")
    print()

    t0 = time.time()
    params, ts = run_atlas(scenario)
    elapsed = time.time() - t0

    summary = summarize_time_series(ts)

    print(f"Completed in {elapsed:.1f}s  ({summary['n_snapshots']} snapshots)")
    print()
    print(f"  Energy:     {summary['energy_initial']:.4e} -> {summary['energy_final']:.4e}  "
          f"(ratio={summary['energy_ratio']:.4f})")
    print(f"  Complexity: {summary['complexity_initial']:.4e} -> {summary['complexity_final']:.4e}  "
          f"(ratio={summary['complexity_ratio']:.4f})")
    print(f"  Mass:       change={summary['mass_change']:.2e}")
    print(f"  H_spec:     {summary['spectral_entropy_initial']:.3f} -> {summary['spectral_entropy_final']:.3f}")
    print(f"  R_grad:     {summary['R_grad_mean']:.4f} (mean)")
    print(f"  xi:         {summary['correlation_length_initial']:.4f} -> {summary['correlation_length_final']:.4f}")
    print(f"  chi:        {summary['euler_chi_initial']} -> {summary['euler_chi_final']}")
    print(f"  v_final:    {summary['v_final']:+.4e}")
    print(f"  E monotone: {summary['energy_monotone']}")
    return 0


def _cmd_sweep(args: argparse.Namespace) -> int:
    """Run a parameter sweep and print results."""
    from .experiments.scenarios import get_scenario
    from .experiments.sweeps import run_sweep
    from .experiments.atlas import summarize_time_series

    try:
        scenario = get_scenario(args.scenario)
    except KeyError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    # Parse values as floats
    try:
        values = [float(v) for v in args.values]
    except ValueError:
        print("Error: sweep values must be numeric.", file=sys.stderr)
        return 1

    print(f"Sweeping {args.param} over {values}")
    print(f"Scenario: {args.scenario}")
    print()

    t0 = time.time()
    results = run_sweep(scenario, args.param, values)
    elapsed = time.time() - t0

    # Print table
    print(f"{'Label':>20s}  {'E_ratio':>8s}  {'C_ratio':>8s}  {'R_grad':>8s}  {'xi_final':>8s}")
    print("-" * 60)
    for sr in results:
        s = summarize_time_series(sr.series)
        print(f"{sr.label:>20s}  {s['energy_ratio']:8.4f}  {s['complexity_ratio']:8.4f}  "
              f"{s['R_grad_mean']:8.4f}  {s['correlation_length_final']:8.4f}")

    print(f"\nCompleted in {elapsed:.1f}s ({len(results)} runs)")
    return 0


def _cmd_certify(args: argparse.Namespace) -> int:
    """Run the reproducibility pipeline."""
    # Delegate to the existing run_all module
    from .reproducibility.run_all import main as run_all_main
    return run_all_main()


def main() -> int:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="edsim",
        description="ED-SIM-02: An Architectural Lab for Entropic Dynamics",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # --- info ---
    subparsers.add_parser("info", help="Print version and environment info")

    # --- run ---
    p_run = subparsers.add_parser("run", help="Run a named scenario (use 'list' to see options)")
    p_run.add_argument("scenario", type=str, help="Scenario name or 'list'")

    # --- sweep ---
    p_sweep = subparsers.add_parser("sweep", help="Run a parameter sweep")
    p_sweep.add_argument("scenario", type=str, help="Base scenario name")
    p_sweep.add_argument("param", type=str, help="Parameter to vary (e.g. 'D', 'ic_A')")
    p_sweep.add_argument("values", nargs="+", help="Values to sweep")

    # --- certify ---
    subparsers.add_parser("certify", help="Run the reproducibility pipeline")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 0

    dispatch = {
        "info": _cmd_info,
        "run": _cmd_run,
        "sweep": _cmd_sweep,
        "certify": _cmd_certify,
    }

    return dispatch[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
