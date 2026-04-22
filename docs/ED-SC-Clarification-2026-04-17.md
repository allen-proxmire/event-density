# Decisive Clarification — ED-SC Hessian Definition

**Date:** 2026-04-17. **Status:** resolved in favour of Option 2 (field-space `∇²E`), subsequently refined to the motif-conditioned median form in ED-SC 2.0. Retained for audit record of the clarification step that unblocked the ED-SC cross-scale test program.

## The question

> **In ED-Arch-01 §5, when you write `κ∥ ≈ −1.3, κ⊥ ≈ +1.0` at the Scenario-D saddle peak, is that the Hessian of the phase-exit-step surface `f(n, σ)` evaluated at the saddle-ridge peak `(n=2.7, σ=0.0556)` in sweep-parameter space, the Hessian `∂²p/∂x_i∂x_j` of the final event-density field `p(x, y)` evaluated at a specific spatial stationary point on the 64×64 lattice, or a derived quantity that maps between these two Hessians?**

The question is binary-forcing: exactly one of `(1) parameter-space f(n, σ)`, `(2) field-space p(x, y)`, `(3) mapping` is the intended object. No fourth option is compatible with ED-Arch-01's published form.

## What each answer implies

**(1) Parameter-space Hessian of `f(n, σ)`.** ED-SC's cross-scale invariant is a statement about *observable surfaces*, not physical fields. Cross-scale comparisons require identifying analogous observable surfaces in each comparison system. Local Group mass sheet and Casimir cavity must have a specified parameter-space observable whose saddle Hessian was measured at `−1.3`. ED-Arch-02's "`H = ∇²E`" definition would need to be rewritten — it currently refers to the field, not an observable. Scenario-D canonical reproduction I ran *does* have a phase-exit-step saddle at `(2.7, 0.0556)`; that's consistent. But the cross-scale match claim becomes metaphorical until the observable surfaces in Local Group and Casimir are named explicitly.

**(2) Field-space Hessian of `p(x, y)`.** ED-Arch-02's definition applies as written. My canonical R2 run shows 28.4% of field-space Morse saddles fall in `[−1.5, −1.1]` at `(n*, σ*)`, with the distribution center at `−1.94` and 50% IQR `[−3.84, −1.34]`. The published `−1.3` is then either (i) a specific hand-picked saddle rather than the distribution peak, or (ii) the result of a different saddle-detection methodology than mine. In either case, the claim needs tightening: "a non-trivial fraction of field saddles cluster near −1.3" is weaker than "`κ∥/κ⊥ = −1.3` is the architectural invariant." Cross-scale tests then reduce to checking whether Local Group and Casimir have analogous field-space Hessian distributions — a concrete but less universal claim.

**(3) Mapping between the two.** ED-SC asserts that `H_param ↔ H_field` under some ED-specific transformation, and `−1.3` is the invariant of the mapped eigenvalue ratio. The mapping must be derived before any cross-scale test can be interpreted. No such mapping appears in ED-Arch-01 or ED-Arch-02. This answer implies the theoretical layer is incomplete.

## Recommended phrasing for escalation

A three-sentence message that forces the choice:

> I have reproduced Scenario D with the canonical `Run_Simulation.py` parameters (α=0.03, γ=0.5, dt=0.05, size=64, seed=77) and extracted two separate Hessian distributions at `(n*, σ*) = (2.7, 0.0556)`: the Hessian of the phase-exit-step surface `f(n, σ)` in the 4×4 sweep, and the per-saddle Hessian `∂²p/∂x_i∂x_j` of the final field `p(x, y)` at its Morse saddles. The second distribution has median `−1.94` with 28% of saddles in `[−1.5, −1.1]`, so the published `κ∥/κ⊥ ≈ −1.3` in ED-Arch-01 §5 does not match its central value.
>
> Which of these is the object you report as `−1.3`: (1) the parameter-space Hessian of `f(n, σ)` at the ridge peak, (2) the field-space Hessian at a specific spatial stationary point (and if so, which one), or (3) a derived invariant that maps between the two?

This formulation: (a) shows reproducibility groundwork done, (b) gives the numerical finding that creates the need to ask, (c) offers three pre-labeled answer options, (d) requests only the minimum information required to unblock the cross-scale testing program. No further action is needed from this side until the choice is returned.

---

## Resolution (2026-04-17)

Option (2) was chosen. The ED-SC architectural invariance claim refers to the field-space Hessian `∇²E`. Subsequent testing (motif-conditioned filter on the canonical Scenario-D field) then refined the form of the invariant: not the raw Morse-saddle distribution, but the median of a motif-conditioned subset. See `ED-SC-2.0.md` for the formal statement.
