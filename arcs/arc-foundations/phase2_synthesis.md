# Phase-2 Global Synthesis

**Phase-2 Closure Memo — ED Quantum Sector Complete**
**Status:** Closure memo. Integrates Arc R (relativistic kinematics + dynamics), Arc M (chain-mass structure), and Arc Q (QFT extension) into a single structural verdict for ED's quantum sector. **Headline closure: ED now has a structurally complete, UV-finite quantum sector. Form is forced; numerical content is inherited. Phase-3 (ED → GR coupling, cosmological structure, empirical signatures) is unblocked.**

---

## 1. Executive summary

### 1.1 What Phase-2 set out to do

Phase-1 closed the non-relativistic single-particle quantum sector: Schrödinger, Born, Bell, Heisenberg derived from the participation measure `P_K = √b · e^{iπ}` + four-band decomposition + commitment dynamics. Two open frontiers were flagged: (a) extension to relativistic and field-level scales, and (b) primitive-level treatment of the chain-mass problem.

Phase-2 set out to address both:

- **Arc R** — extend ED to relativistic single-chain kinematics + dynamics (Klein-Gordon, spin-statistics, Dirac).
- **Arc M** — evaluate whether the chain-mass problem has a primitive-level resolution.
- **Arc Q** — extend ED to multi-chain field-level QFT structure (gauge, vertices, SSB, loops, generations, second quantisation, vacuum).

Plus an independent thread:

- **Arc N** — non-Markovian platform-specific extensions (active; not Phase-2-closure-blocking).

### 1.2 What was structurally achieved

Phase-2 delivered **three FORCED structural theorems** at primitive level beyond what Phase-1 produced, plus extensive form-level admissibility content:

**(T1) Spin-statistics theorem η = (−1)^{2s}** — derived at primitive level from R.2.1 exchange dichotomy + R.2.3 π_1(Q_2) = ℤ_2 + R.2.4 Cl(3,1) frame + R.2.5 MB closure. Anyons forbidden in 3+1D; fermions/bosons exhaustive.

**(T2) GRH unconditional FORCED** — at least one massless Case-P (1/2,1/2) gauge rule-type τ_g exists structurally. **ED's first "particle-class must exist" prediction.** Closed via all five GRH refinements (R-1 lightlike at Q.7, R-2 gauge-quotient at Q.2, R-3 vertex-commitment at Q.3, R-4 non-Abelian at Q.3, R-5 vacuum/particle at Q.8).

**(T3) UV-FIN FORCED at primitive level** — Primitive 01 event-discreteness + Primitive 13 finite proper-time intervals + Primitive 04 bounded bandwidth jointly guarantee primitive-level finiteness of all multi-chain participation integrals. **Renormalisation REFUTED as fundamental requirement** (admissible only as continuum-approximation effective machinery). **Cosmological-constant divergence-form structurally dissolved.** Headline novel result of Phase-2.

Plus form-level FORCED content distributed across the three arcs: KG and Dirac equations FORCED; Cl(3,1) frame uniqueness; canonical (anti-)commutation; lightlike worldlines for σ = 0; vertex catalogue + gauge-invariance filter; mixing matrices + CP phases FORCED-to-exist as linear-algebra theorems; vacuum factorisation; effective vacuum b^env content; Dirac g = 2; non-Abelian D_μ uniqueness conditional on SU(N).

### 1.3 What remains empirical

The empirical-inheritance demarcation is comprehensive and clean:

- **Numerical constants:** ℏ, c, m, q, α, g_s, g_w, sin²θ_W, individual Yukawa values.
- **Specific gauge group:** ED admits any compact Lie group; SM SU(3)×SU(2)×U(1) is empirical.
- **Specific Higgs mechanism:** H1, H2, H3 all admissible; specific mechanism + Higgs mass + VEV + λ all empirical.
- **Generation structure:** count, CKM, PMNS, CP phases, mass hierarchies, Yukawa matrix entries.
- **Mass values:** all per-rule-type mass values inherited via σ_τ formula's chain-initial-condition data.
- **Cosmological constant magnitude.**
- **Specific zero-point magnitudes** (Casimir, Lamb shift, anomalous moments, β-function values).

### 1.4 What was newly discovered

Beyond Phase-1's exponent-2 thread, Phase-2 newly establishes:

- **Three structural theorems (T1, T2, T3 above).**
- **Canonical (anti-)commutation FORCED** from spin-statistics + individuation (Q.7) — second quantisation derived without postulation.
- **Lightlike worldlines FORCED** for σ = 0 rule-types via dispersion-relation argument (Q.7).
- **Cl(3,1) uniqueness theorem** — neither pure commute nor pure anticommute; the anticommutator {γ^μ, γ^ν} = 2η^{μν} is structurally mandatory (R.2.4).
- **π_1(Q_2) = ℤ_2 topological theorem** — anyons forbidden in 3+1D from primitives (R.2.3).
- **Mixing matrices + CP phases FORCED-to-exist** under multi-generation + complex/non-diagonal Yukawa (Q.6 linear-algebra theorem).
- **Cosmological-constant divergence-form structurally dissolved** (Q.8).
- **Renormalisation REFUTED as fundamental requirement** (Q.8).

---

## 2. Arc R integration

### 2.1 R.1 — Scalar relativistic QM

Lorentz-covariant participation measure `P_K(x^μ) = √(b_K) · e^{iπ_K}` on (0,0) Lorentz representation. Klein-Gordon equation `(□ + m²c²/ℏ²)Ψ = 0` derived as primitive-level Casimir constraint. Minimal coupling `D_μ = ∂_μ + (iq/ℏ)A_μ` from local-phase invariance. Scalar conserved current.

**Synthesis:** [`arc_r_stage1_synthesis.md`](arc_r_stage1_synthesis.md). All structural CANDIDATEs forced or admitted-clean; numerical m, q, ℏ, c inherited.

### 2.2 R.2 — Rule-type taxonomy + spin-statistics

Five-memo sub-program (R.2.1 exchange → R.2.2 Lorentz reps → R.2.3 double-cover topology → R.2.4 Clifford → R.2.5 synthesis):

- **R.2.1:** η ∈ {+1, −1}; Case P (bosonic) vs Case R (fermionic + Pauli exclusion).
- **R.2.2:** (j_L, j_R) representation ladder; spin s ∈ {0, 1/2, 1, 3/2, 2, …} exhaustive in 3+1D.
- **R.2.3:** π_1(Q_2) = ℤ_2 from Primitive 02 + 11 + spatial dim 3; anyons forbidden; exchange-rotation generator identity.
- **R.2.4:** Cl(3,1) uniqueness; γ^μ + σ^{μν} → SL(2,ℂ); D(R(2π)) = −𝟙 automatic; 16-dim Fierz basis; FA discharged conditional on MB.
- **R.2.5:** MB discharged; **spin-statistics theorem η = (−1)^{2s} FORCED at primitive level**. No residual CANDIDATEs.

**Verdict:** R.2 is structurally complete; the spin-statistics theorem is Phase-2's first FORCED theorem (T1).

### 2.3 R.3 — Dirac emergence

Dirac equation `(iγ^μ∂_μ − mc/ℏ)Ψ = 0` FORCED as KG square-root on Cl(3,1) module. Minimal coupling extends unchanged. Conserved current `j^μ = Ψ̄γ^μΨ` with positive-definite j^0 = Ψ†Ψ (resolves KG negative-probability for Case R). **Dirac g = 2** structural prediction without tuning. NR Foldy-Wouthuysen reduction recovers Pauli equation, then Schrödinger in spinless limit (Phase-1 consistency loop closed). No CANDIDATEs opened at R.3.

### 2.4 Final Arc R verdict

Arc R closes with relativistic kinematics + dynamics for both Case P (bosonic) and Case R (fermionic) rule-types FORCED at primitive level. Numerical values (m, q, ℏ, c) inherited. The **spin-statistics theorem** is Arc R's strongest structural achievement, paralleling Phase-1's exponent-2 thread as Phase-2's first major positive structural claim.

---

## 3. Arc M integration

### 3.1 M.0 — Scoping with three hypotheses

Three candidate origin hypotheses framed: H1 (mass fully inherited), H2 (m_τ = σ_τ/c² with σ_τ a primitive bandwidth-signature invariant), H3 (mass ratios constrained by taxonomy). Honest expected-verdict distribution opened (~50% mixed / ~30% H1-dominant / ~15% H2 partial / ~5% H3-surprise).

### 3.2 M.1.x — Structural evaluation

- **M.1.1:** σ_τ master formula constructed: σ_τ = ℏ · √(Σ_X w_τ^X · ⟨(∂ ln b_τ^X)²⟩_τ). Lorentz-scalar form FORCED via selection criteria SC1–SC6; specifics CANDIDATE; values INHERITED. Three alternative functional forms explicitly rejected.

- **M.1.2:** Two structurally-admissible massless mechanisms identified: MR-R (Case R chiral, single-chirality L2 assignment) and MR-P (Case P gauge-invariant L3). Mutually exclusive per rule-type; tentatively exhaustive in 3+1D. **Existence of massless slot FORCED conditional on CANDIDATE GRH** (deferred to Arc Q at this stage).

- **M.1.3:** Six strong ratio claims (R3-A through R3-F) systematically REFUTED. H3 in equality form rejected. Three weak inequality candidates (M-Order-2, M-Order-3, M-Fierz-1) survive only as CANDIDATE producing orderings or type-classifications, not numerical ratios. Fierz class FORCED as mass-term TYPE classifier (Dirac/Majorana/pseudoscalar) but not ratio predictor.

### 3.3 M.2 — H1-dominant synthesis

H1-dominant closure: σ_τ structural form FORCED but mass values, ratios, hierarchies, generations, and massless-slot occupancy all INHERITED. M.1.4 (mass-signature identity) declined and deferred indefinitely — M.1.3's ratio refutation makes per-rule-type identity carry no comparative predictive power.

**One-line verdict:** *ED fixes the structure of mass but not its values.*

### 3.4 Back-flow from Arc Q (F-M8 promotion)

Post-Arc-Q.8 closure: with GRH unconditional FORCED, M.1.2's F-M8 (existence of at least one massless Case-P rule-type) **promotes from conditional FORCED to unconditional FORCED**. Arc M's H1-dominant verdict gains one substantive positive structural prediction: **the existence of a massless gauge rule-type is structurally forced** — ED's first unconditional "particle-class must exist" claim.

### 3.5 Final Arc M verdict

Arc M closes H1-dominant with one unconditional positive prediction (post-Arc-Q-back-flow). Most numerical mass content inherited; structural content limited to type classification (Fierz), mechanism per statistics class (MR-R / MR-P), and existence-of-massless-slot. This is the cleanest demarcation between structural prediction and empirical inheritance in ED at the mass layer.

---

## 4. Arc Q integration

### 4.1 Q.0–Q.8 structural results

Nine-substage program plus synthesis:

- **Q.0** scoping with eight structural targets (Q.1 GRH, Q.2 gauge, Q.3 vertices, Q.4 Higgs, Q.5 radiative, Q.6 generations, Q.7 second quantisation, Q.8 vacuum) and four-quadrant verdict prior.
- **Q.1** GRH evaluation — CANDIDATE-STRONG with five refinements identified.
- **Q.2** gauge-group admissibility — U(1) FORCED, SU(N) admissible, SM gauge group EMPIRICAL; R-2 closed.
- **Q.3** vertex catalogue — vector vertex FORCED, mass-like Ψ̄ΨA·A REFUTED under unbroken gauge, non-Abelian D_μ + AAA/AAAA FORCED conditional; R-3, R-4 closed.
- **Q.4** Higgs SSB scoping — H1 ADMISSIBLE-CLEAN, H2 CANDIDATE, H3 ADMISSIBLE-EFFECTIVE, H4 REFUTED, H5 deferred. ED admits multiple SSB routes; specific mechanism EMPIRICAL.
- **Q.5** radiative corrections — loop structure form-level admissible; tree-level g = 2 preserved; only Fierz tensor σ^{μν} contributes to anomalous magnetic moment FORCED; UV-FIN CANDIDATE opened.
- **Q.6** generations + flavour — six mechanisms evaluated; G1 ADMISSIBLE-CLEAN (rule-type duplication); G2/G3/G5 REFUTED; G4 deferred; generation count = 3 EMPIRICAL; mixing matrices + CP phases FORCED-to-exist by linear-algebra under multi-gen + non-diag/complex Yukawa.
- **Q.7** second quantisation — multi-chain field FORCED; canonical (anti-)commutation FORCED from R.2.5 + Primitive 10; R-1 closed via dispersion relation; R-5 partial; UV-FIN promoted to CANDIDATE-STRONG.
- **Q.8** vacuum — R-5 fully closed; **GRH unconditional FORCED**; **UV-FIN FORCED**; H5 reduces to H1/H2; G4 REFUTED-as-mass-differentiation; cosmological-Λ divergence-form dissolved.

### 4.2 Three Arc Q FORCED theorems

**(T2) GRH unconditional FORCED.** All five refinements closed across Q.2/Q.3/Q.7/Q.8. ED's first "particle-class must exist" prediction.

**(T3) UV-FIN FORCED at primitive level.** Three-step argument from Primitive 01 + 13 + 04. Renormalisation REFUTED as fundamental.

**Plus canonical (anti-)commutation FORCED** (Q.7 §3.4) — second quantisation derived directly from R.2.5 + Primitive 10.

### 4.3 Final Arc Q verdict

Arc Q lands in the 30% mostly-positive quadrant of Q.0's prior. Strong positive content: GRH FORCED, UV-FIN FORCED, canonical (anti-)commutation, vertex catalogue, mixing/CP linear-algebra theorems, lightlike worldlines, vacuum-particle dual structure. Strong negative content: SM gauge group empirical, specific Higgs mechanism non-canonical, generation count empirical, all numerical values inherited.

**One-line verdict:** *ED yields a structurally complete, UV-finite quantum field framework whose form is forced but whose numerical content is inherited.*

Synthesis: [`arc_q_synthesis.md`](arc_q_synthesis.md).

---

## 5. Phase-2 master FORCED / CANDIDATE / REFUTED / INHERITED table

### 5.1 Per-layer

| Layer | FORCED | CANDIDATE | REFUTED | INHERITED |
|-------|--------|-----------|---------|-----------|
| **Kinematics (R.1)** | Lorentz-cov P_K; KG eq; Casimir P²= m²c² | — | KG negative-prob for Case R (Dirac fixes) | m, c |
| **Spin-statistics (R.2)** | η = (−1)^{2s}; (j_L, j_R) ladder; π_1 = ℤ_2; Cl(3,1) uniqueness; SL(2,ℂ) | — | Anyons in 3+1D | Specific s per rule-type |
| **Dynamics (R.3)** | Dirac eq; gauge-cov D_μ; j^μ = Ψ̄γ^μΨ; tree-level g = 2; NR Pauli/Schrödinger | — | — | m, q, ℏ |
| **Mass structure (Arc M)** | σ_τ Lorentz-scalar form; MR-R/MR-P admissibility; Fierz TYPE classifier; **F-M8 (post-Q back-flow)** | M-Order-2/3, M-Fierz-1, σ_τ specifics | Six R3-A/B/C/D/E/F ratio claims; mass hierarchies derivable; G2/G3/G5 generation mechanisms | All m_τ; w_τ^X; Γ_τ; ratios; hierarchies |
| **Gauge structure (Q.2)** | U(1) at primitive level; compact-Lie-group admissibility; non-Abelian D_μ uniqueness | CC-U1 (charge quantisation) | SM gauge group as forced; non-compact gauge groups | Specific gauge group; q values |
| **Vertices (Q.3)** | Vector vertex (U(1)); non-Abelian D_μ + AAA/AAAA; locality + gauge-invariance filter; vertex-anchored commitment | Tensor / axial / pseudoscalar (rule-type data) | Mass-like Ψ̄ΨA·A under unbroken gauge; non-local/non-scalar/anyonic | Specific couplings per rule-type |
| **SSB (Q.4)** | Default massless gauge; SSB admissibility; Goldstone absorption; photon survival under partial SSB | H1, H2, H3 occupants | H4 (gauge-fixing artefact); H5 as distinct; ED forces specific Higgs | Higgs mass, VEV, λ; Yukawa values; SSB pattern |
| **Radiative (Q.5)** | Loop admissibility; vacuum-pol transversality; tree-level g = 2 preserved; only σ^{μν} contributes to a_μ | Schwinger sign; asymptotic-freedom sign | Specific numerical coefficients forced; loops violating gauge/Lorentz/locality | All numerical loop content; β-function values; anomalous moments |
| **Generations (Q.6)** | Multi-gen admissibility; flavour-changing vertex admissibility; **mixing matrices forced under multi-gen + non-diag Yukawa**; **CP phases forced under complex Yukawa + ≥3 gen** | G4 as labelling | Generation count = 3 forced; G2/G3/G5; G4 as mass-differentiation; mass hierarchies | Generation count; CKM; PMNS; CP phase values; Yukawa values |
| **Second quantisation (Q.7)** | **Multi-chain field structure**; vacuum as no-commitment; create/annihilate from threshold-crossings; **canonical (anti-)commutation**; **lightlike worldlines for σ = 0** | Multiple vacuum sectors | Anyonic statistics in 3+1D | Specific Fock occupations |
| **Vacuum (Q.8)** | Vacuum factorisation ⊗_τ; Lorentz + gauge invariance; effective b^env content; Λ-as-finite | Stable vacuum sectors; Schwinger-sign carryover | H5 as distinct; G4 as mass-differentiation; **renormalisation as fundamental**; specific Λ value | Λ magnitude; specific zero-point magnitudes |
| **GRH** | **UNCONDITIONAL FORCED** | — | — | — |
| **UV-FIN** | **FORCED at primitive level** | — | Renormalisation as fundamental requirement | Numerical content of any specific divergence-cancellation |

### 5.2 Phase-2 headline-result hierarchy

**Three FORCED structural theorems:**

1. **Spin-statistics theorem η = (−1)^{2s}** — R.2.5
2. **GRH unconditional FORCED** — Q.1 + Q.2/3/7/8 (closure at Q.8)
3. **UV-FIN FORCED at primitive level** — Q.8

**Plus seven supporting FORCED structural results:**

- Canonical (anti-)commutation (Q.7).
- Lightlike worldlines for σ = 0 (Q.7).
- Cl(3,1) uniqueness theorem (R.2.4).
- π_1 = ℤ_2 / anyon prohibition (R.2.3).
- Cosmological-Λ divergence-form dissolution (Q.8).
- F-M8 promotion to unconditional FORCED (post-Q.8 back-flow).
- Mixing/CP existence theorems (Q.6).

---

## 6. Dependency map

```
                   Phase-1 (Schrödinger, Born, Bell, Heisenberg)
                                    │
                                    ▼
                   Stage R.1 (Lorentz-cov P, KG, minimal coupling, j^μ scalar)
                                    │
                                    ▼
                   Stage R.2 (rule-type taxonomy)
                  ┌─────────────────┼─────────────────┐
                  ▼                 ▼                 ▼
                R.2.1            R.2.2-3-4         R.2.5
              (exchange)      (reps + topo + Cl)  (spin-statistics theorem)
                  │                 │                 │
                  └─────────────────┴─────────────────┘
                                    │
                                    ▼
                   Stage R.3 (Dirac + g = 2 + Pauli/Schrödinger)
                                    │
                                    ▼
                          Arc R synthesis
                                    │
                                    ▼
                   Arc M Stage M.0 (scoping)
                                    │
                                    ▼
                   Arc M Stages M.1.1, M.1.2, M.1.3
                                    │
                                    ▼
                   Arc M Stage M.2 (H1-dominant synthesis)
                                    │
                                    ▼
                   Arc Q Stage Q.0 (scoping; eight substage targets)
                                    │
                                    ▼
                   Arc Q Stage Q.1 (GRH evaluation; five refinements opened)
                  ┌─────────────────┼─────────────────┐
                  ▼                 ▼                 ▼
                Q.2                Q.3                Q.7
            (gauge group;       (vertices;         (2nd quant;
             R-2 closed)        R-3+R-4 closed)    R-1 closed; R-5 partial)
                  │                 │                 │
                  ▼                 ▼                 ▼
                Q.4               Q.5                Q.8
            (Higgs SSB)        (radiative;        (vacuum; R-5 closed;
                              UV-FIN opens)       UV-FIN FORCED;
                                                  GRH unconditional FORCED)
                  │                 │                 │
                  └─────────────────┼─────────────────┘
                                    │
                                    ▼
                                  Q.6
                              (generations)
                                    │
                                    ▼
                          Arc Q synthesis
                                    │
                                    ▼
                  ┌─── Back-flow to Arc M ───┐
                  ▼                           ▼
            F-M8 unconditional         M.2 H1-dominant
            FORCED                     verdict updated
                                    │
                                    ▼
                ┌─── Phase-2 Global Synthesis (this memo) ───┐
                                    │
                                    ▼
                  Phase-3 unblocked: ED → GR coupling;
                  cosmological structure; UV-FIN empirical signatures;
                  external write-up; platform-bridge derivations
```

### 6.1 Refinement closure timeline

| Refinement | Source | Closed at |
|-----------|--------|-----------|
| FA (frame-availability) | R.2.3 | R.2.4 (via Cl(3,1)) |
| MB (minimal bilinear) | R.2.4 | R.2.5 (via Primitive 10) |
| Mλ (massless ⟺ no commitment + no internal evolution) | M.1.1 | Standing CANDIDATE |
| GRH (gauge-field-as-rule-type) | M.1.2, Q.1 | **Q.8 (unconditional FORCED)** |
| R-1 (lightlike-worldline) | Q.1 | Q.7 |
| R-2 (gauge-quotient individuation) | Q.1 | Q.2 |
| R-3 (vertex-anchored commitment) | Q.1 | Q.3 |
| R-4 (non-Abelian extension) | Q.1 | Q.3 |
| R-5 (vacuum/particle status) | Q.1 | Q.8 |

Phase-2 closes with **all major CANDIDATEs discharged or carrying-over only as standing-CANDIDATE-with-no-blocking-content** (Mλ, charge-quantisation CC-U1, Schwinger-sign, asymptotic-freedom-sign).

### 6.2 Cross-arc back-flows

- **R.2.5 → Q.7:** spin-statistics enables canonical (anti-)commutation FORCED.
- **R.1 → Q.7:** Casimir P² = m²c² enables R-1 closure.
- **R.2.4 → Q.3:** Cl(3,1) Fierz basis enables vertex catalogue.
- **R.1 → Q.3:** minimal coupling enables U(1) vector vertex FORCED.
- **M.1.2 → Q.1:** MR-P + GRH conditional → unconditional FORCED via Q.8.
- **Q.8 → Arc M:** F-M8 promotion (back-flow).
- **R.2.3 → Q.7/Q.8:** anyon prohibition carries forward to vacuum structure.

---

## 7. Arc N status (parallel thread)

Arc N (non-Markovian memory-kernel extensions for platform-specific phenomenology) is independent of Arc R / M / Q at primitive level. It uses inherited masses directly via Stage R.1 / R.3 mass terms; no Phase-2 closure required. Arc N remains active as a parallel research thread, ties into Q.7 second quantisation at the QFT level, and supplies phenomenological corrections for platform-bridge derivations.

Arc N is not closed by Phase-2 synthesis; it continues independently.

---

## 8. Phase-2 closure statement

### 8.1 What Phase-2 establishes

ED's quantum sector is **structurally complete and UV-finite**:

- **Kinematics:** Lorentz-covariant participation measure on (j_L, j_R) representations; KG (spin-0) and Dirac (spin-1/2) equations FORCED.
- **Spin-statistics:** η = (−1)^{2s} FORCED at primitive level; anyons forbidden in 3+1D.
- **Dynamics:** minimal-coupling gauge interactions FORCED; conserved currents structural; tree-level g = 2.
- **Mass structure:** σ_τ Lorentz-scalar form FORCED; values inherited; type classification by Fierz; massless slot existence unconditional FORCED via GRH.
- **Field structure:** multi-chain fields, canonical (anti-)commutation, Fock-space construction all FORCED.
- **Gauge structure:** any compact Lie group admissible; U(1) FORCED; SM-specific empirical.
- **Vertex structure:** classified via Fierz basis; gauge-invariance filter active.
- **SSB:** multiple admissible mechanisms (H1, H2, H3); specific mechanism empirical.
- **Vacuum:** vacuum-particle dual structure FORCED; effective vacuum content well-defined; Lorentz + gauge invariant.
- **UV behaviour:** UV-FIN FORCED — primitive-level finiteness of all multi-chain participation integrals; renormalisation REFUTED as fundamental; cosmological-Λ divergence-form dissolved.

### 8.2 What Phase-2 does not establish

Phase-2 does not predict:
- Any specific numerical constant of nature.
- Any specific particle mass, ratio, or hierarchy.
- The Standard-Model gauge group SU(3)×SU(2)×U(1).
- The number of fermion generations.
- Specific coupling-constant values.
- The Higgs mechanism choice or parameters.
- The cosmological-constant magnitude.
- The hierarchy problem resolution.

These are demarcated INHERITED. The form-FORCED / value-INHERITED separation is the **canonical Phase-2 methodological framing**.

### 8.3 Phase-2 closure verdict

**Phase-2 closes as structurally complete.** ED now has a structurally complete, UV-finite quantum sector spanning non-relativistic + relativistic + field-level + mass-structure + gauge + vertex + SSB + radiative + generations + second-quantisation + vacuum content. Form is forced; numerical content is inherited.

**Phase-3 unblocked.**

### 8.4 Phase-3 directions

With Phase-2 closed, the natural Phase-3 directions:

1. **ED → GR coupling.** UV-FIN's reframing of cosmological-Λ divergence-form opens the route to coupling ED's quantum sector with general-relativistic structure. The ED-Phys-10 kinematic acoustic-metric arc (closed 2026-04-22) provides the kinematic-curvature foundation; Phase-3 could investigate whether ED admits dynamical curvature / gravitational coupling at primitive level.

2. **Cosmological structure.** Λ admissible-as-finite under UV-FIN; Phase-3 could investigate primitive-level structure determining cosmological scales (without predicting specific values, but mapping which structural choices fix which cosmological observables).

3. **UV-FIN empirical signatures.** Possible high-energy phenomenology near primitive event-discreteness scale. Detectable deviations from continuum-QFT predictions would be Phase-3 empirical signatures.

4. **Platform-bridge derivations.** Now armed with full QFT-extension structure post-Arc-Q. Each experimental platform (matter-wave, SC qubit, optomech, BEC, cavity QED, cosmological) can be given dedicated bridge memos using the Phase-2 structural framework.

5. **External academic write-up.** Phase-2 closure is suitable for publication as the structural-foundations companion to Phase-1's QM-emergence paper. Three structural theorems (T1 spin-statistics, T2 GRH, T3 UV-FIN) constitute publishable headline results.

6. **Open derivations:** Schwinger-sign (CANDIDATE-PLAUSIBLE); CC-U1 charge quantisation; asymptotic-freedom sign — all standing as future work without blocking Phase-2 closure.

### 8.5 Memo inventory at Phase-2 close

**32 memos in `quantum/foundations/` post-Phase-2-synthesis** (this memo brings the count to 32):

- **Phase-1 (12):** participation_measure, schrodinger_emergence, born_rule_from_participation, bell_correlations_from_participation, uncertainty_from_participation, qm_emergence_synthesis, candidate_to_forced_program, u3_evolution_derivation, u5_adjacency_partition_derivation, u4_hamiltonian_form_derivation, phase_independence_derivation, qm_emergence_closure.
- **Arc R (11):** klein_gordon_emergence, kg_minimal_coupling_and_current, relativistic_participation_measure, arc_r_stage1_synthesis, rule_type_taxonomy, rule_type_exchange_symmetry, lorentz_representations_from_primitives, rotational_double_cover_scoping, clifford_algebra_from_spinor_structure, rule_type_taxonomy_synthesis, dirac_emergence.
- **Arc M (5):** chain_mass_scoping, bandwidth_signature_construction, massless_rule_types, mass_ratio_constraints, chain_mass_synthesis.
- **Arc Q (10):** qft_extension_scoping, grh_evaluation, gauge_group_scoping, interaction_vertex_classification, higgs_mechanism_scoping, radiative_corrections, generations_and_mixing, second_quantisation, vacuum_and_zero_point, arc_q_synthesis.
- **Phase-2 supporting (3):** phase2_extensions_roadmap, hbar_origin, memory_kernel_derivation.
- **Phase-2 synthesis (1):** **phase2_synthesis (this memo)**.

Plus extensive supporting memos in `quantum/primitives/`, `quantum/effective_theory/`, `quantum/retrodictions/` (not counted here).

---

## 9. Cross-references

- Phase-1 closure: [`qm_emergence_closure.md`](qm_emergence_closure.md), [`qm_emergence_synthesis.md`](qm_emergence_synthesis.md).
- Arc R synthesis: [`arc_r_stage1_synthesis.md`](arc_r_stage1_synthesis.md), [`rule_type_taxonomy_synthesis.md`](rule_type_taxonomy_synthesis.md), [`dirac_emergence.md`](dirac_emergence.md).
- Arc M synthesis: [`chain_mass_synthesis.md`](chain_mass_synthesis.md).
- Arc Q synthesis: [`arc_q_synthesis.md`](arc_q_synthesis.md).
- Phase-2 supporting: [`phase2_extensions_roadmap.md`](phase2_extensions_roadmap.md), [`hbar_origin.md`](hbar_origin.md), [`memory_kernel_derivation.md`](memory_kernel_derivation.md).
- Memory: [`memory/project_qm_emergence_arc.md`](../../.claude/projects/C--Users-allen-GitHub-Event-Density/memory/project_qm_emergence_arc.md).
- Orientation: [`docs/ED-Orientation.md`](../../docs/ED-Orientation.md).
- Accomplishments: [`docs/ED_Accomplishments.md`](../../docs/ED_Accomplishments.md).

---

## 10. One-line summary

**Phase-2 closes ED's quantum sector with three FORCED structural theorems (spin-statistics η = (−1)^{2s}; GRH unconditional FORCED; UV-FIN FORCED at primitive level), seven supporting FORCED structural results (canonical (anti-)commutation, lightlike worldlines, Cl(3,1) uniqueness, anyon prohibition, cosmological-Λ divergence-form dissolution, F-M8 unconditional, mixing/CP existence theorems), and clean form-FORCED / value-INHERITED demarcation across all numerical content (constants, masses, gauge group, generations, Higgs, Λ) — yielding a structurally complete, UV-finite quantum field framework whose form is forced but whose numerical content is inherited, unblocking Phase-3 (ED → GR coupling, cosmological structure, UV-FIN empirical signatures, platform bridges, external write-up).**
