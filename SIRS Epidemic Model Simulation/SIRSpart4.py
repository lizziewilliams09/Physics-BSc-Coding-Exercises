#takes ~ 3 hrs 15 mins

import numpy as np
import random
import time

class SIRS(object):
    def __init__(self, size, p1, p2, p3):
        self.size = size
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.lattice = np.random.choice([-1, 0, 1], size=(size, size))
        #I (infected) = -1
        #S (suscpetible) = 0
        #R (recovered) = 1
    
    def update(self):
        #pick random site (i,j)
        i = random.randint(0, self.size - 1)
        j = random.randint(0, self.size - 1)
        
        if self.lattice[i, j] == 0 and random.random() < self.p1 and -1 in self.nearest_neighbours(i, j):  
            self.lattice[i, j] = -1 
        elif self.lattice[i,j] == -1 and random.random() < self.p2:
            self.lattice[i,j] = 1
        elif self.lattice[i,j] == 1 and random.random() < self.p3:
            self.lattice[i,j] = 0
    
    def nearest_neighbours(self, i, j): #gives the sign values of the nearest neighbours of (i,j)
        return [self.lattice[(i+1)%self.size, j],
                self.lattice[(i-1)%self.size, j],
                self.lattice[i, (j+1)%self.size],
                self.lattice[i, (j-1)%self.size]]
                
    def infected_sites(self):
        infected_sites = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.lattice[i,j] == -1:
                    infected_sites += 1
        return infected_sites

    def bootstrap_error(self, variables, k):
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
            bootstrap_observable = (np.mean(resampled_variablessquared) - (np.mean(resampled_variables))**2)/(self.size**2)
            
            #store the observable
            bootstrap_observables.append(bootstrap_observable)
            bootstrap_observablessquared.append(bootstrap_observable ** 2)
    
        #find error using the mean and mean squared of the different observables (bootstrap method)
        error = np.sqrt(np.mean(bootstrap_observablessquared) - (np.mean(bootstrap_observables) ** 2))
        return error

        
    def sweep(self):
        for n in range(self.size ** 2):
            self.update()
            
    def animate(self, frame, im):
        self.sweep()
        im.set_array(self.lattice)
        return im,
         
    def run(self, nsweeps, k):
        #list to store variables
        infected_sites = []
        infected_sites_squared = []
        
        for n in range(nsweeps):
            self.sweep()
            if n > 100: #wait 100 sweeps for equilibration
                infected_sites.append(self.infected_sites()) #store appropriate variable
                infected_sites_squared.append(self.infected_sites() ** 2)       

        infected_sites_variance = (np.mean(infected_sites_squared) - (np.mean(infected_sites))**2)/(self.size**2)
        error = self.bootstrap_error(infected_sites, k)
        return infected_sites_variance, error
    
    

if __name__ == "__main__":

    size = 50
    nsweeps = 10000
    p2 = 0.5
    p3 = 0.5
    resolution = 0.025
    k = 1000 #for bootstrap error
    
    infected_sites_variances = []
    errors = []
    p1_values = np.linspace(0.2, 0.5, int(1/resolution))

    for p1 in p1_values:
        model = SIRS(size, p1, p2, p3)
        infected_sites_variance, error = model.run(nsweeps, k)
        infected_sites_variances.append(infected_sites_variance)
        errors.append(error)

    
    
    with open('SIRSpart4data.txt', 'w') as f:
        f.write("p1\tvariance\terror\n")
        for i in range(len(p1_values)):
            f.write(f"{p1_values[i]}\t{infected_sites_variances[i]}\t{errors[i]}\n")

