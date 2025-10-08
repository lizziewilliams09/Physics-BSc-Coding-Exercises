# Cahn-Hilliard Equation Simulation

This folder contains a numerical simulation and analysis of the Cahn-Hilliard equation, which models phase separation in binary mixtures such as water-oil emulsions. The equation tracks the evolution of an order parameter φ(x, t) - representing local composition - that evolves over time as the system separates into distinct phases while conserving total composition.



## Background

The Cahn-Hilliard equation is a fourth-order nonlinear partial differential equation describing how a binary system minimises its free energy by separating into regions of differing composition.

**Governing equations:**

```
∂φ/∂t = M ∇²μ
μ = -aφ + aφ³ - κ∇²φ
```

Where:

* **φ(x,t)** - order parameter (positive in one phase, negative in the other)
* **M** - mobility (rate of diffusion)
* **a**, **κ** - positive constants controlling interaction strength and interfacial energy
* **μ** - chemical potential driving phase separation

Over time, domains of opposite composition coarsen, and the total free energy of the system decreases.

**Free energy density:**

```
f = -(a/2)φ² + (a/4)φ⁴ + (κ/2)(∇φ)²
```



## Numerical Implementation

The equation is solved using a finite-difference explicit Euler scheme on a 2D square lattice with periodic boundary conditions.
Each lattice site holds a value of φ that evolves according to discretised Laplacians and chemical potential updates.

Configurable parameters include:

* `size` - lattice dimension (e.g. 100×100)
* `a`, `M`, `kappa` - physical constants
* `dx`, `dt` - spatial and temporal steps
* `phi_initial` - mean composition
* `initial_random_noise` - random perturbation amplitude



## Folder Contents

### **animation.py**

Animates the phase-separation process governed by the Cahn-Hilliard equation.
You can adjust the lattice size and initial conditions within the script. Produces a live visualisation of domain growth and coarsening.

### **cahn-hilliard free energy densities.py**

Computes and records the **total free energy density** of the system over time.
Outputs results to a text file (`free_energy_densities.txt`) with two columns: time step and total free energy.

### **plot free energy density graphs.py**

Reads the data file and plots *Free Energy Density vs Time*, showing the expected decrease in free energy as the system evolves toward equilibrium.



## Included Example Outputs

### **DATA FILES AND CODE TO CREATE/**

* `100x100 free_energy_densities phi = 0.txt`
* `100x100 free_energy_densities phi = 0.5.txt`
  Generated using the free energy density script for two initial compositions (φ₀ = 0 and φ₀ = 0.5).

### **GRAPHS/**

* `100x100 free energy density vs time w phi = 0.png`
* `100x100 free energy density vs time w phi = 0.5.png`
  Plots showing the decay of total free energy over time.



## Physical Interpretation

* For **φ₀ = 0**, the mixture starts symmetric and separates into roughly equal regions of each phase.
* For **φ₀ = 0.5**, the asymmetry produces smaller domains of the minority phase within a majority background.
* In both cases, the free energy decreases monotonically as the system coarsens toward a stable, low-energy configuration.



## How to Run

1. Run `animation.py` to visualise phase separation dynamics.
2. Run `cahn-hilliard free energy densities.py` to generate `free_energy_densities.txt`.
3. Use `plot free energy density graphs.py` to create the energy-vs-time plot.



## Summary

This project numerically demonstrates how the Cahn-Hilliard equation governs diffusion-driven phase separation in conserved systems.
It combines physical modelling, numerical PDE solving, and data visualisation, illustrating how a complex, nonlinear system evolves to minimise its free energy over time.
