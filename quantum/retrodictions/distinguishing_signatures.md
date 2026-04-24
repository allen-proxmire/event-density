# Distinguishing-Signature Analysis — Structural Problems Surfaced

**Date:** 2026-04-24
**Location:** `quantum/retrodictions/distinguishing_signatures.md`
**Status:** **Analysis memo. Two structural problems surfaced that block the distinguishing-signature path as originally framed.** Produces honest diagnosis rather than execution.
**Purpose:** Draft the infrastructure for distinguishing-signature analysis (N_osc ≈ 9, Q ≈ 3.5, triad ≈ 0.03, 3–6% third-harmonic) against existing Arndt-group fringe data. Discover whether this path is executable without requiring Q-C boundary crossing. **Finding: it is not, without further derivation work.**

---

## 1. The ED-predicted distinguishing signatures

From `quantum/papers/Q-C Boundary_Transition. Theory, Prediction, Path.pdf` (Q-C Boundary paper), four distinguishing signatures are predicted:

| Signature | Value | Regime | ED source |
|---|---|---|---|
| Transient oscillation count `N_osc` | 8–19 (~9) | `D < 0.1` | ED-Phys-17 |
| Quality factor `Q` | ≈ 3.5 | `D < 0.1` | 00.3 |
| Triad coupling coefficient | ≈ 0.03 | all regimes | ED-Phys-16 |
| Third-harmonic generation (3rd / fundamental) | 3–6% | `D < 0.1` | ED-Phys |

**Three of the four signatures (N_osc, Q, third-harmonic) are specifically predicted for the `D < 0.1` regime — deep quantum, highly multi-channel.** The triad coefficient is predicted across all regimes.

### 1.1 Why these are distinguishing

- **Standard environmental decoherence** predicts smooth exponential loss of coherence. No transient oscillations, no specific N_osc, no universal Q value, no specific harmonic structure.
- **Dynamical-collapse models** (GRW, CSL, Diósi-Penrose) predict stochastic collapse events with rates scaling smoothly with mass/complexity. No specific N_osc, no specific harmonic, no sharp transition.
- **Classical phase-space models** predict monotonic decoherence with no oscillatory structure at all.

**ED is the only framework** (per the Q-C Boundary paper) that predicts specific oscillation counts, quality factors, and harmonic structure at these values. If observed, any one of these signatures would distinguish ED from all standard alternatives.

---

## 2. Problem 1: the `D < 0.1` regime is unreachable under the committed D(V) formula

### 2.1 The structural issue

From `visibility_to_bandwidth.md §3.1`, the committed D(V) formula is:

```
D(V) = V⁴/2 + (1 − V²)²                              (1)
```

under the three-channel commitment (two paths + env-commit lump).

**Range analysis:**

- At V = 1 (full coherence, balanced paths): D = 1/2
- At V = 0 (full classical commitment): D = 1
- Minimum of D(V): `dD/dV = 2V³ − 4V + 4V³ = 6V³ − 4V = 0` → `V = √(2/3) ≈ 0.816`
- `D_min = D(√(2/3)) = (2/3)²/2 + (1 − 2/3)² = 2/9 + 1/9 = 3/9 = 1/3`

**Therefore D ∈ [1/3, 1] under the three-channel commitment. The range D ∈ [0, 1/3] is not accessible at all.**

### 2.2 Consequence

**`D < 0.1` is unreachable under the three-channel scheme.** This means:

- The `N_osc ≈ 9` signature (D < 0.1 regime) cannot occur in any state our framework describes
- The `Q ≈ 3.5` signature (D < 0.1 regime) cannot occur
- The `3–6% third-harmonic` (D < 0.1 regime) cannot occur

**Only the triad coefficient (≈ 0.03, predicted across all regimes) remains potentially testable under the current commitments.**

### 2.3 Origin of the conflict

The three-channel commitment was adopted in `visibility_to_bandwidth.md §1.1` **specifically because the path × internal-state product-space alternative makes `V_c = 0.30` structurally unreachable (D_max < 1/2 < 0.828 under that scheme).**

Now the opposite problem: the three-channel scheme that makes V_c reachable makes D < 0.1 unreachable. The two regimes (Q-C boundary at D = 0.83, deep-quantum signatures at D < 0.1) require different channel-counting schemes.

**No single committed channel-counting scheme in our current derivation covers both the Q-C-boundary prediction and the deep-quantum distinguishing signatures.**

### 2.4 What this means structurally

The `visibility_to_bandwidth.md` framework is consistent internally (for the Q-C-boundary prediction it was designed to produce) but does not provide a unified map to the PDE-layer distinguishing signatures. Either:

- **(a)** A multi-scale channel-counting framework is needed — two paths for macroscopic fringe visibility, plus internal-state channels for deep-quantum-regime signatures. Different D values in different regimes of the same apparatus.
- **(b)** The Q-C Boundary paper's `D < 0.1` regime is a different `D` variable than the participation-ratio `D` we committed to. The `D` in ED-Phys-16/17 is the PDE coupling weight between the direct channel and the participation channel in the coupled PDE (1) of `D_crit_Resolution_Memo.md §2`. The participation-ratio `D` from visibility-to-bandwidth is a coarse-graining of channel distribution. These may be related but not identical.
- **(c)** The distinguishing signatures `N_osc ≈ 9` etc. refer to phenomena in the PDE dynamics that do not project onto matter-wave interferometry observables at all.

Option (b) is most likely. The `D` in `D_crit(ζ)` governs the underdamping discriminant of the PDE's linearization around equilibrium (`D_crit_Resolution_Memo.md §3–§5`). This is a PDE-intrinsic quantity distinct from the participation-ratio (ED Primitive 08). The Q-C Boundary paper conflates them when it says "D < 0.1 gives N_osc ≈ 9" — or, equivalently, the conflation is the claim that both `D`s are the same quantity.

**A derivation connecting the participation-ratio `D` (Primitive 08) to the PDE-coupling `D` (underdamping discriminant) is missing.** Without it, predictions at one level cannot be directly tested at the other.

---

## 3. Problem 2: the signatures may refer to temporal, not spatial, structure

### 3.1 Nature of the signatures

- **`N_osc ≈ 9`** — "transient oscillation count" — is a time-domain quantity. In the PDE (1b) of `D_crit_Resolution_Memo.md`, `v(x, t)` oscillates with damping; N_osc is how many oscillation periods occur before the transient decays. This is a **temporal** structure in coherence evolution, not a spatial structure in a density pattern.
- **`Q ≈ 3.5`** — "quality factor" — is `ω / (2γ)` for an oscillator. Also temporal.
- **Triad coupling ≈ 0.03** — coupling coefficient in ED-Phys-16 (coupled oscillators). Structural property of the PDE coupling, not of spatial density.
- **3–6% third-harmonic** — "3rd / fundamental" harmonic. **Unclear whether this refers to temporal harmonics of the coherence evolution or spatial harmonics of the fringe pattern.** The Q-C Boundary paper text ("Harmonic generation (3rd / fundamental) 3–6%") is ambiguous; "harmonic generation" in nonlinear-optics terminology usually means temporal frequency doubling/tripling in driven oscillators, not spatial harmonics.

### 3.2 Matter-wave fringe data is spatial, not temporal

Eibenberger 2013 Fig. 3(a) and Fein 2019 Fig. 2(a) show `counts(z)` — counts as a function of transverse displacement `z` of the third grating. This is a **spatial** fringe pattern: a single snapshot of the matter-wave density at the detector plane, averaged over the experiment's run time.

**None of the four ED signatures is directly a property of spatial fringe patterns.** If N_osc, Q, and third-harmonic are temporal, they cannot be extracted from spatial fringe data at all.

### 3.3 What spatial fringe-data could potentially show

Spatial harmonic content in the fringe pattern itself would be a different quantity:

- First harmonic: amplitude at spatial frequency `2π/d` (the grating period)
- Higher spatial harmonics: amplitude at `2·2π/d`, `3·2π/d`, etc.

These spatial harmonics come from the Talbot-Lau apparatus structure — Fourier coefficients of the grating transmission functions, Bessel-function decomposition of the sinusoidal phase grating, etc. **Standard matter-wave interferometry predicts specific spatial-harmonic amplitudes that depend on apparatus parameters, not on ED-specific coherence physics.**

Deviations from the standard-QM-predicted spatial-harmonic structure would be interesting, but:

- **Standard QM predicts specific amplitudes.** Computing the QM prediction for the spatial third-harmonic content at, say, the Eibenberger apparatus operating point is non-trivial — it requires integrating the full Talbot-Lau density pattern including all grating Fourier orders.
- **ED provides no independent prediction for spatial-harmonic amplitudes** in the current derivation chain. The `3–6%` number refers to something else (temporal, per above).
- **An ED prediction for spatial-harmonic content would require a separate derivation** connecting the PDE-layer coherence-field dynamics to the detector-plane density pattern. This derivation does not currently exist.

---

## 4. Signal-to-noise considerations (assuming Problem 2 resolved)

Even if the signatures were shown to be testable against fringe data, practical concerns:

### 4.1 Data quantity

- Eibenberger 2013 Fig. 3(a): approximately 25 data points across 1100 nm (~4 fringe periods)
- Fein 2019 Fig. 2(a): approximately 50 data points across 1000 nm (~4 fringe periods)

With ~25–50 points across 4 periods, harmonic content beyond the second harmonic is at the edge of what's extractable by Fourier analysis.

### 4.2 Data quality

- Error bars in Fein 2019 Fig. 2(b) suggest ±5% noise floor
- Visibility itself is ~25–33%
- **A 3–6% third-harmonic in a ~30% fringe has absolute amplitude of ~1–2% — below the noise floor as shown**

Extracting a 1–2% harmonic from data with 5% noise floor requires either much more data (averaging) or cleaner datasets than the published figures.

### 4.3 Confounding factors

- **Grating-induced harmonics.** The Talbot-Lau pattern itself has higher-order spatial content from the grating Fourier decomposition. Separating apparatus-induced harmonics from coherence-induced harmonics is a nontrivial theoretical modeling task.
- **Velocity averaging.** Finite velocity spread smears the pattern and affects higher harmonics more than the first. This is an apparatus-specific attenuation that must be computed to interpret any measured harmonic content.
- **Detector nonlinearities.** Electron-impact ionization + QMS has response nonlinearities; spatial harmonic content near detector saturation or near noise floor is affected by these.

### 4.4 Net assessment

Even if Problems 1 and 2 were resolved, the 3–6% signature against existing Arndt fringe data is at or below the published noise floor and would require either (a) access to raw (un-averaged) data from the experimenters, (b) a theoretically-clean apparatus-harmonic model to compare against, or (c) both.

---

## 5. What data would actually be required

Per the original memo requirements (§3):

### 5.1 Raw fringe scans

**Required for any spatial-harmonic analysis.** The published figures show binned/averaged data with sinusoidal fits. For harmonic decomposition:

- Full count data `counts(z_i)` at each measurement position with error bars
- Position resolution finer than the grating period
- Multiple scans for noise-averaging
- Apparatus-baseline (no molecules) for systematic correction

**Availability:** not in the published figures. Would require direct contact with the Arndt group or supplementary-data archives.

### 5.2 Residuals from sinusoidal fits

**Partially available.** The published fits show fit quality visually but not numerical residuals. Residual amplitude and structure could be estimated by digitizing the figures — but with only ~25–50 points per scan, the residual-analysis signal-to-noise is weak.

### 5.3 Harmonic decomposition

**Not directly in the papers.** The Arndt group could likely perform this analysis on their raw data if asked; it is not difficult given the underlying scan data.

### 5.4 Time-resolved coherence data

**Not available from matter-wave interferometry fringe patterns at all.** Fringe patterns are time-averaged density profiles. Temporal N_osc and Q signatures require:

- Time-resolved atom/molecule interferometry (Ramsey-type)
- Optomechanical coherence-decay measurements (Aspelmeyer class)
- Cavity-QED Rabi-oscillation data (Haroche class)
- Superconducting-qubit free-evolution data (Devoret-Martinis-Clarke class)

These are different experimental platforms entirely.

---

## 6. Analysis template (preserved for future use if Problems 1–2 are resolved)

### 6.1 Digitization of fringe data

For each published figure (Eibenberger Fig. 3(a), Fein Fig. 2(a)):

- [ ] Read counts(z) values at each data point from the figure
- [ ] Read error bars where shown
- [ ] Record the fit parameters (amplitude, period, phase, offset) from the sinusoidal fit

### 6.2 Harmonic decomposition

Given the digitized data `{(z_i, C_i, σ_i)}`:

- [ ] Fit: `C(z) = C_0 + A_1 cos(2πz/d + φ_1) + A_2 cos(4πz/d + φ_2) + A_3 cos(6πz/d + φ_3) + ...`
- [ ] Extract harmonic amplitudes `A_1, A_2, A_3`
- [ ] Compute ratios `A_2/A_1, A_3/A_1`
- [ ] Estimate uncertainty on each ratio via covariance of the fit

### 6.3 Comparison with standard-QM apparatus prediction

- [ ] Compute the standard Talbot-Lau expected `A_3/A_1` for the apparatus (requires full Talbot-Lau density calculation with apparatus parameters)
- [ ] Compare measured `A_3/A_1` to standard-QM prediction
- [ ] Any deviation is a candidate distinguishing signature

### 6.4 Comparison with ED prediction

**Blocked** until Problems 1–2 are resolved:

- [ ] Derive the ED prediction for spatial `A_3/A_1` at the apparatus operating point (does not currently exist)
- [ ] Compare measured `A_3/A_1` to ED prediction

This block prevents step 6.4 from executing without further theoretical work.

---

## 7. Prioritized plan

### 7.1 Resolve Problem 2 — clarify what "3–6% third-harmonic" means in ED

**First task:** read ED-Phys-16/17 memos in the archive to determine whether the 3–6% prediction is spatial or temporal. This is a literature/archive task within the ED project files; does not require external data.

Locations:
- [archive/research_history/ED Physics/ED-Phys-16_CoupledOscillators/ED-Phys-16_CoupledOscillators.md](../../archive/research_history/ED Physics/ED-Phys-16_CoupledOscillators/ED-Phys-16_CoupledOscillators.md)
- [archive/research_history/ED Physics/ED-Phys-17_OscillatorCosmology/ED-Phys-17_OscillatorCosmology.md](../../archive/research_history/ED Physics/ED-Phys-17_OscillatorCosmology/ED-Phys-17_OscillatorCosmology.md)

If the prediction is temporal: distinguishing-signature testing against fringe data is structurally impossible, and a different experimental platform must be chosen.

If the prediction is spatial: proceed to 7.2.

### 7.2 Resolve Problem 1 — derive the participation-ratio-D to PDE-coupling-D relationship

**Second task:** derive the relationship between participation-ratio `D` (Primitive 08, our `V→D` map) and PDE-coupling `D` (D_crit resolution memo, underdamping discriminant). These may be different variables that happen to share notation, or they may be related by a specific coarse-graining.

**Output memo:** `quantum/effective_theory/d_variable_disambiguation.md`.

If the two are identified, the `D < 0.1` regime corresponds to a specific range of participation-ratio values — computable from the current derivation — and the signatures can be checked there.

If the two are distinct variables, the `D < 0.1` distinguishing signatures are PDE-layer predictions that do not directly constrain participation-ratio-accessible observables. New ED predictions at the participation-ratio level would need to be derived.

### 7.3 If 7.1 and 7.2 resolve favorably — pick a distinguishing-signature platform

If the analyses above show that fringe-data testing is viable in principle, execute the §6 template against Eibenberger and Fein. Signal-to-noise constraints (§4) will likely make the current datasets inconclusive.

If fringe-data testing is structurally blocked but temporal-signature testing is viable, pivot to optomechanical or cavity-QED data.

### 7.4 Triad coupling — the one signature potentially unblocked

The triad coefficient ≈ 0.03 is predicted across all regimes, not just D < 0.1. If this coupling coefficient is a coupling constant in the PDE that manifests at the participation-ratio `D` level (in the accessible range D ∈ [1/3, 1]), it may be testable.

**Task:** read ED-Phys-16 to determine the physical meaning of the "triad coupling coefficient" and whether it projects onto fringe observables. This is the one distinguishing signature that might be tractable under the current derivation.

---

## 8. Honest status

**Where this memo ended up:**

1. **Problem 1:** the `D < 0.1` regime is unreachable under the committed three-channel D(V) formula. The N_osc, Q, and third-harmonic predictions for that regime cannot occur in any state our current framework describes.
2. **Problem 2:** the distinguishing signatures are likely temporal, not spatial. Matter-wave fringe data is spatial. The two don't directly correspond.
3. **Even if both Problems resolve favorably**, the signal-to-noise of the 3–6% third-harmonic signature in existing fringe data is below the published noise floor.

**What this means for the program:**

The distinguishing-signature path, proposed as the next step because it doesn't require reaching the Q-C boundary, has structural issues as serious as the threshold-crossing path. The ED program's existing theoretical chain produces predictions primarily at the PDE-coupling-D and temporal-evolution levels, not at the participation-ratio-D and spatial-fringe levels. Connecting these is additional Phase 2 derivation work.

**Three honest paths forward:**

- **Archive work (7.1, 7.2):** read ED-Phys-16/17 to determine the actual physical content of the distinguishing signatures. May unblock; may further constrain what's testable.
- **Platform pivot:** accept that molecular interferometry is not the right test platform. Pursue optomechanical or cavity-QED data where temporal coherence evolution is directly measured.
- **Framework acknowledgment:** the ED derivation chain as currently written bridges Primitive 04 bandwidth → ζ → D_crit → V_c for matter-wave interferometry Q-C-boundary prediction. It does **not** currently bridge to the Q-C Boundary paper's D < 0.1 distinguishing-signature predictions. These are two different derivation chains that converge only in the PDE layer, and the connection has not been made.

---

## 9. What was learned

1. **Proposing a path without executing it can hide structural issues.** The distinguishing-signature path looked viable at the `arndt_verdict.md §5.4` / `fein2019_verdict.md §8.1` level because it was only described in words. Attempting to draft the executable memo surfaced problems that only appear when one works through the derivation chain.
2. **The ED program has (at least) two `D` variables.** Participation-ratio D (from Primitive 08, our V→D formula) and PDE-coupling D (from D_crit resolution memo). These may or may not be the same variable; the Q-C Boundary paper's predictions implicitly assume they are. Disambiguation is needed.
3. **"D < 0.1" may be unphysical in our framework.** Under the three-channel commitment, D_min = 1/3. Either the three-channel commitment is wrong, or the two D variables are distinct, or both.
4. **Matter-wave interferometry may not be the right test bed** for ED's strongest distinguishing predictions. The predicted signatures look temporal; the available data is spatial. A different experimental class is needed.

---

## 10. Cross-references

- Q-C Boundary paper: [quantum/papers/Q-C Boundary_Transition. Theory, Prediction, Path.pdf](../papers/Q-C%20Boundary_Transition.%20Theory,%20Prediction,%20Path.pdf)
- Eibenberger verdict: [quantum/retrodictions/arndt_verdict.md](arndt_verdict.md)
- Fein verdict: [quantum/retrodictions/fein2019_verdict.md](fein2019_verdict.md)
- Visibility → D derivation: [quantum/effective_theory/visibility_to_bandwidth.md](../effective_theory/visibility_to_bandwidth.md) §3.1 (D(V) formula), §5 (minimum D analysis)
- D_crit resolution memo: [theory/D_crit_Resolution_Memo.md](../../theory/D_crit_Resolution_Memo.md) §2 (PDE form), §5 (underdamping condition)
- PDE mapping: [quantum/effective_theory/pde_parameter_mapping.md](../effective_theory/pde_parameter_mapping.md) §4.1 (D commitment — participation-ratio form)
- ED-Phys archives: `archive/research_history/ED Physics/ED-Phys-16_CoupledOscillators/`, `ED-Phys-17_OscillatorCosmology/`

---

## 11. One-line summary

> **The distinguishing-signature path is structurally blocked under the current derivation. The D < 0.1 regime where N_osc ≈ 9, Q ≈ 3.5, and 3–6% third-harmonic are predicted is unreachable under the committed three-channel D(V) formula (D_min = 1/3); the signatures may be temporal rather than spatial, and therefore not projectable onto matter-wave fringe data at all; and even if both issues resolved, the signal level is below the published noise floor. The first remediation task is archive work — read ED-Phys-16/17 to determine what the signatures actually refer to and whether the two "D" variables in the framework are the same. If they are distinct, separate derivation work is needed to produce matter-wave-testable ED predictions beyond the V_c = 0.30 Q-C boundary.**
