# ED-SIM-02 Documentation

## What is ED-SIM-02?

ED-SIM-02 is the second-generation simulation platform for the Event Density (ED) framework. It provides a modular, tested, and reproducible environment for solving the canonical ED partial differential equation in two, three, and four spatial dimensions. The platform computes a full invariant atlas at every output time step and includes a nine-phase validation pipeline that checks the architectural laws of the ED system.

The platform is written in Python, depends only on NumPy, SciPy, and Matplotlib, and is designed for scientific clarity rather than computational throughput.

## Who is this for?

ED-SIM-02 is intended for:

- **Researchers** exploring the Event Density framework who want to reproduce the results of ED-Phys-35 through ED-Phys-40 or extend them to new parameter regimes.
- **Scientists** studying nonlinear parabolic PDEs (porous-medium equations, reaction-diffusion systems, geometric flows) who want a well-instrumented comparison platform.
- **Students** learning about PDE simulation, spectral methods, or invariant computation who want a small, readable codebase with comprehensive tests.

You should be comfortable reading Python and have a working understanding of PDEs and spectral methods. You do not need to know the ED-Phys series in detail; the code is self-contained.

## How This Documentation is Organized

| Document | Content |
|----------|---------|
| [Usage Guide](usage.md) | How to construct parameters, run simulations, use scenarios, and inspect results. Includes code snippets. |
| [Architecture](architecture.md) | How the platform is structured: layers, modules, design principles. No equations; conceptual overview only. |
| [API Overview](api.md) | Key classes and functions with import paths and one-line descriptions. |
| [Lab Tour Notebook](../examples/edsim_lab_tour.ipynb) | A hands-on walkthrough: run a scenario, plot invariants, interpret results. |
| [Performance](performance.md) | Backend acceleration (Numba/JAX), benchmarks, limitations. |

For the underlying physics, see the ED-Phys series in `research/ED Physics/`, particularly:

- **ED-Phys-40** (`research/ED Physics/ED-Phys-40_Synthesis/`) for the nine laws and invariant atlas.
- **ED-Phys-38** (`research/ED Physics/ED-Phys-38_CrossFramework/`) for how ED relates to PME, AC, CH, and other PDEs.
- **ED-Phys-39** (`research/ED Physics/ED-Phys-39_HigherDim/`) for the 4D predictions.
