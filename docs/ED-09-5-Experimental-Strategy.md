# ED-09.5 Experimental Strategy — Sharp Quantum-Classical Transition

**Purpose.** Self-contained strategy document for pursuing experimental tests of ED-09.5's sharp quantum-classical (Q-C) transition prediction. Includes: why it's harder to order than FRAP, the three-tier strategy, near-term action sequence, FRAP status snapshot, theory-memo scope, and draft collaboration emails.

**Date opened:** 2026-04-17. **Status:** strategy only; no experiment commissioned yet. FRAP is in motion separately (see §5).

---

## 1. Context

ED-09.5 is the Q-C boundary paper in the ED corpus. Its signature prediction is that **there is a sharp structural transition at the quantum-classical boundary, distinct from standard environmental decoherence**, driven by a system-dependent internal-complexity threshold. Standard quantum mechanics predicts only the smooth decoherence side; ED-09.5 predicts an additional sharp collapse to a single participation channel when internal complexity outpaces event-production capacity.

This is **the single most distinctive falsifiable prediction in the ED corpus**. No competitor predicts it. Its confirmation would be architectural evidence at a level comparable to (or exceeding) any result currently in the Supporting Evidence Registry.

It is also the single most distinctive prediction **with no assigned test program**. This memo exists to change that.

---

## 1.5 Mathematical skeleton (the formal framing — use in every memo and email)

**The sharpness is in the PDE, not in the interpretation.** The canonical ED PDE's damping discriminant (Canon principle P6) defines a sharp bifurcation at

$$\Delta \;=\; D + 2\zeta \;=\; 1 \quad\Longleftrightarrow\quad D_{\text{crit}} = 0.5$$

derived analytically in 00.3 and numerically verified in ED-Phys-18 and ED-SIM-3D. This bifurcation separates three regimes of the same equation with quantitatively distinct dynamics:

| Regime | Parameter condition | Dynamical character |
|:-------|:-------------------:|:--------------------|
| **Oscillatory** | `D < 0.1` (`Δ < 1`) | Underdamped, reversible, standing participation waves; triad coupling generates harmonics at 3–6% of fundamental |
| **Hybrid** | `0.1 ≤ D ≤ 0.4` | Mixed, smooth interpolation; transient oscillation count `N_osc = 8–19` observed in ED-Phys-17 |
| **Parabolic** | `D ≥ 0.5` (`Δ > 1`) | Overdamped, irreversible, structure-forming; Barenblatt spreading; horizon formation at the mobility ceiling |

These are two qualitatively distinct phases of the same PDE, separated by a sharp bifurcation at a specific parameter value. It is a numerically verified property of the equation, not an interpretive claim.

### The ED-09.5 identification

Reformulated without philosophical drapery, ED-09.5 says this:

> The sharp `D_crit = 0.5` bifurcation in the canonical ED PDE **is** the quantum-classical transition. Coherent quantum behaviour corresponds to `D < 0.1` (oscillatory, reversible, wavelike, superposition = coexisting participation channels). Classical behaviour corresponds to `D ≥ 0.5` (parabolic, irreversible, structure-forming, measurement = commitment to a single participation channel). The transition between them is sharp, not continuous.

The sharpness is inherited from P6. What ED-09.5 adds is the **identification of the mathematical bifurcation with the physical Q-C transition** — not a new mathematical claim, but a claim about what the bifurcation is about.

### Quantitative predictions that follow

Once the identification is accepted, the PDE forces specific experimental predictions:

| Quantity | Value | Regime | Source |
|:---------|:-----:|:------:|:-------|
| Transient oscillation count `N_osc` on the quantum side | **8–19** (≈ 9) | `D < 0.1` | ED-Phys-17 |
| Quality factor `Q` on the quantum side | **≈ 3.5** | `D < 0.1` | 00.3 |
| Triad coupling coefficient `C` | **≈ 0.03** | all regimes | ED-Phys-16 |
| Third-harmonic / fundamental ratio | **3–6%** | `D < 0.1` | ED-Phys |
| Transition location in channel weight | **`D = 0.5` exactly** | sharp | P6 / 00.3 |
| Ground state energy | **`E_ground = αγρ₀`** | all regimes | 00.3 |
| Relaxation timescale | **`t_rel ≈ ρ₀/(αγ)`** | all regimes | 00.3 |

These are quantitative. They are either right or wrong when measured.

### Contrast with standard decoherence

Standard environmental decoherence predicts:

- **Smooth exponential loss of coherence** — no sharp transition at any parameter value.
- **No specific oscillation count** — `N_osc` varies continuously with environment coupling, with no universal value.
- **No specific harmonic structure** — no predicted 3–6% third-harmonic signature.
- **No universal `Q`** — quality factor depends entirely on environment details.

### Contrast with dynamical-collapse models (GRW / CSL / Diósi-Penrose)

Dynamical-collapse models predict:

- **Stochastic collapse events** — no deterministic sharp transition at a specific parameter value in a specific system.
- **Collapse rate scales smoothly** with mass or complexity, without a bifurcation.
- **No specific `N_osc` or triad harmonic signature.**

### The experimental mapping

The prediction becomes testable when paired with the **Dimensional Atlas**. For any given experimental regime (matter-wave interferometry, optomechanics, cavity QED), the Atlas provides an effective channel weight `D(x)` as a function of the experiment's control parameter `x` (molecular mass, photon number, mode occupation, etc.).

**The predicted transition location is the solution of**

$$D(x_c) \;=\; 0.5$$

On the quantum side of `x_c`, the PDE predicts `N_osc ≈ 9` transient oscillations with third-harmonic content at 3–6% of the fundamental and `Q ≈ 3.5`. On the classical side, Barenblatt-like spreading with no residual oscillations.

### What this reformulation changes

1. The Q-C transition is **not a new postulate** in ED-09.5. It is a naming of a mathematical feature already present in the canonical PDE (P6, numerically verified).
2. The experimental observable is **not a generic "coherence fall-off"** but **four specific quantitative signatures** on the quantum side of a specific bifurcation point, any of which can falsify the prediction.
3. The prediction **differs from standard decoherence in at least four measurable ways**, not in philosophical framing.
4. The prediction **differs from GRW / CSL / Diósi-Penrose** at the structural level: those are stochastic collapse mechanisms, ED-09.5 is a deterministic dynamical bifurcation at a specific parameter value.

**Use this formal framing in every downstream memo and in every outreach email.** It is the difference between "a speculative theory about quantum cats" and "a specific bifurcation in a specific PDE with specific quantitative signatures that don't match any existing Q-C account."

---

## 2. Why ED-09.5 is harder to order than FRAP

| | FRAP BSA | ED-09.5 Q-C transition |
|:-|:-:|:-:|
| Instrument | Confocal microscope + bleach laser | Varies by regime — cavity QED, optomechanics, or matter-wave interferometer |
| Sample | Off-the-shelf BSA powder, PBS buffer | Custom-engineered macroscopic quantum system |
| Prep time | Hours | Months to years |
| Cost | Hundreds to low thousands USD | Typically $500k–$10M of infrastructure |
| Who can run it | Any core facility | ~10 labs worldwide |
| What you are buying | Data collection on a designed protocol | Access to a years-long research program |

FRAP is a **measurement**. ED-09.5 is a **physics experiment at the frontier of macroscopic quantumness** — a different category of thing. Nobody sells "macroscopic superposition time" on a price list.

---

## 3. Three-tier strategy

### Tier 1 — Data reanalysis (orderable today)

Several groups have published data from macroscopic-quantum experiments whose raw traces could be re-examined for the sharp-transition signature ED-09.5 predicts:

- **Arndt** (Vienna) — matter-wave interferometry with large molecules.
- **Aspelmeyer** (Vienna) — optomechanics.
- **Haroche / Raimond** (ENS Paris, legacy) — cavity QED with increasing photon number.

Much of this data exists in supplementary material of published papers. A competent graduate student could do the reanalysis in weeks.

- **Cost:** student-month, low thousands USD.
- **Output:** either a confirmation (a dataset that already shows the ED-09.5 signature nobody noticed), a null (sharp transition not in the data, narrows the regime where ED-09.5 could hide), or a design spec (here is exactly what a Tier-2 collaboration would need to measure).
- **This is the FRAP-equivalent for ED-09.5.**

### Tier 2 — Collaboration with an existing experimental group

Email one of Aspelmeyer, Arndt, or Chu's group at Stanford with a one-page ED-09.5 memo:

> *"your instrument is one of ~5 in the world that could see this; here is the specific signature we predict; here is the parameter regime."*

If the prediction is sharp enough and the experimental group is in a scanning mode anyway, they may agree to include an ED-09.5 run.

- **Cost:** your time drafting the memo, plus the group's willingness. No money changes hands.
- **Role:** you become a theory collaborator on their experimental time.
- **This is how most novel predictions at this scale actually get tested.**

### Tier 3 — Commissioned experiment

You would need to fund a cavity QED or optomechanics lab for a dedicated run.

- **Cost:** NSF / ERC-scale grant.
- **Timeline:** 2–5 years.
- **PI:** requires a willing host lab.
- **Not orderable in the consumer sense.**

---

## 4. Recommended near-term sequence

1. **Sharpen ED-09.5** into a specific scaling law or threshold observable. Theory memo. **2–4 weeks.** (See §6 for scope.)
2. **Tier 1 reanalysis** of one published dataset. **2–4 months at a grad-student rate.**
3. **Tier 2 collaboration memo** to an experimental group if Tier 1 justifies it. (See §7–8 for draft emails.)

You can't order ED-09.5 like FRAP. But you can order the first rung of a ladder that ends there, starting within the next few weeks. **The bottleneck is making the prediction sharp, not the experiment.**

---

## 5. FRAP status snapshot (as of 2026-04-17)

Experiment is in motion at Creative Proteomics Core. Most recent correspondence:

> *Dear Allen,*
>
> *Thank you very much for your quick response and for providing the details.*
>
> *Since this is beyond the standard FRAP assay, I have forwarded the information to our technician team. We will have an internal discussion to evaluate our capabilities and see if we can find a solution for your project.*
>
> *I will come back with more information after the internal discussion in 1-2 weeks.*

**Implication.** CP did not decline. They escalated internally. Expected next touchpoint: ~2026-04-24 to 2026-05-01. Until then, no action required on the FRAP leg.

**Update the Supporting Evidence Registry item 6 when the CP response returns.**

---

## 6. Theory memo scope — sharpening ED-09.5

**Revised scope (2026-04-17).** §1.5 above supplies most of what the theory memo was originally meant to produce: the observable, the regime character, the discriminator against decoherence and collapse models, and the falsification criterion are already in the PDE via P6 + 00.3 + ED-Phys-16/17/18. The theory memo's real task reduces to **the Dimensional-Atlas computation of `D(x)` in each target regime**.

**Deliverable.** A 3–5 page memo, `docs/ED-09-5-Observable-Sharpening.md`, that produces:

1. **`D(x)` for matter-wave interferometry (Arndt regime).** Using the Dimensional Atlas's quantum-regime mapping, express the effective channel weight `D` as a function of molecular mass (and any relevant secondary parameters). Solve `D(m_c) = 0.5` for the critical mass `m_c`. Report `m_c` in daltons with propagated uncertainty from the atlas anchor.

2. **`D(x)` for optomechanics (Aspelmeyer regime).** Analogous computation with control parameter = mechanical-mode occupation number, mode frequency, or effective mass — whichever is the natural axis along which `D` varies in the Atlas mapping.

3. **`D(x)` for cavity QED (Haroche / Raimond regime).** Analogous, with photon number or atom number as the control parameter.

4. **Quantitative signatures to test on the quantum side of each `x_c`:**
   - `N_osc ≈ 8–19` transient oscillations before commitment.
   - `Q ≈ 3.5`.
   - Third-harmonic content 3–6% of fundamental.
   - These are pre-registered; see §1.5.

5. **Tier-1 reanalysis protocol.** For each of Arndt / Aspelmeyer / Haroche, list the specific published datasets whose control-parameter range spans `x_c`, and the specific observable in each dataset that should show the sharp bifurcation if ED-09.5 is correct.

6. **Pre-registered falsification criteria.**
   - Falsified if the coherence observable in a dataset spanning `x_c` shows a smooth monotonic fall-off with no break.
   - Falsified if `N_osc` on the predicted quantum side is not in `[8, 19]`.
   - Falsified if the third-harmonic content is outside `[3%, 6%]` on the quantum side.
   - Falsified if `Q` is outside `[2, 5]` on the quantum side.

**Owner:** theory work (Allen, with Claude assistance). **Estimated effort:** 1–2 weeks focused (reduced from 2–4 given that §1.5 has done the conceptual work). **Blocking:** all downstream Tier-1 and Tier-2 activity.

**Recommended starting point.** Open the Dimensional Atlas's quantum-regime paper (`papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md`) and work out how `D` is parameterised there as a function of observable quantities. This is the anchor computation. The other regime mappings follow the same pattern.

---

## 7. Draft email — Markus Aspelmeyer (Vienna, optomechanics)

**Status:** DRAFT v3 (2026-04-20). Supersedes v2 after the §20 manual thesis-skim returned negative on the predicted envelope signature in published Delic 2019 and Magrini 2021 figures. v2's "your existing data should already show this" anchor is replaced with the cleaner methodological framing: standard optomechanics analysis pipelines aren't constructed to expose a sub-Hz envelope on a 100 kHz–GHz mechanical carrier, so the absence-from-figures says nothing about absence-from-raw-data. v3 also integrates the more conservative tone and structure suggested by an external Copilot draft (reduced ED density up-front, proportionate request, explicit follow-any-data-conditions offer), while preserving the specific quantitative predictions from the v0.9 [`ED-09-5-Observable-Sharpening.md`](ED-09-5-Observable-Sharpening.md) memo.

DO NOT SEND until: (a) §6 memo cold-reader pass complete; (b) Allen affiliation/email/preprint link filled in; (c) optionally — if FRAP status from Creative Proteomics has resolved by send time, fold in a one-line update for credibility.

**Subject:** Raw heterodyne `x(t)` access for a sub-Hz envelope reanalysis — Delic 2020 / Magrini 2021

> Dear Professor Aspelmeyer,
>
> I am writing after a careful read of the 2020 *Science* paper by Delic et al., the associated 2019 thesis, and the 2021 *Nature* paper and thesis by Magrini et al. I am developing a theoretical framework that makes a specific prediction about long-timescale envelope dynamics in cooled optomechanical systems, and I would like to ask whether the raw heterodyne `x(t)` data underlying any of these works could be shared for a targeted reanalysis.
>
> **What the analysis would look for.** A slow envelope feature on the displacement signal at frequency `ω_v / 2π ≈ 8·γ_dec`. For the Delic 2020 system this is roughly **16 mHz** (envelope period ~63 s); for Magrini 2021 the same order; for higher-frequency setups (e.g. cryogenic Si optomechanical crystals, `γ_dec ~ 10⁵` Hz) the envelope would land in the hundred-kHz range. The framework also predicts a quality factor `Q_v ≈ 6 ± 2` for the envelope itself (distinct from `Q_m` of the mechanical mode), third-harmonic envelope content 3–6 % of the fundamental envelope amplitude, and triad cross-coupling at the `~3 %` level (cross-frequency power at `ω_3 = ω_1 + ω_2`).
>
> **Why this isn't visible in your published figures, and why I'm asking anyway.** I have skimmed both the Delic 2019 and Magrini 2021 theses for any mention of slow envelopes, ringdown features, sub-Hz PSD structure, or Allan-variance signatures of the type predicted. None appears — but on reflection this is exactly what I would expect, because standard optomechanics analysis pipelines (heterodyne demodulate at `ω_m`, time-bin in milliseconds-to-seconds for occupation reconstruction, PSD over Hz–MHz, Allan variance over ms-to-seconds) are not constructed to expose a sub-Hz envelope on top of a 100 kHz mechanical carrier. The reanalysis I would like to attempt is a class of analysis that hasn't been performed on optomechanics data, regardless of whether the predicted physics is present. Visibility in published figures is not the relevant test; raw `x(t)` access is.
>
> **Theoretical motivation, briefly.** The prediction comes from Event Density (ED), a scalar-field framework I have been developing (PhilArchive). The relevant claim — that the canonical ED PDE's sharp damping bifurcation at `D_crit = 0.5` corresponds to the physical quantum-classical transition, and that all currently cooled optomechanical systems sit deep on the quantum side of it — is laid out in full in the attached memo. The prediction differs from standard environmental decoherence (smooth fall-off, no universal envelope) and from GRW / CSL / Diósi-Penrose (stochastic collapse smooth in mass) in at least four jointly measurable ways. The framework has empirical track record at other scales (cluster merger-lag, soft-matter diffusivity universal law, architectural cross-scale invariants matching Local Group mass-sheet to Casimir-cavity geometry); I can summarize on request.
>
> **The specific request.** If feasible, a contiguous segment of raw `x(t)` from one cooled-state run — Delic 2020 or Magrini 2021, whichever is logistically simpler — long enough to span at least 2–3 predicted envelope periods (so ≥ ~200 s for the Delic system, shorter for higher-`γ_dec` setups). A short representative segment is sufficient as a first pass; a fuller dataset could follow if the envelope feature is present and the analysis is informative. I would of course follow any data-use conditions or data-sharing agreements your group prefers.
>
> ED-09.5 is the single distinctive prediction in the framework with no existing test program, which is why I am writing. Critical reactions, dataset pointers, a "yes here is one trace," or simply a "no, but here is why" would all be welcome.
>
> Thank you very much for your time, and for the body of work your group has produced.
>
> With respect,
>
> [Allen Proxmire]
> [affiliation / email / preprint link / memo attachment]

---

## 8. Draft email — Markus Arndt (Vienna, matter-wave interferometry)

**Status:** DRAFT. DO NOT SEND until §6 theory memo completes and `m_c` — the critical molecular mass where `D(m) = 0.5` — is computed.

**Subject:** Sharp coherence bifurcation predicted at a specific molecular mass — testable in KDTLI regime?

> Dear Professor Arndt,
>
> I have a quantitative prediction from a scalar-field framework (Event Density / ED; on PhilArchive) that makes a specific claim about large-molecule interferometry: a sharp coherence bifurcation at a computable critical molecular mass `m_c`. Your KDTLI / OTIMA program is the regime where this is directly testable, and I suspect the mass range you've already explored may contain the transition. I would welcome a brief critical reaction or a data pointer.
>
> **The structure of the claim.** ED's canonical PDE has a sharp bifurcation at `Δ = D + 2ζ = 1` (`D_crit = 0.5`), analytically derived and numerically verified. The bifurcation separates oscillatory (`D < 0.1`, underdamped, reversible, ~9 transient oscillations, 3–6% third-harmonic content, `Q ≈ 3.5`) from parabolic (`D ≥ 0.5`, overdamped, structure-forming) dynamics of the same equation. My working identification (ED-09.5) is that this is the Q-C transition. The identification is new; the bifurcation is a theorem of the equation.
>
> **What this predicts for your experiments.** Using the ED Dimensional Atlas, the effective channel weight `D` is a function of molecular mass in the matter-wave regime. The critical mass `m_c` where `D(m_c) = 0.5` is the predicted sharp transition. Below `m_c`: interference with `N_osc ∈ [8, 19]`, `Q ≈ 3.5`, harmonic ratio ∈ `[3%, 6%]`. Above `m_c`: parabolic / committed, no residual oscillations. The memo [TO BE ATTACHED] works out `m_c` in daltons with the propagated uncertainty from the Atlas anchor.
>
> **Contrast with existing accounts.**
> - Standard environmental decoherence: smooth exponential vs mass, no universal oscillation count, no predicted harmonic structure.
> - GRW / CSL / Diósi-Penrose: stochastic collapse scaling smoothly with mass, no deterministic bifurcation at a specific `m`.
>
> ED-09.5 differs from both in at least four measurable ways.
>
> **What I'm asking for.** Any of:
> 1. A short critical reaction to the memo, negative reactions welcome.
> 2. A pointer to a published mass-sweep dataset from your group — I'd like to check whether the bifurcation signature is already in data you've taken.
> 3. If the prediction is worth the time, a brief conversation about whether a planned run could include the `m_c` regime.
>
> The program has an empirical track record at other scales (cluster merger-lag, soft-matter diffusivity universal law, architectural-saddle cross-scale invariants). ED-09.5 is the single prediction in the corpus with no existing test program, which is why I'm writing.
>
> With respect,
>
> [Allen Proxmire]
> [affiliation / email / preprint link — to fill in]

---

## 9. Pre-send checklist

Before either email goes out:

- [ ] §6 theory memo complete and attached as PDF. The memo must lead with the **§1.5 formal framing** (P6 bifurcation, `D_crit = 0.5`, four quantitative signatures, explicit contrast with decoherence and collapse models). This is the non-negotiable structural backbone; the rest is regime-specific computation.
- [ ] Memo computes `x_c` (the critical control-parameter value where `D(x) = 0.5`) for the recipient's specific experimental regime, with uncertainty propagated from the Dimensional Atlas anchor.
- [ ] Memo lists specific published datasets from the recipient's group whose control-parameter range spans `x_c`, so the recipient can see the data they already have is potentially decisive.
- [ ] Memo includes all four pre-registered falsification criteria (smooth fall-off across `x_c`, `N_osc` outside `[8, 19]`, harmonic ratio outside `[3%, 6%]`, `Q` outside `[2, 5]`).
- [ ] Allen's affiliation, email, and preprint link filled in.
- [ ] One friendly reader (outside ED program) has read both memo and email and flagged anything that reads as crank-theory. Particular attention to: does the math-first §1.5 framing read as a PDE claim, or as philosophy dressed up in PDE notation? If the latter, revise before sending.
- [ ] FRAP status update included in the context if it has landed by send time — a second lab-scale result in progress (even pending) adds credibility that this isn't a purely theoretical submission.

## 10. What happens if ED-09.5 is confirmed or falsified

- **Confirmed (sharp transition visible in reanalyzed data):** ED moves from "hasn't been wrong" to "has made a prediction no competitor makes, and the prediction holds." This is publication-quality evidence at a level that changes the program's external profile.
- **Falsified (sharp transition absent where predicted):** narrows the ED-09.5 regime, possibly eliminates it. ED's other evidence legs remain intact; ED-09.5 itself gets downgraded or retracted. This is still valuable — the single most distinctive prediction becomes the most constrained, and the ED corpus is more honest for it.
- **Ambiguous (data insufficient to decide):** Tier 2 becomes the action. Memo to Aspelmeyer / Arndt with a sharpened observable and a request for a dedicated run.

Any of these three is a better outcome than leaving ED-09.5 untested.

---

*End of strategy memo. Update §5 (FRAP status) when CP responds. Update §6 scope as the observable is sharpened. Update §7–8 email drafts before sending. Log outcomes and responses in §11 (not yet created — append when first reply arrives).*
