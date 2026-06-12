# ED-10 — Round 3: Quantitative Horizon Rates and Area Scaling

**Quantitative causal-structure analysis. Not a GR derivation, not a corpus edit, not a new primitive. Does NOT claim the BH area law `S = A/4`.**
Derives **scaling *forms*** for horizon evolution from the admissible bandwidth rule + V5 finite memory. Stays EFE-free.
**Hard rail:** F is only *partially forced* (Phase-3 GR R2–R3: coefficients and the band↔edge map are free). So this round yields **form-forced scalings with value-inherited coefficients** — ED's own methodology — **never absolute numbers**, and the **mass-dependence is deferred to EFE** throughout. Every `∝` below has a free constant; none is a prediction of a number.

---

## 1. Collapse rate (formation)

Model an edge's reserve `r(t)` near collapse. The corpus gives the commitment rate `Γ_commit ~ b_int/r`; each commit drains `δ` of reserve; influx `J` arrives via the adjacency band. So:

`ṙ = −(b_int/r)·δ·c₁ + J`  (c₁, δ free).

Near collapse the `1/r`-diverging drain dominates `J`. Writing `K = c₁ b_int δ`: `ṙ = −K/r`, hence `r(t) = √(r₀² − 2Kt)`. Two **form-forced** consequences (free coefficient `K`):

- **Finite-time, accelerating collapse:** `r → 0` at `t_c = r₀²/(2K)`, with `ṙ → −∞` as `r → 0` (the `Γ ∝ 1/r` positive feedback — a runaway endgame). Collapse is a sudden nucleation, not a smooth approach.
- **Collapse time `t_c ∝ r₀²/b_int`** — quadratic in the initial reserve, inverse in internal bandwidth. (If `b_int` *grows* as commitment concentrates bandwidth, the runaway is faster still.)

**Threshold:** collapse wins when influx cannot match the diverging drain — `J < J_c ~ K/r₀`. Above `J_c`, sub-critical (sustained `b>0`); below, runaway. The threshold is **local** (per-edge drain-vs-influx), not global.

## 2. Growth rate (accretion)

When a region is decoupled (`b=0`), fronts cannot enter, so commitment activity **piles up at the boundary** → boundary-edge commitment density rises → boundary edges cross *their* local threshold → the surface accretes **outward**. The growth is **surface-flux-limited**: for a horizon of edge-count `A`, infall arrives through the surface, so

`dM/dt ∝ A · j`  (j = commitment flux per surface edge).

This is **superlinear while fed** (abundant infalling commitment) and **self-limiting** when the supply depletes — Bondi-like accretion. The load-bearing scaling: **accretion ∝ horizon area** (`dM/dt ∝ A·j`), the first appearance of area-extensivity.

## 3. Quantum leakage rate (Hawking analogue)

A `b=0` surface blocks classical V1 (A1), but V5 finite memory `τ_V5` lets cross-chain-correlated pairs straddling the surface leak over `~τ_V5`. Per surface edge the leak scales as `(1/τ_V5)·f(κ)`, where `κ` is the local steepness of `b→0` — the **surface-gravity analogue**. Summing over the surface:

`L ∝ A · f(κ) / τ_V5`  (form-forced; `f`, and the `κ↔size` relation, free/EFE-dependent).

- **Symmetry** (from R2): one-way → asymmetric net outflow (**Hawking**); two-way → symmetric, no net flux (**thermal/de Sitter**).
- **Temperature analogue:** `T ∝ κ` (surface b-gradient) — the structural form of `T_H ∝` surface gravity.
- **Endgame:** as a one-way horizon shrinks, `A ↓` but `κ ↑` (steeper `b→0` for a smaller surface). If `f(κ)` rises faster than `A` falls, evaporation **accelerates** (the Hawking final-flash structure). The *sign of the crossover* needs the `κ↔A↔M` relations = **EFE**.

## 4. Area scaling

Treat the `b≈0` edge set as the discrete horizon surface, `A` = edge count.

- **Leakage `∝ A`:** the leak is a sum of independent per-edge contributions → extensive in surface edges. The structural seed of "luminosity ∝ area."
- **Threshold is local, not area-dependent:** each edge collapses on its own drain-vs-influx condition (§1). So *formation* is curvature/local; *leakage* is area/global — an honest split.
- **Holography from A1 severance — the standout result.** Why area (`∝ A`), not enclosed volume? Because A1's determinability severance makes the **interior causally inaccessible from outside** (capacity 0). So an outside observer's *missing information* about the interior is carried by the **boundary cut** — the surface edges — **not** the interior volume (whose detailed state is determinability-severed and adds no *accessible* information). **The information is boundary-encoded because the interior is determinability-cut.** That gives `S ∝ A` (area, not volume) as a **structural consequence of A1**, i.e. a *reason* for holography rather than an assertion.

**What is NOT claimed:** the coefficient — the `1/4`, the Planck-area normalization, `S = A/4` — needs the EFE placement (edge-area ↔ Planck-area). So: **form `S ∝ A` is structurally forced by A1 severance; the coefficient is value-inherited/EFE.** Exactly the form-forced/value-inherited split.

## 5. Classical vs quantum opacity

- **Sharp at the substrate scale.** Discretely, `b=0` is exact → classical V1 capacity is **exactly 0** (A1); V5 leakage is a **separate** finite-memory channel. The split is **sharp**: a discrete edge is coupled or decoupled, full stop.
- **Blurred in the continuum (scale-dependent).** In the thick/DCGT regime `b→0` *asymptotically* → classical capacity is small-but-nonzero and the classical/quantum distinction smears into a crossover. So the split is **scale-dependent**: exact at the substrate, smooth at coarse-graining.
- **Symmetry is topology-dependent, the split is not.** The leak's symmetry tracks one-way vs two-way (R2); the *existence* of the classical/quantum split does not. So: split = **sharp-at-substrate, scale-dependent in continuum**; symmetry = **directionality-dependent**.

## 6. Predicted scalings

| Quantity | EFE-free scaling form | Free / EFE-dependent part |
|---|---|---|
| Collapse time | `t_c ∝ r₀²/b_int`; finite-time; `ṙ ∝ −1/r` (accelerating) | coeff (`δ, c₁`) free |
| Accretion rate | `dM/dt ∝ A·j` (area × infall flux) | `M↔A` relation needs EFE |
| Leakage rate | `L ∝ A·f(κ)/τ_V5` | `f`, `κ↔A↔M` need EFE; `τ_V5` value-inherited |
| Leakage symmetry | one-way asym (Hawking) / two-way sym (thermal) | qualitative — EFE-free |
| Temperature | `T ∝ κ` (surface b-gradient) | `κ↔M` needs EFE |
| Entropy | `S ∝ A` (edge count; **holographic via A1 severance**) | coeff (`1/4`, Planck norm) needs EFE |
| Opacity split | sharp at substrate (`b=0` exact); blurred in continuum | crossover scale = DCGT |

## 7. Verdict

**ED predicts horizon *scaling forms* without EFE; it cannot predict the *numbers* without it — and that boundary is sharp and principled.** Form-forced and EFE-free: collapse is finite-time and accelerating with `t_c ∝ r₀²/b_int`; accretion and leakage are **area-extensive** (`∝ A`); leakage temperature `∝` surface b-gradient; leakage symmetry tracks causal type; entropy is `∝ A` with a **structural holographic argument from A1 severance** (interior determinability-cut → boundary-encoded information → area not volume); and the classical/quantum opacity split is sharp at the substrate, scale-dependent in the continuum. **Value-inherited / EFE-dependent:** every coefficient, and the entire mass-dependence (`A↔M`, `κ↔M`, hence `L↔M`, `T_H` absolute, `S=A/4`) — because those require the horizon *placement* (radius from mass), which is the EFE keystone. This is exactly ED's form-forced/value-inherited methodology, and it draws a clean, honest line: **ED-10 gives the *structure and scalings* of horizon thermodynamics; the *thermodynamic constants* wait on Phase-3 GR.** Nothing here is a number, and the BH area law is not claimed.

## 8. Round-4 questions

1. **Entropy coefficient.** Does edge-counting + Planck-area normalization (post-EFE) give `S = A/4`? (Needs placement.)
2. **Surface gravity.** Define `κ` precisely from the discrete `b`-profile; confirm `T ∝ κ` and identify what fixes the proportionality.
3. **Mass-closure.** Once EFE supplies `A ∝ M²`, `κ ∝ 1/M`, do `L ∝ 1/M²` and `t_evap ∝ M³` follow? (The EFE-dependent thermodynamics.)
4. **Holographic bound.** Make "A1 severance → area not volume" rigorous — is it a genuine holographic entropy bound, or only a scaling?
5. **Information.** As a one-way horizon evaporates, does the A1 common-cause correlation carry the information out (unitarity), or is it lost? — the paradox in ED terms.
6. **Coefficient forcing.** Which free coefficients are genuinely value-inherited vs which might be fixed by the Phase-3 GR R4 covariance hinge?

---

*Round-3 ED-10 quantitative analysis only. Verdict: ED predicts horizon scaling FORMS without EFE (collapse `t_c ∝ r₀²/b_int` finite-time/accelerating; accretion and leakage area-extensive `∝ A`; `T ∝ κ`; `S ∝ A` holographic via A1 severance; opacity split sharp-at-substrate); all COEFFICIENTS and the mass-dependence are value-inherited / require the EFE placement keystone. Form-forced, value-inherited — no numbers claimed, BH area law not asserted. No corpus edits, no new primitives, no speculative physics.*
