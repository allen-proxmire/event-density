"""
edsim.units.constants -- Fundamental physical constants in SI.

All values are CODATA 2018 recommended values.  These are used by the
mapping layer to convert between nondimensional ED quantities and
physical observables.
"""

from __future__ import annotations

# ── Fundamental constants (SI) ────────────────────────────────────────
hbar: float = 1.054571817e-34      # reduced Planck constant  [J s]
G: float = 6.67430e-11             # gravitational constant   [m^3 kg^-1 s^-2]
c: float = 299_792_458.0           # speed of light           [m s^-1]
k_B: float = 1.380649e-23          # Boltzmann constant       [J K^-1]

# ── Particle masses ───────────────────────────────────────────────────
m_p: float = 1.67262192369e-27     # proton mass   [kg]
m_e: float = 9.1093837015e-31      # electron mass [kg]
m_Pl: float = 2.176434e-8          # Planck mass   [kg]

# ── Planck scales ─────────────────────────────────────────────────────
l_Pl: float = 1.616255e-35         # Planck length [m]
t_Pl: float = 5.391247e-44         # Planck time   [s]
rho_Pl: float = 5.155e96           # Planck density [kg m^-3]
E_Pl: float = 1.9561e9             # Planck energy  [J]
T_Pl: float = 1.416784e32          # Planck temperature [K]

# ── Astrophysical ─────────────────────────────────────────────────────
M_sun: float = 1.98892e30          # solar mass     [kg]
pc: float = 3.0857e16              # parsec         [m]
kpc: float = 3.0857e19             # kiloparsec     [m]
Mpc: float = 3.0857e22             # megaparsec     [m]
H_0: float = 2.184e-18            # Hubble constant (67.4 km/s/Mpc) [s^-1]
rho_crit: float = 8.53e-27        # critical density of universe  [kg m^-3]

# ── Atomic / condensed matter ─────────────────────────────────────────
a_0: float = 5.29177210903e-11     # Bohr radius   [m]
E_h: float = 4.3597447222071e-18   # Hartree energy [J]


def print_constants() -> None:
    """Print all defined constants with their values and units."""
    _consts = {
        "hbar": (hbar, "J s", "reduced Planck constant"),
        "G": (G, "m^3 kg^-1 s^-2", "gravitational constant"),
        "c": (c, "m s^-1", "speed of light"),
        "k_B": (k_B, "J K^-1", "Boltzmann constant"),
        "m_p": (m_p, "kg", "proton mass"),
        "m_e": (m_e, "kg", "electron mass"),
        "m_Pl": (m_Pl, "kg", "Planck mass"),
        "l_Pl": (l_Pl, "m", "Planck length"),
        "t_Pl": (t_Pl, "s", "Planck time"),
        "rho_Pl": (rho_Pl, "kg m^-3", "Planck density"),
        "M_sun": (M_sun, "kg", "solar mass"),
        "pc": (pc, "m", "parsec"),
        "H_0": (H_0, "s^-1", "Hubble constant"),
        "rho_crit": (rho_crit, "kg m^-3", "critical density"),
        "a_0": (a_0, "m", "Bohr radius"),
        "E_h": (E_h, "J", "Hartree energy"),
    }
    print(f"{'Name':<10} {'Value':>14}  {'Unit':<20} {'Description'}")
    print("-" * 72)
    for name, (val, unit, desc) in _consts.items():
        print(f"{name:<10} {val:>14.6e}  {unit:<20} {desc}")
