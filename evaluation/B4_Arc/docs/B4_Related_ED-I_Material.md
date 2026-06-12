# B4 — Related ED-I Material (context, not verdict)

**Status:** CONTEXT NOTE. This does **not** reopen or modify the closed B4 arc verdict. It records how two interpretive ED-Interpretation papers frame the B4 result, plus the open questions the connection raises. Everything here is a **flagged hypothesis**, not a finding.

**Sources:**
- `ED-I-05 — Magnetism as Directional Participation` (Allen Proxmire, Feb 2026).
- `ED-I-06 — Fields and Forces in Event Density` (Allen Proxmire, Feb 2026).
- (both at `Desktop/ED Important/ED Interpretations/ED-I/`).

---

## Cautions (read first)

1. **ED-I papers are interpretive, not derivations.** No math, no Σ-rule, assert-not-derive. Treat as conceptual companions, not formal anchors.
2. **The scalar = rho mapping is solid; directional = orientation is natural but not explicit.** ED-I-06 §4's mechanism matches Σ's rho-terms exactly (see below); the directional↔orientation identification is the obvious reading but the papers name "directional organization," not `orientation`/P05/P09.
3. **ED's scalar/directional asymmetry is unlike EM's electric/magnetic symmetry — an open question, not a contradiction.** Do not present it as a refutation of either ED or EM.
4. **None of this reopens B4; it contextualizes it.**

## The connection

ED-I-06 proposes three field classes that map onto the substrate's actual state variables and onto what B4 found about Σ:

| ED-I-06 field class | ED substrate object | Σ coupling (from B4) |
|---|---|---|
| **Scalar field** (density gradient) | `rho` (commitment density) | **STRONG** — Σ's Strain + Grad terms read it directly |
| **Directional field** (orientation) | `orientation` / polarity (P05/P09) | **WEAK** — Σ orientation-blind; only P04/P05 |
| **Curvature-like field** (combined) | rho × orientation geometry | → gravity / ED-10 (out of B4 scope) |

**Concrete grounding (the strong part of the mapping).** ED-I-06 §4 says scalar fields make "micro-events tend to propagate **toward lower-density regions**." That is literally the certified Σ-rule: the **Strain** term penalizes dense targets (`strain = rho_v`) and the **Grad** term penalizes `|rho_v − rho_u|` (see `simulator/sigma.py`). So ED-I-06's scalar-field *mechanism* is the rho-sector of Σ already implemented in code — not analogy, the same rule in prose.

**Corroboration of B4's central finding.** ED-I-05 locates magnetism in directional participation that "favors propagation along the aligned direction" — i.e. transport/bandwidth anisotropy (P04/P05), **not** Σ. That is exactly the only coupling channel B4 derived for orientation (Step 2). An independent, qualitative paper puts the physics of orientation precisely where B4's formal invariant says it must go.

## Why this sharpens (not reopens) B4

The two papers + the B4 audit triangulate on one structural fact: **ED cleanly separates a Σ-active scalar (rho / potential-like) sector from a Σ-blind directional (orientation / charge / winding) sector**, with orientation-blindness as the barrier between them.

The sharp consequence: ED-I-06 puts **electric *potential*** in the scalar (rho) sector, while B4 put the **charge candidate (winding)** in the directional (orientation) sector. In EM, charge sources potential (∇²φ = −ρ). B4 Steps 1–4 found the orientation sector is **decoupled** from the rho/Σ sector — the winding does not source rho. So **B4's "no sourcing" finding is the same gap as the gap between ED-I-06's two "electric" locations**: charge-sector and potential-sector are decoupled by the very invariant B4 characterized. This *explains* B4's result; it does not change it.

## Open questions (flagged hypotheses, for a possible future arc — NOT now)

1. **U(1) vs Z₂ for the directional "spin."** ED-I-05 says spin has "two preferred orientations (up/down)" — Z₂/Ising-flavored, which maps to the **recon's Z₂ tension-sign candidate**, not B4's U(1) winding. It also says "directional organization" — vector/U(1)-flavored. Only the U(1) reading carries the winding. *Disambiguate before building on the link.*
2. **Two "electric" candidates, decoupled.** Is electric charge the orientation winding (B4) or something in the rho/scalar sector (ED-I-06's potential), or are they the source/field pair that ED fails to couple? B4 shows they are decoupled as-built; EM requires them coupled. Which is the real "charge" in ED is unresolved.
3. **Electric/magnetic asymmetry vs EM symmetry.** ED makes the scalar (electric-potential-like) sector Σ-active/strong and the directional (magnetic-like) sector Σ-blind/weak. EM unifies the two (Lorentz invariance mixes them). Whether ED's sector asymmetry survives coarse-graining or genuinely diverges from EM is **open** — a place to watch, not a verdict.

## Net

ED-I-05/06 are the **vision** (a unified participation account of fields and forces); the B4 arc is the **audit** (the formal substrate gives the topological skeleton of charge and decouples it from the scalar/potential sector). The audit and the vision agree on the architecture (two sectors, one barrier) and disagree only where the vision is aspirational and the substrate is not yet — which is exactly the honest, useful place for them to meet.
