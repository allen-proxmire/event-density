# Research Archive

This directory contains the complete research history of the Event Density
framework, from foundational papers through simulation development to the
multi-dimensional extension programme.

## Relationship to ED-SIM-02

ED-SIM-02 (the `edsim/` package at the repository root) is the
second-generation simulation platform that implements the architecture
defined in this research. Specifically:

- **ED-Phys-01 through ED-Phys-40** define the canonical PDE, constitutive
  functions, nine architectural laws, dimensional scaling, and cross-framework
  comparisons that ED-SIM-02 implements and validates.

- **ED-SIM-01** (in `ED Simulation/`) is the first-generation simulation
  platform that ED-SIM-02 supersedes.

- **ED Validation/** contains reproducibility outputs from the v1 pipeline.

The research archive is preserved for reference and historical completeness.
ED-SIM-02 is self-contained and does not import from these directories.

## Contents

| Folder | Description |
|--------|-------------|
| `ED Architecture/` | Structural anatomy: 12 layered documents describing the ED ontological architecture |
| `ED PAPERS/` | Core papers, appendices, and monograph defining the ED framework |
| `ED Physics/` | ED-Phys series (papers 01-40): PDE analysis, multi-dimensional extension, cross-framework comparison, architectural synthesis |
| `ED Interpretations/` | 31 domain interpretations + 12 foundational essays applying ED across physics |
| `ED Experiments/` | Experiment programme, SPARC test design, open notebooks |
| `ED Simulation/` | ED-SIM v1: original numerical pipeline, reproducibility scripts, ED-SIM-02 architecture document |
| `ED Validation/` | P1-P7 reproducible test outputs from the v1 validation suite |
| `CRITICAL ASSESSMENT_27MAR26.pdf` | External critical assessment of the ED framework |

## How to Navigate

**Start here** if you want to understand the physics:
- `ED PAPERS/` for the foundational theory
- `ED Physics/ED-Phys-40_Synthesis/` for the final architectural statement

**Start here** if you want to understand the simulation history:
- `ED Simulation/ED-SIM-02/ED-SIM-02_Architecture.md` for the v2 design document
- `ED Simulation/edsim_core.py` for the v1 solver

**Start here** if you want to see the multi-dimensional results:
- `ED Physics/ED-Phys-35_MultiDim/` for 2D/3D implementation and findings
- `ED Physics/ED-Phys-39_HigherDim/` for the 4D extension

## Status

All materials in this archive are **historical and read-only**. Active
development happens in the `edsim/` package. The research archive is not
modified during normal development or CI runs.
