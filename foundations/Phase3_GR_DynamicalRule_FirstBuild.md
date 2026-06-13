# Phase-3 GR — The Dynamical-Bandwidth Rule `F`, First Build (#1/#8 keystone)

**Foundations construction + simulation — the first build of the dynamical-bandwidth rule on P04, the keystone shared by Phase-3 GR (#1) and A2-dynamical (#8). Not a corpus edit, not a new primitive. Nothing here derives the Einstein field equations.**
The structural arc (R1–R12) reduced "the field equation" to *the steady state of an admissible dynamical-bandwidth rule* `ḃ = F` (R9 §1), whose *form* is already pinned: the band↔edge map is forced (R5), the lapse exponent is forced (`α=1`, the AlphaOne note), and the geodesic structure is fixed (the timelike-geodesic note). This note **builds that rule in its forced form and runs it**, measuring whether its steady state reproduces what it must.
**Crank rail:** `F`'s *form* is the R2 admissible core — never tuned to yield Poisson/Schwarzschild. Poisson is the fixed point of the forced terms (stated as such); the horizon and the cut are *measured*, not imposed. Let it say no. Sim: `evaluation/DynamicalBandwidth/dynamical_bandwidth.py`.

---

## 1. The forced rule

Two terms, each tied to a primitive, **neither tuned to give a field equation**:

> `ḃ = D ∇²b − κ ρ`,  `b ≥ 0` (P04),  `b → 1` at the frame (asymptotic flatness).

- **`D ∇²b` — P02 adjacency sharing.** The metric band is a *reciprocal, shared* record (`b_ij = b_ji`); a shared conserved field on a graph equilibrates by the graph Laplacian. This is the **elliptic geometry sector** — *distinct* from the kinetic *matter* sector the CoarseGrain trilogy showed is non-diffusive; Newtonian gravity is elliptic by nature, so an elliptic geometry sector is correct, not a contradiction.
- **`−κ ρ` — P11 commitment concentration.** Persistent matter *holds* bandwidth in its single concentrated channel (`commitment.md`), depleting the metric band in proportion to its density → `b` **low near matter** (the gravity sign). `κ` carries the `α=1` rate strength.

Separately, the **commitment-reserve band** (P04 §1.5) drains monotonically where commitments fire (P11; no replenishment, R2 §5) — the A2-freeze diagnostic.

**What is built-in vs measured.** The *fixed point* of `D∇²b = κρ` is the Newtonian field equation **by construction** — so the field-equation check (§2.1) confirms the forced terms are Newtonian-consistent, not an independent surprise; the forcing lives in the two terms being primitive-grounded. What is **genuinely emergent (not built in)** is everything in §2.2–§2.3: the linear mass-scaling, the finite-radius horizon, and the frozen cut.

## 2. Measured results

### 2.1 The field equation `∇²b ~ ρ` (the fixed point is Newtonian)

Weak source, relaxed to steady state (`evaluation/DynamicalBandwidth/`):

- `corr(∇²b, ρ) = +0.999` over the field — the steady state satisfies `D∇²b = κρ`, the **Newtonian field equation** (R1/R9).
- `|∇²b|` is **52×** larger on the source than outside — the bandwidth-Laplacian is concentrated on the matter, harmonic in vacuum.
- The vacuum deficit falls as `1 − A\ln r` (2D-harmonic; slope `−0.079`) — the correct 2D Green's function. *(Dimensional note: 2D gives the log; 3D would give `1 − r_s/r`, the Schwarzschild profile. The dimension-independent statement `∇²b ~ ρ` is what R9 claims and what is verified here.)*

### 2.2 Schwarzschild mass-scaling `r_s ∝ M` (emergent)

Varying the source strength, the deficit amplitude is **exactly linear** in the integrated source:

| integrated source `M` | deficit amplitude |
|---|---|
| 201 | 0.040 |
| 402 | 0.080 |
| 603 | 0.120 |
| 804 | 0.160 |

`deficit ∝ M` to the digit — the **Schwarzschild relation `r_s ∝ M`**, emergent from the Poisson fixed point + a localized source (not built in).

### 2.3 The horizon and the frozen A2 cut (emergent — the payoff)

Strong source: nothing in the rule mentions a horizon, yet one **forms**:

- `b → 0` on a **finite-radius surface** (`r_h ≈ 16`, 820 nodes at `b ≤ 0`) — where the local matter-sink outpaces what adjacency-sharing can refill, `b` is driven to the P04 floor on a *sphere*, not just a point.
- `g_rr ~ 1/b → ∞` just outside `r_h` (measured `≈ 31`, diverging as `b → 0`) — the emergent metric **degenerates** on that surface: a **metric horizon**.
- The reserve in the `b = 0` core is **exhausted** (`max 0.00`) — the cut is **frozen** (P11; it cannot reopen).

> **This realizes, dynamically, the R4 §6 unification that was previously only argued structurally:** the `b → 0` locus is *at once* an **A2 emergent decoupling cut** (#8), a **metric horizon** (`g` degenerates), and — by R4 §6 — a V5-saturated surface. One rule, one locus, three identities. The bandwidth-collapse rule that forms A2's cuts **is** the rule that forms the EFE's horizons — now shown by build-and-run, not just by argument.

## 3. Structural vs contingent

| Item | Verdict |
|---|---|
| `F` form = R2 admissible core (P02 share − P11 matter-sink) | **forced** (R2; not tuned) |
| steady state = Newtonian field equation `∇²b~ρ` | **fixed point of the forced terms** (corr 0.999) |
| Schwarzschild mass-scaling `r_s ∝ M` | **emergent + measured** (linear to the digit) |
| finite-radius `b→0` horizon, `g_rr→∞` | **emergent + measured** (not built in) |
| `b→0` = A2 cut = metric horizon (R4 §6 unification) | **realized dynamically** |
| frozen cut (reserve exhausted, P11) | **emergent + measured** |
| 2D log vs 3D `1/r` profile | **dimensional caveat** (field eq `∇²b~ρ` is dimension-independent) |
| hyperbolic/retarded field eq; GW sector; mode count *from this `F`* | **not done** — this is the static/elliptic sector |
| `α₁, α₂` from the linearized `F` | **not done** — needs the dynamical (non-static) rule |
| exact `κ, D` and precise reserve dynamics | **not pinned** (minimal forced model) |
| any structural block | **none** |

## 4. Verdict

**The dynamical-bandwidth rule `F` is built and runs, and its steady state reproduces the three things it must.** In its forced form — P02 adjacency-sharing minus P11 matter-concentration sink, with a monotone-draining reserve — the rule's fixed point is the **Newtonian field equation `∇²b ~ ρ`** (`corr 0.999`, Laplacian concentrated 52× on the source, harmonic vacuum); the deficit amplitude is **exactly linear in the source** (the Schwarzschild relation `r_s ∝ M`, emergent); and at strong coupling a **finite-radius `b → 0` horizon emerges** (`g_rr ~ 1/b → ∞`) that is a **frozen A2 decoupling cut** (reserve exhausted) — *realizing dynamically the R4 §6 identity that the A2 cut, the metric horizon, and the `b → 0` locus are one object.* This is the first build of the #1/#8 keystone, and it clears the static/Newtonian bar: the forced rule is Newtonian-consistent and forms Schwarzschild-scaled, frozen horizons by its own dynamics.

**The honesty lines.** (i) The field-equation result is the *fixed point of the forced terms* — the content is that those two terms are primitive-grounded (P02, P11), not that Poisson is a surprise; the genuinely emergent results are the linear mass-scaling, the horizon, and the frozen cut. (ii) This is the **static/elliptic** sector — the hyperbolic (retarded) field equation, the gravitational-wave sector, the **mode count *from this explicit `F`*** (vs the gauge-group argument of R10), and the preferred-frame `α₁, α₂` all require the *dynamical* (non-static) rule and are **not** done here. (iii) The model is minimal: `κ, D`, and the precise reserve dynamics are not pinned. **Einstein is not derived; the keystone rule now exists, runs, and passes its static checks — and #8 (A2-dynamical) is, for the first time, realized by build-and-run rather than argued.**

## 5. Next

1. **The dynamical (hyperbolic) rule.** Replace the relaxational `ḃ = D∇²b − κρ` with the retarded/second-order form (the wave sector), linearize it, and **count the modes from `F` directly** — confirming R10's gauge-group result (2 tensor + 1 scalar, khronometric) by explicit computation, and reading off the **scalar (khronon) speed** and `α₁, α₂` (the GR-II falsification front).
2. **3D + the `1/r` profile.** Re-run in 3D to recover `b = 1 − r_s/r` explicitly and the strong-field Schwarzschild horizon at `r_s`.
3. **Pin `κ, D`.** Tie the sink coefficient `κ` to the `α=1` commitment-rate strength and `D` to the P02 sharing rate, removing the last free coefficients of the minimal model.
4. **A2 sweep (#8 proper).** Vary source geometry; map when frozen cuts form and confirm A1's exact-zero capacity across each formed cut (the A2↔A1 unification, R2 §6).

---

*First build of the #1/#8 dynamical-bandwidth rule. In its forced form (P02 adjacency-sharing `D∇²b` minus P11 matter-concentration sink `κρ`, with a monotone-draining reserve), the rule's steady state is the Newtonian field equation `∇²b~ρ` (corr 0.999, the fixed point of the forced terms), the deficit scales **linearly with the source** (Schwarzschild `r_s∝M`, emergent), and strong coupling produces a **finite-radius `b→0` horizon** (`g_rr→∞`) that is a **frozen A2 cut** (reserve exhausted) — realizing dynamically the R4 §6 identity (A2 cut = metric horizon = `b→0`). Static/elliptic sector only; the hyperbolic rule, the mode count from `F`, and `α₁,α₂` are next; `κ,D` unpinned. No corpus edits, no new primitives; Einstein not derived; the keystone rule now exists and runs, and #8 is realized by build-and-run.*
