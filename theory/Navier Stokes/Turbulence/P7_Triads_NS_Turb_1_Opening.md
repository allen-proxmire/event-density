# NS-Turb-1 — P7 ↔ Turbulence Arc Opening: Triadic Structure Mapping

**Date:** 2026-04-30
**Status:** Arc opening. **Headline hypothesis to test:** P7's triadic harmonic-generation structure (3–6% amplitude ratio, weak coupling ~0.03, k=3 from k=1) may be the architectural template underlying NS triadic Fourier cascade, with the advective term as physical instantiation. **Honest a-priori caveat:** triadic Fourier structure ($\mathbf{k}_1 + \mathbf{k}_2 + \mathbf{k}_3 = 0$) is a generic property of any quadratic-in-field nonlinearity, not specific to P7. NS-2.08 + NS-3.02b previously established that advection is not P7-class structurally (index-structure mismatch: P7 is symmetric quadratic-in-gradients; advection is bilinear field × gradient with directional preference). This arc tests whether a *non-trivial* mapping exists despite the index-structure mismatch — e.g., at the level of harmonic-amplitude ratios or mode-coupling structure. Worth running.
**Companions:** [`../../Architectural_Canon.md`](../../Architectural_Canon.md) (P7), [`../NS-2.08_ED-PDE_Direct_Mapping.md`](../NS-2.08_ED-PDE_Direct_Mapping.md), [`../NS-3.02b_Multi_Lyapunov_Audit.md`](../NS-3.02b_Multi_Lyapunov_Audit.md), [`../ED-NS_Exploration_Roadmap.md`](../ED-NS_Exploration_Roadmap.md) (#1 route).

---

## 1. Purpose

This arc investigates whether ED's P7 triadic compositional structure corresponds to the triadic Fourier interactions in the Navier-Stokes nonlinearity, and whether the mapping provides an architectural explanation of the turbulence energy cascade.

The arc is exploratory with high potential value. From the [`ED-NS_Exploration_Roadmap.md`](../ED-NS_Exploration_Roadmap.md) (#1 route): "P7's 3–6% amplitude ratio with weak coupling ~0.03 are concrete numbers that either match measured turbulence triad statistics or don't. If it matches, ED supplies a structural prediction about turbulence cascade that standard NS doesn't. If it doesn't match, the result is informative (rules out a specific structural identification)."

**Honest a-priori position before the arc work begins:**

- Triadic Fourier structure ($\mathbf{k}_1 + \mathbf{k}_2 + \mathbf{k}_3 = 0$) is a *generic* feature of any quadratic-in-field nonlinearity. Both P7 and NS's advective term produce triadic Fourier interactions, as do many other unrelated nonlinear PDEs.
- The *specific content* of the triadic structure differs: P7 is symmetric quadratic in gradients of a scalar; NS's advection is bilinear field-times-gradient with transport-directional preference.
- NS-2.08 §5 + NS-3.02b §5 established that advection is structurally non-P7 due to this index-structure mismatch. The arc must address this finding directly.

The arc therefore tests whether a *non-trivial* mapping survives despite the index-structure mismatch — at the level of harmonic-amplitude ratios, mode-coupling weak-coupling-strength, or other quantitative structural content where P7 makes specific predictions and NS triadic statistics can be compared.

This arc is **architectural exploration**, not Clay-NS work. Even a negative result is informative.

---

## 2. Inputs

| Input | Source |
|---|---|
| P7 — nonlinear triad coupling principle | [`../../Architectural_Canon.md`](../../Architectural_Canon.md) §2 (P7) |
| Universal invariants: triad amplitude 3–6%, weak coupling ~0.03 | [`../../Universal_Invariants.md`](../../Universal_Invariants.md) §3 + Canon §3 |
| ED vector-extension canon (P-level field-type agnosticism; triads apply per-component) | [`../../Architectural_Canon_Vector_Extension.md`](../../Architectural_Canon_Vector_Extension.md) §3 |
| NS-2.08: advection as fluid-mechanical-addition not native to ED | [`../NS-2.08_ED-PDE_Direct_Mapping.md`](../NS-2.08_ED-PDE_Direct_Mapping.md) §5 |
| NS-3.02b: advective vortex-stretching breaks gradient-norm Lyapunov | [`../NS-3.02b_Multi_Lyapunov_Audit.md`](../NS-3.02b_Multi_Lyapunov_Audit.md) §3.4 + §5 |
| NS triadic cascade (standard turbulence theory): $\mathbf{k}+\mathbf{p}+\mathbf{q}=0$ structure | Standard literature (Frisch, Pope, Lesieur) |

---

## 3. Non-Goals

This arc is **purely architectural exploration**. Specific exclusions:

- **Not attempting to solve turbulence.** The Kolmogorov 5/3 spectrum, intermittency exponents, anomalous scaling laws — these remain open empirical questions in standard turbulence and the arc does not pretend to derive them.
- **Not attempting Clay-NS regularity.** That question closed at NS-3 Intermediate verdict; this arc does not reopen it.
- **Not attempting full spectral closure** (e.g., EDQNM, DIA, LRA closure schemes). These require dynamical-modeling content beyond architectural mapping.
- **Not attempting LES / RANS / sub-grid modeling.** The arc does not produce a turbulence model.

The arc's deliverable is a **structural mapping verdict**: does P7 architecturally underlie the NS triadic cascade, in any quantitatively or qualitatively meaningful sense, beyond the trivial "both produce triadic Fourier structure"?

---

## 4. Step 1 — NS Nonlinearity in Fourier Triad Form

The advective term $(\mathbf{u} \cdot \nabla)\mathbf{u}$ in NS, written in incompressible form ($\nabla \cdot \mathbf{u} = 0$), can be expressed equivalently as $\nabla \cdot (\mathbf{u} \otimes \mathbf{u})$. Take Fourier transform of the i-component of the momentum equation:

$$\partial_t \hat u_i(\mathbf{k}) + i k_j \widehat{(u_i u_j)}(\mathbf{k}) = -i k_i \hat p(\mathbf{k}) / \rho - \nu k^2 \hat u_i(\mathbf{k}) + \hat f_i(\mathbf{k}).$$

The convolution structure of the bilinear Fourier transform gives:

$$\widehat{(u_i u_j)}(\mathbf{k}) = \int \hat u_i(\mathbf{p}) \, \hat u_j(\mathbf{q}) \, \delta(\mathbf{p} + \mathbf{q} - \mathbf{k}) \, d^3p \, d^3q,$$

which under the convention $\mathbf{k} + \mathbf{p} + \mathbf{q} = 0$ (after relabeling) gives the standard turbulence-triad form:

$$\partial_t \hat u_i(\mathbf{k}) \supset \sum_{\mathbf{p}+\mathbf{q}+\mathbf{k}=0} T_{ij\ell}(\mathbf{k}, \mathbf{p}, \mathbf{q}) \, \hat u_j(\mathbf{p}) \, \hat u_\ell(\mathbf{q}),$$

with interaction coefficient

$$T_{ij\ell}(\mathbf{k}, \mathbf{p}, \mathbf{q}) = -\frac{i}{2} \left[k_\ell \, P_{ij}(\mathbf{k}) + k_j \, P_{i\ell}(\mathbf{k})\right],$$

where $P_{ij}(\mathbf{k}) = \delta_{ij} - k_i k_j / k^2$ is the transverse projector enforcing incompressibility (it eliminates the pressure term via the Helmholtz decomposition).

**Key structural features of NS triads:**
- **Triad constraint** $\mathbf{k} + \mathbf{p} + \mathbf{q} = 0$: momentum conservation in mode-mode interactions.
- **Tensorial coefficient** $T_{ij\ell}$: depends on wavenumber direction (via $\mathbf{k} \cdot \mathbf{u}$ structure) and incompressibility (via $P_{ij}$).
- **Bilinear in $\hat u$**: quadratic-in-field nonlinearity.
- **Energy-conserving structure**: the triadic interactions exchange energy between modes without dissipation; viscous $-\nu k^2$ does the dissipating separately.
- **Asymmetric in indices**: $T_{ij\ell}(\mathbf{k}, \mathbf{p}, \mathbf{q})$ has specific transport-directional structure, not symmetric in (j, ℓ).

---

## 5. Step 2 — P7 Triadic Composition Rule

P7 from [`../../Architectural_Canon.md`](../../Architectural_Canon.md) §2:

> *The nonlinear term $M'(\rho)|\nabla\rho|^2$ generates higher-harmonic content, especially k=3 from k=1, with an invariant amplitude ratio under multiplicative perturbations. Coupling strength is weak (~0.03); harmonic generation is 3–6% of fundamental. No mode locking, no chaos, no bifurcations.*

In Fourier space, the P7 nonlinearity acts as follows. Writing $\rho(x, t) = \sum_k \hat\rho(k, t) e^{ikx}$ for a single-spatial-dimension case (the simplest illustrative setting; vector extensions per Architectural_Canon_Vector_Extension are component-wise):

$$|\nabla \rho|^2 \to \mathcal{F}\big[(i k \hat\rho) (i k' \hat\rho)\big] = -k k' \hat\rho(k) \hat\rho(k')$$

with convolution constraint $k + k' = k_\mathrm{result}$. Combined with $M'(\rho)$ (a function of $\rho$), the full P7 nonlinearity is *cubic* in $\hat\rho$ at the Fourier level:

$$M'(\rho) |\nabla\rho|^2 \to \sum_{k_1 + k_2 + k_3 = k_\mathrm{result}} M''\hat\rho(k_1) \cdot (-k_2 k_3) \hat\rho(k_2)\hat\rho(k_3) + \cdots$$

(at leading order in $M$ expansion around equilibrium; full expression depends on $M$'s specific form).

**Structural features of P7 nonlinearity:**
- **Triadic Fourier structure** $k_1 + k_2 + k_3 = k_\mathrm{result}$ (same generic structure as NS).
- **Weak coupling** (~0.03 amplitude per UDM / Universal_Invariants): generates 3–6% harmonics.
- **Specific harmonic-generation pattern**: k=3 from k=1 driving as canonical case (though general triads admitted).
- **Symmetric quadratic-in-gradients**: $|\nabla\rho|^2$ is symmetric scalar; P7's interaction coefficient does not have the directional-transport asymmetry of NS's $T_{ij\ell}$.
- **Cubic in $\hat\rho$** at leading order (because $M'$ is itself a function of $\rho$, expanding to first order in $\rho$ gives an additional $\hat\rho$ factor).

P7 is therefore *qualitatively* triadic but with structurally different content from NS's bilinear-in-velocity triads.

### 5.1 Honest re-reading of "P7 as triadic composition"

The user's spec described P7 as having "symmetry, associativity, and compositional inheritance properties." This is closer to a generic algebraic-triadic-rule description than to P7's specific canon content. **P7 in canon is not literally a triadic composition rule with associativity** — it is a statement about harmonic generation by the gradient self-coupling $M'(\rho)|\nabla\rho|^2$ in the canonical PDE.

A "triadic composition rule" interpretation of P7 is an interpretation, not the canon content. The arc must be honest about which P7 it is testing:
- **Strict canon P7:** harmonic generation 3–6% with k=3 from k=1, in scalar PDE under multiplicative perturbations.
- **Generalized triadic-composition reading:** triadic Fourier structure with symmetry / associativity / inheritance.

The arc proceeds with strict canon P7 as the primary object; the generalized reading would require additional architectural articulation.

---

## 6. Step 3 — Structural Comparison

### 6.1 Structural matches

- **Both have triadic Fourier structure.** $k_1 + k_2 + k_3 = 0$ (or = $k_\mathrm{out}$) momentum-conservation in mode-mode interactions.
- **Both involve quadratic / nonlinear field coupling.** P7 is quadratic in gradients (cubic in $\hat\rho$ at leading order in $M$); NS is bilinear in velocity (quadratic in $\hat u$).
- **Both are weak-coupling regimes.** P7 explicitly weak-coupling per Canon §3 (~0.03). NS turbulence at moderate Reynolds number can be analyzed perturbatively via weak-coupling closures (DIA, EDQNM); at high Re the weak-coupling assumption breaks down.

### 6.2 Structural mismatches

- **Field type.** P7 is scalar-field; NS is vector-field. (Resolvable via Architectural_Canon_Vector_Extension component-wise application.)
- **Index structure of coupling.** NS triadic coefficient $T_{ij\ell}(\mathbf{k}, \mathbf{p}, \mathbf{q})$ has specific transport-directional + projection structure. P7's triadic coupling is symmetric quadratic-in-gradients without transport-directional preference. **This is the structural feature NS-2.08 §5 + NS-3.02b §5 identified as the "advection is non-ED" mismatch.**
- **Energy-transfer character.** NS triads conserve energy across modes (the cascade redistributes but does not create/destroy kinetic energy in the inertial range). P7 generates harmonic content from a fundamental but the underlying energy bookkeeping differs (the canonical PDE has a Lyapunov-decreasing energy that P7's harmonic generation operates within, not across-mode-conservatively).
- **Magnitude.** P7's 3–6% amplitude ratio is for steady-state response of the canonical PDE to multiplicative perturbations. NS turbulence's analogous quantity (whatever it is — e.g., second-order triad energy-transfer correlation) requires careful definition before comparison.

### 6.3 Possible mapping hypotheses

Given the matches and mismatches, three candidate mapping hypotheses worth testing:

**H1 — Generic triadic similarity (weak claim).** Both produce triadic Fourier interactions. This is generic to quadratic-in-field nonlinearities and not specific to P7. Probably true but uninteresting; doesn't establish ED-architectural insight beyond "NS has a quadratic nonlinearity."

**H2 — Weak-coupling amplitude correspondence (intermediate claim).** P7's 3–6% amplitude per perturbation might correspond to a turbulence-cascade quantity like fractional energy transfer per triad in the inertial range. This would require careful definition of the corresponding turbulence quantity and quantitative comparison. Could be tested if a clean quantitative observable can be defined.

**H3 — Architectural-template claim (strong claim).** P7's specific structural content (symmetric quadratic-in-gradients with weak coupling) is a coarse-grained shadow of NS's triadic cascade, with the advective term as the underlying mechanism. This requires reconciling with NS-2.08 + NS-3.02b's finding that advection is not P7-class structurally. Would need either (a) a structural argument that the index-structure mismatch is irrelevant at coarse-grained Fourier level, or (b) a refinement of the strict canon P7 to admit transport-directional content.

The arc proceeds with H2 as the primary testable hypothesis (intermediate ambition; clean numeric comparison if observable can be defined). H3 is the speculative target; if H2 succeeds and a structural argument resolves the index-structure mismatch, H3 becomes investigable.

---

## 7. Step 4 — Hypothesis: P7 as Architectural Template for Energy Cascade

### 7.1 Working hypothesis

P7's triadic harmonic-generation structure may be the architectural template underlying the NS triadic cascade. Specifically:

- ED's universal-invariant triad amplitude (3–6%) corresponds to a turbulence-cascade quantity at the appropriate Fourier-level definition.
- The weak-coupling structure (~0.03) corresponds to inertial-range cascade properties.
- The "k=3 from k=1" canonical case corresponds to the specific harmonic-generation pattern observed in turbulence cascades at small-amplitude perturbations.

### 7.2 What would confirm the hypothesis

A successful confirmation would identify a turbulence-statistics quantity $Q_\mathrm{turb}$ such that:
- $Q_\mathrm{turb}$ is a triadic Fourier quantity (mode-mode interaction-related).
- $Q_\mathrm{turb}$ has an empirical value or theoretical prediction at order ~3–6% (matching P7's amplitude).
- $Q_\mathrm{turb}$ has a weak-coupling structure (matching P7's ~0.03 coupling).

If such $Q_\mathrm{turb}$ exists and matches, the hypothesis is supported. If it doesn't exist or doesn't match, the hypothesis is rejected.

### 7.3 What would refute the hypothesis

The hypothesis is refuted if:
- No turbulence-cascade quantity can be identified that maps onto P7's amplitude/coupling structure.
- The structural mismatches identified in §6.2 (index structure, energy-transfer character) are not reconcilable with the matches.
- The 3–6% / 0.03 numbers are specific to P7's scalar-PDE setting and don't survive the vector-extension to NS.

### 7.4 Status

This is a **hypothesis to be tested in NS-Turb-2 through NS-Turb-5**, not a result of NS-Turb-1. The arc opening establishes the question and the architectural mapping framework; subsequent memos will perform the quantitative comparison and verdict.

**Honest aggregate:** the hypothesis is plausible at the qualitative level (both have triadic structure) but faces real obstacles at the structural level (index-structure mismatch already identified in NS-2.08 + NS-3.02b). The arc is worth running to deliver a clean verdict — affirmative would be significant (ED supplies a structural prediction about turbulence); negative is informative (rules out a specific identification and clarifies why advection is non-ED structurally).

---

## 8. Recommended Next Steps

In priority order. The arc opens here; subsequent memos perform the substantive analysis.

1. **NS-Turb-2 — Energy-Transfer Expression in Triad Form.** File: `theory/Navier Stokes/Turbulence/P7_Triads_NS_Turb_2_Energy_Transfer.md`. Derive the standard NS triadic energy-transfer expression $T(\mathbf{k}, \mathbf{p}, \mathbf{q})$ and identify the candidate "amplitude ratio" or "fractional-transfer-per-triad" quantity that could correspond to P7's 3–6% amplitude. Define the comparison observable cleanly. Estimated 1–2 sessions.

2. **NS-Turb-3 — Test P7 Inheritance Properties Against Turbulence Triads.** File: `theory/Navier Stokes/Turbulence/P7_Triads_NS_Turb_3_Inheritance.md`. Compare P7's structural inheritance properties (symmetry, weak-coupling invariance, k=3 from k=1 specificity) against turbulence-triad statistics. Quantitative if possible; qualitative if not. Estimated 1–2 sessions.

3. **NS-Turb-4 — Identify Where P7 Fails (If It Does).** File: `theory/Navier Stokes/Turbulence/P7_Triads_NS_Turb_4_Failure_Modes.md`. Honest audit of mismatches. Three candidates from §6.2 / NS-2.08 / NS-3.02b: index-structure asymmetry; energy-transfer-character difference; magnitude calibration. Estimated 1 session.

4. **NS-Turb-5 — Architectural Classification of Turbulence.** File: `theory/Navier Stokes/Turbulence/P7_Triads_NS_Turb_5_Synthesis.md`. Aggregate findings into a verdict: H1 (trivially true — generic triadic structure), H2 (weak-coupling amplitude correspondence — succeeded / failed / partial), H3 (full architectural template — succeeded / failed / partial). Honest synthesis whether ED supplies a non-trivial structural prediction about turbulence. Estimated 1 session.

### Decisions for you

- **Confirm arc opening framework.** Three hypotheses (H1 generic, H2 amplitude-correspondence, H3 architectural-template); arc proceeds with H2 as primary test, H3 as speculative target.
- **Confirm scope: architectural mapping only.** Not turbulence solution, not Clay-NS, not closure modeling.
- **Confirm next deliverable as NS-Turb-2** (energy-transfer expression in triad form, define comparison observable).
- **Note the structural challenge upfront.** NS-2.08 + NS-3.02b already identified that advection is not P7-class via index-structure mismatch. The arc must address this directly; an affirmative result would need to reconcile the mismatch.

---

*NS-Turb-1 arc opened. P7 ↔ NS-turbulence triadic-structure mapping investigated as exploratory architectural arc. Three hypotheses identified (H1 generic — trivially true; H2 amplitude-correspondence — testable if observable can be defined; H3 architectural-template — speculative, requires reconciling NS-2.08/NS-3.02b finding that advection is non-P7 structurally). Arc proceeds with H2 as primary testable hypothesis. Honest a-priori: triadic Fourier structure is generic to quadratic nonlinearities; specific-content matching is the substantive question. Worth running for clean verdict regardless of outcome.*
