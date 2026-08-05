# Scoping Note — The Binding-Mass Scale Is Mechanism-Grounded but Scale-Inherited

**Series:** Event Density (ED) Generative Papers — substrate-evaluation / mass arc. **Scoping note** (records a finding + the open target; not a result paper).

**Status:** Read-first grounded on `Paper_MassWithoutMass_BindingInertia` (the V5 binding-mass mechanism) and `Paper_090_V5Kernel` (the V5 reach/memory scales). Honest tiers below.

**Author:** Allen Proxmire

**Date:** August 2026

---

## Purpose

Step 1 of the mass-scale question. ED grounds a native mechanism for the dominant (composite/binding) form of mass: a lone front is massless (ballistic-or-extinct, `c`-moving), and V5's finite-reach retarded *attraction* confines massless fronts into a bound composite with genuine inertia (`Paper_MassWithoutMass`, Measured / V5-conditional). That paper deliberately produces **no mass value** and leaves the scale open. This note asks: does the substrate **fix** the binding-mass scale, or **inherit** it? The honest answer is *inherit* — and the value of the note is that it locates the one well-posed derivation that would change that.

## 1. The kinematics are clean (and standard)

A bound state of massless-moving constituents confined to a region of linear size `L` has rest energy of order the confinement mode, so its rest mass is

  **m_bind ≈ ħc / L,  with  L ≈ ℓ_V5** (the V5 confinement reach), up to an O(1), constituent-number-dependent factor.

Sanity check: `ħc ≈ 200 MeV·fm`, so `L ≈ 1 fm → m_bind ≈ 200 MeV`, a few of which is the nucleon. So *if* the V5 reach sits near a femtometer, ED's binding mechanism produces nucleon-scale mass. This step is textbook "box of light" kinematics, not an ED-specific result; ED's content is the *mechanism* that makes the box (V5 binding of `c`-moving fronts), not this relation.

## 2. The scale-setting reach is inherited, not derived

The magnitude lives entirely in `ℓ_V5`. `Paper_090_V5Kernel` is explicit that this is a **value-layer inherited** quantity, not a substrate prediction:

- §3.1: `ℓ_V5` is "V5-characteristic spatial scale (regime-dependent; **inherited from ℓ_ED at substrate scale**, renormalized in coarse-grained regimes via DCGT)."
- §3.3 / §7.1–7.3: the V5 memory times `τ_V5` are "inherited from value-layer empirical content, not predicted by the substrate"; **"no coupling constants or masses are derived."** (For the black-hole regime, `τ_V5^BH` is *chosen* to match `ℓ_P/c`, not derived.)

So ED converts a reach into a mass **kinematically** but does not produce the reach.

## 3. The Planck-mass problem (why this matters)

At the *substrate* level, `ℓ_V5 = ℓ_ED = ℓ_P` (the grain). Taken literally, that gives

  **m_bind ≈ ħc / ℓ_P = M_Planck ≈ 10¹⁹ GeV** — nineteen orders too heavy.

A composite bound at the grain scale is a Planck-mass lump. To get a *nucleon* (~1 GeV) instead, the reach must be enormously larger than the grain: `ℓ_V5 ~ 1 fm ≈ 10²⁰ ℓ_P`. **ED inherits that hugeness; it does not derive it.** This is structurally the QCD situation — `Λ_QCD` sits ~19 orders below the Planck scale — except QCD *earns* the separation through dimensional transmutation (logarithmic running of the coupling; confinement kicks in exponentially far below the UV scale). ED currently has **no transmutation mechanism**; the reach is put in by hand.

## 4. Honest tiers

| Element | Tier | Source |
|---|---|---|
| Binding **mechanism** (massless fronts → inertial composite) | **Measured, V5-conditional** | `Paper_MassWithoutMass` §3–4 |
| Kinematic scaling `m ≈ ħc/L` | standard physics (not ED-specific) | box-of-light / confinement mode |
| Scale-setting reach `ℓ_V5` (hence the mass magnitude) | **Inherited** | `Paper_090` §3.1, §3.3, §7.1–7.3 |
| Why `ℓ_V5 ≫ ℓ_P` (the transmutation) | **Attempted 2026-08; NOT AVAILABLE — no marginal coupling; contingent on the OPEN Route-B beta-function derivation** | §5.1 |

Net: ED's binding mass is **mechanism-grounded and kinematic-scaling-clean, but scale-inherited.** Together with the fundamental (Yukawa) masses — inherited, with a six-mechanism refutation of the ratios (`Paper_113` §3.5) — the *entire* ED mass sector bottoms out in the same inherited quantities: the grain `ℓ_P` and the V5 reach/times.

## 5. The one well-posed open target

The corpus states the missing step in its own words: `ℓ_V5` is *"renormalized in coarse-grained regimes via DCGT"* (`Paper_090` §3.1) — but **that renormalization is never computed**. The ED analog of dimensional transmutation is therefore well-posed for the first time in the mass sector:

> **Compute the flow of the V5 reach `ℓ_V5` under DCGT, from `ℓ_P` at the substrate to the confinement scale in the composite (hadronic) regime, and determine whether the flow *forces* `ℓ_V5 ≫ ℓ_P` (an emergent, transmutation-type separation) or merely reproduces whatever reach is put in.**

- If the DCGT running generates a large, exponential-type separation on its own (as QCD's beta function does), ED would **derive** the scale of the dominant form of mass in ordinary matter from the grain. That would be the first genuine mass-scale result in the corpus.
- If it does not, the binding-mass scale stays **honestly inherited**, and this note is the record of why.

This is the first place in the entire mass sector where a derivation is *well-posed rather than refuted* (contrast the fundamental-mass **ratios**, which carry a standing six-mechanism refutation). It is also a serious computation (a coarse-graining flow), not a one-session stab, and it may simply confirm "inherited."

## 5.1 The transmutation was attempted (2026-08) and is NOT available with current machinery

A read-first survey of ED's coarse-graining and scale-flow machinery — DCGT (`Paper_073`); the RG papers (`Paper_097` three-regime, `Paper_ED_SC_4_2`/`4_6` cross-scale); the V5-reach source (`Paper_PhaseCoherence_P12Coh`, `Paper_V5AttractiveSign_P12Coh`); and the `a₀` non-running result (`Paper_037`) — shows the DCGT-running derivation **cannot be executed**, because the three ingredients a QCD-style exponential hierarchy requires are absent or too weak:

1. **DCGT is a single substrate→continuum step, not an iterable RG flow.** It is explicitly placed "one structural level below RG" (`Paper_073` Preamble 5); it produces the continuum *form* by moment expansion and *matches* the scale/coefficient to data (`Paper_073` §4.4, tier **I**). There is no semigroup to compose, so ℓ_V5 cannot be "run."
2. **No derived logarithmically-running dimensionless coupling** — the exact QCD ingredient (β(g) ~ −b g³ ⟹ Λ ~ Λ_UV·e^(−1/bg²)). ED asserts a three-/four-regime RG (`Paper_097`, `Paper_ED_SC_4_6`) but its generator β(K) is inherited by canon-internal matching, not derived (`Paper_ED_SC_4_2` §3.4, **"Route B" OPEN**); the sole dimensionless RG number (the 0.6 transition exponent) is postulated; and `a₀` is explicitly shown *not* to RG-run (`Paper_037` §2.5).
3. **The one disorder-set length that could be large is power-law, not exponential.** ℓ_V5 is the P05-holonomy correlation length ξ ~ 1/var(A) (`Paper_PhaseCoherence` §5.3): it grows only *inverse-linearly* as disorder weakens, the weak-disorder endpoint degenerates into a forbidden crystal (long-range order), and its value is inherited (only *finiteness* is forced).

**Why the distinction is decisive.** A power-law relation (ξ ~ 1/var(A)) merely *relocates* the hierarchy — reaching ℓ_V5/ℓ_P ~ 10²⁰ would require var(A) ~ 10⁻²⁰, itself an unexplained small input. Only an *exponential* relation (QCD's) *explains* a hierarchy, by turning a modest input into a huge output. ED has no exponential channel.

**The structural reason, stated plainly.** Every scale ED sets is one of three kinds: the grain `ℓ_P` (primitive); a boundary condition (`H₀ → a₀ = cH₀/2π`, `Λ` — inherited, horizon-tied, `Paper_037`); or a power-law disorder correlation length (`ℓ_V5`). **None is a marginal, logarithmically-running coupling** — the thing that makes QCD transmute. ED, as built, is a grain-plus-boundary-conditions-plus-power-law-lengths theory, not a log-running theory, so it *inherits* its hierarchies rather than generating them. A genuine transmutation would first require deriving an ED beta-function generator (the open "Route B" of `Paper_ED_SC_4_2`) — a deep, unattempted program, not a next step.

## Bottom line

The binding-mass scale is **inherited, not transmuted**, and we now know *why*: ED lacks the marginal, logarithmically-running coupling that dimensional transmutation requires; its scales are grain, boundary-condition, or power-law disorder lengths, none of which can *generate* (as opposed to *relocate*) a hierarchy. This is **Sabine-consistent** — the Standard Model inherits `Λ_QCD` too; inheriting a scale is not a defect. So the mass sector's honest close is: **mechanism grounded (binding), scale inherited (like the SM's), and the only route to deriving it (the ED beta-function generator, Route B) is a separate deep program, not reachable from here.**
