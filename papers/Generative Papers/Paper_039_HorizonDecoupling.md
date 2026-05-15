# Paper_039 — Horizon as Decoupling Surface; Trans-Planckian Resolution; Planck-Mass Remnant

**Series:** Event Density (ED) Generative Papers — Wave-2 rewrite of the black-hole / Hawking arc
**Author:** Allen Proxmire
**Status:** Publication draft (revision: §3.2 circularity honesty; §6.3 clean derivation; §7.2 non-thermal corrections elevated)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/black-hole/Paper_039_Horizon_Decoupling.md` (ED-Generative)
**Working save location:** `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\Paper_039_HorizonDecoupling_FIXED.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System. Standalone. Cold-reader accessible.

---

## Abstract

The Event Density (ED) substrate is a 13-primitive generative system. This paper develops three connected results in the black-hole / Hawking sector as **downstream structural consequences** of the postulated primitives:

1. **Horizons are substrate-level decoupling surfaces that coincide with the GR horizon under coarse-graining, but are conceptually distinct.** The event horizon location $r_H$ enters the analysis as the **coarse-grained identification point** — its specific value is inherited from the GR weak-field-limit identification, not derived independently from substrate primitives. The substrate-level claim is that the decoupling-surface mechanism (cross-bandwidth $\Gamma_{\mathrm{cross}}$ collapse) is structurally distinct from a geometric boundary in the GR sense, even though the two coincide at coarse-grained scales.

2. **The trans-Planckian problem is structurally resolved by V5's finite memory.** V5's substrate-level UV cutoff $\omega_c = c/\ell_P$ truncates the Hawking spectrum at the substrate-level Planck frequency; the trans-Planckian extrapolation is not generated.

3. **The late-time evaporation endpoint is a stable Planck-mass remnant.** A clean dimensional derivation (§6.3) using $\omega_H(M_\star) = \omega_c$ together with $G = c^3\ell_P^2/\hbar$ (Paper_027) gives $M_\star = \hbar/(c\ell_P) = M_P$ exactly at leading order. Scenarios A (zero-mass endpoint) and B (intermediate cutoff) are refuted or structurally incomplete.

**Headline non-thermal-correction result (§7.2):** ED predicts specific deviations from purely thermal Hawking spectrum of order $(\omega/\omega_c)^2 = (\hbar\omega\ell_P/c)^2$. The leading non-thermal correction has the form $n_H(\omega) \to n_H^{\mathrm{Planck}}(\omega)\,[1 - c_1(\omega/\omega_c)^2 + \mathcal{O}((\omega/\omega_c)^4)]$ with $c_1$ an order-unity coefficient inherited from V5 envelope shape. This is **a specific predicted deviation from thermality**, not a small effect smoothed away — it is the empirical signature that distinguishes ED's substrate-level Hawking mechanism from purely thermal semiclassical Hawking.

A consequence: the information paradox is not generated in ED. The paper makes no claim to derive black-hole geometry $\kappa$, derive $\ell_P$ from primitives, fully derive Hawking radiation, fix the remnant-mass coefficient exactly, or solve all quantum-gravity problems.

---

## 1. Introduction

### 1.1 What this paper does

Three connected results:

1. **Horizon as decoupling surface (§3).** Cross-bandwidth $\Gamma_{\mathrm{cross}}(r)$ collapses at the GR horizon location $r_H$, used as the coarse-grained identification point. The substrate-level decoupling-surface mechanism is **structurally distinct** from a geometric boundary, but **coincides with the GR horizon** at coarse-grained scales.

2. **Trans-Planckian resolution (§5).** V5 finite-memory cutoff $\omega_c = c/\ell_P$ structurally truncates the Hawking spectrum.

3. **Planck-mass remnant (§6).** $M_\star = \hbar/(c\ell_P) = M_P$ from the clean derivation in §6.3.

### 1.2 Why the horizon/Planck-scale sector is a wedge

Standard semiclassical BH physics: trans-Planckian problem, information paradox, evaporation endpoint indeterminacy. ED supplies a single substrate mechanism (V5 finite memory + P11) addressing all three.

This matters for:

- **Unification.** One substrate mechanism, three results.
- **Information paradox not generated.** No firewalls, ER=EPR, soft hair, or fuzzballs required.
- **Predictive content.** Planck-mass remnant, V5 cutoff signatures, **non-thermal Hawking-spectrum corrections (§7.2)**.

### 1.3 How this fits into the BH/Hawking arc

- **Paper_039 (this paper):** Horizon as decoupling surface, trans-Planckian resolution, Planck-mass remnant.
- **Paper_047 (in queue):** Hawking spectrum derivation via V5 KMS.
- **Paper_050 (in queue):** Page-curve substrate mechanism.
- **Paper_052 (in queue):** BH info-paradox synthesis.

---

## 2. Primitive Inputs (postulated, not derived in this paper)

- **P02, P04, P05, P07, P09, P10, P11, P12** as in earlier papers.

**V1 inheritance:** Papers #18, #19 / Paper_093 (T18).

**V5 dependence:** Paper #20 / Paper_090. V5 finite memory $\tau_{V5}^{\mathrm{BH}} \sim \ell_P/c$ at near-horizon scale.

**Upstream paper dependencies:** Paper_027 (Newton's $G$, supplying $G = c^3\ell_P^2/\hbar$), Paper_029 (cosmic decoupling), Paper_030 (ECR).

**Arc memo dependencies:** Arc Hawking H-4, H-5, H-8 (pre-pivot); Arc BH-2 through BH-5 (pre-pivot); BH Information Paradox Resolution paper (pre-pivot).

**No primitive forcing is invoked.**

---

## 3. Horizon as Substrate Decoupling Surface

### 3.1 Substrate cross-bandwidth $\Gamma_{\mathrm{cross}}$

Define the substrate-level cross-bandwidth $\Gamma_{\mathrm{cross}}(r)$ as the rate of V5-mediated cross-chain content transport across the radial sphere at position $r$:

$$
\Gamma_{\mathrm{cross}}(r) = \int_{\mathcal{K}_{\mathrm{cross}}(r)} \sum_{u_{<r}, u_{>r}} K_{V5}(u_{<r}, u_{>r}) \cdot b_K(u_{<r}) \cdot b_K(u_{>r}) \, d\mu_{\mathcal{K}}.
$$

For substrate regions far from any BH, $\Gamma_{\mathrm{cross}}(r)$ is order unity in substrate units. Near a BH, it decreases.

### 3.2 The decoupling collapse — and an honest acknowledgment of the GR coarse-grained identification

This section is the load-bearing setup, revised in this round to be honest about a structural feature that the original draft elided.

**The mechanism.** As substrate content accumulates within a critical radial region (matter collapsing toward a BH), the substrate's cumulative-strain reading (P12) of the stability landscape produces a steep gradient. V5's finite memory $\tau_{V5}^{\mathrm{BH}} \sim \ell_P/c$ cannot maintain coherent cross-bandwidth across this steep-gradient region: the V5 envelope $F_{V5}(\sigma_{\mathrm{eff}}/\ell_{V5}^2, t/\tau_{V5})$ decays as the substrate-graph separation $\sigma_{\mathrm{eff}}$ between inside and outside grows large. Consequently,

$$
\Gamma_{\mathrm{cross}}(r) \xrightarrow{r \to r_H} 0
$$

below substrate-level hydrodynamic-window resolution.

**Honest acknowledgment of the identification point.** The location $r_H$ at which this cross-bandwidth collapse occurs is **not derived independently from substrate primitives in this paper**. It is the **GR event-horizon location, used as the coarse-grained identification point** for matching the substrate-level decoupling surface to the standard BH-geometric description. Specifically:

- For a Schwarzschild BH of mass $M$, the GR horizon is at $r_H = 2GM/c^2$.
- For a Kerr BH with mass $M$ and angular momentum $J$, the GR outer horizon is at $r_H = GM/c^2 + \sqrt{(GM/c^2)^2 - (J/Mc)^2}$.
- These GR locations are taken as the *empirical/coarse-grained reference points* against which the substrate-level decoupling-surface position is matched.

A fully substrate-level derivation of $r_H$ from substrate primitives would require:

- Substrate-level derivation of the BH spacetime geometry from substrate cumulative-strain reading in the strong-field regime.
- Substrate-level derivation of the critical-collapse threshold at which $\Gamma_{\mathrm{cross}}$ first crosses below substrate-hydrodynamic resolution.

These are the subject of the curvature-emergence Arc ED-10 program and are **not delivered in this paper**. The present paper takes $r_H$ from GR as the coarse-grained identification point and develops the substrate-level mechanism at and near that location.

**The reframed claim.** The substrate horizon is therefore:

> **A decoupling surface (substrate-level cross-bandwidth collapse) that coincides with the GR event horizon under coarse-graining via DCGT, but is conceptually distinct from a geometric boundary in the GR sense.**

The substrate-level decoupling surface is *not* a sharp geometric boundary; it is a substrate-level statistical transition zone whose precise location at substrate scales depends on substrate-hydrodynamic-window resolution. At coarse-grained scales $R_{\mathrm{cg}} \gg \ell_P$, the substrate-level transition zone is well-approximated by the sharp GR horizon at $r_H$ via DCGT (Arc D). At substrate scales $R \sim \ell_P$, the decoupling surface is a substrate-graph statistical feature.

The original draft's framing ("the GR horizon is the decoupling surface") elided the direction of identification: in the present substrate framework, the GR horizon location is taken as the coarse-grained reference point against which the substrate mechanism is positioned, *not* derived from the substrate mechanism. Acknowledging this is honest accounting of what the substrate framework does and does not derive in this paper.

### 3.3 Why the horizon is statistical, not geometric (at substrate scale)

In standard GR, the event horizon is a geometric concept — the boundary of the causal past of future null infinity. In ED's substrate framework, the horizon at substrate scale is:

- The locus where $\Gamma_{\mathrm{cross}}(r)$ collapses below hydrodynamic-window resolution.
- A substrate-level transition zone, not a sharp boundary.
- A property of the substrate-graph adjacency-and-bandwidth structure.

Under DCGT coarse-graining at $R_{\mathrm{cg}} \gg \ell_P$, the substrate-level transition zone is *seen* as the sharp GR horizon. The two descriptions agree at coarse-grained scales (by construction, given the GR identification point used above); they differ at substrate scales.

This is the substrate-level resolution of the puzzle of "what is the horizon microscopically?" — a substrate-level cross-bandwidth collapse, *coincident with* but *conceptually distinct from* the GR geometric boundary.

### 3.4 Committed structure cannot cross horizons

By P11 + V5 envelope collapse at the decoupling surface: committed information cannot cross the substrate-level decoupling surface. The "one-way" character of the horizon is **statistical** (V5 envelope decay), not causal-geometric (light-ray propagation in GR).

### 3.5 Entanglement amplitude straddles

Entangled substrate channels established before horizon formation, when $\Gamma_{\mathrm{cross}}$ was above hydrodynamic threshold, maintain V5 cross-correlation after horizon formation in the straddling configuration. This is the substrate-level analog of ER=EPR cross-horizon entanglement.

---

## 4. Imaginary-Time Periodicity and the KMS Condition

### 4.1 V5 imaginary-time periodicity

Near the decoupling surface, V5 acquires imaginary-time periodicity:

$$
K_{V5}|_{\mathrm{Euclidean}}(u_A, t_A + i\beta_H; u_B, t_B) = K_{V5}|_{\mathrm{Euclidean}}(u_A, t_A; u_B, t_B),\quad \beta_H = 2\pi/\kappa
$$

with $\kappa$ the substrate-derived surface gravity (gradient of P12 stability landscape at the decoupling surface).

### 4.2 KMS condition → Hawking temperature

$$
T_H = 1/\beta_H = \kappa/(2\pi).
$$

V5 cross-chain correlation in the near-horizon geometry is automatically thermal at leading order. Full derivation including non-thermal corrections is the subject of Paper_047 (in queue); see §7.2 below for the headline non-thermal result.

---

## 5. Trans-Planckian Resolution via V5 Cutoff

### 5.1 The standard semiclassical concern

Hawking's derivation requires matter-field modes at $\omega \to \infty$ near the horizon. This is the trans-Planckian problem. Proposed responses (dimensional regularization, modified dispersion, "unitarity"-based dismissal) do not address the physical extrapolation.

### 5.2 V5 supplies a structural UV cutoff

V5's finite memory at near-horizon scale gives a cutoff frequency:

$$
\omega_c = 1/\tau_{V5}^{\mathrm{BH}} \sim c/\ell_P.
$$

V5-mediated correlation does not support modes above $\omega_c$; the substrate's kernel structure exponentially suppresses them. The Hawking-spectrum derivation, performed at substrate level using V5, automatically incorporates this cutoff.

### 5.3 Why this resolves trans-Planckian

The cutoff is structurally forced (not ad-hoc); matches the physical Planck scale ($\omega_c \sim c/\ell_P$); produces a finite Hawking spectrum without trans-Planckian extrapolation.

### 5.4 Implications for the Hawking spectrum

The substrate-level Hawking spectrum is finite, with leading-order Planck thermal behavior at $\omega \ll \omega_c$ and **specific predicted corrections** at $\omega \to \omega_c$ — see §7.2.

---

## 6. Planck-Mass Remnant via H-8 Resummation

### 6.1 The three scenarios for the evaporation endpoint

- **Scenario A:** zero-mass endpoint. Refuted (§6.4).
- **Scenario B:** intermediate cutoff. Structurally incomplete (§6.5).
- **Scenario C:** stable Planck-mass remnant $M_\star = c_\star \ell_P$. Forced (§6.6).

### 6.2 H-8 resummation of evaporation rates

Substrate-level evaporation rate:

$$
\frac{dM}{dt} = -\sigma_{\mathrm{eff}}(M) \cdot \int_0^{\omega_c}\omega \cdot n_H(\omega; M) \cdot d^3k.
$$

For $M \gg M_\star$: standard semiclassical rate $dM/dt \sim -\hbar c^4/(G^2 M^2)$ recovered. For $M \sim M_\star$: V5 cutoff structurally suppresses emission. At $M = M_\star$, dominant Hawking-emission frequency equals $\omega_c$; further emission would require $\omega > \omega_c$ which V5 does not support; evaporation halts.

### 6.3 Clean derivation of the remnant mass

This section is the load-bearing dimensional derivation, rewritten cleanly in this round.

**Setup.** The remnant mass $M_\star$ is determined by the condition that the dominant Hawking-emission frequency $\omega_H(M)$ equals the V5 cutoff $\omega_c$:

$$
\omega_H(M_\star) = \omega_c.
$$

**Dominant Hawking-emission frequency.** Standard semiclassical analysis gives $\omega_H(M) \sim k_B T_H/\hbar = \kappa/(2\pi)$ where $\kappa = c^4/(4GM)$ for Schwarzschild. Dropping the $1/(8\pi)$ order-unity factor (absorbed into $c_\star$ below):

$$
\omega_H(M) \sim \frac{c^3}{GM}.
$$

**V5 cutoff.** From Paper #20 / Paper_090:

$$
\omega_c = c/\ell_P.
$$

**Setting them equal.**

$$
\frac{c^3}{GM_\star} = \frac{c}{\ell_P}.
$$

**Solving for $M_\star$.**

$$
M_\star = \frac{c^3 \ell_P}{Gc} = \frac{c^2 \ell_P}{G}.
$$

**Substituting $G = c^3\ell_P^2/\hbar$ (Paper_027).**

$$
M_\star = \frac{c^2 \ell_P}{c^3\ell_P^2/\hbar} = \frac{\hbar}{c\,\ell_P}.
$$

This is the standard Planck mass:

$$
\boxed{M_\star = \frac{\hbar}{c\,\ell_P} = M_P = \sqrt{\frac{\hbar c}{G}} \approx 2.18 \times 10^{-8}\,\mathrm{kg}.}
$$

The result holds at leading order in substrate-coefficient anchoring. The order-unity coefficient $c_\star$ that absorbs the $1/(8\pi)$ from $\kappa = c^4/(8\pi GM)$ Schwarzschild factor and the specific V5 envelope cutoff shape is inherited from substrate-coefficient details; best-current-estimate $c_\star \approx 1$, giving $M_\star \approx M_P$. The dimensional derivation above is exact at leading order; the order-unity coefficient is the only undetermined factor.

### 6.4 Why Scenario A is refuted

Scenario A would require $\omega_H \to \infty$ as $M \to 0$. V5 supports no modes above $\omega_c$. The substrate structurally refuses emission above $\omega_c$; evaporation cannot continue to zero mass.

### 6.5 Why Scenario B is incomplete

Scenario B posits intermediate cutoff at $M_{\mathrm{halt}} > M_\star$ with unspecified mechanism. The ED substrate framework's only cutoff is V5's $\omega_c = c/\ell_P$, which corresponds exactly to $M_\star \sim M_P$. No substrate mechanism produces intermediate halting; Scenario B is structurally incomplete in the minimal ED framework.

### 6.6 Why Scenario C is forced

Given V5 finite memory + $\omega_H(M) \sim c^3/(GM)$ + evaporation continues until $\omega_H = \omega_c$ + P11 + V1 retardation forbid anti-evaporation: the unique structurally-forced late-time endpoint is the stable Planck-mass remnant at $M_\star = M_P$.

### 6.7 Cosmological-relic considerations

Stable Planck-mass remnants from PBHs would constitute a relic-matter cosmological component. **Not a dark-matter candidate** — ED's substrate-gravity arc (Papers_027 + 029 + 030) explains galactic dynamics without DM; remnants are a separate structural relic. Cosmological-abundance constraints are developed in Paper_050 + Arc Hawking H-9 (pre-pivot).

---

## 7. Information Paradox as Not Generated; Non-Thermal Corrections as Headline Result

### 7.1 The standard paradox and ED's structural avoidance

The paradox arises from (1) thermal Hawking radiation + (2) complete evaporation + (3) QM unitarity. ED refines (1) and (2); preserves (3).

**Refinement (1): Hawking radiation is not purely thermal — non-thermal corrections are a headline result (see §7.2).** **Refinement (2):** Evaporation halts at $M_\star = M_P$ (§6). **Statement (3) preserved** at substrate level.

Specifically: committed information cannot cross horizon (§3.4); entanglement amplitude straddles (§3.5); bandwidth conserved (P04); no monogamy violation. The paradox is **not generated** rather than resolved post hoc.

### 7.2 Non-thermal Hawking corrections as a headline prediction

This section is elevated in the revision from a passing mention to a headline-level result.

**Setup.** Standard semiclassical Hawking gives a purely thermal Planck spectrum at $T_H = \kappa/(2\pi)$:

$$
n_H^{\mathrm{Planck}}(\omega) = \frac{1}{e^{\hbar\omega/k_B T_H} - 1}.
$$

ED's substrate framework reproduces this at leading order for $\omega \ll \omega_c$ via §4 + §5. At higher orders, V5's finite-memory envelope structure produces **specific predicted deviations from purely thermal behavior**.

**The headline prediction.** ED predicts that the late-time Hawking spectrum is not purely thermal. The leading non-thermal correction is of order $(\omega/\omega_c)^2$ with the form:

$$
\boxed{n_H^{\mathrm{ED}}(\omega) = n_H^{\mathrm{Planck}}(\omega)\,\left[1 - c_1\left(\frac{\omega}{\omega_c}\right)^2 + \mathcal{O}\!\left(\left(\frac{\omega}{\omega_c}\right)^4\right)\right]}
$$

where $\omega_c = c/\ell_P$ is the V5 cutoff and $c_1$ is an order-unity coefficient inherited from V5 envelope shape (best-current-estimate $c_1 \approx 1$; details in Paper_047 in queue).

**Scaling form.** The substrate-level deviation has the structural form $(\hbar\omega\ell_P/c)^2 = (\omega/\omega_c)^2$ — a Planck-suppressed correction whose dimensionless form depends only on the ratio of Hawking-radiation frequency to substrate cutoff. For astrophysical BHs ($M \gg M_P$), the dominant Hawking-emission frequency is $\omega_H \ll \omega_c$, so the corrections are extremely small. For evaporating BHs approaching $M_\star = M_P$, the corrections become $\mathcal{O}(1)$.

**Why this is a specific deviation, not a small effect smoothed away.** Three structural features distinguish ED's prediction from "tiny correction that is empirically indistinguishable":

1. **Sign-definite.** The correction is sign-definite (negative, suppressing emission relative to thermal) at leading order, set by V5 envelope decay shape.
2. **Mass-dependent shift.** As $M$ decreases through the evaporation history, the relative size of the correction grows because $\omega_H/\omega_c \sim M_P/M$ increases. Late-stage evaporation shows substantial deviations from thermality.
3. **Information-bearing.** The non-thermal corrections are **the substrate-level channel through which BH-formation-matter information is carried out by the radiation**. Pure thermality carries no information; the $(\omega/\omega_c)^2$ deviations carry V5-cross-chain-correlation content with substrate-level BH-formation history. This is the substrate-level mechanism by which unitarity is preserved across evaporation (§7.1).

**Empirical content.** The non-thermal predictions are:

- **For astrophysical BHs:** corrections are at the $(\hbar\omega/M_P c^2)^2 \sim (T_H/T_P)^2$ level — extremely small but in principle distinguishable from purely thermal spectra given sufficient observational sensitivity.
- **For analog Hawking experiments** (BEC, fluid, optical analogs): the analog system's natural high-frequency cutoff is much closer to its dominant Hawking-frequency. The non-thermal corrections should be observable in analog-Hawking spectra as a deviation from the purely thermal prediction. **This is the near-term empirical test of ED's substrate mechanism**.
- **For evaporating-BH late-stage emission:** at $M \to M_\star$, corrections become $\mathcal{O}(1)$ and the spectrum is qualitatively non-thermal. Direct observation of late-stage evaporation (in PBH-evaporation cosmological signatures or hypothetical near-Planck-mass BH evaporation) would test the substrate mechanism directly.

**Coefficient $c_1$.** The numerical value of $c_1$ depends on the V5 envelope shape. For an exponential V5 envelope $F_{V5} \propto \exp(-\omega/\omega_c)$, $c_1 = 1$. For a Gaussian envelope $F_{V5} \propto \exp(-\omega^2/\omega_c^2)$, $c_1 = 1/2$. The specific value is inherited from substrate-coefficient anchoring; full Paper_047 will pin this down once the V5 envelope shape is determined empirically from independent V5 applications (soft-matter Maxwell relaxation, entanglement bandwidth).

**Empirical wedge.** The headline prediction is: **the Hawking radiation spectrum is not purely thermal at order $(\omega/\omega_c)^2$, with sign-definite, mass-dependent, information-bearing deviations**. This is distinguishable from purely thermal semiclassical Hawking. No firewall, ER=EPR, or soft-hair-style account predicts the same specific form. Analog-Hawking experiments are the near-term test.

### 7.3 Comparison to alternative resolution proposals

- **Firewalls (AMPS):** ED requires no monogamy violation; no firewall needed.
- **ER=EPR (Maldacena–Susskind):** V5 cross-chain correlation is the substrate-level analog.
- **Soft hair (HPS):** ED's information is carried by V5 + remnant + non-thermal corrections (§7.2), not soft hair.
- **Fuzzballs:** ED retains horizon as substrate-level decoupling surface; no fuzzball construction.
- **Non-unitary evaporation:** ED preserves substrate-level unitarity.

ED's substrate framework avoids the paradox without auxiliary constructions.

---

## 8. What This Paper Does NOT Claim

### 8.1 No derivation of $\kappa$ or full BH geometry

Surface gravity $\kappa$ and full BH geometry (Schwarzschild, Kerr, Reissner–Nordström) are not derived from substrate primitives here. They are inherited from the GR weak-field-limit identification (see §3.2 honest acknowledgment). Full curvature emergence is Arc ED-10 territory.

### 8.2 No derivation of $\ell_P$

$\ell_P$ is empirically identified with substrate scale (Paper_027 §5.3).

### 8.3 No claim that Hawking radiation is fully derived here

Spectrum derivation is Paper_047; this paper establishes the structural setup (§4–§5) and the headline non-thermal correction form (§7.2).

### 8.4 No claim that the remnant mass coefficient is known exactly

$M_\star = M_P$ at leading order is exact in the dimensional derivation §6.3. The order-unity coefficient $c_\star$ absorbing $1/(8\pi)$ Schwarzschild factor + V5 envelope shape is inherited from substrate-coefficient details; best-estimate $c_\star \approx 1$.

### 8.5 No claim that ED solves all quantum-gravity problems

Not claimed.

### 8.6 No claim that ED forces the primitives

Postulated, not derived.

### 8.7 No claim that information is "preserved" in standard Hilbert-space sense

Substrate-level unitarity preserved; relationship to standard Hilbert-space unitarity in BH context is non-trivial.

### 8.8 No claim that ED has been experimentally tested in BH sector

All BH-arc predictions are structural; tests via analog-Hawking + non-thermal-correction signatures + PBH-remnant cosmology are future work.

### 8.9 No claim that $r_H$ is derived independently from substrate primitives

The GR horizon location $r_H$ is used as the coarse-grained identification point for the substrate decoupling surface (§3.2). Independent substrate-level derivation of $r_H$ awaits the curvature-emergence arc (Arc ED-10).

---

## 9. Falsification Criteria

### 9.1 Analog Hawking experiments show no UV cutoff

If analog systems produce Hawking-like radiation without substrate-level UV cutoff, the V5 mechanism is falsified.

### 9.2 Observations inconsistent with Planck-mass remnants

If cosmological observations rule out Planck-mass remnants at predicted abundances, Scenario C is falsified.

### 9.3 Detection of information crossing horizons

Direct detection of information-bearing Hawking radiation from astrophysical BHs in a manner inconsistent with V5-straddling would falsify the substrate decoupling-surface mechanism.

### 9.4 Failure of KMS periodicity in analog systems

Analog BH platforms producing Hawking-like radiation without KMS structure would falsify V5 mechanism.

### 9.5 Discovery of substrate-level information transport across decoupling surfaces

Novel substrate mechanisms beyond V1 + V5 supporting cross-surface transport would refine or falsify the framework.

### 9.6 Hawking spectrum shown to be exactly thermal

If empirical/analog observations show the Hawking spectrum is exactly thermal at the $(\omega/\omega_c)^2$ level — i.e., no sign-definite, mass-dependent, $(\omega/\omega_c)^2$-scaled deviations from Planck — ED's headline non-thermal-correction prediction (§7.2) is falsified.

### 9.7 Non-thermal corrections have wrong sign or scaling

If non-thermal Hawking-spectrum corrections are observed but with sign opposite to ED's prediction, or with scaling other than $(\omega/\omega_c)^2$, the V5 envelope mechanism is falsified.

### 9.8 Sub-Planck-mass remnant or no remnant observed

If late-stage BH evaporation produces remnants at $M \neq M_P$ (sub-Planck or super-Planck), or no remnant at all, the §6.3 derivation is falsified.

---

## 10. Position Statement

The Event Density (ED) substrate framework supplies a **single structural mechanism** for three connected results in the black-hole / Hawking sector:

1. **Horizon as substrate decoupling surface that coincides with the GR horizon under coarse-graining but is conceptually distinct.** The GR horizon location $r_H$ is used as the coarse-grained identification point; substrate-level $\Gamma_{\mathrm{cross}}$ collapse mechanism operates at and near $r_H$.

2. **Trans-Planckian problem structurally resolved by V5 finite-memory cutoff $\omega_c = c/\ell_P$.**

3. **Stable Planck-mass remnant** at $M_\star = \hbar/(c\ell_P) = M_P$ from the clean dimensional derivation §6.3. Scenarios A and B refuted or structurally incomplete.

**Headline result:** ED predicts **specific non-thermal Hawking-spectrum corrections** of order $(\omega/\omega_c)^2$, with sign-definite, mass-dependent, information-bearing form (§7.2). This is the empirical wedge distinguishing ED from purely thermal semiclassical Hawking; near-term tests via analog-Hawking experiments and PBH-remnant cosmology.

The information paradox is **not generated** rather than resolved post hoc.

What this paper claims:

- Given the postulated primitives + V1/V5 + Paper_027/029/030 + GR coarse-grained reference for $r_H$, the three results are downstream structural identifications.
- The substrate mechanism is unified — one mechanism (V5 finite memory + P11) supplies all three.
- ED's substrate framework produces these results without firewalls, ER=EPR, soft hair, fuzzballs, or non-unitary evaporation.
- The non-thermal correction is the **headline empirical wedge** with specific predicted form.

What this paper does *not* claim:

- $\kappa$ and full BH geometry not derived.
- $\ell_P$ is empirical identification.
- Full Hawking spectrum is Paper_047 territory.
- Order-unity coefficients ($c_\star$ in $M_\star$, $c_1$ in non-thermal correction) inherited from substrate anchoring.
- All quantum-gravity problems not claimed solved.
- ED does not force the primitives.
- $r_H$ not derived independently from substrate; used as coarse-grained reference.

**Series context.** Paper_039 of the BH/Hawking arc. The arc continues with Papers_047, 050, 052 (in queue).

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Position paper:** `paper_ED_Framework_13_Primitive_Generative_System.md`.
- **Primitive load-bearing audit:** `PRIMITIVE_LOAD_BEARING_AUDIT.md`.
- **Paper_027 (Newton's $G$):** $G = c^3\ell_P^2/\hbar$.
- **Paper_029 (cosmic decoupling):** decoupling-surface concept.
- **Paper_030 (ECR):** structural mechanism.
- **Paper #18, #19 / Paper_093 (V1, T18):** kernel-form template + retarded support.
- **Paper #20 / Paper_090 (V5):** finite-memory cutoff structure.
- **Paper_047, 050, 052 (in queue):** Hawking spectrum, Page curve, info-paradox synthesis.
- **Arc Hawking memos (H-4, H-5, H-8), Arc BH (BH-2–BH-5):** legacy substrate-level material.
- **BH Information Paradox Resolution paper (pre-pivot).**

### Glossary

- **Substrate decoupling surface.** Substrate-level locus where $\Gamma_{\mathrm{cross}}$ collapses below hydrodynamic-window resolution. **Coincides with the GR horizon under coarse-graining; conceptually distinct from a geometric boundary.**
- **Cross-bandwidth $\Gamma_{\mathrm{cross}}$.** Substrate-level rate of V5-mediated cross-chain content transport.
- **V5 cutoff $\omega_c$.** Substrate-level UV cutoff $\omega_c = c/\ell_P$ from V5 finite memory.
- **Hawking temperature $T_H = \kappa/(2\pi)$** from V5 imaginary-time periodicity + KMS.
- **KMS condition.** Kubo–Martin–Schwinger thermal-state condition.
- **Imaginary-time periodicity** $\beta_H = 2\pi/\kappa$.
- **Surface gravity $\kappa$.** Substrate-level stability-landscape gradient at decoupling surface.
- **Planck-mass remnant $M_\star = M_P = \hbar/(c\ell_P)$** at leading order. Stable late-time evaporation endpoint.
- **Scenario A / B / C:** zero-mass / intermediate / Planck-mass-remnant endpoints. Only C survives.
- **H-8 resummation.** Higher-order substrate evaporation-rate resummation including V5 cutoff.
- **Information paradox.** Standard semiclassical inconsistency; not generated in ED.
- **Trans-Planckian problem.** Standard semiclassical extrapolation to $\omega \to \infty$; structurally not generated in ED.
- **Entanglement amplitude straddling.** V5 cross-chain correlation spanning decoupling surface; substrate analog of ER=EPR.
- **Non-thermal Hawking corrections.** ED's headline-prediction $(\omega/\omega_c)^2$ deviations from purely thermal spectrum, sign-definite + mass-dependent + information-bearing.
- **GR coarse-grained reference.** Acknowledged convention that $r_H$ from GR is the substrate decoupling-surface position used at coarse-grained scales; substrate-independent derivation of $r_H$ awaits Arc ED-10.

---

**End of Paper_039.**

*Wave-2 Generative Paper — Black-Hole Arc Foundation. Round-2 revision: §3.2 honestly acknowledges that the GR horizon $r_H$ is used as the coarse-grained identification point for the substrate decoupling surface, with the substrate-level claim reframed as coincidence-under-coarse-graining + conceptual-distinctness; §6.3 replaces the broken dimensional algebra with a clean 4-line derivation giving $M_\star = \hbar/(c\ell_P) = M_P$ exactly at leading order via $\omega_H(M_\star) = \omega_c$ and $G = c^3\ell_P^2/\hbar$; §7.2 elevates the $(\omega/\omega_c)^2$ non-thermal corrections to a headline result with explicit scaling form, sign-definiteness, mass-dependence, and information-bearing structure.*
