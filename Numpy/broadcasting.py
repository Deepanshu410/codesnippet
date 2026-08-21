import numpy as np

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1], [2], [3], [4]])
array3 = np.array([[1,2,3,4], [5,6,7,8],[9,10,11,12], [13, 14, 15 ,16]])
array4 = np.array([[1], [2], [3], [4]])
print(array1 * array2)
print(array3 * array4)
# conditions, either;
print(array1.shape) # (1,4)
print(array2.shape) # (4,1)
#OR, this
print(array3.shape) # (4,4)
print(array4.shape) # (4,1)