# ED-SIM-3D — D_crit Propagation Report (v1.0)

**Date.** 2026-04-22.
**Scope.** Propagate the corrected `D_crit` value (from [`theory/D_crit_Resolution_Memo.md`](../../theory/D_crit_Resolution_Memo.md)) through the `edsim` codebase, the atlas/diagram scripts, and the load-bearing theory and protocol documents. Write the propagation record.

---

## 1. Introduction

The Canon P6 single-number threshold `D_crit = 0.5` was retired 2026-04-22 in favour of the exact linearised expression

$$
D_{\rm crit}(\zeta) \;=\; \sqrt{2-\zeta}\bigl(2 - \sqrt{2-\zeta}\bigr)
$$

derived from the 2×2 coupled-eigenvalue discriminant of the canonical PDE around homogeneous equilibrium. At canon-default `ζ = 1/4`, `D_crit ≈ 0.8958`. The old 0.5 value came from the additive heuristic `Δ = D + 2ζ = 1` which drops the coupled cross-term and is off by ~80%.

This memo records how the correction was propagated into (a) the `edsim` simulation package, (b) four atlas/diagram generation scripts, (c) three load-bearing theory documents, and (d) one active experimental protocol. It also identifies the one place where a qualitative conclusion appears to shift (the rate-balance template's identification of named physical thresholds with the bifurcation), and flags it for a dedicated v0.5+ revision.

## 2. Old vs new `D_crit` usage

### 2A. Two distinct forms

| Form | Expression | Canon-default value | Status |
|:---|:---|:---|:---|
| Retired heuristic | `D_crit = 1 − 2ζ` (from `Δ = D + 2ζ = 1`) | 0.5 at `ζ = 1/4` | **retired**; retained as `d_crit_heuristic` helper for legacy reference only |
| Canonical | `D_crit(ζ) = √(2 − ζ)·(2 − √(2 − ζ))` | **≈ 0.8958** at `ζ = 1/4` | **canonical**; `d_crit(zeta)` in `edsim.math.damping` |

### 2B. Places the old value appeared

- **Simulation code** — `edsim/` has **no hard-coded `D_crit = 0.5`**. Regime classification in `edsim/phys/analysis_wave.py` (`"underdamped": regime.omega_osc > 0`) is driven by the actually-computed eigenvalue, so the solver is correct by construction.
- **Atlas/diagram scripts** — four scripts embedded `0.5` as a visual reference or in docstrings:
  - `analysis/scripts/generate_ed_dimensional_ext_d_vs_scale.py`
  - `analysis/scripts/generate_ed_logic_diagram.py`
  - `analysis/scripts/generate_ed_math_pipeline.py`
  - `analysis/scripts/atlas/P6_visual_only.py`
- **Theory documents** — `theory/Universal_Invariants.md` §2 (dedicated section on the threshold), `theory/Architectural_Canon.md` (P6 row + §3 summary), and `theory/ED-Dimensional-01-Ext.md` (v0.4-final, many inline references).
- **Experimental protocols** — `experiements/ED-09-5-Envelope_InProcess/protocol.md` (§0 opening + §1 + §2 pre-registered table).

## 3. Code changes

### 3A. New helper — `edsim/math/damping.py`

```python
def d_crit(zeta: float) -> float:
    """Canonical P6 threshold; D_crit(ζ) = √(2−ζ)·(2 − √(2−ζ))."""
    u = np.sqrt(2.0 - zeta)
    return float(u * (2.0 - u))

def underdamped(D: float, zeta: float) -> bool:
    """Exact coupled-eigenvalue underdamping condition."""
    return (D - zeta) ** 2 < 4.0 * (1.0 - D)

D_CRIT_CANONICAL: float = d_crit(0.25)   # ≈ 0.8958
```

Also exports `d_crit_heuristic(zeta)` for legacy reference and `ZETA_CANONICAL = 0.25`. Exposed via `edsim.math.__init__.py`. Verified by import test: `d_crit(0)=0.828, d_crit(0.25)=0.896, d_crit(0.5)=0.949`.

### 3B. Atlas / diagram script edits (diff summary)

- `generate_ed_dimensional_ext_d_vs_scale.py` — imports `D_CRIT_CANONICAL` from `edsim.math.damping`; replaces the hard-coded `0.5` on the cosmic-web bifurcation anchor and on `axhline`/`axhspan`/legend-label calls; updates docstring.
- `generate_ed_logic_diagram.py` — docstring corrected; Fork 2 panel relabelled from `Δ = D + 2ζ = 1 → D_crit = 0.5` to `(D − ζ)² = 4(1 − D) → D_crit ≈ 0.896 (ζ = 1/4)`; oscillatory/hybrid/parabolic boundary text updated to `D_crit`-relative form.
- `generate_ed_math_pipeline.py` — docstring corrected; P6 row in the pipeline diagram relabelled; bottom-row "sharp bifurcation" label relabelled.
- `atlas/P6_visual_only.py` — docstring corrected; threshold comment relabelled. Image geometry (`Dc_x = 6.5`) unchanged because the diagram's x-coordinate is a visual center, not a quantitative D-axis; the correction is a label/caption issue here.

### 3C. Verification

All five Python files parse cleanly. `from edsim.math import d_crit, D_CRIT_CANONICAL, underdamped` succeeds and returns expected values. No change to the PDE solver, no change to the eigenvalue computations, no change to any data.

## 4. Documentation changes

### 4A. `theory/Universal_Invariants.md` §2 — full rewrite

The dedicated "Oscillation-death threshold" section is rewritten:

- Section header changes from `D_crit = 0.5` to `D_crit(ζ) ≈ 0.896 at canon-default ζ = 1/4`
- Opening update-banner flags the retirement of the heuristic
- Statement, derivation, and three-regimes table all updated to the corrected form
- "Why it matters" paragraph preserves the Q-C-transition claim (which depends on existence of the sharp bifurcation, not its numerical location)
- Summary table in §5 updated

### 4B. `theory/Architectural_Canon.md` — P6 row rewrite

The P6 principle statement is rewritten from

> Δ = D + 2ζ, underdamped when Δ<1, overdamped when Δ>1, sharp at D_crit = 0.5

to

> `(D − ζ)² < 4(1 − D)` underdamped; sharp at `D_crit(ζ) = √(2−ζ)·(2 − √(2−ζ)) ≈ 0.896` at canon-default `ζ = 1/4`

with a link to the resolution memo. The §3 invariants-summary bullet updated correspondingly.

### 4C. `theory/ED-Dimensional-01-Ext.md` — caveat banner added

A prominent banner is inserted ahead of §1 explaining that the paper uses `D_crit = 0.5` throughout via the retired heuristic. **This is the one place where a qualitative conclusion potentially shifts** — see §5 of this memo.

### 4D. `experiements/ED-09-5-Envelope_InProcess/protocol.md` — three targeted edits

- Top-of-file update banner
- §1 "prediction in one paragraph" updated
- §2 "Pre-registered test parameters" table row updated

The protocol's envelope prediction `ω_v = 2π·N_osc·γ_dec` is **unaffected** — it derives from the good-cavity limit `γ_dec ≪ ω_sys`, not from the numerical value of `D_crit`.

## 5. Impact on axiom-P7 validation and qualitative conclusions

### 5A. ED-SIM-3D axiom-P7 results are unchanged

The ED-SIM-3D paper (Orientation §6.7) validates axiom **P7** (dimensional consistency across `d = 1, 2, 3`), not P6. The value of `D_crit` enters the paper only as a regime marker in descriptive language. The paper's quantitative conclusions (5 invariant tests: Barenblatt PME, RC decay, telegraph oscillation, horizon formation, participation coupling; all dimension-independent for penalty + participation, dimension-dependent for mobility per `α_R = 1/(d(m−1)+2)`) are derived from the actually-computed eigenvalues in `edsim`, which are correct by construction. No re-run needed; only the regime-boundary labels shift from "crosses 0.5" to "crosses ≈ 0.896."

### 5B. Orientation §4 three-regimes table

Already updated 2026-04-22 (third pass) — see the existing entry. Heuristic boundaries preserved for traceability; corrected boundary column added; note flags downstream doc re-examination.

### 5C. The one non-trivial shift — ED-Dimensional-01-Ext's physical-threshold identifications

The rate-balance template of v0.4-final uses `D = γ_dec / (γ_dec + ω_sys)`. Under this mapping:

- `D = 0.5` ⟺ `γ_dec = ω_sys` (equal-rates boundary)
- `D_crit ≈ 0.896` ⟺ `γ_dec ≈ 8.6 · ω_sys` (dissipation-dominated boundary)

The paper's substantive cross-regime claims — that the bifurcation lands at sideband resolution (cavity optomechanics), strong coupling (cavity QED), superconducting `T_c`, BEC collective-mode damping, dwarf-galaxy activity boundary, and ΛCDM nonlinear scale `k_NL` — were each made on the premise `D_crit = 0.5`, i.e. "the bifurcation is at equal rates." **Under the correction these named thresholds sit at `D = 1/2` but `D_crit` no longer does.** The identifications therefore need re-examination:

- **Option (a)** — the true bifurcation at `D ≈ 0.896` is itself the physically-meaningful line, and the named thresholds at `D = 1/2` are near-critical but not critical. Under this reading, the paper's cross-regime atlas stands but the "identifies the bifurcation with X" language becomes "identifies the rate-equality line with X."
- **Option (b)** — the rate-balance mapping `D = γ_dec/(γ_dec + ω_sys)` is itself approximate, and under a corrected mapping the equal-rates line and `D_crit` coincide again. This would require deriving the template from first principles rather than taking the rate-ratio form as given.

Neither option can be settled in this propagation pass. The caveat banner in `ED-Dimensional-01-Ext.md` records the open question; a dedicated v0.5+ revision is flagged.

### 5D. ED-09.5 envelope protocol is unchanged in substance

The envelope observable `ω_v = 2π·N_osc·γ_dec` is derived from the good-cavity limit, which is structurally far from `D_crit` regardless of the numerical threshold value. The prediction, the pre-registered parameters (N_osc, Q_v, third-harmonic ratio, triad coupling), and the decision trees all carry through unchanged. Only the boilerplate sentence "the bifurcation at D_crit is the Q-C transition" had its numerical value updated.

## 6. Final regime statement

The corrected canonical regime boundary, expressed three ways:

1. **Underdamping condition:** `(D − ζ)² < 4(1 − D)`, at reference mode `ε_k·τ = 1`.
2. **Critical threshold formula:** `D_crit(ζ) = √(2 − ζ)·(2 − √(2 − ζ))`.
3. **Canon-default numerical value:** `D_crit(1/4) ≈ 0.8958`.

Programmatic access:

```python
from edsim.math import d_crit, D_CRIT_CANONICAL, underdamped

D_CRIT_CANONICAL              # ≈ 0.8958
d_crit(0.0)                   # ≈ 0.828
d_crit(0.5)                   # ≈ 0.949
underdamped(0.5, 0.25)        # True (below canonical threshold)
underdamped(0.95, 0.25)       # False (above canonical threshold)
```

## 7. Diff-style summary

### 7A. Code changes (5 files)

| File | Edit |
|:---|:---|
| `edsim/math/damping.py` | **NEW** — helper module with `d_crit, underdamped, D_CRIT_CANONICAL` |
| `edsim/math/__init__.py` | Export damping helpers |
| `analysis/scripts/generate_ed_dimensional_ext_d_vs_scale.py` | Import `D_CRIT_CANONICAL`; replace 4 hard-coded `0.5` references (anchor, axhline, axhspan, legend) |
| `analysis/scripts/generate_ed_logic_diagram.py` | Docstring corrected; Fork 2 panel relabelled with exact discriminant form |
| `analysis/scripts/generate_ed_math_pipeline.py` | Docstring corrected; P6 row and bottom-row "sharp bifurcation" label updated |
| `analysis/scripts/atlas/P6_visual_only.py` | Docstring + 1 comment; image geometry unchanged |

### 7B. Documentation changes (4 files)

| File | Edit |
|:---|:---|
| `theory/Universal_Invariants.md` | §2 full rewrite; summary-table row updated |
| `theory/Architectural_Canon.md` | P6 row rewrite; §3 invariants-bullet updated |
| `theory/ED-Dimensional-01-Ext.md` | Top-of-file caveat banner flagging the physical-threshold re-interpretation question |
| `experiements/ED-09-5-Envelope_InProcess/protocol.md` | Top-of-file update banner; §1 + §2 bifurcation-statement updates |

### 7C. Figures

No PNG/SVG regenerated in this pass. Figure-generator scripts now produce the corrected figures when re-run. Recommend regenerating and committing:

- `docs/figures/atlas/ED-Dimensional-Ext-D-vs-Scale.png`
- `docs/figures/ED-Logic-Flow.png` (from `generate_ed_logic_diagram.py`)
- `docs/figures/ED-Math-Pipeline.png` (from `generate_ed_math_pipeline.py`)
- any P6 atlas PNG generated by `P6_visual_only.py`

Flagged as a follow-up cleanup task.

### 7D. Unchanged

- `edsim` solver (no D_crit logic in core)
- ED-SIM-3D axiom-P7 validation results (driven by computed eigenvalues, not the threshold label)
- ED-09.5 envelope prediction (`ω_v = 2π·N_osc·γ_dec` is good-cavity, not critical-point)
- Archive / historical files (archive/research_history, outputs/) — intentionally not updated; they reflect their authoring date's state
- Orientation §3 Canon P6 row, §4 three-regimes table (already updated 2026-04-22 in the previous pass)

## 8. Open items

1. **ED-Dimensional-01-Ext v0.5+ revision** — resolve whether the named physical thresholds sit at `D_crit` (option 5C-a) or at an equal-rates near-critical point (option 5C-b). Requires a dedicated theory pass; out of scope here.
2. **Figure regeneration.** All affected figure scripts now produce corrected output, but the PNG files on disk are the old versions. Regenerate and commit when time permits.
3. **Legacy references in archive/research_history/** — intentionally left untouched. Flag only if any of that content is promoted back into active theory.
4. **Heuristic as mnemonic.** Canon P6 in [`Architectural_Canon.md`](../../theory/Architectural_Canon.md) currently drops the old heuristic entirely. If the heuristic has pedagogical value, re-introduce it as an explicit "order-of-magnitude mnemonic" rather than a quantitative threshold, per the Orientation §3 Canon P6 row.

---

*Propagation memo v1.0, 2026-04-22. Authors: Test-to-Axiom Mapping Project pivot into theory-consolidation. Source: [`theory/D_crit_Resolution_Memo.md`](../../theory/D_crit_Resolution_Memo.md).*
