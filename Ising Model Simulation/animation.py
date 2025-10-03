# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 17:21:59 2024

@author: eccwi
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import sys

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
        #pick random sites (i1, j1) and (i2, j2)
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
    
    def sweep(self):
        for n in range(self.size ** 2):
            if self.dynamics == 'Glauber':
                self.glauber_update()
            elif self.dynamics == 'Kawasaki':
                self.kawasaki_update()
                
    
    def animate(self, frame, im):
        self.sweep()
        im.set_array(self.lattice)
        return im,
         
    def run(self, nsteps, frequency):
        norm = plt.Normalize(vmin=-1, vmax=1)
        fig, ax = plt.subplots()
        im = ax.imshow(self.lattice,norm=norm)

        self.anim = animation.FuncAnimation(fig, self.animate, fargs = (im,), frames = nsteps, interval=frequency)
        plt.show()


if __name__ == "__main__":
    
    # Read input arguments
    args = sys.argv
    
    if (len(args) != 6):
        print("animation.py size temperature dynamics nsteps frequency")
        sys.exit(1)
        
    size = int(args[1])
    temperature = float(args[2])
    dynamics = str(args[3])
    nsteps = int(args[4])
    frequency = int(args[5])

    
    r = random.random()
    if dynamics == 'Glauber':
        if r < 0.5: s = 1
        else: s = -1
        lattice = (np.full((size, size), s))
    elif dynamics == 'Kawasaki':
        if r < 0.25: lattice = np.concatenate((np.full((size, int(size/2)), 1), np.full((size, int(size/2)), -1)), axis=1)
        elif r < 0.5: lattice = np.concatenate((np.full((size, int(size/2)), -1), np.full((size, int(size/2)), 1)), axis=1)
        elif r < 0.75: lattice = np.concatenate((np.full((int(size/2), size), 1), np.full((int(size/2), size), -1)), axis=0)
        else: lattice = np.concatenate((np.full((int(size/2), size), -1), np.full((int(size/2), size), 1)), axis=0)
    
    model = IsingModel(size, temperature, dynamics, lattice)
    model.run(nsteps, frequency)

