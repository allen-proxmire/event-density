# ED-10 Geometry-Emergence Scoping Memo

**Date.** 2026-04-22.
**Scope.** One-afternoon feasibility scope. Not a theory, not a derivation, not a proposal for new axioms. The question: given ED's current architecture, can the ED-10 interpretive claim — *"Einstein's equations are a large-scale summary of ED gradients"* — be promoted from analogy to an actual derivation?
**Target.** Einstein field equations `G_μν + Λ g_μν = 8πG T_μν`, or at minimum a linearised weak-field sector (`□ h̄_μν = −16πG T_μν`), from the ED canonical PDE.
**Verdict.** Not achievable as a *direct* derivation under current axioms. A restricted analogue-gravity result (emergent effective metric for small ED fluctuations in a regime where Lorentz invariance appears *accidentally*) is plausible but would be an *analogy-grade* result, not a proof that GR is the large-scale summary of ED. See §8.

---

## 1. Problem Statement

### 1A. The precise question

ED-10 currently sits in the **Interpretations** stratum as a heuristic identification: Einstein's equations describe the large-scale gradient response of whatever the fundamental substrate is, and ED posits that substrate is event density `ρ`. The open question is whether that heuristic can be made into one of the following:

- **(i) Direct derivation.** Starting from `∂_t ρ = D·F[ρ] + H·v` with `F[ρ] = M(ρ)∇²ρ + M'(ρ)|∇ρ|² − P(ρ)`, derive that some functional `G[ρ]` of `ρ` and its gradients satisfies (or coarse-grains to) `G_μν = 8πG T_μν` on an emergent manifold whose metric is constructed from `ρ`.
- **(ii) Effective/analogue derivation.** Show that linearised fluctuations about a background `ρ_0` propagate on an emergent effective metric `g_μν^{\rm eff}[ρ_0]`, in the style of acoustic metrics (Unruh 1981, Barceló–Liberati–Visser 2005) — *without* recovering dynamics for that metric.
- **(iii) Thermodynamic/entropic derivation.** In the style of Jacobson 1995 / Padmanabhan / Verlinde, show that Einstein's equations emerge as an equation of state or force law when ED is summed over microstates, *without* constructing `g_μν` from `ρ` at all.

(i) is the strongest; (iii) is the weakest. (ii) gives a kinematic metric but not the dynamical Einstein equation.

### 1B. Why the ED-10 claim is hard to cash out

Einstein's equations are a **rank-2 tensor equation** on a **4-dimensional pseudo-Riemannian manifold** with **diffeomorphism invariance** and **Lorentz local symmetry**, derivable from an action whose leading term is `√(−g) R`. ED's canonical PDE is a **scalar** dissipative-advective equation on a **substrate treated as Euclidean** with **no built-in Lorentz symmetry** and **no covariant action**. Every one of those mismatches is a non-trivial bridge.

---

## 2. Relevant ED Structures

What ED actually has that could bear on geometric emergence.

### 2A. Canonical PDE

`∂_t ρ = D·F[ρ] + H·v`, `F[ρ] = M(ρ)∇²ρ + M'(ρ)|∇ρ|² − P(ρ)`. A scalar `ρ(x,t)` on a fixed substrate `x ∈ Ω ⊂ ℝ^d`. The operators `∇²`, `∇`, `∂_t` are those of the ambient (Euclidean) geometry — ED does **not** construct its own geometry. This is the first and largest problem (§7A).

### 2B. Mobility `M(ρ)` and penalty `P(ρ)`

Nonlinear `M(ρ)` and `P(ρ)` are the only handles for self-interaction. `M(ρ)|∇ρ|²` is the P7 triad term. No gauge structure, no fibre bundle.

### 2C. Damping split `D + H = 1` and P6 underdamping

The discriminant `(D − ζ)² < 4(1 − D)` picks out a reversible-wave-like regime (propagating fluctuations) from a purely dissipative regime. The reversible sector is the *only* place where anything GR-like could survive, because GR is time-reversal-symmetric at the field-equation level.

### 2D. Dimensional dictionary (ED-Dimensional-01)

`L_0 = ℏ/(mc)`, `T_0 = 0.6 ℏ/(mc²)`, so `c_0 = L_0/T_0 ≈ (1/0.6) c`. ED has a natural signal speed `c_0` set by the dictionary, not by symmetry. GR's `c` is the *only* invariant speed; ED's `c_0` is a parameter of the substrate. §3A–§3B return to this.

### 2E. ED-SC 2.0 cross-scale invariance

The motif-conditioned Hessian exponent `r* = −1.304` is the sharpest structural fact ED currently has. It is not, at present, a geometric statement — it is a statistical property of field configurations. Whether it admits a geometric reinterpretation is open.

### 2F. What ED *does not* have

- No metric tensor.
- No manifold other than the ambient substrate.
- No Lorentz invariance (the wave speed is set by `M(ρ_0), D`, not by a symmetry).
- No diffeomorphism invariance.
- No covariant action.
- No fermions, no gauge bosons, no species label at all (single scalar field).
- No torsion, no connection, no curvature — even as composites of `ρ`.

Every one of these is a structure GR *has* and ED would need to *build*.

---

## 3. Candidate Mappings

Six plausible routes to geometric emergence. Each is evaluated on its own terms.

### 3A. Acoustic metric from linearised ED (Unruh-style)

Linearise `ρ = ρ_0(x) + δρ(x,t)` about a slowly-varying background. For reversible-sector parameters (`D − ζ`)² approaching `4(1 − D)`, the linearised equation is wave-like. Generically, for a scalar PDE of the form `(A^{μν} ∂_μ ∂_ν) δρ = 0` where `A^{μν}` depends on the background, `δρ` sees an effective metric `g^{μν}_{\rm eff} ∝ A^{μν}`. This is the Unruh mechanism.

**What this buys you.** A kinematic metric `g^{\rm eff}_{μν}[ρ_0]` on which small ED fluctuations propagate. Causal structure (lightcones) emerges as the level sets of `g_{μν}^{\rm eff}`.

**What it does *not* buy you.**

- The metric is not dynamical in the GR sense — `g^{\rm eff}` is slaved to `ρ_0`, which evolves via the ED PDE, *not* via Einstein's equations. There is no reason `ρ_0` would satisfy anything like `R_{μν} − ½ g_{μν} R = 8πG T_{μν}`.
- The emergent metric is only Lorentzian in a narrow parameter window; generically it is Riemannian or degenerate.
- Analogue gravity has, after 40 years, not produced a single example where the background *also* satisfies Einstein's equations as a consequence of the microdynamics. ED would have to be the first.

**Status for ED-10.** Plausible as a limited (ii)-grade result. Does **not** justify the ED-10 claim in its strong form.

### 3B. Conformal factor mapping (ρ as scalar curvature source)

Propose `g_{μν}[ρ] = f(ρ) η_{μν}` for some function `f`. Then the scalar curvature `R[g]` is a specific function of `∂f/∂ρ · ∇ρ` and `f'' · (∇ρ)²`. Match `R[g] = κ · (\text{something in ED})`.

**Obstacle.** This is a one-parameter family of metrics (conformally flat), which cannot support Einstein's equations for a generic stress-energy — conformally flat metrics have `C_{μνρσ} = 0`, making them trivial in 4D for gravitational radiation. You lose half of GR.

**Status.** Insufficient: can at best match the Ricci scalar part, not the full tensor equation.

### 3C. ρ as a dilaton-like scalar coupled to an emergent metric

A richer version of §3B: both a metric `g` and `ρ` live on the emergent manifold, with `ρ` playing the role of a dilaton. The Einstein equations pick up a `∂_μ ρ ∂_ν ρ` source.

**Obstacle.** You have to *add* the metric as independent structure. ED provides only `ρ`. So this is not a derivation *from* ED — it is GR + ED-scalar-matter *on top of* GR. The ED-10 claim requires `g` to *come from* `ρ`, not coexist with it.

**Status.** Doesn't satisfy the ED-10 framing.

### 3D. Entropic / thermodynamic (Jacobson 1995)

Jacobson's argument: *if* local Rindler observers see a Clausius-type relation `δQ = T δS` with `S` proportional to horizon area, *then* the Einstein equations follow as an equation of state. No derivation of `g_{μν}` from substrate required.

**What this would require from ED.**

1. A notion of local Rindler wedges in the ED substrate.
2. A thermodynamic identification of energy flux `δQ` with an ED quantity.
3. An area-entropy relation for ED ensembles — i.e., that the entropy of an ED configuration bounded by a 2-surface scales with the area of that surface, with some coefficient playing the role of `1/(4G)`.

(1) requires emergent Lorentz symmetry (→ §3A). (3) is the hard one: ED currently has no horizon/area-law structure because it has no lightcones and no boundary entropy analysis.

**Status.** Most promising of the (iii)-grade options, but contingent on first solving the §3A emergent-Lorentz problem and then separately establishing an area law. Two independent hard steps. Not achievable without substantial new axioms or derivations.

### 3E. Verlinde-style entropic force

Treat gravity as an entropic force arising from information on holographic screens. This requires a notion of bits on screens and a temperature — both of which presuppose a causal/horizon structure ED does not have.

**Status.** Same obstacles as §3D plus additional ones (holographic bound, screen construction). Further from ED than §3D.

### 3F. Sakharov induced gravity

Treat `√(−g) R` as the low-energy effective action that arises from integrating out high-frequency modes of some underlying field on a background `g`. The gravitational coupling `G` comes out as a loop integral `Λ²/(16π)` with cutoff `Λ`.

**Obstacle.** Sakharov's construction *presupposes a metric* and asks where the Einstein-Hilbert term comes from as an induced effect. It does not construct the metric from nothing. To make this ED-grade you would first need the §3A acoustic-metric step.

**Status.** Could be a *second-stage* argument once §3A is done, for determining whether the emergent metric acquires Einstein dynamics as a loop effect. Order-of-operations: (§3A) → (§3F). Both are hard.

---

## 4. Variational Principle Analysis

### 4A. Is the ED PDE derivable from a covariant action?

The canonical ED PDE `∂_t ρ = D·F[ρ] + H·v` contains a dissipative term `D·F[ρ]` that is **not** the Euler-Lagrange equation of any Lagrangian `L(ρ, ∂ρ)` in the standard sense. Dissipative PDEs generically require a doubled-field (Schwinger-Keldysh / Martin-Siggia-Rose) formulation to admit an action principle, and the resulting action is **not** covariant in the GR sense — it distinguishes a time direction explicitly.

### 4B. Consequence

Any geometric emergence route that tries to match ED's action to Einstein-Hilbert `∫ √(−g) R d^4x` has to first manufacture covariance. That is the same problem as §3A emergent Lorentz — you don't get it for free from a dissipative scalar PDE.

### 4C. Reversible sector only

If you restrict to the reversible sector (`H → 0` or the underdamped wave-like regime where dissipation is effectively small over the relevant timescale), the remaining dynamics *can* be cast as a Lagrangian field theory — but only as a Euclidean scalar field theory, still not covariant in the Lorentzian sense.

**Bottom line.** No covariant action ⇒ no clean path to Einstein-Hilbert ⇒ any derivation must go through an *emergent* covariance argument (§3A), which is itself unresolved.

---

## 5. Large-Scale / Coarse-Graining Arguments

### 5A. What coarse-graining *can* give you

Coarse-graining a microscopic scalar PDE over many correlation lengths gives you:

- Effective transport coefficients (renormalised `D`, renormalised `M(ρ)`).
- Hydrodynamic modes (density waves, if the reversible sector is active).
- A `c_0`-lightcone for those waves in the linearised regime.

That is essentially the analogue-gravity story. It reproduces §3A, no more.

### 5B. What coarse-graining *cannot* give you without new input

- Tensor field `g_{μν}` with `d(d+1)/2` independent components from a scalar `ρ` with 1 component. You are strictly missing degrees of freedom.
- Nontrivial Weyl curvature (gravitational waves, black-hole tidal structure) from a conformally-flat ansatz.
- Dynamical backreaction of `g` on matter — the ED metric is slaved to `ρ` and does not evolve by its own equation.

### 5C. The degrees-of-freedom obstruction

In 4D, the metric has 10 components, of which 2 are physical after gauge fixing. ED has 1 scalar field. **You cannot map 1 → 2 without additional structure** (e.g., adding vector/tensor fields, or postulating that `ρ` at multiple scales supplies independent DOFs — neither of which is in current ED).

This is structural, not technical. It is the same obstruction that prevents BEC analogue-gravity from reproducing full GR — it has only longitudinal phonons and cannot source transverse-traceless modes.

---

## 6. Six-Analogue Sequence (Historical Context)

ED-10 would be following a well-travelled road:

| # | Program | Year | What it derives | What it assumes | Outcome |
|---|---------|------|-----------------|-----------------|---------|
| 1 | Unruh acoustic metric | 1981 | Lightcones for fluctuations | Background flow | Kinematic only |
| 2 | Sakharov induced gravity | 1968 | `G` from loops | Metric, matter fields | Partial |
| 3 | BEC analogue gravity | 2000s | Effective `g_{μν}` for phonons | BEC background | Kinematic only |
| 4 | Jacobson thermodynamic | 1995 | Einstein eqs as EoS | Local Rindler + area law | Derivation (given assumptions) |
| 5 | Padmanabhan emergent | 2002– | Einstein-Hilbert from surface term | Horizon thermodynamics | Suggestive |
| 6 | Verlinde entropic | 2010 | Newtonian gravity from bits | Holographic screen | Contested |

None of these programs, 45+ years in, has produced a *completed* derivation of full GR dynamics from a pre-geometric substrate. Jacobson gets the closest but takes local Rindler structure as input. ED would be attempting to surpass all of them. **This is prior evidence that the task is very hard, not that it is impossible — but any optimistic scoping has to account for the base rate.**

---

## 7. Obstacles and Failure Modes

### 7A. Substrate geometry is assumed, not derived

`∇²`, `∇`, `∂_t` all presuppose an ambient Euclidean (`ℝ^d × ℝ`) substrate. ED does not construct the substrate from `ρ`; the substrate is the stage on which `ρ` lives. Any claim that *the emergent geometry is GR* therefore competes with the fact that **ED already has a geometry, and it is not GR**. To make ED-10 work, you must either:

- (α) Argue that the ambient Euclidean geometry is itself emergent from a deeper pre-geometric ED layer — this is not in ED currently and would require a new axiomatic layer (call it ED-00).
- (β) Accept that the "Einstein's equations" being derived are *effective* and live on the ambient substrate — in which case ED-10 is really a claim about effective fields on a Euclidean background, not a claim about the origin of spacetime geometry.

(β) is honest but demotes ED-10 to a claim about gravitational phenomena rather than about GR itself.

### 7B. No Lorentz symmetry

ED's signal speed `c_0` is a parameter, not an invariant. Different choices of `M(ρ_0)` give different `c_0`. To recover relativistic causality you need `c_0` to become universal — the same for *every* ED excitation — which requires a selection mechanism that ED currently lacks.

### 7C. Dissipation

GR is time-reversal symmetric at the field-equation level (the arrow of time comes from cosmology + boundary conditions). ED is dissipative through `D·F[ρ]`. Any geometric emergence has to either confine itself to the `(1 − D)`-weighted reversible sector or explain why dissipation is invisible at the emergent scale.

### 7D. Scalar vs tensor

The degrees-of-freedom count (§5C) is a hard obstruction to recovering full GR from a single `ρ`.

### 7E. Background independence

GR's central conceptual achievement is background independence — the metric is a dynamical field, not a backdrop. ED has a backdrop (the substrate) and a field (`ρ`) on it. Any ED-derived metric inherits its dynamics from `ρ`'s dynamics, and `ρ`'s equation is set *with respect to the backdrop*. This is the deepest conceptual tension, and it is not resolved by any of the analogue-gravity programs.

### 7F. Risk of motivated reasoning

"Large-scale summary of ED gradients" is poetically suggestive and may *read* as a derivation without containing the substantive content. A rigorous scoping has to distinguish:

- **(R1)** `∇ρ`-terms in ED's PDE formally resemble gradient terms in a scalar stress-energy → true but trivial, any field theory has this.
- **(R2)** `∇ρ`-terms coarse-grain to something satisfying Einstein's equations → would be substantive; is not shown.
- **(R3)** The emergent metric from ED fluctuations coincides with the physical spacetime metric → requires §3A plus universality of `c_0` plus tensor DOFs, none of which ED currently has.

ED-10 in its current interpretive form is an (R1)-style claim. The task being scoped here is whether it can be promoted to (R2) or (R3).

---

## 8. Assessment

### 8A. Strongest honest statement ED can support today

*"The gradient structure of the ED canonical PDE is consistent with there being an emergent kinematic metric in the linearised-fluctuation regime, analogous to the acoustic metric of Unruh 1981. The ED framework does not currently derive Einstein's field equations for this metric; it derives only scalar wave propagation on a fluctuation-dependent effective metric."*

This is an (ii)-grade analogue-gravity claim. It is honest, defensible, and within ED's current axiomatic reach.

### 8B. What ED-10 *cannot* support today

The strong claim "Einstein's equations are a large-scale summary of ED gradients" implies (R3) — that the emergent metric satisfies GR dynamics. There is no route to this in current ED without:

1. An emergent Lorentz mechanism (universal `c_0`).
2. Extra degrees of freedom beyond scalar `ρ` (tensor structure).
3. Either a covariant action for ED or an entropic/thermodynamic argument with an ED area law.

Each of these is a research program, not a derivation.

### 8C. Recommended rewording of ED-10

Consider the following replacement for the ED-10 stratum statement:

> **ED-10 (weak form, honest).** "In the linearised fluctuation regime of ED, small disturbances about a slowly-varying background `ρ_0(x)` propagate on an effective metric `g^{\rm eff}_{μν}[ρ_0]`, in the same kinematic sense as the acoustic metric of Unruh 1981. Whether this effective metric's dynamics coincide with Einstein's equations is an open question — answering it affirmatively would require an emergent Lorentz mechanism, additional tensor degrees of freedom, and either a covariant action or an entropic/thermodynamic derivation, none of which are currently in the ED axiomatic stack."

This is (ii)-grade, honest, and preserves the conceptual direction of ED-10 without overclaiming.

### 8D. Verdict on the original task

**Direct (i)-grade derivation of Einstein's equations from ED: not achievable under current axioms.** The obstructions in §7 are structural, not technical. A (ii)-grade analogue-gravity result is achievable and worth pursuing *if* geometric emergence is a priority thread. A (iii)-grade entropic derivation is contingent on first establishing §3A and an area law — two separate new programs.

---

## 9. Research Plan (If Pursued)

If the decision is to promote ED-10 from interpretation to derivation, the following ordered work packages would be needed. *None of this is recommended as urgent work; it is provided so the scope is visible.*

### Stage 1 — Linearised effective metric (3–6 weeks)

- Expand `ρ = ρ_0(x) + δρ(x,t)` and derive the linearised equation for `δρ` about a background `ρ_0(x)` with slowly varying gradients.
- Cast in the form `(A^{μν}[ρ_0] ∂_μ ∂_ν + B^μ[ρ_0] ∂_μ + C[ρ_0]) δρ = 0`.
- Read off `g^{\rm eff}_{μν}[ρ_0]` and determine under what conditions on `(D, ζ, M, P, H)` it is Lorentzian vs Riemannian vs degenerate.
- **Output.** A theory memo `theory/ED_Effective_Metric_v0.1.md` with the explicit form of `g^{\rm eff}`.
- **Pass criterion.** `g^{\rm eff}` exists and is Lorentzian on a non-empty parameter region of the P6 underdamped sector.

### Stage 2 — Universality of `c_0` (open-ended)

- Test whether `c_0` is parameter-set or symmetry-enforced: do different perturbations about the same `ρ_0` all propagate with the same speed?
- Look for a selection mechanism: does the reversible sector's renormalisation group flow drive `M(ρ_0) D` to a fixed point?
- **Output.** A scoping memo on whether emergent Lorentz is possible.
- **Pass criterion.** A concrete mechanism that makes `c_0` universal, not a parameter choice.
- **Risk.** High chance this cannot be done without new axioms. If so, stop here and accept (ii)-grade ED-10.

### Stage 3 — Tensor degrees of freedom (blocked on Stage 2)

- Either: enlarge ED with a second field (e.g., a vector `A_μ` or symmetric tensor `h_{μν}`) whose dynamics are coupled to `ρ` — this is **adding axioms**, not deriving.
- Or: identify `ρ` at multiple scales as independent DOFs (via the ED-SC 2.0 motif structure) and check whether the resulting multi-scale field has enough DOF to source tensor modes. This is speculative.
- **Output.** A proposal for the minimal extension of ED that can carry tensor modes.
- **Pass criterion.** Tensor-mode count matches GR's TT sector.
- **Risk.** If (a) is chosen, ED-10 becomes a statement about ED *plus* an extension, not about ED itself.

### Stage 4 — Dynamical equations for `g^{\rm eff}` (blocked on Stage 3)

- Either: Jacobson-style argument, requires ED area law (separate thread).
- Or: Sakharov-style induced gravity, requires integrating out high-frequency `ρ`-modes and checking whether a `√(−g) R` term is generated with positive `G`.
- **Output.** A derivation (or failure report) for whether `g^{\rm eff}` satisfies Einstein's equations at leading order in coarse-graining.
- **Pass criterion.** `R_{μν} − ½ g_{μν} R = 8πG T_{μν}^{\rm eff}` with `G` computed from ED parameters.
- **Risk.** No existing emergence program has completed this step. Very high risk.

### Stage 5 — Validation (blocked on Stage 4)

- Match emergent `G` against observed Newton constant.
- Check weak-field limit against post-Newtonian tests.
- Check gravitational-wave propagation speed = `c` (LIGO-constrained to `|c_{GW}/c − 1| < 10^{−15}`).
- **Risk.** Without a mechanism for `c_0 = c` exactly, this fails by 15 orders of magnitude.

### Stage 6 — Prediction (optional, blocked on Stage 5)

- Identify a regime where ED predicts a deviation from GR (e.g., at scales where coarse-graining breaks down).
- Propose an observational test.

### Total effort estimate

Stage 1: achievable. Stages 2–6: each individually comparable to a multi-year program. Total: not a one-researcher task, not a one-year task. **If ED-10 is to be kept as a testable claim, it should be re-scoped to Stage 1 only, in the honest (ii)-grade form recommended in §8C.**

---

## 10. Deliverable

- **This memo.** `theory/ED_Geometry_Emergence_Scoping.md` — scoping study, not a derivation.
- **Recommended action.** Keep ED-10 in Interpretations. If promoting, rewrite per §8C (weak form, honest) and queue Stage 1 only.
- **Not recommended.** Treat ED-10 in its current strong form as a testable prediction of ED. It is a conceptual placeholder, not a result.

---

## 11. Related Memos

- `theory/Architectural_Canon.md` — P1–P7 the emergence would have to respect.
- `theory/ED-Dimensional-01-Ext.md` — dictionary + `c_0 = L_0/T_0 ≈ c/0.6` tension flagged in §2D.
- `theory/D_crit_Resolution_Memo.md` — P6 underdamped sector definition (relevant to §3A Stage 1 parameter window).
- `theory/Species_Mass_Spectrum_Scoping.md` — prior scoping memo, same honest format.

---

**Status.** Scoping only. No new axioms, no new predictions, no updates to Canon. Consult before proceeding with any Stage-1 work.
