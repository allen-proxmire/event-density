# Memo_ED_AdmissionFilter — Analysis of the Binary Chirality Admission Filter in the Post-SCBU Regime

**Series:** Wave-3 Construction Memo (Cosmology Arc; pre-baryogenesis prerequisite)
**Status:** Substrate-graph analysis of the candidate admission filter selecting $\chi_C \in \{0, \pi\}$ in the post-SCBU ignition regime. Follows directly from `Memo_ED_ChainArrowChirality.md` (row 14 OPEN). **Not a derivation of baryogenesis. Not a generative paper. No new primitives proposed.**
**Date:** 2026-05-15
**Anchors:** Paper_087 (primitives); Paper_072 (individuation regime); Paper_089 (V1 retarded kernel; T18 exclusivity of retarded support); Paper_090 (V5 cross-chain kernel); Paper_093 (T18 kernel-arrow of time); Papers SC-4.x; Paper_ED_CCC §3.7; Memo_ED_ChainArrowChirality (operational definition of $\chi_C$); Memo_ED_Baryogenesis_Scoping; Paper_095 (verdict grammar).
**Outcome (advance summary):** **The admission filter does not close at substrate-graph level from existing primitives.** Both candidate criteria (A and B) remain OPEN. The eventual baryogenesis paper will require either a focused substrate-graph extension or a paper-specific postulate (verdict downgrade M3 → M2).

---

## §1 Purpose and Inputs

The chirality memo defines, at D-via-I level:

$$\chi_C(e_n) := \pi_C(e_n) - \pi_K(\ell(e_n)) \pmod{2\pi}, \qquad \chi_C \in S^1,$$

with $\chi_C$ conserved along chains in the post-SCBU regime (globally-coherent kernel-arrow per Paper_ED_CCC §3.6 + §3.7 + SC-4.x). The chirality is therefore a chain-attached $S^1$-valued quantity in this regime.

ED-I-11's structural narrative requires a binary admission filter: only $\chi_C \in \{0, \pi\}$ admit Paper_072 individuation. This memo evaluates whether such a filter is derivable from existing substrate content.

Two candidate criteria are inherited from the chirality memo:

- **Criterion-A (structural):** scale-collapsed substrate supports only two distinguishable orientations; intermediate $\chi_C$ require local structure the substrate cannot supply.
- **Criterion-B (capacity):** intermediate $\chi_C$ require substrate slack absent in saturation; individuation fails for capacity reasons.

Both criteria are analyzed below.

---

## §2 Constraints from existing primitives in the post-SCBU regime

| Constraint | Source | Substrate-graph content |
|---|---|---|
| Kernel-arrow globally coherent | Paper_ED_CCC §3.6 + §3.7 + SC-4.x | $\pi_K(\ell)$ uniform across substrate up to global $U(1)$ choice. |
| Substrate homogeneous (no local curvature content) | Papers SC-4.x scale-collapse | No local content distinguishes substrate loci. |
| V1 is strictly retarded (advanced refuted by P11) | Paper_089 T18 | V1 has one propagation mode: forward-causal. No reverse-propagation mode. |
| P09 polarity is $U(1)$-valued (continuous) | Paper_087 §5.9 | P09 admits continuous $S^1$ phase values; no native discrete structure. |
| P11 commitment-irreversibility supplies binary directed events | Paper_087 §5.11 | Each event has unique forward direction; chain-arrow $\sigma_C$ inherits this. |
| Paper_072 individuation requires chain-identity preservation under V1/V5 | Paper_072 | Admission criterion = identity-preservability. |

**Key observation:** the existing substrate content includes one binary structure (P11 directed events) and one continuous structure (P09 $U(1)$ polarity). The chirality $\chi_C$ as currently defined inherits the continuous structure via P09. The binary admission filter $\chi_C \in \{0, \pi\}$ requires either (i) reformulating chirality natively from the P11 binary structure, or (ii) deriving a substrate constraint that restricts P09 continuous values to two discrete values in the post-SCBU regime. Neither (i) nor (ii) is currently constructed.

---

## §3 Analysis of Criterion-A (structural-orientation)

**Statement of Criterion-A:** In the post-SCBU regime with globally-coherent kernel-arrow, the substrate supports only two distinguishable orientations relative to the kernel-arrow (forward = aligned, $\chi_C = 0$; reverse = anti-aligned, $\chi_C = \pi$). Intermediate $\chi_C$ values require local substrate content (orientational freedom) that the scale-collapsed substrate cannot supply.

### 3.1 What follows from existing primitives

- The substrate has a single globally-coherent kernel-arrow direction (Paper_ED_CCC §3.7 + SC-4.x). ✓ IDENTIFIED.
- A chain advancing via V1 propagates forward in the kernel-arrow direction; reverse-propagation is refuted by Paper_089 T18 (advanced V1 contradicts P11). ✓ IDENTIFIED.
- The chain-arrow direction relative to the kernel-arrow direction has continuous angular content at the P09 phase level (the chirality $\chi_C \in S^1$). ✓ IDENTIFIED.

### 3.2 What Criterion-A requires

The substantive claim is that **intermediate $\chi_C \in (0, \pi) \cup (\pi, 2\pi)$ values are non-individuable in the post-SCBU regime.**

For this to be a substrate-graph derivation, one of the following must hold:

**(A1)** P09 phase values that are not aligned/anti-aligned ($0$ or $\pi$) have no substrate edge with the corresponding directional content. The chain cannot propagate via V1 at intermediate phase because V1 propagation requires substrate edges with the appropriate phase content, and the homogeneous substrate has only forward/reverse edges.

**(A2)** Paper_072 individuation criterion fails for intermediate $\chi_C$ because the chain's phase content cannot be preserved across P05 transport — specifically, intermediate phases require local substrate phase reference that the scale-collapsed substrate does not provide.

**(A3)** The chirality is fundamentally a $\mathbb{Z}_2$-valued quantity ("sign of alignment"), not an $S^1$-valued phase difference. The $S^1$ embedding via P09 is mathematical but not structurally load-bearing; the substrate-native chirality is binary.

### 3.3 Status of (A1), (A2), (A3)

**(A1) — substrate edge availability.** Substrate edges per P07 channel structure can have continuous P09 phase content; the claim that intermediate-phase edges do not exist in the post-SCBU regime is not derivable from existing primitives. P07 supplies channel structure but does not restrict phase content to binary in any regime. SC-4.x scale-collapse removes curvature-scale information but does not obviously remove orientational phase content (scale ≠ orientation). **OPEN. Not derivable from primitives + upstream content as currently formulated.**

**(A2) — individuation failure for intermediate phases.** Paper_072 individuation requires chain-identity preservation under V1/V5. P05 transports P09 phase along chain edges; in the post-SCBU regime, P05 transport is trivial (homogeneous substrate, no local rotation content). Trivial transport preserves any phase value, including intermediate ones. Paper_072 individuation criterion is therefore satisfied for all $\chi_C \in S^1$, not just $\{0, \pi\}$. **Criterion (A2) is INCONSISTENT with the current Paper_072 + P05 substrate content.** This is a substantive negative result.

**(A3) — chirality fundamentally $\mathbb{Z}_2$.** This requires REVISING the chirality definition from the $S^1$-valued phase difference (as constructed in the chirality memo) to a $\mathbb{Z}_2$-valued "alignment sign" quantity. The substrate-graph quantity that would support such a $\mathbb{Z}_2$ structure is not currently named in the corpus. P11 supplies binary directed events but the chirality memo's construction uses P09 (continuous) for the phase difference. **Reformulation requires substrate-graph work; not closable from current primitives + upstream content. OPEN.**

### 3.4 Verdict on Criterion-A

**Criterion-A does not close at substrate-graph level from existing primitives.** (A1) is OPEN; (A2) is structurally inconsistent with Paper_072 + P05 trivial transport; (A3) requires reformulation work.

The closest path to closure is (A3): reformulate chirality natively as $\mathbb{Z}_2$ via some substrate-graph quantity beyond P09 phase difference (candidate: a P11-derived alignment sign). This is constructible *in principle* but is not constructed; it would be the next focused construction memo if pursued.

---

## §4 Analysis of Criterion-B (capacity)

**Statement of Criterion-B:** In the saturation regime (substrate update-capacity exhausted), intermediate $\chi_C$ values require additional substrate slack to maintain V1-coherent propagation. Aligned chiralities ($\chi_C = 0$) require no slack because they are "in step" with kernel-arrow; anti-aligned ($\chi_C = \pi$) require minimal/no slack because the alignment-sign is binary; intermediate values require continuous slack that saturation precludes.

### 4.1 What follows from existing primitives

- Update-capacity saturation as a quantitative regime is **OPEN** (Memo_ED_Baryogenesis_Scoping item (b)). The capacity quantification itself is not constructed.
- V1 retarded propagation requires substrate-side V1 content at each substrate edge (Paper_089). ✓ IDENTIFIED.
- V5 cross-chain correlations contribute to substrate update-demand (Paper_090). ✓ IDENTIFIED.

### 4.2 What Criterion-B requires

The substantive claim is that **intermediate $\chi_C$ have a higher V1/V5 capacity demand than binary values $\{0, \pi\}$.**

For substrate-graph derivation:

**(B1)** A definition of substrate-graph "capacity cost" associated with maintaining a given $\chi_C$ value under V1 propagation.

**(B2)** A derivation that capacity cost is binary-minimized (lowest at $\chi_C = 0$ and $\chi_C = \pi$, higher at intermediate values).

**(B3)** A derivation that saturation threshold corresponds to capacity = aligned-chirality demand; below this threshold all $\chi_C$ admitted; above, only binary $\chi_C$.

### 4.3 Status of (B1), (B2), (B3)

**(B1) — capacity cost as substrate-graph quantity.** Not currently constructed. Capacity in the substrate corpus is implicit via P04 bandwidth × P07 channel multiplicity (Memo_ED_Baryogenesis_Scoping §2), but the per-$\chi_C$-value cost function is not defined. **OPEN. Requires substrate-graph construction.**

**(B2) — binary-minimization of capacity cost.** Would follow from (B1) if and only if intermediate $\chi_C$ require continuous substrate phase information that binary $\chi_C$ do not. Currently asserted, not derived. **OPEN.**

**(B3) — saturation threshold criterion.** Quantitative threshold for capacity saturation is OPEN (Memo_ED_Baryogenesis_Scoping item (b)). **OPEN.**

### 4.4 Verdict on Criterion-B

**Criterion-B does not close at substrate-graph level from existing primitives.** All three sub-items (B1)–(B3) are OPEN. (B1) is the prerequisite for (B2) which is the prerequisite for (B3); none has been attempted at substrate-graph level. Criterion-B is further from closure than Criterion-A: Criterion-A has a potential path via reformulation (A3), while Criterion-B requires three independent substrate-graph constructions.

---

## §5 Combined verdict: admission filter is OPEN

| Filter component | Status |
|---|---|
| Chirality definition $\chi_C \in S^1$ as P09 phase difference | **D-via-I** (chirality memo) |
| Conservation of $\chi_C$ along chains in post-SCBU regime | **D-via-I** (chirality memo §3.5) |
| Binary admission $\chi_C \in \{0, \pi\}$ — Criterion-A (structural) | **OPEN** — (A1) OPEN; (A2) inconsistent; (A3) requires reformulation |
| Binary admission $\chi_C \in \{0, \pi\}$ — Criterion-B (capacity) | **OPEN** — three sub-derivations all OPEN |
| Either criterion closing | **OPEN** |

**Substantive negative result:** the admission filter $\chi_C \in \{0, \pi\}$ is NOT derivable from existing ED substrate content in the post-SCBU regime. This is the load-bearing OPEN item identified in `Memo_ED_ChainArrowChirality.md` row 14, and this memo confirms it remains OPEN after focused analysis. Neither candidate criterion supplies a substrate-graph derivation; (A2) is structurally inconsistent under current Paper_072 + P05 content; the closest path to closure is (A3) reformulation of chirality as natively $\mathbb{Z}_2$-valued, which itself requires substrate-graph work not currently undertaken.

---

## §6 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P02, P04, P05, P07, P09, P11, P13 | P | Paper_087. |
| 2 | V1 retarded kernel; T18 advanced-V1 refuted by P11 | I | Paper_089. |
| 3 | V5 cross-chain kernel | I | Paper_090. |
| 4 | Kernel-arrow $\sigma_K(\ell)$ at locus | I | Paper_093 T18. |
| 5 | Paper_072 individuation regime | I | Paper_072. |
| 6 | SC-4.x cross-scale invariance + curvature-moment collapse | I | Papers SC-4.x. |
| 7 | Post-SCBU substrate homogeneity + globally-coherent kernel-arrow | I | Paper_ED_CCC §3.6 + §3.7. |
| 8 | Operational chirality $\chi_C := \pi_C - \pi_K \pmod{2\pi}$ | I | Memo_ED_ChainArrowChirality §3.3. |
| 9 | Conservation of $\chi_C$ along chains in post-SCBU regime | I | Memo_ED_ChainArrowChirality §3.5. |
| 10 | Criterion-A(1): intermediate $\chi_C$ have no V1-propagable substrate edge | **OPEN** | P07 + Paper_089 do not currently restrict edge phase content to binary. SC-4.x removes scale information, not orientation. §3.3. |
| 11 | Criterion-A(2): Paper_072 individuation fails for intermediate $\chi_C$ | **STRUCTURALLY INCONSISTENT** | Under current Paper_072 + P05 trivial transport in homogeneous regime, all $\chi_C$ are individuable. Negative result. §3.3. |
| 12 | Criterion-A(3): chirality natively $\mathbb{Z}_2$ via reformulation | **OPEN** | Requires substrate-graph reconstruction of chirality from P11-derived binary alignment-sign rather than P09 phase-difference. Not undertaken in this memo. §3.3. |
| 13 | Criterion-B(1): substrate-graph capacity cost as function of $\chi_C$ | **OPEN** | Capacity quantification itself is OPEN (Memo_ED_Baryogenesis_Scoping item b). §4.3. |
| 14 | Criterion-B(2): binary-minimization of capacity cost | **OPEN** | Conditional on (B1). §4.3. |
| 15 | Criterion-B(3): saturation threshold = aligned-chirality capacity demand | **OPEN** | Conditional on (B1) + (B2) + saturation threshold derivation. §4.3. |
| 16 | Substrate-graph admission filter $\chi_C \in \{0, \pi\}$ | **OPEN (load-bearing)** | Combined result: neither Criterion-A nor Criterion-B closes. §5. |
| 17 | Paper-specific postulate route: P-BinaryAdmission as declared postulate | **Available** (verdict M2) | Would close row 16 at the cost of a paper-specific postulate; eventual baryogenesis paper acceptable verdict M2. |
| 18 | Verdict: admission filter remains OPEN; closure requires substrate-graph extension or paper-specific postulate | **A→position** | Per Paper_095 §3.3. |

Zero pure-D rows. **Six load-bearing OPEN items** (rows 10, 12, 13, 14, 15, 16) plus one structurally-inconsistent path (row 11). The admission filter is therefore the binding constraint on the eventual baryogenesis paper's verdict.

---

## §7 Falsification Criteria

- **F1 (framework-killing):** Substrate-graph derivation showing all $\chi_C \in S^1$ uniformly admissible in the post-SCBU regime — i.e., Paper_072 individuation criterion holds for arbitrary $\chi_C$ values with no obstruction from V1/V5 or substrate homogeneity. This is item (A2) elevated to a substrate-graph proof; if achieved, **the entire ED-I-11 baryogenesis framework is refuted** and the corpus must abandon chirality-based asymmetry as a substrate mechanism. Currently consistent with Paper_072 + P05 + SC-4.x as constructed; this memo's row 11 is a partial step toward F1.

- **F2:** Substrate-graph derivation of a finer chirality structure (e.g., $\chi_C \in \{0, 2\pi/3, 4\pi/3\}$ ternary, or $\{0, \pi/2, \pi, 3\pi/2\}$ quaternary) in the post-SCBU regime. Would refute both the binary admission claim and the eventual baryogenesis architecture; would force restructuring around a non-binary chirality framework.

- **F3:** Substrate-graph reformulation showing chirality is natively $\mathbb{Z}_2$-valued via Criterion-A(3) AND that aligned and anti-aligned are symmetrically admitted (no asymmetric admission). Would close the binary structure but kill the baryogenesis-specific asymmetric-admission claim; would force baryogenesis to be a separate mechanism (potentially Criterion-B + saturation) rather than a chirality-admission effect.

- **F4:** Discovery that V1 retarded kernel admits genuine reverse-propagation modes (advanced support reactivated under some regime), contradicting Paper_089 T18. Would force reconsideration of the chain-arrow / kernel-arrow alignment framework entirely.

---

## §8 Recommended next steps

**Two paths forward** for the eventual baryogenesis paper:

### Path-1: Construct a substrate-graph reformulation of chirality as natively $\mathbb{Z}_2$.

Attempt Criterion-A(3) explicitly: identify a substrate-graph quantity inherited from P11 binary directed-event structure that supplies a $\mathbb{Z}_2$-valued "alignment sign" between chain-arrow and kernel-arrow. Candidates:
- The sign of the V1-propagation orientation between $\sigma_C$ and $\sigma_K$ (forward-aligned = $+1$, forward-anti-aligned = $-1$).
- The parity of the chain's commitment-event-relabeling under a substrate involution (if such an involution exists in the corpus).
- A V5-cross-chain symmetry generator (if Paper_090 admits a binary symmetry; not currently established).

If Path-1 succeeds, the admission filter closes at D-via-I and the baryogenesis paper proceeds at M3 verdict.

### Path-2: Declare P-BinaryAdmission as paper-specific postulate.

Accept the OPEN status of the admission filter as a substrate-graph derivation gap; declare a paper-specific postulate in the eventual baryogenesis paper:

> **P-BinaryAdmission:** *In the post-SCBU ignition regime, Paper_072 individuation admits only binary chain-arrow chirality $\chi_C \in \{0, \pi\}$. Substrate-graph derivation is OPEN.*

Verdict drops to **M2 (Intermediate Path C with declared paper-specific postulates)** but the baryogenesis paper becomes draftable.

### Recommendation

**Path-1 first.** A focused construction memo attempting the $\mathbb{Z}_2$-reformulation of chirality is the next prerequisite. If Path-1 closes (substrate-graph derivation found), the baryogenesis paper proceeds at M3. If Path-1 fails after focused attempt, fall back to Path-2 (M2 with P-BinaryAdmission postulate). Either way, this memo establishes that **the eventual baryogenesis paper cannot proceed at M3 without further construction work** beyond what currently exists in the corpus.

---

**End Memo_ED_AdmissionFilter.**
