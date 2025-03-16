import numpy as np
from scipy.integrate import simpson

# Constants
me = 0.511       # Electron mass (MeV)
NA = 6.022e23    # Avogadro's number (1/mol)
Mu = 1e-3        # Molar mass constant
re = 2.818e-15   # Classical electron radius (m)

# Bethe-Bloch formula
def bethe_bloch(E, Z, A, I, density, z, m):
    """
    Computes energy loss per unit distance (-dE/dx) using the Bethe-Bloch formula.

    Parameters:
    - E: Kinetic energy of the incident particle (MeV)
    - Z: Atomic number of the material
    - A: Mass number of the material
    - I: Ionization potential of the material (MeV)
    - density: Density of the material (kg/m³)
    - z: Charge of the incident particle
    - m: Mass of the incident particle (MeV)

    Returns:
    - Energy loss per micrometer (MeV/µm)
    """
    gamma = 1 + E / m                  # Lorentz factor (for any particle with mass m)
    beta = np.sqrt(1 - 1 / gamma**2)   # Speed ratio v/c
    n = (NA * Z * density / (A * Mu))  # Electron density (electrons/m³)

    # Bethe-Bloch formula
    dEdx = (4 * np.pi * re**2 * z**2 * me * n / beta**2) * (np.log(2 * me * beta**2 * gamma**2 / I) - beta**2)
  
    return dEdx / 1e6  # Convert to MeV/µm

# Stopping range
def stopping_range(E, Z, A, I, density, z, m, steps: int = 1000):
    """
    Computes the stopping range (penetration depth) of a charged particle.

    Parameters:
    - E: Initial kinetic energy of the incident particle (MeV)
    - Z: Atomic number of the material
    - A: Mass number of the material
    - I: Ionization potential of the material (MeV)
    - z: Charge of the incident particle
    - m: Mass of the incident particle (MeV)
    - density: Density of the material (kg/m³)
    - steps: Number of integration points

    Returns:
    - Stopping range in micrometers (µm)
    """
    energies = np.linspace(E, 0.1, steps)
    dEdx_values = np.array([bethe_bloch(E, Z, A, I, density, z, m) for E in energies])
    
    # Numerical integration
    R_micron = simpson(1 / -dEdx_values, energies)

    return R_micron

# EXAMPLE: Calculating energy loss and stopping range for a proton in Terbium
# Input parameters
E = 17          # Initial energy of proton (MeV)
Z = 65          # Atomic number of Terbium
A = 159         # Mass number of Terbium 
I = 614e-6      # Mean excitation energy (MeV) for Terbium
density = 8299  # Density of Terbium (kg/m³)
z = 1           # Charge of proton 
m = 938.272     # Mass of proton (MeV)

# Output
print(f"Energy loss (-dE/dx) = {bethe_bloch(E, Z, A, I,  density, z, m):.3f} MeV/µm")
print(f"Stopping range: {stopping_range(E, Z, A, I, density, z, m):.3f} µm")