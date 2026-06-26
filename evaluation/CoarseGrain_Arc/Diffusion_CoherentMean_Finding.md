# #3 Re-check — The Ensemble-Mean Density Obeys Transport/Eikonal, Not Diffusion (a clean continuum law, the "wrong" object)

**Evaluation result — the swing-vote re-check from the #2/#5c decomposition arc. Sim: `evaluation/CoarseGrain_Arc/diffusion_coherent_decomp.py`. After #2 flipped (coherent field = Maxwell + entropy) and #5c did not (no Gaussian signal), tests whether #3 flips: does the *ensemble-mean* density (the coherent/signal part, averaging out the ballistic-worldline disorder) obey the diffusion PDE? Result: **no flip to diffusion — but a clean continuum law does emerge, and it is transport/eikonal, not diffusion.** Ensemble-averaging cleaned the dynamics dramatically (step IC: regression R² 0.10 single → 0.60 mean), revealing a coherent continuum law — but eikonal/transport (|∇ρ|, R²=0.597) beats diffusion (∇²ρ, R²=0.258) decisively. So **ED's coarse-grained density continuum is ballistic transport, not diffusion** — the diffusion PDE was the wrong target. Confirms the CoarseGrain arc's kinetic-lattice-gas finding at the ensemble-mean level.**

---

## Result (regression R² of d_t⟨ρ⟩ on the PDE library)

| IC | model | single R² | **mean R²** |
|---|---|---|---|
| step | diffusion | 0.001 | 0.258 |
| step | **eikonal/transport** | 0.094 | **0.597** |
| step | diff+eik | 0.095 | 0.606 |
| gaussian | eikonal | 0.065 | 0.093 |
| ring | eikonal | 0.057 | 0.061 |

- **Averaging reveals a clean law (the method works):** the step IC's R² jumps 0.10 → 0.60 under ensemble-averaging — a coherent continuum equation emerges from the per-realization disorder, exactly as the coherent/signal idea predicts.
- **But the law is eikonal/transport, not diffusion:** eikonal R² (0.60) beats diffusion (0.26) decisively. The mean spreads *ballistically* (∝ t), not diffusively (∝ √t) — because ED's worldlines are straight (|v|≈1), not random-walk steps. (The gaussian/ring ICs give weaker signals — no sharp front — but eikonal still beats diffusion.)

## Verdict

**#3 does not flip to diffusion — because diffusion was the wrong continuum target.** The coherent/mean density *does* obey a clean continuum law (the decomposition method works), but it is **transport/eikonal, not the diffusion PDE.** This is the "you can coarse-grain many ways" point (Newton vs GR for gravity): diffusion and transport are two candidate continuum laws, and ED coarse-grains to the **transport** one. It confirms, at the ensemble-mean level, the CoarseGrain trilogy's verdict that the certified ED substrate is a **kinetic lattice-gas (ballistic worldlines), not a diffusion PDE.**

## The three outcomes — the real result of the arc

The coherent/disorder decomposition, applied to three "ED doesn't reach the continuum" walls, gives **three genuinely different answers** — and the *discriminator* is the content:

| | coherent/signal part | outcome |
|---|---|---|
| **#2 Maxwell** | = the textbook object (Coulomb field) | **window** — measurement error, signal was masked by entropy |
| **#3 diffusion** | a clean continuum law, but a *different* object (transport/eikonal) | **window to the "wrong" object** — ED's continuum is transport, not diffusion |
| **#5c Gaussianity** | *no* coherent object (field is intrinsically non-Gaussian) | **wall** — no signal there to recover |

So the decomposition reveals **what continuum law ED actually coarse-grains to**, and it is *not always the textbook object you asked for, and sometimes there is no clean object at all.* The method + the three outcomes + the discriminator (is there a coherent signal, and is it the expected object?) is a richer, more honest result than "three windows." **Notebook documentation; no external prediction claimed** (per AP).

---

*#3 re-check (`diffusion_coherent_decomp.py`). Ensemble-mean density (signal; ballistic-worldline disorder averaged out): does it diffuse? NO flip to diffusion — but ensemble-averaging reveals a CLEAN continuum law (step IC R² 0.10→0.60), and it is EIKONAL/TRANSPORT (|∇ρ| R²=0.597) not diffusion (∇²ρ R²=0.258). ED's coarse density continuum is ballistic transport, not diffusion — the diffusion PDE was the wrong target (Newton-vs-GR: many CGs; ED gives the transport one). Confirms CoarseGrain's kinetic-lattice-gas finding at ensemble-mean level. Three-outcome arc: #2 Maxwell = window to the textbook object; #3 diffusion = window to a DIFFERENT object (transport not diffusion); #5c Gaussianity = wall (no coherent object, intrinsically non-Gaussian). The coherent/disorder decomposition reveals ED's actual continuum law + a discriminator (coherent signal? expected object?). Crank-rail: my prior (mean stays ballistic, not diffusion) was right this time — did NOT force a flip. Notebook only; no external prediction (per AP).*
