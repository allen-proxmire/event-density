# QM Step 4 — Bell Correlations from Joint Participation

**Date:** 2026-04-24
**Location:** `quantum/foundations/bell_correlations_from_participation.md`
**Status:** Step 4 derivation. Shows that the joint participation measure `P^{AB}_{K_A, K_B}(x_A, x_B, t)` produces Bell-inequality-violating correlations when non-factorizable (entangled). Classical LHV bound S ≤ 2 emerges from factorizable participation; the Tsirelson bound S ≤ 2√2 emerges from the sesquilinear inner-product structure + normalization constraint of the participation measure. **Bell violations are FORCED by non-factorizability; the Tsirelson bound is FORCED by constraint C3 (sesquilinear inner product) + bandwidth normalization.**
**Purpose:** Execute Step 4 of the QM-emergence program. Does not begin Step 5.

---

## 1. Starting material

### 1.1 The joint participation measure (Step 1 extension)

From `participation_measure.md §5.3` equation (11):

```
P^{AB}_{K_A, K_B}(x_A, x_B, t) ∈ ℂ                                             (1)
```

— complex-valued function indexed by channels of each subsystem and by each subsystem's position.

### 1.2 Factorizable case

```
P^{AB}_{K_A, K_B}(x_A, x_B, t) = P^A_{K_A}(x_A, t) · P^B_{K_B}(x_B, t)          (2)
```

— product structure. Corresponds to subsystem A's participation being independent of subsystem B's participation.

### 1.3 Non-factorizable case

```
P^{AB}_{K_A, K_B}(x_A, x_B, t) ≠ P^A_{K_A} · P^B_{K_B}                          (3)
```

— joint structure that cannot be decomposed into single-subsystem factors. Per Primitive 03 §5.1, this is the ED content of entanglement: shared participation structure across two or more endpoints.

### 1.4 Bandwidth conservation (extended to joint system)

```
Σ_{K_A, K_B} |P^{AB}_{K_A, K_B}|² = ⟨P^{AB}|P^{AB}⟩ = N = const                 (4)
```

— normalization of the joint participation measure. Sesquilinear inner product follows from constraint C3 of `participation_measure.md §8`.

---

## 2. The CHSH measurement scenario

### 2.1 Setup

Two spatially separated subsystems A and B, each with binary measurement outcomes. Standard CHSH settings:

- **A's measurement settings:** `a` or `a'` (two choices).
- **B's measurement settings:** `b` or `b'` (two choices).
- **Outcomes:** ±1 on each side.

For each setting pair `(a, b)`, one extracts the correlation function:

```
E(a, b) = Σ_{s_A, s_B = ±1} s_A · s_B · Prob(s_A, s_B | a, b)                   (5)
```

And forms the CHSH statistic:

```
S = E(a, b) + E(a, b') + E(a', b) − E(a', b')                                   (6)
```

### 2.2 Bell's theorem

- **Classical local hidden variable (LHV) theories:** `|S| ≤ 2` (CHSH inequality).
- **Standard QM:** `|S| ≤ 2√2` (Tsirelson bound), saturated by specific measurement-angle choices on maximally-entangled states.

**Task:** show that ED under factorizable participation gives `|S| ≤ 2`, and under non-factorizable participation can reach `|S| = 2√2`.

---

## 3. Commitment events on each subsystem

### 3.1 Measurement as commitment

Per Step 3 (`born_rule_from_participation.md §2`), a measurement on subsystem A is a commitment event: environmental participation `b_env^A` grows, phases randomize across A's channels, individuation forces single-channel outcome `K_A*`. Similarly for B.

### 3.2 Measurement-setting as channel-basis choice

The measurement setting `a` on A corresponds to a **choice of channel basis** for A's commitment. Different settings (a vs a') select different orthonormal bases of A's participation-channel space. Rotation between bases is a unitary transformation.

**Explicit form:** for a two-outcome measurement, setting `a` partitions A's channel index into two subsets `K_A^{(+1)}(a)` and `K_A^{(-1)}(a)` corresponding to outcomes ±1:

```
s_A(K_A, a) = +1  if K_A ∈ K_A^{(+1)}(a)
s_A(K_A, a) = -1  if K_A ∈ K_A^{(-1)}(a)                                        (7)
```

Different settings give different partitions — equivalently, different orthonormal channel bases.

**Status: CANDIDATE.** Identifying "measurement setting = channel basis" is standard in any Hilbert-space formulation; it is the natural ED analog.

### 3.3 Joint commitment

A commitment event occurs on A (selecting K_A*) and independently a commitment event occurs on B (selecting K_B*). Under the locality of commitments (per Primitive 11 §1 — commitment is local at a site), these are independent local events even when the underlying participation is non-factorizable.

**Critical observation:** commitment is local, but the participation structure being committed against is non-local when entangled. The outcomes K_A* and K_B* are statistically correlated through the joint `|P^{AB}|²` structure, even though the individual commitment events are local.

---

## 4. Joint outcome probabilities

### 4.1 Post-decoherence joint mixture

Extending Step 3's single-subsystem decoherence to the joint system: each subsystem's environmental coupling randomizes phases on its side. For independent environments:

```
P^{AB}_{K_A, K_B} → P^{AB}_{K_A, K_B} · e^{i δ^A_{K_A}} · e^{i δ^B_{K_B}}        (8)
```

where `δ^A_{K_A}` are A-environment random phases and `δ^B_{K_B}` are B-environment random phases, all independent.

### 4.2 Cross-terms destroyed by environmental averaging

Consider `|P^{AB}_{K_A, K_B}|²`:

```
|P^{AB}_{K_A, K_B}|² → |P^{AB}_{K_A, K_B}|² · |e^{iδ^A_{K_A}} · e^{iδ^B_{K_B}}|² = |P^{AB}_{K_A, K_B}|²
```

**The squared magnitude is invariant under phase randomization.** Only inter-channel cross-terms (involving `P^{AB}_{K_A, K_B} · (P^{AB}_{K_A', K_B'})*` for different index pairs) average to zero.

### 4.3 Joint probability formula

After environmental averaging on both sides, the joint probability is:

```
Prob(K_A*, K_B* | a, b) = |P^{AB}_{K_A*, K_B*}|² / Σ_{K_A, K_B} |P^{AB}_{K_A, K_B}|²    (9)
```

where the channel indices run over the bases selected by settings (a, b).

**Status: FORCED** given Step 3 Born derivation extended to two independent environments. The squared-amplitude form is inherited from the definition `b = |P|²`.

### 4.4 Non-factorizability implies non-factorizing probabilities

If P^{AB} is factorizable (eq. 2): `|P^{AB}|² = |P^A|² · |P^B|²`, so Prob(K_A, K_B) = Prob_A(K_A) · Prob_B(K_B) — uncorrelated outcomes.

If P^{AB} is non-factorizable (eq. 3): Prob(K_A, K_B) in general does NOT factorize. The outcomes are correlated in a way that cannot be attributed to local hidden variables.

---

## 5. Factorizable case: S ≤ 2

### 5.1 LHV theorem

For factorizable joint participation, the joint probability (9) reduces to products of single-subsystem probabilities. Each subsystem's outcome is determined (stochastically) by its own participation measure and its measurement setting, independently of the other side.

**Under factorizable P^{AB}:** outcomes can be modeled by local hidden variables — specifically, each side's measurement result is a function of:
- The local participation measure `P^A_{K_A}` (resp. `P^B_{K_B}`).
- The measurement setting on that side.
- Independent local randomness from environmental commitment.

This is precisely the structure Bell-CHSH inequalities are derived for. **The derivation of `|S| ≤ 2` for factorizable probabilities is standard and goes through identically for ED:**

```
For factorizable Prob(K_A, K_B | a, b) = Prob_A(K_A | a) · Prob_B(K_B | b):

S = E(a,b) + E(a,b') + E(a',b) − E(a',b')
  = ⟨s_A(a) s_B(b)⟩ + ⟨s_A(a) s_B(b')⟩ + ⟨s_A(a') s_B(b)⟩ − ⟨s_A(a') s_B(b')⟩
  = ⟨s_A(a) [s_B(b) + s_B(b')]⟩ + ⟨s_A(a') [s_B(b) − s_B(b')]⟩

|S| ≤ E[|s_B(b) + s_B(b')|] + E[|s_B(b) − s_B(b')|]                            (10)
```

For any realization of the local random variables: `|s_B(b) + s_B(b')| + |s_B(b) − s_B(b')| = 2` (since s_B ∈ {±1} and exactly one of the sum/difference is 2, the other is 0). Hence `|S| ≤ 2`.

**Status: FORCED** by factorizability + standard Bell-CHSH algebra.

### 5.2 Interpretation

Factorizable joint participation — product states — satisfy the CHSH inequality. No Bell violation, as expected. This matches the classical LHV bound and the QM prediction for product states.

---

## 6. Non-factorizable case: S can exceed 2

### 6.1 Entangled joint participation

For non-factorizable P^{AB}, the joint probability (9) cannot be written as a product. **The key structural feature:** the environmental phase-randomization on A destroys A-internal cross-terms, but the joint (A, B) cross-terms between `P^{AB}_{K_A, K_B}` and `P^{AB}_{K_A', K_B'}` include cases where only one index differs — and these survive or average to specific values depending on the joint structure.

### 6.2 Singlet-state participation measure

The prototypical entangled joint participation measure:

```
P^{AB}_{K_A, K_B} = (δ_{K_A, 0} δ_{K_B, 1} − δ_{K_A, 1} δ_{K_B, 0}) / √2        (11)
```

— the "singlet" configuration. Non-factorizable: cannot be written as `P^A ⊗ P^B`.

### 6.3 Measurement-setting observables

In a two-channel Hilbert space, measurement setting `a` corresponds to a Hermitian observable `σ_a = a · σ` where a is a unit vector on the Bloch sphere and σ is the vector of Pauli matrices. Eigenvalues ±1 correspond to the two outcome channels.

The correlation function for the singlet joint participation (11):

```
E(a, b) = ⟨P^{AB}| σ_a ⊗ σ_b |P^{AB}⟩ = −a · b                                 (12)
```

### 6.4 Tsirelson-saturating angle choice

Choose measurement angles (all unit vectors in the x-z plane):

- a = x̂
- a' = ẑ
- b = (x̂ + ẑ)/√2
- b' = (x̂ − ẑ)/√2

Compute:
- `a · b = 1/√2`, so `E(a,b) = -1/√2`
- `a · b' = 1/√2`, so `E(a,b') = -1/√2`
- `a' · b = 1/√2`, so `E(a',b) = -1/√2`
- `a' · b' = -1/√2`, so `E(a',b') = +1/√2`

```
S = E(a,b) + E(a,b') + E(a',b) − E(a',b')
  = -1/√2 + (-1/√2) + (-1/√2) − (+1/√2)
  = -4/√2
  = -2√2                                                                       (13)
```

Therefore `|S| = 2√2`.

### 6.5 Bell-violation achieved

**For the entangled singlet joint participation, |S| = 2√2 > 2. The CHSH inequality is violated.**

**Status: FORCED** given:
- Non-factorizable joint participation measure (11)
- Identification of measurement settings with Pauli observables
- Joint probability formula (9) from Step 3

**The CHSH violation is a direct consequence of the complex, non-factorizable structure of P^{AB}.** No additional postulate beyond what Step 1 already committed.

---

## 7. The Tsirelson bound

### 7.1 Statement

**For any joint participation measure P^{AB} satisfying the normalization (4) and the sesquilinear inner-product structure (constraint C3 of participation_measure.md §8), the CHSH statistic is bounded by |S| ≤ 2√2.**

### 7.2 Derivation (Landau-Khalfin 1987, reformulated in ED language)

Define the CHSH operator on the joint participation space:

```
Ŝ = σ_a ⊗ σ_b + σ_a ⊗ σ_{b'} + σ_{a'} ⊗ σ_b − σ_{a'} ⊗ σ_{b'}                  (14)
```

Compute `Ŝ²`:

```
Ŝ² = 4 · I_A ⊗ I_B + [σ_a, σ_{a'}] ⊗ [σ_b, σ_{b'}]                             (15)
```

(Using `σ_a² = I`, and cross-terms giving `[σ_a, σ_{a'}]` on A's side and `[σ_b, σ_{b'}]` on B's side.)

**Operator-norm bound:**

```
‖Ŝ²‖ ≤ 4 + ‖[σ_a, σ_{a'}]‖ · ‖[σ_b, σ_{b'}]‖                                    (16)
```

For Hermitian unit-norm observables (||σ|| = 1):
```
‖[σ_a, σ_{a'}]‖ ≤ 2 · ‖σ_a‖ · ‖σ_{a'}‖ = 2                                     (17)
```

Similarly `‖[σ_b, σ_{b'}]‖ ≤ 2`. Therefore:

```
‖Ŝ²‖ ≤ 4 + 2 · 2 = 8
‖Ŝ‖ ≤ √8 = 2√2                                                                 (18)
```

Since `|S| = |⟨P^{AB}|Ŝ|P^{AB}⟩| ≤ ‖Ŝ‖ · ‖P^{AB}‖²` and ‖P^{AB}‖² = 1 (normalization):

```
|S| ≤ 2√2                                                                      (19)
```

**Status: FORCED** given:
- Sesquilinear inner product on the joint participation space (C3)
- Normalization (4)
- Hermitian unit-norm observables (standard operator structure)

**The Tsirelson bound is inherited by ED from the Hilbert-space structure** — specifically, from constraint C3 of `participation_measure.md §8` requiring sesquilinear inner products on the participation manifold.

### 7.3 What constrains Tsirelson to 2√2

Three ingredients, all at the participation-measure level:

1. **Sesquilinear inner product** (C3 from participation_measure.md): gives the Hilbert-space structure on which Ŝ acts.
2. **Normalization of P^{AB}** (eq. 4): bandwidth conservation across the joint system, required for ⟨P^{AB}|P^{AB}⟩ = 1.
3. **Hermitian unit-norm observables**: measurement-setting channel-basis partitions (eq. 7) correspond to Hermitian ±1-outcome operators.

Under (1)–(3), the Landau-Khalfin algebra goes through. **No additional ED-specific constraint is needed** — the Tsirelson bound is a structural consequence of the participation-measure framework's Hilbert-space character.

---

## 8. Interpretation

### 8.1 Bell violation is non-locality of shared participation

Per Primitive 03 §5.1, entanglement is shared participation structure across two endpoints. The CHSH violation is the structural signature that this shared structure cannot be reduced to local variables on each side. ED does not postulate a non-local hidden variable or superluminal signaling — the non-factorizable joint participation measure is the primitive-level object from which the correlation arises, and commitment events are local (Primitive 11) but act on a non-local structure.

### 8.2 No superluminal signaling

Because commitment events are local and each side's marginal probability depends only on local settings:

```
Σ_{K_B} Prob(K_A, K_B | a, b) = Σ_{K_B} Prob(K_A, K_B | a, b')                  (20)
```

— the marginal on A is independent of B's setting. This is the standard "no-signaling" property; ED's framework preserves it because commitment events are local (Primitive 11).

**Status: FORCED** by Primitive 11's locality of commitment + bandwidth conservation.

### 8.3 The Tsirelson bound is saturation, not arbitrary

The value 2√2 is not a free parameter — it is determined by:
- The dimension of the local observable space (Pauli matrices → unit-norm Hermitian operators).
- The commutator structure ‖[σ, σ']‖ ≤ 2.
- The normalization of the joint state.

Any theory with the same Hilbert-space structure and the same observable-norm bounds will hit Tsirelson exactly. **ED inherits this bound; it does not derive a different bound.**

---

## 9. What this memo does and does not achieve

### 9.1 Achieved

1. **Derivation of Bell violations** from non-factorizable joint participation measures. CHSH can reach 2√2 for the singlet participation configuration.
2. **Classical LHV bound |S| ≤ 2** recovered for factorizable joint participation.
3. **Tsirelson bound |S| ≤ 2√2** derived from the sesquilinear inner product + normalization structure.
4. **Preservation of no-signaling** established via the locality of commitment events (Primitive 11).
5. **Identification of the structural constraint** enforcing Tsirelson: constraint C3 of `participation_measure.md §8` (sesquilinear inner product on the participation manifold).

### 9.2 Not achieved

1. **No ED-specific prediction beyond QM.** ED reproduces the standard Tsirelson bound; it does not predict a stronger or weaker bound. The Bell-violation derivation here is structurally equivalent to the standard QM derivation reformulated in participation-measure language.
2. **No derivation of the sesquilinear inner product from primitives.** Constraint C3 was stated in `participation_measure.md §8`; an explicit derivation from ED primitives (complex participation-measure + orthogonal-band structure → sesquilinear inner product as the natural bilinear form) is deferred.
3. **No treatment of PR-box correlations.** Post-quantum correlations (beyond Tsirelson but respecting no-signaling) are ruled out by the Hilbert-space structure but a more direct ED-primitive argument for why they don't appear would be an additional finding.
4. **No explicit singlet-state ED construction.** Equation (11) assumed the singlet form; deriving this specific non-factorizable configuration from primitive-level dynamics (how does a pair of particles get prepared into the singlet state?) is a separate derivation.

### 9.3 Honest framing

**ED reproduces the standard Bell / Tsirelson structure without modification.** The derivation is not ED-specific in the sense that ED does not give a different bound — it gives the same 2√2 as standard QM. What ED contributes is an alternative interpretation of where the correlations come from:

- Standard QM: "Correlations arise from entangled wavefunctions; their non-local structure is a feature of QM's linear algebra."
- **ED:** "Correlations arise from shared participation structure across endpoints (Primitive 03 §5.1). The Hilbert-space structure of the participation measure (constraint C3) inherits the Tsirelson bound."

The Hilbert-space formalism is the same in both; the interpretation of what the formalism represents differs. **Bell violations are FORCED in ED by the non-factorizability of joint participation measures; Tsirelson is FORCED by the inner-product + normalization structure.**

---

## 10. Status classification

| Derivation element | Status |
|---|---|
| Joint participation measure P^{AB} (eq. 1) | CANDIDATE (from Step 1) |
| Factorizable / non-factorizable distinction (eqs. 2–3) | FORCED by complex-valued function space |
| Normalization (eq. 4) | FORCED by bandwidth conservation extended to joint system |
| Measurement = commitment event per side | FORCED by Primitive 11 + Step 3 |
| Measurement setting = channel-basis choice (eq. 7) | CANDIDATE (standard identification) |
| Joint probability (eq. 9) after decoherence | FORCED by Step 3 Born derivation extended |
| LHV |S| ≤ 2 for factorizable | FORCED by standard Bell-CHSH algebra |
| Singlet participation configuration (eq. 11) | CANDIDATE (standard prototypical entangled state) |
| Correlation function E(a,b) = -a·b | FORCED for singlet (standard QM result) |
| Maximal violation |S| = 2√2 at Tsirelson angles | FORCED given singlet + standard measurement operators |
| Tsirelson bound |S| ≤ 2√2 for arbitrary joint state | FORCED by sesquilinear inner product + normalization + Landau-Khalfin algebra |
| Sesquilinear inner product (C3) | CANDIDATE (from participation_measure.md §8); requires derivation from ED primitives |
| No-signaling (eq. 20) | FORCED by Primitive 11 locality |

**Net: Bell violations and the Tsirelson bound are FORCED at the participation-measure level, conditional on three CANDIDATE identifications (joint-measure form, measurement-setting = basis, singlet prototype). The sesquilinear inner product (C3) is the one upstream CANDIDATE whose primitive-level derivation is deferred.**

---

## 11. Comparison with other Bell-derivation frameworks

- **Standard QM:** Bell violations follow from the linear-algebraic structure of entangled pure states; Tsirelson follows from operator-norm bounds.
- **Bohmian mechanics:** reproduces Bell correlations via non-local pilot wave; explicitly non-local hidden variables.
- **Many-Worlds:** Bell correlations are correlations between branching events; Tsirelson from standard Hilbert-space operator bounds.
- **ED (this memo):** Bell correlations arise from **non-factorizable joint participation structure**. The "shared participation" is an ED-primitive-level object; commitment events are local; correlations are structural properties of the joint participation measure. Tsirelson is inherited from the Hilbert-space structure (constraint C3).

**ED is closer to Many-Worlds in that it derives Bell from Hilbert-space structure without adding non-local hidden variables.** But unlike Many-Worlds, ED has a single-world commitment dynamics — the environmental phase-randomization + individuation produces single outcomes, not branching.

**ED is closer to Bohmian mechanics in that it treats the participation structure as "what's really there," including its non-local aspects** (joint participation cannot be localized to either subsystem). But unlike Bohmian mechanics, ED does not postulate particle positions; only commitment events at specific channels.

The novel contribution of ED for Bell: **a framework where non-local correlations are understood as shared participation structure (Primitive 03), commitments are local (Primitive 11), and the no-signaling property is structural rather than postulated.**

---

## 12. Cross-references

- Step 1 participation measure (joint form): [`quantum/foundations/participation_measure.md`](participation_measure.md) §5.3
- Step 2 Schrödinger emergence: [`quantum/foundations/schrodinger_emergence.md`](schrodinger_emergence.md)
- Step 3 Born rule derivation: [`quantum/foundations/born_rule_from_participation.md`](born_rule_from_participation.md)
- Primitive 03 (participation; entanglement as shared structure): [`quantum/primitives/03_participation.md`](../primitives/03_participation.md)
- Primitive 04 (bandwidth; four-band decomposition): [`quantum/primitives/04_participation_bandwidth.md`](../primitives/04_participation_bandwidth.md)
- Primitive 10 (individuation): [`quantum/primitives/10_individuation.md`](../primitives/10_individuation.md)
- Primitive 11 (commitment; locality of events): [`quantum/primitives/11_commitment.md`](../primitives/11_commitment.md)
- Classical references: Bell 1964 (*Physics* 1, 195); Clauser-Horne-Shimony-Holt 1969 (*PRL* 23, 880); Tsirelson 1980 (*Lett. Math. Phys.* 4, 93); Landau 1987 (*Phys. Lett. A* 120, 54).

---

## 13. One-line summary

> **Bell-inequality-violating correlations emerge as a structural consequence of non-factorizable joint participation measures P^{AB}_{K_A, K_B}(x_A, x_B, t). For factorizable (product) participation, the Bell-CHSH inequality |S| ≤ 2 is FORCED. For entangled joint participation (e.g., singlet configuration), CHSH reaches the Tsirelson bound |S| = 2√2 exactly, with this bound FORCED by (i) the sesquilinear inner product on the participation manifold (constraint C3 of Step 1), (ii) bandwidth-conservation normalization, and (iii) Hermitian unit-norm measurement-setting observables. No-signaling is preserved because commitment events are local (Primitive 11) even when the participation structure being committed against is non-local. ED reproduces the standard Bell/Tsirelson structure without modification — its contribution is the interpretation of non-local correlations as shared participation structure, not as a novel mathematical bound. One upstream CANDIDATE (sesquilinear inner product derivation from primitives) remains; all else is FORCED. Step 4 complete; Step 5 unblocked.**
