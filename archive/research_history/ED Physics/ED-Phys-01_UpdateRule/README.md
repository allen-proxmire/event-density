# ED-Phys-01: Update Rule

## Purpose

Extract, formalize, and discretize the ED Compositional Rule from its canonical sources (ED-5, ED-12, ED-12.5) into a simulation-ready update rule.

## Contents

- **ED-Phys-01_UpdateRule.md** — Full mathematical formalization: the general compositional rule, all penalty terms, symbolic derivatives, discretized update rule, stability constraints, and pseudocode.

## Relationship to the ED-Phys Pipeline

This is the foundational layer. Every downstream module depends on the update rule defined here:

- **ED-Phys-02 (Simulator)** implements this update rule in code.
- **ED-Phys-03 (Cosmological Timeline)** runs it forward to produce cosmic histories.
- **ED-Phys-04 (Physical Analogues)** maps its outputs to observable physics.
- **ED-Phys-05 (Parameter Sweeps)** explores its parameter space.
- **ED-Phys-06 (Emergent Phenomena)** identifies structures that arise from it.
- **ED-Phys-07 (Analytical Theory)** derives closed-form results from it.
- **ED-Phys-08 (Documentation)** records the full derivation chain.

## Canonical Sources

| Source | Role |
|--------|------|
| ED-5 (Mathematical Formalization) | Ontological primitives, axioms, ED system definition |
| ED-12 (ED Compositional Rule) | General functional rule with three penalty terms |
| ED-12.5 (Cosmology from the Compositional Rule) | Cosmology-specialized penalties and dynamics |
