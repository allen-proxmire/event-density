"""GRF-Gaussianity higher-cumulant test (the ED-SC 3.x could-say-no).

The S1 statistical sub-arc (motif-conditioned invariant, r*-filtered-GRF,
saddle-classification, SC-4.11 spectral moment) assumes the coarse-grained
participation field is a GAUSSIAN RANDOM FIELD in the hydrodynamic window.
The layers/CoarseGrain program measured the layer-1 deposit field as committal/
trapping and non-Gaussian (random-Fourier-phase diagnostic fails). These
collide. The scale-invariance README proposes exactly this test and flags the
hypothesis "may therefore be false."

THE TEST. Run the certified substrate (evaluation/Bits/simulator, standard
SigmaCoeffs) with SCATTERED seeding (statistically homogeneous field; a radial
mean profile would masquerade as non-Gaussianity). Take the DEPOSIT field
delta = rho_final - rho_initial. Coarse-grain by block-averaging at B in
{2,4,8} (the aggregation ladder toward the hydrodynamic window). At each scale
measure:
  - g1 (standardized skewness), g2 (excess kurtosis) of block means;
  - a connected three-point proxy T3 = <d_i d_j d_k> over adjacent horizontal
    triples of standardized block fields (bispectrum-adjacent, phase-sensitive).
Null: PHASE-RANDOMIZED SURROGATES of the same field (identical power spectrum,
randomized Fourier phases => Gaussianized) -- the exact Gaussian null for this
spectrum, the same diagnostic family the layers program used. Report z-scores
of the real field's statistics against the surrogate distribution.

VERDICTS (stated before running):
  - GRF-hypothesis holds in the window: |z| falls to O(1-2) as B grows
    (CLT/decorrelation Gaussianizes the coarse field).
  - GRF-hypothesis FALSE: significant |z| persists at the coarsest scales
    (structure-making/trapping defeats aggregation) -> the S1 sub-arc's regime
    hypothesis fails; retire/requalify (the soliton-test precedent).
Zero-inflation at fine scales (never-committed cells) is expected and trivially
non-Gaussian; the question is the trend across scales, which is why B=1 is
reported only as the baseline.
"""
import numpy as np
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "evaluation", "Bits"))
from simulator import (ParticipationGraph, NodeState, StateVector, SigmaCoeffs,  # noqa: E402
                       assign_stratum_ids, step)

COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5, increment=1.0,
                     extinction_threshold=-2.0)   # certified defaults (blindness/A3 probes)
SIDE = 64
RHO_BG = 0.5
SEED_FRAC = 0.04
MAX_STEPS = 2500
N_SEEDS = 12
N_SURR = 24
BLOCKS = (1, 2, 4, 8, 16)


def corr_length(field):
    """e-folding radial autocorrelation length (cells) of the standardized field,
    via FFT autocorrelation. Guards the CLT reading: blocks must exceed xi for
    aggregation to have had its chance."""
    x = field - field.mean()
    F = np.fft.rfft2(x)
    ac = np.fft.irfft2(np.abs(F) ** 2, s=field.shape)
    ac = ac / ac[0, 0]
    n = field.shape[0]
    prof = {}
    for dr in range(n // 2):
        for dc in range(n // 2):
            r = int(round(np.hypot(dr, dc)))
            prof.setdefault(r, []).append(ac[dr, dc])
    rs = sorted(prof)
    vals = np.array([np.mean(prof[r]) for r in rs])
    below = np.where(vals < np.exp(-1))[0]
    return float(rs[below[0]]) if len(below) else float(n // 2)


def run_deposit(seed):
    rng = np.random.default_rng(seed)
    g = ParticipationGraph()
    for r in range(SIDE):
        for c in range(SIDE):
            p = r * SIDE + c
            if c + 1 < SIDE: g.add_edge(p, r * SIDE + c + 1, bandwidth=0.5)
            if r + 1 < SIDE: g.add_edge(p, (r + 1) * SIDE + c, bandwidth=0.5)
    sv = StateVector()
    rho0 = np.empty((SIDE, SIDE))
    for r in range(SIDE):
        for c in range(SIDE):
            p = r * SIDE + c
            v = RHO_BG + rng.normal(0, 1e-3)
            rho0[r, c] = v
            sv[p] = NodeState(rho=float(v), orientation=rng.normal(size=2))
    # scattered seeding -> statistically homogeneous deposit
    for s in rng.choice(SIDE * SIDE, size=max(5, int(SEED_FRAC * SIDE * SIDE)),
                        replace=False):
        sv[int(s)].active = True
    for t in range(1, MAX_STEPS + 1):
        if step(sv, g, COEFFS, strata=assign_stratum_ids(sv, g)) == 0:
            break
    rho1 = np.array([sv[p].rho for p in range(SIDE * SIDE)]).reshape(SIDE, SIDE)
    return rho1 - rho0          # the deposit field (what commitment wrote)


def phase_surrogate(field, rng):
    """Same power spectrum, randomized phases (Gaussianized null)."""
    F = np.fft.rfft2(field - field.mean())
    amp = np.abs(F)
    ph = rng.uniform(0, 2 * np.pi, size=F.shape)
    # keep DC and Nyquist-real entries real
    ph[0, 0] = 0.0
    S = amp * np.exp(1j * ph)
    out = np.fft.irfft2(S, s=field.shape)
    return out


def block_mean(field, B):
    n = field.shape[0] // B
    return field[:n * B, :n * B].reshape(n, B, n, B).mean(axis=(1, 3))


def stats_of(field):
    """(g1 skewness, g2 excess kurtosis, T3 adjacent-triple product) of the
    standardized field."""
    x = field.ravel().astype(float)
    x = x - x.mean()
    s = x.std()
    if s < 1e-15:
        return 0.0, 0.0, 0.0
    x = x / s
    g1 = float(np.mean(x ** 3))
    g2 = float(np.mean(x ** 4) - 3.0)
    z = (field - field.mean()) / s
    T3 = float(np.mean(z[:, :-2] * z[:, 1:-1] * z[:, 2:]))   # horizontal triples
    return g1, g2, T3


def main():
    rng = np.random.default_rng(2026)
    print("=" * 80)
    print("GRF-Gaussianity higher-cumulant test  (certified substrate, deposit field)")
    print(f"grid {SIDE}x{SIDE}, scattered seeds {SEED_FRAC:.0%}, coeffs kc/ks/kg=1 "
          f"rho*=0.5 ext=-2.0, {N_SEEDS} runs, {N_SURR} phase surrogates/run")
    print("=" * 80)

    fields = [run_deposit(s) for s in range(N_SEEDS)]

    xis = [corr_length(f) for f in fields]
    print(f"\ndeposit autocorrelation length xi = {np.mean(xis):.2f} +/- "
          f"{np.std(xis):.2f} cells  (CLT guard: coarsest B must be >> xi)")

    print(f"\n{'B':>3} {'stat':>5} {'real(mean)':>11} {'null(mean)':>11} "
          f"{'null(sd)':>9} {'z':>8}   verdict-input")
    summary = {}
    for B in BLOCKS:
        real = np.array([stats_of(block_mean(f, B)) for f in fields])
        null = []
        for f in fields:
            for _ in range(N_SURR // N_SEEDS + 1):
                null.append(stats_of(block_mean(phase_surrogate(f, rng), B)))
        null = np.array(null)
        for k, name in enumerate(("g1", "g2", "T3")):
            r_m = real[:, k].mean()
            n_m, n_sd = null[:, k].mean(), null[:, k].std()
            # z of the MEAN of N_SEEDS real runs vs the null spread of a single
            # field, scaled for the mean of N_SEEDS
            z = (r_m - n_m) / (n_sd / np.sqrt(N_SEEDS) + 1e-15)
            summary[(B, name)] = z
            print(f"{B:>3} {name:>5} {r_m:>11.4f} {n_m:>11.4f} {n_sd:>9.4f} "
                  f"{z:>8.1f}")
        print()

    print("=" * 80)
    print("READING:")
    print("  B=1 is the raw-deposit baseline (zero-inflated, expected non-Gaussian).")
    print("  GRF-hypothesis (ED-SC 3.x S1) needs |z| -> O(1-2) by the coarsest B.")
    print("  Persistent large |z| at B=8 ==> coarse field NOT a GRF ==> the S1")
    print("  sub-arc's regime hypothesis fails on the certified substrate.")
    coarse = [abs(summary[(BLOCKS[-1], n)]) for n in ("g1", "g2", "T3")]
    print(f"  |z| at B={BLOCKS[-1]}: g1={coarse[0]:.1f}  g2={coarse[1]:.1f}  "
          f"T3={coarse[2]:.1f}")
    print("=" * 80)


if __name__ == "__main__":
    main()
