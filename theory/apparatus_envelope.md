# Apparatus-Envelope Correction for KDTLI Visibility

**Date:** 2026-04-24
**Location:** `quantum/effective_theory/apparatus_envelope.md`
**Status:** Derivation memo. Addresses Gap 1 surfaced in `quantum/retrodictions/arndt_verdict.md §4.1`. Produces the envelope-correction formalism needed before any raw-visibility comparison is well-posed; applies to Eibenberger 2013 to produce a corrected comparison; identifies which structural forms are standard matter-wave theory (FORCED) vs. which specific numerical coefficients require direct lookup in Brezger 2003 / Hornberger 2004 (CANDIDATE / PENDING).
**Purpose:** Derive `V_env(apparatus)` such that the ED-predicted `V_c_raw = 0.304` from `visibility_to_bandwidth.md §4.1` can be converted into a physically-comparable visibility `V_c_measurable = V_env × V_c_raw`. Apply to Eibenberger 2013 data. Produce the corrected verdict.

---

## 1. Problem statement

### 1.1 The gap

The derivation in `visibility_to_bandwidth.md` assumed `V_max = 1` at perfect coherence — the coherent limit of a pure two-path interferometer. Real KDTLI interferometers have `V_max_apparatus < 1` even at perfect coherence, because:

- Grating geometry attenuates the first-order fringe amplitude (open-fraction factor).
- The sinusoidal phase grating G2 distributes amplitude across multiple diffraction orders (Bessel-function factor).
- Velocity distribution smears the interference pattern (velocity-average factor).
- Source coherence width is finite (source-broadening factor).
- Detection efficiency is imperfect.

Eibenberger 2013 Fig. 3(b) shows the quantum-prediction peak visibility at `V ≈ 0.38–0.40`, not 1. This ~0.40 ceiling is the apparatus envelope.

### 1.2 The correction

Decompose the measured visibility as a product of two factors:

```
V_measured = V_env(apparatus, P) × V_coh(coherence state)       (1)
```

where:
- `V_env` is the maximum visibility achievable under the apparatus geometry and operating conditions, in the limit of perfect coherence.
- `V_coh ∈ [0, 1]` is the coherence-driven contribution — this is what ED's derivation addresses.

**Status of (1): FORCED.** This decomposition is standard in matter-wave interferometry (see Brezger et al. 2003, Hornberger et al. 2004 reviews); it is the canonical way the community separates geometric limits from coherence effects.

### 1.3 The renormalized prediction

The ED derivation (`visibility_to_bandwidth.md §4.1`) predicts `V_c_raw ≈ 0.304` — but this is a prediction for `V_coh` at the Q-C transition, not for `V_measured`. Under (1):

```
V_c_measurable = V_env × V_c_raw = V_env × 0.304                (2)
```

**This is the quantity that can be compared to experimentally-measured visibility at the Q-C transition.**

---

## 2. Derivation of V_env from standard KDTLI theory

### 2.1 Talbot-Lau visibility structure

For a three-grating Talbot-Lau interferometer with absorptive G1, phase G2, absorptive G3, the first-harmonic visibility at the detector plane is (Brezger, Hackermüller, Uttenthaler, Petschinka, Arndt, Zeilinger, *Phys. Rev. Lett.* **88**, 100404 (2002); Brezger, Arndt, Zeilinger, *J. Opt. B* **5**, S82 (2003)):

```
V_1 = 2 · |A_1^{G1}| · |A_1^{G2}| · |A_1^{G3}| · W_v · W_s      (3)
```

where:
- `A_1^{Gk}` is the first-order Fourier coefficient of grating Gk's transmission function
- `W_v` is the velocity-distribution averaging factor
- `W_s` is the source-coherence factor

**Status of (3): FORCED as structural form.** The specific coefficient of 2 in front and the multiplicative combination follow from the Talbot-Lau self-imaging condition at the Talbot length `L_T = d² / λ_dB`. Specific coefficients should be verified against Brezger 2003 eq. (11) or equivalent.

### 2.2 Grating Fourier coefficients

**G1 and G3 (absorptive slit gratings)** with period `d` and slit width `s`, open fraction `f = s/d`:

```
A_n^{abs}(f) = f · sinc(n · π · f)                               (4)
```

For Eibenberger 2013: `d = 266 nm`, `s ≈ 110 nm` (per user-supplied requirements), so `f ≈ 0.414`. First-order coefficient:

```
|A_1^{abs}(0.414)| = 0.414 · |sinc(0.414 · π)|
                   = 0.414 · |sin(1.301) / 1.301|
                   = 0.414 · |0.964 / 1.301|
                   = 0.414 · 0.741
                   ≈ 0.307                                       (5)
```

**Status of (4): FORCED** (standard grating-optics Fourier decomposition).
**Status of (5) numerical value: CANDIDATE.** The slit width `s ≈ 110 nm` was supplied as user input; the Eibenberger 2013 PDF Fig. 2 caption does not explicitly state it, so the exact value should be verified against the Methods section or Gerlich 2007 apparatus paper.

**G2 (sinusoidal phase grating from standing light wave)** imprints phase `φ(x) = φ₀ · cos²(π x / d) = (φ₀/2)[1 + cos(2π x / d)]` on the matter wave. The Fourier decomposition uses Bessel functions:

```
A_n^{phase}(φ₀) = J_n(φ₀/2)                                     (6)
```

where `φ₀` is the peak phase imprinted per traversal:

```
φ₀(P) = (8 · α_opt · P) / (ℏ · c · ε₀ · v · w_y · √π)           (7a)
```

(Brezger 2003 eq. (4), to within factors; exact form depends on apparatus-specific conventions). A more compact form sometimes written:

```
φ₀ = α_opt · P / (v · ε₀ · c · w_y) · (apparatus factor)         (7b)
```

**Status of (6): FORCED** (standard optics of sinusoidal phase modulation).
**Status of (7): CANDIDATE structural, specific coefficient PENDING** — the exact normalization constant in (7) depends on beam-profile integration conventions; Brezger 2003 eq. (4) is the authoritative source.

The first-order amplitude `|J_1(φ₀/2)|` is maximized at `φ₀/2 ≈ 1.84`, giving `|J_1|_max ≈ 0.582`. Therefore:

```
|A_1^{G2}|_max ≈ 0.582                                          (8)
```

**Status of (8): FORCED** (numerical maximum of the Bessel function J_1).

### 2.3 Velocity-distribution factor W_v

For a Gaussian velocity distribution with mean `v` and spread `Δv`, and Talbot-Lau geometry with inter-grating distance `L`, the velocity-averaged visibility for the first harmonic has the form:

```
W_v = exp(−π² · (Δv / v)² · (L / L_T)²)                         (9)
```

(up to apparatus-specific geometric factors; see Hornberger et al. 2004).

For Eibenberger 2013: `v ≈ 85 m/s` (user input), `Δv ≈ 30 m/s` (user input), so `Δv / v ≈ 0.35`. With `L = L_T` chosen by Talbot condition, `L / L_T = 1`:

```
W_v ≈ exp(−π² · 0.124) = exp(−1.224) ≈ 0.294                    (10)
```

**Status of (9): CANDIDATE.** The structural form is standard; the specific exponent coefficient (π² vs. 2π² vs. other) depends on the Gaussian-averaging convention and Talbot-ordering. Verification against Hornberger 2004 required.
**Status of (10) numerical value: CANDIDATE, pending (9).**

### 2.4 Source-coherence factor W_s

For a molecular beam with finite transverse coherence width `ξ_⊥` compared to the grating period `d`:

```
W_s = exp(−2π² · (d / ξ_⊥)²)  · (other geometric corrections)    (11)
```

For a well-collimated beam in a properly-designed Talbot-Lau interferometer, `ξ_⊥ ≫ d` and `W_s ≈ 1`. Arndt's KDTLI is designed to satisfy this condition.

**Status of (11): CANDIDATE.** Specific form depends on source geometry; typically close to unity for well-designed Talbot-Lau in the Arndt group.

**Working assumption:** `W_s ≈ 1` for Eibenberger 2013 KDTLI at design conditions.

### 2.5 Full envelope formula

Combining (3), (5), (8), (10):

```
V_env_max(P=P_opt) = 2 · |A_1^{G1}| · |A_1^{G2}|_max · |A_1^{G3}| · W_v · W_s
                   = 2 · 0.307 · 0.582 · 0.307 · 0.294 · 1
                   ≈ 0.0322                                       (12)
```

**Wait — this gives 0.03, not 0.40.** The structural form is right; the numerical result is off by a factor of ~12 from the observed V_peak ≈ 0.40 in Fig. 3(b).

### 2.6 Reconciliation with observed V_peak ≈ 0.40

The factor-12 discrepancy means one or more of the factors in (12) is wrong. Most likely candidates:

- **The open fraction `f = s/d ≈ 0.414` from the user-supplied `s ≈ 110 nm` may be wrong.** If in fact the effective open fraction is different (e.g., `f ≈ 0.5` for optimal open slits, giving `A_1^{abs} ≈ 0.318`), the factors change but don't account for 12×.
- **The factor of 2 in (3) may be wrong.** Some conventions put `4` or `π` in front depending on whether `V` is defined via the first harmonic only or includes higher harmonics. Checking Brezger 2003 eq. (11) would resolve.
- **The velocity factor (10) is probably too aggressive.** Arndt-group velocity selection via height delimiters D1/D2 (see Fig. 2 caption: "select a flight parabola") produces a narrower effective Δv/v than the raw beam spread. If the effective `Δv / v ≈ 0.1` after selection, `W_v ≈ exp(−π² · 0.01) ≈ 0.905`, a 3× improvement.
- **The Bessel-function normalization in (6)–(8) may be off by a factor of 2** depending on whether `φ₀` is defined as peak phase or peak-to-peak phase.

**Honest assessment:** the structural formulas (3)–(11) are qualitatively correct, but the specific numerical coefficients are sensitive to convention choices that require direct lookup in Brezger 2003 and Hornberger 2004. My first-pass numerical calculation is off by ~12×, which is a known-to-me issue with these formulas reconstructed from general knowledge rather than from the primary references.

**The robust approach** given the observed V_peak ≈ 0.40 in Fig. 3(b): **take V_env from the data itself**, not from formula-reconstruction. Read:

```
V_env(Eibenberger 2013, L12) ≈ 0.40   (from Fig. 3(b) quantum-prediction peak)
```

This is empirical — the quantum prediction plotted in Fig. 3(b) is the full Talbot-Lau calculation with all envelope factors included, and its peak is 0.40. Using this directly avoids the convention-sensitivity issues above.

**Status: DATA-DRIVEN CANDIDATE.** `V_env ≈ 0.40` is read from the quantum-prediction curve in Fig. 3(b), which is Arndt/Hornberger's own theoretical calculation for their apparatus. It absorbs all the envelope factors without requiring me to reconstruct them from general principles.

---

## 3. Applying the envelope to Eibenberger 2013

### 3.1 Corrected ED prediction

Under the empirical envelope `V_env ≈ 0.40`:

```
V_c_measurable = V_env × V_c_raw = 0.40 × 0.304 ≈ 0.122          (13)
```

**This is the ED-predicted visibility AT THE Q-C TRANSITION for an Eibenberger-apparatus-equivalent experimental configuration.**

### 3.2 Comparison with measured L12 visibility

| Quantity | Value | Interpretation |
|---|---|---|
| `V_measured(L12, P=1W)` | `0.33 ± 0.02` | Fig. 3(a) data |
| `V_env(Eibenberger apparatus)` | `≈ 0.40` | Fig. 3(b) quantum-prediction peak |
| `V_coh(L12, P=1W)` = `V_measured / V_env` | `≈ 0.825` | Coherence fraction |
| `V_c_raw` (ED prediction) | `0.304` | Q-C boundary in coherence-fraction terms |
| `V_c_measurable` | `≈ 0.122` | Q-C boundary in raw-visibility terms |

### 3.3 Verdict on L12

**`V_coh(L12) ≈ 0.825` vs. `V_c_raw = 0.304`.**

L12 is operating at 83% coherence fraction, **well above the ED-predicted Q-C boundary at 30%**. The ratio `V_coh / V_c_raw = 2.7` means L12 is operating at 2.7× the Q-C-boundary coherence level.

**Equivalent reading in raw-visibility terms:**

`V_measured(L12) = 0.33` vs. `V_c_measurable ≈ 0.122`.

The measured visibility is **2.7× the ED-predicted Q-C-boundary value** for this apparatus. L12 is firmly in the quantum regime, not at or near the boundary.

**This is exactly what we would expect physically: interference was observable with good contrast for L12, meaning the molecule is clearly in the quantum regime. ED's prediction is consistent with this: the Q-C boundary should be at lower visibility (V_measured ≈ 0.122) corresponding to more-decohered or larger-mass conditions not reached in Eibenberger 2013.**

---

## 4. Verdict: ED is consistent with but not yet tested by Eibenberger 2013

### 4.1 What this correction achieves

1. The raw numerical coincidence from `arndt_verdict.md §2.2` (`V_measured = 0.33` vs. `V_c_raw = 0.304`) is now correctly diagnosed as apparatus-envelope artifact. **These numbers are not in a direct comparison relationship.**
2. The corrected comparison (`V_measured = 0.33` vs. `V_c_measurable = 0.122`) shows L12 is well inside the quantum regime at 2.7× the Q-C-boundary visibility.
3. The ED framework is *consistent* with the observation that interference survives at 10,000 amu: the apparatus has not reached the Q-C boundary for this molecule.

### 4.2 What this correction does NOT achieve

1. **Still not a retrodiction.** ED predicts the Q-C boundary is at `V_measurable ≈ 0.12`. Eibenberger 2013 does not reach this level. No Q-C crossing is observed in the dataset.
2. **Does not distinguish ED from competitors.** Standard decoherence theory *also* predicts that L12 at 10,000 amu should be quantum-behaving at Eibenberger's operating conditions; both frameworks are consistent.
3. **Does not validate any of the three CANDIDATE commitments** from `visibility_to_bandwidth.md §1`. Those remain open.

### 4.3 Verdict

**CONSISTENT (weak-form) via envelope correction.** No refutation, no distinguishing confirmation. Same verdict as before but now with a properly-framed comparison.

---

## 5. Status classification summary

| Derivation step | Status |
|---|---|
| Decomposition `V_measured = V_env × V_coh` (eq. 1) | **FORCED** (standard matter-wave interferometry) |
| Renormalized ED prediction `V_c_measurable = V_env × 0.304` (eq. 2) | **FORCED given (1)** |
| Talbot-Lau visibility structure (eq. 3) | **FORCED structural**; specific prefactor CANDIDATE |
| Absorptive-grating Fourier coefficient (eq. 4) | **FORCED** |
| Sinusoidal phase grating Bessel coefficient (eq. 6) | **FORCED** |
| Phase-depth formula (eq. 7) | **CANDIDATE** structural; specific constants PENDING Brezger 2003 |
| Velocity factor (eq. 9) | **CANDIDATE** structural; specific exponent PENDING Hornberger 2004 |
| Source factor (eq. 11) | **CANDIDATE**; assumed ≈1 |
| First-pass numerical `V_env` from formulas (eq. 12) | **FAILED** by ~12× — needs primary-reference lookup |
| Empirical `V_env ≈ 0.40` from Fig. 3(b) quantum-prediction peak | **DATA-DRIVEN CANDIDATE** |
| Corrected prediction `V_c_measurable ≈ 0.122` (eq. 13) | **CANDIDATE** (inherits from empirical V_env) |
| Comparison: L12 at 2.7× Q-C-boundary | **FORCED** given numerical inputs |

---

## 6. What remains to execute a full verdict

### 6.1 Primary-reference cleanup

Retrieve and work through:

- **Brezger, Arndt, Zeilinger (2003)**, *J. Opt. B* **5**, S82 — exact KDTLI visibility formula with all convention conventions.
- **Hornberger, Sipe, Arndt (2004)**, *Phys. Rev. A* **70**, 053608 — velocity-averaging and decoherence-corrected contrast.
- **Gerlich et al. (2007)**, *Nature Physics* **3**, 711 — KDTLI-specific apparatus parameters.

After this, the formula-reconstruction in §2.2–§2.4 can be checked against primary sources and the factor-12 discrepancy resolved. **If** the primary-source formula gives `V_env ≈ 0.40` consistent with the empirical reading, that is a positive cross-check. **If not**, the empirical reading is taken as authoritative because it comes from Arndt's own apparatus model (Fig. 3(b) blue curve).

### 6.2 Mass-sweep dataset

The envelope correction makes the ED prediction comparable to any KDTLI-class measurement. But to actually test the Q-C boundary, a dataset in which visibility crosses through the envelope-corrected Q-C value (`V ≈ 0.122` for Eibenberger-apparatus, or the equivalent for other apparatus) is needed.

**Candidates:**
- **Fein, Geyer, Zwick, Kiałka, Pedalino, Mayor, Gerlich, Arndt (2019)**, *Nature Physics* **15**, 1242 — functionalized oligoporphyrins up to ~25,000 amu. If visibility vs. mass is reported in sufficient detail, the envelope-corrected comparison is executable.
- Gerlich et al. 2011 earlier work with smaller molecules — probably all well inside quantum regime but offers more data points for the envelope-vs-coherence separation check.
- Haslinger et al. 2013 OTIMA interferometer — different apparatus class; requires its own envelope derivation (§7 below).

### 6.3 Promote the three CANDIDATE commitments

Still open:
- Exponent = 2 in bandwidth composition rule
- `b_coh = V² · b_total` survival fraction form
- Three-channel KDTLI scheme with env-commit lump

Any of these promoted to FORCED tightens the `V_c_raw ≈ 0.304` prediction and reduces disclosure cost of future retrodiction claims.

---

## 7. Generalization to Fein 2019 and Haslinger 2013

### 7.1 Fein 2019 (high-mass KDTLI, same apparatus class)

Same envelope structure applies; specific numerical `V_env` value differs because:
- Different mass range → different de Broglie wavelengths → different Talbot conditions
- Possibly different laser power, velocity distribution

Protocol:
1. Read the quantum-prediction curve peak from Fein 2019's equivalent of Fig. 3(b) to get `V_env` for that apparatus configuration.
2. Apply `V_c_measurable = V_env × 0.304` to get the envelope-corrected ED prediction for Fein's conditions.
3. Check whether Fein's measured visibility at the highest masses crosses below `V_c_measurable`. If yes, that's the Q-C-crossing retrodiction test.

### 7.2 Haslinger 2013 (OTIMA, different apparatus class)

OTIMA (Optical Time-Domain Ionizing Matter-wave) interferometer uses three pulsed UV ionization gratings rather than absorptive + phase + absorptive. The envelope structure differs:

- No absorptive grating Fourier coefficients (gratings are time-domain ionizing)
- Pulsed-grating geometry changes the Talbot condition structure
- Ionization cross-section replaces absorption

**A separate envelope derivation is required for OTIMA.** The ED prediction `V_c_raw = 0.304` (in coherence-fraction terms) is apparatus-independent, but `V_c_measurable` is apparatus-specific.

**Target memo:** `quantum/effective_theory/otima_envelope.md` — not drafted here; Phase 2 work.

### 7.3 Non-Arndt platforms

Cavity QED (Haroche class), superconducting qubits (Devoret-Martinis-Clarke), optomechanics (Aspelmeyer) each have their own envelope structures. Each would require a dedicated derivation, but all share the decomposition `V_measured = V_env × V_coh`, so the ED `V_c_raw = 0.304` prediction generalizes once the apparatus-specific envelope is computed.

---

## 8. Summary

**Achieved:**

- Envelope-correction formalism laid out for KDTLI.
- Structural decomposition `V_measured = V_env × V_coh` committed (FORCED).
- First-pass formula-reconstruction gives factor-12 wrong answer; diagnosed as primary-reference-dependency issue, not framework issue.
- Empirical `V_env ≈ 0.40` read from Eibenberger 2013 Fig. 3(b).
- Corrected ED prediction: `V_c_measurable ≈ 0.122` for Eibenberger apparatus.
- Corrected verdict on L12: operating at 83% coherence fraction, 2.7× the ED-predicted Q-C boundary. **Consistent, not refuted, not confirmed.**

**Not achieved:**

- A definitive retrodiction test (requires mass-sweep data reaching below V = 0.12).
- Primary-reference verification of the envelope formula.
- Distinguishing test vs. standard decoherence theory.

**Honest framing:**

The envelope correction does what it was supposed to do: it converts the ED prediction into a form that can be compared to real KDTLI measurements, and it shows that the earlier coincidental agreement (`V_measured = 0.33` vs. `V_c_raw = 0.304`) was a confounding of geometry with coherence. With the correction applied, L12 is shown to be well inside the quantum regime — consistent with the Arndt group's own interpretation of their data, consistent with ED, and not a Q-C boundary crossing.

**A real test of the ED prediction requires data from a regime where `V_measured` drops below ~0.12 under KDTLI-class conditions.** Fein 2019 is the closest available candidate. Obtaining that data, applying the same envelope correction, and checking whether the crossing occurs at the mass predicted by the full ED derivation chain is the next executable step.

---

## 9. Cross-references

- Arndt verdict (pre-envelope): [quantum/retrodictions/arndt_verdict.md](../retrodictions/arndt_verdict.md)
- Visibility → D derivation: [quantum/effective_theory/visibility_to_bandwidth.md](visibility_to_bandwidth.md)
- ζ derivation: [quantum/effective_theory/zeta_derivation.md](zeta_derivation.md)
- PDE-parameter mapping: [quantum/effective_theory/pde_parameter_mapping.md](pde_parameter_mapping.md)
- Arndt Step 2 attempt: [quantum/retrodictions/arndt_step_2.md](../retrodictions/arndt_step_2.md)
- Arndt scaffold: [quantum/retrodictions/arndt_interferometry.md](../retrodictions/arndt_interferometry.md)
- D_crit formula: [theory/D_crit_Resolution_Memo.md](../../theory/D_crit_Resolution_Memo.md)
- Source paper: Eibenberger et al. 2013, arXiv:1310.8343v1 — Figs. 2 and 3 inspected directly.
- Primary references pending retrieval: Brezger Arndt Zeilinger 2003; Hornberger Sipe Arndt 2004; Gerlich et al. 2007.

---

## 10. One-line summary

> **Decomposing measured visibility as `V_measured = V_env × V_coh` makes ED's coherence-fraction prediction `V_c_raw ≈ 0.304` comparable to real experiments. Using the empirical `V_env ≈ 0.40` from Eibenberger 2013 Fig. 3(b), the ED-predicted Q-C-boundary measured visibility is `V_c_measurable ≈ 0.122` for the Eibenberger apparatus. L12's measured `V = 0.33` sits at 2.7× this value — firmly in the quantum regime, consistent with the data, not a Q-C crossing. A real retrodiction test requires a dataset (Fein 2019 is the natural candidate) that reaches below V ≈ 0.12 in KDTLI-class conditions.**
