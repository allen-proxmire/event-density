# T4 · Step 13 — Deriving the Bridge: the Lane-Reflection Coupling, Made into Operators, Grants Chiral *Capability* but Does NOT *Force* the Casting — N=1 Is Forced Vector, but N=2-chiral / N=3-vector Is Dynamical (Content), Not Geometric

**Foundations — T4 step 13. Attempts the one open piece from `T4_12`: derive that a fixed-point-free (N=2) lane-set *forces* chiral and a self-mirror (odd N) lane-set *forces* vector, by making "the coupling references γ⁵'s orientation factor" into explicit operators. Crank-rail ON, negatives held to the positive bar. RESULT: the construction is real and it does force **N=1 vector** (empty chiral sector), and it *derives AP's capability/selection split at the operator level* — but it does **NOT** force N=2-chiral vs N=3-vector: both are chiral-*capable*, so the geometry only grants **capability**, exactly matching rep theory's permissiveness. The casting *selection* is dynamical (the stability/attractor program, scope step 1), with no geometric shortcut. Honest verdict: the forcing bridge does not close; what closes is *why* it can't, and that is itself useful.**

## 1. What "derive the bridge" requires
`T4_12` left the coupling step *asserted*: "no middle lane ⟹ chiral." To derive it, make the pieces operators:
- **Parity of the substrate** acts on the fermion as `P = (spinor swap) ⊗ (lane reflection S)`, where `S: e_i ↦ e_{N+1−i}` reflects the lane arrangement. Both factors flip the **same** emergent-space orientation — the spinor part sends `γ⁵ = γ⁰·(orientation) → −γ⁵`, and `S` reverses the lane row. The substrate is **parity-clean**, so `P` is a symmetry (this is the input, established).
- **"The coupling references the orientation factor"** means the non-abelian (cross-channel, V5) coupling carries the spatial orientation on lane-space: a term `∼ (orientation) ⊗ M`, with `M` an `su(N)` generator acting on lanes.
- **Parity-cleanness forces a selection rule.** For `(orientation) ⊗ M` to be `P`-invariant, the orientation's sign flip must be absorbed by `S`: `S M S⁻¹ = −M`. **So the chiral (orientation-referencing) couplings are exactly the `S`-odd generators.** This is the bridge made precise: *chiral coupling ⟺ a nonempty `S`-odd sector of the gauge algebra.*

## 2. The count — S-odd sector dimension
`S` is an involution on the `N`-dim lane space; its `±1` eigenspaces have dimensions
`p = ⌈N/2⌉` (`+1`, the symmetric combos incl. the fixed middle lane for odd `N`) and `q = ⌊N/2⌋` (`−1`).
The `S`-odd operators (those with `S M S⁻¹ = −M`) are exactly the ones mapping the `+` eigenspace ↔ the `−` eigenspace: **`dim(S`-odd`) = 2pq`.**

| `N` | `(p, q)` | fixed middle lane? | `S`-odd (chiral-capable) coupling dim `2pq` | forced? |
|---|---|---|---|---|
| 1 | (1, 0) | yes (the lane itself) | **0** | **forced VECTOR** ✓ |
| 2 | (1, 1) | no | 2 | chiral-**capable** |
| 3 | (2, 1) | yes | 4 | chiral-**capable** |

*(Check, N=2: in the `S`-eigenbasis `S = σ₃`; `S`-odd generators are `σ₁, σ₂` — dim 2. N=3: 4 of the 8 `su(3)` generators are `S`-odd. Both nonzero.)*

## 3. What this forces, and what it does not
- **N=1 is forced vector — a genuine result.** With no cross-channel structure the `S`-odd sector is *empty*: there is no orientation-referencing coupling to build, so an abelian force cannot be chiral *through the orientation factor*. EM (a residual, orientation-type U(1)) is vector — consistent. *(Caveat, not over-built: a U(1) could still be chiral through the **arrow** factor `γ⁰` rather than the orientation — which is plausibly how hypercharge, the global P09 phase that references the arrow, is chiral while EM is not. Flagged as a consistency, not claimed as derived.)*
- **N=2 vs N=3 is NOT forced.** Both have a **nonempty** `S`-odd sector (dims 2 and 4) → both are chiral-**capable**. The geometry does not force N=3 vector; at most it would make the middle-lane component locally symmetric, leaving the outer lanes chiral-capable — i.e. "partially chiral," which is *not* QCD's fully-vector character. **So the forcing bridge does not close.**

## 4. Why it cannot close — and the kernel that this delivers
Chiral-**capable** (a nonempty `S`-odd coupling sector) is **not** chiral-**forced** (that sector actually being populated by the fermion content). The geometry decides *whether a left/right coupling can exist at all*; it does **not** decide *whether nature turns it on*. And this is exactly rep theory's verdict (`T4_12`): vector-vs-chiral is permissive for every `SU(N≥2)` — a **content** choice. **The reflection geometry reproduces the permission structure precisely, and confirms it can do no more.** That agreement (ED geometry "capable for N≥2" = rep theory "permitted for N≥2") is a real internal-consistency check.

So the run **derives AP's capability/selection split at the operator level**, which is the durable gain:
- **Capability = geometric.** Nonempty `S`-odd sector. Empty for N=1 (forced vector), nonempty for N≥2 (a genuine L/R exists to couple to). This *is* AP's "does the highway have a left and a right lane" — now an operator statement, and correct.
- **Selection = dynamical.** *Which* chiralities the stable fermion content populates (both → vector, one → chiral) is **not** fixed by the reflection. It is the stability/attractor question — scope step 1–2. AP's own "why drive on the right" (contingent selection) sits here, one level deeper than he placed it: not just *which* handedness, but *whether* the chiral sector is filled at all.

## 5. Net verdict and where this points
**The forcing bridge does not close: lane geometry grants chiral capability (and forces only the N=1 vector case), but the N=2-chiral / N=3-vector casting is a dynamical content-selection fact, not a geometric one.** Reported straight — this is a negative on "geometry forces the casting," and it is held to the positive bar.

Its value is threefold and real: (1) it **forces N=1 vector** and pins EM's vector character to an empty cross-channel sector; (2) it **derives AP's capability/selection split as operators**, promoting his metaphor from analogy to a precise statement (capability = `S`-odd sector, permissive for N≥2); (3) it **validates the scope's ordering** — the most promising geometric shortcut to the casting provably yields only *permission*, so the casting genuinely has **no shortcut** and must come from the stability dynamics (scope step 1). Every prior shortcut to the matter-content has failed the same way; this one fails *legibly*, telling us exactly which half is geometric (capability, done) and which is dynamical (selection, the real remaining program).

**Concrete next move:** the casting is now provably a *selection-among-capable* problem, so the honest next brick is **scope step 1 — the stability-condition formalism** (which stable fermion attractors populate one vs both `γ⁵` eigenspaces per channel-count). The geometry has handed off everything it can; the rest is the dynamics of the happening.
