# Q.7 Memo 02 — W3 + W4: τ_g Excitation vs Background + Vertex-to-Worldline Lifting (R-5 Partial + R-3 Q.7-Side Closure)

**Stage:** Arc Q · Q.7 · Memo 02 (load-bearing W3 + W4 derivation; R-5 partial closure; R-3 Q.7-side closure)
**Date:** 2026-04-26
**Location:** `arcs/arc-Q/`
**Goal:** Discharge **R-5 partial** (vacuum-field aspect of $\tau_g$'s vacuum-vs-particle status) by deriving W3, and discharge **R-3 Q.7-side** (per-worldline accounting integrating Q.3's vertex-anchored commitment) by deriving W4. Establish the structural distinction between $\tau_g$ as propagating excitation versus $\tau_g$ as background field, and complete the per-worldline lifting of Q.3 V4's vertex-density commitment rate into the affine-parameter framework supplied by Q.7 Memo 01's W1.
**Predecessors:** Q.1 / Q.2 / Q.3 trajectory · [`09_Q7_memo_00_outline.md`](09_Q7_memo_00_outline.md) (Q.7 Memo 00) · [`10_Q7_memo_01_lightlike_worldline.md`](10_Q7_memo_01_lightlike_worldline.md) (W1 + W2 closed CANDIDATE-FORCED; R-1 CLOSED CANDIDATE-FORCED at Q.7 Memo 01; affine-parameter machinery + second-quantised operator framework established)
**Status:** Technical derivation memo. Operates under strict forbidden-input discipline (per Q.7 Memo 00 §5): no R-5 completion (Q.8 work), no full vacuum-state content beyond background-field aspect, no SM specifics, no Higgs / generations / coupling constants, no F-M8 cascade target, no Yang-Mills / BRST as derivation premise. Inherits Q.2 + Q.3's CLOSED CANDIDATE-FORCED commitments + Q.7 Memo 01's W1 + W2 closures + Theorems 1–16 (Theorems 6, 7, 8, 9 directly relevant).
**Purpose:** State and discharge W3 + W4 with the strongest defensible verdict so the Q.7 substage advances to W5 (pre-vacuum structure) and the Q.7 verdict + cascade in Memo 03 (or Memo 04 if additional substantive work proves necessary).

---

## 1. The W3 and W4 Questions Restated

### 1.1 W3 question

**What does it mean for $\tau_g$ to behave as a propagating excitation versus as a background field at the worldline level?**

Background: Q.7 Memo 01 W2 established the second-quantised operator framework — field operator $\hat{A}^a_\mu(x)$, mode expansion in null momentum modes, creation/annihilation operators satisfying canonical commutation per Theorem 6. W3's substantive content is to specify the *structural distinction* between two operational interpretations of $\tau_g$:

- **$\tau_g$ as excitation:** propagating one-particle (or multi-particle) states $\hat{a}^{a, \sigma \dagger}_k | \cdot \rangle$ with worldline-supported amplitudes — the particle-aspect of $\tau_g$'s status.
- **$\tau_g$ as background field:** non-trivial expectation value $\langle \hat{A}^a_\mu(x) \rangle$ in some structural state — the background-field aspect of $\tau_g$'s status, *not* worldline-supported but rather field-extended.

Empirically, electromagnetic and gauge fields exhibit both behaviours: photons as discrete particles propagating on null worldlines; classical electromagnetic fields as background-field configurations sourced by charge distributions. ED's analog requires both interpretations to be structurally clean and mutually consistent.

W3 is the substantive content of **R-5 partial** (the vacuum-field aspect of R-5; the zero-point aspect remains R-5 completion at Q.8).

### 1.2 W4 question

**How does the vertex-anchored commitment rule from Q.3 V4 lift to per-worldline accounting in the affine-parameter framework supplied by Q.7 Memo 01's W1?**

Background: Q.3 V4 established that $\tau_g$'s commitment events are sourced at vertex types T1–T4 with vertex-density-dependent commitment rate $dN_{\text{commit}} / d\lambda = \rho_V(\lambda)$. Q.7 Memo 01's W1 supplied the affine parameter $\lambda$ as the natural per-worldline parametrisation for null curves. W4's substantive content is to *integrate* these — establish the per-worldline accounting that integrates vertex-density commitment rate with Phase-1's general commitment-dynamics specification (Primitive 11), in the affine-parameter framework.

W4 closes the Q.7-side of R-3 (vertex-anchored commitment for $\tau_g$). The Q.3-side closed at Q.3 Memo 02; the Q.7-side closes here at Q.7 Memo 02. Together they constitute R-3's substantive structural closure.

### 1.3 How W3 and W4 jointly close R-5 partial and R-3 Q.7-side

R-5 partial closes via W3: the vacuum-field aspect of $\tau_g$'s status is the "$\tau_g$ as background field" interpretation. W3 specifies what "background field" means at the worldline level (non-worldline-supported expectation value of the field operator) and verifies its structural admissibility.

R-3 Q.7-side closes via W4: the per-worldline accounting integrating vertex-anchored commitment with the affine-parameter framework is the substantive Q.7-side content of R-3.

W3 and W4 are independent derivations — W3 addresses the vacuum-field-vs-particle distinction; W4 addresses the per-worldline accounting integration — but both build on Q.7 Memo 01's W1 + W2 closure and Q.3's V1–V4 closure.

### 1.4 Outcome criteria

For W3:
- **CANDIDATE-FORCED:** the excitation-vs-background distinction is structurally admissible; both interpretations are well-defined and mutually consistent. Anticipated default.
- **CANDIDATE-admissible:** distinction admissible but uniqueness gaps (e.g., the boundary between "excitation" and "background" is not structurally sharp).
- **REFUTED:** the distinction cannot be specified consistently — would force restriction of $\tau_g$'s interpretation to one or the other.

For W4:
- **CANDIDATE-FORCED:** vertex-to-worldline lifting closes affirmatively; per-worldline accounting integrates vertex-density commitment rate with Phase-1 commitment-dynamics in the affine-parameter framework. Anticipated default.
- **CANDIDATE-admissible:** lifting admissible but with gaps (e.g., requires additional content beyond Q.7-internal inputs).
- **REFUTED:** lifting fails — would force revision of either the vertex-density commitment rate or Primitive 11's general specification.

---

## 2. Structural Commitments for W3 (τ_g Excitation vs Background)

### 2.1 The structural distinction

W3 defines the structural distinction between the two interpretations of $\tau_g$ at the worldline level:

#### 2.1.1 (E) τ_g as propagating excitation (worldline-supported)

A *propagating excitation* of $\tau_g$ is a Fock-space state of the form:

$$
| \psi_{\text{exc}} \rangle = \int \frac{d^3 k}{(2\pi)^3 \, 2|k^0|} \sum_\sigma f^{a, \sigma}(k) \, \hat{a}^{a, \sigma \dagger}_k | \Omega \rangle
$$

where $f^{a, \sigma}(k)$ is a wavepacket profile (Lorentz-invariant, gauge-invariant per Q.3 V3 inheritance) and $|\Omega\rangle$ is the (Q.8-deferred) vacuum state. The expectation value of the field operator in this state is:

$$
\langle \psi_{\text{exc}} | \hat{A}^a_\mu(x) | \psi_{\text{exc}} \rangle = 0
$$

(for a single-mode excitation; the field operator's expectation vanishes because $\hat{a}$ and $\hat{a}^\dagger$ have zero diagonal expectation in number-eigenstates). The *position-localised* content of the excitation (the support of $|f^{a, \sigma}(x)|^2$ where $f(x)$ is the spatial Fourier transform of $f(k)$) traces out a null worldline as time progresses, per Q.7 Memo 01 W2 §3.2 (expectation-value trajectory interpretation, equivalent to support-curve interpretation).

#### 2.1.2 (B) τ_g as background field (non-worldline-supported)

A *background field* configuration of $\tau_g$ is a state of the form:

$$
| \Phi_{\text{bg}} \rangle : \quad \langle \Phi_{\text{bg}} | \hat{A}^a_\mu(x) | \Phi_{\text{bg}} \rangle = A^{a, \text{cl}}_\mu(x) \neq 0
$$

where $A^{a, \text{cl}}_\mu(x)$ is a non-trivial classical field configuration on the spacetime manifold. Such states include coherent states (Glauber-style displaced vacuum states) and non-trivial vacuum states with macroscopic field expectation values.

The background field $A^{a, \text{cl}}_\mu(x)$ is *not* worldline-supported: it is a smooth field configuration extended over the spacetime manifold, with no concentration on any particular null curve. Its physical content (energy density, gauge-invariant field-strength content) is computed from the field configuration itself, not from per-worldline accounting.

#### 2.1.3 Excitations on top of a background

The most general state combines both: a coherent state $|\Phi_{\text{bg}}\rangle$ plus an excitation $|\psi_{\text{exc}}\rangle$ above it. The combined state has:

- Background contribution: $A^{a, \text{cl}}_\mu(x)$ (the mean field).
- Excitation contribution: per-worldline propagating quanta on top of the background.

Standard QFT terminology: this is the "background-field method" with field operators decomposed as $\hat{A}^a_\mu = A^{a, \text{cl}}_\mu + \hat{a}^a_\mu$ (background + fluctuation). ED's analog inherits this structural decomposition without invoking the QFT background-field-method machinery as derivation premise.

### 2.2 Minimal structural criteria

For interpretation (E), the structural criterion is:

- **(E-1) Zero field expectation:** $\langle \hat{A}^a_\mu(x) \rangle = 0$ (or only the background part if combined with (B)).
- **(E-2) Worldline support:** the position-localised content of the state traces a null worldline as time progresses.
- **(E-3) Vertex-mediated commitment:** commitment events for the excitation are sourced at vertex events along its null worldline (per Q.3 V4 inheritance + W4 integration below).

For interpretation (B), the structural criterion is:

- **(B-1) Non-zero field expectation:** $\langle \hat{A}^a_\mu(x) \rangle = A^{a, \text{cl}}_\mu(x) \neq 0$ (with $A^{a, \text{cl}}_\mu$ a smooth field configuration).
- **(B-2) Non-worldline support:** the field configuration is extended over the manifold; physical content is not concentrated on any single curve.
- **(B-3) Mean-field content:** physical content is computed from the field configuration's gauge-invariant observables (e.g., $F^a_{\mu\nu} F^{a\mu\nu}$ contracted via the Killing form per Q.2 + Q.3 inheritance).

The two interpretations are *structurally complementary*: a state can have both an excitation content (per (E)) and a background content (per (B)) simultaneously, with the two contributions additive at the field-operator level.

### 2.3 Consequences for downstream content

- **Worldline density:** only excitation content (E) contributes to per-worldline density. Background content (B) is non-worldline-supported and contributes to mean-field configurations rather than to worldline density.
- **Commitment-rate construction:** per Q.3 V4 + W4 below, only excitation content sources commitment events at vertex types T1–T4. Background content affects *vertex factors* (the value of $A^{a, \text{cl}}_\mu$ at a vertex modifies the vertex coupling $-ig/\hbar \cdot \gamma^\mu T^a$ via the minimal-coupling structure $D_\mu = \partial_\mu + (ig/\hbar) A^{a}_\mu T^a$) but does not by itself source new vertex events.
- **Gauge-quotient individuation:** excitation states (E) are individuated as Fock-space content (one-particle, two-particle, etc.) modulo gauge equivalence per Q.3 V3 inheritance. Background field configurations (B) are individuated as gauge-equivalence classes $[A^{a, \text{cl}}_\mu]$ per Q.2 Memo 02's kinematic gauge-quotient.
- **Second-quantised correspondence:** per W2's framework, both interpretations operate within the same operator algebra; the distinction is at the *state* level (which states have non-trivial field expectation), not at the *operator* level.

### 2.4 What is FORCED at the W3 level

- **Excitation-vs-background structural distinction:** FORCED by W2's operator framework + the inherent difference between zero-expectation and non-zero-expectation field-operator states.
- **Worldline support of excitations:** FORCED by W1's null-worldline structure + W2's expectation-value trajectory interpretation.
- **Mean-field interpretation of background:** FORCED by the mathematical content of operator expectation values in coherent states.

### 2.5 What is deferred to Q.8 (R-5 completion)

- **Zero-point fluctuations:** the residual quantum fluctuations of the field operator in the vacuum state $|\Omega\rangle$ — not the excitation-or-background content of W3, but the additional quantum content that distinguishes ED's vacuum from a classical empty configuration. **This is R-5 completion at Q.8.**
- **Vacuum polarisation contributions:** virtual vertex pairs in the vacuum state — Q.8 work.
- **Full vacuum-state structure:** the iε prescription for time-ordered propagators; vacuum expectation values of all operator products beyond two-point functions.
- **Λ derivation refinement:** extension of Theorem 9's V₁ + Synge content with vacuum-vertex contributions — Q.8 work.

---

## 3. Primitive-Level Audit for W3

Each primitive is tested against W3 (excitation-vs-background distinction). Classifications: **supports**, **neutral**, **constrains**, **forbids**.

### 3.1 Primitive 02 — worldline + ambient 3+1D manifold

- **Test.** Does the manifold structure admit both worldline-supported excitations (E) and non-worldline-supported background fields (B)?
- **Analysis.** Standard differential geometry on Lorentzian manifolds admits both: smooth field configurations $A^{a, \text{cl}}_\mu(x)$ defined over the manifold (background); null curves with localised support for excitation content. The two structures coexist on the same manifold without conflict.
- **Tension.** None.
- **Falsifiers triggered.** None.
- **Classification:** **supports**.

### 3.2 Primitive 04 — bandwidth fields

- **Test.** Does the four-band bandwidth structure admit both excitation and background contributions?
- **Analysis.** Excitation content contributes to per-worldline bandwidth flow at vertex events (per Q.3 V4 inheritance). Background field content contributes to *mean-field bandwidth* — the gauge-invariant Killing-contracted content of $A^{a, \text{cl}}_\mu$ supplies mean-field bandwidth values that modify vertex factors but are not themselves vertex events. Primitive 04 admits both contributions naturally.
- **Tension.** Minor: the four-band orthogonality (Primitive 04 §1.5) at the worldline level applies to per-worldline bandwidth content; how this interacts with mean-field bandwidth content (background field) requires the additivity of bandwidth contributions across the excitation/background split. This additivity is structurally clean (the four bands remain orthogonal whether the bandwidth source is excitation or background).
- **Falsifiers triggered.** None.
- **Classification:** **supports**.

### 3.3 Primitive 06 — four-gradient + Lorentz covariance

- **Test.** Does Lorentz covariance admit both interpretations?
- **Analysis.** Both excitation and background content transform covariantly under Lorentz: excitations as Lorentz-covariant Fock-space states; background fields as Lorentz-covariant tensor fields. The decomposition $\hat{A}^a_\mu = A^{a, \text{cl}}_\mu + \hat{a}^a_\mu$ is Lorentz-covariant (each term separately).
- **Tension.** None.
- **Falsifiers triggered.** None.
- **Classification:** **supports**.

### 3.4 Primitive 07 — rule-type taxonomy

- **L1 (bandwidth partition).** Per-rule-type partition unaffected by excitation/background split. **Supports.**
- **L2 (internal index).** Both excitation and background carry the gauge-group internal index $a$. **Supports.**
- **L3 (interface).** L3 specifies how rule-types interact at vertices; excitation content sources vertex events, background content modifies vertex factors. The L3 interface admits both contributions per Q.3 V2 (minimal coupling vertex form) inheritance. **Supports.**
- **L4 (statistics class).** Case P (η = +1) for $\tau_g$ realised by bosonic operator commutation per Theorem 1; the excitation/background split is independent of statistics class. **Supports.**
- **Classification (overall):** **supports**.

### 3.5 Primitive 10 — individuation threshold

- **Test.** Does Primitive 10 admit individuation of excitation states (Fock-space content modulo gauge equivalence) and background field configurations (gauge-equivalence classes $[A^{a, \text{cl}}_\mu]$) separately?
- **Analysis.** Yes — Primitive 10 individuates rule-type instances based on physical content. Excitation states are individuated by Fock-space content (one-particle, two-particle, etc., labeled by null momentum and polarisation); background field configurations are individuated by gauge-equivalence-class field content. Both individuation prescriptions are inherited from Q.2 Memo 02 (kinematic gauge-quotient) and Q.3 Memo 02 (vertex-mediated individuation).
- **Tension.** None.
- **Falsifiers triggered.** None.
- **Classification:** **supports**.

### 3.6 Primitive 11 — commitment dynamics

- **Test.** Does Primitive 11 admit commitment-event sourcing only from excitation content (E), with background content (B) modifying vertex factors but not sourcing new commitment events?
- **Analysis.** Per Q.3 V4 + Q.3 Memo 02 §5, commitment events for $\tau_g$ are sourced at vertex events with vertex-density-dependent rate. Background field content does not by itself constitute vertex events — it modifies the *value* of vertex factors (per the minimal-coupling structure) but does not introduce new vertex events.
  
  This is structurally clean: $\tau_g$'s commitment dynamics is entirely vertex-anchored (per Q.3 V4), and only excitation content propagates through vertex events. Background field content is "always there" — it does not commit, it provides the mean field that vertex events occur within.
- **Tension.** None at W3 level. (Full integration with W4 in §4-§5 below.)
- **Falsifiers triggered.** None at W3 level.
- **Classification:** **supports**.

### 3.7 Primitive 13 — relational timing

- **Test.** Does Primitive 13 admit both interpretations under time evolution?
- **Analysis.** Per Theorem 16 (U3 Schrödinger evolution) inheritance, the time-evolution of $\tau_g$'s state is governed by the Hamiltonian $\hat{H}$. Excitation states evolve via $\exp(-i \hat{H} t / \hbar) | \psi_{\text{exc}} \rangle$; background field configurations evolve via the corresponding evolution of the expectation value $A^{a, \text{cl}}_\mu(x, t) = \exp(-i \hat{H} t / \hbar) A^{a, \text{cl}}_\mu(x, 0)$ (in the Heisenberg picture, equivalently). Both interpretations evolve consistently under time evolution.
- **Tension.** None.
- **Falsifiers triggered.** None.
- **Classification:** **supports**.

### 3.8 W3 primitive-level audit summary

| Primitive | W3 classification | Note |
|---|---|---|
| **P-02** | supports | Manifold admits both excitation (worldline-supported) and background (extended) |
| **P-04** | supports | Bandwidth content additive across excitation/background |
| **P-06** | supports | Lorentz covariance preserved for both |
| **P-07** | supports | L3 admits both vertex-event sourcing (excitation) and vertex-factor modification (background) |
| **P-10** | supports | Individuation prescriptions inherited from Q.2 + Q.3 work for both |
| **P-11** | supports | Commitment events vertex-anchored; background modifies vertex factors but does not source events |
| **P-13** | supports | Time evolution consistent for both via Theorem 16 inheritance |

**No primitive forbids W3. All seven primitives support. WFal-3 (τ_g cannot be treated as excitation vs background) NOT triggered at primitive-level audit.**

---

## 4. Structural Commitments for W4 (Vertex-to-Worldline Lifting, R-3 Q.7-Side)

### 4.1 Integration of Q.3 V4 with W1's affine-parameter framework

W4's substantive content is the integration of Q.3 V4's vertex-anchored commitment with W1's affine-parameter framework, producing the per-worldline accounting that closes R-3's Q.7-side.

#### 4.1.1 Inputs from Q.3 V4

Per Q.3 Memo 02 §4.2 (the full vertex-anchored commitment rule for $\tau_g$):

1. **Source.** Commitment events sourced exclusively at vertex types T1–T4.
2. **Structural form.** Each commitment event has the structural form of the minimal-coupling vertex content (Q.3 V2).
3. **Gauge-equivalence-class counting.** Commitment events individuated by gauge-equivalence-class vertex configuration $[V]$ (Q.3 V3).
4. **Vertex-density-dependent rate.** Per-worldline commitment-event rate proportional to local vertex density.
5. **Primitive 11 admissibility.** Vertex-anchored commitment as structural extension of Primitive 11 (Q.3-side admissibility).

#### 4.1.2 Inputs from W1 (Q.7 Memo 01)

Per Q.7 Memo 01 §2:

- **Affine parameter $\lambda$** along $\tau_g$'s null worldline $\gamma_{\tau_g}$, with affine reparametrisation freedom $\lambda \to a\lambda + b$.
- **Tangent vector** $u^\mu = dx^\mu / d\lambda$ satisfying $u_\mu u^\mu = 0$.
- **Lorentz behaviour** of $\lambda$ via Primitive 06 + Theorem 16 inheritance.

#### 4.1.3 The integration: per-worldline commitment rate in the affine-parameter framework

W4 establishes that the vertex-density commitment rate from Q.3 V4 lifts to a per-worldline commitment rate parametrised by the affine parameter:

$$
\frac{dN_{\text{commit}}}{d\lambda} = \rho_V(\lambda)
$$

where:
- $N_{\text{commit}}(\lambda)$ is the cumulative count of commitment events for $\tau_g$ along its worldline up to affine parameter $\lambda$.
- $\rho_V(\lambda)$ is the local vertex density at affine parameter $\lambda$ — the number of admissible vertex events (V1 types T1–T4) per unit affine parameter that $\tau_g$ participates in at this point along its worldline.

The integral over an affine-parameter interval $[\lambda_1, \lambda_2]$ gives the total commitment-event count along that segment:

$$
N_{\text{commit}}(\lambda_2) - N_{\text{commit}}(\lambda_1) = \int_{\lambda_1}^{\lambda_2} \rho_V(\lambda) \, d\lambda
$$

This is the per-worldline commitment-rate accounting in the affine-parameter framework.

### 4.2 Worldline commitment events: structural form

A *worldline commitment event* for $\tau_g$ at affine parameter $\lambda_v$ has the structural form:

- **Location:** at a vertex point $x^\mu(\lambda_v)$ on $\gamma_{\tau_g}$, with vertex type $T \in \{T1, T2, T3, T4\}$ from Q.3 V1.
- **Vertex content:** minimal-coupling vertex factor (Q.3 V2) for T1/T2, structure-constant content for T3/T4.
- **Operator content:** creation/annihilation operator action per Q.7 Memo 01 W2 — $\hat{a}^{a, \sigma \dagger}_k$ at T1, $\hat{a}^{a, \sigma}_k$ at T2, composite operator products at T3/T4.
- **Gauge-equivalence-class individuation:** vertex configuration $[V_v]$ (gauge-equivalence class) counts as one commitment event per Q.3 V3.
- **Bandwidth content:** four-band Killing-contracted content of the vertex configuration per Q.3 V3 + Memo 02 §3.2.

The worldline commitment event is fully specified by these five components at the W4 level.

### 4.3 Worldline-level conservation

At each vertex event, bandwidth flow and gauge-charge content are conserved:

- **Bandwidth conservation:** total bandwidth (Killing-contracted, gauge-invariant) is conserved across the vertex event — emitted bandwidth at T1 equals the bandwidth gain of the emitted $\tau_g$ excitation; absorbed bandwidth at T2 equals the bandwidth loss of the absorbed $\tau_g$ excitation.
- **Gauge-charge conservation:** charged-rule-type gauge-charge content is conserved at vertex events (with T1/T2 emission/absorption involving the gauge-charge transition between charged and gauge sectors, mediated by the minimal-coupling factor $T^a$).
- **Lorentz/momentum conservation:** four-momentum is conserved at vertex events (incoming = outgoing, with appropriate $\delta^4$ enforcement at vertex).

These conservation laws are inherited from Q.3 V1 + V2 (vertex taxonomy + minimal coupling) and Phase-1/Arc R Lorentz-covariance content. W4's contribution is to verify these conservation laws operate in the affine-parameter per-worldline framework.

### 4.4 Worldline-level gauge-quotient consistency

Per Q.3 V3 (vertex-level gauge-quotient individuation, R-2 completion), gauge-equivalent vertex configurations count as one commitment event. At the worldline level, this lifts to:

- Two worldlines $\gamma_1, \gamma_2$ for $\tau_g$ that are gauge-equivalent (i.e., related by a gauge transformation $U: \mathcal{M} \to G$ that maps $\gamma_1$ to $\gamma_2$ while preserving the null structure) count as **one rule-type instance** under Primitive 10's per-worldline individuation.
- Per-worldline commitment-event counts are gauge-invariant: $N_{\text{commit}}(\lambda) [\gamma_1] = N_{\text{commit}}(\lambda) [\gamma_2]$ for gauge-equivalent worldlines.

This is the worldline-level lift of the kinematic gauge-quotient (Q.2 Memo 02) and vertex-level gauge-quotient (Q.3 V3) — preserving consistency across all three structural levels.

### 4.5 Full Phase-1 reconciliation: from per-proper-time to per-affine-parameter

W4's central contribution: full reconciliation of Primitive 11's general specification (commitment events as primitive-level dynamical content) with the lightlike-worldline + vertex-anchored framework.

For *massive* rule-types (Phase-1 framework):
- Worldline parametrised by proper time $\tau_K$ (timelike).
- Per-worldline commitment rate: $dN_{\text{commit}} / d\tau_K = \rho^{(\text{Phase-1})}_{\text{commit}}(\tau_K)$, where $\rho^{(\text{Phase-1})}_{\text{commit}}$ is the per-proper-time commitment density.
- Primitive 11 admits this as the standard worldline-intrinsic commitment-event accounting.

For *massless* rule-types like $\tau_g$ (Q.7 framework):
- Worldline parametrised by affine parameter $\lambda$ (lightlike).
- Per-worldline commitment rate: $dN_{\text{commit}} / d\lambda = \rho_V(\lambda)$ (vertex-density-dependent per Q.3 V4).
- Primitive 11 admits this as the structural extension to the gauge-rule-type case.

The two are structurally compatible at Primitive 11's general specification level: commitment events are primitive-level dynamical content; the *parametrisation choice* (proper time vs. affine parameter) and the *measure* (per-proper-time density vs. per-affine-parameter vertex density) are structural details that depend on the worldline character (timelike vs. lightlike).

Under affine reparametrisation $\lambda \to a\lambda + b$, the vertex density transforms as $\rho_V(\lambda) \to a \cdot \rho_V(a\lambda + b)$, preserving the cumulative count $\int \rho_V \, d\lambda$ — i.e., the commitment-event count is invariant under affine reparametrisation. This is the structural analog of the proper-time-origin-shift invariance for massive rule-types.

**Phase-1 commitment-dynamics specification is fully reconciled with the lightlike-worldline + vertex-anchored framework.** WFal-7 (P-11 incompatibility with vertex commitment, full reconciliation level) is dispatched.

### 4.6 What is deferred to Q.8 (R-5 completion / vacuum-level)

- **Vacuum-level commitment events:** vacuum polarisation diagrams involve virtual vertex pairs that do not contribute observable commitment events but modify vacuum-state structure. These are Q.8 R-5 completion content.
- **Zero-point contributions to commitment rates:** zero-point fluctuations may contribute to vertex factors via virtual processes; their reconciliation with the per-worldline commitment-rate accounting is Q.8 work.

These do not affect W4's Q.7-side closure of R-3.

---

## 5. Primitive-Level Audit for W4

### 5.1 Primitive 11 — commitment dynamics (load-bearing for W4 + R-3 Q.7-side)

- **Test.** Does Primitive 11 admit the per-worldline commitment-rate accounting in the affine-parameter framework, with full Phase-1 reconciliation per §4.5?
- **Analysis.** Per §4.5, Primitive 11's general specification commits to commitment events as primitive-level dynamical content; the parametrisation choice (proper time vs. affine parameter) is a structural detail dependent on worldline character. The vertex-density commitment rate is the natural specialisation for the lightlike-worldline case.
  
  The full Phase-1 reconciliation: Primitive 11's general specification is invariant under choice of worldline parametrisation (proper time for timelike worldlines; affine parameter for lightlike worldlines); the per-worldline commitment-rate accounting in the affine-parameter framework is structurally consistent with Primitive 11's general content.
- **Tension.** Resolved at §4.5 — the parametrisation choice does not affect the structural content of commitment-event sourcing.
- **Falsifiers triggered.** **WFal-7 (P-11 incompatibility with vertex commitment) NOT triggered at full reconciliation level.** Q.7 Memo 01 §6.4 partially dispatched; this Memo §5 fully dispatches.
- **Classification:** **supports** (full reconciliation at Q.7 Memo 02 level).

### 5.2 Primitive 13 — relational timing

- **Test.** Does Primitive 13 admit the per-worldline accounting in the affine-parameter framework with full Phase-1 reconciliation?
- **Analysis.** Per Q.7 Memo 01 §4.7, Primitive 13 admits affine parameter as a structural generalisation of proper time. The per-worldline commitment-rate accounting in the affine-parameter framework is consistent with Primitive 13's specification — time-axis content is preserved (the affine parameter $\lambda$ is real-valued and increases monotonically along the worldline, structurally analogous to proper time for timelike worldlines).
- **Tension.** None.
- **Falsifiers triggered.** None.
- **Classification:** **supports**.

### 5.3 Other primitives at W4 level

- **Primitive 02:** supports — manifold admits both timelike + lightlike worldlines + vertex events.
- **Primitive 04:** supports — bandwidth conservation at vertex events per §4.3.
- **Primitive 06:** supports — Lorentz covariance of conservation laws + worldline structure.
- **Primitive 07:** supports — L3 interface admits per-worldline accounting; vertex content per Q.3 inheritance.
- **Primitive 10:** supports — worldline-level gauge-quotient individuation per §4.4; lifts kinematic + vertex-level individuation.

### 5.4 W4 primitive-level audit summary

| Primitive | W4 classification | Note |
|---|---|---|
| **P-02** | supports | Manifold admits both worldline types and vertex events |
| **P-04** | supports | Bandwidth conservation at vertex events |
| **P-06** | supports | Lorentz covariance preserved |
| **P-07** | supports | L3 admits per-worldline accounting |
| **P-10** | supports | Worldline-level gauge-quotient lifts kinematic + vertex-level individuation |
| **P-11** | supports (full Phase-1 reconciliation) | Per-worldline commitment-rate accounting in affine-parameter framework structurally consistent with Primitive 11's general specification |
| **P-13** | supports | Affine parameter as structural generalisation of proper time |

**No primitive forbids W4. All seven primitives support, with P-11 (full Phase-1 reconciliation) and P-13 (affine-parameter / proper-time relationship) load-bearing.** **WFal-4 (vertex-to-worldline lifting fails) NOT triggered. WFal-7 (P-11 incompatibility) NOT triggered at full reconciliation level.**

---

## 6. Falsifier Analysis (WFal-3, WFal-4, WFal-7, WFal-8)

### 6.1 WFal-3 — τ_g cannot be consistently treated as excitation vs background

- **Statement.** The excitation/background distinction cannot be cleanly specified at the worldline level; the boundary between propagating excitation and background field is structurally ambiguous, or the two interpretations conflict at some primitive level.
- **Audit (per §2 + §3).** The structural distinction is clean: excitations have zero field-operator expectation and worldline support; background fields have non-zero field-operator expectation and extended (non-worldline) support. The two interpretations are complementary (a state can have both contributions additively) and primitive-level admissible across all seven primitives. The boundary between excitation and background is sharp at the operator-expectation-value level — there is no structural ambiguity.
- **Verdict on WFal-3: NOT triggered.**

### 6.2 WFal-4 — Vertex-to-worldline lifting fails

- **Statement.** The per-worldline accounting cannot integrate Q.3 V4's vertex-density commitment rate with Phase-1's per-worldline commitment-dynamics in the affine-parameter framework — would force restriction of GRH content or revising Phase-1.
- **Audit (per §4 + §5).** The integration is structurally clean: $dN_{\text{commit}} / d\lambda = \rho_V(\lambda)$ specifies the per-worldline commitment rate in the affine-parameter framework; affine reparametrisation invariance preserves cumulative commitment-event counts; conservation laws inherit from Q.3 V1 + V2; gauge-quotient consistency lifts from kinematic + vertex-level closures. Phase-1 reconciliation is fully established at §4.5.
- **Verdict on WFal-4: NOT triggered.**

### 6.3 WFal-7 — Primitive 11 incompatibility (full reconciliation level)

- **Statement.** Primitive 11's general specification cannot be reconciled with the lightlike-worldline + vertex-anchored framework even with affine-parameter machinery — would force revision of Primitive 11.
- **Audit (per §4.5 + §5.1).** Primitive 11's general specification commits to commitment events as primitive-level dynamical content; the parametrisation choice (proper time vs. affine parameter) is a structural detail dependent on worldline character. Per-worldline commitment-rate accounting in the affine-parameter framework is structurally consistent with Primitive 11's general content. Affine reparametrisation invariance is the structural analog of proper-time-origin-shift invariance for massive rule-types.
- **Verdict on WFal-7 (full reconciliation level): NOT triggered.** Q.7 Memo 01 §6.4 partial dispatch; this Memo §5.1 full dispatch.

### 6.4 WFal-8 — UV-FIN conflict

- **Statement.** Theorem 7 (UV-FIN) requires propagators to be finite without renormalisation; the per-worldline + vertex content (Q.3 inheritance + W2 propagator) introduces divergences violating this.
- **Audit.** Per Q.7 Memo 01 §3.1.4, the propagator structural form $\Delta^{ab}_{\mu\nu}(x-y) \propto \delta^{ab} \eta_{\mu\nu} K(x-y)$ inherits Theorem 7's UV-FIN structure via the V₁ kernel finite-width regulator (Theorem 8 inheritance). At the W3 + W4 level, the vertex-content + per-worldline accounting does not introduce additional UV divergences — vertex factors are gauge-invariant local operators, and per-worldline accounting integrates locally (no infinity-producing integrations introduced).
  
  Full propagator details (iε prescription for time-ordered propagators; vacuum-state vertex content) are Q.8 work; Q.7's structural-level UV-finiteness inherits from Theorem 7 + Theorem 8 background and is preserved across W3 + W4.
- **Verdict on WFal-8 (structural level): NOT triggered.** Full audit Q.8.

### 6.5 Cumulative falsifier-status table for W3 + W4

| Falsifier | Status at Q.7 Memo 02 | Where dispatched |
|---|---|---|
| **WFal-1** (W1 primitive incompat.) | not triggered | Q.7 Memo 01 §6.1 |
| **WFal-2** (second-quant. incompat.) | not triggered | Q.7 Memo 01 §6.2 |
| **WFal-3** (excitation-vs-background) | **NOT triggered** | Memo 02 §6.1 |
| **WFal-4** (vertex-to-worldline lifting) | **NOT triggered** | Memo 02 §6.2 |
| **WFal-5** (Q.7 ⟷ Q.8 circular) | deferred to Memo 03 (W5/W6) | — |
| **WFal-6** (Theorem 6 incompat.) | not triggered | Q.7 Memo 01 §6.3 |
| **WFal-7** (P-11 incompat. full reconciliation) | **NOT triggered (full level)** | Memo 02 §6.3 |
| **WFal-8** (UV-FIN conflict, structural) | **NOT triggered (structural level)** | Memo 02 §6.4; full Q.8 |

**No falsifier triggered for W3 or W4 at Q.7 Memo 02.** WFal-5 deferred to Memo 03 (V5/W6 dependency-map audit). WFal-7 and WFal-8 fully dispatched at structural / full-reconciliation level.

---

## 7. Provisional Verdicts for W3 and W4

### 7.1 W3 verdict

**W3 (τ_g excitation vs background at the worldline level): CANDIDATE-FORCED.**

Specifically: the structural distinction between $\tau_g$ as propagating excitation (worldline-supported, zero field expectation) and $\tau_g$ as background field (non-worldline-supported, non-zero field expectation) is clean, primitive-level admissible across all seven primitives, and complementary (states can have both contributions additively). The vacuum-field aspect of $\tau_g$'s status is settled at the W3 level; the zero-point aspect remains R-5 completion at Q.8.

R-5 partial: **CLOSED CANDIDATE-FORCED at Q.7 Memo 02.**

The "FORCED" force is conditional on specific gauge-group + coupling-value choices being empirical inheritance (per the broader GRH closure pattern). The "CANDIDATE" qualifier reflects this conditional-forcing structure.

### 7.2 W4 verdict

**W4 (vertex-to-worldline lifting of commitment events, R-3 Q.7-side): CANDIDATE-FORCED.**

Specifically: the per-worldline commitment-rate accounting in the affine-parameter framework, $dN_{\text{commit}}/d\lambda = \rho_V(\lambda)$, integrates Q.3 V4's vertex-density commitment rate with Phase-1's general commitment-dynamics specification. Worldline-level conservation laws and gauge-quotient consistency lift cleanly from Q.3's vertex-level closures. Full Phase-1 reconciliation: Primitive 11's general specification is invariant under choice of worldline parametrisation; per-worldline commitment-rate accounting in affine-parameter framework is structurally consistent.

R-3 Q.7-side: **CLOSED CANDIDATE-FORCED at Q.7 Memo 02.**

Combined with R-3 Q.3-side closure (Q.3 Memo 02), R-3's substantive structural content is now closed across Q.3 + Q.7. Any vacuum-level vertex content (virtual vertex pairs, vacuum polarisation) is Q.8 work but does not affect R-3's substantive closure.

### 7.3 Justification

The two verdicts rest on:

- **Primitive-level audit (§3 + §5).** No primitive forbids W3 or W4. All seven primitives support both, with P-10 + P-11 (W4) load-bearing.
- **Inheritance from Q.3 + Q.7 Memo 01.** Q.3's vertex content (V1, V2, V3, V4) lifts cleanly to worldline accounting; Q.7 Memo 01's W1 (affine parameter) + W2 (operator framework) supplies the per-worldline parametrisation and operator structure.
- **Falsifier status (§6).** No falsifier triggered. WFal-3, WFal-4, WFal-7 (full level), WFal-8 (structural level) all NOT triggered.
- **Inherited theorem structure.** Theorem 1 (spin-statistics, bosonic content for excitations), Theorem 6 (canonical commutation), Theorem 7 (UV-FIN, finite propagators), Theorem 8 (V₁ kernel finite-width regulator), Theorem 16 (U3 Schrödinger evolution) all support W3 + W4.

### 7.4 Why CANDIDATE-FORCED rather than FORCED unconditionally

W3 + W4 carry forward the same conditional-forcing structure as Q.2, Q.3, Q.7 Memo 01:

- **Specific gauge-group choice empirical.**
- **Coupling constants empirical.**
- **Q.8 closure pending** for R-5 completion (zero-point aspect).
- **GRH itself promotes to FORCED-unconditional only when all five refinements close.**

The CANDIDATE-FORCED verdict is the strongest defensible substage-level closure.

---

## 8. Implications for R-5 Partial and R-3

### 8.1 R-5 partial closure status

**R-5 partial CLOSED at Q.7 Memo 02.**

R-5 has two stages:
- **R-5 partial** (vacuum-field aspect of $\tau_g$ status): ✅ **CLOSED CANDIDATE-FORCED at this Memo (W3).**
- **R-5 completion** (zero-point aspect): outstanding, Q.8 work.

The vacuum-field aspect of $\tau_g$'s status is structurally settled — $\tau_g$ admits both excitation and background-field interpretations, with the boundary between them sharp at the operator-expectation-value level. R-5 completion (zero-point fluctuations, vacuum polarisation, full vacuum-state structure) remains for Q.8.

### 8.2 R-3 closure status

**R-3 substantively CLOSED across Q.3 + Q.7 Memo 02.**

R-3 has two structural sides:
- **R-3 Q.3-side** (vertex-anchored commitment specification): ✅ CLOSED CANDIDATE-FORCED at Q.3 Memo 02.
- **R-3 Q.7-side** (per-worldline accounting in affine-parameter framework): ✅ **CLOSED CANDIDATE-FORCED at this Memo (W4).**

Both sides closed at CANDIDATE-FORCED. R-3's substantive structural content is fully discharged.

Q.8 may add vacuum-level vertex-event content (virtual vertex pairs in vacuum), but R-3 itself does not require Q.8 work — R-3 is about vertex-anchored commitment for $\tau_g$, which is structurally complete at Q.3 + Q.7 levels.

### 8.3 What remains for Q.7 Memo 03 (or Memo 04)

After R-1, R-3 Q.7-side, R-5 partial all closed:

- **W5 (pre-vacuum structure scoping):** identify what Q.7's framework can say about $\tau_g$'s vacuum-related content before Q.8's full vacuum + zero-point work. Largely bookkeeping, with the substantive content already established by W2 + W3.
- **W6 (downstream dependency map for Q.8):** specify what Q.8 inherits from Q.7's closure.
- **Q.7 substage verdict:** CLOSED CANDIDATE-FORCED (anticipated).
- **VFal-5 (Q.7 ⟷ Q.8 circular dependency) full dispatch** at W5/W6 level.

These can likely be handled in a single Memo 03 (verdict + cascade), as W5 and W6 are bookkeeping rather than substantive derivations. Memo 04 may not be needed.

### 8.4 What remains for Q.8 (R-5 completion)

R-5 completion requires:
- **Zero-point fluctuations** as primitive-level vacuum content.
- **Vacuum polarisation** + virtual vertex pairs at the vacuum level.
- **Full vacuum-state structure** (iε prescription for time-ordered propagators; vacuum expectation values of all operator products).
- **Reconciliation with Λ-from-V₁ derivation** (Phase-3 background, Theorems 8 + 9).

### 8.5 Updated GRH refinement-closure map (post-Memo 02)

| Refinement | Pre-Memo-02 status | Post-Memo-02 status | Closure stage |
|---|---|---|---|
| **R-1** | CLOSED (Q.7 Memo 01) | (unchanged) | Q.7 Memo 01 |
| R-2 partial | CLOSED (Q.2 Memo 02) | (unchanged) | Q.2 Memo 02 |
| R-2 completion | CLOSED (Q.3 Memo 02) | (unchanged) | Q.3 Memo 02 |
| **R-2 FULL** | FULLY CLOSED | (unchanged) | Q.2 + Q.3 |
| R-3 Q.3-side | CLOSED (Q.3 Memo 02) | (unchanged) | Q.3 Memo 02 |
| **R-3 Q.7-side** | outstanding | **CLOSED CANDIDATE-FORCED ✅** | **Q.7 Memo 02 (this)** |
| **R-3 SUBSTANTIVE** | partial | **SUBSTANTIVELY CLOSED ✅✅** | Q.3 + Q.7 |
| R-4 | CLOSED (Q.2 Memo 01) | (unchanged) | Q.2 Memo 01 |
| **R-5 partial** | outstanding | **CLOSED CANDIDATE-FORCED ✅** | **Q.7 Memo 02 (this)** |
| R-5 completion | outstanding | (unchanged) | Q.8 |

**Cumulative GRH closure progress: 6/7 refinement items closed (R-1 + R-2 partial + R-2 completion + R-3 Q.3-side + R-3 Q.7-side + R-4 + R-5 partial); 1/7 remaining (R-5 completion → Q.8).** Counting in the original 5-refinement scheme: **R-1 closed, R-2 closed, R-3 substantively closed, R-4 closed, R-5 partially closed (zero-point completion → Q.8)** — only the R-5 zero-point completion remains.

---

## 9. Honest Scope Limits

Memo 02 addresses W3 + W4 only. The following are explicitly out of scope:

### 9.1 Deferred to Q.7 Memo 03 (or Memo 04 if needed)

- **W5 (pre-vacuum structure scoping).**
- **W6 (downstream dependency map for Q.8).**
- **Q.7 substage verdict.**
- **WFal-5 (Q.7 ⟷ Q.8 circular) full dispatch** at W5/W6 level.

### 9.2 Deferred to Q.8

- **R-5 completion (zero-point aspect).** Vacuum-state vertex content, virtual vertex pairs, vacuum polarisation.
- **Full propagator details** (iε prescription, vacuum expectation values of all operator products beyond two-point functions).
- **Λ derivation refinement.**
- **Vacuum-level commitment events** (per §4.6).

### 9.3 Outside the GRH closure trajectory

- **Specific gauge group choice.** Empirical inheritance per Q.2 F4.
- **Coupling constant values.** Empirical via Dimensional Atlas.
- **Charged-rule-type representations.** Empirical / Q.4-onward.
- **Higgs sector / SSB.** Q.4; SPECULATIVE.
- **Generation structure / flavor.** Q.6 / empirical.
- **Charge quantization pattern.** Possibly Q.2 / Q.3 partial sub-memo or empirical.
- **Standard QFT amplitude content.** Built from W2 + W3 + W4 framework but specific computations downstream of GRH closure.

---

## 10. One-Line Summary

> Q.7 Memo 02 closes W3 ($\tau_g$ excitation vs background at the worldline level, R-5 partial) at **CANDIDATE-FORCED** by establishing the structural distinction between propagating excitation states (Fock-space $\hat{a}^{a, \sigma \dagger}_k|\Omega\rangle$ with zero field-operator expectation, worldline-supported, vertex-mediated commitment) and background field configurations (non-zero field-operator expectation $\langle\hat{A}^a_\mu\rangle = A^{a, \text{cl}}_\mu \neq 0$, non-worldline-supported, mean-field content modifying vertex factors but not sourcing new vertex events) as primitive-level admissible complementary interpretations across all seven primitives, plus W4 (vertex-to-worldline lifting, R-3 Q.7-side) at **CANDIDATE-FORCED** by integrating Q.3 V4's vertex-density commitment rate with Q.7 Memo 01's W1 affine-parameter framework into per-worldline accounting $dN_{\text{commit}}/d\lambda = \rho_V(\lambda)$, with worldline-level conservation laws (bandwidth, gauge-charge, Lorentz/momentum) inherited from Q.3 V1 + V2, worldline-level gauge-quotient consistency lifting kinematic + vertex-level closures, and full Phase-1 reconciliation establishing Primitive 11's general specification as invariant under worldline parametrisation choice (proper-time for timelike, affine-parameter for lightlike) — discharging **R-5 partial (vacuum-field aspect)** and **R-3 Q.7-side (substantive R-3 now CLOSED across Q.3 + Q.7)** with no falsifier triggered (WFal-3, WFal-4, WFal-7 full-level, WFal-8 structural-level all NOT triggered) — advancing cumulative GRH closure to **6/7 refinements closed** (R-1 + R-2 partial + R-2 completion + R-3 Q.3-side + R-3 Q.7-side + R-4 + R-5 partial), with only **R-5 completion (zero-point aspect, Q.8)** remaining for full GRH closure, GRH-3 advancing to CANDIDATE-FORCED at second-quantised + vertex + worldline + vacuum-field-aspect levels, GRH itself awaiting Q.8 + Arc Q synthesis before promotion to FORCED-unconditional and addition as Theorem 17 to the structural-foundations inventory with cascade promotion of Arc M's F-M8.

---

## Recommended Next Steps

**(a) Begin Q.7 Memo 03 (W5 + W6; verdict + cascade).** The natural next deliverable. Given that W3 + W4 are closed and the remaining work (W5 pre-vacuum scoping, W6 dependency map) is bookkeeping rather than substantive derivation, **Memo 03 may close the entire Q.7 substage without need for Memo 04**. Memo 03 should: (i) close W5 (pre-vacuum structure: what Q.7 can say before Q.8); (ii) close W6 (downstream dependency map for Q.8); (iii) dispatch WFal-5 (Q.7 ⟷ Q.8 circular dependency); (iv) integrate W1–W4 closures into the Q.7 substage verdict; (v) issue the Q.7 verdict (anticipated CLOSED CANDIDATE-FORCED) + cascade map to Q.8.

**(b) Pre-Memo-03 verification of background-field aspect / V₁ vacuum kernel relationship.** A short audit (15–30 minutes) verifying that W3's background-field interpretation (as the operator expectation value $\langle\hat{A}^a_\mu\rangle$) is consistent with Theorem 8's V₁ kernel finite-width structure (which governs vacuum two-point correlations in the absence of background field). The two structural concepts must coexist cleanly — the V₁ kernel is the vacuum content; the background field is the non-vacuum mean-field content.

**(c) Defer memory-record update until Q.7 closure (Memo 03).** Per the discipline established. The bundled memory update will capture all of: R-1 + R-3 Q.7-side + R-5 partial closures; Q.7 substage verdict (CLOSED CANDIDATE-FORCED); cumulative refinement-closure status (6/7 closed; only R-5 completion remaining); GRH-3 status update; anticipated remaining trajectory (Q.8 → synthesis → cascade); sensitivity flags.

**(d) (Optional) Sketch Q.8 Memo 00 outline now.** With Q.7 substantive work nearly complete (Memos 01–02 closed; only Memo 03 integration remaining), the Q.8 Memo 00 outline can be drafted in skeleton form: R-5 completion (zero-point aspect); sub-features (vacuum state, zero-point fluctuations, vacuum polarisation, Λ refinement); falsifier inventory; dependency map for Arc Q synthesis. Q.8 is anticipated to be substantively lighter than Q.7 (no full second-quantisation framework requirement; primarily R-5 completion). Pre-sketching would let Q.8 land into a known scope when Q.7 closes; useful for trajectory planning.

**(e) (Optional) Update the Sixteen-Theorems desktop graphic if appropriate.** With 6 of 7 refinements closed (or, in 5-refinement counting, 4.5 of 5 closed — only R-5 zero-point remaining), Theorem 5's GRH entry could be updated to reflect the substantial closure progress. User preference whether to update incrementally or wait for full GRH closure (anticipated Q.8 + Arc Q synthesis, ~3–5 memos out).
