# §12 — Internal Consistency: the anomaly question, split honestly

*Draft v1, 2026-07-10. Register: peer-facing. Tiers: charge-conservation face **solid** (measured, B4); clean-substrate baseline **solid** (this session's vector theorem); nontrivial chiral cancellation **inherited**; the one non-inherited possibility a **candidate, T4-gated**. A "forced anomaly-freedom" claim was made and retracted this session; the honest status is the split below. Point-toward. Primary sources (read-first): `Anomaly_State_After_CleanVectorTheorem_2026-07-10`, `Paper_ChargeAsTopology_B4`, `Paper_CleanSubstrateVector` §6.*

---

**The arrow's job here.** Two of the arrow's results feed this section. Its parity-cleanness makes the clean substrate vector (§9), which fixes an anomaly-free baseline. And the anomaly-relevant non-Hermiticity, the thing a genuine chiral anomaly would live in, is the worldline arrow itself (a point-gap spectral flow). So the arrow both sets the safe baseline and is where the one open question lives.

Gauge anomaly cancellation is the deepest internal-consistency requirement of a chiral gauge theory: the gauge current must stay conserved at the quantum level, and in the Standard Model this works only because of a striking numerical balance among the hypercharges. The honest question is what ED contributes to this, and the answer is not "ED forces it" — an earlier version of that claim was overreached and corrected this session. The answer is that the question splits, exactly the way the chirality casting did, into a solid side and an inherited side, with one narrow open candidate.

## The solid side

Two pieces are secure.

**Charge conservation.** The charge-as-topology result (§8) gives an exact integral Gauss law, circulation `= 2πw`, loop-independent, to machine precision. An exact Gauss law is exact gauge-charge conservation, which is the substrate statement of anomaly-freedom for the charge sector. (Read with B4's own caveat: the winding is Σ-blind and weakly coupled, so this is analytic, and reading the exact Gauss law as anomaly-freedom is an interpretive step on top of the measured conservation, taken here.)

**The clean baseline.** A gauge anomaly requires chiral content — left and right contribute with opposite sign, and a vector-like theory cancels automatically. §9's theorem is that the parity-clean substrate is vector for every channel-count. So the clean substrate carries no chiral spectral flow, and there is nothing there to threaten the exact Gauss law. **The clean baseline is anomaly-free, trivially and provably** (at the transport level, contingent on the substrate-to-Dirac descent, like the theorem it rests on).

## The inherited side

The Standard Model's anomaly cancellation is *nontrivial*: the theory is chiral, and its consistency depends on the special balance `ΣY = 0` and `ΣY³ = 0` per generation, the condition that ties the quarks (times three colors) to the leptons. This is one of the Standard Model's most striking just-so facts, and a grand unified theory like SO(10) explains it by putting a generation in a single **16**.

In ED, the chiral content appears only after the spontaneous symmetry breaking of §9, and *which* chiral content it is, is the inherited casting (the pseudoreality of SU(2), the same rep-spectrum wall as §7). So the nontrivial cancellation is **inherited along with the content**. ED does not independently derive why the emergent chiral content is anomaly-free; that rides in with the representation spectrum it inherits.

## The one open candidate

ED's characteristic move is to force a *constraint*, not a *value*, and there is exactly one place it might do so here. B4's Gauss law is *exact*. If that exact charge conservation must survive the arrow's chiral spectral flow, then the substrate would **forbid** a gauge anomaly by construction — forcing *that* whatever chiral content emerges is anomaly-free, without ever selecting *which* content. That would be a genuine, non-inherited ED contribution to the deepest consistency condition in particle physics.

It is a candidate, not a result, and it is gated. Establishing it requires the substrate-to-Dirac worldline reduction (T4, §10), because a gauge anomaly is properly a relativistic object and the spectral-flow face lives there. The operator triage is complete — the anomaly-relevant non-Hermiticity is specifically the worldline arrow, and every off-worldline candidate (the V1 kernel, V5, the Lindblad effective Hamiltonian) was checked and ruled out for a distinct reason — so the question is correctly located, but the reduction that would answer it is the one deep arc still open in the matter sector. The candidate is named, not claimed.

## The correction, on the record

This section exists partly to state a retraction plainly. An earlier note this session argued that ED *forces* anomaly-freedom, by reading B4's classical winding-protection as quantum anomaly-freedom. That conflated two different things: an anomalous theory also has a classically conserved current, so classical winding-protection does not discriminate anomaly-free from anomalous content. Adversarial review caught it, and it contradicted `Paper_CleanSubstrateVector` §6 from the same day. The claim was downgraded to the candidate above. The reason to foreground this rather than bury it is that it is the report's honesty discipline working as designed: the retraction is why the anomaly box is a gated candidate and not a false ✅.

## Scope

- The conservation face and the clean baseline are solid; the nontrivial chiral cancellation is inherited; the "constraint-forcing" possibility is a T4-gated candidate.
- All of it is at the transport/structural level; the relativistic anomaly proper is gated on the substrate-to-Dirac reduction.
- ED does not derive the Standard Model's anomaly cancellation. The section maps the question to its honest floor.

## What this buys the report

The anomaly box is the report's second genuine structural open (#3), and it is smaller and better-located than #1. Its solid pieces are real (exact conservation, a provably vector baseline), its inherited piece is the same rep-spectrum wall the rest of the Standard Model quarter inherits, and its one non-inherited possibility is precisely gated on the T4 reduction that also gates §9's relativistic chirality and §10's graph-native spinor. So the two deep matter-sector arcs, the anomaly constraint-face and the substrate-to-Dirac descent, are one arc, named honestly and left open.

---

*Draft notes for finalization:*
- *Do NOT restore any "ED forces anomaly-freedom" language — that is the retracted overclaim. The box is a gated candidate. This is the single most important tier discipline in the section.*
- *Keep the split explicit (solid conservation + clean baseline / inherited chiral cancellation / gated candidate) — it mirrors §9's casting split and should read as the same shape.*
- *The retraction paragraph is deliberate and should stay — but state it plainly (what happened + why it matters), not as drama. It models the discipline; it is not a confession.*
- *T4 gating language must match §9 and §10 exactly (same substrate-to-Dirac arc behind all three).*
- *Length ~950 words. Register OK: ΣY³=0, spectral flow, point-gap, SO(10) 16, Lindblad named flat-out.*
