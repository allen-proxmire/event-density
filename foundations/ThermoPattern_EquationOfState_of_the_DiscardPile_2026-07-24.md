# Is Every Theory the Equation of State of Its Own Discard Pile? (Step 3 — exploration, adversarially corrected)

**Date:** 2026-07-24
**Status:** Working note — **exploratory**, adversarially reviewed and **corrected**. Chased AP's pattern question (Jacobson got GR from thermodynamics — is there a recipe "each theory = the equation of state of its discard pile," and does the ledger predict where it works?). **What survives review:** a *real, literature-verified asymmetry* — gravity uniquely gets a clean thermodynamic derivation; the reversible theories do not. **What did NOT survive:** the clean "entropy criterion" I proposed to explain it, its stated mechanism, and the "gravity uniquely has horizons" reconciliation — all over-reached (the fifth positive-sharpening over-bank of the session; core observation intact, explanation retracted). Honest tiers throughout.

---

## 1. The question and the precedents

Every coarse-graining **discards** something. The recipe under test: *a theory's equation of motion can be recovered as the equilibrium equation of state of its own discard pile.* Precedents:
- **GR — Jacobson (1995).** Einstein's equation from `δQ = T dS` on local horizons. **Accepted** (PRL, thousands of citations, spawned the "thermodynamics of spacetime" subfield). ED grounds his inputs — step-1 note.
- **Diffusion — Jordan–Kinderlehrer–Otto (1998).** The heat equation *is* the gradient flow of entropy in Wasserstein space. **Established math** — but the *easy* case: diffusion is manifestly dissipative, so "a dissipative equation is thermodynamic" is near-tautological. Confirms the recipe is a real thing; weak as independent support.
- **Newton — Verlinde (2011).** *Contested*, and **not independent of GR** (Newton is a GR limit Jacobson already covers). Demoted from a clean precedent to a disputed, redundant one.

## 2. The one durable finding — the asymmetry is real (kill switch does NOT fire)

The sharp, falsifiable question: is there a clean, accepted derivation of a *reversible* theory (Maxwell, Schrödinger) as an equation of state, comparable to Jacobson? **Literature check says no** — robustly:

- **Schrödinger.** Nelson's stochastic mechanics (1966) derives it from a diffusion-like entropic background, but is blocked by the **Wallstrom objection (1989/94)**: it reaches Schrödinger only by imposing an *ad hoc* phase single-valuedness / integer-circulation condition with no non-circular justification. **Unresolved ~35 years**; the contested patches (Fritsche–Haugk, Schmelzer, Derakhshani, Caticha's entropic dynamics, the June-2026 Nawaz et al. proposal) are **minority/non-accepted**.
- **Maxwell.** Only the **static** part (electro/magnetostatics) falls out as an entropy-extremum; the **propagating Faraday–Ampère core does not**. (Most "Maxwell + thermodynamics" hits are the unrelated "Maxwell *relations*" name-collision.)

**So the asymmetry Jacobson-clean vs. everything-else-contested is real and robust.** Gravity genuinely is the one theory with a clean thermodynamic derivation. That much is a verified fact, not speculation.

## 3. WHY it holds — genuinely OPEN; my clean criterion did NOT survive

I proposed: "the recipe works iff the discard has entropy — direct-dissipative (diffusion) or horizon-hidden (gravity) — and fails for the reversible theories because they have *no entropy pile*." **The adversarial check refuted the mechanism and softened the criterion:**

- **The "no entropy pile" mechanism is wrong.** Nelson *does* build Schrödinger from an explicitly entropic/Brownian substrate — there **is** an entropy pile. The obstruction is **topological (Wallstrom's quantization condition)**, not absence of entropy. So the reversible theories don't resist for the clean reason I gave; the actual block is specific and technical.
- **Maxwell resists differently again** — static-yields / propagating-core-resists, not "no entropy."
- So the three "resists" have **specific, different reasons** (Wallstrom for QM; static-vs-propagating for Maxwell), **not one tidy criterion.** "Works iff the discard has entropy" is thin and retrodictive — its only real content is the literature asymmetry of §2, which does hold but was the input, not a new prediction.
- **"Gravity uniquely has horizons" is false as stated:** analog/acoustic horizons (sonic, BEC) carry Hawking temperature and entropy, so horizons are not unique to fundamental gravity. (They live in dissipative fluids, so not counterexamples to the *recipe* — but they kill the "geometry uniquely" rhetoric.) The "gravity re-deposits its arrow as horizon-entropy" story is coherent but **post-hoc**, built to explain the one datum it needs.

## 4. Honest tier

- **Verified:** the *asymmetry* (§2) — gravity clean, reversible theories contested — is real, literature-checked, and not a-priori guaranteed.
- **Established-but-easy:** diffusion = entropy gradient flow (JKO).
- **Open:** *why* the asymmetry holds. The clean entropy-criterion is **retracted**; the real obstructions are specific (Wallstrom; static-vs-propagating) and it is an **open question whether they share any common cause** — or whether "gravity is special" simply because its discard *is the metric/geometry itself*, so the equation of state closes on the same object it constrains (a candidate worth exploring, not a claim).
- **Retracted:** the tidy criterion, the "no entropy" mechanism, "gravity uniquely has horizons," and Verlinde-as-clean-precedent.

## 5. What this leaves, honestly

The pattern is **not** a clean universal recipe, and I should not have framed it as one. What is genuinely worth keeping is narrower and true: **among all the ledger theories, gravity is uniquely the one recoverable as a thermodynamic equation of state — a real, verified asymmetry — and the honest, open question is what makes gravity special.** The best-surviving ED-flavored candidate answer (untested): gravity's discard is *geometry itself*, so its "equation of state" closes on the metric, unlike theories whose discard is some internal structure sitting *on* a fixed geometry. That is a lead, not a result.

**Process note.** Fifth positive-sharpening over-bank of the session — the *observation* survived, the *explanation* did not, caught by adversarial review before it was banked. Pattern per [[feedback_dont_over_bank_positive_sharpenings]]: I reached for a tidy criterion/mechanism past the honest baseline (a verified asymmetry + an open why).

## Cross-references
- `foundations/ED_and_Jacobson_GravityFromThermo_2026-07-24.md` (step 1 — ED grounds Jacobson's inputs).
- `ED Generative/physics-papers/substrate-evaluation/Paper_HowCoarseGrainReality.md` (the ledger).
- Jacobson 1995 (GR, accepted); JKO 1998 (diffusion = Wasserstein gradient flow of entropy); Verlinde 2011 (Newton, contested); Nelson 1966 + Wallstrom 1989/94 (Schrödinger-from-diffusion and the standing obstruction); Caticha (entropic dynamics, minority).
