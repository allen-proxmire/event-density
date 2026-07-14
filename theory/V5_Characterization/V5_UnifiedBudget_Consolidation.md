# V5 Unified Budget: One Envelope, Three Budgets, Two Forced Relations

**Series:** Event Density (ED) — V5 Characterization
**Status:** Derivation note (structural / form-forced tier; O(1) coefficients inherited). Consolidates three separately-postulated V5 budgets into projections of one bounded envelope and extracts the falsifiable content that survives the inherited scale.
**Sources read verbatim:** `Paper_090_V5Kernel` (§4.1–4.2 boundedness/finite-width), `Paper_065_Monogamy` (P-V5-Budget, $W_{V5}$), `Paper_058_ClassC_Plateau` (P-Corr-Budget, $B_{\mathrm{cross,max}}$, $R_C^{\mathrm{sat}}$, $\Gamma_{\mathrm{plateau}}$), `Paper_050_PageCurve` (P-V5-EntBudget, $B_{\mathrm{ent,max}}^{V5}$), `Paper_053_Mcap` ($\mathcal{M}_{\mathrm{cap}}=\min\{N_{\rm bw},N_{V5},N_{\rm commit}\}$).

---

## What this does, and does not, claim

**Does:** shows that the three finite V5 budgets the corpus postulates separately — monogamy's $W_{V5}$ (065), the Class-C plateau's $B_{\mathrm{cross,max}}$ (058), and the Page curve's $B_{\mathrm{ent,max}}^{V5}$ (050) — are **projections of a single bounded V5 envelope** $W_{\max}=\int F_{V5}$, whose finiteness is form-forced. Extracts the two things that are forced *independent of the inherited envelope scale*: (R1) a complexity-universal plateau onset (a band in any lab proxy, a point in the substrate variable), and (R2) fixed O(1) ratios linking the three budgets across arenas.

**Does not:** derive the absolute value of $W_{\max}$, $\Gamma_{\mathrm{plateau}}$, $t_{\mathrm{Page}}$, or the CKW coefficient. The V5 envelope's scale ($\tau_{V5}$, $\ell_{V5}$) is a substrate constant (like $\ell_P$); it is inherited, and five prior derivation passes confirm it resists a closed form. The O(1) projection factors depend on the envelope *shape*, which is inherited. This note does not fabricate a number; it makes explicit which *relations* are forced once the number is inherited once.

---

## 1. The one bounded envelope (form-forced)

`Paper_090` fixes the V5 kernel as
$$
K_{V5}(A,B) = \theta(t_A-t_B)\,F_{V5}\!\big(\sigma/\ell_{V5}^2,\ \Delta t/\tau_{V5}\big),
$$
with $F_{V5}$ **bounded and finite-width** (§4.1: "no $\delta$-function limit and no infinite-width limit") and V5 producing **bounded cross-chain correlations** (§4.2). Boundedness + finite width means the total integrated weight of the envelope is finite:
$$
\boxed{\;W_{\max} \;\equiv\; \int F_{V5}\,\mathrm{d}\mu \;<\;\infty\;}
\qquad(\text{form-forced: P04 additivity} + \text{§4.1–4.2 boundedness}).
$$
$W_{\max}$ is the **total cross-chain correlation weight the substrate can carry through V5, per chain**. Its *existence and finiteness* are forced; its *value* rides on the envelope scale ($\tau_{V5},\ell_{V5}$) and is inherited. This is the "budget FORM forced, value inherited" fact already noted in the V5 characterization scoping; the step here is to treat $W_{\max}$ as the single parent of the three arena budgets.

## 2. The three budgets are projections of $W_{\max}$

Each arena postulates a finite V5 budget. Read against §1, each is $W_{\max}$ restricted to a content-type and a geometry:

| Arena | Postulated budget | Projection of $W_{\max}$ | Projection factor |
|---|---|---|---|
| Monogamy (065) | $W_{V5}=\int K_{V5}(r,r')\,\mathrm{d}r'$ per chain $\le W_{\max}$ | the per-chain total itself | $\;1\;$ (this *is* $W_{\max}$, per chain) |
| Class-C plateau (058) | $B_{\mathrm{cross}}(u)\le B_{\mathrm{cross,max}}$ per locus | per-locus **density** of the weight | $\rho_{\rm loc}$ (weight per substrate locus) |
| Page curve (050) | $B_{\mathrm{ent}}(t)\le B_{\mathrm{ent,max}}^{V5}$ across a boundary | the **entangling fraction** on a boundary | $f_{\rm ent}\cdot g_{\partial}$ (ent-fraction $\times$ boundary geometry) |

so
$$
W_{V5}=W_{\max},\qquad
B_{\mathrm{cross,max}}=\rho_{\rm loc}\,W_{\max},\qquad
B_{\mathrm{ent,max}}^{V5}=f_{\rm ent}\,g_{\partial}\,W_{\max}.
$$

This matches the corpus's own hedges exactly: 050 states its budget is *"structurally related to but distinct from"* 058's — precisely the statement that they share the parent $W_{\max}$ but carry **different projection factors** ($f_{\rm ent}g_\partial$ vs $\rho_{\rm loc}$). The factors are geometric/content ratios: $\rho_{\rm loc}$ is a density (per-chain weight spread over the loci a chain spans), $f_{\rm ent}\in(0,1]$ is the fraction of the envelope weight that carries *entanglement* amplitude rather than general correlation, and $g_\partial$ is the near-horizon straddling-boundary geometry.

## 3. Consolidation

The three postulates — **P-V5-Budget** (065), **P-Corr-Budget** (058), **P-V5-EntBudget** (050) — collapse to **one** substrate commitment (a finite V5 envelope, §1) plus **three geometric/content projections**. This is the "one $\Lambda$, two descriptions" move (KM-II §7) applied to the V5 budget: three inherited postulates $\to$ one inherited scale $+$ O(1) projection factors. It removes two independent inherited numbers from the corpus (their *ratios* are now fixed, §5) and it is the standard ED shape: one inherited scale, forced O(1) structure on top.

## 4. Relation R1 — the plateau onset is universal in complexity (a band in the proxy)

Class-C (058) is $N_{V5}$-limited (053): the plateau is where the cross-chain correlation *content* saturates the budget. Writing the per-correlated-pair envelope cost as $w_{\rm pair}$, the number of channels the budget can co-correlate is
$$
N_{V5}\;=\;\frac{B_{\mathrm{cross,max}}}{w_{\rm pair}}\;=\;\frac{\rho_{\rm loc}\,W_{\max}}{w_{\rm pair}},
$$
a substrate quantity fixed by the envelope alone. **The plateau onset is at fixed correlation-content $B_{\mathrm{cross,max}}$ for every Class-C architecture** — 058 §5.2's cross-platform-consistency claim, now read as a consequence of the single envelope.

In any *lab proxy* the onset is a **band**, not a point, because the proxy-to-content conversion varies by architecture. For redundancy/code distance $R_C$, 058 has $B_{\mathrm{cross}}(R_C)\approx\alpha R_C$ with $\alpha$ the architecture-specific redundancy$\to$coverage coefficient, so
$$
R_C^{\mathrm{sat}}=\frac{B_{\mathrm{cross,max}}}{\alpha}
$$
spreads over a range as $\alpha$ varies. This is **the same figure as the Class-A wall**: the wall is sharp in $M_{\rm eff}$ (multiplicity = internal complexity) and a band in mass because complexity-per-kDa varies (`Paper_056`: $m_{\rm wall}=\mathcal M_{\rm cap}\,m_u/(\alpha\beta)$); the plateau is sharp in $B_{\mathrm{cross,max}}$ (correlation content = internal complexity) and a band in code distance because content-per-channel varies. **In both, the sharp variable is internal complexity; mass and code-distance are proxies; the band is the proxy-shadow of a sharp complexity threshold.** (This is AP's reframe, made precise.)

**R1, stated:** the Class-C plateau (and the Class-A wall) is a *point in the substrate complexity variable, a band in the lab proxy.* Forced (given the single envelope + architecture-varying proxy conversion). Falsified if two architectures plateau at genuinely different correlation-content after their own conversion.

## 5. Relation R2 — fixed O(1) ratios across the three arenas

Because all three budgets are $W_{\max}$ times a projection factor, their ratios **cancel the inherited scale**:
$$
\frac{B_{\mathrm{ent,max}}^{V5}}{B_{\mathrm{cross,max}}}=\frac{f_{\rm ent}\,g_\partial}{\rho_{\rm loc}},\qquad
\frac{W_{V5}}{B_{\mathrm{cross,max}}}=\frac{1}{\rho_{\rm loc}}.
$$
These are O(1) numbers set by the envelope *shape* and the arena geometry, **independent of $\tau_{V5},\ell_{V5}$**. So the plateau budget, the monogamy budget, and the Page-curve budget are **not three free numbers** — they are one inherited scale seen through three fixed geometric windows.

**R2, stated:** anchor the V5 budget in *any one* arena — the monogamy bound $W_{V5}$ (an entanglement-sharing measurement), or $B_{\mathrm{ent,max}}^{V5}$ (the Page time $t_{\mathrm{Page}}\approx0.54\,\tau_{BH}$), or $B_{\mathrm{cross,max}}$ (the plateau height) — and the other two are constrained up to the forced O(1) ratios. The *existence* of the fixed ratios is forced; the *numerical* ratios are O(1)-on-inherited-shape (they need $f_{\rm ent},\rho_{\rm loc},g_\partial$ from the envelope shape, which is inherited — the open "domain-correlation" shape).

## 6. Tiers

| Claim | Tier |
|---|---|
| Finite $W_{\max}=\int F_{V5}$ exists | **form-forced** (090 §4.1–4.2 + P04) |
| Three arena budgets = projections of $W_{\max}$ | **structural** (geometric reading of 050/058/065 against 090; 050 already calls them "related but distinct") |
| Projection *values* $f_{\rm ent},\rho_{\rm loc},g_\partial$ | **O(1), inherited-shape** (need the uncharacterized envelope shape) |
| R1 universal-in-complexity onset (band in proxy) | **derived-conditional** on §3 + varying proxy conversion; is 058 §5.2 re-grounded |
| R2 fixed inter-arena ratios exist | **forced** (scale cancels); values O(1)-inherited-shape |
| Absolute $\Gamma_{\mathrm{plateau}}$, $W_{\max}$, $t_{\mathrm{Page}}$ | **inherited** (V5 substrate constant; not derived — do not chase) |

## 7. Falsifiers

- **F-R2 (the strong one):** infer the V5 budget in two of {monogamy, Page curve, Class-C plateau} and find their ratio inconsistent with a single $W_{\max}$ at fixed O(1) — that falsifies the single-envelope consolidation (§3), i.e. the claim that one V5 kernel underlies all three.
- **F-R1:** two pure-Class-C architectures plateau at substantially different correlation-content after their own redundancy$\to$coverage conversion — the onset is not universal in the substrate variable (also 058 §6.3).
- **F-form:** error suppression continues to zero at arbitrarily high redundancy with no plateau (058 §6.1) — no finite envelope.

## 8. What this buys weapon #4

Before: "logical error floors at $\Gamma_{\mathrm{plateau}}>0$" with an unpinned height — soft, killable only by the clean "goes to zero forever" outcome. After: the plateau is (i) **universal in complexity** (a band in code distance, a point in $N_{V5}$-content — R1), and (ii) **ratio-locked to monogamy and the Page curve** through one inherited V5 budget (R2). The absolute height stays inherited, per ED's constants doctrine; the *relations* are forced, and they are what a referee can hit. Weapon #4 becomes: *a floor whose height ratio to two other V5 observables is fixed, and whose onset is a fixed point in internal complexity.*

**Straddling-edge pin (2026-07-14, partial — DONE).** The entanglement/boundary factor $f_{\rm ent}g_\partial$ is now *measured*, not free. The straddling-edge count (entanglement-carrying V5 edges crossing a boundary at $\ell_{V5}\sim\ell_P$) is $\approx 0.88$ per Planck cell (`evaluation/AreaLaw_Arc/edge_density_coefficient.py`, `Paper_HorizonTilingThreeCounts`), converging with the frozen-state (0.78) and holographic (1) counts on ~1 bit/Planck-cell (Paper_039 §3.5 for the V5 entanglement straddles). So $B_{\mathrm{ent,max}}$ is anchored to the Bekenstein–Hawking tiling ($f_{\rm ent}g_\partial \approx 0.88$ in substrate units), and **R2's Page-curve / monogamy side is pinned to the area law**.

**Not closed:** $\rho_{\rm loc}$ (the Class-C *bulk* per-locus factor) is not reached by a *boundary-crossing* count; and $0.88$ is the *substrate-scale* value ($\ell_{V5}\sim\ell_P$), while the plateau lives coarse-grained ($\ell_{V5}$ DCGT-renormalized). Net: R2's free O(1)'s drop from three to ~two — the entanglement side pinned, the plateau-bulk side open.

**$\rho_{\rm loc}=1$ (2026-07-14, DONE — pencil, not a probe).** The Class-C factor turned out to be a *structural identity*, not a bulk measurement: $W_{V5}$ (065, per-chain $\int K_{V5}$ over partners) and $B_{\mathrm{cross,max}}$ (058, per-locus cross-chain content) are the *same* $\int K_{V5}=W_{\max}$ — one budget spent two ways (entanglement partners vs redundant-encoding channels), identical at the P08 grain. So $\rho_{\rm loc}=1$ and the monogamy bound *equals* the plateau budget. Combined with §8's $f_{\rm ent}g_\partial\approx0.88$, **R2 is fully pinned: $W_{V5}:B_{\mathrm{cross,max}}:B_{\mathrm{ent,max}}=1:1:0.88$.**

**Canonicalized** as a corpus paper: `ED Generative/physics-papers/substrate-evaluation/Paper_V5UnifiedBudget.md` (report-referenced results need an EDG-repo paper). This note is the working derivation behind it.
