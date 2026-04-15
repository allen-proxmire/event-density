# Event Density: What It Does

**Event Density (ED) is a candidate unifying ontology for physical law, built from four primitives and seven axioms, whose structural consequences reproduce known physics without importing it.**

---

## What ED Does

- Derives a unique canonical PDE from seven structural axioms -- not postulated, not fitted
- Reproduces exponential decay, porous-medium diffusion, and telegraph oscillation as structural consequences of three constitutive channels
- Produces nine architectural laws verified across spatial dimensions 1 through 4
- Generates dwarf galaxy rotation curves matching Burkert profiles to 99.6%
- Predicts flat weak-lensing signals at 100--1000 kpc, a Baryonic Tully-Fisher exponent of 1/4, and activity-dependent rotation velocities that distinguish ED from both MOND and LCDM

---

## The Core Architectural Idea

Start with the question: *what are the minimal primitives from which physically recognisable structure arises?*

The answer is four objects:

| Primitive | What it does |
|-----------|-------------|
| **Density** | Bounded scalar field -- the state variable |
| **Mobility** | Degenerate diffusion coefficient that vanishes at capacity, creating free boundaries (horizons) |
| **Penalty** | Monostable restoring force driving toward a unique equilibrium |
| **Participation** | Global feedback variable creating non-local oscillatory dynamics |

Seven structural axioms (locality, isotropy, gradient-driven flow, dissipative structure, single scalar field, minimal coupling, dimensional consistency) constrain these four primitives into a unique canonical PDE. The PDE decomposes into three independently testable channels.

---

## The Minimal Ontology

The ED system is distinguished by five features that no other known scalar PDE possesses simultaneously:

1. Degenerate mobility creating free boundaries
2. Monostable penalty driving a unique attractor
3. Global participation producing telegraph oscillation
4. Five simultaneous Lyapunov functionals
5. Not a gradient flow of any of them

---

## The Reproducible Pipeline

Everything is implemented in ED-SIM-02, an open-source simulation platform:

- **14 implemented laws** with automated verification functions
- **9 structural analogues** across 2D and 3D, each with explicit falsification conditions
- **112-test validation suite** and a 9-phase reproducibility pipeline
- **56,000+ data records** from galactic-scale comparisons
- **Single entry point:** `run_simulation(config)` produces a complete TimeSeries with energy, spectral, dissipation, morphology, and topology invariants

---

## One Concrete Example

**Penalty channel = RC-circuit decay.**

Silence the mobility and participation channels. The ED PDE reduces to:

```
d(delta)/dt = -D * P0 * delta
```

This is the RC-circuit discharge equation. The time constant is 1/(D*P0). The error between ED and the analytical prediction is **0.00%**. This is not an analogy -- the governing equation is identical. The correspondence holds for all parameter values, without fitting.

Turn the participation channel on, and the system becomes a telegraph oscillator (RLC circuit) with analytically predictable frequency and damping, also at **0.00% error**.

---

## Run It Yourself

The minimal demo notebook runs the full pipeline in under 3 minutes:

**[`outreach/ED_minimal_demo.ipynb`](ED_minimal_demo.ipynb)**

Clone the repo, open the notebook, press "Run All."

**Repository:** [github.com/Allen-Proxmire/Event-Density](https://github.com/Allen-Proxmire/Event-Density)

---

*Allen Proxmire -- Event Density Research Programme*
