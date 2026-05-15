# Walkthroughs Deferred — Future Candidates

**Date last updated:** 2026-05-10. (After Berry / Bloch / Photonic-Chern / Rate-of-Becoming additions to the walkthrough series.)

These are walkthrough candidates identified during audits. Each has closed math content somewhere in the framework's repository and would walk cleanly. None are blocking; flagged here so they don't get lost.

## Closed since last update

- ~~**The 0.6 problem resolution**~~ — closed by `from_primitives_to_the_06_problem.md` (2026-05-09).
- ~~**Berry phase**~~ — closed by `from_primitives_to_berry_phase.md` (2026-05-10).
- ~~**Substrate-level Bloch theorem**~~ — closed by `from_primitives_to_bloch_theorem.md` (2026-05-10).
- ~~**Substrate-level Chern-quantization**~~ — closed by Appendix A of `from_primitives_to_photonic_chern_channels.md` (2026-05-10).
- ~~**Photonic Chern + quantized Hall drift (ED-I-28)**~~ — closed by `from_primitives_to_photonic_chern_channels.md` (2026-05-10).
- ~~**Hau-Katori-Ye cluster (slow / stopped light + optical clocks + clock networks)**~~ — closed by `from_primitives_to_rate_of_becoming.md` (2026-05-10).
- ~~**Substrate-Unruh**~~ — closed by `from_primitives_to_substrate_unruh.md` (2026-05-09).
- ~~**Quantum information landmark results (Deutsch / DJ / BB84 / teleportation / Shor)**~~ — closed by `from_primitives_to_quantum_information.md` (2026-05-09).

## Currently deferred

### From original 2026-05 audit

1. **Wu-Yang non-Abelian phase factor.** Downstream of T17 (gauge fields) and the AB phase walkthrough. Path-ordered exponential of the non-Abelian connection around a closed loop. Pair candidate with Berry-phase walkthrough (U(1) → U(N) for degenerate bands). ~400 lines.

2. **Bandwidth-budget mechanism overview (cross-arc unification).** BH-4 (entanglement-straddling) + E-4 (monogamy) + Q-COMPUTE Class C (correlation-budget plateau) + BH-5 (area-law) as projections of one substrate mechanism. Weaves together what existing walkthroughs each touch separately. ~500 lines.

3. **Higgs mechanism from rule-type symmetry breaking.** Source: `arcs/arc-Q/higgs_mechanism_scoping.md` — needs verification that closure is at FORCED level, not scoping level. If closed, would extend the gauge-fields and mass walkthroughs.

4. **Cluster decomposition / micro-causality.** Substrate-level account of why field operators at spacelike-separated points commute. Related to but distinct from the arrow-of-time walkthrough. Would extend the Yang-Mills and gauge-fields walkthroughs.

### Newly identified (2026-05-10) follow-ons from QI / Berry / Bloch / Photonic-Chern / Rate-of-Becoming series

5. **Tight QFT amplitude bound for $r \nmid 2^n$ general case.** Appendix-grade tightening of QI walkthrough §8.4. Standard discrete Fourier analysis; calculation not new substrate content.

6. **Stabilizer codes / fault-tolerance walkthrough.** Distributed alignment + syndrome-as-non-disturbing-rewrite + threshold-as-multiplicity-cap-tied. Cross-link with Q-COMPUTE Class C correlation-budget plateau.

7. **Grover search.** Sixth QI move (amplitude amplification); $O(\sqrt N)$ unstructured search. Derivable now.

8. **BosonSampling.** High-$M$-channel + indistinguishable-particle reading. Derivable now (uses spin-statistics walkthrough indistinguishability).

9. **IQP / random-circuit sampling.** Commuting-rule generators; thinner new substrate content; partial-grade walkthrough.

10. **Quantum-coherence-enhanced clocks.** Heisenberg-limited $\sim 1/N$ precision via entangled atoms. Substrate-level reading via Arc E unresolved-rule machinery.

11. **Frequency-comb walkthrough.** Femtosecond combs link optical-frequency-clock signals to RF/microwave outputs. Substrate-level account of mode-locked-laser comb structure.

12. **Tests of fundamental-constant drift.** Differential clock comparisons searching for $\dot\alpha_\text{em}$, $\dot{(m_p/m_e)}$. Substrate-level account of why fundamental constants are constants (or could drift). Foundational.

13. **Lorentz/CPT-violation tests at clock precision.** Substrate-level account of Lorentz invariance and potential violations, given $10^{-19}$ clock-comparison constraints. Foundational.

### Photonics direction (ED-I-12 territory — needs three precursors before walkthrough is achievable at QI-grade depth)

14. **Effective-medium / homogenization walkthrough.** First precursor for Yablonovitch / Pendry / Capasso photonics walkthrough. Substrate-level analog of standard homogenization theory — derive how subwavelength substrate-rule-type substructure coarse-grains to macroscopic effective $\varepsilon(\mathbf{r}), \mu(\mathbf{r})$. Arc-grade (5–7 memos).

15. **Transformation-optics walkthrough.** Second precursor for ED-I-12. Derive how substrate-gradient deformations correspond to effective-medium coordinate transformations. Arc-grade.

16. **Metasurface boundary-condition walkthrough.** Third precursor for ED-I-12. Derive generalized Snell's law from substrate primitives + interface conditions on rule-type structure. Short walkthrough.

17. **Yablonovitch / Pendry / Capasso effective-medium photonics walkthrough.** ED-I-12 mathed-out. Composes precursors 14–16. Achievable after precursors close.

### Topological / non-Abelian extensions

18. **Non-Hermitian topology.** Driven-dissipative systems with PT-symmetric or genuinely non-Hermitian Hamiltonians have their own topological classification (exceptional points, non-Hermitian skin effect). Substrate-level account.

19. **Floquet topological insulators.** Periodically-driven systems with topological invariants of the time-evolution operator. Distinct from static Haldane construction.

20. **Bulk-boundary correspondence.** Chern number of bulk band predicts edge-state count. Substrate-level account.

21. **Many-body topology.** Fractional quantum Hall, fractional Chern insulators. Requires interaction effects beyond single-channel band-structure framework. Substantially more involved.

### Other candidates

22. **Aharonov-Anandan (non-cyclic) generalization of Berry phase.** Removes cyclic-evolution requirement; produces phase associated with any path in projective Hilbert space. Substrate-level reading parallel to cyclic case.

23. **Sjöqvist-Pati geometric phase for mixed states.** Generalizes Berry phase to Lindblad-evolved density operators. Substrate-level reading via Lindblad walkthrough.

24. **Strong-field clock corrections.** Clocks near black holes / neutron stars / extreme gravitational fields. Composes with Arc BH and Arc ED-10.

## Skipped candidates (covered elsewhere)

- **Why $D = 3+1$ dimensions.** Covered as consequences across `from_primitives_to_spin_statistics.md`, `from_primitives_to_dirac_equation_and_g2.md`, and `from_primitives_to_navier_stokes_smoothness.md`. Standalone derivation would be smallest-payload candidate.

## Decision criteria for picking one

When returning to this list, sort by:

1. **Distinctive math content** — Higgs mechanism (if closed at FORCED level) and Lorentz/CPT tests have the most ED-distinctive math.
2. **Cross-platform unification value** — bandwidth-budget overview would strengthen cross-domain mechanism identity surfaced in BH / E / Q-COMPUTE.
3. **Pairing with existing walkthroughs** — Wu-Yang pairs with Berry-phase + T17 + AB; quantum-coherence-enhanced clocks pairs with Rate-of-Becoming + Arc E.
4. **Nobel-relevance** — see Nobel-relevance routing table in `project_walkthrough_series_expansion.md` for current status.
5. **Precursor dependencies** — for ED-I-12 photonics, three precursors (14–16) needed before the target walkthrough (17) is achievable.
