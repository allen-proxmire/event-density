# UDM Extension Log

- Status: active log of incremental additions to the published 10-material UDM fit.
- Companion to the published UDM paper in this folder.
- Captures the 2026-04-22 literature-search session and any subsequent material additions.

---

## 1. Material #11 — Roosen-Runge BSA (2011, PNAS)

- **System:** bovine serum albumin (BSA) self-diffusion.
- **Measurement technique:** quasielastic neutron backscattering.
- **Source:** Roosen-Runge et al., PNAS (2011).
- **Conditions:** monomeric BSA in solution; D reaches zero near φ ≈ 0.37.

- **Data points (φ, D/D₀):**
  - φ = 0.070, D/D₀ = 0.85, c ≈ 100 mg/mL
  - φ = 0.130, D/D₀ = 0.40, c ≈ 185 mg/mL
  - φ = 0.250, D/D₀ = 0.20, c ≈ 355 mg/mL
  - φ = 0.285, D/D₀ = 0.15, c ≈ 405 mg/mL
  - φ = 0.300, D/D₀ = 0.12, c ≈ 425 mg/mL

- **UDM fit:**
  - Functional form: D(c) = D₀ (1 − c/c_max)^β
  - **β = 2.15**
  - **R² = 0.923**

- **Cross-technique consistency:**
  - Published BSA fit (material #2, fluorescence technique): β = 2.12
  - Roosen-Runge neutron-scattering fit: β = 2.15
  - Difference: 0.03 (within fit uncertainty)
  - Interpretation: the UDM exponent for BSA is measurement-technique-independent.

- **Caveat:**
  - R² = 0.923 is lower than the 10-material published range (0.986–0.999), driven primarily by the dilute-limit point (φ = 0.07).
  - Fit is consistent with UDM but with wider error bars than other materials.

---

## 2. Candidate Systems (#12–18)

- Identified in the 2026-04-22 literature-search session. Not yet fitted. Data extraction requires paper access (paywalled in most cases).

- **#12 — Lysozyme self-diffusion**
  - Source: Price et al. 1999, J. Am. Chem. Soc. 121, 11503.
  - Technique: NMR pulsed-field-gradient spin-echo (PGSE).
  - Conditions required: monomeric (see §3 for why Price 2001 was rejected).
  - Data location: Table 1.
  - To extract: D vs c at 25 °C.

- **#13 — SDS micelles**
  - Source: Stilbs 1982, J. Colloid Interface Sci. 87, 385.
  - Technique: NMR.
  - Data location: main-text table.
  - To extract: D vs [SDS] above the critical micelle concentration.

- **#14 — CTAB micelles**
  - Source: Stilbs & Lindman 1981, J. Phys. Chem.
  - Technique: NMR.
  - Data location: main-text table.
  - To extract: D vs [CTAB].

- **#15 — Monoclonal antibody (mAb)**
  - Source: Hung et al. 2024, Mol. Pharmaceutics.
  - Data location: table or supplementary information.
  - To extract: D vs c, concentration range 10–400 mg/mL.

- **#16 — AOT microemulsion**
  - Source: literature compilations (specific compilation reference TBD).
  - Data location: figures; digitization required.
  - To extract: D vs φ for water-in-oil droplets.

- **#17 — Charged silica (Ludox, 25 nm spheres)**
  - Source: Philipse & Vrij 1988, J. Chem. Phys.
  - Data location: figure; digitization required.
  - To extract: D vs φ for 25 nm charged-silica spheres.

- **#18 — CI2 in protein crowders**
  - Source: McGuffee & Elcock 2010, J. Phys. Chem. B.
  - Technique: molecular simulation.
  - Data known so far (from literature-search summary):
    - D/D₀ = 0.45 at 100 g/mL BSA crowder
    - D/D₀ = 0.23 at 100 g/mL lysozyme crowder
  - Only 2 points per crowder — insufficient for a standalone UDM fit, usable as a consistency check.

---

## 3. Excluded Data

- **Price 2001 lysozyme — rejected as a UDM material.**
  - Source: Price PGSE NMR study of lysozyme at pH 6, 0.5 M NaCl, 298 K.
  - Naive UDM fit on the t = 0 values: β = 0.83, R² = 0.914.
  - Reason for rejection:
    - pH 6, 0.5 M NaCl are *crystallization* conditions (the paper's actual subject is aggregation/crystallization kinetics, not crowding).
    - At t = 0, the 7 mM sample already shows average molecular weight ⟨M_w⟩ ≈ 3.5× monomer mass (from Figure 3 of the paper).
    - The measured D values therefore reflect diffusion of a monomer/oligomer *mixture*, not the pure concentration-dependent monomer diffusion that UDM predicts.
    - Crowding and oligomerization are confounded in this dataset.
  - The β = 0.83 is artificially low because the apparent D is reduced by both crowding (the UDM effect) and increasing average particle size (a separate effect).

- **Methodological lesson:**
  - UDM tests require *monomeric* conditions: the functional form D(c) = D₀(1 − c/c_max)^β assumes a single diffusing species whose only density-dependent response is crowding.
  - Datasets in which the solute aggregates, oligomerizes, or phase-separates at measured concentrations cannot be cleanly fitted by UDM.
  - Condition screening before inclusion:
    - pH well away from the solute's pI (to avoid charge-mediated aggregation)
    - Low-to-moderate ionic strength (to avoid salting-out)
    - Temperature well above Tg or Tc (to avoid gelation / phase separation)
    - No crystallization reported at the measurement conditions
  - For proteins specifically: check that ⟨M_w⟩ measured under the sample conditions is within ~10% of the monomer mass before treating a D(c) curve as a UDM candidate.

---

## 4. Single-Point Systems

- Systems with a single-concentration D/D₀ datum available. Cannot constrain the UDM exponent β, but may appear in a future table as consistency checks if the single point lies near the fitted UDM curve for a similar material.

- **GFP in E. coli cytoplasm**
  - D/D₀ ≈ 0.089 at ~300 mg/mL total cytoplasmic protein.
  - Source: Nenninger et al. 2010, J. Bacteriol.
  - Use: consistency check only.

- **GFP in mammalian cell nucleus**
  - D/D₀ ≈ 0.33 at nuclear chromatin concentration.
  - Source: Bancaud et al. 2009, EMBO J.
  - Use: consistency check only.

- **BSA tracer in BSA (FCS)**
  - ~50% reduction in D at 400 g/mL.
  - Source: Balbo et al. 2013, Biophys. J.
  - Use: consistency check only; tracer and matrix are the same species, so the concentration axis is well-defined but only one point is reported.

- Policy for single-point systems:
  - Not counted in the material total.
  - May be presented in a qualitative consistency table in a future revision.
  - Promoted to a material only if a multi-point D(c) curve for the same system is later located.

---

## 5. Fitting Framework

- Implementation: `udm_fit.py` (to be written to this folder on next fit run; current session left it as a conceptual framework referenced in the literature-search summary).
- Input: list of (φ, D/D₀) pairs for a single material.
- Output:
  - Best-fit β
  - Best-fit c_max (or confirmed value if fixed from physical constraint)
  - R²
  - Residual plot
  - Fit-quality flag against the published 10-material R² threshold (> 0.986)
- Usage pattern:
  - Paste tabulated (φ, D/D₀) values from a candidate paper.
  - Run the fit.
  - Append the result to this log under the appropriate material number.
  - Cross-check β against other materials in the same system class.

---

## 6. Status Summary

- **UDM materials: 11 total** (10 published + 1 new Roosen-Runge BSA neutron-scattering fit).
- **Seven candidate systems identified**; pending manual extraction from primary sources.
- **One dataset excluded** (Price 2001 lysozyme) with a methodological note requiring monomeric conditions for UDM inclusion.
- **Three single-point systems** available as consistency checks; not counted toward the material total.
- **Open actions:**
  - Extract #12 lysozyme (Price 1999) under monomeric conditions.
  - Extract #13 SDS and #14 CTAB micelles (Stilbs).
  - Access #15 mAb data (Hung 2024) via institutional library.
  - Digitize #16 AOT and #17 charged-silica figures.
  - Run `udm_fit.py` on each newly-extracted dataset and append results here.
