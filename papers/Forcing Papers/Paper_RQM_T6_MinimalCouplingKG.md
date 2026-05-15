# Paper RQM-T6 — Minimal-Coupling Klein–Gordon + Conserved 4-Current

**Series:** Wave-3 Relativistic-QM Bridge — Theorem T6
**Status:** Wave-3 generative paper; M3 verdict at write-time. FORM-INHERITED conditional on Paper_015 + Paper_016.
**Companions:** Paper_RQM_T5 (KG), Paper_RQM_T4 (Dirac), Paper_015 (T17 gauge fields), Paper_016 (minimal-coupling from T17 + DCGT).

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 primitives are not derived.** They are postulated per Paper_087.
2. **No claim that the minimally-coupled KG equation form is derived in this paper.** Per Paper_095 §2.3, writing down the gauge-covariant derivative $D_\mu = \partial_\mu + iqA_\mu$ and the minimally-coupled KG operator is P (definitional standard-form construction). The form is INHERITED from Paper_015 T17 + Paper_016 generalized minimal coupling.
3. **No claim of numerical-content derivation beyond what is explicitly INHERITED.** Specific coupling constants ($q$, gauge couplings) are INHERITED via empirical matching.
4. **No claim that the §3.5 V5 multi-channel substrate-graph derivation is closed.** §3.5 invokes V5 cross-chain content (Paper_090 inheritance) but the substrate-graph-to-multi-channel-coupling derivation is OPEN.
5. **No claim that ED is the only consistent substrate ontology.** Other substrate ontologies are conceivable.
6. **No claim of empirical adequacy outside the regime stated in §2.2.** Non-Abelian extension explicit in Paper_018 / Paper_023; this paper covers $U(1)$ only.

---

## Abstract

Paper RQM-T6 establishes the minimally-coupled Klein–Gordon equation $(D^\mu D_\mu + m^2c^2/\hbar^2)\Psi = 0$ with conserved 4-current $j^\mu$ for scalar rule-types interacting with a $U(1)$ gauge connection. **The minimal-coupling form is INHERITED** from Paper_015 (T17 gauge fields as rule-type bundle connections) + Paper_016 (generalized minimal coupling from T17 + DCGT) + Paper_095 §2.3 (standard-form construction is P-definitional). The substrate-level contribution of this paper is the extension of KG (T5) to gauge-coupled scalar sector under inherited T17 + DCGT machinery; current-conservation $\partial_\mu j^\mu = 0$ follows by Noether's theorem from $U(1)$ phase invariance. Coupling constants are VALUE-INHERITED. Verdict tier: **M3** with FORM-INHERITED framing. §3.5 V5 multi-channel substrate-graph derivation flagged OPEN. The result joins the Wave-3 Relativistic-QM Bridge family as the gauge-interaction companion to T5 (free scalar KG), parallel to Dirac-minimal-coupling, and extended via Paper_018 / Paper_023 to non-Abelian gauge groups. This paper is in the substrate-ontology research-program lineage of 't Hooft, Wolfram, and the causal-set program — not in the operational-reconstruction lineage of Hardy / CDP / Coecke-Kissinger.

---

## §1 Statement of Result

**Claim.** The minimally-coupled Klein–Gordon equation
$$(D^\mu D_\mu + m^2c^2/\hbar^2)\Psi = 0 , \qquad D_\mu = \partial_\mu + i(q/\hbar) A_\mu ,$$
together with a conserved electromagnetic-class 4-current
$$j^\mu = \frac{iq\hbar}{2m}\big[\Psi^* (D^\mu \Psi) - (D^\mu \Psi)^* \Psi\big] , \qquad \partial_\mu j^\mu = 0 ,$$
is form-IDENTIFIED (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3) for scalar rule-types interacting with a $U(1)$ gauge connection (Paper_015 T17). The minimal-coupling substitution $\partial_\mu \to D_\mu$ is form-IDENTIFIED by V1 kernel polarity-transport content (P05) + T17 gauge-bundle structure. The current-conservation $\partial_\mu j^\mu = 0$ follows by Noether's theorem from $U(1)$ phase invariance.

Coupling constants ($q$, gauge coupling $e$) are INHERITED via empirical matching.

Verdict: **M3**. No new postulates.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P05 (Polarity-transport along edges)** — supplies the substrate-level transport whose coarse-graining yields the gauge-covariant derivative.
- **P09 ($U(1)$-valued polarity)** — supplies the $U(1)$ gauge group.
- **P10 (Rule-type primitive)** — scalar rule-type carrier + gauge rule-type (T17).
- **P11 (Commitment-irreversibility)** — supplies direction for V1 retardation in current conservation.

### 2.2 Upstream Dependencies

- **I-015:** T17 gauge fields as rule-type bundle connections (Paper_015).
- **I-016:** Generalized minimal coupling from T17 + DCGT (Paper_016).
- **I-073:** DCGT (Paper_073).
- **I-089:** V1 kernel (Paper_089).
- **I-RQM-T5:** Klein–Gordon equation.
- **I-Noether:** Standard Noether's theorem (standard math).
- **I-MC:** Standard minimal-coupling prescription (standard physics).

---

## §3 Derivation

### 3.1 The minimal-coupling substitution

By T17 (Paper_015), gauge fields $A_\mu$ are connections on rule-type bundles. By Paper_016 (generalized minimal coupling from T17 + DCGT), the substrate-level coupling between a scalar rule-type and a $U(1)$ gauge rule-type takes the form: in regions where the gauge connection is nontrivial, the substrate's polarity-transport (P05) of the scalar amplitude $\Psi$ acquires an additional rotation given by $A_\mu \, dx^\mu$.

Under coarse-graining via DCGT (Paper_073), this substrate-level rotation manifests as the standard minimal-coupling substitution:
$$\partial_\mu \Psi \to D_\mu \Psi = (\partial_\mu + i(q/\hbar) A_\mu)\Psi ,$$
where $q$ is the rule-type's coupling charge (INHERITED via empirical matching).

The substrate-level origin of the $i(q/\hbar)$ prefactor: $q/\hbar$ is the rate at which substrate polarity rotates per unit $A_\mu \, dx^\mu$. By P09 ($U(1)$-valued polarity), this rotation is $U(1)$-valued; by P05 polarity-transport, it accumulates along the substrate-edge content underlying $dx^\mu$.

### 3.2 Minimally-coupled KG equation

Replacing $\partial_\mu$ with $D_\mu$ in the KG equation (Paper_RQM_T5):
$$(\partial_\mu \partial^\mu + m^2c^2/\hbar^2)\Psi = 0 \quad \longrightarrow \quad (D_\mu D^\mu + m^2c^2/\hbar^2)\Psi = 0 .$$

Expanding $D_\mu D^\mu$:
$$D_\mu D^\mu = \partial_\mu \partial^\mu + i(q/\hbar)(\partial_\mu A^\mu + A^\mu \partial_\mu) - (q/\hbar)^2 A_\mu A^\mu .$$

The substrate-level claim: this is the equation governing scalar rule-type evolution in the presence of a $U(1)$ gauge background, derived as the natural extension of KG (T5) under T17 gauge-bundle structure.

### 3.3 Gauge invariance

Under a $U(1)$ gauge transformation
$$\Psi \to e^{i\alpha(x)}\Psi , \qquad A_\mu \to A_\mu - (\hbar/q)\partial_\mu \alpha(x) ,$$
the gauge-covariant derivative transforms covariantly:
$$D_\mu \Psi \to e^{i\alpha(x)} D_\mu \Psi ,$$
and the minimally-coupled KG equation is invariant.

This is the standard $U(1)$ gauge invariance. The substrate-level origin: P09's $U(1)$ polarity structure is global; the gauge transformation is the substrate-level local-phase rotation under which T17 rule-type bundles transform consistently.

### 3.4 Conserved 4-current via Noether

The minimally-coupled KG action
$$S = \int d^4x \big[ (D^\mu \Psi)^* (D_\mu \Psi) - (m^2c^2/\hbar^2)|\Psi|^2 \big]$$
has $U(1)$ global symmetry $\Psi \to e^{i\alpha}\Psi$ (with constant $\alpha$). By Noether's theorem (I-Noether), this symmetry implies a conserved 4-current.

The conserved current is:
$$j^\mu = \frac{iq\hbar}{2m}\big[\Psi^* (D^\mu \Psi) - (D^\mu \Psi)^* \Psi\big] .$$

Conservation $\partial_\mu j^\mu = 0$ follows directly from the KG equation + its complex conjugate (standard calculation).

This is the **conserved electromagnetic-class 4-current** for the scalar rule-type. Substrate origin: $U(1)$ phase invariance + V1 kernel retardation (P11) supplies the conservation law.

### 3.5 V1 / V5 kernel content in current conservation

The conservation $\partial_\mu j^\mu = 0$ is locally derived. At substrate level, the kernel content underlying the gauge-covariant derivative is V1 (within-channel propagation with $U(1)$-rotated polarity) supplemented by V5 cross-chain correlation where multi-channel coupling matters.

In the canonical scalar-KG sector (single channel), V5 is not load-bearing; V1 + T17 gauge connection suffice. In multi-component scalar sectors (e.g., complex scalar fields with internal symmetries beyond $U(1)$), V5 enters to maintain conservation across channels.

### 3.6 Coupling constant inheritance

The charge $q$ in $D_\mu$ is INHERITED:
- Electron charge: $q = -e \approx -1.6 \times 10^{-19}$ C.
- Quark charges: $\pm e/3, \pm 2e/3$.
- Scalar field coupling to photon: per-model.

The substrate framework does not derive $q$ from first principles. The substrate-level claim is the **form** of the minimal coupling, not the coupling magnitude.

### 3.7 Generalization to non-Abelian

For non-Abelian gauge group $G$, the minimal coupling becomes
$$D_\mu = \partial_\mu + i g A_\mu^a T^a ,$$
with $T^a$ Lie-algebra generators. The substrate origin extends via Paper_016 (non-Abelian generalization of T17 + DCGT) and Paper_RQM_T7 (Lorentz reps for non-Abelian gauge rule-types).

The conserved current generalizes to the gauge-covariant current $J^{\mu, a}$ with covariant conservation $D_\mu J^{\mu, a} = 0$.

This is beyond the scope of T6 ($U(1)$ case); see Paper_018 (YM non-Abelian) and Paper_023 (YM Clay synthesis) for the full non-Abelian extension.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P05 polarity-transport | P | Primitive. |
| 2 | P09 $U(1)$-valued polarity | P | Primitive. |
| 3 | P10 scalar rule-type + gauge rule-type | P | Primitive. |
| 4 | T17 gauge fields as rule-type bundle connections | I | Paper_015. |
| 5 | Generalized minimal coupling from T17 + DCGT | I | Paper_016. |
| 6 | Klein–Gordon equation for scalar rule-type | I | Paper_RQM_T5. |
| 7 | Minimal-coupling substitution $\partial_\mu \to D_\mu$ | I | Inherited from Paper_015 + Paper_016 (gauge structure). |
| 8 | Minimally-coupled KG equation form | P | Standard-form construction per Paper_095 §2.3 (definitional). |
| 9 | $U(1)$ gauge invariance | I | Standard math + T17. |
| 10 | $U(1)$ phase invariance Noether theorem | I | Standard math (I-Noether). |
| 11 | Conserved 4-current $j^\mu$ form | P | Standard-form construction per Paper_095 §2.3 (the Noether-current expression is definitional). |
| 12 | $\partial_\mu j^\mu = 0$ conservation | P | Standard-form construction; conservation follows directly from KG + complex conjugate (definitional, not substrate-derived here). |
| 13 | Coupling constant $q$ | I | Empirical / standard matching. |
| 14 | Specific particle charges | I | Empirical. |
| 15 | Non-Abelian extension | I | Paper_018, Paper_023. |
| 16 | V5 substrate-graph multi-channel construction supporting non-Abelian extension | OPEN | §3.5 invokes V5 cross-chain content (Paper_090 inheritance) but the substrate-graph-to-multi-channel-coupling derivation is not closed in this paper. |

---

## §5 Falsification Criteria

- **F1: Empirical detection of charged scalar particle NOT obeying minimally-coupled KG.** Would refute the substrate-coupling identification.

- **F2: Substrate evidence that T17 + DCGT does NOT produce the standard minimal-coupling substitution $\partial_\mu \to D_\mu$.** Would refute Paper_016 application here.

- **F3: This falsifier is structural rather than empirical** — refutation would require a substrate-level inconsistency proof rather than experimental measurement: any demonstration that $U(1)$ phase invariance fails to produce a conserved Noether current would contradict standard math and propagate.

- **F4: Substrate Lorentz covariantization (Paper_017) shown to be incompatible with $U(1)$ gauge invariance in scalar sector.** Would propagate.

---

## §6 Position Statement

Paper RQM-T6 establishes the minimally-coupled KG equation + conserved 4-current as **M3** with **FORM-INHERITED** framing: the minimal-coupling substitution $\partial_\mu \to D_\mu$ and the gauge-covariant KG operator are INHERITED from Paper_015 (T17 gauge fields) and Paper_016 (generalized minimal coupling from T17 + DCGT); the Noether-current expression is P-definitional per Paper_095 §2.3. **Paper_016 is doing load-bearing inheritance work**: this paper extends Paper_016's $U(1)$ minimal-coupling content to the KG scalar sector but does not reprove Paper_016. Coupling constants are VALUE-INHERITED. No new postulates.

This paper does NOT derive the minimal-coupling form from substrate primitives — it is INHERITED. It does NOT close the §3.5 V5 multi-channel substrate-graph derivation (flagged OPEN in audit row 16). It does NOT extend to non-Abelian groups (Paper_018 / Paper_023).

The result joins the Wave-3 Relativistic-QM Bridge family as the gauge-interaction companion to T5 (free scalar KG), parallel to spinor minimal-coupling (deferred to Dirac-EM parallel paper).

This paper is in the Wave-3 Relativistic-QM Bridge series of the Event Density program — a substrate-ontology research program in the lineage of 't Hooft's cellular-automaton interpretation, Wolfram's Ruliad, and the causal-set program (Sorkin et al.); NOT in the operational-reconstruction lineage of Hardy / CDP / Coecke-Kissinger.

---

## §7 Rewrite Note

This paper completes the scalar-rule-type interaction sector of the relativistic-QM bridge: T5 supplies the free-scalar KG equation; T6 supplies the gauge-coupled version + conserved current.

**Relationship to other RQM-bridge papers:**
- **T5 KG:** the free-scalar starting point.
- **T4 Dirac:** the analogous first-order equation for spinor rule-types; minimal-coupling extends Dirac similarly.
- **T7 Lorentz reps:** classifies scalar + gauge rule-types whose interaction is described here.
- **Paper_015 T17 + Paper_016:** supply the substrate-level gauge-coupling content this paper inherits.

**Numerical content INHERITED.** Coupling constants $q$. **Form IDENTIFIED.** Minimally-coupled KG equation form + Noether-conserved 4-current (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3).

**Future work.** Non-Abelian extension explicit in Paper_018/Paper_023; spinor minimal coupling (Dirac in electromagnetic field) is a parallel paper, deferred. Conservation in V5-modulated multi-channel scalars OPEN at quantitative level.

Verdict: **M3**.

---

**End Paper RQM-T6.**
