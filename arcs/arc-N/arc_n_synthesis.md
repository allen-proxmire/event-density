# Arc N Synthesis — Closure Memo

**Stage N.5 — Arc N Closure**
**Status:** Final integration and closure memo. Headline verdict: **ED is Markov-compatible but not Markov-forcing. One memory-kernel-level structure is FORCED at primitive level — V1 (finite-width vacuum memory kernel) — by UV-FIN + Primitive 01 + Primitive 13 jointly. Non-Markovianity is structurally bounded by C1/C2/C3 constraints, not arbitrary. Phase-2 verdicts remain unchanged; Phase-3 substantively enriched. Theorem N1 takes its place alongside the Phase-2 FORCED structural theorems as ED's first memory-kernel-level structural prediction.**

---

## 1. Executive Summary

### 1.1 What Arc N set out to do

Arc N opened with the question (Q-N): *Does ED admit or require non-Markovian structure in chain evolution or multi-chain interactions?* Phase-2 (Arc R + Arc M + Arc Q) closed the structural framework for ED's quantum sector under implicit Markovian assumptions. Arc N tested whether those assumptions are primitive-derived or merely tractability-driven choices.

The Arc N opening memo [1] enumerated three candidate mechanisms (N1 bandwidth-memory, N2 commitment-memory, N3 adjacency-memory), three potential sources (S1 Primitive 11 commitment, S2 Primitive 13 relational timing, S3 Q.8 vacuum response), and three potential constraints (C1 Lorentz covariance, C2 spin-statistics, C3 UV-FIN). A five-substage roadmap (N.1 catalogue → N.2 forced → N.3 refuted → N.4 implications → N.5 synthesis) was set, with an honest expected-verdict prior of 30% mixed-with-FORCED-element.

### 1.2 Five-substage closure summary

- **N.0 (scoping)** [1]: framed (Q-N), enumerated three mechanisms × three sources × three constraints, set roadmap.
- **N.1 (catalogue)** [2]: enumerated 20 admissible non-Markovian structures across N1 (5), N2 (5), N3 (5), V (5) sectors with primitive dependencies and potential constraint flags.
- **N.2 (FORCED evaluation)** [3]: evaluated 20 catalogue items + 1 sub-case for primitive-level FORCED status. Result: **V1 unconditionally FORCED** by UV-FIN + Primitive 01 + Primitive 13; **N1-E, N2-E, N3-D FORCED-conditional-on-V1**; **V5 existence FORCED-conditional, amplitudes INHERITED**.
- **N.3 (REFUTED evaluation)** [4]: evaluated 15 NOT-FORCED items + sub-cases for C1/C2/C3 violations. Result: **7 REFUTED determinations** (N1-D Case-P↔Case-R, N2-B Case-R, N3-E frame-dependent, V3 $\alpha \geq 2$, V1-δ, V1-∞, V5 large-amplitude/long-range).
- **N.4 (cross-arc implications)** [5]: evaluated impact on Arc M, Arc Q.5, Arc Q.6, Arc Q.7, Arc Q.8, Phase-3. Result: **No Phase-2 verdict overturned**; three closures structurally enriched; one new CANDIDATE C-N4.1 opened (vacuum-mediated additional CP phases beyond Jarlskog count); Phase-3 substantively unblocked with three new structural-input channels.

### 1.3 Final inventory

- **1 unconditionally FORCED:** V1 (finite-width vacuum memory kernel).
- **3 FORCED-conditional-on-V1:** N1-E, N2-E, N3-D.
- **1 partial-FORCED:** V5 (existence FORCED-conditional; amplitudes INHERITED).
- **7 REFUTED determinations:** N1-D in P↔R sub-case; N2-B in Case-R sub-case; N3-E in frame-dependent forms; V3 for $\alpha \geq 2$; V1-δ zero-width limit; V1-∞ infinite-width limit; V5 large-amplitude/long-range sub-cases.
- **11 ADMISSIBLE-NOT-FORCED catalogue items** + 4 V-sector specific-form sub-cases admissible within V1 class = **15 admissible-not-forced structures**.
- **1 new CANDIDATE:** C-N4.1 (vacuum-mediated CP-phase enrichment).

### 1.4 Headline structural result

**Theorem N1 (Finite-Width Vacuum Memory Kernel FORCED).** ED's first memory-kernel-level structural theorem. Joins Phase-2's seven FORCED structural theorems as ED's structural inventory.

---

## 2. Theorem N1 — Finite-Width Vacuum Memory Kernel FORCED

### 2.1 Statement

> **Theorem N1.** *The vacuum-response kernel $K_\mathrm{vac}(x - x')$ acting on chain participation perturbations is structurally FORCED at primitive level to have finite, non-zero, decaying width. Specifically, the kernel must satisfy:*
> *(i) Finite width: $K_\mathrm{vac}(x - x')$ is non-singular at $x = x'$ (rules out $\delta^4$-function form).*
> *(ii) Decaying support: $K_\mathrm{vac}(x - x') \to 0$ as $|x - x'| \to \infty$ (rules out constant kernels).*
> *(iii) Lorentz-scalar form: $K_\mathrm{vac}$ depends only on Lorentz invariants of $x - x'$.*
> *(iv) Bounded short-time behaviour: kernel growth is sub-power-law-2 in the proper-time-invariant separation (rules out $\alpha \geq 2$ power-law forms in 3+1D).*
> *Specific functional forms (V2 exponential decay, V3 power-law with $\alpha < 2$, V4 multi-scale composition) are admissible specific realisations within the FORCED class; specific values INHERITED.*

### 2.2 Proof sketch

The proof runs through three structural-argument legs:

**(Leg 1) UV-FIN argument (forces non-zero finite width).** A δ-function vacuum response $K_\mathrm{vac}(x - x') = c_0 \delta^4(x - x')$ has Fourier transform $\widetilde{K_\mathrm{vac}}(\omega, \mathbf{k}) = c_0$, constant across all frequencies. In continuum-approximation loop integrals involving the vacuum response, this constant frequency-weighting amplifies high-frequency contributions, threatening Arc Q Theorem Q3 (UV-FIN).

Primitive 01 event-discreteness imposes a primitive-level event-resolution scale $\ell_\mathrm{ED}$ below which the manifold structure is not continuum-like. Primitive 13 supplies finite proper-time intervals. Jointly, vacuum response cannot resolve perturbations at sub-primitive resolution; the kernel must be smoothed at the $\ell_\mathrm{ED}$ scale. Therefore $K_\mathrm{vac}$ has finite, non-zero width set by the primitive event-discreteness.

The δ-limit is REFUTED by C3 (Stage N.3 §3.1 V1-δ refutation).

**(Leg 2) Lorentz-covariance argument (forces decaying support).** A constant kernel $K_\mathrm{vac}(x - x') = c_\infty$ for all $x - x'$ implies infinite correlation length: every event is correlated with every other event with equal weight, including arbitrary spacelike separations. While trivially Lorentz-scalar, such a kernel is structurally pathological — it does not respect causal-structure constraints embedded in Lorentz covariance and is incompatible with Primitive 11 commitment-event locality.

The infinite-width limit is REFUTED by C1 (Stage N.3 §3.2 V1-∞ refutation).

Therefore the kernel must decay at large separations.

**(Leg 3) UV-FIN refinement (forces sub-power-law-2 decay).** Power-law kernels $K_\mathrm{vac} \propto |x - x'|^{-2\alpha}$ in 3+1D produce UV-divergent integrals when $2\alpha \geq 4$, i.e., $\alpha \geq 2$. The integral $\int d^4 z \, |z|^{-2\alpha} \cdot (\text{bounded test function})$ converges at small $|z|$ iff $\alpha < 2$ in 3+1D.

Power-law kernels with $\alpha \geq 2$ are REFUTED by C3 (Stage N.3 §2.4 V3 refutation).

Therefore admissible kernels have sub-power-law-2 short-distance behaviour.

**(Conclusion).** The three legs jointly force $K_\mathrm{vac}$ to have finite, non-zero, decaying, Lorentz-scalar, sub-power-law-2 form. This is the FORCED V1 class. Specific functional forms within this class (V2 exponential, V3 with $\alpha < 2$, V4 multi-scale) are admissible specific realisations; specific values (timescales, exponents, amplitudes) INHERITED. $\square$

### 2.3 Dependencies on primitives and Phase-2 theorems

- **Primitive 01** (event-discreteness): supplies the natural-cutoff scale $\ell_\mathrm{ED}$.
- **Primitive 04** (bounded bandwidth): bounds amplitude content for finiteness arguments.
- **Primitive 06** (four-gradient, Lorentz covariance): supplies the C1 constraint.
- **Primitive 11** (commitment-event locality): supplies the C1-locality refinement.
- **Primitive 13** (finite proper-time intervals): supplies the second leg of finiteness.
- **Arc Q Theorem Q3** (UV-FIN): primitive-level UV finiteness is the headline theorem driving V1's necessity.
- **Arc Q.8** (effective-vacuum framework): supplies the structural object on which V1 acts.

V1's forcing argument is downstream of UV-FIN: UV-FIN is the more general theorem, V1 is its specific realisation at the vacuum-response level. The two are mutually reinforcing: UV-FIN forces V1; V1 supplies primitive-level kernel structure realising UV-FIN's continuum-approximation reframing.

### 2.4 Cascading FORCED-conditional items

Theorem N1 propagates FORCED status to four secondary items via the vacuum-coupling channel:

- **N1-E (vacuum-induced bandwidth memory):** the $b^\mathrm{env}$ band of any chain inherits memory-kernel structure from V1 when the chain interacts with the effective vacuum. **FORCED-conditional-on-V1.**
- **N2-E (vacuum-modulated commitment memory):** commitment dynamics necessarily interact with the local vacuum state per Arc Q.8 effective-vacuum framework; V1 makes this interaction memory-bearing. **FORCED-conditional-on-V1.**
- **N3-D (vacuum-mediated adjacency memory):** same-vacuum-sector chains acquire correlated $b^\mathrm{env}$ content via the V1 cross-chain extension. **FORCED-conditional-on-V1.**
- **V5 (vacuum-induced cross-chain correlations):** existence of cross-chain correlations is FORCED-conditional-on-V1; specific correlation amplitudes INHERITED.

Since V1 is unconditionally FORCED, these conditional FORCED statuses are effectively unconditional. We retain the conceptual hierarchy: they are FORCED *because* V1 is forced, not by independent primitive arguments.

---

## 3. REFUTED Items Summary

Stage N.3 produced 7 REFUTED determinations. Each is a structural elimination at primitive level under one of the three constraints C1/C2/C3.

### 3.1 REFUTED catalogue

| ID | Sub-case REFUTED | Constraint | Primitive(s) enforcing refutation | Argument |
|---|---|---|---|---|
| **N1-D** | Case-P↔Case-R cross-band coupling | **C2** | R.2.5 spin-statistics + 07-L4 + 10 | Cross-class kernel produces η-mixing; π_1(Q_2) = ℤ_2 forbids intermediate phases |
| **N2-B** | Hysteresis on Case-R | **C2** | 10 individuation + R.2.5 | Two Case-R chains coexist within delay window; violates Pauli exclusion at structural level |
| **N3-E** | Frame-dependent non-local propagation | **C1** | 06 + 11 | Preferred-frame correlations forbidden by Lorentz covariance |
| **V3** | Power-law $\alpha \geq 2$ | **C3** | 01 + 04 + 13 + Q.3 (Theorem Q3) | $\int d^4 z |z|^{-2\alpha}$ diverges in 3+1D for $\alpha \geq 2$ |
| **V1-δ** | Zero-width limit | **C3** | 01 + Q.3 (Theorem Q3) | δ-response amplifies UV (bounds V1 from below) |
| **V1-∞** | Infinite-width limit | **C1** | 06 + 11 | Constant kernel breaks locality (bounds V1 from above) |
| **V5** | Large-amplitude / long-range | **C1, C3** | 06 + 04 + 11 + Theorem Q3 | Infinite correlation length / insufficient decay |

### 3.2 Refutation pattern

- **C1 violations** (Lorentz covariance): 3 items (N3-E primary, V1-∞ sub-case, V5 large-amplitude sub-case).
- **C2 violations** (spin-statistics): 2 items (N1-D P↔R sub-case, N2-B Case-R sub-case).
- **C3 violations** (UV-FIN): 3 items (V3 $\alpha \geq 2$, V1-δ sub-case, V5 long-range sub-case).

All three constraints active. The C1/C2/C3 framework is structurally exhaustive at Stage N.3 — no new constraint sources surfaced.

### 3.3 V1 admissibility class is bounded both ways

The two V1 limit refutations (V1-δ at zero width, V1-∞ at infinite width) together establish that V1's admissibility class is **bounded**: kernels must have finite, non-zero, decaying width. The bounds are themselves consequences of C1 + C3 — derived restrictions, not additional postulates. This refines Theorem N1's content: the FORCED class is structurally well-defined and bounded.

---

## 4. ADMISSIBLE-NOT-FORCED Items Summary

11 catalogue items + 4 V-sector specific-form sub-cases = 15 admissible-not-forced structures. Each is consistent with primitives + Phase-2 theorems + C1/C2/C3 constraints, but not structurally required. They constitute the consistent-extension space for non-Markovian phenomenology.

### 4.1 Admissible-not-forced inventory

| ID | Description | Influences which arc(s)? | Notes |
|---|---|---|---|
| **N1-A** | Finite-width $b^\mathrm{env}$ kernels | Arc M, Arc Q.5 | Largely subsumed by N1-E in practice |
| **N1-B** | History-weighted σ_τ spectral-rate | **Arc M** | Modifies σ_τ structure; H1-dominant unchanged |
| **N1-C** | Multi-scale bandwidth memory | Arc M, Phase-3 | Hierarchical-coupling regimes |
| **N1-D, same-class sub-case** | Same-class cross-band coupling | Arc M | Within-rule-type bands |
| **N2-A** | Density-dependent thresholds | Arc Q.7 | Quantitative threshold modulation |
| **N2-B, Case-P sub-case** | Hysteresis on Case-P | Arc Q.7 | Coincidence-permitting; admissible |
| **N2-C** | Memory-weighted commitment spacing | Arc Q.5, Arc Q.7 | Renewal-process generalisation |
| **N2-D** | Multi-chain commitment correlations | Arc Q.6, Arc Q.7 | Subsumed largely by N3 sector |
| **N3-A** | Time-lagged adjacency graphs | Arc Q.6, Arc Q.7 | Q.2 R-2 generalisation |
| **N3-B** | History-dependent adjacency weights | Arc Q.6 | Entanglement-persistence content |
| **N3-C** | Multi-chain (3+) correlation kernels | **Arc Q.6**, Phase-3 | Higher-order correlations |
| **V2** | Exponential-decay vacuum response | Arc Q.5, Arc Q.8, **Phase-3** | Specific V1 realisation |
| **V3, $\alpha < 2$ sub-case** | Power-law vacuum response | Arc Q.5, **Phase-3** | Specific V1 realisation; long-range admissible |
| **V4** | Multi-scale vacuum memory | Arc Q.5, **Phase-3** | Multi-physical-timescale realisation |
| **V5, bounded sub-case** | Bounded cross-chain correlations | **Arc Q.6**, Phase-3 | FORCED-conditional in existence; values INHERITED |

### 4.2 Cross-arc influence concentrations

- **Arc M influenced** by N1-A/B/C, N1-D-same-class — primarily through σ_τ refinements at Stage N.4.
- **Arc Q.5 influenced** by V1-class (V2, V3-restricted, V4) — vacuum-polarisation form-factor structure.
- **Arc Q.6 influenced** by V5-bounded, N3-B/C — CP-phase enrichment (CANDIDATE C-N4.1).
- **Arc Q.7 influenced** by N2-A/B-Case-P/C, N2-D, N3-A — unequal-time commutator extensions.
- **Arc Q.8 influenced** by V1-class — Λ kernel-integral refinement.
- **Phase-3 influenced** by V1-class, V5-bounded, N1-C, N3-C — cosmological-scale structural inputs.

---

## 5. Cross-Arc Implications Summary

Stage N.4 evaluated the structural impact of FORCED V1 + cascades + ADMISSIBLE structures on Phase-2 closures and Phase-3 hand-off content. **No Phase-2 verdict is overturned by Arc N.** Three closures structurally enriched; one new CANDIDATE opened; Phase-3 substantively unblocked.

### 5.1 Arc M (mass structure)

**Status:** UNCHANGED at verdict level.

- **Theorem M1 (σ_τ form):** UNCHANGED. N1-E refinement adds vacuum-coupled spectral-rate detail; form-FORCED preserved (Lorentz-scalar, amplitude-invariant).
- **Theorem M2 (massless slot):** UNCHANGED FORCED.
- **Theorem M3 (no ratio mechanism):** UNCHANGED.
- **H1-dominant verdict:** UNCHANGED.

Arc M's *value-INHERITED* content now includes V1 kernel structure as additional inherited content but no new mass-ordering inequalities are FORCED.

### 5.2 Arc Q.5 (radiative corrections)

**Status:** UNCHANGED at verdict level.

- **UV-FIN (Theorem Q3):** UNCHANGED FORCED. V1 is its vacuum-response realisation; mutually reinforcing.
- **Vacuum-polarisation transversality:** UNCHANGED FORCED via GRH-3. V1's Lorentz-scalar form-factor structure preserves $q_\mu \Pi^{\mu\nu} = 0$.
- **Tree-level $g = 2$:** UNCHANGED.
- **Only $\sigma^{\mu\nu}$ contributes to $a_\mu$:** UNCHANGED.
- **Schwinger-sign CANDIDATE:** structural setting refined by V1 (vertex-topology argument now operates with finite-width kernels); promotion still requires concrete derivation.

### 5.3 Arc Q.6 (generations and mixing)

**Status:** UNCHANGED at verdict level + **NEW CANDIDATE C-N4.1 opened**.

- **Generation count = 3:** REFUTED-as-forced; UNCHANGED EMPIRICAL.
- **Mixing-matrix existence:** UNCHANGED FORCED.
- **CP-phase existence (Jarlskog):** UNCHANGED FORCED.
- **NEW CANDIDATE C-N4.1:** Under V5 cross-chain correlations + complex Yukawa + ≥3 generations, vacuum-mediated phase content may FORCE additional structural CP-violation channels beyond the tree-level Jarlskog count $(n-1)(n-2)/2$. This is the most substantive Arc N → Phase-2 enrichment.

### 5.4 Arc Q.7 (second quantisation)

**Status:** UNCHANGED at verdict level + structural extension to unequal-time forms.

- **Canonical (anti-)commutation FORCED (Theorem Q2):** UNCHANGED at equal-time coincident-point level.
- **Pauli exclusion at every event:** UNCHANGED FORCED (preserved by Stage N.3 N2-B Case-R refutation).
- **Lightlike worldlines for $\sigma = 0$:** UNCHANGED FORCED.
- **Multi-rule-type vacuum factorisation:** UNCHANGED.
- **Unequal-time commutators:** EXTENDED with memory-kernel structure inherited from V1; form-FORCED preserved.

### 5.5 Arc Q.8 (vacuum structure)

**Status:** UNCHANGED at verdict level (reinforced) + Λ refinement.

- **GRH unconditional FORCED:** UNCHANGED (and reinforced — V1 supplies kernel structure within GRH-FORCED gauge rule-type).
- **Vacuum/particle distinction:** UNCHANGED.
- **Lorentz + gauge invariance of vacuum:** UNCHANGED.
- **Cosmological-Λ divergence-form dissolution:** UNCHANGED (refined). Λ_primitive is now identifiable as the integral of V1 vacuum-response kernel over cosmological-scale spacetime; specific value INHERITED (depends on V1 kernel form + cosmological-boundary content).

---

## 6. Phase-3 Hand-Off

Arc N supplies three substantive new structural-input channels for Phase-3 (ED → GR coupling, cosmological structure, empirical signatures).

### 6.1 Λ as V1-kernel integral

The cosmological-constant divergence-form dissolution from Arc Q.8 acquires explicit kernel-integral structure under V1:
$$
\Lambda_\mathrm{primitive} \sim \int K_\mathrm{vac}(x - x') \cdot \rho_\mathrm{vac\ energy}(x') \, d^4 x',
$$
with V1's specific functional form (V2 / V3 with $\alpha < 2$ / V4) determining the integral's structure. The "what numerical structure determines Λ?" question — left open at Arc Q.8 closure — now reframes under V1 to "what is the V1 kernel form, and what is the integration domain at cosmological scales?" The first remains INHERITED; the second is a Phase-3 cosmological-boundary question.

### 6.2 Curvature-vacuum coupling NEW CANDIDATE

In Phase-3 ED → GR coupling, V1 in flat Minkowski space generalises to curved spacetime as a function of geodesic distance between events. The curvature-coupling structure may produce **new structural terms** in the effective ED-GR action that are not present at Phase-2 level. This is a Phase-3 evaluation deliverable — Arc N supplies the structural setup, Phase-3 evaluates whether ED forces specific curvature-vacuum coupling terms.

### 6.3 Empirical signatures

Two Arc-N-derived empirical-signature routes for high-energy / cosmological-scale tests of ED:

(i) **Dispersion-relation modifications.** V1's finite-width kernel introduces frequency-dependent structure into vacuum response, producing small modifications to photon and graviton dispersion relations near the primitive event-discreteness scale. Possibly testable via cosmic-ray observations, ultra-high-energy gamma-ray timing, or extreme-precision photon timing experiments.

(ii) **Cosmological-correlation persistence.** V5 (cross-chain correlations) implies vacuum-mediated correlations between distant cosmological structures. Specific signatures depend on V1/V5 kernel forms (INHERITED), but the *existence* of structural correlations beyond standard tree-level QFT is FORCED-conditional-on-V1.

Both routes inherit V1/V5 kernel structure; both are admissible structurally; specific values INHERITED. Phase-3 will evaluate empirical viability.

---

## 7. Final Arc N Verdict

### 7.1 ED is Markov-compatible but not Markov-forcing

Arc N's primitive-level analysis confirms the opening claim: Primitives 01–13 admit non-Markovian structure as a consistent extension but do not generally force it. Phase-2's implicit Markovian assumptions were tractability-driven choices, not primitive-derived consequences. Most non-Markovian extensions catalogued in N.1 are ADMISSIBLE-NOT-FORCED.

### 7.2 One memory-kernel-level structure FORCED

V1 (finite-width vacuum memory kernel) is the exception: it is structurally FORCED at primitive level by UV-FIN + Primitive 01 + Primitive 13 jointly. Theorem N1 establishes this as ED's first memory-kernel-level structural prediction.

The forcing argument is downstream of UV-FIN: UV-FIN is the more general theorem, V1 is its specific realisation at the vacuum-response level. Together they constitute a structurally consistent framework where primitive-level UV finiteness manifests as finite-width vacuum kernels.

### 7.3 Non-Markovianity is structurally bounded, not arbitrary

The 7 REFUTED determinations from Stage N.3 establish that admissible non-Markovian structure is *constrained*: not every memory kernel form is admissible. Specifically:

- **C1 (Lorentz covariance)** rules out frame-dependent structures and infinite-correlation-length forms.
- **C2 (spin-statistics)** rules out memory kernels that violate Pauli exclusion or mix Case-P / Case-R sectors.
- **C3 (UV-FIN)** rules out memory kernels with insufficient short-time decay or amplifying high-frequency contributions.

The admissibility class is well-defined and bounded — admissible non-Markovian structures inherit Phase-2 structural constraints automatically.

### 7.4 Phase-2 remains intact; Phase-3 enriched

Arc N's findings do not require any modification of Phase-2 closures. All FORCED Phase-2 structural theorems (R.2.5 spin-statistics, R3 Dirac, M1/M2/M3 Arc M, Q1/Q2/Q3 Arc Q) UNCHANGED. The H1-dominant Arc M verdict, Arc Q's mostly-positive verdict, and the Phase-2 form-FORCED / value-INHERITED methodology all preserved.

Phase-3 (ED → GR coupling, cosmology, empirical signatures) gains substantive new structural input from Arc N — three input channels (Λ-integral structure, curvature-vacuum coupling CANDIDATE, empirical signatures) that were not available pre-Arc-N.

### 7.5 Headline summary

| Arc N output | Status |
|---|---|
| Theorem N1 (V1 FORCED) | Established structurally |
| 4 cascading FORCED-conditional items | Established (effectively unconditional via V1) |
| 7 REFUTED determinations | Established |
| 11 + 4 ADMISSIBLE-NOT-FORCED structures | Catalogued; available for downstream phenomenology |
| New CANDIDATE C-N4.1 | Opened (vacuum-mediated additional CP phases) |
| Phase-2 verdicts | UNCHANGED (Arc N enriches without altering) |
| Phase-3 unblocked | Three new structural-input channels |

---

## 8. Arc N's Place in the ED Structural Inventory

### 8.1 Theorem N1 alongside Phase-2 theorems

Theorem N1 takes its place as ED's eighth FORCED structural theorem:

| # | Theorem | Source | Type |
|---|---|---|---|
| 1 | Spin-statistics $\eta = (-1)^{2s}$ | R.2.5 | Theorem-level structural |
| 2 | Cl(3,1) frame uniqueness | R.2.4 | Algebra-level structural |
| 3 | Anyon prohibition in 3+1D | R.2.3 | Topology-level structural |
| 4 | Dirac equation emergence | R.3 | Dynamical-equation-level structural |
| 5 | GRH unconditional FORCED | Q.1 + Q.2/3/7/8 | Existence-level structural |
| 6 | Canonical (anti-)commutation FORCED | Q.7 | Operator-level structural |
| 7 | UV-FIN FORCED | Q.8 | Bound-level structural |
| **8** | **V1 finite-width vacuum kernel FORCED** | **N.2 + N.5** | **Memory-kernel-level structural** |

Theorem N1 is the **first memory-kernel-level structural theorem** in ED — distinct in character from the Phase-2 theorems but consistent with them. It supplies primitive-level kernel structure to the abstract UV-FIN claim.

### 8.2 How Arc N complements Phase-2

The Phase-2 theorems operate at the **form-level** of ED's quantum sector: they fix the form of equations (Klein-Gordon, Dirac), the structure of representations (Cl(3,1), spin-statistics), the existence of particle classes (GRH), the operator structure (canonical commutation), and the bounds (UV-FIN).

Arc N operates at the **kernel-level**: it specifies the structure of the vacuum-response kernel that realises Phase-2's UV-FIN bound. Phase-2 said "primitive-level multi-chain participation integrals are finite"; Arc N says "the kernel mechanism by which finiteness is realised is V1 with finite, non-zero, decaying, sub-power-law-2 form."

The two layers are complementary:
- **Phase-2 form-level theorems** restrict the space of admissible quantum-sector structures.
- **Arc N kernel-level theorems** specify the primitive-level mechanisms within that space.

Together they yield a more complete ED quantum-sector picture than either layer alone.

### 8.3 How Arc N completes the quantum-sector picture at the kernel level

Pre-Arc-N, the ED quantum-sector picture was structurally complete at the form level (Phase-2 closure) but kernel-level unspecified — Phase-2's UV-FIN claim left open the specific mechanism by which UV finiteness operates. Arc N closes this gap: V1 is the kernel mechanism.

Specifically:

- **Vacuum response** has finite-width kernel structure (V1).
- **Bandwidth memory** in the environment-coupled band inherits V1's structure (N1-E).
- **Commitment dynamics** are vacuum-modulated via V1 (N2-E).
- **Multi-chain adjacency** is vacuum-mediated via V1 (N3-D).
- **Cross-chain correlations** exist as a structural consequence of shared vacuum coupling (V5).

Together, these supply the kernel-level structural detail that makes UV-FIN concrete. The cosmological-constant reframing (Λ as finite primitive-level integral) acquires explicit V1-kernel-integral structure. The vacuum-polarisation transversality in Arc Q.5 acquires explicit V1-form-factor mechanism. The unequal-time commutators in Arc Q.7 acquire explicit V1-derived memory content.

### 8.4 Methodological consistency

Arc N preserves the form-FORCED / value-INHERITED methodological framing established in Arc M and extended through Arc Q:

- **Form-FORCED:** V1 kernel class is structurally required; existence of vacuum-induced bandwidth, commitment, adjacency memory is structurally required; bounds on V1 admissibility (V1-δ and V1-∞ refutations) are structurally derived.
- **Value-INHERITED:** specific V1 functional form, specific kernel timescales, specific correlation amplitudes, specific Λ magnitude all inherited from rule-type / chain-initial-condition / cosmological-boundary data.

This is the same methodology that produced Arc M's H1-dominant verdict and Arc Q's mostly-positive verdict. Arc N closes consistent with the established Phase-2 framing.

### 8.5 Integration into the ED program

Arc N's closure positions ED's structural foundation as follows:

- **Phase-1** (non-relativistic): Schrödinger, Born, Bell, Heisenberg derived from participation measure + commitment.
- **Phase-2 Arc R** (relativistic): Klein-Gordon, spin-statistics, Cl(3,1), Dirac.
- **Phase-2 Arc M** (mass): σ_τ form FORCED; values INHERITED; massless slot existence FORCED via GRH.
- **Phase-2 Arc Q** (QFT): GRH unconditional, canonical commutation, UV-FIN — three FORCED theorems completing the form-level structure.
- **Phase-2 Arc N** (non-Markovian, this synthesis): V1 finite-width vacuum kernel FORCED — kernel-level structure realising UV-FIN.

The five-arc structure is **complete at primitive level**: form-level Phase-2 closures + kernel-level Arc N closure = structurally complete, UV-finite, kernel-explicit ED quantum sector.

Phase-3 (ED → GR coupling) opens with this complete foundation as input.

---

## 9. Cross-References

- Arc N memos: `arc_n_scoping.md` (N.0), `non_markov_catalogue.md` (N.1), `non_markov_forced.md` (N.2), `non_markov_refuted.md` (N.3), `non_markov_implications.md` (N.4), `arc_n_synthesis.md` (this memo, N.5).
- Phase-2 closures: `phase2_synthesis.md`, `arc_r_stage1_synthesis.md`, `chain_mass_synthesis.md`, `arc_q_synthesis.md`, `dirac_emergence.md`, `rule_type_taxonomy_synthesis.md`.
- Phase-1 closure: `qm_emergence_closure.md`.
- Memory-kernel precursor: `memory_kernel_derivation.md`.

---

## 10. One-Line Summary

**Arc N closes with one FORCED structural theorem (Theorem N1: V1 finite-width vacuum memory kernel FORCED at primitive level by UV-FIN + Primitive 01 + Primitive 13, with the admissibility class bounded both ways by V1-δ and V1-∞ refutations to finite, non-zero, decaying, Lorentz-scalar, sub-power-law-2 form), four cascading FORCED-conditional items (N1-E, N2-E, N3-D vacuum-coupled bandwidth/commitment/adjacency mechanisms; V5 cross-chain correlation existence with amplitudes INHERITED), seven REFUTED determinations under C1/C2/C3 (N1-D Case-P↔Case-R, N2-B Case-R hysteresis, N3-E frame-dependent, V3 $\alpha\geq2$, V1-δ, V1-∞, V5 large-amplitude/long-range), eleven catalogue items + four V-sector specific-form sub-cases ADMISSIBLE-NOT-FORCED, one new CANDIDATE C-N4.1 (vacuum-mediated additional CP phases beyond Jarlskog count for $\geq 3$ generations), no Phase-2 verdicts overturned with three closures structurally enriched (Arc M σ_τ vacuum-coupled refinement; Arc Q.5 vacuum-pol form-factor; Arc Q.8 Λ-integral refinement) and Phase-3 substantively unblocked with three new structural-input channels (Λ as V1-kernel integral, curvature-vacuum coupling CANDIDATE, empirical signatures via dispersion-relation modifications and cosmological correlations) — Theorem N1 takes its place as ED's eighth FORCED structural theorem and first memory-kernel-level structural prediction, completing the ED quantum-sector picture at the kernel level alongside Phase-2's form-level theorems while preserving the form-FORCED / value-INHERITED methodology established across Arcs R/M/Q.**
