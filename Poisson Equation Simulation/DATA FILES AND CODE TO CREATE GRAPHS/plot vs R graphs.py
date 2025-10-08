import numpy as np
import matplotlib.pyplot as plt

efield_strengths = []
distances = []
potentials = []

with open('vs R.txt', 'r') as file:
    # Skip the header line
    next(file)
    
    # Read each line in the file
    for line in file:
        # Convert column to the appropriate data type
        columns = line.strip().split('\t')
        distance = float(columns[0])
        efield_strength = float(columns[1])
        potential = float(columns[2])
        
        # Append values to list
        distances.append(distance)
        efield_strengths.append(efield_strength)
        potentials.append(potential)

# Plotting potential vs distance
plt.figure(figsize=(10, 6))
plt.scatter(distances, potentials, label='Potential', color='blue')
plt.xlabel('Distance to charge')
plt.ylabel('Potential')
plt.title('Potential vs Distance to Charge')
plt.legend()
plt.grid(True)
plt.show()

distances_for_fit = []
potentials_for_fit = []

for i in range(len(distances)):
        if 0 < np.log(distances[i]) < 1.5:
            distances_for_fit.append(distances[i])
            potentials_for_fit.append(potentials[i])

x_slope_potential, intercept_potential = np.polyfit(np.log(distances_for_fit), np.log(potentials_for_fit), 1)

fit_line_x = np.linspace(0,4.5, 200)
fit_line_y = x_slope_potential * fit_line_x + intercept_potential

plt.figure(figsize=(10, 6))
plt.scatter(np.log(distances), np.log(potentials), label='Potential', color='blue')
plt.plot(fit_line_x, fit_line_y, label='Fit Line, slope: ' + str(x_slope_potential), color='red')
plt.xlabel('Distance to charge')
plt.ylabel('Potential')
plt.title('Potential vs Distance to Charge')
plt.legend()
plt.grid(True)
plt.show()


# Plotting electric field strength vs distance
plt.figure(figsize=(10, 6))
plt.scatter(distances, efield_strengths, label='Electric Field Strength', color='red')
plt.xlabel('Distance to charge')
plt.ylabel('Electric Field Strength')
plt.title('Electric Field Strength vs Distance to Charge')
plt.legend()
plt.grid(True)
plt.show()

distances_for_fit = []
efields_for_fit = []

for i in range(len(distances)):
        if 0 < np.log(distances[i]) < 1.5:
            distances_for_fit.append(distances[i])
            efields_for_fit.append(efield_strengths[i])

x_slope_efield, intercept_efield = np.polyfit(np.log(distances_for_fit), np.log(efields_for_fit), 1)

fit_line_x = np.linspace(0,4.5, 200)
fit_line_y = x_slope_efield * fit_line_x + intercept_efield

plt.figure(figsize=(10, 6))
plt.scatter(np.log(distances[1:]), np.log(efield_strengths[1:]), label='Electric Field Strength', color='red')
plt.plot(fit_line_x, fit_line_y, label='Fit Line, slope: ' + str(x_slope_efield), color='blue')
plt.xlabel('Distance to charge')
plt.ylabel('Electric Field Strength')
plt.title('Electric Field Strength vs Distance to Charge')
plt.legend()
plt.grid(True)
plt.show()



