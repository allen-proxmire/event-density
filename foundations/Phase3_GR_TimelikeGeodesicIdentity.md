# Phase-3 GR — The Timelike Geodesic Identity (closing `∇·T=0` for *massive* matter)

**Foundations derivation attempt — closes a flagged residual of the Phase-3 GR arc, not a new round of it. Not a rule proposal, not a corpus edit, not a new primitive. Nothing here derives the Einstein equations.**
Round 6 reduced `∇_μ T^μν = ρ a^ν`, so rank-2 conservation `⟺` the bandwidth worldlines are geodesics of `g ~ b⁻¹`. Round 7 proved this for the **null** sector (front propagation = Fermat null geodesics). The **timelike / massive** sector was left *assumed* (GR-I preamble 9: "the claim that ED's massive-matter worldlines *are* those timelike geodesics is shown only for null fronts and is otherwise assumed"). This note attacks the timelike identity directly.
**Crank rail:** forward only — from ED's max-Σ front dynamics to the geodesic statement, never backward from GR. A **forced** identification is a derivation; a **chosen** one is a retrofit. Tag **structural** vs **contingent**. The timelike result must *reduce to the proven null result* in the massless limit, or it is wrong — that is the round's internal check, and it could fail.

---

## 1. The target, stated precisely

ED's massive matter is a **subluminal front**: a worldline that advances *below* the bandwidth-limit speed `c` (a null front carries `|v| = c`; a massive front carries an internal commitment cadence — a rest-frequency — so `|v| < c`). The claim to test:

> The max-Σ path of a subluminal front coincides with the **timelike geodesic** of the emergent metric `g ~ b⁻¹`, `N² ~ b`.

Static isotropic metric (GR-I weak-field gauge): `ds² = −b\,dt² + b⁻¹\,dx²`.

## 2. The two variational principles

**Geodesic (timelike).** A timelike geodesic extremizes proper time `∫dτ`, `dτ² = b\,dt² − b⁻¹ dx²`. Using the `t`-Killing vector, the conserved energy is `E = b\,ṫ`, and the **spatial orbit** extremizes the **Jacobi/Maupertuis** length (the standard reduction of a static timelike geodesic to a spatial variational problem):

> `δ ∫ J(b)\,dl_δ = 0`, with `J(b) = \frac{1}{b}\sqrt{E² − m²b}`   …(J)

(`dl_δ` the flat line element; the `b⁻¹` prefactor is the spatial metric's `√g_{spatial} = b^{−1/2}` times the momentum `√(E²/b − m²) = b^{−1/2}\sqrt{E²−m²b}`.) `m` is the front's rest-frequency (internal commitment cadence), `E` its conserved energy.

**ED max-Σ.** The front advances to its Σ-maximal admissible neighbour each step; the continuum limit is the extremal-coherence principle `δ∫Σ\,dl = 0`. For **null** fronts, Round 7 established this is **Fermat's principle** with optical index `n_opt ~ b⁻¹`, giving the null geodesics of `g ~ b⁻¹`.

The timelike identity is therefore the single statement: **does the subluminal max-Σ functional equal the Jacobi function `J(b)`?**

## 3. The internal check — (J) must reduce to Round 7's null result, and it does

A timelike derivation that did not collapse to the proven null one in the massless limit would be self-inconsistent. Take `m → 0` in (J):

> `J(b) \xrightarrow{m→0} \frac{E}{b} = E\,n_opt`,  with `n_opt ~ b⁻¹`.

This is **exactly the Fermat optical functional** Round 7 matched to ED's null max-Σ (the optical index `n_opt ~ b⁻¹`, the *square* of the spatial index — GR-I §4, the source of the factor of two). So the Jacobi principle (J) **reduces to the proven Fermat/null principle as `m → 0`.** [Structural consistency — the timelike functional contains the null one as its massless limit. Passes; could have failed.]

## 4. The Newtonian check — (J) must give Newtonian orbits, and it does

Weak field `b ≈ 1 + 2Φ`, slow front `E ≈ m + E_kin`, `E_kin, |Φ| ≪ 1`. The radical in (J):

> `E² − m²b ≈ (m + E_kin)² − m²(1 + 2Φ) ≈ m² + 2mE_kin − m² − 2m²Φ = 2m\,(E_kin − mΦ)`.

With the Newtonian potential `V = mΦ` (and `Φ ~ (b−1)/2` from `g_{00} = −b ≡ −(1+2Φ)`, GR-I), the radical is `\sqrt{2m(E_kin − V)}` — the **Maupertuis momentum**. So (J) reduces to the Maupertuis principle `δ∫\sqrt{2m(E−V)}\,dl = 0`, whose extremals are **Newtonian orbits**. [Structural consistency — recovers Newton, as it must; passes.]

So the Jacobi function (J) has **both required limits**: Fermat/null at `m→0` (Round 7), Maupertuis/Newton in the weak field (Round 1). Any correct timelike-geodesic functional for `g~b⁻¹` must have exactly these limits, and (J) does — it *is* the timelike-geodesic functional. The whole question reduces to whether ED's subluminal max-Σ produces (J).

## 5. The reduction: massive max-Σ = the massive eikonal = (J)

The null result (Round 7) is the **eikonal limit** of front propagation: a null front is a surface of constant phase advancing at `c`, and max-Σ selects the Fermat (extremal-optical-path) ray. A **massive** front is the *same eikonal construction with an internal rest-frequency*: in the standard relativistic-particle correspondence, a massive worldline is a null/eikonal ray carrying an internal clock (the de Broglie rest-oscillation), and its eikonal (Hamilton–Jacobi) ray **is** the timelike geodesic, with the massless limit returning the optical/Fermat ray. Concretely, the front phase `S` obeys the Hamilton–Jacobi equation `g^{μν}∂_μS\,∂_νS = −m²`; its rays are timelike geodesics; the `m→0` limit `g^{μν}∂_μS∂_νS = 0` is the eikonal/Fermat null case. The Maupertuis function `√(E²−m²b)/b` is exactly the spatial reduction of this `S`.

So the identification is: **ED's subluminal max-Σ front is the massive eikonal of the same propagation Round 7 treated masslessly; its ray is the Hamilton–Jacobi ray of `g~b⁻¹`, i.e. the timelike geodesic.** The single load-bearing assumption is that ED's massive front carries the standard internal rest-frequency structure (P13 homogeneous tick supplies a worldline's intrinsic cadence; P11 makes it monotone — together a proper-time clock) and that its coherence functional is the eikonal phase. This is **evidenced** (the CoarseGrain worldlines are ballistic free-flight that bends with `∇b` — geodesic motion in `g~b⁻¹`; the front *is* a phase-coherent propagator) and **forced in both limits** (§3–§4), but the explicit massive-front coherence has **not** been computed bit-for-bit from the Σ-rule. **Contingent — evidenced, limit-forced, one named gap.**

## 6. Structural vs contingent

| Item | Verdict |
|---|---|
| `∇·T=0 ⟺ geodesic motion` | **established** (R6 ◆) |
| null sector = geodesics (Fermat) | **proven** (R7) |
| the timelike-geodesic functional = Jacobi `J(b)` (J) | **standard GR** (the spatial reduction of a static timelike geodesic) |
| `J(b) → Fermat` as `m→0` | **forced** — reduces to the proven null case (§3) |
| `J(b) → Maupertuis/Newton` (weak field) | **forced** — recovers Newtonian orbits (§4) |
| massive max-Σ front = massive eikonal of the null front | **evidenced + limit-forced** (§5); explicit Σ-computation **open** |
| internal rest-frequency = proper-time clock (P11/P13) | **structural** (the tick is the worldline's intrinsic cadence) |
| explicit massive-front coherence from the Σ-rule | **contingent — open** (the residual) |
| any structural block | **none found** |

## 7. Verdict

**The timelike geodesic identity is advanced from "assumed" to "reduced to the massive eikonal of the proven null result, forced in both limits."** R6 made `∇·T=0` equivalent to geodesic motion of the bandwidth worldlines; R7 proved the null half (Fermat, `n_opt ~ b⁻¹`); this note treats the timelike half. The timelike-geodesic functional for `g~b⁻¹` is the Jacobi function `J(b) = b⁻¹\sqrt{E²−m²b}` (J), and it satisfies the two non-negotiable internal checks: it **reduces to Round 7's Fermat functional as `m→0`** (so the timelike result *contains* the proven null one) and to **Maupertuis/Newtonian orbits in the weak field** (so it recovers R1). ED's subluminal max-Σ front is identified as the **massive eikonal** of the same propagation Round 7 treated masslessly — its Hamilton–Jacobi ray being the timelike geodesic — with the worldline's intrinsic clock supplied by P11/P13. This is evidenced (ballistic CoarseGrain worldlines bending with `∇b`) and *limit-forced*, but the explicit massive-front coherence has not been computed from the Σ-rule, so the identity is **contingent — limit-forced and evidenced, with one named residual**, not proven. It could have failed the `m→0` check; it did not.

**What this buys the arc:** `∇·T=0` is no longer *assumed* for matter — it is reduced to the massive extension of a proven result, removing the bald "timelike geodesic assumed" caveat that GR-I/GR-II/KM-I/KM-II all carry, and replacing it with a located, limit-checked reduction. The one remaining step (the explicit Σ-rule computation of the massive-front eikonal) is the natural next derivation. **Einstein is still not derived; one more of its load-bearing assumptions is now reduced to a limit-forced identification.**

## 8. Next questions

1. **The explicit massive-front coherence (closes this).** Compute, from the certified Σ-rule, the coherence functional of a *subluminal* front (a front with an internal rest-cadence) and confirm it is the eikonal phase whose spatial reduction is `J(b)`. This is the bit-for-bit version of §5, and it is *simulable* on the certified substrate (the same instrument that gave the null/Fermat ratio 2.09).
2. **`α = 1` (P-Commitment-Linear).** Independently, derive the reserve-independence that fixes the lapse `N²~b` from the P04 band law — the *other* assumption (besides this one) that the Einstein branch rests on.
3. **Anisotropic (non-isotropic-`b`) timelike orbits.** (J) used the isotropic gauge; confirm the per-edge directional `b_ij` (the Einstein-vs-Nordström anisotropy, R6 §4) gives the correct frame-dragging/precession corrections for timelike orbits, not just the isotropic Schwarzschild ones.

---

*Closes (to limit-forced reduction) the timelike half of the Phase-3 GR geodesic identity. R6 made `∇·T=0 ⟺ geodesic motion`; R7 proved the null half (Fermat, `n_opt~b⁻¹`); here the timelike-geodesic functional is the Jacobi `J(b)=b⁻¹√(E²−m²b)`, which is **forced** to reduce to R7's Fermat functional at `m→0` and to Maupertuis/Newtonian orbits in the weak field — the two checks any correct timelike functional must pass, and both pass. ED's subluminal max-Σ front is identified as the massive eikonal of the proven null front (intrinsic clock from P11/P13), evidenced by the ballistic CoarseGrain worldlines and limit-forced, with the explicit Σ-rule massive-front computation the one named residual. The "timelike geodesic assumed" caveat carried by all four gravity papers is replaced by a located, limit-checked reduction. No corpus edits, no new primitives; Einstein not derived; one fewer bald assumption.*
