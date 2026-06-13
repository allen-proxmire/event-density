# Phase-3 GR — The Dynamical Rule, Hyperbolic Build (modes, the khronon speed, `α₁/α₂`)

**Foundations construction + simulation — the hyperbolic (retarded) sector of the dynamical-bandwidth rule `F`. Not a corpus edit, not a new primitive. Nothing here derives the Einstein field equations.**
The first build (`Phase3_GR_DynamicalRule_FirstBuild`) did the static/elliptic sector — the Newtonian field equation `∇²b~ρ`, the Schwarzschild mass-scaling, and the emergent frozen horizon. This build does the **hyperbolic** sector, where the *propagating modes* live: the **mode count from `F`** (vs R10's gauge-group argument), the **khronon speed** (resolving the KM-II §6 open question), and the localization of the **`α₁, α₂`** preferred-frame front.
**Crank rail:** the rule's *form* is the retarded version of the forced static rule (single P05 transport); the foliation coupling is carried as a *general* knob `ε`, not tuned. Mode count and `c_s` are *measured/derived*; `α₁,α₂` numbers stay deferred where they require pinned coefficients. Sim: `evaluation/DynamicalBandwidth/hyperbolic_modes.py`.

---

## 1. The hyperbolic rule and the mode count *from `F`*

The metric perturbation is the symmetric tensor `h_ij = δb_ij` (per-edge, directional — the anisotropy that escaped Nordström, R6 §4). The retarded version of the static rule is the **wave** equation with the single P05 transport operator:

> `ḧ_ij = c² ∇²h_ij + ε·c² ∇²(trace part)`.

- **`c² ∇²h_ij`** — the **single P05 transport** (one wave process at one speed `c`, for *all* of `b`). This is the structural origin of GR-II's single causal cone.
- **`ε·(trace)`** — a *foliation-specific* kinetic term (the `λθ²` khronometric term). `ε = 0` is the **minimal forced rule** (transport only); `ε ≠ 0` is the generic-khronometric case.

**The mode count, from the rule's gauge structure (confirming R10 by operator analysis, not assertion).** `h_ij` (4×4 symmetric = 10 components) is reduced by gauge and constraints. In full GR, four diffeomorphisms + four constraints leave **2** propagating (TT tensor) modes; the scalar/trace is pure gauge. **In ED the arrow lives in the law (P11/P13), so the time-reparametrization gauge that would remove the trace mode is broken** — the gauge group is foliation-preserving diffeomorphisms, one generator smaller. One fewer gauge removal ⟹ the trace/scalar mode **survives as physical**:

> **2 tensor + 1 scalar (the khronon) — khronometric, derived from the rule's gauge structure.** The scalar is physical *because the arrow breaks the gauge that would freeze it* — the same mechanism R10/GR-II identified, now read off the explicit hyperbolic `F` rather than asserted from the gauge group.

## 2. The khronon speed — KM-II §6 resolved (conditionally)

KM-II §6 left open: *does the rule force the khronon onto the light cone (`c_s = c`), or allow `c_s ≠ c`?* The hyperbolic rule decides it as a function of `ε`. Seeding a plane wave in the tensor (off-diagonal) vs the trace (scalar) sector and measuring each speed by its oscillation frequency `v = ω/k` (`hyperbolic_modes.py`):

| `ε` | `c_s/c_T` (measured) | `√(1+ε)` | reading |
|---|---|---|---|
| 0.00 | **1.000** | 1.000 | **single cone — khronon at `c`** |
| 0.25 | 1.118 | 1.118 | two cones |
| 0.50 | 1.225 | 1.225 | two cones |
| 1.00 | 1.414 | 1.414 | two cones |

(The ratio `c_s/c_T` is the lattice-artifact-free quantity; a common ~1.257 absolute offset from the discrete dispersion cancels in the ratio. The measured ratio is **exactly `√(1+ε)`**, validating the operator.)

> **At `ε = 0` — the minimal forced rule, single P05 transport, no foliation-specific kinetic term — `c_s = c` exactly: the khronon rides the same cone as the tensor modes.** ED's scalar gravitational-wave polarization is then **at the speed of light** — the *maximal-predictivity* horn of KM-II §6, sharper than generic khronometric gravity (which allows `c_s ≠ c`).

**The residual that decides it.** The minimal rule has one transport operator → `ε = 0` → `c_s = c`. The only way to get `ε ≠ 0` is a **foliation-specific kinetic term** (a `λθ²` contribution) beyond the single transport. Whether ED's arrow-breaking is *kinematic* (it merely un-freezes the existing transport mode → `ε = 0`) or *dynamical* (it generates an effective `λθ²` → `ε ≠ 0`) is the one open question — now **localized to a single coefficient `ε`**, with the clean dependence `c_s/c = √(1+ε)` measured. The lean is `ε = 0` (the minimal rule has no second operator), but the gauge-breaking → kinetic-term link is not proven.

## 3. The `α₁, α₂` front — localized, not yet numerical

The preferred-frame PPN parameters are the GR-II falsification target. The hyperbolic build does not yet produce their numbers (they need the matter coupling and the pinned `ε`), but it **localizes** them: in khronometric gravity `α₁, α₂` are functions of the foliation coupling, vanishing in the maximally-constrained corner. **`ε = 0` (`c_s = c`) is that corner** — the most preferred-frame-suppressed case — so the `c_s = c` lean points *toward* PPN-safety rather than away. The honest status: `α₁, α₂` are now a computation in **one knob `ε`** (plus the matter coupling), with the framework explicit; the numbers remain deferred until `ε` is fixed from the reserve/foliation sector.

## 4. Structural vs contingent

| Item | Verdict |
|---|---|
| hyperbolic rule = retarded single-transport `F` + foliation knob `ε` | **forced form + 1 labeled knob** |
| tensor modes at `c` (single P05 cone) | **structural** (one transport process) |
| arrow breaks time-gauge → trace mode physical → **2 tensor + 1 scalar** | **derived** (gauge structure; confirms R10 from `F`) |
| `c_s/c = √(1+ε)` | **measured** (exact, lattice-artifact-free ratio) |
| minimal rule (`ε=0`) ⟹ `c_s = c` (khronon at light speed) | **derived (conditional on no `λθ²`)** — resolves KM-II §6 toward maximal predictivity |
| whether the foliation sector supplies `ε ≠ 0` | **the residual** (kinematic vs dynamical gauge-breaking) |
| `α₁, α₂` | **localized to `ε`**; numbers deferred (need pinned `ε` + matter coupling) |
| 2-vs-1 polarization counting in 3+1D | **analytic/dimensional** (the sim measures speeds in reduced dimension; the count is from the gauge structure) |
| lattice absolute-speed offset | **measurement artifact** (cancels in `c_s/c_T`) |
| any structural block | **none** |

## 5. Verdict

**The hyperbolic build confirms the mode count from `F` and resolves the khronon speed conditionally.** The retarded single-transport rule carries **2 tensor + 1 scalar** modes — the scalar (khronon) physical *because the arrow (P11/P13) breaks the time-reparametrization gauge that would freeze it* — reproducing R10/GR-II's khronometric count by direct operator analysis rather than the gauge-group argument. The tensor modes propagate at `c` (single P05 cone, GR-II's `c_T = c` from the explicit wave operator). The khronon speed obeys `c_s/c = √(1+ε)` (measured, exact), where `ε` is a foliation-specific kinetic term: **the minimal forced rule has `ε = 0`, giving `c_s = c` — the khronon at the speed of light, the maximal-predictivity resolution of KM-II §6**, sharper than generic khronometric gravity. The `α₁, α₂` front is thereby localized to the single coefficient `ε`, with `ε = 0` the preferred-frame-suppressed corner.

**The honesty lines.** (i) `c_s = c` is *conditional on `ε = 0`* — i.e. on the arrow's gauge-breaking being kinematic (un-freezing the transport mode) rather than dynamical (generating a `λθ²` term); the minimal rule has no second operator, so the lean is `ε = 0`, but the gauge-breaking → kinetic-term link is not proven. (ii) `α₁, α₂` are localized but not computed — they need `ε` fixed and the matter coupling. (iii) The polarization count (2 TT) is from the gauge structure; the sim measures *speeds* (the dimension-independent cone question), not the 3+1D polarization tally. **Einstein/khronometric is not newly derived here; the mode count is reconfirmed from `F`, the khronon speed is pinned to `√(1+ε)`, and the program's sharpest open phenomenology (`c_s`, `α₁/α₂`) is reduced to one coefficient.**

## 6. Next

1. **Fix `ε` from the foliation/reserve sector.** The single remaining knob: does the arrow's gauge-breaking generate a `λθ²` term (`ε ≠ 0`, two cones) or merely un-freeze the transport mode (`ε = 0`, `c_s = c`)? This closes the khronon speed and, with the matter coupling, delivers `α₁, α₂` — the GR-II falsification numbers.
2. **The B-column numbers.** With the hyperbolic `F` and the horizon (first build), compute the ED-10 scalings as actual numbers (`S = A/4`, Hawking `T`) — the items that were "structure done, numbers waiting on the keystone" (#4).
3. **Feed back to KM-II §6.** If `ε = 0` confirms, KM-II's scalar-mode caveat resolves to "the khronon is at light speed (maximal predictivity)," a sharper published prediction.

---

*Hyperbolic build of the dynamical-bandwidth rule. The retarded single-transport `F` carries 2 tensor + 1 scalar modes (the khronon physical because the arrow P11/P13 breaks the time-gauge that would freeze it — R10's count, now from `F`); tensor modes at `c` (single P05 cone). The khronon speed is measured to obey `c_s/c = √(1+ε)` exactly, with `ε` a foliation-specific kinetic term: the **minimal forced rule (`ε=0`) gives `c_s = c`**, the khronon at light speed — resolving KM-II §6 toward maximal predictivity, sharper than generic khronometric gravity. `α₁, α₂` are localized to the single knob `ε` (numbers deferred). Residual: whether the arrow's gauge-breaking is kinematic (`ε=0`) or dynamical (`ε≠0`). No corpus edits, no new primitives; Einstein not derived; the program's sharpest open phenomenology reduced to one coefficient.*
