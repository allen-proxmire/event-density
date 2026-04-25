# Phase-3 Scoping — ED → GR Coupling

**Phase-3 Stage GR.0 — Opening Scoping Memo**
**Status:** Scoping only. Defines the Phase-3 problem (whether ED couples to curvature and gravitational dynamics structurally), enumerates four central questions (Q-GR1 curvature-vacuum coupling, Q-GR2 finite Λ, Q-GR3 dynamical curvature equation, Q-GR4 geodesic worldlines), structural inputs from Phase-2 + Arc N, four constraints (Lorentz covariance, locality, UV-FIN, primitive event-discreteness), and a five-substage roadmap (GR.1 catalogue → GR.2 FORCED → GR.3 REFUTED → GR.4 cosmological implications → GR.5 synthesis). **Honest framing acknowledged up front:** ED's prior kinematic-curvature work [1] closed with an acoustic-metric-only result — no Einstein equations, no Schwarzschild, no dynamical curvature. Phase-3 is the most speculative ED phase to date; the honest expected verdict is *partial admissibility with substantial inheritance*, paralleling Arc M's H1-dominant pattern at the curvature layer rather than the strong-positive Arc Q + Arc N pattern.

---

## 1. Purpose of Phase-3

### 1.1 The ED → GR coupling problem

Phase-1 + Phase-2 (Arc R + Arc M + Arc Q) + Arc N closed the ED quantum sector at primitive level: form-level Phase-2 theorems supply the structural framework for relativistic quantum mechanics, mass content, and quantum field theory; kernel-level Arc N (Theorem N1) supplies the finite-width vacuum-response mechanism realising UV-FIN. The five-arc structural inventory is **complete at primitive level for the quantum sector**.

Phase-3 opens the next major program: ED → general-relativistic coupling. The driving question:

> **(Q-Phase-3) Does ED's primitive-level structure force, admit, or forbid gravitational coupling, dynamical curvature, and cosmological structure?**

Three sub-classes of answer to (Q-Phase-3) are possible:

- **(GR-emerge):** Curvature emerges as a structural consequence of ED primitives — Einstein-like equations are derivable.
- **(GR-induce):** Curvature is induced through specific ED-GR coupling channels (e.g., bandwidth-curvature coupling, vacuum-curvature coupling) but not derivable as pure Einstein dynamics.
- **(GR-add):** Curvature must be added externally; ED admits coupling to gravitational background structure but does not generate it.

Phase-3 evaluates which sub-class applies. The honest expected outcome is **(GR-induce) partial** — ED admits structural curvature-coupling channels (especially via Arc N's V1 vacuum kernel in curved spacetime) but does not derive full Einstein dynamics from primitives.

### 1.2 Acknowledged prior: ED-Phys-10 kinematic-curvature arc

ED's prior kinematic-curvature work — the ED-Phys-10 arc closed 2026-04-22 [1] — established a **kinematic acoustic-metric-only** result. Bandwidth-field gradients produce an effective metric for small-amplitude perturbations propagating on a smooth bandwidth background, paralleling the analogue-gravity acoustic-metric construction of Unruh and others. This is structurally clean but **does not produce Einstein equations** — there is no derived dynamical equation for the metric itself, no Schwarzschild solution, no full GR dynamics.

Phase-3 inherits this prior result as a starting point but does not assume it suffices. The kinematic acoustic-metric is a structural feature of ED's bandwidth-field dynamics; whether it extends to *dynamical* curvature equations is the central Phase-3 question.

### 1.3 Why Arc N changes the analysis

Pre-Arc-N, ED's quantum-sector closure operated under implicit Markovian assumptions that did not naturally extend to cosmological-scale dynamics (which typically involve persistent memory effects). Arc N's Theorem N1 (V1 finite-width vacuum kernel FORCED) supplies a primitive-level structural mechanism for non-Markovian vacuum response. In flat Minkowski space, V1 acts as a Lorentz-scalar function of $(x - x')^2$. In curved spacetime, V1 generalises to a function of geodesic distance — and the curvature-coupling structure of this generalisation is a substantive Phase-3 deliverable.

This is a genuinely new structural input compared to the ED-Phys-10 acoustic-metric work. Phase-3 has access to:
- The Phase-2 form-level theorems (Cl(3,1) frame, spin-statistics, GRH, UV-FIN, canonical commutation).
- The Arc N kernel-level theorem (V1 finite-width vacuum kernel).
- The cascading FORCED-conditional items (N1-E, N2-E, N3-D, V5-existence).
- The C-N4.1 CANDIDATE (vacuum-mediated CP phases).

Together these constitute the structural inputs Phase-3 evaluates against curvature.

---

## 2. Background

### 2.1 ED-Phys-10 acoustic-metric content (recap)

The ED-Phys-10 arc established that small-amplitude perturbations $\delta b$ on a smooth bandwidth background $b_0$ propagate with an effective metric
$$
g^{\mu\nu}_\mathrm{ac}(x) = \frac{1}{c_s^2(x)} \cdot \rho(x) \cdot \left[ -u^\mu u^\nu + c_s^2(x) (g^{\mu\nu} - u^\mu u^\nu) \right],
$$
with $u^\mu$ the local bandwidth-flow four-velocity, $c_s$ a bandwidth-mode propagation speed, and $\rho$ the local bandwidth density. This is the analogue-gravity acoustic-metric construction.

**What ED-Phys-10 produced:**
- Kinematic effective metric for bandwidth-mode perturbations.
- Analogue-Hawking-radiation-like horizon structures at $c_s$ → 0 surfaces.
- Causal-cone structure for bandwidth-mode propagation.

**What ED-Phys-10 did not produce:**
- Einstein equations for the bandwidth background itself.
- Newtonian-gravity emergence at long-wavelength.
- Schwarzschild or other GR solutions.
- A primitive-level mechanism for vacuum-curvature coupling.

**Guardrails from ED-Phys-10 (preserved in Phase-3):**
- ED has kinematic acoustic metric + free-scalar QFT only.
- No Einstein, no Schwarzschild, no fine-structure constant α from primitives.
- No gauge-field dynamical structure beyond minimal coupling.
- Interior-maximum P4 horizons are extremal.

Phase-3 must produce results consistent with these guardrails or explicitly identify why a guardrail can be relaxed.

### 2.2 Phase-2 + Arc N closure status (recap)

Eight FORCED structural theorems (per Arc N synthesis [2] §8.1):

| # | Theorem | Source | Type |
|---|---|---|---|
| 1 | Spin-statistics $\eta = (-1)^{2s}$ | R.2.5 | Theorem-level |
| 2 | Cl(3,1) frame uniqueness | R.2.4 | Algebra-level |
| 3 | Anyon prohibition in 3+1D | R.2.3 | Topology-level |
| 4 | Dirac equation emergence | R.3 | Dynamical-equation-level |
| 5 | GRH unconditional FORCED | Q.1 + Q.2/3/7/8 | Existence-level |
| 6 | Canonical (anti-)commutation FORCED | Q.7 | Operator-level |
| 7 | UV-FIN FORCED | Q.8 | Bound-level |
| 8 | V1 finite-width vacuum kernel FORCED | N.2 + N.5 | Memory-kernel-level |

Plus Arc M's three theorems (M1 σ_τ form, M2 massless slot, M3 no-ratio-mechanism), the Arc R Stage R.1 / R.3 results (Klein-Gordon, minimal coupling, Dirac), and the cascading FORCED-conditional items (N1-E, N2-E, N3-D, V5-existence).

Phase-3 inherits this complete inventory.

### 2.3 ED is Markov-compatible but not Markov-forcing (Arc N) — applies to GR too

Arc N's general finding — ED is consistent with both Markovian and admissible-bounded non-Markovian extensions — extends naturally to the GR coupling question. There is no primitive-level reason to expect ED to *force* a unique GR-coupling form; the more honest expectation is that ED admits multiple consistent coupling channels with specific channel-occupancy inherited.

This is the Phase-3 analogue of Arc M's H1-dominant pattern: form-level coupling structures admissible; specific coupling-channel choice and numerical content inherited.

---

## 3. Central Questions

Phase-3 organises around four central questions.

### 3.1 (Q-GR1) Does ED force a specific curvature–vacuum coupling?

**Statement.** Under V1 (Theorem N1), the vacuum-response kernel $K_\mathrm{vac}(x - x')$ in flat spacetime depends on Lorentz invariants of the separation $x - x'$. In curved spacetime, the natural generalisation replaces $(x - x')^2$ with the squared geodesic distance:
$$
K_\mathrm{vac}^\mathrm{curved}(x, x') = K_\mathrm{vac}\bigl(\sigma(x, x')\bigr),
$$
with $\sigma(x, x')$ Synge's world function (one-half squared geodesic distance). In the small-curvature expansion, $\sigma$ acquires curvature-dependent corrections — and $K_\mathrm{vac}^\mathrm{curved}$ inherits curvature-coupling structure.

**The question:** does ED's primitive-level framework force a specific curvature-coupling form for $K_\mathrm{vac}^\mathrm{curved}$, or is the coupling form INHERITED?

**Sub-question (Q-GR1.a):** does the V1 forcing argument (UV-FIN + Primitive 01 + Primitive 13) extend cleanly to curved spacetime, fixing $K_\mathrm{vac}^\mathrm{curved}$ structurally?

**Sub-question (Q-GR1.b):** are there additional primitive-level constraints in curved spacetime (e.g., causal-structure-respecting kernels, generally-covariant forms) that further restrict admissible curvature-coupling forms?

### 3.2 (Q-GR2) Does ED force a finite cosmological constant?

**Statement.** Arc Q.8 + Arc N.5 established that the cosmological-constant divergence-form puzzle is structurally dissolved under UV-FIN: $\Lambda_\mathrm{primitive}$ is finite, identifiable as a V1-kernel integral over cosmological-scale spacetime. The numerical magnitude remains INHERITED — depends on V1's specific functional form and cosmological-boundary content.

**The question:** does Phase-3's curved-spacetime extension supply additional structural constraints that fix $\Lambda$ beyond V1-form-and-boundary inheritance?

**Sub-question (Q-GR2.a):** is the V1-kernel integral over a closed cosmological spacetime structurally bounded by Lorentz invariants of the spacetime structure itself (e.g., total spacetime volume, characteristic curvature scale)?

**Sub-question (Q-GR2.b):** does the curvature-vacuum coupling (Q-GR1) introduce *back-reaction* between $\Lambda$ and curvature that fixes both jointly?

### 3.3 (Q-GR3) Does ED admit a dynamical curvature equation?

**Statement.** ED-Phys-10 produced a kinematic acoustic metric without dynamical content. The bandwidth-field equations are dynamical (they evolve in time per Phase-1 + Arc R structure), and the acoustic metric is a function of these dynamical fields. Whether the metric itself satisfies a *dynamical equation* analogous to Einstein's $R_{\mu\nu} - (1/2) R g_{\mu\nu} = 8\pi G T_{\mu\nu}$ is the central question.

**The question:** can ED admit (or force) a dynamical curvature equation for the emergent acoustic metric? If so, what is its source structure (analogue of $T_{\mu\nu}$) and what is its coupling constant (analogue of $G$)?

**Sub-question (Q-GR3.a):** is the bandwidth-field equation, when re-expressed in terms of the emergent acoustic metric, equivalent to (or approximated by) an Einstein-like equation?

**Sub-question (Q-GR3.b):** if (Q-GR3.a) yields an Einstein-like form, what is the structural status of the gravitational coupling constant — FORCED, CANDIDATE, or INHERITED?

### 3.4 (Q-GR4) Are ED worldlines geodesic in emergent geometry?

**Statement.** Phase-2 derivations treat chain worldlines $\gamma_K$ as primitive structural objects with Lorentz-covariant dynamics (Arc R) but do not address whether these worldlines satisfy *geodesic equations* in the emergent acoustic metric. In standard GR, free-fall worldlines are geodesics of $g_{\mu\nu}$; the analogue question for ED asks whether free-chain worldlines in the absence of interaction are geodesics of the emergent ED acoustic metric.

**The question:** in the emergent-acoustic-metric framework of ED-Phys-10, do free Phase-2 chain worldlines satisfy geodesic equations?

**Sub-question (Q-GR4.a):** is the Phase-2 "free chain" condition (no commitment events, no individuation pairing, no gauge coupling) equivalent to the geodesic condition $u^\nu \nabla_\nu u^\mu = 0$ on the emergent metric?

**Sub-question (Q-GR4.b):** if (Q-GR4.a) holds, does this generalise to the equivalence-principle statement that all free chains follow the same geodesic regardless of rule-type?

---

## 4. Structural Inputs from Phase-2 + Arc N

Phase-3 has access to the following primitive-level structural objects.

### 4.1 Form-level Phase-2 inputs

- **Lorentz-covariant participation measure** (Arc R Stage R.1).
- **Klein-Gordon and Dirac equations** with minimal coupling (Arc R).
- **Cl(3,1) frame** (Arc R Theorem R2).
- **Spin-statistics theorem $\eta = (-1)^{2s}$** (Arc R Theorem R1).
- **σ_τ master formula** (Arc M Theorem M1).
- **Massless gauge slot existence** (Arc M Theorem M2 + Arc Q Theorem Q1; unconditional FORCED).
- **GRH** (gauge-field-as-rule-type, unconditional FORCED).
- **Canonical (anti-)commutation** (Arc Q Theorem Q2).
- **UV-FIN** (Arc Q Theorem Q3).

### 4.2 Kernel-level Arc N inputs

- **V1 finite-width vacuum memory kernel** (Theorem N1; FORCED).
- **N1-E vacuum-induced bandwidth memory** (FORCED-conditional-on-V1).
- **N2-E vacuum-modulated commitment memory** (FORCED-conditional-on-V1).
- **N3-D vacuum-mediated adjacency memory** (FORCED-conditional-on-V1).
- **V5 cross-chain correlations** (existence FORCED-conditional; amplitudes INHERITED).
- **CANDIDATE C-N4.1** (vacuum-mediated additional CP phases).

### 4.3 Kinematic-curvature inputs from ED-Phys-10

- **Acoustic effective metric** $g^{\mu\nu}_\mathrm{ac}$.
- **Causal-cone structure** for bandwidth-mode propagation.
- **Analogue-horizon structures** at $c_s$ → 0 surfaces.

### 4.4 What Phase-3 does *not* have

- Einstein equations, Schwarzschild solution, or full GR dynamics — these were not produced by ED-Phys-10 and are not derivable from any closed Phase-2 / Arc N memo.
- Newtonian-gravity emergence at long-wavelength — open question.
- Specific gravitational coupling constant $G$ — INHERITED if it appears.
- Specific cosmological-constant value $\Lambda$ — INHERITED.

These are honest gaps Phase-3 will evaluate.

---

## 5. Constraints

Four primitive-level structural constraints frame what Phase-3 admits.

### 5.1 Lorentz covariance (carryover from Phase-2)

All Phase-3 admissible structures must be Lorentz-covariant in flat-spacetime limit and generally covariant in curved-spacetime extensions. This is the strongest constraint inherited from Phase-2.

**Forbidden Phase-3 structures:** Frame-dependent curvature-coupling forms; coordinate-system-dependent gravitational dynamics; non-tensorial gravitational equations.

### 5.2 Locality (Primitive 11 carryover)

Commitment events are point-events; gravitational coupling at primitive level must respect locality at each event. This restricts admissible non-local-in-spacetime gravitational structures.

**Forbidden Phase-3 structures:** Non-local gravitational propagators violating Primitive 11; non-causal gravitational dynamics.

### 5.3 UV-FIN (Arc Q Theorem Q3 carryover)

Phase-3 structures must preserve primitive-level UV finiteness. Gravitational coupling at primitive level must be UV-finite without renormalisation, paralleling Arc Q's UV-FIN reframing for the gauge sector.

**Forbidden Phase-3 structures:** Gravitational coupling forms that produce UV-divergent integrals at primitive level (continuum-approximation divergences are admissible; primitive-level divergences are not).

### 5.4 Primitive event-discreteness (Primitive 01 carryover)

Phase-3 structures must respect primitive event-discreteness — the substrate on which gravitational dynamics operate is not a continuum manifold but a discrete event set, with continuum-manifold structure emerging in the long-wavelength approximation.

**Forbidden Phase-3 structures:** Gravitational dynamics requiring continuum-manifold structure at primitive level; structures incompatible with the natural-cutoff scale $\ell_\mathrm{ED}$.

---

## 6. Phase-3 Roadmap

Phase-3 proceeds through five substages, paralleling the structure of Arc Q (10–18 sessions) and Arc N (5–9 sessions). Phase-3 is expected to be the most extensive ED phase — comparable in scope to Arc Q.

### 6.1 GR.0 — This memo (scoping). **Complete.**

### 6.2 GR.1 — Catalogue admissible curvature-coupling structures

`gr_coupling_catalogue.md`. Systematically enumerate Phase-3 admissible structures across:

- **GR-1 Bandwidth-curvature coupling.** How $b_K$ couples to spacetime curvature. Sub-classes:
  - GR-1-A: Direct coupling (Ricci scalar in bandwidth equation of motion).
  - GR-1-B: Effective coupling via acoustic metric.
  - GR-1-C: Curvature-induced bandwidth modulation.
- **GR-2 Vacuum-curvature coupling.** How V1 generalises in curved spacetime. Sub-classes:
  - GR-2-A: V1 with Synge world function $\sigma(x, x')$.
  - GR-2-B: Curvature-corrected V1 kernels via small-curvature expansion.
  - GR-2-C: Riemann-tensor-coupled V1 corrections.
- **GR-3 Geodesic structure for chain worldlines.** Whether $\gamma_K$ in absence of interaction is geodesic.
- **GR-4 Einstein-like emergent equations.** Whether bandwidth-field equations re-cast in acoustic-metric variables yield Einstein-like dynamics.

Each catalogue item characterised by primitive dependencies, potential constraint flags, and Phase-3 admissibility status.

Estimated scope: 2–3 sessions.

### 6.3 GR.2 — Evaluate FORCED curvature-coupling structures

`gr_coupling_forced.md`. Evaluate each catalogue item for primitive-level FORCED status.

**Most plausible FORCED candidates** (per Arc N hand-off [2] §6):
- **GR-2-A (V1 with Synge world function):** if V1's flat-space forcing argument extends to curved spacetime via the natural geodesic-distance generalisation, GR-2-A is FORCED. This is the cleanest Phase-3 FORCED candidate.
- **GR-3 (geodesic worldlines for free chains):** if the Phase-2 free-chain condition translates structurally into a geodesic equation on the emergent acoustic metric, GR-3 is FORCED.

**Less plausible FORCED candidates:**
- GR-1-A direct bandwidth-curvature coupling — likely CANDIDATE.
- GR-4 Einstein-like emergent equations — likely SPECULATIVE.

Estimated scope: 2–4 sessions.

### 6.4 GR.3 — Evaluate REFUTED curvature-coupling structures

`gr_coupling_refuted.md`. Evaluate catalogue items against C1 (Lorentz / general covariance), locality, UV-FIN, primitive event-discreteness.

**Likely REFUTED targets:**
- Frame-dependent curvature-coupling forms.
- Non-local gravitational propagators.
- Coupling forms requiring continuum-manifold structure at primitive level.
- Gravitational dynamics violating UV-FIN at primitive level.

Estimated scope: 1–2 sessions.

### 6.5 GR.4 — Cosmological implications

`gr_cosmological_implications.md`. Evaluate the cosmological consequences of FORCED + ADMISSIBLE Phase-3 structures:

- **Cosmological-Λ structure:** explicit V1-kernel-integral computation for closed cosmological spacetime; identification of which boundary content fixes Λ magnitude.
- **Large-scale structure:** how V5 cosmological correlations appear at structure-formation scales.
- **Dispersion-relation modifications:** quantitative form of V1-finite-width modifications to photon/graviton dispersion at extreme high frequencies.
- **Empirical signatures:** cosmic-ray / extreme-precision-photon-timing / cosmological-correlation-persistence test routes.

Estimated scope: 2–4 sessions.

### 6.6 GR.5 — Synthesis

`phase3_synthesis.md`. Integrate GR.0 through GR.4 into a final Phase-3 verdict. Expected closure: **partial GR-induce coupling with V1-curvature-coupling FORCED, geodesic worldlines FORCED-conditional, Einstein-equation emergence SPECULATIVE, Λ as V1-cosmological-integral with magnitude INHERITED, empirical-signature framework available for high-energy / cosmological tests**.

Estimated scope: 1 session.

### 6.7 Phase-3 total estimated scope

8–14 sessions. Comparable to Arc Q (10–18). The largest variability is in GR.2 (FORCED evaluation) — if GR-2-A V1-curvature-coupling closes cleanly, GR.2 is shorter; if GR-4 Einstein-equation emergence requires substantive structural derivation, GR.2 + GR.4 expand.

---

## 7. Honest Framing

### 7.1 Expected verdict-distribution prior

Per the methodological discipline established in M.0 / Q.0 / N.0:

- **45% partial GR-induce:** Phase-3 admits curvature-coupling channels (especially V1 in curved spacetime); some FORCED structural results (e.g., GR-2-A); Einstein-equation emergence partial or admissible-not-forced.
- **30% GR-add:** Phase-3 admits coupling to gravitational background structure but does not generate it; full GR remains external; ED-Phys-10 acoustic-metric stays the structural ceiling.
- **15% GR-emerge:** Phase-3 produces substantive Einstein-like emergence; gravitational coupling constant emerges as a structural CANDIDATE or weak FORCED.
- **10% surprise:** unexpected primitive-level mechanism produces non-trivial gravitational content (e.g., quantum-gravity-style discreteness corrections forced).

The honest expected outcome is **(GR-induce) partial** — paralleling Arc M's H1-dominant pattern at the curvature layer.

### 7.2 What Phase-3 realistically can achieve

- **Catalogue admissible curvature-coupling structures** (high feasibility).
- **Evaluate V1-curvature-coupling for FORCED status** (moderate-high feasibility — GR-2-A is the cleanest candidate).
- **Identify constraint violations** (high feasibility — C1 / locality / UV-FIN / event-discreteness are well-defined).
- **Produce explicit V1-kernel integral structure for cosmological-Λ** (moderate feasibility — depends on cosmological-boundary specification).
- **Identify empirical-signature routes** (high feasibility — at the structural level; specific quantitative predictions inherit V1 specifics).

### 7.3 What Phase-3 realistically cannot achieve

- **Predict Newton's gravitational constant $G$.** No mechanism in hand; $G$ remains INHERITED.
- **Solve the cosmological-Λ-magnitude problem numerically.** $\Lambda$'s magnitude depends on V1 specifics + cosmological boundary, both INHERITED.
- **Derive Schwarzschild or any specific GR solution.** ED-Phys-10 guardrails are preserved.
- **Solve the hierarchy problem** ($m_H \ll M_\mathrm{Planck}$). Out of Phase-3 scope.
- **Force a unique GR-coupling form.** ED's primitive structure is unlikely to admit only one consistent gravitational-coupling channel.

### 7.4 Methodological discipline

Phase-3 follows the M.0 / Q.0 / N.0 methodological pattern:

- Clear separation of FORCED / CANDIDATE / REFUTED / INHERITED.
- Honest expected-verdict prior up front.
- Cross-arc implications explicitly evaluated.
- *Form-FORCED, value-INHERITED* framing preserved.
- ED-Phys-10 guardrails preserved or explicitly relaxed-with-justification.

### 7.5 Phase-3's place in the ED program

Phase-3 sits as the **gravitational-sector structural foundation** of ED, paralleling Phase-1 (non-relativistic QM) + Phase-2 (relativistic + QFT) + Arc N (non-Markovian kernel) at the gravitational layer:

- **Phase-1:** non-relativistic QM at primitive level.
- **Phase-2 Arc R:** relativistic kinematics + dynamics.
- **Phase-2 Arc M:** mass structure.
- **Phase-2 Arc Q:** QFT extension.
- **Phase-2 Arc N:** non-Markovian kernel structure.
- **Phase-3:** gravitational coupling and cosmological structure.

Phase-3's closure will determine whether ED's structural inventory extends to a complete *quantum-and-gravitational* sector or terminates at the Phase-2 + Arc N closure with gravitational content remaining external.

---

## 8. Cross-References

### 8.1 Upstream

- Phase-1 closure: `qm_emergence_closure.md`, `qm_emergence_synthesis.md`.
- Arc R closures: `arc_r_stage1_synthesis.md`, `rule_type_taxonomy_synthesis.md`, `dirac_emergence.md`.
- Arc M closure: `chain_mass_synthesis.md`.
- Arc Q closure: `arc_q_synthesis.md`.
- Arc N closure: `arc_n_synthesis.md`.
- Phase-2 synthesis: `phase2_synthesis.md`.
- ED-Phys-10 kinematic-curvature arc: see `archive/research_history/ED Physics/ED-Phys-10/` and the durable findings recorded in `memory/project_ed10_geometry_qft_scope.md`.

### 8.2 Downstream (Phase-3 substages, forthcoming)

- `gr_coupling_catalogue.md` (GR.1).
- `gr_coupling_forced.md` (GR.2).
- `gr_coupling_refuted.md` (GR.3).
- `gr_cosmological_implications.md` (GR.4).
- `phase3_synthesis.md` (GR.5).

### 8.3 Inputs from Arc N hand-off

Per Arc N synthesis [2] §6, Arc N supplies three Phase-3 input channels:
- $\Lambda$ as V1-kernel integral.
- Curvature-vacuum coupling NEW CANDIDATE.
- Empirical signatures via dispersion-relation modifications and cosmological correlations.

Phase-3 evaluates each in detail.

---

## 9. References

[1] ED-Phys-10 kinematic-curvature arc, closed 2026-04-22. See archive and `memory/project_ed10_geometry_qft_scope.md`. Acoustic-metric construction; no Einstein, no Schwarzschild, no α from primitives.

[2] A. Proxmire, *Arc N Synthesis*, `arc_n_synthesis.md`, 2026.

[3] A. Proxmire, *Phase-2 Global Synthesis*, `phase2_synthesis.md`, 2026.

[4] A. Proxmire and Copilot, *Arc R / Arc M / Arc Q papers*, 2026 (companion publications).

[5] W. G. Unruh, "Experimental Black-Hole Evaporation?", *Phys. Rev. Lett.* **46**, 1351 (1981) — for analogue-gravity acoustic-metric prior art.

[6] M. Visser, "Acoustic black holes: horizons, ergospheres, and Hawking radiation," *Class. Quantum Grav.* **15**, 1767 (1998) — for acoustic-metric formalism.

[7] B. S. DeWitt, *The Global Approach to Quantum Field Theory*. Oxford University Press, 2003 — for Synge's world function $\sigma(x, x')$ in curved spacetime.

---

## 10. One-Line Summary

**Phase-3 opens the ED → GR coupling program with four central questions (Q-GR1 specific curvature-vacuum coupling forced?, Q-GR2 finite Λ structurally determined?, Q-GR3 dynamical curvature equation admissible?, Q-GR4 ED worldlines geodesic in emergent geometry?), structural inputs from Phase-2 + Arc N (eight FORCED structural theorems including V1 finite-width vacuum kernel + cascading items + ED-Phys-10 acoustic-metric kinematic-curvature foundation), four constraints (Lorentz covariance, locality, UV-FIN, primitive event-discreteness), and a five-substage roadmap (GR.1 catalogue → GR.2 FORCED → GR.3 REFUTED → GR.4 cosmological implications → GR.5 synthesis) producing an expected (GR-induce) partial verdict at 45% prior plausibility paralleling Arc M's H1-dominant pattern at the curvature layer — with V1-curvature-coupling (GR-2-A via Synge world function) as the cleanest FORCED candidate, geodesic free-chain worldlines (GR-3) as a likely FORCED-conditional candidate, Einstein-equation emergence (GR-4) likely SPECULATIVE, ED-Phys-10 guardrails preserved (no Einstein/Schwarzschild/α from primitives), $G$ and $\Lambda$ magnitudes INHERITED, and Phase-3 positioned as ED's gravitational-sector structural foundation paralleling Phase-1 + Phase-2 + Arc N at the gravitational layer.**
