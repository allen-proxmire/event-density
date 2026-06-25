# #2b · The Sparsity Bridge — the Chirality Is Topological (and survives sparse commitment)

**Foundations computation — the unitarity/sparsity bridge from SQ1c. Sim: `evaluation/ChiralGauge/chiral_sparsity.py`. Question: ED's commitment is *sparse* (the same fact that makes α₁ tiny) — does that sparsity *suppress* the arrow's net chirality (which would clash with the weak force's *maximal* parity violation), or is the chirality *topological* and robust? Result: the net chirality (point-gap winding) is **topological — quantized at ±1 for every nonzero commitment, however sparse, dropping to 0 only exactly at zero commitment.** So sparse commitment preserves the *full* chirality, unlike the non-topological α₁ which scales with the sparsity. Same sparse-commitment fact, opposite fates — and the toy suggests a reason the Standard Model's parity violation is *maximal*. Honest limits: still 1+1D; "sparse" is modeled as "weak" (a proxy, not a faithful rare-discrete-commitment model); the relativistic and anomaly bridges remain.**

**Crank rail — maximal, and especially here.** This is a favorable result, and the previous step was a correction of *over-pessimism*, so the temptation now is to over-correct into hype. Guard: the topological robustness is a genuine, computed property of the 1D point-gap winding; the "explains maximal parity violation" reading is a *suggestive hypothesis*, explicitly tiered; and the sparse-as-weak modeling is a proxy whose faithful version (rare discrete commitment kicks between unitary evolution) is named as the next refinement, not claimed done.

---

## 1. The worry being tested

SQ1c showed the arrow's retarded transport carries a net chirality (spectral flow ±1). But the chirality was *produced by the non-hermiticity* — i.e. by the arrow's one-wayness, which is non-unitary. ED reconciles this with quantum mechanics via **sparse commitment**: unitary evolution between *rare* irreversible commitments (the same structure that forces α₁ tiny and underwrites the Zeno argument). That raises a sharp worry:

> If commitment is sparse, and the chirality comes from commitment, does the chirality get *suppressed by the sparsity* — scaling away to nothing like α₁ ∼ ρ_event/ρ_Planck does? Because the weak force's parity violation is **maximal**, not tiny. A sparsity-suppressed chirality would be the wrong answer.

## 2. Result: the chirality is topological, not suppressed

Model the effective one-way bias as `ε` (small `ε` ≈ sparse/weak commitment): `tR = 1+ε`, `tL = 1−ε`. Compute the point-gap winding (the net chirality) vs `ε`:

| ε (commitment bias) | net chirality (winding) |
|---|---|
| 0.5 | +1 |
| 0.1 | +1 |
| 0.01 | +1 |
| 10⁻³ | +1 |
| 10⁻⁴ | +1 |
| 10⁻⁵ | +1 |
| **0** | **0** |

The winding is **+1 for every `ε > 0`, however tiny**, and drops to 0 *only exactly at `ε = 0`*. This is the signature of a **topological invariant**: it cannot change continuously, so it stays pinned at its quantized value (±1) until the gap closes (here, only at `ε=0`, the no-arrow / GR limit). Geometrically: for any `ε>0` the dispersion `2cos k + 2iε sin k` is an ellipse *enclosing the origin* (winding 1), however thin; only at `ε=0` does it collapse to a real segment (winding 0).

## 3. The elegant distinction — same sparse-commitment fact, opposite fates

This resolves the worry favorably, and it does so by a clean structural distinction:

- **α₁ is a non-topological coupling.** It scales with the commitment density: `α₁ ∼ ρ_event/ρ_Planck`. Sparse commitment ⟹ tiny α₁. (The GR-IV result.)
- **The chirality is a topological charge.** It is quantized at ±1 and *cannot* scale with the density — it is the full ±1 for *any* nonzero commitment, or 0 only if commitment never happens. Sparse commitment ⟹ **full, maximal chirality.**

So the *same* sparse-commitment fact has *opposite* consequences for the two quantities: it makes the non-topological coupling (α₁) vanishingly small, and it leaves the topological charge (chirality) maximal and intact. **Maximal parity violation is therefore compatible with sparse commitment** — there is no tension, because chirality is the kind of thing sparsity cannot dilute.

## 4. A striking consistency with the Standard Model (hypothesis, tiered)

The Standard Model has a long-standing *unexplained* feature: parity violation is **maximal** (the W couples to a *pure* left-handed current, V−A) — not partial, not a tunable small angle. Why maximal? In the SM it is simply put in by hand.

The toy suggests an answer worth flagging: **parity violation is maximal because chirality is topological.** A topological charge is quantized — you cannot have "a little bit" of it; it is ±1 or 0. If ED's chirality is the arrow's topological charge, then it is *forced* maximal (±1), never partial. And the very same structure that forces it maximal (topological quantization) makes the *non-topological* preferred-frame coupling α₁ tiny (sparsity-suppressed). That single picture — topological quantities maximal, non-topological couplings sparsity-suppressed — matches the SM's actual pattern: **maximal parity violation coexisting with unobservably tiny preferred-frame effects.** This is a genuine, suggestive consistency. It is *not* a derivation; it is the hypothesis the relativistic bridge would have to confirm.

## 5. Honest limits (what this does NOT show)

- **Still 1+1D.** The topological robustness is a property of the 1D point-gap winding. Whether the relativistic 3+1D chirality (the γ⁵ Weyl index) is topological *in the same robust way* is the open relativistic bridge — not settled here.
- **"Sparse" was modeled as "weak."** A small constant bias `ε` is a *proxy* for sparse commitment, not a faithful model of it. The faithful version is *rare discrete non-Hermitian commitment events between stretches of unitary evolution*. Whether that preserves the topological winding (plausible — topology is robust to such perturbations — but not shown) is the next refinement. So the unitarity bridge is *favorably indicated*, not *crossed*.
- **Anomalies (SQ3) untouched**, and remain the hardest piece.

## 6. Verdict

**The sparsity bridge gets a favorable first result: the arrow's net chirality is topological (quantized ±1), so sparse commitment preserves it in full — maximal parity violation is compatible with sparse commitment, with no fine-tuning.** The distinction is clean and ED-coherent: the *same* sparse-commitment fact that makes the non-topological α₁ tiny leaves the topological chirality maximal. The toy even offers a candidate explanation for the SM's unexplained *maximality* of parity violation (a topological charge must be maximal). **But this is 1+1D, "sparse" is proxied as "weak," and the relativistic γ⁵ descent + anomaly cancellation remain open.** The honest status of #2b after four steps: not walled (SQ1), the arrow carries net chirality (SQ1c, correcting SQ1b), and that chirality is topological and survives sparse commitment (here) — a genuinely promising, internally-coherent picture, with the relativistic bridge (needs the open T4 substrate→Dirac chain), a faithful sparse-commitment model, and anomalies as the remaining, increasingly hard work.

**Trajectory:** SQ1 (N–N doesn't bind) → SQ1c (arrow → net chirality) → SQ1d (chirality topological, sparsity-robust, maximal). Each step the picture got more coherent *and* the honest open edge got more specific. The arrow now looks like a candidate source not just of chirality but of *maximal* chirality — the right qualitative match to the weak force — pending the relativistic and anomaly bridges.

---

*Sparsity/unitarity bridge for #2b (`chiral_sparsity.py`). Net chirality (point-gap winding) vs effective one-way bias ε: +1 for ALL ε>0 (0.5 down to 1e-5), 0 only at ε=0. Topological → quantized → robust: sparse commitment does NOT suppress it (unlike α₁ ∼ ρ_event/ρ_Planck, a non-topological coupling). So the SAME sparse-commitment fact gives opposite fates — α₁ tiny (non-topological, suppressed), chirality maximal ±1 (topological, quantized). Maximal parity violation is therefore COMPATIBLE with sparse commitment, no fine-tuning. Suggestive (tiered) SM consistency: parity violation is maximal BECAUSE chirality is topological (a quantized charge can't be partial) — a candidate ED explanation for an unexplained SM feature, matching the real pattern (maximal P-violation + tiny preferred-frame). Honest limits: 1+1D; "sparse" modeled as "weak" ε (proxy, not faithful rare-discrete-commitment model — that's the next refinement); relativistic γ⁵ descent + anomaly cancellation (SQ3) remain open. Verdict: sparsity bridge favorably indicated (not crossed); #2b promising and coherent across SQ1→SQ1c→SQ1d; remaining = relativistic bridge (open T4 chain), faithful sparse model, anomalies. Crank-rail held against over-correction: topological robustness computed/solid; maximality-explanation flagged as hypothesis; sparse-as-weak flagged as proxy. No relativistic coupling built, no anomaly computed, no number faked.*
