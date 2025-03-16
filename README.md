**Bethe-Bloch Energy Loss and Stopping Range Calculator**

This Python script calculates the energy loss (-dE/dx) and stopping range of particles in various materials using the Bethe-Bloch formula.

**Features**
- Computes energy loss per unit distance (-dE/dx) in MeV/µm.
- Calculates the stopping range in micrometers (µm).
- Uses numerical integration (Simpson's rule) for precise calculations.
- Allows customization for different materials and types of incident particles.

**How to Use** \
Modify the input parameters in the script to calculate values for other materials:

- **E**: Initial particle energy (MeV)
- **Z**: Atomic number of the material
- **A**: Mass number of the material
- **I**: Mean ionization potential (MeV)
- **density**: Material density (kg/m³)
- **z**: Charge of the incident particle
- **m**: Mass of the incident particle (MeV)

**How It Works** \
The script:
1. Uses the Bethe-Bloch equation to compute the energy loss of particles as they travel through a material.
2. Integrates the inverse energy loss function to determine the stopping range.

**Formulae Used**

The Bethe-Bloch equation:

$$ -\frac{dE}{dx} = \frac{4 \pi r_e^2 z^2 m_e c^2 n}{\beta^2} \left( \ln \left( \frac{2 m_e c^2 \beta^2 \gamma^2}{I} \right) - \beta^2 \right) $$

where:
- $r_e$: classical electron radius,
- $m_e c^2$: rest mass energy of an electron,
- $z$: charge of the incident particle,
- $n$: electron density of the material,
- $\beta$: speed ratio $v/c$,
- $\gamma$: Lorentz factor,
- $I$: mean ionization potential of the material,

The stopping range is obtained by numerically integrating:

$$ R = \int \frac{dE}{- \frac{dE}{dx}} $$
