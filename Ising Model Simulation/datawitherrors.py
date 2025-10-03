# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 17:21:59 2024

@author: eccwi
"""

import numpy as np
import random

class IsingModel(object):
    def __init__(self, size, temperature, dynamics, lattice):
        self.size = size
        self.temperature = temperature
        self.dynamics = dynamics
        self.lattice = lattice

    def glauber_update(self):
        #pick random site (i,j)
        i = random.randint(0, self.size - 1)
        j = random.randint(0, self.size - 1)
        
        delta_E = self.delta_E(i,j) #find change in energy
        
        if delta_E <= 0 or random.random() < np.exp(-delta_E / self.temperature): #glauber conditions for updating lattice
            self.lattice[i, j] *= -1 #flip the sign of the randomly chosen site
    
    def kawasaki_update(self):
        #pick random sites (i1. j1) and (i2. j2)
        i1 = random.randint(0, self.size - 1)
        j1 = random.randint(0, self.size - 1)
        i2 = random.randint(0, self.size - 1)
        j2 = random.randint(0, self.size - 1)
        
        while self.lattice[i1, j1] == self.lattice[i2, j2]: #if the two sites have the same sign, repick until they are different
            i1 = random.randint(0, self.size - 1)
            j1 = random.randint(0, self.size - 1)
            i2 = random.randint(0, self.size - 1)
            j2 = random.randint(0, self.size - 1)
        
        #if the two sites are nearest neighbours, include a nearest neighbour correction to avoid over counting in energy change
        if [i1, j1] in [[(i2+1)%self.size, j2], [(i2-1)%self.size, j2], [i2, (j2+1)%self.size], [i2, (j2-1)%self.size]]:
           nearest_neighbour_correction = 2 * self.lattice[i1, j1] * self.lattice[i2, j2]
        else:
            nearest_neighbour_correction = 0
        
        delta_E = self.delta_E(i1,j1) + self.delta_E(i2,j2) - nearest_neighbour_correction #find change in energy 
        
        if delta_E <= 0 or random.random() < np.exp(-delta_E / self.temperature): #kawasaki conditions for updating lattice
            self.lattice[i1, j1], self.lattice[i2, j2] = self.lattice[i2, j2], self.lattice[i1, j1] #switch the signs of the two sites
    
    def nearest_neighbours(self, i, j): #gives the sign values of the nearest neighbours of (i,j)
        return [self.lattice[(i+1)%self.size, j],
                self.lattice[(i-1)%self.size, j],
                self.lattice[i, (j+1)%self.size],
                self.lattice[i, (j-1)%self.size]]
    
    def delta_E(self, i, j): #finds change in energy if the sign of a site is flipped
        return 2 * self.lattice[i, j] * np.sum(self.nearest_neighbours(i, j))
    
    def magnetization(self):
        return np.sum(self.lattice) #magnetization is the sum of all signs in the lattice
     
    def total_energy(self): #total energy is sum over all multiplied values of nearest neighbour pairs
        total_energy = 0
        for i in range(self.size):
            for j in range(self.size):
                total_energy -= self.lattice[i, j] * np.sum(self.nearest_neighbours(i, j))
        return total_energy / 2 #divide by two since we are overcounting each pair twice
    
    def susceptibility(self, magnetizations, magnetizationssquared):
        return (1/((self.size ** 2) * self.temperature)) * (np.mean(magnetizationssquared) - np.mean(magnetizations) ** 2)
    
    def heat_capacity(self, energies, energiessquared):
        return (1/((self.size ** 2) * (self.temperature ** 2))) * (np.mean(energiessquared) - np.mean(energies) ** 2)  
    
    def sweep(self):  #one sweep is n updates, where n is the number of sites in the lattice
        for n in range(self.size ** 2):
            if self.dynamics == 'Glauber':
                self.glauber_update()
            elif self.dynamics == 'Kawasaki':
                self.kawasaki_update()
                
    def bootstrap_error(self, variables, formula, k):
        #lists to store observables
        bootstrap_observables = []
        bootstrap_observablessquared = []

        number_of_measurements = len(variables)
        
        for i in range(k): #repeat resampling and observable calculating k times
            resampled_variables = []
            resampled_variablessquared = []
            
            for i in range(number_of_measurements):
                n = random.randint(0, number_of_measurements - 1) #select a random index 
                resampled_variables.append(variables[n]) #use index to randomly pick (resample) from list of variables and store it
                resampled_variablessquared.append(variables[n] ** 2)
            
            #calculate the observable based on list of resampled variables
            if formula == 'susceptibility':
                bootstrap_observable = self.susceptibility(resampled_variables, resampled_variablessquared)
            elif formula == 'heat capacity':
                bootstrap_observable = self.heat_capacity(resampled_variables, resampled_variablessquared)
            
            #store the observable
            bootstrap_observables.append(bootstrap_observable)
            bootstrap_observablessquared.append(bootstrap_observable ** 2)
    
        #find error using the mean and mean squared of the different observables (bootstrap method)
        error = np.sqrt(np.mean(bootstrap_observablessquared) - (np.mean(bootstrap_observables) ** 2))
        return error
        
    def run(self, nsweeps, k):
        #lists to store variables
        magnetizations = []
        abs_magnetizations = []
        magnetizationssquared = []
        energies = []
        energiessquared = []
        
        for n in range(nsweeps):
            self.sweep()
            if n > 100 and n%10 == 0: #wait 100 sweeps for equilibration and store variables every 10 sweeps to avoid correlation between measurements 
                #store appropriate variables
                magnetizations.append(self.magnetization())
                abs_magnetizations.append(np.abs(self.magnetization()))
                magnetizationssquared.append(self.magnetization() ** 2)
                energies.append(self.total_energy())
                energiessquared.append(self.total_energy() ** 2)
        
        #calculate the relevant observables using the stored data 
        average_M = np.mean(abs_magnetizations)
        average_E = np.mean(energies)
        susceptibility = self.susceptibility(magnetizations, magnetizationssquared)
        heat_capacity = self.heat_capacity(energies, energiessquared)
        
        #find errors using bootstrap methods
        susceptibility_error = self.bootstrap_error(magnetizations, 'susceptibility', k)
        heatcapacity_error = self.bootstrap_error(energies, 'heat capacity', k)
        
        return average_M, susceptibility, susceptibility_error, average_E, heat_capacity, heatcapacity_error, self.lattice
    
if __name__ == "__main__":
    
    size = 50
    temperatures = np.arange(1.0, 3.1, 0.1)
    nsweeps = 10000 #number of sweeps for each temperature
    k = 1000 #for bootstrap error
    
    dynamics_list = ['Glauber', 'Kawasaki']
    
    for dynamics in dynamics_list:
    
        magnetization_values = []
        susceptibility_values = []
        energy_values = []
        heat_capacity_values = []
        heatcapacity_error_values = []
        susceptibility_error_values = []
        
        r = random.random()
        if dynamics == 'Glauber':
            if r < 0.5: s = 1
            else: s = -1
            lattice = np.full((size, size), s)
        elif dynamics == 'Kawasaki':
            if r < 0.25: lattice = np.concatenate((np.full((size, int(size/2)), 1), np.full((size, int(size/2)), -1)), axis=1)
            elif r < 0.5: lattice = np.concatenate((np.full((size, int(size/2)), -1), np.full((size, int(size/2)), 1)), axis=1)
            elif r < 0.75: lattice = np.concatenate((np.full((int(size/2), size), 1), np.full((int(size/2), size), -1)), axis=0)
            else: lattice = np.concatenate((np.full((int(size/2), size), -1), np.full((int(size/2), size), 1)), axis=0)
    
        for temperature in temperatures:
            model = IsingModel(size, temperature, dynamics, lattice)
            average_M, susceptibility, susceptibility_error, average_E, heat_capacity, heatcapacity_error, lattice = model.run(nsweeps, k)  
            magnetization_values.append(average_M)
            susceptibility_values.append(susceptibility)
            energy_values.append(average_E)
            heat_capacity_values.append(heat_capacity)
            heatcapacity_error_values.append(heatcapacity_error)
            susceptibility_error_values.append(susceptibility_error)
            
        name = dynamics + ".txt"
        
        f = open(name, 'w')
            
        with open(name, 'w') as file:
            file.write("Temperature\tMagnetization\tSusceptibility\tEnergy\tHeat_Capacity\tHeat_Capacity_Error\tSusceptibility_Error\n")    
            for i in range(len(temperatures)): # Write data for each temperature
                file.write(f"{temperatures[i]}\t{magnetization_values[i]}\t{susceptibility_values[i]}\t{energy_values[i]}\t{heat_capacity_values[i]}\t{heatcapacity_error_values[i]}\t{susceptibility_error_values[i]}\n")
