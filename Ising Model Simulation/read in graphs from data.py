# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 18:04:53 2024

@author: eccwi
"""

import matplotlib.pyplot as plt

dynamics_list = ['Glauber', 'Kawasaki']

for dynamics in dynamics_list:
    
    temperatures = []
    magnetization_values = []
    susceptibility_values = []
    energy_values = []
    heat_capacity_values = []
    heatcapacity_error_values = []
    susceptibility_error_values = []
    
    name = dynamics + ".txt"
    
    with open(name, 'r') as file:
        # Skip the header line
        next(file)
        
        # Read each line in the file
        for line in file:
            # Split the line into columns using tab as delimiter
            columns = line.strip().split('\t')
            
            # Convert each column to the appropriate data type and append to the corresponding list
            temperature = float(columns[0])
            magnetization = float(columns[1])
            susceptibility = float(columns[2])
            energy = float(columns[3])
            heat_capacity = float(columns[4])
            heatcapacity_error = float(columns[5])
            susceptibility_error = float(columns[6])
            
            # Append values to the respective lists
            temperatures.append(temperature)
            magnetization_values.append(magnetization)
            susceptibility_values.append(susceptibility)
            energy_values.append(energy)
            heat_capacity_values.append(heat_capacity)
            heatcapacity_error_values.append(heatcapacity_error)
            susceptibility_error_values.append(susceptibility_error)
            
    
    plt.figure(figsize=(10, 6))
    plt.plot(temperatures, magnetization_values, label=dynamics, marker='o', linewidth = 1)
    plt.xlabel('Temperature (K)')
    plt.ylabel('Average Absolute Magnetization')
    plt.title('Average Magnetization vs Temperature')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    plt.figure(figsize=(10, 6))
    plt.errorbar(temperatures, susceptibility_values, yerr=susceptibility_error_values, label=dynamics, marker='o', linewidth = 1, capsize = 1)
    plt.xlabel('Temperature (K)')
    plt.ylabel('Susceptibility')
    plt.title('Susceptibility vs Temperature')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    plt.figure(figsize=(10, 6))
    plt.plot(temperatures, energy_values, label=dynamics, marker='o', linewidth = 1)
    plt.xlabel('Temperature (K)')
    plt.ylabel('Average Energy')
    plt.title('Average Energy vs Temperature')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    plt.figure(figsize=(10, 6))
    plt.errorbar(temperatures, heat_capacity_values, yerr=heatcapacity_error_values, label=dynamics, marker='o', linewidth = 1, capsize = 1)
    plt.xlabel('Temperature (K)')
    plt.ylabel('Heat Capacity')
    plt.title('Heat Capacity vs Temperature')
    plt.legend()
    plt.grid(True)
    plt.show()