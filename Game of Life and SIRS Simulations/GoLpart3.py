import numpy as np
import copy


class GameofLife(object):
    def __init__(self, size, condition):
        self.size = size
        self.grid = np.zeros((size, size))
        if condition == "random":
            self.grid = np.random.choice([0, 1], size=(size, size))
        elif condition == "oscillator":
            # Blinker oscillator
            self.grid[size // 2, size // 2 - 1] = 1
            self.grid[size // 2, size // 2] = 1
            self.grid[size // 2, size // 2 + 1] = 1
        elif condition == "glider":
            # Glider
            self.grid[size // 2, size // 2 - 1] = 1
            self.grid[size // 2, size // 2] = 1
            self.grid[size // 2, size // 2 + 1] = 1
            self.grid[size // 2 - 1, size // 2 + 1] = 1
            self.grid[size // 2 - 2, size // 2] = 1
            
    def update(self):
        new_grid = copy.deepcopy(self.grid)
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
                
    def centre_of_mass(self):
        x_point_positions = []
        y_point_positions = []
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i, j] == 1:
                    x_point_positions.append(i)
                    y_point_positions.append(j)
        if max(x_point_positions) - min(x_point_positions) < 5 and max(y_point_positions) - min(y_point_positions) < 5:
            x_com = np.sum(x_point_positions)/len(x_point_positions)
            y_com = np.sum(y_point_positions)/len(y_point_positions)
        else:
            x_com = 0
            y_com = 0
        return x_com, y_com    
        
    def run(self, nsteps):
        x_centres_of_mass = []
        y_centres_of_mass = []
        steps = []
        for step in range(nsteps):
            self.update()
            if step%4 == 0:
                x_com, y_com = self.centre_of_mass()
                if x_com != 0:
                    steps.append(step)
                    x_centres_of_mass.append(x_com)
                    y_centres_of_mass.append(y_com)
        return steps, x_centres_of_mass, y_centres_of_mass

if __name__ == "__main__":
    
    #note: very quick to run

    condition = "glider"
    size = 50
    nsteps = 300
    
    model = GameofLife(size, condition)
    steps, x_centres_of_mass, y_centres_of_mass = model.run(nsteps)
    
    with open('GoLpart3data.txt', 'w') as f:
        f.write("steps\tx-axis\ty-axis\n")
        for i in range(len(steps)):
            f.write(f"{steps[i]}\t{x_centres_of_mass[i]}\t{y_centres_of_mass[i]}\n")
