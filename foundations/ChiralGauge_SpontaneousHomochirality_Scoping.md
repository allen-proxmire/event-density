# Spontaneous Homochirality: Can ED's Competition Amplify a Handedness? (Scoping)

**Opened 2026-07-08** at AP's direction, after T4 established ED does not FORCE chirality (default vector; no handed topology (fork a), no screw (Build 1), no pseudoscalar at first-arrival (fork b)). AP + Copilot proposed four emergence routes; this scopes them and runs the decisive test. Crank-rail ON.

## The organizing lens: where's the pseudoscalar?

Parity violation IS, by definition, a nonzero **parity-odd observable** (a pseudoscalar with nonzero mean). Every chirality idea must answer: what pseudoscalar, and why is its mean nonzero? This filter organizes everything.

## The distinction that decides it: chiral structures vs net handedness

- **Chiral structures** (helical motifs, chiral composites) form easily in parity-symmetric systems, but **racemically** — for every L, a mirror R. Navier-Stokes makes vortices and is parity-symmetric. This is NOT parity violation.
- **Net handedness** (a nonzero pseudoscalar mean) needs either a parity-odd term in the dynamics (ED's primitives lack it — T4) or **spontaneous symmetry breaking + amplification**.

## The corrected understanding (the key move)

Two things must be separated:

1. **Ensemble parity symmetry is PRESERVED.** ED has no parity-odd primitive (its one discrete-symmetry-breaker, the arrow P11, is *time*-odd, not *parity*-odd). So over many runs there is no systematic L-vs-R bias: 50/50. This is a genuine **no-go for *systematic* parity violation** — ED will never predict "the universe must be left-handed."

2. **Per-run spontaneous homochirality is NOT forbidden.** A single run can spontaneously fix one handedness (like a ferromagnet picking a direction), giving parity violation *in that universe* from a parity-symmetric theory. This requires a **same-handedness coupling** `κ_h` (do L-composites couple more strongly to L than to R?). Crucially, `κ_h` is a **parity-EVEN** quantity (parity maps LL→RR and LR→LR, preserving |same-vs-opposite|), so it is *allowed* to be nonzero, and in real physics it is: **diastereomeric interactions** (same- vs opposite-handed chiral molecules have different interaction energies) are exactly this, and they are what lets biological **homochirality** bootstrap (the **Frank mechanism**: autocatalysis + mutual antagonism amplifies a fluctuation to fixation).

So the earlier "no-go" over-reached: a parity-EVEN *rule* applied to a parity-ODD (chiral) *configuration* gives a chiral result, and same/opposite-handed composites can couple differently without breaking ensemble parity symmetry.

## Why ED is a live candidate

- **Chiral substrate (ideas 1, 3):** a V5-bound cluster of ≥4 distinguishable chains is generically a chiral 3D object (like a carbon with 4 different substituents). ED makes chiral composites.
- **The amplifier (idea 2 + P11):** ED's winner-take-all commitment dynamics is structurally **autocatalytic** (a committed pattern suppresses its alternatives) — precisely the Frank amplifier, built into P11.
- **The seed (idea 4):** any tiny fluctuation (Frank amplifies fluctuations, not just biases).
- **The missing ingredient = `κ_h`:** do same-handedness composites couple more strongly than opposite (diastereomeric coherence)? This is the one open, decidable gate.

**Route A (the order parameter to track):** the coarse-grained pseudoscalar `χ = v·(∇ρ×j)` (arrow · (density-gradient × polarity-current)), built from ED's own fields. Ensemble mean zero; per-run nonzero iff SSB fixes it. This is *what to measure* once route B says amplification is possible.

## The decisive first test (this probe)

**Diastereomeric coherence:** build chiral composites (4-vertex handed clusters) with phase textures DERIVED from a parity-even substrate rule, and measure whether same-handedness pairs (LL/RR) are more coherent than opposite (LR). The docking uses PROPER rotations only (physical), so same-handed can align geometrically while opposite cannot (mirror frustration).
- **If `coherence(LL) > coherence(LR)`** → `κ_h > 0` → Frank amplification viable → **route B lives** (spontaneous per-run homochirality plausible; then measure route-A's χ under competition).
- **If `coherence(LL) = coherence(LR)`** (handedness-blind) → racemic → **route B dies**, and weak chirality is genuinely *inherited* (needs an external parity-odd input), confirming the T4 wall from a fourth angle.

## Honest tier

Hypotheses/reframes, NOT results. Ensemble parity symmetry is preserved regardless (no systematic PV — that stays a firm no-go). The claim under test is *per-run spontaneous* homochirality via a parity-even same-handedness coupling. Risk: the substrate coupling is handedness-blind (`κ_h = 0`) and it stays racemic. Do not present spontaneous homochirality as established; it is a candidate mechanism whose one open gate (`κ_h`) this probe tests.

---

## Probe 1 (DONE 2026-07-08) — the κ_h gate PASSES; route (b) is mechanism-viable

`evaluation/ChiralGauge/homochirality_probe.py`. Chiral composites = 4-vertex handed tetrahedra; per-vertex phases derived from a parity-even distance rule (`φ_i = Σ_{j≠i} 1/|r_i−r_j| mod 2π`, identical for a composite and its mirror); V5-like coupling = proximity-weighted phase overlap after best **proper-rotation** docking (physical: no mirrors).

**Results.**
- **`κ_h > 0` for every chiral template** (mean **+0.32**; `coh(same)=4` by congruence, `coh(opp)` 3.15–3.99), and it **scales with the composite's chirality** (chirality 0.21 → κ_h 0.85; chirality 0.002 → κ_h 0.007).
- **Achiral control: `κ_h ≈ 0.003`** — the preference vanishes with no handedness to prefer, so it is not a docking artifact.
- **Frank amplification** (population of L/R copies, replication ∝ same-handedness support, winner-take-all): from a near-racemic start every run fixes one handedness (excess ±1.0), with the winner **random across runs** (ensemble stays ~50/50).

**Verdict: the mechanism chain closes and the gate passes.** Same-handedness chiral composites couple more strongly than opposite (a genuine, parity-EVEN **diastereomeric** effect — the same physics that makes chiral catalysis and biological homochirality work), and ED's winner-take-all competition (structurally a Frank amplifier) fixes one handedness per run. So **per-run spontaneous homochirality is mechanism-viable in ED**, while ensemble parity symmetry is preserved. This UPDATES the matter-sector verdict:
- **Systematic / law-level parity violation: NO** (ensemble parity preserved; the no-go stands — ED won't say "the universe *must* be left-handed").
- **Spontaneous / per-run parity violation (homochirality): VIABLE** (the κ_h gate passes; the Frank amplifier is native).

So ED's honest candidate for the weak force's observed chirality: **not a law, but a spontaneously-broken homochirality** — a contingent single-run selection amplified by competition, with a *random* global sign.

**Honest tier + load-bearing caveats (crank rail).** MODEL result, not the certified substrate:
1. **The coupling is a faithful caricature, not the real V5 kernel.** κ_h > 0 relies on ED's coupling being **proximity/docking-based** (proper-rotation-sensitive), which is plausible (V5 couples nearby channels by phase overlap) but was NOT run on the certified simulator or the actual V5 kernel. If ED's real coupling is purely phase-based independent of geometric alignment, κ_h could collapse to 0. This is the #1 thing to verify next.
2. **Chiral composites are asserted, not built.** A 4-chain V5 cluster being chiral and stable (idea 3) is plausible but unbuilt on the substrate.
3. **The Frank step is a standard population model** parametrized by the measured κ_h — it shows κ_h>0 *suffices* for amplification (standard), not that ED's specific dynamics does it (though winner-take-all is structurally Frank).
4. **Different KIND of parity violation than the SM.** ED gives *spontaneous, per-run, contingent-sign* homochirality (possibly with cosmological parity-domains), whereas the SM's weak chirality is a *fixed universal law*. Whether the SM's universal left-handedness can be ED's single-run spontaneous choice, or is genuinely law-level (which ED cannot produce), is the real open physics question and a potential falsifier.

**Net:** route (b) LIVES as a mechanism-viable account (the κ_h gate passes on a faithful model), NOT a closed result. The tautological core (chiral objects proper-dock better than their enantiomers) is real geometry; the ED-specific load-bearing assumption (V5 coupling uses that geometry) is plausible-but-unverified. Next: (a) verify κ_h on a real V5-coupled composite in the certified/kernel machinery (the decisive substrate test); (b) build an actual chiral V5 cluster; (c) confront the per-run-vs-law-level distinction against the SM's universal handedness.

---

## Probe 2 (DONE 2026-07-08) — κ_h COLLAPSES on the real V5 functional; the Probe-1 positive was a docking artifact. Route (b) does NOT survive.

`evaluation/ChiralGauge/homochirality_v5_verify.py`. Replaced Probe 1's docking/vertex-matching model with the **actual V5 coherence functional**: `E(R) = Σ_{i∈A, j∈B} exp(−|r^A_i − R r^B_j|/ℓ_V5) · cos(φ^A_i − φ^B_j)`, summed over ALL cross-pairs (no hand-matching), composites relaxing orientation (proper rotations) to max coherence. Decomposed into full / phase-only / proximity-only.

**Results.**
- **phase-only: `κ_h = 0.000` exactly.** Analytic: `Σ_{ij} cos(φ_i−φ_j) = (Σcos φ)² + (Σsin φ)²` depends only on each composite's total phase, not geometry or handedness. V5's phase part is **handedness-blind**, as the caveat feared.
- **proximity-only: `κ_h ≈ 0`** (mean −0.012), and a reach/separation sweep (ℓ ∈ {0.3,0.5,1.0,2.0}, sep ∈ {0.6,1.3}) gives mean `κ_h` in **[−0.036, +0.037]** with **sign-symmetric** per-template scatter (individual composites go both +0.4 and −0.4, averaging to zero). No systematic same-handedness preference in any regime.
- **full V5: `κ_h ≈ −0.01`** (chiral) ≈ achiral control — indistinguishable from zero.

**Why the Probe-1 positive was an artifact.** Diastereomeric selectivity (`κ_h > 0`) requires **lock-and-key registration**: a forced one-to-one shape complementarity, so that same-handed shapes fully register and enantiomers can't. Probe 1's docking with vertex-matching **imposed** that registration (Hungarian pairing + full alignment), manufacturing `κ_h`. The **real V5 coupling is a smooth all-pairs proximity+phase sum** (mean-field-like, no registration): an opposite-handed composite simply rotates to bring a *different* subset of channels into good contact, achieving comparable total coherence. So V5 does **not** discriminate handedness. `κ_h ≈ 0`.

**Verdict: route (b) does NOT survive verification.** ED's actual V5 coupling is handedness-blind, so its competitive (Frank) dynamics has **no same-handedness bias to amplify** → stays racemic → **no spontaneous homochirality**. The exciting Probe-1 result was a model artifact, caught by the verification it was flagged as needing.

**FINAL matter-sector chirality verdict (four independent angles, all NO).** Parity violation is a genuine WALL in ED:
1. **Topology / wiring** (fork a): canonical P07 has no channel-topology → no handed structure.
2. **Transport / screw** (Build 1): the 3+1D emergent fermion has no forced screw → vector.
3. **First-arrival selection** (fork b): no pseudoscalar order parameter → imprints C (matter/antimatter), not P.
4. **Spontaneous homochirality** (Probe 2): V5 coupling is handedness-blind (`κ_h ≈ 0`) → competition stays racemic.

**Weak chirality is INHERITED, not derived by ED — full stop.** The only chirality-adjacent thing ED derives natively is the **matter/antimatter asymmetry** (C, via the arrow's first-arrival P09-phase selection — R4, solid). Parity (P) is inherited. This is a clean, robust, falsifiable tiering, and it stands on four independent confirmations plus a self-caught artifact-retraction (Probe 1 → Probe 2), which is the discipline working.

**Honest residual (small):** a hypothetical *lock-and-key* V5 variant (very short reach + hard-core exclusion enforcing one-to-one channel registration) could in principle recover `κ_h`, but that is not V5's characterized smooth-coherence form, and building it would be adding structure, not reading it. Not pursued.
