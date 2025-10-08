import matplotlib.pyplot as plt

free_energy_densities = []
steps = []

with open('free_energy_densities.txt', 'r') as file:
    # Skip the header line
    next(file)
    
    # Read each line in the file
    for line in file:
        # Split the line into columns using tab as delimiter
        columns = line.strip().split('\t')
        
        # Convert each column to the appropriate data type and append to the corresponding list
        step = float(columns[0])
        free_energy_density = float(columns[1])
        
        # Append values to the respective lists
        free_energy_densities.append(free_energy_density)
        steps.append(step)
        
plt.figure(figsize=(10, 6))
plt.plot(steps, free_energy_densities, marker='+', linewidth = 0)
plt.xlabel('Time (steps)')
plt.ylabel('Total Free Energy Density of Lattice')
plt.title('Free Energy Density vs Time')
plt.legend()
plt.grid(True)
plt.show()