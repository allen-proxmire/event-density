# Arc: Quadratic Strain and the Newton-MOND Unification (Scoping)

**Opened 2026-07-07** at AP's direction (from the P14 partial-reduction result; see memory `project_p14_partial_reduction`). Working scoping doc; crank-rail ON (this is the MOND-arc over-read trap zone). Read/analyze only, no build until the structural read (Steps 1-4) is complete.

**Goal.** Determine whether ED's gravitational strain can be recast as a quadratic-in-amplitude functional whose **diagonal reproduces Newton** and whose **off-diagonal reproduces the MOND transition**, thereby reducing P14 (geometric-mean bilocal coupling) to the interference modulus of superposed source-amplitudes.

**The candidate recast, stated minimally.** Replace the current per-channel strain (a sum of source *bandwidths*, Paper_026, linear) with a modulus of a sum of source *amplitudes* (quadratic):
$$\text{current (linear): } \; \mathrm{Str}_K = \sum_a b_K^{(a)} \qquad\longrightarrow\qquad \text{recast (quadratic): } \; \mathrm{Str}_K = \Big|\sum_a \sqrt{b_K^{(a)}}\,e^{i\pi_K^{(a)}}\Big|^2 = \sum_a b_K^{(a)} + \sum_{a\neq b} \sqrt{b_K^{(a)} b_K^{(b)}}\,\cos\Delta\pi_{ab}.$$
Diagonal ($a=b$) = the additive Newtonian potentials (unchanged from Paper_026). Off-diagonal ($a\neq b$) = the source-source interference = the geometric-mean cross-term = P14 / MOND. The whole recast is one sentence: *source contributions to a channel superpose as amplitudes, not as bandwidths* (exactly the double-slit move).

---

## Step 1 (DONE) — the current gravity foundation is linear, but only in a strong-field sense

- **Paper_026: `Str` is linear-in-source, and it is an admitted CHOICE.** `Str` is read as the potential $\Phi$ under **P-Potential-Reading**, flagged in §2/§3.4 as a substrate-level *choice* (Model A potential vs Model B modulation). Per-channel $\Phi_{ch}\propto \sigma_{ch}/R$, holographic resolution $\sigma_{ch}=\sigma(M)/N(R)$, $N(R)$ cancels, $\Phi=-GM/R$, linear in $M$ (two sources $\Rightarrow \Phi_1+\Phi_2$, additive). **This is exactly the diagonal reading.** Because the reading is already postulated and non-unique, a quadratic "Model C" is admissible in principle, not a foundation-violation.
- **GR-I linearities, and where each is load-bearing:** (i) $\nabla^2 b\sim\rho$ (Newtonian Poisson, inherited) $\to$ $b$ linear in source; vacuum $b=1-r_s/r$. (ii) $\Gamma\propto b$ (P-Commitment-Linear) $\to$ Einstein branch $N^2\sim b$ (separate linearity, rate-vs-bandwidth). (iii) $g\sim1/b$, $N^2\sim b$, factor-of-two all from one field $b$; and $b\sim1+2\Phi$, so a quadratic $\Phi$ feeds an interference piece into $b$.
- **No HARD constraint forbids quadratic strain.** GR-I operates only in the static, weak-field, **strong-gradient** (solar) regime, inherits $\nabla^2 b\sim\rho$ rather than proving $b$ linear at all scales, and its own §7 defers the khronon$\leftrightarrow$MOND (galactic) reconciliation as OPEN. MOND is itself a modified Poisson (AQUAL), so an off-diagonal that modifies $\nabla^2 b$ at low acceleration is not a contradiction.
- **The one DECISIVE constraint:** the off-diagonal MUST vanish in the strong-field/solar regime so $b$ reverts to linear-Poisson and GR-I's factor-of-two + Schwarzschild relation + solar tests survive exactly. Make-or-break; see Step 2 crux.

## Step 2 (DONE) — is gravitational strain expressible as a bilinear amplitude operator without violating P04/P05/P11/GR-I? Verdict: STRUCTURALLY ADMISSIBLE, with three items to nail.

**Honest self-correction (walks back an earlier loose claim).** FSC-3 §5's operator $O_{V1,2}(x,y)=V1(x-y)[P^*(x)P(y)+\text{h.c.}]$ is a *matter-field propagator/kinetic* structure (ONE field, two loci, explicit $V1$ line; renormalizes the mass/kinetic terms in the failed $\alpha$-flow). It is **NOT** the gravitational two-source strain bilinear. It is **genus-precedent** (amplitude bilinears $P^*P$ are legitimate substrate operators) **not the species** (the gravitational object). The gravitational bilinear I need is $P^{(a)*}P^{(b)}$ between two *already-$V1$-propagated source-contributions* superposed at the test chain, where $b_K^{(a)}$ is the potential-as-bandwidth. Do not conflate them (I did, loosely, in the P14 steps 2-3).

**The R-power check (a real potential showstopper, and it passes).** Worry: if strain $=|P|^2$ with $P\propto V1$-Green $\propto1/R$, the diagonal would be $|V1|^2\propto1/R^2$ (force, not potential) $\ne$ Newton. Resolution: in ED (Paper_030 §4.2, Paper_001) the per-channel **bandwidth** $b_K$ IS the potential ($b_K^{loc}\propto GM/R$, $b_K^{hor}\propto a_0 R$), and the amplitude is $P_K=\sqrt{b_K}$. So $|P_K|^2=b_K=$ potential (diagonal $=$ Newton $\checkmark$, correct $1/R$ power) and $\sqrt{b_{loc}b_{hor}}=\sqrt{GM a_0}$ ($R$-independent $\to$ log $\to$ $\sqrt{a_N a_0}$, off-diagonal $=$ MOND $\checkmark$). Confirmed against Paper_030's own §4.2 conventions. The recast reproduces Newton exactly (it IS Paper_026 on the diagonal) and only ADDS the off-diagonal.

**Primitive-by-primitive admissibility:**
- **P04 (non-negative additive scalar):** total $b_K=|\sum_a P^{(a)}|^2\ge0$ $\checkmark$. Additivity is ACROSS distinct channels ($b_{tot}=\sum_K b_K$), which the recast preserves; the interference is WITHIN a channel (across source-contributions), which P04's across-channel additivity does not forbid. BUT this **commits** the flagged-open "additivity vs sublinearity" question (participation_bandwidth concept §2/§7) to sublinear/interference within-channel. A named structural commitment, not a clean violation.
- **P05 (polarity-transport):** the off-diagonal carries $\Delta\pi_{ab}=\pi^{(b)}-\pi^{(a)}$. Bare $\Delta\pi$ is gauge-COVARIANT; the physical, gauge-INVARIANT object is the **P05-holonomy-corrected** phase difference ($\Delta\pi - \oint A$, Aharonov-Bohm/Berry style, matching Paper_090 §4.3's $e^{i(\alpha_A-\alpha_B)}$ gauge law). Not violated; REQUIRES the holonomy formulation, and its modulus $\sqrt{b_a b_b}$ (P14's phase-free form) is gauge-invariant on its own.
- **P11 (arrow/commitment):** NOT violated. Stronger: **P11 is the candidate MECHANISM for the decoherence the arc needs** (see crux). Interference is a coherent, pre-commitment effect; commitment collapses it.
- **GR-I:** preserved AS THE DIAGONAL / strong-field limit, CONDITIONAL on the decoherence mechanism killing the off-diagonal at strong field.

**THE CRUX (candidate, NOT a result, crank-rail flag):** the Newton$\leftrightarrow$MOND transition as a **commitment-driven decoherence transition**. Strong gradient $\Rightarrow$ dense commitment (P11) $\Rightarrow$ decoherence $\Rightarrow$ off-diagonal vanishes $\Rightarrow$ Newton/GR-I. Weak gradient $\Rightarrow$ sparse commitment $\Rightarrow$ coherence preserved $\Rightarrow$ off-diagonal survives $\Rightarrow$ MOND. **Seductive extra:** the transition scale would be where the local commitment rate drops below the cosmic/horizon rate $a_0=cH_0/2\pi$ (a RATE) $\Rightarrow$ deep-MOND exactly when $a<a_0$. This uses only existing ED machinery (GR-IV sparse becoming, commitment$=$decoherence, $a_0$-as-rate, RelationalTick Zeno) and would simultaneously (a) preserve GR-I at strong field and (b) explain the $a_0$ scale. **It is exactly the kind of "everything clicks" the MOND arc has burned us on. Hold as CANDIDATE. Step 3/4 must derive or kill it, quantitatively (does the decoherence rate cross threshold at $a_0$?).**

**Step-2 verdict:** the quadratic recast is structurally admissible (no hard P04/P05/P11/GR-I violation). Three things must be nailed before it is viable: (1) formulate the phase as a P05-holonomy (gauge-invariance); (2) name/own the within-channel interference commitment (resolves P04 additivity-vs-sublinearity); (3) **the decoherence mechanism** that recovers GR-I at strong field and sets the transition at $a_0$ — the make-or-break.

---

## Step 3 (DONE) — explicit construction reproduces Newton + MOND + BTFR and IMPROVES on Paper_030; viability now rests entirely on the decoherence mechanism

**3.1 The form.** Test chain at $x_c$; per-channel amplitude from source $a$ is $P_K^{(a)}=\sqrt{b_K^{(a)}}\,e^{i\pi_K^{(a)}}$ ($b_K^{(a)}$ = per-channel potential-as-bandwidth, $\pi$ = P05-transported polarity). Single-carrier channels force superposition $P_K=\sum_a P_K^{(a)}$, so
$$\mathrm{Str}_K=|P_K|^2=\sum_a b_K^{(a)}+2\sum_{a<b}\sqrt{b_K^{(a)}b_K^{(b)}}\,\cos\Theta_{ab},\quad \Theta_{ab}=\text{P05-holonomy-corrected }(\pi^{(b)}-\pi^{(a)}).$$
Total $\Phi=\sum_K\mathrm{Str}_K$ (across-channel additivity + Paper_026 holographic resolution on the diagonal).

**3.2 Diagonal = Newton (exactly Paper_026).** Local self-term $\sum_K b_K^{(L)}=-GM/R$ (Paper_026 verbatim), $a_N=GM/R^2$. Reproduced exactly; the recast IS Paper_026 on the diagonal.

**3.3 Off-diagonal = MOND, geometric mean now FORCED.** $\Phi_{cross}=2\cos\Theta_{LH}\sum_K\sqrt{b_K^{(L)}b_K^{(H)}}$. With $b^{(L)}\propto GM/R$, $b^{(H)}\propto a_0 R$ (Paper_030 §4.2), per-channel $\sqrt{b^{(L)}b^{(H)}}\propto\sqrt{GMa_0}$ ($R$-indep), bilocal density $\propto1/R$, so $\Phi_{cross}=2\cos\Theta_{LH}\sqrt{GMa_0}\,\log(R/R_0)$; gradient $=\cos\Theta_{LH}\sqrt{a_Na_0}$. Identical to Paper_030's ECR **when $\cos\Theta_{LH}\approx1$**, but the geometric mean is the interference modulus (forced by single-carrier channels), not a postulate.

**3.4 BTFR slope-4 (unchanged).** Deep-MOND $a=\sqrt{a_Na_0}=\sqrt{GMa_0}/R$; circular orbit $a=v^2/R\Rightarrow v^4=GMa_0\propto M$, slope 4, zero scatter ($a_0,G$ universal). Same as Paper_031; the recast only re-grounds the $\sqrt{a_Na_0}$ it rests on.

**Three structural WINS over Paper_030 (real):**
1. Geometric mean **forced** (interference modulus), not postulated (§8.9 non-uniqueness dissolved).
2. The $\cos\Theta_{LH}$ coherence factor **replaces Paper_030's hand-imposed "joint weak-gradient regime assumption"** (§5.3): the cross-term is present when coherent, absent when decohered, automatically. One fewer postulate.
3. **The horizon contributes ONLY via the off-diagonal (interference/dipole), not a diagonal monopole.** By shell-theorem/Birkhoff the isotropic cosmic horizon exerts no net monopole force; $a_0$ is Paper_029's DIPOLE (anisotropy from the chain's own acceleration) = inherently an interference effect. This DISSOLVES the "diagonal $a_0R$ dominates the cross-term in deep-MOND" problem that forced Paper_030's regime assumption. **CAVEAT:** requires re-examining Paper_030 §3.2's $\Sigma_0=-a_0R$ (real diagonal term, or already the dipole/interference double-counted?) — Step-4 item.

**3.5 The decoherence mechanism (make-or-break) — CANDIDATE, not derived.** The arc rests on $\cos\Theta_{LH}$ going $1\to0$ as local acceleration rises through $\sim a_0$. Two grounded candidate sub-mechanisms:
- **(A) Commitment-rate decoherence (P11/GR-IV).** Commitment randomizes unselected-channel phase (P11). Dense commitment (high $a$) randomizes $\Theta_{LH}$ before interference builds $\Rightarrow\cos\Theta_{LH}\to0\Rightarrow$ Newton; sparse (low $a$) $\Rightarrow$ coherence survives $\Rightarrow$ MOND. Ties to GR-IV sparse-becoming + RelationalTick Zeno.
- **(B) Rindler-cosmic horizon crossing (Paper_029 geometry).** Accelerating chain has a Rindler horizon at $c^2/a$. When $a\gtrsim cH_0$ it falls inside the cosmic horizon $R_H=c/H_0$ $\Rightarrow$ chain decouples from the cosmic horizon $\Rightarrow$ L-H coherence cut $\Rightarrow$ Newton; $a\lesssim cH_0\Rightarrow$ MOND. Crossing at $a\sim cH_0=2\pi a_0$ — the SAME horizon geometry Paper_029 used to derive $a_0$.

**Honest accounting of the mechanism:**
- DELIVERS (if it holds): the transition MECHANISM (off-diagonal off at strong field $\Rightarrow$ GR-I recovered; on at weak field $\Rightarrow$ MOND), replacing Paper_030's regime-assumption postulate.
- INHERITS (does NOT predict): the transition SCALE $a_0=cH_0/2\pi$ from Paper_029's cosmic-horizon geometry (value-inherited via $H_0$). Explains why the transition is AT $a_0$; does not independently predict $a_0$ (nor should it).
- STILL OPEN: (i) do (A) and (B) coincide, or is one correct? **Do NOT assert they are the same.** (ii) transition at $a_0$ or $2\pi a_0$? (O(1)/$2\pi$, within existing $a_0$ ~10% / O(1)-normalization band, but must be pinned). (iii) does a coherent L-H bilocal channel with a definite $\Theta_{LH}$ physically exist? (Paper_030 §4.1 gives bilocal-channel EXISTENCE from P03+P07; the COHERENCE is the new physics and is unshown).

**Step-3 verdict:** construction succeeds and is a genuine structural improvement on Paper_030 (geometric mean forced; regime-assumption eliminated; horizon-via-interference dissolves the $a_0$-dominance problem). Newton, MOND, BTFR all reproduce. **Viability now rests entirely on the decoherence mechanism** — two grounded-but-underived candidate sub-mechanisms with a compelling but scale-INHERITED (not predictive) tie to Paper_029's $a_0$-geometry. Step-4 target.

---

## Step 4 (DONE) — adversarial pass: recast SURVIVES and SIMPLIFIES; the Step-3 decoherence mechanism was UNNECESSARY over-engineering

Read Paper_029 ($a_0$ derivation) to close the checks. The recast comes out CLEANER than Step 3, and I killed my own speculative mechanism (crank-rail working).

**Check 2 ($\Sigma_0$ double-count) — CONFIRMED favorable, decisively.** Paper_029 §5.1: the horizon's effect is a DIPOLE, $\rho_{cosmic}\propto(|\vec a|/c)\cos\theta$ — anisotropic, proportional to the chain's OWN acceleration, existing ONLY for an accelerating chain (§3.3). NOT an isotropic monopole. So Paper_030 §3.2's $\Sigma_0=-a_0R$ (integrating $a_0$ as a "constant isotropic acceleration") mis-treats a dipole as a monopole — a latent inconsistency. **Removing $\Sigma_0$ (horizon contributes only the anisotropic/interference term) is justified and FIXES Paper_030.**

**The Step-3.5 decoherence mechanism is UNNECESSARY (self-correction).** Once $\Sigma_0$ is removed, $\Phi=\Phi_N+\Phi_{cross}\Rightarrow a=a_N+\sqrt{a_Na_0}$. The transition is then a pure RATIO effect: $\sqrt{a_Na_0}$ naturally dominates below $a_0$ (deep-MOND) and is negligible above (Newton); at solar scale $\sqrt{a_Na_0}/a_N\sim\sqrt{a_0/a_N}\sim10^{-4}$, so GR-I/Newton is recovered approximately (the same small residual standard MOND carries). **No $\cos\Theta$ decoherence dynamics, no Rindler/Unruh story, no regime assumption needed.** The elaborate Step-3.5 make-or-break was over-engineering, solving a problem (transition + GR-I recovery) the ratio structure solves automatically once $\Sigma_0$ is gone. Dropped the elegant-but-unneeded mechanism.

**Checks 4 & 7 dissolve with the decoherence mechanism** (they were about it). For the record: Paper_029's $2\pi$ is the azimuthal-Fourier/$SO(2)$ dipole factor (the interference IS the dipole projection, so shares the $2\pi$; no $2\pi a_0$ problem); and Paper_029 §3.2 already has horizon content COHERENT within $R_H$.

**Checks 1, 5, 6:** GR-I recovered approximately by ratio (1 $\checkmark$); within-channel interference is QM-standard (Born rule), low risk (5 $\checkmark$); no V1 conflict, and Paper_029 §7.3 notes the dipole is "V5-like," consistent (6 $\checkmark$).

**Remaining residual (minor, named):** the SIGN of the interference — why constructive ($\cos\Theta_{LH}\approx+1$, gravity-enhancing) not destructive? Same "attractive coherence" question as V5/RelationalTick; plausibly P12 Coh rewarding alignment; not fully derived. Named, not hidden.

**Step-4 verdict:** the recast SURVIVES adversarial pressure and comes out SIMPLER. Two SOLID results, each discharging a Paper_030 postulate:
1. **Geometric mean FORCED** (interference modulus) — P14's functional-form postulate discharged.
2. **$\Sigma_0$ removed** (horizon is a dipole, not a monopole; Paper_029-justified) — Paper_030's "joint weak-gradient regime assumption" postulate discharged AND a latent inconsistency fixed.
Net: Newton + MOND + BTFR reproduced with TWO fewer postulates than Paper_030. Inherited caveats unchanged ($a_0$ scale ~10%/O(1); specific $\mu$-profile is one choice; small solar-scale MOND residual = same as standard MOND). One residual: the constructive-interference sign.

## Step 5 (verdict + deliverable)

**VERDICT: VIABLE** — for the two solid results. The recast is real and improves on Paper_030 (two postulates discharged, one inconsistency fixed), NOT via a new decoherence mechanism (that was dropped) but via the plain ratio structure once $\Sigma_0$ is correctly removed.

**Deliverable — standalone paper, scoped honestly.** Title candidate: *"Quadratic Strain: Newton as Diagonal, MOND as Off-Diagonal, and the Discharge of Two MOND-Line Postulates."* Claims to make:
- Gravitational strain as $\mathrm{Str}_K=|\sum_a P_K^{(a)}|^2$: diagonal = Newton (Paper_026 verbatim), off-diagonal = the forced geometric-mean interference = MOND.
- Discharges P14's geometric-mean postulate (it is the interference modulus, forced by single-carrier channels).
- Discharges Paper_030's regime-assumption postulate (removing $\Sigma_0$, justified by Paper_029's dipole; the transition is then automatic by ratio).
- Reproduces Newton, MOND $\sqrt{a_Na_0}$, BTFR slope-4.
- Does NOT claim: the interference sign (residual), a new transition mechanism (it's ratio), $a_0$ derivation (inherited), or a specific $\mu$-function beyond the ratio profile.
- Preamble must state: this recasts P12's strain reading from linear (Paper_026 Model A) to quadratic ("Model C"); commits within-channel composition to interference (resolving the participation_bandwidth additivity-vs-sublinearity open question); tier = STRUCTURAL (conditional on the quadratic strain reading, which is a substrate-level choice like P-Potential-Reading).

**Honest bottom line:** the "Newton-MOND unification" is real but modest and clean — it is *"MOND is the interference cross-term of the same strain whose diagonal is Newton,"* achieved by fixing Paper_030's monopole/dipole error and forcing the geometric mean. The grand decoherence-drives-the-transition story did not survive (and wasn't needed). Bank the two postulate-discharges; flag the sign as the one residual.

**Live risks:** (i) the decoherence mechanism is the whole arc and is currently a narrative; (ii) does a coherent local-horizon bilocal channel with definite $\Delta\pi$ actually exist (Paper_030 §4.1 asserts bilocal-channel existence from P03+P07; the COHERENCE is new physics); (iii) MOND-arc over-read history $\Rightarrow$ no elegance banked without an adversarial pass.
