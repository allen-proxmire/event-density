"""
Solver 2: Method-of-Lines + scipy.integrate.solve_ivp (BDF, adaptive).

Mathematical setup
------------------
Same PDE as Solver 1, but discretized in space via standard finite differences
(5-point Laplacian + central differences for gradient) with PERIODIC BC,
producing an N^2 + 1 dimensional ODE system. scipy handles the time integration
adaptively using BDF (backward-differentiation formula, implicit multistep).

Why BDF
-------
BDF is L-stable and well-suited to stiff problems. Critically, it uses an
internal error estimator to adapt the time step, and a modified-Newton iteration
at each step, so it makes very different algorithmic choices than ETDRK2.
Agreement between ETDRK2 and BDF on the measured omega is strong evidence of
solver-independence.

State vector layout
-------------------
y = [rho_flat (N^2 entries), v (1 entry)]      total size N^2 + 1

RHS(y, t)
---------
1. Reshape rho_flat -> rho 2D
2. Compute d = rho_max - rho (clamp nonneg), M = M0 * d^beta, Mprime = -beta*M0*d^(beta-1)
3. Laplacian, grad_x, grad_y via 5-pt / central diff with np.roll (periodic)
4. F[rho] = M * lap + Mprime * |grad|^2 - P0 * (rho - rho*)
5. drho/dt = D * F + H * v
6. dv/dt = (F.mean() - zeta * v) / tau
7. Return flat drho/dt concatenated with dv/dt

Jacobian sparsity
-----------------
To speed up BDF, provide jac_sparsity: each rho_i point depends on its 5 stencil
neighbours + v (coupling via +H*v). v depends on all rho (through mean). Sparsity
of dF/dy: block structure with ~6 nonzeros per rho-row + 1 v-coupling column
+ 1 row (for dv/dt) that is dense in rho.

Runtime
-------
Slower than explicit or spectral for this problem because the adaptive implicit
solver has high constant factors. Expected ~1-3 min per H at T=200.
"""

import numpy as np
from dataclasses import dataclass, asdict
from pathlib import Path
from scipy.integrate import solve_ivp
from scipy.sparse import lil_matrix, csr_matrix


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
    store_dt: float = 0.05         # output cadence
    snapshot_dt: float = 1.0


def initial_condition(sim: SimParams, ep: EDParams, amplitude=0.2, sigma=0.15):
    N, L = sim.N, sim.L
    x = np.linspace(0.0, L, N, endpoint=False)
    y = np.linspace(0.0, L, N, endpoint=False)
    X, Y = np.meshgrid(x, y, indexing="ij")
    r2 = (X - L / 2.0) ** 2 + (Y - L / 2.0) ** 2
    bump = np.exp(-r2 / (2.0 * sigma * sigma))
    rho0 = ep.rho_star - amplitude * bump
    rho0 = np.clip(rho0, 0.0, ep.rho_max * 0.999)
    return rho0, x, y


def predict_linear(ep: EDParams):
    gamma = (ep.D * ep.P0 + ep.zeta / ep.tau) / 2.0
    omega0_sq = (ep.D * ep.P0 * ep.zeta + ep.H * ep.P0) / ep.tau
    disc = omega0_sq - gamma * gamma
    omega = np.sqrt(disc) if disc > 0 else 0.0
    return dict(gamma=gamma, omega0_sq=omega0_sq, omega=omega,
                period=(2 * np.pi / omega) if omega > 0 else np.inf)


def make_rhs(ep: EDParams, N: int, dx: float):
    """Factory returning the RHS function for solve_ivp."""
    inv_dx = 1.0 / dx
    inv_dx2 = inv_dx * inv_dx

    def rhs(t, y):
        rho = y[:-1].reshape(N, N)
        v = y[-1]
        # Periodic finite differences
        lap = ((np.roll(rho, 1, axis=0) + np.roll(rho, -1, axis=0)
                + np.roll(rho, 1, axis=1) + np.roll(rho, -1, axis=1)
                - 4.0 * rho) * inv_dx2)
        grad_x = (np.roll(rho, -1, axis=0) - np.roll(rho, 1, axis=0)) * (0.5 * inv_dx)
        grad_y = (np.roll(rho, -1, axis=1) - np.roll(rho, 1, axis=1)) * (0.5 * inv_dx)
        grad_sq = grad_x * grad_x + grad_y * grad_y

        d = np.maximum(ep.rho_max - rho, 0.0)
        M = ep.M0 * d ** ep.beta
        Mprime = -ep.beta * ep.M0 * d ** (ep.beta - 1.0)
        P = ep.P0 * (rho - ep.rho_star)
        F = M * lap + Mprime * grad_sq - P

        drho_dt = ep.D * F + ep.H * v
        dv_dt = (F.mean() - ep.zeta * v) / ep.tau

        dy = np.empty_like(y)
        dy[:-1] = drho_dt.ravel()
        dy[-1] = dv_dt
        return dy

    return rhs


def make_jac_sparsity(N: int):
    """Build sparsity pattern for Jacobian: rho-rho block pentadiagonal + rho-v column
    + v-rho row (dense) + v-v scalar."""
    n_rho = N * N
    n_total = n_rho + 1
    jac = lil_matrix((n_total, n_total), dtype=bool)

    # rho rows: each rho_i depends on itself + 4 periodic neighbours + v
    for i in range(N):
        for j in range(N):
            idx = i * N + j
            # self
            jac[idx, idx] = True
            # neighbours (periodic)
            jac[idx, ((i + 1) % N) * N + j] = True
            jac[idx, ((i - 1) % N) * N + j] = True
            jac[idx, i * N + ((j + 1) % N)] = True
            jac[idx, i * N + ((j - 1) % N)] = True
            # coupling to v
            jac[idx, n_rho] = True

    # v-rho row: v depends on F.mean() which depends on all rho
    jac[n_rho, :] = True
    jac[n_rho, n_rho] = True
    return csr_matrix(jac)


def run(ep: EDParams, sim: SimParams, ic_amplitude=0.2, ic_sigma=0.15,
        outpath=None, verbose=True, method="BDF", rtol=1e-5, atol=1e-8):
    N, L = sim.N, sim.L
    dx = L / N
    n_rho = N * N

    rho0, x_arr, y_arr = initial_condition(sim, ep, ic_amplitude, ic_sigma)
    y0 = np.concatenate([rho0.ravel(), [0.0]])

    rhs = make_rhs(ep, N, dx)
    jac_sp = make_jac_sparsity(N)

    t_eval_scalar = np.arange(0, sim.T + 1e-9, sim.store_dt)
    linpred = predict_linear(ep)

    if verbose:
        print(f"[MOL-BDF] N={N}, dx={dx:.4f}, T={sim.T}, method={method}, rtol={rtol}")
        print(f"  Linear prediction: omega={linpred['omega']:.4f} period={linpred['period']:.2f}")
        print(f"  System size: {n_rho + 1} ODEs")

    sol = solve_ivp(rhs, (0.0, sim.T), y0, method=method,
                    t_eval=t_eval_scalar, rtol=rtol, atol=atol,
                    jac_sparsity=jac_sp, vectorized=False)

    if verbose:
        print(f"  nfev={sol.nfev}, njev={sol.njev}, nlu={sol.nlu}, "
              f"status={sol.status}, message={sol.message}")

    t_hist = sol.t
    rho_hist = sol.y[:-1, :].reshape(N, N, -1)          # (N, N, nT)
    v_hist = sol.y[-1, :]
    center_ix = N // 2
    rho_center_hist = rho_hist[center_ix, center_ix, :]
    rho_mean_hist = rho_hist.mean(axis=(0, 1))
    Fbar_hist = np.zeros_like(t_hist)        # left blank; can re-derive if needed

    # Downsample snapshots
    snap_stride = max(1, int(sim.snapshot_dt / sim.store_dt))
    t_snap = t_hist[::snap_stride]
    rho_snap = np.moveaxis(rho_hist[:, :, ::snap_stride], -1, 0).astype(np.float32)

    meta = {"ed_params": asdict(ep), "sim_params": asdict(sim),
            "ic_amplitude": ic_amplitude, "ic_sigma": ic_sigma,
            "linpred": linpred, "solver": "MOL_BDF", "BC": "periodic",
            "rtol": rtol, "atol": atol, "nfev": int(sol.nfev),
            "njev": int(sol.njev), "nlu": int(sol.nlu)}

    if outpath is not None:
        Path(outpath).parent.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(outpath,
                            v_hist=v_hist, t_hist=t_hist,
                            rho_center_hist=rho_center_hist,
                            rho_mean_hist=rho_mean_hist,
                            Fbar_hist=Fbar_hist,
                            rho_snap=rho_snap, t_snap=t_snap,
                            x=x_arr, y=y_arr, meta_json=str(meta))
        if verbose:
            print(f"  Saved {outpath}  ({Path(outpath).stat().st_size/1e6:.2f} MB)")

    return dict(v_hist=v_hist, t_hist=t_hist,
                rho_center_hist=rho_center_hist,
                rho_mean_hist=rho_mean_hist,
                Fbar_hist=Fbar_hist,
                rho_snap=rho_snap, t_snap=t_snap,
                x=x_arr, y=y_arr, meta=meta, linpred=linpred)
