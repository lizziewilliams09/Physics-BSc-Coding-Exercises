# Game of Life and SIRS Simulations

This folder contains Python scripts, data files, and graphs for simulating the **Game of Life (GoL)** and **SIRS epidemic model**. It includes animations, data generation scripts, analysis, and visualisation. This project demonstrates skills in simulating cellular automata, stochastic processes, handling periodic boundary conditions, bootstrap error analysis, and producing reproducible visualisations

> Developed as part of my *Modelling and Visualisation* course during my BSc in Theoretical Physics, and is included here in my Physics BSc Coding Exercises portfolio.

## **Overviews of Models** 

### **Game of Life (GoL)**

The Game of Life is a 2D cellular automaton where each cell on a grid can be either alive or dead. The state of each cell evolves over discrete time steps according to simple rules based on its neighbours:

1. A live cell with fewer than 2 or more than 3 live neighbours dies (underpopulation or overpopulation).
2. A dead cell with exactly 3 live neighbours becomes alive (reproduction).
   This simple set of rules produces complex patterns and behaviours, including oscillators, gliders, and stable structures.

### **SIRS Epidemic Model**

The SIRS model simulates the spread of an infection across a population arranged on a 2D grid. Each individual can be in one of three states:

* **S (Susceptible)** – healthy but vulnerable to infection.
* **I (Infected)** – currently infected and contagious.
* **R (Recovered)** – temporarily immune after infection, but may become susceptible again.

State transitions are stochastic (random) and depend on the individual and their neighbours:

1. A susceptible individual can become infected if at least one neighbour is infected.
2. Infected individuals recover after some time.
3. Recovered individuals can lose immunity and become susceptible again.

These rules allow the model to capture realistic dynamics of epidemic spread, including outbreaks, persistence, and eventual equilibrium.


## **Folder Structure**

```
/ (root)
├── ANIMATIONS
│   ├── GoLanimation.py
│   └── SIRSanimation.py
├── DATAFILES
│   └── makes_all_the_graphs.py
│   └── GoLpart2data.txt
│   └── GoLpart3data.txt
│   └── SIRSpart3data.txt
│   └── SIRSpart4data.txt
│   └── SIRSpart5data.txt
├── GRAPHS
│   ├── GoL Histogram of Equilibration Times.png
│   ├── GoL Velocity of Centre of Mass of Glider.png
│   ├── SIRS Colour Plot of Average Number of Infected Sites.png
│   ├── SIRS Variance of Number of Infected Sites Along a Cut.png
│   └── SIRS Finding the Immunity Fraction to Prevent Spread.png
├── GoLpart2.py
├── GoLpart3.py
├── SIRSpart3.py
├── SIRSpart4.py
├── SIRSpart5.py

```

The repository separates animations (for visual demonstrations) from analysis scripts (which generate data used for plotting). The animations are optional and independent of the main results.

## **1. Animations**

### **Game of Life (GoL)**

* **Script:** `GoLanimation.py`
* **Purpose:** Creates an animation of the Game of Life cellular automaton.
* **Usage:**

```bash
%run GoLanimation.py {size} {condition}
```

Where `size` is the grid size and `condition` is one of:
* `random` - random initial state
* `oscillator` - blinker pattern
* `glider` - glider pattern

**Details:** The animation uses matplotlib to visualize the grid, updating each cell according to GoL rules. The glider pattern is used later to track centre-of-mass motion.



### **SIRS Epidemic Model**

* **Script:** `SIRSanimation.py`
* **Purpose:** Animates the spread of infection on a 2D lattice using SIRS rules.
* **Usage:**

```bash
%run SIRSanimation.py {size} {p1} {p2} {p3}
```

Where:

* `size` = lattice size
* `p1` = infection probability
* `p2` = recovery probability
* `p3` = loss of immunity probability

**Details:**

* Cells can be Susceptible (0), Infected (-1), or Recovered (1).
* Each sweep updates all sites randomly.
* The legend maps colors to states.



## **2. Data Generation Scripts**

These scripts simulate models and save results as text files for later visualization.

### **Game of Life**

1. **`GoLpart2.py`**

   * Simulates random initial configurations.
   * Runs until the system reaches **equilibrium** (no changes in the last 10 steps).
   * Generates `GoLpart2data.txt` containing **times to equilibrate**.
   * Used to produce **Histogram of Equilibration Times**.

2. **`GoLpart3.py`**

   * Tracks the **centre of mass of a glider** pattern over time.
   * Outputs `GoLpart3data.txt` with time steps and x/y centre-of-mass positions.
   * Used to calculate **velocity of the glider**.



### **SIRS Epidemic Model**

1. **`SIRSpart3.py`**

   * Runs the SIRS model for varying `p1` and `p3` values with fixed `p2 = 0.5`.
   * Outputs `SIRSpart3data.txt` containing the **average fraction of infected sites**.
   * Used to produce the **p1-p3 colour plot** of infection prevalence.

2. **`SIRSpart4.py`**

   * Measures the **variance of infected sites** along a cut at fixed `p2 = p3 = 0.5`.
   * Uses **bootstrap error analysis** to calculate error bars.
   * Outputs `SIRSpart4data.txt` for plotting variance vs. `p1`.
   * Used to produce the **Variance Along a Cut** graph.

3. **`SIRSpart5.py`**

   * Introduces an **immune fraction** of the population.
   * Simulates SIRS dynamics to find the **minimum immunity fraction required to prevent disease spread**.
   * Outputs `SIRSpart5data.txt` for plotting immunity fraction vs. average fraction infected.



## **3. Graphs**

All graphs are produced from the `DATAFILES/makes_all_the_graphs.py` script.

1. **GoL Histogram of Equilibration Times**

   * Reads `GoLpart2data.txt`.
   * Histogram shows distribution of the number of steps required for random GoL grids to reach equilibrium. This distribution typically shows a peak at short equilibration times, reflecting rapid convergence to stable/oscillating states.
   * Color-coded by bin height.

2. **GoL Velocity of Centre of Mass of Glider**

   * Reads `GoLpart3data.txt`.
   * Scatter plot of x/y centre-of-mass over time.
   * Velocity calculated using linear regression over a selected step range.

3. **SIRS Colour Plot of Average Number of Infected Sites**

   * Reads `SIRSpart3data.txt`.
   * Heatmap in `p1-p3` plane, shows **average fraction of infected sites** for each parameter combination.

4. **SIRS Variance of Number of Infected Sites Along a Cut**

   * Reads `SIRSpart4data.txt`.
   * Plot of variance vs `p1` at fixed `p2 = p3 = 0.5`. Peaks in the variance indicate regions of parameter space with strong fluctuations, associated with cyclic waves of infection.
   * Includes error bars (red) from bootstrap analysis.

5. **SIRS Finding the Immunity Fraction to Prevent Spread**

   * Reads `SIRSpart5data.txt`.
   * Plot shows **average fraction of infected sites** vs **immune fraction**.
   * Used to identify minimum immunity fraction for disease prevention.



## **4. Running the Full Analysis**

1. Run the simulation scripts to produce data files:

   ```bash
   python GoLpart2.py
   python GoLpart3.py
   python SIRSpart3.py
   python SIRSpart4.py
   python SIRSpart5.py
   ```
2. Generate all graphs by running:

   ```bash
   python DATAFILES/makes_all_the_graphs.py
   ```

   This will collect all .txt outputs and recreate the five graphs in seen in the `GRAPHS/` folder.
   
4. Optional: Animate simulations using `GoLanimation.py` or `SIRSanimation.py`.



## **5. Notes**

* **Game of Life:**

  * Equilibration times vary; histogram shows typical distribution.
  * Glider velocity shows how patterns propagate over time.

* **SIRS Model:**

  * Part 3 explores parameter space of infection/reinfection.
  * Part 4 focuses on fluctuations along a fixed parameter slice.
  * Part 5 explores effects of immunity fraction on outbreak prevention.

* **Files:** All `.txt` files correspond to the outputs of the scripts and are read by `makes_all_the_graphs.py`.

* **Graphs:** Saved in `GRAPHS` folder; descriptive titles include relevant calculations (e.g., glider velocity).



