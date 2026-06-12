"""ED-ShadowEmergence Round 1 — does PURE ED (eps=0) cast its own diffusion shadow?

The philosophically load-bearing test. ThickRegime R1 showed a clean diffusion PDE only at eps=1
(Sigma-selection fully replaced by injected random scatter). But molecular dynamics is ALSO
deterministic and DOES coarse-grain to diffusion -- via MIXING (chaotic, correlation-decaying
determinism), not via injected noise. So the legitimate question ThickRegime did NOT test:

  does ED generate its OWN effective randomness -- emergent mixing from many interacting
  commitments on rough, self-roughening landscapes -- at eps=0, no injected noise?

If yes: the smooth PDE layer is a TRUE shadow of collective ED determinacy (bridge crossable
from inside ED). If no: ED's committal determinism TRAPS rather than mixes, and confirmed-physics
PDEs live in a different ED model (Q-C/UDM), not the certified Sigma-substrate.

Design (sharper than 'measure alpha'): the decisive 'is it really a PDE' test is SCALE-STABILITY
of the diffusion coefficient. A true diffusion equation has gamma(k) = D k^2 EXACTLY, so
D = gamma(k)/k^2 must be IDENTICAL at every wavenumber. We seed a localized stripe (exciting many
x-modes at once), watch each Fourier mode b_n(t) decay, fit gamma_n, and test gamma_n ~ n^2 i.e.
D_n = gamma_n/k_n^2 = const. Flat D across modes => genuine diffusion; D drifting with scale =>
a kinetic pretender, not a PDE. Ensemble-averaged over hundreds of independent landscapes for SNR.

Crank-safety: eps=0 ONLY (pure certified Sigma-selection; vectorised Sigma validated bit-for-bit).
No primitive changed; rho monotone (P11); bandwidth conserved exactly (unit carriers only MOVED);
periodic boundaries; no drains/sources; landscapes roughen ONLY from ED's own deposits. One eps=1
column is run purely as an instrument-calibration reference (recovers D=0.25), clearly labelled.
"""
from __future__ import annotations
import os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from thick_regime_test import sigma_field, drift_dir, _block, validate_sigma, DX, DY, INCR  # noqa: E402

KMODES = (1, 2, 3, 4)


def landscape(kind, S, rng):
    """Independent initial rho landscapes, all banded near rho*=0.5 so Sigma is meaningful."""
    yy, xx = np.mgrid[0:S, 0:S].astype(float)
    if kind == "smooth":
        f = np.zeros((S, S))
        for _ in range(4):
            kx, ky = rng.integers(1, 4, 2); ph = rng.uniform(0, 2 * np.pi)
            f += np.cos(2 * np.pi * kx * xx / S + ph) * np.cos(2 * np.pi * ky * yy / S)
        f = (f - f.min()) / (np.ptp(f) + 1e-9)
    elif kind == "random":
        f = rng.uniform(0, 1, (S, S))
    elif kind == "gradient":
        f = xx / S
    elif kind == "ring":
        r = np.hypot(xx - S / 2, yy - S / 2)
        f = 0.5 + 0.45 * np.cos(2 * np.pi * r / (S / 3))
        f = (f - f.min()) / (np.ptp(f) + 1e-9)
    else:  # multibasin
        f = np.zeros((S, S))
        for _ in range(5):
            cx, cy = rng.uniform(0, S, 2); w = rng.uniform(S / 12, S / 6)
            f += np.exp(-((xx - cx) ** 2 + (yy - cy) ** 2) / (2 * w * w))
        f = (f - f.min()) / (np.ptp(f) + 1e-9)
    return 0.1 + 0.8 * f                                   # band into [0.1, 0.9]


def run(S, T, frac, eps, kind, seed):
    rng = np.random.default_rng(seed)
    rho = landscape(kind, S, rng)
    n = int(frac * S * S)
    # localized stripe IC in x (excites many x-modes); y uniform
    X = (rng.normal(S / 2, 2.0, n) % S).astype(np.int64)
    Y = rng.integers(0, S, n)
    Xu = X.astype(float).copy()
    xs = np.arange(S)
    amp = np.zeros((len(KMODES), T)); msdx = np.zeros(T); pers = np.zeros(T)
    prev = -np.ones(n, dtype=np.int64)
    Bsizes = [b for b in (4, 8, 16) if S % b == 0]
    bsnap = {b: [] for b in Bsizes}; jxs = {b: [] for b in Bsizes}; jys = {b: [] for b in Bsizes}
    for t in range(T):
        dmap = drift_dir(rho)
        det = dmap[Y, X]
        if eps > 0:
            ran = rng.integers(0, 4, n); d = np.where(rng.random(n) < eps, ran, det)
        else:
            d = det
        if t > 0:
            pers[t] = np.mean(d == prev)
        prev = d
        b = np.zeros((S, S)); np.add.at(b, (Y, X), 1.0)
        jx = np.zeros((S, S)); jy = np.zeros((S, S))
        np.add.at(jx, (Y, X), DX[d]); np.add.at(jy, (Y, X), DY[d])
        for B in Bsizes:
            bsnap[B].append(_block(b, B)); jxs[B].append(_block(jx, B)); jys[B].append(_block(jy, B))
        bx = b.sum(0)
        for i, kk in enumerate(KMODES):
            amp[i, t] = abs(np.sum(bx * np.exp(-1j * 2 * np.pi * kk * xs / S))) / n
        msdx[t] = np.var(Xu)
        X = (X + DX[d]) % S; Y = (Y + DY[d]) % S; Xu += DX[d]
        np.add.at(rho, (Y, X), INCR)
    return amp, msdx, pers, {b: np.array(bsnap[b]) for b in Bsizes}, \
        {b: np.array(jxs[b]) for b in Bsizes}, {b: np.array(jys[b]) for b in Bsizes}, Bsizes


def fit_rate(a):
    """gamma from ln a ~ -gamma t over the window a/a0 in [0.15, 1]."""
    a0 = a[0] if a[0] > 0 else 1.0
    r = a / a0; t = np.arange(len(a))
    m = (r > 0.15) & (r <= 1.0001)
    if m.sum() < 4:
        return np.nan, np.nan
    sl, _ = np.polyfit(t[m], np.log(r[m]), 1)
    pred = np.polyval([sl, _], t[m])
    R2 = 1 - np.sum((np.log(r[m]) - pred) ** 2) / (np.sum((np.log(r[m]) - np.log(r[m]).mean()) ** 2) + 1e-12)
    return -sl, R2


def reg(y, *cols):
    A = np.column_stack(list(cols) + [np.ones_like(y)])
    c, *_ = np.linalg.lstsq(A, y, rcond=None)
    return 1 - np.sum((y - A @ c) ** 2) / (np.sum((y - y.mean()) ** 2) + 1e-12), c


def main():
    w = validate_sigma()
    S, T = 64, 80
    KINDS = ["smooth", "random", "gradient", "ring", "multibasin"]
    print("=" * 80)
    print(f"ED-ShadowEmergence R1 — does PURE ED (eps=0) cast its own diffusion shadow?")
    print(f"S={S} T={T}; certified Sigma validated max|diff|={w:.0e}; ensemble over {len(KINDS)} "
          f"landscape types")
    print("Scale-stability test: D_n = gamma_n/k_n^2 must be FLAT across modes for a true PDE.")
    print("=" * 80)

    for eps, frac, npl, tag in [(0.0, 1.0, 60, "PURE ED"), (0.0, 4.0, 60, "PURE ED, dense"),
                                (1.0, 4.0, 30, "eps=1 CALIBRATION")]:
        amp = np.zeros((len(KMODES), T)); msd = np.zeros(T); pers = np.zeros(T); npers = 0
        pool = {}
        Bs = None
        nruns = 0
        for ki, kind in enumerate(KINDS):
            for r in range(npl):
                a, mx, pe, bsn, jx, jy, Bsizes = run(S, T, frac, eps, kind, 9000 + ki * 1000 + r)
                amp += a; msd += mx; pers += pe; nruns += 1; Bs = Bsizes
                for B in Bsizes:
                    p = pool.setdefault(B, {"b": [], "jx": [], "jy": []})
                    p["b"].append(bsn[B]); p["jx"].append(jx[B]); p["jy"].append(jy[B])
        amp /= nruns; msd /= nruns; pers /= nruns

        # multi-mode decay -> D_n scale-stability
        Dn = []; R2n = []
        for i, kk in enumerate(KMODES):
            g, R2 = fit_rate(amp[i]); k = 2 * np.pi * kk / S
            Dn.append(g / (k * k) if g == g else np.nan); R2n.append(R2)
        Dn = np.array(Dn)
        cv = np.nanstd(Dn) / (np.nanmean(Dn) + 1e-12)
        # MSD exponent (late half, after roughening)
        tt = np.arange(T); mm = msd - msd[0]
        late = (tt > T // 3) & (mm > 0)
        alpha = np.polyfit(np.log(tt[late]), np.log(mm[late]), 1)[0] if late.sum() >= 4 else np.nan
        # persistence drop (mechanism)
        pv = pers[1:]; p_early = pv[:5].mean(); p_late = pv[-10:].mean()

        print(f"\n###### {tag}:  eps={eps}, frac={frac} ({nruns} runs, {int(frac*S*S)} carriers/run) ######")
        print(f"  mechanism:  persistence p  {p_early:.3f} (early) -> {p_late:.3f} (late)   "
              f"[0.25 = fully mixed/memoryless]")
        print(f"  MSD exponent alpha (late) = {alpha:.2f}   [1.0 diffusive, 2.0 ballistic, <1 trapping]")
        print(f"  mode decay D_n = gamma_n/k_n^2  (n=1..4):  "
              + "  ".join(f"{d:.3f}" for d in Dn))
        print(f"  mode decay-R^2 (exponential?):             "
              + "  ".join(f"{r:.2f}" for r in R2n))
        print(f"  >>> SCALE-STABILITY of D across modes: CV = {cv:.2f}   "
              f"[CV<~0.15 = genuine PDE; large CV = kinetic, not a PDE]")
        # pooled closure battery (caveat: local J shot-noise-limited)
        for B in Bs:
            bs = np.concatenate(pool[B]["b"]); jx = np.concatenate(pool[B]["jx"]); jy = np.concatenate(pool[B]["jy"])
            gx = np.gradient(bs, axis=2); gy = np.gradient(bs, axis=1)
            msk = bs > 0.05 * bs.max()
            J = np.concatenate([jx[msk], jy[msk]]); G = np.concatenate([-gx[msk], -gy[msk]])
            rf, cf = reg(J, G)
            print(f"     B={B:>2}: Fickian J=-D grad b  R^2={rf:.3f}  D={cf[0]:+.3f}   (local fit, shot-noise-limited)")

    print("\n" + "=" * 80)
    print("VERDICT key: does PURE ED (eps=0) reach alpha~1, exponential decay, AND scale-stable D")
    print("(low CV) -- WITHOUT injected noise? If yes -> diffusion is a true ED shadow (emergent")
    print("mixing). If alpha<1 / high CV -> ED's committal determinism traps, not mixes; the PDE")
    print("lives in a different ED model. Compare eps=0 columns to the eps=1 calibration (D~0.25).")
    print("=" * 80)
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
