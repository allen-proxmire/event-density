# theory/

**The home of the canonical Event Density PDE statement.** This directory is intentionally small: it holds the authoritative PDE document, the architectural-canon reference, and a navigation README. Long-form theoretical *papers* (the Foundational Paper, the Ontology paper, the Dimensional Atlas, the Numerical Atlas) live in [`/papers/`](../papers/) where every paper has its own canonical folder.

| File | Layer | When to read |
|---|---|---|
| [`PDE.md`](PDE.md) | Concrete PDE with specific functional forms | Compact one-page statement of the equation this repo instantiates and tests. |
| [`Architectural_Canon.md`](Architectural_Canon.md) | Structural axioms: 7 principles P1–P7 + 4 pre-PDE axioms | Understanding what defines ED as a *class* of PDEs, not a specific equation. |
| [`../docs/ED-Orientation.md`](../docs/ED-Orientation.md) | Complete orientation across the 20+ paper ED series | First read for a new session; covers the full paper series including PhilArchive papers not in this repo. |

Use `PDE.md` when you want a compact statement of the equation and its structural setup. Use `Architectural_Canon.md` when you need the architectural principles rather than the concrete equation. Use `/papers/` for long-form derivations, proofs, regime mappings, and computational atlases. Use `ED-Orientation.md` to orient across the wider ED program — including the ED-XX environment-sourcing revision (April 2026), the ED-05 pre-PDE axioms, the ED-09.5 sharp-quantum-classical-transition prediction, and the ED-13 master empirical synthesis.

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

**What is empirically established.** The mobility channel (UDM) has been tested against 10 materials in the soft-matter regime, all $R^2 > 0.986$. The penalty channel (Galaxy-15) has been tested against 7 well-measured clusters and the Finner+25 aggregate of 58 subclusters, all consistent with the corrected formula $\ell = D_T / v_{\rm current}$. The three architectural signatures (velocity scaling, deceleration scaling, scale dependence) are confirmed in the data. See ED-13 (*Event Density as a Physical Ontology*, March 2026) for the master cross-regime empirical synthesis: condensed-matter diffusivity fit (3 chemical systems, exponent ~2), naturally-cored dwarf halos, flat weak-lensing velocities to 1 Mpc, BTFR with the observed 1/4 exponent, plus two sharp discriminating predictions (activity-dependent WL velocities and merger-lag lensing).

**Recent revision (April 2026).** ED-XX *Environment Sourcing of Temporal Tension* overturned the earlier galaxy-sourced hypothesis at galactic scale. The 3D Green's function `T(r) ∝ (1/r)e^(−r/ℓ_T)` has a geometric dilution term that no compact galactic source can overcome. Flat weak-lensing fields require megaparsec-scale sources — i.e., the cosmic web. Galaxies set the amplitude; groups, filaments, and the local cosmic web set the spatial extent. Cluster-scale results (Galaxy-15) are unaffected because clusters are themselves the extended source. See [`../docs/ED-Orientation.md`](../docs/ED-Orientation.md) §6.

**What remains open.** No experimental test of the quantum regime mapping has been performed. No experimental test of the Planck regime mapping has been performed. The cosmological regime is provisionally falsified as a *standalone* model (the monostable penalty cannot generate cosmic structure growth on its own, though the participation channel may; this is unresolved). The participation channel's identification across regimes is a candidate, not a confirmed fact. ED does not derive general relativity, quantum mechanics, or the Standard Model.

**Candidate testable predictions not yet tested.** Beyond the empirical tests currently in flight, two sharp ED-specific predictions are documented in the wider paper series but have no assigned test program in the repo:

- **ED-09.5 sharp quantum-classical transition** (*Event Density and the Quantum–Classical Boundary*, Feb 2026): ED predicts a *structural* boundary at the quantum-classical transition distinct from smooth environmental decoherence — a sharp collapse to a single participation channel when internal complexity outpaces event-production capacity. Standard decoherence theory never predicts this sharp transition. Candidate experimental regimes: macroscopic quantum coherence (cavity QED with increasing atom number; optomechanical systems near the quantum-classical boundary; large-mass superposition experiments).
- **ED-13 activity-dependent weak-lensing velocities**: galaxies with more collective activity should show higher asymptotic `V_∞` at fixed baryonic mass. After ED-XX, the relevant variable is environmental activity (group/filament scale), not individual-galaxy SFR. BIG-SPARC with group/filament cross-match is the definitive test.

These limits are documented in the foundational papers and tested in the simulation engine.
