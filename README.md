# BSc Short Coding Exercises

This repository contains a few of the coding tasks and numerical exercises completed during my BSc in Theoretical Physics (2020–2024). Each task is provided either as a Jupyter notebook (with explanations, background, and results documented in the markdown cells) or as a folder containing multiple Python scripts along with a dedicated README. The purpose of this repository is to showcase coding, simulation, and computational physics skills through a selection of short projects completed during my undergraduate studies.

## Excersises

* **Baseballs in Flight**: Simulates batted baseball trajectories under gravity, drag, and spin using Python's `solve_ivp` for numerical integration. Includes Monte Carlo sampling to explore variability in initial speed, angle, and spin, demonstrating physics-based modelling and stochastic simulation.

* **Harmonics of a Square Wave**: Analyses a square wave using Fourier decomposition, fitting sine and cosine components to reconstruct the signal. Uses least-squares fitting and linear algebra (`numpy`, `scipy.linalg`) to extract amplitudes and phases, showcasing practical signal processing and data modelling.

* **Ising Model Simulation**: Simulates the 2D Ising model on a square lattice with Glauber and Kawasaki dynamics. Produces lattice animations, numerical data with error estimates, and plots of magnetisation, susceptibility, energy, and heat capacity. Demonstrates skills in numerical simulation, statistical analysis, and visualisation of complex physical systems.

* **Game of Life and SIRS Simulations**: Implements 2D cellular automata (Game of Life) and stochastic epidemic dynamics (SIRS model) on a lattice. Generates animations, numerical data, and visualisations for equilibration times, glider motion, infection prevalence, variance, and immunity thresholds. Demonstrates skills in stochastic simulation, handling periodic boundary conditions, data analysis, and reproducible plotting.

* **Cahn–Hilliard Simulation**: Numerically solves the Cahn–Hilliard equation to model phase separation in binary mixtures. Includes scripts for generating and animating free energy density data, and plotting its time evolution for 100×100 systems. Demonstrates skills in PDE discretisation, numerical stability handling, and scientific visualisation.

* **Poisson Equation Simulation**: Solves the 3D Poisson equation for electrostatic potential using the Jacobi iterative method under Dirichlet boundary conditions. Generates contour and vector plots of the potential and electric field, and investigates their dependence on distance. Demonstrates experience with iterative solvers, convergence control, and visual analysis of physical fields.

* **Gauss–Seidel Over-Relaxed Solver**: Extends the Poisson solver using the Gauss–Seidel Successive Over-Relaxation (SOR) method to improve convergence efficiency. Determines the optimal relaxation parameter ω by measuring iteration counts across values of ω ∈ [1.7, 1.98]. Demonstrates understanding of numerical optimisation, performance benchmarking, and iterative algorithm tuning.
