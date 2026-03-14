# Event Density — Ontology, Architecture, and Reproducible Simulation

Event Density (ED) is an ontology — a way of describing reality — not in terms of particles, fields, or forces, but in terms of **updating**, or **becoming**.

At the smallest scales, reality is continuously differentiating itself in what ED calls a **micro‑event**.  
The **event‑density** of a region is the local rate at which these micro‑events occur.  
Different regions update at different rates, producing **ED gradients**.  
As in all systems with gradients, these differences drive flows that redistribute, synchronize, and reshape the underlying becoming.

From this interplay of becoming, gradients, and flow, ED derives the emergence of structure across all scales.

---

# 1. The ED Ontology

## Core primitives

**Becoming**  
The continuous generative activity from which all distinctions, changes, and structures arise.

**Micro‑Event**  
The smallest undirected differentiation within becoming — a minimal flicker of generative activity before any form, direction, or flow emerges.

**Gradient**  
A directional difference in event‑density or flow across a region. Gradients drive movement, reorientation, and structural change.

**Flow**  
The directed propagation of becoming through a region. Flow expresses how event‑density moves, redistributes, or reorganizes.

From these primitives, ED derives:

- saddles  
- boundaries  
- horizons  
- collapse  
- compositionality  
- architectural invariants  

These are not assumptions — they are consequences of how becoming distributes itself.

ED is not a physical theory.  
It is an **architectural and predictive** one.

---

# 2. Why This Simulation Exists

The ED simulation in this repository is the **minimal laboratory** where the ontology becomes measurable.

It uses particles moving ballistically on a ring — not because ED is about particles, but because this is the simplest substrate that exposes:

- exact closed‑form collapse laws  
- seven architectural invariants  
- compositionality  
- regime boundaries  
- the geometry of becoming  

**ED is not the simulation.**  
The simulation is the microscope; ED is the thing under the lens.

---

# 3. The ED‑Arch Architecture Stack

ED‑Arch is the computational backbone of the ED program.  
It consists of four layers:

```
ED‑Arch‑00  →  MicroEvent Engine
ED‑Arch‑20  →  Analytic Law‑Surface Oracle
ED‑Arch‑21  →  Invariant Harness
ED‑Arch‑22  →  Physics Analogs (coming next)
```

### **ED‑Arch‑00 — MicroEvent Engine**
Deterministic microscopic dynamics:

- ballistic motion  
- γ‑gated interaction laws  
- mechanism classification  
- PBC geometry  
- collapse detection  

### **ED‑Arch‑20 — Analytic Oracle**
Closed‑form predictions for:

- collapse time χ  
- angular‑rate law  
- DECAY windows  
- Pythagorean drift  

### **ED‑Arch‑21 — Invariant Harness**
Seven architectural invariants:

1. 3×3 Sheet Compositionality  
2. Memoryless Law‑Surface Switching  
3. Pythagorean Tangential Drift  
4. Programmed Collapse  
5. Perturbation Hardness  
6. DECAY Angular Sub‑Regime  
7. Ghost Compositionality  

All seven pass.

### **ED‑Arch‑22 — Physics Analogs (coming next)**

- optics analogs  
- cosmology analogs  
- quantum‑like analogs  

---

# 4. 📘 ED‑Arch Orientation Map

ED‑Arch is a **computational testbed** for the ED ontology — a controlled “toy universe” that:

- simulates collapse dynamics  
- generates law surfaces  
- identifies mechanism regimes  
- validates structural invariants  
- produces falsifiable predictions  

ED‑Arch is the **instrument** that tests ED.

---

# 5. 🧭 What This System Tests

When you run the ED‑Arch harness, it evaluates six core predictions of the ED ontology.

## **1. Law‑Surface Geometry**
Predicts collapse behavior across `(d, ncl, γ)` and classifies mechanisms:

- inward‑collapse  
- outward‑PBC  
- DECAY  

**Results:**  
- 56 analytic points sampled  
- `max_deviation = 0.0`  
- `all_passed = true`

---

## **2. DECAY Window Boundaries**
Identifies the forbidden band where collapse cannot occur.

**Results:**  
- clean `(d_lower, d_upper)` windows for ncl = 3–6  
- `boundary_accuracy = 1.0`  
- `all_passed = true`

---

## **3. Angular Rate Law**



\[
K = 2 \sin(\pi / ncl)
\]



**Results:**  
- `k_pred == k_emp` for all ncl  
- `max_deviation = 0.0`

---

## **4. Invariant Suite (Arch‑21)**

| ID | Name | Status | Max Dev |
|----|------|--------|---------|
| INV‑21‑1 | 3×3 Sheet Compositionality | PASS | 0.0050 |
| INV‑21‑2 | Memoryless Law‑Surface Jumps | PASS | 0.0000 |
| INV‑21‑3 | Pythagorean Tangential Drift | PASS | ~3e‑13 |
| INV‑21‑4 | Geometry‑Aware Programmed Collapse | PASS | 0.0019 |
| INV‑21‑5 | Perturbation Hardness Hierarchy | PASS | 0.0000 |
| INV‑21‑6 | DECAY Angular Sub‑Regime | PASS | 0.0000 |
| INV‑21‑7 | Ghost Compositionality | PASS | 0.0050 |

All invariants passed.

---

# 6. 🔗 How ED‑Arch Connects to ED

- **ED is the ontology** — the deep structure of micro‑events.  
- **ED‑Arch is the architecture** — a computational universe that instantiates ED’s predictions.  
- ED‑Arch tests ED by comparing empirical collapse behavior to analytic law surfaces.  
- ED‑Arch validates ED by confirming invariants and mechanism boundaries.  
- ED‑Arch extends ED by revealing new commensurability classes and scaling laws.

---

# 7. ▶️ Quickstart: Reproduce the Canonical Results

```bash
python run_arch_harness.py --suite all
```

This command:

- runs all analytic law‑surface tests  
- runs all engine‑integrated tests  
- runs all Arch‑21 invariants  
- generates all figures  
- writes JSON + TXT reports  
- saves everything into `arch_harness_output/`

---

# 8. Installation & Environment Setup

1. Clone the repository  
2. Open a terminal  
3. Navigate into the repo  
4. Create the ED environment:  
   ```bash
   conda env create -f environment.yml
   ```
5. Activate it:  
   ```bash
   conda activate ed-arch
   ```
6. Run the harness (see Quickstart)

---

# 9. 📚 Reproduce the ED‑Arch Papers

Each law has a folder:

```
Reproduce_This_Paper/
    01_Law_I_Geometry/
    02_Law_II_Timing/
    03_Law_III_Resonance/
    04_Law_IV_Recurrence/
    05_Law_V_Scaling/
    06_Law_Vb_Commensurability/
```

Each contains:

- figures  
- code  
- a short README explaining:
  - what the law says  
  - what the experiment tests  
  - how to run it  
  - expected output  

---

# 10. 🗂️ Repository Structure

```
ED‑Arch/
    src/                     # core engine + law modules
    harness/                 # reproducibility harness
    arch_harness_output/     # generated results
    Reproduce_This_Paper/    # law-by-law reproducibility folders
    docs/                    # ED‑Arch papers
    run_arch_harness.py      # entry point
```

---

# 11. 🧪 What You Get After Running the Harness

- **law_surface_results.json**  
- **decay_window_results.json**  
- **angular_rate_results.json**  
- **invariant_results.json**  
- **arch_harness_report.txt**  
- **canonical figures** (PNG)  
- **mechanism maps**  
- **summary plots**  

This is the complete empirical signature of ED‑Arch‑21.

---

# 12. The ED Ontology (One‑Sentence Summary)

> **The saddle is the geometry; the gradients are the calculus; the boundaries are the topology; the horizons are the dynamics.**

---

# 13. Why This Repo Matters

This is the first time ED has been:

- executable  
- testable  
- reproducible  
- validated  
- architecturally complete  

It is now a **scientific instrument**, not just a set of papers.

