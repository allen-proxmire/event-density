# Paper ED-SC 4.2 — Substrate-Derivation of $\xi_{\mathrm{canonical}}(H_0)$

**Cross-Scale Fixed-Point Derivation from the Substrate–Cosmology Boundary**

**Series:** ED-SC 4.x — Cross-Scale Invariance Extensions
**Status:** Wave-3 generative paper; M3 verdict at write-time (derivation attempted, does not close at substrate-first-principles level; value-INHERITED status preserved; structural setup is FORM-FORCED M3)
**Companions:** Paper_SCBU (Substrate–Cosmology Boundary Unification), Paper_096 (Cross-scale invariance, $\xi_{\mathrm{canonical}}$ canonical value), Paper_029 ($a_0 = c H_0/(2\pi)$), Paper_ED_SC_4_1 (BH ↔ cosmic decoupling boundary projection), Paper_091 (kernel cascade), Paper_097 (three-regime RG).

---

## §1 Statement of Result

**Claim (attempted).** The ED-SC canonical operating point $\xi_{\mathrm{canonical}}$ (Paper_096; canon-internal numerical value 1.7575 lu inherited from ED-SC 3.3.x closure) is a **cross-scale fixed point** of the substrate kernel hierarchy (Paper_091 + Paper_092) whose value is **structurally constrained** by the substrate-cosmology boundary $R_H = c/H_0$ (Paper_028, projected via Paper_ED_SC_4.1).

**Clarification.** This paper **attempts** a substrate-level derivation of $\xi_{\mathrm{canonical}}$ as a function of $H_0$. Two outcomes are possible at write-time:

- **(Outcome-Close)** The derivation closes: $\xi_{\mathrm{canonical}}$ is FORM-FORCED + VALUE-FORCED from substrate primitives + P-Substrate-Cosmology-Unified, upgrading Paper_096's verdict from M3 → M2 (or M1 if no additional postulate is required).
- **(Outcome-Open)** The derivation produces a structural setup + dimensional / scaling constraints but **does not close** at first-principles level — the value of $\xi_{\mathrm{canonical}}$ remains INHERITED via canon-internal matching, pending a substrate-derived input not currently in the corpus.

**Outcome of this paper.** The derivation **does not close** in the constructive sense. The fixed-point structure is set up, dimensional and scaling constraints are identified, and the missing substrate-level input is explicitly characterized as a **substrate-cosmology coupling parameter** that is not currently derived from primitives. Verdict remains **M3**: FORM-FORCED structural setup + VALUE-INHERITED numerical content. The paper supplies the **structural setup** for any future closure attempt.

Honest framing: this is the highest-leverage ED-SC 4.x paper, and the honest outcome is that the closure requires either (i) a substrate-derived $\ell_{V5}(H_0)$ relation or (ii) a substrate-derived RG-fixed-point-equation solution. Neither is supplied by this paper. The setup is supplied; the closure is OPEN.

---

## §2 Primitive Inputs

The 13 primitives P01–P13 per Paper_087 canonical enumeration are **posited**, not derived. The load-bearing primitives + cross-paper postulates invoked here are:

### 2.1 Primitives

- **P03 (Channel + locus indexing; spatial homogeneity)** — supplies locus structure on which fixed-point conditions are defined.
- **P08 (Substrate scale $\ell_{\mathrm{ED}}$)** — supplies the substrate-side length scale entering V1 width $\ell_{V1} \sim \ell_P$.
- **P11 (Commitment-irreversibility)** — supplies the directional substrate evolution against which RG flow is defined.
- **P13 (Time homogeneity)** — supplies the temporal-translation invariance on which $H_0$ is defined as a cosmological-rate parameter (Paper_037 P-H0-Cosmological-Invariant).

### 2.2 Cross-paper postulates inherited

- **P-Substrate-Cosmology-Unified (Paper_SCBU)** — the SCBU postulate is the central load-bearing inheritance: BH-scale and cosmic-scale boundary structures share a single substrate object.
- **P-S1-Invariant (Paper_096)** — supplies the cross-scale invariance condition that defines the fixed-point structure.
- **P-Cascade-Continuity (Paper_091)** — supplies the smooth-cascade structure connecting V1, V5, hydrodynamic, and boundary regimes.

**No new postulates introduced.** The derivation attempt rests entirely on inherited postulates + structural composition.

---

## §2.2 Upstream Dependencies

Load-bearing inheritances:

- **I-028:** Cosmic decoupling surface $R_H = c/H_0$ (Paper_028).
- **I-029:** Transition acceleration $a_0 = c H_0/(2\pi)$ — supplies the azimuthal-Fourier $2\pi$ signature.
- **I-091:** Kernel cascade across scales (V1 → V5 → effective-hydrodynamic).
- **I-096:** Cross-scale invariance at canonical operating point $\xi_{\mathrm{canonical}}$ (canon-internal value 1.7575 lu).
- **I-097:** Three-regime RG (UV / transition / IR).
- **I-SCBU:** Substrate-Cosmology Boundary Unification (Paper_SCBU).
- **I-ED_SC_4_1:** BH horizon $r_H$ ↔ cosmic decoupling $R_H$ as two projections of one substrate-cosmology boundary (Paper_ED_SC_4.1).

---

## §3 Derivation Attempt

### 3.1 $\xi_{\mathrm{canonical}}$ as fixed point of the kernel hierarchy

By Paper_091 + Paper_092, the substrate kernel hierarchy is parameterized by $(\ell_n, r_n, k_n)$: characteristic scale, retardation order, cross-chain rank. The cascade flows V1 ($\ell_P$, 1, 1) → V5 ($\ell_{V5}$, $\infty$, 2) → effective hydrodynamic ($R_{\mathrm{cg}}$, $\infty$, $\geq 2$).

By Paper_096, the cross-scale invariance condition selects a **canonical operating point**: a scale $\xi$ at which the substrate S1 kernel-content is preserved under coarse-graining. Formally, denoting the RG flow on kernel-content by $\mathcal{R}_\lambda$ (where $\lambda$ is the rescaling parameter):
$$\mathcal{R}_\lambda \big[ K(\xi_{\mathrm{canonical}}) \big] = K(\xi_{\mathrm{canonical}}) \quad \text{for all } \lambda \in [1, \lambda_{\max}] .$$

This is the substrate-level **fixed-point condition** defining $\xi_{\mathrm{canonical}}$.

The fixed-point structure has three substrate-level constituents:
- **V1 width-scale anchor** $\ell_P$ from P08.
- **V5 bandwidth anchor** $\ell_{V5}$ — a substrate kernel scale at the hydrodynamic-window edge.
- **Cosmological boundary anchor** $R_H = c/H_0$ from Paper_028.

The fixed-point condition is structurally a relation among these three scales.

### 3.2 Mapping fixed-point conditions to $R_H = c/H_0$

Under P-Substrate-Cosmology-Unified (Paper_SCBU), the cosmological boundary $R_H$ is **part of the substrate's kernel-hierarchy structure**, not external to it. The RG flow extends from the UV regime (V1-dominated) through the transition (Paper_097 0.6 exponent regime) to the IR regime (V5-dominated) and beyond, terminating at the substrate-cosmology boundary $R_H$.

The fixed-point condition (§3.1) becomes a **boundary-condition equation** on the RG flow:
$$\mathcal{R}_\lambda \big[ K(\xi) \big]\Big|_{\xi = \xi_{\mathrm{canonical}}} = K(\xi_{\mathrm{canonical}}) , \quad \xi \in [\ell_P, R_H] .$$

This is a substrate-level RG flow on the interval $[\ell_P, R_H]$ with a fixed point at $\xi_{\mathrm{canonical}}$.

The substrate-cosmology boundary $R_H$ enters as the **upper boundary** of the RG flow interval. The lower boundary is $\ell_P$ (substrate UV cutoff). The fixed point $\xi_{\mathrm{canonical}}$ lies somewhere in between.

### 3.3 Dimensional analysis + scaling constraints

The dimensional constraints on $\xi_{\mathrm{canonical}}$:

- $\ell_P \sim 10^{-35}$ m (UV anchor).
- $R_H \sim c/H_0 \sim 10^{26}$ m (cosmological anchor).
- $\ell_{V5}$ — substrate kernel scale, not directly known but bounded by hydrodynamic-window edge.

The ratio $R_H / \ell_P \sim 10^{61}$ — about 61 decades.

For $\xi_{\mathrm{canonical}}$ to be a meaningful canonical operating point in **lattice units** (lu), the value must be set by a substrate-derived dimensionless combination of $\ell_P$, $\ell_{V5}$, $R_H$, with the canon-internal value 1.7575 (Paper_096) suggesting an $O(1)$ outcome.

Natural dimensionless combinations:
$$\xi_{\mathrm{canonical}} \stackrel{?}{=} f\!\left( \frac{\ell_{V5}}{R_H}, \frac{\ell_{V5}}{\ell_P}, \alpha \right) ,$$
where $f$ is a substrate-derived RG-flow integral and $\alpha$ is any substrate-level coupling parameter.

**Dimensional consistency** requires $\xi_{\mathrm{canonical}}$ in lu to be dimensionless under any substrate-rescaling.

**Scaling constraints from RG:**
- Under $\ell \to \lambda \ell$, the fixed-point condition forces $\xi_{\mathrm{canonical}}$ to be a $\lambda$-invariant. P-S1-Invariant (Paper_096) makes this explicit.
- $H_0 \to H_0$ is fixed (cosmological-invariant, Paper_037 P-H0-Cosmological-Invariant); the boundary $R_H = c/H_0$ does not rescale under local DCGT coarse-graining.

So the structural constraint is: $\xi_{\mathrm{canonical}}$ must be a dimensionless combination of substrate-scale and cosmological-scale anchors, invariant under substrate-side DCGT rescaling but **fixed** by the cosmological boundary.

### 3.4 Attempted derivation of $\xi_{\mathrm{canonical}}(H_0)$

The substrate RG flow on the interval $[\ell_P, R_H]$ has structural form
$$\frac{d K}{d \ln \xi} = \beta(K) ,$$
with $\beta(K)$ the substrate beta-function (Paper_097 three-regime). At the canonical operating point, $\beta(K(\xi_{\mathrm{canonical}})) = 0$ (fixed-point condition).

**Step 1 (form-FORCED):** $\xi_{\mathrm{canonical}}$ is a zero of $\beta$. From P-S1-Invariant, this zero exists; it is the **canonical** zero distinguished by cosmological-boundary anchoring.

**Step 2 (form-FORCED):** The boundary condition $K(\xi = R_H) = K_{\mathrm{boundary}}$ ties the RG flow to the cosmological scale.

**Step 3 (attempted derivation):** The fixed-point equation
$$\beta(K(\xi_{\mathrm{canonical}})) = 0$$
combined with the boundary condition + the substrate-cosmology unification (P-Substrate-Cosmology-Unified) should produce a **value** for $\xi_{\mathrm{canonical}}$ in lu.

**Step 4 (where it fails to close):** Solving the fixed-point equation requires:
- (i) The explicit functional form of $\beta(K)$ from substrate primitives.
- (ii) The boundary value $K_{\mathrm{boundary}}$ at $R_H$.
- (iii) The substrate-level relation between $\ell_{V5}$ and $H_0$.

**None of (i), (ii), (iii) are currently derived from substrate primitives** at the corpus's M1 (FORCED-unconditional) level. They are:

- (i): $\beta(K)$ form is currently **inherited** from Paper_097's three-regime RG via canon-internal RG matching; not derived from V1+V5 kernel data explicitly.
- (ii): $K_{\mathrm{boundary}}$ at the cosmological boundary requires a substrate-derived cosmological-boundary kernel value; this would be a Paper_098-class derivation that has not been performed.
- (iii): $\ell_{V5}(H_0)$ — the substrate-cosmology coupling relating V5 bandwidth scale to cosmological rate — is **not** in the corpus. This is the most load-bearing missing input.

The derivation therefore produces a **structural setup**: $\xi_{\mathrm{canonical}}$ is a fixed point of substrate RG flow anchored at $R_H = c/H_0$. The **value** depends on a substrate-cosmology coupling parameter that is OPEN.

### 3.5 Failure modes

Three explicit failure modes for the derivation:

**Failure mode 1: $\beta(K)$ form not derivable.** The substrate beta-function in Paper_097 is canon-internal-inherited at the 0.6 transition exponent. If $\beta(K)$ admits multiple substrate-consistent forms (each producing different $\xi_{\mathrm{canonical}}$ values), the derivation has no unique closure.

**Failure mode 2: $K_{\mathrm{boundary}}$ at $R_H$ ambiguous.** The substrate-cosmology boundary kernel value $K_{\mathrm{boundary}}$ is a single number characterizing the SCBU object at the cosmological projection. If multiple boundary values are admissible under SCBU, the fixed-point equation has multiple solutions and the derivation fails to single out one.

**Failure mode 3: $\ell_{V5}(H_0)$ relation absent.** This is the most load-bearing failure. Without a substrate-derived relation between V5 bandwidth and $H_0$, the dimensional combination $\ell_{V5}/R_H$ has no first-principles value, and $\xi_{\mathrm{canonical}}$ in lu remains canon-internal-inherited.

A constructive closure of the derivation would require either:
- **(Route A)** Deriving $\ell_{V5}(H_0)$ from substrate primitives (likely from substrate-cosmology coupling at the SCBU object level). This is the highest-impact missing derivation.
- **(Route B)** Deriving $\beta(K)$ from V1+V5 kernel data quantitatively (this would also fix the canon-internal 0.6 transition exponent of Paper_097).
- **(Route C)** Deriving $K_{\mathrm{boundary}}$ at $R_H$ from SCBU structural content + Paper_087 primitives.

Routes A, B, C are mutually consistent goals; closing any one would reduce the derivation's remaining OPEN content.

### 3.6 Partial results

The derivation does **not** close, but supplies the following partial results:

**Partial Result 1 (FORM-FORCED).** $\xi_{\mathrm{canonical}}$ is a fixed point of substrate RG flow on the interval $[\ell_P, R_H]$. Existence of at least one fixed point follows from P-S1-Invariant + continuity (P-Cascade-Continuity).

**Partial Result 2 (FORM-FORCED).** The canonical fixed point is distinguished by **cosmological-boundary anchoring**: among possible fixed points of $\beta(K)$, the canonical one is the fixed point selected by the boundary condition at $R_H$.

**Partial Result 3 (FORM-FORCED).** $\xi_{\mathrm{canonical}}$ has dimensional content $f(\ell_{V5}/R_H, \ell_{V5}/\ell_P, \alpha)$ for some substrate-derived function $f$. The function form is not derived in this paper.

**Partial Result 4 (FORM-FORCED + VALUE-INHERITED).** The canon-internal value 1.7575 lu (Paper_096) is consistent with the fixed-point structure but cannot be derived from primitives without closing Routes A, B, or C.

**Partial Result 5 (structural):** If $H_0$ varies (e.g., between local-universe and early-universe measurements, addressing the Hubble tension), the SCBU framework predicts that $\xi_{\mathrm{canonical}}$ **co-varies** with $H_0$ through the cosmological boundary anchor $R_H = c/H_0$. This is a **testable structural prediction** of the framework, even without closing the value-derivation.

### 3.7 Summary: what is FORM-FORCED vs VALUE-INHERITED

| Content | Status |
|---|---|
| $\xi_{\mathrm{canonical}}$ is a fixed point of substrate RG flow | FORM-FORCED |
| Canonical fixed point distinguished by cosmological-boundary anchoring | FORM-FORCED (via SCBU + Paper_ED_SC_4.1) |
| $\xi_{\mathrm{canonical}} = f(\ell_{V5}/R_H, \ell_{V5}/\ell_P, \alpha)$ dimensional form | FORM-FORCED |
| Specific $\beta(K)$ form | OPEN (Route B) |
| Boundary value $K_{\mathrm{boundary}}$ at $R_H$ | OPEN (Route C) |
| $\ell_{V5}(H_0)$ substrate-cosmology coupling | OPEN (Route A; highest impact) |
| Numerical value $\xi_{\mathrm{canonical}} = 1.7575$ lu | VALUE-INHERITED (canon-internal; not derived) |
| $\xi_{\mathrm{canonical}}$ co-varies with $H_0$ (structural prediction) | FORM-FORCED — testable |

**Verdict tier:** M3 (FORM-FORCED structural setup + VALUE-INHERITED numerical content). Upgrade to M2 requires closing Routes A, B, or C; upgrade to M1 requires no additional postulates beyond Paper_087 primitives + Paper_SCBU.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | 13 primitives posited per Paper_087 | P (axiomatic) | Substrate ontology. |
| 2 | P-Substrate-Cosmology-Unified | I | Paper_SCBU. |
| 3 | P-S1-Invariant cross-scale invariance | I | Paper_096. |
| 4 | P-Cascade-Continuity | I | Paper_091. |
| 5 | Cosmic decoupling $R_H = c/H_0$ | I | Paper_028. |
| 6 | $a_0 = c H_0/(2\pi)$ azimuthal-Fourier signature | I | Paper_029. |
| 7 | Kernel cascade structure | I | Paper_091. |
| 8 | Three-regime RG | I | Paper_097. |
| 9 | BH ↔ cosmic boundary projection | I | Paper_ED_SC_4.1. |
| 10 | $\xi_{\mathrm{canonical}}$ as fixed point of substrate RG flow | D-via-I | §3.1: composition of P-S1-Invariant + RG machinery. |
| 11 | RG flow on interval $[\ell_P, R_H]$ | D | §3.2: structural setup. |
| 12 | Fixed-point equation $\beta(K(\xi_{\mathrm{canonical}})) = 0$ | D | §3.4 Step 1. |
| 13 | Cosmological-boundary anchoring distinguishes canonical fixed point | D-via-I | §3.4 Step 2. |
| 14 | $\xi_{\mathrm{canonical}} = f(\ell_{V5}/R_H, \ell_{V5}/\ell_P, \alpha)$ dimensional form | D | §3.3. |
| 15 | Specific $\beta(K)$ functional form | OPEN (Route B) | §3.5 failure mode 1. |
| 16 | $K_{\mathrm{boundary}}$ at $R_H$ | OPEN (Route C) | §3.5 failure mode 2. |
| 17 | $\ell_{V5}(H_0)$ substrate-cosmology coupling | OPEN (Route A; highest-impact) | §3.5 failure mode 3. |
| 18 | Numerical $\xi_{\mathrm{canonical}} = 1.7575$ lu | I | Canon-internal; not derived. |
| 19 | Structural prediction: $\xi_{\mathrm{canonical}}$ co-varies with $H_0$ | D-via-I | §3.6 Partial Result 5. |
| 20 | Derivation outcome | A→position | Outcome-Open: structural setup supplied, numerical closure OPEN. |
| 21 | Verdict tier M3 (no upgrade in this paper) | A→position | §3.7. |
| 22 | Upgrade path: closing Routes A, B, or C | OPEN | Future ED-SC 4.x work. |

---

## §5 Falsification Criteria

- **F1: $\xi_{\mathrm{canonical}}$ empirically independent of $H_0$.** If empirical / structural evidence shows that $\xi_{\mathrm{canonical}}$ does NOT co-vary with $H_0$ (e.g., the canon-internal 1.7575 lu value remains identical under $H_0$ variation between early-universe and local-universe), then the cosmological-boundary anchoring (§3.2 + §3.4) fails. This refutes the SCBU-projection structure for $\xi_{\mathrm{canonical}}$.

- **F2: Fixed-point equations inconsistent with kernel cascade.** If a substrate-level derivation of $\beta(K)$ from V1+V5 kernel data (Route B) produces a $\beta$-function with no zero in $[\ell_P, R_H]$ — or with zeros at points incompatible with the canon-internal $\xi_{\mathrm{canonical}}$ value — then the fixed-point setup fails. The structural setup of §3.1–§3.2 collapses.

- **F3: SCBU postulate refuted.** If P-Substrate-Cosmology-Unified (Paper_SCBU) is refuted by an independent substrate-level derivation, this paper's cosmological-boundary anchoring step (§3.2) loses its inheritance and the derivation attempt has no anchor.

- **F4: Discontinuity in RG regime at cosmological scale.** P-Cascade-Continuity (Paper_091) requires the RG flow to be continuous from the hydrodynamic regime through the cosmological-boundary regime. A substrate-level discontinuity at the cascade-to-cosmology transition would refute the boundary-condition setup (§3.2 + §3.4 Step 2).

- **F5: Independent derivation contradicts this paper's structure.** If a substrate-level derivation of $\xi_{\mathrm{canonical}}$ closing Route A, B, or C produces a value of $\xi_{\mathrm{canonical}}$ **inconsistent** with the canon-internal 1.7575 lu, then the canon-internal matching of Paper_096 is wrong, and this paper's setup (which assumes 1.7575 lu as consistent target) needs revision. (This is a "successful derivation that disagrees" failure mode — note that a successful derivation that **agrees** with 1.7575 lu would upgrade the verdict to M2, not refute the paper.)

---

## §6 Rewrite Note

**Derivation outcome.** The derivation **did not close** at the first-principles level. The structural setup is established — $\xi_{\mathrm{canonical}}$ is a fixed point of substrate RG flow anchored at the substrate-cosmology boundary $R_H = c/H_0$ — but three substrate-derived inputs are missing (Routes A, B, C in §3.5). Without these, the canon-internal value 1.7575 lu remains INHERITED, not derived.

**Implications for SCBU verdict.** The SCBU synthesis (Paper_SCBU) remains at **M3** (FORM-FORCED + VALUE-INHERITED). This paper does not upgrade to M2 because it does not close the substrate-cosmology coupling parameter (Route A) or the $\beta(K)$ functional form (Route B) or the boundary value $K_{\mathrm{boundary}}$ (Route C).

**Closing one of Routes A, B, C upgrades the verdict** (standardized convention):

- **Closing Route A** ($\ell_{V5}(H_0)$ derivation) propagates to an arc-wide **M3 → M2** upgrade. Route A supplies the substrate-cosmology coupling parameter that grounds $\xi_{\mathrm{canonical}}$'s numerical content in $H_0$ directly. This is the highest-impact closure target.

- **Closing Route B** ($\beta(K)$ derivation) supplies the RG-flow functional form; combined with cosmological-boundary anchoring, contributes to closure. Verdict upgrade: M3 → M2.

- **Closing Route C** ($K_{\mathrm{boundary}}$ derivation) supplies the boundary value. Verdict upgrade: M3 → M2.

- **Closing all three Routes A + B + C simultaneously without additional postulates** propagates to an arc-wide **M3 → M1** upgrade. This would be the first cross-arc M1 result in the corpus.

The standardized verdict-upgrade convention (single Route → M2, all three Routes + no new postulates → M1) is used uniformly across the ED-SC 4.x arc.

**Position in ED-SC 4.x roadmap.** This paper is the **second** ED-SC 4.x extension paper, following Paper_ED_SC_4.1 (BH horizon ↔ cosmic decoupling surface projection). It identifies the **highest-impact open derivation** in the ED-SC 4.x program: the substrate-cosmology coupling $\ell_{V5}(H_0)$ (Route A). Subsequent ED-SC 4.x papers (in queue) should target Route A as the priority.

**Testable structural prediction supplied.** Even without closing the numerical derivation, §3.6 Partial Result 5 supplies a **testable structural prediction**: $\xi_{\mathrm{canonical}}$ co-varies with $H_0$ under SCBU. If observations of the canon-internal operating point at different epochs (or under Hubble-tension-class $H_0$ variations between early and local universe) detect a co-variation tracking $H_0$ shifts, this is structural confirmation of the SCBU extension. Conversely, $H_0$-independence of $\xi_{\mathrm{canonical}}$ refutes the structural setup (F1).

**Numerical content.** $\xi_{\mathrm{canonical}} = 1.7575$ lu remains **INHERITED** (canon-internal from Paper_096 ED-SC 3.3.x closure). FORM-FORCED structural setup supplied; VALUE-INHERITED numerical content unchanged. Verdict: **M3**.

**Future ED-SC 4.x work.** Priority order for closure:
1. **Route A** ($\ell_{V5}(H_0)$ substrate-cosmology coupling) — highest impact; potential M1 outcome.
2. **Route B** ($\beta(K)$ from V1+V5 data) — moderate impact; also closes Paper_097 0.6 exponent.
3. **Route C** ($K_{\mathrm{boundary}}$ at $R_H$) — moderate impact; requires SCBU-level boundary kernel-value derivation.

**Honest framing.** This paper is the structural-positive substrate-level fixed-point setup for $\xi_{\mathrm{canonical}}(H_0)$. It does not deliver a first-principles value. It identifies precisely where the closure must happen and what structural inputs are missing. This is the M3-honest outcome for the highest-leverage ED-SC 4.x paper.

---

**End Paper ED-SC 4.2.**
