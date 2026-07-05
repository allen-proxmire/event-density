# Four-Band Dependency Check — Does the Mass Sector Rest on the Archived Structure?

**Run:** 2026-07-05, following the dwell-mass retraction (`Dwell_Question_Answer.md`), which established that the four-band P04 partition (internal/adjacency/environmental/commitment-reserve) is **not canonical** — canonical P04 (`Paper_087`) is a bare non-negative additive scalar, and the four-band split comes from an **archived** M-series forcing paper. The open question the retraction raised: **Arc M's σ_τ mass functional and the Arc Q Higgs scoping both use the four bands — do the mass sector's actual results depend on the archived structure, or does it stand on canonical single-scalar P04?**

## Verdict: NOT load-bearing. The mass sector survives canonical P04. Fix is presentational.

The four-band structure is a **summation index and a decorative label** across Arc M, Paper_113, and the Higgs scoping. None of the surviving mass-sector results depend on there being four bands. Collapse P04 to its canonical single scalar and everything of substance stands.

### Where the four bands enter, and why each is not load-bearing

**Arc M (`papers/Arc_M/paper_arc_m.md`):**
- σ_τ = ℏ·√( **Σ_X** w_τ^X ⟨(∂_μ ln b_τ^X)(∂^μ ln b_τ^X)⟩ ), X ∈ {int, adj, env, com}. The four bands are **only the summation index.** Collapse to one band: σ_τ = ℏ√⟨(∂ ln b)²⟩. Every load-bearing property survives:
  - SC1 Lorentz-scalar (via ∂_μX ∂^μX) — survives.
  - SC2 amplitude-invariance (via the log-derivative) — survives; single-band log-derivative is still blind to b→αb.
  - SC3 energy dimension (via ℏ) — survives.
  - SC4 band-additive — becomes **vacuous** (trivially satisfied with one band). This is the only SC that referenced the bands, and it carries no result.
  - SC5 vanishing / massless slots — **MR-P** (gauge masslessness) comes from the rule-type's gauge-invariant **L3 interface**, **MR-R** (chiral masslessness) from the **internal-index chirality** (Weyl projection). Both are P07 rule-type structure, not P04 bands. Survive untouched.
  - SC6 Case P/R — bilinear choice, not bands. Survives.
- **Theorems M1 (σ_τ form) and M2 (massless slot FORCED via GRH)** — neither invokes the band count. Survive.
- The **one** place the bands do real work is the **M-Order-2** candidate ("rule-types with w^com = 0 have smaller σ_τ" — commitment-band-dominance). It is explicitly an **inequality, not a ratio**, part of the L-R ratio sweep that concluded "no strong ratio claim survives." Non-load-bearing, and it didn't pan out.
- P07 lever **L1 = "bandwidth partition w_τ^X"** classifies rule-types partly by band-weights. Used only in the same speculative ratio sweep (L-R5 "bandweight pattern"), which found nothing surviving. Not load-bearing.

**Paper_113 (`relativistic-qm/Paper_113`):** ties mass to **"P04 bandwidth-budget"** — the rest-frame scalar bandwidth content ("substrate-cell budget ... × c² = rest energy"). This is canonical single-scalar P04. **No four-band dependence.** Audit row 1 is "P04 bandwidth (P)," not a four-band claim.

**Arc Q Higgs H2:** names a condensate "in one of the four-band components (b^env or b^adj)." The mechanism it needs is a **spatially-patterned bandwidth field**, which the single canonical scalar b already provides. The band label is decorative. (And E1 already showed H2 does not ground on the substrate regardless.)

## The one real problem: a presentation over-claim

Arc M §2 states **"Primitive 04 (bandwidth): four-band decomposition b_K = b_K^int + b_K^adj + b_K^env + b_K^com"** — presenting the four bands **as** canonical Primitive 04. That is the archived/non-canonical structure cited as a primitive. The results don't depend on it, but the *framing* does over-claim the primitive basis. The same "P04 §1.5" four-band framing appears in the `position-paper` 13-primitive doc.

**Fix (presentation, not results):** in Arc M and the position paper, either (a) use canonical single-scalar P04 and write σ_τ with a single term (no band sum), noting that any decomposition is an optional Arc-M modeling refinement; or (b) keep the band vocabulary but explicitly flag it as a **non-canonical Arc-M refinement** (not Primitive 04), archived-M-2-derived, that no σ_τ / M1 / M2 result depends on. Either restores honest primitive sourcing without touching the mass results.

## Bottom line

Tonight's four-band retraction was correct **and** it does not damage the corpus's actual mass sector: σ_τ, Theorems M1/M2, the MR-P/MR-R massless slots, and Paper_113's mass-as-bandwidth-budget all stand on canonical single-scalar P04. The only debt is a presentation/citation correction (stop citing the four bands as Primitive 04). The hygiene flag in `docs/ED_Open_Targets_Map_2026-07-05.md` is downgraded accordingly: from "check whether the mass sector inherits the archived forcing" to "checked — not load-bearing; fix is a citation correction in Arc M + the position paper."
