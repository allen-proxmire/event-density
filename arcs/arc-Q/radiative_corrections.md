# Radiative Corrections

**Stage Q.5 — Arc Q Sub-Memo**
**Status:** Evaluation memo. Headline verdict: **Loop-level structure is structurally ADMISSIBLE in ED via multi-chain commitment dynamics — vacuum polarisation, self-energy, vertex corrections, and running couplings all have primitive-level realisations as effective consequences of multi-chain participation. g = 2 FORCED at tree level (Stage R.3); deviations g − 2 ≠ 0 are structurally admissible but their numerical magnitude (α/2π + …) is INHERITED from QFT machinery. Sign of g − 2 is structurally CANDIDATE — Schwinger sign at one loop is plausible but not derived. UV-divergent structures are not directly produced by ED primitives but appear as effective approximations to multi-chain commitment dynamics; renormalisation is admissible but not structurally novel. Q.5 closes with form-level FORCED, value-level INHERITED — the Arc Q pattern again.**

---

## 1. Goal

Stages Q.1–Q.4 closed the tree-level / form-level Arc Q content: GRH structure (Q.1), gauge-group admissibility (Q.2), vertex catalogue (Q.3), Higgs scoping (Q.4). Three of five GRH refinements closed; R-1 and R-5 remain (Q.7/Q.8 deliverables).

Stage Q.5 evaluates **loop-level / radiative-correction** content. The driving questions:

(Q-Rad.1) Does ED's multi-chain participation structure admit a primitive-level analogue of QFT loop corrections?
(Q-Rad.2) Is the Stage R.3 Dirac g = 2 prediction stable under structural extension, or do deviations g − 2 ≠ 0 emerge?
(Q-Rad.3) Does ED admit running couplings (scale-dependent effective interactions), and if so, are β-functions structural or inherited?
(Q-Rad.4) Are UV divergences a feature of ED, or are they artefacts of QFT approximation to underlying multi-chain dynamics?
(Q-Rad.5) Can ED constrain the sign / magnitude of any specific radiative correction (e.g., Schwinger sign for g − 2)?

This memo evaluates these without computing numerical values — Q.5's role is structural admissibility / forcing, not numerical reproduction. Numerical content (α-expansion coefficients, running-coupling β-function values, anomalous-moment magnitudes) is uniformly INHERITED from QFT machinery built on the Q.3 vertex catalogue.

---

## 2. Inputs

### 2.1 From Q.1–Q.4

- GRH CANDIDATE-STRONG; R-3, R-4 closed; R-1, R-5 deferred.
- U(1) FORCED; SU(N) admissible.
- Vertex catalogue from Q.3: vector vertex FORCED, axial / tensor / pseudoscalar admissible, mass-like REFUTED under unbroken gauge.
- Higgs SSB: H1, H2, H3 admissible structurally; specific mechanism EMPIRICAL.

### 2.2 From Stage R.3

- Dirac equation (iγ^μ∂_μ − mc/ℏ)Ψ = 0 with j^μ = Ψ̄γ^μΨ.
- Pauli-equation NR reduction yields g = 2 (Foldy-Wouthuysen at lowest order).
- This is the **tree-level** Dirac prediction.

### 2.3 From Stages Q.0 and M.2

- Q.0 §3.5 expectation: g − 2 ≈ α/π + … is INHERITED via Q.7 second-quantisation framework.
- M.2: form-level FORCED, values INHERITED — paralleling pattern.

---

## 3. The structural problem

### 3.1 What "loop correction" means in rule-type ontology

QFT loops are calculated as integrals over virtual-particle four-momenta in Feynman diagrams with closed loops. In ED's rule-type ontology, the analogue is:

**Multi-chain participation interference at vertices.** A primary chain K of rule-type τ interacts at a vertex; commitment events at that vertex involve not just K but also virtual chains of other rule-types τ' that participate transiently in the bandwidth content around the vertex. These transient participations modify the effective vertex amplitude — this is the ED analogue of loop corrections.

Specifically:

- **Self-energy correction:** chain K of rule-type τ propagates through a region where other τ-chains transiently participate via individuation pairing (Primitive 10), shifting the effective σ_τ along its worldline.
- **Vertex correction:** at an interaction vertex involving chains of rule-types τ and τ_g, transient participations of additional chains modify the effective coupling.
- **Vacuum polarisation:** the gauge rule-type τ_g propagating between two vertices encounters transient charged-rule-type pairs in its bandwidth-environment band b^env, producing effective polarisation of the gauge-field amplitude.

These are not new primitives; they are consequences of Primitives 04 (four-band, including b^env), 10 (multi-chain pairing), and 11 (vertex-localised commitment) acting jointly.

### 3.2 Why this is a structural-admissibility, not derivation, question

ED primitives admit multi-chain participation. Whether the **specific numerical coefficients** (α/π for QED vertex correction, 11N/3 − 2N_f/3 for SU(N) β-function, etc.) emerge from primitives is a different question. Q.5's claim is the weaker one: ED structurally **admits** the form of loop corrections; the numerical content is inherited from QFT.

This parallels Arc M and Q.4: ED gives the *form*, inherits the *values*.

### 3.3 Sub-question structure

Q.5 decomposes into:

- (S1) Self-energy corrections: structurally admissible? FORCED to exist?
- (S2) Vacuum polarisation: structurally admissible?
- (S3) Vertex corrections: structurally admissible?
- (S4) Running couplings: structurally admissible?
- (S5) g − 2 deviation: structurally admissible? Sign predictable?
- (S6) UV behaviour: divergent / finite? Renormalisation structural?

---

## 4. Sub-question evaluations

### 4.1 (S1) Fermion self-energy corrections

**ED realisation.** A Case-R chain K with participation Ψ_τ propagates along its worldline γ_K. Along γ_K, the chain interacts with the bandwidth environment via b^{env}, which includes transient contributions from other rule-types' bandwidth content. These shift the effective σ_τ along γ_K from its bare value σ_τ^{(0)} to a renormalised σ_τ^{(R)}.

In QFT terms, this is the fermion self-energy Σ(p) shifting the bare mass m to a renormalised m^{(R)}.

**Primitive evaluation.**

- **Primitive 04:** b^{env} is a primitive band, structurally well-defined. **Compatible.**
- **Primitive 11:** commitment events along γ_K accumulate environment-band contributions. **Compatible.**
- **Stage R.3:** Dirac mass term mc/ℏ is a parameter; structurally the mass parameter is inherited (Arc M closure). Self-energy shifts the parameter without changing the form of the equation. **Compatible.**

**Status:** **ADMISSIBLE. FORCED to exist whenever multi-chain b^{env} content is present** (which it always is in physical situations — there is no isolated single-chain in ED's primitive ontology).

Numerical magnitude inherited from QFT.

### 4.2 (S2) Gauge-boson vacuum polarisation

**ED realisation.** A gauge rule-type τ_g propagating between two vertices on a lightlike worldline interacts with the local bandwidth-environment band b^{env}_{τ_g}, which includes virtual charged-rule-type-pair participations.

In QFT terms, this is the photon self-energy Π_{μν}(q) inducing the running of α(q²).

**Primitive evaluation.**

- **Primitive 04 + 10:** virtual charged-rule-type participation in τ_g's environment band is structurally admissible (any rule-type can transiently participate in another's environment). **Compatible.**
- **Q.3 vertex:** the vector vertex Ψ̄γ^μΨ A_μ is the structural slot for the τ_g — charged-pair coupling. **Compatible.**
- **GRH-3:** gauge invariance must be preserved by polarisation tensor — Π^{μν}(q) must be transverse, q_μ Π^{μν} = 0. This is a Ward-identity-analogue at primitive level: gauge invariance of the L3 interface forces the polarisation tensor to be transverse. **FORCED transversality.**

**Status:** **ADMISSIBLE.** Transversality FORCED by GRH-3. Numerical value of polarisation coefficient INHERITED.

### 4.3 (S3) Vertex corrections (triangle, box)

**ED realisation.** Multi-chain interference at a vertex point involving more than the minimal vertex structure. Triangle diagrams (three vertices, one closed loop) and box diagrams (four vertices) are higher-order multi-chain participation patterns.

**Primitive evaluation.**

- **Primitive 11 vertex-locality:** vertices remain point-local; multi-vertex interference is admissible as long as each vertex is itself local. **Compatible.**
- **Q.3 vertex catalogue:** triangle-loop content uses three insertions of admissible Q.3 vertices. No new vertex types required. **Compatible.**
- **Anomalies:** the triangle diagram with chiral fermion loop produces the ABJ anomaly. Whether ED reproduces this structurally depends on its treatment of γ^5 in the spinor module. Standard Cl(3,1) γ^5 algebra is preserved (R.2.4); the anomaly is a consequence of regularisation choice in QFT, expected INHERITED at numerical level.

**Status:** **ADMISSIBLE.** Anomaly content (ABJ, gauge anomalies) INHERITED at numerical level; its structural origin via γ^5 trace identities is admitted by R.2.4 framework.

### 4.4 (S4) Non-Abelian running couplings

**ED realisation.** For SU(N) gauge rule-types, the coupling constant g effectively varies with energy scale due to vacuum polarisation contributions from charged matter and gauge-self-coupling.

**Primitive evaluation.**

- **Q.2 + Q.3:** SU(N) admissible; non-Abelian self-couplings AAA, AAAA FORCED conditional on SU(N) admittance.
- **(S2) + (S3):** vacuum polarisation contributions admissible.
- **Asymptotic freedom (β < 0 for SU(3) in QCD):** specific sign of β-function depends on relative contributions of gauge-self-coupling vs matter loops. ED admits both contributions structurally; the **net sign** is the standard 11N/3 − 2N_f/3 calculation, which is a numerical / inherited result.

**Status:** **ADMISSIBLE.** Sign of β-function INHERITED (asymptotic freedom is a numerical QFT result, not structural primitive content).

### 4.5 (S5) g − 2 deviation

**ED realisation.** Stage R.3 forces g = 2 at tree level via the Cl(3,1) frame and Pauli-equation NR reduction. Vertex corrections (S3) modify the effective magnetic-moment coupling at next order.

**Primitive evaluation.**

- **R.3 g = 2 tree-level:** FORCED. (`dirac_emergence.md` §5.3.)
- **Vertex correction admissibility:** §4.3 above. ADMISSIBLE.
- **Tensor (Pauli-moment) vertex Ψ̄σ^{μν}Ψ F_{μν}:** Q.3 §4.2.3 ADMISSIBLE as effective vertex. This is the structural slot for anomalous magnetic moment.

**Sign of g − 2:** at one loop in QED, Schwinger's calculation gives g − 2 = α/(2π) > 0. This comes from the specific sign structure of the photon-electron-photon vertex correction integral. ED admits the structural form but does not derive the sign at primitive level — the sign emerges from QED loop-integral structure, which is QFT machinery inherited via Q.7.

**Magnitude:** α/(2π) ≈ 0.00116 reproduced empirically to 12 decimal places by QED. Pure QFT result; ED INHERITS numerical content.

**Status:** **g = 2 FORCED at tree level (R.3). Deviation g − 2 ≠ 0 ADMISSIBLE structurally. Sign and magnitude INHERITED.**

### 4.6 (S6) UV behaviour and renormalisation

**ED realisation.** ED's primitive structure is built on a discrete event-manifold ontology with finite primitive content per event (Primitive 01 micro-event discreteness, Primitive 13 relational timing). Continuum approximations to multi-chain participation may produce UV-divergent integrals when treated naively, but the underlying ED structure has natural UV cutoff at the primitive event-discreteness scale.

**Primitive evaluation.**

- **Primitive 01 (discrete micro-events):** suggests primitive-level UV cutoff. ED's "loops" as multi-chain commitment events are discrete and finite; they produce divergent integrals only in the continuum approximation.
- **Primitive 13 (relational timing):** proper-time intervals are well-defined; no infinite-energy events at primitive level.
- **Renormalisation in QFT:** standard machinery (regularisation, counterterms, β-functions) is the inherited continuum-approximation framework. ED does not require renormalisation at primitive level (no divergences); inherits it as the effective-theory machinery.

**Status:** **ADMISSIBLE-as-effective.** ED's primitive structure is naively UV-finite; renormalisation is inherited as approximation machinery, not as a primitive-level requirement.

This is a structurally interesting claim: **ED suggests UV divergences are artefacts of continuum approximation, not fundamental.** Whether this can be made rigorous (i.e., demonstrating finite primitive-level multi-chain integrals) is a Q.7 / Q.8 deliverable.

---

## 5. Structural form of the anomalous magnetic moment

### 5.1 Tree-level structure

From Stage R.3, the magnetic-moment operator emerges from the Pauli reduction:

  Ĥ_Zeeman = − (qℏ / 2m) σ · B = − (g / 2)(qℏ / 2m_e) σ · B,                  (1)

with **g = 2 at tree level** from the Dirac equation's Cl(3,1) frame structure.

### 5.2 Loop-level structural form

Vertex correction (S3) contributes an effective tensor-bilinear interaction:

  ΔL_eff = (a / 2)(q / 2m) Ψ̄ σ^{μν} Ψ F_{μν},                                  (2)

where a is the anomalous-magnetic-moment coefficient. Equation (2) is the Pauli-moment effective vertex (Q.3 §4.2.3, ADMISSIBLE-as-effective).

The full magnetic moment becomes g/2 = 1 + a, i.e., g = 2(1 + a) = 2 + 2a, so

  g − 2 = 2a.                                                                  (3)

This is the structural form. ED admits it cleanly. Numerical value of a is QFT loop calculation: a_QED^{(1-loop)} = α/(2π); higher orders α², α³, …; plus electroweak and hadronic contributions.

### 5.3 Which Fierz bilinears contribute to g − 2?

From Q.3 vertex catalogue:

| Bilinear | Contribution to g − 2 |
|----------|----------------------|
| Ψ̄γ^μΨ A_μ (vector) | tree-level g = 2; not a deviation source itself |
| Ψ̄σ^{μν}Ψ F_{μν} (tensor) | **DIRECT** source of a (Pauli moment) |
| Ψ̄γ^μγ^5Ψ A_μ (axial) | EDM-type contribution (electric dipole moment, CP-violating); not g − 2 |
| Ψ̄γ^5Ψ pseudoscalar | EDM-type; not g − 2 |

**FORCED:** Only the tensor bilinear σ^{μν} contributes to anomalous *magnetic* moment. Axial / pseudoscalar contribute to electric dipole moment (CP-violating quantity, currently consistent with zero empirically).

### 5.4 Can ED constrain sign or magnitude of g − 2?

**Magnitude:** No. Specific numerical value of a is QFT loop-integral content, INHERITED.

**Sign at one loop:** ED admits both signs structurally — the σ^{μν} F_{μν} bilinear is sign-indefinite. Schwinger's positive sign in QED comes from the photon-charged-fermion vertex topology and propagator iε prescriptions, which are QFT machinery. ED's R.3 framework is consistent with the positive sign but does not derive it at primitive level.

**Status:** **CANDIDATE for sign-prediction at one loop** — possibly recoverable via careful Q.7 second-quantisation analysis with vertex topology, but currently INHERITED.

---

## 6. FORCED / CANDIDATE / REFUTED table

### 6.1 Per-correction-type

| Correction | Status |
|-----------|--------|
| Fermion self-energy (S1) | **ADMISSIBLE; FORCED to exist** when b^env active |
| Gauge-boson vacuum polarisation (S2) | **ADMISSIBLE**; transversality **FORCED** by gauge invariance |
| Vertex corrections (S3) triangle / box | **ADMISSIBLE** |
| ABJ-type anomalies | **ADMISSIBLE** structurally; numerical content INHERITED |
| Non-Abelian running couplings (S4) | **ADMISSIBLE**; sign of β INHERITED |
| g = 2 tree-level | **FORCED** (R.3) |
| g − 2 deviation existence | **ADMISSIBLE** (Pauli-moment vertex) |
| g − 2 sign at one loop | **CANDIDATE** (Schwinger sign plausible; not derived) |
| g − 2 magnitude | **INHERITED** (QFT loop content) |
| Higgs-loop contributions | **ADMISSIBLE** if H1 occupied (Q.4) |
| Loop-induced mass shifts | **ADMISSIBLE** (S1 carryover) |
| UV divergences | **NOT FORCED** by primitives; arise as continuum-approximation artefacts |
| Renormalisation as effective machinery | **ADMISSIBLE** as approximation tool |

### 6.2 Per-structural-claim

| Claim | Status |
|-------|--------|
| Loops are admissible structurally | **FORCED** |
| Loops are forced to exist in physical situations | **FORCED** (b^env always active) |
| Specific β-function coefficients | **INHERITED** |
| Specific anomalous-magnetic-moment coefficients | **INHERITED** |
| ED forces UV-finiteness at primitive level | **CANDIDATE** (Primitive 01 discreteness suggests it) |
| ED forces renormalisability | NOT FORCED — admitted as approximation |
| ED predicts asymptotic freedom for SU(3) | **REFUTED as structural prediction**; INHERITED |
| ED predicts QED running of α | **REFUTED as structural prediction**; INHERITED |

---

## 7. Renormalisation-like behaviour

### 7.1 Scale-dependent effective couplings

Yes, structurally admissible. Scale dependence arises because multi-chain participation contributions to a coupling depend on the bandwidth-environment content at the relevant scale. At higher energies, more rule-types are participating in b^env; effective couplings shift.

This is a structurally-clean ED realisation of running couplings. **ADMISSIBLE.**

### 7.2 Logarithmic corrections

QFT one-loop corrections produce log(Q²/μ²) factors (running coupling logarithms). ED admits these as effective summaries of multi-chain participation contributions integrated over scales. The log structure emerges from the continuum approximation of discrete multi-chain integrations.

**ADMISSIBLE-as-effective.** Structurally not novel — log structure is inherited.

### 7.3 UV-finite vs UV-divergent structures

A genuine ED prediction worth flagging:

**(CANDIDATE UV-FIN)** ED's primitive event-manifold discreteness (Primitive 01) provides a natural UV cutoff. Multi-chain participation integrals at primitive level are finite. UV divergences in QFT are continuum-approximation artefacts; they should be replaced by **finite contributions at the primitive event-discreteness scale** when ED is treated rigorously.

This is a **structurally meaningful** claim that distinguishes ED from continuum QFT. Whether it can be made rigorous (deriving finite multi-chain integrals from primitive event-discreteness) is a Q.7 / Q.8 deliverable.

If CANDIDATE UV-FIN closes affirmatively, ED would offer a **primitive-level resolution of QFT's UV problems** without renormalisation — possibly a strong positive structural result. If it does not close, renormalisation remains the inherited approximation framework.

---

## 8. Verdict

### 8.1 What is structurally FORCED?

- Multi-chain participation produces effective corrections to single-chain dynamics.
- Self-energy corrections exist whenever b^env is active.
- Gauge-boson vacuum-polarisation transversality (Ward-identity-analogue) FORCED by GRH-3.
- g = 2 at tree level (R.3 carry-forward).
- Only the tensor Fierz bilinear σ^{μν} contributes to anomalous magnetic moment.

### 8.2 What is admissible but not forced?

- Specific numerical content of any radiative correction.
- Sign of g − 2 at one loop (CANDIDATE for Q.7 derivation).
- ABJ anomaly numerical structure.
- Asymptotic freedom for SU(3).
- Schwinger sign for QED vertex correction.
- UV-finite primitive-level multi-chain integrals (CANDIDATE UV-FIN).
- Higgs loops, two-loop EW, hadronic contributions.

### 8.3 What is forbidden?

- Loop-induced violation of gauge invariance (transversality FORCED by GRH-3).
- Loop-induced violation of Lorentz covariance.
- Loop corrections that would re-introduce mass-like Ψ̄ΨA·A vertex without SSB (Q.3 carry-over).
- Non-local loop structures.

### 8.4 What remains empirical?

- All numerical loop-correction coefficients (α-expansion, β-function values, anomalous-moment magnitudes, running-coupling slopes).
- Sign of g − 2 (CANDIDATE for derivation; currently INHERITED).
- Specific renormalisation scheme.
- Higgs-loop contributions (if SM-occupant identified).
- Hadronic and electroweak contributions to muon g − 2 anomaly.

### 8.5 Bottom line

Stage Q.5 closes with the now-familiar Arc Q pattern:

- **Form-level FORCED:** loop structure exists and is structurally admissible; tree-level g = 2 unchanged from R.3; transversality from gauge invariance.
- **Value-level INHERITED:** all numerical content via QFT loop machinery built on Q.3 vertex catalogue.

One **genuinely-novel structural CANDIDATE** is opened: **UV-FIN** — primitive-level event-discreteness as natural UV cutoff. If this closes affirmatively at Q.7 / Q.8, it would be ED's first substantive structural prediction at the radiative-correction layer. Currently CANDIDATE only.

Three of five GRH refinements remain closed (R-2, R-3, R-4); R-1 and R-5 still pending Q.7 / Q.8.

---

## 9. FORCED / CANDIDATE / REFUTED summary

### 9.1 FORCED

- **F-Q5.1.** Multi-chain participation produces effective corrections (loop analogues) at primitive level.
- **F-Q5.2.** Fermion self-energy corrections exist whenever b^env is active.
- **F-Q5.3.** Gauge-boson vacuum-polarisation tensor is transverse (GRH-3 / Ward-identity-analogue).
- **F-Q5.4.** g = 2 at tree level from R.3 (carry-forward).
- **F-Q5.5.** Only Fierz tensor σ^{μν} contributes to anomalous magnetic moment; axial / pseudoscalar contribute to EDM only.
- **F-Q5.6.** Loop corrections preserve gauge invariance, Lorentz covariance, and locality.
- **F-Q5.7.** No loop correction can re-introduce mass-like Ψ̄ΨA·A without SSB (Q.3 §4.4 carry-forward).

### 9.2 CANDIDATE

- **C-Q5.1 (UV-FIN).** Primitive event-discreteness (Primitive 01) provides natural UV cutoff; multi-chain participation integrals finite at primitive level; renormalisation a continuum-approximation artefact. **Most structurally interesting CANDIDATE in Q.5.**
- **C-Q5.2.** Schwinger sign of g − 2 at one loop derivable structurally from Q.7 second-quantisation analysis.
- **C-Q5.3.** Asymptotic-freedom sign for SU(3) recoverable from primitive-level analysis (currently INHERITED).
- **C-Q5.4.** Higgs-loop contributions to gauge-boson masses contribute structurally if H1 is occupied.

### 9.3 REFUTED

- **R-Q5.1.** ED predicts specific numerical loop-correction coefficients. REFUTED — INHERITED.
- **R-Q5.2.** ED predicts asymptotic-freedom sign for SU(3) at primitive level. REFUTED at this stage — CANDIDATE for Q.7.
- **R-Q5.3.** Loop corrections violate gauge / Lorentz / locality. REFUTED — preserved.

### 9.4 INHERITED

- **I-Q5.1.** All numerical loop-correction coefficients.
- **I-Q5.2.** β-function values for any specific gauge group + matter content.
- **I-Q5.3.** Anomalous-magnetic-moment magnitudes.
- **I-Q5.4.** Specific renormalisation scheme.
- **I-Q5.5.** Hadronic, electroweak, Higgs-loop contributions to specific observables.

---

## 10. Implications for downstream substages

### 10.1 To Q.6 (generations and flavour)

Q.6 inherits:
- Loop-induced flavour mixing structure (admissible from §4.3 vertex corrections).
- ABJ anomaly admissibility (relevant for anomaly cancellation across generations).
- Running couplings admissibility — but generation count itself is unaffected.

### 10.2 To Q.7 (second quantisation)

Q.7 inherits:
- Loop content structurally framed at Q.5; Q.7 supplies the operator-level realisation.
- CANDIDATE UV-FIN evaluation — Q.7 should attempt rigorous derivation of finite multi-chain participation integrals from primitive discreteness.
- Schwinger-sign CANDIDATE: Q.7 vertex-topology analysis may resolve.
- R-1 (lightlike-worldline reformulation) closure here.

### 10.3 To Q.8 (vacuum)

Q.8 inherits:
- Vacuum-polarisation structure from §4.2.
- UV-FIN evaluation continuation.
- R-5 (vacuum/particle status) closure here.

### 10.4 Back-flow to Arc M

No back-flow at Q.5 — loop content does not modify Arc M's mass-structure verdict. Arc M's H1-dominant closure is unchanged. Loop-induced mass shifts (S1 self-energy) are admissible but their numerical content is INHERITED, consistent with Arc M's INHERITED-mass finding.

---

## 11. Cross-references

- Upstream: `higgs_mechanism_scoping.md` (Q.4), `interaction_vertex_classification.md` (Q.3), `gauge_group_scoping.md` (Q.2), `grh_evaluation.md` (Q.1), `qft_extension_scoping.md` (Q.0), `dirac_emergence.md` (R.3 — g = 2), `chain_mass_synthesis.md` (M.2).
- Downstream placeholders: `generations_and_mixing.md` (Q.6), `second_quantisation.md` (Q.7 — UV-FIN candidate, Schwinger sign), `vacuum_and_zero_point.md` (Q.8 — UV-FIN continuation, vacuum polarisation finer detail), `arc_q_synthesis.md`.
- Refinement tracking: R-1 open (Q.7); R-2 closed (Q.2); R-3 closed (Q.3); R-4 closed (Q.3); R-5 open (Q.7/Q.8). Q.5 opens no new refinements.

---

## 12. One-line summary

**Stage Q.5 finds that ED admits radiative-correction structure form-level via multi-chain commitment dynamics — fermion self-energy, gauge-boson vacuum polarisation (with FORCED transversality from GRH-3), vertex corrections, ABJ anomalies, running couplings, and Higgs loops all structurally admissible — with R.3's tree-level g = 2 preserved and the only Fierz contribution to anomalous magnetic moment being σ^{μν}; numerical coefficients, β-function values, Schwinger sign for g − 2, and asymptotic-freedom sign all INHERITED from QFT machinery; one structurally-novel CANDIDATE opened (UV-FIN: primitive event-discreteness as natural UV cutoff making renormalisation a continuum-approximation artefact, evaluable at Q.7/Q.8) — Arc Q's form-FORCED / value-INHERITED pattern continues, with Q.5 mostly inheriting at the value level but opening one potentially-substantive structural prediction route.**
