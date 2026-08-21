import numpy as np

# From Mulitdimensional arrays: Forming a 3 letter word using string concatenation (joining two or more sequential objects). 
array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                   [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                   [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]]) 
word = array[0,1,0] + array[1,1,2] + " " + array[0, 2, 2] + array[2,0,1]
print(word)

# Arithmetic: area of a circle through scalar and vectorized functions
radii = np.array([1,2,3])
print(np.pi * radii ** 2)

# Broadcasting: multiplication table via braodcasting
array1 = np.array([[1,2,3,4, 5,6, 7, 8, 9, 10]])
array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
print(array1 * array2)