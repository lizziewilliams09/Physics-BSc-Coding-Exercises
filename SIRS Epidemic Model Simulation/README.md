# SIRS Model for Epidemics Spreading

This folder contains Python scripts, data files, and graphs for simulating the **SIRS epidemic model**. It includes an animation, data generation scripts, analysis, and visualisation. This project demonstrates skills in stochastic processes, bootstrap error analysis, and producing reproducible plots and visualisations.

> Developed as part of my *Modelling and Visualisation* course during my BSc in Theoretical Physics, and is included here in my Physics BSc Coding Exercises portfolio.

## **Overviews of Model** 

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
├── DATAFILES
│   └── makes all the graphs.py
│   └── SIRSpart3data.txt
│   └── SIRSpart4data.txt
│   └── SIRSpart5data.txt
├── GRAPHS
│   ├── SIRS Colour Plot of Average Number of Infected Sites.png
│   ├── SIRS Variance of Number of Infected Sites Along a Cut.png
│   └── SIRS Finding the Immunity Fraction to Prevent Spread.png
├── SIRSanimation.py
├── SIRSpart3.py
├── SIRSpart4.py
├── SIRSpart5.py

```

The repository separates the animation (for visual demonstration) from analysis scripts (which generate data used for plotting). The animations are optional and independent of the main results.

## **1. Animation**

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

These scripts simulate models and save results as text files for later visualisation.

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

All graphs are produced from the `DATAFILES/makes all the graphs.py` script.

1. **SIRS Colour Plot of Average Number of Infected Sites**

   * Reads `SIRSpart3data.txt`.
   * Heatmap in `p1-p3` plane, shows **average fraction of infected sites** for each parameter combination.

2. **SIRS Variance of Number of Infected Sites Along a Cut**

   * Reads `SIRSpart4data.txt`.
   * Plot of variance vs `p1` at fixed `p2 = p3 = 0.5`. Peaks in the variance indicate regions of parameter space with strong fluctuations, associated with cyclic waves of infection.
   * Includes error bars (red) from bootstrap analysis.

3. **SIRS Finding the Immunity Fraction to Prevent Spread**

   * Reads `SIRSpart5data.txt`.
   * Plot shows **average fraction of infected sites** vs **immune fraction**.
   * Used to identify the minimum immunity fraction for disease prevention.



## **4. Running the Full Analysis**

1. Run the simulation scripts to produce data files:

   ```bash
   python SIRSpart3.py
   python SIRSpart4.py
   python SIRSpart5.py
   ```
2. Save all produced .txt files in the `DATAFILES/` folder, then generate all graphs by running:

   ```bash
   python DATAFILES/makes all the graphs.py
   ```

   This will collect all .txt outputs and recreate the five graphs seen in the `GRAPHS/` folder.
   
4. Optional: Animate simulations using `SIRSanimation.py`.



## **5. Notes**

* **SIRS Model:**

  * Part 3 explores the parameter space of infection/reinfection.
  * Part 4 focuses on fluctuations along a fixed parameter slice.
  * Part 5 explores the effects of immunity fraction on outbreak prevention.

* **Files:** All `.txt` files correspond to the outputs of the scripts and are read by `makes all the graphs.py`.

* **Graphs:** Saved in `GRAPHS` folder; descriptive titles include relevant calculations (e.g., glider velocity).




