# Distinguishing-Signature Observable Mapping

**Date:** 2026-04-24
**Location:** `quantum/effective_theory/signature_observable_mapping.md`
**Status:** Resolution memo. Archive read of ED-Phys-16 + ED-Phys-17 executed; Problem 2 of `distinguishing_signatures.md` RESOLVED. Produces the observable-type classification and platform map for each of the four distinguishing signatures. Identifies one discrepancy between the Q-C Boundary paper's wording and the underlying ED-Phys findings.
**Purpose:** Determine whether each ED distinguishing signature (N_osc ≈ 9, Q ≈ 3.5, triad coupling ≈ 0.03, 3–6% "third-harmonic") is a temporal, spatial, or mixed observable; assign each to the correct experimental platform class; clarify testability against Eibenberger 2013 and Fein 2019.

---

## 1. Signatures and their ED-Phys origins

Archive files consulted:

- [archive/research_history/ED Physics/ED-Phys-16_CoupledOscillators/ED-Phys-16_CoupledOscillators.md](../../archive/research_history/ED%20Physics/ED-Phys-16_CoupledOscillators/ED-Phys-16_CoupledOscillators.md)
- [archive/research_history/ED Physics/ED-Phys-17_OscillatorCosmology/ED-Phys-17_OscillatorCosmology.md](../../archive/research_history/ED%20Physics/ED-Phys-17_OscillatorCosmology/ED-Phys-17_OscillatorCosmology.md)

### 1.1 N_osc ≈ 9 — peak-height oscillation count during damped relaxation

**Origin (ED-Phys-17 §4):** peak-height oscillations observed when a Gaussian density peak (a proto-particle) relaxes toward equilibrium `ρ_star` under the P_SY2 penalty. §4.1 baseline: **"Peak height oscillations: 8"** for a single peak on flat background. §4.2: 10 on oscillating background. §4.3: 19 on standing-wave background. §4.4: 9 (flat) / 13 (oscillatory). §7.1: 13–14 at various phases. The Q-C Boundary paper's "8–19 (≈ 9)" range matches this span exactly.

**Physical content:** N_osc counts the damped-oscillation cycles of `ρ(x_peak, t)` as the peak height swings around `ρ_star` during its transient. This is a property of ρ *at a fixed spatial location, as a function of time*.

**Observable type: TEMPORAL.** Requires time-resolved measurement of a density-equivalent quantity at a fixed spatial location (or equivalently, at a fixed mode).

**Physical setting in ED:** the relaxation of a localized proto-particle structure. The experimental analog is coherence-evolution of a prepared excited state toward its ground state, in a system where oscillations occur rather than monotonic decay.

### 1.2 Q ≈ 3.5 — quality factor of damped oscillations

**Origin (ED-Phys-16 §2.1, §2.3):** `Q = ω_0 / (2γ)` where `ω_0 = √(K_eff/τ)` and `γ = ζ/(2τ)`. At canonical simulator parameters (τ = 100, ζ = 0.5), ED-Phys-16 Table §2.3 shows Q values ranging from 6.34 (n=4) to 10.08 (n=64) — **not 3.5**.

**Q-C Boundary paper's Q ≈ 3.5:** predicted for the D < 0.1 regime of the canonical two-channel PDE. This uses different parameters than the ED-Phys-16 simulator's canonical (τ = 100, ζ = 0.5). The PDE form in the D_crit Resolution Memo (§2) has `∂_t v = (F[ρ] − ζv)/τ`; the `D < 0.1` Q ≈ 3.5 pairing comes from linearized PDE analysis at the specific parameter combination where the D_P channel is dominant and the participation-field damping is set by ζ/τ.

**Physical content:** Q is a damped-harmonic-oscillator quantity: `Q = (energy stored) / (energy lost per radian)`. Extracted from the ratio of oscillation frequency to damping rate.

**Observable type: TEMPORAL.** Requires time-resolved ring-down of an oscillation; Q is meaningless without a decay curve.

### 1.3 Triad coupling coefficient ≈ 0.03

**Origin (ED-Phys-16 §12.3):** Explicitly defined as:

```
A_generated / A_parent²  ≈  0.76 / 5.0²  =  0.030            (1)
```

from §12.1 where the strongest triad difference-mode `n=16 (=24−8)` reaches amplitude 0.76 starting from parent modes at amplitude 5.0.

**Physical content:** When two Fourier modes at wavenumbers k_1, k_2 are excited in ρ(x, t), the quadratic nonlinearity (from `M(ρ)∇²ρ` and P_SY2 saturation) generates combination modes at k_1 ± k_2 with amplitude proportional to the product A(k_1) · A(k_2) and to the coupling coefficient ≈ 0.03.

**Observable type: MIXED (primarily mode-space).** The coupling can be measured from either:

- **Spatial mode decomposition** at fixed time: FFT of ρ(x) showing the sum/difference mode amplitudes.
- **Temporal mode decomposition** at fixed location: FFT of ρ(x_0, t).
- **Full spatiotemporal mode coupling**: 2D FFT of ρ(x, t).

**For matter-wave interferometry:** the fringe pattern is `counts(z)` at the detector plane — time-averaged over the experiment's integration time. The triad coupling in the underlying ρ(x, t) dynamics would project to the fringe-mode structure IF the detector-plane density preserves the mode-coupling relationships. Whether it does is not currently derived. Primitively-plausible but not demonstrated.

### 1.4 3–6% "third-harmonic" — discrepancy flagged

**Q-C Boundary paper's wording:** "Harmonic generation (3rd / fundamental) 3–6%, D < 0.1, ED-Phys" (the paper's table of distinguishing signatures).

**ED-Phys-16's actual finding (§7.2, §9, §12.1):** 2**nd** harmonic at 3–6% of fundamental, not 3rd.

- §7.2: *"A standing wave at mode n generates its **second harmonic** at 2n with maximum amplitude ~3–6% of the fundamental."*
- §7 Table: n=16 standing wave → n=32 at 3.3% (0.166/5.0); n=32 → n=64 at 5.5% (0.275/5.0).
- §9 classification table: *"Harmonic generation — Yes — Weak-moderate — **2nd harmonics** at 3–6% of fundamental; from quadratic nonlinearity."*
- §12.1 Strongest effects: "Standing wave harmonic 0.275, source n=32, generated **n=64 (=2·32)**." Explicitly the second harmonic.

**Resolution:** **The Q-C Boundary paper's "(3rd / fundamental) 3–6%" appears to be a wording error; the ED-Phys-16 source clearly reports 2nd harmonic at 3–6%.** Either the Q-C Boundary paper mis-transcribed, or it refers to a third-harmonic calculation in a memo not present in the archive. The `3-6%` amplitude value is accurately cited; the harmonic order (2nd vs. 3rd) is not.

**Physical content (corrected):** A standing wave in ρ(x, t) at spatial wavelength d generates a second-harmonic spatial component at wavelength d/2 with amplitude 3–6% of the fundamental, via the quadratic `M(ρ)∇²ρ` and penalty-saturation nonlinearities.

**Observable type: SPATIAL (in the standing-wave regime) / MIXED (in general).** The 2nd-harmonic generation is a spatial-mode relationship in the ρ(x) pattern at a given time. For a damped standing wave, both fundamental and 2nd harmonic decay in time but the 3–6% ratio is preserved during the decay.

**For matter-wave interferometry:** the fringe pattern `counts(z)` has a fundamental Fourier component at wavelength `d_g` (grating period). A 3–6% second-harmonic at wavelength `d_g/2` would be a specific testable prediction IF ED's nonlinear mode-coupling physics projects onto the Talbot-Lau detector-plane density. This projection derivation is not currently in the ED literature.

---

## 2. Platform map

### 2.1 Observable-type → platform mapping

| Observable type | Accessible in |
|---|---|
| **Temporal** (ρ(x_0, t) or coherence evolution) | Cavity QED (Rabi oscillations), superconducting qubits (T1, T2 decay), optomechanics (mechanical ring-down) |
| **Spatial** (ρ(x) at fixed time, or time-averaged) | Matter-wave interferometry (Eibenberger, Fein), neutron / X-ray scattering, BEC density imaging |
| **Mode-space** (Fourier decomposition of ρ) | Standing-wave experiments in BECs, photonic lattices, cold-atom optical lattices |
| **Spatiotemporal** | Time-resolved imaging of density fields (high-speed BEC imaging, fluid-analog systems) |

### 2.2 Signature-to-platform assignment

| Signature | Observable type | Best platform | Matter-wave testable? |
|---|---|---|---|
| N_osc ≈ 9 | Temporal | Cavity QED population oscillation, SC-qubit T2 decay | No (fringe data is time-averaged) |
| Q ≈ 3.5 | Temporal | Same | No |
| Triad coupling ≈ 0.03 | Mixed (mode-space) | BEC multi-mode excitation with mode-resolved imaging; spatiotemporal Fourier analysis | Weak yes, in principle (fringe-mode harmonics); projection derivation required |
| 3–6% 2nd harmonic (corrected from 3rd) | Spatial (in standing-wave regime) | Standing-wave BEC, photonic lattice density harmonics, high-resolution fringe Fourier analysis | Weak yes, in principle; projection derivation required |

---

## 3. Signature table (comprehensive)

| Signature | Observable type | Platform | Testable with existing Eibenberger/Fein data? | Notes |
|---|---|---|---|---|
| **N_osc ≈ 9** | Temporal: peak-height oscillations in ρ(x_peak, t) during damped relaxation | Cavity QED Rabi-oscillation data; SC-qubit free-evolution traces; optomechanical ring-down | **No** — requires time-resolved trace, not fringe snapshot | Directly from ED-Phys-17 §4.1 baseline; source-referenced correctly in Q-C Boundary paper |
| **Q ≈ 3.5** | Temporal: quality factor of damped oscillation | Same as N_osc | **No** — requires time-resolved decay envelope | ED-Phys-16 §2.1 canonical simulator gives Q = 6–10; Q = 3.5 is a PDE-level prediction at different parameters (D < 0.1 regime) |
| **Triad coupling ≈ 0.03** | Mixed: `A_gen / A_parent² ≈ 0.03` mode-coupling | BEC multi-mode excitation with mode-resolved density imaging; any system supporting controlled multi-mode excitation | **No** directly; in principle via spatial Fourier of fringe data + theory link | Directly from ED-Phys-16 §12.3; weak coupling constant of quadratic nonlinearity in ρ(x,t) dynamics |
| **3–6% 2nd harmonic** (Q-C Boundary paper says "3rd", ED-Phys-16 says "2nd") | Spatial in standing-wave regime: fundamental at mode n, 2nd harmonic at mode 2n | Standing-wave BEC harmonic generation; fringe-pattern Fourier at d_g/2 period (high-resolution) | **Possibly**, with caveats: requires detector-plane projection derivation + high-resolution fringe data | ED-Phys-16 §7.2 says 2nd, not 3rd — Q-C Boundary paper wording discrepancy flagged |

---

## 4. Testability statements

### 4.1 Testable with Eibenberger 2013 and Fein 2019

- **None of the four distinguishing signatures is directly testable against the published Eibenberger 2013 and Fein 2019 datasets.**
- N_osc and Q are temporal quantities; fringe patterns are spatial snapshots (time-averaged).
- Triad coupling and 2nd harmonic are in-principle spatially-accessible, but the derivation linking ρ(x, t) nonlinear mode generation in ED to Talbot-Lau detector-plane fringe harmonics does not exist in the current memos.
- Existing V-vs-P and V-vs-(single mass) data in these papers is at resolution ~25–50 points per scan; a 3–6% 2nd-harmonic signal in a 25–33% fundamental has absolute amplitude 0.8–2%, below the 5% noise floor in the published data.

### 4.2 Require temporal platforms

- **N_osc ≈ 9:** time-resolved oscillation counting in cavity QED, SC qubit, or optomechanical data.
- **Q ≈ 3.5:** Q-factor extraction from time-resolved ring-down data.
- Both are naturally measured in these platforms; published data in any of the three classes likely contains testable cases if the underlying D_E value can be identified.

### 4.3 Require new derivation work

- **Triad coupling ≈ 0.03 in matter-wave context:** requires derivation linking ED mode-coupling in ρ(x, t) to Talbot-Lau fringe-mode harmonics. Not currently in literature.
- **Wording resolution for 3rd vs. 2nd harmonic:** the Q-C Boundary paper's notation should be corrected (or a separate derivation producing 3rd harmonic found) before a well-defined 3rd-harmonic prediction exists.
- **Q = 3.5 parameter-identification:** requires pinning down which PDE parameter set (τ, ζ, D) corresponds to the D < 0.1 regime predicted to have Q = 3.5; current ED-Phys-16 canonical simulator gives Q = 6–10. This is likely a regime-specific prediction that would need derivation to map to any given experiment's operating conditions.

---

## 5. Corrected testability map

### 5.1 The ED program's testable predictions, classified by platform

**Matter-wave interferometry (Eibenberger, Fein, future high-mass experiments):**

- `V_c_measurable ≈ 0.10–0.12` at the Q-C transition (from visibility_to_bandwidth.md + apparatus_envelope.md). **Requires mass-sweep data reaching below V ≈ 0.12.**
- Two-point coherence-trajectory extrapolation: Q-C crossing at ~140,000–250,000 amu (requires data substantially beyond current 25,000 amu reach, OR a third data point in the 50–100 kDa range to sharpen the extrapolation).
- `D_P` level predictions only (per d_variable_disambiguation.md).

**Temporal-coherence platforms (cavity QED, SC qubits, optomechanics):**

- `N_osc ≈ 9` oscillations during damped relaxation.
- `Q ≈ 3.5` quality factor (regime-specific).
- `D_E` level predictions (per d_variable_disambiguation.md).

**BEC / photonic-lattice / standing-wave platforms:**

- `3–6% 2nd harmonic` (corrected from 3rd) in standing-wave density patterns.
- `0.03 triad coupling coefficient` in multi-mode excitation experiments.
- Cleanest platforms to test the nonlinear mode-coupling predictions from ED-Phys-16.

### 5.2 What this means for the ED program's testability state

Previously (before this memo):
- Matter-wave Q-C crossing: blocked on data.
- Distinguishing signatures: blocked on Problem 1 (reachability) + Problem 2 (observable-type).

Now (after this memo):
- Matter-wave Q-C crossing: still blocked on data, but Problem 1 resolved via d_variable_disambiguation.md (Eibenberger/Fein sit inside D_E < 0.1 regime via affine mapping).
- **Temporal signatures: unblocked at the observable-type level. Now blocked on platform-data selection.** Specifically, obtaining and analyzing a specific dataset from cavity QED / SC qubits / optomechanics where the D_E regime is identifiable.
- **Spatial mode-coupling signatures: partially unblocked.** Requires additional derivation connecting ρ(x, t) mode structure to the observable density pattern in a given platform.

---

## 6. Recommended next step

**Survey of temporal-coherence platform data for N_osc-detectable signatures.**

**Rationale:** N_osc is the cleanest ED distinguishing prediction — an integer oscillation count (8–19, centered at ~9) that standard decoherence theory does not produce. Any published time-resolved coherence-decay dataset in cavity QED, superconducting qubits, or optomechanics should have this directly extractable. The signature is qualitative (does the decay oscillate at all?) as well as quantitative (how many times?). Published Ramsey traces, Rabi-oscillation decay curves, and mechanical ring-down data all contain this information in visually inspectable form.

**Specific candidates** (order = most likely to have accessible data):

1. **Superconducting qubit T1/T2 data** — routinely published with detailed time traces. Groups: Devoret (Yale), Martinis (UCSB / Google), Clarke (Berkeley), Oliver (MIT Lincoln).
2. **Cavity QED Rabi-oscillation data** — Haroche-group (ENS Paris) Rydberg-atom-in-microwave-cavity work; well-characterized oscillating coherence decays.
3. **Optomechanical mechanical ring-down** — Aspelmeyer (Vienna), Painter (Caltech); mechanical-mode coherence times directly measured.

**Target memo:** `quantum/retrodictions/temporal_signature_scaffold.md` — data-extraction template with fields for oscillation count, decay envelope, Q-factor extraction.

**Honest caveat:** the D_E regime-identification problem means we need to determine which datasets correspond to D_E < 0.1 (the regime where N_osc ≈ 9 is predicted) before the comparison is well-defined. This is a parameter-mapping task similar to ζ for Arndt: given a specific platform's operating conditions, compute its D_E. Requires further derivation work, but the temporal observable is at least present in principle.

---

## 7. Corrections to prior memos flagged

- `distinguishing_signatures.md §1` should be updated to note that the "3rd harmonic" wording from the Q-C Boundary paper is inconsistent with ED-Phys-16's "2nd harmonic" finding.
- `distinguishing_signatures.md §3` concerning temporal vs. spatial nature of the signatures is now definitively resolved for three of four (N_osc, Q, triad); the 2nd-harmonic case is primarily spatial.
- `d_variable_disambiguation.md §7.3` (what-is-testable-where table) should be cross-referenced with §3 of this memo; the platform assignments are refined here.

None of the verdict memos (`arndt_verdict.md`, `fein2019_verdict.md`) require amendment — their conclusions (consistent-weak-form, not testing the distinguishing signatures, not crossing the Q-C boundary) stand. The `V_c` prediction chain is unaffected.

---

## 8. Status classifications

| Claim | Status |
|---|---|
| ED-Phys-17 §4 reports peak-height oscillation counts of 8–19 centered near 9 | FORCED (direct archive read) |
| N_osc is a temporal observable | FORCED (by definition of peak-height-oscillation-in-time) |
| ED-Phys-16 §12.3 defines triad coupling coefficient ≈ 0.03 | FORCED (direct archive read) |
| ED-Phys-16 §7.2, §9, §12.1 report 2nd harmonic at 3–6%, not 3rd | FORCED (direct archive read) |
| Q-C Boundary paper's "3rd / fundamental 3–6%" is a wording error | CANDIDATE (simplest explanation; alternative is a separate calculation not found in archive) |
| N_osc and Q require time-resolved platform data | FORCED (observable type dictates) |
| Triad coupling projects onto fringe-mode harmonics | SPECULATIVE (requires projection derivation not yet done) |
| 2nd harmonic testable in Eibenberger/Fein fringe data | SPECULATIVE (requires derivation + finer-resolution data than published) |
| SC qubit / cavity QED / optomechanics as best N_osc platforms | FORCED (observable-type match) |

---

## 9. Summary

**Achieved in this memo:**

1. Archive read of ED-Phys-16 + ED-Phys-17 executed.
2. **Problem 2 of `distinguishing_signatures.md` RESOLVED.** N_osc and Q are temporal; triad coupling is mixed / mode-space; 2nd harmonic is spatial in standing-wave regime.
3. Identified the "3rd vs. 2nd harmonic" wording discrepancy between Q-C Boundary paper and ED-Phys-16 source. ED-Phys-16 source reports 2nd harmonic at 3–6%; Q-C Boundary paper wording appears to be an error.
4. Produced the signature-to-platform mapping: matter-wave interferometry cannot test N_osc or Q; cavity QED / SC qubits / optomechanics can.
5. Identified SC qubit T1/T2 data as the most-likely-accessible near-term target for an N_osc retrodiction test.

**Not achieved:**

1. No test executed against any temporal-platform dataset — requires the data retrieval step flagged as next.
2. The detector-plane projection derivation for triad coupling and 2nd harmonic in matter-wave context — deferred as SPECULATIVE.
3. Q-C Boundary paper wording correction — left as a flagged discrepancy.

**Honest bottom line:** the distinguishing-signature path is now properly framed. Matter-wave interferometry data cannot test N_osc or Q; temporal-platform data can. The program has a clear next task (temporal-platform data survey) and a clarified testability map. The ED program now has predictions at two independently-testable levels: D_P (matter-wave) and D_E (temporal platforms).

---

## 10. Cross-references

- Distinguishing-signature analysis (Problem 2 resolved here): [quantum/retrodictions/distinguishing_signatures.md](../retrodictions/distinguishing_signatures.md)
- D-variable disambiguation (platform-level separation): [quantum/effective_theory/d_variable_disambiguation.md](d_variable_disambiguation.md)
- Visibility → D map: [quantum/effective_theory/visibility_to_bandwidth.md](visibility_to_bandwidth.md)
- ζ derivation: [quantum/effective_theory/zeta_derivation.md](zeta_derivation.md)
- Apparatus envelope: [quantum/effective_theory/apparatus_envelope.md](apparatus_envelope.md)
- Eibenberger verdict: [quantum/retrodictions/arndt_verdict.md](../retrodictions/arndt_verdict.md)
- Fein verdict: [quantum/retrodictions/fein2019_verdict.md](../retrodictions/fein2019_verdict.md)
- Q-C Boundary paper (source of signature list): [quantum/papers/Q-C Boundary_Transition. Theory, Prediction, Path.pdf](../papers/Q-C%20Boundary_Transition.%20Theory,%20Prediction,%20Path.pdf)
- ED-Phys-16 (triad, 2nd harmonic origin): [archive/research_history/ED Physics/ED-Phys-16_CoupledOscillators/ED-Phys-16_CoupledOscillators.md](../../archive/research_history/ED%20Physics/ED-Phys-16_CoupledOscillators/ED-Phys-16_CoupledOscillators.md)
- ED-Phys-17 (N_osc origin): [archive/research_history/ED Physics/ED-Phys-17_OscillatorCosmology/ED-Phys-17_OscillatorCosmology.md](../../archive/research_history/ED%20Physics/ED-Phys-17_OscillatorCosmology/ED-Phys-17_OscillatorCosmology.md)

---

## 11. One-line summary

> **Archive read resolves Problem 2 of `distinguishing_signatures.md`: N_osc ≈ 9 is temporal (peak-height oscillation count from ED-Phys-17 §4.1), Q ≈ 3.5 is temporal (damped-oscillator quality factor), triad coupling ≈ 0.03 is mixed-mode-space (from ED-Phys-16 §12.3), and the "3rd harmonic" is actually 2nd harmonic at 3–6% (from ED-Phys-16 §7.2) — Q-C Boundary paper wording is inconsistent with source. Matter-wave interferometry (Eibenberger, Fein) cannot test any of the four; temporal-coherence platforms (cavity QED, superconducting qubits, optomechanics) can test N_osc and Q directly. Recommended next step: survey published SC-qubit T1/T2 data for N_osc signatures.**
