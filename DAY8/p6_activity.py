import numpy as np

np.random.seed(32)
array = np.random.randint(1, 20, (3, 3))  # Generate a 3×3 random array
print("Original Array:\n", array)
print(np.mean(array))

# Manually finding elements < 10 and replacing them with 0
for i in range(array.shape[0]):  # Loop through rows
    for j in range(array.shape[1]):  # Loop through columns
        if array[i, j] < 10:  # If element is less than 10
            array[i, j] = 0  # Replace with 0

print("Modified Array:\n", array)
print(np.where(array==12))
            
