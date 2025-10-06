#~ takes about 6.2 hours (?? pause in between)
#last time took 2.6 hours
import numpy as np
import time

class GameofLife(object):
    def __init__(self, size):
        self.size = size
        self.grid = np.random.choice([0, 1], size=(size, size))

    def update(self):
        new_grid = np.copy(self.grid)
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i, j] == 1:
                    if self.neighbours(i, j) < 2 or self.neighbours(i, j) > 3:
                        new_grid[i, j] = 0
                elif self.grid[i, j] == 0:
                    if self.neighbours(i, j) == 3:
                        new_grid[i, j] = 1
        self.grid = new_grid
        
    
    def neighbours(self, i, j):
        neighbours = (self.grid[(i - 1) % self.size, (j - 1) % self.size]
                    + self.grid[(i - 1) % self.size, j % self.size]
                    + self.grid[(i - 1) % self.size, (j + 1) % self.size]
                    + self.grid[i % self.size, (j - 1) % self.size]
                    + self.grid[i % self.size, (j + 1) % self.size]
                    + self.grid[(i + 1) % self.size, (j - 1) % self.size]
                    + self.grid[(i + 1) % self.size, j % self.size]
                    + self.grid[(i + 1) % self.size, (j + 1) % self.size])
        return neighbours
                
         
    def run_until_equilibrium(self):
        active_sites = [np.sum(self.grid)]
        while True:
            prev_active_sites = active_sites[-10:]
            self.update()
            current_active_sites = np.sum(self.grid)
            if all(current_active_sites == prev for prev in prev_active_sites) or len(active_sites) > 5000:
                break
            active_sites.append(current_active_sites)
        if len(active_sites) <= 5000:
            time_to_equilibrium = len(active_sites) - 10
            return time_to_equilibrium 

if __name__ == "__main__":

    num_simulations = 1000
    size = 50

    equilibration_times = []
    
    total_time = 0
    for i in range(num_simulations):
        time1 = time.time()
        model = GameofLife(size)
        time_to_equilibrium = model.run_until_equilibrium()
        equilibration_times.append(time_to_equilibrium)
        time2 = time.time()
        part_n_time = time2 - time1
        total_time += part_n_time
        time_left = (total_time/(i+1))*(num_simulations - (i+1))
        if i%2 == 0:
            print("part " + str(i + 1) + " time: " + str(part_n_time))
            print("estimated time left: " + str(time_left))
            print("")
    
    print("total time: " + str(total_time))
    
    with open('GoLpart2data.txt', 'w') as f:
        f.write("Equilibration Times\n")
        for e_time in equilibration_times:
            f.write(f"{e_time}\n")

    

  