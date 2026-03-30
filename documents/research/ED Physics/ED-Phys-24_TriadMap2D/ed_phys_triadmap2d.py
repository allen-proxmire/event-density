"""
ED-Phys-24: 2D Triad Map
=========================
Maps nonlinear triad interactions and harmonic generation in 2D ED
oscillatory cosmology.  Quantifies coupling coefficient C between modes.

Pure oscillatory:  D=0, H=1.
Unified PDE:
    drho/dt = H*v
    dv/dt   = (1/tau)(F[rho] - zeta*v)
F[rho] = M*Lap2D + M'*|grad|^2 - P_SY2
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
import json
import time as timer_mod

# =========================================================================
#  Canonical Parameters
# =========================================================================
ALPHA    = 0.1
GAMMA    = 0.5
M0       = 1.0
RHO_MAX  = 100.0
N_MOB    = 2
RHO_STAR = 50.0
RHO_0    = 0.5
TAU      = 100.0
ZETA     = 0.5
DX       = 1.0
ETA      = 0.1
EPS      = 1e-10

# =========================================================================
#  Grid
# =========================================================================
NX       = 128
NY       = 128
N_STEPS  = 30_000
SAMPLE   = 50          # 600 snapshots

D_FIXED  = 0.0
H_FIXED  = 1.0

OUT = Path(__file__).parent / "results"
OUT.mkdir(exist_ok=True)


# =========================================================================
#  Core 2D ED operators
# =========================================================================

def mobility(rho):
    return M0 * np.maximum(1.0 - rho / RHO_MAX, 0.0) ** N_MOB

def mobility_prime(rho):
    return -M0 * (N_MOB / RHO_MAX) * np.maximum(1.0 - rho / RHO_MAX, 0.0) ** (N_MOB - 1)

def penalty_sy2(rho):
    delta = rho - RHO_STAR
    return ALPHA * GAMMA * delta / np.sqrt(delta * delta + RHO_0 * RHO_0)

def laplacian_2d(rho, dx):
    return (np.roll(rho, 1, 0) + np.roll(rho, -1, 0)
          + np.roll(rho, 1, 1) + np.roll(rho, -1, 1)
          - 4.0 * rho) / (dx * dx)

def grad_sq_2d(rho, dx):
    gx = (np.roll(rho, -1, 0) - np.roll(rho, 1, 0)) / (2.0 * dx)
    gy = (np.roll(rho, -1, 1) - np.roll(rho, 1, 1)) / (2.0 * dx)
    return gx * gx + gy * gy

def compute_rhs_2d(rho, dx):
    M  = mobility(rho)
    Mp = mobility_prime(rho)
    return M * laplacian_2d(rho, dx) + Mp * grad_sq_2d(rho, dx) - penalty_sy2(rho)


# =========================================================================
#  FFT mode tracking
# =========================================================================

def get_mode_amplitude(rho, kx, ky, rho_star=RHO_STAR):
    """Get amplitude of a specific Fourier mode (kx, ky)."""
    nx, ny = rho.shape
    delta = rho - rho_star
    fft2 = np.fft.fft2(delta) / delta.size
    # map negative k to FFT index
    ix = kx % nx
    iy = ky % ny
    return float(2.0 * np.abs(fft2[ix, iy]))

def get_mode_amplitudes_batch(rho, mode_list, rho_star=RHO_STAR):
    """Get amplitudes for a list of (kx,ky) modes in one FFT."""
    nx, ny = rho.shape
    delta = rho - rho_star
    fft2 = np.fft.fft2(delta) / delta.size
    result = {}
    for (kx, ky) in mode_list:
        ix = kx % nx
        iy = ky % ny
        result[(kx, ky)] = float(2.0 * np.abs(fft2[ix, iy]))
    return result

def mode_energy(rho, v, kx, ky, rho_star=RHO_STAR):
    """Kinetic + potential energy of a single mode."""
    nx, ny = rho.shape
    delta_rho = rho - rho_star
    fft_rho = np.fft.fft2(delta_rho) / delta_rho.size
    fft_v   = np.fft.fft2(v) / v.size
    ix = kx % nx
    iy = ky % ny
    a_rho = np.abs(fft_rho[ix, iy])
    a_v   = np.abs(fft_v[ix, iy])
    # E_k = (tau/2)|v_k|^2 + (1/2)*K_eff*|rho_k|^2
    k_phys = np.sqrt((2*np.pi*kx/nx)**2 + (2*np.pi*ky/ny)**2)
    M_star = M0 * (1.0 - RHO_STAR / RHO_MAX) ** N_MOB
    K_eff  = M_star * k_phys**2 + ALPHA * GAMMA / RHO_0
    e_kin  = 0.5 * TAU * a_v**2
    e_pot  = 0.5 * K_eff * a_rho**2
    return float(e_kin + e_pot)


# =========================================================================
#  Initial conditions
# =========================================================================

def ic_single_mode(nx, ny, kx=4, ky=4, amplitude=5.0):
    x = np.arange(nx, dtype=np.float64)
    y = np.arange(ny, dtype=np.float64)
    X, Y = np.meshgrid(x, y, indexing="ij")
    k_x = 2.0 * np.pi * kx / nx
    k_y = 2.0 * np.pi * ky / ny
    rho = RHO_STAR + amplitude * np.sin(k_x * X + k_y * Y)
    rho = np.clip(rho, EPS, RHO_MAX - EPS)
    v = np.zeros_like(rho)
    return rho, v

def ic_two_mode(nx, ny, k1x=4, k1y=0, k2x=0, k2y=3, a1=5.0, a2=5.0):
    x = np.arange(nx, dtype=np.float64)
    y = np.arange(ny, dtype=np.float64)
    X, Y = np.meshgrid(x, y, indexing="ij")
    kk1x = 2.0 * np.pi * k1x / nx
    kk1y = 2.0 * np.pi * k1y / ny
    kk2x = 2.0 * np.pi * k2x / nx
    kk2y = 2.0 * np.pi * k2y / ny
    rho = RHO_STAR + a1 * np.sin(kk1x * X + kk1y * Y) \
                   + a2 * np.sin(kk2x * X + kk2y * Y)
    rho = np.clip(rho, EPS, RHO_MAX - EPS)
    v = np.zeros_like(rho)
    return rho, v

def ic_explicit_triad(nx, ny, k1x=4, k1y=0, k2x=0, k2y=3,
                      a1=5.0, a2=5.0, eps_seed=0.1):
    """k3 = k1 + k2 seeded at small amplitude."""
    k3x = k1x + k2x
    k3y = k1y + k2y
    x = np.arange(nx, dtype=np.float64)
    y = np.arange(ny, dtype=np.float64)
    X, Y = np.meshgrid(x, y, indexing="ij")
    kk1x = 2.0 * np.pi * k1x / nx
    kk1y = 2.0 * np.pi * k1y / ny
    kk2x = 2.0 * np.pi * k2x / nx
    kk2y = 2.0 * np.pi * k2y / ny
    kk3x = 2.0 * np.pi * k3x / nx
    kk3y = 2.0 * np.pi * k3y / ny
    rho = RHO_STAR + a1 * np.sin(kk1x * X + kk1y * Y) \
                   + a2 * np.sin(kk2x * X + kk2y * Y) \
                   + eps_seed * np.sin(kk3x * X + kk3y * Y)
    rho = np.clip(rho, EPS, RHO_MAX - EPS)
    v = np.zeros_like(rho)
    return rho, v


# =========================================================================
#  Simulation runner
# =========================================================================

def run_triad_experiment(rho, v, track_modes, label,
                         n_steps=N_STEPS, sample_every=SAMPLE):
    """
    Run the PDE and track specific Fourier mode amplitudes over time.
    track_modes: list of (kx, ky) tuples.
    """
    D = D_FIXED
    H = H_FIXED
    dt = ETA * DX * DX / (M0 + EPS)
    cx, cy = NX // 2, NY // 2

    # storage
    time_hist = []
    amp_hist  = {m: [] for m in track_modes}
    energy_hist = {m: [] for m in track_modes}
    peak_hist = []
    clips_total = 0

    t = 0.0
    for step in range(n_steps):
        F = compute_rhs_2d(rho, DX)
        rho_new = rho + dt * (D * F + H * v)
        v_new   = v   + dt * (1.0 / TAU) * (F - ZETA * v)

        clips = int(np.sum(rho_new < EPS))
        clips_total += clips
        rho_new = np.clip(rho_new, EPS, RHO_MAX - EPS)

        rho = rho_new
        v   = v_new
        t  += dt

        if step % sample_every == 0:
            time_hist.append(t)
            peak_hist.append(float(rho[cx, cy]))
            amps = get_mode_amplitudes_batch(rho, track_modes)
            for m in track_modes:
                amp_hist[m].append(amps[m])
                energy_hist[m].append(mode_energy(rho, v, m[0], m[1]))

    return {
        "label":       label,
        "time_hist":   time_hist,
        "amp_hist":    {str(k): v for k, v in amp_hist.items()},
        "energy_hist": {str(k): v for k, v in energy_hist.items()},
        "peak_hist":   peak_hist,
        "total_clips": clips_total,
    }


# =========================================================================
#  Coupling coefficient
# =========================================================================

def compute_coupling(amp_hist, k1, k2, k3):
    """
    C = max(A_k3) / (A_k1_initial * A_k2_initial)
    """
    a1_init = amp_hist[str(k1)][0]
    a2_init = amp_hist[str(k2)][0]
    a3_series = np.array(amp_hist[str(k3)])
    a3_max = float(np.max(a3_series))
    denom = a1_init * a2_init
    if denom < 1e-20:
        return 0.0, a3_max
    return float(a3_max / denom), a3_max


# =========================================================================
#  Plotting
# =========================================================================

def plot_mode_timeseries(result, track_modes, k1, k2, k3, path):
    fig, ax = plt.subplots(figsize=(11, 5))
    t = result["time_hist"]
    colors = {"k1": "steelblue", "k2": "coral", "k3": "seagreen"}
    labels = {str(k1): f"k1={k1}", str(k2): f"k2={k2}", str(k3): f"k3={k3}"}
    main_keys = [str(k1), str(k2), str(k3)]

    for key in main_keys:
        if key in result["amp_hist"]:
            c = colors.get({"0": "k1", "1": "k2", "2": "k3"}.get(
                str(main_keys.index(key)), ""), "gray")
            idx = main_keys.index(key)
            c = ["steelblue", "coral", "seagreen"][idx]
            ax.plot(t, result["amp_hist"][key], color=c, lw=1.0,
                    label=labels.get(key, key))

    # also plot harmonics if tracked
    for m in track_modes:
        key = str(m)
        if key not in main_keys and key in result["amp_hist"]:
            ax.plot(t, result["amp_hist"][key], "--", lw=0.6, alpha=0.6,
                    label=f"{m}")

    ax.set_xlabel("Time")
    ax.set_ylabel("Fourier amplitude")
    ax.set_title(f"{result['label']}: mode amplitudes vs time")
    ax.legend(fontsize=7, ncol=2)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_triad_growth(result, k3, path):
    fig, ax = plt.subplots(figsize=(10, 4))
    t = result["time_hist"]
    a3 = result["amp_hist"][str(k3)]
    ax.plot(t, a3, "o-", ms=2, color="seagreen", lw=0.8)
    ax.set_xlabel("Time")
    ax.set_ylabel(f"A_{k3}")
    ax.set_title(f"{result['label']}: triad mode k3={k3} growth/decay")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_energy_exchange(result, track_modes, k1, k2, k3, path):
    fig, ax = plt.subplots(figsize=(11, 5))
    t = result["time_hist"]
    main_keys = [str(k1), str(k2), str(k3)]
    colors = ["steelblue", "coral", "seagreen"]
    labels = [f"k1={k1}", f"k2={k2}", f"k3={k3}"]
    for key, c, lab in zip(main_keys, colors, labels):
        if key in result["energy_hist"]:
            ax.plot(t, result["energy_hist"][key], color=c, lw=1.0, label=lab)
    ax.set_xlabel("Time")
    ax.set_ylabel("Mode energy")
    ax.set_title(f"{result['label']}: mode energy vs time")
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_phase_flag(label, n_cycles, regime, path):
    cmap = {"oscillatory": "#2196F3", "hybrid": "#FF9800", "parabolic-like": "#4CAF50"}
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_axis_off()
    ax.add_patch(plt.Rectangle((0.05, 0.1), 0.9, 0.8,
                                facecolor=cmap.get(regime, "gray"),
                                edgecolor="black", lw=2, alpha=0.85))
    ax.text(0.5, 0.6, regime.upper(), ha="center", va="center",
            fontsize=24, fontweight="bold", color="white")
    ax.text(0.5, 0.35, f"{label}  |  {n_cycles} cycles",
            ha="center", va="center", fontsize=11, color="white")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_coupling_vs_amplitude(amp_results, path):
    """C vs A for the amplitude sweep."""
    fig, ax = plt.subplots(figsize=(8, 5))
    As = [r["A"] for r in amp_results]
    Cs = [r["C"] for r in amp_results]
    ax.plot(As, Cs, "o-", ms=6, color="darkviolet", lw=1.5)
    ax.set_xlabel("Initial amplitude A")
    ax.set_ylabel("Coupling coefficient C")
    ax.set_title("Triad Coupling Coefficient vs Amplitude")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def plot_triad_map_summary(all_experiments, path):
    """Overview bar chart of all triads and their C values."""
    fig, ax = plt.subplots(figsize=(10, 5))
    labels = [e["label_short"] for e in all_experiments]
    Cs     = [e["C"] for e in all_experiments]
    colors = ["steelblue" if "single" in l.lower() else
              "coral" if "two" in l.lower() else
              "seagreen" for l in labels]
    ax.barh(range(len(labels)), Cs, color=colors, edgecolor="black", height=0.6)
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlabel("Coupling coefficient C = max(A_k3) / (A_k1 * A_k2)")
    ax.set_title("2D Triad Map: Coupling Coefficients")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


# =========================================================================
#  Detect oscillations for phase flag
# =========================================================================

def detect_oscillations(peak_hist, rho_star=RHO_STAR):
    delta = np.array(peak_hist) - rho_star
    crossings = []
    for i in range(1, len(delta)):
        if delta[i - 1] * delta[i] < 0:
            crossings.append(i)
    return len(crossings) // 2


# =========================================================================
#  Main
# =========================================================================

def main():
    print("=" * 70)
    print("ED-Phys-24: 2D Triad Map")
    print("=" * 70)
    print(f"Grid: {NX}x{NY}, {N_STEPS} steps, sample every {SAMPLE}")
    print(f"Pure oscillatory: D={D_FIXED}, H={H_FIXED}")
    print(f"CFL dt = {ETA * DX**2 / M0:.4f}")
    print("=" * 70)

    all_experiments = []

    # Define triad geometry
    k1 = (4, 0)
    k2 = (0, 3)
    k3 = (4, 3)   # k1 + k2
    k3m = (4, -3)  # k1 - k2

    # Harmonics to track
    h_2k1 = (8, 0)
    h_2k2 = (0, 6)
    h_3k1 = (12, 0)
    h_3k2 = (0, 9)

    all_modes = [k1, k2, k3, k3m, h_2k1, h_2k2, h_3k1, h_3k2]

    # =====================================================================
    #  EXPERIMENT 1: Single mode (kx=4, ky=4) - harmonic generation
    # =====================================================================
    print("\n== EXP 1: Single mode (4,4) ==")
    k_single = (4, 4)
    k_s2 = (8, 8)
    k_s3 = (12, 12)
    single_modes = [k_single, k_s2, k_s3, (0, 0)]

    rho, v = ic_single_mode(NX, NY, kx=4, ky=4, amplitude=5.0)
    t0 = timer_mod.time()
    res1 = run_triad_experiment(rho, v, single_modes, "single_mode_4_4")
    print(f"   Time: {timer_mod.time()-t0:.1f}s, clips={res1['total_clips']}")

    a_init = res1["amp_hist"][str(k_single)][0]
    a2_max = max(res1["amp_hist"][str(k_s2)])
    a3_max = max(res1["amp_hist"][str(k_s3)])
    C_2h = a2_max / (a_init**2) if a_init > 1e-20 else 0.0
    C_3h = a3_max / (a_init**3) if a_init > 1e-20 else 0.0
    print(f"   A_init={a_init:.4f}, A_2h_max={a2_max:.6f}, A_3h_max={a3_max:.8f}")
    print(f"   C_2nd_harmonic={C_2h:.6f}, C_3rd_harmonic={C_3h:.8f}")

    n_cyc = detect_oscillations(res1["peak_hist"])
    regime = "oscillatory" if n_cyc >= 3 else ("hybrid" if n_cyc >= 1 else "parabolic-like")
    print(f"   Oscillations: {n_cyc}, regime: {regime}")

    plot_mode_timeseries(res1, single_modes, k_single, k_s2, k_s3,
                         OUT / "single_mode_timeseries.png")
    plot_triad_growth(res1, k_s2, OUT / "single_mode_harmonic_growth.png")
    plot_energy_exchange(res1, single_modes, k_single, k_s2, k_s3,
                         OUT / "single_mode_energy.png")
    plot_phase_flag("single_mode(4,4)", n_cyc, regime,
                    OUT / "single_mode_phase_flag.png")

    all_experiments.append({
        "label": "single_mode_4_4", "label_short": "Single (4,4)->2nd harm",
        "C": C_2h, "k1": k_single, "k2": k_single, "k3": k_s2,
        "A_k3_max": a2_max, "n_cycles": n_cyc,
    })

    # =====================================================================
    #  EXPERIMENT 2: Two-mode triad (k1=(4,0), k2=(0,3))
    # =====================================================================
    print("\n== EXP 2: Two-mode triad k1=(4,0) k2=(0,3) ==")

    rho, v = ic_two_mode(NX, NY, k1x=4, k1y=0, k2x=0, k2y=3, a1=5.0, a2=5.0)
    t0 = timer_mod.time()
    res2 = run_triad_experiment(rho, v, all_modes, "two_mode_triad")
    print(f"   Time: {timer_mod.time()-t0:.1f}s, clips={res2['total_clips']}")

    C_sum, a3sum_max = compute_coupling(res2["amp_hist"], k1, k2, k3)
    C_dif, a3dif_max = compute_coupling(res2["amp_hist"], k1, k2, k3m)
    print(f"   k3_sum={k3}: A_max={a3sum_max:.6f}, C={C_sum:.6f}")
    print(f"   k3_dif={k3m}: A_max={a3dif_max:.6f}, C={C_dif:.6f}")

    a2k1 = max(res2["amp_hist"][str(h_2k1)])
    a2k2 = max(res2["amp_hist"][str(h_2k2)])
    print(f"   2nd harmonics: 2*k1={a2k1:.6f}, 2*k2={a2k2:.6f}")

    n_cyc2 = detect_oscillations(res2["peak_hist"])
    regime2 = "oscillatory" if n_cyc2 >= 3 else ("hybrid" if n_cyc2 >= 1 else "parabolic-like")
    print(f"   Oscillations: {n_cyc2}, regime: {regime2}")

    plot_mode_timeseries(res2, all_modes, k1, k2, k3,
                         OUT / "two_mode_timeseries.png")
    plot_triad_growth(res2, k3, OUT / "two_mode_triad_growth.png")
    plot_energy_exchange(res2, all_modes, k1, k2, k3,
                         OUT / "two_mode_energy.png")
    plot_phase_flag("two_mode (4,0)+(0,3)", n_cyc2, regime2,
                    OUT / "two_mode_phase_flag.png")

    all_experiments.append({
        "label": "two_mode_sum", "label_short": "Two-mode sum (4,0)+(0,3)->(4,3)",
        "C": C_sum, "k1": k1, "k2": k2, "k3": k3,
        "A_k3_max": a3sum_max, "n_cycles": n_cyc2,
    })
    all_experiments.append({
        "label": "two_mode_dif", "label_short": "Two-mode dif (4,0)+(0,3)->(4,-3)",
        "C": C_dif, "k1": k1, "k2": k2, "k3": k3m,
        "A_k3_max": a3dif_max, "n_cycles": n_cyc2,
    })

    # =====================================================================
    #  EXPERIMENT 3: Explicit triad with seed
    # =====================================================================
    print("\n== EXP 3: Explicit triad k1=(4,0) k2=(0,3) k3=(4,3) seeded ==")

    rho, v = ic_explicit_triad(NX, NY, k1x=4, k1y=0, k2x=0, k2y=3,
                                a1=5.0, a2=5.0, eps_seed=0.1)
    t0 = timer_mod.time()
    res3 = run_triad_experiment(rho, v, all_modes, "explicit_triad")
    print(f"   Time: {timer_mod.time()-t0:.1f}s, clips={res3['total_clips']}")

    C_exp, a3exp_max = compute_coupling(res3["amp_hist"], k1, k2, k3)
    print(f"   k3={k3}: A_max={a3exp_max:.6f}, C={C_exp:.6f}")
    print(f"   k3 initial={res3['amp_hist'][str(k3)][0]:.6f} (seeded at 0.1)")

    n_cyc3 = detect_oscillations(res3["peak_hist"])
    regime3 = "oscillatory" if n_cyc3 >= 3 else ("hybrid" if n_cyc3 >= 1 else "parabolic-like")
    print(f"   Oscillations: {n_cyc3}, regime: {regime3}")

    plot_mode_timeseries(res3, all_modes, k1, k2, k3,
                         OUT / "explicit_triad_timeseries.png")
    plot_triad_growth(res3, k3, OUT / "explicit_triad_growth.png")
    plot_energy_exchange(res3, all_modes, k1, k2, k3,
                         OUT / "explicit_triad_energy.png")
    plot_phase_flag("explicit_triad seeded", n_cyc3, regime3,
                    OUT / "explicit_triad_phase_flag.png")

    all_experiments.append({
        "label": "explicit_triad", "label_short": "Explicit triad (seeded k3)",
        "C": C_exp, "k1": k1, "k2": k2, "k3": k3,
        "A_k3_max": a3exp_max, "n_cycles": n_cyc3,
    })

    # =====================================================================
    #  EXPERIMENT 4: Amplitude sweep (C vs A)
    # =====================================================================
    print("\n== EXP 4: Amplitude sweep for coupling coefficient ==")
    A_sweep = [1.0, 2.0, 3.0, 5.0, 8.0, 10.0]
    amp_results = []

    for A in A_sweep:
        rho, v = ic_two_mode(NX, NY, k1x=4, k1y=0, k2x=0, k2y=3, a1=A, a2=A)
        res_a = run_triad_experiment(rho, v, [k1, k2, k3, k3m],
                                     f"amp_A={A:.0f}",
                                     n_steps=20_000, sample_every=100)
        C_a, a3_a = compute_coupling(res_a["amp_hist"], k1, k2, k3)
        print(f"   A={A:.1f}: C_sum={C_a:.6f}, A_k3_max={a3_a:.6f}")
        amp_results.append({"A": A, "C": C_a, "A_k3_max": a3_a})
        all_experiments.append({
            "label": f"amp_sweep_A={A}", "label_short": f"A={A:.0f} sweep",
            "C": C_a, "k1": k1, "k2": k2, "k3": k3,
            "A_k3_max": a3_a, "n_cycles": -1,
        })

    plot_coupling_vs_amplitude(amp_results, OUT / "coupling_vs_amplitude.png")

    # =====================================================================
    #  Summary plots and output
    # =====================================================================
    # Filter to main experiments (not amp sweep) for the summary bar chart
    main_exps = [e for e in all_experiments if "sweep" not in e["label"]]
    plot_triad_map_summary(main_exps, OUT / "triad_map_summary.png")

    # Summary table
    print("\n" + "=" * 95)
    print(f"{'Experiment':>35} | {'k1':>8} | {'k2':>8} | {'k3':>8} | "
          f"{'A_k3_max':>10} | {'C':>10} | {'cycles':>6}")
    print("-" * 95)
    for e in all_experiments:
        k1s = str(e.get("k1", ""))
        k2s = str(e.get("k2", ""))
        k3s = str(e.get("k3", ""))
        print(f"{e['label_short']:>35} | {k1s:>8} | {k2s:>8} | {k3s:>8} | "
              f"{e['A_k3_max']:>10.6f} | {e['C']:>10.6f} | {e['n_cycles']:>6}")
    print("=" * 95)

    # JSON
    export = []
    for e in all_experiments:
        row = dict(e)
        row["k1"] = list(row["k1"]) if isinstance(row["k1"], tuple) else row["k1"]
        row["k2"] = list(row["k2"]) if isinstance(row["k2"], tuple) else row["k2"]
        row["k3"] = list(row["k3"]) if isinstance(row["k3"], tuple) else row["k3"]
        export.append(row)
    with open(OUT / "triad_map_summary.json", "w") as f:
        json.dump({"experiments": export, "amp_sweep": amp_results}, f, indent=2)
    print(f"\nJSON: {OUT / 'triad_map_summary.json'}")
    print("Done.")


if __name__ == "__main__":
    main()
