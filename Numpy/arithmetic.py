import numpy as np

# Scalar(a linear algebra term, meaning a single value) arithmetic
array = np.array([1,2,3])
print(array ** 3)

# Vertorized(linear algebra term,is a single dimension) math functions: with this we can apply a function to an entire array without writing a loop
array = np.array([1.01, 2.5, 3.99])
print(np.sqrt(array))
print(np.round(array)) # to round normally
print(np.floor(array)) # to always round down
print(np.ceil(array)) # to always round down
print(np.pi) # returns pi

# Element-wise arithmetic; each operation is applied element by element between two arrays. 
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print(array1 * array2)

# Comparison operators; using this we can create boolean arrays, filter data, and use element-wise comparisons. 
scores = np.array([91, 55, 100, 70, 80])
print(scores >= 60)
scores[scores < 60] = 0 
print(scores)