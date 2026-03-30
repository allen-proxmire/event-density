"""
ED-Phys-02: Top-Level Run Script
===================================
Usage:
    python ed_phys_run.py                   # 1D default cosmological run
    python ed_phys_run.py --dim 2           # 2D default cosmological run
    python ed_phys_run.py --dim 1 --N 512   # Custom grid size
    python ed_phys_run.py --alpha 0.2 --gamma_exp 0.3  # Custom physics

All parameters map directly to EDParams (ED-Phys-01 §12).
"""

import argparse
import sys
import numpy as np

from ed_phys_config import EDParams, default_cosmology_1d, default_cosmology_2d
from ed_phys_lattice import create_initial_condition
from ed_phys_engine import simulate
from ed_phys_diagnostics import summary, extract_time_series, identify_phases


def parse_args():
    parser = argparse.ArgumentParser(
        description="ED-Phys Minimal Universe Simulator"
    )

    # Grid
    parser.add_argument("--dim", type=int, default=1, choices=[1, 2],
                        help="Lattice dimensionality (1 or 2)")
    parser.add_argument("--N", type=int, default=None,
                        help="Grid size (default: 256 for 1D, 128 for 2D)")
    parser.add_argument("--dx", type=float, default=1.0,
                        help="Grid spacing")

    # Physics
    parser.add_argument("--alpha", type=float, default=0.1,
                        help="Relational penalty coupling")
    parser.add_argument("--gamma_exp", type=float, default=0.5,
                        help="Concavity exponent (0 < γ < 1)")
    parser.add_argument("--M_0", type=float, default=1.0,
                        help="Bare mobility")
    parser.add_argument("--rho_max", type=float, default=100.0,
                        help="Saturation density")
    parser.add_argument("--n_mob", type=int, default=2,
                        help="Mobility exponent")
    parser.add_argument("--gamma_b", type=float, default=0.0,
                        help="Boundary penalty coupling")

    # Numerics
    parser.add_argument("--eta", type=float, default=None,
                        help="Timestep (None = auto from CFL)")
    parser.add_argument("--cfl_safety", type=float, default=0.1,
                        help="CFL safety factor")
    parser.add_argument("--n_steps", type=int, default=10000,
                        help="Number of timesteps")
    parser.add_argument("--record_interval", type=int, default=100,
                        help="Diagnostic recording interval")
    parser.add_argument("--boundary", type=str, default="periodic",
                        choices=["periodic", "absorbing", "reflecting"])
    parser.add_argument("--early_stop", type=float, default=None,
                        help="Stop when mean gradient < this value")

    # Initial conditions
    parser.add_argument("--ic_mode", type=str, default="uniform_noise",
                        choices=["uniform_noise", "localized_gradient", "random"])
    parser.add_argument("--rho_mean", type=float, default=50.0,
                        help="Mean initial density")
    parser.add_argument("--noise", type=float, default=0.1,
                        help="Noise amplitude")
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed")

    # Output
    parser.add_argument("--snapshot_interval", type=int, default=None,
                        help="Store full-field snapshots every N steps")
    parser.add_argument("--save_npz", type=str, default=None,
                        help="Save results to .npz file")

    return parser.parse_args()


def main():
    args = parse_args()

    # Build parameters
    N = args.N or (256 if args.dim == 1 else 128)

    params = EDParams(
        alpha=args.alpha,
        gamma_exp=args.gamma_exp,
        M_0=args.M_0,
        rho_max=args.rho_max,
        n_mob=args.n_mob,
        gamma_b=args.gamma_b,
        dimensions=args.dim,
        N=N,
        dx=args.dx,
        eta=args.eta,
        cfl_safety=args.cfl_safety,
        n_steps=args.n_steps,
        record_interval=args.record_interval,
        boundary=args.boundary,
        early_stop_gradient=args.early_stop,
    )

    print(f"ED-Phys Simulator -- {args.dim}D, N={N}, {args.n_steps} steps")
    print(f"  eta = {params.eta:.6e}  (CFL safety = {args.cfl_safety})")
    print(f"  alpha={args.alpha}, gamma_exp={args.gamma_exp}, M_0={args.M_0}, "
          f"rho_max={args.rho_max}, n_mob={args.n_mob}")
    print()

    # Create initial conditions
    rho_0 = create_initial_condition(
        params,
        mode=args.ic_mode,
        rho_mean=args.rho_mean,
        noise_amplitude=args.noise,
        seed=args.seed,
    )

    # Run simulation
    print("Running simulation...")
    result = simulate(params, rho_0, snapshot_interval=args.snapshot_interval)

    # Print summary
    print()
    print(summary(result))

    # Print phase identification
    phases = identify_phases(result)
    if phases:
        print("\nPhase Identification:")
        for ph in phases:
            print(f"  [{ph['start_step']:6d} - {ph['end_step']:6d}] "
                  f"{ph['name']:25s}  {ph['description']}")

    # Save if requested
    if args.save_npz:
        ts = extract_time_series(result)
        save_dict = {
            "rho_final": result.rho_final,
            **ts,
        }
        if result.rho_snapshots:
            save_dict["snapshots"] = np.stack(result.rho_snapshots)
        np.savez_compressed(args.save_npz, **save_dict)
        print(f"\nResults saved to {args.save_npz}")

    return result


if __name__ == "__main__":
    main()
