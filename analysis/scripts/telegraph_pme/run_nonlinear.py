"""
v1.1 nonlinear-regime run.

Pushes the amplitude to 0.4 (vs 0.2 in v1.0) to drive the system into the
nonlinear PME regime where Foundational Paper v2 Analogue 5 reports the
54% frequency renormalization and 3-6% third-harmonic content.

CFL check at amp=0.4: rho_min = 0.1, delta_max = 0.9, M_max = 0.81.
With N=80, dt=5e-4: CFL ratio = 0.3 * 0.81 * 5e-4 / (dx^2) ~= 0.19. Stable.
"""

from pathlib import Path
from ed_solver_2d import EDParams, SimParams, run

if __name__ == "__main__":
    # Canonical H=50, weak penalty; push amplitude.
    ep = EDParams(D=0.3, P0=0.01, H=50.0, zeta=0.1, tau=1.0, beta=2.0,
                  rho_max=1.0, rho_star=0.5, M0=1.0)
    sim = SimParams(N=80, L=2.0, T=200.0, dt=5e-4,
                    store_every=50, snapshot_every=500)
    outdir = Path(__file__).parent / "v1.1_nonlinear_regime"
    outdir.mkdir(exist_ok=True)
    out = outdir / "analogue5_H50_nonlinear.npz"
    # v1.1b: wider bump so spatial gradient persists during oscillation
    run(ep, sim, ic_amplitude=0.45, ic_sigma=0.30,
        outpath=outdir / "analogue5_H50_nonlinear_wide.npz",
        verbose=True)
