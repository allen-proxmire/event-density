# Fine-Structure Constant Scoping Memo

**Date.** 2026-04-22.
**Scope.** One-afternoon feasibility scope. Not a theory, not a derivation, not a proposal for new axioms. The question: given ED's current architecture, could the fine-structure constant `α ≈ 1/137.036 ≈ 7.297 × 10⁻³` emerge from ED primitives, the ED-Dimensional-01 dictionary, participation-scattering coefficients, or any structural feature of the penalty functional?
**Target.** The dimensionless Sommerfeld coupling `α = e²/(4πε₀ℏc)` of QED.
**Verdict.** Dead end in current ED. Strictly worse than the species-mass question (`theory/Species_Mass_Spectrum_Scoping.md`): that one had mass as a genuine external dimensional input; `α` has no even-notional hook into current ED because ED has no electromagnetic sector, no charge primitive, and no gauge symmetry. Any near-match against ED's existing dimensionless invariants is numerology. See §7–§8.

---

## 1. Problem Statement

### 1A. The precise question

Can ED — as defined by the four ED-05 pre-PDE axioms and the seven P1–P7 Canon principles, plus the ED-Dimensional-01 quantum-regime dictionary — produce a dimensionless constant equal or structurally related to `α ≈ 7.297 × 10⁻³`, *without* inserting a charge-like coupling by hand?

### 1B. Legitimate derivation vs numerology — criterion

A *legitimate derivation* of `α` (or of any dimensionless constant of Nature) must satisfy at least the following:

- **(C1) Structural.** The value arises from the axiomatic content of the theory, not from choice of a free parameter.
- **(C2) Non-tautological.** The derivation uses at least one non-trivial step — i.e., the answer is not a restatement of a definition or a trivial algebraic identity.
- **(C3) Over-determined.** The derivation also predicts, or is constrained by, at least one independent observable besides the target number. A theory that has one knob and matches one number has zero predictive content.
- **(C4) Robust.** The value does not depend on unspecified functional choices (e.g., specific form of `M(ρ)`, `P(ρ)`) that the axioms do not fix.
- **(C5) Mechanistic.** A specific feature of the theory — symmetry, quantization condition, fixed point, topological invariant — is responsible for the value, and a different choice of that feature would give a different value.

Anything failing (C1)–(C5) is *numerology*. This includes: finding that some algebraic combination of ED invariants approximates `1/137`, fitting a function form to land near `0.00730`, or noticing that the ED-Phys-16 triad coefficient `C ≈ 0.03` is "the same order of magnitude" as `α`.

### 1C. Prior: how hard is this target?

`α` is one of the *least* understood numbers in fundamental physics. The Standard Model does not predict it — it is a Lagrangian input. Attempts at derivation from first principles include:

- Eddington's `1/137 = 16² − 16² − ...` (retracted, numerology).
- Wyler's 1969 algebraic coincidence involving π and the volume of the Siegel disk (numerology; no mechanism).
- String-theory landscape pictures (`α` is an environmental selection effect, not a derivation).
- Asymptotic-safety fixed-point pictures (no completed derivation; `α` is tied to the UV cutoff of QED which is understood to be Landau-trivial).

**Base rate: no existing framework predicts `α` from first principles.** Any positive result in ED would be a first. This matters for assessing claims.

---

## 2. Relevant ED Primitives and Dimensionless Groups

What ED actually has, in full.

### 2A. Primitives (four, per ED-05 → Canon)

Field-level:
- `ρ(x, t)` — scalar event-density field.
- `v(x, t)` — participation variable (time-integrated operator; see P5).

Operator-level parameters:
- `D ∈ [0,1]` — dimensionless direct-channel weight (P2).
- `H = 1 − D ∈ [0,1]` — dimensionless mediated-channel weight (P2).
- `ζ ≥ 0` — dimensionless damping ratio (P5, canon default `1/4`).
- `τ > 0` — participation relaxation time (P5, dimensional).

Functional primitives (shape-free; only qualitative properties fixed by Canon):
- `M(ρ)` — mobility, with `M(ρ_max) = 0` (P4).
- `P(ρ)` — penalty, with unique zero at `ρ*` and `P' > 0` (P3).
- `M'(ρ)` — derivative of mobility; sources the P7 triad term.

Compositional-rule prefactors (ED-Cosmo 00.1):
- `α_CR` — relational-penalty coefficient in the compositional rule. **NB: this is a distinct, unrelated `α` to the fine-structure constant; this memo refers to this one as `α_CR` to avoid collision.**
- `β_CR` — gradient-penalty coefficient.
- `γ_CR` — boundary-term coefficient.

Dimensional dictionary (ED-Dimensional-01, per-species, with `m` as external input):
- `L₀ = ℏ/(mc)`.
- `T₀ = 0.6 ℏ/(mc²)`.
- `D_phys = ℏ/(2m)` (dimensional diffusivity, distinct from channel weight `D`).
- Signal speed: `c₀ = L₀/T₀ = c/0.6 ≈ 1.667 c`. (Note: `c₀ ≠ c`; see `Species_Mass_Spectrum_Scoping.md` §2B.)

### 2B. Dimensionless groups ED can form *without* external inputs

| Group | Value | Status |
|---|---|---|
| `D + H` | `1` | tautological (P2) |
| `D·T₀/L₀²` | `0.3` | tautological in the dictionary (see `Species_Mass_Spectrum_Scoping.md` §2B) |
| `|r*|` | `1.304` | ED-SC 2.0 motif-conditioned Hessian exponent |
| `D_crit(ζ = 1/4)` | `≈ 0.896` | P6 underdamped threshold (corrected 2026-04-22) |
| `ζ / D_crit` | `≈ 0.279` | parameter-choice-dependent |
| `4(1 − D) / (D − ζ)²` | P6 discriminant ratio | depends on (`D`, `ζ`) |
| `C` (P7 triad coupling) | `≈ 0.03` | measured in ED-Phys-16 simulations |
| `K = A₃/A₁³` (C7) | `≈ 0.0148` | predicted invariant (unconfirmed in real data as of 2026-04-22) |
| `Q` (quality factor) | `≈ 3.5` | oscillatory-sector invariant |
| `N_osc` | `~9` | transient oscillations |

### 2C. Are any of these near `α ≈ 7.297 × 10⁻³`?

Only two candidates fall in the `10⁻² – 10⁻³` band:
- `C ≈ 0.03` — factor of **~4** from `α`.
- `K ≈ 0.0148` — factor of **~2** from `α`.

**Neither is a match, and both are architectural coefficients of ED's nonlinear triad sector, not independently-derived quantities.** `C` was measured in ED-Phys-16 with specific `M(ρ)` and perturbation choices; `K` is a predicted invariant whose value depends on the multiplicative-perturbation regime. Neither is fixed to a specific number by the Canon axioms alone — both require a specific `M(ρ)` choice. They fail (C4) immediately.

### 2D. Dimensionless groups ED can form *with* external inputs

Once the ED-Dimensional-01 dictionary is invoked (which introduces `ℏ, c, m` for a given species), one can form:
- `ℏc · L₀ / (something with units of energy·length·area)` — but this reduces to the input scales.
- No combination of `(ℏ, c, m)` alone produces a pure dimensionless number *other than* `1`. To get `α` you *must* introduce a coupling `e²/(4πε₀)` with units of `[ℏc]`. **That coupling is not in ED.**

---

## 3. Candidate Mechanisms for α-Like Constants

Four structurally distinct routes, per the task description. Each evaluated on its own terms.

### 3A. `α` as a participation-scattering coefficient

**Proposal.** Interpret `α` as an effective cross-section for two ED fluctuations scattering via the P7 nonlinear term `M'(ρ)|∇ρ|²`. In momentum space, linearising about `ρ_0`, the term provides a 3-point vertex with coefficient `M'(ρ_0)`. Define `σ_eff / (4π L₀²) =? α`.

**What it would require structurally.**

- (i) A specific functional form for `M(ρ)` such that `M'(ρ_0)` is pinned by an axiom, not chosen. **ED does not provide this**; Canon only requires `M(ρ_max) = 0`, `M(ρ) > 0` for `ρ < ρ_max`. An infinity of `M` shapes satisfies this.
- (ii) A notion of asymptotic scattering states. ED is a classical dissipative PDE; asymptotic states require the reversible sector *plus* a scattering-theory framework that ED does not have.
- (iii) An infrared regulator. Scattering cross-sections for nonlinear scalar theories are infrared-divergent in 4D; regularisation requires extra structure.
- (iv) An ultraviolet regulator. Cross-sections are also UV-divergent; regularisation needs a cutoff that Canon does not supply.

**Status.** Fails (C4) — answer depends on unspecified shape of `M`. Fails (C5) — no mechanism fixes the value. Fails (C1) — would require an additional physical axiom to pin `M'`. Not viable.

### 3B. `α` as a ratio of ED time/length scales

**Proposal.** Construct `α` from combinations of `L₀, T₀, D, ζ, τ`.

**Blocker.** Every such combination is either:
- tautological (`D·T₀/L₀² = 0.3` is an algebraic identity of the dictionary), or
- depends on a parameter choice (`ζ = 1/4` is a convention, not a theorem).

No combination of dimensionless ED invariants gives `α`, and even if one "matched" numerically, it would fail (C2) — it would be a restatement of definitions, not a non-trivial consequence.

**Numerology check.** Combinations near `1/137`:
- `D_crit · C ≈ 0.896 × 0.03 ≈ 0.0269` — off by 3×.
- `C² ≈ 9 × 10⁻⁴` — off by 8×.
- `K · |r*|⁻¹ ≈ 0.0113` — off by 1.5×.
- `α_CR · β_CR` — undetermined, fit parameters.

None of these is a derivation. All fail (C2), (C3), (C4), (C5). **Listing them here only to demonstrate the universal availability of numerological near-matches when a theory has ~10 dimensionless coefficients.**

### 3C. `α` as a mobility–participation coupling constant

**Proposal.** Treat the coupling between the mobility channel (`D·F[ρ]`) and the participation channel (`H·v`) as providing a dimensionless coupling; identify it with `α`.

**Blocker.** The mobility–participation coupling is `D·H = D(1−D)`, which is maximised at `D = 1/2` with value `1/4`. This is a hybrid-regime parameter, not a small number. It can be small only if `D ≈ 0` or `D ≈ 1`, in which case *one channel is off*; that's not a coupling in the gauge-theory sense, it's regime selection. **No structural reason to expect the coupling to be near `α`.**

**Status.** Fails (C5) — no mechanism picks the small value; it requires choosing `D` near the endpoints by fiat.

### 3D. `α` as a renormalized coefficient in the quantum-regime dictionary

**Proposal.** In QED, `α(μ)` runs with scale `μ`. Could an ED analogue of this running — e.g., renormalization of `D`, `M`, `P` under coarse-graining — land at `α ≈ 1/137` at some physical scale?

**What it would require.**

- (i) A second-quantised ED — i.e., a Fock space, a vacuum, loop integrals. ED is classical; Canon defines a PDE, not a QFT.
- (ii) A running-coupling interpretation of the coarse-graining flow. Possible in principle (Wilsonian RG of classical field theories is well-defined) but would require identifying which ED coefficient runs *and* why its IR fixed point would be `1/137`.
- (iii) A Landau-pole or asymptotic-safety argument. QED's `α` is tied to a triviality problem; there is no ED analogue of the QED triviality because ED has no U(1) gauge theory underneath.

**Status.** Requires building second-quantised ED first, then matching to QED renormalization structure, then hoping a fixed point lands at `1/137`. This is several multi-year programs stacked in sequence, with no checkpoint before the final step that gives an intermediate observable. Fails (C3) catastrophically — no over-determination, just one long pipeline aiming at one number.

---

## 4. Quantum-Regime Dictionary Analysis

### 4A. What the dictionary provides

`L₀ = ℏ/(mc)`, `T₀ = 0.6 ℏ/(mc²)`, `D_phys = ℏ/(2m)`. The dictionary introduces `ℏ, c, m` as the only dimensional inputs.

### 4B. Dimensionless quantities from `(ℏ, c, m)` alone

The only dimensionless combination of `(ℏ, c, m)` is `1`. To form `α`, one needs a coupling with units of `[ℏc]` — classically, `e²/(4πε₀)`. **That coupling is not among ED's primitives.**

### 4C. Could `α` arise from a scattering amplitude in the dictionary regime?

ED-Dimensional-01 places ED in the quantum regime by matching to the Schrödinger equation. In that regime, small fluctuations satisfy a diffusion equation (in Euclidean time) or a Schrödinger-like equation (after analytic continuation). Scattering cross-sections for a free Schrödinger particle are:
- Zero for purely kinetic dynamics (no scattering).
- Non-zero only when a coupling is introduced (e.g., a potential `V(x)`, a self-interaction).

ED's P7 self-interaction `M'(ρ)|∇ρ|²` provides a nonlinear term analogous to a `φ⁴`-theory self-coupling. Its dimensionless strength in the dictionary regime is `(M'(ρ_0) · ρ_0 · L₀²) / D_phys`, which — by the dictionary — evaluates to a specific *multiple of the dimensional `M'`*, not a fixed pure number. **Without a Canon axiom fixing `M'(ρ_0)`, this is a free parameter.** Fitting it to `α` would be numerology.

### 4D. Could `α` emerge from a consistency condition on the dictionary?

The dictionary already exhibits one cross-regime invariant: `D_phys · T₀ / L₀² = 0.3`. This was shown to be an algebraic identity of the dictionary definitions (Species-Mass memo §2B). **Any further "consistency condition" on the dictionary is either (a) another tautology, or (b) requires an additional axiom not in Canon.** Neither produces `α` non-trivially.

### 4E. Conclusion on dictionary

The quantum-regime dictionary cannot produce `α` without importing a dimensionful coupling (charge) that ED does not have. Routing `α` through the dictionary therefore reduces to route §3A (participation-scattering) — same obstacles, same verdict.

---

## 5. Participation-Scattering Interpretation

### 5A. Does ED have structural degrees of freedom to encode "charge"?

Charge in QED has three essential properties:
- (i) It is a conserved quantity via a local U(1) symmetry (Noether → gauge invariance → conservation).
- (ii) It labels representations of matter fields (charged vs neutral, positive vs negative).
- (iii) It couples matter to the photon via a vertex factor `eγ^μ`.

ED has:
- (i′) No local symmetries beyond spatial Euclidean isometries of the substrate; the Canon imposes no gauge structure.
- (ii′) A single scalar field `ρ ≥ 0` with no representation labels; there is no "charged" vs "neutral" `ρ`.
- (iii′) No vertex structure between `ρ` and a vector field (there is no vector field in ED).

**ED does not have the structural DOFs to encode charge.** This is a stronger statement than "ED has not yet derived charge" — it is that the structural ingredients charge *requires* are absent.

### 5B. Can a charge-analogue be *constructed* from ED primitives?

Some speculative routes worth noting so they can be ruled out:

- **(a) `ρ` as a modulus of a complex field `ψ`.** Would require adding a phase degree of freedom. That is **adding an axiom**, not deriving from ED.
- **(b) Participation vector `v` as a gauge connection.** `v` in P5 is not a spatial vector field in the gauge sense — it is a participation scalar/vector per point, evolving by an ODE. No curvature 2-form structure.
- **(c) Topological charge from `ρ`-defect configurations.** Would require `ρ` to take values in a target space with nontrivial homotopy (e.g., S¹ for vortex charge in a superfluid). `ρ ≥ 0` is a half-line, homotopically trivial. **No topological charge in ED.**

All three require new axiomatic content. None is a derivation.

### 5C. Participation-transfer efficiency — is this an `α`-analogue?

ED has a participation-transfer mechanism (P5): the operator `F[ρ]` drives `v`, which drives `ρ`. The *efficiency* of this transfer in the reversible sector is set by `(D − ζ)² / 4(1 − D)` (P6 discriminant). At canon default `ζ = 1/4`, `D = D_crit ≈ 0.896`, the efficiency is "marginally underdamped" — `Q ≈ 3.5`.

**Is there a structural reason `1/Q ≈ 0.286` should equal or be related to `α`?** No. The value `Q ≈ 3.5` is a P6 consequence of canon defaults. It is not a gauge coupling, not tied to charge, and not tunable by any axiom to `1/137`. Forcing a match would require choosing `ζ` and `D` to make `1/Q ≈ α`, which is a fit of two parameters to one number — worse than numerology, under-determined parameter tuning.

### 5D. Triad coupling `C ≈ 0.03` or `K ≈ 0.0148` — fingerprints or fundamental?

These are ED's *own* dimensionless coefficients of the nonlinear sector. They are the closest things ED has to a fundamental dimensionless coupling of its own. Two possibilities:

- **(α-analogue interpretation.)** `C` and `K` are ED's equivalent of `α` — architectural dimensionless numbers characterising the self-interaction strength. In this view, ED *has* its own `α`-analogues; they are simply not the QED `α`. This is the honest reading.
- **(α-identification interpretation.)** `C = α` or `K = α` or some function thereof. This fails (C4) — the numbers depend on `M(ρ)` shape, which Canon does not fix.

**The honest reading is (α-analogue), and it supports *keeping open* the narrow subproblem of whether `C`, `K` are architectural invariants across different Canon-compatible `M` choices — but that subproblem is already the live C7 research thread, and it has nothing to do with QED `α`.** Conflating them would confuse two distinct (and both interesting) questions.

---

## 6. Structural Obstacles

Each obstacle classified as **fatal** (cannot be overcome without adding major new axioms), **fixable** (resolvable within existing Canon), or **requiring new axioms** (could be addressed but with a specific additional ingredient).

| # | Obstacle | Severity |
|---|---|---|
| O1 | ED has no electromagnetic sector (no vector potential, no field strength tensor). | **Requires new axioms** — adding a U(1) gauge field is an axiomatic extension. |
| O2 | Charge is not a primitive; `ρ` is a non-negative scalar. | **Fatal** for a direct derivation — would require replacing `ρ` with a richer field type. |
| O3 | No U(1) gauge symmetry anywhere in Canon. | **Fatal** — `α` is fundamentally a U(1) coupling. |
| O4 | No Lorentz symmetry (`c₀ ≠ c`, substrate is Euclidean). | **Fatal** — `α` is Lorentz-invariant; its *value* depends on working in Lorentzian spacetime. (See `ED_Geometry_Emergence_Scoping.md` §7B.) |
| O5 | ED's cross-regime invariants (`D·T₀/L₀² = 0.3`, `r* = −1.304`, `D_crit ≈ 0.896`) are not near `α` and have no structural tie to EM. | **Informative**, not technically fatal — confirms `α` is not hiding in Canon's existing numbers. |
| O6 | No second quantization / Fock space. Running-coupling interpretation requires this. | **Requires new axioms** — Wilsonian RG of classical ED could be defined but adds structure. |
| O7 | Canon does not fix `M(ρ)` or `P(ρ)` functional forms beyond qualitative properties. Any α-match would depend on a specific choice. | **Fatal for derivation**, per (C4). |
| O8 | No mechanism to pin a dimensionless coupling to `1/137` specifically. Even in theories with gauge structure (string landscape), `α` is environmental. | **Informative** — base-rate warning. |
| O9 | ED's existing small dimensionless numbers (`C ≈ 0.03`, `K ≈ 0.0148`) are triad coefficients, not gauge couplings. Conflation risk. | **Manageable** — flag in §5D. |

**Summary.** Four fatal obstacles (O2, O3, O4, O7), two requiring new axioms (O1, O6), three informative (O5, O8, O9). Even under maximal optimism — ruling in all fixable obstacles — you would still face four structural kills. **There is no path through the fatal obstacles without replacing the Canon.**

---

## 7. Assessment

### 7A. Verdict

**No structural path to `α` exists in current ED.** The obstructions are not technical — they are absences: ED has no EM sector, no charge, no gauge symmetry, no Lorentz symmetry, no second quantization. Each of these is a *precondition* for `α` to exist as a meaningful object. Without them, any appearance of `α` in ED-derived algebra would be one of:

- **Numerology.** An algebraic combination of ED invariants that approximates `1/137` without structural reason. Ruled out under (C1)–(C5).
- **Under-determined parameter fit.** Tuning free coefficients of `M` or `P` to land at `α`. Ruled out by (C4).
- **Confusion of analogue with identity.** ED has its own dimensionless constants (`C, K, r*, D_crit`). Calling any of them `α` is a naming error, not a derivation.

### 7B. Direct comparison with Species-Mass scoping

The species-mass scoping memo concluded "dead end" because ED has no species label, but at least had `m` as a bona fide dimensional input via the ED-Dimensional-01 dictionary. The `α` question is **strictly worse**:

- Species-mass: ED has `m` (external input) and needs a discreteness mechanism. Missing one ingredient.
- Fine-structure: ED has no charge, no gauge field, no U(1), no EM sector. Missing four ingredients.

If species-mass is a dead end, `α` is a dead end raised to the fourth power.

### 7C. What would change the verdict

ED would have to acquire, via new axioms:

- (i) A complex scalar or vector field structure (phase + gauge connection).
- (ii) A local U(1) symmetry and associated conservation law.
- (iii) A mechanism that fixes the U(1) coupling to `1/137` at some relevant scale — this is an *additional* problem beyond just adding gauge structure.
- (iv) Emergent Lorentz symmetry (per `ED_Geometry_Emergence_Scoping.md` §7B).

Each of (i)–(iv) is a research program. None exists in ED today.

---

## 8. Recommendation for ED-10 / ED-Quantum Sections

### 8A. Drop the `α` question entirely from ED's research agenda

- **Rationale.** No structural path; pursuing it would be numerology dressed as theory. The scientific opportunity cost is high — cycles spent on `α`-matching are not spent on the live tests (merger-lag, envelope outreach, C7 alternatives).
- **ED-10 reference.** ED-10 in the Interpretations stratum should **not** be expanded to include `α`. Flag in orientation doc if `α` has been informally discussed.
- **ED-Quantum reference.** Nothing in ED-Dimensional-01 or subsequent quantum-regime sections should claim or imply that `α` can be derived from ED. If present, remove or rewrite.

### 8B. Keep open only this narrow subproblem

The P7 triad coefficients `C ≈ 0.03` (ED-Phys-16) and `K ≈ 0.0148` (C7 prediction) are ED's own dimensionless constants. The honest open question is:

> *Are `C` and `K` universal architectural invariants of the ED Canon — i.e., independent of `M(ρ)` shape within the Canon-allowed class — or do they depend on the specific `M` choice?*

This question is **already the live C7 research thread** and does not need a new memo. But when discussing it, **do not conflate it with `α`**. They are different objects: `C` and `K` are nonlinear-sector self-coupling coefficients of a classical scalar PDE; `α` is a gauge coupling of a quantum U(1) theory. The superficial similarity (small dimensionless numbers) is not structural.

### 8C. Public-facing language

When discussing ED and dimensionless constants in lectures, papers, or outreach (the atlas, etc.):

- **Say:** "ED generates its own dimensionless constants — the triad coupling `C ≈ 0.03`, the ED-SC exponent `r* ≈ −1.304`, the oscillation-death threshold `D_crit ≈ 0.896`. These are architectural, not fit."
- **Do not say:** "ED might explain the fine-structure constant." It can't, and claiming it might is scientifically embarrassing when the structural obstacles are this clear.
- **Honest form of the connection:** "Dimensionless constants of Nature like `α` and `m_p/m_e` remain unexplained by all existing frameworks, including ED. ED's contribution is a different class of dimensionless invariants — the architectural numbers that characterise its PDE structure — not an explanation of QED couplings."

### 8D. Deliverable summary

- **This memo.** `theory/Fine_Structure_Constant_Scoping.md` — scoping study, not a derivation.
- **Verdict.** Dead end. Reason: ED lacks the four structural prerequisites (EM sector, charge, U(1), Lorentz) that `α` presupposes.
- **Recommended action.** Drop `α` from ED's agenda. Keep C7 (`C`, `K`) as the live thread, under its own ED-analogue framing — not conflated with QED `α`.
- **Not recommended.** Any attempt to fit ED coefficients to `1/137`. This would be numerology and would damage ED's scientific credibility.

---

## 9. Related Memos

- `theory/Architectural_Canon.md` — Canon P1–P7 and universal invariants.
- `theory/Species_Mass_Spectrum_Scoping.md` — prior scoping memo, similar dead-end verdict; structural obstructions are a subset of those here.
- `theory/ED_Geometry_Emergence_Scoping.md` — prior scoping memo; flagged the Lorentz obstruction (O4) in detail.
- `theory/ED-Dimensional-01-Ext.md` — quantum-regime dictionary (§4 of this memo).
- `theory/Universal_Invariants.md` — list of ED's own dimensionless constants (the `C, K, r*, D_crit` set).

---

**Status.** Scoping only. No new axioms, no new predictions, no updates to Canon. Final verdict: `α` is not available to ED under any current or near-term extension of its axioms. Recommend removing from active research scope.
