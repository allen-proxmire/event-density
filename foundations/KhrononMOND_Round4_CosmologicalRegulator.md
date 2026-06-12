# Khronon–MOND — Round 4: The Cosmological Regulator and the SCBU Tie-In

**Foundations round — the merged thread from Round 3: the `A → 0` degeneracy and the cosmology connection are one question. Not a rule proposal, not a corpus edit, not a new primitive. Form-level; what is structural is derived, what is a family is labeled a family, and the one exciting numerical resonance (§5) is tiered as form-consistency, not a value derivation.**
**Crank rails (held, and this is the round they matter most):** the temptation is to *insert* a `θ`-dependent term into `W` to cure the degeneracy — that would be a retrofit. Instead: (i) establish what ED's structure says about the degenerate point itself; (ii) diagnose the degeneracy as a property of a *truncation*; (iii) prove the tested sector is *invariant* under the regulator choice, so no cure can be smuggled into the physics already checked. No MOND exponent from primitives; clusters/CMB still owed; GR-I untouched.

---

## 1. The merged question

Round 3's single soft spot: the pure-acceleration deep-IR function `W(A²)` degenerates at `A → 0` (vanishing stiffness, slowing modes, dropping strong-coupling scale). Round 3's hint: on the cosmological background the khronon congruence has `a = 0` **but `θ = 3H ≠ 0`** — the expansion is nonzero exactly where the acceleration vanishes. Round 4 asks whether the expansion sector lifts the degeneracy *without retrofit*, and what the khronon's cosmological face says to SCBU.

---

## 2. The degenerate point is not in ED's state space

The configuration at which the theory degenerates is `(A, θ) = (0, 0)`: zero acceleration *and* zero expansion — **exact Minkowski vacuum, eternal and inert**. The first structural observation is ED-native and requires no modification of anything:

> **ED has no Minkowski vacuum.** The khronon's background is cosmic time by construction (R11/R12 — the foliation *is* the Hubble flow); the substrate's tick does not halt and commitment does not cease (P13, P11). A background with `θ = 0` everywhere and forever — no expansion, no commitment flow — is not a configuration of the ED substrate. The physical background manifold is the `(A, θ)` half-space with `θ ∼ H > 0`; the degenerate point sits on its excluded boundary.

This is an observation about the *domain*, not a cure inserted into the *function*: nothing about `W` is changed. What it establishes is that the Round-3 degeneracy lives at a point ED's ontology never visits. The remaining question — the real one — is whether perturbations around the *physical* near-vacuum `(A → 0, θ = 3H)` are healthy. That depends on the IR sector's `θ`-structure, which is §3.

---

## 3. The truncation diagnosis, and the regulator family (labeled honestly)

Rounds 2–3 carried the deep-IR sector as a function of the acceleration alone, `W(A²)`. That was a **truncation**, not a derivation: the foliation EFT's invariants at this order are the congruence scalars — acceleration `a`, expansion `θ`, shear `σ` — and nothing in the substrate singles out `a` as the *only* argument of the non-analytic IR structure. (The truncation was the right tool for Rounds 2–3 because statics kill `θ` and `σ` anyway — see §4.) The general same-order IR sector is a function on the invariant space:

$$
W\big(A^2\big) \;\longrightarrow\; \mathcal{W}\big(A^2,\,\Theta\big), \qquad \Theta \equiv \frac{\theta}{3H_0},
$$

with the Round-2/3 results being `𝒲` evaluated on static slices (`Θ`'s static value is zero; see §4). On the *cosmological* point `(A, Θ) = (0, \sim 1)` the general function sits at a **generic point of its domain** — there is no structural reason for its quadratic forms to vanish or cancel there, so the generic member of this class is **non-degenerate at the physical near-vacuum**: gradient stiffness and a finite scalar speed at `A → 0` are supplied by the `Θ`-sector. The Round-3 degeneracy is thereby diagnosed: **it is a property of the pure-`A²` truncation evaluated at an unphysical point, not a property of the khronon EFT on ED's backgrounds.**

**The honest label.** The *form* of `𝒲`'s `Θ`-dependence is **not forced** — not by the substrate, not by matching Paper_030 (which constrains only the static/`A` sector). It is a **family**: the *regulator family*. Round 4 does not pick a member, and §4 shows why no member needs picking for anything so far tested.

---

## 4. The orthogonality result (the round's cleanest theorem)

Round 2 derived that static congruences have `θ = σ = 0` identically. Therefore:

> **Every `Θ`-dependent term in `𝒲` vanishes identically in the static sector.** The entire tested body of the arc — the modified Poisson equation, the GR limit, the Combination-Rule and BTFR embedding, the lensing pass, the AQUAL ellipticity, the screening and the Cassini constraints — is evaluated at `Θ = 0` and is **invariant under the choice of regulator**.

Consequences, both ways:

- **No leak-back:** the regulator cannot be tuned to "help" the tested sector — it is invisible there. The family is *sequestered* in the cosmological/dynamical sector. There is no channel through which choosing a regulator member retro-fits the galactic physics.
- **No protection either:** by the same token, the tested sector cannot vouch for the regulator. The family must face its own constraints — and it has real ones (§5–§6). The two sectors are independently falsifiable, which is the healthiest available structure.

---

## 5. The cosmological face: the SCBU tie-in, and one tiered resonance

On FRW, the khronon's active invariants are exactly the ones statics killed. Three connections, in increasing order of caution:

**(i) The `λθ²` sector renormalizes cosmological gravity (known-in-class).** On FRW, `λθ² ∼ λH²` enters the Friedmann equation as a rescaling of the effective cosmological Newton constant (`G_{\rm cosmo} ≠ G_N` by a `λ`-dependent factor) — a known khronometric effect, bounded by BBN's constraint on `G_{\rm cosmo}/G_N`. [I — class literature.] ED inherits the bound; nothing new.

**(ii) The SCBU statement in khronon language.** The khronon's background scale is `H₀`; its IR transition is `a₀ = cH₀/2π` (Paper_029); its horizon structure degenerates at `b → 0` (GR-I); and SCBU's unified boundary is `R_H = c/H₀`. In this construction these are not four scales that happen to agree — they are **one scale appearing in four roles**, because the khronon has exactly one background scale to offer. SCBU's "six projections of one boundary" acquires a dynamical carrier: *the boundary's field is the khronon.* [Structural identification at form level; no new SCBU content derived.]

**(iii) The vacuum-term resonance (tiered carefully — form-consistency, NOT a value derivation).** The IR sector evaluated at the cosmological point contributes a constant term to the Lagrangian of order `a₀² \mathcal{W}_0/16πG` — a **vacuum-energy contribution of order `ρ_Λ ∼ a₀²c²/G ∼ H₀²c²/G`**, i.e. of the order of the critical density and hence of the *observed* dark-energy density. The long-noticed numerical coincidence `Λ ∼ a₀²/c⁴ ∼ H₀²` here has a one-line structural reading: **the khronon's only scale is the cosmic rate, so its IR vacuum term can only be of that size.** Three honesty clamps: (a) the `O(1)` constant `𝒲₀` is not derived — this is an order-of-magnitude *form* statement, fully inside the corpus's value-inherited stance (the `Θ_ED ∼ 10^{-122}` think-don't-chase discipline is untouched: no value is chased, a scale is identified); (b) `Λ ∼ H₀²` with `H₀` part of `Λ`-determined cosmology is a *consistency relation*, not a prediction; (c) the corpus already carries a Λ-mechanism (the V1-backreaction reading, Paper_038.5) — the khronon vacuum term and the V1 reading are **two faces to be reconciled, not two competing claims**, and the reconciliation is flagged as open, not performed.

---

## 6. The Čerenkov check (channeled, not waved off)

Round 3 flagged gravitational-Čerenkov concern for slow scalar modes. With §3 in hand the check lands cleanly **in the regulator family's lap**: in voids and intergalactic space (`A ≪ a₀`, `Θ ∼ 1`), the scalar speed is set by the `Θ`-sector. The constraint is then:

> **Admissible regulator members must give `c_s` at the cosmological point high enough to evade gravitational-Čerenkov bounds from high-energy cosmic-ray propagation.** For the pure-`A²` truncation (no regulator), `c_s → 0` in voids and the check would *fail* — one more, independent indication that the truncation is unphysical at near-vacuum, i.e. that §3's diagnosis is right. For regulated members with `c_s ∼ O(1)` there, it passes.

Status: a real constraint, channeled into the family (where the BBN bound of §5(i) also lives); not a pass, not a kill — a **filter on the family**, which is exactly what an honest open sector should accumulate.

---

## 7. Round-4 Summary — and the arc's natural boundary

**Established this round:**
- The degenerate point `(A, θ) = (0, 0)` is **excluded from ED's state space** (no Minkowski vacuum; the substrate always ticks) — an ontology-level observation, not a cure. [Structural.]
- The Round-3 degeneracy is **diagnosed as a truncation artifact**: the pure-`A²` IR sector evaluated at an unphysical point; the generic same-order foliation EFT is non-degenerate at the physical near-vacuum `(0, Θ∼1)`. [Derived at EFT-generality level.]
- **The orthogonality theorem:** `Θ`-dependence vanishes identically in statics, so the entire tested sector (R2–R3) is invariant under the regulator choice — the family is sequestered, with no leak-back and no protection. [Derived; the round's cleanest result.]
- The khronon's cosmological face *is* the SCBU boundary's dynamical carrier — one scale (`H₀`) in four roles — and its IR vacuum term is naturally of order `H₀²` (the `Λ ∼ a₀²` coincidence as single-scale consistency; form-tier only; V1-backreaction reconciliation flagged open). [Structural identification + tiered resonance.]
- Čerenkov: channeled into the regulator family as a `c_s` filter; fails for the bare truncation (confirming the diagnosis), passable for regulated members. [Constraint, placed.]

**The regulator family itself:** open, sequestered, and now carrying three filters (BBN `G_{\rm cosmo}`, Čerenkov `c_s`, FRW stability). Pinning a member is **model-building** — the same epistemic boundary GR-Round-12 drew. **This round is the arc's natural foundations terminus**, with the same shape as the GR arc's: the *tested* half (statics: the modified Poisson, the Combination Rule, lensing, screening) is derived and passing; the *cosmological* half is an honest, constrained, sequestered family pointing directly at SCBU; and the primitives-level origin of the deep-IR branch remains deliberately guarded.

**Standing debts (unchanged, restated):** clusters and the CMB — and the flag now has an address: a khronometric `Θ`-sector active in cosmology is exactly where a dark-matter-*like* cosmological component would have to arise if this class is to address them (there is class literature in that direction); **noted as the direction, claimed as nothing.**

---

*Round-4 regulator analysis. The `A → 0` degeneracy is resolved in the only honest way available: not by inserting a cure, but by (i) noting the degenerate point is outside ED's state space (no Minkowski vacuum — the khronon's background is the Hubble flow and the substrate always ticks), (ii) diagnosing the degeneracy as an artifact of the pure-`A²` truncation, with the generic foliation EFT non-degenerate at the physical cosmological point, and (iii) proving the tested sector is invariant under the regulator choice (`θ ≡ 0` in statics) — the family is sequestered, unable to retrofit the galactic physics and unable to hide behind it. The khronon's cosmological face ties the arc to SCBU (one scale, four roles) and carries a vacuum term naturally of order `H₀²` — the `Λ ∼ a₀²` coincidence as single-scale consistency, form-tier only, with the V1-backreaction reconciliation flagged open. Čerenkov and BBN become filters on the family. The arc reaches its foundations terminus: tested half derived and passing; cosmological half an honest constrained family; origin question still guarded; clusters/CMB still owed, now with a named address.*
