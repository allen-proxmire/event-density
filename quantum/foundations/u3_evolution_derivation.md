# U3 Derivation — Participation-Measure Evolution Equation

**Date:** 2026-04-24
**Location:** `quantum/foundations/u3_evolution_derivation.md`
**Status:** Tightening-program memo #2. Promotes U3 (the participation-measure evolution equation) from CANDIDATE to FORCED, modulo the numerical value of ℏ (which is inherited from the Dimensional Atlas). **Every structural feature of U3 is derived from primitives or from promoted identifications U1/U2: linearity, first-order-in-time, diagonal + off-diagonal operator decomposition, norm preservation, anti-Hermitian generator, and the factor `i` in front of ∂_t.** Only the dimensional value of ℏ remains inherited.
**Purpose:** Second target of the tightening program per `candidate_to_forced_program.md §5.2`. Step 2 Schrödinger emergence's structural form is now FORCED.

---

## 1. Statement of U3 and its role

### 1.1 The equation

```
iℏ ∂_t P_K(x, t) = H_K · P_K(x, t) + Σ_{K'} V_{KK'} · P_{K'}(x, t)              (U3)
```

— a linear first-order complex evolution for the participation measure `P_K(x, t)` on channel index K.

### 1.2 Role in the QM-emergence program

U3 is the structural backbone of Step 2. Without it, there is nothing to take the thin-limit of; Schrödinger cannot emerge.

**Six features of U3 that must be derived from primitives:**

1. **Linearity** in P_K — evolution preserves superposition.
2. **First-order in time** — single time derivative on the LHS.
3. **Operator decomposition** — right-hand side splits into diagonal H_K and off-diagonal V_{KK'}.
4. **Norm preservation** — bandwidth conservation.
5. **Complex coefficient structure** — the factor `i` in front of ∂_t is forced by anti-Hermicity.
6. **The numerical value of ℏ** — deferred to the ℏ-origin memo.

Features 1–5 are derivable from primitives + U1/U2 and are FORCED in this memo. Feature 6 is inherited.

### 1.3 What this memo achieves

- Derivation of features 1–5 from primitives.
- Explicit identification of ℏ as the sole inherited content.
- Promotion of U3 from CANDIDATE to **FORCED (modulo ℏ value)**.
- Cascade: Step 2's structural form becomes FORCED (modulo ℏ).

---

## 2. Derivation of linearity

### 2.1 Required: evolution must preserve superposition

**Premises (primitive-level):**

- **Primitive 03 (Participation):** participation is a relational substrate supporting shared / superposed structure. Two chain-complexes sharing participation produce a composite state (§5.1). Superposition of participation structures is intrinsic.
- **Primitive 07 (Channel):** channels recombine at apparatus junctions (beamsplitters, interferometer mergers). The recombination preserves coherent superposition.
- **Primitive 08 (Multiplicity):** in the thin regime (M_eff > 1), the chain is in a coherent superposition across channels. The coherent state evolves as a superposition and can be recombined at measurement.
- **U1 (promoted to FORCED in the previous memo):** P_K is complex-valued; superpositions `α P^A + β P^B` for complex α, β are valid participation states.

### 2.2 Superposition-preservation forces linearity

**Claim:** if P^A(t=0) evolves to P^A(t) and P^B(t=0) evolves to P^B(t) under the evolution rule F, then the superposition `α P^A(0) + β P^B(0)` must evolve to `α P^A(t) + β P^B(t)`.

**Proof (standard):** if F were non-linear, F(α P^A + β P^B) ≠ α F(P^A) + β F(P^B) in general. The superposition at time 0 would not evolve to the superposition at time t. Superposition would not be preserved — contradicting Primitive 08's coherent-state preservation in the thin regime.

**Formal statement:** the evolution operator E(t) satisfies `E(t)[α P^A + β P^B] = α E(t)[P^A] + β E(t)[P^B]`, which is the definition of linearity.

### 2.3 Alternative-exclusion argument

Could any non-linear evolution be consistent with primitives?

- **Born-rule consistency (per Step 3, `born_rule_from_participation.md`):** the Born rule `Prob = |P|² / Σ|P|²` is FORCED at commitment events. Between commitments, non-linear evolution would shift the `|P|²` structure in a way that breaks Born-rule predictions at later commitments. Specifically: non-linear evolution can create trajectory-dependence that breaks the probabilistic independence of separated commitment events. Primitives 10 + 11 (locality of individuation and commitment) forbid this.
- **Entanglement (per Step 4, `bell_correlations_from_participation.md`):** Bell correlations up to Tsirelson emerge from non-factorizable joint P^{AB}. Non-linear evolution of P^{AB} would generate new entanglement from unentangled initial states (Polchinski 1991; Gisin 1990 — non-linear Schrödinger equations permit faster-than-light signaling). Primitive 11 locality + no-signaling (per Step 4 §8.2) forbid this.

**Conclusion:** linearity is FORCED by (i) superposition preservation (Primitives 03, 07, 08, U1), (ii) Born-rule consistency at all commitment events (Primitive 11 + Step 3), (iii) no-signaling (Primitive 11 locality + Step 4).

**Status: FORCED.**

---

## 3. Derivation of first-order-in-time structure

### 3.1 Required: ∂_t P_K is single time-derivative

**Premises (primitive-level):**

- **Primitive 02 (Chain):** a chain is a sequence of micro-events held by a consistent update rule. The rule is applied *one step at a time* — each application advances the chain by one event. Between rule-applications, no state-update occurs.
- **Primitive 13 (Relational Timing):** time is the relational rhythm of commitment / rule-application events. The parameter `t` is the relational timing coordinate.

### 3.2 Markov-like property

**Claim:** the participation-measure state at time `t + dt` depends only on the state at time `t` (plus the infinitesimal interval dt).

**Argument:** Primitive 02's "single-step update rule" means each rule application depends only on the current state, not on past history. Applying the rule infinitesimally many times (in the continuous-time limit) produces an ODE of the form:

```
∂_t P_K(t) = F[P(t), K, t]                                                     (1)
```

where `F` is a function of the current P_K values but not of past values.

**Why not higher-order in time?** A second-order equation `∂²_t P = G[P, ∂_t P]` would require the evolution to depend on the rate-of-change of P — equivalently, on the recent past history of P. This violates Primitive 02's pure-current-state update rule: the rule takes the current state and produces the next state, without needing a derivative.

**Status: FORCED** by Primitive 02 + Primitive 13.

### 3.3 Interpretation in terms of commitment events

Primitive 11's commitment events are discrete state-transitions that occur at discrete times. Between commitments, the chain's participation evolves continuously according to the update rule. The continuous-time evolution is first-order because each moment's update depends only on the current state.

Higher-order evolution would require the chain to "remember" past velocity-of-change, which would require a secondary memory structure not in the primitive stack. Primitives 01–13 do not support such memory — commit events are discrete atoms; relational timing is a phase structure on commitments; no primitive supplies a "velocity of state" field.

---

## 4. Derivation of the operator form

### 4.1 Most general linear operator

Given linearity (§2), the evolution is:

```
∂_t P_K = Σ_{K'} L_{KK'}(x, t) · P_{K'}                                        (2)
```

for some linear operator kernel `L_{KK'}`. This is the most general linear action of a time-evolution operator on channel-indexed fields.

### 4.2 Diagonal / off-diagonal decomposition

Any linear operator on channel space admits the unique decomposition:

```
L_{KK'} = H_K · δ_{KK'} + V_{KK'}                                              (3)
```

where:
- `H_K = L_{KK}` is the diagonal part (on-diagonal entries).
- `V_{KK'} = L_{KK'}` for `K ≠ K'`, `V_{KK} = 0` (off-diagonal part).

This decomposition is algebraically forced: every matrix / operator decomposes uniquely into diagonal + off-diagonal parts.

**Substituting (3) into (2):**

```
∂_t P_K = H_K · P_K + Σ_{K' ≠ K} V_{KK'} · P_{K'}                              (4)
```

— the diagonal term acts on the same channel (H_K · P_K), and the off-diagonal term couples different channels (V_{KK'} · P_{K'}). This matches U3's structure.

### 4.3 Primitive-level interpretation

- **H_K (diagonal):** the chain's own update rule for channel K. Evolves the channel's participation without inter-channel coupling. This is the primitive-level content of Primitive 02's chain identity — each channel evolves by its own rule.
- **V_{KK'} (off-diagonal):** inter-channel participation coupling. Shares bandwidth between channels, producing interference, entanglement-generating coupling, and coherent transfer of participation. This is the primitive-level content of Primitive 04's adjacency band (b^{adj}).

**Status: FORCED** by linearity + standard linear-operator decomposition.

### 4.4 Compatibility with U2 inner product

U2 (now FORCED): sesquilinear inner product `⟨P|Q⟩ = Σ_K ∫ dx P_K* · Q_K`. Under this inner product, the operator L is represented by a matrix with entries `L_{KK'}`, and its adjoint `L†` has entries `(L†)_{KK'} = L_{K'K}*` (complex-conjugate transpose).

The decomposition (3) respects the inner-product structure: diagonal + off-diagonal is a natural matrix partition preserved under basis transformations.

---

## 5. Derivation of norm preservation and anti-Hermicity

### 5.1 Bandwidth conservation

**Premise:** Primitive 04 §1 states that total bandwidth of an isolated chain is approximately conserved in the chain's persistence regime. In the thin-regime limit (no commitment events, no environmental coupling — per Step 2 §2.6), this becomes strict conservation:

```
d/dt [Σ_K |P_K|²] = 0                                                          (5)
```

where Σ_K |P_K|² = total bandwidth of the chain (and equals the wavefunction's squared norm ‖Ψ‖² after Step 2 identification).

**Status: FORCED** by Primitive 04 in the isolated-chain thin-limit regime.

### 5.2 Expanding the conservation condition

Substitute (4) into (5):

```
d/dt Σ_K |P_K|²
  = Σ_K [(∂_t P_K*) · P_K + P_K* · (∂_t P_K)]
  = Σ_K [(Σ_{K'} L_{KK'}* P_{K'}*) · P_K + P_K* · (Σ_{K'} L_{KK'} P_{K'})]
  = Σ_{K, K'} [L_{KK'}* · P_{K'}* · P_K + P_K* · L_{KK'} · P_{K'}]             (6)
```

Relabel indices in the first term (K ↔ K'):

```
  = Σ_{K, K'} [L_{K'K}* · P_K* · P_{K'} + P_K* · L_{KK'} · P_{K'}]
  = Σ_{K, K'} P_K* · [L_{K'K}* + L_{KK'}] · P_{K'}                             (7)
```

For (5) to hold for arbitrary P:

```
L_{KK'} + L_{K'K}* = 0                                                          (8)
```

**This is the anti-Hermitian condition: L + L† = 0, or equivalently L = −L†.**

### 5.3 Anti-Hermitian generator → Schrödinger form

Any anti-Hermitian operator L can be written as `L = −i · H` where `H` is Hermitian (`H = H†`). This is a standard result: anti-Hermitian and Hermitian operators are related by multiplication by i, which flips the conjugation relation.

Substituting `L = −iH / ℏ_ED` (introducing the ED-natural time scale inside the coefficient, to be unpacked in §6):

```
∂_t P_K = −(i/ℏ_ED) · Σ_{K'} H_{KK'} · P_{K'}
```

Rearranging:

```
iℏ_ED · ∂_t P_K = Σ_{K'} H_{KK'} · P_{K'}                                      (9)
```

Decomposing H_{KK'} = H_K δ_{KK'} + V_{KK'}:

```
iℏ_ED · ∂_t P_K = H_K P_K + Σ_{K' ≠ K} V_{KK'} · P_{K'}                        (10)
```

**This is U3, with ℏ_ED in place of ℏ.**

### 5.4 Status

**Norm preservation is FORCED** by Primitive 04 bandwidth conservation in the isolated-chain thin-limit regime.

**Anti-Hermicity is FORCED** by norm preservation + the most-general-linear-operator form (§4).

**The factor `i` is FORCED** by anti-Hermicity (writing L = −iH makes H Hermitian).

**The ℏ_ED coefficient** is a dimensional constant converting between ED's natural time-scale and the SI-unit energy scale of H. Its value is inherited from the Dimensional Atlas (see §6).

---

## 6. The ℏ coefficient — inherited

### 6.1 What ℏ is in U3

The coefficient in front of ∂_t has units of [time × energy] = [action], i.e., ℏ is an action. In standard QM, ℏ = 1.054 × 10⁻³⁴ J·s.

In ED, the natural time-scale is the participation-relaxation timescale τ_ED (per `pde_parameter_mapping.md §4.3`). The Hamiltonian H has units of energy.

The dimensional relationship: `[ℏ_ED] = [τ_ED] · [H]`. If we set `[τ_ED] = [T_0]` (Dimensional Atlas characteristic time) and `[H] = [E_0]` (Dimensional Atlas characteristic energy), then `ℏ_ED = T_0 · E_0 = ℏ` in the quantum regime.

### 6.2 Derivation vs. inheritance

**The numerical value of ℏ (1.054 × 10⁻³⁴ J·s) is NOT derivable from ED primitives alone.** The primitives give dimensionless structural relations; numerical constants require an empirical anchoring.

**The Dimensional Atlas provides that anchoring** via the Madelung theorem (ED-Dimensional-01_Quantum_Regime §2.3): D_phys = ℏ/(2m). This is a mathematical identity of the free-particle Schrödinger equation, not an ED postulate.

**Under the Dimensional Atlas anchoring, the ℏ in U3 is the same ℏ in the Schrödinger equation, with no free parameter.** ED inherits ℏ from the Madelung structural anchor.

### 6.3 What the ℏ-origin memo would address

A future memo `quantum/foundations/hbar_origin.md` could attempt to derive ℏ's numerical value from more primitive structural constants of ED — for example, by relating ℏ to a ratio of participation-graph structural constants (bandwidth quantum × microevent count × etc.).

This is a deeper question than U3's derivation and is deferred as a separate research task.

**For U3's purposes:** the structural form of the equation is FORCED; the specific value of ℏ is inherited. This is a clean separation of what's primitive-derived vs. what's empirical-anchor.

---

## 7. Summary — U3 is FORCED (modulo ℏ)

### 7.1 Derivation table

| Feature | Status | Source |
|---|---|---|
| Linearity of evolution | **FORCED** | Primitives 03, 07, 08 + U1 + superposition preservation + Born consistency + no-signaling |
| First-order in time | **FORCED** | Primitives 02 + 13 (chain update-rule structure) |
| Operator form `L_{KK'}` | **FORCED** | Standard linear-operator structure |
| Diagonal + off-diagonal decomposition `H_K + V_{KK'}` | **FORCED** | Unique matrix decomposition |
| Norm preservation (unitarity) | **FORCED** | Primitive 04 bandwidth conservation in thin-limit |
| Anti-Hermitian generator `L = −iH` | **FORCED** | Norm preservation + linearity |
| Factor `i` in front of ∂_t | **FORCED** | Anti-Hermicity |
| Numerical value of ℏ | **INHERITED** | Dimensional Atlas (Madelung anchoring) |

### 7.2 Overall status

**U3 is FORCED modulo the inherited ℏ value.** Every structural feature of the evolution equation — linearity, first-order, operator decomposition, norm preservation, anti-Hermitian generator, the factor `i` — derives from primitives + promoted identifications (U1, U2).

The only content inherited from QM is the numerical value of ℏ, which is anchored via Madelung's theorem applied to the free-particle Schrödinger equation.

**Promotion: U3 → FORCED.**

---

## 8. Impact on the QM-emergence chain

### 8.1 Updated step statuses

| Step | Previous status | After this memo |
|---|---|---|
| 1 | **FORCED** (via U1) | **FORCED** |
| 2 | CANDIDATE (3 upstream: U3, U4) | **FORCED (modulo ℏ and U4)** |
| 3 | FORCED (1 CANDIDATE: phase-independence) | same |
| 4 | **FORCED** (via U2) | **FORCED** |
| 5 | FORCED (1 CANDIDATE: U5) | same |

### 8.2 Net gain from this memo

- **Step 2 structural form becomes FORCED.** The only remaining CANDIDATE in Step 2 is U4 (specific H_k form) plus the inherited ℏ value. Structurally, Schrödinger's form is now a primitive-level consequence.
- Three of five steps (1, 2 modulo U4 and ℏ, 4) are now FORCED. Only Step 2 (U4), Step 3 (phase-independence), and Step 5 (U5) retain CANDIDATE dependencies.

### 8.3 Outstanding CANDIDATEs

After this memo:
- **U4** (specific Hamiltonian form H_k = ℏ²k²/(2m) + V): CANDIDATE, hardest remaining.
- **U5** (adjacency-band conjugate partition): CANDIDATE, next target.
- **Phase-independence of environmental couplings (Step 3):** CANDIDATE.
- **ℏ numerical value:** inherited, documented as such.

---

## 9. Roadmap for completing the U3 program

### 9.1 Remaining within U3 itself

1. **ℏ origin memo.** Derive or anchor ℏ from primitive structural constants. Likely outcome: ℏ = function of participation-graph elementary constants × Madelung factor. Not strictly necessary for U3's structural promotion but closes the last inheritance.

2. **Extension beyond the thin limit.** U3 as derived here applies to the isolated-chain thin-limit (no commitment events, no environmental coupling). Outside this regime, Primitive 04's bandwidth conservation fails — environmental coupling bleeds bandwidth to the environment. The extended equation for non-isolated chains is a **Lindblad-master-equation-like structure**:

```
∂_t ρ̂ = -(i/ℏ) [H, ρ̂] + Σ_α L_α · ρ̂ · L_α† − (1/2){L_α†L_α, ρ̂}             (11)
```

where ρ̂ is the density-matrix representation and L_α are jump operators corresponding to environmental commitment events. **Deriving the Lindblad extension from primitives** is a natural next step that would complete U3 beyond the thin limit.

### 9.2 Integration with U4

U3 establishes the structural form `iℏ ∂_t P = Ĥ P` with Ĥ Hermitian. U4 (next tightening target) specifies Ĥ for specific physical systems — the free kinetic + potential form H = p²/(2m) + V.

**U3 does not determine H itself; it only determines the structural form of the evolution equation.** The specific H is a separate identification.

### 9.3 Remaining work in the tightening program

After this memo:

- **U5** (adjacency-band conjugate partition): one-session derivation, independent of U4.
- **U4** (Hamiltonian form + chain-mass derivation): hardest; estimated 2–3 sessions.
- **ℏ-origin memo:** 1 session; clarifies inheritance structure.

**Expected total: 4–5 additional sessions to complete the five-upstream-CANDIDATE tightening program.**

---

## 10. Honest framing

### 10.1 What this memo achieves

1. **U3 derivation** at FORCED-modulo-ℏ level.
2. **Step 2 structural form FORCED.** This was the program's weakest link (3 CANDIDATEs); now reduced to 1 CANDIDATE (U4) plus inherited ℏ.
3. **Explicit separation of primitive-derived content from empirical-anchor content.** The structural form of Schrödinger is now primitive-level; only the numerical constants are inherited.
4. **Cascade to Step 2:** Steps 1, 2 (modulo U4 + ℏ), and 4 are all FORCED after this memo. Steps 3 and 5 have minor residual CANDIDATEs.

### 10.2 What this memo does not achieve

1. **Does not derive ℏ from primitives.** Deferred to a separate memo.
2. **Does not derive the specific Hamiltonian form.** U4 is the next target.
3. **Does not extend beyond the thin-limit isolated-chain regime.** Lindblad extension is future work.
4. **Does not eliminate the Madelung-anchoring inheritance** from the Dimensional Atlas. That inheritance remains explicit.

### 10.3 Structural note on the inheritance

The `iℏ` factor is the one piece of U3 whose numerical value comes from outside ED's primitive structure. **This is a clean inheritance:** the structural form `i · ℏ · ∂_t P = H · P` is derived; only the dimensional constant ℏ requires empirical anchoring.

Every physical theory must at some point anchor its dimensional constants to empirical values. ED's choice is the minimal anchoring: ℏ, m (via chain-mass, to be derived in U4), and c (from Lorentz-invariance, scope not yet extended). Everything else follows from primitives.

**The tightening program's mature goal:** reduce the inheritance to the smallest possible list of dimensional constants, all of which have clear physical-measurement definitions. The structural content should all be primitive-derivable. U1, U2, U3 combined now meet this standard for Steps 1, 4, and 2 (structural form).

---

## 11. Status classification

| Claim | Status |
|---|---|
| Linearity of evolution | FORCED (§2) |
| First-order in time | FORCED (§3) |
| Standard linear operator decomposition | FORCED (§4) |
| Norm preservation in thin-limit | FORCED (§5.1) |
| Anti-Hermitian generator | FORCED (§5.2) |
| Factor `i` in ∂_t coefficient | FORCED (§5.3) |
| Numerical value of ℏ | INHERITED (§6) |
| U3 overall | **FORCED modulo ℏ value** |

**Promotion summary:** U3 moves from CANDIDATE to FORCED (with ℏ inherited). Step 2's structural form FORCED. The tightening program is advancing on schedule per `candidate_to_forced_program.md §5.5`.

---

## 12. Cross-references

### Program-level
- Tightening program master plan: [`quantum/foundations/candidate_to_forced_program.md`](candidate_to_forced_program.md)
- QM-emergence synthesis: [`quantum/foundations/qm_emergence_synthesis.md`](qm_emergence_synthesis.md)
- Step 1 (participation measure, U1 FORCED): [`quantum/foundations/participation_measure.md`](participation_measure.md)
- Step 2 (Schrödinger emergence): [`quantum/foundations/schrodinger_emergence.md`](schrodinger_emergence.md)
- Step 3 (Born rule): [`quantum/foundations/born_rule_from_participation.md`](born_rule_from_participation.md)
- Step 4 (Bell/Tsirelson, U2 FORCED): [`quantum/foundations/bell_correlations_from_participation.md`](bell_correlations_from_participation.md)

### Primitive stack
- [`quantum/primitives/02_chain.md`](../primitives/02_chain.md) (update rule → first-order-in-time)
- [`quantum/primitives/03_participation.md`](../primitives/03_participation.md) (superposition substrate)
- [`quantum/primitives/04_participation_bandwidth.md`](../primitives/04_participation_bandwidth.md) (bandwidth conservation → norm preservation)
- [`quantum/primitives/07_channel.md`](../primitives/07_channel.md) (channel recombination)
- [`quantum/primitives/08_multiplicity.md`](../primitives/08_multiplicity.md) (thin-regime multiplicity; coherent superposition)
- [`quantum/primitives/11_commitment.md`](../primitives/11_commitment.md) (commitment events; locality of individuation)
- [`quantum/primitives/13_relational_timing.md`](../primitives/13_relational_timing.md) (time as relational-commitment rhythm)

### External inheritance
- Dimensional Atlas (ℏ anchoring via Madelung): [`papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md`](../../papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md)
- Classical references: Polchinski 1991 (*PRL* 66, 397) on nonlinear QM / signaling; Gisin 1990 on nonlinear Schrödinger / signaling; Stone's theorem on unitary 1-parameter groups.

---

## 13. One-line summary

> **U3 (participation-measure evolution equation `iℏ ∂_t P_K = H_K P_K + Σ V_{KK'} P_{K'}`) is promoted from CANDIDATE to FORCED modulo the inherited numerical value of ℏ. Linearity (FORCED by Primitives 03+07+08+U1 + superposition preservation + Born/no-signaling consistency), first-order-in-time (FORCED by Primitives 02+13 chain-update-rule structure), operator decomposition into diagonal H_K + off-diagonal V_{KK'} (FORCED by standard linear-operator structure), norm preservation (FORCED by Primitive 04 bandwidth conservation in thin-limit isolated-chain regime), anti-Hermitian generator L = −iH (FORCED by norm preservation + linearity), and the factor `i` in front of ∂_t (FORCED by anti-Hermicity). Only the numerical value of ℏ is inherited from the Dimensional Atlas Madelung anchoring. Step 2's structural form is now FORCED; three of five QM-emergence steps (1, 2 modulo U4, 4) are now fully FORCED. Next targets in order: U5 (one session), U4 (harder, 2–3 sessions, requires chain-mass derivation), ℏ-origin memo (cross-cutting, 1 session).**
