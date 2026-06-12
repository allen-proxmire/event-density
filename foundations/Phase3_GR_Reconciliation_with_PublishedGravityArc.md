# Reconciliation: Phase-3 GR (khronometric) vs the Published Gravity Arc (scalar-tensor / MOND)

**Internal reconciliation memo — not a publication paper. Working material toward GR-I.**
**Author:** Allen Proxmire · June 2026

**Purpose.** The Phase-3 GR rounds (this `foundations/` arc) were developed largely in isolation from the published Wave-2/3 gravity corpus (Papers 025–039), and they reach a *different* picture of ED gravity. Before any standalone GR paper, this memo maps the two against each other honestly: what they share, where they genuinely diverge, which divergences are real conflicts versus same-object-under-different-descriptions, and what concrete computation would resolve each. **It claims no resolution — it lays out the landscape and the leading reconciliation hypothesis so the divergence is handled in the open rather than papered over.**

---

## 1. The shared foundation (common ground)

Both programs rest on the same substrate-gravity base, and on this they agree:

- **Newton recovery:** `a = GM/r²` is form-FORCED at substrate level (Paper_027), with `G = c³ℓ_P²/ℏ` and `ℓ_ED = ℓ_P` value-INHERITED (Paper_027.5, M3).
- **An emergent metric is the right object** — neither treats spacetime geometry as fundamental (consistent with the Contrast-First ontology's "no fundamental metric").
- **DCGT** (Paper_073) bridges substrate-discrete content to the continuum.
- **Value-inherited constants** methodology (form-FORCED / value-INHERITED; Paper_095 verdict grammar).

So the disagreement is *not* about Newton, the constants, or the emergence stance. It is about **which metric, which gravity class, and which Lorentz status** sit on top of that shared base.

## 2. The three divergences, stated precisely

| Axis | Published arc (Papers 025–039) | Phase-3 (`foundations/`) |
|---|---|---|
| **Metric** | cumulative-strain + kinematic-flow **acoustic metric** (P02/P03/P06), Paper_033 | **bandwidth metric** `g_ij ~ b⁻¹` (P04) |
| **Class** | **scalar-tensor / relativistic-MOND**, explicitly "non-GR"; field eq Paper_036; a₀, ECR, BTFR central | **khronometric** (Hořava IR), **Einstein-class** at weak field; factor-of-2, redshift |
| **Lorentz** | kernels "**Lorentz-covariant** in flat spacetime" (Paper_032 WF-6) | **preferred-frame, Lorentz-violating** (P11/P13 arrow → foliation) |
| **MOND (a₀, BTFR)** | central empirical content (`a₀ = cH₀/2π`) | not addressed |

These are not cosmetic. Left unreconciled, a "weak-field Einstein from ED" paper would appear to contradict the published claim that ED gravity is scalar-tensor MOND and *explicitly not GR*, and would never mention a₀ or BTFR — exactly the inconsistency to avoid.

## 3. Reconciliation analysis (per axis)

### 3A. Metric — same object or two constructions? **(open; the central technical gap)**

The acoustic metric (P02/P03/P06 strain + flow) and the bandwidth metric (`b⁻¹`, P04) are built from **different primitives**, so they are not *manifestly* the same object. Three possibilities:

1. **Same metric, two descriptions** — bandwidth `b` is functionally tied to strain/flow content, so `b⁻¹ ∝ g^{acoustic}` in the shared weak-field limit. (Plausible: an edge's bandwidth/coupling capacity and the strain/flow across it are not independent.)
2. **Bandwidth fundamental, acoustic effective** (or vice versa) — one is the substrate-level metric, the other its coarse-grained shadow.
3. **Genuinely different** — only one is "the" spacetime metric; the other is a different effective geometry.

**Resolution:** a direct computation — does `b⁻¹` coincide with the Paper_033 acoustic `g^{αβ}` in the common weak-field/Newtonian limit where both must reduce to `g_00 = −(1+2Φ)`, `∇²Φ = 4πGρ`? Both *do* share that Newtonian limit (§1), which is evidence for (1)/(2); whether they agree beyond Newtonian order is unproven. **This is the load-bearing open question** — most of the class/Lorentz discussion is conditional on it.

### 3B. Class & MOND — likely *unifiable*, not contradictory **(leading hypothesis)**

Khronometric / Einstein-aether gravity is **not** incompatible with MOND — there is an established line in the literature in which the preferred-frame (aether/khronon) field sources MOND-like phenomenology in the deep-IR (aether-as-dark-matter / khronometric MOND). This suggests the most economical reconciliation:

> **One khronometric ED-gravity, two regimes.** At solar-system / black-hole scale (strong binding, `a ≫ a₀`) it reduces to GR / Einstein-class — the Phase-3 result (factor-of-2, Schwarzschild relation). In the deep galactic field (`a ≲ a₀`) the khronon sources the MOND behavior — the published arc's a₀ / BTFR content. The transition scale `a₀ = cH₀/2π` is **cosmological**, which is *natural* for a preferred frame tied to the cosmic rest frame: the same khronon that breaks boost invariance is anchored to the Hubble-scale cosmic frame, so its IR effects switch on at `a₀ ∼ cH₀`.

If this holds, the two programs are **the same theory in different regimes**, and Paper_033's scalar-tensor description is the **effective IR/MOND-sector description** of the khronometric theory — not a competitor to it. **What it requires (not yet shown):** that ED's specific khronon reproduces (i) the MOND interpolation, (ii) `a₀ = cH₀/2π`, and (iii) slope-4 BTFR. Until then this is a *hypothesis*, and the cleanest one — but it is unproven and must be labeled as such.

### 3C. Lorentz — the apparent conflict largely dissolves **(reconcilable)**

Paper_032 WF-6 ("Lorentz-covariant kernels in flat spacetime") and Phase-3's "preferred-frame, Lorentz-violating" look contradictory but operate in **different sectors**, and Phase-3 R12's own result bridges them:

- R12 found ED's Lorentz violation is **universal** — all species share one cone (single substrate, one P05 transport) — so there is **no differential matter-sector LV**, and universal LV is removable by a coordinate rescaling, leaving the **matter sector effectively Lorentz-invariant**. That is exactly WF-6's claim, at the effective level.
- The preferred frame is real but lives in the **gravitational** sector (the foliation). A healthy khronometric theory looks precisely like this: matter sees an (effectively) Lorentz-invariant cone; gravity carries the preferred frame.

So WF-6 (matter, flat-space) and khronometric LV (gravity) are **compatible**, not contradictory — provided the universal-cone result holds. The honest residual: strictly, the preferred frame is underlying-real, so WF-6 should be read as *effective* matter Lorentz-invariance, not exact. Minor reframing, not a conflict.

## 4. The "pivot"

Paper_033 records only a "**pre-pivot** conditional-positive verdict" for the *scalar-tensor* acoustic-metric route, and Arc ED-10 (curvature emergence) is repeatedly called "in-queue." Phase-3 *is* a curvature-emergence program, and it reached **khronometric**, not scalar-tensor. So Phase-3 most likely represents a **post-pivot revision** of the Arc ED-10 verdict: from scalar-tensor (Paper_033, pre-pivot) to khronometric (Phase-3). Under §3B that is not a contradiction but a *deepening* — the scalar-tensor/MOND description becomes the IR limit of the khronometric theory. **Whether this pivot is intended is Allen's call**; the corpus's own "pre-pivot" labeling leaves the door open.

## 5. Net assessment

The two programs are **not cleanly contradictory.** The most likely picture, consistent with everything above, is a **single khronometric ED-gravity** in which:

- the shared Newtonian base (§1) is common ground;
- solar-system / BH scale → **GR / Einstein-class** (Phase-3: factor-of-2, redshift, Schwarzschild relation);
- deep galactic field → **MOND** via the khronon, with `a₀ = cH₀/2π` from the cosmic-frame anchoring (published arc);
- matter sector **effectively Lorentz-invariant** (universal cone, R12), gravitational sector preferred-frame;
- Paper_033's scalar-tensor description = the **IR/MOND-sector effective theory** of the khronometric whole.

This is attractive and falsifiable — but it is a **hypothesis resting on three unproven derivations**: (1) the bandwidth metric coincides with the acoustic metric beyond Newtonian order (§3A); (2) ED's khronon reproduces a₀ + BTFR (§3B); (3) the universal-cone matter-Lorentz-invariance is explicit (§3C). Until those are done, Phase-3 and the published arc are **parallel constructions sharing the Newtonian base** but differing in metric, class, and Lorentz status.

## 6. Implications for GR-I (recommendation)

GR-I **cannot** be written as a clean extension of the published corpus. Two honest paths:

- **(A) Position GR-I as the post-pivot khronometric curvature-emergence result.** It would (i) inherit the shared Newtonian base; (ii) derive the new content (lapse `N²~b`, Schwarzschild relation, factor-of-2, redshift); (iii) include an explicit *positioning* section relating it to Paper_033 (scalar-tensor → khronometric, with the MOND-as-IR-limit hypothesis flagged as future work, §3B); (iv) state the Lorentz reconciliation (§3C). This is publishable and honest, but it *commits to the pivot* and carries the three open items as declared future work.
- **(B) Do the metric-coincidence computation first (§3A).** Ground the bandwidth metric against the acoustic metric before any GR-I, so the paper doesn't rest on an unproven identification of two different constructions.

**Recommended order:** decide the pivot (is Phase-3 the intended current direction?). If yes → path (A), with §3A/§3B/§3C as declared open items and the positioning section mandatory. If the relationship should be nailed down first → path (B). Either way, the MOND content and the Lorentz status must be addressed *in* the paper, not omitted.

---

*Reconciliation memo only. No result claimed; the §5 unified picture is a labeled hypothesis resting on three unproven derivations. Its value is that the divergence between Phase-3 and the published gravity arc is now explicit, characterized, and equipped with concrete resolution steps — so any GR paper is written in the open rather than in tension with the corpus.*
