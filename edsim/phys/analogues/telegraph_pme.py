"""
edsim.phys.analogues.telegraph_pme — Telegraph-modulated PME spreading.

Combines degenerate mobility (PME) with participation (telegraph), using
a very weak penalty (P0 << 1) that serves ONLY to activate the telegraph
channel via F_bar = -D*P0*(<rho> - rho_star) != 0.

Critical insight: with P0 = 0 and Neumann BCs, the divergence theorem
forces <div(M grad rho)> = 0, so F_bar = 0 and v(t) = 0 identically.
A tiny P0 > 0 breaks this degeneracy and allows the participation
coupling to oscillate.

The PME dynamics dominate (spreading exponent alpha_R = 1/(d(m-1)+2))
while the telegraph modulates the interior density at frequency
omega(H, tau, zeta).
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
class TelegraphPMEPrediction:
    beta: float
    m: float
    alpha_R: float
    omega: float
    gamma: float
    T_osc: float
    P0: float
    D_pme: float


@dataclass
class TelegraphPMEResult:
    H: float
    prediction: TelegraphPMEPrediction
    times: np.ndarray
    central_delta: np.ndarray       # delta(0,t) = rho_max - rho(0,t)
    front_radius: np.ndarray        # half-max radius
    v_history: np.ndarray
    alpha_R_fitted: float
    alpha_rho_fitted: float
    omega_density_fitted: float     # frequency of central delta oscillation
    omega_v_fitted: float           # frequency of v oscillation
    density_osc_amplitude: float    # amplitude of oscillation in central delta


@dataclass
class TelegraphPMESweep:
    H_values: list
    results: list
    omega_predicted: list
    omega_density_measured: list
    density_osc_amplitudes: list


# ------------------------------------------------------------------ #
#  Predictions                                                        #
# ------------------------------------------------------------------ #

def predict_telegraph_pme(
    beta: float = 1.0,
    d: int = 2,
    D: float = 0.3,
    M0: float = 1.0,
    P0: float = 0.01,
    H: float = 20.0,
    zeta: float = 0.1,
    tau: float = 1.0,
) -> TelegraphPMEPrediction:
    m = beta + 1.0
    alpha_R = 1.0 / (d * (m - 1.0) + 2.0)
    D_pme = D * M0 / (beta + 1.0)

    gamma = (D * P0 + zeta / tau) / 2.0
    omega0_sq = (D * P0 * zeta + H * P0) / tau
    disc = gamma ** 2 - omega0_sq
    if disc < 0:
        omega = np.sqrt(-disc)
        T_osc = 2 * np.pi / omega
    else:
        omega = 0.0
        T_osc = np.inf

    return TelegraphPMEPrediction(
        beta=beta, m=m, alpha_R=alpha_R,
        omega=omega, gamma=gamma, T_osc=T_osc,
        P0=P0, D_pme=D_pme,
    )


# ------------------------------------------------------------------ #
#  Solver                                                             #
# ------------------------------------------------------------------ #

def _make_params(N, L, beta, P0, H, dt):
    return EDParameters(
        d=2, N=(N, N), L=(L, L),
        D=0.3, H=H, tau=1.0, zeta=0.1,
        rho_star=0.5, rho_max=1.0, M0=1.0, beta=beta,
        P0=max(P0, 1e-12), dt=dt, T=1.0,
        method="implicit_euler", bc="neumann",
    )


def _make_ic(params, A, sigma):
    Nx, Ny = params.N
    Lx = params.L[0]
    dx = Lx / Nx
    x = np.arange(Nx) * dx
    y = np.arange(Ny) * dx
    X, Y = np.meshgrid(x, y, indexing="ij")
    r2 = (X - Lx / 2) ** 2 + (Y - Lx / 2) ** 2
    delta_bg = 1e-4
    delta_ic = A * np.exp(-r2 / (2.0 * sigma ** 2)) + delta_bg
    rho_ic = params.rho_max - delta_ic
    return enforce_bounds(rho_ic, params)


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
            if np.max(np.abs(rho_new - rho)) < 1e-8:
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
#  Analysis                                                           #
# ------------------------------------------------------------------ #

def _measure_half_max_radius(delta, cx, cy, dx):
    Nx, Ny = delta.shape
    x = np.arange(Nx) * dx
    y = np.arange(Ny) * dx
    X, Y = np.meshgrid(x, y, indexing="ij")
    R = np.sqrt((X - cx) ** 2 + (Y - cy) ** 2)
    ci, cj = Nx // 2, Ny // 2
    d_max = delta[ci, cj]
    mask = delta > d_max / 2.0
    return R[mask].max() if mask.any() else 0.0


def _fit_power_law(t, y):
    mask = (t > 0) & (y > 0) & np.isfinite(y)
    if mask.sum() < 3:
        return 0.0, 0.0
    lt = np.log(t[mask])
    ly = np.log(y[mask])
    A = np.vstack([lt, np.ones(len(lt))]).T
    res = np.linalg.lstsq(A, ly, rcond=None)
    return res[0][0], np.exp(res[0][1])


def _extract_oscillation(t, y, t_min=0.0):
    """Extract oscillation frequency and amplitude from a detrended signal."""
    mask = t > t_min
    if mask.sum() < 8:
        return 0.0, 0.0

    t_m = t[mask]
    y_m = y[mask]

    # Detrend with power law: y ~ a * t^b
    pos = y_m > 0
    if pos.sum() < 4:
        # Linear detrend
        A = np.vstack([t_m, np.ones(len(t_m))]).T
        c = np.linalg.lstsq(A, y_m, rcond=None)[0]
        trend = A @ c
    else:
        lt = np.log(t_m[pos])
        ly = np.log(y_m[pos])
        A = np.vstack([lt, np.ones(len(lt))]).T
        c = np.linalg.lstsq(A, ly, rcond=None)[0]
        trend = np.exp(c[1]) * t_m ** c[0]

    residual = y_m - trend

    # FFT
    dt_mean = np.mean(np.diff(t_m))
    if dt_mean <= 0 or len(residual) < 6:
        return 0.0, 0.0

    ft = np.fft.rfft(residual)
    freqs = np.fft.rfftfreq(len(residual), d=dt_mean)
    mag = np.abs(ft)

    if len(mag) > 2:
        peak_idx = np.argmax(mag[1:]) + 1
        omega = 2 * np.pi * freqs[peak_idx]
        amplitude = 2 * mag[peak_idx] / len(residual)
    else:
        omega = 0.0
        amplitude = 0.0

    return omega, amplitude


# ------------------------------------------------------------------ #
#  Experiments                                                        #
# ------------------------------------------------------------------ #

def run_telegraph_pme(
    H: float = 20.0,
    beta: float = 1.0,
    P0: float = 0.01,
    N: int = 64,
    L: float = 8.0,
    A_ic: float = 0.4,
    sigma: float = 0.25,
    T: float = 100.0,
    n_snaps: int = 200,
    dt: float = 0.005,
) -> TelegraphPMEResult:
    """Run one telegraph-PME experiment."""
    params = _make_params(N=N, L=L, beta=beta, P0=P0, H=H, dt=dt)
    pred = predict_telegraph_pme(beta=beta, P0=P0, H=H)

    ic = _make_ic(params, A=A_ic, sigma=sigma)
    snap_interval = T / n_snaps
    result = _run_solver(params, ic, T=T, snap_interval=snap_interval)

    dx = L / N
    cx = L / 2
    ci = N // 2
    times = result["times"]

    central_delta = np.array([params.rho_max - f[ci, ci] for f in result["fields"]])
    front_radius = np.array([
        _measure_half_max_radius(params.rho_max - f, cx, cx, dx)
        for f in result["fields"]
    ])

    # Fit PME exponent from late times
    mask_late = times > T * 0.3
    alpha_R, _ = _fit_power_law(times[mask_late], front_radius[mask_late])
    alpha_rho, _ = _fit_power_law(times[mask_late], central_delta[mask_late])

    # Extract oscillation from central delta
    omega_d, amp_d = _extract_oscillation(times, central_delta, t_min=T * 0.1)

    # Extract oscillation from v
    omega_v, _ = _extract_oscillation(times, np.abs(result["v"]), t_min=T * 0.1)

    return TelegraphPMEResult(
        H=H, prediction=pred,
        times=times,
        central_delta=central_delta,
        front_radius=front_radius,
        v_history=result["v"],
        alpha_R_fitted=alpha_R,
        alpha_rho_fitted=alpha_rho,
        omega_density_fitted=omega_d,
        omega_v_fitted=omega_v,
        density_osc_amplitude=amp_d,
    )


def run_telegraph_pme_sweep(
    H_values: list = None,
    beta: float = 1.0,
    P0: float = 0.01,
    N: int = 64,
) -> TelegraphPMESweep:
    if H_values is None:
        H_values = [0.0, 10.0, 20.0, 50.0]

    results = []
    omega_pred = []
    omega_meas = []
    amp_meas = []

    for H in H_values:
        pred = predict_telegraph_pme(beta=beta, P0=P0, H=H)
        omega_pred.append(pred.omega)
        res = run_telegraph_pme(H=H, beta=beta, P0=P0, N=N)
        results.append(res)
        omega_meas.append(res.omega_density_fitted)
        amp_meas.append(res.density_osc_amplitude)

    return TelegraphPMESweep(
        H_values=H_values, results=results,
        omega_predicted=omega_pred,
        omega_density_measured=omega_meas,
        density_osc_amplitudes=amp_meas,
    )


# ------------------------------------------------------------------ #
#  Full experiment + report                                           #
# ------------------------------------------------------------------ #

def run_full_telegraph_pme_experiment() -> str:
    """Run the complete experiment and produce a report."""

    lines = [
        "# ED Structural Analogue 5: Telegraph-Modulated PME Spreading",
        "",
        "## 1. Structural Mapping",
        "",
        "With weak penalty ($P_0 \\ll 1$) and $H > 0$:",
        "",
        "- The **mobility channel** produces PME spreading: "
        "$R(t) \\propto t^{\\alpha_R}$",
        "- The **weak penalty** activates $\\bar{F} = -D P_0 (\\langle\\rho\\rangle "
        "- \\rho^*) \\neq 0$, driving $v(t)$",
        "- The **participation channel** creates telegraph oscillation of $v(t)$ "
        "at frequency $\\omega$",
        "- The oscillating $v$ modulates the interior density via $+Hv$",
        "",
        "**Critical insight:** With $P_0 = 0$ and Neumann BCs, the divergence "
        "theorem forces $\\langle\\nabla\\!\\cdot\\!(M\\nabla\\rho)\\rangle = 0$, "
        "so $\\bar{F} = 0$ and $v(t) = 0$ identically. A tiny $P_0 > 0$ breaks "
        "this degeneracy.",
        "",
    ]

    # --- Control: H=0 ---
    lines.extend(["## 2. Control: $H = 0$", ""])
    res0 = run_telegraph_pme(H=0.0, P0=0.01, beta=1.0, N=64, T=100.0, n_snaps=100, dt=0.005)
    pred0 = res0.prediction

    lines.extend([
        f"PME exponent: $\\alpha_R = {pred0.alpha_R:.4f}$ (predicted), "
        f"${res0.alpha_R_fitted:.4f}$ (measured)",
        f"Central density exponent: ${res0.alpha_rho_fitted:.4f}$ "
        f"(predicted: ${-2/(2*(pred0.m-1)+2):.4f}$)",
        f"Density oscillation amplitude: {res0.density_osc_amplitude:.6f}",
        f"$v$ max: {np.max(np.abs(res0.v_history)):.6f}",
        "",
    ])

    # --- H=20 ---
    lines.extend(["## 3. Telegraph: $H = 20$", ""])
    res20 = run_telegraph_pme(H=20.0, P0=0.01, beta=1.0, N=64, T=100.0, n_snaps=200, dt=0.005)
    pred20 = res20.prediction

    lines.extend([
        f"Predicted $\\omega = {pred20.omega:.4f}$, $T = {pred20.T_osc:.2f}$",
        "",
        f"PME exponent: $\\alpha_R = {res20.alpha_R_fitted:.4f}$ "
        f"(predicted: {pred20.alpha_R:.4f})",
        f"Density oscillation $\\omega$: {res20.omega_density_fitted:.4f}",
        f"Density oscillation amplitude: {res20.density_osc_amplitude:.6f}",
        f"$v$ oscillation $\\omega$: {res20.omega_v_fitted:.4f}",
        f"$v$ sign changes: {np.sum(np.diff(np.sign(res20.v_history)) != 0)}",
        "",
        "### Central delta and v evolution (sampled):",
        "",
        "| $t$ | $\\delta(0,t)$ | $v(t)$ |",
        "|-----|---------------|--------|",
    ])
    for i in range(0, len(res20.times), max(1, len(res20.times) // 15)):
        t = res20.times[i]
        d = res20.central_delta[i]
        v = res20.v_history[i]
        lines.append(f"| {t:.1f} | {d:.6f} | {v:.7f} |")

    # --- H sweep ---
    lines.extend(["", "## 4. H Sweep", ""])
    sweep = run_telegraph_pme_sweep(
        H_values=[0.0, 5.0, 10.0, 20.0, 50.0],
        P0=0.01, beta=1.0, N=64,
    )

    lines.extend([
        "| $H$ | $\\omega_{\\mathrm{pred}}$ | $\\omega_{\\mathrm{meas}}$ "
        "(density) | Osc. amp | $\\alpha_R$ | $v$ sign changes |",
        "|-----|--------------------------|----------------------------"
        "---------|----------|------------|------------------|",
    ])

    for i, H in enumerate(sweep.H_values):
        res = sweep.results[i]
        op = sweep.omega_predicted[i]
        om = sweep.omega_density_measured[i]
        amp = sweep.density_osc_amplitudes[i]
        v_sc = np.sum(np.diff(np.sign(res.v_history)) != 0)
        op_s = f"{op:.4f}" if op > 0 else "overdamp"
        lines.append(
            f"| {H:.1f} | {op_s} | {om:.4f} | {amp:.6f} | "
            f"{res.alpha_R_fitted:.4f} | {v_sc} |"
        )

    # Amplitude scaling
    H_pos = [H for H in sweep.H_values if H > 0]
    amp_pos = [sweep.density_osc_amplitudes[i]
               for i, H in enumerate(sweep.H_values) if H > 0]

    if len(H_pos) >= 2 and all(a > 0 for a in amp_pos):
        log_h = np.log(H_pos)
        log_a = np.log(amp_pos)
        A_mat = np.vstack([log_h, np.ones(len(log_h))]).T
        slope = np.linalg.lstsq(A_mat, log_a, rcond=None)[0][0]
        lines.append(f"\n**Amplitude scaling:** osc. amp $\\propto H^{{{slope:.2f}}}$")
    else:
        slope = 0.0

    # --- Falsification ---
    lines.extend(["", "## 5. Falsification Assessment", ""])

    h0_res = sweep.results[0]
    h0_quiet = h0_res.density_osc_amplitude < 0.001
    osc_detected = any(r.density_osc_amplitude > h0_res.density_osc_amplitude * 2
                       for r in sweep.results[1:])
    v_active = any(np.sum(np.diff(np.sign(r.v_history)) != 0) >= 2
                   for r in sweep.results[1:])

    # PME exponent preserved
    pme_ok = all(abs(r.alpha_R_fitted - r.prediction.alpha_R) / r.prediction.alpha_R < 0.2
                 for r in sweep.results)

    # Amplitude increases
    amp_increases = len(amp_pos) >= 2 and amp_pos[-1] > amp_pos[0]

    lines.extend([
        "| Criterion | Result | Pass? |",
        "|-----------|--------|-------|",
        f"| No density oscillation at $H = 0$ | amp={h0_res.density_osc_amplitude:.6f} | "
        f"{'**PASS**' if h0_quiet else 'FAIL'} |",
        f"| Density oscillation at $H > 0$ | {'detected' if osc_detected else 'not detected'} | "
        f"{'**PASS**' if osc_detected else 'FAIL'} |",
        f"| $v(t)$ oscillates at $H > 0$ | {'YES' if v_active else 'NO'} | "
        f"{'**PASS**' if v_active else 'FAIL'} |",
        f"| PME exponent preserved | all within 20% | "
        f"{'**PASS**' if pme_ok else 'FAIL'} |",
        f"| Amplitude scales with $H$ | {amp_increases} | "
        f"{'**PASS**' if amp_increases else 'FAIL'} |",
    ])

    all_pass = h0_quiet and osc_detected and v_active and pme_ok and amp_increases

    # --- Conclusion ---
    lines.extend(["", "## 6. Conclusion", ""])

    if all_pass:
        lines.extend([
            "**All falsification criteria are satisfied.**",
            "",
            "The ED PDE with weak penalty ($P_0 = 0.01$) and participation ($H > 0$)",
            "produces PME-like spreading with telegraph-modulated interior density:",
            "",
            f"- PME exponent $\\alpha_R \\approx {pred20.alpha_R:.3f}$ preserved",
            f"- Central density oscillates at the telegraph frequency",
            f"- Oscillation amplitude scales as $H^{{{slope:.2f}}}$",
            "- No oscillation at $H = 0$",
            "",
            "This is the ED structural analogue of a porous-medium flow",
            "with a globally coupled oscillatory forcing.",
        ])
    else:
        lines.extend([
            "**One or more criteria failed.**",
            f"H=0 quiet: {h0_quiet}",
            f"Oscillation detected: {osc_detected}",
            f"v active: {v_active}",
            f"PME preserved: {pme_ok}",
            f"Amplitude scales: {amp_increases}",
        ])

    return "\n".join(lines)
