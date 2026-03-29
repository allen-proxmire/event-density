"""
edsim.math.appendix -- Auto-generated mathematical appendix for the manuscript.

Assembles content from modal, transients, architecture, and laws modules
into a single Markdown document suitable for inclusion in the ED-SIM-02
manuscript.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import numpy as np

from ..core.parameters import EDParameters
from ..experiments.runner import TimeSeries
from ..experiments.scenarios import get_scenario
from ..experiments.atlas import run_atlas
from .modal import compute_modal_spectrum, extract_modal_hierarchy, modal_decay_rates
from .transients import (
    classify_transient,
    compute_transient_invariants,
    TransientType,
)
from .architecture import (
    ArchitecturalAxioms,
    CanonicalPDE,
    derive_canonical_pde,
    derivation_to_markdown,
)
from .laws import ALL_LAWS, verify_all_laws, laws_to_markdown


def _section_header(title: str, level: int = 1) -> str:
    return f"{'#' * level} {title}\n"


def _modal_summary(
    params: EDParameters,
    ts: TimeSeries,
) -> str:
    """Generate the modal hierarchy section."""
    ms = compute_modal_spectrum(ts, params)
    mh = extract_modal_hierarchy(ms)
    rates = modal_decay_rates(ms)

    lines = [
        _section_header("A.1  Modal Hierarchy", 2),
        "The spectral decomposition of the density field reveals the "
        "modal cascade structure of the ED transient.",
        "",
        f"- **Primary mode index:** {mh.primary_k}",
        f"- **Primary amplitude (t=0):** {mh.primary_amplitude:.6e}",
        f"- **Hierarchy ratio (A_1/A_2):** {mh.hierarchy_ratio:.2f}",
        f"- **Energy concentration (top 10%):** {mh.energy_concentration:.4f}",
        f"- **Inertial range:** [{mh.inertial_range[0]:.2f}, {mh.inertial_range[1]:.2f}]",
        f"- **Inertial exponent alpha:** {mh.inertial_exponent:.3f}",
        f"- **Dissipative cutoff:** {mh.dissipative_cutoff:.2f}",
        "",
    ]

    # Decay rate table
    if rates.size > 0:
        n_show = min(8, rates.size)
        sorted_idx = np.argsort(rates)[::-1]
        lines.append("**Top modal decay rates:**")
        lines.append("")
        lines.append("| Mode index | |k| | sigma_k |")
        lines.append("|-----------|-----|---------|")
        for j in range(n_show):
            idx = sorted_idx[j]
            lines.append(
                f"| {ms.k_values[idx]} "
                f"| {ms.k_magnitudes[idx]:.2f} "
                f"| {rates[idx]:.4f} |"
            )
        lines.append("")

    return "\n".join(lines)


def _transient_summary(
    params: EDParameters,
    ts: TimeSeries,
) -> str:
    """Generate the transient classification section."""
    ms = compute_modal_spectrum(ts, params)
    mh = extract_modal_hierarchy(ms)
    tc = classify_transient(ts, mh, ms)
    inv = tc.invariants

    lines = [
        _section_header("A.2  Transient Classification", 2),
        f"**Classification:** {tc.transient_type.value}",
        f"**Confidence:** {tc.confidence:.2f}",
        "",
        "**Transient invariants:**",
        "",
        f"| Invariant | Value |",
        f"|-----------|-------|",
        f"| Relaxation time tau | {inv.relaxation_time:.6f} |",
        f"| Modal turnover rate | {inv.modal_turnover_rate:.4f} |",
        f"| Entropy drop Delta H | {inv.entropy_drop:.4f} |",
        f"| Entropy slope dH/dt | {inv.entropy_slope:.4f} |",
        f"| Correlation growth exponent | {inv.correlation_growth_exponent:.4f} |",
        f"| Energy curvature (mean d^2E/dt^2) | {inv.energy_curvature:.6e} |",
        f"| Plateau fraction | {inv.plateau_fraction:.4f} |",
        f"| Mode switches | {inv.mode_switches} |",
        "",
        "**Evidence:**",
        "",
    ]
    for k, v in tc.evidence.items():
        lines.append(f"- {k}: {v}")
    lines.append("")

    return "\n".join(lines)


def _architecture_section() -> str:
    """Generate the architectural derivation section."""
    lines = [
        _section_header("A.3  Architectural Derivation", 2),
        derivation_to_markdown(),
        "",
    ]
    return "\n".join(lines)


def _laws_section(
    params: EDParameters,
    ts: TimeSeries,
) -> str:
    """Generate the nine laws section with verification results."""
    lines = [
        _section_header("A.4  The Nine Architectural Laws", 2),
        laws_to_markdown(),
        "",
        _section_header("A.5  Law Verification", 2),
        "Verification against the canonical 2D cosine scenario:",
        "",
        "| Law | Name | Passed | Key detail |",
        "|-----|------|--------|------------|",
    ]

    results = verify_all_laws(ts, params)
    for r in results:
        key_detail = ""
        if "rho_std_final" in r:
            key_detail = f"rho_std = {r['rho_std_final']:.4e}"
        elif "violations" in r:
            key_detail = f"violations = {r['violations']}"
        elif "delta_H" in r:
            key_detail = f"delta_H = {r['delta_H']:.4f}"
        elif "A0_leading" in r:
            key_detail = f"A0 = {r['A0_leading']:.4e}"
        elif "mean_sum" in r:
            key_detail = f"sum = {r['mean_sum']:.4f}"
        elif "n_unique" in r:
            key_detail = f"n_unique = {r['n_unique']}"
        elif "error" in r:
            key_detail = f"error = {r['error']:.4f}"
        elif "n_nonzero_classes" in r:
            key_detail = f"classes = {r['n_nonzero_classes']}"
        elif "relative_change" in r:
            key_detail = f"change = {r['relative_change']:.6f}"

        status = "PASS" if r.get("passed", False) else "FAIL"
        lines.append(
            f"| {r['law']} | {r['name']} | {status} | {key_detail} |"
        )
    lines.append("")

    return "\n".join(lines)


def build_math_appendix(
    output_path: str = "manuscript/ED-SIM-02-Appendix-Math.md",
    scenario_name: str = "A_2d_cosine",
) -> str:
    """Build the complete mathematical appendix.

    Runs the specified scenario, computes all mathematical diagnostics,
    and assembles the appendix as a Markdown document.

    Parameters
    ----------
    output_path : str
        Path to write the appendix file.
    scenario_name : str
        Scenario to use for examples and verification.

    Returns
    -------
    str
        Path to the written file.
    """
    # Run a scenario
    scenario = get_scenario(scenario_name)
    params, ts = run_atlas(scenario)

    # Assemble sections
    sections = [
        _section_header("Mathematical Appendix: ED-SIM-02", 1),
        "This appendix is auto-generated from the `edsim.math` package.",
        "",
        _modal_summary(params, ts),
        _transient_summary(params, ts),
        _architecture_section(),
        _laws_section(params, ts),
    ]

    content = "\n".join(sections)

    # Write
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")

    return str(out)
