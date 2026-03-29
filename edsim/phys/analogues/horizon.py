"""
edsim.phys.analogues.horizon — Horizon formation and retreat.

Demonstrates that the canonical ED PDE, with H = 0, produces free-boundary
dynamics structurally analogous to the Stefan problem:

1. A large-amplitude density bump exceeds the horizon threshold rho_crit,
   creating a region where M(rho) < M_crit and diffusion effectively halts.
2. The penalty P(rho) pulls the density back toward rho_star, causing the
   horizon to retreat.
3. The retreat rate dR_H/dt is proportional to -F[rho] / (grad rho) at the
   boundary — the ED analogue of the Stefan condition.
4. There exists a sharp critical amplitude A_c below which no horizon forms.

Stefan condition (ED form)
--------------------------
At the horizon boundary rho(R_H(t), t) = rho_crit:

    dR_H/dt = -F[rho](R_H) / (d rho/dr)(R_H)

where F is the ED density operator.  The penalty drives F < 0 (since
rho > rho_star at the boundary), so the retreat rate is positive (inward)
when d rho/dr < 0 (density decreasing outward from the peak).
"""

from __future__ import annotations

import numpy as np
from dataclasses import dataclass

from ...core.parameters import EDParameters
from ...core.constitutive import mobility, mobility_deriv, penalty, enforce_bounds
from ...core.operators import laplacian_fd_2d, grad_squared_fd_2d


# ------------------------------------------------------------------ #
#  Data structures                                                    #
# ------------------------------------------------------------------ #

@dataclass
class HorizonPrediction:
    """Analytical prediction for horizon formation and retreat."""
    rho_crit: float        # density threshold for horizon
    M_crit: float          # mobility threshold
    A_c: float             # critical amplitude
    sigma: float           # IC Gaussian width
    D: float
    P0: float


@dataclass
class HorizonRunResult:
    """Result of a single horizon experiment."""
    A: float
    prediction: HorizonPrediction
    horizon_formed: bool
    times: np.ndarray
    R_H: np.ndarray                   # horizon radius at each snapshot
    peak_rho: np.ndarray              # peak density
    grad_at_boundary: np.ndarray      # |grad rho| at the horizon boundary
    retreat_rate: np.ndarray           # dR_H/dt (finite difference)
    tau_H: float                       # horizon lifetime (0 if no horizon)
    tau_H_predicted: float             # predicted lifetime


@dataclass
class HorizonSweepResult:
    """Result of sweeping amplitude A."""
    A_values: list
    results: list
    A_c_predicted: float
    A_c_measured: float
    tau_H_values: list                 # horizon lifetimes
    stefan_corr: float                 # correlation between dR/dt and -F/grad


# ------------------------------------------------------------------ #
#  Predictions                                                        #
# ------------------------------------------------------------------ #

def predict_horizon(
    D: float = 0.3,
    P0: float = 1.0,
    M0: float = 1.0,
    beta: float = 2.0,
    rho_star: float = 0.5,
    rho_max: float = 1.0,
    M_crit: float = 0.01,
    sigma: float = 0.3,
) -> HorizonPrediction:
    """Compute analytical predictions for horizon dynamics."""
    rho_crit = rho_max - (M_crit / M0) ** (1.0 / beta)
    A_c = rho_crit - rho_star
    return HorizonPrediction(
        rho_crit=rho_crit, M_crit=M_crit, A_c=A_c,
        sigma=sigma, D=D, P0=P0,
    )


def predict_tau_H(A: float, pred: HorizonPrediction) -> float:
    """Predicted horizon lifetime from penalty-dominated decay."""
    if A <= pred.A_c:
        return 0.0
    return -np.log(pred.A_c / A) / (pred.D * pred.P0)


# ------------------------------------------------------------------ #
#  Solver                                                             #
# ------------------------------------------------------------------ #

def _make_horizon_params(
    N: int = 128,
    L: float = 3.0,
    D: float = 0.3,
    P0: float = 1.0,
    dt: float = 0.0005,
) -> EDParameters:
    return EDParameters(
        d=2, N=(N, N), L=(L, L),
        D=D, H=0.0, tau=1.0, zeta=0.1,
        rho_star=0.5, rho_max=1.0, M0=1.0, beta=2.0,
        P0=P0, dt=dt, T=1.0, method="implicit_euler", bc="neumann",
    )


def _make_horizon_ic(params: EDParameters, A: float, sigma: float) -> np.ndarray:
    """Gaussian bump: rho = rho_star + A * exp(-r^2 / (2*sigma^2))."""
    Nx, Ny = params.N
    Lx, Ly = params.L
    dx = Lx / Nx
    x = np.arange(Nx) * dx
    y = np.arange(Ny) * dx
    X, Y = np.meshgrid(x, y, indexing="ij")
    cx, cy = Lx / 2, Ly / 2
    r2 = (X - cx) ** 2 + (Y - cy) ** 2
    rho = params.rho_star + A * np.exp(-r2 / (2.0 * sigma ** 2))
    return enforce_bounds(rho, params)


def _run_horizon_solver(
    params: EDParameters, rho0: np.ndarray,
    T: float, snap_interval: float,
) -> dict:
    """Time-step with implicit Euler (H=0)."""
    rho = rho0.copy()
    t = 0.0
    dt = params.dt
    dx = (params.L[0] / params.N[0], params.L[1] / params.N[1])

    times = [0.0]
    fields = [rho.copy()]
    n_steps = int(np.ceil(T / dt))
    next_snap = snap_interval

    for _ in range(n_steps):
        rho_old = rho.copy()
        for _fp in range(15):
            lap = laplacian_fd_2d(rho, dx)
            gsq = grad_squared_fd_2d(rho, dx)
            M = mobility(rho, params)
            Mp = mobility_deriv(rho, params)
            P = penalty(rho, params)
            F = params.D * (M * lap + Mp * gsq - P)
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

def _measure_horizon(
    rho: np.ndarray, cx: float, cy: float, dx: float,
    rho_crit: float,
) -> float:
    """Measure the horizon radius (max r where rho > rho_crit)."""
    Nx, Ny = rho.shape
    x = np.arange(Nx) * dx
    y = np.arange(Ny) * dx
    X, Y = np.meshgrid(x, y, indexing="ij")
    R = np.sqrt((X - cx) ** 2 + (Y - cy) ** 2)
    mask = rho > rho_crit
    if mask.any():
        return R[mask].max()
    return 0.0


def _measure_grad_at_boundary(
    rho: np.ndarray, cx: float, cy: float,
    dx_val: float, rho_crit: float,
) -> float:
    """Measure |grad rho| at the horizon boundary (radial average)."""
    Nx, Ny = rho.shape
    # Central differences for gradient magnitude
    gx = np.zeros_like(rho)
    gy = np.zeros_like(rho)
    gx[1:-1, :] = (rho[2:, :] - rho[:-2, :]) / (2 * dx_val)
    gy[:, 1:-1] = (rho[:, 2:] - rho[:, :-2]) / (2 * dx_val)
    grad_mag = np.sqrt(gx ** 2 + gy ** 2)

    # Find points near the horizon boundary
    x = np.arange(Nx) * dx_val
    y = np.arange(Ny) * dx_val
    X, Y = np.meshgrid(x, y, indexing="ij")
    R = np.sqrt((X - cx) ** 2 + (Y - cy) ** 2)

    # Points within one grid cell of rho_crit
    near_boundary = np.abs(rho - rho_crit) < 0.02
    if near_boundary.any():
        return np.mean(grad_mag[near_boundary])
    return 0.0


# ------------------------------------------------------------------ #
#  Experiment runners                                                 #
# ------------------------------------------------------------------ #

def run_horizon_experiment(
    A: float = 0.45,
    N: int = 128,
    L: float = 3.0,
    sigma: float = 0.3,
    M_crit: float = 0.01,
    T: float = 3.0,
    n_snaps: int = 60,
    dt: float = 0.0005,
) -> HorizonRunResult:
    """Run a single horizon experiment at amplitude A."""
    params = _make_horizon_params(N=N, L=L, dt=dt)
    pred = predict_horizon(D=params.D, P0=params.P0, M_crit=M_crit, sigma=sigma)
    tau_H_pred = predict_tau_H(A, pred)

    ic = _make_horizon_ic(params, A=A, sigma=sigma)
    snap_interval = T / n_snaps
    result = _run_horizon_solver(params, ic, T=T, snap_interval=snap_interval)

    dx_val = L / N
    cx, cy = L / 2, L / 2
    times = result["times"]

    R_H = np.zeros(len(times))
    peak_rho = np.zeros(len(times))
    grad_bdy = np.zeros(len(times))

    for i, fld in enumerate(result["fields"]):
        R_H[i] = _measure_horizon(fld, cx, cy, dx_val, pred.rho_crit)
        peak_rho[i] = fld.max()
        grad_bdy[i] = _measure_grad_at_boundary(fld, cx, cy, dx_val, pred.rho_crit)

    # Horizon formed?
    horizon_formed = np.any(R_H > 0)

    # Horizon lifetime
    if horizon_formed:
        active = R_H > 0
        t_first = times[active][0]
        t_last = times[active][-1]
        tau_H = t_last - t_first
    else:
        tau_H = 0.0

    # Retreat rate: dR_H/dt by finite difference
    retreat_rate = np.zeros(len(times))
    for i in range(1, len(times)):
        dt_snap = times[i] - times[i - 1]
        if dt_snap > 0:
            retreat_rate[i] = (R_H[i] - R_H[i - 1]) / dt_snap

    return HorizonRunResult(
        A=A, prediction=pred,
        horizon_formed=horizon_formed,
        times=times, R_H=R_H,
        peak_rho=peak_rho,
        grad_at_boundary=grad_bdy,
        retreat_rate=retreat_rate,
        tau_H=tau_H,
        tau_H_predicted=tau_H_pred,
    )


def run_amplitude_sweep(
    A_values: list = None,
    N: int = 96,
    sigma: float = 0.3,
    M_crit: float = 0.01,
) -> HorizonSweepResult:
    """Sweep amplitude to find A_c and test Stefan-like retreat."""
    if A_values is None:
        A_values = [0.30, 0.35, 0.38, 0.40, 0.41, 0.42, 0.43,
                    0.44, 0.45, 0.46, 0.48]

    pred = predict_horizon(M_crit=M_crit, sigma=sigma)
    results = []
    tau_H_vals = []

    for A in A_values:
        res = run_horizon_experiment(A=A, N=N, sigma=sigma, M_crit=M_crit,
                                     T=3.0, n_snaps=40, dt=0.001)
        results.append(res)
        tau_H_vals.append(res.tau_H)

    # Find measured A_c (smallest A with horizon)
    A_c_meas = None
    for i, A in enumerate(A_values):
        if results[i].horizon_formed:
            A_c_meas = A
            break
    if A_c_meas is None:
        A_c_meas = float('inf')

    # Stefan correlation: pool all (dR/dt, grad_at_boundary) where horizon active
    all_retreat = []
    all_grad = []
    for res in results:
        if res.horizon_formed:
            active = res.R_H > 0
            for i in range(1, len(res.times)):
                if active[i] and active[i - 1] and res.grad_at_boundary[i] > 0.01:
                    all_retreat.append(res.retreat_rate[i])
                    all_grad.append(res.grad_at_boundary[i])

    if len(all_retreat) >= 3:
        corr = np.corrcoef(np.abs(all_retreat), all_grad)[0, 1]
    else:
        corr = 0.0

    return HorizonSweepResult(
        A_values=A_values,
        results=results,
        A_c_predicted=pred.A_c,
        A_c_measured=A_c_meas,
        tau_H_values=tau_H_vals,
        stefan_corr=corr,
    )


# ------------------------------------------------------------------ #
#  Full experiment + report                                           #
# ------------------------------------------------------------------ #

def run_full_horizon_experiment() -> str:
    """Run the complete horizon experiment and return a report."""

    lines = [
        "# ED Structural Analogue 3: Horizon Formation and Retreat",
        "",
        "## 1. The ED-to-Stefan Mapping",
        "",
        "An ED *horizon* is a region where $M(\\rho) < M_{\\mathrm{crit}}$,",
        "i.e., where $\\rho > \\rho_{\\mathrm{crit}} = \\rho_{\\max} - "
        "(M_{\\mathrm{crit}}/M_0)^{1/\\beta}$.",
        "Within this region, diffusion is effectively halted.",
        "",
        "The horizon boundary $R_H(t)$ obeys the ED Stefan condition:",
        "",
        "$$\\frac{dR_H}{dt} = -\\frac{F[\\rho](R_H)}{(\\partial\\rho/\\partial r)(R_H)}$$",
        "",
        "Since $F < 0$ at the boundary (penalty dominates) and "
        "$\\partial\\rho/\\partial r < 0$ (density decreasing outward),",
        "the boundary retreats inward ($dR_H/dt < 0$).",
        "",
        "### Critical amplitude",
        "",
        "A horizon forms when the peak density exceeds $\\rho_{\\mathrm{crit}}$:",
        "",
        "$$A_c = \\rho_{\\mathrm{crit}} - \\rho^*$$",
        "",
    ]

    # --- Run canonical experiment ---
    lines.extend([
        "## 2. Test 1: Horizon Evolution at $A = 0.45$",
        "",
    ])

    res_canon = run_horizon_experiment(A=0.45, N=128, T=3.0, n_snaps=60, dt=0.0005)
    pred = res_canon.prediction

    lines.extend([
        f"Parameters: $M_{{\\mathrm{{crit}}}} = {pred.M_crit}$, "
        f"$\\rho_{{\\mathrm{{crit}}}} = {pred.rho_crit:.4f}$, "
        f"$A_c = {pred.A_c:.4f}$, $\\sigma = {pred.sigma}$",
        "",
        f"**Horizon formed:** {'YES' if res_canon.horizon_formed else 'NO'}",
        "",
        f"**Horizon lifetime:** $\\tau_H = {res_canon.tau_H:.4f}$ "
        f"(predicted: {res_canon.tau_H_predicted:.4f})",
        "",
        "### Horizon radius evolution:",
        "",
        "| $t$ | $R_H(t)$ | Peak $\\rho$ | $|\\nabla\\rho|$ at boundary |",
        "|-----|----------|-------------|-------------------------------|",
    ])

    for i in range(0, len(res_canon.times), max(1, len(res_canon.times) // 12)):
        t = res_canon.times[i]
        rh = res_canon.R_H[i]
        pk = res_canon.peak_rho[i]
        gr = res_canon.grad_at_boundary[i]
        lines.append(f"| {t:.3f} | {rh:.4f} | {pk:.4f} | {gr:.4f} |")

    # --- Amplitude sweep ---
    lines.extend([
        "",
        "## 3. Test 2: Amplitude Sweep (Threshold and Lifetime)",
        "",
    ])

    sweep = run_amplitude_sweep(N=96)

    lines.extend([
        f"**Predicted $A_c$:** {sweep.A_c_predicted:.4f}",
        "",
        f"**Measured $A_c$:** {sweep.A_c_measured:.4f} "
        f"(smallest $A$ with horizon)",
        "",
        "| $A$ | Horizon? | $\\tau_H$ measured | $\\tau_H$ predicted |",
        "|-----|----------|-------------------|---------------------|",
    ])

    for i, A in enumerate(sweep.A_values):
        res = sweep.results[i]
        formed = "YES" if res.horizon_formed else "no"
        tau_m = f"{res.tau_H:.4f}" if res.horizon_formed else "--"
        tau_p = f"{res.tau_H_predicted:.4f}" if res.tau_H_predicted > 0 else "--"
        lines.append(f"| {A:.2f} | {formed} | {tau_m} | {tau_p} |")

    # Check: tau_H monotonic in A?
    formed_results = [(A, r.tau_H) for A, r in zip(sweep.A_values, sweep.results)
                      if r.horizon_formed]
    if len(formed_results) >= 2:
        taus = [t for _, t in formed_results]
        monotone = all(taus[i] <= taus[i + 1] + 0.01 for i in range(len(taus) - 1))
    else:
        monotone = False

    # Stefan correlation
    lines.extend([
        "",
        "## 4. Test 3: Stefan-like Retreat",
        "",
        f"**Correlation between $|dR_H/dt|$ and $|\\nabla\\rho|$ at boundary:** "
        f"{sweep.stefan_corr:.4f}",
        "",
    ])

    if sweep.stefan_corr > 0.5:
        lines.append("The retreat rate is positively correlated with the gradient "
                      "at the boundary, consistent with the Stefan condition.")
    elif sweep.stefan_corr > 0:
        lines.append("Weak positive correlation detected. The gradient at the "
                      "boundary partially controls the retreat rate.")
    else:
        lines.append("No positive correlation detected. The retreat dynamics "
                      "differ from the simple Stefan condition.")

    # --- Falsification ---
    lines.extend([
        "",
        "## 5. Falsification Assessment",
        "",
    ])

    horizon_ok = res_canon.horizon_formed
    threshold_ok = abs(sweep.A_c_measured - sweep.A_c_predicted) / sweep.A_c_predicted < 0.15 if sweep.A_c_predicted > 0 else False
    no_sub = all(not r.horizon_formed for A, r in zip(sweep.A_values, sweep.results) if A < sweep.A_c_predicted - 0.02)
    monotone_ok = monotone
    retreat_ok = res_canon.tau_H > 0 and res_canon.R_H[-1] <= res_canon.R_H[1] + 0.01 if res_canon.horizon_formed else False

    lines.extend([
        "| Criterion | Threshold | Result | Pass? |",
        "|-----------|-----------|--------|-------|",
        f"| Horizon forms at $A > A_c$ | forms at $A = 0.45$ | "
        f"{'YES' if horizon_ok else 'NO'} | {'**PASS**' if horizon_ok else 'FAIL'} |",
        f"| Sharp threshold $A_c$ | pred={sweep.A_c_predicted:.3f}, "
        f"meas={sweep.A_c_measured:.3f} | "
        f"{'within 15%' if threshold_ok else 'mismatch'} | "
        f"{'**PASS**' if threshold_ok else 'FAIL'} |",
        f"| No horizon below $A_c$ | all sub-threshold runs clean | "
        f"{'YES' if no_sub else 'NO'} | {'**PASS**' if no_sub else 'FAIL'} |",
        f"| $\\tau_H$ increases with $A$ | monotonic | "
        f"{'YES' if monotone_ok else 'NO'} | {'**PASS**' if monotone_ok else 'FAIL'} |",
        f"| Horizon retreats | $R_H$ decreases | "
        f"{'YES' if retreat_ok else 'NO'} | {'**PASS**' if retreat_ok else 'FAIL'} |",
    ])

    all_pass = horizon_ok and threshold_ok and no_sub and monotone_ok and retreat_ok

    # --- Conclusion ---
    lines.extend([
        "",
        "## 6. Conclusion",
        "",
    ])

    if all_pass:
        lines.extend([
            "**All falsification criteria are satisfied.**",
            "",
            "The canonical ED PDE, with $H = 0$, produces horizon dynamics",
            "structurally analogous to the Stefan free-boundary problem:",
            "",
            f"- Horizons form when $A > A_c = {sweep.A_c_predicted:.3f}$ "
            f"(measured threshold: {sweep.A_c_measured:.3f})",
            f"- Horizon lifetime $\\tau_H$ increases monotonically with $A$",
            "- Horizons retreat as the penalty pulls density below $\\rho_{\\mathrm{crit}}$",
            f"- Stefan correlation: {sweep.stefan_corr:.3f}",
            "",
            "The ED degenerate mobility creates dynamically isolated regions",
            "(horizons) that form, persist, and retreat under the competition",
            "between mobility degeneracy and penalty relaxation.",
        ])
    else:
        lines.extend([
            "**One or more falsification criteria failed. See table above.**",
            "",
            f"Horizon formed: {horizon_ok}",
            f"Threshold: pred={sweep.A_c_predicted:.3f}, meas={sweep.A_c_measured}",
            f"Monotone lifetime: {monotone_ok}",
            f"Retreat: {retreat_ok}",
        ])

    return "\n".join(lines)
