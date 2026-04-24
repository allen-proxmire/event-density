# Superconducting-Qubit N_osc Retrodiction — Scaffold

**Date:** 2026-04-24
**Location:** `quantum/retrodictions/sc_qubit_scaffold.md`
**Status:** Scaffold memo. No data extracted, no retrodiction executed. Lays out the framework for testing ED's temporal distinguishing signatures (N_osc ≈ 9, Q ≈ 3.5) against published superconducting-qubit coherence data. Identifies a substantial parameter-mapping derivation task as prerequisite.
**Purpose:** Produce the scaffold that `signature_observable_mapping.md §6` recommended — infrastructure for the first ED temporal-platform retrodiction attempt.

---

## 1. The ED temporal predictions

From the archive-read-resolved `signature_observable_mapping.md`:

### 1.1 N_osc ≈ 9

**Source:** ED-Phys-17 §4.1 — peak-height oscillation count during damped relaxation of a localized density peak. Baseline (single peak, flat background): **8 oscillations**. Range across conditions: **8–19**. Q-C Boundary paper's "8–19 (~9)" matches.

**Regime:** D_E < 0.1 (per Q-C Boundary paper). Under the affine D_P ↔ D_E mapping from `d_variable_disambiguation.md`, this corresponds to specific accessible regions of the participation-ratio `D_P` space.

**Physical content:** number of damped oscillation cycles visible above noise floor when a relaxing density peak is observed as ρ(x_peak, t). Equivalent to an underdamped harmonic oscillator with Q ≈ Q_ED that produces `N_peaks ≈ 2Q/π · ln(A_0/σ_noise)` observable extrema before decaying below detection threshold.

### 1.2 Q ≈ 3.5

**Source:** Q-C Boundary paper. Quality factor of the damped-oscillator envelope in the D_E < 0.1 regime. Not directly derived in ED-Phys-16 at this value (§2.3 canonical simulator gives Q = 6–10 at τ = 100, ζ = 0.5 parameters); Q ≈ 3.5 is a regime-specific prediction at D < 0.1 in the canonical two-channel PDE.

**Relationship to N_osc:** if `A_0 / σ_noise ≈ 30–100` (reasonable experimental SNR), Q ≈ 3.5 produces N_osc ≈ 2Q/π · ln(SNR) ≈ 2.23 × (3.4 to 4.6) ≈ 7.6 to 10.3 observable peaks — **directly consistent with the 8–19 range**.

**Internal consistency:** the Q ≈ 3.5 and N_osc ≈ 9 predictions are the same underlying prediction (underdamped oscillator with envelope decay), expressed in two parameterizations.

### 1.3 Connection to the PDE linearization

From `theory/D_crit_Resolution_Memo.md §3–§5`: the canonical two-channel PDE linearized around homogeneous equilibrium gives

```
λ² + T_k λ + S_k = 0                             (1)
T_k = Dε_k + ζ/τ,  S_k = ε_k(D ζ + H)/τ
```

Underdamping when `T_k² < 4 S_k`. Envelope decay rate `γ = T_k/2`; oscillation frequency `ω = √(S_k − T_k²/4)`. Quality factor `Q = ω / (2γ) = ω/T_k`.

For `D_E ≪ 1` and canonical (ζ, τ, ε_k), the coupling between ρ and v dominates over ρ's own damping; the resulting Q depends sharply on the parameter combination `(D, H = 1 − D, ζ, τ)`.

**Q ≈ 3.5 at D_E < 0.1:** corresponds to specific values of (ζ, τ, ε_k) in the PDE where the linearized eigenvalue ratio gives ~3.5. Without explicit parameter-mapping to a given SC-qubit system, "Q = 3.5" is a structural prediction whose quantitative form at the experiment's operating point needs separate derivation.

---

## 2. Relevant SC-qubit observables

Published SC-qubit coherence data comes in several standard forms. Each is potentially a testbed for N_osc and Q, but with different analysis requirements.

### 2.1 T1 (longitudinal relaxation)

**What it measures:** population decay of excited qubit toward ground. Standard form: `P_1(t) = exp(-t/T_1)` — monotonic exponential decay, N_osc = 0.

**Testability:** Pure T1 data is NOT a test of N_osc. Monotonic exponential is what standard decoherence theory predicts. Unless there is underdamped structure superposed (e.g., from a coupled TLS fluctuator), T1 traces are not informative for this retrodiction.

### 2.2 T2 / T2* (dephasing)

**What it measures:** coherence decay during free evolution between Ramsey π/2 pulses. Standard form: `⟨σ_x⟩(τ) = exp(-τ/T_2) · cos(δ·τ + φ)` where `δ` is detuning and `τ` is the free-evolution time.

**Testability:** The oscillation at detuning frequency `δ` shows many cycles (10s–100s typically) under an exponential envelope. The envelope is monotonic exponential; the oscillations are driven (detuning-frequency), not free damped oscillations of a relaxing excited state. **N_osc in this data is not the ED observable** — the fringes are at detuning frequency, not at a natural oscillation frequency of the dissipative system.

**Caveat:** zero-detuning Ramsey (`δ = 0`) would show pure decay envelope without fringes, recovering a T1-like picture.

### 2.3 Rabi oscillations

**What it measures:** under resonant continuous drive, population oscillates at Rabi frequency `Ω_R = g·E_drive / ℏ`. Decay envelope from T_1 and T_2 effects. Standard form: `P_1(t) = (1/2)[1 - cos(Ω_R t) · exp(-t/T_Rabi)]`.

**Testability:** This IS a damped-oscillation trace — the envelope decays while the population oscillates. Relevant Q = `Ω_R · T_Rabi / 2`. For typical transmon Rabi data: Ω_R ~ 10 MHz, T_Rabi ~ 10 μs → Q ≈ 300 ≫ 3.5. **Rabi oscillations are too high-Q for a direct N_osc = 9 match.**

**Caveat:** the oscillation frequency is drive-set (Ω_R depends on amplitude), not intrinsic. A driven oscillator with high Q is structurally different from ED's predicted free-oscillator behavior.

### 2.4 Free-induction decay (FID) / ring-down

**What it measures:** after a π/2 pulse or a prepared coherent superposition, the system evolves freely. If there is a natural oscillation (e.g., from qubit-resonator coupling), the observable oscillates with envelope decay from T2 and resonator loss.

**Testability:** This is the closest direct analog to ED's N_osc setup. If a published FID/ring-down trace shows N = 8-19 oscillation peaks with Q ≈ 3.5 envelope, that is a direct match. **Requires ring-down data with natural (not drive-set) oscillation frequency and damping.**

**Typical source:** qubit-resonator dispersive readout in strong-coupling regime; qubit coupled to a TLS fluctuator showing beating; Jaynes-Cummings vacuum Rabi oscillations.

### 2.5 Vacuum Rabi oscillations (qubit-cavity strong coupling)

**What it measures:** a qubit prepared in |e⟩ coupled to an initially-empty cavity exchanges excitation with the cavity at the vacuum-Rabi frequency `2g`. Observable: qubit population oscillates with envelope decay from `κ` (cavity loss) and `1/T_1^{qubit}`. Published form: `P_1(t) = cos²(g t) · exp(-(κ + 1/T_1)t)`.

**Testability:** Classic damped-oscillator geometry with natural frequency `2g` and decay rate `(κ + 1/T_1)`. Q = `g / (κ + 1/T_1)`. For typical circuit-QED: g ~ 50 MHz, κ ~ 1 MHz, T_1 ~ 100 μs → Q ≈ 50. **Higher than 3.5 but in the same decade.** For weak-coupling or high-dissipation regimes, Q can drop to ~3–10.

**This is the most promising SC-qubit observable class for N_osc testing** because the oscillation is intrinsic (set by coupling strength, not drive), the envelope is naturally damped, and the Q depends on apparatus parameters that span the relevant range.

### 2.6 Summary

| Observable | Natural oscillation? | Damped envelope? | Typical Q | N_osc testable? |
|---|---|---|---|---|
| T1 decay | No | Yes | N/A | No (monotonic) |
| T2 Ramsey (δ > 0) | Yes (but drive-set detuning) | Yes | 10s–100s | Partial (detuning-driven, not free) |
| Rabi oscillations | Yes (drive-set Ω_R) | Yes | ~100–1000 | Q too high for ED match |
| FID / ring-down with TLS | Yes (natural) | Yes | variable | **Yes** |
| Vacuum Rabi oscillations | Yes (coupling-set 2g) | Yes | 3–100 | **Best match** |

---

## 3. Data-extraction template

For the selected SC-qubit paper (populated later, §6):

### 3.1 Trace digitization

| Field | Value | Source |
|---|---|---|
| Observable | e.g., `P_1(t)` or `⟨σ_z(t)⟩` | — |
| Time range | `t ∈ [0, t_max]` | Figure caption or axis |
| Sampling points | number of data points visible in figure | Count from figure |
| Sampling rate | `Δt` between points | Derived |
| Apparent noise floor | visual estimate from data scatter | — |
| SNR estimate | `A_initial / σ_noise` | Derived |
| Figure reference | Fig. X of [paper] | — |

### 3.2 Oscillation counting

Protocol:

1. Identify the envelope function (fit or visual).
2. Subtract or normalize by the envelope to reveal oscillations.
3. Count peaks above the noise floor in the residual.
4. Report N_osc_measured with uncertainty from noise-floor definition.

```
N_osc_measured = <number of distinguishable peaks>
Uncertainty: ± count of peaks within 2σ of noise floor
```

### 3.3 Q extraction

Two methods:

**Method A (direct fit):** fit `A · cos(ω t + φ) · exp(-γ t) + offset` to the trace. Q = ω / (2γ).

**Method B (peaks vs. envelope):**
- Peaks at `t_n = n · T_osc = n · 2π/ω`
- Envelope value at t_n: `A_n = A_0 · exp(-γ t_n)`
- From two peak ratios: `γ = ln(A_n / A_m) / (t_m - t_n)`
- Q = `ω / (2γ)`

Report Q_measured with propagated uncertainty.

### 3.4 Comparison with ED prediction

- ED predicts: Q = 3.5, N_osc = 8–19 (consistent under SNR-dependent peak-counting).
- If measured Q ≈ 3.5 within ±20%: **consistent**.
- If measured Q > 10 or Q < 1: **not matching** (wrong regime).
- If observed N_osc in [8, 19]: **consistent**.
- Joint consistency on both Q and N_osc is the strong match.

### 3.5 Status flags

Report for each comparison:

- **Match:** consistent within tolerance.
- **Partial match:** one of (Q, N_osc) within tolerance, other outside.
- **No match:** both outside tolerance (possibly wrong regime).
- **Not testing:** data does not exhibit damped oscillations at all (e.g., pure T1 decay); no comparison possible.

---

## 4. The parameter-mapping task (critical blocker)

**Before any measured Q or N_osc from SC-qubit data can be compared meaningfully to ED's predictions, the SC-qubit apparatus must be mapped to the `D_E` parameter space.** This is analogous to ζ_Arndt for matter-wave interferometry, and is similarly non-trivial.

### 4.1 What D_E means for an SC qubit

The PDE (from D_crit Resolution Memo):

```
∂_t ρ = D · F[ρ] + H · v
∂_t v = (F[ρ] − ζ·v) / τ
```

For an SC qubit in a coherent superposition `α|0⟩ + β|1⟩`:

- **ρ candidate:** the local ED density count at the qubit's participation site. In some mappings: `ρ ↔ |ψ|²` (Born-rule probability density, per Dimensional Atlas Madelung anchoring). For a qubit this is `ρ_0 = |α|²`, `ρ_1 = |β|²`.
- **v candidate:** polarity-weighted commitment-rate density. For a qubit: the rate of off-diagonal coherence decay, possibly related to the mean-field coupling of the qubit to its environmental bath.
- **D candidate:** weight of direct ρ-dynamics in the PDE. For a qubit: the fraction of population evolution driven by local (non-mean-field) terms.
- **H = 1 − D:** weight of participation-field mediated evolution.

**None of these identifications is currently derived.** A full primitive-level mapping from SC-qubit Hamiltonian dynamics to the canonical ED PDE is not in the current memos.

### 4.2 Candidate mapping (SPECULATIVE)

Using the affine mapping from `d_variable_disambiguation.md` with N = 2 (two qubit states):

```
D_E = 2 · D_P − 1                               (2)
```

For a qubit in equal-amplitude superposition: `D_P = |α|⁴ + |β|⁴ = 0.25 + 0.25 = 0.5`, giving `D_E = 0`. At `D_E < 0.1`: `D_P < 0.55`, i.e., `|α|⁴ + |β|⁴ < 0.55`, i.e., amplitude-balance parameter `r = |α|²` satisfies `r² + (1-r)² < 0.55` → `r ∈ (0.26, 0.74)`.

**Implication:** a qubit starting in equal superposition and evolving freely is in the D_E < 0.1 regime until decoherence tips the amplitude balance substantially. This is the natural starting regime for free-induction / Ramsey / vacuum-Rabi data. **The N_osc ≈ 9 prediction should apply during this window.**

### 4.3 ζ for an SC qubit

Applying `ζ = Λ · τ` from zeta_derivation.md with:

- `Λ` ↔ decoherence rate `1/T_2`
- `τ` ↔ internal rule-period: qubit frequency inverse `1/ω_q` (roughly 10⁻¹⁰ s for 5 GHz transmon) OR Rabi period `1/Ω_R` depending on whether "rule" is interpreted as computational or driven

For transmon with T_2 ≈ 100 μs (10⁻⁴ s) and ω_q ≈ 5 GHz (τ_rule ≈ 2·10⁻¹¹ s):

```
ζ_SC = Λ · τ ≈ (10⁴ Hz) · (2·10⁻¹¹ s) ≈ 2·10⁻⁷
```

**Extremely small ζ.** D_crit(ζ ≪ 1) ≈ 0.828 — same regime as Arndt.

### 4.4 Is the N_osc prediction reachable?

Under the candidate mapping:

- D_E < 0.1 IS reachable in the natural SC-qubit free-evolution regime (equal-amplitude superposition).
- ζ ≪ 1 means D_crit ≈ 0.828 (boundary), consistent with `D_crit` formula in the small-ζ limit.
- The ED prediction `N_osc ≈ 9, Q ≈ 3.5` applies to the underdamped relaxation in this regime.

**Predicted match with experiment:** time-resolved free-evolution data from an SC qubit in coherent superposition should show Q ≈ 3.5 underdamped oscillations with 8–19 visible peaks — **IF** the candidate parameter mapping (§4.2, §4.3) is correct.

**Status of the candidate mapping:** SPECULATIVE. Requires explicit primitive-level derivation linking SC-qubit Hamiltonian evolution to the ED canonical PDE to promote to CANDIDATE or FORCED.

### 4.5 Honest caveats on the mapping

1. **Ramsey fringes at ω = δ (detuning) are not natural frequencies.** They are drive-set. ED's ω in the underdamped-oscillator picture should be a natural frequency of the dissipative system — more likely Rabi frequency `Ω_R` or vacuum-Rabi `2g`, not Ramsey detuning.

2. **The D_P → D_E affine mapping is already CANDIDATE, not FORCED.** N = 2 channel count is defensible for a qubit but not forced (alternative: N = 2 + |environment|).

3. **Primitive-level qubit description is thin.** Primitives 10 (individuation) and 02 (chain) are the most relevant primitives for a qubit as "single rule-type localized chain" but explicit derivation is not in the primitive memos.

4. **Rabi dynamics are driven, not free.** The N_osc prediction is specifically for free damped relaxation. Driven Rabi oscillations require extension of ED's model to include driving terms, not currently in the PDE.

---

## 5. Candidate SC-qubit papers

Order by accessibility and likelihood of containing the right observable class:

### 5.1 Vacuum Rabi oscillations (preferred platform)

- **Wallraff et al. 2004** (*Nature* 431, 162) — first demonstration of circuit QED vacuum-Rabi splitting. Time-domain data may be in supplementary.
- **Hofheinz et al. 2008** (*Nature* 454, 310) — "Generation of Fock states in a superconducting quantum circuit." Contains ring-down traces of cavity-field oscillations.
- **Hofheinz et al. 2009** (*Nature* 459, 546) — photon-number-state synthesis; detailed time-resolved population data.
- **Kirchmair et al. 2013** (*Nature* 495, 205) — qubit-cavity photon-number Kerr; clean ringing traces.
- **Leghtas et al. 2015** (*Science* 347, 853) — dynamically-protected cat-state preparation.

### 5.2 Qubit-TLS coupling (secondary platform)

- **Simmonds et al. 2004** (*PRL* 93, 077003) — first demonstration of two-level fluctuators causing Rabi-like oscillations in phase-qubit decay. Direct oscillatory-decoherence pattern.
- **Neeley et al. 2008** (*Nature Physics* 4, 523) — coupling between phase qubit and TLS with clear damped oscillations.

### 5.3 Qubit free-evolution traces with visible oscillations

- **Vion et al. 2002** (*Science* 296, 886) — quantronium qubit. Historic; may show clean free-evolution traces.
- **Devoret & Schoelkopf 2013** (*Science* 339, 1169) — review with illustrative plots of damped oscillations.
- **Krantz et al. 2019** (*Applied Physics Reviews* 6, 021318) — pedagogical review; contains multiple example time-traces of different decoherence regimes.

### 5.4 Recommended first dataset

**Kirchmair et al. 2013, *Nature* 495, 205** — "Observation of quantum state collapse and revival due to the single-photon Kerr effect."

**Reason for recommendation:**
- Demonstrates clear oscillatory-decay structure (collapse/revival) with multiple visible peaks.
- Parameter regime (strong-dispersive coupling) produces Q in the range where ED's prediction is potentially matched.
- Published figures show enough time-resolution to count oscillations.
- Widely-cited; readily accessible (arXiv:1211.2228).

**Alternative first choice:** Hofheinz et al. 2009 Figs. 2–3 for Fock-state decay traces.

---

## 6. Execution plan

### 6.1 Phase 0 — parameter-mapping derivation (PREREQUISITE)

**Task:** produce `quantum/effective_theory/sc_qubit_pde_mapping.md` that explicitly maps (qubit Hamiltonian, bath coupling) to (ρ, v, D_E, ζ, τ) in the canonical ED PDE.

**Required derivations:**

1. Qubit state `α|0⟩ + β|1⟩` → ED density ρ(x, t) at the qubit participation site.
2. Environmental bath → commitment-reserve dissipation → ζ_SC formula.
3. Identification of the "natural oscillation frequency" in the SC-qubit context.
4. Mapping from experimental observable `⟨σ_z⟩(t)` (or `P_1(t)`) to the ED oscillator variable whose N_osc is predicted.

**Status:** not yet attempted. Estimated scope: 1 session of focused derivation.

### 6.2 Phase 1 — first retrodiction attempt

**Task:** using the §6.1 mapping, execute the N_osc / Q comparison against the Kirchmair 2013 dataset.

**Steps:**

1. Obtain Kirchmair 2013 PDF / arXiv preprint.
2. Digitize the collapse-revival trace from the published figures.
3. Apply the §3 extraction template.
4. Compute D_E for Kirchmair's operating regime using §6.1 mapping.
5. Verify D_E < 0.1 regime is applicable.
6. Compare measured Q and N_osc to ED predictions (Q = 3.5, N_osc = 8–19).
7. Classify as match / partial match / no match / not testing.

**Output memo:** `quantum/retrodictions/kirchmair2013_verdict.md`.

### 6.3 Phase 2 — cross-dataset check

**Task:** repeat against a second dataset (Hofheinz 2009 or similar) to check whether the first result is a coincidence or a pattern.

### 6.4 Phase 3 — distinguishing from competitors

**Task:** check whether standard decoherence theory, GRW, CSL, or DP also predict the measured Q and N_osc. Only if ED's prediction is distinguishing does a match count as distinguishing evidence.

**Key differentiators:**
- Standard decoherence: monotonic exponential; N_osc = 0 unless driven.
- GRW / CSL: stochastic stepwise decoherence; no specific N_osc.
- DP: gravitationally-induced; typically decoherence timescale >> SC-qubit timescales.

If the SC-qubit data shows clear natural-oscillation structure, standard decoherence already fails; observed underdamping at Q ≈ 3.5 with N_osc ≈ 9 would be ED-consistent + other-framework-inconsistent.

---

## 7. Status classifications

| Claim | Status |
|---|---|
| N_osc ≈ 9 and Q ≈ 3.5 are temporal observables | FORCED (per signature_observable_mapping.md) |
| SC-qubit free-evolution traces are the right observable class | CANDIDATE (best match among standard platforms) |
| Vacuum-Rabi and qubit-TLS systems are the natural Q ≈ 3.5 targets | CANDIDATE |
| D_E < 0.1 corresponds to equal-amplitude qubit superposition under N=2 affine mapping | SPECULATIVE |
| ζ_SC ≈ Λ · τ ≪ 1 → D_crit ≈ 0.828 same-regime as Arndt | SPECULATIVE (depends on correct τ identification) |
| Kirchmair 2013 is the recommended first dataset | CANDIDATE (based on observable type + visibility of oscillations; other datasets may be better once examined) |

---

## 8. What this scaffold does NOT provide

- No SC-qubit data extracted.
- No primitive-level derivation of the SC-qubit → ED PDE mapping.
- No retrodiction executed.
- No measured N_osc or Q values.
- The "Ramsey detuning vs. natural oscillation" distinction is flagged but not fully resolved — the ED N_osc prediction may apply only to natural-frequency oscillations, not detuning-fringe counts.

These are Phase 0 / Phase 1 tasks per §6.

---

## 9. Honest framing

**The SC-qubit retrodiction path is in principle cleaner than matter-wave interferometry** because:
- The temporal observable class is directly accessible (published time traces).
- Signal-to-noise is typically excellent.
- Operating parameters are well-characterized.
- Multiple well-known datasets exist.

**But two substantial gates stand before a verdict can be produced:**

1. **Parameter-mapping derivation.** Without the SC-qubit → ED PDE mapping, "D_E < 0.1" is a statement about an unmapped variable. Approximate mapping candidates (§4.2–§4.4) exist but are SPECULATIVE.

2. **Observable identification within a trace.** Ramsey detuning fringes are not the right observable; Rabi driven oscillations are too high-Q; natural-frequency ring-downs in vacuum-Rabi or TLS-coupled systems are the right class but narrow the dataset selection.

**If both gates are passed:** the first ED temporal retrodiction attempt becomes a roughly one-session task (digitize trace, count peaks, extract Q, compare). That would be the first completed retrodiction in the program.

**Honest estimate:** Phase 0 (mapping derivation) is the hardest step and may surface further structural issues — continuing the pattern where each executed step reveals blockers the proposed step didn't anticipate. The scaffold makes the task tractable; it does not guarantee the task will succeed on first attempt.

---

## 10. Cross-references

- Signature observable mapping: [quantum/effective_theory/signature_observable_mapping.md](../effective_theory/signature_observable_mapping.md)
- D-variable disambiguation: [quantum/effective_theory/d_variable_disambiguation.md](../effective_theory/d_variable_disambiguation.md)
- ζ derivation: [quantum/effective_theory/zeta_derivation.md](../effective_theory/zeta_derivation.md)
- PDE-parameter mapping: [quantum/effective_theory/pde_parameter_mapping.md](../effective_theory/pde_parameter_mapping.md)
- D_crit resolution: [theory/D_crit_Resolution_Memo.md](../../theory/D_crit_Resolution_Memo.md)
- ED-Phys-16 (Q, triad, harmonic origins): [archive/research_history/ED Physics/ED-Phys-16_CoupledOscillators/ED-Phys-16_CoupledOscillators.md](../../archive/research_history/ED%20Physics/ED-Phys-16_CoupledOscillators/ED-Phys-16_CoupledOscillators.md)
- ED-Phys-17 (N_osc origin): [archive/research_history/ED Physics/ED-Phys-17_OscillatorCosmology/ED-Phys-17_OscillatorCosmology.md](../../archive/research_history/ED%20Physics/ED-Phys-17_OscillatorCosmology/ED-Phys-17_OscillatorCosmology.md)
- Arndt verdict (as template for a verdict memo structure): [quantum/retrodictions/arndt_verdict.md](arndt_verdict.md)

---

## 11. One-line summary

> **Superconducting-qubit coherence data (best: vacuum-Rabi oscillations or qubit-TLS coupling traces, NOT T1 decay or Rabi-driven oscillations) is the correct platform class for testing ED's temporal distinguishing signatures N_osc ≈ 9 and Q ≈ 3.5. Under the candidate SC-qubit parameter mapping (N=2 affine D_P ↔ D_E, ζ_SC ≈ Λ·τ_internal), free-evolution of an equal-amplitude superposition should satisfy D_E < 0.1 and therefore exhibit the ED prediction — IF the SPECULATIVE mapping (§4.2–§4.4) is approximately correct. Phase 0 (primitive-level SC-qubit → PDE derivation) is the critical prerequisite; Phase 1 (Kirchmair 2013 Fock-state collapse/revival data as the recommended first retrodiction) executes once Phase 0 is complete. The scaffold makes the task tractable; it does not guarantee success on first attempt.**
