# Memo_ED_ChiralityRoutes_Flagged — Future Research Routes for Substrate-Graph Chirality Closure

**Series:** Wave-3 Bookkeeping Memo (Cosmology Arc; research-program tracking)
**Status:** Forward-looking inventory of substrate-graph routes potentially closing the OPEN admission-filter derivation in Paper_ED_Baryogenesis. **Not a derivation. Not a generative paper. No claims of closure on any route.**
**Date:** 2026-05-15
**Anchors:** Paper_ED_Baryogenesis (M2 with P-BinaryAdmission); Memo_ED_BinaryChirality (Criterion-A(3) negative result); Paper_015/T17 (rule-type bundles for gauge fields); Paper_009 (Berry phase); Paper_010 (Aharonov-Bohm); Paper_098_5/T1 (spin-statistics).

---

## Purpose

Memo_ED_BinaryChirality §9 named "ontology extension" as Path-A for the chirality admission-filter closure but left it specified loosely. Conversation with external review (Copilot) sharpened the diagnosis: **ED has the geometry for a Berry phase, but not the topology for a Berry quantization.** Closing the substrate-graph chirality OPEN derivation requires either:

(a) a **fiber-bundle structure** with nontrivial topology over chain-configuration-space, supplying a topological obstruction class that quantizes chirality;
(b) a **holonomy mechanism** in P05 polarity-transport (or V5 cross-chain coupling) producing path-dependent phase content with quantized values around closed loops;
(c) a **curvature-induced quantization** mechanism analogous to Berry-phase quantization in standard QM.

ED's current substrate content has none of these at the chain-arrow level. This memo flags six routes worth investigating in future construction work — none claimed to close, all worth a focused mini-memo if pursued.

---

## Route 1 — Fiber-bundle primitive extension

**Sketch:** extend P07 channel structure (or add an explicit bundle primitive) to support nontrivial topology over chain-configuration-space. The fiber would be P09 polarity ($S^1$); the base would be the substrate-graph configuration space (loci × commitment events). Nontrivial bundle structure supplies the topological obstruction class that quantizes chirality.

**Status if pursued:** would constitute genuine ontology extension (new substrate-graph primitive). Verdict downgrade: any paper using this route would need to argue the new primitive is consistent with the existing 13 + earns its place. Heavy lift.

**Risk:** would change the corpus's "13 primitives" character. Worth doing only if no other route closes.

---

## Route 2 — T17 rule-type bundle inheritance (HIGH PRIORITY)

**Sketch:** Paper_015 / T17 already establishes that ED has **rule-type bundles** for gauge fields. T17's $U(1)$-bundle-over-torus structure (Paper_010 Aharonov-Bohm; Paper_015_5 Photonic-Chern) is genuinely topologically nontrivial — integer-Chern quantization is forced by bundle topology. **Does T17's bundle structure extend to chain-configuration-space, supplying the chirality bundle for free?**

**Initial reading:** likely no — T17's bundle is over physical space (continuum-side spacetime); chirality bundle would need to be over chain-configuration-space (substrate-side commitment-sequence configurations). Different base spaces, different bundle structures. But worth confirming rather than assuming.

**Path forward:** focused construction memo "Memo_ED_RuleTypeBundle_ChiralityExtension" examining whether T17 bundle structure has a substrate-side analog over chain configurations.

**Status if pursued:** if T17 extends, **chirality closure at D-via-I from Paper_015 inheritance** — no new primitives, baryogenesis paper upgrades M2 → M3. Very high-value if it closes.

**Highest-priority route to investigate.**

---

## Route 3 — P05 holonomy from path-dependence

**Sketch:** examine whether P05 polarity-transport along chain edges is path-dependent (non-holonomic) or path-independent (holonomic) in the substrate-graph structure. If non-holonomic, P05 around a closed-loop chain configuration produces nontrivial holonomy = phase shift = discrete invariant if bundle topology forces quantization.

**Key observation:** the corpus has not currently stated whether P05 is holonomic or non-holonomic. This is a substrate-graph question that admits investigation without new primitives — it's a property of P05 as currently defined.

**Path forward:** focused construction memo "Memo_ED_P05_Holonomy" examining P05's path-dependence structure. Three possible outcomes:
- **Holonomic** → P05 doesn't supply a chirality holonomy mechanism; route closes negatively.
- **Non-holonomic with quantized holonomy** → P05 supplies the chirality bundle structure; baryogenesis upgrade M2 → M3 from existing primitives.
- **Non-holonomic with continuous holonomy** → partial; needs additional quantization mechanism.

**Status if pursued:** could close from existing primitives (no ontology extension required) if outcome is the second case. Medium priority — depends on substrate-graph property of P05.

---

## Route 4 — V5 cross-chain coupling as holonomy source

**Sketch:** V5 (Paper_090) supplies cross-chain finite-memory coupling. When chain $C_1$ couples to chain $C_2$ via V5, the substrate-graph content transferred has structural form. Could V5 introduce a chirality holonomy when chains couple cross-chain in cycles?

**Initial reading:** V5 is symmetric in chain-pair structure (per Paper_090 reading; would need spot-check). Symmetric coupling doesn't naturally introduce chain-typing $\mathbb{Z}_2$. But "V5 around a chain-pair cycle" might supply path-dependence.

**Status if pursued:** speculative; would require careful Paper_090 analysis. Lower priority than Routes 2 and 3.

---

## Route 5 — Berry-phase content of Paper_009 extended to chirality

**Sketch:** Paper_009 (Berry phase) establishes substrate-side Berry phase content for QM-kinematics. The Berry phase is geometric (path-dependent in parameter space) but not topologically quantized in Paper_009's current form. **Could Paper_009's Berry-phase machinery extend to chain-configuration-space and supply quantized Berry-phase content?**

**Path forward:** focused construction memo examining Paper_009's substrate-graph structure and whether it admits the topological extension needed for $\mathbb{Z}_2$ chirality quantization.

**Status if pursued:** depends on Paper_009's substrate-graph specifics. Berry phase without quantization is exactly the "geometry without topology" Copilot identified — Paper_009 already has the geometry, the question is whether the topology can be added.

---

## Route 6 — Spin-statistics T1 connection

**Sketch:** Paper_098_5 / T1 establishes spin-statistics theorem at substrate level: D=3+1 forces exactly two statistics classes (boson, fermion). This is already a substrate-side $\mathbb{Z}_2$ structure forced by dimension. **Is T1's $\mathbb{Z}_2$ related to or convertible to chirality $\mathbb{Z}_2$?**

**Initial reading:** likely different structures. Spin-statistics $\mathbb{Z}_2$ is over particle exchange; chirality $\mathbb{Z}_2$ is over chain-arrow alignment with kernel-arrow. Different physical content. But T1 is one of the cleanest substrate-side $\mathbb{Z}_2$ derivations the corpus has — worth confirming the structures are independent rather than assuming.

**Path forward:** quick spot-check of T1 to confirm independence; if independent, no implications for chirality. If unexpectedly related, would supply a substrate-graph $\mathbb{Z}_2$ with a clean derivation.

**Status if pursued:** quick check; either resolves negative (independent) or surprising-positive (related). Low expected value but cheap to verify.

---

## Route 7 — Wilson-line analog in V1

**Sketch:** in gauge theory, Wilson lines are the ordered exponentials of the gauge connection along a path; their trace gives gauge-invariant holonomy. **Could V1's substrate-side propagation along chain edges admit a Wilson-line analog whose holonomy is the substrate-side chirality content?**

**Path forward:** focused analysis of V1's algebraic structure (Paper_089) to see whether ordered-V1-product-along-chain has Wilson-line-class properties.

**Status if pursued:** speculative. V1 in Paper_089 is a kernel, not obviously a connection in the gauge-theory sense. But "kernel composition along chain" is structurally Wilson-line-adjacent. Lower priority.

---

## Priority ordering

| Route | Priority | Rationale |
|---|---|---|
| **2 (T17 inheritance)** | **HIGH** | Existing substrate-graph bundle structure; if extends, closes from primitives without ontology extension. Highest expected value. |
| **3 (P05 holonomy)** | **MEDIUM-HIGH** | Substrate-graph property of P05 admitting investigation; could close from primitives. |
| **5 (Paper_009 Berry extension)** | **MEDIUM** | Existing Berry-phase content; topological extension needed but partially constructive. |
| **6 (T1 connection)** | **LOW (cheap)** | Quick spot-check; either resolves negative or supplies surprising positive. |
| **4 (V5 holonomy)** | **LOW** | Speculative; requires deeper Paper_090 analysis. |
| **7 (V1 Wilson-line)** | **LOW** | Speculative; V1's algebraic structure not obviously gauge-theoretic. |
| **1 (bundle primitive extension)** | **LAST RESORT** | Genuine ontology extension; only pursue if Routes 2–7 all fail. |

---

## Recommendation

Pursue Routes 2 and 3 as focused construction memos when chirality work resumes:

1. **Memo_ED_RuleTypeBundle_ChiralityExtension** (Route 2 — T17 bundle structure over chain configuration space).
2. **Memo_ED_P05_Holonomy** (Route 3 — path-dependence of P05 polarity-transport).

Either closing would supply the substrate-graph chirality derivation and upgrade Paper_ED_Baryogenesis verdict M2 → M3. Routes 4–7 are flagged as backup options; Route 1 is last resort (ontology extension).

If all routes fail after focused investigation, the M2 verdict for Paper_ED_Baryogenesis stands as the honest research-program result, with chirality $\mathbb{Z}_2$ recognized as a genuine substrate-graph open question requiring ontology work to close.

---

**Note on the diagnosis:** Copilot's framing "ED has the geometry for a Berry phase, but not the topology for a Berry quantization" is the cleanest one-line statement of the substrate-graph terrain. The Berry-phase analogy is precise — the chirality's continuous P09 phase is structurally Berry-class — and the missing topological-quantization mechanism is exactly what Routes 1–7 attempt to supply. Worth keeping this framing visible in any future chirality work.

---

**End Memo_ED_ChiralityRoutes_Flagged.**
