"""
Solver 1: Spectral ETDRK2 for the ED PDE.

Mathematical setup
------------------
Full PDE (periodic BC, 2D):
    dt rho = D * [ M(rho) Lap(rho) + M'(rho) |grad rho|^2 - P(rho) ] + H * v
    dt v   = (1/tau) ( mean(F[rho]) - zeta * v )

where M(rho) = M0 * (rho_max - rho)^beta and P(rho) = P0 * (rho - rho_star).

Splitting for ETDRK2
--------------------
Linear part (constant-coefficient, exact integrating factor in Fourier):
    L[rho] = D * Mbar * Lap(rho) - D * P0 * (rho - rho_star)
    where Mbar = M(rho_star) = (rho_max - rho_star)^beta    (constant reference mobility)

Nonlinear part (everything else):
    N[rho, v] = D * ( M(rho) - Mbar ) * Lap(rho) + D * M'(rho) * |grad(rho)|^2 + H * v

In Fourier space, L is diagonal:
    L_hat(k) = - D * Mbar * |k|^2 - D * P0       (note: constant shift -D*P0*rho_star goes into N)

We re-center to handle the constant forcing:
    Let eta = rho - rho_star.
    Then L[eta] = D * Mbar * Lap(eta) - D * P0 * eta             (homogeneous)
         N[eta, v] = D * ( M(rho) - Mbar ) * Lap(eta) + D * M'(rho) * |grad(eta)|^2 + H * v
                     (no shift needed; rho_max - rho = (rho_max - rho_star) - eta)

ETDRK2 step for dt with linear operator L (diagonal lambda_k) and nonlinear N:
    Let phi1(z) = (e^z - 1) / z                     (ETD coefficient)
    Let phi2(z) = (e^z - 1 - z) / z^2
    E  = exp(lambda * dt)
    a  = eta_n + dt * phi1(lambda*dt) * N(eta_n, v_n)
    N_a = N(a, v_n_half)                             (nonlinear evaluated at predictor)
    eta_{n+1} = E * eta_n + dt * ( phi1(lambda*dt) - 2*phi2(lambda*dt) ) * N(eta_n, v_n)
              + 2 * dt * phi2(lambda*dt) * N_a

For participation v, use linear-exact step because it is a scalar ODE:
    v_dot = (Fbar - zeta v) / tau
    If Fbar approximately constant over dt:
        v_{n+1} = v_n * exp(-zeta*dt/tau) + (Fbar/zeta) * (1 - exp(-zeta*dt/tau))
    Use midpoint Fbar from eta_n and eta_{n+1} for better accuracy.

Note on coefficient functions for lambda -> 0:
    phi1(0) = 1, phi2(0) = 1/2.
    Use series expansion when |lambda*dt| < 1e-4 to avoid cancellation.

BC
---
Periodic. Means the domain wraps; initial Gaussian bump centered at (L/2, L/2)
should be far from boundaries to avoid wraparound contamination.

References
----------
Cox & Matthews (2002), Kassam & Trefethen (2005) for ETDRK2/ETDRK4 on PDEs with
constant-coefficient stiff linear operators and smooth nonlinearities.
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
    dt: float = 0.02
    store_every: int = 1
    snapshot_every: int = 25


def etd_phi1(z):
    """phi1(z) = (e^z - 1)/z. Stable for small z via series."""
    out = np.empty_like(z, dtype=np.float64)
    small = np.abs(z) < 1e-4
    out[~small] = (np.exp(z[~small]) - 1) / z[~small]
    zs = z[small]
    out[small] = 1 + zs / 2 + zs * zs / 6 + zs ** 3 / 24
    return out


def etd_phi2(z):
    """phi2(z) = (e^z - 1 - z)/z^2. Stable for small z via series."""
    out = np.empty_like(z, dtype=np.float64)
    small = np.abs(z) < 1e-4
    out[~small] = (np.exp(z[~small]) - 1 - z[~small]) / (z[~small] ** 2)
    zs = z[small]
    out[small] = 0.5 + zs / 6 + zs * zs / 24 + zs ** 3 / 120
    return out


def compute_nonlinear(eta, v, ep: EDParams, kx2_plus_ky2, kx, ky):
    """Compute N[eta, v] in real space, using FFT for derivatives.

    eta = rho - rho_star  (centered)
    rho = eta + rho_star
    rho_max - rho = (rho_max - rho_star) - eta
    """
    d_star = ep.rho_max - ep.rho_star         # constant
    Mbar = ep.M0 * d_star ** ep.beta          # reference mobility
    d = np.maximum(d_star - eta, 0.0)
    M = ep.M0 * d ** ep.beta
    Mprime = -ep.beta * ep.M0 * d ** (ep.beta - 1.0)

    # Derivatives via spectral
    eta_hat = np.fft.fft2(eta)
    # Laplacian: FFT -> multiply by -(kx^2+ky^2), iFFT
    lap_hat = -kx2_plus_ky2 * eta_hat
    lap = np.real(np.fft.ifft2(lap_hat))
    dx = np.real(np.fft.ifft2(1j * kx * eta_hat))
    dy = np.real(np.fft.ifft2(1j * ky * eta_hat))
    grad_sq = dx * dx + dy * dy

    # Variable-coefficient correction + gradient term + participation
    N = ep.D * (M - Mbar) * lap + ep.D * Mprime * grad_sq + ep.H * v
    return N, lap, M


def compute_Fbar(eta, v, ep: EDParams, kx2_plus_ky2, kx, ky):
    """Compute domain-averaged F[rho] for participation ODE."""
    d_star = ep.rho_max - ep.rho_star
    d = np.maximum(d_star - eta, 0.0)
    M = ep.M0 * d ** ep.beta
    Mprime = -ep.beta * ep.M0 * d ** (ep.beta - 1.0)

    eta_hat = np.fft.fft2(eta)
    lap = np.real(np.fft.ifft2(-kx2_plus_ky2 * eta_hat))
    dx = np.real(np.fft.ifft2(1j * kx * eta_hat))
    dy = np.real(np.fft.ifft2(1j * ky * eta_hat))
    grad_sq = dx * dx + dy * dy

    P = ep.P0 * eta   # since P = P0*(rho - rho_star) = P0*eta
    F = M * lap + Mprime * grad_sq - P
    return F.mean()


def initial_condition(sim: SimParams, ep: EDParams, amplitude=0.2, sigma=0.15):
    N, L = sim.N, sim.L
    x = np.linspace(0.0, L, N, endpoint=False)   # periodic: last pt omitted
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


def run(ep: EDParams, sim: SimParams, ic_amplitude=0.2, ic_sigma=0.15,
        outpath=None, verbose=True):
    N, L = sim.N, sim.L
    dx = L / N

    # Fourier wavenumbers
    kx_1d = 2 * np.pi * np.fft.fftfreq(N, d=dx)
    ky_1d = 2 * np.pi * np.fft.fftfreq(N, d=dx)
    KX, KY = np.meshgrid(kx_1d, ky_1d, indexing="ij")
    K2 = KX * KX + KY * KY

    # Linear operator eigenvalue at each Fourier mode
    d_star = ep.rho_max - ep.rho_star
    Mbar = ep.M0 * d_star ** ep.beta
    Lambda = -ep.D * Mbar * K2 - ep.D * ep.P0    # shape (N, N)

    dt = sim.dt
    E = np.exp(Lambda * dt)
    Ldt = Lambda * dt
    phi1 = etd_phi1(Ldt)
    phi2 = etd_phi2(Ldt)

    # Initial condition
    rho, x_arr, y_arr = initial_condition(sim, ep, ic_amplitude, ic_sigma)
    eta = rho - ep.rho_star
    v = 0.0

    n_steps = int(sim.T / dt)
    n_scalar = n_steps // sim.store_every + 1
    n_snap = n_steps // sim.snapshot_every + 1

    v_hist = np.zeros(n_scalar)
    t_hist = np.zeros(n_scalar)
    rho_center_hist = np.zeros(n_scalar)
    rho_mean_hist = np.zeros(n_scalar)
    Fbar_hist = np.zeros(n_scalar)
    rho_snap = np.zeros((n_snap, N, N), dtype=np.float32)
    t_snap = np.zeros(n_snap)

    center_ix = N // 2

    v_hist[0] = 0.0
    rho_center_hist[0] = rho[center_ix, center_ix]
    rho_mean_hist[0] = rho.mean()
    rho_snap[0] = rho.astype(np.float32)
    scalar_idx = 1
    snap_idx = 1

    linpred = predict_linear(ep)
    if verbose:
        print(f"[spectral-ETDRK2] N={N}, dx={dx:.4f}, dt={dt}, T={sim.T}")
        print(f"  Linear prediction: omega={linpred['omega']:.4f} period={linpred['period']:.2f}")
        print(f"  Mbar (reference mobility at rho*) = {Mbar:.4f}")
        print(f"  Total steps: {n_steps}")

    for step in range(1, n_steps + 1):
        # Nonlinear evaluation at current state
        N_n, _, _ = compute_nonlinear(eta, v, ep, K2, KX, KY)

        # Fourier-space ETDRK2 step:
        eta_hat = np.fft.fft2(eta)
        N_n_hat = np.fft.fft2(N_n)

        # Predictor: a = E * eta + dt * phi1 * N_n  (in Fourier)
        a_hat = E * eta_hat + dt * phi1 * N_n_hat
        a_real = np.real(np.fft.ifft2(a_hat))

        # Update v from its own ODE (use current Fbar; Heun-like average)
        Fbar_n = compute_Fbar(eta, v, ep, K2, KX, KY)
        # Explicit Euler on v over half step
        v_half = v + (0.5 * dt) * (Fbar_n - ep.zeta * v) / ep.tau
        # Full explicit update using predictor's Fbar
        Fbar_a = compute_Fbar(a_real, v_half, ep, K2, KX, KY)
        v_new = v + dt * (0.5 * (Fbar_n + Fbar_a) - ep.zeta * v) / ep.tau

        # Corrector: nonlinear at predictor
        N_a, _, _ = compute_nonlinear(a_real, v_new, ep, K2, KX, KY)
        N_a_hat = np.fft.fft2(N_a)

        # Corrector step
        eta_hat_new = (E * eta_hat
                        + dt * (phi1 - 2 * phi2) * N_n_hat
                        + 2 * dt * phi2 * N_a_hat)
        eta_new = np.real(np.fft.ifft2(eta_hat_new))

        # Clamp rho to physical range
        rho_new = np.clip(eta_new + ep.rho_star, 0.0, ep.rho_max * 0.9999)
        eta = rho_new - ep.rho_star
        v = v_new

        # Storage
        if step % sim.store_every == 0 and scalar_idx < n_scalar:
            v_hist[scalar_idx] = v
            t_hist[scalar_idx] = step * dt
            rho_center_hist[scalar_idx] = rho_new[center_ix, center_ix]
            rho_mean_hist[scalar_idx] = rho_new.mean()
            Fbar_hist[scalar_idx] = Fbar_a
            scalar_idx += 1

        if step % sim.snapshot_every == 0 and snap_idx < n_snap:
            rho_snap[snap_idx] = rho_new.astype(np.float32)
            t_snap[snap_idx] = step * dt
            snap_idx += 1

        if verbose and step % max(1, n_steps // 10) == 0:
            print(f"  t={step*dt:6.1f}  v={v:+.5e}  rho_c={rho_new[center_ix, center_ix]:.4f}"
                  f"  mean-rho*={rho_new.mean()-ep.rho_star:+.3e}")

    v_hist = v_hist[:scalar_idx]
    t_hist = t_hist[:scalar_idx]
    rho_center_hist = rho_center_hist[:scalar_idx]
    rho_mean_hist = rho_mean_hist[:scalar_idx]
    Fbar_hist = Fbar_hist[:scalar_idx]
    rho_snap = rho_snap[:snap_idx]
    t_snap = t_snap[:snap_idx]

    meta = {"ed_params": asdict(ep), "sim_params": asdict(sim),
            "ic_amplitude": ic_amplitude, "ic_sigma": ic_sigma,
            "linpred": linpred, "solver": "spectral_ETDRK2", "BC": "periodic"}

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
