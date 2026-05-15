# Paper U-ThinParticipation — Schrödinger Emergence in the Thin-Participation Limit

**Series:** Wave-3 U-Series (Phase-1 Schrödinger Program)
**Status:** Wave-3 generative paper; **M2 (Intermediate Path C)** verdict — substrate mechanism identified; constructive coarse-graining derivation OPEN
**Companions:** Paper_U3 (Schrödinger via Stone), Paper_U4 (Hamiltonian), Paper_073 (DCGT), Paper_089 (V1), Paper_006 (slot 6).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of the thin-participation limit's collapse to Schrödinger from nothing. Result is conditional on the 13 ED primitives (Paper_087) + declared paper-specific postulates.
2. It does **not** claim closed-proof reconstruction in the Hardy 2001 / CDP 2011 / Coecke-Kissinger operational-reconstruction sense. ED sits in the substrate-ontology lineage ('t Hooft cellular-automaton, Wolfram Ruliad, causal-set program), not the operational-reconstruction lineage.
3. It does **not** override Paper_095's three-tier verdict grammar. Verdict for this paper is stated in §1.
4. It does **not** claim closed derivation of V1 → unitary-time-translation coarse-graining — that derivation is OPEN. The V1-coarse-graining step is currently asserted via DCGT analogy, not constructed.
5. Thin-participation expansion is P-postulated (**P-ThinParticipation-Expansion**, §2.3); leading-order unitary form is FORCED in the regime; higher-order corrections and explicit construction of the small-$b_K$ expansion are OPEN.

---

## Abstract

This paper supplies the regime characterization for the Phase-1 QM-emergence program: in the **thin-participation limit** (low per-cell amplitude $b_K \ll 1$; weak inter-amplitude coupling; V1-dominated dynamics), substrate-level participation-measure dynamics collapse to the standard non-relativistic Schrödinger equation. The small-parameter expansion is declared as **P-ThinParticipation-Expansion** (§2.3); the V1 → unitary-time-translation coarse-graining step is currently asserted via DCGT analogy with constructive substrate derivation OPEN. The result is **compositional synthesis at M2, NOT closed-proof reconstruction**. Verdict: **M2 (Intermediate Path C)** per Paper_095's three-tier verdict grammar. Key falsifier **F2**: substrate evidence that V1-dominated DCGT does NOT produce unitary evolution refutes the regime-collapse mechanism.

---

## §1 Statement of Result

**Claim.** In the **thin-participation limit** — the substrate regime where:
- Participation density per substrate cell is low ($b_K \ll 1$ in normalization where $\sum_K b_K^2 = 1$),
- Inter-amplitude interactions are negligible (no significant multi-amplitude coupling),
- V1 kernel propagation dominates V5 cross-chain content,

the substrate-level participation-measure dynamics **collapse to the standard non-relativistic Schrödinger equation** (Paper_U3):
$$i\hbar \frac{\partial\Psi}{\partial t} = \hat H \Psi .$$

The thin-participation limit is the **natural emergence regime** for non-relativistic single-particle QM. Deviations from Schrödinger evolution appear when thin-participation fails (multi-particle interactions; high-amplitude regimes; V5-dominated open-system dynamics).

form-CONSISTENT in the thin-participation regime (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3). Specific corrections beyond thin-participation INHERITED via standard QFT / many-body theory.

Verdict: **M2 (Intermediate Path C)** — substrate mechanism identified; the V1 → unitary-time-translation coarse-graining is currently **asserted via DCGT analogy**, not constructed; the thin-participation small-parameter expansion is declared as P-ThinParticipation-Expansion (§2.3). Constructive substrate-derivation OPEN.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P04 (Bandwidth)** — supplies the participation-density scaling.
- **P10 (Rule-type primitive)** — V1 and V5 kernels.
- **P11 (Commitment-irreversibility)** — supplies V1 retardation.

### 2.2 Upstream Dependencies

- **I-U3:** Schrödinger equation via Stone's theorem.
- **I-U4:** Hamiltonian form $\hat T = \hat p^2/(2m)$.
- **I-U5:** Momentum operator.
- **I-073:** DCGT coarse-graining.
- **I-089:** V1 kernel structure.
- **I-090:** V5 cross-chain kernel.
- **I-006:** Unitary evolution from V1 (canonical slot 6).
- **I-RQM-T5:** Klein–Gordon non-relativistic limit.

### 2.3 Declared paper-specific postulates

- **P-ThinParticipation-Expansion:** Small-parameter expansion in $\epsilon \equiv b_K \ll 1$, with leading-order term yielding unitary evolution (Schrödinger form) and higher-order corrections OPEN. The expansion structure is declared; explicit substrate-level construction of the expansion (proof that the leading-order term recovers Stone-generated unitarity, and characterization of correction terms) is **OPEN**.

---

## §3 Derivation

### 3.1 The thin-participation regime

Define the **thin-participation regime** quantitatively:

- **Per-cell amplitude:** $b_K \ll 1$ (in normalized convention).
- **Inter-amplitude coupling:** $\langle\Psi_1|\hat V_{\mathrm{int}}|\Psi_2\rangle \ll \langle\hat H_0\rangle$ where $\hat V_{\mathrm{int}}$ is the inter-amplitude interaction and $\hat H_0$ is the free-particle Hamiltonian.
- **V5 vs V1 ratio:** V5 cross-chain bandwidth contributions to dynamics are negligible compared to V1 within-chain content.

This regime is the substrate-level analog of the standard QM "single-particle, weakly-interacting" regime.

### 3.2 Full substrate-level dynamics

In the **general** substrate regime, the participation-measure evolution is governed by:
- V1 kernel content (within-chain propagation, Paper_089).
- V5 kernel content (cross-chain correlations, Paper_090).
- Multi-amplitude inter-coupling (V5-modulated and higher-order corrections).
- DCGT coarse-graining (Paper_073).

The full substrate evolution is more complex than the standard Schrödinger equation: it includes open-system dissipation (Lindblad-class corrections, Paper_024), multi-particle interactions, V5-correlation effects, and substrate-cell discreteness corrections at scales near $\ell_P$.

### 3.3 Thin-participation collapse to Schrödinger

In the thin-participation regime:
1. **Low $b_K$** ensures linear superposition dominates: $\Psi = \sum_K P_K |K\rangle$ with $|P_K|^2 = b_K^2$ small per cell, so coherent superposition is preserved.
2. **Weak inter-amplitude coupling** ensures single-amplitude evolution dominates: the participation amplitude evolves independently of other amplitudes.
3. **V1-dominated dynamics** ensures retarded-kernel evolution: under DCGT (Paper_073), V1's contribution coarse-grains to the unitary one-parameter group of substrate time-translation.

By Paper_U3 (Stone's theorem applied to substrate time-translation), the V1-dominated unitary evolution produces:
$$i\hbar\frac{\partial\Psi}{\partial t} = \hat H \Psi .$$

The thin-participation limit therefore **collapses** the full substrate dynamics to the standard Schrödinger equation. The Hamiltonian $\hat H$ is the V1-kernel-derived time-translation generator (per Paper_U3 + Paper_U4 + Paper_U5).

### 3.4 Why thin-participation isolates the Schrödinger sector

The substrate's full dynamical content is rich — it includes:
- Closed-system unitary evolution (Schrödinger).
- Open-system dissipation (Lindblad, Paper_024 from V5).
- Measurement-induced state reduction (Paper_005).
- Multi-particle coupling and entanglement (Paper_063 et al.).

The thin-participation regime **filters out** the V5-correlation content, the open-system dissipation, and the multi-particle interactions, isolating the **closed-system single-particle unitary** content — exactly the Schrödinger regime.

Conceptually: Schrödinger is the substrate-level "vacuum-near-limit" of substrate-level QM dynamics. Other regimes (decoherence, measurement, many-body) require relaxing the thin-participation assumption.

### 3.5 Departures from thin-participation

Departures appear in:

**Decoherence regime:** When V5 cross-chain content is non-negligible (e.g., open-system coupling to environment), thin-participation fails on the V5-ratio condition. Dynamics include Lindblad-class corrections (Paper_024).

**Many-body regime:** When multi-particle inter-amplitude coupling is strong (e.g., interacting QFT, condensed-matter systems), thin-participation fails on the inter-coupling condition. Dynamics include explicit interaction terms.

**Strong-amplitude regime:** When $b_K \sim O(1)$ for multiple cells simultaneously (high-density participation), thin-participation fails on the per-cell amplitude condition. Substrate corrections beyond the Schrödinger form appear.

In each case, Schrödinger evolution is a **leading-order approximation** in the thin-participation expansion, with corrections supplied by the relaxed conditions.

### 3.6 Schrödinger emergence as canonical substrate-QM result

The thin-participation limit + the U-series derivations (U1 through U5) collectively constitute the **Phase-1 QM-emergence program**: a compositional synthesis at M2 level of standard QM as a regime of substrate dynamics.

The Phase-1 program is a **compositional synthesis at M2 level** (per Paper_U-FourPostulates §3.6), not a Hardy-class closed-proof reconstruction. The thin-participation limit is the **regime label** for the leading-order term in the small-parameter expansion declared as P-ThinParticipation-Expansion.

### 3.7 Numerical content

- Quantitative threshold defining "thin-participation" (e.g., $b_K^2 < 0.1$ or similar): INHERITED via empirical / canon-internal matching.
- Specific Hamiltonians per system: INHERITED.
- Schrödinger equation form in thin-participation regime: form-CONSISTENT.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P04, P10, P11 primitives | P | Primitives. |
| 2 | Full substrate dynamics under V1 + V5 + DCGT | I | Papers_073, 089, 090. |
| 3 | Thin-participation regime definition | P (regime) | Regime postulate. |
| 4 | Per-cell amplitude $b_K \ll 1$ | P-Thin | Regime condition. |
| 5 | Weak inter-amplitude coupling | P-Thin | Regime condition. |
| 6 | V5 cross-chain negligible | P-Thin | Regime condition. |
| 7 | Linear superposition dominates | D-via-I | From step 4. |
| 8 | Single-amplitude evolution | D-via-I | From step 5. |
| 9 | V1 coarse-grains to unitary time-translation | OPEN | Currently asserted via DCGT analogy; substrate construction OPEN. |
| 9b | P-ThinParticipation-Expansion (small-$b_K$ expansion structure) | P | Declared §2.3; explicit construction OPEN. |
| 10 | Stone's theorem application yields Schrödinger | I | Paper_U3. |
| 11 | Hamiltonian form $\hat H$ | I | Paper_U4. |
| 12 | $\hat p$ form | I | Paper_U5. |
| 13 | Thin-participation collapse to Schrödinger | D-via-I | Composition. |
| 14 | Departures (decoherence, many-body, strong-amplitude) | I | Papers_024, 005, etc. |
| 15 | Verdict M2 (Intermediate Path C — compositional synthesis; substrate construction OPEN) | A→position | Per Paper_095. |

---

## §5 Falsification Criteria

- **F1:** Empirical detection of Schrödinger evolution in a manifestly thick-participation regime — would refute the limit-regime identification.
- **F2:** Substrate evidence that V1-dominated DCGT does NOT produce unitary evolution — refutes step 9.
- **F3:** Thin-participation regime shown to fail to isolate single-amplitude dynamics — refutes step 7.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), **not** within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

This paper supplies the **regime characterization** for the Phase-1 QM-emergence program: thin-participation is the substrate-level regime in which standard non-relativistic Schrödinger QM emerges.

**Relationship to other ED papers:**
- **U-series (U1–U5):** structural ingredients (amplitudes, inner-products, evolution, Hamiltonian, momentum).
- **Paper_006:** V1 → unitary evolution canonical slot.
- **Paper_073 DCGT:** substrate-to-continuum bridge.
- **Paper_024 Lindblad:** the regime-departure paper (V5-driven decoherence).

**Numerical content INHERITED.** Specific thin-participation thresholds, Hamiltonians. **Form CONSISTENT.** Schrödinger emergence in thin-participation regime (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3).

Verdict: **M2 (Intermediate Path C)**.

---

**End Paper U-ThinParticipation.**
