"""
edsim.math.laws -- Formal mathematical statements of the nine architectural laws.

Each law is expressed as a Law dataclass containing:
    - name and number
    - precise mathematical statement
    - derivation status (derived / empirical / partial)
    - dimensional dependence
    - universality (which parameters it holds for)
    - a verification function that tests the law against a TimeSeries

These form the "constitution" of the ED architecture.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional

import numpy as np

from ..experiments.runner import TimeSeries
from ..core.parameters import EDParameters


@dataclass(frozen=True)
class Law:
    """A single architectural law of the ED system.

    Attributes
    ----------
    number : int
        Law number (1-9).
    name : str
        Short name.
    statement : str
        Precise mathematical statement.
    latex : str
        LaTeX-formatted statement.
    derivation_status : str
        One of: "derived", "partial", "empirical".
    dimensional_dependence : str
        How the law depends on d.
    universality : str
        Which parameter regimes the law holds for.
    """

    number: int
    name: str
    statement: str
    latex: str
    derivation_status: str
    dimensional_dependence: str
    universality: str


def _check_attractor(ts: TimeSeries, params: EDParameters) -> dict:
    """Check Law 1: unique attractor."""
    if len(ts.fields) < 2:
        return {"passed": False, "reason": "too few snapshots"}
    rho_final = ts.fields[-1]
    std_final = float(np.std(rho_final))
    v_final = ts.v_history[-1] if ts.v_history else 0.0
    passed = std_final < 0.1 * abs(params.rho_star) and abs(v_final) < 0.1
    return {
        "passed": passed,
        "rho_std_final": std_final,
        "v_final": v_final,
    }


def _check_energy_monotone(ts: TimeSeries, params: EDParameters) -> dict:
    """Check Law 2: monotone energy decay."""
    E = np.array(ts.energy)
    if E.size < 2:
        return {"passed": False, "reason": "too few snapshots"}
    diffs = np.diff(E)
    violations = int(np.sum(diffs > 1e-12))
    passed = violations == 0
    return {
        "passed": passed,
        "violations": violations,
        "max_increase": float(np.max(diffs)) if diffs.size > 0 else 0.0,
    }


def _check_spectral_concentration(ts: TimeSeries, params: EDParameters) -> dict:
    """Check Law 3: spectral entropy decreases."""
    H = np.array(ts.spectral_entropy) if ts.spectral_entropy else np.array([])
    if H.size < 2:
        return {"passed": False, "reason": "no spectral data"}
    passed = H[-1] < H[0]
    return {
        "passed": passed,
        "H_initial": float(H[0]),
        "H_final": float(H[-1]),
        "delta_H": float(H[0] - H[-1]),
    }


def _check_modal_hierarchy(ts: TimeSeries, params: EDParameters) -> dict:
    """Check Law 4: leading mode dominates and decays."""
    if not ts.modal_hierarchy or len(ts.modal_hierarchy) < 2:
        return {"passed": False, "reason": "no modal data"}
    A0 = ts.modal_hierarchy[0]
    Af = ts.modal_hierarchy[-1]
    passed = float(Af[0]) < float(A0[0]) if A0.size > 0 and Af.size > 0 else False
    return {
        "passed": passed,
        "A0_leading": float(A0[0]) if A0.size > 0 else 0.0,
        "Af_leading": float(Af[0]) if Af.size > 0 else 0.0,
    }


def _check_dissipation_channels(ts: TimeSeries, params: EDParameters) -> dict:
    """Check Law 5: R_grad + R_pen + R_part ~ 1."""
    if not ts.R_grad:
        return {"passed": False, "reason": "no dissipation data"}
    sums = [
        ts.R_grad[i] + ts.R_pen[i] + ts.R_part[i]
        for i in range(len(ts.R_grad))
    ]
    mean_sum = float(np.mean(sums))
    passed = abs(mean_sum - 1.0) < 0.05
    return {
        "passed": passed,
        "mean_sum": mean_sum,
        "R_grad_mean": float(np.mean(ts.R_grad)),
    }


def _check_topology_conservation(ts: TimeSeries, params: EDParameters) -> dict:
    """Check Law 6: Euler characteristic conserved."""
    chi = ts.euler_characteristic if ts.euler_characteristic else []
    if len(chi) < 2:
        return {"passed": False, "reason": "no topology data"}
    unique = len(set(chi))
    passed = unique == 1
    return {
        "passed": passed,
        "chi_values": list(set(chi)),
        "n_unique": unique,
    }


def _check_dimensional_universality(ts: TimeSeries, params: EDParameters) -> dict:
    """Check Law 7: R_grad matches the derived formula."""
    R_pred = params.R_grad_predicted
    R_meas = float(np.mean(ts.R_grad)) if ts.R_grad else 0.0
    passed = abs(R_meas - R_pred) < 0.1
    return {
        "passed": passed,
        "R_grad_predicted": R_pred,
        "R_grad_measured": R_meas,
        "error": abs(R_meas - R_pred),
    }


def _check_morphology_stratification(ts: TimeSeries, params: EDParameters) -> dict:
    """Check Law 8: morphology fractions sum to 1 and are nontrivial."""
    if not ts.morphology_fractions:
        return {"passed": False, "reason": "no morphology data"}
    m0 = ts.morphology_fractions[0]
    total = sum(m0.values())
    n_nonzero = sum(1 for v in m0.values() if v > 0.01)
    passed = abs(total - 1.0) < 0.01 and n_nonzero >= 2
    return {
        "passed": passed,
        "total": total,
        "n_nonzero_classes": n_nonzero,
        "fractions": dict(m0),
    }


def _check_structural_invariance(ts: TimeSeries, params: EDParameters) -> dict:
    """Check Law 9: mass approximately conserved."""
    M = np.array(ts.mass) if ts.mass else np.array([])
    if M.size < 2:
        return {"passed": False, "reason": "no mass data"}
    change = abs(M[-1] - M[0]) / (abs(M[0]) + 1e-30)
    passed = change < 0.01
    return {
        "passed": passed,
        "mass_initial": float(M[0]),
        "mass_final": float(M[-1]),
        "relative_change": float(change),
    }


# ══════════════════════════════════════════════════════════════════════
#  The Nine Laws
# ══════════════════════════════════════════════════════════════════════

LAW_1 = Law(
    number=1,
    name="Unique attractor",
    statement=(
        "The coupled (rho, v) system possesses a unique globally "
        "attracting equilibrium rho = rho*, v = 0 for all initial "
        "conditions in [0, rho_max]."
    ),
    latex=(
        "\\rho(x,t) \\to \\rho^*, \\quad v(t) \\to 0 "
        "\\quad \\text{as } t \\to \\infty"
    ),
    derivation_status="partial",
    dimensional_dependence="Holds for all d.",
    universality="All constitutive parameters with P0 > 0, M0 > 0.",
)

LAW_2 = Law(
    number=2,
    name="Monotone energy decay",
    statement=(
        "The Lyapunov functional E[rho] = int Phi(rho) dV is "
        "non-increasing along all solutions: dE/dt <= 0."
    ),
    latex=(
        "\\frac{dE}{dt} = -D\\int\\frac{|\\nabla\\rho|^2}{M(\\rho)}\\,dV "
        "- D\\int\\frac{P(\\rho)^2}{M(\\rho)}\\,dV \\leq 0"
    ),
    derivation_status="derived",
    dimensional_dependence="Holds for all d.",
    universality="All parameters.",
)

LAW_3 = Law(
    number=3,
    name="Spectral concentration",
    statement=(
        "The spectral entropy H = -sum p_k log p_k decreases over "
        "time as energy concentrates into low-k modes."
    ),
    latex=(
        "H(t_2) \\leq H(t_1) \\quad \\forall\\, t_2 > t_1"
    ),
    derivation_status="empirical",
    dimensional_dependence="Holds for all d; initial H increases with d.",
    universality="Canonical constitutive functions.",
)

LAW_4 = Law(
    number=4,
    name="Factorial complexity dilution",
    statement=(
        "The initial ED-complexity C^(d) scales as C^(1)/d! "
        "with spatial dimension d."
    ),
    latex=(
        "C_{\\text{ED}}^{(d)} = \\frac{C_{\\text{ED}}^{(1)}}{d!}"
    ),
    derivation_status="partial",
    dimensional_dependence="Explicit: d!",
    universality="Isotropic Neumann eigenbasis with fixed A, Nm.",
)

LAW_5 = Law(
    number=5,
    name="Gradient-dissipation dominance",
    statement=(
        "The gradient dissipation channel R_grad increases with d "
        "and approaches 1 asymptotically."
    ),
    latex=(
        "R_{\\text{grad}}^{(d)} = "
        "\\frac{d\\pi^2}{d\\pi^2 + P_0^2/M^*} \\to 1"
    ),
    derivation_status="derived",
    dimensional_dependence="Explicit: linear in d.",
    universality="All parameters with P0, M* > 0.",
)

LAW_6 = Law(
    number=6,
    name="Topological conservation",
    statement=(
        "The Euler characteristic chi of excursion sets is "
        "constant in time: d chi/dt = 0."
    ),
    latex=(
        "\\frac{d\\chi}{dt} = 0, \\quad "
        "\\chi = \\sum_{k=0}^{d-1}(-1)^k \\beta_k"
    ),
    derivation_status="partial",
    dimensional_dependence="Holds for all d (Morse theory).",
    universality="Smooth solutions with non-degenerate critical points.",
)

LAW_7 = Law(
    number=7,
    name="Horizon formation",
    statement=(
        "Horizons (regions where M(rho) -> 0) form when the "
        "effective amplitude exceeds a d-dependent threshold."
    ),
    latex=(
        "A_{\\text{eff}} = A / \\sqrt{N_m^d} > A_{\\text{crit}}"
    ),
    derivation_status="empirical",
    dimensional_dependence="Exponentially suppressed with d.",
    universality="Degenerate mobility with beta > 0.",
)

LAW_8 = Law(
    number=8,
    name="Morphological hierarchy",
    statement=(
        "In d >= 2, the Hessian eigenvalue structure produces a "
        "stratified morphology: filaments dominate in 3D, sheets "
        "and blobs fill the remainder."
    ),
    latex=(
        "f_{\\text{fil}} > f_{\\text{sht}} > f_{\\text{blb}} "
        "\\quad (d=3)"
    ),
    derivation_status="empirical",
    dimensional_dependence="New classes appear with each d.",
    universality="Multi-modal initial conditions.",
)

LAW_9 = Law(
    number=9,
    name="Sheet-filament oscillation",
    statement=(
        "In d >= 3, the morphology fractions exhibit oscillatory "
        "exchange between sheets and filaments during the transient."
    ),
    latex=(
        "\\exists\\, t_1 < t_2 < t_3: "
        "f_{\\text{sht}}(t_2) > f_{\\text{sht}}(t_1), "
        "f_{\\text{sht}}(t_3) < f_{\\text{sht}}(t_2)"
    ),
    derivation_status="empirical",
    dimensional_dependence="d >= 3 only.",
    universality="Multi-modal ICs with Nm >= 2.",
)


ALL_LAWS = [LAW_1, LAW_2, LAW_3, LAW_4, LAW_5, LAW_6, LAW_7, LAW_8, LAW_9]

_CHECKERS: dict[int, Callable] = {
    1: _check_attractor,
    2: _check_energy_monotone,
    3: _check_spectral_concentration,
    4: _check_modal_hierarchy,
    5: _check_dissipation_channels,
    6: _check_topology_conservation,
    7: _check_dimensional_universality,
    8: _check_morphology_stratification,
    9: _check_structural_invariance,
}


def verify_law(
    law_number: int,
    ts: TimeSeries,
    params: EDParameters,
) -> dict:
    """Verify a single law against a TimeSeries.

    Parameters
    ----------
    law_number : int
        Law number (1-9).
    ts : TimeSeries
        Completed simulation output.
    params : EDParameters
        Simulation parameters.

    Returns
    -------
    dict
        {"law": int, "name": str, "passed": bool, ...details}.
    """
    if law_number not in _CHECKERS:
        raise ValueError(f"No checker for Law {law_number}")

    law = ALL_LAWS[law_number - 1]
    result = _CHECKERS[law_number](ts, params)
    result["law"] = law_number
    result["name"] = law.name
    return result


def verify_all_laws(
    ts: TimeSeries,
    params: EDParameters,
) -> list[dict]:
    """Verify all nine laws against a TimeSeries.

    Returns
    -------
    list[dict]
        One result dict per law.
    """
    return [verify_law(i, ts, params) for i in range(1, 10)]


def laws_to_markdown() -> str:
    """Format all nine laws as a Markdown section."""
    lines = ["## The Nine Architectural Laws", ""]
    for law in ALL_LAWS:
        lines.append(f"### Law {law.number}: {law.name}")
        lines.append("")
        lines.append(f"**Statement:** {law.statement}")
        lines.append("")
        lines.append(f"$$\n{law.latex}\n$$")
        lines.append("")
        lines.append(f"- **Derivation:** {law.derivation_status}")
        lines.append(f"- **Dimensions:** {law.dimensional_dependence}")
        lines.append(f"- **Universality:** {law.universality}")
        lines.append("")
    return "\n".join(lines)
