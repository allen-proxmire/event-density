# ED Targeted Hooks

Audience-specific entry points for Event Density outreach. Each hook is designed to be dropped into a short email or message, linked directly to something ED produces, and connected to the minimal demo notebook.

---

## 1. Computational Cosmologists

> Event Density is a single canonical PDE that produces a BAO-like preferred correlation scale set by its internal telegraph frequency -- not by a sound horizon. The full simulation pipeline is open-source, runs in under 3 minutes, and reproduces flat weak-lensing signals at 100--1000 kpc where both NFW and Burkert profiles fail. The prediction is that galactic rotation velocities depend on star-formation activity at fixed baryonic mass -- something neither LCDM nor MOND predicts.

**Demo entry:** [ED_minimal_demo.ipynb](ED_minimal_demo.ipynb) -- Parts 1--2 (canonical PDE + nine laws)

---

## 2. Numerical / Computational Physicists

> ED-SIM-02 implements a nonlinear degenerate-mobility PDE with participation coupling, solved via implicit Euler and Crank-Nicolson integrators on grids up to 4D. The system has nine architectural laws, each with an automated verification function. The full 112-test validation suite and 9-phase reproducibility pipeline are included. If you work with nonlinear diffusion, free-boundary problems, or spectral methods for PDEs, the codebase is structured for direct inspection.

**Demo entry:** [ED_minimal_demo.ipynb](ED_minimal_demo.ipynb) -- Cell 4 (run simulation) + Cell 6 (verify all nine laws)

---

## 3. Foundations of Physics Researchers

> Event Density asks: what are the minimal constitutive primitives from which physically recognisable structure arises? The answer is four objects and seven axioms that determine a unique canonical PDE. Its three constitutive channels reproduce exponential decay, porous-medium diffusion, and telegraph oscillation -- not as analogies, but as exact structural reductions (0.00% error for the penalty and participation channels). The framework is falsifiable: every structural prediction has an explicit channel-silencing test.

**Demo entry:** [ED_minimal_demo.ipynb](ED_minimal_demo.ipynb) -- Parts 3--4 (RC decay and telegraph oscillation analogues)

---

## 4. Complexity Scientists / Santa Fe Institute Orbit

> A single scalar PDE with degenerate mobility, monostable penalty, and global participation produces emergent pair interactions between density structures: baseline nonlinear-mobility repulsion at zero coupling, and telegraph-modulated attraction/repulsion at finite coupling. These effective forces are not programmed in -- they emerge from the constitutive architecture. The system has five simultaneous Lyapunov functionals but is not a gradient flow of any of them, placing it outside the standard dissipative-systems classification.

**Demo entry:** [ED_minimal_demo.ipynb](ED_minimal_demo.ipynb) -- Part 5 (energy decay + dissipation channels). For the emergent interaction results, see `edsim/phys/analogues/temporal_tension.py` in the full repo.

---

## 5. Physics-Adjacent AI / Scientific Discovery Researchers

> Event Density is a complete, reproducible, computationally validated ontological framework implemented as a Python simulation engine. It has 14 implemented laws with automated verification, 9 structural analogues with explicit falsification criteria, and 56,000+ galactic data records. If you work on automated theory generation, symbolic regression, or AI-guided scientific discovery, this is a ground-truth benchmark: a minimal system that generates physics-shaped dynamics from constitutive principles, with every claim backed by executable code.

**Demo entry:** [ED_minimal_demo.ipynb](ED_minimal_demo.ipynb) -- the entire notebook is a self-contained pipeline run

---

## 6. PDE / Applied Mathematics Researchers

> The ED canonical PDE is a degenerate nonlinear diffusion equation with a monostable reaction term and a globally-coupled ODE. It reduces exactly to the porous-medium equation (m = beta + 1) when the penalty and participation are silenced, and to the telegraph equation when the mobility is silenced. The front-propagation exponent follows alpha_R = 1/(d*beta + 2), verified numerically in dimensions 1--3. The system possesses five simultaneous Lyapunov functionals and supports compact-support (sharp-front) solutions via the degenerate mobility.

**Demo entry:** [ED_minimal_demo.ipynb](ED_minimal_demo.ipynb) -- Part 3 (penalty channel = exponential decay). For the Barenblatt self-similarity analogue, see `edsim/phys/analogues/barenblatt.py`.

---

## 7. Galactic Dynamics / Dark Matter Researchers

> ED produces Burkert-matching rotation curves for dwarf galaxies (99.6% match) via a degenerate-mobility mechanism that creates flat cores without invoking dark matter halos. At spiral-galaxy scales, adding the temporal-tension channel reproduces NGC 3198 at 1.9 km/s RMS. At weak-lensing scales (100--1000 kpc), ED predicts flat V where Burkert falls to zero and NFW slowly declines -- consistent with Mistele et al. (2024) observations. The Baryonic Tully-Fisher exponent is 1/4, matching the free fit to within 0.2 sigma and rejecting LCDM's 1/3 at >3 sigma.

**Demo entry:** [ED_minimal_demo.ipynb](ED_minimal_demo.ipynb) for the foundational pipeline. Galactic results are in `documents/RESULTS_OVERVIEW.md` and `data/ED-Data-12` through `data/ED-Data-18`.

---

## 8. Information Geometry / Differential Geometry Researchers

> The ED density field induces a Hessian structure at each point whose eigenvalue morphology (filaments, sheets, blobs) is tracked as a simulation invariant. In 3D and 4D, the morphology fractions exhibit oscillatory exchange between sheets and filaments (Law 9). The connection between this Hessian structure and Riemannian curvature or information geometry is an open research direction. If you work on geometric structures arising from scalar fields, ED provides a concrete, computationally accessible test case.

**Demo entry:** [ED_minimal_demo.ipynb](ED_minimal_demo.ipynb) -- Cell 6 (law verification, including morphological hierarchy). For the full invariant atlas, see `edsim/invariants/`.

---

## Usage Notes

- Each hook is designed to be copy-pasted into the body of a short outreach email
- Always link to the **minimal demo notebook** as the first action item
- The ask is always the same: **"Run it. Tell me what you see."**
- Personalise by referencing the recipient's specific published work where it intersects with ED
