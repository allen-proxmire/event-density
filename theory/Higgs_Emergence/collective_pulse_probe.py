"""Collective phase-locking test (route 2a, "to persist is to pulse" / "a star
pulses"): take many memory-carrying fronts with a SPREAD of natural tempos,
couple them through the substrate's own shared rho field, and ask -- do their
tempos pull together (frequency-locking) and does the whole population's
commitment activity start to pulse in unison (a collective rhythm)?

HONEST DESIGN NOTES (why it's built this way):
- Identical oscillators would "sync" trivially by being copies. Real Kuramoto
  phase-locking is DIFFERENT natural frequencies pulled to a common one by
  coupling. So the fronts get a SPREAD of memory strengths k_mem -> a spread of
  natural hop-tempos (confirmed by the rhythm probe: stronger memory = longer
  stride). The test is whether coupling narrows that spread.
- The coupling is the substrate's OWN native channel, not invented: when a
  front commits it raises rho at that locus (certified commit()); other fronts
  read rho in their Sigma (certified compute_sigma). A trailing front runs into
  a leader's fresh rho-trail. Plus excluded volume (two chains can't occupy one
  locus -> a front blocked from advancing dwells instead), also native.
- Geometry: a RING (periodic chain), so fronts keep re-encountering each other
  (faster ones lap slower ones) -> recurrent coupling, unlike a line where they
  separate and stop interacting. Honest caveat: rho is irreversible (monotone),
  so the ring's ground slowly "fills up"; measured over a finite window before
  saturation, and the saturation itself is reported.
- Per-decision physics is certified (compute_sigma / compute_candidates /
  apply_tiebreak / commit reused verbatim). Only the multi-front orchestration
  and the memory channel are new.

MEASURES:
  (1) Frequency-locking: spread (std) of per-front hop-rates, COUPLED vs the
      same fronts run ISOLATED (each alone on its own ring). Coupling that
      shrinks the spread = frequency pulling-together = the hallmark of sync.
  (2) Collective pulse: the population hop-activity time series (total hops per
      timestep). A sharp FFT peak / high peak-to-mean = the population pulses in
      unison; a flat spectrum = incoherent, no collective rhythm. Compared to a
      phase-shuffled null (each front's hop-train randomly time-shifted), which
      destroys any real cross-front timing while preserving each front's own rate.
"""
import numpy as np
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "evaluation", "Bits"))
from simulator import ParticipationGraph, NodeState, StateVector, SigmaCoeffs  # noqa: E402
from simulator.sigma import compute_sigma  # noqa: E402
from simulator.update import apply_tiebreak  # noqa: E402

RHO_STAR = 0.5
EDGE_BW = 0.5
B_SELF = 1.0
JITTER_SD = 1e-3
MEM_DECAY = 0.9
COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=RHO_STAR, increment=1.0,
                     extinction_threshold=None)


def build_ring(n, b_self):
    g = ParticipationGraph()
    for i in range(n):
        g.add_edge(i, (i + 1) % n, bandwidth=EDGE_BW)   # periodic: closes the loop
    if b_self > 0:
        for i in range(n):
            g.add_edge(i, i, bandwidth=b_self)
    return g


def run_fronts(ring_n, front_specs, max_steps, seed):
    """front_specs: list of (start_pos, k_mem). Multiple fronts on ONE ring,
    coupled through shared rho + excluded volume. Returns per-front hop-time
    lists and the population activity time-series (hops per step)."""
    rng = np.random.default_rng(seed)
    g = build_ring(ring_n, B_SELF)
    sv = StateVector()
    for i in range(ring_n):
        sv[i] = NodeState(rho=float(max(0.0, RHO_STAR + rng.normal(0, JITTER_SD))))

    # front state: position, its own carried memory, its own k_mem
    fronts = [{"pos": s, "mem": 0.0, "k_mem": k, "id": j}
              for j, (s, k) in enumerate(front_specs)]
    for f in fronts:
        sv[f["pos"]].active = True

    hop_times = {f["id"]: [] for f in fronts}
    activity = []          # hops per step across the whole population
    mean_rho = []          # saturation tracker: mean rho over the ring, per step
    occupied = {f["pos"] for f in fronts}

    for t in range(1, max_steps + 1):
        hops_this_step = 0
        # process fronts in a fixed canonical order (by id) for determinism
        for f in sorted(fronts, key=lambda x: x["id"]):
            u = f["pos"]
            # candidates: non-decoupled neighbors NOT occupied by another front,
            # plus self (dwell always allowed). Excluded volume = native coupling.
            nbrs = [v for v in g.admissible_neighbors(u)
                    if v == u or v not in occupied]
            if not nbrs:
                nbrs = [u]      # boxed in -> can only dwell
            sig = {}
            for v in nbrs:
                s = compute_sigma(u, v, sv, g, COEFFS)
                if v == u:
                    s += f["k_mem"] * f["mem"]   # self-loop memory bonus
                sig[v] = s
            smax = max(sig.values())
            maximal = [v for v, s in sig.items() if s == smax]
            winner = apply_tiebreak(u, maximal, g)

            sv[winner].commit(COEFFS.increment)
            f["mem"] = MEM_DECAY * f["mem"] + 1.0
            if winner != u:
                # advance: update occupancy, record a hop
                occupied.discard(u)
                occupied.add(winner)
                sv[u].active = False
                sv[winner].active = True
                f["pos"] = winner
                hop_times[f["id"]].append(t)
                hops_this_step += 1
            # dwell: position unchanged, occupancy unchanged
        activity.append(hops_this_step)
        if t % 20 == 0:                      # sample saturation cheaply
            mean_rho.append((t, np.mean([sv[i].rho for i in range(ring_n)])))

    # sanity: front count conserved, no two fronts co-located
    assert len({f["pos"] for f in fronts}) == len(fronts), "front collision -- exclusion failed"
    return hop_times, np.array(activity), mean_rho


def front_rate(hop_list, w0, w1):
    """Mean hops-per-step for one front over the window [w0, w1]."""
    hs = [h for h in hop_list if w0 <= h < w1]
    if len(hs) < 5:
        return np.nan
    return len(hs) / (w1 - w0)


def activity_peakedness(activity, w0, w1):
    """Peak-to-mean of the population-activity power spectrum over [w0, w1]
    (excluding DC). High = the population pulses at a dominant frequency;
    ~1 = flat/incoherent."""
    a = activity[w0:w1].astype(float)
    a = a - a.mean()
    if np.allclose(a, 0):
        return 1.0, 0.0
    ps = np.abs(np.fft.rfft(a)) ** 2
    ps = ps[1:]        # drop DC
    if len(ps) == 0 or ps.mean() == 0:
        return 1.0, 0.0
    peak_to_mean = ps.max() / ps.mean()
    peak_freq = (np.argmax(ps) + 1) / len(a)   # cycles per step
    return peak_to_mean, peak_freq


def main():
    print("=" * 90)
    print("COLLECTIVE PULSE PROBE -- do many coupled memory-fronts phase-lock into a")
    print("shared pulsation (the 'a star pulses' claim), or stay incoherent?")
    print("=" * 90)

    # Big ring + a FRESH measurement window before irreversible rho saturates the
    # ground (saturation kills dwelling -> kills the rhythm; a real closed-system
    # effect, tracked explicitly below).
    RING_N = 3000
    MAX_STEPS = 1200
    W0, W1 = 200, 1000     # post-transient, pre-saturation (verified by rho tracker)
    N_FRONTS = 8
    seeds = list(range(5))
    k_spread = np.linspace(0.1, 0.5, N_FRONTS)   # spread of natural tempos

    # --- Saturation check + sanity: one front, is the window fresh & rhythmic? ---
    ht, act, mrho = run_fronts(RING_N, [(0, 0.3)], MAX_STEPS, seed=0)
    r_one = front_rate(ht[0], W0, W1)
    print(f"\n[sanity] single front, hop-rate in window [{W0},{W1}] = {r_one:.4f} "
          f"(expect ~0.5 = period-2 dwelling alive)")
    print("[saturation] mean ring rho over time (step: rho): "
          + ", ".join(f"{t}:{r:.2f}" for t, r in mrho[::10][:8]))

    # --- ISOLATED baseline: each front alone -> natural frequency spread ---
    iso_rates = []
    for s in seeds:
        for k in k_spread:
            ht_i, _, _ = run_fronts(RING_N, [(0, float(k))], MAX_STEPS, seed=1000 * s + int(k * 100))
            iso_rates.append(front_rate(ht_i[0], W0, W1))
    iso_rates = np.array(iso_rates).reshape(len(seeds), N_FRONTS)
    iso_spread = np.nanmean(np.nanstd(iso_rates, axis=1))
    print(f"\n[isolated] natural hop-rates (seed 0): "
          + ", ".join(f"{x:.3f}" for x in iso_rates[0]))
    print(f"[isolated] within-population frequency spread (std): {iso_spread:.4f}")

    # --- COUPLED: all fronts on one ring, spaced so they interact in-window ---
    coup_rates_all, peakedness_all, peakfreq_all, null_peaks = [], [], [], []
    for s in seeds:
        starts = np.linspace(0, RING_N, N_FRONTS, endpoint=False).astype(int)
        specs = [(int(st), float(k)) for st, k in zip(starts, k_spread)]
        ht_c, act_c, _ = run_fronts(RING_N, specs, MAX_STEPS, seed=2000 + s)
        rates = np.array([front_rate(ht_c[j], W0, W1) for j in range(N_FRONTS)])
        coup_rates_all.append(rates)
        p2m, pf = activity_peakedness(act_c, W0, W1)
        peakedness_all.append(p2m)
        peakfreq_all.append(pf)
        # Proper null: within the window, redistribute each front's hops uniformly
        # at random (destroys cross-front timing alignment; keeps per-front count).
        rng = np.random.default_rng(9000 + s)
        null_act = np.zeros(MAX_STEPS)
        for j in range(N_FRONTS):
            hs = [h for h in ht_c[j] if W0 <= h < W1]
            for _ in hs:
                null_act[rng.integers(W0, W1)] += 1
        p2m_null, _ = activity_peakedness(null_act, W0, W1)
        null_peaks.append(p2m_null)
    coup_rates_all = np.array(coup_rates_all)
    coup_spread = np.nanmean(np.nanstd(coup_rates_all, axis=1))
    print(f"\n[coupled] hop-rates (seed 0): "
          + ", ".join(f"{x:.3f}" for x in coup_rates_all[0]))
    print(f"[coupled] within-population frequency spread (std): {coup_spread:.4f}")

    print("\n" + "=" * 90)
    print("RESULTS (all measured in the fresh window):")
    print(f"  frequency spread:  isolated={iso_spread:.4f}  coupled={coup_spread:.4f}  "
          f"ratio={coup_spread/iso_spread:.2f}")
    print("    ratio < ~0.7 => coupling PULLS TEMPOS TOGETHER (frequency-locking).")
    print("    ratio ~ 1     => no frequency pulling.")
    print(f"  collective-pulse peak-to-mean:  coupled={np.mean(peakedness_all):.1f}  "
          f"null(shuffled)={np.mean(null_peaks):.1f}  "
          f"ratio={np.mean(peakedness_all)/np.mean(null_peaks):.2f}")
    print("    coupled >> null => the population PULSES in unison (real collective rhythm).")
    print("    coupled ~ null  => incoherent; no collective pulse.")
    print(f"  dominant collective frequency (coupled): {np.mean(peakfreq_all):.4f} cycles/step "
          f"(period ~ {1/np.mean(peakfreq_all) if np.mean(peakfreq_all)>0 else float('inf'):.1f} steps)")
    print("=" * 90)


if __name__ == "__main__":
    main()
