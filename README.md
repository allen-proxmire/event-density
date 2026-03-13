# Event Density — Ontology, Architecture, and Reproducible Simulation

## What is Event Density?

Event Density (ED) is an ontology — a way of describing reality — not in terms of particles, fields, or forces, but in terms of updating, or — becoming.

At the smallest scales, reality is continuously differentiating itself in what ED calls a micro‑event.
The event‑density of a region is the local rate at which these micro‑events occur.
Different regions update at different rates, producing ED gradients.
As in all systems with gradients, these differences drive flows that redistribute, synchronize, and reshape the underlying becoming.
From this interplay of becoming, gradients, and flow, ED derives the emergence of structure across all scales.

## Core primitives

**Becoming**: The continuous generative activity from which all distinctions, changes, and structures arise. Becoming is the substrate of reality; ED models how it distributes itself.

**Micro‑Event**: The smallest undirected differentiation within becoming — a minimal flicker of generative activity before any form, direction, or flow emerges.

**Gradient**: A directional difference in event‑density or flow across a region. Gradients drive movement, reorientation, and structural change.

**Flow**: The directed propagation of becoming through a region. Flow expresses how event‑density moves, redistributes, or reorganizes.

From these primitives, ED derives the familiar features of both cosmology and microphysics — the emergence of space and time, the formation of structure, and the architectural analogues of entanglement, spin, and baryogenesis.
ED defines a compositional rule that determines how regions combine, how gradients evolve, and how structures emerge. Saddles, boundaries, horizons, collapse, and compositionality are not assumptions — they are consequences of how becoming distributes itself.

ED is not a physical theory. It is an architectural and predictive one.
It shows that geometry and discrete gates can generate stable, predictive laws — and that these laws can be discovered, formalized, and reproduced.

ED is an architectural account of the structural possibilities for any universe.

The culmination of the ED program is the discovery of:
- three law surfaces governing all collapse behavior.
- seven architectural invariants that hold across all tested configurations.
- These and other findings can be reproduced through the simulations described below.

---

## Why this simulation?

The ED simulation in this repository is the minimal laboratory where the ontology becomes measurable.
The simulation uses particles moving ballistically on a ring — not because ED is about particles, but because this is the simplest substrate that exposes:

- exact closed‑form collapse laws.
- seven architectural invariants.
- compositionality.
- regime boundaries.
- the geometry of becoming.

ED is not the simulation. The simulation is the microscope; ED is the thing under the lens.

---

## What does this repository contain?

This repository provides:

1. The complete ED simulation pipeline.
 1. a fully reproducible workflow for regenerating every figure, invariant, and law surface.
2. The ED‑Arch series (ED‑Arch‑00 through ED‑Arch‑21).
3. The ED Research series.
   1. ED Foundations (ED‑01 through ED‑12.5).
   2. ED Interpretations (ED‑I‑01 through ED‑I‑31).
   3.ED Testing (open note for experimental predictions).
   4. ED Physical Computation (computational consequences).
   5. ED Simulations (historical simulation code).

---

## How to Reproduce the ED‑Arch Simulations? (Step‑by‑Step)

1. Clone this repository  
Use Git (git clone …) or download the ZIP from GitHub and unzip it.

2. Open a terminal window  
Command Prompt, PowerShell, or Anaconda Prompt all work.

3. Navigate into the repo folder  
Example: cd "C:\Users\allen\GitHub\Event Density"  
Make sure you see files like environment.yml and run_all.py.

4. Create the ED environment  
Run: conda env create -f environment.yml  
This installs the exact versions of Python, NumPy, Matplotlib, etc.

5. Activate the environment  
Run: conda activate ed-arch  
Your prompt should now begin with (ed-arch).

6. Run the golden experiment  
Run: python run_all.py --scenario H  
You should see: chi_ref = 0.4000, chi_emp = 0.4000, dev = 0.0000.

7. Run all ED‑Arch scenarios  
Run: python run_all.py --all  
This regenerates all figures, verifies all invariants, and writes results/summary.json.

8. (Optional) Regenerate everything from scratch  
Delete old outputs: rm -rf figures/* results/summary.json  
Then run: python run_all.py --all.

9. (Optional) Reproduce the Jupyter notebooks  
Run: jupyter notebook experiments/  
Then choose: Kernel → Restart & Run All.

10. You’re done  
You have reproduced all ED‑Arch law surfaces, invariants, canonical scenarios, and figures.
