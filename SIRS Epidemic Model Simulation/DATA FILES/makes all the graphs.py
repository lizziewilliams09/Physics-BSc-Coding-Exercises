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

'''
SIRS Part 3 - Colour Plot in p1-p3 Plane
'''

with open('SIRSpart3data.txt', 'r') as file:
    text = file.readlines()
    number = int(len(text))
    
colour_plot_values = np.empty((number,number))

with open('SIRSpart3data.txt', 'r') as file:    
    i = 0
    # Read each line in the file
    for line in file:
        # Convert each column to the appropriate data type and append to the corresponding list
        columns = line.strip().split('\t')
        for j in range(number):
            colour_plot_values[i,j] = float(columns[j])
        i += 1
        
cmap = cm.gnuplot
fig, ax = plt.subplots()
im = ax.imshow(colour_plot_values, extent = [0,1,0,1], cmap=cmap)
plt.xlabel("p1")
plt.ylabel("p3")
fig.colorbar(im)
plt.title("Average Fraction of Infected Sites with p2 = 0.5")
plt.show()

'''
SIRS Part 4 - Variance of number of infected sites along cut
'''

infected_sites_variances = []
p1_values = []
errors = []

with open('SIRSpart4data.txt', 'r') as file:
    # Skip the header line
    next(file)
    
    # Read each line in the file
    for line in file:
        # Convert column to the appropriate data type
        columns = line.strip().split('\t')
        p1 = float(columns[0])
        infected_sites_variance = float(columns[1])
        error = float(columns[2])
        
        # Append values to list
        infected_sites_variances.append(infected_sites_variance)
        p1_values.append(p1)
        errors.append(error)
        
fig, ax = plt.subplots()        
plt.errorbar(p1_values, infected_sites_variances, yerr = errors, linewidth = 1, ecolor='red')
plt.xlabel("p1")
plt.ylabel("Variance of the Number of Infected Sites")
plt.title("Variance Along a Cut at Fixed p2 = p3 = 0.5")


'''
SIRS Part 5 - Plot to find the mininmum immunity fraction to prevent spread
'''

average_infected_fractions = []
immunity_fraction_values = []

with open('SIRSpart5data.txt', 'r') as file:
    # Skip the header line
    next(file)
    
    # Read each line in the file
    for line in file:
        # Convert column to the appropriate data type
        columns = line.strip().split('\t')
        immunity_fraction = float(columns[0])
        average_fraction_infected_sites = float(columns[1])
        
        # Append values to list
        immunity_fraction_values.append(immunity_fraction)
        average_infected_fractions.append(average_fraction_infected_sites)

'''
one_after_insufficient_immunity_fraction = []

for i in range(len(immunity_fraction_values)):
    if average_infected_fractions[i] > 0:
        one_after_insufficient_immunity_fraction.append(immunity_fraction_values[i+1])
        
min_immunity_fraction = one_after_insufficient_immunity_fraction[-1]

for i in range(len(immunity_fraction_values)) : 
    if average_infected_fractions[i] == 0:
        min_immunity_fraction = immunity_fraction_values[i]
        break
'''
 
fig, ax = plt.subplots()
plt.scatter(immunity_fraction_values, average_infected_fractions, marker = 'x', linewidth = 1)
#plt.axvline(min_immunity_fraction, label = "Min Immunity Fraction: " + str(round(min_immunity_fraction,3)), color = 'r')
plt.xlabel("Immunity Fraction")
plt.ylabel("Average Fraction of Infected States")
plt.title("Finding the Minimum Immunity Fraction to Prevent Spread")
#plt.legend()