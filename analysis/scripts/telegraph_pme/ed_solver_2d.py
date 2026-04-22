"""
Minimal 2D ED PDE solver for the telegraph-modulated PME (Analogue 5).

Canonical ED PDE:
    dt rho = D * [ M(rho) * Laplacian(rho) + M'(rho) * |grad rho|^2 - P(rho) ] + H * v
    dt v   = (1/tau) * ( mean(F[rho]) - zeta * v )

with:
    M(rho) = M0 * (rho_max - rho)^beta          (canonical M0=1, beta=2)
    P(rho) = P0 * (rho - rho_star)               (linear penalty)
    F[rho] = M(rho) * Laplacian(rho) + M'(rho) * |grad rho|^2 - P(rho)

Explicit Euler, 5-point Laplacian, Neumann BC via mirror padding.

Two storage rates:
  * `store_every` samples scalar time-series (v, rho_center, rho_mean, Fbar) frequently
  * `snapshot_every` saves the full rho field at a coarser rate

Output: compressed .npz with arrays + metadata.
"""

import numpy as np
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class EDParams:
    M0: float = 1.0
    beta: float = 2.0
    rho_max: float = 1.0
    P0: float = 0.01
    rho_star: float = 0.5
    H: float = 50.0
    zeta: float = 0.1
    tau: float = 1.0
    D: float = 0.3


@dataclass
class SimParams:
    N: int = 80
    L: float = 2.0
    T: float = 200.0
    dt: float = 5e-4
    store_every: int = 50       # scalar time-series cadence
    snapshot_every: int = 500   # full-field snapshot cadence
    seed: int = 0


def neumann_pad(a):
    return np.pad(a, 1, mode="edge")


def laplacian_5pt(rho, dx):
    rp = neumann_pad(rho)
    return (rp[2:, 1:-1] + rp[:-2, 1:-1] + rp[1:-1, 2:] + rp[1:-1, :-2]
            - 4.0 * rp[1:-1, 1:-1]) / (dx * dx)


def grad_squared(rho, dx):
    rp = neumann_pad(rho)
    dxv = (rp[1:-1, 2:] - rp[1:-1, :-2]) / (2.0 * dx)
    dyv = (rp[2:, 1:-1] - rp[:-2, 1:-1]) / (2.0 * dx)
    return dxv * dxv + dyv * dyv


def compute_F(rho, ep: EDParams, dx):
    d = np.maximum(ep.rho_max - rho, 0.0)
    M = ep.M0 * d ** ep.beta
    # M'(rho) = d/drho [M0 * (rho_max - rho)^beta] = -beta*M0*(rho_max - rho)^(beta-1)
    Mprime = -ep.beta * ep.M0 * d ** (ep.beta - 1.0)
    lap = laplacian_5pt(rho, dx)
    gsq = grad_squared(rho, dx)
    P = ep.P0 * (rho - ep.rho_star)
    return M * lap + Mprime * gsq - P


def initial_condition(sim: SimParams, ep: EDParams, amplitude=0.2, sigma=0.15):
    """Gaussian depression centered in domain."""
    N, L = sim.N, sim.L
    x = np.linspace(0.0, L, N)
    y = np.linspace(0.0, L, N)
    X, Y = np.meshgrid(x, y, indexing="ij")
    r2 = (X - L / 2.0) ** 2 + (Y - L / 2.0) ** 2
    bump = np.exp(-r2 / (2.0 * sigma * sigma))
    rho0 = ep.rho_star - amplitude * bump
    rho0 = np.clip(rho0, 0.0, ep.rho_max * 0.999)
    return rho0, x, y


def predict_linear(ep: EDParams):
    """Linearized eigenmode prediction for (delta, v) around (rho_star, 0)."""
    gamma = (ep.D * ep.P0 + ep.zeta / ep.tau) / 2.0
    omega0_sq = (ep.D * ep.P0 * ep.zeta + ep.H * ep.P0) / ep.tau
    disc = omega0_sq - gamma * gamma
    if disc > 0:
        omega = np.sqrt(disc)
        regime = "underdamped"
    else:
        omega = 0.0
        regime = "overdamped"
    return dict(gamma=gamma, omega0_sq=omega0_sq, omega=omega, regime=regime,
                period=(2 * np.pi / omega) if omega > 0 else np.inf,
                Q=omega / (2 * gamma) if gamma > 0 else np.inf)


def run(ep: EDParams, sim: SimParams, ic_amplitude=0.2, ic_sigma=0.15,
        outpath=None, verbose=True):
    dx = sim.L / (sim.N - 1)
    n_steps = int(sim.T / sim.dt)

    rho, x_arr, y_arr = initial_condition(sim, ep, ic_amplitude, ic_sigma)
    v = 0.0

    n_scalar = n_steps // sim.store_every + 1
    n_snap = n_steps // sim.snapshot_every + 1

    v_hist = np.zeros(n_scalar, dtype=np.float64)
    t_hist = np.zeros(n_scalar, dtype=np.float64)
    rho_center_hist = np.zeros(n_scalar, dtype=np.float64)
    rho_mean_hist = np.zeros(n_scalar, dtype=np.float64)
    Fbar_hist = np.zeros(n_scalar, dtype=np.float64)
    rho_snap = np.zeros((n_snap, sim.N, sim.N), dtype=np.float32)
    t_snap = np.zeros(n_snap, dtype=np.float64)

    center_ix = sim.N // 2

    # t = 0 record
    v_hist[0] = v
    t_hist[0] = 0.0
    rho_center_hist[0] = rho[center_ix, center_ix]
    rho_mean_hist[0] = rho.mean()
    Fbar_hist[0] = 0.0
    rho_snap[0] = rho.astype(np.float32)
    t_snap[0] = 0.0
    scalar_idx = 1
    snap_idx = 1

    linpred = predict_linear(ep)
    D_eff_max = ep.D * ep.M0 * ep.rho_max ** ep.beta
    cfl = D_eff_max * sim.dt / (dx * dx)

    if verbose:
        print(f"Grid: {sim.N}x{sim.N}, dx={dx:.4f}, dt={sim.dt:.4e}, T={sim.T}")
        print(f"CFL (worst-case max mobility): {cfl:.3f}")
        print(f"Linearized prediction: omega={linpred['omega']:.4f}, "
              f"period={linpred['period']:.2f}, gamma={linpred['gamma']:.4f}, "
              f"Q={linpred['Q']:.2f}")
        print(f"Total steps: {n_steps}, scalar samples: {n_scalar}, snapshots: {n_snap}")

    for step in range(1, n_steps + 1):
        F = compute_F(rho, ep, dx)
        Fbar = F.mean()

        rho = rho + sim.dt * (ep.D * F + ep.H * v)
        rho = np.clip(rho, 0.0, ep.rho_max * 0.9999)

        v = v + sim.dt * (Fbar - ep.zeta * v) / ep.tau

        if step % sim.store_every == 0 and scalar_idx < n_scalar:
            v_hist[scalar_idx] = v
            t_hist[scalar_idx] = step * sim.dt
            rho_center_hist[scalar_idx] = rho[center_ix, center_ix]
            rho_mean_hist[scalar_idx] = rho.mean()
            Fbar_hist[scalar_idx] = Fbar
            scalar_idx += 1

        if step % sim.snapshot_every == 0 and snap_idx < n_snap:
            rho_snap[snap_idx] = rho.astype(np.float32)
            t_snap[snap_idx] = step * sim.dt
            snap_idx += 1

        if verbose and step % (n_steps // 10) == 0:
            print(f"  t={step*sim.dt:6.1f}  v={v:+.5f}  rho_c={rho[center_ix, center_ix]:.4f}  "
                  f"mean(rho)-rho*={rho.mean()-ep.rho_star:+.5e}  Fbar={Fbar:+.3e}")

    # Trim
    v_hist = v_hist[:scalar_idx]
    t_hist = t_hist[:scalar_idx]
    rho_center_hist = rho_center_hist[:scalar_idx]
    rho_mean_hist = rho_mean_hist[:scalar_idx]
    Fbar_hist = Fbar_hist[:scalar_idx]
    rho_snap = rho_snap[:snap_idx]
    t_snap = t_snap[:snap_idx]

    meta = {
        "ed_params": asdict(ep),
        "sim_params": asdict(sim),
        "ic_amplitude": ic_amplitude,
        "ic_sigma": ic_sigma,
        "linpred": linpred,
    }

    if outpath is not None:
        Path(outpath).parent.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(outpath,
                            v_hist=v_hist, t_hist=t_hist,
                            rho_center_hist=rho_center_hist,
                            rho_mean_hist=rho_mean_hist,
                            Fbar_hist=Fbar_hist,
                            rho_snap=rho_snap, t_snap=t_snap,
                            x=x_arr, y=y_arr,
                            meta_json=str(meta))
        if verbose:
            print(f"Saved: {outpath}  ({Path(outpath).stat().st_size/1e6:.2f} MB)")

    return dict(v_hist=v_hist, t_hist=t_hist,
                rho_center_hist=rho_center_hist,
                rho_mean_hist=rho_mean_hist,
                Fbar_hist=Fbar_hist,
                rho_snap=rho_snap, t_snap=t_snap,
                x=x_arr, y=y_arr, meta=meta, linpred=linpred)


if __name__ == "__main__":
    ep = EDParams(D=0.3, P0=0.01, H=50.0, zeta=0.1, tau=1.0, beta=2.0,
                  rho_max=1.0, rho_star=0.5, M0=1.0)
    sim = SimParams(N=80, L=2.0, T=200.0, dt=5e-4,
                    store_every=50, snapshot_every=500)
    out = Path(__file__).parent / "analogue5_H50.npz"
    run(ep, sim, ic_amplitude=0.2, ic_sigma=0.15, outpath=out, verbose=True)
