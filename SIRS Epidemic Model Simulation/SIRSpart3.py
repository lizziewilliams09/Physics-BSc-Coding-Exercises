import numpy as np
import random



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
        
    def sweep(self):
        for n in range(self.size ** 2):
            self.update()
            
    def animate(self, frame, im):
        self.sweep()
        im.set_array(self.lattice)
        return im,
         
    def run(self, nsweeps):
        #list to store variables
        infected_sites = []
        
        for n in range(nsweeps):
            self.sweep()
            if n > 100: #wait 100 sweeps for equilibration
                infected_sites.append(self.infected_sites()) #store appropriate variable
        
        N = self.size**2
        average_fraction_infected_sites = np.mean(infected_sites)/N
        return average_fraction_infected_sites
    
    

if __name__ == "__main__":
    
    #note: approx 1.5 hours
    size = 50
    nsweeps = 1000
    p2 = 0.5
    resolution = 0.05    
    
    
    p_values = np.arange(0, 1, resolution)
    colour_plot_values = np.empty((len(p_values),len(p_values)))

    

    for i in range(len(p_values)):

        for j in range(len(p_values)):

            p1 = p_values[j]
            p3 = p_values[i]
            model = SIRS(size, p1, p2, p3)
            colour_plot_values[len(p_values)-1-i,j] = model.run(nsweeps)

        

    with open('SIRSpart3data.txt', 'w') as f:
        for i in range(len(p_values)):
            for j in range(len(p_values)):
                    f.write(f"{colour_plot_values[i,j]}\t")
            f.write("\n")
    
    
    


