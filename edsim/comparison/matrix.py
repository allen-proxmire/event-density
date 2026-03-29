"""
edsim.comparison.matrix -- Cross-framework comparison matrix.

Builds a structured matrix comparing frameworks along five axes:
ontology, primitives, dynamics, invariants, epistemology.

Each cell contains an overlap score (0-3) and a qualitative note.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .frameworks import Framework, load_frameworks


@dataclass
class CellEntry:
    """One cell in the comparison matrix.

    Attributes
    ----------
    axis : str
        Comparison axis (ontology, primitives, dynamics, invariants, epistemology).
    framework_a : str
        Name of the first framework.
    framework_b : str
        Name of the second framework (always "event_density").
    score : int
        Overlap score: 0 = none, 1 = weak, 2 = moderate, 3 = strong.
    note : str
        Qualitative description of the overlap or divergence.
    """

    axis: str
    framework_a: str
    framework_b: str = "event_density"
    score: int = 0
    note: str = ""


@dataclass
class ComparisonMatrix:
    """Full cross-framework comparison matrix.

    Attributes
    ----------
    frameworks : list[str]
        Names of all compared frameworks.
    axes : list[str]
        Comparison axes.
    entries : dict[tuple[str, str], CellEntry]
        Keyed by (framework_name, axis).
    """

    frameworks: list = field(default_factory=list)
    axes: list = field(default_factory=lambda: [
        "ontology", "primitives", "dynamics", "invariants", "epistemology",
    ])
    entries: dict = field(default_factory=dict)

    def get(self, framework: str, axis: str) -> Optional[CellEntry]:
        """Retrieve a cell entry."""
        return self.entries.get((framework, axis))

    def total_score(self, framework: str) -> int:
        """Sum of overlap scores across all axes for one framework."""
        return sum(
            e.score for k, e in self.entries.items()
            if k[0] == framework
        )

    def to_table(self) -> str:
        """Format as a Markdown table."""
        header = "| Framework | " + " | ".join(self.axes) + " | Total |"
        sep = "|" + "|".join(["---"] * (len(self.axes) + 2)) + "|"
        lines = [header, sep]
        for fw in self.frameworks:
            if fw == "event_density":
                continue
            cells = []
            for ax in self.axes:
                e = self.get(fw, ax)
                cells.append(str(e.score) if e else "-")
            total = self.total_score(fw)
            lines.append(f"| {fw} | " + " | ".join(cells) + f" | {total} |")
        return "\n".join(lines)


# ══════════════════════════════════════════════════════════════════════
#  Comparison rules
# ══════════════════════════════════════════════════════════════════════

_COMPARISONS: dict[tuple[str, str], tuple[int, str]] = {
    # Causal Sets
    ("causal_sets", "ontology"): (
        1,
        "Both start from events.  Causal sets use discrete partial orders; "
        "ED uses a continuous scalar field.  No continuous manifold in causal sets."
    ),
    ("causal_sets", "primitives"): (
        0,
        "Causal sets: discrete elements + causal order.  "
        "ED: continuous density + mobility + penalty.  No structural overlap."
    ),
    ("causal_sets", "dynamics"): (
        0,
        "Causal sets: stochastic birth process.  "
        "ED: deterministic PDE.  Fundamentally different update rules."
    ),
    ("causal_sets", "invariants"): (
        1,
        "Both have volume-like invariants (diamond volumes vs mass).  "
        "Causal sets lack dissipation channels and spectral entropy."
    ),
    ("causal_sets", "epistemology"): (
        1,
        "Both produce dimensional quantities.  Causal sets measure "
        "causal structure; ED measures density, gradients, spectra."
    ),

    # Entropic Gravity
    ("entropic_gravity", "ontology"): (
        2,
        "Both treat entropy as fundamental.  Entropic gravity uses "
        "holographic screens; ED uses a density field.  Shared: entropy "
        "gradients drive dynamics."
    ),
    ("entropic_gravity", "primitives"): (
        1,
        "Entropic gravity: S, T, A.  ED: rho, M, P.  "
        "Shared concept of entropy, but different mathematical objects."
    ),
    ("entropic_gravity", "dynamics"): (
        1,
        "Entropic gravity: F = T dS/dx.  ED: gradient flow with "
        "Lyapunov functional.  Both are driven by entropy/energy gradients, "
        "but ED has a full PDE while entropic gravity has a force law."
    ),
    ("entropic_gravity", "invariants"): (
        2,
        "Both have entropy non-decrease and energy conservation.  "
        "ED adds dissipation channel decomposition, spectral entropy, "
        "morphological invariants."
    ),
    ("entropic_gravity", "epistemology"): (
        1,
        "Entropic gravity: gravitational acceleration, horizon temperature.  "
        "ED: density field, gradients, spectra, topology."
    ),

    # Constructor Theory
    ("constructor_theory", "ontology"): (
        1,
        "Constructor theory: tasks and possibility.  ED: density and flow.  "
        "Shared: both constrain what dynamics can occur via axioms."
    ),
    ("constructor_theory", "primitives"): (
        0,
        "Constructor theory: tasks, constructors.  ED: rho, M, P.  "
        "No structural overlap in primitives."
    ),
    ("constructor_theory", "dynamics"): (
        0,
        "Constructor theory has no evolution equation.  "
        "ED is defined by a PDE.  Fundamentally different."
    ),
    ("constructor_theory", "invariants"): (
        1,
        "Constructor theory: constructor invariance, composability.  "
        "ED: Lyapunov energy, mass.  Shared: invariance under "
        "transformation, but different mathematical objects."
    ),
    ("constructor_theory", "epistemology"): (
        0,
        "Constructor theory: which tasks are possible.  "
        "ED: quantitative field observables.  No overlap."
    ),

    # Hydrodynamics
    ("hydrodynamics", "ontology"): (
        2,
        "Both describe continuous fields on bounded domains.  "
        "Hydrodynamics has vector fields (velocity); ED is scalar only."
    ),
    ("hydrodynamics", "primitives"): (
        2,
        "Both have density rho(x,t) as a primary field.  "
        "Hydrodynamics adds velocity and pressure; ED adds "
        "mobility, penalty, and participation."
    ),
    ("hydrodynamics", "dynamics"): (
        2,
        "Both are parabolic PDEs with diffusion.  Navier-Stokes has "
        "advection (nonlinear transport); ED has degenerate mobility "
        "and penalty relaxation.  Shared: Laplacian smoothing."
    ),
    ("hydrodynamics", "invariants"): (
        2,
        "Both conserve mass.  Hydrodynamics conserves momentum and "
        "energy; ED has monotone energy decay (dissipative, not conservative).  "
        "Shared: mass conservation.  Different: energy treatment."
    ),
    ("hydrodynamics", "epistemology"): (
        2,
        "Both produce density fields, correlation functions, spectra.  "
        "Hydrodynamics adds velocity and pressure fields."
    ),

    # Statistical Mechanics
    ("statistical_mechanics", "ontology"): (
        2,
        "Both describe distributions evolving toward equilibrium.  "
        "StatMech uses phase-space distributions; ED uses a spatial density."
    ),
    ("statistical_mechanics", "primitives"): (
        2,
        "Both have density/distribution as primary.  StatMech has "
        "Hamiltonian and temperature; ED has mobility and penalty.  "
        "Shared: state-dependent diffusion."
    ),
    ("statistical_mechanics", "dynamics"): (
        3,
        "Fokker-Planck equation is the closest structural match to ED.  "
        "Both: diffusion + drift/penalty.  Shared: gradient-flow structure.  "
        "Difference: ED has degenerate mobility and participation coupling."
    ),
    ("statistical_mechanics", "invariants"): (
        3,
        "Both have entropy (spectral/Boltzmann), energy (Lyapunov/free energy), "
        "mass/probability conservation.  Shared: H-theorem ~ energy monotonicity.  "
        "ED adds morphological invariants and dissipation channels."
    ),
    ("statistical_mechanics", "epistemology"): (
        2,
        "Both produce correlation functions, fluctuation spectra, "
        "thermodynamic-like observables.  StatMech adds response functions."
    ),

    # Quantum Foundations
    ("quantum_foundations", "ontology"): (
        1,
        "Quantum: Hilbert space states.  ED: scalar density field.  "
        "Shared: density matrix rho ~ ED density rho (structural analogy)."
    ),
    ("quantum_foundations", "primitives"): (
        1,
        "Quantum: |psi>, H, Born rule.  ED: rho, M, P.  "
        "Shared: density-like primary object."
    ),
    ("quantum_foundations", "dynamics"): (
        1,
        "Schrodinger is linear and unitary; ED is nonlinear and dissipative.  "
        "Both are second-order in space.  Shared: diffusion-like Laplacian."
    ),
    ("quantum_foundations", "invariants"): (
        1,
        "Quantum: unitarity, norm, von Neumann entropy (constant).  "
        "ED: energy monotone, spectral entropy (decreasing).  "
        "Opposite entropy behaviour (constant vs decreasing)."
    ),
    ("quantum_foundations", "epistemology"): (
        1,
        "Quantum: measurement outcomes, expectation values.  "
        "ED: field observables, invariant atlas.  Different measurement theories."
    ),
}


def build_comparison_matrix(
    frameworks: list[Framework] = None,
) -> ComparisonMatrix:
    """Build the full comparison matrix.

    Parameters
    ----------
    frameworks : list[Framework], optional
        Frameworks to compare.  Defaults to load_frameworks().

    Returns
    -------
    ComparisonMatrix
    """
    if frameworks is None:
        frameworks = load_frameworks()

    matrix = ComparisonMatrix(
        frameworks=[f.name for f in frameworks],
    )

    for fw in frameworks:
        if fw.name == "event_density":
            continue
        for axis in matrix.axes:
            key = (fw.name, axis)
            score, note = _COMPARISONS.get(key, (0, "Not assessed."))
            matrix.entries[key] = CellEntry(
                axis=axis,
                framework_a=fw.name,
                score=score,
                note=note,
            )

    return matrix
