"""#5c, the RIGHT test (AP's route 3): is ED's coarse field a Gaussian random field
in the sense that actually matters -- random Fourier PHASES?

A GRF is DEFINED by independent Gaussian Fourier modes <=> random independent phases.
Amplitude-Gaussianity is a trap: by a CLT-in-Fourier-space, each mode a_k = sum_x f(x)
e^{-ikx} is a sum over all space, so almost ANY field has ~Gaussian amplitudes. What
separates a true GRF from a lumpy non-Gaussian field is the PHASES -- filaments ARE
phase correlations.

Test (phase-randomized surrogate, the standard one): build the Gaussian field with
ED's EXACT power spectrum (keep |a_k|, randomize phases) and compare real-space
cumulants. The surrogate is "the most Gaussian field that still has ED's power
spectrum."
  - ED field cumulants ~ surrogate cumulants : the non-Gaussianity is just the power
    spectrum; the PHASES are random -> ED is a GRF -> #5c FLIPS (route 3).
  - ED field MORE non-Gaussian than surrogate : the non-Gaussianity is in the PHASES
    (filaments = correlated phases) -> genuinely non-Gaussian -> #5c CONFIRMED.

Honest prior: ED's filaments are coherent structures = phase-aligned, so I expect
CORRELATED phases (ED >> surrogate) -> confirm, not flip. But this is the correct
test and it could surprise (it has twice). Sparse seeding = strong filaments = hardest.
"""
from __future__ import annotations
import os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coarsegrain_test import ensemble_run, coarse


def cumulants(x):
    x = np.asarray(x, float)
    x = x - x.mean()
    s = x.std()
    if s < 1e-12:
        return 0.0, 0.0
    return float(np.mean(x ** 3) / s ** 3), float(np.mean(x ** 4) / s ** 4 - 3.0)


def phase_surrogate(field, rng):
    """Gaussian field with the SAME power spectrum: keep |FFT|, randomize phases
    (Hermitian-valid phases borrowed from a white-noise field's FFT)."""
    F = np.fft.fft2(field)
    amp = np.abs(F)
    g = rng.standard_normal(field.shape)
    ph = np.angle(np.fft.fft2(g))      # valid Hermitian random phases -> real surrogate
    surr = np.fft.ifft2(amp * np.exp(1j * ph)).real
    return surr


def main():
    S, T = 121, 45
    seeds = list(range(2, 14))
    LATE = 0.4
    SEED_FRAC = 0.01           # sparse -> strong filaments = hardest test
    rng = np.random.default_rng(12345)

    print("=" * 80)
    print(f"#5c Fourier-phase test — is the non-Gaussianity in the PHASES?  (S={S}, sparse)")
    print("=" * 80)

    fields = []
    for sd in seeds:
        fr = ensemble_run(S, "uniform", T, n_seed_frac=SEED_FRAC, seed=sd)
        n = len(fr)
        fields.append(fr[int(n * (1 - LATE)):])

    for b in (1, 4):
        ed_sk, ed_ek, su_sk, su_ek = [], [], [], []
        for late in fields:
            cg = coarse(late, b)
            for f in cg:
                sk, ek = cumulants(f.ravel())
                ed_sk.append(sk); ed_ek.append(ek)
                surr = phase_surrogate(f, rng)
                ssk, sek = cumulants(surr.ravel())
                su_sk.append(ssk); su_ek.append(sek)
        ed_sk, ed_ek = np.mean(ed_sk), np.mean(ed_ek)
        su_sk, su_ek = np.mean(su_sk), np.mean(su_ek)
        print(f"\n  R_cg = {b}")
        print(f"    {'':<22}{'skew':>9}{'exkurt':>9}")
        print(f"    ED field            {ed_sk:>9.3f}{ed_ek:>9.3f}")
        print(f"    phase-surrogate     {su_sk:>9.3f}{su_ek:>9.3f}   (Gaussian field, ED's power spectrum)")
        # how much non-Gaussianity is removed by randomizing phases?
        ng_ed = abs(ed_sk) + abs(ed_ek)
        ng_su = abs(su_sk) + abs(su_ek)
        frac = (ng_ed - ng_su) / ng_ed if ng_ed > 1e-9 else 0.0
        print(f"    -> {frac*100:.0f}% of ED's non-Gaussianity is in the PHASES "
              f"({'flip: phases ~random, it is a GRF' if frac < 0.3 else 'confirm: phases carry it, genuinely non-Gaussian'})")

    print("\n" + "-" * 80)
    print("READ: surrogate ~ Gaussian (skew,kurt ~0) AND ED field also ~0 -> phases are")
    print("  random, ED is a GRF (flip). ED field non-Gaussian while surrogate is ~0 -> the")
    print("  non-Gaussianity is in the phases (filaments = correlated phases), genuine (confirm).")
    print("-" * 80)
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
