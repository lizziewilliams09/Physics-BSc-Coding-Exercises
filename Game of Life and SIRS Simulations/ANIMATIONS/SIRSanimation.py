import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.animation as animation
import random
import sys

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
                
    
    def sweep(self):
        for n in range(self.size ** 2):
            self.update()
            
    def animate(self, frame, im):
        self.sweep()
        im.set_array(self.lattice)
        return im,
         
    def run(self, nsweeps, frequency):
        norm = plt.Normalize(vmin=-1, vmax=1)
        cmap = cm.Spectral
        fig, ax = plt.subplots()
        im = ax.imshow(self.lattice, norm=norm, cmap=cmap)
        
        sirs_label = ["Infected", "Suscpetible", "Recovered"]
        colors = [im.cmap(im.norm(value)) for value in [-1,0,1]]
        patches = [mpatches.Patch(color=colors[i], label="{l}".format(l=sirs_label[i]) ) for i in range(len(sirs_label)) ]
        plt.legend(handles=patches, bbox_to_anchor=(1.4, 1), borderaxespad=0. )
       
        self.anim = animation.FuncAnimation(fig, self.animate, fargs = (im,), frames = nsweeps, interval=frequency)
        plt.show()


if __name__ == "__main__":
    
    # Read input arguments
    args = sys.argv
    
    if (len(args) != 5):
        print("%run SIRSanimation.py size p1 p2 p3")
        sys.exit(1)
        
    size = int(args[1])
    p1 = float(args[2])
    p2 = float(args[3])
    p3 = float(args[4])
    nsweeps = 1000
    frequency = 1
        
    model = SIRS(size, p1, p2, p3)
    model.run(nsweeps, frequency)


