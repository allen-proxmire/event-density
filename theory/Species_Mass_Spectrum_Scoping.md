# Species-Mass Spectrum Scoping Memo

**Date.** 2026-04-22.
**Scope.** One-afternoon feasibility scope. Not a theory, not a derivation, not a proposal for new axioms. The question: given ED's current architecture, is there a structural mechanism by which the framework could admit a *discrete* spectrum of stable species masses?
**Target.** Ratios like `m_p/m_e ≈ 1836` and `m_p/m_n ≈ 0.9986`. Explicitly avoided: reverse-engineering any specific number.
**Verdict.** Dead end at current ED state. Reasons in §6.

---

## 1. Problem Statement

### 1A. The precise question

Under ED's ontology and ED-Dimensional-01, is there a structural reason to expect a discrete spectrum of stable species masses, and if so, could that in principle explain observed ratios like `m_p/m_e ≈ 1836`?

### 1B. Two separable sub-questions

- **(a) Does a discrete spectrum exist at all?** — is there a mechanism internal to ED by which only certain `m`-values correspond to stable participation patterns, with all other `m`-values forbidden or unstable?
- **(b) Are the numerical values derivable?** — if (a) is true, does the mechanism *predict* specific numerical masses rather than admit them as additional parameters?

(a) is the "mechanism exists" question; (b) is the "mechanism is predictive" question. An affirmative (a) with a negative (b) would still be interesting but would not explain 1836. A negative (a) ends the program.

### 1C. Why the target number is already problematic

Even in the Standard Model, `m_p/m_e` is **not a fundamental parameter**. `m_e` comes from a Higgs Yukawa coupling; `m_p` is dominated by the QCD confinement scale `Λ_QCD ≈ 1 GeV` with only ~1% contribution from bare quark masses. The ratio 1836 is `(Λ_QCD × O(1) factor) / (y_e · v_Higgs)` — a composite of two unrelated scales at different sectors. **No existing framework predicts this ratio from first principles**, including string theory.

This matters because "deriving 1836" is poorly framed as a target even before we ask what ED could do. A better-framed target would be "derive a dimensionless mass ratio between two *elementary* species of the same type" — e.g., `m_μ/m_e ≈ 207` or `m_τ/m_μ ≈ 16.8`. These are closer to pure Yukawa ratios, less confounded by strong-coupling physics.

## 2. Relevant ED Structures

What ED actually has that could in principle bear on species discreteness.

### 2A. ED-Dimensional-01 per-species dictionary

For a quantum species of mass `m`:

$$
L_0 = \frac{\hbar}{mc}, \qquad T_0 = \frac{0.6\,\hbar}{mc^2}, \qquad D_{\rm phys} = \frac{\hbar}{2m}
$$

Mass `m` enters as an **external input** selecting a physical scale. The dictionary itself imposes no constraint on which `m` values are admissible — any `m > 0` gives a self-consistent scale.

### 2B. Cross-regime dimensional invariant

`D·T₀/L₀² = 0.3` across 61 orders of magnitude. Substituting the dictionary:

$$
\frac{D_{\rm phys}\,T_0}{L_0^2}
= \frac{(\hbar/2m)(0.6\,\hbar/mc^2)}{(\hbar/mc)^2}
= \frac{0.6\,\hbar^2 / (2m^2 c^2)}{\hbar^2/(m^2 c^2)}
= \frac{0.6}{2}
= 0.3.
$$

**This is an algebraic identity given the dictionary, not a constraint on `m`.** It holds trivially for any mass. This is worth flagging explicitly because the "invariant across 61 orders of magnitude" framing has sometimes been read as a structural constraint; at the species-mass level it is tautological.

### 2C. Canon P1–P7 (00.2)

- **P1 Operator Structure** `F[ρ] = M(ρ)∇²ρ + M′|∇ρ|² − P(ρ)` — single scalar field `ρ`. No species label, no multi-field structure.
- **P2 Channel Complementarity** `D + H = 1` — parameter, not mass-setting.
- **P3 Penalty Equilibrium** — unique globally-attracting `ρ*`. One fixed point per parameter set.
- **P4 Mobility Capacity Bound** — `ρ_max` is a constitutive parameter, not a dynamical output.
- **P5 Participation Feedback** — scalar `v` field, no species label.
- **P6 Damping Discriminant** — `D_crit(ζ)` scalar threshold.
- **P7 Nonlinear Triad Coupling** — architectural, not species-indexed.

**ED's canonical PDE has no species structure.** `ρ(x, t)` is a single real scalar. Any notion of "species" must be introduced at a higher level (e.g., interpreting stable localized patterns as particles) rather than being built into the PDE.

### 2D. ED-05 pre-PDE axioms

Non-negativity, null baseline, monotonicity, subadditivity. All statements about an ED functional on event configurations. No reference to mass or species.

### 2E. Sandbox Law XIII — Generative Closure

The `emergence-universe` sandbox claims exactly 10 sub-mechanism types, no 11th possible — a closure theorem at the discrete-particle update-rule level. This is **the strongest existing discreteness result in the ED corpus**. Two features to note:

- It is about mechanism *types* (update rules), not about particle masses.
- The count is 10, which does not correspond to any observed particle-count taxonomy (Standard Model has ≥17 elementary particles).

### 2F. Sandbox Law XIV — grid-dependent exponents

Collapse-time scaling `χ ∝ λ^p` with `p = −7/3` on canonical grid, `p = −2.81` on extended grid. Discrete exponents, but they are **grid-dependent**, so their discreteness comes from lattice choice, not architecture.

### 2G. Six structural analogues (Foundational Paper v2)

RC, Barenblatt PME, Stefan horizons, oscillatory horizons (negative), telegraph-PME, repulsion. These are **regimes** of the same PDE, not species. A stable localized pattern in one regime is architecturally distinct from a stable pattern in another, but that gives at most ~6 "kinds of stability," not a mass spectrum.

## 3. Candidate Mechanisms for Discreteness

Five candidates. Each is evaluated for (a) what ED primitive it depends on, (b) what would have to be true for it to work, and (c) whether it is operationally constructive or stipulative.

### 3A. Stable soliton spectrum of the nonlinear PDE

- **Statement** — the full nonlinear `F[ρ]` might admit a discrete set of stable localized standing-wave solutions with different characteristic sizes `L_n`. If `L_n ↔ L_0 = ℏ/(m_n c)`, the masses would be discrete.
- **Depends on** — Canon P1 (operator structure), P3 (penalty equilibrium), P4 (mobility bound).
- **What has to be true** — the PDE must support discrete isolated stable solutions, not a continuous family.
- **Assessment** — **fails at the PDE level**. The ED PDE is dissipative (Lyapunov-descending per derivation axiom D4). Dissipative scalar PDEs with a single globally-attracting equilibrium (Canon P3) *do not* support a discrete spectrum of isolated stable localized solutions — everything decays to `ρ*`. Stable patterns exist only transiently during relaxation, and their characteristic scales are set by initial conditions, not eigenvalues of an operator. This is the same reason the ED PDE does not have solitons in the Hamiltonian/NLS sense.
- **Verdict** — **fatal** under current Canon. Would require relaxing D4 (dissipation) or P3 (unique attractor), both of which are load-bearing.

### 3B. Topological invariants of participation patterns

- **Statement** — if participation patterns carry a topological charge (winding number, homotopy class, domain-wall count), the charge discretizes naturally, and mass could scale with the charge.
- **Depends on** — the codomain and symmetry structure of `ρ` and `v`.
- **What has to be true** — `ρ` or `v` must be valued in a space with nontrivial homotopy (e.g., `S¹`, `S²`) rather than `ℝ`.
- **Assessment** — **fails by construction**. `ρ: ℝ^d → ℝ` is a real scalar field. `π_n(ℝ) = 0` for all `n`. There are no nontrivial topological invariants. The participation field `v` is similarly a real scalar. Domain walls between `ρ*` and a boundary value exist but admit only a `ℤ_2` "side" charge, not a mass-indexed ladder.
- **Verdict** — **fatal** without promoting `ρ` to a multi-component or complex field, which would violate derivation axiom D5 (single scalar field).

### 3C. Eigenvalue discretization from bounded participation-space

- **Statement** — if the system is posed on a finite domain or with restrictive boundary conditions, the spectrum of allowed `k`-modes discretizes (`k_n = nπ/L` etc.), and `L_0` tied to the lowest mode gives discrete masses.
- **Depends on** — the domain geometry and BCs, not the ED architecture itself.
- **What has to be true** — the domain size `L` must itself be architecturally fixed (not a free parameter).
- **Assessment** — **circular**. The discretization comes from the boundary, and the boundary is not itself determined by ED. To use this mechanism you would need an ED axiom specifying the domain size, which does not exist. If you stipulate `L = L_0` you are inserting the answer by hand.
- **Verdict** — **stipulative**; does not count as an ED-derived discreteness mechanism.

### 3D. Capacity-bound-induced discrete levels

- **Statement** — Canon P4 sets `M(ρ_max) = 0`. If stable participation patterns must fit within `[0, ρ_max]` and satisfy some integer-valued counting condition (e.g., number of nodes, number of `ρ*`-crossings), the spectrum of admissible patterns could discretize.
- **Depends on** — P4 and a node-counting principle not currently in the Canon.
- **What has to be true** — the node-counting principle must follow from existing axioms or be derived from a new one.
- **Assessment** — **underdetermined**. In linear Sturm–Liouville problems node-counting arises from oscillation theorems on a fixed interval; in ED's nonlinear dissipative setting, no analogous theorem exists. One could construct a variational functional with integer-valued minima by hand, but that imports discreteness rather than deriving it.
- **Verdict** — **fixable in principle but speculative**; would require new axiom material not currently present.

### 3E. Sandbox Generative Closure extension

- **Statement** — Law XIII gives 10 sub-mechanism types. If each type corresponds to one species of particle, the spectrum is trivially discrete at 10 elements.
- **Depends on** — the sandbox discrete-particle framework, not the continuum PDE.
- **What has to be true** — the mapping "mechanism type ↔ particle species" must be physically defensible, and the count must match observed particles.
- **Assessment** — **fails at the count level**. Ten does not match the Standard Model (17 elementary particles, or 12–25 depending on how gauge bosons and supersymmetric partners are counted). Even if the mapping were defensible, the number is wrong. Also, mechanism types in the sandbox are update rules governing how patterns evolve, which is conceptually a very different object from a particle's mass — more like a "kind of interaction" than a "kind of particle."
- **Verdict** — **wrong target**; Law XIII is a real discreteness result but it is discreteness of *dynamics*, not of *species masses*.

## 4. Toy Models

Two explicit toy models to check whether discreteness is *natural* in ED-like settings or *imposed*.

### 4A. Toy 1 — 1D Standing Participation Modes

- **Setup** — linearised ED system on `x ∈ [0, L]` with Neumann BCs. Allowed modes: `k_n = nπ/L` for `n = 0, 1, 2, …`.
- **Per-mode damping** — from the D_crit memo, mode `n` is underdamped iff `(D − ζ)² < 4(1 − D)` at `ε_n = M₀(nπ/L)² + P₀`. For large `n`, `ε_n` grows, and `D_crit → 0`: high-`n` modes are always underdamped.
- **Stable-mode count** — **infinite**. There is no upper cutoff on `n`, so "stable" modes form a countably infinite ladder. This is discrete in the ordinal sense but not in the species sense — we have an unbounded tower, not a closed list.
- **Mass assignment** — if `m_n ~ ℏ/(c·L_n)` with `L_n ~ L/n`, then `m_n ∝ n`. Infinite ladder of masses with integer spacing.
- **Interpretation** — **discreteness is present but unphysical**. The ladder is an artifact of the finite domain; take `L → ∞` and the spectrum becomes continuous. The ladder spacing is set by `L`, which has no architectural origin. If you want `m_1/m_0 = 1836`, you just choose `L` to make it so — pure fitting.
- **Verdict** — **does not demonstrate natural discreteness**. Shows that finite-box BC discreteness is available but stipulative.

### 4B. Toy 2 — Nonlinear Breather on the Full PDE

- **Setup** — posit (per mechanism 3A) a discrete family of radially-symmetric standing-pulse solutions `ρ_n(r, t)` of the full `F[ρ]` with periodic time structure `ρ_n(r, t) = ρ_n(r, t + 2π/ω_n)`.
- **Existence** — dissipative nonlinear scalar PDEs generically admit at most a continuous family of breathers in narrow parameter windows, or none at all. Famous example: the φ⁴ breather is non-existent as a true periodic solution; only approximate quasi-breathers exist. For ED's dissipative PDE, analogous negative results are expected.
- **Numerical probe (scope-level)** — if one ran `edsim` with a single localized pulse and monitored amplitude, the pulse would relax monotonically to `ρ*`. Confirmed by existing analogue-5 simulation runs (the telegraph-PME runs show decaying oscillation, not sustained breathers).
- **Mass assignment** — moot; no stable solutions exist.
- **Verdict** — **mechanism absent**; no discrete stable patterns to count.

**Both toys confirm the §3 assessment**: discreteness either requires stipulating a discretizing structure (finite box, integer counting) or is absent in the PDE itself. **Nothing in ED's architecture naturally produces a discrete mass spectrum.**

## 5. Constraints and Failure Modes

| Failure mode | Status |
|:---|:---|
| ρ is a single real scalar → no topological charges | **Fatal under Canon D5** (single scalar field). Fixing requires multi-component fields, which would break the derivation axiom. |
| PDE is dissipative with unique attractor → no isolated stable localized solutions | **Fatal under D4 + P3**. Fixing requires relaxing dissipation or multiplicity of attractors. |
| D·T₀/L₀² = 0.3 is a tautology → no mass constraint from the cross-regime invariant | **Fatal**; not fixable, the algebra is identity. |
| No node-counting / integer-valued functional exists in Canon | **Fixable in principle** — would need a new axiom. But no such axiom has been proposed or motivated. |
| Sandbox Law XIII gives 10 mechanism types, not species | **Wrong target**; Law XIII is about dynamics classification, not mass. |
| m_p is QCD-emergent, not a fundamental parameter → even fixing (a) wouldn't directly address the 1836 ratio | **Fatal for the specific 1836 goal**; would need to reproduce QCD-like confinement inside ED. |

## 6. Assessment — Real Direction or Dead End?

**Dead end at current ED state.** Four independent reasons:

1. **ED has no species structure.** Canonical PDE is a single-scalar equation. There is no field-theoretic place for species to live without a structural change (multi-component `ρ`, complex `v`, etc.) that would break derivation axioms D5 and related.
2. **The invariant D·T₀/L₀² = 0.3 imposes no constraint on `m`.** It's an algebraic identity given the per-species dictionary. Any `m > 0` trivially satisfies it. Reading this invariant as a species-constraint is a mistake.
3. **No ED axiom or principle picks out discrete mass values.** None of P1–P7, none of the derivation axioms, none of the ED-05 pre-PDE axioms say anything about mass. Mass enters only at the ED-Dimensional-01 dictionary layer as a regime-selecting external parameter.
4. **The target ratio 1836 is not even a fundamental parameter in the Standard Model.** Even granting a hypothetical ED mass-setting mechanism, 1836 involves both QCD confinement (proton) and electroweak Yukawa (electron) — two different physics sectors. ED would have to simultaneously reproduce both, a much larger program than "constrain species masses."

**The strongest existing ED discreteness result (Sandbox Law XIII, exactly 10 sub-mechanism types)** is real but applies to dynamics classification, not particle masses. It does not translate into a species spectrum.

**Structurally supported vs numerology line.** Structurally supported: the claim that ED's current architecture does *not* constrain species masses. Numerology: any attempt to derive `1836` from combinations of `0.3`, `1/4`, etc. within current ED — these numbers are architectural but carry no species content.

## 7. Next Steps

### 7A. If we accept the dead-end verdict (recommended)

- **Add one line to ED-Dimensional-01 and to Orientation §5.8**: "Mass `m` enters the quantum-regime dictionary as an external input labelling a species. The current ED framework does not constrain which masses are admissible; species selection is not an ED-level question." This is the honest framing — it closes a latent overclaim and matches what the architecture actually does.
- **Drop the species-mass direction from the whimsical-leverage list.** Reallocate the afternoon budget to the C7 residual scan on the AFM pilot frame (from two turns back) or to the cosmic-void ED-XX test.

### 7B. If we want to pursue it anyway

Two concrete follow-up tasks that would be non-trivial but well-defined:

- **Formalize Sandbox Law XIII as a species-count theorem.** Not a mass-setting exercise. The claim would be: "ED admits exactly N distinct dynamical regimes" for some specific N, derivable from the update-rule closure argument. This is tractable and might bear on species *taxonomy* (how many kinds of stable patterns) without addressing numerical masses. Low-risk, single-afternoon scope follow-up.
- **Add a multi-component participation field and ask whether ED-like axioms force a discrete spectrum.** This is a genuinely new theory direction. Would require a new paper, an extension of the Canon, and several weeks of work. Not recommended unless an independent motivation appears.

**Do not attempt to derive 1836 directly.** Under current ED structure, any such attempt would be numerology — fitting a target by combining `0.3`, `π`, canon parameters, etc. until the product approximates 1836. This would damage the program's empirical credibility more than it could gain in speculative reach.

---

*Scoping memo v1.0, 2026-04-22. Budget: one afternoon. Verdict: dead end. Memo archived for reference in case the mechanism question surfaces independently in future ED-I work.*
