"""
Run the full solver-independence test: 2 solvers x 3 H values x 2 amplitudes.

Linear regime verification:  amp=0.2, sigma=0.15 (same as v1.0)
Nonlinear regime attempt:    amp=0.45, sigma=0.30 (same as v1.1b)

Expected outcomes:
 - Both solvers reproduce ω_linear in the linear regime → validates solver linear accuracy.
 - In the nonlinear regime: if both give ω_linear, FPv2 54% is solver-specific (Scenario A).
                            If either gives ω ≈ 0.54·ω_linear, result is physical (Scenario B).
                            If they disagree with each other, result is protocol-sensitive (Scenario C).

All runs at N=80, L=2.0, periodic BC (both solvers).
"""

import time
from pathlib import Path
import numpy as np

import solver_spectral_etdrk2 as sp
import solver_mol_bdf as bdf


def run_all():
    outdir = Path(__file__).parent
    H_values = [10.0, 20.0, 50.0]
    amp_configs = [
        ("linear", 0.2, 0.15),
        ("nonlinear", 0.45, 0.30),
    ]

    summary_rows = []

    for regime, amp, sigma in amp_configs:
        for H in H_values:
            print(f"\n{'='*78}")
            print(f"REGIME={regime}   H={H}   amp={amp}   sigma={sigma}")
            print(f"{'='*78}")

            # Spectral ETDRK2
            ep_sp = sp.EDParams(D=0.3, P0=0.01, H=H, zeta=0.1, tau=1.0)
            sim_sp = sp.SimParams(N=80, L=2.0, T=200.0, dt=0.02,
                                    store_every=1, snapshot_every=50)
            out_sp_path = outdir / f"spec_H{int(H):02d}_{regime}.npz"
            t0 = time.time()
            sp.run(ep_sp, sim_sp, ic_amplitude=amp, ic_sigma=sigma,
                    outpath=out_sp_path, verbose=True)
            t_sp = time.time() - t0
            print(f"  [spectral wall-time: {t_sp:.1f} s]")

            # MOL-BDF
            ep_bdf = bdf.EDParams(D=0.3, P0=0.01, H=H, zeta=0.1, tau=1.0)
            sim_bdf = bdf.SimParams(N=80, L=2.0, T=200.0,
                                      store_dt=0.05, snapshot_dt=1.0)
            out_bdf_path = outdir / f"bdf_H{int(H):02d}_{regime}.npz"
            t0 = time.time()
            bdf.run(ep_bdf, sim_bdf, ic_amplitude=amp, ic_sigma=sigma,
                     outpath=out_bdf_path, verbose=True, rtol=1e-5, atol=1e-8)
            t_bdf = time.time() - t0
            print(f"  [BDF wall-time: {t_bdf:.1f} s]")

            summary_rows.append(dict(regime=regime, H=H, amp=amp, sigma=sigma,
                                      t_spectral=t_sp, t_bdf=t_bdf))

    # Print runtime summary
    print("\n\n" + "=" * 78)
    print("RUNTIME SUMMARY")
    print("=" * 78)
    print(f"{'Regime':<12}{'H':>6}{'amp':>6}{'sigma':>7}{'t_spec (s)':>12}{'t_BDF (s)':>12}")
    for r in summary_rows:
        print(f"{r['regime']:<12}{r['H']:>6.0f}{r['amp']:>6.2f}{r['sigma']:>7.2f}"
              f"{r['t_spectral']:>12.1f}{r['t_bdf']:>12.1f}")


if __name__ == "__main__":
    run_all()
