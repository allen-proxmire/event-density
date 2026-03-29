"""
edsim.roadmap.architecture -- ED-SIM-03 next-generation architecture.

Defines the component structure, motivations, risks, and inter-component
dependencies for the third-generation ED simulation platform.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Component:
    """One architectural component of ED-SIM-03.

    Attributes
    ----------
    name : str
        Short identifier.
    title : str
        Descriptive title.
    description : str
        What this component does and why.
    motivation : str
        Why ED-SIM-03 needs this beyond ED-SIM-02.
    risks : tuple[str, ...]
        Technical or scientific risks.
    prerequisites : tuple[str, ...]
        Component names that must be complete first.
    outputs : tuple[str, ...]
        What this component produces.
    """

    name: str
    title: str
    description: str
    motivation: str
    risks: tuple = ()
    prerequisites: tuple = ()
    outputs: tuple = ()


@dataclass
class EDSIM3Architecture:
    """Full architectural specification for ED-SIM-03.

    Attributes
    ----------
    components : list[Component]
        All planned components.
    description : str
        One-paragraph summary.
    version : str
        Target version string.
    """

    components: list = field(default_factory=list)
    description: str = ""
    version: str = "0.2.0"

    def get(self, name: str) -> Component:
        for c in self.components:
            if c.name == name:
                return c
        raise KeyError(f"Unknown component: {name}")

    def names(self) -> list[str]:
        return [c.name for c in self.components]


def build_edsim3_architecture() -> EDSIM3Architecture:
    """Define the ED-SIM-03 architecture.

    Returns
    -------
    EDSIM3Architecture
        Complete next-generation architectural plan.
    """
    components = [
        Component(
            name="multi_field",
            title="Multi-Field Coupling",
            description=(
                "Extend the single-scalar ED PDE to coupled systems: "
                "(rho_1, rho_2, ..., rho_n) with cross-mobility and "
                "cross-penalty terms.  Enables ED models of multi-component "
                "systems and field-field interaction."
            ),
            motivation=(
                "ED-SIM-02 evolves a single density.  Physical systems "
                "often involve coupled fields (e.g., matter + radiation, "
                "two-fluid models).  Multi-field ED is the natural extension."
            ),
            risks=(
                "Cross-coupling may break the Lyapunov structure",
                "Constitutive function design is non-trivial",
                "Computational cost scales as n^2 per coupling",
            ),
            prerequisites=(),
            outputs=(
                "Multi-field solver",
                "Cross-mobility constitutive library",
                "Coupled invariant atlas",
            ),
        ),
        Component(
            name="stochastic",
            title="Stochastic Forcing",
            description=(
                "Add multiplicative or additive noise to the ED PDE: "
                "d rho = F[rho] dt + sigma(rho) dW.  Enables the study "
                "of fluctuation-driven phenomena, nucleation, and noise-induced "
                "transitions."
            ),
            motivation=(
                "The deterministic ED PDE always relaxes to rho*.  "
                "Stochastic forcing can sustain non-trivial steady states, "
                "produce intermittency, and model thermal fluctuations."
            ),
            risks=(
                "Noise + degenerate mobility may produce blow-up",
                "Numerical stability of stochastic integrators",
                "Invariant definitions need adaptation for stochastic systems",
            ),
            prerequisites=(),
            outputs=(
                "Stochastic integrator (Euler-Maruyama, Milstein)",
                "Noise-aware invariant atlas",
                "Fluctuation spectrum analysis",
            ),
        ),
        Component(
            name="adaptive_grid",
            title="Adaptive Mesh Refinement (AMR)",
            description=(
                "Replace uniform grids with locally refined meshes that "
                "concentrate resolution near horizons, filaments, and "
                "sharp gradients."
            ),
            motivation=(
                "4D simulations at N=64 require 16M grid points.  AMR "
                "can achieve equivalent accuracy with 10-100x fewer points "
                "by refining only where needed."
            ),
            risks=(
                "AMR + spectral methods is non-trivial",
                "Load balancing on GPU",
                "Invariant computation on non-uniform grids",
            ),
            prerequisites=("gpu_solver",),
            outputs=(
                "AMR data structure (quadtree/octree)",
                "Refinement criteria (gradient, curvature)",
                "AMR-aware operators",
            ),
        ),
        Component(
            name="gpu_solver",
            title="GPU-Native Solver",
            description=(
                "Rewrite the core solver in JAX or CuPy for GPU execution.  "
                "All operators, integrators, and invariants run on GPU "
                "without host-device transfer."
            ),
            motivation=(
                "3D and 4D simulations are memory- and compute-bound.  "
                "GPU execution provides 10-100x speedup for structured grids."
            ),
            risks=(
                "JAX ecosystem maturity",
                "Memory constraints for 4D arrays on consumer GPUs",
                "Reproducibility across hardware",
            ),
            prerequisites=(),
            outputs=(
                "JAX/CuPy solver backend",
                "GPU-resident invariant computation",
                "Benchmark suite (CPU vs GPU)",
            ),
        ),
        Component(
            name="spectral_fd_hybrid",
            title="Spectral-FD Hybrid Integrator",
            description=(
                "Combine spectral methods (FFT/DCT) for the linear part "
                "with finite differences for the nonlinear part in a "
                "dimension-agnostic IMEX framework."
            ),
            motivation=(
                "ETD-RK4 is currently 2D-only.  A general IMEX hybrid "
                "would provide spectral accuracy in all dimensions "
                "while handling nonlinearity robustly."
            ),
            risks=(
                "IMEX stability at high Reynolds-like numbers",
                "DCT compatibility with AMR",
            ),
            prerequisites=(),
            outputs=(
                "IMEX-RK integrator (ARK4/5)",
                "Spectral Laplacian for d=1..6",
                "Nonlinear FD evaluator",
            ),
        ),
        Component(
            name="high_dim",
            title="5D/6D Generalisation",
            description=(
                "Extend the solver and invariant atlas to d=5 and d=6.  "
                "Test the factorial complexity law and gradient dominance "
                "at higher dimensions."
            ),
            motivation=(
                "ED-Phys-39 predicts asymptotic behaviour for d -> infinity.  "
                "Testing at d=5,6 validates these predictions and completes "
                "the dimensional program."
            ),
            risks=(
                "Memory: N^6 at N=16 = 16M points",
                "Morphology classification beyond d=4 is combinatorially complex",
                "Visualization in d>3 requires projection",
            ),
            prerequisites=("gpu_solver",),
            outputs=(
                "5D/6D solver",
                "5D/6D invariant atlas",
                "Dimensional law verification at d=5,6",
            ),
        ),
        Component(
            name="realtime_viz",
            title="Real-Time Visualisation",
            description=(
                "Interactive 3D visualisation of ED fields using WebGL "
                "or PyVista.  Live invariant dashboards during simulation."
            ),
            motivation=(
                "ED-SIM-02 generates static Matplotlib figures post-run.  "
                "Real-time visualisation enables exploratory science and "
                "parameter steering."
            ),
            risks=(
                "Browser-based rendering performance",
                "Data transfer overhead for large 3D fields",
            ),
            prerequisites=(),
            outputs=(
                "Interactive 3D field viewer",
                "Live invariant dashboard",
                "Animation export (GIF/MP4)",
            ),
        ),
        Component(
            name="interactive_nb",
            title="Interactive Notebooks",
            description=(
                "Jupyter notebooks with ipywidgets for parameter exploration, "
                "regime selection, and cross-framework comparison."
            ),
            motivation=(
                "Lower the barrier to entry for new users.  Enable rapid "
                "exploration of the parameter space and regime manifold."
            ),
            risks=(
                "Widget compatibility across Jupyter versions",
                "Performance for 3D/4D simulations in notebooks",
            ),
            prerequisites=("realtime_viz",),
            outputs=(
                "Parameter explorer notebook",
                "Regime navigator notebook",
                "Law verification dashboard",
            ),
        ),
        Component(
            name="formal_proofs",
            title="Formal Proof Infrastructure",
            description=(
                "Machine-checkable proofs for Laws 2 and 5 (derived laws) "
                "using Lean 4 or Coq.  Provide a proof skeleton for the "
                "remaining laws."
            ),
            motivation=(
                "ED-Phys-36 provides partial derivations.  Formal proofs "
                "elevate the architectural laws from empirical observations "
                "to mathematical theorems."
            ),
            risks=(
                "Lean/Coq formalisation of nonlinear PDE theory is immature",
                "Proof engineering effort is high",
            ),
            prerequisites=(),
            outputs=(
                "Lean 4 proof files for Laws 2, 5",
                "Proof sketches for Laws 1, 3, 4, 6",
                "Formal specification of the ED axiom system",
            ),
        ),
        Component(
            name="experimental_bridge",
            title="Experimental Bridge",
            description=(
                "Map ED predictions to specific experimental observables "
                "in condensed matter, astrophysics, or quantum systems.  "
                "Design concrete falsifiable experiments."
            ),
            motivation=(
                "ED-Phys-38 identifies PME as the closest structural relative.  "
                "An experimental bridge would anchor ED predictions to "
                "measurable quantities in real systems."
            ),
            risks=(
                "Parameter mapping may be degenerate",
                "ED predictions may be too generic to distinguish from PME",
            ),
            prerequisites=("multi_field",),
            outputs=(
                "Prediction catalogue for thin-film experiments",
                "Prediction catalogue for dark-matter halo profiles",
                "Experimental design document",
            ),
        ),
    ]

    return EDSIM3Architecture(
        components=components,
        description=(
            "ED-SIM-03 extends the second-generation platform with "
            "multi-field coupling, stochastic forcing, GPU-native solvers, "
            "adaptive grids, higher-dimensional generalisation (d=5,6), "
            "interactive visualisation, formal proof infrastructure, and "
            "an experimental bridge to physical measurements."
        ),
        version="0.2.0",
    )
