"""
edsim.phys.experiments_wave — Wave/telegraph-regime numerical experiments.

Three experiments:

1. **Uniform perturbation oscillation** — a spatially uniform density offset
   oscillates via the (rho, v) participation coupling.  This is the cleanest
   test of the telegraph-like dynamics.

2. **Sine-wave decay** — a single-mode cosine perturbation decays
   exponentially.  The participation coupling is checked for residual
   oscillatory contamination at higher amplitudes.

3. **Wave-packet evolution** — a localised oscillatory packet is evolved to
   test whether any group-velocity-like propagation occurs.  The expectation
   is diffusive spreading with no net translation.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

import numpy as np

from ..core.parameters import EDParameters
from ..core.constitutive import enforce_bounds
from ..experiments.runner import RunConfig, TimeSeries, run_simulation
from .wave_regime import WaveRegime, build_wave_regime


# ---------------------------------------------------------------
# Result containers
# ---------------------------------------------------------------

@dataclass
class UniformOscillationResult:
    """Output of the uniform-perturbation experiment.

    Attributes
    ----------
    regime : WaveRegime
    series : TimeSeries
    times : np.ndarray
    mean_rho : np.ndarray
        Domain-averaged rho at each snapshot (should oscillate).
    v_history : np.ndarray
        Participation variable at each snapshot.
    A0 : float
        Initial perturbation amplitude.
    """

    regime: WaveRegime
    series: TimeSeries
    times: np.ndarray
    mean_rho: np.ndarray
    v_history: np.ndarray
    A0: float


@dataclass
class SineWaveDecayResult:
    """Output of the sine-wave decay experiment.

    Attributes
    ----------
    regime : WaveRegime
    series : TimeSeries
    times : np.ndarray
    mode_amplitudes : np.ndarray
        Amplitude of the k-th mode at each snapshot.
    k : int
        Wavenumber index.
    v_history : np.ndarray
    """

    regime: WaveRegime
    series: TimeSeries
    times: np.ndarray
    mode_amplitudes: np.ndarray
    k: int
    v_history: np.ndarray


@dataclass
class WavePacketResult:
    """Output of the wave-packet experiment.

    Attributes
    ----------
    regime : WaveRegime
    series : TimeSeries
    times : np.ndarray
    centroids : np.ndarray
        Centre of mass of |rho - rho_star| along x at each snapshot.
    widths : np.ndarray
        RMS width of the packet along x at each snapshot.
    peak_amplitudes : np.ndarray
        Peak |rho - rho_star| at each snapshot.
    """

    regime: WaveRegime
    series: TimeSeries
    times: np.ndarray
    centroids: np.ndarray
    widths: np.ndarray
    peak_amplitudes: np.ndarray


# ---------------------------------------------------------------
# Experiment 1: uniform perturbation
# ---------------------------------------------------------------

def run_uniform_oscillation(
    regime: Optional[WaveRegime] = None,
    amplitude: float = 0.02,
) -> UniformOscillationResult:
    """Evolve a spatially uniform density offset and track oscillation.

    rho(x, 0) = rho_star + A  (constant field, no spatial gradients)

    The Laplacian is zero, so the only dynamics come from the penalty and
    participation coupling.  The linearised system predicts telegraph-like
    oscillation of <rho>(t) around rho_star.

    Parameters
    ----------
    regime : WaveRegime, optional
        If None, the default 2D wave regime is built.
    amplitude : float
        Initial uniform offset from rho_star (default 0.02).

    Returns
    -------
    UniformOscillationResult
    """
    if regime is None:
        regime = build_wave_regime(d=2)

    params = regime.parameters
    ic = np.full(params.N, params.rho_star + amplitude)
    ic = enforce_bounds(ic, params)

    config = RunConfig(
        params=params,
        ic_type="custom",
        ic_kwargs={"field": ic},
    )

    series = run_simulation(config)
    times = np.array(series.times)

    # Domain-average rho at each snapshot
    mean_rho = np.array([float(np.mean(f)) for f in series.fields])
    v_hist = np.array(series.v_history)

    return UniformOscillationResult(
        regime=regime,
        series=series,
        times=times,
        mean_rho=mean_rho,
        v_history=v_hist,
        A0=amplitude,
    )


# ---------------------------------------------------------------
# Experiment 2: sine-wave decay
# ---------------------------------------------------------------

def run_sine_wave_decay(
    regime: Optional[WaveRegime] = None,
    k: int = 1,
    amplitude: float = 0.02,
) -> SineWaveDecayResult:
    """Evolve a single cosine mode and track its amplitude decay.

    rho(x, 0) = rho_star + A cos(k pi x / L)

    In 2D this is a 1D cosine varying along x, uniform along y.

    Parameters
    ----------
    regime : WaveRegime, optional
    k : int
        Wavenumber index (default 1).
    amplitude : float
        Mode amplitude (default 0.02).

    Returns
    -------
    SineWaveDecayResult
    """
    if regime is None:
        regime = build_wave_regime(d=2)

    params = regime.parameters
    grid = params.make_grid()

    # Build cosine IC along axis 0
    coords = np.meshgrid(*grid, indexing="ij")
    rho = np.full(params.N, params.rho_star, dtype=float)
    rho += amplitude * np.cos(k * np.pi * coords[0] / params.L[0])
    rho = enforce_bounds(rho, params)

    config = RunConfig(
        params=params,
        ic_type="custom",
        ic_kwargs={"field": rho},
    )

    series = run_simulation(config)
    times = np.array(series.times)

    # Extract mode amplitude at each snapshot using projection
    basis = np.cos(k * np.pi * coords[0] / params.L[0])
    norm2 = float(np.sum(basis ** 2))

    mode_amps = np.array([
        float(np.sum((f - params.rho_star) * basis)) / (norm2 + 1e-30)
        for f in series.fields
    ])

    return SineWaveDecayResult(
        regime=regime,
        series=series,
        times=times,
        mode_amplitudes=mode_amps,
        k=k,
        v_history=np.array(series.v_history),
    )


# ---------------------------------------------------------------
# Experiment 3: wave packet
# ---------------------------------------------------------------

def run_wave_packet(
    regime: Optional[WaveRegime] = None,
    k0: int = 4,
    sigma: float = 0.1,
    amplitude: float = 0.02,
) -> WavePacketResult:
    """Evolve a localised oscillatory wave packet.

    rho(x, 0) = rho_star + A * exp(-|x - x_c|^2 / (2 sigma^2))
                              * cos(k0 pi x / L)

    In 2D the packet varies along x and is uniform along y.

    We track the centroid, width, and peak amplitude to detect any
    propagation (centroid shift) or dispersive spreading.

    Parameters
    ----------
    regime : WaveRegime, optional
    k0 : int
        Carrier wavenumber (default 4).
    sigma : float
        Envelope width (default 0.1).
    amplitude : float
        Peak amplitude (default 0.02).

    Returns
    -------
    WavePacketResult
    """
    if regime is None:
        regime = build_wave_regime(d=2)

    params = regime.parameters
    grid = params.make_grid()
    coords = np.meshgrid(*grid, indexing="ij")

    x = coords[0]
    xc = params.L[0] / 2.0
    envelope = np.exp(-(x - xc) ** 2 / (2.0 * sigma ** 2))
    carrier = np.cos(k0 * np.pi * x / params.L[0])
    rho = np.full(params.N, params.rho_star, dtype=float) + amplitude * envelope * carrier
    rho = enforce_bounds(rho, params)

    config = RunConfig(
        params=params,
        ic_type="custom",
        ic_kwargs={"field": rho},
    )

    series = run_simulation(config)
    times = np.array(series.times)

    # Track centroid and width of |delta rho| along x
    x_1d = grid[0]
    dx = params.dx[0]

    centroids = []
    widths = []
    peaks = []

    for field in series.fields:
        # Average over all axes except the first (x)
        axes_to_avg = tuple(range(1, params.d))
        if axes_to_avg:
            prof = np.mean(np.abs(field - params.rho_star), axis=axes_to_avg)
        else:
            prof = np.abs(field - params.rho_star)

        total = float(np.sum(prof) * dx)
        if total < 1e-30:
            centroids.append(xc)
            widths.append(0.0)
        else:
            centroid = float(np.sum(x_1d * prof) * dx) / total
            width = np.sqrt(
                float(np.sum((x_1d - centroid) ** 2 * prof) * dx) / total
            )
            centroids.append(centroid)
            widths.append(width)

        peaks.append(float(np.max(np.abs(field - params.rho_star))))

    return WavePacketResult(
        regime=regime,
        series=series,
        times=times,
        centroids=np.array(centroids),
        widths=np.array(widths),
        peak_amplitudes=np.array(peaks),
    )
