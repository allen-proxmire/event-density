# Phase-3 GR — Pinning `κ, D`: the Rule's Coefficients from the Substrate Bands

**Foundations derivation — expresses the minimal rule's two coefficients in terms of the substrate, removing GR-III's "coefficients unpinned" caveat. Not a corpus edit, not a new primitive. Dry and entirely internal — and, honestly, it produces no new number: it reduces `κ, D` to inherited scales + postulated band fractions.**
The minimal dynamical rule is `ḃ = D∇²b − κρ` (GR-III §3): `D` the P02 adjacency-sharing rate, `κ` the P11 commitment-concentration sink. GR-III flagged both as unpinned minimal-model constants. This note pins them — and the honest outcome is that they are *not free*, but neither are they newly derived: they are fixed by the substrate scales (`c, ℓ_P`, inherited via `G`) and the dimensionless P04 band-partition fractions (postulated), with their physical ratio the Einstein coupling `8πG`.
**Crank rail:** express `κ, D` from what the primitives are; do not invent values. Where the result reduces to an inherited or postulated quantity, say so.

---

## 1. `D` — the P02 adjacency-sharing rate

The metric band `b` is a **reciprocal, shared** edge record (P02; `b_{ij} = b_{ji}`). Its equilibration across adjacency is the graph Laplacian, at a rate set by how much of the shared band exchanges per tick. In the continuum (`ḃ = D∇²b`), with edge length `ℓ_P` (P08 substrate scale) and tick `τ_P = ℓ_P/c` (the bandwidth-limit speed P03 fixes the tick from the length):

> `D = s_{02}\,\dfrac{ℓ_P²}{τ_P} = s_{02}\,c\,ℓ_P`,

where `s_{02}` is the **dimensionless per-tick sharing fraction** — a P02/P04 structural quantity (what fraction of the shared band equilibrates per tick). So `D` is the substrate transport scale `c\,ℓ_P` times a dimensionless band fraction.

## 2. `κ` — the P11 commitment-concentration sink

Each commitment removes a bandwidth quantum from the metric band, concentrating it into the matter channel (`commitment.md`). The sink rate per unit event density is

> `κ = k_{11}\,\dfrac{c}{ℓ_P}`,

where `k_{11}` is the **dimensionless commitment factor** (bandwidth-quantum-per-commitment × concentration efficiency; a P11/P04 structural quantity). (Dimensions: `κρ` is a rate `~ 1/τ_P = c/ℓ_P` times dimensionless `ρ`, `b`.)

## 3. The ratio `κ/D` is the Einstein coupling `8πG` (value-inherited)

The physical, scale-free combination is the ratio. The rule's steady state is `∇²b = (κ/D)\,ρ`. GR-I gives `g_{00} = −b = −(1+2Φ)`, so `b = 1 + 2Φ` and `∇²b = 2∇²Φ`; Newtonian Poisson `∇²Φ = 4πGρ` then forces

> `\dfrac{κ}{D} = 8πG` — **the Einstein field-equation coupling.**

So `κ/D = (k_{11}/s_{02})\,ℓ_P^{-2} = 8πG` (units `c = 1`), i.e. the dimensionless band-fraction ratio is pinned by Newton's constant: `k_{11}/s_{02} = 8πG\,ℓ_P²/c⁴ × …` — fixed by `G`, which is **value-inherited** (`G = c³ℓ_P²/ℏ`, Paper_027). This recovers, from the rule's coefficients directly, the `κ = 8πG` that GR-II/R9 obtained by Newtonian matching of the Lovelock form.

## 4. What is pinned, and what is not

| Quantity | Status |
|---|---|
| `D = s_{02}\,c\,ℓ_P` | substrate transport scale `c ℓ_P` × dimensionless `s_{02}` |
| `κ = k_{11}\,c/ℓ_P` | substrate rate `c/ℓ_P` × dimensionless `k_{11}` |
| `c, ℓ_P` (substrate scales) | **value-inherited** (via `G = c³ℓ_P²/ℏ`, Paper_027) |
| `s_{02}, k_{11}` (band fractions) | **P04/P02/P11 structure — postulated** |
| `κ/D = 8πG` (Einstein coupling) | **value-inherited** (Newton's `G`); recovers GR-II/R9 |
| any **new** number | **none** — `κ, D` reduce to inherited scales + postulated fractions |

## 5. Verdict

**`κ` and `D` are pinned — to inherited substrate scales and postulated band fractions — but no new number emerges, and that is the honest result.** `D = s_{02}\,c\,ℓ_P` (P02 adjacency-sharing) and `κ = k_{11}\,c/ℓ_P` (P11 commitment-concentration) are the substrate transport scales (`c ℓ_P`, `c/ℓ_P`) times dimensionless band/commitment fractions; their physical ratio is the **Einstein coupling `κ/D = 8πG`** — the bandwidth→metric conversion, which *is* Newton's `G` and is value-inherited (Paper_027), recovering the `κ = 8πG` GR-II/R9 got by Lovelock matching. So GR-III's "coefficients unpinned" caveat is **removed**: `κ, D` are not arbitrary — they are fixed by `G` (inherited) and the P04 band structure (postulated). But the exercise produces **no new derived value**: the dimensional part is the Planck scale (inherited via `G`), the dimensionless part is P04 postulate, and their physical ratio is Newton's `G`. It confirms the coefficients are *inherited + postulated*, not *free* — exactly the program's stance on constants.

**The honest payoff line.** This sets the dimensional **scale** (`G`) of the rule. It does **not**, by itself, deliver `α₁, α₂`: those are *dimensionless* PPN parameters set by the rule's dimensionless coupling structure (the band fractions, `ε = 0`) run through the khronometric PPN machinery — so pinning `κ, D` is necessary tidying, not sufficient for the falsification numbers. The "unpinned coefficient" worry is closed; the `α₁, α₂` computation still needs the dimensionless structure mapped to the khronometric couplings + the PPN apparatus.

---

*Pins the minimal rule's coefficients. `D = s_{02}\,c\,ℓ_P` (P02 adjacency-sharing rate) and `κ = k_{11}\,c/ℓ_P` (P11 commitment-concentration sink) are the substrate transport scales times dimensionless P04 band fractions; their physical ratio is the Einstein coupling `κ/D = 8πG` (value-inherited Newton's `G`, Paper_027; recovers GR-II/R9). GR-III's "coefficients unpinned" caveat is removed — `κ, D` are fixed by inherited scales + postulated band structure, not arbitrary — but no new number emerges: the dimensional part is inherited (via `G`), the dimensionless part is P04 postulate. Sets the rule's scale `G`; does not by itself give the dimensionless `α₁, α₂` (still PPN-machinery-gated). No corpus edits, no new primitives.*
