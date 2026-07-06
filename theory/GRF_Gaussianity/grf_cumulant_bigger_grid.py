"""Extension run: 128^2 grid so B=16 has the sampling B=8 had at 64^2.
Decides whether the scale-invariant skewness persists at B=16 (deeper
non-Gaussianity) or decays (Gaussianization scale ~12-16 cells, which would
BOUND rather than kill the GRF hypothesis: valid only above that filter scale).
"""
import numpy as np
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import grf_cumulant_test_probe as G

G.SIDE = 128
G.MAX_STEPS = 4000

def main():
    rng = np.random.default_rng(4048)
    n_seeds, n_surr_each = 4, 6
    print(f"128x128 extension, {n_seeds} seeds")
    fields = [G.run_deposit(s + 100) for s in range(n_seeds)]
    xis = [G.corr_length(f) for f in fields]
    print(f"xi = {np.mean(xis):.2f} +/- {np.std(xis):.2f} cells")
    print(f"{'B':>3} {'stat':>5} {'real(mean)':>11} {'null(mean)':>11} {'null(sd)':>9} {'z':>8}")
    for B in (8, 16, 32):
        real = np.array([G.stats_of(G.block_mean(f, B)) for f in fields])
        null = []
        for f in fields:
            for _ in range(n_surr_each):
                null.append(G.stats_of(G.block_mean(G.phase_surrogate(f, rng), B)))
        null = np.array(null)
        for k, name in enumerate(("g1", "g2", "T3")):
            r_m = real[:, k].mean()
            n_m, n_sd = null[:, k].mean(), null[:, k].std()
            z = (r_m - n_m) / (n_sd / np.sqrt(n_seeds) + 1e-15)
            print(f"{B:>3} {name:>5} {r_m:>11.4f} {n_m:>11.4f} {n_sd:>9.4f} {z:>8.1f}")
        print()

if __name__ == "__main__":
    main()
