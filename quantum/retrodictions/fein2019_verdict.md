# Fein 2019 Retrodiction — Verdict Memo

**Date:** 2026-04-24
**Location:** `quantum/retrodictions/fein2019_verdict.md`
**Source data:** Fein, Geyer, Zwick, Kiałka, Pedalino, Mayor, Gerlich, Arndt (2019), "Quantum superposition of molecules beyond 25 kDa," *Nature Physics* **15**, 1242–1245. Figures 1, 2, 3 inspected directly.
**Status:** **Verdict: CONSISTENT (weak-form), NOT TESTING. Same epistemic class as Eibenberger 2013.** Fein 2019 is the record-setting matter-wave interference demonstration at ~25,000 Da but, like Eibenberger 2013, does not report a Q-C transition measurement. A new structural observation emerges from combining the two datasets: an ED-framework-motivated *two-point coherence trajectory* that extrapolates the Q-C-crossing prediction to masses well above the current experimental state-of-the-art.

---

## 1. Data extracted from Fein 2019

### 1.1 Apparatus (Fig. 1, caption)

| Quantity | Value | Source |
|---|---|---|
| Apparatus | LUMI (Long-Baseline Universal Matter-wave Interferometer) | Fig. 1a |
| Grating period `d` (G1, G3) | `266 nm` | Fig. 1 caption |
| Grating open fraction `f` | `0.43` | Fig. 1 caption |
| Grating thickness | `160 nm` | Fig. 1 caption |
| Slit width `s = f · d` | `≈ 114 nm` | Derived |
| Optical grating `G2` wavelength `λ` | `532 nm` | Fig. 1 caption |
| Vertical beam waist `w_y` | `690 μm` | Fig. 1 caption |
| Horizontal beam waist `w_x` | **PENDING** (not in Fig. 1 caption) | Methods section |
| Inter-grating distance `L` | `0.98 m` | Fig. 1 caption |
| Laser pulse characteristics | `532 nm, 1 kHz, I ≈ 1 × 10⁸ W/cm²` | Fig. 1 caption |
| Molecular source | nanosecond laser desorption | Fig. 1 caption |
| Velocity encoding | pseudo-random chopper (TOF) | Fig. 1 caption |
| Detection | electron-impact ionization + QMS | Fig. 1 caption |
| Molecular velocity `v` | **PENDING** | Methods section |
| Velocity spread `Δv` | **PENDING** | Methods section |

### 1.2 Molecular library (Fig. 1b, 1c)

| Quantity | Value | Source |
|---|---|---|
| Molecular structure | tetraphenylmethane core + 4 zinc-coordinated porphyrin branches, each with up to 15 fluoroalkylsulfanyl chains (R = F or C₁₀F₁₇S) | Fig. 1b |
| Mass library range (MALDI-TOF) | approximately 20,000–30,000 Da | Fig. 1c |
| Dominant peaks (visual estimate from Fig. 1c) | ~25,000–27,000 Da | Fig. 1c |

### 1.3 Interference data (Fig. 2)

**Fig. 2a — Single interference scan:**
- Laser power `P = 1.2 W`
- Transverse-displacement range `0–1000 nm`
- Sinusoidal-fit visibility: **`V = 25 ± 3%`**

**Fig. 2b — Visibility vs. laser power:**
- Quantum-model peak visibility (blue curve, after 0.93 scaling): `V ≈ 33%` at `P ≈ 1 W`
- Classical-model peak visibility (red curve, after 0.93 scaling): `V ≈ 5%` at `P ≈ 0.3 W`
- Noise floor (grey shading): `V ≈ 5%`
- Data points span `P ∈ [~0.5, ~3.5] W`

**Approximate data-point readings from Fig. 2b:**

| P (W) | V (%, approx) | Error bar (approx) |
|---|---|---|
| 0.75 | 20 | ±5 |
| 1.0 | 20 | ±5 |
| 1.2 | 25 | ±3 (from 2a) |
| 1.5 | 18 | ±5 |
| 2.0 | 12 | ±5 |
| 2.5 | 10 | ±5 |
| 3.0 | 5 | ±3 |

All readings visual; specific numerical values should be verified if used for precision analysis.

### 1.4 Macroscopicity (Fig. 3a, equation (2))

From equation (2) in the paper:
```
μ = log₁₀[(1/ln(η)) · (m/m_e)² · (τ/1 s)] = 14.1
```

This places Fein 2019 at the highest macroscopicity of any matter-wave experiment in the Fig. 3a timeline (red diamond in 2019), exceeding previous records from BECs (red plus), molecules (green circles), atoms (purple squares), and neutrons (blue cross).

### 1.5 CSL bounds (Fig. 3b)

Fein 2019 reports bounds on Continuous Spontaneous Localization model parameters `(r_c, λ)`, with the new experimental bound in green shading on a plot with axes `r_c` (m) vs. `λ` (s⁻¹). The experiment rules out a region of CSL parameter space that previous interferometric bounds did not reach. Error bars per Adler's proposed values are shown. This is the paper's primary distinguishing test — constraining CSL, not directly measuring a Q-C transition.

### 1.6 Critical observation: this is NOT a mass-sweep

Like Eibenberger 2013, Fein 2019 reports visibility at a single molecular library (mass ~25,000 Da) as a function of **laser power**, not as a function of mass. The mass-spectrum in Fig. 1c shows the library but the visibility analysis in Fig. 2 is at a single operating regime of the apparatus.

**Implication:** the scaffold §5 decision-tree ("does V(m) cross below V_c_measurable_LUMI?") does not apply directly. Fein 2019 is structurally analogous to Eibenberger 2013 but at higher mass.

---

## 2. Envelope correction for LUMI

### 2.1 Empirical V_env_LUMI

From the quantum-prediction curve peak in Fig. 2b:

```
V_env_LUMI ≈ 0.33                                (1)
```

(read directly from the blue curve's maximum, which occurs at `P ≈ 1 W`). This is LUMI's apparatus-limited maximum visibility with perfect coherence under these operating conditions.

**Comparison to Eibenberger KDTLI:** Eibenberger 2013 had `V_env ≈ 0.40`. LUMI has a lower envelope (0.33). This reflects differences in:
- Longer baseline (2 × 0.98 m = 1.96 m vs. KDTLI's shorter geometry)
- Lower molecular velocities for higher-mass molecules (longer Talbot time, but also more velocity-averaging attenuation)
- Possibly different open-fraction or detection efficiency

### 2.2 Envelope-corrected ED prediction

```
V_c_measurable_LUMI = V_env_LUMI × V_c_raw = 0.33 × 0.304 ≈ 0.100      (2)
```

**This is the ED-predicted visibility at the Q-C boundary for LUMI operating conditions.**

---

## 3. Comparison with measured data

### 3.1 Record-mass data point

| Quantity | Value | Interpretation |
|---|---|---|
| `V_measured(25,000 Da, P=1.2 W)` | `0.25 ± 0.03` | Fig. 2a fit |
| `V_env_LUMI` | `≈ 0.33` | Fig. 2b quantum peak |
| `V_coh = V_measured / V_env` | `≈ 0.76` | Coherence fraction |
| `V_c_raw` (ED prediction) | `0.304` | Q-C boundary in coherence-fraction terms |
| `V_c_measurable_LUMI` | `≈ 0.100` | Q-C boundary in raw visibility |
| Ratio `V_measured / V_c_measurable` | `≈ 2.5` | Measured is 2.5× the Q-C boundary |

### 3.2 Verdict on the record-mass molecule

**V_coh ≈ 0.76 vs. V_c_raw = 0.304.** The ~25,000 Da molecule at Fein 2019 operating conditions is **operating at 76% coherence fraction, 2.5× the ED-predicted Q-C boundary**. Firmly in the quantum regime, not at the boundary.

Equivalent in raw-visibility terms: `V_measured = 0.25` vs. `V_c_measurable = 0.10`, a 2.5× margin.

### 3.3 High-power data points

At `P ≈ 3 W` in Fig. 2b, V drops to ≈ 0.05, which is below `V_c_measurable_LUMI ≈ 0.10`. **However, this is NOT a Q-C transition.** High laser power takes `φ₀` past the first Bessel-function peak; the drop in visibility is diffraction physics (loss of first-harmonic amplitude), not coherence loss. The quantum-prediction curve itself (which is fully coherent) shows the same drop to ≈ 0.05 at these powers.

**Critical discrimination:** coherence-loss drop (physical Q-C transition) vs. envelope drop (diffraction artifact). The envelope-corrected framework correctly distinguishes these: `V_coh = V_measured / V_env`. At `P ≈ 3 W`, `V_env` itself is near 0.05, so `V_coh ≈ 0.05 / 0.05 ≈ 1` — the data is consistent with full coherence even though the raw visibility is very low. **Coherence is NOT lost; the apparatus is operating in a diffraction-minimum regime.**

**This is exactly why the envelope correction is essential.** Without it, the `V ≈ 0.05` at `P = 3 W` could be misread as a Q-C crossing. Properly corrected, it shows no coherence loss at all.

---

## 4. Verdict

**CONSISTENT (weak-form), NOT TESTING.** Same epistemic class as Eibenberger 2013.

- **Not refuted**: Fein 2019's record-mass molecule operates at 76% coherence fraction, consistent with ED's prediction that the Q-C boundary is at 30%.
- **Not confirmed in a distinguishing sense**: standard decoherence theory also predicts the molecule should be in the quantum regime at LUMI operating conditions; ED and competitors are indistinguishable from this data alone.
- **Not testing**: the Q-C boundary at `V_coh = 0.30` is not reached anywhere in the Fein 2019 data when envelope corrections are applied properly.

The paper's own focus (CSL bounds, macroscopicity record) is a different kind of test; the ED retrodiction framework as currently derived does not generate comparable CSL-bound or macroscopicity predictions.

---

## 5. Combining Eibenberger 2013 and Fein 2019

### 5.1 Two-point coherence trajectory

With both datasets now analyzed under the same envelope-corrected framework:

| Experiment | Mass (amu) | V_measured (peak) | V_env | V_coh |
|---|---|---|---|---|
| Eibenberger 2013 (L12, KDTLI) | ~10,000 | 0.33 | ~0.40 | ~0.82 |
| Fein 2019 (25 kDa library, LUMI) | ~25,000 | 0.25 | ~0.33 | ~0.76 |

### 5.2 Coherence-fraction extrapolation to V_c_raw = 0.30

Two data points allow a first-order extrapolation to the mass at which `V_coh = 0.304` (the ED-predicted Q-C boundary):

**Linear extrapolation** (`V_coh linear in m`):
- Slope: `ΔV_coh / Δm = (0.76 − 0.82) / (25000 − 10000) = −0.06 / 15000 ≈ −4 × 10⁻⁶ /amu`
- Crossing at: `m_c ≈ 10000 + (0.82 − 0.30) / 4 × 10⁻⁶ ≈ 140,000 amu`

**Exponential extrapolation** (`V_coh = V_0 · exp(−m / m_0)`):
- Fit: `ln(0.82 / 0.76) = 15000 / m_0` → `m_0 ≈ 200,000 amu`
- Crossing at: `m_c ≈ m_0 · ln(V_0 / 0.30) ≈ 200,000 · 1 = ~240,000 amu`

**ED-framework extrapolated prediction:** the Q-C boundary crossing, under linear or exponential extrapolation of the two-point coherence trajectory, occurs at a molecular mass of approximately **140,000–250,000 amu**.

### 5.3 Caveats on the extrapolation

Several reasons this is a weak prediction:

- **Two points do not constrain a curve.** Linear and exponential forms give different m_c (factor ~1.7); a single additional data point in the 50,000–100,000 Da range would fix the functional form.
- **The two apparatus are different.** KDTLI and LUMI envelope corrections are applied separately, but residual apparatus-specific factors in how `V_coh` was extracted may bias the comparison.
- **Apparatus-specific decoherence mechanisms.** Λ(m) depends on apparatus (gas pressure, thermal-photon emission, internal-state dynamics). The coherence trajectory reflects both mass-intrinsic and apparatus-intrinsic decoherence.
- **The ED derivation chain itself has three upstream CANDIDATE commitments.** Each affects `V_c_raw`; the 0.30 value is not itself forced.

### 5.4 What this extrapolation says

**If the two-point trajectory is accurate to within a factor of ~2, the ED-predicted Q-C boundary is at molecular masses 5–10× larger than the current Arndt-group experimental state-of-the-art.** Reaching this mass scale is the subject of next-generation interferometer designs — MAQRO (space-based), larger-baseline LUMI variants, etc.

This suggests that **the Q-C transition, as predicted by ED, may be beyond current experimental capability entirely.** The framework would then remain "consistent but not testing" until experimental reach improves.

Alternatively, **the distinguishing signatures** (`N_osc ≈ 9`, 3–6% third-harmonic) predicted by ED but not by standard decoherence theory may be observable *within* the current quantum-regime data without requiring a Q-C boundary crossing. Those remain the under-investigated path to a distinguishing test.

---

## 6. What Fein 2019 *does* test that is not captured here

### 6.1 CSL bounds

Fein 2019's primary distinguishing test is the CSL-parameter-space exclusion in Fig. 3b. This tests Continuous Spontaneous Localization — a competing framework to standard QM and to ED. The bounds exclude a region of `(r_c, λ)` space.

**ED analog:** ED has no direct CSL mapping in the current derivation chain. A separate derivation (`quantum/effective_theory/csl_comparison.md`, hypothetical) would be needed to translate ED's primitive-level commitment dynamics into an (r_c, λ)-equivalent parameter set for comparison with Fig. 3b bounds.

This is a Phase 2/3 task not undertaken in this session.

### 6.2 Macroscopicity

Equation (2) in Fein 2019:
```
μ = log₁₀[(1/ln(η)) · (m/m_e)² · (τ/1 s)] = 14.1
```

This is a model-specific metric (based on the macro-realism proposal by Nimmrichter-Hornberger 2013). ED has no direct structural translation of μ; a primitive-level derivation of what "macroscopicity" means in ED terms is open.

---

## 7. Honest framing

**What this session achieved for Fein 2019:**

1. Extracted data directly from Figs. 1, 2, 3.
2. Applied envelope correction to LUMI (V_env ≈ 0.33).
3. Computed envelope-corrected ED prediction V_c_measurable_LUMI ≈ 0.10.
4. Confirmed V_measured(25 kDa) = 0.25 corresponds to V_coh ≈ 0.76, well above V_c_raw = 0.30.
5. Correctly diagnosed the high-power visibility drop as diffraction, not coherence loss (§3.3).
6. Generated a first-order two-point extrapolation to the ED-predicted mass of Q-C crossing: ~140,000–250,000 amu.

**What this session did NOT achieve:**

1. A completed Q-C-crossing retrodiction. Fein 2019, like Eibenberger 2013, does not reach the ED boundary.
2. A distinguishing test vs. standard decoherence theory or CSL.
3. A derivation of ED's analog of CSL bounds or macroscopicity.

**Status of the Path C retrodiction program after this session:**

- **Eibenberger 2013 and Fein 2019 both produce "consistent, not testing" verdicts.**
- **No currently-published Arndt-group dataset reaches the ED-predicted Q-C boundary.**
- **The two-point extrapolation suggests the Q-C boundary is at molecular masses 5–10× larger than current experimental reach.**
- **Distinguishing tests (N_osc ≈ 9, 3–6% third-harmonic) remain the under-investigated alternative path.**

**Honest implication for the overall program:**

Path C in its current framing — threshold-crossing retrodiction via molecular interferometry — may require next-generation experimental capability before it can execute. The theoretical framework is in place; the empirical data is not yet in the right regime. This is not a failure of the framework; it is a statement about where the current experimental front lies.

The more promising near-term distinguishing tests are:
- Non-molecular-interferometry platforms (optomechanics, cavity QED, superconducting qubits) where the Q-C parameter regime may be differently accessible
- Distinguishing-signature checks (N_osc ≈ 9, harmonic structure) within existing datasets
- Cosmological tests (η derivation, Phase 4) which test different aspects of the framework

---

## 8. Next-priority actions

### 8.1 Distinguishing-signature analysis

ED predicts (per Q-C Boundary paper): N_osc ≈ 9, Q ≈ 3.5, triad ≈ 0.03, 3–6% third-harmonic — all in the `D < 0.1` sector. These are ED-specific predictions not made by standard decoherence or CSL.

**Task:** check Eibenberger 2013 and/or Fein 2019 interference patterns (Fig. 3a and Fig. 2a respectively) for these signatures. The sinusoidal fit applied in both papers assumes pure first-harmonic structure; deviations from pure-sinusoid could contain the ED-specific third-harmonic signal.

**Target memo:** `quantum/retrodictions/distinguishing_signatures.md`.

### 8.2 Non-molecular-interferometry platform selection

The three candidates from the Arndt scaffold §1 (Haroche cavity QED, Devoret-Martinis-Clarke superconducting qubits, Aspelmeyer optomechanics) each have different Q-C parameter ranges. One or more may be in a regime where the ED boundary is reachable with published data.

**Task:** survey which of these has the clearest coherence-fraction-vs-control-parameter data and redo the retrodiction there.

### 8.3 CSL-to-ED parameter bridge

Fein 2019 Fig. 3b constrains CSL. If ED's structural commitment dynamics can be mapped to an effective (r_c, λ)-like parameter pair, Fein 2019's bounds would directly apply to ED.

**Task:** derive the CSL-to-ED parameter bridge. This is Phase 2/3 work; non-trivial.

### 8.4 Distinguishing test via N_osc ≈ 9 signature

`Q-C Boundary_Transition. Theory, Prediction, Path.pdf` specifies N_osc ≈ 9 oscillation count on the quantum side. This is a transient-oscillation phenomenon in PDE solutions at small `D`. Whether it manifests in sinusoidal-interference-fringe datasets is unclear — it may be a specific temporal structure that requires time-resolved rather than fringe-pattern data. Clarifying this is a precursor to §8.1.

---

## 9. Cross-references

- Envelope correction: [quantum/effective_theory/apparatus_envelope.md](../effective_theory/apparatus_envelope.md)
- Eibenberger verdict: [quantum/retrodictions/arndt_verdict.md](arndt_verdict.md)
- Fein scaffold: [quantum/retrodictions/fein2019_scaffold.md](fein2019_scaffold.md)
- Visibility→D derivation: [quantum/effective_theory/visibility_to_bandwidth.md](../effective_theory/visibility_to_bandwidth.md)
- ζ derivation: [quantum/effective_theory/zeta_derivation.md](../effective_theory/zeta_derivation.md)
- PDE-parameter mapping: [quantum/effective_theory/pde_parameter_mapping.md](../effective_theory/pde_parameter_mapping.md)
- Q-C Boundary paper: [quantum/papers/Q-C Boundary_Transition. Theory, Prediction, Path.pdf](../papers/Q-C%20Boundary_Transition.%20Theory,%20Prediction,%20Path.pdf)
- Source paper: Fein et al. 2019, "Quantum superposition of molecules beyond 25 kDa," *Nature Physics* **15**, 1242–1245.

---

## 10. One-line summary

> **Fein 2019 record-mass (25 kDa) molecule operates at V_coh ≈ 0.76 — 2.5× the ED-predicted Q-C boundary at V_coh = 0.30. Same verdict class as Eibenberger 2013: consistent with ED, not reaching the predicted boundary, not distinguishing from standard decoherence. A first-order two-point extrapolation of the coherence trajectory across Eibenberger and Fein predicts the Q-C boundary at molecular masses of 140,000–250,000 amu, 5–10× beyond current experimental reach. Distinguishing-signature analysis (N_osc ≈ 9, 3–6% third-harmonic) is the next under-investigated path that does not require next-generation interferometry.**
