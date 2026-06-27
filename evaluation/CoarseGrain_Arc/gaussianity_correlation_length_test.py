"""Layer-2 test #1 — GAUSSIANITY via correlation length: does ED's layer-1 deposit field
Gaussianize once you coarse-grain PAST its correlation length (door #1), or is it
genuinely non-Gaussian at every scale (door #2)?

The CLT fires only when you average INDEPENDENT contributions — i.e. over a region much
larger than the correlation length xi. The earlier #5c test coarse-grained only at small
R_cg and found non-Gaussian + anti-CLT (kurtosis grew). The honest decider is: measure xi
directly, then coarse-grain at R_cg >> xi and watch the kurtosis.

  - kurtosis -> 0 once R_cg >> xi  => DOOR #1 (Gaussianizes past the correlation length;
    layer-2 Gaussianity exists; #5c was just too local).
  - kurtosis stays / grows, or xi is effectively scale-invariant (large) => DOOR #2
    (genuinely non-Gaussian; the observed Gaussian world is paid at a different layer —
    the layer-2 walker density, which the diffusion test already showed IS ~Gaussian).

Note the two-layer split this lives in: the deposit field is the LAYER-1 (committal)
object; the walker-position density is the LAYER-2 (diffused) object and is Gaussian
(diffusion test). This test is about the layer-1 field. Certified Sigma-substrate.
"""
from __future__ import annotations
import os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coarsegrain_test import ensemble_run, coarse


def cumulants(x):
    x = np.asarray(x, float); x = x - x.mean(); s = x.std()
    if s < 1e-12:
        return 0.0, 0.0
    return float(np.mean(x ** 3) / s ** 3), float(np.mean(x ** 4) / s ** 4 - 3.0)


def corr_length(frames):
    """correlation length xi (cells) from the radially-averaged autocorrelation, per-frame demeaned."""
    radials = []
    for f in frames:
        f = f - f.mean()
        C = np.fft.ifft2(np.abs(np.fft.fft2(f)) ** 2).real
        C = np.fft.fftshift(C)
        C = C / C.max()
        cy, cx = np.array(C.shape) // 2
        yy, xx = np.mgrid[0:C.shape[0], 0:C.shape[1]]
        r = np.hypot(xx - cx, yy - cy).astype(int)
        rad = np.array([C[r == i].mean() for i in range(1, min(cx, cy))])
        radials.append(rad)
    rad = np.mean(radials, axis=0)
    below = np.where(rad < 1.0 / np.e)[0]
    xi = (below[0] + 1) if len(below) else len(rad)
    return xi, rad


def main():
    S, T = 161, 50
    seeds = list(range(2, 12))
    LATE = 0.4
    SEED_FRAC = 0.01
    print("=" * 80)
    print(f"GAUSSIANITY correlation-length test — door #1 (Gaussianizes past xi) vs #2  (S={S})")
    print("=" * 80)

    late_frames = []
    for sd in seeds:
        fr = ensemble_run(S, "uniform", T, n_seed_frac=SEED_FRAC, seed=sd)
        n = len(fr)
        late_frames.extend(list(fr[int(n * (1 - LATE)):]))
    late_frames = np.array(late_frames)

    xi, rad = corr_length(late_frames)
    print(f"\n  correlation length xi ~ {xi} cells  (autocorrelation 1/e crossing)")
    print("    autocorr C(r)/C(0): " + " ".join(f"{rad[k]:.2f}" for k in range(0, min(20, len(rad)), 2)))
    frac_of_box = xi / (S / 2)
    print(f"    xi / (S/2) = {frac_of_box:.2f}  ({'finite, well inside the box -> can CG past it' if frac_of_box < 0.3 else 'large vs box -> effectively scale-invariant (leans #2)'})")

    print(f"\n  {'R_cg':>5} {'R_cg/xi':>8} {'skew':>8} {'exkurt':>8}   reading")
    blocks = sorted(set([1, max(2, xi // 2), xi, 2 * xi, 4 * xi, 8 * xi]))
    blocks = [b for b in blocks if b <= S // 4]
    ek_trend = []
    for b in blocks:
        cg = coarse(late_frames, b)
        pooled = np.concatenate([(f - f.mean()).ravel() for f in cg])
        sk, ek = cumulants(pooled)
        ek_trend.append(ek)
        tag = "~Gaussian" if abs(sk) < 0.15 and abs(ek) < 0.2 else "non-Gaussian"
        print(f"  {b:>5} {b/max(xi,1):>8.1f} {sk:>8.2f} {ek:>8.2f}   {tag}")

    print("\n" + "-" * 80)
    far = [ek for b, ek in zip(blocks, ek_trend) if b >= 2 * xi]
    if far and abs(np.mean(far)) < 0.2:
        v = "DOOR #1 — kurtosis -> 0 past xi: the layer-1 field DOES Gaussianize (CLT fires)"
    elif len(ek_trend) >= 2 and ek_trend[-1] > ek_trend[0]:
        v = "DOOR #2 — kurtosis grows / stays with CG: genuinely non-Gaussian (anti-CLT confirmed)"
    else:
        v = "INTERMEDIATE — does not cleanly Gaussianize past xi; leans #2"
    print(f"  VERDICT (layer-1 deposit field): {v}")
    print("  (Layer-2 walker density is separately ~Gaussian — diffusion test. Two layers.)")
    print("-" * 80)
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
