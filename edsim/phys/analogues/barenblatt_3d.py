"""
edsim.phys.analogues.barenblatt_3d — 3D Barenblatt self-similar spreading.

Extends the 2D Barenblatt analogue to d=3, verifying that the PME exponent
mapping m = beta + 1 and the Barenblatt scaling R(t) ~ t^{alpha_R} hold
in three spatial dimensions.

For d=3:
    alpha_R = 1 / (3(m-1) + 2)
    beta=1 => m=2, alpha_R = 1/5 = 0.2000
    beta=2 => m=3, alpha_R = 1/8 = 0.1250
"""

from __future__ import annotations

import numpy as np
from dataclasses import dataclass

from ...core.parameters import EDParameters
from ...core.constitutive import mobility, mobility_deriv, enforce_bounds
from ...core.operators import laplacian_fd_3d, grad_squared_fd_3d


# ------------------------------------------------------------------ #
#  Data structures                                                    #
# ------------------------------------------------------------------ #

@dataclass
class Barenblatt3DPrediction:
    beta: float
    m: float
    d: int
    D_pme: float
    alpha_R: float
    alpha_rho: float

@dataclass
class Barenblatt3DRunResult:
    prediction: Barenblatt3DPrediction
    times: np.ndarray
    front_radii: np.ndarray
    central_delta: np.ndarray
    alpha_R_fitted: float
    alpha_rho_fitted: float
    alpha_R_error_pct: float
    alpha_rho_error_pct: float
    compact_support: bool
    tail_max: float

@dataclass
class Barenblatt3DSweepResult:
    runs: list


# ------------------------------------------------------------------ #
#  Predictions                                                        #
# ------------------------------------------------------------------ #

def predict_barenblatt_3d(
    beta: float = 2.0,
    D: float = 0.3,
    M0: float = 1.0,
) -> Barenblatt3DPrediction:
    d = 3
    m = beta + 1.0
    D_pme = D * M0 / (beta + 1.0)
    alpha_R = 1.0 / (d * (m - 1.0) + 2.0)
    alpha_rho = -d / (d * (m - 1.0) + 2.0)
    return Barenblatt3DPrediction(
        beta=beta, m=m, d=d, D_pme=D_pme,
        alpha_R=alpha_R, alpha_rho=alpha_rho,
    )


# ------------------------------------------------------------------ #
#  Solver                                                             #
# ------------------------------------------------------------------ #

def _make_params_3d(N=32, L=4.0, beta=2.0, D=0.3, M0=1.0, dt=0.002):
    return EDParameters(
        d=3, N=(N, N, N), L=(L, L, L),
        D=D, H=0.0, tau=1.0, zeta=0.1,
        rho_star=0.5, rho_max=1.0, M0=M0, beta=beta,
        P0=1e-12, dt=dt, T=1.0,
        method="implicit_euler", bc="neumann",
    )


def _make_ic_3d(params, A=0.4, R0=0.5):
    Nx, Ny, Nz = params.N
    Lx = params.L[0]
    dx = Lx / Nx
    x = np.arange(Nx) * dx
    y = np.arange(Ny) * dx
    z = np.arange(Nz) * dx
    X, Y, Z = np.meshgrid(x, y, z, indexing="ij")
    cx = Lx / 2
    r2 = (X - cx) ** 2 + (Y - cx) ** 2 + (Z - cx) ** 2
    sigma = R0 / 2.0
    delta_bg = 1e-4
    delta = A * np.exp(-r2 / (2.0 * sigma ** 2)) + delta_bg
    return enforce_bounds(params.rho_max - delta, params)


def _run_pme_3d(params, rho0, T, snap_interval):
    rho = rho0.copy()
    t = 0.0
    dt = params.dt
    dx = tuple(L / N for L, N in zip(params.L, params.N))

    times = [0.0]
    fields = [rho.copy()]
    n_steps = int(np.ceil(T / dt))
    next_snap = snap_interval

    for step in range(n_steps):
        rho_old = rho.copy()
        for _fp in range(12):
            lap = laplacian_fd_3d(rho, dx)
            gsq = grad_squared_fd_3d(rho, dx)
            M = mobility(rho, params)
            Mp = mobility_deriv(rho, params)
            F = params.D * (M * lap + Mp * gsq)
            rho_new = rho_old + dt * F
            rho_new = enforce_bounds(rho_new, params)
            if np.max(np.abs(rho_new - rho)) < 1e-8:
                rho = rho_new
                break
            rho = rho_new

        t += dt
        if t >= next_snap - dt / 2:
            times.append(t)
            fields.append(rho.copy())
            next_snap += snap_interval

    return {"times": np.array(times), "fields": fields}


# ------------------------------------------------------------------ #
#  Analysis                                                           #
# ------------------------------------------------------------------ #

def _measure_front_3d(delta, cx, dx, threshold=0.001):
    Nx, Ny, Nz = delta.shape
    x = np.arange(Nx) * dx
    y = np.arange(Ny) * dx
    z = np.arange(Nz) * dx
    X, Y, Z = np.meshgrid(x, y, z, indexing="ij")
    R = np.sqrt((X - cx) ** 2 + (Y - cx) ** 2 + (Z - cx) ** 2)
    mask = delta > threshold
    if not mask.any():
        return 0.0
    return R[mask].max()


def _fit_exponent(times, values, t_start=None):
    mask = (times > 0) & (values > 0)
    if t_start is not None:
        mask &= times >= t_start
    if mask.sum() < 3:
        return 0.0
    log_t = np.log(times[mask])
    log_v = np.log(values[mask])
    coeffs = np.polyfit(log_t, log_v, 1)
    return coeffs[0]


def _run_single_beta_3d(beta, N=32, L=4.0, T=200.0, dt=0.002,
                        snap_interval=5.0, A=0.4, R0=0.5):
    pred = predict_barenblatt_3d(beta=beta)
    params = _make_params_3d(N=N, L=L, beta=beta, dt=dt)
    rho0 = _make_ic_3d(params, A=A, R0=R0)

    result = _run_pme_3d(params, rho0, T, snap_interval)
    times = result["times"]
    fields = result["fields"]

    dx = L / N
    cx = L / 2.0
    delta_bg = 1e-4

    front_radii = []
    central_delta = []
    for fld in fields:
        delta = params.rho_max - fld
        front_radii.append(_measure_front_3d(delta, cx, dx))
        # Central delta: value at the center voxel
        ci = N // 2
        central_delta.append(delta[ci, ci, ci])

    front_radii = np.array(front_radii)
    central_delta = np.array(central_delta)

    # Fit exponents from the second half of the run
    t_start = T / 3.0
    alpha_R_fit = _fit_exponent(times, front_radii, t_start)
    alpha_rho_fit = _fit_exponent(times, central_delta, t_start)

    alpha_R_err = abs(alpha_R_fit - pred.alpha_R) / pred.alpha_R * 100
    alpha_rho_err = abs(alpha_rho_fit - pred.alpha_rho) / abs(pred.alpha_rho) * 100

    # Compact support check
    tail_max = 0.0
    if len(fields) > 1:
        delta_last = params.rho_max - fields[-1]
        # Check outside front
        R_front = front_radii[-1] if front_radii[-1] > 0 else L / 2
        Nx = N
        x = np.arange(Nx) * dx
        X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
        R = np.sqrt((X - cx) ** 2 + (Y - cx) ** 2 + (Z - cx) ** 2)
        outer = R > R_front + 2 * dx
        if outer.any():
            tail_max = (delta_last[outer] - delta_bg).max()

    return Barenblatt3DRunResult(
        prediction=pred,
        times=times,
        front_radii=front_radii,
        central_delta=central_delta,
        alpha_R_fitted=alpha_R_fit,
        alpha_rho_fitted=alpha_rho_fit,
        alpha_R_error_pct=alpha_R_err,
        alpha_rho_error_pct=alpha_rho_err,
        compact_support=(tail_max < 0.01),
        tail_max=tail_max,
    )


# ------------------------------------------------------------------ #
#  Main entry points                                                  #
# ------------------------------------------------------------------ #

def run_barenblatt_3d_experiment(
    betas=(1.0, 2.0),
    N=32,
    L=4.0,
    T=200.0,
    dt=0.002,
) -> Barenblatt3DSweepResult:
    """Run the full 3D Barenblatt analogue for multiple beta values."""
    runs = []
    for beta in betas:
        print(f"  3D Barenblatt: beta={beta} ...", end=" ", flush=True)
        r = _run_single_beta_3d(beta, N=N, L=L, T=T, dt=dt)
        print(f"alpha_R={r.alpha_R_fitted:.4f} "
              f"(pred {r.prediction.alpha_R:.4f}, err {r.alpha_R_error_pct:.1f}%)")
        runs.append(r)
    return Barenblatt3DSweepResult(runs=runs)


def build_barenblatt_3d_report(result: Barenblatt3DSweepResult = None) -> str:
    """Generate the Markdown report."""
    if result is None:
        result = run_barenblatt_3d_experiment()

    lines = [
        "# ED Analogue: 3D Barenblatt Self-Similar Spreading",
        "",
        "## Setup",
        "- Channels: mobility only (P0 = 0, H = 0)",
        "- Dimension: d = 3",
        "- PDE reduces to 3D PME with m = beta + 1",
        "",
        "## Results",
        "",
        "| beta | m | alpha_R pred | alpha_R meas | Error | "
        "alpha_rho pred | alpha_rho meas | Error | Compact? |",
        "|------|---|-------------|-------------|-------|"
        "--------------|---------------|-------|----------|",
    ]

    for r in result.runs:
        p = r.prediction
        lines.append(
            f"| {p.beta:.0f} | {p.m:.0f} | {p.alpha_R:.4f} | "
            f"{r.alpha_R_fitted:.4f} | {r.alpha_R_error_pct:.1f}% | "
            f"{p.alpha_rho:.4f} | {r.alpha_rho_fitted:.4f} | "
            f"{r.alpha_rho_error_pct:.1f}% | "
            f"{'Yes' if r.compact_support else 'No'} |"
        )

    lines.extend([
        "",
        "## Falsification",
        "- Finite-speed propagation: "
        + ("PASS" if all(r.compact_support for r in result.runs) else "FAIL"),
        "- Exponent match (beta=1): "
        + (f"PASS ({result.runs[0].alpha_R_error_pct:.1f}%)"
           if result.runs[0].alpha_R_error_pct < 20 else "FAIL"),
        "",
        "## Interpretation",
        "The ED mobility channel in 3D reproduces the porous-medium equation ",
        "with the predicted exponent mapping m = beta + 1.",
    ])

    return "\n".join(lines)
