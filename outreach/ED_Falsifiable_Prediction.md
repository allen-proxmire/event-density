# ED Falsifiable Prediction: Activity-Dependent Rotation Velocities

## The Prediction

Event Density predicts that galaxies with higher star-formation activity (specific star-formation rate, sSFR) will have systematically higher outer rotation velocities at fixed baryonic mass, with a shift of approximately 30--70 km/s between quiescent and actively star-forming galaxies of the same mass.

Neither MOND nor LCDM predict this effect. In MOND, the rotation velocity at fixed baryonic mass is determined entirely by the baryonic Tully-Fisher relation -- activity plays no role. In LCDM, the rotation curve is set by the dark matter halo, which is insensitive to current star-formation rate. ED uniquely predicts that the density-driven mobility mechanism couples galactic activity to the effective gravitational potential, producing a measurable velocity offset.

## Why This Is the Strongest Test

This prediction is clean because:

1. **It is unique to ED.** Both major alternatives (MOND and LCDM) predict zero activity dependence at fixed mass. A confirmed positive signal would be unexplained by either framework.
2. **It is quantitative.** The predicted shift (30--70 km/s) is well above measurement uncertainty for resolved rotation curves in nearby galaxies (~5--10 km/s).
3. **It is testable with existing data.** The combination of resolved HI rotation curves (SPARC, THINGS, LITTLE THINGS) with star-formation rate estimates (GALEX UV, WISE IR) provides the necessary observables for a sample of ~150 galaxies.
4. **It is falsifiable in both directions.** If the velocity offset is zero, ED's coupling mechanism is wrong. If the offset exists but in the wrong direction or at the wrong magnitude, the constitutive form requires revision.

## How to Reproduce It

1. Open the minimal demo notebook: [`ED_minimal_demo.ipynb`](ED_minimal_demo.ipynb)
2. The notebook demonstrates the core pipeline. For the galactic prediction specifically, the relevant analysis is in `edsim/phys/` and the data files in `data/ED-Data-12-Galactic-Activity/` through `data/ED-Data-14-Photometric-SFR/`.
3. The prediction emerges from the ED mobility law applied to the galactic regime: higher activity corresponds to higher effective density gradients, which modulate the degenerate mobility and shift the equilibrium rotation velocity.

## What Would Confirm It

- A statistically significant positive correlation (>3 sigma) between sSFR and outer rotation velocity residuals at fixed baryonic mass, across a mass-controlled sample of late-type galaxies.
- The magnitude of the velocity offset should fall within the 30--70 km/s range predicted by the ED constitutive parameters.

## What Would Refute It

- No detectable correlation between sSFR and rotation velocity at fixed baryonic mass (velocity offset consistent with zero).
- A correlation in the opposite direction (higher activity corresponding to lower rotation velocity).
- A correlation with the correct sign but at a magnitude incompatible with the ED parameter range (e.g., <5 km/s or >150 km/s).

## Observational Feasibility

This test requires no new instrumentation. The necessary data products already exist:

| Observable | Source |
|-----------|--------|
| Resolved rotation curves | SPARC (Lelli+ 2016), THINGS, LITTLE THINGS |
| Star-formation rates | GALEX (UV), WISE (IR), combined SED fitting |
| Baryonic masses | Stellar mass from photometry + HI gas mass from 21cm |

Upcoming surveys (Euclid, SKA pathfinders) will extend this test to larger samples and higher redshifts.

---

*This prediction is documented in ED-Data-12 and ED-Data-13 in the Event Density repository.*
