# Paper 049 — Cosmological PBH Relic-Matter Abundance (H-9)

**Series:** Wave-2 Generative Papers (Black-Hole Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_041 (Planck-mass remnant), Paper_048 (higher-order resummation), Paper_038 (cosmological implications).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim that Planck-mass remnants are a dark-matter candidate (consistent with Paper_041 §4 framing). Remnants are a structural relic-matter component, distinct from DM.
2. It does **not** claim a complete derivation of the relic-abundance numerical value; it supplies the **structural form** of the abundance as a function of PBH formation scenarios.
3. It does **not** claim novel observational predictions overriding standard PBH cosmology; structural form FORCED, numerical content INHERITED.
4. It does **not** introduce new substrate primitives.
5. "Relic-matter abundance" = fractional contribution of Planck-mass remnants to the cosmic energy budget at the current epoch, computed under specified PBH formation scenarios.

---

## Abstract

Cosmological Planck-mass remnant relic abundance follows structurally from Paper_041 (remnant $M_\star = c_\star \ell_P$) + Paper_048 (Scenario C forced) + standard PBH-formation cosmology. The substrate audit composes: (i) PBH formation rate $n_{\mathrm{PBH}}(t_{\mathrm{form}}, M_{\mathrm{form}})$ at formation epoch (INHERITED from standard PBH cosmology); (ii) Hawking-evaporation evolution under substrate-corrected rate (Paper_048) producing a remnant per initial PBH; (iii) cosmological dilution of remnants between formation and current epoch. The resulting abundance $\Omega_\star \propto n_{\mathrm{PBH}} \cdot M_\star$ depends linearly on the PBH formation density, with substrate-specific content concentrated in the remnant identification. **Remnants do not contribute to DM** (per Paper_041); they are a separate structural relic-matter component.

---

## §1 Introduction

If Hawking evaporation terminates at $M_\star$ (Paper_041), every primordial black hole (PBH) of initial mass $M_{\mathrm{PBH}} > M_\star$ produces exactly one Planck-mass remnant after evaporation completes. The relic abundance is the cumulative remnant population diluted to the current cosmological epoch.

This paper supplies the substrate audit of the relic abundance, with explicit framing that **remnants are not DM**.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P08 (Substrate scale $\ell_{\mathrm{ED}}$)** — Planck length.
- **P11 (Commitment-irreversibility)** — directional evaporation.
- **P13 (Time homogeneity)** — substrate-cosmological evolution.

### 2.2 Upstream dependencies

- **I-038:** Substrate-gravity cosmological implications (Paper_038).
- **I-041:** Planck-mass remnant $M_\star$ (Paper_041).
- **I-048:** Higher-order resummation selecting Scenario C (Paper_048).
- **I-PBH:** Standard PBH cosmology / formation scenarios (standard astrophysics).
- **I-FRW:** Standard FRW cosmological dilution machinery (standard math).

### 2.3 Paper-specific postulates

- **P-One-Remnant-Per-PBH:** Each PBH of initial mass $M_{\mathrm{PBH}} > M_\star$ produces exactly one Planck-mass remnant upon Hawking-evaporation completion.
- **P-Remnant-Stable-Cosmological:** Remnants are stable on cosmological timescales (no late-time decay through unaccounted-for channels). (Inherited from Paper_041 P-Remnant-Stability.)

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | PBH formation rate at formation epoch | I | Standard PBH cosmology (I-PBH). |
| 2 | Scenario C remnant endpoint | I | Paper_048. |
| 3 | One remnant per PBH | P-One-Remnant-Per-PBH | Postulate. |
| 4 | Remnant mass $M_\star = c_\star \ell_P$ | I | Paper_041. |
| 5 | Remnant stable cosmologically | I (from Paper_041) + P-Remnant-Stable-Cosmological | Postulate inherited from Paper_041. |
| 6 | FRW dilution from formation to current epoch | I | Standard cosmology (I-FRW). |
| 7 | Relic abundance $\Omega_\star \propto n_{\mathrm{PBH}}(t_{\mathrm{form}}) \cdot M_\star / \rho_{\mathrm{crit}}$ | D-via-I | Composition of steps 1, 3, 4, 6. |
| 8 | Numerical $n_{\mathrm{PBH}}(t_{\mathrm{form}})$ for specific PBH-formation scenarios | I | Standard astrophysics. |
| 9 | Specific $\Omega_\star$ values | I | Empirical / standard cosmology matching. |
| 10 | **Remnants are NOT DM** | A→position | Per Paper_041 framing. |

---

## §3 The Relic Abundance

### 3.1 Per-PBH remnant production

By P-One-Remnant-Per-PBH and I-048, each PBH of initial mass $M_{\mathrm{PBH}} > M_\star$ produces exactly one stable remnant of mass $M_\star$ when its evaporation reaches the Scenario-C endpoint.

Time-to-evaporate is $t_{\mathrm{evap}} \sim M_{\mathrm{PBH}}^3/(c \ell_P^2)$ (standard Hawking lifetime). For PBH formed at $t_{\mathrm{form}}$ with mass $M_{\mathrm{PBH}}$ such that $t_{\mathrm{form}} + t_{\mathrm{evap}} < t_0$ (current epoch), the PBH has completed evaporation and the remnant survives at the current epoch.

### 3.2 Cosmological dilution

Standard FRW dilution (I-FRW) reduces the remnant number density between $t_{\mathrm{form}}$ and $t_0$ by $a^{-3}$ where $a$ is the scale factor.

### 3.3 Composing

The current-epoch relic abundance is:
$$\Omega_\star = \frac{n_{\mathrm{remnant}}(t_0) \cdot M_\star}{\rho_{\mathrm{crit}}} = \frac{n_{\mathrm{PBH}}(t_{\mathrm{form}}) \cdot a(t_{\mathrm{form}})^3/a(t_0)^3 \cdot M_\star}{\rho_{\mathrm{crit}}} .$$

This is the structural form of the relic abundance. The factor $n_{\mathrm{PBH}}(t_{\mathrm{form}})$ depends on the PBH-formation scenario (matter-domination, radiation-domination, inflationary perturbations, etc.) and is **INHERITED** from standard PBH cosmology.

### 3.4 Why remnants are not DM

By the ED program's substrate-gravity walkthrough (Papers_027–034), galactic dynamics are explained **without DM**. Remnants are a **separate structural relic-matter component** of the cosmic energy budget. The PBH-remnant abundance contributes to the cosmic energy density but does **not** play the dynamical role of galactic-rotation-curve DM.

This is **A→position** (load-bearing framing claim).

---

## §4 What This Paper Supplies and Does Not Supply

**Supplies:** Structural form of the relic abundance. Substrate identification of $M_\star$ as the remnant mass per PBH. Framing-statement separation of remnant relic-matter from DM.

**Does not supply:** Specific PBH-formation scenario predictions. Numerical $\Omega_\star$ value (requires astrophysical $n_{\mathrm{PBH}}(t_{\mathrm{form}})$). DM substitution mechanism (remnants are not DM).

---

## §5 Falsification Criteria

- **F1:** Empirical detection of remnants playing the dynamical role of galactic-rotation DM — would refute the substrate-gravity walkthrough and the framing.
- **F2:** Detection of remnant-mass relics at scales $\ne M_\star$ — refutes Paper_041 inheritance.
- **F3:** Empirical evidence that PBH evaporation produces multiple remnants (or fragments) per initial PBH — refutes P-One-Remnant-Per-PBH.
- **F4:** Detection of late-time remnant decay — refutes P-Remnant-Stable-Cosmological.

---

## §6 Position Statement

Cosmological PBH relic-matter abundance is **structurally FORCED** as $\Omega_\star \propto n_{\mathrm{PBH}}(t_{\mathrm{form}}) \cdot M_\star$ under P-One-Remnant-Per-PBH + Paper_041 remnant identification + standard FRW dilution. Numerical content INHERITED via PBH-cosmology.

**Remnants are not a DM candidate** — galactic dynamics explained by substrate gravity (Papers_027–034); remnants are a separate cosmic-energy-budget component.

---

**End Paper 049 (FIXED).**
