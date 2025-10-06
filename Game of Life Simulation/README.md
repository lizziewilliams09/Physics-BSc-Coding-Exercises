# Game of Life

This folder contains Python scripts, data files, and graphs for simulating the **Game of Life (GoL)**. It includes an animation, data generation scripts, analysis, and visualisation. This project demonstrates skills in simulating cellular automata, efficient array updates, handling periodic boundary conditions, and producing reproducible visualisations

> Developed as part of my *Modelling and Visualisation* course during my BSc in Theoretical Physics, and is included here in my Physics BSc Coding Exercises portfolio.

## **Overview of Model** 

The Game of Life is a 2D cellular automaton where each cell on a grid can be either alive or dead. The state of each cell evolves over discrete time steps according to simple rules based on its neighbours:

1. A live cell with fewer than 2 or more than 3 live neighbours dies (underpopulation or overpopulation).
2. A dead cell with exactly 3 live neighbours becomes alive (reproduction).
   This simple set of rules produces complex patterns and behaviours, including oscillators, gliders, and stable structures.

## **Folder Structure**

```
/ (root)
├── DATAFILES
│   └── makes all the graphs.py
│   └── GoLpart2data.txt
│   └── GoLpart3data.txt
├── GRAPHS
│   ├── GoL Histogram of Equilibration Times.png
│   ├── GoL Velocity of Centre of Mass of Glider.png
├── GoLanimation.py
├── GoLpart2.py
├── GoLpart3.py

```

The repository separates the animation (for visual demonstrations) from analysis scripts (which generate data used for plotting). The animations are optional and independent of the main results.

## **1. Animation**

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

## **2. Data Generation Scripts**

These scripts simulate models and save results as text files for later visualisation.

1. **`GoLpart2.py`**

   * Simulates random initial configurations.
   * Runs until the system reaches **equilibrium** (no changes in the last 10 steps).
   * Generates `GoLpart2data.txt` containing **times to equilibrate**.
   * Used to produce **Histogram of Equilibration Times**.

2. **`GoLpart3.py`**

   * Tracks the **centre of mass of a glider** pattern over time.
   * Outputs `GoLpart3data.txt` with time steps and x/y centre-of-mass positions.
   * Used to calculate **velocity of the glider**.

## **3. Graphs**

All graphs are produced from the `DATAFILES/makes all the graphs.py` script.

1. **GoL Histogram of Equilibration Times**

   * Reads `GoLpart2data.txt`.
   * Histogram shows the distribution of the number of steps required for random GoL grids to reach equilibrium. This distribution typically shows a peak at short equilibration times, reflecting rapid convergence to stable/oscillating states.
   * Colour-coded by bin height.

2. **GoL Velocity of Centre of Mass of Glider**

   * Reads `GoLpart3data.txt`.
   * Scatter plot of x/y centre-of-mass over time.
   * Velocity calculated using linear regression over a selected step range.

## **4. Running the Full Analysis**

1. Run the simulation scripts to produce data files:

   ```bash
   python GoLpart2.py
   python GoLpart3.py
   ```
2. Save all files in the `DATAFILES/` folder, then generate all graphs by running:

   ```bash
   python DATAFILES/makes all the graphs.py
   ```

   This will collect all .txt outputs and recreate the five graphs seen in the `GRAPHS/` folder.
   
4. Optional: Animate simulation using `GoLanimation.py`


## **5. Notes**

* **Game of Life:**

  * Equilibration times vary; histogram shows typical distribution.
  * Glider velocity shows how patterns propagate over time.

* **Files:** All `.txt` files correspond to the outputs of the scripts and are read by `makes all the graphs.py`.

* **Graphs:** Seen in `GRAPHS` folder; descriptive titles include relevant calculations (e.g., glider velocity).







