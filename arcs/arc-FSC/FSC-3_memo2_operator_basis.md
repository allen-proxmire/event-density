# Arc FSC — Memo 4: Operator Basis for Substrate RG Flow (FSC-3 Memo 2)

**Status:** Second memo of Arc FSC sub-arc FSC-3. Construction memo: identifies the minimal operator basis required for a Wilsonian substrate-RG flow analysis aimed at the coupling-magnitude-universality question. Architect-mode active. No new primitives. Discipline reminder (FSC-0 §9): no quoting of $1/137$ or $\alpha = 1/137.036\ldots$; numerical-match checks reserved for sub-arc closure.

**Date:** 2026-05-25

**Prior context.** FSC-3 Memo 1 produced preliminary verdict (b) SPECULATIVE-COHERENT for the substrate-RG universality route, with the explicit follow-on requirement of an extended Arc-RG-style flow computation in an operator basis that includes coupling-magnitude-like operators. This memo constructs that basis. Memo 3 (future) will derive the flow equations on this basis and search for fixed-point structure.

**Methodological inheritance.** Arc RG (`arcs/arc-RG/ED_RG_Flow_Analysis.md`, seventh pass, 2026-04-22) established the operator-basis methodology for canonical ED PDE coefficients. This memo extends the Arc RG basis to include the additional operator classes required for coupling-magnitude flow: V1-mediated bilocal operators, channel-mixing operators, memory-bandwidth-partition operators, and horizon/saturation indicator operators.

---

## 1. What the Basis Must Achieve

### 1.1 Computational target

The FSC-3 flow computation must determine, for a dimensionless coupling-like substrate observable $g(k)$ defined at coarse-graining scale $k^{-1}$, whether
$$\frac{\mathrm{d}g}{\mathrm{d}\log k} \;=\; \beta_g(g, \{c_i\}, k)$$
admits an IR-attractive fixed point $g^{(*)}$ with universal basin of attraction (independent of substrate-microscopic initial conditions $\{c_i\}^{(0)}$ that encode V1 spectral shape, lattice connectivity, and the other FSC-2.1 inherited parameters).

To compute $\beta_g$ explicitly requires:

- A closed operator basis $\mathcal{B}$ such that block-averaging + rescaling under Wilsonian coarse-graining maps $\mathcal{B}$ into itself (modulo controlled truncation of irrelevant operators).
- Identification of the operator $O_g \in \mathcal{B}$ whose coupling is $g$.
- Identification of which other operators mix into $O_g$ under flow.
- Classification of each operator's RG-relevance (relevant / marginal / irrelevant / dangerously irrelevant) at the candidate fixed point.

### 1.2 Scope discipline

This memo identifies the operator basis structure. It does *not*:

- Derive the explicit flow equations $\beta_g, \beta_{c_i}$. That is Memo 3.
- Identify specific numerical fixed points. That is Memo 4–5.
- Verify universality of the fixed-point basin. That is Memo 6.

This memo's deliverable is the table of operators with their scaling dimensions, expected flow behavior, and operator-mixing structure — sufficient input for Memo 3.

---

## 2. Inheritance from Arc RG Basis

The closed Arc RG analysis used the operator basis (`ED_RG_Flow_Analysis.md` §1.2):

| Arc RG Symbol | Operator | Source |
|:---|:---|:---|
| $O_0$ | $\delta$ | linear penalty $P_0 \delta$ |
| $O_2$ | $\nabla^2 \delta$ | linear mobility $M_0 \nabla^2 \delta$ |
| $O_{3,0}$ | $\delta^3$ | cubic penalty $P_3 \delta^3 / 6$ |
| $O_{1,2}$ | $\delta^2 \nabla^2 \delta$ | even mobility $\frac{1}{2} M_2 \delta^2 \nabla^2 \delta$ |
| $O_{2,2}$ | $\delta \|\nabla\delta\|^2$ | even mobility $M_2 \delta \|\nabla\delta\|^2$ |
| $O_4$ | $\nabla^4 \delta$ | higher-derivative (trial) |
| $O_v$ | $v$ | participation mode |
| $O_{v,t}$ | $\dot v$ | participation kinetic |
| $O_{\delta v}$ | $\delta v$ | two-channel mixing |

This basis is adequate for canonical-ED PDE-coefficient flow analysis (which is what produced the 0.6 ratio universal result). It is **not adequate** for the FSC-3 coupling-magnitude analysis, because:

- It does not contain operators built from the complex participation measure $P_K = \sqrt{b_K}\, e^{i\pi_K}$ — only its real bandwidth-density component $\delta = \rho - \rho_*$.
- It does not contain $U(1)$-polarity-carrying operators required to track phase-coupling structure.
- It does not contain bilocal V1-mediated operators required to track FSC-2.1's V1-shape dependence.
- It does not contain channel-mixing operators required to track reversible-vs.-irreversible flow content.

The Arc RG basis is the *real-amplitude PDE sector*; FSC-3 requires the *complex-amplitude participation-measure sector* extended with cross-chain machinery.

---

## 3. Substrate-Level Fields and the Field-Theoretic Action

### 3.1 Canonical fields

At substrate scale, the load-bearing fields for participation-flow dynamics are:

| Field | Symbol | P-source | $D = 3+1$ canonical dimension |
|---|---|---|---|
| Participation measure (complex amplitude) | $P_K(x)$ | P04 + P09 | 1 |
| Bandwidth density (real-amplitude PDE sector) | $b_K(x) = \|P_K(x)\|^2$ | P04 | 2 |
| Polarity (phase) | $\pi_K(x) = \arg P_K(x)$ | P09 | 0 |
| Chain occupation field | $\chi(x)$ | P02 | (sector-dependent) |
| Edge transport elements | $T_e$ | P05 | 0 (group element) |
| Commitment-event density | $n_\mathrm{comm}(x)$ | P11 | 4 (delta-like local density at substrate; coarse-graining lowers) |
| Bandwidth-band allocations | $b^{(\alpha)}_K(x)$, $\alpha \in \{i, a, e, c\}$ | P04 §1.5 | 2 each |

Canonical dimension assignments follow from Stone-normalization (which fixes the $|P|$ dimension to 1 to deliver $\hbar$ correctly) and standard 4D scalar-field-theory dimension counting.

### 3.2 Substrate effective action (formal)

For the Wilsonian RG analysis, the substrate-emergent effective action at scale $k^{-1}$ has the structural form
$$\Gamma_k[P, \pi, \chi, T] \;=\; \sum_{O \in \mathcal{B}} g_O(k)\,\int O(x)\, d^4x \;+\; \sum_{O_{\mathrm{bl}}} g_{O_{\mathrm{bl}}}(k)\,\int O_{\mathrm{bl}}(x, y)\, d^4x\, d^4y \;+\; (\text{higher multi-locals})$$
where $\mathcal{B}$ is the local operator basis and $O_{\mathrm{bl}}$ denotes bilocal operators (V1-mediated). The flow is
$$k\frac{\mathrm{d}g_O}{\mathrm{d}k} \;=\; \beta_O(\{g_{O'}\}, k).$$

The substrate-RG question is whether the family $\{g_O(k)\}$ has an IR-attractive fixed point structure.

The basis $\mathcal{B}$ must include all operators that (a) are generated by coarse-graining from substrate primitives, and (b) contribute to coupling-magnitude flow. §4–§7 enumerate.

---

## 4. Local Operator Inventory

### 4.1 Real-amplitude (bandwidth) sector — inherits Arc RG basis

This sector is the Arc RG basis of §2, applied to $\delta = b_K - b_K^*$ (deviation of bandwidth from equilibrium). The Arc RG closure handles flow within this sector. For FSC-3 the load-bearing question is *cross-sector mixing* (does the real-amplitude sector couple into the complex-amplitude sector under flow?), addressed in §8.

### 4.2 Complex-amplitude (participation-measure) sector — required for FSC-3

The standard 4D scalar QFT-style operator basis applied to $P_K$, with manifest $U(1)$ invariance under global phase rotations (forced by P09 + P11):

| Symbol | Operator | Mass dimension $[O]$ | Coupling dimension $[g_O]$ | Status |
|---|---|---|---|---|
| $O_{P,\mathrm{mass}}$ | $\|P\|^2 = b_K$ | 2 | 2 | relevant (substrate "mass" term) |
| $O_{P,\mathrm{kin}}$ | $\|\partial P\|^2$ | 4 | 0 | marginal (kinetic normalization) |
| $\boxed{O_{P,4}}$ | $\|P\|^4$ | **4** | **0** | **marginal — α-like coupling sector** |
| $O_{P,6}$ | $\|P\|^6$ | 6 | $-2$ | irrelevant |
| $O_{P,4d}$ | $\|\partial P\|^2 \|P\|^2$ | 6 | $-2$ | irrelevant |
| $O_{P,\partial^4}$ | $\|\partial^2 P\|^2$ | 6 | $-2$ | irrelevant (higher-derivative kinetic) |

**Load-bearing structural observation.** The operator $O_{P,4} = |P|^4$ has mass dimension exactly 4 in $D = 3+1$, making its coupling $\lambda$ exactly *marginal*. Marginal couplings are precisely the operators whose flow is *logarithmic* in $k$ — the class of operators that *can* (but is not guaranteed to) exhibit non-trivial fixed-point structure. The α-like coupling lives here.

This is direct structural analog of standard scalar $\phi^4$ theory in 4D: $\lambda \phi^4$ is marginal, runs logarithmically, has the Landau-pole asymptotic-freedom problem in the IR direction (trivial IR fixed point for purely scalar) but non-trivial fixed-point structure under appropriate symmetry constraints (Wilson-Fisher in $4 - \epsilon$).

For ED, the question is whether the substrate's additional structure (commitment events P11, channel structure P07, rule-type primitive P10) produces a non-trivial fixed point for the $\lambda |P|^4$ coupling beyond the trivial scalar $\phi^4$ result.

### 4.3 Polarity-sector operators

Forced by P09 + P05's connection-status, the polarity-sector operators include:

| Symbol | Operator | Mass dimension $[O]$ | Coupling dimension $[g_O]$ | Status |
|---|---|---|---|---|
| $O_{\pi,\mathrm{kin}}$ | $\|D_\mu \pi\|^2$ (D-covariant) | 4 | 0 | marginal (gauge kinetic) |
| $O_{\pi,F^2}$ | $F_{\mu\nu} F^{\mu\nu}$ (substrate plaquette curvature) | 4 | 0 | marginal (substrate gauge-field strength) |
| $O_{\pi,A}^4$ | $(A_\mu A^\mu)^2$ | 4 | 0 | marginal-but-gauge-noninvariant |

The marginal operator $F^2$ is the substrate analog of the QED Maxwell term. Its coefficient is precisely the inverse-squared gauge coupling: $-\frac{1}{4 e^2} F_{\mu\nu} F^{\mu\nu}$ in conventional QED normalization. **In ED, the $F^2$ coefficient at the IR scale is the structural locus of $\alpha_\mathrm{ED}^{-1}$ (after $e \to e\sqrt{4\pi\alpha}$ identification).**

This identifies the FSC-3 target coupling cleanly: $g_{F^2}(k)$, the coefficient of the substrate plaquette-curvature operator under substrate-RG flow.

### 4.4 Matter-gauge interaction sector

The vertex operator coupling matter-rule-type $P$ to gauge-rule-type $A$:

| Symbol | Operator | Mass dimension $[O]$ | Coupling dimension $[g_O]$ | Status |
|---|---|---|---|---|
| $O_{PA,\mathrm{vert}}$ | $A_\mu (P^* \partial^\mu P + \mathrm{h.c.})$ | 4 | 0 | marginal (gauge-matter vertex) |
| $O_{PA,\mathrm{Seagull}}$ | $A_\mu A^\mu \|P\|^2$ | 4 | 0 | marginal (seagull-type two-photon coupling) |

The vertex coupling is the substrate analog of the QED interaction $e \bar\psi \gamma^\mu \psi A_\mu$. Its IR-flow behavior is jointly determined with $g_{F^2}$ and is the standard locus where Ward-Takahashi-type identities constrain coupling-flow in standard QFT.

ED has no automatic Ward-Takahashi identity at substrate scale (gauge invariance is *emergent* via T17, not a substrate-level forced principle, per FSC-0 §5.2). Whether emergent gauge invariance produces Ward-Takahashi-analog constraints at coarse-grained scales is a load-bearing question for Memo 3.

---

## 5. V1-Mediated Bilocal Operator Inventory

This is the new operator class required for FSC-3 — not present in Arc RG basis. V1's bilocal structure (chain at $y$ influences chain at $x$ via $V_1(x-y)$) generates a hierarchy of bilocal operators that contribute to the local-operator coupling flow through derivative expansion.

### 5.1 Bilocal kinetic-type operator

$$O_{V_1,2}(x, y) \;=\; V_1(x - y)\, [P_K^*(x) P_K(y) + \mathrm{h.c.}]$$

Mass dimension of integrated operator: $[V_1] + [P^* P] + [d^4y] = 2 + 2 + (-4) = 0$ at the integration-completed point. After derivative expansion of $P_K(y) = P_K(x) + (y-x)^\mu \partial_\mu P_K(x) + \frac{1}{2}(y-x)^\mu (y-x)^\nu \partial_\mu \partial_\nu P_K(x) + \ldots$, this bilocal contributes to local operators:

- Leading: $|P_K|^2 \cdot \int V_1(z) d^4z$ — Stone-normalized to fixed value; pure mass term contribution.
- First derivative correction: $\partial^\mu |P|^2 \cdot \int V_1(z) z^\mu d^4z$ — vanishes by Lorentz-isotropy + retardation requires non-zero contribution along $z^0$-direction (asymmetric piece).
- Second derivative: $\|\partial P\|^2 \cdot \int V_1(z) z^\mu z^\nu d^4z \cdot \eta_{\mu\nu}$ — contributes to *kinetic* operator $O_{P,\mathrm{kin}}$ with coefficient $\propto \langle z^2 \rangle_{V_1}$.

**Crucially, this contribution depends on the V1 *second moment*, which is shape-dependent (FSC-2.1).** The bilocal-kinetic operator's local-expansion contribution to the marginal kinetic operator is a shape-parameter-dependent quantity.

### 5.2 Bilocal quartic-type operator

$$O_{V_1,4}(x, y) \;=\; V_1(x - y)\, \|P_K(x)\|^2 \|P_K(y)\|^2$$

Mass dimension: $2 + 2 + 2 + (-4) = 2$ — relevant after integration over one variable, becomes irrelevant after both ($2 - 4 = -2$). Wait, let me re-examine.

Bilocal operator $\int O_{V_1,4}(x,y)\, d^4y$ has dimensions $[V_1] + [|P|^4] + [d^4y] = 2 + 4 + (-4) = 2$. As a local operator at point $x$, this is dimension 2 — *relevant*. But the leading derivative-expansion contribution is:

- $|P(x)|^4 \cdot \int V_1(z) d^4z$ (Stone-normalized constant) — contributes to $O_{P,4}$ with coefficient $\propto \int V_1 d^4z$ which is fixed by Stone. So leading contribution to $\lambda$ is Stone-fixed.

Wait, but then I_overlap (FSC-2's $I(0)$) doesn't enter at leading order? Let me reconsider.

Actually I think I was conflating two different bilocal structures. Let me distinguish:

**Type A bilocal** (single-V1):
$$O_{V_1,4}^{(A)}(x,y) = V_1(x-y) \, \|P(x)\|^2 \|P(y)\|^2$$
Leading local-expansion: $|P(x)|^4 \cdot \int V_1(z) d^4z$ — Stone-fixed contribution.

**Type B bilocal** (V1-squared, which IS the FSC-2 $I(\delta)$ structure):
$$O_{V_1^2}^{(B)}(x,y) = V_1(x-y) V_1(y-x) \, |\text{something}|$$
Or more precisely, the cross-overlap appears when *two* V1 lines connect the same two vertices — the "fish" or "sunset" diagram analog in standard QFT. This is a *loop* contribution, not a tree-level operator.

OK so the proper accounting is:

- **Tree-level bilocal contributions** (single V1 line): coefficient is Stone-fixed, no shape dependence at leading order.
- **One-loop contributions** (two V1 lines, $I(\delta)$ appears): coefficient is shape-dependent (FSC-2.1).

This is the standard QFT structure: tree-level couplings are fixed by Lagrangian; loop corrections are scheme-dependent.

For substrate-RG flow on $\lambda$ ($|P|^4$ coupling), the one-loop $\beta$-function picks up the $I(0)$ shape-dependent contribution. Let me revise the operator basis accordingly.

### 5.3 Revised V1-mediated operator inventory

| Symbol | Operator structure | Dimension | Status | Shape-dependence |
|---|---|---|---|---|
| $O_{V_1,\mathrm{kin}}^{(A)}$ | Tree-level single-V1 kinetic | renormalizes $O_{P,\mathrm{kin}}$ | marginal-contribution | Stone-fixed at tree level; shape-dependent at one loop |
| $O_{V_1,4}^{(A)}$ | Tree-level single-V1 quartic | renormalizes $O_{P,4}$ | marginal-contribution | Stone-fixed at tree level; shape-dependent at one loop |
| $O_{V_1^2,\mathrm{self}}^{(B)}$ | Two-V1 loop (self-energy) | renormalizes $O_{P,\mathrm{mass}}, O_{P,\mathrm{kin}}$ | UV-divergent → substrate-regulated by N1; coefficient is FSC-2.1's $I(0)$ | **shape-dependent** |
| $O_{V_1^2,\mathrm{vert}}^{(B)}$ | Two-V1 loop (vertex correction) | renormalizes $O_{P,4}$ | UV-divergent → substrate-regulated; shape-dependent at one loop | **shape-dependent** |

The shape-dependent contributions enter the flow equations as loop corrections to the marginal operator couplings. **This is precisely the substrate-RG locus where FSC-2.1 freedom could wash out (if loop corrections drive flow to a shape-independent fixed point) or propagate (if loop corrections preserve shape memory).**

---

## 6. Channel-Mixing Operators

### 6.1 Reversible vs. irreversible channel-mixing distinction

The substrate distinguishes two flow categories:

- **Reversible channel-mixing.** Mediated by P05 polarity-transport (no P11 commitment event). Conserves the substrate one-parameter unitary group structure; corresponds to the unitary part of substrate evolution.
- **Irreversible channel-mixing.** Mediated by P11 commitment events (chain commits to single channel with uniform-$U(1)$ phase-randomization). Breaks the unitary group structure; corresponds to the decoherence / measurement-update content of substrate evolution.

Both categories produce operators contributing to substrate-RG flow. The dimensionless ratio $R_\mathrm{rev/irrev}$ flagged in FSC-3 Memo 1 §5.1 lives in this sector.

### 6.2 Operator inventory

| Symbol | Operator | Dimension | Status | Sector |
|---|---|---|---|---|
| $O_{\mathrm{rev}}^{KK'}$ | $P_K^* P_{K'} + \mathrm{h.c.}$ (off-diagonal channel) | 2 | relevant | reversible channel-mixing (real part of $K \to K'$ coherence) |
| $O_{\mathrm{rev,kin}}^{KK'}$ | $\partial P_K^* \partial P_{K'} + \mathrm{h.c.}$ | 4 | marginal | reversible kinetic-channel-mixing |
| $O_{\mathrm{irrev}}^{KK'}$ | $n_\mathrm{comm}(x) [P_K^* P_K - P_{K'}^* P_{K'}]$ | 6 | irrelevant (commitment-density is dim 4 at substrate; lowers under coarse-graining) | irreversible |
| $O_{\mathrm{ratio}}$ | $g_{\mathrm{rev}}/g_{\mathrm{irrev}}$ (composite) | 0 | dimensionless ratio | mixed |

The irreversible operator $O_{\mathrm{irrev}}^{KK'}$ has unusual dimension structure: at substrate scale $n_\mathrm{comm}$ is delta-function-like (events at discrete points) with dimension 4; coarse-graining replaces it by a continuous density with substrate-scale value $1/(\ell_P^4 \tau_\mathrm{comm})$ for some commitment timescale $\tau_\mathrm{comm}$ inherited from P11 statistics. After coarse-graining to scale $R_\mathrm{cg}$, the effective commitment density has dimension consistent with marginal-to-irrelevant operator behavior.

This sector's flow is the substrate-RG analog of decoherence-rate flow in standard quantum-system coarse-graining (Lindblad-type analyses). The ED-specific content is that *commitment density itself is a substrate primitive observable*, not a phenomenological coefficient — so its flow is structurally constrained by P11.

### 6.3 The reversible-irreversible ratio operator

$O_{\mathrm{ratio}}$ is constructed from $g_{\mathrm{rev}}$ and $g_{\mathrm{irrev}}$ as a derived dimensionless quantity. Its substrate-RG flow is determined by the joint flow of its constituents:
$$\frac{\mathrm{d} O_{\mathrm{ratio}}}{\mathrm{d}\log k} \;=\; O_{\mathrm{ratio}} \left[\frac{\beta_{\mathrm{rev}}}{g_{\mathrm{rev}}} - \frac{\beta_{\mathrm{irrev}}}{g_{\mathrm{irrev}}}\right].$$

If $\beta_{\mathrm{rev}}/g_{\mathrm{rev}}$ and $\beta_{\mathrm{irrev}}/g_{\mathrm{irrev}}$ are equal at some scale $k^{(*)}$, then $O_{\mathrm{ratio}}$ has a fixed point at that scale. This is the FSC-3 Memo 1 §5.1 candidate substrate-RG universal.

**$O_{\mathrm{ratio}}$ is a candidate fixed-point operator at the ratio level, complementing the absolute-magnitude operators $\lambda$ and $g_{F^2}$.**

---

## 7. Memory-Bandwidth-Partition Operators

P04 §1.5 specifies the four-band bandwidth partition: internal (i), adjacency (a), environmental (e), commitment-reserve (c). The dimensionless allocation ratios are
$$r_\alpha = b^{(\alpha)} / b_\mathrm{tot}, \quad \alpha \in \{i, a, e, c\}, \qquad \sum_\alpha r_\alpha = 1.$$

This is a 3-dimensional manifold of dimensionless ratios. Each $r_\alpha$ is a candidate substrate-RG operator. Their flow is determined by which P-primitive's coarse-graining contributes most strongly to each band:

- $r_i$ (internal): chain-self-coherence; sourced by V1 self-kernel, evolves under reversible flow.
- $r_a$ (adjacency): chain-chain coherence; sourced by V1 cross-kernel, evolves under polarity-transport (P05).
- $r_e$ (environmental): chain-environment coherence; sourced by V5 cross-chain kernel + decoherence (P11).
- $r_c$ (commitment-reserve): bandwidth reserved for commitment events; sourced by P11 statistics.

The flow equations on $\{r_\alpha\}$ couple this sector to the V1-mediated sector (§5) and the channel-mixing sector (§6). Fixed-point analysis on $\{r_\alpha\}$ would identify whether the substrate's bandwidth partition flows to a universal allocation at IR — a substrate-RG-universal allocation ratio would be a substantive program-level result.

### 7.1 Operator inventory

| Symbol | Operator | Dimension | Status |
|---|---|---|---|
| $O_{r_i}, O_{r_a}, O_{r_e}, O_{r_c}$ | $b^{(\alpha)}/b_\mathrm{tot}$ | 0 (dimensionless ratios) | marginal-by-construction; flow determined by inter-band cross-flow |
| $O_{b,\mathrm{tot}}$ | $b_\mathrm{tot}$ | 2 | relevant (substrate "mass" sector) |

The total bandwidth is in the relevant-mass sector; only the inter-band ratios are dimensionless and candidate substrate-RG-universal quantities.

---

## 8. Horizon and Saturation Operators

### 8.1 Cross-bandwidth saturation operator

Arc BH / BH-2 established that $\Gamma_\mathrm{cross}$ saturates at substrate-fixed thresholds at decoupling surfaces. The saturation creates a flow-endpoint structure analogous to a phase-transition fixed-point in standard statistical-mechanics RG.

| Symbol | Operator | Dimension | Status |
|---|---|---|---|
| $O_{\Gamma\mathrm{sat}}$ | $\Theta(\Gamma_\mathrm{cross} - \Gamma_\mathrm{cross}^{(\mathrm{sat})})$ | 0 | dimensionless indicator; non-analytic but well-defined as flow-endpoint marker |

This operator is *non-analytic* (step-function) and does not contribute as a standard local operator in the Wilsonian basis. Its role is to mark *flow termination* at decoupling surfaces — the flow on coupling-magnitude operators is well-defined only for $\Gamma_\mathrm{cross} > \Gamma_\mathrm{cross}^{(\mathrm{sat})}$ and changes character qualitatively (becomes a horizon-type boundary value problem) at saturation.

For FSC-3 flow computation aimed at bulk-substrate coupling-magnitude flow (away from horizons), $O_{\Gamma\mathrm{sat}}$ is *not* part of the bulk operator basis. It is part of the *boundary-condition* specification for the flow equations.

### 8.2 Multiplicity-cap operator (Q-COMPUTE)

| Symbol | Operator | Dimension | Status |
|---|---|---|---|
| $O_{\mathcal{M}}$ | $\Theta(M - \mathcal{M}_\mathrm{crit})$ | 0 | dimensionless indicator; non-analytic boundary marker |

Same status as $O_{\Gamma\mathrm{sat}}$: boundary-condition operator, not bulk-flow operator.

---

## 9. RG Relevance Classification Table

Consolidated classification of all operators identified in §4–§8, organized by RG-relevance status at the trivial (Gaussian) fixed point in $D = 3+1$:

### 9.1 Relevant operators (IR-growing)

| Operator | Dimension | Coupling | Substrate Role |
|---|---|---|---|
| $O_{P,\mathrm{mass}}$ | 2 | $m^2$ | substrate "mass" — sourced by Stone-fixed $\int V_1\,d^4z$ tree-level + loop corrections |
| $O_{\mathrm{rev}}^{KK'}$ | 2 | $g_\mathrm{rev}^{KK'}$ | reversible channel-mixing amplitude |
| $O_{b,\mathrm{tot}}$ | 2 | $b_\mathrm{tot}$ | total bandwidth scale |

### 9.2 Marginal operators (the FSC-3 load-bearing class)

| Operator | Dimension | Coupling | Substrate Role | FSC-3 status |
|---|---|---|---|---|
| $O_{P,\mathrm{kin}}$ | 4 | $Z$ | kinetic normalization | runs via $V_1$-loops; shape-dependent |
| $\boxed{O_{P,4}}$ | 4 | $\lambda$ | quartic self-coupling | **α-like coupling candidate (matter sector)** |
| $\boxed{O_{\pi,F^2}}$ | 4 | $1/(4e^2)$ | substrate plaquette curvature | **α-like coupling candidate (gauge sector)** |
| $O_{\pi,\mathrm{kin}}$ | 4 | gauge $Z$ | gauge kinetic normalization | gauge $Z$ flow |
| $O_{PA,\mathrm{vert}}$ | 4 | $e$ | matter-gauge vertex | constrains $e$-flow via Ward-Takahashi (if emergent) |
| $O_{PA,\mathrm{Seagull}}$ | 4 | $e^2$ | seagull two-photon vertex | constrains via gauge invariance |
| $O_{\mathrm{rev,kin}}^{KK'}$ | 4 | reversible kinetic | reversible channel kinetic mixing | one of the FSC-3 candidate fixed-point operators |
| $O_{r_\alpha}$ | 0 | $r_\alpha$ | P04 band-allocation ratio | marginal-by-construction; flow couples to V1 and channel-mixing sectors |
| $O_{\mathrm{ratio}}$ | 0 | rev/irrev ratio | derived dimensionless | candidate fixed-point ratio (Memo 1 §5.1) |

**Eight marginal operators**, of which two ($O_{P,4}$ and $O_{\pi,F^2}$) are the *direct* α-like coupling-magnitude candidates and six are the structural-context operators that constrain their flow.

### 9.3 Irrelevant operators (IR-suppressed)

| Operator | Dimension | Coupling | Substrate Role |
|---|---|---|---|
| $O_{P,6}$ | 6 | $1/M^2$ | sextic self-coupling — irrelevant in $D = 3+1$ |
| $O_{P,4d}$ | 6 | derivative-quartic | derivative correction |
| $O_{P,\partial^4}$ | 6 | $1/M^2$ | higher-derivative kinetic |
| $O_{\mathrm{irrev}}^{KK'}$ | 6 | irreversible-flow | irreversible channel-mixing |
| All other operators with $[O] > 4$ | $> 4$ | various | IR-suppressed |

Irrelevant operators are systematically truncated in standard Wilsonian RG analysis. The substrate-emergent gauge structure has potential *dangerously irrelevant* operators that contribute to flow even when nominally irrelevant — flagged in §10.

### 9.4 Dangerously irrelevant operators

Two operators in the substrate-RG basis are nominally irrelevant but potentially dangerous:

- **$O_{V_1^2,\mathrm{self}}^{(B)}$ (V1 self-energy).** Nominally a one-loop correction (which would be dimensionally irrelevant in a power-counting sense), but its substrate-regularized UV-cutoff behavior produces a logarithm of $k \ell_P$ that survives at IR. This is the standard "logarithmic running" of $\lambda$ in $\phi^4$ theory. The log-correction is shape-dependent (FSC-2.1) — dangerously irrelevant in the sense that it does not vanish at IR but persists with shape-dependent coefficient.
- **$O_{\mathrm{irrev}}^{KK'}$ (commitment density).** Nominally dimension-6 after coarse-graining, but if commitment density has a fixed substrate-emergent value (not flowing to zero), then its contribution to flow on $O_{P,4}$ is finite at IR and shape-dependent on the P11 commitment statistics.

Both dangerously-irrelevant operators are loci where shape-dependence enters the marginal-operator flow. **They are the structural loci where FSC-2.1's freedom propagates to the IR flow on $\lambda$ and $g_{F^2}$.** This is the load-bearing finding for whether FSC-3 closes positively or negatively.

---

## 10. Operator Mixing Analysis

### 10.1 Closed sub-bases under Z₂-symmetric flow

Under the Z₂ symmetry $P \to e^{i\pi} P$ (i.e., $P \to -P$), operators are graded into Z₂-even and Z₂-odd:

- **Z₂-even (closed under flow if Z₂ holds):** $O_{P,\mathrm{mass}}, O_{P,\mathrm{kin}}, O_{P,4}, O_{P,6}, O_{P,4d}, O_{V_1,\mathrm{kin}}^{(A)}, O_{V_1,4}^{(A)}, O_{V_1^2,\mathrm{self}}^{(B)}, O_{V_1^2,\mathrm{vert}}^{(B)}, O_{\pi,\mathrm{kin}}, O_{\pi,F^2}, O_{PA,\mathrm{Seagull}}, O_{\mathrm{rev,kin}}^{KK'}, O_{r_\alpha}$.
- **Z₂-odd (not generated under Z₂-preserving flow):** $O_{P,3} = P^3 + \mathrm{h.c.}$, $O_{PA,\mathrm{vert}}$ (under specific Z₂-action on $A$).

The Z₂-even sub-basis is closed under Wilsonian flow if Z₂ is preserved (which it is in the matter-rule-type sector under uniform $U(1)$ randomization of P11).

### 10.2 Bandwidth-partition coupling

The four band-allocation ratios $r_\alpha$ are *not* independently flowing — they sum to unity, so there are only 3 independent degrees of freedom in $(r_i, r_a, r_e, r_c)$. The flow on $(r_i, r_a, r_e, r_c)$ couples to:

- V1-mediated operators (through $r_i, r_a$ — internal and adjacency bands sourced by V1).
- V5-mediated and commitment operators (through $r_e, r_c$ — environmental and commitment-reserve bands).
- Reversible-irreversible ratio $O_{\mathrm{ratio}}$.

The band-allocation operators form a *closed sub-system* together with the channel-mixing and V1-mediated sectors. The marginal-operator flow on $\lambda$ and $g_{F^2}$ couples *into* this sub-system through V1-loop contributions.

### 10.3 Minimal closed operator set

For the FSC-3 Memo 3 flow-equation computation aimed at coupling-magnitude flow, the minimal closed operator set is:

**Tier 1 (load-bearing marginal couplings):**
- $O_{P,4}$ (matter quartic, coupling $\lambda$).
- $O_{\pi,F^2}$ (gauge plaquette, coupling $1/e^2$).
- $O_{PA,\mathrm{vert}}$ (matter-gauge vertex, coupling $e$).

**Tier 2 (relevant operators, source-of-flow):**
- $O_{P,\mathrm{mass}}$ (matter mass, coupling $m^2$).
- $O_{\mathrm{rev}}^{KK'}$ (reversible channel-mixing amplitudes).
- $O_{b,\mathrm{tot}}$ (total bandwidth).

**Tier 3 (kinetic normalization, must track):**
- $O_{P,\mathrm{kin}}$ (matter $Z$).
- $O_{\pi,\mathrm{kin}}$ (gauge $Z$).
- $O_{\mathrm{rev,kin}}^{KK'}$ (reversible kinetic mixing).

**Tier 4 (dangerously irrelevant, shape-dependence carriers):**
- $O_{V_1^2,\mathrm{self}}^{(B)}$ (one-loop self-energy with shape-dependent log).
- $O_{V_1^2,\mathrm{vert}}^{(B)}$ (one-loop vertex correction).
- $O_{\mathrm{irrev}}^{KK'}$ (commitment-density mixing).

**Tier 5 (ratio-level candidate fixed-point operators):**
- $O_{\mathrm{ratio}}$ (reversible/irreversible ratio).
- $\{O_{r_\alpha}\}_{\alpha = i,a,e,c}$ with $\sum_\alpha r_\alpha = 1$ (P04 band allocation, 3 independent).

**Truncation:** all operators of mass-dimension $> 4$ not in Tier 4 are truncated.

**Total operators in minimal closed basis:** 14 (3 Tier-1 + 3 Tier-2 + 3 Tier-3 + 3 Tier-4 + 4 Tier-5, minus 1 constraint on $r_\alpha$).

This is a substantially larger basis than Arc RG's 9-operator PDE basis, but is the minimum required to track coupling-magnitude flow with FSC-2.1 shape-dependence carriers explicit.

---

## 11. Operator-Mixing Structure Under Coarse-Graining

For the Memo 3 flow-equation derivation, the operator-mixing matrix structure is:

$$\beta_{O_i} \;=\; \sum_j A_{ij}\, g_{O_j} \;+\; \sum_{j,k} B_{ijk}\, g_{O_j} g_{O_k} \;+\; \cdots$$

with $A$ the linear (anomalous-dimension) mixing matrix and $B$ the cubic mixing tensor. Key structural features expected:

- **$\lambda$ flow couples to $V_1$-loop integrals:** $\beta_\lambda \sim a \lambda^2 + b\, \lambda\, I(0)\, [\text{kinematic factor}] + \cdots$ where $I(0)$ is the FSC-2.1 shape-dependent integral. This is the structural locus where FSC-2.1 propagates to coupling-magnitude flow.
- **$g_{F^2}$ flow couples to $e$ flow via gauge structure:** $\beta_{1/e^2} \sim c\, e^2 \cdot [\text{matter loop}]$ — standard QED-analog one-loop running. The matter loop is the V1-mediated participation-loop, with $I(0)$ entering as the substrate analog of the bare loop.
- **Ratio operators decouple from absolute-magnitude operators only if the substrate has additional symmetry:** in standard QFT, this requires conformal invariance or similar. ED's substrate has *partial* conformal-like structure at hydrodynamic-window scales (DCGT) but does not have substrate-level conformal invariance. The ratio operators are *not* automatically decoupled.

The expected structural finding (FSC-3 Memo 1 §6.4): the ratio-operator flow exhibits IR-attractive fixed points; the absolute-magnitude operator flow does not. **This is what Memo 3 will test.**

---

## 12. Recommendation for Memo 3

### 12.1 Methodology

For Memo 3 (flow-equation derivation):

- **Adopt the 14-operator minimal closed basis of §10.3.**
- **Truncate to one-loop order** in the Wilsonian RG expansion, consistent with Arc RG seventh-pass methodology.
- **Preserve Z₂ symmetry** explicitly; flag Z₂-breaking sources separately if needed.
- **Track $V_1$ shape parameters $\{s_i\}$ as explicit flow-equation inputs** so that the FSC-2.1 dependence is manifest at every flow scale.
- **Compute $\beta_\lambda, \beta_{1/e^2}, \beta_e$** with explicit shape-parameter dependence; identify any operator combinations whose flow is shape-independent (universal candidates).

### 12.2 Expected outcomes

Three structurally-distinct scenarios for Memo 3:

- **Scenario A (FSC-3 positive).** Memo 3 finds IR-attractive fixed points for $\lambda$ and $g_{F^2}$ with universal basin (shape-independent). This would be surprising; not expected based on standard-QFT analog. If found, would substantively unblock FSC-2.1 at emergent scales.
- **Scenario B (FSC-3 partial-positive).** Memo 3 finds IR-attractive fixed points for *ratio* operators ($O_{\mathrm{ratio}}$, $\{r_\alpha\}$) but not for absolute-magnitude operators ($\lambda$, $g_{F^2}$). This is the structurally-expected outcome based on Arc RG's 0.6-ratio precedent and V5 cross-scale universality. Would further sharpen §7.2.
- **Scenario C (FSC-3 negative).** Memo 3 finds no fixed-point structure even for ratios; absolute-magnitude flow propagates shape-dependence fully to IR. Position-paper §7.2 would be substantially strengthened to "FORCED-INHERITED at all scales."

### 12.3 Computational scope

Memo 3 is the load-bearing computational memo of the sub-arc. Estimated scope: substantial — comparable to Arc RG's full seven-pass closure. May require multiple memos (Memo 3a flow-equation setup, Memo 3b fixed-point search, Memo 3c universality basin verification).

### 12.4 Tier-1 recommendation reaffirmed

Per FSC-3 Memo 1 §7.2: hold position-paper §7.2 as currently stated until Memo 3 is closed. The basis-construction work in this memo does not change the §7.2 disclaimer's structural status — it only sets up the computation that would change it (in either direction).

---

## 13. Summary

| Question (FSC-3 Memo 2 scope) | Answer |
|---|---|
| Does Arc RG basis suffice for FSC-3? | No (real-amplitude PDE basis; missing complex-amplitude, polarity-sector, V1-bilocal, channel-mixing). |
| What is the minimal closed operator basis for coupling-magnitude flow? | 14 operators in five tiers (§10.3). |
| Which operators are the α-like coupling-magnitude candidates? | $O_{P,4}$ (matter quartic, $\lambda$); $O_{\pi,F^2}$ (gauge plaquette, $1/e^2$); $O_{PA,\mathrm{vert}}$ (vertex, $e$). |
| What is the structural locus where FSC-2.1 shape-dependence enters coupling-magnitude flow? | Tier-4 dangerously-irrelevant operators $O_{V_1^2,\mathrm{self}}^{(B)}$, $O_{V_1^2,\mathrm{vert}}^{(B)}$ (V1-loop integrals carrying $I(0)$ shape-dependence). |
| Which operators are candidate ratio-level substrate-RG fixed-point operators? | Tier-5: $O_{\mathrm{ratio}}$, $\{O_{r_\alpha}\}_{\alpha = i,a,e,c}$ (band-allocation ratios). |
| Is Memo 3's flow-equation computation now scoped? | Yes — 14-operator basis, one-loop Wilsonian, Z₂-symmetric, explicit shape-parameter dependence. |
| Expected outcome of Memo 3? | Scenario B (partial-positive): ratio fixed points exist, absolute-magnitude fixed points do not. |
| Implication for §7.2 disclaimer? | Unchanged by this memo; will be updated upon Memo 3 closure. |

---

## 14. References and Inheritance

| Inherited Item | Source | Use in FSC-3 Memo 2 |
|---|---|---|
| Arc RG basis (9-operator PDE) | `arcs/arc-RG/ED_RG_Flow_Analysis.md` | Methodology template + real-amplitude sector inheritance (§2) |
| DCGT (continuum coarse-graining) | Paper #73 / Arc D | Wilsonian block-averaging foundation (§1.1) |
| Stone-theorem normalization | Papers #4, #13 | $P$-field canonical dimension assignment (§3.1) |
| T17 (gauge-field-as-rule-type) | Paper #5 | Polarity-sector operator identification ($O_{\pi,F^2}, O_{\pi,\mathrm{kin}}$, §4.3); matter-gauge vertex structure (§4.4) |
| Theorems N1, T18 | Papers #18, #19 | V1 finite width + retardation → V1-bilocal operator structure (§5) |
| P04 §1.5 (four-band partition) | Position paper | Memory-bandwidth-partition operators (§7) |
| P11 (commitment with uniform randomization) | Position paper | Irreversible channel-mixing operator structure (§6) |
| Arc BH / BH-2 (saturation) | `theory/Black_Holes/BH-2*` | Horizon/saturation boundary-condition operators (§8) |
| Arc Q-COMPUTE / Class A | `theory/Quantum_Computing/` | Multiplicity-cap boundary operator (§8.2) |
| FSC-1 Memo 1 | `FSC-1_polarity_transport_topology.md` | Polarity-transport reading (P05 as genuine connection) |
| FSC-2 Memo 1 | `FSC-2_v1_cross_overlap.md` | $I(0)$ as the shape-dependent integral entering Tier-4 operators |
| FSC-3 Memo 1 | `FSC-3_substrate_rg_universality.md` | Sub-arc setup + 0.6-ratio universal precedent + ratio-vs.-absolute structural distinction |

---

**End of FSC-3 Memo 2.**

*Minimal closed operator basis for substrate-RG coupling-magnitude flow constructed: 14 operators in five tiers. Tier-1 (3 marginal couplings $\lambda$, $1/e^2$, $e$): the α-like coupling-magnitude candidates. Tier-4 (3 dangerously-irrelevant V1-loop + commitment-density operators): the structural carriers of FSC-2.1 shape-dependence into the marginal-operator flow. Tier-5 (4 ratio operators): candidate fixed-point operators paralleling Arc RG's 0.6-ratio universal. Memo 3 (flow-equation derivation) is now scoped: 14-operator basis, one-loop Wilsonian, Z₂-symmetric, explicit shape-parameter tracking. Expected outcome (Scenario B): partial universality — ratio fixed points yes, absolute-magnitude fixed points no — paralleling Arc RG closure + standard-QFT pattern. Position-paper §7.2 disclaimer unchanged until Memo 3 closes.*
