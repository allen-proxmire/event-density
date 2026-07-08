"""V5 envelope-shape characterization: is the cross-chain coherence envelope
EXPONENTIAL, and does it come from phase dephasing?

V5's coupling = the cross-chain coherence (G1). So V5's spatial envelope F_V5 is
how the coherence C(r) decays with separation r. In the edge-adjacent dephasing
model (deposition reach = nearest-neighbor, so NO spatial envelope is imposed; any
decay is emergent), the P05 connection carries quenched disorder that random-walks
the transported phase along growth paths. Dephasing predicts:

    C(r) = <cos(dphi)> = e^{-V(r)/2},   V(r) = accumulated phase variance.
    independent per-edge increments => V(r) proportional to r => C(r) = e^{-r/xi}
    (EXPONENTIAL). Ballistic/coherent (V ~ r^2) => Gaussian. Sub-diffusive => stretched.

We measure C(r) directly (cos is wrapping-robust), form V_eff(r) = -2 ln C(r)
(exact for a wrapped-normal phase: the mean resultant length is e^{-sigma^2/2}),
and fit V_eff(r) ~ r^alpha. alpha = 1 is exponential C (independent-increment
dephasing); alpha = 2 is Gaussian; alpha < 1 stretched/sub-diffusive. We also fit
xi from C(r)=e^{-r/xi}, report the exponential-fit quality, where C first goes
negative (a deviation a pure exponential cannot produce), and the scale law xi(kappa)
(dephasing predicts xi ~ 1/kappa^2).

Reuses the certified rho-engine + P05 holonomy verbatim via run_fill from the
Step-3 intrinsic-disorder probe. No imposed envelope, single seed, no thermal noise.
"""
import sys, os
import numpy as np

THEORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, THEORY)
from p12_phase_coherence_probe_v2_intrinsic import run_fill  # noqa: E402


def corr_and_shape(phase, committed, coords, rng, rmax=32, n_pairs=1_200_000):
    idx = np.where(committed)[0]
    a = rng.choice(idx, n_pairs); b = rng.choice(idx, n_pairs)
    d = np.hypot(coords[a, 0] - coords[b, 0], coords[a, 1] - coords[b, 1])
    dcos = np.cos(phase[a] - phase[b]); rb = np.round(d).astype(int)
    C = {}
    for r in range(1, rmax + 1):
        m = rb == r
        if m.sum() > 200:
            C[r] = float(np.mean(dcos[m]))
    return C


def analyze(C):
    rs = np.array(sorted(C)); cs = np.array([C[r] for r in rs])
    # where does C first go negative?
    neg = rs[cs <= 0]
    neg_onset = int(neg[0]) if len(neg) else None
    # positive-C range for fits
    pos = cs > 0.02
    rp, cp = rs[pos], cs[pos]
    out = {"neg_onset": neg_onset, "C": {int(r): round(float(C[r]), 3) for r in rs}}
    if len(rp) < 4:
        out["note"] = "too few positive points to fit"; return out
    # exponential fit: ln C = -r/xi
    lnC = np.log(cp)
    A = np.vstack([rp, np.ones_like(rp)]).T
    slope, intercept = np.linalg.lstsq(A, lnC, rcond=None)[0]
    xi = -1.0 / slope if slope < 0 else float("inf")
    pred = A @ np.array([slope, intercept])
    ss_res = np.sum((lnC - pred) ** 2); ss_tot = np.sum((lnC - lnC.mean()) ** 2)
    r2_exp = 1 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    # shape exponent: V_eff = -2 ln C ~ r^alpha  =>  ln V_eff = ln A + alpha ln r
    Veff = -2.0 * lnC
    good = Veff > 0
    la = np.log(rp[good]); lv = np.log(Veff[good])
    B = np.vstack([la, np.ones_like(la)]).T
    alpha, _ = np.linalg.lstsq(B, lv, rcond=None)[0]
    out.update({"xi_exp": round(float(xi), 2), "r2_exp": round(float(r2_exp), 3),
                "alpha_shape": round(float(alpha), 2)})
    return out


def main():
    L = 80
    print(f"V5 ENVELOPE SHAPE: grid {L}x{L}, single seed, NO thermal noise, NO imposed")
    print("envelope (edge-adjacent deposition). Decay is purely emergent dephasing.\n")
    print("alpha_shape: 1.0 = exponential C (independent-increment dephasing);")
    print("2.0 = Gaussian (coherent/ballistic phase); <1 = stretched/sub-diffusive.\n")

    kappas = [0.3, 0.5, 1.0, 2.0]
    xis = []
    for kap in kappas:
        rng = np.random.default_rng(7)  # matched seed per condition
        phase, committed, coords = run_fill(L, bw_disorder=0.5, kappa_bw=kap,
                                             kappa_rho=0.0, rng=rng, n_seeds=1)
        rng2 = np.random.default_rng(101)
        C = corr_and_shape(phase, committed, coords, rng2)
        res = analyze(C)
        xis.append(res.get("xi_exp", float("nan")))
        print(f"### kappa_bw={kap}  committed={int(committed.sum())} ###")
        print(f"  C(r): " + "  ".join(f"{r}={res['C'].get(r,float('nan')):+.2f}"
                                      for r in [1, 2, 3, 5, 8, 12, 16, 22, 28] if r in res['C']))
        print(f"  exp-fit xi={res.get('xi_exp')}  R^2(ln C vs r)={res.get('r2_exp')}"
              f"  shape alpha={res.get('alpha_shape')}  C<0 onset r={res.get('neg_onset')}")
        print()

    # scale law xi(kappa): dephasing predicts xi ~ 1/kappa^2 (slope -2 in log-log)
    k = np.array(kappas, float); x = np.array(xis, float)
    ok = np.isfinite(x) & (x > 0)
    if ok.sum() >= 2:
        s, _ = np.linalg.lstsq(np.vstack([np.log(k[ok]), np.ones(ok.sum())]).T,
                               np.log(x[ok]), rcond=None)[0]
        print(f"SCALE LAW: xi(kappa) log-log slope = {s:.2f}  "
              f"(dephasing independent-increment predicts -2.0)")
        print(f"  kappa: {list(k)}   xi: {[round(v,2) for v in x]}")


if __name__ == "__main__":
    main()
