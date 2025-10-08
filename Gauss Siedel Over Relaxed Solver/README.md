# Gauss-Seidel Over-Relaxed Solver (SOR) - Finding the Optimal ω

This project implements a Gauss-Seidel Over-Relaxed (SOR) solver for the 3D Poisson equation, with the goal of identifying the optimal relaxation factor (ω) that minimises the number of iterations required for convergence.

The simulation models a unit point charge placed at the centre of a cubic grid, and iteratively solves for the electrostatic potential φ under Dirichlet boundary conditions (φ = 0 at all faces). The relaxation factor ω ∈ [1.7, 1.98] is varied to study its effect on convergence speed.



## Method

The SOR algorithm improves upon the standard Gauss-Seidel method by introducing a relaxation parameter ω (1 < ω < 2) that accelerates convergence:

$$
\phi_{i,j,k}^{(n+1)} = (1 - \omega)\phi_{i,j,k}^{(n)} + \frac{\omega}{6} \left(
\phi_{i+1,j,k} + \phi_{i-1,j,k} +
\phi_{i,j+1,k} + \phi_{i,j-1,k} +
\phi_{i,j,k+1} + \phi_{i,j,k-1} +
\rho_{i,j,k}(\Delta x)^2
\right)
$$

The iterative process continues until the total absolute difference between successive potential arrays falls below a specified tolerance ε.



## Files

| File | Description |
|------|--------------|
| **`finding best omega.py`** | Main solver script. Runs the 3D SOR algorithm for a range of ω values and records iteration counts required to reach convergence (ε = 1e-3). |
| **`gauss-siedel over relaxed.txt`** | Output file storing the results (`omega` vs `iterations`). |
| **`plot graph.py`** | Loads the data and plots convergence iterations as a function of ω. |
| **`finding best omega.png`** | Graph showing the relationship between ω and iteration count, illustrating the optimal relaxation parameter. |



## Results

The resulting plot shows a clear minimum in the number of iterations around the optimal ω ≈ 1.9, where convergence is fastest.  
Lower ω values under-relax (slow convergence), while values too close to 2 cause instability or oscillations.



## Key Concepts

- **Successive Over-Relaxation (SOR)**: an accelerated Gauss-Seidel method.  
- **Convergence tuning**: the parameter ω directly influences numerical stability and efficiency.  
- **Performance evaluation**: this project quantifies algorithmic improvement over the basic iterative method.



## Dependencies

- `numpy`
- `matplotlib`



## Context

This project builds on a simpler Poisson-equation solver by introducing over-relaxation to reduce iteration time.  
It can stand alone as an example of numerical optimisation in scientific computing, focusing on computational performance rather than physical analysis.

