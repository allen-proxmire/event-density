# Q.7 Memo 01 — W1 + W2: Lightlike-Worldline Structure + Second-Quantised Field/Worldline Correspondence (R-1 Closure)

**Stage:** Arc Q · Q.7 · Memo 01 (load-bearing W1 + W2 derivation; R-1 closure)
**Date:** 2026-04-26
**Location:** `arcs/arc-Q/`
**Goal:** Derive W1 (lightlike-worldline structure under GRH) and W2 (second-quantised field / worldline correspondence) at CANDIDATE-FORCED. Close R-1 (lightlike-worldline reformulation) at the Q.7 level. Prepare the ground for Memos 02–04 (W3 background-field aspect with R-5 partial; W4 vertex-to-worldline lifting with R-3 Q.7-side; W5 pre-vacuum structure; W6 dependency map).
**Predecessors:** Q.1 / Q.2 / Q.3 trajectory · [`09_Q7_memo_00_outline.md`](09_Q7_memo_00_outline.md) (Q.7 Memo 00 — six-sub-feature decomposition; W2/W3/W4 designated load-bearing)
**Status:** Technical derivation memo. Operates under strict forbidden-input discipline (per Q.7 Memo 00 §5): no R-5 completion (Q.8 work), no full vacuum-state content, no SM specifics, no Higgs / generations / coupling constants, no F-M8 cascade target, no Yang-Mills / BRST / path-integral measure as derivation premise. Inherits Q.2 + Q.3's CLOSED CANDIDATE-FORCED commitments + Theorems 1–16 (with Theorems 6, 7, 8, 9 directly relevant).
**Purpose:** State and discharge W1 + W2 with the strongest defensible verdict so the Q.7 substage advances to W3 (background-field aspect, R-5 partial) and W4 (vertex-to-worldline lifting, R-3 Q.7-side) in Memo 02.

---

## 1. The W1 and W2 Questions Restated

### 1.1 W1 question

**What does it mean for GRH to force lightlike worldlines for $\tau_g$, and what affine-parameter machinery replaces proper-time parametrisation in this case?**

Background: GRH-4 specifies $\sigma_{\tau_g} = 0$ (the gauge rule-type is structurally massless via the MR-P mechanism of M.1.2). Standard relativistic kinematics says that massless particles propagate on null curves (lightlike worldlines, with tangent vector $u^\mu$ satisfying $u_\mu u^\mu = 0$). The proper-time parameter $\tau$ for null curves satisfies $d\tau = 0$, breaking the proper-time parametrisation that Phase-1's per-worldline accounting assumed.

W1's substantive content: derive the null-propagation condition from GRH + ED primitives, establish the affine-parameter machinery that replaces proper-time parametrisation, and verify this machinery is primitive-level admissible without invoking content beyond Q.7's allowed inputs.

### 1.2 W2 question

**What is the structural worldline / field correspondence for $\tau_g$ in the second-quantised regime, and how does the framework lift from single-vertex content (Q.3) to a full quantum-field framework?**

W2's substantive content: construct the minimal second-quantised operator structure for $\tau_g$ — field operators $A^a_\mu(x)$, mode expansion in null momentum modes, creation/annihilation operators, propagator content — consistent with Theorem 6 (canonical (anti-)commutation), Theorem 7 (UV-FIN), and Q.3's vertex content (V1 taxonomy, V2 minimal coupling, V3 vertex-level gauge-quotient). Show that worldlines arise naturally from this structure: as expectation-value trajectories, as support curves of $\tau_g$ excitations, and as null curves under GRH.

W2 must use only primitive-level + inherited-theorem machinery; no Yang-Mills Lagrangian, no path-integral measure, no BRST gauge-fixing imported as derivation premise.

### 1.3 How W1 and W2 jointly close R-1

R-1 (lightlike-worldline reformulation) requires both:
- **W1:** the affine-parameter machinery for $\tau_g$'s null worldline (replacing the proper-time framework that breaks for $d\tau = 0$).
- **W2:** the second-quantised framework that the affine-parameter machinery operates within (creation/annihilation operators, propagator content, field/particle correspondence).

Without W1, W2 has no parametrisation for per-worldline content. Without W2, W1's affine-parameter machinery is purely geometric without dynamical content. Together they close R-1: W1 supplies the parametrisation, W2 supplies the operator framework, and the joint structure realises Phase-1 commitment dynamics in the lightlike case.

The W4 (vertex-to-worldline lifting; Memo 02) will integrate Q.3's vertex-anchored commitment with this joint W1 + W2 structure to fully discharge R-3's Q.7-side. R-5 partial (vacuum-field aspect; W3 in Memo 02) builds on W2's framework.

### 1.4 Outcome criteria

- **CANDIDATE-FORCED:** W1 + W2 close affirmatively with primitive-level admissibility, no falsifier triggered, conditional-forcing aligned with the empirical inheritance of specific gauge-group / coupling values. Anticipated default.
- **CANDIDATE-admissible:** structural admissibility but uniqueness gaps (e.g., multiple admissible affine-parameter conventions, multiple admissible mode-expansion structures with no primitive-level discriminator).
- **REFUTED:** primitive-level obstruction blocks W1 or W2 — would force restriction of GRH to massive gauge rule-types (conflicting with GRH-4) or restructuring of Theorem 6 / Theorem 7.

---

## 2. Structural Commitments for W1 (Lightlike-Worldline Structure)

### 2.1 Derivation of the null-propagation condition

The null-propagation condition for $\tau_g$ — that $\tau_g$'s worldline tangent vector $u^\mu$ satisfies $u_\mu u^\mu = 0$ — derives from a chain of inputs:

#### 2.1.1 (Step 1) GRH-4: $\sigma_{\tau_g} = 0$

GRH-4 (per Q.1 evaluation memo §2.4) specifies $\tau_g$'s structural mass parameter $\sigma_{\tau_g}$ vanishes via the MR-P mechanism of M.1.2. This is the foundational masslessness commitment.

#### 2.1.2 (Step 2) Massless ⟹ null propagation in 3+1D Minkowski

For any massive rule-type with $\sigma > 0$, the on-shell condition (Phase-1 + Arc R inheritance) is $p_\mu p^\mu = m^2 c^2$ (timelike four-momentum). For $\sigma = 0$, the on-shell condition reduces to $p_\mu p^\mu = 0$ (null four-momentum).

Standard relativistic kinematics (Primitive 02 + Primitive 06): a particle with null four-momentum propagates on a null worldline. The tangent vector along the worldline is proportional to the four-momentum (up to affine reparametrisation), so $u^\mu \propto p^\mu$ and therefore $u_\mu u^\mu = 0$.

#### 2.1.3 (Step 3) Null tangent ⟹ proper-time degeneracy

For a null tangent vector $u^\mu$, the proper-time line element $d\tau^2 = -u_\mu u^\mu \, ds^2$ vanishes: $d\tau = 0$. Phase-1's per-worldline accounting (Primitive 11 specification + Primitive 13 relational timing) assumed timelike worldlines parametrised by proper time $\tau_K$; this parametrisation is structurally degenerate for $\tau_g$.

#### 2.1.4 (Step 4) Affine parameter replaces proper time

For null curves, the natural parametrisation is by an *affine parameter* $\lambda$ — a parameter such that the geodesic equation takes its simplest form ($d^2 x^\mu / d\lambda^2 = 0$ in flat spacetime; $\nabla_u u^\mu = 0$ on a curved background per Phase-3 acoustic-metric inheritance via Theorem 9). The affine parameter has the freedom of affine reparametrisation $\lambda \to a\lambda + b$ for $a, b$ real constants — a two-parameter ambiguity that is a structural symmetry of the null curve specification.

The tangent vector $u^\mu = dx^\mu / d\lambda$ is then well-defined and null. Per-worldline content (commitment rates, field amplitudes, vertex-density measurements) parametrises by $\lambda$ rather than by $\tau$.

### 2.2 What W1 commits to

- **Null propagation:** $\tau_g$'s worldline tangent $u^\mu$ satisfies $u_\mu u^\mu = 0$.
- **Affine parameter:** $\tau_g$'s worldline carries a parameter $\lambda$ with affine reparametrisation freedom $\lambda \to a\lambda + b$.
- **Tangent structure:** $u^\mu = dx^\mu / d\lambda$ is a well-defined null vector along $\gamma_{\tau_g}$.
- **Lorentz behaviour:** under Lorentz boosts, the affine parameter $\lambda$ transforms by a frame-dependent rescaling (the boosted parameter $\lambda'$ is related to $\lambda$ by the boost factor of $u^\mu$; physical observables along the worldline are constructed to be invariant under this rescaling).

### 2.3 What is FORCED at the W1 level

- **Null propagation:** FORCED by GRH-4 + Step 2 (massless ⟹ null in 3+1D).
- **Affine parameter machinery:** FORCED by Step 4 (proper-time degenerate ⟹ affine parameter required).
- **Affine reparametrisation freedom:** FORCED by the structural ambiguity of null-curve parametrisation.
- **Lorentz behaviour of affine parameter:** FORCED by Primitive 06 covariance.

### 2.4 What remains empirical (none at W1 level)

W1's structural content is fully derived from GRH + ED primitives + standard differential geometry of null curves. No empirical inheritance enters at the W1 level (the affine parameter is a structural object, not a value to be measured).

(Specific worldline trajectories of physical $\tau_g$ quanta — e.g., the actual paths photons take through real material configurations — depend on the empirical content of the configurations, but the *parametrisation framework* is FORCED.)

### 2.5 What is deferred

- **Vacuum effects on the worldline parametrisation:** zero-point fluctuations may modify the affine-parameter machinery in subtle ways (Q.8 R-5 completion content).
- **Renormalisation of the worldline content:** if needed at the second-quantisation level (W2 + Q.8 work).
- **Specific tangent vectors for physical $\tau_g$ quanta:** depend on initial conditions and empirical context.

---

## 3. Structural Commitments for W2 (Second-Quantised Worldline/Field Correspondence)

### 3.1 Minimal second-quantised structure compatible with Q.2 + Q.3

W2 constructs the minimal operator framework for $\tau_g$ at the second-quantisation level, using only primitive-level inputs + inherited theorems.

#### 3.1.1 Field operator

The gauge field $A^a_\mu(x)$ becomes an operator on the participation-measure Hilbert space: $\hat{A}^a_\mu(x)$, with $a$ the gauge-group internal index, $\mu$ the Lorentz spacetime index, and $x \in \mathcal{M}$ the spacetime point.

The operator inherits:
- **Lorentz covariance** from Primitive 06 (transforms as a four-vector under $\mathrm{SO}^+(3,1)$).
- **Adjoint-rep gauge action** from Q.2 Memo 01 (transforms as $\hat{A}^a_\mu \to U^{ab} \hat{A}^b_\mu + \ldots$ under gauge transformations).
- **L3-interface gauge-invariance constraint** from Q.2 Memo 02 (operator content depends on gauge-equivalence class $[\hat{A}_\mu]$ at the kinematic level).

#### 3.1.2 Mode expansion in null momentum modes

Per W1's null-propagation condition, the field decomposes into modes labelled by null four-momentum $k^\mu$ ($k_\mu k^\mu = 0$):

$$
\hat{A}^a_\mu(x) = \int \frac{d^3 k}{(2\pi)^3 \, 2 |k^0|} \sum_{\sigma} \left[ \hat{a}^{a, \sigma}_k \, \varepsilon^\sigma_\mu(k) \, e^{-ikx/\hbar} + \hat{a}^{a, \sigma \dagger}_k \, \varepsilon^{\sigma *}_\mu(k) \, e^{+ikx/\hbar} \right]
$$

where $\sigma$ labels the polarisation states (two physical polarisations for a massless gauge boson; the longitudinal and timelike polarisations are gauge-equivalent to zero per the gauge-quotient structure of Q.2 + Q.3), $\varepsilon^\sigma_\mu(k)$ are the polarisation vectors, and the integration measure $d^3 k / (2\pi)^3 \cdot 1/(2|k^0|)$ is the standard Lorentz-invariant measure on the null mass-shell.

The mode-expansion structure uses standard differential-geometric and Lie-algebraic content; no Yang-Mills Lagrangian, no specific gauge-fixing prescription is invoked.

#### 3.1.3 Creation and annihilation operators

The operators $\hat{a}^{a, \sigma}_k$ (annihilation) and $\hat{a}^{a, \sigma \dagger}_k$ (creation) satisfy bosonic canonical commutation per Theorem 6 (Arc Q, Q.7 background — note: Theorem 6 is *inherited* here as background, with Q.7's role being to *verify* its second-quantised structure for $\tau_g$ specifically):

$$
[\hat{a}^{a, \sigma}_k, \hat{a}^{b, \sigma' \dagger}_{k'}] = (2\pi)^3 \, 2 |k^0| \, \delta^{ab} \, \delta^{\sigma \sigma'} \, \delta^3(k - k'), \qquad [\hat{a}^{a, \sigma}_k, \hat{a}^{b, \sigma'}_{k'}] = 0
$$

The bosonic ($+$ commutator, not $-$ anticommutator) character is forced by GRH-1 (Case P, $\eta = +1$, integer spin) per Theorem 1 (spin-statistics).

#### 3.1.4 Propagator content

The two-point function $\Delta^{ab}_{\mu\nu}(x - y) = \langle 0 | \hat{A}^a_\mu(x) \hat{A}^b_\nu(y) | 0 \rangle$ is the propagator for $\tau_g$. Per Theorem 7 (UV-FIN, Arc Q inheritance), the propagator is finite without renormalisation — the participation-graph's bandwidth structure provides the natural cutoff (per the explainer 16 visualisation).

The propagator's structural form for $\tau_g$ is:
$$
\Delta^{ab}_{\mu\nu}(x-y) \propto \delta^{ab} \, \eta_{\mu\nu} \, K(x-y)
$$
where $K(x-y)$ is the scalar Green's function for the massless wave equation on the participation graph (with the V₁ kernel content of Theorem 8 supplying the finite-width regulator structure inherited as background).

The full propagator structure depends on Q.8's vacuum-state work (specifically, the iε prescription for time-ordered propagators is vacuum-dependent), but the structural *form* (gauge-invariant content, $\delta^{ab}$ adjoint structure, $\eta_{\mu\nu}$ Lorentz structure, finite-width regulator from Theorem 8) is W2-level content.

### 3.2 Worldlines as expectation-value trajectories

A one-particle state for $\tau_g$ — created by a single application of $\hat{a}^{a, \sigma \dagger}_k$ to the (Q.8-deferred) vacuum — has expectation values $\langle \hat{x}^\mu(t) \rangle$ that trace out a null curve in spacetime. For a sharply-peaked momentum-state (limit of Gaussian wavepackets in null momentum), the expectation-value trajectory $\langle \hat{x}^\mu(t) \rangle$ is the classical null worldline parametrised by the affine parameter $\lambda$ from W1.

This is the **expectation-value trajectory interpretation** of $\tau_g$'s worldline: the worldline is the support curve of the one-particle state's spatial probability distribution as time progresses. The wavepacket spread does not modify the leading-order (sharply-peaked) trajectory; quantum corrections to the trajectory are subleading.

### 3.3 Worldlines as support curves of τ_g excitations

Equivalently, $\tau_g$'s worldline is the support curve of $\tau_g$ excitation content. In the absence of vertex events (no interaction with charged rule-types or self-coupling vertices), $\tau_g$ excitations propagate freely along their null worldlines — the support of the one-particle state is concentrated on these curves.

When vertex events occur, excitations are created (T1 emission) or destroyed (T2 absorption) at the vertex location, and the support curve is "broken" at the vertex point. This is the per-worldline picture: $\tau_g$ propagates between vertices on null worldlines, with vertex events being the points where worldlines start, end, or interact.

### 3.4 Worldlines as null curves under GRH

By W1, the worldline tangent is null: $u^\mu = dx^\mu / d\lambda$ satisfies $u_\mu u^\mu = 0$. The worldline is a null curve in the spacetime manifold per Primitive 02. Under the affine parameter $\lambda$, the worldline equation in flat spacetime is $d^2 x^\mu / d\lambda^2 = 0$ (free propagation along the null direction).

The three interpretations (expectation-value, support-curve, null-curve) are structurally equivalent at the W2 level: they describe the same per-worldline structure from different operational perspectives.

### 3.5 Minimal operator algebra (no QFT machinery imported)

The operator algebra for W2 consists of:
1. Field operator $\hat{A}^a_\mu(x)$ with Lorentz / gauge transformation properties as inherited.
2. Creation / annihilation operators $\hat{a}^{a, \sigma}_k$, $\hat{a}^{a, \sigma \dagger}_k$ satisfying canonical commutation per Theorem 6.
3. Mode expansion connecting the two via standard differential-geometric integration.
4. Propagator $\Delta^{ab}_{\mu\nu}(x-y)$ as a two-point function on the (Q.8-deferred) vacuum.

This is the minimal operator algebra needed for W2; no Yang-Mills Lagrangian is invoked, no path-integral measure is constructed, no BRST gauge-fixing machinery is imported. The algebra is built from primitive-level + inherited-theorem inputs alone.

---

## 4. Primitive-Level Audit for W1 and W2

Each primitive is tested against W1 + W2. Classifications: **supports**, **neutral**, **constrains**, **forbids**.

### 4.1 Primitive 02 — worldline + ambient 3+1D manifold

- **W1 test.** Does the spacetime manifold admit null curves with affine parametrisation?
- **Analysis.** Standard differential geometry on Lorentzian manifolds. Null curves are well-defined; affine parametrisation is the natural parametrisation for null geodesics. Primitive 02's 3+1D Minkowski background trivially admits null curves.
- **W2 test.** Does the manifold admit field operators $\hat{A}^a_\mu(x)$ defined on it?
- **Analysis.** Yes — operator-valued distributions on smooth manifolds are standard.
- **Tension.** None at W1 / W2 level.
- **Falsifiers triggered.** None.
- **Classification:** **supports**.

### 4.2 Primitive 04 — bandwidth fields

- **W1 test.** Does the bandwidth structure admit per-worldline content along null curves?
- **Analysis.** Bandwidth content along worldlines (charged rule-types or $\tau_g$) is rule-type-data; per-worldline accounting in the affine-parameter framework adapts naturally. No Primitive 04 obstruction.
- **W2 test.** Does the four-band bandwidth content admit field-operator structure?
- **Analysis.** Field-operator amplitudes squared ($|\hat{A}^a_\mu|^2$ at vertex events) correspond to bandwidth content (per Q.3 V3 inheritance — Killing-contracted gauge-invariant observables). Compatible.
- **Tension.** None.
- **Falsifiers triggered.** None.
- **Classification:** **supports**.

### 4.3 Primitive 06 — four-gradient + Lorentz covariance

- **W1 test.** Does Lorentz covariance admit affine-parameter machinery for null curves?
- **Analysis.** Yes — Lorentz transformations act on null curves by mapping null to null (the null condition $u_\mu u^\mu = 0$ is Lorentz-invariant). The affine parameter rescales under boosts in a structurally consistent way; affine reparametrisation freedom is preserved.
- **W2 test.** Does Lorentz covariance admit field-operator $\hat{A}^a_\mu(x)$ with mode expansion in null momentum modes?
- **Analysis.** Yes — field operators transform as four-vectors under Lorentz; the mode expansion uses Lorentz-invariant measures on the null mass-shell. Standard QFT machinery is Lorentz-covariant; ED's analog inherits this property.
- **Tension.** None.
- **Falsifiers triggered.** None.
- **Classification:** **supports**.

### 4.4 Primitive 07 — rule-type taxonomy

- **L1 (bandwidth partition).** Per-worldline bandwidth content adjusts via vertex events; structural content unchanged. **Supports.**
- **L2 (internal index).** Field operator $\hat{A}^a_\mu$ carries internal index $a$; mode expansion preserves the index structure (creation/annihilation operators carry $a$). **Supports.**
- **L3 (interface).** L3 specifies how rule-types interact at vertices; the operator framework realises the L3 interface at the second-quantisation level. Q.3's L3-Q-V1, L3-Q-V2, L3-Q-V3 conditions lift to W2's operator structure. **Supports.**
- **L4 (statistics class).** Case P (η = +1) for $\tau_g$ realised at W2 by bosonic commutation $[\hat{a}, \hat{a}^\dagger]$ (not anticommutation), per Theorem 1 inheritance. **Supports.**
- **Classification (overall):** **supports**.

### 4.5 Primitive 10 — individuation threshold

- **W1 test.** Does Primitive 10 admit per-worldline individuation in the lightlike case?
- **Analysis.** Per-worldline individuation of $\tau_g$ rule-type instances inherits from Q.3 V3 (vertex-mediated individuation). At the worldline level, individuation is via gauge-equivalence-class one-particle states $|k\rangle = \hat{a}^{a, \sigma \dagger}_k |0\rangle$ — gauge-equivalent states count as one rule-type instance.
- **W2 test.** Does Primitive 10 admit Fock-space-like individuation for second-quantised $\tau_g$?
- **Analysis.** Multi-particle states $|k_1, k_2, \ldots\rangle$ are individuated by their gauge-invariant content; bosonic symmetry under particle exchange (per Theorem 1 inheritance) is consistent with Primitive 10's individuation threshold for Case P rule-types.
- **Tension.** None.
- **Falsifiers triggered.** None.
- **Classification:** **supports**.

### 4.6 Primitive 11 — commitment dynamics

- **W1 test.** Does Primitive 11 admit per-worldline commitment-rate accounting in the affine-parameter framework?
- **Analysis.** Q.3 Memo 02 §3.6 + §5 established that Primitive 11's general specification commits to commitment events as primitive-level dynamical content, not specifically to per-proper-time accounting. The affine-parameter framework supplies the parametrisation; per-worldline commitment-rate accounting (W4, Memo 02) integrates with it. **At W1 level: admissible**; full integration is W4 work.
- **W2 test.** Does Primitive 11 admit second-quantised commitment events (per-vertex commitment-event sourcing per Q.3 V4)?
- **Analysis.** Yes — Q.3 V4 established vertex-anchored commitment for $\tau_g$. W2's second-quantised framework realises this: each vertex event corresponds to a creation or annihilation operator action on the Hilbert space.
- **Tension.** Full Phase-1 reconciliation (per-worldline accounting of commitment events with proper-time → affine-parameter measure change) is W4 work. At W1 + W2 level, the structural admissibility is established; the accounting integration is Memo 02.
- **Falsifiers triggered.** WFal-7 (P-11 incompat. lifting) anticipated NOT triggered at full W4 closure (Memo 02). At W1 + W2 level, no Primitive 11 obstruction identified.
- **Classification:** **supports** (at W1 + W2 level; full reconciliation W4 / Memo 02).

### 4.7 Primitive 13 — relational timing

- **W1 test.** Does Primitive 13 admit affine parameter as a generalisation of proper time for null curves?
- **Analysis.** Primitive 13 specifies the time axis at the structural level (per U3 derivation, the continuous-time interpretation is canonical). For massive rule-types, proper time $\tau_K$ is the natural per-worldline parametrisation. For massless rule-types, the proper-time degeneracy ($d\tau = 0$) requires an alternative — the affine parameter $\lambda$ is the natural choice.
  
  Primitive 13 admits affine parametrisation as a structural generalisation: the affine parameter is a real-valued parameter along the worldline, with the same general role as proper time but with the affine reparametrisation freedom $\lambda \to a\lambda + b$ instead of the proper-time origin shift $\tau \to \tau + c$.
- **W2 test.** Does Primitive 13 admit second-quantised time-evolution for $\tau_g$?
- **Analysis.** Yes — Theorem 16 (U3, Schrödinger evolution) supplies the time-evolution framework; W2's operator structure fits within it. Time evolution of field operators $\hat{A}^a_\mu(x, t)$ is governed by the Hamiltonian inherited from U4 + GRH content.
- **Tension.** None.
- **Falsifiers triggered.** None.
- **Classification:** **supports**.

### 4.8 Primitive-level audit summary

| Primitive | W1 (lightlike worldline) | W2 (second-quantised correspondence) | Note |
|---|---|---|---|
| **P-02** | supports | supports | Manifold admits null curves + field operators |
| **P-04** | supports | supports | Bandwidth content compatible with operator amplitudes |
| **P-06** | supports | supports | Lorentz covariance of null curves + field operators |
| **P-07** | supports | supports | L3 lever load-bearing; admits operator framework |
| **P-10** | supports | supports | Per-worldline + Fock-space individuation admissible |
| **P-11** | supports | supports (W4 reconciliation deferred) | Vertex-anchored commitment per Q.3 V4 lifts cleanly |
| **P-13** | supports | supports | Affine parameter as structural generalisation of proper time |

**No primitive forbids W1 or W2.** All seven primitives actively support. **No falsifier (WFal-1, WFal-2) triggered at the primitive-level audit.**

---

## 5. Integration of W1 and W2 into R-1 Closure

### 5.1 Joint W1 + W2 closure

R-1 closes affirmatively when:
- W1 establishes the affine-parameter machinery for $\tau_g$'s null worldline (✅ §2 above).
- W2 establishes the second-quantised operator framework that the affine-parameter machinery operates within (✅ §3 above).
- The two integrate cleanly without structural conflict (verified in §4 primitive-level audit + §5.2 below).

### 5.2 Minimal structural form of worldline commitment events

Combining W1's affine-parameter machinery and W2's operator framework, a worldline commitment event for $\tau_g$ takes the form:

- **Location:** at an interaction vertex (V1 type T1, T2, T3, or T4 from Q.3) along $\tau_g$'s null worldline at affine parameter $\lambda_{\text{vertex}}$.
- **Operator content:** creation/annihilation operator action on the Fock space — $\hat{a}^{a, \sigma \dagger}_k$ for emission (T1, $\tau_g$ created), $\hat{a}^{a, \sigma}_k$ for absorption (T2, $\tau_g$ destroyed), composite operator products for self-coupling vertices (T3, T4).
- **Vertex factor:** minimal-coupling vertex content per Q.3 V2 ($-ig/\hbar \cdot \gamma^\mu T^a$ for T1/T2; structure-constant content $f^{abc}$ for T3, $f^{abe} f^{cde}$ for T4).
- **Gauge-invariance:** vertex content is gauge-invariant per Q.3 V3 (vertex-level Q3-A automatic).
- **Per-worldline rate:** $dN_{\text{commit}} / d\lambda = \rho_V(\lambda)$, where $\rho_V$ is the local vertex density along $\tau_g$'s worldline at affine parameter $\lambda$ (per Q.3 V4 vertex-density-dependent commitment rate; full integration with Phase-1 commitment dynamics is W4 work).

The structural form is **complete at the W1 + W2 level**; the W4 integration (Memo 02) verifies the per-worldline accounting is fully consistent with Primitive 11's general specification.

### 5.3 What remains for W3 and W4

After R-1 closure (this Memo):

- **W3 (background-field aspect, R-5 partial; Memo 02):** distinguish $\tau_g$ as background field $\langle \hat{A}^a_\mu \rangle$ from $\tau_g$ as particle excitations on top of the background. W2 supplies the operator framework; W3 specifies the background-vs-excitation structural commitment.
- **W4 (vertex-to-worldline lifting, R-3 Q.7-side; Memo 02):** integrate Q.3 V4's vertex-density commitment rate with Phase-1's per-worldline commitment-dynamics in the affine-parameter framework. W1 supplies the affine parameter; W4 specifies the integration with Primitive 11.

W3 and W4 build on W1 + W2's closure; they do not require revisiting R-1.

---

## 6. Falsifier Analysis (WFal-1, WFal-2, WFal-6, WFal-7)

### 6.1 WFal-1 — Lightlike-worldline reformulation primitive incompatibility

- **Statement.** No affine-parameter machinery is structurally admissible for $\tau_g$'s lightlike worldline; some primitive (P-02, P-06, P-13) forbids the affine-parameter parametrisation.
- **Audit (per §2 + §4).** All three relevant primitives (P-02 manifold structure, P-06 Lorentz covariance, P-13 relational timing) actively support affine-parameter machinery as structural generalisation of proper-time parametrisation for null curves. Standard differential geometry on Lorentzian manifolds admits null curves with affine parameters; no primitive obstruction.
- **Verdict on WFal-1: NOT triggered.**

### 6.2 WFal-2 — Second-quantised framework incompatibility with ED primitives

- **Statement.** ED's primitive-level structure (Primitive 04 bandwidth, Primitive 07 L3 interface, Primitive 11 commitment dynamics) cannot accommodate the creation/annihilation operator structure that Theorem 6 supplies.
- **Audit (per §3 + §4).** All seven primitives (P-02 through P-13) support the second-quantised framework. Field operator $\hat{A}^a_\mu(x)$ structurally compatible with Primitive 04's bandwidth content (operator amplitudes squared = gauge-invariant bandwidth via Q.3 V3). Creation/annihilation operators consistent with Theorem 6 (canonical commutation) and Theorem 1 (spin-statistics). Mode expansion uses standard Lorentz-invariant measures on null mass-shell.
- **Verdict on WFal-2: NOT triggered.**

### 6.3 WFal-6 — Theorem 6 inconsistency with worldline structure

- **Statement.** Canonical (anti-)commutation relations (Theorem 6) cannot be specified consistently with $\tau_g$'s lightlike-worldline structure — would force restructuring of either Theorem 6 or W1.
- **Audit.** Theorem 6 specifies canonical commutation $[\hat{a}, \hat{a}^\dagger] = \delta$ (bosonic, for Case P rule-types) and anticommutation $\{\hat{\psi}, \hat{\psi}^\dagger\} = \delta$ (fermionic, for Case R rule-types). For $\tau_g$ (Case P per GRH-1), the bosonic commutation relations apply.
  
  The lightlike-worldline structure does not modify the algebraic content of canonical commutation: the operators are defined on momentum modes (parametrised by null four-momentum $k^\mu$), and the commutation relations are at the *operator-algebraic* level, not at the worldline-parametrisation level. The affine-parameter machinery of W1 operates on the spacetime trajectory of one-particle states; the canonical commutation operates on the Fock-space operator structure. The two structures are independent and mutually consistent.
- **Verdict on WFal-6: NOT triggered.** Theorem 6 inherits cleanly to the lightlike-worldline + second-quantised framework.

### 6.4 WFal-7 — Primitive 11 incompatibility with per-worldline commitment lifting

- **Statement.** Primitive 11's general specification (worldline-intrinsic commitment events as primitive-level dynamical content) cannot be reconciled with the lightlike-worldline + vertex-anchored framework even with affine-parameter machinery — would force revision of Primitive 11.
- **Audit.** Q.3 Memo 02 §3.6 + Q.3 Memo 03 §2 established that Primitive 11 admits the vertex-anchored commitment specification as a structural extension at Q.3 level (vertex-density-dependent commitment rate replacing per-proper-time accounting). At W1 + W2 level, this admissibility lifts: the affine-parameter framework supplies the parametrisation that the vertex-density measure operates on.
  
  Full reconciliation (i.e., explicit derivation of how the vertex-density measure on the affine parameter relates to Primitive 11's general specification) is **W4 work in Memo 02**, not W1 + W2. At W1 + W2 level, the structural admissibility is established; full reconciliation pending Memo 02.
- **Verdict on WFal-7: NOT triggered at W1 + W2 level.** Full reconciliation deferred to W4 / Memo 02.

### 6.5 Cumulative falsifier-status table for W1 + W2

| Falsifier | Status | Where dispatched |
|---|---|---|
| **WFal-1** (W1 primitive incompat.) | **NOT triggered** | §6.1 + §4 |
| **WFal-2** (second-quant. incompat.) | **NOT triggered** | §6.2 + §4 |
| **WFal-3** (vacuum-field aspect — W3) | deferred to Memo 02 | — |
| **WFal-4** (vertex-to-worldline lifting — W4) | deferred to Memo 02 | — |
| **WFal-5** (Q.7 ⟷ Q.8 circular — W5/W6) | deferred to Memo 03/04 | — |
| **WFal-6** (Theorem 6 incompat.) | **NOT triggered** | §6.3 |
| **WFal-7** (P-11 incompat. lifting) | NOT triggered at W1+W2 level; full audit Memo 02 | §6.4 |
| **WFal-8** (UV-FIN conflict — propagator content) | NOT triggered at structural level (propagator form W2-defined; full propagator details with vacuum content Q.8) | §3.1.4 |

**No falsifier triggered for W1 or W2.** Three falsifiers (WFal-3, WFal-4, WFal-5) deferred to Memo 02 / Memo 03–04 dispatch. Two falsifiers (WFal-7, WFal-8) NOT triggered at W1 + W2 level with full audits deferred to Memo 02 / Memo 03–04.

---

## 7. Provisional Verdicts for W1 and W2

### 7.1 W1 verdict

**W1 (lightlike-worldline structure under GRH): CANDIDATE-FORCED.**

Specifically: $\tau_g$'s worldline tangent $u^\mu$ satisfies $u_\mu u^\mu = 0$ (null propagation, FORCED by GRH-4 + standard relativistic kinematics), with the affine-parameter $\lambda$ replacing proper-time parametrisation (FORCED by Step 4 of §2.1's derivation; affine reparametrisation freedom $\lambda \to a\lambda + b$). All four W1 commitments (null propagation, affine parameter, tangent structure, Lorentz behaviour) are primitive-level admissible across P-02, P-06, P-13.

The "FORCED" force is unconditional at the W1 level — no empirical inheritance enters at this level (the affine parameter is a structural object, not a value to be measured). The "CANDIDATE" qualifier reflects the conditional-forcing structure of the broader GRH closure trajectory (specific gauge-group choice + downstream Q.8 closure pending).

R-1 closure trajectory: W1 contributes the affine-parameter machinery side.

### 7.2 W2 verdict

**W2 (second-quantised worldline/field correspondence): CANDIDATE-FORCED.**

Specifically: the minimal second-quantised operator framework for $\tau_g$ (field operator $\hat{A}^a_\mu(x)$, mode expansion in null momentum modes, creation/annihilation operators satisfying Theorem 6, propagator content consistent with Theorem 7's UV-FIN structure) is structurally admissible and complete at the W2 level. Worldlines arise as expectation-value trajectories, support curves of $\tau_g$ excitations, and null curves under GRH — all three interpretations structurally equivalent.

The "CANDIDATE" qualifier reflects:
- Specific gauge-group choice + coupling values + representations remain empirical.
- Full propagator details with vacuum content (specifically iε prescriptions) are Q.8 work.
- W3 (background-field aspect) and W4 (vertex-to-worldline lifting) remain Memo 02 work.

R-1 closure trajectory: W2 contributes the second-quantised framework side.

### 7.3 R-1 closure verdict

**R-1 (lightlike-worldline reformulation): CLOSED — CANDIDATE-FORCED at Q.7 Memo 01.**

W1 + W2 jointly close R-1 at the structural level. The affine-parameter machinery (W1) and the second-quantised operator framework (W2) integrate cleanly; no falsifier triggered at the primitive-level audit. Per-worldline commitment events for $\tau_g$ are realised as creation/annihilation operator actions at vertex events along the affine-parameter-parametrised null worldline.

R-1 status flag updates:
- Pre-Memo-01: "outstanding"
- Post-Memo-01: "**CLOSED — CANDIDATE-FORCED at Q.7 Memo 01**"

### 7.4 Justification

The verdicts rest on:

- **Primitive-level audit (§4).** All seven primitives (P-02, P-04, P-06, P-07, P-10, P-11, P-13) support W1 + W2. No primitive forbids.
- **Inherited theorem structure.** Theorem 1 (spin-statistics, bosonic commutation for Case P), Theorem 6 (canonical commutation, lift to lightlike case), Theorem 7 (UV-FIN, finite propagators), Theorems 8/9 (V₁ vacuum kernel, finite-width regulator background) all support the W2 framework.
- **GRH + Q.2 + Q.3 inheritance.** GRH-4 forces masslessness → null propagation; Q.2 closure supplies non-Abelian admissibility + kinematic gauge-quotient; Q.3 closure supplies vertex content + vertex-mediated individuation that lifts to W2's operator framework.
- **Falsifier status (§6).** WFal-1, WFal-2, WFal-6 NOT triggered. WFal-7 NOT triggered at W1 + W2 level (full audit Memo 02). WFal-8 NOT triggered at structural level (full propagator details Q.8).

### 7.5 Why CANDIDATE-FORCED rather than FORCED unconditionally

R-1 closure inherits the conditional-forcing structure of the broader GRH closure trajectory:
- Specific gauge-group choice empirical (per Q.2 F4 inherited).
- Coupling constant values empirical via Dimensional Atlas.
- Q.8 closure pending for full vacuum-state structure (the propagator's iε prescription, full vacuum-state content).

The CANDIDATE-FORCED verdict is the strongest defensible substage-level closure for R-1 at Memo 01.

---

## 8. Implications for R-1 and Downstream Refinements

### 8.1 R-1 status update

**R-1 CLOSED at Q.7 Memo 01.**

R-1 had Q.7 as its sole closure stage (per Q.7 Memo 00 §3 refinement mapping). With W1 + W2 closed at this Memo, R-1 is fully discharged.

### 8.2 What remains for R-5 partial (W3, W5)

R-5 partial (vacuum-field aspect of $\tau_g$'s vacuum-vs-particle status) requires:
- **W3 (Memo 02):** distinguish $\tau_g$ as background field $\langle \hat{A}^a_\mu \rangle$ from $\tau_g$ as particle excitations.
- **W5 (Memo 03 or 04):** pre-vacuum scoping — what Q.7 can say before Q.8's full vacuum work.

W3 + W5 build on W2's operator framework (background field as expectation value of $\hat{A}^a_\mu$ in some non-trivial state; particle excitations as creation operator actions on this background).

### 8.3 What remains for R-3 Q.7-side (W4)

R-3 Q.7-side (per-worldline accounting integrating Q.3's vertex-anchored commitment) requires:
- **W4 (Memo 02):** integrate Q.3 V4's vertex-density commitment rate with Phase-1's per-worldline commitment-dynamics in the affine-parameter framework supplied by W1.

W4 builds on W1's affine-parameter machinery + Q.3's vertex-anchored commitment structure.

### 8.4 What remains for R-5 completion (Q.8)

R-5 completion (zero-point aspect of $\tau_g$'s vacuum status) is Q.8 work. Includes:
- Zero-point fluctuations as primitive-level vacuum content.
- Vacuum polarisation diagrams + virtual vertex pairs.
- Full vacuum-state structure (the iε prescription for time-ordered propagators; vacuum expectation values of all operator products).
- Reconciliation with Λ-from-V₁ derivation (Phase-3 background, Theorems 8 + 9).

### 8.5 Updated GRH refinement-closure map (post-Memo 01)

| Refinement | Pre-Memo-01 status | Post-Memo-01 status | Closure stage |
|---|---|---|---|
| **R-1** | outstanding | **CLOSED CANDIDATE-FORCED ✅** | **Q.7 Memo 01 (this)** |
| R-2 partial | CLOSED (Q.2 Memo 02) | (unchanged) | Q.2 Memo 02 |
| R-2 completion | CLOSED (Q.3 Memo 02) | (unchanged) | Q.3 Memo 02 |
| R-2 FULL | FULLY CLOSED | (unchanged) | Q.2 + Q.3 |
| R-3 Q.3-side | CLOSED (Q.3 Memo 02) | (unchanged) | Q.3 Memo 02 |
| **R-3 Q.7-side** | outstanding | outstanding | **Q.7 Memo 02 (W4)** |
| R-4 | CLOSED (Q.2 Memo 01) | (unchanged) | Q.2 Memo 01 |
| **R-5 partial** | outstanding | outstanding | **Q.7 Memo 02 / 03 (W3 + W5)** |
| R-5 completion | outstanding | (unchanged) | Q.8 |

**Cumulative closure: 5/7 refinement items closed (R-1 + R-2 partial + R-2 completion + R-3 Q.3-side + R-4); 2/7 + R-3 Q.7-side outstanding for Q.7 Memo 02 + Q.8.**

---

## 9. Honest Scope Limits

Memo 01 addresses W1 + W2 only — *lightlike-worldline structure* + *second-quantised correspondence*. The following are explicitly out of scope:

### 9.1 Deferred to Q.7 Memo 02

- **W3 (background-field aspect of $\tau_g$, R-5 partial).** Memo 02 substantive content.
- **W4 (vertex-to-worldline lifting, R-3 Q.7-side).** Memo 02 substantive content; full reconciliation of Primitive 11 with affine-parameter machinery.
- **WFal-3, WFal-4, WFal-7 (full audit) dispatch.**

### 9.2 Deferred to Q.7 Memo 03 / 04

- **W5 (pre-vacuum structure scoping).**
- **W6 (downstream dependency map for Q.8).**
- **Q.7 substage verdict.**

### 9.3 Deferred to Q.8

- **R-5 completion (zero-point aspect).** Vacuum-state vertex content; vacuum polarisation; virtual vertex pairs; full vacuum-state structure.
- **Full propagator details** (iε prescription for time-ordered propagators; vacuum expectation values).
- **Λ derivation refinement** (extension of Theorem 9's V₁ + Synge content).
- **Specific renormalisation prescriptions** — ED inherits UV-FIN; specific prescriptions are empirical / convention.

### 9.4 Outside the GRH closure trajectory

- **Specific gauge group choice.** Empirical inheritance per Q.2 F4.
- **Coupling constant values.** Empirical via Dimensional Atlas.
- **Charged-rule-type representations.** Empirical / Q.4-onward.
- **Higgs sector / SSB.** Q.4; SPECULATIVE.
- **Generation structure.** Q.6 / empirical.
- **Standard QFT amplitude content** (cross-sections, S-matrix elements). Built from Q.7's framework but specific computations downstream of GRH closure.

---

## 10. One-Line Summary

> Q.7 Memo 01 closes W1 (lightlike-worldline structure under GRH) at **CANDIDATE-FORCED** by deriving the null-propagation condition from GRH-4 + standard relativistic kinematics ($\sigma_{\tau_g} = 0$ ⟹ $u_\mu u^\mu = 0$ in 3+1D Minkowski) and replacing proper-time parametrisation (degenerate for null curves with $d\tau = 0$) with affine-parameter machinery $\lambda$ admitting the affine reparametrisation freedom $\lambda \to a\lambda + b$ as structural symmetry, plus W2 (second-quantised worldline/field correspondence) at **CANDIDATE-FORCED** by constructing the minimal operator framework ($\hat{A}^a_\mu(x)$ field operator, mode expansion in null momentum modes, creation/annihilation operators satisfying canonical commutation per Theorem 6, finite propagator content per Theorem 7 UV-FIN, finite-width regulator inheriting from Theorems 8 and 9 V₁ kernel) that realises worldlines as expectation-value trajectories + support curves of $\tau_g$ excitations + null curves under GRH (three structurally equivalent interpretations) — across a clean primitive-level audit (P-02, P-04, P-06, P-07, P-10, P-11, P-13 all actively support, no primitive forbids), no falsifier triggered for W1 or W2 (WFal-1, WFal-2, WFal-6 NOT triggered; WFal-7 NOT triggered at W1+W2 level with full audit deferred to Memo 02; WFal-8 NOT triggered at structural level with full propagator details Q.8) — discharging **R-1 (lightlike-worldline reformulation)** fully at Q.7 Memo 01 and advancing the GRH closure trajectory toward Q.7 Memo 02 (W3 background-field aspect for R-5 partial; W4 vertex-to-worldline lifting for R-3 Q.7-side) with cumulative GRH closure progress now 5/7 refinements closed (R-1 + R-2 partial + R-2 completion + R-3 Q.3-side + R-4), R-3 Q.7-side + R-5 partial + R-5 completion remaining for Q.7 Memo 02 + Q.8.

---

## Recommended Next Steps

**(a) Begin Q.7 Memo 02 (W3 + W4; R-5 partial + R-3 Q.7-side closure).** The natural next deliverable. Memo 02 should: (i) derive W3 ($\tau_g$ excitation vs background at the worldline level) — distinguish background field $\langle \hat{A}^a_\mu \rangle$ from particle excitations on top; (ii) derive W4 (vertex-to-worldline lifting) — integrate Q.3 V4's vertex-density commitment rate with Phase-1's per-worldline commitment-dynamics in the affine-parameter framework; (iii) dispatch falsifiers WFal-3, WFal-4, WFal-7 (full audit); (iv) state R-5 partial closure + R-3 Q.7-side closure verdicts. Anticipated length: comparable to this Memo 01 (substantive primitive-level work for W3 + W4 integration).

**(b) Pre-Memo-02 audit of the relationship between background field $\langle \hat{A}^a_\mu \rangle$ and the V₁ vacuum kernel (Theorem 8).** A short audit (15-30 minutes) confirming the structural relationship: the V₁ kernel governs vacuum two-point correlations; the background field is the expectation value $\langle \hat{A}^a_\mu \rangle$ in the (Q.8-deferred) vacuum state; these are consistent. Important for W3 derivation.

**(c) Verify the propagator structural form noted in §3.1.4 against Theorem 7 UV-FIN.** A short derivation (2-3 paragraphs) confirming that the propagator $\Delta^{ab}_{\mu\nu}(x-y) \propto \delta^{ab} \eta_{\mu\nu} K(x-y)$ with V₁-kernel-supplied finite-width regulator $K(x-y)$ inherits Theorem 7's UV-FIN structure cleanly. Important for WFal-8 final dispatch (currently NOT triggered at structural level; full audit Q.8).

**(d) Defer memory-record update until Q.7 closure (Memo 03 or Memo 04).** Per the discipline established. The bundled memory update will capture R-1 closure + R-3 Q.7-side closure + R-5 partial closure + Q.7 substage verdict + downstream handoffs to Q.8 + cumulative refinement-closure status.

**(e) (Optional) Sketch W3's background-field-vs-excitation distinction now.** With R-1 closed and W2's operator framework established, the W3 derivation strategy can be pre-sketched: background field as $\langle \hat{A}^a_\mu \rangle$ in a coherent state or a non-trivial vacuum; particle excitations as creation operator actions $\hat{a}^\dagger_k$ shifting the state away from the background. Pre-sketching would let Memo 02 land into a known structure. Optional but useful for trajectory planning.
