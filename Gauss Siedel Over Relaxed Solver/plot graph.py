import matplotlib.pyplot as plt

iterations_list = []
omegas = []

with open('gauss-siedel over relaxed.txt', 'r') as file:
    # Skip the header line
    next(file)
    
    # Read each line in the file
    for line in file:
        # Split the line into columns using tab as delimiter
        columns = line.strip().split('\t')
        
        # Convert each column to the appropriate data type and append to the corresponding list
        omega = float(columns[0])
        iterations = float(columns[1])
        
        # Append values to the respective lists
        iterations_list.append(iterations)
        omegas.append(omega)
        
plt.figure(figsize=(10, 6))
plt.plot(omegas, iterations_list)
plt.xlabel('ω')
plt.ylabel('Iterations')
plt.title('error = 1e-3')
plt.grid(True)
plt.show()