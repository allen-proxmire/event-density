"""NodeState / StateVector — B1 events, B4 commitment density, B5 orientation.

commit() is the SOLE writer of rho: the irreversibility chokepoint (B7).
No other code path in the package may assign to NodeState.rho.
"""
from __future__ import annotations

from typing import Optional

import numpy as np


class NodeState:
    """Per-node substrate state.

    rho         : commitment density (B4); monotone non-decreasing (B7).
    orientation : B5; index 0 = longitudinal (derivable), 1.. = transverse
                  (primitive). Carried by chain-continuity, never read by Sigma.
    """

    def __init__(self, rho: float = 0.0,
                 orientation: Optional[np.ndarray] = None,
                 orientation_dim: int = 2) -> None:
        self.rho: float = float(rho)
        if orientation is None:
            orientation = np.zeros(orientation_dim, dtype=float)
        self.orientation: np.ndarray = np.asarray(orientation, dtype=float)
        self.committed: bool = False
        self.active: bool = False
        self.stratum_id: int = 0

    def commit(self, delta: float,
               longitudinal: Optional[float] = None,
               transverse: Optional[np.ndarray] = None) -> None:
        """The ONLY method that writes rho. Enforces irreversibility (B7):
        delta must be >= 0; rho is incremented, never decremented.

        Optionally writes orientation: longitudinal (index 0) is the derivable
        commitment-flow direction; transverse (1..) is the primitive component
        transported from the source node.
        """
        if delta < 0:
            raise ValueError(
                f"Irreversibility violation (B7): commit delta={delta} < 0"
            )
        self.rho += float(delta)
        self.committed = True
        if longitudinal is not None:
            self.orientation[0] = float(longitudinal)
        if transverse is not None:
            self.orientation[1:] = np.asarray(transverse, dtype=float)


class StateVector(dict):
    """node_id -> NodeState, with convenience accessors.

    A thin dict subclass: the whole-substrate state is the mapping itself.
    """

    def rho_at(self, v: int) -> float:
        return self[v].rho

    def orientation_at(self, v: int) -> np.ndarray:
        return self[v].orientation

    def is_active(self, v: int) -> bool:
        return self[v].active

    def stratum_id(self, v: int) -> int:
        return self[v].stratum_id

    def active_nodes(self) -> list[int]:
        return [v for v, s in self.items() if s.active]
