"""
ED-Phys-23: 2D Oscillatory Cosmology
======================================
Tests the unified ED cosmology PDE in 2D with pure oscillatory dynamics
(D=0, H=1). Measures radial mode stability, standing wave persistence,
2D mode coupling, and searches for new motifs.

Unified PDE:
    drho/dt = D*F[rho] + H*v
    dv/dt   = (1/tau)(F[rho] - zeta*v)
    D + H = 1,  D = 0,  H = 1  (pure oscillatory)

F[rho] = M(rho)*Lap2D(rho) + M'(rho)*|grad(rho)|^2 - P_SY2(rho)
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
ETA      = 0.1        # CFL factor for 2D (half of 1D value)
EPS      = 1e-10

HORIZON_THRESH = 0.9 * RHO_MAX

# =========================================================================
#  Grid
# =========================================================================
NX       = 128         # 128x128 for tractability
NY       = 128
N_STEPS  = 40_000
SAMPLE   = 100         # sample every 100 steps -> 400 snapshots
SNAP_STEPS = [0, 500, 2000, 5000, 10000, 20000, 39999]  # heatmap snapshots

# =========================================================================
#  Fixed mixing (pure oscillatory)
# =========================================================================
D_FIXED  = 0.0
H_FIXED  = 1.0

OUT = Path(__file__).parent / "results"
OUT.mkdir(exist_ok=True)
SNAP_DIR = OUT / "snapshots"
SNAP_DIR.mkdir(exist_ok=True)


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
    lap = laplacian_2d(rho, dx)
    gsq = grad_sq_2d(rho, dx)
    return M * lap + Mp * gsq - penalty_sy2(rho)


# =========================================================================
#  Initial conditions
# =========================================================================

def ic_radial_gaussian(nx, ny, amplitude=40.0, sigma=15.0):
    """Radial Gaussian peak centered on grid."""
    x = np.arange(nx, dtype=np.float64) - nx / 2.0
    y = np.arange(ny, dtype=np.float64) - ny / 2.0
    X, Y = np.meshgrid(x, y, indexing="ij")
    r2 = X * X + Y * Y
    rho = RHO_STAR + amplitude * np.exp(-0.5 * r2 / (sigma * sigma))
    rho = np.clip(rho, EPS, RHO_MAX - EPS)
    v = np.zeros_like(rho)
    return rho, v, "radial_gaussian"

def ic_standing_wave(nx, ny, amplitude=5.0, n_modes=4):
    """2D standing wave: sin(kx*x)*sin(ky*y)."""
    x = np.arange(nx, dtype=np.float64)
    y = np.arange(ny, dtype=np.float64)
    X, Y = np.meshgrid(x, y, indexing="ij")
    kx = 2.0 * np.pi * n_modes / nx
    ky = 2.0 * np.pi * n_modes / ny
    rho = RHO_STAR + amplitude * np.sin(kx * X) * np.sin(ky * Y)
    rho = np.clip(rho, EPS, RHO_MAX - EPS)
    v = np.zeros_like(rho)
    return rho, v, "standing_wave"

def ic_two_mode(nx, ny, a1=5.0, a2=3.0, k1_n=3, k2_n=5):
    """Two-mode superposition: A1*sin(k1*x) + A2*sin(k2*y)."""
    x = np.arange(nx, dtype=np.float64)
    y = np.arange(ny, dtype=np.float64)
    X, Y = np.meshgrid(x, y, indexing="ij")
    k1 = 2.0 * np.pi * k1_n / nx
    k2 = 2.0 * np.pi * k2_n / ny
    rho = RHO_STAR + a1 * np.sin(k1 * X) + a2 * np.sin(k2 * Y)
    rho = np.clip(rho, EPS, RHO_MAX - EPS)
    v = np.zeros_like(rho)
    return rho, v, "two_mode"


# =========================================================================
#  2D mode analysis (FFT-based)
# =========================================================================

def mode_spectrum_2d(rho, rho_star=RHO_STAR):
    """Compute 2D FFT power spectrum."""
    delta = rho - rho_star
    fft2 = np.fft.fft2(delta)
    power = np.abs(fft2) ** 2 / (delta.size ** 2)
    return power

def radial_power_spectrum(power, nx, ny):
    """Azimuthally averaged power spectrum."""
    kx = np.fft.fftfreq(nx, d=1.0)
    ky = np.fft.fftfreq(ny, d=1.0)
    KX, KY = np.meshgrid(kx, ky, indexing="ij")
    kr = np.sqrt(KX**2 + KY**2)

    # bin by radial wavenumber
    k_max = 0.5  # Nyquist
    n_bins = min(nx, ny) // 2
    k_bins = np.linspace(0, k_max, n_bins + 1)
    spectrum = np.zeros(n_bins)
    for i in range(n_bins):
        mask = (kr >= k_bins[i]) & (kr < k_bins[i + 1])
        if np.sum(mask) > 0:
            spectrum[i] = np.mean(power[mask])
    k_centers = 0.5 * (k_bins[:-1] + k_bins[1:])
    return k_centers, spectrum

def measure_anisotropy(rho, rho_star=RHO_STAR):
    """Measure x-variance vs y-variance to detect anisotropy."""
    delta = rho - rho_star
    var_x = np.var(np.mean(delta, axis=1))  # variance along x (averaged over y)
    var_y = np.var(np.mean(delta, axis=0))  # variance along y (averaged over x)
    if var_x + var_y < 1e-20:
        return 1.0  # isotropic by default
    return var_x / (var_x + var_y)  # 0.5 = isotropic

def check_radial_symmetry(rho, rho_star=RHO_STAR):
    """Measure deviation from radial symmetry."""
    nx, ny = rho.shape
    delta = rho - rho_star
    cx, cy = nx // 2, ny // 2
    # compare opposite quadrants
    q1 = delta[:cx, :cy]
    q2 = delta[:cx, cy:][:, ::-1]
    q3 = delta[cx:, :cy][::-1, :]
    q4 = delta[cx:, cy:][::-1, ::-1]
    min_shape = (min(q1.shape[0], q3.shape[0]), min(q1.shape[1], q2.shape[1]))
    q1 = q1[:min_shape[0], :min_shape[1]]
    q2 = q2[:min_shape[0], :min_shape[1]]
    q3 = q3[:min_shape[0], :min_shape[1]]
    q4 = q4[:min_shape[0], :min_shape[1]]
    mean_q = (q1 + q2 + q3 + q4) / 4.0
    dev = np.sqrt(np.mean((q1 - mean_q)**2 + (q2 - mean_q)**2
                        + (q3 - mean_q)**2 + (q4 - mean_q)**2))
    scale = np.std(delta) + 1e-20
    return float(dev / scale)

def top_modes_2d(rho, rho_star=RHO_STAR, n_top=8):
    """Return top n_top Fourier modes by amplitude."""
    delta = rho - rho_star
    nx, ny = delta.shape
    fft2 = np.fft.fft2(delta) / delta.size
    amps = np.abs(fft2)
    # flatten and sort
    flat_idx = np.argsort(amps.ravel())[::-1]
    modes = []
    for idx in flat_idx[:n_top]:
        ix, iy = np.unravel_index(idx, (nx, ny))
        # map to centered frequencies
        kx = ix if ix <= nx // 2 else ix - nx
        ky = iy if iy <= ny // 2 else iy - ny
        modes.append({"kx": int(kx), "ky": int(ky),
                       "amplitude": float(amps[ix, iy])})
    return modes


# =========================================================================
#  Time integrator
# =========================================================================

def run_2d_case(ic_func, D=D_FIXED, n_steps=N_STEPS, sample_every=SAMPLE):
    H = 1.0 - D
    rho, v, ic_name = ic_func(NX, NY)
    cx, cy = NX // 2, NY // 2
    dt = ETA * DX * DX / (M0 + EPS)

    # storage
    peak_hist       = []
    mean_hist       = []
    std_hist        = []
    time_hist       = []
    horizon_hist    = []
    anisotropy_hist = []
    radial_sym_hist = []
    clips_total     = 0

    # mode energy tracking: store radial spectra at sample times
    spectra_times   = []
    spectra_data    = []

    # top modes at start and end
    top_modes_start = top_modes_2d(rho)

    # snapshot storage
    snapshots = {}

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
            peak_hist.append(float(rho[cx, cy]))
            mean_hist.append(float(np.mean(rho)))
            std_hist.append(float(np.std(rho)))
            time_hist.append(t)
            horizon_hist.append(int(np.sum(rho >= HORIZON_THRESH)))
            anisotropy_hist.append(measure_anisotropy(rho))

        if step in SNAP_STEPS:
            snapshots[step] = rho.copy()
            power = mode_spectrum_2d(rho)
            k_c, spec = radial_power_spectrum(power, NX, NY)
            spectra_times.append(t)
            spectra_data.append(spec.tolist())
            if ic_name == "radial_gaussian":
                radial_sym_hist.append({
                    "step": step, "time": t,
                    "radial_dev": check_radial_symmetry(rho)
                })

    top_modes_end = top_modes_2d(rho)

    return {
        "ic_name":          ic_name,
        "D": D, "H": H, "dt": dt, "n_steps": n_steps,
        "nx": NX, "ny": NY,
        "peak_hist":        peak_hist,
        "mean_hist":        mean_hist,
        "std_hist":         std_hist,
        "time_hist":        time_hist,
        "horizon_hist":     horizon_hist,
        "anisotropy_hist":  anisotropy_hist,
        "radial_sym_hist":  radial_sym_hist,
        "total_clips":      clips_total,
        "final_rho_peak":   float(rho[cx, cy]),
        "final_rho_std":    float(np.std(rho)),
        "top_modes_start":  top_modes_start,
        "top_modes_end":    top_modes_end,
        "spectra_times":    spectra_times,
        "spectra_data":     spectra_data,
        "k_centers":        k_c.tolist(),
        "snapshots":        snapshots,
    }


# =========================================================================
#  Analysis
# =========================================================================

def detect_oscillations(peak_hist, rho_star=RHO_STAR):
    delta = np.array(peak_hist) - rho_star
    crossings = []
    for i in range(1, len(delta)):
        if delta[i - 1] * delta[i] < 0:
            crossings.append(i)
    n_cycles = len(crossings) // 2
    amplitudes = []
    for i in range(len(crossings) - 1):
        seg = delta[crossings[i]:crossings[i + 1]]
        if len(seg) > 0:
            amplitudes.append(float(np.max(np.abs(seg))))
    return n_cycles, amplitudes, crossings

def classify_regime(n_cycles):
    if n_cycles >= 3:
        return "oscillatory"
    elif n_cycles >= 1:
        return "hybrid"
    else:
        return "parabolic-like"


# =========================================================================
#  Plotting
# =========================================================================

def plot_time_series(result, path):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(result["time_hist"], result["peak_hist"], "k-", lw=0.8)
    ax.axhline(RHO_STAR, color="blue", ls="--", alpha=0.5, label=r"$\rho^*$")
    ax.set_xlabel("Time")
    ax.set_ylabel(r"$\rho$ at center")
    ax.set_title(f"2D {result['ic_name']}: center density vs time  (D={result['D']})")
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)

def plot_envelope(result, n_cycles, amplitudes, path):
    fig, ax = plt.subplots(figsize=(10, 4))
    if amplitudes:
        ax.plot(range(len(amplitudes)), amplitudes, "o-", ms=3, color="crimson")
        ax.set_xlabel("Half-cycle index")
        ax.set_ylabel(r"Amplitude $|\rho - \rho^*|$")
    else:
        ax.text(0.5, 0.5, "No oscillations detected",
                transform=ax.transAxes, ha="center", va="center", fontsize=14)
    ax.set_title(f"2D {result['ic_name']}: oscillation envelope  ({n_cycles} cycles)")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)

def plot_mode_energy(result, path):
    """Radial power spectra at snapshot times."""
    fig, ax = plt.subplots(figsize=(10, 5))
    k_c = np.array(result["k_centers"])
    cmap = plt.cm.viridis
    n = len(result["spectra_times"])
    for i, (t, spec) in enumerate(zip(result["spectra_times"], result["spectra_data"])):
        c = cmap(i / max(n - 1, 1))
        ax.semilogy(k_c, np.array(spec) + 1e-30, color=c, lw=1.0,
                     label=f"t={t:.0f}")
    ax.set_xlabel("Radial wavenumber k")
    ax.set_ylabel("Power (azimuthal avg)")
    ax.set_title(f"2D {result['ic_name']}: radial power spectrum evolution")
    ax.legend(fontsize=8, ncol=2)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)

def plot_snapshots_grid(result, path):
    """Grid of 2D heatmaps at snapshot times."""
    snaps = result["snapshots"]
    steps = sorted(snaps.keys())
    n = len(steps)
    cols = min(4, n)
    rows = (n + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(4 * cols, 3.5 * rows))
    if rows == 1:
        axes = [axes] if cols == 1 else list(axes)
    else:
        axes = [ax for row in axes for ax in row]

    vmin = RHO_STAR - 10
    vmax = RHO_STAR + 45

    for i, step in enumerate(steps):
        ax = axes[i]
        im = ax.imshow(snaps[step].T, origin="lower", cmap="RdBu_r",
                       vmin=vmin, vmax=vmax, aspect="equal")
        ax.set_title(f"step {step}", fontsize=10)
        ax.set_xticks([]); ax.set_yticks([])

    # hide unused axes
    for j in range(i + 1, len(axes)):
        axes[j].set_visible(False)

    fig.suptitle(f"2D {result['ic_name']}: density snapshots", fontsize=13)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)

def save_individual_snapshots(result, snap_dir):
    """Save individual heatmap PNGs."""
    ic = result["ic_name"]
    for step, rho in result["snapshots"].items():
        fig, ax = plt.subplots(figsize=(5, 4.5))
        im = ax.imshow(rho.T, origin="lower", cmap="RdBu_r",
                       vmin=RHO_STAR - 10, vmax=RHO_STAR + 45, aspect="equal")
        plt.colorbar(im, ax=ax, shrink=0.8)
        ax.set_title(f"{ic} step={step}")
        fig.tight_layout()
        fig.savefig(snap_dir / f"{ic}_step{step:05d}.png", dpi=120)
        plt.close(fig)

def plot_phase_flag(result, regime, n_cycles, path):
    cmap = {"oscillatory": "#2196F3", "hybrid": "#FF9800", "parabolic-like": "#4CAF50"}
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_axis_off()
    ax.add_patch(plt.Rectangle((0.05, 0.1), 0.9, 0.8,
                                facecolor=cmap.get(regime, "gray"),
                                edgecolor="black", lw=2, alpha=0.85))
    ax.text(0.5, 0.6, regime.upper().replace("-", " "),
            ha="center", va="center", fontsize=22, fontweight="bold", color="white")
    ax.text(0.5, 0.35, f"2D {result['ic_name']}  |  {n_cycles} cycles",
            ha="center", va="center", fontsize=12, color="white")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)

def plot_mode_coupling_summary(all_analysis, path):
    """Compare top modes start vs end for each IC."""
    fig, axes = plt.subplots(1, len(all_analysis), figsize=(5 * len(all_analysis), 5))
    if len(all_analysis) == 1:
        axes = [axes]
    for ax, ana in zip(axes, all_analysis):
        # start modes
        start_labels = [f"({m['kx']},{m['ky']})" for m in ana["top_modes_start"][:6]]
        start_amps   = [m["amplitude"] for m in ana["top_modes_start"][:6]]
        end_labels   = [f"({m['kx']},{m['ky']})" for m in ana["top_modes_end"][:6]]
        end_amps     = [m["amplitude"] for m in ana["top_modes_end"][:6]]

        x = np.arange(6)
        w = 0.35
        ax.bar(x - w/2, start_amps, w, label="Initial", color="steelblue", edgecolor="black")
        ax.bar(x + w/2, end_amps, w, label="Final", color="coral", edgecolor="black")
        ax.set_xticks(x)
        combined = start_labels  # use start labels for x-axis
        ax.set_xticklabels(combined, fontsize=8, rotation=45)
        ax.set_ylabel("Amplitude")
        ax.set_title(f"{ana['ic_name']}", fontsize=11)
        ax.legend(fontsize=8)

    fig.suptitle("2D Mode Coupling: Top Modes (Initial vs Final)", fontsize=13)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)

def plot_anisotropy(all_results, path):
    """Anisotropy index vs time for each IC."""
    fig, ax = plt.subplots(figsize=(10, 4))
    for res in all_results:
        ax.plot(res["time_hist"], res["anisotropy_hist"], lw=0.8,
                label=res["ic_name"])
    ax.axhline(0.5, color="gray", ls="--", alpha=0.5, label="isotropic")
    ax.set_xlabel("Time")
    ax.set_ylabel("Anisotropy (x-var / total-var)")
    ax.set_title("2D Anisotropy Index vs Time")
    ax.legend(fontsize=9)
    ax.set_ylim(-0.05, 1.05)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


# =========================================================================
#  Main
# =========================================================================

def main():
    print("=" * 70)
    print("ED-Phys-23: 2D Oscillatory Cosmology")
    print("=" * 70)
    print(f"Grid: {NX}x{NY}, {N_STEPS} steps, sample every {SAMPLE}")
    print(f"Canonical: alpha={ALPHA}, gamma={GAMMA}, rho*={RHO_STAR}, rho0={RHO_0}")
    print(f"Oscillator: tau={TAU}, zeta={ZETA}")
    print(f"Pure oscillatory: D={D_FIXED}, H={H_FIXED}")
    print(f"CFL dt = {ETA * DX * DX / M0:.4f}")
    print("=" * 70)

    ic_funcs = [ic_radial_gaussian, ic_standing_wave, ic_two_mode]
    all_results  = []
    all_analysis = []

    for ic_func in ic_funcs:
        # get IC name
        _, _, ic_name = ic_func(4, 4)
        print(f"\n== IC: {ic_name} ==")

        t0 = timer_mod.time()
        result = run_2d_case(ic_func)
        elapsed = timer_mod.time() - t0
        print(f"   Simulation: {elapsed:.1f}s,  clips={result['total_clips']}")

        # oscillation analysis
        n_cycles, amplitudes, crossings = detect_oscillations(result["peak_hist"])
        regime = classify_regime(n_cycles)
        print(f"   Cycles: {n_cycles},  regime: {regime}")
        if amplitudes:
            print(f"   Amp envelope: {amplitudes[0]:.4f} -> {amplitudes[-1]:.4f}")

        # anisotropy
        aniso = result["anisotropy_hist"]
        print(f"   Anisotropy: start={aniso[0]:.4f}, end={aniso[-1]:.4f}")

        # radial symmetry (for radial IC only)
        if result["radial_sym_hist"]:
            devs = [r["radial_dev"] for r in result["radial_sym_hist"]]
            print(f"   Radial symmetry deviation: {devs[0]:.6f} -> {devs[-1]:.6f}")

        # horizon
        hor_life = int(np.sum(np.array(result["horizon_hist"]) > 0))
        print(f"   Horizon lifetime: {hor_life} samples")

        # top modes
        print(f"   Top modes (start):")
        for m in result["top_modes_start"][:4]:
            print(f"      (kx={m['kx']}, ky={m['ky']}): amp={m['amplitude']:.6f}")
        print(f"   Top modes (end):")
        for m in result["top_modes_end"][:4]:
            print(f"      (kx={m['kx']}, ky={m['ky']}): amp={m['amplitude']:.6f}")

        # check for new modes (modes in top-8 at end that weren't in top-8 at start)
        start_keys = {(m["kx"], m["ky"]) for m in result["top_modes_start"][:8]}
        end_keys   = {(m["kx"], m["ky"]) for m in result["top_modes_end"][:8]}
        new_modes  = end_keys - start_keys
        if new_modes:
            print(f"   NEW MODES appeared: {new_modes}")
        else:
            print(f"   No new modes in top-8")

        analysis = {
            "ic_name":          ic_name,
            "n_cycles":         n_cycles,
            "regime":           regime,
            "amplitudes":       amplitudes[:20],
            "horizon_lifetime": hor_life,
            "anisotropy_start": float(aniso[0]),
            "anisotropy_end":   float(aniso[-1]),
            "radial_sym":       result["radial_sym_hist"],
            "top_modes_start":  result["top_modes_start"][:8],
            "top_modes_end":    result["top_modes_end"][:8],
            "new_modes":        [list(m) for m in new_modes],
            "total_clips":      result["total_clips"],
            "final_std":        result["final_rho_std"],
        }

        all_results.append(result)
        all_analysis.append(analysis)

        # per-IC plots
        tag = ic_name
        plot_time_series(result, OUT / f"{tag}_time_series.png")
        plot_envelope(result, n_cycles, amplitudes, OUT / f"{tag}_oscillation_envelope.png")
        plot_mode_energy(result, OUT / f"{tag}_mode_energy.png")
        plot_snapshots_grid(result, OUT / f"{tag}_snapshots_grid.png")
        save_individual_snapshots(result, SNAP_DIR)
        plot_phase_flag(result, regime, n_cycles, OUT / f"{tag}_phase_flag.png")
        print(f"   Plots saved: {tag}_*.png")

    # -- Summary plots --
    plot_mode_coupling_summary(all_analysis, OUT / "mode_coupling_summary.png")
    plot_anisotropy(all_results, OUT / "anisotropy_evolution.png")
    print("\nSummary plots saved.")

    # -- Summary table --
    print("\n" + "=" * 90)
    print(f"{'IC':>20} | {'cycles':>6} | {'regime':>12} | {'hor_life':>8} | "
          f"{'aniso_s':>8} | {'aniso_e':>8} | {'new_modes':>10} | {'clips':>6}")
    print("-" * 90)
    for a in all_analysis:
        print(f"{a['ic_name']:>20} | {a['n_cycles']:>6} | {a['regime']:>12} | "
              f"{a['horizon_lifetime']:>8} | {a['anisotropy_start']:>8.4f} | "
              f"{a['anisotropy_end']:>8.4f} | {len(a['new_modes']):>10} | "
              f"{a['total_clips']:>6}")
    print("=" * 90)

    # -- JSON export --
    with open(OUT / "2d_osc_summary.json", "w") as f:
        json.dump(all_analysis, f, indent=2)
    print(f"\nJSON: {OUT / '2d_osc_summary.json'}")
    print("Done.")


if __name__ == "__main__":
    main()
