#note: takes ~ 50 mins with 20 points
#should take ~ 4 hours with 100 points
   
import numpy as np
import random
import time

class SIRS(object):
    def __init__(self, size, p1, p2, p3, immunity_fraction):
        self.size = size
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        prob_SIR = (1-immunity_fraction)/3
        self.lattice = np.random.choice([-1, 0, 1, 2], size=(size, size), p = [prob_SIR, prob_SIR, prob_SIR, immunity_fraction])
        #I (infected) = -1
        #S (suscpetible) = 0
        #R (recovered) = 1
        #Immune = 2
    
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
    
    def nearest_neighbours(self, i, j): #gives the values of the nearest neighbours of (i,j)
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
        #list to store variable
        infected_sites = []
        
        for n in range(nsweeps):
            self.sweep()
            if n > 100: #wait 100 sweeps for equilibration
                infected_sites.append(self.infected_sites()) #store variable
        
        N = self.size**2
        average_fraction_infected_sites = np.mean(infected_sites)/N
        return average_fraction_infected_sites

if __name__ == "__main__":
    
    size = 50
    nsweeps = 10000
    p1 = p2 = p3 = 0.5 

    immunity_fraction_values = np.linspace(0,1,100)
    average_infected_fractions = []
    
    print(str(len(immunity_fraction_values)) + " parts")
    print("")
    
    total_time = 0
    i = 0
    for immunity_fraction in immunity_fraction_values:
        time1 = time.time()
        print(immunity_fraction)
        model = SIRS(size, p1, p2, p3, immunity_fraction)
        average_fraction_infected_sites = model.run(nsweeps)
        average_infected_fractions.append(average_fraction_infected_sites)
        time2 = time.time()
        part_n_time = time2 - time1
        total_time += part_n_time
        time_left = (total_time/(i+1))*(len(immunity_fraction_values) - (i+1))
        print("time: " + str(part_n_time))
        print("estimated time left: " + str(time_left))
        print("")
        i+=1
        
    print("total time: " + str(total_time))
        
    with open('SIRSpart5data.txt', 'w') as f:
        f.write("immunity fraction\taverage infected fraction\n")
        for i in range(len(immunity_fraction_values)):
            f.write(f"{immunity_fraction_values[i]}\t{average_infected_fractions[i]}\n")
    
    
    


