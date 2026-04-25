# ED Test-to-Axiom Mapping Report (v1.0)

## Section 1 — The 18 Axioms

### 1A. ED-05 Pre-PDE Axioms (4)

- **A1 Non-negativity** — ED ≥ 0 on any finite configuration
- **A2 Null baseline** — ED(∅) = 0
- **A3 Monotonicity** — adding events cannot decrease ED
- **A4 Subadditivity** — ED(A ∪ B) ≤ ED(A) + ED(B)

### 1B. Derivation Axioms (7)

- **D1 Locality** — dynamics depend only on local field values and derivatives
- **D2 Isotropy** — no preferred spatial direction
- **D3 Gradient-driven flow** — dynamics sourced by ρ and ∇ρ
- **D4 Dissipative structure** — monotone Lyapunov functional
- **D5 Single scalar field** — one ρ, no additional degrees of freedom at this layer
- **D6 Minimal coupling** — no higher-order or exotic couplings beyond those required
- **D7 Dimensional consistency** — equation invariant across spatial dimension d

### 1C. Architectural Canon P1–P7 (7)

- **C1 Operator Structure** — F[ρ] = M(ρ)∇²ρ + M′(ρ)|∇ρ|² − P(ρ)
- **C2 Channel Complementarity** — ρ̇ = D·F[ρ] + H·v, D + H = 1
- **C3 Penalty Equilibrium** — P(ρ*) = 0, P′ > 0, unique globally-attracting ρ*
- **C4 Mobility Capacity Bound** — M(ρ_max) = 0, M > 0 below
- **C5 Participation Feedback Loop** — v̇ = (1/τ)(F[ρ] − ζv)
- **C6 Damping Discriminant** — Δ = D + 2ζ, sharp transition at D_crit
- **C7 Nonlinear Triad Coupling** — M′(ρ)|∇ρ|² generates k=3 from k=1

## Section 2 — The Four Empirical Tests

- **T1 AFM thin-film dewetting** — motif-conditioned field-space Hessian on PS-on-Si AFM topography; ED-SC 2.0 prediction med(ℛ_motif) ∈ [−1.50, −1.10]
- **T2 UDM-FRAP high-BSA mobility** — BSA-FITC FRAP 200–350 mg/mL; Barenblatt 2D PME prediction R(t) ~ t^(1/6), β = 2; PME-vs-Fickian AIC decision
- **T3 ED-09.5 participation envelope** — envelope law ω_v = 2π·N_osc·γ_dec at two regimes
  - **T3a Track A** — Aspelmeyer optomechanics raw x(t) reanalysis
  - **T3b Track B** — Lomb-Scargle on public FRAP residuals at 80–800 Hz
- **T4 RLC analogue (Runs A–D)** — benchtop linear-limit telegraph/participation coupling; underdamped/overdamped discriminant sweep

## Section 3 — Coverage Definitions

### 3A. Direct Coverage

- Test observable is a quantitative consequence derived *specifically* from that axiom
- Negating the axiom predicts a numerically different test outcome
- Axiom is load-bearing in the prediction's derivation chain

### 3B. Indirect Coverage

- Axiom is necessary for the theoretical scaffold the test sits inside, but not the specific observable
- Test requires the axiom to hold but does not discriminate against its variants
- Axiom enters the prediction only through shared architectural assumptions

### 3C. Non-Coverage

- Test outcome is invariant under changes to the axiom
- No derivation step from axiom to observable
- Axiom operates at a layer (pre-PDE, architectural class) the test cannot resolve

## Section 4 — Full 18×5 Coverage Matrix

Columns: **T1** AFM · **T2** UDM-FRAP · **T3a** ED-09.5 Track A · **T3b** ED-09.5 Track B · **T4** RLC analogue

### A1 Non-negativity

| T1 | T2 | T3a | T3b | T4 |
|---|---|---|---|---|
| indirect | indirect | indirect | indirect | indirect |

- T1 — AFM height field is non-negative by construction of the density observable
- T2 — FRAP intensity field is a non-negative concentration proxy
- T3a — cavity displacement envelope amplitude is non-negative
- T3b — FRAP recovery residual amplitude is non-negative
- T4 — RLC energy/amplitude observables are non-negative

### A2 Null baseline

| T1 | T2 | T3a | T3b | T4 |
|---|---|---|---|---|
| none | none | none | none | none |

- No test prepares or probes the empty-configuration limit

### A3 Monotonicity

| T1 | T2 | T3a | T3b | T4 |
|---|---|---|---|---|
| none | none | none | none | none |

- No test manipulates configuration cardinality against the ED value

### A4 Subadditivity

| T1 | T2 | T3a | T3b | T4 |
|---|---|---|---|---|
| none | none | none | none | none |

- Compositional-rule content lives at the 00.1 cosmological layer; none of the four tests probes union-of-configurations structure

### D1 Locality

| T1 | T2 | T3a | T3b | T4 |
|---|---|---|---|---|
| indirect | indirect | indirect | indirect | indirect |

- T1 — field-space Hessian evaluated on local neighborhoods
- T2 — 2D PME derivation assumes local flux
- T3a/T3b — envelope ω_v = 2π·N_osc·γ_dec derived from local participation ODE
- T4 — RLC lumped-element locality

### D2 Isotropy

| T1 | T2 | T3a | T3b | T4 |
|---|---|---|---|---|
| indirect | indirect | none | none | none |

- T1 — motif-conditioned median is an isotropic statistic over the 2D field
- T2 — radial-profile front-detection assumes isotropic spreading
- T3a/T3b — temporal-only observables, no spatial directionality
- T4 — 0-D/lumped circuit, no spatial isotropy content

### D3 Gradient-driven flow

| T1 | T2 | T3a | T3b | T4 |
|---|---|---|---|---|
| direct | direct | indirect | indirect | indirect |

- T1 — Hessian of ∇²E probes gradient structure of the field-space energy
- T2 — R(t) ~ t^(1/6) is the Barenblatt gradient-flow signature
- T3a/T3b — gradient-driven F[ρ] enters the participation source term
- T4 — RLC is a lumped-element reduction of the gradient flow

### D4 Dissipative structure

| T1 | T2 | T3a | T3b | T4 |
|---|---|---|---|---|
| indirect | direct | indirect | indirect | direct |

- T1 — spinodal dewetting is dissipative coarsening
- T2 — PME relaxation is the canonical dissipative Lyapunov descent
- T3a — γ_dec is the dissipation rate entering the envelope
- T3b — recovery residual dissipation on 80–800 Hz band
- T4 — ohmic damping R is the dissipation term being swept

### D5 Single scalar field

| T1 | T2 | T3a | T3b | T4 |
|---|---|---|---|---|
| indirect | indirect | indirect | indirect | indirect |

- All four tests reduce to a single scalar observable; none requires a second field

### D6 Minimal coupling

| T1 | T2 | T3a | T3b | T4 |
|---|---|---|---|---|
| indirect | indirect | indirect | indirect | indirect |

- Each test's predictive derivation uses only the canonical operator set; no exotic couplings invoked or required

### D7 Dimensional consistency

| T1 | T2 | T3a | T3b | T4 |
|---|---|---|---|---|
| indirect | indirect | none | none | indirect |

- T1 — 2D realization of the field-space Hessian invariant
- T2 — 2D PME realization with β = 2
- T3a/T3b — purely temporal, no spatial-dimension content
- T4 — lumped-element / effectively 0-D realization; cross-dimensional check only in aggregate

### C1 Operator Structure

| T1 | T2 | T3a | T3b | T4 |
|---|---|---|---|---|
| direct | direct | indirect | indirect | indirect |

- T1 — ED-SC 2.0 field-space Hessian is the geometric signature of this operator form
- T2 — PME Barenblatt solution follows from the M(ρ)∇²ρ + M′|∇ρ|² pair
- T3a/T3b — operator enters only through F[ρ] as a source to v-ODE
- T4 — linear-limit reduction of F[ρ]

### C2 Channel Complementarity

| T1 | T2 | T3a | T3b | T4 |
|---|---|---|---|---|
| none | none | direct | direct | direct |

- T1 — static-field test, no participation channel activated
- T2 — pure mobility regime, H channel not probed
- T3a — envelope observable is the v-channel signature, resolving the H weight
- T3b — same envelope prediction at condensed-matter regime
- T4 — RLC is the canonical two-channel analogue; sweeping C vs L weights probes D+H balance

### C3 Penalty Equilibrium

| T1 | T2 | T3a | T3b | T4 |
|---|---|---|---|---|
| indirect | indirect | none | none | indirect |

- T1 — pre-rupture thin-film sits at a metastable ρ* controlled by P
- T2 — FRAP recovery asymptote is the penalty equilibrium
- T3a/T3b — envelope observable is insensitive to the penalty form
- T4 — restoring element sets the equilibrium of the lumped circuit

### C4 Mobility Capacity Bound

| T1 | T2 | T3a | T3b | T4 |
|---|---|---|---|---|
| none | direct | none | none | none |

- T2 — UDM β = 2 saturating mobility at high BSA is the defining signature of the capacity bound
- Other tests operate below the mobility ceiling and do not probe M(ρ_max) vanishing

### C5 Participation Feedback Loop

| T1 | T2 | T3a | T3b | T4 |
|---|---|---|---|---|
| none | none | direct | direct | direct |

- T3a — ω_v = 2π·N_osc·γ_dec envelope is the direct consequence of this ODE
- T3b — same ODE tested at FRAP-residual regime
- T4 — RLC L-branch is the literal circuit analogue of the v-ODE; v1.0 linear-limit telegraph PME (one-char-patched in `telegraph_pme.py:162`) validates this coupling structure
- T1/T2 — no participation channel resolved

### C6 Damping Discriminant

| T1 | T2 | T3a | T3b | T4 |
|---|---|---|---|---|
| none | none | indirect | indirect | direct |

- T4 — Runs A–D sweep the underdamped ↔ overdamped discriminant, directly probing D_crit
- T3a/T3b — envelope law is derived in the underdamped regime (Δ < 1) but does not scan the transition
- T1/T2 — static / overdamped-only settings; discriminant not resolved

### C7 Nonlinear Triad Coupling

| T1 | T2 | T3a | T3b | T4 |
|---|---|---|---|---|
| indirect | indirect | indirect | indirect | none |

- T1 — nonlinear field structure underlies the motif-conditioned invariant but triad ratio is not the observable
- T2 — M′|∇ρ|² term is present in the PME derivation; triad not measured
- T3a/T3b — nonlinear coupling required for v-channel activation; triad ratio not resolved
- T4 — explicitly linear regime, no triad content

## Section 5 — Gap Analysis

### 5A. No Coverage (0 direct, 0 indirect)

- **A2 Null baseline** — ED(∅) = 0 never probed
- **A3 Monotonicity** — no test manipulates configuration cardinality
- **A4 Subadditivity** — compositional-rule content (00.1) not reached by any empirical test

### 5B. Indirect-Only (≥1 indirect, 0 direct)

- **A1 Non-negativity** — 5 indirect (presupposed by every observable, never discriminated)
- **D1 Locality** — 5 indirect (all PDE derivations assume it, none falsifies it)
- **D2 Isotropy** — 2 indirect (T1, T2 via radial/motif statistics)
- **D5 Single scalar field** — 5 indirect (all tests use single scalar observables)
- **D6 Minimal coupling** — 5 indirect (no test rules out exotic couplings)
- **D7 Dimensional consistency** — 3 indirect (individual tests occupy single d; no in-test cross-d check)
- **C3 Penalty Equilibrium** — 4 indirect (equilibria observed but P-form not discriminated)
- **C7 Nonlinear Triad Coupling** — 4 indirect (M′|∇ρ|² present in derivations; k=3-from-k=1 ratio never measured)

### 5C. Multi-Test Direct (≥2 direct)

- **D3 Gradient-driven flow** — direct in T1, T2 (two independent settings: 2D static Hessian + 2D PME)
- **D4 Dissipative structure** — direct in T2, T4 (soft-matter relaxation + ohmic damping; independent mechanisms)
- **C1 Operator Structure** — direct in T1, T2 (static field geometry + dynamic PME; independent aspects)
- **C2 Channel Complementarity** — direct in T3a, T3b, T4 (two participation-envelope regimes + RLC two-channel analogue)
- **C5 Participation Feedback Loop** — direct in T3a, T3b, T4 (envelope law at two regimes + RLC circuit analogue)

### 5D. Layer Summary (cell counts)

- **Pre-PDE layer (A1–A4, 20 cells)** — 0 direct · 5 indirect · 15 none
- **Derivation layer (D1–D7, 35 cells)** — 4 direct · 26 indirect · 5 none
- **Canon layer (C1–C7, 35 cells)** — 10 direct · 13 indirect · 12 none

Per-axiom direct-count by layer:

- **Pre-PDE** — A1:0, A2:0, A3:0, A4:0
- **Derivation** — D1:0, D2:0, D3:2, D4:2, D5:0, D6:0, D7:0
- **Canon** — C1:2, C2:3, C3:0, C4:1, C5:3, C6:1, C7:0

### 5E. Structurally Under-Tested Region

- **Primary — Pre-PDE layer (A1–A4)**
  - 0 direct cells across the entire layer
  - 15/20 cells are `none`
  - Root cause — pre-PDE axioms live on a bare event domain with no dynamics; the four empirical tests are all PDE-level or circuit-level
- **Secondary — Derivation "infrastructure band" (D1, D5, D6)**
  - Each has 5 indirect, 0 direct
  - Load-bearing in every derivation but never falsified because no test varies them
- **Tertiary — Canon axioms C3 and C7**
  - Both 0 direct despite sitting inside the mature PDE program
  - C3 broadly observed (4 indirect) but alternative penalty forms not discriminated
  - C7 has 4 indirect entries and is the most distinctive falsifiable architectural signature currently unprobed

### 5F. Most Load-Bearing Under-Tested Axiom

- **C7 Nonlinear Triad Coupling** is selected
- Why load-bearing — most distinctive mechanistic claim: `M′(ρ)|∇ρ|²` generates k=3 from k=1 with invariant triad ratio; mechanism behind Analogue-5 coupling structure surviving the 2026-04-22 FPv2 §8.4 retraction
- Why under-tested — 4 indirect, 0 direct, 1 none; all current tests are linear-limit (T4), single-harmonic envelope (T3a/T3b), static geometric (T1), or exponent-only (T2)
- Runner-up — C3 Penalty Equilibrium (4 indirect, 0 direct; less architecturally distinctive)
- Runner-up — A4 Subadditivity (highest-leverage pre-PDE axiom; outside current empirical reach)

## Section 6 — Next-Experiment Generator

### 6A. Target

- **C7 Nonlinear Triad Coupling** — `M′(ρ)|∇ρ|²` generates a k=3 spatial (or third-harmonic temporal) response from a k=1 drive with invariant triad ratio; ED-Phys-16 reports coupling ~0.03 and harmonic 3–6% of fundamental

### 6B. Discriminating Observable

- **Modal amplitude ratio** `A₃/A₁` between third-harmonic and fundamental under single-mode drive or spontaneous single-mode organization
- **Spatial realization** — Fourier-decompose `ρ(x,y)` at dominant `k_s`, measure `A(3k_s)/A(k_s)`
- **Temporal realization** — drive lumped analogue at `f₀`, measure `A(3f₀)/A(f₀)` at steady state
- **Sourcing test** — whether `A₃` is sourced by `A₁` (transfer `∝ A₁²`) or decays independently

### 6C. Prediction Under C7

- `A₃/A₁ ∈ [0.02, 0.08]` (from ED-Phys-16 coupling ~0.03, harmonic 3–6%)
- Scaling `A₃ ∝ A₁²` (cubic-order mixing)
- Triad selects k=3 (not k=2) by odd symmetry of gradient-squared product
- Phase locking of `A₃` to `A₁` at fixed offset

### 6D. Negation Prediction

- Linear regime — `A₃/A₁ < 0.005`, independent decay of `A₃`
- Quadratic-only nonlinearity — `A₂ > A₃`
- Broadband nonlinearity — `A₃/A₁` present but not phase-locked; scaling not `A₁²`
- No triad invariance — `A₃/A₁` drifts with sample/temperature/drive amplitude

### 6E. Minimum Apparatus

- **Instrument class** — 2D field imager with ≥ 6× oversampling of dominant mode, OR lumped-analogue benchtop rig with harmonic spectrum readout
- **Sample class** — thin-film dewetting AFM (reuses T1), OR RLC + mild nonlinear element on AstroAI breadboard (reuses T4), OR patterned FRAP in BSA band (reuses T2 prep)
- **Resolution floor** — spatial `Δx ≤ λ_s/6`; spectral SNR ≥ 40 dB at 3f₀; ≥ 10-bit dynamic range on fundamental

### 6F. Decision Rule

- **PASS** — `A₃/A₁ ∈ [0.02, 0.08]`, `A₃ ∝ A₁²` over ≥ 1 decade in drive, phase-locked
- **FAIL** — `A₃/A₁ < 0.005` with independent decay, OR `A₂ > A₃`, OR scaling not `A₁²`
- **UNDECIDABLE** — `A₃/A₁ ∈ [0.005, 0.02]`, noise-limited, insufficient amplitude range
- **SPLIT** — ratio in band but scaling or phase-lock fails; flag partial-support, follow-up required

## Section 7 — Recommended Experiment

### 7A. Top-1 — AFM Spinodal-Dewetting Fourier Triad Reanalysis

- **Method** — take existing or newly-acquired AFM dewetting frames (T1 pipeline), Fourier-decompose each frame, identify dominant spinodal wavevector `k_s`, measure `A(3k_s)/A(k_s)` across the evolution, check `A₁²` scaling across frames where `A(k_s)` varies naturally in time
- **Cost** — $0 incremental (pure reanalysis) to ~$500 if new dewetting run required
- **Timeline** — 1–2 weeks analysis-only; 4–6 weeks if new samples required
- **Dependency** — reuses full T1 protocol at [`AFM-Dewetting-ED-SC_InProcess/protocol.md`](../experiements/AFM-Dewetting-ED-SC_InProcess/protocol.md)
- **Why top-1** — zero new equipment; direct spatial-harmonic measurement (not a lumped analogue); simultaneously upgrades T1's C7 cell from `indirect` to `direct` and strengthens D3/C1 cross-confirmation

### 7B. Alternative 1 — Nonlinear RLC Third-Harmonic Generation (T4 extension)

- Add saturating inductor or reverse-biased diode to AstroAI RLC kit; drive sinusoidally at `f₀`, sweep amplitude, measure `A(3f₀)/A(f₀)`
- **Cost** — ~$20 incremental; 1–2 days bench time
- **Coverage gain** — upgrades T4's C7 cell from `none` to `direct` in the participation-channel analogue; complements top-1 in temporal rather than spatial domain

### 7C. Alternative 2 — Patterned-FRAP k=3 Recovery

- Confocal FRAP with structured-illumination bleaching imprints a k=1 spatial pattern on high-BSA sample; recovery of k=1 and k=3 spatial Fourier components measured independently
- **Cost** — ~$2000–5000 via Creative Proteomics; requires patterned-bleach capability confirmation
- **Coverage gain** — upgrades T2's C7 cell from `indirect` to `direct` in the canonical PME setting where M′(ρ) is exactly the UDM β=2 mobility; cleanest mapping to C7, highest cost

### 7D. Alternative 3 — Telegraph-PME Simulation Calibration Benchmark

- Run v1.0 linear + mildly-nonlinear extension of `telegraph_pme.py` (post one-char patch at line 162) on monochromatic k=1 seeded field; measure `A₃/A₁` vs M′ magnitude; compare to [0.02, 0.08] band
- **Cost** — $0, CPU-only
- **Coverage gain** — does not upgrade any matrix cell (simulation, not experiment), but produces predicted band at first-principles resolution and tightens decision rule for top-1 and Alternative 1; necessary theoretical companion rather than standalone test

---

*Document version: v1.0. Compiled from Stages 1–4 of the Test-to-Axiom Mapping Project. Stable; subsequent revisions should increment the version number in the title.*
