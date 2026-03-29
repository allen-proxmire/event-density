"""
edsim.manuscript.sections_phys_master — Manuscript section for ED-PHYS-10.
"""

from __future__ import annotations


def section_phys_master() -> str:
    """Return a manuscript-ready section synthesising the ED-PHYS programme."""
    from ..phys.master_interpretation import build_master_interpretation

    mi = build_master_interpretation()

    findings_rows = ""
    for f in mi.findings:
        findings_rows += f"\n| {f.number} | {f.name} | {f.result} | {f.accuracy} |"

    relatives_rows = ""
    for name, reason in mi.universality.nearest_relatives:
        relatives_rows += f"\n| {name} | {reason} |"

    not_rows = ""
    for domain in mi.is_not:
        not_rows += f"\n| {domain.title()} | See PHYS programme for details |"

    analogue_rows = ""
    for a in mi.analogues:
        analogue_rows += f"\n| {a.target} | {a.mechanism} | {a.quality} |"

    text = f"""\
## ED-PHYS-10: Master Interpretation and Synthesis

### The ED-PHYS Programme

Nine experiments (PHYS-01 through PHYS-09) systematically decompose the
canonical ED PDE into its physical channels, map its parameter space, and
identify its structural analogies:

| # | Experiment | Result | Accuracy |
|---|-----------|--------|----------|{findings_rows}

### Mathematical Identity

{mi.mathematical_identity}

### Physical Identity

{mi.physical_identity}

### Universality Class

**{mi.universality.name}**

Nearest relatives:

| PDE | Relationship |
|-----|-------------|{relatives_rows}

### What ED Is

{mi.is_what}

### What ED Is Not

| Domain | Status |
|--------|--------|{not_rows}

### Structural Analogues

| Target | Mechanism | Quality |
|--------|-----------|---------|{analogue_rows}

All analogies are mathematical (shared PDE structure), not physical claims.

### Closing Statement

The Event Density PDE is the simplest PDE that simultaneously exhibits
degenerate mobility, monostable penalty, five Lyapunov functionals,
telegraph-like oscillation, and transient morphological structure.  Its
structure has been quantitatively characterised across nine experiments
spanning diffusion, waves, reactions, patterns, quantum-like signatures,
phase diagrams, energy structure, physical interpretations, and
cosmological analogues.  The framework is complete, reproducible, and
falsifiable.
"""
    return text
