# Arc: Does P12's Coherence Term Reward Phase Alignment? (Scoping)

**Opened 2026-07-08** at AP's direction. The convergence target: this one question is the shared bottleneck of three arcs. Crank-rail ON (trap-zone: this is exactly where "everything clicks" over-reads happen).

**The question, precise.** Is the P12 coherence functional `Coh` *higher when participating phases align* (rewards alignment) or *indifferent to phase* (phase-neutral)? Since `Σ = Coh − Str − Grad` and chains extremize `Σ` (`a = −∇Σ`), "rewards alignment" means aligned phase is dynamically favored.

**Why it matters (the convergence).** Cracking this in the "rewards alignment" direction discharges, simultaneously:
- **MOND's constructive sign** (`cos Θ_LH ≈ +1`, gravity-enhancing) — the one residual of the Interference-Gravity paper.
- **V5's attractive/synchronizing sign** — a necessity condition in RelationalTick, not derived.
- **P12-Coh operationalization** — named the shared upstream fork in RelationalTick + the open-targets roadmap.
- **Model C** (the quadratic strain reading) — `Coh = |Σ P|²` is the same object.
Three independent sign-residuals + one strain-reading, one move.

**Candidate mechanism.** With the canonical amplitude `P_K = √b_K e^{iπ_K}` (P04+P09, Paper_001), the "coherence content" of a multi-source superposition on a channel is the phase-dependent interference part,
`Coh = |Σ_a P_a|² − Σ_a|P_a|² = 2 Σ_{a<b} √(b_a b_b) cos Δπ_ab`,
which is zero at random/orthogonal phase and maximal at alignment. A functional named "coherence" that rewards alignment is what "coherence" *means* given the amplitude structure. This is also exactly Model C's off-diagonal.

---

## Step 1 (DONE) — the wall is down; the phase-rewarding Coh is permitted, needed, and natural, but it is a rule extension, not forced

The apparent blocker was the certified simulator's Σ orientation-blindness (hard invariant, `sigma.py:3-7`) and the "Knots, Not Crystals" invariant. A trace (2026-07-08) shows it does **not** forbid a phase-rewarding `Coh`, for three independent reasons:

1. **Wrong object.** The sim's inert "orientation (B5)" is a **spatial/relational director** (transverse relational direction, helicity-adjacent; `Phase_B_ArchitecturalSpecification.md:42`, `Phase_OrientationPrimitivity_Resolution.md:50`), NOT P09 polarity (the rule-vs-flow phase `π_K`). `tension_polarity.md:28` separates them ("Not handedness or helicity. … Polarity is the phase of the whole rule against the external flow"); the B5→P05/P09 mapping is flagged **"WEAK"** (`B4_Related_ED-I_Material.md:15,26`). A phase-rewarding `Coh` targets P09, a *different channel* the blindness invariant does not govern. **(The V5 investigation and the earlier framing conflated B5 with P09; that conflation was the wall.)**
2. **Wrong scale.** "Knots" forbids only a **long-range ordering coupling** (kind 3, `C(r)→const`). It is "a structural reading confirmed by measurement, not a theorem" and "not proved for all rules" (`Paper_BlindnessInvariant_KnotsNotCrystals.md:16`). V5 binding and MOND interference are **finite-reach**, giving finite-correlation-length structure, not true long-range order.
3. **Not canonical.** The sim's phase-blindness is a **tractability reduction**: "Current ED-Arch is single-rule-type; no explicit polarity … a polarity-extended simulator would instantiate two rule-types distinguished by phase" (`tension_polarity.md:154`). The Σ-blindness "corrupts *this evaluation*" (`sigma.py:3`), i.e. is scoped to the certified rule, not asserted for all rules.

**Positively needed (consilience).** At least two independent sectors require exactly this functional: V5 "must be attractive/synchronizing" (`V5_Synchronization_Characterization.md:36`, reclassified from assumption to necessity) and the MOND sign is "plausibly P12 Coh rewarding alignment" (`QuadraticStrain_NewtonMOND_Scoping.md`). RelationalTick names it the upstream fork. Baryogenesis *wants* it but does not independently prove it (weaker, OPEN).

**Natural.** "Coherence content" = interference part = maximal at alignment (candidate mechanism above). The certified `Coh = −(ρ−ρ*)²` is a density-target, not a coherence measure; arguably mislabeled.

**HONEST LIMIT (crank-rail; corrects the trace's slightly-too-quick "local read = permitted").** A phase-*alignment reward* is an **aligning coupling**, not a local-stabilizing penalty. It is Knots-safe **only if finite-reach** (an infinite-reach version WOULD produce the forbidden long-range order). And adopting it is a **rule extension** (a finite-reach, P09-phase-reading `Coh`), well-motivated and permitted, but **not forced** from the certified substrate. It is also **untested**: every certified build-and-run result runs on the phase-blind rule.

**Step-1 status:** the question is cracked **open, not shut.** No written result forbids a finite-reach phase-rewarding `Coh`; it is needed and natural. But it is an operationalization + rule extension, and its behavior is unverified. "Does Coh reward phase alignment?" → *under the natural operationalization, yes, and that forces the three signs; but the operationalization must be finite-reach and must be build-and-run confirmed.*

---

## Step 2 (DONE 2026-07-08) — the build: phase-Coh REWARDS alignment (confirmed); finite-reach is REGIME-CONDITIONAL (crystallizes in the clean limit; Knots-safe only under disorder/multi-nucleation)

Built `p12_phase_coherence_probe.py` (working repo): a polarity-extended rule on the CERTIFIED Σ-engine. The ρ-dynamics use `compute_sigma`/`compute_candidates`/`apply_tiebreak`/`NodeState.commit` verbatim; an added P09 phase channel deposits, at each node's first commit, the phase that MAXIMIZES a finite-reach term `Coh_phase(v)=Σ_{w committed,|v−w|≤ℓ} e^{−d/ℓ}cos(π_v−π_w)` (maximizer = mean-field angle = Σ-maximization of the phase term). 60×60 grid.

**Results:**
- **(a) Rewards alignment — YES.** Control (coherence off, random phases): `R_global=0.016` (=1/√N, no order), `C(r)≈0` at all r. Coherence on: strong local order, `C(r=1)` up to +0.9. The Σ phase term demonstrably drives alignment.
- **(c) Certified ρ-dynamics unchanged — YES.** The phase channel never writes ρ; the control commits all 3600 nodes with the certified rule at zero phase-order, confirming the ρ-side is the certified rule.
- **(b) Finite-reach — REGIME-CONDITIONAL (the key finding).** A finite-reach phase-alignment reward is a *genuine ordering coupling* with an order-disorder transition:
  - **Clean/coherent limit (single seed, no noise): CRYSTAL.** `R_global=1.000`, `C(r)=+1.000` at ALL r out to 25 — perfect long-range order = exactly the Knots kind-3 the substrate is supposed to lack. So the phase-Coh is NOT automatically Knots-safe; under coherent single-front growth it crystallizes.
  - **Realistic regime (40 seeds): DOMAINS, finite-reach.** `R_global≈0.22–0.27`, `C(r)` decays to ~0 by r≈8–12 (ξ≈5–8, growing modestly with ℓ). No global crystal; local stiffness + phase-domain walls (defects) = the Knots-permitted "not crystals" picture.
  - **Order–disorder transition:** single-seed deposition noise crosses ordered (noise 0.3: R=0.89) → finite-reach (noise 0.8: R=0.26). XY-type, as expected for an aligning coupling.

**Verdict.** The phase-Coh **rewards alignment (confirmed)** and leaves the certified ρ-rule intact. But finite-reach/Knots-safety is **not a free property of the term**: it is a real ordering coupling that crystallizes in the coherent limit and stays finite-reach (domains+defects) only under multi-nucleation/disorder. Crucially, that disordered/multi-front regime is exactly where **RelationalTick found native ED lives** (native dynamics do NOT globally synchronize). So the constructive/attractive sign (MOND, V5) **is available from a phase-Coh** and **is Knots-safe in the regime ED actually occupies** — but finite-reach is *conditional on ED's disorder*, not an unconditional guarantee, and a hypothetical coherent-single-front limit WOULD crystallize.

**Reframed residual.** The open question is no longer "does Coh reward alignment" (yes) but "does ED's own dynamics keep the phase-order finite-reach (domains) rather than crystalline" — which RelationalTick's no-global-sync result already answers affirmatively for native ED, but which this probe imposed via multi-seed rather than derived from the substrate's intrinsic disorder.

**Honest limits / follow-ups.** (i) The probe deposits a *pure* mean-field copy; whether ED's *intrinsic* ρ-disorder (irregular front paths, ρ-weighting) alone breaks the single-seed crystal with no added noise is the natural next probe (would upgrade "Knots-safe under imposed disorder" to "Knots-safe natively"). (ii) Winner-selection was left certified (phase passive on ρ); a variant with the phase term in winner-selection would test ρ-perturbation. (iii) 3D vs 2D (true long-range order is easier in 3D).

## Step 3 (DONE 2026-07-08) — intrinsic disorder breaks the crystal: the phase-Coh is finite-reach NATIVELY (Knots-safe). The crack closes.

`p12_phase_coherence_probe_v2_intrinsic.py`: same certified ρ-engine + P09 phase, but the phase is transported across each edge with a P05 CONNECTION (holonomy) tied to the substrate's INTRINSIC disorder — quenched bandwidth heterogeneity `A(w→v)=κ_bw(bw−1)` and/or the substrate's own ρ-field `A=κ_ρ(ρ_w−ρ_v)`. Single seed, NO imposed thermal noise.

**Results:**
- **Baseline (κ=0, trivial/flat connection, pure copy): CRYSTAL** (R=1.000, C(r)=+1.00 to r=25) — the Step-2 artifact reproduced.
- **Bandwidth-holonomy (quenched intrinsic disorder), κ_bw=0.5→2.0: FINITE-REACH.** R → 0.16→0.03; C(r) decays with correlation length ξ≈4–6 (κ=0.5) shrinking to ξ≈2 (κ=2.0).
- **ρ-holonomy (homogeneous grid, purest intrinsic — only the substrate's OWN ρ-field): FINITE-REACH.** κ_ρ=0.5 → R=0.064, ξ≈4–5; κ_ρ=1.0 → ξ≈1–2; κ_ρ=2.0 → ξ<1 (fully disordered). Even with NO imposed heterogeneity, the certified dynamics' own ρ-accumulation disorder breaks the crystal.

**Verdict — the crack closes favorably (MEASURED).** A phase-rewarding P12-Coh gives **finite-reach** phase-order (Knots-safe "not crystals": short-range stiffness + defects, not long-range order) **natively**, because the P05 connection carries the substrate's intrinsic disorder, which random-walks the phase to a finite correlation length. The forbidden crystal appears ONLY for a **trivial (substrate-blind) connection** (κ=0), which is unphysical (P05 IS the substrate's connection). Robust across two independent disorder sources and a range of connection strengths; single seed, no imposed noise.

**What this discharges (conditional on the operationalization, now build-verified):**
- **MOND's constructive sign** (Interference-Gravity residual) — a finite-reach constructive phase-Coh.
- **V5's attractive/synchronizing sign** — the finite-reach phase-Coh IS the finite-reach attractive coupling V5 needs (RelationalTick's local-not-universal binding).
- **P12-Coh operationalized** — the participation-superposition coherence content, phase-based, finite-reach via the P05 connection.
- **Model C grounded** — `Coh = |Σ P|²`.
- **Knots preserved** — finite-reach, not crystal.

**Honest tier + value-inheritance + caveat.** Tier: **MEASURED** (build-verified on the certified engine) that a phase-rewarding, connection-carrying Coh is finite-reach. The *operationalization* (reading P12-Coh as the finite-reach participation-superposition coherence) is natural + permitted + needed + now-verified, but remains an operationalization (form-forced conditional), NOT a theorem from nothing. The correlation length ξ (= V5's ℓ_V5, MOND's reach) is **value-inherited** (set by κ and disorder variance): form-forced-finite, value-inherited — the standard ED pattern. **Caveat — a window:** too-weak a connection (κ→0) crystallizes; too-strong (κ_ρ≳2) gives ξ<1 (no binding). Useful finite-reach binding lives in the intermediate window where ℓ_V5 sits.

**Bottom line for the convergence:** one operationalization of P12-Coh discharges the MOND and V5 sign-residuals and grounds Model C, build-verified and Knots-preserving. The arc's core question is answered: **yes, Coh rewards phase alignment, and the resulting order is finite-reach natively (Knots-safe); the crystallization risk exists only for an unphysical substrate-blind connection.**

**3D hardening (DONE 2026-07-08, `p12_phase_coherence_probe_3d.py`).** The load-bearing stress test: genuine long-range order is easier in 3D (XY: quasi-order in 2D, true LRO in 3D), and physical space is 3+1 (P06). **Result: the finite-reach result is ROBUST to dimensionality.** 28³ grid, single seed, no imposed noise. Trivial connection (κ=0) → CRYSTAL (R=1.000, C(r)=+1 to r=18) — the ordering tendency confirmed (if anything stronger). Intrinsic disorder → FINITE-REACH: bandwidth-holonomy κ_bw=0.5 → ξ≈3–4; ρ-holonomy (homogeneous) κ_ρ=0.5 → ξ≈2–3. If anything ξ is **shorter** in 3D than 2D at the same κ (more neighbors → more disordered-path averaging → faster decorrelation). The "3D XY has LRO" intuition does NOT apply, because this is not an equilibrium XY model but a one-shot **irreversible** deposition in which phase accumulates holonomy along growth paths (a ~1D random walk along paths, roughly dimension-independent). So the crystallization risk is confined to the unphysical trivial connection in BOTH 2D and 3D; the physical (substrate-coupled) connection gives finite-reach in both. **The irreversibility of commitment (P11) is what makes it robust — the deposited phase never relaxes, so there is no thermal ordering transition.** Crack hardened.

**Possible next (bank or push):** (1) write it up as a standalone EDG paper ("Phase-Coherence in P12: the Attractive Sign, Finite-Reach, from the Substrate's Own Disorder"), now 2D+3D verified; (2) propagate the discharge to the Interference-Gravity paper (§9 residual) and RelationalTick §7 (V5 sign); (3) the winner-selection-active variant (phase term perturbs ρ) — the one remaining stress test.

---

## (superseded) Step 2 as originally planned — the decisive build: a finite-reach P09-phase coherence term

The first *build* in this line. Implement a finite-reach, P09-phase-reading coherence term in `Σ` on the certified substrate (a polarity-extended rule) and measure:
- **(a) Attractive/constructive:** do co-participating chains dynamically favor phase alignment (does the added `Coh` term drive `cos Δπ → +1`)? This is the V5 attractive sign and the MOND constructive sign, tested directly.
- **(b) Finite-reach / Knots-safe:** does the resulting phase order have a *finite correlation length* (`C(r)` decays), i.e. short-to-medium-range stiffness, NOT forbidden long-range order (`C(r)→const`)? Sweep the reach; confirm order dies beyond it.
- **(c) Certified results survive:** rerun the load-bearing certified probes (or a representative subset) with the phase term on; confirm nothing that depended on phase-blindness breaks (or characterize exactly what changes).

Deliverable if it passes: P12-Coh operationalized as a finite-reach phase-coherence term (measured), discharging the MOND and V5 signs and grounding Model C. If it fails (e.g. produces long-range order, or does not give net alignment), the phase-`Coh` is refuted as-posed and the signs stay irreducible additions.

**Crank notes.** (i) Do NOT present the phase-`Coh` as the certified rule; it is an honestly-named polarity-extended rule (per `tension_polarity.md:154`, Knots §4). (ii) Test the real simulator, not a hand-built Kuramoto stand-in (the V5 probes used a Kuramoto abstraction; this must be the certified Σ-rule with a genuine P09 channel added). (iii) The finite-reach constraint is load-bearing: an infinite-reach aligning term would violate Knots, so reach must be a swept parameter and order must be shown to die beyond it.
