# Paper EDSC-rstar — $r^*$ as FORCED Filtered-GRF Statistic (S1 Projection at Canonical Point)

**Series:** Wave-3 ED-SC 3.x Extension
**Status:** Wave-3 generative paper; M3 verdict at write-time (FORM-FORCED + VALUE-INHERITED; specific numerical $r^*$ pooled-$R^2$ values canon-internal)
**Companions:** Paper_096 ($\xi_{\mathrm{canonical}}$), Paper_EDSC_Motif (motif-conditioned distribution), Paper_EDSC_SaddleClassification (next), Paper_ED_SC_4.1.

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of the $r^*$ filtered-GRF statistic from nothing. Result is conditional on the 13 ED primitives (Paper_087) + declared paper-specific postulates (GRF regime hypothesis, P-S1-Invariant, canonical-operating-point selection).
2. It does **not** claim closed-proof reconstruction in the Hardy 2001 / CDP 2011 / Coecke-Kissinger operational-reconstruction sense. ED sits in the substrate-ontology lineage ('t Hooft cellular-automaton, Wolfram Ruliad, causal-set program), not the operational-reconstruction lineage.
3. It does **not** override Paper_095's three-tier verdict grammar. Verdict for this paper is stated in §1.
4. It does **not** claim positive predictive performance for $r^*$ — the current canon-internal pooled $R^2 \approx -1.88 \pm 0.4$ is **negative**, indicating the substrate-conditioned $r_*$ predictor explains LESS variance than a constant-mean null model. The paper reports this as evidence that canon-internal matching is statistically weak, not as a positive prediction.
5. **INHERITED vs FORCED breakdown:** The $r^*$-as-filtered-GRF-statistic form is D-via-I composition; predictive validity has been tested only canon-internally so far, and a substrate derivation of the kernel $K_{r^*}$ + pooled $R^2$ value is OPEN.
6. **Route A OPEN status:** This paper consumes $\xi_{canonical} = 1.7575$ lu (Paper_092). Substrate derivation of $\ell_{V5}(H_0)$ — and hence of $\xi_{canonical}$ from substrate parameters — is OPEN. All quantitative claims downstream inherit this OPEN status.
7. **(Correction, 2026-06-23.)** The title's and §1/§3.3's framing of $r^*$ as an **S1 (cross-scale invariant) projection** is **superseded on the invariance question**: the 2026-04-23 falsifier audit retired $r^*$ from invariant status (filter-conditioned, filter-dependent), so $r^*$ is **not S1** — its landing class (S2 vs S3) is unsettled. What survives, and what this paper actually forces, is the *structural form* — $r^*$ as a filtered-GRF statistic — **not** its invariance or predictive validity. For clarity on the number: the $-1.88 \pm 0.4$ is the predictor's **pooled $R^2$** (goodness-of-fit; negative ⇒ worse than a constant-mean null), **not** the value of $r^*$; the formerly-reported scalar $r^*$ median was $\approx -1.304$.

---

## Abstract

This paper formalizes the substrate-level observable $r^*$ as a **filtered-GRF statistic** at the S1 projection of the canonical operating point $\xi_{canonical} = 1.7575$ lu (Paper_096). $r^*$ is a linear functional of the substrate participation field filtered through V1 + V5 kernel content; standard linear-filter-preserves-Gaussian machinery composed with P-S1-Invariant forces the filtered-GRF structural form. The canon-internal pooled $R^2 \approx -1.88 \pm 0.4$ is INHERITED; this is a NEGATIVE value (predictor explains less variance than null), reported as honest evidence of weak canon-internal matching, not as positive prediction. Route A ($\ell_{V5}(H_0)$) is OPEN. Per Paper_095 form-FORCED / value-INHERITED methodology, verdict is **M3** for the structural form (predictive validity tested only canon-internally). Key falsifier **F1:** independent dataset (not used in canon calibration) yielding $R^2 > 0$ would constitute framework-level evidence.

---

## §1 Statement of Result

**Claim.** The substrate-level observable $r^*$ — identified in the ED-SC 3.x program as a load-bearing test statistic — is **FORCED to be a filtered-GRF statistic** at the **S1 projection of the canonical operating point** $\xi_{\mathrm{canonical}} = 1.7575$ lu (Paper_096). Specifically:

1. $r^*$ is a linear functional of the substrate participation field, filtered through V1 and V5 kernel content.
2. The substrate GRF structure (Paper_EDSC_Motif) forces $r^*$ to be Gaussian-distributed in the appropriate motif-conditioning.
3. The S1 projection at the canonical operating point fixes the distribution's specific moments to canon-internal values (pooled $R^2$ median $\approx -1.88 \pm 0.4$).

The structural form is FORM-FORCED. Specific numerical values (the $-1.88 \pm 0.4$ pooled $R^2$ median) are VALUE-INHERITED via canon-internal matching to the ED-SC 3.3.x closure.

Verdict: **M3**.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P02 (Participation)** — substrate-statistical content.
- **P10 (Rule-type primitive)** — V1, V5 kernels supplying filter content.
- **P13 (Time homogeneity)** — temporal-translation symmetry on which $r^*$ is defined.

### 2.2 Upstream Dependencies

- **I-091:** Kernel cascade.
- **I-096:** $\xi_{\mathrm{canonical}}$ canonical operating point, P-S1-Invariant.
- **I-EDSC-Motif:** Motif-conditioned distribution as S1 invariant.
- **I-089:** V1 finite-width retarded kernel.
- **I-090:** V5 cross-chain correlation kernel.
- **I-073:** DCGT coarse-graining.
- **I-GRF:** Standard Gaussian-random-field machinery.
- **I-Filter:** Standard linear-filtering theory.

---

## §3 Derivation

### 3.1 What $r^*$ is

In the ED-SC 3.x program, $r^*$ is a specific substrate-level observable defined via the substrate participation field at the canonical operating point. Per `project_ed_r_star_analytic_arc.md`, $r^*$ was developed across nine memos and closed at:
- Pooled $R^2$ median $\approx -1.88 \pm 0.4$.
- S1 projection at canonical operating point $\xi_{\mathrm{canonical}} = 1.7575$ lu.

The substrate-level construction: $r^*$ is a linear functional of the substrate participation field, evaluated at locations selected by the canonical-operating-point structure, filtered through the substrate kernel content (V1 + V5).

### 3.2 Filtered-GRF structure

By Paper_EDSC_Motif, the substrate participation field has GRF statistics in the appropriate regime. Linear filtering of a GRF preserves the Gaussian class (linear combinations of jointly-Gaussian random variables are Gaussian).

Specifically: if the substrate participation field $\Psi(x)$ is GRF and $r^* = \int K_{r^*}(x) \Psi(x) \, dx$ for some substrate-derived kernel $K_{r^*}$, then $r^*$ is itself a Gaussian random variable. Its moments are:
- $\langle r^*\rangle = \int K_{r^*}(x) \langle\Psi(x)\rangle \, dx = 0$ (if $\Psi$ is centered).
- $\langle (r^*)^2\rangle = \int\int K_{r^*}(x) C(x,y) K_{r^*}(y) \, dx \, dy$, where $C(x,y)$ is the substrate two-point correlator.

The kernel $K_{r^*}$ encodes the substrate-canonical-operating-point structure. The two-point correlator $C$ is the V1 + V5 kernel content.

### 3.3 S1 projection at canonical operating point

The S1 sector (Paper_096 P-S1-Invariant) contains substrate kernel content invariant under cross-scale transformations within the hydrodynamic window. $r^*$ is the **S1 projection at the canonical operating point**: the linear functional that captures the S1-invariant content of the substrate participation field at $\xi = \xi_{\mathrm{canonical}}$.

By Paper_EDSC_Motif, the motif-conditioned distribution at the canonical operating point is invariant under DCGT coarse-graining. The S1 projection $r^*$ inherits this invariance: $r^*$'s functional structure is preserved across scale transformations.

### 3.4 FORCED structure

The FORCED nature of $r^*$:
- Given the substrate GRF structure (Paper_EDSC_Motif), $r^*$ as a linear functional is Gaussian.
- Given P-S1-Invariant (Paper_096), the linear-functional structure is preserved under cross-scale transformations.
- Given the canonical operating point $\xi_{\mathrm{canonical}}$, the linear functional has specific (canon-internal) kernel structure.

The composition: $r^*$ as a filtered-GRF statistic is **forced** by P-S1-Invariant + GRF structure + canonical-operating-point selection. Specific numerical moments are canon-internal-inherited.

### 3.5 The pooled $R^2$ median value

Per `project_ed_r_star_analytic_arc.md`, the pooled $R^2$ median is canon-internal $\approx -1.88 \pm 0.4$. This is the empirical / canon-internal moment-matching outcome for $r^*$ at the canonical operating point.

**Operational definition:** Pooled $R^2$ computed over the realized GRF ensemble using a constant-mean null model; negative $R^2$ indicates the substrate-conditioned $r_*$ predictor explains LESS variance than the null. Stated as evidence the canon-internal matching is statistically weak, not as a positive prediction.

The substrate framework provides:
- FORM-FORCED: $r^*$ as filtered-GRF statistic at S1 projection.
- VALUE-INHERITED: numerical pooled $R^2 \approx -1.88 \pm 0.4$ from canon-internal matching.

A first-principles substrate derivation of the pooled $R^2$ value would require quantitative substrate-level derivation of the V1, V5 kernel data — analogous to Paper_ED_SC_4.2 Route A.

### 3.6 Connection to ED-SC 4.x extension

By Paper_ED_SC_4.2, $\xi_{\mathrm{canonical}} = 1.7575$ lu is a fixed point of substrate RG flow on the interval $[\ell_P, R_H]$ with cosmological-boundary anchoring. $r^*$, being the S1 projection at this fixed point, inherits structural anchoring to the SCBU boundary.

This places $r^*$ in the corpus's broader cross-scale-invariance framework. If Paper_ED_SC_4.2 Route A closes (substrate-derived $\ell_{V5}(H_0)$), $r^*$'s numerical content would acquire structural derivation, upgrading from canon-internal to substrate-derived.

### 3.7 What is OPEN

- Substrate-level derivation of the specific kernel $K_{r^*}$ from V1 + V5 + canonical-operating-point data.
- Substrate-level derivation of the pooled $R^2 \approx -1.88 \pm 0.4$ value.
- Empirical falsification programs targeting $r^*$ at canonical-operating-point regime.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P02, P10, P13 primitives | P | Primitives. |
| 2 | Substrate GRF structure | I | Paper_EDSC_Motif + Paper_096. |
| 3 | V1 + V5 kernel correlator content | I | Papers_089, 090. |
| 4 | Linear filtering preserves Gaussian class | I | Standard math (I-Filter). |
| 5 | $r^*$ as filtered-GRF statistic | D-via-I | Composition. |
| 6 | P-S1-Invariant cross-scale invariance | I | Paper_096. |
| 7 | $r^*$ at S1 projection of canonical operating point | A→position | Framing of the composed result; not separate derivation work (compositional content is at row 10). |
| 8 | Canonical operating point $\xi_{\mathrm{canonical}} = 1.7575$ lu | I | Paper_096 (canon-internal). |
| 9 | Pooled $R^2$ median $\approx -1.88 \pm 0.4$ | I | Canon-internal (ED-SC 3.3.x closure). |
| 10 | $r^*$ FORCED structural form | D | Composition. |
| 11 | $r^*$ inherits SCBU-boundary anchoring | I | Paper_ED_SC_4.2. |
| 12 | Verdict M3 | A→position | Per Paper_095. |

---

## §5 Falsification Criteria

- **F1:** Independent dataset (not used in canon calibration) yielding $R^2 > 0$ for the substrate $r_*$ predictor against the null would constitute framework-level evidence; the prior form of F1 (re-measurement reproducing the canon-internal value) only addresses canon-internal matching.
- **F2:** Substrate evidence that $r^*$ is NOT a filtered-GRF statistic — refutes step 5.
- **F3:** Substrate evidence that S1 invariance fails for $r^*$ — refutes step 7.
- **F4:** Substrate derivation of $r^*$ from first principles (upgrade, not refutation).

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), **not** within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

This paper formalizes the ED-SC 3.x r* analytic arc closure as a corpus paper.

**Relationship to other papers:**
- **Paper_096:** supplies the canonical operating point.
- **Paper_EDSC_Motif:** supplies the GRF / motif-conditioned framework.
- **Paper_ED_SC_4.2:** supplies the SCBU-boundary anchoring.

**Numerical content INHERITED.** Pooled $R^2 \approx -1.88 \pm 0.4$ canon-internal. **Form FORCED.** $r^*$ as filtered-GRF statistic at S1 projection.

Verdict: **M3**.

---

**End Paper EDSC-rstar.**
