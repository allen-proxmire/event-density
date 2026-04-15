# theory/

**The home of the Event Density PDE.** This directory contains the canonical theoretical material of the framework: the axiomatic derivation, the unique PDE it selects, the cross-regime dimensional atlas, the rigorous numerical atlas, and all supporting appendices.

If you want to know what ED *is* — as opposed to what it predicts in any particular regime — start here.

---

## The PDE in one expression

$$
\partial_t \rho \;=\; D \cdot \bigl[\, M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho)\, \bigr] \;+\; H \cdot v
$$
$$
\dot v \;=\; \tfrac{1}{\tau}\,\bigl(\bar F(\rho) - \zeta v\bigr)
$$

with $M(\rho) = M_0(\rho_{\max}-\rho)^\beta$ and $P(\rho) = P_0(\rho-\rho^\ast)$.

Four primitives, seven structural constraints, three constitutive channels. Full statement and derivation in **[PDE.md](PDE.md)**.

---

## How the three flagship results map onto the PDE

| Channel exercised | Empirical regime | Prediction | Result | Paper |
|---|---|---|---|---|
| **Mobility** $M(\rho) = M_0(\rho_{\max}-\rho)^\beta$ | Concentrated soft matter | $D(c) = D_0(1-c/c_{\max})^\beta$ | UDM, 10 materials, $R^2 > 0.986$ | [`papers/UDM/`](../papers/UDM/) |
| **Penalty** + dynamical wake | Galaxy cluster mergers | $\ell = D_T / v_{\rm current}$ | Galaxy-15, 7 clusters + Finner+25 median | [`papers/galaxy-15/`](../papers/galaxy-15/) |
| **All three channels, all five regimes** | Quantum → cosmological | $D_{\rm phys}\,T_0/L_0^2 = 0.3$ | PDE Atlas, 9 architectural laws verified in $d = 1$–$4$ | [`Dimensional_Atlas/`](Dimensional_Atlas/) + [`Numerical_Atlas/`](Numerical_Atlas/) |

The unifier is the diffusivity $D$. Set independently from the Mistele weak-lensing extent at galactic scales (giving $D_T = 2.1 \times 10^{27}\,\mathrm{m^2/s}$), the *same* constant — through the dimensional bridges of the Atlas — becomes the $D_0$ of the soft-matter mobility law in the condensed-matter regime. No fitting between domains. See [`../RESULTS.md`](../RESULTS.md) for the full unification narrative.

---

## What is in this directory

```
theory/
├── README.md                       ← you are here (high-level overview)
├── PDE.md                          ← the canonical PDE statement (one page)
│
├── Dimensional_Atlas/              ← cross-regime dimensional mappings
│   ├── ED-Dimensional-Master_The_Unified_Atlas.md     (synthesis paper)
│   ├── ED-Dimensional-01_Quantum_Regime.md
│   ├── ED-Dimensional-02_Planck_Regime.md
│   ├── ED-Dimensional-03_Condensed_Matter_Regime.md
│   ├── ED-Dimensional-04_Galactic_Regime.md
│   └── ED-Dimensional-05_Cosmological_Regime.md
│
├── Numerical_Atlas/                ← computational realisation of the canonical PDE
│   └── numerical_atlas.md          (well-posedness, spectra, Lyapunov, bifurcations)
│
└── Foundations/                    ← axiomatic source material
    ├── ED_Foundational_Paper.md    (the Foundational Paper, source markdown)
    ├── Appendix_G_3D_Analogues.md  (3D extension of the structural analogues)
    ├── Event_Density_as_a_Physical_Ontology.md  (ontology paper)
    └── Appendices/                 (formal supporting appendices)
        ├── appendix_A_Proofs of Independence Results.md
        ├── appendix_B_Proofs of Sufficiency Results.md
        ├── appendix_C_PDE Analysis.md
        ├── appendix_D_Universality Class.md
        ├── appendix_E_Numerical Methods.md
        ├── appendix_F_Extended Figures and Data.md
        ├── appendix G_Glossary of Symbols.md
        ├── appendix_H_Reproducibility Statement.md
        ├── glossary.md
        └── references.md
```

---

## Reading order

For a researcher new to ED who wants a complete theoretical understanding:

1. **[PDE.md](PDE.md)** — start here. The canonical PDE on one page.
2. **[Foundations/ED_Foundational_Paper.md](Foundations/ED_Foundational_Paper.md)** — the axiomatic derivation, the constitutive structure, the six structural analogues.
3. **[Foundations/Event_Density_as_a_Physical_Ontology.md](Foundations/Event_Density_as_a_Physical_Ontology.md)** — the philosophical / ontological framing (becoming as primitive).
4. **[Foundations/Appendices/appendix_C_PDE Analysis.md](Foundations/Appendices/appendix_C_PDE%20Analysis.md)** — rigorous PDE analysis: well-posedness, spectral structure, three-stage convergence theorem.
5. **[Foundations/Appendices/appendix_D_Universality Class.md](Foundations/Appendices/appendix_D_Universality%20Class.md)** — the universality framework and the uniqueness theorem (Theorem D.19).
6. **[Dimensional_Atlas/ED-Dimensional-Master_The_Unified_Atlas.md](Dimensional_Atlas/ED-Dimensional-Master_The_Unified_Atlas.md)** — synthesis of the five regime mappings, the universal nondimensional invariant.
7. Individual regime mappings as needed: [Quantum](Dimensional_Atlas/ED-Dimensional-01_Quantum_Regime.md), [Planck](Dimensional_Atlas/ED-Dimensional-02_Planck_Regime.md), [Condensed Matter](Dimensional_Atlas/ED-Dimensional-03_Condensed_Matter_Regime.md), [Galactic](Dimensional_Atlas/ED-Dimensional-04_Galactic_Regime.md), [Cosmological](Dimensional_Atlas/ED-Dimensional-05_Cosmological_Regime.md).
8. **[Numerical_Atlas/numerical_atlas.md](Numerical_Atlas/numerical_atlas.md)** — computational atlas demonstrating each theorem of Appendix C numerically across the $(D, \zeta, \tau)$ parameter space.

---

## Cross-references

- **Empirical results that test this theory:** [../RESULTS.md](../RESULTS.md), [../papers/UDM/](../papers/UDM/), [../papers/galaxy-15/](../papers/galaxy-15/).
- **Runnable demonstration of the three channels:** [../analysis/notebooks/02_three_channels.ipynb](../analysis/notebooks/02_three_channels.ipynb).
- **Simulation engine that integrates this PDE:** [../edsim/](../edsim/) (Python package, CLI, 112-test suite, 9-phase certify pipeline).
- **Falsifiable prediction not yet tested:** [../ED_FrontDoor/ED_Falsifiable_Prediction.md](../ED_FrontDoor/ED_Falsifiable_Prediction.md).

---

## Status of the theory

**What is mathematically established.** The uniqueness theorem (Theorem D.19) selects the canonical PDE from C1–C7 with no free choices. Well-posedness, spectral structure, Lyapunov dissipation, and the three-stage convergence theorem are proved in Appendix C. The five-regime dimensional reduction is an explicit construction.

**What is empirically established.** The mobility channel (UDM) has been tested against 10 materials in the soft-matter regime, all $R^2 > 0.986$. The penalty channel (Galaxy-15) has been tested against 7 well-measured clusters and the Finner+25 aggregate of 58 subclusters, all consistent with the corrected formula $\ell = D_T / v_{\rm current}$. The three architectural signatures (velocity scaling, deceleration scaling, scale dependence) are confirmed in the data.

**What remains open.** No experimental test of the quantum regime mapping has been performed. No experimental test of the Planck regime mapping has been performed. The cosmological regime is provisionally falsified as a *standalone* model (the monostable penalty cannot generate cosmic structure growth on its own, though the participation channel may; this is unresolved). The participation channel's identification across regimes is a candidate, not a confirmed fact. ED does not derive general relativity, quantum mechanics, or the Standard Model.

These limits are documented in the foundational papers and tested in the simulation engine.
