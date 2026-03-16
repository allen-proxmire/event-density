# Event Density Ontology

## Overview

Event Density (ED) is a foundational framework for physics built on a minimal ontology of **events**, **becoming**, and **event density**.  
It does **not** assume spacetime, fields, curvature, or geometric structure.  
Instead, ED begins with the idea that the universe is a finite configuration of events whose density of becoming evolves according to a single **compositional rule**.

From this rule alone, ED derives large‑scale cosmological behavior — early exponential smoothing, residual gradients, structure formation, expansion, and late‑time flattening — without invoking geometry or external dynamical laws.

ED is not a simulation or a toy model.  
It is a **candidate ontology for this universe**.

This repository contains the ED ontology, the compositional rule, and the cosmological consequences derived from it.

---

## Primitives

ED is defined by three irreducible primitives:

### 1. **Events**  
The fundamental units of becoming.  
Events are not embedded in spacetime; spacetime is an emergent description of relations among events.

### 2. **Event Density (p)**  
A measure of “how much becoming” is present in a finite configuration.  
High ED corresponds to rich, active regions; low ED corresponds to thin, quiescent ones.

### 3. **Finite Configurations**  
ED is always defined on finite sets of events.  
There is no continuum, no background manifold, and no geometric structure assumed.

Everything else — gradients, boundaries, horizons, structure, expansion — emerges from how ED behaves across these finite configurations.

---

## The Compositional Rule

The core of ED is a universal rule that determines the ED of a union of configurations:

p(A ∪ B)
= p(A) + p(B)
− α ∫_{A∩B} f(p) du
− β ∫_{A∪B} g(|∇p|) du
− γ ∫_{∂(A∪B)} h(|∇p|) dS.

This rule contains three competing contributions:

### **Relational Penalty**  
Concave in p.  
Suppresses overlap of high‑ED regions.  
Drives competition and structure formation.

### **Gradient Penalty**  
Quadratic in |∇p|.  
Penalizes inhomogeneity.  
Drives exponential smoothing (ED‑inflation).

### **Boundary Term**  
Saturating in |∇p|.  
Dominates in extreme regimes.  
Generates horizon‑like behavior and late‑time flattening.

These three terms — competition, smoothing, and boundary dominance — are the engines of ED cosmology.

---

## Cosmology from ED

When applied to the universe as a whole, the compositional rule produces a coherent cosmological history:

### **Early Universe: Exponential Smoothing**  
The gradient penalty dominates, forcing rapid decay of gradients.  
This yields an inflation‑like phase without geometry or fields.

### **Residual Gradients: Seeds of Structure**  
Smoothing weakens as gradients shrink.  
Small variations survive and become the seeds of structure.

### **Structure Formation**  
The concave relational penalty amplifies residual gradients and stabilizes high‑ED pockets — the ED analogues of galaxies, stars, and clusters.

### **Expansion via Thinning**  
ED flows outward from high‑ED pockets, reducing the global average ED density.  
The coarse‑grained homogeneity scale grows.  
This is the ED analogue of cosmic expansion.

### **Late‑Time Flattening and Horizons**  
As gradients vanish, the boundary term dominates.  
The universe approaches a thin, nearly uniform state with horizon‑like behavior.

All of this arises from the compositional rule alone — no metric, no curvature, no fields.

---

## Repository Structure

ED/
│
├── ED-Foundations/
│   ├── ED_Foundations.pdf
│   ├── ED_Interpretations.pdf
│   └── ontology_notes/
│
├── ED-Compositional-Rule/
│   ├── ED_Compositional_Rule.pdf
│   ├── Cosmology_from_ED_Compositional_Rule.pdf
│   └── derivations/
│
├── ED-Cosmology/
│   ├── coarse_graining/
│   ├── inflation/
│   ├── structure_formation/
│   ├── expansion/
│   └── late_time_flattening/
│
└── README.md

---

## What ED Is Not

- Not a simulation  
- Not a discretization of GR or QM  
- Not a cellular automaton  
- Not a toy model  
- Not a geometric theory  

ED is a **non‑geometric ontology** that aims to explain why the universe has the laws it does.

---

## What ED Aims to Explain

- Why laws exist  
- Why they are stable  
- Why they are finite  
- Why structure forms  
- Why the universe smooths  
- Why expansion occurs  
- Why horizons appear  
- Why late‑time flattening is universal  

These are testable consequences of the compositional rule.

---

## Status

ED is an active research program.  
The ontology is defined.  
The compositional rule is specified.  
The cosmological consequences are derived.  
Mathematical formalization and empirical mapping are ongoing.
