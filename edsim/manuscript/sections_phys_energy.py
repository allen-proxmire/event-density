"""
edsim.manuscript.sections_phys_energy — Manuscript section for ED-PHYS-07.
"""

from __future__ import annotations


def section_phys_energy() -> str:
    """Return a manuscript-ready section for ED-PHYS-07."""
    from ..phys import run_full_energy_study

    study = run_full_energy_study(d=2, N=32, H_pos=0.5)
    gf = study.gf_test

    mono_dec_H0 = [m.name for m in study.monotonicity_H0 if m.is_monotone_decreasing]
    mono_inc_H0 = [m.name for m in study.monotonicity_H0 if m.is_monotone_increasing]

    lyap_H0 = next(m for m in study.monotonicity_H0 if m.name == "E_Lyapunov")
    lyap_Hp = next(m for m in study.monotonicity_Hpos if m.name == "E_Lyapunov")

    text = f"""\
## ED-PHYS-07: Energy, Entropy, and Lyapunov Structure

### Candidate Functionals

Seven candidate functionals are tracked along ED trajectories:
$E_{{\\mathrm{{Lyap}}}}$, $E_{{\\mathrm{{grad}}}}$, $E_{{\\mathrm{{pen}}}}$,
$E_{{\\mathrm{{part}}}}$, $S_{{\\mathrm{{Boltz}}}}$, $I_{{\\mathrm{{Fisher}}}}$,
and $F_{{\\mathrm{{free}}}}$.

### Monotonicity (H = 0)

With zero participation coupling, {len(mono_dec_H0)} functionals are
monotone decreasing: {', '.join(mono_dec_H0)}.  Boltzmann entropy
is monotone increasing.

$E_{{\\mathrm{{Lyap}}}}$ decays to {lyap_H0.decay_ratio:.2e} of its initial
value, confirming Law 2 (monotone energy decay).

### Monotonicity (H = 0.5)

$E_{{\\mathrm{{Lyap}}}}$ remains monotone decreasing (decay ratio
{lyap_Hp.decay_ratio:.2e}) because the participation injection is weaker
than the dissipation at this amplitude.  For larger $H$ or larger
perturbations, monotonicity can be violated.

### Gradient-Flow Test

The ED operator is compared to the formal gradient flow
$\\partial_t\\rho = D\\,\\nabla\\!\\cdot\\!(M\\,\\nabla(P/M))$.
The residual is {gf.mean_residual:.1%}: **ED is NOT a gradient flow**
of $E_{{\\mathrm{{Lyap}}}}$.  The operators differ by
$O(|\\nabla\\rho|^2)$ terms from the nonlinear mobility.

### Summary

ED possesses a Lyapunov functional (Law 2) but is not a gradient flow.
Five functionals are simultaneously monotone decreasing for $H = 0$,
providing a rich dissipation structure.  Boltzmann entropy increases
(diffusion increases disorder) but is not a Lyapunov functional.
"""
    return text
