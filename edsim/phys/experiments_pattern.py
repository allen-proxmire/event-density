"""
edsim.phys.experiments_pattern — Pattern-formation numerical experiments.

Three experiments:

1. **Noise instability test** — small random noise is evolved.  If any mode
   grows, ED has an instability.  The prediction: NO mode grows (all decay).
   Measures the transient complexity peak.

2. **Filament stability** — a thin elongated structure (1D ridge in 2D) is
   evolved.  Tests whether it breaks up (Plateau-Rayleigh-like instability)
   or decays smoothly.

3. **Spot evolution** — a localised bump is evolved.  Tests whether it
   develops ring structure, filaments, or simply diffuses and decays.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

import numpy as np

from ..core.parameters import EDParameters
from ..core.constitutive import enforce_bounds
from ..experiments.runner import RunConfig, TimeSeries, run_simulation
from .pattern_regime import PatternRegime, build_pattern_regime


# ---------------------------------------------------------------
# Result containers
# ---------------------------------------------------------------

@dataclass
class NoiseInstabilityResult:
    """Output of the noise-instability test.

    Attributes
    ----------
    regime : PatternRegime
    series : TimeSeries
    times : np.ndarray
    complexity : np.ndarray
        ED-complexity C(t) at each snapshot.
    spectral_entropy : np.ndarray
        Spectral entropy H(t).
    max_mode_amplitudes : np.ndarray
        Amplitude of the largest Fourier mode at each snapshot.
    any_mode_grew : bool
        Whether any mode's amplitude exceeded its initial value.
    transient_amplification : float
        max(C(t)) / C(0) — how much complexity grows transiently.
    peak_complexity_time : float
        Time at which C(t) is maximised.
    noise_amplitude : float
    """

    regime: PatternRegime
    series: TimeSeries
    times: np.ndarray
    complexity: np.ndarray
    spectral_entropy: np.ndarray
    max_mode_amplitudes: np.ndarray
    any_mode_grew: bool
    transient_amplification: float
    peak_complexity_time: float
    noise_amplitude: float


@dataclass
class FilamentStabilityResult:
    """Output of the filament-stability test.

    Attributes
    ----------
    regime : PatternRegime
    series : TimeSeries
    times : np.ndarray
    peak_amplitude : np.ndarray
    cross_section_variance : np.ndarray
        Variance of the filament cross-section (measures breakup).
    filament_intact : bool
        Whether the filament decayed smoothly (no breakup).
    filament_width : float
    """

    regime: PatternRegime
    series: TimeSeries
    times: np.ndarray
    peak_amplitude: np.ndarray
    cross_section_variance: np.ndarray
    filament_intact: bool
    filament_width: float


@dataclass
class SpotEvolutionResult:
    """Output of the spot-evolution test.

    Attributes
    ----------
    regime : PatternRegime
    series : TimeSeries
    times : np.ndarray
    peak_amplitude : np.ndarray
    radial_profiles : list[np.ndarray]
        Radially-averaged profile at each snapshot.
    r_coords : np.ndarray
    developed_ring : bool
        Whether a ring structure appeared.
    """

    regime: PatternRegime
    series: TimeSeries
    times: np.ndarray
    peak_amplitude: np.ndarray
    radial_profiles: list
    r_coords: np.ndarray
    developed_ring: bool


# ---------------------------------------------------------------
# Experiment 1: noise instability test
# ---------------------------------------------------------------

def run_noise_instability(
    regime: Optional[PatternRegime] = None,
    noise_amplitude: float = 0.01,
) -> NoiseInstabilityResult:
    """Evolve small random noise and test for instability.

    rho(x, 0) = rho_star + noise

    If any Fourier mode amplitude exceeds its initial value at any
    later time, the system has an instability.

    Parameters
    ----------
    regime : PatternRegime, optional
    noise_amplitude : float

    Returns
    -------
    NoiseInstabilityResult
    """
    if regime is None:
        regime = build_pattern_regime(d=2)

    params = regime.parameters
    rng = np.random.default_rng(params.seed)
    ic = params.rho_star + noise_amplitude * (2.0 * rng.random(params.N) - 1.0)
    ic = enforce_bounds(ic, params)

    config = RunConfig(
        params=params,
        ic_type="custom",
        ic_kwargs={"field": ic},
    )

    series = run_simulation(config)
    times = np.array(series.times)
    complexity = np.array(series.complexity)
    entropy = np.array(series.spectral_entropy)

    # Track the maximum Fourier mode amplitude at each snapshot
    from scipy.fft import dctn
    max_amps = []
    for field in series.fields:
        coeffs = dctn(field - params.rho_star, type=2, norm="ortho")
        coeffs_flat = np.abs(coeffs.ravel())
        coeffs_flat[0] = 0.0  # exclude DC
        max_amps.append(float(np.max(coeffs_flat)))

    max_amps = np.array(max_amps)

    # Did any mode grow?
    any_grew = bool(np.any(max_amps[1:] > max_amps[0] * 1.01))

    # Transient amplification
    C_max = float(np.max(complexity))
    C_0 = complexity[0] if complexity[0] > 1e-30 else 1e-30
    amp_ratio = C_max / C_0
    peak_t = times[np.argmax(complexity)]

    return NoiseInstabilityResult(
        regime=regime,
        series=series,
        times=times,
        complexity=complexity,
        spectral_entropy=entropy,
        max_mode_amplitudes=max_amps,
        any_mode_grew=any_grew,
        transient_amplification=amp_ratio,
        peak_complexity_time=peak_t,
        noise_amplitude=noise_amplitude,
    )


# ---------------------------------------------------------------
# Experiment 2: filament stability
# ---------------------------------------------------------------

def run_filament_instability(
    regime: Optional[PatternRegime] = None,
    width: float = 0.05,
    amplitude: float = 0.08,
) -> FilamentStabilityResult:
    """Evolve a thin ridge (1D filament in 2D) and test for breakup.

    rho(x, y, 0) = rho_star + A * exp(-y^2 / (2 w^2))

    A stable filament decays smoothly in amplitude while spreading.
    An unstable filament develops along-axis modulations (breakup).

    Parameters
    ----------
    regime : PatternRegime, optional
    width : float
        Filament half-width (default 0.05).
    amplitude : float
        Peak amplitude (default 0.08).

    Returns
    -------
    FilamentStabilityResult
    """
    if regime is None:
        regime = build_pattern_regime(d=2)

    params = regime.parameters
    grid = params.make_grid()
    coords = np.meshgrid(*grid, indexing="ij")

    # Ridge along x-axis at y = L/2
    y_centre = params.L[1] / 2.0 if params.d >= 2 else params.L[0] / 2.0
    if params.d >= 2:
        y_dev = coords[1] - y_centre
    else:
        y_dev = coords[0] - y_centre

    ic = params.rho_star + amplitude * np.exp(-y_dev ** 2 / (2.0 * width ** 2))
    ic = enforce_bounds(ic, params)

    config = RunConfig(
        params=params,
        ic_type="custom",
        ic_kwargs={"field": ic},
    )

    series = run_simulation(config)
    times = np.array(series.times)

    # Track peak and cross-section variance
    peaks = []
    cs_vars = []
    for field in series.fields:
        delta = field - params.rho_star
        peaks.append(float(np.max(np.abs(delta))))

        if params.d >= 2:
            # Cross-section: profile along y at x = L/2
            mid_x = params.N[0] // 2
            cross = delta[mid_x, :]
        else:
            cross = delta

        # Variance of the cross-section along y — if the filament breaks
        # up, the variance will increase then decrease non-monotonically.
        # For a smooth decay, the cross-section shape is preserved.
        if np.max(np.abs(cross)) > 1e-14:
            normalised = cross / (np.max(np.abs(cross)) + 1e-30)
        else:
            normalised = cross
        cs_vars.append(float(np.var(normalised)))

    peaks = np.array(peaks)
    cs_vars = np.array(cs_vars)

    # Filament is "intact" if the cross-section variance is monotonically
    # non-increasing (the shape doesn't develop new features).
    intact = bool(np.all(np.diff(cs_vars) <= cs_vars[0] * 0.1 + 1e-10))

    return FilamentStabilityResult(
        regime=regime,
        series=series,
        times=times,
        peak_amplitude=peaks,
        cross_section_variance=cs_vars,
        filament_intact=intact,
        filament_width=width,
    )


# ---------------------------------------------------------------
# Experiment 3: spot evolution
# ---------------------------------------------------------------

def run_spot_evolution(
    regime: Optional[PatternRegime] = None,
    sigma: float = 0.06,
    amplitude: float = 0.08,
) -> SpotEvolutionResult:
    """Evolve a localised Gaussian bump and track radial structure.

    Tests whether the bump develops ring structure (indicating
    morphological instability) or simply diffuses and decays.

    Parameters
    ----------
    regime : PatternRegime, optional
    sigma : float
    amplitude : float

    Returns
    -------
    SpotEvolutionResult
    """
    if regime is None:
        regime = build_pattern_regime(d=2)

    params = regime.parameters
    grid = params.make_grid()
    coords = np.meshgrid(*grid, indexing="ij")

    r2 = np.zeros(params.N)
    centres = [params.L[ax] / 2.0 for ax in range(params.d)]
    for ax in range(params.d):
        r2 += (coords[ax] - centres[ax]) ** 2

    ic = params.rho_star + amplitude * np.exp(-r2 / (2.0 * sigma ** 2))
    ic = enforce_bounds(ic, params)

    config = RunConfig(
        params=params,
        ic_type="custom",
        ic_kwargs={"field": ic},
    )

    series = run_simulation(config)
    times = np.array(series.times)

    # Compute radial profiles
    r_field = np.sqrt(r2)
    r_max = min(centres) * 0.9
    n_bins = 30
    r_edges = np.linspace(0, r_max, n_bins + 1)
    r_centres = 0.5 * (r_edges[:-1] + r_edges[1:])

    peaks = []
    radial_profs = []
    for field in series.fields:
        delta = field - params.rho_star
        peaks.append(float(np.max(np.abs(delta))))

        prof = np.zeros(n_bins)
        for b in range(n_bins):
            mask = (r_field >= r_edges[b]) & (r_field < r_edges[b + 1])
            if np.any(mask):
                prof[b] = float(np.mean(delta[mask]))
        radial_profs.append(prof)

    peaks = np.array(peaks)

    # Detect ring formation: a ring appears when the radial profile
    # develops a local maximum at r > 0 (not at the centre).
    developed_ring = False
    for prof in radial_profs[1:]:
        if len(prof) > 3:
            interior = prof[1:-1]
            if len(interior) > 1:
                max_idx = np.argmax(interior)
                if max_idx > 0 and interior[max_idx] > prof[0] * 1.05:
                    developed_ring = True
                    break

    return SpotEvolutionResult(
        regime=regime,
        series=series,
        times=times,
        peak_amplitude=peaks,
        radial_profiles=radial_profs,
        r_coords=r_centres,
        developed_ring=developed_ring,
    )
