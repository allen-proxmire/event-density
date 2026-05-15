# Paper ED-SC 4.1 — BH Horizon ↔ Cosmic Decoupling Surface

**Cross-Scale Correspondence at the Substrate–Cosmology Boundary**

**Series:** ED-SC 4.x — Cross-Scale Invariance Extensions
**Status:** Wave-3 generative paper; M3 verdict at write-time (FORM-FORCED + VALUE-INHERITED)
**Companions:** Paper_SCBU (Substrate–Cosmology Boundary Unification), Paper_039 (Horizon as decoupling surface, $\Gamma_{\mathrm{cross}} \to 0$), Paper_028 (Cosmic decoupling surface $R_H = c/H_0$), Paper_096 (Cross-scale invariance, ED-SC 3.x canonical), Paper_091 (Kernel cascade across scales), Paper_097 (Three-regime RG).

---

## §1 Statement of Result

**Claim.** The black-hole horizon radius $r_H = 2GM/c^2$ (Schwarzschild form, inherited from Paper_039) and the cosmic decoupling surface scale $R_H = c/H_0$ (inherited from Paper_028) are FORM-FORCED to be **two projections of the same substrate–cosmology boundary** under the SCBU unification postulate (Paper_SCBU) + cross-scale invariance (Paper_096). At substrate level, both quantities mark the locus where cross-chain participation flux $\Gamma_{\mathrm{cross}}$ saturates against the V5 cross-chain correlation budget; the two values $r_H$ and $R_H$ are projections of the single substrate object onto two distinct regime parameters — local-gravitational ($M$) and cosmological ($H_0$).

**Clarification.** This is a **FORM-FORCED structural correspondence**, not a numerical identification. The values $r_H$ and $R_H$ remain numerically INHERITED from the standard expressions (Schwarzschild form, Hubble-horizon form). The substrate-level claim is that both expressions descend from a single substrate object — the substrate–cosmology boundary — under two distinct projection mechanisms (azimuthal-Fourier for $R_H$, cross-chain cascade for $r_H$). The verdict is M3: FORM-FORCED structural-positive, VALUE-INHERITED, no constructive proof that one expression generates the other.

The paper closes the first extension target in the ED-SC 4.x roadmap: BH horizon ↔ cosmic decoupling surface as two manifestations of one substrate object.

---

## §2 Primitive Inputs

The 13 primitives P01–P13 per Paper_087 canonical enumeration are **posited**, not derived. The load-bearing primitives + cross-paper postulates invoked here are:

### 2.1 Primitives

- **P03 (Channel + locus indexing; spatial homogeneity)** — supplies the locus structure on which the substrate–cosmology boundary is defined; the boundary is a locus-level feature.
- **P08 (Substrate scale $\ell_{\mathrm{ED}}$)** — supplies the substrate-side length scale entering $G = c^3 \ell_P^2/\hbar$ (Paper_027); the cosmic-side scale enters via $H_0$.
- **P11 (Commitment-irreversibility)** — supplies the directional structure forcing $\Gamma_{\mathrm{cross}} \to 0$ at the boundary (Paper_039) and the cosmological-evolution direction (Paper_028 + Paper_038).
- **P13 (Time homogeneity)** — supplies the substrate temporal-translation invariance on which $H_0$ is defined as a global cosmological-rate parameter.

### 2.2 Cross-paper postulates inherited

- **P-Substrate-Cosmology-Unified (Paper_SCBU)** — the central SCBU postulate: BH-scale and cosmic-scale boundary structures share a single substrate object. This paper is a structural extension of P-Substrate-Cosmology-Unified, not an independent claim.
- **P-S1-Invariant (Paper_096)** — substrate-level S1 kernel-content is preserved across canonical-operating-point scale transformations within the hydrodynamic window; this paper extends the invariance to the cosmological-boundary regime.
- **P-Cascade-Continuity (Paper_091)** — coarse-graining between scale regimes is continuous under DCGT; this paper invokes the continuity at the BH-horizon-to-cosmological-boundary transition.

No new postulates introduced.

---

## §2.2 Upstream Dependencies

Load-bearing inheritances (I-rows in the audit table of §4):

- **I-028:** Cosmic decoupling surface $R_H = c/H_0$ (Paper_028). Marks the substrate-side cosmological scale beyond which dressed-object propagation decouples from local physics.
- **I-029:** Transition acceleration $a_0 = c H_0/(2\pi)$ (Paper_029). The factor of $2\pi$ in $a_0$ is the load-bearing azimuthal-Fourier projection signature used in §3.2.
- **I-039:** BH horizon structure with $\Gamma_{\mathrm{cross}} \to 0$ (Paper_039). Defines the substrate-side BH-horizon as the decoupling surface where cross-chain participation flux collapses.
- **I-091:** Kernel cascade across scales (Paper_091). Supplies the multi-scale substrate kernel structure used in §3.6.
- **I-096:** Cross-scale invariance with canonical operating point $\xi_{\mathrm{canonical}} = 1.7575$ lu (Paper_096). Provides the cross-scale-fixed-point mechanism used in §3.3.
- **I-097:** Three-regime RG (UV V1-dominated / transition / IR V5-dominated) (Paper_097). Supplies the regime classification used in §3.7.
- **I-SCBU:** Substrate-Cosmology Boundary Unification (Paper_SCBU). Supplies the unifying postulate P-Substrate-Cosmology-Unified that this paper extends.

All inheritances are upstream; no new substantive content introduced beyond projection-extension.

---

## §3 Derivation

### 3.1 Substrate–cosmology boundary as shared object

By P-Substrate-Cosmology-Unified (Paper_SCBU), the substrate-cosmology boundary is a **single substrate-level object** — a locus structure (P03) characterized by:

- (a) $\Gamma_{\mathrm{cross}}$ saturation against the V5 cross-chain correlation budget.
- (b) Substrate-level commitment-irreversibility (P11) marking the boundary as one-way.
- (c) Cross-scale invariance (P-S1-Invariant) ensuring the object survives DCGT coarse-graining without scale-rescaling.

This shared object is **not** the GR metric; it is a substrate-level structural feature. The two derived quantities $r_H$ and $R_H$ are projections of this object onto two distinct parameter regimes.

### 3.2 Projection mechanism A: substrate-causality (Paper_028)

The cosmic decoupling surface $R_H = c/H_0$ (Paper_028) arises from the substrate-cosmology boundary under a **substrate-causality / decoupling-surface argument**: beyond $R_H$, substrate-level cross-locus influence cannot reach a local chain coherently, because the kernel-propagation-rate / Hubble-expansion-rate crossover places the boundary at $R_H = c/H_0$. This is Paper_028's load-bearing mechanism; it does **not** invoke azimuthal-Fourier projection (that mechanism applies to $a_0$ via Paper_029, not to $R_H$).

Projection A yields:
$$R_H = c/H_0 \quad \text{(cosmic decoupling surface scale)} .$$

The factor of $2\pi$ that appears in Paper_029's $a_0 = c H_0/(2\pi)$ is a **distinct** projection-mechanism signature: it arises from azimuthal-Fourier-mode normalization on the residual SO(2) symmetry of an accelerating chain, applied at the galactic-acceleration parameter axis (Paper_029 + Paper_ED_SC_4.3 §3.2). Both projections share substrate-cosmology-boundary anchoring (via Paper_SCBU), but they use different projection mechanisms onto different parameter axes.

### 3.3 Projection mechanism B: cross-scale fixed point (Paper_096)

The BH horizon $r_H = 2GM/c^2$ (Schwarzschild form) arises from the substrate-cosmology boundary under **cross-scale fixed-point projection**: at a local-gravitational scale parameterized by mass $M$, the boundary's $\Gamma_{\mathrm{cross}}$ saturation occurs where the substrate-coarse-grained acoustic-metric (Paper_017) fixed-point condition is satisfied.

Under P-S1-Invariant (Paper_096), the substrate kernel content at the boundary is preserved under scale transformations; the fixed-point condition $\xi(r) = \xi_{\mathrm{canonical}}$ defines the boundary radius. Standard Schwarzschild machinery (inherited from Paper_039 + standard GR matching) yields:
$$r_H = 2GM/c^2 \quad \text{(BH horizon radius)} .$$

Projection B yields a mass-dependent boundary radius; Projection A yields a Hubble-rate-dependent boundary radius. Both project from the same substrate-cosmology boundary.

### 3.4 BH horizon as V5-saturated boundary (Paper_039)

By Paper_039, the BH horizon is the substrate surface where cross-chain participation flux $\Gamma_{\mathrm{cross}}$ saturates against the V5 cross-chain correlation budget. The V5-saturation interpretation:

- For $r < r_H$: substrate cells inside the would-be horizon have $\Gamma_{\mathrm{cross}}$ unable to bridge outward — V5 budget exhausted by the strong-curvature substrate configuration.
- For $r > r_H$: $\Gamma_{\mathrm{cross}}$ is sub-saturated; cross-chain correlation flows freely.
- At $r = r_H$: precisely the boundary — V5 budget exactly matched, $\Gamma_{\mathrm{cross}} = 0$ asymptotically (P11 commitment-irreversibility makes the boundary one-way).

This is the BH-side manifestation of the substrate-cosmology boundary. The cosmic-side manifestation (Paper_028) has the same V5-saturation structure at scale $R_H$.

### 3.5 Mapping $r_H \leftrightarrow R_H$ under SCBU

Under P-Substrate-Cosmology-Unified, the two quantities are related as projections of the single substrate object onto two parameter regimes:

$$\boxed{\quad r_H(M) \;\;\xleftrightarrow{\text{SCBU projection}}\;\; R_H(H_0) \quad}$$

where the left side parameterizes the boundary by local gravitational mass and the right side parameterizes it by global cosmological rate. The mapping is **structural**: there is no claimed numerical identity $r_H = R_H$ for any specific $(M, H_0)$ pair; rather, both quantities are FORM-FORCED to descend from the same substrate object.

The numerical values of $r_H$ and $R_H$ at any specific $(M, H_0)$ remain INHERITED from standard expressions. The substrate-level content is the **structural projection-correspondence**, not a quantitative identification.

The factor of 2 in $r_H = 2GM/c^2$ (Schwarzschild form) and the absence of a $2\pi$ factor in $R_H = c/H_0$ (Paper_028's substrate-causality form) are different projection-mechanism signatures, both inherited via empirical / standard-math matching at the projection level. The $2\pi$ that *does* appear in $a_0 = cH_0/(2\pi)$ (Paper_029) is a separate signature attached to the galactic-acceleration projection axis, not to $R_H$ itself.

### 3.6 Kernel-cascade interpretation (Paper_091)

By Paper_091's kernel cascade across scales, the substrate kernel hierarchy V1 → V5 → effective-hydrodynamic produces effective dynamics at successively larger scales under DCGT. The substrate-cosmology boundary lives at the **endpoint** of this cascade:

- **UV regime ($r \lesssim \ell_{V1}$):** V1-dominated; boundary structure not yet active.
- **Transition regime ($\ell_{V1} \lesssim r \lesssim \ell_{V5}$):** V5 takes over; cross-chain bandwidth structure becomes relevant.
- **Hydrodynamic regime ($\ell_{V5} \lesssim r \lesssim L_{\mathrm{flow}}$):** V5-modulated effective dynamics.
- **BH-horizon regime ($r \sim r_H$):** V5 cross-chain budget saturates; $\Gamma_{\mathrm{cross}} \to 0$.
- **Cosmological regime ($r \sim R_H$):** V5 cross-chain budget saturates at global cosmological scale; same substrate-cosmology boundary, projected azimuthally-Fourier.

By P-Cascade-Continuity (Paper_091), the transition between regimes is smooth; the BH-horizon and cosmological-decoupling regimes are continuous endpoints of the same cascade structure.

### 3.7 Regime classification: four RG regimes with multi-parameter cosmological arms

Composing Paper_097's three-regime RG (UV V1-dominated, transition, IR V5-dominated) with this paper's substrate-cosmology boundary projection, the full classification is **four RG regimes** with regime 4 (cosmological) hosting two parameter-axis arms (local-gravitational mass and global cosmological rate):

| Regime | Scale | Substrate content | Boundary manifestation |
|---|---|---|---|
| 1 UV | $r \lesssim \ell_{V1}$ | V1-dominated | Sub-cascade; no boundary |
| 2 Transition | $\ell_{V1} \lesssim r \lesssim \ell_{V5}$ | V1↔V5 cascade region | Cascade region (Paper_097 0.6 exponent) |
| 3 IR (hydrodynamic) | $\ell_{V5} \lesssim r \lesssim L_{\mathrm{flow}}$ | V5-modulated dynamics | NS / MHD regime |
| 4 Cosmological — local-grav arm | $r \sim r_H$ | V5-saturated boundary | BH-horizon projection of substrate-cosmology boundary (parameterized by mass $M$) |
| 4 Cosmological — global arm | $r \sim R_H$ | V5-saturated boundary | Cosmic decoupling projection of substrate-cosmology boundary (parameterized by $H_0$) |

The two "regime 4" rows are **both arms of the same RG regime** — different parameter-axis projections of the same V5-saturated substrate-cosmology boundary. They are not separate regimes; they are two parameter-axis manifestations within regime 4. The substrate object is one; the parameter-axes of its projection are two.

### 3.8 Summary

The BH horizon $r_H = 2GM/c^2$ and the cosmic decoupling surface $R_H = c/H_0$ are **two parameter-axis arms of regime 4** (cosmological) under the SCBU unification postulate. They differ by:

- **Projection mechanism:** substrate-causality / decoupling-surface argument (Paper_028, for $R_H$) vs cross-scale fixed-point + Schwarzschild matching (Paper_039 + Paper_096, for $r_H$).
- **Parameter axis:** global cosmological rate $H_0$ vs local gravitational mass $M$.
- **Numerical-factor signatures:** $R_H$ carries no special signature factor (form is $c/H_0$ directly); $r_H$ carries Schwarzschild factor $2$. Both inherited via empirical / standard-math matching, not derived from substrate primitives.

The structural correspondence is FORM-FORCED. The numerical values are INHERITED. The verdict is **M3**: form-FORCED + value-INHERITED, no constructive numerical identification claimed.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | 13 primitives posited per Paper_087 | P (axiomatic) | Substrate ontology. |
| 2 | P-Substrate-Cosmology-Unified | I | Inherited from Paper_SCBU. |
| 3 | Cosmic decoupling surface $R_H = c/H_0$ | I | Paper_028. |
| 4 | $a_0 = c H_0/(2\pi)$ azimuthal-Fourier signature | I | Paper_029. |
| 5 | BH horizon $\Gamma_{\mathrm{cross}} \to 0$ structure | I | Paper_039. |
| 6 | Kernel cascade across scales | I | Paper_091. |
| 7 | Cross-scale invariance + canonical operating point | I | Paper_096. |
| 8 | Three-regime RG classification | I | Paper_097. |
| 9 | Substrate-cosmology boundary as shared object | D (composition of SCBU + I-039 + I-028) | Composition is new content of §3.1. |
| 10 | Projection A: substrate-causality $\to R_H = c/H_0$ | D-via-I | Application of Paper_028 substrate-causality argument to SCBU object. |
| 11 | Projection B: cross-scale fixed-point $\to r_H = 2GM/c^2$ | D-via-I | Application of Paper_096 fixed-point + Schwarzschild matching to SCBU object. |
| 12 | BH horizon = V5-saturated boundary manifestation | I | Paper_039 substrate identification. |
| 13 | Mapping $r_H \leftrightarrow R_H$ under SCBU | D (composition) | §3.5; structural correspondence, not numerical identity. |
| 14 | Cascade-continuity at boundary regimes | I | Paper_091. |
| 15 | Four-regime classification with regime-4 two-arm (local-grav $r_H$ + global $R_H$) | D-via-I | §3.7 composition of Paper_097 + SCBU + this paper. |
| 16 | Structural correspondence FORM-FORCED | A→position | Composite verdict. |
| 17 | Numerical values $r_H, R_H$ inherited | I | Standard expressions; not derived from substrate primitives. |
| 18 | M3 verdict (FORM-FORCED + VALUE-INHERITED) | A→position | Verdict register per Paper_095 methodology. |
| 19 | Constructive numerical identity $r_H = R_H$ for some $(M, H_0)$ | NOT CLAIMED | OPEN; not the scope of this paper. |

---

## §5 Falsification Criteria

- **F1:** BH horizon scaling inconsistent with $H_0$ variation under SCBU prediction — i.e., empirical detection that $r_H$ for BH of mass $M$ does **not** track the same substrate-cosmology boundary as $R_H$ under SCBU projection. If $r_H$ and $R_H$ have independent substrate-level mechanisms (rather than projections of one object), the SCBU-extension fails.

- **F2:** $r_H$ and $R_H$ respond differently to substrate-scale rescaling. Under P-S1-Invariant, both should be governed by the same substrate-scale-rescaling response (since they project from the same substrate object). If empirical / structural evidence shows they respond differently (e.g., one rescales with $\ell_P$, the other does not), the projection-extension fails.

- **F3:** Cross-scale invariance (Paper_096) fails at the cosmological regime. The SCBU projection requires P-S1-Invariant to extend to the cosmological-boundary scale. If cross-scale invariance breaks at $R_H$-class scales, the extension collapses.

- **F4:** SCBU postulate (P-Substrate-Cosmology-Unified) refuted by an independent derivation showing BH-side and cosmic-side boundaries originate from distinct substrate objects. This refutes the unifying postulate that this paper extends.

- **F5:** Kernel-cascade discontinuity at the cosmological regime — by P-Cascade-Continuity, the transition from the hydrodynamic regime to the cosmological-boundary regime should be smooth under DCGT. If a substrate-level discontinuity is identified at the cascade-to-cosmology transition, the cascade-continuity step (§3.6) fails.

Refutation of any of F1–F5 falsifies the extension verdict without necessarily refuting either of the constituent boundaries (Paper_039 BH-horizon and Paper_028 cosmic decoupling surface remain individually intact; only the SCBU projection-correspondence is refuted).

---

## §6 Rewrite Note

This paper is the **first ED-SC 4.x extension paper**. The ED-SC 3.x arc closed with cross-scale invariance at the substrate-kernel level (Paper_096) + three-regime RG (Paper_097). The ED-SC 4.x roadmap extends cross-scale invariance to **substrate–cosmology boundary phenomena**: specifically, the structural correspondences linking BH-scale features (horizons, Hawking, remnants, BHPT scattering) with cosmic-scale features (decoupling surface, Hubble horizon, BTFR slope-4 universality, large-scale-structure).

**Relationship to Paper_SCBU.** Paper_SCBU supplies the unifying postulate P-Substrate-Cosmology-Unified: BH-scale and cosmic-scale boundary structures share a single substrate object. This paper (Paper_ED_SC_4.1) is a **projection-extension**: it shows that two specific quantities ($r_H$ from Paper_039 and $R_H$ from Paper_028) are projections of the SCBU object under two distinct mechanisms (cross-scale fixed-point and azimuthal-Fourier respectively). No semantic drift from SCBU: this paper does not modify P-Substrate-Cosmology-Unified or introduce a parallel claim; it extends SCBU to a specific instance.

**Roadmap status.** This paper closes the first extension target in the ED-SC 4.x roadmap: BH horizon ↔ cosmic decoupling surface as two boundary-regime manifestations of one substrate object. Subsequent ED-SC 4.x papers (in queue) extend the correspondence to Hawking ↔ cosmological-redshift (substrate-Unruh / KMS at cosmological boundary), remnant ↔ cosmological-relic-abundance (already partially in Paper_049, awaiting SCBU explicit framing), and BHPT scattering ↔ large-scale-structure-formation (most speculative; ED-SC 4.x deferred).

**Numerical content.** Numerical values $r_H = 2GM/c^2$ and $R_H = c/H_0$ remain **INHERITED** from standard expressions. The substrate-level claim is the **structural projection-correspondence**, FORM-FORCED only. The factors of $2$ (Schwarzschild) and $2\pi$ (Hubble + azimuthal-Fourier signature) are different projection-mechanism artifacts and are not derived from substrate primitives at the SCBU level. Verdict: **M3** (FORM-FORCED + VALUE-INHERITED).

---

**End Paper ED-SC 4.1.**
