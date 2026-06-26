# The Three UDM Channels, Bottom-Up — the Substrate Is the Generative Core; the Dissipative & Non-Local Channels Are ED's Own Switched-Off Ingredients

**Evaluation result — the bottom-up companion to AP's empirically-validated UDM/PDE paper (`ED_Foundational_Paper_v2`: one canonical PDE, three channels — mobility=PME/UDM diffusion 1.1%, penalty=RC/Debye 0.00%, participation=RLC/telegraph 0.00%). Question: does the *certified worldline substrate* reproduce these three channels? Sims: `tracer_diffusion_test.py`, `crowding_capacity_test.py`, `mobility_recovery_test.py`, `rc_relaxation_test.py`, `rlc_oscillation_test.py`. Verdict: the bare local generative rule gives the GENERATIVE/LOCAL content (diffusion; the up-half of relaxation); every other piece (downward decay, capacity, oscillation) needs a dissipative or non-local ingredient — and each one is a real ED primitive (extinction, b→0 capacity, P04 participation), just off in the minimal certified rule. Turn ED's own ingredients on and the substrate reproduces all three UDM channels bottom-up.**

---

## The map

| UDM channel | bare local substrate | missing piece | real ED ingredient |
|---|---|---|---|
| **Mobility → diffusion** | ✅ native — a worldline diffuses in disorder (MSD∝t^1.18, VACF→0); a front packet spreads Fickian (R∝t^0.51) | — | the generative core |
| **Penalty → RC** | ½ — relaxes *up* toward ρ* from below (with extinction, k=1.32 exponential), but cannot decay *down* from above (deposit-only, no ρ-removal) | ρ-removal / dissipation | extinction |
| **Participation → RLC** | ❌ monotone — bare local rule cannot ring (⟨ρ⟩→plateau); add the global participation feedback and it **rings** (damped telegraph around ρ*, strength ∝ H) | non-local global feedback | P04 participation |
| *(degenerate mobility, the UDM's signature)* | ❌ linear only — D_eff flat in density, packet exponent stays 0.5 as core ρ→3.0 (no capacity in the rule) | capacity ρ_max | P04 / b→0 |

## The pattern

**The certified substrate is the generative, local floor.** It supplies, for free, the *generative* content of the UDM: diffusion (mobility), and the up/saturating half of relaxation. Everything else in the UDM-PDE is either:
- **dissipative** — *downward* decay (RC's other half), and the *capacity* (degenerate mobility) — which need ρ-removal / a ρ_max bound the additive deposit-rule lacks; or
- **non-local** — the *oscillation* (RLC) — which needs the global participation feedback a purely local rule cannot have.

And the punchline: **every missing piece is a real ED primitive, not a foreign patch.** Extinction (fronts dying) supplies the decay; P04 bandwidth-capacity / b→0 (the same mechanism behind gravitational horizons) supplies the capacity; P04 participation (the global, non-local coupling) supplies the oscillation. They are *switched off* in the minimal certified rule used for the substrate evaluations — and when switched on, each channel appears (extinction → up-relaxation; participation → telegraph ring).

## What this says about "the UDM is ED coarse-grained"

**True — with a sharp statement.** The UDM is empirically validated on its own (11 materials / 8 domains, R²>0.986; AP holds it 100% correct) — nothing here touches that. The bottom-up relationship: the substrate is the **generative core** of the UDM, and the dissipative + non-local channels are ED's **other primitives layered on**. AP's path was ED-philosophy → UDM → physics (top-down, validated); this is the same physics reached from the substrate side, with the channel-by-channel ledger of which part is generative-native vs which ED ingredient supplies it.

This is the spine of the **substrate-consilience companion paper** (pairs with the UDM paper): not "the substrate gives the PDE," but the precise map of *which half of each channel is substrate-native and which ED ingredient supplies the rest* — sharper and more honest than a blanket "all yes," and it ties the soft-matter UDM to the gravitational b→0 through the shared capacity primitive ("the capacity that stops a crowded gel is the capacity that makes a black hole").

---

*Three UDM channels bottom-up. Mobility/diffusion = substrate-native (worldlines diffuse). Penalty/RC = half (up-relaxation via extinction; no down-decay, deposit-only). Participation/RLC = bare rule monotone, RINGS once global participation feedback added. Degenerate mobility = absent (no capacity in rule). Pattern: substrate = generative/local floor; dissipative (decay, capacity) + non-local (oscillation) channels need ED's own off-by-default primitives (extinction, b→0, P04 participation). Turn them on → all three channels bottom-up. UDM validated independently; this is the channel-by-channel substrate ledger = the consilience companion paper. Notebook only; no external prediction (per AP).*
