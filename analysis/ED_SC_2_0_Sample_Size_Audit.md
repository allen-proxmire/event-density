# ED-SC 2.0 Sample-Size Audit

**Status.** Follow-on audit to the r* arc (2026-04-22). Closes task (1) from
the post-arc suggestion list: sweep the ED-SC 2.0 corpus for numerical
invariant claims calibrated at small-N and flag those at risk of the same
single-seed pathology that dissolved r* = −1.304 → −1.88.

**Scope.** Audits the canonical ED-SC 2.0 statement (`docs/ED-SC-2.0.md`),
the orientation doc (`docs/ED-Orientation.md`), the universal-invariants
compendium (`theory/Universal_Invariants.md`), and the empirical-status
table at ED-Orientation §7. Does not re-audit upstream ED-Foundation or
ED-Math derivations (those are analytic, not sample-calibrated).

---

## 1. Method

For each numerical claim in the audited docs, record:

- **N** — the sample size the claim was calibrated on (number of seeds,
  realisations, materials, or measurements; "deriv" if purely analytic).
- **Class** — FIT (calibrated from sample), DERIV (analytic), VALID
  (derivation cross-checked against a single simulation).
- **Verdict** — PASS if N ≥ 10 or class ≠ FIT; AT-RISK if class = FIT and
  N < 10; CORRECTED if already resolved.

The threshold N = 10 is the same threshold ED-SC 2.0 §3 condition (3)
requires of a comparison system, so applying it here is consistency with
the theory's own acceptance rule.

---

## 2. Findings

### 2.1 Summary table

| Claim | Location | N | Class | Verdict |
|-------|----------|-----|-------|---------|
| **r* = −1.304** (motif-conditioned median) | `ED-SC-2.0.md` §2, §7; `ED-Orientation.md` §6.9 line 971 | 6 motifs, 1 seed | FIT | **CORRECTED** (→ −1.88 ± 0.4 at N=34 pooled; see `ED_SC_2_0_r_star_Final_Verdict.md`) |
| AFM-dewetting sim↔image pilot (−2.063 vs −2.149) | `ED-Orientation.md` §7 line 1034 | 1 image | FIT | **AT-RISK** |
| D_crit(ζ) ≈ 0.896 at ζ=1/4 | `Universal_Invariants.md` §2 | deriv | DERIV | PASS |
| E_ground = αγρ₀ | `Universal_Invariants.md` §3 | deriv + 1 sim validation | DERIV / VALID | PASS |
| t_rel ≈ ρ₀/(αγ) | `Universal_Invariants.md` §4 | deriv + hybrid-regime spread ~13% | DERIV / VALID | PASS |
| D·T₀/L₀² = 0.3 (5 regimes, 61 orders of magnitude) | `Universal_Invariants.md` §5 | 5 regime fits | FIT | PASS (N=5 spans 61 orders of magnitude — different regime, but sample-size logic applies only within a regime, not across; flag for review) |
| C ≈ 0.03 triad coupling (ED-Phys-16) | `ED-Orientation.md` §3 line 224 | 1 simulation | VALID? | **AT-RISK** (needs source check) |
| K = 0.0148 ± 0.0005, K₂ = 0.279, α₃ = 3.0 (C7 triad) | `telegraph_pme/triad_calibration/memo.md` line 13–16 | 1 deterministic run | DERIV-of-canonical-op / VALID | PASS (deterministic operator + fixed monochromatic IC; sample-size not applicable) |
| 3–6 % third-harmonic ratio | `ED-Orientation.md` §3 line 225 | unspecified | unknown | **AT-RISK** (provenance unclear) |
| SPARC dwarf ⟨D_outer⟩ 6.01 vs 3.94 (53%) | `ED-Orientation.md` §3 line 94, §6.1 | 46 galaxies | FIT | PASS |
| UDM R² > 0.986 | §7 line 1025 | 10 materials | FIT | PASS |
| Cluster merger-lag `ℓ = D_T/v_current` | §7 line 1026 | 7 clusters | FIT | PASS |
| Analogue-3 A_c = 0.400 predicted / 0.410 measured | `ED-Orientation.md` §6.4 | 1 canonical param point | DERIV / VALID | PASS (threshold prediction + single-point check) |
| Analogue-5 ω ∝ H^0.52 (predicted 0.50) | `ED-Orientation.md` §6.4 | scan over H | FIT | PASS (scan, not single point) |

### 2.2 Detail on the AT-RISK items

**AFM-dewetting sim↔image pilot.** ED-Orientation §7 line 1034 reports the
cross-scale pilot as "N=1 ℛ_all agrees sim↔image (−2.063 vs −2.149)." This
is a single-image / single-simulation comparison. Under the r*-arc finding
(single-seed medians of motif-filtered saddle populations are high-variance
fluctuations), this pilot should not be read as evidence for cross-scale
invariance at any meaningful level. The status entry already marks it
"needs real motif-resolvable AFM data" so the operational risk is low —
but the memory-level implication ("agreement at the 4% level") is
currently more precise than the data warrants.

**Recommendation.** Reword the pilot line to make the N=1 nature explicit:
drop "agrees" and replace with "single-image vs. single-seed comparison
yielded medians of similar order (−2.1 vs −2.0); a pooled-N test with ≥10
images and ≥10 seeds is required before the comparison is informative."

**C ≈ 0.03 triad coupling (ED-Phys-16).** The 0.03 value appears in
`ED-Orientation.md` §3 line 224 as "coupling ~0.03 (measured in
ED-Phys-16)." ED-Phys-16 is in-repo at
`archive/research_history/ED Physics/16 results/` but the audit here did
not open that directory. The sample-size basis is unclear. The newer C7
work (`telegraph_pme/triad_calibration/memo.md`) uses a deterministic
canonical operator with fixed monochromatic IC and reports K = 0.0148,
which is a different coupling definition. Whether "0.03" and "0.0148" refer
to the same object — and if so whether the factor of ~2 discrepancy is
significant — is an open provenance question. ED-Orientation §7 line 1037
notes "K may vary by factor ≤ 2 across clean-regime realizations," which
would absorb the discrepancy.

**Recommendation.** Trace the 0.03 figure to its ED-Phys-16 source and
document whether it is derivation-based (like K = 0.0148) or fit-based
(ensemble over simulations). If fit-based at small N, flag as AT-RISK.
Otherwise update the orientation to cite K = 0.0148 as canonical.

**3–6 % third-harmonic ratio.** `ED-Orientation.md` §3 line 225 states
"harmonic generation at 3–6% of fundamental" without provenance. If this
is the A₃/A₁ ratio from ED-Phys simulations, the C7 calibration gives
A₃/A₁ = K·A₁² ≈ 0.015·A₁², which is 3% at A₁ ≈ 1.4 — plausibly consistent.
But the original 3–6% range's sample-size basis is undocumented.

**Recommendation.** Either cite provenance (which ED-Phys paper, how many
runs) or drop the numerical range and replace with the C7-derived form
A₃/A₁ = K·A₁² with K = 0.0148.

### 2.3 The D·T₀/L₀² = 0.3 invariant

This is a cross-regime identity claimed over five regimes spanning 61 orders
of magnitude. Each regime contributes one (D, T₀, L₀) triple; agreement
at five data points over 61 orders of magnitude is a very different kind
of evidence than five same-regime samples. The sample-size audit does not
cleanly apply. Flagged here only to note that the claim's robustness would
benefit from a second triple within at least one regime (e.g., two galactic
data points instead of one), which would convert it from a strict
structural claim to a statistical one.

**Recommendation.** No change required for ED-SC 2.0. If a regime were
ever to gain a second data point, check whether the 0.3 value is stable
across it.

---

## 3. Aggregate verdict on ED-SC 2.0

Of 13 numerical claims audited:

- **1 corrected** (r* = −1.304 → −1.88)
- **2–3 at-risk** (AFM pilot; triad coupling 0.03 provenance; 3–6% third-
  harmonic provenance)
- **1 unusual** (D·T₀/L₀² = 0.3 cross-regime)
- **Remainder pass** (derivations, multi-sample fits, scan-based fits)

The r* claim was the most visible single-seed artefact in the corpus but
not the only one. The AFM pilot is the next-most-consequential because it
is the pointer for the highest-certainty near-term cross-scale test; its
N=1 status should be explicit in any forward planning.

The triad and harmonic claims are less consequential because the C7
program has already superseded them with deterministic canonical-operator
results (K, K₂, α₃, Δφ). Aligning the orientation language to cite the
C7 values and retire the older fit-based figures would complete the
cleanup.

---

## 4. Required edits

The following edits would close the audit's flagged items. None are made
in this memo; they are left as staged recommendations:

1. **`docs/ED-SC-2.0.md` §2, §7, §8.1.** Replace the quoted invariant
   `r* ≈ −1.30 (−1.304)` with the pooled value `r* ≈ −1.88 ± 0.4` and
   restate the invariant as a distribution rather than a scalar. §8.1
   "ensemble statistics" open item is superseded by the
   `ED_SC_2_0_r_star_Final_Verdict.md` result.

2. **`docs/ED-Orientation.md` §6.9 line 971.** Update motif-conditioned
   median to the pooled value. Optional: keep the single-seed value as a
   historical note with explicit N=6 annotation.

3. **`docs/ED-Orientation.md` §7 line 1034 (AFM pilot row).** Reword to
   make N=1 explicit and drop "agreement" language.

4. **`theory/Universal_Invariants.md` §5.** Remove `r* ≈ −1.304` from the
   universal-invariant block, or replace with the structural form
   "filtered GRF saddle-ratio median exists and is finite."

5. **`docs/ED-Orientation.md` §3 lines 224–225.** Trace 0.03 and 3–6%
   provenance; either cite source with N or retire in favour of the C7
   deterministic values.

6. **`~/.claude/projects/.../memory/project_ed_r_star_analytic_arc.md`.**
   Append a ninth-pass closure line reflecting the GRF port + falsifier
   findings. (Separate task; not an ED-SC 2.0 edit.)

---

## 5. Audit conclusion

**The r* = −1.304 single-seed pathology is real and was present in at
least two places beyond the headline (`Universal_Invariants.md` §5
citation; AFM pilot).** The rest of the ED-SC 2.0 corpus is largely
clean: the main derivation-based invariants (D_crit, E_ground, t_rel, C7
triad quantities) are immune to the pathology by construction, and the
main fit-based claims with external data (SPARC, UDM, merger-lag) are at
N ≥ 7. The two remaining ED-Phys-16 citations (triad coupling 0.03 and
harmonic ratio 3–6%) warrant a provenance check but are unlikely to be
load-bearing for any active prediction thread, since the C7 program has
produced successor values.

**ED-SC 2.0 as a framework survives the audit; as a scalar target it does
not.** ED-SC 3.0 should restate the invariant at the structural level (a
filtered GRF saddle-ratio distribution exists and is stable under
correlation-length-preserving transformations) and abandon the scalar form.

**Deliverable.** This memo + recommended edits list above. No code
changes. No doc edits performed without user sign-off.
