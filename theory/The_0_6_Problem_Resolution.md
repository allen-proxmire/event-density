# Resolution of the "0.6 Problem" in the ED Dimensional Dictionary

**Date.** 2026-04-22 (sixth pass).
**Status.** Structural reduction + partial derivation. The 0.6 is forced algebraically; it inherits from an adjacent, already-named open problem.
**Scope.** Resolves where the `0.6` in `T_0 = 0.6 · ℏ/(mc²)` comes from and whether it is a free constant, a derived invariant, or a disguised convention. Audits five proposed derivation routes and reconciles the outcome with the `c_s = c/0.6` mismatch flagged in `ED_Geometry_Emergence_Scoping.md` §7B, `ED_Effective_Acoustic_Metric.md` §5, and `ED_Acoustic_Analogue_Experimental_Program.md` §5.

---

## 1. The problem statement

The ED dimensional dictionary defines
$$L_0 = \frac{\hbar}{mc}, \qquad T_0 = \frac{0.6\,\hbar}{mc^2}, \qquad D_{\text{phys}} = \frac{\hbar}{2m},$$
so the canonical signal speed is
$$c_0 \;=\; \frac{L_0}{T_0} \;=\; \frac{c}{0.6} \;\approx\; 1.667\, c.$$

The acoustic-metric derivation (`ED_Effective_Acoustic_Metric.md` §4) identifies the reversible-slice sound speed with the dictionary's `c_0`:
$$c_s \;=\; \sqrt{M_0} \;=\; c_0 \;=\; c/0.6.$$

The `0.6` is the single most conspicuous unexplained number in ED. The question is whether it is a free dimensionless constant, a derived invariant, or something else.

## 2. The direct derivation — read off the dictionary construction

Open `papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md` §2.4. The `T_0` definition is not stipulative — it is a *construction* from `L_0`, `D_phys`, and the nondimensional channel weight `D_nd`:

$$T_0 \;=\; \frac{L_0^2 \cdot D_{\text{nd}}}{D_{\text{phys}}} \;=\; \frac{[\hbar/(mc)]^2 \cdot D_{\text{nd}}}{\hbar/(2m)} \;=\; \frac{2\,D_{\text{nd}}\,\hbar}{mc^2}.$$

This construction is *required* for the nondimensionalisation to produce the standard simulation equation: rescaling `t ↦ t/T_0`, `x ↦ x/L_0` sends the mobility term's coefficient to `D_phys · T_0 / L_0² = D_nd` by construction. That's the point — `T_0` is chosen so that the simulation's dimensionless `D` equals `D_nd`.

Plugging in the canonical quantum-regime convention `D_nd = 0.3`:

$$T_0 \;=\; \frac{2 \cdot 0.3 \cdot \hbar}{mc^2} \;=\; \frac{0.6\,\hbar}{mc^2}.$$

**So `0.6 = 2 · D_nd(quantum)`, exactly.** And the full velocity identity is:

$$\boxed{\;\; \frac{c_0}{c} \;=\; \frac{1}{2\,D_{\text{nd}}} \;\;}$$

This is not phenomenology. It is algebraic. The `0.6` is not a free constant; it is a *derived proxy* for the quantum-regime channel weight. The question "why `0.6`?" is literally identical to the question "why `D_nd = 0.3` in the quantum regime?"

## 3. Consequences before checking the other routes

Three immediate consequences follow from the boxed identity:

**3.1.** The `c_0/c = 1/(2·D_nd)` relationship is *universal* across the atlas — it is forced by the `T_0` construction in every regime. It has nothing to do with ℏ, `m`, `c`, or quantum-ness per se. It is purely a channel-weight relationship.

**3.2.** The equal-rates point `D_nd = 1/2` corresponds *exactly* to `c_0 = c`. No free parameter, no fit. The regime where the decoherence rate equals the coherent system rate (`γ_dec = ω_sys` ⇒ `D = 1/2`) is the regime where the dictionary's signal speed is identically `c`. This is a new structural statement not in the corpus.

**3.3.** The `c_0 = c/0.6 ≈ 1.667c` superluminal value is *not* a physical propagation speed — `ED-Dimensional-01_Quantum_Regime.md` §2.5 already flags it as a "regime-boundary marker, not a physical prediction," because the underlying PDE is parabolic and has formally infinite signal speed anyway. The "60% mismatch with physical c" flagged in the geometry-emergence memos is therefore a mismatch between a *nondimensionalisation artifact* and a *physical invariant* — not two physical speeds in disagreement. The memos' language can be sharpened accordingly.

## 4. The five proposed routes — pass/fail audit

### Route 1 — damping discriminant

Test: does `D_crit(ζ) = √(2−ζ)·(2−√(2−ζ))` produce `D_nd = 0.3` or `2·D_nd = 0.6` as a fixed point, ratio, or invariant?

- At `ζ = 0`: `D_crit = 2√2 − 2 ≈ 0.828`. Not 0.3 or 0.6.
- At `ζ = 1/4` (canonical): `D_crit ≈ 0.896`. Not 0.3 or 0.6.
- At `ζ = 1/2`: `D_crit ≈ 0.775`. Not 0.3 or 0.6.

Solving `D_crit(ζ) = 0.6` yields `ζ ≈ 1.2`, outside the canonical `ζ ∈ [0,1]` range. No fixed point, no ratio, no invariant produces 0.3 or 0.6. **Route 1 fails to force the value.**

### Route 2 — reversible-slice QFT normalisation

Test: in the reversible slice (`D = 0, ζ = 0`), does the free-scalar Hamiltonian's mass/speed normalisation force `T_0/L_0 = 0.6/c`?

The reversible slice has `D_nd = 0`, so `T_0 = 2·0·ℏ/(mc²) = 0`. The `T_0/L_0` ratio is formally degenerate. The QFT mode expansion uses `c_s = √M_0` directly in absolute units and does not reference `T_0` at all. The 0.6 never enters the reversible-slice QFT construction. **Route 2 does not produce 0.6.** (The `c_s = c/0.6` identification is applied *after* the QFT construction, inherited from the dictionary.)

### Route 3 — acoustic-metric curvature scaling

Test: does the Gaussian-bump closed form `R(0) = −a/[σ²(1−a)]` or the Visser surface-gravity normalisation introduce a natural 0.6?

All curvature quantities are dimensionless functions of the bump amplitude `a` and width `σ` in units of `L_0`. No universal numerical prefactor of 0.6 or 0.3 appears at any order. The horizon-temperature formula `T_H = ℏ c_∞²/(4π L k_B)` inherits `c_∞ = c/0.6` from §2's dictionary but does not *generate* it. **Route 3 fails.**

### Route 4 — coarse-graining / PME scaling

Test: does PME-style similarity scaling produce `T_0/L_0 = 0.6/c` as a self-similar fixed point?

The porous-medium similarity solution `ρ_t = Δρ^m` in dimension `d` decays as `t^{−α}` with `α = d/(d(m−1)+2)`. For `d = 3`, `m = 2`: `α = 3/5 = 0.6`. This is a suggestive numerical coincidence. But `α` is a *temporal-decay exponent of the density*, not a velocity ratio. The Barenblatt similarity variable is `ξ = x·t^{−β}` with `β = 1/(d(m−1)+2) = 1/5`, giving a *time-dependent* characteristic velocity `∝ t^{β−1}`, not a constant `L_0/T_0` ratio. The 3/5 does not sit at the right place in the dimensional hierarchy to fix `T_0/L_0`. **Route 4 is a false positive — coincidentally the right number, structurally the wrong quantity.**

### Route 5 — ζ-dependence

Test: does canonical `ζ = 1/4` combined with the reversible limit `ζ = 0` produce 0.6 as an interpolation constant?

No natural interpolation formula between `ζ = 0` and `ζ = 1/4` produces 0.6 or 0.3. Solving `√(2−ζ)/2 = 0.6` gives `ζ = 0.56`, not canonical. Solving `1 − √(2−ζ)/2 = 0.6` gives `ζ = 1.36`, outside the canonical range. **Route 5 fails.**

## 5. Verdict

**Partial derivation + structural reduction.** The 0.6 is not a free dimensionless constant — it is algebraically forced by `T_0 = L_0²·D_nd/D_phys` to equal `2·D_nd(quantum)`. But the quantum-regime value `D_nd = 0.3` is *itself* a convention inherited from the Atlas's initial nondimensionalisation, not a derivation.

In full:

| Level | Status |
|:---|:---|
| `T_0 = 2·D_nd·ℏ/(mc²)` | **Structurally forced** by the dimensional-dictionary construction. No freedom. |
| `c_0/c = 1/(2·D_nd)` | **Structurally forced** as a corollary. No freedom. |
| `D_nd(quantum) = 0.3` | **Convention**, not derivation. The rate-balance-template program ([`ED-Dimensional-01-Ext.md`](ED-Dimensional-01-Ext.md)) is the ongoing attempt to derive it per regime. |

**The "0.6 problem" does not have its own standalone resolution.** It collapses cleanly into the already-named "`D_nd` anchoring problem" that ED-Dimensional-01-Ext was written to address. The work of deriving 0.6 is *exactly* the work of deriving `D_nd(quantum)` from first principles.

## 6. What the reduction buys

Even though the 0.6 is not independently derived, three structural statements follow from the reduction that were not previously in the corpus:

**6.1.** The "60% speed mismatch" is a mismatch between an *atlas-nondimensionalisation artifact* and a *physical invariant*. `c_0 > c` arises purely because the Atlas picks `D_nd = 0.3` (deep-coherent convention), not because ED predicts superluminal signals. ED-Dimensional-01 §2.5 already flagged this honestly: "not a physical velocity... a regime-boundary marker." The geometry-emergence memos should be updated to incorporate this framing rather than treat the mismatch as a physical anomaly.

**6.2.** `c_0 = c` exactly at the equal-rates point `D_nd = 1/2` (where `γ_dec = ω_sys`). This is a clean *selection rule*: a regime where the dictionary's signal speed coincides with the physical speed of light is the regime of rate-balance. Whether ED-09.5's Q-C transition, in its true form (at `D_crit ≈ 0.896` post-2026-04-22 correction), sits closer to or farther from this `c_0 = c` point than the canonical-convention quantum regime is a quantitative question worth pursuing.

**6.3.** The acoustic-analogue experimental program's "cross-regime signal-speed consistency check" (parent memo §9) is now sharper. Each regime's measured `c_s` is predicted to obey `c_s/c = 1/(2·D_nd(regime))`. If analogue platforms at differing `D_nd` reproduce this scaling, the dictionary is validated; if not, the `D_nd` anchoring is wrong in at least one regime.

## 7. Assumptions and caveats

- The derivation assumes the dictionary construction `T_0 = L_0²·D_nd/D_phys` is the correct nondimensionalisation convention. This is explicit in `ED-Dimensional-01_Quantum_Regime.md` §2.4 Appendix A. If a future ED revision changes this convention, the algebraic identity changes.
- `D_nd(quantum) = 0.3` is the pre-v0.4 convention. The v0.4 rate-balance-template extension anchors `D_nd` for optomechanics / cavity-QED / condensed-matter / galactic / cosmological regimes from independent rate identifications, but does not yet apply the template *within* the quantum regime itself — so the quantum-regime 0.3 remains unanchored. This is a tractable v0.5+ target.
- The `c_0/c = 1/(2·D_nd)` relationship is algebraic, not predictive. It does not tell you `D_nd`; it tells you `c_0` once `D_nd` is specified.

## 8. Deferred work to fully close the question

The 0.6 is reduced but not eliminated. Full closure requires:

- **D_nd(quantum) derivation.** Apply the rate-balance template *inside* the quantum regime itself — i.e., identify the quantum-regime `γ_dec` and `ω_sys` from first principles (Madelung / Schrödinger structure), compute `D_nd = γ_dec/(γ_dec + ω_sys)`, and check whether it reproduces 0.3 or replaces it.
- **`c_s = c` selection.** Either (a) show that rate-balance `D_nd = 1/2` is architecturally preferred in the quantum regime (resolving the mismatch), or (b) accept that the quantum-regime dictionary sits at `D_nd ≠ 1/2` and the acoustic-metric signal speed is permanently atlas-dependent.
- **Atlas-independent formulation of the acoustic metric.** Currently `c_s = √M_0` is pinned to the dictionary's `c_0`. An atlas-independent formulation would express `c_s` in observable-only quantities, bypassing `D_nd`. Possible via the Visser construction applied directly in physical units.

These are concrete, tractable theory-only targets.

---

## Appendix A — Summary card

| Claim | Status |
|:---|:---|
| 0.6 is a free dimensionless constant | **False.** It is `2·D_nd(quantum)` by construction. |
| 0.6 is a fundamental invariant | **False.** It inherits from the quantum-regime convention `D_nd = 0.3`. |
| 0.6 is derived from damping discriminant | **No.** `D_crit(ζ)` does not force 0.3 or 0.6. |
| 0.6 is derived from reversible-slice QFT | **No.** The reversible slice has `D_nd = 0`; 0.6 never enters. |
| 0.6 is derived from acoustic-metric curvature | **No.** Curvature formulae inherit `c_0`, do not generate it. |
| 0.6 is derived from PME Barenblatt scaling | **No.** `3/5` coincidence is the wrong physical quantity. |
| 0.6 is derived from ζ-interpolation | **No.** No natural interpolation produces it. |
| 0.6 is algebraically forced by the dictionary | **Yes.** `T_0 = 2·D_nd·ℏ/(mc²)`; structural, one-line. |
| 0.6 reduces to the `D_nd(quantum)` anchoring problem | **Yes.** These are the same question. |
| `c_0 = c` is reached at `D_nd = 1/2` (equal-rates) | **Yes.** New structural selection rule. |
| The "60% speed mismatch" is a physical anomaly | **No.** It is a nondimensionalisation artifact; Atlas §2.5 already noted this. |
