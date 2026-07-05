"""E1 probe: does STRUCTURED participation density impede commitment spread
(a mass-like effect), and is that mass-analog amplitude-INVARIANT the way Arc M's
sigma_tau claims, or amplitude-SENSITIVE like the certified Sigma actually is?

This is the substrate test of the H2 (bandwidth-shift / patterned-condensate) Higgs
candidate. Arc Q Q.4 evaluated H2 analytically: a UNIFORM condensate cannot give mass
because sigma_tau = hbar*sqrt(sum_X w^X <(d_mu ln b^X)^2>) reads the LOG-DERIVATIVE of
the bandwidth field and is blind to b -> alpha*b; only a SPATIALLY PATTERNED condensate
delta b(x) feeds the gradient integral. Nobody ran it on the substrate.

FIELD MAPPING (grounding, honest).  Arc M's sigma_tau is built on a rule-type bandwidth
field b that is amplitude-invariant by construction. The certified simulator
(evaluation/Bits/simulator) has NO such field: Sigma reads the COMMITMENT DENSITY rho
(B4) and graph-local structure only; the edge `bandwidth` enters solely at the tie-break,
and orientation is never read. So the certified substrate's own gradient-penalized field
is rho, via Sigma = kc*Coh(rho) - ks*rho - kg*|d rho|. We therefore pattern rho -- the
field the dynamics actually read -- NOT the edge bandwidth (which would be a field-
mismatch). This means the probe also tests whether Arc M's amplitude-INVARIANT sigma_tau
form is faithful to the amplitude-SENSITIVE certified Sigma, or an idealization.

WHAT IS "MASS" HERE.  Mass = a gap = influence that fails to spread. We seed a localized
commitment source and measure how far commitment REACHES before fronts extinguish. Free
(massless) spread reaches far; an effective mass suppresses the reach. We compare a
PATTERNED rho background against a UNIFORM one AT MATCHED MEAN, so any difference is from
the GRADIENT content, not the amplitude -- exactly the sigma_tau distinction.

Grounding discipline: we set only an allowed initial condition (the rho landscape) and
read a propagation observable off the certified step(). No new term, no coupling, no
potential. Survival is reported alongside reach to rule out the extinction confound that
spoiled the micro-stiffness probe (a barrier that kills fronts by extinction is not mass).
"""
import numpy as np
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "evaluation", "Bits"))
from simulator import (ParticipationGraph, NodeState, StateVector, SigmaCoeffs,  # noqa: E402
                       assign_stratum_ids, step)

# Certified default coefficients (as used by the blindness / A3 probes).
COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5,
                     increment=1.0, extinction_threshold=-2.0)
RHO_BG = 0.5          # background = rho_star, so uniform arm is coherence-neutral
SIDE = 41             # odd, so there is a center node
MAX_STEPS = 400


def build_grid(side):
    g = ParticipationGraph()
    for r in range(side):
        for c in range(side):
            p = r * side + c
            if c + 1 < side:
                g.add_edge(p, r * side + c + 1, bandwidth=0.5)
            if r + 1 < side:
                g.add_edge(p, (r + 1) * side + c, bandwidth=0.5)
    return g


def smooth_field(field, xi):
    """Isotropic Gaussian smoothing to real-space correlation length ~xi, via an
    FFT low-pass (dependency-free). xi<=0 returns the field unchanged (white)."""
    if xi <= 0:
        return field
    ny, nx = field.shape
    fy = np.fft.fftfreq(ny)[:, None]
    fx = np.fft.fftfreq(nx)[None, :]
    k2 = fy ** 2 + fx ** 2
    filt = np.exp(-0.5 * (2 * np.pi) ** 2 * k2 * xi ** 2)
    return np.fft.ifft2(np.fft.fft2(field) * filt).real


def landscape(side, amp, lam, kind, rng=None, corr=0.0):
    """Return rho(r,c) with mean == RHO_BG.
      kind='uniform' -> flat.
      kind='stripes' -> zero-mean sinusoidal walls along columns (anisotropic).
      kind='random'  -> zero-mean ISOTROPIC field, std==amp, correlation length `corr`
                        (corr=0 white = steepest gradients; larger corr = smoother =
                        shallower gradients at the SAME amplitude). Amplitude is fixed
                        by renormalizing std AFTER smoothing, so `corr` varies gradient
                        content independently of amplitude -- the sigma_tau axis."""
    rho = np.full((side, side), RHO_BG, float)
    if kind == "uniform" or amp == 0.0:
        return rho
    if kind == "stripes":
        cc = np.arange(side)
        pattern = amp * np.sin(2 * np.pi * cc / lam)      # zero spatial mean over full periods
        pattern = pattern - pattern.mean()
        rho = rho + pattern[None, :]
    elif kind == "random":
        if rng is None:
            rng = np.random.default_rng(0)
        field = rng.uniform(-1.0, 1.0, size=(side, side))
        field = smooth_field(field, corr)                 # set correlation length
        field = field - field.mean()                      # exact zero mean
        sd = field.std()
        if sd > 1e-12:
            field = field / sd                            # renormalize -> std == amp below
        rho = rho + amp * field                           # amplitude fixed; gradient set by corr
    np.clip(rho, 0.0, None, out=rho)                       # rho >= 0 (B4)
    return rho


def run_once(side, amp, lam, kind, scale, seed, corr=0.0, coeffs=COEFFS, max_steps=MAX_STEPS):
    """Seed a localized source at center; spread commitment through the rho
    landscape (scaled by `scale`); measure reach and survival."""
    rng = np.random.default_rng(seed)
    g = build_grid(side)
    rho0 = landscape(side, amp, lam, kind, rng=rng, corr=corr) * scale
    sv = StateVector()
    for r in range(side):
        for c in range(side):
            p = r * side + c
            # tiny noise breaks exact Sigma ties structurally (not load-bearing)
            jitter = rng.normal(0, 1e-3)
            sv[p] = NodeState(rho=float(max(0.0, rho0[r, c] + jitter)),
                              orientation=rng.normal(size=2))
    # localized source: a 3x3 active cluster at the center
    ctr = side // 2
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            sv[(ctr + dr) * side + (ctr + dc)].active = True
    committed = set()

    class Rec:
        def log_commit(self, t, u, v): committed.add(v)
        def snapshot(self, t, state): pass
    rec = Rec()

    steps_run = 0
    for t in range(1, max_steps + 1):
        n = step(sv, g, coeffs, strata=assign_stratum_ids(sv, g), recorder=rec, t=t)
        steps_run = t
        if n == 0:
            break

    if committed:
        rc = np.array([(v // side, v % side) for v in committed], float)
        dr = rc[:, 0] - ctr        # displacement ALONG stripes (within a column) -> troughs conduct
        dc = rc[:, 1] - ctr        # displacement ACROSS stripes (crossing walls) -> the gap direction
        d = np.hypot(dr, dc)
        reach_rms = float(np.sqrt((d ** 2).mean()))
        reach_max = float(d.max())
        reach_row = float(np.sqrt((dr ** 2).mean()))   # along-channel (parallel to walls)
        reach_col = float(np.sqrt((dc ** 2).mean()))   # across-wall (the mass direction)
    else:
        reach_rms = reach_max = reach_row = reach_col = 0.0
    return dict(n_committed=len(committed), reach_rms=reach_rms, reach_max=reach_max,
                reach_row=reach_row, reach_col=reach_col, steps=steps_run)


def summarize(side, amp, lam, kind, scale, seeds, corr=0.0, coeffs=COEFFS, max_steps=MAX_STEPS):
    rows = [run_once(side, amp, lam, kind, scale, s, corr=corr, coeffs=coeffs,
                     max_steps=max_steps) for s in seeds]
    agg = {k: float(np.mean([r[k] for r in rows])) for k in rows[0]}
    agg["reach_rms_sd"] = float(np.std([r["reach_rms"] for r in rows]))
    return agg


def main():
    seeds = list(range(8))
    print("=" * 78)
    print("E1 -- mass from structured participation (H2 on the certified substrate)")
    print(f"grid {SIDE}x{SIDE}, coeffs kc/ks/kg=1, rho_star={COEFFS.rho_star}, "
          f"rho_bg={RHO_BG}, ext_thr={COEFFS.extinction_threshold}, seeds={len(seeds)}")
    print("=" * 78)

    # --- Test 1: patterned vs uniform at matched mean, sweep gradient content ---
    print("\n[1] REACH vs GRADIENT  (uniform control, then stripes; matched mean)")
    print(f"{'arm':<22}{'amp':>6}{'lam':>6}{'n_commit':>10}{'reach_rms':>11}"
          f"{'reach_max':>11}{'steps':>8}")
    base = summarize(SIDE, 0.0, 0, "uniform", 1.0, seeds)
    print(f"{'uniform':<22}{0.0:>6}{'-':>6}{base['n_committed']:>10.1f}"
          f"{base['reach_rms']:>11.2f}{base['reach_max']:>11.2f}{base['steps']:>8.1f}")
    grad_rows = []
    for amp in (0.1, 0.2, 0.3, 0.4):
        for lam in (4, 8):
            a = summarize(SIDE, amp, lam, "stripes", 1.0, seeds)
            grad_content = (amp ** 2) / (lam ** 2)   # ~ <(d rho)^2>, arbitrary units
            grad_rows.append((amp, lam, grad_content, a))
            print(f"{'stripes':<22}{amp:>6}{lam:>6}{a['n_committed']:>10.1f}"
                  f"{a['reach_rms']:>11.2f}{a['reach_max']:>11.2f}{a['steps']:>8.1f}")

    # --- Test 2: amplitude-invariance, EXTINCTION-IMMUNE (the sigma_tau discriminator) ---
    # Rescale the WHOLE rho landscape by alpha. Under sigma_tau (log-derivative,
    # amplitude-invariant), the mass -> pat/uni reach DEFICIT is constant across alpha.
    # Under an absolute-gradient confinement (Str keys on absolute rho), the deficit
    # DEEPENS with alpha. The v1 Test 2 was confounded: alpha=2 tripped the extinction
    # cliff. Here we turn extinction OFF and measure front reach at a FIXED step budget
    # on a larger grid (front-velocity proxy) so alpha cannot kill fronts -- pure
    # propagation resistance. Isotropic (random) patterning is used: it is the
    # mass-relevant case (stripes give a crystal, not a mass).
    NOEXT = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5, increment=1.0,
                        extinction_threshold=None)
    SIDE2, TMEAS, CORR2 = 61, 30, 0.0   # corr=0 white = the CONFINING regime (Test 4b)
    print(f"\n[2] AMPLITUDE-INVARIANCE (extinction OFF, {SIDE2}x{SIDE2}, {TMEAS} steps, "
          f"isotropic amp=0.3 corr={CORR2})")
    print(f"{'alpha':>7}{'uni_reach':>11}{'pat_reach':>11}{'deficit':>9}{'uni_ncmt':>10}{'pat_ncmt':>10}")
    for alpha in (0.5, 1.0, 2.0):
        u = summarize(SIDE2, 0.0, 0, "uniform", alpha, seeds, coeffs=NOEXT, max_steps=TMEAS)
        p = summarize(SIDE2, 0.3, 0, "random", alpha, seeds, corr=CORR2, coeffs=NOEXT, max_steps=TMEAS)
        deficit = p["reach_rms"] / u["reach_rms"] if u["reach_rms"] > 0 else float("nan")
        print(f"{alpha:>7}{u['reach_rms']:>11.2f}{p['reach_rms']:>11.2f}{deficit:>9.3f}"
              f"{u['n_committed']:>10.1f}{p['n_committed']:>10.1f}")
    print("   deficit CONSTANT across alpha -> sigma_tau (log-derivative) faithful;")
    print("   deficit DEEPENS with alpha    -> absolute-rho-gradient confinement, not sigma_tau.")

    # --- Test 2b: is the confinement an EXTINCTION effect? (single-variable paired) ---
    # Same grid, same white amp=0.3 field, same 30-step budget, in-flight regime.
    # ONLY extinction on/off differs. If the reach deficit vs uniform is present with
    # extinction ON and GONE with extinction OFF, the isotropic "mass" is worldline
    # termination at gradient peaks, NOT an intrinsic sigma_tau propagation gap.
    print(f"\n[2b] IS IT EXTINCTION?  (paired, {SIDE2}x{SIDE2}, {TMEAS} steps, white amp=0.3)")
    print(f"{'extinction':<12}{'uni_reach':>11}{'pat_reach':>11}{'deficit':>9}{'uni_ncmt':>10}{'pat_ncmt':>10}")
    for label, cf in (("ON (-2.0)", COEFFS), ("OFF", NOEXT)):
        u = summarize(SIDE2, 0.0, 0, "uniform", 1.0, seeds, coeffs=cf, max_steps=TMEAS)
        p = summarize(SIDE2, 0.3, 0, "random", 1.0, seeds, corr=0.0, coeffs=cf, max_steps=TMEAS)
        deficit = p["reach_rms"] / u["reach_rms"] if u["reach_rms"] > 0 else float("nan")
        print(f"{label:<12}{u['reach_rms']:>11.2f}{p['reach_rms']:>11.2f}{deficit:>9.3f}"
              f"{u['n_committed']:>10.1f}{p['n_committed']:>10.1f}")
    print("   deficit<1 with ON, ~1 with OFF -> confinement IS extinction (worldline")
    print("   termination), not a sigma_tau gap. deficit<1 in BOTH -> real propagation gap.")

    # --- Test 3: ANISOTROPY -- is the mass a directional gap across the gradient? ---
    # Stripes vary along columns c: high-rho WALLS and low-rho TROUGHS are vertical.
    # reach_row = spread ALONG a channel (parallel to walls, should be free).
    # reach_col = spread ACROSS walls (the sigma_tau gradient direction, the mass dir).
    # Uniform arm: reach_row == reach_col (isotropic). Patterned arm: reach_col < reach_row
    # would be an ANISOTROPIC mass -- a gap across the gradient, conduction along it.
    print("\n[3] ANISOTROPY  (reach along-channel vs across-wall; lam=8)")
    print(f"{'arm':<14}{'amp':>6}{'reach_row':>11}{'reach_col':>11}{'col/row':>9}{'n_commit':>10}")
    ui = summarize(SIDE, 0.0, 0, "uniform", 1.0, seeds)
    aniso_u = ui["reach_col"] / ui["reach_row"] if ui["reach_row"] > 0 else float("nan")
    print(f"{'uniform':<14}{0.0:>6}{ui['reach_row']:>11.2f}{ui['reach_col']:>11.2f}"
          f"{aniso_u:>9.3f}{ui['n_committed']:>10.1f}")
    for amp in (0.2, 0.3, 0.4):
        pi = summarize(SIDE, amp, 8, "stripes", 1.0, seeds)
        aniso = pi["reach_col"] / pi["reach_row"] if pi["reach_row"] > 0 else float("nan")
        print(f"{'stripes':<14}{amp:>6}{pi['reach_row']:>11.2f}{pi['reach_col']:>11.2f}"
              f"{aniso:>9.3f}{pi['n_committed']:>10.1f}")

    # --- Test 4: ISOTROPIC patterning -- the decisive sigma_tau test ---
    # A random (isotropic, no preferred direction) zero-mean rho field at matched mean.
    # If an isotropic patterned condensate gives an ISOTROPIC reach DEFICIT that scales
    # with gradient content (amp), that is a sigma_tau-like Lorentz-scalar mass -> H2
    # rescued on the native field. If reach is unchanged/up or the deficit does not
    # scale, the native rho field does not carry a sigma_tau mass.
    # density = n_committed / (pi * reach_rms^2). CONFOUND SEPARATOR:
    #   reach shrinks + density HOLDS  -> confinement == real isotropic mass gap.
    #   reach shrinks + density DROPS  -> extinction (sparse holes), not a mass.
    print("\n[4] ISOTROPIC (random-field) patterning  (matched mean; decisive)")
    print(f"{'arm':<12}{'amp':>6}{'reach_rms':>11}{'col/row':>9}{'n_commit':>10}"
          f"{'density':>9}{'reach/uni':>10}")
    ru = summarize(SIDE, 0.0, 0, "uniform", 1.0, seeds)
    dens_u = ru["n_committed"] / (np.pi * ru["reach_rms"] ** 2)
    print(f"{'uniform':<12}{0.0:>6}{ru['reach_rms']:>11.2f}"
          f"{ru['reach_col']/ru['reach_row']:>9.3f}{ru['n_committed']:>10.1f}"
          f"{dens_u:>9.3f}{1.0:>10.3f}")
    for amp in (0.15, 0.3, 0.45):
        rr = summarize(SIDE, amp, 0, "random", 1.0, seeds)
        iso = rr["reach_col"] / rr["reach_row"] if rr["reach_row"] > 0 else float("nan")
        rel = rr["reach_rms"] / ru["reach_rms"] if ru["reach_rms"] > 0 else float("nan")
        dens = rr["n_committed"] / (np.pi * rr["reach_rms"] ** 2) if rr["reach_rms"] > 0 else 0.0
        print(f"{'random':<12}{amp:>6}{rr['reach_rms']:>11.2f}{iso:>9.3f}"
              f"{rr['n_committed']:>10.1f}{dens:>9.3f}{rel:>10.3f}")

    # --- Test 4b: CORRELATION-LENGTH sweep at FIXED amplitude (the missing axis) ---
    # sigma_tau mass ~ gradient content <(d ln rho)^2>, which at FIXED amplitude falls
    # as the field smooths (corr up -> shallower gradients). Test 4 only swept amplitude
    # (corr=0 white). Here amp is fixed and corr varies: predict the reach deficit SHRINKS
    # toward 1 as corr grows. Deficit tracking 1/corr (not flat) == mass tracks gradient
    # content, not amplitude alone -- the second axis of the sigma_tau claim.
    print("\n[4b] GRADIENT CONTENT via CORRELATION LENGTH  (fixed amp=0.3, isotropic)")
    print(f"{'arm':<12}{'corr':>6}{'reach_rms':>11}{'density':>9}{'reach/uni':>10}{'grad~amp/corr':>15}")
    rb = summarize(SIDE, 0.0, 0, "uniform", 1.0, seeds)
    db = rb["n_committed"] / (np.pi * rb["reach_rms"] ** 2)
    print(f"{'uniform':<12}{'-':>6}{rb['reach_rms']:>11.2f}{db:>9.3f}{1.0:>10.3f}{'-':>15}")
    for cval in (0.0, 1.5, 3.0, 6.0):
        rr = summarize(SIDE, 0.3, 0, "random", 1.0, seeds, corr=cval)
        rel = rr["reach_rms"] / rb["reach_rms"] if rb["reach_rms"] > 0 else float("nan")
        dens = rr["n_committed"] / (np.pi * rr["reach_rms"] ** 2) if rr["reach_rms"] > 0 else 0.0
        grad = 0.3 / cval if cval > 0 else float("inf")
        gtxt = "inf(white)" if cval == 0 else f"{grad:.3f}"
        print(f"{'random':<12}{cval:>6}{rr['reach_rms']:>11.2f}{dens:>9.3f}{rel:>10.3f}{gtxt:>15}")
    print("   deficit SHRINKS toward 1 as corr grows -> mass tracks gradient content (sigma_tau).")
    print("   deficit FLAT vs corr                   -> mass tracks amplitude only, not gradient.")

    # --- Verdict scaffold ---
    print("\n" + "=" * 78)
    print("READINGS:")
    pat_all = [a for (_, _, _, a) in grad_rows]
    mean_pat_reach = np.mean([a["reach_rms"] for a in pat_all])
    print(f"  uniform reach_rms      = {base['reach_rms']:.2f}  "
          f"(n_committed {base['n_committed']:.0f})")
    print(f"  mean patterned reach   = {mean_pat_reach:.2f}")
    print("  -> H2-mechanism reading: patterned reach < uniform reach ==> structure")
    print("     impedes spread == effective mass from gradient content.")
    print("  -> monotone reach-deficit vs grad_content (amp^2/lam^2) supports sigma_tau form.")
    print("  -> Test[2] ratio CONSTANT across alpha ==> amplitude-invariant (sigma_tau faithful);")
    print("     ratio DRIFTS with alpha ==> certified Sigma is amplitude-SENSITIVE, sigma_tau")
    print("     is an idealization the raw substrate does not honor.")
    print("  CONFOUND GUARD: if patterned n_committed collapses toward 0, the 'mass' is")
    print("     extinction, not a gap -- read reach only where fronts survive.")
    print("=" * 78)


if __name__ == "__main__":
    main()
