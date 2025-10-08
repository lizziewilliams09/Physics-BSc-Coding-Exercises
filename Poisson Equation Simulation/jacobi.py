import numpy as np
import matplotlib.pyplot as plt

class Jacobi_Algorithm(object):
    def __init__(self, size, dx):
        self.size = size

        self.dx = dx
        
        self.charge_distribution = np.zeros((size, size, size))
        
        # Place a 1 in the center of the array
        self.charge_distribution[size//2,size//2,size//2] = 1
        
        self.potential = np.zeros((self.size, self.size, self.size))

        self.error = float('inf')
        
    def update(self):
        new_potential = np.zeros_like(self.potential)
        
        # Roll the lattice in four directions
        neighbour_potential_sum = (np.roll(self.potential, shift=1, axis=0)
                                  + np.roll(self.potential, shift=-1, axis=0)
                                  + np.roll(self.potential, shift=1, axis=1)
                                  + np.roll(self.potential, shift=-1, axis=1)
                                  + np.roll(self.potential, shift=1, axis=2)
                                  + np.roll(self.potential, shift=-1, axis=2))     
        
        # Update the lattice
        new_potential = (1/6)*(neighbour_potential_sum + self.charge_distribution)
        
        # Add boundary conditions
        new_potential[:, :, 0] = 0
        new_potential[:, :, -1] = 0
        new_potential[:, 0, :] = 0 
        new_potential[:, -1, :] = 0
        new_potential[0, :, :] = 0
        new_potential[-1, :, :] = 0
        
        self.error = np.sum(np.abs(new_potential - self.potential))
        
        self.potential = new_potential
         
    def electric_field(self):
        Ex = (np.roll(self.potential, shift=1, axis=0) - np.roll(self.potential, shift=-1, axis=0))/(2*self.dx)
        Ey = (np.roll(self.potential, shift=1, axis=1) - np.roll(self.potential, shift=-1, axis=1))/(2*self.dx)
        Ez = (np.roll(self.potential, shift=1, axis=2) - np.roll(self.potential, shift=-1, axis=2))/(2*self.dx)

        return Ex, Ey, Ez
        
    def run(self, epsilon):
        i = 0
        while self.error > epsilon:
            self.update()
            i += 1
            
        Ex, Ey, Ez = self.electric_field()
        
        
        return self.potential, Ex, Ey, Ez
    


if __name__ == "__main__":
    size = int(input("Enter the size of the lattice: "))
    epsilon = float(input("Enter the value of desired accuracy: "))
    
    dx = 1

    
    model = Jacobi_Algorithm(size, dx)
    potential, Ex, Ey, Ez = model.run(epsilon)
    
    efield_strengths = []
    distances = []
    potentials = []
    
    for i in range(size):
        for j in range(size):
            for k in range(size):
                    efield_strengths.append(np.sqrt(Ex[i, j, k]**2 + Ey[i, j, k]**2 + Ez[i, j, k]**2))
                    center = np.array([size // 2, size // 2, size // 2])
                    distances.append(np.linalg.norm(np.array([i, j, k]) - center) * dx)
                    potentials.append(potential[i,j,k])

   
    
    with open('vs R.txt', 'w') as f:
        f.write("distance\te field strength\tpotential\n")
        for i in range(len(distances)):
            f.write(f"{distances[i]}\t{efield_strengths[i]}\t{potentials[i]}\n")

    potential_cut = potential[size//2, :, :]
    Ex_cut = Ex[:, :, size//2]
    Ey_cut = Ey[:, :, size//2]
     
    with open('potential_cut.txt', 'w') as f:
        for i in range(size):
            for j in range(size):
                    f.write(f"{potential_cut[i,j]}\t")
            f.write("\n")
    
    with open('Ex_cut.txt', 'w') as f:
        for i in range(size):
            for j in range(size):
                
                f.write(f"{Ex_cut[i,j]}\t")
            f.write("\n")
    
    with open('Ey_cut.txt', 'w') as f:
        for i in range(size):
            for j in range(size):

                f.write(f"{Ey_cut[i,j]}\t")
            f.write("\n")

