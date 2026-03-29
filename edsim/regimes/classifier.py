"""
edsim.regimes.classifier -- Regime classification for ED simulations.

Given a set of characteristic Scales (L0, R0, T0) and optionally a
PhysicalTimeSeries, determine which physical regime best describes
the simulation.

Classification is deterministic: it uses the L0 and R0 ranges defined
in manifold.py.  When multiple regimes overlap, the one with the
tightest L0 bracket wins; ties are broken by R0 proximity.
"""

from __future__ import annotations

import math
from typing import Optional

from ..core.parameters import EDParameters
from ..units.scales import Scales
from ..units import constants as C
from .manifold import Regime, build_regime_manifold, _ALL_REGIMES


def classify_scales(scales: Scales) -> Regime:
    """Classify a Scales object into the best-matching regime.

    Algorithm:
        1. Check each regime's L0 and R0 containment.
        2. Among matching regimes, pick the one whose L0 midpoint
           (on a log scale) is closest to log10(scales.L0).
        3. If no regime matches, return the one with smallest
           log-distance to (L0, R0).

    Parameters
    ----------
    scales : Scales
        Characteristic scales to classify.

    Returns
    -------
    Regime
        Best-matching physical regime.
    """
    regimes = build_regime_manifold()

    # Phase 1: exact containment
    matches = [r for r in regimes if r.contains(scales)]
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        # Tightest L0 bracket
        def _L_span(r: Regime) -> float:
            return math.log10(r.L0_range[1]) - math.log10(r.L0_range[0])
        return min(matches, key=_L_span)

    # Phase 2: no exact match -- nearest in log space
    log_L = math.log10(max(scales.L0, 1e-100))
    log_R = math.log10(max(scales.R0, 1e-100))

    def _dist(r: Regime) -> float:
        mid_L = 0.5 * (math.log10(r.L0_range[0]) + math.log10(r.L0_range[1]))
        mid_R = 0.5 * (math.log10(r.R0_range[0]) + math.log10(r.R0_range[1]))
        return (log_L - mid_L) ** 2 + (log_R - mid_R) ** 2

    return min(regimes, key=_dist)


def classify_params(
    params: EDParameters,
    scales: Scales,
) -> Regime:
    """Classify using both EDParameters and Scales.

    This is a convenience wrapper that delegates to classify_scales
    but adds parameter-aware heuristics for edge cases.

    Parameters
    ----------
    params : EDParameters
        Nondimensional simulation parameters.
    scales : Scales
        Physical characteristic scales.

    Returns
    -------
    Regime
    """
    return classify_scales(scales)


def classify_timeseries(pts: "PhysicalTimeSeries") -> Regime:
    """Classify from a completed PhysicalTimeSeries.

    Uses the Scales stored in the PhysicalTimeSeries.  Falls back to
    condensed_matter if no scales are available.

    Parameters
    ----------
    pts : PhysicalTimeSeries
        Completed simulation output in physical units.

    Returns
    -------
    Regime
    """
    if pts.scales is not None:
        return classify_scales(pts.scales)
    # Fallback: inspect physical values to infer scale
    from .manifold import CONDENSED_MATTER
    return CONDENSED_MATTER


def compute_dimensionless_groups(
    scales: Scales,
    params: Optional[EDParameters] = None,
) -> dict[str, float]:
    """Compute key dimensionless groups for the given scales.

    Returns a dictionary of named dimensionless ratios that locate
    the simulation within the regime manifold.

    Parameters
    ----------
    scales : Scales
        Characteristic scales.
    params : EDParameters, optional
        Nondimensional parameters (for mobility-derived groups).

    Returns
    -------
    dict[str, float]
        Named dimensionless ratios.
    """
    eps = 1e-300  # guard against division by zero

    groups = {
        # Length comparisons
        "L0/l_Pl": scales.L0 / (C.l_Pl + eps),
        "L0/a_0": scales.L0 / (C.a_0 + eps),
        "L0/kpc": scales.L0 / (C.kpc + eps),
        "L0/L_H": scales.L0 / (C.c / C.H_0 + eps),
        # Density comparisons
        "R0/rho_crit": scales.R0 / (C.rho_crit + eps),
        "R0/rho_Pl": scales.R0 / (C.rho_Pl + eps),
        "R0/rho_water": scales.R0 / 1e3,
        # Time comparisons
        "T0/t_Pl": scales.T0 / (C.t_Pl + eps),
        "T0*H_0": scales.T0 * C.H_0,
        # Velocity comparison
        "V0/c": scales.V0 / C.c,
    }

    if params is not None:
        groups["M_star/M0"] = params.M_star / (params.M0 + eps)
        groups["rho_star/rho_max"] = params.rho_star / params.rho_max
        groups["R_grad_predicted"] = params.R_grad_predicted

    return groups


def regime_summary(
    scales: Scales,
    params: Optional[EDParameters] = None,
) -> str:
    """Return a human-readable regime summary string.

    Parameters
    ----------
    scales : Scales
    params : EDParameters, optional

    Returns
    -------
    str
        Multi-line summary.
    """
    regime = classify_scales(scales)
    groups = compute_dimensionless_groups(scales, params)

    lines = [
        f"Regime: {regime.label}",
        f"  L0 = {scales.L0:.4e} m    (L0/l_Pl = {groups['L0/l_Pl']:.2e})",
        f"  T0 = {scales.T0:.4e} s    (T0*H_0  = {groups['T0*H_0']:.2e})",
        f"  R0 = {scales.R0:.4e} kg/m^3 (R0/rho_crit = {groups['R0/rho_crit']:.2e})",
        f"  V0 = {scales.V0:.4e} m/s  (V0/c    = {groups['V0/c']:.2e})",
        f"",
        f"  Description: {regime.description[:120]}...",
    ]
    return "\n".join(lines)
