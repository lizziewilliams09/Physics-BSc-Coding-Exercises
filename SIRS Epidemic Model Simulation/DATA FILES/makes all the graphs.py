import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import colors

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


# The following section (currently commented out) attempts to automatically identify the
# minimum immunity fraction required to stop the infection spreading. It was left out
# because the calculation can fail or give unstable results when the data is noisy or
# when the infected fraction never exactly reaches zero. The threshold can be determined
# visually from the scatter plot as well.

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
