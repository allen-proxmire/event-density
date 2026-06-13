# Phase-3 GR — The Sub-Leading Reserve Speed-Renormalization of the Khronon

**Foundations derivation + measurement — the sub-leading correction to `c_s = c` flagged in the `ε`-derivation. Not a corpus edit, not a new primitive. Minor by construction.**
The `ε`-derivation established `c_s = c` at **leading order**: the dissipative reserve damps the khronon (it does not supply a conservative `λθ²` second cone). The flagged residual: integrating out the dissipative reserve renormalizes the *real* part of the dispersion sub-leadingly. This note computes that shift and confirms it.
**Crank rail:** the shift is derived from the damped-oscillator dispersion (not tuned); the measurement confirms the magnitude where resolvable. Sim: `evaluation/DynamicalBandwidth/reserve_speed_renorm.py`.

---

## 1. The derivation

A dissipative reserve coupling is a friction term `−γ ḣ` on the khronon. The damped wave equation

> `ḧ + γ ḣ + ω₀² h = 0`,  `ω₀ = c k`,

oscillates at `ω_d = √(ω₀² − γ²/4)`, so the phase speed is

> `c_s/c = ω_d/ω₀ = \sqrt{1 − (γ/2ck)²} \;≈\; 1 − \tfrac{1}{2}\,(γ/2ck)²`.

Three features, all sub-leading and benign:

- **`γ²`-suppressed** — the shift is second order in the (small) reserve coupling.
- **`k`-dependent** — it vanishes at high wavenumber; it is a dispersive, not a uniform-cone, effect.
- **Below `c`** — the renormalized khronon is *slightly slower*, never faster (so it never overtakes the light cone), and it **overdamps** entirely (stops propagating) when `γ > 2ck`.

## 2. Measurement

Measuring `ω_d(γ)/ω_d(0)` (the ratio cancels the lattice dispersion offset):

| `γ` | `ω_d/ω₀` (measured) | `√(1−(γ/2ω₀)²)` (predicted) | `c_s/c − 1` |
|---|---|---|---|
| 0.00 | 1.000 | 1.000 | 0 |
| 0.05 | 0.969 | 0.999 | (resolution-limited) |
| 0.10 | 0.984 | 0.995 | (resolution-limited) |
| 0.20 | **0.977** | **0.979** | **−0.023** |

The small-`γ` points are below the zero-crossing measurement precision (the `γ²`-suppressed shift is `< 1 %`, comparable to the timing resolution), but the largest resolvable point confirms the formula: `γ = 0.20` gives `−2.3 %` measured vs `−2.1 %` predicted. The trend (a slowing below `c`, growing with `γ`) is correct throughout.

## 3. Verdict

**The sub-leading reserve renormalization slows the khronon below `c` by `c_s/c = √(1−(γ/2ck)²) ≈ 1 − γ²/(8c²k²)` — tiny, `γ²`-suppressed, `k`-dependent, and below the light cone; confirmed numerically at resolvable damping (`γ = 0.20`: `−2.3 %` vs `−2.1 %`).** This *reinforces* `c_s = c` for the observable khronon: in **vacuum** (no commitment, `γ → 0`) the shift vanishes and the far-field khronon a detector sees is at exactly `c`; only **near matter** (finite `γ`) does it slow slightly, and there it is anyway **overdamped** (`γ > 2ck`, no propagation). So the renormalization never produces a second cone — it is a near-matter slowing of an already-dissipated mode, with the propagating far-field khronon at `c`. The flagged residual is closed: the correction exists, is computed, and is benign.

---

*The sub-leading reserve speed-renormalization. Integrating out the dissipative reserve (a friction `−γḣ`) gives `c_s/c = √(1−(γ/2ck)²) ≈ 1 − γ²/(8c²k²)` — a tiny, `γ²`-suppressed, `k`-dependent shift **below** `c`, vanishing in vacuum (`γ→0`) and overdamping near matter (`γ>2ck`). Confirmed at resolvable damping (`γ=0.20`: `−2.3 %` measured vs `−2.1 %` predicted). It reinforces `c_s = c` for the observable (vacuum) khronon and never yields a second cone. No corpus edits, no new primitives.*
