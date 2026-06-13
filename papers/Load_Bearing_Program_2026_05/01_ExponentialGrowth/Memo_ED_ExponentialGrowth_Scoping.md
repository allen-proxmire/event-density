# Memo_ED_ExponentialGrowth_Scoping — Scoping Memo for Load-Bearing Derivation #1

**Series:** Wave-3 Scoping Memo (Cosmology Arc; inflation sub-thread; load-bearing derivation #1 from Memo_ED_CosmologyAndDynamics_ResearchDirections §4)
**Status:** Substrate-graph scoping of whether $\dot a \propto a$ (the exponential-growth condition characteristic of standard inflation's Hubble-parameter regime) can be derived from existing ED substrate content. Closure would upgrade Paper_ED_Cos_01 audit row 13 OPEN → D-via-I; reframe inflation's horizon-resolution from "primarily SCBU inheritance" to "SCBU + substrate-graph exponential-extension contribution." **Not a derivation. Not a generative paper. No new primitives proposed.**
**Date:** 2026-05-16
**Anchors:** Paper_ED_Cos_01 (Inflation; row 13 OPEN); Paper_073 (DCGT); Paper_089 (V1 retarded kernel); Paper_090 (V5 cross-chain); Paper_093 (T18 kernel-arrow); Paper_012 (P-RB-1 substrate-c); Paper_ED_SC_4_9 (substrate-action saddle Hessian); Paper_ED_CCC §3.7 (post-SCBU ignition regime); Memo_ED_CosmologyAndDynamics_ResearchDirections §4 (load-bearing derivation #1).

---

## §1 The OPEN item

Paper_ED_Cos_01 audit row 13:

> *Substrate-graph derivation that substrate-c-bounded region-growth produces **exponential** (not linear) scale-growth — requires $\dot a \propto a$ mechanism not currently constructed.*

Without this closure, Paper_ED_Cos_01's substrate-c-bounded region-growth gives at most LINEAR scale-growth $a(t) \sim t$, not the exponential $a(t) \sim e^{Ht}$ characteristic of standard inflation's Hubble regime. The paper currently acknowledges this honestly: primary horizon-resolution falls on SCBU inheritance (§3.6), and the GR-side $H$ cannot be directly mapped onto substrate-c-bounded region-growth without closing this derivation.

Closing row 13 would upgrade Paper_ED_Cos_01 M2 → M3 retroactively and supply ED with a genuinely-exponential-growth substrate-graph mechanism for inflation — closer parity with standard inflation cosmology phenomenology.

---

## §2 What "exponential growth" requires substrate-graph

The mathematical content of $\dot a \propto a$ is that the rate of scale-factor increase is proportional to the current scale factor. Equivalently: each substrate "unit volume" contributes to scale-factor growth proportional to itself — feedback / amplifying / branching structure where existing extent drives further extent.

Standard cosmology: in de Sitter (vacuum-energy-dominated) regime, $\rho_{\mathrm{vac}}$ is constant; Friedmann $H^2 = (8\pi G/3)\rho$ gives constant $H$; $\dot a/a = H$ constant gives $a \propto e^{Ht}$. The constancy of $\rho_{\mathrm{vac}}$ as $a$ grows is the load-bearing GR-side property.

**Substrate-graph translation:** for exponential growth, the substrate must supply a quantity that stays constant (or grows proportionally) as the unbalanced-saddle-Hessian-signature region expands. Without such a quantity, growth is bounded by substrate-c and is at-most-linear.

Three structural patterns could supply exponential growth at substrate-graph level:

**(P1) Branching / amplifying boundary expansion.** Each substrate locus reaching the unbalanced regime starts contributing to outward propagation. Total propagation rate scales with total unbalanced volume; total volume growth $\dot V \propto V$ → exponential.

**(P2) Self-reinforcing diffusion-dominated regime.** $\Gamma_{\mathrm{diff}}$ scales with current expansion-dominant axis content; as more substrate enters the unbalanced regime, $\Gamma_{\mathrm{diff}}$ increases proportionally, accelerating further expansion.

**(P3) Substrate-graph non-Euclidean coarse-graining.** DCGT's substrate→continuum bridge translates substrate-graph propagation to continuum-side scale-factor evolution non-trivially. The continuum-side $a(t)$ may scale exponentially even when substrate-graph propagation is substrate-c-bounded, via the geometry of DCGT's coarse-graining map.

---

## §3 Candidate substrate-graph mechanisms

### Candidate 1: Branching boundary expansion (P1)

The unbalanced-saddle Hessian-signature pattern propagates outward via V1 at substrate-c. As each locus enters the unbalanced regime, its V1 starts propagating the pattern further. If the total V1-propagation-rate of the unbalanced-region boundary scales with the volume of unbalanced substrate already present, growth is exponential.

**Substrate-graph plausibility:** structurally analogous to a chain reaction. Plausible in principle. Each unbalanced locus contributes to its neighborhood's V1 transport; many unbalanced loci together produce a substrate-graph reinforcement.

**Obstruction:** in flat 3D geometry, boundary surface area scales as $a^2$ while interior volume scales as $a^3$. Boundary expansion is driven by boundary loci (surface), not interior. Surface-to-volume ratio scales as $1/a$ → boundary contribution per unit volume drops as $a$ grows → growth becomes sub-linear, not super-linear.

Unless the substrate-graph has dimensional structure where boundary loci contribute disproportionally (e.g., long-range V1 reach via Paper_089 finite-width supporting non-local boundary contributions across the substrate region), this candidate produces sub-exponential growth.

**Status: requires substrate-graph derivation that V1's finite-width supports super-linear-in-volume boundary expansion. Currently OPEN.**

### Candidate 2: Self-reinforcing diffusion rate (P2)

In the diffusion-dominated regime, $\Gamma_{\mathrm{diff}} > \Gamma_{\mathrm{prod}}$. If $\Gamma_{\mathrm{diff}}$ at a locus scales with the local expansion-dominant Hessian content (more unbalanced substrate = more diffusion), then $\Gamma_{\mathrm{diff}}$ amplifies as the unbalanced region grows. The substrate-side expansion rate $\dot a$ then increases proportionally with $a$.

**Substrate-graph plausibility:** would require a substrate-graph derivation that $\Gamma_{\mathrm{diff}}$ at a locus depends on the substrate's local Hessian state, not just on V1+V5 kernel parameters. Per Paper_073 DCGT, $\Gamma_{\mathrm{diff}}$ is bounded above by substrate-c — its dependence on local state is more subtle.

**Obstruction:** DCGT supplies $\Gamma_{\mathrm{diff}}$ as a substrate-graph quantity bounded by V1 finite-width × P04 bandwidth content. It is not currently substrate-side-derived to scale with local Hessian content. The corpus's DCGT formulation has $\Gamma_{\mathrm{diff}}$ as approximately substrate-parameter-determined, not substrate-state-determined.

**Status: would require an extension of DCGT to state-dependent diffusion rates. Currently OPEN.**

### Candidate 3: DCGT non-Euclidean coarse-graining (P3)

The substrate→continuum bridge via DCGT is regime-conditional (A→regime hydrodynamic-window scale-separation per Paper_073 + ED_MEMORY anchor). Within this window, substrate-graph propagation at substrate-c maps to continuum-side propagation, but the *geometric* details of the map depend on the DCGT prescription.

If DCGT's coarse-graining naturally produces non-Euclidean continuum geometry — e.g., a substrate-graph configuration where the coarse-grained metric content is itself responsive to the unbalanced-saddle pattern — the continuum-side scale-factor evolution may be exponential even when substrate-graph propagation is at most substrate-c-bounded.

**Substrate-graph plausibility:** non-trivial. Requires DCGT to produce continuum-side metric content that "expands more rapidly" as more substrate enters the unbalanced regime. Standard DCGT in the hydrodynamic window produces approximately-flat continuum geometry (consistent with FRW cosmology); the regime where DCGT produces inflation-like exponential coarse-grained geometry is structurally distinct.

**Obstruction:** DCGT operating in the saturation regime is itself in a non-standard regime (substrate event-density very high; A→regime hydrodynamic-window conditions stressed). Whether DCGT supplies exponential coarse-grained geometry in this regime is substrate-research-frontier work.

**Status: requires substrate-graph derivation of DCGT's behavior in the saturation regime. Currently OPEN.**

### Candidate 4: Substrate-graph dimensionality effect

If the substrate-graph effective dimensionality changes during the saturation regime — e.g., the unbalanced-saddle region has effectively higher-dimensional substrate-graph connectivity (more loci connected per substrate-c step) — boundary expansion could outpace flat-geometry expectations.

**Substrate-graph plausibility:** speculative. Would require V1+V5 substrate-graph structure to produce dimension-effective shifts in the saturation regime.

**Obstruction:** no substrate-graph content in the corpus currently allows for dimension-effective shifts. Paper_098_5 / T1 forces $D = 3+1$ structurally.

**Status: not currently substrate-graph supported. OPEN; lowest priority.**

---

## §4 Negative observation: substrate-c-bounded gives at-most-linear in flat geometry

The cleanest substrate-graph reading of Paper_ED_Cos_01 §3.4: V1 retarded propagation carries the unbalanced-saddle pattern outward at substrate-c. In flat substrate-graph geometry (the default), a region's boundary advances at substrate-c → boundary position scales as $r(t) = ct$ → linear.

For exponential scale-factor growth, the substrate-graph needs to supply one of:

- A feedback mechanism where existing unbalanced volume contributes to further expansion proportionally (Candidate 1, 2, 4)
- A non-Euclidean substrate-to-continuum map where flat substrate-graph propagation produces exponential continuum coarse-graining (Candidate 3)

None of these currently closes from existing primitives. **The default substrate-graph reading is at-most-linear scale-growth.**

If this is accepted as the honest substrate-graph state:

- Paper_ED_Cos_01's framing of "primary horizon-resolution via SCBU inheritance" (§3.6) is the cleanest reading.
- Inflation in ED supplies the post-boundary ignition-phase transition dynamics (substrate scale grows at-most-linearly via V1 propagation) without contributing exponentially to horizon resolution.
- The GR-side Hubble parameter $H$ does not have a direct substrate-graph correspondence under substrate-c-bounded propagation; the GR-side identification is approximate or requires DCGT's non-Euclidean contribution (Candidate 3).

**The honest negative finding: substrate-c-bounded substrate-graph propagation in default-flat substrate geometry gives at-most-linear scale-growth, not exponential.** Exponential growth requires substrate-graph mechanism not currently in the corpus.

This is parallel to the chirality cascade's central negative finding (substrate is chirality-symmetric at substrate-graph level). Both arise from the same structural pattern: the corpus's substrate content is "too symmetric" or "too direct" to supply specialized features that standard cosmology / standard physics treats as load-bearing.

---

## §5 What closure would require

For exponential-growth row 13 to close at substrate-graph D-via-I:

**Path-1 (Candidate 1 closure):** substrate-graph derivation that V1 finite-width supports super-linear-in-volume boundary expansion. Would require examining Paper_089's V1 kernel structure carefully and identifying any feedback/branching mechanism in V1 retarded support. Plausibility: low-medium.

**Path-2 (Candidate 2 closure):** substrate-graph extension of DCGT to state-dependent diffusion rates. Would require examining Paper_073 DCGT and identifying whether $\Gamma_{\mathrm{diff}}$ admits state-dependence. Plausibility: medium.

**Path-3 (Candidate 3 closure):** substrate-graph derivation of DCGT's behavior in the saturation regime, producing exponential coarse-grained geometry. Plausibility: medium-low; substrate-research-frontier.

**Path-4 (Candidate 4 closure):** dimension-effective shifts. Plausibility: very low (contradicts T1).

**Path-5 (accept linear growth):** acknowledge substrate-graph reading is at-most-linear; reframe Paper_ED_Cos_01 to drop any inflation-side exponential-growth claims; lean entirely on SCBU inheritance for horizon resolution. **This is the honest current state.**

---

## §6 IDENTIFIED vs OPEN

### IDENTIFIED:

- **Exponential growth is not derivable from substrate-c-bounded substrate-graph propagation in default-flat geometry.** Substrate-graph default reading gives at-most-linear scale-growth.
- **Three candidate mechanisms (P1, P2, P3) are structurally distinguishable** and each could supply exponential growth if their substrate-graph derivations close. Currently none close from existing primitives.
- **Paper_ED_Cos_01's "primary horizon-resolution via SCBU inheritance" framing (§3.6) is the cleanest reading under the honest substrate-graph state** — does not depend on exponential-growth closure.

### OPEN (load-bearing):

- **Path-1, Path-2, Path-3 closures** all require substrate-graph derivations not in the corpus.
- **The GR-side Hubble parameter $H$ substrate-graph correspondence** — currently OPEN. Either $H$ maps to substrate-c-bounded linear-growth rate (mismatch with standard cosmology phenomenology), or $H$ maps to a substrate-graph quantity not yet identified.

### Cross-arc impact:

- If Path-2 closes (state-dependent DCGT), the closure affects multiple cosmology-arc and dynamics-arc papers, since DCGT is upstream of every continuum-level result in the corpus.
- If Path-3 closes (saturation-regime DCGT), it adds a new regime to Paper_073 and may upgrade Paper_ED_CCC §3.7 ignition-phase content.
- The substrate-research-frontier work is high-value if any path closes.

---

## §7 Recommended next steps

**Three honest paths (non-prescriptive):**

**Path-α (Pursue Path-2):** focused construction memo attempting state-dependent DCGT extension. Most-leverage potential closure (DCGT is upstream of much of the corpus). Risk: substrate-research frontier, may not close.

**Path-β (Pursue Path-1):** focused construction memo examining whether V1 finite-width supports super-linear boundary expansion. Lowest-extension required (uses V1 as currently constructed). Risk: most likely to yield a clean negative result quickly.

**Path-γ (Accept linear, reframe Paper_ED_Cos_01):** honest acknowledgment that substrate-graph reading is at-most-linear; reframe inflation paper to make this explicit. Closes row 13 by **flagging it as substrate-research-frontier requiring ontology extension** rather than attempting substrate-graph derivation. Verdict stays M2.

**My recommended next step:** Path-β first (lowest investment; likely fast negative result). If Path-β confirms linear-only behavior, proceed to Path-α (state-dependent DCGT extension as the most-leverage substrate-research direction). If both yield negative results, fall back to Path-γ (honest reframe).

**Parallel to baryogenesis cascade pattern:** scoping memo → focused construction memo → audit/comparison → eventual reframe of arc paper if closure fails. Estimated 3–5 memos to settle the row 13 OPEN item honestly.

**Cross-arc note:** even if all paths yield negative results, the substrate-research finding ("substrate-graph propagation gives at-most-linear scale-growth in default-flat geometry") is **substantively informative**. It tells us that ED's substrate ontology has structural limits that standard cosmology's GR-side inflation framework exceeds — the substrate is "leaner" than GR's inflaton+potential machinery and produces leaner cosmology phenomenology unless ontology-extension routes (Candidates 1–3) close.

This would be a substrate-ontology-discipline finding worth its own corpus contribution: "ED's substrate-graph cosmology gives at-most-linear inflation-phase expansion; horizon-resolution falls on SCBU inheritance not exponential extension; the corpus is structurally leaner than GR-inflation and the empirical match must absorb the linear-vs-exponential difference (probably via SCBU's strong scale-collapse contribution)."

---

**End Memo_ED_ExponentialGrowth_Scoping.**
