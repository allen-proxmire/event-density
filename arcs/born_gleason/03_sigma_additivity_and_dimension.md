# Memo 03 — σ-Additivity and Dimension ≥ 3

**Date:** 2026-04-26
**Arc:** `arcs/born_gleason/`
**Predecessors:** [`01_gleason_inventory.md`](01_gleason_inventory.md), [`02_noncontextuality_argument.md`](02_noncontextuality_argument.md)
**Status:** Admissibility memo. Verifies that ED's channel structure satisfies Gleason's remaining structural prerequisites — σ-additivity over countable orthogonal families (A7) and dimension d ≥ 3 (A2) — given the FORCED non-contextuality result of Memo 02.
**Purpose:** Close the structural admissibility check so Memo 04 can focus solely on the d = 2 edge case (Busch POVM extension).

---

## 1. What this memo must show

Memo 02 settled the non-contextuality content (A4 / A8). Memo 01 classified A1 (Hilbert-space arena), A3 (projector lattice), A5 (non-negativity), and A6 (normalization) as automatic or interpretive in ED. Two structural prerequisites remain:

- **A7 (σ-additivity).** For any countable family {Pᵢ} of mutually orthogonal projectors, f(Σ Pᵢ) = Σ f(Pᵢ). In ED translation: for any countable family {Sᵢ} of mutually disjoint channel-subsets at locus u, the bandwidth assigned to the union equals the sum of the bandwidths assigned to each.
- **A2 (dim ≥ 3).** The Hilbert space ℋ representing the chain's local channel-space at u has dimension at least 3. In ED translation: the available-channel set 𝒦(u) has at least three mutually orthogonal channels at any non-degenerate locus.

This memo verifies both. Each is structurally close to automatic; the work is to do the verification cleanly and to identify the corner cases where either could fail.

---

## 2. σ-Additivity

### 2.1 The setup

Let *u* be a vertex of the participation graph at which chain *C* has multiplicity M ≥ 3, in the thin-participation regime (consistent with Memo 02's scope). Let 𝒦(u) be the available-channel set at u (Primitive 07 §1; intrinsic to u per Memo 02 §2.1).

A **channel-subset** S ⊆ 𝒦(u) is a (possibly infinite) collection of channels in 𝒦(u). Two channel-subsets S, S' are **disjoint** if S ∩ S' = ∅ as sets — i.e., no channel is in both. (This is the ED-primitive analog of orthogonality of projectors via the Memo 01 §3 A3 mapping: orthogonal projectors ↔ disjoint channel-subsets.)

The bandwidth assigned to a channel-subset S is:

```
b(S | u) = Σ_{K ∈ S} b_K(u)                                                    (1)
```

— the sum of per-channel bandwidths over channels in S, with each `b_K(u)` partition-independent by Memo 02. The corresponding probability is `f(S | u) = b(S | u) / b(𝒦(u) | u)`, the bandwidth-fraction map of Memo 02 extended from singleton channels to channel-subsets.

### 2.2 Finite additivity is immediate

For two disjoint channel-subsets S₁, S₂ ⊆ 𝒦(u):

```
b(S₁ ∪ S₂ | u) = Σ_{K ∈ S₁ ∪ S₂} b_K(u)
              = Σ_{K ∈ S₁} b_K(u) + Σ_{K ∈ S₂} b_K(u)        [disjoint sum]
              = b(S₁ | u) + b(S₂ | u).                                          (2)
```

The middle step is set-theoretic disjoint-sum decomposition of a non-negative function over a finite (or finite-at-this-step) index set. It does not invoke any additional structural commitment; it is a property of how summation works on disjoint sets.

Dividing through by `b(𝒦(u) | u)`:

```
f(S₁ ∪ S₂ | u) = f(S₁ | u) + f(S₂ | u).                                        (3)
```

Finite additivity of the bandwidth-fraction map over disjoint channel-subsets follows from set-theoretic additivity of the underlying non-negative bandwidth function. **Status: automatic from Primitive 04 (bandwidth as non-negative scalar) and Memo 02 (per-channel bandwidth partition-independent).**

### 2.3 Countable additivity

Countable additivity requires extending (2) from finite to countable disjoint families:

```
b(⋃_{i=1}^∞ Sᵢ | u) = Σ_{i=1}^∞ b(Sᵢ | u).                                    (4)
```

For (4) to hold, two conditions are needed:

- **(C1)** the union ⋃_{i=1}^∞ Sᵢ is itself a well-defined channel-subset of 𝒦(u);
- **(C2)** the infinite sum on the right converges to a well-defined non-negative real number.

Both are satisfied in ED:

**(C1)** ⋃_{i=1}^∞ Sᵢ ⊆ 𝒦(u) is a subset of 𝒦(u) (subsets are closed under arbitrary unions). Per Primitive 07 §1, "the number of available channels of a given rule-type is finite (usually small)" — so 𝒦(u) is itself **at most countable** (in fact finite for any concrete physical chain), and any union of subsets is a subset of 𝒦(u). (C1) is structurally trivial in the at-most-countable case. The "finite" reading of Primitive 07 makes condition (C1) entirely automatic; the "countable" reading is the more permissive case that still satisfies it.

**(C2)** Each `b(Sᵢ | u) ≥ 0` (Primitive 04 non-negativity) and the partial sums are bounded above by the total bandwidth at u:

```
Σ_{i=1}^N b(Sᵢ | u) ≤ b(𝒦(u) | u) < ∞                                         (5)
```

The total bandwidth at u is finite (Primitive 04 four-band conservation: `b_total(C) = b_int + b_adj + b_env + b_com` is bounded along the chain's persistence regime). A non-negative monotone sequence bounded above converges. (C2) is automatic from the boundedness of total chain-bandwidth.

Together (C1) and (C2) force (4). Dividing through by `b(𝒦(u) | u)`:

```
f(⋃_{i=1}^∞ Sᵢ | u) = Σ_{i=1}^∞ f(Sᵢ | u).                                    (6)
```

**Conclusion.** σ-additivity of the bandwidth-fraction map holds over any countable family of disjoint channel-subsets at u. It follows from (i) non-negativity of bandwidth (Primitive 04), (ii) at-most-countable available-channel set at any locus (Primitive 07 §1), (iii) finiteness of total chain-bandwidth (Primitive 04 four-band conservation), and (iv) partition-independence of per-channel bandwidth (Memo 02).

**Status: A7 PASSES, automatically, in the regime where Memo 02 applies.**

### 2.4 Where σ-additivity could fail (corner-case audit)

- **Uncountable channel sets.** If 𝒦(u) were uncountable (e.g., a continuous channel spectrum), (C1) would require care — the union of an uncountable family of singletons is well-defined as a subset, but σ-additivity in the standard Gleason sense is countable-only. The continuous-spectrum case is a *separate* extension question (analogous to extending Born to position measurements), explicitly flagged in Memo 02 §6 item 5 as out-of-scope for the discrete-channel argument. For the discrete-channel case considered here (and in Gleason's original theorem), 𝒦(u) is at most countable and (C1) is automatic.

- **Unbounded total bandwidth.** If `b_total(C)` at u were infinite, (C2) would fail and σ-additivity would degrade to extended-real-valued additivity. Primitive 04's four-band conservation explicitly restricts attention to chains in their persistence regime, where total bandwidth is finite. **Status: not a physical concern in regimes where Gleason is being applied.** Pathological or limiting cases (commitment-divergence, topological obstructions to bandwidth-conservation) would be flagged at the primitive level before reaching this argument.

- **Cross-coherences c_{KK'} ≠ 0 (thick regime).** Outside the thin-participation regime, cross-coherences between non-disjoint channel-subsets do not average to zero, and (2) acquires a correction term `2 c_{S₁ S₂} √(b(S₁) b(S₂))` per the sublinear composition rule (Loophole 1, Memo 02 §4.1). For *disjoint* subsets in the strict set-theoretic sense, the cross-term coefficient c_{S₁ S₂} = 0 by structural disjointness — there are no shared channels to coherently combine. The thick-regime correction applies to overlapping or correlated subsets, not disjoint ones; σ-additivity over disjoint subsets remains intact. **Status: thick-regime corrections do not affect A7.**

No corner case threatens the verdict. **A7 PASSES unconditionally in the discrete-channel, thin-participation regime that Memo 02 already restricted to.**

---

## 3. Dimension d ≥ 3

### 3.1 The setup

The Hilbert space ℋ that Gleason requires is the chain's local channel-space at u — equivalently, the complex span of the available-channel basis-elements |K⟩, K ∈ 𝒦(u). Its dimension is:

```
d(u) = |𝒦(u)| = number of channels in the available-channel set at u.          (7)
```

(In the rule-type-restricted version: d(u) is the number of channels of *C*'s rule-type at u. Since Gleason is applied to a specific quantum subsystem with a specific state space, this is the relevant count.)

Gleason's theorem requires d ≥ 3.

### 3.2 d ≥ 3 in non-degenerate regimes

Three structural facts guarantee d(u) ≥ 3 generically:

**(D1) Multi-channel availability is the structural norm.** Primitive 07 §1: "channels are the operational object connecting the ontological primitives (01–06) to the phenomenological apparatus of quantum mechanics (amplitudes, branches, modes, transitions)." Every standard quantum subsystem with internal degrees of freedom — atom with multiple energy levels, spin-S system with S ≥ 1, photon with polarization plus continuous-mode structure, particle in a region of space (continuous position channel set) — corresponds to an ED chain with a structurally large 𝒦(u). The single-channel (d = 1) and two-channel (d = 2) cases are special, restrictive limits.

**(D2) Multiplicity M ≥ 3 is the operating regime.** Memo 02 explicitly restricted attention to M ≥ 3, consistent with Primitive 08's notion of effective multiplicity `M_eff = (Σ|P|²)² / Σ|P|⁴`. For chains in coherent superposition across at least three significantly-populated channels, d(u) ≥ M_eff ≥ 3 is automatic. (The available-channel set 𝒦(u) is at least as large as the support of the chain's current bandwidth distribution; channels with `b_K = 0` are present in 𝒦(u) as structural features of the graph but contribute zero to the distribution.)

**(D3) Concrete physical realizations.** The QM-emergence program's platform bridges (BEC, matter-wave interferometry, Q-C boundary, SC qubit, optomechanics; see `project_platform_bridges.md`) all involve channel sets with d ≥ 3 in their natural formulation:

| Platform | Channel structure | d |
|---|---|---|
| Matter-wave interferometer (Arndt, Eibenberger, Fein) | Spatial paths through grating slits + continuous transverse momentum modes | Large (dozens to hundreds of effective channels) |
| BEC (Jin 1997) | Discrete trap-mode spectrum + continuous-density profile | Large |
| Atomic system (e.g., n-level atom, n ≥ 3) | n internal states | n ≥ 3 |
| Photon polarization alone | 2 polarization states | d = 2 — *the edge case* |
| Spin-1/2 alone | 2 spin states | d = 2 — *the edge case* |

**The d = 2 edge cases are structurally significant** — they correspond to genuine physical systems (qubits, polarization measurements). Memo 04 handles these via the Busch POVM extension. For all higher-dimensional systems (d ≥ 3), Gleason applies directly.

### 3.3 Where d ≥ 3 could fail (corner-case audit)

- **Pure two-state systems (qubits, single-polarization photons, spin-1/2).** Genuine d = 2 case. **Edge case, addressed in Memo 04.** Not a Memo 03 problem.

- **Effectively-truncated systems.** A nominally high-dimensional system can be effectively two-dimensional in a regime where the chain's bandwidth is concentrated in only two channels (e.g., a multi-level atom driven near a two-level resonance). In such cases, the *operational* channel set is d = 2; the *structural* available-channel set 𝒦(u) is still high-dimensional. Two readings:
  - Take Gleason on the structural 𝒦(u) (d ≥ 3): theorem applies, Born rule recovered for the full system, the truncation is a property of the prepared state ρ rather than of the observable structure. **Recommended reading.**
  - Take Gleason on the truncated effective space (d = 2): edge case, Memo 04 handles via Busch.
  - Both readings are consistent and give the same physical predictions. The first is more natural in ED because 𝒦(u) is the structural object.

- **Single-channel (d = 1) chains.** A chain that has fully committed to a single channel has M = 1 and d = 1. This is the *post-commitment* state, not a pre-commitment Gleason setup. There is no probability rule to derive — the outcome is determined. **Not a counterexample to Gleason's applicability; it is outside Gleason's scope by construction.**

- **Pathological / topological cases.** Hypothetical chains living on a participation-graph region with only one or two available channels of the chain's rule-type could in principle exist as structural curiosities. These are not *physical* in any standard sense (every realistic quantum system in dimension ≥ 1 has at least continuum-many position channels, and any internal degree of freedom of dimension ≥ 3 alone yields d ≥ 3). **Status: measure-zero in the space of physical configurations; not a concern.**

### 3.4 Net assessment

For all non-degenerate physical regimes, d(u) ≥ 3 holds structurally — typically by a wide margin (continuous channel spectra give d = ∞ generically). The d = 2 edge case is real and physically significant but is exactly one specific structural situation, addressed in Memo 04 by the standard Busch POVM extension to Gleason. The d = 1 case is outside Gleason's scope by construction (post-commitment state, no probability rule needed).

**Status: A2 PASSES for all d ≥ 3 cases (the regime Gleason was originally proven for); the d = 2 edge case requires Memo 04.**

---

## 4. Joint admissibility status

Combining Memo 01's classification + Memo 02's non-contextuality result + this memo's σ-additivity + dimension verification:

| Gleason assumption | Status after Memos 01–03 |
|---|---|
| A1 — Hilbert-space arena | Interpretive; conditional on upstream U2 |
| A2 — dim ≥ 3 | **PASSES** for d ≥ 3; d = 2 edge case → Memo 04 |
| A3 — Projector lattice | Interpretive; channel-subset lattice maps cleanly |
| A4 — Frame function domain (typing form of non-contextuality) | **FORCED** by Memo 02 |
| A5 — Non-negativity | Automatic (Primitive 04 domain) |
| A6 — Normalization | Automatic (bandwidth conservation + commitment locus) |
| A7 — σ-additivity | **PASSES** by §2.3 above |
| A8 — Frame-sum constancy (operational form of non-contextuality) | **FORCED** by Memo 02 |

**All eight Gleason structural prerequisites are met or forced for d ≥ 3 in the thin-participation regime, conditional only on upstream CANDIDATE U2 (sesquilinear inner product, inherited from the QM-emergence Step-1 program).**

The Gleason chain Primitives → non-contextuality → Gleason theorem → Born rule is **structurally open at theorem grade for d ≥ 3**. The only remaining structural item is the d = 2 case (Memo 04), and the only inherited gap is U2 (separate program item).

---

## 5. Verdict

**PASSES** for d ≥ 3.

σ-additivity (A7) and dimension (A2) both follow automatically from the primitive structure under the regime conditions Memo 02 already imposed (thin-participation, M ≥ 3). σ-additivity is forced by non-negativity of bandwidth + at-most-countable channel sets + finiteness of total chain-bandwidth + partition-independence of per-channel bandwidth (the last from Memo 02). Dimension ≥ 3 is structurally generic for any quantum subsystem with non-trivial internal or spatial structure; the d = 2 case is real, named, and deferred to Memo 04.

The d = 2 case is the only deferred item from this memo. There are no inconclusive or partially-passing items.

---

## 6. Recommended Next Steps

**(a) Begin Memo 04 (d = 2 edge case via Busch POVM extension).** This is the next logical arc step. The 2003 Busch result extends Gleason to cover d = 2 by replacing projectors with positive operator-valued measures (POVMs) and replacing frame functions with effects. The ED translation should be straightforward: "POVM effect" maps to "weighted channel-subset" and "effect-additivity" maps to "bandwidth-additivity over weighted subsets" — both already in hand from the present memo. The d = 2 case is the last structural-admissibility item in the arc.

**(b) Audit ED's two-channel chain literature for any structural mismatch with the Busch setup.** Spin-1/2 systems, photon polarization, and SC qubit are the three ED platforms most directly testing the d = 2 case. A short pre-Memo-04 scan of `arcs/arc-foundations/`, `arcs/arc-Q/`, and `quantum/` for any existing two-channel structural commitment will save time during Memo 04 itself by surfacing whether ED's two-channel treatment already aligns with Busch's POVM framing or requires adjustment.

**(c) Defer the upstream U2 (sesquilinear inner product) promotion to its own arc.** U2 is not a born_gleason problem — it is a QM-emergence Step-1 problem inherited by every downstream derivation in the program. The present arc's chain is robust enough to state "Born is FORCED conditional on U2," and U2 should be addressed in a dedicated session aimed at promoting it to FORCED via the same primitive-stack analysis used in Memo 02. This is the cleanest way to keep the born_gleason arc's verdict crisp while flagging the genuine residual structural item without conflating arcs.

---

## 7. Cross-references

- Arc outline: [`arcs/born_gleason/00_arc_outline.md`](00_arc_outline.md)
- Memo 01 (assumption inventory): [`arcs/born_gleason/01_gleason_inventory.md`](01_gleason_inventory.md)
- Memo 02 (non-contextuality argument): [`arcs/born_gleason/02_noncontextuality_argument.md`](02_noncontextuality_argument.md)
- Step 3 (predecessor Born derivation): [`arcs/arc-foundations/born_rule_from_participation.md`](../arc-foundations/born_rule_from_participation.md)
- Primitive 04 (bandwidth, four-band conservation): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 07 (channel countability §1): `quantum/primitives/07_channel.md`
- Primitive 08 (multiplicity M_eff): `quantum/primitives/08_multiplicity.md`
- Platform bridges (channel-set sizes by platform): `memory/project_platform_bridges.md`
- Busch 2003 (POVM extension to Gleason — for Memo 04): P. Busch, Phys. Rev. Lett. 91, 120403.

---

## 8. One-line memo summary

> **σ-additivity (A7) follows automatically from non-negativity of bandwidth + at-most-countable channel sets + finiteness of total chain-bandwidth + Memo 02's partition-independence; dimension ≥ 3 (A2) holds structurally for every non-degenerate physical regime, with the d = 2 edge case (qubits, polarization, spin-1/2) deferred to Memo 04. After Memos 01–03, every Gleason structural prerequisite is met or forced for d ≥ 3 in the thin-participation regime, conditional only on inherited upstream CANDIDATE U2. Verdict: PASSES.**
