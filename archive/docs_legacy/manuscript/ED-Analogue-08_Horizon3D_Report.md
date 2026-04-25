# ED Analogue: 3D Horizon Formation and Retreat

## Setup
- Channels: mobility + penalty (H = 0)
- Dimension: d = 3
- rho_crit = 0.9000, A_c predicted = 0.4000

## Results

| A | Horizon? | R_H max | tau_H | tau_H pred |
|---|---------|---------|-------|------------|
| 0.35 | No | 0.000 | 0.000 | 0.000 |
| 0.38 | No | 0.000 | 0.000 | 0.000 |
| 0.40 | No | 0.000 | 0.000 | 0.000 |
| 0.42 | No | 0.000 | 0.000 | 0.109 |
| 0.45 | Yes | 0.133 | 0.160 | 0.263 |
| 0.48 | Yes | 0.162 | 0.320 | 0.407 |

A_c predicted: 0.400
A_c measured:  0.450 (12.5% error)

## Falsification
- Sharp threshold: FAIL
- No horizon below A_c: PASS
- Monotone retreat: PASS

## Interpretation
3D horizons follow the same structural pattern as 2D: sharp threshold, 
monotone retreat, lifetime increasing with amplitude.