Absolutely! Here's a **comprehensive README** for your Ising Model folder. I’ve structured it with background, folder structure, usage instructions, and details about each script. You can paste this directly as a Markdown file (`README.md`) in your folder.

```markdown
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

**Example:**

```bash
%run animations.py 50 2.5 Glauber 1000 50
```

---

### 2. `data_with_errors.py`

Performs simulations across a range of temperatures and calculates:

* Average magnetization
* Susceptibility
* Average energy
* Heat capacity

It also estimates **errors** using a bootstrap resampling method. The output is written to text files in the `Data files/` folder:

* `Glauber.txt` – Data from Glauber dynamics
* `Kawasaki.txt` – Data from Kawasaki dynamics

**Usage:**

```bash
%run data_with_errors.py
```

**Notes:**

* The script uses default parameters: lattice size 50, 10000 sweeps per temperature, temperatures 1.0–3.0 in steps of 0.1.
* You can modify parameters by editing the script.

---

### 3. `read_in_graphs.py`

Reads data files from `Data files/` and produces graphs of:

* Average absolute magnetization vs. temperature
* Susceptibility vs. temperature
* Average energy vs. temperature
* Heat capacity vs. temperature

Graphs for Kawasaki dynamics include magnetization and susceptibility to show they are effectively zero.

**Usage:**

```bash
%run read_in_graphs.py
```

**Output:**

* The figures are displayed interactively and can be saved manually if desired.
* Graphs are also stored in the `Graphs/` folder (if previously generated).

---

## Example Workflow

1. **Visualize dynamics:**

```bash
%run animations.py 50 2.5 Glauber 1000 50
```

2. **Generate data and calculate errors:**

```bash
%run data_with_errors.py
```

* This produces `Glauber.txt` and `Kawasaki.txt` in `Data files/`.

3. **Plot graphs from data:**

```bash
%run read_in_graphs.py
```

* Plots will include error bars where applicable and illustrate critical behavior around the phase transition.

---

## Background Notes

* **Critical Temperature Estimation:** The phase transition is observable as a sharp change in magnetization or a peak in heat capacity. For a 2D square lattice Ising model using Glauber dynamics, the critical temperature is approximately `T_c ≈ 2.27` (in units where J/k_B = 1).
* **Periodic Boundary Conditions:** Implemented to avoid edge effects in the lattice.
* **Equilibration and Sampling:** Observables are measured after an initial equilibration period and at intervals to reduce correlation between samples.
* **Error Estimation:** Bootstrap resampling is used to calculate uncertainties in susceptibility and heat capacity.

---

## References

* [K. Huang, *Statistical Mechanics*, 2nd Edition, 1987]
* [N. Metropolis et al., *Equation of State Calculations by Fast Computing Machines*, 1953]
* [Wikipedia: Ising model](https://en.wikipedia.org/wiki/Ising_model)

---

This folder demonstrates **simulation, data analysis, and visualization skills** in computational physics, and is part of my collection of short coding exercises.

```

---

If you want, I can also **draft a slightly shorter “portfolio-friendly” version** for the main `Short Exercises` README that introduces this folder in one paragraph, so it doesn’t overwhelm someone browsing your repo.  

Do you want me to do that too?
```
