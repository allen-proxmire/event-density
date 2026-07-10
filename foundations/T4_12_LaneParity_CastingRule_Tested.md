# T4 · Step 12 — Running AP's Lane-Parity Rule for the Chirality Casting: the Arithmetic Is Exactly True, It Correctly Singles Out the Chiral Force, but the Even/Odd *Generalization* Does Not Survive — the Real Invariant Is "N=2 Is Special," and the Chiral/Vector *Bridge* Is Still Asserted, Not Derived

**Foundations — T4 step 12. Tests AP's highway-lane rule (`RepSpectrum_Program_Scope_*` step 3) as the candidate mechanism for the chirality casting wall (`T4_11`): does "odd N → vector, even N → chiral" hold as a real rule about the channel multiplicity? Crank-rail ON — held to the same bar as a positive. Result: the arithmetic core is exactly true and it correctly flags the one chiral non-abelian force, but the even/odd *generalization* is not supported (the genuine invariant is "N=2 special," not parity-of-N), the abelian sector needs a separate treatment, and the step from "no middle lane" to "chiral" is asserted rather than derived. Net: PROMOTE the metaphor to the leading casting candidate for *why N=2 is the chiral one*; DEMOTE the general N-rule; name the one real open piece (the bridge).**

## 1. The arithmetic core — exactly true
Lay the `N` channels in a row and let the spatial reflection reverse the row: `σ: i ↦ N+1−i` on `{1,…,N}`. A fixed lane needs `i = N+1−i`, i.e. `i = (N+1)/2` — an integer **iff `N` is odd**. So:

> **The order-reversing involution on `N` lanes has a fixed (self-mirror) central lane iff `N` is odd; it is fixed-point-free iff `N` is even.**

This is just arithmetic, and it is exactly AP's picture: 1 lane and the middle of 3 lanes are *their own mirror image* (a fixed lane); 2 lanes have *no* fixed lane (they swap). Solid, no wobble.

## 2. The bridge to chiral/vector — the asserted step (flag it now)
The metaphor then asserts a *physics* bridge:
- **odd `N` (a fixed central lane):** the fixed lane is parity-invariant → it anchors the coupling symmetrically in the two `γ⁵` eigenspaces → **vector**;
- **even `N` (no fixed lane):** the reflection pairs lanes with no anchor, so the arrangement itself carries an intrinsic `ℤ₂` = a handedness that can lock to `γ⁵ = arrow × orientation` → **chiral-capable**.

**This bridge is asserted, not derived.** "No fixed lane" gives an intrinsic `ℤ₂`; it does not by itself *force* the coupling to be chiral (it *permits* it). Keep this flagged — it is the one genuinely open piece (§5).

## 3. Test against the Standard Model
| force | ED lane-count `N` | rule predicts | nature | hit? |
|---|---|---|---|---|
| U(1)_em | 1 | vector | vector | ✓ |
| SU(2)_weak | 2 | chiral | chiral | ✓ |
| SU(3)_strong | 3 | vector | vector | ✓ |
| **U(1)_Y hypercharge** | **"1"** | **vector** | **CHIRAL** | **✗** |

The first three land. **The fourth breaks the naive rule:** hypercharge is chiral (left and right fermions carry different `Y`), yet it is abelian ("1 lane") and the rule says vector. Two honest readings:
- **Principled exclusion:** in ED, `U(1)_Y` is *not* a channel-multiplicity at all — it is the single **global P09 phase** (Gauge_11), not a lane count. Its chirality (which handedness gets which `Y`) is itself part of the casting, not a lane fact. Excluding it is defensible — but then the lane rule governs only the **non-abelian multiplicity**, which is **two data points** (N=2 chiral, N=3 vector), not three.
- **Or the rule is simply silent on the abelian sector** and must be paired with a separate hypercharge-casting sub-problem.

Either way, the abelian sector is not a clean win; it is out-of-scope or a miss.

## 4. Does the even/odd generalization survive past N=3? — NO
The rule predicts N=4 chiral, N=5 vector, etc. There is no SM data past N=3, so test it against the one real group-theory landmark:

- The genuine mathematical distinction among `SU(N)` fundamentals is **N=2 pseudoreal (quaternionic) vs N≥3 complex** — it singles out **N=2**, and does **not** track even/odd (N=4 is complex, like N=3, *not* like N=2). So the deep reason N=2 is the special/chiral-natural case is its **pseudoreality**, which is an "N=2 is unique" fact, not a "parity of N" fact.
- Therefore the metaphor's success is really **"N=2 is the distinguished chiral case"** (which it captures — N=2 is the unique smallest no-middle arrangement), while its *even/odd extrapolation* (N=4 chiral) has **no support** and most likely fails.

Honest correction to my own earlier framing (scope note said "in tension with group theory"): **group theory is not in tension — it is silent/permissive.** Vector-vs-chiral for *every* `SU(N)` is a contingent **matter-content choice** (SU(3)'s fundamental is complex, so QCD *could* have been chiral; nature made it vector by putting both quark handednesses in the **3**). No group rule derives the SM's vector/chiral pattern. So the lane rule is not contradicted by group theory — it is *attempting to derive what the SM stipulates*, which is exactly the right ambition. The real limit is that the invariant it should be tracking is "N=2 special," not "even N."

## 5. What the run establishes
**PROMOTE (the kernel that survives):** For the *non-abelian* sector, the lane picture gives a clean, exactly-true, ED-native handle on **why N=2 is the chiral force** — the fixed-point-free reflection is the channel-side shadow of the doublet's specialness, expressed in ED's own terms (the spatial reflection acting on the physical channel set), *without* importing pseudoreality as a postulate. As the candidate answer to "which channel-count is chiral," it correctly picks **N=2**, and it does so structurally where the SM has only a contingent choice. That is real, and it keeps the lane rule as the **leading casting candidate for N=2**.

**DEMOTE (the overreach, railed):**
- the **even/odd general N-rule** is not robust — the true invariant is "N=2 special" (pseudoreal), not parity-of-N; drop the N≥4 extrapolation until something motivates it;
- the **abelian sector** is not covered (hypercharge is chiral); handle it separately via the global-phase casting;
- the **chiral/vector bridge** (§2: "no middle lane ⟹ chiral," not just "⟹ can be chiral") is **asserted, not derived** — this is the one genuinely open mechanism.

## 6. Net verdict and the sharp next sub-problem
Running #1 did its job: it **hardened** AP's idea where it is strong (N=2 is structurally the chiral case, in ED-native terms) and **broke** it where it overreached (even/odd past N=3; the abelian miss), and it corrected a framing error of mine (no group-theory "tension" — group theory is permissive; the SM pattern is contingent content the lane rule is trying to *derive*).

The wall is now even sharper than `T4_11` left it. It is **one** thing:

> **The bridge: show that a fixed-point-free reflection on the channel set (N=2) *forces* a chiral coupling to `γ⁵ = arrow × orientation`, while a reflection with a fixed central lane (odd N) *forces* vector — deriving the step §2 currently only asserts.**

That is the concrete next sub-problem, and it is now well-posed: it is a question about how the coupling built from `γ⁵`'s orientation factor acts on a lane-set with vs without a self-mirror lane. No shortcut around it survives, but it is a single, sharp, decidable target rather than the diffuse "why is anything chiral." Crank-rail: ran the test, kept the true kernel, dropped the coincidental generalization, reported the abelian miss and the asserted bridge straight, and fixed my own overstated "tension" claim.
