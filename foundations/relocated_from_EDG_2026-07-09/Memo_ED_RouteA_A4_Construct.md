# Memo_ED_RouteA_A4_Construct — Construction Memo (Route A4 Attempt)

**Series:** Wave-3 Construction Memo (Cosmology Arc + ED-SC Arc; Route A Substrate-Graph Derivation of $H_0$; Path-A4 from Memo_ED_RouteA_Scoping_Wave3 §7.2)
**Status:** Substrate-graph attempt at Route A4 — derivation of the late-universe Hubble scale $H_0$ from the substrate-action density asymptotic $\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$ at the saturation regime, applying the Paper_027 dimensional-rearrangement template. **Not a derivation. No new primitives.** Outcome: **substantive partial-positive — A4 closes at substrate-parameter-INHERITED level analogous to Paper_027's Newton's $G$ closure**, supplying $H_0$ via dimensional rearrangement from substrate parameters $(\ell_{\mathrm{ED}}, c, \hbar, \Theta_{\mathrm{ED}})$. The substrate-graph derivation of $\Theta_{\mathrm{ED}}$ value from sub-primitive content remains OPEN (RA-OPEN-4a, newly introduced). Closure level matches Paper_027's M3 + value-INHERITED-at-substrate-parameter-level pattern.
**Date:** 2026-05-16
**Anchors:** Memo_ED_RouteA_Scoping_Wave3 (Route A4 scope; canonical $\ell_{V_5}(H_0)$ formulation; DCGT parametric transparency $H_0 \sim c/\ell_{V_5}$); Paper_ED_SC_4_9 ($S_{\mathrm{sub}}$ + kernel-derivative structure); Paper_027 (Newton's $G$ via dimensional rearrangement — template); Paper_073 (DCGT hydrodynamic-window); Paper_087 (P02 + P04 + **P12 ED-threshold**); Paper_012 (P-RB-1 substrate-c + $\hbar$); Paper_090 (V5 cross-chain finite-memory; ~40 OOM cross-scale); Paper_ED_Cos_01 (M3; Q1A + Q2A + C3 + IC-INHERITED chain); Paper_ED_Cos_05 (M3 conditional on Route A); Paper_038_5 (Λ-smallness reframing — $\rho_\Lambda$ reduces to Route A + Friedmann); Memo_ED_Q1Q2_JointClosure_Construct (Q1A surviving A.1: $T^{\mu\nu}_{\mathrm{sub}} = -g^{\mu\nu}\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$ at saturation).

> ⚠️ **Correction (2026-07-06):** This memo cites Θ_ED as "Paper_087 P12 (ED-threshold)." That attribution is incorrect — canonical `Paper_087` P12 is a stability-landscape functional unrelated to an event-density threshold. Θ_ED's actual (uncritically-inherited) origin is `Paper_ED_CCC_ConformalCyclicCosmology.md` §3.2/§3.7, itself now flagged. This does not change this memo's tier verdicts (Θ_ED remains substrate-parameter-INHERITED throughout) — it only corrects the primitive citation. See `event-density/docs/Scoping_ThetaED_FirstPrinciples_2026-07-06.md`.

---

## §1 Restated A4 target

### §1.1 The A4 closure target

Per Memo_ED_RouteA_Scoping_Wave3 §4.4 + §5 finding (all four routes converge on $H_0 \sim c/\ell_{A4}$ parametric structure): show that the **substrate-action density asymptotic in the saturation regime** supplies a characteristic length $\ell_{A4}$ such that

$$
H_0 = c / \ell_{A4} \quad\text{via DCGT translation + Friedmann inheritance}
$$

with $\ell_{A4}$ derivable substrate-graph from primitive content via the **Paper_027 dimensional-rearrangement template**.

### §1.2 Substrate-side reduction via Q1A + Q2A + C3

The Q1A + Q2A + C3 chain (Memo_ED_Q1Q2_JointClosure_Construct + Memo_ED_ChainClass_C3_Construct) closes the form-IDENTIFIED side:

- **Q1A:** at uniform-$\Psi$ saturation, substrate-side Noether $T^{\mu\nu}_{\mathrm{sub}} = -g^{\mu\nu}\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$
- **Q2A:** DCGT preserves uniform structure → $T^{\mu\nu}_{\mathrm{eff}} = -g^{\mu\nu}\rho_\Lambda$ at leading order in $\varepsilon$
- **Friedmann:** $H_0^2 = (8\pi G_{\mathrm{eff}}/3) \rho_\Lambda$

So the value-DERIVED target reduces to: **derive $\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$ from substrate parameters** ($\rho_\Lambda = \mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$ modulo standard DCGT coefficient; $G_{\mathrm{eff}}$ via Paper_027 inherited). The Route A4 target reduces to substrate-graph derivation of the substrate-action density's saturation-regime value.

### §1.3 The canonical Λ-smallness reduction (Paper_038_5)

Per Paper_038_5 §3.7: $\rho_\Lambda^{\mathrm{substrate}} = (3/8\pi) H_0^2 \cdot M_P^2$ with $M_P^2$ via Paper_027. Inverting: $H_0^2 = (8\pi/3) \rho_\Lambda / M_P^2 \sim \mathcal{L}_{\mathrm{sub}}^{\mathrm{const}} / M_P^2$ modulo standard coefficients. The Route A4 derivation must therefore supply $\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}} / M_P^2 \sim H_0^2$ at the right order of magnitude — capturing the famous 120-OOM $(H_0/M_P)^2 \sim 10^{-122}$ hierarchy.

---

## §2 Extracted SC-4.9 asymptotic structure

Per Paper_ED_SC_4_9, the substrate-action density at saturation:

### §2.1 Kernel-derivative suppression

In the saturation regime, kernel derivatives vanish (Memo_ED_ChainClass_C3_Construct §3.1): $\nabla_K\Psi = 0$ for all $K \in \{V_1, V_5\}$. The substrate-action density collapses to its **potential-only component**:

$$
\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}} = \mathcal{L}_{\mathrm{sub}}[\Psi^{\mathrm{const}}, 0, 0] = U(\Psi^{\mathrm{const}})
$$

where $U(\Psi)$ is the potential-only substrate-action functional evaluated at uniform $\Psi^{\mathrm{const}}$.

### §2.2 Uniform-$\Psi$ limit at saturation

Per Paper_ED_CCC §3.7 + Paper_087 P12 (ED-threshold), at saturation the substrate event-density crosses $\Theta_{\mathrm{ED}}$ from below; the configuration is "globally-homogeneous, kernel-active, individuated initial state." The substrate $\Psi^{\mathrm{const}}$ value at this configuration is **the ED-threshold value**:

$$
\Psi^{\mathrm{const}}_{\mathrm{saturation}} = \Theta_{\mathrm{ED}}
$$

This identification is corpus-internal: saturation regime = at-threshold regime; $\Psi$ value at saturation = $\Theta_{\mathrm{ED}}$.

### §2.3 Action-density constancy + value structure

Combining §2.1 + §2.2:

$$
\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}} = U(\Theta_{\mathrm{ED}})
$$

The substrate-action density at saturation is the potential-only substrate-action functional evaluated at the ED-threshold value. **Substrate-graph derivation of $\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$ value reduces to substrate-graph derivation of $U(\Theta_{\mathrm{ED}})$** — i.e., the form of $U$ + the value of $\Theta_{\mathrm{ED}}$.

For the canonical leading-order form $U(\Psi) \sim \Psi$ (substrate-action density scales linearly with substrate event-density per Paper_ED_SC_4_9 + Paper_087 P02 + P04 structural reading), this further reduces to:

$$
\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}} \sim \Theta_{\mathrm{ED}}
$$

up to a substrate-graph-derivable dimensionless coefficient. The Route A4 derivation therefore reduces to: **substrate-graph derivation of $\Theta_{\mathrm{ED}}$ value.**

---

## §3 Applying Paper_027 dimensional-rearrangement template

### §3.1 Paper_027 template summary

Per Paper_027, Newton's $G$ closes at substrate-graph M3 via dimensional rearrangement: given substrate parameters $\ell_{\mathrm{ED}} (= \ell_P), c, \hbar$ with substrate-graph identifications (Paper_087 P02 + P12 + Paper_012 P-RB-1), the unique dimensionally-consistent combination giving $G$ is

$$
G = \frac{\hbar c}{M_P^2} = \frac{\hbar c^3}{(\ell_P^2 c^4 / \hbar) \cdot c^{-2}} \cdot c^{-4} = \frac{\ell_P^2 c^3}{\hbar}.
$$

Substrate parameters $(\ell_P, c, \hbar)$ are substrate-parameter INHERITED — they enter the corpus as axiomatic substrate constants per Paper_087 + Paper_012. Paper_027's M3 closure is **form-DERIVED via dimensional rearrangement + value-INHERITED at substrate-parameter level**.

### §3.2 Template applied to Route A4

For Route A4, available substrate parameters:

| Parameter | Origin | Dimension |
|---|---|---|
| $\ell_{\mathrm{ED}} = \ell_P$ | Paper_087 + Paper_027 | Length |
| $c$ | Paper_012 P-RB-1 (substrate-c) | Length/Time |
| $\hbar$ | Paper_012 (substrate rate-of-becoming bound) | Energy·Time |
| $\Theta_{\mathrm{ED}}$ | Paper_087 P12 (ED-threshold) | Event-density (per substrate-volume per substrate-time) |
| $\tau_{V_5}$ | Paper_090 (V5 finite-memory time) | Time |

The Route A4 target is a length $\ell_{A4}$. Dimensionally-consistent combinations:

**Combination 1 (Planck-only):** $\ell_{A4} \sim \ell_P$ — gives Planck-scale length. **Rules out cosmological scale by ~60 OOM.** Not Route A4.

**Combination 2 (with $\Theta_{\mathrm{ED}}$):** $\Theta_{\mathrm{ED}}$ has dimension $[L^{-3} T^{-1}]$ (event-density per substrate-volume per substrate-time). Combined with $c$: $\Theta_{\mathrm{ED}} \cdot c \cdot \ell_P^3 \sim$ dimensionless. Then $\ell_{A4}$ from $\ell_P \cdot (\Theta_{\mathrm{ED}} \cdot c \cdot \ell_P^3)^{-1/4}$ has dimension of length (Planck-scale modulated by a dimensionless factor depending on $\Theta_{\mathrm{ED}}$ value).

**Combination 3 (with $\tau_{V_5}$):** $\ell_{V_5} = c\tau_{V_5}$ is a length. $\ell_{A4} \sim \ell_{V_5}$ directly. This is Route A1's framing — and reduces to "what determines $\tau_{V_5}$" which is the substrate-research-frontier question.

**Combination 4 (with both $\Theta_{\mathrm{ED}}$ and $\tau_{V_5}$):** various combinations; in practice these are not independent — both are primitive-content parameters whose values are substrate-parameter-INHERITED.

### §3.3 The substrate hierarchy and the 120-OOM problem

Cosmological observation: $H_0^{-1} \approx 4.6 \times 10^{17}$ s; $R_H = c/H_0 \approx 1.4 \times 10^{26}$ m. Compared to Planck: $\ell_P \approx 1.6 \times 10^{-35}$ m, $\tau_P = \ell_P/c \approx 5.4 \times 10^{-44}$ s. Ratios:

$$
\frac{R_H}{\ell_P} \approx 10^{61}, \quad \frac{H_0^{-1}}{\tau_P} \approx 10^{61}, \quad \left(\frac{H_0}{M_P}\right)^2 \approx 10^{-122}.
$$

**The substrate hierarchy is $\sim 10^{61}$ between Planck and Hubble scales.** Route A4's $\ell_{A4}$ must reproduce this hierarchy from substrate parameters.

**From dimensional analysis alone:** the only substrate parameters that can supply the large dimensionless factor are $\Theta_{\mathrm{ED}}$ (via its specific value relative to Planck-scale event-density) or $\tau_{V_5}$ (via its value relative to Planck time). Both are primitive-content parameters per Paper_087 P12 + Paper_090.

**Substrate-parameter-INHERITED closure structure:**

$$
\ell_{A4} = \ell_P \cdot N_{\mathrm{ED}} \quad \text{where} \quad N_{\mathrm{ED}} \approx 10^{61}
$$

with $N_{\mathrm{ED}}$ a dimensionless ratio derivable from $\Theta_{\mathrm{ED}}$, $\ell_P$, $c$, $\hbar$ — a substrate-parameter-content quantity.

### §3.4 Connecting back to substrate-action density

Per §2.3, $\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}} \sim \Theta_{\mathrm{ED}}$ at saturation. Via Q1A + Q2A: $\rho_\Lambda \sim \Theta_{\mathrm{ED}}$ in appropriate units. Via Friedmann: $H_0^2 \sim \rho_\Lambda / M_P^2 \sim \Theta_{\mathrm{ED}} / M_P^2$.

In Planck units ($\Theta_{\mathrm{ED}}$ measured in Planck-event-density units): $H_0^2 / M_P^2 \sim \Theta_{\mathrm{ED}}^{\mathrm{Planck-units}}$.

**Observed:** $H_0^2 / M_P^2 \approx 10^{-122}$. Therefore: $\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}} \approx 10^{-122}$.

**Interpretation:** the ED-threshold value $\Theta_{\mathrm{ED}}$, when expressed in Planck-event-density units, is $\sim 10^{-122}$ — extremely small relative to Planck scale. **This is the substrate-parameter-content value that, via Route A4, reproduces the observed $H_0$.**

---

## §4 Dimensional-consistency analysis: ruled-in and ruled-out combinations

### §4.1 Ruled-in combinations (supply length)

- $\ell_P$ (trivially) — gives Planck length; insufficient for cosmological scale alone
- $\ell_P \cdot (\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}})^{-1/4}$ — gives cosmological length if $\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}} \approx 10^{-244}$ (too small by 122 OOM; doesn't match)
- $\ell_P \cdot (\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}})^{-1/2}$ — gives cosmological length if $\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}} \approx 10^{-122}$ (matches; consistent with §3.4)
- $\ell_{V_5} = c \tau_{V_5}$ (Route A1 direct) — substrate-parameter-INHERITED $\tau_{V_5}$
- Combinations via Hessian asymptotic + ED-SC 4.x content (Route A2; separate construction)

### §4.2 Ruled-out combinations (SC-4.x structural constraints)

Per Papers SC-4.x + Paper_ED_GW_00 §3.2 (no fundamental substrate metric):

- Combinations requiring substrate-side metric content beyond DCGT-emergent continuum metric: **ruled out** (no fundamental substrate metric available)
- Combinations requiring substrate-side absolute time beyond commitment-rate $\hbar$ content: **ruled out** (no fundamental absolute time)
- Combinations requiring substrate-side cosmological-time scale independent of $\tau_{V_5}$ + $\Theta_{\mathrm{ED}}$ + Planck content: **ruled out** — substrate primitives don't supply additional time scales

### §4.3 The constrained surviving combination

After dimensional consistency + SC-4.x exclusions, the substrate-parameter-content combination supplying $\ell_{A4}$ at cosmological scale is:

$$
\ell_{A4} \sim \ell_P \cdot (\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}})^{-1/2}
$$

or equivalently (via Friedmann + Q1A + Q2A composition):

$$
H_0^2 \sim \frac{\Theta_{\mathrm{ED}}}{M_P^2}, \quad H_0 \sim M_P \cdot (\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}})^{1/2}.
$$

**Substrate-graph derivation status:**
- Functional form $H_0 \sim M_P \cdot (\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}})^{1/2}$ is **substrate-graph-DERIVED** via Q1A + Q2A + Friedmann composition + dimensional rearrangement; closure analogous to Paper_027's $G$ form-derivation.
- Numerical value $\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}} \approx 10^{-122}$ is **substrate-parameter-INHERITED** at P12 ED-threshold level (analogous to Paper_027's $\ell_P, \hbar, c$ INHERITED at primitive level).

---

## §5 Translation to $H_0$ via DCGT

### §5.1 DCGT parametric transparency

Per Memo_ED_RouteA_Scoping_Wave3 §3, DCGT translation is parametrically transparent: all three DCGT-side conversion mechanisms (coarse-graining radius; effective metric scaling; long-time hydrodynamic limit) yield $H_0 \sim c / \ell_{A4}$.

For Route A4 with $\ell_{A4} \sim \ell_P \cdot (\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}})^{-1/2}$:

$$
H_0 \sim c / \ell_{A4} = c / [\ell_P \cdot (\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}})^{-1/2}] = (c/\ell_P) \cdot (\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}})^{1/2} = (1/\tau_P) \cdot (\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}})^{1/2}.
$$

In natural units ($M_P = 1$, $c = 1$, $\hbar = 1$): $H_0 = (\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}})^{1/2}$. Matching observation $H_0 \approx 10^{-61}$ in Planck units requires $\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}} \approx 10^{-122}$ — consistent with §3.4 + §4.3.

### §5.2 Coefficient structure

The $\sim$ relation hides a Friedmann + Q1A + Q2A coefficient $(3/8\pi)^{1/2}$ from $H_0^2 = (8\pi G/3) \rho_\Lambda$ and the Q2A coarse-graining coefficient (standard hydrodynamic-window inheritance). Explicit form:

$$
H_0 = \sqrt{\frac{8\pi G}{3} \rho_\Lambda} = \sqrt{\frac{8\pi}{3} \cdot \frac{\hbar c^5}{M_P^2 c^4} \cdot \mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}} = \sqrt{\frac{8\pi}{3} \cdot \frac{\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}}{M_P^2 \hbar^{-1} c^{-1}}} \cdot (\hbar/c)^{1/2}
$$

(using $G = \ell_P^2 c^3/\hbar = \hbar/(M_P^2 c)$). After dimensional book-keeping:

$$
H_0 = (8\pi/3)^{1/2} \cdot M_P^{-1} \cdot \mathcal{L}_{\mathrm{sub}}^{\mathrm{const}, 1/2} = (8\pi/3)^{1/2} \cdot c/\ell_P \cdot \Theta_{\mathrm{ED}}^{\mathrm{Planck-units}, 1/2}
$$

with the dimensionless coefficient $(8\pi/3)^{1/2} \approx 2.9$ — standard cosmology coefficient inheritance.

### §5.3 $\ell_{V_5}$ identification

Per Memo_ED_RouteA_Scoping_Wave3 §3, the canonical Route A formulation expects $\ell_{V_5} \sim c/H_0$. Combining with §5.1:

$$
\ell_{V_5} \sim c/H_0 \sim \ell_P \cdot (\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}})^{-1/2}.
$$

**Route A4 supplies the substrate-graph derivation of $\ell_{V_5}$ via the substrate-action density asymptotic + Paper_027 dimensional-rearrangement template** — $\ell_{V_5}$ is not an independent substrate-parameter; it is derived from $\Theta_{\mathrm{ED}}$ via this composition. Route A1's canonical formulation reduces to Route A4's substrate-action density derivation.

---

## §6 IDENTIFIED vs OPEN

### §6.1 IDENTIFIED (substantive A4 closures)

- **Functional form $H_0 = (8\pi/3)^{1/2} \cdot c/\ell_P \cdot \Theta_{\mathrm{ED}}^{\mathrm{Planck-units}, 1/2}$** — substrate-graph derivation via Q1A + Q2A + Friedmann + Paper_027 dimensional rearrangement. Closes at substrate-graph form-DERIVED level (§5.2).
- **$\ell_{V_5}$ derivation from $\Theta_{\mathrm{ED}}$** — Route A1's canonical $\ell_{V_5}$ scale reduces to Route A4's substrate-action density derivation (§5.3). Route A1 not an independent route from A4; both reduce to substrate-parameter-content for $\Theta_{\mathrm{ED}}$.
- **Substrate-parameter-INHERITED closure structure** — analogous to Paper_027's M3 closure pattern; substrate-graph derivation of $H_0$'s functional form modulo substrate-parameter ($\Theta_{\mathrm{ED}}$) value INHERITED at primitive level.
- **Λ-smallness 120-OOM hierarchy** — captured via $(\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}})^{1/2} \approx 10^{-61}$. The "smallness" of $\Lambda$ is the smallness of the ED-threshold value in Planck units; substrate-graph framing replaces the QFT mode-summation question with the ED-threshold-value question. **This is the substantive substrate-research finding of Route A4.**
- **SC-4.x consistency** — surviving combination is consistent with SC-4.x structural constraints (no fundamental substrate metric; no absolute time; no independent cosmological scale).

### §6.2 OPEN (load-bearing for full Route A closure beyond A4)

| OPEN | Description | Status |
|---|---|---|
| **RA-OPEN-4a (newly introduced)** | Substrate-graph derivation of the **numerical value** of $\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}} \approx 10^{-122}$ from sub-primitive content | Substrate-research-frontier; **outside standard Paper_027-template scope** (Paper_027 takes $\ell_P, \hbar, c$ as substrate-parameter-INHERITED primitive constants; same template treats $\Theta_{\mathrm{ED}}$ as INHERITED) |
| **RA-OPEN-4b (subleading)** | Substrate-graph derivation of the proportionality coefficient relating $\mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$ to $\Theta_{\mathrm{ED}}$ beyond leading-order $\mathcal{L} \sim \Theta_{\mathrm{ED}}$ assumption | Substantive; SC-4.9 functional structure analysis required |
| **RA-OPEN-4c (cross-route convergence)** | Substrate-graph verification that Route A2 (Hessian asymptotics) + Route A3 ($\Psi$ relaxation timescale) yield the same $H_0$ prediction as A4 | Cross-route convergence audit; if convergent, tightens closure |

### §6.3 OPEN (not load-bearing for A4 closure)

- Substrate-graph derivation of cyclic-CCC framework coherence (CCC audit row 17) — independent
- Substrate-graph derivation of matter-Λ crossover redshift $z_\Lambda \approx 0.7$ — Route C1 + Route A composition; outside A4 scope
- Substrate-graph derivation of subleading-order corrections to $H_0$ — Q2A subleading scheme-dependence; not load-bearing for leading-order

### §6.4 Comparison with prior substrate-graph closure status

| Closure | Status | Closure level |
|---|---|---|
| Paper_027 (Newton's $G$) | M3 | form-DERIVED via dimensional rearrangement + value-INHERITED at substrate-parameter level ($\ell_P, \hbar, c$ INHERITED) |
| **Route A4 (this construction; $H_0$)** | **M3-equivalent at functional-form level; value-INHERITED at substrate-parameter level ($\Theta_{\mathrm{ED}}$ INHERITED)** | **Same closure level as Paper_027 — functional form derived via dimensional rearrangement + value-INHERITED at substrate-parameter level** |

**Critical interpretation:** Route A4 closes **at the same closure level as Paper_027's M3 status** — form-DERIVED via dimensional rearrangement; substrate-parameter ($\Theta_{\mathrm{ED}}$) INHERITED. Whether this counts as "value-DERIVED $H_0$" or "still value-INHERITED at substrate-parameter level" depends on the corpus reading:

- **Practical corpus reading (per Paper_027's M3 status):** functional-form derivation from substrate parameters via dimensional rearrangement counts as substrate-graph closure. Route A4 closes at this level.
- **Strict reading:** value-DERIVED requires primitive-only derivation. Under this reading, Route A4 supplies a partial closure; further substrate-research-frontier work to derive $\Theta_{\mathrm{ED}}$ from sub-primitive content (RA-OPEN-4a) would be required.

The practical corpus reading is consistent with Paper_027's existing M3 status; under it, **Route A4 closes Route A at substrate-graph level, with the residual $\Theta_{\mathrm{ED}}$-value question parallel to Paper_027's residual $\ell_P, \hbar, c$-value questions** (all at primitive level).

---

## §7 Status update + recommended next steps

### §7.1 Route A4 closure status

| Aspect | Status |
|---|---|
| Functional form $H_0 = (8\pi/3)^{1/2} \cdot M_P \cdot \Theta_{\mathrm{ED}}^{\mathrm{Planck-units}, 1/2}$ | **substrate-graph-DERIVED** via Q1A + Q2A + Friedmann + Paper_027 dimensional-rearrangement template |
| Numerical value $\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}} \approx 10^{-122}$ | **substrate-parameter-INHERITED** at primitive level (P12 ED-threshold); RA-OPEN-4a flagged |
| $\ell_{V_5}$ identification | Reduces to A4: $\ell_{V_5} \sim \ell_P \cdot \Theta_{\mathrm{ED}}^{\mathrm{Planck-units}, -1/2}$ |
| Λ-smallness 120-OOM | Reframed: smallness of $\Lambda$ = smallness of $\Theta_{\mathrm{ED}}$ in Planck units; substrate-research question replaces QFT-mode-summation question |
| Comparison to Paper_027 closure level | **Same M3-equivalent status** (form-DERIVED + substrate-parameter-INHERITED) |

### §7.2 Cross-arc consequence (if A4 audit accepts)

| Paper | Pre-A4 | Post-A4 (audit-accepted) |
|---|---|---|
| Paper_ED_Cos_01 (Inflation) | M3 + value-INHERITED | **M3 + form-DERIVED $H$ via Route A4** (substrate-parameter-INHERITED at $\Theta_{\mathrm{ED}}$ level) |
| Paper_ED_Cos_05 (Dark Energy) | M3 conditional on Route A | **M3 unconditional** (Route A4 closure delivers the conditional) |
| Paper_038_5 (Lambda_V1) | M2 conditional retroactive M3 | **M3 retroactive upgrade** per Paper_038_5 reframing |
| ED-SC 4.x arc-wide | M3 (six projections) | **M3 → M2 upgrade** (Route A4 closure triggers ED-SC 4.x arc-wide upgrade per ED_MEMORY anchor 7) |
| Paper_027 (Newton's $G$) | M3 form-DERIVED + value-INHERITED at $\ell_P, \hbar, c$ | unchanged — Route A4 inherits Paper_027's closure pattern; both papers stand at same M3 closure status |

**Λ-smallness 120-OOM problem reframed:** the substantive substrate-research question becomes "what determines $\Theta_{\mathrm{ED}}$ value?" — parallel to the longstanding question "what determines $\ell_P, \hbar, c$ values?" The 120-OOM hierarchy is **substrate-parameter-INHERITED at ED-threshold level**, not a separate "fine-tuning problem" requiring specialized substrate-graph mechanism.

### §7.3 Recommended next steps

**Path-A4-Audit:** adversarial audit of this memo's construction following the discipline cascade. Verify:
- Q1A + Q2A composition delivers $\rho_\Lambda \sim \mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$ at standard-coefficient level
- $\Psi^{\mathrm{const}}_{\mathrm{saturation}} = \Theta_{\mathrm{ED}}$ identification holds under Paper_ED_CCC §3.7 (under cyclic framing) and R3 framing (under non-cyclic framing)
- SC-4.x structural-constraint analysis cleanly rules out alternative combinations
- Paper_027 template legitimately extends to Route A4 (analog-inheritance verification)
- $U(\Psi) \sim \Psi$ leading-order linearity assumption (RA-OPEN-4b)

**Path-A2-Construction (parallel; tightening via cross-route convergence):** focused construction memo attempting Route A2 (Hessian asymptotics + ED-SC 4.x six-projection framework) per scoping memo §7.2 recommended-parallel path. If A2 closes convergently with A4, multi-route convergence tightens the closure (RA-OPEN-4c).

**Path-Cos05-Update (conditional on A4 audit + Cos_05 verification):** update Paper_ED_Cos_05 to reflect M3-unconditional status; remove "conditional on Route A" qualifier from status line + abstract + §1 + audit row + §6.

**Path-Cos01-Note (conditional on A4 audit):** update Paper_ED_Cos_01 to note A4 closure provides substrate-graph form-derivation of $H$ within M3 framing.

**Path-038_5-Update (conditional on A4 audit):** update Paper_038_5 to reflect retroactive M2 → M3 upgrade per the reframing's conditional clause.

**Path-ED-SC-4.x-Arc-Update (conditional on A4 audit):** propagate ED-SC 4.x arc-wide M3 → M2 upgrade across the six projections.

### §7.4 My recommendation

**Path-A4-Audit immediately.** The construction's substantive content (functional-form derivation + Paper_027 template inheritance) is sufficiently structured for adversarial audit; the key audit questions are (a) Paper_027 template legitimacy, (b) $\Psi^{\mathrm{const}} = \Theta_{\mathrm{ED}}$ identification, (c) leading-order linearity assumption. If A4 audit accepts, propagation to corpus paper structure is straightforward.

**Path-A2-Construction in parallel** for cross-route convergence verification per RA-OPEN-4c.

---

**End Memo_ED_RouteA_A4_Construct.**
