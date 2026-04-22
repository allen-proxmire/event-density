"""
v1.2 H-sweep run.

Runs three simulations at H=10, 20, 50 in the linear regime (amp=0.2, sigma=0.15,
same as canonical v1.0 but varying H). Extracts peak omega from each and produces
an omega(H) scaling plot.

Linear prediction:  omega = sqrt((D*P0*zeta + H*P0)/tau - gamma^2)
                    with gamma = (D*P0 + zeta/tau)/2 = 0.0515
"""

from pathlib import Path
from ed_solver_2d import EDParams, SimParams, run, predict_linear

if __name__ == "__main__":
    outdir = Path(__file__).parent / "v1.2_H_sweep"
    outdir.mkdir(exist_ok=True)

    for H in [10.0, 20.0, 50.0]:
        print(f"\n===== H = {H} =====")
        ep = EDParams(D=0.3, P0=0.01, H=H, zeta=0.1, tau=1.0, beta=2.0,
                      rho_max=1.0, rho_star=0.5, M0=1.0)
        sim = SimParams(N=80, L=2.0, T=200.0, dt=5e-4,
                        store_every=50, snapshot_every=500)
        out = outdir / f"analogue5_H{int(H):02d}.npz"
        run(ep, sim, ic_amplitude=0.2, ic_sigma=0.15,
            outpath=out, verbose=True)
    print("\n===== H-sweep complete =====")
