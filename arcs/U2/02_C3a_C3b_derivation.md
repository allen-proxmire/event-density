# Memo 02 — Derivation of C3a (Linearity) and C3b (Conjugate-Bilinearity)

**Date:** 2026-04-26
**Arc:** `arcs/U2/`
**Predecessors:** [`00_arc_outline.md`](00_arc_outline.md), [`01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md)
**Status:** Derivation memo. Closes the linearity (C3a) and conjugate-bilinearity (C3b) sub-commitments of the U2 inner-product structure using only the primitive inputs identified in Memo 01.
**Purpose:** Settle C3a and C3b so Memo 03 can focus entirely on the load-bearing question of whether C3c's specific Σ_K ∫ form is FORCED.

---

## 1. What this memo must establish

From Memo 01 §1, U2 decomposes into:

- **C3a — Linearity.** The space of participation measures 𝒫 admits complex-vector-space structure under componentwise sum and complex-scalar multiplication.
- **C3b — Conjugate-bilinearity.** A pairing ⟨·|·⟩ : 𝒫 × 𝒫 → ℂ exists satisfying conjugate-linearity in the first slot, linearity in the second, conjugate symmetry, and positive-definiteness.

This memo derives both from primitives. Memo 01 classified C3a as AUTOMATIC and C3b as FORCED-with-derivation-needed; the work here is to make those classifications rigorous.

---

## 2. C3a — Linearity of 𝒫

### 2.1 Setup

The participation measure (Step 1 eq. †) is constructed as:

```
P_K(x, t) = √b_K(x, t) · e^{i π(K, x, t)}                                      (1)
```

with:
- `b_K(x, t) ∈ ℝ_{≥0}` from Primitive 04 (bandwidth as edge-weight on the participation graph; non-negative real).
- `π(K, x, t) ∈ [0, 2π)` from Primitive 09 (polarity as U(1)-valued phase).

The product √b_K · e^{iπ_K} is a complex number for each (K, x, t) tuple. The full participation measure is the array {P_K(x, t) : K ∈ 𝒦, x ∈ M, t ∈ ℝ}.

Let 𝒫 denote the space of all such arrays — i.e., functions P : 𝒦 × M × ℝ → ℂ. (Time-dependence will be suppressed in what follows; the analysis is at fixed t.)

### 2.2 The space 𝒫 is a complex vector space

**Claim.** 𝒫 admits componentwise sum and complex-scalar multiplication satisfying the standard complex-vector-space axioms.

**Proof.**

**(Sum.)** For P, Q ∈ 𝒫, define `(P + Q)_K(x) := P_K(x) + Q_K(x)`. Each P_K(x), Q_K(x) is a complex number, and the sum of two complex numbers is a complex number. Therefore (P + Q)_K(x) ∈ ℂ for every (K, x). Since 𝒫 is the set of *all* complex-valued functions on 𝒦 × M, the sum is in 𝒫 trivially.

**(Scalar multiplication.)** For α ∈ ℂ and P ∈ 𝒫, define `(α · P)_K(x) := α · P_K(x)`. The product of a complex scalar and a complex value is complex. Therefore (α · P)_K(x) ∈ ℂ, and α · P ∈ 𝒫.

**(Vector-space axioms.)** Componentwise sum and componentwise scalar multiplication on a function space valued in a field inherit all field axioms (associativity, commutativity, distributivity, identities, inverses) pointwise from the codomain. Since ℂ is a field, all standard complex-vector-space axioms hold for 𝒫. ∎

### 2.3 Closure remarks

- **Loophole L-loop-1 from Memo 01 §2.4** ("sums of participation measures may not themselves satisfy a normalization condition") is dispatched at this stage by distinguishing the **linear span** 𝒫 (on which the inner product lives) from the **physical-state subset** {P : ⟨P|P⟩ = 1} (the unit-norm rays). Hilbert-space construction operates on the span; physical interpretation operates on the unit subset. This is standard quantum-mechanical practice and is structurally identical to how a wavefunction `ψ` lives in the linear span of `L²` functions even though physical states are unit-norm.

- **Loophole L-loop-2 from Memo 01 §2.4** ("complex scalar multiplication may violate Primitive 04's bandwidth non-negativity") is dispatched by recognizing scalar multiplication as a *re-normalization*: P → α·P scales bandwidth by `|α|²`, which is itself non-negative. The unit-norm convention picks the physical normalization; α is a free re-scaling parameter on the linear span.

### 2.4 Status

**C3a is established. The participation-measure space 𝒫 is a complex vector space.**

This is essentially a verification that no primitive structure obstructs the standard complex-vector-space construction on a complex-valued function space. The construction (1) places each P-slot in ℂ; the field structure of ℂ supplies all the axioms; the physical-state distinction handles the normalization concern.

---

## 3. C3b — Conjugate-bilinearity (sesquilinearity)

### 3.1 What we need to derive

A pairing ⟨·|·⟩ : 𝒫 × 𝒫 → ℂ satisfying:

- **(S1) Conjugate-linearity in the first slot:** ⟨α P + β Q | R⟩ = α* ⟨P | R⟩ + β* ⟨Q | R⟩.
- **(S2) Linearity in the second slot:** ⟨R | α P + β Q⟩ = α ⟨R | P⟩ + β ⟨R | Q⟩.
- **(S3) Conjugate symmetry:** ⟨P | Q⟩ = ⟨Q | P⟩*.
- **(S4) Positive-definiteness:** ⟨P | P⟩ ≥ 0, with equality iff P = 0.

The derivation proceeds in three steps:
- **Step A.** Show that the pairing's diagonal `⟨P | P⟩` must equal a non-negative real that reduces to bandwidth on each (K, x) slot.
- **Step B.** Show that U(1) phase invariance eliminates complex-bilinear and real-bilinear alternatives, leaving only sesquilinear forms.
- **Step C.** Show that band-additivity (Primitive 04 §1.5) forces the off-diagonal pairing's specific (conjugate-linear, linear) slot structure.

### 3.2 Step A — Diagonal pairing equals bandwidth

**Premise (P4-norm).** Primitive 04 §2 establishes bandwidth as a non-negative real: `b_K(x) = |P_K(x)|² ≥ 0` (per construction (1) and the definitional relation `b = |P|²` from Step 1 §2).

The diagonal of any inner product on 𝒫 must produce, for each P, a number that:
- is a non-negative real (because it is supposed to represent a norm-squared, generalizing bandwidth);
- reduces to bandwidth on each (K, x) slot — otherwise the inner-product norm would not match the primitive-level bandwidth structure.

The pointwise (single-slot) requirement is:

```
[diagonal pairing on slot (K, x)] applied to P_K(x) = b_K(x) = |P_K(x)|².      (2)
```

For P_K(x) = a + ib ∈ ℂ, this requires `[diagonal](a + ib) = a² + b² = (a + ib)*(a + ib)`. Up to overall positive scaling, the unique pointwise function on ℂ satisfying this is the squared modulus, equivalent to the complex-conjugate product `P_K*(x) · P_K(x)`.

**Consequence:** the diagonal pairing must reduce on each slot to the complex-conjugate product. Aggregating over slots (with the channel- and position-measure questions deferred to Memo 03), the diagonal of the full inner product satisfies:

```
⟨P | P⟩ = [aggregation over (K, x)] of P_K*(x) · P_K(x) = [aggregation] of b_K(x).  (3)
```

**Status: positive-definiteness (S4) is forced** by Primitive 04 non-negativity + the construction (1) requirement that bandwidth be the diagonal norm-squared. The aggregation form (whether Σ_K, Σ_K ∫ dx, or other) is C3c material — deferred — but the *pointwise* diagonal structure is fixed.

### 3.3 Step B — U(1) invariance forces sesquilinearity

**Premise (P9-U(1)).** Primitive 09 §1.16 establishes polarity as a phase ("Polarity is not a binary in general — it is a phase in the full treatment"); §1.30 confirms it is U(1)-valued ("Not a scalar"). The participation-measure construction (1) has phase factor `e^{iπ_K(x)}`, which is U(1)-valued.

**Physical content of U(1) invariance.** The bandwidth `b_K(x) = |P_K(x)|²` is invariant under global phase rotation `P → e^{iα} P`:

```
|e^{iα} P_K(x)|² = e^{-iα} e^{iα} |P_K(x)|² = |P_K(x)|² = b_K(x).             (4)
```

This is the structural statement that *bandwidth does not depend on the absolute phase of the participation measure*. Bandwidth is the magnitude-squared; phase rotation does not change magnitudes.

The inner product must respect this — specifically, the diagonal `⟨P | P⟩` must be α-invariant under global rotation, since it equals an aggregation of bandwidths.

**Three candidate pairing types and how they respond to U(1) rotation:**

**(B-bilinear) Complex-bilinear pairing** β(P, Q) linear in both slots:

```
β(e^{iα} P, e^{iα} P) = e^{iα} · e^{iα} · β(P, P) = e^{2iα} · β(P, P).         (5)
```

For arbitrary α this is *not* equal to β(P, P) unless β(P, P) = 0. **Complex-bilinearity is incompatible with U(1) invariance of the diagonal — eliminated.**

**(B-real-bilinear) Real-bilinear pairing** β(P, Q) treating ℂ as ℝ² and bilinear over ℝ:

A general such pairing has the form (on a single slot):

```
β(z, w) = a Re(z) Re(w) + b Im(z) Im(w) + c Re(z) Im(w) + d Im(z) Re(w)        (6)
```

with a, b, c, d ∈ ℝ. For β(z, z) ≥ 0 to hold for all z ∈ ℂ, the quadratic form must be positive-semidefinite, which constrains a, b ≥ 0 and `4ab ≥ (c + d)²`.

Under z → e^{iα} z = (cos α · Re z − sin α · Im z) + i(sin α · Re z + cos α · Im z):

```
β(e^{iα} z, e^{iα} z) = (a cos²α + b sin²α + (c+d) sin α cos α) Re(z)²
                       + (a sin²α + b cos²α − (c+d) sin α cos α) Im(z)²
                       + (...) Re(z) Im(z).                                   (7)
```

For this to equal β(z, z) for *all* α and *all* z, the coefficients must match independently of α. Matching the Re(z)² coefficient: `a cos²α + b sin²α + (c+d) sin α cos α = a` for all α. Setting α = π/2: `b = a`. With a = b, the equation reduces to `a + (c+d) sin α cos α = a`, forcing `c + d = 0`. Similarly the Re(z) Im(z) coefficient forces `c − d = 0`, hence `c = d = 0`.

The U(1)-invariant real-bilinear form is therefore:

```
β(z, w) = a (Re(z) Re(w) + Im(z) Im(w)) = a · Re(z* w).                        (8)
```

**This is exactly the real part of the sesquilinear pairing z* w, scaled by a.** It is not a separate alternative — it is the real part of sesquilinearity. The imaginary part is missing, which means (8) cannot recover off-diagonal phase information that physical interference experiments require (e.g., interference of P + Q depends on `Re(P* Q)` AND `Im(P* Q)` jointly to encode the full relative phase). **Real-bilinearity that satisfies U(1) invariance reduces to the real-part of sesquilinearity and is therefore strictly weaker than sesquilinearity — it cannot encode all the physical content of the participation-measure framework.**

**(B-sesquilinear) Conjugate-bilinear (sesquilinear) pairing** ⟨P, Q⟩ conjugate-linear in first slot, linear in second:

```
⟨e^{iα} P | e^{iα} P⟩ = e^{-iα} · e^{iα} · ⟨P | P⟩ = ⟨P | P⟩.                  (9)
```

**Sesquilinearity is U(1)-invariant on the diagonal automatically** — and on the off-diagonal:

```
⟨e^{iα} P | e^{iα} Q⟩ = e^{-iα} · e^{iα} · ⟨P | Q⟩ = ⟨P | Q⟩.                  (10)
```

— *both diagonal and off-diagonal pairings are U(1)-invariant under global rotation*. This matches the physical content: global phase has no observable consequences, but relative phase does, and sesquilinearity preserves relative-phase information in the imaginary part of ⟨P | Q⟩.

**Conclusion of Step B.** Among the three candidate pairing types:

- Complex-bilinear: eliminated by U(1) invariance violation on the diagonal.
- Real-bilinear: U(1)-invariant version reduces to the real part of sesquilinearity, strictly weaker, cannot encode full physical content.
- Sesquilinear: U(1)-invariant on both diagonal and off-diagonal; preserves all relative-phase information.

**Sesquilinearity (S1) + (S2) is forced** by U(1) invariance of bandwidth + the requirement that the inner product encode full physical participation-measure content (including relative phases relevant to interference and to Steps 4–5 of the QM-emergence program).

### 3.4 Step C — Band additivity confirms slot-asymmetric linearity structure

**Premise (P4-band-additivity).** Primitive 04 §1.5 + Memo 03 of born_gleason §2 establish bandwidth additivity over orthogonal channel-subsets and (more broadly) over the four orthogonal bands. For two disjoint channel-subsets S₁, S₂:

```
b(S₁ ⊔ S₂) = b(S₁) + b(S₂).                                                   (11)
```

Translated to the inner product: for two participation measures P, Q with disjoint support (P_K(x) = 0 wherever Q_K(x) ≠ 0 and vice versa), the diagonal pairing of P + Q decomposes as:

```
⟨P + Q | P + Q⟩ = ⟨P | P⟩ + ⟨Q | Q⟩.                                          (12)
```

(The cross-terms ⟨P | Q⟩ + ⟨Q | P⟩ vanish because P_K*(x) Q_K(x) = 0 pointwise for disjoint-support P, Q.)

For (12) to follow from a pairing structure, the pairing must be *additive* in each slot (S1's "linearity in α + β" content for arbitrary scalar α, β, and S2's analogous content). Additivity in each slot, combined with Step B's U(1)-invariance constraint that picks sesquilinear over bilinear, yields:

- conjugate-linearity in first slot (S1 forced);
- linearity in second slot (S2 forced).

(The choice of which slot is conjugated is convention; physics is invariant under relabeling. The standard choice — conjugate-linear in the first, linear in the second — is the convention adopted in the QM-emergence Step-1 framework and inherited here.)

**Conjugate symmetry (S3)** follows automatically from (S1) + (S2) for sesquilinear forms:

```
⟨P | Q⟩* = (Σ over slots of P_K*(x) Q_K(x))* = Σ over slots of P_K(x) Q_K*(x) = ⟨Q | P⟩.   (13)
```

(Where Σ over slots is the C3c-deferred aggregation, but the structural relation holds independently of which aggregation is used.)

### 3.5 Joint conclusion of Steps A–C

All four sesquilinearity properties (S1)–(S4) are forced by primitive-level inputs:

| Property | Forced by |
|---|---|
| (S1) Conjugate-linearity (first slot) | P4 band-additivity (Step C) + P9 U(1) invariance (Step B) |
| (S2) Linearity (second slot) | P4 band-additivity (Step C) + P9 U(1) invariance (Step B) |
| (S3) Conjugate symmetry | (S1) + (S2) algebraic consequence |
| (S4) Positive-definiteness on diagonal | P4 non-negativity (Step A) + construction (1) diagonal-equals-bandwidth |

**C3b is FORCED by Primitives 04 + 09 + the participation-measure construction (1).**

The derivation does not introduce new structural commitments beyond those already present in the primitive stack. Specifically:
- It does not require the channel-sum measure (deferred to Memo 03);
- It does not require the position-integral measure (deferred to Memo 03);
- It does not require any non-local cross-slot terms (deferred to Memo 03);
- It does not require new symmetry assumptions beyond U(1) (which is already the explicit choice in Primitive 09).

### 3.6 Loophole audit (revisiting Memo 01 §3.4)

- **(F1 — non-sesquilinear bilinear pairing):** dispatched by Step B (Step B-bilinear and B-real-bilinear analysis). Complex-bilinear violates U(1) invariance; real-bilinear that satisfies U(1) reduces to the real part of sesquilinearity and is strictly weaker.
- **(F4 — non-U(1) phase symmetry):** Primitive 09 explicitly commits to U(1)-valued polarity. A future amendment to Primitive 09 introducing wider polarity symmetry (e.g., SU(2)-valued) would invalidate Step B and require redoing C3b under the new structure. **No current amendment is on the table.** The structural sensitivity is real and worth flagging for downstream work, but does not constitute a current loophole.

---

## 4. What this memo does and does not establish

### 4.1 Established

- **C3a (linearity of 𝒫):** automatic verification, no primitive obstacle.
- **C3b (conjugate-bilinearity / sesquilinearity):** FORCED via the joint action of Primitives 04 + 09 + construction (1) + four-band orthogonality. Both diagonal positive-definiteness and off-diagonal sesquilinear structure follow.

### 4.2 Not established (deferred to Memo 03)

The full specific form `⟨P | Q⟩ = Σ_K ∫ dx P_K*(x) Q_K(x)` requires three further sub-derivations, **all part of C3c** and explicitly out-of-scope here:

- **C3c-(i):** is the channel-aggregation measure counting-measure (Σ_K), or could it admit non-trivial weighting?
- **C3c-(ii):** is the position-aggregation measure the participation-graph vertex counting / emergent-manifold volume form, or could it admit non-Lebesgue alternatives?
- **C3c-(iii):** is the basic inner product strictly local on (K, x)-slots (no cross-slot mixing terms), or could it include genuine cross-slot contributions consistent with the four-band orthogonality?

**These are the load-bearing items of the U2 arc.** Memo 03 carries the load. Falsifiers F2 (alternative channel measure), F3 (alternative position measure), and F1′ (non-local cross-slot terms) all attach to C3c.

### 4.3 What Memo 02 does NOT touch

- **Hilbert-space completeness.** A Hilbert space requires not just a sesquilinear inner product but completeness in the induced norm topology. This is a measure-theoretic question separate from the algebraic structure derived here. Standard practice in QM-foundations is to take the L²-completion of the algebraic span; the same is implicit here, with completion handled in the standard mathematical-physics manner.

- **The choice of sign convention** (which slot is conjugated). Conventional in the QM-emergence Step-1 framework (first slot conjugated); inherited here. Physics is invariant under relabeling.

- **Multi-particle / tensor-product structure.** Bipartite and multi-subsystem inner products (relevant for Step 4 Bell/Tsirelson) are constructed by tensor-product extension of the single-particle structure. Standard mathematical construction; not a new structural commitment.

---

## 5. Joint structural status after Memos 01–02

| Sub-commitment | Status after Memo 02 |
|---|---|
| **C3a** Linearity | **AUTOMATIC** — verified §2 |
| **C3b** Conjugate-bilinearity | **FORCED** — derived §3 |
| **C3c-(i)** Channel measure | LOAD-BEARING (deferred to Memo 03) |
| **C3c-(ii)** Position measure | LOAD-BEARING (deferred to Memo 03) |
| **C3c-(iii)** Local pointwise pairing | LOAD-BEARING (deferred to Memo 03) |

**The arc's verdict now reduces entirely to Memo 03's treatment of C3c's three sub-features.** If all three close affirmatively, U2 is FORCED. If any closes with a non-pathological alternative, U2 is CONDITIONAL with a precise residual. If any closes with a consistent and physically distinct alternative, U2 is NOT FORCED.

---

## 6. Recommended Next Steps

**(a) Begin Memo 03 (C3c sub-features).** This is the natural next session step. Memo 03 is the load-bearing memo of the arc and should examine each of C3c-(i), (ii), (iii) against falsifiers F2, F3, F1′. Anticipated structure: one section per sub-feature, a falsifier audit per sub-feature, and a closing verdict identifying any residual.

**(b) Decide Memo 03's regime scope deliberately.** Memo 01 §8(c) flagged C3c-(ii)'s discrete-to-continuum lift via Primitive 12 thickening as the most likely sticking point. Two options for Memo 03: (a) restrict the U2-FORCED claim to the discrete (participation-graph vertex) regime where (ii) is structurally clean and defer the continuum lift to a follow-up arc; (b) include the continuum lift in Memo 03 by drawing on the Primitive 12 thickening machinery and the Phase-3 / acoustic-metric work. Choosing this scope before drafting will keep Memo 03 focused. *Recommended:* option (a) — produce a clean discrete-regime FORCED verdict, then a separate continuum follow-up. The discrete result is the load-bearing one; the continuum lift is technical scaffolding.

**(c) Note the Primitive 09 U(1) sensitivity for downstream work.** The FORCED status of C3b is conditional on Primitive 09's U(1)-valued polarity. If a future arc (e.g., on SM gauge group emergence or extended polarity structure) amends Primitive 09 to a wider symmetry, C3b would need to be re-derived under the new structure. This sensitivity is worth surfacing into the project memory record `project_qm_emergence_arc.md` so that any future Primitive-09 amendment work knows it has downstream consequences for U2.

---

## 7. Cross-references

- Arc outline: [`arcs/U2/00_arc_outline.md`](00_arc_outline.md)
- Memo 01 (decomposition + mapping): [`arcs/U2/01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md)
- Step 1 participation-measure framework (construction (1) source; constraint C3): [`arcs/arc-foundations/participation_measure.md`](../arc-foundations/participation_measure.md)
- Born_gleason Memo 03 (band-additivity over disjoint channel-subsets, source for Step C): [`arcs/born_gleason/03_sigma_additivity_and_dimension.md`](../born_gleason/03_sigma_additivity_and_dimension.md)
- Sibling upstream-CANDIDATE derivations (program standard): [`arcs/arc-foundations/u3_evolution_derivation.md`](../arc-foundations/u3_evolution_derivation.md), [`arcs/arc-foundations/u4_hamiltonian_form_derivation.md`](../arc-foundations/u4_hamiltonian_form_derivation.md), [`arcs/arc-foundations/u5_adjacency_partition_derivation.md`](../arc-foundations/u5_adjacency_partition_derivation.md)
- Primitive 04 (bandwidth non-negativity, four-band additivity): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 09 (polarity, U(1) phase): `quantum/primitives/09_tension_polarity.md`
- Primitive 12 (thickening, relevant for Memo 03's continuum question): `quantum/primitives/12_thickening.md`

---

## 8. One-line memo summary

> **C3a (linearity of the participation-measure space) is verified automatic — the construction P_K(x) = √b_K · e^{iπ_K} produces complex-valued slots, and complex-valued function spaces are closed under componentwise sum and complex-scalar multiplication. C3b (conjugate-bilinearity) is FORCED by three primitive inputs in concert: Primitive 04 non-negativity forces the diagonal pairing to equal the squared modulus; Primitive 09 U(1) invariance eliminates complex-bilinear and reduces real-bilinear to the strictly-weaker real part of sesquilinearity; Primitive 04 §1.5 band additivity over disjoint-support participation measures forces additivity in each slot. The arc's verdict now reduces entirely to Memo 03's treatment of C3c's three sub-features (channel measure, position measure, local pointwise pairing) against falsifiers F2, F3, F1′.**
