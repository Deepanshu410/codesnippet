# INTRO:
import numpy as np
array0 = np.array([1,2,3]) * 2
print(array0)

#MULTI-DIMENSIONAL ARRAYS:
array1 = np.array('A') # 0d array
array2 = np.array(['A', 'B', 'C']) # 1d array or vector
array3 = np.array([['A', 'B', 'C'], 
                   ['D', 'E', 'F'], 
                   ['G', 'H', 'I']]) # 2d array or matrix
array4 = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                   [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                   [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]]) # 3d array or tensor
# each of these lists, they need a consistent number of elements with each other
print(array1.ndim) # returns the number of array dimensions (also known as axes) as an integer
print(array4.shape) # this will return a tuple of integers. It shows, depth, the number of rows, and the number of coloumns

print(array4[0][0][0]) # called chain indexing, in python to acces index
print(array4[0,0,0]) # in numpy, we have to access through something called, mutli-dimensional indexing. 
