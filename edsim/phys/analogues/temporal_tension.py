"""
edsim.phys.analogues.temporal_tension — Effective interaction between density peaks.

Tests whether ED's constitutive channels generate an emergent "interaction"
between separated density peaks. Two identical Gaussian bumps are placed at
distance d and evolved. Their centres of mass are tracked to measure drift.

Mechanism:
    The tail of each peak creates a gradient bias at the other peak's
    location. The nonlinear mobility M(rho) makes the effective diffusion
    density-dependent, breaking the symmetry of the spreading. The
    participation variable v(t) modulates this asymmetry by uniformly
    adding/subtracting density, changing the local mobility.

    This experiment measures:
    1. Whether isolated peaks drift toward or away from each other.
    2. Whether the drift correlates with v(t).
    3. Whether the drift magnitude scales with H and decays with d.
"""

from __future__ import annotations

import numpy as np
from dataclasses import dataclass

from ...core.parameters import EDParameters
from ...core.constitutive import mobility, mobility_deriv, penalty, enforce_bounds
from ...core.operators import laplacian_fd_2d, grad_squared_fd_2d
from ...core.participation import advance_v, spatial_average


# ------------------------------------------------------------------ #
#  Data structures                                                    #
# ------------------------------------------------------------------ #

@dataclass
class TensionResult:
    H: float
    d_init: float
    times: np.ndarray
    x1: np.ndarray          # peak 1 CoM (x-coordinate)
    x2: np.ndarray          # peak 2 CoM
    separation: np.ndarray   # |x2 - x1|
    v_history: np.ndarray
    drift_rate: float        # mean d(separation)/dt
    drift_v_correlation: float  # corr(d(sep)/dt, v(t))


@dataclass
class TensionSweep:
    H_values: list
    d_values: list
    results: dict            # (H, d) -> TensionResult
    drift_rates: dict        # (H, d) -> float


# ------------------------------------------------------------------ #
#  Solver + IC                                                        #
# ------------------------------------------------------------------ #

def _make_params(N, L, H, P0, dt):
    return EDParameters(
        d=2, N=(N, N), L=(L, L),
        D=0.3, H=H, tau=1.0, zeta=0.1,
        rho_star=0.5, rho_max=1.0, M0=1.0, beta=2.0,
        P0=P0, dt=dt, T=1.0, method="implicit_euler", bc="neumann",
    )


def _make_two_peak_ic(params, A, sigma, d_sep):
    """Two Gaussian bumps separated by d_sep along the x-axis."""
    Nx, Ny = params.N
    Lx = params.L[0]
    dx = Lx / Nx
    x = np.arange(Nx) * dx
    y = np.arange(Ny) * dx
    X, Y = np.meshgrid(x, y, indexing="ij")
    cx, cy = Lx / 2, Lx / 2
    x1 = cx - d_sep / 2
    x2 = cx + d_sep / 2
    r1_sq = (X - x1) ** 2 + (Y - cy) ** 2
    r2_sq = (X - x2) ** 2 + (Y - cy) ** 2
    rho = params.rho_star + A * (np.exp(-r1_sq / (2 * sigma ** 2))
                                  + np.exp(-r2_sq / (2 * sigma ** 2)))
    return enforce_bounds(rho, params)


def _run_solver(params, rho0, T, snap_interval):
    rho = rho0.copy()
    v = 0.0
    t = 0.0
    dt = params.dt
    dx = (params.L[0] / params.N[0], params.L[1] / params.N[1])

    times = [0.0]
    fields = [rho.copy()]
    v_hist = [0.0]
    n_steps = int(np.ceil(T / dt))
    next_snap = snap_interval

    for _ in range(n_steps):
        rho_old = rho.copy()
        for _fp in range(12):
            lap = laplacian_fd_2d(rho, dx)
            gsq = grad_squared_fd_2d(rho, dx)
            M = mobility(rho, params)
            Mp = mobility_deriv(rho, params)
            P = penalty(rho, params)
            F_local = M * lap + Mp * gsq - P
            F_total = params.D * F_local + params.H * v
            rho_new = rho_old + dt * F_total
            rho_new = enforce_bounds(rho_new, params)
            if np.max(np.abs(rho_new - rho)) < 1e-7:
                rho = rho_new
                break
            rho = rho_new

        F_avg = spatial_average(params.D * F_local, dx)
        v = advance_v(v, F_avg, params)
        t += dt

        if t >= next_snap - dt / 2:
            times.append(t)
            fields.append(rho.copy())
            v_hist.append(v)
            next_snap += snap_interval

    return {"times": np.array(times), "fields": fields, "v": np.array(v_hist)}


# ------------------------------------------------------------------ #
#  Peak tracking                                                      #
# ------------------------------------------------------------------ #

def _track_peak_com(rho, params, cx, cy, side):
    """Track the centre of mass of one peak (left or right of cx).

    side = 'left' or 'right'.
    Uses the density above rho_star as the weight.
    """
    Nx, Ny = params.N
    Lx = params.L[0]
    dx = Lx / Nx
    x = np.arange(Nx) * dx
    y = np.arange(Ny) * dx
    X, Y = np.meshgrid(x, y, indexing="ij")

    weight = np.maximum(rho - params.rho_star, 0.0)

    if side == "left":
        mask = X < cx
    else:
        mask = X >= cx

    w = weight * mask
    total = np.sum(w) * dx ** 2
    if total < 1e-15:
        return cx - 0.5 if side == "left" else cx + 0.5

    x_com = np.sum(X * w) * dx ** 2 / total
    return x_com


# ------------------------------------------------------------------ #
#  Experiments                                                        #
# ------------------------------------------------------------------ #

def run_tension_experiment(
    H: float = 5.0,
    d_sep: float = 1.0,
    A: float = 0.15,
    sigma: float = 0.2,
    P0: float = 1.0,
    N: int = 128,
    L: float = 6.0,
    T: float = 5.0,
    n_snaps: int = 100,
    dt: float = 0.001,
) -> TensionResult:
    """Run one two-peak tension experiment."""
    params = _make_params(N=N, L=L, H=H, P0=P0, dt=dt)
    ic = _make_two_peak_ic(params, A=A, sigma=sigma, d_sep=d_sep)
    snap_interval = T / n_snaps

    result = _run_solver(params, ic, T=T, snap_interval=snap_interval)

    cx, cy = L / 2, L / 2
    times = result["times"]
    x1_arr = np.empty(len(times))
    x2_arr = np.empty(len(times))

    for i, fld in enumerate(result["fields"]):
        x1_arr[i] = _track_peak_com(fld, params, cx, cy, "left")
        x2_arr[i] = _track_peak_com(fld, params, cx, cy, "right")

    separation = x2_arr - x1_arr

    # Drift rate: linear fit to separation(t)
    mask = times > T * 0.1
    if mask.sum() >= 3:
        A_mat = np.vstack([times[mask], np.ones(mask.sum())]).T
        coeffs = np.linalg.lstsq(A_mat, separation[mask], rcond=None)[0]
        drift_rate = coeffs[0]
    else:
        drift_rate = 0.0

    # Correlation between d(sep)/dt and v(t)
    dsep_dt = np.diff(separation) / np.diff(times)
    v_mid = (result["v"][:-1] + result["v"][1:]) / 2
    if len(dsep_dt) >= 5:
        # Remove trend
        dsep_detrended = dsep_dt - np.mean(dsep_dt)
        v_detrended = v_mid - np.mean(v_mid)
        denom = np.std(dsep_detrended) * np.std(v_detrended)
        if denom > 1e-15:
            corr = np.mean(dsep_detrended * v_detrended) / denom
        else:
            corr = 0.0
    else:
        corr = 0.0

    return TensionResult(
        H=H, d_init=d_sep,
        times=times, x1=x1_arr, x2=x2_arr,
        separation=separation, v_history=result["v"],
        drift_rate=drift_rate,
        drift_v_correlation=corr,
    )


def run_tension_sweep(
    H_values: list = None,
    d_values: list = None,
    A: float = 0.15,
    sigma: float = 0.2,
    N: int = 96,
) -> TensionSweep:
    """Sweep H and d to map the interaction."""
    if H_values is None:
        H_values = [0.0, 2.0, 5.0, 10.0]
    if d_values is None:
        d_values = [0.5, 1.0, 1.5, 2.0]

    results = {}
    drift_rates = {}

    for H in H_values:
        for d in d_values:
            res = run_tension_experiment(
                H=H, d_sep=d, A=A, sigma=sigma, N=N,
                T=5.0, n_snaps=80, dt=0.001,
            )
            results[(H, d)] = res
            drift_rates[(H, d)] = res.drift_rate

    return TensionSweep(
        H_values=H_values, d_values=d_values,
        results=results, drift_rates=drift_rates,
    )


# ------------------------------------------------------------------ #
#  Full experiment + report                                           #
# ------------------------------------------------------------------ #

def run_full_tension_experiment() -> str:
    """Run the complete experiment and produce a report."""

    lines = [
        "# ED Structural Analogue 6: Temporal Tension as an Effective Potential",
        "",
        "## 1. Structural Mapping",
        "",
        "Two identical density peaks at distance $d$ interact through:",
        "",
        "1. **Tail overlap**: each peak's gradient creates a bias at the other's location",
        "2. **Nonlinear mobility**: $M(\\rho)$ makes diffusion density-dependent, "
        "breaking spreading symmetry",
        "3. **Participation**: $v(t)$ modulates the density field uniformly, "
        "changing the local mobility between the peaks",
        "",
        "The measured quantity is the **separation** $s(t) = x_2(t) - x_1(t)$.",
        "A decrease indicates attraction; an increase indicates repulsion.",
        "",
    ]

    # --- Control: H=0 ---
    lines.extend(["## 2. Control: $H = 0$", ""])

    res0 = run_tension_experiment(H=0.0, d_sep=1.0, N=96, T=5.0, n_snaps=80, dt=0.001)
    lines.extend([
        f"Initial separation: {res0.separation[0]:.4f}",
        f"Final separation: {res0.separation[-1]:.4f}",
        f"Drift rate: {res0.drift_rate:.6f}",
        f"$v$-drift correlation: {res0.drift_v_correlation:.4f}",
        "",
    ])

    # --- H=5 ---
    lines.extend(["## 3. Active: $H = 5$, $d = 1.0$", ""])

    res5 = run_tension_experiment(H=5.0, d_sep=1.0, N=96, T=5.0, n_snaps=100, dt=0.001)
    lines.extend([
        f"Initial separation: {res5.separation[0]:.4f}",
        f"Final separation: {res5.separation[-1]:.4f}",
        f"Drift rate: {res5.drift_rate:.6f}",
        f"$v$-drift correlation: {res5.drift_v_correlation:.4f}",
        f"$v$ sign changes: {np.sum(np.diff(np.sign(res5.v_history)) != 0)}",
        "",
        "### Separation and v evolution:",
        "",
        "| $t$ | Separation | $v(t)$ | $\\Delta$sep |",
        "|-----|-----------|--------|-------------|",
    ])

    for i in range(0, len(res5.times), max(1, len(res5.times) // 12)):
        t = res5.times[i]
        s = res5.separation[i]
        v = res5.v_history[i]
        ds = s - res5.separation[0]
        lines.append(f"| {t:.2f} | {s:.6f} | {v:.6f} | {ds:+.6f} |")

    # --- Full sweep ---
    lines.extend(["", "## 4. H and d Sweep", ""])

    sweep = run_tension_sweep(
        H_values=[0.0, 2.0, 5.0, 10.0],
        d_values=[0.5, 1.0, 1.5, 2.0],
        N=96,
    )

    lines.extend([
        "### Drift rates (separation change per unit time):",
        "",
        "| | $d = 0.5$ | $d = 1.0$ | $d = 1.5$ | $d = 2.0$ |",
        "|---|----------|----------|----------|----------|",
    ])

    for H in sweep.H_values:
        row = f"| $H = {H:.0f}$ |"
        for d in sweep.d_values:
            dr = sweep.drift_rates.get((H, d), 0.0)
            row += f" {dr:+.6f} |"
        lines.append(row)

    # v-drift correlations
    lines.extend([
        "",
        "### $v$-drift correlations:",
        "",
        "| | $d = 0.5$ | $d = 1.0$ | $d = 1.5$ | $d = 2.0$ |",
        "|---|----------|----------|----------|----------|",
    ])

    for H in sweep.H_values:
        row = f"| $H = {H:.0f}$ |"
        for d in sweep.d_values:
            res = sweep.results.get((H, d))
            c = res.drift_v_correlation if res else 0.0
            row += f" {c:+.4f} |"
        lines.append(row)

    # --- Analysis ---
    lines.extend(["", "## 5. Analysis", ""])

    # Does drift increase with H?
    d_ref = 1.0
    h0_drift = abs(sweep.drift_rates.get((0.0, d_ref), 0.0))
    h_drifts = {H: abs(sweep.drift_rates.get((H, d_ref), 0.0))
                for H in sweep.H_values if H > 0}
    drift_scales = all(v > h0_drift * 1.5 for v in h_drifts.values()) if h_drifts else False

    # Does drift decay with d?
    H_ref = 5.0
    d_drifts = {d: abs(sweep.drift_rates.get((H_ref, d), 0.0))
                for d in sweep.d_values}
    d_sorted = sorted(d_drifts.items())
    drift_decays = len(d_sorted) >= 2 and d_sorted[0][1] > d_sorted[-1][1]

    # Is H=0 quiet?
    h0_drifts = [abs(sweep.drift_rates.get((0.0, d), 0.0)) for d in sweep.d_values]
    h0_quiet = all(dr < 0.01 for dr in h0_drifts)

    # v-drift correlation for H > 0
    correlations = [sweep.results[(H, d_ref)].drift_v_correlation
                    for H in sweep.H_values if H > 0]
    mean_corr = np.mean(correlations) if correlations else 0.0

    # Direction consistency
    h_pos_drifts = [sweep.drift_rates.get((H, d_ref), 0.0)
                    for H in sweep.H_values if H > 0]
    all_same_sign = (all(d > 0 for d in h_pos_drifts) or
                     all(d < 0 for d in h_pos_drifts) or
                     all(abs(d) < 0.001 for d in h_pos_drifts))

    direction = "repulsion" if np.mean(h_pos_drifts) > 0 else "attraction" if np.mean(h_pos_drifts) < 0 else "negligible"

    lines.extend([
        f"**Direction of drift:** {direction}",
        f"**H=0 quiet:** {h0_quiet} (max drift: {max(h0_drifts):.6f})",
        f"**Drift scales with H:** {drift_scales}",
        f"**Drift decays with d:** {drift_decays}",
        f"**Mean v-drift correlation (H>0):** {mean_corr:.4f}",
        "",
    ])

    # --- Falsification ---
    lines.extend(["## 6. Falsification Assessment", ""])

    lines.extend([
        "| Criterion | Result | Pass? |",
        "|-----------|--------|-------|",
        f"| Drift direction consistent | {all_same_sign} ({direction}) | "
        f"{'**PASS**' if all_same_sign else 'FAIL'} |",
        f"| No drift at $H = 0$ | max={max(h0_drifts):.6f} | "
        f"{'**PASS**' if h0_quiet else 'FAIL'} |",
        f"| Drift scales with $H$ | {drift_scales} | "
        f"{'**PASS**' if drift_scales else 'FAIL'} |",
        f"| Drift decays with $d$ | {drift_decays} | "
        f"{'**PASS**' if drift_decays else 'FAIL'} |",
    ])

    all_pass = all_same_sign and h0_quiet and drift_scales and drift_decays

    # --- Conclusion ---
    lines.extend(["", "## 7. Conclusion", ""])

    if all_pass:
        lines.extend([
            "**All falsification criteria are satisfied.**",
            "",
            f"The canonical ED PDE generates an effective **{direction}** "
            "between density peaks:",
            "",
            f"- Direction: peaks {direction.replace('tion','')} each other",
            f"- Drift magnitude scales with participation coupling $H$",
            f"- Drift decays with separation $d$",
            "- No drift at $H = 0$ (pure diffusion is symmetric)",
            "",
            "This is the ED structural analogue of an effective potential "
            "between localised structures.",
        ])
    else:
        failed = []
        if not all_same_sign:
            failed.append("direction inconsistent")
        if not h0_quiet:
            failed.append(f"H=0 drift too large ({max(h0_drifts):.6f})")
        if not drift_scales:
            failed.append("drift doesn't scale with H")
        if not drift_decays:
            failed.append("drift doesn't decay with d")
        lines.extend([
            "**One or more criteria failed:**",
            "",
        ] + [f"- {f}" for f in failed])

    return "\n".join(lines)
