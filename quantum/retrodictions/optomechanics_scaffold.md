# Optomechanical / BEC Collective-Mode Retrodiction Scaffold

**Date:** 2026-04-24
**Location:** `quantum/retrodictions/optomechanics_scaffold.md`
**Status:** Scaffold memo. No data extracted, no retrodiction executed. Identifies optomechanical ring-down and BEC collective-mode decay as the correct temporal testbed for ED's N_osc / Q predictions — spatial-relaxation structure preserved (unlike 0-D SC qubit case of `sc_qubit_pde_mapping.md`). Produces mapping candidates, dataset shortlist, and data-extraction template. Flags two structural issues: typical optomechanical Q is too high; BEC collective-mode Q is in the right range but datasets may be sparse.
**Purpose:** Pivot from the SC-qubit retrodiction path (blocked on 0-D / spatial mismatch) to platforms where ED-Phys-17's spatial peak-relaxation picture maps naturally.

---

## 1. Why optomechanics / BEC preserve the ED structure

ED-Phys-17 §4.1 derives the N_osc ≈ 9 prediction from the relaxation dynamics of a **spatially-extended Gaussian density peak** in a 1D or 2D ED field. The peak height oscillates as the field relaxes: ρ(x_peak, t) swings around ρ_star while the peak decays into its surrounding medium. This requires:

- A **spatially-extended field** ρ(x, t) with non-trivial mode structure.
- A **localized excitation** (peak) that can relax into the surrounding continuum.
- **Both the mobility channel** `M(ρ)∇²ρ` **and the penalty channel** `P(ρ)` active.

### 1.1 0-D systems (qubits) lose this structure

Per `sc_qubit_pde_mapping.md §2.1`: reducing the PDE to 0-D kills the mobility channel. Only the penalty + participation channels remain. ED-Phys-17's prediction, derived from the full spatial PDE, does not straightforwardly apply.

### 1.2 Optomechanical mechanical modes preserve spatial structure

A mechanical mode of a resonator (cantilever, membrane, photonic-crystal defect, levitated particle) is a spatially-extended oscillation with:

- Mode shape `u_n(x)` (a specific spatial profile for mode `n`).
- Temporal amplitude `a_n(t)` that oscillates at frequency `ω_n` and decays at rate `Γ_n`.
- Coupling to environmental modes (phonon bath, photon-mediated dissipation).

The mechanical displacement field is `ξ(x, t) = Σ_n a_n(t) u_n(x)`. For a single-mode excitation, `ξ(x, t) = a_n(t) u_n(x)` — spatial profile fixed, amplitude oscillates and decays. This is structurally isomorphic to ED's "peak relaxing in a spatial field."

### 1.3 BEC collective modes preserve spatial structure

A BEC in a harmonic trap supports collective modes: breathing (monopole), quadrupole, scissors, dipole, etc. Each is a specific spatial deformation of the condensate density that oscillates coherently and damps through Landau + thermal mechanisms. Observable: density profile `n(x, t)` evolves with clear oscillatory time dependence in specific spatial moments (e.g., `⟨x²⟩(t)` for breathing mode).

Again structurally isomorphic to ED-Phys-17's setup.

---

## 2. Relevant observables

### 2.1 Optomechanical mechanical ring-down

**Protocol:** prepare mechanical mode in a coherent state (via optical drive, radiation-pressure cooling, or feedback). Turn off the drive. Observe the mechanical amplitude as it decays via coupling to environmental baths.

**Observable:** `a(t)` — mechanical-mode amplitude vs. time. Typically extracted via homodyne/heterodyne detection of the optical field that reads out the mechanical position.

**Signal shape:** `a(t) ≈ a_0 · cos(ω_m t + φ) · exp(−Γ_m t / 2)`.

**Extractable ED observables:**
- N_osc_observed = count of visible oscillation peaks before envelope decay below noise.
- Q_measured = ω_m / Γ_m.

**Typical parameter ranges:**

| System | ω_m (Hz) | Γ_m (Hz) | Q |
|---|---|---|---|
| Bulk mechanical (Verhagen-Kippenberg 2012) | ~10⁸ | ~10³ | ~10⁵ |
| Photonic crystal (Chan 2011) | ~10¹⁰ | ~10⁴ | ~10⁶ |
| Levitated nanosphere (Jain 2016, Magrini 2021) | ~10⁵ | ~1 | ~10⁵ |
| Membrane-in-middle (Rossi 2018) | ~10⁶ | ~1 | ~10⁶ |

**Issue:** typical optomechanical Q is **10⁴ to 10⁶**, far above ED's predicted Q ≈ 3.5. Most experiments deliberately optimize for high Q (the whole point of optomechanical ground-state cooling is to reach ultra-coherent regimes). **ED's moderate-Q prediction may require finding specific experiments or regimes where mechanical damping is substantial.**

Candidate high-damping regimes:

- Near-resonance with a lossy cavity mode (cavity-induced damping)
- Room-temperature mechanical modes (thermal damping dominates)
- Levitated systems with significant gas-pressure damping
- Feedback-cooled modes in the over-damped regime

### 2.2 BEC collective-mode decay

**Protocol:** excite a collective mode (e.g., breathing via sudden trap-frequency quench, dipole via trap displacement, scissors via trap rotation). Observe the condensate shape as the mode oscillates and damps.

**Observable:** `⟨x²⟩(t)` or similar spatial moment, or direct density-profile time-series via absorption imaging.

**Signal shape:** `⟨x²⟩(t) ≈ ⟨x²⟩_eq + A_0 · cos(ω_c t + φ) · exp(−γ_c t)`.

**Typical parameter ranges:**

| System / mode | ω_c (Hz) | γ_c (Hz) | Q |
|---|---|---|---|
| Jin 1996 Rb breathing mode | ~200 (2π·32 Hz) | ~2 | ~100 |
| MIT Na scissors (Mewes 1996) | ~160 | ~5 | ~30 |
| ENS scissors (Chevy 2002) | ~200 | ~3 | ~70 |
| High-T BEC near critical | variable | variable | ~3–30 |

**Issue:** cold BECs at T ≪ T_c typically show Q ≈ 30–100 — still higher than ED's Q ≈ 3.5 but much closer to the target than optomechanics. **High-T BECs near the critical temperature, where thermal damping is strong, exhibit Q in the 3–10 range.**

Candidate high-damping regimes:

- Near T_c (thermal collective-mode damping dominant)
- Highly anisotropic traps (mode-coupling-induced damping)
- Spinor BEC collective modes with internal-state coupling

### 2.3 Summary

| Platform | Typical Q | Distance to ED Q = 3.5 |
|---|---|---|
| Optomechanics (cold, standard) | 10⁴–10⁶ | Very far — unlikely match |
| Optomechanics (warm / high-loss) | 10–10³ | Possibly in range for specific systems |
| BEC collective modes (cold) | 30–100 | Close — within one decade |
| BEC collective modes (near T_c) | 3–30 | **Direct match range** |

**Best near-term targets: BEC collective modes near T_c, or specific optomechanical systems operated in high-damping regimes.**

---

## 3. Mapping optomechanical / BEC parameters to ED PDE variables

### 3.1 Optomechanical mapping (CANDIDATE)

| ED PDE variable | Optomechanical correspondent | Status |
|---|---|---|
| ρ(x, t) | mechanical displacement profile `ξ(x, t) = a(t) u(x)` | CANDIDATE |
| Alternatively | mechanical energy density `ξ²(x, t)` or `ξ̇²(x, t)` | CANDIDATE |
| v(x, t) | mechanical velocity field `ξ̇(x, t)` | CANDIDATE |
| ρ_star | mechanical equilibrium (ξ = 0) | FORCED |
| ω_n | mechanical frequency ω_m | FORCED |
| γ_n (decay rate) | Γ_m/2 (mechanical damping) | FORCED |
| Q | ω_m / Γ_m | FORCED |
| τ | 1/ω_m (mechanical period) | CANDIDATE |
| ζ | Γ_m · τ = Γ_m / ω_m = 1/Q | CANDIDATE |
| D_E | see §3.3 below | SPECULATIVE |
| ε_k | M_0 k_m² + P_0 where k_m is mode wavenumber | CANDIDATE |

**Key observation:** under `ζ = 1/Q`, ED's Q ≈ 3.5 maps directly to **mechanical Q ≈ 3.5**. This is a direct target to search for.

### 3.2 BEC collective-mode mapping (CANDIDATE)

| ED PDE variable | BEC correspondent | Status |
|---|---|---|
| ρ(x, t) | condensate density `n(x, t)` | FORCED (per ED Madelung anchoring; n = \|ψ\|²) |
| v(x, t) | superfluid velocity `v_s(x, t) = (ℏ/m)∇φ` | CANDIDATE |
| ρ_star | equilibrium density profile `n_eq(x)` | CANDIDATE |
| Collective-mode frequency ω_c | determined by trap + s-wave scattering | FORCED (for given mode) |
| Collective-mode decay γ_c | Landau/Beliaev damping + thermal | FORCED |
| Q_collective | ω_c / γ_c | FORCED |
| τ | 1/ω_c | CANDIDATE |
| ζ | γ_c / ω_c = 1/Q_collective | CANDIDATE |
| D_E | see §3.3 below | SPECULATIVE |
| ε_k | M_0 k² (k = inverse condensate size) | CANDIDATE |

**Notable:** the BEC mapping is cleaner than optomechanics in one respect — the ρ ↔ |ψ|² identification is direct (ED's Madelung anchoring in the quantum regime), not an analogy.

### 3.3 D_E identification (SPECULATIVE, common to both)

From the underdamping discriminant (D_crit resolution memo):

```
Q = √(1 − D(1 − ζ)) / (D + ζ)                         (1)
```

Given experimental Q and ζ = 1/Q:

```
Q² = (1 − D(1 − 1/Q)) / (1 + 1/Q)²
```

Solve for D:

```
D = [1 − Q²(1 + 1/Q)²] / (1/Q − 1)
  = [1 − (Q + 1)²] / (1/Q − 1)
  = [Q (1 − (Q+1)²)] / (1 − Q)
```

At Q = 3.5:
- (Q+1)² = 20.25
- 1 − 20.25 = −19.25
- 1 − Q = −2.5
- D = 3.5 × (−19.25) / (−2.5) = 26.95

**This is > 1, outside the PDE range D ∈ [0, 1]. The algebra suggests that under ζ = 1/Q with Q = 3.5, the linearized-PDE Q-formula does not have a solution in the physical D range.**

**Diagnostic:** either the ζ = 1/Q identification is wrong, or the Q-formula at ε_k τ = 1 doesn't apply at this parameter combination, or both.

Trying alternate ε_k τ values: per the D_crit memo §5.5, restoring ε_k and τ gives rescaling `ζ̃ = ζ/(τ ε_k)`. If τ ε_k ≠ 1, the effective ζ differs from 1/Q.

For the Q-formula to give D ∈ [0, 1] at Q = 3.5 requires (per §5.3 of sc_qubit_pde_mapping.md) ζ ≈ 0.15–0.20, corresponding to τ ε_k in a specific range. **The ζ identification for optomechanics / BEC must therefore include an ε_k factor, not just 1/Q.**

**Candidate resolution:** ζ includes both the temporal damping-to-frequency ratio (1/Q) and a spatial-mode factor (ε_k at the relevant wavenumber). Explicit derivation required to pin down the combination. This is SPECULATIVE and is the main remaining derivation task for this platform.

---

## 4. Candidate datasets

### 4.1 Optomechanics (selected from 2010–2020s literature)

**Mechanical ring-down with visible oscillations:**

1. **Verhagen, Deléglise, Weis, Schliesser, Kippenberg (2012)** "Quantum-coherent coupling of a mechanical oscillator to an optical cavity mode." *Nature* 482, 63. Normal-mode splitting, time-resolved coherent state exchange. arXiv:1107.3761.

2. **Chan, Alegre, Safavi-Naeini, Hill, Krause, Gröblacher, Aspelmeyer, Painter (2011)** "Laser cooling of a nanomechanical oscillator into its quantum ground state." *Nature* 478, 89. Sideband cooling + ring-down.

3. **Teufel, Donner, Li, Harlow, Allman, Cicak, Sirois, Whittaker, Lehnert, Simmonds (2011)** "Sideband cooling of micromechanical motion to the quantum ground state." *Nature* 475, 359.

4. **Rossi, Mason, Chen, Tsaturyan, Schliesser (2018)** "Measurement-based quantum control of mechanical motion." *Nature* 563, 53. Feedback-cooled membrane; detailed time traces.

5. **Jain, Gieseler, Moritz, Dellago, Quidant, Novotny (2016)** "Direct measurement of photon recoil from a levitated nanoparticle." *PRL* 116, 243601. Levitated optomechanics.

**Issue for all:** Q typically 10⁴ or higher — far above ED target Q = 3.5. Would need to search for specific sub-experiments or apparatus regimes with Q in the 3–30 range.

### 4.2 BEC collective modes (preferred)

1. **Jin, Ensher, Matthews, Wieman, Cornell (1996)** "Collective excitations of a Bose-Einstein condensate in a dilute gas." *PRL* 77, 420. **First BEC collective-mode measurements with direct time-resolved data.** Several modes observed.

2. **Mewes, Andrews, van Druten, Kurn, Durfee, Townsend, Ketterle (1996)** "Collective excitations of a Bose-Einstein condensate in a magnetic trap." *PRL* 77, 988. MIT collective-mode data.

3. **Chevy, Madison, Dalibard (2000)** "Measurement of the angular momentum of a rotating Bose-Einstein condensate." *PRL* 85, 2223. Scissors-mode observation.

4. **Stamper-Kurn, Miesner, Inouye, Andrews, Ketterle (1998)** "Collisionless and hydrodynamic excitations of a Bose-Einstein condensate." *PRL* 81, 500. Temperature-dependent damping — includes near-T_c data.

5. **Jin, Matthews, Ensher, Wieman, Cornell (1997)** "Temperature-dependent damping and frequency shifts in collective excitations of a dilute Bose-Einstein condensate." *PRL* 78, 764. **Directly addresses the temperature-dependent damping regime where Q can be in the ED target range.**

### 4.3 Recommended first dataset

**Jin, Matthews, Ensher, Wieman, Cornell (1997), *PRL* 78, 764.**

**Reason for recommendation:**

- **Explicit temperature-dependent damping study.** Reports Q (= ω/Γ) for m=0 and m=2 breathing modes across temperatures from below T_c to ~0.9·T_c.
- **Q range covers ED target.** Reported Q values span ~5 (near T_c) to ~100 (cold BEC).
- **Time-resolved data shown in figures.** Published ring-down-like traces for several temperatures.
- **Clean theoretical interpretation.** Standard BEC theory (Landau damping) provides comparison baseline — ED's Q ≈ 3.5 prediction can be checked against specific (T, mode) combinations.
- **Historically important paper; widely accessible.** JILA group; data well-documented.

**Alternative first choice:** Jin 1996 original collective-mode paper — simpler but may not have the Q range ED needs.

---

## 5. Data-extraction template

### 5.1 Trace digitization

| Field | Value | Source |
|---|---|---|
| Observable | e.g., `⟨x²⟩(t)` for BEC breathing, `a(t)` for optomech | figure caption |
| Time range | `t ∈ [0, t_max]` | — |
| Temperature / operating condition | `T/T_c` for BEC, cryo temp for optomech | methods section |
| Mode identification | e.g., m=0 breathing, m=2 quadrupole | figure caption |
| Sampling points | number of data points visible | count from figure |
| Apparent noise floor | visual estimate | — |
| SNR estimate | A_initial / σ_noise | derived |

### 5.2 Oscillation counting

Protocol (same as sc_qubit scaffold):

1. Identify envelope function (fit or visual).
2. Subtract or normalize by envelope to reveal pure oscillations.
3. Count peaks above noise floor in residual.
4. Report N_osc_measured with uncertainty.

### 5.3 Q extraction

From amplitude fit `A(t) = A_0 · cos(ω t + φ) · exp(−γ t)`:
- ω extracted from peak-to-peak spacing
- γ extracted from envelope fit
- Q = ω / (2γ)

For BEC mode data where ω and γ are usually reported directly in the paper, Q extraction is just arithmetic from the paper's own values.

### 5.4 Comparison with ED prediction

| ED prediction | Measurement criterion | Match tolerance |
|---|---|---|
| Q ≈ 3.5 | measured Q within factor 2 of 3.5 | i.e., Q ∈ [1.75, 7.0] |
| N_osc = 8–19 | measured peaks in range | i.e., 8 ≤ N_peaks ≤ 19 |
| Joint consistency | both above simultaneously | — |

**Status interpretation:**

- **Strong match:** Q and N_osc both in target range — consistent retrodiction.
- **Partial match:** one in range, other not — suggests correct observable class but wrong regime mapping.
- **No match:** both out of range — refuted in this regime under current parameter identifications.
- **Not testing:** data is in far-off-regime (e.g., Q = 10⁵ optomechanics) — consistency unchecked.

---

## 6. Structural blockers discovered while drafting

### 6.1 Q-formula inconsistency (§3.3)

Under ζ = 1/Q, the underdamping-discriminant Q-formula `Q = √(1 − D(1 − ζ)) / (D + ζ)` has no physical solution in `D ∈ [0, 1]` at Q = 3.5. The ζ = 1/Q identification is too aggressive.

**Implication:** the ED Q ≈ 3.5 prediction is NOT a direct "match any oscillator with Q = 3.5" claim. It is a PDE-parameter-specific prediction that requires ζ ∈ [0.15, 0.20] approximately. The relationship between physical damping rate (1/Q) and PDE ζ must include a spatial-mode factor (ε_k), which has not been derived for these platforms.

**Required derivation:** explicit ε_k computation for (a) optomechanical mechanical modes given mode shape and coupling, (b) BEC collective modes given condensate geometry. Then `ζ = (physical damping rate) · τ · f(ε_k)` where `f` is some normalization function from the PDE.

This is the Phase 0 blocker for optomechanics / BEC, analogous to the Phase 0 blocker for SC qubits.

### 6.2 Typical Q-range mismatch

Optomechanics routinely achieves Q = 10⁴–10⁶. BEC collective modes at low T routinely achieve Q = 30–100. **Few published datasets naturally fall in the Q ≈ 3.5 range.**

Finding Q = 3.5 requires either:
- Near-T_c BEC data (highly thermally damped)
- Specific high-loss optomechanical configurations
- Heavily-damped mechanical modes (not the mainstream of the field)

This is a real experimental-selection constraint: most publications deliberately push toward high Q; ED needs moderate Q.

### 6.3 The "first dataset" specificity

Jin 1997 is recommended because it reports Q vs. T, making Q = 3.5 identifiable at some specific T. But executing the retrodiction still requires:

- Digitizing the T-dependence of Q to identify the T at which Q_measured ≈ 3.5.
- At that T, extracting the full ring-down trace and counting oscillations.
- Checking whether N_osc = 8–19 is consistent with the extracted trace.

**The two checks must pass at the same operating point**, not at different points of the dataset. This constrains the match test more tightly than a generic "does some dataset show Q = 3.5?" question.

### 6.4 ρ_star framing — spatial profile

For BEC, ρ_star is the equilibrium density profile `n_eq(x)`, not a single constant. This is different from the 0-D qubit case and from the canonical-PDE treatment around a homogeneous equilibrium. Whether the Q ≈ 3.5 linearization applies around a spatially-varying equilibrium needs explicit derivation.

For optomechanics, ρ_star ≈ 0 is the mechanical rest position — simpler but may not match ED's ρ_star = 0.5 interpretation.

---

## 7. Execution plan

### 7.1 Phase 0 — finish the ε_k / ζ derivation (PREREQUISITE)

**Task:** derive `ζ_effective = f(Γ_m/ω_m, ε_k, τ)` for optomechanical modes and BEC collective modes, such that the Q-formula (1) gives physical D ∈ [0, 1].

**Required inputs:**
- Mode shape u(x) and its eigenvalue ε_k = M_0 k_m² + P_0
- Normalization conventions for τ in the spatially-extended case
- Explicit PDE linearization around non-homogeneous ρ_star (for BEC)

**Output:** `quantum/effective_theory/optomech_bec_pde_mapping.md`. Estimated scope: 1 focused derivation session.

**Alternative framing:** if the spatial-mode factor ε_k consistently produces ζ ≈ 0.15–0.20 for typical mechanical / collective modes, the mapping is natural. If it forces specific unnatural parameter choices, the mapping is strained — which is a structural finding.

### 7.2 Phase 1 — execute Jin 1997 comparison

1. Obtain Jin 1997 *PRL* 78, 764 PDF.
2. Extract Q(T) data from figures.
3. Identify temperature T* where Q(T*) ≈ 3.5.
4. Extract ring-down trace at T* (if shown) or at nearest available T.
5. Count oscillations; extract N_osc_measured.
6. Compare to ED prediction (Q = 3.5 baseline; N_osc = 8–19 from §1).
7. Classify as match / partial match / no match / not testing.

**Output:** `quantum/retrodictions/jin1997_verdict.md`.

### 7.3 Phase 2 — cross-platform check

If Phase 1 yields match or partial match, repeat against a second dataset from a different platform:

- Stamper-Kurn 1998 (different BEC species, different apparatus) — natural BEC cross-check.
- A high-damping optomechanical dataset if available — cross-platform cross-check.

### 7.4 Phase 3 — distinguishing from competitors

Standard theories predict for BEC collective modes:
- **Landau damping (Szepfalusy-Kondor / Giorgini):** γ_L ∝ T²/T_c² · ω_mode. Predicts specific Q(T) curves.
- **Beliaev damping:** γ_B ∝ ω_mode⁵/ε_F⁴ (negligible at low mode frequencies).

ED's prediction `Q ≈ 3.5 in D_E < 0.1 regime` needs to be distinct from Landau-damping-predicted Q at the same temperature. If both predict the same Q, the test is not distinguishing. **Explicit comparison of ED vs. Landau prediction at T* is required before claiming a retrodiction win.**

---

## 8. Honest framing

**What this scaffold achieves:**

1. Identifies optomechanical ring-down and BEC collective-mode decay as the structurally-correct temporal testbed for N_osc ≈ 9 and Q ≈ 3.5 — spatial-relaxation structure preserved, unlike SC-qubit 0-D case.
2. Maps candidate variables with explicit FORCED / CANDIDATE / SPECULATIVE classifications.
3. Identifies Jin 1997 as a uniquely suitable first dataset because it explicitly reports Q vs. T across a range spanning the ED target value.
4. Flags three new structural blockers (Q-formula inconsistency under ζ = 1/Q; typical-Q mismatch; non-homogeneous ρ_star for BEC).

**What this scaffold does not achieve:**

1. No data extracted; no retrodiction executed.
2. No derivation of ε_k / ζ that makes the Q-formula (1) yield physical D.
3. No verification that standard decoherence / Landau-damping theory does not also predict Q ≈ 3.5 at the same (T, mode) — i.e., no distinguishing-test baseline.

**Pattern-level observation:**

This is the fourth Phase-0-analog derivation attempt this session (matter-wave → SC qubit → optomechanics/BEC). Each has surfaced structural issues. The pattern is consistent: the ED program has strong internal consistency at the primitive level, strong internal consistency at the PDE level, but the bridges to specific experimental platforms are each missing at least one derivation step. **This is not a sign that the program is wrong; it is a sign that the primitive-to-platform bridges have been under-developed relative to the within-level structure.**

**The right framing for future sessions:** treat the platform-bridge derivations as the core Phase-2 work. Each platform (matter-wave, SC qubit, optomechanics, BEC) needs a dedicated `*_pde_mapping.md` memo that gives the ε_k / ζ / τ / D_E / ρ / v identifications uniquely for that platform. Only then can retrodiction attempts execute cleanly.

---

## 9. Cross-references

- SC-qubit scaffold (predecessor): [quantum/retrodictions/sc_qubit_scaffold.md](sc_qubit_scaffold.md)
- SC-qubit PDE mapping (Phase 0 that surfaced 0-D issue): [quantum/effective_theory/sc_qubit_pde_mapping.md](../effective_theory/sc_qubit_pde_mapping.md)
- Signature observable mapping: [quantum/effective_theory/signature_observable_mapping.md](../effective_theory/signature_observable_mapping.md)
- D-variable disambiguation: [quantum/effective_theory/d_variable_disambiguation.md](../effective_theory/d_variable_disambiguation.md)
- ζ derivation: [quantum/effective_theory/zeta_derivation.md](../effective_theory/zeta_derivation.md)
- PDE-parameter mapping: [quantum/effective_theory/pde_parameter_mapping.md](../effective_theory/pde_parameter_mapping.md)
- D_crit resolution (Q-formula source): [theory/D_crit_Resolution_Memo.md](../../theory/D_crit_Resolution_Memo.md)
- ED-Phys-17 (N_osc source): [archive/research_history/ED Physics/ED-Phys-17_OscillatorCosmology/ED-Phys-17_OscillatorCosmology.md](../../archive/research_history/ED%20Physics/ED-Phys-17_OscillatorCosmology/ED-Phys-17_OscillatorCosmology.md)

---

## 10. One-line summary

> **Optomechanical ring-down and BEC collective-mode decay preserve the spatial-relaxation structure required by ED-Phys-17's N_osc prediction — unlike 0-D SC qubits. Mapping candidates identified for ρ (mechanical displacement / condensate density), v (velocity / phase), τ (1/ω_m or 1/ω_c), and ζ (≈ 1/Q with spatial-mode correction). **Three structural blockers surfaced:** (1) naive ζ = 1/Q produces D > 1 in the Q-formula, so ζ requires a spatial-mode (ε_k) correction factor; (2) typical Q ranges in these platforms don't naturally include Q ≈ 3.5 — moderate-damping regimes are needed; (3) the BEC equilibrium is spatially non-homogeneous, requiring non-trivial PDE linearization. **Jin et al. 1997 (*PRL* 78, 764) "Temperature-dependent damping of BEC collective excitations" is the recommended first dataset** because it explicitly reports Q across a T range spanning the ED target value. Phase 0 (ε_k / ζ derivation for these platforms) is the prerequisite for Phase 1 (Jin 1997 retrodiction). This is the fourth Phase-0-analog attempt this session, all producing similar structural issues — suggesting the cross-level primitive-to-platform bridges are the core Phase-2 work.**
