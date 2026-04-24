# Arndt Retrodiction — Verdict Memo

**Date:** 2026-04-24
**Location:** `quantum/retrodictions/arndt_verdict.md`
**Source data:** Eibenberger, Gerlich, Arndt, Mayor, Tüxen (2013), arXiv:1310.8343v1 [*PCCP* **15**, 14696–14700]. Figures 2 and 3 inspected directly.
**Status:** **Verdict: INCONCLUSIVE. The data does not match the structure the retrodiction was framed to test. Two methodological gaps were surfaced, neither fatal, both specific.**
**Purpose:** Report honest findings from direct inspection of Eibenberger 2013 data against the predictions of `visibility_to_bandwidth.md §4.1` (`V_c ≈ 0.304` at Q-C transition).

---

## 1. Data actually extracted from Eibenberger 2013

### 1.1 Apparatus (Fig. 2)

| Quantity | Value | Source in paper |
|---|---|---|
| Grating period | `d = 266 nm` | Fig. 2 caption |
| Grating type G1, G3 | SiN_x | Fig. 2 caption |
| Grating type G2 | optical phase grating (standing light wave) | Fig. 2 caption |
| Laser beam waist x | `w_x ≅ 18 μm` | Fig. 2 caption |
| Laser beam waist y | `w_y ≅ 945 μm` | Fig. 2 caption |
| Detection | electron ionization + quadrupole mass spectrometry | Fig. 2 caption |
| Mass-spectrum range displayed | approximately 7000–14000 amu | Fig. 2 inset |

### 1.2 Interference data for molecule L12 (Fig. 3)

| Quantity | Value | Source |
|---|---|---|
| Molecule | L12 (specific library member) | Fig. 3 text |
| Laser power for primary data point | `P ≅ 1 W` | Fig. 3(a) |
| **Measured quantum fringe visibility** | **`V = 33 ± 2%`** | Fig. 3(a) text, sinusoidal fit |
| Classical-model prediction at same `P` | `V = 8%` | Fig. 3(a) text |
| Visibility-vs-P measured range | approximately `P ∈ [0.5, 1.7] W` | Fig. 3(b) data points |
| Visibility peak in quantum prediction | `V_peak ≈ 38–40%` at `P ≈ 1 W` | Fig. 3(b) blue curve |
| Visibility peak in classical prediction | `V ≈ 8%` at `P ≈ 0.3 W` | Fig. 3(b) red curve |

### 1.3 What the paper does NOT report (from these two figures)

- Specific mass value of L12 (inferable to be in the 10,000 amu region from Fig. 2 inset arrow, but not quoted in these figures)
- Visibility-vs-mass data for different library members
- Molecular velocity, temperature, pressure (apparatus parameters needed for Λ)
- Any measured or computed decoherence rate Λ
- Any transition mass `m_c`
- Any claim of a Q-C transition being crossed

### 1.4 Honest note on extraction limits

I have inspected Fig. 2 and Fig. 3 only. The paper may contain a Fig. 1 with different data (mass spectrum details, velocity distributions) and methodological text with apparatus parameters not visible in these two figures. The extraction above is from what was made available in the session.

---

## 2. Comparison with ED prediction — as originally framed

### 2.1 The prediction

From `quantum/effective_theory/visibility_to_bandwidth.md §4.1`:

> **`V_c ≈ 0.304` at the Arndt Q-C transition** (under three CANDIDATE commitments: three-channel KDTLI scheme, sublinear exp=2 composition, squared-amplitude coherence survival).

### 2.2 The raw comparison

`V_measured(L12, P=1W) = 0.33 ± 0.02` vs. `V_c_predicted = 0.304`.

Numerical agreement: the measured value is **within 0.026 of the prediction** — well within the experimental error bar (which alone is ±0.02) and close to the theoretical uncertainty of the CANDIDATE commitments.

**If taken at face value, this would be a tight retrodiction match.**

### 2.3 Why "face value" is wrong

Two structural problems that direct inspection of the data reveals:

**Problem 1 — Eibenberger 2013 does not measure a Q-C transition.** The paper demonstrates *sustained* quantum interference at a record-high mass (~10,000 amu region). The visibility values are reported for a single molecule (L12) as a function of laser power `P`, not as a function of a Q-C-transition control parameter. The molecule is operating *within* the quantum regime throughout the dataset; there is no observed crossing.

The V(P) curve in Fig. 3(b) is driven by grating-diffraction physics (the phase imprinted by G2 depends on laser power), not by decoherence crossing a threshold. Both the quantum and classical predictions show V as a bell-shaped function of P, peaking at different P values. The data matches the quantum prediction, definitively ruling out the classical prediction — but that is *not* the kind of measurement the retrodiction was framed to test.

**The retrodiction protocol assumed a V-vs-mass sweep with visibility dropping through V_c as mass increases. Eibenberger 2013 does not contain such a sweep.** It contains visibility-at-single-mass-as-function-of-diffraction-conditions. My methodological concern in `arndt_data_extraction.md §2` was correct and is now confirmed by direct inspection.

**Problem 2 — apparatus-specific visibility envelope.** Even at optimal `P` and in the pure quantum-prediction case, `V_peak ≈ 0.40`, not `V = 1`. The apparatus-specific envelope (grating geometry, Talbot pattern visibility limit, ionization/detection efficiency considerations) caps the theoretical maximum visibility at ~0.40 regardless of coherence state.

The ED derivation in `visibility_to_bandwidth.md` assumed `V_max = 1` at perfect coherence. A comparison between `V_measured = 0.33` and `V_c = 0.30` without accounting for this envelope confuses *coherence-limited* with *apparatus-limited* visibility degradation.

**Normalized comparison:** `V_normalized = V / V_apparatus_max`.
- At `P = 1 W`, `V_apparatus_max ≈ 0.40` (read from the quantum-prediction curve peak).
- `V_normalized_measured = 0.33 / 0.40 ≈ 0.825`.
- `V_c_normalized_predicted` = 0.30 / V_apparatus_max_at_Q-C_conditions, which we do not know.

Under the normalization, `V_normalized ≈ 0.83` suggests L12 is operating *well inside* the coherent regime, with coherence retention ~83%. This is inconsistent with the naive "measured = 0.33 ≈ predicted = 0.30" reading.

**The numerical closeness of raw `V_measured ≈ V_c_predicted` is a coincidence of apparatus envelope plus diffraction geometry, not evidence of Q-C boundary crossing.**

---

## 3. Verdict

**INCONCLUSIVE.**

Not **consistent** in the strong sense, because the raw numerical agreement evaporates once the apparatus envelope is accounted for.

Not **refuted**, because Eibenberger 2013 does not provide the kind of measurement that the retrodiction was designed to test.

Not **tested**, because the dataset structure is mismatched to the prediction structure.

This is the honest read. A weaker claim — "the ED framework is consistent with the observation that interference survives at 10,000 amu" — is true but shallow; any framework that doesn't predict collapse below 10,000 amu is consistent with the same observation.

---

## 4. Methodological gaps surfaced by direct data inspection

### 4.1 Apparatus-envelope correction (new gap)

The `V_max = 1` assumption in `visibility_to_bandwidth.md §2` does not match real matter-wave interferometers, where grating geometry produces `V_max_apparatus ≈ 0.4` even at perfect coherence. The ED derivation needs an envelope-correction step:

- Define `V_apparatus_envelope(P, apparatus)` = maximum possible visibility under grating / detection geometry at apparatus settings
- Define `V_coherence_fraction = V_measured / V_apparatus_envelope` = the coherence-driven contribution
- ED's `V_c = 0.304` prediction should be compared to `V_coherence_fraction`, not raw `V_measured`

This is a straightforward correction in principle but requires the apparatus-envelope function. For KDTLI this is computable from standard matter-wave interferometry theory.

**Status of the gap:** NEW. Not previously flagged. Surfaces only when real data is confronted.

### 4.2 Control-parameter identification (refinement)

Eibenberger 2013's control parameter is laser power `P`, not mass. Mass is fixed for a given molecule; the Q-C-relevant sweep would be across the molecular library (L1, L2, …, L12, …) with their different masses. This data is not in Figs. 2 and 3 of arXiv 1310.8343v1.

For a mass-sweep retrodiction, the relevant Arndt-group datasets may be:

- **Fein et al. 2019** (*Nature Physics* 15, 1242) — reports interference up to 25,000 amu. If visibility is reported at multiple masses, this is the cleanest mass-sweep.
- **Gerlich et al. 2011** and earlier KDTLI papers — smaller mass range but more mass values.
- **Haslinger et al. 2013** (OTIMA interferometer) — different apparatus class, different derivation needed.

**Status of the gap:** confirms the methodological concern in `arndt_data_extraction.md §2`. The specific Eibenberger 2013 dataset is not sufficient; a mass-sweep dataset is needed.

---

## 5. What was learned

### 5.1 The ED derivation chain produces a falsifiable number

From primitives 04 + 11 through ζ derivation through `D_crit(ζ)` through `D(V)`, the prediction `V_c ≈ 0.304` is a real quantitative target. The derivation chain is internally consistent and produces a specific number (not a range, not a qualitative claim).

This is real progress. Regardless of whether this specific number agrees or disagrees with data, the program now has a concrete prediction that can be checked against any suitable KDTLI-class dataset.

### 5.2 The prediction is not testable against arbitrary Arndt data

Specifically, visibility-vs-mass sweeps are required. Visibility-vs-laser-power (as in Eibenberger 2013 Fig. 3) is a different kind of measurement that the ED derivation was not framed to address.

### 5.3 Apparatus-envelope effects are non-trivial

The `V_max = 1` idealization breaks contact with real interferometers at the ~2× level (`V_max ≈ 0.4` rather than 1). Future retrodiction work must include envelope correction to avoid coincidental-agreement claims.

### 5.4 The raw numerical coincidence is real but not load-bearing

`V_measured(L12) = 0.33 ± 0.02` vs. `V_c_predicted = 0.304` is numerically close. If I had not inspected the actual data and had read only the number, I could have claimed a retrodiction match. Direct inspection revealed that the apparent match is apparatus-driven, not coherence-driven, and therefore does not constitute evidence for the ED prediction.

**This is why actually looking at the data matters.** A textual summary saying "Arndt measured V = 33% at record mass" would have supported a false retrodiction claim.

---

## 6. Path forward

### 6.1 Near-term — apparatus-envelope derivation

Produce `quantum/effective_theory/apparatus_envelope.md`:

- Derive the KDTLI-apparatus visibility envelope `V_env(P, d, w_x, w_y, L_T, v, …)` from standard matter-wave interferometry theory (see Brezger 2003, Hornberger 2004 reviews).
- Express the ED prediction as the *coherence fraction* rather than the raw V: `V_c_coherence = 0.304 × V_env(conditions)`.
- This gives `V_c_predicted` as a function of apparatus conditions that can be compared to `V_measured` directly.

### 6.2 Near-term — mass-sweep dataset

Obtain Fein et al. 2019 or equivalent mass-sweep data. Re-execute the retrodiction protocol against a dataset that actually measures visibility at multiple masses.

### 6.3 Medium-term — promote CANDIDATE commitments to FORCED

The three CANDIDATE commitments in `visibility_to_bandwidth.md §1` (channel-counting, exp=2 composition, `b_coh = V²`) remain open. Promoting any of them to FORCED tightens the prediction and reduces the disclosure cost of a retrodiction claim.

### 6.4 Long-term — check distinguishing signatures

`N_osc ≈ 9`, 3–6% third-harmonic, and sharp vs. smooth transition are ED-specific predictions. None is testable against Eibenberger 2013 Fig. 3 at the granularity available. These require either higher-precision data in the low-D regime or cross-platform checks against other Arndt-class or non-Arndt experiments.

---

## 7. Honest framing for the record

**What this session achieved:**

1. Complete derivation chain from ED primitives to a quantitative retrodiction prediction (`V_c ≈ 0.304`).
2. First direct test against published Arndt data.
3. Discovery of two methodological gaps (apparatus envelope, mass-sweep requirement) that the derivation chain did not anticipate.
4. Honest verdict: **inconclusive, not yet tested**.

**What this session did not achieve:**

1. A retrodiction that cleanly matches published data without disclosure cost.
2. A refutation of ED.
3. Execution against a mass-sweep dataset.
4. Envelope-corrected comparison.

**What the reader should take from this:** the ED program now has a concrete, quantitative, falsifiable prediction framework in place for matter-wave interferometry retrodictions. The first attempt at a retrodiction verdict surfaced two specific, addressable methodological gaps. Neither is fatal. Both are tractable in near-term Phase 2 work. The program is in a substantially better position than it was before this session — not because a retrodiction landed, but because the full derivation chain was built, executed, and honestly stress-tested against real data.

**If someone had claimed "V = 0.33 measured, V_c = 0.30 predicted, retrodiction confirmed" without inspecting the envelope structure, that would have been exactly the drift we've been steering away from this entire session.** The verdict here — INCONCLUSIVE — is the honest one.

---

## 8. Cross-references

- Data extraction template: [quantum/retrodictions/arndt_data_extraction.md](arndt_data_extraction.md)
- Visibility→D derivation: [quantum/effective_theory/visibility_to_bandwidth.md](../effective_theory/visibility_to_bandwidth.md)
- ζ derivation: [quantum/effective_theory/zeta_derivation.md](../effective_theory/zeta_derivation.md)
- PDE-parameter mapping: [quantum/effective_theory/pde_parameter_mapping.md](../effective_theory/pde_parameter_mapping.md)
- Arndt Step 2 attempt: [quantum/retrodictions/arndt_step_2.md](arndt_step_2.md)
- Arndt scaffold: [quantum/retrodictions/arndt_interferometry.md](arndt_interferometry.md)
- Source paper (inspected): Eibenberger et al. 2013, arXiv:1310.8343v1, Figures 2 and 3

---

## 9. One-line summary

> **Direct inspection of Eibenberger 2013 Figures 2 and 3 reveals that the paper measures visibility at a fixed molecular species as a function of laser power, not visibility as a function of mass across a Q-C-transition sweep. The raw numerical agreement `V_measured(L12) = 0.33 ± 0.02` vs. `V_c_predicted = 0.304` would be a tight retrodiction if taken at face value — but the apparatus-envelope effect (`V_max_apparatus ≈ 0.40`, not 1) means the comparison is not well-posed without envelope correction. Verdict: inconclusive, not refuted, not tested. Two new methodological gaps surfaced: apparatus-envelope correction (required before any raw-V comparison is valid) and mass-sweep dataset acquisition (required for the originally-framed Q-C transition retrodiction). Both are addressable in near-term Phase 2 work.**
