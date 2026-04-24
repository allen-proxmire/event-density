# Fein et al. 2019 Retrodiction Scaffold

**Date:** 2026-04-24
**Location:** `quantum/retrodictions/fein2019_scaffold.md`
**Status:** **Data not retrieved. Memo produces a template; no numbers are fabricated.** The Fein et al. 2019 *Nature Physics* paper is not in this working session. This scaffold lays out the extraction template, flags the apparatus-class distinction from Eibenberger 2013, and specifies the decision tree for the final verdict.
**Purpose:** Prepare the retrodiction infrastructure for Fein 2019 data so that once the PDF (or the specific numerical values) is supplied, the comparison executes mechanically.

---

## 1. Purpose of this dataset choice

Fein et al. 2019, *Nature Physics* **15**, 1242–1245, reports matter-wave interference for molecules with masses up to ~25,000 amu — approximately 2.5× the Eibenberger 2013 record. This dataset is the **best near-term candidate** for a Q-C-crossing retrodiction because:

1. **Extended mass range.** Higher mass → stronger decoherence → potentially `V_measured` crossing below the ED-predicted envelope-corrected threshold `V_c_measurable ≈ 0.12` (see `apparatus_envelope.md §3`).
2. **Published mass sweep.** Unlike Eibenberger 2013 (which focuses on a single-mass demonstration), Fein 2019 reports visibility at multiple masses across its library. This is the kind of sweep the ED retrodiction was framed to test.
3. **Same research group and molecular class.** Functionalized oligoporphyrins continue from earlier Arndt-group work; decoherence modeling is already established for this class.

**Key question this scaffold prepares to answer:**

> *Does `V_measured(m)` in Fein 2019 cross below the envelope-corrected ED-predicted Q-C threshold at some measured mass `m_c`?*

- If yes: execute the full Q-C-crossing retrodiction test.
- If no: verdict is "consistent but not testing" (same class as Eibenberger 2013).

---

## 2. Apparatus-class distinction from Eibenberger 2013

**Important:** Fein 2019 uses the **LUMI** (Long-Baseline Universal Matter-wave Interferometer), *not* the KDTLI apparatus of Eibenberger 2013. The apparatus-envelope `V_env` will be different.

### 2.1 Known differences (from general recall; verify against the PDF)

| Property | KDTLI (Eibenberger 2013) | LUMI (Fein 2019) |
|---|---|---|
| Baseline length | ~0.7 m | ~2 m |
| Grating structure | SiN material + optical phase + SiN material | similar 3-grating topology, longer |
| Typical molecular velocity | ~85 m/s | lower (~10–70 m/s) due to higher mass |
| Typical Talbot time | ~1 ms | ~10 ms or longer |
| Empirical V_env at peak | ~0.40 (from Fig. 3(b)) | **PENDING PDF** |

### 2.2 Consequence

The envelope derivation in `apparatus_envelope.md` assumed KDTLI parameters and used the empirical `V_env ≈ 0.40` reading from Eibenberger 2013 Fig. 3(b). For Fein 2019, this must be redone:

- Read `V_env_LUMI` from Fein 2019's equivalent quantum-prediction plot (if the paper shows one).
- Or reconstruct from LUMI apparatus parameters via the same structural formula as `apparatus_envelope.md §2.5`, with LUMI-specific numerical inputs.

**Once `V_env_LUMI` is in hand, the envelope-corrected ED prediction becomes:**

```
V_c_measurable_LUMI = V_env_LUMI × 0.304                    (1)
```

This is the threshold to compare Fein 2019 data against.

---

## 3. Data-extraction template

### 3.1 Visibility-vs-mass data

To populate from Fein 2019 figures (likely Fig. 2 or Fig. 3):

| Molecule label | Mass `m` (amu) | Visibility `V` (%) | Error bar on V | Notes |
|---|---|---|---|---|
| — | **PENDING PDF** | **PENDING PDF** | **PENDING PDF** | |
| — | **PENDING PDF** | **PENDING PDF** | **PENDING PDF** | |
| — | **PENDING PDF** | **PENDING PDF** | **PENDING PDF** | |
| — | **PENDING PDF** | **PENDING PDF** | **PENDING PDF** | |
| — | **PENDING PDF** | **PENDING PDF** | **PENDING PDF** | |

**Population rule:** every row must trace to a specific figure or table in the Fein 2019 PDF. No values populated from memory. Rows not traceable are flagged `CANNOT EXTRACT`.

### 3.2 LUMI apparatus parameters

| Parameter | Symbol | Value | Source |
|---|---|---|---|
| Grating period (G1, G3) | `d` | **PENDING PDF** | Methods |
| Slit width (G1, G3) | `s` | **PENDING PDF** | Methods |
| Optical-grating wavelength | `λ` | **PENDING PDF** | Methods |
| Laser power | `P` | **PENDING PDF** | Methods (per-measurement) |
| Beam waist `x` | `w_x` | **PENDING PDF** | Methods |
| Beam waist `y` | `w_y` | **PENDING PDF** | Methods |
| Mean velocity | `v` | **PENDING PDF** | Methods (per-mass) |
| Velocity spread | `Δv` | **PENDING PDF** | Methods |
| Grating-to-grating distance | `L` | **PENDING PDF** | Methods (LUMI geometry) |
| Talbot length | `L_T = d²·m·v/h` | **COMPUTABLE** per mass | Derived |
| Internal molecular temperature | `T_int` | **PENDING PDF** | Methods |
| Residual gas pressure | `p` | **PENDING PDF** | Methods |

### 3.3 Quantum-prediction envelope curve

Does Fein 2019 plot a theoretical quantum-prediction visibility curve (the analog of Eibenberger 2013 Fig. 3(b) blue line)?

- **If yes:** read the peak value as `V_env_LUMI`.
- **If no:** LUMI-specific envelope must be computed from §3.2 apparatus parameters using the Talbot-Lau visibility formula (same structural approach as `apparatus_envelope.md §2`).

**Status:** PENDING PDF inspection.

### 3.4 Hornberger Λ values (if computed in paper)

| Mass | Λ_thermal-photons | Λ_gas-collisions | Λ_total | Notes |
|---|---|---|---|---|
| — | **PENDING PDF** | **PENDING PDF** | **PENDING PDF** | Check supplementary materials |

Fein 2019 may include Hornberger-Λ calculations in their analysis (the Arndt group routinely computes these). If present, they can be used directly for the `ζ_Arndt` computation via `zeta_derivation.md §4`.

---

## 4. Analysis template (to execute once §3 is populated)

### 4.1 Compute V_env_LUMI

**Option A (if paper provides quantum-prediction curve):**
Read peak V from the curve. Record in §3.3.

**Option B (if not):**
Compute from apparatus parameters via:
```
V_env = 2 · |A_1^G1| · |A_1^G2|_max · |A_1^G3| · W_v · W_s
```
per `apparatus_envelope.md §2.5` with LUMI-specific numerical inputs. Flag factor-convention issues per `apparatus_envelope.md §2.6` (first-pass formulas may be off by multiplicative convention factors).

### 4.2 Compute V_c_measurable_LUMI

```
V_c_measurable_LUMI = V_env_LUMI × 0.304                    (2)
```

### 4.3 Check threshold crossing

For each (mass, visibility) row in §3.1:

- Compute `V_coh(m) = V(m) / V_env_LUMI`
- Compare V(m) to V_c_measurable_LUMI

**Find `m_c`:** the mass at which the smooth-fit of V(m) drops below V_c_measurable_LUMI.

**If such an `m_c` is found within the Fein 2019 data range:** proceed to §4.4 for verdict.
**If V(m) > V_c_measurable_LUMI across the full data range:** verdict is "consistent but not testing" — L12-analogous situation extended to higher mass.

### 4.4 ED prediction for `m_c` (if threshold crossing is observed)

The ED derivation does not currently predict `m_c` directly — `m_c` is the apparatus-dependent mass at which the combination of decoherence rate and apparatus conditions drives `V_measured` below `V_c_measurable`. To predict `m_c` a priori requires:

- `ζ_Arndt(m) = Λ(m) · τ_internal(m)` — mass-dependent ζ
- `D_crit(ζ_Arndt(m))` — mass-dependent D_crit
- `V_c_raw(m) = V_c_raw(D_crit(ζ_Arndt(m)))` — solving D(V) = D_crit
- `V_c_measurable(m) = V_env_LUMI(m) × V_c_raw(m)` — full envelope-corrected prediction

**All but the last step vary with mass in principle but were held constant in the Eibenberger derivation because ζ ≪ 1 across all relevant parameters.** For Fein 2019 masses (~25,000 amu), the same limit likely applies; ζ remains ≪ 1. This means:

```
V_c_raw ≈ 0.304   regardless of mass (under current derivation)
V_c_measurable(m) ≈ V_env_LUMI(m) × 0.304
```

If `V_env_LUMI` is approximately mass-independent in the Fein 2019 range, then `V_c_measurable` is approximately a single value, and `m_c` is defined by the intersection of that horizontal line with the measured V(m) curve.

### 4.5 Comparison

Compare the measured `m_c` to any transition-mass or threshold-mass value reported by Fein 2019 (if one is reported at all — they may report "quantum behavior observed at all masses studied" without identifying a transition).

---

## 5. Decision tree for verdict classification

```
V(m) from Fein 2019 data
       |
       v
  Does any V(m) fall below V_c_measurable_LUMI?
       |
   ____|____
  |         |
  YES       NO
  |         |
  v         v
  Q-C      "Consistent but
  crossing  not testing"
  found     (same as
  |         Eibenberger 2013
  v         L12 case)
  Compare
  m_c measured to
  ED framework
  expectations
  |
  v
  Verdict:
  - Consistent (measured m_c near predicted, agreement within error)
  - Refuted (measured m_c far from any expectation, or no m_c found)
  - Inconclusive (sparse data, large error bars)
```

**Per `zeta_derivation.md §5.3`:** the ED framework does not predict a sharp mass value for `m_c` because ζ is unconstrained at the apparatus level; the prediction is a threshold visibility `V_c_measurable`, not a transition mass. A retrodiction under this framing is "did the experiment cross the predicted visibility threshold at all?" not "did it cross at the predicted mass?"

**To promote the Fein 2019 test from "threshold crossing observed / not observed" to "mass-of-crossing predicted / measured," the mass-dependent ζ_Arndt(m) would have to be computed** — requiring Hornberger Λ(m) values either from the paper or computed from apparatus parameters. This is the quantitative upgrade that would make the Fein 2019 test distinguishing rather than merely consistent.

---

## 6. Status classifications

| Derivation component | Status |
|---|---|
| Decomposition `V = V_env × V_coh` (from apparatus_envelope.md) | FORCED |
| ED prediction `V_c_raw ≈ 0.304` (from visibility_to_bandwidth.md) | CANDIDATE (three upstream commitments) |
| ζ ≪ 1 at Fein 2019 masses | CANDIDATE (same argument as Eibenberger; verify for LUMI-specific τ_internal) |
| `V_env_LUMI` value | PENDING PDF |
| Fein 2019 visibility-vs-mass data | PENDING PDF |
| Apparatus parameters | PENDING PDF |
| `V_c_measurable_LUMI` numerical value | PENDING (follows from V_env_LUMI) |
| Threshold-crossing detection | PENDING (follows from V(m) data) |
| Mass-of-crossing prediction | SPECULATIVE (requires mass-dependent ζ_Arndt(m)) |

---

## 7. What this memo does NOT do

- **Does not extract any data.** The Fein 2019 PDF is not in this session.
- **Does not fabricate visibility values or apparatus parameters.** No entries populated from memory; every table cell labeled `PENDING PDF`.
- **Does not derive LUMI-specific envelope.** Will be done once apparatus parameters are retrieved.
- **Does not execute the comparison.** Awaiting data.

**No numbers in this scaffold have been invented.** The only numerical commitments are those inherited from prior memos (`V_c_raw ≈ 0.304` from `visibility_to_bandwidth.md`, `ζ ≪ 1` argument from `zeta_derivation.md`).

---

## 8. Fallback considerations

### 8.1 If Fein 2019 does not report a sharp `m_c`

Likely. Arndt-group publications typically demonstrate sustained quantum behavior rather than measured transitions. In this case:

- Report `V_measured` at highest mass studied.
- Compute `V_coh_min = V_min / V_env_LUMI` (the lowest coherence fraction reached in the experiment).
- Compare to ED `V_c_raw = 0.304`: if `V_coh_min > 0.304`, experiment did not reach the ED-predicted Q-C boundary; if `V_coh_min < 0.304`, the threshold was crossed.
- This gives the "consistent-vs-threshold-crossing" binary verdict even without a sharp `m_c`.

### 8.2 If data is only available for a single mass

Report as Eibenberger-2013-style single-mass result. Not a mass-sweep retrodiction; "consistent weak-form" verdict at best.

### 8.3 If LUMI apparatus parameters are not in the main paper

Check supplementary materials. The Arndt group typically publishes apparatus details in supplementary PDFs. If still not available, the LUMI envelope must be estimated from general LUMI geometry (see Geyer et al. 2018, or the LUMI design paper).

### 8.4 If Fein 2019 cannot be obtained

Alternative datasets sharing the structural goal:
- **Gerlich et al. 2011** (*Nature Communications* **2**, 263) — earlier Arndt-group work with functionalized fullerenes and porphyrins
- **Brezger et al. 2002** (*PRL* **88**, 100404) — original Talbot-Lau with C_60, C_70, biomolecules
- **Haslinger et al. 2013** (*Nature Physics* **9**, 144) — OTIMA, different apparatus class (requires separate envelope derivation)

**Recommendation priority:** Fein 2019 > Gerlich 2011 > Brezger 2002, by mass-range coverage and likelihood of threshold-crossing. Haslinger 2013 deferred pending OTIMA envelope derivation.

---

## 9. Checklist for the final verdict memo

### 9.1 Data retrieval

- [ ] Obtain Fein et al. 2019 PDF (arXiv preprint, publisher DOI, ResearchGate, or supplied directly)
- [ ] Extract visibility-vs-mass data points (table §3.1)
- [ ] Extract LUMI apparatus parameters (table §3.2)
- [ ] Extract quantum-prediction envelope curve if present (§3.3)
- [ ] Check supplementary materials for additional data if main paper is sparse

### 9.2 Envelope derivation

- [ ] Read or compute `V_env_LUMI`
- [ ] Document convention choices if formula-reconstruction is used
- [ ] Cross-check against any quantum-prediction curve in the paper

### 9.3 Comparison execution

- [ ] Compute `V_c_measurable_LUMI = V_env_LUMI × 0.304`
- [ ] Check whether any V(m) data point falls below this threshold
- [ ] If yes: identify `m_c` and compute coherence-fraction V_coh at threshold crossing
- [ ] If no: report lowest `V_coh` achieved and compare to 0.304

### 9.4 Verdict classification

- [ ] Assign verdict: Q-C crossing observed / consistent-weak-form / inconclusive / refuted
- [ ] Document all commitments that fed into the verdict (CANDIDATE inheritance from earlier memos)
- [ ] If threshold crossing observed: attempt mass-of-crossing prediction via mass-dependent ζ_Arndt(m) calculation
- [ ] Disclose any discrepancies between Fein 2019's own interpretation and the ED retrodiction framing

### 9.5 Write-up

- [ ] Draft `quantum/retrodictions/fein2019_verdict.md`
- [ ] Include full comparison table with uncertainties
- [ ] Identify next-priority dataset if Fein 2019 also does not reach the Q-C boundary
- [ ] Update `arndt_interferometry.md` scaffold with the resolved / unresolved status after the Fein test

### 9.6 Distinguishing-signature check (optional, stronger claim)

- [ ] Check Fein 2019 data for ED-specific signatures: `N_osc ≈ 9` oscillations, 3–6% third-harmonic, sharp vs. smooth transition
- [ ] These would distinguish ED from standard decoherence theory in a way the threshold-crossing check does not

---

## 10. Summary

**Purpose:** Fein 2019 is the best near-term candidate for a Q-C-crossing retrodiction test because it extends the Arndt-group mass range to ~25,000 amu, potentially crossing the envelope-corrected ED threshold `V_c_measurable ≈ 0.12` (or the LUMI-specific equivalent).

**Status:** Data not in session. Scaffold laid out with explicit `PENDING PDF` markers. LUMI apparatus-class distinction from KDTLI flagged; envelope must be re-derived or read from Fein 2019's own quantum-prediction curve.

**Decision tree (§5):** threshold-crossing observed → executable retrodiction; no threshold crossing → "consistent but not testing" (L12-class verdict extended to higher masses).

**Honest note on expected outcome:** Arndt-group publications typically demonstrate sustained quantum behavior at their highest masses. If Fein 2019 follows this pattern and `V_measured(25,000 amu)` remains above `V_c_measurable_LUMI`, the retrodiction will be inconclusive — consistent with ED but not distinguishing from standard decoherence theory. This outcome would be the same epistemic class as Eibenberger 2013. A genuinely distinguishing test would require either (a) data from a mass regime where visibility genuinely collapses, or (b) checking for ED-specific signatures (N_osc ≈ 9, 3–6% harmonic) in the transition region.

**What this memo enables:** the moment Fein 2019 data (PDF, specific numerical values, or apparatus parameters) is supplied, the comparison executes mechanically per the §9 checklist. No further theory work is required for a first-pass verdict.

---

## 11. Cross-references

- Envelope correction: [quantum/effective_theory/apparatus_envelope.md](../effective_theory/apparatus_envelope.md)
- Arndt verdict for Eibenberger 2013: [quantum/retrodictions/arndt_verdict.md](arndt_verdict.md)
- Visibility→D derivation: [quantum/effective_theory/visibility_to_bandwidth.md](../effective_theory/visibility_to_bandwidth.md)
- ζ derivation: [quantum/effective_theory/zeta_derivation.md](../effective_theory/zeta_derivation.md)
- PDE-parameter mapping: [quantum/effective_theory/pde_parameter_mapping.md](../effective_theory/pde_parameter_mapping.md)
- Arndt data extraction (Eibenberger scaffold): [quantum/retrodictions/arndt_data_extraction.md](arndt_data_extraction.md)
- Arndt scaffold: [quantum/retrodictions/arndt_interferometry.md](arndt_interferometry.md)
- Source paper (to be retrieved): Fein, Geyer, Zwick, Kiałka, Pedalino, Mayor, Gerlich, Arndt (2019), *Nature Physics* **15**, 1242–1245

---

## 12. One-line summary

> **Fein 2019 LUMI-interferometer data up to ~25,000 amu is the best available candidate for a Q-C-crossing retrodiction test; the scaffold lays out the extraction template, flags the apparatus-class distinction from KDTLI (envelope must be re-derived for LUMI), and specifies the decision tree. If Fein 2019 data crosses below `V_c_measurable_LUMI = V_env_LUMI × 0.304`, the ED prediction is testable; if not, verdict is "consistent but not testing" in the same epistemic class as Eibenberger 2013. Data retrieval is the one outstanding action.**
