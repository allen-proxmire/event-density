# Phase-3 GR — Round 11: Khronon Parameters and the Observational Confrontation

**Foundations → phenomenology. Not a rule proposal, not a corpus edit, not a new primitive.**
Round 10 placed ED's gravity in the khronometric (Hořava-IR) class — Einstein's tensor sector plus a preferred-foliation scalar. Round 11 asks the quantitative question that decides viability: what are the khronon/Lorentz-violation parameters, and does ED survive **GW170817** and the **preferred-frame PPN** bounds? The result is one **structurally forced** pass and one **genuinely open** risk.
**Crank rail:** the temptation here is "ED passes every test." It does **not** claim that. Separate what ED's structure *forces* (computable now) from what needs the still-only-partially-specified dynamical rule `F` (not computable now). Name the wall.

---

## 1. The parameter landscape and the bounds

A khronometric / hypersurface-orthogonal Einstein-aether theory has a small set of dimensionless coefficients (Einstein-aether `c₁…c₄`; equivalently khronometric `α, β, λ`). They fix the observables:

- **Tensor (spin-2) GW speed:** `c_T² = 1/(1 − c₁ − c₃)`. **GW170817** forces `|c_T/c − 1| ≲ 10⁻¹⁵`, i.e. `c₁ + c₃ ≈ 0` — a razor-thin constraint that, in *generic* Einstein-aether, is a fine-tuning.
- **Scalar (khronon) mode speed:** a different combination; subject to stability and gravi-Čerenkov bounds.
- **Preferred-frame PPN parameters** `α₁, α₂`: functions of the `cᵢ`, bounded by solar-system and pulsar data to `α₁ ≲ 10⁻⁴`, `α₂ ≲ 10⁻⁷`.

For ED, the `cᵢ` are set by the **linearized dynamical-bandwidth rule** `δḃ_ij = F'[δb]`. Since `F` is only *partially* forced (R2/R3 fix its shape; R5 fixes the band↔edge map; the exact coefficients remain a residual family), **the numerical `cᵢ` are not yet computable from first principles.** What *is* computable is which constraints ED's structure forces independent of `F` — and there is a decisive one.

## 2. GW170817 is passed structurally — ED has a *single causal cone*

This is the round's main result, and it does not depend on `F`. In generic Einstein-aether the aether is an **independent field with its own kinetic term**, so its modes have their own light cone and `c_T = c` requires tuning `c₁+c₃=0`. **ED is different by construction:**

- ED has **one** maximal signal speed — the **bandwidth-limit speed** (the finite-width kernel, T8/N1), which bounds *every* substrate process (P05 adjacency transport is the only transport).
- **Light** = a matter front, propagated by P05 adjacency, saturating that cone (R8: "the cone = the bandwidth-limit speed").
- **Tensor gravitational waves** = perturbations `δb_ij` of the bandwidth field, *also* propagated by P05 adjacency — there is no separate "aether kinetics." A massless `δb_ij` mode saturates the **same** cone.

Both massless sectors propagate through the *same* substrate by the *same* mechanism at the *same* maximal speed, so

> **`c_T = c_light` — structurally, not by tuning.** ED is the khronometric theory whose khronon is the substrate's own foliation, sharing the matter cone; the GW170817 condition `c₁+c₃ ≈ 0` is **automatic**, not fine-tuned.

This is a genuine, distinctive prediction: the constraint that squeezes generic Hořava/Einstein-aether after GW170817 is, for ED, a structural identity. (It likely also forces the **scalar** mode toward the same cone — an even stronger, possibly over-constraining feature flagged in §4.)

## 3. The preferred-frame (PPN) test — the real open risk, with a natural suppressor

The `α₁, α₂` parameters measure **preferred-frame coupling** — how much a system's velocity relative to the preferred frame affects local gravity. Unlike the GW speed, this is a **coupling strength**, and it *is* `F`-dependent. ED has a natural suppression mechanism but not a guaranteed pass:

- **The preferred frame is the substrate frame — i.e. the cosmological / CMB rest frame, naturally** (the ED substrate *is* the universe's rest frame; there is no other candidate). Preferred-frame effects are then suppressed by the local velocity relative to the CMB (`v/c ~ 10⁻³` for the solar system).
- But the *magnitude* of `α₁, α₂` is `(coupling) × (v/c)²`-type, and the coupling comes from `F`. So whether `α₁ ≲ 10⁻⁴`, `α₂ ≲ 10⁻⁷` hold depends on the khronon coupling strength, which is **not yet computed.**

**Honest status:** this is the tightest test ED faces and the place it could fail. The cosmic-frame alignment is a real, favorable structural feature (it is *why* a preferred-frame theory can be viable at all), but it does not by itself guarantee the bounds — the coupling must also be small, and that is an `F`-computation, not yet done. **The PPN preferred-frame parameters are ED-gravity's genuine falsification target.**

## 4. The honest wall, and a possible over-constraint

The numerical `cᵢ` (hence `α₁, α₂`, the scalar speed, stability) require the **explicit linearized `F`**, which the arc has forced only in shape. So R11 cannot deliver the numbers — it delivers the *structure*: one forced pass (`c_T=c`), one suppressed-but-open risk (PPN). Two honest cautions:

- **Possible over-constraint.** If *every* substrate mode shares the single cone (§2), the **scalar** khronon mode may be forced to `c_scalar = c` as well. Khronometric consistency (stability, no gravi-Čerenkov) places specific demands on the scalar speed; a substrate that forces all speeds equal is *very* constrained and might conflict with those demands. This is a real internal-consistency check ED must pass — it could be a strength (maximal predictivity) or a problem (over-rigidity).
- **The `F` residual is now the whole game.** Everything quantitative funnels through the one remaining freedom — the exact coefficients of the dynamical-bandwidth rule. Pinning `F` (the last underdetermination, R3's residual family minus what R5 already forced) is the concrete next computation; it converts "structurally plausible" into "viable or ruled out."

## 5. A simulable target (flagged, not built)

The `c_T = c` claim is directly testable in simulation: perturb `b_ij`, watch the tensor perturbation propagate, and compare its speed to a matter front's. The structural argument predicts they are equal. I do **not** build it here, because a faithful version needs the specified `F` (an unspecified `F` would test my choice, not ED) — but it is a concrete, near-term check once `F` is pinned, and a clean way to confirm or break the §2 result.

## 6. Structural vs contingent

| Item | Verdict |
|---|---|
| single causal cone (one substrate speed) | **structural** (P05 / T8-N1) |
| `c_T = c` (GW170817 passed) | **forced** (single cone; not `F`-dependent) |
| `c₁ + c₃ ≈ 0` automatic | **forced** (vs fine-tuned in generic Einstein-aether) |
| preferred frame = CMB rest frame | **structural** (substrate = universe frame) |
| preferred-frame suppression by `v/c` | **structural**, but magnitude **`F`-dependent** |
| `α₁, α₂` numerical values (PPN) | **contingent — open** (need explicit `F`) — the falsification target |
| scalar mode speed / stability | **open** — possible over-constraint if forced to `c` |
| any structural block | **none** |

## 7. Verdict

**ED-khronometric is observationally plausible, with one robust pass and one open risk — and is now a concrete, falsifiable program rather than a foundational question.** The headline is structural and `F`-independent: because ED has a **single causal cone** (one substrate, one bandwidth-limit speed, one transport mechanism), the tensor gravitational wave and light share that speed automatically, so **`c_T = c` and ED satisfies GW170817 without tuning** — the very constraint that fine-tunes generic Hořava/Einstein-aether is, for ED, an identity. The genuine open test is the **preferred-frame PPN sector** (`α₁, α₂`): ED has a natural suppressor (its preferred frame *is* the cosmological rest frame, so effects scale with the small local `v/c` relative to the CMB), but the magnitude depends on the khronon coupling, which requires the explicit linearized dynamical-bandwidth rule `F` — not yet pinned. So R11 does **not** claim ED passes every test; it shows ED passes the headline GW test structurally, has a natural reason to survive the preferred-frame test, and reduces the remaining viability question to **one computation: specify `F`, extract `α₁, α₂`, confront PPN.** That computation is the falsification target — the point where ED-gravity becomes confirmable or refutable. No corpus edits, no new primitives, no structural block.

## 8. Round-12+ questions

1. **Pin `F` (the last freedom).** Fix the exact coefficients of the dynamical-bandwidth rule within the admissible family; this is now the bottleneck for all numbers.
2. **Extract `α₁, α₂`** from the linearized `F`; confront the PPN bounds — the falsification target.
3. **Scalar mode.** Compute its speed and stability; is it forced to `c` (over-constraint) and does that conflict with khronometric consistency?
4. **The GW-speed simulation.** Once `F` is pinned, perturb `b_ij` and confirm `c_T = c` numerically (§5).
5. **Cosmology.** A preferred frame is natural in cosmology; connect to the ED-SC / SCBU dark-energy sector (khronometric gravity has a distinctive cosmological history).

---

*Round-11 phenomenology. Verdict: ED's single causal cone (one substrate speed, P05 transport for both matter fronts and `δb` geometry perturbations) **forces `c_T = c`**, so ED satisfies **GW170817 structurally** — the post-2017 constraint `c₁+c₃≈0` is an identity for ED, not a fine-tuning, distinguishing it from generic Hořava/Einstein-aether. The **preferred-frame PPN sector** (`α₁, α₂`) is the genuine open test: ED's preferred frame is naturally the cosmological/CMB rest frame (a real suppressor), but the magnitude needs the explicit linearized rule `F`, only partially forced. So R11 delivers one structural pass and one suppressed-but-unconfirmed risk, reducing viability to a single computation — specify `F`, extract `α₁,α₂`, confront PPN — the falsification target. A possible over-constraint (all modes forced to one cone) is flagged. No corpus edits, no new primitives. ED-gravity is now a concrete, falsifiable theory: GW-clean by construction, with its fate resting on the preferred-frame coupling.*
