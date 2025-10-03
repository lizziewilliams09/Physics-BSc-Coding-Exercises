# Ising Model Simulation

This folder contains a Python implementation of the two-dimensional Ising model on a square lattice. The Ising model describes spins on a lattice which can point up (`+1`) or down (`-1`). Neighbouring aligned spins lower the system energy, leading to collective behaviour and a finite-temperature phase transition.  

This implementation supports two update rules:
- **Glauber dynamics**: single-spin flips with Metropolis acceptance.  
- **Kawasaki dynamics**: spin exchanges which conserve total magnetisation.  

> This project was developed as part of my *Modelling and Visualisation* course during my BSc in Theoretical Physics, and is included here in my Physics BSc Coding Exercises portfolio.

## Folder Structure

```

Ising_Model/
│
├── animations.py                  # Runs lattice evolution animations
├── datawitherrors.py              # Produces numerical data with bootstrap uncertainties
├── read in graphs from data.py    # Reads data files and produces plots
├── Data files/                    # Output numerical data (Glauber.txt, Kawasaki.txt)
└── Graphs/                        # Plots of magnetisation, energy, heat capacity, susceptibility

````



## Simulation Setup

All results and graphs in this project are generated with the following parameters:

- **Lattice size:** `50 × 50` (periodic boundary conditions)  
- **Coupling constant:** `J = 1`  
- **Boltzmann constant:** `k_B = 1`  
- **Temperature range:** `T = 1.0 → 3.0` (steps of 0.1)  
- **Equilibration:** 100 sweeps discarded before measurement  
- **Measurements:** every 10 sweeps, ~1000 samples per temperature  
- **Error estimation:** bootstrap resampling  

> Note: The critical temperature of the infinite 2D Ising model in these units is `T_c ≈ 2.27`. Finite-size effects shift and broaden the peaks in susceptibility and heat capacity around this value.



## Scripts Overview

### 1. `animations.py`
Simulates and animates lattice evolution under Glauber or Kawasaki dynamics.

**Usage:**
```bash
%run animations.py {size} {temperature} {dynamics} {nsteps} {frequency}
````

Arguments:

* `size` - lattice size (e.g. 50)
* `temperature` - system temperature (e.g. 2.5)
* `dynamics` - `'Glauber'` or `'Kawasaki'`
* `nsteps` - number of sweeps
* `frequency` - frame interval (ms)

### 2. `datawitherrors.py`

Runs simulations across the temperature range and calculates:

* Average absolute magnetisation `<|M|>`
* Susceptibility `chi`
* Average energy `<E>`
* Heat capacity `C`

Bootstrap resampling gives uncertainty estimates.

**Output files:** `Glauber.txt` and `Kawasaki.txt`

### 3. `read in graphs from data.py`

Reads numerical data files and produces plots (as seen in `Graphs/` folder).

* `<|M|>` vs T
* `chi` vs T
* `<E>` vs T
* `C` vs T

(Kawasaki plots include `<|M|>` and `chi` for completeness, though they remain ≈ 0.)



## Graphs and Data Files Overview

### 1. **Data Files (`Data files/`)**

   * `Glauber.txt`: `<|M|>`, `chi`, `<E>`, `C` with uncertainties
   * `Kawasaki.txt`: `<E>`, `C` (plus near-zero `<|M|>` and `chi`)

   Useful for quantitative checks and reproducibility.

### 2. **Graphs (`Graphs/`)**

The simulation outputs plots of the main observables as functions of temperature (`T = 1.0–3.0`), and all observables include error bars estimated via bootstrap resampling:
    
  * **Magnetisation `<|M|>`**
  
    * Glauber: decreases smoothly with temperature, approaching zero above the critical region.
    * Kawasaki: remains ≈ 0 at all T (magnetisation is conserved).
  
  * **Susceptibility `χ`**
  
    * Glauber: shows a finite-size peak near the expected critical temperature (`T_c ≈ 2.27` in units where J/k_B = 1).
    * Kawasaki: remains ≈ 0.
  
  * **Energy `<E>`**
  
    * Both dynamics: continuous curve with a slope change around `T_c`.
  
  * **Heat Capacity `C`**
  
    * Glauber: sharp peak near `T_c`, a finite-size signature of the phase transition.
    * Kawasaki: smoother variation without a pronounced peak.
  
  In an infinite 2D Ising model, both susceptibility and heat capacity would diverge at `T_c`. In the finite 50×50 simulation, they appear as fairly sharp peaks under Glauber dynamics. Under Kawasaki dynamics, conservation of magnetisation suppresses the ordering, so `χ` stays near zero and `C` shows a broader and weaker maximum.


