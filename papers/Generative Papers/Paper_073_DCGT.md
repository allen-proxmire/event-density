# Paper_073 — The Diffusion Coarse-Graining Theorem (DCGT)

**Series:** Event Density (ED) Generative Papers — Wave-2 soft-matter / cross-domain bridge
**Author:** Allen Proxmire
**Status:** Publication draft (substrate→continuum bridge; load-bearing for V5, gravity arc, BH arc)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/soft-matter/Paper_073_DCGT.md` (ED-Generative)
**Working save location:** `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\Paper_073_DCGT.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System. Standalone. Cold-reader accessible.

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **The 13 substrate primitives are not derived** (Paper_087).
2. **DCGT is not the only possible substrate→continuum bridge.** Other coarse-graining procedures (Wilsonian RG, hydrodynamic projection, mode-coupling) may apply in specific regimes; DCGT is the one substrate-level bridge derived from substrate-graph diffusion of V1/V5 content.
3. **DCGT does not derive continuum-level coupling constants or transport coefficients.** It supplies the *form* of continuum equations (diffusion-type, propagator-type, constitutive-law-type); the *coefficients* (diffusion constant, viscosity, conductivity, etc.) are inherited from value-layer empirical content and substrate-level matching at the coarse-graining scale.
4. **DCGT is regime-conditional.** It applies in the hydrodynamic-window scale separation $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$. Outside this window (strong-gradient regimes, near-substrate-scale physics, near-singularity regimes), DCGT breaks down.
5. **No claim that DCGT derives standard QFT renormalization.** DCGT operates one structural level below RG: it produces the continuum theory whose RG flow is then studied by standard techniques. The relationship between DCGT and Wilsonian RG is an active area (Papers in queue).
6. **DCGT is not a derivation of Einstein equations.** The substrate→continuum bridge produces flat-spacetime continuum equations under the standard hydrodynamic window; curvature emergence is the subject of the Arc ED-10 program, not DCGT.
7. **No claim that DCGT is exhaustive across all ED arcs.** Soft-matter Maxwell relaxation, gravity-arc cumulative-strain, BH-arc Hawking spectrum, and Q-COMPUTE multiplicity-cap behavior all use DCGT differently; the regime-specific applications are developed in arc-specific papers.

---

## Abstract

The **Diffusion Coarse-Graining Theorem (DCGT)** is the substrate→continuum bridge in the Event Density Generative Substrate Ontology: given the 13 postulated primitives (Paper_087) + V1 inheritance (Paper_089) + V5 dependence (Paper_090), substrate-level kernel-mediated content coarse-grains under the **hydrodynamic-window scale separation** $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$ to continuum diffusion-type / propagator-type / constitutive-law equations. The theorem has three load-bearing components: (1) **scale separation** — substrate-graph operations at scale $\ell_{\mathrm{ED}}$ produce well-defined coarse-grained content at scale $R_{\mathrm{cg}}$ that depends on macroscopic flows at scale $L_{\mathrm{flow}}$ but is decoupled from substrate microstructure; (2) **diffusion-form emergence** — V1's finite-width retarded envelope coarse-grains to a continuum diffusion operator under standard substrate-graph averaging; (3) **cross-domain instantiations** — DCGT produces continuum Maxwell relaxation in soft-matter (V5 soft-regime), retarded / Feynman / advanced propagator hierarchy in QFT (V5 QFT-regime), Lieb–Robinson velocity bound in condensed matter, and curved-spacetime entanglement at horizons (V5 BH-regime). The paper makes no claim that DCGT is the only substrate→continuum bridge, no claim of derivation of continuum-level transport coefficients, no claim of validity outside the hydrodynamic window, and no claim of curvature-emergence derivation. The empirical case rests on cross-domain reach: DCGT is load-bearing for Paper_090 (V5 cross-chain kernel applications), the gravity arc (Papers_027/029/030/031), the BH arc (Papers_039/047), and the soft-matter arc.

---

## 1. Introduction

### 1.1 What this paper does

This paper supplies the **canonical reference** for the Diffusion Coarse-Graining Theorem (DCGT) — the substrate→continuum bridge invoked across the ED corpus. The paper:

1. States DCGT formally, with explicit regime assumptions (hydrodynamic-window scale separation).
2. Derives the substrate-level diffusion-form emergence from V1 finite-width + substrate-graph averaging.
3. Catalogues cross-domain instantiations (soft-matter Maxwell, QFT propagators, condensed-matter Lieb–Robinson, BH curved-spacetime entanglement).
4. Specifies breakdown conditions (strong-gradient, near-substrate-scale, near-singularity regimes).

DCGT is **upstream of Paper_090** (which uses DCGT in §6 for V5 cross-domain coarse-graining), **upstream of Paper_027** (which uses DCGT to convert V1 cumulative-strain reading into continuum Newtonian potential), **upstream of Paper_039 / Paper_047** (which use DCGT to bridge substrate Hawking mechanism to semiclassical Hawking spectrum), and referenced by Paper_054 (UR-1) for the continuum-limit decoherence-theory bridge.

### 1.2 Why DCGT matters

Standard physics operates in the *continuum*: fields, propagators, diffusion equations, hydrodynamics. ED's substrate ontology operates on *discrete* substrate-graph content: chains, channels, polarity-transport, commitment. The bridge between the two is **load-bearing for the entire ED corpus**: every continuum-level empirical prediction is, structurally, a coarse-graining of substrate-level mechanism via DCGT.

This matters for three reasons:

- **Empirical adequacy.** Without DCGT, ED's substrate-level mechanisms cannot connect to standard continuum-level empirical observations (rotation curves, propagator measurements, Hawking radiation, Maxwell relaxation, etc.).
- **Cross-domain coherence.** DCGT applies the same substrate→continuum procedure across soft-matter, gravity, BH, condensed-matter, and QFT regimes — the procedural unity is itself the cross-domain wedge claim.
- **Breakdown predictions.** DCGT specifies when substrate-level mechanism is *not* captured by continuum description — strong-gradient regimes, near-substrate-scale physics, near-singularity content. These breakdown predictions distinguish ED from standard continuum-only frameworks.

### 1.3 How this fits into the corpus

DCGT is a wedge/foundation paper used across multiple arcs:

- **Soft-matter arc:** DCGT + V5 → Maxwell relaxation, Krieger–Dougherty viscosity.
- **Gravity arc:** DCGT + V1 cumulative-strain → Newtonian potential (Paper_027).
- **BH arc:** DCGT + V5 KMS → semiclassical Hawking (Paper_047).
- **Condensed-matter arc:** DCGT + V5 finite-memory → Lieb–Robinson velocity.
- **V5 paper (Paper_090):** uses DCGT for all four cross-domain instantiations.

DCGT closes the substrate→continuum gap that prior pre-pivot Arc-D work developed (Arc-D closure 2026-04-30).

---

## 2. Primitive Inputs

This paper takes the following ED substrate primitives as **postulated** (Paper_087):

- **P02 (Participation).**
- **P03 (Channel + locus indexing; spatial homogeneity).** Translation-invariance is load-bearing for the substrate-graph averaging.
- **P04 (Bandwidth as non-negative additive scalar).** Additivity is load-bearing for coarse-grained substrate content.
- **P05 (Polarity-transport along edges).**
- **P06 (Spatial dimension $D = 3+1$).** Continuum diffusion operators are $D$-dimensional.
- **P07 (Channel structure).**
- **P08 (Substrate scale $\ell_{\mathrm{ED}}$).** Defines the substrate-graph granularity below which DCGT does not resolve.
- **P09 ($U(1)$-valued polarity).**
- **P10 (Rule-type primitive).**
- **P11 (Commitment irreversibility).**
- **P13 (Time homogeneity).**

**V1 inheritance (Paper_089):** finite-width retarded structure; substrate-level kernel that coarse-grains to continuum diffusion / propagator operators.

**V5 dependence (Paper_090):** cross-chain correlation kernel; coarse-grains to continuum constitutive laws (Maxwell relaxation, Lieb–Robinson bound, KMS-thermal structure).

**Upstream paper dependencies:**

- **Paper_087:** position paper.
- **Paper_089:** V1 canonical reference.
- **Paper_090:** V5 cross-chain kernel.

**Empirical / value-layer inputs:**

- Substrate scale $\ell_{\mathrm{ED}}$ empirically identified with $\ell_P$ (Paper_027 §5.3).
- Coarse-graining scale $R_{\mathrm{cg}}$ regime-dependent.
- Macroscopic flow scale $L_{\mathrm{flow}}$ regime-dependent.

**No primitive forcing is invoked.**

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| V1 finite-width retarded structure | D | Paper_089 |
| V5 cross-chain correlation kernel | D | Paper_090 |
| Hydrodynamic-window scale separation $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$ | A→regime | **Regime assumption**, §3.1 |
| Substrate-graph averaging at $R_{\mathrm{cg}}$ produces well-defined continuum content | D | §3.2 from P03 translation-invariance + P04 additivity |
| V1 envelope coarse-grains to diffusion operator | D | §4 from V1 finite-width + substrate-graph averaging |
| V5 envelope coarse-grains to memory-kernel diffusion | D | §5 from V5 finite-memory + cross-chain averaging |
| Continuum Maxwell relaxation form (exponential decay) | D | §6.1 from §5 V5 Markovian-limit derivation (form is derived) |
| Continuum Maxwell relaxation **numerical** $\tau_{\mathrm{Maxwell}}$ value | **I** | §6.1 empirical matching: $\tau_{V5}^{\mathrm{soft}} = \tau_{\mathrm{Maxwell}}^{\mathrm{empirical}}$. **Numerical value inherited via empirical anchoring, not substrate-derived.** *(Round-3 Rereading Test: was D, now I — matching is not derivation.)* |
| Continuum propagator hierarchy (QFT) form | D | §6.2 from V1/V5 substrate kernel coarse-graining via §4 + §5 |
| Lieb–Robinson velocity bound **form** $v_{LR} \sim \ell_{V5}/\tau_{V5}^{\mathrm{ent}}$ | **A→dimensional-analogy** | §6.3 derives the LR bound *form* by **dimensional analysis** matching to standard Lieb–Robinson theorem. The actual LR theorem is a tight commutator-norm bound from Hamiltonian locality; substrate-level derivation requires more than dimensional analysis. *(Round-3 Rereading Test: was D, now A→dimensional-analogy.)* |
| KMS-thermal structure at horizons (BH) | D | §6.4 from §5 V5 imaginary-time substrate-graph extension + DCGT |
| Breakdown taxonomy (strong-gradient / near-substrate / near-singularity / strong-curvature) | **P (breakdown-taxonomy regime classification)** | §7.1–§7.4 identify breakdown regimes by structural analogy to standard physics. Not derived from substrate primitives; substrate-level regime-failure taxonomy. *(Round-3 Rereading Test: was D, now P.)* |
| Numerical transport coefficients | I | Empirical inheritance |

One row is "A→regime" (hydrodynamic-window scale separation): this is **explicitly labeled as a regime assumption**, §3.1, per QC discipline (item 8 — regime conditions are an acceptable category, neither D nor P). All other rows are P, D, or I. **No A (asserted-without-label) rows.**

---

## 3. Setup — Scale Separation and Substrate-Graph Averaging

### 3.1 The hydrodynamic-window scale separation (regime assumption)

DCGT operates in the **hydrodynamic-window scale separation**:

$$
\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}.
$$

where:

- $\ell_{\mathrm{ED}}$: substrate scale (Primitive P08).
- $R_{\mathrm{cg}}$: coarse-graining scale — the spatial / temporal extent over which substrate-graph content is averaged to produce continuum-level quantities.
- $L_{\mathrm{flow}}$: macroscopic flow scale — the spatial / temporal extent over which continuum-level quantities vary appreciably.

**This is a regime assumption, not a derivation.** DCGT's conclusions apply when the scale separation holds. Outside this window (e.g., $R_{\mathrm{cg}} \sim \ell_{\mathrm{ED}}$, near-substrate-scale; or $R_{\mathrm{cg}} \sim L_{\mathrm{flow}}$, near-flow-scale), DCGT breaks down (§7).

In practice, $R_{\mathrm{cg}}$ is chosen anywhere in the scale-separated window; coarse-grained quantities are insensitive to the specific choice within the window (the hallmark of effective-theory regime stability).

### 3.2 Substrate-graph averaging

A **substrate-graph average** of a substrate-level quantity $\mathcal{Q}(u, t)$ at coarse-graining scale $R_{\mathrm{cg}}$ is:

$$
\langle \mathcal{Q}\rangle_{R_{\mathrm{cg}}}(\bar{u}, \bar{t}) = \frac{1}{V_{R_{\mathrm{cg}}}}\int_{|u - \bar{u}| < R_{\mathrm{cg}}}\int_{|t - \bar{t}| < R_{\mathrm{cg}}/c}\mathcal{Q}(u, t)\,d\mu_{\mathrm{substrate-graph}}
$$

where $V_{R_{\mathrm{cg}}}$ is the substrate-graph volume of the coarse-graining cell and $d\mu_{\mathrm{substrate-graph}}$ is the substrate-graph measure (substrate channels per substrate cell).

**Well-definedness.** By P03 (spatial homogeneity), translation-invariance of substrate-graph operations means the average depends only on $(\bar{u}, \bar{t})$ — the coarse-graining center — not on the specific substrate channels enumerated within the cell. By P04 (bandwidth additivity), substrate bandwidth contributions sum additively within the cell.

**Dimensional check:** $\langle\mathcal{Q}\rangle_{R_{\mathrm{cg}}}$ has the same dimensions as $\mathcal{Q}$ (averaging is dimensionless). ✓

### 3.3 What survives coarse-graining

Substrate-level content that varies on scales $\sim \ell_{\mathrm{ED}}$ is **averaged out**: substrate-graph microstructure (specific channel labels, specific commitment-event timings) becomes invisible at scale $R_{\mathrm{cg}}$.

Substrate-level content that varies on scales $\sim L_{\mathrm{flow}}$ **survives**: macroscopic flows of bandwidth, polarity, strain content are captured by the coarse-graining.

Substrate-level content at the intermediate scale $\sim R_{\mathrm{cg}}$ has partial visibility: it depends on the specific $R_{\mathrm{cg}}$ choice within the scale-separated window.

---

## 4. V1 Kernel → Continuum Diffusion Operator

### 4.1 V1 envelope at substrate-graph scale

By Paper_089, V1 has the canonical form:

$$
K_{V1}(x, x') = \theta(t - t')\,G(\sigma(x, x')/\ell_{\mathrm{ED}}^2).
$$

The envelope $G$ is bounded, finite-width with characteristic scale $\ell_{\mathrm{ED}}$, decaying outside the substrate-graph scale.

### 4.2 Coarse-graining V1 to a diffusion-type operator

Coarse-grain V1 at scale $R_{\mathrm{cg}}$ via the substrate-graph averaging of §3.2. For separations $|x - x'| \gg \ell_{\mathrm{ED}}$, the V1 envelope $G(\sigma/\ell_{\mathrm{ED}}^2)$ becomes effectively local at scale $R_{\mathrm{cg}}$ — the kernel acts like a **point-supported operator** with effective range $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}}$.

The continuum-limit operator $\hat{D}_{\mathrm{cont}}$ defined by:

$$
\hat{D}_{\mathrm{cont}}\,\psi(x) = \int K_{V1}(x, x')\,\psi(x')\,d^4x'
$$

(restricted to retarded support) reduces in the hydrodynamic window to a **local differential operator** acting on the coarse-grained field $\psi(\bar{x})$. The standard expansion (Taylor in $(x - x')/R_{\mathrm{cg}}$ to second order; constant + first + second derivative terms) gives:

$$
\hat{D}_{\mathrm{cont}}\,\psi(\bar{x}) \approx \left[a_0 + a_1\,\partial_t + D\,\nabla^2 + \mathcal{O}(\partial^3)\right]\psi(\bar{x})
$$

where:

- $a_0$ = $\int G\,d^4(\Delta x)$ (zeroth-moment integral of the V1 envelope).
- $a_1$ = $\int G\,\Delta t\,d^4(\Delta x)$ (first-moment in time).
- $D$ = $(1/6)\int G\,|\Delta\vec{x}|^2\,d^4(\Delta x)$ (second-moment in space; gives diffusion constant).

**Dimensional check:** $\hat{D}_{\mathrm{cont}}$ has dimensions of $[1/\mathrm{time}]$ when $G$ has dimensions $[1/\mathrm{length}^3 \cdot 1/\mathrm{time}]$ (for 3+1 D propagator-density convention); $D$ has dimensions $[\mathrm{length}^2/\mathrm{time}]$ as expected for diffusion constant. ✓

### 4.3 Diffusion-form result

In the hydrodynamic window, V1's coarse-grained action on substrate content reduces to a **diffusion-type continuum operator**:

$$
\hat{D}_{\mathrm{cont}} \approx \partial_t - D\,\nabla^2 + (\text{higher-order corrections})
$$

(after suitable normalization absorbing the zeroth-moment $a_0$). This is the substrate→continuum diffusion form: V1 cross-chain content propagates at the substrate level via finite-width retarded kernel, and coarse-grains to a continuum diffusion equation with diffusion constant $D$ set by V1's second-moment substrate-graph structure.

### 4.4 Where the diffusion constant comes from

The numerical value of $D$ is set by:

- V1's specific functional shape (envelope details inherited from substrate-coefficient anchoring).
- The substrate scale $\ell_{\mathrm{ED}}$.

For a generic V1 envelope $G \sim e^{-\sigma/\ell_{\mathrm{ED}}^2}$, $D \sim \ell_{\mathrm{ED}}^2/\tau_{V1}$ where $\tau_{V1} \sim \ell_{\mathrm{ED}}/c$. This gives $D \sim c\ell_{\mathrm{ED}}$ at the substrate scale.

In specific regimes (soft-matter, condensed-matter, BH), the effective $D$ is renormalized by substrate-coefficient matching to empirical values — **value-layer empirical content**, not substrate-derived. DCGT supplies the *form* (diffusion equation); the *coefficient* is matched.

---

## 5. V5 Kernel → Continuum Memory-Kernel Diffusion

### 5.1 V5 envelope

By Paper_090, V5 has the canonical form:

$$
K_{V5}(u_A, t_A; u_B, t_B) = \theta(t_A - t_B)\,F_{V5}(\sigma/\ell_{V5}^2, (t_A - t_B)/\tau_{V5}).
$$

V5 has both finite spatial extent ($\ell_{V5}$) and finite memory time ($\tau_{V5}$).

### 5.2 Coarse-graining V5 to memory-kernel diffusion

The same substrate-graph averaging of §3.2 applied to V5 yields a **memory-kernel diffusion operator** in the continuum:

$$
\hat{D}_{\mathrm{cont}}^{V5}\,\psi(\bar{x}, \bar{t}) = \int_0^\infty d\tau\,\mathcal{M}(\tau)\left[D_{V5}\,\nabla^2\psi(\bar{x}, \bar{t} - \tau) - \psi(\bar{x}, \bar{t} - \tau)/\tau_{V5}\right]
$$

where $\mathcal{M}(\tau)$ is the **memory kernel** inherited from V5's temporal envelope $F_{V5}$, $D_{V5}$ is the V5 diffusion constant (analog of §4.3), and $\tau_{V5}$ is the V5 memory time.

**Dimensional check:** $\mathcal{M}(\tau)$ has dimensions $[1/\mathrm{time}]$; $D_{V5}\nabla^2\psi$ has $[\psi/\mathrm{time}]$; $\psi/\tau_{V5}$ has $[\psi/\mathrm{time}]$; integral $\int d\tau$ has $[\mathrm{time}]$; total: $\hat{D}_{\mathrm{cont}}^{V5}\psi$ has $[\psi]$ — consistent with $\hat{D}$ being a differential / integral operator. ✓

### 5.3 Markovian limit

In the **Markovian limit** $\tau_{V5} \to 0$ (V5 memory time fast compared to flow timescale $L_{\mathrm{flow}}/c$), the memory kernel becomes $\mathcal{M}(\tau) \to \delta(\tau)$, and the operator reduces to a Markovian diffusion + decay form:

$$
\hat{D}_{\mathrm{cont}}^{V5,\,\mathrm{Markov}} \approx D_{V5}\,\nabla^2 - 1/\tau_{V5}.
$$

This is the substrate-level structural origin of standard Markovian diffusion + exponential relaxation in soft-matter (§6.1) and condensed-matter (§6.3) contexts.

### 5.4 Non-Markovian regime

In the **non-Markovian regime** ($\tau_{V5}$ comparable to flow timescale), the full memory kernel $\mathcal{M}(\tau)$ contributes. The resulting continuum equation is a **generalized diffusion equation with memory**:

$$
\partial_t\psi(\bar{x}, t) = \int_0^t \mathcal{M}(t - t')\,D_{V5}\,\nabla^2\psi(\bar{x}, t')\,dt' - \psi/\tau_{V5}.
$$

This is the substrate-level structural origin of non-Markovian behavior in soft-matter (Maxwell viscoelastic response with frequency-dependent moduli) and BH-radiation (non-thermal corrections to Hawking spectrum, Paper_047).

---

## 6. Cross-Domain Instantiations

### 6.1 Soft-matter Maxwell relaxation — form derived, value empirically matched

**Form (derived).** DCGT applied to V5 in the soft-matter Markovian limit (§5.3) produces the **exponential-decay form** of the Maxwell stress-relaxation modulus:

$$
G(t) = G_0\,e^{-t/\tau_{V5}^{\mathrm{soft}}}.
$$

The exponential form is a substrate-level structural consequence of V5's Markovian-limit envelope (§5.3).

**Numerical value (empirically matched, not derived).** In the soft-matter regime, $\tau_{V5}^{\mathrm{soft}}$ is **identified with the empirically-measured Maxwell relaxation time** $\tau_{\mathrm{Maxwell}}^{\mathrm{empirical}}$ via direct empirical matching:

$$
\tau_{V5}^{\mathrm{soft}} = \tau_{\mathrm{Maxwell}}^{\mathrm{empirical}} \quad \text{(empirical matching, not substrate-derived)}.
$$

**Honest framing (round-3 QC):** The numerical value of $\tau_{V5}^{\mathrm{soft}}$ in any specific polymer system is **inherited from rheometry** — it is the empirically-measured Maxwell relaxation time for that system. DCGT supplies the *form* (exponential decay); the *coefficient* $\tau_{V5}^{\mathrm{soft}}$ is matched to empirical data, not derived from substrate primitives.

Krieger–Dougherty viscosity and Cross / Carreau / Bird–Carreau constitutive laws emerge as DCGT continuum limits in different soft-matter regimes (high shear, low shear, multi-mode), with each regime's specific numerical coefficients similarly inherited via empirical matching.

### 6.2 QFT propagator hierarchy

In the QFT regime, V1/V5 coarse-graining (§4 + §5) produces standard QFT propagators:

- **Retarded propagator** $G_R$: V1 retarded support coarse-grained to continuum retarded propagator.
- **Feynman propagator** $G_F$: Wick rotation of V1 + V5 in the Euclidean continuation.
- **Advanced propagator** $G_A$: from $G_R$ via mathematical compositional closure (Paper_089 §6.1); not directly substrate-operational but mathematically derivable from $G_R$ via complex-analytic methods.

V1 finite-width supplies the substrate-level UV cutoff $\omega_c = c/\ell_{\mathrm{ED}}$ that becomes the standard QFT regulator (Pauli–Villars, dimensional, lattice) in the continuum limit.

### 6.3 Lieb–Robinson velocity bound — form by dimensional analogy

**A→dimensional-analogy (not derivation).** In the condensed-matter regime, DCGT applied to V5 in the Markovian limit suggests, **by dimensional analysis matching to the standard Lieb–Robinson theorem**, a velocity bound for entanglement-content propagation:

$$
v_{LR} \sim c_{V5}\cdot\frac{\ell_{V5}}{\tau_{V5}^{\mathrm{ent}}}.
$$

**Honest framing (round-3 QC):** This is **dimensional analogy**, not substrate-level derivation. The standard Lieb–Robinson theorem (Lieb–Robinson 1972 + later refinements) is a tight commutator-norm bound from Hamiltonian locality; its derivation requires Hamiltonian-level analysis of bounded local operators. ED's substrate-level $v_{LR}$ form is obtained by matching the substrate-level scales $\ell_{V5}$ and $\tau_{V5}^{\mathrm{ent}}$ to the standard LR-velocity dimensional structure. **The substrate-level mechanism that would derive an LR-type *tight* bound from substrate primitives alone is not supplied in this paper; it is invoked by dimensional analogy to the standard result.** The substrate-level $v_{LR}$ form is a defensible identification at the dimensional level, but it does not constitute a substrate-level proof of the Lieb–Robinson theorem.

### 6.4 BH curved-spacetime entanglement and KMS

In the BH near-horizon regime, V5 acquires imaginary-time periodicity (Paper_047 §3). DCGT applied to V5 in the Euclidean continuation produces the substrate-level KMS condition:

$$
\langle\phi(t_A)\phi(t_B)\rangle_{V5}^{\mathrm{Eucl}} = \langle\phi(t_A + i\beta_H)\phi(t_B)\rangle_{V5}^{\mathrm{Eucl}}, \quad \beta_H = 2\pi/\kappa,
$$

giving thermal Planck spectrum at $T_H = \kappa/(2\pi)$ (Paper_047 §4). The full Hawking spectrum derivation, including the substrate-level non-thermal $(\omega/\omega_c)^2$ corrections, is the subject of Paper_047.

### 6.5 The procedural unity

The four instantiations (§6.1–§6.4) are not four independent mechanisms — they are **one substrate→continuum procedure (DCGT) applied to one substrate primitive (V5)** across four regimes that differ in regime-specific $\tau_{V5}$, $\ell_{V5}$, and substrate-source content. The procedural unity is the cross-domain coherence claim of DCGT (paralleling Paper_090's structural unification of formalism across regimes).

---

## 7. DCGT Breakdown Conditions

### 7.1 Strong-gradient regimes

In regimes where $L_{\mathrm{flow}} \to R_{\mathrm{cg}}$ (gradient scale approaches coarse-graining scale), DCGT breaks down: the scale separation $R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$ fails.

**Empirical signature of breakdown:** continuum equations derived via DCGT no longer match substrate-level mechanism predictions. Specific examples:

- Shock waves: gradient scale collapses to substrate scale.
- Near-singularity content in BH evaporation late-stage.
- Strong-coupling soft-matter (gels, glasses) where collective-mode wavelength approaches $\ell_{V5}$.

### 7.2 Near-substrate-scale regimes

In regimes where $R_{\mathrm{cg}} \to \ell_{\mathrm{ED}}$ (coarse-graining scale approaches substrate scale), DCGT cannot resolve substrate-graph microstructure cleanly. Substrate-level effects (kernel finite-width, V5 memory, commitment-event statistics) become visible at coarse-grained level.

**Empirical signature of breakdown:** continuum equations require substrate-level corrections that scale as $(\ell_{\mathrm{ED}}/R_{\mathrm{cg}})^n$ for some $n > 0$. Specific examples:

- Trans-Planckian regime in Hawking spectrum (Paper_039 / Paper_047 — V5 cutoff at $\omega_c = c/\ell_P$).
- Sub-Planckian length-scale probes (hypothetical future high-energy physics).
- Near-Planck-mass BH evaporation late-stage (Paper_039 §6 — remnant scale).

### 7.3 Near-singularity regimes

In regimes where substrate-level stability-landscape gradients (P12) become large enough to trigger substrate-level commitment-event proliferation, DCGT's averaging breaks down because commitment events at substrate-scale are not coarse-grain-able.

**Empirical signature of breakdown:** discrete substrate-level commitment statistics become visible in continuum measurements. Specific examples:

- Quantum-measurement events at substrate-graph scale.
- Near-horizon information-blocking transitions (Paper_039 §3 — UR-1.2 failure).

### 7.4 Strong-curvature regimes (Arc ED-10 territory)

DCGT operates in flat-spacetime (or approximately-flat) regime. Strong-curvature regimes (near singularities, near horizons at substrate scale) require the Arc ED-10 curvature-emergence framework, not DCGT directly. The relationship between DCGT and Arc ED-10 is in-queue.

---

## 8. Falsification Criteria

### 8.1 Continuum equations fail to match substrate-level predictions

**Falsifier sentence:** *Empirical demonstration that continuum-level equations derived via DCGT (Maxwell relaxation, Newtonian potential, Hawking spectrum, Lieb–Robinson velocity) fail to match substrate-level predictions within the hydrodynamic-window scale separation — i.e., systematic discrepancies between substrate-level mechanism and continuum-level observation that cannot be absorbed into value-layer coefficient adjustment — would falsify DCGT.*

### 8.2 Hydrodynamic-window failure outside expected breakdown regimes

**Falsifier sentence:** *Empirical demonstration that DCGT breaks down in a regime that should satisfy $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$ would falsify §3.1's scale-separation regime condition.*

### 8.3 Diffusion-form failure

**Falsifier sentence:** *Empirical demonstration that V1 coarse-graining does not produce a diffusion-type operator in the continuum limit — e.g., produces a non-local integral operator at scales $R_{\mathrm{cg}} \gg \ell_{\mathrm{ED}}$ — would falsify §4's diffusion-form derivation.*

### 8.4 Memory-kernel structure failure

**Falsifier sentence:** *Empirical demonstration that V5 coarse-graining does not produce a memory-kernel operator with structure inherited from V5 envelope — e.g., that soft-matter Maxwell relaxation does not follow the predicted memory-kernel form — would falsify §5.*

### 8.5 Cross-domain procedural unity failure

**Falsifier sentence:** *Empirical demonstration that the four cross-domain instantiations (§6.1–§6.4) require *different* substrate→continuum procedures, not the same DCGT applied differently to different $\tau_{V5}$ — would falsify the procedural unity claim and reduce DCGT's wedge content.*

### 8.6 Strong-gradient failure pattern violates prediction

**Falsifier sentence:** *Empirical demonstration that DCGT breakdown in strong-gradient regimes (§7.1) follows a pattern inconsistent with substrate-level gradient-scale-vs-coarse-graining-scale failure — e.g., breakdown signatures inconsistent with substrate-graph commitment-event proliferation — would falsify the §7 breakdown taxonomy.*

---

## 9. Position Statement

The **Diffusion Coarse-Graining Theorem (DCGT)** is a downstream structural result in the ED Generative Primitives System. Given the postulated primitives + V1 inheritance + V5 dependence + the hydrodynamic-window scale separation $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$ (regime condition), substrate-level kernel-mediated content coarse-grains to continuum diffusion-type / propagator-type / constitutive-law equations:

- V1 → continuum diffusion operator (§4).
- V5 → continuum memory-kernel diffusion (§5).
- Cross-domain instantiations: Maxwell relaxation (soft-matter), QFT propagator hierarchy, Lieb–Robinson velocity, KMS-thermal structure at horizons (§6).

The procedural unity — one substrate→continuum procedure applied across multiple regimes — is the cross-domain coherence claim of DCGT.

DCGT specifies breakdown conditions (§7): strong-gradient, near-substrate-scale, near-singularity, strong-curvature regimes are where substrate-level mechanism is *not* captured by continuum description. These breakdowns are predictions, not failures: they distinguish ED from continuum-only frameworks and provide falsifiability handles.

What this paper claims:

- Given the postulated primitives + V1/V5 + hydrodynamic-window regime, DCGT produces continuum diffusion-type / propagator-type equations as substrate-level structural consequences.
- The four cross-domain instantiations (soft-matter, QFT, condensed-matter, BH) are one substrate→continuum procedure applied to one substrate primitive (V5) across regimes.
- DCGT is load-bearing for Papers_027 (Newton), 047 (Hawking), 090 (V5 cross-domain), 056 (Class-A coarse-grained matching).

What this paper does *not* claim:

- The substrate primitives are not derived (Paper_087).
- DCGT is not the only substrate→continuum bridge.
- Continuum-level transport coefficients are not derived; inherited.
- DCGT does not apply outside the hydrodynamic window.
- DCGT does not derive Einstein equations or standard QFT renormalization.

The empirical case rests on cross-domain reach: DCGT is load-bearing across multiple arcs; falsification in any arc traces back to DCGT or to the arc-specific application.

**Series context.** Paper_073 of the soft-matter / cross-domain bridge. Used by:

- Paper_027 (Newton's $G$).
- Paper_029 (cosmic decoupling — coarse-grained matching).
- Paper_039 (BH horizon decoupling — substrate→geometric).
- Paper_047 (Hawking spectrum — substrate→thermal).
- Paper_090 (V5 cross-chain — substrate→continuum across regimes).

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Position paper:** Paper_087.
- **Paper_089 (V1):** kernel inheritance.
- **Paper_090 (V5):** cross-chain kernel; primary downstream user.
- **Paper_027 (Newton's $G$):** uses DCGT for V1 cumulative-strain → continuum Newtonian potential.
- **Paper_047 (Hawking Spectrum):** uses DCGT for V5 substrate KMS → semiclassical thermal spectrum.
- **Pre-pivot Arc-D memos (Arc-D closure 2026-04-30):** substrate-level Arc-D legacy material.

### Glossary

- **DCGT (Diffusion Coarse-Graining Theorem).** Substrate→continuum bridge: V1/V5 substrate-level kernels coarse-grain to continuum diffusion-type / propagator-type / constitutive-law equations under the hydrodynamic-window scale separation.
- **Hydrodynamic-window scale separation.** $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$. Regime condition under which DCGT applies.
- **Coarse-graining scale $R_{\mathrm{cg}}$.** Spatial/temporal extent of substrate-graph averaging cell.
- **Macroscopic flow scale $L_{\mathrm{flow}}$.** Spatial/temporal extent over which continuum quantities vary.
- **Substrate-graph averaging.** Local averaging of substrate-level quantities over coarse-graining cell via substrate-graph measure.
- **Memory-kernel diffusion.** Generalized diffusion equation with V5-inherited memory kernel; non-Markovian regime.
- **Markovian limit.** $\tau_{V5} \to 0$ limit; memory kernel reduces to $\delta$-function; standard diffusion + decay.
- **Procedural unity.** One substrate→continuum procedure (DCGT) applied across multiple regimes; cross-domain coherence claim.
- **Breakdown regimes.** Strong-gradient, near-substrate-scale, near-singularity, strong-curvature — regimes where DCGT does not apply.

---

**End of Paper_073.**

*Wave-2 Generative Paper — Soft-Matter Arc / Cross-Domain Bridge Foundation. Canonical reference for the substrate→continuum coarse-graining procedure used across ED arcs.*
