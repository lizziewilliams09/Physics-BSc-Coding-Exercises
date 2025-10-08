import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm

class IsingModel(object):
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
                
    def animate(self, frame, im):
        print(frame)
        self.update()
        im.set_array(self.lattice)
        return im,
         
    def run(self, nsteps, frequency):
        norm = plt.Normalize(vmin=-1, vmax=1)
        cmap = cm.coolwarm
        fig, ax = plt.subplots()
        im = ax.imshow(self.lattice, cmap=cmap, norm = norm)
        fig.colorbar(im)
        plt.title("Cahn-Hilliard equation")

        self.anim = animation.FuncAnimation(fig, self.animate, fargs = (im,), frames = nsteps, interval=frequency)
        plt.show()


if __name__ == "__main__":
    
        
    size = 100
    a = 0.1
    M = 0.1
    kappa = 0.1
    phi_initial = 0
    initial_random_noise = 0.1
    
    dx = 1
    dt = 2

    nsteps = 100000
    frequency = 100
    

    model = IsingModel(size, a, M, kappa, phi_initial, initial_random_noise, dx, dt)
    model.run(nsteps, frequency)

