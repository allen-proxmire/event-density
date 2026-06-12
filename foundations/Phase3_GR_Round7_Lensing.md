# Phase-3 GR — Round 7: Light Bending and the Einstein/Nordström Fork

**Foundations derivation attempt, with the arc's first simulation. Not a rule proposal, not a corpus edit, not a new primitive. Nothing here derives the Einstein equations.**
Round 6 reduced the whole Einstein question to a falsifiable, simulable fork: does an ED source deflect fronts (Einstein-class) or not (Nordström)? Round 7 closes the geodesic identity, sharpens the fork (correcting a tempting over-reading), gives a physically-grounded forward argument for which way it tilts, and builds the lensing instrument.
**Crank rail:** forward only; tag **structural** vs **contingent**; the most valuable outcome is a sharp test, and *over-claiming a positive is the failure mode to guard against* — including against this round's own simulation.

---

## 1. Q1 closed: front propagation is Fermat = null-geodesic motion

The certified front advances each step to the **max-Σ neighbour** — greedily to the locally most-coherent / highest-bandwidth channel. That greedy local rule is, exactly, a **discrete Fermat principle** (Huygens construction: each step takes the locally fastest channel). Fermat's principle *is* null-geodesic propagation: in the continuum, a wavefront whose normal advances along the locally-extremal-bandwidth direction traces the **null geodesics of the optical metric** built from `b`. So:

> **ED's front worldlines are null geodesics of the optical metric — forced by the greedy max-Σ rule (= discrete Fermat).**

This closes R6's open geodesic identity for the **null/front sector**: the `∇_μ T^μν = ρ a^ν` condition (R6 ◆) is met for fronts, `a^ν = 0`. (Timelike/massive geodesics need the full lapse and are deferred.) **Structural→resolved** for the null sector. One critical consequence carried into §2: the **optical metric is not the spatial metric** — it combines the spatial bandwidth metric *and* the temporal lapse.

## 2. The fork, stated correctly — and a self-correction

It is tempting to say "the bandwidth profile bends a ray, therefore ED bends light, therefore Einstein." **That is wrong, and the sim below would mislead if read that way.** A spatial index field bends rays in a Fermat sense *regardless* of the gravity class — but the **physical** light deflection in a static spacetime is governed by the **optical metric** `g^opt_ij = g_ij / (−g_00)`, which divides the spatial metric by the temporal lapse. The decisive fact:

- **Null geodesics are conformally invariant.** A **conformally flat** metric `g_μν = Ω²η_μν` (Nordström) has `g^opt_ij = Ω²δ_ij / Ω² = δ_ij` — flat — so **light bends by exactly zero.** The spatial factor `Ω` cancels against the temporal `Ω`.
- **Einstein (Schwarzschild)** has `g_00` and `g_rr` that do *not* cancel (`g_00 g_rr = −1`), so the optical metric is curved and light bends — with the famous **factor of 2** (spatial and temporal contributions *add* equally).

So the deflection decomposes as **spatial contribution ⊕ temporal contribution**, and the fork is *which way the temporal lapse acts*:

> **Nordström** ⟺ lapse **cancels** the spatial bending (total 0).  **Einstein** ⟺ lapse **reinforces** it (total = 2 × spatial).

The bandwidth profile alone (spatial) cannot decide this. The fork is the **relationship between the spatial metric `g~b⁻¹` and the temporal lapse `c(b)`.**

## 3. Which way ED tilts — a physical forward argument

In ED both sectors are built from the same `b` (R4 §2): the spatial metric is `g_rr ~ b⁻¹`, and the lapse is the **finite-width bandwidth-limit speed** `c` (T8/N1). The fork is the scaling of `c` with `b`:

- The spacetime is **conformally flat (Nordström)** iff `g_00 ~ g_rr`, i.e. `c² ~ b⁻¹` — the bandwidth-limit speed **decreasing** with bandwidth.
- The spacetime obeys the **Schwarzschild/Einstein relation** `g_00 g_rr ~ −const` iff `c² ~ b` — the bandwidth-limit speed **increasing** with bandwidth.

The physical meaning of "bandwidth-limit speed" decides it. `c` is the cap on how fast a front can propagate, set by available bandwidth/capacity. **More bandwidth → higher capacity → faster front → larger `c`.** That is `c` *increasing* with `b` (`c² ~ b` to leading order), which is the **Einstein** relation, not the Nordström one. The Nordström branch would require the front to go *slower* where there is *more* bandwidth — the opposite of what "bandwidth-limit speed" means.

> **ED tilts to Einstein, for a physical reason:** the bandwidth-limit speed rises with bandwidth, giving `g_00 g_rr ~ −const` (the Schwarzschild relation) and a non-conformal, light-bending metric. Nordström is disfavoured because it needs the bandwidth-limit speed to *fall* with bandwidth.

This is a **lean, not a proof** — the exact functional `c(b)` must come from explicit signature assembly (R4 Q2), which is **R8**. But the direction is physically forced by what the lapse *is*.

## 4. The lensing instrument (the arc's first simulation)

`gr_lensing_test.py` ray-traces fronts (eikonal: `dT/ds = ∇⊥ ln n`) through an imposed static **spatial** index `n(r) = b(r)^{−1/2}`, with an ED-like depleted profile `b(r) = b∞(1 − rs/r)` (bandwidth drawn down near a high-ρ source). It measures the deflection `α` vs impact parameter `ξ`. Results:

- **Gravitational-lensing law confirmed:** `α·ξ = −1.07` (constant across `ξ = 10…80`, CV = 0.058), matching the weak-field prediction `α = rs/ξ` (`rs = 1`). The deflection is `∝ 1/ξ`, **toward** the source (correct sign).
- **Scales with source strength:** `α·ξ` linear in `rs` (`−0.52, −1.08, −2.38` for `rs = 0.5, 1, 2`) — `α ∝ M`, the lensing signature.
- **Flat control (no source):** `α = 0` exactly — no spurious bending.

**What this validates, honestly:** the **Fermat/null-geodesic mechanism** and the lensing *kinematics* (`∝ rs/ξ`, `∝ M`) — i.e. the **spatial contribution** to the deflection. It does **not** by itself decide the fork: per §2, the physical total is spatial ⊕ temporal, and the sim imposes only the spatial sector. Read correctly, the sim confirms ED has a working gravitational-lensing kinematics and a non-trivial spatial deflection; §3 argues the temporal lapse *adds* to it (Einstein, total ≈ 2× this), pending R8.

## 5. ED ↔ GR structure map (updated through Round 7)

| GR object | ED structure | status |
|---|---|---|
| null geodesics | front = discrete Fermat (max-Σ) | **= optical-metric null geodesics ✓ (R7)** |
| `∇_μ T^μν = 0` (null sector) | `a^ν = 0` for fronts | **holds ✓ (R7)** |
| lensing kinematics `α ∝ M/ξ` | eikonal ray-trace of `n=b^{−1/2}` | **confirmed ✓ (sim, spatial part)** |
| temporal lapse `c(b)` | bandwidth-limit speed (T8/N1) | scaling **open — R8** (physically `c²~b`) |
| Einstein vs Nordström | `g_00 g_rr ~ −const` (`c²~b`) vs conformal (`c²~b⁻¹`) | **tilts Einstein (§3); not closed** |
| field equation `G=κT` vs `R=κT` | curvature↔source relation | **open — R8** |

## 6. Structural vs contingent

| Item | Verdict |
|---|---|
| front = null geodesic (Q1) | **resolved** (discrete Fermat, forced) |
| spatial bending nonzero, `∝M/ξ` | **confirmed** (sim) |
| conformal⇒no-bending (the real fork) | **clarified** (null conformal invariance) |
| `c(b)` scaling (decides the fork) | **contingent — open** (R8); physically `c²~b` ⇒ Einstein |
| field equation form | **contingent — open** (R8) |
| imposed `b(r)` profile (not derived) | **contingent** (needs dynamical rule + field eq, R8) |
| any structural block | **none found** |

## 7. Verdict

**The geodesic identity closes for fronts, the fork is correctly located in the spatial-vs-temporal relationship, and ED tilts to Einstein for a physical reason — but the tilt is not yet a proof.** Three results: (i) ED front propagation **is** Fermat / null-geodesic motion (forced by the greedy max-Σ rule), closing R6's geodesic condition for the null sector; (ii) the Einstein/Nordström fork is **not** "does the spatial profile bend a ray" (it always does, in a Fermat sense — and a naive reading of the simulation would over-claim here) but **whether the temporal lapse cancels (Nordström, zero) or reinforces (Einstein, 2×) that spatial bending** — decided by the scaling of the bandwidth-limit speed `c(b)`; (iii) the **physical meaning of "bandwidth-limit speed" — faster where there is more bandwidth — forces `c² ~ b`, the Schwarzschild/Einstein relation**, with Nordström disfavoured because it would need speed to *fall* with bandwidth. The arc's first **simulation** validates the lensing kinematics (`α = rs/ξ`, CV 0.058; `α ∝ M`; flat→0), confirming the spatial contribution and the Fermat mechanism.

So ED is **Einstein-leaning, not Nordström**, and the reason is structural-physical, not retrofitted. What remains is genuinely quantitative: pin `c(b)` by explicit **signature assembly** (R8) to confirm `g_00 g_rr ~ −const` and the factor-of-2, and derive the **field equation** to fix the source coefficient. **No structural block survives; Einstein is not derived; the open problem is now a *quantitative* one — the lapse scaling and the field-equation coefficient — with the qualitative class (bends light, non-conformal) physically argued and the lensing kinematics simulated.**

## 8. Round-8 questions

1. **Signature assembly (now the critical path).** Assemble the Lorentzian metric explicitly and derive `c(b)`: does the bandwidth-limit speed give `c² ~ b` (Einstein, `g_00 g_rr ~ −const`) or `c² ~ b⁻¹` (Nordström)? This single scaling decides the fork.
2. **Full deflection.** With `c(b)` in hand, compute the *total* (spatial ⊕ temporal) deflection — is it the GR factor `4GM/c²ξ` (2× the simulated spatial part) or zero?
3. **Field equation.** Derive the curvature↔source relation; is it full-tensor `G^μν = κT^μν` (Einstein) or trace `R = κT` (Nordström)?
4. **Derive `b(r)`.** Replace the imposed profile with the one the dynamical-bandwidth rule (R2) + field equation actually produce around an ED source; re-run the instrument on it.
5. **Timelike geodesics.** Extend Q1 from null (fronts) to timelike (massive) worldlines, which require the assembled lapse.

---

*Round-7 derivation attempt + first simulation. Verdict: front propagation **is** Fermat / null-geodesic motion (closing the geodesic identity for the null sector, forced by max-Σ); the Einstein/Nordström fork is correctly the **spatial⊕temporal** relation (conformal⇒zero bending by null conformal invariance — a naive "the profile bends rays, so Einstein" over-reads the sim), decided by the bandwidth-limit-speed scaling `c(b)`; and ED **tilts Einstein** because "more bandwidth ⇒ faster" forces `c²~b` (the Schwarzschild relation), Nordström needing the unphysical opposite. The arc's first simulation validates the lensing kinematics (`α ∝ rs/ξ ∝ M`, flat→0) — the spatial contribution. No corpus edits, no new primitives, no speculative physics. Nothing here derives the Einstein equations; the residual is now quantitative (lapse scaling + field-equation coefficient), with the qualitative class physically argued.*
