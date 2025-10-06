import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import colors

'''
Game of Life Part 2 - Histogram of Equilibration Times
'''
equilibrium_times = []

with open('GoLpart2data.txt', 'r') as file:
    # Skip the header line
    next(file)
    
    # Read each line in the file
    for line in file:
        # Convert each column to the appropriate data type and append to the corresponding list
        columns = line.strip().split('\t')
        equilibrium_time = columns[0]
        
        if equilibrium_time != "None":
            # Append values to the respective lists
            equilibrium_times.append(float(equilibrium_time))

fig, ax = plt.subplots()

N, bins, patches = ax.hist(equilibrium_times, bins=30, density=True) # N is count in each bin, bins is the lower-limit of the bin
fracs = N / N.max() # colour code by height
norm = colors.Normalize(fracs.min(), fracs.max()) #normalize the data for the full range of the colormap

#loop through the objects and set the color of each accordingly
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

plt.xlabel('Time to Equilibrate')
plt.ylabel('Probability Density')
plt.title('Distribution of ' + str(len(equilibrium_times)) + ' Times Needed to Equilibrate')
plt.show()

'''
Game of Life Part 3 - Glider Centre of Mass Plot
'''

steps = []
x_centres_of_mass = []
y_centres_of_mass = []


with open("GoLpart3data.txt", 'r') as file:
    # Skip the header line
    next(file)
    
    # Read each line in the file
    for line in file:
        # Split the line into columns using tab as delimiter
        columns = line.strip().split('\t')
        
        # Convert each column to the appropriate data type and append to the corresponding list
        step = int(columns[0])
        x_com = float(columns[1])
        y_com = float(columns[2])  
        
        # Append values to the respective lists
        steps.append(step)
        x_centres_of_mass.append(x_com)
        y_centres_of_mass.append(y_com)

x_slope, _ = np.polyfit(steps[38:75], x_centres_of_mass[38:75], 1)
y_slope, _ = np.polyfit(steps[38:75], y_centres_of_mass[38:75], 1)

velocity = np.sqrt(x_slope**2 + y_slope**2)

fig, ax = plt.subplots()
plt.scatter(steps, x_centres_of_mass, marker = 'x', label = "x-axis (slope: " + str(round(x_slope, 4)) + ")", linewidth = 1)
plt.scatter(steps, y_centres_of_mass, marker = 'x', label = "y-axis (slope: " + str(round(y_slope, 4)) + ")", linewidth = 1)
plt.xlabel('Time Step')
plt.ylabel('Centre of Mass Position')
plt.title('Centre of Mass of Glider with Velocity ' + str(round(velocity,5)))
plt.legend()
plt.show()
