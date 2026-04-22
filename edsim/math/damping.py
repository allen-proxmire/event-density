"""
edsim.math.damping -- Canonical damping-discriminant helpers.

Implements the linearised D_crit(zeta) for Canon principle P6 as derived
in theory/D_crit_Resolution_Memo.md (2026-04-22). Supersedes the earlier
heuristic D_crit = 1 - 2*zeta = 0.5 at canon-default zeta = 1/4.

Mathematical content (reference-mode epsilon_k*tau = 1):

    underdamped iff  (D - zeta)^2 < 4 (1 - D)
    critical at       D_crit(zeta) = -(2 - zeta) + 2*sqrt(2 - zeta)
                                    = sqrt(2 - zeta) * (2 - sqrt(2 - zeta))
    at zeta = 1/4 ->  D_crit approx 0.896

The earlier additive heuristic D + 2*zeta = 1 (giving 0.5 at zeta=1/4)
is retained via `d_crit_heuristic` for documentation and for legacy
figure regeneration. It is NOT canonical.
"""

from __future__ import annotations

import numpy as np


ZETA_CANONICAL = 0.25


def d_crit(zeta: float) -> float:
    """Linearised critical damping threshold for Canon P6.

    Derived in theory/D_crit_Resolution_Memo.md. Valid at reference
    mode epsilon_k * tau = 1 (i.e. M_0 * k^2 + P_0 = 1 / tau).

    Parameters
    ----------
    zeta : float
        Participation damping coefficient, in [0, 1].

    Returns
    -------
    D_crit : float
        Critical damping threshold in [2*sqrt(2)-2, 1].
    """
    if not (0.0 <= zeta <= 1.0):
        raise ValueError(f"zeta must lie in [0, 1]; got {zeta}")
    u = np.sqrt(2.0 - zeta)
    return float(u * (2.0 - u))


def d_crit_heuristic(zeta: float) -> float:
    """Retired additive heuristic D_crit = 1 - 2*zeta.

    Gives 0.5 at canon-default zeta = 1/4. Retained only for legacy
    comparison; NOT canonical.
    """
    return 1.0 - 2.0 * zeta


def underdamped(D: float, zeta: float) -> bool:
    """True iff a mode at reference rate is underdamped.

    Uses the exact condition (D - zeta)^2 < 4 (1 - D).
    """
    return (D - zeta) ** 2 < 4.0 * (1.0 - D)


# Canon-default reference value used by atlas / diagram scripts
D_CRIT_CANONICAL: float = d_crit(ZETA_CANONICAL)
"""Canonical D_crit at zeta = 1/4 -> approx 0.896. Supersedes 0.5."""
