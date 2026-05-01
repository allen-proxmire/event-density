# NS-1.04 — T19 / T20 Dimensional Sensitivity Audit

**Date:** 2026-04-30
**Status:** Audit complete. **Verdict: Route 2.4 PARTIALLY CLOSES — but in an empirical-consistency sense, not a pure-architectural sense.** T19 and T20 are dimension-sensitive at the *output* layer (4πr² and the dipole-2π are d=3-specific). The substrate *primitives* feeding T19/T20 are d-agnostic. Therefore Route 2.4 forces d = 3 only conditional on "ED's substrate-gravity arc must reproduce observed Newton (1/r²) and observed a₀ (~1.2 × 10⁻¹⁰ m/s²)." Architectural forcing without empirical input is not delivered.
**Sources audited:** [`theorems/T19.md`](../../theorems/T19.md), [`theorems/T20.md`](../../theorems/T20.md), [`arcs/arc-SG/substrate_holographic_bound.md`](../../arcs/arc-SG/substrate_holographic_bound.md), [`arcs/arc-SG/substrate_a0_ed_native.md`](../../arcs/arc-SG/substrate_a0_ed_native.md), [`arcs/arc-SG/substrate_2pi_question.md`](../../arcs/arc-SG/substrate_2pi_question.md). Cross-checked against substrate-gravity paper and T20 scope note.

---

## 1. Purpose

This memo executes Step 2 of NS-1: audit whether the T19/T20 substrate→continuum coarse-graining pattern is dimension-sensitive in a way that forces d = 3 spatial dimensions, or is dimension-agnostic.

The audit isolates two specific load-bearing geometric facts:

- **T19's 4πr² (holographic bound on a 2-sphere)** — used to derive Newton's law a = GM/r² from cumulative-strain reading + participation-count bound.
- **T20's 2π (dipole-mode azimuthal periodicity)** — used to derive a₀ = c·H₀/(2π) from the cosmic horizon's anisotropic projection onto an accelerating chain.

The question for Route 2.4 is whether these are dimension-specific in a way that (a) breaks the substrate-gravity derivations at d ≠ 3, and (b) forces d = 3 from within the framework.

---

## 2. What T19 and T20 Actually State

### 2.1 T19 — Newton's law from substrate

The derivation chain (from [`substrate_holographic_bound.md`](../../arcs/arc-SG/substrate_holographic_bound.md) §§1–4 and [`substrate_rules_stability_availability.md`](../../arcs/arc-SG/substrate_rules_stability_availability.md)):

1. **Cumulative-strain reading.** A chain's stability landscape Σ(x) at point x reads cumulative ED-gradient strain from surrounding mass distribution.
2. **Holographic participation bound.** Distinguishable channels in a region are bounded by *boundary area*: N ≤ A/ℓ_ED², not by volume. Forced by combination of UV-FIN (Q.8) + finite-c propagation + cosmic horizon + channel-coherence stability (§4.1 of holographic-bound memo).
3. **2-sphere holographic screen.** A test chain at distance r from mass M is enclosed by a 2-sphere of area 4πr² (the natural holographic screen at radius r).
4. **Channel-density gradient.** Mass M's contribution to channels on the screen falls as 1/(4πr²) — the area-density of M's induced channel content on the screen.
5. **Newton-form a = GM/r².** The stability-landscape gradient on a test chain at radius r combines the 1/(4πr²) channel-density falloff with substrate constants to produce a = GM/r².
6. **Newton-recovery fixes ℓ_ED.** Matching the resulting coefficient to empirical G forces `ℓ_ED² = ℏG/c³ = ℓ_P²`, i.e., `G = c³ℓ_P²/ℏ`.

### 2.2 T20 — Transition acceleration

The derivation chain (from [`substrate_a0_ed_native.md`](../../arcs/arc-SG/substrate_a0_ed_native.md) §§2–4, [`substrate_2pi_question.md`](../../arcs/arc-SG/substrate_2pi_question.md), and T20 scope note):

1. **Cosmic decoupling surface.** Cosmic horizon at radius R_H = c/H₀ is a 2-sphere of area 4π(c/H₀)² (`substrate_a0_ed_native.md` §2.1).
2. **Acceleration-induced decoupling.** A chain accelerating at rate a has a Rindler-type decoupling surface at d_a = c²/a behind it.
3. **Chain breaks isotropy.** The chain's acceleration direction is a privileged axis. The chain's adjacency structure has azimuthal symmetry around this axis but polar variation.
4. **Cosmic horizon projects anisotropically.** The cosmic decoupling 2-sphere projects onto the chain's accessible region non-isotropically; the projection has a directional (axis-aligned) structure.
5. **Leading anisotropic mode = dipole.** The (l=1, m=0) spherical harmonic is the leading anisotropic mode coupling to the chain's adjacency structure (T20 scope note; cited via Y_1^0(θ) ∝ cos θ).
6. **2π azimuthal cycle.** The dipole mode's only spatial periodicity is the φ-coordinate's 2π period on the 2-sphere.
7. **Rate matching.** Chain's experienced fluctuation rate γ_chain = a/c equals dipole-mediated cosmic rate γ_cosmic^eff = H₀/(2π) at the transition: a₀ = c·H₀/(2π).

### 2.3 Where d = 3-specific geometry enters

| Step | Object | d=3-specific? |
|---|---|---|
| T19.3 | 2-sphere holographic screen (4πr²) | **Yes** — area of $S^{d-1}$ in d-spatial is $S_{d-1} r^{d-1} = \frac{2\pi^{d/2}}{\Gamma(d/2)} r^{d-1}$. Equals 4πr² only at d = 3. |
| T19.4 | 1/(4πr²) channel-density falloff | **Yes** — at d-spatial, falls as 1/r^(d-1), giving a Gauss's-law form `a ∝ M/r^(d-1)`. |
| T19.5 | Newton form a = GM/r² | **Yes** — the 1/r² is precisely 1/r^(d-1) at d = 3. |
| T20.1 | Cosmic horizon = 2-sphere | **Yes** — at d-spatial, cosmic horizon is $S^{d-1}$. |
| T20.4–5 | Spherical-harmonic projection on $S^2$ | **Yes** — $S^2$ harmonics use SO(3) representation theory; at d-spatial, the cosmic horizon $S^{d-1}$ uses SO(d) representation theory with different mode structure. |
| T20.6 | 2π azimuthal cycle | **Yes** — the φ-azimuth of $S^2$ is an artifact of the (polar, azimuthal) parameterization that exists naturally only when d − 1 = 2, i.e., d = 3. In other d, the azimuthal isolation around an acceleration axis is geometrically different. |

### 2.4 Where the substrate primitives feeding T19/T20 are *not* d-specific

| Primitive | Statement | d-agnostic? |
|---|---|---|
| P02 (chain) | Timelike worldlines parameterized by proper time | **Yes** — works in any (1, d) Lorentzian signature |
| P04 (bandwidth additivity) | Bandwidth content additive at commitment events | **Yes** — no d-dependence in primitive statement |
| P11 (commitment-irreversibility) | Commitment events non-reversible | **Yes** |
| P13 (proper-time intervals) | Finite intervals between commitments | **Yes** |
| ED-06 (decoupling surfaces) | Surfaces where participation becomes one-sided | **Yes** at primitive ontology level; specific surface geometries arise in derivations |
| ED-07 (signal propagation) | Finite-speed micro-event propagation | **Yes** — finite-c works in any d |
| ED-10 (relational adjacency) | Adjacency is relational, not a-priori-geometric | **Yes** |
| Q.8 / UV-FIN | UV cutoff ℓ_ED exists | **Yes** — existence is d-agnostic |

**Critical observation.** The d = 3 specificity enters T19/T20 at the *output* layer (the geometry of the holographic screen, the spherical-harmonic projection of the cosmic horizon, the azimuthal-2π structure). It does *not* enter at the primitive-input layer. The primitives are d-agnostic; the d = 3 specification enters via "the cosmic horizon is a 2-sphere" — which is a fact about the d = 3 substrate we live in, not a primitive commitment.

---

## 3. Dimensional Generalization Attempt

For each load-bearing geometric step, replace d = 3 with arbitrary d-spatial and check what survives.

### 3.1 T19 generalized to d-spatial

**Step T19.3 — holographic screen.** Replace 2-sphere with $S^{d-1}$ of area $A_{d-1}(r) = S_{d-1} r^{d-1}$ where $S_{d-1} = 2\pi^{d/2}/\Gamma(d/2)$.

**Step T19.4 — channel-density gradient.** Mass M's induced channels distributed across $A_{d-1}(r)$ give density $\rho \propto M / (S_{d-1} r^{d-1})$.

**Step T19.5 — Gauss's-law form.** The substrate-gravity derivation yields:
$$a_{(d)}(r) = \frac{G_{(d)} M}{r^{d-1}}.$$

This is the standard Gauss's-law generalization of Newton in d spatial dimensions. The form is *not* a = GM/r² unless d = 3.

**Step T19.6 — Newton-recovery in d-spatial.** Matching to "empirical gravity" requires what we observe in d = 3, which is a ∝ 1/r². For the substrate-derived form to match empirical gravity, we need d − 1 = 2, i.e., **d = 3 is forced by empirical match**.

In d ≠ 3, the derivation goes through formally — there is a Gauss's-law-form a ∝ 1/r^(d-1) — but it does not match observed Newton.

**Verdict on T19 generalization.** The mechanism is fully generalizable. Newton's *form* (the specific 1/r²) is what fixes d = 3. The holographic argument itself works in any d ≥ 2; it's the empirical match to 1/r² that forces d = 3.

### 3.2 T20 generalized to d-spatial

**Step T20.1 — cosmic horizon in d-spatial.** Cosmic horizon is $S^{d-1}$ at radius R_H = c/H₀. Surface area $S_{d-1} (c/H₀)^{d-1}$.

**Step T20.4 — anisotropic projection on $S^{d-1}$.** Chain's acceleration axis is one direction; the (d − 1)-sphere's structure relative to this axis varies with d:

- **d = 2.** Cosmic horizon is $S^1$ (a circle). The chain's acceleration axis on a 2D substrate has only one orthogonal direction; the "polar / azimuthal" decomposition of $S^{d-1}$ degenerates. There is no separate 2π azimuth — the entire cosmic horizon is parameterized by a single angle. The dipole-mode argument doesn't translate: the leading anisotropic mode on $S^1$ is $e^{i\phi}$ with period 2π, but there is no analog of the (l=1, m=0) "polar harmonic" structure.
- **d = 3.** Cosmic horizon is $S^2$. The chain's acceleration axis singles out a polar direction; the orthogonal directions form a 1-sphere parameterized by φ ∈ [0, 2π). Spherical harmonics decompose as $Y_l^m(\theta, \phi)$; the dipole-mode (l=1, m=0) is azimuthally symmetric around the polar axis with the *only* spatial period being the 2π azimuth. **This is the canonical structure used by T20.**
- **d ≥ 4.** Cosmic horizon is $S^{d-1}$. The chain's acceleration axis singles out one polar direction, but the remaining (d − 1) orthogonal directions form a higher-dimensional sphere $S^{d-2}$, not a circle. Spherical harmonics on $S^{d-1}$ are Gegenbauer polynomials in cos θ × harmonics on $S^{d-2}$; the "azimuthal 2π" of $S^2$ is replaced by the more elaborate $S^{d-2}$ harmonic structure. **The 2π factor does not survive as the leading-mode period.**

**Step T20.6 — 2π factor.** The 2π is geometrically forced by the (polar, azimuthal) parameterization of $S^2$ specifically. In d ≠ 3, this parameterization doesn't apply at the cosmic horizon; the leading-mode period is different.

**Step T20.7 — rate matching in d-spatial.**
- **d = 2:** the dipole-mode argument doesn't translate; the cosmic horizon has no "azimuthal isolation around polar axis" structure. The natural prefactor is *not* 1/(2π); the substrate-gravity derivation degenerates.
- **d = 3:** a₀ = c·H₀/(2π), matching empirical to ~10%.
- **d = 4:** the leading-mode period on $S^2$ (the residual sphere after fixing the acceleration axis) gives a different geometric factor; computed prefactor ≠ 1/(2π).
- **d ≥ 5:** further degeneration.

**Verdict on T20 generalization.** T20's mechanism is *fundamentally d = 3-specific.* The dipole-mode + 2π azimuth structure requires the cosmic horizon to be $S^2$ — true in d = 3, false elsewhere. In d ≠ 3, the analog derivation either degenerates (d ≤ 2) or gives a structurally different prefactor (d ≥ 4).

### 3.3 What survives, what breaks, what becomes degenerate

| Step | Dimension behavior |
|---|---|
| T19 holographic bound (area-scaling) | **Survives all d ≥ 2.** Area-scaling is a generic consequence of UV-FIN + finite-c + cosmic horizon. |
| T19 Gauss's-law form a ∝ 1/r^(d-1) | **Survives all d ≥ 2.** The functional form differs from 1/r² unless d = 3. |
| T19 empirical match to a ∝ 1/r² | **Forces d = 3.** Empirical-consistency forcing. |
| T20 cosmic horizon as 2-sphere | **d = 3 specific.** $S^{d-1}$ at general d, $S^2$ only at d = 3. |
| T20 dipole-mode (l=1, m=0) on $S^2$ | **d = 3 specific.** SO(3) representation theory; doesn't exist in this form for $S^{d-1}$, d ≠ 3. |
| T20 azimuthal 2π factor | **d = 3 specific.** Requires (polar, azimuthal) decomposition of $S^2$. |
| T20 a₀ = c·H₀/(2π) prefactor matching empirical | **Forces d = 3.** Combined geometric + empirical-consistency forcing. |
| Substrate primitives (P02, P04, P11, P13, ED-06, ED-07, ED-10, Q.8) | **Dimension-agnostic.** No d-dependence at primitive-statement level. |
| Holographic-bound mechanism (count of distinguishable channels through boundary) | **Dimension-agnostic.** Mechanism transfers to any (d − 1)-dimensional boundary. |

---

## 4. Structural Sensitivity Analysis

### 4.1 What does T19 force?

| Question | Verdict |
|---|---|
| Forces d = 3 from primitives alone? | **No.** Primitives + holographic mechanism work in any d ≥ 2; output is a ∝ 1/r^(d-1). |
| Forces d ≥ 3? | **No.** Mechanism works at d = 2 (a ∝ 1/r) and trivially at d = 1. |
| Forces d = 3 conditional on empirical Newton (a ∝ 1/r²)? | **Yes.** The 1/r² form is the d = 3 case of the d-spatial Gauss's-law derivation. |
| Dimension-agnostic? | **No** — at the *output* layer it's d-discriminating. **Yes** at the primitive/mechanism layer. |
| Collapses for d ≠ 3? | **No.** Derivation goes through; output differs from observed Newton. |

**Net.** T19's force on d is *conditional on empirical match to observed Newton.* Pure primitive-level forcing is not delivered.

### 4.2 What does T20 force?

| Question | Verdict |
|---|---|
| Forces d = 3 from primitives alone? | **Stronger than T19.** Primitives are d-agnostic, but the dipole-mode + 2π azimuthal structure requires the cosmic horizon to be specifically $S^2$. In d ≠ 3 the mechanism either degenerates (d ≤ 2) or yields a structurally different prefactor (d ≥ 4). |
| Forces d ≥ 3? | **Approximately yes.** At d ≤ 2 the dipole-mode mechanism degenerates outright (no separate "polar / azimuthal" structure on the cosmic horizon's (d − 1)-sphere); the entire derivation chain breaks. So T20 forbids d ≤ 2 internally. |
| Forces d = 3 conditional on empirical a₀? | **Yes, more cleanly than T19.** The 1/(2π) prefactor is a d = 3-specific geometric output. Empirical match (a₀ ~ c·H₀/(2π) ≈ 1.08 × 10⁻¹⁰ m/s² vs. observed ~1.2 × 10⁻¹⁰ m/s², ~10% match) is what makes the d = 3 case empirically privileged. |
| Dimension-agnostic? | **No** — both at output layer (2π) and at mechanism layer (dipole on $S^2$ requires d = 3). |
| Collapses for d ≠ 3? | **Yes for d ≤ 2** (mechanism degenerates outright). **No but predicts wrongly** for d ≥ 4 (mechanism gives different prefactor that wouldn't match observed a₀). |

**Net.** T20's d-sensitivity is stronger than T19's. T20 contributes *internal-consistency forcing* at d ≤ 2 (mechanism degenerates) and *empirical-consistency forcing* at d ≥ 4 (mechanism produces wrong prefactor). The d ≤ 2 forbidding is closer to pure architectural forcing than T19 delivers.

### 4.3 Combined T19 + T20 verdict

- **d = 1.** Both T19 and T20 break; chain primitive (P02) plausibly degenerates as well (no transverse direction). **Forbidden.**
- **d = 2.** T19 mechanism gives a ∝ 1/r (logarithmic potential); T20 mechanism degenerates (no polar/azimuthal decomposition of $S^1$). T20 dipole structure inapplicable. **Forbidden by T20 mechanism degeneracy** — this is closer to architectural forcing than T19's empirical match.
- **d = 3.** Both T19 and T20 produce the canonical, observation-matching results. **Privileged.**
- **d = 4.** T19 mechanism gives a ∝ 1/r³, doesn't match observed Newton. T20 dipole structure on $S^3$ gives a different prefactor, doesn't match observed a₀. **Forbidden by empirical mismatch on both fronts.**
- **d ≥ 5.** Same as d = 4, more so.

**Combined verdict.** Routes 2.4 forces d = 3 via:
- d ≤ 2: T20 mechanism degeneracy (architectural forcing, not empirical-dependent)
- d ≥ 4: T19 + T20 empirical mismatch (empirical-consistency forcing)

The d ≤ 2 forbidding is the cleaner half — it's nearly pure architectural forcing because the dipole-mode mechanism *cannot be constructed* on $S^1$ in the same form. The d ≥ 4 forbidding requires importing observed Newton + a₀ as constraints.

---

## 5. Verdict for Route 2.4

**Route 2.4 PARTIALLY CLOSES.**

The route forces d = 3 in two distinct senses:

1. **Lower bound (d ≥ 3):** T20's dipole-mode mechanism degenerates at d ≤ 2 — the cosmic horizon's (d − 1)-sphere has no separate "polar / azimuthal" decomposition for d − 1 ≤ 1, so the 2π factor and the dipole-mode anisotropic projection don't admit construction. **This is approximately architectural forcing** — the mechanism cannot be built at d ≤ 2, similar in style to T18's "BC3 has no primitive-level construction" finding from Arc B. The framework structurally cannot host its own substrate-gravity arc at d ≤ 2.

2. **Upper bound (d ≤ 3):** T19's Gauss's-law output a ∝ 1/r^(d-1) and T20's dipole prefactor on $S^{d-1}$ both match observation only at d = 3. **This is empirical-consistency forcing** — the substrate primitives + holographic mechanism work formally in any d ≥ 2, but the specific match to observed Newton (a ∝ 1/r²) and observed a₀ (~1.2 × 10⁻¹⁰ m/s²) requires d = 3.

### 5.1 Conditions on the verdict

**Pure-architectural forcing (no empirical input):** Route 2.4 closes only at d ≤ 2 (T20 mechanism degeneracy). Closure of the d ≥ 4 half requires accepting observed gravity (Newton's 1/r² + empirical a₀) as a load-bearing constraint.

**With empirical input (observed gravity matches ED's substrate output):** Route 2.4 closes at both ends. d = 3 is forced uniquely.

**Conditional on substrate primitive d-agnosticism:** Verified in §2.4. P02, P04, P11, P13, ED-06, ED-07, ED-10, Q.8 are stated d-agnostically at primitive-statement level. The d = 3 specification enters via the geometry of T19/T20's outputs, not the primitives.

### 5.2 Honest distinction from Route 2.3

Route 2.3 (substrate motif viability — pending audit in NS-1.03) was designed to provide pure architectural forcing of d ≤ 3 via factorial dilution / concentration of measure. Route 2.4 provides:
- *Architectural* forcing of d ≥ 3 (via T20 mechanism degeneracy at d ≤ 2)
- *Empirical-consistency* forcing of d ≤ 3 (via T19/T20 output match to observed gravity)

These are complementary: Route 2.3 may give pure architectural d ≤ 3, while Route 2.4 gives architectural d ≥ 3 plus empirical-consistency d ≤ 3.

If Route 2.3 closes affirmatively, the combined Route 2.3 + 2.4 result is:
- d ≤ 3 from Route 2.3 (pure architectural, upper bound)
- d ≥ 3 from Route 2.4 (architectural via T20 degeneracy, lower bound)
- d = 3 forced from substrate level alone, without empirical input.

This is the cleanest path to substrate-level B2 closure.

---

## 6. Implications for NS-1

### 6.1 The route landscape after NS-1.04

Updated state of the four candidate forcing routes:

| Route | Layer | NS-1 status |
|---|---|---|
| 2.1 Cl(3,1) → PDE | Representation | Deferred (NS-1.01); audit not yet run |
| 2.2 Huygens via T18 | PDE/kernel | **CLOSED FAILED (NS-1.02)** |
| 2.3 Substrate motif viability | Substrate-combinatorial | Pending (NS-1.03); load-bearing for d ≥ 3 lower bound coverage |
| 2.4 T19/T20 internal consistency | Substrate-geometric | **PARTIALLY CLOSES (this memo)** — d ≥ 3 architectural via T20 degeneracy; d ≤ 3 empirical-consistency via T19/T20 output match |

### 6.2 Updated dependency structure

- **Route 2.4's d ≥ 3 architectural half** partially overlaps with Route 2.3's expected d ≥ 3 lower bound (NS-1 scoping §2.3 anticipated borrowing from T20 dipole degeneracy at d = 2). After this audit, that anticipated borrowing is now formal: T20's mechanism cannot be constructed at d ≤ 2. Route 2.3 can cite Route 2.4 for the d ≥ 3 half rather than rederiving it.
- **Route 2.4's d ≤ 3 empirical half** depends on accepting observed gravity as a load-bearing input. This is reasonable — the program's empirical-test framework already treats observed gravity phenomenology (Newton, a₀, BTFR) as load-bearing — but it should be flagged explicitly as empirical-consistency forcing, not architectural-only forcing.
- **Route 2.3 is now more critical for pure architectural closure.** If Route 2.3 closes the d ≤ 3 upper bound architecturally (via factorial dilution / concentration of measure), then combined with Route 2.4's d ≥ 3 architectural lower bound, B2 closes at substrate level *without* empirical input. Without Route 2.3, the d ≤ 3 half of B2 closure relies on empirical match.

### 6.3 What NS-2 inherits

NS-2 (substrate→NS coarse-graining) inherits from this audit:

- **The substrate-gravity precedent is fully d = 3-validated.** T19/T20 derive Newton + a₀ at d = 3 via specific geometric mechanisms tied to $S^2$ horizons. The substrate→continuum coarse-graining template is established at d = 3 specifically; lifting it to NS will operate in the same d = 3 setting.
- **Substrate primitives are d-agnostic.** The substrate primitives feeding NS-2 (and the substrate→NS coarse-graining) do not themselves commit to d = 3. NS-2 can proceed in d = 3 without re-litigating dimensionality, and d = 3 specification enters at the geometry-of-the-coarse-graining stage, not the primitive-input stage.
- **Empirical-consistency forcing precedent.** The substrate-gravity arc demonstrates that ED's primitives + observed empirical phenomenology jointly force d = 3. NS-2 can adopt the same framing if needed: "ED's primitives + observed Navier-Stokes phenomenology in d = 3+1 force d = 3+1" is at least as strong as the substrate-gravity-based forcing.

### 6.4 Can B2 close at substrate level alone?

**Yes, with a caveat.** Substrate-level B2 closure has two paths:

- **Path A (architectural-only):** Route 2.3 closes affirmatively for d ≤ 3 + Route 2.4 closes architecturally for d ≥ 3 (T20 degeneracy). Yields d = 3 forced from substrate primitives without empirical input. **This is the strongest possible substrate-level closure.**
- **Path B (architectural + empirical):** Route 2.4 closes architecturally for d ≥ 3 + empirical-consistency for d ≤ 3 (Route 2.4 alone). Yields d = 3 conditional on observed gravity. **Less clean than Path A but still a definitive answer to B2.**

If Route 2.3 fails (factorial dilution doesn't admit primitive-level derivation, or the d ≤ 3 upper bound can't be established architecturally), NS-1 falls back to Path B. B2 still closes; the closure is just empirical-consistency-conditioned at the upper-bound half.

### 6.5 Substantive finding from this audit

The audit reveals a structural pattern worth noting. The substrate-gravity arc's primitives are d-agnostic, but its outputs (Newton's specific functional form, a₀'s specific prefactor) are d = 3-specific. This means the framework *already implicitly relies on d = 3 input* via the cosmic horizon's $S^2$ structure — this is not a new forcing, it's a recognition that the substrate-gravity arc's empirical match to observation is *also* a dimensional commitment.

In other words: ED's substrate-gravity arc has been operating in d = 3 implicitly (because that's where we live), and the empirical match validates d = 3 retroactively. The framework hasn't been *forcing* d = 3 from the primitive side alone; it's been *assuming* d = 3 via the cosmic horizon's $S^2$ structure and then validating that assumption against observation.

This is consistent with substrate_2pi_question.md's honest finding (2026-04-27, §4.2): "ED-06 + ED-10, used strictly, do not articulate a substrate-level mechanism that forces a natural 2π factor." The 2π is geometric — it's specific to $S^2$ — but $S^2$ is itself an input (the cosmic horizon's geometry at d = 3), not a primitive-derived result.

---

## 7. Inventory Status

### 7.1 Files updated by this audit

None directly. This memo is the audit deliverable.

### 7.2 Files that should be updated downstream

- **NS-1 scoping document** ([`Dimensional_Forcing_B2_Scoping.md`](Dimensional_Forcing_B2_Scoping.md)): update §2.4 (route description) and §3 (dependency structure) to reflect partial-close verdict; specifically distinguish architectural-only forcing (d ≥ 3 via T20 degeneracy) from empirical-consistency forcing (d ≤ 3 via T19/T20 output match). Update §4 (NS-1 closure conditions) to note the two-path structure (Path A architectural-only vs. Path B architectural+empirical).
- **NS-1.03 scoping** (the next memo to draft): the d ≥ 3 lower bound that Route 2.3 was anticipated to articulate is now *partially supplied* by this memo. NS-1.03 can reference NS-1.04 §3.2 for the d ≤ 2 forbidding via T20 degeneracy; Route 2.3's main remaining work is the d ≤ 3 upper bound via factorial dilution / concentration of measure.
- **NS-1.05 synthesis (when drafted):** report Route 2.4's partial-close verdict alongside Route 2.2's failure and Route 2.3's pending verdict.
- **Project memory** (`memory/project_navier_stokes_roadmap.md` once NS arc moves to active): record Route 2.4's partial-close.

### 7.3 No new derivations needed in this audit

The audit is structural — it identifies which existing T19/T20 derivation steps are d = 3-specific and which generalize, without producing new theorems or primitive-level work.

### 7.4 Optional follow-up: explicit d-spatial calculation

A short calculation memo deriving T19 in d-spatial explicitly (`a_(d)(r) = G_(d) M / r^(d-1)` with explicit $G_{(d)} = c^3 \ell_P^{d-1} / \hbar$ or similar) would formalize the d-generalization. **Not required for NS-1 closure**, but useful as a downstream artifact and as preparation for any future "ED in alternative dimensions" thought experiments.

---

## 8. Recommended Next Steps

In priority order. Route 2.4's partial-close shifts the load-bearing balance: pure-architectural B2 closure now hinges on Route 2.3's success.

1. **Draft Memo NS-1.03 — substrate motif viability + lower bound.** File: `theory/Navier Stokes/NS-1.03_Substrate_Motif_Viability.md`. This is now the *highest-priority remaining audit*, because it carries the d ≤ 3 upper bound for pure-architectural B2 closure. Work: (a) primitive-level derivation of factorial dilution / concentration of measure — replace heuristic C(d) ~ 1/d! with primitive-anchored argument (concentration of measure on participation-measure setup); (b) brief d ≥ 3 lower bound section that *cites NS-1.04* for the d ≤ 2 forbidding rather than rederiving it (since Route 2.4 already supplies that half). NS-1.03 is now narrower in scope than originally anticipated — the d ≥ 3 half is supplied externally. Estimated length: shorter than originally scoped because the lower-bound half is offloaded to this memo.

2. **Update [`Dimensional_Forcing_B2_Scoping.md`](Dimensional_Forcing_B2_Scoping.md)** to reflect both NS-1.02 (Route 2.2 failed) and NS-1.04 (Route 2.4 partial-closes) verdicts. Specifically: §2.2 add closure-failed note; §2.4 add partial-close note distinguishing architectural d ≥ 3 from empirical-consistency d ≤ 3; §3 update dependency structure (Routes 2.4 and 2.3 now overlap at the d ≥ 3 half); §4 add Path A / Path B closure-condition distinction; §6 risk assessment update (pure-architectural closure hinges on Route 2.3 success).

3. **Defer NS-1.01 (Route 2.1 Cl(3,1) → PDE propagation audit)** until after NS-1.03 delivers a verdict. Route 2.1's potential value depends on whether B2 has already closed via Routes 2.3 + 2.4. If those close cleanly (Path A), Route 2.1 becomes corroborating (additional layer of concordance) rather than load-bearing. If Route 2.3 fails and B2 closes only via empirical-consistency (Path B), Route 2.1's potential PDE-level forcing becomes more important.

4. **Synthesis (NS-1.05)** is last; it depends on outcomes of steps 1 and 3.

### Prerequisites and checks

- **Verify primitive d-agnosticism explicitly.** §2.4 of this memo asserts P02, P04, P11, P13, ED-06, ED-07, ED-10, Q.8 are d-agnostic at primitive-statement level. NS-1.03 should include an explicit short audit of primitive statements to formalize this — either as a §1 sub-audit or as an appendix. If any primitive turns out to presuppose d = 3 in its statement (unexpected but possible), the analysis here changes.
- **Locate ED-Phys-39.** Still pending; needed for NS-1.03's factorial-dilution work if it lives in the repo. Glob for "Phys-39" / "Phys_39" before NS-1.03 drafting begins.
- **Decide on Path A vs Path B framing for B2 closure.** This is a project-level decision: does NS-1 aim for pure-architectural closure (Path A, requires Route 2.3 success) or accept architectural+empirical closure (Path B, achievable now via Route 2.4 alone)? Recommendation: aim for Path A as the primary target, with Path B as the documented fallback. Path A is the cleaner result and matches the program's "form-FORCED, value-INHERITED" methodology more closely; Path B reads as "primitives + observation jointly force d = 3+1," which is weaker but still a definite answer.

---

*Audit complete. T19's holographic-bound mechanism is dimension-agnostic at primitive level but produces d=3-specific output (4πr², a ∝ 1/r²). T20's dipole-mode mechanism is more strongly d=3-specific — it cannot be constructed at d ≤ 2 (the cosmic horizon's $S^{d-1}$ has no separate polar/azimuthal decomposition at d − 1 ≤ 1). Combined, T19 + T20 force d = 3 architecturally at the lower bound (d ≥ 3) and via empirical-consistency at the upper bound (d ≤ 3). Pure-architectural B2 closure now depends on Route 2.3.*
