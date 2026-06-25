# #2b · Is the 4-D Survivor One-Handed? The Transport Route Fails; the Per-Commitment Route Unifies with Baryogenesis

**Foundations analysis + toy — attacks the open core ("is the 3+1D transport survivor genuinely chiral?") and develops AP's per-commitment route. Sim: `evaluation/ChiralGauge/chiral_percommit.py`. Two findings: (1) the *transport* route gives a **vector-like** survivor in 3+1D — the 1+1D chirality was dimension-special, a real partial-no; (2) AP's *per-commitment* route relocates the handedness to a winding of committed P09 phases, which is topological/robust (matching SQ1d), reduces entirely to whether the phase-advance sign is **locked**, and the lock is the **first-arrival mechanism ED's baryogenesis already needs** — so parity violation and the matter/antimatter asymmetry plausibly collapse to ONE handed-commitment lock-in. This reframes and *unifies* #2b with baryogenesis; it does not close it. The phase-winding → relativistic γ⁵ identification, and the first-arrival lock itself (an undischarged postulate, P-BinaryAdmission), remain open.**

**Crank rail.** Finding (1) is a negative I establish by standard lattice-fermion structure, not spin. Finding (2)'s toy is *schematic* — it demonstrates the *mechanism* (locked vs random phase winding), not that ED's actual commitment dynamics realize it; the identification "P09-phase-helix = relativistic chirality" is a hypothesis, flagged, not derived. The unification with baryogenesis is offered as a structural hypothesis with a named open core.

---

## 1. The 4-D transport survivor is vector-like (the open core, answered for the transport route)

SQ1e showed the arrow undoubles in 3+1D (16 → 1). The sharp question: is that single survivor *chiral* (one-handed, what the weak force needs) or *vector-like* (two-handed)? Look at what it is near the surviving point `p=0`:

> `D(p) = Σ_μ γ^μ (e^{ip_μ}−1) ≈ i Σ_μ γ^μ p_μ + O(p²)`.

The leading term is the **full four-component continuum Dirac operator** — all four `γ^μ`, both chiralities present (a massless Dirac point = L ⊕ R). The non-hermiticity sits in the `O(p²)` Wilson-like term, which lifts the *other* doublers but does not change the four-component structure *at* `p=0`. And the retarded forward-difference is, by construction, in the **Wilson class** — which is vector-like. So:

> **The 3+1D transport survivor is a vector-like Dirac point, not a chiral Weyl point.**

The 1+1D net chirality (SQ1c) does **not** generalize through the transport route. Why it looked chiral in 1+1D: there, the global non-hermitian point-gap winding *coincides* with the fermion's chirality (1+1D is special — chirality = directionality). In 3+1D the global non-hermitian invariant (a 3D point-gap object) is a *different* thing from the local γ⁵ chirality of the `p=0` point, and they decouple. **This is a real partial-no: the transport route to chirality is vector-like in the physical dimension.** Honest, and it redirects the whole effort.

## 2. AP's per-commitment route: handedness lives in the commitment, not the transport

AP's reframing — *handedness is a property of a commitment, so it's a count* — says: don't extract chirality from the continuum transport (which just failed); locate it in the commitment **events**. Model the handedness as the **winding of the P09 phase along the commitment sequence** — a helix/screw, whose pitch-sign is the handedness. Each commitment advances the phase; P11 adds randomization. The toy (`chiral_percommit.py`) computes the net winding per commitment:

| case | drift (lock) | P11 noise | net winding/step |
|---|---|---|---|
| **LOCKED**, strong noise | 0.30 | 1.0 | **+0.048** |
| **LOCKED**, tiny drift, strong noise | 0.05 | 1.0 | **+0.008** |
| **LOCKED**, huge noise | 0.30 | 5.0 | **+0.050** |
| **UNLOCKED** (random sign) | 0.30 | 1.0 | −0.0007 ≈ 0 |
| **UNLOCKED**, no noise | 0.30 | 0.0 | 0.000 |

The reading is clean and it mirrors SQ1d's topological robustness:

- **If the sign of the phase-advance is *locked* (every commitment screws the same way), there is a net winding — a handedness — and it is robust to P11 randomization** (the noise is a random walk `∼√N`; the locked drift accumulates `∼N`, so the net winding survives any amount of noise, even at tiny drift).
- **If the sign is *unlocked* (each commitment picks its own), the net winding is zero — vector-like** — regardless of noise.

So the per-commitment handedness reduces to **one** question: *is the sign of the commitment phase-advance globally locked?* Nothing else matters — not the drift magnitude, not the randomization strength.

## 3. The unification: parity violation = the baryogenesis lock-in

The thing that would lock the sign globally is a **first-arrival selection**: the first commitment picks a screw-handedness, and all subsequent commitments inherit it. **That is exactly the mechanism ED's baryogenesis arc already invokes** — the first-arrival lock-in that selects matter over antimatter (the `Memo_ED_BinaryChirality` / `P-BinaryAdmission` content). So:

> **Hypothesis (unification):** the weak force's parity violation and the universe's matter/antimatter asymmetry are *the same phenomenon* — one global handed-commitment lock-in. The universe picked a screw-handedness at first arrival; that single choice shows up as *parity violation* in the gauge sector (the phase-helix's handedness) and as *matter dominance* in the cosmological sector (the chain-arrow chirality). One lock-in, two faces.

This is a genuine structural consolidation. It explains, in one stroke, why both are *maximal/global* (a topological lock-in is all-or-nothing, §SQ1d), and it folds the unmapped #2b gap into an arc the corpus already has (baryogenesis), reusing its machinery instead of inventing new structure.

## 4. What is open (the honest core, now shared with baryogenesis)

The unification sharpens the open problem to two linked pieces — and both were *already* open in baryogenesis:

1. **The first-arrival lock itself is undischarged.** `Memo_ED_BinaryChirality` showed ED has *no native chain-typing ℤ₂* (R1/R2/R3 all failed); the binary/handed lock-in is currently the *postulate* `P-BinaryAdmission` (verdict M2). So "the sign is globally locked" is assumed, not derived. Closing #2b's chirality and closing baryogenesis's lock-in are now **the same open derivation** — which is good (one problem, not two) but it is still open.
2. **The phase-winding → relativistic γ⁵ identification is a hypothesis.** That the helical winding of the P09 phase along the arrow *is* the relativistic chirality (the γ⁵ Weyl structure coupling to gauge fields) is asserted, not shown. This is the relativistic bridge in a new guise — now phrased as "does the committed-phase helix coarse-grain to a γ⁵ chiral coupling?" rather than "does the transport." It is the cleaner question, but unproven.
3. **Anomalies (SQ3)** — still untouched, still the hardest.

## 5. Verdict

**Pushing on "is the 4-D survivor one-handed?" gives a clean two-part answer.** *Via the transport route: no* — the survivor is vector-like, and the 1+1D chirality was dimension-special (a real partial-no, established by standard lattice-fermion structure). *Via AP's per-commitment route: it can be* — handedness as the winding of committed P09 phases is topological/robust and reduces entirely to whether first-arrival globally locks the sign. And that lock is **the same mechanism baryogenesis needs**, so **#2b unifies with the baryogenesis arc: parity violation and matter/antimatter asymmetry are plausibly one handed-commitment lock-in.** This is real consolidation — the unmapped gap folds into an existing arc, reusing its machinery — but it is a *reframing*, not a closure: the lock-in is an undischarged postulate (`P-BinaryAdmission`, M2), and the phase-helix → γ⁵ identification is unproven. **The honest endpoint of the #2b sprint:** the gap is no longer "unmapped and possibly a wall"; it is "a specific, ED-native, baryogenesis-unified open problem — derive the first-arrival handed-commitment lock and its γ⁵ realization." That is the genuine research target, and it is now one target instead of two.

**Trajectory (six steps):** SQ1 not-walled → SQ1c arrow→net chirality (1+1D) → SQ1d topological/maximal → SQ1e undoubles in 3+1D → SQ1f *transport survivor vector-like (1+1D was special), but per-commitment route works and unifies with baryogenesis.* The arrow remains the source of the orientation; the open core is the global lock that turns orientation into a single handedness — shared now with baryogenesis.

---

*#2b core, attacked (`chiral_percommit.py`). (1) Transport route: the 3+1D survivor is VECTOR-LIKE — near p=0, `D≈iΣγ^μ p_μ` is the full 4-component Dirac point (both chiralities); retarded = Wilson class = vector-like; the 1+1D chirality was dimension-special (there the global point-gap winding coincides with chirality; in 3+1D they decouple). A real partial-no for the transport route. (2) Per-commitment route (AP): handedness = winding of P09 phase along the commitment sequence; toy shows net winding survives iff the phase-advance SIGN is LOCKED (robust to P11 noise: drift∼N beats noise∼√N), else vector-like (net 0). So chirality reduces to one question — is the sign globally locked? — and the lock is FIRST-ARRIVAL, the same mechanism ED baryogenesis already needs. UNIFICATION HYPOTHESIS: parity violation + matter/antimatter asymmetry = ONE handed-commitment lock-in (one choice, two faces; both maximal because topological). Open core (now shared with baryogenesis): the first-arrival lock is undischarged (no native ℤ₂; P-BinaryAdmission, M2; R1/R2/R3 failed); the phase-helix → γ⁵ identification is unproven (the relativistic bridge, re-phrased); anomalies (SQ3) untouched. Verdict: #2b reframed from unmapped-possible-wall to a specific ED-native baryogenesis-unified open problem (derive the handed-commitment lock + its γ⁵ realization) — ONE target, not two. Crank-rail: transport-vector-like established by standard structure; per-commitment toy schematic (mechanism, not ED's actual dynamics); unification + γ⁵ identification flagged as hypotheses. No coupling built, no anomaly computed, no lock-in derived.*
