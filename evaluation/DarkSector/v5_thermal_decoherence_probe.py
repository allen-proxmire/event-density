"""Thermal-decoherence probe (dark-sector / superfluid-relic program).

QUESTION: is the condensation boundary THERMAL (set by velocity dispersion) rather than
set by acceleration? The galaxy=MOND / cluster=CDM split needs THERMAL: galaxies are cold
(ordered disks, low dispersion) -> condense -> MOND; clusters are hot (high dispersion) ->
decohere -> CDM. If decoherence tracked acceleration instead, clusters (also sub-a0) would
wrongly condense.

ED-NATIVE DECOHERENCE (not put in by hand): P11 commitment randomizes phases ("un-selected
channels' phase content randomized" -- Paper_087 P11). A relic commits when it ENCOUNTERS
another (interaction -> single-channel collapse). Kinetic theory: encounter rate ~ relative
velocity. So the decoherence rate is DERIVED from the motion, and scales with velocity
dispersion = TEMPERATURE. Acceleration does not enter.

MODEL:
  * N relics in a periodic box, moving ballistically with velocity dispersion sigma_v (= T).
  * V5 coherence aligns phases within reach: dphi_i = K sum_j exp(-r_ij/ell) sin(phi_j-phi_i) dt
    (constant coupling K -- the coherence glue does NOT depend on temperature).
  * P11 decoherence: relic i commits (phi_i -> random) at rate gamma * sum_{j in reach} |v_i-v_j|/ell
    -- the kinetic encounter rate. This is the ONLY noise; it is derived, thermal.
  * Order parameter C = sum w cos(dphi) / sum w  (1 condensed, 0 dispersed).

TEST: sweep sigma_v (temperature). Thermal boundary => C high at low sigma_v (cold/galaxy),
low at high sigma_v (hot/cluster), and the decoherence rate ~ sigma_v (confirming thermal).
"""
import numpy as np


def run(sigma_v, N=60, L=3.0, ell=1.0, K=1.5, gamma=1.0, steps=4500, dt=0.02, burn=0.5, seed=0):
    rng = np.random.default_rng(seed)
    pos = rng.uniform(0.0, L, (N, 3))
    vel = rng.normal(0.0, sigma_v, (N, 3))
    phi = rng.uniform(0.0, 2 * np.pi, N)
    Cacc, ratacc = [], []
    for t in range(steps):
        pos = (pos + vel * dt) % L
        d = pos[:, None, :] - pos[None, :, :]
        d -= L * np.round(d / L)                       # minimum image
        r = np.linalg.norm(d, axis=2)
        W = np.exp(-r / ell)
        np.fill_diagonal(W, 0.0)
        # V5 alignment (constant coupling)
        phi = phi + K * np.sum(W * np.sin(phi[None, :] - phi[:, None]), axis=1) * dt
        # P11 decoherence: kinetic encounter rate ~ |relative velocity| over neighbors in reach
        close = (r < ell) & (r > 0.0)
        relv = np.linalg.norm(vel[:, None, :] - vel[None, :, :], axis=2)
        rate = gamma * np.sum(close * relv, axis=1) / ell
        commit = rng.random(N) < np.clip(rate * dt, 0, 1)
        if commit.any():
            phi[commit] = rng.uniform(0.0, 2 * np.pi, int(commit.sum()))
        if t > steps * burn:
            cosd = np.cos(phi[:, None] - phi[None, :])
            Cacc.append(float(np.sum(W * cosd) / (W.sum() + 1e-12)))
            ratacc.append(float(rate.mean()))
    return np.mean(Cacc), np.mean(ratacc)


def main():
    print("Thermal-decoherence probe: coherence C vs velocity dispersion sigma_v (=T).")
    print("V5 aligns (constant K); P11 decoheres on encounters (rate DERIVED, ~ relative velocity).\n")
    sig = [0.05, 0.1, 0.2, 0.35, 0.5, 0.75, 1.0, 1.5, 2.5, 4.0]
    rows = [run(s, seed=7) for s in sig]
    C = [c for c, _ in rows]
    rate = [rt for _, rt in rows]
    print("  sigma_v: " + "  ".join(f"{s:5.2f}" for s in sig))
    print("  C      : " + "  ".join(f"{c:5.2f}" for c in C))
    print("  dec.rate: " + " ".join(f"{r:5.2f}" for r in rate))

    # thermal scaling check: is the decoherence rate ~ sigma_v? (log-log slope)
    lo, hi = 1, len(sig) - 1
    slope = np.polyfit(np.log(sig[lo:hi]), np.log(np.array(rate[lo:hi]) + 1e-9), 1)[0]

    print("\n" + "=" * 72)
    print("READ:")
    print(f"  cold (sigma_v=0.05, ~galaxy disk): C = {C[0]:.2f}  -> {'CONDENSED' if C[0] > 0.7 else 'no'}")
    print(f"  hot  (sigma_v=4.0,  ~cluster):     C = {C[-1]:.2f}  -> {'DISPERSED' if C[-1] < 0.3 else 'no'}")
    print(f"  decoherence-rate scaling with sigma_v: exponent ~ {slope:.2f}  "
          f"(~1 => kinetic/THERMAL, set by velocity not acceleration)")
    thermal = C[0] > 0.7 and C[-1] < 0.3 and 0.7 < slope < 1.4
    print(f"  VERDICT: {'THERMAL boundary confirmed' if thermal else 'not a clean thermal boundary'} "
          f"-- cold condenses, hot disperses, noise ~ velocity dispersion.")
    print("  (galaxy disks vs clusters differ in sigma_v by ~20-100x, so a transition anywhere")
    print("   in this range gives galaxies=MOND / clusters=CDM. Acceleration does not enter.)")
    print("=" * 72)


if __name__ == "__main__":
    main()
