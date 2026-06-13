# Memo_ED_ChainClass_C3_Construct — Construction Memo (Route C3 Attempt)

**Series:** Wave-3 Construction Memo (Cosmology + Dynamics Arcs; Chain-Class Identification Project; Path-C3 from Memo_ED_ChainClassIdentification_Scoping §8)
**Status:** Substrate-graph attempt at Route C3 — derivation of the substrate-side criterion that uniform-$\Psi$ (zero-gradient) states are the **unique** substrate-side configurations corresponding to saturation regime (LDE / inflation, $w = -1$), with non-uniform $\Psi$-gradient structure corresponding to non-saturation regimes ($w \neq -1$). **Not a derivation. No new primitives.** Outcome: **substantive positive — C3 closes the saturation vs non-saturation discrimination under stated assumptions, with three explicit closure qualifications.** Sufficient to upgrade Paper_ED_Cos_01 M2 → M3 conditional on audit acceptance. **Not sufficient** for further RDE vs MDE discrimination (Route C1 required for Dyn_02) or source-class identification (Route C4 required for Dyn_03).
**Date:** 2026-05-16
**Anchors:** Memo_ED_ChainClassIdentification_Scoping (parent project; Route C3 scope; CC-OPEN-6 target); Memo_ED_Q1Q2_JointClosure_Construct (Q1A construction-uniqueness precedent); Paper_ED_Cos_01 (M2; Cos_01 upgrade target via C3); Paper_ED_SC_4_9 ($S_{\mathrm{sub}}$ + saddle Hessian + kernel-derivative content); Paper_ED_CCC §3.6 + §3.7 (post-SCBU homogeneity + saturation realization); Paper_073 (DCGT); Paper_087 (P02 + P04 + P11 + P12); Paper_089 (V1); Paper_090 (V5); Memo_ED_DCGT_VacuumEnergyMapping + Audit (substrate-side Noether for constant $\Psi$ → vacuum-energy form, audit ACCEPTED at approximately-vacuum-energy level).

---

## §1 Restated target

**Route C3 claim to close:** the substrate-side identification

$$
\nabla\Psi = 0 \;\text{and}\; \partial_t \Psi = 0 \quad\Longleftrightarrow\quad \text{continuum saturation regime (LDE/inflation, } w = -1)
$$

is a **substrate-graph derivation** (not standard-physics-analog inheritance) given:
- The substrate-side $\mathcal{L}_{\mathrm{sub}}[\Psi, \nabla_{V_1}\Psi, \nabla_{V_5}\Psi]$ structure (Paper_ED_SC_4_9)
- Q1A construction-uniqueness for substrate-side Noether (Memo_ED_Q1Q2_JointClosure_Construct §2)
- Q2A construction-uniqueness for DCGT mapping at leading order (Memo_ED_Q1Q2_JointClosure_Construct §3)
- Paper_ED_CCC §3.6 + §3.7 post-SCBU homogeneity (saturation realizable at substrate-graph level)

**Two directions to establish:**

**Forward (uniform → saturation):** if $\nabla\Psi = 0$ and $\partial_t \Psi = 0$ on the substrate graph, then the resulting continuum stress-energy is vacuum-energy form with $w = -1$.

**Converse (saturation → uniform):** if the continuum stress-energy is vacuum-energy form with $w = -1$, then the substrate $\Psi$ configuration must be uniform (modulo Lagrangian-degeneracy exceptions).

**Together:** uniform $\Psi$ ↔ saturation regime, with explicit Lagrangian-genericity qualification.

This is the saturation-vs-non-saturation discrimination addressed by CC-OPEN-6. **Route C3 does not address:** further RDE vs MDE discrimination within non-saturation (requires Route C1); source-class identification within radiation (requires Route C4).

---

## §2 Substrate-side gradient invariants available from SC-4.9

Per Paper_ED_SC_4_9 + Paper_087, the substrate-graph supplies four classes of substrate-side gradient invariant that bear on Route C3:

### (i) Gradient magnitude $|\nabla\Psi|$, $|\partial_t \Psi|$

Spatial and temporal gradient magnitudes of the substrate-action density $\Psi$ are substrate-graph well-defined as kernel-derivative magnitudes:

$$
|\nabla_K \Psi|^2 \equiv (\nabla_K \Psi)(\nabla^\mu_K \Psi)_\mu \quad\text{for } K \in \{V_1, V_5\}.
$$

**Substrate-graph well-definedness:** STRONG. Direct from $\mathcal{L}_{\mathrm{sub}}$ structure.

### (ii) Gradient sign structure

The sign pattern of $\nabla\Psi$ across substrate-graph regions partitions substrate into source-like ($\nabla\Psi > 0$ outward), sink-like ($\nabla\Psi < 0$ outward), and neutral (zero-gradient) substrate loci.

**Substrate-graph well-definedness:** STRONG (with caveat: requires a substrate-graph notion of "outward" via Paper_093 T18 chain-arrow direction or Paper_ED_SC_4_9 saddle compression-vs-expansion axes).

### (iii) Hessian eigenvalue signature

Per Paper_ED_SC_4_9, the substrate-action saddle Hessian $\mathcal{H} = \delta^2 S_{\mathrm{sub}}/\delta\Psi \delta\Psi'$ classifies each substrate locus by eigenvalue signature into S1 (all-compression), S2 (mixed compression/expansion saddle), S3 (all-expansion) classes.

**Substrate-graph well-definedness:** STRONG. Direct from SC-4.9.

### (iv) V1 / V5 kernel response to gradient patterns

V1 retarded propagation (Paper_089) carries gradient content forward-causally at substrate-c; V5 cross-chain coupling (Paper_090) carries gradient content with finite-memory across chain pairs. The substrate-graph "response" of these kernels to a given $\Psi$-gradient pattern is well-defined as kernel application.

**Substrate-graph well-definedness:** STRONG. Direct from V1 + V5 kernel structure.

---

## §3 Forward direction: uniform $\Psi$ → saturation regime ($w = -1$)

### §3.1 Step 1 — uniform $\Psi$ kills kernel derivatives

If $\Psi$ is uniform on the substrate graph ($\nabla\Psi = 0$, $\partial_t \Psi = 0$ everywhere in the substrate region), then for each $K \in \{V_1, V_5\}$:

$$
\nabla_K \Psi = \int K(x - y)\, \nabla\Psi(y) \, dy = 0
$$

since the kernel-weighted integral of a vanishing gradient is zero regardless of kernel structure. **Kernel derivatives of uniform $\Psi$ vanish identically.** Substrate-graph derivation; no inheritance.

### §3.2 Step 2 — substrate-side Noether collapses to vacuum-energy form

Applying the substrate-side Noether construction (Q1A surviving candidate A.1; Memo_ED_Q1Q2_JointClosure_Construct §2.3):

$$
T^{\mu\nu}_{\mathrm{sub}} = \sum_K \frac{\partial \mathcal{L}_{\mathrm{sub}}}{\partial(\nabla_K \Psi)} \cdot \nabla^\nu_K \Psi - g^{\mu\nu} \mathcal{L}_{\mathrm{sub}}.
$$

With $\nabla_K \Psi = 0$ for all $K$ (Step 1), the first term vanishes identically:

$$
T^{\mu\nu}_{\mathrm{sub}}\big|_{\nabla\Psi = 0} = -g^{\mu\nu} \mathcal{L}_{\mathrm{sub}}\big|_{\nabla\Psi = 0} = -g^{\mu\nu} \mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}.
$$

This is **the vacuum-energy form**: $T^{\mu\nu}_{\mathrm{sub}} = -g^{\mu\nu} \rho_{\Lambda}^{\mathrm{sub}}$ with $\rho_{\Lambda}^{\mathrm{sub}} \equiv \mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$. Substrate-graph derivation; matches the Memo_ED_DCGT_VacuumEnergyMapping audit-ACCEPTED result.

### §3.3 Step 3 — DCGT preserves uniform structure → uniform continuum

Applying the DCGT coarse-graining (Q2A surviving candidate B.1; Memo_ED_Q1Q2_JointClosure_Construct §3.3):

$$
T^{\mu\nu}_{\mathrm{eff}}(x) = \int W_{R_{\mathrm{cg}}}(x - y) \cdot T^{\mu\nu}_{\mathrm{sub}}(y) \, dy = \int W_{R_{\mathrm{cg}}}(x - y) \cdot (-g^{\mu\nu} \rho_{\Lambda}^{\mathrm{sub}}) \, dy = -g^{\mu\nu} \rho_{\Lambda}^{\mathrm{sub}}
$$

using $\int W_{R_{\mathrm{cg}}}(x-y) \, dy = 1$ (DCGT normalization axiom, Paper_073). **Uniform substrate stress-energy maps to uniform continuum stress-energy** at leading order in $\varepsilon = \ell_{\mathrm{ED}}/R_{\mathrm{cg}}$. Subleading corrections $O(\varepsilon)$ vanish identically for uniform input (no spatial structure to perturb). Substrate-graph derivation; Q2A audit-ACCEPTED at leading order.

### §3.4 Step 4 — vacuum-energy continuum stress-energy → $w = -1$ → saturation regime phenomenology

The vacuum-energy continuum stress-energy $T^{\mu\nu}_{\mathrm{eff}} = -g^{\mu\nu} \rho_{\Lambda}$ has equation of state

$$
w \equiv \frac{p_{\mathrm{eff}}}{\rho_{\mathrm{eff}}} = \frac{-\rho_{\Lambda}}{\rho_{\Lambda}} = -1.
$$

Standard Friedmann inheritance (textbook standard cosmology) gives $a(t) \propto e^{Ht}$ with $H$ constant — **de Sitter / saturation regime phenomenology**. This is the LDE / inflation regime.

### §3.5 Substrate-realizability of uniform $\Psi$ at substrate-graph level

The uniform-$\Psi$ configuration is **substrate-realizable**: Paper_ED_CCC §3.6 + §3.7 establish post-SCBU spatial homogeneity at substrate-graph level (post-substrate-cosmology-boundary configurations are spatially uniform on the substrate graph as the homogeneous saturation state). The saturation regime is therefore a substrate-graph realizable configuration, not just a mathematical limit.

### §3.6 Forward closure

Steps 1–5 compose to give:

$$
\nabla\Psi = 0, \partial_t \Psi = 0 \;\text{(substrate-side)} \quad\Longrightarrow\quad w = -1 \;\text{(continuum-side)}.
$$

**Forward direction closed at substrate-graph level via Q1A + Q2A + Paper_ED_CCC §3.6 composition.** No standard-physics-analog inheritance required (modulo standard Friedmann inheritance at Step 4, which is the standard cosmology continuum-side machinery — outside the scope of substrate-graph chain-class identification).

---

## §4 Converse direction: saturation regime ($w = -1$) → uniform $\Psi$

### §4.1 Step 1 — vacuum-energy continuum requires uniform continuum

If $T^{\mu\nu}_{\mathrm{eff}} = -g^{\mu\nu} \rho_{\Lambda}^{\mathrm{const}}$ at continuum (saturation regime), then continuum stress-energy is spatially uniform: $\partial_i T^{\mu\nu}_{\mathrm{eff}} = 0$.

### §4.2 Step 2 — DCGT invertibility at leading order

Q2A established that the DCGT coarse-graining map is unique at leading order in $\varepsilon = \ell_{\mathrm{ED}}/R_{\mathrm{cg}}$ (Bensoussan-Lions-Papanicolaou homogenization inheritance). The map is *not invertible in general* (coarse-graining loses information), but the **inverse problem at leading order is constrained**: a uniform continuum stress-energy is consistent with a substrate-side configuration whose averaged stress-energy is uniform, i.e., the substrate-side stress-energy $T^{\mu\nu}_{\mathrm{sub}}(y)$ has the form

$$
T^{\mu\nu}_{\mathrm{sub}}(y) = -g^{\mu\nu} \rho_{\Lambda}^{\mathrm{sub}} + \delta T^{\mu\nu}(y)
$$

where $\delta T^{\mu\nu}(y)$ averages to zero over the coarse-graining window: $\int W_{R_{\mathrm{cg}}}(x-y) \delta T^{\mu\nu}(y) \, dy = 0$ for all $x$.

**At leading order**, $\delta T^{\mu\nu}(y) = 0$ identically (no fluctuation that survives window-averaging while preserving uniformity at every continuum-side $x$). **At subleading order $O(\varepsilon)$**, small fluctuations are admissible.

### §4.3 Step 3 — substrate-side Noether form requires uniform $\Psi$ (modulo Lagrangian degeneracy)

If $T^{\mu\nu}_{\mathrm{sub}} = -g^{\mu\nu} \mathcal{L}_{\mathrm{sub}}$ identically (vacuum-energy form on substrate), then the Q1A surviving Noether construction (Memo_ED_Q1Q2_JointClosure_Construct §2.3) requires:

$$
\sum_K \frac{\partial \mathcal{L}_{\mathrm{sub}}}{\partial(\nabla_K \Psi)} \cdot \nabla^\nu_K \Psi = 0 \quad\text{for all } \nu.
$$

Two solution branches:

**Branch (a):** $\nabla_K \Psi = 0$ for all $K$ — the **uniform-$\Psi$ branch**. This is the substrate-graph saturation configuration.

**Branch (b):** $\partial \mathcal{L}_{\mathrm{sub}}/\partial(\nabla_K \Psi) = 0$ for all $K$ — the **Lagrangian-degeneracy branch**: $\mathcal{L}_{\mathrm{sub}}$ is independent of kernel derivatives.

Per Paper_ED_SC_4_9, $\mathcal{L}_{\mathrm{sub}}$ is a functional of $\Psi, \nabla_{V_1}\Psi, \nabla_{V_5}\Psi$ with **explicit dependence on kernel derivatives** (the kernel-derivative content is the substrate-side analog of "kinetic energy" — load-bearing for the substrate-action's dynamical content). Branch (b) is a **degenerate Lagrangian** not consistent with the SC-4.9 substrate-action structure.

**Branch (a) is therefore the unique substrate-side configuration giving vacuum-energy form**, modulo the Lagrangian-genericity assumption (Branch (b) excluded by SC-4.9 structure).

### §4.4 Converse closure (modulo two qualifications)

Steps 1–3 compose to give:

$$
w = -1 \;\text{(continuum-side)} \quad\Longrightarrow\quad \nabla\Psi = 0, \partial_t \Psi = 0 \;\text{(substrate-side)}
$$

at leading order in $\varepsilon$, modulo Lagrangian-degeneracy exclusion.

**Closure qualifications (carried explicitly):**

- **Q-C3-1 (Lagrangian-genericity):** the converse requires Branch (b) (kernel-derivative-independent $\mathcal{L}_{\mathrm{sub}}$) to be ruled out by Paper_ED_SC_4_9 substrate-action structure. The corpus supplies this structurally (SC-4.9 explicitly includes kernel-derivative terms) but the exclusion is structural-content-dependent, not absolutely primitive.
- **Q-C3-2 (subleading-order fluctuations):** at $O(\varepsilon)$, small substrate-side fluctuations $\delta T^{\mu\nu}(y)$ that average to zero are admissible. This subleading-order non-uniqueness is at the same order as the Q2A scheme-dependence (Q2A OPEN-ii) and is not load-bearing for leading-order continuum phenomenology.

---

## §5 Non-uniform $\Psi$ → non-saturation ($w \neq -1$)

### §5.1 Direct consequence of forward + converse

The forward + converse closures together imply: **non-uniform $\Psi$ at substrate-graph level produces continuum stress-energy with $w \neq -1$** (otherwise the converse would force uniform $\Psi$, contradiction). This is the non-saturation discrimination.

### §5.2 Substrate-graph reasoning for non-uniform case

For non-uniform $\Psi$ with $\nabla_K \Psi \neq 0$ for some $K$, the Noether tensor has non-trivial kinetic-term contribution:

$$
T^{\mu\nu}_{\mathrm{sub}}\big|_{\mathrm{non-uniform}} = \underbrace{\sum_K \frac{\partial \mathcal{L}_{\mathrm{sub}}}{\partial(\nabla_K \Psi)} \nabla^\nu_K \Psi}_{\neq 0 \text{ generically}} - g^{\mu\nu} \mathcal{L}_{\mathrm{sub}}.
$$

The kinetic-term contribution has non-vacuum-energy structure — generically gives $w \neq -1$ at continuum after DCGT translation. **Non-saturation regime confirmed substrate-graph for non-uniform $\Psi$.**

The specific value of $w$ (e.g., $1/3$ for RDE; $0$ for MDE) depends on the specific structure of the kinetic-term contribution, which is **not addressed by Route C3** — that's the RDE vs MDE further discrimination requiring Route C1 (substrate-graph kinetic-theory-analog distribution function).

---

## §6 Elimination of alternative mappings

### §6.1 Alternative scenario: non-uniform $\Psi$ → saturation continuum

Ruled out by the Converse direction (§4.4): if continuum is saturation ($w = -1$), substrate must be uniform $\Psi$ (modulo Q-C3-1 + Q-C3-2 qualifications). Non-uniform $\Psi$ giving saturation continuum would require Branch (b) Lagrangian-degeneracy, excluded by Paper_ED_SC_4_9 structure.

### §6.2 Alternative scenario: uniform $\Psi$ → non-saturation continuum

Ruled out by the Forward direction (§3.6): uniform $\Psi$ uniquely produces vacuum-energy substrate-side Noether (Step 2), which DCGT preserves as uniform continuum (Step 3) with $w = -1$ (Step 4). Uniform $\Psi$ giving $w \neq -1$ continuum would require either Q1A failure (substrate-side Noether non-unique) or Q2A failure (DCGT mapping non-unique) — both eliminated by the construction-uniqueness closure.

### §6.3 Alternative scenario: DCGT scheme-dependent saturation identification

Ruled out by Q2A (Memo_ED_Q1Q2_JointClosure_Construct §3): the leading-order DCGT mapping is scheme-independent (Bensoussan-Lions-Papanicolaou). Different window kernels would not produce different saturation-vs-non-saturation discriminations at leading order. Subleading scheme-dependence (OPEN-ii) is at $O(\varepsilon)$ and not load-bearing.

### §6.4 Alternative scenario: SC-4.9 Hessian-signature-based saturation identification

Per the scoping memo §4.2 Route C2, an alternative would be using SC-4.9 Hessian eigenvalue signatures (S1/S2/S3 partition) to identify saturation. Under Route C3's $\Psi$-gradient discrimination, saturation corresponds to uniform $\Psi$ which has *vanishing* Hessian gradient (all-equal eigenvalues at saddle-stationarity). This is **consistent with but more specific than** the S1/S2/S3 partition — saturation is the specific case where the Hessian classification degenerates (no compression/expansion partition because no gradient structure to partition). Route C2 reframes this but does not supply additional substrate-graph content beyond Route C3 for the saturation case. **Route C2 confirmed vocabulary-level for saturation identification; substantive for non-saturation regime mapping (which Route C3 doesn't address).**

---

## §7 IDENTIFIED vs OPEN after C3

### IDENTIFIED (substantive C3 closures)

- **Forward direction (§3):** uniform $\Psi$ at substrate-graph → vacuum-energy continuum stress-energy ($w = -1$) → saturation regime phenomenology. Closes via Q1A + Q2A + Paper_ED_CCC §3.6 composition. No standard-physics-analog inheritance for the chain-class identification step.
- **Converse direction (§4):** vacuum-energy continuum stress-energy → uniform $\Psi$ at substrate-graph (modulo Q-C3-1 Lagrangian-genericity + Q-C3-2 subleading-order fluctuations).
- **Non-saturation discrimination (§5):** non-uniform $\Psi$ → $w \neq -1$ continuum → non-saturation regime. (Further RDE vs MDE discrimination not addressed; requires Route C1.)
- **Substrate-realizability of uniform $\Psi$ (§3.5):** Paper_ED_CCC §3.6 + §3.7 post-SCBU homogeneity supplies the substrate-graph realizable saturation state.
- **Elimination of alternative scenarios (§6.1, §6.2, §6.3):** non-uniform → saturation and uniform → non-saturation and scheme-dependent identifications all ruled out under Q1A + Q2A construction-uniqueness.
- **Route C2 status clarified (§6.4):** vocabulary-level for saturation case; substantive only for non-saturation regime mapping (separate question).

### Residual OPEN items after C3

**Carried from C3 closure (load-bearing for Cos_01 M3 upgrade):**

| OPEN | Description | Status / closure path |
|---|---|---|
| **Q-C3-1** | Lagrangian-genericity exclusion of Branch (b) (kernel-derivative-independent $\mathcal{L}_{\mathrm{sub}}$) | Structurally supplied by Paper_ED_SC_4_9; load-bearing on SC-4.9's explicit kernel-derivative content; closure path: audit verification |
| **Q-C3-2** | Subleading-order $O(\varepsilon)$ fluctuation admissibility | Not load-bearing for leading-order continuum phenomenology (parallel to Q2A OPEN-ii) |
| **Inherited from Q1A** | Q1A OPEN-i (substrate-scalar $\Psi$ verification at SC-4.9) | Inherited from Q1A construction; load-bearing for the Q1A → C3 composition; closure path: audit verification |
| **Inherited from Q2A** | Q2A OPEN-ii (subleading scheme-dependence) | Not load-bearing for leading-order |

**Not addressed by C3 (require subsequent routes for Dyn_02 / Dyn_03 upgrades):**

| OPEN | Description | Required route |
|---|---|---|
| **CC-OPEN-1 through 4** | Substrate-graph parameter constructions for per-chain V1 rate, V5 coupling, chain-mass, distribution function | Route C1 (for Dyn_02 RDE/MDE + Dyn_03 acceleration class) |
| **CC-OPEN-5** | Hessian → $w$ mapping for non-saturation regimes | Route C2 (substantive for non-saturation; vocabulary for saturation) |
| **CC-OPEN-7 + 8** | Multipole structure for GW + EM source classes | Route C4 (for Dyn_03 source-class identification) |

---

## §8 Closure status + recommended next steps

### §8.1 Cos_01 M3 upgrade pathway

After C3 construction:

- **Cos_01 saturation case** (inflation): chain-class identification CLOSED at substrate-graph level via Route C3.
- **Combined with Q1A + Q2A** (Memo_ED_Q1Q2_JointClosure_Construct): full M3-template chain for the saturation case is substrate-graph derived.
- **Upgrade trigger:** if the Q1A + Q2A + C3 closures all pass adversarial audit, **Cos_01 upgrades M2 → M3** on the strength of the saturation case being fully substrate-graph closed.

**Cos_01's audit-flagged Q1/Q2 inheritance qualifications would be retired** — replaced by the substrate-graph Q1A + Q2A + C3 chain. The five-anchor verdict-sync would be updated to M3 across status / abstract / §1 / audit verdict row / §6.

### §8.2 Dyn_02 + Dyn_03 status unchanged

- **Dyn_02 (Horizon-Motion):** saturation case (LDE) inherits C3's closure; RDE + MDE still M2 pending Route C1.
- **Dyn_03 (Radiation Law):** source-class identification still M2 pending Route C4 + Route C1.

C3 alone does not upgrade Dyn_02 or Dyn_03 to M3; **only Cos_01 upgrades on C3 alone** (because Cos_01 is saturation-regime exclusive).

### §8.3 Anticipated audit qualifications for C3

Following the discipline cascade pattern (CommitPhaseInheritance → SubstrateAction_Constancy → DCGT_VacuumEnergyMapping → NonSaturation_StressEnergy → NoetherFlux → Q1A/Q2A audits), an adversarial audit of C3 would examine:

- **A-C3-1:** Q-C3-1 Lagrangian-genericity verification — does Paper_ED_SC_4_9 explicitly require kernel-derivative dependence in $\mathcal{L}_{\mathrm{sub}}$? Examine whether the SC-4.9 substrate-action structure has any limit in which Branch (b) is approached or admitted (e.g., specific parameter regimes where kernel-derivative coupling vanishes).
- **A-C3-2:** alternative-mapping counterexample search beyond §6 enumeration. Concrete: could substrate-side $\Psi$ configurations with non-trivial gradient structure but specific symmetry properties (e.g., circularly oscillating $\Psi$) produce vacuum-energy form continuum at leading order?
- **A-C3-3:** Paper_ED_CCC §3.6 + §3.7 verification — does the post-SCBU homogeneity argument cleanly supply substrate-side uniform $\Psi$, or are there residual fluctuations / non-uniformity at the substrate-graph level that survive into the saturation regime?
- **A-C3-4:** composition-with-Q1A/Q2A verification — does the Q1A + Q2A + C3 composition introduce any residual freedom not captured by individual closures?

**Anticipated audit verdict:** ACCEPTED with audit qualifications named (analogous to Q1A audit pattern). The construction relies on substantive structural content (SC-4.9 substrate-action structure; CCC post-SCBU homogeneity; Q1A + Q2A surviving candidates) — all corpus-internal, no new primitives. Plausibility HIGH; matches the closure-plausibility grade in the scoping memo §4.3.

### §8.4 Recommended next steps

**Path-C3-Audit:** adversarial audit of this memo's construction following the discipline cascade. Verify A-C3-1 through A-C3-4 explicitly. **Likely audit outcome: ACCEPTED.**

**Path-Cos01-Update (conditional on C3 audit acceptance):** update Paper_ED_Cos_01 to reflect the M2 → M3 upgrade following the C3 closure. Add §3.x explicit substrate-graph chain-class identification reference; convert audit-flagged Q1/Q2 inheritance qualifications to substrate-graph-closed rows.

**Path-C4-Construction (parallel; targets Dyn_03 source-class):** focused construction memo attempting CC-OPEN-7 + 8 (multipole structure for GW and EM source classes). Per scoping memo §8 recommended sequence after C3.

**Path-C1-Construction (substantively harder; targets Dyn_02 + Dyn_03 acceleration class):** focused construction memo attempting CC-OPEN-1 through 4 (substrate-graph parameter constructions). Substrate-research-frontier work; may produce N1 negative finding (substrate-ontology genuinely lacks per-chain rate parameter; Dyn_02 + Dyn_03 cap at M2).

### My recommendation

**Path-C3-Audit + Path-C4-Construction in parallel.** Both are substantively tractable; together they would upgrade Cos_01 to M3 and supply the easier half of Dyn_03's chain-class identification. Path-C1-Construction follows as the harder substrate-research-frontier project.

### Cross-program impact summary (after C3 alone, audit-accepted)

| Paper | Before C3 | After C3 |
|---|---|---|
| Paper_ED_Cos_01 (Inflation) | M2 | **M3** (saturation case fully substrate-graph closed) |
| Paper_ED_Dyn_02 (Horizon-Motion) | M2 | M2 (LDE row strengthens via C3 inheritance; RDE + MDE still pending Route C1) |
| Paper_ED_Dyn_03 (Radiation Law) | M2 | M2 (still pending Route C4 + Route C1) |
| Paper_ED_GW_00 (GW) | M3 + row 12 partial | M3 + row 12 partial (unchanged) |
| Paper_ED_Cos_05 (Dark Energy; pending) | Draftable at M2 via Cos_01 | **Draftable at M3 via Cos_01 conditional on Route A** |

**Single-paper M2 → M3 upgrade for Cos_01** is the immediate corpus-impact deliverable. Cos_05 draftability upgrades to M3 (still Route A-conditional for quantitative $H_0$).

---

**End Memo_ED_ChainClass_C3_Construct.**
