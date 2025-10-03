# Ising Model Simulation

This folder contains a Python implementation of the two-dimensional Ising model on a square lattice. The Ising model is a classical statistical mechanics model that describes a lattice of spins which can be in one of two states (up `+1` or down `-1`). Neighbouring aligned spins lower the energy of the system, leading to interesting phenomena such as phase transitions. The model is widely used to study magnetism and critical phenomena.

This implementation allows simulation using two types of dynamics:

1. **Glauber dynamics** - single-spin flips according to the Metropolis algorithm.
2. **Kawasaki dynamics** - spin-exchange updates preserving magnetization.

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

* `Glauber.txt` - Data from Glauber dynamics
* `Kawasaki.txt` - Data from Kawasaki dynamics

**Usage:**

```bash
%run data_with_errors.py
```

**Note:** The script uses default parameters: lattice size 50, 10000 sweeps per temperature, temperatures 1.0-3.0 in steps of 0.1. You can modify parameters by editing the script.

---

### 3. `read in graphs from errors.py`

Reads data files and produces graphs of:

* Average absolute magnetisation vs. temperature
* Susceptibility vs. temperature
* Average energy vs. temperature
* Heat capacity vs. temperature

**Note:** Graphs for Kawasaki dynamics still include magnetisation and susceptibility to show they are effectively zero.

**Usage:**

```bash
%run read_in_graphs.py
```

## Background Notes

* **Ising Hamiltonian:** The energy of a spin configuration ({S_i}) on a 2D square lattice is
  [
  E({S_i}) = -J \sum_{\langle i,j\rangle} S_i S_j ,
  ]
  where (S_i \in {-1, +1}), the sum runs over nearest-neighbour pairs, and (J>0) favours aligned spins. In your code, (J = k_B = 1).

* **Update Dynamics:**

  * *Glauber Dynamics*: Single-spin flips are proposed at random sites, accepted with Metropolis probability (\min{1, e^{-\Delta E/T}}). This samples the canonical ensemble at temperature (T).
  * *Kawasaki Dynamics*: Spin exchanges between randomly chosen sites conserve total magnetisation, so magnetisation is no longer an order parameter. Critical behaviour is instead studied via energy and heat capacity.

* **Observables:**

  * **Magnetisation:** (M = \sum_i S_i), tracks spontaneous symmetry breaking below (T_c).
  * **Susceptibility:** (\chi = \frac{1}{N T} (\langle M^2 \rangle - \langle M \rangle^2)), peaks near (T_c).
  * **Energy:** Average energy per spin gives insight into ordering.
  * **Heat Capacity:** (C = \frac{1}{N T^2} (\langle E^2 \rangle - \langle E \rangle^2)), also peaks near (T_c).

* **Simulation Setup:**

  * *Periodic Boundary Conditions* remove finite-size edge effects.
  * *Equilibration:* The system is evolved for ~100 sweeps before recording data.
  * *Measurement Intervals:* Measurements are taken every 10 sweeps to reduce correlations.
  * *Error Estimation:* Bootstrap resampling is applied to compute uncertainties in (\chi) and (C).

* **Critical Behaviour:**

  * The true critical temperature for the 2D square Ising model is (T_c \approx 2.27) (in units with (J/k_B = 1)).
  * In finite-size simulations (e.g. (50 \times 50) lattices), the observed peaks in (\chi) and (C) shift and broaden, but still cluster near (T_c).

* **Visualisation:**

  * *Animations* generated with `matplotlib.animation.FuncAnimation` show the lattice evolving in real time under the chosen dynamics.
  * *Plots* of magnetisation, susceptibility, energy, and heat capacity as functions of (T) allow numerical estimation of (T_c).



