# Paper EDSC-Saddle — Saddle-Geometry Classification (S1 / S2 / S3)

**Series:** Wave-3 ED-SC 3.x Extension — Saddle-Geometry Sector
**Status:** Wave-3 generative paper; M3 verdict at write-time (form-IDENTIFIED Hessian-signature classification + INHERITED specific saddle parameters)
**Companions:** Paper_EDSC_Motif, Paper_EDSC_rstar, Paper_096, Paper_087.

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of the S1/S2/S3 saddle-classification from nothing. Result is conditional on the 13 ED primitives (Paper_087) + declared paper-specific postulates (P-S1-Invariant, substrate-action structure).
2. It does **not** claim closed-proof reconstruction in the Hardy 2001 / CDP 2011 / Coecke-Kissinger operational-reconstruction sense. ED sits in the substrate-ontology lineage ('t Hooft cellular-automaton, Wolfram Ruliad, causal-set program), not the operational-reconstruction lineage.
3. It does **not** override Paper_095's three-tier verdict grammar. Verdict for this paper is stated in §1.
4. It does **not** claim substrate-FORCED exhaustiveness of S1/S2/S3 — the trichotomy is partition-by-construction on the axes {invariant, ensemble-conditioned, motif-conditioned}, not a substrate-derived theorem. Substrate-level proof that no fourth class is structurally relevant is **OPEN**.
5. **INHERITED vs FORCED breakdown:** The classification form is D-via-I composition (Hessian/Morse machinery + P-S1-Invariant + motif-conditioning); exhaustiveness in the substrate sense is OPEN.
6. **Route A OPEN status:** This paper consumes $\xi_{canonical} = 1.7575$ lu (Paper_092). Substrate derivation of $\ell_{V5}(H_0)$ — and hence of $\xi_{canonical}$ from substrate parameters — is OPEN. All quantitative claims downstream inherit this OPEN status.
7. **(Correction, 2026-06-23.)** Where §6 / the companion references list $r^*$ (Paper_EDSC_rstar) as an **S1 (cross-scale invariant)** example, that is **superseded**: the 2026-04-23 falsifier audit (ED-SC 2.0 r\* Final Verdict) retired $r^*$ from invariant status and reclassified it as a *filter-conditioned* GRF statistic. Being filter/motif-dependent, $r^*$ is therefore **not S1**; its correct landing class (S2 ensemble-only vs S3 motif-specific) is **unsettled** by the source language, which calls $r^*$ both *motif-conditioned* and *filter-conditioned*. The S1/S2/S3 *classification scheme* — this paper's actual result — is **unaffected**; only the mislabeled example is corrected.

---

## Abstract

This paper formalizes a substrate-level **three-class classification** of saddle-geometry of the substrate participation-action: **S1 (cross-scale invariant)**, **S2 (ensemble-only)**, **S3 (motif-specific)**. The classification is constructed via composition of standard Hessian-signature / Morse-theory machinery with P-S1-Invariant (Paper_096), motif-conditioning (Paper_EDSC_Motif), and ensemble-regime decomposition. The trichotomy is exhaustive **by partition-axis construction**; substrate-FORCED exhaustiveness (no fourth structural class) is OPEN. The canon-internal 5×3 verdict grid is INHERITED. Route A ($\ell_{V5}(H_0)$) is OPEN. Per Paper_095 form-FORCED / value-INHERITED methodology, verdict is **M3** for the classification form. Key falsifier **F1:** discovery of a substrate-derived classification axis orthogonal to {invariant, ensemble-conditioned, motif-conditioned} requiring a fourth class.

---

## §1 Statement of Result

**Claim.** The substrate-level saddle-geometry of the participation-action functional admits a **canonical three-class classification** based on Hessian-signature structure:

- **S1 (cross-scale invariant):** Saddle classes invariant under DCGT coarse-graining; Hessian signature preserved across scales. Examples: substrate kernel-content extrema; cross-scale fixed points (Paper_096).
- **S2 (ensemble-only):** Saddle classes whose Hessian signature is statistical-ensemble-level, not preserved under specific substrate realizations. Regime-dependent structure.
- **S3 (motif-specific):** Saddle classes specific to particular substrate motifs; Hessian signature determined by motif content; not cross-scale invariant.

The three-class classification is form-IDENTIFIED by:
1. Hessian-signature structure of substrate-action saddle points (standard differential geometry of critical points).
2. P-S1-Invariant cross-scale invariance (Paper_096) selecting S1 class.
3. Motif-conditioning (Paper_EDSC_Motif) selecting S3 class.
4. Regime-dependent ensemble statistics selecting S2 class.

Verdict: **M3**.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P02 (Participation)** — substrate-action content.
- **P10 (Rule-type primitive)** — V1, V5 kernel structure entering Hessian.
- **P12 (Stability landscape)** — substrate-level stability content (Hessian-signature relevance).

### 2.2 Upstream Dependencies

- **I-026:** Cumulative-strain reading of P12 stability landscape.
- **I-091:** Kernel cascade.
- **I-096:** Cross-scale invariance + $\xi_{\mathrm{canonical}}$.
- **I-EDSC-Motif:** Motif-conditioned distribution.
- **I-EDSC-rstar:** $r^*$ filtered-GRF statistic.
- **I-Hessian:** Standard Hessian / Morse-theory classification.
- **I-Saddle:** Standard saddle-point / steepest-descent machinery.

---

## §3 Derivation

### 3.1 Substrate-action and saddle structure

The substrate-level participation-action $S_{\mathrm{sub}}[\Psi]$ is a functional of the substrate participation field $\Psi$, with V1 + V5 kernel content supplying the action's quadratic form. Critical points of $S_{\mathrm{sub}}$ — solutions of $\delta S_{\mathrm{sub}}/\delta\Psi = 0$ — are the substrate-level **saddle points**.

The **Hessian** at each saddle, $\mathcal{H} = \delta^2 S_{\mathrm{sub}}/\delta\Psi\delta\Psi'$, classifies the saddle by its eigenvalue-signature:
- All positive: minimum.
- All negative: maximum.
- Mixed signs: saddle (proper).
- Some zero: degenerate.

Standard Morse-theory machinery (I-Hessian) supplies the classification framework.

### 3.2 S1 — Cross-scale invariant saddle classes

By Paper_096 P-S1-Invariant, certain substrate-level structural features are preserved under DCGT coarse-graining. Saddle classes whose Hessian-signature pattern is **preserved** across scales are the **S1 saddles**.

Examples:
- The canonical operating point $\xi_{\mathrm{canonical}} = 1.7575$ lu (Paper_096) is an S1 saddle: a substrate-RG fixed point with cross-scale-invariant Hessian signature.
- Substrate kernel-content extrema at the V1 / V5 transition scale are S1 (per Paper_091 cascade structure).

S1 saddles inherit the universal structural properties of the substrate framework: they are scale-invariant features.

### 3.3 S2 — Ensemble-only saddle classes

S2 saddles are saddle classes whose Hessian signature is **statistical-ensemble-level only** — they describe ensemble-averaged substrate behavior, but specific substrate realizations may exhibit different signatures.

Examples:
- Mean-field saddle points of the substrate-action ensemble.
- Statistical-mechanics critical points (analog of phase-transition critical points) in substrate participation thermodynamics.

S2 saddles are regime-dependent: their classification holds in specific ensemble regimes (e.g., the hydrodynamic-window) but does not extend cross-scale.

### 3.4 S3 — Motif-specific saddle classes

S3 saddles are saddle classes specific to particular substrate motifs. Their Hessian signature is determined by the **specific motif** $M$ on which the saddle is realized. Different motifs produce different S3 saddle classes.

Examples:
- Saddle points of the substrate-action when restricted to participation fields with specific motif $M$.
- Symmetry-broken saddle classes in motifs lacking the full substrate symmetry.

S3 saddles are **non-universal**: they depend on motif-specific substrate content. The motif-conditioning (Paper_EDSC_Motif) selects specific S3 saddle structure.

### 3.5 Exhaustiveness of S1 / S2 / S3

The three-class classification is form-IDENTIFIED (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3) to be **exhaustive** at substrate level:
- Any saddle is either cross-scale invariant (S1) or not.
- If not cross-scale invariant, it is either ensemble-level (S2) or motif-specific (S3).
- These three exhaust the possibilities under the substrate-level Morse-theory + invariance-class analysis.

The exhaustiveness mirrors the three-constituent structure of $\mathcal{M}_{\mathrm{cap}}$ (Paper_053 / 055 Q-Compute three-class exhaustiveness): in both cases, the substrate's structural decomposition into three exhaustive classes is FORCED by primitive content.

### 3.6 The 5×3 verdict grid (canon-internal)

Per `project_ed_sc_3_arc.md`, the ED-SC 3.3.x arc closure included a **5×3 verdict grid** classifying substrate-level saddle realizations into the S1 / S2 / S3 classes across five regime contexts. The grid's content:
- 0 cells "Refuted" — all 15 cells are at minimum "Conditional-positive" or stronger.
- Specific cell-by-cell verdicts are canon-internal-inherited.

The structural classification (this paper) FORCED. The specific 5×3 verdict-grid content INHERITED.

### 3.7 Geometric interpretation in substrate

Geometrically, the three saddle classes correspond to:
- **S1:** "Fixed-point" geometry — the saddle is structurally locked at a scale-invariant location in substrate configuration space.
- **S2:** "Statistical-equilibrium" geometry — the saddle is the equilibrium of an ensemble distribution.
- **S3:** "Motif-broken" geometry — the saddle is at a symmetry-broken configuration specific to a particular motif.

The three correspond to three distinct mechanisms by which the substrate-action functional develops critical points.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P02, P10, P12 primitives | P | Primitives. |
| 2 | Substrate-action $S_{\mathrm{sub}}[\Psi]$ structure | I | Cites Paper_087 P10 + Paper_095 substrate-action; explicit construction OPEN. |
| 3 | Hessian-signature classification | I | Standard Morse theory (I-Hessian). |
| 4 | P-S1-Invariant cross-scale invariance | I | Paper_096. |
| 5 | S1 cross-scale invariant saddle class | D-via-I | Composition. |
| 6 | Ensemble-level statistical structure | I | Standard statistical mechanics. |
| 7 | S2 ensemble-only saddle class | D-via-I | Composition. |
| 8 | Motif-conditioning structure | I | Paper_EDSC_Motif. |
| 9 | S3 motif-specific saddle class | D-via-I | Composition. |
| 10 | Three-class exhaustiveness | D-via-I | Partition by construction: invariant vs non-invariant; if non-invariant, ensemble-conditioned vs motif-conditioned. Trichotomy is exhaustive *by definition of the partition axes*, not by substrate-FORCED argument. Substrate-level proof that no fourth class is structurally relevant is OPEN. |
| 11 | 5×3 verdict grid | I | Canon-internal (ED-SC 3.3.x). |
| 12 | Specific saddle realizations per substrate motif | I | Empirical / canon-internal. |
| 13 | Substrate exhaustiveness of S1/S2/S3 (no fourth class) | OPEN | Partition-axis exhaustiveness is by definition, not substrate-derived. |
| 14 | Verdict M3 | A→position | Per Paper_095. |

---

## §5 Falsification Criteria

- **F1:** Discovery of a substrate-derived classification axis orthogonal to {invariant, ensemble-conditioned, motif-conditioned} requiring a fourth class would falsify the closure claim.
- **F2:** Cross-scale-invariant saddle shown to be motif-specific (S3 mislabel). Would refute step 5.
- **F3:** Motif-specific saddle shown to be cross-scale invariant. Would refute step 9.
- **F4:** 5×3 verdict-grid cell shown empirically refuted. Would refute canon-internal matching.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), **not** within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

This paper formalizes the ED-SC 3.x saddle-geometry classification (S1 / S2 / S3) for the corpus.

**Relationship to other papers:**
- **Paper_096:** supplies P-S1-Invariant principle.
- **Paper_EDSC_Motif:** supplies motif-conditioning framework.
- **Paper_EDSC_rstar:** $r^*$ was *originally* offered as an S1 example — **superseded** (see Preamble item 7). Following the 2026-04-23 falsifier audit $r^*$ is retired from invariant status, filter/motif-dependent, hence **not cross-scale invariant (not S1)**; landing class S2-vs-S3 unsettled. What is forced for $r^*$ is its *structural form* (a filtered-GRF statistic), not its invariance.
- **Paper_053 / 055 Q-Compute:** analogous three-class exhaustiveness (different sector).

**Numerical content INHERITED.** Specific saddle parameters, 5×3 verdict-grid contents. **Form IDENTIFIED.** Three-class S1 / S2 / S3 exhaustive classification (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3).

Verdict: **M3**.

---

**End Paper EDSC-SaddleClassification.**
