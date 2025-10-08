import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

with open('potential_cut.txt', 'r') as file:
    text = file.readlines()
    size = int(len(text))
    
potential_cut = np.empty((size,size))
Ex_cut = np.empty((size,size))
Ey_cut = np.empty((size,size))


with open('potential_cut.txt', 'r') as file:    
    i = 0
    # Read each line in the file
    for line in file:
        # Convert each column to the appropriate data type and append to the corresponding list
        columns = line.strip().split('\t')
        for j in range(size):
            potential_cut[i,j] = float(columns[j])
        i += 1
        
with open('Ex_cut.txt', 'r') as file:    
    i = 0
    # Read each line in the file
    for line in file:
        # Convert each column to the appropriate data type and append to the corresponding list
        columns = line.strip().split('\t')
        for j in range(size):
            Ex_cut[i,j] = float(columns[j])
        i += 1

with open('Ey_cut.txt', 'r') as file:    
    i = 0
    # Read each line in the file
    for line in file:
        # Convert each column to the appropriate data type and append to the corresponding list
        columns = line.strip().split('\t')
        for j in range(size):
            Ey_cut[i,j] = float(columns[j])
        i += 1


#electric field vector plot
Ex_norm = np.empty((size,size))
Ey_norm = np.empty((size,size))

for i in range(size):
    for j in range(size):
        norm = np.sqrt(Ex_cut[i,j]**2 + Ey_cut[i,j]**2)
        if norm != 0:  # Ensure not dividing by zero
            Ex_norm[i,j] = Ex_cut[i,j] / norm
            Ey_norm[i,j] = Ey_cut[i,j] / norm
        else:
            Ex_norm[i,j] = 0
            Ey_norm[i,j] = 0     

Ex_norm[size//2,size//2] = 0
Ey_norm[size//2,size//2] = 0

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.quiver(
    Ey_norm[40:60,40:60], Ex_norm[40:60,40:60], scale = 22, width = 0.005)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Electric Field Vectors')

plt.show()



#potential colour plot
cmap = cm.inferno
fig, ax = plt.subplots()
im = ax.imshow(potential_cut, cmap=cmap)
fig.colorbar(im)
plt.title("Potential Distribution")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()