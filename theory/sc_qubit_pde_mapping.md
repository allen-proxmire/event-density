# SC-Qubit → ED PDE Mapping (Phase 0 of SC-qubit retrodiction)

**Date:** 2026-04-24
**Location:** `quantum/effective_theory/sc_qubit_pde_mapping.md`
**Status:** Phase 0 derivation memo. Maps superconducting-qubit Hamiltonian dynamics to the canonical ED PDE variables (ρ, v, D_E, ζ, τ). **Result: the mapping is viable under explicit assumptions but involves five SPECULATIVE identifications. Structural tension surfaces: the canonical ED PDE is a spatial (∇²-containing) equation, while a qubit is a 0-dimensional system.** The mapping "works" only after reducing the PDE to its 0-D limit, which changes what the predictions mean.
**Purpose:** Address the Phase 0 prerequisite identified in `sc_qubit_scaffold.md §6.1`. Honest derivation with explicit assumptions; no forcing of a match.

---

## 1. Starting material

### 1.1 The canonical ED PDE (FORCED)

From `theory/D_crit_Resolution_Memo.md §2`:

```
∂_t ρ = D · F[ρ] + H · v                                (1a)
∂_t v = (F[ρ] − ζ · v) / τ                              (1b)
F[ρ] = M(ρ) ∇²ρ + M'(ρ) |∇ρ|² − P(ρ)                  (1c)
D + H = 1, D, H ∈ [0, 1]                               (1d)
```

This is a **spatial** PDE. `∇²ρ` requires spatial structure; `M'(ρ)|∇ρ|²` likewise.

### 1.2 The SC qubit (FORCED)

Standard two-level system with rotating-frame Hamiltonian:

```
H_qubit = (ℏω_q / 2) σ_z                               (2)
```

plus drive terms and bath couplings. State space is ℂ² (two basis states |0⟩, |1⟩); density matrix is 2×2 complex; evolution via Lindblad master equation

```
dρ_q/dt = −(i/ℏ)[H, ρ_q] + L_1[ρ_q] + L_φ[ρ_q]        (3)
```

where L_1 contains T_1 energy relaxation and L_φ contains pure dephasing (T_φ). Observable dynamics include T_1 decay (`⟨σ_z⟩(t) → -1` exponentially with rate 1/T_1), T_2* dephasing (`⟨σ_x⟩(t) → 0` exponentially with rate 1/T_2), and driven or coupled oscillations (Rabi, vacuum-Rabi).

**Key dimensional parameters:** `ω_q` (qubit frequency, typically 2π × 5 GHz), `T_1` (energy relaxation, 50–200 μs), `T_2` (dephasing, 50–200 μs), coupling `g` to cavity modes (1–100 MHz), drive amplitude `Ω_R` (1–100 MHz), cavity loss `κ` (1 kHz – 10 MHz).

---

## 2. Structural issue: dimensional mismatch

The qubit is 0-dimensional (no spatial extent); the ED PDE is 1D or higher-dimensional. This must be addressed before any parameter correspondence is meaningful.

### 2.1 Option A: 0-D reduction of the PDE (adopted here)

Take the PDE at a single point, treating ρ and v as functions of time only. Spatial derivatives vanish:

```
∂_t ρ(t) = −D · P(ρ) + H · v                          (4a)
∂_t v(t) = (−P(ρ) − ζ · v) / τ                         (4b)
```

(The `M(ρ) ∇²ρ` and gradient terms drop at the point.)

**Status: CANDIDATE.** This is a reasonable reduction for a spatially-localized chain-complex (a qubit being exactly that — one well-localized participation site). The dynamics become purely penalty + participation coupled-ODEs.

**Consequence:** the PDE's mobility channel `M(ρ) ∇²ρ` is inactive; the qubit sees only the penalty channel + participation coupling. This narrows the parameter-space that applies to qubits.

### 2.2 Option B: embed qubit in its environment to recover spatial structure

The qubit lives in a participation graph containing the qubit itself + its cavity + the environmental bath modes. Spatial structure exists at the participation-graph level even if the qubit's "site" is a point.

**Status: SPECULATIVE.** Requires an explicit multi-site embedding and a derivation of how PDE variables map to graph-level quantities across qubit / cavity / bath. Substantial additional work.

### 2.3 Commitment

**This memo commits to Option A (0-D PDE).** Option B would produce a more complete mapping but is out of scope; flag for future Phase 2 work.

---

## 3. Identifying ρ and v in the qubit context

### 3.1 ρ ↔ qubit excited-state population (CANDIDATE)

**Proposal:**

```
ρ(t) = ⟨σ_+ σ_−⟩(t) = P_1(t) = ⟨1|ρ_q(t)|1⟩          (5)
```

— the probability of being in the excited state.

**Why this candidate:**

- ρ in the ED PDE is the count/density of accumulated micro-events (Primitive 05). For a qubit, the natural count of "commitment activity" at a site is the population in the non-ground state — excitations that represent committed participation events above the vacuum.
- Madelung anchoring (Dimensional Atlas): ρ ↔ |ψ|² in the quantum regime. For a qubit, `|ψ|² = (|α|², |β|²)`, with `|β|² = P_1` being the excited-state probability.
- Equilibrium at `ρ_star = 0.5`: for a balanced superposition, `P_1 = 0.5`. This matches the canonical ED equilibrium.

**Why SPECULATIVE-leaning:**

- Two other candidates compete: ρ ↔ ⟨σ_z⟩ (expectation value of Pauli z, ranging -1 to +1) or ρ ↔ coherence-magnitude `|ρ_{01}|`. Each maps to a different aspect of qubit dynamics.
- The "equilibrium at ρ_star" interpretation assumes thermal equilibrium is at `⟨σ_z⟩ = 0`, which is the high-temperature limit — not the true SC-qubit thermal state which is near `⟨σ_z⟩ = -1` at typical cryogenic conditions.

### 3.2 v ↔ qubit coherence (CANDIDATE)

**Proposal:**

```
v(t) = Im[ρ_{01}(t)]                                   (6)
```

(or its real part, or magnitude — the exact choice depends on phase convention).

**Why this candidate:**

- In `pde_parameter_mapping.md §5.4`, v is identified as "polarity-weighted commitment-rate density." For a qubit, the natural polarity-phase-carrier is the off-diagonal element of the density matrix ρ_{01}.
- Ramsey fringes in an SC qubit show `⟨σ_x⟩ = 2 Re[ρ_{01}] cos(δ t) + ...` — the coherence amplitude oscillates.
- The PDE (1b) has v driven by F[ρ] and damped at rate ζ/τ. Qubit coherence is driven by population dynamics (via Hamiltonian coupling) and damped at rate 1/T_2 — structurally similar.

**Why SPECULATIVE-leaning:**

- v is a real scalar in the PDE; ρ_{01} is complex. Taking Im, Re, or |ρ_{01}| as v is a choice.
- Lindblad dephasing acts on ρ_{01} directly, while ED's ζ acts on v via coupling to F[ρ]. The precise structural analogy requires careful matching.

### 3.3 Summary of field identification

| ED variable | Qubit observable | Status |
|---|---|---|
| ρ(t) | P_1(t) = ⟨1\|ρ_q\|1⟩ | CANDIDATE |
| v(t) | Im[ρ_{01}(t)] | CANDIDATE |
| ρ_star | 0.5 (high-T thermal / equal superposition) | CANDIDATE |
| F[ρ] | −P(ρ) at linear order near ρ_star | CANDIDATE (0-D reduction) |

---

## 4. Two-channel structure in the qubit context

The canonical ED PDE's D and H are weights for two evolution channels. For a qubit under the 0-D reduction:

### 4.1 Direct channel (weight D)

From (4a): `D · F[ρ] = −D · P(ρ)`. For P(ρ) = P_0(ρ − ρ_star) near equilibrium:

```
D channel: population dynamics from local penalty
  ↔  qubit T_1 decay (population relaxes toward equilibrium)
```

**Candidate identification:** D-channel dynamics at rate `D · P_0` ↔ qubit T_1 relaxation at rate `1/T_1`.

### 4.2 Participation channel (weight H)

From (4a): `H · v`. Coherence (v) drives population (ρ) change.

```
H channel: coherence-mediated population dynamics
  ↔  Hamiltonian coherent evolution (unitary) where population changes via coherence
```

For a driven qubit: drive amplitude Ω_R couples populations via coherence, producing Rabi oscillations. For a qubit-cavity coupled system: coupling g couples excitation exchange via shared coherence.

**Candidate identification:** H-channel dynamics ↔ coherent Hamiltonian evolution rate (Ω_R for driven, 2g for vacuum Rabi).

### 4.3 The D + H = 1 constraint

In the PDE, D + H = 1 is a normalization choice — the two channels share a fixed total weight. For a qubit:

- Pure Hamiltonian evolution (no dissipation): D = 0, H = 1. All dynamics via coherence.
- Pure dissipation (no coherent dynamics): D = 1, H = 0. All dynamics via population relaxation.
- Real qubit: D > 0 from Lindblad decay AND H > 0 from coherent Hamiltonian terms. The ratio depends on which dominates.

**Candidate formula:**

```
D/(D + H) = (1/T_1) / ((1/T_1) + Ω_R)                  (7)
```

— fraction of total dynamics-rate that comes from dissipation vs. coherent drive. For typical Ω_R ≫ 1/T_1 (strong drive): D → 0, H → 1. For free qubit with no drive: Ω_R → 0, D → 1.

**Status: CANDIDATE but convention-dependent.** The specific form of (7) assumes dissipation-rate and coherent-rate add linearly, which is approximate.

---

## 5. Derivation of ζ, τ, and D_E

### 5.1 ζ — participation damping

From `zeta_derivation.md §4.3`:

```
ζ = τ · α_env · Γ_com / b_com  =  τ / τ_com  ≈  Λ · τ    (8)
```

where Λ is the Hornberger-type decoherence rate and τ is the participation-relaxation timescale.

**For an SC qubit:**

- Λ ↔ 1/T_2 (dephasing rate) — the rate at which environmental coupling destroys coherence.
- τ ↔ ? (see §5.2 below for three candidates).

**Candidate ζ values (all SPECULATIVE pending τ identification):**

| τ candidate | τ value (transmon) | ζ = Λ · τ = τ/T_2 |
|---|---|---|
| 1/ω_q (qubit period) | ~3·10⁻¹¹ s | ~3·10⁻⁷ (extremely small) |
| 1/Ω_R (Rabi period) | ~10⁻⁷ s (at 10 MHz Rabi) | ~10⁻³ |
| T_1 (energy-relaxation time) | 10⁻⁴ s | ~1 (boundary) |
| Vacuum-Rabi period 1/(2g) | ~10⁻⁹ s (at 50 MHz g) | ~10⁻⁵ |

**Range: ζ ∈ [10⁻⁷, 1]** depending on τ identification. Covers the full range from tiny (analog of Arndt regime) to order-unity.

### 5.2 τ — participation relaxation timescale

**Three candidates:**

**Candidate τ-A: τ = 1/ω_q (qubit intrinsic period).** Natural for "rule-period" interpretation from `pde_parameter_mapping.md §4.3` where τ is the chain's internal rule-period. For transmon ω_q = 2π·5 GHz: τ ≈ 3·10⁻¹¹ s.

**Candidate τ-B: τ = 1/Ω_R (Rabi period) or 1/(2g) (vacuum-Rabi period).** Natural if "participation relaxation" refers to coherent-oscillation timescale. Typically τ ∈ [10⁻⁸, 10⁻⁷] s.

**Candidate τ-C: τ = T_1 (energy relaxation timescale).** Natural if "participation relaxation" refers to the system's overall return to equilibrium. τ ≈ 10⁻⁴ s for typical transmon.

**Each produces a different ζ (§5.1 table) and therefore a different D_crit(ζ).** The τ identification is the most consequential unresolved question in this mapping.

### 5.3 D_E — the PDE coupling weight

Given D_E in the two-channel PDE:

**Approach 1: match by Q (CANDIDATE).** From the D_crit memo linearization at `ε_k τ = 1`:

```
Q = √(1 − D(1 − ζ)) / (D + ζ)                         (9)
```

Setting Q = 3.5 (ED's predicted value):

- At ζ = 0.15: solving gives D ≈ 0.11
- At ζ = 0.2: D ≈ 0.09
- At ζ = 0.1: D ≈ 0.13

So **Q ≈ 3.5 corresponds to (D, ζ) ≈ (0.1, 0.17)** approximately, under `ε_k τ = 1` normalization.

**Implication:** the "D < 0.1, Q ≈ 3.5" pairing in the Q-C Boundary paper is internally consistent with the D_crit formula only if ζ ≈ 0.2, not ζ ≪ 1. This conflicts with the candidate `ζ = Λ·τ ≪ 1` for most τ identifications.

**Resolution candidates:**

- **Use τ = T_1** (§5.2 τ-C), giving ζ ~ 1 and different D_crit regime. But ζ ~ 1 is at the boundary of the PDE's damping regime, where D_crit → 1.
- **Find a τ identification giving ζ ∈ [0.1, 0.3]**, which points to a timescale in the 10⁻⁵ to 10⁻³ s range. This is between T_1 and 1/Ω_R. No obvious physical timescale in this range for a typical transmon.
- **The Q ≈ 3.5 regime is a specific PDE parameter combination that SC qubits do not naturally sit in.** Generic SC qubits have ζ ≪ 1 and therefore D_crit ≈ 0.828, producing oscillator Q ~ higher than 3.5.

**Status: the mapping is self-consistent in form but does not automatically place SC qubits in the Q ≈ 3.5 regime.** Additional derivation is required to determine what τ identification (if any) produces the right ζ.

**Approach 2: match by D_P via affine mapping (CANDIDATE).** From `d_variable_disambiguation.md §3.1` with N = 2:

```
D_E = 2 · D_P − 1                                      (10)
```

For a qubit with ρ = P_1 in the superposition state: D_P = P_1² + (1 − P_1)². At equal superposition (P_1 = 0.5): D_P = 0.5, D_E = 0. At P_1 = 0.7: D_P = 0.49 + 0.09 = 0.58, D_E = 0.16.

**Under this mapping, D_E < 0.1 requires P_1 ∈ (0.38, 0.62) — the balanced-superposition window.** A qubit in free evolution from equal-superposition spends time in this D_E < 0.1 regime during much of its dynamics.

**This is structurally informative: Approach 2 places the qubit in the N_osc ≈ 9 regime naturally during the coherent window.** Approach 1 raises a different constraint on ζ.

**Resolution:** the two approaches give different pictures. Honest reading: Approach 1 (Q-formula) and Approach 2 (D_P via affine) treat different aspects. Approach 1 asks "what PDE parameters produce Q = 3.5?" Approach 2 asks "what range of D_P is D_E < 0.1?" Both are needed; they agree in principle but the exact numbers differ because the PDE coupling weight D is not literally D_E (the affine mapping is a coarse-graining).

---

## 6. Mapping table

| ED PDE variable | SC-qubit observable / parameter | Status | Notes |
|---|---|---|---|
| ρ(t) | P_1(t) | CANDIDATE | excited-state population; alternative: ⟨σ_z⟩ |
| v(t) | Im[ρ_{01}(t)] | CANDIDATE | coherence-phase carrier; alternative: Re[ρ_{01}], \|ρ_{01}\| |
| ρ_star | 0.5 | CANDIDATE | equal superposition / high-T thermal |
| Spatial dimension | 0-D (single point) | ADOPTED (Option A) | M(ρ)∇²ρ channel inactive |
| D (PDE weight) | Dissipation fraction (T_1)/(T_1 + Ω_R·T_1) | CANDIDATE | formula (7) |
| H = 1 − D | Coherent-evolution fraction | CANDIDATE |
| D_E (underdamping-discriminant level) | See §5.3 — two candidate approaches | SPECULATIVE | Not determined uniquely |
| ζ | 1/T_2 · τ | SPECULATIVE | depends on τ identification |
| τ | 1/ω_q or 1/Ω_R or 1/(2g) or T_1 | SPECULATIVE | four candidates spanning 7 orders of magnitude |
| ε_k | 0 in 0-D (no spatial modes) | ADOPTED | consequence of Option A |
| Natural oscillation frequency ω | Ω_R (driven) or 2g (vacuum Rabi) | CANDIDATE | |
| Decay rate γ | (κ + 1/T_1)/2 (vacuum Rabi) or 1/T_Rabi (Rabi) | CANDIDATE | |
| Q_qubit = ω/(2γ) | 2g/(κ + 1/T_1) or Ω_R · T_Rabi/2 | FORCED (given identifications) | standard qubit quality factor |
| N_osc_observed | count of visible oscillation peaks in free-evolution trace | FORCED | standard extraction |

---

## 7. Open questions

### 7.1 τ identification

**The single most important unresolved question.** Four candidates span 7 orders of magnitude. The retrodiction target (Q ≈ 3.5, N_osc ≈ 9) depends sensitively on which τ is used.

**Needed:** a derivation from primitives + PDE structure that uniquely determines τ for a 0-D localized participation site (the qubit). Likely candidates:

- If τ corresponds to the chain's own rule-update rate, then τ = 1/ω_q (qubit frequency).
- If τ corresponds to participation-bandwidth redistribution, then τ might be an environmental-bath timescale closer to T_2.

### 7.2 ρ identification

Three candidates (P_1, ⟨σ_z⟩, |ρ_{01}|) for different aspects of qubit dynamics. The one that matches ED's ρ role should be determined by which produces ED-predicted N_osc behavior in observable traces.

### 7.3 0-D vs. spatially-embedded qubit

Option A (0-D reduction) loses the mobility channel M(ρ)∇²ρ entirely. This is a large simplification. If the ED-predicted N_osc specifically requires mobility-channel dynamics (not just penalty + participation), the 0-D reduction invalidates the prediction for SC qubits. Needed: check whether ED-Phys-17's peak-height-oscillation phenomenology survives at ε_k = 0.

### 7.4 Driven vs. free dynamics

ED's N_osc prediction is for free damped relaxation (ED-Phys-17 §4.1 baseline). SC-qubit data with clear oscillations usually involves driving (Rabi) or coupling (vacuum Rabi). Whether ED's prediction applies to driven oscillations at all is unclear — the PDE does not currently have driving terms.

**Implication:** vacuum-Rabi oscillations (coherent excitation exchange with a cavity, no external drive) may be the only strictly "free" observable that matches ED's setup. Driven Rabi oscillations would require PDE extension.

### 7.5 Lindblad structure vs. PDE dissipation

SC-qubit decoherence has two distinct contributions: T_1 (energy relaxation, amplitude damping) and T_φ (pure dephasing, phase damping). ED's PDE has ζ as a single participation-damping parameter. Whether ζ corresponds to T_1, T_2, or some combination (possibly `ζ ∝ 1/T_2 = 1/(2T_1) + 1/T_φ`) is unclear.

### 7.6 Equilibrium thermal-state issue

ρ_star = 0.5 (high-T thermal) does not match SC-qubit cryogenic equilibrium (near ⟨σ_z⟩ = -1, i.e., P_1 ≈ 0). This means the "equilibrium point" of the ED PDE is not the SC-qubit's equilibrium.

**Candidate resolution:** ED's ρ_star is a dynamical equilibrium of the ED field, not necessarily the thermal equilibrium of the mapped system. For the N_osc prediction, what matters is the point around which a prepared excited state relaxes — which for a qubit is the ground state, not equal superposition.

Alternatively: the "relaxation around ρ_star = 0.5" picture applies to qubit **coherences**, not populations. A prepared coherent superposition undergoes coherence decay toward ρ_01 = 0 (coherence equilibrium) with possible oscillations. This reframing may be more natural.

---

## 8. What this mapping achieves and does not achieve

### 8.1 Achieved

- Identified the structural tension between 0-D qubit and spatial ED PDE.
- Proposed (CANDIDATE) identifications for ρ, v, D, H, and the two-channel structure.
- Derived the Q-formula constraint: Q ≈ 3.5 corresponds to (D, ζ) ≈ (0.1, 0.17) under canonical normalization.
- Identified τ identification as the single most consequential open question.
- Produced an explicit mapping table with status classifications.

### 8.2 Not achieved

- No single determination of τ (four candidates remain).
- No derivation showing that ED's N_osc ≈ 9 applies to 0-D penalty + participation dynamics (the mobility channel is cut by Option A).
- No verification that the qubit's natural oscillation mode (Rabi, vacuum-Rabi, or free coherence decay) matches what ED's linearization describes.
- The thermal-equilibrium vs ρ_star discrepancy is flagged but not resolved.
- Driven dynamics (Rabi oscillations under continuous drive) are outside the current PDE scope.

### 8.3 Honest assessment

**The mapping is viable in form but heavily loaded with CANDIDATE and SPECULATIVE identifications.** Executing the Kirchmair 2013 retrodiction using this mapping would require adopting specific choices for each open parameter, which makes the retrodiction carry substantial disclosure cost.

**More importantly:** the structural mismatches flagged in §7 suggest that a 0-D qubit may not be the cleanest test of ED's N_osc prediction. ED-Phys-17's N_osc is for a **spatially-extended relaxing peak** in a 1D or 2D ED field. A 0-D qubit loses the spatial structure entirely. The prediction "8–19 peak-height oscillations" specifically counts maxima in `ρ(x_peak, t)` as the peak decays into its surrounding medium. A 0-D qubit has no surrounding medium.

**Implication:** SC qubits may not be the ideal platform for testing N_osc despite being the most data-rich temporal platform. **Optomechanical systems with spatially-extended mechanical modes, or BECs with collective-mode relaxation, may be more natural — they have the spatial structure ED's prediction was derived for.**

---

## 9. Revised recommendation

Based on this Phase 0 derivation attempt:

**9.1 Partial completion of the SC-qubit Phase 0.** The mapping is in form but not in closed analytic shape. Producing a clean Phase 1 retrodiction against Kirchmair 2013 would require additional disclosure of the SPECULATIVE choices (τ selection, ρ identification, v identification). A one-session retrodiction is not straightforwardly executable from this scaffold.

**9.2 Pivot consideration.** Optomechanical ring-down or BEC collective-mode decay data may be closer to ED's N_osc framework because they preserve the spatial-relaxation structure. Specifically:

- **Aspelmeyer-group optomechanical data:** mechanical modes have clear spatial structure; ring-down decay of a prepared coherent state is a direct analog of ED's peak relaxation.
- **BEC collective modes:** a density peak in a BEC undergoes oscillatory decay; some published datasets show multiple visible oscillations.

**9.3 Or: accept the disclosure cost.** Execute Phase 1 (Kirchmair 2013) with the SPECULATIVE mapping, disclose all assumption choices, and treat the comparison as a first-pass sanity check rather than a distinguishing retrodiction. Even a partial-match result would inform which SPECULATIVE choices are closer to correct.

**My suggestion:** given the pattern this session has shown (each Phase-0-analog step surfaces structural issues), **pivot to optomechanical data for the temporal-platform retrodiction test, where the spatial-relaxation structure is preserved.** SC-qubit testing remains available but requires further theory work before it becomes a clean first test.

---

## 10. Cross-references

- SC-qubit scaffold (prerequisite of): [quantum/retrodictions/sc_qubit_scaffold.md](../retrodictions/sc_qubit_scaffold.md)
- Signature observable mapping: [quantum/effective_theory/signature_observable_mapping.md](signature_observable_mapping.md)
- D-variable disambiguation: [quantum/effective_theory/d_variable_disambiguation.md](d_variable_disambiguation.md)
- ζ derivation: [quantum/effective_theory/zeta_derivation.md](zeta_derivation.md)
- PDE-parameter mapping: [quantum/effective_theory/pde_parameter_mapping.md](pde_parameter_mapping.md)
- D_crit resolution: [theory/D_crit_Resolution_Memo.md](../../theory/D_crit_Resolution_Memo.md)
- ED-Phys-17 (N_osc source): [archive/research_history/ED Physics/ED-Phys-17_OscillatorCosmology/ED-Phys-17_OscillatorCosmology.md](../../archive/research_history/ED%20Physics/ED-Phys-17_OscillatorCosmology/ED-Phys-17_OscillatorCosmology.md)
- ED-Phys-16 (oscillator structure): [archive/research_history/ED Physics/ED-Phys-16_CoupledOscillators/ED-Phys-16_CoupledOscillators.md](../../archive/research_history/ED%20Physics/ED-Phys-16_CoupledOscillators/ED-Phys-16_CoupledOscillators.md)

---

## 11. One-line summary

> **The SC-qubit → ED PDE mapping is viable in form but carries five SPECULATIVE identifications (ρ, v, τ, D_E, ζ) and a structural tension: the canonical ED PDE is spatial (∇²) while a qubit is 0-dimensional. Under the 0-D reduction, the mobility channel drops out; only the penalty + participation channels remain. The Q ≈ 3.5 target constrains (D, ζ) ≈ (0.1, 0.17), which does not automatically match the "ζ ≪ 1" expectation from Hornberger-rate reasoning. **The cleanest next step is a pivot to optomechanical ring-down or BEC collective-mode decay data, which preserve the spatial-relaxation structure that ED-Phys-17's N_osc prediction was derived for.** SC-qubit testing remains available but requires further theory work (τ identification, driven-PDE extension, thermal-equilibrium framing) before becoming a clean first temporal retrodiction.**
