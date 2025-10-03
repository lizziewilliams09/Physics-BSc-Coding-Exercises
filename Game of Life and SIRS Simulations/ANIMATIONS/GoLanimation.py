import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
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
                
    
    def animate(self, frame, im):
        self.update()
        im.set_array(self.grid)
        return im,
         
    def run(self, nsteps):
        norm = plt.Normalize(vmin=0, vmax=1)
        fig, ax = plt.subplots()
        im = ax.imshow(self.grid,norm=norm)

        self.anim = animation.FuncAnimation(fig, self.animate, fargs = (im,), frames = nsteps, interval=1)
        plt.show()


if __name__ == "__main__":
    
    
    # Read input arguments
    args = sys.argv
    
    if (len(args) != 3):
        print("%run GoLanimation.py size condition[random/oscillator/glider]")
        sys.exit(1)
    
    size = int(args[1])
    condition = str(args[2])
    nsteps = 10000
    
    model = GameofLife(size, condition)
    model.run(nsteps)

