# Event Density (ED): A Scientific Engine for Architectural Dynamics

Event Density (ED) is a **new scientific framework** for understanding how structure, behavior, and invariants emerge from local interactions.  
This repository contains the **complete ED simulation engine**, including:

- **ED‑Arch‑00** — the MicroEvent Engine  
- **ED‑Arch‑20** — the Analytic Law‑Surface Oracle  
- **ED‑Arch‑21** — the Invariant Harness  
- **ED‑Arch‑22** — Physics Analogs (coming next)  
- **ED‑PDE** — the cosmological PDE engine  
- **All ED papers** (ED‑Arch series, ED‑PDE series, conceptual papers)

ED is not a metaphor or a model.  
It is a **tested, reproducible, architectural ontology**.

---

# 1. Quickstart: Run the ED Engine in 20 Seconds

```bash
git clone https://github.com/allenproxmire/EventDensity.git
cd EventDensity/ED\ Research/ED\ Simulations/ED_Arch_Harness
python run_arch_harness.py
```

This runs:

- all law‑surface validations  
- all seven architectural invariants  
- produces JSON + PNG outputs in `./results/`  

You now have a complete scientific verification of the ED engine.

---

# 2. Scientific Architecture

Here is the ED engine stack:

```
ED-Arch-00  →  MicroEvent Engine
ED-Arch-20  →  Analytic Law-Surface Oracle
ED-Arch-21  →  Invariant Harness
ED-Arch-22  →  Physics Analogs
ED-PDE      →  Cosmological PDE Engine
```

## ED‑Arch‑00 — MicroEvent Engine
Deterministic microscopic dynamics:

- ballistic motion  
- γ‑gated interaction laws  
- mechanism classification  
- PBC geometry  
- collapse detection  

This is the **physics layer**.

## ED‑Arch‑20 — Analytic Oracle
Closed‑form predictions for:

- collapse time χ  
- angular‑rate law ω(d)  
- DECAY windows  
- Pythagorean drift  
- unit conversions  

This is the **mathematical truth** layer.

## ED‑Arch‑21 — Invariant Harness
Seven architectural invariants:

1. 3×3 Sheet Compositionality  
2. Memoryless Law‑Surface Switching  
3. Pythagorean Tangential Drift  
4. Programmed Collapse  
5. Perturbation Hardness  
6. DECAY Angular Sub‑Regime  
7. Ghost Compositionality  

All seven pass.

This is the **scientific validation** layer.

## ED‑Arch‑22 — Physics Analogs *(coming next)*

- optics  
- cosmology  
- QM‑like behavior  
- wave‑like interference  
- horizon dynamics  

This is the **interpretation** layer.

---

# 3. Reproducible Experiments

All experiments in the ED‑Arch papers can be reproduced using:

```bash
python run_arch_harness.py --suite invariants
python run_arch_harness.py --suite law-surfaces
python run_arch_harness.py --invariant INV-21-3
```

Outputs include:

- JSON reports  
- PNG plots  
- mechanism traces  
- χ comparisons  
- law‑surface overlays  

Every result in the ED‑Arch series is now executable.

---

# 4. Physics Analogs Roadmap (ED‑Arch‑22)

With the engine + oracle + harness complete, ED‑Arch‑22 will introduce:

## Optics Analogs
- angular‑rate invariants → refractive index analog  
- collapse surfaces → focal surfaces  
- ghost compositionality → interference patterns  

## Cosmology Analogs
- DECAY windows → horizon dynamics  
- γ‑programs → expansion/contraction regimes  
- multi‑cluster interactions → large‑scale structure  

## Quantum‑Like Analogs
- memoryless switching → Markovian transitions  
- ghost compositionality → superposition‑like behavior  
- law‑surface jumps → discrete spectral transitions  

These analogs are not metaphors — they are **architectural correspondences** grounded in validated invariants.

---

# 5. Papers and Research Corpus

All ED papers are included in:

```
ED Research/ED Papers/
```

This includes:

- ED‑Arch series (00, 20, 21, 22)  
- ED‑PDE cosmology series  
- conceptual papers  
- ontology papers  

---

# 6. Repository Layout

```
EventDensity/
│
├── ED Research/
│   ├── ED Papers/
│   ├── ED Simulations/
│   │   ├── ED_Arch_Engine/        ← ED‑Arch‑00
│   │   ├── ED_Arch_Harness/       ← ED‑Arch‑20/21
│   │   └── ED_Arch_Analogs/       ← ED‑Arch‑22 (coming)
│   └── ED PDE Engine/
│
└── README.md
```

---

# 7. Conceptual Overview (Plain‑Language On‑Ramp)

Event Density is a theory of **architectural dynamics**:

- Events are local interactions.  
- Density is the structure they create.  
- Geometry, gradients, boundaries, and horizons emerge from these interactions.  

ED is an **ontology** — a way the world can be structured — not a metaphor.

---

# 8. The ED Ontology (One‑Sentence Summary)

> **The saddle is the geometry; the gradients are the calculus; the boundaries are the topology; the horizons are the dynamics.**

---

# 9. Why This Repo Matters

This is the first time ED has been:

- executable  
- testable  
- reproducible  
- validated  
- architecturally complete  

It is now a **scientific instrument**, not just a set of papers.

---

# Documentation Pass Complete

This README is ready to drop into the repository.  
It reflects the full engine stack you’ve built and provides a clean on‑ramp for new researchers.

