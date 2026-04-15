# ED-PHYS-01: ED as an Effective Diffusion Equation

## Regime

- Dimension: 2D
- Grid: 64 per axis (4096 points)
- D = 0.3, M_star = 0.2500, P0 = 0.01
- H = 0.0 (no participation)
- Predicted D_eff = D * M_star = 0.075000

## Experiment 1: Gaussian Spread

- Initial width: sigma_0 = 0.08
- Initial amplitude: A_0 = 0.03
- Variance at t=0: 0.012800
- Variance at t=0.3000: 0.095351
- Fitted D_eff = 0.069364
- Predicted D_eff = 0.075000
- Relative error: 0.0752 (7.52%)
- Variance fit R^2 = 0.998257

### Profile Comparison (Gaussian vs Heat Equation)

| Snapshot | Time | Rel L2 Error | Peak Error | Variance Error |
|----------|------|-------------|------------|----------------|
| 0 | 0.0000 | 0.0000e+00 | 9.7936e-03 | 1.0000e+00 |
| 1 | 0.0150 | 6.4538e-03 | 4.0059e-03 | 1.0262e+00 |
| 2 | 0.0299 | 1.0296e-02 | 8.3936e-03 | 1.0446e+00 |
| 3 | 0.0449 | 1.4000e-02 | 1.4160e-02 | 1.0584e+00 |
| 4 | 0.0598 | 1.7394e-02 | 1.9556e-02 | 1.0693e+00 |
| 5 | 0.0747 | 2.0392e-02 | 2.4272e-02 | 1.0781e+00 |
| 6 | 0.0897 | 2.3043e-02 | 2.8330e-02 | 1.0852e+00 |
| 7 | 0.1047 | 2.5458e-02 | 3.1823e-02 | 1.0906e+00 |
| 8 | 0.1196 | 2.7782e-02 | 3.4846e-02 | 1.0941e+00 |
| 9 | 0.1346 | 3.0168e-02 | 3.7483e-02 | 1.0957e+00 |
| 10 | 0.1495 | 3.2767e-02 | 3.9799e-02 | 1.0953e+00 |
| 11 | 0.1645 | 3.5704e-02 | 4.1850e-02 | 1.0927e+00 |
| 12 | 0.1794 | 3.9067e-02 | 4.3677e-02 | 1.0880e+00 |
| 13 | 0.1944 | 4.2906e-02 | 4.5315e-02 | 1.0813e+00 |
| 14 | 0.2093 | 4.7233e-02 | 4.6791e-02 | 1.0725e+00 |
| 15 | 0.2243 | 5.2034e-02 | 4.8126e-02 | 1.0620e+00 |
| 16 | 0.2392 | 5.7279e-02 | 4.9337e-02 | 1.0498e+00 |
| 17 | 0.2541 | 6.2930e-02 | 5.0436e-02 | 1.0360e+00 |
| 18 | 0.2691 | 6.8947e-02 | 5.1432e-02 | 1.0208e+00 |
| 19 | 0.2841 | 7.5294e-02 | 5.2331e-02 | 1.0044e+00 |
| 20 | 0.2990 | 8.1936e-02 | 5.3135e-02 | 9.8692e-01 |
| 21 | 0.3000 | 8.2390e-02 | 5.3186e-02 | 9.8572e-01 |

**Mean relative L2 error: 3.8794e-02**

## Experiment 2: Step Relaxation

- Step half-amplitude: delta = 0.03
- Initial smoothing width: w = 0.02
- D_eff used: 0.069364 (from Gaussian fit)

### Midline Profile Comparison (Step vs erfc)

| Snapshot | Time | Rel L2 Error |
|----------|------|-------------|
| 0 | 0.0000 | 4.7306e-02 |
| 1 | 0.0150 | 9.4394e-03 |
| 2 | 0.0299 | 6.6791e-03 |
| 3 | 0.0449 | 7.6514e-03 |
| 4 | 0.0598 | 9.0528e-03 |
| 5 | 0.0747 | 1.0361e-02 |
| 6 | 0.0897 | 1.1534e-02 |
| 7 | 0.1047 | 1.2592e-02 |
| 8 | 0.1196 | 1.3561e-02 |
| 9 | 0.1346 | 1.4462e-02 |
| 10 | 0.1495 | 1.5317e-02 |
| 11 | 0.1645 | 1.6144e-02 |
| 12 | 0.1794 | 1.6963e-02 |
| 13 | 0.1944 | 1.7794e-02 |
| 14 | 0.2093 | 1.8659e-02 |
| 15 | 0.2243 | 1.9578e-02 |
| 16 | 0.2392 | 2.0570e-02 |
| 17 | 0.2541 | 2.1654e-02 |
| 18 | 0.2691 | 2.2845e-02 |
| 19 | 0.2841 | 2.4154e-02 |
| 20 | 0.2990 | 2.5593e-02 |
| 21 | 0.3000 | 2.5694e-02 |

**Mean relative L2 error: 1.7618e-02**

## Conclusions

**The ED PDE in the weak-penalty, zero-participation regime behaves as an effective diffusion equation.**

The fitted D_eff = 0.069364 agrees with the prediction D * M_star = 0.075000 to within 7.5%.  The variance grows linearly (R^2 = 0.9983).  The Gaussian and step profiles match the heat-equation solutions with mean relative L2 errors of 3.88e-02 and 1.76e-02 respectively.

## Limitations

- Comparison uses the infinite-domain Gaussian solution; Neumann boundaries introduce reflections that grow with time.
- The mobility M(rho) is not exactly constant at rho = rho_star; deviations scale as O(A^2 / (rho_max - rho_star)^2).
- The weak penalty P0 = 0.01 produces a slow drift toward rho_star that is absent in the pure heat equation.
- For large amplitudes or long times the nonlinear terms dominate and the diffusion approximation breaks down.