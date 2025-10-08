import numpy as np
import time

class Cahn_Hilliard(object):
    def __init__(self, size, a, M, kappa, phi_initial, initial_random_noise, dx, dt):
        self.size = size
        self.a = a
        self.M = M
        self.kappa = kappa
        self.dx = dx
        self.dt = dt
        
        self.lattice = np.random.normal(phi_initial, initial_random_noise, (size,size))

    def update(self):
        new_lattice = np.copy(self.lattice)
        
        # Roll the lattice in four directions
        rolled_lattice_up = np.roll(self.lattice, shift=1, axis=0)
        rolled_lattice_down = np.roll(self.lattice, shift=-1, axis=0)
        rolled_lattice_right = np.roll(self.lattice, shift=1, axis=1)
        rolled_lattice_left = np.roll(self.lattice, shift=-1, axis=1)
        
        # Calculate chemical potential terms for rolled lattices
        chemical_potential_sum = (self.chemical_potential(rolled_lattice_up)
                                  + self.chemical_potential(rolled_lattice_down)
                                  + self.chemical_potential(rolled_lattice_right)
                                  + self.chemical_potential(rolled_lattice_left)
                                  - 4 * self.chemical_potential(self.lattice))
        
        
        # Update the lattice
        new_lattice += (self.M * self.dt / self.dx**2) * chemical_potential_sum
        
        self.lattice = new_lattice
    
    def chemical_potential(self, lattice):
        # Roll the lattice in four directions
        rolled_lattice_up = np.roll(lattice, shift=1, axis=0)
        rolled_lattice_down = np.roll(lattice, shift=-1, axis=0)
        rolled_lattice_right = np.roll(lattice, shift=1, axis=1)
        rolled_lattice_left = np.roll(lattice, shift=-1, axis=1)
        
        mu = (-self.a*lattice
              + self.a*(lattice)**3
              - (self.kappa/(self.dx)**2)*(rolled_lattice_up + rolled_lattice_down + rolled_lattice_right + rolled_lattice_left - 4*lattice))
        return mu
    
    def free_energy_density(self):
        
        rolled_lattice_up = np.roll(self.lattice, shift=1, axis=0)
        rolled_lattice_down = np.roll(self.lattice, shift=-1, axis=0)
        rolled_lattice_right = np.roll(self.lattice, shift=1, axis=1)
        rolled_lattice_left = np.roll(self.lattice, shift=-1, axis=1)
        
        d_x_phi = (rolled_lattice_up - rolled_lattice_down)/(2*self.dx)
        d_y_phi = (rolled_lattice_right - rolled_lattice_left)/(2*self.dx)
        del_phi_squared = d_x_phi**2 + d_y_phi**2
        free_energy_lattice = -(self.a/2)*(self.lattice**2) + (self.a/4)*(self.lattice**4) + (self.kappa/2)*del_phi_squared
        
        total_free_energy = np.sum(free_energy_lattice)
        
        return total_free_energy
         
    def run(self, nsteps, frequency):
        free_energy_densities = []
        steps = []
        
        #time
        times = []
        part_times = []
        times.append(time.time())
        i = 1
        total_i = int(nsteps/frequency)
        
        self.update()
        free_energy_densities.append(self.free_energy_density())
        steps.append(0)
        
        for step in range(nsteps):
            self.update()
            if (step+1)%frequency == 0:
                free_energy_densities.append(self.free_energy_density())
                steps.append(step)
                
                #time
                print("part " + str(i) + "/" + str(total_i) + " complete")
                times.append(time.time())
                part_i_time = times[-1] - times[-2]
                part_times.append(part_i_time)
                print("time for part " + str(i) + ": " + str(part_i_time) + " secs") 
                time_left = np.mean(part_times) * (total_i - i)
                print("estimated time left: " + str(time_left/60) + " mins")
                i += 1
                
        return free_energy_densities, steps

if __name__ == "__main__":
    size = 100
    a = 0.1
    M = 0.1
    kappa = 0.1
    phi_initial = 0
    initial_random_noise = 0.1
    dx = 1
    dt = 1

    nsteps = 100000
    frequency = 1000
    
    model = Cahn_Hilliard(size, a, M, kappa, phi_initial, initial_random_noise, dx, dt)
    free_energy_densities, steps = model.run(nsteps, frequency)
        
    with open('free_energy_densities.txt', 'w') as file:
        file.write("Steps\tFree Energy Density\n")
        for i in range(len(free_energy_densities)): # Write data for each temperature
            file.write(f"{steps[i]}\t{free_energy_densities[i]}\n")

