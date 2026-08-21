import numpy as np
array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12], 
                  [13, 14, 15, 16]])

# array[start: end: step], subscript operator, end is exclusive and step is NOT exclusive
print(array[::2]) # row selection
print(array[:, ::]) # column selection, array[row, column]
print(array[:2, :2])
