# Phase B5 — Citation-Chain Integrity Audit

**Round 2 — Phase B Step 5**
**Edges audited:** 49 (target 40–60)
**Distribution:** C1 = 38 (78%), C2 = 6 (12%), C3 = 1 (2%), C4 = 2 (4%), C5 = 0.

---

## §1 Summary Table

| # | Downstream → Upstream | Claim | Class |
|---|---|---|---|
| 1 | Paper_054 → Paper_087 | 13 primitives postulated | C1 |
| 2 | Paper_054 → Paper_089 | V1 baseline rate Γ₀ = c/ℓ_ED | C1 |
| 3 | Paper_054 → Paper_090 | V5 cross-chain bandwidth Γ_cross | C1 |
| 4 | Paper_077 → Paper_089 | V1 finite second moment | C1 |
| 5 | Paper_077 → Paper_084 | Vortex-stretching obstruction | C1 |
| 6 | Paper_077 → Paper_076 | NS-2 substrate→continuum | C1 |
| 7 | Paper_084 → Paper_090 | V5 cross-chain budget cap | C1 |
| 8 | Paper_062 → Paper_039 | Γ_cross → 0 at horizon | C1 |
| 9 | Paper_062 → Paper_058 | Q-COMPUTE wall = V5 saturation | C1 |
| 10 | Paper_062 → Paper_090 | V5 substrate mechanism | C1 |
| 11 | Paper_043 → Paper_025 | Holographic count N = 4πR²/ℓ_ED² | C1 |
| 12 | Paper_043 → Paper_039 | Horizon as decoupling surface | C1 |
| 13 | Paper_043 → Paper_067 | vN entropy via Shannon–Khinchin | C1 |
| 14 | Paper_036 → Paper_027 | Newton's G + Poisson Newtonian limit | C1 |
| 15 | Paper_036 → Paper_029 | a_0 in MOND interpolation | C1 |
| 16 | Paper_036 → Paper_034 | Deep-MOND limit | C1 |
| 17 | Paper_027 → Papers_018/019 | ħ from YM-arc | C1 |
| 18 | Paper_097 → Paper_091 | Memory-kernel cascade | C1 |
| 19 | Paper_097 → Paper_096 | Cross-scale invariance | C1 |
| 20 | Paper_097 → Paper_073 | DCGT | C1 |
| 21 | Paper_097 → Paper_089 | V1 kinematic-window | C1 |
| 22 | Paper_063 → Paper_087 | P02/P03/P07 | C1 |
| 23 | Paper_063 → Paper_001 | Pre-individuation amplitude | C1 |
| 24 | Paper_088 → Paper_087 | 13-primitive enumeration | C1 |
| 25 | Paper_088 (P02 row) → Paper_063 | P02 in entanglement | C1 |
| 26 | Paper_088 (P06 row) → Papers_025/027 | 3+1 dim load-bearing | C1 |
| 27 | Paper_093 → Paper_089 | V1 retarded support | C1 |
| 28 | Paper_093 → Paper_090 | V5 finite-memory directional | C1 |
| 29 | Paper_093 → Paper_073 | DCGT for arrow inheritance | C1 |
| 30 | Paper_093 → Paper_018 | DCGT-NA | C1 |
| 31 | T19 → Paper_028 | "substrate-gravity foundational" mislabel | **C2** |
| 32 | T19 → Paper_029 | "stability-landscape coupling" mislabel | **C2** |
| 33 | T19 → Paper_032 | "scalar-curvature coarse-graining" mislabel | **C2 (mild)** |
| 34 | T19 → Paper_036 | Newtonian Poisson limit | C1 |
| 35 | T19 → Paper_073 | DCGT bridge | C1 |
| 36 | **T19 ↛ Paper_027 MISSING** | Newton's G structural derivation | **C4** |
| 37 | T20 → Paper_030 | ECR | C1 |
| 38 | T20 → Paper_031 | BTFR slope-4 invokes a_0 | C1 |
| 39 | T20 → Paper_033 | P-MOND-Interpolation-Substrate | C1 |
| 40 | T20 → Paper_034 | P-No-New-Primitive | C1 |
| 41 | T20 → Paper_037 | P-H0-Cosmological-Invariant | C1 (verified §2.3 L52) |
| 42 | **T20 ↛ Paper_029 MISSING** | a_0 = cH₀/(2π) defining formula | **C4** |
| 43 | T21 → Paper_030 | ECR | C1 |
| 44 | T21 → Paper_031 | BTFR slope-4 | C1 |
| 45 | T21 → T19, T20 | propagation (inherits C4) | (inherits C4) |
| 46 | T21 → Paper_028 | mislabel inherited from T19 | **C2** |
| 47 | T21 → Paper_029 | mislabel inherited from T19 | **C2** |
| 48 | T21 → Paper_034 | Deep-MOND framing | C1 |
| 49 | T21 → Paper_038 | "cosmological consistency" | **C3** (contextual not load-bearing) |

---

## §2 High-Priority Findings (Big Three Upstream Nodes)

### 2.1 Paper_087 (Canonical Primitives) — 4 audited

All four sampled downstream citations (Paper_054, Paper_063, Paper_088, plus implicit references in T-stubs) cite Paper_087 correctly for the 13-primitive enumeration. No overclaims. The "13 primitives postulated per Paper_087" pattern is consistently used as an axiomatic P-row, never as a D-row. Given Paper_087's downstream count of 93, the sample is small but covers diverse arcs (Q-Compute, Entanglement, audit-meta, theorem stubs); no integrity issues detected.

### 2.2 Paper_090 (V5 Kernel) — 5 audited

Edges sampled: Paper_054 → 090 (Γ_cross bandwidth), Paper_062 → 090 (V5 substrate mechanism), Paper_077/084 → 090 (cross-chain budget cap, vortex obstruction), Paper_093 → 090 (V5 finite-memory directional flow). All C1. Downstream papers consistently treat V5's properties (finite memory τ_V5, cross-chain bandwidth budget, even envelope, forward-causal directionality) as INHERITED from Paper_090. No paper overclaims V5 as deriving content Paper_090 does not supply.

### 2.3 Paper_089 (V1 Kernel) — 4 audited

Edges sampled: Paper_054 → 089 (baseline rate Γ₀ = c/ℓ_ED), Paper_077 → 089 (V1 finite second moment), Paper_097 → 089 (V1 kinematic-window), Paper_093 → 089 (V1 retarded support). All C1. The V1 finite-width retarded property and second-moment finiteness are consistently INHERITED rather than re-derived. Big-Three integrity is the strongest positive finding of this audit.

---

## §3 Cross-Arc Findings

All 8 sampled cross-arc edges are C1:
- **QFT → Gravity:** Paper_027 → Papers 018/019 for ħ derivation from YM-arc.
- **Gravity → BH:** Paper_043 → Paper_025 (holographic bound) and Paper_039 (horizon decoupling).
- **NS → Soft-Matter:** Paper_077 → Paper_076, Paper_084 (chain intact).
- **Q-Compute → BH:** Paper_062 → Paper_039 cross-domain echo (V5-shared mechanism).
- **Wedges → Wedges:** Paper_097 → Paper_091, 096, 073 (chain intact).

The prompt example "Paper_017 cites Paper_007" was not found in either the registry or via grep — likely a speculative example rather than an actual edge. No finding produced for it.

The cross-arc citation discipline is honest. Where Paper A in one arc cites Paper B in another, the citation correctly classifies B's content as INHERITED rather than absorbing it as derived.

---

## §4 Theorem-Stub Findings (T18–T21)

### 4.1 T18 (Paper_093) — every I-row audited

**Result: 4/4 clean (C1).** Paper_093's upstream I-rows are I-073 (DCGT), I-089 (V1 retarded), I-090 (V5 forward-flowing memory), I-018 (DCGT-NA). Each upstream paper genuinely delivers the claimed content. T18 introduces P-T18-Kernel-Retardation and P-T18-Arrow-Inheritance as its own postulates rather than over-attributing them to upstream papers. No breakage to propagate downward.

### 4.2 T19 — every I-row audited

**Result: 1 C4, 3 C2, 2 C1.** This is the audit's worst finding.

- **C4 (critical):** I-027 is **MISSING ENTIRELY**. Paper_027 ("Newton's G from Substrate Constants") is the only paper in the corpus that structurally constructs G = c³ℓ_P²/ħ from substrate primitives (P02+P03+P07+P08+P12 via V1 holographic count). T19's §3.2/§3.3 invokes "G as proportionality coefficient" but supplies no upstream source for the substrate identification. The chain technically closes via Paper_036 (which cites 027), but the I-row list is structurally incomplete.
- **C2 mislabels:** T19 calls Paper_028 "substrate-gravity foundational content" — Paper_028 is actually the H₀ cosmic-horizon paper (R_H = c/H₀). T19 calls Paper_029 "substrate-gravity stability-landscape coupling" — the stability-landscape paper is Paper_026, and Paper_029 is the a_0 derivation paper. T19's I-032 description "scalar-curvature coarse-graining" is mild mislabel (Paper_032 is the six-WF-prerequisites paper, not curvature-coarse-graining).
- **C1:** I-036 (Newtonian Poisson limit) and I-073 (DCGT) are correctly described.

### 4.3 T20 — every I-row audited

**Result: 1 C4, 5 C1.** 

- **C4 (critical):** I-029 is **MISSING ENTIRELY**. Paper_029 IS the defining derivation of a_0 = cH₀/(2π) — the formula T20 names in §1 Statement. T20 cites Paper_037 (which inherits the formula from Paper_029), so the chain closes by indirection, but the structurally-required source paper is omitted from T20's upstream.
- **C1:** I-030 (ECR), I-031 (BTFR slope-4), I-033 (P-MOND-Interpolation-Substrate), I-034 (P-No-New-Primitive), I-037 (P-H0-Cosmological-Invariant — verified present in Paper_037 §2.3 line 52) all correctly described.

### 4.4 T21 — every I-row audited

**Result: 2 C2 (inherited from T19), 1 C3, 1 inherited-C4 from T19/T20, 5 C1.**

T21's §3 algebraic derivation is structurally clean given G and a_0 as inputs. The breakage in T19/T20 propagates through I-T19, I-T20. Local issues:
- **C2:** Paper_028 and Paper_029 mislabels copied from T19 word-for-word.
- **C3:** I-038 ("cosmological consistency") is contextually cited rather than load-bearing for the §3.4 deep-MOND algebra. Not an error, but flagged as overinclusion.
- **C1:** I-030 (ECR), I-031 (BTFR), I-034 (Deep-MOND framing) correctly described.

---

## §5 Correction Plans

### 5.1 T19 §2.2 — Replace upstream dependencies

Recommended new list:
- **I-027:** Newton's G structural identification G = c³ℓ_ED²/ħ (Paper_027). **[LOAD-BEARING — newly added]**
- **I-025:** Holographic participation-count bound (Paper_025). **[LOAD-BEARING via 027]**
- **I-026:** P12 stability-landscape cumulative-strain reading (Paper_026). **[LOAD-BEARING via 027]**
- **I-036:** MOND field equation; Newtonian limit μ→1 (Paper_036). **[LOAD-BEARING]**
- **I-073:** DCGT substrate-to-continuum bridge (Paper_073). **[LOAD-BEARING]**
- **I-032:** Weak-field prerequisites (Paper_032). **[CONTEXT]**

Update §3.2/§3.3 to cite Paper_027 explicitly when identifying the coefficient as G.

### 5.2 T20 §2.2 — Insert I-029 at top

- **I-029:** a_0 = cH₀/(2π) substrate-cosmology dipole-projection (Paper_029). **[LOAD-BEARING]**
- **I-028:** Cosmic decoupling surface R_H = c/H₀ (Paper_028). **[LOAD-BEARING via 029]**

Retain existing five I-rows.

### 5.3 T21 §2.2 — Fix labels, demote I-038

(a) Relabel inherited I-028/I-029 to match corrected T19 wording (or drop entirely; Paper_030 + Paper_031 + T19 + T20 suffice for §3).
(b) Demote I-038 to contextual / consistency-check (not load-bearing for §3.4 deep-MOND algebra).
(c) I-T19 / I-T20 auto-correct via 5.1/5.2.

### 5.4 Registry rebuild

After 5.1–5.3, rerun Phase A registry extraction so `registry_citation_graph.md` includes top-level T19/T20/T21 entries. Consider aliasing T19→Paper_NNN (or moving them into the Paper_NNN namespace) for glob compatibility with the rest of the corpus naming convention.

---

## §6 Recommended Order of Fixes (cheapest first)

1. **T20 §2.2 add I-029** — ~2 min, single-line insertion, highest impact-to-effort.
2. **T19 §2.2 add I-027 + correct mislabels** — ~10 min, highest structural importance.
3. **T19 §3.2/§3.3 cite Paper_027 explicitly** — ~10 min.
4. **T21 §2.2 fix labels + demote I-038** — ~5 min.
5. **Registry rebuild** — ~5 min once naming conventions are settled.

**Total: ~35 minutes for full correction.**

### Deferred to future audit rounds:

- Paper_087 internal load-bearing audit consistency (large-scale per-primitive sweep).
- QM-kinematics arc internal cross-citations (Papers 001–012).
- YM chain integrity (Papers 018–023).
- Q-COMPUTE Class A/B/C cross-citations (Papers 055–060).
- Paper_101 falsification register (37 upstream — substantial separate audit).
- Full ~500-edge graph (~10× present effort for complete coverage).

---

## Relevant file paths

- `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\T19.md`
- `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\T20.md`
- `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\T21.md`
- `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\Paper_027_Newtons_G_FIXED.md` (load-bearing missing upstream for T19)
- `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\Paper_029_a0_FIXED.md` (load-bearing missing upstream for T20)
- `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\Paper_037_a0_Invariance_FIXED.md` (P-H0-Cosmological-Invariant verified present at line 52)
- `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\Paper_093_T18_ArrowOfTime_FIXED.md` (T18 clean)

---

**End of Phase B5 audit report.**
