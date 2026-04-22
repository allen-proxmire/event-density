"""
C7 Triad Coupling — Simulation Calibration Companion
=====================================================

Target: calibrate the predicted A_3/A_1 band and scaling for the
Nonlinear Triad Coupling experiment defined in
experiements/Triad-Coupling-C7_InProcess/protocol.md.

Setup
-----
1D periodic domain [0, 2*pi], N=256, spectral FFT derivatives.
Isolate mobility-channel triad by setting H = 0.
Use beta = 2 (UDM high-BSA mobility, M''(rho) != 0 -> direct k=3 source).

Canonical F[rho] = M(rho) rho_xx + M'(rho) (rho_x)^2 - P(rho)
with
  M(rho) = M0 * ((rho_max - rho)/rho_max)^beta
  P(rho) = P0 * (rho - rho_star)

Seed rho(x, 0) = rho_star + A1 * cos(x)  (monochromatic k=1)

Sweep A1 in {0.01, 0.02, 0.05, 0.1, 0.2}.
At each snapshot, FFT rho and extract A(k=1), A(k=2), A(k=3).
Fit log(A3) vs log(A1) across the sweep at quasi-steady reference time.

Output: JSON + text report.
"""

from __future__ import annotations

import json
import os
import numpy as np


# ------------------------------------------------------------------ #
#  Parameters                                                         #
# ------------------------------------------------------------------ #

N = 256
L = 2.0 * np.pi
DX = L / N
X = np.arange(N) * DX

RHO_STAR = 0.5
RHO_MAX = 1.0
M0 = 1.0
BETA = 2.0
P0 = 0.01
D_WEIGHT = 0.3            # D channel weight from canon
DT = 1.0e-3
T_END = 2.0               # keep short; quasi-steady is reached quickly
SNAP_DT = 0.02            # 100 snaps per run

A1_SWEEP = [0.01, 0.02, 0.05, 0.10, 0.20]

# Reference time (quasi-steady): k=3 dissipation timescale is ~1/(9 M(rho*) k^2 D)
# = 1/(9 * 0.25 * 1 * 0.3) ~ 1.5 sec, so pick t_ref after this
T_REF = 1.0


# ------------------------------------------------------------------ #
#  Spectral derivatives                                               #
# ------------------------------------------------------------------ #

K = np.fft.fftfreq(N, d=DX) * 2.0 * np.pi    # wavenumbers
IK = 1j * K

def dx(rho):
    return np.real(np.fft.ifft(IK * np.fft.fft(rho)))

def dxx(rho):
    return np.real(np.fft.ifft(-(K ** 2) * np.fft.fft(rho)))


# ------------------------------------------------------------------ #
#  Constitutive                                                        #
# ------------------------------------------------------------------ #

def mobility(rho):
    frac = np.clip((RHO_MAX - rho) / RHO_MAX, 0.0, 1.0)
    return M0 * frac ** BETA

def mobility_deriv(rho):
    # dM/drho = - M0 * beta / rho_max * ((rho_max - rho)/rho_max)^(beta-1)
    frac = np.clip((RHO_MAX - rho) / RHO_MAX, 0.0, 1.0)
    return -M0 * BETA / RHO_MAX * frac ** (BETA - 1.0)

def penalty(rho):
    return P0 * (rho - RHO_STAR)


# ------------------------------------------------------------------ #
#  Canonical F[rho] operator (mobility + penalty; H = 0)             #
# ------------------------------------------------------------------ #

def F_operator(rho):
    r_x = dx(rho)
    r_xx = dxx(rho)
    M = mobility(rho)
    Mp = mobility_deriv(rho)
    P = penalty(rho)
    return M * r_xx + Mp * (r_x ** 2) - P


# ------------------------------------------------------------------ #
#  Time stepping — RK2 (Heun), explicit                              #
# ------------------------------------------------------------------ #

def step(rho, dt):
    F1 = F_operator(rho)
    rho_pred = rho + dt * D_WEIGHT * F1
    F2 = F_operator(rho_pred)
    return rho + 0.5 * dt * D_WEIGHT * (F1 + F2)


# ------------------------------------------------------------------ #
#  Diagnostics                                                        #
# ------------------------------------------------------------------ #

def mode_amplitudes(rho, ks=(1, 2, 3)):
    """Return amplitudes of cosine modes at the given integer wavenumbers."""
    F = np.fft.fft(rho) / N
    out = {}
    for k in ks:
        # cos(k x) coefficient -> 2 * Re(F[k]) for k > 0
        out[k] = 2.0 * np.abs(F[k])
    return out


def mode_phases(rho, ks=(1, 3)):
    """Phase of each mode in rad."""
    F = np.fft.fft(rho) / N
    return {k: float(np.angle(F[k])) for k in ks}


# ------------------------------------------------------------------ #
#  Single run                                                         #
# ------------------------------------------------------------------ #

def run_single(A1_init):
    rho = RHO_STAR + A1_init * np.cos(X)
    t = 0.0
    times = [0.0]
    A1_hist = [mode_amplitudes(rho)[1]]
    A2_hist = [mode_amplitudes(rho)[2]]
    A3_hist = [mode_amplitudes(rho)[3]]
    phi1_hist = [mode_phases(rho)[1]]
    phi3_hist = [mode_phases(rho)[3]]

    next_snap = SNAP_DT
    n_steps = int(np.ceil(T_END / DT))
    for _ in range(n_steps):
        rho = step(rho, DT)
        t += DT
        if t >= next_snap - DT / 2:
            times.append(t)
            A = mode_amplitudes(rho)
            P = mode_phases(rho)
            A1_hist.append(A[1])
            A2_hist.append(A[2])
            A3_hist.append(A[3])
            phi1_hist.append(P[1])
            phi3_hist.append(P[3])
            next_snap += SNAP_DT

    return {
        "A1_init": A1_init,
        "times": np.array(times),
        "A1": np.array(A1_hist),
        "A2": np.array(A2_hist),
        "A3": np.array(A3_hist),
        "phi1": np.array(phi1_hist),
        "phi3": np.array(phi3_hist),
    }


# ------------------------------------------------------------------ #
#  Sweep + analysis                                                   #
# ------------------------------------------------------------------ #

def nearest_time_index(times, t_target):
    return int(np.argmin(np.abs(times - t_target)))


def analyze_sweep(runs, t_ref=T_REF):
    A1_ref = []
    A2_ref = []
    A3_ref = []
    ratio_31 = []
    ratio_21 = []
    phase_offsets = []  # phi3 - 3 * phi1

    for r in runs:
        i = nearest_time_index(r["times"], t_ref)
        A1 = r["A1"][i]
        A2 = r["A2"][i]
        A3 = r["A3"][i]
        A1_ref.append(A1)
        A2_ref.append(A2)
        A3_ref.append(A3)
        ratio_31.append(A3 / A1 if A1 > 0 else 0.0)
        ratio_21.append(A2 / A1 if A1 > 0 else 0.0)
        dphi = r["phi3"][i] - 3.0 * r["phi1"][i]
        # wrap to [-pi, pi]
        dphi = (dphi + np.pi) % (2 * np.pi) - np.pi
        phase_offsets.append(dphi)

    A1_ref = np.array(A1_ref)
    A3_ref = np.array(A3_ref)
    ratio_31 = np.array(ratio_31)

    # Fit log(A3) vs log(A1) --> slope in amplitude units
    mask = (A1_ref > 0) & (A3_ref > 0)
    if mask.sum() >= 2:
        p = np.polyfit(np.log(A1_ref[mask]), np.log(A3_ref[mask]), 1)
        slope_A3_vs_A1 = float(p[0])
        intercept_A3_vs_A1 = float(p[1])
    else:
        slope_A3_vs_A1 = 0.0
        intercept_A3_vs_A1 = 0.0

    # Fit log(A3/A1) vs log(A1) --> slope of ratio
    if mask.sum() >= 2:
        p = np.polyfit(np.log(A1_ref[mask]), np.log(ratio_31[mask]), 1)
        slope_ratio_vs_A1 = float(p[0])
    else:
        slope_ratio_vs_A1 = 0.0

    return {
        "A1_ref": A1_ref.tolist(),
        "A2_ref": A2_ref,
        "A3_ref": A3_ref.tolist(),
        "ratio_A3_A1": ratio_31.tolist(),
        "ratio_A2_A1": ratio_21,
        "phase_offset_rad": phase_offsets,
        "slope_log_A3_vs_log_A1": slope_A3_vs_A1,
        "intercept_log_A3_vs_log_A1": intercept_A3_vs_A1,
        "slope_log_ratio_vs_log_A1": slope_ratio_vs_A1,
        "t_ref": t_ref,
    }


# ------------------------------------------------------------------ #
#  Main                                                               #
# ------------------------------------------------------------------ #

def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    results = []
    print(f"Running triad calibration sweep over A1 = {A1_SWEEP}")
    print(f"  N={N}, L=2*pi, beta={BETA}, D={D_WEIGHT}, P0={P0}, H=0")
    print(f"  dt={DT}, T_end={T_END}, t_ref={T_REF}")
    print()

    for A1 in A1_SWEEP:
        r = run_single(A1)
        results.append(r)
        i = nearest_time_index(r["times"], T_REF)
        print(f"  A1_init={A1:.3f}  |  t={r['times'][i]:.3f}  "
              f"A1={r['A1'][i]:.4e}  A2={r['A2'][i]:.4e}  A3={r['A3'][i]:.4e}  "
              f"A3/A1={r['A3'][i]/r['A1'][i]:.4e}")

    analysis = analyze_sweep(results, t_ref=T_REF)

    print()
    print(f"Slope log(A3) vs log(A1)    = {analysis['slope_log_A3_vs_log_A1']:.3f}  (expect ~3)")
    print(f"Slope log(A3/A1) vs log(A1) = {analysis['slope_log_ratio_vs_log_A1']:.3f}  (expect ~2)")
    print(f"A3/A1 at each A1: {[f'{x:.3e}' for x in analysis['ratio_A3_A1']]}")
    print(f"Phase offsets (phi3 - 3*phi1) [rad]: {[f'{x:+.3f}' for x in analysis['phase_offset_rad']]}")

    # Save full results
    payload = {
        "parameters": {
            "N": N, "L": float(L), "beta": BETA, "D": D_WEIGHT,
            "P0": P0, "M0": M0, "rho_star": RHO_STAR, "rho_max": RHO_MAX,
            "dt": DT, "T_end": T_END, "t_ref": T_REF,
            "A1_sweep": A1_SWEEP,
        },
        "analysis": analysis,
        "time_series": [
            {
                "A1_init": r["A1_init"],
                "times": r["times"].tolist(),
                "A1": r["A1"].tolist(),
                "A2": r["A2"].tolist(),
                "A3": r["A3"].tolist(),
                "phi1": r["phi1"].tolist(),
                "phi3": r["phi3"].tolist(),
            }
            for r in results
        ],
    }

    out_file = os.path.join(out_dir, "triad_calibration_results.json")
    with open(out_file, "w") as f:
        json.dump(payload, f, indent=2)
    print()
    print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()
