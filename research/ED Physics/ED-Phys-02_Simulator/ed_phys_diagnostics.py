"""
ED-Phys-02: Diagnostics and Observable Extraction
====================================================
Canonical source: ED-Phys-01 §9

Post-run analysis of simulation results: time series extraction,
phase identification, and summary statistics.
"""

import numpy as np
from ed_phys_engine import SimulationResult, DiagnosticRecord


def extract_time_series(result: SimulationResult) -> dict[str, np.ndarray]:
    """Extract all diagnostic observables as numpy arrays.

    Returns a dict with keys matching ED-Phys-01 §9:
      steps, rho_total, rho_mean, rho_max, rho_min,
      grad_mean, grad_max, grad_energy, thinning_rate, n_basins,
      scale_factor_proxy
    """
    h = result.history
    if not h:
        return {}

    data = {
        "steps": np.array([r.step for r in h]),
        "rho_total": np.array([r.rho_total for r in h]),
        "rho_mean": np.array([r.rho_mean for r in h]),
        "rho_max": np.array([r.rho_max for r in h]),
        "rho_min": np.array([r.rho_min for r in h]),
        "grad_mean": np.array([r.grad_mean for r in h]),
        "grad_max": np.array([r.grad_max for r in h]),
        "grad_energy": np.array([r.grad_energy for r in h]),
        "thinning_rate": np.array([r.thinning_rate for r in h]),
        "n_basins": np.array([r.n_basins for r in h]),
    }

    # Scale factor proxy: a(t) = 1 / G(t)  (ED-Phys-01 §9)
    # Guard against division by zero
    grad_mean = data["grad_mean"]
    with np.errstate(divide='ignore', invalid='ignore'):
        scale_factor = np.where(grad_mean > 0, 1.0 / grad_mean, np.inf)
    data["scale_factor_proxy"] = scale_factor

    return data


def identify_phases(result: SimulationResult) -> list[dict]:
    """Attempt to identify cosmological phases from diagnostics.

    Returns a list of phase dicts with 'name', 'start_step', 'end_step',
    and 'description'.

    Phase identification (ED-Phys-01 §10):
    1. Inflation: grad_mean is rapidly decreasing (exponential decay)
    2. Structure Formation: n_basins is increasing
    3. Thinning: rho_mean is decreasing, grad_mean is small
    4. Heat Death: rho_mean and grad_mean are both approximately constant
    """
    ts = extract_time_series(result)
    if not ts:
        return []

    steps = ts["steps"]
    grad_mean = ts["grad_mean"]
    rho_mean = ts["rho_mean"]
    n_basins = ts["n_basins"]
    n = len(steps)

    if n < 4:
        return [{"name": "insufficient_data", "start_step": 0,
                 "end_step": int(steps[-1]),
                 "description": "Too few records to identify phases"}]

    phases_raw = []

    # Compute cumulative rates over sliding windows for robust detection.
    # Single-interval changes are often too small for threshold detection;
    # we compare each record to a baseline using cumulative trends.

    # Reference values at t=0
    G0 = grad_mean[0] if grad_mean[0] > 0 else 1e-30
    rho0 = rho_mean[0] if rho_mean[0] > 0 else 1e-30
    basins0 = n_basins[0]

    for i in range(n - 1):
        s0, s1 = int(steps[i]), int(steps[i + 1])

        # Cumulative gradient decay from initial value
        grad_frac_remaining = grad_mean[i] / G0 if G0 > 0 else 1.0
        # Local gradient trend (compare to ~5 intervals ago if possible)
        lookback = max(0, i - 5)
        local_grad_declining = (
            grad_mean[i] < 0.98 * grad_mean[lookback]
        ) if grad_mean[lookback] > 0 else False

        basins_growing = n_basins[i + 1] > n_basins[i]
        basins_declining = n_basins[i] < basins0 * 0.9
        rho_declining = rho_mean[i] < rho0 * 0.9999

        near_static = (
            abs(rho_mean[i + 1] - rho_mean[i]) < 1e-6 * max(rho_mean[i], 1e-30)
            and abs(grad_mean[i + 1] - grad_mean[i]) < 1e-6 * max(grad_mean[i], 1e-30)
        )

        # Phase classification with cumulative awareness
        if grad_frac_remaining > 0.5 and local_grad_declining:
            # Still in the steep part of gradient decay
            name = "inflation"
            desc = "Gradient smoothing (exponential decay of grad_rho)"
        elif basins_growing:
            name = "structure_formation"
            desc = "Basin count increasing (concave relational instability)"
        elif basins_declining and local_grad_declining:
            # Gradients still declining AND basins merging = residual gradient era
            name = "residual_gradient"
            desc = "Residual gradients persisting; basins merging"
        elif rho_declining and not local_grad_declining:
            name = "thinning"
            desc = "Global density decreasing (cosmological expansion)"
        elif near_static:
            name = "heat_death"
            desc = "Near-static equilibrium (minimal evolution)"
        elif rho_declining and local_grad_declining:
            name = "thinning"
            desc = "Global density decreasing with gradient decay"
        else:
            name = "transition"
            desc = "Transitional regime"

        phases_raw.append({
            "name": name,
            "start_step": s0,
            "end_step": s1,
            "description": desc,
        })

    # Merge consecutive intervals with the same phase name
    if not phases_raw:
        return []

    phases = [phases_raw[0].copy()]
    for p in phases_raw[1:]:
        if p["name"] == phases[-1]["name"]:
            phases[-1]["end_step"] = p["end_step"]
        else:
            phases.append(p.copy())

    return phases


def summary(result: SimulationResult) -> str:
    """Generate a human-readable summary of the simulation run."""
    p = result.params
    h = result.history

    lines = [
        "=" * 60,
        "  ED-Phys Simulation Summary",
        "=" * 60,
        f"  Dimensions:     {p.dimensions}D  ({p.N}" +
        (f"x{p.N})" if p.dimensions == 2 else ")"),
        f"  Steps:          {result.final_step} / {p.n_steps}" +
        (" (converged)" if result.converged else ""),
        f"  Timestep eta:   {p.eta:.6e}",
        f"  alpha:          {p.alpha}",
        f"  gamma_exp:      {p.gamma_exp}",
        f"  M_0:            {p.M_0}",
        f"  rho_max:        {p.rho_max}",
        f"  n_mob:          {p.n_mob}",
        f"  Boundary:       {p.boundary}",
        "-" * 60,
    ]

    if h:
        first, last = h[0], h[-1]
        lines += [
            f"  Initial: rho_mean={first.rho_mean:.4f}, G={first.grad_mean:.6f}, "
            f"basins={first.n_basins}",
            f"  Final:   rho_mean={last.rho_mean:.4f}, G={last.grad_mean:.6f}, "
            f"basins={last.n_basins}",
            f"  rho range: [{last.rho_min:.4f}, {last.rho_max:.4f}]",
            f"  Total rho change: {last.rho_total - first.rho_total:.4f}",
        ]
    else:
        lines.append("  No diagnostic records.")

    lines.append("=" * 60)
    return "\n".join(lines)
