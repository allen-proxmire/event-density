# theory/

**The home of the canonical Event Density PDE statement.** This directory is intentionally small: it holds the one-page authoritative PDE document and a navigation README. Long-form theoretical *papers* (the Foundational Paper, the Ontology paper, the Dimensional Atlas, the Numerical Atlas) live in [`/papers/`](../papers/) where every paper has its own canonical folder.

Use `theory/PDE.md` when you want a compact, complete statement of the equation and its structural setup. Use `/papers/` when you want the long-form derivations, proofs, regime mappings, and computational atlases that *establish* what `theory/PDE.md` summarizes.

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
| **Mobility** $M(\rho) = M_0(\rho_{\max}-\rho)^\beta$ | Concentrated soft matter | $D(c) = D_0(1-c/c_{\max})^\beta$ | UDM, 10 materials, $R^2 > 0.986$ | [`/papers/Universal_Mobility_Law/`](../papers/Universal_Mobility_Law/) |
| **Penalty** + dynamical wake | Galaxy cluster mergers | $\ell = D_T / v_{\rm current}$ | Galaxy-15, 7 clusters + Finner+25 median | [`/papers/Cluster_Merger_Lag_Evidence/`](../papers/Cluster_Merger_Lag_Evidence/) |
| **All three channels, all five regimes** | Quantum → cosmological | $D_{\rm phys}\,T_0/L_0^2 = 0.3$ | PDE Atlas, 9 architectural laws verified in $d = 1$–$4$ | [`/papers/Dimensional_Atlas/`](../papers/Dimensional_Atlas/) + [`/papers/Numerical_Atlas/`](../papers/Numerical_Atlas/) |

The unifier is the diffusivity $D$. Set independently from the Mistele weak-lensing extent at galactic scales (giving $D_T = 2.1 \times 10^{27}\,\mathrm{m^2/s}$), the *same* constant — through the dimensional bridges of the Atlas — becomes the $D_0$ of the soft-matter mobility law in the condensed-matter regime. No fitting between domains. See [`/RESULTS.md`](../RESULTS.md) for the full unification narrative.

---

## What is in this directory

```
theory/
├── README.md     ← you are here (high-level overview, links to papers/)
└── PDE.md        ← the canonical PDE statement (one page)
```

That is the entire `theory/` directory. Everything else now lives in [`/papers/`](../papers/) under descriptive names:

```
papers/
├── Foundations_of_Event_Density/        ← axiomatic derivation + 10 formal appendices
├── Event_Density_Ontology_and_Axioms/   ← philosophical / ontological framing
├── Universal_Mobility_Law/              ← UDM (mobility channel, soft matter)
├── Cluster_Merger_Lag_Evidence/         ← Galaxy-15 (penalty channel, cluster mergers)
├── Dimensional_Atlas/                   ← 5-regime synthesis + per-regime documents
└── Numerical_Atlas/                     ← computational atlas
```

---

## Reading order

For a researcher new to ED who wants a complete theoretical understanding:

1. **[PDE.md](PDE.md)** — start here. The canonical PDE on one page.
2. **[`/papers/Foundations_of_Event_Density/paper.md`](../papers/Foundations_of_Event_Density/paper.md)** — the axiomatic derivation, the constitutive structure, the six structural analogues.
3. **[`/papers/Event_Density_Ontology_and_Axioms/paper.md`](../papers/Event_Density_Ontology_and_Axioms/paper.md)** — the philosophical / ontological framing (becoming as primitive).
4. **[`/papers/Foundations_of_Event_Density/Appendices/appendix_C_PDE Analysis.md`](../papers/Foundations_of_Event_Density/Appendices/appendix_C_PDE%20Analysis.md)** — rigorous PDE analysis: well-posedness, spectral structure, three-stage convergence theorem.
5. **[`/papers/Foundations_of_Event_Density/Appendices/appendix_D_Universality Class.md`](../papers/Foundations_of_Event_Density/Appendices/appendix_D_Universality%20Class.md)** — the universality framework and the uniqueness theorem (Theorem D.19).
6. **[`/papers/Dimensional_Atlas/paper.md`](../papers/Dimensional_Atlas/paper.md)** — synthesis of the five regime mappings, the universal nondimensional invariant.
7. Individual regime mappings as needed: [Quantum](../papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md), [Planck](../papers/Dimensional_Atlas/regimes/ED-Dimensional-02_Planck_Regime.md), [Condensed Matter](../papers/Dimensional_Atlas/regimes/ED-Dimensional-03_Condensed_Matter_Regime.md), [Galactic](../papers/Dimensional_Atlas/regimes/ED-Dimensional-04_Galactic_Regime.md), [Cosmological](../papers/Dimensional_Atlas/regimes/ED-Dimensional-05_Cosmological_Regime.md).
8. **[`/papers/Numerical_Atlas/paper.md`](../papers/Numerical_Atlas/paper.md)** — computational atlas demonstrating each theorem of Appendix C numerically across the $(D, \zeta, \tau)$ parameter space.

---

## Cross-references

- **Empirical results that test this theory:** [`/RESULTS.md`](../RESULTS.md), [`/papers/Universal_Mobility_Law/`](../papers/Universal_Mobility_Law/), [`/papers/Cluster_Merger_Lag_Evidence/`](../papers/Cluster_Merger_Lag_Evidence/).
- **Runnable demonstration of the three channels:** [`/analysis/notebooks/02_three_channels.ipynb`](../analysis/notebooks/02_three_channels.ipynb).
- **Simulation engine that integrates this PDE:** [`/edsim/`](../edsim/) (Python package, CLI, 112-test suite, 9-phase certify pipeline).
- **Falsifiable prediction not yet tested:** [`/outreach/ED_Falsifiable_Prediction.md`](../outreach/ED_Falsifiable_Prediction.md).

---

## Status of the theory

**What is mathematically established.** The uniqueness theorem (Theorem D.19) selects the canonical PDE from C1–C7 with no free choices. Well-posedness, spectral structure, Lyapunov dissipation, and the three-stage convergence theorem are proved in Appendix C. The five-regime dimensional reduction is an explicit construction.

**What is empirically established.** The mobility channel (UDM) has been tested against 10 materials in the soft-matter regime, all $R^2 > 0.986$. The penalty channel (Galaxy-15) has been tested against 7 well-measured clusters and the Finner+25 aggregate of 58 subclusters, all consistent with the corrected formula $\ell = D_T / v_{\rm current}$. The three architectural signatures (velocity scaling, deceleration scaling, scale dependence) are confirmed in the data.

**What remains open.** No experimental test of the quantum regime mapping has been performed. No experimental test of the Planck regime mapping has been performed. The cosmological regime is provisionally falsified as a *standalone* model (the monostable penalty cannot generate cosmic structure growth on its own, though the participation channel may; this is unresolved). The participation channel's identification across regimes is a candidate, not a confirmed fact. ED does not derive general relativity, quantum mechanics, or the Standard Model.

These limits are documented in the foundational papers and tested in the simulation engine.
