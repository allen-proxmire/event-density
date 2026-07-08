# Arc: V5 Forward-Derivation — can the attractive sign be DERIVED (not assumed)?

**Opened 2026-07-08** at AP's direction, after P12-Coh Step 4 (winner-selection-active) supplied the missing piece. Crank-rail ON. This is the trap-arc with the worst over-read history in the program (the Tsirelson reduction was retracted; four+ passes of the envelope-shape thread were downgraded). The single hardest discipline here: **do not read into Paper_090 what it did not build.** Every identification below is a hypothesis to TEST on the substrate, not a claim inherited from the source.

---

## Why now

The 2026-07-07 forward thread (banked in RelationalTick §7) diagnosed the real blocker as upstream: "the attractive sign is a necessity condition, not derived, and the deeper reason is that P12-Coh had no operational definition." Step 4 (2026-07-08) removed that blocker: P12-Coh is now operationalized as the coherence content of the participation superposition, and build-verified to be (a) dynamically operative (it decides ~half of growth choices) and (b) finite-reach / Knots-safe under quenched substrate disorder. So the question the whole V5 keystone reduces to can now be asked concretely: **is V5's cross-chain coupling the same coherence content, applied across two chains?** If yes, V5's attractive sign is inherited from "coherence rewards alignment" rather than assumed.

---

## The ledger: what Paper_090 already gives vs what it leaves open

Read directly from `physics-papers/wedges/Paper_090_V5Kernel.md` (2026-07-08), not from memory.

**Already derived-conditional (do NOT re-derive; cite):**
- **Existence.** §1.1 (line 31): V5 is "not a free-standing postulate... a rule-type the substrate carries given the 13 primitives + V1 inheritance: P10 opens room for kernel rule-types beyond V1; P02+P04+P05+P07+P09 supply the inter-chain correlation-transport mechanism; P11 + V1's retardation supply the causal-direction constraint." So V5's existence is a P10-licensed kernel, on the same footing as V1. This stays a posit in the same sense V1 is: licensed, not forced. The forward-derivation does NOT claim to derive V5 from nothing.
- **Retarded support.** §5.1 (line 148): the `θ(t_A − t_B)` support is "forced by the same P11 commitment-irreversibility argument that fixes V1's retardation" (Paper_093 T18). Retardation is already derived. The envelope-shape thread's earlier difficulty was about the temporal *profile* F_V5, not the retarded support, which is settled.
- **Gauge-covariant phase.** §4.3 (line 171): `K_V5 → e^{i(α(u_A) − α(u_B))} K_V5` under U(1), from P05 (connection) + P09 (polarity). The phase that enters the kernel is the P09 relative phase between the two chains, transported by the P05 connection. This is the exact object Step 2-4's probes used (P09 phase + P05 holonomy).
- **Finite memory / reach.** §2 (line 90): `K_V5 = θ(t_A−t_B) F_V5( σ(u_A,u_B)/ℓ_V5², (t_A−t_B)/τ_V5 )`. Finite ℓ_V5, τ_V5. Structural form; the VALUES are inherited (§3, line 141).

**Left genuinely open (the free pieces):**
- **The SIGN of the coupling.** F_V5 is a general envelope. Nothing in Paper_090 fixes whether the coupling is attractive (synchronizing) or repulsive. The synchronization characterization (`V5_Synchronization_Characterization.md`) established attractive is a NECESSITY condition (needed to bind composites) but assumed it as an input. This is the target.
- **The envelope shape F_V5** (temporal + spatial profile). Open (the envelope-shape thread; the trajectory-not-field framing is the right one, still open).

So the honest target is narrow and real: **derive the attractive SIGN** (and, as a bonus, supply a *mechanism* for the finite reach, not its value). Existence, retardation, and the gauge phase are already conditional-derived in 090; the values stay inherited.

---

## The move (what Step 4 enables)

Two chains A, B participating on a shared channel / overlapping substrate region superpose their participation amplitudes `P^A = √b_A e^{iπ_A}`, `P^B = √b_B e^{iπ_B}` (Paper_063's joint amplitude `Ψ^AB`). The **coherence content** of that cross-chain superposition is the interference cross-term
`Coh_AB = |P^A + P^B|² − (b_A + b_B) = 2√(b_A b_B) cos(π_A − π_B)`,
whose phase dependence is exactly `cos(π_A − π_B)`, i.e. the modulus of the same gauge-covariant relative phase `e^{i(α_A − α_B)}` that Paper_090 §4.3 puts in K_V5. `Coh_AB` is **maximal when the phases align** and falls to zero / negative as they separate.

**The hypothesis (H-V5-Coh):** V5's cross-chain coupling is (the phase-dependent part of) `Coh_AB` — the coherence content of the cross-chain participation superposition. If so:
- **Attractive sign FORCED.** A coupling that extremizes coherence pulls π_A → π_B (alignment raises Coh). This is the synchronizing sign, and it is not put in by hand: it follows from "coherence rewards alignment," which Step 4 build-verified is dynamically operative on the certified substrate. The sign Paper_090 left open is filled.
- **Finite reach gets a MECHANISM.** Step 4: the P05 connection carries quenched substrate disorder, which random-walks the transported relative phase and holds the coherence-order to a finite correlation length ξ, robustly even when the coupling is causally active. Identify ℓ_V5 with that ξ. The VALUE stays inherited (set by the connection strength κ and the disorder variance), but the finiteness now has a substrate mechanism rather than being a bare structural stipulation.

Net if H-V5-Coh holds: V5 = a P10 cross-chain kernel (existence, licensed) whose phase is the P05/P09 gauge phase (090 §4.3), whose retardation is P11-forced (090 §5.1), and whose **sign is forced attractive by being the coherence content of the cross-chain superposition** (new), with a finite reach mechanism from quenched disorder (new), value inherited. That reduces V5's free pieces from {existence, sign, reach-mechanism, values} to {existence (P10 posit, as for V1), values (inherited)} — a real advance on target A2.

---

## The load-bearing gap + honest checks (crank rail)

- **G1 (the crux): is V5's coupling THE coherence content, or merely LIKE it?** Paper_090 writes F_V5 as a *general* envelope; it does NOT write it as an interference modulus `2√(b_A b_B) cos Δπ`. Identifying the two is an ADDED reading. This is exactly the error class that sank the Tsirelson attempt (reading a specific structure into a source that only stated a general one). Therefore H-V5-Coh must be **tested as a substrate hypothesis**, not asserted from 090. The test: does the coherence content, used as the actual cross-chain coupling with its sign NOT assumed, reproduce V5's required behavior (attractive local synchronization + finite reach)? If it does, that is positive substrate evidence for the identification; it is still not a theorem that 090's F_V5 must be this. State it at that tier.
- **G2 (transfer): single-chain → two-chain.** Step 4 tested the coherence term on ONE growing front (coherence among a front's committed neighbors). V5 is genuinely two distinct chains. The decisive build must put the coherence coupling BETWEEN two chains and check the sign/reach there, not assume Step 4 transfers.
- **G3 (retardation): mostly closed by the source.** 090 §5.1 forces retarded support from P11. The remaining envelope-*shape* question is separate and stays open; it is not needed for the sign result.
- **G4 (existence stays a posit).** V5's existence as a kernel is P10-licensed, not derived-from-nothing, exactly as V1's is. The forward-derivation explicitly does NOT close this and must say so.

---

## The decisive first build (proposed)

Reuse `v5_substrate_coupling_probe.py` — it already builds a real cross-chain V5 term in the certified substrate and shows finite-reach local synchronization (nearby chains lock into a shared proper time, distant chains stay free). BUT its coupling is a hand-put rate term `A_V5 · (x_target − x_i)` with the attractive sign PUT IN BY HAND. That assumed sign is the gap.

**Build:** replace the hand-put coupling with the **coherence-derived** coupling. Give each chain a P09 phase; couple two chains by having each front's advance/dwell decision include the cross-chain coherence content `Coh_AB` of the overlapping-region superposition (reach-weighted by the P05 connection over transverse distance, retarded via last-step state). Crucially, **do not put a sign in**: the coupling is "extremize coherence," and whether that synchronizes (attractive) or anti-synchronizes (repulsive) is READ OFF, not assumed. Then test:
1. **Sign (the headline):** does the coherence coupling drive nearby chains toward a *shared* rate (attractive) purely because coherence is maximal at alignment, with no assumed sign? If yes, V5's attractive sign is derived from P12-Coh.
2. **Finite reach:** with the quenched-disorder P05 connection (Step 4's mechanism), is the synchronization local (nearby lock, distant free = time dilation preserved), and does it collapse to a universal tick only when the reach exceeds the separation, matching the characterization?
3. **Falsifier:** if the coherence coupling comes out sign-ambiguous or repulsive, or cannot give local-without-global, H-V5-Coh fails and the attractive sign is NOT reducible to P12-Coh (a real negative, report it).

This build simultaneously answers the star-pulsation lead (does a genuine cross-chain phase coupling synchronize where shared-ρ failed, `Collective_Pulse_Results.md`) and the V5 sign question — same object.

**Tier discipline:** a positive result is "MEASURED substrate evidence that V5's attractive sign is the coherence content of the cross-chain superposition (H-V5-Coh), conditional on the identification G1." NOT "V5 derived." Existence stays a P10 posit; values stay inherited.

---

## Build 1 (DONE 2026-07-08) — the attractive sign EMERGES from P12's + Coh sign (MEASURED, conditional on G1)

`v5_coherence_coupling_probe.py`. Two clusters of 4 real certified chains on parallel lanes (real `compute_sigma` advance/dwell, route-2 memory-driven natural rates, genuine within-cluster rate spread + a cross-cluster rate gap = a time-dilation setup). Each front carries a U(1) gauge phase `φ = DPHI·(forward progress)` (090 §4.3). The ONLY cross-chain coupling is P12's coherence gradient entered into the certified selection Σ with P12's own `+` sign: `sig_adv += k_c5 · Σ_j w_ij sin(φ_j^ret + A_ij − φ_i)`, where `w_ij` = transverse reach `e^{−|dy|/ℓ_V5}` × longitudinal window, `A_ij` = quenched P05 holonomy. No hand-put attractive term. The `+` is P12's definitional sign (Σ = Coh − Str − Grad); whether it synchronizes is read off, not assumed.

**First attempt was a NULL, diagnosed, fixed (recorded honestly).** The initial coupling compared "my phase after each choice" to neighbors' frozen last-step phase, which at the aligned start rewards phase STASIS (holding still), not rate-matching: result was sign-independent (+k and −k both gave w/w0≈0.72, no directional effect). Root cause: a cos-difference-of-choices is the wrong discretization of "reward coherence" for a rate decision. Fix (principled, not a fishing tweak): use the coherence GRADIENT `Σ_j w_ij sin(φ_j−φ_i)` (the exact derivative of `cos` coherence w.r.t. φ_i), which points a phase-behind front toward advancing. Lowered DPHI 0.2→0.05 so the relative phase does not wrap during the transient.

**Result (gradient form, 3 seeds averaged, STEPS=2500, D=20):**

| condition | ℓ_V5 window | within-spread (w/w0) | cross-gap | reading |
|---|---|---|---|---|
| **P12 sign (+)** | 2–30 (`< D`) | 0.022–0.025 (**0.27–0.30**) | 0.21–0.24 (**preserved**) | **LOCAL lock, time dilation intact** |
| **P12 sign (+)** | 100 (`≥ D`) | 0.027 (0.32) | **0.036 (collapsed)** | universal tick (finiteness load-bearing) |
| **SIGN-FLIP (−)** | all | 0.062–0.065 (0.74–0.78) | ~0.21 | **no lock at any reach** |
| **(+) + quenched disorder** | 2–30 | 0.023–0.025 (0.27–0.30) | preserved | local lock, robust to disorder |

**What this shows (headline).** V5's required attractive local-synchronization signature (nearby chains lock to a shared proper-time rate while distant clusters keep their rate gap; collapse to a universal tick only when reach ≥ separation) EMERGES from a cross-chain coupling that is nothing but P12's coherence gradient with P12's own `+` sign. **Flipping to `−Coh` destroys binding at every reach** — the decisive control: the attraction is tied specifically to P12's reward-coherence sign, not to the coupling machinery or the reach structure. So the attractive sign Paper_090 leaves open, and which `V5_Synchronization_Characterization.md` had to ASSUME, is instead inherited from P12: given the identification H-V5-Coh, V5 must be attractive because P12 rewards coherence and coherence is maximal at phase alignment.

**Honest scope / what it does NOT show (crank rail).**
- **G1 unclosed.** This is substrate evidence FOR H-V5-Coh (V5's coupling = the coherence content), not a theorem that Paper_090's general envelope `F_V5` must be the interference modulus. 090 writes `F_V5` general; identifying it with `Coh` remains a hypothesis, now supported by a working substrate realization + a passing sign control.
- **Existence stays a P10 posit** (like V1); **ℓ_V5's value stays inherited** (here it is the free reach knob; the substrate only fixes that finite-reach gives local-without-universal, not the number).
- **Modeling choices, flagged:** the U(1) clock `φ = DPHI·progress` with advance-steps-the-clock; instantaneous-with-one-step-retard coupling (the θ-support shape is separately 090/P11-forced, not tested here); coherence entered as its gradient (the correct continuous form, but a choice). The sign-independent w/w0≈0.72 residue in the flipped/short-reach runs is a small uniform coupling perturbation, distinct from the real lock (w/w0→0.27 with the gap preserved and the sharp ℓ_V5≈D transition).

**Net for target A2.** V5's free pieces reduce from {existence, attractive sign, reach mechanism, values} to {existence (P10 posit, as for V1), values (inherited)}: existence + retardation + gauge phase were already 090-conditional; the **attractive sign is now derived (conditional on G1) from P12's reward-coherence structure**, build-verified, with a passing sign-flip control and robustness to quenched disorder. Tier: **MEASURED**, conditional on H-V5-Coh.

**Next (bank or push):** (1) close/tighten G1 — check directly whether 090's `F_V5` phase-part can be written as the cross-chain interference modulus, from 090 §4.3 + Paper_063's Ψ^AB, at the algebra level (the crank-critical step; do NOT over-read); (2) propagate to `V5_Synchronization_Characterization.md` (sign reclassified assumption→derived-conditional) and the open-targets map (A2 narrowed); (3) optional: retardation-shape variant and a larger fleet. This also resolves the star-pulsation lead (`Collective_Pulse_Results.md`): a genuine cross-chain phase coupling DOES synchronize where shared-ρ did not, and it is the P12-coherence coupling.

---

## G1 (DONE 2026-07-08) — CLOSES to forced-conditional: 090's own gauge law forces V5's coupling to be the coherence content

Read verbatim: Paper_090 §3.1 (kernel), §4.3 (gauge law); Paper_063 §3.1-3.3 (joint amplitude), §P09 note. The question: is V5's phase-dependent coupling THE coherence content `√(b_A b_B) cos Δπ`, or merely like it?

**The structure in 090.** The V5 correlation is `⟨X^A(u_A,t_A)·Y^B(u_B,t_B)⟩_V5 = ∫ K_V5 · Q^{AB}_{X,Y} dμ` (§3.1, line 104). `K_V5 = θ(t_A−t_B) F_V5(σ/ℓ_V5², Δt/τ_V5)` is the REAL, bounded, retarded envelope (the reach/memory part). The phase-carrying object is the cross-chain participation content `Q^{AB}`, because §4.3 requires the whole correlation to transform as
`K_V5 → e^{i(α(u_A) − α(u_B))} K_V5` (a DIFFERENCE phase). *(090 loosely writes this on the real envelope K_V5; a real envelope cannot carry a phase, so the phase must live in the participation content Q^{AB} it multiplies. Resolving 090's own looseness the only internally-consistent way, not an over-read.)*

**The fingerprint: difference phase ⟹ conjugated-pair moment.** With per-chain U(1) polarity `P^C = √b_C e^{iπ_C}`, `P^C → e^{iα(u_C)} P^C` (P09). Then:
- conjugated pair `P^A (P^B)^* → e^{i(α_A − α_B)} P^A (P^B)^*` — DIFFERENCE phase ✓ matches §4.3 exactly.
- the joint-amplitude PRODUCT `P^A P^B` (Paper_063's Ψ^{AB}, §3.2 boxed) → `e^{i(α_A + α_B)}` — SUM phase, a DIFFERENT object.

So 090's §4.3 difference-phase is the signature of a **two-point correlation / conjugated amplitude-pair moment** `⟨P^A (P^B)^*⟩` (propagator structure), NOT the joint-amplitude product. Its gauge-invariant real part is
`Re[P^A (P^B)^*] = √(b_A b_B) cos(π_A − π_B)`,
which is exactly the coherence content `Coh_AB = |P^A + P^B|² − b_A − b_B = 2√(b_A b_B) cos Δπ` (up to the factor 2). This is the coupling Build 1 used (`cos Δπ`, gradient `sin Δπ`).

**Verdict: G1 closes to FORCED-CONDITIONAL.** V5's phase-dependent coupling IS the coherence content of the cross-chain superposition, forced by 090's §4.3 gauge law, conditional on three pre-existing commitments (none invented for this result):
1. **§4.3 gauge law** `e^{i(α_A − α_B)}` — stated verbatim in 090.
2. **Bilinear cross-chain content** — V5 "acts on pairs of chains" (090 §3.2); 063 §3 builds the bipartite content from `P^A_K, P^B_L` (`Ψ^{AB}_{KL} = P^A_K P^B_L + Δ^{AB}_{KL}`, the product piece marked P-Bipartite-Mapping, a corpus postulate). So the content is bilinear in the two amplitudes.
3. **Conjugated-moment / like-chain reading** — that V5 is a two-point correlation between like chains (⟨P^A P^{B*}⟩, standard propagator), which selects the difference structure `cos Δπ`. A formal alternative consistent with the same gauge law — opposite-charge chains with a product `P^A P^B` giving `cos(π_A + π_B)` — is physically EXCLUDED because it is maximal at anti-alignment (`π_A = −π_B`) and would ANTI-bind, contradicting V5's binding role. So the like-chain correlation reading is selected by V5's function, not assumed arbitrarily.

**This is a far weaker and cleaner dependency than the retracted Tsirelson attempt.** That needed ±1-involution operators + a commuting tensor split + a bipartite Born bridge, none of which 063 builds. G1 needs only 063's Ψ^{AB} (which 063 DOES build) + 090's gauge law + the standard correlation reading — all present in the sources, no operator algebra invented. It uses only what the papers actually state.

**Net for the arc.** Build 1 showed the attractive sign emerges from P12's `+Coh` with a passing sign-flip control. G1 shows the identification behind it (V5's coupling = the coherence content, H-V5-Coh) is not a free hypothesis but is forced by 090's own gauge law, conditional on the bipartite-bilinear content (P-Bipartite-Mapping) and the like-chain correlation reading. Therefore: **V5's attractive sign is DERIVED (forced-conditional) from P12's reward-coherence structure.** The remaining honest residuals are (a) 090's §3.1 loosely attributes the gauge phase to the real envelope (resolved by consistency), (b) the bilinearity rests on P-Bipartite-Mapping (a postulate, not primitive-derived; but pre-existing, not invented here), (c) the intermediate integral `dμ` could dress the leading two-chain term (minor). Tier upgrade: the sign moves from Build 1's "MEASURED, conditional on an untested identification" to "**MEASURED + the identification is gauge-law-FORCED, conditional on P-Bipartite-Mapping + the like-chain reading**." Existence stays a P10 posit; ℓ_V5, τ_V5 stay inherited.

**Upgrades the old "suggestive" note.** `project_v5_kernel_characterization` line 22 had 090 §4.3's gauge law as "suggestive, not probative" that the kernel is moment-shaped. G1 upgrades it: combined with the requirement that V5's content is bilinear cross-chain participation, the conjugated-pair moment is the UNIQUE such object with that transformation (up to the physically-excluded opposite-charge product), so §4.3 is forcing, not merely suggestive.
