# Phase-3 GR — Route B, the `η` Cross-Check: the Acoustic Normalization, and Where It Blocks

**Foundations derivation — attempts the `η` computation that ties Route B to Route A (`η` should equal Route A's `−c₁₄`). Not a corpus edit, not a new primitive. The honest outcome is a *located obstruction*: the acoustic matching is clean and fixes the conformal structure, but `η` itself is NOT computable from the scalar rule — it requires the directed-flux (vector) sector of `F`, which the primitives declare (P05 transport is directional) but which is not yet built. Both Route A and Route B independently reduce the entire open falsification number to the coupling of this one unbuilt sector. That convergence is the result.**

Route B (`Phase3_GR_PPN_RouteB_DirectExpansion.md`) reduced `α₁, α₂` to a single normalization `η` in `g_{0i} = η J_b^i`, and flagged `η = −c₁₄` (Route A) as the cross-check. This note computes `η` as far as it goes.

**Crank rail:** derive forward; where the computation blocks, say *exactly* where and why; do not paper the gap with a guessed normalization. A precisely-located obstruction is a real result; a fabricated `η` is not.

---

## 1. The acoustic framework, matched to ED (clean, derived)

ED's emergent metric is an analogue (acoustic) metric: the substrate's maximal-speed fronts (P05) are the "sound," propagating on the bandwidth "fluid" `b`. The standard acoustic line element (Barceló–Liberati–Visser, 3+1 dimensions) for a fluid of density `ρ_f`, signal speed `c_s`, and flow velocity `v^i`:

> `g_{μν} = \dfrac{ρ_f}{c_s}\begin{pmatrix} -(c_s^2 - v^2) & -v_j \\ -v_i & δ_{ij}\end{pmatrix}`.

**Match to ED's static pieces** (GR-I: `g_{00} = -b`, `g_{ij} = b^{-1}δ_{ij}`, `v = 0`):

- `g_{ij}`: `(ρ_f/c_s)\,δ_{ij} = b^{-1}δ_{ij} ⟹ ρ_f/c_s = 1/b`;
- `g_{00}`: `-(ρ_f/c_s)c_s^2 = -ρ_f c_s = -b ⟹ ρ_f c_s = b`.

Product and ratio give **`ρ_f = 1`, `c_s = b`, conformal factor `Ω ≡ ρ_f/c_s = 1/b`.** (Consistent and clean: the bandwidth "fluid" has unit density, and the local signal speed is `c_s = b` — i.e. light slows where bandwidth is depleted, as required.) The cross-term is therefore

> **`g_{0i} = Ω\,(-v_i) = -v_i/b ≈ -v_i`**  (at O(v³), `b ≈ 1`).

So `η` is fixed the moment the flow velocity `v^i` is expressed through the bandwidth current.

## 2. The naive normalization — and why it is pure gauge

The conserved current of the acoustic fluid is `J_b^i = ρ_f v^i = v^i` (since `ρ_f = 1`), so naively `v^i = J_b^i` and `g_{0i} = -J_b^i`, i.e. **`η = -1`**. If this survived, the cross-check would read `c_{14} = -η = 1` — an `O(1)` coupling, hence (Route A) `α_1 = -4c_{14} = O(1)`, wildly above the bound, with ED's survival resting entirely on the dissipative suppression.

But it does not survive, for a precise reason. The scalar rule fixes the current to be **purely diffusive**:

> `∂_t b = D∇^2 b - κρ = -∇\cdot J_b - κρ`,  with  `J_b = -D∇b`.

`J_b = -D∇b` is the gradient of a scalar — it is **curl-free**, `∇×J_b = 0`. In the acoustic metric an irrotational flow `v = ∇φ` gives `g_{0i} = -∂_iφ`, which is **pure gauge**: the gravitomagnetic field `B_g = ∇×\vec g_0` vanishes, and a coordinate shift `t → t + φ` removes it. So:

> **The scalar rule `ḃ = D∇²b − κρ`, by itself, sources no physical `g_{0i}`.** Its entire current is the curl-free diffusive flux; the preferred-frame (gravitomagnetic) cross-term has zero source. This is *consistent* — the static ED metric is correctly diagonal — but it means `η` is **not determined by the scalar rule.**

This also resolves a would-be paradox: the static diffusive flux `-D∇β_2 = 2D∇U` is nonzero, yet the static metric has `g_{0i} = 0`. Correct — that flux is curl-free, hence gauge, hence no physical cross-term.

## 3. Where the cross-term actually lives — the directed-flux (vector) sector

A physical `g_{0i}` (a nonzero gravitomagnetic field) requires a **rotational** current — vorticity in the bandwidth flow. The scalar rule has none. The rotational part comes from the substrate's **directed transport**: P05 says influence propagates along adjacency *with direction*; the scalar reduction `ḃ = D∇²b − κρ` keeps only the band *magnitude* and discards the flux *direction*. The directional flux is a genuine vector field `J^i` with its own dynamics (a continuity law plus a transport/relaxation law for the flux itself), and it is *that* sector — not the scalar — that sources `g_{0i}`.

Concretely, the missing piece is a vector evolution of the form

> `∂_t J^i = -D∇^i b - \tilde Γ\,J^i + (\text{advection / source currents})`   *(schematic — the directed-flux law, NOT yet built; `\tilde Γ` the reserve drain on the flux)*,

whose *solenoidal* part is the physical gravitomagnetic source. The coefficient relating the solenoidal flux to `g_{0i}` is `η`. **This is exactly the "cross-terms require the directed-flux dynamics" that the metric-assembly note deferred** — the vector sector of `F` that no round has constructed.

## 4. The convergence — both routes reduce to one unbuilt coupling

This is the payoff. Route A and Route B reach the same wall from opposite sides:

- **Route A:** the open number is `α_1 = -4c_{14}`, where `c_{14} = c_1 + c_4` is the khronon **acceleration** coupling — a *vector/foliation* quantity (the coefficient of `a_μ a^μ`, `a` the khronon acceleration).
- **Route B:** the open number is `α_1 = 4η`, where `η` is the **directed-flux** normalization — the coefficient of ED's vector current sector.

Both are the strength of the **same object: ED's directed bandwidth-flux (vector) sector.** Neither the conservative khronometric formulas (Route A) nor the scalar diffusion rule (Route B) can compute it, because both omit the vector dynamics — Route A by assuming a conservative action, Route B by reducing to the scalar band. The cross-check `η = -c_{14}` is therefore **not yet evaluable**; it is a *consistency target* for once the vector sector exists, and it correctly identifies what to build.

> **The entire open falsification number of the ED gravity line is the coupling strength of one unbuilt piece of the dynamical rule: the directed (vector) bandwidth-flux sector. Two independent derivations confirm this is the single missing ingredient.**

## 5. The stakes — what the conservative limit implies (flagged, not a verdict)

If the directed-flux sector turns out to drag the local frame near a moving source at `O(1)` strength — the generic acoustic expectation (`η = -1`, `c_{14} = O(1)`) — then the *conservative* `α_1 = O(1)`, far above `|α_1| ≲ 10^{-4}`. ED would then be a generic, observationally-excluded preferred-frame theory **unless** the dissipative reserve supplies a suppression of `~10^4–10^5` in the near-field functional `𝒮(Γ)`. So the honest framing of the stakes:

- the conservative skeleton points toward `α_1 = O(1)` (dangerous);
- ED's survival rests **entirely and heavily** on the dissipative-reserve suppression `𝒮(Γ)` being very large in the near-field;
- whether the dissipative mechanism can deliver `~10^4–10^5` of suppression is **the** open question, and it could come back either way. This is a genuine falsification pressure, not a reassurance.

*(This is conditional on `η = O(1)`, which is itself what the vector-sector build must determine — the coupling could be structurally small. No verdict; the stakes are stated honestly.)*

## 6. Verdict (this session)

**The `η` cross-check is set up and pushed to its obstruction, which is the useful result.** The acoustic matching is clean and derived (`ρ_f = 1`, `c_s = b`, `Ω = 1/b`, `g_{0i} = -v_i/b`); but `η` is **not computable from the scalar rule**, because that rule's current is curl-free (pure gauge for `g_{0i}`). The physical cross-term requires the **directed-flux (vector) sector** of `F` — declared by P05's directionality, deferred by the metric-assembly note, built by no round. **Route A's `c_{14}` and Route B's `η` are the same quantity: the coupling of that one unbuilt sector**, which neither the conservative formulas nor the scalar rule can reach. The cross-check `η = -c_{14}` becomes evaluable only after the vector sector is constructed. The number is not computed and not faked; what is delivered is the precise location of the single missing ingredient, confirmed from two directions, plus an honest reading of the stakes (the conservative skeleton leans `α_1 = O(1)`, putting the whole burden on the dissipative suppression).

## 7. Next — build the directed-flux (vector) sector of `F`

1. **Construct the vector law** for the directed bandwidth flux `J^i` (continuity + a transport/relaxation law from P05 directionality and the P11 reserve drain `\tilde Γ`), as an admissible extension that introduces no new primitive — the same status as the scalar rule.
2. **Extract its solenoidal response** to a source moving at `w`: this gives the physical `g_{0i}`, hence `η`, hence the conservative `α_1, α_2`.
3. **Evaluate the cross-check `η = -c_{14}`** — Route A and Route B must agree; disagreement signals an error in one.
4. **Fold in the reserve `\tilde Γ`** to get `𝒮(Γ)`, and compare to the bounds. The moving-binary simulation now also needs this vector sector (a scalar-only sim gives `g_{0i} = 0`), so the build is the shared prerequisite for both the analytic and numerical closes.

---

*The `η` cross-check, pushed to its obstruction. Acoustic matching of ED's emergent metric is clean and derived: `ρ_f=1`, `c_s=b`, `Ω=1/b`, `g_{0i}=-v_i/b`. But the scalar rule's current `J_b=-D∇b` is curl-free ⟹ pure gauge ⟹ the scalar rule sources NO physical `g_{0i}` and cannot determine `η`. The preferred-frame cross-term lives in ED's directed-flux (vector) sector — P05's transport directionality, deferred by the metric-assembly note, built by no round. Route A's khronon-acceleration coupling `c_{14}` and Route B's directed-flux normalization `η` are the SAME quantity: the coupling of that one unbuilt vector sector; both routes independently reduce the whole open number to it, and the cross-check `η=-c_{14}` is its consistency condition. Conservative skeleton leans `α_1=O(1)` ⟹ ED's viability rests heavily on the dissipative suppression `𝒮(Γ)` (~10^4–10^5 needed if `η=O(1)`) — honest falsification pressure, no verdict. Next: build the vector sector. No corpus edits, no new primitives; Einstein not derived; the number deliberately not faked.*
