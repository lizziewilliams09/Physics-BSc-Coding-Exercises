import numpy as np
import matplotlib.pyplot as plt

class Gauss_Siedel_Over_Relaxed(object):
    def __init__(self, size, dx, omega):
        self.size = size

        self.dx = dx
        self.omega = omega
        
        self.charge_distribution = np.zeros((self.size,self.size,self.size))
        # Place a 1 in the center of the array
        self.charge_distribution[size//2,size//2,size//2] = 1
        
        self.potential = np.zeros((self.size, self.size, self.size))

        self.error = float('inf')
        
    def update(self):
        old_potential = np.copy(self.potential)
        
        for i in range (self.size):
            for j in range(self.size):
                for k in range(self.size):
                    
                    self.potential[i,j,k] = ((1-self.omega)*self.potential[i,j,k]
                                             + (self.omega/6)*(self.potential[(i+1)%self.size, j, k]
                                                          + self.potential[(i-1)%self.size, j, k]
                                                          + self.potential[i, (j+1)%self.size, k]
                                                          + self.potential[i, (j-1)%self.size, k]
                                                          + self.potential[i, j, (k+1)%self.size]
                                                          + self.potential[i, j, (k-1)%self.size]
                                                          + self.charge_distribution[i,j,k] * self.dx**2))
        # Add boundary conditions
        self.potential[:, :, 0] = 0
        self.potential[:, :, -1] = 0
        self.potential[:, 0, :] = 0 
        self.potential[:, -1, :] = 0
        self.potential[0, :, :] = 0
        self.potential[-1, :, :] = 0
         
        self.error = np.sum(np.abs(self.potential - old_potential))
        
        
    def run(self, epsilon):
        iterations = 0
        while self.error > epsilon:
            self.update()
            iterations += 1
        return iterations


if __name__ == "__main__":
    size = 50
    epsilon = 1e-3 #0.0001
    dx = 1
    
    iterations_list = []
    omegas = np.arange(1.7, 1.98, 0.02)

    for omega in omegas:
        print("omega: " + str(omega))
        model = Gauss_Siedel_Over_Relaxed(size, dx, omega)
        iterations = model.run(epsilon)
        iterations_list.append(iterations)
        print("iterations: " + str(iterations))
    
    with open('gauss-siedel over relaxed.txt', 'w') as file:
        file.write("Omega\tIterations\n")
        for i in range(len(omegas)): 
            file.write(f"{omegas[i]}\t{iterations_list[i]}\n")

    
    