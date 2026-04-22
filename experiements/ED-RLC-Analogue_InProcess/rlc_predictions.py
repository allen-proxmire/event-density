"""
Pre-registered prediction curves for the ED-RLC-Analogue benchtop experiment.

Generates predicted V_C(t) step-response traces for four runs (A-D) that sweep
the (L, R, C) parameter space in ways that test distinct aspects of the ED
uniform-limit → RLC isomorphism documented in memo.md §3.2.

Mathematical setup
------------------
The ED uniform-limit 2D system reduces to a second-order damped oscillator:

    y'' + 2γ y' + ω₀² y = 0,    2γ = DP₀ + ζ/τ,    ω₀² = (DP₀·ζ + H·κ)/τ

Under the ED→circuit mapping (memo §3.2), this is *exactly* isomorphic to a
series RLC circuit with

    V_C'' + (R/L) V_C' + (1/LC)(V_C - V₀) = 0,    2γ = R/L,    ω₀² = 1/LC

for step-input V₀ applied at t=0 with V_C(0) = 0, V_C'(0) = 0.

Underdamped (γ < ω₀) step-response:

    V_C(t) = V₀ [1 - e^(-γt) (cos(ωt) + (γ/ω) sin(ωt))]
           = V₀ [1 - (1/ω) e^(-γt) ω₀ cos(ωt - φ)]    with tan(φ) = γ/ω

where ω = √(ω₀² - γ²) is the damped oscillation frequency.

For the ringdown from pre-charged capacitor (V_C(0) = V₀, source disconnected):

    V_C(t) = V₀ e^(-γt) (cos(ωt) + (γ/ω) sin(ωt))

Both traces are produced for each run.

Runs
----
A:  L=10mH, C=1µF, R = DCR only (~30 Ω)         — canonical, moderate Q
B:  L=10mH, C=1µF, R = 30+50 = 80 Ω total       — heavy damping, near-critical
C:  L=1mH,  C=1µF, R = DCR only (~3 Ω)          — high Q, 10× higher frequency
D:  L=100µH,C=1µF, R = DCR only (~0.5 Ω)        — highest frequency + very high Q

C is fixed at 1 µF (built from parallel 0.47 + 0.56 µF from the kit).
L swept across the three Bourns RLB0913 inductors Allen ordered.
R varied via DCR + optional external series resistor.

Outputs
-------
- rlc_predictions/predicted_run_A.png through predicted_run_D.png
- rlc_predictions/all_runs_combined.png
- rlc_predictions/summary_table.json  (for programmatic comparison post-bench)

Dependencies: numpy, matplotlib
"""

from pathlib import Path
import json
import numpy as np
import matplotlib.pyplot as plt


# =================================================================
# Circuit / ED uniform-limit analytic predictions
# =================================================================

def predict_rlc(L, R, C, V0=9.0):
    """Return (gamma, omega0, omega, Q, regime, period_us, envelope_tau_us)."""
    gamma = R / (2 * L)
    omega0 = 1.0 / np.sqrt(L * C)
    if omega0 > gamma:
        regime = "underdamped"
        omega = np.sqrt(omega0 * omega0 - gamma * gamma)
    elif np.isclose(omega0, gamma):
        regime = "critically damped"
        omega = 0.0
    else:
        regime = "overdamped"
        omega = 0.0
    Q = omega0 / (2 * gamma) if gamma > 0 else np.inf
    period_s = 2 * np.pi / omega if omega > 0 else np.inf
    envelope_tau_s = 1.0 / gamma if gamma > 0 else np.inf
    return dict(gamma=gamma, omega0=omega0, omega=omega, Q=Q,
                regime=regime, period_s=period_s,
                envelope_tau_s=envelope_tau_s, V0=V0, L=L, R=R, C=C)


def step_response(t, pr):
    """V_C(t) for step input V0 applied at t=0, V_C(0)=0, V_C'(0)=0.

    For underdamped case returns V_C; for overdamped returns the overdamped form."""
    V0 = pr["V0"]
    gamma = pr["gamma"]
    if pr["regime"] == "underdamped":
        omega = pr["omega"]
        env = np.exp(-gamma * t)
        return V0 * (1 - env * (np.cos(omega * t) + (gamma / omega) * np.sin(omega * t)))
    elif pr["regime"] == "critically damped":
        return V0 * (1 - np.exp(-gamma * t) * (1 + gamma * t))
    else:  # overdamped
        omega0 = pr["omega0"]
        disc = np.sqrt(gamma * gamma - omega0 * omega0)
        lam1 = -gamma + disc
        lam2 = -gamma - disc
        A = -lam2 / (lam1 - lam2)
        B = lam1 / (lam1 - lam2)
        return V0 * (1 + A * np.exp(lam1 * t) + B * np.exp(lam2 * t))


def ringdown_response(t, pr):
    """V_C(t) for ringdown from pre-charged V_C(0)=V0, V_C'(0)=0, source removed.

    Series RLC homogeneous: V'' + 2γ V' + ω₀² V = 0."""
    V0 = pr["V0"]
    gamma = pr["gamma"]
    if pr["regime"] == "underdamped":
        omega = pr["omega"]
        env = np.exp(-gamma * t)
        return V0 * env * (np.cos(omega * t) + (gamma / omega) * np.sin(omega * t))
    elif pr["regime"] == "critically damped":
        return V0 * np.exp(-gamma * t) * (1 + gamma * t)
    else:
        omega0 = pr["omega0"]
        disc = np.sqrt(gamma * gamma - omega0 * omega0)
        lam1 = -gamma + disc
        lam2 = -gamma - disc
        A = -lam2 / (lam1 - lam2)
        B = lam1 / (lam1 - lam2)
        return V0 * (A * np.exp(lam1 * t) + B * np.exp(lam2 * t))


# =================================================================
# Run definitions
# =================================================================

RUNS = {
    "A": dict(label="Canonical Q≈3 (10mH, 1µF, DCR-only)",
              L=10e-3, R=30.0, C=1e-6,
              inductor_part="Bourns RLB0913-103KL (10 mH, DCR ≈ 30 Ω)",
              external_R=0.0,
              purpose="Baseline — default benchtop configuration; clean ringdown with ~5 visible cycles."),
    "B": dict(label="Heavy damping (10mH, 1µF, R=80Ω total)",
              L=10e-3, R=80.0, C=1e-6,
              inductor_part="Bourns RLB0913-103KL (10 mH, DCR ≈ 30 Ω)",
              external_R=50.0,
              purpose="Near-critical damping; demonstrates the γ/ω₀ ratio controls oscillation count."),
    "C": dict(label="L-swap: 1mH (high-Q, 10× faster)",
              L=1e-3, R=3.0, C=1e-6,
              inductor_part="Bourns RLB0913-102KL (1 mH, DCR ≈ 3 Ω)",
              external_R=0.0,
              purpose="Higher frequency + higher Q; tests ω₀ ∝ 1/√L scaling."),
    "D": dict(label="L-swap: 100µH (very-high-Q, 100× faster)",
              L=100e-6, R=0.5, C=1e-6,
              inductor_part="Bourns RLB0913-101KL (100 µH, DCR ≈ 0.5 Ω)",
              external_R=0.0,
              purpose="Highest accessible frequency; pushes scope timebase but still within 50 MSa/s limit."),
}


# =================================================================
# Figure 1: per-run predicted trace
# =================================================================

def plot_run(run_id, run, outpath):
    pr = predict_rlc(run["L"], run["R"], run["C"])
    # Time axis: span ~5 envelope time constants to see full decay
    T_total = min(6 * pr["envelope_tau_s"], 50 * pr["period_s"])
    t = np.linspace(0, T_total, 4000)
    V_ring = ringdown_response(t, pr)
    V_step = step_response(t, pr)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 7), sharex=True)

    # Ringdown (top panel)
    ax1.plot(t * 1e6, V_ring, "C0", lw=1.5, label="V_C(t) — ringdown from V₀")
    env = pr["V0"] * np.exp(-pr["gamma"] * t)
    ax1.plot(t * 1e6, env, "C1--", lw=0.9, alpha=0.7, label=f"envelope ±V₀·e^(-γt), τ_env = {pr['envelope_tau_s']*1e6:.1f} µs")
    ax1.plot(t * 1e6, -env, "C1--", lw=0.9, alpha=0.7)
    ax1.axhline(0, color="k", lw=0.3, alpha=0.4)
    ax1.set_ylabel("V_C  (V)")
    ax1.set_title(f"Run {run_id}:  {run['label']}", fontsize=12)
    ax1.legend(loc="upper right", fontsize=9)
    ax1.grid(True, alpha=0.3)

    # Step response (bottom panel)
    ax2.plot(t * 1e6, V_step, "C3", lw=1.5, label="V_C(t) — step input V₀ applied at t=0")
    ax2.axhline(pr["V0"], color="k", ls=":", lw=0.6, alpha=0.6, label=f"V₀ = {pr['V0']:.1f} V")
    ax2.axhline(0, color="k", lw=0.3, alpha=0.4)
    ax2.set_xlabel("time  (µs)")
    ax2.set_ylabel("V_C  (V)")
    ax2.legend(loc="lower right", fontsize=9)
    ax2.grid(True, alpha=0.3)

    # Text box with predicted measurements
    text = (f"L = {pr['L']*1e3:.2f} mH    R = {pr['R']:.1f} Ω    C = {pr['C']*1e6:.2f} µF\n"
            f"ω₀ = 1/√(LC)       = {pr['omega0']:8.1f} rad/s   ({pr['omega0']/(2*np.pi):.1f} Hz)\n"
            f"γ  = R/(2L)        = {pr['gamma']:8.1f} /s\n"
            f"ω  = √(ω₀²−γ²)     = {pr['omega']:8.1f} rad/s   ({pr['omega']/(2*np.pi):.1f} Hz)\n"
            f"T  = 2π/ω          = {pr['period_s']*1e6:8.2f} µs\n"
            f"Q  = ω₀/(2γ)       = {pr['Q']:8.2f}\n"
            f"Regime: {pr['regime']}\n"
            f"Visible cycles before 1% amplitude: {pr['Q']*np.log(100)/np.pi:.1f}")
    fig.text(0.15, -0.02, text, fontsize=10, family="monospace",
             bbox=dict(boxstyle="round,pad=0.5", fc="lemonchiffon",
                       ec="gray", alpha=0.95))

    fig.tight_layout(rect=[0, 0.05, 1, 1])
    fig.savefig(outpath, dpi=140, bbox_inches="tight")
    plt.close(fig)
    return pr


# =================================================================
# Figure 2: all runs overlaid for direct comparison
# =================================================================

def plot_combined(all_results, outpath):
    fig, axes = plt.subplots(2, 2, figsize=(14, 9))
    axes = axes.flatten()
    for ax, (run_id, (run, pr)) in zip(axes, all_results.items()):
        T_total = min(6 * pr["envelope_tau_s"], 50 * pr["period_s"])
        t = np.linspace(0, T_total, 4000)
        V = ringdown_response(t, pr)
        env = pr["V0"] * np.exp(-pr["gamma"] * t)

        ax.plot(t * 1e6, V, lw=1.3, label="V_C(t)")
        ax.plot(t * 1e6, env, "--", color="gray", lw=0.8, alpha=0.7)
        ax.plot(t * 1e6, -env, "--", color="gray", lw=0.8, alpha=0.7)
        ax.axhline(0, color="k", lw=0.3, alpha=0.4)

        ax.set_xlabel("time (µs)")
        ax.set_ylabel("V_C (V)")
        ax.set_title(f"Run {run_id}: {run['label']}\n"
                     f"f = {pr['omega']/(2*np.pi):.0f} Hz   "
                     f"Q = {pr['Q']:.2f}   "
                     f"T = {pr['period_s']*1e6:.1f} µs   "
                     f"τ_env = {pr['envelope_tau_s']*1e6:.0f} µs",
                     fontsize=10)
        ax.grid(True, alpha=0.3)

    fig.suptitle("ED-RLC-Analogue: pre-registered predicted ringdown traces for four runs",
                 fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(outpath, dpi=140, bbox_inches="tight")
    plt.close(fig)


# =================================================================
# Main
# =================================================================

def main():
    here = Path(__file__).parent
    outdir = here / "rlc_predictions"
    outdir.mkdir(exist_ok=True)

    all_results = {}
    for run_id, run in RUNS.items():
        figpath = outdir / f"predicted_run_{run_id}.png"
        pr = plot_run(run_id, run, figpath)
        all_results[run_id] = (run, pr)
        print(f"Run {run_id}: f={pr['omega']/(2*np.pi):.0f} Hz, "
              f"Q={pr['Q']:.2f}, regime={pr['regime']}, "
              f"τ_env={pr['envelope_tau_s']*1e6:.1f} µs")

    plot_combined(all_results, outdir / "all_runs_combined.png")

    # Summary JSON for programmatic comparison post-bench
    summary = {}
    for run_id, (run, pr) in all_results.items():
        summary[run_id] = {
            "label": run["label"],
            "purpose": run["purpose"],
            "inductor_part": run["inductor_part"],
            "external_R_ohm": run["external_R"],
            "L_mH": run["L"] * 1e3,
            "R_total_ohm": run["R"],
            "C_uF": run["C"] * 1e6,
            "predicted": {
                "omega0_rad_s": pr["omega0"],
                "gamma_per_s": pr["gamma"],
                "omega_rad_s": pr["omega"],
                "frequency_Hz": pr["omega"] / (2 * np.pi),
                "period_us": pr["period_s"] * 1e6,
                "envelope_tau_us": pr["envelope_tau_s"] * 1e6,
                "Q": pr["Q"],
                "regime": pr["regime"],
                "visible_cycles_to_1pct": pr["Q"] * np.log(100) / np.pi,
            },
            "measured": {
                "omega_rad_s": None,
                "gamma_per_s": None,
                "frequency_Hz": None,
                "Q": None,
                "notes": "",
            }
        }
    (outdir / "summary_table.json").write_text(json.dumps(summary, indent=2))
    print(f"\nWrote summary: {outdir / 'summary_table.json'}")


if __name__ == "__main__":
    main()
