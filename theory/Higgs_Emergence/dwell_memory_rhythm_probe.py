"""Route #2 from Parked_Routes_And_Open_Threads.md ("waves have memory"): does a
chain's finite memory produce a temporal RHYTHM -- regular, clockwork hops (a
real emergent frequency, the seed of wave behavior) -- or just stochastic
slowing (stable average, but random individual hop times, no rhythm)?

WHY THIS SPECIFIC QUESTION, HONESTLY. A wave equation is second-order in time
(memory of one derivative); finite memory is what turns diffusion into
oscillation. But in ED a front CANNOT reverse (P11 irreversibility: rho only
increases, fronts advance or dwell, never go backward), so a single particle's
POSITION cannot oscillate spatially -- genuine spatial waves are structurally
off the table. What CAN emerge is a temporal rhythm: if memory makes the front
hop at REGULAR intervals (dwell-dwell-dwell-HOP repeating on a fixed period),
that regular stride is a real frequency/wavelength born from memory -- the
honest, testable core of "waves have memory" on this substrate. Full QM phase
waves live in the phase/polarity channel, which the certified Sigma does not
read (the same wall the mass work already hit); this probe therefore tests the
one wave-adjacent thing this substrate CAN show, and says so.

THE DISCRIMINANT. Coefficient of variation (CV = std/mean) of the inter-hop
intervals at steady state:
  CV -> 0  : clockwork-regular hops -- a genuine emergent temporal rhythm
             (a stable stride length = a frequency = wave-adjacent). Strong.
  CV ~ 1   : exponential/Poisson intervals -- stable MEAN but memoryless-looking
             individual hop times; slowing without rhythm. Honest negative.
  0 < CV < 1: partial rhythm.
Note the control (memoryless, k_mem=0) is ballistic: it hops every step, so its
interval is trivially always 1 (CV=0 but meaningless -- no dwelling). The
meaningful test is a memory regime with mean interval clearly > 1: THERE, is
CV low (real rhythm) or ~1 (random)?

GROUNDING. Reuses the certified-based intrinsic-memory mechanism verbatim
(imported from dwell_intrinsic_memory_probe.py, itself built on the unmodified
certified Sigma/commit/tiebreak). Only new content is the interval analysis.
"""
import numpy as np
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dwell_intrinsic_memory_probe as dm  # noqa: E402

# Long chain so the front never hits the boundary within the step budget --
# we need steady-state hop statistics, not a truncated transient.
dm.CHAIN_LEN = 20000


def hop_intervals(trace, burn):
    """Inter-hop intervals (steps between successive position increases),
    from the steady-state portion only (after `burn` steps)."""
    pos = np.asarray(trace, dtype=float)
    hop_steps = np.where(np.diff(pos) > 0)[0]
    hop_steps = hop_steps[hop_steps > burn]
    if len(hop_steps) < 5:
        return np.array([])
    return np.diff(hop_steps)


def main():
    print("=" * 90)
    print("MEMORY RHYTHM PROBE (route #2, 'waves have memory') -- are memory-driven hops")
    print("clockwork-regular (an emergent temporal frequency) or random (no rhythm)?")
    print("=" * 90)

    MAX_STEPS = 15000
    BURN = 3000            # discard the transient; measure steady state only
    START = 10
    seeds = list(range(6))

    print(f"\nchain={dm.CHAIN_LEN}, steps={MAX_STEPS}, burn-in discarded={BURN}, seeds={len(seeds)}")
    print(f"\n{'k_mem':>6}{'decay':>7}{'mean_interval':>15}{'std':>8}{'CV':>7}{'n_hops':>9}  interpretation")
    print("-" * 90)

    for k_mem, decay in ((0.05, 0.95), (0.1, 0.9), (0.2, 0.9), (0.3, 0.9), (0.5, 0.9)):
        all_ints = []
        for s in seeds:
            r = dm.run_probe(s, k_mem, decay, max_steps=MAX_STEPS, start=START)
            ints = hop_intervals(r["trace"], BURN)
            if len(ints) > 0:
                all_ints.append(ints)
        if not all_ints:
            print(f"{k_mem:>6}{decay:>7}{'--':>15}{'--':>8}{'--':>7}{'0':>9}  (front never left transient)")
            continue
        ints = np.concatenate(all_ints)
        mean, std = ints.mean(), ints.std()
        cv = std / mean if mean > 0 else float("nan")
        if mean < 1.15:
            interp = "~ballistic (little dwelling; interval not meaningfully >1)"
        elif cv < 0.35:
            interp = "CLOCKWORK -> real emergent rhythm (wave-adjacent frequency)"
        elif cv > 0.8:
            interp = "Poisson-like -> stable mean, random hops, NO rhythm"
        else:
            interp = "partial rhythm"
        print(f"{k_mem:>6}{decay:>7}{mean:>15.3f}{std:>8.3f}{cv:>7.3f}{len(ints):>9}  {interp}")

    # Detail on one clear multi-step-interval regime: the actual interval histogram,
    # so the shape (sharp peak vs exponential tail) is visible, not just CV.
    print("\nInterval-distribution detail (k_mem=0.3, decay=0.9, seed 0, steady state):")
    r = dm.run_probe(0, 0.3, 0.9, max_steps=MAX_STEPS, start=START)
    ints = hop_intervals(r["trace"], BURN)
    if len(ints) > 0:
        vals, counts = np.unique(ints, return_counts=True)
        total = counts.sum()
        for v, c in zip(vals[:12], counts[:12]):
            bar = "#" * int(60 * c / counts.max())
            print(f"  interval={int(v):>3} steps: {100*c/total:>5.1f}%  {bar}")
        mean = ints.mean()
        # Poisson/geometric comparison: for a memoryless hop process with this mean,
        # intervals would be geometric with CV ~ sqrt(1 - p) / ... ~ close to 1.
        print(f"  (mean={mean:.2f}, CV={ints.std()/mean:.3f}; a memoryless process at this "
              f"mean would have CV near 1 and an exponential/geometric tail)")

    print("\n" + "=" * 90)
    print("READING: a sharply-peaked interval distribution with low CV = memory produces a")
    print("genuine, regular temporal stride -- a frequency emergent from finite memory, the")
    print("honest wave-adjacent core of the idea. A broad/exponential distribution with CV~1")
    print("= slowing without rhythm; the memory damps but does not clock. Either way, full")
    print("phase-wave (de Broglie) behavior is NOT testable here -- phase/polarity is not read")
    print("by the certified Sigma (same wall as the mass work); this tests temporal rhythm only.")
    print("=" * 90)


if __name__ == "__main__":
    main()
