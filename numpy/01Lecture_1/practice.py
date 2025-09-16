import numpy as np
# Task 1: Create Arrays
# Create a 1D array with numbers from 1 to 10.
# Create a 2D array of size 3x3 filled with ones.
# Create a 3D array of shape 2x2x3 with random integers between 1 and 20.


# 1D array
array_1d = np.arange(1, 11)
print("1D Array:", array_1d)

# 2D array
array_2d = np.ones((3, 3))
print("2D Array:\n", array_2d)

# 3D array
array_3d = np.random.randint(1, 21,size=(2, 2, 3))
print("3D Array:\n", array_3d)



# Task 2: Array Attributes
# Given:

arr = np.array([[5,10,15],[20,25,30],[35,40,45]])
# Find its dimension, shape, size, and data type.

print(np.shape(arr))
print(np.ndim(arr))
print(np.size(arr)) 
print(arr.dtype)



# Task 3: Special Arrays
# Create an array of numbers from 50 to 100 with step 10.
# Create 8 equally spaced values between 0 and 2.
# Create a 5x5 identity matrix.


# Array from 50 to 100 with step 10
array_step = np.arange(50, 101, 10)
print(array_step)

# 8 equally spaced values between 0 and 2
array_linspace = np.linspace(0, 2, 8)
print(array_linspace)

# 5x5 identity matrix
identity_matrix = np.eye(5)
print(identity_matrix)

# Task 4: Basic Operations
# Given:

a = np.array([3,6,9,12])
b = np.array([1,2,3,4])
# Perform:
# Addition
# Subtraction
# Multiplication
# Division
# Square of each element


print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Square of each element in a:", a ** 2)
print("Square of each element in b:", b ** 2)



# Task 5: Indexing (1D)
# Given:

arr = np.array([5,10,15,20,25,30,35])
# Extract the first 4 elements.
# Extract the last 2 elements.
# Extract every second element.
# Change the element at index 3 to 100.

print("First 4 elements:", arr[:4])
print("Last 2 elements:", arr[-2:])
print("Every second element:", arr[::2])
arr[3] = 100
print("Array after changing index 3 to 100:", arr)


# Task 6: Indexing (2D)
# Given:

arr2d = np.array([[11,12,13],[21,22,23],[31,32,33]])
# Access element at row 1, column 2.
# Get the second row.
# Get the first column.

print("Element at row 1, column 2:", arr2d[1, 2])
print("Second row:", arr2d[1, :])
print("First column:", arr2d[:, 0])



# Task 7: Useful Functions
# Given:

arr = np.array([4,8,12,16,20,24])
# Find the minimum, maximum, sum, mean, and standard deviation.

print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))



# Task 8: Reshape Array
# Create an array with numbers from 1 to 12.
# Reshape it into a 3x4 matrix.
# Reshape it again into a 2x2x3 array.


arr_task8=np.arange(1, 13)
print("Original Array:", arr_task8)

print("Reshaped to 3x4:\n", arr_task8.reshape(3, 4))

print("Reshaped to 2x2x3:\n", arr_task8.reshape(2, 2, 3))




# Task 9: Compare List vs NumPy Speed 
# Create a Python list and a NumPy array with 1 million numbers.
# Add 5 to each element using both methods.
# Compare the execution time.






# Task 10: Bonus Challenge
# Generate a 4x4 random matrix with integers between 1 and 50.
# Find:
# Maximum element of each row
# Minimum element of each column
# The sum of all elements

random_matrix = np.random.randint(1, 51, size=(4, 4))
print("Random Matrix:\n", random_matrix)
print("Maximum element of each row:", np.max(random_matrix, axis=1))
print("Minimum element of each column:", np.min(random_matrix, axis=0))
print("total sum of all elements ",np.sum(random_matrix))