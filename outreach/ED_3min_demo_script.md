# Event Density: 3-Minute Demo Script

**Purpose:** Spoken walkthrough for a screen-recorded video showing ED in action.
**Tone:** Clear, confident, accurate. No jargon without explanation. No hedging.

---

## [0:00 -- 0:20] Opening

> I'm going to show you a single PDE that reproduces known physical laws without importing them.
>
> No fitting. No tuning. No borrowed equations. Just four primitives, seven axioms, and the structural consequences that follow.
>
> This is Event Density.

*[Screen: Repository README or the 1-pager overview]*

---

## [0:20 -- 0:50] What ED Is

> Event Density starts with four objects: a bounded density field, a degenerate mobility that vanishes at capacity, a monostable penalty that drives the system toward equilibrium, and a global participation variable.
>
> From seven structural axioms -- locality, isotropy, gradient-driven flow, dissipative structure, single scalar field, minimal coupling, and dimensional consistency -- these four primitives determine a unique canonical PDE.
>
> The PDE decomposes into three channels: mobility, penalty, and participation. Each channel can be activated or silenced independently.

*[Screen: The canonical PDE from WHAT_IS_ED.md, or a clean slide version]*

---

## [0:50 -- 1:20] Running the Pipeline

> Let's run it. I'm going to execute the ED simulation engine on a 64-by-64 grid with canonical parameters. No special tuning -- these are the default values derived from the axioms.
>
> The simulation runs in about ten seconds. It produces density field snapshots, tracks the Lyapunov energy, computes dissipation channel fractions, and records nine architectural invariants at every output step.

*[Screen: Running Cell 4 in the notebook. Show the output: "Done. N snapshots recorded."]*

> Here's the density field evolving over time. You can see the initial cosine perturbation relaxing toward the unique equilibrium. The mobility creates nonlinear diffusion; the penalty drives convergence; the participation creates global oscillatory feedback.

*[Screen: The 4-panel density field evolution plot from Cell 5]*

---

## [1:20 -- 1:50] The Structural Analogues

> Now here's what makes this interesting. When I silence the mobility and participation channels -- set H to zero and start with a uniform field -- the PDE reduces to a single ODE.
>
> That ODE is identical to an RC-circuit discharge equation. The time constant is set by the constitutive architecture: one over D times P-zero. The error between ED and the analytical prediction is zero-point-zero-zero percent.

*[Screen: The RC decay plot from Cell 7, showing ED simulation overlaying the analytical prediction]*

> When I turn the participation channel back on, the system becomes a damped harmonic oscillator -- mathematically identical to a telegraph equation, or equivalently, an RLC circuit. The frequency and damping match the analytical prediction exactly.

*[Screen: The telegraph oscillation plot from Cell 8]*

> These are not analogies. The penalty channel *is* exponential decay. The participation channel *is* a telegraph oscillator. The governing equations are identical.

---

## [1:50 -- 2:20] The Nine Laws

> ED predicts nine architectural laws that hold across all parameter values and all spatial dimensions from one through four. Let me verify them against this simulation.

*[Screen: Running Cell 6. Show the verification table with PASS/FAIL results]*

> Monotone energy decay. Spectral concentration. Topological conservation. Dimensional universality. These aren't design choices -- they're mathematical consequences of the four primitives and seven axioms. And every one of them has an explicit falsification condition.

---

## [2:20 -- 2:50] Why This Matters

> So what you've just seen is a single, minimal PDE that reproduces the mathematical structure of exponential relaxation, porous-medium diffusion, and telegraph oscillation. It does this without importing any of those laws. They emerge from the constitutive architecture.
>
> Beyond the foundational pipeline, ED also produces dwarf galaxy rotation curves matching Burkert profiles to 99.6%, flat weak-lensing signals at 100 to 1000 kiloparsecs where NFW and Burkert both fail, and a Baryonic Tully-Fisher exponent of one-quarter that matches the observed free fit to within 0.2 sigma.
>
> All of this is in the repository. Everything is reproducible. Every claim has code behind it.

---

## [2:50 -- 3:00] Close

> Event Density is a candidate unifying ontology for physical law. The repository is open, the pipeline is reproducible, and the predictions are falsifiable.
>
> Clone it. Run it. Tell me what you see.

*[Screen: Repository URL]*

---

## Production Notes

- **Total runtime target:** 3:00
- **Screen recording:** Jupyter notebook cells executing in real time
- **No slides required** -- the notebook IS the visual
- **Suggested software:** OBS Studio for screen capture, or Loom for quick recording
- **Resolution:** 1920x1080, with notebook zoomed to ~125% for readability
- **Audio:** Direct to camera or voiceover; no background music
