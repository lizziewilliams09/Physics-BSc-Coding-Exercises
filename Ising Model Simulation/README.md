# Ising Model Simulation

This folder contains a Python implementation of the **two-dimensional Ising model** on a square lattice. It is part of my "Short Exercises" repository showcasing coding and computational physics tasks from my BSc in Theoretical Physics (2020–2024).

The Ising model is a classical statistical mechanics model that describes a lattice of spins which can be in one of two states (up `+1` or down `-1`). Neighboring aligned spins lower the energy of the system, leading to interesting phenomena such as **phase transitions**. The model is widely used to study magnetism and critical phenomena.

This implementation allows simulation using two types of dynamics:

1. **Glauber dynamics** – single-spin flips according to the Metropolis algorithm.
2. **Kawasaki dynamics** – spin-exchange updates preserving magnetization.

---

## Folder Structure

```

Ising_Model/
│
├── animations.py          # Runs animations of the Ising lattice evolution
├── data_with_errors.py    # Produces numerical data and calculates errors via bootstrap
├── read_in_graphs.py      # Reads data files and produces plots for analysis
├── Data files/            # Contains output data files (Glauber.txt, Kawasaki.txt)
└── Graphs/                # Contains generated graphs (magnetization, energy, heat capacity, susceptibility)

````

---

## Scripts Overview

### 1. `animations.py`
Simulates and animates the lattice evolution over time using either Glauber or Kawasaki dynamics.

**Usage:**

```bash
%run animations.py {size} {temperature} {dynamics} {nsteps} {frequency}
````

**Arguments:**

* `size`: Linear dimension of the square lattice (e.g., 50)
* `temperature`: System temperature (e.g., 2.5)
* `dynamics`: `'Glauber'` or `'Kawasaki'`
* `nsteps`: Number of sweeps/steps in the simulation
* `frequency`: Interval (ms) between frames in the animation

---

### 2. `datawitherrors.py`

Performs simulations across a range of temperatures and calculates:

* Average magnetisation
* Susceptibility
* Average energy
* Heat capacity

It also estimates errors using a bootstrap resampling method. The output is written to text files:

* `Glauber.txt` – Data from Glauber dynamics
* `Kawasaki.txt` – Data from Kawasaki dynamics

**Usage:**

```bash
%run data_with_errors.py
```

**Note:** The script uses default parameters: lattice size 50, 10000 sweeps per temperature, temperatures 1.0–3.0 in steps of 0.1. You can modify parameters by editing the script.

---

### 3. `read in graphs from errors.py`

Reads data files and produces graphs of:

* Average absolute magnetisation vs. temperature
* Susceptibility vs. temperature
* Average energy vs. temperature
* Heat capacity vs. temperature

**Note:** Graphs for Kawasaki dynamics still include magnetization and susceptibility to show they are effectively zero.

**Usage:**

```bash
%run read_in_graphs.py
```

## Background Notes

* **Critical Temperature Estimation:** The phase transition is observable as a sharp change in magnetization or a peak in heat capacity. For a 2D square lattice Ising model using Glauber dynamics, the critical temperature is approximately `T_c ≈ 2.27` (in units where J/k_B = 1).
* **Periodic Boundary Conditions:** Implemented to avoid edge effects in the lattice.
* **Equilibration and Sampling:** Observables are measured after an initial equilibration period and at intervals to reduce correlation between samples.
* **Error Estimation:** Bootstrap resampling is used to calculate uncertainties in susceptibility and heat capacity.

