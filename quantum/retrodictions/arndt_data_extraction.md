# Arndt Data Extraction — Eibenberger et al. 2013

**Date:** 2026-04-24
**Location:** `quantum/retrodictions/arndt_data_extraction.md`
**Status:** **Data not retrieved. Memo produces a template; no numbers are fabricated.** The Eibenberger et al. 2013 *PCCP* paper is not in this working session; I do not have its figures or data tables in hand. This memo lays out the extraction template, flags what is known from general recall (with explicit uncertainty), raises a methodological concern about whether a "Q-C transition" is actually reported in the paper at all, and specifies the checklist for completing the extraction once the PDF is retrieved.
**Purpose:** Produce the scaffolded data-extraction document that `arndt_step_2.md §7.2` called for; avoid fabricating visibility-vs-mass data.

---

## 1. Source paper

**Citation (from general recall, verify against the actual PDF):**

Eibenberger, S.; Gerlich, S.; Arndt, M.; Mayor, M.; Tüxen, J. (2013). "Matter-wave interference of particles selected from a molecular library with masses exceeding 10,000 amu." *Physical Chemistry Chemical Physics* **15**, 14696–14700. DOI: 10.1039/C3CP51500A (approximate; verify).

**What the paper is known to demonstrate (from general recall, uncertainty flagged):**

- First matter-wave interference demonstration for particles > 10,000 amu
- Uses Kapitza-Dirac-Talbot-Lau (KDTLI) interferometer
- Molecular library: functionalized tetraphenylporphyrin derivatives (large organic molecules with attached side-groups for mass tuning)
- Reports fringe visibility for multiple mass classes within the library

**Not reliably recalled (must come from the PDF):**

- Specific mass values of the molecules studied
- Specific visibility values at each mass
- Apparatus parameters (velocity, temperature, pressure, grating period)
- Whether the paper reports a transition point or only demonstrates sustained interference

---

## 2. Methodological concern (raised before extraction)

Arndt-group matter-wave interferometry papers typically demonstrate **that interference survives at a given mass**, not **that a transition occurs at a measured mass** `m_c`. The strategic point of Arndt's research program has historically been to push the upper boundary of mass at which quantum interference is observable, demonstrating survival rather than failure.

**If Eibenberger 2013 reports visibility values at several masses, all of which remain well above zero,** then there is no directly-measured `m_c` at which `V = 0.3` occurs. The ED prediction `V_c ≈ 0.30` (from `visibility_to_bandwidth.md §4.1`) would then have to be compared to either:

- **(a) Extrapolation of the visibility-vs-mass curve to larger masses** — assumes the trend continues, which may or may not be valid. Introduces fitting-function choice as an additional free parameter.
- **(b) Combination with later Arndt-group datasets** — e.g., Fein et al. 2019 (interference at masses ~25,000 amu), where if visibility has dropped substantially at the larger masses, the 0.30 crossing may be observable.
- **(c) Reinterpretation of the ED prediction as a "surviving-visibility lower bound"** — the prediction becomes "visibility should remain above the transition threshold for all masses studied," which is a weaker consistency check rather than a retrodiction of `m_c`.

**Each of these has disclosure costs.** This memo does not resolve which framing is correct; it flags that the strategic premise of "Arndt measures a Q-C transition at `m_c`" may not match the structure of the actual published data.

**Action item:** once the PDF is retrieved, determine:
- Does the paper report visibility dropping below some threshold at the highest mass studied?
- If yes, can `m_c` at `V = 0.30` be read off directly or interpolated?
- If no, which of (a)–(c) is appropriate for the retrodiction framing?

---

## 3. Extraction template

### 3.1 Visibility-vs-mass data

To be populated from Eibenberger 2013 Figures (likely Fig. 2, Fig. 3, or a data table):

| Molecule label | Molecular mass `m` (amu) | Visibility `V` | Error bar on `V` | Notes |
|---|---|---|---|---|
| — | **PENDING PDF** | **PENDING PDF** | **PENDING PDF** | |
| — | **PENDING PDF** | **PENDING PDF** | **PENDING PDF** | |
| — | **PENDING PDF** | **PENDING PDF** | **PENDING PDF** | |
| — | **PENDING PDF** | **PENDING PDF** | **PENDING PDF** | |

**Do not populate this table from memory.** Every row must trace to a specific figure or table in the PDF. Rows that cannot be traced must be flagged `CANNOT EXTRACT`.

### 3.2 Apparatus parameters

Required for Λ computation via Hornberger-Joos-Zeh formulas (Hornberger et al. 2012, *Rev. Mod. Phys.* **84**, 157):

| Parameter | Symbol | Eibenberger 2013 value | Source |
|---|---|---|---|
| Mean molecular velocity | `v` | **PENDING PDF** | Methods section |
| Velocity spread | `Δv/v` | **PENDING PDF** | Methods section |
| Residual gas pressure | `p` | **PENDING PDF** | Methods section |
| Background temperature | `T_env` | **PENDING PDF** | Methods section |
| Grating period | `d_g` | **PENDING PDF** | Methods or Gerlich 2007 |
| Grating-to-grating distance | `L` | **PENDING PDF** | Methods or Gerlich 2007 |
| Talbot length | `L_T = d_g²·m·v / h` | **COMPUTABLE** from above | Derived |
| Internal molecular temperature | `T_int` | **PENDING PDF** | Methods section |

### 3.3 Internal relaxation timescale τ_internal

Required for `ζ_Arndt = Λ · τ_internal` computation.

| Source | Candidate value | Status |
|---|---|---|
| Vibrational period of dominant low-frequency mode of oligoporphyrin derivative | **PENDING LITERATURE** | Published in vibrational-spectroscopy papers for related porphyrins |
| Electronic relaxation timescale | **PENDING LITERATURE** | — |

**Note:** `τ_internal` is not typically reported in Arndt-group interferometry papers. It must be sourced from vibrational or electronic spectroscopy literature on tetraphenylporphyrin derivatives. A first-pass estimate: `τ_internal ~ 10⁻¹² s` (picosecond-scale vibrational relaxation), order-of-magnitude. This is not derivation-grade data; flag as approximate.

### 3.4 Hornberger Λ

Computed from apparatus parameters (§3.2) via Hornberger 2012 formulas. Required inputs:
- Molecular mass
- Geometric cross-section (function of molecular size)
- Background temperature and pressure
- Internal-state structure

| Mass | Λ_thermal-photons (s⁻¹) | Λ_gas-collisions (s⁻¹) | Λ_total (s⁻¹) | ζ = Λτ |
|---|---|---|---|---|
| — | **PENDING COMPUTATION** | — | — | — |

This table is populated by arithmetic from §3.2 + §3.3 data, using Hornberger's formulas. Arithmetic is mechanical; **the input data must come from the PDF**.

---

## 4. Finding `m_c` at `V = 0.30`

Once §3.1 is populated:

**Protocol:**

1. Plot `V` vs. `m` from the extracted table.
2. Fit a smooth curve (exponential decay, or Gaussian, or whatever structure the data suggests).
3. Determine the mass `m_c` at which the fit crosses `V = 0.30`.
4. Propagate error bars from the individual data points to an uncertainty on `m_c`.

**If no data point in the published range falls below `V = 0.30`**: report `m_c` as lower-bound extrapolation, with explicit disclosure that the prediction is being compared to an extrapolation rather than a measurement. This is the (a) framing from §2.

**If data points span the `V = 0.30` crossing**: interpolate directly. This is the cleanest case.

**If only sparse data** (e.g., visibility reported at 3–4 mass values, none near 0.30): flag as inconclusive; the prediction cannot be tested against this dataset alone.

---

## 5. Assembly for the comparison memo

Once §3.1, §3.2, §3.3, §3.4 are populated:

**Predicted side (already in hand from `visibility_to_bandwidth.md` and `zeta_derivation.md`):**

- `ζ_Arndt = Λ_total · τ_internal` — computed from §3.4
- `D_crit(ζ_Arndt) ≈ 0.828` — computed via `D_crit(ζ) = √(2−ζ)(2−√(2−ζ))` formula
- `V_c ≈ 0.304` — derived from `D(V) = V⁴/2 + (1−V²)² = 0.828`

**Measured side (populated from this memo once complete):**

- `m_c` = mass at which `V(m_c) = 0.304` from the Arndt data
- Uncertainty on `m_c`

**Comparison:**

- **Direct test:** does the fitted `V(m)` curve pass through `V = 0.304` at a mass within the data range? Yes / No.
- **Consistency check:** if yes, does the crossing match any threshold or transition value reported by Eibenberger?
- **Extrapolation test:** if no, what mass does extrapolation predict for the crossing? Compare to upper-bound trends in later Arndt-group data (Fein et al. 2019, etc.).

---

## 6. What this memo does NOT do

- **Does not extract any data.** The PDF is not in this session.
- **Does not fabricate visibility values.** No entries in the §3.1 table are populated from memory.
- **Does not compute Λ.** Awaiting §3.2 data.
- **Does not determine `m_c`.** Awaiting §3.1 data.
- **Does not execute the comparison.** Awaiting completed extraction.

**I can confirm: no numbers in this memo have been invented. Every entry is either a placeholder labeled `PENDING PDF` or a value derived from already-existing prior memos (the `D_crit ≈ 0.828` and `V_c ≈ 0.304` predictions).**

---

## 7. Remaining for the final retrodiction-verdict memo

### 7.1 Data retrieval — external action required

- [ ] Obtain Eibenberger et al. 2013 PDF (author preprint from Arndt group website, publisher DOI, university library, or ResearchGate)
- [ ] Alternatively: user provides the specific visibility-vs-mass data points directly (copied from the figures or table)
- [ ] Obtain Gerlich et al. 2007 KDTLI apparatus paper for the apparatus parameters if not fully specified in Eibenberger 2013

### 7.2 Secondary literature

- [ ] Obtain Hornberger et al. 2012 *Rev. Mod. Phys.* **84**, 157 for the Λ formula
- [ ] Obtain vibrational-spectroscopy literature on tetraphenylporphyrin derivatives for `τ_internal` estimate
- [ ] Identify whether a later Arndt-group paper (Fein 2019 or similar) extends the mass range in a way that makes the `V = 0.30` crossing observable

### 7.3 Extraction pass (once data is in hand)

- [ ] Populate §3.1 table from Figs./tables of Eibenberger 2013
- [ ] Populate §3.2 table from Methods section
- [ ] Estimate §3.3 `τ_internal` with order-of-magnitude honesty
- [ ] Compute §3.4 `Λ` and `ζ` for each mass class
- [ ] Determine `m_c` at `V = 0.304` via §4 protocol

### 7.4 Verdict memo assembly (once §7.3 complete)

- [ ] Draft `quantum/retrodictions/arndt_verdict.md`
- [ ] Report comparison: predicted `V_c ≈ 0.30` vs. measured `V(m_c)` at the experimental transition mass, OR predicted `m_c` at the extrapolated crossing vs. observed trend
- [ ] Verdict: consistent / inconclusive / refuted / requires-extension
- [ ] Document all CANDIDATE commitments that were required; disclose tuning if any was needed

### 7.5 Distinguishing-signature check (optional, stronger-form retrodiction)

- [ ] Check for `N_osc ≈ 9` transient-oscillation signature in low-D regime of Eibenberger data (if the data granularity supports this)
- [ ] Check for 3–6% third-harmonic signature
- [ ] These would distinguish ED from standard decoherence theory in a way the `V_c ≈ 0.30` consistency check alone does not

---

## 8. Fallback if the PDF is unobtainable

If Eibenberger et al. 2013 cannot be retrieved:

**Option A — alternative Arndt dataset.** Haslinger et al. 2013 (OTIMA interferometer), Gerlich et al. 2011 (previous KDTLI), or Fein et al. 2019 (newer high-mass) may be more accessible and can substitute. Each would require its own extraction pass with apparatus parameters refit.

**Option B — use a non-Arndt experimental system.** The Q-C transition can be checked against other platforms from the Arndt scaffold §1 list: Haroche cavity-QED, Devoret-Martinis-Clarke superconducting qubits, Aspelmeyer optomechanics. Each has different channel-counting requirements that would need to be re-derived (the `visibility_to_bandwidth.md` memo is KDTLI-specific).

**Option C — theoretical refinement first.** Return to `visibility_to_bandwidth.md §7` and derive one of the three SPECULATIVE items (exponent 2, `b_coh = V²`, channel-counting scheme). This strengthens the prediction before testing, at the cost of further delay.

Recommendation if blocked: **Option A**, specifically Haslinger 2013 OTIMA or Fein 2019 high-mass, because they share apparatus class with Eibenberger 2013 and the same theoretical derivation chain applies.

---

## 9. Summary of current status

**In hand (from prior memos):**

- Predicted `D_crit ≈ 0.828`
- Predicted `V_c ≈ 0.304`
- Derivation chain from primitives to both predictions

**Missing (required for verdict):**

- Specific Eibenberger 2013 visibility-vs-mass data
- Apparatus parameters for Hornberger-Λ computation
- Literature value for `τ_internal`

**Honest bottom line:** the theory chain is complete; the retrodiction is fully specified in advance; the arithmetic is mechanical. **Only the literature retrieval stands between this program and an executable retrodiction verdict against Arndt data.** That retrieval is a real-world action I cannot take from within this session: either the user provides the PDF or the relevant numerical data, or the extraction is deferred to a future session with appropriate access.

This is the honest stopping point for Path C Step 2 at the current session boundary.

---

## 10. Cross-references

- Arndt Step 2 attempt: [quantum/retrodictions/arndt_step_2.md](arndt_step_2.md)
- Arndt scaffold: [quantum/retrodictions/arndt_interferometry.md](arndt_interferometry.md)
- Visibility→D derivation: [quantum/effective_theory/visibility_to_bandwidth.md](../effective_theory/visibility_to_bandwidth.md)
- ζ derivation: [quantum/effective_theory/zeta_derivation.md](../effective_theory/zeta_derivation.md)
- PDE-parameter mapping: [quantum/effective_theory/pde_parameter_mapping.md](../effective_theory/pde_parameter_mapping.md)
- Tightening pass: [quantum/primitives/TIGHTENING_PASS_01.md](../primitives/TIGHTENING_PASS_01.md)
- D_crit formula: [theory/D_crit_Resolution_Memo.md](../../theory/D_crit_Resolution_Memo.md)

---

## 11. One-line summary

> **The Eibenberger 2013 PDF is not in this session; the data-extraction template is laid out with explicit `PENDING PDF` flags and no fabricated numbers. The theory chain is complete; the predicted transition visibility is `V_c ≈ 0.304`; retrieving the PDF (or the user providing the key data directly) is the one remaining step before the retrodiction verdict can be computed. A methodological concern is flagged: Arndt-group papers typically demonstrate sustained interference rather than a measured Q-C transition, so the comparison may need to be framed as extrapolation or cross-dataset rather than as direct measurement of `m_c`.**
