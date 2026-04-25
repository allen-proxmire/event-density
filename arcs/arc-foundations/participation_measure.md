# QM Step 1 — The Participation Measure

**Date:** 2026-04-24
**Location:** `quantum/foundations/participation_measure.md`
**Status:** Provisional definition. Not final. Designed to unlock Steps 2–5 of the QM derivation (Schrödinger emergence, Born rule, Bell violations, uncertainty relations).
**Purpose:** Define a mathematical object — the **participation measure** — that (a) sits at the primitive level (Primitives 03 + 04 joined into a single quantitative object), (b) maps cleanly onto the identifications already committed in the platform-bridge work, and (c) is structured so that the four target QM phenomena emerge from specific limits or operations on it.

---

## 1. Starting point: what the primitives give us

From the primitive stack:

- **Primitive 03 (Participation):** the relation between micro-events when they integrate each other's becoming. Relational substrate. Not a scalar.
- **Primitive 04 (Participation bandwidth):** the graded scalar measure of how rich the participation relation is. `b_K(x, t) ∈ ℝ≥0` on channels K.
- **Primitive 07 (Channel):** stable rule-type-selective participation pathway. Discrete index K.
- **Primitive 09 (Tension polarity):** phase relation between a chain's rule and local flow direction. `π(K, x) ∈ S¹` per channel.
- **Primitive 11 (Commitment):** discrete event selecting one channel with weight `∝ b_K²` (Born-rule-like).

The primitives separately supply amplitude (bandwidth, real scalar) and phase (polarity, S¹-valued) information on channels. **They have not been combined into a single object.**

QM's wavefunction `ψ_K(x)` combines amplitude and phase into a single complex number per channel per position. This is the natural fusion of bandwidth and polarity.

---

## 2. The participation measure — definition

### 2.1 Core object

**The participation measure** `P` is a complex-valued distribution over channels and positions:

```
P_K(x, t) ∈ ℂ                                                (1)
```

indexed by channel K (discrete, per Primitive 07) and position x (continuous or discrete, depending on regime).

### 2.2 Decomposition into amplitude and phase

```
P_K(x, t) = √(b_K(x, t)) · e^{i · π(K, x, t)}                (2)
```

where:
- `b_K(x, t) = |P_K(x, t)|²` is the participation bandwidth in channel K (Primitive 04; real, non-negative).
- `π(K, x, t) = arg(P_K(x, t))` is the polarity phase of channel K (Primitive 09; S¹-valued).

**Status: CANDIDATE.** The decomposition (2) is the simplest complex-number fusion of the two primitive-level quantities; alternative fusions (e.g., quaternion-valued for more complex internal structure) are possible but not motivated by the current primitive stack.

### 2.3 Derived scalar quantities

- **Event density:** `ρ(x, t) = Σ_K |P_K(x, t)|² = Σ_K b_K` (Primitive 05; sum over channels gives the local ED count).
- **Effective multiplicity:** `M_eff(x, t) = (Σ_K |P_K|²)² / Σ_K |P_K|⁴` (Primitive 08; participation ratio).
- **Participation ratio D_P:** `D_P(x, t) = 1 / M_eff = Σ_K |P_K|⁴ / (Σ_K |P_K|²)²` (per `pde_parameter_mapping.md §4.1`).
- **Total participation amplitude (complex):** `Ψ(x, t) = Σ_K P_K(x, t)` — the coherent sum over channels. **This is the QM wavefunction in the thin-regime limit.**
- **Interference visibility:** `V(x, t) = |Ψ(x, t)|² / Σ_K |P_K|²` ∈ [0, 1]. Equals 1 when all channels are phase-aligned (fully coherent); equals 1/N when equidistributed with random phases.

### 2.4 Mathematical object type

`P_K(x, t)` is naturally viewed as a **section of a line bundle** over the product space (channel index × spacetime). Under a unitary channel-basis change `P_K' = Σ_K U_{K'K} · P_K`, the core object transforms covariantly.

In the thin regime where channels become a continuous label (e.g., momentum modes), `P_K(x, t) → P(k, x, t)` — a complex-valued field on phase space. Integration over k recovers `Ψ(x, t)` as the spacetime wavefunction.

**Status: CANDIDATE; SPECULATIVE for the bundle interpretation.** The sectionality is a natural geometric reading but is not forced.

---

## 3. Internal vs. external participation

From Primitive 04 §1's four-band partition `(b_int, b_adj, b_env, b_com)`, the participation measure admits a parallel decomposition:

```
P_K = P_K^{int} + P_K^{adj} + P_K^{env} + P_K^{com}         (3)
```

where each term carries amplitude and phase appropriate to its band.

### 3.1 Internal participation `P_K^{int}`

- Sustains the chain's own rule.
- Carries identity information (rule-type, polarity of the chain's own dynamics).
- Preserved under isolation (zero external coupling).
- For a single chain in vacuum: `P = P^{int}` alone.

### 3.2 Adjacency participation `P_K^{adj}`

- Couples to immediate participation-adjacent structure.
- Sets kinematic (position/momentum-like) coupling.
- Responsible for most of the "where is the chain" information.

### 3.3 Environmental participation `P_K^{env}`

- Couples to the broader bath.
- Carries the decoherence-relevant content.
- Typically phase-randomized (environmental average destroys coherence).

### 3.4 Commitment-reserve participation `P_K^{com}`

- Available for commitment events.
- Depletes as commitments consume it; replenishes from adjacency via flux-continuity (per `zeta_derivation.md`).

### 3.5 Constraint

Local total-bandwidth conservation (Primitive 04 §1):

```
Σ_K (|P_K^{int}|² + |P_K^{adj}|² + |P_K^{env}|² + |P_K^{com}|²) = b_total   (4)
```

constant along an isolated chain's persistence regime.

**Status: CANDIDATE.** The four-band partition of `P` inherits the four-band partition of bandwidth from Primitive 04.

---

## 4. Relations to other primitives

### 4.1 Bandwidth (Primitive 04)

Direct by construction: `b_K = |P_K|²`.

### 4.2 ED gradient (Primitive 06)

```
∇ρ = ∇(Σ_K |P_K|²) = Σ_K [P_K* ∇P_K + P_K ∇P_K*]           (5)
```

— a sum involving both amplitude and phase gradients of P_K. **The gradient of participation is richer than the gradient of bandwidth alone** — it contains phase-gradient information that bandwidth does not.

### 4.3 Multiplicity (Primitive 08)

```
M_eff = (Σ_K |P_K|²)² / Σ_K |P_K|⁴                          (6)
```

— real-valued, depends only on bandwidth (amplitudes), not on phases.

### 4.4 Commitment (Primitive 11)

A commitment event at position x selects channel K* with probability proportional to `|P_{K*}(x)|²` (the bandwidth in that channel). Post-commitment: `P_K → δ_{K, K*} · P_{K*}` (collapsed to single channel).

**Born rule structure:** `Prob(K* | commit at x) = |P_{K*}(x)|² / Σ_K |P_K(x)|²` — the normalized bandwidth. Squared-amplitude form natural because `|P_K|²` IS the amplitude-squared by definition (2).

### 4.5 Tension polarity (Primitive 09)

`arg(P_K) = π(K, x)` by (2). Polarity is the phase of the participation measure.

### 4.6 Relational timing (Primitive 13)

Phase differences between channels produce oscillatory coupling:

```
P_{K'}* · P_K = √(b_{K'} b_K) · e^{i(π_K − π_{K'})}          (7)
```

— the cross-channel bilinear carries the inter-channel phase, which is the relational-timing content.

---

## 5. Constraints from the four QM target phenomena

The participation measure must be structured so that the following four phenomena emerge correctly in the appropriate limits.

### 5.1 Schrödinger equation in the thin-participation limit

**Thin-participation regime:** `M_eff ≫ 1` (many channels, no single dominant channel), D_P small, chain distributed across many channels with coherent phases.

**Coherent sum:**

```
Ψ(x, t) = Σ_K P_K(x, t)                                     (8)
```

In the thin limit, the discrete channel sum becomes an integral over a continuous label (momentum, mode number, etc.). The coherent sum `Ψ(x, t)` is a complex-valued spacetime field — QM's wavefunction.

**Madelung decomposition:** writing `Ψ(x, t) = √(|Ψ|²) · e^{iS/ℏ}` recovers the density-phase form. The ED field equations (canonical PDE at D = 0 pure participation per `bec_pde_mapping.md §5.3`) must reduce to the Madelung form in the thin limit.

**Constraint on P:** evolution of `P_K` must produce a linear equation for `Ψ` in the thin limit. The simplest candidate:

```
iℏ ∂_t P_K = H_K · P_K + Σ_{K'} V_{KK'} · P_{K'}           (9)
```

— a Schrödinger-like equation for each channel amplitude, with intra-channel "free" Hamiltonian H_K and inter-channel coupling V_{KK'}. Summing over K gives an effective Schrödinger equation for Ψ.

**Status: CANDIDATE.** The exact derivation from ED primitives is Step 2 work. (9) is the form required.

**Subsidiary constraint:** the V_{KK'} coupling must be consistent with the bandwidth-composition rule committed in `visibility_to_bandwidth.md §1.2` (sublinear with exponent 2).

### 5.2 Born rule from forced participation (commitment)

**Commitment event:** environmental participation (b_env) grows rapidly, forcing individuation (Primitive 10). The chain collapses to a single channel K*.

**Probability of K*:** given the four-band structure, at commitment the environmental-phase randomization destroys coherence between channels, so the selection reduces to weighting by the channel's bandwidth:

```
Prob(K*) = b_{K*} / Σ_K b_K = |P_{K*}|² / Σ_K |P_K|²       (10)
```

**This is the Born rule.** The squared-amplitude form is automatic because (2) *defines* bandwidth as `|P|²`.

**Constraint on P:** (10) requires that phase information becomes irrelevant at commitment — this is the sublinear-composition rule applied in the environmental-decohering limit. For coherent composition (pre-commitment), phases matter; at commitment, they are averaged out and only amplitudes survive.

**Status: CANDIDATE, consistent with Primitive 11 §2.**

### 5.3 Bell-violating correlations from joint participation

**Joint participation:** for two subsystems A, B, the joint participation measure is:

```
P^{AB}_{K_A, K_B}(x_A, x_B, t) ∈ ℂ                           (11)
```

— indexed by channel of each subsystem and by each position.

**Factorizable case:** `P^{AB}_{K_A K_B}(x_A, x_B) = P^A_{K_A}(x_A) · P^B_{K_B}(x_B)` — product state, Bell inequalities satisfied.

**Non-factorizable case:** `P^{AB}` cannot be written as a product — entangled state. Bell inequalities can be violated up to the Tsirelson bound.

**Constraint on P:** the joint measure must admit non-product structure. Since (11) is a complex-valued function on the product space (channel_A × channel_B × x_A × x_B), non-factorizability is just non-product complex functions — no additional structural constraint needed. The complex structure admits Bell-violating correlations automatically.

**Tsirelson bound emergence:** the limit on Bell violations (CHSH ≤ 2√2) should emerge from the bandwidth-conservation constraint (4) applied to the joint system. Specifically: the total joint bandwidth is bounded, limiting how strongly non-factorizable the P can be.

**Status: CANDIDATE; SPECULATIVE on the Tsirelson-bound derivation** (requires explicit calculation in Step 4 work).

### 5.4 Uncertainty relations from orthogonal participation partitions

**Orthogonal partitions:** the four-band structure `{int, adj, env, com}` and subdivisions within each band (e.g., adjacency further decomposed into position-adjacency and momentum-adjacency) provide orthogonal partitions.

**Allocation inequality:** for two orthogonal partitions A, B drawing from a common bandwidth budget:

```
(Δb_A) · (Δb_B) ≥ K_{AB}                                    (12)
```

where K_{AB} is a structural constant of the partition topology.

**Heisenberg Δx · Δp ≥ ℏ/2 origin:** the adjacency band splits into position-adjacency (b_x) and momentum-adjacency (b_p) via Fourier-conjugate decomposition. Under the bandwidth-conservation constraint on the adjacency band, (12) applies with K_{xp} = ℏ/2 in the thick-regime limit.

**Constraint on P:** the decomposition into orthogonal partitions requires that the participation measure has a natural bilinear inner-product structure (for orthogonality to be defined). Complex-valued `P_K(x)` with sesquilinear inner product `⟨P|Q⟩ = Σ_K ∫ dx P_K*(x) Q_K(x)` provides this naturally — Hilbert-space structure emerges from the participation measure's defining properties.

**Status: CANDIDATE; consistent with Primitive 04 §5.4's four-band structural claim.**

---

## 6. Compatibility with platform-bridge identifications

### 6.1 Matter-wave (Eibenberger / Fein regime)

Under `visibility_to_bandwidth.md`: three-channel KDTLI scheme (path-1, path-2, env-commit). Participation measure:

```
P = (P_{path-1}, P_{path-2}, P_{env-commit})               (13)
```

Visibility V is the normalized coherent sum amplitude. `D_P = Σ|P_K|⁴ / (Σ|P_K|²)²` reproduces the participation-ratio formula. V_c ≈ 0.304 prediction carries through.

### 6.2 BEC (Jin 1997 regime)

Under `bec_pde_mapping.md`: ρ ↔ n, v ↔ φ. Continuous channel label (collective-mode index m). Participation measure:

```
P_m(x, t) = √n(x, t) · e^{iφ(x, t)} · u_m(x)                (14)
```

— the BEC wavefunction decomposed onto collective-mode eigenfunctions. Sum over m gives ψ_BEC = √n · e^{iφ}, matching the Madelung form.

### 6.3 SC qubit (0-D)

Under `sc_qubit_pde_mapping.md`: 0-D reduction. Two channels (|0⟩, |1⟩):

```
P = (P_0, P_1) = (α, β)                                     (15)
```

— the two qubit amplitudes. |P_0|² = P_0_population, |P_1|² = P_1_population. The 5 SPECULATIVE identifications from that memo become clearer: P is literally α|0⟩ + β|1⟩, the qubit state vector.

**Consistent across all three platforms.** The participation measure `P_K(x, t)` unifies matter-wave, BEC, and SC-qubit descriptions under one object.

---

## 7. What the measure is *not*

- **Not a scalar.** Scalar bandwidth `b_K` is extracted as `|P_K|²`; phase information is lost.
- **Not a probability distribution.** `|P_K|² / Σ|P_K|²` is a probability (Born rule), but `P_K` itself is the amplitude, not the probability.
- **Not a tensor** (in the multilinear-algebra sense) at the single-chain level; it is complex-vector-valued on the channel index. For multi-subsystem joint states, it becomes tensor-product-structured.
- **Not the ED field itself.** ρ(x, t) = Σ|P_K|² is the ED field (Primitive 05); P carries more information (phases + channel structure).

---

## 8. Constraints the measure must satisfy — consolidated

For the Schrödinger / Born / Bell / uncertainty-relation emergences to work, P must satisfy:

**C1. Complex-valuedness.** Amplitude + phase structure. Without phase, interference and Schrödinger fail.

**C2. Channel-indexed.** Enables Born rule via bandwidth ratios; enables multi-channel superposition structure.

**C3. Sesquilinear inner product.** Enables Hilbert-space structure, orthogonal partitions, uncertainty inequalities.

**C4. Sublinear composition (exponent 2).** `|P_1 + P_2|² = |P_1|² + |P_2|² + 2Re(P_1* P_2)` is the squared-amplitude composition. Committed in `visibility_to_bandwidth.md §1.2`.

**C5. Four-band decomposability.** `P = P^{int} + P^{adj} + P^{env} + P^{com}` with conservation (4).

**C6. Joint-measure non-factorizability.** For multi-subsystem participation, P^{AB} is a complex-valued function on the product space; non-product forms exist and admit Bell-violating correlations.

**C7. Thin-regime limit → Schrödinger.** Evolution (9) + Madelung decomposition gives the Schrödinger equation when channel sum becomes continuous and coherent.

**C8. Environmental-decohering limit → Born weights.** When b_env-randomization destroys inter-channel phases, the commitment-selection probability reduces to `|P_{K*}|² / Σ|P_K|²`.

**C9. Fourier-conjugate partition → Heisenberg.** Position-adjacency and momentum-adjacency decompose the adjacency band via Fourier-conjugate split; combined with conservation, gives Δx·Δp ≥ ℏ/2 in the thick limit.

All nine constraints are structurally consistent with the complex-valued definition (2) and the four-band decomposition (3).

---

## 9. What this provisional definition unlocks

This definition is **sufficient to begin Steps 2–5** of the QM derivation program:

- **Step 2 — Schrödinger emergence:** derive (9) from the ED primitives + PDE evolution. Show the thin-regime limit gives `iℏ ∂_t Ψ = H Ψ`.
- **Step 3 — Born rule derivation:** derive (10) from the commitment event structure (Primitive 11) + environmental phase-randomization (Primitive 04 §5.3).
- **Step 4 — Bell correlations:** compute maximal CHSH value under the joint-participation structure; check it hits 2√2.
- **Step 5 — Uncertainty relations:** derive Heisenberg from (12) applied to Fourier-conjugate partitions of the adjacency band.

Each is a dedicated derivation memo. The participation measure as defined here is the common scaffold.

---

## 10. Status classification summary

| Element | Status |
|---|---|
| Core object: complex-valued `P_K(x, t)` (eq. 2) | **CANDIDATE** |
| Amplitude-phase decomposition `P = √b · e^{iπ}` | CANDIDATE (natural fusion of Primitives 04 + 09) |
| Derived ρ = Σ\|P\|² matches Primitive 05 | FORCED (given the decomposition) |
| Derived M_eff, D_P match Primitive 08 formulas | FORCED |
| Four-band decomposition `P = P^{int} + P^{adj} + P^{env} + P^{com}` | CANDIDATE (parallels Primitive 04 §1) |
| C1–C9 constraints for QM target phenomena | **CANDIDATE** |
| Schrödinger emergence via (9) in thin limit | SPECULATIVE (requires Step 2 derivation) |
| Born rule via (10) at commitment | CANDIDATE (consistent with Primitive 11) |
| Bell violations via non-factorizable joint P | CANDIDATE (consistent with Primitive 03 §5.1) |
| Uncertainty via (12) | CANDIDATE (consistent with Primitive 04 §5.4) |
| Line-bundle / section interpretation | SPECULATIVE |

**Net status: provisional definition complete at CANDIDATE level for all core elements. Five SPECULATIVE or Step-2+ items remain to be closed through the explicit derivations.**

---

## 11. Honest framing

**What this memo achieves:**

1. Provisional definition of the participation measure `P_K(x, t)` as a complex-valued distribution over channels — fusing Primitive 04 (bandwidth) and Primitive 09 (polarity) into a single object.
2. Nine structural constraints (C1–C9) that the measure must satisfy for QM emergence.
3. Compatibility check against the three platform-bridge identifications (matter-wave, BEC, SC-qubit) — the measure specializes correctly in each case.
4. Infrastructure for Steps 2–5 of the QM derivation program.

**What it does not achieve:**

1. No derivation of the evolution equation (9) from ED primitives.
2. No explicit Schrödinger derivation; no explicit Born derivation; no explicit Bell or Heisenberg derivations.
3. No proof that the four-band decomposition (3) is unique.
4. No rigorous treatment of the continuous-channel-label limit (where K becomes a continuous index).

**These are Steps 2–5 tasks, not Step 1 tasks.** This memo establishes the object that those steps will operate on.

**Key structural claim:** the complex-valued `P_K(x, t)` is the natural mathematical object that makes ED's primitive structure compatible with QM's linear-algebra / Hilbert-space machinery. The participation measure IS the wavefunction in the thin-regime limit; at deeper regimes, the channel structure is explicit and discrete.

---

## 12. Cross-references

- Primitive 03 (participation relation): [`quantum/primitives/03_participation.md`](../primitives/03_participation.md)
- Primitive 04 (participation bandwidth): [`quantum/primitives/04_participation_bandwidth.md`](../primitives/04_participation_bandwidth.md)
- Primitive 07 (channel): [`quantum/primitives/07_channel.md`](../primitives/07_channel.md)
- Primitive 08 (multiplicity): [`quantum/primitives/08_multiplicity.md`](../primitives/08_multiplicity.md)
- Primitive 09 (tension polarity): [`quantum/primitives/09_tension_polarity.md`](../primitives/09_tension_polarity.md)
- Primitive 11 (commitment): [`quantum/primitives/11_commitment.md`](../primitives/11_commitment.md)
- Visibility → D (sublinear composition origin): [`quantum/effective_theory/visibility_to_bandwidth.md`](../effective_theory/visibility_to_bandwidth.md)
- D-variable disambiguation (D_P / D_E): [`quantum/effective_theory/d_variable_disambiguation.md`](../effective_theory/d_variable_disambiguation.md)
- BEC platform bridge (matches participation measure): [`quantum/effective_theory/bec_pde_mapping.md`](../effective_theory/bec_pde_mapping.md)
- SC-qubit platform bridge (matches participation measure): [`quantum/effective_theory/sc_qubit_pde_mapping.md`](../effective_theory/sc_qubit_pde_mapping.md)
- Dimensional Atlas Madelung anchoring: [`papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md`](../../papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md)

---

## 13. One-line summary

> **The participation measure P_K(x, t) = √(b_K) · e^{iπ_K} is a complex-valued distribution over channels and positions that fuses Primitive 04 (bandwidth) with Primitive 09 (polarity) into a single object. It reduces to ρ = Σ|P|² (Primitive 05), M_eff = (Σ|P|²)²/Σ|P|⁴ (Primitive 08), and acts as the QM wavefunction Ψ = Σ_K P_K in the thin-participation limit. Nine structural constraints (C1–C9) ensure Schrödinger, Born, Bell, and Heisenberg emerge from specific limits and operations. Compatible with the three completed platform-bridge identifications (matter-wave, BEC, SC-qubit). Provisional; unlocks QM Steps 2–5.**
