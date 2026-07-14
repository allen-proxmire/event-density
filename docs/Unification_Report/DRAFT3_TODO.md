# Unification Report — deferred to draft 3

Draft 2 = what we finished in the 2026-07-12 pass. This file holds work intentionally deferred.

## 1. Salvage the khronometric λ<1/3 healthy-branch bound

**Cut from draft 2.** The claim "ED sits on the healthy Hořava branch, `λ < 1/3`, `λ ≠ 1` — not GR at the scalar level" was removed from the report (§5 subsection, §5 falsifiable-edge + debts bullets, the §2 scorecard Gravity-status add-on, the abstract clause). The Gravity box keeps its ✅ (GR-I..IV + khronon MOND/DE — canonically sourced); only the λ add-on came out.

**Why:** the bound is in **no canonical paper**. `Paper_GR-II` leaves the scalar-mode speed *open*. The only corpus derivations are the working note `event-density/foundations/Khronometric_Lambda_HealthyBranch_FromStandingKeystone.md` and the **quarantined** `remove from repo/gravity-reinvention-2026-07-09/…`. A headline scorecard claim can't rest on that. (Claude B adversarial review, finding #1.)

**The physics (standard Hořava, sound):** `K_ijK^ij − λK² = shear² + (1/3−λ)K²`; ghost-free scalar needs `(1/3−λ)>0 ⟹ λ<1/3`. GR is `λ=1`, ghost-free only because full 4-diffeo makes the mode non-propagating; ED breaks 4-diffeo (propagating khronon, GR-II) so it can't use that escape ⟹ healthy branch. Exact λ inherited (F-dependent).

**Salvage plan:**
1. Promote the working note into a **canonical published gravity paper** (a "GR-V," or a GR-II/KM addendum).
2. Re-add to the report at **structural-argument** tier — *not* a §14 weapon (nothing to measure; exact λ is inherited).
3. Cite the canonical paper, not the working note.

**The gate (must clear before salvage is real, needs a GR-literate check):** does the heuristic ghost step — "the coefficient `(1/3−λ)` must be positive" — survive the **full Hořava scalar-mode stability analysis** (complete quadratic action, gradient terms, real propagator; standard healthy region is `λ<1/3` *or* `λ>1`)? If yes, salvage is solid. If it's an oversimplification, the claim isn't real yet. This is the deciding check.

Full detail: memory `project_lambda_bound_salvage_draft3`.

## 2. "Entanglement is Pre-Spatial" — a short synthesis paper (optional, high-interest)

**The claim is already in the corpus; the technical bridge is not yet made explicit.** Join the pre-individuation account of entanglement (`entanglement/Paper_072_IndividuationRegime` + `primitives/concepts/individuation.md`) to the emergent-metric machinery (`gravity/Paper_MetricFromTheGraph_ForcedTo3D`): *the metric separation of the endpoints is a committed-structure quantity; a pre-individuated pair has no such separation, which is why it reads nonlocal.* One clean statement unifying **072 + individuation + MetricFromTheGraph + 071 (ER=EPR echo): entanglement is pre-spatial because space is what commitment builds.**

**Honest caveat (keep it falsifiable):** entangled chains still sit at substrate loci (`u` in P02) — they have index positions. What's undefined pre-commitment is the *emergent metric* separation, not location itself. So it is **pre-metric**, precisely, not "nowhere."

Full detail: memory `project_entanglement_prespatial_paper`.

## Report edits SHIPPED to EDG (commit `1d667ba`, 2026-07-12)

- **Entanglement promoted to its own scorecard box (13th, under QM)** + a new **§4 subsection**: closed arc 063–070 + Bell–Tsirelson + the pre-individuation interpretation (Paper_072) + ER=EPR echo (Paper_071), honestly tiered. Box counts reconciled to thirteen.
- Fixed the **§3 arena/space language**: the metric and the boundary between systems are emergent; only the bare index/adjacency (P03), dimension (P06), and grain scale (P08) stay primitive.

Still draft-3-pending: the **"Entanglement is Pre-Spatial" paper** (§2 above) and the **λ salvage** (§1 above).
