# ED–Vienna Program Map

**Purpose.** Operational backbone for ED-09.5 engagement with the Vienna quantum-nanophysics ecosystem (Arndt + Kiesel + Aspelmeyer + Hornberger + adjacent). Distills six www.quantumnano.at sub-page reviews into a single decision-ready map. Each row is a candidate empirical target; columns give the ED variable mapping, the observable to look for, the falsification criterion, and current status.

**Scope.** Vienna ecosystem only. Other regimes (FRAP at Creative Proteomics; cosmological at Stage-IV survey scale; cavity-QED at Haroche/ENS) are tracked elsewhere.

**Conventions.** **T1** = Tier-1 ready or near-ready (data accessible or askable, theory in place); **T1\*** = Tier-1 conditional on candidate-(c) sharpening; **T2** = Tier-2 fallback; **THEORY** = no current data, theoretical prediction needed first; **CLOSED** = empirically ruled out.

---

## The Map

| # | Tier | Target | ρ identification | v identification | γ_dec | ω_sys | D position | Primary observable | Falsification criterion | Status |
|:-:|:----:|:-------|:-----------------|:-----------------|:------|:------|:-----------|:-------------------|:------------------------|:-------|
| 1 | **T1** | Aspelmeyer optomechanics (Delic 2020, Magrini 2021) | mechanical mode (slow envelope) | X_cav (cavity-field amplitude quadrature) | γ_m(2n̄_th+1), bath-induced | ω_m (mechanical freq) | ~10⁻⁹–10⁻⁶ — deep oscillatory | slow envelope at ω_v = 2π·N_osc·γ_dec ≈ 8 γ_dec on raw x(t) ringdown | F0: no envelope at predicted freq; F2/F3: wrong N_osc∈[6,12] or Q_v∈[4,9]; F4/F5: wrong harmonic/triad ratio | Email v3 drafted; Delic raw x(t) NOT in public deposit; ask in flight |
| 2 | **T1** | Dumbbell-rotor librations (Quantumnano) | librational mode (slow envelope) | X_cav (same identification) | γ_lib (recoil + gas) | ω_lib (libration freq) | ~10⁻⁹ — same regime as #1 | TWO independent libration modes → built-in cross-check on envelope structure | divergent N_osc between the two modes; envelope absent in either | Add to Aspelmeyer email as parallel ask |
| 3 | **T1\*** | Gring 2010 + Brand 2018 + Tüxen 2010 (matter-wave internal-mode / conformer / isomer) | molecular c.o.m. (translational) | internal vibrational/rotational modes (candidate c) | internal-mode coupling rate to c.o.m. | mode-specific (typically THz–IR) | TBD — depends on candidate (c) sharpening | conformer- / isomer- / internal-state-resolved residual fringe contrast or phase shift, *beyond* polarizability/electric-moment fit | residual matches Hornberger standard internal-mode decoherence model; no signature distinguishable from established theory | Three published datasets exist; needs candidate (c) sharpening (1–2 wk theory) before email |
| 4 | **T1** | Nanorotor clock (1 μHz linewidth) | rotational angle / angular momentum | feedback control signal (polarization modulation) | ~1 μHz (the linewidth) | ~1 MHz (rotation freq) | ~10⁻¹² — deepest D in any system | multi-day envelope (~35 hr period) on rotation — visible only in raw unlocked-rotor signal at high time resolution | locked-rotor signal averages over envelope; raw data shows no structure at 8 μHz | Separate email; specific ask: raw unlocked-rotor traces |
| 5 | **T1** | Hackermüller 2004 thermal C₇₀ (Nature 427, 711) | molecular c.o.m. | candidate (c) — internal vibrational modes thermally excited at >3000 K | photon-emission rate (set by T) | mol vib freq | varies with T | structured residual in fringe contrast vs internal T, beyond smooth Hornberger model | smooth fit perfect; no envelope or oscillation in residual | Published 2004; reanalysis-grade dataset; parallel to #1 |
| 6 | **T1\*** | OTIMA vs KDTL cross-instrument residual (same molecule, two grating mechanisms) | molecular c.o.m. | candidate (c) — internal-mode coupling | grating-mechanism-specific (mechanical vs photodepletion) | mol vib freq | varies | SAME molecule run through OTIMA AND KDTL → residual fringe-contrast structure should DIFFER between instruments in ED-predictable way | residuals identical between OTIMA and KDTL; no instrument-dependent structure | Vienna group has run same molecules through both; needs candidate (c) + cross-instrument analysis design |
| 7 | T2 | Sisyphus cavity nonlinear cooling (Aspelmeyer/Kiesel 2013, Arndt 2013) | mechanical mode (slow envelope) | X_cav with nonlinear coupling | self-induced cavity feedback rate | ω_m | varies | sharper third-harmonic envelope content (F4 ≈ 3–6 % per §16) than in linear-cavity systems — Sisyphus nonlinearity should amplify triad signature | F4 same as linear-cavity systems; no nonlinear amplification | 2013 archived data; secondary reanalysis target |
| 8 | T2 | Eibenberger 2014 photon-recoil cross sections (PRL 112, 250402) | molecular c.o.m. | recoil-event sequence | photon-recoil rate | mech freq | TBD | per-molecule recoil-rate residual at few-% level beyond standard cross-section model | no residual; clean cross-section recovery | Precision fallback; lowest-leverage T2 |
| 9 | T2 | KDTL / LUMI / MUSCLE longitudinal meta-analysis | molecular c.o.m. (meta) | n/a (cross-instrument) | mass-dependent (per particle) | mass-dependent (per particle) | scans 0 → 1 with mass | fringe-contrast vs particle mass on log-log axis across 15-yr Vienna dataset; deviation from standard decoherence as function of mass | smooth standard-decoherence curve fits all data; no structured deviation at any mass class | Public data across all Vienna mass-record papers; meta-analysis-grade target |
| 10 | THEORY | Rotational matter-wave interferometry (future Vienna experiment) | rotational mode | TBD — likely candidate (b) or (c) | TBD | rotational frequency | TBD | envelope on rotational interference fringes | TBD pending theory | **Make prediction before experiment lands.** ED gets prior-prediction credibility if signature predicted in print |
| 11 | THEORY | Single-molecule imaging (Juffmann 2012) | molecular c.o.m. | candidate (c) candidate | TBD | TBD | TBD | per-molecule arrival-position correlation across time; sub-fringe spatial structure (3rd harmonic); time-stationarity violations | per-molecule arrivals statistically independent; no sub-fringe structure; contrast stationary | Capability exists; needs candidate (c) sharpening to produce specific predictions |
| — | **CLOSED** | Naïve mass-threshold ED-09.5 in matter-wave | molecular c.o.m. | "mass" (m_c-style cutoff) | n/a | n/a | n/a | sharp coherence cutoff at predicted m_c | MUSCLE 175 kDa coherence with µ=15.4 falsifies any m_c < 200 kDa rescue; biomolecule range 100 Da–25 kDa further constrains | **EMPIRICALLY CLOSED.** Stop trying to rescue. |

---

## Two Pillars + Two Cross-Checks + Periphery

The map collapses to a **two-pillar program architecture**:

- **Pillar A — Candidate (b), cavity-coupled regimes.** Targets #1, #2, #4 (and #7 as T2). Theory derived in §22 of Observable-Sharpening memo. Email v3 ready. Lowest-friction path to a result.
- **Pillar B — Candidate (c), internal-mode-driven matter-wave regimes.** Targets #3, #5, #6 (and #11 as future). Theory NOT derived; needs 1–2 wk sharpening pass. **High asymmetric upside if it works** (one regime → three+); fast-fail kill criterion if it doesn't.

Plus **two cross-checks** that test the program's internal consistency:
- **Cross-check 1: OTIMA vs KDTL** (#6) — same molecule, different grating mechanism. If candidate (c) is right, residuals should differ in a calculable way. Tests whether candidate (c) signal is real or artifact.
- **Cross-check 2: longitudinal mass meta-analysis** (#9) — 15 years of Vienna fringe-contrast measurements vs particle mass. Tests whether ANY mass-threshold rescue version of ED-09.5 survives.

Plus a **periphery** of theory-target items (#10, #11) and an **empirical closure** that's worth keeping visible (CLOSED row) so ED doesn't waste cycles re-litigating it.

## Decision rules

**If candidate (c) sharpening succeeds within 2 weeks:** expand the Aspelmeyer email into a **Vienna-network reanalysis program** ask covering #1, #2, #3, #5, #6 — much bigger framing, easier for senior PIs to take seriously than single-system ask.

**If candidate (c) sharpening fails within 2 weeks:** kill candidate (c) work; restrict the program to Pillar A only (#1, #2, #4, #7). Still a complete program; smaller scope, cleaner.

**If Aspelmeyer responds with raw data before candidate (c) is sharpened:** execute #1 reanalysis immediately; candidate (c) sharpening continues in parallel as time permits.

**If MUSCLE pushes the mass record past 1 MDa:** longitudinal meta-analysis (#9) tightens further; no other map entry affected.

## What this map is NOT

- Not a publication plan. The map identifies test targets, not papers to write.
- Not an exhaustive list of ED predictions. Other regimes (FRAP, galactic, cosmological) are outside Vienna scope.
- Not a commitment to all entries. T1 entries are ready-to-execute when conditions met; T2 entries are fallbacks; THEORY entries are open prediction targets.

## Maintenance

- **Move #3, #6, #11 from T1\*/THEORY to T1** if/when candidate (c) sharpening produces specific testable predictions.
- **Add new entries** if the Vienna group publishes new instrument or new dataset that maps to ED-09.5.
- **Move entries to CLOSED** if Vienna data definitively rules out the predicted signature.
- **Move entries to a "RESULT" section** if reanalysis confirms or falsifies the prediction.

This is a working document. Update in place rather than versioning.

---

*Drafted 2026-04-20 from the six www.quantumnano.at sub-page reviews + the v0.4-final Observable-Sharpening memo §22. Operational use: read before composing any Vienna-network email; reread before deciding what to work on next; update after any reanalysis result lands.*
